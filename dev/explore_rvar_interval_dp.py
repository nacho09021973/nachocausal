#!/usr/bin/env python
"""EXPLORATION PROTOTYPE -- polynomial interval-DP candidate for the R-VAR selector.

STATUS: dev/ exploration, NOT Gate-0-verified, NOT authorized for any mu computation or
scoring. Its production-scale outputs below are CLAIM-INERT (timing/existence demo only).
The ONLY verified statement this script makes is Part 1's exact match against the
committed Gate 0 Tier 0 reference (dev/measure_pr003_rvar_gate0.py) on its own toy poset.

Mathematical content (candidate resolution of comité 019's blocker -- the falsifier's
"it is unproven a polynomial algorithm for max_{D in A(C)} S exists at all"):

  1. MODULARITY. For any down-set D, both A(D) and B(D) are modular:
     A(D) = sum_{v in D} a_v, B(D) = sum_{v in D} b_v, with
       a_v = sum_{v covered-by y} (d+v - d+y) - sum_{x covered-by v... } -- precisely:
       a_v = d+_v*outdeg(v) - sum_{y: v<|y} d+_y - sum_{x: x<|v} d+_x + d+_v*indeg(v),
       b_v = outdeg(v) - indeg(v)  (Hasse degrees).
     Proof: for a down-set, a cover edge (x,y) crosses iff x in D, y not in D, and
     z_x*z_y = z_y, so [x in D][y not in D] = z_x - z_y; telescoping per element.
     (This is the same linearization gate0's maxflow_mincut_closure already uses --
     the c_z there equals q*a_v - p*b_v here.)

  2. REPARAMETRIZATION. A(C)-members are exactly D = downset(M) for M subset of Max(C),
     so v in D iff I_v := {m in Max : v <= m} meets M.

  3. INTERVAL STRUCTURE (2D orders). In the posets this project generates (1+1D
     sprinklings), I_v is a CONTIGUOUS INTERVAL of Max(C) sorted by a null coordinate
     (measured: 0 violations in 24/24 production-scale dev draws, MINK under u=t-r and
     BH under p=t+r -- dev/rvar_structure_probe_result.json). The property is CERTIFIED
     PER DRAW in O(N*K) before solving; on failure this prototype raises (a production
     version would emit a typed abstention, keeping the guardrail falsifiable).

  4. GAP-DP. With intervals, max_M sum_{v covered} c_v subject to (i) M nonempty,
     (ii) some minimal element uncovered ((C-D) & Min != empty; note downset(Max)=C so
     this also enforces D != C), is a classic O(K^2) gap DP over the sorted antichain:
     minimize the c-weight of elements whose whole interval falls in a "gap" between
     consecutive selected antichain positions. Lexicographic tie-break toward maximal
     covered B handles the (A,B)=(0,0) boundary-tie degeneracy gate0 documented (any D
     with H = empty has objective exactly 0 at every lambda, so whenever a feasible
     optimum with B >= 1 exists the tie-break finds it). H != empty (= B >= 1) is then
     asserted on the argmax. Dinkelbach over exact Fractions drives the ratio.

Complexity: O(N^2) dominated by the Hasse cover computation (vectorized boolean-matmul
transitive reduction); the DP itself is O(K^2) per Dinkelbach iteration, K = |Max(C)|.
Replaces the 2^K enumerate-and-filter of the only Gate-0-verified implementation
(2^40 at production MINK; 2^426 at production BH).

Run: PYTHONPATH=. .venv/bin/python dev/explore_rvar_interval_dp.py
Output: dev/rvar_interval_dp_result.json (+ this stdout log).
"""
from __future__ import annotations

import json
import os
import sys
import time
from fractions import Fraction

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from measure_pr003_rvar_gate0 import (  # noqa: E402  (committed Gate 0 reference)
    PI as TOY_PI,
    build_poset,
    family_A,
    is_cover,
    maximal_elements,
    minimal_elements,
)

from nachocausal import generator, thresholds  # noqa: E402

RESULT_PATH = os.path.join(os.path.dirname(__file__), "rvar_interval_dp_result.json")
DEV_SEED = 20240617


# =============================================================================
# Core: intervals + modular coefficients + lexicographic gap-DP + Dinkelbach.
# Input convention matches past_matrix_fast: C[i, j] == (j strictly precedes i).
# =============================================================================
def hasse_covers(C: np.ndarray) -> np.ndarray:
    """W[x, y] = (x covered-by y), via boolean-matmul transitive reduction."""
    rel = C.T  # rel[x, y] = x strictly below y
    rel_f = rel.astype(np.float32)
    return rel & ~((rel_f @ rel_f) > 0.5)


def solve(C: np.ndarray, max_sort_key: np.ndarray) -> dict:
    """Exact max of S = A/B over A(C), assuming (and certifying) the interval property.
    Returns dict with status OK / EMPTY_FAMILY, and on OK: lam (Fraction), D (bool mask),
    A, B, iters."""
    n = C.shape[0]
    maximal = np.flatnonzero(~C.any(axis=0))
    minimal_mask = ~C.any(axis=1)
    order = maximal[np.argsort(max_sort_key)]
    K = len(order)

    # interval certificate (raise on failure -- production version: typed abstention)
    U = C[order, :].copy()
    U[np.arange(K), order] = True
    counts = U.sum(axis=0)
    posk = np.arange(K)[:, None]
    first = np.where(U, posk, K).min(axis=0)
    last = np.where(U, posk, -1).max(axis=0)
    if not (np.all(counts > 0) and np.all(last - first + 1 == counts)):
        raise AssertionError("interval certificate FAILED -- gap-DP not applicable")

    # modular coefficients
    W = hasse_covers(C)
    dplus = W.sum(axis=1).astype(np.int64)   # gate0's dplus: number of cover successors
    ind = W.sum(axis=0).astype(np.int64)
    Wf = W.astype(np.float64)
    a = ((dplus * dplus - (Wf @ dplus).astype(np.int64))
         - ((Wf.T @ dplus).astype(np.int64) - dplus * ind))
    b = dplus - ind

    # gap tables: gsum[i1, j] = sum of arr over v with first_v >= i1 and last_v < j
    def tables(arr: np.ndarray) -> np.ndarray:
        bucket = np.zeros((K + 1, K + 1))
        np.add.at(bucket, (first, last + 1), arr.astype(np.float64))
        suf = np.cumsum(bucket[::-1, :], axis=0)[::-1, :]
        return np.cumsum(suf, axis=1)

    gmin_b = np.zeros((K + 1, K + 1))
    np.add.at(gmin_b, (first[minimal_mask], last[minimal_mask] + 1), 1.0)
    gmin = np.cumsum(np.cumsum(gmin_b[::-1, :], axis=0)[::-1, :], axis=1) > 0.5
    gs_b = tables(b)
    total_b = float(b.sum())

    def gap_dp(c_arr: np.ndarray):
        """Lexicographic min over S != empty with >=1 minimal uncovered:
        primary = missed c-weight (=> max covered c), secondary = missed b (=> max B)."""
        gs = tables(c_arr)
        total = float(c_arr.sum())
        INF = (float("inf"), float("inf"))
        dp = [[INF] * K for _ in range(2)]
        par = [[None] * K for _ in range(2)]
        for j in range(K):
            f = 1 if gmin[0, j] else 0
            v = (gs[0, j], gs_b[0, j])
            if v < dp[f][j]:
                dp[f][j] = v
                par[f][j] = (-1, -1)
        for j in range(K):
            for f in (0, 1):
                base = dp[f][j]
                if base[0] == float("inf"):
                    continue
                row_c, row_b, row_m = gs[j + 1], gs_b[j + 1], gmin[j + 1]
                for j2 in range(j + 1, K):
                    nf = 1 if (f or row_m[j2]) else 0
                    nv = (base[0] + row_c[j2], base[1] + row_b[j2])
                    if nv < dp[nf][j2]:
                        dp[nf][j2] = nv
                        par[nf][j2] = (f, j)
        best, arg = INF, None
        for j in range(K):
            for f in (0, 1):
                if dp[f][j][0] == float("inf"):
                    continue
                if not (f or gmin[j + 1, K]):
                    continue
                v = (dp[f][j][0] + gs[j + 1, K], dp[f][j][1] + gs_b[j + 1, K])
                if v < best:
                    best, arg = v, (f, j)
        if arg is None:
            return None, None, None
        S = []
        f, j = arg
        while j != -1:
            S.append(j)
            f, j = par[f][j]
        z = np.zeros(n, dtype=bool)
        for k in S:
            z |= (first <= k) & (k <= last)
        return total - best[0], total_b - best[1], z

    # feasibility: maximize B itself; if best covered B < 1, no member has H != empty
    _, Bmax, z0 = gap_dp(b.astype(np.float64))
    if z0 is None or Bmax < 1:
        return dict(status="EMPTY_FAMILY", K=K)

    lam = Fraction(int(a[z0].sum()), int(b[z0].sum()))
    for it in range(1, 100):
        p, q = lam.numerator, lam.denominator
        val, _, z = gap_dp((q * a - p * b).astype(np.float64))
        Ad, Bd = int(a[z].sum()), int(b[z].sum())
        assert Bd >= 1, "tie-break failed to find a feasible optimum"
        if abs(val) < 1e-6:
            return dict(status="OK", K=K, iters=it, lam=lam, D=z, A=Ad, B=Bd)
        lam = Fraction(Ad, Bd)
    return dict(status="NO_CONVERGENCE", K=K)


# =============================================================================
# Part 1 -- exact validation against the committed Gate 0 Tier 0 reference (toy poset).
# =============================================================================
def toy_validation() -> dict:
    elems, leq = build_poset(TOY_PI)
    n = len(elems)
    Min = minimal_elements(elems, leq)
    Max = maximal_elements(elems, leq)
    covers = [(x, y) for x in elems for y in elems if is_cover(elems, leq, x, y)]
    dplus_ref = {x: sum(1 for (u, _) in covers if u == x) for x in elems}
    fam = family_A(elems, leq, covers, dplus_ref, Min, Max)

    # brute-force lambda* / argmax / tied set (gate0 semantics)
    Dstar_bf, (Astar, Bstar) = max(fam.items(), key=lambda kv: Fraction(kv[1][0], kv[1][1]))
    lam_bf = Fraction(Astar, Bstar)
    p, q = lam_bf.numerator, lam_bf.denominator
    tied_bf = {D for D, (A, B) in fam.items() if q * A - p * B == 0}

    # same object through the DP path: C matrix + realizer sort (element index)
    C = np.zeros((n, n), dtype=bool)
    for i in elems:
        for j in elems:
            if i != j and leq(j, i):
                C[i, j] = True
    maximal = np.flatnonzero(~C.any(axis=0))
    out = solve(C, np.asarray(maximal, dtype=float))  # toy realizer coord 1 = index

    # modularity cross-check on EVERY family member
    W = hasse_covers(C)
    dplus = W.sum(axis=1).astype(np.int64)
    ind = W.sum(axis=0).astype(np.int64)
    Wf = W.astype(np.float64)
    a = ((dplus * dplus - (Wf @ dplus).astype(np.int64))
         - ((Wf.T @ dplus).astype(np.int64) - dplus * ind))
    b = dplus - ind
    modularity_ok = all(
        (int(a[list(D)].sum()), int(b[list(D)].sum())) == AB for D, AB in fam.items()
    )

    D_dp = frozenset(int(v) for v in np.flatnonzero(out["D"]))
    checks = dict(
        modularity_all_family_members=modularity_ok,
        lambda_star_match=(out["status"] == "OK" and out["lam"] == lam_bf),
        argmax_in_tied_set=D_dp in tied_bf,
        argmax_equals_unique_bf_argmax=(D_dp == Dstar_bf and len(tied_bf) == 1),
        argmax_in_family_with_H_nonempty=(D_dp in fam and out["B"] >= 1),
    )
    return dict(
        family_size=len(fam),
        lambda_star_bf=str(lam_bf),
        lambda_star_dp=str(out.get("lam")),
        dinkelbach_iters=out.get("iters"),
        checks=checks,
        PASS=all(checks.values()),
    )


# =============================================================================
# Part 2 -- production-scale demo (dev seed; CLAIM-INERT: timing/existence only).
# =============================================================================
def production_demo() -> list[dict]:
    rows = []
    for kind in ("MINK", "BH"):
        for intensity in thresholds.INTENSITIES:
            emb, _, _ = generator.numpy_sprinkle(DEV_SEED, intensity)
            C = generator.past_matrix_fast(emb, kind)
            t, r = emb[:, 0], emb[:, 1]
            maximal = np.flatnonzero(~C.any(axis=0))
            key = (t[maximal] - r[maximal]) if kind == "MINK" else (t[maximal] + r[maximal])
            t0 = time.time()
            out = solve(C, key)
            wall = time.time() - t0
            row = dict(
                kind=kind, intensity=intensity, N=int(emb.shape[0]), K=out["K"],
                status=out["status"], iters=out.get("iters"),
                lambda_star=str(out.get("lam")) if out.get("lam") is not None else None,
                size_D=int(out["D"].sum()) if out.get("D") is not None else None,
                A=out.get("A"), B=out.get("B"), wall_seconds=round(wall, 2),
            )
            rows.append(row)
            print(f"[{kind:4s} I={intensity:>7.0f}] N={row['N']:6d} K={row['K']:3d}  "
                  f"{row['status']:12s} iters={row['iters'] or '-':>2}  "
                  f"lambda*={row['lambda_star'] or '-':>8s}  |D*|={row['size_D'] or '-':>6}  "
                  f"B={row['B'] or '-':>4}  wall={wall:6.2f}s  [claim-inert]")
    return rows


if __name__ == "__main__":
    thresholds.assert_environment()
    print("Part 1 -- toy validation vs committed Gate 0 Tier 0 reference:")
    toy = toy_validation()
    for k, v in toy["checks"].items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")
    print(f"  toy validation OVERALL: {'PASS' if toy['PASS'] else 'FAIL'}\n")
    print("Part 2 -- production-scale demo (values NOT verified, timing only):")
    rows = production_demo()
    output = dict(
        scope=("EXPLORATION -- candidate polynomial implementation of the SAME frozen "
               "selector object; toy-validated against the committed Gate 0 reference; "
               "production outputs claim-inert; requires its own fresh Gate 0 (comité 017 "
               "§9 / addendum §6 discipline) before any calibration or scoring use"),
        dev_seed=DEV_SEED,
        toy_validation=toy,
        production_demo=rows,
    )
    with open(RESULT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nWrote {RESULT_PATH}")
