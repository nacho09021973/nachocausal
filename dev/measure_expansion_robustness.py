"""dev measurement (PR-003, comité decision 002 — S1 + S2). EXPLORATION ONLY, nothing
frozen, not validated, not audited. Scored with hidden r (reveal ONLY to score).

Two reversible checks the committee asked for before pursuing the expansion diagnostic:

  S1 — MINIMAL FALSIFICATION TEST (falsifier).  Fase #1-B builds the EGS Eq.14 expansion
       estimator only on the OUTGOING ladders, split by an order-only direction proxy
       (relphi_mean > median) that the dev notes flag as UNRELIABLE (ABSTAIN). If the
       interior-negative / exterior-positive sign change of mean(E) at r*~R_S SURVIVES
       with NO direction split (all ladders pooled), the 3600 POSITIVE is robust to the
       bad discriminator. If it DISAPPEARS, Fase #1-B is an artefact of ladder selection.

  S2 — TALLER-BOX PROBE (physicist).  EGS (md:188-191, 450) get a sharp interior/exterior
       contrast only with LARGE timelike extent (t*/r_S in [0,50]); the dev runs used
       t_edge=6. EGS also flag (md:469) that raising DENSITY does not converge ("not
       enough ladders in a given sprinkling"). So the right lever is timelike extent at
       FIXED density, NOT higher density. numpy_sprinkle draws N=Poisson(intensity) points
       in a box [0,t_edge] x R_EDGE, so to hold density rho=N/area fixed while raising
       t_edge we SCALE intensity proportionally:
           (t_edge, intensity) = (6, 3600), (12, 7200), (24, 14400)  -> ell = const ~0.0447.
       We measure whether interior negativity strengthens / persists with timelike extent.

DISCIPLINE (comité decision 002, §9):
  * EXPLORE_POOL seeds only; RESERVED_002 untouched; r/d_perp ONLY score.
  * t_edge != 6 changes the box, so ell != thresholds.ell(intensity); we compute a LOCAL
    ell = sqrt(area/N) for d_perp and DO NOT compare against the frozen theta_stab/theta_loc
    (which assume t_edge=6/area=7.2). We report the SHAPE of the signal, not a PASS/FAIL.
  * The sealed localiser/thresholds are NOT touched; make verify-seal must stay 6e2c3888...

Run:  python3 dev/measure_expansion_robustness.py --phase s1            # 2 seeds
      python3 dev/measure_expansion_robustness.py --phase s2 --seeds 2  # taller-box sweep
      python3 dev/measure_expansion_robustness.py                       # s1 then s2
"""

from __future__ import annotations

import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import generator, thresholds  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402
from explore_ladders import link_future_csr  # noqa: E402
from explore_direction import order_only_heights, rel_field  # noqa: E402
# reuse the EXACT Fase #1-B kernels so this is the same instrument, only the split changes
from measure_expansion_horizon import (  # noqa: E402
    KNN, LMIN, RBIN, R_S, build_ladders, profile, sep,
)

R_EDGE = thresholds.R_EDGE


def local_ell(intensity, t_edge):
    """ell = rho^-1/2 with the ACTUAL box area (not the frozen 7.2)."""
    return (intensity / (t_edge * R_EDGE)) ** -0.5


def expansion_samples(C, emb, seed, split=True):
    """(r_of_rung, E) for ladder pairs (EGS Eq.14). split=True -> outgoing-only via the
    relphi proxy (the original Fase #1-B); split=False -> ALL ladders pooled (S1 test).
    r revealed ONLY here (scoring)."""
    Lmat, indptr, idx = link_future_csr(C)
    Lpast, Lfut = order_only_heights(C)
    relphi = rel_field(Lfut, Lpast)
    ladders, _ = build_ladders(C, indptr, idx, Lmat, seed)
    if len(ladders) < 2:
        return np.zeros(0), np.zeros(0)
    if split:
        rphi_mean = np.array([float(relphi[p].mean()) for p in ladders])
        out = [p for p, m in zip(ladders, rphi_mean > np.median(rphi_mean)) if m]
    else:
        out = ladders                                   # NO direction split (S1)
    r = emb[:, 1]                                        # TRUTH — score only

    rr, EE = [], []
    heads = np.array([p[0] for p in out])
    for i, pI in enumerate(out):
        d0 = np.array([sep(int(pI[0]), int(h), C, Lpast) for h in heads])
        d0[i] = np.nan
        order = np.argsort(np.where(np.isfinite(d0), d0, np.inf))
        for j in order[:KNN]:
            if not np.isfinite(d0[j]):
                break
            pJ = out[j]
            L = min(len(pI), len(pJ)) - 1
            for a in range(L):
                Da = sep(int(pI[a]), int(pJ[a]), C, Lpast)
                Da1 = sep(int(pI[a + 1]), int(pJ[a + 1]), C, Lpast)
                if np.isfinite(Da) and np.isfinite(Da1) and Da > 0:
                    EE.append((Da1 - Da) / Da)
                    rr.append(float(r[int(pI[a])]))
    return np.array(rr), np.array(EE)


def _contrast(r, E):
    hi = float(E[r > R_S + 0.1].mean()) if (r > R_S + 0.1).any() else float("nan")
    lo = float(E[r < R_S - 0.1].mean()) if (r < R_S - 0.1).any() else float("nan")
    return hi, lo, (hi - lo)


def _aggregate(seeds, intensity, t_edge, split):
    agg_r, agg_E, agg_r_mk, agg_E_mk, rstars = [], [], [], [], []
    for s in seeds:
        emb, _, _ = generator.numpy_sprinkle(s, float(intensity), float(t_edge))
        Cbh = generator.past_matrix_fast(emb, "BH")
        r_bh, E_bh = expansion_samples(Cbh, emb, s, split=split)
        _, _, _, rstar = profile(r_bh, E_bh)
        rstars.append(rstar)
        agg_r.append(r_bh); agg_E.append(E_bh)
        Cmk = generator.past_matrix_fast(emb, "MINK")
        r_mk, E_mk = expansion_samples(Cmk, emb, s, split=split)
        agg_r_mk.append(r_mk); agg_E_mk.append(E_mk)
    R_bh = np.concatenate(agg_r) if agg_r else np.zeros(0)
    E_bh = np.concatenate(agg_E) if agg_E else np.zeros(0)
    R_mk = np.concatenate(agg_r_mk) if agg_r_mk else np.zeros(0)
    E_mk = np.concatenate(agg_E_mk) if agg_E_mk else np.zeros(0)
    return R_bh, E_bh, R_mk, E_mk, np.array(rstars, float)


def _report(tag, R_bh, E_bh, R_mk, E_mk, rstars, ell):
    cen, me, cnt, rstar_pool = profile(R_bh, E_bh)
    _, _, _, rstar_mk = profile(R_mk, E_mk)
    hi_bh, lo_bh, con_bh = _contrast(R_bh, E_bh)
    hi_mk, lo_mk, con_mk = _contrast(R_mk, E_mk)
    med = lambda a: float(np.nanmedian(a)) if np.isfinite(np.asarray(a, float)).any() else float("nan")
    d_perp = np.abs(rstars - R_S) / ell
    print(f"  [{tag}]  ell={ell:.4f}  samples BH={E_bh.size} MINK={E_mk.size}")
    print(f"     interior bins (r<R_S, expect NEG):", end=" ")
    print(" ".join(f"{c:.2f}:{m:+.3f}" for c, m in zip(cen, me) if c < R_S) or "(none)")
    print(f"     contrast BH = {con_bh:+.3f} ({hi_bh:+.3f} vs {lo_bh:+.3f})   "
          f"MINK = {con_mk:+.3f}")
    print(f"     zero-crossing r*: BH pooled={rstar_pool:.3f} per-seed med={med(rstars):.3f}  "
          f"d_perp/ell={med(d_perp):.2f}   (MINK r*={rstar_mk:.3f})")
    flat_pass = np.isfinite(con_bh) and con_bh > 0.05 and (
        not np.isfinite(con_mk) or abs(con_mk) < 0.5 * con_bh)
    print(f"     FLAT CONTROL (BH sign-change, MINK not): {'PASS' if flat_pass else 'FAIL'}")
    return con_bh, rstar_pool


def run_s1(seeds):
    print("=" * 78)
    print("S1 — MINIMAL FALSIFICATION TEST: does the mean(E) sign-change survive WITHOUT")
    print("     the (unreliable) outgoing/ingoing direction split?  t_edge=6, intensity=3600")
    print("=" * 78)
    ell = local_ell(3600, 6.0)
    t0 = time.perf_counter()
    print("\n-- WITH direction split (original Fase #1-B) --")
    a = _aggregate(seeds, 3600, 6.0, split=True)
    con_split, rs_split = _report("split", *a, ell)
    print("\n-- WITHOUT direction split (all ladders pooled) --")
    b = _aggregate(seeds, 3600, 6.0, split=False)
    con_nosplit, rs_nosplit = _report("no-split", *b, ell)
    print(f"\n  [{time.perf_counter()-t0:.0f}s]  VERDICT S1:")
    # The LOCALIZING signature is interior mean(E)<0 AND a zero-crossing AT R_S, NOT merely
    # exterior>interior (a non-localizing gradient still gives contrast>0). Judge on both.
    int_mean = lambda R, E: float(E[R < R_S - 0.1].mean()) if (R < R_S - 0.1).any() else float("nan")
    im = int_mean(b[0], b[1])                                  # no-split interior mean(E)
    dperp_nosplit = abs(rs_nosplit - R_S) / ell
    localizes = np.isfinite(im) and im < 0 and np.isfinite(rs_nosplit) and dperp_nosplit < 1.5
    print(f"     no-split: interior mean(E)={im:+.3f} (need <0)   crossing r*={rs_nosplit:.3f} "
          f"d_perp/ell={dperp_nosplit:.2f} (need <1.5)   contrast={con_nosplit:+.3f}")
    print(f"     -> {'LOCALIZING SIGNAL SURVIVES the split removal' if localizes else 'LOCALIZING SIGNAL DOES NOT SURVIVE: interior negativity / crossing-at-R_S depend on the relphi split (only a weak non-localizing gradient remains)'}")
    print(f"     (split version: interior negative, contrast {con_split:+.3f}, r*={rs_split:.3f})")
    return localizes


def run_s2(seeds, split):
    print("\n" + "=" * 78)
    print("S2 — TALLER-BOX PROBE at FIXED density (the physicist's lever): timelike extent")
    print(f"     t_edge in 6/12/24 with intensity 3600/7200/14400 (ell~const).  split={split}")
    print("=" * 78)
    configs = [(6.0, 3600), (12.0, 7200), (24.0, 14400)]
    for t_edge, inten in configs:
        ell = local_ell(inten, t_edge)
        t0 = time.perf_counter()
        print(f"\n-- t_edge={t_edge:.0f}  intensity={inten}  (density fixed) --")
        a = _aggregate(seeds, inten, t_edge, split=split)
        _report(f"t={t_edge:.0f}", *a, ell)
        print(f"     [{time.perf_counter()-t0:.0f}s]")
    print("\n  READ: if interior negativity / contrast STRENGTHENS or holds as t_edge grows,")
    print("  the 7200 degradation was a DOMAIN (short-box) artefact, fixable per EGS md:188-191.")


if __name__ == "__main__":
    phase = "both"
    if "--phase" in sys.argv:
        phase = sys.argv[sys.argv.index("--phase") + 1]
    nseeds = 2
    if "--seeds" in sys.argv:
        nseeds = int(sys.argv[sys.argv.index("--seeds") + 1])
    force_split = "--split" in sys.argv
    seeds = list(EXPLORE_POOL[:nseeds])

    s1_ok = None
    if phase in ("s1", "both"):
        s1_ok = run_s1(seeds)
    if phase in ("s2", "both"):
        # default: pool all ladders (no split) unless S1 said the split is needed / forced
        use_split = force_split or (s1_ok is False)
        run_s2(seeds, split=use_split)
