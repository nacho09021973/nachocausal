"""PUENTE-3P1 / B2 — corrected-kernel local identifiability audit.

This is deliberately a separate artifact from the historical B2.2 run.  It
keeps the frozen path and t0, imports the corrected physical q kernel, and
uses the strengthened B1.4 angular lower/upper bounds.  The numerical
quadrature audit is reported separately from the analytic enclosure: two
nearby Gauss orders are evidence of stability, not a formal remainder bound.
Consequently this script cannot emit POSITIVE until a genuine quadrature
remainder certificate is supplied.
"""
import json
import math
from pathlib import Path

import numpy as np
from scipy.special import lambertw, roots_legendre

HERE = Path(__file__).resolve().parent

L0 = np.array((0.5, 1.0, 1.0, 0.5, 0.1))
L1 = np.array((0.2, 0.8, 2.0, 0.9, 0.1))
T0 = 0.5


def s_of_uv(uv):
    return 1.0 + lambertw(-np.asarray(uv) / math.e, 0).real


def G(uv):
    s = s_of_uv(uv)
    return s * np.exp(-s)


def q(uv):
    s = s_of_uv(uv)
    return 2.0 * np.exp(-0.5 * s) / s ** 1.5


def path(t):
    return (1.0 - t) * L0 + t * L1


def angular_prob(budget):
    return (1.0 - np.cos(np.minimum(math.pi, np.maximum(0.0, budget)))) / 2.0


def pair_h_bounds(ux, vx, uy, vy):
    """Corrected B1.4 bounds for the angularly averaged causal kernel."""
    ordered = (ux <= uy) & (vx <= vy)
    du, dv = np.maximum(uy - ux, 0.0), np.maximum(vy - vx, 0.0)

    # B1.4 upper bound: pointwise q_max(V), followed by Cauchy--Schwarz.
    un, uw = roots_legendre(16)
    tt = (un + 1.0) / 2.0
    vq = vx[..., None] + dv[..., None] * tt
    uq = np.where(vq >= 0.0, uy[..., None], ux[..., None])
    qsq = q(uq * vq) ** 2
    upper_budget = np.sqrt(du * np.maximum(dv * np.sum(uw * qsq, axis=-1) / 2.0, 0.0))

    # B1.4 lower bound: maximum over the fixed, preregistered 19-knot family.
    pn, pw = roots_legendre(12)
    vm = (vx + vy) / 2.0
    lower_budget = np.zeros_like(du)
    for beta in np.linspace(0.05, 0.95, 19):
        um = ux + beta * (uy - ux)
        total = np.zeros_like(du)
        for a, b, ua, ub in ((vx, vm, ux, um), (vm, vy, um, uy)):
            slope = (ub - ua) / np.where(b > a, b - a, 1.0)
            vv = a[..., None] + (b - a)[..., None] * (pn + 1.0) / 2.0
            uu = ua[..., None] + slope[..., None] * (vv - a[..., None])
            total += np.sqrt(np.maximum(slope, 0.0)) * np.sum(
                pw * q(uu * vv), axis=-1
            ) * (b - a) / 2.0
        lower_budget = np.maximum(lower_budget, total)
    lower_budget[~ordered] = 0.0
    return angular_prob(lower_budget), angular_prob(upper_budget)


def evaluate(lam, order):
    v0, v1, uout, uin, _ = lam
    ulo, uhi = -uout, uin
    nodes, weights = roots_legendre(order)
    V = (nodes + 1.0) * (v1 - v0) / 2.0 + v0
    Wv = weights * (v1 - v0) / 2.0
    U = (nodes + 1.0) * (uhi - ulo) / 2.0 + ulo
    Wu = weights * (uhi - ulo) / 2.0
    z = float(np.sum(Wu[:, None] * Wv[None, :] * G(U[:, None] * V[None, :])))

    ds = L1 - L0
    speeds = (-ds[2], ds[3], ds[0], ds[1])
    a_prime = (
        speeds[0] * np.sum(Wv * G(ulo * V))
        + speeds[1] * np.sum(Wv * G(uhi * V))
        + speeds[2] * np.sum(Wu * G(U * v0))
        + speeds[3] * np.sum(Wu * G(U * v1))
    )

    yu, yv = np.meshgrid(U, V, indexing="ij")
    yw = Wu[:, None] * Wv[None, :] * G(yu * yv)
    b_ranges = []
    faces = ((ulo, v0, speeds[0], V, Wv), (uhi, v0, speeds[1], V, Wv),
             (v0, None, speeds[2], U, Wu), (v1, None, speeds[3], U, Wu))
    for face, _, speed, other, other_w in faces:
        if other is V:
            xU, xV, xW = np.full_like(other, face), other, other_w
        else:
            xU, xV, xW = other, np.full_like(other, face), other_w
        lo_h, hi_h = pair_h_bounds(xU[:, None, None], xV[:, None, None],
                                   yu[None, :, :], yv[None, :, :])
        inner_lo = np.sum(yw[None, :, :] * lo_h, axis=(1, 2))
        inner_hi = np.sum(yw[None, :, :] * hi_h, axis=(1, 2))
        vals = (np.sum(xW * G(xU * xV) * inner_lo),
                np.sum(xW * G(xU * xV) * inner_hi))
        b_ranges.append((speed * vals[0], speed * vals[1]) if speed >= 0
                        else (speed * vals[1], speed * vals[0]))
    b_lo, b_hi = 2.0 * sum(x[0] for x in b_ranges), 2.0 * sum(x[1] for x in b_ranges)

    ux, vx, uy, vy = np.meshgrid(U, V, U, V, indexing="ij")
    ww = np.meshgrid(Wu, Wv, Wu, Wv, indexing="ij")
    weight = ww[0] * ww[1] * ww[2] * ww[3] * G(ux * vx) * G(uy * vy)
    blo, bhi = pair_h_bounds(ux, vx, uy, vy)
    B_lo, B_hi = float(np.sum(weight * blo)), float(np.sum(weight * bhi))
    rho_lo, rho_hi = B_lo / z**2, B_hi / z**2
    candidates = [b / z**2 - 2 * rho * a_prime / z
                  for b in (b_lo, b_hi) for rho in (rho_lo, rho_hi)]
    return min(candidates), max(candidates), z, (a_prime, B_lo, B_hi)


def main():
    raw = [evaluate(path(T0), order) for order in (10, 14, 18)]
    observed_margin = max(abs(raw[-1][i] - raw[-2][i]) for i in (0, 1))
    numerical_interval = [raw[-1][0] - observed_margin, raw[-1][1] + observed_margin]
    # Explicit gate: observed order-to-order stability is not a theorem about
    # the quadrature remainder, so it cannot support the strong terminal.
    quadrature_error_certificate = {
        "status": "MISSING_FORMAL_REMAINDER_BOUND",
        "orders": [10, 14, 18],
        "observed_last_step_margin": observed_margin,
        "is_certified": False,
        "reason": "Gauss-order differences bound observed variation only; no outward-rounded interval quadrature or analytic remainder estimate is implemented.",
    }
    strong_positive = quadrature_error_certificate["is_certified"] and (
        numerical_interval[0] > 0 or numerical_interval[1] < 0
    )
    out = {
        "unit": "PUENTE-3P1/B2_CORRECTED_KERNEL",
        "path": "lambda(t)=(1-t)*lambda0+t*lambda1",
        "lambda0": L0.tolist(), "lambda1": L1.tolist(), "t0": T0,
        "kernel": "q(uv)=2*exp(-s(uv)/2)/s(uv)^(3/2)",
        "raw_orders": raw,
        "numerical_stability_interval": numerical_interval,
        "quadrature_error_certificate": quadrature_error_certificate,
        "no_new_path": True, "no_new_t0": True, "no_search": True,
        "no_seeds": True, "no_monte_carlo": True,
        "terminal": "B2_CORRECTED_POSITIVE" if strong_positive
        else "B2_CORRECTED_INCONCLUSIVE_BY_BOUNDS",
    }
    print(json.dumps(out, indent=2))
    with open(HERE / "verification_b2_corrected_kernel.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
