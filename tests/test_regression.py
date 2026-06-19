"""Bit-exact regression: the SEALED package must reproduce the 64 audited O
multisets in nachocausal/fixtures/o_samples.json (the dev oracle that an
independent audit re-derived 0/64 mismatch, PHASE0_NOTES.md:98). This proves the
"lift out of dev" did not drift the estimator/accelerator (cmte SWE MAJOR-1).

Requires numpy==1.26.4 (the sealed environment); skips otherwise so the suite is
informative rather than red on a wrong interpreter.
"""

import json
import os

import numpy as np
import pytest

from nachocausal import estimator, generator, thresholds

FIX = os.path.join(os.path.dirname(__file__), "..", "nachocausal", "fixtures",
                   "o_samples.json")

pytestmark = pytest.mark.skipif(
    np.__version__ != thresholds.PINNED_NUMPY,
    reason=f"oracle was sealed under numpy=={thresholds.PINNED_NUMPY}",
)


def test_o_multisets_bit_exact():
    records = json.load(open(FIX))
    assert len(records) == 64
    # Cache one sprinkle per (seed, intensity); both kinds share the cloud.
    cache = {}
    mismatches = []
    for rec in records:
        key = (rec["seed"], rec["intensity"])
        if key not in cache:
            emb, _, _ = generator.numpy_sprinkle(rec["seed"], rec["intensity"])
            cache[key] = emb
        emb = cache[key]
        assert emb.shape[0] == rec["N"], f"N drift {key}: {emb.shape[0]} vs {rec['N']}"
        C = generator.past_matrix_fast(emb, rec["kind"])
        O_by_min, _, _ = estimator.estimate_O(C)
        got = [int(v) for v in O_by_min.values()]
        if got != rec["O"]:
            mismatches.append((rec["kind"], rec["seed"], rec["intensity"]))
    assert not mismatches, f"O multiset drift in {len(mismatches)} records: {mismatches[:5]}"
