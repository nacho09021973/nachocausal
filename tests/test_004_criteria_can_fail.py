"""test_004_criteria_can_fail — comité 052 §5 / §9 step 4 (pre-freeze; verdicts discarded).

Feeds known-bad inputs to the CANDIDATE 2+1 verdict (nachocausal2p1.validate.summarise_level and
verdict_from_levels) and asserts each criterion goes FALSE and the verdict is FAIL. If a case
does not FAIL, that criterion is decoration and prereg-004 must not be frozen.

  baseline  a synthetic all-good grid gives PASS, so FAIL below is not guaranteed by construction.
  (a)       the dev rho=126, T=8 cell (coverage 0.20, dev/2P1_TMIN_RHO126_RESULT_2026-10-13.md)
            -> ii_localisation_primary false.
  (b)       synthetic flat control with 2 of 20 escapes -> iv false (control: 1 of 20 passes).
  (c)       the dev rho=126, T=20 widths scaled so the median is theta_loc*(1+eps) -> loc_pass
            false (control: (1-eps) -> true).
  (v)       Guard-v not run -> v_order_only false (auditor report 043, finding 1).

Only already-used exploration seeds (7_000_100..7_000_109, sweep 88a25f6) and synthetic rows are
used. The dev cells have 10 seeds, so (a) and (c) lower MIN_VALID_SEEDS to 10 in the test only
(as the comité bypasses the domain gate in the test only); without it the cell is INCONCLUSIVE,
which is asserted too. With 10 seeds (i) also fails (p >= 2^-10), so for (a) and (c) the
informative assertion is the specific check, not the overall FAIL. Nothing here prints or
asserts a comparison of theta with the dev widths (comité 052, leakage (c)).
"""

import functools
import hashlib
import json
import os

import numpy as np
import pytest

from nachocausal2p1 import thresholds, validate

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEV_SWEEP = os.path.join(ROOT, "dev", "2p1_sweep_T_rho126_v2_2026-10-12.jsonl")
# committed in 10d3ebe; the (a) and (c) inputs must not change silently
DEV_SWEEP_SHA256 = "13256b2925091f9e2d6c2a5f0eb4cd3410014a60f54a0477875ad018e2948e8d"
EPS = 1e-3
PRIM = thresholds.PRIMARY_RHO

pytestmark = pytest.mark.skipif(
    np.__version__ != thresholds.PINNED_NUMPY,
    reason=f"2+1 package pinned to numpy=={thresholds.PINNED_NUMPY}")


# --- inputs ----------------------------------------------------------------------------------
def _dev_cell(t_edge):
    """Dev rows at rho=126 and T=t_edge, converted to the port's per-seed row format
    (sep -> 0 when the gate abstains, as nachocausal2p1.estimator does)."""
    rows = []
    for line in open(DEV_SWEEP):
        rec = json.loads(line)
        if rec["T_EDGE"] != t_edge or rec["rho"] != float(PRIM):
            continue
        bh, mk = rec["BH"], rec["MINK"]
        sep_bh = 0.0 if bh["abstain"] else bh["sep"]
        sep_mk = 0.0 if mk["abstain"] else mk["sep"]
        row = {"seed": rec["seed"], "invalid": False, "abstained_BH": bh["abstain"],
               "abstained_MINK": mk["abstain"], "d": sep_bh - sep_mk, "valid": bh["claimed"]}
        if bh["claimed"]:
            w = bh["width_over_2M"] * thresholds.TWO_M
            row.update(width=w, clean=bool(w >= 0.0), midpoint=bh["mid"],
                       covers=bh["covers_2M"])
        rows.append(row)
    return rows


def _synthetic_rows(rho, escapes=0, n=thresholds.ENSEMBLE):
    """An all-good level: every seed claims, d > 0, bracket of width theta_loc/2 centred on 2M,
    flat control abstains except on the first `escapes` seeds."""
    w = 0.5 * thresholds.theta_loc(rho) * thresholds.TWO_M
    return [{"seed": i, "invalid": False, "abstained_BH": False, "abstained_MINK": i >= escapes,
             "d": 1.0 + 0.01 * i, "valid": True, "clean": True, "width": w,
             "midpoint": thresholds.TWO_M, "covers": True} for i in range(n)]


@functools.lru_cache(maxsize=None)
def _synthetic_level(rho, escapes=0):
    return validate.summarise_level(_synthetic_rows(rho, escapes), rho)


def _levels(primary):
    lv = {rho: dict(_synthetic_level(rho)) for rho in thresholds.RHO_GRID}
    lv[PRIM] = primary
    return lv


# --- provenance of the dev input -------------------------------------------------------------
def test_dev_cells_use_burned_exploration_seeds_only():
    for t_edge in (8.0, 20.0):
        seeds = [r["seed"] for r in _dev_cell(t_edge)]
        assert sorted(seeds) == list(thresholds.DRY_RUN_SEEDS)          # 10 seeds, 88a25f6
        assert all(thresholds.EXPLORE_BAND[0] <= s <= thresholds.EXPLORE_BAND[1] for s in seeds)
        assert not any(8_000_000 <= s <= 8_999_999 for s in seeds)       # virgin band untouched


def test_dev_sweep_is_pinned():
    sha = hashlib.sha256(open(DEV_SWEEP, "rb").read()).hexdigest()
    assert sha == DEV_SWEEP_SHA256


# --- baseline: the verdict CAN pass ----------------------------------------------------------
def test_synthetic_baseline_passes():
    out = validate.verdict_from_levels(_levels(dict(_synthetic_level(PRIM))), guard_ran=True)
    assert out["verdict"] == "PASS", out["checks"]


# --- (a) T=8 cell: localisation (ii) fails on coverage ---------------------------------------
def test_a_rho126_T8_fails_localisation(monkeypatch):
    rows = _dev_cell(8.0)
    assert validate.summarise_level(rows, PRIM)["status"] == "inconclusive"   # 10 < 18 seeds
    monkeypatch.setattr(thresholds, "MIN_VALID_SEEDS", len(rows))            # test-only bypass
    prim = validate.summarise_level(rows, PRIM)
    assert prim["status"] == "scored"
    assert prim["coverage_frac"] == pytest.approx(0.2)
    assert prim["coverage_frac"] < thresholds.COVERAGE_FLOOR
    out = validate.verdict_from_levels(_levels(prim), guard_ran=True)
    assert out["checks"]["ii_localisation_primary"] is False
    assert out["verdict"] == "FAIL"


# --- (b) flat control: 2 of 20 escapes fails (iv); 1 of 20 does not -------------------------
def test_b_two_flat_escapes_fail_iv():
    prim = dict(_synthetic_level(PRIM, escapes=2))
    assert prim["n_escape_MINK"] == 2
    out = validate.verdict_from_levels(_levels(prim), guard_ran=True)
    assert out["checks"]["iv_flat_escapes_primary"] is False
    assert [k for k, v in out["checks"].items() if not v] == ["iv_flat_escapes_primary"]
    assert out["verdict"] == "FAIL"


def test_b_control_one_flat_escape_passes():
    prim = dict(_synthetic_level(PRIM, escapes=1))
    out = validate.verdict_from_levels(_levels(prim), guard_ran=True)
    assert out["checks"]["iv_flat_escapes_primary"] is True
    assert out["verdict"] == "PASS"


# --- (c) T=20 widths scaled just above / below theta_loc ------------------------------------
def _scaled_cell(factor):
    rows = _dev_cell(20.0)
    widths = np.array([r["width"] / thresholds.TWO_M for r in rows if r["valid"] and r["clean"]])
    k = factor * thresholds.theta_loc(PRIM) / float(np.median(widths))     # never printed
    for r in rows:
        if r["valid"]:
            r["width"] *= k
    return rows


def test_c_widths_just_above_theta_fail_loc(monkeypatch):
    rows = _scaled_cell(1.0 + EPS)
    monkeypatch.setattr(thresholds, "MIN_VALID_SEEDS", len(rows))
    prim = validate.summarise_level(rows, PRIM)
    assert prim["status"] == "scored"
    assert prim["loc_pass"] is False
    out = validate.verdict_from_levels(_levels(prim), guard_ran=True)
    assert out["checks"]["ii_localisation_primary"] is False
    assert out["verdict"] == "FAIL"


def test_c_control_widths_just_below_theta_pass_loc(monkeypatch):
    rows = _scaled_cell(1.0 - EPS)
    monkeypatch.setattr(thresholds, "MIN_VALID_SEEDS", len(rows))
    assert validate.summarise_level(rows, PRIM)["loc_pass"] is True


# --- (a') synthetic: coverage alone below the floor fails (ii) -------------------------------
def test_a_synthetic_coverage_below_floor_fails_ii_only():
    rows = _synthetic_rows(PRIM)
    for r in rows[:11]:                                   # 9/20 = 0.45 < 0.5
        r["covers"] = False
    prim = validate.summarise_level(rows, PRIM)
    out = validate.verdict_from_levels(_levels(prim), guard_ran=True)
    assert [k for k, v in out["checks"].items() if not v] == ["ii_localisation_primary"]
    assert out["verdict"] == "FAIL"


# --- (v) Guard-v not run -> (v) false (auditor report 043, finding 1) ------------------------
def test_v_guard_off_fails_v_only():
    out = validate.verdict_from_levels(_levels(dict(_synthetic_level(PRIM))), guard_ran=False)
    assert [k for k, v in out["checks"].items() if not v] == ["v_order_only"]
    assert out["verdict"] == "FAIL"
