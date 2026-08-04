#!/usr/bin/env python3
"""P1a d=2 stability and post-selection diagnostics under frozen contract v1.0.

Selection uses only the product order represented by a permutation. Latent
coordinates, thinning labels and heights are evaluated only after selection.
No height ratio or metric claim is produced by this executable.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import io
import json
import math
import os
import platform
import statistics
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np

from emergencia import p1a_enumeracion_simulacion as selector


BASE_N = (32, 48, 64, 96, 128)
GATE_N = (64, 96, 128)
BASE_REPLICATES_PER_N = 12_000
BASE_BATCHES = 8
BASE_REPLICATES_PER_BATCH = 1_500
RETENTION = (0.90, 0.80)
COORDINATE_SEED_BASE = 2_608_035_000
THINNING_SEED_BASE = 2_608_036_000
BASELINE_SEED_BASE = 2_608_037_000
BASELINE_REPLICATES_PER_SIZE = 4_000
BOUNDARY_DELTA = 0.05
UNIFORM_BOUNDARY_REFERENCE = 1.0 - (1.0 - 2.0 * BOUNDARY_DELTA) ** 2

PASS_SAME_090_LOWER = 0.50
PASS_SAME_080_LOWER = 0.25
PASS_FLOOR_UPPER = 0.25
PARK_SAME_090_UPPER = 0.25
PARK_FLOOR_LOWER = 0.75

TERMINAL_PASS = "PASS_STABILITY_TO_P1B_DESIGN"
TERMINAL_PARK = "PARK_POINT_SELECTOR_INSTABILITY"
TERMINAL_INCONCLUSIVE = "INCONCLUSIVE_STABILITY_GATE"
TERMINAL_INVALID = "IMPLEMENTATION_INVALID"

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = HERE / "resultados"
STABILITY_FILENAME = "p1a_estabilidad_d2.csv"
THINNING_FILENAME = "p1a_thinning_d2.csv"
BASELINE_FILENAME = "p1a_alturas_baseline_d2.csv"
SUMMARY_FILENAME = "p1a_estabilidad_resumen.json"

STABILITY_FIELDS = (
    "n",
    "replicates",
    "unique_count",
    "p_unique",
    "p_unique_ci95_low",
    "p_unique_ci95_high",
    "selected_interval_count",
    "past_size_mean",
    "future_size_mean",
    "min_size_mean",
    "min_size_median",
    "floor_count",
    "p_floor",
    "p_floor_ci95_low",
    "p_floor_ci95_high",
    "balance_mean",
    "balance_median",
    "selected_endpoint_count",
    "near_boundary_endpoint_count",
    "near_boundary_endpoint_fraction",
    "uniform_boundary_reference",
    "boundary_enrichment",
    "endpoint_clearance_mean",
    "height_residual_count",
    "height_residual_mean",
    "height_residual_standard_error",
    "past_height_residual_mean",
    "future_height_residual_mean",
)

THINNING_FIELDS = (
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

BASELINE_FIELDS = (
    "interval_size",
    "baseline_replicates",
    "baseline_mean_height",
    "baseline_sd_height",
    "baseline_standard_error",
    "selected_interval_count",
    "selected_mean_height",
    "selected_mean_residual",
)


@dataclass(frozen=True)
class UniqueSelection:
    quadruple: tuple[int, int, int, int]
    past_size: int
    future_size: int
    score: int


@dataclass(frozen=True)
class SelectedInterval:
    n: int
    side: str
    size: int
    height: int


@dataclass
class ThinningCounts:
    original_unique: int = 0
    endpoint_survive: int = 0
    thinned_unique: int = 0
    thinned_unique_given_survival: int = 0
    exact_reselected: int = 0


@dataclass
class BaseAccumulator:
    n: int
    replicates: int = 0
    unique_count: int = 0
    past_sizes: list[int] | None = None
    future_sizes: list[int] | None = None
    min_sizes: list[int] | None = None
    balances: list[float] | None = None
    endpoint_clearances: list[float] | None = None
    selected_intervals: list[SelectedInterval] | None = None

    def __post_init__(self) -> None:
        self.past_sizes = []
        self.future_sizes = []
        self.min_sizes = []
        self.balances = []
        self.endpoint_clearances = []
        self.selected_intervals = []


def coordinate_seed(n: int, batch: int) -> int:
    if n not in BASE_N or not 0 <= batch < BASE_BATCHES:
        raise ValueError("coordinate seed outside frozen contract")
    return COORDINATE_SEED_BASE + 100 * n + batch


def thinning_seed(n: int, batch: int) -> int:
    if n not in BASE_N or not 0 <= batch < BASE_BATCHES:
        raise ValueError("thinning seed outside frozen contract")
    return THINNING_SEED_BASE + 100 * n + batch


def baseline_seed(interval_size: int) -> int:
    if interval_size < selector.K0:
        raise ValueError("baseline interval below k0")
    return BASELINE_SEED_BASE + interval_size


def product_permutation(
    u: Sequence[float], v: Sequence[float]
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Sort latent points by u and return u, v and v-rank permutation."""

    u_array = np.asarray(u, dtype=np.float64)
    v_array = np.asarray(v, dtype=np.float64)
    if u_array.ndim != 1 or v_array.shape != u_array.shape or len(u_array) == 0:
        raise ValueError("u and v must be nonempty vectors of equal length")
    if len(np.unique(u_array)) != len(u_array) or len(np.unique(v_array)) != len(v_array):
        raise ValueError("latent coordinate ties are outside the continuous model")
    order = np.argsort(u_array)
    u_sorted = u_array[order]
    v_sorted = v_array[order]
    permutation = np.empty(len(order), dtype=np.int64)
    permutation[np.argsort(v_sorted)] = np.arange(len(order), dtype=np.int64)
    return u_sorted, v_sorted, permutation


def select_unique_quadruple(permutation: Sequence[int]) -> UniqueSelection | None:
    """Return the sole F_cov,3 maximizing quadruple, otherwise abstain."""

    counts, comparable = selector.interval_count_matrix(permutation)
    eligible = counts >= selector.K0

    left_values = np.where(eligible, counts, -1)
    left_max = left_values.max(axis=0)
    left_mult = ((counts == left_max[None, :]) & eligible).sum(axis=0)

    right_values = np.where(eligible, counts, -1)
    right_max = right_values.max(axis=1)
    right_mult = ((counts == right_max[:, None]) & eligible).sum(axis=1)

    bridges = comparable & (left_max[:, None] >= selector.K0) & (
        right_max[None, :] >= selector.K0
    )
    if not bool(bridges.any()):
        return None

    bridge_scores = left_max[:, None] + right_max[None, :]
    max_score = int(bridge_scores[bridges].max())
    maximizing_bridges = bridges & (bridge_scores == max_score)
    bridge_rows, bridge_cols = np.nonzero(maximizing_bridges)
    if len(bridge_rows) != 1:
        return None
    b = int(bridge_rows[0])
    c = int(bridge_cols[0])
    if int(left_mult[b]) != 1 or int(right_mult[c]) != 1:
        return None

    past = np.flatnonzero(eligible[:, b] & (counts[:, b] == left_max[b]))
    future = np.flatnonzero(eligible[c, :] & (counts[c, :] == right_max[c]))
    if len(past) != 1 or len(future) != 1:
        raise RuntimeError("unique multiplicity did not identify unique endpoints")
    a = int(past[0])
    d = int(future[0])
    return UniqueSelection(
        quadruple=(a, b, c, d),
        past_size=int(counts[a, b]),
        future_size=int(counts[c, d]),
        score=max_score,
    )


def induced_permutation(
    permutation: Sequence[int], retained: Sequence[int]
) -> np.ndarray:
    perm = selector.validate_permutation(permutation)
    kept = np.asarray(retained, dtype=np.int64)
    if kept.ndim != 1 or len(np.unique(kept)) != len(kept):
        raise ValueError("retained indices must be a unique vector")
    if len(kept) == 0:
        return np.array([], dtype=np.int64)
    if np.any(kept < 0) or np.any(kept >= len(perm)) or np.any(kept[:-1] >= kept[1:]):
        raise ValueError("retained indices must be strictly increasing and in range")
    values = perm[kept]
    induced = np.empty(len(values), dtype=np.int64)
    induced[np.argsort(values)] = np.arange(len(values), dtype=np.int64)
    return induced


def lis_length(values: Iterable[int]) -> int:
    tails: list[int] = []
    for value in values:
        position = bisect.bisect_left(tails, int(value))
        if position == len(tails):
            tails.append(int(value))
        else:
            tails[position] = int(value)
    return len(tails)


def interval_height(permutation: Sequence[int], start: int, stop: int) -> tuple[int, int]:
    perm = selector.validate_permutation(permutation)
    if not (0 <= start < stop < len(perm) and perm[start] < perm[stop]):
        raise ValueError("interval endpoints must be comparable and ordered")
    segment = perm[start : stop + 1]
    inside = segment[(segment >= perm[start]) & (segment <= perm[stop])]
    return lis_length(inside), len(inside)


def _mean(values: Sequence[float] | Sequence[int]) -> float:
    return float(statistics.fmean(values)) if values else math.nan


def _median(values: Sequence[float] | Sequence[int]) -> float:
    return float(statistics.median(values)) if values else math.nan


def simulate_base(
    n_values: Iterable[int] = BASE_N,
) -> tuple[list[BaseAccumulator], dict[tuple[int, float], ThinningCounts]]:
    accumulators: list[BaseAccumulator] = []
    thinning: dict[tuple[int, float], ThinningCounts] = {}

    for n in n_values:
        accumulator = BaseAccumulator(n=n)
        for retention in RETENTION:
            thinning[(n, retention)] = ThinningCounts()

        for batch in range(BASE_BATCHES):
            coordinate_rng = np.random.Generator(
                np.random.PCG64(coordinate_seed(n, batch))
            )
            thinning_rng = np.random.Generator(np.random.PCG64(thinning_seed(n, batch)))
            for _ in range(BASE_REPLICATES_PER_BATCH):
                u_sorted, v_sorted, permutation = product_permutation(
                    coordinate_rng.random(n), coordinate_rng.random(n)
                )
                masks = {
                    retention: thinning_rng.random(n) < retention
                    for retention in RETENTION
                }
                accumulator.replicates += 1
                selected = select_unique_quadruple(permutation)
                if selected is None:
                    continue

                accumulator.unique_count += 1
                a, b, c, d = selected.quadruple
                assert accumulator.past_sizes is not None
                assert accumulator.future_sizes is not None
                assert accumulator.min_sizes is not None
                assert accumulator.balances is not None
                assert accumulator.endpoint_clearances is not None
                assert accumulator.selected_intervals is not None
                accumulator.past_sizes.append(selected.past_size)
                accumulator.future_sizes.append(selected.future_size)
                accumulator.min_sizes.append(
                    min(selected.past_size, selected.future_size)
                )
                accumulator.balances.append(
                    min(selected.past_size, selected.future_size)
                    / max(selected.past_size, selected.future_size)
                )

                for endpoint in selected.quadruple:
                    accumulator.endpoint_clearances.append(
                        min(
                            float(u_sorted[endpoint]),
                            1.0 - float(u_sorted[endpoint]),
                            float(v_sorted[endpoint]),
                            1.0 - float(v_sorted[endpoint]),
                        )
                    )

                past_height, past_count = interval_height(permutation, a, b)
                future_height, future_count = interval_height(permutation, c, d)
                if past_count != selected.past_size or future_count != selected.future_size:
                    raise RuntimeError("interval cardinality mismatch")
                accumulator.selected_intervals.extend(
                    (
                        SelectedInterval(n, "PAST", selected.past_size, past_height),
                        SelectedInterval(n, "FUTURE", selected.future_size, future_height),
                    )
                )

                for retention in RETENTION:
                    record = thinning[(n, retention)]
                    record.original_unique += 1
                    mask = masks[retention]
                    endpoints_survive = bool(mask[list(selected.quadruple)].all())
                    if endpoints_survive:
                        record.endpoint_survive += 1
                    retained = np.flatnonzero(mask)
                    if len(retained) < 2 * selector.K0:
                        continue
                    induced = induced_permutation(permutation, retained)
                    selected_thin = select_unique_quadruple(induced)
                    if selected_thin is None:
                        continue
                    record.thinned_unique += 1
                    if endpoints_survive:
                        record.thinned_unique_given_survival += 1
                    mapped = tuple(int(retained[index]) for index in selected_thin.quadruple)
                    if mapped == selected.quadruple:
                        if not endpoints_survive:
                            raise RuntimeError("reselected endpoint did not survive thinning")
                        record.exact_reselected += 1

        if accumulator.replicates != BASE_REPLICATES_PER_N:
            raise RuntimeError(f"base replicate mismatch at n={n}")
        if any(
            thinning[(n, retention)].original_unique != accumulator.unique_count
            for retention in RETENTION
        ):
            raise RuntimeError(f"thinning denominator mismatch at n={n}")
        accumulators.append(accumulator)
        print(
            f"P1A_STABILITY_N={n} REPLICATES={accumulator.replicates} "
            f"UNIQUE={accumulator.unique_count}",
            flush=True,
        )
    return accumulators, thinning


def simulate_height_baselines(
    interval_sizes: Iterable[int],
) -> dict[int, list[int]]:
    baselines: dict[int, list[int]] = {}
    for interval_size in sorted(set(interval_sizes)):
        rng = np.random.Generator(np.random.PCG64(baseline_seed(interval_size)))
        interior_size = interval_size - 2
        heights = [
            2 + lis_length(rng.permutation(interior_size))
            for _ in range(BASELINE_REPLICATES_PER_SIZE)
        ]
        if not all(3 <= height <= interval_size for height in heights):
            raise RuntimeError(f"invalid baseline height at m={interval_size}")
        baselines[interval_size] = heights
    return baselines


def survival_control(record: ThinningCounts, retention: float) -> tuple[float, bool]:
    if record.original_unique <= 0:
        raise RuntimeError("no unique selections for thinning control")
    expected = retention**4
    tolerance = (
        6.0
        * math.sqrt(expected * (1.0 - expected) / record.original_unique)
        + 1.0 / record.original_unique
    )
    observed = record.endpoint_survive / record.original_unique
    return tolerance, abs(observed - expected) <= tolerance


def thinning_rows(
    records: dict[tuple[int, float], ThinningCounts]
) -> tuple[list[dict[str, object]], bool]:
    rows: list[dict[str, object]] = []
    controls_pass = True
    for n in BASE_N:
        for retention in RETENTION:
            record = records[(n, retention)]
            if record.endpoint_survive <= 0:
                raise RuntimeError("zero surviving-endpoint denominator")
            low, high = selector.wilson_interval(
                record.exact_reselected, record.endpoint_survive
            )
            tolerance, control_pass = survival_control(record, retention)
            controls_pass = controls_pass and control_pass
            rows.append(
                {
                    "n": n,
                    "retention": retention,
                    "original_unique_count": record.original_unique,
                    "endpoint_survive_count": record.endpoint_survive,
                    "endpoint_survive_fraction": (
                        record.endpoint_survive / record.original_unique
                    ),
                    "endpoint_survive_expected": retention**4,
                    "survival_control_tolerance": tolerance,
                    "survival_control_pass": control_pass,
                    "thinned_unique_count": record.thinned_unique,
                    "thinned_unique_given_survival_count": (
                        record.thinned_unique_given_survival
                    ),
                    "p_thinned_unique_given_survival": (
                        record.thinned_unique_given_survival / record.endpoint_survive
                    ),
                    "exact_reselected_count": record.exact_reselected,
                    "p_same_given_survival": (
                        record.exact_reselected / record.endpoint_survive
                    ),
                    "p_same_ci95_low": low,
                    "p_same_ci95_high": high,
                    "p_same_unconditional": (
                        record.exact_reselected / record.original_unique
                    ),
                }
            )
    return rows, controls_pass


def baseline_rows(
    selected_intervals: Sequence[SelectedInterval],
    baselines: dict[int, list[int]],
) -> list[dict[str, object]]:
    selected_by_size: dict[int, list[int]] = defaultdict(list)
    for interval in selected_intervals:
        selected_by_size[interval.size].append(interval.height)
    rows: list[dict[str, object]] = []
    for interval_size in sorted(baselines):
        baseline = baselines[interval_size]
        selected = selected_by_size[interval_size]
        baseline_mean = _mean(baseline)
        baseline_sd = statistics.stdev(baseline)
        rows.append(
            {
                "interval_size": interval_size,
                "baseline_replicates": len(baseline),
                "baseline_mean_height": baseline_mean,
                "baseline_sd_height": baseline_sd,
                "baseline_standard_error": baseline_sd / math.sqrt(len(baseline)),
                "selected_interval_count": len(selected),
                "selected_mean_height": _mean(selected),
                "selected_mean_residual": _mean(selected) - baseline_mean,
            }
        )
    return rows


def stability_rows(
    accumulators: Sequence[BaseAccumulator],
    baseline_means: dict[int, float],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for accumulator in accumulators:
        assert accumulator.past_sizes is not None
        assert accumulator.future_sizes is not None
        assert accumulator.min_sizes is not None
        assert accumulator.balances is not None
        assert accumulator.endpoint_clearances is not None
        assert accumulator.selected_intervals is not None
        unique_low, unique_high = selector.wilson_interval(
            accumulator.unique_count, accumulator.replicates
        )
        floor_count = sum(size == selector.K0 for size in accumulator.min_sizes)
        floor_low, floor_high = selector.wilson_interval(
            floor_count, accumulator.unique_count
        )
        residuals = [
            interval.height - baseline_means[interval.size]
            for interval in accumulator.selected_intervals
        ]
        past_residuals = [
            interval.height - baseline_means[interval.size]
            for interval in accumulator.selected_intervals
            if interval.side == "PAST"
        ]
        future_residuals = [
            interval.height - baseline_means[interval.size]
            for interval in accumulator.selected_intervals
            if interval.side == "FUTURE"
        ]
        residual_se = (
            statistics.stdev(residuals) / math.sqrt(len(residuals))
            if len(residuals) > 1
            else math.nan
        )
        near_count = sum(
            clearance <= BOUNDARY_DELTA
            for clearance in accumulator.endpoint_clearances
        )
        boundary_fraction = near_count / len(accumulator.endpoint_clearances)
        rows.append(
            {
                "n": accumulator.n,
                "replicates": accumulator.replicates,
                "unique_count": accumulator.unique_count,
                "p_unique": accumulator.unique_count / accumulator.replicates,
                "p_unique_ci95_low": unique_low,
                "p_unique_ci95_high": unique_high,
                "selected_interval_count": len(accumulator.selected_intervals),
                "past_size_mean": _mean(accumulator.past_sizes),
                "future_size_mean": _mean(accumulator.future_sizes),
                "min_size_mean": _mean(accumulator.min_sizes),
                "min_size_median": _median(accumulator.min_sizes),
                "floor_count": floor_count,
                "p_floor": floor_count / accumulator.unique_count,
                "p_floor_ci95_low": floor_low,
                "p_floor_ci95_high": floor_high,
                "balance_mean": _mean(accumulator.balances),
                "balance_median": _median(accumulator.balances),
                "selected_endpoint_count": len(accumulator.endpoint_clearances),
                "near_boundary_endpoint_count": near_count,
                "near_boundary_endpoint_fraction": boundary_fraction,
                "uniform_boundary_reference": UNIFORM_BOUNDARY_REFERENCE,
                "boundary_enrichment": (
                    boundary_fraction / UNIFORM_BOUNDARY_REFERENCE
                ),
                "endpoint_clearance_mean": _mean(accumulator.endpoint_clearances),
                "height_residual_count": len(residuals),
                "height_residual_mean": _mean(residuals),
                "height_residual_standard_error": residual_se,
                "past_height_residual_mean": _mean(past_residuals),
                "future_height_residual_mean": _mean(future_residuals),
            }
        )
    return rows


def scientific_terminal(
    stability: Sequence[dict[str, object]],
    thinning: Sequence[dict[str, object]],
) -> tuple[str, dict[str, object]]:
    stability_by_n = {int(row["n"]): row for row in stability}
    thinning_by_key = {
        (int(row["n"]), float(row["retention"])): row for row in thinning
    }
    gate: dict[str, object] = {}
    pass_all = True
    park_all = True
    for n in GATE_N:
        floor = stability_by_n[n]
        same_090 = thinning_by_key[(n, 0.90)]
        same_080 = thinning_by_key[(n, 0.80)]
        pass_n = (
            float(same_090["p_same_ci95_low"]) >= PASS_SAME_090_LOWER
            and float(same_080["p_same_ci95_low"]) >= PASS_SAME_080_LOWER
            and float(floor["p_floor_ci95_high"]) < PASS_FLOOR_UPPER
        )
        park_n = (
            float(same_090["p_same_ci95_high"]) < PARK_SAME_090_UPPER
            or float(floor["p_floor_ci95_low"]) > PARK_FLOOR_LOWER
        )
        pass_all = pass_all and pass_n
        park_all = park_all and park_n
        gate[str(n)] = {
            "p_same_090": same_090["p_same_given_survival"],
            "p_same_090_wilson95_low": same_090["p_same_ci95_low"],
            "p_same_090_wilson95_high": same_090["p_same_ci95_high"],
            "p_same_080": same_080["p_same_given_survival"],
            "p_same_080_wilson95_low": same_080["p_same_ci95_low"],
            "p_same_080_wilson95_high": same_080["p_same_ci95_high"],
            "p_floor": floor["p_floor"],
            "p_floor_wilson95_low": floor["p_floor_ci95_low"],
            "p_floor_wilson95_high": floor["p_floor_ci95_high"],
            "pass_n": pass_n,
            "park_n": park_n,
        }
    if pass_all:
        return TERMINAL_PASS, gate
    if park_all:
        return TERMINAL_PARK, gate
    return TERMINAL_INCONCLUSIVE, gate


def _format_value(value: object) -> object:
    if isinstance(value, float):
        if math.isnan(value):
            return ""
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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _atomic_write(path: Path, data: bytes, *, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"refusing to overwrite existing artifact: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    temporary.write_bytes(data)
    temporary.replace(path)


def _write_with_sidecar(path: Path, data: bytes, *, overwrite: bool) -> str:
    digest = sha256_bytes(data)
    _atomic_write(path, data, overwrite=overwrite)
    _atomic_write(
        path.with_suffix(path.suffix + ".sha256"),
        f"{digest}  {path.name}\n".encode("utf-8"),
        overwrite=overwrite,
    )
    return digest


def contract_dict() -> dict[str, object]:
    return {
        "k0": selector.K0,
        "dimension": 2,
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
        "baseline_seed_base": BASELINE_SEED_BASE,
        "baseline_seed_formula": "BASELINE_SEED_BASE + interval_size",
        "baseline_replicates_per_size": BASELINE_REPLICATES_PER_SIZE,
        "boundary_delta": BOUNDARY_DELTA,
        "pass_same_090_lower": PASS_SAME_090_LOWER,
        "pass_same_080_lower": PASS_SAME_080_LOWER,
        "pass_floor_upper": PASS_FLOOR_UPPER,
        "park_same_090_upper": PARK_SAME_090_UPPER,
        "park_floor_lower": PARK_FLOOR_LOWER,
    }


def execute(output_dir: Path, *, overwrite: bool = False) -> dict[str, object]:
    filenames = (
        STABILITY_FILENAME,
        THINNING_FILENAME,
        BASELINE_FILENAME,
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

    accumulators, thinning_counts = simulate_base()
    all_intervals = [
        interval
        for accumulator in accumulators
        for interval in (accumulator.selected_intervals or [])
    ]
    baselines = simulate_height_baselines(interval.size for interval in all_intervals)
    baseline_means = {size: _mean(heights) for size, heights in baselines.items()}
    baseline_table = baseline_rows(all_intervals, baselines)
    stability_table = stability_rows(accumulators, baseline_means)
    thinning_table, survival_controls_pass = thinning_rows(thinning_counts)

    stability_data = rows_to_csv(stability_table, STABILITY_FIELDS).encode("utf-8")
    thinning_data = rows_to_csv(thinning_table, THINNING_FIELDS).encode("utf-8")
    baseline_data = rows_to_csv(baseline_table, BASELINE_FIELDS).encode("utf-8")
    stability_sha = _write_with_sidecar(
        output_dir / STABILITY_FILENAME, stability_data, overwrite=overwrite
    )
    thinning_sha = _write_with_sidecar(
        output_dir / THINNING_FILENAME, thinning_data, overwrite=overwrite
    )
    baseline_sha = _write_with_sidecar(
        output_dir / BASELINE_FILENAME, baseline_data, overwrite=overwrite
    )

    if survival_controls_pass:
        terminal, gate = scientific_terminal(stability_table, thinning_table)
    else:
        terminal, gate = TERMINAL_INVALID, {}

    summary: dict[str, object] = {
        "schema_version": "p1a_stability_d2_v1",
        "contract_status": "FROZEN_BEFORE_RESULTS",
        "terminal": terminal,
        "survival_controls_pass": survival_controls_pass,
        "contract": contract_dict(),
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "artifacts": {
            STABILITY_FILENAME: {"sha256": stability_sha},
            THINNING_FILENAME: {"sha256": thinning_sha},
            BASELINE_FILENAME: {"sha256": baseline_sha},
        },
        "stability": stability_table,
        "thinning": thinning_table,
        "gate": gate,
        "claim_ceiling": "D2_SELECTOR_STABILITY_DIAGNOSTICS_NO_METRIC_RATIO",
    }
    summary_data = (json.dumps(summary, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )
    summary_sha = _write_with_sidecar(
        output_dir / SUMMARY_FILENAME, summary_data, overwrite=overwrite
    )
    summary["summary_sha256"] = summary_sha

    print(f"P1A_SURVIVAL_CONTROLS_PASS={str(survival_controls_pass).upper()}")
    print(f"P1A_STABILITY_TERMINAL={terminal}")
    print(f"P1A_STABILITY_SHA256={stability_sha}")
    print(f"P1A_THINNING_SHA256={thinning_sha}")
    print(f"P1A_BASELINE_SHA256={baseline_sha}")
    print(f"P1A_STABILITY_SUMMARY_SHA256={summary_sha}")
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
        print(f"P1A_STABILITY_TERMINAL={TERMINAL_INVALID}", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 2
    return 2 if summary["terminal"] == TERMINAL_INVALID else 0


if __name__ == "__main__":
    raise SystemExit(main())
