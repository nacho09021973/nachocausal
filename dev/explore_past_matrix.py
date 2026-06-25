"""dev/explore_past_matrix.py — EXPLORATION / timing for the order-only pipeline.

OFF the sealed validation path. Builds the same numpy point cloud as the sealed
generator (so the geometry is reproducible), then runs the two heavy stages on
CPU or GPU and reports timing:

  1. past-matrix build  (generator.past_matrix_fast port) — FLOAT; the BH branch
     is not guaranteed GPU-bit-exact (log + FMA near the horizon).
  2. estimator estimate_O (longest-chain max-plus relaxation) — INTEGER only, so
     bit-for-bit identical on CPU and GPU.

With --check each stage is also run on the other device and compared
(disagreeing past-matrix entries; O-multiset / Lfut equality). This is a
benchmark, never a verdict.

Run on a GPU box:   dev/run-gpu.sh --device auto --intensity 12000 --check
Run anywhere (CPU): python -m dev.explore_past_matrix --device cpu --intensity 1500

(Run from the repo root with the venv active so `nachocausal` and `dev` import.)
"""

from __future__ import annotations

import argparse
import time

import numpy as np

from nachocausal import generator
from dev import backend


def _sync(device_name):
    """Block until GPU kernels finish so timings are real (no-op on CPU)."""
    if device_name == "gpu":
        import cupy as cp
        cp.cuda.Device().synchronize()


def _time_matrix(embedding, kind, device):
    """Build the past matrix on `device`. Returns (C_device, secs, dev_name)."""
    t0 = time.perf_counter()
    C, dev_name = backend.past_matrix(embedding, kind, device=device)
    _sync(dev_name)
    return C, time.perf_counter() - t0, dev_name


def _time_estimator(C_device, device):
    """Run estimate_O on the (already on-device) matrix. Returns (O, Lfut, secs)."""
    t0 = time.perf_counter()
    O, _min, Lfut, dev_name = backend.estimate_O(C_device, device=device)
    _sync(dev_name)
    return O, Lfut, time.perf_counter() - t0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--device", default="auto", choices=["auto", "cpu", "gpu"],
                    help="auto (GPU if available, else CPU) | cpu | gpu")
    ap.add_argument("--intensity", type=float, default=1500.0,
                    help="Poisson intensity (mean N); validation uses 1500..12000")
    ap.add_argument("--seed", type=int, default=20240617, help="sprinkle seed")
    ap.add_argument("--kinds", default="BH,MINK", help="comma list: BH,MINK")
    ap.add_argument("--check", action="store_true",
                    help="also run each stage on the other device and compare")
    args = ap.parse_args()

    emb, edges, center = generator.numpy_sprinkle(args.seed, args.intensity)
    generator.assert_coordinate_uniform(emb, edges, center)
    N = emb.shape[0]
    print(f"sprinkle seed={args.seed} intensity={args.intensity:g} -> N={N} "
          f"(past matrix is {N}x{N} bool = {N * N / 1e6:.1f} M entries)")

    for kind in [k.strip() for k in args.kinds.split(",") if k.strip()]:
        C, t_mat, dev = _time_matrix(emb, kind, args.device)
        O, Lfut, t_est = _time_estimator(C, args.device)
        Omax = max(O.values()) if O else 0
        print(f"  [{kind:4}] device={dev:3}  matrix {t_mat * 1e3:8.1f} ms | "
              f"estimate_O {t_est * 1e3:8.1f} ms   "
              f"(|min|={len(O)}, Omax={Omax})")

        if not args.check:
            continue
        other = "cpu" if dev == "gpu" else "gpu"
        try:
            C2, t_mat2, dev2 = _time_matrix(emb, kind, other)
            O2, Lfut2, t_est2 = _time_estimator(C2, other)
        except RuntimeError as e:
            print(f"         --check skipped ({other}): {e}")
            continue
        Ch, C2h = backend.to_host(C), backend.to_host(C2)
        mat_diff = int(np.count_nonzero(Ch != C2h))
        est_ok = (O == O2) and np.array_equal(Lfut, Lfut2)
        mat_tag = "BIT-EXACT" if mat_diff == 0 else f"DIFFERS ({mat_diff} entries)"
        print(f"         vs {dev2:3}  matrix {t_mat2 * 1e3:8.1f} ms | "
              f"estimate_O {t_est2 * 1e3:8.1f} ms   "
              f"matrix:{mat_tag}  estimate_O:{'BIT-EXACT' if est_ok else 'DIFFERS!'}")
        if mat_diff:
            frac = mat_diff / float(N * N)
            print(f"         (matrix {frac:.2e} of entries differ -- BH log/FMA "
                  f"caveat; why GPU stays OFF the sealed validation path)")


if __name__ == "__main__":
    main()
