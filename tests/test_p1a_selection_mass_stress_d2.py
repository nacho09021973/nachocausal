"""Tests for the preregistered Piece B selection-mass stress script."""

from __future__ import annotations

from emergencia import p1a_selection_mass_stress_d2 as stress


def test_contract_constants_are_frozen() -> None:
    assert stress.STRESS_N == (192, 256, 384, 512)
    assert stress.STRESS_BATCHES == 8
    assert stress.STRESS_REPLICATES_PER_N == {
        192: 12_000,
        256: 12_000,
        384: 4_000,
        512: 4_000,
    }
    assert stress.STRESS_BOOTSTRAP_REPLICATES == 10_000
    assert stress.FLOOR == 0.38
    assert stress.BAND_LOW == 0.15
    assert stress.BAND_HIGH == 0.41


def test_selection_trend_is_exhaustive_and_does_not_punish_rising() -> None:
    assert (
        stress.selection_trend(
            {192: (0.40, 0.50), 384: (0.22, 0.30), 512: (0.10, 0.20)}
        )
        == "DECAYING"
    )
    assert (
        stress.selection_trend(
            {192: (0.10, 0.20), 384: (0.30, 0.40), 512: (0.50, 0.60)}
        )
        == "RISING"
    )
    assert (
        stress.selection_trend(
            {192: (0.10, 0.50), 384: (0.30, 0.60), 512: (0.40, 0.70)}
        )
        == "STABILISING"
    )
    assert (
        stress.selection_trend(
            {192: (0.10, 0.30), 384: (0.40, 0.50), 512: (0.20, 0.35)}
        )
        == "INDETERMINATE"
    )


def test_recommendation_requires_completed_terminal() -> None:
    assert (
        stress.recommendation("STRESS_B_BLOCKED", "MET", "RISING", "BOUNDED_CONSISTENT")
        == "UNDECIDED"
    )
    assert (
        stress.recommendation("STRESS_B_COMPLETED", "MET", "RISING", "BOUNDED_CONSISTENT")
        == "YES"
    )


def test_seed_preflight_failure_emits_blocked_terminal(monkeypatch, capsys) -> None:
    def fail_seed_preflight():
        raise AssertionError("forced seed collision")

    monkeypatch.setattr(stress, "preflight_seeds", fail_seed_preflight)

    assert stress.main() == 1
    output = capsys.readouterr().out
    assert "PREFLIGHTS = FAIL" in output
    assert "STRESS_B_TERMINAL              = STRESS_B_BLOCKED" in output
    assert "STRESS_B_SIZES_COMPLETED       = []" in output
    assert "forced seed collision" in output


def test_threshold_preflight_failure_emits_blocked_terminal(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        stress,
        "preflight_seeds",
        lambda: {
            "emitted": 40,
            "historical": 100,
            "max_historical": 1,
            "min_emitted": 2,
            "guard": 1,
        },
    )

    def fail_threshold_preflight():
        raise AssertionError("forced threshold mismatch")

    monkeypatch.setattr(stress, "preflight_thresholds", fail_threshold_preflight)

    assert stress.main() == 1
    output = capsys.readouterr().out
    assert "PREFLIGHTS = FAIL" in output
    assert "STRESS_B_TERMINAL              = STRESS_B_BLOCKED" in output
    assert "forced threshold mismatch" in output
