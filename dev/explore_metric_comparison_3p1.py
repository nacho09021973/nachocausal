"""dev exploration — metric-comparison monotonicity of causal relations in full 3+1D.

NOT sealed. Exploration seeds 7_000_910..7_000_919 of the 2+1 exploration band (the 3+1
check reuses the 2+1 machinery); virgin band untouched. Companion of
dev/explore_metric_comparison_2p1.py and of
research_program/puente_3p1/2026-10-16/M1_metric_comparison_and_upper_rate.md.

3+1D order. By spherical symmetry, rotate the great circle through two points onto the
equator. Lemma E1 then gives: x < y iff U_x < U_y, V_x < V_y and alpha_xy <= min(pi, L_xy),
where alpha is the angle between the two directions on S^2 and L is the supremal angular
reach of the 2+1 equatorial order for those (U, V) endpoints. L comes from the audited
geodesic shot dev/gen2p1_efbox.py:shoot_pairs_fast (coarse pass, then fine pass for pairs
within COARSE_MARGIN of the boundary, as in bh_order). Mass scaling as in the 2+1 check:
relation_tau(t, r) = relation_{2M=0.5}(t k, r k), k = 0.5 / tau.

Box: t* in [0, 4], r in [0.15, 1.3] with density ~ r^2 (sqrt(-g) = r^2 sin theta), uniform
directions on S^2.

PRE-DECLARED checks (written before the first run), tau grid 0.40, 0.45, ..., 0.70:
  N0 sanity: for 300 equatorial points at tau = 0.5, this relation equals bh_order of the
     2+1 generator exactly (zero disagreements).
  N1 pointwise: on 10 seeds of 300 points, no pair is unrelated at tau_k and related at
     tau_{k+1} (zero violations).
  N2 monotone p: the related-pair fraction decreases at every step with the paired
     difference > 5 se.
  Verdict MONOTONE_3P1_CONSISTENT if N0-N2 pass, else FAILED_<check>.

Run:  .venv/bin/python dev/explore_metric_comparison_3p1.py
Writes dev/explore_metric_comparison_3p1_results.json (refuses to overwrite).
"""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys

os.environ["NC2P1_T_EDGE"] = "10.0"

import numpy as np  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import gen2p1_efbox as g  # noqa: E402

OUT = os.path.join(HERE, "explore_metric_comparison_3p1_results.json")
TAUS = np.round(np.arange(0.40, 0.7001, 0.05), 2)
SEEDS = range(7_000_910, 7_000_920)
N_POINTS = 300
T_BOX, R_LO_BOX, R_HI_BOX = 4.0, 0.15, 1.3


def sprinkle(rng, n, equatorial=False):
    t = rng.uniform(0.0, T_BOX, n)
    r = np.cbrt(rng.uniform(R_LO_BOX ** 3, R_HI_BOX ** 3, n))        # density ~ r^2
    if equatorial:
        ph = rng.uniform(0.0, 2.0 * math.pi, n)
        nvec = np.c_[np.cos(ph), np.sin(ph), np.zeros(n)]
    else:
        nvec = rng.normal(size=(n, 3))
        nvec /= np.linalg.norm(nvec, axis=1, keepdims=True)
    return t, r, nvec


def order_3p1(t, r, nvec, tau):
    """order[i, j]: i precedes j, for the mass with 2M = tau."""
    k = 0.5 / tau
    U, V = g.to_kruskal(t * k, r * k)
    alpha = np.arccos(np.clip(nvec @ nvec.T, -1.0, 1.0))
    ii, jj = np.nonzero((U[None, :] > U[:, None]) & (V[None, :] > V[:, None]))
    order = np.zeros((t.size, t.size), bool)
    if ii.size == 0:
        return order, 0
    a = alpha[ii, jj]
    Lc, mc = g.shoot_pairs_fast(U[ii], V[ii], U[jj], V[jj], *g.COARSE)
    dmax = np.minimum(Lc, math.pi)
    far = (np.abs(a - dmax) > g.COARSE_MARGIN) & (mc < 1e-9)
    order[ii[far], jj[far]] = a[far] <= dmax[far]
    kk = np.nonzero(~far)[0]
    near = 0
    if kk.size:
        Lf, mf = g.shoot_pairs_fast(U[ii[kk]], V[ii[kk]], U[jj[kk]], V[jj[kk]], *g.FINE)
        assert np.all(mf < 1e-9), "fine shooting missed"
        dm = np.minimum(Lf, math.pi)
        near = int((np.abs(a[kk] - dm) < g.TOL).sum())
        order[ii[kk], jj[kk]] = a[kk] <= dm
    return order, near


def main() -> int:
    if os.path.exists(OUT):
        print(f"refusing to overwrite {OUT}", file=sys.stderr)
        return 1
    rng = np.random.default_rng(7_000_919)
    t, r, nv = sprinkle(rng, 300, equatorial=True)
    mine, _ = order_3p1(t, r, nv, 0.5)
    phi = np.arctan2(nv[:, 1], nv[:, 0]) % (2 * math.pi)
    ref, _ = g.bh_order(t, r, phi, rng=None, audit=0)
    n0 = int((mine != ref).sum())
    print("N0 disagreements with 2+1 bh_order on the equator:", n0, "of", int(ref.sum()), "relations", flush=True)
    viol, fracs, near_tot = 0, [], 0
    iu = np.triu_indices(N_POINTS, 1)
    for seed in SEEDS:
        t, r, nv = sprinkle(np.random.default_rng(seed), N_POINTS)
        prev, row = None, []
        for tau in TAUS:
            o, near = order_3p1(t, r, nv, tau)
            near_tot += near
            cur = (o | o.T)[iu]
            if prev is not None:
                viol += int(np.count_nonzero(cur & ~prev))
            prev = cur
            row.append(float(cur.mean()))
        fracs.append(row)
        print("seed", seed, [round(x, 4) for x in row], "violations", viol, flush=True)
    F = np.array(fracs)
    d = F[:, 1:] - F[:, :-1]
    md, sd = d.mean(axis=0), d.std(axis=0, ddof=1) / math.sqrt(F.shape[0])
    n2 = bool(np.all(md < 0) and np.all(-md > 5 * sd))
    failed = (["N0"] if n0 else []) + (["N1"] if viol else []) + ([] if n2 else ["N2"])
    verdict = "MONOTONE_3P1_CONSISTENT" if not failed else "FAILED_" + "_".join(failed)
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                            cwd=HERE).stdout.strip()
    res = {"verdict": verdict, "repo_head": commit, "taus": TAUS.tolist(), "seeds": list(SEEDS),
           "n_points": N_POINTS, "box": [T_BOX, R_LO_BOX, R_HI_BOX], "N0_disagreements": n0,
           "N1_violations": viol, "near_boundary_pairs_total": near_tot,
           "p_mean": F.mean(axis=0).tolist(), "dp_mean": md.tolist(), "dp_se": sd.tolist(), "N2_pass": n2}
    with open(OUT, "x") as f:
        json.dump(res, f, indent=1)
    print(json.dumps({k: res[k] for k in ("verdict", "N0_disagreements", "N1_violations", "p_mean",
                                          "dp_mean", "dp_se")}, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
