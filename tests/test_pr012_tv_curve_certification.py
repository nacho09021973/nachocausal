"""Tests for PR012 (draft) — certified TV vs Δτ curve, tensorized Hellinger bound."""

from __future__ import annotations

import hashlib
import math
import subprocess
import sys
from pathlib import Path

import pytest

from dev import pr011_tv_certification_enumeration as pr011
from dev import pr012_tv_curve_certification as pr012


_ROOT = Path(__file__).resolve().parent.parent


def test_frozen_geometry_reused_from_pr011_not_redefined() -> None:
    assert pr012.TAU_FAMILY == pr011.TAU_FAMILY == (0.8, 1.2)
    assert pr012.R_P == pr011.R_P and pr012.R_Q == pr011.R_Q
    assert pr012.V_P == pr011.V_P and pr012.V_Q == pr011.V_Q


def test_terminal_vocabulary_reused_from_pr011_not_reimplemented() -> None:
    # PR012 must call PR011's already-fixed terminal_for_epsilon (auditor_report_011), not a
    # second copy that could silently reintroduce the dead-branch bug.
    assert pr012.terminal_for_epsilon is pr011.terminal_for_epsilon


def test_delta_tau_ladder_is_frozen_symmetric_fractions_of_family_span() -> None:
    assert pr012.DELTA_TAU_LADDER == (0.0125, 0.025, 0.05, 0.1, 0.2, 0.4)
    assert 0.1 in pr012.DELTA_TAU_LADDER  # PR011's own certified pair, kept as a cross-check
    for dt in pr012.DELTA_TAU_LADDER:
        tau_a = pr012.TAU_CENTER - dt / 2
        tau_b = pr012.TAU_CENTER + dt / 2
        assert pr012.TAU_FAMILY[0] <= tau_a <= tau_b <= pr012.TAU_FAMILY[1]


def test_bhattacharyya_tv_upper_range_validation() -> None:
    with pytest.raises(ValueError):
        pr012.bhattacharyya_tv_upper(-0.1, 4)
    with pytest.raises(ValueError):
        pr012.bhattacharyya_tv_upper(2.1, 4)
    assert pr012.bhattacharyya_tv_upper(0.0, 8) == 0.0


def test_tensorized_bound_is_root_n_tighter_than_naive_for_small_h2() -> None:
    # Exact analytic fact for H^2 << 1: TV_tensorized/TV_naive -> 1/sqrt(n). Verified against the
    # actual frozen PR011 H^2 for the certification pair.
    h2, _ = pr011.verify_hellinger_stability(*pr011.TAU_PAIR)
    for n in (4, 5, 6, 7, 8):
        tensorized = pr012.bhattacharyya_tv_upper(h2, n)
        naive = pr012.naive_linear_tv_upper(h2, n)
        assert tensorized < naive
        assert tensorized / naive == pytest.approx(1.0 / math.sqrt(n), rel=1e-3)


def test_naive_bound_at_delta_0p1_n8_matches_pr011_published_epsilon() -> None:
    # Cross-check against the already-audited, already-published PR011 n=8 artifact.
    h2, _ = pr011.verify_hellinger_stability(*pr011.TAU_PAIR)
    naive = pr011.certified_tv_upper(pr012.naive_linear_tv_upper(h2, 8))
    assert naive == pytest.approx(0.009223798457, abs=1e-9)


def test_n_for_target_tv_inverts_bhattacharyya_tv_upper() -> None:
    h2, _ = pr011.verify_hellinger_stability(*pr011.TAU_PAIR)
    for target in (0.5, 0.9, 0.99):
        n = pr012.n_for_target_tv(h2, target)
        assert pr012.bhattacharyya_tv_upper(h2, n) == pytest.approx(target, rel=1e-6)
    with pytest.raises(ValueError):
        pr012.n_for_target_tv(h2, 0.0)
    with pytest.raises(ValueError):
        pr012.n_for_target_tv(h2, 1.0)


def test_assert_not_scale_related_rejects_degenerate_pair() -> None:
    with pytest.raises(ValueError):
        pr012.assert_not_scale_related(1.0, 1.0)
    pr012.assert_not_scale_related(0.95, 1.05)  # does not raise


def test_delta_tau_floor_enforced() -> None:
    with pytest.raises(ValueError, match="below the frozen numerical floor"):
        pr012.certify_curve_point(pr012.DELTA_TAU_FLOOR / 10)


def test_certify_curve_point_outside_family_range_rejected() -> None:
    with pytest.raises(ValueError, match="outside frozen family"):
        pr012.certify_curve_point(1.0)  # would need tau outside [0.8, 1.2]


def test_certify_curve_point_at_delta_0p1_matches_naive_cross_check() -> None:
    point = pr012.certify_curve_point(0.1, n=8)
    assert point.terminal == pr011.TERMINAL_DISTINGUISHABLE
    assert point.epsilon_naive_linear_for_comparison == pytest.approx(0.009223798457, abs=1e-9)
    assert point.epsilon_certified_upper < point.epsilon_naive_linear_for_comparison
    assert point.minimax_error_floor == pytest.approx(
        (1.0 - point.epsilon_certified_upper) / 2.0
    )


def test_certify_curve_reports_grid_resolution_abstain_for_smallest_points() -> None:
    points = pr012.certify_curve()
    by_delta = {p.delta_tau: p for p in points}
    assert by_delta[0.0125].terminal == pr012.TERMINAL_GRID_ABSTAIN
    assert by_delta[0.0125].epsilon_certified_upper is None
    assert by_delta[0.025].terminal == pr012.TERMINAL_GRID_ABSTAIN
    # Larger, better-resolved points must still certify normally.
    assert by_delta[0.1].terminal == pr011.TERMINAL_DISTINGUISHABLE
    assert by_delta[0.1].epsilon_certified_upper is not None


def test_render_curve_csv_handles_abstain_rows() -> None:
    points = pr012.certify_curve(delta_tau_ladder=(0.0125, 0.1))
    csv_bytes = pr012.render_curve_csv(points)
    text = csv_bytes.decode()
    lines = text.splitlines()
    assert lines[0] == ",".join(pr012.CURVE_CSV_FIELDS)
    assert "GRID_RESOLUTION_ABSTAIN" in lines[1]
    assert "None" in lines[1]
    assert pr011.TERMINAL_DISTINGUISHABLE in lines[2]


def test_publish_curve_roundtrip_and_refuses_overwrite(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    report_dir = tmp_path / "data" / "reports"
    report_dir.mkdir(parents=True)
    monkeypatch.setattr(pr012, "REPORT_DIR", report_dir)
    monkeypatch.setattr(pr012, "CURVE_CSV_PATH", report_dir / "pr012_tv_curve_n8.csv")
    monkeypatch.setattr(pr012, "CURVE_SHA256_PATH", report_dir / "pr012_tv_curve_n8.sha256")

    points = pr012.certify_curve(delta_tau_ladder=(0.1,))
    pr012.publish_curve(points)
    csv_data = pr012.CURVE_CSV_PATH.read_bytes()
    digest = hashlib.sha256(csv_data).hexdigest()
    assert pr012.CURVE_SHA256_PATH.read_text() == f"{digest}  {pr012.CURVE_CSV_PATH.name}\n"
    with pytest.raises(RuntimeError, match="refusing to overwrite"):
        pr012.publish_curve(points)


def test_sanity_cli_passes() -> None:
    proc = subprocess.run(
        [sys.executable, str(_ROOT / "dev" / "pr012_tv_curve_certification.py"), "sanity"],
        cwd=_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "PR012_SANITY=PASS" in proc.stdout


def test_curve_dry_run_cli_writes_no_artifacts(tmp_path: Path) -> None:
    reports = tmp_path / "data" / "reports"
    reports.mkdir(parents=True)
    before = set(reports.glob("pr012_*"))
    proc = subprocess.run(
        [
            sys.executable,
            str(_ROOT / "dev" / "pr012_tv_curve_certification.py"),
            "curve",
            "--dry-run",
        ],
        cwd=_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "PR012_CURVE=OK" in proc.stdout
    assert "GRID_RESOLUTION_ABSTAIN" in proc.stdout
    assert set(reports.glob("pr012_*")) == before
