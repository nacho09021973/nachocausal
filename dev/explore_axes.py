"""dev exploration — estimator-v2 stability on the PATCH-EXTENT and
DENSITY/RESOLUTION axes (prerequisite #1 toward prereg-002, continued).
Committee framing 2026-06-22.

Finding 3 (dev/explore_stability.py) closed the SEED axis. This adds the two
remaining stability axes the committee named, with one geometric subtlety made
explicit:

  In this FIXED-box generator (box = [t_edge, R_EDGE], area = t_edge*R_EDGE,
  intensity = expected #points), "density rho" and "resolution at fixed physical
  area" are the SAME knob: raising intensity at a fixed box raises rho AND
  shrinks the discreteness scale ell ~ 1/sqrt(rho). So:

  * DENSITY / RESOLUTION axis = intensity sweep at the FIXED box (t_edge=6). We
    EXTEND Finding 3's 3000/6000/12000 with 1500 and 24000 to see the trend and
    where coverage breaks.
  * PATCH-EXTENT axis = vary the box size at MATCHED density, to isolate extent
    from density. Only t_edge is a cleanly-exposed sprinkle parameter (R_EDGE /
    R_CENTER are frozen thresholds, left untouched). Holding rho constant means
    intensity = rho0 * t_edge * R_EDGE; with intensity = 1000 * t_edge this gives
    a constant rho0 = 1000 / R_EDGE = 833.3 pts/area across t_edge in {3,6,12}.

Same gated pipeline, same 40 EXPLORE_POOL replicate seeds, BH only. The gate,
observable, and null are imported verbatim from explore_fp_gated.py and the
across-seed metric from explore_stability.py, so this cannot drift. Nothing
sealed is touched; the reserved prereg-002 band is never evaluated.

Run:  python3 dev/explore_axes.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import generator, estimator, thresholds  # noqa: E402
from nachocausal.scoring import blind_bracket  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402
from explore_fp_gated import (  # noqa: E402
    improvement, minimal_volume, build_tau_table, ALPHA, NULL_MC_SEED,
    NULL_MC_REPS,
)
from explore_stability import stability  # noqa: E402  (across-seed metric)

POOL = EXPLORE_POOL
R_EDGE = thresholds.R_EDGE          # 1.2 (frozen patch width in r; not varied)
R_S = thresholds.R_S               # 0.5


def collect_bh(inten, t_edge):
    """Per seed (BH only) at a given intensity AND box height t_edge."""
    rows = []
    for s in POOL:
        emb, _, _ = generator.numpy_sprinkle(s, inten, t_edge)
        C = generator.past_matrix_fast(emb, "BH")
        Ob, mi = minimal_volume(C)
        vals = [Ob[i] for i in mi]
        thr, sep = estimator.two_means_split(vals)
        br = blind_bracket(Ob, mi, thr, emb)
        rows.append((len(mi), improvement(vals), sep, br))
    return rows


def report(rows, tau, label):
    m = stability(rows, tau)
    ns = [r[0] for r in rows]
    print(f"  {label:<22} n[{min(ns):>3},{max(ns):>3}]  "
          f"abst={m['abst']:>2}/{m['n_seeds']}  cov={m['cov']:.2f}  "
          f"mid={m['mid_mean']:.4f}+-{m['mid_std']:.4f} "
          f"bias={m['mid_bias']:+.4f}  w/2M={m['w_med']:.3f}+-{m['w_std']:.3f}",
          flush=True)


def run_patch():
    print("=== PATCH-EXTENT axis: vary t_edge at MATCHED density "
          "(intensity = 1000 * t_edge) ===", flush=True)
    cells = [(3, 3000), (6, 6000), (12, 12000)]   # (t_edge, intensity)
    rho0 = 3000 / (3 * R_EDGE)
    print(f"  matched rho0 = {rho0:.1f} pts/area; box r in "
          f"[{thresholds.R_CENTER - R_EDGE/2:.1f},{thresholds.R_CENTER + R_EDGE/2:.1f}] "
          f"(R_S={R_S})", flush=True)
    allrows = {te: collect_bh(I, te) for te, I in cells}
    tau = build_tau_table([r[0] for te in allrows for r in allrows[te]])
    for te, I in cells:
        report(allrows[te], tau, f"t_edge={te:<2} (I={I})")
    print(flush=True)


def run_density():
    print("=== DENSITY/RESOLUTION axis: vary intensity at FIXED box "
          f"(t_edge={thresholds.T_EDGE:.0f}); 1500/24000 EXTEND Finding 3 ===",
          flush=True)
    intens = [1500, 3000, 6000, 12000, 24000]
    te = thresholds.T_EDGE
    allrows = {I: collect_bh(I, te) for I in intens}
    tau = build_tau_table([r[0] for I in allrows for r in allrows[I]])
    for I in intens:
        report(allrows[I], tau, f"I={I:<5} (rho={I/(te*R_EDGE):.0f})")
    print(flush=True)


def run():
    print(f"PATCH + DENSITY axes  |  POOL={len(POOL)} seeds "
          f"{POOL[0]}..{POOL[-1]}  |  R_S={R_S}", flush=True)
    print(f"gate: tau(n)=p{int((1-ALPHA)*100)} uniform null, "
          f"MC seed={NULL_MC_SEED} reps={NULL_MC_REPS}\n", flush=True)
    run_patch()       # cheaper -> early signal
    run_density()     # includes I=24000 (the long pole)


if __name__ == "__main__":
    run()
