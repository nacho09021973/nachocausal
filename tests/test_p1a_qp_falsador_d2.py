"""Bounded unit tests for the exact q_p coefficients and the frozen falsifier.

These run inside the lane authorized by
``emergencia/P1a_contrato_falsador_paso7_d2.md``: exact mask summation, no Monte
Carlo, no threshold, no choice of p.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations

from emergencia import p1a_paisaje_niveles_d2 as landscape
from emergencia import p1a_qp_falsador_d2 as falsifier
from emergencia import p1a_sup_exacto as sup_exact
from emergencia import p1a_tie_aut_diagnostic as tie_aut


def test_reranker_matches_the_authorized_induction_and_keeps_comparabilities() -> None:
    for permutation in ((0, 3, 1, 5, 2, 4), (2, 0, 4, 1, 5, 3)):
        falsifier.crosscheck_reranking(permutation)


def test_h1_holds_on_unavailable_permutations() -> None:
    checked = 0
    for permutation in permutations(range(7)):
        if landscape.score_landscape(permutation).n_candidates:
            continue
        falsifier.check_h1(permutation)
        checked += 1
        if checked == 25:
            break
    assert checked == 25


def test_controls_q0_zero_and_q1_equals_r_orb() -> None:
    for permutation in permutations(range(7)):
        result = landscape.score_landscape(permutation)
        if result.n_candidates == 0:
            continue
        a, b = falsifier.coefficients(permutation)
        diagnostic = tie_aut.evaluate_tie_aut(permutation)
        r_orb = int(
            diagnostic.diagnostic_state
            in (tie_aut.DIAGNOSTIC_UNIQUE, tie_aut.DIAGNOSTIC_TIE_AUT_ONLY)
        )
        assert a[0] == 0
        assert a[7] == r_orb
        assert all(a[k] == 0 and b[k] == 0 for k in range(6))
        assert all(0 <= a[k] <= b[k] for k in range(8))


def test_polynomial_matches_the_direct_mask_sum() -> None:
    for permutation in ((0, 1, 2, 3, 4, 5, 6), (0, 1, 2, 3, 5, 6, 4)):
        a, b = falsifier.coefficients(permutation)
        falsifier.check_polynomial_against_direct_sum(permutation, a, b)


def test_alpha_drops_exactly_the_tautological_top_coefficient() -> None:
    a, _ = falsifier.coefficients((0, 1, 2, 3, 4, 5, 6, 7))
    assert falsifier.alpha_of(a, 8) == (a[6], a[7])


def test_supremum_encloses_a_known_maximum() -> None:
    poly = sup_exact.bernstein_to_monomial([0] * 6 + [1, 0, 0, 0], 9)
    low, high = sup_exact.supremum_on_unit_interval(poly)
    exact = Fraction(2, 3) ** 6 * Fraction(1, 3) ** 3
    assert low <= exact <= high


def test_difference_polynomial_vanishes_at_both_endpoints() -> None:
    poly = sup_exact.bernstein_to_monomial([0, 0, 0, 0, 0, 0, 5, -3, 2, 0], 9)
    assert sup_exact.evaluate(poly, Fraction(0)) == 0
    assert sup_exact.evaluate(poly, Fraction(1)) == 0


def test_verdict_and_population_at_the_smallest_two_sizes() -> None:
    for n, expected_verdict, expected_population in ((6, "VACUOUS", 0), (7, "SUFFICIENT", 3)):
        report, _ = falsifier.run_size(n)
        falsifier.validate_report(report)
        for member in falsifier.MEMBERS:
            assert report[member]["verdict"] == expected_verdict
            assert report[member]["population_fibres"] == expected_population
