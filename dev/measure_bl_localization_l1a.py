"""dev/ exploration — L₁a empirical probe for the BL-localization null-law program.

DEV-PHASE, EXPLORATION ONLY. Runs on flat Minkowski (the NULL hypothesis) sprinklings
over DEV_SEEDS only. NEVER imports/evaluates VALIDATION_SEEDS. Does NOT modify the sealed
estimator or any frozen threshold; reads only nachocausal.generator primitives + numpy.
Writes nothing under nachocausal/, docs/, or results/. Companion note:
dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md §9 (this is the §9.5 decisive probe).

What it measures (decides the §9.4 conditional-locality conjecture, Lectura A vs B):
  (1) Var Φ_link(ℓ_bulk) vs N         — §9.2 scaling claim Var ~ √N.
  (2) add-one cost D_{x'}Φ_link        — §9.3 mean / tail (sampled removals).
  (3) height-shift sparsity            — THE decisive quantity: #{z : s(z) changes when
      x' is removed}. O(1)/polylog ⇒ Lectura B (L₁ → toward CONFIRMED);
      growing like N^{1/3} ⇒ Lectura A (L₁ → reverts to IMPOSSIBLE).
Reporting is symmetric: A or B is documented as found.

Definitions (order-only; coords used only to sprinkle the flat null + benchmark scaling):
  Pred[i,j] = (j ≺ i)         from generator.past_matrix_fast(..., "MINK")
  s(i)  = longest chain to i (height), DP over the t-linear extension
  link j⋖i  ⇔  Pred[i,j] and no k with j≺k≺i        (transitive reduction)
  Φ(ℓ) = #{ links j⋖i : s(j) ≤ ℓ < s(i) }            (covering-link flux, §9.1)
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nachocausal import generator, thresholds  # noqa: E402

thresholds.assert_environment()  # RAISES unless numpy == sealed 1.26.4

DEV_SEEDS = thresholds.DEV_SEEDS
assert set(DEV_SEEDS).isdisjoint(thresholds.VALIDATION_SEEDS), "dev/validation seed leak"


def heights(Pred: np.ndarray, t: np.ndarray, active: np.ndarray | None = None) -> np.ndarray:
    """Longest-chain height s. s[i] = -1 for inactive, 0 for active minimal."""
    N = Pred.shape[0]
    if active is None:
        active = np.ones(N, bool)
    s = np.full(N, -1, np.int64)
    for i in np.argsort(t, kind="stable"):
        if not active[i]:
            continue
        pr = Pred[i] & active
        s[i] = (1 + int(s[pr].max())) if pr.any() else 0
    return s


def link_mask(Pred: np.ndarray) -> np.ndarray:
    """Transitive reduction: link_mask[i,j] iff j⋖i (covering link j ≺ i)."""
    P = Pred.astype(np.int32)
    Pred2 = (P @ P) > 0  # exists k with j≺k≺i
    return Pred & ~Pred2


def flux(linkm: np.ndarray, s: np.ndarray, ell: int) -> int:
    """Φ(ℓ): covering links crossing level ℓ (lower endpoint ≤ ℓ < upper)."""
    sj = s[None, :]  # lower endpoint j (columns)
    si = s[:, None]  # upper endpoint i (rows)
    return int((linkm & (sj <= ell) & (sj >= 0) & (si > ell)).sum())


def bulk_level(s: np.ndarray) -> int:
    act = s[s >= 0]
    return int(np.median(act))


def run(intensities=(200, 400, 800, 1600), n_removals=40, link_cap=900, smoke=False):
    if smoke:
        intensities, n_removals, link_cap = (200, 400), 12, 900
    print(f"# BL-localization L₁a probe | numpy {np.__version__} | seeds {DEV_SEEDS}")
    print(f"# t0={time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
    print("# col: intensity meanN  E[Φ]  Var[Φ]  Var/sqrtN  | "
          "mean|DΦ|  max|DΦ|  frac(DΦ≠0)  #contrib=frac*N  #contrib/sqrtN")
    for lam in intensities:
        fluxes, Ns = [], []
        shift_means, dphi_means, dphi_maxes, frac_nz = [], [], [], []
        for seed in DEV_SEEDS:
            emb, edges, center = generator.numpy_sprinkle(seed, float(lam))
            generator.assert_coordinate_uniform(emb, edges, center)
            N = emb.shape[0]
            Ns.append(N)
            t = emb[:, 0]
            Pred = generator.past_matrix_fast(emb, "MINK")
            s = heights(Pred, t)
            ell = bulk_level(s)
            linkm = link_mask(Pred)
            phi_full = flux(linkm, s, ell)
            fluxes.append(phi_full)

            # (3) decisive: height-shift sparsity + (2) add-one cost, sampled removals
            rng = np.random.default_rng(seed ^ 0x5F3759DF)
            cand = np.where(s >= 0)[0]
            sample = rng.choice(cand, size=min(n_removals, cand.size), replace=False)
            n_shift, dphi = [], []
            do_links = N <= link_cap
            for xp in sample:
                act = np.ones(N, bool)
                act[xp] = False
                s2 = heights(Pred, t, act)
                changed = (s2 != s) & act & (s >= 0)
                n_shift.append(int(changed.sum()))
                if do_links:
                    # links incident to xp are gone; recompute on sub-poset
                    sub = np.where(act)[0]
                    Psub = Pred[np.ix_(sub, sub)]
                    lm2 = link_mask(Psub)
                    phi2 = flux(lm2, s2[sub], ell)
                    dphi.append(abs(phi_full - phi2))
            shift_means.append(np.mean(n_shift))
            if dphi:
                dphi_means.append(np.mean(dphi))
                dphi_maxes.append(np.max(dphi))
                frac_nz.append(np.mean(np.asarray(dphi) > 0))
        meanN = float(np.mean(Ns))
        EPhi = float(np.mean(fluxes))
        VPhi = float(np.var(fluxes, ddof=1))
        fr = float(np.mean(frac_nz)) if frac_nz else float("nan")
        ncontrib = fr * meanN
        print(f"{lam:7d} {meanN:7.1f} {EPhi:7.2f} {VPhi:8.2f} {VPhi/np.sqrt(meanN):9.3f}  | "
              f"{(np.mean(dphi_means) if dphi_means else float('nan')):8.3f} "
              f"{(np.max(dphi_maxes) if dphi_maxes else float('nan')):8.1f} "
              f"{fr:10.3f} {ncontrib:14.1f} {ncontrib/np.sqrt(meanN):14.3f}")
    print(f"# t1={time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
    print("# READ (the rate hinges on #contrib scaling, with Var~sqrtN measured separately):")
    print("#   #contrib/sqrtN ~ const  ⇒ contributors ~ sqrtN (membrane) ⇒ rate ~ N^-1/4 → 0  (Lectura B, L₁→CONFIRMED path)")
    print("#   #contrib/sqrtN ~ sqrtN  ⇒ contributors ~ N (bulk)        ⇒ rate ~ O(1)        (inconclusive / Lectura A risk)")


if __name__ == "__main__":
    run(smoke="--smoke" in sys.argv)
