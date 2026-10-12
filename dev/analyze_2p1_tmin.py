"""2+1 phase B: apply the inherited t_min rule (docs/estimator_v2_decision_spec.md, Decision 2)
to the T sweep (dev; NO verdict).  t_min(rho) = smallest T such that (1) |bias| <= mean bracket
half-width, (2) coverage >= 0.5, and (3) both hold for every swept T in [T, 2T].
Usage: .venv/bin/python dev/analyze_2p1_tmin.py dev/2p1_sweep_T_2026-10-12.jsonl
"""
import collections
import json
import sys

import numpy as np

rows = [json.loads(l) for l in open(sys.argv[1])]
assert not any("error" in d for d in rows)
cells = collections.defaultdict(list)
for d in rows:
    cells[(d["rho"], d["T_EDGE"])].append(d)
table = {}
for (rho, T), L in sorted(cells.items()):
    b = [d["BH"] for d in L]; m = [d["MINK"] for d in L]
    cl = [x for x in b if x.get("claimed")]
    mids = np.array([x["mid"] for x in cl]); hw = np.array([(x["r_hi"] - x["r_lo"]) / 2 for x in cl])
    rec = {"n_seeds": len(L), "bh_claims": len(cl), "mink_abstains": sum(x["abstain"] for x in m),
           "coverage": float(np.mean([x["covers_2M"] for x in cl])),
           "bias": float(mids.mean() - 0.5), "half_width": float(hw.mean()),
           "mid_sd": float(mids.std(ddof=1)),
           "width_over_2M_median": float(np.median([x["width_over_2M"] for x in cl]))}
    rec["clause1"] = abs(rec["bias"]) <= rec["half_width"]
    rec["clause2"] = rec["coverage"] >= 0.5
    table[(rho, T)] = rec
out = {"cells": {f"rho={r:g},T={t:g}": v for (r, t), v in table.items()}, "t_min": {}}
for rho in sorted({k[0] for k in table}):
    Ts = sorted(t for (r, t) in table if r == rho)
    tmin = None
    for T in Ts:
        window = [t for t in Ts if T <= t <= 2 * T]
        if max(window) < 2 * T:
            continue                      # plateau not testable within the sweep
        if all(table[(rho, t)]["clause1"] and table[(rho, t)]["clause2"] for t in window):
            tmin = T
            break
    out["t_min"][f"rho={rho:g}"] = tmin
print(json.dumps(out, indent=1))
