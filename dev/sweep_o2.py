#!/usr/bin/env python
"""
nachocausal -- DEV SWEEP 2 (exploration only; Phase 0). NOT frozen, NO verdict.

Improvements over sweep_o.py (see dev/PHASE0_NOTES.md):
  * numpy Poisson-uniform sprinkle (2D EF: sqrt(-g)=1 => coordinate-uniform IS
    natural-volume, Glue 3). Bypasses Minz's O(N^2) relate() so we reach the
    dense ceiling N~2e4 in seconds instead of minutes.
  * fast==Minz gate kept ONCE per kind at small N on Minz-drawn coordinates.
  * significance is CONTROL-ANCHORED (decided 2026-06-18): for each (box,intensity)
    we compare each BLIND separation statistic of BH against the MINK ensemble over
    dev seeds, reporting z=(mean_BH-mean_MINK)/std_MINK. The frozen Hartigan-dip
    theta_sig is deferred to its own validated environment.
  * two timelike extents (paper Sec. III predicts a larger t-extent sharpens the jump).
DEV SCORING ONLY (split_acc, dr/M) reveals r AFTER the blind split, never before.
"""
from __future__ import annotations

import numpy as np

import prototype_o as P
from sweep_o import two_means_split
from causets.sprinkledcauset import SprinkledCauset
from causets.spacetimes import BlackHoleSpacetime, FlatSpacetime
from causets.shapes import CoordinateShape

DEV_SEEDS = [20240617, 13, 101, 7, 42, 99, 2718, 31415]  # dev only; disjoint from validation
INTENSITIES = [1500.0, 3000.0, 6000.0, 12000.0]
T_EDGES = [2.0, 6.0]      # timelike extents to compare
R_EDGE, R_CENTER = 1.2, 0.7
R_S = 0.5


def numpy_sprinkle(seed, intensity, t_edge):
    """Poisson(intensity) points uniform in the box; coordinate-uniform == natural
    volume for 2D EF (Glue 3). Returns (embedding, edges, center)."""
    edges = np.array([t_edge, R_EDGE], float)
    center = np.array([t_edge / 2.0, R_CENTER], float)     # t in [0,t_edge]
    rng = np.random.default_rng(seed)
    n = rng.poisson(intensity)
    low = center - edges / 2.0
    pts = low + rng.random((n, 2)) * edges
    return pts, edges, center


def gate_once(kind):
    """One fast==Minz cross-check per kind, on Minz-drawn coordinates at small N."""
    shape = CoordinateShape(2, "cuboid", edges=np.array([2.0, R_EDGE], float),
                            center=np.array([1.0, R_CENTER], float))
    st = BlackHoleSpacetime(2, r_S=R_S, metric="Eddington-Finkelstein") \
        if kind == "BH" else FlatSpacetime(2)
    rng = np.random.default_rng(20240617)
    C = SprinkledCauset(dim=2, spacetime=st, shape=shape)
    C.intensify(420.0, rng=rng, shape=shape)
    events = C.sortedByCausality()
    emb = np.array([e.Coordinates for e in events], float)
    Cm = C.PastMatrix(events, dtype=bool)
    Cf = P.past_matrix_fast(emb, kind, R_S)
    P.verify_fast_matches_minz(Cm, Cf, kind)


def blind_stats(O):
    """Two coordinate-free separation statistics on the multiset O."""
    o = np.sort(np.asarray(O, float))
    _, sep = two_means_split(o)                      # between/pooled
    if o.size < 2 or o[-1] == o[0]:
        return sep, float("nan")
    gaps = np.diff(o)
    gap_ratio = float(gaps.max() / ((o[-1] - o[0]) / (o.size - 1)))  # max gap / mean gap
    return sep, gap_ratio


def run():
    for k in ("BH", "MINK"):
        gate_once(k)
    hdr = (f"{'t_ext':>5} {'inten':>6} {'~N':>6} {'sep_BH':>6} {'z_sep':>6} "
           f"{'gapr_BH':>7} {'z_gap':>6} {'acc_BH':>6} {'drM_BH':>6}")
    print("=" * len(hdr))
    print("nachocausal DEV SWEEP 2 -- control-anchored bimodality (NO verdict)")
    print(f"r_edge={R_EDGE} r_center={R_CENTER} r_S={R_S} seeds={len(DEV_SEEDS)}")
    print("=" * len(hdr)); print(hdr)
    for t_edge in T_EDGES:
        for intensity in INTENSITIES:
            acc = {"BH": [], "MINK": []}
            sep = {"BH": [], "MINK": []}
            gapr = {"BH": [], "MINK": []}
            drM = {"BH": [], "MINK": []}
            Ns = []
            for seed in DEV_SEEDS:
                emb, edges, center = numpy_sprinkle(seed, intensity, t_edge)
                Ns.append(emb.shape[0])
                for kind in ("BH", "MINK"):
                    Cf = P.past_matrix_fast(emb, kind, R_S)
                    O_by_min, min_idx, _ = P.estimate_O(Cf)
                    s, g = blind_stats(list(O_by_min.values()))
                    sep[kind].append(s); gapr[kind].append(g)
                    # DEV SCORING: blind split threshold, then reveal r to check.
                    thr, _ = two_means_split(list(O_by_min.values()))
                    r = emb[:, 1]
                    truth = np.array([r[i] < R_S for i in min_idx])
                    pred = np.array([O_by_min[i] < thr for i in min_idx])
                    acc[kind].append(float(np.mean(pred == truth)) if len(min_idx) else np.nan)
                    rint = [r[i] for i in min_idx if r[i] < R_S]
                    rext = [r[i] for i in min_idx if r[i] >= R_S]
                    drM[kind].append(abs(min(rext) - max(rint)) / R_S
                                     if rint and rext else np.nan)

            mu_m_sep, sd_m_sep = np.nanmean(sep["MINK"]), np.nanstd(sep["MINK"]) or 1e-12
            mu_m_gap, sd_m_gap = np.nanmean(gapr["MINK"]), np.nanstd(gapr["MINK"]) or 1e-12
            z_sep = (np.nanmean(sep["BH"]) - mu_m_sep) / sd_m_sep
            z_gap = (np.nanmean(gapr["BH"]) - mu_m_gap) / sd_m_gap
            print(f"{t_edge:>5.1f} {intensity:>6.0f} {int(np.mean(Ns)):>6} "
                  f"{np.nanmean(sep['BH']):>6.2f} {z_sep:>6.1f} "
                  f"{np.nanmean(gapr['BH']):>7.2f} {z_gap:>6.1f} "
                  f"{np.nanmean(acc['BH']):>6.2f} {np.nanmean(drM['BH']):>6.3f}")
    print("-" * len(hdr))
    print("z = (mean_BH - mean_MINK)/std_MINK over dev seeds; large positive z = BH "
          "separation lies far outside the MINK control ensemble (blind, no r). "
          "acc_BH/drM_BH: DEV SCORING ONLY.")


if __name__ == "__main__":
    run()
