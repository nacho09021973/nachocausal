#!/usr/bin/env python3
"""Paired d=2 comparison of coverage and balanced P1a selectors.

All selectors see the same order-only permutation and thinned induced subposets.
Latent coordinates are used only for post-selection boundary diagnostics. Heights
and metric ratios are outside this frozen comparison contract.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import os
import platform
import statistics
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import numpy as np

from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_estabilidad_d2 as previous


COVERAGE = "COVERAGE"
MIN_ONLY = "MIN_ONLY"
MIN_COVERAGE_LEX = "MIN_COVERAGE_LEX"
SELECTORS = (COVERAGE, MIN_ONLY, MIN_COVERAGE_LEX)
CANDIDATES = (MIN_ONLY, MIN_COVERAGE_LEX)

STATE_EMPTY = "EMPTY"
STATE_UNIQUE = "UNIQUE"
STATE_TIE = "TIE"
STATES = (STATE_EMPTY, STATE_UNIQUE, STATE_TIE)

BASE_N = (32, 48, 64, 96, 128)
GATE_N = (64, 96, 128)
BASE_REPLICATES_PER_N = 12_000
BASE_BATCHES = 8
BASE_REPLICATES_PER_BATCH = 1_500
RETENTION = (0.90, 0.80)
COORDINATE_SEED_BASE = 2_608_038_000
THINNING_SEED_BASE = 2_608_039_000
BOUNDARY_DELTA = 0.05
UNIFORM_BOUNDARY_REFERENCE = 1.0 - (1.0 - 2.0 * BOUNDARY_DELTA) ** 2

QUALIFY_UNIQUE_LOWER = 0.10
QUALIFY_SAME_090_LOWER = 0.50
QUALIFY_SAME_080_LOWER = 0.25
QUALIFY_FLOOR_UPPER = 0.25

TERMINAL_SELECT_MIN = "SELECT_MIN_ONLY_FOR_HEIGHT_BIAS_GATE"
TERMINAL_SELECT_LEX = "SELECT_MIN_COVERAGE_LEX_FOR_HEIGHT_BIAS_GATE"
TERMINAL_NONE = "NO_BALANCED_SELECTOR_QUALIFIES"
TERMINAL_INVALID = "IMPLEMENTATION_INVALID"

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = HERE / "resultados"
SELECTOR_FILENAME = "p1a_comparacion_selectores_d2.csv"
THINNING_FILENAME = "p1a_comparacion_thinning_d2.csv"
PAIRED_FILENAME = "p1a_comparacion_pareada_selectores_d2.csv"
SUMMARY_FILENAME = "p1a_comparacion_selectores_resumen.json"

SELECTOR_FIELDS = (
    "selector",
    "n",
    "replicates",
    "empty_count",
    "p_empty",
    "unique_count",
    "p_unique",
    "p_unique_ci95_low",
    "p_unique_ci95_high",
    "tie_count",
    "p_tie",
    "floor_count",
    "p_floor",
    "p_floor_ci95_low",
    "p_floor_ci95_high",
    "past_size_mean",
    "future_size_mean",
    "min_size_mean",
    "min_size_median",
    "balance_mean",
    "balance_median",
    "selected_endpoint_count",
    "near_boundary_endpoint_count",
    "near_boundary_endpoint_fraction",
    "uniform_boundary_reference",
    "boundary_enrichment",
    "endpoint_clearance_mean",
)

THINNING_FIELDS = (
    "selector",
    "n",
    "retention",
    "original_unique_count",
    "endpoint_survive_count",
    "endpoint_survive_fraction",
    "endpoint_survive_expected",
    "survival_control_tolerance",
    "survival_control_pass",
    "thinned_unique_count",
    "thinned_unique_given_survival_count",
    "p_thinned_unique_given_survival",
    "exact_reselected_count",
    "p_same_given_survival",
    "p_same_ci95_low",
    "p_same_ci95_high",
    "p_same_unconditional",
)

PAIRED_FIELDS = (
    "n",
    "selector_a",
    "selector_b",
    "replicates",
    "a_unique_count",
    "b_unique_count",
    "both_unique_count",
    "a_only_unique_count",
    "b_only_unique_count",
    "same_quadruple_count",
    "p_same_quadruple_given_both_unique",
)


@dataclass(frozen=True)
class Selection:
    quadruple: tuple[int, int, int, int]
    past_size: int
    future_size: int


@dataclass(frozen=True)
class ScoreOutcome:
    state: str
    n_maximizers: int
    primary_score: int | None
    secondary_score: int | None
    selection: Selection | None


@dataclass
class SelectorAccumulator:
    selector: str
    n: int
    replicates: int = 0
    counts: Counter[str] | None = None
    past_sizes: list[int] | None = None
    future_sizes: list[int] | None = None
    min_sizes: list[int] | None = None
    balances: list[float] | None = None
    endpoint_clearances: list[float] | None = None

    def __post_init__(self) -> None:
        self.counts = Counter()
        self.past_sizes = []
        self.future_sizes = []
        self.min_sizes = []
        self.balances = []
        self.endpoint_clearances = []


@dataclass
class ThinningCounts:
    original_unique: int = 0
    endpoint_survive: int = 0
    thinned_unique: int = 0
    thinned_unique_given_survival: int = 0
    exact_reselected: int = 0


@dataclass
class PairCounts:
    replicates: int = 0
    a_unique: int = 0
    b_unique: int = 0
    both_unique: int = 0
    same_quadruple: int = 0


def coordinate_seed(n: int, batch: int) -> int:
    if n not in BASE_N or not 0 <= batch < BASE_BATCHES:
        raise ValueError("coordinate seed outside frozen contract")
    return COORDINATE_SEED_BASE + 100 * n + batch


def thinning_seed(n: int, batch: int) -> int:
    if n not in BASE_N or not 0 <= batch < BASE_BATCHES:
        raise ValueError("thinning seed outside frozen contract")
    return THINNING_SEED_BASE + 100 * n + batch


def _empty_outcome() -> ScoreOutcome:
    return ScoreOutcome(STATE_EMPTY, 0, None, None, None)


def _selection(
    counts: np.ndarray, a: int, b: int, c: int, d: int
) -> Selection:
    return Selection(
        quadruple=(a, b, c, d),
        past_size=int(counts[a, b]),
        future_size=int(counts[c, d]),
    )


def _retrieve_unique(
    counts: np.ndarray,
    eligible: np.ndarray,
    bridge_rows: np.ndarray,
    bridge_cols: np.ndarray,
    predicate,
) -> Selection:
    matches: list[Selection] = []
    for b_raw, c_raw in zip(bridge_rows, bridge_cols):
        b, c = int(b_raw), int(c_raw)
        for a_raw in np.flatnonzero(eligible[:, b]):
            a = int(a_raw)
            left = int(counts[a, b])
            for d_raw in np.flatnonzero(eligible[c, :]):
                d = int(d_raw)
                right = int(counts[c, d])
                if predicate(left, right):
                    matches.append(_selection(counts, a, b, c, d))
                    if len(matches) > 1:
                        raise RuntimeError("unique score count produced multiple endpoints")
    if len(matches) != 1:
        raise RuntimeError("unique score count did not identify one endpoint tuple")
    return matches[0]


def evaluate_selectors(permutation: Sequence[int]) -> dict[str, ScoreOutcome]:
    """Evaluate all three selectors from one interval-count matrix."""

    counts, comparable = sealed.interval_count_matrix(permutation)
    eligible = counts >= sealed.K0
    left_max = np.where(eligible, counts, -1).max(axis=0)
    right_max = np.where(eligible, counts, -1).max(axis=1)
    left_mult = ((counts == left_max[None, :]) & eligible).sum(axis=0)
    right_mult = ((counts == right_max[:, None]) & eligible).sum(axis=1)
    bridges = comparable & (left_max[:, None] >= sealed.K0) & (
        right_max[None, :] >= sealed.K0
    )
    if not bool(bridges.any()):
        return {name: _empty_outcome() for name in SELECTORS}

    outcomes: dict[str, ScoreOutcome] = {}

    coverage_scores = left_max[:, None] + right_max[None, :]
    coverage_best = int(coverage_scores[bridges].max())
    coverage_bridges = bridges & (coverage_scores == coverage_best)
    coverage_rows, coverage_cols = np.nonzero(coverage_bridges)
    coverage_nmax = sum(
        int(left_mult[b]) * int(right_mult[c])
        for b, c in zip(coverage_rows, coverage_cols)
    )
    if coverage_nmax == 1:
        b, c = int(coverage_rows[0]), int(coverage_cols[0])
        a = int(np.flatnonzero(eligible[:, b] & (counts[:, b] == left_max[b]))[0])
        d = int(np.flatnonzero(eligible[c, :] & (counts[c, :] == right_max[c]))[0])
        coverage_selection = _selection(counts, a, b, c, d)
        coverage_state = STATE_UNIQUE
    else:
        coverage_selection = None
        coverage_state = STATE_TIE
    outcomes[COVERAGE] = ScoreOutcome(
        coverage_state, coverage_nmax, coverage_best, None, coverage_selection
    )

    minimum_scores = np.minimum(left_max[:, None], right_max[None, :])
    minimum_best = int(minimum_scores[bridges].max())
    minimum_bridges = bridges & (minimum_scores == minimum_best)
    minimum_rows, minimum_cols = np.nonzero(minimum_bridges)
    left_ge = ((counts >= minimum_best) & eligible).sum(axis=0)
    right_ge = ((counts >= minimum_best) & eligible).sum(axis=1)
    left_gt = ((counts > minimum_best) & eligible).sum(axis=0)
    right_gt = ((counts > minimum_best) & eligible).sum(axis=1)
    minimum_nmax = sum(
        int(left_ge[b]) * int(right_ge[c])
        - int(left_gt[b]) * int(right_gt[c])
        for b, c in zip(minimum_rows, minimum_cols)
    )
    if minimum_nmax == 1:
        minimum_selection = _retrieve_unique(
            counts,
            eligible,
            minimum_rows,
            minimum_cols,
            lambda left, right: min(left, right) == minimum_best,
        )
        minimum_state = STATE_UNIQUE
    else:
        minimum_selection = None
        minimum_state = STATE_TIE
    outcomes[MIN_ONLY] = ScoreOutcome(
        minimum_state, minimum_nmax, minimum_best, None, minimum_selection
    )

    left_equal = ((counts == minimum_best) & eligible).sum(axis=0)
    right_equal = ((counts == minimum_best) & eligible).sum(axis=1)
    lex_records: list[tuple[int, int, int, int]] = []
    lex_secondary_best = -1
    for b_raw, c_raw in zip(minimum_rows, minimum_cols):
        b, c = int(b_raw), int(c_raw)
        case_scores: list[tuple[int, int]] = []
        if int(left_equal[b]) > 0:
            case_scores.append(
                (
                    minimum_best + int(right_max[c]),
                    int(left_equal[b]) * int(right_mult[c]),
                )
            )
        if int(right_equal[c]) > 0:
            case_scores.append(
                (
                    minimum_best + int(left_max[b]),
                    int(right_equal[c]) * int(left_mult[b]),
                )
            )
        local_best = max(score for score, _ in case_scores)
        local_count = sum(count for score, count in case_scores if score == local_best)
        if (
            len(case_scores) == 2
            and case_scores[0][0] == case_scores[1][0]
            and int(left_max[b]) == minimum_best
            and int(right_max[c]) == minimum_best
        ):
            local_count -= int(left_equal[b]) * int(right_equal[c])
        lex_records.append((b, c, local_best, local_count))
        lex_secondary_best = max(lex_secondary_best, local_best)

    lex_best_records = [record for record in lex_records if record[2] == lex_secondary_best]
    lex_nmax = sum(record[3] for record in lex_best_records)
    lex_rows = np.asarray([record[0] for record in lex_best_records], dtype=np.int64)
    lex_cols = np.asarray([record[1] for record in lex_best_records], dtype=np.int64)
    if lex_nmax == 1:
        lex_selection = _retrieve_unique(
            counts,
            eligible,
            lex_rows,
            lex_cols,
            lambda left, right: (
                min(left, right) == minimum_best
                and left + right == lex_secondary_best
            ),
        )
        lex_state = STATE_UNIQUE
    else:
        lex_selection = None
        lex_state = STATE_TIE
    outcomes[MIN_COVERAGE_LEX] = ScoreOutcome(
        lex_state,
        lex_nmax,
        minimum_best,
        lex_secondary_best,
        lex_selection,
    )
    return outcomes


def _mean(values: Sequence[int] | Sequence[float]) -> float | None:
    return float(statistics.fmean(values)) if values else None


def _median(values: Sequence[int] | Sequence[float]) -> float | None:
    return float(statistics.median(values)) if values else None


def _wilson(successes: int, trials: int) -> tuple[float | None, float | None]:
    if trials == 0:
        return None, None
    return sealed.wilson_interval(successes, trials)


def simulate() -> tuple[
    dict[tuple[str, int], SelectorAccumulator],
    dict[tuple[str, int, float], ThinningCounts],
    dict[tuple[int, str, str], PairCounts],
]:
    accumulators = {
        (name, n): SelectorAccumulator(name, n) for name in SELECTORS for n in BASE_N
    }
    thinning = {
        (name, n, retention): ThinningCounts()
        for name in SELECTORS
        for n in BASE_N
        for retention in RETENTION
    }
    pairs = {
        (n, SELECTORS[i], SELECTORS[j]): PairCounts()
        for n in BASE_N
        for i in range(len(SELECTORS))
        for j in range(i + 1, len(SELECTORS))
    }

    for n in BASE_N:
        for batch in range(BASE_BATCHES):
            coordinate_rng = np.random.Generator(
                np.random.PCG64(coordinate_seed(n, batch))
            )
            thinning_rng = np.random.Generator(np.random.PCG64(thinning_seed(n, batch)))
            for _ in range(BASE_REPLICATES_PER_BATCH):
                u_sorted, v_sorted, permutation = previous.product_permutation(
                    coordinate_rng.random(n), coordinate_rng.random(n)
                )
                masks = {
                    retention: thinning_rng.random(n) < retention
                    for retention in RETENTION
                }
                outcomes = evaluate_selectors(permutation)

                for name in SELECTORS:
                    outcome = outcomes[name]
                    accumulator = accumulators[(name, n)]
                    assert accumulator.counts is not None
                    accumulator.replicates += 1
                    accumulator.counts[outcome.state] += 1
                    if outcome.state != STATE_UNIQUE:
                        continue
                    if outcome.selection is None:
                        raise RuntimeError("UNIQUE outcome missing selection")
                    selection = outcome.selection
                    assert accumulator.past_sizes is not None
                    assert accumulator.future_sizes is not None
                    assert accumulator.min_sizes is not None
                    assert accumulator.balances is not None
                    assert accumulator.endpoint_clearances is not None
                    accumulator.past_sizes.append(selection.past_size)
                    accumulator.future_sizes.append(selection.future_size)
                    accumulator.min_sizes.append(
                        min(selection.past_size, selection.future_size)
                    )
                    accumulator.balances.append(
                        min(selection.past_size, selection.future_size)
                        / max(selection.past_size, selection.future_size)
                    )
                    for endpoint in selection.quadruple:
                        accumulator.endpoint_clearances.append(
                            min(
                                float(u_sorted[endpoint]),
                                1.0 - float(u_sorted[endpoint]),
                                float(v_sorted[endpoint]),
                                1.0 - float(v_sorted[endpoint]),
                            )
                        )

                for i in range(len(SELECTORS)):
                    for j in range(i + 1, len(SELECTORS)):
                        a_name, b_name = SELECTORS[i], SELECTORS[j]
                        record = pairs[(n, a_name, b_name)]
                        a_outcome, b_outcome = outcomes[a_name], outcomes[b_name]
                        a_unique = a_outcome.state == STATE_UNIQUE
                        b_unique = b_outcome.state == STATE_UNIQUE
                        record.replicates += 1
                        record.a_unique += int(a_unique)
                        record.b_unique += int(b_unique)
                        if a_unique and b_unique:
                            record.both_unique += 1
                            assert a_outcome.selection is not None
                            assert b_outcome.selection is not None
                            record.same_quadruple += int(
                                a_outcome.selection.quadruple
                                == b_outcome.selection.quadruple
                            )

                if not any(outcome.state == STATE_UNIQUE for outcome in outcomes.values()):
                    continue
                for retention in RETENTION:
                    mask = masks[retention]
                    retained = np.flatnonzero(mask)
                    if len(retained) >= 2 * sealed.K0:
                        induced = previous.induced_permutation(permutation, retained)
                        thinned_outcomes = evaluate_selectors(induced)
                    else:
                        thinned_outcomes = {
                            name: _empty_outcome() for name in SELECTORS
                        }
                    for name in SELECTORS:
                        base_outcome = outcomes[name]
                        if base_outcome.state != STATE_UNIQUE:
                            continue
                        assert base_outcome.selection is not None
                        record = thinning[(name, n, retention)]
                        record.original_unique += 1
                        endpoints_survive = bool(
                            mask[list(base_outcome.selection.quadruple)].all()
                        )
                        if endpoints_survive:
                            record.endpoint_survive += 1
                        thinned_outcome = thinned_outcomes[name]
                        if thinned_outcome.state != STATE_UNIQUE:
                            continue
                        assert thinned_outcome.selection is not None
                        record.thinned_unique += 1
                        if endpoints_survive:
                            record.thinned_unique_given_survival += 1
                        mapped = tuple(
                            int(retained[index])
                            for index in thinned_outcome.selection.quadruple
                        )
                        if mapped == base_outcome.selection.quadruple:
                            if not endpoints_survive:
                                raise RuntimeError(
                                    "reselected endpoint did not survive thinning"
                                )
                            record.exact_reselected += 1

        for name in SELECTORS:
            accumulator = accumulators[(name, n)]
            if accumulator.replicates != BASE_REPLICATES_PER_N:
                raise RuntimeError(f"replicate mismatch selector={name} n={n}")
            assert accumulator.counts is not None
            if sum(accumulator.counts[state] for state in STATES) != accumulator.replicates:
                raise RuntimeError(f"state partition mismatch selector={name} n={n}")
        print(
            "P1A_COMPARE_N={} ".format(n)
            + " ".join(
                f"{name}_UNIQUE={accumulators[(name, n)].counts[STATE_UNIQUE]}"
                for name in SELECTORS
            ),
            flush=True,
        )
    return accumulators, thinning, pairs


def selector_rows(
    accumulators: dict[tuple[str, int], SelectorAccumulator]
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for name in SELECTORS:
        for n in BASE_N:
            accumulator = accumulators[(name, n)]
            assert accumulator.counts is not None
            assert accumulator.past_sizes is not None
            assert accumulator.future_sizes is not None
            assert accumulator.min_sizes is not None
            assert accumulator.balances is not None
            assert accumulator.endpoint_clearances is not None
            unique = accumulator.counts[STATE_UNIQUE]
            floor = sum(size == sealed.K0 for size in accumulator.min_sizes)
            unique_low, unique_high = _wilson(unique, accumulator.replicates)
            floor_low, floor_high = _wilson(floor, unique)
            endpoint_count = len(accumulator.endpoint_clearances)
            near_count = sum(
                clearance <= BOUNDARY_DELTA
                for clearance in accumulator.endpoint_clearances
            )
            near_fraction = near_count / endpoint_count if endpoint_count else None
            rows.append(
                {
                    "selector": name,
                    "n": n,
                    "replicates": accumulator.replicates,
                    "empty_count": accumulator.counts[STATE_EMPTY],
                    "p_empty": accumulator.counts[STATE_EMPTY] / accumulator.replicates,
                    "unique_count": unique,
                    "p_unique": unique / accumulator.replicates,
                    "p_unique_ci95_low": unique_low,
                    "p_unique_ci95_high": unique_high,
                    "tie_count": accumulator.counts[STATE_TIE],
                    "p_tie": accumulator.counts[STATE_TIE] / accumulator.replicates,
                    "floor_count": floor,
                    "p_floor": floor / unique if unique else None,
                    "p_floor_ci95_low": floor_low,
                    "p_floor_ci95_high": floor_high,
                    "past_size_mean": _mean(accumulator.past_sizes),
                    "future_size_mean": _mean(accumulator.future_sizes),
                    "min_size_mean": _mean(accumulator.min_sizes),
                    "min_size_median": _median(accumulator.min_sizes),
                    "balance_mean": _mean(accumulator.balances),
                    "balance_median": _median(accumulator.balances),
                    "selected_endpoint_count": endpoint_count,
                    "near_boundary_endpoint_count": near_count,
                    "near_boundary_endpoint_fraction": near_fraction,
                    "uniform_boundary_reference": UNIFORM_BOUNDARY_REFERENCE,
                    "boundary_enrichment": (
                        near_fraction / UNIFORM_BOUNDARY_REFERENCE
                        if near_fraction is not None
                        else None
                    ),
                    "endpoint_clearance_mean": _mean(
                        accumulator.endpoint_clearances
                    ),
                }
            )
    return rows


def _survival_control(
    record: ThinningCounts, retention: float
) -> tuple[float | None, bool | None]:
    if record.original_unique == 0:
        return None, None
    expected = retention**4
    tolerance = (
        6.0
        * math.sqrt(expected * (1.0 - expected) / record.original_unique)
        + 1.0 / record.original_unique
    )
    observed = record.endpoint_survive / record.original_unique
    return tolerance, abs(observed - expected) <= tolerance


def thinning_rows(
    records: dict[tuple[str, int, float], ThinningCounts]
) -> tuple[list[dict[str, object]], bool]:
    rows: list[dict[str, object]] = []
    all_executable_controls_pass = True
    for name in SELECTORS:
        for n in BASE_N:
            for retention in RETENTION:
                record = records[(name, n, retention)]
                tolerance, control_pass = _survival_control(record, retention)
                if control_pass is not None:
                    all_executable_controls_pass &= control_pass
                same_low, same_high = _wilson(
                    record.exact_reselected, record.endpoint_survive
                )
                rows.append(
                    {
                        "selector": name,
                        "n": n,
                        "retention": retention,
                        "original_unique_count": record.original_unique,
                        "endpoint_survive_count": record.endpoint_survive,
                        "endpoint_survive_fraction": (
                            record.endpoint_survive / record.original_unique
                            if record.original_unique
                            else None
                        ),
                        "endpoint_survive_expected": retention**4,
                        "survival_control_tolerance": tolerance,
                        "survival_control_pass": control_pass,
                        "thinned_unique_count": record.thinned_unique,
                        "thinned_unique_given_survival_count": (
                            record.thinned_unique_given_survival
                        ),
                        "p_thinned_unique_given_survival": (
                            record.thinned_unique_given_survival
                            / record.endpoint_survive
                            if record.endpoint_survive
                            else None
                        ),
                        "exact_reselected_count": record.exact_reselected,
                        "p_same_given_survival": (
                            record.exact_reselected / record.endpoint_survive
                            if record.endpoint_survive
                            else None
                        ),
                        "p_same_ci95_low": same_low,
                        "p_same_ci95_high": same_high,
                        "p_same_unconditional": (
                            record.exact_reselected / record.original_unique
                            if record.original_unique
                            else None
                        ),
                    }
                )
    return rows, all_executable_controls_pass


def paired_rows(records: dict[tuple[int, str, str], PairCounts]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n in BASE_N:
        for i in range(len(SELECTORS)):
            for j in range(i + 1, len(SELECTORS)):
                a_name, b_name = SELECTORS[i], SELECTORS[j]
                record = records[(n, a_name, b_name)]
                rows.append(
                    {
                        "n": n,
                        "selector_a": a_name,
                        "selector_b": b_name,
                        "replicates": record.replicates,
                        "a_unique_count": record.a_unique,
                        "b_unique_count": record.b_unique,
                        "both_unique_count": record.both_unique,
                        "a_only_unique_count": record.a_unique - record.both_unique,
                        "b_only_unique_count": record.b_unique - record.both_unique,
                        "same_quadruple_count": record.same_quadruple,
                        "p_same_quadruple_given_both_unique": (
                            record.same_quadruple / record.both_unique
                            if record.both_unique
                            else None
                        ),
                    }
                )
    return rows


def scientific_terminal(
    selectors: Sequence[dict[str, object]],
    thinning: Sequence[dict[str, object]],
) -> tuple[str, str | None, dict[str, object]]:
    selector_by_key = {
        (str(row["selector"]), int(row["n"])): row for row in selectors
    }
    thinning_by_key = {
        (str(row["selector"]), int(row["n"]), float(row["retention"])): row
        for row in thinning
    }
    gate: dict[str, object] = {}
    qualifies: dict[str, bool] = {}
    for name in CANDIDATES:
        candidate_gate: dict[str, object] = {}
        qualifies_all = True
        for n in GATE_N:
            base = selector_by_key[(name, n)]
            thin_090 = thinning_by_key[(name, n, 0.90)]
            thin_080 = thinning_by_key[(name, n, 0.80)]
            values_defined = all(
                value is not None
                for value in (
                    base["p_unique_ci95_low"],
                    base["p_floor_ci95_high"],
                    thin_090["p_same_ci95_low"],
                    thin_080["p_same_ci95_low"],
                )
            )
            qualifies_n = bool(
                values_defined
                and float(base["p_unique_ci95_low"]) >= QUALIFY_UNIQUE_LOWER
                and float(thin_090["p_same_ci95_low"])
                >= QUALIFY_SAME_090_LOWER
                and float(thin_080["p_same_ci95_low"])
                >= QUALIFY_SAME_080_LOWER
                and float(base["p_floor_ci95_high"]) < QUALIFY_FLOOR_UPPER
            )
            qualifies_all &= qualifies_n
            candidate_gate[str(n)] = {
                "p_unique": base["p_unique"],
                "p_unique_wilson95_low": base["p_unique_ci95_low"],
                "p_floor": base["p_floor"],
                "p_floor_wilson95_high": base["p_floor_ci95_high"],
                "p_same_090": thin_090["p_same_given_survival"],
                "p_same_090_wilson95_low": thin_090["p_same_ci95_low"],
                "p_same_080": thin_080["p_same_given_survival"],
                "p_same_080_wilson95_low": thin_080["p_same_ci95_low"],
                "qualifies_n": qualifies_n,
            }
        qualifies[name] = qualifies_all
        gate[name] = {
            "qualifies_all_gate_n": qualifies_all,
            "by_n": candidate_gate,
        }

    if qualifies[MIN_ONLY]:
        return TERMINAL_SELECT_MIN, MIN_ONLY, gate
    if qualifies[MIN_COVERAGE_LEX]:
        return TERMINAL_SELECT_LEX, MIN_COVERAGE_LEX, gate
    return TERMINAL_NONE, None, gate


def _format_value(value: object) -> object:
    if value is None:
        return ""
    if isinstance(value, float):
        return format(value, ".12g")
    if isinstance(value, bool):
        return str(value).upper()
    return value


def rows_to_csv(rows: Sequence[dict[str, object]], fields: Sequence[str]) -> str:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({field: _format_value(row[field]) for field in fields})
    return buffer.getvalue()


def _atomic_write(path: Path, data: bytes, *, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"refusing to overwrite existing artifact: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    temporary.write_bytes(data)
    temporary.replace(path)


def _write_with_sidecar(path: Path, data: bytes, *, overwrite: bool) -> str:
    digest = hashlib.sha256(data).hexdigest()
    _atomic_write(path, data, overwrite=overwrite)
    _atomic_write(
        path.with_suffix(path.suffix + ".sha256"),
        f"{digest}  {path.name}\n".encode("utf-8"),
        overwrite=overwrite,
    )
    return digest


def contract_dict() -> dict[str, object]:
    return {
        "dimension": 2,
        "k0": sealed.K0,
        "selectors": list(SELECTORS),
        "candidates": list(CANDIDATES),
        "base_n": list(BASE_N),
        "gate_n": list(GATE_N),
        "base_replicates_per_n": BASE_REPLICATES_PER_N,
        "base_batches": BASE_BATCHES,
        "base_replicates_per_batch": BASE_REPLICATES_PER_BATCH,
        "retention": list(RETENTION),
        "rng": "numpy.random.Generator(numpy.random.PCG64)",
        "coordinate_seed_base": COORDINATE_SEED_BASE,
        "coordinate_seed_formula": "COORDINATE_SEED_BASE + 100*n + batch",
        "thinning_seed_base": THINNING_SEED_BASE,
        "thinning_seed_formula": "THINNING_SEED_BASE + 100*n + batch",
        "boundary_delta": BOUNDARY_DELTA,
        "qualify_unique_lower": QUALIFY_UNIQUE_LOWER,
        "qualify_same_090_lower": QUALIFY_SAME_090_LOWER,
        "qualify_same_080_lower": QUALIFY_SAME_080_LOWER,
        "qualify_floor_upper": QUALIFY_FLOOR_UPPER,
        "priority": [MIN_ONLY, MIN_COVERAGE_LEX],
    }


def execute(output_dir: Path, *, overwrite: bool = False) -> dict[str, object]:
    filenames = (
        SELECTOR_FILENAME,
        THINNING_FILENAME,
        PAIRED_FILENAME,
        SUMMARY_FILENAME,
    )
    prospective = tuple(
        path
        for filename in filenames
        for path in (
            output_dir / filename,
            (output_dir / filename).with_suffix(
                (output_dir / filename).suffix + ".sha256"
            ),
        )
    )
    if not overwrite:
        existing = [str(path) for path in prospective if path.exists()]
        if existing:
            raise FileExistsError("refusing to overwrite: " + ", ".join(existing))

    accumulators, thinning_counts, pair_counts = simulate()
    selector_table = selector_rows(accumulators)
    thinning_table, survival_controls_pass = thinning_rows(thinning_counts)
    paired_table = paired_rows(pair_counts)

    selector_data = rows_to_csv(selector_table, SELECTOR_FIELDS).encode("utf-8")
    thinning_data = rows_to_csv(thinning_table, THINNING_FIELDS).encode("utf-8")
    paired_data = rows_to_csv(paired_table, PAIRED_FIELDS).encode("utf-8")
    selector_sha = _write_with_sidecar(
        output_dir / SELECTOR_FILENAME, selector_data, overwrite=overwrite
    )
    thinning_sha = _write_with_sidecar(
        output_dir / THINNING_FILENAME, thinning_data, overwrite=overwrite
    )
    paired_sha = _write_with_sidecar(
        output_dir / PAIRED_FILENAME, paired_data, overwrite=overwrite
    )

    if survival_controls_pass:
        terminal, selected_candidate, gate = scientific_terminal(
            selector_table, thinning_table
        )
    else:
        terminal, selected_candidate, gate = TERMINAL_INVALID, None, {}

    summary: dict[str, object] = {
        "schema_version": "p1a_balanced_selector_comparison_d2_v1",
        "contract_status": "FROZEN_BEFORE_RESULTS",
        "terminal": terminal,
        "selected_candidate": selected_candidate,
        "survival_controls_pass": survival_controls_pass,
        "contract": contract_dict(),
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "artifacts": {
            SELECTOR_FILENAME: {"sha256": selector_sha},
            THINNING_FILENAME: {"sha256": thinning_sha},
            PAIRED_FILENAME: {"sha256": paired_sha},
        },
        "selectors": selector_table,
        "thinning": thinning_table,
        "paired": paired_table,
        "gate": gate,
        "claim_ceiling": "D2_SELECTOR_COMPARISON_NO_HEIGHT_RATIO",
    }
    summary_data = (json.dumps(summary, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )
    summary_sha = _write_with_sidecar(
        output_dir / SUMMARY_FILENAME, summary_data, overwrite=overwrite
    )
    summary["summary_sha256"] = summary_sha

    print(f"P1A_COMPARE_SURVIVAL_CONTROLS_PASS={str(survival_controls_pass).upper()}")
    print(f"P1A_COMPARE_TERMINAL={terminal}")
    print(f"P1A_COMPARE_SELECTED_CANDIDATE={selected_candidate or 'NONE'}")
    print(f"P1A_COMPARE_SELECTOR_SHA256={selector_sha}")
    print(f"P1A_COMPARE_THINNING_SHA256={thinning_sha}")
    print(f"P1A_COMPARE_PAIRED_SHA256={paired_sha}")
    print(f"P1A_COMPARE_SUMMARY_SHA256={summary_sha}")
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="artifact directory"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="explicitly replace existing generated artifacts",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        summary = execute(args.output_dir, overwrite=args.overwrite)
    except (FileExistsError, RuntimeError, ValueError) as exc:
        print(f"P1A_COMPARE_TERMINAL={TERMINAL_INVALID}", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 2
    return 2 if summary["terminal"] == TERMINAL_INVALID else 0


if __name__ == "__main__":
    raise SystemExit(main())
