#!/usr/bin/env python3
"""EF-2 exact fiber enumeration for selected COUNT_VOLUME intervals in d=2.

The sample space is the uniform permutation space fixed in EF-0.  This executable
uses the frozen MIN_COVERAGE_LEX selector, records only the discrete lateral fields
M, K, L and r=K*L for unique selections, and emits the exact Omega and C counts.
It performs no Monte Carlo simulation and reads no latent coordinate magnitudes.
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
from collections import Counter
from dataclasses import dataclass, field
from itertools import combinations, permutations
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np

from emergencia import p1a_comparar_selectores_d2 as comparison


EXACT_N = (6, 7, 8, 9)
INDEPENDENT_CROSSCHECK_N = (6, 7)
SIDES = ("PAST", "FUTURE")
STATES = (
    comparison.STATE_EMPTY,
    comparison.STATE_UNIQUE,
    comparison.STATE_TIE,
)

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = HERE / "resultados"
LEGACY_EXACT_PATH = DEFAULT_OUTPUT_DIR / "p1a_enumeracion_exacta_d2.csv"

STATE_FILENAME = "p1a_entropia_fibras_estados_exactos_d2.csv"
OMEGA_FILENAME = "p1a_entropia_fibras_omega_exacta_d2.csv"
C_FILENAME = "p1a_entropia_fibras_c_exacta_d2.csv"
SUMMARY_FILENAME = "p1a_entropia_fibras_resumen.json"

STATE_FIELDS = ("selector", "n", "permutations", "state", "count", "probability")
OMEGA_FIELDS = ("n", "side", "m", "k", "l", "r", "count")
C_FIELDS = ("n", "side", "m", "r", "count")

OmegaKey = tuple[str, int, int, int, int]
CKey = tuple[str, int, int]


@dataclass(frozen=True)
class IndependentSelection:
    quadruple: tuple[int, int, int, int]
    past_size: int
    future_size: int


@dataclass(frozen=True)
class IndependentOutcome:
    state: str
    n_maximizers: int
    primary_score: int | None
    secondary_score: int | None
    selection: IndependentSelection | None


@dataclass
class ExactFiberAggregate:
    n: int
    permutations: int = 0
    state_counts: Counter[str] = field(default_factory=Counter)
    legacy_coverage_counts: Counter[str] = field(default_factory=Counter)
    omega: Counter[OmegaKey] = field(default_factory=Counter)
    c_counts: Counter[CKey] = field(default_factory=Counter)
    independent_crosschecks: int = 0


def _interval_size_naive(permutation: Sequence[int], i: int, j: int) -> int:
    if not (i < j and permutation[i] < permutation[j]):
        return 0
    return sum(
        i <= x <= j and permutation[i] <= permutation[x] <= permutation[j]
        for x in range(len(permutation))
    )


def evaluate_lex_naive(permutation: Sequence[int]) -> IndependentOutcome:
    """Independent direct definition of MIN_COVERAGE_LEX.

    This implementation intentionally does not call the vectorized interval matrix
    or selector evaluator.  It is used exhaustively at n=6,7 as EF-2's second
    implementation.
    """

    perm = tuple(int(value) for value in permutation)
    if sorted(perm) != list(range(len(perm))):
        raise ValueError("expected a permutation of range(n)")

    candidates: list[
        tuple[tuple[int, int, int, int], int, int, tuple[int, int]]
    ] = []
    for a, b, c, d in combinations(range(len(perm)), 4):
        if not perm[a] < perm[b] < perm[c] < perm[d]:
            continue
        past = _interval_size_naive(perm, a, b)
        future = _interval_size_naive(perm, c, d)
        if past < 3 or future < 3:
            continue
        candidates.append(
            ((a, b, c, d), past, future, (min(past, future), past + future))
        )

    if not candidates:
        return IndependentOutcome(comparison.STATE_EMPTY, 0, None, None, None)

    best_score = max(record[3] for record in candidates)
    maximizers = [record for record in candidates if record[3] == best_score]
    if len(maximizers) == 1:
        quadruple, past, future, _ = maximizers[0]
        selection = IndependentSelection(quadruple, past, future)
        state = comparison.STATE_UNIQUE
    else:
        selection = None
        state = comparison.STATE_TIE
    return IndependentOutcome(
        state=state,
        n_maximizers=len(maximizers),
        primary_score=best_score[0],
        secondary_score=best_score[1],
        selection=selection,
    )


def _optimized_signature(outcome: comparison.ScoreOutcome) -> tuple[object, ...]:
    selection = outcome.selection
    selection_signature = (
        None
        if selection is None
        else (selection.quadruple, selection.past_size, selection.future_size)
    )
    return (
        outcome.state,
        outcome.n_maximizers,
        outcome.primary_score,
        outcome.secondary_score,
        selection_signature,
    )


def _independent_signature(outcome: IndependentOutcome) -> tuple[object, ...]:
    selection = outcome.selection
    selection_signature = (
        None
        if selection is None
        else (selection.quadruple, selection.past_size, selection.future_size)
    )
    return (
        outcome.state,
        outcome.n_maximizers,
        outcome.primary_score,
        outcome.secondary_score,
        selection_signature,
    )


def _shape_for_side(
    permutation: Sequence[int],
    selection: comparison.Selection,
    side: str,
) -> tuple[int, int, int, int]:
    a, b, c, d = selection.quadruple
    if side == "PAST":
        x, y, m = a, b, selection.past_size
    elif side == "FUTURE":
        x, y, m = c, d, selection.future_size
    else:
        raise ValueError(f"unknown side: {side}")
    k = y - x
    l = int(permutation[y]) - int(permutation[x])
    r = k * l
    return m, k, l, r


def _validate_shape(n: int, shape: tuple[int, int, int, int]) -> None:
    m, k, l, r = shape
    if not (
        n >= 6
        and 3 <= m <= n - 3
        and m - 1 <= k <= n - 4
        and m - 1 <= l <= n - 4
        and k + l <= n + m - 2
        and r == k * l
    ):
        raise RuntimeError(f"EF1 support envelope failed at n={n}: {shape}")


def _add_unique_shapes(
    aggregate: ExactFiberAggregate,
    permutation: Sequence[int],
    selection: comparison.Selection,
) -> None:
    for side in SIDES:
        m, k, l, r = _shape_for_side(permutation, selection, side)
        _validate_shape(aggregate.n, (m, k, l, r))
        aggregate.omega[(side, m, k, l, r)] += 1
        aggregate.c_counts[(side, m, r)] += 1


def _read_sidecar_digest(path: Path) -> str:
    sidecar = path.with_suffix(path.suffix + ".sha256")
    if not path.exists() or not sidecar.exists():
        raise FileNotFoundError(f"missing frozen artifact or sidecar: {path}")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    fields = sidecar.read_text(encoding="utf-8").strip().split()
    if len(fields) != 2 or fields[0] != digest or fields[1] != path.name:
        raise RuntimeError(f"frozen sidecar mismatch: {sidecar}")
    return digest


def load_legacy_coverage_counts(
    path: Path = LEGACY_EXACT_PATH,
) -> tuple[dict[int, Counter[str]], str]:
    """Load the frozen coverage-selector state counts, collapsing tie subtypes."""

    digest = _read_sidecar_digest(path)
    counts = {n: Counter() for n in EXACT_N}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["method"] != "EXACT":
                continue
            n = int(row["n"])
            if n not in counts:
                continue
            state = row["state"]
            if state not in (comparison.STATE_EMPTY, comparison.STATE_UNIQUE):
                state = comparison.STATE_TIE
            counts[n][state] += int(row["count"])
    for n in EXACT_N:
        if sum(counts[n].values()) != math.factorial(n):
            raise RuntimeError(f"invalid frozen coverage counts at n={n}")
    return counts, digest


def enumerate_exact(
    n_values: Iterable[int] = EXACT_N,
    *,
    legacy_expected: dict[int, Counter[str]] | None = None,
) -> list[ExactFiberAggregate]:
    n_sequence = tuple(int(n) for n in n_values)
    if any(n not in EXACT_N for n in n_sequence):
        raise ValueError(f"n values must be a subset of {EXACT_N}")
    if legacy_expected is None:
        legacy_expected, _ = load_legacy_coverage_counts()

    aggregates: list[ExactFiberAggregate] = []
    for n in n_sequence:
        aggregate = ExactFiberAggregate(n=n)
        for permutation in permutations(range(n)):
            outcomes = comparison.evaluate_selectors(permutation)
            optimized = outcomes[comparison.MIN_COVERAGE_LEX]
            legacy = outcomes[comparison.COVERAGE]

            aggregate.permutations += 1
            aggregate.state_counts[optimized.state] += 1
            aggregate.legacy_coverage_counts[legacy.state] += 1

            if n in INDEPENDENT_CROSSCHECK_N:
                independent = evaluate_lex_naive(permutation)
                if _optimized_signature(optimized) != _independent_signature(independent):
                    raise RuntimeError(
                        "independent MIN_COVERAGE_LEX mismatch "
                        f"at n={n}, permutation={permutation}"
                    )
                aggregate.independent_crosschecks += 1

            if optimized.state == comparison.STATE_UNIQUE:
                if optimized.selection is None:
                    raise RuntimeError("UNIQUE outcome missing selected quadruple")
                _add_unique_shapes(aggregate, permutation, optimized.selection)
            elif optimized.selection is not None:
                raise RuntimeError("non-UNIQUE outcome unexpectedly has a selection")

        validate_aggregate(aggregate, legacy_expected[n])
        aggregates.append(aggregate)
        print(
            "EF2_EXACT "
            f"N={n} PERMUTATIONS={aggregate.permutations} "
            f"EMPTY={aggregate.state_counts[comparison.STATE_EMPTY]} "
            f"UNIQUE={aggregate.state_counts[comparison.STATE_UNIQUE]} "
            f"TIE={aggregate.state_counts[comparison.STATE_TIE]}",
            flush=True,
        )
    return aggregates


def validate_aggregate(
    aggregate: ExactFiberAggregate,
    legacy_expected: Counter[str],
) -> None:
    n = aggregate.n
    expected_total = math.factorial(n)
    if aggregate.permutations != expected_total:
        raise RuntimeError(f"factorial total mismatch at n={n}")
    if sum(aggregate.state_counts[state] for state in STATES) != expected_total:
        raise RuntimeError(f"MIN_COVERAGE_LEX state partition mismatch at n={n}")
    if aggregate.legacy_coverage_counts != legacy_expected:
        raise RuntimeError(f"frozen coverage-state reproduction failed at n={n}")
    if (
        aggregate.state_counts[comparison.STATE_EMPTY]
        != aggregate.legacy_coverage_counts[comparison.STATE_EMPTY]
    ):
        raise RuntimeError(f"selector-independent EMPTY control failed at n={n}")

    unique = aggregate.state_counts[comparison.STATE_UNIQUE]
    for side in SIDES:
        omega_total = sum(
            count for (key_side, *_), count in aggregate.omega.items() if key_side == side
        )
        c_total = sum(
            count for (key_side, *_), count in aggregate.c_counts.items() if key_side == side
        )
        if omega_total != unique or c_total != unique:
            raise RuntimeError(f"unique fiber total mismatch at n={n}, side={side}")

    derived_c: Counter[CKey] = Counter()
    for (side, m, k, l, r), count in aggregate.omega.items():
        _validate_shape(n, (m, k, l, r))
        if aggregate.omega[(side, m, l, k, r)] != count:
            raise RuntimeError(f"U/V Omega symmetry failed at n={n}")
        other_side = "FUTURE" if side == "PAST" else "PAST"
        if aggregate.omega[(other_side, m, k, l, r)] != count:
            raise RuntimeError(f"PAST/FUTURE Omega symmetry failed at n={n}")
        derived_c[(side, m, r)] += count
    if derived_c != aggregate.c_counts:
        raise RuntimeError(f"Omega-to-C aggregation failed at n={n}")

    for (side, m, r), count in aggregate.c_counts.items():
        other_side = "FUTURE" if side == "PAST" else "PAST"
        if aggregate.c_counts[(other_side, m, r)] != count:
            raise RuntimeError(f"PAST/FUTURE C symmetry failed at n={n}")

    expected_crosschecks = expected_total if n in INDEPENDENT_CROSSCHECK_N else 0
    if aggregate.independent_crosschecks != expected_crosschecks:
        raise RuntimeError(f"independent crosscheck total failed at n={n}")


def state_rows(aggregates: Sequence[ExactFiberAggregate]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for aggregate in aggregates:
        for state in STATES:
            count = aggregate.state_counts[state]
            rows.append(
                {
                    "selector": comparison.MIN_COVERAGE_LEX,
                    "n": aggregate.n,
                    "permutations": aggregate.permutations,
                    "state": state,
                    "count": count,
                    "probability": count / aggregate.permutations,
                }
            )
    return rows


def omega_rows(aggregates: Sequence[ExactFiberAggregate]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for aggregate in aggregates:
        for (side, m, k, l, r), count in sorted(aggregate.omega.items()):
            rows.append(
                {"n": aggregate.n, "side": side, "m": m, "k": k, "l": l, "r": r, "count": count}
            )
    return rows


def c_rows(aggregates: Sequence[ExactFiberAggregate]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for aggregate in aggregates:
        for (side, m, r), count in sorted(aggregate.c_counts.items()):
            rows.append(
                {"n": aggregate.n, "side": side, "m": m, "r": r, "count": count}
            )
    return rows


def rows_to_csv(rows: Sequence[dict[str, object]], fields: Sequence[str]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


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


def _summary_record(aggregate: ExactFiberAggregate) -> dict[str, object]:
    reachable_m = sorted({m for _, m, _, _, _ in aggregate.omega})
    reachable_r = sorted({r for _, _, _, _, r in aggregate.omega})
    return {
        "n": aggregate.n,
        "permutations": aggregate.permutations,
        "state_counts": {state: aggregate.state_counts[state] for state in STATES},
        "legacy_coverage_counts": {
            state: aggregate.legacy_coverage_counts[state] for state in STATES
        },
        "unique_side_records": sum(aggregate.omega.values()),
        "omega_rows": len(aggregate.omega),
        "c_rows": len(aggregate.c_counts),
        "reachable_m": reachable_m,
        "reachable_r": reachable_r,
        "independent_crosschecks": aggregate.independent_crosschecks,
    }


def execute(output_dir: Path, *, overwrite: bool = False) -> dict[str, object]:
    output_paths = {
        STATE_FILENAME: output_dir / STATE_FILENAME,
        OMEGA_FILENAME: output_dir / OMEGA_FILENAME,
        C_FILENAME: output_dir / C_FILENAME,
        SUMMARY_FILENAME: output_dir / SUMMARY_FILENAME,
    }
    prospective = tuple(output_paths.values()) + tuple(
        path.with_suffix(path.suffix + ".sha256") for path in output_paths.values()
    )
    if not overwrite:
        existing = [str(path) for path in prospective if path.exists()]
        if existing:
            raise FileExistsError("refusing to overwrite: " + ", ".join(existing))

    legacy_expected, legacy_digest = load_legacy_coverage_counts()
    aggregates = enumerate_exact(legacy_expected=legacy_expected)

    data_by_name = {
        STATE_FILENAME: rows_to_csv(state_rows(aggregates), STATE_FIELDS),
        OMEGA_FILENAME: rows_to_csv(omega_rows(aggregates), OMEGA_FIELDS),
        C_FILENAME: rows_to_csv(c_rows(aggregates), C_FIELDS),
    }
    artifact_hashes: dict[str, str] = {}
    for filename, data in data_by_name.items():
        artifact_hashes[filename] = _write_with_sidecar(
            output_paths[filename], data, overwrite=overwrite
        )

    summary: dict[str, object] = {
        "schema_version": "p1a_entropia_fibras_ef2_v1",
        "contract_status": "EF0_EF1_FIXED_BEFORE_ENUMERATION",
        "selector": comparison.MIN_COVERAGE_LEX,
        "sample_space": "uniform_permutations_conditioned_on_N_equals_n",
        "exact_n": list(EXACT_N),
        "independent_crosscheck_n": list(INDEPENDENT_CROSSCHECK_N),
        "recorded_fields": ["M", "K", "L", "r=KL"],
        "legacy_control": {
            "artifact": str(LEGACY_EXACT_PATH.relative_to(HERE.parent)),
            "selector": comparison.COVERAGE,
            "comparison": "EMPTY_UNIQUE_TIE_AFTER_COLLAPSING_FROZEN_TIE_SUBTYPES",
            "sha256": legacy_digest,
            "pass": True,
        },
        "validations": {
            "factorial_totals": True,
            "state_partitions": True,
            "legacy_state_reproduction": True,
            "independent_implementation": True,
            "omega_uv_symmetry": True,
            "omega_past_future_symmetry": True,
            "ef1_support_envelope": True,
            "omega_to_c_aggregation": True,
        },
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
            "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "artifacts": {
            filename: {"sha256": digest}
            for filename, digest in artifact_hashes.items()
        },
        "by_n": [_summary_record(aggregate) for aggregate in aggregates],
        "terminal": "EXACT_SMALL_N_FIBER_TABLES_VALIDATED",
        "claim_ceiling": "EXACT_N_6_TO_9_ONLY_NO_ASYMPTOTIC_INFERENCE",
        "monte_carlo": "NOT_RUN",
        "gauss_kuzmin": "NOT_USED",
    }
    summary_data = (json.dumps(summary, indent=2, sort_keys=True) + "\n").encode("utf-8")
    summary_digest = _write_with_sidecar(
        output_paths[SUMMARY_FILENAME], summary_data, overwrite=overwrite
    )

    print("EF2_VALIDATION=PASS")
    for filename, digest in artifact_hashes.items():
        print(f"EF2_SHA256 {filename}={digest}")
    print(f"EF2_SHA256 {SUMMARY_FILENAME}={summary_digest}")
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="new EF-2 artifact directory",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="explicitly replace only the new EF-2 artifacts",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        execute(args.output_dir, overwrite=args.overwrite)
    except (FileExistsError, FileNotFoundError, RuntimeError, ValueError) as exc:
        print("EF2_VALIDATION=FAIL", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
