#!/usr/bin/env python3
"""P1a exact enumeration and d=2 Monte Carlo under the frozen v1.0 contract.

The input law is a uniform permutation.  Its product order is the causal order of
an iid sprinkling in a 1+1-dimensional Minkowski diamond conditional on N=n.

This executable classifies only selector availability and tie mechanisms.  It does
not calculate longest-chain ratios or make metric claims.
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
from dataclasses import asdict, dataclass
from functools import lru_cache
from itertools import permutations
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np


K0 = 3
EXACT_N = (6, 7, 8, 9)
MC_N = (6, 7, 8, 9, 12, 16, 24, 32, 48, 64)
MC_REPLICATES_PER_N = 20_000
MC_BATCHES = 8
MC_REPLICATES_PER_BATCH = 2_500
SEED_BASE = 2_608_030_000
GATE_N = (32, 48, 64)
WILSON_Z = 1.959963984540054
VIABLE_LOWER = 0.10
PARK_UPPER = 0.01

STATE_EMPTY = "EMPTY"
STATE_UNIQUE = "UNIQUE"
STATE_TIE_BRIDGE = "TIE_BRIDGE_ONLY"
STATE_TIE_PAST = "TIE_PAST_ENDPOINT"
STATE_TIE_FUTURE = "TIE_FUTURE_ENDPOINT"
STATE_TIE_MIXED = "TIE_MIXED"
STATES = (
    STATE_EMPTY,
    STATE_UNIQUE,
    STATE_TIE_BRIDGE,
    STATE_TIE_PAST,
    STATE_TIE_FUTURE,
    STATE_TIE_MIXED,
)
TIE_STATES = STATES[2:]

TERMINAL_IMPLEMENTATION_INVALID = "IMPLEMENTATION_INVALID"
TERMINAL_CROSSCHECK_FAILED = "MC_EXACT_CROSSCHECK_FAILED"
TERMINAL_VIABLE = "POINT_SELECTOR_OPERATIONALLY_VIABLE"
TERMINAL_PARK = "POINT_SELECTOR_PARK_SET_VALUED_ONLY"
TERMINAL_INCONCLUSIVE = "POINT_SELECTOR_VIABILITY_INCONCLUSIVE"

CSV_FIELDS = (
    "method",
    "n",
    "replicates",
    "state",
    "count",
    "probability",
    "ci95_low",
    "ci95_high",
)

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = HERE / "resultados"
EXACT_FILENAME = "p1a_enumeracion_exacta_d2.csv"
MC_FILENAME = "p1a_monte_carlo_d2.csv"
SUMMARY_FILENAME = "p1a_ejecucion_resumen.json"


@dataclass(frozen=True)
class SelectorOutcome:
    state: str
    n_maximizers: int
    max_score: int
    n_maximizing_bridges: int
    bridge_tie: bool
    past_endpoint_tie: bool
    future_endpoint_tie: bool


@dataclass
class Aggregate:
    n: int
    method: str
    replicates: int = 0
    counts: Counter[str] | None = None
    tie_maximizers_sum: int = 0
    tie_replicates: int = 0
    max_maximizers: int = 0
    nonempty_coverage_fraction_sum: float = 0.0
    nonempty_replicates: int = 0
    maximizing_bridges_sum: int = 0
    past_tie_replicates: int = 0
    future_tie_replicates: int = 0

    def __post_init__(self) -> None:
        if self.counts is None:
            self.counts = Counter()

    def add(self, outcome: SelectorOutcome) -> None:
        assert self.counts is not None
        self.replicates += 1
        self.counts[outcome.state] += 1
        self.max_maximizers = max(self.max_maximizers, outcome.n_maximizers)
        if outcome.state != STATE_EMPTY:
            self.nonempty_replicates += 1
            self.nonempty_coverage_fraction_sum += outcome.max_score / self.n
            self.maximizing_bridges_sum += outcome.n_maximizing_bridges
        if outcome.state in TIE_STATES:
            self.tie_replicates += 1
            self.tie_maximizers_sum += outcome.n_maximizers
        if outcome.past_endpoint_tie:
            self.past_tie_replicates += 1
        if outcome.future_endpoint_tie:
            self.future_tie_replicates += 1

    def diagnostic_dict(self) -> dict[str, object]:
        return {
            "method": self.method,
            "n": self.n,
            "replicates": self.replicates,
            "mean_maximizers_given_tie": (
                self.tie_maximizers_sum / self.tie_replicates
                if self.tie_replicates
                else None
            ),
            "max_maximizers_observed": self.max_maximizers,
            "mean_coverage_fraction_given_nonempty": (
                self.nonempty_coverage_fraction_sum / self.nonempty_replicates
                if self.nonempty_replicates
                else None
            ),
            "mean_maximizing_bridges_given_nonempty": (
                self.maximizing_bridges_sum / self.nonempty_replicates
                if self.nonempty_replicates
                else None
            ),
            "past_endpoint_tie_fraction": self.past_tie_replicates / self.replicates,
            "future_endpoint_tie_fraction": self.future_tie_replicates / self.replicates,
        }


@lru_cache(maxsize=None)
def _index_grids(n: int) -> tuple[np.ndarray, np.ndarray]:
    idx = np.arange(n, dtype=np.int64)
    return np.broadcast_arrays(idx[:, None], idx[None, :])


def validate_permutation(permutation: Sequence[int]) -> np.ndarray:
    perm = np.asarray(permutation, dtype=np.int64)
    if perm.ndim != 1:
        raise ValueError("permutation must be one-dimensional")
    n = len(perm)
    if n == 0 or not np.array_equal(np.sort(perm), np.arange(n)):
        raise ValueError("expected a permutation of range(n)")
    return perm


def interval_count_matrix(permutation: Sequence[int]) -> tuple[np.ndarray, np.ndarray]:
    """Return closed-interval cardinalities and the product-order relation.

    Matrix entry (i,j) is zero unless i precedes j.  Otherwise it is the number
    of permutation points in the inclusive axis-aligned rectangle with corners
    (i,pi[i]) and (j,pi[j]).
    """

    perm = validate_permutation(permutation)
    n = len(perm)
    points = np.zeros((n, n), dtype=np.int32)
    points[np.arange(n), perm] = 1
    prefix = np.zeros((n + 1, n + 1), dtype=np.int32)
    prefix[1:, 1:] = points.cumsum(axis=0).cumsum(axis=1)

    i_grid, j_grid = _index_grids(n)
    vi = perm[:, None]
    vj = perm[None, :]
    comparable = (i_grid < j_grid) & (vi < vj)
    counts = (
        prefix[j_grid + 1, vj + 1]
        - prefix[i_grid, vj + 1]
        - prefix[j_grid + 1, vi]
        + prefix[i_grid, vi]
    )
    counts = np.where(comparable, counts, 0).astype(np.int32, copy=False)
    return counts, comparable


def classify_permutation(permutation: Sequence[int]) -> SelectorOutcome:
    counts, comparable = interval_count_matrix(permutation)
    eligible = counts >= K0

    left_values = np.where(eligible, counts, -1)
    left_max = left_values.max(axis=0)
    left_mult = ((counts == left_max[None, :]) & eligible).sum(axis=0)

    right_values = np.where(eligible, counts, -1)
    right_max = right_values.max(axis=1)
    right_mult = ((counts == right_max[:, None]) & eligible).sum(axis=1)

    bridges = (
        comparable
        & (left_max[:, None] >= K0)
        & (right_max[None, :] >= K0)
    )
    if not bool(bridges.any()):
        return SelectorOutcome(
            state=STATE_EMPTY,
            n_maximizers=0,
            max_score=0,
            n_maximizing_bridges=0,
            bridge_tie=False,
            past_endpoint_tie=False,
            future_endpoint_tie=False,
        )

    bridge_scores = left_max[:, None] + right_max[None, :]
    max_score = int(bridge_scores[bridges].max())
    maximizing_bridges = bridges & (bridge_scores == max_score)
    bridge_rows, bridge_cols = np.nonzero(maximizing_bridges)
    n_bridges = len(bridge_rows)
    n_maximizers = sum(
        int(left_mult[b]) * int(right_mult[c])
        for b, c in zip(bridge_rows, bridge_cols)
    )
    bridge_tie = n_bridges > 1
    past_tie = any(int(left_mult[b]) > 1 for b in bridge_rows)
    future_tie = any(int(right_mult[c]) > 1 for c in bridge_cols)

    if n_maximizers == 1:
        state = STATE_UNIQUE
    else:
        flags = (bridge_tie, past_tie, future_tie)
        if flags == (True, False, False):
            state = STATE_TIE_BRIDGE
        elif flags == (False, True, False):
            state = STATE_TIE_PAST
        elif flags == (False, False, True):
            state = STATE_TIE_FUTURE
        else:
            state = STATE_TIE_MIXED

    return SelectorOutcome(
        state=state,
        n_maximizers=n_maximizers,
        max_score=max_score,
        n_maximizing_bridges=n_bridges,
        bridge_tie=bridge_tie,
        past_endpoint_tie=past_tie,
        future_endpoint_tie=future_tie,
    )


def wilson_interval(successes: int, trials: int, z: float = WILSON_Z) -> tuple[float, float]:
    if trials <= 0 or not 0 <= successes <= trials:
        raise ValueError("invalid binomial counts")
    p = successes / trials
    z2 = z * z
    denominator = 1.0 + z2 / trials
    center = (p + z2 / (2.0 * trials)) / denominator
    half = (
        z
        * math.sqrt(p * (1.0 - p) / trials + z2 / (4.0 * trials * trials))
        / denominator
    )
    return max(0.0, center - half), min(1.0, center + half)


def aggregate_rows(aggregate: Aggregate) -> list[dict[str, object]]:
    assert aggregate.counts is not None
    rows: list[dict[str, object]] = []
    for state in STATES:
        count = aggregate.counts[state]
        probability = count / aggregate.replicates
        if aggregate.method == "EXACT":
            low, high = probability, probability
        else:
            low, high = wilson_interval(count, aggregate.replicates)
        rows.append(
            {
                "method": aggregate.method,
                "n": aggregate.n,
                "replicates": aggregate.replicates,
                "state": state,
                "count": count,
                "probability": probability,
                "ci95_low": low,
                "ci95_high": high,
            }
        )
    return rows


def enumerate_exact(n_values: Iterable[int] = EXACT_N) -> list[Aggregate]:
    aggregates: list[Aggregate] = []
    for n in n_values:
        aggregate = Aggregate(n=n, method="EXACT")
        for perm in permutations(range(n)):
            aggregate.add(classify_permutation(perm))
        expected = math.factorial(n)
        if aggregate.replicates != expected:
            raise RuntimeError(f"exact enumeration count mismatch at n={n}")
        aggregates.append(aggregate)
        print(f"P1A_EXACT_N={n} PERMUTATIONS={expected}", flush=True)
    return aggregates


def seed_for(n: int, batch: int) -> int:
    if not 0 <= batch < MC_BATCHES:
        raise ValueError("batch outside frozen range")
    return SEED_BASE + 100 * n + batch


def simulate_monte_carlo(n_values: Iterable[int] = MC_N) -> list[Aggregate]:
    aggregates: list[Aggregate] = []
    for n in n_values:
        aggregate = Aggregate(n=n, method="MONTE_CARLO")
        for batch in range(MC_BATCHES):
            rng = np.random.Generator(np.random.PCG64(seed_for(n, batch)))
            for _ in range(MC_REPLICATES_PER_BATCH):
                aggregate.add(classify_permutation(rng.permutation(n)))
        if aggregate.replicates != MC_REPLICATES_PER_N:
            raise RuntimeError(f"Monte Carlo count mismatch at n={n}")
        aggregates.append(aggregate)
        print(
            f"P1A_MC_N={n} REPLICATES={MC_REPLICATES_PER_N}",
            flush=True,
        )
    return aggregates


def validate_state_partition(aggregates: Iterable[Aggregate]) -> None:
    for aggregate in aggregates:
        assert aggregate.counts is not None
        total = sum(aggregate.counts[state] for state in STATES)
        if total != aggregate.replicates:
            raise RuntimeError(
                f"state partition mismatch method={aggregate.method} n={aggregate.n}"
            )
        tie_total = sum(aggregate.counts[state] for state in TIE_STATES)
        if tie_total != aggregate.tie_replicates:
            raise RuntimeError(
                f"tie partition mismatch method={aggregate.method} n={aggregate.n}"
            )


def validate_analytic_controls(exact: Sequence[Aggregate]) -> None:
    by_n = {aggregate.n: aggregate for aggregate in exact}
    n6 = by_n.get(6)
    n7 = by_n.get(7)
    if n6 is None or n7 is None or n6.counts is None or n7.counts is None:
        raise RuntimeError("missing n=6 or n=7 exact analytic control")
    if (
        n6.counts[STATE_EMPTY] != 719
        or n6.counts[STATE_UNIQUE] != 1
        or sum(n6.counts[state] for state in TIE_STATES) != 0
    ):
        raise RuntimeError("n=6 analytic control failed")
    if n7.counts[STATE_EMPTY] != 5003:
        raise RuntimeError("n=7 RSK empty-count control failed")


def crosscheck_exact_mc(
    exact: Sequence[Aggregate], mc: Sequence[Aggregate]
) -> tuple[bool, list[dict[str, object]]]:
    exact_by_n = {aggregate.n: aggregate for aggregate in exact}
    mc_by_n = {aggregate.n: aggregate for aggregate in mc}
    records: list[dict[str, object]] = []
    passed = True
    for n in EXACT_N:
        exact_aggregate = exact_by_n[n]
        mc_aggregate = mc_by_n[n]
        assert exact_aggregate.counts is not None and mc_aggregate.counts is not None
        for state in STATES:
            p_exact = exact_aggregate.counts[state] / exact_aggregate.replicates
            p_mc = mc_aggregate.counts[state] / mc_aggregate.replicates
            if p_exact == 0.0:
                tolerance = 0.0
            else:
                tolerance = (
                    6.0
                    * math.sqrt(
                        p_exact * (1.0 - p_exact) / mc_aggregate.replicates
                    )
                    + 1.0 / mc_aggregate.replicates
                )
            ok = abs(p_mc - p_exact) <= tolerance
            passed = passed and ok
            records.append(
                {
                    "n": n,
                    "state": state,
                    "p_exact": p_exact,
                    "p_mc": p_mc,
                    "absolute_error": abs(p_mc - p_exact),
                    "tolerance": tolerance,
                    "pass": ok,
                }
            )
    return passed, records


def scientific_terminal(mc: Sequence[Aggregate]) -> tuple[str, dict[str, object]]:
    by_n = {aggregate.n: aggregate for aggregate in mc}
    gate_records: dict[str, object] = {}
    all_viable = True
    all_park = True
    for n in GATE_N:
        aggregate = by_n[n]
        assert aggregate.counts is not None
        count = aggregate.counts[STATE_UNIQUE]
        low, high = wilson_interval(count, aggregate.replicates)
        gate_records[str(n)] = {
            "unique_count": count,
            "replicates": aggregate.replicates,
            "p_def": count / aggregate.replicates,
            "wilson95_low": low,
            "wilson95_high": high,
        }
        all_viable = all_viable and low >= VIABLE_LOWER
        all_park = all_park and high < PARK_UPPER
    if all_viable:
        return TERMINAL_VIABLE, gate_records
    if all_park:
        return TERMINAL_PARK, gate_records
    return TERMINAL_INCONCLUSIVE, gate_records


def rows_to_csv(rows: Sequence[dict[str, object]]) -> str:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=CSV_FIELDS, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
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
    sidecar = path.with_suffix(path.suffix + ".sha256")
    _atomic_write(
        sidecar,
        f"{digest}  {path.name}\n".encode("utf-8"),
        overwrite=overwrite,
    )
    return digest


def contract_dict() -> dict[str, object]:
    return {
        "k0": K0,
        "exact_n": list(EXACT_N),
        "mc_n": list(MC_N),
        "mc_replicates_per_n": MC_REPLICATES_PER_N,
        "mc_batches": MC_BATCHES,
        "mc_replicates_per_batch": MC_REPLICATES_PER_BATCH,
        "rng": "numpy.random.Generator(numpy.random.PCG64)",
        "seed_base": SEED_BASE,
        "seed_formula": "SEED_BASE + 100*n + batch",
        "gate_n": list(GATE_N),
        "wilson_z": WILSON_Z,
        "viable_lower": VIABLE_LOWER,
        "park_upper": PARK_UPPER,
    }


def execute(output_dir: Path, *, overwrite: bool = False) -> dict[str, object]:
    exact_path = output_dir / EXACT_FILENAME
    mc_path = output_dir / MC_FILENAME
    summary_path = output_dir / SUMMARY_FILENAME
    prospective = (
        exact_path,
        exact_path.with_suffix(exact_path.suffix + ".sha256"),
        mc_path,
        mc_path.with_suffix(mc_path.suffix + ".sha256"),
        summary_path,
        summary_path.with_suffix(summary_path.suffix + ".sha256"),
    )
    if not overwrite:
        existing = [str(path) for path in prospective if path.exists()]
        if existing:
            raise FileExistsError("refusing to overwrite: " + ", ".join(existing))

    exact = enumerate_exact()
    validate_state_partition(exact)
    validate_analytic_controls(exact)

    mc = simulate_monte_carlo()
    validate_state_partition(mc)
    crosscheck_pass, crosscheck_records = crosscheck_exact_mc(exact, mc)

    exact_rows = [row for aggregate in exact for row in aggregate_rows(aggregate)]
    mc_rows = [row for aggregate in mc for row in aggregate_rows(aggregate)]
    exact_data = rows_to_csv(exact_rows).encode("utf-8")
    mc_data = rows_to_csv(mc_rows).encode("utf-8")
    exact_sha = _write_with_sidecar(exact_path, exact_data, overwrite=overwrite)
    mc_sha = _write_with_sidecar(mc_path, mc_data, overwrite=overwrite)

    if crosscheck_pass:
        terminal, gate_records = scientific_terminal(mc)
    else:
        terminal = TERMINAL_CROSSCHECK_FAILED
        gate_records = {}

    summary: dict[str, object] = {
        "schema_version": "p1a_execution_v1",
        "contract_status": "FROZEN_BEFORE_RESULTS",
        "terminal": terminal,
        "crosscheck_pass": crosscheck_pass,
        "contract": contract_dict(),
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "artifacts": {
            EXACT_FILENAME: {"sha256": exact_sha},
            MC_FILENAME: {"sha256": mc_sha},
        },
        "exact_diagnostics": [aggregate.diagnostic_dict() for aggregate in exact],
        "mc_diagnostics": [aggregate.diagnostic_dict() for aggregate in mc],
        "crosscheck": crosscheck_records,
        "gate": gate_records,
        "claim_ceiling": "SELECTOR_AVAILABILITY_ONLY_NO_METRIC_RATIO",
    }
    summary_data = (json.dumps(summary, indent=2, sort_keys=True) + "\n").encode("utf-8")
    summary_sha = _write_with_sidecar(summary_path, summary_data, overwrite=overwrite)
    summary["summary_sha256"] = summary_sha

    print(f"P1A_CROSSCHECK_PASS={str(crosscheck_pass).upper()}")
    print(f"P1A_TERMINAL={terminal}")
    print(f"P1A_EXACT_SHA256={exact_sha}")
    print(f"P1A_MC_SHA256={mc_sha}")
    print(f"P1A_SUMMARY_SHA256={summary_sha}")
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="artifact directory",
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
        print(f"P1A_TERMINAL={TERMINAL_IMPLEMENTATION_INVALID}", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 2
    return 0 if summary["crosscheck_pass"] else 3


if __name__ == "__main__":
    raise SystemExit(main())
