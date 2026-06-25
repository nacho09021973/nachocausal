# Optional GPU backend (exploration only)

**Not on the sealed validation path.** The committed package `nachocausal/` stays
pure CPU `numpy==1.26.4` and bit-for-bit reproducible. The GPU code lives entirely
in this untracked `dev/` sandbox and is used only for exploration / large-N timing.

Two heavy stages are ported in `dev/backend.py` (both device-agnostic, `auto|cpu|gpu`):

1. **`past_matrix`** — port of `generator.past_matrix_fast`. **Float**; the BH branch
   uses `np.log` + chained mul/add, so it is *not guaranteed* GPU-bit-exact.
2. **`estimate_O`** — port of `estimator.estimate_O`, reformulated as a parallel
   max-plus longest-chain relaxation. **Integer arithmetic only**, so it is
   bit-for-bit identical on CPU and GPU (the DAG longest-path fixed point is unique).

## Why GPU is kept off the seal

The whole instrument's value is bit-exact reproducibility under the pinned numpy on
CPU (`tests/test_regression.py`, the SHA256 seal). Stage 1 (the past matrix) is **not
guaranteed** bit-identical on GPU: GPU `log` + FMA contraction can differ from CPU libm
in the last ulp, flipping a causal relation near the horizon → a different poset → a
different `O`. (In practice it is often 0 diffs at a given seed — see `--check` — but
not *guaranteed*.) Stage 2 (`estimate_O`) *is* integer-exact, but it consumes stage 1's
matrix, so the pipeline as a whole must stay CPU-only for any sealed verdict. GPU is for
exploration and timing, never a verdict.

## Measured speedups (RTX 5060, N≈12019, warm kernels)

| stage              | CPU         | GPU       | speedup | agreement  |
|--------------------|-------------|-----------|---------|------------|
| past_matrix (BH)   | ~2250 ms    | ~350 ms   | ~6×     | bit-exact* |
| past_matrix (MINK) | ~1196 ms    | ~30 ms    | ~40×    | bit-exact* |
| estimate_O (BH)    | ~52800 ms   | ~1140 ms  | ~46×    | bit-exact  |
| estimate_O (MINK)  | ~68500 ms   | ~1440 ms  | ~48×    | bit-exact  |

`estimate_O` (the Python-loop topological DP) is what made `make test` take ~280 s.
*matrix agreement was 0 diffs at the tested seeds but is not guaranteed for BH.

## Two separate venvs (required)

CuPy 14.x depends on `numpy>=2.0`, which is incompatible with the sealed
`numpy==1.26.4`. They cannot share one venv, so:

| venv         | numpy   | purpose                                        |
|--------------|---------|------------------------------------------------|
| `.venv`      | 1.26.4  | **sealed** path: `make test`, `dry-run`, etc.  |
| `.venv-gpu`  | 2.x     | exploration only: GPU past-matrix benchmarking |

Setup:
```bash
python3 -m venv .venv     && .venv/bin/pip install -r requirements.txt       # sealed
python3 -m venv .venv-gpu && .venv-gpu/bin/pip install -r requirements-gpu.txt # GPU explore
```

## Running

```bash
# Single-config benchmark / bit-exactness check (auto-detects GPU, else CPU).
dev/run-gpu.sh --device auto --intensity 12000 --check

# Full-ensemble exploration sweep: 4 frozen intensities x seed set, reports the
# order-only signal d = sep_BH - sep_MINK per intensity + timing. NOT a verdict.
dev/run-sweep.sh --device auto --seeds dev          # 8 dev seeds
dev/run-sweep.sh --device auto --seeds validation   # 20 validation seeds

# CPU-only machine: just use the sealed venv, no GPU libs needed.
PYTHONPATH=. .venv/bin/python -m dev.explore_past_matrix --device cpu --intensity 1500
PYTHONPATH=. .venv/bin/python -m dev.sweep_ensemble     --device cpu --seeds dev
```

`dev/sweep_ensemble.py` runs only the blind order-only stage (cloud → matrix →
`estimate_O` → `two_means_split`); it never reveals coordinates to a scorer, never
applies the frozen PASS/FAIL thresholds, and writes no verdict. The sealed verdict
comes ONLY from `python -m nachocausal.validate` in the sealed CPU venv. Measured:
the 8-seed × 4-intensity sweep runs in ~28 s on the RTX 5060; GPU and CPU produce
identical `sep` values (the estimator is integer-exact).

It writes raw per-seed results to `dev_ensemble_raw/sweep_<seeds>_<device>_<UTC>.json`
(git-ignored) — metadata (device, numpy version, seeds, intensities, timing) plus a
flat `per_seed` list (intensity, seed, N, sep_BH, sep_MINK, d) and `per_level`
aggregates. Override the path with `--out PATH`, or `--out none` to skip writing.
The payload is tagged `"kind": "exploration_sweep"` so it is never mistaken for a
sealed verdict (which `nachocausal.validate` writes to `results/`).

Device selection (`dev/backend.py`):
- `--device auto` (or env `NACHOCAUSAL_DEVICE=auto`): GPU if CuPy + a device are
  present, else CPU. **This is the "not fixed" behaviour** — same script runs on the
  GPU box and on a laptop with no GPU.
- `--device cpu`: force numpy.
- `--device gpu`: force CuPy; clear error if unavailable.

`--check` rebuilds on the other device and reports how many poset entries disagree —
a direct measurement of the bit-exactness caveat.

## WSL2 driver gotcha (this machine)

A stale native `libcuda.so.535` in `/lib/x86_64-linux-gnu` shadows the WSL stub in
`/usr/lib/wsl/lib` (which matches the Windows driver), giving `cudaErrorNoDevice` even
though `nvidia-smi` works. `dev/run-gpu.sh` prepends `/usr/lib/wsl/lib` to
`LD_LIBRARY_PATH` to fix it; harmless on non-WSL machines (the dir won't exist).

Blackwell note: the RTX 5060 is `sm_120`; NVRTC must be ≥ CUDA 12.8 to compile for it,
which is why `requirements-gpu.txt` uses the `[ctk]` extra (bundles CUDA 12.9 headers).
