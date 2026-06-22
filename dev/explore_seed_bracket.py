"""dev exploration (PR-003 #3 + #2 in the regime that matters) — SEED fuzzy
ladders from the estimator-v2 BRACKET BOUNDARY (order-only) and ask:

  (a) does bracket-seeding actually yield NEAR-HORIZON ladders?  (it should:
      the boundary minimal elements straddle the true r_S, but we pick them
      ORDER ONLY via the volume 2-means split, never via coordinates)
  (b) does the order-only direction feature (#2) separate outgoing/ingoing
      THERE (the near-horizon band where #2 was previously untested / nan)?
  (c) do the bracket-seeded ladders sit close to r_S? (first look at d_perp =
      |r - R_S|, the eventual reconstruction-accuracy metric)

ORDER-ONLY seeding: classify the minimal elements by the v2 volume observable
2-means split; the BOUNDARY minimals are the highest-O of the low class and the
lowest-O of the high class. Start rungs originate at those. Coordinates enter
ONLY to score (truth direction + d_perp), never to seed/build/feature.

Run:  python3 dev/explore_seed_bracket.py
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import estimator, generator, thresholds  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402
import explore_ladders as XL  # noqa: E402
from explore_direction import greedy_ladder, order_only_heights, rel_field, auc  # noqa: E402

R_S = thresholds.R_S


def boundary_minimals(C, k_side=6):
    """ORDER-ONLY bracket boundary: 2-means split the volume observable on the
    minimal antichain; return the k_side highest-O low-class + k_side lowest-O
    high-class minimal elements (those straddling the blind threshold)."""
    O_by_min, min_idx = estimator.estimate_O_volume(C)
    mins = np.array(min_idx)
    O = np.array([O_by_min[i] for i in min_idx], float)
    thr, _ = estimator.two_means_split(list(O))
    low = mins[O < thr]
    low_O = O[O < thr]
    high = mins[O >= thr]
    high_O = O[O >= thr]
    if low.size == 0 or high.size == 0:
        return np.zeros(0, np.int64)
    lo_b = low[np.argsort(low_O)[-k_side:]]               # highest-O interior side
    hi_b = high[np.argsort(high_O)[:k_side]]              # lowest-O exterior side
    return np.concatenate([lo_b, hi_b]).astype(np.int64)


def collect(seed, intensity, t_edge, min_len=6, lmax=25):
    emb, _, _ = generator.numpy_sprinkle(seed, intensity, t_edge)
    C = generator.past_matrix_fast(emb, "BH")
    Lpast, Lfut = order_only_heights(C)
    rel_phi = rel_field(Lfut, Lpast)
    L, indptr, idx = XL.link_future_csr(C)
    bmin = boundary_minimals(C)
    rows = []
    for m in bmin:                                        # start rungs from boundary
        for t in range(indptr[m], indptr[m + 1]):         # links (m, child)
            q1 = idx[t]
            ln, pb = greedy_ladder(int(m), int(q1), indptr, idx, C, 3, lmax)
            if ln < min_len:
                continue
            p = pb[:ln]
            i = np.arange(ln, dtype=float)
            f_relphi_mean = float(rel_phi[p].mean())
            f_relphi_slope = float(np.polyfit(i, rel_phi[p], 1)[0])
            r = emb[p, 1]                                  # TRUTH (score only)
            rows.append((f_relphi_mean, f_relphi_slope,
                         np.sign(r[-1] - r[0]), float(r.mean()),
                         float(np.abs(r - R_S).mean()), ln))
    return rows


def run():
    print("PR-003 #3+#2: ladders SEEDED from the order-only v2 bracket boundary")
    print("(coords only score: truth direction + d_perp=|r-R_S|)\n")
    seeds = EXPLORE_POOL[:6]
    for t_edge, inten in [(12.0, 6000.0), (25.0, 12000.0)]:
        allrows = []
        for s in seeds:
            allrows += collect(s, inten, t_edge)
        if not allrows:
            print(f"t_edge={t_edge}: no ladders"); continue
        relm = np.array([r[0] for r in allrows])
        rels = np.array([r[1] for r in allrows])
        diru = np.array([r[2] for r in allrows])
        meanr = np.array([r[3] for r in allrows])
        dperp = np.array([r[4] for r in allrows])
        lens = np.array([r[5] for r in allrows])
        pos = diru > 0
        near = np.abs(meanr - R_S) < 0.15
        ell = thresholds.ell(inten)
        print(f"--- t_edge={t_edge:.0f} inten={inten:.0f} (ell={ell:.3f}) --- "
              f"ladders={len(allrows)} len(mean={lens.mean():.1f},max={lens.max()})")
        print(f"   near-horizon (|mean_r-R_S|<0.15): {int(near.sum())}/{len(allrows)} "
              f"= {near.mean():.0%}   (vs random-seed ~ low)")
        print(f"   d_perp=|r-R_S| over all bracket-seeded ladders: "
              f"median={np.median(dperp):.3f}  in ell units: {np.median(dperp)/ell:.1f}")
        print(f"   direction AUC  relphi_mean(all)={auc(relm,pos):.3f} "
              f"relphi_slope(all)={auc(rels,pos):.3f}")
        if near.sum() >= 4 and pos[near].sum() not in (0, near.sum()):
            print(f"   direction AUC near-horizon  relphi_mean={auc(relm[near],pos[near]):.3f} "
                  f"relphi_slope={auc(rels[near],pos[near]):.3f}  "
                  f"(out {int(pos[near].sum())}/in {int((~pos[near]).sum())})")
        else:
            print(f"   near-horizon AUC: still too few/imbalanced "
                  f"(out {int(pos[near].sum())}/in {int((~pos[near]).sum())})")
        print()


if __name__ == "__main__":
    run()
