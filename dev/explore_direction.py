"""dev exploration (PR-003 #2) — can an ORDER-ONLY rule tell an OUTGOING fuzzy
ladder from an INGOING one? EGS used the coordinate slope; we must not.

Hypothesis: the longest-future-chain field phi(e) = L_fut(e) is EGS's
interior/exterior diagnostic (md:463: interior short, exterior long). A ladder
moving OUTWARD (toward the exterior) should gain "exteriority" -> phi rises along
it; an INGOING ladder loses it. We build ladders ORDER ONLY, compute order-only
trend features of phi along them, then REVEAL coordinates only to SCORE: the true
direction is sign(delta r) along the ladder (r rises = outward). If an order-only
feature predicts the true direction, #2 is solvable.

Ladder builder is ITERATIVE greedy (njit while-loop) -> no recursion, no segfault
(= the C++-portable form). Coords are used ONLY for the truth label, never to
build ladders or compute features.

Run:  python3 dev/explore_direction.py
"""

from __future__ import annotations

import os
import sys

import numpy as np
from numba import njit

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import estimator, generator, thresholds  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402
import explore_ladders as XL  # noqa: E402

R_S = thresholds.R_S


@njit(cache=True)
def greedy_ladder(sp, sq, indptr, idx, C, M, lmax):
    """Iterative greedy fuzzy ladder from start rung (sp,sq): extend by the FIRST
    valid (Def-2-satisfying) next rung until stuck. Returns (length, p_path)."""
    p_path = np.empty(lmax, np.int64)
    q_path = np.empty(lmax, np.int64)
    p_path[0] = sp
    q_path[0] = sq
    d = 1
    while d < lmax:
        p_i = p_path[d - 1]
        q_i = q_path[d - 1]
        found = False
        for ta in range(indptr[p_i], indptr[p_i + 1]):
            np_ = idx[ta]
            for tb in range(indptr[q_i], indptr[q_i + 1]):
                nq = idx[tb]
                if np_ == nq or not XL._is_future_link(np_, nq, indptr, idx):
                    continue
                if d >= M:
                    cp = XL._interval_card(p_path[d - M], np_, C)
                    if cp < M - 1 or cp > 2 * M - 1:
                        continue
                    cq = XL._interval_card(q_path[d - M], nq, C)
                    if cq < M - 1 or cq > 2 * M - 1:
                        continue
                p_path[d] = np_
                q_path[d] = nq
                d += 1
                found = True
                break
            if found:
                break
        if not found:
            break
    return d, p_path


def order_only_heights(C):
    """Lpast(e), Lfut(e): longest chain ending at / starting from e. Order-only."""
    _, _, Lfut = estimator.estimate_O(C)                  # future-first DP (reused)
    N = C.shape[0]
    order = estimator._topological_future_first(C)         # sinks first
    Lpast = np.zeros(N, dtype=np.int64)
    for e in reversed(order):                             # sources first
        past = np.nonzero(C[e])[0]
        Lpast[e] = 1 + (int(Lpast[past].max()) if past.size else 0)
    return Lpast, Lfut.astype(np.int64)


def rel_field(field, level):
    """field(e) minus the mean field over elements sharing the same level value
    (order-only 'exteriority relative to time-depth')."""
    rel = field.astype(float).copy()
    for lv in np.unique(level):
        m = level == lv
        rel[m] = field[m] - field[m].mean()
    return rel


def collect_ladders(seed, intensity, t_edge, min_len=6, n_starts=600, lmax=25):
    emb, _, _ = generator.numpy_sprinkle(seed, intensity, t_edge)
    C = generator.past_matrix_fast(emb, "BH")
    Lpast, Lfut = order_only_heights(C)
    rel_phi = rel_field(Lfut, Lpast)
    L, indptr, idx = XL.link_future_csr(C)
    qs, ps = np.nonzero(L)
    rng = np.random.default_rng(seed)
    sel = rng.choice(qs.size, size=min(n_starts, qs.size), replace=False)
    rows = []
    for k in sel:
        ln, pb = greedy_ladder(int(ps[k]), int(qs[k]), indptr, idx, C, 3, lmax)
        if ln < min_len:
            continue
        p = pb[:ln]
        phi = Lfut[p].astype(float)
        rphi = rel_phi[p]
        i = np.arange(ln, dtype=float)
        f_phi_slope = float(np.polyfit(i, phi, 1)[0])
        f_relphi_slope = float(np.polyfit(i, rphi, 1)[0])
        f_relphi_mean = float(rphi.mean())
        r = emb[p, 1]                                      # TRUTH (score only)
        dir_true = np.sign(r[-1] - r[0])
        mean_r = float(r.mean())
        rows.append((f_phi_slope, f_relphi_slope, f_relphi_mean,
                     dir_true, mean_r, ln))
    return rows


def auc(score, label_pos):
    s = np.asarray(score, float)
    y = np.asarray(label_pos, bool)
    if y.all() or (~y).all():
        return float("nan")
    order = np.argsort(s)
    ranks = np.empty(s.size, float)
    ranks[order] = np.arange(1, s.size + 1)
    n_pos = y.sum()
    n_neg = (~y).sum()
    return float((ranks[y].sum() - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg))


def run():
    print("PR-003 #2: ORDER-ONLY outgoing-vs-ingoing direction test")
    print("features from L_fut field only; truth = sign(delta r); coords only score\n")
    seeds = EXPLORE_POOL[:4]
    for t_edge, inten in [(12.0, 4000.0), (25.0, 9000.0)]:
        allrows = []
        for s in seeds:
            allrows += collect_ladders(s, inten, t_edge)
        if not allrows:
            print(f"t_edge={t_edge}: no ladders >= min_len"); continue
        a = np.array([r[:3] for r in allrows], float)
        dir_true = np.array([r[3] for r in allrows])
        mean_r = np.array([r[4] for r in allrows])
        pos = dir_true > 0
        near = np.abs(mean_r - R_S) < 0.15
        print(f"--- t_edge={t_edge:.0f} inten={inten:.0f} --- ladders={len(allrows)} "
              f"(outward {int(pos.sum())} / inward {int((~pos).sum())}); "
              f"near-horizon {int(near.sum())}")
        for j, name in enumerate(["phi_slope", "relphi_slope", "relphi_mean"]):
            print(f"   {name:<13} AUC(all)={auc(a[:, j], pos):.3f}   "
                  f"AUC(near-horiz)={auc(a[near, j], pos[near]):.3f}   "
                  f"mean(out)={a[pos, j].mean():+.3f} mean(in)={a[~pos, j].mean():+.3f}")
        print()


if __name__ == "__main__":
    run()
