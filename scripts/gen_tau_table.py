"""Regenerate the FROZEN tau(n) gate table -> nachocausal/fixtures/tau_table.json.

tau(n) = the (1 - GATE_ALPHA) quantile of `improvement` under an abstract
Uniform[0,1] null at matched n, by Monte Carlo with the FROZEN parameters in
thresholds.py. The procedure is fully specified and reproducible:

  * a SINGLE rng = numpy.random.default_rng(GATE_NULL_MC_SEED);
  * n iterated ASCENDING and CONTIGUOUS over [2, GATE_TAU_N_MAX] (no skips), so
    the table is deterministic and append-only when N_MAX is raised;
  * for each n: GATE_NULL_MC_REPS draws of rng.random(n), tau = quantile p(1-alpha)
    of estimator.improvement over those reps.

Data-independent: no project seeds, no sprinkling, no ground truth. The committed
fixture records the params so the loader (nachocausal/gate.py) can refuse a table
whose params drift from the sealed thresholds. tests/test_tau_table.py regenerates
a small-n prefix and asserts bit-equality with the committed fixture.

Run:  python3 scripts/gen_tau_table.py
"""

from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import estimator, thresholds  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "nachocausal", "fixtures", "tau_table.json")


def build_tau(n_max: int, alpha: float, mc_seed: int, mc_reps: int) -> dict:
    """One shared rng, n ascending contiguous 2..n_max. Returns {n: tau(n)}."""
    rng = np.random.default_rng(mc_seed)
    q = 1.0 - alpha
    tau = {}
    for n in range(2, n_max + 1):
        vals = np.fromiter(
            (estimator.improvement(rng.random(n)) for _ in range(mc_reps)),
            dtype=float, count=mc_reps)
        tau[n] = float(np.quantile(vals, q))
    return tau


def main() -> None:
    tau = build_tau(thresholds.GATE_TAU_N_MAX, thresholds.GATE_ALPHA,
                    thresholds.GATE_NULL_MC_SEED, thresholds.GATE_NULL_MC_REPS)
    doc = {
        "_comment": "FROZEN tau(n) gate table; regenerate via scripts/gen_tau_table.py",
        "params": {
            "alpha": thresholds.GATE_ALPHA,
            "mc_seed": thresholds.GATE_NULL_MC_SEED,
            "mc_reps": thresholds.GATE_NULL_MC_REPS,
            "n_max": thresholds.GATE_TAU_N_MAX,
            "null": "uniform01",
            "rng": "single default_rng(mc_seed), n ascending contiguous 2..n_max",
            "statistic": "estimator.improvement (1 - SSE2/SSE1, best 1D 2-means)",
        },
        "tau": {str(n): v for n, v in tau.items()},
    }
    with open(OUT, "w") as f:
        json.dump(doc, f, indent=1)
    lo = ", ".join(f"{n}:{tau[n]:.4f}" for n in (2, 16, 40, 71, 128) if n in tau)
    print(f"wrote {OUT}  (n=2..{thresholds.GATE_TAU_N_MAX}; sample {lo})")


if __name__ == "__main__":
    main()
