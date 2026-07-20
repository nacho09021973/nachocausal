#!/usr/bin/env python
"""New-geometry future-observables evaluation.

Implements docs/preregistration_new_geometry_future_observables.md.

Default usage is safe:

  .venv/bin/python dev/run_new_geometry_future_observables.py preflight

The evaluation path writes only under evidence/new_geometry_20260719/ and must be invoked
explicitly:

  .venv/bin/python dev/run_new_geometry_future_observables.py evaluate

No old R-VAR artifacts, PR009/PR010 artifacts, prereg-002 artifacts, or validation paths are read
as data inputs. The script imports the existing causal-relation builder only as code.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import platform
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from nachocausal import generator, thresholds


CONTRACT_PATH = ROOT / "docs" / "preregistration_new_geometry_future_observables.md"
EVIDENCE_DIR = ROOT / "evidence" / "new_geometry_20260719"

PATCH_GEOMETRY = "SQUARE_BOX_2P4"
T_EDGE_NEW = 2.4
R_EDGE_NEW = 2.4
R_CENTER_NEW = 1.3
R_LOW_NEW = R_CENTER_NEW - R_EDGE_NEW / 2.0
R_HIGH_NEW = R_CENTER_NEW + R_EDGE_NEW / 2.0
BOX_AREA_NEW = T_EDGE_NEW * R_EDGE_NEW
ASPECT_RATIO_NEW = T_EDGE_NEW / R_EDGE_NEW

INTENSITIES_NEW = (1200.0, 2400.0, 4800.0, 9600.0)
PRIMARY_INTENSITY_NEW = 9600.0
MIN_MINIMALS = 8
MIN_VALID_SEEDS = 20
EVAL_SEED_COUNT = 24
MINK_CV_FLOOR = 0.05
P_PERM_THRESHOLD = 0.01

NEW_GEOM_DEV_SEEDS = tuple(range(4_100_000, 4_100_012))
NEW_GEOM_EVAL_SEEDS = tuple(range(4_200_000, 4_200_024))

EXCLUDED_SEEDS = set(thresholds.DEV_SEEDS) | set(thresholds.VALIDATION_SEEDS)
EXCLUDED_SEEDS |= set(range(1_000_000, 1_000_040))
EXCLUDED_SEEDS |= set(range(1_101_000, 1_101_024))
EXCLUDED_SEEDS |= set(range(2_000_000, 3_000_000))
EXCLUDED_SEEDS |= set(range(3_000_000, 4_000_000))


@dataclass(frozen=True)
class MetricRow:
    seed: int
    intensity: float
    kind: str
    N: int
    n_min: int
    valid: bool
    abstention_reason: str
    mean_L: float
    std_L: float
    cv_L: float
    iqr_L: float
    range_L: float
    mean_V: float
    std_V: float
    cv_V: float
    iqr_V: float
    range_V: float
    flags: str


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except Exception:
        return "[UNVERIFIED]"


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def assert_seed_disjointness() -> None:
    new = set(NEW_GEOM_DEV_SEEDS) | set(NEW_GEOM_EVAL_SEEDS)
    overlap = sorted(new & EXCLUDED_SEEDS)
    if overlap:
        raise RuntimeError(f"new geometry seed overlap detected: {overlap}")
    if len(NEW_GEOM_EVAL_SEEDS) != EVAL_SEED_COUNT:
        raise RuntimeError("evaluation seed count does not match frozen contract")


def assert_patch_contract() -> None:
    if PATCH_GEOMETRY != "SQUARE_BOX_2P4":
        raise RuntimeError("patch label mismatch")
    if not math.isclose(T_EDGE_NEW, 2.4):
        raise RuntimeError("T_EDGE_NEW mismatch")
    if not math.isclose(R_EDGE_NEW, 2.4):
        raise RuntimeError("R_EDGE_NEW mismatch")
    if not math.isclose(R_CENTER_NEW, 1.3):
        raise RuntimeError("R_CENTER_NEW mismatch")
    if not math.isclose(R_LOW_NEW, 0.1):
        raise RuntimeError("r low mismatch")
    if not math.isclose(R_HIGH_NEW, 2.5):
        raise RuntimeError("r high mismatch")
    if not math.isclose(ASPECT_RATIO_NEW, 1.0):
        raise RuntimeError("aspect ratio mismatch")


def preflight() -> dict:
    thresholds.assert_environment()
    assert_seed_disjointness()
    assert_patch_contract()
    if not CONTRACT_PATH.exists():
        raise RuntimeError(f"contract missing: {CONTRACT_PATH}")
    return {
        "status": "PREFLIGHT_PASS",
        "contract": str(CONTRACT_PATH.relative_to(ROOT)),
        "contract_sha256": file_sha256(CONTRACT_PATH),
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "patch_geometry": PATCH_GEOMETRY,
        "t_edge": T_EDGE_NEW,
        "r_edge": R_EDGE_NEW,
        "r_center": R_CENTER_NEW,
        "r_low": R_LOW_NEW,
        "r_high": R_HIGH_NEW,
        "box_area": BOX_AREA_NEW,
        "aspect_ratio": ASPECT_RATIO_NEW,
        "eval_seeds": list(NEW_GEOM_EVAL_SEEDS),
        "dev_smoke_seeds": list(NEW_GEOM_DEV_SEEDS),
    }


def sprinkle_square(seed: int, intensity: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    n = rng.poisson(float(intensity))
    edges = np.array([T_EDGE_NEW, R_EDGE_NEW], dtype=float)
    center = np.array([T_EDGE_NEW / 2.0, R_CENTER_NEW], dtype=float)
    low = center - edges / 2.0
    pts = low + rng.random((n, 2)) * edges
    return pts, edges, center


def longest_chain_lengths(C: np.ndarray) -> np.ndarray:
    """Longest future-chain length in edges for each element.

    Convention: C[a, b] is true iff b is in the causal past of a. Therefore future(i) is C[:, i].
    """
    N = C.shape[0]
    H = np.zeros(N, dtype=np.int64)
    past_size = C.sum(axis=1)
    order = np.argsort(-past_size, kind="stable")
    for i in order:
        fut_mask = C[:, i]
        if fut_mask.any():
            H[i] = 1 + H[fut_mask].max()
    return H


def finite_or_nan(x: float) -> float:
    return float(x) if np.isfinite(x) else float("nan")


def summarize(x: np.ndarray) -> dict[str, float]:
    x = np.asarray(x, dtype=float)
    if x.size == 0:
        return {
            "mean": float("nan"),
            "std": float("nan"),
            "cv": float("nan"),
            "iqr": float("nan"),
            "range": float("nan"),
        }
    mean = float(np.mean(x))
    std = float(np.std(x))
    q75, q25 = np.percentile(x, [75, 25])
    cv = std / mean if mean > 0 else float("nan")
    return {
        "mean": finite_or_nan(mean),
        "std": finite_or_nan(std),
        "cv": finite_or_nan(cv),
        "iqr": finite_or_nan(float(q75 - q25)),
        "range": finite_or_nan(float(np.max(x) - np.min(x))),
    }


def metric_row(seed: int, intensity: float, kind: str) -> MetricRow:
    emb, _, _ = sprinkle_square(seed, intensity)
    C = generator.past_matrix_fast(emb, kind, r_S=thresholds.R_S)
    minimal = np.flatnonzero(~C.any(axis=1))
    H = longest_chain_lengths(C)
    L_min = H[minimal]
    V_min = C[:, minimal].sum(axis=0)
    L = summarize(L_min)
    V = summarize(V_min)
    flags: list[str] = []
    valid = True
    abstention = ""
    if len(minimal) < MIN_MINIMALS:
        valid = False
        abstention = "SUPPORT_ABSTAIN"
        flags.append("LOW_MINIMAL_SUPPORT")
    if kind == "MINK" and np.isfinite(L["cv"]) and L["cv"] < MINK_CV_FLOOR:
        flags.append("NEAR_DELTA_MINK_L")
    if kind == "MINK" and np.isfinite(V["cv"]) and V["cv"] < MINK_CV_FLOOR:
        flags.append("NEAR_DELTA_MINK_V")
    if not all(np.isfinite(v) for v in (L["mean"], L["cv"], V["mean"], V["cv"])):
        valid = False
        abstention = abstention or "NONFINITE_SUMMARY"
    if L["mean"] <= 0 or V["mean"] <= 0:
        valid = False
        abstention = abstention or "ZERO_MEAN_SUMMARY"
    return MetricRow(
        seed=seed,
        intensity=float(intensity),
        kind=kind,
        N=int(emb.shape[0]),
        n_min=int(len(minimal)),
        valid=valid,
        abstention_reason=abstention,
        mean_L=L["mean"],
        std_L=L["std"],
        cv_L=L["cv"],
        iqr_L=L["iqr"],
        range_L=L["range"],
        mean_V=V["mean"],
        std_V=V["std"],
        cv_V=V["cv"],
        iqr_V=V["iqr"],
        range_V=V["range"],
        flags=";".join(flags),
    )


def median(xs: Iterable[float]) -> float:
    vals = [float(x) for x in xs if np.isfinite(x)]
    return float(np.median(vals)) if vals else float("nan")


def exact_sign_flip_pvalue(ds: Sequence[float]) -> float:
    vals = np.asarray([float(d) for d in ds if np.isfinite(d)], dtype=float)
    n = vals.size
    if n == 0:
        return float("nan")
    observed = abs(float(vals.sum()))
    ge = 0
    total = 1 << n
    for mask in range(total):
        signed_sum = 0.0
        for i, value in enumerate(vals):
            signed_sum += value if ((mask >> i) & 1) else -value
        if abs(signed_sum) >= observed - 1e-15:
            ge += 1
    return ge / total


def decide_terminal(rows: Sequence[MetricRow]) -> tuple[str, str, dict]:
    by = {(r.kind, r.intensity, r.seed): r for r in rows}
    support_counts: dict[str, int] = {}
    for intensity in INTENSITIES_NEW:
        for kind in ("MINK", "BH"):
            valid_count = sum(
                1 for s in NEW_GEOM_EVAL_SEEDS if by[(kind, intensity, s)].valid
            )
            support_counts[f"{kind}_{intensity}"] = valid_count
            if valid_count < MIN_VALID_SEEDS:
                return "FAILED_SUPPORT_CONTRACT", "contract/design", {
                    "support_counts": support_counts
                }

    mink_primary = [
        by[("MINK", PRIMARY_INTENSITY_NEW, s)]
        for s in NEW_GEOM_EVAL_SEEDS
        if by[("MINK", PRIMARY_INTENSITY_NEW, s)].valid
    ]
    med_mink_cv_L = median(r.cv_L for r in mink_primary)
    med_mink_cv_V = median(r.cv_V for r in mink_primary)
    mink_nondegenerate = (
        len(mink_primary) >= MIN_VALID_SEEDS
        and (med_mink_cv_L >= MINK_CV_FLOOR or med_mink_cv_V >= MINK_CV_FLOOR)
    )
    if not mink_nondegenerate:
        return "MINK_CONTROL_DEGENERATE_ON_NEW_GEOMETRY", "contract/design", {
            "valid_mink_primary": len(mink_primary),
            "median_cv_L_MINK": med_mink_cv_L,
            "median_cv_V_MINK": med_mink_cv_V,
        }

    paired: list[tuple[MetricRow, MetricRow]] = []
    for seed in NEW_GEOM_EVAL_SEEDS:
        bh = by[("BH", PRIMARY_INTENSITY_NEW, seed)]
        mk = by[("MINK", PRIMARY_INTENSITY_NEW, seed)]
        if bh.valid and mk.valid:
            paired.append((bh, mk))
    if len(paired) < MIN_VALID_SEEDS:
        return "INSUFFICIENT_VALID_PAIRS", "contract/design", {
            "valid_pairs_primary": len(paired)
        }

    dL = [bh.cv_L - mk.cv_L for bh, mk in paired]
    dV = [bh.cv_V - mk.cv_V for bh, mk in paired]
    pL = exact_sign_flip_pvalue(dL)
    pV = exact_sign_flip_pvalue(dV)
    med_dL = median(dL)
    med_dV = median(dV)
    details = {
        "valid_pairs_primary": len(paired),
        "median_D_L": med_dL,
        "median_D_V": med_dV,
        "p_perm_D_L": pL,
        "p_perm_D_V": pV,
        "median_cv_L_MINK": med_mink_cv_L,
        "median_cv_V_MINK": med_mink_cv_V,
    }
    if (med_dL > 0 and pL <= P_PERM_THRESHOLD) or (
        med_dV > 0 and pV <= P_PERM_THRESHOLD
    ):
        return "BH_MINK_DISPERSION_DIFFERENCE_DETECTED", "scientific", details
    if np.isfinite(pL) and np.isfinite(pV):
        return "NO_BH_MINK_DISPERSION_DIFFERENCE_DETECTED", "scientific", details
    return "INCONCLUSIVE_SCIENTIFIC_CONTRAST", "scientific", details


def write_csv(path: Path, rows: Sequence[MetricRow]) -> None:
    fields = list(MetricRow.__dataclass_fields__)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: getattr(row, field) for field in fields})


def write_text_outputs(
    out_dir: Path,
    terminal: str,
    layer: str,
    details: dict,
    preflight_info: dict,
) -> None:
    (out_dir / "terminal.txt").write_text(f"{terminal}\nlayer={layer}\n", encoding="utf-8")
    env = {
        **preflight_info,
        "uname": platform.uname()._asdict(),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }
    (out_dir / "environment.txt").write_text(
        json.dumps(env, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    report = f"""# New Geometry Future Observables — Summary Report

STATUS: EVALUATION_COMPLETE

This is a new question under `SQUARE_BOX_2P4`.

The R-VAR closure remains intact:

```text
CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]
```

No old seeds, R-VAR thresholds, R-VAR artifacts, PR009 outputs, PR010 artifacts, or prereg-002
validation artifacts were used as evaluation data.

Terminal:

```text
{terminal}
```

Layer:

```text
{layer}
```

Details:

```json
{json.dumps(details, indent=2, sort_keys=True)}
```

No horizon reconstruction claim is made.
"""
    (out_dir / "summary_report.md").write_text(report, encoding="utf-8")


def evaluate() -> tuple[str, str]:
    info = preflight()
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    rows: list[MetricRow] = []
    for intensity in INTENSITIES_NEW:
        for seed in NEW_GEOM_EVAL_SEEDS:
            for kind in ("MINK", "BH"):
                rows.append(metric_row(seed, intensity, kind))
    terminal, layer, details = decide_terminal(rows)
    write_csv(EVIDENCE_DIR / "per_seed_metrics.csv", rows)
    write_text_outputs(EVIDENCE_DIR, terminal, layer, details, info)
    return terminal, layer


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("preflight", help="check contract, seed disjointness, environment; no data")
    sub.add_parser("evaluate", help="run frozen evaluation and write evidence directory")
    args = parser.parse_args(argv)

    if args.command == "preflight":
        print(json.dumps(preflight(), indent=2, sort_keys=True))
        return 0

    terminal, layer = evaluate()
    print(f"NEW_GEOMETRY_TERMINAL={terminal}")
    print(f"TERMINAL_LAYER={layer}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
