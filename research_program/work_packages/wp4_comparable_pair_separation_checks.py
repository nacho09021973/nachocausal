"""Verification script for wp4_comparable_pair_separation.md.

Subject: p(tau) := P(two i.i.d. points from the normalized volume measure of the
WP4 §4 causal diamond D_tau are causally comparable) -- i.e. the concordance
probability of the copula c_tau, equivalently (1 + Kendall's tau_K(c_tau))/2.
This is the scalar p(theta) of `research_program/bibliography/ficha_se_busca_tv_order_only.md`
§7.1 / §2.1(B), whose non-constancy was `[OPEN por par]`.

Mathematics only. NOT part of the sealed instrument: this script touches no
threshold, no seed band, no generator, no estimator, no validation artifact, and
imports nothing from `nachocausal/`. It runs symbolic algebra (sympy), determin-
istic Gauss-Legendre quadrature, and one fixed-seed Monte-Carlo cross-check of
the quadrature.

Run with:
    .venv/bin/python research_program/work_packages/wp4_comparable_pair_separation_checks.py

Checks, in order:
  [1] sqrt(-det g) = 1 in EF coordinates (v, r): the sampling measure is dv dr.
  [2] rho(r, Delta) (the outgoing-ray flow) satisfies drho/dDelta = (rho-tau)/(2 rho).
  [3] Ray lemma (Lemma C1): int_{v0}^{v0+Delta} R(v) dv = rho^2 - r0^2 + tau*Delta,
      symbolically and numerically.
  [4] Reduction (Prop C2/C3): the 4D concordance integral collapses to a 2D one,
      cross-checked against a fixed-seed Monte Carlo.
  [5] Spectral convergence of the 2D quadrature.
  [6] Dilation invariance of p (the mandatory orbit test, ficha §4).
  [7] Symbolic derivation of the leading asymptotics kappa (Theorem C4), matched
      against Richardson-extrapolated quadrature.
  [8] Positivity of kappa's numerator, (x - 1/x)/2 - log(x) > 0 for x > 1.
  [9] The concrete pair: p(tau) != p(tau') at working precision.
"""
import numpy as np
import sympy as sp
from scipy.special import lambertw

E_CONST = np.e

# --------------------------------------------------------------------------
# numerics: the null-coordinate flow of the diamond family
# --------------------------------------------------------------------------


def omega(r, tau):
    """omega_tau(r) = e^{r/tau} (r/tau - 1); strictly increasing, omega(tau) = 0."""
    x = r / tau
    return np.exp(x) * (x - 1.0)


def omega_inv(w, tau):
    """Inverse of omega_tau, via the principal Lambert branch: tau*(1 + W_0(w/e))."""
    return tau * (1.0 + np.real(lambertw(np.asarray(w, dtype=float) / E_CONST, 0)))


def rho(r0, Delta, tau):
    """r at v = v0 + Delta along the outgoing null ray (Utilde = const) through (v0, r0)."""
    return omega_inv(np.exp(Delta / (2.0 * tau)) * omega(r0, tau), tau)


def area_sub(r_x, Delta, r_q, tau):
    """Area (in dv dr) of J^+(x) ^ J^-(q), with Delta = v_q - v_x -- Prop C2."""
    return rho(r_x, Delta, tau) ** 2 + rho(r_q, -Delta, tau) ** 2 - r_x**2 - r_q**2


def p_comparable(tau, r_p, r_q, dv, n_outer=80, n_inner=80):
    """p(tau) by the 2D Gauss-Legendre reduction of Prop C3. Returns (p, A_tot, N)."""
    c = float(dv)
    A_tot = area_sub(r_p, c, r_q, tau)

    xD, wD = np.polynomial.legendre.leggauss(n_outer)
    Delta = 0.5 * c * (xD + 1.0)          # Delta = v_q - v_x in [0, c]
    wDs = 0.5 * c * wD

    alpha = rho(r_p, c - Delta, tau)      # upper r-boundary of D at that v
    beta = rho(r_q, -Delta, tau)          # lower r-boundary of D at that v

    xR, wR = np.polynomial.legendre.leggauss(n_inner)
    mid = 0.5 * (alpha + beta)[:, None]
    half = 0.5 * (alpha - beta)[:, None]
    r = mid + half * xR[None, :]
    integrand = rho(r, Delta[:, None], tau) ** 2 + (beta**2)[:, None] - r**2 - r_q**2
    inner = half[:, 0] * (integrand * wR[None, :]).sum(axis=1)
    N = float((wDs * inner).sum())
    return 2.0 * N / A_tot**2, float(A_tot), N


def p_monte_carlo(tau, r_p, r_q, dv, n=400_000, seed=20260725):
    """Independent cross-check: uniform points in D by rejection, then count
    comparable pairs. Fixed seed; this is a quadrature check, not a sprinkling
    experiment (no poset is built, no estimator is evaluated)."""
    rng = np.random.default_rng(seed)
    c = float(dv)
    # Bounding box. The two r-boundaries are monotone in v but in OPPOSITE senses:
    # drho/dDelta = (rho-tau)/(2rho), so the exterior ray through p (r_p > tau)
    # rises in v while the interior ray through q (r_q < tau) falls. Hence the
    # extremes sit at opposite ends of the v-range -- min r = r_q (attained at
    # v = v_q), max r = rho(r_p, dv) (attained at v = v_q). Taking min/max over
    # both endpoints keeps this correct regardless of which side r_p, r_q fall on.
    r_hi = max(float(rho(r_p, c, tau)), float(r_p))
    r_lo = min(float(rho(r_q, -c, tau)), float(r_q))
    v, r = [], []
    got, tried = 0, 0
    while got < n:
        m = 2 * (n - got) + 1000
        vv = rng.uniform(0.0, c, size=m)
        rr = rng.uniform(r_lo, r_hi, size=m)
        keep = (rr <= rho(r_p, vv, tau)) & (rr >= rho(r_q, vv - c, tau))
        v.append(vv[keep])
        r.append(rr[keep])
        got += int(keep.sum())
        tried += m
    accept = got / tried
    v = np.concatenate(v)[:n]
    r = np.concatenate(r)[:n]
    U = -np.exp(-v / (2.0 * tau)) * omega(r, tau)

    # (a) direct pair counting
    half = n // 2
    i, j = slice(0, half), slice(half, 2 * half)
    comp = ((v[i] < v[j]) & (U[i] < U[j])) | ((v[j] < v[i]) & (U[j] < U[i]))
    # (b) same sample, but through the closed-form future area of Prop C2 --
    #     an independent check of that formula rather than of the ordering test
    Ax = area_sub(r, c - v, r_q, tau)
    A_tot = area_sub(r_p, c, r_q, tau)
    return dict(
        p_pairs=comp.mean(), se_pairs=comp.std(ddof=1) / np.sqrt(comp.size),
        p_future=2.0 * Ax.mean() / A_tot,
        se_future=2.0 * Ax.std(ddof=1) / np.sqrt(Ax.size) / A_tot,
        area_mc=accept * c * (r_hi - r_lo), area_closed=float(A_tot),
    )


def kappa_closed_form(r_p, r_q):
    """kappa of Theorem C4: [(rp^2-rq^2) - 2 rp rq log(rp/rq)] / [12 rp rq (rp-rq)^2]."""
    num = (r_p**2 - r_q**2) - 2.0 * r_p * r_q * np.log(r_p / r_q)
    return num / (12.0 * r_p * r_q * (r_p - r_q) ** 2)


def K_extrapolated(tau, r_p, r_q, dvs=(0.08, 0.04, 0.02, 0.01, 0.005, 0.0025), n=220):
    """Richardson extrapolation of (p - 1/2)/dv as dv -> 0."""
    ks = np.array([(p_comparable(tau, r_p, r_q, dv, n, n)[0] - 0.5) / dv for dv in dvs])
    col = ks
    while col.size > 1:                       # successive halving => error ~ dv
        col = 2.0 * col[1:] - col[:-1]
    return float(col[0]), ks


# --------------------------------------------------------------------------
# [1]-[3] symbolic checks
# --------------------------------------------------------------------------


def check_volume_measure():
    v, r, tau = sp.symbols('v r tau', positive=True)
    f = 1 - tau / r
    g = sp.Matrix([[-f, 1], [1, 0]])
    det = sp.simplify(g.det())
    assert det == -1, det
    print("[1] EF metric g = -(1-tau/r)dv^2 + 2 dv dr : det g =", det,
          "=> sqrt(-det g) = 1, sampling measure = dv dr (uniform Lebesgue).")


ORD = 4  # retained order of the lapse series


def _rho_series(sym_r, sym_lap, tau, order=ORD):
    """Series solution of drho/dDelta = (rho - tau)/(2 rho), rho(0) = r."""
    coeffs = [sym_r]
    for k in range(1, order):
        ck = sp.Symbol(f'_c{k}')
        trial = sum(coeffs[i] * sym_lap**i for i in range(k)) + ck * sym_lap**k
        resid = sp.expand(sp.diff(trial, sym_lap) * 2 * trial - (trial - tau))
        coeffs.append(sp.simplify(sp.solve(sp.Eq(resid.coeff(sym_lap, k - 1), 0), ck)[0]))
    return sum(coeffs[i] * sym_lap**i for i in range(order))


def check_ray_flow_and_lemma():
    r, L, tau = sp.symbols('r L tau', positive=True)
    rho_s = _rho_series(r, L, tau)
    resid = sp.simplify(sp.expand(
        sp.series(sp.diff(rho_s, L) * 2 * rho_s - (rho_s - tau), L, 0, ORD - 1).removeO()))
    assert resid == 0, resid
    print("[2] rho(r,Delta) series solves 2 rho rho' = rho - tau to O(Delta^%d): residual = %s"
          % (ORD - 1, resid))
    print("    rho = r + Delta*(r-tau)/(2r) + Delta^2*tau*(r-tau)/(8r^3) + ...")

    # Lemma C1, symbolically: d/dDelta [rho^2 + tau*Delta] = rho.
    lhs = sp.simplify(sp.expand(sp.series(
        sp.diff(rho_s**2 + tau * L, L) - rho_s, L, 0, ORD - 1).removeO()))
    assert lhs == 0, lhs
    print("[3] Lemma C1 symbolically: d/dDelta[rho^2 + tau*Delta] - rho =", lhs)

    # and numerically, against direct quadrature of the ray
    tau_n, r0, Delta = 1.3, 2.0, 0.7
    xs, ws = np.polynomial.legendre.leggauss(400)
    vv = 0.5 * Delta * (xs + 1.0)
    num = float((0.5 * Delta * ws * rho(r0, vv, tau_n)).sum())
    closed = float(rho(r0, Delta, tau_n) ** 2 - r0**2 + tau_n * Delta)
    print("    numerically (tau=1.3, r0=2.0, Delta=0.7): quadrature = %.15f, closed form = %.15f, "
          "|diff| = %.2e" % (num, closed, abs(num - closed)))
    assert abs(num - closed) < 1e-12


# --------------------------------------------------------------------------
# [7] symbolic derivation of kappa
# --------------------------------------------------------------------------


def derive_kappa_symbolically():
    r, D, c, t, tau, a, b = sp.symbols('r D c t tau a b', positive=True)
    L = sp.Symbol('L')
    rho_s = _rho_series(r, L, tau)

    def Q(x, s):
        """Q(x,s) = rho(x,s)^2 - x^2."""
        return sp.expand(rho_s.subs({r: x, L: s}) ** 2 - x**2)

    # antiderivative in r of Q(r, D), order by order in the lapse
    anti = {k: sp.integrate(sp.simplify(co), r)
            for (k,), co in sp.Poly(sp.expand(Q(r, D)), D).terms()}

    def Qanti(x, s, upto):
        return sum(anti[k] * s**k for k in sorted(anti) if k <= upto).subs(r, x)

    def trunc(expr, var, n):
        return sp.series(sp.expand(expr), var, 0, n).removeO()

    NEED = 3
    alpha = trunc(rho_s.subs({r: a, L: c - D}).subs(D, c * t), c, NEED)
    beta = trunc(rho_s.subs({r: b, L: -D}).subs(D, c * t), c, NEED)

    # M(Delta, c) = int_{beta}^{alpha} [Q(r,Delta) + Q(b,-Delta)] dr, Delta = c*t
    M = trunc(Qanti(alpha, c * t, 2) - Qanti(beta, c * t, 2)
              + Q(b, -c * t) * (alpha - beta), c, NEED)

    N = sp.expand(c * sp.integrate(sp.expand(M), (t, 0, 1)))
    A = sp.expand(Q(a, c) + Q(b, -c))

    # factor out the leading c-powers before dividing (N = c^2*Nhat, A = c*Ahat)
    Nhat = sp.simplify(sp.cancel(N / c**2))
    Ahat = sp.simplify(sp.cancel(A / c))
    p_ser = sp.series(2 * Nhat / Ahat**2, c, 0, 2).removeO()

    p0 = sp.simplify(p_ser.coeff(c, 0))
    K = sp.simplify(sp.factor(sp.simplify(p_ser.coeff(c, 1))))
    assert p0 == sp.Rational(1, 2), p0
    print("[7] symbolic expansion of p in the v-lapse dv:")
    print("    p(dv -> 0) =", p0, "  (the flat/independence value, as required)")
    print("    d p / d dv at 0 =", K)

    K_target = tau * ((a**2 - b**2) - 2 * a * b * sp.log(a / b)) / (12 * a * b * (a - b) ** 2)
    diff = sp.simplify(sp.expand_log(sp.simplify(K - K_target), force=True))
    assert diff == 0, diff
    print("    matches kappa*tau with kappa = [(a^2-b^2) - 2ab*log(a/b)] / [12ab(a-b)^2];"
          " difference =", diff)
    return K_target


def check_kappa_positivity():
    x = sp.Symbol('x', positive=True)
    phi = (x - 1 / x) / 2 - sp.log(x)
    dphi = sp.simplify(sp.diff(phi, x))
    assert sp.simplify(dphi - (x - 1) ** 2 / (2 * x**2)) == 0, dphi
    print("[8] positivity of kappa: with x = rp/rq > 1, numerator = 2 rp rq [(x-1/x)/2 - log x];")
    print("    phi(x) := (x-1/x)/2 - log x has phi(1) = 0 and phi'(x) =", dphi,
          "= (x-1)^2/(2x^2) > 0")
    print("    => phi(x) > 0 strictly for x > 1 => kappa(rp, rq) > 0 strictly. PROVED.")


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

# The concrete diamond of record for this note (admissible: 0 < r_q < tau < r_p).
R_P, R_Q = 3.0, 0.5
TAU_A, TAU_B = 1.0, 1.2          # the concrete pair (tau, tau')
DV_ASYMPTOTIC = 0.02             # inside the small-lapse regime of Theorem C4
DV_LARGE = 4.0                   # far outside it, for contrast


def main():
    check_volume_measure()
    print()
    check_ray_flow_and_lemma()
    print()

    print("[4] reduction cross-checked against fixed-seed Monte Carlo "
          "(r_p=%.1f, r_q=%.1f, dv=%.2f):" % (R_P, R_Q, DV_LARGE))
    for tau in (1.0, 2.5):
        pq = p_comparable(tau, R_P, R_Q, DV_LARGE)[0]
        mc = p_monte_carlo(tau, R_P, R_Q, DV_LARGE)
        print("    tau=%.2f  quadrature p          = %.12f" % (tau, pq))
        print("             MC, pair counting     = %.6f +/- %.6f  (%.2f sigma)"
              % (mc['p_pairs'], mc['se_pairs'], abs(pq - mc['p_pairs']) / mc['se_pairs']))
        print("             MC, closed-form future= %.6f +/- %.6f  (%.2f sigma)"
              % (mc['p_future'], mc['se_future'], abs(pq - mc['p_future']) / mc['se_future']))
        print("             MC area = %.6f vs closed form A_tot = %.6f"
              % (mc['area_mc'], mc['area_closed']))
        assert abs(pq - mc['p_pairs']) < 4 * mc['se_pairs']
        assert abs(mc['area_mc'] - mc['area_closed']) < 0.01 * mc['area_closed']
    print()

    # The patch volume is tau-dependent, which is what makes the unconditioned
    # Poisson channel unusable for Forma L (note §5 item 1): with rho known, the
    # N-marginal would separate tau from tau' on its own. These are the values
    # the note cites; they are emitted here so the note quotes literal output.
    print("[4b] patch volume V(tau) = vol(D_tau), r_p=%.1f, r_q=%.1f "
          "(note §5 item 1, the cardinality confounder):" % (R_P, R_Q))
    for dv in (DV_LARGE, DV_ASYMPTOTIC):
        for tau in (TAU_A, TAU_B):
            print("     dv=%-5.2f tau=%.2f   V(tau) = %.12f"
                  % (dv, tau, area_sub(R_P, dv, R_Q, tau)))
        v_a = float(area_sub(R_P, dv, R_Q, TAU_A))
        v_b = float(area_sub(R_P, dv, R_Q, TAU_B))
        print("     dv=%-5.2f relative difference |V(tau')-V(tau)|/V(tau) = %.3e"
              % (dv, abs(v_b - v_a) / v_a))
        assert v_a != v_b, "V(tau) must depend on tau for §5 item 1 to hold"
    print()

    print("[5] spectral convergence of the 2D quadrature (tau=%.1f, dv=%.1f):" % (TAU_A, DV_LARGE))
    for n in (10, 20, 40, 80, 160):
        print("    n=%3d  p = %.15f" % (n, p_comparable(TAU_A, R_P, R_Q, DV_LARGE, n, n)[0]))
    print()

    print("[6] orbit test (ficha §4): p must be invariant under the joint dilation "
          "(tau, r_p, r_q, dv) -> s*(...)")
    base = p_comparable(1.0, 3.0, 0.5, 4.0)[0]
    for s in (0.37, 2.7, 11.0):
        got = p_comparable(s * 1.0, s * 3.0, s * 0.5, s * 4.0)[0]
        print("    s=%6.2f  p = %.15f   |diff| = %.2e" % (s, got, abs(got - base)))
        assert abs(got - base) < 1e-13
    print("    => p is a functional of the copula only; the scale orbit is invisible to it,")
    print("       as Theorem A requires. The statistic passes the mandatory orbit test.")
    print()

    derive_kappa_symbolically()
    print()
    check_kappa_positivity()
    print()

    print("[7b] closed-form kappa*tau vs Richardson-extrapolated quadrature:")
    print("     tau    r_p   r_q      closed form        extrapolated       rel.diff")
    cases = [(tau, 3.0, 0.5) for tau in (0.6, 1.0, 1.5, 2.5)] + \
            [(1.0, rp, 0.5) for rp in (2.0, 6.0)] + \
            [(1.0, 3.0, rq) for rq in (0.4, 0.9)]
    for tau, rp, rq in cases:
        cf = tau * kappa_closed_form(rp, rq)
        ex, _ = K_extrapolated(tau, rp, rq)
        print("    %5.2f  %4.1f  %4.2f   %.12f    %.12f    %.2e"
              % (tau, rp, rq, cf, ex, abs(cf - ex) / cf))
    print()

    print("[9] the concrete pair, r_p=%.1f, r_q=%.1f:" % (R_P, R_Q))
    for dv, label in ((DV_ASYMPTOTIC, "asymptotic regime"), (DV_LARGE, "outside it")):
        pa = p_comparable(TAU_A, R_P, R_Q, dv, 200, 200)[0]
        pb = p_comparable(TAU_B, R_P, R_Q, dv, 200, 200)[0]
        pred = kappa_closed_form(R_P, R_Q) * (TAU_B - TAU_A) * dv
        print("    dv=%.2f (%s):" % (dv, label))
        print("       p(tau=%.2f) = %.15f" % (TAU_A, pa))
        print("       p(tau=%.2f) = %.15f" % (TAU_B, pb))
        print("       p(tau') - p(tau) = %+.6e   (Theorem C4 leading term: %+.6e)"
              % (pb - pa, pred))
        print("       Kendall tau_K: %.12f vs %.12f" % (2 * pa - 1, 2 * pb - 1))
        assert pa != pb
    print()
    print("CONCLUSION: p(tau) != p(tau') for the WP4 §4 diamond family.")
    print("  - PROVED as dv -> 0: p = 1/2 + kappa(r_p,r_q)*tau*dv + O(dv^2), kappa > 0,")
    print("    so the leading term is strictly proportional to tau (check [7]+[8]).")
    print("  - VERIFIED numerically at the concrete pair above (check [9]).")
    print("  This closes ingredient (a) of ficha §7.1 for this family. It does NOT")
    print("  close Forma L: see wp4_comparable_pair_separation.md §5 for what remains.")


if __name__ == "__main__":
    main()
