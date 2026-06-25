"""dev exploration — richer order-only observables to lift localisation COVERAGE.

NOT sealed (dev/, untracked). DEV_SEEDS only; never imports/evaluates
VALIDATION_SEEDS. Does NOT modify the sealed estimator or any threshold. It only
*reads* the sealed generator/estimator/two_means_split to stay apples-to-apples
with the frozen baseline.

Question (post-#5 FAIL, axis (ii) coverage): the sealed observable O is future
HEIGHT (longest future chain from each minimal element) — an EXTREME statistic,
brittle near the boundary. Do smoother order-only observables separate minimal
elements by true r more cleanly, lifting coverage?

For each observable we report, per intensity, averaged over DEV_SEEDS (BH only):
  * cov   : faithful coverage = the scorer's bracket covers R_S
            (two_means_split -> r_lo=max r interior-pred, r_hi=min r exterior-pred,
             covers = r_lo <= R_S <= r_hi)  -- this IS check (ii) coverage.
  * sep'able: does ANY threshold on O perfectly bracket R_S among minimals
            (max O over r<R_S  <  min O over r>=R_S)?  Decouples "observable is
            r-monotone enough" (sep'able) from "2-means gap sits at the horizon"
            (cov). cov<=sep'able always; a big gap means the SPLIT is the problem,
            not the observable.
  * |rho| : |Spearman(O, r)| over minimals — threshold-free monotone separation.
  * width : median bracket width / 2M (must not blow up while fixing coverage).

Run (sealed venv ok):  .venv/bin/python dev/explore_observable.py
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import estimator, generator, thresholds  # noqa: E402

R_S = thresholds.R_S
TWO_M = thresholds.TWO_M
SEEDS = thresholds.DEV_SEEDS
INTENS = thresholds.INTENSITIES


# ----- order-only observables on minimal elements (from C alone) -------------
def _minimal_mask(C: np.ndarray) -> np.ndarray:
    return ~C.any(axis=1)  # rows with no past


def obs_height(C, minimal):
    """Sealed baseline: longest future chain length (estimator.estimate_O)."""
    O_by_min, min_idx, _ = estimator.estimate_O(C)
    idx = np.flatnonzero(minimal)
    return np.array([O_by_min[i] for i in idx], float)


def obs_volume(C, minimal):
    """|future(i)| = number of elements with i in their past. Column sum of C.
    Smoother (integrated) than height -> hypothesis: less brittle near boundary."""
    return C.sum(axis=0)[minimal].astype(float)


def obs_volheight2(C, minimal):
    """volume / height^2 : a 2D dimension/anomaly proxy. In a 2D causal diamond
    volume ~ height^2; truncation inside the horizon distorts the ratio."""
    h = obs_height(C, minimal)
    v = obs_volume(C, minimal)
    return v / np.maximum(h, 1.0) ** 2


OBSERVABLES = {
    "height (sealed)": obs_height,
    "volume": obs_volume,
    "vol/height^2": obs_volheight2,
}


# ----- metrics (mirror scorer.py exactly for the faithful coverage) ----------
def faithful_cover_width(O_vals, r_min):
    thr, _ = estimator.two_means_split(O_vals)
    if not np.isfinite(thr):
        return None
    lo = r_min[O_vals < thr]   # predicted interior
    hi = r_min[O_vals >= thr]  # predicted exterior
    if lo.size == 0 or hi.size == 0:
        return None
    r_lo, r_hi = float(lo.max()), float(hi.min())
    covers = (r_lo <= R_S <= r_hi)
    return covers, (r_hi - r_lo) / TWO_M


def separable(O_vals, r_min):
    interior = r_min < R_S
    if interior.all() or (~interior).all():
        return None
    return float(O_vals[interior].max()) < float(O_vals[~interior].min())


def spearman_abs(O_vals, r_min):
    if O_vals.size < 3:
        return float("nan")
    ro = np.argsort(np.argsort(O_vals)).astype(float)
    rr = np.argsort(np.argsort(r_min)).astype(float)
    c = np.corrcoef(ro, rr)[0, 1]
    return abs(float(c))


def run():
    print(f"DEV_SEEDS={SEEDS}  R_S={R_S}  (BH only; coverage axis)\n")
    header = f"{'observable':<16}{'inten':>7}{'cov':>7}{'sep`able':>9}{'|rho|':>7}{'medW/2M':>9}"
    for inten in INTENS:
        # build each BH causet once, reuse across observables
        per_seed = []
        for s in SEEDS:
            emb, edges, center = generator.numpy_sprinkle(s, inten)
            C = generator.past_matrix_fast(emb, "BH")
            minimal = _minimal_mask(C)
            r_min = emb[minimal, 1]
            per_seed.append((C, minimal, r_min))
        print(header)
        for name, fn in OBSERVABLES.items():
            covs, seps, rhos, widths = [], [], [], []
            for C, minimal, r_min in per_seed:
                O_vals = fn(C, minimal)
                cw = faithful_cover_width(O_vals, r_min)
                if cw is not None:
                    covs.append(cw[0]); widths.append(cw[1])
                sp = separable(O_vals, r_min)
                if sp is not None:
                    seps.append(sp)
                rhos.append(spearman_abs(O_vals, r_min))
            mc = np.mean(covs) if covs else float("nan")
            ms = np.mean(seps) if seps else float("nan")
            mr = np.nanmean(rhos)
            mw = np.median(widths) if widths else float("nan")
            print(f"{name:<16}{inten:>7.0f}{mc:>7.2f}{ms:>9.2f}{mr:>7.2f}{mw:>9.3f}")
        print()


if __name__ == "__main__":
    run()
