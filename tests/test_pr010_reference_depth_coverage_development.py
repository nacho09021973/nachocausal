from __future__ import annotations

import ast
import hashlib
import inspect
import os
from pathlib import Path
import subprocess

import numpy as np
import pytest

from dev import evaluate_pr010_reference_depth_coverage_development as evaluator
from dev import run_pr010_reference_depth_coverage_development as runner


NORMATIVE_SHA = "489f560f2cbe0cc92671b06574dc48b04d432968"
COMMITTED_CSV_SHA256 = (
    "58037a1b1ef9dcbf63901fb85e8ee7f2095270f432bff7f37176479d716bb58f"
)


def synthetic_rows(
    support_by_cell: dict[tuple[str, int], int] | None = None,
) -> list[dict[str, int | str]]:
    support_by_cell = support_by_cell or {
        (kind, depth): 24
        for kind in evaluator.SPACETIME_KINDS
        for depth in evaluator.TRANSITION_DEPTHS
    }
    rows = []
    for seed_index, seed in enumerate(evaluator.DEVELOPMENT_SEEDS):
        for kind in evaluator.SPACETIME_KINDS:
            for depth in evaluator.TRANSITION_DEPTHS:
                supported = int(seed_index < support_by_cell[(kind, depth)])
                evaluable = 5 if supported else 4
                rows.append(
                    {
                        "seed": seed,
                        "spacetime_kind": kind,
                        "depth_k": depth,
                        "n_emitted_starts": 5,
                        "n_transition_evaluable_starts": evaluable,
                        "seed_depth_supported": supported,
                    }
                )
    return rows


def render_synthetic(rows: list[dict[str, int | str]]) -> bytes:
    lines = [",".join(evaluator.CSV_FIELDS)]
    lines.extend(
        ",".join(str(row[field]) for field in evaluator.CSV_FIELDS) for row in rows
    )
    return ("\n".join(lines) + "\n").encode()


def patch_paths(monkeypatch: pytest.MonkeyPatch, module: object, root: Path) -> None:
    report_dir = root / "data" / "reports"
    report_dir.mkdir(parents=True)
    monkeypatch.setattr(module, "REPORT_DIR", report_dir)
    monkeypatch.setattr(module, "CSV_PATH", report_dir / "pr010_reference_depth_coverage_development.csv")
    monkeypatch.setattr(module, "SIDECAR_PATH", report_dir / "pr010_reference_depth_coverage_development.sha256")
    monkeypatch.setattr(module, "CSV_TMP_PATH", report_dir / "pr010_reference_depth_coverage_development.csv.tmp")
    monkeypatch.setattr(module, "SIDECAR_TMP_PATH", report_dir / "pr010_reference_depth_coverage_development.sha256.tmp")


def write_artifact_pair(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    rows: list[dict[str, int | str]],
) -> tuple[bytes, bytes]:
    patch_paths(monkeypatch, evaluator, tmp_path)
    csv_data = render_synthetic(rows)
    sidecar = (
        f"{hashlib.sha256(csv_data).hexdigest()}  {evaluator.CSV_PATH.name}\n".encode()
    )
    evaluator.CSV_PATH.write_bytes(csv_data)
    evaluator.SIDECAR_PATH.write_bytes(sidecar)
    return csv_data, sidecar


def _function_node(source: str, name: str, class_name: str | None = None) -> ast.AST:
    tree = ast.parse(source)
    body = tree.body
    if class_name is not None:
        cls = next(node for node in body if isinstance(node, ast.ClassDef) and node.name == class_name)
        body = cls.body
    return next(node for node in body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name)


@pytest.mark.parametrize(
    ("name", "class_name", "source_path"),
    [
        ("make_exchangeable_tie_ranks", None, "dev/run_pr009_effective_expansion.py"),
        ("sample_starts_exchangeably", None, "dev/run_pr009_effective_expansion.py"),
        ("kbeam_exchangeable", None, "dev/run_pr009_effective_expansion.py"),
        ("ensemble_width", "EnclosingDiamondWorkspace", "dev/pr009_effective_expansion_core.py"),
    ],
)
def test_normative_definitions_are_literal_ast_copies(name, class_name, source_path):
    committed = subprocess.run(
        ["git", "show", f"{NORMATIVE_SHA}:{source_path}"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    implemented = Path(inspect.getsourcefile(runner) or "").read_text()
    expected = _function_node(committed, name, class_name)
    actual = _function_node(implemented, name, class_name)
    assert ast.dump(actual, include_attributes=False) == ast.dump(
        expected, include_attributes=False
    )


def test_committed_development_artifact_evaluates_to_infeasible_terminal() -> None:
    root = Path(__file__).resolve().parent.parent
    csv_path = root / "data" / "reports" / "pr010_reference_depth_coverage_development.csv"
    sidecar_path = (
        root / "data" / "reports" / "pr010_reference_depth_coverage_development.sha256"
    )
    csv_data = csv_path.read_bytes()
    assert hashlib.sha256(csv_data).hexdigest() == COMMITTED_CSV_SHA256
    expected_sidecar = (
        f"{COMMITTED_CSV_SHA256}  {csv_path.name}\n".encode("ascii")
    )
    assert sidecar_path.read_bytes() == expected_sidecar
    rows = evaluator.validate_csv_bytes(csv_data)
    assert evaluator.evaluate_rows(rows) == evaluator.INFEASIBLE_TERMINAL


def test_frozen_constants_and_schema_are_exact():
    assert runner.DEVELOPMENT_SEEDS == tuple(range(1_101_000, 1_101_024))
    assert runner.SPACETIME_KINDS == ("BH", "MINK")
    assert runner.INTENSITY == 4_800
    assert runner.T_EDGE == 6.0
    assert runner.M == 3
    assert runner.K == 64
    assert runner.MAX_STARTS == 40
    assert runner.TIE_RANK_MASTER_SEED == 9_009_009
    assert runner.REQUIRED_SLICES == (3, 4, 5, 6)
    assert runner.TRANSITION_DEPTHS == (3, 4, 5)
    assert runner.CSV_FIELDS == evaluator.CSV_FIELDS
    runner._validate_frozen_configuration()


def test_computational_thread_backends_are_fixed_below_process_cap():
    for name in (
        "OPENBLAS_NUM_THREADS",
        "OMP_NUM_THREADS",
        "MKL_NUM_THREADS",
        "NUMEXPR_NUM_THREADS",
        "VECLIB_MAXIMUM_THREADS",
        "BLIS_NUM_THREADS",
    ):
        assert os.environ[name] == "1"


def test_exchangeable_ranks_are_deterministic_and_seeded():
    first = runner.make_exchangeable_tie_ranks(100, 42)
    repeat = runner.make_exchangeable_tie_ranks(100, 42)
    other = runner.make_exchangeable_tie_ranks(100, 43)
    assert np.array_equal(first, repeat)
    assert not np.array_equal(first, other)
    assert np.array_equal(np.sort(first), np.arange(100))


@pytest.mark.parametrize(
    ("name", "value"),
    [("T_EDGE", 6.1), ("TIE_RANK_MASTER_SEED", 9_009_010)],
)
def test_geometry_and_tie_seed_internal_drift_is_refused(name, value, monkeypatch):
    monkeypatch.setattr(runner, name, value)
    with pytest.raises(runner.DataContractError, match="configuration drift"):
        runner._validate_frozen_configuration()


def test_full_traversal_is_fixed_and_has_no_coverage_early_stop(monkeypatch):
    visited = []

    def fake_seed_rows(seed):
        visited.append(seed)
        return [
            {
                "seed": seed,
                "spacetime_kind": kind,
                "depth_k": depth,
                "n_emitted_starts": 5,
                "n_transition_evaluable_starts": 5,
                "seed_depth_supported": 1,
            }
            for kind in runner.SPACETIME_KINDS
            for depth in runner.TRANSITION_DEPTHS
        ]

    monkeypatch.setattr(runner, "_coverage_rows_for_seed", fake_seed_rows)
    rows = runner.build_coverage_rows()
    assert visited == list(runner.DEVELOPMENT_SEEDS)
    assert len(rows) == 144


def test_seed_outside_development_is_refused_before_sprinkling(monkeypatch):
    called = False

    def forbidden(*_args):
        nonlocal called
        called = True

    monkeypatch.setattr(runner.generator, "numpy_sprinkle", forbidden)
    with pytest.raises(runner.DataContractError):
        runner._coverage_rows_for_seed(1_101_024)
    assert not called


def test_exact_144_row_serialization_and_roundtrip():
    rows = synthetic_rows()
    data = runner.render_csv(rows)
    assert len(data.splitlines()) == 145
    assert data.splitlines()[0].decode() == ",".join(runner.CSV_FIELDS)
    assert data.endswith(b"\n") and b"\r" not in data
    assert runner.validate_csv_bytes(data) == rows
    assert evaluator.validate_csv_bytes(data) == rows


@pytest.mark.parametrize("evaluable,supported", [(4, 0), (5, 1)])
def test_support_predicate_boundary(evaluable, supported):
    rows = synthetic_rows()
    rows[0]["n_transition_evaluable_starts"] = evaluable
    rows[0]["seed_depth_supported"] = supported
    data = render_synthetic(rows)
    assert evaluator.validate_csv_bytes(data)[0]["seed_depth_supported"] == supported


@pytest.mark.parametrize("mutation", ["missing", "duplicate", "extra", "order"])
def test_row_count_key_set_and_order_fail_closed(mutation):
    rows = synthetic_rows()
    if mutation == "missing":
        rows.pop()
    elif mutation == "duplicate":
        rows[-1] = dict(rows[0])
    elif mutation == "extra":
        rows.append(dict(rows[-1]))
    else:
        rows[0], rows[1] = rows[1], rows[0]
    with pytest.raises(evaluator.DataContractError):
        evaluator.validate_csv_bytes(render_synthetic(rows))


@pytest.mark.parametrize(
    "mutation",
    ["extra_field", "forbidden_field", "quoted", "crlf", "wrong_support", "count_domain"],
)
def test_schema_serialization_and_forbidden_information_fail_closed(mutation):
    rows = synthetic_rows()
    data = render_synthetic(rows)
    if mutation in {"extra_field", "forbidden_field"}:
        field = "extra" if mutation == "extra_field" else "width_lower_median"
        lines = data.decode().splitlines()
        lines[0] += f",{field}"
        lines[1] += ",1"
        data = ("\n".join(lines) + "\n").encode()
    elif mutation == "quoted":
        data = data.replace(b"1101000,BH,3", b'"1101000",BH,3', 1)
    elif mutation == "crlf":
        data = data.replace(b"\n", b"\r\n")
    elif mutation == "wrong_support":
        rows[0]["seed_depth_supported"] = 0
        data = render_synthetic(rows)
    else:
        rows[0]["n_transition_evaluable_starts"] = 6
        rows[0]["n_emitted_starts"] = 5
        data = render_synthetic(rows)
    with pytest.raises(evaluator.DataContractError):
        evaluator.validate_csv_bytes(data)


@pytest.mark.parametrize("kind", evaluator.SPACETIME_KINDS)
@pytest.mark.parametrize("depth", evaluator.TRANSITION_DEPTHS)
def test_each_cell_independently_forces_infeasibility_at_21(kind, depth):
    support = {
        (cell_kind, cell_depth): 24
        for cell_kind in evaluator.SPACETIME_KINDS
        for cell_depth in evaluator.TRANSITION_DEPTHS
    }
    support[(kind, depth)] = 21
    assert evaluator.evaluate_rows(synthetic_rows(support)) == evaluator.INFEASIBLE_TERMINAL


def test_21_vs_22_boundary_is_applied_only_by_evaluator():
    support = {
        (kind, depth): 24
        for kind in evaluator.SPACETIME_KINDS
        for depth in evaluator.TRANSITION_DEPTHS
    }
    support[("MINK", 5)] = 21
    assert evaluator.evaluate_rows(synthetic_rows(support)) == evaluator.INFEASIBLE_TERMINAL
    support[("MINK", 5)] = 22
    assert evaluator.evaluate_rows(synthetic_rows(support)) == evaluator.PASS_TERMINAL
    assert not hasattr(runner, "MIN_SUPPORTED_SEEDS_PER_CELL")


@pytest.mark.parametrize("terminal", [evaluator.PASS_TERMINAL, evaluator.INFEASIBLE_TERMINAL])
def test_evaluator_valid_terminals_leave_artifacts_byte_identical(
    terminal, monkeypatch, tmp_path, capsys
):
    support = None
    if terminal == evaluator.INFEASIBLE_TERMINAL:
        support = {
            (kind, depth): (21 if (kind, depth) == ("BH", 3) else 24)
            for kind in evaluator.SPACETIME_KINDS
            for depth in evaluator.TRANSITION_DEPTHS
        }
    before = write_artifact_pair(monkeypatch, tmp_path, synthetic_rows(support))
    assert evaluator.main([]) == 0
    captured = capsys.readouterr()
    assert captured.out == f"{evaluator.PREFIX}{terminal}\n"
    assert captured.err == ""
    assert evaluator.CSV_PATH.read_bytes() == before[0]
    assert evaluator.SIDECAR_PATH.read_bytes() == before[1]


@pytest.mark.parametrize("corruption", ["digest", "basename", "syntax", "csv"])
def test_hash_and_sidecar_validation(corruption, monkeypatch, tmp_path):
    csv_data, sidecar = write_artifact_pair(monkeypatch, tmp_path, synthetic_rows())
    if corruption == "digest":
        evaluator.SIDECAR_PATH.write_bytes(b"0" * 64 + sidecar[64:])
    elif corruption == "basename":
        evaluator.SIDECAR_PATH.write_bytes(sidecar.replace(evaluator.CSV_PATH.name.encode(), b"other.csv"))
    elif corruption == "syntax":
        evaluator.SIDECAR_PATH.write_bytes(sidecar.replace(b"  ", b" "))
    else:
        evaluator.CSV_PATH.write_bytes(csv_data + b"x")
    with pytest.raises(evaluator.DataContractError):
        evaluator.load_validated_artifact()


@pytest.mark.parametrize("present", ["none", "csv", "sidecar", "csv_tmp", "sidecar_tmp"])
def test_incomplete_and_temporary_artifact_sets_are_refused(present, monkeypatch, tmp_path):
    patch_paths(monkeypatch, evaluator, tmp_path)
    if present != "none":
        getattr(evaluator, f"{present.upper()}_PATH").write_bytes(b"x")
    expected = evaluator.RuntimeFailure if present == "none" else evaluator.DataContractError
    with pytest.raises(expected):
        evaluator.load_validated_artifact()


def test_evaluator_argument_refusal_precedes_artifact_read(monkeypatch, capsys):
    monkeypatch.setattr(evaluator, "load_validated_artifact", lambda: pytest.fail("artifact read"))
    assert evaluator.main(["--seed", "1101000"]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == f"{evaluator.PREFIX}{evaluator.DATA_CONTRACT_TERMINAL}\n"


def test_evaluator_has_no_generator_beam_or_geometry_dependency():
    source = Path(inspect.getsourcefile(evaluator) or "").read_text()
    tree = ast.parse(source)
    imports = [node for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))]
    rendered = " ".join(ast.unparse(node) for node in imports)
    assert "generator" not in rendered
    assert "run_pr010" not in rendered
    assert "explore_ladders" not in rendered
    assert "numpy" not in rendered


def test_atomic_publication_and_exact_sidecar(monkeypatch, tmp_path):
    patch_paths(monkeypatch, runner, tmp_path)
    data = runner.render_csv(synthetic_rows())
    runner.AtomicPublisher().publish(data)
    assert runner.CSV_PATH.read_bytes() == data
    assert runner.SIDECAR_PATH.read_bytes() == (
        f"{hashlib.sha256(data).hexdigest()}  {runner.CSV_PATH.name}\n".encode()
    )
    assert not runner.CSV_TMP_PATH.exists() and not runner.SIDECAR_TMP_PATH.exists()
    before = (runner.CSV_PATH.read_bytes(), runner.SIDECAR_PATH.read_bytes())
    with pytest.raises(runner.DataContractError):
        runner.AtomicPublisher().publish(data)
    assert (runner.CSV_PATH.read_bytes(), runner.SIDECAR_PATH.read_bytes()) == before


@pytest.mark.parametrize(
    "stage",
    [
        "csv_created",
        "csv_written",
        "csv_flushed",
        "csv_fsynced",
        "csv_reread",
        "csv_validated",
        "sidecar_created",
        "sidecar_written",
        "sidecar_flushed",
        "sidecar_fsynced",
        "sidecar_reread",
        "sidecar_validated",
        "csv_renamed",
        "sidecar_renamed",
        "directory_fsynced",
    ],
)
def test_every_publication_failure_stage_rolls_back(stage, monkeypatch, tmp_path):
    patch_paths(monkeypatch, runner, tmp_path)
    data = runner.render_csv(synthetic_rows())
    publisher = runner.AtomicPublisher()

    def fail(current):
        if current == stage:
            raise OSError("synthetic failure")

    monkeypatch.setattr(publisher, "_checkpoint", fail)
    with pytest.raises(OSError):
        publisher.publish(data)
    assert not any(path.exists() for path in runner._all_artifact_paths())


@pytest.mark.parametrize("temporary_name", ["CSV_TMP_PATH", "SIDECAR_TMP_PATH"])
def test_post_create_interrupt_is_owned_and_rolled_back(
    temporary_name, monkeypatch, tmp_path
):
    patch_paths(monkeypatch, runner, tmp_path)
    data = runner.render_csv(synthetic_rows())
    target = getattr(runner, temporary_name)
    real_open = Path.open

    def create_then_interrupt(path, mode="r", *args, **kwargs):
        handle = real_open(path, mode, *args, **kwargs)
        if path == target and mode == "xb":
            handle.close()
            raise runner.BudgetExceeded("synthetic post-create interrupt")
        return handle

    monkeypatch.setattr(Path, "open", create_then_interrupt)
    with pytest.raises(runner.BudgetExceeded):
        runner.AtomicPublisher().publish(data)
    assert not any(path.exists() for path in runner._all_artifact_paths())


@pytest.mark.parametrize("final_name", ["CSV_PATH", "SIDECAR_PATH"])
def test_post_rename_interrupt_is_owned_and_rolled_back(
    final_name, monkeypatch, tmp_path
):
    patch_paths(monkeypatch, runner, tmp_path)
    data = runner.render_csv(synthetic_rows())
    target = getattr(runner, final_name)
    real_replace = runner.os.replace

    def replace_then_interrupt(source, destination):
        real_replace(source, destination)
        if destination == target:
            raise runner.BudgetExceeded("synthetic post-rename interrupt")

    monkeypatch.setattr(runner.os, "replace", replace_then_interrupt)
    with pytest.raises(runner.BudgetExceeded):
        runner.AtomicPublisher().publish(data)
    assert not any(path.exists() for path in runner._all_artifact_paths())


def test_cleanup_failure_has_runtime_precedence(monkeypatch, tmp_path):
    patch_paths(monkeypatch, runner, tmp_path)
    data = runner.render_csv(synthetic_rows())
    publisher = runner.AtomicPublisher()
    monkeypatch.setattr(publisher, "_checkpoint", lambda stage: (_ for _ in ()).throw(OSError()) if stage == "csv_written" else None)
    real_unlink = Path.unlink

    def fail_unlink(path, *args, **kwargs):
        if path == runner.CSV_TMP_PATH:
            raise OSError("synthetic cleanup failure")
        return real_unlink(path, *args, **kwargs)

    monkeypatch.setattr(Path, "unlink", fail_unlink)
    with pytest.raises(runner.RuntimeFailure):
        publisher.publish(data)


def test_operational_precedence_is_runtime_then_contract_then_budget():
    assert runner.select_operational_terminal((runner.BudgetExceeded(),)) == runner.BUDGET_TERMINAL
    assert runner.select_operational_terminal((runner.BudgetExceeded(), runner.DataContractError())) == runner.DATA_CONTRACT_TERMINAL
    assert runner.select_operational_terminal((runner.BudgetExceeded(), runner.DataContractError(), OSError())) == runner.RUNTIME_TERMINAL


@pytest.mark.parametrize(
    "snapshot",
    [
        runner.ResourceSnapshot(0, 0, 0, 2, 1),
        runner.ResourceSnapshot(0, 0, 0, 1, 5),
        runner.ResourceSnapshot(runner.MAX_WALL_SECONDS + 1, 0, 0, 1, 1),
        runner.ResourceSnapshot(0, runner.MAX_CPU_SECONDS + 1, 0, 1, 1),
        runner.ResourceSnapshot(0, 0, runner.MAX_RSS_BYTES + 1, 1, 1),
    ],
)
def test_each_budget_dimension_fails_closed_without_artifact(snapshot, monkeypatch, tmp_path):
    patch_paths(monkeypatch, runner, tmp_path)
    with pytest.raises(runner.BudgetExceeded):
        runner.enforce_resource_snapshot(snapshot)
    assert not any(path.exists() for path in runner._all_artifact_paths())


@pytest.mark.parametrize(
    ("error", "terminal"),
    [
        (runner.BudgetExceeded(), runner.BUDGET_TERMINAL),
        (runner.DataContractError(), runner.DATA_CONTRACT_TERMINAL),
        (OSError(), runner.RUNTIME_TERMINAL),
    ],
)
def test_generator_operational_terminals_are_exact(error, terminal, monkeypatch, capsys):
    monkeypatch.setattr(runner, "run", lambda: (_ for _ in ()).throw(error))
    assert runner.main([]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == f"PR010_DEVELOPMENT_TERMINAL={terminal}\n"


def test_generator_argument_refusal_precedes_run(monkeypatch, capsys):
    monkeypatch.setattr(runner, "run", lambda: pytest.fail("run called"))
    assert runner.main(["--override", "1"]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == f"PR010_DEVELOPMENT_TERMINAL={runner.DATA_CONTRACT_TERMINAL}\n"


def test_postpublication_budget_failure_removes_the_complete_pair(
    monkeypatch, tmp_path
):
    patch_paths(monkeypatch, runner, tmp_path)
    rows = synthetic_rows()
    monkeypatch.setattr(runner, "build_coverage_rows", lambda: rows)

    class FakeBudget:
        def __init__(self):
            self.checks = 0

        def __enter__(self):
            return self

        def check(self):
            self.checks += 1
            if self.checks == 3:
                raise runner.BudgetExceeded("synthetic late budget")

        def __exit__(self, *_args):
            return False

    monkeypatch.setattr(runner, "BudgetGuard", FakeBudget)
    with pytest.raises(runner.BudgetExceeded):
        runner.run()
    assert not any(path.exists() for path in runner._all_artifact_paths())


def test_success_terminal_does_not_compute_coverage(monkeypatch, capsys):
    monkeypatch.setattr(runner, "run", lambda: None)
    assert runner.main([]) == 0
    captured = capsys.readouterr()
    assert captured.out == f"{runner.PUBLISHED_TERMINAL}\n"
    assert captured.err == ""
    assert "PASS_DEVELOPMENT_COVERAGE" not in Path(inspect.getsourcefile(runner) or "").read_text()
