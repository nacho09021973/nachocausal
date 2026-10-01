"""Bounded guards for the independent orbital-curve refinement campaign."""

from __future__ import annotations

import csv
import json

import pytest

from emergencia import p1a_large_n_orbital_baseline_d2 as baseline
from emergencia import p1a_orbital_backend_preflight_d2 as orbital
from emergencia import p1a_orbital_curve_refinement_d2 as refinement


def test_design_is_frozen_before_execution() -> None:
    assert refinement.N_VALUES == (20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40)
    assert refinement.N_MC == 100_000
    assert refinement.PARALLEL_WORKERS == 4
    assert refinement.ENGINEERING_GATE_N == (36, 40)
    assert refinement.ENGINEERING_GATE_P95_MAX_S == 0.25
    assert [refinement.scientific_seed(n) for n in refinement.N_VALUES] == [
        260_828_000 + n for n in refinement.N_VALUES
    ]


def test_sources_and_wrapper_are_still_sealed() -> None:
    validation = refinement.validate_sources()
    assert validation["wrapper_byte_identical"] is True


def test_summary_is_wilson_and_has_new_phase() -> None:
    raw = baseline.RawCounts(
        24, "MONTE_CARLO_REFINEMENT", 100, 260_828_024, 3, 47, 50, 0, (0.001,) * 100
    )
    row = refinement.summarize(raw)
    assert row["PHASE"] == refinement.PHASE
    assert row["interval_method"] == "WILSON_95"
    assert row["G_hat"] == "0.5"


def test_backend_failure_remains_fail_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    failure = orbital.BackendResult(
        orbital.STATUS_BACKEND_FAILURE, 0, None, None, False, (), None, "Forced", "failure"
    )
    monkeypatch.setattr(orbital, "evaluate_orbital_backend", lambda *args, **kwargs: failure)
    with pytest.raises(RuntimeError, match="BACKEND_FAILURE"):
        baseline._accumulate(
            20,
            [tuple(range(20))],
            method="MONTE_CARLO_REFINEMENT",
            replicates=1,
            seed=1,
            timeout_s=1,
        )


def test_trend_classifier_accepts_plateau_without_calling_it_nonmonotone() -> None:
    rows = [{"x": value} for value in (0.8, 0.9, 0.9)]
    assert refinement._trend(rows, "x") == "INCREASED"


def test_completed_artifacts_are_sealed_and_self_consistent() -> None:
    csv_path = refinement.RESULTS_DIR / refinement.CSV_FILENAME
    json_path = refinement.RESULTS_DIR / refinement.JSON_FILENAME
    baseline._verify_sidecar(csv_path)
    baseline._verify_sidecar(json_path)
    with csv_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    payload = json.loads(json_path.read_text(encoding="utf-8"))

    assert [int(row["n"]) for row in rows] == list(refinement.N_VALUES)
    assert all(row["PHASE"] == refinement.PHASE for row in rows)
    assert all(int(row["backend_failures"]) == 0 for row in rows)
    assert payload["result_status"] == "ORBITAL_CURVE_REFINEMENT_COMPLETED"
    assert payload["controls"]["BACKEND_FAILURES"] == "0"
    assert payload["observed_structure"]["E_hat"] == "INCREASED"
    assert payload["provenance"]["runner_sha256"] == refinement._sha256(
        refinement.Path(refinement.__file__)
    )
