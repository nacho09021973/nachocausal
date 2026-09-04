from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_SCRIPT = ROOT / ".claude" / "skills" / "auditor" / "audit.sh"
REGISTRY = ROOT / "provenance" / "committed_artifact_generators.tsv"
HEADER = "artifact_path\tgenerator_path\tcommand_or_template\tprovenance_anchor"
GENERATOR_PATHS = {
    "dev/measure_kbeam_peeloff.py",
    "dev/pr011_tv_certification_enumeration.py",
    "dev/present_anchor_sanity_pilot.py",
    "dev/run_new_geometry_future_observables.py",
}
HISTORICAL_ARTIFACTS = {
    "data/reports/kbeam_braiding_diagnostic_per_survivor.csv",
    "data/reports/pr004_braiding_v2_per_lineage.csv",
    "data/reports/pr005_k_stability_heldout_K2.csv",
    "data/reports/pr005_k_stability_heldout_K4.csv",
    "data/reports/pr005_k_stability_heldout_K8.csv",
    "data/reports/pr005_k_stability_heldout_K16.csv",
    "data/reports/pr005_k_stability_heldout_K32.csv",
    "data/reports/pr005_k_stability_heldout_K64.csv",
    "data/reports/pr005_population_depth_barrier_slices.csv",
    "data/reports/pr005_population_depth_barrier_slices_heldout.csv",
    "data/reports/pr011_tv_certification_n4.csv",
    "data/reports/pr011_tv_certification_n4.sha256",
    "data/reports/pr011_tv_certification_n5.csv",
    "data/reports/pr011_tv_certification_n5.sha256",
    "data/reports/pr011_tv_certification_n6.csv",
    "data/reports/pr011_tv_certification_n6.sha256",
    "data/reports/pr011_tv_certification_n7.csv",
    "data/reports/pr011_tv_certification_n7.sha256",
    "data/reports/pr011_tv_certification_n8.csv",
    "data/reports/pr011_tv_certification_n8.sha256",
    "data/reports/present_anchor_clean_v3_kill_test.csv",
    "data/reports/present_anchor_sanity_pilot.csv",
    "evidence/new_geometry_20260719/mink_control_metrics.csv",
}


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        text=True,
        capture_output=True,
    )


def _audit(repo: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["bash", str(AUDIT_SCRIPT), str(repo)],
        check=False,
        text=True,
        capture_output=True,
    )


def _registry_rows(path: Path) -> list[list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == HEADER
    return [line.split("\t") for line in lines[1:]]


def _init_fixture(tmp_path: Path, artifacts: set[str]) -> tuple[Path, str]:
    repo = tmp_path / "fixture"
    repo.mkdir()
    _git(repo, "init", "-b", "main")
    _git(repo, "config", "user.name", "Auditor Test")
    _git(repo, "config", "user.email", "auditor-test@example.invalid")
    for generator in GENERATOR_PATHS:
        path = repo / generator
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("print('fixture generator')\n", encoding="utf-8")
    test_path = repo / "tests" / "test_fixture.py"
    test_path.parent.mkdir(parents=True, exist_ok=True)
    test_path.write_text("def test_fixture():\n    assert True\n", encoding="utf-8")
    for artifact in artifacts:
        path = repo / artifact
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("value\n1\n", encoding="utf-8")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "fixture artifacts and generators")
    anchor = _git(repo, "rev-parse", "HEAD").stdout.strip()
    return repo, anchor


def _write_fixture_registry(
    repo: Path,
    anchor: str,
    artifacts: set[str],
    *,
    missing_generator_for: str | None = None,
    duplicate: str | None = None,
) -> None:
    rows = [HEADER]
    for artifact in sorted(artifacts):
        generator = (
            "dev/nonexistent_generator.py"
            if artifact == missing_generator_for
            else "dev/measure_kbeam_peeloff.py"
        )
        rows.append(f"{artifact}\t{generator}\tfixture command\tgit:{anchor}")
    if duplicate is not None:
        rows.append(
            f"{duplicate}\tdev/measure_kbeam_peeloff.py\tduplicate fixture command\tgit:{anchor}"
        )
    registry = repo / "provenance" / "committed_artifact_generators.tsv"
    registry.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text("\n".join(rows) + "\n", encoding="utf-8")
    _git(repo, "add", str(registry.relative_to(repo)))
    _git(repo, "commit", "-m", "fixture registry")


def test_historical_registry_covers_exactly_23_unique_artifacts() -> None:
    rows = _registry_rows(REGISTRY)
    assert len(rows) == 23
    assert all(len(row) == 4 and all(row) for row in rows)
    registered = [row[0] for row in rows]
    assert len(registered) == len(set(registered))
    assert set(registered) == HISTORICAL_ARTIFACTS


def test_historical_registry_generators_exist_and_are_tracked() -> None:
    rows = _registry_rows(REGISTRY)
    assert {row[1] for row in rows} == GENERATOR_PATHS
    for generator in GENERATOR_PATHS:
        assert (ROOT / generator).is_file()
        _git(ROOT, "ls-files", "--error-unmatch", "--", generator)


def test_fictitious_unregistered_csv_still_warns(tmp_path: Path) -> None:
    artifact = "data/reports/fictitious_orphan.csv"
    repo, _anchor = _init_fixture(tmp_path, {artifact})
    result = _audit(repo)
    assert result.returncode == 0
    assert f"WARN: committed data file with no generator reference: {artifact}" in result.stdout
    assert "Auditor: 0 error(s), 1 warning(s)" in result.stdout


def test_nonexistent_generator_is_an_error_not_a_pass(tmp_path: Path) -> None:
    artifact = "data/reports/registered_but_broken.csv"
    repo, anchor = _init_fixture(tmp_path, {artifact})
    _write_fixture_registry(repo, anchor, {artifact}, missing_generator_for=artifact)
    result = _audit(repo)
    assert result.returncode == 1
    assert f"ERROR: provenance inconsistency for {artifact}" in result.stdout
    assert "generator is missing or untracked" in result.stdout
    assert "Auditor: 1 error(s), 0 warning(s)" in result.stdout


def test_duplicate_registry_rows_are_an_error(tmp_path: Path) -> None:
    artifact = "data/reports/duplicated.csv"
    repo, anchor = _init_fixture(tmp_path, {artifact})
    _write_fixture_registry(repo, anchor, {artifact}, duplicate=artifact)
    result = _audit(repo)
    assert result.returncode == 1
    assert "expected exactly one registry row, found 2" in result.stdout


def test_removing_one_historical_registry_row_restores_warning(tmp_path: Path) -> None:
    omitted = "data/reports/pr005_k_stability_heldout_K32.csv"
    repo, anchor = _init_fixture(tmp_path, HISTORICAL_ARTIFACTS)
    _write_fixture_registry(repo, anchor, HISTORICAL_ARTIFACTS - {omitted})
    result = _audit(repo)
    assert result.returncode == 0
    assert f"WARN: committed data file with no generator reference: {omitted}" in result.stdout
    assert "Auditor: 0 error(s), 1 warning(s)" in result.stdout
