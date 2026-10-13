"""ESTIMATOR — order-only, 2+1 bench (CANDIDATE, not frozen).

A thin wrapper around the SEALED estimator-v2 primitives of the 1+1 package, imported UNCHANGED
(comité 052, reproducibility brief): estimate_O_volume (O(i) = |future(i)| over the minimal
elements), two_means_split, improvement, verify_order_only (Guard-v). The 2+1 generator returns
order[i, j] = "i precedes j"; the sealed primitives take the past matrix C[i, j] = "j precedes i",
so C = order.T. Same observable and split as dev/explore_2p1_estimator.py.

Input: the boolean order matrix ONLY. This module imports nothing from nachocausal2p1.scoring
and never sees coordinates (tests/test_2p1_package.py enforces both).
"""

from __future__ import annotations

from typing import Dict, List

import numpy as np

from nachocausal import estimator as sealed

from . import gate


def past_matrix(order: np.ndarray) -> np.ndarray:
    """C[i, j] = j precedes i, from order[i, j] = i precedes j."""
    return np.ascontiguousarray(np.asarray(order, dtype=bool).T)


def estimate(order: np.ndarray, guard: bool = True, guard_seed: int = 0) -> Dict[str, object]:
    """Order-only estimate. Guard-v (sealed verify_order_only on the production observable)
    RAISES if O is not invariant under a pure relabelling. Returns the minimal elements, O,
    the frozen blind threshold, sep, improvement, n and the gate decision."""
    C = past_matrix(order)
    if guard:
        sealed.verify_order_only(C, seed=guard_seed)
    O_by_min, min_idx = sealed.estimate_O_volume(C)
    vals: List[int] = [O_by_min[i] for i in min_idx]
    n = len(min_idx)
    imp = sealed.improvement(vals) if n >= 2 else 0.0
    thr, sep = sealed.two_means_split(vals)
    abstained = gate.abstains(imp, n)
    if abstained:
        sep = 0.0                      # no boundary claimed
    return {"O_by_min": O_by_min, "min_idx": min_idx, "thr": thr, "sep": float(sep),
            "improvement": float(imp), "n_minimal": n, "abstained": bool(abstained)}
