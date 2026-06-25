"""dev/backend.py — OPTIONAL GPU backend for EXPLORATION ONLY.

NOT on the validation path. The sealed package `nachocausal/` stays pure CPU
numpy==1.26.4 and bit-for-bit reproducible; nothing here is imported by it.

Why GPU is off the seal: the BH branch uses np.log (transcendental) and chained
mul/add. GPU log + FMA contraction differ from CPU libm in the last ulp, which
flips causal relations near the horizon -> a different poset -> a different O.
So GPU results are NOT bit-identical to the sealed CPU instrument. This module
exists to explore / benchmark at large N, and to *quantify* that divergence
(see explore_past_matrix.py --check), never to produce a sealed verdict.

Device selection (graceful, never hard-fails on a CPU-only machine):
  * "auto" (default): use CuPy on the GPU if importable AND a device is present,
    otherwise fall back to numpy on the CPU.
  * "cpu": force numpy.
  * "gpu": force CuPy; raises a clear error if CuPy/GPU is unavailable.
Overridable by the env var NACHOCAUSAL_DEVICE (auto|cpu|gpu); an explicit
device= argument wins over the env var.
"""

from __future__ import annotations

import os
from typing import Tuple

import numpy as np

from nachocausal import thresholds  # frozen constants only (R_S); pure numpy


def _try_import_cupy():
    """Return the cupy module if it imports AND a usable GPU is visible, else None."""
    try:
        import cupy as cp  # type: ignore
    except Exception:
        return None
    try:
        if cp.cuda.runtime.getDeviceCount() < 1:
            return None
    except Exception:
        return None
    return cp


def resolve_device(device: str | None = None) -> Tuple[object, str]:
    """Pick the array module. Returns (xp, device_name) where device_name is
    'cpu' or 'gpu'. `device` overrides the env var NACHOCAUSAL_DEVICE; both
    default to 'auto'."""
    if device is None:
        device = os.environ.get("NACHOCAUSAL_DEVICE", "auto")
    device = device.lower()
    if device not in ("auto", "cpu", "gpu"):
        raise ValueError(f"device must be auto|cpu|gpu, got {device!r}")

    if device == "cpu":
        return np, "cpu"

    cp = _try_import_cupy()
    if device == "gpu":
        if cp is None:
            raise RuntimeError(
                "device='gpu' requested but CuPy/GPU is unavailable. Install the "
                "optional backend (pip install -r requirements-gpu.txt) on a CUDA "
                "machine, or use device='auto' to fall back to CPU."
            )
        return cp, "gpu"

    # auto: prefer GPU, silently fall back to CPU.
    return (cp, "gpu") if cp is not None else (np, "cpu")


def to_host(arr):
    """Bring an array back to host numpy regardless of backend."""
    cp = _try_import_cupy()
    if cp is not None and isinstance(arr, cp.ndarray):
        return cp.asnumpy(arr)
    return np.asarray(arr)


# =============================================================================
# Device-agnostic port of generator.past_matrix_fast (behaviour-preserving on
# CPU; see explore_past_matrix.py --check for the GPU-vs-CPU agreement report).
# =============================================================================
def past_matrix(embedding, kind: str, r_S: float = thresholds.R_S, device=None):
    """N x N boolean past matrix C[i,j] = (j precedes i), built on the selected
    device. Mirrors nachocausal.generator.past_matrix_fast op-for-op so the CPU
    path is identical to the sealed one; the GPU path is the same math on CuPy.

    Returns (C, device_name). C is an xp.ndarray on the chosen device."""
    xp, device_name = resolve_device(device)
    if kind not in ("MINK", "BH"):
        raise ValueError(f"unknown kind {kind!r}")

    emb = xp.asarray(embedding, dtype=xp.float64)
    eps = 1e-12  # == Minz causality_eps
    t = emb[:, 0]
    r = emb[:, 1]
    N = emb.shape[0]
    C = xp.zeros((N, N), dtype=bool)

    if kind == "BH":
        # divide/invalid at r == r_S are expected (log singularity at horizon);
        # numpy.errstate only guards numpy, so guard generically.
        old = np.seterr(divide="ignore", invalid="ignore") if xp is np else None
        try:
            func = r + 2.0 * r_S * xp.log(xp.abs(r - r_S) / r_S)
        finally:
            if old is not None:
                np.seterr(**old)

    # Same row-blocking heuristic as the sealed accelerator (caps NxN temporaries).
    block = max(1, 64_000_000 // (8 * max(N, 1)))
    rj = r[None, :]
    tj = t[None, :]
    for a in range(0, N, block):
        b = min(a + block, N)
        ti = t[a:b, None]
        ri = r[a:b, None]
        dt = ti - tj
        if kind == "MINK":
            C[a:b] = (dt > 0.0) & (dt >= xp.abs(ri - rj) - eps)
        else:  # BH, Eddington-Finkelstein
            earlier = tj < ti
            t_out = func[a:b, None] - func[None, :]
            t_in = rj - ri
            b1 = (ri <= rj) & (rj <= r_S)
            b2 = (rj >= r_S) & (rj >= ri)
            b3 = (rj >= r_S) & (rj <= ri)
            isc = xp.where(
                b1,
                (t_out >= dt) & (dt >= t_in),
                xp.where(b2, dt >= t_in, xp.where(b3, dt >= t_out, False)),
            )
            C[a:b] = earlier & isc
    xp.fill_diagonal(C, False)
    return C, device_name


# =============================================================================
# Device-agnostic port of estimator.estimate_O — the order-only observable O.
# =============================================================================
def estimate_O(past_matrix, device=None):
    """O(i) for each minimal element i = longest timelike chain (in #elements)
    starting at i, computed from the boolean past matrix ALONE.

    The sealed estimator does this with a topological-order DP in a Python loop
    (estimator.estimate_O). Here it is the SAME Bellman recurrence
        Lfut[e] = 1 + max_{f in future(e)} Lfut[f]   (future(e) = rows i: C[i,e])
    solved by parallel max-plus relaxation instead — a fixed-point iteration that
    GPU vectorises. It is INTEGER arithmetic only (no float), so unlike the BH
    matrix build the result is bit-for-bit identical to the CPU estimator on
    BOTH devices; the fixed point of a DAG longest-path recurrence is unique.

    Returns (O_by_minimal_index, minimal_indices, Lfut_host, device_name).
    Lfut_host is a host numpy int array (matches estimator.estimate_O's 3rd value).
    """
    xp, device_name = resolve_device(device)
    C = xp.asarray(past_matrix)
    if C.dtype != xp.bool_:
        C = C.astype(xp.bool_)
    N = C.shape[0]
    assert C.shape == (N, N), "estimator expects a square poset matrix"

    Lfut = xp.ones(N, dtype=xp.int32)  # every element is a chain of >= 1
    # Column-block the N x N temporary so memory stays bounded at large N.
    block = max(1, 256_000_000 // (4 * max(N, 1)))
    converged = False
    for _ in range(N + 1):  # converges in <= longest-chain-length iterations
        newL = xp.empty(N, dtype=xp.int32)
        for a in range(0, N, block):
            b = min(a + block, N)
            # cand[i, e] = Lfut[i] if e is in the future of i (C[i,e]) else 0;
            # column max over i is max Lfut over future(e), or 0 for a sink.
            cand = C[:, a:b] * Lfut[:, None]
            newL[a:b] = 1 + cand.max(axis=0)
        if bool((newL == Lfut).all()):
            Lfut = newL
            converged = True
            break
        Lfut = newL
    if not converged:
        raise RuntimeError("longest-path relaxation did not converge (cycle?)")

    minimal_mask = to_host(~C.any(axis=1))
    Lfut_host = to_host(Lfut).astype(int)
    minimal_indices = [i for i in range(N) if minimal_mask[i]]
    O_by_minimal = {i: int(Lfut_host[i]) for i in minimal_indices}
    return O_by_minimal, minimal_indices, Lfut_host, device_name
