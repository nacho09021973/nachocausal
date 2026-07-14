"""Tests for PR011 TV enumeration scaffold (no viability terminal, no reports)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from dev import pr011_tv_certification_enumeration as enum


_ROOT = Path(__file__).resolve().parent.parent


def test_frozen_geometry_matches_pr011_anchor() -> None:
    assert enum.R_P == 2.0 and enum.V_P == 0.0
    assert enum.R_Q == 0.5 and enum.V_Q == 1.0
    assert enum.TAU_PAIR == (0.95, 1.05)
    assert enum.N_LADDER == (4, 5, 6, 7, 8)


def test_poset_law_renormalizes_to_unit_mass_at_n4_grid12() -> None:
    fam, copula = enum.build_diamond_family(enum.TAU_PAIR[0])
    grid = enum.copula_grid(copula, fam, 12)
    raw_law = enum.poset_law_from_grid(grid, 4)
    law, raw_sum = enum.normalize_law(raw_law)
    assert raw_sum >= enum.RAW_MASS_SUM_MIN
    assert sum(law.values()) == pytest.approx(1.0)


def test_enumeration_is_reproducible_at_n4() -> None:
    first = enum.enumerate_tv(4, enum.TAU_PAIR[0], enum.TAU_PAIR[1], grid_m=12)
    second = enum.enumerate_tv(4, enum.TAU_PAIR[0], enum.TAU_PAIR[1], grid_m=12)
    assert first.tv == second.tv
    assert first.mass_sum_a == second.mass_sum_a


def test_falsifier_finds_positive_tv_at_certification_pair() -> None:
    result = enum.run_falsifier(grid_m=12)
    assert result.tv > 0.0
    assert result.tv_certified_upper > 0.0
    assert enum.falsifier_verdict(result) == "PAIR_DISTINGUISHABLE_TV_POSITIVE"


def test_certified_tv_upper_rounds_up() -> None:
    assert enum.certified_tv_upper(0.0) == 0.0
    assert enum.certified_tv_upper(1e-13) == 1e-12
    noisy = 0.0007022 + 5e-16
    assert enum.certified_tv_upper(noisy) >= noisy


def test_falsifier_cli_writes_no_report_artifacts(tmp_path: Path) -> None:
    reports = tmp_path / "data" / "reports"
    reports.mkdir(parents=True)
    before = set(reports.glob("pr011_*"))
    proc = subprocess.run(
        [sys.executable, str(_ROOT / "dev" / "pr011_tv_certification_enumeration.py"), "falsifier", "--grid-m", "12"],
        cwd=_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "PR011_ENUM_FALSIFIER=OK" in proc.stdout
    assert "falsifier_verdict=PAIR_DISTINGUISHABLE_TV_POSITIVE" in proc.stdout
    assert set(reports.glob("pr011_*")) == before