"""Tests for two alternative MIN_COVERAGE_LEX duration representations."""

from __future__ import annotations

import hashlib
import json
import math
from itertools import combinations, permutations
from pathlib import Path

import numpy as np

from emergencia import p1a_representaciones_alternativas_d2 as alternatives


_ROOT = Path(__file__).resolve().parent.parent
_RESULTS = _ROOT / "emergencia" / "resultados"


def naive_width(permutation: tuple[int, ...]) -> int:
    n = len(permutation)
    best = 0
    for size in range(1, n + 1):
        for indices in combinations(range(n), size):
            if all(
                permutation[i] > permutation[j]
                for i, j in combinations(indices, 2)
            ):
                best = size
    return best


def test_contract_constants_are_frozen() -> None:
    assert alternatives.REPRESENTATIONS == (
        alternatives.HEIGHT_ONLY,
        alternatives.COUNT_VOLUME,
        alternatives.HEIGHT_WIDTH,
    )
    assert alternatives.CANDIDATES == (
        alternatives.COUNT_VOLUME,
        alternatives.HEIGHT_WIDTH,
    )
    assert alternatives.BASE_N == (64, 96, 128)
    assert alternatives.BASE_REPLICATES_PER_N == 12_000
    assert alternatives.COORDINATE_SEED_BASE == 2_608_044_000
    assert alternatives.BOOTSTRAP_SEED_BASE == 2_608_045_000
    assert alternatives.BOOTSTRAP_REPLICATES == 1_000


def test_count_volume_exact_cases() -> None:
    assert alternatives.estimate_count_volume(18, 66) == 0.5
    assert alternatives.estimate_count_volume(3, 6) == 0.5
    assert alternatives.estimate_count_volume(10, 10) == 1.0


def test_width_matches_naive_antichain_enumeration_through_n6() -> None:
    for n in range(1, 7):
        for permutation in permutations(range(n)):
            assert alternatives.width_from_permutation(permutation) == naive_width(
                permutation
            )


def test_chain_and_antichain_width_controls() -> None:
    assert alternatives.width_from_permutation(tuple(range(8))) == 1
    assert alternatives.width_from_permutation(tuple(reversed(range(8)))) == 8


def test_interval_height_width_control() -> None:
    height, width, size = alternatives.interval_height_width(
        (0, 2, 1, 4, 3, 5), 0, 5
    )
    assert (height, width, size) == (4, 2, 6)


def test_height_width_formula_is_not_fitted() -> None:
    assert alternatives.estimate_height_width(6, 2, 64) == 0.25
    assert alternatives.estimate_height_width(10, 6, 64) == 0.5


def test_small_simulation_is_reproducible(monkeypatch) -> None:
    monkeypatch.setattr(alternatives, "BASE_N", (64,))
    monkeypatch.setattr(alternatives, "BASE_BATCHES", 1)
    monkeypatch.setattr(alternatives, "BASE_REPLICATES_PER_BATCH", 20)
    monkeypatch.setattr(alternatives, "BASE_REPLICATES_PER_N", 20)
    assert alternatives.simulate_base() == alternatives.simulate_base()


def test_bootstrap_is_reproducible(monkeypatch) -> None:
    monkeypatch.setattr(alternatives, "BOOTSTRAP_REPLICATES", 40)
    latent = np.linspace(0.2, 0.8, 30)
    estimate = latent + np.linspace(-0.02, 0.02, 30)
    errors = estimate - latent
    relative = np.abs(errors) / latent
    first = alternatives.bootstrap_metrics(
        estimate,
        latent,
        errors,
        relative,
        representation=alternatives.COUNT_VOLUME,
        n=64,
        side=alternatives.PAST,
    )
    second = alternatives.bootstrap_metrics(
        estimate,
        latent,
        errors,
        relative,
        representation=alternatives.COUNT_VOLUME,
        n=64,
        side=alternatives.PAST,
    )
    assert first == second
    assert -1 <= first["pearson_bootstrap95_low"] <= 1
    assert -1 <= first["pearson_bootstrap95_high"] <= 1


def synthetic_metrics(count_mode: str, width_mode: str):
    rows = []
    for representation, mode in (
        (alternatives.COUNT_VOLUME, count_mode),
        (alternatives.HEIGHT_WIDTH, width_mode),
    ):
        for n in alternatives.BASE_N:
            for side in alternatives.SIDES:
                if mode == "pass":
                    corr_low, corr_high = 0.85, 0.92
                    rel_low, rel_high = 0.10, 0.20
                    bias_low, bias_high = -0.01, 0.01
                elif mode == "strong":
                    corr_low, corr_high = 0.20, 0.40
                    rel_low, rel_high = 0.60, 0.70
                    bias_low, bias_high = -0.01, 0.01
                else:
                    corr_low, corr_high = 0.55, 0.65
                    rel_low, rel_high = 0.10, 0.20
                    bias_low, bias_high = -0.01, 0.01
                rows.append(
                    {
                        "representation": representation,
                        "n": n,
                        "side": side,
                        "bias_mean": 0.0,
                        "bias_bootstrap95_low": bias_low,
                        "bias_bootstrap95_high": bias_high,
                        "median_absolute_relative_error": (rel_low + rel_high) / 2,
                        "median_are_bootstrap95_low": rel_low,
                        "median_are_bootstrap95_high": rel_high,
                        "pearson_correlation": (corr_low + corr_high) / 2,
                        "pearson_bootstrap95_low": corr_low,
                        "pearson_bootstrap95_high": corr_high,
                    }
                )
    return rows


def test_scientific_terminal_priority_and_fallbacks() -> None:
    terminal, _ = alternatives.scientific_terminal(
        synthetic_metrics("pass", "pass")
    )
    assert terminal == alternatives.TERMINAL_SELECT_COUNT

    terminal, _ = alternatives.scientific_terminal(
        synthetic_metrics("open", "pass")
    )
    assert terminal == alternatives.TERMINAL_SELECT_HEIGHT_WIDTH

    terminal, _ = alternatives.scientific_terminal(
        synthetic_metrics("strong", "strong")
    )
    assert terminal == alternatives.TERMINAL_PARK_BOTH

    terminal, _ = alternatives.scientific_terminal(
        synthetic_metrics("open", "strong")
    )
    assert terminal == alternatives.TERMINAL_INCONCLUSIVE


def test_contract_excludes_ratios_and_physical_poisson_scale() -> None:
    contract = alternatives.contract_dict()
    assert contract["fixed_n_channel"] is True
    assert contract["ratio_computed"] is False
    assert contract["count_volume_formula"] == "sqrt((m-2)/(n-2))"
    assert contract["height_width_formula"] == "(H+W)/(4*sqrt(n))"


def test_generated_artifacts_match_frozen_hashes_and_use_lf() -> None:
    expected = {
        "p1a_representaciones_intervalos_d2.csv": (
            "5110688b89142bf06e738a6f66bb41fa7c248e29352392b8bc763480ebd3ab08"
        ),
        "p1a_representaciones_metricas_d2.csv": (
            "4d98f014612af57212190a86e91f3445a111289cd55b66cca1adbde827e48cec"
        ),
        "p1a_representaciones_resumen.json": (
            "7176a3a6e55cf309911a636592780880c55574773d398a9a620a1536ea7899dc"
        ),
    }
    for filename, digest in expected.items():
        path = _RESULTS / filename
        data = path.read_bytes()
        assert b"\r" not in data
        assert hashlib.sha256(data).hexdigest() == digest
        assert path.with_suffix(path.suffix + ".sha256").read_text() == (
            f"{digest}  {filename}\n"
        )


def test_result_parks_height_width_but_leaves_count_volume_open() -> None:
    summary = json.loads((_RESULTS / alternatives.SUMMARY_FILENAME).read_text())
    assert summary["contract_status"] == "FROZEN_BEFORE_RESULTS"
    assert summary["terminal"] == alternatives.TERMINAL_INCONCLUSIVE
    assert summary["contract"]["ratio_computed"] is False
    count = summary["gate"][alternatives.COUNT_VOLUME]
    height_width = summary["gate"][alternatives.HEIGHT_WIDTH]
    assert count["qualifies_all_n"] is False
    assert count["strongly_parked_all_n"] is False
    assert height_width["qualifies_all_n"] is False
    assert height_width["strongly_parked_all_n"] is True
