"""prereg-004 step 1: tau(n) for the 2+1 front by the SEALED procedure, extended to n_max = 256.

Committee 052 (docs/comite/comite_decision_052_prereg004-2p1-design.md, §9 step 1): regenerate
tau(n) with scripts/gen_tau_table.build_tau UNCHANGED (one shared rng = default_rng(
GATE_NULL_MC_SEED), n ascending and contiguous from 2, GATE_NULL_MC_REPS reps, alpha =
GATE_ALPHA), so n <= 128 must reproduce nachocausal/fixtures/tau_table.json bit for bit and
n in [129, 256] is the contiguous continuation of the same stream.
n_max = 256: the largest n_minimal seen in any dev 2+1 realisation is 184 (rho = 126, any T);
256 leaves a 39% margin.  A blind-run n above n_max must abort, never extrapolate.
Run in the SEALED .venv (numpy 1.26.4).  Output is a dev candidate, not yet a sealed fixture.
Usage: .venv/bin/python dev/gen_tau_table_2p1.py
"""
import hashlib
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "scripts"))
import numpy as np  # noqa: E402
from nachocausal import thresholds  # noqa: E402
import gen_tau_table as g  # noqa: E402

N_MAX = 256
OUT = ROOT / "dev" / "tau_table_2p1_candidate_2026-10-13.json"


def main():
    assert np.__version__ == thresholds.PINNED_NUMPY, np.__version__
    t0 = time.time()
    tau = g.build_tau(N_MAX, thresholds.GATE_ALPHA, thresholds.GATE_NULL_MC_SEED,
                      thresholds.GATE_NULL_MC_REPS)
    sealed = json.loads((ROOT / "nachocausal" / "fixtures" / "tau_table.json").read_text())["tau"]
    mism = [n for n in range(2, 129) if tau[n] != float(sealed[str(n)])]
    assert not mism, "n <= 128 differs from the sealed fixture at %s" % mism[:5]
    doc = {"params": {"alpha": thresholds.GATE_ALPHA, "mc_seed": thresholds.GATE_NULL_MC_SEED,
                      "mc_reps": thresholds.GATE_NULL_MC_REPS, "n_max": N_MAX,
                      "procedure": "scripts/gen_tau_table.build_tau, unchanged"},
           "n_le_128_bit_equal_to_sealed": True,
           "seconds": round(time.time() - t0, 1),
           "tau": {str(n): v for n, v in tau.items()}}
    OUT.write_text(json.dumps(doc, indent=1) + "\n")
    print("ok", OUT, "sha256", hashlib.sha256(OUT.read_bytes()).hexdigest(), "seconds", doc["seconds"])


if __name__ == "__main__":
    main()
