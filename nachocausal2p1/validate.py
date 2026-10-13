"""validate — the BLIND 2+1 runner and its PASS/FAIL verdict (CANDIDATE, not frozen).

Port of nachocausal/validate.py to the 2+1 equatorial bench (comité 052 §9 step 3). Order of
operations per seed: GENERATE (validity checks) -> per kind: Guard-v -> ESTIMATE (order only)
-> GATE; the blind threshold is frozen from O; ONLY THEN is r revealed to the isolated scoring
subpackage. The estimator never receives r (split record: blind dict, then score dict).

Differences from 1+1 (all from comité 052 §8 and the PI decisions in §11):
  * thresholds keyed by rho at the frozen T, never by realised N;
  * separate counters: generator-INVALID seeds (assertion, audit disagreement, transitivity
    violation, radial-check mismatch) vs BH abstentions vs flat-control escapes;
  * INCONCLUSIVE is reserved for < MIN_VALID_SEEDS generator-valid seeds;
  * (i) at every rho >= SIGNIFICANCE_MIN_RHO, and >= BH_ABSTAIN_FAIL BH abstentions FAIL (i);
  * (ii) convergence slack restated over the rho grid with ell_rad;
  * (iv) as an explicit count of flat-control non-abstentions;
  * tau(n) for n > 256 aborts the run (gate RAISES);
  * results are written atomically (temp file + fsync + rename) and the validation label is
    one-shot: an existing results/validation_004.json is never overwritten.
"""

from __future__ import annotations

import json
import os
import tempfile
import time
from typing import Dict, List, Optional

import numpy as np

from . import estimator, generator, thresholds
from .scoring import blind_bracket

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
VALIDATION_LABEL = "validation_004"


# =============================================================================
# Frozen statistical primitives (as 1+1, with the 2+1 constants).
# =============================================================================
def signflip_perm_p(d) -> float:
    """One-sided exact paired sign-flip p-value for mean(d) > 0 (as nachocausal.validate)."""
    d = np.asarray(d, float)
    d = d[np.isfinite(d)]
    n = d.size
    if n == 0:
        return float("nan")
    obs = d.mean()
    if n <= thresholds.PERM_EXACT_MAX_N:
        idx = np.arange(1 << n)
        bits = (idx[:, None] >> np.arange(n)[None, :]) & 1
        means = ((1 - 2 * bits) * d[None, :]).mean(axis=1)
    else:
        rng = np.random.default_rng(0)
        signs = 1 - 2 * rng.integers(0, 2, size=(thresholds.PERM_RANDOM_SAMPLES, n))
        means = (signs * d[None, :]).mean(axis=1)
    return float(np.mean(means >= obs - 1e-12))


def _iqr(x) -> float:
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    if x.size < 2:
        return float("nan")
    q75, q25 = np.percentile(x, [75, 25])
    return float(q75 - q25)


# =============================================================================
# Generation with validity checks (an invalid seed is counted, never replaced).
# =============================================================================
def generate(seed: int, rho: float) -> dict:
    rng = np.random.default_rng(seed)
    t, r, phi = generator.sprinkle(thresholds.n_mean(rho), rng)
    reasons: List[str] = []
    stats: dict = {}
    try:
        bh, stats = generator.bh_order(t, r, phi, rng=rng, audit=thresholds.AUDIT_PAIRS)
    except AssertionError as exc:            # fine shooting missed
        return {"t": t, "r": r, "phi": phi, "bh": None, "mk": None, "stats": {},
                "invalid": True, "reasons": [f"generator_assertion: {exc}"]}
    mk = generator.mink_order(t, r, phi)
    for part, a in stats.get("audit_vs_fine", {}).items():
        if a["endpoint_failures"] or a["disagreements_among_hit"]:
            reasons.append(f"audit_{part}: {a}")
    tv_bh = generator.transitivity_violations(bh)
    tv_mk = generator.transitivity_violations(mk)
    mism, _ = generator.radial_check(t, r)
    stats.update(transitivity_violations_BH=tv_bh, transitivity_violations_MINK=tv_mk,
                 radial_check_mismatches=mism)
    if tv_bh:
        reasons.append(f"transitivity_BH={tv_bh}")
    if tv_mk:
        reasons.append(f"transitivity_MINK={tv_mk}")
    if mism:
        reasons.append(f"radial_check_mismatches={mism}")
    return {"t": t, "r": r, "phi": phi, "bh": bh, "mk": mk, "stats": stats,
            "invalid": bool(reasons), "reasons": reasons}


# =============================================================================
# Per-seed blind phase (order only) -> then reveal r to score.
# =============================================================================
def per_seed(seed: int, rho: float, guard: bool = True) -> dict:
    t0 = time.time()
    g = generate(seed, rho)
    row: Dict[str, object] = {"seed": int(seed), "rho": float(rho), "N": int(g["t"].size),
                              "invalid": g["invalid"], "invalid_reasons": g["reasons"],
                              "generator_stats": g["stats"]}
    if g["invalid"]:
        row["seconds"] = round(time.time() - t0, 1)
        return row
    blind = {kind: estimator.estimate(order, guard=guard, guard_seed=int(seed))
             for kind, order in (("BH", g["bh"]), ("MINK", g["mk"]))}
    # thr is frozen from O alone for both kinds; ONLY NOW is r revealed (BH only).
    bh, mk = blind["BH"], blind["MINK"]
    if bh["abstained"]:
        br = dict(valid=False, r_lo=float("nan"), r_hi=float("nan"), width=float("nan"),
                  midpoint=float("nan"), covers=False, clean=False)
    else:
        br = blind_bracket(bh["O_by_min"], bh["min_idx"], bh["thr"], g["r"])
    row.update(sep_BH=bh["sep"], sep_MINK=mk["sep"], d=bh["sep"] - mk["sep"],
               abstained_BH=bh["abstained"], abstained_MINK=mk["abstained"],
               n_minimal_BH=bh["n_minimal"], n_minimal_MINK=mk["n_minimal"],
               improvement_BH=bh["improvement"], improvement_MINK=mk["improvement"], **br)
    row["seconds"] = round(time.time() - t0, 1)
    return row


def summarise_level(rows: List[dict], rho: float) -> dict:
    """Level statistics from per-seed rows (pure function: used by run_level and by the
    step-4 can-fail test on synthetic rows)."""
    ok = [r for r in rows if not r["invalid"]]
    res = {
        "rho": float(rho),
        "n_mean": thresholds.n_mean(rho),
        "n_seeds": len(rows),
        "n_invalid": len(rows) - len(ok),
        "n_generator_valid": len(ok),
        "n_abstain_BH": int(sum(bool(r["abstained_BH"]) for r in ok)),
        "n_escape_MINK": int(sum(not r["abstained_MINK"] for r in ok)),
        "theta_loc": thresholds.theta_loc(rho),
        "theta_stab": thresholds.theta_stab(rho),
        "slack_over_2M": thresholds.convergence_slack(rho),
    }
    if len(ok) < thresholds.MIN_VALID_SEEDS:
        res["status"] = "inconclusive"
        return res
    res["p_perm"] = signflip_perm_p([r["d"] for r in ok])
    res["significant"] = bool(res["p_perm"] <= thresholds.P_PERM_THRESHOLD
                              and res["n_abstain_BH"] < thresholds.BH_ABSTAIN_FAIL)
    brk = [r for r in ok if r["valid"]]
    clean = [r for r in brk if r["clean"]]
    widths = np.array([r["width"] / thresholds.TWO_M for r in clean])
    res["n_bracket_valid"] = len(brk)
    res["n_clean"] = len(clean)
    res["median_width_over_2M"] = float(np.median(widths)) if widths.size else float("nan")
    res["iqr_width_over_2M"] = _iqr(widths)
    res["loc_pass"] = bool(res["median_width_over_2M"] <= res["theta_loc"])
    res["loc_inconclusive"] = bool(res["iqr_width_over_2M"] > res["theta_loc"])
    res["coverage_count"] = int(sum(bool(r["covers"]) for r in brk))
    res["coverage_frac"] = res["coverage_count"] / len(brk) if brk else float("nan")
    mids = np.array([r["midpoint"] for r in clean])
    res["boundary_r_std"] = float(np.std(mids)) if mids.size else float("nan")
    res["stab_pass"] = bool(res["boundary_r_std"] <= res["theta_stab"])
    res["escape_pass"] = bool(res["n_escape_MINK"] <= thresholds.MAX_MINK_ESCAPES)
    res["status"] = "scored"
    return res


def run_level(seeds, rho: float, guard: bool = True) -> dict:
    rows = [per_seed(s, rho, guard) for s in seeds]
    res = summarise_level(rows, rho)
    res["rows"] = rows
    return res


def verdict_from_levels(levels: Dict[float, dict]) -> dict:
    """Frozen-form verdict from level summaries (pure; exercised by the can-fail test)."""
    prim = levels[thresholds.PRIMARY_RHO]
    if prim.get("status") != "scored":
        return {"verdict": "INCONCLUSIVE",
                "reason": f"primary rho={thresholds.PRIMARY_RHO} has fewer than "
                          f"{thresholds.MIN_VALID_SEEDS} generator-valid seeds"}
    required = [rho for rho in thresholds.RHO_GRID if rho >= thresholds.SIGNIFICANCE_MIN_RHO]
    sig_ok = all(levels[rho].get("significant", False) for rho in required)
    slack_ok = True
    grid = list(thresholds.RHO_GRID)
    for a_rho, b_rho in zip(grid[:-1], grid[1:]):
        a, b = levels[a_rho], levels[b_rho]
        if a.get("status") != "scored" or b.get("status") != "scored":
            slack_ok = False
            break
        if b["median_width_over_2M"] > a["median_width_over_2M"] + a["slack_over_2M"]:
            slack_ok = False
    checks = {
        "i_significant_every_rho_ge_min": bool(sig_ok and prim["significant"]),
        "ii_localisation_primary": bool(prim["loc_pass"] and not prim["loc_inconclusive"]
                                        and prim["coverage_frac"] >= thresholds.COVERAGE_FLOOR),
        "ii_convergence_slack": bool(slack_ok),
        "iii_stability_primary": bool(prim["stab_pass"]),
        "iv_flat_escapes_primary": bool(prim["escape_pass"]),
        # (v) Guard-v: no verify_order_only raised during the run.
        "v_order_only": True,
    }
    return {"verdict": "PASS" if all(checks.values()) else "FAIL", "checks": checks}


# =============================================================================
# Full run -> verdict.
# =============================================================================
def run(seeds=None, label: str = VALIDATION_LABEL, guard: bool = True, write: bool = True,
        t_edge: Optional[float] = None) -> dict:
    thresholds.assert_environment()
    seeds = list(thresholds.VALIDATION_SEEDS if seeds is None else seeds)
    if not seeds:
        raise RuntimeError("no seeds: VALIDATION_SEEDS are not drawn (step C2 of comité 052).")
    if label == VALIDATION_LABEL:
        if thresholds.STATUS != "FROZEN" or tuple(seeds) != tuple(thresholds.VALIDATION_SEEDS):
            raise RuntimeError("the validation label is reserved for the single blind run on the "
                               "frozen VALIDATION_SEEDS after C1/C2.")
        if os.path.exists(_result_path(label)):
            raise RuntimeError(f"{_result_path(label)} exists: the blind run is one-shot.")
    t_edge = thresholds.T_EDGE if t_edge is None else float(t_edge)
    if t_edge < thresholds.T_EDGE_MIN:
        out = {"label": label, "seeds": seeds, "t_edge": t_edge, "verdict": "OUT_OF_DOMAIN",
               "reason": f"t_edge={t_edge} < T_EDGE_MIN={thresholds.T_EDGE_MIN} (not a FAIL)"}
        if write:
            write_atomic(out, label)
        return out
    if t_edge != generator.T_EDGE:
        raise RuntimeError("t_edge must equal the generator's literal T_EDGE (no T knob).")
    levels = {rho: run_level(seeds, rho, guard) for rho in thresholds.RHO_GRID}
    out = {"label": label, "status_of_thresholds": thresholds.STATUS, "seeds": seeds,
           "t_edge": t_edge, "levels": levels, **verdict_from_levels(levels)}
    if write:
        write_atomic(out, label)
    return out


def _result_path(label: str) -> str:
    return os.path.join(RESULTS_DIR, f"{label}.json")


def write_atomic(obj: dict, label: str) -> str:
    """Write results/<label>.json atomically: temp file in the same dir, fsync, rename."""
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = _result_path(label)
    fd, tmp = tempfile.mkstemp(prefix=f".{label}.", suffix=".tmp", dir=RESULTS_DIR)
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(obj, f, indent=2, default=_json_default)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
    return path


def _json_default(x):
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.floating,)):
        return float(x)
    if isinstance(x, np.ndarray):
        return x.tolist()
    return str(x)
