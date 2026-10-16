"""dev exploration — numerical check of the analytic monotonicity lemma for p(tau).

NOT sealed; plain Monte Carlo/quadrature of the analytic model of
research_program/work_packages/wp6_domain_bridge_fixed_ef_box.md §1.

Lemma checked (written before the first run). For two points with v1 < v2, the event
"related" (Delta u * Delta v > 0) is non-increasing in tau for every fixed pair; and
  -p'(tau) >= c(tau) := (1/L^2) iint_{tau<r1<r2<r_b} (2/T)(1 - dphi/T)_+ (gamma(r2) - gamma(r1)) dr1 dr2,
with phi(r) = 2r + 2 tau log((r - tau)/tau), dphi = phi(r2) - phi(r1) and
gamma = d_tau phi = 2 log((r - tau)/tau) - 2 tau/(r - tau) - 2 (exterior pairs that stop
being related when tau grows).

PRE-DECLARED checks:
  G1 pointwise: on 2e6 random pairs, the related indicator on the tau grid
     [0.12, 1.28] step 0.01 never goes from 0 to 1 (zero violations).
  G2 bound: c(tau) by quadrature is > 0 and <= -p'(tau) from
     dev/explore_ef_box_comparable_pair_monotonicity_results.json at every common grid
     point, allowing 3 se.
  Verdict LEMMA_CONSISTENT if G1 and G2 pass, else FAILED_<check>.

Run:  .venv/bin/python dev/explore_ef_box_pairwise_relation_monotonicity.py
Writes dev/explore_ef_box_pairwise_relation_monotonicity_results.json (refuses to overwrite).
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

L = R_B - R_A
OUT = os.path.join(HERE, "explore_ef_box_pairwise_relation_monotonicity_results.json")
PREV = os.path.join(HERE, "explore_ef_box_comparable_pair_monotonicity_results.json")
FINE = np.round(np.arange(0.12, 1.2801, 0.01), 2)
SEED = 20261019


def related(v, r, tau):
    u = u_coord(v, r, tau)
    return (u[:, 0] - u[:, 1]) * (v[:, 0] - v[:, 1]) > 0


def c_of_tau(tau, m=1500):
    """Quadrature of c(tau) with t = r - tau log-spaced (integrand vanishes where dphi >= T)."""
    y = np.linspace(np.log(1e-9), np.log(R_B - tau), m)
    t = np.exp(y)
    r = tau + t
    w = t * np.gradient(y)
    phi = 2 * r + 2 * tau * np.log(t / tau)
    gam = 2 * np.log(t / tau) - 2 * tau / t - 2
    d = phi[None, :] - phi[:, None]          # [i, j]: r_i = r1, r_j = r2
    up = np.triu(np.ones((m, m), bool), 1)   # r2 > r1
    dens = np.where(up & (d < T), (2 / T) * (1 - d / T), 0.0)
    val = dens * (gam[None, :] - gam[:, None]) * w[:, None] * w[None, :]
    return float(val.sum() / L**2)


def main() -> int:
    if os.path.exists(OUT):
        print(f"refusing to overwrite {OUT}", file=sys.stderr)
        return 1
    rng = np.random.default_rng(SEED)
    viol = 0
    for _ in range(4):
        v = rng.random((500_000, 2)) * T
        r = R_A + rng.random((500_000, 2)) * L
        prev = related(v, r, FINE[0])
        for t in FINE[1:]:
            cur = related(v, r, t)
            viol += int(np.count_nonzero(cur & ~prev))
            prev = cur
    print("G1 violations (0 -> 1):", viol, flush=True)
    prevrows = json.load(open(PREV))["grid"]
    g2 = {}
    for key, row in prevrows.items():
        tau = float(key)
        c1, c2 = c_of_tau(tau, 1500), c_of_tau(tau, 3000)
        ok = c2 > 0 and c2 <= -row["dp"] + 3 * row["dp_se"]
        g2[key] = {"c": c2, "c_coarse": c1, "minus_dp": -row["dp"], "se": row["dp_se"], "pass": ok}
        print(f"tau={key} c={c2:.5f} (coarse {c1:.5f}) -p'={-row['dp']:.5f} pass={ok}", flush=True)
    failed = (["G1"] if viol else []) + ([] if all(x["pass"] for x in g2.values()) else ["G2"])
    verdict = "LEMMA_CONSISTENT" if not failed else "FAILED_" + "_".join(failed)
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                            cwd=HERE).stdout.strip()
    with open(OUT, "x") as f:
        json.dump({"verdict": verdict, "repo_head": commit, "seed": SEED, "G1_violations": viol,
                   "G1_pairs": 2_000_000, "G1_grid_step": 0.01, "G2": g2}, f, indent=1)
    print("VERDICT:", verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
