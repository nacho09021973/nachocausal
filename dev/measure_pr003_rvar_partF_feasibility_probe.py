#!/usr/bin/env python
"""R-VAR Part F feasibility probe -- comité 019 §9 step 1 (docs/comite/
comite_decision_019_rvar-partF-execution-feasibility.md).

Authorized scope (PI, 2026-07-05): a measurement ONLY. This script does not
compute mu, does not run Part F step 3, does not touch EXPLORE_POOL or
VALIDATION_SEEDS, does not freeze any threshold, and makes no reconstruction
claim. It does not modify production/BH-patch tracks: MINK only, one draw per
intensity, on a documented dev seed outside EXPLORE_POOL (SEED=20240617
precedent, dev/gate_highN.py:20).

What it measures, per production intensity in thresholds.INTENSITIES:
  - N actually generated (the realized Poisson draw)
  - |Max(C)| (maximal antichain size) -- read directly off the already-
    verified, already-polynomial past_matrix_fast output (O(N) column scan,
    no new algorithm)
  - 2^|Max(C)| (log2 form when the exact value is too large to print)
  - number of Hasse cover relations, and the wall-clock time to compute them
    via a vectorized boolean-matmul transitive-reduction (a measurement-only
    reimplementation of gate0's is_cover loop, NOT adopted as the Part F
    algorithm -- see docstring note below)
  - an ANALYTICAL, deliberately optimistic lower bound on enumerate-and-filter
    wall time, from a raw itertools.combinations throughput benchmark. Per
    the falsifier's own instruction (comité 019 §5 "Minimal falsification
    test"), family_A itself is NEVER run at production N -- only a raw
    subset-generation rate is benchmarked, which is strictly cheaper per
    subset than family_A's actual downset+crossing_interface work. If even
    this optimistic floor is infeasible, the real cost is certainly worse.

Note on the cover computation: gate0's is_cover (dev/measure_pr003_rvar_gate0.py:50)
is pure-Python O(N^3) predicate calls, itself flagged by comité 019's falsifier
as a second, independent blocker. This script computes the identical Hasse
cover relation via vectorized numpy (boolean matmul transitive-reduction) so
that the |covers| measurement itself does not fall over before producing a
number. This reimplementation is a measurement probe only; it is not proposed
as -- and has not passed Gate 0 as -- a replacement for any Part F/D.2 code
path.

Run: .venv/bin/python dev/measure_pr003_rvar_partF_feasibility_probe.py
Output: dev/rvar_partF_feasibility_probe_result.json (+ this stdout log).
"""
from __future__ import annotations

import itertools
import json
import math
import os
import time

import numpy as np

from nachocausal import generator, thresholds

DEV_SEED = 20240617  # documented dev seed, disjoint from EXPLORE_POOL (1_000_000+)
RESULT_PATH = os.path.join(os.path.dirname(__file__), "rvar_partF_feasibility_probe_result.json")

# Optimistic subset-throughput floor: how many trivial itertools.combinations
# items/sec this benchmark reaches on THIS machine, calibrated once at a size
# that finishes in well under a second. Used only as a best-case divisor.
_BENCH_K = 20  # 2**20 ~ 1.05e6 trivial subsets -- calibration, not enumeration


def maximal_and_covers(C: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    """Max(C) (bool mask) and Hasse cover-relation matrix, both read off the
    already-verified past_matrix_fast poset C[i,j] == (j precedes i)."""
    maximal_mask = ~C.any(axis=0)  # x maximal iff no y has x in its past
    rel = C.T  # rel[x, y] == True iff x precedes y (strict, transitively closed)
    rel_f = rel.astype(np.float32)
    t0 = time.time()
    has_intermediate = (rel_f @ rel_f) > 0.5
    covers = rel & ~has_intermediate
    t_covers = time.time() - t0
    return maximal_mask, covers, t_covers


def calibrate_subset_rate() -> float:
    """Optimistic floor: raw combinations-of-20-items/sec, trivial per-item work."""
    items = list(range(_BENCH_K))
    t0 = time.time()
    count = 0
    for combo in itertools.combinations(items, _BENCH_K // 2):
        count += len(combo)
    elapsed = time.time() - t0
    total_subsets = math.comb(_BENCH_K, _BENCH_K // 2)
    return total_subsets / elapsed if elapsed > 0 else float("inf")


def format_huge(exponent_bits: int) -> str:
    """2**exponent_bits, printed exactly if small, else as a base-10 order of magnitude."""
    if exponent_bits <= 60:
        return str(2**exponent_bits)
    log10_val = exponent_bits * math.log10(2)
    return f"~10^{log10_val:.1f}"


def estimate_enum_seconds(max_size: int, subsets_per_sec: float) -> str:
    log10_subsets = max_size * math.log10(2)
    log10_seconds = log10_subsets - math.log10(subsets_per_sec)
    if log10_seconds < 2:
        return f"{10**log10_seconds:.3g} s"
    log10_years = log10_seconds - math.log10(365.25 * 24 * 3600)
    if log10_years < 0:
        return f"{10**log10_seconds:.3g} s"
    return f"~10^{log10_years:.1f} years"


def main() -> None:
    thresholds.assert_environment()
    subsets_per_sec = calibrate_subset_rate()
    print(f"[calibration] optimistic subset-generation floor: {subsets_per_sec:.3g} subsets/s "
          f"(raw itertools.combinations, trivial per-item work; family_A's real per-subset cost "
          f"-- downset + crossing_interface -- is strictly higher)")

    results = []
    for intensity in thresholds.INTENSITIES:
        embedding, edges, center = generator.numpy_sprinkle(DEV_SEED, intensity)
        N = embedding.shape[0]

        t0 = time.time()
        C = generator.past_matrix_fast(embedding, "MINK")
        t_pastmatrix = time.time() - t0

        maximal_mask, covers, t_covers = maximal_and_covers(C)
        max_size = int(maximal_mask.sum())
        num_covers = int(covers.sum())

        enum_2pow_repr = format_huge(max_size)
        est_time_repr = estimate_enum_seconds(max_size, subsets_per_sec)

        # Conservative per-level verdict from the arithmetic alone.
        log10_subsets = max_size * math.log10(2)
        if log10_subsets > 8:  # >~1e8 subsets: infeasible under any realistic per-subset cost
            level_verdict = "INFEASIBLE"
        elif log10_subsets > 5:
            level_verdict = "MARGINAL"
        else:
            level_verdict = "FEASIBLE_TO_REQUEST_PARTF"

        row = dict(
            intensity=intensity,
            N_generated=N,
            max_size=max_size,
            enum_2pow=enum_2pow_repr,
            log2_enum=max_size,
            num_covers=num_covers,
            t_pastmatrix_s=round(t_pastmatrix, 4),
            t_covers_s=round(t_covers, 4),
            est_enum_and_filter_time_optimistic_floor=est_time_repr,
            level_verdict=level_verdict,
        )
        results.append(row)
        print(f"[intensity={intensity:>7.0f}] N={N:6d}  |Max(C)|={max_size:5d}  "
              f"2^|Max|={enum_2pow_repr:>10s}  |covers|={num_covers:7d}  "
              f"t_pastmatrix={t_pastmatrix:.3f}s  t_covers={t_covers:.3f}s  "
              f"est_enum_time(optimistic)={est_time_repr}  verdict={level_verdict}")

    infeasible_count = sum(1 for r in results if r["level_verdict"] == "INFEASIBLE")
    if infeasible_count == len(results):
        overall_verdict = "INFEASIBLE"
    elif infeasible_count > 0:
        overall_verdict = "INFEASIBLE"  # any production level failing blocks the frozen 4-level table
    elif any(r["level_verdict"] == "MARGINAL" for r in results):
        overall_verdict = "NEEDS_ALGORITHM_REDESIGN"
    else:
        overall_verdict = "FEASIBLE_TO_REQUEST_PARTF"

    output = dict(
        scope="MEASUREMENT_ONLY -- comité 019 §9 step 1; NOT Part F step 3; NO mu computed",
        dev_seed=DEV_SEED,
        subsets_per_sec_optimistic_floor=subsets_per_sec,
        levels=results,
        overall_verdict=overall_verdict,
    )
    with open(RESULT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nOVERALL_VERDICT={overall_verdict}")
    print(f"Wrote {RESULT_PATH}")


if __name__ == "__main__":
    main()
