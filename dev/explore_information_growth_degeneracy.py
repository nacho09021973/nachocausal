"""dev exploration — is the superlinear joint information of the 3+1 toy a degenerate combination?

Follow-up of dev/explore_information_growth_3p1_toy.py (verdict UNDECIDED: CONTROL slope 1.07
[0.97, 1.17]; TOY slope 1.10 [1.03, 1.22]; each single statistic grows at most linearly, the
joint lower bound grows by 10.1x for 8x n). Same deterministic seed sequences, so n <= 2000
reproduces the same replicates; adds n = 4000 for the TOY (100 replicates) and stores raw
replicates.

Question (CREATE test 3: Astra-2 versus Opus-2): does a fixed combination w of the order
statistics have a vanishing first-order (Hajek) fluctuation, n Var(w.S) -> 0, while its
derivative w.d stays away from 0? That would mean information of order n^2 (rate n^{-1}).

PRE-DECLARED (written before the first run). w* = Sigma_{n_max}^{-1} d_{n_max}, normalized
to w*.d_{n_max} = 1, with n_max = 4000 (TOY) or 2000 (CONTROL). For each n: V_n = n Var(w*.S)
and g_n = w*.d_n. Fit log V_n = c + s log n; 90% bootstrap CI for s.
  TOY DEGENERATE_COMBINATION if the CI upper end < -0.20 and max/min of g_n over n < 1.3;
  NON_DEGENERATE if the CI contains 0 and is contained in [-0.20, 0.20]; otherwise UNDECIDED.
  CONTROL is reported the same way (theory: linear information, so it should not be
  DEGENERATE_COMBINATION; if it is, the analysis is invalid).
Also refits the slope of the joint I_tilde_n over n in {250, ..., 4000} for the TOY.

Run:  .venv/bin/python dev/explore_information_growth_degeneracy.py
Writes dev/explore_information_growth_degeneracy_results.json (refuses to overwrite).
"""

from __future__ import annotations

import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import explore_information_growth_3p1_toy as base  # noqa: E402

OUT = os.path.join(HERE, "explore_information_growth_degeneracy_results.json")
BOOT = 400


def collect(name, order_fn, dim, b, ns, reps):
    base.NS = ns
    base.REPS = reps
    return base.run_model(name, order_fn, dim, b)


def degeneracy(data, ns, rng):
    nmax = ns[-1]
    S, D = np.array(data[nmax]["S0"]), np.array(data[nmax]["D"])
    w = np.linalg.pinv(np.cov(S, rowvar=False)) @ D.mean(axis=0)
    w = w / (w @ D.mean(axis=0))
    V = np.array([n * np.var(np.array(data[n]["S0"]) @ w, ddof=1) for n in ns])
    g = np.array([np.array(data[n]["D"]).mean(axis=0) @ w for n in ns])
    s = float(np.polyfit(np.log(ns), np.log(V), 1)[0])
    boots = []
    for _ in range(BOOT):
        Vb = []
        for n in ns:
            X = np.array(data[n]["S0"]) @ w
            Vb.append(n * np.var(X[rng.integers(0, X.size, X.size)], ddof=1))
        boots.append(np.polyfit(np.log(ns), np.log(Vb), 1)[0])
    return {"w": w.tolist(), "V_n": dict(zip(map(str, ns), V.tolist())),
            "g_n": dict(zip(map(str, ns), g.tolist())), "slope_logV": s,
            "ci90": [float(np.quantile(boots, 0.05)), float(np.quantile(boots, 0.95))],
            "g_ratio": float(np.max(np.abs(g)) / np.min(np.abs(g)))}


def classify(r):
    lo, hi = r["ci90"]
    if hi < -0.20 and r["g_ratio"] < 1.3:
        return "DEGENERATE_COMBINATION"
    if lo <= 0 <= hi and -0.20 <= lo and hi <= 0.20:
        return "NON_DEGENERATE"
    return "UNDECIDED"


def main() -> int:
    if os.path.exists(OUT):
        print(f"refusing to overwrite {OUT}", file=sys.stderr)
        return 1
    rng = np.random.default_rng(7_000_922)
    ns_c = (250, 500, 1000, 2000)
    ctrl = collect("CONTROL", base.control_order, 2, 0.5, ns_c, {250: 400, 500: 400, 1000: 300, 2000: 200})
    ns_t = (250, 500, 1000, 2000, 4000)
    toy = collect("TOY", base.toy_order, 4, 1.0, ns_t, {250: 400, 500: 400, 1000: 300, 2000: 200, 4000: 100})
    rc, rt = degeneracy(ctrl, ns_c, rng), degeneracy(toy, ns_t, rng)
    rc["verdict"], rt["verdict"] = classify(rc), classify(rt)
    base.NS = ns_t
    It = [base.info(np.array(toy[n]["S0"]), np.array(toy[n]["D"]))[0] for n in ns_t]
    rt["I_tilde"] = dict(zip(map(str, ns_t), It))
    rt["I_tilde_slope_5pts"] = float(np.polyfit(np.log(ns_t), np.log(It), 1)[0])
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                            cwd=HERE).stdout.strip()
    with open(OUT, "x") as f:
        json.dump({"repo_head": commit, "stats": base.NAMES, "control": rc, "toy": rt,
                   "raw": {"control": {str(k): v for k, v in ctrl.items()},
                           "toy": {str(k): v for k, v in toy.items()}}}, f)
    for nm, r in (("CONTROL", rc), ("TOY", rt)):
        print(nm, json.dumps({k: r[k] for k in r if k not in ("w",)}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
