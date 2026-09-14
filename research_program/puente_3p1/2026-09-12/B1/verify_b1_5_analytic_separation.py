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

Arithmetic.  Every step from the scalar enclosures to the final comparison keeps
its rounding direction outward (section 0).  No step relies on a rounding error
being small compared to the separation gap: the result is a directed-rounding
enclosure, not a float computation with a safety margin bolted on.  Audit
041 (AUDIT_PASS_CONDITIONAL_H4) required exactly this, the mathematics of the
chain having passed unchanged.

Determinism: no seeds, no Monte Carlo, no search over lambda, no fitting.  The
frozen pair is the one of B1.3 and is asserted against it below.
"""
import json
import math
import os
from fractions import Fraction

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

# ---------------------------------------------------------------------------
# 0. Directed rounding.  Each IEEE-754 binary64 operation is correctly rounded,
#    so its result differs from the exact value by at most half an ulp; moving
#    one ulp outward therefore bounds the exact value with certainty.  Sums use
#    math.fsum, which is exactly rounded regardless of sign or length, so a
#    single outward step suffices for a whole sum as well.
# ---------------------------------------------------------------------------
INF = float("inf")


def up(x):
    return np.nextafter(x, INF)


def dn(x):
    return np.nextafter(x, -INF)


def mul_up(a, b):
    return up(np.multiply(a, b))


def mul_dn(a, b):
    return dn(np.multiply(a, b))


def div_up(a, b):
    return up(np.divide(a, b))


def div_dn(a, b):
    return dn(np.divide(a, b))


def sub_up(a, b):
    return up(np.subtract(a, b))


def sub_dn(a, b):
    return dn(np.subtract(a, b))


def fsum_up(xs):
    return float(up(math.fsum(xs)))


def fsum_dn(xs):
    return float(dn(math.fsum(xs)))


def frac_up(fr):
    return float(up(float(fr)))


def frac_dn(fr):
    return float(dn(float(fr)))


# Recursive summation error constant, used only for the cumulative sums of
# section 4, where fsum cannot be applied prefix-wise at acceptable cost:
# |fl(sum) - sum| <= gamma_n * sum(|x_i|)  (Higham, Accuracy and Stability, 3.1).
_U_ROUND = 2.0 ** -53


def gamma_n(n):
    return (n * _U_ROUND) / (1.0 - n * _U_ROUND)


E_INV_HI = float(iv.exp(-iv.mpf(1)).b)     # rigorous upper bound for 1/e
E_INV_LO = float(iv.exp(-iv.mpf(1)).a)

# ---------------------------------------------------------------------------
# 1. Scalar layer.  s(w) is defined by (1-s)e^s = w on s>0, where f(s)=(1-s)e^s
#    is strictly decreasing (f'(s) = -s e^s < 0).  Hence
#        s >= a   <=>   f(a) >= w ,      s <= b   <=>   f(b) <= w ,
#    and an enclosure is certified by two scalar inequalities, each evaluated in
#    rigorous interval arithmetic.  No Lambert W routine is called anywhere.
#
#    A product such as U*t is itself rounded, so the exact argument lies in
#    [dn(U*t), up(U*t)]; the *_at helpers below enclose the function over that
#    whole interval, never at the rounded point alone.
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
    hi = E_INV_HI if a <= 1.0 <= b else max(float(va.b), float(vb.b))
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


def G_lo_at(wc):
    """Lower bound of G over the rounding interval of the product wc."""
    a, b = dn(wc), up(wc)
    return min(G_encl(a)[0], G_encl(b)[0])


def G_hi_at(wc):
    a, b = dn(wc), up(wc)
    if a <= 0.0 <= b:
        return E_INV_HI
    return max(G_encl(a)[1], G_encl(b)[1])


def q_lo_at(wc):
    return q_encl(dn(wc))[0]        # q increases in w


def q_hi_at(wc):
    return q_encl(up(wc))[1]


def arr_at(fn, ws):
    return np.array([fn(w) for w in ws], dtype=float)


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
#    monotone and endpoint values bracket the cell.  Refining in V shrinks the
#    envelope gap like 1/L while keeping every integral one-dimensional.
# ---------------------------------------------------------------------------
def z_bracket(lam):
    v0, v1, uout, uin, _ = lam
    U = grid(-uout, uin, N_CELLS_U, extra=(0.0,))
    t = np.linspace(v0, v1, L_CELLS + 1)
    w_dn, w_up = dn(np.diff(U)), up(np.diff(U))
    lo_terms, hi_terms = [], []
    for l in range(L_CELLS):
        lo_env = arr_at(G_lo_at, U * t[l + 1])
        hi_env = arr_at(G_hi_at, U * t[l])
        cell_lo = mul_dn(w_dn, np.minimum(lo_env[:-1], lo_env[1:]))
        cell_hi = mul_up(w_up, np.maximum(hi_env[:-1], hi_env[1:]))
        dt_dn, dt_up = dn(t[l + 1] - t[l]), up(t[l + 1] - t[l])
        lo_terms.append(mul_dn(fsum_dn(cell_lo), dt_dn))
        hi_terms.append(mul_up(fsum_up(cell_hi), dt_up))
    return fsum_dn(lo_terms), fsum_up(hi_terms)


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
def _wgt_exact(a, b, v0, v1):
    """int_a^b (V-v0)(v1-V) dV, exactly, as a rational (no cancellation risk)."""
    A, B, P, Q = Fraction(a), Fraction(b), Fraction(v0), Fraction(v1)
    prim = lambda z: -z ** 3 / 3 + (P + Q) * z ** 2 / 2 - P * Q * z
    return prim(B) - prim(A)


def rho_upper(lam):
    v0, v1, uout, uin, _ = lam
    z_lo, _ = z_bracket(lam)
    U = grid(-uout, uin, N_CELLS_U, extra=(0.0,))
    V = grid(v0, v1, N_CELLS_V)
    weights = np.array([frac_up(_wgt_exact(V[i], V[i + 1], v0, v1))
                        for i in range(len(V) - 1)])
    # C1(U) = int q(UV)^2 (V-v0)(v1-V) dV, upper bound; q^2 monotone in V
    c1_hi = np.empty(len(U))
    for i, u in enumerate(U):
        edge = V[1:] if u > 0 else V[:-1]        # the V endpoint maximising |w|-side
        qh = arr_at(q_hi_at, u * edge)
        c1_hi[i] = fsum_up(mul_up(weights, mul_up(qh, qh)))
    g_hi = arr_at(G_hi_at, U * v0)
    # A1(U) = e^{-1}(U+uout)^2/2, increasing; all factors non-negative
    off = up(np.add(U, uout))
    a1 = div_up(mul_up(E_INV_HI, mul_up(off, off)), 2.0)
    # C1 and A1 increase in U; Gcheck is unimodal with peak at the grid point 0
    cells = mul_up(up(np.diff(U)),
                   mul_up(np.maximum(g_hi[:-1], g_hi[1:]),
                          mul_up(a1[1:], c1_hi[1:])))
    main_hi = fsum_up(cells)
    return float(div_up(main_hi, mul_dn(2.0, mul_dn(z_lo, z_lo))))


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
#    one-dimensional pieces times the closed-form V moments below.
# ---------------------------------------------------------------------------
def _v_moments(A, B, C, D, same):
    """Exact rationals for int int (Vy-Vx) and int int (Vy-Vx)^2 over the block.

    Same cell: the ordered triangle, (B-A)^3/6 and (B-A)^4/12.  Distinct cells:
    the full rectangle [A,B] x [C,D], where the ordering is automatic.
    """
    A, B, C, D = Fraction(A), Fraction(B), Fraction(C), Fraction(D)
    if same:
        return (B - A) ** 3 / 6, (B - A) ** 4 / 12
    f2 = lambda z: z ** 3 / 6
    f4 = lambda z: z ** 4 / 12
    v2 = f2(D - A) - f2(D - B) - f2(C - A) + f2(C - B)
    v4 = f4(D - A) - f4(D - B) - f4(C - A) + f4(C - B)
    return v2, v4


def rho_lower(lam, diagnostics=None):
    v0, v1, uout, uin, _ = lam
    _, z_hi = z_bracket(lam)
    c = np.linspace(-uout, uin, K_ANCHORS + 1)
    t = np.linspace(v0, v1, L_CELLS + 1)
    U = grid(-uout, uin, N_CELLS_U, extra=tuple(c) + (0.0,))
    n_u = len(U)
    dU_dn, dU_up = dn(np.diff(U)), up(np.diff(U))
    idx = {float(x): int(np.argmin(np.abs(U - x))) for x in c}
    gam = gamma_n(n_u)

    g_lo = {l: arr_at(G_lo_at, U * t[l]) for l in range(L_CELLS + 1)}
    g_hi = {l: arr_at(G_hi_at, U * t[l]) for l in range(L_CELLS + 1)}
    q_lo = {l: arr_at(q_lo_at, U * t[l]) for l in range(L_CELLS + 1)}
    q_hi = {l: arr_at(q_hi_at, U * t[l]) for l in range(L_CELLS + 1)}
    neg = U < 0

    terms = []
    main_terms, quart_terms = [], []
    for l in range(L_CELLS):
        for m in range(l, L_CELLS):
            # qtilde_{l,m}(u): worst V in [t_l, t_{m+1}] -> t_{m+1} for u<0, t_l for u>=0
            qt_lo = np.where(neg, q_lo[m + 1], q_lo[l])
            qt_hi = np.where(neg, q_hi[m + 1], q_hi[l])
            # qtilde increases in u: lower/upper Riemann sums of its primitive.
            # cumsum is not exactly rounded, so its error is bounded explicitly.
            cl = np.concatenate([[0.0], np.cumsum(mul_dn(dU_dn, qt_lo[:-1]))])
            ch = np.concatenate([[0.0], np.cumsum(mul_up(dU_up, qt_hi[1:]))])
            err_lo = up(2.0 * gam * cl[-1])
            err_hi = up(2.0 * gam * ch[-1])
            v2f, v4f = _v_moments(t[l], t[l + 1], t[m], t[m + 1], m == l)
            v2, v4 = frac_dn(v2f), frac_up(v4f)
            for j in range(K_ANCHORS):
                cj, cj1 = c[j], c[j + 1]
                jj = idx[float(cj)]
                if jj < 1:
                    continue
                ua, ub, wdn = U[:jj], U[1:jj + 1], dU_dn[:jj]
                # T at the cell's left end (T increases in U_x) for the main term
                t_lo = np.maximum(0.0, div_dn(sub_dn(sub_dn(cl[jj], cl[:jj]), err_lo),
                                              up(np.subtract(cj, ua))))
                # T at the right end for the quartic term; the last cell ends at
                # c_j, where the average degenerates to qtilde(c_j), its supremum
                den_r = np.subtract(cj, ub)
                t_hi = np.full(jj, float(qt_hi[jj]))
                ok = den_r > 0
                if ok.any():
                    t_hi[ok] = div_up(sub_up(sub_up(ch[jj], ch[1:jj + 1][ok]), -err_hi),
                                      dn(den_r[ok]))
                t_hi = np.minimum(t_hi, float(qt_hi[jj]))
                j1 = idx[float(cj1)]
                gy_floor = min(float(g_lo[m + 1][jj]), float(g_lo[m + 1][j1]))
                gy_ceil = (E_INV_HI if cj <= 0.0 <= cj1
                           else max(float(g_hi[m][jj]), float(g_hi[m][j1])))
                # M1 = int Ghat(Uy)(Uy-Ux) dUy >= gy_floor (c1-c0)((c1-Ux)+(c0-Ux))/2
                # M2 = int Gcheck(Uy)(Uy-Ux)^2 dUy
                #    <= gy_ceil (c1-c0)((c1-Ux)^2+(c1-Ux)(c0-Ux)+(c0-Ux)^2)/3
                # Both rewritten without cancellation: every factor is >= 0.
                d1l, d0l = dn(np.subtract(cj1, ub)), dn(np.subtract(cj, ub))
                m1_lo = mul_dn(gy_floor,
                               div_dn(mul_dn(dn(cj1 - cj), dn(np.add(d1l, d0l))), 2.0))
                d1u, d0u = up(np.subtract(cj1, ua)), up(np.subtract(cj, ua))
                poly = up(np.add(np.add(mul_up(d1u, d1u), mul_up(d1u, d0u)),
                                 mul_up(d0u, d0u)))
                m2_hi = mul_up(gy_ceil, div_up(mul_up(up(cj1 - cj), poly), 3.0))
                gx_lo = np.minimum(g_lo[l + 1][:jj], g_lo[l + 1][1:jj + 1])
                gx_hi = np.maximum(g_hi[l][:jj], g_hi[l][1:jj + 1])
                p2 = fsum_dn(mul_dn(mul_dn(wdn, gx_lo),
                                    mul_dn(mul_dn(t_lo, t_lo), np.maximum(m1_lo, 0.0))))
                t2 = mul_up(t_hi, t_hi)
                p4 = fsum_up(mul_up(mul_up(dU_up[:jj], gx_hi), mul_up(mul_up(t2, t2), m2_hi)))
                main = div_dn(mul_dn(v2, max(p2, 0.0)), 4.0)
                quart = div_up(mul_up(v4, p4), 48.0)
                main_terms.append(main)
                quart_terms.append(quart)
                terms.append(main)
                terms.append(-quart)
    total_lo = fsum_dn(terms)
    if diagnostics is not None:
        diagnostics.update(
            main_term=float(div_dn(mul_dn(2.0, fsum_dn(main_terms)), mul_up(z_hi, z_hi))),
            quartic_term=float(div_up(mul_up(2.0, fsum_up(quart_terms)), mul_dn(z_hi, z_hi))))
    return float(div_dn(mul_dn(2.0, total_lo), mul_up(z_hi, z_hi)))


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
                             "N_cells_U": N_CELLS_U, "N_cells_V": N_CELLS_V},
        "scalar_layer": {"s_enclosure": "verified_by_monotone_scalar_inequality",
                         "lambert_w_used": False,
                         "interval_arithmetic": "scalar_only_mpmath_iv_dps25"},
        "arithmetic": {
            "mode": "outward_directed_rounding_end_to_end",
            "sums": "math.fsum (exactly rounded) then one ulp outward",
            "products_quotients": "one ulp outward after each binary64 operation",
            "cumulative_sums": "np.cumsum with explicit Higham gamma_n error term",
            "partition_moments": "exact rationals (fractions.Fraction), rounded outward",
            "products_of_grid_values": "enclosed over [dn(x*y), up(x*y)], not at the "
                                       "rounded point",
            "global_slack_constant": None,
        },
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
