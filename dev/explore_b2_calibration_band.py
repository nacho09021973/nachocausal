"""B2, new representation probe: Delta_max as a 2D Lorentzian time separation.

B1.2 section 2 defines Delta_max(x,y) = sup_U int q(UV) sqrt(U') dV over monotone
U(V).  That is exactly the maximal proper time of the 2D metric

    ds^2 = F(w) dU dV,     F = q^2,  w = UV.

In coordinates (w, nu) = (UV, ln V) the metric is F(w)(dw dnu - w dnu^2): it does
not depend on nu (the boost Killing field) and is regular across w = 0.

UPPER BOUND (calibration).  For a future causal tangent write a = nu' >= 0 and
b = w' - w nu' >= 0 (b is proportional to U').  Then dtau = sqrt(F a b), and for
W = c nu + Phi(w),  dW = Phi' b + (Phi' w + c) a >= 2 sqrt(Phi'(Phi' w + c) a b)
by AM-GM.  So dW >= dtau along every future causal curve as soon as

    Phi' >= 0,  Phi' w + c >= 0,  4 Phi'(Phi' w + c) >= F.

The smallest such Phi' is Phi_c' = F / (2 (c + sqrt(c^2 + F w))), valid wherever
c^2 + F w >= 0 and c + sqrt(c^2 + F w) > 0.  Then for every such c on the causal
rectangle of (x, y):

    Delta_max(x,y) <= W_c(y) - W_c(x)  =  c (nu_y - nu_x) + Phi_c(w_y) - Phi_c(w_x).

LOWER BOUND (explicit curve).  Equality in AM-GM fixes b/a, which gives the
geodesic of constant c:  dw/dnu = 2w + c/Phi_c'(w).  It is monotone in c, so c is
found by bisection to hit w_y at nu_y; its proper time, integrated along the
curve, is a lower bound (any admissible curve is).

Diagnostic only: tables and quadratures are floats, no directed rounding.
Usage: .venv/bin/python dev/explore_b2_calibration_band.py
"""
import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "dev"))
import explore_b2_gate_ideal_interval as gate  # noqa: E402

q = gate.q
L0, L1 = gate.L0, gate.L1

# --- tables over w ---------------------------------------------------------
LAM = (1.0 - 0.5) * L0 + 0.5 * L1
W_MIN, W_MAX = -LAM[2] * LAM[1] - 1e-9, LAM[3] * LAM[1] + 1e-9
WT = np.linspace(W_MIN, W_MAX, 40001)
FT = q(WT) ** 2
C_POS = np.geomspace(1e-3, 50.0, 260)
C_NEG = -np.geomspace(1e-3, 50.0, 120)


def F(w):
    return np.interp(w, WT, FT)


def phi_table(c):
    """Phi_c on the w table, NaN where invalid.  For c < 0 only w > 0 is valid."""
    disc = c * c + FT * WT
    den = c + np.sqrt(np.maximum(disc, 0.0))
    ok = (disc >= 0.0) & (den > 0.0) & ((c >= 0.0) | (WT > 0.0))
    fp = FT / (2.0 * np.where(ok, den, 1.0))
    phi = np.full(WT.shape, np.nan)
    # the valid set is one interval of the table; integrate across it
    idx = np.nonzero(ok)[0]
    if idx.size < 2:
        return phi
    i0, i1 = idx[0], idx[-1]
    seg = 0.5 * (fp[i0 + 1:i1 + 1] + fp[i0:i1]) * np.diff(WT[i0:i1 + 1])
    phi[i0:i1 + 1] = np.concatenate([[0.0], np.cumsum(seg)])
    return phi


PHI = {float(c): phi_table(c) for c in np.concatenate([C_POS, C_NEG])}
# validity range per c: the w-interval on which Phi_c is finite
VALID = {c: (WT[np.isfinite(ph)].min(), WT[np.isfinite(ph)].max()) for c, ph in PHI.items()}


def ub_calibration(ux, vx, uy, vy):
    """inf over the c-grid of W_c(y)-W_c(x); arrays of oriented pairs (x <= y)."""
    corners = np.stack([ux * vx, ux * vy, uy * vx, uy * vy])
    wlo, whi = corners.min(0), corners.max(0)
    wx, wy = ux * vx, uy * vy
    dnu = np.log(vy) - np.log(vx)
    best = np.full(ux.shape, np.inf)
    for c, ph in PHI.items():
        a, b = VALID[c]
        ok = (wlo >= a) & (whi <= b)
        if not ok.any():
            continue
        val = c * dnu + np.interp(wy, WT, np.nan_to_num(ph, nan=0.0)) \
            - np.interp(wx, WT, np.nan_to_num(ph, nan=0.0))
        best = np.where(ok, np.minimum(best, val), best)
    return best


def lb_geodesic(ux, vx, uy, vy):
    """Bisection on c so the constant-c geodesic from x hits w_y at nu_y."""
    wx, wy = ux * vx, uy * vy
    nux, nuy = np.log(vx), np.log(vy)
    lo = np.full(ux.shape, -50.0)
    hi = np.full(ux.shape, 50.0)
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        wend, _, bad = geodesic_c(wx, nux, nuy, mid)
        # w_end increases with c; an invalid c (c^2 + F w < 0, or c < 0 at w <= 0)
        # is one that is too small
        over = (wend > wy) & ~bad
        hi = np.where(over, mid, hi)
        lo = np.where(over, lo, mid)
    c = 0.5 * (lo + hi)
    wend, tau, bad = geodesic_c(wx, nux, nuy, c)
    miss = np.abs(wend - wy)
    return np.where(bad, np.nan, tau), miss


def geodesic_c(wx, nux, nuy, c, steps=96):
    h = (nuy - nux) / steps
    w = wx.copy(); tau = np.zeros_like(wx); bad = np.zeros(wx.shape, bool)

    def rhs(w):
        F_ = F(w)
        disc = c * c + F_ * w
        s = np.sqrt(np.maximum(disc, 0.0))
        den = c + s
        b_ = (disc < 0) | (den <= 0)
        fp = F_ / (2.0 * np.where(den > 0, den, 1e-300))
        dw = 2.0 * w + c / fp
        dtau = np.sqrt(np.maximum(F_ * (fp * w + c) / fp, 0.0))
        return dw, dtau, b_
    for _ in range(steps):
        k1, t1, b1 = rhs(w)
        k2, t2, b2 = rhs(w + 0.5 * h * k1)
        k3, t3, b3 = rhs(w + 0.5 * h * k2)
        k4, t4, b4 = rhs(w + h * k3)
        w = np.clip(w + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0, W_MIN, W_MAX)
        tau = tau + h * (t1 + 2 * t2 + 2 * t3 + t4) / 6.0
        bad |= b1 | b2 | b3 | b4
    return w, tau, bad


def orient(ux, vx, uy, vy):
    fwd = (ux <= uy) & (vx <= vy)
    bwd = (uy <= ux) & (vy <= vx)
    pu = np.where(fwd, ux, uy); pv = np.where(fwd, vx, vy)
    fu = np.where(fwd, uy, ux); fv = np.where(fwd, vy, vx)
    return pu, pv, fu, fv, fwd | bwd


def band(ux, vx, uy, vy):
    """[lower, upper] budget per pair, with the old line / CS bounds for comparison."""
    ux, vx, uy, vy = np.broadcast_arrays(*(np.asarray(a, float) for a in (ux, vx, uy, vy)))
    shape = ux.shape
    pu, pv, fu, fv, ordered = (a.ravel() for a in orient(ux, vx, uy, vy))
    nondeg = ordered & (fu > pu) & (fv > pv)
    out = {k: np.zeros(pu.shape) for k in ("line", "cs", "ub", "lb")}
    i = np.nonzero(nondeg)[0]
    if i.size:
        du, dv = fu[i] - pu[i], fv[i] - pv[i]
        T = gate.TN; Wt = gate.TW
        V = pv[i, None] + dv[:, None] * T
        out["line"][i] = np.sqrt(du * dv) * np.sum(Wt * q((pu[i, None] + du[:, None] * T) * V), -1)
        out["cs"][i] = np.sqrt(du * dv * np.sum(Wt * q(fu[i, None] * V) ** 2, -1))
        out["ub"][i] = np.minimum(ub_calibration(pu[i], pv[i], fu[i], fv[i]), out["cs"][i])
        lb, miss = lb_geodesic(pu[i], pv[i], fu[i], fv[i])
        lb = np.where(miss < 1e-6, lb, 0.0)
        out["lb"][i] = np.maximum(np.nan_to_num(lb), out["line"][i])
    return {k: v.reshape(shape) for k, v in out.items()}


def main():
    rng = np.random.default_rng(0)  # sample pairs only to report band widths
    v0, v1, uout, uin, _ = LAM
    n = 4000
    ux, uy = rng.uniform(-uout, uin, n), rng.uniform(-uout, uin, n)
    vx, vy = rng.uniform(v0, v1, n), rng.uniform(v0, v1, n)
    b = band(ux, vx, uy, vy)
    m = b["cs"] > 0
    rel = lambda a: float(np.median(a[m]))
    print(json.dumps({
        "pairs_ordered": int(m.sum()),
        "violations_lb_gt_ub": int(np.sum(b["lb"][m] > b["ub"][m] + 1e-9)),
        "median_width_old_cs_minus_line": rel(b["cs"] - b["line"]),
        "median_width_new_ub_minus_lb": rel(b["ub"] - b["lb"]),
        "median_relative_new_width": rel((b["ub"] - b["lb"]) / b["ub"]),
        "max_relative_new_width": float(np.max(((b["ub"] - b["lb"]) / b["ub"])[m])),
        "median_ub_over_cs": rel(b["ub"] / b["cs"]),
        "median_lb_over_line": rel(b["lb"] / np.maximum(b["line"], 1e-300)),
    }, indent=1))


if __name__ == "__main__":
    main()
