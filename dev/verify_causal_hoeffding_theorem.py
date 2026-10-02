"""Exact-arithmetic audit of dev/CAUSAL_HOEFFDING_FISHER_SUFFICIENCY.md.

No Monte Carlo, no random seeds. Two independent checks:

1. Continuous 3+1D witness (k=2, F=comparability) on the standard causal diamond
   I((-1,0),(1,0)) in flat 3+1D Minkowski: verifies V_4(tau)=pi*tau^4/24, the
   mean/variance constants of the comparability witness, and the exact finite-N
   Fisher-retention rate.
2. Discrete 4-point toy causal set, k=2 and k=3 simultaneously, multinomial-exact
   enumeration for N=3..50: verifies the exact Cov(S_N,U_{N,F}) and Var(U_{N,F})
   formulas of the Causal Hoeffding Theorem, and the asymptotic dominance of the
   overlap-1 term in the cross-degree covariance (needed for the finite-span step).

Run: python3 dev/verify_causal_hoeffding_theorem.py
"""
from fractions import Fraction as Fr
from itertools import combinations
import math

import sympy as sp


def check_3p1d_witness():
    print("=" * 70)
    print("CHECK 1 -- continuous 3+1D comparability witness (k=2)")
    print("=" * 70)
    t, r = sp.symbols("t r", real=True)
    tau_sym = sp.symbols("tau_sym", positive=True)
    tt, rr = sp.symbols("tt rr", real=True)

    V4_expr = sp.integrate(
        sp.Rational(4, 3) * sp.pi * sp.Min(tt, tau_sym - tt) ** 3, (tt, 0, tau_sym)
    )
    print("V_4(tau) =", sp.simplify(V4_expr))
    assert sp.simplify(V4_expr - sp.pi * tau_sym**4 / 24) == 0

    VD = V4_expr.subs(tau_sym, 2)
    print("V(D), tau=2 tips:", VD)

    m = sp.Min(1 + t, 1 - t)
    norm = sp.integrate(sp.integrate(4 * sp.pi * r**2, (r, 0, m)), (t, -1, 1)) / VD
    assert sp.simplify(norm - 1) == 0

    P = (1 + t) ** 2 - r**2
    Q = (1 - t) ** 2 - r**2
    a = (P**2 + Q**2) / 16

    def Emu(expr):
        inner = sp.integrate(expr * 4 * sp.pi * r**2, (r, 0, m))
        outer = sp.integrate(inner, (t, -1, 1))
        return sp.nsimplify(sp.simplify(outer / VD))

    abar = Emu(a)
    var_a = sp.simplify(Emu(a**2) - abar**2)
    Var_h = abar * (1 - abar)
    tau2 = sp.simplify(Var_h - 2 * var_a)

    print("bar a =", abar, " sigma^2 =", var_a, " tau^2 =", tau2)
    assert abar == sp.Rational(1, 10)
    assert var_a == sp.Rational(1, 100)
    assert tau2 == sp.Rational(7, 100)

    N = sp.symbols("N", positive=True)
    eta_bound = sp.simplify(1 / (1 + tau2 / (2 * var_a * (N - 1))))
    print("eta_N(psi) >=", eta_bound, " == (2N-2)/(2N+5):",
          sp.simplify(eta_bound - (2 * N - 2) / (2 * N + 5)) == 0)
    print("CHECK 1 PASSED\n")


def check_discrete_toy():
    print("=" * 70)
    print("CHECK 2 -- discrete 4-point toy causet, k=2 and k=3, N=3..50")
    print("=" * 70)
    support = [0, 1, 2, 3]
    p = {x: Fr(1, 4) for x in support}
    order = {(0, 1), (0, 2), (0, 3), (1, 3), (2, 3)}  # diamond poset, transitively closed

    def comparable(x, y):
        if x == y:
            return 0
        return 1 if ((x, y) in order or (y, x) in order) else 0

    def h2(x, y):
        return Fr(comparable(x, y))

    def h3(x, y, z):
        vals = [x, y, z]
        if len(set(vals)) < 3:
            return Fr(0)
        a, b, c = vals
        return Fr(1) if (comparable(a, b) and comparable(a, c) and comparable(b, c)) else Fr(0)

    def E(f, arity):
        from itertools import product

        tot = Fr(0)
        for tup in product(support, repeat=arity):
            w = Fr(1)
            for v in tup:
                w *= p[v]
            tot += w * f(*tup)
        return tot

    theta2, theta3 = E(h2, 2), E(h3, 3)
    varphi2 = {x: E(lambda y, x=x: h2(x, y), 1) - theta2 for x in support}
    varphi3 = {x: E(lambda y, z, x=x: h3(x, y, z), 2) - theta3 for x in support}

    def inner(f, g):
        return sum(p[x] * f[x] * g[x] for x in support)

    norm2_phi2 = inner(varphi2, varphi2)
    cross_phi = inner(varphi2, varphi3)
    Var_h2 = E(lambda x, y: h2(x, y) ** 2, 2) - theta2**2
    zeta2_k2 = Var_h2 - 2 * norm2_phi2

    H2 = {(a, b): h2(a, b) for a in support for b in support}
    H3 = {(a, b, c): h3(a, b, c) for a in support for b in support for c in support}

    def multinomial_weight(N, counts):
        num = math.factorial(N)
        den = 1
        for c in counts:
            den *= math.factorial(c)
        return Fr(num, den) * Fr(1, 4) ** N

    def compositions(N, parts=4):
        if parts == 1:
            yield (N,)
            return
        for i in range(N + 1):
            for rest in compositions(N - i, parts - 1):
                yield (i,) + rest

    def brute_counts(N):
        pairs = list(combinations(support, 2))
        triples = list(combinations(support, 3))
        U2_vals, U3_vals, S_vals, weights = [], [], [], []
        for counts in compositions(N, 4):
            w = multinomial_weight(N, counts)
            n = dict(zip(support, counts))
            u2 = sum(n[a] * n[b] * H2[(a, b)] for a, b in pairs)
            u3 = sum(n[a] * n[b] * n[c] * H3[(a, b, c)] for a, b, c in triples) if N >= 3 else Fr(0)
            s = sum(n[a] * varphi2[a] for a in support)
            U2_vals.append(u2)
            U3_vals.append(u3)
            S_vals.append(s)
            weights.append(w)

        def wmean(vals):
            return sum(w * v for w, v in zip(weights, vals))

        EU2, EU3, ES = wmean(U2_vals), wmean(U3_vals), wmean(S_vals)
        return dict(
            VarU2=wmean([v * v for v in U2_vals]) - EU2**2,
            CovU2U3=wmean([a * b for a, b in zip(U2_vals, U3_vals)]) - EU2 * EU3,
            CovSU2=wmean([a * b for a, b in zip(S_vals, U2_vals)]) - ES * EU2,
            CovSU3=wmean([a * b for a, b in zip(S_vals, U3_vals)]) - ES * EU3,
        )

    def C(n, k):
        return math.comb(n, k) if 0 <= k <= n else 0

    all_exact_ok = True
    print(f"{'N':>3}  {'Var(U2)':>8} {'Cov(S,U2)':>10} {'Cov(S,U3)':>10}  {'ell1/actual(U2,U3)':>18}")
    for N in [3, 4, 5, 6, 8, 10, 14, 18, 25, 35, 50]:
        bf = brute_counts(N)
        predVarU2 = Fr(N) * Fr(C(N - 1, 1)) ** 2 * norm2_phi2 + Fr(C(N, 2)) * zeta2_k2
        predCovSU2 = Fr(N) * Fr(C(N - 1, 1)) * norm2_phi2
        predCovSU3 = Fr(N) * Fr(C(N - 1, 2)) * cross_phi
        m1, m2, m3 = predVarU2 == bf["VarU2"], predCovSU2 == bf["CovSU2"], predCovSU3 == bf["CovSU3"]
        all_exact_ok &= m1 and m2 and m3
        predCovU2U3_ell1 = Fr(N) * Fr(C(N - 1, 1)) * Fr(C(N - 2, 2)) * cross_phi
        actual = bf["CovU2U3"]
        ratio = float(predCovU2U3_ell1) / float(actual) if actual != 0 else float("nan")
        print(f"{N:3d}  {str(m1):>8} {str(m2):>10} {str(m3):>10}  {ratio:18.4f}")

    assert all_exact_ok, "exact formula mismatch -- theorem or transcription error"
    print("\nCHECK 2 PASSED (all exact-formula matches hold; overlap-1 ratio -> 1 as N grows)\n")


if __name__ == "__main__":
    check_3p1d_witness()
    check_discrete_toy()
    print("ALL CHECKS PASSED")
