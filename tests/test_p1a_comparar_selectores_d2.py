"""Tests for the frozen paired comparison of P1a d=2 selectors."""

from __future__ import annotations

import hashlib
import json
from itertools import combinations, permutations
from pathlib import Path

import numpy as np

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_estabilidad_d2 as previous


_ROOT = Path(__file__).resolve().parent.parent
_RESULTS = _ROOT / "emergencia" / "resultados"


def naive_outcomes(permutation: tuple[int, ...]):
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
        if past >= sealed.K0 and future >= sealed.K0:
            candidates.append(((a, b, c, d), past, future))

    if not candidates:
        return {
            name: (comparison.STATE_EMPTY, 0, None, None, None)
            for name in comparison.SELECTORS
        }

    scores = {
        comparison.COVERAGE: lambda past, future: (past + future,),
        comparison.MIN_ONLY: lambda past, future: (min(past, future),),
        comparison.MIN_COVERAGE_LEX: lambda past, future: (
            min(past, future),
            past + future,
        ),
    }
    results = {}
    for name, score_function in scores.items():
        scored = [
            (quadruple, past, future, score_function(past, future))
            for quadruple, past, future in candidates
        ]
        best = max(record[3] for record in scored)
        maximizers = [record for record in scored if record[3] == best]
        state = (
            comparison.STATE_UNIQUE
            if len(maximizers) == 1
            else comparison.STATE_TIE
        )
        selection = maximizers[0][:3] if len(maximizers) == 1 else None
        primary = best[0]
        secondary = best[1] if len(best) == 2 else None
        results[name] = (state, len(maximizers), primary, secondary, selection)
    return results


def test_contract_constants_are_frozen() -> None:
    assert comparison.SELECTORS == (
        comparison.COVERAGE,
        comparison.MIN_ONLY,
        comparison.MIN_COVERAGE_LEX,
    )
    assert comparison.CANDIDATES == (
        comparison.MIN_ONLY,
        comparison.MIN_COVERAGE_LEX,
    )
    assert comparison.BASE_N == (32, 48, 64, 96, 128)
    assert comparison.GATE_N == (64, 96, 128)
    assert comparison.BASE_REPLICATES_PER_N == 12_000
    assert comparison.BASE_BATCHES == 8
    assert comparison.BASE_REPLICATES_PER_BATCH == 1_500
    assert comparison.COORDINATE_SEED_BASE == 2_608_038_000
    assert comparison.THINNING_SEED_BASE == 2_608_039_000


def test_all_selectors_match_naive_enumeration_through_n7() -> None:
    for n in (6, 7):
        for permutation in permutations(range(n)):
            expected = naive_outcomes(permutation)
            observed = comparison.evaluate_selectors(permutation)
            for name in comparison.SELECTORS:
                state, nmax, primary, secondary, selection = expected[name]
                outcome = observed[name]
                assert outcome.state == state
                assert outcome.n_maximizers == nmax
                assert outcome.primary_score == primary
                assert outcome.secondary_score == secondary
                if selection is None:
                    assert outcome.selection is None
                else:
                    quadruple, past, future = selection
                    assert outcome.selection is not None
                    assert outcome.selection.quadruple == quadruple
                    assert outcome.selection.past_size == past
                    assert outcome.selection.future_size == future


def test_coverage_matches_sealed_classifier_through_n7() -> None:
    for n in (6, 7):
        for permutation in permutations(range(n)):
            observed = comparison.evaluate_selectors(permutation)[comparison.COVERAGE]
            expected = sealed.classify_permutation(permutation)
            if expected.state == sealed.STATE_EMPTY:
                expected_state = comparison.STATE_EMPTY
            elif expected.state == sealed.STATE_UNIQUE:
                expected_state = comparison.STATE_UNIQUE
            else:
                expected_state = comparison.STATE_TIE
            assert observed.state == expected_state
            assert observed.n_maximizers == expected.n_maximizers
            assert observed.primary_score == (
                expected.max_score if expected.state != sealed.STATE_EMPTY else None
            )


def test_chain_controls() -> None:
    n6 = comparison.evaluate_selectors(tuple(range(6)))
    assert all(outcome.state == comparison.STATE_UNIQUE for outcome in n6.values())
    assert all(
        outcome.selection is not None
        and outcome.selection.quadruple == (0, 2, 3, 5)
        for outcome in n6.values()
    )
    n7 = comparison.evaluate_selectors(tuple(range(7)))
    assert all(outcome.state == comparison.STATE_TIE for outcome in n7.values())


def test_empty_state_is_common_to_all_scores() -> None:
    outcomes = comparison.evaluate_selectors(tuple(reversed(range(12))))
    assert all(outcome.state == comparison.STATE_EMPTY for outcome in outcomes.values())


def test_induced_permutation_control_remains_valid() -> None:
    permutation = np.array([4, 0, 5, 2, 1, 3])
    retained = np.array([0, 1, 3, 5])
    induced = previous.induced_permutation(permutation, retained)
    for i, j in combinations(range(len(retained)), 2):
        assert (permutation[retained[i]] < permutation[retained[j]]) == (
            induced[i] < induced[j]
        )


def test_small_paired_simulation_is_reproducible(monkeypatch) -> None:
    monkeypatch.setattr(comparison, "BASE_N", (32,))
    monkeypatch.setattr(comparison, "BASE_BATCHES", 1)
    monkeypatch.setattr(comparison, "BASE_REPLICATES_PER_BATCH", 25)
    monkeypatch.setattr(comparison, "BASE_REPLICATES_PER_N", 25)
    first = comparison.simulate()
    second = comparison.simulate()
    assert first == second


def _synthetic_gate_rows(min_qualifies: bool, lex_qualifies: bool):
    selector_rows = []
    thinning_rows = []
    qualification = {
        comparison.MIN_ONLY: min_qualifies,
        comparison.MIN_COVERAGE_LEX: lex_qualifies,
    }
    for name in comparison.CANDIDATES:
        good = qualification[name]
        for n in comparison.GATE_N:
            selector_rows.append(
                {
                    "selector": name,
                    "n": n,
                    "p_unique": 0.30 if good else 0.05,
                    "p_unique_ci95_low": 0.25 if good else 0.04,
                    "p_floor": 0.05,
                    "p_floor_ci95_high": 0.07,
                }
            )
            for retention in comparison.RETENTION:
                thinning_rows.append(
                    {
                        "selector": name,
                        "n": n,
                        "retention": retention,
                        "p_same_given_survival": 0.75,
                        "p_same_ci95_low": 0.70,
                    }
                )
    return selector_rows, thinning_rows


def test_gate_priority_and_terminals() -> None:
    selectors, thinning = _synthetic_gate_rows(True, True)
    terminal, selected, _ = comparison.scientific_terminal(selectors, thinning)
    assert terminal == comparison.TERMINAL_SELECT_MIN
    assert selected == comparison.MIN_ONLY

    selectors, thinning = _synthetic_gate_rows(False, True)
    terminal, selected, _ = comparison.scientific_terminal(selectors, thinning)
    assert terminal == comparison.TERMINAL_SELECT_LEX
    assert selected == comparison.MIN_COVERAGE_LEX

    selectors, thinning = _synthetic_gate_rows(False, False)
    terminal, selected, _ = comparison.scientific_terminal(selectors, thinning)
    assert terminal == comparison.TERMINAL_NONE
    assert selected is None


def test_generated_artifacts_match_frozen_hashes_and_use_lf() -> None:
    expected = {
        "p1a_comparacion_selectores_d2.csv": (
            "fa8b5fe9989658ee8b4de7df14ab2c5bbb5cd1319a0de646142f769a9062e0bf"
        ),
        "p1a_comparacion_thinning_d2.csv": (
            "7734986acc5661985a3c05f3c42e0dfd845ebfb031b172cd741e62f8cefa6fe0"
        ),
        "p1a_comparacion_pareada_selectores_d2.csv": (
            "65cdeaffc1c687e12ddfddda8eea9ddc3385048e161f7f9daa3317acae725bdb"
        ),
        "p1a_comparacion_selectores_resumen.json": (
            "798282701e9bafc10af3d6a5899d52bb793b15829c6394215ab6ca25ebc515e7"
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


def test_result_selects_lexicographic_candidate_under_frozen_gate() -> None:
    summary = json.loads((_RESULTS / comparison.SUMMARY_FILENAME).read_text())
    assert summary["contract_status"] == "FROZEN_BEFORE_RESULTS"
    assert summary["survival_controls_pass"] is True
    assert summary["terminal"] == comparison.TERMINAL_SELECT_LEX
    assert summary["selected_candidate"] == comparison.MIN_COVERAGE_LEX
    assert summary["gate"][comparison.MIN_ONLY]["qualifies_all_gate_n"] is False
    assert (
        summary["gate"][comparison.MIN_COVERAGE_LEX]["qualifies_all_gate_n"]
        is True
    )
    assert all(
        record["qualifies_n"]
        for record in summary["gate"][comparison.MIN_COVERAGE_LEX]["by_n"].values()
    )
