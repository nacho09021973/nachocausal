"""dev/sweep_ensemble.py — full-ensemble EXPLORATION sweep on CPU or GPU.

OFF the sealed validation path. Runs the blind, order-only stage of the pipeline
(numpy point cloud -> past matrix -> estimate_O -> two_means_split `sep`) for both
BH and MINK across the 4 frozen intensities and a chosen seed set, then aggregates
the separation signal d = sep_BH - sep_MINK per intensity and reports timing.

This is NOT validate.run: it never reveals coordinates to a scorer, never applies
the frozen PASS/FAIL thresholds, and writes no verdict. It exists to explore the
order-only signal at scale and to time the GPU pipeline end-to-end. The sealed
verdict is produced ONLY by `python -m nachocausal.validate` in the sealed CPU
venv (numpy==1.26.4).

Run on a GPU box:   dev/run-gpu.sh-style launch, e.g.
    LD_LIBRARY_PATH=/usr/lib/wsl/lib PYTHONPATH=. .venv-gpu/bin/python \
        -m dev.sweep_ensemble --device auto --seeds dev
Or simply:          dev/run-sweep.sh --device auto --seeds dev
CPU-only machine:   PYTHONPATH=. .venv/bin/python -m dev.sweep_ensemble --device cpu --seeds dev
"""

from __future__ import annotations

import argparse
import json
import os
import time
from datetime import datetime, timezone

import numpy as np

from nachocausal import estimator, generator, thresholds
from dev import backend

# Raw per-seed sweep output goes here (git-ignored; see .gitignore).
RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dev_ensemble_raw")


def _seed_set(name: str):
    if name == "dev":
        return list(thresholds.DEV_SEEDS)
    if name == "validation":
        return list(thresholds.VALIDATION_SEEDS)
    return [int(s) for s in name.split(",") if s.strip()]


def _free_gpu(device_name: str) -> None:
    """Release pooled GPU memory between seeds so large-N sweeps don't OOM."""
    if device_name == "gpu":
        import cupy as cp
        cp.get_default_memory_pool().free_all_blocks()


def _sep_for(emb, kind, device):
    """Blind order-only sep for one cloud+kind: matrix -> O -> two_means_split."""
    C, dev = backend.past_matrix(emb, kind, device=device)
    O_by_min, _min, _Lfut, _ = backend.estimate_O(C, device=device)
    del C
    _, sep = estimator.two_means_split(list(O_by_min.values()))  # tiny, host numpy
    return sep, dev


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--device", default="auto", choices=["auto", "cpu", "gpu"])
    ap.add_argument("--seeds", default="dev",
                    help="'dev' (8) | 'validation' (20) | comma list of ints")
    ap.add_argument("--intensities", default="",
                    help="comma list; default = the 4 frozen thresholds.INTENSITIES")
    ap.add_argument("--out", default="",
                    help="JSON output path; default dev_ensemble_raw/sweep_<seeds>_"
                         "<device>_<UTC>.json. Pass 'none' to skip writing.")
    args = ap.parse_args()

    seeds = _seed_set(args.seeds)
    intensities = ([float(x) for x in args.intensities.split(",") if x.strip()]
                   or list(thresholds.INTENSITIES))

    print(f"EXPLORATION sweep (NOT a verdict) | device={args.device} | "
          f"seeds={args.seeds} (n={len(seeds)}) | intensities={intensities}")
    print(f"{'intensity':>9} {'N_mean':>7} {'seeds':>5} {'sepBH':>7} {'sepMK':>7} "
          f"{'mean d':>7} {'med d':>7} {'d>0':>5} {'secs':>7}")
    print("-" * 72)

    dev_used = args.device
    per_seed = []      # flat raw records, one per (intensity, seed)
    per_level = []     # aggregates per intensity
    t_all = time.perf_counter()
    for lam in intensities:
        t0 = time.perf_counter()
        Ns, sBH, sMK = [], [], []
        for s in seeds:
            emb, edges, center = generator.numpy_sprinkle(s, lam)
            generator.assert_coordinate_uniform(emb, edges, center)
            N = int(emb.shape[0])
            sb, dev_used = _sep_for(emb, "BH", args.device)
            sm, dev_used = _sep_for(emb, "MINK", args.device)
            Ns.append(N)
            sBH.append(sb)
            sMK.append(sm)
            per_seed.append({"intensity": lam, "seed": int(s), "N": N,
                             "sep_BH": float(sb), "sep_MINK": float(sm),
                             "d": float(sb - sm)})
            _free_gpu(dev_used)
        sBH, sMK = np.array(sBH), np.array(sMK)
        d = sBH - sMK
        secs = time.perf_counter() - t0
        agg = {"intensity": lam, "N_mean": float(np.mean(Ns)), "n_seeds": len(seeds),
               "mean_sep_BH": float(np.nanmean(sBH)), "mean_sep_MINK": float(np.nanmean(sMK)),
               "mean_d": float(np.nanmean(d)), "median_d": float(np.nanmedian(d)),
               "n_d_positive": int(np.sum(d > 0)), "secs": secs}
        per_level.append(agg)
        print(f"{lam:>9.0f} {agg['N_mean']:>7.0f} {len(seeds):>5} "
              f"{agg['mean_sep_BH']:>7.3f} {agg['mean_sep_MINK']:>7.3f} "
              f"{agg['mean_d']:>7.3f} {agg['median_d']:>7.3f} "
              f"{agg['n_d_positive']:>3}/{len(seeds):<1} {secs:>7.1f}")

    total = time.perf_counter() - t_all
    print("-" * 72)
    print(f"device={dev_used}  total wall time = {total:.1f} s")
    print("NOTE: exploration only. d = sep_BH - sep_MINK is the raw order-only "
          "signal; PASS/FAIL needs the sealed CPU runner (nachocausal.validate).")

    if args.out.lower() == "none":
        return
    if args.out:
        path = args.out
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    else:
        os.makedirs(RAW_DIR, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        path = os.path.join(RAW_DIR, f"sweep_{args.seeds}_{dev_used}_{stamp}.json")
    payload = {
        "kind": "exploration_sweep",  # NOT a sealed verdict
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "device": dev_used,
        "numpy_version": np.__version__,
        "seeds_label": args.seeds,
        "seeds": [int(s) for s in seeds],
        "intensities": intensities,
        "total_secs": total,
        "per_level": per_level,
        "per_seed": per_seed,
    }
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print(f"raw per-seed results written: {path}  "
          f"({len(per_seed)} records, {len(per_level)} levels)")


if __name__ == "__main__":
    main()
