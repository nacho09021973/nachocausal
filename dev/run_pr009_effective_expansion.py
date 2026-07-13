"""Frozen production runner for the PR009 effective-expansion kill test.

This module owns generation, the exchangeably tie-broken order-only beam, width
rows, separately held evaluation truth, and atomic block publication.  It does
not score zones, compute contrasts or terminal labels, or render the report.

Do not run a production block before the implementation tests and review pass.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
import hashlib
import io
import math
import os
from pathlib import Path
import sys
from typing import Callable, Iterable, Mapping, Sequence

import numpy as np


_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent
sys.path.insert(0, str(_ROOT))
sys.path.insert(0, str(_HERE))

from nachocausal import generator, thresholds  # noqa: E402
import explore_ladders as XL  # noqa: E402
from dev.measure_pr003 import boundary_minimals_invariant  # noqa: E402
from dev.pr009_effective_expansion_core import (  # noqa: E402
    ContractError as CoreContractError,
    WidthResult,
    build_depth_mink_reference,
    ensemble_width,
    lower_median,
)


REFERENCE_SEEDS = tuple(range(1_100_000, 1_100_006))
EVALUATION_SEEDS = tuple(range(1_100_006, 1_100_012))
SPACETIME_KINDS = ("BH", "MINK")
INTENSITY = 4_800
T_EDGE = 6.0
M = 3
K = 64
MAX_DEPTH = 12
MAX_STARTS = 40
BAND_CENTRE = 1.5 * M - 1.0
TIE_RANK_MASTER_SEED = 9_009_009
MIN_REFERENCE_PER_DEPTH = 12

REPORT_DIR = _ROOT / "data" / "reports"
REFERENCE_ORDER_ONLY = REPORT_DIR / (
    "pr009_ladder_ensemble_effective_expansion_reference_order_only.csv"
)
REFERENCE_SHA256 = REPORT_DIR / (
    "pr009_ladder_ensemble_effective_expansion_reference_order_only.sha256"
)
EVALUATION_ORDER_ONLY = REPORT_DIR / (
    "pr009_ladder_ensemble_effective_expansion_evaluation_order_only.csv"
)
EVALUATION_TRUTH = REPORT_DIR / (
    "pr009_ladder_ensemble_effective_expansion_evaluation_truth.csv"
)
CANONICAL_ORDER_ONLY = REPORT_DIR / (
    "pr009_ladder_ensemble_effective_expansion_order_only.csv"
)

ORDER_FIELDS = (
    "run_block",
    "seed",
    "spacetime_kind",
    "intensity",
    "K",
    "start_id",
    "depth_k",
    "slice_status",
    "n_survivors",
    "n_valid_pair_separations",
    "width_lower_median",
    "theta_raw",
    "depth_mink_reference",
    "theta_residual",
    "survivor_growth_baseline",
)
TRUTH_FIELDS = (
    "run_block",
    "seed",
    "spacetime_kind",
    "intensity",
    "K",
    "start_id",
    "depth_k",
    "truth_r_mid",
    "truth_zone",
    "distance_to_horizon_over_ell",
)
PRIMARY_KEY = ORDER_FIELDS[:7]
SLICE_STATUSES = {
    "TRANSITION_EVALUABLE",
    "WIDTH_ONLY",
    "WIDTH_UNEVALUABLE",
    "EMPTY",
}


class DataContractError(ValueError):
    """A frozen PR009 input or artifact contract was violated."""


class PublicationError(RuntimeError):
    """A production artifact set could not be published safely."""


@dataclass(frozen=True)
class RawSlice:
    run_block: str
    seed: int
    spacetime_kind: str
    intensity: int
    K: int
    start_id: int
    depth_k: int
    slice_status: str
    n_survivors: int
    n_valid_pair_separations: int
    width_lower_median: float | None
    theta_raw: float | None
    survivor_growth_baseline: float | None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def build_order_only_slices(
    causal: np.ndarray,
    by_depth: Sequence[Sequence[tuple[int, float, Sequence[int], Sequence[int]]]],
    *,
    run_block: str,
    seed: int,
    spacetime_kind: str,
    start_id: int,
) -> list[RawSlice]:
    """Build raw rows without accepting an embedding or any truth value."""

    widths: list[WidthResult] = []
    for depth_k in range(1, MAX_DEPTH + 1):
        widths.append(ensemble_width(causal, _survivor_rungs(by_depth, depth_k)))

    rows = []
    for index, current in enumerate(widths):
        following = widths[index + 1] if index + 1 < len(widths) else None
        if current.n_survivors == 0:
            status = "EMPTY"
        elif current.width_lower_median is None:
            status = "WIDTH_UNEVALUABLE"
        elif following is None or following.width_lower_median is None:
            status = "WIDTH_ONLY"
        else:
            status = "TRANSITION_EVALUABLE"

        theta_raw = None
        survivor_growth = None
        if status == "TRANSITION_EVALUABLE":
            if current.width_lower_median is None or following is None:
                raise AssertionError("transition status without two widths")
            if following.width_lower_median is None:
                raise AssertionError("transition status without following width")
            theta_raw = math.log(following.width_lower_median) - math.log(
                current.width_lower_median
            )
            survivor_growth = math.log(following.n_survivors) - math.log(
                current.n_survivors
            )
        rows.append(
            RawSlice(
                run_block=run_block,
                seed=int(seed),
                spacetime_kind=spacetime_kind,
                intensity=INTENSITY,
                K=K,
                start_id=int(start_id),
                depth_k=index + 1,
                slice_status=status,
                n_survivors=current.n_survivors,
                n_valid_pair_separations=current.n_valid_pair_separations,
                width_lower_median=current.width_lower_median,
                theta_raw=theta_raw,
                survivor_growth_baseline=survivor_growth,
            )
        )
    return rows


def build_truth_slices(
    embedding: np.ndarray,
    by_depth: Sequence[Sequence[tuple[int, float, Sequence[int], Sequence[int]]]],
    *,
    seed: int,
    spacetime_kind: str,
    start_id: int,
) -> list[dict[str, object]]:
    """Geometry-aware collector kept outside the order-only row builder."""

    radius = np.asarray(embedding, dtype=float)[:, 1]
    ell = thresholds.ell(INTENSITY)
    rows = []
    for depth_k in range(1, MAX_DEPTH + 1):
        rungs = _survivor_rungs(by_depth, depth_k)
        if not rungs:
            r_mid = None
            zone = None
            distance = None
        else:
            midpoint_radii = [0.5 * (radius[p] + radius[q]) for p, q in rungs]
            r_mid = lower_median(midpoint_radii)
            distance = abs(r_mid - thresholds.R_S) / ell
            if r_mid <= thresholds.R_S - 2.0 * ell:
                zone = "INTERIOR"
            elif r_mid >= thresholds.R_S + 2.0 * ell:
                zone = "EXTERIOR"
            else:
                zone = "GUARD"
        rows.append(
            {
                "run_block": "EVALUATION",
                "seed": int(seed),
                "spacetime_kind": spacetime_kind,
                "intensity": INTENSITY,
                "K": K,
                "start_id": int(start_id),
                "depth_k": depth_k,
                "truth_r_mid": r_mid,
                "truth_zone": zone,
                "distance_to_horizon_over_ell": distance,
            }
        )
    return rows


def build_block(
    run_block: str,
    seeds: Sequence[int],
    *,
    include_truth: bool,
) -> tuple[list[RawSlice], list[dict[str, object]]]:
    if run_block not in {"REFERENCE", "EVALUATION"}:
        raise DataContractError("unknown run block")
    expected = REFERENCE_SEEDS if run_block == "REFERENCE" else EVALUATION_SEEDS
    if tuple(seeds) != expected:
        raise DataContractError("seed block differs from frozen PR009 block")
    if include_truth != (run_block == "EVALUATION"):
        raise DataContractError("truth is allowed for the evaluation block only")

    order_rows: list[RawSlice] = []
    truth_rows: list[dict[str, object]] = []
    for seed in seeds:
        embedding, edges, center = generator.numpy_sprinkle(seed, INTENSITY, T_EDGE)
        generator.assert_coordinate_uniform(embedding, edges, center)
        tie_rank = make_exchangeable_tie_ranks(len(embedding), seed)
        for kind in SPACETIME_KINDS:
            causal = generator.past_matrix_fast(embedding, kind)
            _links, indptr, indices = XL.link_future_csr(causal)
            starts = sample_starts_exchangeably(
                causal, indptr, indices, tie_rank, MAX_STARTS
            )
            for start_id, (start_p, start_q) in enumerate(starts):
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
                order_rows.extend(
                    build_order_only_slices(
                        causal,
                        by_depth,
                        run_block=run_block,
                        seed=seed,
                        spacetime_kind=kind,
                        start_id=start_id,
                    )
                )
                if include_truth:
                    truth_rows.extend(
                        build_truth_slices(
                            embedding,
                            by_depth,
                            seed=seed,
                            spacetime_kind=kind,
                            start_id=start_id,
                        )
                    )
    return order_rows, truth_rows


def derive_reference_depths(rows: Sequence[RawSlice]) -> dict[int, float]:
    inputs = [
        {
            "run_block": row.run_block,
            "spacetime_kind": row.spacetime_kind,
            "depth_k": row.depth_k,
            "theta_raw": row.theta_raw,
        }
        for row in rows
        if row.run_block == "REFERENCE"
        and row.spacetime_kind == "MINK"
        and row.slice_status == "TRANSITION_EVALUABLE"
    ]
    try:
        return build_depth_mink_reference(inputs, MIN_REFERENCE_PER_DEPTH)
    except CoreContractError as exc:
        raise DataContractError(str(exc)) from exc


def finalize_order_rows(
    rows: Sequence[RawSlice], depth_reference: Mapping[int, float]
) -> list[dict[str, object]]:
    finalized = []
    for row in rows:
        item = {
            field: getattr(row, field)
            for field in ORDER_FIELDS
            if hasattr(row, field)
        }
        if row.slice_status == "TRANSITION_EVALUABLE":
            if row.theta_raw is None or row.survivor_growth_baseline is None:
                raise DataContractError("transition row lacks raw statistics")
            if row.depth_k not in depth_reference:
                raise DataContractError(
                    f"missing Minkowski reference for depth {row.depth_k}"
                )
            reference = float(depth_reference[row.depth_k])
            item["depth_mink_reference"] = reference
            item["theta_residual"] = row.theta_raw - reference
        else:
            item["depth_mink_reference"] = None
            item["theta_residual"] = None
            item["theta_raw"] = None
            item["survivor_growth_baseline"] = None
            if row.slice_status in {"WIDTH_UNEVALUABLE", "EMPTY"}:
                item["width_lower_median"] = None
        finalized.append(item)
    return finalized


def _format_scalar(value: object) -> str:
    if value is None:
        return "NA"
    if isinstance(value, (bool, np.bool_)):
        raise DataContractError("booleans are not valid CSV scalars")
    if isinstance(value, (int, np.integer)):
        if int(value) < 0:
            raise DataContractError("negative integer in unsigned field")
        return str(int(value))
    if isinstance(value, (float, np.floating)):
        numeric = float(value)
        if not math.isfinite(numeric):
            raise DataContractError("nonfinite float")
        if numeric == 0.0:
            numeric = 0.0
        return format(numeric, ".17g")
    return str(value)


def _row_sort_key(row: Mapping[str, object]) -> tuple[object, ...]:
    return (
        0 if row["run_block"] == "REFERENCE" else 1,
        int(row["seed"]),
        0 if row["spacetime_kind"] == "BH" else 1,
        int(row["intensity"]),
        int(row["K"]),
        int(row["start_id"]),
        int(row["depth_k"]),
    )


def render_csv(
    rows: Sequence[Mapping[str, object]], fields: Sequence[str]
) -> bytes:
    ordered = sorted(rows, key=_row_sort_key)
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(fields)
    for row in ordered:
        if set(row) != set(fields):
            raise DataContractError("row fields differ from frozen schema")
        writer.writerow([_format_scalar(row[field]) for field in fields])
    data = stream.getvalue().encode("utf-8")
    if not data.endswith(b"\n") or b"\r" in data:
        raise AssertionError("noncanonical line endings")
    return data


def _parse_unsigned(value: str, field: str) -> int:
    if not value.isascii() or not value.isdecimal():
        raise DataContractError(f"{field} is not canonical unsigned decimal")
    return int(value)


def _parse_float(value: str, field: str) -> float | None:
    if value == "NA":
        return None
    try:
        numeric = float(value)
    except ValueError as exc:
        raise DataContractError(f"{field} is not a float") from exc
    if not math.isfinite(numeric) or _format_scalar(numeric) != value:
        raise DataContractError(f"{field} is not a canonical finite float")
    return numeric


def validate_order_csv_bytes(
    data: bytes, allowed_blocks: set[str]
) -> list[dict[str, str]]:
    if not data.endswith(b"\n") or b"\r" in data:
        raise DataContractError("order CSV line endings are not canonical")
    try:
        text = data.decode("utf-8")
        parsed = list(csv.reader(io.StringIO(text, newline=""), strict=True))
    except (UnicodeDecodeError, csv.Error) as exc:
        raise DataContractError("malformed order CSV") from exc
    if not parsed or tuple(parsed[0]) != ORDER_FIELDS:
        raise DataContractError("order CSV header drift")
    rows: list[dict[str, str]] = []
    keys: set[tuple[str, ...]] = set()
    for values in parsed[1:]:
        if len(values) != len(ORDER_FIELDS):
            raise DataContractError("order CSV row width drift")
        row = dict(zip(ORDER_FIELDS, values, strict=True))
        if row["run_block"] not in allowed_blocks:
            raise DataContractError("unexpected run block")
        if row["spacetime_kind"] not in SPACETIME_KINDS:
            raise DataContractError("unexpected spacetime kind")
        parsed_unsigned = {}
        for field in (
            "seed",
            "intensity",
            "K",
            "start_id",
            "depth_k",
            "n_survivors",
            "n_valid_pair_separations",
        ):
            parsed_unsigned[field] = _parse_unsigned(row[field], field)
        if _parse_unsigned(row["intensity"], "intensity") != INTENSITY:
            raise DataContractError("intensity drift")
        if _parse_unsigned(row["K"], "K") != K:
            raise DataContractError("K drift")
        if parsed_unsigned["start_id"] >= MAX_STARTS:
            raise DataContractError("start_id outside frozen range")
        depth = _parse_unsigned(row["depth_k"], "depth_k")
        if depth not in range(1, MAX_DEPTH + 1):
            raise DataContractError("depth drift")
        if row["slice_status"] not in SLICE_STATUSES:
            raise DataContractError("unknown slice status")
        numeric = {
            field: _parse_float(row[field], field)
            for field in ORDER_FIELDS[10:]
        }
        status = row["slice_status"]
        if (status == "EMPTY") != (parsed_unsigned["n_survivors"] == 0):
            raise DataContractError("EMPTY status and survivor count disagree")
        if status == "TRANSITION_EVALUABLE":
            if any(value is None for value in numeric.values()):
                raise DataContractError("transition row has missing statistic")
        elif status == "WIDTH_ONLY":
            if numeric["width_lower_median"] is None or any(
                numeric[field] is not None for field in ORDER_FIELDS[11:]
            ):
                raise DataContractError("invalid WIDTH_ONLY fields")
        else:
            if any(value is not None for value in numeric.values()):
                raise DataContractError("unevaluable row has a numeric statistic")
        key = tuple(row[field] for field in PRIMARY_KEY)
        if key in keys:
            raise DataContractError("duplicate primary key")
        keys.add(key)
        rows.append(row)
    if rows != sorted(rows, key=_row_sort_key):
        raise DataContractError("order CSV row ordering drift")
    _validate_start_id_sequences(rows)
    return rows


def validate_truth_csv_bytes(data: bytes) -> list[dict[str, str]]:
    if not data.endswith(b"\n") or b"\r" in data:
        raise DataContractError("truth CSV line endings are not canonical")
    try:
        parsed = list(
            csv.reader(io.StringIO(data.decode("utf-8"), newline=""), strict=True)
        )
    except (UnicodeDecodeError, csv.Error) as exc:
        raise DataContractError("malformed truth CSV") from exc
    if not parsed or tuple(parsed[0]) != TRUTH_FIELDS:
        raise DataContractError("truth CSV header drift")
    rows: list[dict[str, str]] = []
    keys: set[tuple[str, ...]] = set()
    for values in parsed[1:]:
        if len(values) != len(TRUTH_FIELDS):
            raise DataContractError("truth CSV row width drift")
        row = dict(zip(TRUTH_FIELDS, values, strict=True))
        if row["run_block"] != "EVALUATION":
            raise DataContractError("truth contains a non-evaluation row")
        if row["spacetime_kind"] not in SPACETIME_KINDS:
            raise DataContractError("truth spacetime drift")
        parsed_unsigned = {
            field: _parse_unsigned(row[field], field)
            for field in ("seed", "intensity", "K", "start_id", "depth_k")
        }
        if parsed_unsigned["start_id"] >= MAX_STARTS:
            raise DataContractError("truth start_id outside frozen range")
        r_mid = _parse_float(row["truth_r_mid"], "truth_r_mid")
        distance = _parse_float(
            row["distance_to_horizon_over_ell"],
            "distance_to_horizon_over_ell",
        )
        if row["truth_zone"] == "NA":
            if r_mid is not None or distance is not None:
                raise DataContractError("missing truth zone has numeric truth")
        elif row["truth_zone"] not in {"INTERIOR", "EXTERIOR", "GUARD"}:
            raise DataContractError("unknown truth zone")
        elif r_mid is None or distance is None:
            raise DataContractError("defined truth zone lacks numeric truth")
        key = tuple(row[field] for field in PRIMARY_KEY)
        if key in keys:
            raise DataContractError("duplicate truth primary key")
        keys.add(key)
        rows.append(row)
    if rows != sorted(rows, key=_row_sort_key):
        raise DataContractError("truth CSV row ordering drift")
    _validate_start_id_sequences(rows)
    return rows


def _validate_start_id_sequences(rows: Sequence[Mapping[str, str]]) -> None:
    grouped: dict[tuple[str, str, str], set[int]] = {}
    for row in rows:
        group = (row["run_block"], row["seed"], row["spacetime_kind"])
        grouped.setdefault(group, set()).add(int(row["start_id"]))
    for start_ids in grouped.values():
        if sorted(start_ids) != list(range(len(start_ids))):
            raise DataContractError("start_id sequence is not contiguous from zero")


def validate_truth_alignment(
    order_rows: Sequence[Mapping[str, str]],
    truth_rows: Sequence[Mapping[str, str]],
) -> None:
    order_by_key = {
        tuple(row[field] for field in PRIMARY_KEY): row for row in order_rows
    }
    truth_by_key = {
        tuple(row[field] for field in PRIMARY_KEY): row for row in truth_rows
    }
    if set(order_by_key) != set(truth_by_key):
        raise DataContractError("evaluation and truth keys differ")
    for key, order_row in order_by_key.items():
        truth_row = truth_by_key[key]
        empty = order_row["slice_status"] == "EMPTY"
        truth_missing = truth_row["truth_zone"] == "NA"
        if empty != truth_missing:
            raise DataContractError("truth missingness disagrees with EMPTY status")


def reference_depths_from_csv(data: bytes) -> dict[int, float]:
    rows = validate_order_csv_bytes(data, {"REFERENCE"})
    inputs = [
        {
            "run_block": row["run_block"],
            "spacetime_kind": row["spacetime_kind"],
            "depth_k": row["depth_k"],
            "theta_raw": row["theta_raw"],
        }
        for row in rows
        if row["spacetime_kind"] == "MINK"
        and row["slice_status"] == "TRANSITION_EVALUABLE"
    ]
    try:
        derived = build_depth_mink_reference(inputs, MIN_REFERENCE_PER_DEPTH)
    except CoreContractError as exc:
        raise DataContractError(str(exc)) from exc
    for row in rows:
        if row["slice_status"] != "TRANSITION_EVALUABLE":
            continue
        depth = int(row["depth_k"])
        if depth not in derived:
            raise DataContractError("reference transition lacks derived depth")
        serialized = _parse_float(
            row["depth_mink_reference"], "depth_mink_reference"
        )
        theta_raw = _parse_float(row["theta_raw"], "theta_raw")
        residual = _parse_float(row["theta_residual"], "theta_residual")
        if serialized != derived[depth]:
            raise DataContractError("serialized reference baseline is not derived")
        if theta_raw is None or residual != theta_raw - derived[depth]:
            raise DataContractError("reference residual arithmetic drift")
    return derived


def combine_order_csv(reference: bytes, evaluation: bytes) -> bytes:
    validate_order_csv_bytes(reference, {"REFERENCE"})
    validate_order_csv_bytes(evaluation, {"EVALUATION"})
    header_end = evaluation.index(b"\n") + 1
    combined = reference + evaluation[header_end:]
    validate_order_csv_bytes(combined, {"REFERENCE", "EVALUATION"})
    return combined


def _fsync_file(path: Path, data: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def publish_set(items: Sequence[tuple[Path, bytes]]) -> None:
    finals = [path for path, _data in items]
    temporaries = [path.with_name(path.name + ".tmp") for path in finals]
    if any(path.exists() for path in (*finals, *temporaries)):
        raise PublicationError("production output or temporary already exists")
    for path in finals:
        path.parent.mkdir(parents=True, exist_ok=True)
    try:
        for temporary, (_final, data) in zip(temporaries, items, strict=True):
            _fsync_file(temporary, data)
        for temporary, final in zip(temporaries, finals, strict=True):
            os.replace(temporary, final)
    except BaseException:
        for path in (*temporaries, *finals):
            try:
                path.unlink()
            except FileNotFoundError:
                pass
        raise


def load_finalized_reference() -> tuple[bytes, dict[int, float]]:
    try:
        data = REFERENCE_ORDER_ONLY.read_bytes()
        sidecar = REFERENCE_SHA256.read_bytes()
    except OSError as exc:
        raise PublicationError("finalized reference artifact set is unreadable") from exc
    expected_sidecar = (
        f"{sha256_bytes(data)}  {REFERENCE_ORDER_ONLY.name}\n".encode("ascii")
    )
    if sidecar != expected_sidecar:
        raise DataContractError("reference sidecar mismatch")
    return data, reference_depths_from_csv(data)


def run_reference() -> None:
    raw_rows, truth_rows = build_block(
        "REFERENCE", REFERENCE_SEEDS, include_truth=False
    )
    if truth_rows:
        raise AssertionError("reference block emitted truth")
    depth_reference = derive_reference_depths(raw_rows)
    order_data = render_csv(
        finalize_order_rows(raw_rows, depth_reference), ORDER_FIELDS
    )
    validate_order_csv_bytes(order_data, {"REFERENCE"})
    sidecar = (
        f"{sha256_bytes(order_data)}  {REFERENCE_ORDER_ONLY.name}\n".encode("ascii")
    )
    publish_set(
        ((REFERENCE_ORDER_ONLY, order_data), (REFERENCE_SHA256, sidecar))
    )


def run_evaluation() -> None:
    reference_data, depth_reference = load_finalized_reference()
    reference_hash_before = sha256_bytes(reference_data)
    raw_rows, truth_rows = build_block(
        "EVALUATION", EVALUATION_SEEDS, include_truth=True
    )
    evaluation_data = render_csv(
        finalize_order_rows(raw_rows, depth_reference), ORDER_FIELDS
    )
    truth_data = render_csv(truth_rows, TRUTH_FIELDS)
    validate_order_csv_bytes(evaluation_data, {"EVALUATION"})
    validate_truth_csv_bytes(truth_data)
    evaluation_keys = {
        tuple(row[field] for field in PRIMARY_KEY)
        for row in validate_order_csv_bytes(evaluation_data, {"EVALUATION"})
    }
    truth_keys = {
        tuple(row[field] for field in PRIMARY_KEY)
        for row in validate_truth_csv_bytes(truth_data)
    }
    if evaluation_keys != truth_keys:
        raise DataContractError("evaluation and truth keys differ")
    validate_truth_alignment(
        validate_order_csv_bytes(evaluation_data, {"EVALUATION"}),
        validate_truth_csv_bytes(truth_data),
    )
    canonical_data = combine_order_csv(reference_data, evaluation_data)
    reference_after, _mapping_after = load_finalized_reference()
    if sha256_bytes(reference_after) != reference_hash_before:
        raise DataContractError("reference artifact changed during evaluation")
    publish_set(
        (
            (EVALUATION_ORDER_ONLY, evaluation_data),
            (EVALUATION_TRUTH, truth_data),
            (CANONICAL_ORDER_ONLY, canonical_data),
        )
    )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Frozen PR009 reference/evaluation runner"
    )
    parser.add_argument("--block", required=True, choices=("REFERENCE", "EVALUATION"))
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.block == "REFERENCE":
        run_reference()
    else:
        run_evaluation()
    print(f"PR009_{args.block}_PUBLISHED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
