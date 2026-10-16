"""dev exploration — numerical check of the root-score modulus bound, part (b).

NOT sealed; plain Monte Carlo/quadrature of the analytic model of
research_program/work_packages/wp6_domain_bridge_fixed_ef_box.md §1, like
dev/explore_create_fisher_quotient_check.py (commit dccc54b), whose quotient
representation Pi_n = phi(J, D, V) with phi tau-free is reused.

Claim checked (written before the first run). With A_n = sum of one-point scores
s = d_tau log f_tau(J, D) and B_n = sum of b = d_tau^2 log f_tau(J, D):
  pi_sigma'' = E[(A_n^2 + B_n) 1{phi = sigma}],  hence by Cauchy-Schwarz
  ||s_n''||_2^2 <= (9/8) E[A_n^4] + E[B_n^2],
  E[A_n^4] = n m4 + 3 n (n-1) J^2,   E[B_n^2] = n Var(b) + n^2 J^2,
so ||s_n''|| <= C_K n and Omega_{n,K}(eta) <= C_K n eta.

PRE-DECLARED checks:
  D1 information identity: |E[b] + J| < 1e-6 * J at each tau (guardrail on b).
  D2 moments finite: m4 and E[b^2] agree within 1e-4 relative between two
     quadrature resolutions.
  D3 bound: for n in {2, 3, 4} and tau in {0.4, 0.5, 0.7}, the Monte Carlo
     second-difference estimate of ||s_n''||_2 is <= bound_n + 3 se.
  Verdict MODULUS_BOUND_CONSISTENT if D1-D3 pass, else FAILED_<check>.
Numerical consistency at small n only; the bound for all n rests on the argument.

Run:  .venv/bin/python dev/explore_create_omega_modulus_check.py
Writes dev/explore_create_omega_modulus_check_results.json (refuses to overwrite).
"""

from __future__ import annotations

import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from explore_create_fisher_quotient_check import (  # noqa: E402
    L, NS, R_A, R_B, TAUS, perm_code, sample, score_t, sorted_by_v, u_coord)

OUT = os.path.join(HERE, "explore_create_omega_modulus_check_results.json")
MC_SEED = 20261017
MC_SETS = 20_000_000
MC_BATCHES = 10
H_MC = 0.05
H_FD = 1e-4


def t_of(d, eps, tau, t0):
    """Solve log t + eps t/tau = log t_b + eps t_b/tau - d/(2 tau) by Newton from t0."""
    b = np.where(eps > 0, R_B, R_A)
    tb = np.abs(b - tau)
    rhs = np.log(tb) + eps * tb / tau - d / (2.0 * tau)
    t = t0.copy()
    for _ in range(60):
        g = np.log(t) + eps * t / tau - rhs
        t = t - g / (1.0 / t + eps / tau)
    return t


def log_f(t, eps, tau):
    return np.log(t / (2.0 * L * (tau + eps * t)))


def moments(tau, m):
    J = m4 = eb = eb2 = 0.0
    for eps_v, b in ((-1.0, R_A), (1.0, R_B)):
        y = np.linspace(-np.log(abs(b - tau)), 30.0, m)
        t = np.exp(-y)
        eps = np.full_like(t, eps_v)
        tb = abs(b - tau)
        d = 2.0 * tau * np.log(tb / t) + 2.0 * eps * (tb - t)
        tp = t_of(d, eps, tau + H_FD, t)
        tm = t_of(d, eps, tau - H_FD, t)
        bb = (log_f(tp, eps, tau + H_FD) - 2.0 * log_f(t, eps, tau) + log_f(tm, eps, tau - H_FD)) / H_FD**2
        s = score_t(t, eps, tau)
        w = t / L
        J += np.trapz(s**2 * w, y)
        m4 += np.trapz(s**4 * w, y)
        eb += np.trapz(bb * w, y)
        eb2 += np.trapz(bb**2 * w, y)
    return {"J": float(J), "m4": float(m4), "Eb": float(eb), "Eb2": float(eb2)}


def bound(n, mo):
    ea4 = n * mo["m4"] + 3 * n * (n - 1) * mo["J"] ** 2
    eb2 = n * (mo["Eb2"] - mo["J"] ** 2) + n**2 * mo["J"] ** 2
    return float(np.sqrt(9.0 / 8.0 * ea4 + eb2))


def sddot_mc(rng, n, tau):
    k = n ** n
    per_batch = MC_SETS // MC_BATCHES
    vals, tot = [], np.zeros((3, k))
    for _ in range(MC_BATCHES):
        counts = np.zeros((3, k))
        done = 0
        while done < per_batch:
            m = min(2_000_000, per_batch - done)
            v, r = sample(rng, m, n)
            for i, tt in enumerate((tau - H_MC, tau, tau + H_MC)):
                counts[i] += np.bincount(perm_code(sorted_by_v(v, u_coord(v, r, tt))), minlength=k)
            done += m
        tot += counts
        s = np.sqrt(counts / per_batch)
        vals.append(float(np.linalg.norm((s[2] - 2 * s[1] + s[0]) / H_MC**2)))
    s = np.sqrt(tot / (per_batch * MC_BATCHES))
    est = float(np.linalg.norm((s[2] - 2 * s[1] + s[0]) / H_MC**2))
    return est, float(np.std(vals, ddof=1) / np.sqrt(MC_BATCHES))


def main() -> int:
    if os.path.exists(OUT):
        print(f"refusing to overwrite {OUT}", file=sys.stderr)
        return 1
    mom, failed = {}, []
    for tau in TAUS:
        a, b = moments(tau, 200_001), moments(tau, 800_001)
        rel = {k: abs(a[k] - b[k]) / abs(b[k]) for k in ("m4", "Eb2")}
        mom[str(tau)] = dict(b, rel_diff=rel, info_identity=abs(b["Eb"] + b["J"]) / b["J"])
        print("moments", tau, mom[str(tau)], flush=True)
    if any(x["info_identity"] >= 1e-6 for x in mom.values()):
        failed.append("D1")
    if any(max(x["rel_diff"].values()) >= 1e-4 for x in mom.values()):
        failed.append("D2")
    rng = np.random.default_rng(MC_SEED)
    d3 = {}
    for tau in TAUS:
        for n in NS:
            est, se = sddot_mc(rng, n, tau)
            bd = bound(n, mom[str(tau)])
            d3[f"{tau}/{n}"] = {"sddot_mc": est, "se": se, "bound": bd, "ratio": est / bd,
                                "bound_over_n": bd / n, "pass": est <= bd + 3 * se}
            print("D3", tau, n, d3[f"{tau}/{n}"], flush=True)
    if not all(x["pass"] for x in d3.values()):
        failed.append("D3")
    verdict = "MODULUS_BOUND_CONSISTENT" if not failed else "FAILED_" + "_".join(failed)
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                            cwd=HERE).stdout.strip()
    with open(OUT, "x") as f:
        json.dump({"verdict": verdict, "repo_head": commit, "h_mc": H_MC, "mc_sets": MC_SETS,
                   "mc_seed": MC_SEED, "moments": mom, "D3": d3}, f, indent=1)
    print("VERDICT:", verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
