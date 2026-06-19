"""scorer — reveals r to MEASURE where the blind boundary fell. Never feeds back.

The blind split (threshold `thr` from O alone) partitions the minimal elements
into a low-O (interior-candidate) class and a high-O (exterior-candidate) class.
Revealing r, we form an order-statistic BRACKET [r_lo, r_hi]:

    r_lo = max r over low-O (predicted-interior) minimal elements
    r_hi = min r over high-O (predicted-exterior) minimal elements

This binning-free bracket localises the hidden horizon: a clean split has
r_lo <= r_S <= r_hi, and the bracket WIDTH (r_hi - r_lo) shrinks toward the
discreteness floor ell as density grows. Misclassification (r_lo > r_hi) marks
the seed impure. This realises success criterion (ii) and the reframed
discreteness-floor convergence claim (see addendum).
"""

from __future__ import annotations

from typing import Dict, List

import numpy as np

from .. import thresholds


def blind_bracket(
    O_by_min: Dict[int, int],
    min_idx: List[int],
    thr: float,
    embedding: np.ndarray,
) -> dict:
    """Score a single causet's blind split against the revealed r.

    Args:
      O_by_min, min_idx: estimator output (order-only).
      thr: the blind boundary threshold, FROZEN from O before this call.
      embedding: hidden coordinates (t, r) — revealed here only.

    Returns a dict with:
      valid    : both classes non-empty (else no two-class split -> inconclusive)
      r_lo,r_hi: bracket edges (NaN if invalid)
      width    : r_hi - r_lo (may be < 0 under misclassification)
      midpoint : boundary r-location 0.5*(r_lo+r_hi) (NaN if invalid)
      covers   : r_lo <= r_S <= r_hi
      clean    : valid and width >= 0
    """
    r = embedding[:, 1]
    lo_r = [r[i] for i in min_idx if O_by_min[i] < thr]   # predicted interior
    hi_r = [r[i] for i in min_idx if O_by_min[i] >= thr]  # predicted exterior
    if not lo_r or not hi_r:
        return dict(valid=False, r_lo=np.nan, r_hi=np.nan, width=np.nan,
                    midpoint=np.nan, covers=False, clean=False)
    r_lo = float(max(lo_r))
    r_hi = float(min(hi_r))
    width = r_hi - r_lo
    covers = (r_lo <= thresholds.R_S <= r_hi)
    return dict(valid=True, r_lo=r_lo, r_hi=r_hi, width=width,
                midpoint=0.5 * (r_lo + r_hi), covers=covers, clean=(width >= 0.0))
