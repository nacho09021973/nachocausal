"""Standalone validator and mechanical evaluator for PR010 development coverage."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
from typing import Sequence


_ROOT = Path(__file__).resolve().parent.parent

DEVELOPMENT_SEEDS = tuple(range(1_101_000, 1_101_024))
SPACETIME_KINDS = ("BH", "MINK")
TRANSITION_DEPTHS = (3, 4, 5)
MAX_STARTS = 40
MIN_SUPPORTED_SEEDS_PER_CELL = 22
EXPECTED_ROW_COUNT = 144

CSV_FIELDS = (
    "seed",
    "spacetime_kind",
    "depth_k",
    "n_emitted_starts",
    "n_transition_evaluable_starts",
    "seed_depth_supported",
)

REPORT_DIR = _ROOT / "data" / "reports"
CSV_PATH = REPORT_DIR / "pr010_reference_depth_coverage_development.csv"
SIDECAR_PATH = REPORT_DIR / "pr010_reference_depth_coverage_development.sha256"
CSV_TMP_PATH = REPORT_DIR / "pr010_reference_depth_coverage_development.csv.tmp"
SIDECAR_TMP_PATH = REPORT_DIR / "pr010_reference_depth_coverage_development.sha256.tmp"

PASS_TERMINAL = "PASS_DEVELOPMENT_COVERAGE"
INFEASIBLE_TERMINAL = "PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE"
RUNTIME_TERMINAL = "PR010_FAILED_RUNTIME"
DATA_CONTRACT_TERMINAL = "PR010_FAILED_DATA_CONTRACT"
PREFIX = "PR010_DEVELOPMENT_TERMINAL="


class DataContractError(ValueError):
    """The final PR010 artifact pair violates its frozen contract."""


class RuntimeFailure(RuntimeError):
    """The required final artifact pair could not be read."""


def _parse_unsigned(value: str, field: str) -> int:
    if not value.isascii() or not value.isdecimal():
        raise DataContractError(f"{field} is not unsigned decimal")
    parsed = int(value)
    if str(parsed) != value:
        raise DataContractError(f"{field} is not canonical unsigned decimal")
    return parsed


def _expected_keys() -> list[tuple[int, str, int]]:
    return [
        (seed, kind, depth)
        for seed in DEVELOPMENT_SEEDS
        for kind in SPACETIME_KINDS
        for depth in TRANSITION_DEPTHS
    ]


def validate_csv_bytes(data: bytes) -> list[dict[str, int | str]]:
    if not data.endswith(b"\n") or b"\r" in data:
        raise DataContractError("CSV line endings are not canonical")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise DataContractError("CSV is not UTF-8") from exc
    lines = text.splitlines()
    if not lines or lines[0] != ",".join(CSV_FIELDS):
        raise DataContractError("CSV header drift")
    if len(lines) != EXPECTED_ROW_COUNT + 1:
        raise DataContractError("CSV row count drift")
    expected_keys = _expected_keys()
    seen: set[tuple[int, str, int]] = set()
    rows: list[dict[str, int | str]] = []
    for index, line in enumerate(lines[1:]):
        values = line.split(",")
        if len(values) != len(CSV_FIELDS) or any(value == "" for value in values):
            raise DataContractError("CSV row width drift")
        seed = _parse_unsigned(values[0], "seed")
        kind = values[1]
        depth = _parse_unsigned(values[2], "depth_k")
        emitted = _parse_unsigned(values[3], "n_emitted_starts")
        evaluable = _parse_unsigned(
            values[4], "n_transition_evaluable_starts"
        )
        supported = _parse_unsigned(values[5], "seed_depth_supported")
        key = (seed, kind, depth)
        if key in seen:
            raise DataContractError("duplicate primary key")
        seen.add(key)
        if key != expected_keys[index]:
            raise DataContractError("CSV key set or row order drift")
        if emitted > MAX_STARTS or evaluable > emitted:
            raise DataContractError("CSV count domain drift")
        if supported not in (0, 1) or supported != int(evaluable >= 5):
            raise DataContractError("support predicate drift")
        rows.append(
            {
                "seed": seed,
                "spacetime_kind": kind,
                "depth_k": depth,
                "n_emitted_starts": emitted,
                "n_transition_evaluable_starts": evaluable,
                "seed_depth_supported": supported,
            }
        )
    if seen != set(expected_keys):
        raise DataContractError("CSV key set drift")
    canonical_lines = [",".join(CSV_FIELDS)]
    canonical_lines.extend(
        ",".join(str(row[field]) for field in CSV_FIELDS) for row in rows
    )
    canonical = ("\n".join(canonical_lines) + "\n").encode("utf-8")
    if canonical != data:
        raise DataContractError("CSV serialization is not canonical")
    return rows


def _validate_artifact_presence() -> None:
    finals = (CSV_PATH.exists(), SIDECAR_PATH.exists())
    temporaries = (CSV_TMP_PATH.exists(), SIDECAR_TMP_PATH.exists())
    if any(temporaries) or finals.count(True) == 1:
        raise DataContractError("incomplete or temporary artifact set")
    if not all(finals):
        raise RuntimeFailure("required final artifact pair is absent")


def load_validated_artifact() -> list[dict[str, int | str]]:
    _validate_artifact_presence()
    try:
        csv_data = CSV_PATH.read_bytes()
        sidecar_data = SIDECAR_PATH.read_bytes()
    except OSError as exc:
        raise RuntimeFailure("required final artifact pair is unreadable") from exc
    expected_sidecar = (
        f"{hashlib.sha256(csv_data).hexdigest()}  {CSV_PATH.name}\n".encode("ascii")
    )
    if sidecar_data != expected_sidecar:
        raise DataContractError("sidecar syntax, basename, or digest mismatch")
    return validate_csv_bytes(csv_data)


def evaluate_rows(rows: Sequence[dict[str, int | str]]) -> str:
    if len(rows) != EXPECTED_ROW_COUNT:
        raise DataContractError("evaluator received an incomplete row set")
    support = {
        (kind, depth): 0
        for kind in SPACETIME_KINDS
        for depth in TRANSITION_DEPTHS
    }
    keys: set[tuple[int, str, int]] = set()
    for row in rows:
        key = (
            int(row["seed"]),
            str(row["spacetime_kind"]),
            int(row["depth_k"]),
        )
        if key in keys or key not in set(_expected_keys()):
            raise DataContractError("evaluator row key drift")
        keys.add(key)
        supported = int(row["seed_depth_supported"])
        if supported not in (0, 1):
            raise DataContractError("evaluator support state drift")
        support[(key[1], key[2])] += supported
    if keys != set(_expected_keys()):
        raise DataContractError("evaluator key set drift")
    if all(value >= MIN_SUPPORTED_SEEDS_PER_CELL for value in support.values()):
        return PASS_TERMINAL
    return INFEASIBLE_TERMINAL


def main(argv: Sequence[str] | None = None) -> int:
    arguments = tuple(sys.argv[1:] if argv is None else argv)
    try:
        if arguments:
            raise DataContractError("arguments are forbidden")
        terminal = evaluate_rows(load_validated_artifact())
    except DataContractError:
        print(f"{PREFIX}{DATA_CONTRACT_TERMINAL}", file=sys.stderr)
        return 1
    except BaseException:
        print(f"{PREFIX}{RUNTIME_TERMINAL}", file=sys.stderr)
        return 1
    print(f"{PREFIX}{terminal}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
