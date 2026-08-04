#!/usr/bin/env python3
"""Height-duration gate for the selected MIN_COVERAGE_LEX rule in d=2.

The selector sees only the product order. Latent null durations are used after
selection to evaluate each interval separately. No past/future ratio is computed.
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
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import numpy as np

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_estabilidad_d2 as previous


PAST = "PAST"
FUTURE = "FUTURE"
SIDES = (PAST, FUTURE)
SIDE_CODE = {PAST: 0, FUTURE: 1}

BASE_N = (64, 96, 128)
BASE_REPLICATES_PER_N = 12_000
BASE_BATCHES = 8
BASE_REPLICATES_PER_BATCH = 1_500
RETENTION = (0.90, 0.80)
COORDINATE_SEED_BASE = 2_608_040_000
THINNING_SEED_BASE = 2_608_041_000
BASELINE_SEED_BASE = 2_608_042_000
BASELINE_REPLICATES_PER_SIZE = 4_000
BOOTSTRAP_SEED_BASE = 2_608_043_000
BOOTSTRAP_REPLICATES = 1_000

HEIGHT_RESIDUAL_LIMIT = 0.50
CORRELATION_LOWER = 0.80
MEDIAN_RELATIVE_ERROR_UPPER = 0.30
TARGET_090_LOWER = 0.50
TARGET_080_LOWER = 0.35
PARK_CORRELATION_UPPER = 0.50
PARK_RELATIVE_ERROR_LOWER = 0.50
TARGET_FACTOR_PRIMARY = 1.25
TARGET_FACTOR_SECONDARY = 1.50

TERMINAL_PASS = "PASS_LEX_TO_PREREGISTER_HEIGHT_RATIO_D2"
TERMINAL_PARK = "PARK_LEX_HEIGHT_REPRESENTATION"
TERMINAL_INCONCLUSIVE = "INCONCLUSIVE_LEX_HEIGHT_GATE"
TERMINAL_INVALID = "IMPLEMENTATION_INVALID"

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = HERE / "resultados"
INTERVAL_FILENAME = "p1a_lex_intervalos_d2.csv"
CALIBRATION_FILENAME = "p1a_lex_altura_calibracion_d2.csv"
BASELINE_FILENAME = "p1a_lex_altura_baseline_por_tamano_d2.csv"
THINNING_FILENAME = "p1a_lex_target_thinning_d2.csv"
SUMMARY_FILENAME = "p1a_lex_altura_duracion_resumen.json"

INTERVAL_FIELDS = (
    "n",
    "replicate",
    "side",
    "interval_size",
    "height",
    "latent_duration",
    "height_duration_estimate",
    "signed_duration_error",
    "absolute_relative_error",
    "baseline_mean_height",
    "height_residual",
)

CALIBRATION_FIELDS = (
    "n",
    "side",
    "selected_count",
    "interval_size_mean",
    "interval_size_median",
    "height_mean",
    "height_sd",
    "height_cv",
    "height_residual_mean",
    "height_residual_bootstrap95_low",
    "height_residual_bootstrap95_high",
    "latent_duration_mean",
    "height_duration_estimate_mean",
    "duration_bias_mean",
    "duration_mae",
    "duration_rmse",
    "median_absolute_relative_error",
    "median_are_bootstrap95_low",
    "median_are_bootstrap95_high",
    "pearson_correlation",
    "pearson_bootstrap95_low",
    "pearson_bootstrap95_high",
    "ols_slope",
    "ols_intercept",
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

THINNING_FIELDS = (
    "n",
    "retention",
    "base_unique_count",
    "both_unique_count",
    "p_both_unique_given_base_unique",
    "exact_reselected_count",
    "p_exact_reselected_given_both_unique",
    "target_within_25_count",
    "p_target_within_25",
    "p_target_within_25_ci95_low",
    "p_target_within_25_ci95_high",
    "target_within_50_count",
    "p_target_within_50",
    "log_drift_mean",
    "log_drift_median",
    "log_drift_p90",
)


@dataclass(frozen=True)
class IntervalRecord:
    n: int
    replicate: int
    side: str
    interval_size: int
    height: int
    latent_duration: float
    height_duration_estimate: float


@dataclass
class TargetThinning:
    base_unique: int = 0
    both_unique: int = 0
    exact_reselected: int = 0
    log_drifts: list[float] | None = None

    def __post_init__(self) -> None:
        self.log_drifts = []


def coordinate_seed(n: int, batch: int) -> int:
    if n not in BASE_N or not 0 <= batch < BASE_BATCHES:
        raise ValueError("coordinate seed outside frozen contract")
    return COORDINATE_SEED_BASE + 100 * n + batch


def thinning_seed(n: int, batch: int) -> int:
    if n not in BASE_N or not 0 <= batch < BASE_BATCHES:
        raise ValueError("thinning seed outside frozen contract")
    return THINNING_SEED_BASE + 100 * n + batch


def baseline_seed(interval_size: int) -> int:
    if interval_size < sealed.K0:
        raise ValueError("baseline interval below k0")
    return BASELINE_SEED_BASE + interval_size


def bootstrap_seed(n: int, side: str) -> int:
    if n not in BASE_N or side not in SIDES:
        raise ValueError("bootstrap seed outside frozen contract")
    return BOOTSTRAP_SEED_BASE + 100 * n + SIDE_CODE[side]


def latent_duration(
    u_sorted: Sequence[float],
    v_sorted: Sequence[float],
    start: int,
    stop: int,
) -> float:
    u = np.asarray(u_sorted, dtype=np.float64)
    v = np.asarray(v_sorted, dtype=np.float64)
    if u.shape != v.shape or u.ndim != 1:
        raise ValueError("latent coordinates must be equal one-dimensional arrays")
    if not 0 <= start < stop < len(u):
        raise ValueError("invalid latent interval endpoints")
    du = float(u[stop] - u[start])
    dv = float(v[stop] - v[start])
    if du <= 0.0 or dv <= 0.0:
        raise ValueError("latent interval endpoints are not timelike ordered")
    return math.sqrt(du * dv)


def height_duration_estimate(height: int, n: int) -> float:
    if height < 2 or n <= 0:
        raise ValueError("invalid height or total cardinality")
    return height / (2.0 * math.sqrt(n))


def _selected_lex(permutation: Sequence[int]) -> comparison.Selection | None:
    outcome = comparison.evaluate_selectors(permutation)[comparison.MIN_COVERAGE_LEX]
    if outcome.state == comparison.STATE_UNIQUE:
        if outcome.selection is None:
            raise RuntimeError("unique lex outcome missing selection")
        return outcome.selection
    return None


def simulate_base() -> tuple[list[IntervalRecord], dict[tuple[int, float], TargetThinning]]:
    intervals: list[IntervalRecord] = []
    target = {
        (n, retention): TargetThinning()
        for n in BASE_N
        for retention in RETENTION
    }

    for n in BASE_N:
        unique_count = 0
        replicate = 0
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
                selected = _selected_lex(permutation)
                if selected is not None:
                    unique_count += 1
                    a, b, c, d = selected.quadruple
                    past_height, past_size = previous.interval_height(permutation, a, b)
                    future_height, future_size = previous.interval_height(
                        permutation, c, d
                    )
                    if (
                        past_size != selected.past_size
                        or future_size != selected.future_size
                    ):
                        raise RuntimeError("selected interval size mismatch")
                    past_duration = latent_duration(u_sorted, v_sorted, a, b)
                    future_duration = latent_duration(u_sorted, v_sorted, c, d)
                    intervals.extend(
                        (
                            IntervalRecord(
                                n,
                                replicate,
                                PAST,
                                past_size,
                                past_height,
                                past_duration,
                                height_duration_estimate(past_height, n),
                            ),
                            IntervalRecord(
                                n,
                                replicate,
                                FUTURE,
                                future_size,
                                future_height,
                                future_duration,
                                height_duration_estimate(future_height, n),
                            ),
                        )
                    )

                    base_durations = (past_duration, future_duration)
                    for retention in RETENTION:
                        record = target[(n, retention)]
                        record.base_unique += 1
                        retained = np.flatnonzero(masks[retention])
                        if len(retained) < 2 * sealed.K0:
                            continue
                        induced = previous.induced_permutation(permutation, retained)
                        selected_thin = _selected_lex(induced)
                        if selected_thin is None:
                            continue
                        record.both_unique += 1
                        mapped = tuple(
                            int(retained[index]) for index in selected_thin.quadruple
                        )
                        ta, tb, tc, td = mapped
                        thinned_durations = (
                            latent_duration(u_sorted, v_sorted, ta, tb),
                            latent_duration(u_sorted, v_sorted, tc, td),
                        )
                        assert record.log_drifts is not None
                        record.log_drifts.append(
                            max(
                                abs(
                                    math.log(
                                        thinned_durations[0] / base_durations[0]
                                    )
                                ),
                                abs(
                                    math.log(
                                        thinned_durations[1] / base_durations[1]
                                    )
                                ),
                            )
                        )
                        record.exact_reselected += int(mapped == selected.quadruple)
                replicate += 1

        if replicate != BASE_REPLICATES_PER_N:
            raise RuntimeError(f"replicate mismatch at n={n}")
        if len([row for row in intervals if row.n == n]) != 2 * unique_count:
            raise RuntimeError(f"interval row mismatch at n={n}")
        for retention in RETENTION:
            record = target[(n, retention)]
            if record.base_unique != unique_count:
                raise RuntimeError(f"thinning base denominator mismatch at n={n}")
            if record.log_drifts is None or len(record.log_drifts) != record.both_unique:
                raise RuntimeError(f"thinning drift denominator mismatch at n={n}")
        print(
            f"P1A_LEX_HEIGHT_N={n} REPLICATES={replicate} UNIQUE={unique_count}",
            flush=True,
        )
    return intervals, target


def simulate_baselines(interval_sizes: Sequence[int]) -> dict[int, list[int]]:
    baselines: dict[int, list[int]] = {}
    for interval_size in sorted(set(interval_sizes)):
        rng = np.random.Generator(np.random.PCG64(baseline_seed(interval_size)))
        interior_size = interval_size - 2
        heights = [
            2 + previous.lis_length(rng.permutation(interior_size))
            for _ in range(BASELINE_REPLICATES_PER_SIZE)
        ]
        if not all(3 <= height <= interval_size for height in heights):
            raise RuntimeError(f"invalid baseline height at m={interval_size}")
        baselines[interval_size] = heights
    return baselines


def pearson_correlation(x: np.ndarray, y: np.ndarray) -> float:
    if x.ndim != 1 or y.shape != x.shape or len(x) < 2:
        raise ValueError("Pearson inputs must be equal vectors of length at least two")
    x_centered = x - x.mean()
    y_centered = y - y.mean()
    denominator = math.sqrt(
        float(np.dot(x_centered, x_centered) * np.dot(y_centered, y_centered))
    )
    if denominator == 0.0:
        raise ValueError("Pearson correlation undefined for constant vector")
    value = float(np.dot(x_centered, y_centered) / denominator)
    return max(-1.0, min(1.0, value))


def percentile_interval(values: Sequence[float]) -> tuple[float, float]:
    array = np.asarray(values, dtype=np.float64)
    if array.ndim != 1 or len(array) == 0 or not np.isfinite(array).all():
        raise ValueError("invalid bootstrap values")
    low, high = np.quantile(array, (0.025, 0.975), method="linear")
    return float(low), float(high)


def bootstrap_metrics(
    height_residuals: np.ndarray,
    absolute_relative_errors: np.ndarray,
    estimated: np.ndarray,
    latent: np.ndarray,
    *,
    n: int,
    side: str,
) -> dict[str, float]:
    size = len(height_residuals)
    if not (
        size >= 2
        and absolute_relative_errors.shape == (size,)
        and estimated.shape == (size,)
        and latent.shape == (size,)
    ):
        raise ValueError("invalid bootstrap arrays")
    rng = np.random.Generator(np.random.PCG64(bootstrap_seed(n, side)))
    residual_means = np.empty(BOOTSTRAP_REPLICATES, dtype=np.float64)
    relative_medians = np.empty(BOOTSTRAP_REPLICATES, dtype=np.float64)
    correlations = np.empty(BOOTSTRAP_REPLICATES, dtype=np.float64)
    for replicate in range(BOOTSTRAP_REPLICATES):
        indices = rng.integers(0, size, size=size)
        residual_means[replicate] = float(height_residuals[indices].mean())
        relative_medians[replicate] = float(
            np.median(absolute_relative_errors[indices])
        )
        correlations[replicate] = pearson_correlation(
            estimated[indices], latent[indices]
        )
    residual_low, residual_high = percentile_interval(residual_means)
    relative_low, relative_high = percentile_interval(relative_medians)
    correlation_low, correlation_high = percentile_interval(correlations)
    return {
        "height_residual_bootstrap95_low": residual_low,
        "height_residual_bootstrap95_high": residual_high,
        "median_are_bootstrap95_low": relative_low,
        "median_are_bootstrap95_high": relative_high,
        "pearson_bootstrap95_low": correlation_low,
        "pearson_bootstrap95_high": correlation_high,
    }


def interval_rows(
    intervals: Sequence[IntervalRecord], baseline_means: dict[int, float]
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for interval in intervals:
        signed_error = (
            interval.height_duration_estimate - interval.latent_duration
        )
        rows.append(
            {
                "n": interval.n,
                "replicate": interval.replicate,
                "side": interval.side,
                "interval_size": interval.interval_size,
                "height": interval.height,
                "latent_duration": interval.latent_duration,
                "height_duration_estimate": interval.height_duration_estimate,
                "signed_duration_error": signed_error,
                "absolute_relative_error": (
                    abs(signed_error) / interval.latent_duration
                ),
                "baseline_mean_height": baseline_means[interval.interval_size],
                "height_residual": (
                    interval.height - baseline_means[interval.interval_size]
                ),
            }
        )
    return rows


def calibration_rows(interval_table: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[int, str], list[dict[str, object]]] = defaultdict(list)
    for row in interval_table:
        grouped[(int(row["n"]), str(row["side"]))].append(row)
    rows: list[dict[str, object]] = []
    for n in BASE_N:
        for side in SIDES:
            group = grouped[(n, side)]
            sizes = np.asarray([row["interval_size"] for row in group], dtype=np.float64)
            heights = np.asarray([row["height"] for row in group], dtype=np.float64)
            residuals = np.asarray(
                [row["height_residual"] for row in group], dtype=np.float64
            )
            latent = np.asarray(
                [row["latent_duration"] for row in group], dtype=np.float64
            )
            estimated = np.asarray(
                [row["height_duration_estimate"] for row in group], dtype=np.float64
            )
            errors = estimated - latent
            relative = np.abs(errors) / latent
            correlation = pearson_correlation(estimated, latent)
            x_centered = latent - latent.mean()
            slope = float(np.dot(x_centered, estimated - estimated.mean())) / float(
                np.dot(x_centered, x_centered)
            )
            intercept = float(estimated.mean() - slope * latent.mean())
            bootstrap = bootstrap_metrics(
                residuals,
                relative,
                estimated,
                latent,
                n=n,
                side=side,
            )
            height_sd = float(heights.std(ddof=1))
            rows.append(
                {
                    "n": n,
                    "side": side,
                    "selected_count": len(group),
                    "interval_size_mean": float(sizes.mean()),
                    "interval_size_median": float(np.median(sizes)),
                    "height_mean": float(heights.mean()),
                    "height_sd": height_sd,
                    "height_cv": height_sd / float(heights.mean()),
                    "height_residual_mean": float(residuals.mean()),
                    **bootstrap,
                    "latent_duration_mean": float(latent.mean()),
                    "height_duration_estimate_mean": float(estimated.mean()),
                    "duration_bias_mean": float(errors.mean()),
                    "duration_mae": float(np.abs(errors).mean()),
                    "duration_rmse": math.sqrt(float(np.mean(errors * errors))),
                    "median_absolute_relative_error": float(np.median(relative)),
                    "pearson_correlation": correlation,
                    "ols_slope": slope,
                    "ols_intercept": intercept,
                }
            )
    return rows


def baseline_rows(
    intervals: Sequence[IntervalRecord], baselines: dict[int, list[int]]
) -> list[dict[str, object]]:
    selected: dict[int, list[int]] = defaultdict(list)
    for interval in intervals:
        selected[interval.interval_size].append(interval.height)
    rows: list[dict[str, object]] = []
    for interval_size in sorted(baselines):
        baseline = baselines[interval_size]
        selected_heights = selected[interval_size]
        baseline_mean = float(statistics.fmean(baseline))
        baseline_sd = statistics.stdev(baseline)
        selected_mean = float(statistics.fmean(selected_heights))
        rows.append(
            {
                "interval_size": interval_size,
                "baseline_replicates": len(baseline),
                "baseline_mean_height": baseline_mean,
                "baseline_sd_height": baseline_sd,
                "baseline_standard_error": baseline_sd / math.sqrt(len(baseline)),
                "selected_interval_count": len(selected_heights),
                "selected_mean_height": selected_mean,
                "selected_mean_residual": selected_mean - baseline_mean,
            }
        )
    return rows


def thinning_rows(
    target: dict[tuple[int, float], TargetThinning]
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    primary_threshold = math.log(TARGET_FACTOR_PRIMARY)
    secondary_threshold = math.log(TARGET_FACTOR_SECONDARY)
    for n in BASE_N:
        for retention in RETENTION:
            record = target[(n, retention)]
            assert record.log_drifts is not None
            if record.both_unique == 0:
                raise RuntimeError("no joint unique selections for target stability")
            drifts = np.asarray(record.log_drifts, dtype=np.float64)
            within_primary = int((drifts <= primary_threshold).sum())
            within_secondary = int((drifts <= secondary_threshold).sum())
            low, high = sealed.wilson_interval(within_primary, record.both_unique)
            rows.append(
                {
                    "n": n,
                    "retention": retention,
                    "base_unique_count": record.base_unique,
                    "both_unique_count": record.both_unique,
                    "p_both_unique_given_base_unique": (
                        record.both_unique / record.base_unique
                    ),
                    "exact_reselected_count": record.exact_reselected,
                    "p_exact_reselected_given_both_unique": (
                        record.exact_reselected / record.both_unique
                    ),
                    "target_within_25_count": within_primary,
                    "p_target_within_25": within_primary / record.both_unique,
                    "p_target_within_25_ci95_low": low,
                    "p_target_within_25_ci95_high": high,
                    "target_within_50_count": within_secondary,
                    "p_target_within_50": within_secondary / record.both_unique,
                    "log_drift_mean": float(drifts.mean()),
                    "log_drift_median": float(np.median(drifts)),
                    "log_drift_p90": float(np.quantile(drifts, 0.90, method="linear")),
                }
            )
    return rows


def scientific_terminal(
    calibration: Sequence[dict[str, object]],
    thinning: Sequence[dict[str, object]],
) -> tuple[str, dict[str, object]]:
    calibration_by_key = {
        (int(row["n"]), str(row["side"])): row for row in calibration
    }
    thinning_by_key = {
        (int(row["n"]), float(row["retention"])): row for row in thinning
    }
    gate: dict[str, object] = {}
    pass_all = True
    park_all_n = True
    for n in BASE_N:
        side_gate: dict[str, object] = {}
        sides_pass = True
        strong_failure_n = False
        for side in SIDES:
            row = calibration_by_key[(n, side)]
            height_pass = (
                float(row["height_residual_bootstrap95_low"])
                >= -HEIGHT_RESIDUAL_LIMIT
                and float(row["height_residual_bootstrap95_high"])
                <= HEIGHT_RESIDUAL_LIMIT
            )
            correlation_pass = (
                float(row["pearson_bootstrap95_low"]) >= CORRELATION_LOWER
            )
            relative_pass = (
                float(row["median_are_bootstrap95_high"])
                <= MEDIAN_RELATIVE_ERROR_UPPER
            )
            side_pass = height_pass and correlation_pass and relative_pass
            sides_pass &= side_pass
            strong_failure = (
                float(row["pearson_bootstrap95_high"])
                < PARK_CORRELATION_UPPER
                or float(row["median_are_bootstrap95_low"])
                > PARK_RELATIVE_ERROR_LOWER
            )
            strong_failure_n |= strong_failure
            side_gate[side] = {
                "height_residual_mean": row["height_residual_mean"],
                "height_residual_bootstrap95_low": row[
                    "height_residual_bootstrap95_low"
                ],
                "height_residual_bootstrap95_high": row[
                    "height_residual_bootstrap95_high"
                ],
                "pearson_correlation": row["pearson_correlation"],
                "pearson_bootstrap95_low": row["pearson_bootstrap95_low"],
                "pearson_bootstrap95_high": row["pearson_bootstrap95_high"],
                "median_absolute_relative_error": row[
                    "median_absolute_relative_error"
                ],
                "median_are_bootstrap95_low": row[
                    "median_are_bootstrap95_low"
                ],
                "median_are_bootstrap95_high": row[
                    "median_are_bootstrap95_high"
                ],
                "height_pass": height_pass,
                "correlation_pass": correlation_pass,
                "relative_error_pass": relative_pass,
                "side_pass": side_pass,
                "strong_failure": strong_failure,
            }
        thin_090 = thinning_by_key[(n, 0.90)]
        thin_080 = thinning_by_key[(n, 0.80)]
        target_090_pass = (
            float(thin_090["p_target_within_25_ci95_low"])
            >= TARGET_090_LOWER
        )
        target_080_pass = (
            float(thin_080["p_target_within_25_ci95_low"])
            >= TARGET_080_LOWER
        )
        pass_n = sides_pass and target_090_pass and target_080_pass
        pass_all &= pass_n
        park_all_n &= strong_failure_n
        gate[str(n)] = {
            "sides": side_gate,
            "p_target_within_25_090": thin_090["p_target_within_25"],
            "p_target_within_25_090_wilson95_low": thin_090[
                "p_target_within_25_ci95_low"
            ],
            "p_target_within_25_080": thin_080["p_target_within_25"],
            "p_target_within_25_080_wilson95_low": thin_080[
                "p_target_within_25_ci95_low"
            ],
            "target_090_pass": target_090_pass,
            "target_080_pass": target_080_pass,
            "pass_n": pass_n,
            "strong_failure_n": strong_failure_n,
        }
    if pass_all:
        return TERMINAL_PASS, gate
    if park_all_n:
        return TERMINAL_PARK, gate
    return TERMINAL_INCONCLUSIVE, gate


def _format_value(value: object) -> object:
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
        "selector": comparison.MIN_COVERAGE_LEX,
        "dimension": 2,
        "fixed_n_channel": True,
        "metric_convention": "ds^2=du*dv",
        "base_n": list(BASE_N),
        "base_replicates_per_n": BASE_REPLICATES_PER_N,
        "base_batches": BASE_BATCHES,
        "base_replicates_per_batch": BASE_REPLICATES_PER_BATCH,
        "retention": list(RETENTION),
        "coordinate_seed_base": COORDINATE_SEED_BASE,
        "thinning_seed_base": THINNING_SEED_BASE,
        "baseline_seed_base": BASELINE_SEED_BASE,
        "baseline_replicates_per_size": BASELINE_REPLICATES_PER_SIZE,
        "bootstrap_seed_base": BOOTSTRAP_SEED_BASE,
        "bootstrap_replicates": BOOTSTRAP_REPLICATES,
        "height_duration_estimator": "H/(2*sqrt(n))",
        "height_residual_limit": HEIGHT_RESIDUAL_LIMIT,
        "correlation_lower": CORRELATION_LOWER,
        "median_relative_error_upper": MEDIAN_RELATIVE_ERROR_UPPER,
        "target_090_lower": TARGET_090_LOWER,
        "target_080_lower": TARGET_080_LOWER,
        "park_correlation_upper": PARK_CORRELATION_UPPER,
        "park_relative_error_lower": PARK_RELATIVE_ERROR_LOWER,
        "height_ratio_computed": False,
    }


def execute(output_dir: Path, *, overwrite: bool = False) -> dict[str, object]:
    filenames = (
        INTERVAL_FILENAME,
        CALIBRATION_FILENAME,
        BASELINE_FILENAME,
        THINNING_FILENAME,
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

    intervals, target = simulate_base()
    baselines = simulate_baselines([row.interval_size for row in intervals])
    baseline_means = {
        size: float(statistics.fmean(heights)) for size, heights in baselines.items()
    }
    interval_table = interval_rows(intervals, baseline_means)
    calibration_table = calibration_rows(interval_table)
    baseline_table = baseline_rows(intervals, baselines)
    thinning_table = thinning_rows(target)
    terminal, gate = scientific_terminal(calibration_table, thinning_table)

    tables = (
        (INTERVAL_FILENAME, interval_table, INTERVAL_FIELDS),
        (CALIBRATION_FILENAME, calibration_table, CALIBRATION_FIELDS),
        (BASELINE_FILENAME, baseline_table, BASELINE_FIELDS),
        (THINNING_FILENAME, thinning_table, THINNING_FIELDS),
    )
    artifact_hashes: dict[str, str] = {}
    for filename, table, fields in tables:
        data = rows_to_csv(table, fields).encode("utf-8")
        artifact_hashes[filename] = _write_with_sidecar(
            output_dir / filename, data, overwrite=overwrite
        )

    summary: dict[str, object] = {
        "schema_version": "p1a_lex_height_duration_d2_v1",
        "contract_status": "FROZEN_BEFORE_RESULTS",
        "terminal": terminal,
        "contract": contract_dict(),
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "artifacts": {
            filename: {"sha256": digest}
            for filename, digest in artifact_hashes.items()
        },
        "calibration": calibration_table,
        "target_thinning": thinning_table,
        "gate": gate,
        "claim_ceiling": "D2_INDIVIDUAL_HEIGHT_CALIBRATION_NO_RATIO",
    }
    summary_data = (json.dumps(summary, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )
    summary_sha = _write_with_sidecar(
        output_dir / SUMMARY_FILENAME, summary_data, overwrite=overwrite
    )
    summary["summary_sha256"] = summary_sha

    print(f"P1A_LEX_HEIGHT_TERMINAL={terminal}")
    for filename, digest in artifact_hashes.items():
        print(f"P1A_LEX_HEIGHT_SHA256_{filename}={digest}")
    print(f"P1A_LEX_HEIGHT_SUMMARY_SHA256={summary_sha}")
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
        print(f"P1A_LEX_HEIGHT_TERMINAL={TERMINAL_INVALID}", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
