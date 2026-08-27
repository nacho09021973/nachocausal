#!/usr/bin/env python3
"""Bounded falsifier for the natural repeated-resistant-block construction.

This is not a permutation-space sweep.  It checks cross-block transpositions at
block distances one and two between the two exact realizers of one pure a=0
fibre in B_8.  For each binary block word it asks whether some endpoint swap
produces one winning orbit at a score strictly above the unchanged block score.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_tie_aut_diagnostic as tie_aut
from emergencia import p1a_tie_aut_generic_cross as generic_cross


REALIZERS = (
    (0, 1, 3, 4, 5, 7, 2, 6),
    (0, 1, 6, 2, 3, 4, 7, 5),
)
BLOCK_SIZE = 8


@dataclass(frozen=True)
class Diagnostic:
    score: tuple[int, int] | None
    n_orbits: int
    n_maximizers: int


def skew_pair(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(value + len(right) for value in left) + right


def skew_word(word: tuple[int, ...]) -> tuple[int, ...]:
    permutation: tuple[int, ...] = ()
    for realizer_type in word:
        permutation = skew_pair(permutation, REALIZERS[realizer_type])
    return permutation


def exact_diagnostic(permutation: tuple[int, ...]) -> Diagnostic:
    _, comparable, maximizers, score = generic_cross._materialize_expanded_maximizers(
        permutation
    )
    optimized = comparison.evaluate_selectors(permutation)[
        comparison.MIN_COVERAGE_LEX
    ]
    if len(maximizers) != optimized.n_maximizers:
        raise RuntimeError("materialized M does not match the optimized selector")
    if score is None:
        if optimized.state != comparison.STATE_EMPTY:
            raise RuntimeError("EMPTY mismatch in repeated-block probe")
        return Diagnostic(None, 0, 0)
    if score != (optimized.primary_score, optimized.secondary_score):
        raise RuntimeError("score mismatch in repeated-block probe")

    relation = tie_aut._as_relation(comparable)
    automorphisms = generic_cross._exact_colored_automorphisms(
        relation, (0,) * len(permutation)
    )
    orbits = tie_aut._orbit_partition(maximizers, automorphisms)
    return Diagnostic(score, len(orbits), len(maximizers))


def probe_internal_transpositions() -> bool:
    """Check the only internal swaps that could dominate untouched blocks."""

    found_strictly_higher_r1 = False
    for realizer_type, base in enumerate(REALIZERS):
        base_diagnostic = exact_diagnostic(base)
        strictly_higher = []
        repairs = []
        for left_index in range(BLOCK_SIZE):
            for right_index in range(left_index + 1, BLOCK_SIZE):
                modified = list(base)
                modified[left_index], modified[right_index] = (
                    modified[right_index],
                    modified[left_index],
                )
                diagnostic = exact_diagnostic(tuple(modified))
                if (
                    diagnostic.score is not None
                    and diagnostic.score > base_diagnostic.score
                ):
                    strictly_higher.append(
                        {
                            "left_index": left_index,
                            "right_index": right_index,
                            "score": diagnostic.score,
                            "n_orbits": diagnostic.n_orbits,
                        }
                    )
                if (
                    diagnostic.score is not None
                    and diagnostic.score > base_diagnostic.score
                    and diagnostic.n_orbits == 1
                ):
                    repairs.append(strictly_higher[-1])
        if repairs:
            found_strictly_higher_r1 = True
        print(
            f"REALIZER={realizer_type} INTERNAL_STRICT_HIGHER={len(strictly_higher)} "
            f"INTERNAL_STRICT_HIGHER_R1={len(repairs)} "
            f"FIRST_INTERNAL_HIGHER={strictly_higher[:1]}"
        )
    return found_strictly_higher_r1


def probe_word_length(length: int) -> bool:
    all_words_repairable = True
    for word in product(range(2), repeat=length):
        base = skew_word(word)
        base_diagnostic = exact_diagnostic(base)
        if base_diagnostic.score != (3, 6) or base_diagnostic.n_orbits != 2:
            raise RuntimeError("repeated resistant blocks did not reproduce B")

        strictly_higher = []
        repairs = []
        for left_index in range(BLOCK_SIZE):
            for right_local in range(BLOCK_SIZE):
                right_index = (length - 1) * BLOCK_SIZE + right_local
                modified = list(base)
                modified[left_index], modified[right_index] = (
                    modified[right_index],
                    modified[left_index],
                )
                diagnostic = exact_diagnostic(tuple(modified))
                if (
                    diagnostic.score is not None
                    and diagnostic.score > base_diagnostic.score
                ):
                    strictly_higher.append(
                        {
                            "left_index": left_index,
                            "right_index": right_local,
                            "score": diagnostic.score,
                            "n_orbits": diagnostic.n_orbits,
                        }
                    )
                if (
                    diagnostic.score is not None
                    and diagnostic.score > base_diagnostic.score
                    and diagnostic.n_orbits == 1
                ):
                    repairs.append(
                        {
                            "left_index": left_index,
                            "right_index": right_local,
                            "score": diagnostic.score,
                            "n_maximizers": diagnostic.n_maximizers,
                        }
                    )

        if not repairs:
            all_words_repairable = False
        print(
            f"WORD={''.join(str(value) for value in word)} "
            f"STRICT_HIGHER={len(strictly_higher)} "
            f"STRICT_HIGHER_R1={len(repairs)} "
            f"FIRST_HIGHER={strictly_higher[:1]}"
        )
    return all_words_repairable


def main() -> None:
    print("REPEATED_BLOCK_PROBE=BOUNDED_RADII_1_2_NO_FACTORIAL_SWEEP")
    internal_repair = probe_internal_transpositions()
    radius_one = probe_word_length(2)
    radius_two = probe_word_length(3)

    print(
        "F2_INTERNAL_REALIZERS=" + ("YES" if internal_repair else "NO")
    )
    print(
        "F2_ALL_WORDS_RADIUS_1=" + ("YES" if radius_one else "NO")
    )
    print(
        "F2_ALL_WORDS_RADIUS_2=" + ("YES" if radius_two else "NO")
    )


if __name__ == "__main__":
    main()
