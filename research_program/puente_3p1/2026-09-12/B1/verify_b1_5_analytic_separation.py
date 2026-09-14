"""PUENTE-3P1 / B1.5 — analytic separation certificate for the frozen pair.

Goal.  Produce two numbers U0, L1 with

    rho(lambda0) <= U0 < L1 <= rho(lambda1),

so that TV(P_{lambda0,2}, P_{lambda1,2}) = |rho(lambda0) - rho(lambda1)| > 0 is
established by a chain of inequalities rather than by quadrature stability.
Neither rho is computed: only a crude upper bound for lambda0 and a crude lower
bound for lambda1.

What this file does NOT use, by design (B1.5 stop rule):
  * no multidimensional quadrature -- every integral below is one-dimensional,
    the pair integrals having been collapsed exactly by Fubini;
  * no multidimensional interval arithmetic -- intervals appear only in the
    scalar layer, to enclose s, G and q at single points;
  * no Lambert W:  s(w) is enclosed by the monotone scalar inequality
    f(s) = (1-s)e^s = w, verified in both directions at each point;
  * no large partition -- the block counts K, L and the cell counts are printed
    with the result, and every choice of them yields a *valid* bound.  Refining
    them tightens the bound; it never validates an invalid one.

Determinism: no seeds, no Monte Carlo, no search over lambda, no fitting.  The
frozen pair is the one of B1.3 and is asserted against it below.
"""
import json
import math
import os

import numpy as np
from mpmath import iv

iv.dps = 25

# --- frozen pair (B1.3 section 2); must not be edited ----------------------
LAMBDA0 = (0.5, 1.0, 1.0, 0.5, 0.1)
LAMBDA1 = (0.2, 0.8, 2.0, 0.9, 0.1)

# --- proof parameters (any values give a valid bound; larger = tighter) ----
K_ANCHORS = 16      # U_y anchor bins for the lower bound
L_CELLS = 16        # V cells for the lower bound
N_CELLS_U = 480     # U cells for every one-dimensional quadrature bound
N_CELLS_V = 160     # V cells for the C1 bound of the upper chain
SLACK = 1e-9        # relative slack absorbing float accumulation (doc section 7, H4)

E_INV = math.exp(-1.0)

# ---------------------------------------------------------------------------
# 1. Scalar layer.  s(w) is defined by (1-s)e^s = w on s>0, where f(s)=(1-s)e^s
#    is strictly decreasing (f'(s) = -s e^s < 0).  Hence
#        s >= a   <=>   f(a) >= w ,      s <= b   <=>   f(b) <= w ,
#    and an enclosure is certified by two scalar inequalities, each evaluated in
#    rigorous interval arithmetic.  No Lambert W routine is called anywhere.
# ---------------------------------------------------------------------------
_CACHE_S, _CACHE_G, _CACHE_Q = {}, {}, {}


def _f_iv(s):
    """Rigorous interval enclosure of f(s) = (1-s) e^s."""
    S = iv.mpf(s)
    return (iv.mpf(1) - S) * iv.exp(S)


def _s_approx(w):
    """Float bisection on the monotone equation; only a starting guess."""
    lo, hi = 1e-300, 1.0
    while (1.0 - hi) * math.exp(hi) > w:
        hi *= 2.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if (1.0 - mid) * math.exp(mid) > w:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def s_encl(w):
    """Certified (s_lo, s_hi) with s(w) in [s_lo, s_hi]."""
    key = float(w)
    if key in _CACHE_S:
        return _CACHE_S[key]
    s0 = _s_approx(key)
    pad = 1e-13
    for _ in range(80):
        lo = max(1e-300, s0 - pad * max(1.0, abs(s0)))
        hi = s0 + pad * max(1.0, abs(s0))
        if float(_f_iv(lo).a) >= key and float(_f_iv(hi).b) <= key:
            _CACHE_S[key] = (lo, hi)
            return lo, hi
        pad *= 4.0
    raise RuntimeError("no certified enclosure of s at w=%r" % key)


def G_encl(w):
    """Certified bracket of G(w) = s e^{-s}; G is unimodal in s with peak 1/e."""
    key = float(w)
    if key in _CACHE_G:
        return _CACHE_G[key]
    a, b = s_encl(key)
    va, vb = iv.mpf(a) * iv.exp(-iv.mpf(a)), iv.mpf(b) * iv.exp(-iv.mpf(b))
    lo = min(float(va.a), float(vb.a))
    hi = E_INV if a <= 1.0 <= b else max(float(va.b), float(vb.b))
    _CACHE_G[key] = (lo, hi)
    return lo, hi


def q_encl(w):
    """Certified bracket of q(w) = 2 e^{-s/2} s^{-3/2}; q is decreasing in s."""
    key = float(w)
    if key in _CACHE_Q:
        return _CACHE_Q[key]
    a, b = s_encl(key)
    hi_v = iv.mpf(2) * iv.exp(-iv.mpf(a) / 2) / (iv.mpf(a) ** iv.mpf(1.5))
    lo_v = iv.mpf(2) * iv.exp(-iv.mpf(b) / 2) / (iv.mpf(b) ** iv.mpf(1.5))
    out = (float(lo_v.a), float(hi_v.b))
    _CACHE_Q[key] = out
    return out


def arr(fn, ws, idx):
    return np.array([fn(w)[idx] for w in ws], dtype=float)


def grid(lo, hi, n, extra=()):
    g = np.linspace(lo, hi, n + 1)
    g = np.unique(np.concatenate([g, np.array([x for x in extra if lo <= x <= hi])]))
    return g


# ---------------------------------------------------------------------------
# 2. Z brackets.  For every U and every V in [v0,v1],
#        G(U v1) <= G(U V) <= G(U v0),
#    because w = U V lies between U v1 and U v0 on one side of 0, G is increasing
#    in w for w<0 and decreasing for w>0.  Both envelopes are unimodal in U with
#    their peak at U = 0, which is forced to be a grid point, so each cell is
#    monotone and endpoint values bracket the cell.
# ---------------------------------------------------------------------------
def z_bracket(lam):
    v0, v1, uout, uin, _ = lam
    U = grid(-uout, uin, N_CELLS_U, extra=(0.0,))
    t = np.linspace(v0, v1, L_CELLS + 1)
    dU = np.diff(U)
    z_lo = z_hi = 0.0
    for l in range(L_CELLS):          # one 1-D integral per V cell: envelope gap ~ 1/L
        lo_env = arr(G_encl, U * t[l + 1], 0)
        hi_env = arr(G_encl, U * t[l], 1)
        z_lo += float(np.sum(dU * np.minimum(lo_env[:-1], lo_env[1:]))) * (t[l + 1] - t[l])
        z_hi += float(np.sum(dU * np.maximum(hi_env[:-1], hi_env[1:]))) * (t[l + 1] - t[l])
    return z_lo, z_hi


# ---------------------------------------------------------------------------
# 3. Upper bound.   For an ordered pair x < y, every admissible path U(.) obeys
#    U(V) <= U_y, hence q(U(V)V) <= q(U_y V) (q increasing in w, V>0), and
#    Cauchy-Schwarz gives
#        Delta_max <= a := sqrt( dU * int_{Vx}^{Vy} q(U_y V)^2 dV ).
#    With p(a) = (1-cos min(a,pi))/2 <= a^2/4 and G <= Gcheck(U) = G(U v0),
#    the pair integral collapses exactly:
#        int int_{Vx<=Vy} int_{Vx}^{Vy} h(V) dV dVx dVy = int h(V)(V-v0)(v1-V) dV,
#        int_{-uout}^{U_y} G(Ux v0)(U_y-Ux) dUx <= e^{-1}(U_y+uout)^2/2 ,
#    leaving one outer one-dimensional integral.
# ---------------------------------------------------------------------------
def rho_upper(lam):
    v0, v1, uout, uin, _ = lam
    z_lo, _ = z_bracket(lam)
    U = grid(-uout, uin, N_CELLS_U, extra=(0.0,))
    V = grid(v0, v1, N_CELLS_V)

    def wgt(a, b):  # int_a^b (V-v0)(v1-V) dV
        F = lambda z: -z ** 3 / 3.0 + (v0 + v1) * z ** 2 / 2.0 - v0 * v1 * z
        return F(b) - F(a)

    weights = np.array([wgt(V[i], V[i + 1]) for i in range(len(V) - 1)])
    # C1(U) = int q(UV)^2 (V-v0)(v1-V) dV, upper bound; q^2 monotone in V
    c1_hi = np.empty(len(U))
    for i, u in enumerate(U):
        edge = V[1:] if u > 0 else V[:-1]        # the V endpoint maximising |w|-side
        qh = arr(q_encl, u * edge, 1)
        c1_hi[i] = float(np.sum(weights * qh ** 2))
    g_hi = arr(G_encl, U * v0, 1)
    a1 = E_INV * (U + uout) ** 2 / 2.0           # A1(U), increasing
    # C1 and A1 increase in U; Gcheck is unimodal with peak at the grid point 0
    cell = np.diff(U) * np.maximum(g_hi[:-1], g_hi[1:]) * a1[1:] * c1_hi[1:]
    main_hi = float(np.sum(cell))
    return main_hi / (2.0 * z_lo ** 2) * (1.0 + SLACK)


# ---------------------------------------------------------------------------
# 4. Lower bound.   Fix U-anchors c_0<...<c_K and V-nodes t_0<...<t_L.  For a
#    pair with U_y in [c_j,c_{j+1}], U_x <= c_j, V_x in [t_l,t_{l+1}] and V_y in
#    [t_m,t_{m+1}] (m>=l), the straight segment from x to y is admissible, and
#    its profile dominates the segment from x to (c_j,V_y):
#        U_lin(V) >= U_x + (c_j-U_x)(V-V_x)/(V_y-V_x).
#    Substituting tau = (V-V_x)/(V_y-V_x) makes that profile independent of
#    V_x,V_y, and q(.) is bounded below by qtilde_{l,m}, the worst V in
#    [t_l,t_{m+1}].  Hence
#        Delta_max >= sqrt(dU dV) * T,   T = mean of qtilde on [U_x, c_j],
#    and with p(b) >= b^2/4 - b^4/48 the pair integral again factorises into
#    one-dimensional pieces times the closed-form V moments
#        int int (Vy-Vx) = F2, int int (Vy-Vx)^2 = F4.
# ---------------------------------------------------------------------------
def rho_lower(lam, diagnostics=None):
    v0, v1, uout, uin, _ = lam
    _, z_hi = z_bracket(lam)
    c = np.linspace(-uout, uin, K_ANCHORS + 1)
    t = np.linspace(v0, v1, L_CELLS + 1)
    U = grid(-uout, uin, N_CELLS_U, extra=tuple(c) + (0.0,))
    dU = np.diff(U)
    idx = {float(x): int(np.argmin(np.abs(U - x))) for x in c}

    g_lo = {l: arr(G_encl, U * t[l], 0) for l in range(L_CELLS + 1)}
    g_hi = {l: arr(G_encl, U * t[l], 1) for l in range(L_CELLS + 1)}
    q_lo = {l: arr(q_encl, U * t[l], 0) for l in range(L_CELLS + 1)}
    q_hi = {l: arr(q_encl, U * t[l], 1) for l in range(L_CELLS + 1)}
    neg = U < 0

    F2 = lambda z: z ** 3 / 6.0
    F4 = lambda z: z ** 4 / 12.0
    total = 0.0
    main_acc = 0.0
    quart_acc = 0.0
    for l in range(L_CELLS):
        for m in range(l, L_CELLS):
            # qtilde_{l,m}(u): worst V in [t_l, t_{m+1}] -> t_{m+1} for u<0, t_l for u>=0
            qt_lo = np.where(neg, q_lo[m + 1], q_lo[l])
            qt_hi = np.where(neg, q_hi[m + 1], q_hi[l])
            # qtilde is increasing in u: lower/upper Riemann sums of its primitive
            cum_lo = np.concatenate([[0.0], np.cumsum(dU * qt_lo[:-1])])
            cum_hi = np.concatenate([[0.0], np.cumsum(dU * qt_hi[1:])])
            A, B, C, D = t[l], t[l + 1], t[m], t[m + 1]
            if m == l:
                v2, v4 = (B - A) ** 3 / 6.0, (B - A) ** 4 / 12.0
            else:
                v2 = F2(D - A) - F2(D - B) - F2(C - A) + F2(C - B)
                v4 = F4(D - A) - F4(D - B) - F4(C - A) + F4(C - B)
            for j in range(K_ANCHORS):
                cj, cj1 = c[j], c[j + 1]
                jj = idx[float(cj)]
                if jj < 1:
                    continue
                sl = slice(0, jj)                      # cells inside [-uout, c_j]
                ua, ub, wdt = U[:jj], U[1:jj + 1], dU[sl]
                den = cj - ua
                t_lo = np.maximum(0.0, (cum_lo[jj] - cum_lo[:jj]) / den)   # T at left ends
                # T increases in U_x, so its cell maximum sits at the right end;
                # the last cell ends at c_j, where the average degenerates to
                # qtilde(c_j), the supremum of an increasing integrand.
                den_r = cj - ub
                t_hi = np.empty_like(ub)
                ok = den_r > 0
                t_hi[ok] = (cum_hi[jj] - cum_hi[1:jj + 1][ok]) / den_r[ok]
                t_hi[~ok] = qt_hi[jj]
                t_hi = np.minimum(t_hi, qt_hi[jj])
                j1 = idx[float(cj1)]
                gy_floor = min(float(g_lo[m + 1][jj]), float(g_lo[m + 1][j1]))
                gy_ceil = (E_INV if cj <= 0.0 <= cj1
                           else max(float(g_hi[m][jj]), float(g_hi[m][j1])))
                m1_lo = gy_floor * ((cj1 - ub) ** 2 - (cj - ub) ** 2) / 2.0  # decreasing
                m2_hi = gy_ceil * ((cj1 - ua) ** 3 - (cj - ua) ** 3) / 3.0   # decreasing
                gx_lo = np.minimum(g_lo[l + 1][:jj], g_lo[l + 1][1:jj + 1])
                gx_hi = np.maximum(g_hi[l][:jj], g_hi[l][1:jj + 1])
                p2 = float(np.sum(wdt * gx_lo * t_lo ** 2 * np.maximum(m1_lo, 0.0)))
                p4 = float(np.sum(wdt * gx_hi * t_hi ** 4 * m2_hi))
                main_acc += v2 * p2 / 4.0
                quart_acc += v4 * p4 / 48.0
                total += v2 * p2 / 4.0 - v4 * p4 / 48.0
    if diagnostics is not None:
        diagnostics.update(main_term=2.0 * main_acc / z_hi ** 2,
                           quartic_term=2.0 * quart_acc / z_hi ** 2)
    return 2.0 * total / z_hi ** 2 * (1.0 - SLACK)


# ---------------------------------------------------------------------------
# 5. Guards on the two trigonometric inequalities actually used.
# ---------------------------------------------------------------------------
def guard_polynomials():
    a = np.linspace(0.0, 12.0, 240001)
    p = (1.0 - np.cos(np.minimum(math.pi, a))) / 2.0
    return {"p_le_a2_over_4": bool(np.all(p <= a ** 2 / 4.0 + 1e-15)),
            "p_ge_a2_4_minus_a4_48": bool(np.all(p >= a ** 2 / 4.0 - a ** 4 / 48.0 - 1e-15))}


def _q_f(w):
    s = _s_approx(float(w))
    return 2.0 * math.exp(-0.5 * s) / s ** 1.5


def guard_pointwise(lam, npts=7, mutation="none"):
    """The whole certificate rests on two pointwise inequalities, for every
    ordered pair:  b_anchor <= b_line  (the anchored profile never exceeds the
    real straight-line budget) and  b_line <= a  (the Cauchy-Schwarz bound
    dominates that explicit path).  B1.2 places Delta_max between b_line and a,
    so a failure here would invalidate the chain.  Checked on a fixed lattice.

    `mutation` deliberately breaks one step, so the guard's own sensitivity is
    measured rather than assumed:
      anchor_above    anchor moved three bins past the legal c_j
      anchor_top      anchor moved to u_in, ignoring U_y altogether
      qtilde_wrong_V  the V endpoint of qtilde flipped to the favourable side
    Each must be caught; a guard that cannot fail certifies nothing.
    """
    v0, v1, uout, uin, _ = lam
    c = np.linspace(-uout, uin, K_ANCHORS + 1)
    t = np.linspace(v0, v1, L_CELLS + 1)
    Us = np.linspace(-uout, uin, npts)
    Vs = np.linspace(v0, v1, npts)
    tested = 0
    worst_anchor = worst_cs = -math.inf
    for ux in Us:
        for uy in Us:
            if uy <= ux:
                continue
            for vx in Vs:
                for vy in Vs:
                    if vy <= vx:
                        continue
                    du, dv = uy - ux, vy - vx
                    z = np.linspace(vx, vy, 301)
                    qline = np.array([_q_f(u * V) for u, V in
                                      zip(ux + (du / dv) * (z - vx), z)])
                    b_line = math.sqrt(du / dv) * float(np.trapz(qline, z))
                    qy = np.array([_q_f(uy * V) for V in z])
                    a_cs = math.sqrt(du * float(np.trapz(qy ** 2, z)))
                    j = min(int(np.searchsorted(c, uy, side="right") - 1), K_ANCHORS - 1)
                    anchor = c[j]
                    if mutation == "anchor_above":
                        anchor = c[min(j + 3, K_ANCHORS)]
                    elif mutation == "anchor_top":
                        anchor = uin
                    if anchor <= ux:
                        continue
                    l = min(int(np.searchsorted(t, vx, side="right") - 1), L_CELLS - 1)
                    m = min(int(np.searchsorted(t, vy, side="right") - 1), L_CELLS - 1)
                    u_seg = np.linspace(ux, anchor, 301)
                    if mutation == "qtilde_wrong_V":
                        qt = np.array([_q_f(u * t[l]) for u in u_seg])
                    else:
                        qt = np.array([_q_f(u * (t[m + 1] if u < 0 else t[l]))
                                       for u in u_seg])
                    T = float(np.trapz(qt, u_seg)) / (anchor - ux)
                    b_anchor = math.sqrt(du * dv) * T
                    tested += 1
                    worst_anchor = max(worst_anchor, b_anchor - b_line)
                    worst_cs = max(worst_cs, b_line - a_cs)
    clean = mutation == "none"
    violated = worst_anchor > 1e-9 or worst_cs > 1e-9
    return {"pairs_tested": tested,
            "max_violation_anchor_le_line": worst_anchor,
            "max_violation_line_le_cauchy_schwarz": worst_cs,
            "ok": bool((not violated) if clean else violated)}


def main():
    assert LAMBDA0 == (0.5, 1.0, 1.0, 0.5, 0.1) and LAMBDA1 == (0.2, 0.8, 2.0, 0.9, 0.1)
    guards = guard_polynomials()
    muts = ("none", "anchor_above", "anchor_top", "qtilde_wrong_V")
    guards_pw = {nm: {mu: guard_pointwise(lam, mutation=mu) for mu in muts}
                 for nm, lam in (("lambda0", LAMBDA0), ("lambda1", LAMBDA1))}
    diag0, diag1 = {}, {}
    u0, u1 = rho_upper(LAMBDA0), rho_upper(LAMBDA1)
    l0 = rho_lower(LAMBDA0, diag0)
    l1 = rho_lower(LAMBDA1, diag1)
    z0, z1 = z_bracket(LAMBDA0), z_bracket(LAMBDA1)
    guards_ok = (all(guards.values())
                 and all(r["ok"] for lamres in guards_pw.values() for r in lamres.values())
                 and l0 <= u0 and l1 <= u1)
    separated = bool(u0 < l1 and guards_ok)
    out = {
        "unit": "PUENTE-3P1/B1.5",
        "frozen_pair": True,
        "lambda_pair": [list(LAMBDA0), list(LAMBDA1)],
        "method": "closed_form_inequality_chain_one_dimensional_integrals_only",
        "proof_parameters": {"K_anchors": K_ANCHORS, "L_cells": L_CELLS,
                             "N_cells_U": N_CELLS_U, "N_cells_V": N_CELLS_V,
                             "relative_slack": SLACK},
        "scalar_layer": {"s_enclosure": "verified_by_monotone_scalar_inequality",
                         "lambert_w_used": False,
                         "interval_arithmetic": "scalar_only_mpmath_iv_dps25"},
        "trigonometric_guards": guards,
        "pointwise_inequality_guards": guards_pw,
        "Z_bracket_lambda0": list(z0), "Z_bracket_lambda1": list(z1),
        "rho_lambda0_upper_U0": u0, "rho_lambda0_lower": l0,
        "rho_lambda1_upper": u1, "rho_lambda1_lower_L1": l1,
        "lower_bound_decomposition_lambda1": diag1,
        "analytic_separation_gap": l1 - u0,
        "relative_margin": (l1 - u0) / u0 if u0 > 0 else None,
        "b14_numerical_band_lambda0": [0.012756190222626588, 0.018794228860215523],
        "b14_numerical_band_lambda1": [0.027931264080398928, 0.04383499708576354],
        "consistency_upper_above_lower": bool(l0 <= u0 and l1 <= u1),
        "consistency_with_b14_bands": bool(u0 >= 0.012756190222626588
                                           and l1 <= 0.04383499708576354),
        "no_search": True, "no_seeds": True, "no_monte_carlo": True,
        "no_multidimensional_quadrature": True,
        "terminal": ("B1.5_ANALYTIC_SEPARATION_ESTABLISHED" if separated
                     else "B1.5_ANALYTIC_CERTIFICATION_TOO_COSTLY"),
        "B1_FORMAL_CERTIFICATE": "ESTABLISHED" if separated else "NOT_ESTABLISHED",
    }
    print(json.dumps(out, indent=2))
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "verification_b1_5_analytic_separation.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
