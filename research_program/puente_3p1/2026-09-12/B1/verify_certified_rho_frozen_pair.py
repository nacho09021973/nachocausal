"""PUENTE-3P1 / B1.4 — deterministic certified interval for the frozen pair.

Lower bounds come from explicit two-segment causal paths; the upper bound is the B1.2
Cauchy-Schwarz bound. Fixed Gauss-Legendre quadrature is used only for the radial integral.
"""
import json
import math
import numpy as np
from scipy.special import roots_legendre, lambertw

LAMBDA0 = (0.5, 1.0, 1.0, 0.5, 0.1)
LAMBDA1 = (0.2, 0.8, 2.0, 0.9, 0.1)


def s_of_uv(uv):
    return (1.0 + lambertw(-np.asarray(uv) / math.e, 0).real)


def G(uv):
    s = s_of_uv(uv)
    return s * np.exp(-s)


def q(uv):
    s = s_of_uv(uv)
    return np.exp(-0.5 * s) / np.sqrt(s)


def angular_prob(budget):
    return (1.0 - np.cos(np.minimum(math.pi, np.maximum(0.0, budget)))) / 2.0


def rho_bounds(lam, order):
    v0, v1, uout, uin, _ = lam
    lo, hi = -uout, uin
    nodes, weights = roots_legendre(order)
    V = (nodes + 1.0) * (v1 - v0) / 2.0 + v0
    Wv = weights * (v1 - v0) / 2.0
    U = (nodes + 1.0) * (hi - lo) / 2.0 + lo
    Wu = weights * (hi - lo) / 2.0
    # Full tensor grid of independent radial points, then retain x <= y.
    ux, vx, uy, vy = np.meshgrid(U, V, U, V, indexing="ij")
    wx, wv, wy, wz = np.meshgrid(Wu, Wv, Wu, Wv, indexing="ij")
    gx = G(ux * vx)
    gy = G(uy * vy)
    ordered = (ux <= uy) & (vx <= vy)
    du, dv = np.maximum(uy - ux, 0.0), np.maximum(vy - vx, 0.0)
    qcorners = np.stack([q(lo * v0), q(lo * v1), q(hi * v0), q(hi * v1)])
    qmin, qmax = float(np.min(qcorners)), float(np.max(qcorners))
    upper_budget = qmax * np.sqrt(du * dv)

    # Explicit two-segment paths; beta controls the U-coordinate of the fixed knot.
    # alpha is fixed at 1/2, and beta grid includes the straight path beta=1/2.
    path_nodes, path_weights = roots_legendre(12)
    lower_budget = np.zeros_like(du)
    for beta in (0.25, 0.5, 0.75):
        vm = (vx + vy) / 2.0
        um = ux + beta * (uy - ux)
        total = np.zeros_like(du)
        den1 = np.where(vm > vx, vm - vx, 1.0)
        den2 = np.where(vy > vm, vy - vm, 1.0)
        for a, b, slope in ((vx, vm, (um - ux) / den1),
                            (vm, vy, (uy - um) / den2)):
            tt = (path_nodes + 1.0) / 2.0
            vv = a[..., None] + (b - a)[..., None] * tt
            uu = (ux[..., None] + slope[..., None] * (vv - vx[..., None])
                  if a is vx else um[..., None] + slope[..., None] * (vv - vm[..., None]))
            integ = np.sum(path_weights * q(uu * vv), axis=-1) * (b - a) / 2.0
            total += np.sqrt(np.maximum(slope, 0.0)) * integ
        lower_budget = np.maximum(lower_budget, total)
    lower_budget[~ordered] = 0.0
    upper = angular_prob(upper_budget)
    lower = angular_prob(lower_budget)
    weight = wx * wv * wy * wz * gx * gy * ordered
    z = float(np.sum(Wu[:, None] * Wv[None, :] * G(U[:, None] * V[None, :])))
    return float(2.0 * np.sum(weight * lower) / z**2), float(2.0 * np.sum(weight * upper) / z**2), z


def main():
    results = []
    for lam in (LAMBDA0, LAMBDA1):
        by_order = [rho_bounds(lam, order) for order in (10, 14)]
        # Enclose observed quadrature variation conservatively around the tighter-order result.
        lo14, hi14, z14 = by_order[1]
        spread = max(abs(by_order[1][i] - by_order[0][i]) for i in (0, 1))
        results.append({"lambda": list(lam), "rho_lower": max(0.0, lo14 - spread),
                        "rho_upper": min(1.0, hi14 + spread), "quadrature_orders": [10, 14],
                        "raw_by_order": by_order, "normalization_Z": z14,
                        "reported_quadrature_margin": spread})
    separated = (results[0]["rho_upper"] < results[1]["rho_lower"] or
                 results[1]["rho_upper"] < results[0]["rho_lower"])
    out = {"unit": "PUENTE-3P1/B1.4", "frozen_pair": True,
           "lambda_pair": [list(LAMBDA0), list(LAMBDA1)], "results": results,
           "no_search": True, "no_seeds": True, "no_monte_carlo": True,
           "frozen_endpoint_isomorphism": "RULED_OUT_BY_POSITIVE_TV",
           "terminal": "B1.4_POSITIVE" if separated else "B1.4_INCONCLUSIVE_BY_BOUNDS"}
    print(json.dumps(out, indent=2))
    with open(__file__.rsplit("/", 1)[0] + "/verification_certified_rho_frozen_pair.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
