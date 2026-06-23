#!/usr/bin/env python
"""
nachocausal -- DEV SWEEP (exploration only; Phase 0 of docs/roadmap.md).
NOT frozen, NOT a result, sets NO thresholds.

Goal: measure on dev WHERE the bimodality of O (longest timelike chain from each
minimal element) is robust across N (intensity) and seed, for BH vs the
box-matched Minkowski control. This produces the N / ensemble figure that
docs/reuse_check.md:39-40 still marks [UNVERIFIED].

Method (faithful to docs/reuse_check.md):
  * coordinates come from Minz Poisson sprinkling (fast);
  * the poset uses our gated accelerator past_matrix_fast, with the
    fast==Minz gate (verify_fast_matches_minz) kept at the SMALLEST intensity of
    each (kind,seed) -- the accelerator replaces Minz only above the gated
    regime;
  * the estimator sees ONLY the poset (estimate_O);
  * bimodality is scored coordinate-free (bimodality coefficient + a 1-D 2-means
    split). Ground-truth r is revealed AFTERWARDS only to check the split, never
    to choose it (guard: ground truth only scores). The frozen significance test
    will be Hartigan's dip (preregistration.md:52); this dev proxy is pure-numpy.
"""
from __future__ import annotations

import numpy as np

import prototype_o as P  # dev sibling; provides accelerator + estimator + glue
from causets.sprinkledcauset import SprinkledCauset
from causets.spacetimes import BlackHoleSpacetime, FlatSpacetime
from causets.shapes import CoordinateShape

# DEV seeds: documented, DISJOINT from any future validation seed set.
DEV_SEEDS = [20240617, 13, 101]
INTENSITIES = [420.0, 1500.0, 3000.0, 6000.0]
EDGES = [2.0, 1.2]      # (t, r); box-matched BH/MINK (smoke default)
CENTER = [1.0, 0.7]     # r in [0.1, 1.3], spans r_S
R_S = 0.5               # HIDDEN from estimator


def _sprinkle_coords(kind, seed, intensity):
    shape = CoordinateShape(2, "cuboid",
                            edges=np.array(EDGES, float),
                            center=np.array(CENTER, float))
    st = BlackHoleSpacetime(2, r_S=R_S, metric="Eddington-Finkelstein") \
        if kind == "BH" else FlatSpacetime(2)
    rng = np.random.default_rng(seed)
    C = SprinkledCauset(dim=2, spacetime=st, shape=shape)
    C.intensify(intensity, rng=rng, shape=shape)
    events = C.sortedByCausality()
    embedding = np.array([e.Coordinates for e in events], dtype=float)
    return C, events, embedding


def bimodality_coefficient(x):
    """Pure-numpy BC = (g^2 + 1) / k, g=skew, k=kurtosis (Pearson, with the
    sample correction term). BC > 5/9 ~ 0.555 is the uniform-threshold heuristic
    for bimodality. DEV proxy only; the frozen test is Hartigan's dip."""
    x = np.asarray(x, float)
    n = x.size
    if n < 4 or np.allclose(x, x[0]):
        return float("nan")
    m = x.mean(); s = x.std()
    if s == 0:
        return float("nan")
    g = np.mean(((x - m) / s) ** 3)
    k = np.mean(((x - m) / s) ** 4)
    bc_corr = (g ** 2 + 1.0) / (k + 3.0 * (n - 1) ** 2 / ((n - 2) * (n - 3)))
    return float(bc_corr)


def two_means_split(O):
    """1-D 2-means on sorted O: pick the gap that minimises within-cluster SSE.
    Coordinate-free. Returns (threshold, sep) where sep = |mu_hi-mu_lo|/pooled_sd."""
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
    pooled = np.sqrt((lo.var() * lo.size + hi.var() * hi.size) / n) or 1e-12
    sep = abs(hi.mean() - lo.mean()) / pooled
    return float(thr), float(sep)


def run():
    ell = lambda N: (N / (EDGES[0] * EDGES[1])) ** -0.5  # rho^-1/2, 2D scale
    hdr = f"{'kind':>4} {'seed':>9} {'N':>6} {'|min|':>5} {'BC':>6} " \
          f"{'2m_sep':>7} {'thr':>6} {'split_acc':>9} {'dr/M':>7}"
    print("=" * len(hdr))
    print("nachocausal DEV SWEEP -- bimodality of O vs N/seed (NO verdict)")
    print(f"box edges={EDGES} center={CENTER} r_S(hidden)={R_S}")
    print("=" * len(hdr))
    print(hdr)
    for kind in ("BH", "MINK"):
        for seed in DEV_SEEDS:
            for j, intensity in enumerate(INTENSITIES):
                C, events, emb = _sprinkle_coords(kind, seed, intensity)
                Cf = P.past_matrix_fast(emb, kind, R_S)
                if j == 0:  # keep the fast==Minz gate at smallest N per (kind,seed)
                    Cm = C.PastMatrix(events, dtype=bool)
                    P.verify_fast_matches_minz(Cm, Cf, kind)
                O_by_min, min_idx, _ = P.estimate_O(Cf)
                O = list(O_by_min.values())
                N = Cf.shape[0]
                bc = bimodality_coefficient(O)
                thr, sep = two_means_split(O)
                # DEV SCORING ONLY: reveal r to check the coordinate-free split.
                r = emb[:, 1]
                truth_int = np.array([r[i] < R_S for i in min_idx])  # interior?
                pred_int = np.array([O_by_min[i] < thr for i in min_idx])
                acc = float(np.mean(pred_int == truth_int)) if len(min_idx) else float("nan")
                # boundary localisation: r of the lowest exterior vs highest interior
                rint = [r[i] for i in min_idx if r[i] < R_S]
                rext = [r[i] for i in min_idx if r[i] >= R_S]
                dr = (min(rext) - max(rint)) if rint and rext else float("nan")
                dr_over_M = abs(dr) / (R_S) if dr == dr else float("nan")  # 2M=r_S here
                print(f"{kind:>4} {seed:>9} {N:>6} {len(min_idx):>5} "
                      f"{bc:>6.3f} {sep:>7.2f} {thr:>6.1f} {acc:>9.2f} {dr_over_M:>7.3f}")
    print("-" * len(hdr))
    print("BC>0.555 ~ bimodal (dev proxy). split_acc/dr per (kind,seed,N): DEV "
          "SCORING ONLY -- r revealed after the coordinate-free split, never before.")


if __name__ == "__main__":
    run()
