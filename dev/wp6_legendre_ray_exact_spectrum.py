"""Exact finite-N Fisher spectrum for diagonal shifted-Legendre tangents.

Exploratory WP6 backend.  It enumerates permutations, quotients their product
orders by abstract-poset isomorphism, and computes exact rational Fisher Gram
matrices for ``e_k(u)e_k(v)``, where the shifted Legendre modes are L2-normalized.

The default N=4,5,6 run is deliberately small and exact.  It neither proves an
asymptotic statement nor promotes generated output to validation evidence.

Run:
    .venv/bin/python dev/wp6_legendre_ray_exact_spectrum.py
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import sympy as sp


Z = sp.symbols("z")


def order_density(n: int, rank: int) -> sp.Expr:
    return n * sp.binomial(n - 1, rank) * Z**rank * (1 - Z) ** (n - 1 - rank)


def legendre_order_moments(n: int) -> list[list[sp.Expr]]:
    """Return E[e_k(U_(i))], k=1..n-1 and zero-based rank i."""
    rows: list[list[sp.Expr]] = []
    for k in range(1, n):
        mode = sp.sqrt(2 * k + 1) * sp.legendre(k, 2 * Z - 1)
        rows.append(
            [
                sp.integrate(sp.expand(mode * order_density(n, i)), (Z, 0, 1))
                for i in range(n)
            ]
        )
    return rows


def relation_mask(n: int, permutation: tuple[int, ...]) -> int:
    mask = 0
    bit = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                if i < j and permutation[i] < permutation[j]:
                    mask |= 1 << bit
                bit += 1
    return mask


def relabel_maps(n: int) -> list[list[int]]:
    maps: list[list[int]] = []
    for relabel in itertools.permutations(range(n)):
        edge_map = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    ri, rj = relabel[i], relabel[j]
                    edge_map.append(ri * (n - 1) + rj - (1 if rj > ri else 0))
        maps.append(edge_map)
    return maps


def canonical_mask(mask: int, maps: list[list[int]]) -> int:
    best: int | None = None
    for edge_map in maps:
        candidate = 0
        remaining = mask
        while remaining:
            lowbit = remaining & -remaining
            source = lowbit.bit_length() - 1
            candidate |= 1 << edge_map[source]
            remaining ^= lowbit
        if best is None or candidate < best:
            best = candidate
    assert best is not None
    return best


def exact_spectrum(n: int) -> dict[str, object]:
    permutations = list(itertools.permutations(range(n)))
    moments = legendre_order_moments(n)
    relabelings = relabel_maps(n)
    classes: dict[int, list[int]] = {}
    scores: list[sp.Matrix] = []

    for index, permutation in enumerate(permutations):
        mask = relation_mask(n, permutation)
        key = canonical_mask(mask, relabelings)
        classes.setdefault(key, []).append(index)
        scores.append(
            sp.Matrix(
                [
                    sp.factor(
                        2
                        * sum(
                            moments[k][i] * moments[k][permutation[i]]
                            for i in range(n)
                        )
                    )
                    for k in range(n - 1)
                ]
            )
        )

    factorial = sp.factorial(n)
    oracle = sum((score * score.T for score in scores), sp.zeros(n - 1)) / factorial
    poset = sp.zeros(n - 1)
    for members in classes.values():
        score_sum = sum((scores[index] for index in members), sp.zeros(n - 1, 1))
        poset += score_sum * score_sum.T / (factorial * len(members))

    # Exact permutation-oracle formula.  Continuous Legendre orthogonality does
    # not imply finite-N orthogonality after the order-statistic projection.
    expected_oracle = sp.Matrix(
        n - 1,
        n - 1,
        lambda j, k: sp.Rational(4, n - 1)
        * sum(moments[j][i] * moments[k][i] for i in range(n)) ** 2,
    )
    assert oracle == expected_oracle
    assert poset == poset.T
    assert (oracle - poset).is_positive_semidefinite

    mode_eta = [sp.factor(poset[k, k] / oracle[k, k]) for k in range(n - 1)]
    if n >= 4:
        # Finite evidence for the candidate exact-visibility lemma.  This is an
        # assertion about the enumerated sizes, not a proof for arbitrary N.
        assert mode_eta[0] == 1
    fiber_witnesses: list[dict[str, object] | None] = []
    for k in range(n - 1):
        witness = None
        for members in classes.values():
            first = members[0]
            different = next(
                (index for index in members if scores[index][k] != scores[first][k]),
                None,
            )
            if different is not None:
                witness = {
                    "sigma": list(permutations[first]),
                    "tau": list(permutations[different]),
                    "score_sigma": str(scores[first][k]),
                    "score_tau": str(scores[different][k]),
                }
                break
        fiber_witnesses.append(witness)
    ray_eta = []
    for m in range(1, n):
        weights = sp.Matrix([sp.Rational(1, (k + 1) ** 2) for k in range(m)])
        ray_eta.append(
            sp.factor(
                (weights.T * poset[:m, :m] * weights)[0]
                / (weights.T * oracle[:m, :m] * weights)[0]
            )
        )

    return {
        "n": n,
        "n_permutations": math.factorial(n),
        "n_poset_classes": len(classes),
        "oracle_gram": [[str(value) for value in row] for row in oracle.tolist()],
        "poset_gram": [[str(value) for value in row] for row in poset.tolist()],
        "mode_eta": [str(value) for value in mode_eta],
        "mode_eta_decimal": [float(value) for value in mode_eta],
        "fiber_witnesses": fiber_witnesses,
        "ray_eta": [str(value) for value in ray_eta],
        "ray_eta_decimal": [float(value) for value in ray_eta],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, default=[4, 5, 6])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if any(n < 2 or n > 6 for n in args.n):
        parser.error("the exact exploratory backend is intentionally capped at 2 <= N <= 6")

    results = [exact_spectrum(n) for n in args.n]
    rendered = json.dumps(results, indent=2)
    if args.output is not None:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
