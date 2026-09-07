"""Exact symbolic checks for the radial normal-channel algebra.

Requires SymPy. This script checks algebraic identities only; it does not
assert a Mellin/conormal expansion for a global reconstruction.
"""

import sympy as sp

x, y, p, beta, tau, s = sp.symbols("x y p beta tau s", positive=True, real=True)
I = sp.I

den_p = (p + 1) * (p + 2)
Jp = (x ** (p + 1) - 1) / ((1 - x) * den_p)
assert sp.simplify((1 - x) * Jp - (x ** (p + 1) - 1) / den_p) == 0

kappa_beta = (beta + 1) * (beta + 2)
Jbeta = (y ** (beta + 1) - 1) / ((1 - y) * kappa_beta)
A_beta = y * y**beta - kappa_beta * (1 - y) * Jbeta
assert sp.simplify(A_beta - 1) == 0

alpha = -sp.Rational(1, 2) + I * tau
kappa_tau = 6 / (alpha + 2)
assert sp.simplify(kappa_tau - 6 / (sp.Rational(3, 2) + I * tau)) == 0

# Re w and |w|^2 for w = 1 + 24/(3/2+i tau).
re_w = 1 + 36 / s
abs_w_sq = 1 + 648 / s
# Squaring |w| > 7 - 36/s gives this polynomial, when the RHS is nonnegative.
threshold_poly = sp.expand(
    s**2 * (abs_w_sq - (7 - 36 / s) ** 2)
)
assert sp.factor(threshold_poly) == -48 * (s**2 - 24 * s + 27)

roots = sp.solve(s**2 - 24 * s + 27, s)
assert roots == [12 - 3 * sp.sqrt(13), 12 + 3 * sp.sqrt(13)]
tau_sq_bound = sp.simplify(roots[1] - sp.Rational(9, 4))
assert tau_sq_bound == sp.Rational(39, 4) + 3 * sp.sqrt(13)

print("NORMAL_CHANNEL_ALGEBRA=PASS")
print("TAU_BOUND_SQUARED=", tau_sq_bound)
print("TAU_BOUND_NUMERIC=", sp.N(sp.sqrt(tau_sq_bound), 15))
