"""dev exploration — boundary counts as control variates: superlinear order information in 3+1?

Follow-up of dev/explore_information_growth_3p1_toy.py (UNDECIDED) and
dev/explore_information_growth_degeneracy.py. There the joint lower bound for the 3+1
Minkowski toy jumped to 41065 at n = 4000 (100 replicates), driven by combining the
related-pair fraction with the numbers of maximal and minimal elements, while U-statistics
alone grew about linearly and the 1+1 EF control was linear. Hypothesis: boundary counts act
as control variates that cancel the Hajek (point-cloud) fluctuation of the related-pair
fraction, giving information growing faster than n (rate faster than n^{-1/2}).

Reduced family (no matrix products needed): related-pair fraction, n_max, n_min, height.
Same models as before: CONTROL 1+1 fixed EF box at tau = 0.5; TOY 3+1 Minkowski box with
aspect a = 1. Seeds: sequences rooted at 7_000_923 (outside sealed and virgin bands).

PRE-DECLARED (written before the first run): n in {500, 1000, 2000, 4000, 8000}, 300
replicates each, CRN central differences with relative step 0.02, bias-corrected
I_tilde_n = d^T Sigma^{-1} d - tr(Sigma^{-1} Cov(d_hat)). Fit log I_tilde_n on log n; 90% CI
by bootstrap over replicates.
  METHOD_INVALID if the CONTROL slope CI is not contained in [0.80, 1.20].
  Otherwise TOY: SUPERLINEAR if the CI lower end > 1.10; LINEAR_CONSISTENT if the CI is
  contained in [0.80, 1.20]; otherwise UNDECIDED.
Also reported: the same fit for the related-pair fraction alone and for the pair plus
boundary counts without height.

Run:  .venv/bin/python dev/explore_information_growth_boundary_cv.py
Writes dev/explore_information_growth_boundary_cv_results.json (refuses to overwrite).
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from nachocausal import generator  # noqa: E402

OUT = os.path.join(HERE, "explore_information_growth_boundary_cv_results.json")
NS = (500, 1000, 2000, 4000, 8000)
REPS = 300
DELTA = 0.02
BOOT = 400
NAMES = ["rel_frac", "n_max", "n_min", "height"]
SUBSETS = {"all": [0, 1, 2, 3], "rel_only": [0], "rel_max_min": [0, 1, 2]}


def stats_sorted(P):
    """P[i, j]: i precedes j, with points already sorted so that i < j whenever i precedes j."""
    n = P.shape[0]
    h = np.ones(n, np.int32)
    for j in range(1, n):
        preds = P[:j, j]
        if preds.any():
            h[j] = 1 + h[:j][preds].max()
    return np.array([P.sum() / (n * (n - 1) / 2), float((~P.any(axis=1)).sum()),
                     float((~P.any(axis=0)).sum()), float(h.max())])


def toy_order(u, a):
    u = u[np.argsort(u[:, 0])]
    t, x = u[:, 0], u[:, 1:] * a
    n = t.size
    P = np.zeros((n, n), bool)
    for s in range(0, n, 1000):
        e = min(n, s + 1000)
        dt = t[None, :] - t[s:e, None]
        d2 = ((x[None, :, :] - x[s:e, None, :]) ** 2).sum(-1)
        P[s:e] = (dt > 0) & (dt * dt >= d2)
    return P


def control_order(u, tau):
    u = u[np.argsort(u[:, 0])]
    pts = np.c_[u[:, 0] * 6.0, 0.1 + u[:, 1] * 1.2]
    return generator.past_matrix_fast(pts, "BH", r_S=tau).T


def run(order_fn, dim, base, tag):
    data = {}
    for n in NS:
        t0 = time.time()
        S0, D = [], []
        for rep in range(REPS):
            u = np.random.default_rng([7_000_923, dim, n, rep]).random((n, dim))
            sm = stats_sorted(order_fn(u, base * (1 - DELTA)))
            s0 = stats_sorted(order_fn(u, base))
            sp = stats_sorted(order_fn(u, base * (1 + DELTA)))
            S0.append(s0)
            D.append((sp - sm) / (2 * DELTA * base))
        data[n] = (np.array(S0), np.array(D))
        print(f"{tag} n={n} {time.time() - t0:.0f}s", flush=True)
    return data


def info(S0, D):
    Sigma = np.atleast_2d(np.cov(S0, rowvar=False))
    d = D.mean(axis=0)
    covd = np.atleast_2d(np.cov(D, rowvar=False)) / D.shape[0]
    Si = np.linalg.pinv(Sigma)
    return float(d @ Si @ d - np.trace(Si @ covd))


def fit(data, cols, rng):
    ns = np.array(NS, float)
    I = np.array([info(data[n][0][:, cols], data[n][1][:, cols]) for n in NS])
    b = float(np.polyfit(np.log(ns), np.log(np.maximum(I, 1e-12)), 1)[0])
    boots = []
    for _ in range(BOOT):
        Ib = []
        for n in NS:
            S0, D = data[n]
            idx = rng.integers(0, REPS, REPS)
            Ib.append(info(S0[idx][:, cols], D[idx][:, cols]))
        if min(Ib) > 0:
            boots.append(np.polyfit(np.log(ns), np.log(Ib), 1)[0])
    return {"I_tilde": dict(zip(map(str, NS), I.tolist())), "slope": b,
            "ci90": [float(np.quantile(boots, 0.05)), float(np.quantile(boots, 0.95))], "boot_ok": len(boots)}


def main() -> int:
    if os.path.exists(OUT):
        print(f"refusing to overwrite {OUT}", file=sys.stderr)
        return 1
    rng = np.random.default_rng(7_000_924)
    res = {}
    for tag, fn, dim, base in (("control", control_order, 2, 0.5), ("toy", toy_order, 4, 1.0)):
        data = run(fn, dim, base, tag)
        res[tag] = {k: fit(data, cols, rng) for k, cols in SUBSETS.items()}
        res[tag]["raw"] = {str(n): {"S0": data[n][0].tolist(), "D": data[n][1].tolist()} for n in NS}
        print(tag, json.dumps({k: {kk: v[kk] for kk in ("I_tilde", "slope", "ci90")} for k, v in res[tag].items()
                               if k != "raw"}), flush=True)
    lo, hi = res["control"]["all"]["ci90"]
    if not (0.80 <= lo and hi <= 1.20):
        verdict = "METHOD_INVALID"
    else:
        tlo, thi = res["toy"]["all"]["ci90"]
        verdict = "SUPERLINEAR" if tlo > 1.10 else ("LINEAR_CONSISTENT" if 0.80 <= tlo and thi <= 1.20 else "UNDECIDED")
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                            cwd=HERE).stdout.strip()
    with open(OUT, "x") as f:
        json.dump({"verdict": verdict, "repo_head": commit, "ns": NS, "reps": REPS, "delta": DELTA,
                   "stats": NAMES, "subsets": SUBSETS, **res}, f)
    print("VERDICT:", verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
