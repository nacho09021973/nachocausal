"""Tests for the EF-4 prescribed-family certificate in d=2."""

from __future__ import annotations

import math
from itertools import combinations, permutations

import pytest

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_entropia_fibras_ef4 as ef4


def test_even_prescription_is_an_injective_partial_permutation() -> None:
    n = 100_000
    rho = ef4.rho_for_n(n)
    prescribed = ef4.build_even_prescription(n)
    assert len(prescribed) == 2 * rho + 2
    assert len(set(prescribed)) == len(prescribed)
    assert len(set(prescribed.values())) == len(prescribed)
    assert prescribed[1] == 1
    assert prescribed[n // 2] == n // 2
    assert prescribed[n // 2 + 1] == n // 2 + 1
    assert prescribed[n] == n


def test_prescription_leaves_exactly_half_the_residual_on_each_side() -> None:
    for n in (100_000, 1_000_000, 10_000_000):
        assert ef4.validate_even_balance(n)
        bounds = ef4.certificate_bounds(n)
        assert bounds.free_count % 2 == 0


def test_invalid_or_colliding_prescriptions_are_refused() -> None:
    with pytest.raises(ValueError):
        ef4.build_even_prescription(99)
    with pytest.raises(ValueError):
        ef4.build_even_prescription(100, rho=25)


def test_incomparable_embedding_preserves_the_frozen_selector() -> None:
    for permutation in permutations(range(6)):
        embedded = ef4.append_incomparable(permutation)
        original = comparison.evaluate_selectors(permutation)[
            comparison.MIN_COVERAGE_LEX
        ]
        extended = comparison.evaluate_selectors(embedded)[
            comparison.MIN_COVERAGE_LEX
        ]
        assert extended.state == original.state
        assert extended.n_maximizers == original.n_maximizers
        assert extended.primary_score == original.primary_score
        assert extended.secondary_score == original.secondary_score
        if original.selection is None:
            assert extended.selection is None
        else:
            assert extended.selection is not None
            assert extended.selection.quadruple == original.selection.quadruple
            assert extended.selection.past_size == original.selection.past_size
            assert extended.selection.future_size == original.selection.future_size


def test_geometric_trichotomy_exhausts_all_abstract_n12_chains() -> None:
    n = 12
    rho = 2
    half = n // 2
    prescribed = ef4.build_even_prescription(n, rho=rho)
    prescribed_points = set(prescribed.items())
    free_rows = set(range(1, n + 1)) - set(prescribed)
    free_columns = set(range(1, n + 1)) - set(prescribed.values())
    free_count = len(free_rows)
    threshold = 1.0 / 8.0 + rho / free_count
    lower_stair = {
        point
        for point in prescribed_points
        if half - rho + 1 <= point[0] <= half - 1
    }
    upper_stair = {
        point
        for point in prescribed_points
        if half + 2 <= point[0] <= half + rho
    }

    def inside(
        point: tuple[int, int], lower: tuple[int, int], upper: tuple[int, int]
    ) -> bool:
        return (
            lower[0] <= point[0] <= upper[0]
            and lower[1] <= point[1] <= upper[1]
        )

    for rows in combinations(range(1, n + 1), 4):
        for columns in combinations(range(1, n + 1), 4):
            past_lower, past_upper, future_lower, future_upper = tuple(
                zip(rows, columns)
            )
            past_free_product = (
                sum(past_lower[0] <= row <= past_upper[0] for row in free_rows)
                * sum(
                    past_lower[1] <= column <= past_upper[1]
                    for column in free_columns
                )
                / free_count**2
            )
            future_free_product = (
                sum(
                    future_lower[0] <= row <= future_upper[0]
                    for row in free_rows
                )
                * sum(
                    future_lower[1] <= column <= future_upper[1]
                    for column in free_columns
                )
                / free_count**2
            )
            fixed_inner = past_upper == (half, half) and future_lower == (
                half + 1,
                half + 1,
            )
            small_product = (
                min(past_free_product, future_free_product) <= threshold
            )
            past_crosses = any(
                inside(point, past_lower, past_upper) for point in upper_stair
            )
            future_crosses = any(
                inside(point, future_lower, future_upper) for point in lower_stair
            )
            past_loses = not any(
                inside(point, past_lower, past_upper) for point in lower_stair
            )
            future_loses = not any(
                inside(point, future_lower, future_upper) for point in upper_stair
            )
            past_prescribed = sum(
                inside(point, past_lower, past_upper) for point in prescribed_points
            )
            future_prescribed = sum(
                inside(point, future_lower, future_upper)
                for point in prescribed_points
            )
            loss_case = not past_crosses and not future_crosses and (
                (
                    past_loses
                    and past_prescribed <= 3
                    and future_prescribed <= rho + 2
                )
                or (
                    future_loses
                    and future_prescribed <= 3
                    and past_prescribed <= rho + 2
                )
            )
            assert fixed_inner or small_product or loss_case


def test_loss_case_exact_envelope_dominates_a_dense_grid() -> None:
    bounds = ef4.certificate_bounds(1_000_000)
    assert ef4.validate_loss_optimization(bounds, grid_size=100_000)


def test_fixed_margins_enter_the_proved_asymptotic_regime() -> None:
    early = ef4.certificate_bounds(100_000)
    late = ef4.certificate_bounds(10_000_000)
    assert not early.uniqueness_margin_positive
    assert late.uniqueness_margin_positive
    assert late.loss_gap > 2 * late.discrepancy_radius
    assert late.small_product_gap > 2 * late.discrepancy_radius


def test_prescription_cost_is_subexponential_on_log_scale() -> None:
    ratios = [
        ef4.entropy_log_upper_bound(n) / n
        for n in (10**8, 10**10, 10**12)
    ]
    assert ratios[0] > ratios[1] > ratios[2] > 0.0
    asymptotic_scales = [
        ef4.entropy_log_upper_bound(n)
        / (n ** (2.0 / 3.0) * math.log(n) ** (4.0 / 3.0))
        for n in (10**8, 10**10, 10**12)
    ]
    assert all(1.9 < ratio < 2.1 for ratio in asymptotic_scales)


def test_loss_gap_has_the_declared_rho_over_two_scale() -> None:
    ratios = []
    for n in (10**8, 10**10, 10**12):
        bounds = ef4.certificate_bounds(n)
        ratios.append(bounds.loss_gap / bounds.rho)
    assert all(0.45 < ratio < 0.51 for ratio in ratios)
    assert ratios[0] < ratios[1] < ratios[2]
