"""validate — the BLIND benchmark runner and FROZEN PASS/FAIL verdict.

Committed as part of the seal so the analysis is fixed in advance. In block #4
it is run ONLY on DEV_SEEDS via dry_run.py (verdict discarded). Step #5 runs it
on thresholds.VALIDATION_SEEDS and emits the committed verdict.

Order of operations (runnable guard, cmte M4): for each causet the estimator
produces O and the boundary threshold `thr` from the poset ALONE; Guard-v
(verify_order_only) RAISES if O is not order-only; only THEN is the embedding
revealed to the isolated scoring subpackage. The estimator never sees r.
"""

from __future__ import annotations

import json
import os
from typing import Dict, List

import numpy as np

from . import estimator, generator, thresholds
from .scoring import blind_bracket

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")


# =============================================================================
# Frozen statistical primitives.
# =============================================================================
def signflip_perm_p(d: np.ndarray) -> float:
    """One-sided paired sign-flip permutation p-value for H1: mean(d) > 0.
    d = per-seed sep_BH - sep_MINK on the SAME cloud (exchangeable under the
    no-horizon null). Enumerate 2^n sign flips exactly for n <= PERM_EXACT_MAX_N,
    else PERM_RANDOM_SAMPLES random flips. p = P(mean(+/- d) >= mean(d))."""
    d = np.asarray(d, float)
    d = d[np.isfinite(d)]
    n = d.size
    if n == 0:
        return float("nan")
    obs = d.mean()
    if n <= thresholds.PERM_EXACT_MAX_N:
        idx = np.arange(1 << n)
        bits = (idx[:, None] >> np.arange(n)[None, :]) & 1
        signs = 1 - 2 * bits  # 0 -> +1, 1 -> -1
        means = (signs * d[None, :]).mean(axis=1)
    else:
        rng = np.random.default_rng(0)
        signs = 1 - 2 * rng.integers(0, 2, size=(thresholds.PERM_RANDOM_SAMPLES, n))
        means = (signs * d[None, :]).mean(axis=1)
    return float(np.mean(means >= obs - 1e-12))


def loo_fp_fraction(mink_seps: np.ndarray) -> float:
    """Leave-one-out false-positive fraction: each MINK seed is a 'positive' iff
    its sep exceeds the FP_PERCENTILE of the held-out (other) MINK seps."""
    s = np.asarray(mink_seps, float)
    s = s[np.isfinite(s)]
    n = s.size
    if n < 3:
        return float("nan")
    flags = 0
    for i in range(n):
        null = np.delete(s, i)
        if s[i] > np.percentile(null, thresholds.FP_PERCENTILE):
            flags += 1
    return flags / n


def _iqr(x: np.ndarray) -> float:
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    if x.size < 2:
        return float("nan")
    q75, q25 = np.percentile(x, [75, 25])
    return float(q75 - q25)


# =============================================================================
# Per-seed blind phase (poset only) -> then reveal r to score.
# =============================================================================
def _per_seed(seed: int, intensity: float, guard: bool = True) -> dict:
    emb, edges, center = generator.numpy_sprinkle(seed, intensity)
    generator.assert_coordinate_uniform(emb, edges, center)  # Glue-3, can fail
    out: Dict[str, object] = {"seed": int(seed), "N": int(emb.shape[0])}
    blind = {}
    for kind in ("BH", "MINK"):
        C = generator.past_matrix_fast(emb, kind)
        if guard:
            estimator.verify_order_only(C, seed=seed)  # Guard-v: RAISES if not order-only
        O_by_min, min_idx, _ = estimator.estimate_O(C)
        thr, sep = estimator.two_means_split(list(O_by_min.values()))
        blind[kind] = (O_by_min, min_idx, thr, sep)
    # thr is now frozen from O alone for both kinds; ONLY now reveal r.
    O_bh, min_bh, thr_bh, sep_bh = blind["BH"]
    _, _, _, sep_mk = blind["MINK"]
    br = blind_bracket(O_bh, min_bh, thr_bh, emb)  # scoring: reveals r
    out.update(sep_BH=sep_bh, sep_MINK=sep_mk, d=sep_bh - sep_mk, **br)
    return out


def run_level(seeds, intensity: float, guard: bool = True) -> dict:
    rows = [_per_seed(s, intensity, guard) for s in seeds]
    valid = [r for r in rows if r["valid"] and np.isfinite(r["sep_MINK"])]
    n_valid = len(valid)
    lam_ell_2m = thresholds.ell(intensity) / thresholds.TWO_M
    res = {
        "intensity": intensity,
        "N_mean": float(np.mean([r["N"] for r in rows])),
        "n_valid": n_valid,
        "theta_loc": thresholds.theta_loc(intensity),
        "theta_stab": thresholds.theta_stab(intensity),
        "ell_over_2M": lam_ell_2m,
    }
    if n_valid < thresholds.MIN_VALID_SEEDS:
        res["status"] = "inconclusive"
        return res
    d = np.array([r["d"] for r in valid])
    res["p_perm"] = signflip_perm_p(d)
    res["significant"] = res["p_perm"] <= thresholds.P_PERM_THRESHOLD
    clean = [r for r in valid if r["clean"]]
    widths_2m = np.array([r["width"] / thresholds.TWO_M for r in clean])
    res["median_width_over_2M"] = float(np.median(widths_2m)) if widths_2m.size else float("nan")
    res["iqr_width_over_2M"] = _iqr(widths_2m)
    res["loc_pass"] = res["median_width_over_2M"] <= res["theta_loc"]
    res["loc_inconclusive"] = res["iqr_width_over_2M"] > res["theta_loc"]
    res["coverage_frac"] = float(np.mean([r["covers"] for r in valid]))
    mids = np.array([r["midpoint"] for r in clean])
    res["boundary_r_std"] = float(np.std(mids)) if mids.size else float("nan")
    res["stab_pass"] = res["boundary_r_std"] <= res["theta_stab"]
    res["fp_fraction"] = loo_fp_fraction([r["sep_MINK"] for r in valid])
    res["fp_pass"] = res["fp_fraction"] <= thresholds.THETA_FP
    res["status"] = "scored"
    return res


# =============================================================================
# Full run across the 4 N levels -> frozen verdict.
# =============================================================================
def run(seeds=None, label: str = "validation", guard: bool = True, write: bool = True) -> dict:
    thresholds.assert_environment()
    seeds = list(thresholds.VALIDATION_SEEDS if seeds is None else seeds)
    levels = {lam: run_level(seeds, lam, guard) for lam in thresholds.INTENSITIES}

    prim = levels[thresholds.PRIMARY_INTENSITY]
    verdict = {"label": label, "seeds": seeds, "levels": levels}

    if prim.get("status") != "scored":
        verdict["verdict"] = "INCONCLUSIVE"
        verdict["reason"] = f"primary N (intensity {thresholds.PRIMARY_INTENSITY}) inconclusive"
        if write:
            _write(verdict, label)
        return verdict

    # Convergence: sequence non-increasing within 1*ell slack across the 4 N.
    seq = [levels[lam] for lam in thresholds.INTENSITIES]
    slack_ok = True
    for k in range(len(seq) - 1):
        a, b = seq[k], seq[k + 1]
        if a.get("status") != "scored" or b.get("status") != "scored":
            slack_ok = False
            break
        if b["median_width_over_2M"] > a["median_width_over_2M"] + a["ell_over_2M"]:
            slack_ok = False
    # Significance at every N >= 3000.
    sig_all = all(
        levels[lam].get("significant", False)
        for lam in thresholds.INTENSITIES if lam >= 3000.0
    )

    checks = {
        "i_significant_primary_and_above_3000": bool(prim["significant"] and sig_all),
        "ii_localisation_primary": bool(prim["loc_pass"] and not prim["loc_inconclusive"]
                                        and prim["coverage_frac"] >= 0.5),
        "ii_convergence_slack": bool(slack_ok),
        "iii_stability_primary": bool(prim["stab_pass"]),
        "iv_false_positive_primary": bool(prim["fp_pass"]),
        # (v) Guard-v: no verify_order_only raised during the run -> order-only holds.
        "v_order_only": True,
    }
    verdict["checks"] = checks
    verdict["verdict"] = "PASS" if all(checks.values()) else "FAIL"
    if write:
        _write(verdict, label)
    return verdict


def _write(verdict: dict, label: str) -> str:
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, f"{label}.json")
    with open(path, "w") as f:
        json.dump(verdict, f, indent=2, default=float)
    return path
