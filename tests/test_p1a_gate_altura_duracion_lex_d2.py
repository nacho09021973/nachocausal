"""Tests for the frozen MIN_COVERAGE_LEX height-duration gate in d=2."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_gate_altura_duracion_lex_d2 as gate


_ROOT = Path(__file__).resolve().parent.parent
_RESULTS = _ROOT / "emergencia" / "resultados"


def test_contract_constants_are_frozen() -> None:
    assert gate.BASE_N == (64, 96, 128)
    assert gate.BASE_REPLICATES_PER_N == 12_000
    assert gate.BASE_BATCHES == 8
    assert gate.BASE_REPLICATES_PER_BATCH == 1_500
    assert gate.RETENTION == (0.90, 0.80)
    assert gate.COORDINATE_SEED_BASE == 2_608_040_000
    assert gate.THINNING_SEED_BASE == 2_608_041_000
    assert gate.BASELINE_SEED_BASE == 2_608_042_000
    assert gate.BOOTSTRAP_SEED_BASE == 2_608_043_000
    assert gate.BASELINE_REPLICATES_PER_SIZE == 4_000
    assert gate.BOOTSTRAP_REPLICATES == 1_000


def test_latent_duration_uses_frozen_null_metric() -> None:
    duration = gate.latent_duration([0.1, 0.5], [0.2, 0.8], 0, 1)
    assert math.isclose(duration, math.sqrt(0.4 * 0.6))


def test_height_duration_estimate_is_not_fitted() -> None:
    assert gate.height_duration_estimate(8, 64) == 0.5
    assert gate.height_duration_estimate(12, 144) == 0.5


def test_selected_wrapper_uses_frozen_lex_selector() -> None:
    permutation = tuple(range(6))
    expected = comparison.evaluate_selectors(permutation)[
        comparison.MIN_COVERAGE_LEX
    ].selection
    assert gate._selected_lex(permutation) == expected
    assert gate._selected_lex(tuple(range(7))) is None


def test_fixed_size_baseline_has_exact_m3_height(monkeypatch) -> None:
    monkeypatch.setattr(gate, "BASELINE_REPLICATES_PER_SIZE", 20)
    assert gate.simulate_baselines((3,)) == {3: [3] * 20}


def test_pearson_controls() -> None:
    x = np.array([1.0, 2.0, 4.0, 8.0])
    assert math.isclose(gate.pearson_correlation(x, 3.0 * x + 2.0), 1.0)
    assert math.isclose(gate.pearson_correlation(x, -2.0 * x), -1.0)


def test_bootstrap_is_reproducible_and_bounded(monkeypatch) -> None:
    monkeypatch.setattr(gate, "BOOTSTRAP_REPLICATES", 50)
    residuals = np.linspace(-0.2, 0.2, 30)
    relative = np.linspace(0.05, 0.20, 30)
    latent = np.linspace(0.1, 0.8, 30)
    estimated = latent + np.linspace(-0.02, 0.02, 30)
    first = gate.bootstrap_metrics(
        residuals, relative, estimated, latent, n=64, side=gate.PAST
    )
    second = gate.bootstrap_metrics(
        residuals, relative, estimated, latent, n=64, side=gate.PAST
    )
    assert first == second
    assert -1.0 <= first["pearson_bootstrap95_low"] <= 1.0
    assert -1.0 <= first["pearson_bootstrap95_high"] <= 1.0


def test_small_base_simulation_is_reproducible(monkeypatch) -> None:
    monkeypatch.setattr(gate, "BASE_N", (64,))
    monkeypatch.setattr(gate, "BASE_BATCHES", 1)
    monkeypatch.setattr(gate, "BASE_REPLICATES_PER_BATCH", 20)
    monkeypatch.setattr(gate, "BASE_REPLICATES_PER_N", 20)
    first = gate.simulate_base()
    second = gate.simulate_base()
    assert first == second


def _synthetic_rows(mode: str):
    calibration = []
    thinning = []
    for n in gate.BASE_N:
        for side in gate.SIDES:
            if mode == "pass":
                correlation_low, correlation_high = 0.85, 0.92
                relative_low, relative_high = 0.10, 0.20
            elif mode == "park":
                correlation_low, correlation_high = 0.20, 0.40
                relative_low, relative_high = 0.60, 0.70
            else:
                correlation_low, correlation_high = 0.75, 0.85
                relative_low, relative_high = 0.20, 0.35
            calibration.append(
                {
                    "n": n,
                    "side": side,
                    "height_residual_mean": 0.0,
                    "height_residual_bootstrap95_low": -0.1,
                    "height_residual_bootstrap95_high": 0.1,
                    "pearson_correlation": (correlation_low + correlation_high) / 2,
                    "pearson_bootstrap95_low": correlation_low,
                    "pearson_bootstrap95_high": correlation_high,
                    "median_absolute_relative_error": (
                        relative_low + relative_high
                    )
                    / 2,
                    "median_are_bootstrap95_low": relative_low,
                    "median_are_bootstrap95_high": relative_high,
                }
            )
        for retention in gate.RETENTION:
            thinning.append(
                {
                    "n": n,
                    "retention": retention,
                    "p_target_within_25": 0.70,
                    "p_target_within_25_ci95_low": 0.65,
                }
            )
    return calibration, thinning


def test_scientific_terminals() -> None:
    calibration, thinning = _synthetic_rows("pass")
    terminal, _ = gate.scientific_terminal(calibration, thinning)
    assert terminal == gate.TERMINAL_PASS

    calibration, thinning = _synthetic_rows("park")
    terminal, _ = gate.scientific_terminal(calibration, thinning)
    assert terminal == gate.TERMINAL_PARK

    calibration, thinning = _synthetic_rows("inconclusive")
    terminal, _ = gate.scientific_terminal(calibration, thinning)
    assert terminal == gate.TERMINAL_INCONCLUSIVE


def test_contract_explicitly_excludes_height_ratio() -> None:
    contract = gate.contract_dict()
    assert contract["selector"] == comparison.MIN_COVERAGE_LEX
    assert contract["fixed_n_channel"] is True
    assert contract["height_ratio_computed"] is False


def test_generated_artifacts_match_frozen_hashes_and_use_lf() -> None:
    expected = {
        "p1a_lex_intervalos_d2.csv": (
            "4db6001ceba4716696bc4ac63e36452863675408fd88a632b65a2d561dce85ba"
        ),
        "p1a_lex_altura_calibracion_d2.csv": (
            "bb1e38d8c99fdcbfae8aed329aad3c7d19f130058f600b45e0bc7e6f5aaee018"
        ),
        "p1a_lex_altura_baseline_por_tamano_d2.csv": (
            "bf41a0ba47462994b47889606e3e82c7611748fc00eef13509b993d099738f56"
        ),
        "p1a_lex_target_thinning_d2.csv": (
            "f7062580b90224ac2e0c936fb38b066fbead907f5ac6b11202c2b8b5aeb65ae5"
        ),
        "p1a_lex_altura_duracion_resumen.json": (
            "395d3aba30948cfc0211aa752cac5836a4731494f306a0e87a7e1651b12fa49d"
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


def test_result_parks_height_representation_without_computing_ratio() -> None:
    summary = json.loads((_RESULTS / gate.SUMMARY_FILENAME).read_text())
    assert summary["contract_status"] == "FROZEN_BEFORE_RESULTS"
    assert summary["terminal"] == gate.TERMINAL_PARK
    assert summary["contract"]["height_ratio_computed"] is False
    assert all(
        record["strong_failure_n"] and not record["pass_n"]
        for record in summary["gate"].values()
    )
    assert all(
        side["height_pass"]
        and side["relative_error_pass"]
        and not side["correlation_pass"]
        and side["strong_failure"]
        for record in summary["gate"].values()
        for side in record["sides"].values()
    )
