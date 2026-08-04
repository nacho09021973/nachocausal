"""Tests for the frozen P1a d=2 stability and bias experiment."""

from __future__ import annotations

import hashlib
import json
from itertools import combinations, permutations
from pathlib import Path

import numpy as np

from emergencia import p1a_enumeracion_simulacion as selector
from emergencia import p1a_estabilidad_d2 as stability


_ROOT = Path(__file__).resolve().parent.parent
_RESULTS = _ROOT / "emergencia" / "resultados"


def naive_unique(permutation: tuple[int, ...]):
    n = len(permutation)

    def interval_size(i: int, j: int) -> int:
        if not (i < j and permutation[i] < permutation[j]):
            return 0
        return sum(
            permutation[i] <= permutation[k] <= permutation[j]
            for k in range(i, j + 1)
        )

    candidates = []
    for a, b, c, d in combinations(range(n), 4):
        if not permutation[a] < permutation[b] < permutation[c] < permutation[d]:
            continue
        past = interval_size(a, b)
        future = interval_size(c, d)
        if past >= selector.K0 and future >= selector.K0:
            candidates.append(((a, b, c, d), past, future, past + future))
    if not candidates:
        return None
    best = max(candidate[3] for candidate in candidates)
    maximizers = [candidate for candidate in candidates if candidate[3] == best]
    return maximizers[0] if len(maximizers) == 1 else None


def test_contract_constants_are_frozen() -> None:
    assert stability.BASE_N == (32, 48, 64, 96, 128)
    assert stability.GATE_N == (64, 96, 128)
    assert stability.BASE_REPLICATES_PER_N == 12_000
    assert stability.BASE_BATCHES == 8
    assert stability.BASE_REPLICATES_PER_BATCH == 1_500
    assert stability.RETENTION == (0.90, 0.80)
    assert stability.COORDINATE_SEED_BASE == 2_608_035_000
    assert stability.THINNING_SEED_BASE == 2_608_036_000
    assert stability.BASELINE_SEED_BASE == 2_608_037_000
    assert stability.BASELINE_REPLICATES_PER_SIZE == 4_000
    assert stability.BOUNDARY_DELTA == 0.05


def test_product_permutation_uses_only_coordinate_ranks() -> None:
    u = np.array([0.8, 0.1, 0.5, 0.3])
    v = np.array([0.2, 0.7, 0.4, 0.1])
    u_sorted, v_sorted, permutation = stability.product_permutation(u, v)
    assert np.array_equal(u_sorted, [0.1, 0.3, 0.5, 0.8])
    assert np.array_equal(v_sorted, [0.7, 0.1, 0.4, 0.2])
    assert np.array_equal(permutation, [3, 0, 2, 1])


def test_unique_extractor_matches_naive_and_sealed_classifier_through_n7() -> None:
    for n in (6, 7):
        for permutation in permutations(range(n)):
            detail = stability.select_unique_quadruple(permutation)
            naive = naive_unique(permutation)
            sealed = selector.classify_permutation(permutation)
            assert (detail is not None) == (naive is not None)
            assert (detail is not None) == (sealed.state == selector.STATE_UNIQUE)
            if detail is not None and naive is not None:
                quadruple, past, future, score = naive
                assert detail.quadruple == quadruple
                assert detail.past_size == past
                assert detail.future_size == future
                assert detail.score == score == sealed.max_score


def test_chain_controls() -> None:
    selected = stability.select_unique_quadruple(tuple(range(6)))
    assert selected is not None
    assert selected.quadruple == (0, 2, 3, 5)
    assert selected.past_size == selected.future_size == 3
    assert stability.select_unique_quadruple(tuple(range(7))) is None


def test_induced_permutation_preserves_all_retained_comparabilities() -> None:
    permutation = np.array([4, 0, 5, 2, 1, 3])
    retained = np.array([0, 1, 3, 5])
    induced = stability.induced_permutation(permutation, retained)
    assert np.array_equal(induced, [3, 0, 1, 2])
    for i, j in combinations(range(len(retained)), 2):
        original_comparable = permutation[retained[i]] < permutation[retained[j]]
        induced_comparable = induced[i] < induced[j]
        assert original_comparable == induced_comparable


def test_interval_height_and_cardinality() -> None:
    height, size = stability.interval_height((0, 2, 1, 4, 3, 5), 0, 5)
    assert size == 6
    assert height == 4
    height, size = stability.interval_height((1, 4, 2, 3, 0, 5), 0, 5)
    assert size == 5
    assert height == 4


def test_fixed_size_baseline_has_exact_m3_height(monkeypatch) -> None:
    monkeypatch.setattr(stability, "BASELINE_REPLICATES_PER_SIZE", 25)
    baselines = stability.simulate_height_baselines((3,))
    assert baselines == {3: [3] * 25}


def test_seeded_small_base_simulation_is_reproducible(monkeypatch) -> None:
    monkeypatch.setattr(stability, "BASE_N", (32,))
    monkeypatch.setattr(stability, "BASE_BATCHES", 1)
    monkeypatch.setattr(stability, "BASE_REPLICATES_PER_BATCH", 30)
    monkeypatch.setattr(stability, "BASE_REPLICATES_PER_N", 30)
    first_accumulators, first_thinning = stability.simulate_base((32,))
    second_accumulators, second_thinning = stability.simulate_base((32,))
    first = first_accumulators[0]
    second = second_accumulators[0]
    assert first.replicates == second.replicates == 30
    assert first.unique_count == second.unique_count
    assert first.past_sizes == second.past_sizes
    assert first.future_sizes == second.future_sizes
    assert first.endpoint_clearances == second.endpoint_clearances
    assert first.selected_intervals == second.selected_intervals
    assert first_thinning == second_thinning


def test_survival_control_accepts_exact_expectation() -> None:
    record = stability.ThinningCounts(
        original_unique=10_000,
        endpoint_survive=6_561,
    )
    tolerance, passed = stability.survival_control(record, 0.90)
    assert tolerance > 0
    assert passed


def test_gate_terminals() -> None:
    stability_rows = [
        {"n": n, "p_floor": 0.05, "p_floor_ci95_low": 0.04, "p_floor_ci95_high": 0.06}
        for n in stability.GATE_N
    ]
    thinning_rows = [
        {
            "n": n,
            "retention": retention,
            "p_same_given_survival": 0.70 if retention == 0.90 else 0.50,
            "p_same_ci95_low": 0.65 if retention == 0.90 else 0.45,
            "p_same_ci95_high": 0.75 if retention == 0.90 else 0.55,
        }
        for n in stability.GATE_N
        for retention in stability.RETENTION
    ]
    terminal, gate = stability.scientific_terminal(stability_rows, thinning_rows)
    assert terminal == stability.TERMINAL_PASS
    assert all(record["pass_n"] for record in gate.values())

    for row in thinning_rows:
        if row["retention"] == 0.90:
            row["p_same_given_survival"] = 0.10
            row["p_same_ci95_low"] = 0.08
            row["p_same_ci95_high"] = 0.12
    terminal, gate = stability.scientific_terminal(stability_rows, thinning_rows)
    assert terminal == stability.TERMINAL_PARK
    assert all(record["park_n"] for record in gate.values())


def test_generated_artifacts_match_frozen_hashes_and_use_lf() -> None:
    expected = {
        "p1a_estabilidad_d2.csv": (
            "aea397394886f9eec161dc90fb02c4ed13f079f10bba433befe5768d60281448"
        ),
        "p1a_thinning_d2.csv": (
            "681e0fd0b05a447046092c8ce5e270075c9095f796f161a06fa69016a46ab842"
        ),
        "p1a_alturas_baseline_d2.csv": (
            "3c2807fb88d17186e71409db2d2e34bf61d03cb079b6d0e18591e90ffde21184"
        ),
        "p1a_estabilidad_resumen.json": (
            "6ec69648666bca250aa7cbca93a2b21e2fb1a7ddabec087eafd5d38df9967dbb"
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


def test_result_records_integrity_and_frozen_inconclusive_terminal() -> None:
    summary = json.loads((_RESULTS / stability.SUMMARY_FILENAME).read_text())
    assert summary["contract_status"] == "FROZEN_BEFORE_RESULTS"
    assert summary["survival_controls_pass"] is True
    assert summary["terminal"] == stability.TERMINAL_INCONCLUSIVE
    assert set(summary["gate"]) == {"64", "96", "128"}
    assert all(
        record["p_same_090_wilson95_low"] >= stability.PASS_SAME_090_LOWER
        for record in summary["gate"].values()
    )
    assert all(
        record["p_same_080_wilson95_low"] >= stability.PASS_SAME_080_LOWER
        for record in summary["gate"].values()
    )
    assert all(
        record["p_floor_wilson95_high"] >= stability.PASS_FLOOR_UPPER
        for record in summary["gate"].values()
    )
