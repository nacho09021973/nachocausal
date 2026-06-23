#!/usr/bin/env python
"""DEV diagnostic: why does the box-matched MINK control trip the dip? Two
candidate causes: (1) genuine box-edge bimodality in O; (2) integer-ties artifact
(diptest's tabulated p assumes continuous data, real O is tied integers).
Runs in the dip venv. NOT a result."""
import json
import numpy as np
import diptest

RNG = np.random.default_rng(1)

# (2) FP rate on TIED INTEGER data resembling O: integers drawn from a smooth
# unimodal shape, then rounded -> heavy ties, like our O multisets.
def tied_unimodal(n, K):
    # triangular-ish unimodal integer sample in [0,K]; rounding creates ties
    x = RNG.triangular(0, K/2, K, n)
    return np.round(x)

print("=== ties artifact check: dip FP on TIED integer unimodal data (alpha=0.01) ===")
print(f"{'n':>5} {'K=10':>7} {'K=30':>7} {'K=80':>7}")
for n in (16, 22, 32, 46):
    row = []
    for K in (10, 30, 80):
        c = sum(diptest.diptest(tied_unimodal(n, K))[1] < 0.01 for _ in range(3000))
        row.append(c/3000)
    print(f"{n:>5} " + " ".join(f"{v:>7.3f}" for v in row))
print("  if these are >>0.01, the tied-integer calibration differs from continuous.")

# (1) look at the actual MINK O multisets that tripped, vs BH, at intensity 3000
recs = json.load(open("dev/o_samples.json"))
print("\n=== actual O multisets at intensity=3000 (sorted), with dip p ===")
for kind in ("MINK", "BH"):
    print(f"-- {kind} --")
    for r in recs:
        if r["kind"] == kind and r["intensity"] == 3000.0:
            O = np.sort(np.asarray(r["O"], float))
            _, p = diptest.diptest(O)
            tag = "  <-- p<0.01" if p < 0.01 else ""
            print(f"  seed={r['seed']:>6} |min|={O.size:>3} p={p:.3f}{tag}  O={O.astype(int).tolist()}")
