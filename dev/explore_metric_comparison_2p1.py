"""dev exploration — metric-comparison monotonicity of causal relations, checked in 2+1D.

NOT sealed. Exploration seeds of the 2+1 band only (7_000_900..7_000_909); the virgin band
8_000_000..8_999_999 is untouched. Reuses the audited 2+1 equatorial order of
dev/gen2p1_efbox.py (bh_order) unchanged.

Lemma (any dimension, ingoing EF): g_M(X,X) = -(1-2M/r) vdot^2 + 2 vdot rdot + r^2 |Omegadot|^2,
so g_{M'}(X,X) - g_M(X,X) = 2 (M'-M) vdot^2 / r >= 0 for M' > M, and future-directed causal
<=> vdot >= 0 for every M. Hence J^+_{M'}(x) is contained in J^+_M(x) at fixed coordinates:
for every fixed pair of points, "related" is non-increasing in M. With sqrt(-g) M-free, the
comparable-pair probability p(M) of a fixed EF box is non-increasing.

Mass scaling: the order is invariant under a constant conformal factor, and
(v, r) -> (v, r) * (0.5 / tau) maps the metric of 2M = tau to 16 M^2 times the metric of
2M = 0.5 (the generator's units). So relation_tau(t, r, phi) = bh_order(t k, r k, phi), k = 0.5/tau.

Box for this check: t* in [0, 4], r in [0.15, 1.3], phi in S^1, density ~ r (sqrt(-g) = r).
r_lo = 0.15 keeps 1 - UV inside the generator's z-table for tau <= 0.7, and NC2P1_T_EDGE=10 is
set before import so that the table covers the rescaled box for tau >= 0.4.

PRE-DECLARED checks (written before the first run), tau grid 0.40, 0.45, ..., 0.70:
  M0 sanity: same-angle pairs agree with the 1+1 closed form (radial_check) at tau = 0.5.
  M1 pointwise: on 10 seeds of 500 points, no pair is unrelated at tau_k and related at
     tau_{k+1} (zero violations).
  M2 monotone p: the comparable-pair fraction, pooled over the 10 seeds with common points,
     decreases at every grid step, with the paired difference > 5 se at every step.
  Verdict MONOTONE_2P1_CONSISTENT if M0-M2 pass, else FAILED_<check>.

Run:  .venv/bin/python dev/explore_metric_comparison_2p1.py
Writes dev/explore_metric_comparison_2p1_results.json (refuses to overwrite).
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

OUT = os.path.join(HERE, "explore_metric_comparison_2p1_results.json")
TAUS = np.round(np.arange(0.40, 0.7001, 0.05), 2)
SEEDS = range(7_000_900, 7_000_910)
N_POINTS = 500
T_BOX, R_LO_BOX, R_HI_BOX = 4.0, 0.15, 1.3


def sprinkle(rng):
    t = rng.uniform(0.0, T_BOX, N_POINTS)
    r = np.sqrt(rng.uniform(R_LO_BOX ** 2, R_HI_BOX ** 2, N_POINTS))
    phi = rng.uniform(0.0, 2.0 * math.pi, N_POINTS)
    return t, r, phi


def related(t, r, phi, tau):
    k = 0.5 / tau
    order, st = g.bh_order(t * k, r * k, phi, rng=None, audit=0)
    return order | order.T, st


def main() -> int:
    if os.path.exists(OUT):
        print(f"refusing to overwrite {OUT}", file=sys.stderr)
        return 1
    rng0 = np.random.default_rng(7_000_900)
    t, r, _ = sprinkle(rng0)
    k = 0.5 / 0.5
    mism, tot = g.radial_check(t * k, r * k)
    print("M0 radial mismatches:", mism, "of", tot, flush=True)
    viol, fracs, near = 0, [], 0
    for seed in SEEDS:
        rng = np.random.default_rng(seed)
        t, r, phi = sprinkle(rng)
        iu = np.triu_indices(N_POINTS, 1)
        prev, row = None, []
        for tau in TAUS:
            rel, st = related(t, r, phi, tau)
            near += st["near_boundary_pairs_tol"]
            cur = rel[iu]
            if prev is not None:
                viol += int(np.count_nonzero(cur & ~prev))
            prev = cur
            row.append(float(cur.mean()))
        fracs.append(row)
        print("seed", seed, "fractions", [round(x, 4) for x in row], "violations so far", viol, flush=True)
    F = np.array(fracs)
    diffs = F[:, 1:] - F[:, :-1]
    mean_d = diffs.mean(axis=0)
    se_d = diffs.std(axis=0, ddof=1) / math.sqrt(F.shape[0])
    m2 = bool(np.all(mean_d < 0) and np.all(-mean_d > 5 * se_d))
    failed = (["M0"] if mism else []) + (["M1"] if viol else []) + ([] if m2 else ["M2"])
    verdict = "MONOTONE_2P1_CONSISTENT" if not failed else "FAILED_" + "_".join(failed)
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                            cwd=HERE).stdout.strip()
    res = {"verdict": verdict, "repo_head": commit, "taus": TAUS.tolist(), "seeds": list(SEEDS),
           "n_points": N_POINTS, "box": [T_BOX, R_LO_BOX, R_HI_BOX], "M0_radial_mismatches": mism,
           "M0_radial_pairs": tot, "M1_violations": viol, "near_boundary_pairs_total": near,
           "p_mean": F.mean(axis=0).tolist(), "dp_mean_per_step": mean_d.tolist(),
           "dp_se_per_step": se_d.tolist(), "M2_pass": m2}
    with open(OUT, "x") as f:
        json.dump(res, f, indent=1)
    print(json.dumps({k: res[k] for k in ("verdict", "M1_violations", "p_mean", "dp_mean_per_step",
                                          "dp_se_per_step")}, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
