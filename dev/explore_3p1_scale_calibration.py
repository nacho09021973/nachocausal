"""EXPLORATION (dev/) — Paper II, Phase I: 3+1 discrete scale calibration.

NOT on the validation path. This file does NOT import, touch, or re-seal
`nachocausal/` (the frozen 1+1D generator stays exactly as it is: it is 2D by
construction and its Glue-3 argument -- coordinate-uniform == natural-volume
because det g = -1 in 2D EF -- does not port to 3+1).

Scope of this script (deliberately narrow):

  Phase I only. 3+1 MINKOWSKI, no excision, no black hole. It measures whether
  the two order-only future observables on a finite patch obey the expected
  density scaling

      V(i) = |J^+(i) cap D|        ~  rho
      L(i) = longest future chain  ~  rho^{1/4}

  and therefore whether the dimensionless ratio R(i) = L(i)^4 / V(i)
  stabilises in rho at FIXED continuum region.

  R is a SHAPE functional of the truncated future, not a universal constant:
  Brightwell-Gregory's L (rho V)^{-1/d} -> m_d holds for an ALEXANDROV INTERVAL,
  and a truncated future in a box is not an interval. See the notes file
  dev/PAPER3_3P1_SCALE_NOTES.md.

Order-only discipline: V, L, R and the minimal-element probe set are computed
from the causal matrix alone. The embedding is used ONLY to build the poset and
is never read by any observable.

Convention note: unlike nachocausal/generator.py (which stores a PAST matrix),
this file stores a FUTURE matrix, C[i, j] == True iff i precedes j.

Run:  python3 dev/explore_3p1_scale_calibration.py
"""

from __future__ import annotations

import json
import sys
from typing import Dict, List, Tuple

import numpy as np

# Fixed continuum region for the whole sweep: the box is NEVER changed with rho.
T_EDGE = 1.0
X_EDGE = 1.0
BOX_VOLUME = T_EDGE * X_EDGE**3

RHO_SWEEP = (500.0, 1000.0, 2000.0, 4000.0, 8000.0)
SEEDS = (11, 12, 13)


# ---------------------------------------------------------------------------
# Generator (3+1 Minkowski). Uniform in the box == natural volume, since
# sqrt(-g) = 1 in inertial coordinates. This is the ONLY geometry for which the
# coordinate-uniform shortcut is legitimate in 3+1.
# ---------------------------------------------------------------------------
def sprinkle_minkowski_4d(seed: int, rho: float) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = rng.poisson(rho * BOX_VOLUME)
    pts = rng.random((n, 4))
    pts[:, 0] *= T_EDGE
    pts[:, 1:] *= X_EDGE
    return pts


def future_matrix_minkowski(pts: np.ndarray, block: int = 1024) -> np.ndarray:
    """C[i, j] = True iff i strictly precedes j: dt > 0 and dt >= |dx|."""
    n = pts.shape[0]
    t = pts[:, 0]
    x = pts[:, 1:]
    C = np.zeros((n, n), dtype=bool)
    for a in range(0, n, block):
        b = min(a + block, n)
        dt = t[None, :] - t[a:b, None]
        d2 = np.sum((x[None, :, :] - x[a:b, None, :]) ** 2, axis=2)
        C[a:b] = (dt > 0.0) & (dt * dt >= d2)
    np.fill_diagonal(C, False)
    return C


# ---------------------------------------------------------------------------
# Order-only observables.
# ---------------------------------------------------------------------------
def future_cardinality(C: np.ndarray) -> np.ndarray:
    """V(i) = |J^+(i)|. Valid as a row sum because the Minkowski causal
    relation is already transitive (no transitive closure needed)."""
    return C.sum(axis=1).astype(np.int64)


def longest_future_chain(C: np.ndarray, order: np.ndarray) -> np.ndarray:
    """L(i) = number of RELATIONS in the longest chain starting at i
    (so L = 0 for a maximal element). `order` must be a linear extension."""
    n = C.shape[0]
    L = np.zeros(n, dtype=np.int64)
    for i in order[::-1]:
        row = C[i]
        if row.any():
            L[i] = 1 + int(L[row].max())
    return L


def minimal_elements(C: np.ndarray) -> np.ndarray:
    """Order-only: i is minimal iff no element precedes it (empty column)."""
    return ~C.any(axis=0)


# ---------------------------------------------------------------------------
# Sweep.
# ---------------------------------------------------------------------------
def measure(seed: int, rho: float) -> Dict[str, float]:
    pts = sprinkle_minkowski_4d(seed, rho)
    n = pts.shape[0]
    lin_ext = np.argsort(pts[:, 0], kind="stable")  # embedding used ONLY here
    C = future_matrix_minkowski(pts)
    V = future_cardinality(C)
    L = longest_future_chain(C, lin_ext)
    mins = minimal_elements(C)

    live = V > 0  # R is undefined on maximal elements
    R = np.full(n, np.nan)
    R[live] = (L[live].astype(float) ** 4) / V[live]

    out = {
        "seed": seed,
        "rho": rho,
        "N": int(n),
        "n_minimal": int(mins.sum()),
        "mean_V_all": float(V.mean()),
        "mean_L_all": float(L.mean()),
        "mean_V_min": float(V[mins].mean()),
        "mean_L_min": float(L[mins].mean()),
        "median_R_all": float(np.nanmedian(R)),
        "median_R_min": float(np.nanmedian(R[mins])),
        "max_L": int(L.max()),
    }
    # Cross-sectional slope WITHIN one realisation (this is NOT the scaling
    # test: it mixes future-shapes at fixed rho, and is reported precisely to
    # show that it does not equal 1/4).
    sel = live & (L > 0)
    if sel.sum() > 10:
        s = np.polyfit(np.log(V[sel]), np.log(L[sel].astype(float)), 1)[0]
        out["cross_sectional_slope"] = float(s)
    return out


def loglog_slope(xs: List[float], ys: List[float]) -> float:
    return float(np.polyfit(np.log(xs), np.log(ys), 1)[0])


def main() -> int:
    rows: List[Dict[str, float]] = []
    for rho in RHO_SWEEP:
        for seed in SEEDS:
            r = measure(seed, rho)
            rows.append(r)
            print(
                f"rho={rho:7.0f} seed={seed} N={r['N']:5d} "
                f"<V>={r['mean_V_all']:9.2f} <L>={r['mean_L_all']:6.3f} "
                f"med R_all={r['median_R_all']:7.3f} "
                f"med R_min={r['median_R_min']:7.3f} "
                f"xsec={r.get('cross_sectional_slope', float('nan')):.3f}",
                flush=True,
            )

    print("\n--- Phase I scaling test (means across the rho sweep) ---")
    agg: Dict[float, Tuple[float, float, float, float]] = {}
    for rho in RHO_SWEEP:
        sub = [r for r in rows if r["rho"] == rho]
        agg[rho] = (
            float(np.mean([r["mean_V_all"] for r in sub])),
            float(np.mean([r["mean_L_all"] for r in sub])),
            float(np.mean([r["mean_V_min"] for r in sub])),
            float(np.mean([r["mean_L_min"] for r in sub])),
        )
    rhos = list(RHO_SWEEP)
    V_all = [agg[r][0] for r in rhos]
    L_all = [agg[r][1] for r in rhos]
    V_min = [agg[r][2] for r in rhos]
    L_min = [agg[r][3] for r in rhos]

    print(f"d log <V>_all / d log rho = {loglog_slope(rhos, V_all):.4f}   (expect 1)")
    print(f"d log <L>_all / d log rho = {loglog_slope(rhos, L_all):.4f}   (expect 1/4)")
    print(f"d log <L>_all / d log <V>_all = {loglog_slope(V_all, L_all):.4f}  (expect 1/4)")
    print(f"d log <V>_min / d log rho = {loglog_slope(rhos, V_min):.4f}   (expect 1)")
    print(f"d log <L>_min / d log rho = {loglog_slope(rhos, L_min):.4f}   (expect 1/4)")
    print(f"d log <L>_min / d log <V>_min = {loglog_slope(V_min, L_min):.4f}  (expect 1/4)")

    with open("dev/explore_3p1_scale_calibration_results.json", "w") as fh:
        json.dump(
            {
                "box": {"T_EDGE": T_EDGE, "X_EDGE": X_EDGE, "volume": BOX_VOLUME},
                "rho_sweep": list(RHO_SWEEP),
                "seeds": list(SEEDS),
                "rows": rows,
                "slopes": {
                    "logV_all_vs_logrho": loglog_slope(rhos, V_all),
                    "logL_all_vs_logrho": loglog_slope(rhos, L_all),
                    "logL_vs_logV_all": loglog_slope(V_all, L_all),
                    "logV_min_vs_logrho": loglog_slope(rhos, V_min),
                    "logL_min_vs_logrho": loglog_slope(rhos, L_min),
                    "logL_vs_logV_min": loglog_slope(V_min, L_min),
                },
            },
            fh,
            indent=2,
        )
    print("\nwrote dev/explore_3p1_scale_calibration_results.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
