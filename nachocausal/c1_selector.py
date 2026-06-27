"""C1 relational selector preflight.

This module implements only the current written draft `R = Max(C)` so tests can
lock in its finite-poset consequence: `down(Max(C)) = C`, hence no interface.
It is a negative preflight guardrail, not a C1 signal implementation.
"""

from __future__ import annotations

from typing import Dict, FrozenSet, Tuple

import numpy as np


Selection = Dict[str, FrozenSet[int] | FrozenSet[Tuple[int, int]]]


def maximal_elements(past_matrix: np.ndarray) -> FrozenSet[int]:
    """Return maximal elements of the finite poset."""
    if past_matrix.dtype != bool:
        past_matrix = past_matrix.astype(bool)
    n = past_matrix.shape[0]
    assert past_matrix.shape == (n, n), "C1 selector expects a square poset matrix"
    has_future = past_matrix.any(axis=0)
    return frozenset(int(i) for i, value in enumerate(has_future) if not value)


def down_closure(past_matrix: np.ndarray, reference: FrozenSet[int]) -> FrozenSet[int]:
    """Return `{x : exists r in reference, x <= r}` for the past-matrix convention."""
    if past_matrix.dtype != bool:
        past_matrix = past_matrix.astype(bool)
    n = past_matrix.shape[0]
    assert past_matrix.shape == (n, n), "C1 selector expects a square poset matrix"
    closure = set(reference)
    for r in reference:
        closure.update(int(x) for x in np.nonzero(past_matrix[int(r), :])[0])
    return frozenset(closure)


def cover_relations(past_matrix: np.ndarray) -> FrozenSet[Tuple[int, int]]:
    """Return ordered cover pairs `(x, y)` with `x < y` and no strict intermediate."""
    if past_matrix.dtype != bool:
        past_matrix = past_matrix.astype(bool)
    n = past_matrix.shape[0]
    assert past_matrix.shape == (n, n), "C1 selector expects a square poset matrix"
    covers: set[Tuple[int, int]] = set()
    for y in range(n):
        for x in np.nonzero(past_matrix[y, :])[0]:
            x = int(x)
            intermediates = past_matrix[y, :] & past_matrix[:, x]
            if not intermediates.any():
                covers.add((x, y))
    return frozenset(covers)


def c1_selector(past_matrix: np.ndarray) -> Selection:
    """Select the draft C1 reference and finite interface.

    Returns only element labels so it can be checked by
    `verify_selection_order_only`. For finite nonempty posets under the current
    draft, the interface is expected to be empty.
    """
    if past_matrix.dtype != bool:
        past_matrix = past_matrix.astype(bool)
    n = past_matrix.shape[0]
    assert past_matrix.shape == (n, n), "C1 selector expects a square poset matrix"

    reference = maximal_elements(past_matrix)
    accessible = down_closure(past_matrix, reference)
    black_region = frozenset(i for i in range(n) if i not in accessible)
    covers = cover_relations(past_matrix)
    interface = frozenset(
        (x, y) for x, y in covers if x in black_region and y in accessible
    )
    return {"R": reference, "interface": interface}


def c1_status(selection: Selection) -> str:
    """Interpret only the selector status, not physics."""
    return "NO_INTERFACE" if not selection["interface"] else "INTERFACE_PRESENT"
