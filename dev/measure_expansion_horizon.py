"""dev measurement (PR-003 roadmap 24-jun, Fase #1-B — the CANONICAL apparent-horizon
diagnostic). EXPLORATION ONLY, nothing frozen. Scored with hidden r (reveal ONLY to score).

EGS (arXiv:2605.06813) define the apparent horizon as the marginally outer-trapped surface
where the outgoing null expansion vanishes, Theta_out(r)=0 (md:201,225). In Schwarzschild
Theta_out(r) = (1/r)(1 - 2M/r): POSITIVE for r>2M, NEGATIVE for r<2M, ZERO at r=R_S. Their
discrete counterpart (Eq. 14, md:276-287) uses PAIRS of fuzzy ladders (null tracers) and the
logarithmic change of the SPATIAL DISTANCE between them along the affine parameter (~ rung
index): mean(E) changes sign across the horizon "as it should" (md:16).

EGS computed those spatial distances WITH the embedding. The whole point of PR-003 is to be
BLIND, so here the transverse separation between two spacelike rungs is an ORDER-ONLY proxy:
the cardinality of the SMALLEST CAUSAL DIAMOND enclosing them,
    sep(u,v) = sqrt(|[e,f]|),  e = highest common past, f = lowest common future,
which scales like the proper size of the minimal enclosing diamond (~ spatial separation).
r is revealed ONLY to score WHERE mean(E) crosses zero.

Construction (order-only):
  * ladders = longest fuzzy ladders (explore_ladders kernel) from sampled link start-rungs;
  * direction label = sign of relphi_mean (#2 order-only exteriority feature) -> OUTGOING set;
  * for each outgoing ladder, its K nearest outgoing neighbours (smallest rung-0 sep);
  * per matched rung a (spacelike pair): D_a = sep, E = (D_{a+1}-D_a)/D_a   (EGS Eq. 11/14).
Score (reveal r): bin E by the rung's r; mean(E)(r); zero-crossing r* -> d_perp=|r*-R_S|/ell.
Guards: MINK same-cloud FLAT CONTROL (flat space: sep const -> E~0, no sign change at a fixed r);
relabel stability of r*; no r feedback.

Run:  python3 dev/measure_expansion_horizon.py            # 6 seeds x {3600,7200}
      python3 dev/measure_expansion_horizon.py --smoke    # 2 seeds x {3600}
"""

from __future__ import annotations

import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import generator, thresholds  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402
from explore_ladders import link_future_csr, longest_one_path  # noqa: E402
from explore_direction import order_only_heights, rel_field  # noqa: E402

R_S = thresholds.R_S
KNN = 4            # nearest outgoing neighbours per reference ladder
LMIN = 6           # min ladder length
RBIN = 0.06        # r-bin width for the mean(E)(r) profile


def build_ladders(C, indptr, idx, Lmat, seed, max_starts=500, M=3, lmax=30, budget=3000):
    """Order-only longest fuzzy ladders from sampled link start-rungs. Returns the
    list of p-rail paths (the null tracers)."""
    qs, ps = np.nonzero(Lmat)                      # start rungs p <* q
    rng = np.random.default_rng(seed)
    if qs.size > max_starts:
        sel = rng.choice(qs.size, size=max_starts, replace=False)
        qs, ps = qs[sel], ps[sel]
    ladders = []
    cand_lengths = []                              # INSTRUMENTATION: every candidate's length
    for sp, sq in zip(ps, qs):
        ln, pb, _ = longest_one_path(int(sp), int(sq), indptr, idx, C, M, lmax, budget)
        cand_lengths.append(int(ln))               # recorded for ALL candidates (pre-LMIN)
        if ln >= LMIN:
            ladders.append(pb[:ln].copy())
    return ladders, cand_lengths                   # (computation unchanged; only +cand_lengths)


def sep(u, v, C, Lpast):
    """Order-only transverse separation between spacelike u,v: sqrt of the smallest
    enclosing causal-diamond cardinality. NaN if u,v not spacelike or no diamond."""
    if u == v or C[u, v] or C[v, u]:
        return float("nan")                        # not spacelike (timelike or equal)
    cf = C[:, u] & C[:, v]                          # common future (z with u,v in past)
    cp = C[u, :] & C[v, :]                          # common past
    if not cf.any() or not cp.any():
        return float("nan")
    cfi = np.nonzero(cf)[0]
    f = cfi[np.argmin(Lpast[cfi])]                 # lowest common future
    cpi = np.nonzero(cp)[0]
    e = cpi[np.argmax(Lpast[cpi])]                 # highest common past
    ge_e = C[:, e].copy(); ge_e[e] = True          # z >= e
    le_f = C[f, :].copy(); le_f[f] = True          # z <= f
    return float(np.sqrt(int((ge_e & le_f).sum())))


def expansion_samples(C, emb, seed, ell, mink=False):
    """Return (r_of_rung, E) samples for OUTGOING ladder pairs (EGS Eq.14), plus the
    ingoing-cross-check mean. r revealed ONLY here (scoring)."""
    Lmat, indptr, idx = link_future_csr(C)
    Lpast, Lfut = order_only_heights(C)
    relphi = rel_field(Lfut, Lpast)
    ladders = build_ladders(C, indptr, idx, Lmat, seed)
    if len(ladders) < 2:
        return np.zeros(0), np.zeros(0), float("nan")
    # order-only direction: outgoing = relphi_mean above the median of the sample
    rphi_mean = np.array([float(relphi[p].mean()) for p in ladders])
    out_mask = rphi_mean > np.median(rphi_mean)
    out = [p for p, m in zip(ladders, out_mask) if m]
    ing = [p for p, m in zip(ladders, out_mask) if not m]
    r = emb[:, 1]                                   # TRUTH — score only

    def _pair_E(group):
        rr, EE = [], []
        heads = np.array([p[0] for p in group])
        for i, pI in enumerate(group):
            d0 = np.array([sep(int(pI[0]), int(h), C, Lpast) for h in heads])
            d0[i] = np.nan
            order = np.argsort(np.where(np.isfinite(d0), d0, np.inf))
            for j in order[:KNN]:
                if not np.isfinite(d0[j]):
                    break
                pJ = group[j]
                L = min(len(pI), len(pJ)) - 1
                for a in range(L):
                    Da = sep(int(pI[a]), int(pJ[a]), C, Lpast)
                    Da1 = sep(int(pI[a + 1]), int(pJ[a + 1]), C, Lpast)
                    if np.isfinite(Da) and np.isfinite(Da1) and Da > 0:
                        EE.append((Da1 - Da) / Da)
                        rr.append(float(r[int(pI[a])]))
        return np.array(rr), np.array(EE)

    r_out, E_out = _pair_E(out)
    _, E_in = _pair_E(ing)
    ing_mean = float(np.mean(E_in)) if E_in.size else float("nan")
    return r_out, E_out, ing_mean


def profile(r, E):
    """mean(E) in r-bins; return (bin_centers, mean_E, counts) and the zero-crossing r*."""
    if r.size == 0:
        return np.zeros(0), np.zeros(0), np.zeros(0), float("nan")
    lo, hi = 0.1, 1.3
    edges = np.arange(lo, hi + RBIN, RBIN)
    cen, me, cnt = [], [], []
    for k in range(len(edges) - 1):
        m = (r >= edges[k]) & (r < edges[k + 1])
        if m.sum() >= 5:
            cen.append(0.5 * (edges[k] + edges[k + 1]))
            me.append(float(E[m].mean()))
            cnt.append(int(m.sum()))
    cen, me, cnt = np.array(cen), np.array(me), np.array(cnt)
    # zero-crossing: highest r where mean(E) goes + (above) -> - (below) as r decreases
    rstar = float("nan")
    for k in range(len(cen) - 1):
        if np.isfinite(me[k]) and np.isfinite(me[k + 1]) and me[k] < 0 <= me[k + 1]:
            # linear interp between cen[k] (lower r, neg) and cen[k+1] (higher r, pos)
            t = (0 - me[k]) / (me[k + 1] - me[k])
            rstar = cen[k] + t * (cen[k + 1] - cen[k])
    return cen, me, cnt, rstar


def run(seeds, intensities, t_edge=6.0):
    print("PR-003 Fase #1-B — apparent horizon by discrete-expansion sign change "
          "(order-only, blind)")
    print(f"seeds={len(seeds)}  t_edge={t_edge:.0f}  R_S={R_S}  KNN={KNN}  LMIN={LMIN}\n")
    def _contrast(r, E):
        hi = float(E[r > R_S + 0.1].mean()) if (r > R_S + 0.1).any() else float("nan")
        lo = float(E[r < R_S - 0.1].mean()) if (r < R_S - 0.1).any() else float("nan")
        return hi, lo, (hi - lo)

    for inten in intensities:
        ell = thresholds.ell(inten)
        t0 = time.perf_counter()
        rstars = []
        agg_r, agg_E, agg_r_mk, agg_E_mk = [], [], [], []
        for s in seeds:
            emb, _, _ = generator.numpy_sprinkle(s, float(inten), float(t_edge))
            Cbh = generator.past_matrix_fast(emb, "BH")
            r_out, E_out, _ = expansion_samples(Cbh, emb, s, ell)
            _, _, _, rstar = profile(r_out, E_out)
            rstars.append(rstar)
            agg_r.append(r_out); agg_E.append(E_out)
            Cmk = generator.past_matrix_fast(emb, "MINK")           # flat control, same cloud
            r_mk, E_mk, _ = expansion_samples(Cmk, emb, s, ell, mink=True)
            agg_r_mk.append(r_mk); agg_E_mk.append(E_mk)
        rstars = np.array(rstars, float)
        d_perp = np.abs(rstars - R_S) / ell
        med = lambda a: float(np.nanmedian(a)) if np.isfinite(np.asarray(a, float)).any() else float("nan")
        R_bh = np.concatenate(agg_r) if agg_r else np.zeros(0)
        E_bh = np.concatenate(agg_E) if agg_E else np.zeros(0)
        R_mk = np.concatenate(agg_r_mk) if agg_r_mk else np.zeros(0)
        E_mk = np.concatenate(agg_E_mk) if agg_E_mk else np.zeros(0)
        cen, me, cnt, rstar_pool = profile(R_bh, E_bh)
        cen_mk, me_mk, cnt_mk, rstar_mk = profile(R_mk, E_mk)
        hi_bh, lo_bh, con_bh = _contrast(R_bh, E_bh)
        hi_mk, lo_mk, con_mk = _contrast(R_mk, E_mk)
        print(f"intensity={inten:>6.0f}  ell={ell:.4f}  [{time.perf_counter()-t0:.0f}s]")
        print(f"   BH mean(E) vs r  (expect + for r>R_S, - for r<R_S) | MINK (expect ~flat ~0):")
        mk_lookup = {round(c, 2): m for c, m in zip(cen_mk, me_mk)}
        for c, m, n in zip(cen, me, cnt):
            mark = "  <-- R_S" if abs(c - R_S) < RBIN else ""
            mkv = mk_lookup.get(round(c, 2), float("nan"))
            print(f"      r={c:.2f}  BH={m:+.3f} (n={n:>4})   MINK={mkv:+.3f}{mark}")
        print(f"   zero-crossing r* : BH pooled={rstar_pool:.3f}   per-seed median={med(rstars):.3f}  "
              f"[{np.nanmin(rstars):.3f},{np.nanmax(rstars):.3f}]   (MINK pooled={rstar_mk:.3f})")
        print(f"   d_perp(r*)/ell   : median={med(d_perp):.2f}   (localises R_S={R_S}?)")
        print(f"   expansion contrast  mean(E|r>R_S+.1) - mean(E|r<R_S-.1):")
        print(f"        BH   = {con_bh:+.3f}  ({hi_bh:+.3f} vs {lo_bh:+.3f})")
        print(f"        MINK = {con_mk:+.3f}  ({hi_mk:+.3f} vs {lo_mk:+.3f})")
        flat_pass = np.isfinite(con_bh) and con_bh > 0.05 and (
            not np.isfinite(con_mk) or abs(con_mk) < 0.5 * con_bh)
        print(f"   FLAT CONTROL (structured sign change BH but not MINK): "
              f"{'PASS' if flat_pass else 'FAIL'}\n")


if __name__ == "__main__":
    if "--smoke" in sys.argv:
        run(list(EXPLORE_POOL[:2]), [3600.0])
    else:
        run(list(EXPLORE_POOL[:6]), [3600.0, 7200.0])
