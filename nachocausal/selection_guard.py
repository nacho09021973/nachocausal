"""Generic Guard-v for order-only element selection.

This module verifies selectors, not scalar observables. A selector receives only
the boolean past matrix and returns element labels, possibly nested in simple
Python containers. Under a pure relabelling of the poset, the selected labels
must relabel-conjugate exactly.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Callable

import numpy as np


def _map_labels(obj: Any, old_to_new: np.ndarray) -> Any:
    if isinstance(obj, (int, np.integer)):
        return int(old_to_new[int(obj)])
    if isinstance(obj, tuple):
        return tuple(_map_labels(x, old_to_new) for x in obj)
    if isinstance(obj, list):
        return [_map_labels(x, old_to_new) for x in obj]
    if isinstance(obj, (set, frozenset)):
        return frozenset(_map_labels(x, old_to_new) for x in obj)
    if isinstance(obj, Mapping):
        return {k: _map_labels(v, old_to_new) for k, v in obj.items()}
    if obj is None or isinstance(obj, str):
        return obj
    raise TypeError(f"unsupported selector output component: {type(obj).__name__}")


def _canonical(obj: Any) -> Any:
    if isinstance(obj, (int, np.integer)):
        return ("int", int(obj))
    if isinstance(obj, tuple):
        return ("tuple", tuple(_canonical(x) for x in obj))
    if isinstance(obj, list):
        return ("list", tuple(_canonical(x) for x in obj))
    if isinstance(obj, (set, frozenset)):
        return ("set", tuple(sorted((_canonical(x) for x in obj), key=repr)))
    if isinstance(obj, Mapping):
        return (
            "dict",
            tuple(sorted(((repr(k), _canonical(v)) for k, v in obj.items()), key=repr)),
        )
    if obj is None or isinstance(obj, str):
        return ("atom", obj)
    raise TypeError(f"unsupported selector output component: {type(obj).__name__}")


def verify_selection_order_only(
    past_matrix: np.ndarray,
    selector: Callable[[np.ndarray], Any],
    seed: int = 0,
) -> Any:
    """Raise if an element-selection rule is not relabel-conjugate.

    `selector` must take only the boolean past matrix and return selected
    element labels, e.g. a set of elements, a set of linked pairs, or a dict such
    as `{"R": {...}, "interface": {(..., ...)}}`. Numeric scalar scores should
    not be included in this output; guard those separately as observables.
    """
    if past_matrix.dtype != bool:
        past_matrix = past_matrix.astype(bool)
    n = past_matrix.shape[0]
    assert past_matrix.shape == (n, n), "selection guard expects a square poset matrix"

    selected = selector(past_matrix)
    rng = np.random.default_rng(seed)
    perm = rng.permutation(n)
    permuted = past_matrix[perm][:, perm]
    selected_permuted = selector(permuted)

    old_to_new = np.empty(n, dtype=int)
    old_to_new[perm] = np.arange(n)
    expected = _map_labels(selected, old_to_new)

    if _canonical(expected) != _canonical(selected_permuted):
        raise ValueError(
            "Guard (v) VIOLATED: selection changed under a pure relabelling; "
            "the selector is not order-only / relabel-conjugate."
        )
    return selected
