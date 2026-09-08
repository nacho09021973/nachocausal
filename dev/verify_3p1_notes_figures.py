"""EXPLORATION (dev/) — figure-provenance checker for dev/PAPER3_3P1_SCALE_NOTES.md.

Asserts that every number quoted in sections 3.1 and 3.2 of the notes is the
literal (rounded) content of the committed result JSONs. Reads only; runs no
sweep. Exit code 0 iff every figure matches.

Run:  python3 dev/verify_3p1_notes_figures.py
"""

from __future__ import annotations

import json
import sys

import numpy as np

PREC = "dev/explore_3p1_bg_reference_precision_results.json"
BASE = "dev/explore_3p1_bg_reference_results.json"
CAL = "dev/explore_3p1_scale_calibration_results.json"

# (label, value as written in the notes, tolerance)
NOTE_3_1 = [
    (2000, 12.625, 0.375, 1.8879),
    (8000, 18.000, 0.189, 1.9033),
    (16000, 22.625, 0.420, 2.0117),
    (32000, 27.625, 0.375, 2.0655),
]
NOTE_3_1_LOCAL = [0.2559, 0.3299, 0.2881]
NOTE_3_1_BASE_GLOBAL = 0.2902
NOTE_3_2_SLOPES = {
    "logV_all_vs_logrho": 1.0179,
    "logL_all_vs_logrho": 0.3161,
    "logL_vs_logV_all": 0.3106,
    "logV_min_vs_logrho": 1.0634,
    "logL_min_vs_logrho": 0.3195,
    "logL_vs_logV_min": 0.3005,
}
NOTE_3_2_MEDIAN_R_MIN = {500: 3.449, 1000: 3.790, 2000: 4.792, 4000: 5.248, 8000: 5.975}


def main() -> int:
    prec = json.load(open(PREC))
    base = json.load(open(BASE))
    cal = json.load(open(CAL))
    failures = []

    def chk(label: str, noted: float, actual: float, tol: float) -> None:
        good = abs(noted - actual) <= tol
        print(f"{'OK      ' if good else 'MISMATCH'}  {label:42s} note={noted}  json={actual:.6f}")
        if not good:
            failures.append(label)

    for row, (n, mL, se, q) in zip(prec["rows"], NOTE_3_1):
        assert row["N"] == n, f"row order changed: {row['N']} != {n}"
        chk(f"3.1 N={n} mean_L", mL, row["mean_L"], 5e-4)
        chk(f"3.1 N={n} sem_L", se, row["sem_L"], 5e-4)
        chk(f"3.1 N={n} L/N^(1/4)", q, row["L_over_N_quarter"], 5e-5)
    for noted, actual in zip(NOTE_3_1_LOCAL, prec["local_slopes"]):
        chk("3.1 local slope", noted, actual, 5e-5)
    chk("3.1 base-leg global_slope", NOTE_3_1_BASE_GLOBAL, base["global_slope"], 5e-5)

    for key, noted in NOTE_3_2_SLOPES.items():
        chk(f"3.2 {key}", noted, cal["slopes"][key], 5e-5)
    for rho, noted in NOTE_3_2_MEDIAN_R_MIN.items():
        sub = [r for r in cal["rows"] if r["rho"] == float(rho)]
        chk(f"3.2 med R_min rho={rho}", noted, float(np.mean([r["median_R_min"] for r in sub])), 5e-4)

    # Structural claims made in safeguard 5 of the notes.
    chk("safeguard 5: n_seeds", 8, float(prec["rows"][0]["n_seeds"]), 0)
    chk("safeguard 5: N max", 32000, float(max(r["N"] for r in prec["rows"])), 0)

    print("\nRESULT:", "ALL FIGURES MATCH" if not failures else f"DISCREPANCIES: {failures}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
