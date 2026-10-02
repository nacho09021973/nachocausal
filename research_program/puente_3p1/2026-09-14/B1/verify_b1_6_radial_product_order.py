#!/usr/bin/env python3
"""B1.6 radial product-order control for the frozen B1.5 pair.

This is a deterministic numerical control.  It keeps the B1.5 radial density
G(U V) and the same two patches, but replaces the spherical causal predicate
by

    x <_rad y  iff  U_x < U_y and V_x < V_y.

The four-dimensional ordered-pair integral is evaluated after the exact smooth
triangle substitutions used below.  The order ladder is a stability check;
it is not a formal enclosure.  No seeds, Monte Carlo, pair search, or n-sweep
are used.
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
B1_5_COMMIT = "6633ebd2da81188ecc492f59b44b75e0e2c59cd2"
B1_5_ANALYTIC_GAP = 0.002918225282557404


def radial_density(w: np.ndarray) -> np.ndarray:
    """Return G(w)=s(w) exp(-s(w)) on the positive Kruskal branch.

    Here (1-s) exp(s)=w, hence s=1+W_0(-w/e).  Lambert W is used only
    as a numerical evaluation device in this control; B1.5's formal
    certificate remains the no-Lambert-W directed-rounding artifact.
    """

    s = 1.0 + lambertw(-np.asarray(w, dtype=float) / np.e, 0).real
    return s * np.exp(-s)


def radial_probability(lam: tuple[float, ...], order: int) -> tuple[float, float]:
    """Compute rho_rad and Z with order-point Gauss-Legendre quadrature.

    The substitutions are

        U_y = U_min + L_U y,  U_x = U_min + (U_y-U_min) x,
        V_y = v_0 + L_V z,    V_x = v_0 + (V_y-v_0) t,

    for x,y,t,z in [0,1].  They remove both order-triangle boundaries, so
    the integrand is smooth in the four unit variables.  The Jacobian is
    L_U^2 y L_V^2 z.
    """

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

    # Axes are (Uy, Ux, Vy, Vx).
    gx = radial_density(ux[:, :, None, None] * vx[None, None, :, :])
    gy = radial_density(uy[:, None, None, None] * vy[None, None, :, None])

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
    ordered_pair_mass = np.sum(weights4 * jacobian * gx * gy)

    u = umin + lu * unit
    v = v0 + lv * unit
    z = np.sum(
        radial_density(u[:, None] * v[None, :])
        * (lu * unit_weights)[:, None]
        * (lv * unit_weights)[None, :]
    )
    rho = 2.0 * ordered_pair_mass / (z * z)
    return float(rho), float(z)


def run(orders: list[int]) -> dict:
    rows = []
    for order in orders:
        rho0, z0 = radial_probability(LAMBDA0, order)
        rho1, z1 = radial_probability(LAMBDA1, order)
        rows.append(
            {
                "order": order,
                "rho_rad_lambda0": rho0,
                "rho_rad_lambda1": rho1,
                "absolute_gap": abs(rho1 - rho0),
                "Z_lambda0": z0,
                "Z_lambda1": z1,
            }
        )

    last = rows[-1]
    previous = rows[-2] if len(rows) > 1 else last
    stability = max(
        abs(last["rho_rad_lambda0"] - previous["rho_rad_lambda0"]),
        abs(last["rho_rad_lambda1"] - previous["rho_rad_lambda1"]),
    )
    radial_gap = last["absolute_gap"]
    terminal = (
        "B1.6_RADIAL_NUMERICALLY_SEPARATED"
        if radial_gap > 10.0 * stability
        else "B1.6_RADIAL_NUMERICALLY_INCONCLUSIVE"
    )
    return {
        "unit": "PUENTE-3P1/B1.6",
        "status": "DETERMINISTIC_NUMERICAL_CONTROL",
        "frozen_pair": True,
        "lambda_pair": [list(LAMBDA0), list(LAMBDA1)],
        "b1_5_commit": B1_5_COMMIT,
        "causal_predicate": "Ux < Uy and Vx < Vy",
        "retained_radial_density": "G(UV)=s exp(-s), (1-s) exp(s)=UV",
        "angular_kernel_used": False,
        "q_true_used": False,
        "orders": rows,
        "last_step_stability": stability,
        "radial_gap_at_finest_order": radial_gap,
        "b1_5_analytic_gap_reference": B1_5_ANALYTIC_GAP,
        "no_search": True,
        "no_seeds": True,
        "no_monte_carlo": True,
        "n": 2,
        "terminal": terminal,
        "claim_ceiling": (
            "The angular causal reach is not necessary for numerical separation "
            "of this frozen pair under the retained radial density. This is not "
            "a formal enclosure and does not isolate the 3+1D volume measure."
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
