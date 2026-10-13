"""Re-gate the dev 2+1 v2 sweeps with the step-1 tau table (comité 052 §5: "no BH or MINK verdict
may flip"). Generator of the numbers in dev/PREREG004_STEPS_1_2_2026-10-13.md (Paso 1, "Decisiones
de dev recalculadas"); added after auditor report 043, warning 3.

For every BH and MINK record in the two v2 sweeps: new decision = improvement < tau_new(n_minimal)
(improvement as stored, 4 decimals), compared with the recorded dev decision.
Usage: .venv/bin/python dev/regate_2p1_sweeps.py
Expected (2026-10-13): decisions 360  n>128 69  flips 0  min_margin 0.0358
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAU = ROOT / "nachocausal2p1" / "fixtures" / "tau_table_2p1.json"
SWEEPS = ("dev/2p1_sweep_T_v2_2026-10-12.jsonl", "dev/2p1_sweep_T_rho126_v2_2026-10-12.jsonl")


def main():
    tau = {int(k): float(v) for k, v in json.load(open(TAU))["tau"].items()}
    n = big = flips = 0
    margin = float("inf")
    for f in SWEEPS:
        for line in open(ROOT / f):
            rec = json.loads(line)
            for kind in ("BH", "MINK"):
                e = rec[kind]
                t = tau[e["n_minimal"]]
                n += 1
                big += e["n_minimal"] > 128
                flips += (e["improvement"] < t) != e["abstain"]
                margin = min(margin, abs(e["improvement"] - t))
    print(f"decisions {n}  n>128 {big}  flips {flips}  min_margin {margin:.4f}")


if __name__ == "__main__":
    main()
