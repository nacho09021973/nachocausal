from __future__ import annotations

import csv
import hashlib
import io
from dataclasses import replace
from pathlib import Path

import pytest

from dev import audit_pr008_h_hat_baseline_leakage as audit


CONFIGURATION_DIGEST = "479af5244d580f6cd3ca938e7644a2c852b90a6a7d00259609d9fb812681b66e"
PROVENANCE_DIGEST = "3a711d1b4019ace446653eb3ee6e2c167ddb6ac9b9311b8ff950afc409a1c4b4"
RUN_ID = "220ea523938dcddf34f8f3940133955adee73b6b56da9824e28e4dbea54f38cc"
TEST_PATHS = tuple(
    f"tests/input_{index:02d}.{'csv' if index in (3, 6) else 'md'}"
    for index in range(1, 8)
)
TEST_OUTPUT_PATHS = (
    "tests/TEST_VECTOR_ONLY/output.csv",
    "tests/TEST_VECTOR_ONLY/report.md",
)
IDENTIFIERS = audit.Identifiers(RUN_ID, CONFIGURATION_DIGEST, PROVENANCE_DIGEST)


@pytest.fixture(autouse=True)
def forbid_real_pr008_input_reads(monkeypatch):
    real_inputs = {
        (audit.REPO_ROOT / relative).resolve() for relative in audit.INPUT_ARTIFACTS
    }
    original_open = Path.open

    def guarded_open(path, *args, **kwargs):
        if path.resolve() in real_inputs:
            pytest.fail(f"test attempted to open real PR008 input: {path}")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded_open)


def sequence_rows(
    seed: int,
    intensity: float,
    start_id: int,
    first_empty: int,
    *,
    K: int = 8,
) -> list[audit.InputRow]:
    return [
        audit.InputRow(
            seed,
            intensity,
            K,
            start_id,
            depth,
            "EMPTY" if depth >= first_empty and first_empty <= 25 else "EVALUABLE",
        )
        for depth in range(1, 26)
    ]


def synthetic_reference_rows() -> list[audit.InputRow]:
    values = {
        1.0: (4, 4, 5, 5, 6, 6),
        2.0: (3, 4, 4, 4, 5, 6),
        3.0: (8, 8, 8, 9, 9, 9),
    }
    return [
        row
        for intensity, depths in values.items()
        for seed, first_empty in zip(audit.FROZEN_PR006_SEEDS, depths, strict=True)
        for row in sequence_rows(seed, intensity, 0, first_empty)
    ]


def synthetic_evaluation_rows() -> list[audit.InputRow]:
    return [
        row
        for seed in (2001, 2002)
        for intensity in (1.0, 2.0, 3.0)
        for row in sequence_rows(seed, intensity, 0, 4)
    ]


def write_input_csv(path: Path, rows: list[audit.InputRow]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(audit.REQUIRED_CALCULATION_COLUMNS)
    for row in rows:
        writer.writerow((
            row.seed,
            row.intensity,
            row.K,
            row.start_id,
            row.depth_k,
            row.slice_status,
        ))
    data = output.getvalue().encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def failure_summary(
    identifiers: audit.Identifiers = IDENTIFIERS,
    label: str = "FAILED_DATA_CONTRACT",
) -> audit.AuditSummary:
    return audit.AuditSummary(identifiers, label, None, None, None, None, None)


def valid_failure_pair(
    identifiers: audit.Identifiers = IDENTIFIERS,
    hash_03: str = "2" * 64,
    hash_06: str = "3" * 64,
) -> tuple[bytes, bytes]:
    summary = failure_summary(identifiers)
    csv_data = audit.render_audit_csv(summary, [])
    report_data = audit.render_report(
        summary,
        TEST_PATHS,
        hash_03,
        hash_06,
        *TEST_OUTPUT_PATHS,
        audit.empty_failure_counts(),
        None,
    )
    return csv_data, report_data


def pair_validators(
    configuration_digest: str = CONFIGURATION_DIGEST,
):
    def validate_csv(data: bytes):
        return audit.validate_audit_csv_bytes(data)

    def validate_report(data: bytes):
        return audit.validate_report_bytes(
            data, TEST_PATHS, TEST_OUTPUT_PATHS, configuration_digest
        )

    def validate_pair(csv_data: bytes, report_data: bytes):
        return audit.validate_output_pair_bytes(
            csv_data,
            report_data,
            TEST_PATHS,
            TEST_OUTPUT_PATHS,
            configuration_digest,
        )

    return validate_csv, validate_report, validate_pair


def publication_paths(root: Path) -> audit.PublicationPaths:
    return audit.PublicationPaths(
        root / "output.csv",
        root / "report.md",
        root / ".output.csv.tmp",
        root / ".report.md.tmp",
    )


def write_valid_pair(paths: audit.PublicationPaths) -> tuple[bytes, bytes]:
    csv_data, report_data = valid_failure_pair()
    paths.csv_final.write_bytes(csv_data)
    paths.report_final.write_bytes(report_data)
    return csv_data, report_data


def validate_pair_paths(csv_path: Path, report_path: Path) -> None:
    pair_validators()[2](csv_path.read_bytes(), report_path.read_bytes())


def test_lower_median_and_first_empty_vectors():
    assert audit.lower_median([9, 1, 5]) == 5
    assert audit.lower_median([9, 1, 5, 3]) == 3
    rows = (
        sequence_rows(1, 1.0, 0, 1)
        + sequence_rows(1, 1.0, 1, 25)
        + sequence_rows(1, 1.0, 2, 26)
    )
    derived = audit.derive_h_hat(rows)
    assert list(derived.first_empty_by_sequence.values()) == [1, 25, 26]
    assert derived.h_hat_by_cell == {(1, 1.0): 25}


def test_frozen_interface_schema_and_paths():
    assert audit.PRODUCTION_COMMAND == "python3 dev/audit_pr008_h_hat_baseline_leakage.py"
    assert len(audit.INPUT_ARTIFACTS) == 7
    assert len(audit.CSV_COLUMNS) == 17
    assert len(audit.MACHINE_KEYS) == 22
    assert audit.CSV_FINAL_PATH == "data/reports/pr008_h_hat_baseline_leakage_audit.csv"
    assert audit.REPORT_FINAL_PATH == "data/reports/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_REPORT.md"
    assert audit.CSV_TEMP_PATH == "data/reports/.pr008_h_hat_baseline_leakage_audit.csv.tmp"
    assert audit.REPORT_TEMP_PATH == "data/reports/.PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_REPORT.md.tmp"


@pytest.mark.parametrize("path", ["/absolute", "./relative", "a/../b", "a\\b"])
def test_canonical_paths_reject_overrides(path):
    with pytest.raises(ValueError):
        audit.normalize_path(path)


def test_reference_baselines_use_exact_six_seed_lower_median():
    reference = audit.derive_h_hat(synthetic_reference_rows())
    evaluation_cells = {(999, intensity) for intensity in (1.0, 2.0, 3.0)}
    baselines = audit.build_reference_baselines(reference.h_hat_by_cell, evaluation_cells)
    assert baselines["pr006_intensity_h_hat"] == {
        (999, 1.0): 5,
        (999, 2.0): 4,
        (999, 3.0): 8,
    }
    assert set(baselines) == {"pr006_block_h_hat", "pr006_intensity_h_hat"}
    assert audit.build_reference_baselines(
        reference.h_hat_by_cell, {(123456, 1.0)}
    )["pr006_intensity_h_hat"][(123456, 1.0)] == 5


def test_reference_baselines_reject_missing_duplicate_and_new_intensity():
    reference = audit.derive_h_hat(synthetic_reference_rows()).h_hat_by_cell
    missing = dict(reference)
    missing.pop(next(iter(missing)))
    with pytest.raises(audit.DataContractError) as exc:
        audit.build_reference_baselines(missing, {(1, 1.0)})
    assert exc.value.counts["missing_frozen_pr006_seed_intensity_cells"] > 0
    duplicated = [*reference.items(), next(iter(reference.items()))]
    with pytest.raises(audit.DataContractError) as exc:
        audit.build_reference_baselines(duplicated, {(1, 1.0)})
    assert exc.value.counts["duplicate_derived_pr006_cells"] == 1
    with pytest.raises(audit.DataContractError):
        audit.build_reference_baselines(reference, {(1, 7.0)})


def test_metrics_oracle_exclusion_and_boundaries():
    cells = {(1, 1.0): 4, (1, 2.0): 4, (1, 3.0): 5}
    primary = {
        "constant_depth_8": {cell: 8 for cell in cells},
        "constant_depth_26": {cell: 26 for cell in cells},
        "pr006_block_h_hat": {cell: 5 for cell in cells},
        "pr006_intensity_h_hat": {
            (1, 1.0): 5,
            (1, 2.0): 4,
            (1, 3.0): 8,
        },
    }
    metrics = audit.compute_primary_metrics(cells, primary)
    assert metrics.h_hat_cell_agreement_with_H4 == pytest.approx(2 / 3)
    assert metrics.max_baseline_cell_agreement_with_H4 == pytest.approx(1 / 3)
    assert metrics.delta_agreement == pytest.approx(1 / 3)
    constants = audit.build_constant_baselines(cells)
    assert constants["constant_depth_4"] == {cell: 4 for cell in cells}
    assert "constant_depth_4" not in metrics.baseline_agreements
    with pytest.raises(audit.DataContractError):
        audit.compute_primary_metrics(cells, {**primary, "constant_depth_4": constants["constant_depth_4"]})


def test_secondary_summaries_are_frozen_set():
    rows = synthetic_evaluation_rows()
    evaluation = audit.derive_h_hat(rows)
    secondary = audit.compute_secondary_summaries(rows, evaluation.h_hat_by_cell)
    assert secondary.H_hat_block == 4
    assert secondary.cell_fraction_H4 == 1.0
    assert secondary.seed_group_medians == {2001: 4, 2002: 4}
    assert secondary.intensity_group_medians == {1.0: 4, 2.0: 4, 3.0: 4}


def test_report_uses_readable_decimal_intensities():
    secondary = audit.compute_secondary_summaries(
        synthetic_evaluation_rows(),
        audit.derive_h_hat(synthetic_evaluation_rows()).h_hat_by_cell,
    )
    report = audit.render_report(
        failure_summary(),
        TEST_PATHS,
        "2" * 64,
        "3" * 64,
        *TEST_OUTPUT_PATHS,
        audit.empty_failure_counts(),
        secondary,
    ).decode("utf-8")

    assert "`intensity_group_median(1.0)`: 4" in report
    assert "`intensity_group_median(3ff0000000000000)`" not in report


@pytest.mark.parametrize(
    ("flags", "metrics", "expected"),
    [
        (audit.TerminalFlags(True, True, True), None, "FAILED_RUNTIME"),
        (audit.TerminalFlags(False, True, True), None, "FAILED_DATA_CONTRACT"),
        (audit.TerminalFlags(False, False, True), None, "FAILED_LEAKAGE_AUDIT"),
        (
            audit.TerminalFlags(),
            audit.PrimaryMetrics(0.5, {}, 0.5, 0.0),
            "BASELINE_DOMINATED",
        ),
        (
            audit.TerminalFlags(),
            audit.PrimaryMetrics(1.0, {}, 0.5, 0.5),
            "PASSED_BASELINE_AND_LEAKAGE_AUDIT",
        ),
        (
            audit.TerminalFlags(),
            audit.PrimaryMetrics(0.75, {}, 0.5, 0.25),
            "INCONCLUSIVE",
        ),
    ],
)
def test_terminal_precedence_and_all_labels(flags, metrics, expected):
    assert audit.assign_terminal_label(flags, metrics) == expected


def test_canonical_known_answer_vector():
    fields = (
        ("vector_schema", "string", "TEST_VECTOR_ONLY"),
        ("ascii", "string", "alpha"),
        ("unicode", "string", "e\u0301"),
        ("reserved", "string", "a,b=c%\n"),
        ("path", "path", "tests/vector.txt"),
        ("boolean", "bool", True),
        ("integer", "int", -7),
        ("float_positive", "float", 1.5),
        ("float_negative_zero", "float", -0.0),
        ("null_value", "null", None),
    )
    payload = audit.canonical_payload(fields)
    expected = (
        b"vector_schema=TEST_VECTOR_ONLY\n"
        b"ascii=alpha\n"
        b"unicode=%C3%A9\n"
        b"reserved=a%2Cb%3Dc%25%0A\n"
        b"path=tests/vector.txt\n"
        b"boolean=true\n"
        b"integer=-7\n"
        b"float_positive=3ff8000000000000\n"
        b"float_negative_zero=0000000000000000\n"
        b"null_value=null\n"
    )
    assert payload == expected
    assert payload.hex() == (
        "766563746f725f736368656d613d544553545f564543544f525f4f4e4c590a61736369693d616c7068610a756e69636f64653d2543332541390a72657365727665643d6125324362253344632532352530410a706174683d74657374732f766563746f722e7478740a626f6f6c65616e3d747275650a696e74656765723d2d370a666c6f61745f706f7369746976653d336666383030303030303030303030300a666c6f61745f6e656761746976655f7a65726f3d303030303030303030303030303030300a6e756c6c5f76616c75653d6e756c6c0a"
    )
    assert hashlib.sha256(payload).hexdigest() == "dfc42ccbf753154ff7c74cfe46a7a1c5b0a3cfa1866002189431a5fbfd053726"


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0.0, "0000000000000000"),
        (-0.0, "0000000000000000"),
        (1.0, "3ff0000000000000"),
        (-1.0, "bff0000000000000"),
        (1.5, "3ff8000000000000"),
    ],
)
def test_float_known_answers(value, expected):
    assert audit.serialize_float(value) == expected
    assert audit.serialize_float(audit.parse_float_hex(expected)) == expected


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_float_serializer_rejects_nonfinite(value):
    with pytest.raises(ValueError):
        audit.serialize_float(value)


@pytest.mark.parametrize(
    "value",
    [
        "0x3ff0000000000000",
        "3FF0000000000000",
        "3ff000000000000",
        "03ff0000000000000",
        "1.0",
        "1e0",
        "7ff0000000000000",
        "fff0000000000000",
        "7ff8000000000000",
        "8000000000000000",
    ],
)
def test_float_parser_negative_vectors(value):
    with pytest.raises(audit.OutputContractError):
        audit.parse_float_hex(value)


def test_fingerprint_and_run_id_known_answers():
    configuration = audit.configuration_fingerprint(
        "tests/preregistration.md",
        "0" * 64,
        "tests/implementation_plan.md",
        "1" * 64,
        "python3 tests/audit.py",
    )
    provenance = audit.input_provenance_fingerprint(TEST_PATHS, "2" * 64, "3" * 64)
    run_id = audit.make_run_id(configuration, provenance)
    assert configuration == CONFIGURATION_DIGEST
    assert provenance == PROVENANCE_DIGEST
    assert run_id == RUN_ID


def test_input_artifact_validation_missing_and_hash_mismatch(tmp_path):
    paths = tuple(f"fixtures/input_{index}.txt" for index in range(7))
    for relative in paths[:-1]:
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(relative.encode())
    expected = {paths[0]: "0" * 64}
    with pytest.raises(audit.DataContractError) as exc:
        audit.validate_artifacts(tmp_path, paths, expected)
    assert exc.value.counts["missing_required_artifacts"] == 1
    assert exc.value.counts["artifact_sha256_mismatches"] == 1


def test_existing_but_unreadable_artifact_is_runtime_class(monkeypatch, tmp_path):
    paths = tuple(f"fixtures/input_{index}.txt" for index in range(7))
    for relative in paths:
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"synthetic")

    def unreadable(_path):
        raise OSError("TEST_VECTOR_ONLY unreadable")

    monkeypatch.setattr(audit, "sha256_file", unreadable)
    with pytest.raises(audit.ArtifactReadError):
        audit.validate_artifacts(tmp_path, paths, {paths[0]: "0" * 64})


def test_input_csv_validation_and_fail_closed_cases(tmp_path):
    valid_path = tmp_path / "valid.csv"
    write_input_csv(valid_path, sequence_rows(1, 1.0, 0, 4))
    assert len(audit.read_and_validate_csv(valid_path, "evaluation")) == 25

    missing_column = tmp_path / "missing.csv"
    missing_column.write_text("seed,intensity,K,start_id,depth_k\n", encoding="utf-8")
    with pytest.raises(audit.DataContractError):
        audit.read_and_validate_csv(missing_column, "evaluation")

    nonfinite = tmp_path / "nonfinite.csv"
    data = valid_path.read_text().replace(",1.0,", ",NaN,", 1)
    nonfinite.write_text(data, encoding="utf-8")
    with pytest.raises(audit.DataContractError):
        audit.read_and_validate_csv(nonfinite, "evaluation")

    duplicate = tmp_path / "duplicate.csv"
    lines = valid_path.read_text().splitlines()
    duplicate.write_text("\n".join([*lines, lines[1]]) + "\n", encoding="utf-8")
    with pytest.raises(audit.DataContractError) as exc:
        audit.read_and_validate_csv(duplicate, "evaluation")
    assert exc.value.counts["duplicate_raw_rows"] == 1

    incomplete = tmp_path / "incomplete.csv"
    incomplete.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")
    with pytest.raises(audit.DataContractError) as exc:
        audit.read_and_validate_csv(incomplete, "evaluation")
    assert exc.value.counts["incomplete_depth_coverage_sequences"] == 1

    wrong_k = tmp_path / "wrong_k.csv"
    wrong_k.write_text(valid_path.read_text().replace(",8,", ",4,"), encoding="utf-8")
    with pytest.raises(audit.DataContractError) as exc:
        audit.read_and_validate_csv(wrong_k, "evaluation")
    assert exc.value.counts["rows_with_nonreference_k"] == 25


def test_input_projection_never_exposes_an_extra_column(tmp_path):
    path = tmp_path / "projected.csv"
    base = io.StringIO(newline="")
    writer = csv.writer(base, lineterminator="\n")
    writer.writerow((*audit.REQUIRED_CALCULATION_COLUMNS, "forbidden_extra"))
    for row in sequence_rows(1, 1.0, 0, 4):
        writer.writerow((
            row.seed, row.intensity, row.K, row.start_id, row.depth_k,
            row.slice_status, "TEST_VECTOR_ONLY",
        ))
    path.write_text(base.getvalue(), encoding="utf-8")
    projected = audit.read_and_validate_csv(path, "evaluation")
    assert set(projected[0].__dict__) == set(audit.REQUIRED_CALCULATION_COLUMNS)


def test_exact_failure_csv_known_answer():
    csv_data, _report = valid_failure_pair()
    expected = (
        "record_type,run_id,configuration_fingerprint,input_provenance_fingerprint,seed,intensity,estimator_id,estimator_role,predicted_depth,agrees_with_H4,included_in_primary_max,terminal_label,h_hat_cell_agreement_with_H4,max_baseline_cell_agreement_with_H4,delta_agreement,H_hat_block,cell_fraction_H4\n"
        f"RUN_SUMMARY,{RUN_ID},{CONFIGURATION_DIGEST},{PROVENANCE_DIGEST},null,null,null,null,null,null,null,FAILED_DATA_CONTRACT,null,null,null,null,null\n"
    ).encode()
    assert csv_data == expected
    audit.validate_audit_csv_bytes(csv_data)


def nonfailure_pair() -> tuple[bytes, bytes]:
    reference = audit.derive_h_hat(synthetic_reference_rows())
    evaluation_rows = synthetic_evaluation_rows()
    evaluation = audit.derive_h_hat(evaluation_rows)
    empirical = audit.build_reference_baselines(reference.h_hat_by_cell, evaluation.h_hat_by_cell)
    constants = audit.build_constant_baselines(evaluation.h_hat_by_cell)
    primary = {
        "constant_depth_8": constants["constant_depth_8"],
        "constant_depth_26": constants["constant_depth_26"],
        "pr006_block_h_hat": empirical["pr006_block_h_hat"],
        "pr006_intensity_h_hat": empirical["pr006_intensity_h_hat"],
    }
    metrics = audit.compute_primary_metrics(evaluation.h_hat_by_cell, primary)
    secondary = audit.compute_secondary_summaries(evaluation_rows, evaluation.h_hat_by_cell)
    label = audit.assign_terminal_label(audit.TerminalFlags(), metrics)
    summary = audit.AuditSummary(
        IDENTIFIERS,
        label,
        metrics.h_hat_cell_agreement_with_H4,
        metrics.max_baseline_cell_agreement_with_H4,
        metrics.delta_agreement,
        secondary.H_hat_block,
        secondary.cell_fraction_H4,
    )
    cells = audit.make_cell_estimates(
        IDENTIFIERS,
        label,
        evaluation.h_hat_by_cell,
        primary,
        constants[audit.ORACLE_BASELINE_ID],
    )
    csv_data = audit.render_audit_csv(summary, cells)
    report = audit.render_report(
        summary,
        TEST_PATHS,
        "2" * 64,
        "3" * 64,
        *TEST_OUTPUT_PATHS,
        audit.empty_failure_counts(),
        secondary,
    )
    return csv_data, report


@pytest.mark.parametrize(
    "mutator",
    [
        lambda data: data.replace(b"\n", b"\r\n"),
        lambda data: data.replace(b"RUN_SUMMARY", b'"RUN_SUMMARY"', 1),
        lambda data: data.replace(b"RUN_SUMMARY", b'"RUN_SUMMARY', 1),
        lambda data: data.replace(b",null,", b",,", 1),
        lambda data: data.replace(b",null,null,null,null,null,null,null,FAILED", b",0,null,null,null,null,null,null,FAILED", 1),
        lambda data: data.replace(b"record_type,", b"unknown,record_type,", 1),
        lambda data: data.replace(b"record_type,", b"", 1),
        lambda data: data.replace(b"record_type,run_id", b"run_id,record_type", 1),
        lambda data: data.replace(b"RUN_SUMMARY", b"UNKNOWN_ROW", 1),
        lambda data: data + data.split(b"\n")[1] + b"\n",
    ],
)
def test_csv_negative_contract_vectors(mutator):
    csv_data, _report = valid_failure_pair()
    with pytest.raises(audit.OutputContractError):
        audit.validate_audit_csv_bytes(mutator(csv_data))


def test_nonfailure_csv_row_invariants_and_duplicates():
    csv_data, _report = nonfailure_pair()
    summary, cells = audit.validate_audit_csv_bytes(csv_data)
    assert summary["terminal_label"] == "PASSED_BASELINE_AND_LEAKAGE_AUDIT"
    assert len(cells) == 6 * 6
    lines = csv_data.splitlines(keepends=True)
    duplicate = b"".join([*lines, lines[2]])
    with pytest.raises(audit.OutputContractError):
        audit.validate_audit_csv_bytes(duplicate)
    reordered = b"".join([lines[0], lines[1], lines[3], lines[2], *lines[4:]])
    with pytest.raises(audit.OutputContractError):
        audit.validate_audit_csv_bytes(reordered)

    parsed = list(csv.reader(io.StringIO(csv_data.decode(), newline=""), strict=True))
    parsed[1][audit.CSV_COLUMNS.index("h_hat_cell_agreement_with_H4")] = "0000000000000000"
    output = io.StringIO(newline="")
    csv.writer(output, lineterminator="\n").writerows(parsed)
    with pytest.raises(audit.OutputContractError, match="does not match"):
        audit.validate_audit_csv_bytes(output.getvalue().encode())


def test_machine_block_exact_keys_and_known_provenance_vector():
    _csv_data, report = valid_failure_pair()
    values = audit.validate_report_bytes(
        report, TEST_PATHS, TEST_OUTPUT_PATHS, CONFIGURATION_DIGEST
    )
    assert tuple(values) == audit.MACHINE_KEYS
    assert len(values) == 22
    assert values["input_provenance_fingerprint"] == PROVENANCE_DIGEST
    text = report.decode()
    block = text[text.index(audit.MACHINE_BEGIN):text.index(audit.MACHINE_END) + len(audit.MACHINE_END)]
    assert block.splitlines()[0] == audit.MACHINE_BEGIN
    assert block.splitlines()[-1] == audit.MACHINE_END


@pytest.mark.parametrize(
    "mutator",
    [
        lambda data: data.replace(b"BEGIN_PR008_MACHINE_READABLE_V1\n", b"", 1),
        lambda data: data + data[data.index(b"BEGIN_PR008_MACHINE_READABLE_V1"):],
        lambda data: data.replace(b"machine_schema=", b"extra=x\nmachine_schema=", 1),
        lambda data: data.replace(b"machine_schema=pr008-machine-readable-v1\n", b"", 1),
        lambda data: data.replace(b"run_id=", b"machine_schema=pr008-machine-readable-v1\nrun_id=", 1),
        lambda data: data.replace(
            b"run_id=" + RUN_ID.encode() + b"\nconfiguration_fingerprint=",
            b"configuration_fingerprint=",
            1,
        ),
        lambda data: data.replace(b"tests/input_01.md", b"tests/changed.md"),
        lambda data: data.replace(PROVENANCE_DIGEST.encode(), b"4" * 64, 1),
        lambda data: data.replace(
            b"## 9. Interpretation limits\n",
            b"## Unexpected section\n\n## 9. Interpretation limits\n",
            1,
        ),
    ],
)
def test_machine_block_negative_vectors(mutator):
    _csv_data, report = valid_failure_pair()
    with pytest.raises(audit.OutputContractError):
        audit.validate_report_bytes(
            mutator(report), TEST_PATHS, TEST_OUTPUT_PATHS, CONFIGURATION_DIGEST
        )


def test_pair_rejects_divergent_shared_fields():
    csv_data, report = valid_failure_pair()
    changed = report.replace(b"terminal_label=FAILED_DATA_CONTRACT", b"terminal_label=FAILED_RUNTIME")
    audit.validate_report_bytes(changed, TEST_PATHS, TEST_OUTPUT_PATHS, CONFIGURATION_DIGEST)
    with pytest.raises(audit.OutputContractError):
        pair_validators()[2](csv_data, changed)


def test_cli_rejects_every_override(monkeypatch):
    monkeypatch.setattr(audit, "run_production", lambda: pytest.fail("production must not run"))
    assert audit.main(["--input", "anything"]) == 2


def test_publication_vector_1_clean(tmp_path):
    result = audit.preflight_publication(publication_paths(tmp_path), validate_pair_paths)
    assert result == audit.PreflightResult("CLEAN", True)


def test_publication_vector_2_temporaries_are_deleted(tmp_path):
    paths = publication_paths(tmp_path)
    paths.csv_temp.write_bytes(b"temporary")
    paths.report_temp.write_bytes(b"temporary")
    result = audit.preflight_publication(paths, validate_pair_paths)
    assert result == audit.PreflightResult("CLEAN", True)
    assert not paths.csv_temp.exists() and not paths.report_temp.exists()


@pytest.mark.parametrize("which", ["csv", "report"])
def test_publication_vectors_3_and_4_lone_final(tmp_path, which):
    paths = publication_paths(tmp_path)
    target = paths.csv_final if which == "csv" else paths.report_final
    target.write_bytes(b"partial")
    result = audit.preflight_publication(paths, validate_pair_paths)
    assert result == audit.PreflightResult("PARTIALLY_PUBLISHED", True)
    assert not paths.csv_final.exists() and not paths.report_final.exists()


def test_publication_vector_5_one_final_invalid(tmp_path):
    paths = publication_paths(tmp_path)
    write_valid_pair(paths)
    paths.report_final.write_bytes(b"invalid")
    result = audit.preflight_publication(paths, validate_pair_paths)
    assert result == audit.PreflightResult("FAILED_OUTPUT_CONTRACT", True)
    assert not paths.csv_final.exists() and not paths.report_final.exists()


def test_preflight_cleans_pair_when_source_backed_validation_fails(tmp_path):
    paths = publication_paths(tmp_path)
    write_valid_pair(paths)

    def source_contract_failure(_csv_path, _report_path):
        raise audit.DataContractError("TEST_VECTOR_ONLY source failure")

    result = audit.preflight_publication(paths, source_contract_failure)
    assert result == audit.PreflightResult("FAILED_OUTPUT_CONTRACT", True)
    assert not paths.csv_final.exists() and not paths.report_final.exists()


def test_publication_vector_6_individually_valid_but_divergent(tmp_path):
    paths = publication_paths(tmp_path)
    csv_data, _report = valid_failure_pair()
    other_provenance = audit.input_provenance_fingerprint(TEST_PATHS, "4" * 64, "3" * 64)
    other_ids = audit.Identifiers(
        audit.make_run_id(CONFIGURATION_DIGEST, other_provenance),
        CONFIGURATION_DIGEST,
        other_provenance,
    )
    _other_csv, other_report = valid_failure_pair(other_ids, "4" * 64, "3" * 64)
    audit.validate_audit_csv_bytes(csv_data)
    audit.validate_report_bytes(other_report, TEST_PATHS, TEST_OUTPUT_PATHS, CONFIGURATION_DIGEST)
    paths.csv_final.write_bytes(csv_data)
    paths.report_final.write_bytes(other_report)
    result = audit.preflight_publication(paths, validate_pair_paths)
    assert result == audit.PreflightResult("FAILED_OUTPUT_CONTRACT", True)
    assert not paths.csv_final.exists() and not paths.report_final.exists()


def test_publication_vector_7_residual_temp_then_revalidate(tmp_path):
    paths = publication_paths(tmp_path)
    write_valid_pair(paths)
    paths.csv_temp.write_bytes(b"residual")
    result = audit.preflight_publication(paths, validate_pair_paths)
    assert result == audit.PreflightResult("VALID", False)
    assert not paths.csv_temp.exists()
    assert paths.csv_final.exists() and paths.report_final.exists()


def test_publication_vector_8_interrupt_after_first_final_rolls_back(tmp_path):
    paths = publication_paths(tmp_path)
    csv_data, report = valid_failure_pair()
    validators = pair_validators()

    def interrupt():
        raise KeyboardInterrupt()

    with pytest.raises(KeyboardInterrupt):
        audit.publish_output_pair(
            csv_data, report, paths, *validators, after_csv_publish=interrupt
        )
    assert not any(path.exists() for path in (
        paths.csv_final, paths.report_final, paths.csv_temp, paths.report_temp
    ))


def test_publication_vector_9_valid_pair_preserved_and_retry_refused(tmp_path):
    paths = publication_paths(tmp_path)
    csv_data, report = valid_failure_pair()
    validators = pair_validators()
    result = audit.publish_output_pair(csv_data, report, paths, *validators)
    assert result == audit.PreflightResult("CLEAN", True)
    validate_pair_paths(paths.csv_final, paths.report_final)
    with pytest.raises(audit.PublicationError, match="VALID_OUTPUT_SET_EXISTS"):
        audit.publish_output_pair(csv_data, report, paths, *validators)
    assert paths.csv_final.read_bytes() == csv_data
    assert paths.report_final.read_bytes() == report


def test_synthetic_end_to_end_and_byte_repeatability(tmp_path):
    fixture_root = tmp_path / "fixtures"
    reference_path = fixture_root / TEST_PATHS[2]
    evaluation_path = fixture_root / TEST_PATHS[5]
    reference_bytes = write_input_csv(reference_path, synthetic_reference_rows())
    evaluation_bytes = write_input_csv(evaluation_path, synthetic_evaluation_rows())
    for index, relative in enumerate(TEST_PATHS):
        path = fixture_root / relative
        if index not in (2, 5):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"TEST_VECTOR_ONLY_{index}\n", encoding="utf-8")
    expected_hashes = {
        TEST_PATHS[2]: hashlib.sha256(reference_bytes).hexdigest(),
        TEST_PATHS[5]: hashlib.sha256(evaluation_bytes).hexdigest(),
    }
    validated = audit.validate_artifacts(fixture_root, TEST_PATHS, expected_hashes)
    reference_rows = audit.read_and_validate_csv(reference_path, "reference")
    evaluation_rows = audit.read_and_validate_csv(evaluation_path, "evaluation")
    reference = audit.derive_h_hat(reference_rows)
    evaluation = audit.derive_h_hat(evaluation_rows)
    empirical = audit.build_reference_baselines(reference.h_hat_by_cell, evaluation.h_hat_by_cell)
    constants = audit.build_constant_baselines(evaluation.h_hat_by_cell)
    primary = {
        "constant_depth_8": constants["constant_depth_8"],
        "constant_depth_26": constants["constant_depth_26"],
        "pr006_block_h_hat": empirical["pr006_block_h_hat"],
        "pr006_intensity_h_hat": empirical["pr006_intensity_h_hat"],
    }
    metrics = audit.compute_primary_metrics(evaluation.h_hat_by_cell, primary)
    secondary = audit.compute_secondary_summaries(evaluation_rows, evaluation.h_hat_by_cell)
    label = audit.assign_terminal_label(audit.TerminalFlags(), metrics)
    provenance = audit.input_provenance_fingerprint(
        TEST_PATHS,
        validated.observed_hashes[TEST_PATHS[2]],
        validated.observed_hashes[TEST_PATHS[5]],
    )
    ids = audit.Identifiers(
        audit.make_run_id(CONFIGURATION_DIGEST, provenance),
        CONFIGURATION_DIGEST,
        provenance,
    )
    summary = audit.AuditSummary(
        ids, label,
        metrics.h_hat_cell_agreement_with_H4,
        metrics.max_baseline_cell_agreement_with_H4,
        metrics.delta_agreement,
        secondary.H_hat_block,
        secondary.cell_fraction_H4,
    )
    cells = audit.make_cell_estimates(
        ids, label, evaluation.h_hat_by_cell, primary, constants[audit.ORACLE_BASELINE_ID]
    )
    csv_first = audit.render_audit_csv(summary, cells)
    report_first = audit.render_report(
        summary,
        TEST_PATHS,
        validated.observed_hashes[TEST_PATHS[2]],
        validated.observed_hashes[TEST_PATHS[5]],
        *TEST_OUTPUT_PATHS,
        audit.empty_failure_counts(),
        secondary,
    )
    csv_second = audit.render_audit_csv(summary, cells)
    report_second = audit.render_report(
        summary,
        TEST_PATHS,
        validated.observed_hashes[TEST_PATHS[2]],
        validated.observed_hashes[TEST_PATHS[5]],
        *TEST_OUTPUT_PATHS,
        audit.empty_failure_counts(),
        secondary,
    )
    assert csv_first == csv_second
    assert report_first == report_second
    validators = pair_validators(CONFIGURATION_DIGEST)
    paths = publication_paths(tmp_path / "published")
    paths.csv_final.parent.mkdir(parents=True)
    audit.publish_output_pair(csv_first, report_first, paths, *validators)
    validators[2](paths.csv_final.read_bytes(), paths.report_final.read_bytes())
    assert label == "PASSED_BASELINE_AND_LEAKAGE_AUDIT"
