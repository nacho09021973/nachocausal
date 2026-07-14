"""Tests for PR011 TV certification (enumeration + Hellinger fallback)."""

from __future__ import annotations

import hashlib
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
    assert enum.HELLINGER_M == 100


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


def test_hellinger_stability_and_upper_bound() -> None:
    h2, h2_x = enum.verify_hellinger_stability(enum.TAU_PAIR[0], enum.TAU_PAIR[1])
    assert h2 > 0.0 and h2_x > 0.0
    eps, _ = enum.poset_tv_upper_via_hellinger(enum.TAU_PAIR[0], enum.TAU_PAIR[1], 4)
    assert 0.0 < eps < 1.0


def test_certify_n4_via_hellinger_fallback(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(enum, "PRIMARY_CERTIFY_PROBE", ())
    result = enum.certify(4, enum.TAU_PAIR[0], enum.TAU_PAIR[1])
    assert result.method == "HELLINGER_FALLBACK"
    assert result.terminal == enum.TERMINAL_DISTINGUISHABLE
    assert 0.0 < result.epsilon_certified_upper < 1.0
    assert result.primary_tv_nominal is not None
    assert result.primary_tv_nominal < result.epsilon_certified_upper


def test_publish_certification_roundtrip(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(enum, "PRIMARY_CERTIFY_PROBE", ())
    report_dir = tmp_path / "data" / "reports"
    report_dir.mkdir(parents=True)
    monkeypatch.setattr(enum, "REPORT_DIR", report_dir)

    result = enum.certify(4)
    csv_path, sidecar_path = enum.certification_artifact_paths(4)
    enum.publish_certification(result)
    csv_data = csv_path.read_bytes()
    digest = hashlib.sha256(csv_data).hexdigest()
    assert sidecar_path.read_text() == f"{digest}  {csv_path.name}\n"
    with pytest.raises(RuntimeError, match="refusing to overwrite"):
        enum.publish_certification(result)


def test_falsifier_cli_writes_no_report_artifacts(tmp_path: Path) -> None:
    reports = tmp_path / "data" / "reports"
    reports.mkdir(parents=True)
    before = set(reports.glob("pr011_*"))
    proc = subprocess.run(
        [
            sys.executable,
            str(_ROOT / "dev" / "pr011_tv_certification_enumeration.py"),
            "falsifier",
            "--grid-m",
            "12",
        ],
        cwd=_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "PR011_ENUM_FALSIFIER=OK" in proc.stdout
    assert set(reports.glob("pr011_*")) == before


def test_certify_dry_run_via_main(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(enum, "PRIMARY_CERTIFY_PROBE", ())
    assert enum.main(["certify", "--dry-run"]) == 0


def test_certify_n5_via_hellinger_fallback(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(enum, "PRIMARY_CERTIFY_PROBE", ())
    result = enum.certify(5, enum.TAU_PAIR[0], enum.TAU_PAIR[1])
    assert result.method == "HELLINGER_FALLBACK"
    assert result.n == 5
    assert result.terminal == enum.TERMINAL_DISTINGUISHABLE
    assert 0.0 < result.epsilon_certified_upper < 1.0


COMMITTED_CERT_SHA256_N4 = (
    "5b53df73cdb02cba1198e02fb332d69d0ca3377a033cb767075d7855b6a475a0"
)
COMMITTED_CERT_SHA256_N5 = (
    "092b3d42011cb4221f6c18648debe5e5023d5ba5836896b6da55c6accdda473f"
)


@pytest.mark.parametrize(
    ("n", "sha256"),
    [
        (4, COMMITTED_CERT_SHA256_N4),
        (5, COMMITTED_CERT_SHA256_N5),
    ],
)
def test_committed_certification_artifact_matches_terminal(n: int, sha256: str) -> None:
    csv_path, sidecar_path = enum.certification_artifact_paths(n)
    csv_data = csv_path.read_bytes()
    assert hashlib.sha256(csv_data).hexdigest() == sha256
    assert sidecar_path.read_text() == f"{sha256}  {csv_path.name}\n"
    lines = csv_data.decode().splitlines()
    assert lines[0] == ",".join(enum.CERT_CSV_FIELDS)
    row = dict(zip(enum.CERT_CSV_FIELDS, lines[1].split(",")))
    assert row["method"] == "HELLINGER_FALLBACK"
    assert row["n"] == str(n)
    assert row["terminal"] == enum.TERMINAL_DISTINGUISHABLE
    assert float(row["epsilon_certified_upper"]) < 1.0