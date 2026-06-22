"""GATE — estimator-v2 tau(n) abstaining gate (FROZEN; freeze cl. C).

Order-only: it sees the order-derived `improvement` statistic and the minimal-
element count `n`, never the embedding. Imports nothing from nachocausal.scoring.
The frozen tau(n) table lives in fixtures/tau_table.json (regenerate with
scripts/gen_tau_table.py); this module loads it and refuses a table whose Monte
Carlo parameters drift from the sealed thresholds.

Semantics: a causet ABSTAINS (no boundary claimed; sep -> 0) iff
    improvement(O_min) < tau(n).
n < 2 cannot define a 2-partition -> abstain.
"""

from __future__ import annotations

import json
import os
from functools import lru_cache
from typing import Dict

from . import thresholds

_TAU_PATH = os.path.join(os.path.dirname(__file__), "fixtures", "tau_table.json")


@lru_cache(maxsize=1)
def _tau_table() -> Dict[int, float]:
    with open(_TAU_PATH) as f:
        doc = json.load(f)
    p = doc["params"]
    if not (p["alpha"] == thresholds.GATE_ALPHA
            and p["mc_seed"] == thresholds.GATE_NULL_MC_SEED
            and p["mc_reps"] == thresholds.GATE_NULL_MC_REPS
            and p["n_max"] == thresholds.GATE_TAU_N_MAX):
        raise RuntimeError(
            "tau_table.json params drifted from sealed thresholds "
            f"(file {p} vs thresholds alpha={thresholds.GATE_ALPHA}, "
            f"seed={thresholds.GATE_NULL_MC_SEED}, reps={thresholds.GATE_NULL_MC_REPS}, "
            f"n_max={thresholds.GATE_TAU_N_MAX}); regenerate scripts/gen_tau_table.py.")
    return {int(k): float(v) for k, v in doc["tau"].items()}


def tau(n: int) -> float:
    """Frozen tau(n). RAISES if n is outside the table's [2, N_MAX] range."""
    table = _tau_table()
    if n in table:
        return table[n]
    raise ValueError(
        f"tau(n) requested for n={n} outside the frozen table [2, "
        f"{thresholds.GATE_TAU_N_MAX}]; raise GATE_TAU_N_MAX and regenerate.")


def abstains(improvement_value: float, n: int) -> bool:
    """True => abstain (no boundary claimed). n < 2 -> abstain (cannot split)."""
    if n < 2:
        return True
    return improvement_value < tau(n)
