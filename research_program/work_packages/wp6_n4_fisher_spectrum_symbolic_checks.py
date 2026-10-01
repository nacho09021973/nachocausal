"""Exact symbolic checks for WP6 tangent classification, Section 15.

Run with the project environment:
    .venv/bin/python3 research_program/work_packages/
        wp6_n4_fisher_spectrum_symbolic_checks.py

The script enumerates all 24 permutations, quotients them by abstract-poset
isomorphism, integrates the order-statistic scores, and checks the two Fisher
Gram matrices and generalized characteristic polynomial using exact rationals.
"""

from __future__ import annotations

import itertools

import sympy as sp


U, V, LAMBDA = sp.symbols("u v lambda")
N = 4


def x(z: sp.Expr) -> sp.Expr:
    return z - sp.Rational(1, 2)


def q(z: sp.Expr) -> sp.Expr:
    return x(z) ** 2 - sp.Rational(1, 12)


def r(z: sp.Expr) -> sp.Expr:
    return x(z) ** 3 - sp.Rational(3, 20) * x(z)


POLYS = (x, q, r)


def order_density(rank: int, z: sp.Expr) -> sp.Expr:
    return N * sp.binomial(N - 1, rank) * z**rank * (1 - z) ** (N - 1 - rank)


def canonical_poset(permutation: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    relations = {
        (i, j)
        for i in range(N)
        for j in range(N)
        if i < j and permutation[i] < permutation[j]
    }
    return min(
        tuple(sorted((relabel[i], relabel[j]) for i, j in relations))
        for relabel in itertools.permutations(range(N))
    )


def integrate_unit_square(expr: sp.Expr) -> sp.Expr:
    return sp.integrate(sp.integrate(expr, (U, 0, 1)), (V, 0, 1))


def main() -> None:
    permutations = list(itertools.permutations(range(N)))
    classes: dict[tuple[tuple[int, int], ...], list[tuple[int, ...]]] = {}
    for permutation in permutations:
        classes.setdefault(canonical_poset(permutation), []).append(permutation)

    assert len(classes) == 16
    assert sorted(map(len, classes.values())) == [1] * 9 + [2] * 6 + [3]

    basis: list[sp.Expr] = []
    for i in range(3):
        for j in range(i, 3):
            term = POLYS[i](U) * POLYS[j](V)
            if i != j:
                term += POLYS[j](U) * POLYS[i](V)
            basis.append(sp.expand(term))

    derivatives: dict[tuple[int, ...], sp.Matrix] = {}
    for permutation in permutations:
        values = []
        for tangent in basis:
            value = sp.Rational(1, 12) * sum(
                integrate_unit_square(
                    tangent
                    * order_density(i, U)
                    * order_density(permutation[i], V)
                )
                for i in range(N)
            )
            values.append(sp.factor(value))
        derivatives[permutation] = sp.Matrix(values)

    class_derivatives = []
    poset_gram = sp.zeros(6)
    for members in classes.values():
        derivative = sum(
            (derivatives[member] for member in members), sp.zeros(6, 1)
        )
        probability = sp.Rational(len(members), sp.factorial(N))
        class_derivatives.append(derivative)
        poset_gram += derivative * derivative.T / probability

    assert sp.Matrix.hstack(*class_derivatives).rank() == 6

    expected_poset_gram = sp.Matrix(
        [
            [sp.Rational(4, 75), 0, 0, 0, 0, 0],
            [0, sp.Rational(8, 3375), 0, 0, 0, 0],
            [
                0,
                0,
                sp.Rational(1, 55125),
                sp.Rational(1, 354375),
                0,
                sp.Rational(1, 38587500),
            ],
            [
                0,
                0,
                sp.Rational(1, 354375),
                sp.Rational(11, 455625),
                0,
                -sp.Rational(1, 49612500),
            ],
            [0, 0, 0, 0, sp.Rational(2, 4134375), 0],
            [
                0,
                0,
                sp.Rational(1, 38587500),
                -sp.Rational(1, 49612500),
                0,
                sp.Rational(11, 5402250000),
            ],
        ]
    )
    assert poset_gram == expected_poset_gram

    full_gram = sp.Matrix(
        [
            [16 * integrate_unit_square(left * right) for right in basis]
            for left in basis
        ]
    )
    expected_full_gram = sp.diag(
        sp.Rational(1, 9),
        sp.Rational(2, 135),
        sp.Rational(1, 1050),
        sp.Rational(1, 2025),
        sp.Rational(1, 15750),
        sp.Rational(1, 490000),
    )
    assert full_gram == expected_full_gram

    operator = full_gram.inv() * poset_gram
    expected_characteristic = (
        (25 * LAMBDA - 12)
        * (25 * LAMBDA - 4)
        * (525 * LAMBDA - 4)
        * (
            144703125 * LAMBDA**3
            - 9975000 * LAMBDA**2
            + 142000 * LAMBDA
            - 128
        )
        / sp.Integer(47480712890625)
    )
    assert sp.factor(operator.charpoly(LAMBDA).as_expr()) == expected_characteristic

    # x tensor r has symmetric component e_13 / 2; its antisymmetric component
    # vanishes after quotienting by coordinate exchange.
    assert poset_gram[2, 2] / 4 == sp.Rational(1, 220500)

    cubic = (
        144703125 * LAMBDA**3
        - 9975000 * LAMBDA**2
        + 142000 * LAMBDA
        - 128
    )
    assert sp.discriminant(cubic, LAMBDA) == sp.Integer(303830148132000000000000)
    roots = sorted(float(root) for root in sp.nroots(cubic))
    expected_roots = [
        0.0009660470349413817,
        0.018516072040000612,
        0.0494521212878698,
    ]
    assert all(abs(actual - expected) < 1e-14 for actual, expected in zip(roots, expected_roots))

    print("N4_CLASSES=16")
    print("N4_VISIBLE_RANK=6")
    print("N3_TO_N4_WITNESS_I4=1/220500")
    print("N4_GENERALIZED_SPECTRUM_CHECK=PASS")


if __name__ == "__main__":
    main()
