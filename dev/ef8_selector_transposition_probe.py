#!/usr/bin/env python3
"""Finite, exhaustive transposition probe for the EF-8 preflight.

This is exploratory diagnostics, not asymptotic evidence.  It enumerates every
permutation at n=6,7,8, evaluates the frozen MIN_COVERAGE_LEX implementation,
and checks every transposition leaving a UNIQUE state.
"""

from __future__ import annotations

import itertools
import json
import math
from collections.abc import Sequence

from emergencia.p1a_comparar_selectores_d2 import (
    MIN_COVERAGE_LEX,
    STATE_UNIQUE,
    ScoreOutcome,
    evaluate_selectors,
)


SIZES = (6, 7, 8)
DETERMINISTIC_SEQUENCE_SIZES = tuple(range(8, 42, 2))


def selected_z_values(
    permutation: Sequence[int], outcome: ScoreOutcome
) -> tuple[float, float]:
    """Return the past/future normalized rank-gap observables."""

    if outcome.state != STATE_UNIQUE or outcome.selection is None:
        raise ValueError("selected_z_values requires a UNIQUE outcome")
    n = len(permutation)
    a, b, c, d = outcome.selection.quadruple
    return (
        math.sqrt((b - a) * (permutation[b] - permutation[a])) / (n + 1),
        math.sqrt((d - c) * (permutation[d] - permutation[c])) / (n + 1),
    )


def transpose(
    permutation: tuple[int, ...], first: int, second: int
) -> tuple[int, ...]:
    result = list(permutation)
    result[first], result[second] = result[second], result[first]
    return tuple(result)


def probe_size(n: int) -> dict[str, object]:
    outcomes = {
        permutation: evaluate_selectors(permutation)[MIN_COVERAGE_LEX]
        for permutation in itertools.permutations(range(n))
    }
    unique = {
        permutation: outcome
        for permutation, outcome in outcomes.items()
        if outcome.state == STATE_UNIQUE
    }

    directed_edges = 0
    unique_to_nonunique = 0
    unique_to_unique = 0
    maximum_jump = -1.0
    maximum_witness: dict[str, object] | None = None

    for permutation, outcome in unique.items():
        values = selected_z_values(permutation, outcome)
        for first, second in itertools.combinations(range(n), 2):
            directed_edges += 1
            neighbor = transpose(permutation, first, second)
            neighbor_outcome = outcomes[neighbor]
            if neighbor_outcome.state != STATE_UNIQUE:
                unique_to_nonunique += 1
                continue

            unique_to_unique += 1
            neighbor_values = selected_z_values(neighbor, neighbor_outcome)
            jump = max(
                abs(value - neighbor_value)
                for value, neighbor_value in zip(values, neighbor_values)
            )
            if jump > maximum_jump:
                maximum_jump = jump
                assert outcome.selection is not None
                assert neighbor_outcome.selection is not None
                maximum_witness = {
                    "permutation": permutation,
                    "quadruple": outcome.selection.quadruple,
                    "z_values": values,
                    "transposition": (first, second),
                    "neighbor": neighbor,
                    "neighbor_quadruple": neighbor_outcome.selection.quadruple,
                    "neighbor_z_values": neighbor_values,
                }

    return {
        "n": n,
        "permutations": math.factorial(n),
        "unique": len(unique),
        "directed_edges_from_unique": directed_edges,
        "unique_to_nonunique": unique_to_nonunique,
        "unique_to_unique": unique_to_unique,
        "maximum_unique_to_unique_z_jump": (
            None if maximum_witness is None else maximum_jump
        ),
        "maximum_witness": maximum_witness,
    }


def probe_deterministic_sequence(n: int) -> dict[str, object]:
    """Check the same-limit UNIQUE/TIE witness used in the macro preflight."""

    identity = tuple(range(n))
    first_swap = transpose(identity, 0, 1)
    identity_outcome = evaluate_selectors(identity)[MIN_COVERAGE_LEX]
    swap_outcome = evaluate_selectors(first_swap)[MIN_COVERAGE_LEX]
    return {
        "n": n,
        "identity_state": identity_outcome.state,
        "identity_quadruple": (
            None
            if identity_outcome.selection is None
            else identity_outcome.selection.quadruple
        ),
        "first_swap_state": swap_outcome.state,
        "first_swap_maximizers": swap_outcome.n_maximizers,
        "expected_states_hold": (
            identity_outcome.state == STATE_UNIQUE
            and swap_outcome.state != STATE_UNIQUE
        ),
        "empirical_measure_atom_change_bound": 2 / n,
    }


def main() -> None:
    for n in SIZES:
        print(json.dumps(probe_size(n), sort_keys=True))
    for n in DETERMINISTIC_SEQUENCE_SIZES:
        print(json.dumps(probe_deterministic_sequence(n), sort_keys=True))


if __name__ == "__main__":
    main()
