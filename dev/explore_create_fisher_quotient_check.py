"""dev exploration — numerical check of a CREATE route for UNIFORM_IN_N_REGULARITY.

NOT sealed. No causal-set ensembles, no DEV/VALIDATION seeds of the sealed track:
plain Monte Carlo of the analytic model of
research_program/work_packages/wp6_domain_bridge_fixed_ef_box.md §1 (fixed EF box,
parameter tau = 2M, causal order = product order in null coordinates (u, v)).

Origin: CREATE test of 2026-10-16
(~/herramientas/CREATE/runs/2026-10-16-fisher-uniforme-n/). claude-opus-5-5 (route 1)
and gpt-6-astra (route 1) proposed independently the same idea, UNVERIFIED:

  J = 1{r > tau} (side of the horizon), b_J = r_b (exterior) or r_a (interior),
  D = 2 tau log(|W_tau(b_J)| / |W_tau(r)|) >= 0,   V = v.
  Then u < 0 exactly on the exterior and u > 0 on the interior. Within a side, the
  u-order is the (D + V)-order (ascending outside, descending inside). So
  Pi_n = phi((J_i, D_i, V_i)_i) with phi INDEPENDENT of tau, while (J, D) has the
  FIXED support {int, ext} x [0, inf) and density f_tau(j, d) = |r - tau| / (2 L r).
  If that one-point family is regular with Fisher information J(tau) < inf, data
  processing gives  I_n^Pi(tau) <= n J(tau)  (linear, not factorial).

PRE-DECLARED checks (written before the first run):
  C1 representation: on 200 000 samples of n = 6 points per tau, the permutation
     from u_tau equals the permutation from the fixed rule in 100% of the samples.
  C2 one-point Fisher: |E[score]| < 1e-6 * sqrt(J); J agrees within 1e-4 relative
     between two quadrature resolutions; the implicit score agrees with a
     finite-difference score (by root finding) within 1e-5 relative on test points.
  C3 bound: for n in {2, 3, 4} and tau in {0.4, 0.5, 0.7}, the Monte Carlo estimate
     of I_n^Pi(tau) satisfies I_n <= n J + 3 se.
  Verdict BOUND_CONSISTENT if C1-C3 all pass, otherwise FAILED_<check>.
  Passing is numerical consistency on one box, not a proof.

Box: the sealed one, r in [0.1, 1.3], v in [0, 6] (thresholds.py:37-40).
Run:  .venv/bin/python dev/explore_create_fisher_quotient_check.py
Writes dev/explore_create_fisher_quotient_check_results.json (refuses to overwrite).
"""

from __future__ import annotations

import itertools
import json
import os
import subprocess
import sys

import numpy as np
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "explore_create_fisher_quotient_check_results.json")
R_A, R_B, T = 0.1, 1.3, 6.0
L = R_B - R_A
TAUS = (0.4, 0.5, 0.7)
NS = (2, 3, 4)
MC_SEED = 20261016
MC_SETS = 20_000_000
MC_BATCHES = 10
DELTA = 0.01


def W(r, tau):
    return np.exp(r / tau) * (r / tau - 1.0)


def u_coord(v, r, tau):
    return -np.exp(-v / (2.0 * tau)) * W(r, tau)


def D_coord(r, tau):
    b = np.where(r > tau, R_B, R_A)
    return 2.0 * tau * np.log(np.abs(W(b, tau)) / np.abs(W(r, tau)))


def perm_code(keys_by_v_order):
    """Code of the permutation 'rank in u of the k-th point in v-order'."""
    ranks = np.argsort(np.argsort(keys_by_v_order, axis=1), axis=1)
    n = ranks.shape[1]
    return (ranks * (n ** np.arange(n))).sum(axis=1)


def sample(rng, m, n):
    return rng.random((m, n)) * T, R_A + rng.random((m, n)) * L


def sorted_by_v(v, x):
    idx = np.argsort(v, axis=1)
    return np.take_along_axis(x, idx, axis=1)


def check_c1(rng):
    out = {}
    for tau in TAUS:
        v, r = sample(rng, 200_000, 6)
        from_u = perm_code(sorted_by_v(v, u_coord(v, r, tau)))
        s = D_coord(r, tau) + v
        key = np.where(r > tau, s - 1e9, 1e9 - s)
        from_rule = perm_code(sorted_by_v(v, key))
        out[str(tau)] = int(np.count_nonzero(from_u != from_rule))
    return out


def score_t(t, eps, tau):
    """d/dtau log f_tau(j, d) at fixed (j, d), as a function of t = |r - tau| > 0.
    Uses d = 2 tau log(t_b / t) + 2 eps (t_b - t), exact and stable near the horizon."""
    b = np.where(eps > 0, R_B, R_A)
    tb = np.abs(b - tau)
    d = 2.0 * tau * np.log(tb / t) + 2.0 * eps * (tb - t)
    g_t = 1.0 / t + eps / tau
    g_tau = -eps * t / tau**2 + eps / tb + 1.0 / tau + eps * tb / tau**2 - d / (2.0 * tau**2)
    dt = -g_tau / g_t
    return dt / t - (1.0 + eps * dt) / (tau + eps * t)


def score_implicit(r, tau):
    eps = np.where(r > tau, 1.0, -1.0)
    return score_t(np.abs(r - tau), eps, tau)


def log_f(j_ext, d, tau):
    b = R_B if j_ext else R_A
    lo, hi = (tau + 1e-15, R_B) if j_ext else (R_A, tau - 1e-15)
    r = brentq(lambda x: D_coord(np.array(x), tau) - d, lo, hi, xtol=1e-15, rtol=1e-15)
    return np.log(abs(r - tau) / (2.0 * L * r))


def fisher_one_point(tau, m):
    """Quadrature in t = |r - tau| = exp(-y) on each side (r uniform, density 1/L)."""
    total, mean = 0.0, 0.0
    for eps, b in ((-1.0, R_A), (1.0, R_B)):
        y = np.linspace(-np.log(abs(b - tau)), 30.0, m)
        t = np.exp(-y)
        w = t / L
        s = score_t(t, eps, tau)
        total += np.trapz(s**2 * w, y)
        mean += np.trapz(s * w, y)
    return float(total), float(mean)


def check_c2():
    out = {}
    for tau in TAUS:
        J1, m1 = fisher_one_point(tau, 200_001)
        J2, _ = fisher_one_point(tau, 800_001)
        fd = []
        for r0 in (R_A + 0.05, tau - 0.01, tau + 1e-4, tau + 0.2, R_B - 0.05):
            j_ext = r0 > tau
            d0 = float(D_coord(np.array(r0), tau))
            h = 1e-6
            num = (log_f(j_ext, d0, tau + h) - log_f(j_ext, d0, tau - h)) / (2 * h)
            ana = float(score_implicit(np.array(r0), tau))
            fd.append(abs(num - ana) / max(1.0, abs(ana)))
        out[str(tau)] = {"J": J2, "J_rel_diff": abs(J1 - J2) / J2, "mean_score": m1,
                         "fd_max_rel_err": max(fd)}
    return out


def fisher_mc(rng, n, tau):
    """I_n^Pi by common-random-numbers central differences; batch-means se."""
    k = n ** n
    per_batch = MC_SETS // MC_BATCHES
    vals = []
    counts_tot = np.zeros((3, k))
    for _ in range(MC_BATCHES):
        counts = np.zeros((3, k))
        done = 0
        while done < per_batch:
            m = min(2_000_000, per_batch - done)
            v, r = sample(rng, m, n)
            for i, tt in enumerate((tau - DELTA, tau, tau + DELTA)):
                counts[i] += np.bincount(perm_code(sorted_by_v(v, u_coord(v, r, tt))), minlength=k)
            done += m
        counts_tot += counts
        p = counts / per_batch
        dp = (p[2] - p[0]) / (2 * DELTA)
        ok = p[1] > 0
        vals.append(float(np.sum(dp[ok] ** 2 / p[1][ok])))
    p = counts_tot / (per_batch * MC_BATCHES)
    dp = (p[2] - p[0]) / (2 * DELTA)
    ok = p[1] > 0
    est = float(np.sum(dp[ok] ** 2 / p[1][ok]))
    se = float(np.std(vals, ddof=1) / np.sqrt(MC_BATCHES))
    n_perm = int(np.count_nonzero(ok))
    return est, se, n_perm


def main() -> int:
    if os.path.exists(OUT):
        print(f"refusing to overwrite {OUT}", file=sys.stderr)
        return 1
    rng = np.random.default_rng(MC_SEED)
    c1 = check_c1(rng)
    print("C1 mismatches:", c1, flush=True)
    c2 = check_c2()
    print("C2:", json.dumps(c2), flush=True)
    c3 = {}
    for tau in TAUS:
        J = c2[str(tau)]["J"]
        for n in NS:
            est, se, n_perm = fisher_mc(rng, n, tau)
            c3[f"{tau}/{n}"] = {"I_n_mc": est, "se": se, "n_J": n * J, "ratio": est / (n * J),
                                "perms_seen": n_perm, "pass": est <= n * J + 3 * se}
            print(f"C3 tau={tau} n={n}:", c3[f"{tau}/{n}"], flush=True)
    failed = []
    if any(c1.values()):
        failed.append("C1")
    if any(x["J_rel_diff"] >= 1e-4 or abs(x["mean_score"]) >= 1e-6 * np.sqrt(x["J"])
           or x["fd_max_rel_err"] >= 1e-5 for x in c2.values()):
        failed.append("C2")
    if not all(x["pass"] for x in c3.values()):
        failed.append("C3")
    verdict = "BOUND_CONSISTENT" if not failed else "FAILED_" + "_".join(failed)
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                            cwd=HERE).stdout.strip()
    result = {"verdict": verdict, "repo_head": commit, "box": [R_A, R_B, T], "delta": DELTA,
              "mc_sets": MC_SETS, "mc_seed": MC_SEED, "C1_mismatches": c1, "C2": c2, "C3": c3}
    with open(OUT, "x") as f:
        json.dump(result, f, indent=1)
    print("VERDICT:", verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
