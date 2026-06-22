"""Formula density sweep using the C++ volume kernel.

Python remains responsible for sprinkling, tau-gate semantics, aggregation, and
artifact writing. C++ computes the heavy order-derived volume observable without
materializing the full N x N past matrix.
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path
from typing import Iterable

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from nachocausal import gate, generator, thresholds, validate

CPP_SRC = ROOT / "cpp" / "formula_volume_kernel.cpp"
CPP_BIN = ROOT / "cpp" / "formula_volume_kernel"
DEFAULT_INTENSITIES = (1500.0, 3000.0, 6000.0, 12000.0, 24000.0)
FORMULA_SEED_LOW = 4_000_000
FORMULA_SEED_HIGH = 5_000_000
FORMULA_DRAW_SEED = 20260623
_TAU_EXTENSION_CACHE: dict[tuple[int, int], float] = {}


def draw_formula_seeds(count: int, draw_seed: int = FORMULA_DRAW_SEED) -> tuple[int, ...]:
    rng = np.random.default_rng(draw_seed)
    seeds = rng.choice(np.arange(FORMULA_SEED_LOW, FORMULA_SEED_HIGH), count, replace=False)
    return tuple(int(x) for x in sorted(seeds))


def ensure_kernel(force: bool = False) -> Path:
    if force or not CPP_BIN.exists() or CPP_BIN.stat().st_mtime < CPP_SRC.stat().st_mtime:
        cmd = [
            "g++",
            "-O3",
            "-std=c++17",
            "-march=native",
            str(CPP_SRC),
            "-o",
            str(CPP_BIN),
        ]
        subprocess.run(cmd, cwd=ROOT, check=True)
    return CPP_BIN


def run_kernel(embedding: np.ndarray, kernel: Path) -> dict:
    lines = [str(int(embedding.shape[0]))]
    lines.extend(f"{t:.17g} {r:.17g}" for t, r in embedding)
    payload = "\n".join(lines) + "\n"
    proc = subprocess.run(
        [str(kernel)],
        input=payload,
        text=True,
        capture_output=True,
        check=True,
    )
    return json.loads(proc.stdout)


def per_seed(seed: int, intensity: float, kernel: Path) -> dict:
    emb, edges, center = generator.numpy_sprinkle(seed, intensity, thresholds.T_EDGE)
    generator.assert_coordinate_uniform(emb, edges, center)
    out = run_kernel(emb, kernel)
    bh = out["BH"]
    mk = out["MINK"]
    tau_bh = formula_tau(int(bh["n_min"]))
    tau_mk = formula_tau(int(mk["n_min"]))
    abst_bh = int(bh["n_min"]) < 2 or bh["improvement"] < tau_bh
    abst_mk = int(mk["n_min"]) < 2 or mk["improvement"] < tau_mk
    sep_bh = 0.0 if abst_bh else bh["sep"]
    sep_mk = 0.0 if abst_mk else mk["sep"]

    br = bh["bracket"]
    if abst_bh:
        br = {
            "valid": False,
            "r_lo": None,
            "r_hi": None,
            "width": None,
            "midpoint": None,
            "covers": False,
            "clean": False,
        }

    width = none_to_nan(br["width"])
    midpoint = none_to_nan(br["midpoint"])
    center_error = abs(midpoint - thresholds.R_S) if np.isfinite(midpoint) else float("nan")

    return {
        "lambda": float(intensity),
        "seed": int(seed),
        "N": int(out["N"]),
        "n_min_BH": int(bh["n_min"]),
        "improvement_BH": float(bh["improvement"]),
        "tau_n_BH": tau_bh,
        "abstained_BH": bool(abst_bh),
        "r_lo": none_to_nan(br["r_lo"]),
        "r_hi": none_to_nan(br["r_hi"]),
        "width": width,
        "width_over_2M": width / thresholds.TWO_M if np.isfinite(width) else float("nan"),
        "midpoint": midpoint,
        "center_error": center_error,
        "covers": bool(br["covers"]),
        "clean": bool(br["clean"]),
        "sep_BH": float(sep_bh),
        "sep_MINK": float(sep_mk),
        "d": float(sep_bh - sep_mk),
        "n_min_MINK": int(mk["n_min"]),
        "improvement_MINK": float(mk["improvement"]),
        "tau_n_MINK": tau_mk,
        "abstained_MINK": bool(abst_mk),
    }


def formula_tau(n: int, reps: int = thresholds.GATE_NULL_MC_REPS) -> float:
    """Formula-branch tau(n), extending beyond the sealed fixture if needed.

    For n within the sealed table, this delegates to nachocausal.gate.tau. For
    higher n reached by formula-only density sweeps, it computes a deterministic
    data-independent Uniform[0,1] Monte Carlo quantile. This does not modify the
    sealed fixture or validation path.
    """

    if n < 2:
        return float("nan")
    try:
        return gate.tau(n)
    except ValueError:
        key = (n, reps)
        if key not in _TAU_EXTENSION_CACHE:
            _TAU_EXTENSION_CACHE[key] = tau_extension_mc(n, reps)
        return _TAU_EXTENSION_CACHE[key]


def tau_extension_mc(n: int, reps: int) -> float:
    rng = np.random.default_rng(thresholds.GATE_NULL_MC_SEED + 1_000_003 * n)
    draws = np.sort(rng.random((reps, n)), axis=1)
    total = draws.var(axis=1) * n
    csum = np.cumsum(draws, axis=1)
    csq = np.cumsum(draws * draws, axis=1)
    best = np.full(reps, np.inf)
    idx = np.arange(1, n)
    for i in idx:
        sl = csum[:, i - 1]
        sql = csq[:, i - 1]
        sse_l = sql - sl * sl / i
        sr = csum[:, -1] - sl
        sqr = csq[:, -1] - sql
        right_n = n - i
        sse_r = sqr - sr * sr / right_n
        best = np.minimum(best, sse_l + sse_r)
    imp = np.where(total > 0.0, 1.0 - best / total, 0.0)
    tau = float(np.quantile(imp, 1.0 - thresholds.GATE_ALPHA))
    print(f"formula tau extension n={n} reps={reps} tau={tau:.6f}", flush=True)
    return tau


def none_to_nan(value) -> float:
    return float("nan") if value is None else float(value)


def finite(values: Iterable[float]) -> np.ndarray:
    arr = np.array(list(values), float)
    return arr[np.isfinite(arr)]


def iqr(values: Iterable[float]) -> float:
    arr = finite(values)
    if arr.size < 2:
        return float("nan")
    q75, q25 = np.percentile(arr, [75, 25])
    return float(q75 - q25)


def aggregate(rows: list[dict]) -> list[dict]:
    out = []
    for intensity in sorted({row["lambda"] for row in rows}):
        group = [row for row in rows if row["lambda"] == intensity]
        clean = [row for row in group if row["clean"]]
        widths = finite(row["width_over_2M"] for row in clean)
        mids = finite(row["midpoint"] for row in clean)
        errs = finite(row["center_error"] for row in clean)
        d = finite(row["d"] for row in group if row["clean"])
        sep_mink = finite(row["sep_MINK"] for row in group if row["clean"])
        out.append(
            {
                "lambda": intensity,
                "N_mean": float(np.mean([row["N"] for row in group])),
                "n_rows": len(group),
                "n_clean": len(clean),
                "median_width_over_2M": float(np.median(widths)) if widths.size else float("nan"),
                "iqr_width_over_2M": iqr(widths),
                "mean_width_over_2M": float(np.mean(widths)) if widths.size else float("nan"),
                "std_width_over_2M": float(np.std(widths)) if widths.size else float("nan"),
                "mean_midpoint": float(np.mean(mids)) if mids.size else float("nan"),
                "std_midpoint": float(np.std(mids)) if mids.size else float("nan"),
                "abs_mean_midpoint_error": (
                    abs(float(np.mean(mids)) - thresholds.R_S) if mids.size else float("nan")
                ),
                "median_center_error": float(np.median(errs)) if errs.size else float("nan"),
                "coverage_frac": float(np.mean([row["covers"] for row in group])),
                "abstain_frac_BH": float(np.mean([row["abstained_BH"] for row in group])),
                "abstain_frac_MINK": float(np.mean([row["abstained_MINK"] for row in group])),
                "fp_fraction": validate.loo_fp_fraction(sep_mink),
                "p_perm": validate.signflip_perm_p(d),
            }
        )
    return out


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--intensities", nargs="+", type=float, default=list(DEFAULT_INTENSITIES))
    parser.add_argument("--seed-count", type=int, default=40)
    parser.add_argument("--draw-seed", type=int, default=FORMULA_DRAW_SEED)
    parser.add_argument("--label", default="formula_density_sweep_cpp")
    parser.add_argument("--force-build", action="store_true")
    parser.add_argument("--print-seeds-only", action="store_true")
    args = parser.parse_args()

    thresholds.assert_environment()
    seeds = draw_formula_seeds(args.seed_count, args.draw_seed)
    print("formula seeds:", " ".join(str(seed) for seed in seeds))
    if args.print_seeds_only:
        return

    kernel = ensure_kernel(force=args.force_build)
    rows = []
    for intensity in args.intensities:
        for seed in seeds:
            print(f"lambda={intensity:g} seed={seed}", flush=True)
            rows.append(per_seed(seed, intensity, kernel))

    agg = aggregate(rows)
    out_dir = ROOT / "results"
    per_seed_path = out_dir / f"{args.label}_per_seed.csv"
    aggregate_path = out_dir / f"{args.label}_aggregate.json"
    write_csv(per_seed_path, rows)
    aggregate_path.write_text(json.dumps(agg, indent=2, default=float), encoding="utf-8")
    print(f"wrote: {per_seed_path.relative_to(ROOT)}")
    print(f"wrote: {aggregate_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
