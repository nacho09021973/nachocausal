#!/usr/bin/env python3
"""EF-3 deterministic checks for the COUNT_VOLUME fiber reduction in d=2.

This module performs no permutation enumeration and no Monte Carlo simulation.  It
checks two consequences of the EF-3 argument against the frozen EF-2 artifacts:

* the RSK recurrence for the number of EMPTY permutations; and
* the exact finite-n Q2 moments obtained from the frozen C_n(m, r; S) table.

It writes no files.  The concentration theorem and its claim ceiling are recorded
in ``docs/hoja_de_ruta_agosto_2026.md``.
"""

from __future__ import annotations

import csv
import math
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Iterable, Iterator, Sequence


HERE = Path(__file__).resolve().parent
RESULTS_DIR = HERE / "resultados"
STATE_PATH = RESULTS_DIR / "p1a_entropia_fibras_estados_exactos_d2.csv"
C_PATH = RESULTS_DIR / "p1a_entropia_fibras_c_exacta_d2.csv"

EXACT_N = (6, 7, 8, 9)
SIDES = ("PAST", "FUTURE")
LIS_THRESHOLD = 6


Shape = tuple[int, ...]


@dataclass(frozen=True)
class MomentSummary:
    n: int
    side: str
    unique_count: int
    q2: float
    rectangle_proxy_mse: float


def integer_partitions(n: int, max_part: int | None = None) -> Iterator[Shape]:
    """Yield integer partitions of ``n`` in nonincreasing order."""

    if n < 0:
        raise ValueError("n must be nonnegative")
    if n == 0:
        yield ()
        return
    upper = n if max_part is None else min(n, max_part)
    for first in range(upper, 0, -1):
        for tail in integer_partitions(n - first, first):
            yield (first, *tail)


def removable_corner_shapes(shape: Shape) -> tuple[Shape, ...]:
    """Return the Young shapes obtained by deleting one removable corner."""

    if any(value <= 0 for value in shape) or any(
        shape[index] < shape[index + 1] for index in range(len(shape) - 1)
    ):
        raise ValueError(f"not a partition: {shape}")
    children: list[Shape] = []
    for index, row_length in enumerate(shape):
        next_length = shape[index + 1] if index + 1 < len(shape) else 0
        if row_length == next_length:
            continue
        child = list(shape)
        child[index] -= 1
        if child[index] == 0:
            child.pop(index)
        children.append(tuple(child))
    return tuple(children)


@lru_cache(maxsize=None)
def standard_tableaux_count(shape: Shape) -> int:
    """Count standard Young tableaux by the corner-removal recurrence."""

    if not shape:
        return 1
    return sum(standard_tableaux_count(child) for child in removable_corner_shapes(shape))


def hook_length_tableaux_count(shape: Shape) -> int:
    """Independent hook-length evaluation used to check the recurrence."""

    size = sum(shape)
    hook_product = 1
    for row_index, row_length in enumerate(shape):
        for column_index in range(row_length):
            below = sum(
                column_index < lower_row_length
                for lower_row_length in shape[row_index + 1 :]
            )
            hook_product *= row_length - column_index + below
    return math.factorial(size) // hook_product


def empty_count_rsk(n: int) -> int:
    """Count permutations with no selector candidate, equivalently LIS <= 5."""

    return sum(
        standard_tableaux_count(shape) ** 2
        for shape in integer_partitions(n, LIS_THRESHOLD - 1)
    )


def lis_length(permutation: Sequence[int]) -> int:
    """Return the longest increasing subsequence length by patience sorting."""

    tails: list[int] = []
    for raw_value in permutation:
        value = int(raw_value)
        lo = 0
        hi = len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] < value:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(tails):
            tails.append(value)
        else:
            tails[lo] = value
    return len(tails)


def closed_rectangle_correction(n: int, k: int, l: int) -> float:
    """Return the deterministic normalization correction in EF-3.2."""

    if n <= 0 or not (0 <= k <= n - 1 and 0 <= l <= n - 1):
        raise ValueError("expected 0 <= k,l <= n-1 and n > 0")
    closed_area = ((k + 1) * (l + 1)) / (n * n)
    z_squared = (k * l) / ((n + 1) * (n + 1))
    return closed_area - z_squared


def discrepancy_tail_bound(n: int, epsilon: float) -> float:
    """Union-bound tail for normalized interval-rectangle discrepancy."""

    if n <= 0 or epsilon < 0:
        raise ValueError("expected n > 0 and epsilon >= 0")
    return min(1.0, 2.0 * n**4 * math.exp(-2.0 * n * epsilon**2))


def conditional_q2_bound(n: int, selection_probability: float, epsilon: float) -> float:
    """Finite-n EF-3 bound Q2 <= eps + 4/n + Pr(Delta>eps)/Pr(S)."""

    if not 0.0 < selection_probability <= 1.0:
        raise ValueError("selection_probability must lie in (0, 1]")
    return (
        epsilon
        + 4.0 / n
        + discrepancy_tail_bound(n, epsilon) / selection_probability
    )


def load_state_counts(path: Path = STATE_PATH) -> dict[int, dict[str, int]]:
    counts: dict[int, dict[str, int]] = defaultdict(dict)
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            counts[int(row["n"])][row["state"]] = int(row["count"])
    return dict(counts)


def load_c_rows(path: Path = C_PATH) -> list[tuple[int, str, int, int, int]]:
    rows: list[tuple[int, str, int, int, int]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rows.append(
                (
                    int(row["n"]),
                    row["side"],
                    int(row["m"]),
                    int(row["r"]),
                    int(row["count"]),
                )
            )
    return rows


def exact_moment_summaries(
    rows: Iterable[tuple[int, str, int, int, int]],
) -> dict[tuple[int, str], MomentSummary]:
    """Evaluate EF1.16 and a projection control from exact C-table rows."""

    grouped: dict[tuple[int, str, int], list[tuple[int, int]]] = defaultdict(list)
    for n, side, m, r, count in rows:
        grouped[(n, side, m)].append((r, count))

    by_side: dict[
        tuple[int, str], list[tuple[int, list[tuple[int, int]]]]
    ] = defaultdict(list)
    for (n, side, m), entries in grouped.items():
        by_side[(n, side)].append((m, entries))

    summaries: dict[tuple[int, str], MomentSummary] = {}
    for (n, side), strata in by_side.items():
        unique_count = sum(count for _, entries in strata for _, count in entries)
        q2_numerator = 0.0
        proxy_squared_error = 0.0
        for m, entries in strata:
            d_nm = sum(count for _, count in entries)
            a_nm = math.fsum(math.sqrt(r) * count for r, count in entries)
            b_nm = sum(r * count for r, count in entries)
            q2_numerator += b_nm - a_nm * a_nm / d_nm
            proxy = math.sqrt(m / n)
            proxy_squared_error += math.fsum(
                count * (math.sqrt(r) / (n + 1) - proxy) ** 2
                for r, count in entries
            )
        q2 = q2_numerator / ((n + 1) ** 2 * unique_count)
        summaries[(n, side)] = MomentSummary(
            n=n,
            side=side,
            unique_count=unique_count,
            q2=max(0.0, q2),
            rectangle_proxy_mse=proxy_squared_error / unique_count,
        )
    return summaries


def verify_frozen_ef2() -> dict[tuple[int, str], MomentSummary]:
    """Run every deterministic EF-3 control against the frozen EF-2 tables."""

    state_counts = load_state_counts()
    summaries = exact_moment_summaries(load_c_rows())
    if tuple(sorted(state_counts)) != EXACT_N:
        raise RuntimeError("unexpected EF-2 n support")

    for n in EXACT_N:
        recurrent_empty = empty_count_rsk(n)
        if recurrent_empty != state_counts[n]["EMPTY"]:
            raise RuntimeError(f"RSK EMPTY mismatch at n={n}")
        nonempty = math.factorial(n) - recurrent_empty
        if nonempty != state_counts[n]["UNIQUE"] + state_counts[n]["TIE"]:
            raise RuntimeError(f"EMPTY/UNIQUE/TIE partition mismatch at n={n}")

        past = summaries[(n, "PAST")]
        future = summaries[(n, "FUTURE")]
        if past.unique_count != state_counts[n]["UNIQUE"]:
            raise RuntimeError(f"C-table normalization mismatch at n={n}")
        if past.unique_count != future.unique_count:
            raise RuntimeError(f"side count mismatch at n={n}")
        if not math.isclose(past.q2, future.q2, rel_tol=0.0, abs_tol=1e-15):
            raise RuntimeError(f"side Q2 mismatch at n={n}")
        if past.q2 > past.rectangle_proxy_mse + 1e-15:
            raise RuntimeError(f"conditional projection control failed at n={n}")

    for n in range(1, 20):
        for shape in integer_partitions(n, LIS_THRESHOLD - 1):
            if standard_tableaux_count(shape) != hook_length_tableaux_count(shape):
                raise RuntimeError(f"tableau recurrence mismatch for {shape}")

    return summaries


def main() -> int:
    state_counts = load_state_counts()
    summaries = verify_frozen_ef2()
    for n in EXACT_N:
        states = state_counts[n]
        summary = summaries[(n, "PAST")]
        print(
            "EF3_CHECK "
            f"N={n} EMPTY_RSK={empty_count_rsk(n)} "
            f"UNIQUE={states['UNIQUE']} TIE={states['TIE']} "
            f"Q2={summary.q2:.12g} "
            f"RECTANGLE_PROXY_MSE={summary.rectangle_proxy_mse:.12g}"
        )
    print("EF3_RSK_EMPTY_RECURRENCE=PASS")
    print("EF3_EF1_MOMENT_IDENTITY=PASS")
    print("EF3_PROJECTION_CONTROL=PASS")
    print("EF3_TERMINAL=OPEN_AFTER_FIBER_AUDIT")
    print("EF3_OPEN_OBLIGATION=SUBEXPONENTIAL_LOWER_BOUND_ON_UNIQUE_SELECTION")
    print("EF3_MONTE_CARLO=NOT_RUN")
    print("EF3_GAUSS_KUZMIN=NOT_USED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
