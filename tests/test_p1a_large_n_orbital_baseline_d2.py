"""Bounded guards for the post-hoc large-n orbital baseline runner."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import pytest

from emergencia import p1a_large_n_orbital_baseline_d2 as baseline
from emergencia import p1a_orbital_backend_preflight_d2 as orbital


def test_design_constants_and_seeds_are_frozen() -> None:
    assert baseline.MC_N == (10, 12, 16, 24, 32)
    assert baseline.N_MC == 100_000
    assert [baseline.scientific_seed(n) for n in baseline.MC_N] == [
        260_826_010,
        260_826_012,
        260_826_016,
        260_826_024,
        260_826_032,
    ]
    assert baseline.ENGINEERING_GATE_N == (24, 32)
    assert baseline.ENGINEERING_GATE_INSTANCES == 100
    assert baseline.ENGINEERING_GATE_P95_MAX_S == 0.25


def test_validated_wrapper_is_still_byte_identical() -> None:
    validation = baseline.validate_sources()
    assert validation["wrapper_byte_identical"] is True
    assert validation["wrapper_current_sha256"] == validation["wrapper_validated_sha256"]


def test_exact_n6_control_reproduces_frozen_counts() -> None:
    raw = baseline._accumulate(
        6,
        __import__("itertools").permutations(range(6)),
        method="EXACT",
        replicates=math.factorial(6),
        seed=None,
        timeout_s=None,
    )
    assert (raw.empty, raw.orbital_unique, raw.orbital_nonunique) == (719, 1, 0)


def test_summary_keeps_exact_and_wilson_intervals_distinct() -> None:
    exact = baseline.RawCounts(6, "EXACT", 720, None, 719, 1, 0, 0, (0.001,) * 720)
    mc = baseline.RawCounts(10, "MONTE_CARLO", 100, 1, 80, 15, 5, 0, (0.001,) * 100)
    exact_row = baseline.summarize(exact)
    mc_row = baseline.summarize(mc)
    assert exact_row["interval_method"] == "EXACT_POINT"
    assert exact_row["U_ci95_low"] == exact_row["U_hat"] == exact_row["U_ci95_high"]
    assert mc_row["interval_method"] == "WILSON_95"
    assert float(mc_row["U_ci95_low"]) < float(mc_row["U_hat"]) < float(mc_row["U_ci95_high"])


def test_backend_failure_aborts_without_imputation(monkeypatch: pytest.MonkeyPatch) -> None:
    failure = orbital.BackendResult(
        status=orbital.STATUS_BACKEND_FAILURE,
        n_maximizers=0,
        n_orbits_on_m=None,
        n_automorphisms=None,
        automorphism_enumeration_complete=False,
        maximizers=(),
        orbits=None,
        error_type="SyntheticFailure",
        error_message="forced",
    )
    monkeypatch.setattr(orbital, "evaluate_orbital_backend", lambda *args, **kwargs: failure)
    with pytest.raises(RuntimeError, match="BACKEND_FAILURE"):
        baseline._accumulate(
            10,
            [(tuple(range(10)))],
            method="MONTE_CARLO",
            replicates=1,
            seed=1,
            timeout_s=1,
        )


def test_committed_large_n_artifacts_are_sealed_and_guarded() -> None:
    for filename in (baseline.CSV_FILENAME, baseline.JSON_FILENAME):
        path = baseline.RESULTS_DIR / filename
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert path.with_suffix(path.suffix + ".sha256").read_text() == (
            f"{digest}  {path.name}\n"
        )
    payload = json.loads((baseline.RESULTS_DIR / baseline.JSON_FILENAME).read_text())
    assert payload["result_status"] == "LARGE_N_BASELINE_COMPLETED"
    assert payload["design"]["mc_n_authorized"] == list(baseline.MC_N)
    assert payload["controls"] == {
        "BACKEND_FAILURES": "0",
        "COUNTS_SUM_TO_NMC": "PASS",
        "EXACT_BASELINE_REPRODUCTION": "PASS",
        "U_LE_E": "PASS",
        "U_STAR_EQUALS_U_OVER_E": "PASS",
    }
    assert payload["provenance"]["runner_sha256"] == hashlib.sha256(
        Path(baseline.__file__).read_bytes()
    ).hexdigest()
