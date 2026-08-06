"""Geometry and order kernel for the pedagogical figures of the limits manuscript.

No drawing here: this module holds only 1+1 Schwarzschild geometry, the sprinkling,
and the causal order.  The `figNN_*.py` files import from here and only draw.

Conventions, and why they are exact
-----------------------------------
1+1 Schwarzschild metric in `(t, r)` coordinates, exterior `r > rs`:

    g = -(1 - rs/r) dt^2 + (1 - rs/r)^{-1} dr^2

Two facts make everything below exact rather than approximate:

1. `det g = -1`, so the volume form is `dt dr`.  A Poisson sprinkling conditioned on
   `N = n` is therefore **n iid uniform points in the `(t, r)` rectangle** — no
   Jacobian, no weights.  Any weighting in this code would be a bug.

2. With the tortoise coordinate `r* = r + rs·ln|r/rs - 1|` the metric becomes
   `(1 - rs/r)·(-dt^2 + dr*^2)`: conformally flat.  A conformal factor does not
   change the causal order, so the order is **exactly** the Minkowski order in
   `(t, r*)`, i.e. the product order in the null coordinates `u = t - r*`,
   `v = t + r*`.  No geodesics need to be integrated.

Dilation (Theorem 3.1)
----------------------
`Phi_s(t, r) = (s·t, s·r)` carries the horizon-radius-`rs` model to the `s·rs` one.
In tortoise coordinates:

    r*(s·r ; s·rs) = s·r + s·rs·ln|s·r/(s·rs) - 1| = s·(r + rs·ln|r/rs - 1|)
                   = s · r*(r ; rs)

hence `(u, v) -> (s·u, s·v)`: a dilation of the null coordinates, which preserves the
product order **element by element**.  This is why Theorem 3.1 is an exact identity
and not an approximation, and `check_dilation_identity` verifies it.
"""

from __future__ import annotations

import numpy as np

__all__ = [
    "tortoise",
    "null_coords",
    "sprinkle_exterior",
    "causal_matrix",
    "dilate",
    "check_dilation_identity",
    "hasse_edges",
    "layer_of",
    "future_volume",
    "comparable_fraction",
]


# --------------------------------------------------------------------------- #
# Geometry
# --------------------------------------------------------------------------- #

def tortoise(r, rs):
    """Tortoise coordinate `r* = r + rs·ln|r/rs - 1|`.  Exterior only: `r > rs`."""
    r = np.asarray(r, dtype=float)
    if np.any(r <= rs):
        raise ValueError("tortoise() is defined here only on the exterior r > rs")
    return r + rs * np.log(r / rs - 1.0)


def null_coords(t, r, rs):
    """Null coordinates `(u, v) = (t - r*, t + r*)`.  Causal order = product order."""
    rstar = tortoise(r, rs)
    return t - rstar, t + rstar


def sprinkle_exterior(rs, t_range, r_range, n, rng):
    """`n` iid points from the volume form on the `(t, r)` rectangle.

    Since `det g = -1`, the volume form is `dt dr` and the sampling is uniform.
    Returns `(t, r)`, each of shape `(n,)`.
    """
    if r_range[0] <= rs:
        raise ValueError("the patch must lie in the exterior: r_lo > rs")
    t = rng.uniform(t_range[0], t_range[1], size=n)
    r = rng.uniform(r_range[0], r_range[1], size=n)
    return t, r


# --------------------------------------------------------------------------- #
# Causal order
# --------------------------------------------------------------------------- #

def causal_matrix(t, r, rs):
    """Boolean matrix `rel[i, j] = (i strictly precedes j)`.

    `i < j` iff `u_i <= u_j` and `v_i <= v_j` and `i != j` (product order in nulls).
    """
    u, v = null_coords(t, r, rs)
    le = (u[:, None] <= u[None, :]) & (v[:, None] <= v[None, :])
    np.fill_diagonal(le, False)
    return le


def dilate(t, r, rs, s):
    """`Phi_s`: returns `(s·t, s·r, s·rs)` — the same point set in the dilated model."""
    return s * np.asarray(t, float), s * np.asarray(r, float), s * rs


def check_dilation_identity(t, r, rs, s):
    """Check that `Phi_s` preserves the order **element by element**.

    Returns `(identical, n_discrepancies)`.  This is the numerical check of the
    mechanism behind Theorem 3.1: it does not check the theorem (which is about
    laws), but that this particular realisation induces literally the same labelled
    poset in both models.
    """
    rel_a = causal_matrix(t, r, rs)
    t_b, r_b, rs_b = dilate(t, r, rs, s)
    rel_b = causal_matrix(t_b, r_b, rs_b)
    diff = int(np.sum(rel_a != rel_b))
    return diff == 0, diff


# --------------------------------------------------------------------------- #
# Poset utilities
# --------------------------------------------------------------------------- #

def hasse_edges(rel):
    """Covering edges (transitive reduction) of a strict order relation."""
    n = rel.shape[0]
    cover = rel.copy()
    for i in range(n):
        for j in range(n):
            if not rel[i, j]:
                continue
            # i < j stops being a cover if some k has i < k < j
            if np.any(rel[i] & rel[:, j]):
                cover[i, j] = False
    return [(i, j) for i in range(n) for j in range(n) if cover[i, j]]


def layer_of(rel):
    """Height of each element: length of the longest chain ending at it."""
    n = rel.shape[0]
    layer = np.zeros(n, dtype=int)
    order = np.argsort(rel.sum(axis=0))  # fewest predecessors first
    for _ in range(n):
        changed = False
        for j in order:
            preds = np.nonzero(rel[:, j])[0]
            new = 0 if preds.size == 0 else int(layer[preds].max()) + 1
            if new != layer[j]:
                layer[j] = new
                changed = True
        if not changed:
            break
    return layer


def future_volume(rel):
    """`|future(i)|` — cardinality of the strict future of each element."""
    return rel.sum(axis=1)


def comparable_fraction(rel):
    """Fraction of unordered pairs that are comparable."""
    n = rel.shape[0]
    total = n * (n - 1) // 2
    return float(rel.sum()) / total if total else 0.0
