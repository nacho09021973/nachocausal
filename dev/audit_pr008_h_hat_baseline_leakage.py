"""Deterministic implementation of the frozen PR008 audit contract.

The production entry point has no arguments. Tests exercise the pure functions with
synthetic inputs; importing this module performs no I/O.
"""

from __future__ import annotations

import csv
import hashlib
import io
import math
import os
import re
import struct
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Callable, Iterable, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]

PREREGISTRATION_PATH = "dev/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_PREREGISTRATION.md"
IMPLEMENTATION_PLAN_PATH = "dev/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_IMPLEMENTATION_PLAN.md"
PRODUCTION_COMMAND = "python3 dev/audit_pr008_h_hat_baseline_leakage.py"

INPUT_ARTIFACTS = (
    "dev/PR006_ORDER_ONLY_H_HAT_PREREGISTRATION.md",
    "data/reports/PR006_ORDER_ONLY_H_HAT_VALIDATION_REPORT.md",
    "data/reports/pr006_order_only_h_hat_validation.csv",
    "dev/PR007_H_HAT_ROBUSTNESS_PREREGISTRATION.md",
    "data/reports/PR007_H_HAT_ROBUSTNESS_VALIDATION_REPORT.md",
    "data/reports/pr007_h_hat_robustness_seed_density.csv",
    "dev/PR007_A_H_HAT_ROBUSTNESS_CLOSURE_DECISION.md",
)
REFERENCE_CSV_PATH = INPUT_ARTIFACTS[2]
EVALUATION_CSV_PATH = INPUT_ARTIFACTS[5]
FROZEN_INPUT_HASHES = {
    REFERENCE_CSV_PATH: "e9f9d2dd861795454b32267477d7510ba1f48ddc0ba75fae66363a4a33cf0255",
    EVALUATION_CSV_PATH: "b0da043bd16554066d262ad897d7240052530e652475f62c9df3570c40463afd",
}

CSV_FINAL_PATH = "data/reports/pr008_h_hat_baseline_leakage_audit.csv"
REPORT_FINAL_PATH = "data/reports/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_REPORT.md"
CSV_TEMP_PATH = "data/reports/.pr008_h_hat_baseline_leakage_audit.csv.tmp"
REPORT_TEMP_PATH = "data/reports/.PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_REPORT.md.tmp"

K_REF = 8
MAX_DEPTH = 25
NO_EMPTY_SENTINEL = 26
FROZEN_PR006_SEEDS = (1000024, 1000025, 1000026, 1000027, 1000028, 1000029)
REQUIRED_CALCULATION_COLUMNS = (
    "seed",
    "intensity",
    "K",
    "start_id",
    "depth_k",
    "slice_status",
)
ALLOWED_SLICE_STATUSES = frozenset({"EMPTY", "EVALUABLE"})

PRIMARY_BASELINE_IDS = (
    "constant_depth_8",
    "constant_depth_26",
    "pr006_block_h_hat",
    "pr006_intensity_h_hat",
)
ORACLE_BASELINE_ID = "constant_depth_4"
ESTIMATOR_ORDER = ("H_hat", *PRIMARY_BASELINE_IDS, ORACLE_BASELINE_ID)
ESTIMATOR_ROLES = {
    "H_hat": "AUDITED_ESTIMATOR",
    **{baseline_id: "PRIMARY_BASELINE" for baseline_id in PRIMARY_BASELINE_IDS},
    ORACLE_BASELINE_ID: "DEGENERATE_ORACLE_SANITY_CHECK",
}

TERMINAL_LABELS = (
    "FAILED_RUNTIME",
    "FAILED_DATA_CONTRACT",
    "FAILED_LEAKAGE_AUDIT",
    "BASELINE_DOMINATED",
    "PASSED_BASELINE_AND_LEAKAGE_AUDIT",
    "INCONCLUSIVE",
)
FAILURE_LABELS = frozenset(TERMINAL_LABELS[:3])
NON_FAILURE_LABELS = frozenset(TERMINAL_LABELS[3:])

FAILURE_COUNT_KEYS = (
    "missing_required_artifacts",
    "artifact_sha256_mismatches",
    "missing_or_malformed_required_csv_columns",
    "duplicate_raw_rows",
    "incomplete_depth_coverage_sequences",
    "rows_with_nonreference_k",
    "missing_frozen_pr006_seed_intensity_cells",
    "duplicate_derived_pr006_cells",
)

CSV_COLUMNS = (
    "record_type",
    "run_id",
    "configuration_fingerprint",
    "input_provenance_fingerprint",
    "seed",
    "intensity",
    "estimator_id",
    "estimator_role",
    "predicted_depth",
    "agrees_with_H4",
    "included_in_primary_max",
    "terminal_label",
    "h_hat_cell_agreement_with_H4",
    "max_baseline_cell_agreement_with_H4",
    "delta_agreement",
    "H_hat_block",
    "cell_fraction_H4",
)

MACHINE_KEYS = (
    "machine_schema",
    "run_id",
    "configuration_fingerprint",
    "input_provenance_fingerprint",
    "publication_status",
    "terminal_label",
    "artifact_01_path",
    "artifact_02_path",
    "artifact_03_path",
    "artifact_04_path",
    "artifact_05_path",
    "artifact_06_path",
    "artifact_07_path",
    "artifact_03_sha256",
    "artifact_06_sha256",
    "csv_output_path",
    "report_output_path",
    "h_hat_cell_agreement_with_H4",
    "max_baseline_cell_agreement_with_H4",
    "delta_agreement",
    "H_hat_block",
    "cell_fraction_H4",
)
MACHINE_BEGIN = "BEGIN_PR008_MACHINE_READABLE_V1"
MACHINE_END = "END_PR008_MACHINE_READABLE_V1"
REPORT_HEADINGS = (
    "## 1. Scope and frozen input identities",
    "## 2. Data-contract checks and counts",
    "## 3. Leakage guard evidence",
    "## 4. Frozen baseline definitions and roles",
    "## 5. Primary comparison metrics",
    "## 6. Frozen secondary summaries",
    "## 7. DEGENERATE_ORACLE_SANITY_CHECK",
    "## 8. Terminal-label evaluation",
    "## 9. Interpretation limits",
)

_SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")
_INT_RE = re.compile(r"(?:0|[1-9][0-9]*)\Z")
_SIGNED_INT_RE = re.compile(r"(?:0|-?[1-9][0-9]*)\Z")
_FLOAT_HEX_RE = re.compile(r"[0-9a-f]{16}\Z")
_KEY_RE = re.compile(r"[A-Za-z0-9_]+\Z")
_SAFE_BYTES = frozenset(b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._~/-")


class DataContractError(ValueError):
    """A frozen PR008 input contract was violated."""

    def __init__(self, message: str, counts: Mapping[str, int] | None = None):
        super().__init__(message)
        self.counts = empty_failure_counts()
        if counts:
            self.counts.update(counts)


class OutputContractError(ValueError):
    """A serialized output or output pair is invalid."""


class PublicationError(RuntimeError):
    """The per-file publication protocol could not complete."""


class ArtifactReadError(RuntimeError):
    """An existing required artifact could not be read."""


def empty_failure_counts() -> dict[str, int]:
    return {key: 0 for key in FAILURE_COUNT_KEYS}


def _one_failure_count(key: str, count: int = 1) -> dict[str, int]:
    counts = empty_failure_counts()
    counts[key] = count
    return counts


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def lower_median(values: Iterable[int]) -> int:
    ordered = sorted(values)
    if not ordered:
        raise DataContractError("lower median is undefined for an empty collection")
    return ordered[(len(ordered) - 1) // 2]


def serialize_float(value: float) -> str:
    numeric = float(value)
    if not math.isfinite(numeric):
        raise ValueError("NaN and infinities are prohibited")
    if numeric == 0.0:
        numeric = 0.0
    return struct.pack(">d", numeric).hex()


def parse_float_hex(value: str) -> float:
    if not _FLOAT_HEX_RE.fullmatch(value):
        raise OutputContractError("invalid FLOAT_HEX64")
    numeric = struct.unpack(">d", bytes.fromhex(value))[0]
    if not math.isfinite(numeric):
        raise OutputContractError("non-finite FLOAT_HEX64")
    if numeric == 0.0 and value != "0000000000000000":
        raise OutputContractError("negative zero is not canonical")
    return numeric


def normalize_path(value: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError("path must be a nonempty POSIX string")
    normalized = unicodedata.normalize("NFC", value)
    pure = PurePosixPath(normalized)
    if pure.is_absolute() or normalized.startswith("./"):
        raise ValueError("path must be repository-relative")
    if any(part in {"", ".", ".."} for part in pure.parts):
        raise ValueError("path contains a forbidden component")
    if str(pure) != normalized:
        raise ValueError("path is not in canonical POSIX form")
    return normalized


def encode_string(value: str) -> str:
    normalized = unicodedata.normalize("NFC", value)
    encoded = normalized.encode("utf-8")
    return "".join(chr(byte) if byte in _SAFE_BYTES else f"%{byte:02X}" for byte in encoded)


def decode_string(value: str) -> str:
    raw = bytearray()
    index = 0
    while index < len(value):
        char = value[index]
        if char == "%":
            if index + 2 >= len(value) or not re.fullmatch(r"[0-9A-F]{2}", value[index + 1:index + 3]):
                raise OutputContractError("invalid percent escape")
            byte = int(value[index + 1:index + 3], 16)
            if byte in _SAFE_BYTES:
                raise OutputContractError("unnecessary percent escape")
            raw.append(byte)
            index += 3
            continue
        byte = ord(char)
        if byte not in _SAFE_BYTES:
            raise OutputContractError("unescaped byte in canonical string")
        raw.append(byte)
        index += 1
    try:
        decoded = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise OutputContractError("invalid UTF-8 in canonical string") from exc
    if unicodedata.normalize("NFC", decoded) != decoded or encode_string(decoded) != value:
        raise OutputContractError("noncanonical string encoding")
    return decoded


def _validate_sha256(value: str) -> str:
    if not isinstance(value, str) or not _SHA256_RE.fullmatch(value):
        raise ValueError("SHA256 must be 64 lowercase hexadecimal characters")
    return value


def encode_scalar(kind: str, value: object) -> str:
    if kind in {"string", "enum"}:
        if not isinstance(value, str):
            raise TypeError(f"{kind} value must be str")
        return encode_string(value)
    if kind == "path":
        return encode_string(normalize_path(str(value)))
    if kind == "sha256":
        return _validate_sha256(str(value))
    if kind == "bool":
        if type(value) is not bool:
            raise TypeError("boolean value must be bool")
        return "true" if value else "false"
    if kind == "int":
        if type(value) is not int:
            raise TypeError("integer value must be int")
        return str(value)
    if kind == "float":
        return serialize_float(float(value))
    if kind == "null":
        if value is not None:
            raise TypeError("null value must be None")
        return "null"
    raise ValueError(f"unknown scalar kind: {kind}")


def canonical_payload(fields: Sequence[tuple[str, str, object]]) -> bytes:
    records: list[str] = []
    seen: set[str] = set()
    for key, kind, value in fields:
        if not _KEY_RE.fullmatch(key) or key in seen:
            raise ValueError("invalid or duplicate canonical key")
        seen.add(key)
        records.append(f"{key}={encode_scalar(kind, value)}\n")
    return "".join(records).encode("ascii")


def configuration_fingerprint(
    preregistration_path: str,
    preregistration_sha256: str,
    implementation_plan_path: str,
    implementation_plan_sha256: str,
    production_command: str,
) -> str:
    fields = (
        ("fingerprint_schema", "string", "pr008-configuration-v1"),
        ("preregistration_path", "path", preregistration_path),
        ("preregistration_sha256", "sha256", preregistration_sha256),
        ("implementation_plan_path", "path", implementation_plan_path),
        ("implementation_plan_sha256", "sha256", implementation_plan_sha256),
        ("production_command", "string", production_command),
    )
    return sha256_bytes(canonical_payload(fields))


def input_provenance_fingerprint(
    artifact_paths: Sequence[str],
    artifact_03_sha256: str | None,
    artifact_06_sha256: str | None,
) -> str:
    if len(artifact_paths) != 7:
        raise ValueError("input provenance requires exactly seven artifacts")
    fields: list[tuple[str, str, object]] = [
        ("fingerprint_schema", "string", "pr008-input-provenance-v1")
    ]
    fields.extend(
        (f"artifact_{index:02d}_path", "path", path)
        for index, path in enumerate(artifact_paths, 1)
    )
    fields.extend((
        (
            "artifact_03_sha256",
            "null" if artifact_03_sha256 is None else "sha256",
            artifact_03_sha256,
        ),
        (
            "artifact_06_sha256",
            "null" if artifact_06_sha256 is None else "sha256",
            artifact_06_sha256,
        ),
    ))
    return sha256_bytes(canonical_payload(fields))


def make_run_id(configuration_digest: str, provenance_digest: str) -> str:
    fields = (
        ("run_id_schema", "string", "pr008-run-id-v1"),
        ("configuration_fingerprint", "sha256", configuration_digest),
        ("input_provenance_fingerprint", "sha256", provenance_digest),
    )
    return sha256_bytes(canonical_payload(fields))


@dataclass(frozen=True)
class InputRow:
    seed: int
    intensity: float
    K: int
    start_id: int
    depth_k: int
    slice_status: str


CellKey = tuple[int, float]
SequenceKey = tuple[int, float, int, int]


@dataclass(frozen=True)
class DerivedHhat:
    first_empty_by_sequence: Mapping[SequenceKey, int]
    h_hat_by_cell: Mapping[CellKey, int]


@dataclass(frozen=True)
class PrimaryMetrics:
    h_hat_cell_agreement_with_H4: float
    baseline_agreements: Mapping[str, float]
    max_baseline_cell_agreement_with_H4: float
    delta_agreement: float


@dataclass(frozen=True)
class SecondarySummaries:
    H_hat_block: int
    cell_fraction_H4: float
    seed_group_medians: Mapping[int, int]
    intensity_group_medians: Mapping[float, int]


@dataclass(frozen=True)
class TerminalFlags:
    runtime_failure: bool = False
    data_contract_failure: bool = False
    leakage_failure: bool = False


@dataclass(frozen=True)
class Identifiers:
    run_id: str
    configuration_fingerprint: str
    input_provenance_fingerprint: str


@dataclass(frozen=True)
class AuditSummary:
    identifiers: Identifiers
    terminal_label: str
    h_hat_cell_agreement_with_H4: float | None
    max_baseline_cell_agreement_with_H4: float | None
    delta_agreement: float | None
    H_hat_block: int | None
    cell_fraction_H4: float | None


@dataclass(frozen=True)
class CellEstimate:
    identifiers: Identifiers
    seed: int
    intensity: float
    estimator_id: str
    predicted_depth: int
    terminal_label: str


@dataclass(frozen=True)
class ArtifactValidation:
    observed_hashes: Mapping[str, str | None]
    failure_counts: Mapping[str, int]


def validate_artifacts(
    root: Path,
    artifact_paths: Sequence[str],
    expected_hashes: Mapping[str, str],
) -> ArtifactValidation:
    if len(artifact_paths) != 7 or len(set(artifact_paths)) != 7:
        raise DataContractError("artifact inventory must contain seven unique paths")
    counts = empty_failure_counts()
    observed: dict[str, str | None] = {path: None for path in artifact_paths}
    for relative in artifact_paths:
        normalize_path(relative)
        path = root / relative
        if not path.is_file():
            counts["missing_required_artifacts"] += 1
            continue
        try:
            with path.open("rb") as handle:
                handle.read(1)
            if relative in expected_hashes:
                observed[relative] = sha256_file(path)
        except OSError as exc:
            error = ArtifactReadError(f"required artifact is unreadable: {relative}")
            error.observed_hashes = observed
            raise error from exc
        if relative in expected_hashes and observed[relative] != expected_hashes[relative]:
            counts["artifact_sha256_mismatches"] += 1
    if any(counts.values()):
        error = DataContractError("artifact validation failed", counts)
        error.observed_hashes = observed
        raise error
    return ArtifactValidation(observed, counts)


def _parse_input_int(value: str, name: str, allow_zero: bool = True) -> int:
    if not isinstance(value, str) or not _INT_RE.fullmatch(value):
        raise ValueError(f"invalid {name}")
    parsed = int(value)
    if not allow_zero and parsed == 0:
        raise ValueError(f"invalid {name}")
    return parsed


def _parse_input_float(value: str) -> float:
    if not isinstance(value, str) or not value or value.strip() != value:
        raise ValueError("invalid intensity")
    try:
        parsed = float(value)
    except ValueError as exc:
        raise ValueError("invalid intensity") from exc
    if not math.isfinite(parsed):
        raise ValueError("invalid intensity")
    return 0.0 if parsed == 0.0 else parsed


def read_and_validate_csv(path: Path, contract: str) -> list[InputRow]:
    if contract not in {"reference", "evaluation"}:
        raise ValueError("unknown input contract")
    counts = empty_failure_counts()
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, strict=True)
            header = reader.fieldnames
            if header is None or len(header) != len(set(header)) or any(
                name not in header for name in REQUIRED_CALCULATION_COLUMNS
            ):
                raise DataContractError(
                    "missing or duplicate required CSV column",
                    _one_failure_count("missing_or_malformed_required_csv_columns"),
                )
            rows: list[InputRow] = []
            raw_keys: set[tuple[int, float, int, int, int]] = set()
            for raw in reader:
                if None in raw or any(raw.get(name) in {None, ""} for name in REQUIRED_CALCULATION_COLUMNS):
                    counts["missing_or_malformed_required_csv_columns"] += 1
                    continue
                try:
                    row = InputRow(
                        seed=_parse_input_int(raw["seed"], "seed"),
                        intensity=_parse_input_float(raw["intensity"]),
                        K=_parse_input_int(raw["K"], "K", allow_zero=False),
                        start_id=_parse_input_int(raw["start_id"], "start_id"),
                        depth_k=_parse_input_int(raw["depth_k"], "depth_k", allow_zero=False),
                        slice_status=raw["slice_status"],
                    )
                    if row.slice_status not in ALLOWED_SLICE_STATUSES:
                        raise ValueError("invalid slice_status")
                except (TypeError, ValueError):
                    counts["missing_or_malformed_required_csv_columns"] += 1
                    continue
                if row.K != K_REF:
                    counts["rows_with_nonreference_k"] += 1
                raw_key = (row.seed, row.intensity, row.K, row.start_id, row.depth_k)
                if raw_key in raw_keys:
                    counts["duplicate_raw_rows"] += 1
                raw_keys.add(raw_key)
                rows.append(row)
    except (csv.Error, UnicodeError, OSError) as exc:
        raise DataContractError(
            "CSV could not be parsed",
            _one_failure_count("missing_or_malformed_required_csv_columns"),
        ) from exc

    sequence_depths: dict[SequenceKey, list[int]] = defaultdict(list)
    for row in rows:
        sequence_depths[(row.seed, row.intensity, row.K, row.start_id)].append(row.depth_k)
    expected_depths = list(range(1, MAX_DEPTH + 1))
    counts["incomplete_depth_coverage_sequences"] += sum(
        sorted(depths) != expected_depths for depths in sequence_depths.values()
    )
    if not rows:
        counts["missing_or_malformed_required_csv_columns"] += 1
    if any(counts.values()):
        raise DataContractError(f"{contract} CSV contract failed", counts)
    return rows


def derive_h_hat(rows: Sequence[InputRow]) -> DerivedHhat:
    if not rows:
        raise DataContractError("cannot derive H_hat from no rows")
    grouped: dict[SequenceKey, list[InputRow]] = defaultdict(list)
    raw_keys: set[tuple[int, float, int, int, int]] = set()
    for row in rows:
        if set(row.__dict__) != set(REQUIRED_CALCULATION_COLUMNS):
            raise DataContractError("calculation row contains forbidden columns")
        raw_key = (row.seed, row.intensity, row.K, row.start_id, row.depth_k)
        if raw_key in raw_keys:
            raise DataContractError(
                "duplicate raw key", _one_failure_count("duplicate_raw_rows")
            )
        raw_keys.add(raw_key)
        if row.K != K_REF:
            raise DataContractError(
                "K differs from K_REF", _one_failure_count("rows_with_nonreference_k")
            )
        grouped[(row.seed, row.intensity, row.K, row.start_id)].append(row)

    first_empty: dict[SequenceKey, int] = {}
    expected = list(range(1, MAX_DEPTH + 1))
    for key, sequence in grouped.items():
        ordered = sorted(sequence, key=lambda item: item.depth_k)
        if [row.depth_k for row in ordered] != expected:
            raise DataContractError(
                "incomplete depth coverage",
                _one_failure_count("incomplete_depth_coverage_sequences"),
            )
        first_empty[key] = next(
            (row.depth_k for row in ordered if row.slice_status == "EMPTY"),
            NO_EMPTY_SENTINEL,
        )

    cell_values: dict[CellKey, list[int]] = defaultdict(list)
    for (seed, intensity, _K, _start), value in first_empty.items():
        cell_values[(seed, intensity)].append(value)
    h_hat = {cell: lower_median(values) for cell, values in cell_values.items()}
    return DerivedHhat(first_empty, h_hat)


def _cell_items(
    values: Mapping[CellKey, int] | Iterable[tuple[CellKey, int]],
) -> list[tuple[CellKey, int]]:
    return list(values.items()) if isinstance(values, Mapping) else list(values)


def build_reference_baselines(
    reference_h_hat: Mapping[CellKey, int] | Iterable[tuple[CellKey, int]],
    evaluation_cells: Iterable[CellKey],
) -> dict[str, dict[CellKey, int]]:
    items = _cell_items(reference_h_hat)
    keys = [cell for cell, _value in items]
    duplicate_count = len(keys) - len(set(keys))
    if duplicate_count:
        raise DataContractError(
            "duplicate derived PR006 cell",
            _one_failure_count("duplicate_derived_pr006_cells", duplicate_count),
        )
    reference = dict(items)
    intensities = sorted({intensity for _seed, intensity in reference})
    expected_cells = {(seed, intensity) for seed in FROZEN_PR006_SEEDS for intensity in intensities}
    if (
        {seed for seed, _intensity in reference} != set(FROZEN_PR006_SEEDS)
        or len(intensities) != 3
        or len(reference) != 18
        or set(reference) != expected_cells
    ):
        missing = max(1, len(expected_cells - set(reference)))
        raise DataContractError(
            "frozen PR006 seed-intensity grid is incomplete or incompatible",
            _one_failure_count("missing_frozen_pr006_seed_intensity_cells", missing),
        )
    intensity_prediction = {
        intensity: lower_median(reference[(seed, intensity)] for seed in FROZEN_PR006_SEEDS)
        for intensity in intensities
    }
    block_prediction = lower_median(reference.values())
    cells = sorted(set(evaluation_cells))
    if not cells:
        raise DataContractError("evaluation cell set is empty")
    missing_intensities = {intensity for _seed, intensity in cells} - set(intensity_prediction)
    if missing_intensities:
        raise DataContractError(
            "evaluation intensity missing from PR006 reference",
            _one_failure_count(
                "missing_frozen_pr006_seed_intensity_cells", len(missing_intensities)
            ),
        )
    return {
        "pr006_block_h_hat": {cell: block_prediction for cell in cells},
        "pr006_intensity_h_hat": {
            cell: intensity_prediction[cell[1]] for cell in cells
        },
    }


def build_constant_baselines(evaluation_cells: Iterable[CellKey]) -> dict[str, dict[CellKey, int]]:
    cells = sorted(set(evaluation_cells))
    if not cells:
        raise DataContractError("evaluation cell set is empty")
    return {
        "constant_depth_8": {cell: 8 for cell in cells},
        "constant_depth_26": {cell: 26 for cell in cells},
        ORACLE_BASELINE_ID: {cell: 4 for cell in cells},
    }


def cell_agreement_with_H4(values: Mapping[CellKey, int]) -> float:
    if not values:
        raise DataContractError("cell agreement requires at least one cell")
    return sum(value == 4 for value in values.values()) / len(values)


def compute_primary_metrics(
    evaluation_h_hat: Mapping[CellKey, int],
    primary_baselines: Mapping[str, Mapping[CellKey, int]],
) -> PrimaryMetrics:
    if tuple(primary_baselines) != PRIMARY_BASELINE_IDS:
        raise DataContractError("primary baseline IDs or order differ from the frozen set")
    evaluation_cells = set(evaluation_h_hat)
    if any(set(predictions) != evaluation_cells for predictions in primary_baselines.values()):
        raise DataContractError("baseline cells do not match evaluation cells")
    h_agreement = cell_agreement_with_H4(evaluation_h_hat)
    agreements = {
        baseline_id: cell_agreement_with_H4(primary_baselines[baseline_id])
        for baseline_id in PRIMARY_BASELINE_IDS
    }
    maximum = max(agreements.values())
    return PrimaryMetrics(h_agreement, agreements, maximum, h_agreement - maximum)


def compute_secondary_summaries(
    evaluation_rows: Sequence[InputRow],
    evaluation_h_hat: Mapping[CellKey, int],
) -> SecondarySummaries:
    derived = derive_h_hat(evaluation_rows)
    if dict(derived.h_hat_by_cell) != dict(evaluation_h_hat):
        raise DataContractError("evaluation H_hat is inconsistent with source rows")
    by_seed: dict[int, list[int]] = defaultdict(list)
    by_intensity: dict[float, list[int]] = defaultdict(list)
    for (seed, intensity, _K, _start), value in derived.first_empty_by_sequence.items():
        by_seed[seed].append(value)
        by_intensity[intensity].append(value)
    return SecondarySummaries(
        H_hat_block=lower_median(evaluation_h_hat.values()),
        cell_fraction_H4=cell_agreement_with_H4(evaluation_h_hat),
        seed_group_medians={seed: lower_median(values) for seed, values in sorted(by_seed.items())},
        intensity_group_medians={
            intensity: lower_median(values) for intensity, values in sorted(by_intensity.items())
        },
    )


def assign_terminal_label(
    flags: TerminalFlags,
    metrics: PrimaryMetrics | None,
) -> str:
    if flags.runtime_failure:
        return "FAILED_RUNTIME"
    if flags.data_contract_failure:
        return "FAILED_DATA_CONTRACT"
    if flags.leakage_failure:
        return "FAILED_LEAKAGE_AUDIT"
    if metrics is None:
        raise ValueError("metrics are required when no failure applies")
    if metrics.max_baseline_cell_agreement_with_H4 >= metrics.h_hat_cell_agreement_with_H4:
        return "BASELINE_DOMINATED"
    if metrics.h_hat_cell_agreement_with_H4 == 1.0 and metrics.delta_agreement > 0.0:
        return "PASSED_BASELINE_AND_LEAKAGE_AUDIT"
    return "INCONCLUSIVE"


def make_cell_estimates(
    identifiers: Identifiers,
    terminal_label: str,
    evaluation_h_hat: Mapping[CellKey, int],
    primary_baselines: Mapping[str, Mapping[CellKey, int]],
    oracle_baseline: Mapping[CellKey, int],
) -> list[CellEstimate]:
    combined: dict[str, Mapping[CellKey, int]] = {"H_hat": evaluation_h_hat}
    combined.update(primary_baselines)
    combined[ORACLE_BASELINE_ID] = oracle_baseline
    if tuple(combined) != ESTIMATOR_ORDER:
        raise DataContractError("emitted estimator IDs differ from frozen order")
    return [
        CellEstimate(identifiers, seed, intensity, estimator_id, combined[estimator_id][(seed, intensity)], terminal_label)
        for seed, intensity in sorted(evaluation_h_hat)
        for estimator_id in ESTIMATOR_ORDER
    ]


def _csv_scalar(column: str, value: object) -> str:
    if value is None:
        return "null"
    if column in {"run_id", "configuration_fingerprint", "input_provenance_fingerprint"}:
        return _validate_sha256(str(value))
    if column in {"seed", "predicted_depth", "H_hat_block"}:
        if type(value) is not int:
            raise OutputContractError(f"{column} must be an integer")
        return str(value)
    if column in {
        "intensity",
        "h_hat_cell_agreement_with_H4",
        "max_baseline_cell_agreement_with_H4",
        "delta_agreement",
        "cell_fraction_H4",
    }:
        return serialize_float(float(value))
    if column in {"agrees_with_H4", "included_in_primary_max"}:
        if type(value) is not bool:
            raise OutputContractError(f"{column} must be boolean")
        return "true" if value else "false"
    if not isinstance(value, str) or not value:
        raise OutputContractError(f"{column} must be a nonempty enum")
    return value


def _summary_row(summary: AuditSummary) -> dict[str, object]:
    return {
        "record_type": "RUN_SUMMARY",
        "run_id": summary.identifiers.run_id,
        "configuration_fingerprint": summary.identifiers.configuration_fingerprint,
        "input_provenance_fingerprint": summary.identifiers.input_provenance_fingerprint,
        "seed": None,
        "intensity": None,
        "estimator_id": None,
        "estimator_role": None,
        "predicted_depth": None,
        "agrees_with_H4": None,
        "included_in_primary_max": None,
        "terminal_label": summary.terminal_label,
        "h_hat_cell_agreement_with_H4": summary.h_hat_cell_agreement_with_H4,
        "max_baseline_cell_agreement_with_H4": summary.max_baseline_cell_agreement_with_H4,
        "delta_agreement": summary.delta_agreement,
        "H_hat_block": summary.H_hat_block,
        "cell_fraction_H4": summary.cell_fraction_H4,
    }


def _cell_row(cell: CellEstimate) -> dict[str, object]:
    role = ESTIMATOR_ROLES[cell.estimator_id]
    return {
        "record_type": "CELL_ESTIMATE",
        "run_id": cell.identifiers.run_id,
        "configuration_fingerprint": cell.identifiers.configuration_fingerprint,
        "input_provenance_fingerprint": cell.identifiers.input_provenance_fingerprint,
        "seed": cell.seed,
        "intensity": cell.intensity,
        "estimator_id": cell.estimator_id,
        "estimator_role": role,
        "predicted_depth": cell.predicted_depth,
        "agrees_with_H4": cell.predicted_depth == 4,
        "included_in_primary_max": role == "PRIMARY_BASELINE",
        "terminal_label": cell.terminal_label,
        "h_hat_cell_agreement_with_H4": None,
        "max_baseline_cell_agreement_with_H4": None,
        "delta_agreement": None,
        "H_hat_block": None,
        "cell_fraction_H4": None,
    }


def render_audit_csv(summary: AuditSummary, cells: Sequence[CellEstimate]) -> bytes:
    semantic_rows = [_summary_row(summary), *(_cell_row(cell) for cell in cells)]
    output = io.StringIO(newline="")
    writer = csv.writer(
        output,
        delimiter=",",
        quotechar='"',
        doublequote=True,
        escapechar=None,
        lineterminator="\n",
        quoting=csv.QUOTE_MINIMAL,
        strict=True,
    )
    writer.writerow(CSV_COLUMNS)
    for semantic in semantic_rows:
        serialized = [_csv_scalar(column, semantic[column]) for column in CSV_COLUMNS]
        if any(value == "" for value in serialized):
            raise OutputContractError("empty CSV field")
        writer.writerow(serialized)
    data = output.getvalue().encode("utf-8")
    validate_audit_csv_bytes(data)
    return data


def _parse_int(value: str, *, nonnegative: bool = False) -> int:
    pattern = _INT_RE if nonnegative else _SIGNED_INT_RE
    if not pattern.fullmatch(value):
        raise OutputContractError("invalid INT")
    return int(value)


def validate_audit_csv_bytes(
    data: bytes,
    expected_evaluation_cells: Iterable[CellKey] | None = None,
) -> tuple[dict[str, str], list[dict[str, str]]]:
    if data.startswith(b"\xef\xbb\xbf") or not data.endswith(b"\n") or b"\r" in data:
        raise OutputContractError("invalid CSV encoding or record terminator")
    try:
        text = data.decode("utf-8")
        rows = list(csv.reader(io.StringIO(text, newline=""), strict=True))
    except (UnicodeError, csv.Error) as exc:
        raise OutputContractError("CSV is not parseable") from exc
    if not rows or tuple(rows[0]) != CSV_COLUMNS or any(not row for row in rows):
        raise OutputContractError("invalid CSV header or blank row")
    if any(len(row) != len(CSV_COLUMNS) or any(value == "" for value in row) for row in rows[1:]):
        raise OutputContractError("invalid CSV row width or empty field")
    replay = io.StringIO(newline="")
    writer = csv.writer(replay, lineterminator="\n", quoting=csv.QUOTE_MINIMAL, strict=True)
    writer.writerows(rows)
    if replay.getvalue().encode("utf-8") != data:
        raise OutputContractError("CSV quoting is not canonical")
    records = [dict(zip(CSV_COLUMNS, row, strict=True)) for row in rows[1:]]
    summaries = [row for row in records if row["record_type"] == "RUN_SUMMARY"]
    if len(summaries) != 1 or not records or records[0]["record_type"] != "RUN_SUMMARY":
        raise OutputContractError("CSV must begin with exactly one RUN_SUMMARY")
    if any(row["record_type"] not in {"RUN_SUMMARY", "CELL_ESTIMATE"} for row in records):
        raise OutputContractError("unknown CSV record type")
    summary = summaries[0]
    if summary["terminal_label"] not in TERMINAL_LABELS:
        raise OutputContractError("unknown terminal label")
    for name in ("run_id", "configuration_fingerprint", "input_provenance_fingerprint"):
        try:
            _validate_sha256(summary[name])
        except ValueError as exc:
            raise OutputContractError(f"invalid {name}") from exc
    summary_null = (
        "seed", "intensity", "estimator_id", "estimator_role", "predicted_depth",
        "agrees_with_H4", "included_in_primary_max",
    )
    if any(summary[name] != "null" for name in summary_null):
        raise OutputContractError("invalid RUN_SUMMARY null placement")
    metric_columns = (
        "h_hat_cell_agreement_with_H4", "max_baseline_cell_agreement_with_H4",
        "delta_agreement", "H_hat_block", "cell_fraction_H4",
    )
    if summary["terminal_label"] in FAILURE_LABELS:
        if any(summary[name] != "null" for name in metric_columns):
            raise OutputContractError("failure summary metrics must be null")
    else:
        if any(summary[name] == "null" for name in metric_columns):
            raise OutputContractError("non-failure summary metrics are required")
        for name in metric_columns:
            if name == "H_hat_block":
                value = _parse_int(summary[name], nonnegative=True)
                if not 1 <= value <= 26:
                    raise OutputContractError("H_hat_block outside [1,26]")
            else:
                parse_float_hex(summary[name])

    cells = records[1:]
    if summary["terminal_label"] in FAILURE_LABELS and cells:
        raise OutputContractError("failure output cannot contain cell rows")
    expected_roles = ESTIMATOR_ROLES
    parsed_sort_keys: list[tuple[int, float, int]] = []
    uniqueness: set[tuple[str, str, str]] = set()
    predictions: dict[str, dict[CellKey, int]] = {
        estimator_id: {} for estimator_id in ESTIMATOR_ORDER
    }
    for row in cells:
        if row["record_type"] != "CELL_ESTIMATE":
            raise OutputContractError("RUN_SUMMARY appears after first row")
        if any(row[name] != summary[name] for name in (
            "run_id", "configuration_fingerprint", "input_provenance_fingerprint", "terminal_label"
        )):
            raise OutputContractError("shared CSV fields differ")
        if any(row[name] != "null" for name in metric_columns):
            raise OutputContractError("cell summary columns must be null")
        seed = _parse_int(row["seed"], nonnegative=True)
        intensity = parse_float_hex(row["intensity"])
        estimator_id = row["estimator_id"]
        if estimator_id not in expected_roles or row["estimator_role"] != expected_roles[estimator_id]:
            raise OutputContractError("invalid estimator ID or role")
        predicted = _parse_int(row["predicted_depth"], nonnegative=True)
        if not 1 <= predicted <= 26:
            raise OutputContractError("predicted_depth outside [1,26]")
        agrees = row["agrees_with_H4"]
        included = row["included_in_primary_max"]
        if agrees not in {"true", "false"} or included not in {"true", "false"}:
            raise OutputContractError("invalid BOOL")
        if (agrees == "true") != (predicted == 4):
            raise OutputContractError("agrees_with_H4 is inconsistent")
        if (included == "true") != (expected_roles[estimator_id] == "PRIMARY_BASELINE"):
            raise OutputContractError("included_in_primary_max is inconsistent")
        unique = (row["seed"], row["intensity"], estimator_id)
        if unique in uniqueness:
            raise OutputContractError("duplicate CELL_ESTIMATE")
        uniqueness.add(unique)
        parsed_sort_keys.append((seed, intensity, ESTIMATOR_ORDER.index(estimator_id)))
        predictions[estimator_id][(seed, intensity)] = predicted
    if parsed_sort_keys != sorted(parsed_sort_keys):
        raise OutputContractError("CELL_ESTIMATE order is invalid")
    groups = Counter((row["seed"], row["intensity"]) for row in cells)
    if summary["terminal_label"] in NON_FAILURE_LABELS and (
        not cells or any(count != 6 for count in groups.values())
    ):
        raise OutputContractError("every evaluation cell must contain six estimators")
    if summary["terminal_label"] in NON_FAILURE_LABELS:
        if expected_evaluation_cells is not None and (
            set(predictions["H_hat"]) != set(expected_evaluation_cells)
        ):
            raise OutputContractError("CSV omits or adds an evaluation cell")
        if any(value != 8 for value in predictions["constant_depth_8"].values()):
            raise OutputContractError("constant_depth_8 predictions differ")
        if any(value != 26 for value in predictions["constant_depth_26"].values()):
            raise OutputContractError("constant_depth_26 predictions differ")
        if any(value != 4 for value in predictions[ORACLE_BASELINE_ID].values()):
            raise OutputContractError("constant_depth_4 predictions differ")
        if len(set(predictions["pr006_block_h_hat"].values())) != 1:
            raise OutputContractError("pr006_block_h_hat is not a scalar broadcast")
        intensity_predictions: dict[float, set[int]] = defaultdict(set)
        for (_seed, intensity), value in predictions["pr006_intensity_h_hat"].items():
            intensity_predictions[intensity].add(value)
        if any(len(values) != 1 for values in intensity_predictions.values()):
            raise OutputContractError("pr006_intensity_h_hat depends on evaluation seed")

        h_agreement = cell_agreement_with_H4(predictions["H_hat"])
        baseline_agreements = {
            baseline_id: cell_agreement_with_H4(predictions[baseline_id])
            for baseline_id in PRIMARY_BASELINE_IDS
        }
        maximum = max(baseline_agreements.values())
        delta = h_agreement - maximum
        h_hat_block = lower_median(predictions["H_hat"].values())
        expected_summary = {
            "h_hat_cell_agreement_with_H4": serialize_float(h_agreement),
            "max_baseline_cell_agreement_with_H4": serialize_float(maximum),
            "delta_agreement": serialize_float(delta),
            "H_hat_block": str(h_hat_block),
            "cell_fraction_H4": serialize_float(h_agreement),
        }
        if any(summary[key] != value for key, value in expected_summary.items()):
            raise OutputContractError("RUN_SUMMARY does not match CELL_ESTIMATE rows")
        expected_label = assign_terminal_label(
            TerminalFlags(),
            PrimaryMetrics(h_agreement, baseline_agreements, maximum, delta),
        )
        if summary["terminal_label"] != expected_label:
            raise OutputContractError("terminal label does not match frozen metric tree")
    return summary, cells


def _machine_value(kind: str, value: object | None) -> str:
    if value is None:
        return "null"
    return encode_scalar(kind, value)


def machine_values(
    summary: AuditSummary,
    artifact_paths: Sequence[str],
    artifact_03_sha256: str | None,
    artifact_06_sha256: str | None,
    csv_output_path: str,
    report_output_path: str,
) -> list[tuple[str, str]]:
    if len(artifact_paths) != 7:
        raise ValueError("machine inventory requires seven artifacts")
    values: list[tuple[str, str]] = [
        ("machine_schema", _machine_value("enum", "pr008-machine-readable-v1")),
        ("run_id", _machine_value("sha256", summary.identifiers.run_id)),
        ("configuration_fingerprint", _machine_value("sha256", summary.identifiers.configuration_fingerprint)),
        ("input_provenance_fingerprint", _machine_value("sha256", summary.identifiers.input_provenance_fingerprint)),
        ("publication_status", _machine_value("enum", "VALID")),
        ("terminal_label", _machine_value("enum", summary.terminal_label)),
    ]
    values.extend(
        (f"artifact_{index:02d}_path", _machine_value("path", path))
        for index, path in enumerate(artifact_paths, 1)
    )
    values.extend((
        ("artifact_03_sha256", _machine_value("sha256", artifact_03_sha256)),
        ("artifact_06_sha256", _machine_value("sha256", artifact_06_sha256)),
        ("csv_output_path", _machine_value("path", csv_output_path)),
        ("report_output_path", _machine_value("path", report_output_path)),
        ("h_hat_cell_agreement_with_H4", _machine_value("float", summary.h_hat_cell_agreement_with_H4)),
        ("max_baseline_cell_agreement_with_H4", _machine_value("float", summary.max_baseline_cell_agreement_with_H4)),
        ("delta_agreement", _machine_value("float", summary.delta_agreement)),
        ("H_hat_block", _machine_value("int", summary.H_hat_block)),
        ("cell_fraction_H4", _machine_value("float", summary.cell_fraction_H4)),
    ))
    if tuple(key for key, _value in values) != MACHINE_KEYS:
        raise AssertionError("machine key construction drifted")
    return values


def render_report(
    summary: AuditSummary,
    artifact_paths: Sequence[str],
    artifact_03_sha256: str | None,
    artifact_06_sha256: str | None,
    csv_output_path: str,
    report_output_path: str,
    failure_counts: Mapping[str, int],
    secondary: SecondarySummaries | None,
) -> bytes:
    counts = [f"- `{key}`: {failure_counts[key]}" for key in FAILURE_COUNT_KEYS]
    seed_lines = [] if secondary is None else [
        f"- `seed_group_median({seed})`: {value}"
        for seed, value in secondary.seed_group_medians.items()
    ]
    intensity_lines = [] if secondary is None else [
        f"- `intensity_group_median({intensity!r})`: {value}"
        for intensity, value in secondary.intensity_group_medians.items()
    ]
    sections = [
        "# PR008 H_hat Baseline and Leakage Audit Report\n",
        f"{REPORT_HEADINGS[0]}\n\n" + "\n".join(f"- `{path}`" for path in artifact_paths) + "\n",
        f"{REPORT_HEADINGS[1]}\n\n" + "\n".join(counts) + "\n",
        f"{REPORT_HEADINGS[2]}\n\nAccess is restricted to the frozen artifact inventory; calculation columns are `seed`, `intensity`, `K`, `start_id`, `depth_k`, and `slice_status`.\n",
        f"{REPORT_HEADINGS[3]}\n\n" + "\n".join(f"- `{item}`" for item in PRIMARY_BASELINE_IDS) + "\n",
        f"{REPORT_HEADINGS[4]}\n\nThe normative values are serialized in the machine-readable block.\n",
        f"{REPORT_HEADINGS[5]}\n\n" + ("Not applicable for a failed terminal state." if secondary is None else "\n".join(seed_lines + intensity_lines)) + "\n",
        f"{REPORT_HEADINGS[6]}\n\n`constant_depth_4` is emitted only with this role and is excluded from primary logic.\n",
        f"{REPORT_HEADINGS[7]}\n\n`{summary.terminal_label}`\n",
        f"{REPORT_HEADINGS[8]}\n\n"
        "PR008 does not claim horizon reconstruction, radial localization, K-invariance, "
        "a physical barrier, Schwarzschild 3+1D reconstruction, robustness over patch "
        "size, `M`, or `MAX_STARTS`, or superiority over baselines not preregistered "
        "before audit execution.\n",
    ]
    block = [MACHINE_BEGIN, *(f"{key}={value}" for key, value in machine_values(
        summary, artifact_paths, artifact_03_sha256, artifact_06_sha256,
        csv_output_path, report_output_path,
    )), MACHINE_END]
    text = "\n".join(section.rstrip("\n") for section in sections) + "\n\n" + "\n".join(block) + "\n"
    return text.encode("utf-8")


def _parse_machine_block(data: bytes) -> tuple[str, dict[str, str]]:
    if data.startswith(b"\xef\xbb\xbf") or not data.endswith(b"\n") or b"\r" in data:
        raise OutputContractError("invalid report encoding or record terminator")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise OutputContractError("report is not UTF-8") from exc
    lines = text.splitlines()
    if lines.count(MACHINE_BEGIN) != 1 or lines.count(MACHINE_END) != 1:
        raise OutputContractError("machine block delimiters are missing or duplicated")
    begin = lines.index(MACHINE_BEGIN)
    end = lines.index(MACHINE_END)
    if end <= begin:
        raise OutputContractError("machine block delimiters are out of order")
    records = lines[begin + 1:end]
    if len(records) != len(MACHINE_KEYS) or any(not record or record.count("=") != 1 for record in records):
        raise OutputContractError("machine block record count or syntax is invalid")
    pairs = [record.split("=", 1) for record in records]
    if tuple(pair[0] for pair in pairs) != MACHINE_KEYS:
        raise OutputContractError("machine keys are missing, duplicated, or reordered")
    return text, {key: value for key, value in pairs}


def validate_report_bytes(
    data: bytes,
    expected_artifact_paths: Sequence[str],
    expected_output_paths: tuple[str, str],
    expected_configuration_fingerprint: str,
) -> dict[str, str]:
    text, values = _parse_machine_block(data)
    report_section_lines = tuple(
        line for line in text.splitlines() if line.startswith("## ")
    )
    positions = [text.find(heading) for heading in REPORT_HEADINGS]
    if (
        report_section_lines != REPORT_HEADINGS
        or any(text.count(heading) != 1 for heading in REPORT_HEADINGS)
        or any(position < 0 for position in positions)
        or positions != sorted(positions)
    ):
        raise OutputContractError("report sections are missing or reordered")
    if values["machine_schema"] != "pr008-machine-readable-v1" or values["publication_status"] != "VALID":
        raise OutputContractError("invalid machine schema or publication status")
    for key in ("run_id", "configuration_fingerprint", "input_provenance_fingerprint"):
        try:
            _validate_sha256(values[key])
        except ValueError as exc:
            raise OutputContractError(f"invalid machine {key}") from exc
    if values["configuration_fingerprint"] != expected_configuration_fingerprint:
        raise OutputContractError("configuration fingerprint differs")
    terminal = values["terminal_label"]
    if terminal not in TERMINAL_LABELS:
        raise OutputContractError("invalid machine terminal label")
    decoded_paths = []
    for index in range(1, 8):
        decoded = decode_string(values[f"artifact_{index:02d}_path"])
        normalize_path(decoded)
        decoded_paths.append(decoded)
    if tuple(decoded_paths) != tuple(expected_artifact_paths):
        raise OutputContractError("machine artifact inventory differs")
    observed_hashes: list[str | None] = []
    for key in ("artifact_03_sha256", "artifact_06_sha256"):
        raw = values[key]
        if raw == "null":
            observed_hashes.append(None)
        else:
            try:
                observed_hashes.append(_validate_sha256(raw))
            except ValueError as exc:
                raise OutputContractError(f"invalid {key}") from exc
    output_paths = (
        decode_string(values["csv_output_path"]),
        decode_string(values["report_output_path"]),
    )
    if output_paths != expected_output_paths:
        raise OutputContractError("machine output paths differ")
    for path in output_paths:
        normalize_path(path)
    metric_keys = MACHINE_KEYS[17:]
    if terminal in FAILURE_LABELS:
        if any(values[key] != "null" for key in metric_keys):
            raise OutputContractError("failed machine summary must use null")
    else:
        if any(values[key] == "null" for key in metric_keys):
            raise OutputContractError("non-failure machine summary is incomplete")
        for key in metric_keys:
            if key == "H_hat_block":
                parsed = _parse_int(values[key], nonnegative=True)
                if not 1 <= parsed <= 26:
                    raise OutputContractError("machine H_hat_block outside [1,26]")
            else:
                parse_float_hex(values[key])
    provenance = input_provenance_fingerprint(decoded_paths, *observed_hashes)
    if provenance != values["input_provenance_fingerprint"]:
        raise OutputContractError("input provenance fingerprint cannot be recalculated")
    run_id = make_run_id(expected_configuration_fingerprint, provenance)
    if run_id != values["run_id"]:
        raise OutputContractError("run_id cannot be recalculated")
    return values


def validate_output_pair_bytes(
    csv_data: bytes,
    report_data: bytes,
    expected_artifact_paths: Sequence[str],
    expected_output_paths: tuple[str, str],
    expected_configuration_fingerprint: str,
    expected_evaluation_cells: Iterable[CellKey] | None = None,
) -> None:
    summary, _cells = validate_audit_csv_bytes(csv_data, expected_evaluation_cells)
    machine = validate_report_bytes(
        report_data,
        expected_artifact_paths,
        expected_output_paths,
        expected_configuration_fingerprint,
    )
    shared = (
        "run_id",
        "configuration_fingerprint",
        "input_provenance_fingerprint",
        "terminal_label",
        "h_hat_cell_agreement_with_H4",
        "max_baseline_cell_agreement_with_H4",
        "delta_agreement",
        "H_hat_block",
        "cell_fraction_H4",
    )
    if any(summary[key] != machine[key] for key in shared):
        raise OutputContractError("CSV and report shared fields differ")


@dataclass(frozen=True)
class PublicationPaths:
    csv_final: Path
    report_final: Path
    csv_temp: Path
    report_temp: Path


@dataclass(frozen=True)
class PreflightResult:
    diagnosis: str
    production_permitted: bool


def _unlink_if_present(path: Path) -> None:
    try:
        path.unlink()
    except FileNotFoundError:
        pass


def _cleanup_all(paths: PublicationPaths) -> None:
    for path in (paths.csv_temp, paths.report_temp, paths.csv_final, paths.report_final):
        _unlink_if_present(path)


def preflight_publication(
    paths: PublicationPaths,
    validate_pair_paths: Callable[[Path, Path], None],
) -> PreflightResult:
    _unlink_if_present(paths.csv_temp)
    _unlink_if_present(paths.report_temp)
    csv_exists = paths.csv_final.exists()
    report_exists = paths.report_final.exists()
    if csv_exists != report_exists:
        _unlink_if_present(paths.csv_final)
        _unlink_if_present(paths.report_final)
        if any(path.exists() for path in (paths.csv_temp, paths.report_temp, paths.csv_final, paths.report_final)):
            raise PublicationError("partial output cleanup failed")
        return PreflightResult("PARTIALLY_PUBLISHED", True)
    if csv_exists and report_exists:
        try:
            validate_pair_paths(paths.csv_final, paths.report_final)
        except (OSError, OutputContractError, DataContractError, ArtifactReadError):
            _unlink_if_present(paths.csv_final)
            _unlink_if_present(paths.report_final)
            if paths.csv_final.exists() or paths.report_final.exists():
                raise PublicationError("invalid output cleanup failed")
            return PreflightResult("FAILED_OUTPUT_CONTRACT", True)
        return PreflightResult("VALID", False)
    if any(path.exists() for path in (paths.csv_temp, paths.report_temp, paths.csv_final, paths.report_final)):
        raise PublicationError("preflight did not establish an empty state")
    return PreflightResult("CLEAN", True)


def _write_validated_temp(path: Path, data: bytes, validator: Callable[[bytes], object]) -> None:
    if not path.parent.is_dir():
        raise PublicationError("temporary parent directory does not exist")
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    validator(path.read_bytes())


def publish_output_pair(
    csv_data: bytes,
    report_data: bytes,
    paths: PublicationPaths,
    validate_csv: Callable[[bytes], object],
    validate_report: Callable[[bytes], object],
    validate_pair: Callable[[bytes, bytes], None],
    after_csv_publish: Callable[[], None] | None = None,
) -> PreflightResult:
    def validate_pair_paths(csv_path: Path, report_path: Path) -> None:
        validate_pair(csv_path.read_bytes(), report_path.read_bytes())

    preflight = preflight_publication(paths, validate_pair_paths)
    if not preflight.production_permitted:
        raise PublicationError("VALID_OUTPUT_SET_EXISTS")
    try:
        _write_validated_temp(paths.csv_temp, csv_data, validate_csv)
        os.replace(paths.csv_temp, paths.csv_final)
        if after_csv_publish is not None:
            after_csv_publish()
        _write_validated_temp(paths.report_temp, report_data, validate_report)
        os.replace(paths.report_temp, paths.report_final)
        if paths.csv_temp.exists() or paths.report_temp.exists():
            raise OutputContractError("temporary remains after publication")
        validate_pair_paths(paths.csv_final, paths.report_final)
        return preflight
    except BaseException:
        _cleanup_all(paths)
        if any(path.exists() for path in (paths.csv_temp, paths.report_temp, paths.csv_final, paths.report_final)):
            raise PublicationError("publication rollback failed")
        raise


def _configuration_digest(root: Path) -> str:
    return configuration_fingerprint(
        PREREGISTRATION_PATH,
        sha256_file(root / PREREGISTRATION_PATH),
        IMPLEMENTATION_PLAN_PATH,
        sha256_file(root / IMPLEMENTATION_PLAN_PATH),
        PRODUCTION_COMMAND,
    )


def _identifiers(
    configuration_digest: str,
    artifact_03_sha256: str | None,
    artifact_06_sha256: str | None,
) -> Identifiers:
    provenance = input_provenance_fingerprint(
        INPUT_ARTIFACTS, artifact_03_sha256, artifact_06_sha256
    )
    return Identifiers(make_run_id(configuration_digest, provenance), configuration_digest, provenance)


def _production_validators(
    configuration_digest: str,
    expected_evaluation_cells: Iterable[CellKey] | None = None,
):
    frozen_expected_cells = (
        None if expected_evaluation_cells is None else frozenset(expected_evaluation_cells)
    )

    def validate_csv(data: bytes) -> object:
        return validate_audit_csv_bytes(data, frozen_expected_cells)

    def validate_report(data: bytes) -> object:
        return validate_report_bytes(
            data, INPUT_ARTIFACTS, (CSV_FINAL_PATH, REPORT_FINAL_PATH), configuration_digest
        )

    def validate_pair(csv_data: bytes, report_data: bytes) -> None:
        expected_cells = frozen_expected_cells
        if expected_cells is None:
            summary, _cells = validate_audit_csv_bytes(csv_data)
            if summary["terminal_label"] in NON_FAILURE_LABELS:
                validate_artifacts(REPO_ROOT, INPUT_ARTIFACTS, FROZEN_INPUT_HASHES)
                evaluation_rows = read_and_validate_csv(
                    REPO_ROOT / EVALUATION_CSV_PATH, "evaluation"
                )
                expected_cells = frozenset(derive_h_hat(evaluation_rows).h_hat_by_cell)
        validate_output_pair_bytes(
            csv_data, report_data, INPUT_ARTIFACTS,
            (CSV_FINAL_PATH, REPORT_FINAL_PATH), configuration_digest, expected_cells,
        )

    return validate_csv, validate_report, validate_pair


def _failure_summary(identifiers: Identifiers, label: str) -> AuditSummary:
    return AuditSummary(identifiers, label, None, None, None, None, None)


def _render_and_publish_production(
    summary: AuditSummary,
    cells: Sequence[CellEstimate],
    observed_03: str | None,
    observed_06: str | None,
    counts: Mapping[str, int],
    secondary: SecondarySummaries | None,
    expected_evaluation_cells: Iterable[CellKey] | None = None,
) -> None:
    csv_data = render_audit_csv(summary, cells)
    report_data = render_report(
        summary, INPUT_ARTIFACTS, observed_03, observed_06,
        CSV_FINAL_PATH, REPORT_FINAL_PATH, counts, secondary,
    )
    validators = _production_validators(
        summary.identifiers.configuration_fingerprint, expected_evaluation_cells
    )
    publish_output_pair(
        csv_data,
        report_data,
        PublicationPaths(
            REPO_ROOT / CSV_FINAL_PATH,
            REPO_ROOT / REPORT_FINAL_PATH,
            REPO_ROOT / CSV_TEMP_PATH,
            REPO_ROOT / REPORT_TEMP_PATH,
        ),
        *validators,
    )


def run_production() -> int:
    """Execute the fixed production audit. Authorization is external to this function."""
    configuration_digest = _configuration_digest(REPO_ROOT)
    validators = _production_validators(configuration_digest)
    publication_paths = PublicationPaths(
        REPO_ROOT / CSV_FINAL_PATH,
        REPO_ROOT / REPORT_FINAL_PATH,
        REPO_ROOT / CSV_TEMP_PATH,
        REPO_ROOT / REPORT_TEMP_PATH,
    )
    preflight = preflight_publication(
        publication_paths,
        lambda csv_path, report_path: validators[2](csv_path.read_bytes(), report_path.read_bytes()),
    )
    if not preflight.production_permitted:
        raise PublicationError("VALID_OUTPUT_SET_EXISTS")

    observed_03: str | None = None
    observed_06: str | None = None
    counts = empty_failure_counts()
    try:
        artifact_validation = validate_artifacts(REPO_ROOT, INPUT_ARTIFACTS, FROZEN_INPUT_HASHES)
        observed_03 = artifact_validation.observed_hashes[REFERENCE_CSV_PATH]
        observed_06 = artifact_validation.observed_hashes[EVALUATION_CSV_PATH]
        reference_rows = read_and_validate_csv(REPO_ROOT / REFERENCE_CSV_PATH, "reference")
        evaluation_rows = read_and_validate_csv(REPO_ROOT / EVALUATION_CSV_PATH, "evaluation")
        reference = derive_h_hat(reference_rows)
        evaluation = derive_h_hat(evaluation_rows)
        empirical = build_reference_baselines(reference.h_hat_by_cell, evaluation.h_hat_by_cell)
        constants = build_constant_baselines(evaluation.h_hat_by_cell)
        primary = {
            "constant_depth_8": constants["constant_depth_8"],
            "constant_depth_26": constants["constant_depth_26"],
            "pr006_block_h_hat": empirical["pr006_block_h_hat"],
            "pr006_intensity_h_hat": empirical["pr006_intensity_h_hat"],
        }
        metrics = compute_primary_metrics(evaluation.h_hat_by_cell, primary)
        secondary = compute_secondary_summaries(evaluation_rows, evaluation.h_hat_by_cell)
        label = assign_terminal_label(TerminalFlags(), metrics)
        identifiers = _identifiers(configuration_digest, observed_03, observed_06)
        summary = AuditSummary(
            identifiers, label,
            metrics.h_hat_cell_agreement_with_H4,
            metrics.max_baseline_cell_agreement_with_H4,
            metrics.delta_agreement,
            secondary.H_hat_block,
            secondary.cell_fraction_H4,
        )
        cells = make_cell_estimates(
            identifiers, label, evaluation.h_hat_by_cell, primary, constants[ORACLE_BASELINE_ID]
        )
        _render_and_publish_production(
            summary, cells, observed_03, observed_06, counts, secondary,
            evaluation.h_hat_by_cell,
        )
        return 0
    except DataContractError as exc:
        counts.update(exc.counts)
        observed = getattr(exc, "observed_hashes", {})
        observed_03 = observed.get(REFERENCE_CSV_PATH, observed_03)
        observed_06 = observed.get(EVALUATION_CSV_PATH, observed_06)
        identifiers = _identifiers(configuration_digest, observed_03, observed_06)
        _render_and_publish_production(
            _failure_summary(identifiers, "FAILED_DATA_CONTRACT"),
            [], observed_03, observed_06, counts, None,
        )
        return 0
    except ArtifactReadError as exc:
        observed = getattr(exc, "observed_hashes", {})
        observed_03 = observed.get(REFERENCE_CSV_PATH, observed_03)
        observed_06 = observed.get(EVALUATION_CSV_PATH, observed_06)
        identifiers = _identifiers(configuration_digest, observed_03, observed_06)
        _render_and_publish_production(
            _failure_summary(identifiers, "FAILED_RUNTIME"),
            [], observed_03, observed_06, counts, None,
        )
        return 1
    except (PublicationError, OutputContractError):
        raise
    except Exception:
        identifiers = _identifiers(configuration_digest, observed_03, observed_06)
        _render_and_publish_production(
            _failure_summary(identifiers, "FAILED_RUNTIME"),
            [], observed_03, observed_06, counts, None,
        )
        return 1


def main(argv: Sequence[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    if arguments:
        print("PR008 accepts no command-line arguments", file=sys.stderr)
        return 2
    try:
        return run_production()
    except BaseException as exc:
        print(f"PR008 publication/runtime failure: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
