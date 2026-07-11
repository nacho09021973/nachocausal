"""PRESENT_ANCHOR_SANITY_PILOT v2.

Private exploratory diagnostic only. This script reuses the existing numpy
sprinkler, past-matrix builder, and order-only longest-chain machinery to check
whether point anchors have nondegenerate past/future cones.

v2 is a post-hoc repair of a diagnostic scale bug in v1: boundary proxies with
different units must not share one threshold. It is not a clean preregistered
result.

No K-beam, no PR003/PR004 modification, no publication claim.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from collections import Counter
from statistics import median

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import estimator, generator, thresholds  # noqa: E402


DEFAULT_SEEDS = (1_000_000, 1_000_001, 1_000_002)
DEFAULT_INTENSITY = 600.0
DEFAULT_T_EDGE = 6.0
DEFAULT_MAX_ANCHORS_PER_RULE = 5
DEFAULT_MAX_SEEDS = 3
EXPANDED_KILL_TEST_MAX_SEEDS = 12
EXPANDED_KILL_TEST_MAX_ANCHORS_PER_RULE = 10
DEFAULT_CSV = "data/reports/present_anchor_sanity_pilot_v2.csv"
DEFAULT_SUMMARY = "data/reports/PRESENT_ANCHOR_SANITY_PILOT_V2_SUMMARY.md"
CHEAP_VERDICT_VERSION = "v2_proxy_separated"

ORDER_DEPTH_MIN = "ORDER_DEPTH_MIN"
GEOMETRIC_NORMALIZED_DISTANCE = "GEOMETRIC_NORMALIZED_DISTANCE"
UNKNOWN_PROXY = "UNKNOWN"

FIELDNAMES = [
    "run_id",
    "seed",
    "intensity",
    "kind",
    "anchor_rule_id",
    "anchor_class",
    "selected_p_index_or_id",
    "past_volume",
    "future_volume",
    "past_depth",
    "future_depth",
    "volume_asymmetry",
    "depth_asymmetry",
    "boundary_proxy_kind",
    "boundary_distance_proxy_value",
    "cheap_verdict",
    "cheap_verdict_version",
    "notes",
]


def order_only_heights(C: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return longest-chain depth to past and future for every element."""
    _, _, Lfut = estimator.estimate_O(C)
    order = estimator._topological_future_first(C)
    Lpast = np.zeros(C.shape[0], dtype=np.int64)
    for e in reversed(order):
        past = np.nonzero(C[e])[0]
        Lpast[e] = 1 + (int(Lpast[past].max()) if past.size else 0)
    return Lpast, Lfut.astype(np.int64)


def cone_stats(C: np.ndarray, p: int, Lpast: np.ndarray, Lfut: np.ndarray) -> dict:
    past_volume = int(C[p, :].sum())
    future_volume = int(C[:, p].sum())
    past_depth = max(0, int(Lpast[p]) - 1)
    future_depth = max(0, int(Lfut[p]) - 1)
    volume_asymmetry = abs(past_volume - future_volume) / max(
        1, past_volume + future_volume
    )
    depth_asymmetry = abs(past_depth - future_depth) / max(1, past_depth + future_depth)
    return dict(
        past_volume=past_volume,
        future_volume=future_volume,
        past_depth=past_depth,
        future_depth=future_depth,
        volume_asymmetry=float(volume_asymmetry),
        depth_asymmetry=float(depth_asymmetry),
    )


def internal_eligible(C: np.ndarray, Lpast: np.ndarray, Lfut: np.ndarray) -> np.ndarray:
    past_volume = C.sum(axis=1)
    future_volume = C.sum(axis=0)
    mask = (
        (past_volume >= 5)
        & (future_volume >= 5)
        & (Lpast >= 3)
        & (Lfut >= 3)
    )
    return np.flatnonzero(mask)


def choose_random_eligible(
    eligible: np.ndarray, seed: int, max_anchors: int
) -> list[int]:
    if eligible.size == 0:
        return []
    rng = np.random.default_rng(seed + 91_001)
    n = min(max_anchors, int(eligible.size))
    return [int(x) for x in rng.choice(eligible, size=n, replace=False)]


def choose_midrank(
    eligible: np.ndarray, Lpast: np.ndarray, Lfut: np.ndarray, max_anchors: int
) -> list[int]:
    if eligible.size == 0:
        return []
    score = np.abs(Lpast[eligible] - Lfut[eligible])
    order = np.lexsort((eligible, score))
    return [int(x) for x in eligible[order[:max_anchors]]]


def choose_balanced_volume(C: np.ndarray, eligible: np.ndarray, max_anchors: int) -> list[int]:
    if eligible.size == 0:
        return []
    past_volume = C.sum(axis=1)[eligible]
    future_volume = C.sum(axis=0)[eligible]
    score = np.abs(past_volume - future_volume) / np.maximum(1, past_volume + future_volume)
    order = np.lexsort((eligible, score))
    return [int(x) for x in eligible[order[:max_anchors]]]


def choose_central_embedding(
    emb: np.ndarray,
    edges: np.ndarray,
    center: np.ndarray,
    eligible: np.ndarray,
    max_anchors: int,
) -> list[int]:
    if eligible.size == 0:
        return []
    scaled = (emb[eligible] - center) / np.maximum(edges, 1e-12)
    score = np.sum(scaled * scaled, axis=1)
    order = np.lexsort((eligible, score))
    return [int(x) for x in eligible[order[:max_anchors]]]


def order_boundary_proxy(stats: dict) -> float:
    return float(min(stats["past_depth"], stats["future_depth"]))


def embedding_boundary_proxy(
    emb: np.ndarray, edges: np.ndarray, center: np.ndarray, p: int
) -> float:
    low = center - edges / 2.0
    high = center + edges / 2.0
    d = np.minimum(emb[p] - low, high - emb[p])
    return float(np.min(d / np.maximum(edges, 1e-12)))


def cheap_verdict(
    stats: dict, boundary_proxy: float, boundary_proxy_kind: str
) -> tuple[str, str]:
    if (
        stats["past_volume"] < 5
        or stats["future_volume"] < 5
        or stats["past_depth"] < 2
        or stats["future_depth"] < 2
    ):
        return "DEGENERATE", "one cone too small for bilateral diagnostic"

    if boundary_proxy_kind == ORDER_DEPTH_MIN:
        boundary_flag = boundary_proxy <= 2
        proxy_note = "order-depth boundary proxy"
    elif boundary_proxy_kind == GEOMETRIC_NORMALIZED_DISTANCE:
        boundary_flag = boundary_proxy <= 0.10
        proxy_note = "geometry-normalized boundary proxy"
    else:
        boundary_flag = False
        proxy_note = "unknown boundary proxy; boundary flag not applied"

    if boundary_flag or stats["volume_asymmetry"] > 0.85 or stats["depth_asymmetry"] > 0.85:
        return "BOUNDARY_DOMINATED", "near order-boundary proxy or very asymmetric cones"
    if (
        stats["past_volume"] >= 10
        and stats["future_volume"] >= 10
        and stats["past_depth"] >= 3
        and stats["future_depth"] >= 3
        and stats["volume_asymmetry"] <= 0.75
        and stats["depth_asymmetry"] <= 0.75
    ):
        return "PROMISING", f"nondegenerate bilateral cones under {proxy_note}"
    return "MIXED", f"usable cones but asymmetry/boundary risk remains under {proxy_note}"


def rows_for_seed(seed: int, intensity: float, t_edge: float, max_anchors: int) -> list[dict]:
    emb, edges, center = generator.numpy_sprinkle(seed, intensity, t_edge)
    C = generator.past_matrix_fast(emb, "BH")
    Lpast, Lfut = order_only_heights(C)
    eligible = internal_eligible(C, Lpast, Lfut)
    rules = [
        (
            "RANDOM_ELIGIBLE_INTERNAL_POINT",
            "ORDER_ONLY",
            choose_random_eligible(eligible, seed, max_anchors),
            "order-depth proxy",
        ),
        (
            "MIDRANK_ORDER_POINT",
            "ORDER_ONLY",
            choose_midrank(eligible, Lpast, Lfut, max_anchors),
            "order-depth proxy",
        ),
        (
            "BALANCED_PAST_FUTURE_VOLUME_POINT",
            "ORDER_ONLY",
            choose_balanced_volume(C, eligible, max_anchors),
            "order-depth proxy; selection favors volume balance by construction",
        ),
        (
            "CENTRAL_EMBEDDING_POINT",
            "GEOMETRY_ASSISTED",
            choose_central_embedding(emb, edges, center, eligible, max_anchors),
            "geometry-assisted edge-distance proxy; no order-only claim",
        ),
    ]
    rows: list[dict] = []
    for rule_id, anchor_class, anchors, note in rules:
        for p in anchors:
            stats = cone_stats(C, p, Lpast, Lfut)
            if anchor_class == "GEOMETRY_ASSISTED":
                boundary_proxy = embedding_boundary_proxy(emb, edges, center, p)
                boundary_proxy_kind = GEOMETRIC_NORMALIZED_DISTANCE
            else:
                boundary_proxy = order_boundary_proxy(stats)
                boundary_proxy_kind = ORDER_DEPTH_MIN
            verdict, verdict_note = cheap_verdict(stats, boundary_proxy, boundary_proxy_kind)
            rows.append(
                dict(
                    run_id="PRESENT_ANCHOR_SANITY_PILOT",
                    seed=int(seed),
                    intensity=float(intensity),
                    kind="BH",
                    anchor_rule_id=rule_id,
                    anchor_class=anchor_class,
                    selected_p_index_or_id=int(p),
                    boundary_proxy_kind=boundary_proxy_kind,
                    boundary_distance_proxy_value=float(boundary_proxy),
                    cheap_verdict=verdict,
                    cheap_verdict_version=CHEAP_VERDICT_VERSION,
                    notes=f"{note}; {verdict_note}",
                    **stats,
                )
            )
    return rows


def fmt_float(x: float) -> str:
    return f"{x:.4f}"


def overall_result(counts: Counter) -> str:
    total = sum(counts.values())
    if total == 0 or counts.get("NOT_COMPUTABLE", 0) == total:
        return "NO_CHEAP_PILOT_AVAILABLE"
    if counts.get("DEGENERATE", 0) / total >= 0.5:
        return "DEGENERATE"
    if counts.get("BOUNDARY_DOMINATED", 0) / total >= 0.5:
        return "BOUNDARY_DOMINATED"
    if counts.get("PROMISING", 0) / total >= 0.5:
        return "PROMISING"
    return "MIXED"


def posthoc_result(result: str) -> str:
    if result == "PROMISING":
        return "PROMISING_BUT_POSTHOC"
    if result == "MIXED":
        return "MIXED_BUT_POSTHOC"
    if result == "BOUNDARY_DOMINATED":
        return "BOUNDARY_DOMINATED"
    if result == "DEGENERATE":
        return "DEGENERATE"
    return "SCRIPT_NOT_REPAIRED"


def write_summary(
    path: str, rows: list[dict], command: str, expanded_kill_test_mode: bool
) -> None:
    counts = Counter(r["cheap_verdict"] for r in rows)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if rows:
        med_past_volume = median(r["past_volume"] for r in rows)
        med_future_volume = median(r["future_volume"] for r in rows)
        med_volume_asymmetry = median(r["volume_asymmetry"] for r in rows)
        med_depth_asymmetry = median(r["depth_asymmetry"] for r in rows)
    else:
        med_past_volume = med_future_volume = 0
        med_volume_asymmetry = med_depth_asymmetry = float("nan")
    result = overall_result(counts)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("# PRESENT_ANCHOR_SANITY_PILOT_V2_SUMMARY\n\n")
        fh.write("STATUS: PRIVATE_EXPLORATORY\n\n")
        fh.write("SCOPE: DIAGNOSTIC_ONLY\n\n")
        fh.write("POSTHOC_REPAIR=YES\n\n")
        fh.write("CHEAP_VERDICT_VERSION=v2_proxy_separated\n\n")
        fh.write(f"expanded_kill_test_mode={expanded_kill_test_mode}\n\n")
        fh.write("KBEAM_USED=NO\n\n")
        fh.write(f"COMMAND={command}\n\n")
        fh.write("## Status of v2\n\n")
        fh.write("- v2 repairs a diagnostic scale bug found after v1.\n")
        fh.write("- v2 is not a clean preregistered result.\n")
        fh.write("- v2 may be used only to decide whether a future clean preregistered pilot is worth designing.\n\n")
        fh.write("| metric | value |\n")
        fh.write("|---|---|\n")
        fh.write(f"| n_runs | {len(set(r['seed'] for r in rows)) if rows else 0} |\n")
        fh.write(f"| n_anchors | {len(rows)} |\n")
        fh.write(f"| median_past_volume | {med_past_volume} |\n")
        fh.write(f"| median_future_volume | {med_future_volume} |\n")
        fh.write(f"| median_volume_asymmetry | {fmt_float(med_volume_asymmetry)} |\n")
        fh.write(f"| median_depth_asymmetry | {fmt_float(med_depth_asymmetry)} |\n")
        fh.write(f"| verdict_counts | {dict(sorted(counts.items()))} |\n\n")
        fh.write(f"PRESENT_ANCHOR_SANITY_RESULT={result}\n\n")
        fh.write(f"PRESENT_ANCHOR_V2_RESULT={posthoc_result(result)}\n\n")
        fh.write("INTERPRETATION_LIMITS:\n\n")
        fh.write("- No horizon claim.\n")
        fh.write("- No order-only recoverability claim.\n")
        fh.write("- No uncertainty-principle claim.\n")
        fh.write("- No universality claim.\n")


def write_csv(path: str, rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", default=",".join(str(s) for s in DEFAULT_SEEDS))
    ap.add_argument("--intensity", type=float, default=DEFAULT_INTENSITY)
    ap.add_argument("--t-edge", type=float, default=DEFAULT_T_EDGE)
    ap.add_argument("--max-anchors-per-rule", type=int, default=DEFAULT_MAX_ANCHORS_PER_RULE)
    ap.add_argument("--csv-out", default=DEFAULT_CSV)
    ap.add_argument("--summary-out", default=DEFAULT_SUMMARY)
    ap.add_argument("--output", dest="csv_out", help="alias for --csv-out")
    ap.add_argument("--summary-output", dest="summary_out", help="alias for --summary-out")
    ap.add_argument("--allow-expanded-kill-test", action="store_true")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    seeds = tuple(int(x) for x in args.seeds.split(",") if x.strip())
    max_seeds = EXPANDED_KILL_TEST_MAX_SEEDS if args.allow_expanded_kill_test else DEFAULT_MAX_SEEDS
    max_anchors = (
        EXPANDED_KILL_TEST_MAX_ANCHORS_PER_RULE
        if args.allow_expanded_kill_test
        else DEFAULT_MAX_ANCHORS_PER_RULE
    )
    if len(seeds) > max_seeds:
        raise ValueError(f"sanity pilot is capped at {max_seeds} seeds")
    if args.max_anchors_per_rule > max_anchors:
        raise ValueError(f"sanity pilot is capped at {max_anchors} anchors per rule")
    rows: list[dict] = []
    for seed in seeds:
        rows.extend(rows_for_seed(seed, args.intensity, args.t_edge, args.max_anchors_per_rule))
    write_csv(args.csv_out, rows)
    command = " ".join(sys.argv)
    write_summary(args.summary_out, rows, command, args.allow_expanded_kill_test)
    counts = Counter(r["cheap_verdict"] for r in rows)
    result = overall_result(counts)
    print("PRESENT_ANCHOR_SANITY_PILOT v2 complete")
    print(f"csv={args.csv_out}")
    print(f"summary={args.summary_out}")
    print(f"n_runs={len(seeds)}")
    print(f"n_anchors={len(rows)}")
    print(f"verdict_counts={dict(sorted(counts.items()))}")
    print(f"PRESENT_ANCHOR_SANITY_RESULT={result}")
    print(f"PRESENT_ANCHOR_V2_RESULT={posthoc_result(result)}")
    print("PRIVATE_EXPLORATORY=YES")
    print("DIAGNOSTIC_ONLY=YES")
    print("POSTHOC_REPAIR=YES")
    print("NO_KBEAM_BY_DEFAULT=YES")


if __name__ == "__main__":
    main()
