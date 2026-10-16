"""dev exploration — is the comparable-pair probability p(tau) monotone in the fixed EF box?

NOT sealed; plain Monte Carlo of the analytic model of
research_program/work_packages/wp6_domain_bridge_fixed_ef_box.md §1 (causal order =
product order in (u_tau, v)). No causal-set ensembles, no track seeds.

Why: for the order-only statistic U_n = fraction of related pairs (a U-statistic,
function of Pi_n and of the unlabeled poset), Var U_n <= 4 p(1-p)/n. Hence
  (lower)  I_n^Pi(tau) >= n p'(tau)^2 / (4 p(1-p))       if p'(tau) != 0, and
  (upper)  tau_hat = p^{-1}(clip(U_n)) has E|tau_hat - tau| <= 2 sqrt(p(1-p)) / (m sqrt n)
           if p is strictly monotone on K with min_K |p'| = m > 0.
Both need p' != 0 on K. This script only gives NUMERICAL evidence, not a proof.

PRE-DECLARED (written before the first run): grid tau in [0.15, 1.25] step 0.05 inside
(r_a, r_b) = (0.1, 1.3); p and p' by common-random-number Monte Carlo
(4e7 pairs, central difference h = 0.01, 10 batches for se).
  MONOTONE_ON_GRID if p' has the same sign at every grid point and |p'| > 5 se there;
  NOT_MONOTONE if some grid point has |p'| > 5 se with the opposite sign;
  otherwise UNDECIDED (report the grid points that fail).
Also reports the lower bound n p'^2/(4p(1-p)) next to the Monte Carlo I_n^Pi of
dev/explore_create_fisher_quotient_check_results.json (tau 0.4, 0.5, 0.7).

Run:  .venv/bin/python dev/explore_ef_box_comparable_pair_monotonicity.py
Writes dev/explore_ef_box_comparable_pair_monotonicity_results.json (refuses to overwrite).
"""

from __future__ import annotations

import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from explore_create_fisher_quotient_check import R_A, R_B, T, u_coord  # noqa: E402

OUT = os.path.join(HERE, "explore_ef_box_comparable_pair_monotonicity_results.json")
PREV = os.path.join(HERE, "explore_create_fisher_quotient_check_results.json")
GRID = np.round(np.arange(0.15, 1.2501, 0.05), 2)
PAIRS = 40_000_000
BATCHES = 10
H = 0.01
SEED = 20261018


def comparable(v, r, tau):
    u = u_coord(v, r, tau)
    return (u[:, 0] - u[:, 1]) * (v[:, 0] - v[:, 1]) > 0


def main() -> int:
    if os.path.exists(OUT):
        print(f"refusing to overwrite {OUT}", file=sys.stderr)
        return 1
    rng = np.random.default_rng(SEED)
    per = PAIRS // BATCHES
    acc = {float(t): {"p": [], "dp": []} for t in GRID}
    for _ in range(BATCHES):
        v = rng.random((per, 2)) * T
        r = R_A + rng.random((per, 2)) * (R_B - R_A)
        for t in GRID:
            pm, p0, pp = (comparable(v, r, t + d).mean() for d in (-H, 0.0, H))
            acc[float(t)]["p"].append(p0)
            acc[float(t)]["dp"].append((pp - pm) / (2 * H))
    rows = {}
    for t, a in acc.items():
        p, dp = float(np.mean(a["p"])), float(np.mean(a["dp"]))
        se = float(np.std(a["dp"], ddof=1) / np.sqrt(BATCHES))
        rows[f"{t:.2f}"] = {"p": p, "dp": dp, "dp_se": se, "z": dp / se if se > 0 else float("inf"),
                            "lower_bound_coef": dp**2 / (4 * p * (1 - p))}
        print(f"tau={t:.2f} p={p:.6f} p'={dp:+.5f} se={se:.5f}", flush=True)
    signs = {np.sign(x["dp"]) for x in rows.values() if abs(x["z"]) > 5}
    weak = [k for k, x in rows.items() if abs(x["z"]) <= 5]
    if len(signs) > 1:
        verdict = "NOT_MONOTONE"
    elif weak:
        verdict = "UNDECIDED"
    else:
        verdict = "MONOTONE_ON_GRID"
    compare = {}
    if os.path.exists(PREV):
        prev = json.load(open(PREV))["C3"]
        for key, x in prev.items():
            tau, n = key.split("/")
            coef = rows[f"{float(tau):.2f}"]["lower_bound_coef"]
            compare[key] = {"I_n_mc": x["I_n_mc"], "lower_bound": int(n) * coef,
                            "holds": x["I_n_mc"] >= int(n) * coef}
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                            cwd=HERE).stdout.strip()
    with open(OUT, "x") as f:
        json.dump({"verdict": verdict, "weak_points": weak, "repo_head": commit, "pairs": PAIRS,
                   "h": H, "seed": SEED, "grid": rows, "lower_bound_vs_mc": compare}, f, indent=1)
    print("lower bound vs MC:", json.dumps(compare))
    print("VERDICT:", verdict, "weak:", weak)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
