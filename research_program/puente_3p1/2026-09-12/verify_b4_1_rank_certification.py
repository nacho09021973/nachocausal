"""PUENTE-3P1 / B4.1 — all-minor and spectral rank audit at frozen point."""
import json
import numpy as np
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from verify_b4_execution import XSTAR, moments  # noqa: E402


def main():
    # Fixed chart and fixed central step; no post-hoc coordinate choice.
    h = 1e-3
    J = np.zeros((4, 3))
    for j in range(3):
        xp, xm = XSTAR.copy(), XSTAR.copy()
        xp[j] += h; xm[j] -= h
        J[:, j] = (moments(xp) - moments(xm)) / (2.0 * h)
    minors = {}
    for omit in range(4):
        rows = [i for i in range(4) if i != omit]
        minors[f"omit_row_{omit}"] = float(np.linalg.det(J[rows, :]))
    R = np.diag([1.0, 10000.0, 10000.0, 10000.0])
    Jt = R @ J
    singular_values = np.linalg.svd(Jt, compute_uv=False)
    out = {"unit": "PUENTE-3P1/B4.1", "frozen_point": XSTAR.tolist(),
           "fixed_row_rescaling": [1.0, 10000.0, 10000.0, 10000.0],
           "J": J.tolist(), "all_3x3_minors": minors,
           "scaled_singular_values": singular_values.tolist(),
           "certified_minor": False, "certified_sigma_min": False,
           "no_new_point": True, "no_new_chart": True, "no_row_dropping": True,
           "no_search": True, "no_seeds": True, "no_monte_carlo": True,
           "terminal": "B4_INCONCLUSIVE_BY_BOUNDS"}
    print(json.dumps(out, indent=2))
    with open(HERE / "verification_b4_1_rank_certification.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
