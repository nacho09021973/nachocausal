"""Deterministic implementation-fidelity tests for the truncated-futures localizer.

These tests use synthetic posets/coordinates only. They do not consume TRUNC_FUT_* seeds.
"""

from __future__ import annotations

import math
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

from dev import run_truncated_futures_localization as trunc


_ROOT = Path(__file__).resolve().parent.parent


def _past_matrix(edges: list[tuple[int, int]], n: int) -> np.ndarray:
    """Build C[a,b] true iff b precedes a from covering/transitive edges."""
    C = np.zeros((n, n), dtype=bool)
    for before, after in edges:
        C[after, before] = True
    changed = True
    while changed:
        before = C.copy()
        C = C | (C @ C)
        np.fill_diagonal(C, False)
        changed = not np.array_equal(before, C)
    return C.astype(bool)


def _selector_fixture() -> np.ndarray:
    # Minimals are 0..7. Futures are shaped so the T top band is {1,3}.
    edges = [
        (0, 8), (8, 9), (9, 10), (10, 11),
        (1, 12), (12, 13), (13, 14),
        (2, 15), (15, 16), (16, 17), (2, 18), (2, 19), (2, 20),
        (3, 21), (21, 22), (3, 23), (3, 24), (3, 25),
        (4, 26), (26, 27), (27, 28), (28, 29), (4, 30), (4, 31), (4, 32),
        (5, 33), (33, 34), (5, 35), (5, 36), (5, 37), (5, 38),
        (6, 39), (39, 40), (40, 41), (41, 42), (42, 43), (6, 44), (6, 45),
        (7, 46), (46, 47), (47, 48), (7, 49), (7, 50), (7, 51), (7, 52),
    ]
    return _past_matrix(edges, 53)


def test_L_V_midrank_and_T_formula_are_literal() -> None:
    C = _selector_fixture()
    minimals, scores = trunc.low_future_scores(C)
    assert minimals.tolist() == list(range(8))
    assert scores.L.tolist() == [4, 3, 3, 2, 4, 2, 5, 3]
    assert scores.V.tolist() == [4, 3, 6, 5, 7, 6, 7, 7]
    assert scores.rank_L.tolist() == pytest.approx([0.7857143, 0.4285714, 0.4285714, 0.0714286, 0.7857143, 0.0714286, 1.0, 0.4285714])
    assert scores.rank_V.tolist() == pytest.approx([0.1428571, 0.0, 0.5, 0.2857143, 0.8571429, 0.5, 0.8571429, 0.8571429])
    assert scores.T.tolist() == pytest.approx(1.0 - 0.5 * scores.rank_L - 0.5 * scores.rank_V)


def test_selection_and_component_controls_are_order_only() -> None:
    C = _selector_fixture()
    selections = trunc.select_truncated_and_controls(C, seed=123)
    assert selections["trunc"].selected.tolist() == [1, 3]
    assert selections["L"].selected.tolist() == [3, 5]
    assert selections["V"].selected.tolist() == [0, 1]
    assert selections["rand"].selected.size == selections["trunc"].selected.size
    assert set(selections["rand"].selected).issubset(set(range(8)))


def test_tie_boundary_over_cap_abstains() -> None:
    minimals = np.arange(8)
    scores = np.array([1.0, 0.9, 0.9, 0.9, 0.5, 0.4, 0.3, 0.2])
    sel = trunc.select_by_scores(minimals, scores, "synthetic")
    assert not sel.valid
    assert sel.abstention_reason == "TIE_OVER_CAP_ABSTAIN"


def test_random_control_salt_separates_stream_from_plain_seed() -> None:
    C = _selector_fixture()
    mins = trunc.minimal_elements(C)
    size = trunc.select_truncated_and_controls(C, seed=777)["trunc"].selected.size
    salted = trunc.select_truncated_and_controls(C, seed=777)["rand"].selected
    plain_rng_pick = np.sort(np.random.default_rng(777).choice(mins, size=size, replace=False))
    assert not np.array_equal(salted, plain_rng_pick)
    assert np.array_equal(salted, trunc.select_truncated_and_controls(C, seed=777)["rand"].selected)


def test_scoring_uses_coordinates_after_selection_for_loc_and_edge() -> None:
    C = _selector_fixture()
    selection = trunc.select_truncated_and_controls(C, seed=123)["trunc"]
    emb = np.zeros((C.shape[0], 2), dtype=float)
    emb[:, 0] = 1.2
    emb[:, 1] = 1.3
    emb[1] = [1.2, 0.7]
    emb[3] = [2.35, 0.5]
    scored = trunc.score_selection(emb, 9600.0, trunc.minimal_elements(C), selection)
    e = trunc.ell(9600.0)
    assert scored.loc_med == pytest.approx(np.median([0.0, 0.2 / e]))
    assert scored.loc_q75 == pytest.approx(np.percentile([0.0, 0.2 / e], 75))
    assert scored.edge_med == pytest.approx(np.median([0.05 / e, 0.6 / e]))
    assert math.isfinite(scored.edge_rank_med)


def test_sign_test_and_min_n_match_contract_examples() -> None:
    stat = trunc.exact_one_sided_sign_test([1.0] * 12 + [-1.0])
    assert stat["n"] == 13
    assert stat["k"] == 12
    assert stat["p"] == pytest.approx((math.comb(13, 12) + math.comb(13, 13)) / 2**13)
    assert trunc.min_n(0.01, 2, 26) == 13
    assert trunc.min_n(0.01, 1, 26) == 13


def test_synergy_terminal_precedence_failure_before_tie_dominated() -> None:
    rows = {}
    for seed in range(26):
        rows[seed] = {
            "trunc": trunc.ArmScoring("trunc", True, "", 2, 1.0, 1.0, 1.0, 0.5, 1.0),
            "L": trunc.ArmScoring("L", True, "", 2, 1.0, 1.0, 1.0, 0.5, 1.0),
            "V": trunc.ArmScoring("V", True, "", 2, 3.0, 1.0, 1.0, 0.5, 1.0),
        }
    terminal, details = trunc.synergy_terminal(rows)
    assert terminal == "NO_TRUNCATED_FUTURES_SYNERGY_DETECTED"
    assert details["contrasts"]["L"]["median_delta"] == 0.0


def test_boundary_confound_terminal_requires_near_wall_and_exclusion_loss() -> None:
    rows = {}
    for seed in range(26):
        rows[seed] = {
            "trunc": trunc.ArmScoring("trunc", True, "", 2, 1.0, 1.0, 1.0, 0.0, 3.0),
            "L": trunc.ArmScoring("L", True, "", 2, 3.0, 1.0, 1.0, 0.5, 3.0),
            "V": trunc.ArmScoring("V", True, "", 2, 3.0, 1.0, 1.0, 0.5, 3.0),
        }
    terminal, details = trunc.synergy_terminal(rows)
    assert terminal == "BOUNDARY_CONFOUND_DETECTED"
    assert details["edge"]["near_wall_significant"] is True
    assert details["edge"]["loss_after_exclusion"] is True


def test_cli_preflight_and_fidelity_run_no_seed_modes() -> None:
    script = _ROOT / "dev" / "run_truncated_futures_localization.py"
    preflight = subprocess.run(
        [sys.executable, str(script), "preflight"],
        cwd=_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert preflight.returncode == 0, preflight.stdout + preflight.stderr
    assert "PREFLIGHT_PASS_NO_SEEDS" in preflight.stdout
    fidelity = subprocess.run(
        [sys.executable, str(script), "fidelity"],
        cwd=_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert fidelity.returncode == 0, fidelity.stdout + fidelity.stderr
    assert "IMPLEMENTATION_FIDELITY_PASS" in fidelity.stdout
    blocked = subprocess.run(
        [sys.executable, str(script), "dev"],
        cwd=_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert blocked.returncode != 0
    assert "not authorized" in blocked.stderr
