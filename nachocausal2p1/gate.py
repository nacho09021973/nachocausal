"""GATE — estimator-v2 tau(n) abstaining gate for the 2+1 bench (CANDIDATE, not frozen).

Same semantics as the sealed nachocausal.gate: abstain (no boundary claimed) iff
improvement(O_min) < tau(n), n = number of minimal elements; n < 2 abstains.
The table is fixtures/tau_table_2p1.json: scripts/gen_tau_table.build_tau UNCHANGED, one shared
rng, n ascending from 2 to 256, 40000 reps; n <= 128 is bit-equal to the sealed 1+1 table
(comité 052 §9 step 1; dev/PREREG004_STEPS_1_2_2026-10-13.md). The file's SHA256 must equal
thresholds.TAU_FIXTURE_SHA256. n > 256 RAISES: the run aborts, it never extrapolates.
Order-only; imports nothing from the scoring subpackage.
"""

from __future__ import annotations

import hashlib
import json
import os
from functools import lru_cache
from typing import Dict

from . import thresholds

TAU_PATH = os.path.join(os.path.dirname(__file__), "fixtures", "tau_table_2p1.json")


@lru_cache(maxsize=1)
def _tau_table() -> Dict[int, float]:
    with open(TAU_PATH, "rb") as f:
        raw = f.read()
    sha = hashlib.sha256(raw).hexdigest()
    if sha != thresholds.TAU_FIXTURE_SHA256:
        raise RuntimeError(f"tau_table_2p1.json SHA256 {sha} != {thresholds.TAU_FIXTURE_SHA256}")
    doc = json.loads(raw)
    p = doc["params"]
    if not (p["alpha"] == thresholds.GATE_ALPHA
            and p["mc_seed"] == thresholds.GATE_NULL_MC_SEED
            and p["mc_reps"] == thresholds.GATE_NULL_MC_REPS
            and p["n_max"] == thresholds.GATE_TAU_N_MAX):
        raise RuntimeError(f"tau_table_2p1.json params {p} drifted from thresholds")
    return {int(k): float(v) for k, v in doc["tau"].items()}


def tau(n: int) -> float:
    """tau(n) for n in [2, 256]; RAISES outside (abort, never extrapolate)."""
    table = _tau_table()
    if n in table:
        return table[n]
    raise ValueError(f"tau(n) requested for n={n} outside [2, {thresholds.GATE_TAU_N_MAX}]: "
                     "the 2+1 run must ABORT (comité 052 step 1).")


def abstains(improvement_value: float, n: int) -> bool:
    if n < 2:
        return True
    return improvement_value < tau(n)
