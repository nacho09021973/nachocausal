"""Symbolic verification for Proposition 5 (global rigidity, §4) and Proposition 6
(dilation invariance of V*Ibar, §5a) of wp4_fisher_localization_floor.md.

Mathematics-only check: symbolic algebra (sympy), no sampling, no simulation,
no estimator. Run with: python3 research_program/work_packages/wp4_fisher_localization_floor_symbolic_checks.py

Proposition 5 checks, in order:
  1. R_t(v,r) = -2t/r^3 for g_t = -(1-t/r) dv^2 + 2 dv dr (the Ricci scalar cited
     in the annex).
  2. Constant-conformal covariance R[kappa*g] = R[g]/kappa for this metric family.
  3. The v-derivative identity psi'(v) = (tau'/tau) * u * phi'(u) / phi(u) used to
     go from the r-preservation functional equation to the power-law ansatz for phi.
  4. The final polynomial-coefficient contradiction: matching the r^1 and r^0
     coefficients of tau(r-tau) = C*tau2*(r-tau2) forces two different values of C
     (tau/tau2 and (tau/tau2)^2), equal only when tau2 = tau.
  FIXED GAP (found by audit, now fixed in the write-up): step 3's ORIGINAL derivation
  used the power-law ansatz phi(u) = K*|u|^C, which is not valid across u = 0 (phi
  must change sign to map Ũ_tau(p) < 0 to Ũ_tau'(p) < 0 and Ũ_tau(q) > 0 to
  Ũ_tau'(q) > 0). Checks 3-4 below reproduce that original derivation for the
  historical record only; the annex's step 3 now cites check_r_derivative_route()
  instead, which differentiates (*) directly in r and eliminates phi(u) via (*)
  itself -- never solving for phi in closed form, so the sign-branch issue never
  arises.

Proposition 6 checks (§5a, dilation invariance of V*Ibar):
  5. W_{s*t}(s*r) = W_t(r) and Ũ_{s*t}(s*v, s*r) = Ũ_t(v, r) exactly (dilation
     covariance of the null coordinate).
  6. The Jacobian of (v,r) -> (s*v, s*r) is s^2 (area scaling V'(s*tau) = s^2 V(tau)).
"""
import sympy as sp


def check_ricci_scalar_and_conformal_covariance():
    v, r, tau, kappa = sp.symbols('v r tau kappa', positive=True)
    f = 1 - tau / r
    g = sp.Matrix([[-f, 1], [1, 0]])
    coords = [v, r]

    def ricci_scalar(gmat):
        n = len(coords)
        ginv = gmat.inv()
        Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    s = 0
                    for l in range(n):
                        s += ginv[k, l] * (
                            sp.diff(gmat[l, i], coords[j])
                            + sp.diff(gmat[l, j], coords[i])
                            - sp.diff(gmat[i, j], coords[l])
                        )
                    Gamma[k][i][j] = sp.simplify(s / 2)

        def riemann(l, i, j, k):
            term = sp.diff(Gamma[l][j][k], coords[i]) - sp.diff(Gamma[l][i][k], coords[j])
            for m in range(n):
                term += Gamma[l][i][m] * Gamma[m][j][k] - Gamma[l][j][m] * Gamma[m][i][k]
            return sp.simplify(term)

        ric = sp.zeros(n, n)
        for j in range(n):
            for k in range(n):
                ric[j, k] = sp.simplify(sum(riemann(i, j, i, k) for i in range(n)))

        return sp.simplify(sum(ginv[j, k] * ric[j, k] for j in range(n) for k in range(n)))

    R_g = ricci_scalar(g)
    R_kg = ricci_scalar(kappa * g)

    assert sp.simplify(R_g - (-2 * tau / r**3)) == 0, "Ricci scalar formula mismatch"
    assert sp.simplify(R_kg - R_g / kappa) == 0, "constant-conformal covariance mismatch"
    print("[1,2] R_t(v,r) = -2t/r^3, verified:", R_g)
    print("      R[kappa*g] = R[g]/kappa, verified:", R_kg)


def check_derivative_identity():
    v, r, tau, tau2 = sp.symbols('v r tau tau2', positive=True)
    phi = sp.Function('phi')
    psi = sp.Function('psi')

    W = lambda t: sp.exp(r / t) * (r / t - 1)
    u = -sp.exp(-v / (2 * tau)) * W(tau)
    rhs = -sp.exp(psi(v) / (2 * tau2)) * phi(u)

    d_rhs_dv = sp.diff(rhs, v)
    dpsi = sp.diff(psi(v), v)
    sol = sp.solve(sp.Eq(d_rhs_dv, 0), dpsi)[0]

    # Expected: psi'(v) = tau2 * u * phi'(u) / (tau * phi(u))
    phiprime_at_u = sp.Subs(sp.Derivative(phi(sp.Symbol('xi')), sp.Symbol('xi')), sp.Symbol('xi'), u).doit()
    expected = tau2 * u * phiprime_at_u / (tau * phi(u))
    assert sp.simplify(sol - expected) == 0, "derivative identity mismatch"
    print("[3] psi'(v) = (tau2/tau) * u * phi'(u)/phi(u), verified")


def check_final_contradiction():
    r, tau, tau2, C = sp.symbols('r tau tau2 C', positive=True)
    lhs_poly = sp.expand(tau * (r - tau))
    rhs_poly = sp.expand(C * tau2 * (r - tau2))
    diff_poly = sp.Poly(lhs_poly - rhs_poly, r)
    coeff_r1 = diff_poly.coeff_monomial(r)
    coeff_r0 = diff_poly.coeff_monomial(1)

    sol_from_r1 = sp.solve(sp.Eq(coeff_r1, 0), C)[0]
    sol_from_r0 = sp.solve(sp.Eq(coeff_r0, 0), C)[0]
    assert sp.simplify(sol_from_r1 - tau / tau2) == 0
    assert sp.simplify(sol_from_r0 - (tau / tau2) ** 2) == 0

    agree_only_when = sp.solve(sp.Eq(sol_from_r1, sol_from_r0), tau2)
    assert agree_only_when == [tau], "expected agreement only at tau2 = tau"
    print("[4] C = tau/tau2 (r^1 coeff) vs C = (tau/tau2)^2 (r^0 coeff);")
    print("    equal only when tau2 =", agree_only_when, " -- contradiction for tau2 != tau, verified")


def check_r_derivative_route():
    """Audit fix for step 3: derive L_tau2(r) = h(u) * L_tau(r) directly from the
    r-derivative of equation (*), eliminating phi(u) via (*) itself -- never solving
    for phi in closed form, so the u=0 sign-branch issue of the phi=K|u|^C ansatz
    never arises."""
    v, r, tau, tau2 = sp.symbols('v r tau tau2', positive=True)
    phi = sp.Function('phi')
    psi = sp.Function('psi')
    P0 = sp.Symbol('P0')

    W = lambda t: sp.exp(r / t) * (r / t - 1)
    u_expr = -sp.exp(-v / (2 * tau)) * W(tau)
    rhs = -sp.exp(psi(v) / (2 * tau2)) * phi(u_expr)
    lhs = W(tau2)

    eqB_expr = sp.expand(sp.diff(lhs, r) - sp.diff(rhs, r))
    subs_atom = list(eqB_expr.atoms(sp.Subs))[0]     # stands for phi'(u)
    phi0_atom = [a for a in eqB_expr.atoms(sp.Function) if a.func == phi][0]  # phi(u)
    P1 = sp.Symbol('P1')
    eqB_sub = eqB_expr.subs({subs_atom: P1, phi0_atom: P0})

    sol_P1 = sp.solve(sp.Eq(eqB_sub, 0), P1)[0]
    h_from_dr = sp.simplify(u_expr * sol_P1 / P0)

    # eliminate P0 and psi(v) using equation (*) itself: W(tau2) = -e^{psi/2tau2} * P0
    P0_value = -W(tau2) * sp.exp(-psi(v) / (2 * tau2))
    h_closed = sp.simplify(h_from_dr.subs(P0, P0_value))

    L = lambda t: sp.simplify(sp.diff(W(t), r) / W(t))
    ratio = sp.simplify(L(tau2) / L(tau))

    assert sp.simplify(h_closed - ratio) == 0, "r-derivative route does not match L_tau2/L_tau"
    print("[3'] audit fix: h(u) from d/dr of (*), P0 eliminated via (*) itself, equals")
    print("     L_tau2(r)/L_tau(r) =", ratio, " -- verified, no phi(u) closed form needed")


def check_dilation_covariance():
    v, r, tau, s = sp.symbols('v r tau s', positive=True)
    W = lambda t, rr: sp.exp(rr / t) * (rr / t - 1)
    Utilde = lambda t, vv, rr: -sp.exp(-vv / (2 * t)) * W(t, rr)

    check_W = sp.simplify(W(s * tau, s * r) - W(tau, r))
    check_U = sp.simplify(Utilde(s * tau, s * v, s * r) - Utilde(tau, v, r))
    assert check_W == 0 and check_U == 0, "dilation covariance of W or Utilde failed"
    print("[5] W_(s*t)(s*r) = W_t(r) and Ũ_(s*t)(s*v,s*r) = Ũ_t(v,r): verified, diff =", check_W, check_U)

    Jac = sp.Matrix([[sp.diff(s * v, v), sp.diff(s * v, r)],
                      [sp.diff(s * r, v), sp.diff(s * r, r)]]).det()
    assert sp.simplify(Jac - s**2) == 0, "area Jacobian mismatch"
    print("[6] Jacobian of (v,r)->(s*v,s*r) =", Jac, " => V'(s*tau) = s^2 * V(tau)")
    print("\n    Conclusion (Proposition 6): kappa(tau) := V(tau)*I(tau) satisfies")
    print("    V'(s*tau)*I'(s*tau) = [s^2 V(tau)] * [I(tau)/s^2] = V(tau)*I(tau) = kappa(tau),")
    print("    i.e. kappa is invariant under the joint corner+tau-range dilation by any s>0.")


if __name__ == "__main__":
    check_ricci_scalar_and_conformal_covariance()
    check_derivative_identity()
    check_final_contradiction()
    check_r_derivative_route()
    print("\nAll checks for Proposition 5 passed (including the audit-fix route for step 3).")
    print()
    check_dilation_covariance()
    print("\nAll checks for Proposition 6 (§5a) passed.")
