---
name: gpu-exploration-backend
description: Optional GPU (CuPy) backend lives in dev/ only; sealed path stays CPU numpy 1.26.4
metadata: 
  node_type: memory
  type: project
  originSessionId: 232b08ee-6185-48b8-a363-e50f44024aae
---

nachocausal has an optional GPU acceleration path for the past-matrix build,
added 2026-06-20 at the user's request ("option to use the GPU but not fixed,
since I also work from CPU-only machines").

Key constraints and layout:
- GPU is **exploration only**, never on the sealed validation path. The sealed
  package `nachocausal/` must stay pure CPU `numpy==1.26.4` and bit-for-bit
  reproducible (`tests/test_regression.py`, thresholds.py SHA256 seal,
  `thresholds.assert_environment`). GPU float math (BH branch: `np.log` + FMA)
  is not guaranteed bit-identical near the horizon, so it would break the seal.
- Code lives in untracked `dev/`: `backend.py` (device selector `resolve_device`
  auto|cpu|gpu with graceful CPU fallback + device-agnostic ports of BOTH
  `generator.past_matrix_fast` AND `estimator.estimate_O`), `explore_past_matrix.py`
  (CLI benchmark timing both stages with `--device`/`--check`),
  `sweep_ensemble.py` (full 4-intensity x seed-set exploration sweep: blind
  order-only stage only -> d = sep_BH - sep_MINK per intensity + timing; NOT a
  verdict, ~28 s for 8 dev seeds on GPU), `run-gpu.sh` + `run-sweep.sh`
  (launchers; run-gpu.sh takes NACHO_MODULE override), `README-gpu.md`.
- The `estimate_O` GPU port is a parallel max-plus longest-chain relaxation;
  INTEGER-only so it is bit-for-bit identical CPU vs GPU (verified). It was the
  real bottleneck: CPU estimate_O took ~50-70 s at N=12000 (Python topological-DP
  loop), GPU ~1.1-1.4 s warm (~40-60x). The matrix build is float (BH log), only
  ~6-40x and not guaranteed bit-exact.
- **Two separate venvs** are required because CuPy 14.x needs numpy>=2.0:
  `.venv` = sealed (numpy 1.26.4, run `make test`/dry-run here);
  `.venv-gpu` = numpy 2.x + `cupy-cuda12x[ctk]` (run only the dev explore script).
  Never let cupy/numpy2 into `.venv`.
- WSL2 gotcha on the user's box: a stale native `libcuda.so.535` in
  `/lib/x86_64-linux-gnu` shadows the WSL stub in `/usr/lib/wsl/lib` (driver 610),
  causing `cudaErrorNoDevice` even though `nvidia-smi` works. `dev/run-gpu.sh`
  prepends `/usr/lib/wsl/lib` to `LD_LIBRARY_PATH` to fix it.
- GPU is an RTX 5060 (Blackwell, sm_120): NVRTC must be >= CUDA 12.8, hence the
  `[ctk]` extra (bundles CUDA 12.9 headers). Measured ~6x (BH) / ~36x (MINK)
  speedup vs CPU at N~12000; disagreement was 0 entries at the tested seeds.

See [[nachocausal-sealed-instrument]].
