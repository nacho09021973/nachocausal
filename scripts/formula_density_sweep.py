"""Run the formula-branch density sweep and write per-seed scaling artifacts.

This is exploratory tooling for docs/formula_run_protocol.md. It is not part of
the sealed prereg-002 PASS/FAIL path.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Iterable

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from nachocausal import estimator, gate, generator, thresholds, validate
from nachocausal.scoring import blind_bracket


DEFAULT_INTENSITIES = (1500.0, 3000.0, 6000.0, 12000.0, 24000.0)
FORMULA_SEED_LOW = 4_000_000
FORMULA_SEED_HIGH = 5_000_000
FORMULA_DRAW_SEED = 20260623


def draw_formula_seeds(count: int, draw_seed: int = FORMULA_DRAW_SEED) -> tuple[int, ...]:
    rng = np.random.default_rng(draw_seed)
    seeds = rng.choice(np.arange(FORMULA_SEED_LOW, FORMULA_SEED_HIGH), count, replace=False)
    return tuple(int(x) for x in sorted(seeds))


def per_seed(seed: int, intensity: float, guard: bool = True) -> dict:
    emb, edges, center = generator.numpy_sprinkle(seed, intensity, thresholds.T_EDGE)
    generator.assert_coordinate_uniform(emb, edges, center)
    row = {
        "lambda": float(intensity),
        "seed": int(seed),
        "N": int(emb.shape[0]),
    }

    blind = {}
    for kind in ("BH", "MINK"):
        C = generator.past_matrix_fast(emb, kind)
        if guard:
            estimator.verify_order_only(C, seed=seed)
        O_by_min, min_idx = estimator.estimate_O_volume(C)
        vals = list(O_by_min.values())
        thr, sep = estimator.two_means_split(vals)
        imp = estimator.improvement(vals)
        n_min = len(min_idx)
        tau_n = gate.tau(n_min) if n_min >= 2 else float("nan")
        abstained = gate.abstains(imp, n_min)
        if abstained:
            sep = 0.0
        blind[kind] = {
            "O_by_min": O_by_min,
            "min_idx": min_idx,
            "thr": thr,
            "sep": sep,
            "improvement": imp,
            "n_min": n_min,
            "tau_n": tau_n,
            "abstained": abstained,
        }

    bh = blind["BH"]
    mk = blind["MINK"]
    if bh["abstained"]:
        br = {
            "valid": False,
            "r_lo": float("nan"),
            "r_hi": float("nan"),
            "width": float("nan"),
            "midpoint": float("nan"),
            "covers": False,
            "clean": False,
        }
    else:
        br = blind_bracket(bh["O_by_min"], bh["min_idx"], bh["thr"], emb)

    midpoint = br["midpoint"]
    center_error = abs(midpoint - thresholds.R_S) if np.isfinite(midpoint) else float("nan")
    row.update(
        n_min_BH=bh["n_min"],
        improvement_BH=bh["improvement"],
        tau_n_BH=bh["tau_n"],
        abstained_BH=bool(bh["abstained"]),
        r_lo=br["r_lo"],
        r_hi=br["r_hi"],
        width=br["width"],
        width_over_2M=br["width"] / thresholds.TWO_M if np.isfinite(br["width"]) else float("nan"),
        midpoint=midpoint,
        center_error=center_error,
        covers=bool(br["covers"]),
        clean=bool(br["clean"]),
        sep_BH=bh["sep"],
        sep_MINK=mk["sep"],
        d=bh["sep"] - mk["sep"],
        n_min_MINK=mk["n_min"],
        improvement_MINK=mk["improvement"],
        tau_n_MINK=mk["tau_n"],
        abstained_MINK=bool(mk["abstained"]),
    )
    return row


def finite(values: Iterable[float]) -> np.ndarray:
    arr = np.array(list(values), float)
    return arr[np.isfinite(arr)]


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


def iqr(values: np.ndarray) -> float:
    values = finite(values)
    if values.size < 2:
        return float("nan")
    q75, q25 = np.percentile(values, [75, 25])
    return float(q75 - q25)


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
    parser.add_argument("--label", default="formula_density_sweep")
    parser.add_argument("--no-guard", action="store_true")
    parser.add_argument(
        "--print-seeds-only",
        action="store_true",
        help="Draw and print the deterministic formula seeds without running the sweep.",
    )
    args = parser.parse_args()

    thresholds.assert_environment()
    seeds = draw_formula_seeds(args.seed_count, args.draw_seed)
    print("formula seeds:", " ".join(str(seed) for seed in seeds))
    if args.print_seeds_only:
        return

    rows = []
    for intensity in args.intensities:
        for seed in seeds:
            print(f"lambda={intensity:g} seed={seed}", flush=True)
            rows.append(per_seed(seed, intensity, guard=not args.no_guard))

    agg = aggregate(rows)
    out_dir = Path("results")
    per_seed_path = out_dir / f"{args.label}_per_seed.csv"
    aggregate_path = out_dir / f"{args.label}_aggregate.json"
    write_csv(per_seed_path, rows)
    aggregate_path.write_text(json.dumps(agg, indent=2, default=float), encoding="utf-8")
    print(f"wrote: {per_seed_path}")
    print(f"wrote: {aggregate_path}")


if __name__ == "__main__":
    main()
