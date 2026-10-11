"""B2 gate, feasibility probe: the ideal interval of S at the frozen t0.

Not a certificate.  It asks whether the signed gate (0 not in enclosure of
S = B' - 2 (Z'/Z) B, amendment 2026-10-11) can succeed AT ALL with the only
pointwise information B1.5's chain rests on:

    p(b_line(x,y)) <= h(x,y) <= p(a_CS(x,y))        (H1b, H1a of B1.5 section 7)

b_line is the budget of the explicit straight segment; a_CS the Cauchy-Schwarz
bound.  Any certified chain built on these two inequalities -- B1.5's included,
which further relaxes p by polynomials and anchors the profile -- can only be
WIDER than the interval computed here.  So if this interval contains zero, no
refinement of that chain certifies the sign at t0; if it excludes zero, the
certified build is worth attempting and this gives its target.

Integration error is separated from angular slack by repeating the quadrature
at increasing order: the width that does not shrink is the angular slack.

Faces move with outward normal velocity v_n (dev/B2_2_SIGN_BUG_2026-10-11.md):
U=-u_out: +u_out',  U=u_in: +u_in',  V=v0: -v0',  V=v1: +v1'.

Usage: .venv/bin/python dev/explore_b2_gate_ideal_interval.py
"""
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.special import roots_legendre

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research_program/puente_3p1/2026-09-12/B1"))
from verify_certified_rho_frozen_pair import G, q  # noqa: E402

L0 = np.array((0.5, 1.0, 1.0, 0.5, 0.1))
L1 = np.array((0.2, 0.8, 2.0, 0.9, 0.1))
T0 = 0.5
TAU_NODES = 16


def p(b):
    return (1.0 - np.cos(np.minimum(math.pi, np.maximum(0.0, b)))) / 2.0


TN, TW = roots_legendre(TAU_NODES)
TN, TW = (TN + 1.0) / 2.0, TW / 2.0


def h_bounds(ux, vx, uy, vy):
    """Pointwise [p(b_line), p(a_CS)] for every pair; 0 for unordered pairs."""
    fwd = (ux <= uy) & (vx <= vy)
    bwd = (uy <= ux) & (vy <= vx)
    # orient every ordered pair as past -> future
    pu = np.where(fwd, ux, uy); pv = np.where(fwd, vx, vy)
    fu = np.where(fwd, uy, ux); fv = np.where(fwd, vy, vx)
    du, dv = np.maximum(fu - pu, 0.0), np.maximum(fv - pv, 0.0)
    V = pv[..., None] + dv[..., None] * TN
    Uline = pu[..., None] + du[..., None] * TN
    b_line = np.sqrt(du * dv) * np.sum(TW * q(Uline * V), axis=-1)
    a_cs = np.sqrt(du * dv * np.sum(TW * q(fu[..., None] * V) ** 2, axis=-1))
    ordered = fwd | bwd
    return np.where(ordered, p(b_line), 0.0), np.where(ordered, p(a_cs), 0.0)


def ideal_interval(n):
    v0, v1, uout, uin, _ = (1.0 - T0) * L0 + T0 * L1
    d = L1 - L0
    xn, xw = roots_legendre(n)
    U = (xn + 1.0) * (uin + uout) / 2.0 - uout; Wu = xw * (uin + uout) / 2.0
    V = (xn + 1.0) * (v1 - v0) / 2.0 + v0; Wv = xw * (v1 - v0) / 2.0
    yu, yv = np.meshgrid(U, V, indexing="ij")
    yw = (Wu[:, None] * Wv[None, :] * G(yu * yv)).ravel()
    yu, yv = yu.ravel(), yv.ravel()
    Z = yw.sum()

    # B over K x K, chunked over x
    B_lo = B_hi = 0.0
    for i in range(len(yu)):
        lo, hi = h_bounds(yu[i], yv[i], yu, yv)
        B_lo += yw[i] * np.dot(yw, lo)
        B_hi += yw[i] * np.dot(yw, hi)

    faces = (("U=-u_out", np.full(n, -uout), V, Wv, d[2]),
             ("U=u_in", np.full(n, uin), V, Wv, d[3]),
             ("V=v0", U, np.full(n, v0), Wu, -d[0]),
             ("V=v1", U, np.full(n, v1), Wu, d[1]))
    Zp = 0.0
    Bp_lo = Bp_hi = 0.0
    per_face = {}
    for name, fu, fv, fw, vn in faces:
        gx = fw * G(fu * fv)
        lo, hi = h_bounds(fu[:, None], fv[:, None], yu[None, :], yv[None, :])
        H_lo, H_hi = lo @ yw, hi @ yw
        f_lo, f_hi = 2.0 * vn * np.dot(gx, H_lo), 2.0 * vn * np.dot(gx, H_hi)
        Bp_lo += min(f_lo, f_hi); Bp_hi += max(f_lo, f_hi)
        Zp += vn * gx.sum()
        per_face[name] = {"v_n": float(vn), "Bprime_contrib": [min(f_lo, f_hi), max(f_lo, f_hi)]}
    assert Zp > 0
    k = 2.0 * Zp / Z
    S_lo, S_hi = Bp_lo - k * B_hi, Bp_hi - k * B_lo
    return {"n": n, "Z": Z, "Zprime": Zp, "B": [B_lo, B_hi], "Bprime": [Bp_lo, Bp_hi],
            "two_Zp_over_Z_times_B": [k * B_lo, k * B_hi],
            "rho": [B_lo / Z**2, B_hi / Z**2],
            "S": [S_lo, S_hi], "drho_dt": [S_lo / Z**2, S_hi / Z**2],
            "S_excludes_zero": bool(S_lo > 0 or S_hi < 0), "faces": per_face}


def main():
    runs = [ideal_interval(n) for n in (16, 24, 32)]
    out = {"probe": "B2 gate ideal interval at t0=0.5 (diagnostic, not a certificate)",
           "pointwise_information": "p(b_line) <= h <= p(a_CS)", "tau_nodes": TAU_NODES,
           "runs": runs}
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
