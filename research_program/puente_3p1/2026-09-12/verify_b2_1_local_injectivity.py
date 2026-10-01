"""PUENTE-3P1 / B2.1 — fixed-path local rho enclosures.

The path and t0 are constants inherited from B2. Pointwise angular upper bounds and explicit
causal-path lower bounds are integrated with fixed Gauss-Legendre rules.
"""
import json
import math
import sys
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre, lambertw

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "B1"))
from verify_certified_rho_frozen_pair import G, q  # noqa: E402

L0 = np.array((0.5, 1.0, 1.0, 0.5, 0.1))
L1 = np.array((0.2, 0.8, 2.0, 0.9, 0.1))
T0 = 0.5
T_GRID = (0.45, 0.475, 0.5, 0.525, 0.55)


def path(t):
    return (1.0 - t) * L0 + t * L1


def angular_prob(budget):
    return (1.0 - np.cos(np.minimum(math.pi, np.maximum(0.0, budget)))) / 2.0


def enclosure(lam, order=16):
    v0, v1, uout, uin, _ = lam
    ulo, uhi = -uout, uin
    n, w = roots_legendre(order)
    V = (n + 1.0) * (v1 - v0) / 2.0 + v0
    Wv = w * (v1 - v0) / 2.0
    U = (n + 1.0) * (uhi - ulo) / 2.0 + ulo
    Wu = w * (uhi - ulo) / 2.0
    ux, vx, uy, vy = np.meshgrid(U, V, U, V, indexing="ij")
    wx, wv, wy, wz = np.meshgrid(Wu, Wv, Wu, Wv, indexing="ij")
    weight = wx * wv * wy * wz * G(ux * vx) * G(uy * vy)
    ordered = (ux <= uy) & (vx <= vy)
    du, dv = np.maximum(uy - ux, 0.0), np.maximum(vy - vx, 0.0)

    # Pointwise upper bound: q is maximized at the largest UV corner of this sub-rectangle.
    qrect = np.maximum.reduce([q(ux * vx), q(ux * vy), q(uy * vx), q(uy * vy)])
    upper_budget = qrect * np.sqrt(du * dv)

    # Fixed explicit two-segment paths, with three fixed beta values for the midpoint U.
    pn, pw = roots_legendre(10)
    tt = (pn + 1.0) / 2.0
    lower_budget = np.zeros_like(du)
    vm = (vx + vy) / 2.0
    for beta in (0.25, 0.5, 0.75):
        um = ux + beta * (uy - ux)
        den1, den2 = np.where(vm > vx, vm - vx, 1.0), np.where(vy > vm, vy - vm, 1.0)
        slope1, slope2 = (um - ux) / den1, (uy - um) / den2
        vv1 = vx[..., None] + (vm - vx)[..., None] * tt
        vv2 = vm[..., None] + (vy - vm)[..., None] * tt
        uu1 = ux[..., None] + slope1[..., None] * (vv1 - vx[..., None])
        uu2 = um[..., None] + slope2[..., None] * (vv2 - vm[..., None])
        i1 = np.sum(pw * q(uu1 * vv1), axis=-1) * (vm - vx) / 2.0
        i2 = np.sum(pw * q(uu2 * vv2), axis=-1) * (vy - vm) / 2.0
        lower_budget = np.maximum(lower_budget, np.sqrt(np.maximum(slope1, 0.0)) * i1 +
                                  np.sqrt(np.maximum(slope2, 0.0)) * i2)
    lower_budget[~ordered] = 0.0
    z = np.sum(Wu[:, None] * Wv[None, :] * G(U[:, None] * V[None, :]))
    return (float(2.0 * np.sum(weight * angular_prob(lower_budget)) / z**2),
            float(2.0 * np.sum(weight * angular_prob(upper_budget)) / z**2), float(z))


def main():
    rows = []
    for t in T_GRID:
        lam = path(t)
        lo10, hi10, z10 = enclosure(lam, 10)
        lo16, hi16, z16 = enclosure(lam, 16)
        margin = max(abs(lo16 - lo10), abs(hi16 - hi10))
        rows.append({"t": t, "lambda": lam.tolist(), "rho_lower": max(0.0, lo16 - margin),
                     "rho_upper": min(1.0, hi16 + margin), "raw_order10": [lo10, hi10],
                     "raw_order16": [lo16, hi16], "quadrature_margin": margin,
                     "normalization_Z": z16})
    increasing_grid = all(a["rho_upper"] < b["rho_lower"]
                          for a, b in zip(rows, rows[1:]))
    out = {"unit": "PUENTE-3P1/B2.1", "path": "affine B2 path", "t0": T0,
           "t_grid": list(T_GRID), "rho_enclosures": rows,
           "grid_interval_order_control": increasing_grid, "no_search": True,
           "no_new_path": True, "no_new_t0": True, "no_seeds": True, "no_monte_carlo": True,
           "terminal": ("B2.1_POSITIVE_LOCAL_MONOTONICITY" if increasing_grid
                        else "B2.1_INCONCLUSIVE_BY_BOUNDS")}
    print(json.dumps(out, indent=2))
    with open(HERE / "verification_b2_1_local_injectivity.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
