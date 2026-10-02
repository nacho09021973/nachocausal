"""Guards for the frozen post-hoc orbital-multiplicity campaign."""

from __future__ import annotations

import csv
import json
import math
from collections import Counter

import pytest

from emergencia import p1a_large_n_orbital_baseline_d2 as baseline
from emergencia import p1a_orbital_backend_preflight_d2 as orbital
from emergencia import p1a_orbital_multiplicity_d2 as multiplicity
from emergencia import p1a_orbital_curve_refinement_d2 as refinement


def test_design_is_frozen_before_execution() -> None:
    assert multiplicity.PHASE == "POST_HOC_EXPLORATORY_ORBITAL_MULTIPLICITY"
    assert multiplicity.EXACT_N == (6, 7, 8, 9)
    assert multiplicity.N_VALUES == tuple(range(20, 41, 2))
    assert multiplicity.N_MC == 100_000
    assert multiplicity.SCIENTIFIC_SEED_BASE == 260_828_000
    assert multiplicity.QUANTILES == (0.50, 0.75, 0.90, 0.95, 0.99)
    assert multiplicity.QUANTILE_METHOD == "inverted_cdf"
    assert multiplicity.BOOTSTRAP_REPLICATES == 1_000
    assert multiplicity.BOOTSTRAP_SEED_BASE == 2_608_275_000


def test_sources_and_backend_wrapper_are_still_sealed() -> None:
    validation = multiplicity.validate_sources()
    assert validation["backend_wrapper_byte_identical"] is True


def test_backend_exposes_certified_exact_r_not_only_binary_status() -> None:
    unique = orbital.evaluate_orbital_backend(tuple(range(6)), complete_orbits=False)
    binary_tie = orbital.evaluate_orbital_backend(tuple(range(7)), complete_orbits=False)
    assert unique.status == orbital.STATUS_ORBITAL_UNIQUE
    assert unique.n_orbits_on_m == 1
    assert binary_tie.status == orbital.STATUS_ORBITAL_NONUNIQUE
    assert binary_tie.n_orbits_on_m == 2


def test_empty_is_separate_from_conditional_r_distribution() -> None:
    raw = multiplicity.RawMultiplicity(
        n=6,
        method="EXACT",
        total=10,
        seed=None,
        empty=4,
        r_counts=((1, 3), (2, 2), (5, 1)),
        backend_failures=0,
        median_time_ms=0.0,
        p95_time_ms=0.0,
    )
    assert raw.nonempty == 6
    assert raw.ties == 3
    assert 0 not in raw.counter


def test_inverted_cdf_quantiles_use_observed_integer_support() -> None:
    counts = Counter({1: 4, 2: 3, 7: 2, 20: 1})
    assert multiplicity._count_quantile(counts, 0.50) == 2
    assert multiplicity._count_quantile(counts, 0.75) == 7
    assert multiplicity._count_quantile(counts, 0.90) == 7
    assert multiplicity._count_quantile(counts, 0.95) == 20
    assert multiplicity._count_quantile(counts, 0.99) == 20


def test_multinomial_percentile_bootstrap_is_reproducible() -> None:
    counts = Counter({1: 70, 2: 20, 3: 7, 6: 3})
    first = multiplicity.bootstrap_distribution(counts, seed=123, replicates=50)
    second = multiplicity.bootstrap_distribution(counts, seed=123, replicates=50)
    assert first == second
    assert set(first) == {"mean_log", "entropy", "q50", "q75", "q90", "q95", "q99"}
    assert first["mean_log"][0] <= first["mean_log"][1]
    assert first["entropy"][0] <= first["entropy"][1]


def test_summary_obeys_direct_log_and_shannon_identities(monkeypatch) -> None:
    raw = multiplicity.RawMultiplicity(
        n=20,
        method="MONTE_CARLO_REPRODUCTION",
        total=100,
        seed=multiplicity.scientific_seed(20),
        empty=10,
        r_counts=((1, 45), (2, 30), (3, 10), (5, 5)),
        backend_failures=0,
        median_time_ms=1.0,
        p95_time_ms=2.0,
    )
    monkeypatch.setattr(multiplicity, "BOOTSTRAP_REPLICATES", 30)
    row = multiplicity.summarize(raw)
    direct = (30 * math.log(2) + 10 * math.log(3) + 5 * math.log(5)) / 90
    assert math.isclose(float(row["Sbar_n"]), direct, abs_tol=1e-15)
    assert math.isclose(float(row["U_n_star"]), 0.5, abs_tol=1e-15)
    assert abs(float(row["shannon_decomposition_residual"])) <= 1e-12
    assert float(row["Sbar_n_tie"]) >= math.log(2)


def test_long_distribution_keeps_zero_count_gaps_and_tail() -> None:
    raw = multiplicity.RawMultiplicity(
        n=7,
        method="EXACT",
        total=6,
        seed=None,
        empty=1,
        r_counts=((1, 3), (3, 1), (5, 1)),
        backend_failures=0,
        median_time_ms=0.0,
        p95_time_ms=0.0,
    )
    rows = multiplicity.distribution_rows(raw)
    assert [row["r"] for row in rows] == [1, 2, 3, 4, 5]
    assert [row["count"] for row in rows] == [3, 0, 1, 0, 1]
    assert rows[-1]["q_given_tie"] == "0.5"


def test_backend_failure_aborts_without_classifying(monkeypatch: pytest.MonkeyPatch) -> None:
    failure = orbital.BackendResult(
        orbital.STATUS_BACKEND_FAILURE,
        0,
        None,
        None,
        False,
        (),
        None,
        "Forced",
        "failure",
    )
    monkeypatch.setattr(orbital, "evaluate_orbital_backend", lambda *args, **kwargs: failure)
    with pytest.raises(RuntimeError, match="BACKEND_FAILURE"):
        multiplicity.accumulate(
            6,
            [tuple(range(6))],
            method="TEST",
            total=1,
            seed=None,
            timeout_s=1.0,
        )


@pytest.mark.skipif(
    not (multiplicity.RESULTS_DIR / multiplicity.JSON_FILENAME).exists(),
    reason="scientific artifacts are written only after the frozen run",
)
def test_completed_artifacts_are_sealed_and_reproduce_prior_binary_counts() -> None:
    summary_path = multiplicity.RESULTS_DIR / multiplicity.SUMMARY_CSV_FILENAME
    long_path = multiplicity.RESULTS_DIR / multiplicity.LONG_CSV_FILENAME
    json_path = multiplicity.RESULTS_DIR / multiplicity.JSON_FILENAME
    for path in (summary_path, long_path, json_path):
        baseline._verify_sidecar(path)
    with summary_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    scientific = [row for row in rows if row["method"] == "MONTE_CARLO_REPRODUCTION"]
    prior = json.loads(
        (refinement.RESULTS_DIR / refinement.JSON_FILENAME).read_text(encoding="utf-8")
    )
    prior_counts = {
        int(row["n"]): (
            int(row["empty_count"]),
            int(row["orbital_unique_count"]),
            int(row["orbital_nonunique_count"]),
        )
        for row in prior["results"]
    }
    assert [int(row["n"]) for row in scientific] == list(multiplicity.N_VALUES)
    for row in scientific:
        observed = (
            int(row["N_empty"]),
            int(row["N_nonempty"]) - int(row["N_R_ge_2"]),
            int(row["N_R_ge_2"]),
        )
        assert observed == prior_counts[int(row["n"])]
    assert payload["result_status"] == multiplicity.SCIENTIFIC_TERMINAL
    assert payload["controls"]["SHANNON_DECOMPOSITION"] == "PASS"
