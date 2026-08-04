#!/usr/bin/env python3
"""Independent d=2 comparison of two alternative duration representations.

COUNT_VOLUME and HEIGHT_WIDTH are evaluated against latent duration for each side
selected by MIN_COVERAGE_LEX. HEIGHT_ONLY is a non-eligible benchmark. No ratio
between past and future intervals is computed.
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
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import numpy as np

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_estabilidad_d2 as previous
from emergencia import p1a_gate_altura_duracion_lex_d2 as height_gate


HEIGHT_ONLY = "HEIGHT_ONLY"
COUNT_VOLUME = "COUNT_VOLUME"
HEIGHT_WIDTH = "HEIGHT_WIDTH"
REPRESENTATIONS = (HEIGHT_ONLY, COUNT_VOLUME, HEIGHT_WIDTH)
CANDIDATES = (COUNT_VOLUME, HEIGHT_WIDTH)
REPRESENTATION_CODE = {HEIGHT_ONLY: 0, COUNT_VOLUME: 1, HEIGHT_WIDTH: 2}

PAST = height_gate.PAST
FUTURE = height_gate.FUTURE
SIDES = height_gate.SIDES
SIDE_CODE = height_gate.SIDE_CODE

BASE_N = (64, 96, 128)
BASE_REPLICATES_PER_N = 12_000
BASE_BATCHES = 8
BASE_REPLICATES_PER_BATCH = 1_500
COORDINATE_SEED_BASE = 2_608_044_000
BOOTSTRAP_SEED_BASE = 2_608_045_000
BOOTSTRAP_REPLICATES = 1_000

BIAS_LIMIT = 0.05
MEDIAN_RELATIVE_ERROR_UPPER = 0.30
CORRELATION_LOWER = 0.80
PARK_CORRELATION_UPPER = 0.50
PARK_RELATIVE_ERROR_LOWER = 0.50

TERMINAL_SELECT_COUNT = "SELECT_COUNT_VOLUME_FOR_RATIO_PREREGISTRATION"
TERMINAL_SELECT_HEIGHT_WIDTH = "SELECT_HEIGHT_WIDTH_FOR_RATIO_PREREGISTRATION"
TERMINAL_PARK_BOTH = "PARK_BOTH_ALTERNATIVE_REPRESENTATIONS"
TERMINAL_INCONCLUSIVE = "INCONCLUSIVE_ALTERNATIVE_REPRESENTATIONS"
TERMINAL_INVALID = "IMPLEMENTATION_INVALID"

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = HERE / "resultados"
INTERVAL_FILENAME = "p1a_representaciones_intervalos_d2.csv"
METRICS_FILENAME = "p1a_representaciones_metricas_d2.csv"
SUMMARY_FILENAME = "p1a_representaciones_resumen.json"

INTERVAL_FIELDS = (
    "n",
    "replicate",
    "side",
    "interval_size",
    "height",
    "width",
    "latent_duration",
    "estimate_height_only",
    "estimate_count_volume",
    "estimate_height_width",
    "signed_error_height_only",
    "signed_error_count_volume",
    "signed_error_height_width",
    "absolute_relative_error_height_only",
    "absolute_relative_error_count_volume",
    "absolute_relative_error_height_width",
)

METRICS_FIELDS = (
    "representation",
    "n",
    "side",
    "selected_count",
    "estimate_mean",
    "estimate_sd",
    "estimate_cv",
    "latent_duration_mean",
    "bias_mean",
    "bias_bootstrap95_low",
    "bias_bootstrap95_high",
    "mae",
    "rmse",
    "median_absolute_relative_error",
    "median_are_bootstrap95_low",
    "median_are_bootstrap95_high",
    "pearson_correlation",
    "pearson_bootstrap95_low",
    "pearson_bootstrap95_high",
    "ols_slope",
    "ols_intercept",
)


@dataclass(frozen=True)
class IntervalRecord:
    n: int
    replicate: int
    side: str
    interval_size: int
    height: int
    width: int
    latent_duration: float
    estimate_height_only: float
    estimate_count_volume: float
    estimate_height_width: float


def coordinate_seed(n: int, batch: int) -> int:
    if n not in BASE_N or not 0 <= batch < BASE_BATCHES:
        raise ValueError("coordinate seed outside frozen contract")
    return COORDINATE_SEED_BASE + 100 * n + batch


def bootstrap_seed(representation: str, n: int, side: str) -> int:
    if representation not in REPRESENTATIONS or n not in BASE_N or side not in SIDES:
        raise ValueError("bootstrap seed outside frozen contract")
    return (
        BOOTSTRAP_SEED_BASE
        + 1000 * REPRESENTATION_CODE[representation]
        + 100 * n
        + SIDE_CODE[side]
    )


def width_from_permutation(permutation: Sequence[int]) -> int:
    values = np.asarray(permutation, dtype=np.int64)
    if values.ndim != 1 or len(values) == 0 or len(np.unique(values)) != len(values):
        raise ValueError("width input must be a nonempty sequence of distinct ranks")
    return previous.lis_length(-values)


def interval_height_width(
    permutation: Sequence[int], start: int, stop: int
) -> tuple[int, int, int]:
    perm = comparison.sealed.validate_permutation(permutation)
    if not (0 <= start < stop < len(perm) and perm[start] < perm[stop]):
        raise ValueError("interval endpoints must be comparable and ordered")
    segment = perm[start : stop + 1]
    inside = segment[(segment >= perm[start]) & (segment <= perm[stop])]
    height = previous.lis_length(inside)
    width = width_from_permutation(inside)
    return height, width, len(inside)


def estimate_count_volume(interval_size: int, n: int) -> float:
    if not 2 < interval_size <= n or n <= 2:
        raise ValueError("invalid interval or total cardinality")
    return math.sqrt((interval_size - 2) / (n - 2))


def estimate_height_width(height: int, width: int, n: int) -> float:
    if height < 1 or width < 1 or n <= 0:
        raise ValueError("invalid height, width or total cardinality")
    return (height + width) / (4.0 * math.sqrt(n))


def _selected_lex(permutation: Sequence[int]) -> comparison.Selection | None:
    outcome = comparison.evaluate_selectors(permutation)[comparison.MIN_COVERAGE_LEX]
    if outcome.state == comparison.STATE_UNIQUE:
        if outcome.selection is None:
            raise RuntimeError("unique lex outcome missing selection")
        return outcome.selection
    return None


def simulate_base() -> list[IntervalRecord]:
    intervals: list[IntervalRecord] = []
    for n in BASE_N:
        unique_count = 0
        replicate = 0
        for batch in range(BASE_BATCHES):
            rng = np.random.Generator(np.random.PCG64(coordinate_seed(n, batch)))
            for _ in range(BASE_REPLICATES_PER_BATCH):
                u_sorted, v_sorted, permutation = previous.product_permutation(
                    rng.random(n), rng.random(n)
                )
                selected = _selected_lex(permutation)
                if selected is not None:
                    unique_count += 1
                    a, b, c, d = selected.quadruple
                    for side, start, stop, expected_size in (
                        (PAST, a, b, selected.past_size),
                        (FUTURE, c, d, selected.future_size),
                    ):
                        height, width, size = interval_height_width(
                            permutation, start, stop
                        )
                        if size != expected_size:
                            raise RuntimeError("selected interval size mismatch")
                        latent = height_gate.latent_duration(
                            u_sorted, v_sorted, start, stop
                        )
                        intervals.append(
                            IntervalRecord(
                                n=n,
                                replicate=replicate,
                                side=side,
                                interval_size=size,
                                height=height,
                                width=width,
                                latent_duration=latent,
                                estimate_height_only=(
                                    height_gate.height_duration_estimate(height, n)
                                ),
                                estimate_count_volume=estimate_count_volume(size, n),
                                estimate_height_width=estimate_height_width(
                                    height, width, n
                                ),
                            )
                        )
                replicate += 1
        if replicate != BASE_REPLICATES_PER_N:
            raise RuntimeError(f"replicate mismatch at n={n}")
        if len([row for row in intervals if row.n == n]) != 2 * unique_count:
            raise RuntimeError(f"interval row mismatch at n={n}")
        print(
            f"P1A_ALT_REP_N={n} REPLICATES={replicate} UNIQUE={unique_count}",
            flush=True,
        )
    return intervals


def interval_rows(intervals: Sequence[IntervalRecord]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for interval in intervals:
        estimates = {
            HEIGHT_ONLY: interval.estimate_height_only,
            COUNT_VOLUME: interval.estimate_count_volume,
            HEIGHT_WIDTH: interval.estimate_height_width,
        }
        errors = {
            name: estimate - interval.latent_duration
            for name, estimate in estimates.items()
        }
        rows.append(
            {
                "n": interval.n,
                "replicate": interval.replicate,
                "side": interval.side,
                "interval_size": interval.interval_size,
                "height": interval.height,
                "width": interval.width,
                "latent_duration": interval.latent_duration,
                "estimate_height_only": estimates[HEIGHT_ONLY],
                "estimate_count_volume": estimates[COUNT_VOLUME],
                "estimate_height_width": estimates[HEIGHT_WIDTH],
                "signed_error_height_only": errors[HEIGHT_ONLY],
                "signed_error_count_volume": errors[COUNT_VOLUME],
                "signed_error_height_width": errors[HEIGHT_WIDTH],
                "absolute_relative_error_height_only": (
                    abs(errors[HEIGHT_ONLY]) / interval.latent_duration
                ),
                "absolute_relative_error_count_volume": (
                    abs(errors[COUNT_VOLUME]) / interval.latent_duration
                ),
                "absolute_relative_error_height_width": (
                    abs(errors[HEIGHT_WIDTH]) / interval.latent_duration
                ),
            }
        )
    return rows


def _representation_columns(representation: str) -> tuple[str, str, str]:
    suffix = {
        HEIGHT_ONLY: "height_only",
        COUNT_VOLUME: "count_volume",
        HEIGHT_WIDTH: "height_width",
    }[representation]
    return (
        f"estimate_{suffix}",
        f"signed_error_{suffix}",
        f"absolute_relative_error_{suffix}",
    )


def bootstrap_metrics(
    estimate: np.ndarray,
    latent: np.ndarray,
    errors: np.ndarray,
    relative: np.ndarray,
    *,
    representation: str,
    n: int,
    side: str,
) -> dict[str, float]:
    size = len(estimate)
    if not (
        size >= 2
        and latent.shape == (size,)
        and errors.shape == (size,)
        and relative.shape == (size,)
    ):
        raise ValueError("invalid bootstrap arrays")
    rng = np.random.Generator(
        np.random.PCG64(bootstrap_seed(representation, n, side))
    )
    biases = np.empty(BOOTSTRAP_REPLICATES, dtype=np.float64)
    relative_medians = np.empty(BOOTSTRAP_REPLICATES, dtype=np.float64)
    correlations = np.empty(BOOTSTRAP_REPLICATES, dtype=np.float64)
    for replicate in range(BOOTSTRAP_REPLICATES):
        indices = rng.integers(0, size, size=size)
        biases[replicate] = float(errors[indices].mean())
        relative_medians[replicate] = float(np.median(relative[indices]))
        correlations[replicate] = height_gate.pearson_correlation(
            estimate[indices], latent[indices]
        )
    bias_low, bias_high = height_gate.percentile_interval(biases)
    relative_low, relative_high = height_gate.percentile_interval(relative_medians)
    correlation_low, correlation_high = height_gate.percentile_interval(correlations)
    return {
        "bias_bootstrap95_low": bias_low,
        "bias_bootstrap95_high": bias_high,
        "median_are_bootstrap95_low": relative_low,
        "median_are_bootstrap95_high": relative_high,
        "pearson_bootstrap95_low": correlation_low,
        "pearson_bootstrap95_high": correlation_high,
    }


def metrics_rows(interval_table: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[int, str], list[dict[str, object]]] = defaultdict(list)
    for row in interval_table:
        grouped[(int(row["n"]), str(row["side"]))].append(row)
    rows: list[dict[str, object]] = []
    for representation in REPRESENTATIONS:
        estimate_column, error_column, relative_column = _representation_columns(
            representation
        )
        for n in BASE_N:
            for side in SIDES:
                group = grouped[(n, side)]
                estimate = np.asarray(
                    [row[estimate_column] for row in group], dtype=np.float64
                )
                latent = np.asarray(
                    [row["latent_duration"] for row in group], dtype=np.float64
                )
                errors = np.asarray(
                    [row[error_column] for row in group], dtype=np.float64
                )
                relative = np.asarray(
                    [row[relative_column] for row in group], dtype=np.float64
                )
                correlation = height_gate.pearson_correlation(estimate, latent)
                latent_centered = latent - latent.mean()
                slope = float(
                    np.dot(latent_centered, estimate - estimate.mean())
                    / np.dot(latent_centered, latent_centered)
                )
                intercept = float(estimate.mean() - slope * latent.mean())
                bootstrap = bootstrap_metrics(
                    estimate,
                    latent,
                    errors,
                    relative,
                    representation=representation,
                    n=n,
                    side=side,
                )
                estimate_sd = float(estimate.std(ddof=1))
                rows.append(
                    {
                        "representation": representation,
                        "n": n,
                        "side": side,
                        "selected_count": len(group),
                        "estimate_mean": float(estimate.mean()),
                        "estimate_sd": estimate_sd,
                        "estimate_cv": estimate_sd / float(estimate.mean()),
                        "latent_duration_mean": float(latent.mean()),
                        "bias_mean": float(errors.mean()),
                        **bootstrap,
                        "mae": float(np.abs(errors).mean()),
                        "rmse": math.sqrt(float(np.mean(errors * errors))),
                        "median_absolute_relative_error": float(np.median(relative)),
                        "pearson_correlation": correlation,
                        "ols_slope": slope,
                        "ols_intercept": intercept,
                    }
                )
    return rows


def scientific_terminal(
    metrics: Sequence[dict[str, object]],
) -> tuple[str, dict[str, object]]:
    by_key = {
        (str(row["representation"]), int(row["n"]), str(row["side"])): row
        for row in metrics
    }
    gate: dict[str, object] = {}
    qualifies: dict[str, bool] = {}
    strongly_parked: dict[str, bool] = {}
    for representation in CANDIDATES:
        by_n: dict[str, object] = {}
        qualifies_all = True
        strong_all_n = True
        for n in BASE_N:
            side_gate: dict[str, object] = {}
            pass_n = True
            strong_failure_n = False
            for side in SIDES:
                row = by_key[(representation, n, side)]
                bias_pass = (
                    float(row["bias_bootstrap95_low"]) >= -BIAS_LIMIT
                    and float(row["bias_bootstrap95_high"]) <= BIAS_LIMIT
                )
                relative_pass = (
                    float(row["median_are_bootstrap95_high"])
                    <= MEDIAN_RELATIVE_ERROR_UPPER
                )
                correlation_pass = (
                    float(row["pearson_bootstrap95_low"]) >= CORRELATION_LOWER
                )
                side_pass = bias_pass and relative_pass and correlation_pass
                pass_n &= side_pass
                strong_failure = (
                    float(row["pearson_bootstrap95_high"])
                    < PARK_CORRELATION_UPPER
                    or float(row["median_are_bootstrap95_low"])
                    > PARK_RELATIVE_ERROR_LOWER
                )
                strong_failure_n |= strong_failure
                side_gate[side] = {
                    "bias_mean": row["bias_mean"],
                    "bias_bootstrap95_low": row["bias_bootstrap95_low"],
                    "bias_bootstrap95_high": row["bias_bootstrap95_high"],
                    "median_absolute_relative_error": row[
                        "median_absolute_relative_error"
                    ],
                    "median_are_bootstrap95_low": row[
                        "median_are_bootstrap95_low"
                    ],
                    "median_are_bootstrap95_high": row[
                        "median_are_bootstrap95_high"
                    ],
                    "pearson_correlation": row["pearson_correlation"],
                    "pearson_bootstrap95_low": row["pearson_bootstrap95_low"],
                    "pearson_bootstrap95_high": row["pearson_bootstrap95_high"],
                    "bias_pass": bias_pass,
                    "relative_error_pass": relative_pass,
                    "correlation_pass": correlation_pass,
                    "side_pass": side_pass,
                    "strong_failure": strong_failure,
                }
            qualifies_all &= pass_n
            strong_all_n &= strong_failure_n
            by_n[str(n)] = {
                "sides": side_gate,
                "pass_n": pass_n,
                "strong_failure_n": strong_failure_n,
            }
        qualifies[representation] = qualifies_all
        strongly_parked[representation] = strong_all_n
        gate[representation] = {
            "qualifies_all_n": qualifies_all,
            "strongly_parked_all_n": strong_all_n,
            "by_n": by_n,
        }

    if qualifies[COUNT_VOLUME]:
        return TERMINAL_SELECT_COUNT, gate
    if qualifies[HEIGHT_WIDTH]:
        return TERMINAL_SELECT_HEIGHT_WIDTH, gate
    if strongly_parked[COUNT_VOLUME] and strongly_parked[HEIGHT_WIDTH]:
        return TERMINAL_PARK_BOTH, gate
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
        "representations": list(REPRESENTATIONS),
        "candidates": list(CANDIDATES),
        "dimension": 2,
        "fixed_n_channel": True,
        "metric_convention": "ds^2=du*dv",
        "base_n": list(BASE_N),
        "base_replicates_per_n": BASE_REPLICATES_PER_N,
        "base_batches": BASE_BATCHES,
        "base_replicates_per_batch": BASE_REPLICATES_PER_BATCH,
        "coordinate_seed_base": COORDINATE_SEED_BASE,
        "bootstrap_seed_base": BOOTSTRAP_SEED_BASE,
        "bootstrap_replicates": BOOTSTRAP_REPLICATES,
        "count_volume_formula": "sqrt((m-2)/(n-2))",
        "height_width_formula": "(H+W)/(4*sqrt(n))",
        "bias_limit": BIAS_LIMIT,
        "median_relative_error_upper": MEDIAN_RELATIVE_ERROR_UPPER,
        "correlation_lower": CORRELATION_LOWER,
        "park_correlation_upper": PARK_CORRELATION_UPPER,
        "park_relative_error_lower": PARK_RELATIVE_ERROR_LOWER,
        "ratio_computed": False,
    }


def execute(output_dir: Path, *, overwrite: bool = False) -> dict[str, object]:
    filenames = (INTERVAL_FILENAME, METRICS_FILENAME, SUMMARY_FILENAME)
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

    intervals = simulate_base()
    interval_table = interval_rows(intervals)
    metrics_table = metrics_rows(interval_table)
    terminal, gate = scientific_terminal(metrics_table)

    interval_data = rows_to_csv(interval_table, INTERVAL_FIELDS).encode("utf-8")
    metrics_data = rows_to_csv(metrics_table, METRICS_FIELDS).encode("utf-8")
    interval_sha = _write_with_sidecar(
        output_dir / INTERVAL_FILENAME, interval_data, overwrite=overwrite
    )
    metrics_sha = _write_with_sidecar(
        output_dir / METRICS_FILENAME, metrics_data, overwrite=overwrite
    )

    summary: dict[str, object] = {
        "schema_version": "p1a_alternative_representations_d2_v1",
        "contract_status": "FROZEN_BEFORE_RESULTS",
        "terminal": terminal,
        "contract": contract_dict(),
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "artifacts": {
            INTERVAL_FILENAME: {"sha256": interval_sha},
            METRICS_FILENAME: {"sha256": metrics_sha},
        },
        "metrics": metrics_table,
        "gate": gate,
        "claim_ceiling": "D2_ALTERNATIVE_INTERVAL_REPRESENTATIONS_NO_RATIO",
    }
    summary_data = (json.dumps(summary, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )
    summary_sha = _write_with_sidecar(
        output_dir / SUMMARY_FILENAME, summary_data, overwrite=overwrite
    )
    summary["summary_sha256"] = summary_sha

    print(f"P1A_ALT_REP_TERMINAL={terminal}")
    print(f"P1A_ALT_REP_INTERVAL_SHA256={interval_sha}")
    print(f"P1A_ALT_REP_METRICS_SHA256={metrics_sha}")
    print(f"P1A_ALT_REP_SUMMARY_SHA256={summary_sha}")
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
        print(f"P1A_ALT_REP_TERMINAL={TERMINAL_INVALID}", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
