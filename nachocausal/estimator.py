"""ESTIMATOR — order-only. Sees ONLY the boolean past matrix C and |C|.

FROZEN. Lifted verbatim (behaviour-preserving) from the dev prototype
(dev/prototype_o.py: estimate_O, _topological_future_first, verify_order_only;
dev/sweep_o.py: two_means_split). The bit-exact regression test
(tests/test_regression.py) proves this module reproduces the 64 audited O
multisets in nachocausal/fixtures/o_samples.json.

This module imports NOTHING from nachocausal.scoring and never touches
coordinates. tests/test_leak.py enforces that the scoring subpackage is not
imported as a side effect of importing the estimator.
"""

from __future__ import annotations

from typing import Dict, List, Tuple

import numpy as np

from . import thresholds


# =============================================================================
# Glue 2 — the order-only observable O.
# =============================================================================
def estimate_O(
    past_matrix: np.ndarray,
) -> Tuple[Dict[int, int], List[int], np.ndarray]:
    """INPUT: the boolean past matrix C ONLY (C[i,j] True iff j precedes i).

    From this alone:
      * minimal elements (PastInf) = rows with no past (all-False row);
      * O(i) for minimal i = length (in #elements) of the maximal timelike
        chain starting at i, as a SINGLE-SOURCE LONGEST PATH on the DAG via DP
        in topological order (element forward-height).

    Returns (O_by_minimal_index, minimal_indices, longest_future_chain_all).
    """
    if past_matrix.dtype != bool:
        past_matrix = past_matrix.astype(bool)
    N = past_matrix.shape[0]
    assert past_matrix.shape == (N, N), "estimator expects a square poset matrix"
    # Guard (v): the only input is an N x N boolean order matrix. There is no
    # coordinate array in scope here at all.

    Lfut = np.zeros(N, dtype=int)
    order = _topological_future_first(past_matrix)  # process sinks first
    for e in order:
        future = np.nonzero(past_matrix[:, e])[0]
        Lfut[e] = 1 + (int(Lfut[future].max()) if future.size else 0)

    has_past = past_matrix.any(axis=1)
    minimal_indices = [i for i in range(N) if not has_past[i]]
    O_by_minimal = {i: int(Lfut[i]) for i in minimal_indices}
    return O_by_minimal, minimal_indices, Lfut


def _topological_future_first(past_matrix: np.ndarray) -> List[int]:
    """Order indices so every element appears before its past (Kahn on the
    future->past DAG): sinks (no future) first. Pure order, no coordinates."""
    N = past_matrix.shape[0]
    future_count = past_matrix.sum(axis=0).astype(int)
    ready = [e for e in range(N) if future_count[e] == 0]
    order: List[int] = []
    fc = future_count.copy()
    while ready:
        e = ready.pop()
        order.append(e)
        for p in np.nonzero(past_matrix[e, :])[0]:
            fc[p] -= 1
            if fc[p] == 0:
                ready.append(int(p))
    assert len(order) == N, "cycle detected -- not a DAG"
    return order


# =============================================================================
# BOUNDARY — order-only 1-D 2-means split on the integer multiset O.
# =============================================================================
def two_means_split(O) -> Tuple[float, float]:
    """1-D 2-means on sorted O: pick the gap minimising within-cluster SSE.
    Coordinate-free. Returns (threshold, sep) where:
      threshold = midpoint of the chosen gap (the frozen boundary definition);
      sep       = |mu_hi - mu_lo| / pooled_sd, with pooled_sd FLOORED at
                  thresholds.POOLED_SD_FLOOR (one O-discreteness unit) so a
                  degenerate tied control cannot inflate sep (cmte m2).

    On integer O the threshold is a half-integer midpoint, so exact ties
    (O == threshold) are impossible — classification O < threshold is
    unambiguous and needs no tie rule (cmte M1).
    """
    o = np.sort(np.asarray(O, float))
    n = o.size
    if n < 2:
        return float("nan"), float("nan")
    best_i, best_sse = 1, np.inf
    for i in range(1, n):
        lo, hi = o[:i], o[i:]
        sse = lo.var() * lo.size + hi.var() * hi.size
        if sse < best_sse:
            best_sse, best_i = sse, i
    lo, hi = o[:best_i], o[best_i:]
    thr = 0.5 * (lo[-1] + hi[0])
    pooled = np.sqrt((lo.var() * lo.size + hi.var() * hi.size) / n)
    pooled = max(pooled, thresholds.POOLED_SD_FLOOR)
    sep = abs(hi.mean() - lo.mean()) / pooled
    return float(thr), float(sep)


# =============================================================================
# GUARD (v) — runnable proof O depends ONLY on the abstract poset.
# =============================================================================
def verify_order_only(past_matrix: np.ndarray, seed: int = 0) -> Dict[int, int]:
    """Relabel elements by a random permutation (conjugate the order matrix) and
    recompute O. A permutation preserves the order but destroys any
    index/coordinate correlation. RAISES if the O multiset, or the per-element
    O value tracked through the permutation, changes. Returns O for the caller."""
    O0, min0, _ = estimate_O(past_matrix)
    rng = np.random.default_rng(seed)
    N = past_matrix.shape[0]
    perm = rng.permutation(N)
    permuted = past_matrix[perm][:, perm]
    O1, min1, _ = estimate_O(permuted)

    if len(min1) != len(min0) or sorted(O1.values()) != sorted(O0.values()):
        raise ValueError(
            "Guard (v) VIOLATED: O changed under a pure relabelling "
            f"(|minimal| {len(min0)}->{len(min1)}); O is NOT order-only."
        )
    inv = np.empty(N, dtype=int)
    inv[perm] = np.arange(N)  # old index -> new index
    for old_i, o_val in O0.items():
        new_i = int(inv[old_i])
        if O1.get(new_i) != o_val:
            raise ValueError(
                f"Guard (v) VIOLATED: element O not invariant under relabel "
                f"(old {old_i} O={o_val} -> new {new_i} O={O1.get(new_i)})."
            )
    return {int(k): int(v) for k, v in O0.items()}
