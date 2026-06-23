#!/usr/bin/env python
"""
DEV gate (Phase 0): close audit gap #1 -- verify the vectorized accelerator
past_matrix_fast reproduces the Minz reference poset BIT-FOR-BIT at the dense
ceiling N~1e4, where the sweeps relied on the fast path but the gate had only been
run to N~2008/3046. Runs in the Minz venv. Slow (Minz relate is O(N^2)).

This is the falsifiable test: if the fast path were wrong (or rigged) at large N,
verify_fast_matches_minz RAISES with the first disagreeing [i,j]. Not controlled
by the author -- decided by the comparison.
"""
from __future__ import annotations
import time
import numpy as np
import prototype_o as P
from causets.sprinkledcauset import SprinkledCauset
from causets.spacetimes import BlackHoleSpacetime, FlatSpacetime
from causets.shapes import CoordinateShape

SEED = 20240617          # documented dev seed
INTENSITY = 10000.0      # dense-ceiling scale
T_EDGE, R_EDGE = 6.0, 1.2
CENTER = [T_EDGE / 2.0, 0.7]
R_S = 0.5

def main():
    shape = CoordinateShape(2, "cuboid", edges=np.array([T_EDGE, R_EDGE], float),
                            center=np.array(CENTER, float))
    for kind in ("BH", "MINK"):
        st = BlackHoleSpacetime(2, r_S=R_S, metric="Eddington-Finkelstein") \
            if kind == "BH" else FlatSpacetime(2)
        rng = np.random.default_rng(SEED)
        t0 = time.time()
        C = SprinkledCauset(dim=2, spacetime=st, shape=shape)
        C.intensify(INTENSITY, rng=rng, shape=shape)
        events = C.sortedByCausality()
        emb = np.array([e.Coordinates for e in events], float)
        N = emb.shape[0]
        t_gen = time.time() - t0
        Cm = C.PastMatrix(events, dtype=bool)
        t_minz = time.time() - t0
        Cf = P.past_matrix_fast(emb, kind, R_S)
        # RAISES on any disagreement; prints the agreement count otherwise.
        P.verify_fast_matches_minz(Cm, Cf, kind)
        print(f"[{kind}] N={N}  Minz gen+poset {t_minz:.1f}s  "
              f"fast==Minz over {N*N} pairs CONFIRMED")
    print("AUDIT GAP #1 CLOSED: accelerator == Minz bit-for-bit at the dense ceiling.")

if __name__ == "__main__":
    main()
