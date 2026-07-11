from __future__ import annotations

import math

import numpy as np
import pytest

from dev import pr009_effective_expansion_core as core


def causal_matrix(n: int, covers: list[tuple[int, int]]) -> np.ndarray:
    """Build strict transitive closure; cover pair is (past, future)."""
    matrix = np.zeros((n, n), dtype=bool)
    for past, future in covers:
        matrix[future, past] = True
    for middle in range(n):
        for future in range(n):
            if matrix[future, middle]:
                matrix[future] |= matrix[middle]
    return matrix


def three_rung_diamond() -> tuple[np.ndarray, list[tuple[int, int]]]:
    # e=0, p rail=1..3, q rail=4..6, f=7. Every rail endpoint is
    # spacelike to the other endpoints on that rail and shares [e,f].
    covers = [(0, node) for node in range(1, 7)]
    covers += [(node, 7) for node in range(1, 7)]
    return causal_matrix(8, covers), [(1, 4), (2, 5), (3, 6)]


def relabel(matrix: np.ndarray, permutation: np.ndarray) -> np.ndarray:
    return matrix[np.ix_(permutation, permutation)]


def inverse_permutation(permutation: np.ndarray) -> np.ndarray:
    inverse = np.empty_like(permutation)
    inverse[permutation] = np.arange(len(permutation))
    return inverse


def test_lower_median_is_frozen_lower_choice():
    assert core.lower_median([9, 1, 5, 3]) == 3
    assert core.lower_median([9, 1, 5]) == 5
    with pytest.raises(core.ContractError):
        core.lower_median([])


def test_minimum_enclosing_diamond_separation():
    matrix, _ = three_rung_diamond()
    assert core.minimum_enclosing_diamond_separation(matrix, 1, 2) == pytest.approx(
        math.sqrt(8)
    )
    assert core.minimum_enclosing_diamond_separation(matrix, 0, 1) is None
    assert core.minimum_enclosing_diamond_separation(matrix, 1, 1) is None


def test_minimum_selects_smallest_enclosing_diamond():
    # 0 encloses all nodes through 7, while 8 and 9 form a smaller diamond
    # around nodes 1 and 2. The direct minimum must choose cardinality four.
    matrix = causal_matrix(
        10,
        [(0, 8), (8, 1), (8, 2), (1, 9), (2, 9), (9, 7)],
    )
    assert core.minimum_enclosing_diamond_separation(matrix, 1, 2) == 2.0


def test_separation_and_width_are_relabeling_invariant():
    matrix, rungs = three_rung_diamond()
    expected = core.ensemble_width(matrix, rungs)
    permutation = np.array([6, 2, 7, 1, 5, 0, 4, 3])
    inverse = inverse_permutation(permutation)
    permuted_rungs = [(int(inverse[p]), int(inverse[q])) for p, q in rungs]
    actual = core.ensemble_width(relabel(matrix, permutation), permuted_rungs)
    assert actual == expected


def test_width_requires_three_survivors_and_three_pairs():
    matrix, rungs = three_rung_diamond()
    assert core.ensemble_width(matrix, rungs).width_lower_median == pytest.approx(
        math.sqrt(8)
    )
    result = core.ensemble_width(matrix, rungs[:2])
    assert result.n_valid_pair_separations == 1
    assert result.width_lower_median is None


def test_width_rejects_duplicate_terminal_rungs():
    matrix, rungs = three_rung_diamond()
    with pytest.raises(core.ContractError):
        core.ensemble_width(matrix, [rungs[0], rungs[0], rungs[1]])


def test_transition_separates_width_from_survivor_growth():
    current = core.WidthResult(8, 12, 2.0)
    following = core.WidthResult(8, 10, 4.0)
    result = core.transition_metrics(current, following, 0.1)
    assert result is not None
    assert result.theta_raw == pytest.approx(math.log(2))
    assert result.theta_residual == pytest.approx(math.log(2) - 0.1)
    assert result.survivor_growth_baseline == 0.0


def test_transition_returns_none_for_unevaluable_width():
    assert core.transition_metrics(
        core.WidthResult(2, 1, None), core.WidthResult(3, 3, 2.0), 0.0
    ) is None


def test_depth_reference_accepts_reference_mink_only():
    rows = [
        {
            "run_block": "REFERENCE",
            "spacetime_kind": "MINK",
            "depth_k": 2,
            "theta_raw": value,
        }
        for value in (0.4, -0.1, 0.2, 0.0)
    ]
    assert core.build_depth_mink_reference(rows, minimum_per_depth=4) == {2: 0.0}
    rows[0] = {**rows[0], "spacetime_kind": "BH"}
    with pytest.raises(core.ContractError):
        core.build_depth_mink_reference(rows, minimum_per_depth=4)


def test_contrast_uses_lower_medians():
    values = [-2.0, -1.0, 1.0, 3.0]
    zones = ["INTERIOR", "INTERIOR", "EXTERIOR", "EXTERIOR"]
    assert core.contrast(values, zones) == 3.0


def test_stratified_permutation_is_exact_and_deterministic():
    values = [-2.0, 2.0, -1.0, 1.0]
    zones = ["INTERIOR", "EXTERIOR", "INTERIOR", "EXTERIOR"]
    seeds = [10, 10, 11, 11]
    first = core.stratified_permutation_pvalue(values, zones, seeds)
    second = core.stratified_permutation_pvalue(values, zones, seeds)
    # Four exact assignments; only the observed assignment reaches its contrast.
    assert first == pytest.approx(2 / 5)
    assert second == first


def test_permutation_rejects_guard_and_single_zone_seed():
    with pytest.raises(core.ContractError):
        core.stratified_permutation_pvalue(
            [-1.0, 0.0, 1.0], ["INTERIOR", "GUARD", "EXTERIOR"], [1, 1, 1]
        )
    with pytest.raises(core.ContractError):
        core.stratified_permutation_pvalue(
            [-1.0, 1.0], ["INTERIOR", "EXTERIOR"], [1, 2]
        )
