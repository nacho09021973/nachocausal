"""Guards for the exact post-hoc exploratory thinning macrotest."""

from __future__ import annotations

from fractions import Fraction

from emergencia import p1a_macrotest_exploratorio_d2 as macrotest


def test_fixed_grid_was_not_adapted() -> None:
    assert macrotest.P_GRID == (Fraction(0),) + tuple(
        Fraction(i, 20) for i in range(2, 21)
    )


def test_exact_controls_and_projective_consistency() -> None:
    analysis = macrotest.analyze()
    assert set(analysis.controls.values()) == {"PASS"}
    for n in macrotest.EXACT_N:
        for k in range(n + 1):
            assert analysis.nk_exact[n, k][:2] == analysis.baseline[k][:2]


def test_tie_aut_only_is_included_in_frozen_orbital_counts() -> None:
    analysis = macrotest.analyze()
    # S_7 has 32 literal UNIQUE plus 4 TIE_AUT_ONLY cases: 36/7! = 1/140.
    assert analysis.baseline[7][0] == Fraction(36, 5040) == Fraction(1, 140)
    assert analysis.baseline[7][1] == Fraction(37, 5040)


def test_na_is_not_encoded_as_zero() -> None:
    analysis = macrotest.analyze()
    p0 = next(row for row in analysis.np_rows if row["n"] == 6 and row["p"] == "0.00")
    assert p0["PHASE"] == macrotest.PHASE
    assert p0["U_orbital"] == "0"
    assert p0["E_available"] == "0"
    assert p0["U_orbital_given_available"] == "NA"
