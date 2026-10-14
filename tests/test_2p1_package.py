"""Runnable guards for the prereg-004 CANDIDATE 2+1 sub-package (comité 052 §9 step 3).

1. The port is behaviour-preserving: the sealed generator equals dev/gen2p1_efbox.py bit for bit
   at the same T, and the estimator reproduces dev/explore_2p1_estimator.py's O, minimal set,
   threshold and sep.
2. T is a literal (no env knob) and the numba cache is off.
3. The tau fixture has the recorded SHA, n <= 128 equals the sealed 1+1 table, n > 256 raises.
4. Estimator/gate do not import the scoring subpackage, and the estimator source is coordinate-
   free; Guard-v RAISES when the observable is made label-dependent (it can fail).
5. Counters, the one-shot validation label and atomic writing behave as specified.
No test compares theta with widths on the real rho grid (comité 052, leakage (c)).
"""

import ast
import hashlib
import importlib
import inspect
import json
import math
import os
import subprocess
import sys

import numpy as np
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from nachocausal2p1 import estimator, gate, generator, thresholds, validate  # noqa: E402

pytestmark = pytest.mark.skipif(
    np.__version__ != thresholds.PINNED_NUMPY,
    reason=f"2+1 package pinned to numpy=={thresholds.PINNED_NUMPY}")

SMALL_N = 150
SEED = thresholds.DRY_RUN_SEEDS[0]


def _small_cloud(seed=SEED, n=SMALL_N):
    rng = np.random.default_rng(seed)
    return generator.sprinkle(n, rng)


# --- 1. behaviour-preserving port --------------------------------------------------------
def test_generator_bit_equal_to_dev_at_same_T():
    t, r, phi = _small_cloud()
    order, _ = generator.bh_order(t, r, phi, rng=None)
    port_sha = hashlib.sha256(np.packbits(order).tobytes()).hexdigest()
    code = (
        "import sys,hashlib,numpy as np;"
        f"sys.path.insert(0,{os.path.join(ROOT, 'dev')!r});"
        "import gen2p1_efbox as g;"
        f"rng=np.random.default_rng({SEED});t,r,phi=g.sprinkle({SMALL_N},rng);"
        "o,_=g.bh_order(t,r,phi,rng=None);"
        "print(hashlib.sha256(np.packbits(o).tobytes()).hexdigest())")
    env = dict(os.environ, NC2P1_T_EDGE=repr(thresholds.T_EDGE))
    out = subprocess.run([sys.executable, "-c", code], env=env, capture_output=True,
                         text=True, check=True).stdout.strip().splitlines()[-1]
    assert out == port_sha


def test_estimator_matches_dev_estimator():
    sys.path.insert(0, os.path.join(ROOT, "dev"))
    try:
        os.environ["NC2P1_T_EDGE"] = repr(thresholds.T_EDGE)
        dev = importlib.import_module("explore_2p1_estimator")
    finally:
        os.environ.pop("NC2P1_T_EDGE", None)
    t, r, phi = _small_cloud()
    for order in (generator.bh_order(t, r, phi)[0], generator.mink_order(t, r, phi)):
        e = estimator.estimate(order)
        d = dev.estimate(order)
        assert sorted(e["min_idx"]) == sorted(int(i) for i in d["minimal"])
        assert sorted(e["O_by_min"].values()) == sorted(int(x) for x in d["O"])
        assert e["thr"] == d["thr"] or (math.isnan(e["thr"]) and math.isnan(d["thr"]))
        if not e["abstained"]:
            assert e["sep"] == d["sep"]


# --- 2. literal T, cache off ---------------------------------------------------------------
def test_T_is_literal_and_cache_off():
    src = inspect.getsource(generator)
    assert "os.environ" not in src and "NC2P1_T_EDGE" not in src.split('"""', 2)[2]
    assert "cache=True" not in src
    assert generator.T_EDGE == thresholds.T_EDGE == 16.0
    assert thresholds.T_EDGE >= thresholds.T_EDGE_MIN


# --- 3. tau fixture ------------------------------------------------------------------------
def test_tau_fixture_sha_and_prefix():
    raw = open(gate.TAU_PATH, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == thresholds.TAU_FIXTURE_SHA256
    sealed = json.load(open(os.path.join(ROOT, "nachocausal", "fixtures", "tau_table.json")))
    for n in range(2, 129):
        assert gate.tau(n) == float(sealed["tau"][str(n)])
    assert gate.tau(256) > 0
    with pytest.raises(ValueError):
        gate.tau(257)


def test_theta_anchor_arithmetic():
    # ASTRA table (revisiones/2026-10-13-anclaje-theta-ciego/astra.md); arithmetic only.
    for rho, loc, stab in ((32, 0.09023, 0.04511), (63, 0.05744, 0.02872),
                           (126, 0.03619, 0.01809)):
        assert abs(thresholds.theta_loc(rho) - loc) < 5e-5
        assert abs(thresholds.theta_stab(rho) - stab) < 5e-5
        assert thresholds.convergence_slack(rho) == pytest.approx(thresholds.theta_loc(rho) / 2)


# --- 4. leakage and Guard-v ----------------------------------------------------------------
def test_estimator_and_gate_do_not_import_scoring():
    for mod in list(sys.modules):
        if mod.startswith("nachocausal2p1"):
            del sys.modules[mod]
    importlib.import_module("nachocausal2p1.estimator")
    importlib.import_module("nachocausal2p1.gate")
    assert not any(m.startswith("nachocausal2p1.scoring") for m in sys.modules)


def test_estimator_source_is_coordinate_free():
    tree = ast.parse(inspect.getsource(estimator))
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.Module)) and ast.get_docstring(node):
            node.body = node.body[1:]
    code = ast.unparse(tree)
    for forbidden in ("scoring", "embedding", "phi", "to_kruskal", ".r ", "[:, 1]"):
        assert forbidden not in code, forbidden


def test_guard_v_can_fail(monkeypatch):
    from nachocausal import estimator as sealed
    t, r, phi = _small_cloud()
    order = generator.mink_order(t, r, phi)
    estimator.estimate(order)                      # real order-only O: no raise
    orig = sealed.estimate_O_volume

    def label_dependent(C):
        O, mn = orig(C)
        if mn:
            O[mn[0]] += 1
        return O, mn
    monkeypatch.setattr(sealed, "estimate_O_volume", label_dependent)
    with pytest.raises(ValueError, match="Guard"):
        estimator.estimate(order)


# --- 5. counters, one-shot label, atomic write ---------------------------------------------
def _row(abst_bh=False, abst_mk=True, invalid=False):
    if invalid:
        return {"invalid": True}
    return {"invalid": False, "abstained_BH": abst_bh, "abstained_MINK": abst_mk,
            "d": 0.0 if abst_bh else 5.0, "valid": not abst_bh, "clean": not abst_bh,
            "width": 0.0, "midpoint": 0.5, "covers": True}


def test_counters_are_separate():
    rows = [_row() for _ in range(15)] + [_row(abst_bh=True)] * 2 + [_row(abst_mk=False)] * 2 \
        + [_row(invalid=True)]
    s = validate.summarise_level(rows, thresholds.PRIMARY_RHO)
    assert (s["n_invalid"], s["n_abstain_BH"], s["n_escape_MINK"]) == (1, 2, 2)
    assert s["status"] == "scored" and s["escape_pass"] is False


def test_too_many_invalid_is_inconclusive():
    rows = [_row() for _ in range(17)] + [_row(invalid=True)] * 3
    assert validate.summarise_level(rows, thresholds.PRIMARY_RHO)["status"] == "inconclusive"


def test_validation_label_refuses_before_freeze():
    with pytest.raises(RuntimeError):
        validate.run(seeds=list(thresholds.DRY_RUN_SEEDS), label=validate.VALIDATION_LABEL,
                     write=False)
    with pytest.raises(RuntimeError):
        validate.run(seeds=None, label="x", write=False)


def test_atomic_write(tmp_path, monkeypatch):
    monkeypatch.setattr(validate, "RESULTS_DIR", str(tmp_path))
    p = validate.write_atomic({"a": np.float64(1.5), "b": np.int64(2)}, "probe")
    assert json.load(open(p)) == {"a": 1.5, "b": 2}
    assert [f for f in os.listdir(tmp_path) if f.endswith(".tmp")] == []


def test_environment_assertion_can_fail(monkeypatch):
    thresholds.assert_environment()
    monkeypatch.setenv("NC2P1_DEVICE", "gpu")
    with pytest.raises(RuntimeError):
        thresholds.assert_environment()


# --- 6. seed guard and Guard-v enforcement (auditor report 043, findings 1-2) --------------
VIRGIN_20 = tuple(range(8_000_000, 8_000_020))


def _no_generation(*a, **k):
    raise AssertionError("generation must not be reached")


def test_seed_guard_can_fail(monkeypatch):
    validate.check_seed(thresholds.DRY_RUN_SEEDS[0])
    for bad in (8_000_001, 12345, 6_999_999, 7_001_000):
        with pytest.raises(RuntimeError):
            validate.check_seed(bad)
    monkeypatch.setattr(thresholds, "VALIDATION_SEEDS", VIRGIN_20)
    with pytest.raises(RuntimeError):                    # drawn but not frozen
        validate.check_seed(VIRGIN_20[0])
    monkeypatch.setattr(thresholds, "STATUS", "FROZEN")
    validate.check_seed(VIRGIN_20[0])                    # frozen and drawn: allowed
    with pytest.raises(RuntimeError):
        validate.check_seed(VIRGIN_20[0] + 100)          # virgin but not drawn


def test_run_refuses_bad_seeds_before_generation(monkeypatch):
    monkeypatch.setattr(validate, "generate", _no_generation)
    with pytest.raises(RuntimeError, match="virgin"):
        validate.run(seeds=[8_000_001], label="probe", write=False)
    monkeypatch.setattr(thresholds, "STATUS", "FROZEN")
    monkeypatch.setattr(thresholds, "VALIDATION_SEEDS", VIRGIN_20)
    with pytest.raises(RuntimeError, match="validation label"):
        validate.run(seeds=[VIRGIN_20[0]], label="probe", write=False)


def test_validation_label_requires_guard(monkeypatch, tmp_path):
    monkeypatch.setattr(validate, "generate", _no_generation)
    monkeypatch.setattr(validate, "RESULTS_DIR", str(tmp_path))
    monkeypatch.setattr(thresholds, "STATUS", "FROZEN")
    monkeypatch.setattr(thresholds, "VALIDATION_SEEDS", VIRGIN_20)
    with pytest.raises(RuntimeError, match="Guard-v"):
        validate.run(seeds=None, label=validate.VALIDATION_LABEL, guard=False, write=False)


def test_check_validation_seeds_can_fail():
    thresholds.check_validation_seeds(())
    thresholds.check_validation_seeds(VIRGIN_20)
    for bad in (VIRGIN_20[:19], VIRGIN_20[:19] + (VIRGIN_20[0],),
                VIRGIN_20[:19] + (7_000_500,), VIRGIN_20[:19] + (12345,)):
        with pytest.raises(ValueError):
            thresholds.check_validation_seeds(bad)


def test_port_relation_count_and_T_discrimination():
    # Counts recorded in dev/PREREG004_STEP_3_2026-10-13.md (auditor report 043, warning 5).
    t, r, phi = _small_cloud()
    order, _ = generator.bh_order(t, r, phi, rng=None)
    assert int(order.sum()) == 8652
    code = (
        "import sys,numpy as np;"
        f"sys.path.insert(0,{os.path.join(ROOT, 'dev')!r});"
        "import gen2p1_efbox as g;"
        f"rng=np.random.default_rng({SEED});t,r,phi=g.sprinkle({SMALL_N},rng);"
        "o,_=g.bh_order(t,r,phi,rng=None);print(int(o.sum()))")
    env = dict(os.environ, NC2P1_T_EDGE="6.0")
    out = subprocess.run([sys.executable, "-c", code], env=env, capture_output=True,
                         text=True, check=True).stdout.strip().splitlines()[-1]
    assert int(out) == 5125


# --- 7. blind-run thread count (O3) and per-seed progress log (O4), 2026-10-14 ---------------
def test_blind_threads_can_fail(monkeypatch):
    import numba
    monkeypatch.delenv("NUMBA_NUM_THREADS", raising=False)
    with pytest.raises(RuntimeError, match="NUMBA_NUM_THREADS"):
        thresholds.assert_blind_threads()
    monkeypatch.setenv("NUMBA_NUM_THREADS", "20")
    monkeypatch.setattr(numba, "get_num_threads", lambda: 4)
    with pytest.raises(RuntimeError, match="NUMBA_NUM_THREADS"):
        thresholds.assert_blind_threads()           # env says 20, numba runs on 4
    monkeypatch.setattr(numba, "get_num_threads", lambda: 20)
    thresholds.assert_blind_threads()               # both 20: allowed
    monkeypatch.setenv("NUMBA_NUM_THREADS", "4")
    with pytest.raises(RuntimeError, match="NUMBA_NUM_THREADS"):
        thresholds.assert_blind_threads()


def test_validation_run_checks_threads_before_generation(monkeypatch, tmp_path):
    import numba
    monkeypatch.setattr(validate, "generate", _no_generation)
    monkeypatch.setattr(validate, "RESULTS_DIR", str(tmp_path))
    monkeypatch.setattr(thresholds, "STATUS", "FROZEN")
    monkeypatch.setattr(thresholds, "VALIDATION_SEEDS", VIRGIN_20)
    monkeypatch.setenv("NUMBA_NUM_THREADS", "4")
    monkeypatch.setattr(numba, "get_num_threads", lambda: 4)
    with pytest.raises(RuntimeError, match="NUMBA_NUM_THREADS"):
        validate.run(seeds=None, label=validate.VALIDATION_LABEL, write=False)
    assert os.listdir(tmp_path) == []


def test_progress_line_is_blind():
    row = dict(_row(), seed=7_000_100, rho=126.0, seconds=1.0, r_lo=0.2, r_hi=0.3, width=0.1,
               midpoint=0.25, covers=True, clean=True, sep_BH=1.0, sep_MINK=0.0, d=1.0)
    line = validate.progress_line(row)
    assert tuple(line) == validate.PROGRESS_FIELDS
    leaky = {"r_lo", "r_hi", "width", "midpoint", "covers", "clean", "valid", "sep_BH",
             "sep_MINK", "d", "theta_loc", "theta_stab"}
    assert not leaky & set(validate.PROGRESS_FIELDS)
    assert not leaky & set(line)


def test_progress_log_written_per_seed_before_the_verdict(monkeypatch, tmp_path):
    monkeypatch.setattr(validate, "RESULTS_DIR", str(tmp_path))
    calls = []

    def fake_per_seed(seed, rho, guard=True):
        path = validate._progress_path("probe")
        n_before = sum(1 for _ in open(path)) if os.path.exists(path) else 0
        calls.append(n_before)
        return dict(_row(), seed=seed, rho=rho, seconds=0.0)

    monkeypatch.setattr(validate, "per_seed", fake_per_seed)
    seeds = list(thresholds.DRY_RUN_SEEDS[:3])
    validate.run(seeds=seeds, label="probe", write=True)
    lines = [json.loads(x) for x in open(validate._progress_path("probe"))]
    assert lines[0]["event"] == "start"
    body = lines[1:]
    assert len(body) == len(seeds) * len(thresholds.RHO_GRID)
    assert all(set(x) == set(validate.PROGRESS_FIELDS) for x in body)
    assert calls == list(range(1, 1 + len(body)))   # each line is on disk before the next seed
    validate.run(seeds=seeds, label="probe", write=False)
    assert sum(1 for _ in open(validate._progress_path("probe"))) == len(lines)  # write=False: none
