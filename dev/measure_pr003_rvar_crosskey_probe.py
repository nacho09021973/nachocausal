#!/usr/bin/env python
"""R-VAR cross-key probe -- comité 020 §9 step 1 (falsifier's minimal falsification test).

Question: does the interval-DP's output/abstention depend on WHICH sort key orders the
maximal antichain? The prototype (dev/explore_rvar_interval_dp.py) switches the key on the
hidden kind label (MINK: u=t-r; BH: p=t+r) -- comité 020 §5 verified this as a live
NO_GROUND_TRUTH_LEAKAGE risk. This probe runs BOTH keys on BOTH kinds for one dev draw and
reports, per (kind, key): certificate PASS/FAIL, and on PASS the (lambda*, |D*|, A, B).

Falsifier's branch map (comité 020 §5, minimal falsification test):
  (a) certificate fails under the swapped key -> the abstain/OK boundary provably depends on
      the key choice, hence (as currently implemented, key chosen by label) on the hidden
      label -> leakage confirmed; DP blocked until an order-only key derivation is
      specified and frozen.
  (b) certificate passes but (lambda*, argmax) differ across keys -> the "same frozen
      object" claim is false as implemented (object is key-augmented).
  (c) certificate passes and results are identical -> key-invariance evidence; the leakage
      objection reduces to freezing any order-only ordering.

MEASUREMENT ONLY, CLAIM-INERT: dev seed 20240617, intensity 1500, no mu, no EXPLORE_POOL,
no VALIDATION_SEEDS, no threshold, no spec change.

Run: PYTHONPATH=. .venv/bin/python dev/measure_pr003_rvar_crosskey_probe.py
Output: dev/rvar_crosskey_probe_result.json (+ this stdout log).
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_rvar_interval_dp import solve  # noqa: E402  (committed prototype under test)

from nachocausal import generator, thresholds  # noqa: E402

RESULT_PATH = os.path.join(os.path.dirname(__file__), "rvar_crosskey_probe_result.json")
DEV_SEED = 20240617
INTENSITY = 1500.0


def run_one(kind: str, key_name: str) -> dict:
    emb, _, _ = generator.numpy_sprinkle(DEV_SEED, INTENSITY)
    C = generator.past_matrix_fast(emb, kind)
    t, r = emb[:, 0], emb[:, 1]
    maximal = np.flatnonzero(~C.any(axis=0))
    key = (t[maximal] - r[maximal]) if key_name == "u=t-r" else (t[maximal] + r[maximal])
    try:
        out = solve(C, key)
    except AssertionError as e:
        return dict(kind=kind, key=key_name, certificate="FAIL", detail=str(e))
    row = dict(kind=kind, key=key_name, certificate="PASS", status=out["status"], K=out["K"])
    if out["status"] == "OK":
        row.update(
            lambda_star=str(out["lam"]), size_D=int(out["D"].sum()), A=out["A"], B=out["B"]
        )
    return row


def main() -> None:
    thresholds.assert_environment()
    rows = [
        run_one("BH", "p=t+r"),    # prototype's own BH key (baseline)
        run_one("BH", "u=t-r"),    # falsifier's swap: MINK key on BH
        run_one("MINK", "u=t-r"),  # prototype's own MINK key (baseline)
        run_one("MINK", "p=t+r"),  # swap: BH key on MINK
    ]
    for row in rows:
        print(row)

    bh_swap = next(r for r in rows if r["kind"] == "BH" and r["key"] == "u=t-r")
    bh_base = next(r for r in rows if r["kind"] == "BH" and r["key"] == "p=t+r")
    if bh_swap["certificate"] == "FAIL":
        branch = "a"
        verdict = ("KEY_DEPENDENCE_CONFIRMED: the abstain/OK boundary depends on the sort key; "
                   "with the key currently chosen by the hidden kind label, this is a "
                   "NO_GROUND_TRUTH_LEAKAGE violation as implemented. DP blocked until an "
                   "order-only key derivation is specified and frozen (comité 020 §8(2)(a)).")
    elif (bh_swap.get("lambda_star"), bh_swap.get("size_D")) != (
        bh_base.get("lambda_star"), bh_base.get("size_D")
    ):
        branch = "b"
        verdict = "SAME_OBJECT_CLAIM_FALSE: results differ across keys (key-augmented object)."
    else:
        branch = "c"
        verdict = "KEY_INVARIANCE_EVIDENCE: identical results; freeze any order-only ordering."

    output = dict(
        scope=("MEASUREMENT_ONLY -- comité 020 §9 step 1 (falsifier's minimal test); "
               "claim-inert; no mu, no seed-band consumption, no spec change"),
        dev_seed=DEV_SEED, intensity=INTENSITY, rows=rows,
        branch=branch, verdict=verdict,
    )
    with open(RESULT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nBRANCH=({branch})  {verdict}")
    print(f"Wrote {RESULT_PATH}")


if __name__ == "__main__":
    main()
