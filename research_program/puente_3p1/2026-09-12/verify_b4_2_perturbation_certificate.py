"""PUENTE-3P1 / B4.2 — fixed-scaling perturbation audit.

This is deliberately conservative: convergence differences are reported, but are not labelled
rigorous interval bounds. Therefore the terminal remains inconclusive unless a formal enclosure
is supplied.
"""
import json
import sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from verify_b4_execution import XSTAR, moments  # noqa: E402

R = np.diag([1.0, 10000.0, 10000.0, 10000.0])
SIGMA_MIN_J0 = 1.1370045523898505e-3


def jacobian(order, step):
    J = np.zeros((4, 3))
    for j in range(3):
        xp, xm = XSTAR.copy(), XSTAR.copy()
        xp[j] += step; xm[j] -= step
        # moments currently expose the fixed deterministic quadrature order as n.
        J[:, j] = (moments(xp, n=order) - moments(xm, n=order)) / (2.0 * step)
    return R @ J


def main():
    configs = ((10, 1e-3), (14, 1e-3), (10, 5e-4), (14, 5e-4))
    mats = [jacobian(n, h) for n, h in configs]
    reference = mats[1]
    entrywise = np.max(np.abs(np.stack([m - reference for m in mats])), axis=0)
    frob = float(np.linalg.norm(entrywise, ord="fro"))
    out = {"unit": "PUENTE-3P1/B4.2", "fixed_row_scaling": [1, 10000, 10000, 10000],
           "sigma_min_Jtilde0": SIGMA_MIN_J0, "configs": [list(c) for c in configs],
           "Jtilde_reference": reference.tolist(), "observed_entrywise_spread": entrywise.tolist(),
           "observed_frobenius_spread": frob, "formal_interval_enclosure": False,
           "no_rescaling": True, "no_new_point": True, "no_new_chart": True,
           "no_search": True, "no_seeds": True, "no_monte_carlo": True,
           "terminal": "B4_INCONCLUSIVE_BY_BOUNDS"}
    print(json.dumps(out, indent=2))
    with open(HERE / "verification_b4_2_perturbation_certificate.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
