"""dev exploration — growth of order-only information with n: 1+1 EF control and 3+1 Minkowski toy.

NOT sealed; no causal-set track seeds (seed sequences rooted at 7_000_920, outside the sealed
and virgin bands). Origin: CREATE test 3 of 2026-10-16, route Opus-5
(~/herramientas/CREATE/runs/2026-10-16-tasa-3p1/).

Question: does the Fisher information of the order channel grow linearly in n (rate n^{-1/2})
or faster, in a setting without the 1+1 automorphism group?

Method: variational lower bound I_tilde_n = d^T Sigma^{-1} d over a family S of order-invariant
statistics (d = d theta / d parameter by common-random-number central differences, Sigma =
covariance at the base point), with the finite-replicate bias tr(Sigma^{-1} Cov(d_hat))
subtracted. I_tilde_n <= I_n always; a superlinear I_tilde_n proves superlinear information
(and gives an estimator), a linear one is evidence, not proof, of linear I_n.

Family S (all order-invariant): related-pair fraction; links per element; fractions of
related pairs with exactly k = 1, 2, 3 elements in between; numbers of maximal and minimal
elements; height (longest chain).

Models:
  CONTROL  1+1 fixed EF box r in [0.1, 1.3], v in [0, 6], parameter tau = 2M at 0.5
           (theory: I_n <= n J and I_n >= c n, so the slope must be ~1).
  TOY      3+1 Minkowski box t in [0,1], x, y, z in [0, a], parameter a at 1 (aspect ratio;
           not removable by Poincare or dilations).

PRE-DECLARED decision (written before the first run): fit log I_tilde_n = c + b log n over
n in {250, 500, 1000, 2000}; 90% CI by bootstrap over replicates.
  METHOD_INVALID if the CONTROL slope CI is not contained in [0.80, 1.20].
  Otherwise for TOY: SUPERLINEAR if the lower CI end > 1.10; LINEAR_CONSISTENT if the CI is
  contained in [0.80, 1.20]; otherwise UNDECIDED.

Run:  .venv/bin/python dev/explore_information_growth_3p1_toy.py
Writes dev/explore_information_growth_3p1_toy_results.json (refuses to overwrite).
"""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from nachocausal import generator  # noqa: E402

OUT = os.path.join(HERE, "explore_information_growth_3p1_toy_results.json")
NS = (250, 500, 1000, 2000)
REPS = {250: 400, 500: 400, 1000: 300, 2000: 200}
DELTA = 0.02
BOOT = 400
NAMES = ["rel_frac", "links_per_n", "k1_frac", "k2_frac", "k3_frac", "n_max", "n_min", "height"]


def stats_from_order(P):
    """P[i, j] = True iff i precedes j (strict order, transitive)."""
    n = P.shape[0]
    Pf = P.astype(np.float32)
    between = (Pf @ Pf).astype(np.int32)            # [i, j]: # z with i < z < j
    rel = P
    npairs = n * (n - 1) / 2
    k = between[rel]
    height = np.zeros(n, np.int32)
    order = np.argsort(P.sum(axis=0), kind="stable")   # number of predecessors: linear extension
    for j in order:
        preds = P[:, j]
        height[j] = 1 + (height[preds].max() if preds.any() else 0)
    return np.array([
        rel.sum() / npairs,
        (k == 0).sum() / n,
        (k == 1).sum() / npairs,
        (k == 2).sum() / npairs,
        (k == 3).sum() / npairs,
        float((~P.any(axis=1)).sum()),
        float((~P.any(axis=0)).sum()),
        float(height.max()),
    ])


def control_order(u, tau):
    """1+1 EF box; u in [0,1]^2 -> (v, r)."""
    pts = np.c_[u[:, 0] * 6.0, 0.1 + u[:, 1] * 1.2]
    C = generator.past_matrix_fast(pts, "BH", r_S=tau)  # C[i, j]: j precedes i
    return C.T


def toy_order(u, a):
    """3+1 Minkowski box t in [0,1], x in [0,a]^3; u in [0,1]^4."""
    t = u[:, 0]
    x = u[:, 1:] * a
    dt = t[None, :] - t[:, None]
    dist = np.sqrt(((x[None, :, :] - x[:, None, :]) ** 2).sum(-1))
    return (dt > 0) & (dt >= dist)


def run_model(name, order_fn, dim, base):
    out = {}
    for n in NS:
        t0 = time.time()
        s0, ds = [], []
        for rep in range(REPS[n]):
            rng = np.random.default_rng([7_000_920, dim, n, rep])
            u = rng.random((n, dim))
            sm = stats_from_order(order_fn(u, base * (1 - DELTA)))
            s = stats_from_order(order_fn(u, base))
            sp = stats_from_order(order_fn(u, base * (1 + DELTA)))
            s0.append(s)
            ds.append((sp - sm) / (2 * DELTA * base))
        S0, D = np.array(s0), np.array(ds)
        out[n] = {"S0": S0.tolist(), "D": D.tolist()}
        print(f"{name} n={n} done in {time.time() - t0:.0f}s", flush=True)
    return out


def info(S0, D):
    Sigma = np.cov(S0, rowvar=False)
    d = D.mean(axis=0)
    covd = np.cov(D, rowvar=False) / D.shape[0]
    Si = np.linalg.pinv(Sigma)
    return float(d @ Si @ d - np.trace(Si @ covd)), [float(d[i] ** 2 / Sigma[i, i] - covd[i, i] / Sigma[i, i])
                                                    for i in range(len(d))]


def slope(data, rng):
    ns = np.array(NS, float)
    I = np.array([info(np.array(data[n]["S0"]), np.array(data[n]["D"]))[0] for n in NS])
    b = float(np.polyfit(np.log(ns), np.log(np.maximum(I, 1e-12)), 1)[0])
    boots = []
    for _ in range(BOOT):
        Ib = []
        for n in NS:
            S0, D = np.array(data[n]["S0"]), np.array(data[n]["D"])
            idx = rng.integers(0, S0.shape[0], S0.shape[0])
            Ib.append(info(S0[idx], D[idx])[0])
        Ib = np.array(Ib)
        if np.all(Ib > 0):
            boots.append(np.polyfit(np.log(ns), np.log(Ib), 1)[0])
    lo, hi = (float(np.quantile(boots, 0.05)), float(np.quantile(boots, 0.95))) if boots else (math.nan, math.nan)
    per = {n: info(np.array(data[n]["S0"]), np.array(data[n]["D"]))[1] for n in NS}
    return {"I_tilde": dict(zip(map(str, NS), I.tolist())), "slope": b, "ci90": [lo, hi],
            "boot_ok": len(boots), "per_stat_info": {str(n): dict(zip(NAMES, v)) for n, v in per.items()}}


def main() -> int:
    if os.path.exists(OUT):
        print(f"refusing to overwrite {OUT}", file=sys.stderr)
        return 1
    rng = np.random.default_rng(7_000_921)
    ctrl = slope(run_model("CONTROL", control_order, 2, 0.5), rng)
    print("CONTROL", json.dumps({k: ctrl[k] for k in ("I_tilde", "slope", "ci90")}), flush=True)
    toy = slope(run_model("TOY", toy_order, 4, 1.0), rng)
    print("TOY", json.dumps({k: toy[k] for k in ("I_tilde", "slope", "ci90")}), flush=True)
    lo, hi = ctrl["ci90"]
    if not (0.80 <= lo and hi <= 1.20):
        verdict = "METHOD_INVALID"
    else:
        tlo, thi = toy["ci90"]
        verdict = ("SUPERLINEAR" if tlo > 1.10 else
                   "LINEAR_CONSISTENT" if (0.80 <= tlo and thi <= 1.20) else "UNDECIDED")
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                            cwd=HERE).stdout.strip()
    with open(OUT, "x") as f:
        json.dump({"verdict": verdict, "repo_head": commit, "delta": DELTA, "reps": REPS, "stats": NAMES,
                   "control": ctrl, "toy": toy}, f, indent=1)
    print("VERDICT:", verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
