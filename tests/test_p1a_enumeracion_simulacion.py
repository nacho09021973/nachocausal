"""Tests for the frozen P1a d=2 coverage-selector execution."""

from __future__ import annotations

import hashlib
import json
from itertools import combinations
from itertools import permutations
from pathlib import Path

import numpy as np

from emergencia import p1a_enumeracion_simulacion as p1a


_ROOT = Path(__file__).resolve().parent.parent
_RESULTS = _ROOT / "emergencia" / "resultados"


def lis_length(permutation: tuple[int, ...]) -> int:
    tails: list[int] = []
    for value in permutation:
        index = int(np.searchsorted(tails, value))
        if index == len(tails):
            tails.append(value)
        else:
            tails[index] = value
    return len(tails)


def naive_outcome(permutation: tuple[int, ...]):
    n = len(permutation)

    def interval_size(i: int, j: int) -> int:
        if not (i < j and permutation[i] < permutation[j]):
            return 0
        return sum(
            i <= k <= j and permutation[i] <= permutation[k] <= permutation[j]
            for k in range(n)
        )

    candidates = []
    for a, b, c, d in combinations(range(n), 4):
        if not (
            permutation[a]
            < permutation[b]
            < permutation[c]
            < permutation[d]
        ):
            continue
        left = interval_size(a, b)
        right = interval_size(c, d)
        if left >= p1a.K0 and right >= p1a.K0:
            candidates.append(((a, b, c, d), left + right))
    if not candidates:
        return p1a.STATE_EMPTY, 0, 0
    max_score = max(score for _, score in candidates)
    maximizers = [quad for quad, score in candidates if score == max_score]
    if len(maximizers) == 1:
        state = p1a.STATE_UNIQUE
    else:
        bridges = {(b, c) for _, b, c, _ in maximizers}
        bridge_tie = len(bridges) > 1
        past_tie = any(
            len({a for a, b0, _, _ in maximizers if b0 == b}) > 1
            for b, _ in bridges
        )
        future_tie = any(
            len({d for _, _, c0, d in maximizers if c0 == c}) > 1
            for _, c in bridges
        )
        flags = (bridge_tie, past_tie, future_tie)
        if flags == (True, False, False):
            state = p1a.STATE_TIE_BRIDGE
        elif flags == (False, True, False):
            state = p1a.STATE_TIE_PAST
        elif flags == (False, False, True):
            state = p1a.STATE_TIE_FUTURE
        else:
            state = p1a.STATE_TIE_MIXED
    return state, len(maximizers), max_score


def test_contract_constants_are_frozen() -> None:
    assert p1a.K0 == 3
    assert p1a.EXACT_N == (6, 7, 8, 9)
    assert p1a.MC_N == (6, 7, 8, 9, 12, 16, 24, 32, 48, 64)
    assert p1a.MC_REPLICATES_PER_N == 20_000
    assert p1a.MC_BATCHES == 8
    assert p1a.MC_REPLICATES_PER_BATCH == 2_500
    assert p1a.SEED_BASE == 2_608_030_000
    assert p1a.GATE_N == (32, 48, 64)


def test_increasing_chain_n6_is_unique() -> None:
    outcome = p1a.classify_permutation(tuple(range(6)))
    assert outcome.state == p1a.STATE_UNIQUE
    assert outcome.n_maximizers == 1
    assert outcome.max_score == 6


def test_increasing_chain_n7_has_two_bridge_maximizers() -> None:
    outcome = p1a.classify_permutation(tuple(range(7)))
    assert outcome.state == p1a.STATE_TIE_BRIDGE
    assert outcome.n_maximizers == 2
    assert outcome.n_maximizing_bridges == 2
    assert outcome.max_score == 7


def test_decreasing_permutation_is_empty() -> None:
    outcome = p1a.classify_permutation(tuple(reversed(range(12))))
    assert outcome.state == p1a.STATE_EMPTY


def test_chain_six_plus_isolates_is_unique() -> None:
    for n in (7, 8, 12):
        permutation = tuple(range(n - 1, 5, -1)) + tuple(range(6))
        outcome = p1a.classify_permutation(permutation)
        assert outcome.state == p1a.STATE_UNIQUE
        assert outcome.n_maximizers == 1


def test_empty_equivalent_to_lis_below_six_for_all_n6_permutations() -> None:
    for permutation in permutations(range(6)):
        empty = p1a.classify_permutation(permutation).state == p1a.STATE_EMPTY
        assert empty == (lis_length(permutation) < 6)


def test_exact_n6_analytic_counts() -> None:
    aggregate = p1a.enumerate_exact((6,))[0]
    assert aggregate.counts[p1a.STATE_EMPTY] == 719
    assert aggregate.counts[p1a.STATE_UNIQUE] == 1
    assert sum(aggregate.counts[state] for state in p1a.TIE_STATES) == 0


def test_vectorized_classifier_matches_naive_for_all_n6_permutations() -> None:
    for permutation in permutations(range(6)):
        outcome = p1a.classify_permutation(permutation)
        assert (outcome.state, outcome.n_maximizers, outcome.max_score) == naive_outcome(
            permutation
        )


def test_exact_n7_rsk_empty_count() -> None:
    aggregate = p1a.enumerate_exact((7,))[0]
    assert aggregate.counts[p1a.STATE_EMPTY] == 5003


def test_seeded_monte_carlo_is_reproducible_for_small_batch(monkeypatch) -> None:
    monkeypatch.setattr(p1a, "MC_BATCHES", 1)
    monkeypatch.setattr(p1a, "MC_REPLICATES_PER_BATCH", 25)
    monkeypatch.setattr(p1a, "MC_REPLICATES_PER_N", 25)
    first = p1a.simulate_monte_carlo((8,))[0]
    second = p1a.simulate_monte_carlo((8,))[0]
    assert first.counts == second.counts
    assert first.diagnostic_dict() == second.diagnostic_dict()


def test_wilson_interval_contains_observed_fraction() -> None:
    low, high = p1a.wilson_interval(2000, 20_000)
    assert low < 0.1 < high


def test_generated_artifacts_match_frozen_hashes_and_use_lf() -> None:
    expected = {
        "p1a_enumeracion_exacta_d2.csv": (
            "650ce526e1e88626ce41d8e9925d5b19fbb94c143c63714c0e51ebd9fcafd224"
        ),
        "p1a_monte_carlo_d2.csv": (
            "a760fb72b31cd4a783fa13c94b5426bc73ede00208f9609dd1e9d91cf79fa3e9"
        ),
        "p1a_ejecucion_resumen.json": (
            "fa1c24ff46bb183f5c2d6b0e8cbe422ce2eae7e514ce3f81a2328fabba2f7073"
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


def test_result_summary_records_valid_crosscheck_and_operational_terminal() -> None:
    summary = json.loads((_RESULTS / "p1a_ejecucion_resumen.json").read_text())
    assert summary["contract_status"] == "FROZEN_BEFORE_RESULTS"
    assert summary["crosscheck_pass"] is True
    assert summary["terminal"] == p1a.TERMINAL_VIABLE
    assert set(summary["gate"]) == {"32", "48", "64"}
    assert all(record["wilson95_low"] >= 0.10 for record in summary["gate"].values())
