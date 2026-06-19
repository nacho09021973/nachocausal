"""Minz-free poset checksum: the accelerator's output at the fixed gate config
must still match the checksum recorded when bit-for-bit Minz agreement was
verified (nachocausal/fixtures/gate_evidence.json). Fast (N=424); guards against
silent accelerator drift without needing the Minz clone (cmte SWE MAJOR-2).
"""

import hashlib
import json
import os

import numpy as np
import pytest

from nachocausal import generator, thresholds

EV = os.path.join(os.path.dirname(__file__), "..", "nachocausal", "fixtures",
                  "gate_evidence.json")

pytestmark = pytest.mark.skipif(
    np.__version__ != thresholds.PINNED_NUMPY,
    reason=f"checksum sealed under numpy=={thresholds.PINNED_NUMPY}",
)


@pytest.mark.parametrize("kind", ["BH", "MINK"])
def test_fast_poset_matches_gate_evidence(kind):
    ev = json.load(open(EV))["small_N_gate"][kind]
    emb, _, _ = generator.numpy_sprinkle(ev["seed"], ev["intensity"])
    C = generator.past_matrix_fast(emb, kind)
    chk = hashlib.sha256(np.packbits(C).tobytes()).hexdigest()
    assert chk == ev["fast_poset_sha256"], f"{kind} accelerator poset drifted"
