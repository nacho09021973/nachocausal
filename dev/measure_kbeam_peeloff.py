"""dev measurement — PR-003 Fase #3 / R2: K-BEAM peel-off FALSIFICATION.
EXPLORATION ONLY — nothing frozen, not validated, not audited, no claim.

Авал: docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md §9 R2.
Decides the one open Fase-#3 question: is the `BARE_RELOCALISATION` peel-off
(the bracket-seeded fuzzy ladder drifts away from r_S after ~2-3 adherent rungs —
dev/PR003_NEAR_HORIZON_NOTES.md:112-119) **algorithmic** (greedy myopia, curable
by keeping more hypotheses) or **physical** (a marginally-unstable null orbit =
the order-only localisation wall)?

BINDING pre-committed protocol (declared BEFORE peeking — comité-003 §9 R2):
  (a) BOX FIXED (t_edge=6) and the K-beam is compared against the SINGLE-TRACER
      baseline (`explore_direction.greedy_ladder`) at the SAME box and SAME seed
      rungs (`boundary_minimals_invariant`).
  (b) The K hypotheses are ranked by an ORDER-ONLY quantity ONLY — the EGS fuzzy
      interval-cardinality regularity (|[p_{i-M},p_i]| centred in the band
      [M-1,2M-1]) and link branching. It MUST NOT use relphi or any
      embedding-derived direction (falsifier leakage / physicist relphi caveat).
      `r` is REVEALED ONLY to SCORE d_perp afterward; it never seeds, builds, ranks
      or cuts a ladder.
  (c) THREE-WAY report, no silent collapse to a "win":
        * min-over-beam d_perp/ell tail DROPS to adherence as K grows  -> the order
          retains an adherent ladder a wider search recovers  => ALGORITHMIC.
        * min-over-beam d_perp/ell tail FLAT (stays peeled) for all K   => PHYSICAL
          (no order-only beam keeps adherence -> hardens the Le Cam bound).
        * ladders truncate at the box edge before the profile resolves  => INCONCLUSIVE
          (under-reach; t_edge=6 vs EGS t*/r_S∈[0,50]; a taller box is a NEW prereg).

GPU: the heavy compute (BH past matrix + the transitive-reduction matmul C·C for
the covering/link relation) runs on the local NVIDIA GPU via dev/backend.py /
CuPy; the matmul is integer-valued (0/1 float32, counts << 2^24) so the GPU link
matrix is bit-identical to CPU. The beam combinatorics run on CPU/numba. Nothing
here is on the sealed path; `make verify-seal` = 6e2c3888... before AND after.

Run:
  dev/run-gpu.sh  with NACHO_MODULE=dev.measure_kbeam_peeloff   (WSL libcuda fix)
  or:  python3 dev/measure_kbeam_peeloff.py --smoke   # 2 seeds x {3600}, K<=8
       python3 dev/measure_kbeam_peeloff.py           # 6 seeds x {3600,7200,14400}
"""

from __future__ import annotations

import argparse
import hashlib
import os
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_HERE))  # repo root (nachocausal package)
sys.path.insert(0, _HERE)                   # dev/ (sibling explore_* modules)

from nachocausal import generator, thresholds  # noqa: E402
import explore_ladders as XL  # noqa: E402
from explore_direction import greedy_ladder  # noqa: E402  (single-tracer baseline)
from explore_seeds import EXPLORE_POOL, in_reserved_002  # noqa: E402
from measure_pr003 import boundary_minimals_invariant  # noqa: E402
import backend  # noqa: E402  (dev GPU backend)

SEAL_SHA = "6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4"
R_S = thresholds.R_S
M = 3                     # EGS fuzziness parameter (matches the ladder studies)
LMAX = 25                 # max ladder depth (rungs)
MIN_LEN = 6               # a ladder counts only if it reaches this many rungs
K_GRID = (1, 2, 4, 8, 16, 32, 64)
K_REF = 8                 # reference tail depth for the adherence-vs-K read
ADH = 3.0                 # adherence band in ℓ (NOT a frozen threshold; = truncated_head ADH)
MAX_STARTS = 200          # cap start rungs per seed (deterministic sample)
BAND_CENTRE = 1.5 * M - 1.0   # centre of the EGS interval band [M-1, 2M-1]


# --------------------------------------------------------------------------- seal/hygiene
def seal_sha():
    p = os.path.join(os.path.dirname(_HERE), "nachocausal", "thresholds.py")
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def assert_seal(tag):
    got = seal_sha()
    print(f"[{tag}] thresholds.py sha256 = {got}")
    if got != SEAL_SHA:
        raise SystemExit(f"SEAL MISMATCH ({tag}): {got} != {SEAL_SHA}; aborting.")


def assert_seeds(seeds):
    pool = set(EXPLORE_POOL)
    for s in seeds:
        if s not in pool:
            raise SystemExit(f"seed {s} not in EXPLORE_POOL — refusing (leakage guard).")
        if in_reserved_002(s):
            raise SystemExit(f"seed {s} in RESERVED_002 band — refusing.")


def git_branch():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()
    except Exception:
        return "?"


# --------------------------------------------------------------------------- GPU link CSR
def gpu_link_csr(emb, device):
    """C (BH past matrix) and the future-link CSR, with the heavy build + the
    transitive-reduction matmul C·C on the GPU. Returns (C_host_bool, indptr, idx, dev).
    Bit-identical to explore_ladders.link_future_csr (integer-valued matmul)."""
    C, dev = backend.past_matrix(emb, "BH", r_S=R_S, device=device)  # xp array on device
    xp = backend.to_host(C).__class__ if dev == "cpu" else None
    if dev == "gpu":
        import cupy as cp  # type: ignore
        Cf = C.astype(cp.float32)
        two_step = (Cf @ Cf) > 0.5
        L = C & ~two_step
        L_host = cp.asnumpy(L)
        del Cf, two_step, L
        C_host = cp.asnumpy(C)
        del C
        cp.get_default_memory_pool().free_all_blocks()
    else:
        C_host = np.asarray(C)
        Cf = C_host.astype(np.float32)
        L_host = C_host & ~((Cf @ Cf) > 0.5)
    # future-link children of a = column a of L (x with L[x,a] True)
    cols = [np.nonzero(L_host[:, a])[0].astype(np.int64) for a in range(C_host.shape[0])]
    indptr = np.zeros(C_host.shape[0] + 1, np.int64)
    for a, c in enumerate(cols):
        indptr[a + 1] = indptr[a] + c.size
    idx = (np.concatenate(cols) if cols else np.zeros(0, np.int64)).astype(np.int64)
    return np.ascontiguousarray(C_host), indptr, idx, L_host, dev


# --------------------------------------------------------------------------- the K-beam
def _children(a, indptr, idx):
    return idx[indptr[a]:indptr[a + 1]]


def kbeam(sp, sq, indptr, idx, C, K, lmax=LMAX):
    """Order-only K-beam fuzzy-ladder search from start rung (sp,sq).

    A state = (p_path, q_path, regscore). At each depth, expand every surviving
    state by all Def-2-valid successor rungs, accumulate the ORDER-ONLY regularity
    reward (centred-ness of the interval cardinalities in the EGS band), then keep
    the top-K states by regscore (deduped by terminal rung for diversity).

    Returns a list (per reached depth d=1..) of the surviving p-paths at that depth
    (each a python list of node indices), so the caller can score d_perp/ell. r is
    NOT touched here — this is order-only."""
    # state: (regscore, p_tuple, q_tuple)
    frontier = [(0.0, (int(sp),), (int(sq),))]
    by_depth = [[list(frontier[0][1])]]  # depth-1 survivors (just the seed p)
    d = 1
    while d < lmax and frontier:
        cand = {}  # key=(p_last,q_last) -> best (regscore, p_tuple, q_tuple)
        for reg, pt, qt in frontier:
            p_i, q_i = pt[-1], qt[-1]
            for np_ in _children(p_i, indptr, idx):
                np_ = int(np_)
                for nq in _children(q_i, indptr, idx):
                    nq = int(nq)
                    if np_ == nq or not XL._is_future_link(np_, nq, indptr, idx):
                        continue
                    rwd = 0.0
                    if d >= M:
                        cp = XL._interval_card(pt[d - M], np_, C)
                        if cp < M - 1 or cp > 2 * M - 1:
                            continue
                        cq = XL._interval_card(qt[d - M], nq, C)
                        if cq < M - 1 or cq > 2 * M - 1:
                            continue
                        rwd = -(abs(cp - BAND_CENTRE) + abs(cq - BAND_CENTRE))
                    key = (np_, nq)
                    nreg = reg + rwd
                    prev = cand.get(key)
                    if prev is None or nreg > prev[0]:
                        cand[key] = (nreg, pt + (np_,), qt + (nq,))
        if not cand:
            break
        survivors = sorted(cand.values(), key=lambda s: s[0], reverse=True)[:K]
        frontier = survivors
        by_depth.append([list(pt) for _, pt, _ in survivors])
        d += 1
    return by_depth


# --------------------------------------------------------------------------- per-seed
def sample_starts(C, indptr, idx, seed):
    """Seed rungs = (m, child) over the invariant boundary minimals; deterministic
    sample to MAX_STARTS. Order-only (index-based)."""
    bmin = boundary_minimals_invariant(C)
    starts = []
    for m in bmin:
        for t in range(int(indptr[m]), int(indptr[m + 1])):
            starts.append((int(m), int(idx[t])))
    if len(starts) > MAX_STARTS:
        rng = np.random.default_rng(seed ^ 0xBEA3)
        sel = rng.choice(len(starts), size=MAX_STARTS, replace=False)
        starts = [starts[i] for i in sorted(sel)]
    return starts


def measure_seed(seed, intensity, t_edge, device):
    emb, _, _ = generator.numpy_sprinkle(seed, float(intensity), float(t_edge))
    ell = thresholds.ell(intensity)
    C, indptr, idx, _L, dev = gpu_link_csr(emb, device)
    r = emb[:, 1]
    starts = sample_starts(C, indptr, idx, seed)

    # SINGLE-TRACER baseline (protocol a): the existing greedy ladder, same rungs.
    g_tail, g_len = [], []
    for (sp, sq) in starts:
        gln, gpb = greedy_ladder(sp, sq, indptr, idx, C, M, LMAX)
        if gln >= MIN_LEN:
            gp = gpb[:gln]
            gd = np.abs(r[gp] - R_S) / ell
            g_len.append(int(gln))
            if gln > 3:
                g_tail.append(float(np.median(gd[3:])))

    # K-beam sweep. Per K: pooled per-depth d_perp/ell of (i) the top-1 regularity
    # ladder and (ii) the MIN over the K survivors (best retained hypothesis).
    out = {}
    for K in K_GRID:
        top1 = [[] for _ in range(LMAX)]   # depth -> list of d_perp/ell (top-1 reg)
        beammin = [[] for _ in range(LMAX)]
        reach = []                         # max depth reached per start
        for (sp, sq) in starts:
            bd = kbeam(sp, sq, indptr, idx, C, K)
            reach.append(len(bd))
            if len(bd) < MIN_LEN:
                continue
            for k in range(len(bd)):
                paths = bd[k]              # survivors at depth k+1, ranked (top1 first)
                # d_perp/ell of the LAST rung of each survivor path
                dvals = [abs(r[p[-1]] - R_S) / ell for p in paths]
                top1[k].append(dvals[0])           # order-only top-1 selection
                beammin[k].append(min(dvals))      # best retained hypothesis
        out[K] = dict(
            top1=[np.median(x) if x else np.nan for x in top1],
            beammin=[np.median(x) if x else np.nan for x in beammin],
            n_at=[len(x) for x in top1],
            reach=np.array(reach, float),
        )
    return dict(ell=ell, g_tail=np.array(g_tail, float), g_len=np.array(g_len, float),
                kbeam=out, dev=dev, N=emb.shape[0])


# --------------------------------------------------------------------------- run
def run(seeds, intensities, t_edge, device):
    print(f"seeds={len(seeds)} {seeds}  t_edge={t_edge:.0f}  M={M}  lmax={LMAX} "
          f"min_len={MIN_LEN}  K={K_GRID}  k_ref={K_REF}  ADH={ADH:.0f}ℓ\n")
    for inten in intensities:
        t0 = time.perf_counter()
        rows = [measure_seed(s, inten, t_edge, device) for s in seeds]
        ell = rows[0]["ell"]
        dev = rows[0]["dev"]
        # single-tracer baseline
        gt = np.concatenate([r["g_tail"] for r in rows]) if rows else np.array([])
        gl = np.concatenate([r["g_len"] for r in rows]) if rows else np.array([])
        print(f"================ intensity {inten:g}  ℓ={ell:.4f}  N≈{rows[0]['N']}  "
              f"dev={dev}  [{time.perf_counter()-t0:.0f}s] ================")
        print(f"  SINGLE-TRACER (greedy, K=1 baseline): len median={np.nanmedian(gl):.0f} "
              f"n={gl.size};  tail d⊥/ℓ (rungs>3) median={np.nanmedian(gt):.2f}  "
              f"(peel-off reference)")
        print(f"  {'K':>3} | {'top1 d⊥/ℓ@kref':>14} | {'minbeam d⊥/ℓ@kref':>17} | "
              f"{'n@kref':>6} | {'reach≥kref':>10} | profile min-beam d⊥/ℓ by depth k=1..12")
        for K in K_GRID:
            prof_top1, prof_min, n_prof = [], [], []
            reach_all = np.concatenate([r["kbeam"][K]["reach"] for r in rows])
            for k in range(LMAX):
                t1 = [r["kbeam"][K]["top1"][k] for r in rows
                      if k < len(r["kbeam"][K]["top1"]) and np.isfinite(r["kbeam"][K]["top1"][k])]
                bm = [r["kbeam"][K]["beammin"][k] for r in rows
                      if k < len(r["kbeam"][K]["beammin"]) and np.isfinite(r["kbeam"][K]["beammin"][k])]
                n_k = sum(r["kbeam"][K]["n_at"][k] for r in rows
                          if k < len(r["kbeam"][K]["n_at"]))
                prof_top1.append(np.median(t1) if t1 else np.nan)
                prof_min.append(np.median(bm) if bm else np.nan)
                n_prof.append(n_k)
            kref = K_REF - 1
            top1_ref = prof_top1[kref] if kref < len(prof_top1) else np.nan
            min_ref = prof_min[kref] if kref < len(prof_min) else np.nan
            n_ref = n_prof[kref] if kref < len(n_prof) else 0
            reach_frac = float(np.mean(reach_all >= K_REF))
            prof_str = " ".join(f"{prof_min[k]:4.1f}" if np.isfinite(prof_min[k]) else "  . "
                                for k in range(12))
            print(f"  {K:>3} | {top1_ref:>14.2f} | {min_ref:>17.2f} | {n_ref:>6d} | "
                  f"{reach_frac:>9.0%} | {prof_str}")
        print()


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true", help="2 seeds x {3600}, K<=8")
    ap.add_argument("--seeds", type=int, default=6)
    ap.add_argument("--device", default="auto", choices=["auto", "cpu", "gpu"])
    return ap.parse_args()


def main():
    args = parse_args()
    print("PR-003 Fase #3 / R2 — K-beam peel-off falsification (dev, NOT a result)")
    print(f"UTC {datetime.now(timezone.utc).isoformat()}  host {platform.node()}")
    print(f"git branch = {git_branch()}  python {platform.python_version()} "
          f"numpy {np.__version__}")
    assert_seal("pre")
    XL.selftest()  # ladder-primitive oracle before any measurement

    if args.smoke:
        global K_GRID
        K_GRID = (1, 2, 4, 8)
        seeds = list(EXPLORE_POOL[:2]); intensities = (3600.0,)
    else:
        seeds = list(EXPLORE_POOL[:args.seeds]); intensities = (3600.0, 7200.0, 14400.0)
    assert_seeds(seeds)
    _xp, dev = backend.resolve_device(args.device)
    print(f"backend device = {dev}  (requested {args.device})\n")

    t0 = time.time()
    run(seeds, intensities, 6.0, args.device)
    print(f"elapsed {time.time()-t0:.1f}s")
    assert_seal("post")
    print("done — exploration only; nothing frozen, no seed in RESERVED_002 touched.")


if __name__ == "__main__":
    main()
