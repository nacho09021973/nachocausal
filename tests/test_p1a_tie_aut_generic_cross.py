"""Bounded tests for the generic TIE/Aut core--padding surgery diagnostic."""

from __future__ import annotations

import pytest

from emergencia import p1a_tie_aut_diagnostic as tie_aut
from emergencia import p1a_tie_aut_generic_cross as generic_cross


def test_generic_realization_has_large_exact_twin_middle_class() -> None:
    core = tuple(range(7))
    realization = generic_cross.generic_cross_realization(core, 3)

    assert realization.low_index == 3
    assert len(realization.middle_indices) == 9
    assert realization.high_index == 16
    assert len(realization.permutation) == 17
    assert realization.permutation[realization.low_index] == 0
    assert realization.permutation[realization.high_index] == 13


def test_odd_chain_generic_coefficient_is_three() -> None:
    summary = generic_cross.generic_cross_repairability(tuple(range(7)))

    assert summary.a == 3
    assert summary.repairable_indices == (2, 3, 4)
    assert tuple(diagnostic.n_orbits for diagnostic in summary.diagnostics) == (
        2,
        2,
        1,
        1,
        1,
        2,
        2,
    )
    assert all(
        diagnostic.diagnostic_state == tie_aut.DIAGNOSTIC_UNIQUE
        for diagnostic in summary.diagnostics[2:5]
    )


def test_generic_boundary_exceptions_are_not_encoded_as_repairable() -> None:
    # With empty middle padding, x=1 and x=5 become TIE_AUT_ONLY for id_7.
    # D_x is explicitly the stable non-boundary surgery and keeps both bad.
    for core_index in (1, 5):
        diagnostic = generic_cross.generic_cross_diagnostic(
            tuple(range(7)), core_index
        )
        assert diagnostic.diagnostic_state == tie_aut.DIAGNOSTIC_TIE_NONAUT
        assert diagnostic.n_orbits == 2
        assert diagnostic.middle_size == 9


def test_exact_n8_zero_repairability_witness() -> None:
    core = (0, 1, 2, 4, 5, 7, 3, 6)
    summary = generic_cross.generic_cross_repairability(core)

    assert summary.a == 0
    assert summary.repairable_indices == ()
    assert tuple(diagnostic.n_orbits for diagnostic in summary.diagnostics) == (
        2,
        0,
        0,
        0,
        0,
        2,
        2,
        2,
    )


def test_generic_diagnostic_rejects_a_good_core() -> None:
    with pytest.raises(ValueError, match="TIE_NONAUT core"):
        generic_cross.generic_cross_diagnostic(tuple(range(6)), 0)


def test_generic_diagnostic_rejects_invalid_core_index() -> None:
    with pytest.raises(ValueError, match="outside the core"):
        generic_cross.generic_cross_realization(tuple(range(7)), 7)
