"""Pure order-only primitives for the PR009 effective-expansion kill test.

This module intentionally has no generator, embedding, filesystem, or reporting imports.
It is not the PR009 production runner.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
import math
from typing import Iterable, Mapping, Sequence

import numpy as np


MIN_SURVIVORS = 3
MIN_PAIR_SEPARATIONS = 3
MAX_EXACT_PERMUTATIONS = 100_000
MONTE_CARLO_PERMUTATIONS = 100_000
PERMUTATION_SEED = 9009


class ContractError(ValueError):
    """Raised when an input violates the frozen PR009 core contract."""


@dataclass(frozen=True)
class WidthResult:
    n_survivors: int
    n_valid_pair_separations: int
    width_lower_median: float | None


@dataclass(frozen=True)
class TransitionResult:
    theta_raw: float
    theta_residual: float
    survivor_growth_baseline: float


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


def minimum_enclosing_diamond_separation(
    causal: np.ndarray, u: int, v: int
) -> float | None:
    """Return sqrt(min |[e,f]|) for spacelike ``u,v``, or ``None``.

    ``causal[x, y]`` means ``y < x``. The minimization is over all common-past
    ``e`` and common-future ``f`` elements and therefore does not choose a
    representative through labels or embedding data.
    """

    matrix = validate_strict_causal_matrix(causal)
    n = matrix.shape[0]
    if not 0 <= u < n or not 0 <= v < n:
        raise ContractError("element identifier outside causal matrix")
    if u == v or matrix[u, v] or matrix[v, u]:
        return None

    common_past = np.flatnonzero(matrix[u] & matrix[v])
    common_future = np.flatnonzero(matrix[:, u] & matrix[:, v])
    if common_past.size == 0 or common_future.size == 0:
        return None

    minimum_cardinality: int | None = None
    for e in common_past:
        future_of_e = matrix[:, e].copy()
        future_of_e[e] = True
        for f in common_future:
            past_of_f = matrix[f].copy()
            past_of_f[f] = True
            cardinality = int(np.count_nonzero(future_of_e & past_of_f))
            if cardinality < 4:
                raise ContractError("enclosing diamond omitted required elements")
            if minimum_cardinality is None or cardinality < minimum_cardinality:
                minimum_cardinality = cardinality

    if minimum_cardinality is None:
        return None
    return math.sqrt(minimum_cardinality)


def survivor_rung_separation(
    causal: np.ndarray,
    left: tuple[int, int],
    right: tuple[int, int],
) -> float | None:
    d_p = minimum_enclosing_diamond_separation(causal, left[0], right[0])
    d_q = minimum_enclosing_diamond_separation(causal, left[1], right[1])
    if d_p is None or d_q is None or d_p <= 0.0 or d_q <= 0.0:
        return None
    return math.sqrt(d_p * d_q)


def ensemble_width(
    causal: np.ndarray,
    survivor_rungs: Sequence[tuple[int, int]],
) -> WidthResult:
    n_survivors = len(survivor_rungs)
    if len(set(survivor_rungs)) != n_survivors:
        raise ContractError("survivor terminal rungs must be deduplicated")

    separations = []
    for left_index, right_index in combinations(range(n_survivors), 2):
        value = survivor_rung_separation(
            causal, survivor_rungs[left_index], survivor_rungs[right_index]
        )
        if value is not None:
            separations.append(value)

    evaluable = (
        n_survivors >= MIN_SURVIVORS
        and len(separations) >= MIN_PAIR_SEPARATIONS
    )
    width = lower_median(separations) if evaluable else None
    return WidthResult(n_survivors, len(separations), width)


def transition_metrics(
    current: WidthResult,
    following: WidthResult,
    depth_mink_reference: float,
) -> TransitionResult | None:
    if current.width_lower_median is None or following.width_lower_median is None:
        return None
    if current.width_lower_median <= 0.0 or following.width_lower_median <= 0.0:
        raise ContractError("evaluable widths must be positive")
    if current.n_survivors <= 0 or following.n_survivors <= 0:
        raise ContractError("evaluable transitions require survivors")
    if not math.isfinite(depth_mink_reference):
        raise ContractError("depth reference must be finite")

    theta_raw = math.log(following.width_lower_median) - math.log(
        current.width_lower_median
    )
    return TransitionResult(
        theta_raw=theta_raw,
        theta_residual=theta_raw - depth_mink_reference,
        survivor_growth_baseline=(
            math.log(following.n_survivors) - math.log(current.n_survivors)
        ),
    )


def build_depth_mink_reference(
    rows: Iterable[Mapping[str, object]], minimum_per_depth: int = 12
) -> dict[int, float]:
    grouped: dict[int, list[float]] = {}
    for row in rows:
        if row.get("run_block") != "REFERENCE" or row.get("spacetime_kind") != "MINK":
            raise ContractError("depth reference accepts reference-MINK rows only")
        depth = int(row["depth_k"])
        value = float(row["theta_raw"])
        if not math.isfinite(value):
            raise ContractError("reference theta must be finite")
        grouped.setdefault(depth, []).append(value)

    if not grouped:
        raise ContractError("no reference-MINK rows")
    result = {}
    for depth, values in grouped.items():
        if len(values) < minimum_per_depth:
            raise ContractError(f"insufficient reference-MINK rows at depth {depth}")
        result[depth] = lower_median(values)
    return result


def contrast(values: Sequence[float], zones: Sequence[str]) -> float:
    if len(values) != len(zones) or not values:
        raise ContractError("contrast vectors must be non-empty and aligned")
    interior = [value for value, zone in zip(values, zones, strict=True) if zone == "INTERIOR"]
    exterior = [value for value, zone in zip(values, zones, strict=True) if zone == "EXTERIOR"]
    if not interior or not exterior:
        raise ContractError("contrast requires both scoring zones")
    return lower_median(exterior) - lower_median(interior)


def stratified_permutation_pvalue(
    values: Sequence[float],
    zones: Sequence[str],
    seeds: Sequence[int],
) -> float:
    """Frozen one-sided seed-stratified permutation p-value for positive contrast."""

    if not (len(values) == len(zones) == len(seeds)) or not values:
        raise ContractError("permutation vectors must be non-empty and aligned")
    if any(zone not in {"INTERIOR", "EXTERIOR"} for zone in zones):
        raise ContractError("guard or unknown zones cannot enter permutation logic")
    observed = contrast(values, zones)

    groups: list[tuple[list[int], int]] = []
    assignment_count = 1
    for seed in sorted(set(int(seed) for seed in seeds)):
        indices = [index for index, item in enumerate(seeds) if int(item) == seed]
        n_exterior = sum(zones[index] == "EXTERIOR" for index in indices)
        if n_exterior == 0 or n_exterior == len(indices):
            raise ContractError("every seed must contribute to both zones")
        groups.append((indices, n_exterior))
        assignment_count *= math.comb(len(indices), n_exterior)

    numeric_values = [float(value) for value in values]

    def assigned_contrast(exterior_by_group: Sequence[set[int]]) -> float:
        assigned_zones = ["INTERIOR"] * len(numeric_values)
        for exterior in exterior_by_group:
            for index in exterior:
                assigned_zones[index] = "EXTERIOR"
        return contrast(numeric_values, assigned_zones)

    exceedances = 0
    if assignment_count <= MAX_EXACT_PERMUTATIONS:
        choices = [
            [set(choice) for choice in combinations(indices, n_exterior)]
            for indices, n_exterior in groups
        ]
        total = assignment_count
        for assignment in product(*choices):
            if assigned_contrast(assignment) >= observed:
                exceedances += 1
    else:
        rng = np.random.Generator(np.random.PCG64(PERMUTATION_SEED))
        total = MONTE_CARLO_PERMUTATIONS
        for _ in range(total):
            assignment = [
                set(rng.choice(indices, size=n_exterior, replace=False).tolist())
                for indices, n_exterior in groups
            ]
            if assigned_contrast(assignment) >= observed:
                exceedances += 1

    return (1.0 + exceedances) / (1.0 + total)
