"""Symbolic closure of the R2 near-horizon prefactor.

This is a deterministic algebra check: no sprinkling, simulation, estimator, or
random seed.  The geometry and notation are those of
``R2_lambda6_derivation_NOTES.md``:

    tau = 1 + lambda*sigma,
    r_p = 1 + a*lambda,  r_q = 1 - a*lambda,
    v_p = 0,             v_q = b*lambda.

Expanding the exact Lambert-W inverse of the outgoing null coordinate on the
fixed square (z,y) in [0,1]^2 gives the coefficients used below.  The script
checks the marginal projection that turns the fixed-square joint score into
the copula score, and then integrates its square exactly.
"""

import sympy as sp


def main():
    a, b, z, y = sp.symbols("a b z y", positive=True, real=True)
    Z, Y = z - sp.Rational(1, 2), y - sp.Rational(1, 2)

    # p = 1 + lambda*p1 + lambda^2*p2 + lambda^3*p3 + O(lambda^4).
    # Only p1, A2 := d_sigma p2, and A3 := d_sigma p3 at sigma=0
    # are needed for the leading tau-score, since d_tau=lambda^-1 d_sigma.
    p1 = 4 * a * Z + sp.Rational(1, 2) * b * Y
    A2 = -(2 * a + b) * Z + sp.Rational(1, 2) * b * Y
    A3 = (
        -192 * a**2 * z**2
        + 192 * a**2 * z
        - 32 * a**2
        + 36 * a * b * y * z
        - 18 * a * b * y
        - 108 * a * b * z**2
        + 90 * a * b * z
        - 9 * a * b
        + 6 * b**2 * y**2
        - 12 * b**2 * y * z
        + 6 * b**2 * z
        - 2 * b**2
    ) / 12

    # Fixed-square joint log-score at order lambda^2.
    B = sp.expand(A3 - p1 * A2)

    # At this order the marginal-quantile motion contributes only O(lambda^3):
    # p1 is additive and sigma-independent, and A2 is additive.  The copula
    # score is therefore the two-way (zero-marginal) projection of B.
    B_z = sp.integrate(B, (y, 0, 1))
    B_y = sp.integrate(B, (z, 0, 1))
    B_mean = sp.integrate(B, (z, 0, 1), (y, 0, 1))
    score2 = sp.factor(B - B_z - B_y + B_mean)
    expected_score2 = sp.Rational(1, 2) * b * (4 * a - b) * Z * Y
    assert sp.simplify(score2 - expected_score2) == 0

    fisher_coefficient = sp.factor(
        sp.integrate(score2**2, (z, 0, 1), (y, 0, 1))
    )
    expected_fisher = b**2 * (4 * a - b) ** 2 / 576
    assert sp.simplify(fisher_coefficient - expected_fisher) == 0

    volume_coefficient = 2 * a * b
    kappa_coefficient = sp.factor(volume_coefficient * fisher_coefficient)
    expected_kappa = a * b**3 * (4 * a - b) ** 2 / 288
    assert sp.simplify(kappa_coefficient - expected_kappa) == 0

    symmetric = sp.factor(kappa_coefficient.subs(b, a))
    assert sp.simplify(symmetric - a**6 / 32) == 0

    reference = sp.Rational(3, 10)
    reference_coefficient = sp.N(symmetric.subs(a, reference), 12)

    print("copula score / lambda^2 =", score2)
    print("I(1) / lambda^4        =", fisher_coefficient)
    print("V(1) / lambda^2        =", volume_coefficient)
    print("kappa(1) / lambda^6    =", kappa_coefficient)
    print("a=b specialization      =", symmetric)
    print("a=b=0.3 coefficient     =", reference_coefficient)
    print("exception                = b=4*a cancels the displayed leading term")
    print("R2 symbolic prefactor checks passed.")


if __name__ == "__main__":
    main()
