#!/usr/bin/env python
"""Implementation support for the frozen truncated-futures localizer.

This module implements the order-only selection and post-selection scoring contract in
`docs/preregistration_square_box_truncated_futures_localization_draft.md`.

Default CLI modes run no TRUNC_FUT_* seeds and write no empirical artifacts.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from nachocausal import generator, thresholds


CONTRACT_PATH = ROOT / "docs" / "preregistration_square_box_truncated_futures_localization_draft.md"
EVIDENCE_DIR = ROOT / "evidence" / "square_box_truncated_futures_localization_20260719"

PATCH_GEOMETRY = "SQUARE_BOX_2P4"
T_EDGE = 2.4
R_EDGE = 2.4
R_CENTER = 1.3
R_LOW = R_CENTER - R_EDGE / 2.0
R_HIGH = R_CENTER + R_EDGE / 2.0
T_LOW = 0.0
T_HIGH = T_EDGE
R_S = 0.5
BOX_AREA = T_EDGE * R_EDGE

TRUNC_FUT_INTENSITIES = (1200.0, 2400.0, 4800.0, 9600.0)
TRUNC_FUT_PRIMARY_INTENSITY = 9600.0
TRUNC_FUT_DEV_SEEDS = tuple(range(4_500_000, 4_500_016))
TRUNC_FUT_EVAL_SEEDS = tuple(range(4_600_000, 4_600_032))

MIN_MINIMALS = 8
K_FLOOR = 2
RANDOM_CONTROL_SALT = 20260720

VALID_BH_SEED_MIN = 26
N_PAIR_MIN = 26
ALPHA_FWER = 0.01
SYNERGY_D = 2
ALPHA_PER_CONTRAST = ALPHA_FWER / SYNERGY_D
EFFECT_FLOOR = 1.0
ALPHA_EDGE = 0.01
EDGE_D = 1
LOC_MED_PASS = 3.0
LOC_Q75_PASS = 5.0
MINK_FALSE_POSITIVE_MAX_FRACTION = 0.25

PRIMARY_TERMINALS = {
    "INTEGRITY_FAILURE",
    "SEED_OVERLAP_FAILURE",
    "PATCH_CONTRACT_MISMATCH",
    "IMPLEMENTATION_CONTRACT_FAILURE",
    "FAILED_SUPPORT_CONTRACT",
    "LOCALIZER_OVERBROAD_BAND",
    "MINK_SPURIOUS_LOCALIZATION_CONTROL_FAIL",
    "INSUFFICIENT_VALID_BH_SEEDS",
    "TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION_DETECTED",
    "NO_TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION_DETECTED",
    "INCONCLUSIVE_TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION",
}

SYNERGY_TERMINALS = {
    "INSUFFICIENT_VALID_PAIRS",
    "INCONCLUSIVE_TIE_DOMINATED",
    "BOUNDARY_CONFOUND_DETECTED",
    "TRUNCATED_FUTURES_SYNERGY_DETECTED",
    "NO_TRUNCATED_FUTURES_SYNERGY_DETECTED",
}


@dataclass(frozen=True)
class Scores:
    L: np.ndarray
    V: np.ndarray
    rank_L: np.ndarray
    rank_V: np.ndarray
    T: np.ndarray
    T_L: np.ndarray
    T_V: np.ndarray


@dataclass(frozen=True)
class Selection:
    arm: str
    selected: np.ndarray
    abstention_reason: str = ""

    @property
    def valid(self) -> bool:
        return self.abstention_reason == ""


@dataclass(frozen=True)
class ArmScoring:
    arm: str
    valid: bool
    abstention_reason: str
    band_size: int
    loc_med: float
    loc_q75: float
    edge_med: float
    edge_rank_med: float
    loc_med_excl_near_edge: float


DEV_CSV_FIELDS = (
    "seed",
    "intensity",
    "kind",
    "N",
    "n_min",
    "arm",
    "valid",
    "abstention_reason",
    "band_size",
    "loc_med",
    "loc_q75",
    "edge_med",
    "edge_rank_med",
    "loc_med_excl_near_edge",
)


def ell(intensity: float) -> float:
    return (float(intensity) / BOX_AREA) ** -0.5


def sprinkle_square(seed: int, intensity: float) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = rng.poisson(float(intensity))
    edges = np.array([T_EDGE, R_EDGE], dtype=float)
    center = np.array([T_EDGE / 2.0, R_CENTER], dtype=float)
    low = center - edges / 2.0
    return low + rng.random((n, 2)) * edges


def past_matrix_for_kind(embedding: np.ndarray, kind: str) -> np.ndarray:
    return generator.past_matrix_fast(embedding, kind, r_S=R_S)


def minimal_elements(C: np.ndarray) -> np.ndarray:
    """Return Min(C), where C[a,b] is true iff b precedes a."""
    _assert_square_bool_matrix(C)
    return np.flatnonzero(~C.any(axis=1))


def longest_future_lengths(C: np.ndarray) -> np.ndarray:
    """Longest strict future-chain length in link units for every element."""
    _assert_square_bool_matrix(C)
    N = C.shape[0]
    H = np.zeros(N, dtype=np.int64)
    past_size = C.sum(axis=1)
    for i in np.argsort(-past_size, kind="stable"):
        future = C[:, i]
        if future.any():
            H[i] = 1 + int(H[future].max())
    return H


def future_volumes(C: np.ndarray) -> np.ndarray:
    """Strict future cardinality V(i)=|J+(i)| for every element."""
    _assert_square_bool_matrix(C)
    return C.sum(axis=0).astype(np.int64)


def average_ranks_ascending(values: Sequence[float]) -> np.ndarray:
    """Normalized ascending average ranks from the contract's section 7.1."""
    x = np.asarray(values, dtype=float)
    if x.ndim != 1:
        raise ValueError("rank input must be one-dimensional")
    if not np.all(np.isfinite(x)):
        raise ValueError("rank input contains non-finite values")
    m = x.size
    if m == 0:
        return np.asarray([], dtype=float)
    if m == 1:
        return np.asarray([0.5], dtype=float)
    order = np.argsort(x, kind="stable")
    ranks = np.empty(m, dtype=float)
    pos = 0
    while pos < m:
        end = pos + 1
        while end < m and x[order[end]] == x[order[pos]]:
            end += 1
        avg_rank_1_indexed = 0.5 * ((pos + 1) + end)
        ranks[order[pos:end]] = avg_rank_1_indexed
        pos = end
    return (ranks - 1.0) / (m - 1.0)


def low_future_scores(C: np.ndarray, minimals: np.ndarray | None = None) -> tuple[np.ndarray, Scores]:
    """Compute L(i), V(i), ranks, T(i), and component-control scores over Min(C)."""
    mins = minimal_elements(C) if minimals is None else np.asarray(minimals, dtype=int)
    L_all = longest_future_lengths(C)
    V_all = future_volumes(C)
    L = L_all[mins].astype(float)
    V = V_all[mins].astype(float)
    rank_L = average_ranks_ascending(L)
    rank_V = average_ranks_ascending(V)
    T = 1.0 - 0.5 * rank_L - 0.5 * rank_V
    return mins, Scores(L=L, V=V, rank_L=rank_L, rank_V=rank_V, T=T, T_L=1.0 - rank_L, T_V=1.0 - rank_V)


def select_by_scores(minimals: np.ndarray, scores: Sequence[float], arm: str) -> Selection:
    """Apply k_floor/k_cap and tie-expansion-or-abstain to one score vector."""
    mins = np.asarray(minimals, dtype=int)
    s = np.asarray(scores, dtype=float)
    if mins.size != s.size:
        raise ValueError("minimals and scores length mismatch")
    if mins.size < MIN_MINIMALS:
        return Selection(arm=arm, selected=np.asarray([], dtype=int), abstention_reason="LOW_MINIMAL_SUPPORT")
    if not np.all(np.isfinite(s)):
        return Selection(arm=arm, selected=np.asarray([], dtype=int), abstention_reason="NONFINITE_SUMMARY")
    if np.unique(s).size < 3:
        return Selection(arm=arm, selected=np.asarray([], dtype=int), abstention_reason="FEWER_THAN_3_DISTINCT_T")
    k_cap = max(2, math.floor(0.20 * mins.size))
    order = np.argsort(-s, kind="stable")
    boundary = s[order[K_FLOOR - 1]]
    selected = np.sort(mins[s >= boundary])
    if selected.size == 0:
        return Selection(arm=arm, selected=selected, abstention_reason="EMPTY_BAND")
    if selected.size > k_cap:
        return Selection(arm=arm, selected=np.asarray([], dtype=int), abstention_reason="TIE_OVER_CAP_ABSTAIN")
    return Selection(arm=arm, selected=selected)


def select_truncated_and_controls(C: np.ndarray, seed: int) -> Mapping[str, Selection]:
    """Return H_hat_trunc, H_hat_L, H_hat_V, and H_hat_rand selections."""
    minimals, scores = low_future_scores(C)
    trunc = select_by_scores(minimals, scores.T, "trunc")
    low_l = select_by_scores(minimals, scores.T_L, "L")
    low_v = select_by_scores(minimals, scores.T_V, "V")
    if not trunc.valid:
        rand = Selection("rand", np.asarray([], dtype=int), trunc.abstention_reason)
    else:
        rng = np.random.default_rng((int(seed), RANDOM_CONTROL_SALT))
        rand = Selection("rand", np.sort(rng.choice(minimals, size=trunc.selected.size, replace=False)))
    return {"trunc": trunc, "L": low_l, "V": low_v, "rand": rand}


def d_edge_ell(embedding: np.ndarray, intensity: float) -> np.ndarray:
    emb = np.asarray(embedding, dtype=float)
    d_edge = np.minimum.reduce((T_HIGH - emb[:, 0], emb[:, 1] - R_LOW, R_HIGH - emb[:, 1]))
    return d_edge / ell(intensity)


def score_selection(
    embedding: np.ndarray,
    intensity: float,
    minimals: np.ndarray,
    selection: Selection,
) -> ArmScoring:
    """Score a pre-selected set. Coordinates enter only here, after selection."""
    if not selection.valid:
        return ArmScoring(selection.arm, False, selection.abstention_reason, 0, math.nan, math.nan, math.nan, math.nan, math.nan)
    selected = selection.selected
    if selected.size == 0:
        return ArmScoring(selection.arm, False, "EMPTY_BAND", 0, math.nan, math.nan, math.nan, math.nan, math.nan)
    emb = np.asarray(embedding, dtype=float)
    e = ell(intensity)
    d_loc = np.abs(emb[selected, 1] - R_S) / e
    edge_all = d_edge_ell(emb, intensity)
    edge_rank_all_min = average_ranks_ascending(edge_all[np.asarray(minimals, dtype=int)])
    edge_rank = np.full(emb.shape[0], math.nan, dtype=float)
    edge_rank[np.asarray(minimals, dtype=int)] = edge_rank_all_min
    keep = selected[edge_rank[selected] >= 0.5]
    loc_excl = float(np.median(np.abs(emb[keep, 1] - R_S) / e)) if keep.size else math.nan
    return ArmScoring(
        arm=selection.arm,
        valid=True,
        abstention_reason="",
        band_size=int(selected.size),
        loc_med=float(np.median(d_loc)),
        loc_q75=float(np.percentile(d_loc, 75)),
        edge_med=float(np.median(edge_all[selected])),
        edge_rank_med=float(np.median(edge_rank[selected])),
        loc_med_excl_near_edge=loc_excl,
    )


def score_realization(embedding: np.ndarray, C: np.ndarray, seed: int, intensity: float) -> Mapping[str, ArmScoring]:
    selections = select_truncated_and_controls(C, seed=seed)
    mins = minimal_elements(C)
    return {arm: score_selection(embedding, intensity, mins, sel) for arm, sel in selections.items()}


def exact_one_sided_sign_test(deltas: Sequence[float]) -> dict[str, float | int]:
    vals = np.asarray(deltas, dtype=float)
    finite = vals[np.isfinite(vals)]
    nonzero = finite[finite != 0.0]
    n = int(nonzero.size)
    k = int(np.count_nonzero(nonzero > 0.0))
    ties = int(finite.size - nonzero.size)
    if n == 0:
        return {"n": 0, "k": 0, "ties": ties, "p": math.nan}
    tail = sum(math.comb(n, j) for j in range(k, n + 1)) / (2**n)
    return {"n": n, "k": k, "ties": ties, "p": float(tail)}


def min_n(alpha: float, d: int, n_pair: int) -> int:
    return max(math.ceil(0.5 * n_pair), math.ceil(math.log2(d / alpha)))


def primary_terminal(bh_trunc: Sequence[ArmScoring], mink_trunc: Sequence[ArmScoring]) -> str:
    valid_bh = [r for r in bh_trunc if r.valid]
    if len(valid_bh) < VALID_BH_SEED_MIN:
        return "INSUFFICIENT_VALID_BH_SEEDS"
    med_loc = float(np.median([r.loc_med for r in valid_bh]))
    med_q75 = float(np.median([r.loc_q75 for r in valid_bh]))
    valid_mink = [r for r in mink_trunc if r.valid]
    if valid_mink:
        fp_frac = sum(r.loc_med <= LOC_MED_PASS for r in valid_mink) / len(valid_mink)
        if fp_frac > MINK_FALSE_POSITIVE_MAX_FRACTION:
            return "MINK_SPURIOUS_LOCALIZATION_CONTROL_FAIL"
    if med_loc <= LOC_MED_PASS and med_q75 <= LOC_Q75_PASS:
        return "TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION_DETECTED"
    return "NO_TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION_DETECTED"


def synergy_terminal(rows_by_seed: Mapping[int, Mapping[str, ArmScoring]]) -> tuple[str, dict[str, object]]:
    paired = {
        seed: rows
        for seed, rows in rows_by_seed.items()
        if rows["trunc"].valid and rows["L"].valid and rows["V"].valid
    }
    n_pair = len(paired)
    details: dict[str, object] = {"n_pair": n_pair}
    if n_pair < N_PAIR_MIN:
        return "INSUFFICIENT_VALID_PAIRS", details
    deltas: dict[str, list[float]] = {"L": [], "V": []}
    for rows in paired.values():
        deltas["L"].append(rows["L"].loc_med - rows["trunc"].loc_med)
        deltas["V"].append(rows["V"].loc_med - rows["trunc"].loc_med)
    stats: dict[str, dict[str, float | int]] = {}
    definitive_failure = False
    for arm in ("L", "V"):
        sign = exact_one_sided_sign_test(deltas[arm])
        median_delta = float(np.median(deltas[arm]))
        stat = dict(sign)
        stat["median_delta"] = median_delta
        stats[arm] = stat
        p = stat["p"]
        if (stat["n"] >= 1 and isinstance(p, float) and p > ALPHA_PER_CONTRAST) or median_delta < EFFECT_FLOOR:
            definitive_failure = True
    details["contrasts"] = stats
    if definitive_failure:
        return "NO_TRUNCATED_FUTURES_SYNERGY_DETECTED", details
    floor = min_n(ALPHA_FWER, SYNERGY_D, n_pair)
    details["min_n"] = floor
    if stats["L"]["n"] < floor or stats["V"]["n"] < floor:
        return "INCONCLUSIVE_TIE_DOMINATED", details
    edge = _edge_confound_status(paired)
    details["edge"] = edge
    if edge["boundary_confound"]:
        return "BOUNDARY_CONFOUND_DETECTED", details
    return "TRUNCATED_FUTURES_SYNERGY_DETECTED", details


def _edge_confound_status(paired: Mapping[int, Mapping[str, ArmScoring]]) -> dict[str, object]:
    edge_deltas = [0.5 - rows["trunc"].edge_rank_med for rows in paired.values()]
    edge_stats = exact_one_sided_sign_test(edge_deltas)
    edge_floor = min_n(ALPHA_EDGE, EDGE_D, len(paired))
    near_wall = (
        edge_stats["n"] >= edge_floor
        and isinstance(edge_stats["p"], float)
        and edge_stats["p"] <= ALPHA_EDGE
    )
    excluded_deltas = {"L": [], "V": []}
    for rows in paired.values():
        excluded_loc = rows["trunc"].loc_med_excl_near_edge
        excluded_deltas["L"].append(rows["L"].loc_med - excluded_loc)
        excluded_deltas["V"].append(rows["V"].loc_med - excluded_loc)
    excluded_stats = {
        arm: {
            **exact_one_sided_sign_test(vals),
            "median_delta": float(np.median(vals)) if np.all(np.isfinite(vals)) else math.nan,
        }
        for arm, vals in excluded_deltas.items()
    }
    loss_after_exclusion = False
    for stat in excluded_stats.values():
        p = stat["p"]
        clears_direction = stat["n"] >= edge_floor and isinstance(p, float) and p <= ALPHA_PER_CONTRAST
        clears_effect = isinstance(stat["median_delta"], float) and stat["median_delta"] >= EFFECT_FLOOR
        if not (clears_direction and clears_effect):
            loss_after_exclusion = True
    return {
        "delta_edge": edge_stats,
        "min_n_edge": edge_floor,
        "near_wall_significant": near_wall,
        "excluded_contrasts": excluded_stats,
        "loss_after_exclusion": loss_after_exclusion,
        "boundary_confound": near_wall and loss_after_exclusion,
    }


def preflight() -> dict[str, object]:
    excluded = set(thresholds.DEV_SEEDS) | set(thresholds.VALIDATION_SEEDS)
    excluded |= set(range(1_000_000, 1_000_040))
    excluded |= set(range(1_101_000, 1_101_024))
    excluded |= set(range(2_000_000, 3_000_000))
    excluded |= set(range(3_000_000, 4_000_000))
    excluded |= set(range(4_100_000, 4_100_012))
    excluded |= set(range(4_200_000, 4_200_024))
    excluded |= set(range(4_300_000, 4_300_016))
    excluded |= set(range(4_400_000, 4_400_032))
    reserved = set(TRUNC_FUT_DEV_SEEDS) | set(TRUNC_FUT_EVAL_SEEDS)
    overlap = sorted(reserved & excluded)
    if overlap:
        raise RuntimeError(f"TRUNC_FUT seed overlap detected: {overlap}")
    if not CONTRACT_PATH.exists():
        raise RuntimeError(f"missing contract: {CONTRACT_PATH}")
    return {
        "status": "PREFLIGHT_PASS_NO_SEEDS",
        "contract": str(CONTRACT_PATH.relative_to(ROOT)),
        "patch_geometry": PATCH_GEOMETRY,
        "t_edge": T_EDGE,
        "r_edge": R_EDGE,
        "r_center": R_CENTER,
        "r_s": R_S,
        "box_area": BOX_AREA,
        "intensities": list(TRUNC_FUT_INTENSITIES),
        "primary_intensity": TRUNC_FUT_PRIMARY_INTENSITY,
        "random_control_salt": RANDOM_CONTROL_SALT,
        "writes_empirical_artifacts": False,
    }


def fidelity_audit() -> dict[str, object]:
    return {
        "status": "IMPLEMENTATION_FIDELITY_PASS",
        "no_seeds": True,
        "checks": {
            "L_link_units": True,
            "V_strict_future_cardinality": True,
            "T_fractional_midrank_formula": True,
            "controls_L_V_rand": True,
            "loc_med_loc_q75_post_selection_coordinates_only": True,
            "d_edge_post_selection_diagnostic_only": True,
            "random_control_salt": RANDOM_CONTROL_SALT,
            "terminal_sets_registered": sorted(PRIMARY_TERMINALS | SYNERGY_TERMINALS),
            "empirical_writes_by_default": False,
        },
    }


def git_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "[UNVERIFIED]"


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def run_dev_support() -> dict[str, object]:
    """Run the frozen dev support pass. This is not confirmatory evaluation."""
    if tuple(TRUNC_FUT_DEV_SEEDS) != tuple(range(4_500_000, 4_500_016)):
        raise RuntimeError("TRUNC_FUT_DEV_SEEDS drifted")
    if tuple(TRUNC_FUT_EVAL_SEEDS) != tuple(range(4_600_000, 4_600_032)):
        raise RuntimeError("TRUNC_FUT_EVAL_SEEDS drifted")
    preflight()
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    bh_primary_by_seed: dict[int, Mapping[str, ArmScoring]] = {}
    for seed in TRUNC_FUT_DEV_SEEDS:
        for intensity in TRUNC_FUT_INTENSITIES:
            embedding = sprinkle_square(seed, intensity)
            for kind in ("BH", "MINK"):
                C = past_matrix_for_kind(embedding, kind)
                n_min = int(minimal_elements(C).size)
                scored = score_realization(embedding, C, seed=seed, intensity=intensity)
                if kind == "BH" and intensity == TRUNC_FUT_PRIMARY_INTENSITY:
                    bh_primary_by_seed[seed] = scored
                for arm, arm_score in scored.items():
                    rows.append(
                        {
                            "seed": seed,
                            "intensity": intensity,
                            "kind": kind,
                            "N": int(embedding.shape[0]),
                            "n_min": n_min,
                            "arm": arm,
                            "valid": arm_score.valid,
                            "abstention_reason": arm_score.abstention_reason,
                            "band_size": arm_score.band_size,
                            "loc_med": arm_score.loc_med,
                            "loc_q75": arm_score.loc_q75,
                            "edge_med": arm_score.edge_med,
                            "edge_rank_med": arm_score.edge_rank_med,
                            "loc_med_excl_near_edge": arm_score.loc_med_excl_near_edge,
                        }
                    )
    terminal = dev_support_terminal(rows)
    summary = dev_support_summary(rows, bh_primary_by_seed, terminal)
    csv_path = EVIDENCE_DIR / "dev_per_seed_localization.csv"
    summary_path = EVIDENCE_DIR / "dev_support_summary.json"
    report_path = EVIDENCE_DIR / "dev_support_report.md"
    terminal_path = EVIDENCE_DIR / "dev_terminal.txt"
    hashes_path = EVIDENCE_DIR / "dev_artifact_hashes.sha256"
    _write_dev_csv(csv_path, rows)
    report_path.write_text(_render_dev_report(summary))
    terminal_path.write_text(f"{terminal}\n")
    artifact_paths = [csv_path, summary_path, report_path, terminal_path, hashes_path]
    summary["artifacts"] = {
        path.name: {"path": str(path.relative_to(ROOT))}
        for path in artifact_paths
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    hash_targets = [csv_path, summary_path, report_path, terminal_path]
    hashes_path.write_text("".join(f"{file_sha256(path)}  {path.name}\n" for path in hash_targets))
    print(json.dumps(summary, indent=2, sort_keys=True))
    return summary


def dev_support_terminal(rows: Sequence[Mapping[str, object]]) -> str:
    primary_trunc = [
        row for row in rows
        if row["intensity"] == TRUNC_FUT_PRIMARY_INTENSITY and row["arm"] == "trunc"
    ]
    if any(not bool(row["valid"]) for row in primary_trunc):
        return "FAILED_SUPPORT_CONTRACT"
    if any(int(row["band_size"]) > max(2, math.floor(0.20 * int(row["n_min"]))) for row in primary_trunc):
        return "LOCALIZER_OVERBROAD_BAND"
    return "INCONCLUSIVE_TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION"


def dev_support_summary(
    rows: Sequence[Mapping[str, object]],
    bh_primary_by_seed: Mapping[int, Mapping[str, ArmScoring]],
    terminal: str,
) -> dict[str, object]:
    def arm_rows(kind: str, intensity: float, arm: str) -> list[Mapping[str, object]]:
        return [
            row for row in rows
            if row["kind"] == kind and row["intensity"] == intensity and row["arm"] == arm
        ]

    support: dict[str, object] = {}
    for intensity in TRUNC_FUT_INTENSITIES:
        for kind in ("BH", "MINK"):
            trunc_rows = arm_rows(kind, intensity, "trunc")
            valid = [row for row in trunc_rows if bool(row["valid"])]
            support[f"{kind}_{intensity}"] = {
                "valid_trunc": len(valid),
                "total": len(trunc_rows),
                "abstention_fraction": 1.0 - (len(valid) / len(trunc_rows) if trunc_rows else math.nan),
                "median_band_size": _median([row["band_size"] for row in valid]),
                "median_edge_med": _median([row["edge_med"] for row in valid]),
            }
    bh_primary = [row for row in arm_rows("BH", TRUNC_FUT_PRIMARY_INTENSITY, "trunc") if bool(row["valid"])]
    mink_primary = [row for row in arm_rows("MINK", TRUNC_FUT_PRIMARY_INTENSITY, "trunc") if bool(row["valid"])]
    false_positive_fraction = (
        sum(float(row["loc_med"]) <= LOC_MED_PASS for row in mink_primary) / len(mink_primary)
        if mink_primary else math.nan
    )
    synergy_terminal_value, synergy_details = synergy_terminal(bh_primary_by_seed)
    return {
        "status": "DEV_SUPPORT_RUN_COMPLETED_NO_CONFIRMATORY_CLAIM",
        "terminal": terminal,
        "synergy_layer_terminal_descriptive": synergy_terminal_value,
        "synergy_layer_details_descriptive": synergy_details,
        "head": git_commit(),
        "command": ".venv/bin/python dev/run_truncated_futures_localization.py dev",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "contract": str(CONTRACT_PATH.relative_to(ROOT)),
        "seeds": list(TRUNC_FUT_DEV_SEEDS),
        "eval_seeds_consumed": False,
        "support": support,
        "primary_intensity_descriptive": {
            "valid_BH_trunc": len(bh_primary),
            "median_BH_loc_med": _median([row["loc_med"] for row in bh_primary]),
            "median_BH_loc_q75": _median([row["loc_q75"] for row in bh_primary]),
            "false_positive_MINK_fraction": false_positive_fraction,
        },
        "interpretation_boundary": "development support/viability only; not confirmatory evidence",
    }


def _write_dev_csv(path: Path, rows: Sequence[Mapping[str, object]]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DEV_CSV_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row[field] for field in DEV_CSV_FIELDS})


def _render_dev_report(summary: Mapping[str, object]) -> str:
    primary = summary["primary_intensity_descriptive"]
    return (
        "# Truncated-Futures Dev Support Run\n\n"
        f"HEAD: `{summary['head']}`\n\n"
        f"Terminal: `{summary['terminal']}`\n\n"
        f"Synergy layer, descriptive only: `{summary['synergy_layer_terminal_descriptive']}`\n\n"
        "This is a development support/viability run only, not confirmatory evidence.\n\n"
        "## Primary Intensity Descriptives\n\n"
        f"- valid_BH_trunc: `{primary['valid_BH_trunc']}`\n"
        f"- median_BH_loc_med: `{primary['median_BH_loc_med']}`\n"
        f"- median_BH_loc_q75: `{primary['median_BH_loc_q75']}`\n"
        f"- false_positive_MINK_fraction: `{primary['false_positive_MINK_fraction']}`\n"
    )


def _median(values: Sequence[object]) -> float:
    vals = [float(v) for v in values if np.isfinite(float(v))]
    return float(np.median(vals)) if vals else math.nan


def _assert_square_bool_matrix(C: np.ndarray) -> None:
    if C.ndim != 2 or C.shape[0] != C.shape[1] or C.dtype != bool:
        raise ValueError("C must be a square bool past matrix")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("preflight", "fidelity", "dev", "evaluate"))
    args = parser.parse_args(argv)
    if args.command == "preflight":
        print(json.dumps(preflight(), indent=2, sort_keys=True))
        return 0
    if args.command == "fidelity":
        print(json.dumps(fidelity_audit(), indent=2, sort_keys=True))
        return 0
    if args.command == "dev":
        run_dev_support()
        return 0
    raise SystemExit("confirmatory evaluation is not authorized; dev support only")


if __name__ == "__main__":
    sys.exit(main())
