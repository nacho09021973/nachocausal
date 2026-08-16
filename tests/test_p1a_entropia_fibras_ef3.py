"""Tests for the EF-3 COUNT_VOLUME fiber reduction in d=2."""

from __future__ import annotations

import math
from itertools import permutations

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_entropia_fibras_ef3 as ef3


def test_tableau_recurrence_matches_hook_length_formula() -> None:
    for n in range(1, 13):
        for shape in ef3.integer_partitions(n, ef3.LIS_THRESHOLD - 1):
            assert ef3.standard_tableaux_count(shape) == ef3.hook_length_tableaux_count(
                shape
            )


def test_rsk_empty_recurrence_matches_frozen_ef2_counts() -> None:
    state_counts = ef3.load_state_counts()
    assert [ef3.empty_count_rsk(n) for n in ef3.EXACT_N] == [
        719,
        5003,
        39429,
        344837,
    ]
    for n in ef3.EXACT_N:
        assert ef3.empty_count_rsk(n) == state_counts[n][comparison.STATE_EMPTY]


def test_candidate_exists_if_and_only_if_lis_is_at_least_six() -> None:
    for n in (6, 7):
        for permutation in permutations(range(n)):
            outcome = comparison.evaluate_selectors(permutation)[
                comparison.MIN_COVERAGE_LEX
            ]
            assert (outcome.state != comparison.STATE_EMPTY) == (
                ef3.lis_length(permutation) >= ef3.LIS_THRESHOLD
            )


def test_closed_rectangle_normalization_correction_is_uniform() -> None:
    for n in range(2, 50):
        for k in range(n):
            for l in range(n):
                correction = ef3.closed_rectangle_correction(n, k, l)
                assert 0.0 <= correction <= 4.0 / n


def test_exact_q2_reproduces_side_symmetry_and_projection_bound() -> None:
    state_counts = ef3.load_state_counts()
    summaries = ef3.exact_moment_summaries(ef3.load_c_rows())
    for n in ef3.EXACT_N:
        past = summaries[(n, "PAST")]
        future = summaries[(n, "FUTURE")]
        assert past.unique_count == state_counts[n][comparison.STATE_UNIQUE]
        assert past.unique_count == future.unique_count
        assert math.isclose(past.q2, future.q2, rel_tol=0.0, abs_tol=1e-15)
        assert 0.0 <= past.q2 <= past.rectangle_proxy_mse


def test_discrepancy_bound_has_the_declared_conditioning_cost() -> None:
    n = 10_000
    epsilon = 0.1
    polynomial_probability = n ** -3
    subexponential_probability = math.exp(-math.sqrt(n))
    assert ef3.discrepancy_tail_bound(n, epsilon) < polynomial_probability
    assert ef3.conditional_q2_bound(n, polynomial_probability, epsilon) < 0.11
    assert ef3.conditional_q2_bound(n, subexponential_probability, epsilon) < 0.11


def test_full_frozen_verifier_passes() -> None:
    summaries = ef3.verify_frozen_ef2()
    assert set(summaries) == {
        (n, side) for n in ef3.EXACT_N for side in ef3.SIDES
    }
