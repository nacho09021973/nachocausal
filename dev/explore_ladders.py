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


# --- ITERATIVE longest-fuzzy-ladder kernel (explicit stack) ----------------
# Replaces the recursive _dfs/_dfs_path (Numba njit recursion SIGSEGVs on the
# real BH posets even at modest depth). Verified bit-for-bit vs the recursive
# kernel (lengths AND paths) over M in {2,3,4}, lmax<=40, budget in {5..3000};
# selftest() carries a hand-checked len-3 ladder as the standing oracle.
@njit(cache=True)
def _one_iter(sp, sq, indptr, idx, C, M, lmax, budget_val, want_path):
    """Single start rung (sp, sq). Returns (best_len, p_best, q_best).
    Faithful explicit-stack simulation of the recursive _dfs / _dfs_path:
      - identical DFS visit order (ta outer, tb inner);
      - budget decremented at the exact accept point, shared across the search;
      - best path recorded at frame ENTRY on strict improvement (first reach).
    want_path=False skips path bookkeeping (length-only, used by longest_ladders).
    """
    p_path = np.empty(lmax, np.int64)
    q_path = np.empty(lmax, np.int64)
    p_best = np.empty(lmax, np.int64)
    q_best = np.empty(lmax, np.int64)
    # frame stack: depth fd[top], and the next loop cursor (fta[top], ftb[top])
    fd = np.empty(lmax, np.int64)
    fta = np.empty(lmax, np.int64)
    ftb = np.empty(lmax, np.int64)

    budget = budget_val
    best_len = 0

    p_path[0] = sp
    q_path[0] = sq

    # push + ENTER root frame d = 1
    top = 0
    fd[0] = 1
    fta[0] = indptr[sp]
    ftb[0] = indptr[sq]
    if 1 > best_len:                       # root entry recording (d = 1)
        best_len = 1
        if want_path:
            p_best[0] = p_path[0]
            q_best[0] = q_path[0]

    while top >= 0:
        d = fd[top]
        # entry guards, == recursion's `if d >= lmax or budget <= 0: return`
        if budget <= 0 or d >= lmax:
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
                if np_ != nq and _is_future_link(np_, nq, indptr, idx):
                    ok = True
                    if d >= M:                              # conditions 4, 5
                        cp = _interval_card(p_path[d - M], np_, C)
                        if cp < M - 1 or cp > 2 * M - 1:
                            ok = False
                        if ok:
                            cq = _interval_card(q_path[d - M], nq, C)
                            if cq < M - 1 or cq > 2 * M - 1:
                                ok = False
                    accept = ok
                if accept:
                    # save resume cursor = NEXT pair within this frame
                    fta[top] = ta
                    ftb[top] = tb + 1
                    # accept node: decrement shared budget, extend the path
                    budget -= 1
                    p_path[d] = np_
                    q_path[d] = nq
                    # push + ENTER child frame d + 1
                    top += 1
                    fd[top] = d + 1
                    fta[top] = indptr[np_]      # child p_i = p_path[d] = np_
                    ftb[top] = indptr[nq]        # child q_i = q_path[d] = nq
                    if (d + 1) > best_len:       # child entry recording
                        best_len = d + 1
                        if want_path:
                            for t in range(d + 1):
                                p_best[t] = p_path[t]
                                q_best[t] = q_path[t]
                    advanced = True
                    break
                tb += 1
            if advanced:
                break
            ta += 1
            tb = indptr[q_i]                     # reset inner loop for next ta
        if not advanced:
            top -= 1                             # frame loop exhausted -> return
    return best_len, p_best, q_best


@njit(cache=True)
def longest_one_path(sp, sq, indptr, idx, C, M, lmax, budget_val):
    """Return (length, p_best, q_best) for a single start rung (sp, sq).
    Only p_best[:length], q_best[:length] are meaningful (same as before)."""
    return _one_iter(sp, sq, indptr, idx, C, M, lmax, budget_val, True)


@njit(cache=True)
def longest_ladders(start_p, start_q, indptr, idx, C, M, lmax, per_start_budget):
    """For each starting rung (start_p[s], start_q[s]) return max #rungs."""
    out = np.empty(start_p.size, np.int64)
    for s in range(start_p.size):
        bl, _, _ = _one_iter(start_p[s], start_q[s], indptr, idx, C, M, lmax,
                             per_start_budget, False)
        out[s] = bl
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

    # --- ladder kernel on a hand-checked 2-chain ladder (oracle-confirmed) ----
    # nodes 0=p0 1=p1 2=p2 3=q0 4=q1 5=q2 6=z; the parallel chains p0<*p1<*p2,
    # q0<*q1<*q2 with rungs p_i<*q_i form a fuzzy ladder of length 3. Node z sits
    # p0<*z<*p2 (off the p1 line) inflating |[p0,p2]| to 4, so at M=2 conditions
    # 4-5 REJECT the i=2 rung (length 3 -> 2); at M=4 they never fire (length 3).
    # This is the only kernel coverage once the recursive oracle is gone, so it
    # exercises link-chaining, the rung-link test, AND interval-card accept/reject.
    edges = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5), (0, 6), (6, 2)]
    less = np.zeros((7, 7), bool)
    for a, b in edges:
        less[a, b] = True
    for _ in range(7):                       # transitive closure
        for k in range(7):
            for i in range(7):
                if less[i, k]:
                    less[i] |= less[k]
    Cl = np.zeros((7, 7), bool)
    for i in range(7):
        for j in range(7):
            if less[j, i]:
                Cl[i, j] = True              # j in past of i
    assert _interval_card(0, 2, Cl) == 4 and _interval_card(3, 5, Cl) == 3
    Ll, ipl, ixl = link_future_csr(Cl)
    assert int(Ll.sum()) == 9
    sp = np.array([0, 1, 2]); sq = np.array([3, 4, 5])     # start rungs p_i<*q_i
    assert list(longest_ladders(sp, sq, ipl, ixl, Cl, 4, 20, 100000)) == [3, 2, 1]
    assert list(longest_ladders(sp, sq, ipl, ixl, Cl, 2, 20, 100000)) == [2, 2, 1]
    Lp, _, _ = longest_one_path(0, 3, ipl, ixl, Cl, 4, 20, 100000)
    assert Lp == 3
    print("selftest OK: interval card + link matrix (4-chain) + ladder kernel "
          "(len-3 ladder, M=2 interval-card rejection) all correct")


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
