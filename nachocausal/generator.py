"""GENERATOR — produces (poset, hidden embedding) SEPARATELY.

FROZEN. The validation path is PURE NUMPY: numpy Poisson-uniform sprinkle +
Glue-3 uniformity gate + past_matrix_fast. It does NOT import Minz and contains
NO absolute path. The Minz cross-check `gate()` is optional and the ONLY place
Minz is referenced; it is located via the env var NACHOCAUSAL_MINZ_PATH and is
off the validation path (its admissibility evidence is recorded once in
nachocausal/fixtures/gate_evidence.json — cmte SWE MAJOR-2).

2D EF identity (Glue 3): det g = -1 (sqrt(-g)=1), so a coordinate-uniform
Poisson process IS the natural-volume Poisson process (preregistration.md:61).
EGS confirm det g is constant in both Schwarzschild and (t*,r) coordinates.
"""

from __future__ import annotations

import os
import sys
from typing import List, Tuple

import numpy as np

from . import thresholds

# Glue-3 (b) gate: pre-committed critical value for the per-axis equiprobable-bin
# uniformity chi-square. dof = _UNIFORMITY_BINS - 1 = 4; alpha = 1e-3, so the
# critical value is chi2_{0.999,4} = 18.467 (fixed in advance). This tests
# MARGINAL uniformity per axis (not joint 2D), which for a cuboid Poisson
# sprinkle is sufficient (cmte phys MINOR-1).
_UNIFORMITY_BINS = 5
_CHI2_CRIT_DOF4_P001 = 18.467


# =============================================================================
# Numpy Poisson-uniform sprinkle (same cloud for BH and MINK at a given seed).
# =============================================================================
def numpy_sprinkle(
    seed: int, intensity: float, t_edge: float = thresholds.T_EDGE
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Poisson(intensity) points uniform in the tall box; coordinate-uniform ==
    natural volume for 2D EF (Glue 3). Returns (embedding, edges, center).
    The SAME embedding is used to build both the BH and MINK posets, so the two
    causal sets sit on one identical point cloud and differ only in causality."""
    edges = np.array([t_edge, thresholds.R_EDGE], float)
    center = np.array([t_edge / 2.0, thresholds.R_CENTER], float)  # t in [0, t_edge]
    rng = np.random.default_rng(seed)
    n = rng.poisson(intensity)
    low = center - edges / 2.0
    pts = low + rng.random((n, 2)) * edges
    return pts, edges, center


def assert_coordinate_uniform(
    embedding: np.ndarray, edges: np.ndarray, center: np.ndarray
) -> None:
    """Glue-3 (b): RAISES if any point lies outside the box, or if either axis'
    equiprobable-bin chi-square exceeds the pre-committed critical value. A
    guardrail that CAN fail (founding rule); near-tautological on a correct numpy
    uniform sprinkle, but it catches a broken sprinkle / wrong shape."""
    edges = np.asarray(edges, float)
    center = np.asarray(center, float)
    low = center - edges / 2.0
    high = center + edges / 2.0
    outside = np.any((embedding < low - 1e-6) | (embedding > high + 1e-6), axis=1)
    if int(np.count_nonzero(outside)):
        raise ValueError(
            f"Glue3 violated: {int(np.count_nonzero(outside))} point(s) outside "
            f"box low={low.tolist()} high={high.tolist()}."
        )
    nb = _UNIFORMITY_BINS
    for axis, name in ((0, "t"), (1, "r")):
        x = np.clip(embedding[:, axis], low[axis], high[axis])
        bins = np.linspace(low[axis], high[axis], nb + 1)
        counts, _ = np.histogram(x, bins=bins)
        exp = x.size / nb
        chi2 = float(np.sum((counts - exp) ** 2 / exp)) if exp > 0 else float("nan")
        if not np.isfinite(chi2) or chi2 > _CHI2_CRIT_DOF4_P001:
            raise ValueError(
                f"Glue3 violated: axis {name} chi2={chi2:.2f} exceeds "
                f"pre-committed critical {_CHI2_CRIT_DOF4_P001} (dof={nb - 1}, "
                f"p=1e-3); sprinkle is not coordinate-uniform."
            )


# =============================================================================
# Vectorized accelerator — verified bit-for-bit vs Minz (docs/reuse_check.md).
# =============================================================================
def past_matrix_fast(
    embedding: np.ndarray, kind: str, r_S: float = thresholds.R_S
) -> np.ndarray:
    """N x N past matrix C[i,j] = (j in causal past of i), from coordinates,
    replicating Minz's closed-form 2D relations (MINK: isCausal_flat2D
    spacetimes.py:295; BH EF: isCausal_BH2D spacetimes.py:759). Convention
    matches Minz PastMatrix: C[i,j] True iff event j precedes i."""
    eps = 1e-12  # == Minz causality_eps
    if kind not in ("MINK", "BH"):
        raise ValueError(f"unknown kind {kind!r}")
    t = embedding[:, 0].astype(float)
    r = embedding[:, 1].astype(float)
    N = embedding.shape[0]
    C = np.zeros((N, N), dtype=bool)
    if kind == "BH":
        with np.errstate(divide="ignore", invalid="ignore"):
            func = r + 2.0 * r_S * np.log(np.abs(r - r_S) / r_S)
    block = max(1, 64_000_000 // (8 * max(N, 1)))
    rj = r[None, :]
    tj = t[None, :]
    for a in range(0, N, block):
        b = min(a + block, N)
        ti = t[a:b, None]
        ri = r[a:b, None]
        dt = ti - tj
        if kind == "MINK":
            C[a:b] = (dt > 0.0) & (dt >= np.abs(ri - rj) - eps)
        else:  # BH, Eddington-Finkelstein
            earlier = tj < ti
            t_out = func[a:b, None] - func[None, :]
            t_in = rj - ri
            b1 = (ri <= rj) & (rj <= r_S)
            b2 = (rj >= r_S) & (rj >= ri)
            b3 = (rj >= r_S) & (rj <= ri)
            isc = np.where(
                b1,
                (t_out >= dt) & (dt >= t_in),
                np.where(b2, dt >= t_in, np.where(b3, dt >= t_out, False)),
            )
            C[a:b] = earlier & isc
    np.fill_diagonal(C, False)
    return C


# =============================================================================
# OPTIONAL Minz gate (admissibility evidence). Off the validation path.
# =============================================================================
def verify_fast_matches_minz(minz_matrix, fast_matrix, kind: str) -> None:
    """Hard gate: the accelerator may be used ONLY where it reproduces Minz's
    poset bit-for-bit on the same coordinates. RAISES on any disagreement."""
    minz = minz_matrix.astype(bool)
    if minz.shape != fast_matrix.shape:
        raise ValueError(f"[{kind}] fast/Minz shape mismatch")
    disagree = minz != fast_matrix
    n = int(np.count_nonzero(disagree))
    if n:
        ij = np.argwhere(disagree)[:5].tolist()
        raise ValueError(
            f"[{kind}] ACCELERATOR REJECTED: {n} poset entries differ from Minz "
            f"(first [i,j]={ij}); Minz remains the only trusted relation."
        )


def gate(kind: str, intensity: float = 420.0, seed: int = 20240617) -> int:
    """Run the Minz cross-check once at small N: build the Minz poset and the
    fast poset on the SAME Minz-drawn coordinates and assert bit-for-bit
    agreement. Requires the Minz clone (env NACHOCAUSAL_MINZ_PATH). Returns N.
    NOT on the validation path; used only to (re)produce admissibility evidence."""
    minz_parent = os.path.expanduser(
        os.environ.get("NACHOCAUSAL_MINZ_PATH", "~/cs-horizon-reuse-check")
    )
    if minz_parent not in sys.path:
        sys.path.insert(0, minz_parent)
    from causets.sprinkledcauset import SprinkledCauset  # noqa: E402
    from causets.spacetimes import BlackHoleSpacetime, FlatSpacetime  # noqa: E402
    from causets.shapes import CoordinateShape  # noqa: E402

    shape = CoordinateShape(
        2, "cuboid",
        edges=np.array([2.0, thresholds.R_EDGE], float),
        center=np.array([1.0, thresholds.R_CENTER], float),
    )
    st = (BlackHoleSpacetime(2, r_S=thresholds.R_S, metric="Eddington-Finkelstein")
          if kind == "BH" else FlatSpacetime(2))
    rng = np.random.default_rng(seed)
    C = SprinkledCauset(dim=2, spacetime=st, shape=shape)
    C.intensify(intensity, rng=rng, shape=shape)
    events = C.sortedByCausality()
    emb = np.array([e.Coordinates for e in events], float)
    Cm = C.PastMatrix(events, dtype=bool)
    Cf = past_matrix_fast(emb, kind, thresholds.R_S)
    verify_fast_matches_minz(Cm, Cf, kind)
    return emb.shape[0]
