#!/usr/bin/env python3
"""B1.7 true 1+1D radial-measure control for the frozen B1.5 pair.

This keeps the B1.5 patches and the product order but replaces the spherical
4-volume weight G(UV)=s exp(-s) by the natural 1+1D Schwarzschild volume
weight H(UV)=exp(-s)/s in the same Kruskal coordinates.  The calculation is
deterministic numerical evidence only; it is not a directed-rounding
enclosure.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import lambertw


LAMBDA0 = (0.5, 1.0, 1.0, 0.5, 0.1)
LAMBDA1 = (0.2, 0.8, 2.0, 0.9, 0.1)
B1_6_JSON = "verification_b1_6_radial_product_order.json"


def radial_1p1_density(w: np.ndarray) -> np.ndarray:
    """Return H(w)=exp(-s(w))/s(w), up to a cancelling constant."""

    s = 1.0 + lambertw(-np.asarray(w, dtype=float) / np.e, 0).real
    return np.exp(-s) / s


def radial_probability(lam: tuple[float, ...], order: int) -> tuple[float, float]:
    """Compute the product-order probability and normalization."""

    v0, v1, uout, uin, _ = lam
    nodes, weights = leggauss(order)
    unit = (nodes + 1.0) / 2.0
    unit_weights = weights / 2.0

    umin = -uout
    lu = uin + uout
    lv = v1 - v0
    uy = umin + lu * unit
    ux = umin + (uy[:, None] - umin) * unit[None, :]
    vy = v0 + lv * unit
    vx = v0 + (vy[:, None] - v0) * unit[None, :]

    # Axes are (Uy, Ux, Vy, Vx), with both order triangles removed exactly.
    hx = radial_1p1_density(ux[:, :, None, None] * vx[None, None, :, :])
    hy = radial_1p1_density(uy[:, None, None, None] * vy[None, None, :, None])
    weights4 = (
        unit_weights[:, None, None, None]
        * unit_weights[None, :, None, None]
        * unit_weights[None, None, :, None]
        * unit_weights[None, None, None, :]
    )
    jacobian = (
        lu * lu * unit[:, None, None, None]
        * lv * lv * unit[None, None, :, None]
    )
    ordered_pair_mass = np.sum(weights4 * jacobian * hx * hy)

    u = umin + lu * unit
    v = v0 + lv * unit
    z = np.sum(
        radial_1p1_density(u[:, None] * v[None, :])
        * (lu * unit_weights)[:, None]
        * (lv * unit_weights)[None, :]
    )
    return float(2.0 * ordered_pair_mass / (z * z)), float(z)


def run(orders: list[int]) -> dict:
    rows = []
    for order in orders:
        rho0, z0 = radial_probability(LAMBDA0, order)
        rho1, z1 = radial_probability(LAMBDA1, order)
        rows.append(
            {
                "order": order,
                "rho_1p1d_lambda0": rho0,
                "rho_1p1d_lambda1": rho1,
                "absolute_gap": abs(rho1 - rho0),
                "Z_lambda0": z0,
                "Z_lambda1": z1,
            }
        )

    last = rows[-1]
    previous = rows[-2] if len(rows) > 1 else last
    stability = max(
        abs(last["rho_1p1d_lambda0"] - previous["rho_1p1d_lambda0"]),
        abs(last["rho_1p1d_lambda1"] - previous["rho_1p1d_lambda1"]),
    )
    gap = last["absolute_gap"]
    return {
        "unit": "PUENTE-3P1/B1.7",
        "status": "DETERMINISTIC_NUMERICAL_CONTROL",
        "frozen_pair": True,
        "lambda_pair": [list(LAMBDA0), list(LAMBDA1)],
        "causal_predicate": "Ux < Uy and Vx < Vy",
        "radial_measure": "H(UV)=exp(-s)/s, (1-s) exp(s)=UV",
        "measure_origin": "natural 1+1D Schwarzschild volume in Kruskal coordinates, up to constant",
        "angular_kernel_used": False,
        "q_true_used": False,
        "orders": rows,
        "last_step_stability": stability,
        "gap_at_finest_order": gap,
        "no_search": True,
        "no_seeds": True,
        "no_monte_carlo": True,
        "n": 2,
        "terminal": (
            "B1.7_TRUE_1P1D_NUMERICALLY_SEPARATED"
            if gap > 10.0 * stability
            else "B1.7_TRUE_1P1D_NUMERICALLY_INCONCLUSIVE"
        ),
        "claim_ceiling": (
            "The frozen pair remains numerically separated under the natural "
            "1+1D radial measure and product order. This is not a formal enclosure."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--orders",
        nargs="+",
        type=int,
        default=[8, 12, 16, 20, 24, 32],
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if len(args.orders) < 2 or any(order < 4 for order in args.orders):
        parser.error("provide at least two quadrature orders >= 4")
    result = run(args.orders)
    payload = json.dumps(result, indent=2) + "\n"
    print(payload, end="")
    if args.output is not None:
        args.output.write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    main()
