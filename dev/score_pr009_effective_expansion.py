"""Frozen scorer for finalized PR009 runner artifacts.

The scorer is geometry-aware by design.  It never invokes the generator and it
never writes or modifies a runner artifact.  Pre-scoring failures refuse to
publish; scientific terminals publish the scored CSV and report as one pair.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import io
import json
import math
from pathlib import Path
import sys
from typing import Mapping, Sequence


_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent
sys.path.insert(0, str(_ROOT))
sys.path.insert(0, str(_HERE))

from nachocausal import thresholds  # noqa: E402
from dev import run_pr009_effective_expansion as runner  # noqa: E402
from dev.pr009_effective_expansion_core import (  # noqa: E402
    ContractError as CoreContractError,
    contrast,
    lower_median,
    stratified_permutation_pvalue,
)


SCORED = runner.REPORT_DIR / (
    "pr009_ladder_ensemble_effective_expansion_scored.csv"
)
REPORT = runner.REPORT_DIR / (
    "PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_REPORT.md"
)
SCORED_FIELDS = runner.ORDER_FIELDS + runner.TRUTH_FIELDS[-3:]
SCIENTIFIC_LABELS = {
    "INCONCLUSIVE_COVERAGE",
    "KILLED_GENERIC_OR_BASELINE_SIGNAL",
    "KILLED_NO_SIGNED_EXPANSION",
    "SURVIVED_CHEAP_KILL_TEST",
}
FORBIDDEN_ORDER_FIELDS = {
    "coordinate",
    "coordinates",
    "radius",
    "r_mid",
    "truth_r_mid",
    "truth_zone",
    "distance_to_horizon_over_ell",
    "horizon",
    "shell",
    "straddles_horizon",
    "path_geometry",
    "relphi",
}

MACHINE_BEGIN = "BEGIN_PR009_MACHINE_READABLE_V1"
MACHINE_END = "END_PR009_MACHINE_READABLE_V1"
MACHINE_KEYS = (
    "machine_schema",
    "terminal_label",
    "configuration_fingerprint",
    "reference_order_only_sha256",
    "evaluation_order_only_sha256",
    "evaluation_truth_sha256",
    "canonical_order_only_sha256",
    "bh_theta_contrast",
    "mink_theta_contrast",
    "bh_survivor_contrast",
    "bh_permutation_pvalue",
    "mink_permutation_pvalue",
    "n_positive_bh_seed_contrasts",
    "bh_interior_lower_median",
    "bh_exterior_lower_median",
    "bh_interior_n",
    "bh_exterior_n",
    "mink_interior_n",
    "mink_exterior_n",
    "bh_complete_zone_seeds",
    "mink_complete_zone_seeds",
)


class RuntimeInputError(RuntimeError):
    """Readable production inputs or publication were unavailable."""


class LeakageAuditError(ValueError):
    """The order/truth isolation boundary was violated."""


@dataclass(frozen=True)
class Observation:
    seed: int
    spacetime_kind: str
    zone: str
    theta_residual: float
    survivor_growth_baseline: float


@dataclass(frozen=True)
class Coverage:
    complete_seed_kind_cells: bool
    reference_depths_valid: bool
    cell_counts: Mapping[tuple[str, str], int]
    complete_zone_seeds: Mapping[str, tuple[int, ...]]

    @property
    def passes(self) -> bool:
        required_cells = (
            ("BH", "INTERIOR"),
            ("BH", "EXTERIOR"),
            ("MINK", "INTERIOR"),
            ("MINK", "EXTERIOR"),
        )
        return (
            self.complete_seed_kind_cells
            and self.reference_depths_valid
            and all(self.cell_counts.get(cell, 0) >= 30 for cell in required_cells)
            and all(
                len(self.complete_zone_seeds.get(kind, ())) >= 4
                for kind in runner.SPACETIME_KINDS
            )
        )


@dataclass(frozen=True)
class Metrics:
    bh_theta_contrast: float | None
    mink_theta_contrast: float | None
    bh_survivor_contrast: float | None
    bh_permutation_pvalue: float | None
    mink_permutation_pvalue: float | None
    positive_bh_seed_contrasts: int
    bh_seed_contrasts: Mapping[int, float | None]
    bh_interior_lower_median: float | None
    bh_exterior_lower_median: float | None
    bh_theta_equals_survivor_everywhere: bool


@dataclass(frozen=True)
class InputArtifacts:
    reference: bytes
    evaluation: bytes
    truth: bytes
    canonical: bytes
    reference_rows: tuple[dict[str, str], ...]
    evaluation_rows: tuple[dict[str, str], ...]
    truth_rows: tuple[dict[str, str], ...]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def configuration_fingerprint() -> str:
    payload = {
        "reference_seeds": runner.REFERENCE_SEEDS,
        "evaluation_seeds": runner.EVALUATION_SEEDS,
        "spacetime_kinds": runner.SPACETIME_KINDS,
        "intensity": runner.INTENSITY,
        "t_edge": runner.T_EDGE,
        "M": runner.M,
        "K": runner.K,
        "max_depth": runner.MAX_DEPTH,
        "max_starts": runner.MAX_STARTS,
        "tie_rank_master_seed": runner.TIE_RANK_MASTER_SEED,
        "min_reference_per_depth": runner.MIN_REFERENCE_PER_DEPTH,
        "permutation_seed": 9009,
        "max_exact_permutations": 100_000,
        "monte_carlo_permutations": 100_000,
        "cell_minimum": 30,
        "complete_zone_seed_minimum": 4,
        "positive_bh_seed_minimum": 5,
        "bh_pvalue_maximum": 0.01,
        "mink_generic_pvalue_maximum": 0.10,
        "order_fields": runner.ORDER_FIELDS,
        "truth_fields": runner.TRUTH_FIELDS,
        "scored_fields": SCORED_FIELDS,
    }
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return sha256(encoded)


def _read(path: Path) -> bytes:
    try:
        return path.read_bytes()
    except OSError as exc:
        raise RuntimeInputError(f"unreadable input: {path.name}") from exc


def _header_fields(data: bytes) -> tuple[str, ...]:
    try:
        first_line = data.split(b"\n", 1)[0].decode("utf-8")
        import csv

        return tuple(next(csv.reader(io.StringIO(first_line), strict=True)))
    except (UnicodeDecodeError, StopIteration, csv.Error) as exc:
        raise runner.DataContractError("malformed CSV header") from exc


def leakage_prescan(data: bytes) -> None:
    header = _header_fields(data)
    if any(field in FORBIDDEN_ORDER_FIELDS for field in header):
        raise LeakageAuditError("forbidden geometric field in order-only artifact")


def _key(row: Mapping[str, str]) -> tuple[str, ...]:
    return tuple(row[field] for field in runner.PRIMARY_KEY)


def _validate_sequence_depths(rows: Sequence[Mapping[str, str]]) -> None:
    grouped: dict[tuple[str, ...], list[int]] = {}
    for row in rows:
        sequence = tuple(row[field] for field in runner.PRIMARY_KEY[:-1])
        grouped.setdefault(sequence, []).append(int(row["depth_k"]))
    expected = list(range(1, runner.MAX_DEPTH + 1))
    if any(depths != expected for depths in grouped.values()):
        raise runner.DataContractError("incomplete or reordered depth sequence")


def _validate_seed_membership(
    rows: Sequence[Mapping[str, str]], block: str
) -> None:
    expected = set(
        runner.REFERENCE_SEEDS if block == "REFERENCE" else runner.EVALUATION_SEEDS
    )
    observed = {int(row["seed"]) for row in rows}
    if not observed <= expected:
        raise runner.DataContractError("seed outside frozen block")


def _validate_truth_values(rows: Sequence[Mapping[str, str]]) -> None:
    ell = thresholds.ell(runner.INTENSITY)
    for row in rows:
        if row["truth_zone"] == "NA":
            continue
        r_mid = float(row["truth_r_mid"])
        distance = float(row["distance_to_horizon_over_ell"])
        expected_distance = abs(r_mid - thresholds.R_S) / ell
        if distance != expected_distance:
            raise runner.DataContractError("truth distance does not match r_mid")
        if r_mid <= thresholds.R_S - 2.0 * ell:
            expected_zone = "INTERIOR"
        elif r_mid >= thresholds.R_S + 2.0 * ell:
            expected_zone = "EXTERIOR"
        else:
            expected_zone = "GUARD"
        if row["truth_zone"] != expected_zone:
            raise runner.DataContractError("truth zone does not match r_mid")


def load_and_validate_inputs() -> InputArtifacts:
    reference = _read(runner.REFERENCE_ORDER_ONLY)
    sidecar = _read(runner.REFERENCE_SHA256)
    evaluation = _read(runner.EVALUATION_ORDER_ONLY)
    truth = _read(runner.EVALUATION_TRUTH)
    canonical = _read(runner.CANONICAL_ORDER_ONLY)

    leakage_prescan(reference)
    leakage_prescan(evaluation)
    leakage_prescan(canonical)
    expected_sidecar = (
        f"{sha256(reference)}  {runner.REFERENCE_ORDER_ONLY.name}\n".encode("ascii")
    )
    if sidecar != expected_sidecar:
        raise runner.DataContractError("reference SHA-256 sidecar mismatch")

    reference_rows = runner.validate_order_csv_bytes(reference, {"REFERENCE"})
    evaluation_rows = runner.validate_order_csv_bytes(evaluation, {"EVALUATION"})
    canonical_rows = runner.validate_order_csv_bytes(
        canonical, {"REFERENCE", "EVALUATION"}
    )
    truth_rows = runner.validate_truth_csv_bytes(truth)
    if canonical != runner.combine_order_csv(reference, evaluation):
        raise runner.DataContractError("canonical artifact is not exact concatenation")
    if len(canonical_rows) != len(reference_rows) + len(evaluation_rows):
        raise runner.DataContractError("canonical row count mismatch")

    _validate_sequence_depths(reference_rows)
    _validate_sequence_depths(evaluation_rows)
    _validate_seed_membership(reference_rows, "REFERENCE")
    _validate_seed_membership(evaluation_rows, "EVALUATION")
    _validate_truth_values(truth_rows)

    evaluation_keys = {_key(row) for row in evaluation_rows}
    truth_keys = {_key(row) for row in truth_rows}
    if evaluation_keys != truth_keys:
        raise LeakageAuditError("truth/order key isolation is not one-to-one")

    references = runner.reference_depths_from_csv(reference)
    reference_counts: dict[int, int] = {}
    for row in reference_rows:
        if (
            row["spacetime_kind"] == "MINK"
            and row["slice_status"] == "TRANSITION_EVALUABLE"
        ):
            depth = int(row["depth_k"])
            reference_counts[depth] = reference_counts.get(depth, 0) + 1
    if any(
        reference_counts.get(depth, 0) < runner.MIN_REFERENCE_PER_DEPTH
        for depth in references
    ):
        raise runner.DataContractError("reference depth has fewer than 12 rows")
    for row in evaluation_rows:
        if row["slice_status"] != "TRANSITION_EVALUABLE":
            continue
        depth = int(row["depth_k"])
        if depth not in references:
            raise runner.DataContractError("evaluation uses an absent reference depth")
        reference_value = float(row["depth_mink_reference"])
        theta_raw = float(row["theta_raw"])
        theta_residual = float(row["theta_residual"])
        if reference_value != references[depth]:
            raise runner.DataContractError("evaluation reference value drift")
        if theta_residual != theta_raw - reference_value:
            raise runner.DataContractError("evaluation residual arithmetic drift")

    return InputArtifacts(
        reference=reference,
        evaluation=evaluation,
        truth=truth,
        canonical=canonical,
        reference_rows=tuple(reference_rows),
        evaluation_rows=tuple(evaluation_rows),
        truth_rows=tuple(truth_rows),
    )


def join_scored_rows(inputs: InputArtifacts) -> list[dict[str, object]]:
    truth_by_key = {_key(row): row for row in inputs.truth_rows}
    scored = []
    for order_row in inputs.evaluation_rows:
        truth_row = truth_by_key[_key(order_row)]
        scored.append(
            {
                **order_row,
                "truth_r_mid": truth_row["truth_r_mid"],
                "truth_zone": truth_row["truth_zone"],
                "distance_to_horizon_over_ell": truth_row[
                    "distance_to_horizon_over_ell"
                ],
            }
        )
    return scored


def validate_scored_csv_bytes(data: bytes) -> list[dict[str, str]]:
    if not data.endswith(b"\n") or b"\r" in data:
        raise runner.DataContractError("scored CSV line endings drift")
    import csv

    try:
        parsed = list(
            csv.reader(io.StringIO(data.decode("utf-8"), newline=""), strict=True)
        )
    except (UnicodeDecodeError, csv.Error) as exc:
        raise runner.DataContractError("malformed scored CSV") from exc
    if not parsed or tuple(parsed[0]) != SCORED_FIELDS:
        raise runner.DataContractError("scored CSV header drift")
    rows = []
    keys = set()
    for values in parsed[1:]:
        if len(values) != len(SCORED_FIELDS):
            raise runner.DataContractError("scored CSV row width drift")
        row = dict(zip(SCORED_FIELDS, values, strict=True))
        key = _key(row)
        if key in keys:
            raise runner.DataContractError("duplicate scored key")
        keys.add(key)
        rows.append(row)
    order_projection = [
        {field: row[field] for field in runner.ORDER_FIELDS} for row in rows
    ]
    truth_projection = [
        {field: row[field] for field in runner.TRUTH_FIELDS} for row in rows
    ]
    runner.validate_order_csv_bytes(
        runner.render_csv(order_projection, runner.ORDER_FIELDS), {"EVALUATION"}
    )
    runner.validate_truth_csv_bytes(
        runner.render_csv(truth_projection, runner.TRUTH_FIELDS)
    )
    return rows


def observations(scored_rows: Sequence[Mapping[str, object]]) -> list[Observation]:
    result = []
    for row in scored_rows:
        if row["slice_status"] != "TRANSITION_EVALUABLE":
            continue
        zone = str(row["truth_zone"])
        if zone not in {"INTERIOR", "EXTERIOR"}:
            continue
        result.append(
            Observation(
                seed=int(row["seed"]),
                spacetime_kind=str(row["spacetime_kind"]),
                zone=zone,
                theta_residual=float(row["theta_residual"]),
                survivor_growth_baseline=float(row["survivor_growth_baseline"]),
            )
        )
    return result


def compute_coverage(inputs: InputArtifacts, obs: Sequence[Observation]) -> Coverage:
    expected_cells = {
        (seed, kind)
        for seed in (*runner.REFERENCE_SEEDS, *runner.EVALUATION_SEEDS)
        for kind in runner.SPACETIME_KINDS
    }
    observed_cells = {
        (int(row["seed"]), row["spacetime_kind"])
        for row in (*inputs.reference_rows, *inputs.evaluation_rows)
    }
    cell_counts = {
        (kind, zone): sum(
            item.spacetime_kind == kind and item.zone == zone for item in obs
        )
        for kind in runner.SPACETIME_KINDS
        for zone in ("INTERIOR", "EXTERIOR")
    }
    complete_zone_seeds = {}
    for kind in runner.SPACETIME_KINDS:
        complete = []
        for seed in runner.EVALUATION_SEEDS:
            zones = {
                item.zone
                for item in obs
                if item.spacetime_kind == kind and item.seed == seed
            }
            if zones == {"INTERIOR", "EXTERIOR"}:
                complete.append(seed)
        complete_zone_seeds[kind] = tuple(complete)
    reference_depths = runner.reference_depths_from_csv(inputs.reference)
    evaluation_depths = {
        int(row["depth_k"])
        for row in inputs.evaluation_rows
        if row["slice_status"] == "TRANSITION_EVALUABLE"
    }
    return Coverage(
        complete_seed_kind_cells=observed_cells == expected_cells,
        reference_depths_valid=evaluation_depths <= set(reference_depths),
        cell_counts=cell_counts,
        complete_zone_seeds=complete_zone_seeds,
    )


def _contrast_or_none(
    items: Sequence[Observation], kind: str, field: str
) -> float | None:
    selected = [item for item in items if item.spacetime_kind == kind]
    if {item.zone for item in selected} != {"INTERIOR", "EXTERIOR"}:
        return None
    return contrast(
        [float(getattr(item, field)) for item in selected],
        [item.zone for item in selected],
    )


def _permutation_or_none(
    items: Sequence[Observation], kind: str, complete_seeds: Sequence[int]
) -> float | None:
    selected = [
        item
        for item in items
        if item.spacetime_kind == kind and item.seed in set(complete_seeds)
    ]
    if not selected:
        return None
    try:
        return stratified_permutation_pvalue(
            [item.theta_residual for item in selected],
            [item.zone for item in selected],
            [item.seed for item in selected],
        )
    except CoreContractError as exc:
        raise runner.DataContractError(str(exc)) from exc


def compute_metrics(
    obs: Sequence[Observation], coverage: Coverage
) -> Metrics:
    bh_seed_contrasts: dict[int, float | None] = {}
    for seed in runner.EVALUATION_SEEDS:
        selected = [
            item
            for item in obs
            if item.spacetime_kind == "BH" and item.seed == seed
        ]
        if {item.zone for item in selected} == {"INTERIOR", "EXTERIOR"}:
            bh_seed_contrasts[seed] = contrast(
                [item.theta_residual for item in selected],
                [item.zone for item in selected],
            )
        else:
            bh_seed_contrasts[seed] = None

    bh = [item for item in obs if item.spacetime_kind == "BH"]
    bh_interior = [item.theta_residual for item in bh if item.zone == "INTERIOR"]
    bh_exterior = [item.theta_residual for item in bh if item.zone == "EXTERIOR"]
    return Metrics(
        bh_theta_contrast=_contrast_or_none(
            obs, "BH", "theta_residual"
        ),
        mink_theta_contrast=_contrast_or_none(
            obs, "MINK", "theta_residual"
        ),
        bh_survivor_contrast=_contrast_or_none(
            obs, "BH", "survivor_growth_baseline"
        ),
        bh_permutation_pvalue=_permutation_or_none(
            obs, "BH", coverage.complete_zone_seeds.get("BH", ())
        ),
        mink_permutation_pvalue=_permutation_or_none(
            obs, "MINK", coverage.complete_zone_seeds.get("MINK", ())
        ),
        positive_bh_seed_contrasts=sum(
            value is not None and value > 0.0
            for value in bh_seed_contrasts.values()
        ),
        bh_seed_contrasts=bh_seed_contrasts,
        bh_interior_lower_median=(
            lower_median(bh_interior) if bh_interior else None
        ),
        bh_exterior_lower_median=(
            lower_median(bh_exterior) if bh_exterior else None
        ),
        bh_theta_equals_survivor_everywhere=(
            bool(bh)
            and all(
                item.theta_residual == item.survivor_growth_baseline
                for item in bh
            )
        ),
    )


def assign_terminal_label(coverage: Coverage, metrics: Metrics) -> str:
    if not coverage.passes:
        return "INCONCLUSIVE_COVERAGE"
    required = (
        metrics.bh_theta_contrast,
        metrics.mink_theta_contrast,
        metrics.bh_survivor_contrast,
        metrics.bh_permutation_pvalue,
        metrics.mink_permutation_pvalue,
        metrics.bh_interior_lower_median,
        metrics.bh_exterior_lower_median,
    )
    if any(value is None for value in required):
        raise runner.DataContractError("coverage passed with an unavailable metric")
    assert metrics.bh_theta_contrast is not None
    assert metrics.mink_theta_contrast is not None
    assert metrics.bh_survivor_contrast is not None
    assert metrics.bh_permutation_pvalue is not None
    assert metrics.mink_permutation_pvalue is not None
    assert metrics.bh_interior_lower_median is not None
    assert metrics.bh_exterior_lower_median is not None

    if (
        (
            metrics.mink_theta_contrast > 0.0
            and metrics.mink_permutation_pvalue <= 0.10
        )
        or metrics.bh_theta_contrast <= metrics.bh_survivor_contrast
        or metrics.bh_theta_equals_survivor_everywhere
    ):
        return "KILLED_GENERIC_OR_BASELINE_SIGNAL"
    if (
        metrics.bh_theta_contrast <= 0.0
        or metrics.bh_permutation_pvalue > 0.01
        or metrics.positive_bh_seed_contrasts < 5
        or metrics.bh_interior_lower_median >= 0.0
        or metrics.bh_exterior_lower_median <= 0.0
    ):
        return "KILLED_NO_SIGNED_EXPANSION"
    return "SURVIVED_CHEAP_KILL_TEST"


def _metric(value: object) -> str:
    if value is None:
        return "NA"
    if isinstance(value, bool):
        return "1" if value else "0"
    return runner._format_scalar(value)


def render_report(
    inputs: InputArtifacts,
    coverage: Coverage,
    metrics: Metrics,
    terminal_label: str,
) -> bytes:
    if terminal_label not in SCIENTIFIC_LABELS:
        raise runner.DataContractError("non-scientific label cannot render a report")
    hashes = {
        "reference_order_only_sha256": sha256(inputs.reference),
        "evaluation_order_only_sha256": sha256(inputs.evaluation),
        "evaluation_truth_sha256": sha256(inputs.truth),
        "canonical_order_only_sha256": sha256(inputs.canonical),
    }
    machine_values = {
        "machine_schema": "pr009-machine-readable-v1",
        "terminal_label": terminal_label,
        "configuration_fingerprint": configuration_fingerprint(),
        **hashes,
        "bh_theta_contrast": _metric(metrics.bh_theta_contrast),
        "mink_theta_contrast": _metric(metrics.mink_theta_contrast),
        "bh_survivor_contrast": _metric(metrics.bh_survivor_contrast),
        "bh_permutation_pvalue": _metric(metrics.bh_permutation_pvalue),
        "mink_permutation_pvalue": _metric(metrics.mink_permutation_pvalue),
        "n_positive_bh_seed_contrasts": str(
            metrics.positive_bh_seed_contrasts
        ),
        "bh_interior_lower_median": _metric(
            metrics.bh_interior_lower_median
        ),
        "bh_exterior_lower_median": _metric(
            metrics.bh_exterior_lower_median
        ),
        "bh_interior_n": str(coverage.cell_counts.get(("BH", "INTERIOR"), 0)),
        "bh_exterior_n": str(coverage.cell_counts.get(("BH", "EXTERIOR"), 0)),
        "mink_interior_n": str(
            coverage.cell_counts.get(("MINK", "INTERIOR"), 0)
        ),
        "mink_exterior_n": str(
            coverage.cell_counts.get(("MINK", "EXTERIOR"), 0)
        ),
        "bh_complete_zone_seeds": str(
            len(coverage.complete_zone_seeds.get("BH", ()))
        ),
        "mink_complete_zone_seeds": str(
            len(coverage.complete_zone_seeds.get("MINK", ()))
        ),
    }
    machine = "\n".join(
        [MACHINE_BEGIN]
        + [f"{key}={machine_values[key]}" for key in MACHINE_KEYS]
        + [MACHINE_END]
    )
    seed_lines = "\n".join(
        f"- `{seed}`: {_metric(metrics.bh_seed_contrasts[seed])}"
        for seed in runner.EVALUATION_SEEDS
    )
    text = f"""# PR009 Ladder-Ensemble Effective-Expansion Report

## 1. Terminal result

`{terminal_label}`

## 2. Frozen configuration

- Reference seeds: `{','.join(map(str, runner.REFERENCE_SEEDS))}`
- Evaluation seeds: `{','.join(map(str, runner.EVALUATION_SEEDS))}`
- `intensity={runner.INTENSITY}`, `t_edge={runner.T_EDGE:g}`, `M={runner.M}`, `K={runner.K}`
- `MAX_DEPTH={runner.MAX_DEPTH}`, `MAX_STARTS={runner.MAX_STARTS}`, `device=cpu`
- Exchangeable tie-rank master seed: `{runner.TIE_RANK_MASTER_SEED}`
- Configuration fingerprint: `{configuration_fingerprint()}`

## 3. Input hashes

- Reference order-only: `{hashes['reference_order_only_sha256']}`
- Evaluation order-only: `{hashes['evaluation_order_only_sha256']}`
- Evaluation truth: `{hashes['evaluation_truth_sha256']}`
- Canonical order-only: `{hashes['canonical_order_only_sha256']}`

## 4. Coverage

| Cell | Evaluable scored transitions |
|---|---:|
| BH / INTERIOR | {coverage.cell_counts.get(('BH', 'INTERIOR'), 0)} |
| BH / EXTERIOR | {coverage.cell_counts.get(('BH', 'EXTERIOR'), 0)} |
| MINK / INTERIOR | {coverage.cell_counts.get(('MINK', 'INTERIOR'), 0)} |
| MINK / EXTERIOR | {coverage.cell_counts.get(('MINK', 'EXTERIOR'), 0)} |

- Complete seed-kind cells: `{coverage.complete_seed_kind_cells}`
- Valid reference depths for evaluation: `{coverage.reference_depths_valid}`
- BH seeds contributing both zones: `{len(coverage.complete_zone_seeds.get('BH', ()))}`
- MINK seeds contributing both zones: `{len(coverage.complete_zone_seeds.get('MINK', ()))}`
- Coverage gate: `{'PASS' if coverage.passes else 'FAIL'}`

## 5. Frozen primary statistics

- `C_BH(theta_residual)={_metric(metrics.bh_theta_contrast)}`
- `p_BH={_metric(metrics.bh_permutation_pvalue)}`
- `C_MINK(theta_residual)={_metric(metrics.mink_theta_contrast)}`
- `p_MINK={_metric(metrics.mink_permutation_pvalue)}`
- `C_BH(survivor_growth_baseline)={_metric(metrics.bh_survivor_contrast)}`
- Positive BH seed contrasts: `{metrics.positive_bh_seed_contrasts}/6`
- BH interior lower median: `{_metric(metrics.bh_interior_lower_median)}`
- BH exterior lower median: `{_metric(metrics.bh_exterior_lower_median)}`

## 6. BH seed contrasts

{seed_lines}

## 7. Machine-readable block

```text
{machine}
```

## 8. Interpretation limits

This result concerns one frozen randomized order-only ladder-ensemble width statistic in
the preregistered 1+1D cheap kill test. It does not establish apparent-horizon
reconstruction, convergence, 3+1D transfer, an area law, or identification of a marginally
outer trapped surface. An inconclusive or killed result cannot be converted to survival by
tuning the frozen design.
"""
    return text.encode("utf-8")


def validate_report_bytes(data: bytes, expected_label: str) -> dict[str, str]:
    if not data.endswith(b"\n") or b"\r" in data:
        raise runner.DataContractError("report line endings drift")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise runner.DataContractError("report is not UTF-8") from exc
    if text.count(MACHINE_BEGIN) != 1 or text.count(MACHINE_END) != 1:
        raise runner.DataContractError("machine block multiplicity drift")
    block = text[text.index(MACHINE_BEGIN) : text.index(MACHINE_END)].splitlines()
    pairs = [line.split("=", 1) for line in block[1:] if "=" in line]
    values = dict(pairs)
    if tuple(values) != MACHINE_KEYS:
        raise runner.DataContractError("machine key order drift")
    if values["terminal_label"] != expected_label:
        raise runner.DataContractError("report terminal label drift")
    return values


def score_inputs(inputs: InputArtifacts) -> tuple[bytes, bytes, str]:
    scored_rows = join_scored_rows(inputs)
    scored_data = runner.render_csv(scored_rows, SCORED_FIELDS)
    validate_scored_csv_bytes(scored_data)
    obs = observations(scored_rows)
    coverage = compute_coverage(inputs, obs)
    metrics = compute_metrics(obs, coverage)
    label = assign_terminal_label(coverage, metrics)
    report_data = render_report(inputs, coverage, metrics, label)
    validate_report_bytes(report_data, label)
    return scored_data, report_data, label


def run_production() -> str:
    inputs = load_and_validate_inputs()
    scored_data, report_data, label = score_inputs(inputs)
    try:
        runner.publish_set(((SCORED, scored_data), (REPORT, report_data)))
    except runner.PublicationError as exc:
        raise RuntimeInputError(str(exc)) from exc
    return label


def _refusal(label: str) -> int:
    print(f"PR009_TERMINAL_LABEL={label}", file=sys.stderr)
    return 1


def main(argv: Sequence[str] | None = None) -> int:
    if argv:
        return _refusal("FAILED_DATA_CONTRACT")
    try:
        label = run_production()
    except LeakageAuditError:
        return _refusal("FAILED_LEAKAGE_AUDIT")
    except runner.DataContractError:
        return _refusal("FAILED_DATA_CONTRACT")
    except RuntimeInputError:
        return _refusal("FAILED_RUNTIME")
    except Exception:
        return _refusal("FAILED_RUNTIME")
    print(f"PR009_TERMINAL_LABEL={label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
