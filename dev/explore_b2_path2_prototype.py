"""B2 path 2, float prototype of the exact bounding scheme (NOT a certificate).

Question: with the bounds a certificate would actually use -- cell-level, not
pointwise -- does S_lo stay above zero, and at what resolution?

Key structural fact.  Delta_max is the time separation of the 2D Lorentzian
metric q(UV)^2 dU dV (dev/B2_NEW_REPRESENTATION_2026-10-11.md), so it obeys the
reverse triangle inequality: concatenating future causal curves gives a future
causal curve.  For x in cell P and y in cell Q,

    P_top <= Q_bot   ==>   Delta(x,y) >= Delta(P_top, Q_bot)      (lower)
    P_bot <= Q_top   ==>   Delta(x,y) <= Delta(P_bot, Q_top)      (upper)

so every cell pair is bounded by ONE pair of lattice corners.  Lower bounds use
the straight-line budget between the corners; upper bounds use
min(calibration inf_c, Cauchy-Schwarz) between the corners.

Only S_lo = B'_lo - (2 Z'/Z) B_hi is needed (amendment: exclude zero; the
expected sign is positive).  B'_lo takes the LOWER bound of H on the three faces
with v_n > 0 and the UPPER bound on V = v1 (v_n < 0); B_hi takes the upper bound.

Floats throughout; Z, Z' and cell weights by Gauss-Legendre.  The certificate
would replace each with directed-rounding enclosures.
Usage: .venv/bin/python dev/explore_b2_path2_prototype.py [M ...]
"""
import json
import math
import sys
from pathlib import Path

import numpy as np
from numba import njit, prange
from scipy.special import roots_legendre

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "dev"))
import explore_b2_calibration_band as cb  # noqa: E402

LAM = cb.LAM
V0, V1, UOUT, UIN, _ = LAM
D = cb.L1 - cb.L0
# outward normal velocities: U=-u_out, U=u_in, V=v0, V=v1
VN = {"U=-u_out": D[2], "U=u_in": D[3], "V=v0": -D[0], "V=v1": D[1]}
QT = np.sqrt(cb.FT)            # q on the w table
TN, TW = roots_legendre(16)
TN, TW = (TN + 1.0) / 2.0, TW / 2.0

C_LIST = np.array(sorted(cb.PHI))
PHI_TAB = np.stack([np.nan_to_num(cb.PHI[c], nan=0.0) for c in C_LIST])
C_WLO = np.array([cb.VALID[c][0] for c in C_LIST])
C_WHI = np.array([cb.VALID[c][1] for c in C_LIST])


@njit(cache=True)
def interp(x, xs, ys):
    n = xs.size
    t = (x - xs[0]) / (xs[n - 1] - xs[0]) * (n - 1)
    i = min(max(int(t), 0), n - 2)
    f = t - i
    return ys[i] * (1.0 - f) + ys[i + 1] * f


@njit(parallel=True, cache=True)
def corner_bounds(PU, PV, A, c_list, c_wlo, c_whi, wt, qt, tn, tw):
    """lb[a,b], ub[a,b] for lattice points a <= b (componentwise); 0 otherwise."""
    n = PU.size
    lb = np.zeros((n, n))
    ub = np.zeros((n, n))
    for a in prange(n):
        for b in range(n):
            du, dv = PU[b] - PU[a], PV[b] - PV[a]
            if du <= 0.0 or dv <= 0.0:
                continue
            line = 0.0
            cs2 = 0.0
            for k in range(tn.size):
                v = PV[a] + dv * tn[k]
                line += tw[k] * interp((PU[a] + du * tn[k]) * v, wt, qt)
                qq = interp(PU[b] * v, wt, qt)
                cs2 += tw[k] * qq * qq
            lb[a, b] = math.sqrt(du * dv) * line
            best = math.sqrt(du * dv * cs2)
            w1, w2 = PU[a] * PV[a], PU[a] * PV[b]
            w3, w4 = PU[b] * PV[a], PU[b] * PV[b]
            wlo = min(min(w1, w2), min(w3, w4))
            whi = max(max(w1, w2), max(w3, w4))
            for j in range(c_list.size):
                if wlo >= c_wlo[j] and whi <= c_whi[j]:
                    val = A[j, b] - A[j, a]
                    if val < best:
                        best = val
            ub[a, b] = best
    return lb, ub


def p(b):
    return (1.0 - np.cos(np.minimum(math.pi, np.maximum(0.0, b)))) / 2.0


def p_inplace(b):
    """p(b) overwriting b, to keep the (M+1)^4 corner tables to one copy each."""
    np.clip(b, 0.0, math.pi, out=b)
    np.cos(b, out=b)
    b *= -0.5
    b += 0.5
    return b


def cell_weights(Ug, Vg, order=8):
    """W[i,j] = int over cell (U_i..U_i+1) x (V_j..V_j+1) of G(UV)."""
    xn, xw = roots_legendre(order)
    xn, xw = (xn + 1.0) / 2.0, xw / 2.0
    du, dv = np.diff(Ug), np.diff(Vg)
    U = Ug[:-1, None] + du[:, None] * xn
    V = Vg[:-1, None] + dv[:, None] * xn
    g = cb.gate.G(U[:, None, :, None] * V[None, :, None, :])
    return np.einsum("ijkl,k,l->ij", g, xw, xw) * du[:, None] * dv[None, :]


def segment_weights(fixed, Other, along_U, order=8):
    xn, xw = roots_legendre(order)
    xn, xw = (xn + 1.0) / 2.0, xw / 2.0
    d = np.diff(Other)
    pts = Other[:-1, None] + d[:, None] * xn
    w = fixed * pts
    return (cb.gate.G(w) * xw).sum(-1) * d


def run(M):
    Ug = np.linspace(-UOUT, UIN, M + 1)
    Vg = np.linspace(V0, V1, M + 1)
    iu, iv = np.meshgrid(np.arange(M + 1), np.arange(M + 1), indexing="ij")
    PU, PV = Ug[iu].ravel(), Vg[iv].ravel()
    pid = lambda i, j: i * (M + 1) + j
    A = np.stack([c * np.log(PV) + np.interp(PU * PV, cb.WT, PHI_TAB[k])
                  for k, c in enumerate(C_LIST)])
    lb, ub = corner_bounds(PU, PV, A, C_LIST, C_WLO, C_WHI, cb.WT, QT, TN, TW)
    plb = p_inplace(lb); del lb
    pub = p_inplace(ub); del ub

    W = cell_weights(Ug, Vg)
    Z = W.sum()
    ci, cj = np.meshgrid(np.arange(M), np.arange(M), indexing="ij")
    ci, cj = ci.ravel(), cj.ravel()
    Wc = W.ravel()
    bot = pid(ci, cj)
    top = pid(ci + 1, cj + 1)

    # B_hi: 2 * sum over cell pairs (P,Q) of W_P W_Q p(UB(P_bot, Q_top))
    B_hi = 2.0 * float(Wc @ pub[np.ix_(bot, top)] @ Wc)

    faces = {
        "U=-u_out": (np.zeros(M, int), np.arange(M), True, -UOUT),
        "U=u_in": (np.full(M, M), np.arange(M), True, UIN),
        "V=v0": (np.arange(M), np.zeros(M, int), False, V0),
        "V=v1": (np.arange(M), np.full(M, M), False, V1),
    }
    Bp_lo = 0.0
    Zp = 0.0
    detail = {}
    for name, (fi, fj, along_V, fixed) in faces.items():
        if along_V:   # face at fixed U; segment k from (fi, k) to (fi, k+1)
            s0, s1 = pid(fi, fj), pid(fi, fj + 1)
            fw = segment_weights(fixed, Vg, True)
        else:         # face at fixed V; segment k from (k, fj) to (k+1, fj)
            s0, s1 = pid(fi, fj), pid(fi + 1, fj)
            fw = segment_weights(fixed, Ug, False)
        vn = VN[name]
        Zp += vn * fw.sum()
        if vn > 0:   # lower bound of H on the face
            fwd = plb[np.ix_(s1, bot)]          # x <= s1 <= Q_bot <= y
            bwd = plb[np.ix_(top, s0)].T        # y <= Q_top <= s0 <= x
            H = (fwd + bwd) @ Wc
        else:        # upper bound of H on the face
            fwd = pub[np.ix_(s0, top)]          # s0 <= x <  y <= Q_top
            bwd = pub[np.ix_(bot, s1)].T        # Q_bot <= y < x <= s1
            H = (fwd + bwd) @ Wc
        contrib = 2.0 * vn * float(fw @ H)
        Bp_lo += contrib
        detail[name] = contrib
    k = 2.0 * Zp / Z
    return {"M": M, "Z": Z, "Zprime": Zp, "B_hi": B_hi, "Bprime_lo": Bp_lo,
            "faces": detail, "S_lo": Bp_lo - k * B_hi}


def main():
    Ms = [int(a) for a in sys.argv[1:]] or [16, 32, 64]
    for M in Ms:
        print(json.dumps(run(M)), flush=True)


if __name__ == "__main__":
    main()
