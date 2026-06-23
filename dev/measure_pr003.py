"""dev measurement (PR-003, commissioned 2026-06-23) — produce the numbers the
membrane-reframe argument PRESUPPOSES but that were never measured:

  #1 RELABELING EQUIVARIANCE.  Is the reconstruction a function of the abstract
     poset, or of the arbitrary element labels?  Measured two ways:
       - selection invariance: does the order-only bracket seed set (mapped back
         to original labels) survive a random relabel P C P^T?
       - length invariance: does the longest bracket-seeded ladder length survive?
     Insight: estimate_O_volume is already permutation-invariant; label-dependence
     enters only via boundary_minimals' argsort TIE-break and via the kernel's
     "first path" / censored best_len.  A COMPLETE longest search is length-
     invariant; a budget/lmax-bound one is NOT -> #2 and #1 are the same wound.

  #2 CENSORING.  The kernel returns the best length found.  Here it ALSO reports
     complete / budget_hit / lmax_hit / states, so "longest" is only called
     longest when complete=True; otherwise it is a LOWER BOUND.

  #3 LOCALISATION BY POSITION.  d_perp = |r - R_S| per rung, split into first-3
     vs the tail, for the GREEDY-first and the LONGEST bracket-seeded ladder.
     Tests directly: does longest help localisation, and does the tail drift?

Order-only throughout: coordinates enter ONLY to score d_perp (never to seed,
build, or select).  Aggregation is PER-SPRINKLING (one summary per seed), never
per-ladder, then median + IQR across the 40 EXPLORE_POOL seeds.

Run:  python3 dev/measure_pr003.py            # full 40-seed measurement
      python3 dev/measure_pr003.py --smoke    # 3 seeds, fast self-check
"""

from __future__ import annotations

import os
import sys
import time

import numpy as np
from numba import njit

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import estimator, generator, thresholds  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402
import explore_ladders as XL  # noqa: E402
from explore_direction import greedy_ladder, order_only_heights  # noqa: E402

R_S = thresholds.R_S


# ----------------------------------------------------------------------------
# #2 — CENSORED longest-fuzzy-ladder kernel.  Same DFS as XL._one_iter, but it
# tracks WHY the search stopped, so best_len can be tagged complete vs bound.
#   complete  : the whole tree under (sp,sq) was exhausted (no budget/lmax cut)
#   budget_hit: budget reached 0 with frames still pending  -> best_len is a LB
#   lmax_hit  : some frame was pruned at d>=lmax             -> best_len is a LB
#   states    : #accepted nodes (search size)
# best_len is INVARIANT under relabeling iff complete=True (the tie-break on the
# best PATH may still differ; lengths do not once the search completes).
# ----------------------------------------------------------------------------
@njit(cache=True)
def longest_censored(sp, sq, indptr, idx, C, M, lmax, budget_val):
    p_path = np.empty(lmax, np.int64)
    q_path = np.empty(lmax, np.int64)
    p_best = np.empty(lmax, np.int64)
    q_best = np.empty(lmax, np.int64)
    fd = np.empty(lmax, np.int64)
    fta = np.empty(lmax, np.int64)
    ftb = np.empty(lmax, np.int64)

    budget = budget_val
    best_len = 0
    states = 0
    budget_hit = 0
    lmax_hit = 0

    p_path[0] = sp
    q_path[0] = sq
    top = 0
    fd[0] = 1
    fta[0] = indptr[sp]
    ftb[0] = indptr[sq]
    best_len = 1
    p_best[0] = p_path[0]
    q_best[0] = q_path[0]

    while top >= 0:
        d = fd[top]
        if budget <= 0:
            budget_hit = 1          # stopped with a frame still pending
            break
        if d >= lmax:
            lmax_hit = 1            # this branch could have gone deeper
            top -= 1
            continue
        p_i = p_path[d - 1]
        q_i = q_path[d - 1]
        ta = fta[top]
        tb = ftb[top]
        advanced = False
        while ta < indptr[p_i + 1]:
            np_ = idx[ta]
            while tb < indptr[q_i + 1]:
                nq = idx[tb]
                accept = False
                if np_ != nq and XL._is_future_link(np_, nq, indptr, idx):
                    ok = True
                    if d >= M:
                        cp = XL._interval_card(p_path[d - M], np_, C)
                        if cp < M - 1 or cp > 2 * M - 1:
                            ok = False
                        if ok:
                            cq = XL._interval_card(q_path[d - M], nq, C)
                            if cq < M - 1 or cq > 2 * M - 1:
                                ok = False
                    accept = ok
                if accept:
                    fta[top] = ta
                    ftb[top] = tb + 1
                    budget -= 1
                    states += 1
                    p_path[d] = np_
                    q_path[d] = nq
                    top += 1
                    fd[top] = d + 1
                    fta[top] = indptr[np_]
                    ftb[top] = indptr[nq]
                    if (d + 1) > best_len:
                        best_len = d + 1
                        for t in range(d + 1):
                            p_best[t] = p_path[t]
                            q_best[t] = q_path[t]
                    advanced = True
                    break
                tb += 1
            if advanced:
                break
            ta += 1
            tb = indptr[q_i]
        if not advanced:
            top -= 1
    complete = 1 if (budget_hit == 0 and lmax_hit == 0) else 0
    return best_len, complete, budget_hit, lmax_hit, states, p_best, q_best


# ----------------------------------------------------------------------------
# #1 — order-only bracket seed set, in TWO variants.
# ----------------------------------------------------------------------------
def boundary_minimals_current(C, k_side=6):
    """The CURRENT rule (explore_seed_bracket.boundary_minimals): exactly k_side
    each side, chosen by np.argsort -> TIE-break by arbitrary index."""
    O_by_min, min_idx = estimator.estimate_O_volume(C)
    mins = np.array(min_idx)
    O = np.array([O_by_min[i] for i in min_idx], float)
    thr, _ = estimator.two_means_split(list(O))
    low, low_O = mins[O < thr], O[O < thr]
    high, high_O = mins[O >= thr], O[O >= thr]
    if low.size == 0 or high.size == 0:
        return np.zeros(0, np.int64)
    lo_b = low[np.argsort(low_O)[-k_side:]]
    hi_b = high[np.argsort(high_O)[:k_side]]
    return np.concatenate([lo_b, hi_b]).astype(np.int64)


def boundary_minimals_invariant(C, k_side=6):
    """TIE-COMPLETE, label-invariant variant: take the k_side-th O value from
    each side as a THRESHOLD and return EVERY minimal at or beyond it. With ties
    at the cut this returns >= k_side per side, but the set is a function of the
    O-multiset alone -> invariant under relabeling. (Proposed fix #4/#1.)"""
    O_by_min, min_idx = estimator.estimate_O_volume(C)
    mins = np.array(min_idx)
    O = np.array([O_by_min[i] for i in min_idx], float)
    thr, _ = estimator.two_means_split(list(O))
    low, low_O = mins[O < thr], O[O < thr]
    high, high_O = mins[O >= thr], O[O >= thr]
    if low.size == 0 or high.size == 0:
        return np.zeros(0, np.int64)
    lo_cut = np.sort(low_O)[-min(k_side, low_O.size)]      # k-th highest on low side
    hi_cut = np.sort(high_O)[min(k_side, high_O.size) - 1]  # k-th lowest on high side
    lo_b = low[low_O >= lo_cut]
    hi_b = high[high_O <= hi_cut]
    sel = np.concatenate([lo_b, hi_b]).astype(np.int64)
    return np.sort(sel)                                    # sorted -> canonical


def relabel(C, emb, rng):
    """Return (C2, emb2, inv) for a random relabel: new label of old i is perm[i],
    C2[perm[i],perm[j]] = C[i,j]; inv maps new label -> old label."""
    n = C.shape[0]
    perm = rng.permutation(n)
    inv = np.argsort(perm)
    C2 = C[np.ix_(inv, inv)]
    emb2 = emb[inv]
    return np.ascontiguousarray(C2), np.ascontiguousarray(emb2), inv


# ----------------------------------------------------------------------------
# reconstruction over one sprinkling: bracket-seed -> greedy & longest ladders.
# ----------------------------------------------------------------------------
def reconstruct(C, select, M=3, lmax=120, budget=30000, min_len=6):
    """For every bracket seed rung (m, child): build the greedy ladder and the
    censored-longest ladder.  Returns a dict of per-ladder arrays (p-paths,
    lengths, completeness) and the seed set, all in C's own labels."""
    L, indptr, idx = XL.link_future_csr(C)
    bmin = select(C)
    g_paths, l_paths, l_len, l_complete = [], [], [], []
    for m in bmin:
        for t in range(indptr[m], indptr[m + 1]):
            q1 = int(idx[t])
            gln, gpb = greedy_ladder(int(m), q1, indptr, idx, C, M, lmax)
            bl, comp, _, _, _, lpb, _ = longest_censored(
                int(m), q1, indptr, idx, C, M, lmax, budget)
            if gln >= min_len:
                g_paths.append(gpb[:gln].copy())
            if bl >= min_len:
                l_paths.append(lpb[:bl].copy())
                l_len.append(int(bl))
                l_complete.append(int(comp))
    return dict(seed_set=set(int(x) for x in bmin),
                g_paths=g_paths, l_paths=l_paths,
                l_len=np.array(l_len, int), l_complete=np.array(l_complete, int))


def dperp_profile(paths, emb, ell):
    """Per-ladder (first3, tail) median d_perp/ell, pooled over ladders of a
    sprinkling.  first3 = rungs 0..2 ; tail = rungs 3.. .  Returns (first3, tail,
    overall) medians in ell units, or nan if absent."""
    first, tail, alld = [], [], []
    for p in paths:
        d = np.abs(emb[p, 1] - R_S) / ell
        alld.extend(d.tolist())
        first.extend(d[:3].tolist())
        tail.extend(d[3:].tolist())
    med = lambda a: float(np.median(a)) if a else float("nan")
    return med(first), med(tail), med(alld)


# ----------------------------------------------------------------------------
def measure_seed(seed, intensity, t_edge, k_relabel=3):
    emb, _, _ = generator.numpy_sprinkle(seed, float(intensity), float(t_edge))
    C = generator.past_matrix_fast(emb, "BH")
    ell = thresholds.ell(intensity)

    rec = reconstruct(C, boundary_minimals_current)
    g1, gt, ga = dperp_profile(rec["g_paths"], emb, ell)
    l1, lt, la = dperp_profile(rec["l_paths"], emb, ell)
    n_long = rec["l_len"].size
    complete_frac = (float(rec["l_complete"].mean()) if n_long else float("nan"))
    best_len = int(rec["l_len"].max()) if n_long else 0
    best_complete = (int(rec["l_complete"][int(np.argmax(rec["l_len"]))])
                     if n_long else -1)

    # #1 equivariance: relabel k times, compare seed set (current) + best length.
    rng = np.random.default_rng(seed ^ 0x5151)
    sel_curr_viol = sel_inv_viol = len_viol = 0
    base_set_inv = reconstruct(C, boundary_minimals_invariant)["seed_set"]
    for _ in range(k_relabel):
        C2, emb2, inv = relabel(C, emb, rng)
        r2c = reconstruct(C2, boundary_minimals_current)
        r2i_set = reconstruct(C2, boundary_minimals_invariant)["seed_set"]
        # map new labels back to original
        back_curr = set(int(inv[s]) for s in r2c["seed_set"])
        back_inv = set(int(inv[s]) for s in r2i_set)
        if back_curr != rec["seed_set"]:
            sel_curr_viol += 1
        if back_inv != base_set_inv:
            sel_inv_viol += 1
        bl2 = int(r2c["l_len"].max()) if r2c["l_len"].size else 0
        if bl2 != best_len:
            len_viol += 1

    return dict(seed=seed, N=emb.shape[0], n_long=n_long,
                g_first3=g1, g_tail=gt, g_all=ga,
                l_first3=l1, l_tail=lt, l_all=la,
                best_len=best_len, best_complete=best_complete,
                complete_frac=complete_frac,
                sel_curr_viol=sel_curr_viol, sel_inv_viol=sel_inv_viol,
                len_viol=len_viol, k_relabel=k_relabel)


def _agg(rows, key):
    v = np.array([r[key] for r in rows if np.isfinite(r[key])], float)
    if v.size == 0:
        return float("nan"), float("nan"), float("nan")
    return float(np.median(v)), float(np.percentile(v, 25)), float(np.percentile(v, 75))


def run(seeds, intensity=3600.0, t_edge=6.0, k_relabel=3):
    print(f"PR-003 measurement  seeds={len(seeds)}  intensity={intensity:.0f}  "
          f"t_edge={t_edge:.0f}  ell={thresholds.ell(intensity):.4f}  "
          f"k_relabel={k_relabel}\n")
    rows = []
    for s in seeds:
        t0 = time.perf_counter()
        r = measure_seed(s, intensity, t_edge, k_relabel)
        rows.append(r)
        print(f"  seed={s} N={r['N']} nLong={r['n_long']:>2} "
              f"best_len={r['best_len']:>3}({'C' if r['best_complete']==1 else 'LB'}) "
              f"compl={r['complete_frac']:.2f}  "
              f"GREEDY d_perp/ell first3={r['g_first3']:.2f} tail={r['g_tail']:.2f}  "
              f"LONG first3={r['l_first3']:.2f} tail={r['l_tail']:.2f}  "
              f"viol[selCur/selInv/len]={r['sel_curr_viol']}/{r['sel_inv_viol']}/{r['len_viol']} "
              f"[{time.perf_counter()-t0:.1f}s]")

    print("\n=== AGGREGATE (median [IQR] across seeds; per-sprinkling) ===")
    for key, lbl in [("g_first3", "GREEDY first-3 d_perp/ell"),
                     ("g_tail", "GREEDY tail   d_perp/ell"),
                     ("l_first3", "LONGEST first-3 d_perp/ell"),
                     ("l_tail", "LONGEST tail   d_perp/ell"),
                     ("complete_frac", "longest complete fraction"),
                     ("best_len", "best longest length")]:
        m, lo, hi = _agg(rows, key)
        print(f"  {lbl:<28} {m:.3f}  [{lo:.3f}, {hi:.3f}]")
    nseed = len(rows) * k_relabel
    sc = sum(r["sel_curr_viol"] for r in rows)
    si = sum(r["sel_inv_viol"] for r in rows)
    lv = sum(r["len_viol"] for r in rows)
    bc = sum(1 for r in rows if r["best_complete"] == 1)
    print(f"\n  RELABEL trials = {nseed} ({len(rows)} seeds x {k_relabel})")
    print(f"  selection-set violations  CURRENT  = {sc}/{nseed}  ({sc/nseed:.0%})")
    print(f"  selection-set violations  INVARIANT= {si}/{nseed}  ({si/nseed:.0%})")
    print(f"  best-length violations    CURRENT  = {lv}/{nseed}  ({lv/nseed:.0%})")
    print(f"  best-longest COMPLETE     = {bc}/{len(rows)} seeds "
          f"(rest are lower bounds)")
    return rows


if __name__ == "__main__":
    smoke = "--smoke" in sys.argv
    pool = EXPLORE_POOL[:3] if smoke else EXPLORE_POOL
    run(list(pool), k_relabel=(2 if smoke else 3))
