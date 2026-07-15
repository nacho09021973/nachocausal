"""OP-2.1 reference certifier suite (dev prereg OP21 §5; decision 034 R3).

Not part of the prereg-002 evaluation path and never run by the canonical
`make test` (`pytest tests/`): it lives under `certifier/tests/` on purpose.

Layout:
  - Deterministic guard tests (G1-G6, C5 semantics, exact-p0 sanity): no RNG draw,
    safe to run before the prereg freeze commit.
  - Monte Carlo tests: gated behind the prereg freeze — the dev smoke uses a reduced
    n_rep (uncitable dev work), and the full terminal-issuing run happens exactly
    once via `python -m certifier.bench --terminal` (dev prereg OP21 §7), not here.
"""

from __future__ import annotations

import ast
import math
import os
import pathlib

import numpy as np
import pytest

from certifier import bench, kernel
from certifier.kernel import (
    DomainError,
    STATE_ABSTAIN_GENERATOR_ERROR,
    STATE_ABSTAIN_PRECISION,
    STATE_BOUND_POSITIVE,
    STATE_ZERO_BOUND,
    certify_tv_lower,
    hoeffding_radius,
)
from certifier.ledger import (
    CertificationLedger,
    LedgerError,
    LedgerOverdraft,
    SequentialUseError,
)

_HALF = np.full(32, 0.5)


# --- kernel formula (op13:59-76) ------------------------------------------------

def test_radius_matches_frozen_formula() -> None:
    assert hoeffding_radius(200, 0.01) == math.sqrt(math.log(4.0 / 0.01) / 400.0)
    assert hoeffding_radius(50, 0.25) == math.sqrt(math.log(16.0) / 100.0)


def test_radius_rejects_bad_inputs() -> None:
    for m, alpha in [(0, 0.1), (-3, 0.1), (2.5, 0.1), (True, 0.1),
                     (10, 0.0), (10, 1.0), (10, -0.2), (10, "x")]:
        with pytest.raises(DomainError):
            hoeffding_radius(m, alpha)


def test_bound_value_is_exact_on_extreme_streams() -> None:
    zeros, ones = np.zeros(100), np.ones(100)
    cert = certify_tv_lower(zeros, ones, 0.05, 0.0, 0.0)
    r = hoeffding_radius(100, 0.05)
    assert cert.state == STATE_BOUND_POSITIVE
    assert cert.tv_lower == 1.0 - 2.0 * r
    assert cert.r_p == cert.r_q == r


# --- G1: [0,1]-domain guard (must be able to fail) --------------------------------

@pytest.mark.parametrize("bad", [
    np.array([0.2, 1.5]),
    np.array([-0.1, 0.5]),
    np.array([0.3, np.nan]),
    np.array([0.3, np.inf]),
    np.zeros((4, 4)),
    np.array([]),
    ["a", "b"],
])
def test_g1_domain_guard_raises(bad) -> None:
    with pytest.raises((DomainError, ValueError)):
        certify_tv_lower(bad, _HALF, 0.1, 0.0, 0.0)
    with pytest.raises((DomainError, ValueError)):
        certify_tv_lower(_HALF, bad, 0.1, 0.0, 0.0)


def test_g1_kernel_accepts_no_poset_like_object() -> None:
    with pytest.raises((DomainError, ValueError, TypeError)):
        certify_tv_lower({frozenset({(0, 1)}): 1.0}, _HALF, 0.1, 0.0, 0.0)


# --- C5: distinct return states (op13:122-133; falsifier verdict-coercion fix) ----

def test_c5_generator_error_abstention_is_mandatory() -> None:
    for bad_eps in [None, math.nan, -0.1, "0.0", True]:
        cert = certify_tv_lower(_HALF, _HALF, 0.1, bad_eps, 0.0)
        assert cert.state == STATE_ABSTAIN_GENERATOR_ERROR
        assert cert.tv_lower is None  # an abstention reports NO bound


def test_c5_precision_abstention_distinct_from_zero_bound() -> None:
    abstain = certify_tv_lower(_HALF, _HALF, 0.1, 0.0, 0.0, precision_budget=0.01)
    assert abstain.state == STATE_ABSTAIN_PRECISION and abstain.tv_lower is None
    zero = certify_tv_lower(_HALF, _HALF, 0.1, 0.0, 0.0)
    assert zero.state == STATE_ZERO_BOUND and zero.tv_lower == 0.0


def test_c5_precision_budget_validated() -> None:
    for bad in [0.0, -1.0, math.nan, math.inf, "x"]:
        with pytest.raises(DomainError):
            certify_tv_lower(_HALF, _HALF, 0.1, 0.0, 0.0, precision_budget=bad)


# --- G4: ledger budget (op13:44,110-120) -------------------------------------------

def test_g4_overdraft_raises() -> None:
    ledger = CertificationLedger(0.05)
    ledger.register_cell("a", 10, 10, 0.03, 0.0, 0.0)
    with pytest.raises(LedgerOverdraft):
        ledger.register_cell("b", 10, 10, 0.03, 0.0, 0.0)


def test_g4_duplicate_cell_and_post_freeze_registration_raise() -> None:
    ledger = CertificationLedger(0.5)
    ledger.register_cell("a", 10, 10, 0.1, 0.0, 0.0)
    with pytest.raises(LedgerError):
        ledger.register_cell("a", 20, 20, 0.1, 0.0, 0.0)
    ledger.freeze()
    with pytest.raises(LedgerError):
        ledger.register_cell("b", 10, 10, 0.1, 0.0, 0.0)


def test_g4_certify_requires_freeze() -> None:
    ledger = CertificationLedger(0.5)
    ledger.register_cell("a", 32, 32, 0.1, 0.0, 0.0)
    with pytest.raises(LedgerError):
        ledger.certify_cell("a", _HALF, _HALF)


# --- G5: structural rejection of the sequential path (op13:141-151) -----------------

def test_g5_second_certification_raises() -> None:
    ledger = CertificationLedger(0.5)
    ledger.register_cell("a", 32, 32, 0.1, 0.0, 0.0)
    ledger.freeze()
    ledger.certify_cell("a", _HALF, _HALF)
    with pytest.raises(SequentialUseError):
        ledger.certify_cell("a", _HALF, _HALF)


def test_g5_wrong_length_stream_raises() -> None:
    ledger = CertificationLedger(0.5)
    ledger.register_cell("a", 32, 32, 0.1, 0.0, 0.0)
    ledger.freeze()
    with pytest.raises(SequentialUseError):
        ledger.certify_cell("a", np.full(31, 0.5), _HALF)   # shrunk
    with pytest.raises(SequentialUseError):
        ledger.certify_cell("a", np.full(33, 0.5), _HALF)   # grown


def test_g5_no_incremental_entry_point_exists() -> None:
    public = {name for name in dir(CertificationLedger) if not name.startswith("_")}
    assert public == {"register_cell", "freeze", "certify_cell", "manifest"}
    for forbidden in ("add", "append", "update", "extend", "push", "feed", "observe"):
        assert not any(forbidden in name.lower() for name in public)


# --- G3: seed band -------------------------------------------------------------------

def test_g3_seed_rule_and_band() -> None:
    assert bench.synth_seed(0, 0) == 3_000_000
    assert bench.synth_seed(2, 500) == 3_002_500
    with pytest.raises(bench.SeedBandError):
        bench.synth_seed(0, 7)          # outside the frozen derivation rule
    with pytest.raises(bench.SeedBandError):
        bench.synth_seed(1_200, 0)      # would leave SYNTH_MC_BAND


def test_g3_band_disjoint_from_frozen_bands() -> None:
    from nachocausal import thresholds

    low, high = bench.SYNTH_MC_BAND
    assert all(not (low <= s <= high) for s in thresholds.DEV_SEEDS)
    assert all(not (low <= s <= high) for s in thresholds.VALIDATION_SEEDS)
    assert high < 4_000_000 and low > 2_999_999  # virgin band [2_000_000, 2_999_999]


# --- G6: import firewall (source-level, per dev prereg OP21 §1) ----------------------

_FORBIDDEN_SEALED = {"validate", "estimator", "generator", "gate", "scoring", "c1_selector"}


def test_g6_certifier_never_imports_the_sealed_path() -> None:
    pkg_dir = pathlib.Path(bench.__file__).resolve().parent
    sources = list(pkg_dir.glob("*.py"))
    assert sources, "certifier package sources not found"
    for src in sources:
        tree = ast.parse(src.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    parts = alias.name.split(".")
                    if parts[0] == "nachocausal":
                        assert parts[1:] == ["thresholds"], f"{src.name}: {alias.name}"
            elif isinstance(node, ast.ImportFrom) and node.module:
                parts = node.module.split(".")
                if parts[0] == "nachocausal":
                    imported = {a.name for a in node.names}
                    assert parts[1:] in ([], ["thresholds"]), f"{src.name}: {node.module}"
                    if parts[1:] == []:
                        assert imported <= {"thresholds"}, f"{src.name}: {imported}"


# --- exact reference miscoverage (§4.3) sanity ----------------------------------------

def test_exact_p0_values_are_in_the_predicted_regime() -> None:
    by_id = {c.cell_id: c for c in bench.CELLS}
    p0_cal = bench.exact_miscoverage_bernoulli(by_id["CELL-CAL"])
    assert 2e-4 < p0_cal < 3e-3          # ≈ 8.7e-4 predicted in the prereg
    p0_b1 = bench.exact_miscoverage_bernoulli(by_id["CELL-B1"])
    assert p0_b1 < 1e-6
    p0_eps = bench.exact_miscoverage_bernoulli(by_id["CELL-EPS"])
    assert p0_eps < 1e-3
    p0_b0 = bench.exact_miscoverage_bernoulli(by_id["CELL-B0"])
    assert p0_b0 < 1e-4


def test_exact_p0_detects_the_mutant_a_gap_at_cell_cal() -> None:
    """The calibration cell's whole point: the mutant-A radius multiplies p0 by ≫ 1."""
    by_id = {c.cell_id: c for c in bench.CELLS}
    cell = by_id["CELL-CAL"]
    p0 = bench.exact_miscoverage_bernoulli(cell)
    r_mut = bench._mutant_a_radius(cell.m, cell.alpha_j)
    threshold = cell.tv_true + 2.0 * r_mut
    pmf = bench._binomial_pmf(cell.m, 0.5)
    frac = np.arange(cell.m + 1, dtype=float) / cell.m
    mask = np.abs(frac[:, None] - frac[None, :]) > threshold
    p0_mut = float((pmf[:, None] * pmf[None, :])[mask].sum())
    band = bench.N_REP * p0 + max(5.0 * math.sqrt(bench.N_REP * p0 * (1 - p0)), 6.0)
    assert bench.N_REP * p0_mut > 2.0 * band   # detection margin ≫ 1


# --- Monte Carlo (gated: only after the prereg freeze commit) --------------------------

_MC_GATE = os.environ.get("OP21_PREREG_FROZEN") == "1"
_mc = pytest.mark.skipif(
    not _MC_GATE,
    reason="MC draws only after dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md is committed "
    "(set OP21_PREREG_FROZEN=1)",
)


@_mc
def test_mc_dev_smoke_bench_structure() -> None:
    """Reduced-n_rep dev smoke (uncitable): checks report structure and that the
    real-kernel pass is reproducible; does NOT assert mutant power (underpowered
    below the frozen N_REP) and is not a terminal run."""
    report = bench.run_bench(n_rep=1_000)
    assert report["terminal"] in bench.TERMINAL_PRECEDENCE
    frozen = report["frozen"]
    assert set(frozen["cells"]) == {c.cell_id for c in bench.CELLS}
    assert frozen["report_hash_run1"] == frozen["report_hash_run2"]
    assert frozen["criteria"]["c5_ok"]
    for cell in frozen["cells"].values():
        assert cell["miscoverage_count"] >= 0
        assert cell["max_tv_lower"] >= 0.0


@_mc
def test_mc_dev_smoke_null_cell_certifies_nothing_often() -> None:
    """CELL-B0 (TV=0): at dev n_rep the false-positive count must stay tiny."""
    report = bench.run_bench(n_rep=1_000)
    b0 = report["frozen"]["cells"]["CELL-B0"]
    assert b0["miscoverage_count"] <= b0["c1_limit"]
