"""Exact second-order expansion of the unlabelled-poset law along the S1
antisymmetric witness.

Witness (roadmap §5.5, eq. (5.54)):  psi = e_1 (x) e_2 - e_2 (x) e_1,
with e_k the L2-normalised shifted Legendre modes on [0,1].

For N iid points from mu_eps = q_eps du dv, q_eps = e^{2 eps psi}/Z(eps), the
rank-permutation law is the finite integral

    p_pi(eps) = N! int_Delta int_Delta prod_i q_eps(u_i, v_pi(i)) dv du
              = <e^{2 eps T_pi}> / (N! Z(eps)^N),
    T_pi     = sum_i psi(u_i, v_pi(i)),

where <.> is expectation under two independent families of uniform order
statistics (density N! on the ordered simplex Delta).  Expanding,

    p_pi'(0)  = (2/N!) <T_pi>
    p_pi''(0) = (4/N!) ( <T_pi^2> - N sigma^2 ),   sigma^2 = int int psi^2 dmu_0

everything being a polynomial integral over a simplex, hence exact in Q.

Hellinger convention is the repository's:  H^2(p,q) = int (sqrt p - sqrt q)^2,
no factor 1/2 (wp6_domain_bridge_fixed_ef_box.md:119, manuscript_limits_draft.md:594).

For the intrinsic boundary coordinate theta = eps^2, the same exact data give

    d^+ p_C / d theta (0) = p_C''(0) / 2,
    score_C^+                = p_C''(0) / (2 p_C(0)),
    I_{N,theta}^+            = sum_C p_C''(0)^2 / (4 p_C(0)) = 4 K_N.

The accompanying roadmap proof establishes one-sided QMD at theta = 0.  This
backend checks its finite-alphabet coefficients; it does not claim ordinary
interior QMD or two-sided LAN at the boundary.

Exploratory WP6 backend.  Exact rational arithmetic, no seeds, no simulation.

Run:
    .venv/bin/python dev/wp6_second_order_antisymmetric_witness.py --n 2 3
"""

from __future__ import annotations

import argparse
import itertools
import json

import sympy as sp

A, B = sp.symbols("a b")


def shifted_legendre(k: int, t: sp.Expr) -> sp.Expr:
    return sp.sqrt(2 * k + 1) * sp.legendre(k, 2 * t - 1)


def witness() -> sp.Expr:
    """psi(a,b) = e_1(a) e_2(b) - e_2(a) e_1(b);  antisymmetric, P psi = psi."""
    return sp.expand(
        shifted_legendre(1, A) * shifted_legendre(2, B)
        - shifted_legendre(2, A) * shifted_legendre(1, B)
    )


def interaction_projection(expr: sp.Expr) -> sp.Expr:
    """P f = f - f_U - f_V + fbar, the S1 interaction projection (9.2)."""
    fu = sp.integrate(expr, (B, 0, 1))
    fv = sp.integrate(expr, (A, 0, 1))
    fbar = sp.integrate(sp.integrate(expr, (A, 0, 1)), (B, 0, 1))
    return sp.expand(expr - fu - fv + fbar)


def squared_witness_report() -> dict[str, str]:
    """psi is antisymmetric, so psi^2 is SYMMETRIC: the O(eps^2) term of q_eps
    lands in the symmetric interaction sector, the one with full retention."""
    psi = witness()
    square = sp.expand(psi**2)
    swapped = square.subs({A: B, B: A}, simultaneous=True)
    assert sp.simplify(square - swapped) == 0, "psi^2 must be symmetric"
    projected = interaction_projection(square)
    assert sp.simplify(projected) != 0, "P(psi^2) must not vanish"
    norm2 = sp.nsimplify(
        sp.integrate(sp.integrate(sp.expand(projected**2), (A, 0, 1)), (B, 0, 1))
    )
    return {
        "psi_squared_symmetric": "True",
        "P_psi_squared_nonzero": "True",
        "P_psi_squared_hs_norm_squared": str(norm2),
    }


def simplex_integral(expr: sp.Expr, vars_: list[sp.Symbol]) -> sp.Expr:
    """int over {0 < x_1 < ... < x_n < 1}: x_1 up to x_2, ..., x_n up to 1."""
    out = expr
    n = len(vars_)
    for i in range(n):
        hi = vars_[i + 1] if i < n - 1 else sp.Integer(1)
        out = sp.integrate(sp.expand(out), (vars_[i], 0, hi))
    return sp.expand(out)


def relation_mask(n: int, permutation: tuple[int, ...]) -> int:
    mask, bit = 0, 0
    for i in range(n):
        for j in range(n):
            if i != j:
                if i < j and permutation[i] < permutation[j]:
                    mask |= 1 << bit
                bit += 1
    return mask


def canonical_mask(n: int, mask: int) -> int:
    best: int | None = None
    for relabel in itertools.permutations(range(n)):
        edge_map = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    ri, rj = relabel[i], relabel[j]
                    edge_map.append(ri * (n - 1) + rj - (1 if rj > ri else 0))
        candidate, remaining = 0, mask
        while remaining:
            lowbit = remaining & -remaining
            candidate |= 1 << edge_map[lowbit.bit_length() - 1]
            remaining ^= lowbit
        if best is None or candidate < best:
            best = candidate
    assert best is not None
    return best


def n_relations(n: int, permutation: tuple[int, ...]) -> int:
    """Number of comparable ordered pairs; labels the class for small n."""
    return sum(
        1
        for i in range(n)
        for j in range(n)
        if i < j and permutation[i] < permutation[j]
    )


def analyse(n: int) -> dict[str, object]:
    us = list(sp.symbols(f"u1:{n + 1}", positive=True))
    vs = list(sp.symbols(f"v1:{n + 1}", positive=True))
    psi = witness()

    def psi_at(x: sp.Expr, y: sp.Expr) -> sp.Expr:
        return psi.subs({A: x, B: y}, simultaneous=True)

    sigma2 = sp.nsimplify(
        sp.integrate(sp.integrate(sp.expand(psi_at(A, B) ** 2), (A, 0, 1)), (B, 0, 1))
    )
    factorial = sp.factorial(n)
    permutations = list(itertools.permutations(range(n)))

    first: dict[tuple[int, ...], sp.Expr] = {}
    second: dict[tuple[int, ...], sp.Expr] = {}
    for permutation in permutations:
        score = sum(psi_at(us[i], vs[permutation[i]]) for i in range(n))
        m1 = simplex_integral(simplex_integral(sp.expand(score), us), vs)
        m2 = simplex_integral(simplex_integral(sp.expand(score**2), us), vs)
        m1 = sp.nsimplify(m1 * factorial**2)
        m2 = sp.nsimplify(m2 * factorial**2)
        first[permutation] = sp.nsimplify(2 * m1 / factorial)
        second[permutation] = sp.nsimplify(4 * (m2 - n * sigma2) / factorial)

    # Normalisation: the law sums to one identically in eps.
    assert sp.nsimplify(sum(first.values())) == 0
    assert sp.nsimplify(sum(second.values())) == 0

    # Reflection: swapping the two null coordinates inverts the permutation and
    # flips the first-order term.  This is (5.58) at the level of derivatives.
    for permutation in permutations:
        inverse = tuple(sorted(range(n), key=lambda i: permutation[i]))
        assert sp.simplify(first[permutation] + first[inverse]) == 0

    classes: dict[int, list[tuple[int, ...]]] = {}
    for permutation in permutations:
        classes.setdefault(
            canonical_mask(n, relation_mask(n, permutation)), []
        ).append(permutation)

    rows = []
    for key, members in sorted(classes.items()):
        c1 = sp.nsimplify(sum(first[p] for p in members))
        c2 = sp.nsimplify(sum(second[p] for p in members))
        p0 = sp.nsimplify(sp.Rational(len(members), factorial))
        theta_derivative = sp.nsimplify(c2 / 2)
        theta_score = sp.nsimplify(theta_derivative / p0)
        # Parity of the poset law: every class has vanishing first derivative.
        assert c1 == 0
        rows.append(
            {
                "size": len(members),
                "n_relations": n_relations(n, members[0]),
                "p0": str(p0),
                "second_derivative": str(c2),
                "second_derivative_float": float(c2),
                "theta_right_derivative_at_zero": str(theta_derivative),
                "theta_right_score_at_zero": str(theta_score),
            }
        )

    assert any(sp.nsimplify(row["second_derivative"]) != 0 for row in rows), (
        "no second-order signal: the witness would be invisible to this order"
    )

    # Hellinger, repository convention H^2 = int (sqrt p - sqrt q)^2 (no 1/2).
    # p_C(eps) = p_C(0) + (1/2) p_C''(0) eps^2 + O(eps^4) gives
    # H^2 = K_N eps^4 + o(eps^4),  K_N = sum_C p_C''(0)^2 / (16 p_C(0)).
    hellinger = sp.nsimplify(
        sum(
            sp.nsimplify(row["second_derivative"]) ** 2
            / (16 * sp.nsimplify(row["p0"]))
            for row in rows
        )
    )
    assert hellinger > 0

    # Boundary coordinate theta = eps^2.  Normalisation centres the right
    # score, and its L2(P_0) norm is exactly four times the eps^4 Hellinger
    # coefficient.  Positivity of every p0 follows here from nonempty fibres of
    # the uniform permutation law, so no zero-cell convention is needed.
    theta_score_mean = sp.nsimplify(
        sum(
            sp.nsimplify(row["p0"])
            * sp.nsimplify(row["theta_right_score_at_zero"])
            for row in rows
        )
    )
    theta_information = sp.nsimplify(
        sum(
            sp.nsimplify(row["p0"])
            * sp.nsimplify(row["theta_right_score_at_zero"]) ** 2
            for row in rows
        )
    )
    assert theta_score_mean == 0
    assert theta_information == 4 * hellinger

    return {
        "n": n,
        "sigma_squared": str(sigma2),
        "n_permutations": len(permutations),
        "n_poset_classes": len(classes),
        "classes": rows,
        "hellinger_quartic_coefficient": str(hellinger),
        "hellinger_quartic_coefficient_float": float(hellinger),
        "theta_right_score_mean": str(theta_score_mean),
        "theta_one_sided_fisher_information": str(theta_information),
        "theta_one_sided_fisher_information_float": float(theta_information),
        "theta_information_equals_four_times_hellinger_coefficient": "True",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, default=[2, 3])
    args = parser.parse_args()
    if any(n < 2 or n > 4 for n in args.n):
        parser.error("exact simplex backend intentionally capped at 2 <= N <= 4")
    payload = {
        "second_order_mechanism": squared_witness_report(),
        "theta_boundary_parameter": {
            "coordinate": "theta = epsilon^2",
            "parameter_space": "[0, +infinity)",
            "qmd_status": "PROVED_ONE_SIDED_AT_ZERO_IN_ROADMAP",
            "ordinary_interior_qmd_claimed": "False",
            "two_sided_lan_claimed": "False",
        },
        "by_cardinality": [analyse(n) for n in args.n],
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
