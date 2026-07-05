#!/usr/bin/env python
"""R-VAR structure probe -- order-theoretic structure of production-scale patches.

Follow-up to the Part F feasibility probe (dev/PR003_RVAR_PARTF_FEASIBILITY_PROBE_REPORT.md)
and to comité 019 §9 (docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md).
MEASUREMENT ONLY: no μ, no Part F step 3, no EXPLORE_POOL / VALIDATION_SEEDS, no threshold
frozen, no reconstruction claim. Dev seeds 20240617/13/101 (precedent: dev/sweep_o.py),
MINK and BH, the 4 production intensities, read-only against the sealed generator.

Two structural questions, each with a per-draw certificate:

(A) INTERVAL PROPERTY. For each element v, is I_v = {m in Max(C) : v <= m} a CONTIGUOUS
    interval of the maximal antichain under a null-coordinate sort? (Theorem for MINK:
    1+1D Minkowski sprinkling = dominance order in (u,v)=(t-r,t+r), and an up-set
    intersected with an antichain of a 2D order is a suffix-cap-prefix = interval.
    Empirical question for BH-EF, where the outgoing null coordinate flips inside the
    horizon.) This is the load-bearing precondition for the polynomial gap-DP candidate
    (dev/explore_rvar_interval_dp.py): if I_v is an interval, the A(C)-restricted
    optimisation reduces to an O(K^2) DP instead of the 2^K enumeration.

(B) EMPTY-FAMILY CERTIFICATE. A(C) requires (C-D) & Min != empty for D = downset(M),
    M subset of Max nonempty. If EVERY minimal element lies below EVERY maximal element,
    then downset(M) contains all of Min for any nonempty M, hence A(C) = EMPTY -- certified
    by counting unrelated (min, max) pairs on the past matrix, O(|Min|*|Max|) lookups,
    no enumeration. Conversely, minimals with a PARTIAL interval are what make A(C)
    potentially nonempty.

Run: PYTHONPATH=. .venv/bin/python dev/measure_pr003_rvar_structure_probe.py
Output: dev/rvar_structure_probe_result.json (+ this stdout log).
"""
from __future__ import annotations

import json
import os

import numpy as np

from nachocausal import generator, thresholds

DEV_SEEDS = (20240617, 13, 101)
RESULT_PATH = os.path.join(os.path.dirname(__file__), "rvar_structure_probe_result.json")


def interval_violations(C: np.ndarray, order_idx: np.ndarray) -> tuple[int, int]:
    """Count elements v whose I_v (reflexive up-set within Max, in the candidate sorted
    order) is nonempty and NOT contiguous; also count empty I_v (must be 0: every element
    lies below-or-equal some maximal element)."""
    K = len(order_idx)
    U = C[order_idx, :].copy()  # U[k, v] = v strictly below k-th maximal (C[i,j]=j in past of i)
    U[np.arange(K), order_idx] = True  # reflexive
    counts = U.sum(axis=0)
    pos = np.arange(K)[:, None]
    first = np.where(U, pos, K).min(axis=0)
    last = np.where(U, pos, -1).max(axis=0)
    noncontig = int(np.count_nonzero((counts > 0) & ((last - first + 1) != counts)))
    empty = int(np.count_nonzero(counts == 0))
    return noncontig, empty


def main() -> None:
    thresholds.assert_environment()
    rows = []
    func = lambda r: r + 2.0 * thresholds.R_S * np.log(np.abs(r - thresholds.R_S) / thresholds.R_S)
    for kind in ("MINK", "BH"):
        for intensity in thresholds.INTENSITIES:
            for seed in DEV_SEEDS:
                emb, _, _ = generator.numpy_sprinkle(seed, intensity)
                C = generator.past_matrix_fast(emb, kind)
                t, r = emb[:, 0], emb[:, 1]
                maximal = np.flatnonzero(~C.any(axis=0))
                minimal = np.flatnonzero(~C.any(axis=1))
                K = len(maximal)

                # (A) interval property under candidate sorts
                sorts = {
                    "u=t-r": t[maximal] - r[maximal],       # outgoing null (MINK conjugate)
                    "p=t+r": t[maximal] + r[maximal],       # ingoing null (globally monotone in BH-EF)
                    "r": r[maximal],
                    "q=t-rstar": t[maximal] - func(r[maximal]),  # outgoing EF (flips inside horizon)
                }
                viol = {}
                empty_iv = None
                for name, key in sorts.items():
                    v, e = interval_violations(C, maximal[np.argsort(key)])
                    viol[name] = v
                    empty_iv = e  # sort-independent

                # (B) empty-family certificate
                rel = C[np.ix_(maximal, minimal)]  # rel[a,b] = minimal b below maximal a
                unrelated_pairs = int((~rel).sum())
                partial_minimals = int((~rel.all(axis=0)).sum())
                family_status = (
                    "EMPTY_CERTIFIED" if unrelated_pairs == 0 else "POSSIBLY_NONEMPTY"
                )

                row = dict(
                    kind=kind, intensity=intensity, seed=seed, N=int(emb.shape[0]),
                    n_min=int(len(minimal)), n_max=K,
                    interval_violations_per_sort=viol, empty_I_v=empty_iv,
                    unrelated_min_max_pairs=unrelated_pairs,
                    partial_interval_minimals=partial_minimals,
                    family_status=family_status,
                )
                rows.append(row)
                best_sort = min(viol, key=viol.get)
                print(f"[{kind:4s} I={intensity:>7.0f} seed={seed:8d}] N={row['N']:6d} "
                      f"K={K:3d} |Min|={row['n_min']:3d}  "
                      f"best_sort={best_sort}:{viol[best_sort]} viol  "
                      f"unrelated(min,max)={unrelated_pairs:6d}  "
                      f"partial-I_z minimals={partial_minimals:3d}  {family_status}")

    mink_all_empty = all(
        r["family_status"] == "EMPTY_CERTIFIED" for r in rows if r["kind"] == "MINK"
    )
    bh_all_partial = all(
        r["partial_interval_minimals"] == r["n_min"] for r in rows if r["kind"] == "BH"
    )
    interval_holds = all(
        min(r["interval_violations_per_sort"].values()) == 0 and r["empty_I_v"] == 0
        for r in rows
    )
    summary = dict(
        interval_property_holds_all_draws=interval_holds,
        mink_family_empty_certified_all_production_draws=mink_all_empty,
        bh_all_minimals_partial_interval_all_draws=bh_all_partial,
    )
    output = dict(
        scope=("MEASUREMENT_ONLY -- structural facts on dev seeds; no mu, no Part F, "
               "no seed-band consumption, no claim beyond the counted certificates"),
        dev_seeds=list(DEV_SEEDS),
        rows=rows,
        summary=summary,
    )
    with open(RESULT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print("\nSUMMARY:")
    for k, v in summary.items():
        print(f"  {k} = {v}")
    print(f"Wrote {RESULT_PATH}")


if __name__ == "__main__":
    main()
