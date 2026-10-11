"""PUENTE-3P1 / B2 path 2 -- directed-rounding lower bound of S at the frozen t0.

Rule (dev/B2_PROMOTION_RULE_AMENDMENT_2026-10-11.md, signed by the PI):

    B2_CORRECTED_POSITIVE  iff  0 not in formal_enclosure(drho_dt),

with drho_dt = S / Z^2 and S = B' - 2 (Z'/Z) B.  The expected sign is positive,
so this file builds only a certified LOWER bound S_lo; S_lo > 0 gives the
one-sided enclosure [S_lo/Z_hi^2, +inf) of drho_dt, which excludes zero.

Representation (dev/B2_NEW_REPRESENTATION_2026-10-11.md).  Delta_max(x,y) is the
time separation of the 2D Lorentzian metric F(w) dU dV, F = q^2, w = UV.
  * Reverse triangle inequality: for x in cell P and y in cell Q,
        P_top <= Q_bot  =>  Delta(x,y) >= Delta(P_top, Q_bot),
        P_bot <= Q_top  =>  Delta(x,y) <= Delta(P_bot, Q_top),
    so every cell pair is bounded by ONE pair of lattice corners.
  * Lower corner bound: straight-line budget sqrt(dU dV) int_0^1 q(w(tau)) dtau,
    a lower Riemann sum of q over the interval range of w on each tau-cell.
  * Upper corner bound: min of
      - Cauchy-Schwarz  sqrt(dU int q(U_b V)^2 dV)          (B1.2 section 3), and
      - calibration     c (nu_b - nu_a) + Phi_c(w_b) - Phi_c(w_a),  nu = ln V,
        Phi_c' = F / (2 (c + sqrt(c^2 + F w))), for every c valid on the causal
        rectangle (c^2 + F w >= 0 there, and c + sqrt(...) > 0).
    Each c gives a valid bound on its own, so the c grid needs no certification.
  * h = p(Delta) with p(b) = (1 - cos min(b, pi))/2, nondecreasing on [0, inf).

Which bound goes where (only S_lo is built):
  B'_lo = sum over faces of 2 v_n int_face w H,  H(x) = int_K w(y) h(x,y) dy;
          LOWER H on U=-u_out, U=u_in, V=v0 (v_n > 0), UPPER H on V=v1 (v_n < 0).
  B_hi  = 2 sum_{P,Q} W_P W_Q p(UB(P_bot, Q_top)).
  S_lo  = B'_lo - (2 Z'_hi / Z_lo) B_hi.

Arithmetic, following B1.5 section 5bis:
  * every binary64 operation is pushed one ulp outward (np.nextafter, also inside
    numba kernels); sums are directed sequential or directed prefix sums;
  * transcendental functions enter ONLY through certified monotone tables built
    with B1.5's audited scalar layer (s_encl / q_encl / G_encl, mpmath.iv, no
    Lambert W).  A lookup is rigorous by monotonicity alone: q increasing in w,
    G increasing for w <= 0 and decreasing for w >= 0 (0 is a table node), p
    nondecreasing.  Table indices are located by exact float comparisons;
  * ln V at the lattice nodes and the face velocities are enclosed exactly
    (mpmath.iv / fractions.Fraction);
  * the numba kernels are checked for fast-math / contraction flags in their
    LLVM IR, and that check is itself mutation-tested.

Frozen point convention (declared, as in B1.5): the certified point is the
binary64 lambda* = path(0.5) that the frozen B2 scripts evaluate, and the
direction is d = L1 - L0 taken exactly from the binary64 L0, L1.  The quantity is
the directional derivative of rho at lambda* along d.

Determinism: no seeds, no Monte Carlo, no search over lambda, t0 or points.
Usage: .venv/bin/python research_program/puente_3p1/2026-10-11/verify_b2_path2_gate_certificate.py [M]
"""
import json
import math
import re
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
from numba import njit, prange
from mpmath import iv

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "2026-09-12" / "B1"))
import verify_b1_5_analytic_separation as b15  # noqa: E402

INF = math.inf

# --- frozen inputs -----------------------------------------------------------
L0 = np.array((0.5, 1.0, 1.0, 0.5, 0.1))
L1 = np.array((0.2, 0.8, 2.0, 0.9, 0.1))
T0 = 0.5
LAM = (1.0 - T0) * L0 + T0 * L1          # binary64, exactly as the frozen scripts
V0, V1, UOUT, UIN = (float(x) for x in LAM[:4])
DFR = [Fraction(float(b)) - Fraction(float(a)) for a, b in zip(L0, L1)]
# outward normal velocities (dev/B2_2_SIGN_BUG_2026-10-11.md)
VN_FR = {"U=-u_out": DFR[2], "U=u_in": DFR[3], "V=v0": -DFR[0], "V=v1": DFR[1]}

# --- proof parameters (any values give a valid bound; larger = tighter) -------
M_DEFAULT = 128      # lattice cells per side
R_SUB = 8            # sub-cells per lattice cell for weights and CS integrals
N_TAU = 64           # tau-cells for the line budget
NT_HALF = 2 ** 15    # w-table nodes on each side of w = 0
NP = 2 ** 17         # p-table nodes on [0, P_MAX]
P_MAX = 3.2
C_POS = np.geomspace(1e-3, 50.0, 260)
C_NEG = -np.geomspace(1e-3, 50.0, 120)


def up(x):
    return np.nextafter(x, INF)


def dn(x):
    return np.nextafter(x, -INF)


def frac_iv(fr):
    return float(dn(float(fr))), float(up(float(fr)))


# ---------------------------------------------------------------------------
# 1. Certified monotone tables.
# ---------------------------------------------------------------------------
def w_table():
    wlo = float(dn(-UOUT * V1)) - 1e-3
    whi = float(up(UIN * V1)) + 1e-3
    left = np.linspace(wlo, 0.0, NT_HALF + 1)
    right = np.linspace(0.0, whi, NT_HALF + 1)[1:]
    wt = np.concatenate([left, right])
    assert np.all(np.diff(wt) > 0) and wt[NT_HALF] == 0.0
    return wt


def certified_tables(wt):
    qlo = np.empty_like(wt); qhi = np.empty_like(wt)
    glo = np.empty_like(wt); ghi = np.empty_like(wt)
    for k, w in enumerate(wt):
        qlo[k], qhi[k] = b15.q_encl(float(w))
        glo[k], ghi[k] = b15.G_encl(float(w))
    Flo = dn(qlo * qlo)
    Fhi = up(qhi * qhi)
    return qlo, qhi, glo, ghi, Flo, Fhi


def p_table():
    bt = np.linspace(0.0, P_MAX, NP + 1)
    plo = np.empty_like(bt); phi = np.empty_like(bt)
    pi_iv = iv.pi
    for k, b in enumerate(bt):
        B = iv.mpf(float(b))
        if B.a >= pi_iv.b:                 # certified b >= pi: p = 1
            plo[k] = phi[k] = 1.0
            continue
        if B.b <= pi_iv.a:                 # certified b <= pi
            val = (iv.mpf(1) - iv.cos(B)) / 2
            plo[k], phi[k] = b15.iv_lo(val), min(1.0, b15.iv_hi(val))
        else:                              # b within rounding of pi
            val = (iv.mpf(1) - iv.cos(iv.mpf([pi_iv.a, float(b)]))) / 2
            plo[k], phi[k] = b15.iv_lo(val), 1.0
    return bt, plo, phi


def nu_enclosures(Vg):
    lo = np.empty_like(Vg); hi = np.empty_like(Vg)
    for j, v in enumerate(Vg):
        x = iv.log(iv.mpf(float(v)))
        lo[j], hi[j] = b15.iv_lo(x), b15.iv_hi(x)
    return lo, hi


# ---------------------------------------------------------------------------
# 2. Numba kernels.  Directed rounding by np.nextafter after every operation.
# ---------------------------------------------------------------------------
@njit(cache=True)
def _up(x):
    return np.nextafter(x, np.inf)


@njit(cache=True)
def _dn(x):
    return np.nextafter(x, -np.inf)


@njit(cache=True)
def k_below(t, x):
    """Largest k with t[k] <= x (t increasing); -1 if none."""
    lo, hi = 0, t.size - 1
    if x < t[0]:
        return -1
    if x >= t[hi]:
        return hi
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if t[mid] <= x:
            lo = mid
        else:
            hi = mid
    return lo


@njit(cache=True)
def k_above(t, x):
    """Smallest k with t[k] >= x; t.size if none."""
    lo, hi = 0, t.size - 1
    if x <= t[0]:
        return 0
    if x > t[hi]:
        return t.size
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if t[mid] >= x:
            hi = mid
        else:
            lo = mid
    return hi


@njit(cache=True)
def p_lo_of(b, bt, plo):
    if b <= 0.0:
        return 0.0
    k = k_below(bt, b)
    return plo[k]


@njit(cache=True)
def p_hi_of(b, bt, phi):
    if b <= 0.0:
        return 0.0
    k = k_above(bt, b)
    if k >= bt.size:
        return 1.0
    return phi[k]


@njit(cache=True)
def phi_cell_bounds(c, wt, Flo, Fhi):
    """Per table cell [w_k, w_k+1]: certified (phi_lo, phi_hi) or invalid."""
    n = wt.size - 1
    plo = np.zeros(n); phi = np.zeros(n); ok = np.zeros(n, np.bool_)
    cc_lo, cc_hi = _dn(c * c), _up(c * c)
    for k in range(n):
        f_lo, f_hi = Flo[k], Fhi[k + 1]          # F increasing in w
        a, b = wt[k], wt[k + 1]
        # X = F w over the cell, interval product (F > 0)
        x1, x2, x3, x4 = _dn(f_lo * a), _dn(f_lo * b), _dn(f_hi * a), _dn(f_hi * b)
        X_lo = min(min(x1, x2), min(x3, x4))
        y1, y2, y3, y4 = _up(f_lo * a), _up(f_lo * b), _up(f_hi * a), _up(f_hi * b)
        X_hi = max(max(y1, y2), max(y3, y4))
        if c > 0.0:
            disc_lo = _dn(cc_lo + X_lo)
            if disc_lo < 0.0:
                continue
            den_lo = _dn(c + _dn(math.sqrt(disc_lo)))
            den_hi = _up(c + _up(math.sqrt(_up(cc_hi + X_hi))))
        else:
            # c + sqrt(c^2 + X) = X / (sqrt(c^2 + X) - c), no cancellation for c < 0
            if X_lo <= 0.0:
                continue
            den_lo = _dn(X_lo / _up(_up(math.sqrt(_up(cc_hi + X_lo))) - c))
            den_hi = _up(X_hi / _dn(_dn(math.sqrt(_dn(cc_lo + X_hi))) - c))
            if den_lo <= 0.0:
                continue
        plo[k] = _dn(f_lo / _up(2.0 * den_hi))
        phi[k] = _up(f_hi / _dn(2.0 * den_lo))
        ok[k] = True
    return plo, phi, ok


@njit(cache=True)
def phi_prefix(c, wt, Flo, Fhi):
    """Directed prefix sums of the upper and lower cell integrals of Phi_c',
    from the first node k0 of the valid run that reaches the top of the table.
    Returns k0, PU_lo, PU_hi, PL_lo, PL_hi (NaN below k0)."""
    plo, phi, ok = phi_cell_bounds(c, wt, Flo, Fhi)
    n = wt.size
    k0 = n - 1
    while k0 > 0 and ok[k0 - 1]:
        k0 -= 1
    PU_lo = np.full(n, np.nan); PU_hi = np.full(n, np.nan)
    PL_lo = np.full(n, np.nan); PL_hi = np.full(n, np.nan)
    PU_lo[k0] = PU_hi[k0] = PL_lo[k0] = PL_hi[k0] = 0.0
    for k in range(k0, n - 1):
        h_lo, h_hi = _dn(wt[k + 1] - wt[k]), _up(wt[k + 1] - wt[k])
        tu_lo, tu_hi = _dn(phi[k] * h_hi), _up(phi[k] * h_hi)
        tl_lo, tl_hi = _dn(plo[k] * h_lo), _up(plo[k] * h_lo)
        # the upper cell term is phi_hi*h_hi; rounding both ways bounds its prefix
        PU_lo[k + 1] = _dn(PU_lo[k] + tu_lo)
        PU_hi[k + 1] = _up(PU_hi[k] + tu_hi)
        PL_lo[k + 1] = _dn(PL_lo[k] + tl_lo)
        PL_hi[k + 1] = _up(PL_hi[k] + tl_hi)
    return k0, PU_lo, PU_hi, PL_lo, PL_hi


@njit(parallel=True, cache=True)
def calibration_point_tables(cs, wt, Flo, Fhi, wlo_pt, whi_pt, nulo_pt, nuhi_pt):
    """Separable per-point pieces of the calibration bound, for every c:
       case wb_hi >= wa_lo : UB_c <= AU_hi[b,c] - AU_lo[a,c]
       case wb_hi <  wa_lo : UB_c <= AL_hi[b,c] - AL_lo[a,c]
    plus thr[c] = w of the first valid node."""
    nc, npt = cs.size, wlo_pt.size
    AU_lo = np.full((npt, nc), np.nan); AU_hi = np.full((npt, nc), np.nan)
    AL_lo = np.full((npt, nc), np.nan); AL_hi = np.full((npt, nc), np.nan)
    thr = np.empty(nc)
    for j in prange(nc):
        c = cs[j]
        k0, PU_lo, PU_hi, PL_lo, PL_hi = phi_prefix(c, wt, Flo, Fhi)
        thr[j] = wt[k0]
        for i in range(npt):
            kb = k_below(wt, wlo_pt[i])       # point used as the past end a
            ka = k_above(wt, whi_pt[i])       # point used as the future end b
            if kb < k0 or ka >= wt.size:
                continue
            if c > 0.0:
                cnu_lo, cnu_hi = _dn(c * nulo_pt[i]), _up(c * nuhi_pt[i])
            else:
                cnu_lo, cnu_hi = _dn(c * nuhi_pt[i]), _up(c * nulo_pt[i])
            AU_lo[i, j] = _dn(cnu_lo + PU_lo[kb]); AU_hi[i, j] = _up(cnu_hi + PU_hi[ka])
            AL_lo[i, j] = _dn(cnu_lo + PL_lo[kb]); AL_hi[i, j] = _up(cnu_hi + PL_hi[ka])
    return AU_lo, AU_hi, AL_lo, AL_hi, thr


@njit(parallel=True, cache=True)
def ub_table(M, Ug, Vg, wlo_pt, whi_pt, AU_lo, AU_hi, AL_lo, AL_hi, thr,
             Pcs_lo, Pcs_hi, bt, phi_p):
    """p_hi(UB(a,b)) for every lattice pair a <= b (strict in both); 0 otherwise."""
    n1 = M + 1
    npt = n1 * n1
    out = np.zeros((npt, npt))
    nc = thr.size
    for a in prange(npt):
        ia, ja = a // n1, a % n1
        for ib in range(ia + 1, n1):
            du_hi = _up(Ug[ib] - Ug[ia])
            for jb in range(ja + 1, n1):
                b = ib * n1 + jb
                # Cauchy-Schwarz with U_b fixed, prefix sums along V
                I_hi = _up(Pcs_hi[ib, jb] - Pcs_lo[ib, ja])
                best = _up(math.sqrt(_up(du_hi * I_hi)))
                # rectangle w-range from its four lattice corners
                c2, c3 = ia * n1 + jb, ib * n1 + ja
                rwlo = min(min(wlo_pt[a], wlo_pt[b]), min(wlo_pt[c2], wlo_pt[c3]))
                case_up = whi_pt[b] >= wlo_pt[a]
                cmin = np.inf
                for j in range(nc):
                    if thr[j] > rwlo:
                        continue
                    # plain differences; one outward step on the minimum suffices,
                    # since up() is monotone: min_j up(d_j) = up(min_j d_j)
                    if case_up:
                        v = AU_hi[b, j] - AU_lo[a, j]
                    else:
                        v = AL_hi[b, j] - AL_lo[a, j]
                    if v < cmin:
                        cmin = v
                if cmin < np.inf:
                    cmin = _up(cmin)
                    if cmin < best:
                        best = cmin
                out[a, b] = p_hi_of(best, bt, phi_p)
    return out


@njit(parallel=True, cache=True)
def lb_rows(src, forward, Ug, Vg, M, wt, qlo, bt, plo_p, ntau):
    """p_lo(LB) for pairs (s, x): s in src (lattice ids), x over all lattice
    points; forward: s is the past end; else s is the future end."""
    n1 = M + 1
    npt = n1 * n1
    out = np.zeros((src.size, npt))
    inv = 1.0 / ntau                       # exact: ntau is a power of two
    for r in prange(src.size):
        s = src[r]
        for x in range(npt):
            if forward:
                a, b = s, x
            else:
                a, b = x, s
            ia, ja, ib, jb = a // n1, a % n1, b // n1, b % n1
            if not (Ug[ib] > Ug[ia] and Vg[jb] > Vg[ja]):
                continue
            Ua, Va = Ug[ia], Vg[ja]
            du_lo, du_hi = _dn(Ug[ib] - Ua), _up(Ug[ib] - Ua)
            dv_lo, dv_hi = _dn(Vg[jb] - Va), _up(Vg[jb] - Va)
            acc = 0.0
            for k in range(ntau):
                t0, t1 = k * inv, (k + 1) * inv
                U_lo = _dn(Ua + _dn(du_lo * t0))
                U_hi = _up(Ua + _up(du_hi * t1))
                V_lo = _dn(Va + _dn(dv_lo * t0))
                V_hi = _up(Va + _up(dv_hi * t1))
                # w = U V with V > 0: the minimum is at V_lo if U_lo >= 0, else V_hi
                w_lo = _dn(U_lo * V_lo) if U_lo >= 0.0 else _dn(U_lo * V_hi)
                kq = k_below(wt, w_lo)
                if kq >= 0:                    # below the table: q > 0 is the bound
                    acc = _dn(acc + qlo[kq])
            line = _dn(_dn(math.sqrt(_dn(du_lo * dv_lo))) * _dn(acc * inv))
            out[r, x] = p_lo_of(line, bt, plo_p)
    return out


@njit(parallel=True, cache=True)
def b_hi_sum(M, W_hi, pub):
    """2 sum_{P,Q} W_P W_Q p_hi(UB(P_bot, Q_top)), directed upward."""
    n1 = M + 1
    nc = M * M
    part = np.zeros(nc)
    for P in prange(nc):
        iP, jP = P // M, P % M
        bot = iP * n1 + jP
        acc = 0.0
        for Q in range(nc):
            iQ, jQ = Q // M, Q % M
            top = (iQ + 1) * n1 + (jQ + 1)
            v = pub[bot, top]
            if v > 0.0:
                acc = _up(acc + _up(W_hi[Q] * v))
        part[P] = _up(W_hi[P] * acc)
    tot = 0.0
    for P in range(nc):
        tot = _up(tot + part[P])
    return _up(2.0 * tot)


@njit(cache=True)
def face_h(M, s0, s1, W, vals_fwd, vals_bwd, use_top_bot_lower):
    """H on each face segment from per-(segment endpoint, lattice point) tables.

    use_top_bot_lower (lower bound): fwd uses (s1 -> Q_bot), bwd (Q_top -> s0).
    otherwise (upper bound):         fwd uses (s0 -> Q_top), bwd (Q_bot -> s1).
    vals_fwd[r, x] / vals_bwd[r, x] are indexed by the segment endpoint row r.
    Sums are rounded down for the lower bound and up for the upper bound."""
    n1 = M + 1
    nseg = s0.size
    H = np.zeros(nseg)
    for i in range(nseg):
        acc = 0.0
        for Q in range(M * M):
            iQ, jQ = Q // M, Q % M
            bot = iQ * n1 + jQ
            top = (iQ + 1) * n1 + (jQ + 1)
            if use_top_bot_lower:
                v = vals_fwd[i + 1, bot] + vals_bwd[i, top]     # both >= 0
                acc = _dn(acc + _dn(W[Q] * _dn(v)))
            else:
                v = vals_fwd[i, top] + vals_bwd[i + 1, bot]
                acc = _up(acc + _up(W[Q] * _up(v)))
        H[i] = acc
    return H


# ---------------------------------------------------------------------------
# 3. Weights by sub-cell envelopes of G (unimodal, peak 1/e at w = 0).
# ---------------------------------------------------------------------------
@njit(cache=True)
def tiling(a, b, r):
    """r+1 increasing nodes with the endpoints EXACTLY a and b, so sub-cells
    tile the cell with no gap or overlap (numba's linspace does not promise it)."""
    xs = np.linspace(a, b, r + 1)
    xs[0] = a
    xs[r] = b
    for k in range(r):
        if not xs[k] < xs[k + 1]:
            raise ValueError("non-increasing tiling")
    return xs


@njit(cache=True)
def g_range(wl, wh, wt, glo, ghi, e_inv_hi):
    """Certified (lo, hi) of G over [wl, wh]; 0 is a node of wt."""
    if wh <= 0.0:
        lo = glo[k_below(wt, wl)]
        hi = ghi[k_above(wt, wh)]
    elif wl >= 0.0:
        lo = glo[k_above(wt, wh)]
        hi = ghi[k_below(wt, wl)]
    else:
        lo = min(glo[k_below(wt, wl)], glo[k_above(wt, wh)])
        hi = e_inv_hi
    return lo, hi


@njit(cache=True)
def rect_w(u0, u1, v0, v1):
    a, b, c, d = u0 * v0, u0 * v1, u1 * v0, u1 * v1
    lo = min(min(_dn(a), _dn(b)), min(_dn(c), _dn(d)))
    hi = max(max(_up(a), _up(b)), max(_up(c), _up(d)))
    return lo, hi


@njit(cache=True)
def cell_weights(Ug, Vg, r, wt, glo, ghi, e_inv_hi):
    M = Ug.size - 1
    W_lo = np.zeros(M * M); W_hi = np.zeros(M * M)
    for i in range(M):
        us = tiling(Ug[i], Ug[i + 1], r)
        for j in range(M):
            vs = tiling(Vg[j], Vg[j + 1], r)
            alo = 0.0; ahi = 0.0
            for a in range(r):
                for b in range(r):
                    wl, wh = rect_w(us[a], us[a + 1], vs[b], vs[b + 1])
                    gl, gh = g_range(wl, wh, wt, glo, ghi, e_inv_hi)
                    ar_lo = _dn(_dn(us[a + 1] - us[a]) * _dn(vs[b + 1] - vs[b]))
                    ar_hi = _up(_up(us[a + 1] - us[a]) * _up(vs[b + 1] - vs[b]))
                    alo = _dn(alo + _dn(ar_lo * gl))
                    ahi = _up(ahi + _up(ar_hi * gh))
            W_lo[i * M + j] = alo; W_hi[i * M + j] = ahi
    return W_lo, W_hi


@njit(cache=True)
def segment_weights(fixed, grid, r, wt, glo, ghi, e_inv_hi):
    n = grid.size - 1
    lo = np.zeros(n); hi = np.zeros(n)
    for i in range(n):
        xs = tiling(grid[i], grid[i + 1], r)
        alo = 0.0; ahi = 0.0
        for a in range(r):
            w1, w2 = fixed * xs[a], fixed * xs[a + 1]
            wl = min(_dn(w1), _dn(w2)); wh = max(_up(w1), _up(w2))
            gl, gh = g_range(wl, wh, wt, glo, ghi, e_inv_hi)
            alo = _dn(alo + _dn(_dn(xs[a + 1] - xs[a]) * gl))
            ahi = _up(ahi + _up(_up(xs[a + 1] - xs[a]) * gh))
        lo[i] = alo; hi[i] = ahi
    return lo, hi


@njit(cache=True)
def cs_prefix(Ug, Vg, r, wt, Fhi):
    """Directed prefix sums along V of upper bounds of int F(U_i V) dV per cell."""
    n1 = Ug.size
    P_lo = np.zeros((n1, n1)); P_hi = np.zeros((n1, n1))
    for i in range(n1):
        u = Ug[i]
        for j in range(n1 - 1):
            vs = tiling(Vg[j], Vg[j + 1], r)
            cell = 0.0
            for a in range(r):
                # w = u V monotone in V: the max is at the upper end iff u >= 0
                wmax = _up(u * vs[a + 1]) if u >= 0.0 else _up(u * vs[a])
                cell = _up(cell + _up(_up(vs[a + 1] - vs[a]) * Fhi[k_above(wt, wmax)]))
            P_lo[i, j + 1] = _dn(P_lo[i, j] + cell)
            P_hi[i, j + 1] = _up(P_hi[i, j] + cell)
    return P_lo, P_hi


# ---------------------------------------------------------------------------
# 4. Guard: no fast-math or contraction in any compiled kernel.
# ---------------------------------------------------------------------------
_FAST = re.compile(r"\b(fast|contract|reassoc|afn|arcp|nnan|ninf|nsz)\b|llvm\.fma|fmuladd")
KERNELS = (tiling, phi_cell_bounds, phi_prefix, calibration_point_tables, ub_table, lb_rows,
           b_hi_sum, face_h, g_range, rect_w, cell_weights, segment_weights, cs_prefix,
           k_below, k_above, p_lo_of, p_hi_of, _up, _dn)


def fastmath_flags(fn):
    found = set()
    for sig in fn.signatures:
        found |= {m.group(0) for m in _FAST.finditer(fn.inspect_llvm(sig))}
    return sorted(found)


def _compile_helpers():
    """Helpers called only from other kernels register no signature of their
    own; compile each once from Python with the argument types the kernels use,
    so the guard inspects real IR rather than passing vacuously."""
    t = np.linspace(-1.0, 1.0, 9)
    tiling(0.0, 1.0, 4); phi_cell_bounds(1.0, t, t + 2.0, t + 3.0)
    phi_prefix(1.0, t, t + 2.0, t + 3.0); g_range(-0.5, 0.5, t, t, t, 1.0)
    rect_w(0.0, 1.0, 0.5, 1.0); k_below(t, 0.1); k_above(t, 0.1)
    p_lo_of(0.1, t, t); p_hi_of(0.1, t, t); _up(1.0); _dn(1.0)


def fastmath_guard():
    _compile_helpers()
    flags = {fn.py_func.__name__: fastmath_flags(fn) for fn in KERNELS}
    uncompiled = [fn.py_func.__name__ for fn in KERNELS if not fn.signatures]

    @njit(fastmath=True)
    def _mutant(a, b, c):
        return a * b + c
    _mutant(1.0, 2.0, 3.0)
    mutant_caught = bool(fastmath_flags(_mutant))
    clean = all(not v for v in flags.values())
    return {"kernels_checked": len(flags), "kernels_without_compiled_signature": uncompiled,
            "flags_found": {k: v for k, v in flags.items() if v},
            "all_clean": clean, "mutation_fastmath_detected": mutant_caught,
            "ok": bool(clean and mutant_caught and not uncompiled)}


# ---------------------------------------------------------------------------
# 5. Assembly.
# ---------------------------------------------------------------------------
def run(M):
    t_start = time.time()
    Ug = np.linspace(-UOUT, UIN, M + 1)
    Vg = np.linspace(V0, V1, M + 1)
    assert Ug[0] == -UOUT and Ug[-1] == UIN and Vg[0] == V0 and Vg[-1] == V1
    assert np.all(np.diff(Ug) > 0) and np.all(np.diff(Vg) > 0) and Vg[0] > 0
    n1 = M + 1

    wt = w_table()
    qlo, qhi, glo, ghi, Flo, Fhi = certified_tables(wt)
    bt, plo_p, phi_p = p_table()
    e_inv_hi = b15.E_INV_HI
    nulo, nuhi = nu_enclosures(Vg)
    t_tables = time.time()

    # lattice points: id = i*(M+1) + j, (U_i, V_j)
    iu, jv = np.divmod(np.arange(n1 * n1), n1)
    PU, PV = Ug[iu], Vg[jv]
    wlo_pt, whi_pt = dn(PU * PV), up(PU * PV)
    nulo_pt, nuhi_pt = nulo[jv], nuhi[jv]

    cs = np.concatenate([C_POS, C_NEG])
    AU_lo, AU_hi, AL_lo, AL_hi, thr = calibration_point_tables(
        cs, wt, Flo, Fhi, wlo_pt, whi_pt, nulo_pt, nuhi_pt)
    Pcs_lo, Pcs_hi = cs_prefix(Ug, Vg, R_SUB, wt, Fhi)
    pub = ub_table(M, Ug, Vg, wlo_pt, whi_pt, AU_lo, AU_hi, AL_lo, AL_hi, thr,
                   Pcs_lo, Pcs_hi, bt, phi_p)
    del AU_lo, AU_hi, AL_lo, AL_hi
    t_ub = time.time()

    W_lo, W_hi = cell_weights(Ug, Vg, R_SUB, wt, glo, ghi, e_inv_hi)
    Z_lo, Z_hi = b15.sum_dn(W_lo), b15.sum_up(W_hi)
    B_hi = b_hi_sum(M, W_hi, pub)

    faces = {"U=-u_out": ("U", 0, -UOUT), "U=u_in": ("U", M, UIN),
             "V=v0": ("V", 0, V0), "V=v1": ("V", M, V1)}
    Bp_terms, Zp_lo_terms, Zp_hi_terms, face_out = [], [], [], {}
    for name, (axis, idx, fixed) in faces.items():
        if axis == "U":
            pts = idx * n1 + np.arange(n1)                  # (U fixed, V_j)
            fw_lo, fw_hi = segment_weights(fixed, Vg, R_SUB, wt, glo, ghi, e_inv_hi)
        else:
            pts = np.arange(n1) * n1 + idx                  # (U_i, V fixed)
            fw_lo, fw_hi = segment_weights(fixed, Ug, R_SUB, wt, glo, ghi, e_inv_hi)
        vn_lo, vn_hi = frac_iv(VN_FR[name])
        s0, s1 = pts[:-1], pts[1:]
        if vn_lo > 0:
            fwd = lb_rows(pts, True, Ug, Vg, M, wt, qlo, bt, plo_p, N_TAU)
            bwd = lb_rows(pts, False, Ug, Vg, M, wt, qlo, bt, plo_p, N_TAU)
            H = face_h(M, s0, s1, W_lo, fwd, bwd, True)
            inner = b15.sum_dn(dn(fw_lo * H))
            term = float(dn(2.0 * dn(vn_lo * inner)))
            Zp_lo_terms.append(float(dn(vn_lo * b15.sum_dn(fw_lo))))
            Zp_hi_terms.append(float(up(vn_hi * b15.sum_up(fw_hi))))
        else:
            fwd = pub[pts, :]                               # (s -> Q_top), s past end
            bwd = pub[:, pts].T                             # (Q_bot -> s), s future end
            H = face_h(M, s0, s1, W_hi, fwd, bwd, False)
            inner = b15.sum_up(up(fw_hi * H))
            term = float(dn(2.0 * dn(vn_lo * inner)))     # vn < 0: lower = vn_lo * hi
            Zp_lo_terms.append(float(dn(vn_lo * b15.sum_up(fw_hi))))
            Zp_hi_terms.append(float(up(vn_hi * b15.sum_dn(fw_lo))))
        Bp_terms.append(term)
        face_out[name] = {"v_n": [vn_lo, vn_hi], "Bprime_contribution_lower": term}
    Bp_lo = b15.sum_dn(Bp_terms)
    Zp_lo, Zp_hi = b15.sum_dn(Zp_lo_terms), b15.sum_up(Zp_hi_terms)
    assert Zp_lo > 0
    k_hi = float(up(2.0 * up(Zp_hi / Z_lo)))
    S_lo = float(dn(Bp_lo - up(k_hi * B_hi)))
    drho_lo = float(dn(S_lo / up(Z_hi * Z_hi))) if S_lo > 0 else float(dn(S_lo / dn(Z_lo * Z_lo)))
    return {
        "M": M, "R_sub": R_SUB, "N_tau": N_TAU, "w_table_nodes": int(wt.size),
        "p_table_nodes": int(bt.size), "c_values": int(cs.size),
        "Z": [Z_lo, Z_hi], "Zprime": [Zp_lo, Zp_hi], "two_Zp_over_Z_hi": k_hi,
        "B_hi": B_hi, "Bprime_lo": Bp_lo, "faces": face_out,
        "S_lo": S_lo, "drho_dt_lower_bound": drho_lo,
        "seconds": {"tables": round(t_tables - t_start, 1), "ub_table": round(t_ub - t_tables, 1),
                    "total": round(time.time() - t_start, 1)},
    }


def main():
    M = int(sys.argv[1]) if len(sys.argv) > 1 else M_DEFAULT
    res = run(M)
    guard = fastmath_guard()
    positive = bool(res["S_lo"] > 0 and guard["ok"])
    out = {
        "unit": "PUENTE-3P1/B2_PATH2_GATE_CERTIFICATE",
        "rule": "B2_CORRECTED_POSITIVE iff 0 not in formal_enclosure(drho_dt) "
                "(amendment signed 2026-10-11)",
        "frozen_point": {"lambda_star_binary64": [float(x) for x in LAM],
                         "direction_exact": [str(f) for f in DFR], "t0": T0},
        "representation": "time separation of q(UV)^2 dU dV; corners by reverse triangle "
                          "inequality; lower = straight line; upper = min(Cauchy-Schwarz, "
                          "HJ calibration)",
        "arithmetic": {
            "mode": "outward_directed_rounding_end_to_end",
            "operations": "np.nextafter one ulp outward after each binary64 op, also in numba",
            "transcendentals": "certified monotone tables from B1.5 scalar layer "
                               "(s_encl/q_encl/G_encl, mpmath.iv dps 25); p and ln V by mpmath.iv",
            "lambert_w_used": False,
            "fastmath_guard": guard,
        },
        **res,
        "enclosure_of_drho_dt": [res["drho_dt_lower_bound"], "+inf"],
        "no_new_path": True, "no_new_t0": True, "no_new_points": True,
        "no_search": True, "no_adjustment": True, "no_seeds": True, "no_monte_carlo": True,
        "terminal": "B2_CORRECTED_POSITIVE" if positive else "B2_GATE_NOT_CERTIFIED_AT_THIS_RESOLUTION",
    }
    print(json.dumps(out, indent=2))
    if len(sys.argv) <= 1:
        with open(HERE / "verification_b2_path2_gate_certificate.json", "w") as fh:
            json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
