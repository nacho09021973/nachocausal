"""Validate the GPU generator (dev/gen2p1_gpu.py) against the CPU one (dev/gen2p1_efbox.py).

Same sprinkle (same seed), both orders; reports mismatching pairs, the pairs within TOL of the
boundary on either side (the only place a disagreement is admissible), transitivity of the GPU
order, the same-angle check against the sealed 1+1D closed form, and timings.
Run in .venv-gpu:  NC2P1_T_EDGE=T .venv-gpu/bin/python dev/validate_gen2p1_gpu.py N seed
"""
import json
import sys
import time

import numpy as np

sys.path.insert(0, "dev")
import gen2p1_efbox as gen  # noqa: E402
import gen2p1_gpu as gpu  # noqa: E402


def main():
    n_mean, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = np.random.default_rng(seed)
    t, r, phi = gen.sprinkle(n_mean, rng)
    t0 = time.time(); og, sg = gpu.bh_order(t, r, phi); tg = time.time() - t0
    t0 = time.time(); oc, sc = gen.bh_order(t, r, phi, rng=None); tc = time.time() - t0
    mism = np.argwhere(og != oc)
    out = {"T_EDGE": gen.T_EDGE, "n": int(t.size), "gpu_seconds": round(tg, 1),
           "cpu_seconds": round(tc, 1), "relations_gpu": sg["relations"],
           "relations_cpu": sc["relations"], "mismatched_pairs": int(mism.shape[0]),
           "gpu_near_boundary": sg["near_boundary_pairs_tol"],
           "cpu_near_boundary": sc["near_boundary_pairs_tol"]}
    if mism.shape[0]:
        U, V = gen.to_kruskal(t, r)
        a, b = mism[:, 0], mism[:, 1]
        L, m = gen.shoot_pairs_fast(U[a], V[a], U[b], V[b], 4096, 16384)
        d = np.abs(phi[b] - phi[a]); d = np.minimum(d, 2 * np.pi - d)
        out["mismatch_gap_to_boundary_max"] = float(np.max(np.abs(d - np.minimum(L, np.pi))))
    out["gpu_transitivity_violations"] = gen.transitivity_violations(og)
    mm, tot = gen.radial_check(t, r)
    out["radial_check_mismatches"] = mm
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
