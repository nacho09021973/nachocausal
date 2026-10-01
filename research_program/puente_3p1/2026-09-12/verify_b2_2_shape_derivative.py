"""PUENTE-3P1 / B2.2 — direct shape derivative enclosure at frozen t0.

The derivative is obtained from boundary transport terms, not finite differences.
"""
import json
import math
import sys
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "B1"))
from verify_certified_rho_frozen_pair import G, q  # noqa: E402

L0 = np.array((0.5, 1.0, 1.0, 0.5, 0.1))
L1 = np.array((0.2, 0.8, 2.0, 0.9, 0.1))
T0 = 0.5


def path(t):
    return (1.0 - t) * L0 + t * L1


def angular_prob(b):
    return (1.0 - np.cos(np.minimum(math.pi, np.maximum(0.0, b)))) / 2.0


def pair_h_bounds(ux, vx, uy, vy):
    """Pointwise lower/upper bounds for the angularly averaged causal kernel."""
    forward = (ux <= uy) & (vx <= vy)
    backward = (uy <= ux) & (vy <= vx)
    ordered = forward | backward
    ax, bx = np.minimum(ux, uy), np.maximum(ux, uy)
    av, bv = np.minimum(vx, vy), np.maximum(vx, vy)
    du, dv = np.maximum(bx - ax, 0.0), np.maximum(bv - av, 0.0)
    qrect = np.maximum.reduce([q(ax * av), q(ax * bv), q(bx * av), q(bx * bv)])
    upper = qrect * np.sqrt(du * dv)
    # Explicit midpoint two-segment path; valid for every ordered pair.
    vm, um = (av + bv) / 2.0, ax + 0.5 * (bx - ax)
    den1, den2 = np.where(vm > av, vm - av, 1.0), np.where(bv > vm, bv - vm, 1.0)
    sl1, sl2 = (um - ax) / den1, (bx - um) / den2
    pn, pw = roots_legendre(8)
    tt = (pn + 1.0) / 2.0
    vv1 = av[..., None] + (vm - av)[..., None] * tt
    vv2 = vm[..., None] + (bv - vm)[..., None] * tt
    uu1 = ax[..., None] + sl1[..., None] * (vv1 - av[..., None])
    uu2 = um[..., None] + sl2[..., None] * (vv2 - vm[..., None])
    lower = (np.sqrt(np.maximum(sl1, 0.0)) *
             np.sum(pw * q(uu1 * vv1), axis=-1) * (vm - av) / 2.0 +
             np.sqrt(np.maximum(sl2, 0.0)) *
             np.sum(pw * q(uu2 * vv2), axis=-1) * (bv - vm) / 2.0)
    lower[~ordered] = 0.0
    return angular_prob(lower), angular_prob(upper)


def evaluate(lam, order, parameter_speeds=None):
    v0, v1, uout, uin, _ = lam
    ulo, uhi = -uout, uin
    n, w = roots_legendre(order)
    V = (n + 1.0) * (v1 - v0) / 2.0 + v0
    Wv = w * (v1 - v0) / 2.0
    U = (n + 1.0) * (uhi - ulo) / 2.0 + ulo
    Wu = w * (uhi - ulo) / 2.0
    z = float(np.sum(Wu[:, None] * Wv[None, :] * G(U[:, None] * V[None, :])))

    # Exact deterministic first variation of A from the four moving faces.
    if parameter_speeds is None:
        parameter_speeds = L1 - L0
    speeds = (-parameter_speeds[2], parameter_speeds[3],
              parameter_speeds[0], parameter_speeds[1])
    face_specs = ((ulo, speeds[0], V, Wv), (uhi, speeds[1], V, Wv),
                  (None, speeds[2], U, Wu), (None, speeds[3], U, Wu))
    a_prime = (speeds[0] * np.sum(Wv * G(ulo * V)) +
               speeds[1] * np.sum(Wv * G(uhi * V)) +
               speeds[2] * np.sum(Wu * G(U * v0)) +
               speeds[3] * np.sum(Wu * G(U * v1)))

    # Boundary contributions to B'. For signed face speed, select h lower/upper accordingly.
    b_ranges = []
    for face, speed, other, other_w in face_specs:
        if face is not None:
            fx, fy = np.meshgrid(np.array([face]), other, indexing="ij")
            xU, xV = fx.ravel(), fy.ravel()
            xW = other_w
        else:
            fx, fy = np.meshgrid(other, np.array([face if face is not None else 0.0]), indexing="ij")
            # For V faces, the sentinel is replaced below by the actual face coordinate.
            face_v = v0 if speed == speeds[2] else v1
            xU, xV = fx[:, 0], np.full_like(fx[:, 0], face_v)
            xW = Wu
        # Integrate over y=K with a tensor grid.
        yu, yv = np.meshgrid(U, V, indexing="ij")
        yw = Wu[:, None] * Wv[None, :] * G(yu * yv)
        xxu = xU[:, None, None]
        xxv = xV[:, None, None]
        lo_h, hi_h = pair_h_bounds(xxu, xxv, yu[None, :, :], yv[None, :, :])
        inner_lo = np.sum(yw[None, :, :] * lo_h, axis=(1, 2))
        inner_hi = np.sum(yw[None, :, :] * hi_h, axis=(1, 2))
        vals_lo = np.sum(xW * G(xU * xV) * inner_lo)
        vals_hi = np.sum(xW * G(xU * xV) * inner_hi)
        b_ranges.append((speed * vals_lo, speed * vals_hi) if speed >= 0 else
                        (speed * vals_hi, speed * vals_lo))
    b_lo = 2.0 * sum(x[0] for x in b_ranges)
    b_hi = 2.0 * sum(x[1] for x in b_ranges)
    # B itself is bounded by the same pair kernel over KxK.
    ux, vx, uy, vy = np.meshgrid(U, V, U, V, indexing="ij")
    ww = np.meshgrid(Wu, Wv, Wu, Wv, indexing="ij")
    weight = ww[0] * ww[1] * ww[2] * ww[3] * G(ux * vx) * G(uy * vy)
    blo, bhi = pair_h_bounds(ux, vx, uy, vy)
    B_lo, B_hi = float(np.sum(weight * blo)), float(np.sum(weight * bhi))
    # Conservative interval propagation for rho'.
    rho_lo, rho_hi = B_lo / z**2, B_hi / z**2
    candidates = [b_lo / z**2 - 2 * rho * a_prime / z for b in (b_lo, b_hi)
                  for rho in (rho_lo, rho_hi)]
    return min(candidates), max(candidates), z, (a_prime, B_lo, B_hi)


def main():
    lam = path(T0)
    vals = [evaluate(lam, n) for n in (10, 14)]
    lo, hi = vals[-1][0], vals[-1][1]
    margin = max(abs(vals[-1][i] - vals[0][i]) for i in (0, 1))
    interval = [lo - margin, hi + margin]
    out = {"unit": "PUENTE-3P1/B2.2", "path_frozen": True, "t0": T0,
           "raw_orders": vals, "reported_quadrature_margin": margin,
           "drho_dt_enclosure": interval, "no_finite_difference": True,
           "no_search": True, "no_seeds": True, "no_monte_carlo": True,
           "terminal": "B2.2_POSITIVE_DERIVATIVE" if interval[0] > 0 or interval[1] < 0
           else "B2.2_INCONCLUSIVE_BY_BOUNDS"}
    print(json.dumps(out, indent=2))
    with open(HERE / "verification_b2_2_shape_derivative.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
