"""dev measurement (PR-003 roadmap 24-jun) — S3: HARDEN iterative order-only
re-seeding v0. EXPLORATION ONLY, nothing frozen, not validated, not audited.

Авал: docs/comite/comite_decision_002_*.md §9 (S3). v0 lives in
`dev/measure_iterative_reseed.py`; this v1 reuses the SEALED v2 localiser
(`two_means_split` + `gate.abstains` + frozen `tau(n)`) WITHOUT touching it.
The advance over v0 is dev-side accounting only:

  (1) THIRD DENSITY 14400 (criterion (d): does coverage/persistence converge?).
  (2) HONEST COVERAGE. The frozen `tau(n)` gate is the order-only STOPPING RULE
      (the principled answer to "is there an order-only stopping rule?" — it is
      NOT a new rule, it is the gate already sealed in fixtures/tau_table.json).
      v0 dropped abstaining (and degenerate) fronts from the locus AND from the
      coverage denominator -> coverage biased UP (falsifier, comite_decision_002
      §5 "verdict coercion 3"). v1 counts every candidate front (size >= NMIN);
      abstain and degenerate fronts count as MISSES. Reports BOTH the optimistic
      v0 rate (covers / localised) and the honest rate (covers / candidates).
  (3) STOPPING-RULE DIAGNOSTIC (r reveals ONLY to score, never to cut). Among
      the fronts tau(n) ABSTAINED on, what fraction WOULD have covered R_S if
      forced to localise? If that is << the localised cover-rate, tau(n) is a
      GOOD stopping rule: it abstains preferentially on the non-covering tail.
      If it is comparable, tau(n) throws away good fronts. The CUT is purely
      order-only (tau(n)); r only measures, post-hoc, whether the cut aligned
      with geometry. No r feeds back into construction.

Leakage discipline (docs/pr003_leakage_gate.md; pre-committed comite_decision_002
§9 binding rules): construction uses ONLY C-derived quantities (vol O, L_past,
tau(n)); r/d_perp ONLY score, never seed/construct/cut/select. relabel Guard-v
on the constructed set must keep passing. MINK same-cloud flat control. No
threshold touched; `make verify-seal` = 6e2c3888... before AND after.

Honesty: a v1 that DEGRADES at 14400 is a legitimate NEGATIVE / re-label to
INCONCLUSIVE, NOT a licence to drop the density. 14400 is reported pase lo que
pase. No "apparent horizon" framing; only order-only localisation of hidden r_S
within the bracket, in a finite 1+1D patch.

Run:  python3 dev/measure_iterative_reseed_v1.py --smoke   # 2 seeds x {3600}
      python3 dev/measure_iterative_reseed_v1.py           # 6 seeds x {3600,7200,14400}
"""

from __future__ import annotations

import hashlib
import os
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import estimator, gate, generator, thresholds  # noqa: E402
import explore_seeds  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402
from explore_direction import order_only_heights  # noqa: E402
from measure_pr003 import relabel  # noqa: E402
# reuse the v0 connectivity / witness-set helpers unchanged (same construction).
from measure_iterative_reseed import _connected_frac, _witness_set  # noqa: E402

R_S = thresholds.R_S
NMIN = 8          # min front size to ATTEMPT a localisation (a candidate front)

# front categories
LOCALISED = "loc"     # tau(n) did NOT abstain and the split is non-degenerate
ABSTAIN = "abstain"   # tau(n) abstained (the order-only stopping rule fired)
DEGEN = "degen"       # non-abstain but the 2-means split put all mass on one side


# ---------------------------------------------------------------------------
# ORDER-ONLY construction. For EVERY candidate front (size >= NMIN) record its
# category and the witness ELEMENT SETS of its (would-be) localisation. The CUT
# is tau(n) only. r is NOT touched here. The constructed locus = LOCALISED only;
# abstain/degen fronts carry witnesses too, used ONLY for the post-hoc
# stopping-rule scoring diagnostic (never built into the object).
# ---------------------------------------------------------------------------
def build_locus(C):
    vol = C.sum(axis=0).astype(int)               # O(i) = |future(i)|, order-only
    Lpast, _ = order_only_heights(C)              # order-only discrete time
    fronts = []                                   # (depth, category, in_set, ex_set)
    for d in range(1, int(Lpast.max()) + 1):
        F = np.nonzero(Lpast == d)[0]
        if F.size < NMIN:
            continue                              # below the localisable domain
        vals = vol[F]
        thr, _ = estimator.two_means_split(list(vals))
        abst = gate.abstains(estimator.improvement(list(vals)), F.size)
        inside = F[vals < thr]
        outside = F[vals >= thr]
        if inside.size == 0 or outside.size == 0:
            cat = DEGEN
            in_set = ex_set = np.array([], dtype=int)
        else:
            v_in = int(vol[inside].max())         # extremal O -> invariant witness set
            v_ex = int(vol[outside].min())
            in_set = inside[vol[inside] == v_in]
            ex_set = outside[vol[outside] == v_ex]
            cat = ABSTAIN if abst else LOCALISED
        fronts.append((d, cat, np.sort(in_set), np.sort(ex_set)))
    return fronts


def _locus(fronts):
    """the constructed object: LOCALISED fronts only (depth, in_set, ex_set)."""
    return [(d, a, b) for (d, c, a, b) in fronts if c == LOCALISED]


def _covers(r, in_set, ex_set):
    r_in = float(r[in_set].mean())
    r_ex = float(r[ex_set].mean())
    return min(r_in, r_ex) <= R_S <= max(r_in, r_ex), 0.5 * (r_in + r_ex)


def score(fronts, emb, ell):
    """REVEAL r — scoring only. Honest coverage + stopping-rule diagnostic."""
    r = emb[:, 1]
    t = emb[:, 0]
    n_cand = len(fronts)
    n_abst = sum(1 for f in fronts if f[1] == ABSTAIN)
    n_degen = sum(1 for f in fronts if f[1] == DEGEN)

    mids, dperp, tspan = [], [], []
    loc_cov = 0                                   # localised fronts that cover R_S
    abst_forced = 0                               # abstained fronts WITH a 2-side split
    abst_cov = 0                                  # ...of those, that WOULD have covered
    for d, cat, in_set, ex_set in fronts:
        has_split = in_set.size > 0 and ex_set.size > 0
        if not has_split:
            continue
        cov, mid = _covers(r, in_set, ex_set)
        if cat == LOCALISED:
            mids.append(mid)
            dperp.append(abs(mid - R_S) / ell)
            tspan.append(float(t[np.concatenate([in_set, ex_set])].mean()))
            loc_cov += int(cov)
        elif cat == ABSTAIN:
            abst_forced += 1
            abst_cov += int(cov)
    mids = np.array(mids)
    dperp = np.array(dperp)
    n_loc = len(mids)
    r_iqr = (float(np.percentile(mids, 75) - np.percentile(mids, 25))
             if mids.size >= 2 else float("nan"))
    return dict(
        n_cand=n_cand, n_loc=n_loc, n_abst=n_abst, n_degen=n_degen,
        abstain_frac=(n_abst / n_cand) if n_cand else float("nan"),
        dperp_med=float(np.median(dperp)) if dperp.size else float("nan"),
        # optimistic v0 rate: covers among LOCALISED fronts only.
        cover_loc=(loc_cov / n_loc) if n_loc else float("nan"),
        # HONEST rate: covers among ALL candidate fronts (abstain+degen = miss).
        cover_honest=(loc_cov / n_cand) if n_cand else float("nan"),
        # stopping-rule diagnostic: would-cover rate among ABSTAINED fronts.
        abst_wouldcover=(abst_cov / abst_forced) if abst_forced else float("nan"),
        r_std=float(np.std(mids)) if mids.size else float("nan"),
        r_iqr=r_iqr,
        t_lo=float(min(tspan)) if tspan else float("nan"),
        t_hi=float(max(tspan)) if tspan else float("nan"),
    )


def measure_seed(seed, intensity, t_edge, guard=True):
    emb, _, _ = generator.numpy_sprinkle(seed, float(intensity), float(t_edge))
    ell = thresholds.ell(intensity)
    Cbh = generator.past_matrix_fast(emb, "BH")
    Cmk = generator.past_matrix_fast(emb, "MINK")

    fronts = build_locus(Cbh)
    sc = score(fronts, emb, ell)
    sc["connected_frac"] = _connected_frac(_locus(fronts), Cbh)
    sc["theta_stab"] = thresholds.theta_stab(intensity)

    # MINK flat control (same cloud): without a horizon the localiser should NOT
    # build a coherent extended locus. Report honest coverage there too.
    fronts_mk = build_locus(Cmk)
    sc_mk = score(fronts_mk, emb, ell)
    sc["mink_n_loc"] = sc_mk["n_loc"]
    sc["mink_dperp_med"] = sc_mk["dperp_med"]
    sc["mink_cover_honest"] = sc_mk["cover_honest"]

    # relabel Guard-v on the CONSTRUCTED witness set (order-only invariance).
    sc["relabel_invariant"] = None
    if guard:
        rng = np.random.default_rng(seed ^ 0xA17C)
        C2, _, inv = relabel(Cbh, emb, rng)
        loc2 = _locus(build_locus(C2))
        back = set(int(inv[s]) for s in _witness_set(loc2))
        sc["relabel_invariant"] = (back == _witness_set(_locus(fronts)))
    return sc


def _provenance():
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    seal = hashlib.sha256(
        open(os.path.join(os.path.dirname(thresholds.__file__),
                          "thresholds.py"), "rb").read()).hexdigest()
    seeds = list(EXPLORE_POOL[:6])
    assert not any(explore_seeds.in_reserved_002(s) for s in seeds), \
        "seed entered RESERVED_002 band"
    print("# PR-003 S3 — iterative-reseed v1 (HARDEN). dev / exploratory / NOT a result.")
    print(f"# git HEAD={head}  numpy={np.__version__}  {platform.uname().system} "
          f"{platform.uname().release}")
    print(f"# thresholds.py sha256={seal}  (seal must read 6e2c3888...)")
    print(f"# seeds=EXPLORE_POOL[:6]={seeds}  RESERVED_002 untouched")
    print(f"# {datetime.now(timezone.utc).isoformat(timespec='seconds')}  R_S={R_S}  NMIN={NMIN}\n")


def run(seeds, intensities, t_edge=6.0, guard=True):
    _provenance()
    print("iterative order-only boundary re-localisation, piecewise locus; "
          "tau(n) = order-only stopping rule")
    print(f"seeds={len(seeds)}  t_edge={t_edge:.0f}  guard={guard}\n")
    hist = []
    for inten in intensities:
        ell = thresholds.ell(inten)
        t0 = time.perf_counter()
        rows = [measure_seed(s, inten, t_edge, guard) for s in seeds]
        agg = lambda k: np.array([r[k] for r in rows], float)
        med = lambda a: float(np.nanmedian(a)) if np.isfinite(a).any() else float("nan")
        n_loc, n_cand = agg("n_loc"), agg("n_cand")
        dperp = agg("dperp_med")
        cov_loc, cov_hon = agg("cover_loc"), agg("cover_honest")
        abst, abst_wc = agg("abstain_frac"), agg("abst_wouldcover")
        rstd, riqr, conn = agg("r_std"), agg("r_iqr"), agg("connected_frac")
        mink_n, mink_dperp, mink_cov = agg("mink_n_loc"), agg("mink_dperp_med"), agg("mink_cover_honest")
        inv = [r["relabel_invariant"] for r in rows]
        theta_stab = rows[0]["theta_stab"]
        # flat control PASSES if BH builds a coherent locus near R_S that MINK does
        # not (BH closer to R_S, or MINK barely localises, or MINK honest cover ~ 0).
        flat_pass = (med(dperp) < med(mink_dperp)) or (med(mink_n) < 0.5 * med(n_loc))
        hist.append((inten, ell, med(n_loc), med(dperp), med(cov_loc), med(cov_hon),
                     med(abst), med(abst_wc), med(conn), med(rstd), med(riqr)))
        print(f"intensity={inten:>6.0f}  ell={ell:.4f}  theta_stab={theta_stab:.3f}  "
              f"[{time.perf_counter()-t0:.0f}s]")
        print(f"   candidate fronts (>=NMIN)/seed : median={med(n_cand):.0f}   "
              f"localised={med(n_loc):.0f}  abstain={med(abst):.0%}")
        print(f"   d_perp/ell  per-front (med)    : {med(dperp):.2f}   "
              f"(phys d_perp={med(dperp)*ell:.4f})")
        print(f"   coverage of R_S  OPTIMISTIC    : {med(cov_loc):.0%}  (covers / localised, the v0 number)")
        print(f"   coverage of R_S  HONEST        : {med(cov_hon):.0%}  (covers / ALL candidates; abstain+degen = miss)")
        print(f"   tau(n) stopping-rule alignment : abstained fronts would-cover {med(abst_wc):.0%}  "
              f"(<< {med(cov_loc):.0%} localised => gate drops the non-covering tail)")
        print(f"   connected across fronts        : {med(conn):.0%}")
        print(f"   boundary r-scatter             : BH std={med(rstd):.4f} IQR={med(riqr):.4f}"
              f"   (theta_stab={theta_stab:.3f})")
        print(f"   FLAT CONTROL (MINK, same cloud): BH d_perp={med(dperp):.2f}ell honest_cov={med(cov_hon):.0%}"
              f"  vs MINK d_perp={med(mink_dperp):.2f}ell honest_cov={med(mink_cov):.0%} "
              f"fronts={med(mink_n):.0f}  ->  {'PASS' if flat_pass else 'FAIL'}")
        if guard:
            ok = sum(1 for x in inv if x is True)
            print(f"   relabel Guard-v invariant      : {ok}/{len(inv)} seeds")
        print()

    # convergence read across densities (criterion (d)) — printed, not judged here.
    print("CONVERGENCE TABLE (criterion d) — does the HONEST locus persist with density?")
    print("  intensity   ell     n_loc  dperp/ell  cov_opt  cov_honest  abstain  abst_wc  conn   r_IQR")
    for (inten, ell, nl, dp, cl, ch, ab, awc, cn, rs, riqr) in hist:
        print(f"   {inten:>7.0f}  {ell:.4f}  {nl:>5.0f}    {dp:>5.2f}     "
              f"{cl:>4.0%}     {ch:>4.0%}      {ab:>4.0%}    {awc:>4.0%}   {cn:>4.0%}  {riqr:.4f}")


if __name__ == "__main__":
    if "--smoke" in sys.argv:
        run(list(EXPLORE_POOL[:2]), [3600.0])
    else:
        run(list(EXPLORE_POOL[:6]), [3600.0, 7200.0, 14400.0])
