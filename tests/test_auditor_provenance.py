from __future__ import annotations

import subprocess
from pathlib import Path

import pytest


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
# Listing these basenames here is deliberate. Auditor report 040 recorded that this
# very list silenced all 23 provenance warnings, because audit.sh ran a literal
# `git grep` over '*.py' before ever consulting the registry. The fix makes the
# registry authoritative and bars test paths from satisfying the literal fallback,
# so this list must now be harmless. It stays as a permanent regression trap.
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
BOGUS_ANCHOR = "git:" + "0" * 40
FALLBACK_DENIED_CANDIDATE_PATHS = (
    "tests/test_name.py",
    "pkg/tests/helper.py",
    "test/test_name.py",
    "pkg/test/helper.py",
    "mytests/test_name.py",
    "pkg/mytests/helper.py",
    "conftest.py",
    "dev/conftest.py",
    "dev/test_name.py",
    "foo_test.py",
    "foo_test.ipynb",
    "foo_test.sh",
    "docs/generator.py",
    "pkg/docs/generator.py",
    "provenance/generator.py",
    "pkg/provenance/generator.py",
    ".claude/generator.py",
    "pkg/.claude/generator.py",
)


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


def _write(repo: Path, relpath: str, text: str) -> None:
    path = repo / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _mentions(paths: set[str]) -> str:
    """Source text that names each artifact basename verbatim."""
    return "\n".join(f'NAMES = "{Path(p).name}"' for p in sorted(paths)) + "\n"


def _init_fixture(
    tmp_path: Path,
    artifacts: set[str],
    *,
    mention_in_tests: set[str] | None = None,
    mention_in_generator: set[str] | None = None,
    mention_in_docs: set[str] | None = None,
) -> tuple[Path, str]:
    """A throwaway repo. `mention_in_tests` reproduces the Auditor 040 trap."""
    repo = tmp_path / "fixture"
    repo.mkdir()
    _git(repo, "init", "-b", "main")
    _git(repo, "config", "user.name", "Auditor Test")
    _git(repo, "config", "user.email", "auditor-test@example.invalid")
    for generator in GENERATOR_PATHS:
        _write(repo, generator, "print('fixture generator')\n")
    _write(repo, "tests/test_fixture.py", "def test_fixture():\n    assert True\n")
    if mention_in_tests:
        _write(repo, "tests/test_names.py", _mentions(mention_in_tests))
    if mention_in_generator:
        _write(repo, "dev/legit_generator.py", _mentions(mention_in_generator))
    if mention_in_docs:
        _write(repo, "docs/notes.py", _mentions(mention_in_docs))
    for artifact in artifacts:
        _write(repo, artifact, "value\n1\n")
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
    anchor_override: dict[str, str] | None = None,
    malformed_for: str | None = None,
) -> None:
    rows = [HEADER]
    overrides = anchor_override or {}
    for artifact in sorted(artifacts):
        if artifact == malformed_for:
            rows.append(f"{artifact}\tdev/measure_kbeam_peeloff.py\t\tgit:{anchor}")
            continue
        generator = (
            "dev/nonexistent_generator.py"
            if artifact == missing_generator_for
            else "dev/measure_kbeam_peeloff.py"
        )
        row_anchor = overrides.get(artifact, f"git:{anchor}")
        rows.append(f"{artifact}\t{generator}\tfixture command\t{row_anchor}")
    if duplicate is not None:
        rows.append(
            f"{duplicate}\tdev/measure_kbeam_peeloff.py\tduplicate fixture command\tgit:{anchor}"
        )
    registry = repo / "provenance" / "committed_artifact_generators.tsv"
    registry.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text("\n".join(rows) + "\n", encoding="utf-8")
    _git(repo, "add", str(registry.relative_to(repo)))
    _git(repo, "commit", "-m", "fixture registry")


# --- the real registry, as content -------------------------------------------------


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


# --- reachability: the Auditor 040 defect ------------------------------------------


def test_registry_is_the_only_thing_that_clears_the_historical_artifacts() -> None:
    """Reachability on the real repository.

    Auditor 040 measured 0 of 57 scanned artifacts reaching the registry: every
    historical basename was matched by the literal `git grep` inside this very
    test file first. This asserts the structural property that makes the live
    0/0 earned -- every code-type reference to these 23 basenames lives in a path
    barred from the literal fallback, so the registry is the only thing that can
    clear them.
    """
    barred_prefixes = ("tests/", "docs/", ".claude/", "provenance/")
    for artifact, *_rest in _registry_rows(REGISTRY):
        base = Path(artifact).name
        refs = subprocess.run(
            [
                "git", "-C", str(ROOT), "grep", "-l", "--", base, "--",
                "*.py", "*.sh", "*.js", "*.ts", "*.ipynb", "*.go", "*.rs", "Makefile",
            ],
            check=False,
            text=True,
            capture_output=True,
        ).stdout.split()
        assert refs, f"expected at least this test file to name {base}"
        for ref in refs:
            assert ref.startswith(barred_prefixes) or Path(ref).name.startswith("test_"), (
                f"{base} is referenced from generator-candidate code at {ref}; "
                "the registry would no longer be the reason it passes the audit"
            )
    result = _audit(ROOT)
    assert result.returncode == 0
    assert "Auditor: 0 error(s), 0 warning(s)" in result.stdout


def test_provenance_confirmed_is_distinct_from_reproduction_command_documented() -> None:
    """W-4: an undocumented historical command is not silently upgraded.

    Provenance (generator + validated commit anchor) is confirmed for all 23.
    An exact re-runnable command is a strictly stronger property that two rows
    do not have, and no command was invented to manufacture it.
    """
    rows = _registry_rows(REGISTRY)
    provenance_confirmed = [r for r in rows if r[1] and r[3].startswith("git:")]
    assert len(provenance_confirmed) == len(rows) == 23

    undocumented = {r[0] for r in rows if r[2].startswith("NOT_DOCUMENTED")}
    assert undocumented == {
        "data/reports/kbeam_braiding_diagnostic_per_survivor.csv",
        "evidence/new_geometry_20260719/mink_control_metrics.csv",
    }
    documented = [r for r in rows if not r[2].startswith("NOT_DOCUMENTED")]
    assert len(documented) == 21
    # Every documented command actually invokes its own registered generator.
    for artifact, generator, command, _anchor in documented:
        assert Path(generator).name in command, (artifact, generator, command)

def test_bogus_anchor_errors_even_though_basename_is_in_tests(tmp_path: Path) -> None:
    artifact = "data/reports/spoofed_by_tests.csv"
    repo, anchor = _init_fixture(tmp_path, {artifact}, mention_in_tests={artifact})
    _write_fixture_registry(
        repo, anchor, {artifact}, anchor_override={artifact: BOGUS_ANCHOR}
    )
    result = _audit(repo)
    assert result.returncode == 1
    assert "invalid git commit anchor" in result.stdout
    assert "Auditor: 1 error(s), 0 warning(s)" in result.stdout


@pytest.mark.parametrize("candidate_path", FALLBACK_DENIED_CANDIDATE_PATHS)
def test_test_infrastructure_denylist_cannot_satisfy_fallback(
    tmp_path: Path, candidate_path: str
) -> None:
    """Pin every directory and basename exclusion by executing the real auditor."""
    artifact = "data/reports/only_named_in_denied_candidate.csv"
    repo, _anchor = _init_fixture(tmp_path, {artifact})
    _write(repo, candidate_path, _mentions({artifact}))
    _git(repo, "add", candidate_path)
    _git(repo, "commit", "-m", f"sole basename reference in {candidate_path}")
    result = _audit(repo)
    assert result.returncode == 0
    assert f"WARN: committed data file with no generator reference: {artifact}" in result.stdout
    assert "Auditor: 0 error(s), 1 warning(s)" in result.stdout


@pytest.mark.parametrize("candidate_path", ("dev/real_generator.py", "scripts/real_generator.py"))
def test_legitimate_generator_reference_still_passes(
    tmp_path: Path, candidate_path: str
) -> None:
    """The historical literal fallback survives for real generator code."""
    artifact = "data/reports/named_in_real_generator.csv"
    repo, _anchor = _init_fixture(tmp_path, {artifact})
    _write(repo, candidate_path, _mentions({artifact}))
    _git(repo, "add", candidate_path)
    _git(repo, "commit", "-m", f"sole basename reference in {candidate_path}")
    result = _audit(repo)
    assert result.returncode == 0
    assert artifact not in result.stdout
    assert "Auditor: 0 error(s), 0 warning(s)" in result.stdout


# --- registry validation failure modes ----------------------------------------------


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


def test_malformed_row_with_empty_field_is_an_error(tmp_path: Path) -> None:
    artifact = "data/reports/malformed_row.csv"
    repo, anchor = _init_fixture(tmp_path, {artifact})
    _write_fixture_registry(repo, anchor, {artifact}, malformed_for=artifact)
    result = _audit(repo)
    assert result.returncode == 1
    assert "must contain four non-empty tab-separated fields" in result.stdout


def test_unsupported_anchor_scheme_is_an_error(tmp_path: Path) -> None:
    artifact = "data/reports/unsupported_anchor.csv"
    repo, anchor = _init_fixture(tmp_path, {artifact})
    _write_fixture_registry(
        repo, anchor, {artifact}, anchor_override={artifact: "svn:12345"}
    )
    result = _audit(repo)
    assert result.returncode == 1
    assert "unsupported provenance anchor: svn:12345" in result.stdout


def test_anchor_commit_that_does_not_touch_the_artifact_is_an_error(tmp_path: Path) -> None:
    artifact = "data/reports/anchor_elsewhere.csv"
    repo, _anchor = _init_fixture(tmp_path, {artifact})
    # A real, later commit that touches something else entirely.
    _write(repo, "dev/unrelated_change.py", "print('unrelated')\n")
    _git(repo, "add", "dev/unrelated_change.py")
    _git(repo, "commit", "-m", "unrelated commit")
    unrelated = _git(repo, "rev-parse", "HEAD").stdout.strip()
    _write_fixture_registry(
        repo, unrelated, {artifact}, anchor_override={artifact: f"git:{unrelated}"}
    )
    result = _audit(repo)
    assert result.returncode == 1
    assert "anchor commit does not introduce or modify the artifact" in result.stdout
    assert "Auditor: 1 error(s), 0 warning(s)" in result.stdout


def test_removing_one_historical_registry_row_restores_warning(tmp_path: Path) -> None:
    omitted = "data/reports/pr005_k_stability_heldout_K32.csv"
    repo, anchor = _init_fixture(
        tmp_path, HISTORICAL_ARTIFACTS, mention_in_tests=HISTORICAL_ARTIFACTS
    )
    _write_fixture_registry(repo, anchor, HISTORICAL_ARTIFACTS - {omitted})
    result = _audit(repo)
    assert result.returncode == 0
    assert f"WARN: committed data file with no generator reference: {omitted}" in result.stdout
    assert "Auditor: 0 error(s), 1 warning(s)" in result.stdout
