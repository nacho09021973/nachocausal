#!/usr/bin/env python
"""
nachocausal -- DEV PROTOTYPE (exploration only). NOT frozen, NOT a result.

Implements the mandatory separation architecture of pre-registration guard (v):

    generator  (sees coordinates) -> produces (poset, hidden_embedding) SEPARATELY
    estimator  (sees ONLY the poset matrix + |C|) -> computes O(i)
    scorer     (sees the embedding) -> DEV post-hoc inspection ONLY, never feeds estimator

Reuse decision (docs/reuse_check.md): generation via c-minz/Python-causets (referenced
from a scratch clone, NOT vendored, NOT committed). Glue we wrote here: box-matched cuboid,
det g = -1 handling (Glue 3), and the single-source longest-future-chain estimator O
(Glue 2; NOT Minz Paths(a,b) over all pairs).

This file does NO thresholding and reports NO verdict. It only looks.
"""

from __future__ import annotations

import os
import sys
from typing import Dict, List, Tuple

import numpy as np

# --- Make Minz importable from the scratch clone WITHOUT vendoring it. --------
# The clone dir contains a symlink `causets -> Python-causets`, so adding the
# parent of that symlink to sys.path makes `import causets` resolve. We do NOT
# copy or commit any of it; this is a runtime path reference only.
_MINZ_PARENT = os.path.expanduser("~/cs-horizon-reuse-check")
if _MINZ_PARENT not in sys.path:
    sys.path.insert(0, _MINZ_PARENT)

from causets.sprinkledcauset import SprinkledCauset  # noqa: E402
from causets.spacetimes import BlackHoleSpacetime, FlatSpacetime  # noqa: E402
from causets.shapes import CoordinateShape  # noqa: E402


# =============================================================================
# GENERATOR  -- sees coordinates. Returns poset and embedding SEPARATELY.
# =============================================================================
def generate(
    kind: str,
    seed: int,
    intensity: float,
    edges: List[float],
    center: List[float],
    r_S: float = 0.5,
) -> Tuple[np.ndarray, int, np.ndarray]:
    """
    kind: 'BH'  -> BlackHoleSpacetime(2, r_S, Eddington-Finkelstein)
          'MINK'-> FlatSpacetime(2)  (box-matched control)
    Returns (past_matrix C, N, embedding) where:
        C[i,j] is True iff event j is in the causal past of event i  (the poset),
        N = |C|,
        embedding[i] = (t, r) coordinates of event i  -- FOR THE SCORER ONLY.
    The embedding is returned as a SEPARATE object; callers must not pass it
    to the estimator.
    """
    shape = CoordinateShape(
        2,
        "cuboid",
        edges=np.array(edges, dtype=float),
        center=np.array(center, dtype=float),
    )
    if kind == "BH":
        st = BlackHoleSpacetime(2, r_S=r_S, metric="Eddington-Finkelstein")
    elif kind == "MINK":
        st = FlatSpacetime(2)
    else:
        raise ValueError(f"unknown kind {kind!r}")

    # Genuine Poisson sprinkling (intensify -> rng.poisson), seeded explicitly.
    # We construct empty then intensify so we control the rng (the __init__
    # path uses an unseeded module-level default rng).
    rng = np.random.default_rng(seed)
    C = SprinkledCauset(dim=2, spacetime=st, shape=shape)
    C.intensify(intensity, rng=rng, shape=shape)

    events = C.sortedByCausality()
    past_matrix = C.PastMatrix(events, dtype=bool)
    embedding = np.array([e.Coordinates for e in events], dtype=float)
    N = past_matrix.shape[0]

    # --- Glue 3: det g = -1 handling. ---------------------------------------
    # Minz exposes NO metric-tensor accessor (only MetricName); see
    # docs/reuse_check.md. So we take the documented contingency (path ii):
    #   (a) ASSERT the 2D analytic fact sqrt(-g)=1 for EF (det g = -1), so that
    #       coordinate-uniform sampling == natural-volume Poisson, and
    #   (b) NUMERICALLY verify the sprinkle is coordinate-uniform in the box.
    # (a) is an assertion of a known 2D identity, not a measurement; (b) is the
    # measurement that the tooling actually realises it.
    _assert_coordinate_uniform(embedding, edges, center)

    return past_matrix, N, embedding


# Glue 3 (b) gate: pre-committed critical value for the per-axis uniformity
# chi-square. dof = _UNIFORMITY_BINS - 1 = 4; alpha = 1e-3, so the critical
# value is chi2_{0.999, 4} = 18.467 (standard chi-square table, fixed in
# advance per the threshold-anchoring rule). Low enough that a genuinely
# uniform sprinkle effectively never trips it, but a gross departure (e.g.
# radial densification or a wrong shape/spacetime) does. This makes Glue 3's
# uniformity claim an assertion that CAN fail, not a printed decoration.
_UNIFORMITY_BINS = 5
_CHI2_CRIT_DOF4_P001 = 18.467


def _assert_coordinate_uniform(
    embedding: np.ndarray, edges: List[float], center: List[float]
) -> None:
    """Glue 3 (b): ASSERT the sprinkle is uniform-in-coordinates over the box.

    For 2D EF, det g = -1 (sqrt(-g)=1) is asserted analytically, so a
    coordinate-uniform Poisson process IS the natural-volume Poisson process.
    This turns that into a guardrail that can fail (README founding rule): it
    RAISES if any point lies outside the box, or if either axis' equiprobable-
    bin chi-square exceeds the pre-committed critical value (dof=4, p=1e-3).
    Diagnostics are still printed for transparency.
    """
    edges = np.asarray(edges, dtype=float)
    center = np.asarray(center, dtype=float)
    low = center - edges / 2.0
    high = center + edges / 2.0
    outside_mask = np.any(
        (embedding < low - 1e-6) | (embedding > high + 1e-6), axis=1
    )
    n_outside = int(np.count_nonzero(outside_mask))
    print(f"    [Glue3] det g = -1 (2D EF) ASSERTED analytically (sqrt(-g)=1).")
    print(
        f"    [Glue3] all {embedding.shape[0]} points inside box: "
        f"{n_outside == 0}"
    )
    if n_outside:
        raise ValueError(
            f"Glue3 violated: {n_outside} sprinkled point(s) outside box "
            f"low={low.tolist()} high={high.tolist()}; the "
            f"coordinate-uniform == natural-volume reasoning no longer holds."
        )
    nb = _UNIFORMITY_BINS
    for axis, name in ((0, "t"), (1, "r")):
        # clip into [low, high]: points within the 1e-6 inside-box tolerance
        # must still be counted so the bins sum to N and chi2 is undistorted.
        x = np.clip(embedding[:, axis], low[axis], high[axis])
        bins = np.linspace(low[axis], high[axis], nb + 1)
        counts, _ = np.histogram(x, bins=bins)
        exp = x.size / nb
        chi2 = float(np.sum((counts - exp) ** 2 / exp)) if exp > 0 else float("nan")
        print(
            f"    [Glue3] axis {name}: counts/{nb}-equal-bins {counts.tolist()} "
            f"(expected ~{exp:.1f} each), chi2={chi2:.2f} "
            f"(dof={nb - 1}, crit={_CHI2_CRIT_DOF4_P001} @ p=1e-3)"
        )
        if not np.isfinite(chi2) or chi2 > _CHI2_CRIT_DOF4_P001:
            raise ValueError(
                f"Glue3 violated: axis {name} chi2={chi2:.2f} exceeds "
                f"pre-committed critical {_CHI2_CRIT_DOF4_P001} (dof={nb - 1}, "
                f"p=1e-3); sprinkle is not coordinate-uniform."
            )


# =============================================================================
# ESTIMATOR  -- sees ONLY the poset matrix + |C|. No coordinates. No labels.
# =============================================================================
def estimate_O(past_matrix: np.ndarray) -> Tuple[Dict[int, int], List[int], np.ndarray]:
    """
    Glue 2. INPUT: the boolean past matrix C ONLY (C[i,j] True iff j < i).
    From this alone:
      * minimal elements (PastInf) = rows with no past (all-False row);
      * O(i) for minimal i = length (in #elements) of the maximal timelike
        chain starting at i, computed as a SINGLE-SOURCE LONGEST PATH on the
        DAG via DP in topological order (element forward-height).
    We deliberately do NOT use Minz Paths(a,b) over all pairs.

    Returns (O_by_minimal_index, minimal_indices, longest_future_chain_all).
    """
    if past_matrix.dtype != bool:
        past_matrix = past_matrix.astype(bool)
    N = past_matrix.shape[0]
    assert past_matrix.shape == (N, N), "estimator expects a square poset matrix"
    # Guard (v): the estimator's only input is an N x N boolean order matrix.
    # There is no coordinate array in scope here at all.

    # future(e) = indices f with C[f, e] True  (e in past of f  <=>  f in future of e)
    # longest forward chain Lfut(e) = 1 + max(Lfut(f) for f in future(e)), else 1.
    Lfut = np.zeros(N, dtype=int)
    order = _topological_future_first(past_matrix)  # process sinks first
    for e in order:
        future = np.nonzero(past_matrix[:, e])[0]
        Lfut[e] = 1 + (int(Lfut[future].max()) if future.size else 0)

    # minimal elements: empty past => all-False row of C
    has_past = past_matrix.any(axis=1)
    minimal_indices = [i for i in range(N) if not has_past[i]]
    O_by_minimal = {i: int(Lfut[i]) for i in minimal_indices}
    return O_by_minimal, minimal_indices, Lfut


# =============================================================================
# OPTIONAL ACCELERATOR (ours) -- vectorized poset, GATED by exact equality with
# Minz. Minz's pure-Python relate() is O(N^2) and dominates generation cost
# (~16 min/sprinkling at N=1e4). This computes the SAME poset in vectorized
# numpy, but Minz REMAINS the reference relation: the fast matrix may be used
# only where verify_fast_matches_minz() confirms bit-for-bit agreement on the
# same coordinates. It is a verified third implementation, not a new physics
# claim (Minz is the reference; vidh2000 C++ is the independent cross-check).
# =============================================================================
def past_matrix_fast(embedding: np.ndarray, kind: str, r_S: float = 0.5) -> np.ndarray:
    """Vectorized N x N past matrix C[i,j] = (j in causal past of i), built
    directly from coordinates, replicating Minz's closed-form 2D relation:
      MINK: isCausal_flat2D            (spacetimes.py:295)
      BH:   isCausal_BH2D, EF branch   (spacetimes.py:759)  -- closed form,
            no Newton iteration (that lives only in _XT_slice, for plotting).
    Convention matches Minz PastMatrix: C[i,j] True iff event j precedes i.
    """
    eps = 1e-12  # == Minz causality_eps (spacetimes.py:21)
    if kind not in ("MINK", "BH"):
        raise ValueError(f"unknown kind {kind!r}")
    t = embedding[:, 0].astype(float)
    r = embedding[:, 1].astype(float)
    N = embedding.shape[0]
    C = np.zeros((N, N), dtype=bool)  # the only N x N allocation we keep
    # func(r) for the EF outgoing lightray from the origin (BH only).
    if kind == "BH":
        with np.errstate(divide="ignore", invalid="ignore"):
            func = r + 2.0 * r_S * np.log(np.abs(r - r_S) / r_S)
    # Row-block chunking: cap each block temporary near ~64 MB (8 bytes/float),
    # so peak memory stays bounded regardless of N (only C scales as N^2 bool).
    block = max(1, 64_000_000 // (8 * max(N, 1)))
    rj = r[None, :]
    tj = t[None, :]
    for a in range(0, N, block):
        b = min(a + block, N)
        ti = t[a:b, None]
        ri = r[a:b, None]
        dt = ti - tj  # t_i - t_j  (rows i in [a,b), all cols j)
        if kind == "MINK":
            C[a:b] = (dt > 0.0) & (dt >= np.abs(ri - rj) - eps)
        else:  # BH, Eddington-Finkelstein
            # j is the earlier (past-candidate) element x; i the later one y.
            earlier = tj < ti
            t_out = func[a:b, None] - func[None, :]  # func(r_y) - func(r_x)
            t_in = rj - ri  # r_x - r_y
            b1 = (ri <= rj) & (rj <= r_S)  # r_y <= r_x <= r_S (x inside)
            b2 = (rj >= r_S) & (rj >= ri)  # r_S <= r_x, r_x >= r_y
            b3 = (rj >= r_S) & (rj <= ri)  # r_S <= r_x <= r_y
            isc = np.where(
                b1,
                (t_out >= dt) & (dt >= t_in),
                np.where(b2, dt >= t_in, np.where(b3, dt >= t_out, False)),
            )
            C[a:b] = earlier & isc
    np.fill_diagonal(C, False)
    return C


def verify_fast_matches_minz(
    minz_matrix: np.ndarray, fast_matrix: np.ndarray, kind: str
) -> None:
    """Hard gate: the accelerator may be used ONLY where it reproduces Minz's
    poset bit-for-bit on the same coordinates. Raises on any disagreement so an
    incorrect fast path fails loud instead of silently corrupting a result."""
    minz = minz_matrix.astype(bool)
    if minz.shape != fast_matrix.shape:
        raise ValueError(f"[{kind}] fast/Minz shape mismatch")
    disagree = minz != fast_matrix
    n = int(np.count_nonzero(disagree))
    if n:
        ij = np.argwhere(disagree)[:5].tolist()
        raise ValueError(
            f"[{kind}] ACCELERATOR REJECTED: {n} poset entries differ from "
            f"Minz (first [i,j]={ij}); Minz remains the only trusted relation."
        )
    print(
        f"    [fast] vectorized poset == Minz bit-for-bit ({kind}): "
        f"{minz.shape[0]}^2 entries agree."
    )


def _topological_future_first(past_matrix: np.ndarray) -> List[int]:
    """Order indices so that every element appears before its past (Kahn on the
    future->past DAG): elements with no future (sinks) first. Pure order, no
    coordinates."""
    N = past_matrix.shape[0]
    # out-degree toward future = number of f with C[f,e] (column sum)
    future_count = past_matrix.sum(axis=0).astype(int)
    ready = [e for e in range(N) if future_count[e] == 0]
    order: List[int] = []
    fc = future_count.copy()
    while ready:
        e = ready.pop()
        order.append(e)
        # e's past elements p (C[e, p] True) lose one future
        for p in np.nonzero(past_matrix[e, :])[0]:
            fc[p] -= 1
            if fc[p] == 0:
                ready.append(int(p))
    assert len(order) == N, "cycle detected -- not a DAG"
    return order


# =============================================================================
# SCORER  -- sees the embedding. DEV POST-HOC INSPECTION ONLY.
# !!! Nothing computed here ever feeds back into estimate_O. !!!
# =============================================================================
def dev_score_O_vs_r(
    O_by_minimal: Dict[int, int], embedding: np.ndarray, r_S: float
) -> None:
    """DEV SCORING ONLY (guard: ground truth only scores). Reveals hidden r to
    eyeball whether the bimodality of O lines up with interior (r<r_S) vs
    exterior (r>=r_S). Prints a table sorted by hidden r."""
    print(f"    [DEV-SCORING] hidden r revealed for inspection only; r_S={r_S}")
    print(f"    {'idx':>5} {'r_hidden':>10} {'t_hidden':>10} {'O':>5}  region")
    rows = sorted(O_by_minimal.keys(), key=lambda i: embedding[i, 1])
    for i in rows:
        t, r = embedding[i, 0], embedding[i, 1]
        region = "interior" if r < r_S else "exterior"
        print(f"    {i:>5} {r:>10.4f} {t:>10.4f} {O_by_minimal[i]:>5}  {region}")


# =============================================================================
# GUARD (v) ARTIFACT -- order-only invariance of O, runnable and verifiable.
# =============================================================================
def verify_order_only(past_matrix: np.ndarray, seed: int = 0) -> Dict[int, int]:
    """Runnable evidence for success criterion (v): O depends ONLY on the
    abstract poset, never on labels/coordinates.

    We relabel the elements by a random permutation P -- i.e. conjugate the
    order matrix, C' = C[P][:, P] -- and recompute O. A permutation is a pure
    relabelling: it preserves the order but destroys any index/coordinate
    correlation. If O were contaminated by labels or coordinates, the multiset
    of O over minimal elements would change. We RAISE if it does.

    Returns the per-element permutation map (for the caller to report).
    """
    O0, min0, _ = estimate_O(past_matrix)
    rng = np.random.default_rng(seed)
    N = past_matrix.shape[0]
    perm = rng.permutation(N)
    permuted = past_matrix[perm][:, perm]
    O1, min1, _ = estimate_O(permuted)

    multiset0 = sorted(O0.values())
    multiset1 = sorted(O1.values())
    if len(min1) != len(min0) or multiset1 != multiset0:
        raise ValueError(
            "Guard (v) VIOLATED: O changed under a pure relabelling "
            f"(|minimal| {len(min0)}->{len(min1)}, "
            f"O-multiset {multiset0} -> {multiset1}); O is NOT order-only."
        )
    # Stronger: the value must track the element through the permutation,
    # not merely match as a multiset. perm maps new index -> old index.
    inv = np.empty(N, dtype=int)
    inv[perm] = np.arange(N)  # old index -> new index
    for old_i, o_val in O0.items():
        new_i = int(inv[old_i])
        if O1.get(new_i) != o_val:
            raise ValueError(
                f"Guard (v) VIOLATED: element O not invariant under relabel "
                f"(old {old_i} O={o_val} -> new {new_i} O={O1.get(new_i)})."
            )
    print(
        f"    [Guard-v] O invariant under random relabel (seed={seed}): "
        f"|minimal|={len(min0)}, O-multiset preserved element-wise. "
        f"O is order-only."
    )
    return {int(k): int(v) for k, v in O0.items()}


# =============================================================================
# Helpers for the smoke-test
# =============================================================================
def histogram_O(O_values: List[int]) -> None:
    if not O_values:
        print("    (no minimal elements)")
        return
    lo, hi = min(O_values), max(O_values)
    bins = np.arange(lo, hi + 2)
    counts, edges = np.histogram(O_values, bins=bins)
    for b, c in zip(edges[:-1], counts):
        bar = "#" * int(c)
        print(f"    O={int(b):>3} : {int(c):>4} {bar}")


# =============================================================================
# SMOKE-TEST  (DEV)
# =============================================================================
def smoke() -> None:
    # ---- DEV seed, documented and DISJOINT from any future validation seed ---
    DEV_SEED = 20240617  # dev only; validation seeds will be a disjoint set
    INTENSITY = 420.0  # expected count (small, fast); Poisson-realised
    R_S = 0.5  # Minz default Schwarzschild radius (HIDDEN from estimator)
    # box-matched cuboid: SAME edges+center for BH and Minkowski control
    EDGES = [2.0, 1.2]  # (t-edge, r-edge)
    CENTER = [1.0, 0.7]  # r in [0.1, 1.3], spans the horizon r_S=0.5

    print("=" * 72)
    print("nachocausal DEV prototype smoke-test (exploration; NO verdict)")
    print(f"  dev_seed={DEV_SEED}  intensity={INTENSITY}  r_S(hidden)={R_S}")
    print(f"  box-matched cuboid edges={EDGES} center={CENTER}")
    print("=" * 72)

    # INTENTIONAL: BH and the control share DEV_SEED. Each generate() builds a
    # fresh default_rng(DEV_SEED) and the box/shape is identical, so the Poisson
    # count and coordinate draws are IDENTICAL for both -- the two causal sets
    # sit on the SAME point cloud and differ ONLY in causality. This is the
    # strongest possible box-match: it isolates horizon-truncation from the
    # luck of the sprinkle. (Validation will instead use a disjoint seed set.)
    for kind, label in (
        ("BH", "Schwarzschild EF (horizon present)"),
        ("MINK", "Minkowski control (box-matched, no horizon)"),
    ):
        print(f"\n[{kind}] {label}")
        C, N, embedding = generate(kind, DEV_SEED, INTENSITY, EDGES, CENTER, R_S)
        print(f"    Poisson-realised N = {N}")

        # ACCELERATOR: prove the vectorized poset reproduces Minz bit-for-bit
        # on these coordinates, then keep using Minz's C as the reference. (At
        # validation N this gate runs at small N; the fast path replaces Minz
        # only above the gated regime.)
        C_fast = past_matrix_fast(embedding, kind, R_S)
        verify_fast_matches_minz(C, C_fast, kind)

        # ESTIMATOR: poset only. We pass ONLY C. (embedding stays out of scope.)
        O_by_min, min_idx, _ = estimate_O(C)
        O_vals = list(O_by_min.values())
        print(f"    minimal elements (PastInf) = {len(min_idx)}")
        print(f"    histogram of O over minimal elements (BH may be bimodal):")
        histogram_O(O_vals)

        # GUARD (v): runnable proof that O is order-only (raises if not).
        verify_order_only(C, seed=DEV_SEED)

        # SCORER: dev-only reveal of hidden r vs O.
        dev_score_O_vs_r(O_by_min, embedding, R_S)

    print("\n[separation] estimate_O() received only the boolean poset matrix C;")
    print(
        "[separation] no coordinate array exists in its scope, and verify_order_only()"
    )
    print(
        "[separation] proved O is invariant under relabelling. Guard (v) honoured here."
    )


if __name__ == "__main__":
    smoke()
