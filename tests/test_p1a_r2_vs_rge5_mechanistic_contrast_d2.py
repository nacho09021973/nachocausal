"""Guards for the frozen R=2 versus R>=5 combinatorial contrast."""

from __future__ import annotations

import ast
import csv
import io
import json
import math

import numpy as np
import pytest

from emergencia import p1a_large_n_orbital_baseline_d2 as baseline
from emergencia import p1a_orbital_backend_preflight_d2 as orbital
from emergencia import p1a_r2_vs_rge5_mechanistic_contrast_d2 as contrast


def test_design_is_frozen_before_run() -> None:
    assert contrast.N_VALUES == (22, 24, 40)
    assert contrast.N_MC == 100_000
    assert contrast.SCIENTIFIC_SEED_BASE == 260_828_000
    assert contrast.BOOTSTRAP_REPLICATES == 1_000
    assert contrast.BOOTSTRAP_SEED_BASE == 2_608_276_000
    assert contrast.GROUP_ORDER == ("R_EQ_2", "R_GE_5")
    assert contrast.OBSERVABLES == (
        "n_maximizers",
        "n_automorphisms",
        "primary_score",
        "secondary_score",
        "mean_orbit_size",
        "max_orbit_size",
    )


def test_instrument_does_not_import_forbidden_fronts() -> None:
    source = contrast.Path(contrast.__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    assert not any("xi" in name.lower() for name in imported)
    assert not any("estabilidad" in name.lower() for name in imported)
    assert "induced_permutation" not in source
    assert "near_max" not in source


def test_sources_are_sealed_and_prior_partition_is_complete() -> None:
    validation = contrast.validate_sources()
    assert validation["backend_wrapper_byte_identical"] is True
    prior = validation["prior_partition"]
    assert set(prior) == set(contrast.N_VALUES)
    assert all(sum(counter.values()) == contrast.N_MC for counter in prior.values())


def test_descriptor_vector_reuses_complete_exact_orbit_partition() -> None:
    permutation = tuple(range(7))
    result = orbital.evaluate_orbital_backend(permutation, complete_orbits=False)
    assert result.n_orbits_on_m == 2
    assert result.automorphism_enumeration_complete is True
    values = contrast.descriptor_values(permutation, result)
    assert values == contrast.descriptor_values(permutation, result)
    assert len(values) == len(contrast.OBSERVABLES)
    assert values[0] == result.n_maximizers
    assert values[1] == result.n_automorphisms
    assert values[4] == result.n_maximizers / result.n_orbits_on_m
    assert values[5] == max(len(orbit) for orbit in result.orbits or ())


def test_descriptor_vector_fails_closed_on_incomplete_orbits() -> None:
    incomplete = orbital.BackendResult(
        status=orbital.STATUS_ORBITAL_NONUNIQUE,
        n_maximizers=2,
        n_orbits_on_m=2,
        n_automorphisms=None,
        automorphism_enumeration_complete=False,
        maximizers=((0, 1, 2, 3), (1, 2, 3, 4)),
        orbits=None,
    )
    with pytest.raises(RuntimeError, match="complete exact orbit partition"):
        contrast.descriptor_values(tuple(range(7)), incomplete)


def test_point_statistics_use_frozen_pooled_cohen_d() -> None:
    r2 = np.asarray([[1.0, 2.0], [2.0, 4.0], [3.0, 6.0]])
    r5 = np.asarray([[3.0, 3.0], [4.0, 5.0], [5.0, 7.0]])
    mu2, mu5, delta, d = contrast.point_statistics(r2, r5)
    assert np.allclose(mu2, [2.0, 4.0])
    assert np.allclose(mu5, [4.0, 5.0])
    assert np.allclose(delta, [2.0, 1.0])
    pooled = np.sqrt((r2.var(axis=0, ddof=1) + r5.var(axis=0, ddof=1)) / 2)
    assert np.allclose(d, delta / pooled)


def test_joint_multinomial_bootstrap_is_reproducible() -> None:
    r2 = np.asarray([[1.0, 2.0], [1.0, 2.0], [3.0, 4.0], [5.0, 8.0]])
    r5 = np.asarray([[2.0, 3.0], [4.0, 6.0], [6.0, 9.0], [8.0, 12.0]])
    first = contrast.bootstrap_statistics(r2, r5, seed=123, replicates=40)
    second = contrast.bootstrap_statistics(r2, r5, seed=123, replicates=40)
    for name in first:
        assert np.allclose(first[name][0], second[name][0], equal_nan=True)
        assert np.allclose(first[name][1], second[name][1], equal_nan=True)


def test_long_recomposition_reproduces_summary_points(monkeypatch) -> None:
    monkeypatch.setattr(contrast, "N_VALUES", (22,))
    result = contrast.SizeResult(
        n=22,
        seed=contrast.SCIENTIFIC_SEED_BASE + 22,
        total=5,
        counts=(("EMPTY", 1), ("R_EQ_1", 0), ("R_EQ_2", 2), ("R_EQ_3_4", 0), ("R_GE_5", 2)),
        records=(
            contrast.DescriptorRecord(1, "R_EQ_2", 2, (2, 1, 3, 6, 1, 1)),
            contrast.DescriptorRecord(2, "R_EQ_2", 2, (4, 2, 4, 8, 2, 3)),
            contrast.DescriptorRecord(3, "R_GE_5", 5, (5, 1, 5, 10, 1, 1)),
            contrast.DescriptorRecord(4, "R_GE_5", 6, (12, 3, 6, 12, 2, 4)),
        ),
        backend_failures=0,
    )
    monkeypatch.setattr(contrast, "BOOTSTRAP_REPLICATES", 20)
    summary = contrast.summarize(result)
    encoded = contrast._csv_bytes(contrast.long_rows([result]), contrast.LONG_FIELDS)
    contrast.validate_long_recomposition(encoded, summary)


def test_backend_failure_is_never_classified(monkeypatch: pytest.MonkeyPatch) -> None:
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
    monkeypatch.setattr(contrast, "N_MC", 1)
    monkeypatch.setattr(contrast, "_uniform_permutations", lambda *args: [tuple(range(22))])
    monkeypatch.setattr(orbital, "evaluate_orbital_backend", lambda *args, **kwargs: failure)
    with pytest.raises(RuntimeError, match="BACKEND_FAILURE"):
        contrast.run_size(22)


@pytest.mark.skipif(
    not (contrast.RESULTS_DIR / contrast.JSON_FILENAME).exists(),
    reason="scientific artifacts are written only after the frozen run",
)
def test_completed_artifacts_are_sealed_and_recomposable() -> None:
    summary_path = contrast.RESULTS_DIR / contrast.SUMMARY_CSV_FILENAME
    long_path = contrast.RESULTS_DIR / contrast.LONG_CSV_FILENAME
    json_path = contrast.RESULTS_DIR / contrast.JSON_FILENAME
    for path in (summary_path, long_path, json_path):
        baseline._verify_sidecar(path)
    with summary_path.open(newline="", encoding="utf-8") as handle:
        summary = list(csv.DictReader(handle))
    contrast.validate_long_recomposition(long_path.read_bytes(), summary)
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    assert payload["result_status"] == contrast.SCIENTIFIC_TERMINAL
    assert payload["controls"]["BACKEND_FAILURES"] == "0"
    assert payload["controls"]["LONG_RECOMPOSITION"] == "PASS"
    assert len(summary) == len(contrast.N_VALUES) * len(contrast.OBSERVABLES)


def test_long_recomposition_matches_the_summary_memory_layout(monkeypatch) -> None:
    """Regression: the recomposed matrices must be C-contiguous, like ``_arrays``.

    ``np.asarray(columns).T`` is an F-contiguous view, and ``var(axis=0)``
    accumulates in a layout-dependent order once a column exceeds numpy's
    pairwise-summation block.  On the sealed n=22 sample that shifted
    ``primary_score``'s ``cohen_d`` by 1.8e-13 -- just past ``rel_tol=1e-13`` --
    on bit-identical data, aborting the campaign before any artifact was
    written.  The margin is data-dependent and marginal, so the guard is the
    layout invariant itself, not a fixture tuned to cross the threshold.
    """
    monkeypatch.setattr(contrast, "N_VALUES", (22,))
    monkeypatch.setattr(contrast, "BOOTSTRAP_REPLICATES", 5)
    rng = np.random.default_rng(2_608_270_022)
    records = []
    counts = {"EMPTY": 0, "R_EQ_1": 0, "R_EQ_2": 0, "R_EQ_3_4": 0, "R_GE_5": 0}
    for index in range(1_024):
        group = "R_EQ_2" if index % 4 else "R_GE_5"
        counts[group] += 1
        values = tuple(int(value) for value in rng.integers(1, 13, size=6))
        records.append(
            contrast.DescriptorRecord(
                index + 1, group, 2 if group == "R_EQ_2" else 5, values
            )
        )
    result = contrast.SizeResult(
        n=22,
        seed=contrast.SCIENTIFIC_SEED_BASE + 22,
        total=len(records),
        counts=tuple(counts.items()),
        records=tuple(records),
        backend_failures=0,
    )
    summary = contrast.summarize(result)
    encoded = contrast._csv_bytes(contrast.long_rows([result]), contrast.LONG_FIELDS)

    seen: list[tuple[np.ndarray, np.ndarray]] = []
    original = contrast.point_statistics

    def recording(r2: np.ndarray, rge5: np.ndarray):
        seen.append((r2, rge5))
        return original(r2, rge5)

    monkeypatch.setattr(contrast, "point_statistics", recording)
    contrast.validate_long_recomposition(encoded, summary)

    assert len(seen) == 1
    from_csv = seen[0]
    for matrix in from_csv:
        assert matrix.flags["C_CONTIGUOUS"], "recomposition drifted off the summary layout"

    direct = contrast._arrays(result)
    for left, right in zip(direct, from_csv):
        assert np.array_equal(left, right)
    for left, right in zip(original(*direct), original(*from_csv)):
        assert np.array_equal(left, right, equal_nan=True), "statistics not bit-identical"
