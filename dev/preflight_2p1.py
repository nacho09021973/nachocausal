"""prereg-004 step 5 pre-flight (comité 052 §9), CPU only, on BURNED exploration seeds.

Plan declared before running: dev/PREREG004_STEP_5_2026-10-13.md.

Mode 1 (default): for each seed, run the candidate package's blind chain on CPU exactly as
nachocausal2p1.validate does (generate with validity checks and the 20000-pair audit, then the
order-only estimate, then the bracket) and compare it with the GPU record of the same seed in
dev/2p1_sweep_T_rho126_v2_2026-10-12.jsonl (T=16, rho=126). Only match flags, counts, hashes and
timings are written; no width, bracket end or theta value is written or printed (comité 052,
leakage (c)).
Mode 2 (--threads-probe SEED): generate SEED and print the sha256 of both packed orders, to be
run once with NUMBA_NUM_THREADS=1 and compared with the mode-1 hash (default threads).

Usage (.venv, CPU):
  .venv/bin/python dev/preflight_2p1.py --out dev/preflight_2p1_2026-10-13.jsonl
  NUMBA_NUM_THREADS=1 .venv/bin/python dev/preflight_2p1.py --threads-probe 7000100
"""
import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

import numba
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nachocausal import estimator as sealed  # noqa: E402
from nachocausal2p1 import estimator, generator, thresholds, validate  # noqa: E402
from nachocausal2p1.scoring import blind_bracket  # noqa: E402

DEV_GPU = ROOT / "dev" / "2p1_sweep_T_rho126_v2_2026-10-12.jsonl"
RHO = 126


def _sha(order):
    return hashlib.sha256(np.packbits(order).tobytes()).hexdigest()


def _dev_records():
    out = {}
    for line in open(DEV_GPU):
        rec = json.loads(line)
        if rec["T_EDGE"] == thresholds.T_EDGE and rec["rho"] == float(RHO):
            out[rec["seed"]] = rec
    return out


def _quartiles(vals):
    return np.quantile(np.asarray(vals), [0, .25, .5, .75, 1]).astype(int).tolist()


def _compare(kind, e, br, dev):
    """Match flags port(CPU) vs dev(GPU) for one kind. Values themselves are not returned."""
    vals = [e["O_by_min"][i] for i in e["min_idx"]]
    _, raw_sep = sealed.two_means_split(vals)            # dev records sep before abstention
    m = {"n_minimal": e["n_minimal"] == dev["n_minimal"],
         "O_quartiles": _quartiles(vals) == dev["O_quartiles"],
         "improvement": round(e["improvement"], 4) == dev["improvement"],
         "sep": round(float(raw_sep), 3) == dev["sep"],
         "abstain": e["abstained"] == dev["abstain"]}
    if kind == "BH":
        m["claimed"] = bool(br["valid"]) == dev["claimed"]
        if dev["claimed"] and br["valid"]:
            m["r_lo"] = br["r_lo"] == dev["r_lo"]
            m["r_hi"] = br["r_hi"] == dev["r_hi"]
            m["covers_2M"] = br["covers"] == dev["covers_2M"]
    return m


def run_seed(seed, dev):
    t0 = time.time()
    g = validate.generate(seed, RHO)
    t_gen = time.time() - t0
    row = {"seed": seed, "rho": RHO, "T_EDGE": thresholds.T_EDGE, "device": "cpu",
           "numba_threads": numba.get_num_threads(),
           "N": int(g["t"].size), "invalid": g["invalid"], "invalid_reasons": g["reasons"],
           "audit_vs_fine": g["stats"].get("audit_vs_fine"),
           "transitivity_violations_BH": g["stats"].get("transitivity_violations_BH"),
           "radial_check_mismatches": g["stats"].get("radial_check_mismatches"),
           "seconds_generate_with_checks": round(t_gen, 1)}
    if g["bh"] is None:
        row["seconds_total"] = round(time.time() - t0, 1)
        return row
    row["order_sha_BH"], row["order_sha_MINK"] = _sha(g["bh"]), _sha(g["mk"])
    t1 = time.time()
    est = {k: estimator.estimate(o, guard=True, guard_seed=seed)
           for k, o in (("BH", g["bh"]), ("MINK", g["mk"]))}
    br = blind_bracket(est["BH"]["O_by_min"], est["BH"]["min_idx"], est["BH"]["thr"], g["r"]) \
        if not est["BH"]["abstained"] else {"valid": False}
    row["seconds_estimate"] = round(time.time() - t1, 1)
    row["seconds_total"] = round(time.time() - t0, 1)
    if dev is not None:
        row["dev_gpu_seconds"] = dev["gen_seconds"]
        match = {"N": row["N"] == dev["n"]}
        for k in ("BH", "MINK"):
            match.update({f"{k}.{f}": v for f, v in _compare(k, est[k], br, dev[k]).items()})
        row["match_vs_gpu"] = match
        row["all_match"] = all(match.values())
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--seeds", type=int, nargs="*", default=list(thresholds.DRY_RUN_SEEDS))
    ap.add_argument("--threads-probe", type=int)
    a = ap.parse_args()
    thresholds.assert_environment()
    for s in ([a.threads_probe] if a.threads_probe else a.seeds):
        assert s in thresholds.DRY_RUN_SEEDS, "burned exploration seeds only"
    if a.threads_probe:
        g = validate.generate(a.threads_probe, RHO)
        print(json.dumps({"seed": a.threads_probe,
                          "numba_threads": numba.get_num_threads(),
                          "order_sha_BH": _sha(g["bh"]), "order_sha_MINK": _sha(g["mk"])}))
        return
    dev = _dev_records()
    with open(a.out, "a") as f:
        for s in a.seeds:
            row = run_seed(s, dev.get(s))
            f.write(json.dumps(row) + "\n")
            f.flush()
            print(json.dumps({k: row.get(k) for k in ("seed", "N", "invalid", "all_match",
                                                       "seconds_total")}), flush=True)


if __name__ == "__main__":
    main()
