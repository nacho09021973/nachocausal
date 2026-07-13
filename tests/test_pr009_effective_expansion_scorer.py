from __future__ import annotations

from dataclasses import replace
import math
from pathlib import Path

import pytest

from dev import run_pr009_effective_expansion as runner
from dev import score_pr009_effective_expansion as scorer


def complete_coverage() -> scorer.Coverage:
    return scorer.Coverage(
        complete_seed_kind_cells=True,
        reference_depths_valid=True,
        cell_counts={
            ("BH", "INTERIOR"): 30,
            ("BH", "EXTERIOR"): 30,
            ("MINK", "INTERIOR"): 30,
            ("MINK", "EXTERIOR"): 30,
        },
        complete_zone_seeds={
            "BH": runner.EVALUATION_SEEDS,
            "MINK": runner.EVALUATION_SEEDS,
        },
    )


def surviving_metrics() -> scorer.Metrics:
    return scorer.Metrics(
        bh_theta_contrast=2.0,
        mink_theta_contrast=0.0,
        bh_survivor_contrast=0.5,
        bh_permutation_pvalue=0.001,
        mink_permutation_pvalue=1.0,
        positive_bh_seed_contrasts=5,
        bh_seed_contrasts={seed: 1.0 for seed in runner.EVALUATION_SEEDS},
        bh_interior_lower_median=-1.0,
        bh_exterior_lower_median=1.0,
        bh_theta_equals_survivor_everywhere=False,
    )


def order_row(
    block: str,
    seed: int,
    kind: str,
    start_id: int,
    depth: int,
    theta: float,
) -> dict[str, object]:
    transition = depth == 1
    residual = theta if transition else None
    return {
        "run_block": block,
        "seed": seed,
        "spacetime_kind": kind,
        "intensity": runner.INTENSITY,
        "K": runner.K,
        "start_id": start_id,
        "depth_k": depth,
        "slice_status": "TRANSITION_EVALUABLE" if transition else "EMPTY",
        "n_survivors": 3 if transition else 0,
        "n_valid_pair_separations": 3 if transition else 0,
        "width_lower_median": 2.0 if transition else None,
        "theta_raw": theta if transition else None,
        "depth_mink_reference": 0.0 if transition else None,
        "theta_residual": residual,
        "survivor_growth_baseline": 0.0 if transition else None,
    }


def truth_row(
    seed: int,
    kind: str,
    start_id: int,
    depth: int,
    zone: str,
) -> dict[str, object]:
    if depth != 1:
        r_mid = None
        final_zone = None
        distance = None
    else:
        r_mid = 0.1 if zone == "INTERIOR" else 0.9
        final_zone = zone
        distance = abs(r_mid - runner.thresholds.R_S) / runner.thresholds.ell(
            runner.INTENSITY
        )
    return {
        "run_block": "EVALUATION",
        "seed": seed,
        "spacetime_kind": kind,
        "intensity": runner.INTENSITY,
        "K": runner.K,
        "start_id": start_id,
        "depth_k": depth,
        "truth_r_mid": r_mid,
        "truth_zone": final_zone,
        "distance_to_horizon_over_ell": distance,
    }


def valid_artifact_bytes() -> tuple[bytes, bytes, bytes, bytes]:
    reference_rows = []
    for seed in runner.REFERENCE_SEEDS:
        for kind in runner.SPACETIME_KINDS:
            # Two starts make 12 reference-MINK transitions per depth.
            for start_id in range(2):
                for depth in range(1, runner.MAX_DEPTH + 1):
                    reference_rows.append(
                        order_row("REFERENCE", seed, kind, start_id, depth, 0.0)
                    )

    evaluation_rows = []
    truth_rows = []
    for seed in runner.EVALUATION_SEEDS:
        for kind in runner.SPACETIME_KINDS:
            for start_id, zone in enumerate(("INTERIOR", "EXTERIOR")):
                theta = (
                    -1.0
                    if kind == "BH" and zone == "INTERIOR"
                    else 1.0
                    if kind == "BH"
                    else 0.0
                )
                for depth in range(1, runner.MAX_DEPTH + 1):
                    evaluation_rows.append(
                        order_row(
                            "EVALUATION", seed, kind, start_id, depth, theta
                        )
                    )
                    truth_rows.append(
                        truth_row(seed, kind, start_id, depth, zone)
                    )
    reference = runner.render_csv(reference_rows, runner.ORDER_FIELDS)
    evaluation = runner.render_csv(evaluation_rows, runner.ORDER_FIELDS)
    truth = runner.render_csv(truth_rows, runner.TRUTH_FIELDS)
    canonical = runner.combine_order_csv(reference, evaluation)
    return reference, evaluation, truth, canonical


def write_inputs(tmp_path: Path, monkeypatch) -> None:
    reference, evaluation, truth, canonical = valid_artifact_bytes()
    paths = {
        "REFERENCE_ORDER_ONLY": tmp_path / "reference.csv",
        "REFERENCE_SHA256": tmp_path / "reference.sha256",
        "EVALUATION_ORDER_ONLY": tmp_path / "evaluation.csv",
        "EVALUATION_TRUTH": tmp_path / "truth.csv",
        "CANONICAL_ORDER_ONLY": tmp_path / "canonical.csv",
    }
    for name, path in paths.items():
        monkeypatch.setattr(runner, name, path)
    paths["REFERENCE_ORDER_ONLY"].write_bytes(reference)
    paths["REFERENCE_SHA256"].write_bytes(
        f"{scorer.sha256(reference)}  {paths['REFERENCE_ORDER_ONLY'].name}\n".encode()
    )
    paths["EVALUATION_ORDER_ONLY"].write_bytes(evaluation)
    paths["EVALUATION_TRUTH"].write_bytes(truth)
    paths["CANONICAL_ORDER_ONLY"].write_bytes(canonical)


def test_configuration_fingerprint_is_stable():
    first = scorer.configuration_fingerprint()
    second = scorer.configuration_fingerprint()
    assert first == second and len(first) == 64


def test_leakage_prescan_rejects_truth_in_order_header():
    header = b"run_block,seed,truth_zone\n"
    with pytest.raises(scorer.LeakageAuditError):
        scorer.leakage_prescan(header)


def test_all_terminal_branches_and_precedence():
    coverage = complete_coverage()
    metrics = surviving_metrics()
    assert scorer.assign_terminal_label(coverage, metrics) == (
        "SURVIVED_CHEAP_KILL_TEST"
    )

    generic_mink = replace(
        metrics, mink_theta_contrast=0.2, mink_permutation_pvalue=0.1
    )
    assert scorer.assign_terminal_label(coverage, generic_mink) == (
        "KILLED_GENERIC_OR_BASELINE_SIGNAL"
    )
    baseline = replace(metrics, bh_survivor_contrast=2.0)
    assert scorer.assign_terminal_label(coverage, baseline) == (
        "KILLED_GENERIC_OR_BASELINE_SIGNAL"
    )
    no_sign = replace(metrics, bh_permutation_pvalue=0.0100001)
    assert scorer.assign_terminal_label(coverage, no_sign) == (
        "KILLED_NO_SIGNED_EXPANSION"
    )
    insufficient = replace(coverage, complete_seed_kind_cells=False)
    assert scorer.assign_terminal_label(insufficient, generic_mink) == (
        "INCONCLUSIVE_COVERAGE"
    )


def test_missing_zone_seed_is_na_and_cannot_count_positive():
    obs = []
    for seed in runner.EVALUATION_SEEDS[:5]:
        obs.extend(
            [
                scorer.Observation(seed, "BH", "INTERIOR", -1.0, 0.0),
                scorer.Observation(seed, "BH", "EXTERIOR", 1.0, 0.0),
            ]
        )
    # Sixth seed contributes only exterior and cannot become a positive contrast.
    obs.append(
        scorer.Observation(
            runner.EVALUATION_SEEDS[5], "BH", "EXTERIOR", 2.0, 0.0
        )
    )
    coverage = scorer.Coverage(
        True,
        True,
        {
            ("BH", "INTERIOR"): 5,
            ("BH", "EXTERIOR"): 6,
            ("MINK", "INTERIOR"): 0,
            ("MINK", "EXTERIOR"): 0,
        },
        {"BH": runner.EVALUATION_SEEDS[:5], "MINK": ()},
    )
    metrics = scorer.compute_metrics(obs, coverage)
    assert metrics.positive_bh_seed_contrasts == 5
    assert metrics.bh_seed_contrasts[runner.EVALUATION_SEEDS[5]] is None


def test_full_input_validation_and_inconclusive_scoring(tmp_path, monkeypatch):
    write_inputs(tmp_path, monkeypatch)
    inputs = scorer.load_and_validate_inputs()
    scored_data, report_data, label = scorer.score_inputs(inputs)
    assert label == "INCONCLUSIVE_COVERAGE"
    scored_rows = scorer.validate_scored_csv_bytes(scored_data)
    assert len(scored_rows) == 6 * 2 * 2 * runner.MAX_DEPTH
    machine = scorer.validate_report_bytes(report_data, label)
    assert machine["canonical_order_only_sha256"] == scorer.sha256(
        inputs.canonical
    )
    assert machine["bh_interior_n"] == "6"
    assert machine["bh_exterior_n"] == "6"


def test_truth_zone_arithmetic_is_revalidated(tmp_path, monkeypatch):
    write_inputs(tmp_path, monkeypatch)
    truth_path = runner.EVALUATION_TRUTH
    data = truth_path.read_text()
    truth_path.write_text(data.replace(",INTERIOR,", ",GUARD,", 1))
    with pytest.raises(runner.DataContractError, match="truth zone"):
        scorer.load_and_validate_inputs()


def test_truth_key_mismatch_is_leakage_not_generic_contract(tmp_path, monkeypatch):
    write_inputs(tmp_path, monkeypatch)
    lines = runner.EVALUATION_TRUTH.read_bytes().splitlines(keepends=True)
    runner.EVALUATION_TRUTH.write_bytes(b"".join(lines[:-1]))
    with pytest.raises(scorer.LeakageAuditError):
        scorer.load_and_validate_inputs()


def test_report_machine_block_rejects_mutation(tmp_path, monkeypatch):
    write_inputs(tmp_path, monkeypatch)
    inputs = scorer.load_and_validate_inputs()
    _csv_data, report, label = scorer.score_inputs(inputs)
    mutated = report.replace(
        b"terminal_label=INCONCLUSIVE_COVERAGE",
        b"terminal_label=SURVIVED_CHEAP_KILL_TEST",
    )
    with pytest.raises(runner.DataContractError, match="terminal"):
        scorer.validate_report_bytes(mutated, label)


@pytest.mark.parametrize(
    ("error", "label"),
    [
        (scorer.RuntimeInputError("x"), "FAILED_RUNTIME"),
        (runner.DataContractError("x"), "FAILED_DATA_CONTRACT"),
        (scorer.LeakageAuditError("x"), "FAILED_LEAKAGE_AUDIT"),
    ],
)
def test_pre_scoring_refusals_publish_nothing(monkeypatch, capsys, error, label):
    monkeypatch.setattr(scorer, "run_production", lambda: (_ for _ in ()).throw(error))
    assert scorer.main([]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == f"PR009_TERMINAL_LABEL={label}\n"


def test_cli_rejects_every_argument_without_running(monkeypatch, capsys):
    monkeypatch.setattr(
        scorer,
        "run_production",
        lambda: pytest.fail("production scorer must not run"),
    )
    assert scorer.main(["--input", "anything"]) == 1
    assert capsys.readouterr().err == (
        "PR009_TERMINAL_LABEL=FAILED_DATA_CONTRACT\n"
    )
