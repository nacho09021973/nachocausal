#!/usr/bin/env python
"""R-VAR EGS-object falsification test -- comite_decision_021 SS5/SS9 step 1.

MEASUREMENT ONLY, dev/, CLAIM-INERT. Zero NEW seed consumption: reuses the exact
three dev seeds (20240617, 13, 101) already drawn for the structure probe
(dev/measure_pr003_rvar_structure_probe.py, commit 6347459) at all 4 frozen
production intensities. No mu, no spec freeze, no EXPLORE_POOL, no
VALIDATION_SEEDS, no threshold frozen, no reconstruction claim.

Computes, order-only (no auxiliary sort key, no coordinate enters the statistic
itself -- coordinates are used ONLY to label points for the diagnostic split
below, exactly as the structure probe scored kind/geometry post hoc):

  L(i)          = length (in edges) of the longest chain starting at minimal
                  element i, i.e. i = x_0 < x_1 < ... < x_k. Computed via the
                  standard DAG-longest-path recursion H(i) = 1 + max_{j in
                  future(i)} H(j) (0 if future(i) is empty), using the FULL
                  transitively-closed relation C -- this gives the exact same
                  value as recursing over covers only (a dominated-successor
                  argument), so no separate cover computation is needed.
  future_card(i) = |future(i)| = C[:, i].sum() = the sealed O_min(i) restricted
                  to i in Min(C) (docs/estimator_v2_freeze.md:34-37). Computed
                  here ONLY as the labelled secondary/diagnostic variant, per
                  comite_decision_021 SS8 -- NEVER promoted to primary.

The two questions this test attacks (falsifier, comite_decision_021 SS5,
"Minimal falsification test"):

  (a) Is the MINK null degenerate on THIS box geometry? EGS's non-degeneracy
      evidence ("varies between n and sqrt(n) already for Minkowski") is
      textually scoped to a CAUSAL DIAMOND (literature-verifier, SS7), not this
      project's frozen TALL BOX (T_EDGE=6.0 >> R_EDGE=1.2). If every MINK
      minimal's future is nearly the whole set (the same mechanism that
      certified A(C)=EMPTY 12/12 for MINK, commit 6347459), L(i) and
      future_card(i) should cluster tightly (near-zero spread) across Min(C)
      -- degeneracy dressed as gradedness.
  (b) Does the BH interior-mode occupancy SCALE with n_min across the four
      frozen intensities, or does it stay roughly CONSTANT (the corner-artifact
      signature that killed the prior A(C) object's argmax, comite_020 SS4:
      |D*|~=N-few, B in {3..8} independent of N)?

No accept/reject threshold is frozen by this script -- that is Gate 0's job,
per NO_POST_HOC_TUNING (a floor invented after seeing this data would itself be
a forbidden move). This prints and records the raw diagnostics only.

Run: PYTHONPATH=. .venv/bin/python dev/measure_pr003_rvar_egs_falsification_test.py
Output: dev/rvar_egs_falsification_test_result.json (+ this stdout log).
"""
from __future__ import annotations

import json
import os
import platform
import subprocess
from datetime import datetime, timezone

import numpy as np

from nachocausal import generator, thresholds

DEV_SEEDS = (20240617, 13, 101)
RESULT_PATH = os.path.join(
    os.path.dirname(__file__), "rvar_egs_falsification_test_result.json"
)


def longest_chain_lengths(C: np.ndarray) -> np.ndarray:
    """H[i] = length (edges) of the longest chain i = x_0 < x_1 < ... < x_k.
    C[a, b] = True means b is in the past of a (b < a). future(i) = column i.
    Recursion uses the FULL transitive relation (not just covers) -- exact,
    since any non-cover successor is dominated by some cover successor's own
    H value (see module docstring)."""
    N = C.shape[0]
    H = np.zeros(N, dtype=np.int64)
    past_size = C.sum(axis=1)
    # Elements with larger past_size cannot be in the future of an element
    # with smaller past_size (i < j ==> past_size(i) < past_size(j)), so
    # processing in DESCENDING past_size order guarantees future(i) is
    # already resolved when we reach i.
    order = np.argsort(-past_size, kind="stable")
    for i in order:
        fut_mask = C[:, i]
        if fut_mask.any():
            H[i] = 1 + H[fut_mask].max()
        else:
            H[i] = 0
    return H


def stats(x: np.ndarray) -> dict:
    x = np.asarray(x, dtype=float)
    mean = float(x.mean()) if len(x) else float("nan")
    std = float(x.std()) if len(x) else float("nan")
    return dict(
        n=int(len(x)),
        mean=mean,
        std=std,
        cv=(std / mean) if mean > 0 else None,
        min=float(x.min()) if len(x) else None,
        max=float(x.max()) if len(x) else None,
    )


def cohens_d(a: np.ndarray, b: np.ndarray) -> float | None:
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    if len(a) < 2 or len(b) < 2:
        return None
    pooled_std = np.sqrt(((a.std(ddof=1) ** 2) + (b.std(ddof=1) ** 2)) / 2)
    if pooled_std == 0:
        return None
    return float((b.mean() - a.mean()) / pooled_std)


def main() -> None:
    thresholds.assert_environment()
    rows = []
    for kind in ("MINK", "BH"):
        for intensity in thresholds.INTENSITIES:
            for seed in DEV_SEEDS:
                emb, _, _ = generator.numpy_sprinkle(seed, intensity)
                C = generator.past_matrix_fast(emb, kind)
                t, r = emb[:, 0], emb[:, 1]

                minimal = np.flatnonzero(~C.any(axis=1))
                H = longest_chain_lengths(C)
                L_min = H[minimal]
                future_card_min = C[:, minimal].sum(axis=0)

                row = dict(
                    kind=kind, intensity=intensity, seed=seed,
                    N=int(emb.shape[0]), n_min=int(len(minimal)),
                    L_minimal=stats(L_min),
                    future_card_minimal=stats(future_card_min),
                )

                if kind == "BH":
                    r_min = r[minimal]
                    interior_mask = r_min < thresholds.R_S
                    n_interior = int(interior_mask.sum())
                    n_exterior = int(len(minimal) - n_interior)
                    row["interior_diagnostic"] = dict(
                        note="r used ONLY as a post-hoc diagnostic label here, "
                             "never as input to L() or future_card(); scoring-only "
                             "per NO_GROUND_TRUTH_LEAKAGE",
                        n_interior=n_interior,
                        n_exterior=n_exterior,
                        interior_fraction=(n_interior / len(minimal)) if len(minimal) else None,
                        expected_geometric_fraction=(thresholds.R_S - 0.1) / thresholds.R_EDGE,
                        L_interior=stats(L_min[interior_mask]),
                        L_exterior=stats(L_min[~interior_mask]),
                        L_cohens_d_ext_minus_int=cohens_d(L_min[interior_mask], L_min[~interior_mask]),
                        future_card_interior=stats(future_card_min[interior_mask]),
                        future_card_exterior=stats(future_card_min[~interior_mask]),
                        future_card_cohens_d_ext_minus_int=cohens_d(
                            future_card_min[interior_mask], future_card_min[~interior_mask]
                        ),
                    )

                rows.append(row)
                extra = ""
                if kind == "BH":
                    d = row["interior_diagnostic"]
                    extra = (f"  n_interior={d['n_interior']:3d} n_exterior={d['n_exterior']:3d} "
                             f"frac={d['interior_fraction']:.3f} "
                             f"L_d={d['L_cohens_d_ext_minus_int']}")
                print(f"[{kind:4s} I={intensity:>7.0f} seed={seed:8d}] N={row['N']:6d} "
                      f"n_min={row['n_min']:3d} "
                      f"L_cv={row['L_minimal']['cv']} "
                      f"fc_cv={row['future_card_minimal']['cv']}{extra}")

    # Aggregate per-intensity views (across the 3 dev seeds) for the two
    # falsifiable questions -- no accept/reject threshold is asserted here.
    mink_cv_by_intensity = {}
    bh_interior_by_intensity = {}
    for intensity in thresholds.INTENSITIES:
        mink_rows = [r for r in rows if r["kind"] == "MINK" and r["intensity"] == intensity]
        mink_cv_by_intensity[str(intensity)] = dict(
            L_cv=[r["L_minimal"]["cv"] for r in mink_rows],
            future_card_cv=[r["future_card_minimal"]["cv"] for r in mink_rows],
        )
        bh_rows = [r for r in rows if r["kind"] == "BH" and r["intensity"] == intensity]
        bh_interior_by_intensity[str(intensity)] = dict(
            n_min=[r["n_min"] for r in bh_rows],
            n_interior=[r["interior_diagnostic"]["n_interior"] for r in bh_rows],
            interior_fraction=[r["interior_diagnostic"]["interior_fraction"] for r in bh_rows],
        )

    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=os.path.dirname(__file__)
        ).decode().strip()
    except Exception:
        commit = "[UNVERIFIED -- git rev-parse failed]"

    output = dict(
        scope=("MEASUREMENT_ONLY -- falsification test per comite_decision_021 SS5/SS9 "
               "step 1; dev seeds only, ZERO NEW seed consumption (reuses the three dev "
               "seeds already drawn in commit 6347459); no mu, no spec freeze, no "
               "EXPLORE_POOL/VALIDATION_SEEDS, no threshold frozen here, no "
               "reconstruction claim. Interior/exterior labels use r as a POST-HOC "
               "diagnostic only, never as input to L() or future_card()."),
        dev_seeds=list(DEV_SEEDS),
        provenance=dict(
            git_commit=commit,
            numpy_version=np.__version__,
            uname=platform.uname()._asdict(),
            timestamp_utc=datetime.now(timezone.utc).isoformat(),
        ),
        rows=rows,
        summary=dict(
            mink_cv_by_intensity=mink_cv_by_intensity,
            bh_interior_occupancy_by_intensity=bh_interior_by_intensity,
            note=("No non-degeneracy floor or scaling-law acceptance threshold is "
                  "asserted by this script (that would be NO_POST_HOC_TUNING if "
                  "invented after seeing these numbers). Read mink_cv_by_intensity: "
                  "values near 0 across all levels indicate a near-degenerate MINK "
                  "null (falsifier failure mode 1). Read "
                  "bh_interior_occupancy_by_intensity: n_interior tracking "
                  "interior_fraction*n_min roughly constant across intensities while "
                  "n_min itself grows 13-21 -> 64-73 indicates SCALING (candidate "
                  "survives); n_interior staying roughly CONSTANT in absolute count "
                  "indicates a corner-artifact redux (falsifier failure mode 2)."),
        ),
    )
    with open(RESULT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nWrote {RESULT_PATH}")


if __name__ == "__main__":
    main()
