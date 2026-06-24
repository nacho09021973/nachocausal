"""dev measurement (PR-003 roadmap 24-jun, Fase #1 — iterative order-only re-seeding).
EXPLORATION ONLY, nothing frozen. A first concrete v0 of EGS's "piecewise discrete
horizon" idea (arXiv:2605.06813 md:443, left to future work), made BLIND.

Idea. A single order-only tracer cannot stay on r_S (marginally unstable null orbit ->
peel-off after O(1) rungs; this is the BARE_RELOCALISATION bound). EGS's remedy is to
re-seed on successive future antichains and take the UNION of localised pieces. Here the
"piece" is not a ladder but a re-localised boundary POINT, and the "future antichain" is an
order-only TIME-FRONT:

  * L_past(e) = longest chain ending at e is an order-only discrete time. Its level sets
    {e : L_past(e) == d} are GENUINE ANTICHAINS (a<b => L_past(b) > L_past(a), so equal
    L_past => incomparable). These are the order-only future antichains to re-seed on.
  * On each front F_d we re-run the SEALED v2 boundary localiser: O(i)=|future(i)| (column
    sum of C), `two_means_split`, and the frozen tau(n) abstain gate. A non-abstaining front
    yields interior (O<thr) / exterior (O>=thr) witness sets -> a localised boundary point.
  * The ordered union of those points over fronts is the candidate PIECEWISE horizon locus.

The question Fase #1 asks (measured here): does this order-only piecewise locus
  (a) COVER an arc of r_S over many fronts (more than the single seed neighbourhood),
  (b) keep each piece at d_perp = O(ell),
  (c) form a CONNECTED causal sequence across fronts, and
  (d) PERSIST / converge with density (boundary_r_std small, shrinking)?

Leakage discipline (docs/pr003_leakage_gate.md, pre-committed in comite_decision_001):
  - Construction uses ONLY C-derived quantities (vol, L_past). r is revealed ONLY to score.
  - Witness sets are taken at the EXTREMAL O-value (a function of the O-multiset) -> no
    label-dependent tie-break; a relabel Guard-v checks set-invariance and REPORTS it.
  - MINK same-cloud FLAT CONTROL: the locus must NOT persist (low r-scatter) without a horizon.
  - No r feedback: nothing scored changes the construction.

Run:  python3 dev/measure_iterative_reseed.py            # 6 seeds x {3600,7200}
      python3 dev/measure_iterative_reseed.py --smoke    # 2 seeds x {3600}
      python3 dev/measure_iterative_reseed.py --full     # 6 seeds x {3600,7200,14400}
"""

from __future__ import annotations

import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import estimator, gate, generator, thresholds  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402
from explore_direction import order_only_heights  # noqa: E402
from measure_pr003 import relabel  # noqa: E402

R_S = thresholds.R_S
NMIN = 8          # min front size to attempt a localisation (needs a 2-means + tau gate)


# ---------------------------------------------------------------------------
# ORDER-ONLY construction: re-localise the boundary on each L_past time-front.
# Returns, per localising front, the interior/exterior witness ELEMENT SETS
# (original labels) and the front depth. r is NOT touched here.
# ---------------------------------------------------------------------------
def build_locus(C):
    vol = C.sum(axis=0).astype(int)               # O(i) = |future(i)|, order-only
    Lpast, _ = order_only_heights(C)              # order-only discrete time
    locus = []                                    # (depth, in_set, ex_set)
    n_front = n_abst = 0
    for d in range(1, int(Lpast.max()) + 1):
        F = np.nonzero(Lpast == d)[0]
        if F.size < NMIN:
            continue
        n_front += 1
        vals = vol[F]
        thr, _ = estimator.two_means_split(list(vals))
        if gate.abstains(estimator.improvement(list(vals)), F.size):
            n_abst += 1
            continue
        inside = F[vals < thr]
        outside = F[vals >= thr]
        if inside.size == 0 or outside.size == 0:
            continue
        v_in = int(vol[inside].max())             # extremal O -> invariant witness set
        v_ex = int(vol[outside].min())
        in_set = inside[vol[inside] == v_in]
        ex_set = outside[vol[outside] == v_ex]
        locus.append((d, np.sort(in_set), np.sort(ex_set)))
    return locus, n_front, n_abst


def _connected_frac(locus, C):
    """fraction of consecutive localising fronts whose witness sets are causally
    linked (some witness of the lower front is in the past of some witness of the
    upper). Order-only."""
    if len(locus) < 2:
        return float("nan")
    ok = 0
    for (_, in_a, ex_a), (_, in_b, ex_b) in zip(locus[:-1], locus[1:]):
        a = np.concatenate([in_a, ex_a])
        b = np.concatenate([in_b, ex_b])
        if bool(C[np.ix_(b, a)].any()):           # any b has any a in its past
            ok += 1
    return ok / (len(locus) - 1)


def score_locus(locus, emb, ell):
    """REVEAL r — scoring only. Per front: midpoint r, d_perp/ell, signed width,
    covers R_S. Returns arrays + summary."""
    r = emb[:, 1]
    t = emb[:, 0]
    mids, dperp, covers, tspan = [], [], [], []
    for _, in_set, ex_set in locus:
        r_in = float(r[in_set].mean())            # interior witness r
        r_ex = float(r[ex_set].mean())            # exterior witness r
        mid = 0.5 * (r_in + r_ex)
        mids.append(mid)
        dperp.append(abs(mid - R_S) / ell)
        covers.append(min(r_in, r_ex) <= R_S <= max(r_in, r_ex))
        tspan.append(float(t[np.concatenate([in_set, ex_set])].mean()))
    mids = np.array(mids)
    dperp = np.array(dperp)
    r_iqr = (float(np.percentile(mids, 75) - np.percentile(mids, 25))
             if mids.size >= 2 else float("nan"))
    return dict(
        mids=mids, dperp=dperp, covers=np.array(covers),
        n=len(locus),
        dperp_med=float(np.median(dperp)) if dperp.size else float("nan"),
        cover_frac=float(np.mean(covers)) if covers else float("nan"),
        r_std=float(np.std(mids)) if mids.size else float("nan"),
        r_iqr=r_iqr,                               # robust scatter (outlier-resistant)
        t_lo=float(min(tspan)) if tspan else float("nan"),
        t_hi=float(max(tspan)) if tspan else float("nan"),
    )


def _witness_set(locus):
    out = set()
    for _, a, b in locus:
        out.update(int(x) for x in a)
        out.update(int(x) for x in b)
    return out


def measure_seed(seed, intensity, t_edge, guard=True):
    emb, _, _ = generator.numpy_sprinkle(seed, float(intensity), float(t_edge))
    ell = thresholds.ell(intensity)
    Cbh = generator.past_matrix_fast(emb, "BH")
    Cmk = generator.past_matrix_fast(emb, "MINK")

    locus, n_front, n_abst = build_locus(Cbh)
    sc = score_locus(locus, emb, ell)
    sc["n_front"] = n_front
    sc["abstain_frac"] = (n_abst / n_front) if n_front else float("nan")
    sc["connected_frac"] = _connected_frac(locus, Cbh)
    sc["theta_stab"] = thresholds.theta_stab(intensity)

    # MINK flat control (same cloud): without a horizon the localiser should NOT
    # build a coherent extended locus. Capture both how MANY fronts it localises and
    # how tightly (so "MINK localised ~nothing" reads as the control PASSING, not as
    # a spuriously small r_std).
    locus_mk, n_front_mk, n_abst_mk = build_locus(Cmk)
    sc_mk = score_locus(locus_mk, emb, ell)
    sc["mink_n"] = sc_mk["n"]
    sc["mink_r_std"] = sc_mk["r_std"]
    sc["mink_dperp_med"] = sc_mk["dperp_med"]     # |mid-R_S|/ell vs the SAME R_S (no horizon)
    sc["mink_abstain_frac"] = (n_abst_mk / n_front_mk) if n_front_mk else float("nan")

    # relabel Guard-v on the constructed witness set (order-only invariance).
    sc["relabel_invariant"] = None
    if guard:
        rng = np.random.default_rng(seed ^ 0xA17C)
        C2, _, inv = relabel(Cbh, emb, rng)
        locus2, _, _ = build_locus(C2)
        back = set(int(inv[s]) for s in _witness_set(locus2))
        sc["relabel_invariant"] = (back == _witness_set(locus))
    return sc


def run(seeds, intensities, t_edge=6.0, guard=True):
    print("PR-003 Fase #1 — iterative order-only boundary re-localisation "
          "(piecewise locus)")
    print(f"seeds={len(seeds)}  t_edge={t_edge:.0f}  R_S={R_S}  NMIN={NMIN}  "
          f"guard={guard}\n")
    for inten in intensities:
        ell = thresholds.ell(inten)
        t0 = time.perf_counter()
        rows = [measure_seed(s, inten, t_edge, guard) for s in seeds]
        agg = lambda k: np.array([r[k] for r in rows], float)
        med = lambda a: float(np.nanmedian(a)) if np.isfinite(a).any() else float("nan")
        n, dperp, cov = agg("n"), agg("dperp_med"), agg("cover_frac")
        rstd, riqr, conn, abst = agg("r_std"), agg("r_iqr"), agg("connected_frac"), agg("abstain_frac")
        mink_n, mink_dperp = agg("mink_n"), agg("mink_dperp_med")
        inv = [r["relabel_invariant"] for r in rows]
        theta_stab = rows[0]["theta_stab"]
        # flat control PASSES if BH builds a coherent locus near R_S that MINK does
        # not: BH sits closer to R_S than MINK, or MINK barely localises.
        flat_pass = (med(dperp) < med(mink_dperp)) or (med(mink_n) < 0.5 * med(n))
        print(f"intensity={inten:>6.0f}  ell={ell:.4f}  theta_stab={theta_stab:.3f}  "
              f"[{time.perf_counter()-t0:.0f}s]")
        print(f"   localising fronts / seed   : median={med(n):.0f}  "
              f"[{np.nanmin(n):.0f},{np.nanmax(n):.0f}]   abstain_frac={med(abst):.0%}")
        print(f"   d_perp/ell  per-front (med) : {med(dperp):.2f}   "
              f"(each piece O(ell)?)")
        print(f"   coverage of r_S (covers)   : {med(cov):.0%}  of localising fronts")
        print(f"   connected across fronts    : {med(conn):.0%}")
        print(f"   boundary r-scatter         : BH std={med(rstd):.4f} IQR={med(riqr):.4f}"
              f"   (theta_stab={theta_stab:.3f})")
        print(f"   FLAT CONTROL (MINK, same cloud): BH d_perp={med(dperp):.2f}ell vs "
              f"MINK d_perp={med(mink_dperp):.2f}ell ; fronts BH={med(n):.0f} vs "
              f"MINK={med(mink_n):.0f}  ->  {'PASS' if flat_pass else 'FAIL'}")
        if guard:
            ok = sum(1 for x in inv if x is True)
            print(f"   relabel Guard-v invariant  : {ok}/{len(inv)} seeds")
        print()


if __name__ == "__main__":
    if "--smoke" in sys.argv:
        run(list(EXPLORE_POOL[:2]), [3600.0])
    elif "--full" in sys.argv:
        run(list(EXPLORE_POOL[:6]), [3600.0, 7200.0, 14400.0])
    else:
        run(list(EXPLORE_POOL[:6]), [3600.0, 7200.0])
