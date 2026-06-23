#!/usr/bin/env python
"""
DEV helper (Phase 0): dump real O multisets to JSON so the dip test (its own venv)
can read them without importing Minz. Runs in the Minz venv (numpy sprinkle +
accelerator + estimator are pure numpy; only the module import touches causets).

Tall box (the geometry favoured by Sweep 2), BH + box-matched MINK control.
Writes dev/o_samples.json. NOT a result.
"""
from __future__ import annotations
import json
import numpy as np
import prototype_o as P
from sweep_o2 import numpy_sprinkle, R_S

DEV_SEEDS = [20240617, 13, 101, 7, 42, 99, 2718, 31415]
INTENSITIES = [1500.0, 3000.0, 6000.0, 12000.0]
T_EDGE = 6.0  # tall box

def main():
    records = []
    for seed in DEV_SEEDS:
        for intensity in INTENSITIES:
            emb, edges, center = numpy_sprinkle(seed, intensity, T_EDGE)
            for kind in ("BH", "MINK"):
                Cf = P.past_matrix_fast(emb, kind, R_S)
                O_by_min, min_idx, _ = P.estimate_O(Cf)
                records.append({
                    "kind": kind, "seed": int(seed),
                    "intensity": float(intensity),
                    "N": int(emb.shape[0]),
                    "O": [int(v) for v in O_by_min.values()],
                })
            print(f"  done seed={seed} intensity={intensity}")
    with open("dev/o_samples.json", "w") as f:
        json.dump(records, f)
    print(f"wrote dev/o_samples.json ({len(records)} records)")

if __name__ == "__main__":
    main()
