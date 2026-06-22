"""dev feasibility probe (PR-003) — do order-only FUZZY LADDERS (EGS Def 2)
exist and grow long enough, and in WHICH geometry? Committee 2026-06-22.

This answers the gating SWE feasibility question before any PR-003 criterion is
written: EGS needed ~2e5 points / tall boxes and found length-8 fuzzy ladders at
n~1e4 (md:436). Our sealed box is t_edge=6, N<=1.2e4. Here we MEASURE the
fuzzy-ladder length distribution across a small (t_edge, intensity) sweep, ORDER
ONLY (no coordinates enter the search; the embedding is not even read here).

Engine (committee decision): generation + link matrix in verified numpy; the
combinatorial ladder search in a Numba njit kernel (INTEGER only -> deterministic;
to be ported to C++ with a bit-for-bit cross-check if/when PR-003 is sealed).

Fuzzy ladder L^(M)_k (EGS Def 2, md:405): tuples {(p_i,q_i)} with
  1. p_{i-1} <* p_i  (link)      2. q_{i-1} <* q_i  (link)
  3. p_i <* q_i      (rung is a link)
  4. for i>=M:  M-1 <= |[p_{i-M}, p_i]| <= 2M-1
  5. for i>=M:  M-1 <= |[q_{i-M}, q_i]| <= 2M-1
where <* is a covering relation (link) and |[a,b]| the order-interval cardinality.

Run:  python3 dev/explore_ladders.py
"""

from __future__ import annotations

import os
import sys
import time

import numpy as np
from numba import njit

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import generator  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402


# ----------------------------------------------------------------------------
# numpy: past matrix -> link (covering) matrix, future-link CSR adjacency.
# ----------------------------------------------------------------------------
def link_future_csr(C: np.ndarray):
    """L[i,j] (j <* i, j an immediate past of i) = C[i,j] & not exists k: C[i,k]&C[k,j].
    Returns CSR of FUTURE links: for node a, children = {x : L[x,a]} (x covers a).
    indptr[a]:indptr[a+1] -> idx[...] lists those x."""
    Cf = C.astype(np.float32)
    two_step = (Cf @ Cf) > 0.5            # reachable in >=2 steps
    L = C & ~two_step                     # covering relation (transitive reduction)
    # future-link children of a = column a of L (x with L[x,a] True)
    cols = [np.nonzero(L[:, a])[0].astype(np.int64) for a in range(C.shape[0])]
    indptr = np.zeros(C.shape[0] + 1, np.int64)
    for a, c in enumerate(cols):
        indptr[a + 1] = indptr[a] + c.size
    idx = (np.concatenate(cols) if cols else np.zeros(0, np.int64)).astype(np.int64)
    return L, indptr, idx


# ----------------------------------------------------------------------------
# Numba integer kernel: interval cardinality + longest fuzzy ladder via DFS.
# ----------------------------------------------------------------------------
@njit(cache=True)
def _interval_card(a, b, C):
    """|[a,b]| = #{z : a<=z<=b}, a precedes b. C[i,j]=j in past of i (bool)."""
    N = C.shape[0]
    cnt = 0
    for z in range(N):
        ge_a = (z == a) or C[z, a]      # z >= a
        le_b = (z == b) or C[b, z]      # z <= b
        if ge_a and le_b:
            cnt += 1
    return cnt


@njit(cache=True)
def _is_future_link(a, nb, indptr, idx):
    """True iff nb covers a (a <* nb), i.e. nb in future-link children of a."""
    for t in range(indptr[a], indptr[a + 1]):
        if idx[t] == nb:
            return True
    return False


@njit(cache=True)
def _dfs(d, p_path, q_path, indptr, idx, C, M, lmax, budget):
    """Longest fuzzy ladder reachable; d rungs already in p_path/q_path[0:d].
    budget = 1-elem array (node expansions left). Returns max #rungs."""
    best = d
    if d >= lmax or budget[0] <= 0:
        return best
    p_i = p_path[d - 1]
    q_i = q_path[d - 1]
    for ta in range(indptr[p_i], indptr[p_i + 1]):
        np_ = idx[ta]
        for tb in range(indptr[q_i], indptr[q_i + 1]):
            nq = idx[tb]
            if np_ == nq:
                continue
            if not _is_future_link(np_, nq, indptr, idx):   # rung p<*q must be a link
                continue
            ok = True
            if d >= M:                                       # conditions 4,5
                cp = _interval_card(p_path[d - M], np_, C)
                if cp < M - 1 or cp > 2 * M - 1:
                    ok = False
                if ok:
                    cq = _interval_card(q_path[d - M], nq, C)
                    if cq < M - 1 or cq > 2 * M - 1:
                        ok = False
            if ok:
                budget[0] -= 1
                p_path[d] = np_
                q_path[d] = nq
                r = _dfs(d + 1, p_path, q_path, indptr, idx, C, M, lmax, budget)
                if r > best:
                    best = r
                if budget[0] <= 0:
                    return best
    return best


@njit(cache=True)
def _dfs_path(d, p_path, q_path, indptr, idx, C, M, lmax, budget,
              p_best, q_best, best_len):
    if d > best_len[0]:
        best_len[0] = d
        for t in range(d):
            p_best[t] = p_path[t]
            q_best[t] = q_path[t]
    if d >= lmax or budget[0] <= 0:
        return
    p_i = p_path[d - 1]
    q_i = q_path[d - 1]
    for ta in range(indptr[p_i], indptr[p_i + 1]):
        np_ = idx[ta]
        for tb in range(indptr[q_i], indptr[q_i + 1]):
            nq = idx[tb]
            if np_ == nq or not _is_future_link(np_, nq, indptr, idx):
                continue
            ok = True
            if d >= M:
                cp = _interval_card(p_path[d - M], np_, C)
                if cp < M - 1 or cp > 2 * M - 1:
                    ok = False
                if ok:
                    cq = _interval_card(q_path[d - M], nq, C)
                    if cq < M - 1 or cq > 2 * M - 1:
                        ok = False
            if ok:
                budget[0] -= 1
                p_path[d] = np_
                q_path[d] = nq
                _dfs_path(d + 1, p_path, q_path, indptr, idx, C, M, lmax, budget,
                          p_best, q_best, best_len)
                if budget[0] <= 0:
                    return


@njit(cache=True)
def longest_one_path(sp, sq, indptr, idx, C, M, lmax, budget_val):
    """Return (length, p_best, q_best) for a single start rung (sp, sq)."""
    p_path = np.empty(lmax, np.int64)
    q_path = np.empty(lmax, np.int64)
    p_best = np.empty(lmax, np.int64)
    q_best = np.empty(lmax, np.int64)
    best_len = np.zeros(1, np.int64)
    budget = np.empty(1, np.int64)
    budget[0] = budget_val
    p_path[0] = sp
    q_path[0] = sq
    _dfs_path(1, p_path, q_path, indptr, idx, C, M, lmax, budget,
              p_best, q_best, best_len)
    return best_len[0], p_best, q_best


@njit(cache=True)
def longest_ladders(start_p, start_q, indptr, idx, C, M, lmax, per_start_budget):
    """For each starting rung (link) (start_p[s], start_q[s]) return max #rungs."""
    out = np.empty(start_p.size, np.int64)
    p_path = np.empty(lmax, np.int64)
    q_path = np.empty(lmax, np.int64)
    budget = np.empty(1, np.int64)
    for s in range(start_p.size):
        p_path[0] = start_p[s]
        q_path[0] = start_q[s]
        budget[0] = per_start_budget
        out[s] = _dfs(1, p_path, q_path, indptr, idx, C, M, lmax, budget)
    return out


# ----------------------------------------------------------------------------
def sample_start_rungs(L, max_starts, rng):
    """Starting rungs = links p<*q -> (p, q) with L[q,p]. Sample up to max_starts."""
    qs, ps = np.nonzero(L)        # L[q,p] True => p <* q ; here rows=q, cols=p
    if qs.size > max_starts:
        sel = rng.choice(qs.size, size=max_starts, replace=False)
        qs, ps = qs[sel], ps[sel]
    return ps.astype(np.int64), qs.astype(np.int64)


def probe(seed, intensity, t_edge, M=3, lmax=30, max_starts=1000,
          per_start_budget=3000):
    emb, _, _ = generator.numpy_sprinkle(seed, intensity, t_edge)
    N = emb.shape[0]
    C = generator.past_matrix_fast(emb, "BH")
    L, indptr, idx = link_future_csr(C)
    n_links = int(L.sum())
    rng = np.random.default_rng(seed)
    sp, sq = sample_start_rungs(L, max_starts, rng)
    if sp.size == 0:
        return dict(N=N, n_links=n_links, n_starts=0, maxlen=0, ge6=0, ge8=0)
    lens = longest_ladders(sp, sq, indptr, idx, C, M, lmax, per_start_budget)
    return dict(N=N, n_links=n_links, n_starts=int(sp.size),
                maxlen=int(lens.max()), mean=float(lens.mean()),
                ge6=int((lens >= 6).sum()), ge8=int((lens >= 8).sum()))


def selftest():
    """Verify primitives on a tiny hand poset: chain 0<1<2<3 (C[i,j]=j in past i)."""
    C = np.zeros((4, 4), bool)
    for i in range(4):
        for j in range(i):
            C[i, j] = True            # j<i totally ordered
    assert _interval_card(0, 3, C) == 4 and _interval_card(1, 2, C) == 2
    L, indptr, idx = link_future_csr(C)
    # covering links only: 0<*1,1<*2,2<*3
    assert int(L.sum()) == 3 and _is_future_link(0, 1, indptr, idx) \
        and not _is_future_link(0, 2, indptr, idx)
    print("selftest OK: interval card + link matrix correct on the 4-chain")


def run():
    selftest()
    print("\nFUZZY LADDER feasibility (M=3; ORDER-ONLY; coords NOT used)\n")
    seeds = EXPLORE_POOL[:3]
    # vary box HEIGHT at matched density (intensity ~ 500 * t_edge * R_EDGE):
    # isolates "do ladders get longer in a taller patch?" (the gating question).
    grid = [(6, 3600), (12, 7200), (25, 15000)]   # (t_edge, intensity), rho~500
    hdr = f"{'t_edge':>6} {'inten':>6} {'N':>6} {'links':>7} {'starts':>6} {'maxlen':>6} {'mean':>5} {'>=6':>4} {'>=8':>4}"
    print(hdr)
    for t_edge, inten in grid:
        agg = []
        t0 = time.perf_counter()
        for s in seeds:
            agg.append(probe(s, float(inten), float(t_edge)))
        dt = time.perf_counter() - t0
        N = int(np.mean([a["N"] for a in agg]))
        links = int(np.mean([a["n_links"] for a in agg]))
        starts = int(np.mean([a["n_starts"] for a in agg]))
        maxlen = max(a["maxlen"] for a in agg)
        mean = float(np.mean([a["mean"] for a in agg if "mean" in a]))
        ge6 = sum(a["ge6"] for a in agg)
        ge8 = sum(a["ge8"] for a in agg)
        print(f"{t_edge:>6} {inten:>6} {N:>6} {links:>7} {starts:>6} {maxlen:>6} "
              f"{mean:>5.2f} {ge6:>4} {ge8:>4}   ({dt:.1f}s/{len(seeds)} seeds)")


if __name__ == "__main__":
    run()
