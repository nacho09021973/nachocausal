"""Frozen PR010 development coverage generator.

This program measures only seed-level transition evaluability.  It never emits
widths, geometry, expansion values, or a coverage terminal.  Running it is not
authorized until a separate implementation audit issues PASS_READY_TO_RUN.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
import hashlib
from itertools import combinations
import math
import os
from pathlib import Path
import resource
import signal
import sys
import threading
import time
from typing import Callable, Iterable, Iterator, Mapping, Sequence


# One computational thread plus the budget monitor stay within the frozen
# four-thread process limit.  Existing environment values are overwritten, not
# accepted as configuration overrides.
for _thread_variable in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "NUMEXPR_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "BLIS_NUM_THREADS",
):
    os.environ[_thread_variable] = "1"

import numpy as np
from threadpoolctl import threadpool_limits


_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent
sys.path.insert(0, str(_ROOT))
sys.path.insert(0, str(_HERE))

from nachocausal import estimator, generator  # noqa: E402
import explore_ladders as XL  # noqa: E402


DEVELOPMENT_SEEDS = tuple(range(1_101_000, 1_101_024))
N_DEVELOPMENT_SEEDS = 24
SPACETIME_KINDS = ("BH", "MINK")
INTENSITY = 4_800
T_EDGE = 6.0
M = 3
K = 64
MAX_STARTS = 40
TIE_RANK_MASTER_SEED = 9_009_009
REQUIRED_SLICES = (3, 4, 5, 6)
TRANSITION_DEPTHS = (3, 4, 5)
MAX_DEPTH = 6
BAND_CENTRE = 1.5 * M - 1.0

CSV_FIELDS = (
    "seed",
    "spacetime_kind",
    "depth_k",
    "n_emitted_starts",
    "n_transition_evaluable_starts",
    "seed_depth_supported",
)
EXPECTED_ROW_COUNT = 144

REPORT_DIR = _ROOT / "data" / "reports"
CSV_PATH = REPORT_DIR / "pr010_reference_depth_coverage_development.csv"
SIDECAR_PATH = REPORT_DIR / "pr010_reference_depth_coverage_development.sha256"
CSV_TMP_PATH = REPORT_DIR / "pr010_reference_depth_coverage_development.csv.tmp"
SIDECAR_TMP_PATH = REPORT_DIR / "pr010_reference_depth_coverage_development.sha256.tmp"

MAX_WALL_SECONDS = 60 * 60
MAX_CPU_SECONDS = 4 * 60 * 60
MAX_RSS_BYTES = 1 << 30
MAX_PROCESSES = 1
MAX_THREADS = 4
RESOURCE_POLL_SECONDS = 0.05

PUBLISHED_TERMINAL = "PR010_DEVELOPMENT_COVERAGE_PUBLISHED"
RUNTIME_TERMINAL = "PR010_FAILED_RUNTIME"
DATA_CONTRACT_TERMINAL = "PR010_FAILED_DATA_CONTRACT"
BUDGET_TERMINAL = "PR010_FAILED_BUDGET"


class DataContractError(ValueError):
    """The frozen PR010 data or command contract was violated."""


class ContractError(ValueError):
    """The frozen enclosing-diamond contract was violated."""


class RuntimeFailure(RuntimeError):
    """A runtime or publication operation failed."""


class BudgetExceeded(RuntimeError):
    """A frozen resource limit was exceeded."""


@dataclass(frozen=True)
class WidthResult:
    n_survivors: int
    n_valid_pair_separations: int
    width_lower_median: float | None


def lower_median(values: Iterable[float]) -> float:
    ordered = sorted(float(value) for value in values)
    if not ordered:
        raise ContractError("lower median requires at least one value")
    if not all(math.isfinite(value) for value in ordered):
        raise ContractError("lower median values must be finite")
    return ordered[(len(ordered) - 1) // 2]


def validate_strict_causal_matrix(causal: np.ndarray) -> np.ndarray:
    matrix = np.asarray(causal, dtype=bool)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ContractError("causal relation must be a square matrix")
    if np.any(np.diag(matrix)):
        raise ContractError("causal relation must be strict")
    if np.any(matrix & matrix.T):
        raise ContractError("causal relation must be acyclic")
    return matrix


def _set_bit_indices(bits: int) -> Iterator[int]:
    """Yield set-bit indices without allocating an N-length boolean vector."""

    while bits:
        least = bits & -bits
        yield least.bit_length() - 1
        bits ^= least


class EnclosingDiamondWorkspace:
    """Prepared exact separation engine copied from normative commit 489f560."""

    def __init__(self, causal: np.ndarray):
        self.matrix = validate_strict_causal_matrix(causal)
        self.n = int(self.matrix.shape[0])
        packed_past = np.packbits(self.matrix, axis=1, bitorder="little")
        packed_future = np.packbits(self.matrix.T, axis=1, bitorder="little")
        self._past_bits = tuple(
            int.from_bytes(row.tobytes(), byteorder="little")
            for row in packed_past
        )
        self._future_bits = tuple(
            int.from_bytes(row.tobytes(), byteorder="little")
            for row in packed_future
        )
        cache_dtype = np.uint16 if self.n < 65_534 else np.uint32
        cache_limits = np.iinfo(cache_dtype)
        self._cache_unknown = int(cache_limits.max)
        self._cache_none = self._cache_unknown - 1
        self._separation_cache = np.full(
            self.n * (self.n - 1) // 2,
            self._cache_unknown,
            dtype=cache_dtype,
        )
        self._separation_cache_entries = 0
        self._width_cache: dict[tuple[tuple[int, int], ...], WidthResult] = {}

    def require_matrix(self, causal: np.ndarray) -> None:
        """Refuse accidental reuse with a different causal relation."""

        if np.asarray(causal, dtype=bool) is not self.matrix:
            raise ContractError("separation workspace belongs to another matrix")

    def cache_info(self) -> tuple[int, int]:
        """Return separation and width entry counts for deterministic tests."""

        return self._separation_cache_entries, len(self._width_cache)

    def _pair_index(self, u: int, v: int) -> int:
        if u > v:
            u, v = v, u
        return u * (2 * self.n - u - 1) // 2 + (v - u - 1)

    def _store_separation(self, index: int, cardinality: int | None) -> None:
        if int(self._separation_cache[index]) == self._cache_unknown:
            self._separation_cache_entries += 1
        self._separation_cache[index] = (
            self._cache_none if cardinality is None else cardinality
        )

    def minimum_enclosing_diamond_separation(
        self, u: int, v: int
    ) -> float | None:
        if not 0 <= u < self.n or not 0 <= v < self.n:
            raise ContractError("element identifier outside causal matrix")
        if u == v:
            return None

        cache_index = self._pair_index(u, v)
        cached = int(self._separation_cache[cache_index])
        if cached != self._cache_unknown:
            return None if cached == self._cache_none else math.sqrt(cached)
        if self.matrix[u, v] or self.matrix[v, u]:
            self._store_separation(cache_index, None)
            return None

        common_past = self._past_bits[u] & self._past_bits[v]
        common_future = self._future_bits[u] & self._future_bits[v]
        if common_past == 0 or common_future == 0:
            self._store_separation(cache_index, None)
            return None

        maximal_past = [
            e
            for e in _set_bit_indices(common_past)
            if (self._future_bits[e] & common_past) == 0
        ]
        minimal_future = [
            f
            for f in _set_bit_indices(common_future)
            if (self._past_bits[f] & common_future) == 0
        ]

        minimum_cardinality: int | None = None
        for e in maximal_past:
            strict_future = self._future_bits[e]
            for f in minimal_future:
                cardinality = (
                    strict_future & self._past_bits[f]
                ).bit_count() + 2
                if cardinality < 4:
                    raise ContractError(
                        "enclosing diamond omitted required elements"
                    )
                if (
                    minimum_cardinality is None
                    or cardinality < minimum_cardinality
                ):
                    minimum_cardinality = cardinality
                    if cardinality == 4:
                        self._store_separation(cache_index, cardinality)
                        return 2.0

        self._store_separation(cache_index, minimum_cardinality)
        if minimum_cardinality is None:
            return None
        return math.sqrt(minimum_cardinality)

    def survivor_rung_separation(
        self,
        left: tuple[int, int],
        right: tuple[int, int],
    ) -> float | None:
        d_p = self.minimum_enclosing_diamond_separation(left[0], right[0])
        d_q = self.minimum_enclosing_diamond_separation(left[1], right[1])
        if d_p is None or d_q is None or d_p <= 0.0 or d_q <= 0.0:
            return None
        return math.sqrt(d_p * d_q)

    def ensemble_width(
        self, survivor_rungs: Sequence[tuple[int, int]]
    ) -> WidthResult:
        n_survivors = len(survivor_rungs)
        if len(set(survivor_rungs)) != n_survivors:
            raise ContractError("survivor terminal rungs must be deduplicated")

        cache_key = tuple(sorted((int(p), int(q)) for p, q in survivor_rungs))
        cached = self._width_cache.get(cache_key)
        if cached is not None:
            return cached

        separations = []
        for left_index, right_index in combinations(range(n_survivors), 2):
            value = self.survivor_rung_separation(
                survivor_rungs[left_index], survivor_rungs[right_index]
            )
            if value is not None:
                separations.append(value)

        evaluable = (
            n_survivors >= MIN_SURVIVORS
            and len(separations) >= MIN_PAIR_SEPARATIONS
        )
        width = lower_median(separations) if evaluable else None
        result = WidthResult(n_survivors, len(separations), width)
        self._width_cache[cache_key] = result
        return result


MIN_SURVIVORS = 3
MIN_PAIR_SEPARATIONS = 3


def boundary_minimals_invariant(C, k_side=6):
    """Return the tie-complete invariant boundary-minimal selection."""

    O_by_min, min_idx = estimator.estimate_O_volume(C)
    mins = np.array(min_idx)
    O = np.array([O_by_min[i] for i in min_idx], float)
    thr, _ = estimator.two_means_split(list(O))
    low, low_O = mins[O < thr], O[O < thr]
    high, high_O = mins[O >= thr], O[O >= thr]
    if low.size == 0 or high.size == 0:
        return np.zeros(0, np.int64)
    lo_cut = np.sort(low_O)[-min(k_side, low_O.size)]
    hi_cut = np.sort(high_O)[min(k_side, high_O.size) - 1]
    lo_b = low[low_O >= lo_cut]
    hi_b = high[high_O <= hi_cut]
    sel = np.concatenate([lo_b, hi_b]).astype(np.int64)
    return np.sort(sel)


def make_exchangeable_tie_ranks(n_elements: int, seed: int) -> np.ndarray:
    if n_elements < 0:
        raise DataContractError("negative element count")
    sequence = np.random.SeedSequence([TIE_RANK_MASTER_SEED, int(seed)])
    ranks = np.random.Generator(np.random.PCG64(sequence)).permutation(n_elements)
    return np.asarray(ranks, dtype=np.int64)


def validate_tie_ranks(tie_rank: np.ndarray, n_elements: int) -> np.ndarray:
    ranks = np.asarray(tie_rank)
    if ranks.shape != (n_elements,) or not np.issubdtype(ranks.dtype, np.integer):
        raise DataContractError("tie ranks must be one integer per element")
    if not np.array_equal(np.sort(ranks), np.arange(n_elements)):
        raise DataContractError("tie ranks must be a permutation of 0..N-1")
    return ranks.astype(np.int64, copy=False)


def _children(element: int, indptr: np.ndarray, indices: np.ndarray) -> np.ndarray:
    return indices[indptr[element] : indptr[element + 1]]


def sample_starts_exchangeably(
    causal: np.ndarray,
    indptr: np.ndarray,
    indices: np.ndarray,
    tie_rank: np.ndarray,
    max_starts: int = MAX_STARTS,
    selector: Callable[[np.ndarray], Iterable[int]] = boundary_minimals_invariant,
) -> list[tuple[int, int]]:
    """Return invariant boundary starts ordered only by attached random ranks."""

    ranks = validate_tie_ranks(tie_rank, causal.shape[0])
    if max_starts <= 0:
        raise DataContractError("max_starts must be positive")
    starts = {
        (int(p), int(q))
        for p in selector(causal)
        for q in _children(int(p), indptr, indices)
    }
    ordered = sorted(starts, key=lambda rung: (ranks[rung[0]], ranks[rung[1]]))
    return ordered[:max_starts]


def _path_tie_key(
    p_path: Sequence[int], q_path: Sequence[int], tie_rank: np.ndarray
) -> tuple[tuple[int, int], ...]:
    return tuple(
        (int(tie_rank[p]), int(tie_rank[q]))
        for p, q in zip(p_path, q_path, strict=True)
    )


def kbeam_exchangeable(
    start_p: int,
    start_q: int,
    indptr: np.ndarray,
    indices: np.ndarray,
    causal: np.ndarray,
    tie_rank: np.ndarray,
    beam_size: int = K,
    max_depth: int = MAX_DEPTH,
) -> list[list[tuple[int, float, list[int], list[int]]]]:
    """Existing Definition-2 beam with exchangeable, path-complete tie keys."""

    ranks = validate_tie_ranks(tie_rank, causal.shape[0])
    if beam_size <= 0 or max_depth <= 0:
        raise DataContractError("beam size and depth must be positive")
    next_lineage_id = 1
    frontier = [(0, 0.0, (int(start_p),), (int(start_q),))]
    by_depth = [[(0, 0.0, [int(start_p)], [int(start_q)])]]
    depth = 1
    while depth < max_depth and frontier:
        candidates: dict[
            tuple[int, int],
            tuple[
                float,
                tuple[int, ...],
                tuple[int, ...],
                int,
                tuple[tuple[int, int], ...],
            ],
        ] = {}
        for lineage_id, regularity, p_path, q_path in frontier:
            p_last, q_last = p_path[-1], q_path[-1]
            for next_p_raw in _children(p_last, indptr, indices):
                next_p = int(next_p_raw)
                for next_q_raw in _children(q_last, indptr, indices):
                    next_q = int(next_q_raw)
                    if next_p == next_q or not XL._is_future_link(
                        next_p, next_q, indptr, indices
                    ):
                        continue
                    reward = 0.0
                    if depth >= M:
                        card_p = XL._interval_card(
                            p_path[depth - M], next_p, causal
                        )
                        if card_p < M - 1 or card_p > 2 * M - 1:
                            continue
                        card_q = XL._interval_card(
                            q_path[depth - M], next_q, causal
                        )
                        if card_q < M - 1 or card_q > 2 * M - 1:
                            continue
                        reward = -(
                            abs(card_p - BAND_CENTRE)
                            + abs(card_q - BAND_CENTRE)
                        )
                    new_regularity = float(regularity + reward)
                    new_p = p_path + (next_p,)
                    new_q = q_path + (next_q,)
                    tie_key = _path_tie_key(new_p, new_q, ranks)
                    terminal = (next_p, next_q)
                    previous = candidates.get(terminal)
                    if (
                        previous is None
                        or new_regularity > previous[0]
                        or (
                            new_regularity == previous[0]
                            and tie_key < previous[4]
                        )
                    ):
                        candidates[terminal] = (
                            new_regularity,
                            new_p,
                            new_q,
                            lineage_id,
                            tie_key,
                        )
        if not candidates:
            break
        ranked = sorted(candidates.values(), key=lambda item: (-item[0], item[4]))[
            :beam_size
        ]
        used_parents: set[int] = set()
        survivors = []
        for regularity, p_path, q_path, parent_lineage, _tie_key in ranked:
            if parent_lineage not in used_parents:
                lineage_id = parent_lineage
                used_parents.add(parent_lineage)
            else:
                lineage_id = next_lineage_id
                next_lineage_id += 1
            survivors.append((lineage_id, regularity, p_path, q_path))
        frontier = survivors
        by_depth.append(
            [
                (lineage, float(score), list(p_path), list(q_path))
                for lineage, score, p_path, q_path in survivors
            ]
        )
        depth += 1
    return by_depth


def _survivor_rungs(
    by_depth: Sequence[Sequence[tuple[int, float, Sequence[int], Sequence[int]]]],
    depth_k: int,
) -> list[tuple[int, int]]:
    if depth_k > len(by_depth):
        return []
    return [
        (int(p_path[-1]), int(q_path[-1]))
        for _lineage, _score, p_path, q_path in by_depth[depth_k - 1]
    ]


def _validate_frozen_configuration() -> None:
    expected = (
        DEVELOPMENT_SEEDS == tuple(range(1_101_000, 1_101_024))
        and N_DEVELOPMENT_SEEDS == 24
        and SPACETIME_KINDS == ("BH", "MINK")
        and INTENSITY == 4_800
        and T_EDGE == 6.0
        and M == 3
        and K == 64
        and MAX_STARTS == 40
        and TIE_RANK_MASTER_SEED == 9_009_009
        and REQUIRED_SLICES == (3, 4, 5, 6)
        and TRANSITION_DEPTHS == (3, 4, 5)
        and MAX_DEPTH == 6
    )
    if not expected:
        raise DataContractError("frozen configuration drift")


def _coverage_rows_for_seed(seed: int) -> list[dict[str, int | str]]:
    if seed not in DEVELOPMENT_SEEDS:
        raise DataContractError("seed outside frozen development band")
    # Keep NumPy-linked native pools at a single worker so the frozen budget
    # counter never sees extra native threads beyond the monitored process.
    with threadpool_limits(limits=1):
        embedding, edges, center = generator.numpy_sprinkle(seed, INTENSITY, T_EDGE)
        generator.assert_coordinate_uniform(embedding, edges, center)
        tie_rank = make_exchangeable_tie_ranks(len(embedding), seed)
        rows: list[dict[str, int | str]] = []
        for kind in SPACETIME_KINDS:
            causal = generator.past_matrix_fast(embedding, kind)
            _links, indptr, indices = XL.link_future_csr(causal)
            starts = sample_starts_exchangeably(
                causal, indptr, indices, tie_rank, MAX_STARTS
            )
            workspace = EnclosingDiamondWorkspace(causal)
            evaluable_counts = {depth: 0 for depth in TRANSITION_DEPTHS}
            for start_p, start_q in starts:
                by_depth = kbeam_exchangeable(
                    start_p,
                    start_q,
                    indptr,
                    indices,
                    causal,
                    tie_rank,
                    K,
                    MAX_DEPTH,
                )
                widths = {
                    depth: workspace.ensemble_width(_survivor_rungs(by_depth, depth))
                    for depth in REQUIRED_SLICES
                }
                for depth in TRANSITION_DEPTHS:
                    if (
                        widths[depth].width_lower_median is not None
                        and widths[depth + 1].width_lower_median is not None
                    ):
                        evaluable_counts[depth] += 1
            for depth in TRANSITION_DEPTHS:
                n_evaluable = evaluable_counts[depth]
                rows.append(
                    {
                        "seed": seed,
                        "spacetime_kind": kind,
                        "depth_k": depth,
                        "n_emitted_starts": len(starts),
                        "n_transition_evaluable_starts": n_evaluable,
                        "seed_depth_supported": int(n_evaluable >= 5),
                    }
                )
        return rows


def build_coverage_rows() -> list[dict[str, int | str]]:
    _validate_frozen_configuration()
    rows: list[dict[str, int | str]] = []
    for seed in DEVELOPMENT_SEEDS:
        rows.extend(_coverage_rows_for_seed(seed))
    return rows


def _parse_unsigned(value: str, field: str) -> int:
    if not value.isascii() or not value.isdecimal():
        raise DataContractError(f"{field} is not unsigned decimal")
    parsed = int(value)
    if str(parsed) != value:
        raise DataContractError(f"{field} is not canonical unsigned decimal")
    return parsed


def _expected_keys() -> list[tuple[int, str, int]]:
    return [
        (seed, kind, depth)
        for seed in DEVELOPMENT_SEEDS
        for kind in SPACETIME_KINDS
        for depth in TRANSITION_DEPTHS
    ]


def validate_csv_bytes(data: bytes) -> list[dict[str, int | str]]:
    if not data.endswith(b"\n") or b"\r" in data:
        raise DataContractError("CSV line endings are not canonical")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise DataContractError("CSV is not UTF-8") from exc
    lines = text.splitlines()
    header = ",".join(CSV_FIELDS)
    if not lines or lines[0] != header:
        raise DataContractError("CSV header drift")
    if len(lines) != EXPECTED_ROW_COUNT + 1:
        raise DataContractError("CSV row count drift")
    expected_keys = _expected_keys()
    rows: list[dict[str, int | str]] = []
    seen: set[tuple[int, str, int]] = set()
    for index, line in enumerate(lines[1:]):
        values = line.split(",")
        if len(values) != len(CSV_FIELDS) or any(value == "" for value in values):
            raise DataContractError("CSV row width drift")
        seed = _parse_unsigned(values[0], "seed")
        kind = values[1]
        depth = _parse_unsigned(values[2], "depth_k")
        emitted = _parse_unsigned(values[3], "n_emitted_starts")
        evaluable = _parse_unsigned(
            values[4], "n_transition_evaluable_starts"
        )
        supported = _parse_unsigned(values[5], "seed_depth_supported")
        key = (seed, kind, depth)
        if key in seen:
            raise DataContractError("duplicate primary key")
        seen.add(key)
        if key != expected_keys[index]:
            raise DataContractError("CSV key set or row order drift")
        if emitted > MAX_STARTS or evaluable > emitted:
            raise DataContractError("CSV count domain drift")
        if supported not in (0, 1) or supported != int(evaluable >= 5):
            raise DataContractError("support predicate drift")
        rows.append(
            {
                "seed": seed,
                "spacetime_kind": kind,
                "depth_k": depth,
                "n_emitted_starts": emitted,
                "n_transition_evaluable_starts": evaluable,
                "seed_depth_supported": supported,
            }
        )
    if seen != set(expected_keys):
        raise DataContractError("CSV key set drift")
    canonical = render_csv(rows)
    if canonical != data:
        raise DataContractError("CSV serialization is not canonical")
    return rows


def render_csv(rows: Sequence[Mapping[str, int | str]]) -> bytes:
    if len(rows) != EXPECTED_ROW_COUNT:
        raise DataContractError("in-memory row count drift")
    stream: list[str] = [",".join(CSV_FIELDS)]
    expected_keys = _expected_keys()
    for index, row in enumerate(rows):
        if tuple(row) != CSV_FIELDS or set(row) != set(CSV_FIELDS):
            raise DataContractError("in-memory schema drift")
        key = (int(row["seed"]), str(row["spacetime_kind"]), int(row["depth_k"]))
        if key != expected_keys[index]:
            raise DataContractError("in-memory key set or row order drift")
        values = [str(row[field]) for field in CSV_FIELDS]
        if any("," in value or "\n" in value or "\r" in value for value in values):
            raise DataContractError("noncanonical CSV scalar")
        stream.append(",".join(values))
    data = ("\n".join(stream) + "\n").encode("utf-8")
    return data


def _sidecar_bytes(csv_data: bytes) -> bytes:
    digest = hashlib.sha256(csv_data).hexdigest()
    return f"{digest}  {CSV_PATH.name}\n".encode("ascii")


def _all_artifact_paths() -> tuple[Path, ...]:
    return (CSV_PATH, SIDECAR_PATH, CSV_TMP_PATH, SIDECAR_TMP_PATH)


def refuse_existing_artifacts() -> None:
    if any(path.exists() for path in _all_artifact_paths()):
        raise DataContractError("development artifact or temporary already exists")


class AtomicPublisher:
    """Publish the fixed CSV/sidecar pair with fail-closed rollback."""

    def __init__(self) -> None:
        self.created_paths: set[Path] = set()

    def _checkpoint(self, _stage: str) -> None:
        return None

    def _exclusive_write(self, path: Path, data: bytes, label: str) -> None:
        # Register intent before the exclusive-create syscall so an asynchronous
        # interruption cannot strand a file between creation and bookkeeping.
        # A genuine pre-existing path is explicitly released from ownership.
        self.created_paths.add(path)
        try:
            handle = path.open("xb")
        except FileExistsError:
            self.created_paths.discard(path)
            raise
        with handle:
            self._checkpoint(f"{label}_created")
            handle.write(data)
            self._checkpoint(f"{label}_written")
            handle.flush()
            self._checkpoint(f"{label}_flushed")
            os.fsync(handle.fileno())
            self._checkpoint(f"{label}_fsynced")

    def _replace_owned(self, source: Path, target: Path) -> None:
        # The destination is absent by contract.  Track it before the syscall
        # while retaining the source, so either pre- or post-rename interruption
        # leaves every possible invocation-owned path eligible for rollback.
        self.created_paths.add(target)
        try:
            os.replace(source, target)
        except BaseException:
            if source.exists():
                self.created_paths.discard(target)
            raise
        self.created_paths.discard(source)

    def _rollback(self) -> None:
        failures = []
        for path in tuple(self.created_paths):
            try:
                path.unlink()
            except FileNotFoundError:
                self.created_paths.discard(path)
            except OSError as exc:
                failures.append(exc)
            else:
                self.created_paths.discard(path)
        if failures:
            raise RuntimeFailure("publication rollback failed")

    def publish(self, csv_data: bytes) -> None:
        refuse_existing_artifacts()
        try:
            self._exclusive_write(CSV_TMP_PATH, csv_data, "csv")
            persisted_csv = CSV_TMP_PATH.read_bytes()
            self._checkpoint("csv_reread")
            validate_csv_bytes(persisted_csv)
            self._checkpoint("csv_validated")
            sidecar_data = _sidecar_bytes(persisted_csv)
            self._exclusive_write(SIDECAR_TMP_PATH, sidecar_data, "sidecar")
            persisted_sidecar = SIDECAR_TMP_PATH.read_bytes()
            self._checkpoint("sidecar_reread")
            if persisted_sidecar != _sidecar_bytes(persisted_csv):
                raise DataContractError("temporary sidecar mismatch")
            self._checkpoint("sidecar_validated")
            self._replace_owned(CSV_TMP_PATH, CSV_PATH)
            self._checkpoint("csv_renamed")
            self._replace_owned(SIDECAR_TMP_PATH, SIDECAR_PATH)
            self._checkpoint("sidecar_renamed")
            directory_fd = os.open(REPORT_DIR, os.O_RDONLY)
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
            self._checkpoint("directory_fsynced")
        except BaseException as exc:
            try:
                self._rollback()
            except RuntimeFailure as cleanup_exc:
                raise cleanup_exc from exc
            raise


@dataclass(frozen=True)
class ResourceSnapshot:
    wall_seconds: float
    cpu_seconds: float
    peak_rss_bytes: int
    process_count: int
    thread_count: int


def _linux_resource_snapshot(started_at: float) -> ResourceSnapshot:
    try:
        usage = resource.getrusage(resource.RUSAGE_SELF)
        task_paths = tuple(Path("/proc/self/task").iterdir())
        children: set[int] = set()
        for task_path in task_paths:
            raw = (task_path / "children").read_text(encoding="ascii").strip()
            if raw:
                children.update(int(value) for value in raw.split())
    except (OSError, ValueError) as exc:
        raise RuntimeFailure("resource measurement unavailable") from exc
    return ResourceSnapshot(
        wall_seconds=time.monotonic() - started_at,
        cpu_seconds=float(usage.ru_utime + usage.ru_stime),
        peak_rss_bytes=int(usage.ru_maxrss) * 1024,
        process_count=1 + len(children),
        thread_count=len(task_paths),
    )


def enforce_resource_snapshot(snapshot: ResourceSnapshot) -> None:
    if snapshot.process_count > MAX_PROCESSES:
        raise BudgetExceeded("process budget exceeded")
    if snapshot.thread_count > MAX_THREADS:
        raise BudgetExceeded("thread budget exceeded")
    if snapshot.wall_seconds > MAX_WALL_SECONDS:
        raise BudgetExceeded("wall-time budget exceeded")
    if snapshot.cpu_seconds > MAX_CPU_SECONDS:
        raise BudgetExceeded("CPU budget exceeded")
    if snapshot.peak_rss_bytes > MAX_RSS_BYTES:
        raise BudgetExceeded("memory budget exceeded")


class BudgetGuard:
    """Continuously monitor all frozen resource dimensions."""

    def __init__(self) -> None:
        self.started_at = time.monotonic()
        self._stop = threading.Event()
        self._failure: BaseException | None = None
        self._thread: threading.Thread | None = None
        self._old_alarm_handler: object | None = None
        self._old_interrupt_handler: object | None = None

    def check(self) -> None:
        if self._failure is not None:
            raise self._failure
        enforce_resource_snapshot(_linux_resource_snapshot(self.started_at))

    def _interrupt(self, _signum: int, _frame: object) -> None:
        if self._failure is None:
            self._failure = BudgetExceeded("wall-time budget exceeded")
        if sys.exception() is not None:
            return
        raise self._failure

    def _monitor(self) -> None:
        while not self._stop.wait(RESOURCE_POLL_SECONDS):
            try:
                enforce_resource_snapshot(_linux_resource_snapshot(self.started_at))
            except BaseException as exc:
                self._failure = exc
                os.kill(os.getpid(), signal.SIGUSR1)
                return

    def __enter__(self) -> "BudgetGuard":
        if threading.current_thread() is not threading.main_thread():
            raise RuntimeFailure("budget guard requires the main thread")
        self._old_alarm_handler = signal.getsignal(signal.SIGALRM)
        self._old_interrupt_handler = signal.getsignal(signal.SIGUSR1)
        signal.signal(signal.SIGALRM, self._interrupt)
        signal.signal(signal.SIGUSR1, self._interrupt)
        try:
            signal.setitimer(signal.ITIMER_REAL, MAX_WALL_SECONDS)
            self._thread = threading.Thread(
                target=self._monitor, name="pr010-budget-monitor", daemon=True
            )
            self._thread.start()
            self.check()
        except BaseException:
            self._stop.set()
            signal.setitimer(signal.ITIMER_REAL, 0.0)
            if self._thread is not None:
                self._thread.join(timeout=1.0)
            signal.signal(signal.SIGALRM, self._old_alarm_handler)
            signal.signal(signal.SIGUSR1, self._old_interrupt_handler)
            raise
        return self

    def __exit__(self, exc_type: object, exc: object, tb: object) -> bool:
        self._stop.set()
        signal.setitimer(signal.ITIMER_REAL, 0.0)
        if self._thread is not None:
            self._thread.join(timeout=1.0)
            if self._thread.is_alive() and exc is None:
                self._failure = RuntimeFailure("budget monitor did not stop")
        if self._old_alarm_handler is not None:
            signal.signal(signal.SIGALRM, self._old_alarm_handler)
        if self._old_interrupt_handler is not None:
            signal.signal(signal.SIGUSR1, self._old_interrupt_handler)
        if exc is not None and self._failure is not None:
            selected = select_operational_terminal((exc, self._failure))
            failure_terminal = select_operational_terminal((self._failure,))
            if selected == failure_terminal:
                raise self._failure
        elif exc is None:
            self.check()
        return False


def select_operational_terminal(errors: Sequence[BaseException]) -> str:
    if any(not isinstance(error, (DataContractError, BudgetExceeded)) for error in errors):
        return RUNTIME_TERMINAL
    if any(isinstance(error, DataContractError) for error in errors):
        return DATA_CONTRACT_TERMINAL
    return BUDGET_TERMINAL


def run() -> None:
    _validate_frozen_configuration()
    refuse_existing_artifacts()
    publisher = AtomicPublisher()
    try:
        with BudgetGuard() as budget:
            rows = build_coverage_rows()
            budget.check()
            csv_data = render_csv(rows)
            validate_csv_bytes(csv_data)
            budget.check()
            publisher.publish(csv_data)
            budget.check()
    except BaseException as exc:
        cleanup_failures = []
        for path in tuple(publisher.created_paths):
            try:
                path.unlink()
            except FileNotFoundError:
                publisher.created_paths.discard(path)
            except OSError as cleanup_exc:
                cleanup_failures.append(cleanup_exc)
            else:
                publisher.created_paths.discard(path)
        if cleanup_failures:
            raise RuntimeFailure("run rollback failed") from exc
        raise


def main(argv: Sequence[str] | None = None) -> int:
    arguments = tuple(sys.argv[1:] if argv is None else argv)
    try:
        if arguments:
            raise DataContractError("arguments are forbidden")
        run()
    except BaseException as exc:
        terminal = select_operational_terminal((exc,))
        print(f"PR010_DEVELOPMENT_TERMINAL={terminal}", file=sys.stderr)
        return 1
    print(PUBLISHED_TERMINAL)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
