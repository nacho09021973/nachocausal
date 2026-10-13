"""scorer — reveals r to MEASURE where the blind 2+1 boundary fell. Never feeds back.

Same bracket as the sealed 1+1 scorer (nachocausal/scoring/scorer.py), with 2M from the 2+1
thresholds: r_lo = max r over low-O minimal elements, r_hi = min r over high-O ones.
valid: both classes non-empty; clean: width >= 0; covers: r_lo <= 2M <= r_hi.
"""

from __future__ import annotations

from typing import Dict, List

import numpy as np

from .. import thresholds


def blind_bracket(O_by_min: Dict[int, int], min_idx: List[int], thr: float,
                  r: np.ndarray) -> dict:
    lo_r = [float(r[i]) for i in min_idx if O_by_min[i] < thr]
    hi_r = [float(r[i]) for i in min_idx if O_by_min[i] >= thr]
    if not lo_r or not hi_r:
        return dict(valid=False, r_lo=float("nan"), r_hi=float("nan"), width=float("nan"),
                    midpoint=float("nan"), covers=False, clean=False)
    r_lo, r_hi = max(lo_r), min(hi_r)
    width = r_hi - r_lo
    return dict(valid=True, r_lo=r_lo, r_hi=r_hi, width=width, midpoint=0.5 * (r_lo + r_hi),
                covers=bool(r_lo <= thresholds.TWO_M <= r_hi), clean=bool(width >= 0.0))
