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
import csv
import hashlib
import json
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

    A state = (lineage_id, regscore, p_path, q_path). At each depth, expand every
    surviving state by all Def-2-valid successor rungs, accumulate the ORDER-ONLY
    regularity reward (centred-ness of the interval cardinalities in the EGS
    band), then keep the top-K states by regscore (deduped by terminal rung for
    diversity).

    `lineage_id` is unique within this kbeam() call (one call = one start) and is
    assigned once when a candidate is first created; it is inherited unchanged by
    the single highest-scoring child that continues a given parent. If a parent
    survives into multiple children (a beam branch/split), every child other than
    that highest-scoring one is a newly created lineage and gets a fresh id — a
    branch is a new survivor, not a continuation of the old one. This makes
    `lineage_id` a persistent identity across depths (PR004 V2 preregistration §2),
    unlike the depth-relative rank the caller assigns downstream.

    Returns a list by depth. Each depth entry is a list of survivors
    `(lineage_id, regscore, p_path, q_path)` in rank order. r is NOT touched here —
    this is order-only."""
    next_lineage_id = 1  # 0 is reserved for the depth-1 seed lineage
    frontier = [(0, 0.0, (int(sp),), (int(sq),))]  # (lineage_id, regscore, p_tuple, q_tuple)
    _lid0, _reg0, _pt0, _qt0 = frontier[0]
    by_depth = [[(_lid0, _reg0, list(_pt0), list(_qt0))]]
    d = 1
    while d < lmax and frontier:
        cand = {}  # key=(p_last,q_last) -> best (regscore, p_tuple, q_tuple, parent_lineage_id)
        for lid, reg, pt, qt in frontier:
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
                        cand[key] = (nreg, pt + (np_,), qt + (nq,), lid)
        if not cand:
            break
        ranked = sorted(cand.values(), key=lambda s: s[0], reverse=True)[:K]
        used_parents = set()
        survivors = []
        for nreg, pt, qt, parent_lid in ranked:
            if parent_lid not in used_parents:
                lid = parent_lid
                used_parents.add(parent_lid)
            else:
                lid = next_lineage_id
                next_lineage_id += 1
            survivors.append((lid, nreg, pt, qt))
        frontier = survivors
        by_depth.append([(lid, float(reg), list(pt), list(qt)) for lid, reg, pt, qt in survivors])
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


def _child_degree_stats(indptr):
    deg = np.diff(indptr)
    return dict(
        avg_outdeg=float(np.mean(deg)) if deg.size else 0.0,
        max_outdeg=int(np.max(deg)) if deg.size else 0,
    )


def measure_seed(seed, intensity, t_edge, device, probe_k=None, probe_writer=None):
    t_seed0 = time.perf_counter()
    emb, _, _ = generator.numpy_sprinkle(seed, float(intensity), float(t_edge))
    ell = thresholds.ell(intensity)
    t0 = time.perf_counter()
    C, indptr, idx, _L, dev = gpu_link_csr(emb, device)
    t_link = time.perf_counter() - t0
    r = emb[:, 1]
    t0 = time.perf_counter()
    starts = sample_starts(C, indptr, idx, seed)
    t_starts = time.perf_counter() - t0
    deg_stats = _child_degree_stats(indptr)

    # SINGLE-TRACER baseline (protocol a): the existing greedy ladder, same rungs.
    t0 = time.perf_counter()
    g_tail, g_len = [], []
    for (sp, sq) in starts:
        gln, gpb = greedy_ladder(sp, sq, indptr, idx, C, M, LMAX)
        if gln >= MIN_LEN:
            gp = gpb[:gln]
            gd = np.abs(r[gp] - R_S) / ell
            g_len.append(int(gln))
            if gln > 3:
                g_tail.append(float(np.median(gd[3:])))
    t_greedy = time.perf_counter() - t0

    # K-beam sweep. Per K: pooled per-depth d_perp/ell of (i) the top-1 regularity
    # ladder and (ii) the MIN over the K survivors (best retained hypothesis).
    out = {}
    kbeam_stats = {}
    for K in K_GRID:
        t0 = time.perf_counter()
        top1 = [[] for _ in range(LMAX)]   # depth -> list of d_perp/ell (top-1 reg)
        beammin = [[] for _ in range(LMAX)]
        reach = []                         # max depth reached per start
        total_frontier_states = 0
        total_survivors = 0
        for start_id, (sp, sq) in enumerate(starts):
            bd = kbeam(sp, sq, indptr, idx, C, K)
            reach.append(len(bd))
            if len(bd) < MIN_LEN:
                continue
            for k in range(len(bd)):
                paths = bd[k]              # survivors at depth k+1, ranked (top1 first)
                total_frontier_states += len(paths)
                total_survivors += len(paths)
                # d_perp/ell of the LAST rung of each survivor path
                dvals = []
                for lid, reg, p, q in paths:
                    r_p_last = float(r[p[-1]])
                    r_q_last = float(r[q[-1]])
                    d_mid = abs(0.5 * (r_p_last + r_q_last) - R_S) / ell
                    dvals.append(d_mid)
                if probe_writer is not None and probe_k is not None and K == probe_k:
                    rows_k = []
                    for survivor_rank, (lid, reg, p, q) in enumerate(paths):
                        r_p_last = float(r[p[-1]])
                        r_q_last = float(r[q[-1]])
                        d_p = abs(r_p_last - R_S) / ell
                        d_q = abs(r_q_last - R_S) / ell
                        d_mid = abs(0.5 * (r_p_last + r_q_last) - R_S) / ell
                        rows_k.append(dict(
                            lineage_id=int(lid),
                            survivor_rank_at_depth=int(survivor_rank),
                            p_last=int(p[-1]),
                            q_last=int(q[-1]),
                            r_p_last=r_p_last,
                            r_q_last=r_q_last,
                            d_p_over_ell=float(d_p),
                            d_q_over_ell=float(d_q),
                            d_mid_over_ell=float(d_mid),
                            straddles_horizon=int((r_p_last - R_S) * (r_q_last - R_S) <= 0.0),
                            regscore=float(reg),
                            is_top1=int(survivor_rank == 0),
                            path_p=json.dumps(p, separators=(",", ":")),
                            path_q=json.dumps(q, separators=(",", ":")),
                        ))
                    # is_minbeam_at_k: argmin d_mid_over_ell within this depth's
                    # survivor group; ties broken deterministically by lowest
                    # lineage_id (PR004 V2 preregistration §7 item 5).
                    min_d_mid = min(row["d_mid_over_ell"] for row in rows_k)
                    minbeam_lineage_id = min(
                        row["lineage_id"] for row in rows_k
                        if row["d_mid_over_ell"] == min_d_mid
                    )
                    for row in rows_k:
                        row["is_minbeam_at_k"] = int(row["lineage_id"] == minbeam_lineage_id)
                        probe_writer.writerow(dict(
                            seed=int(seed),
                            intensity=float(intensity),
                            K=int(K),
                            start_id=int(start_id),
                            depth_k=int(k + 1),
                            **row,
                        ))
                top1[k].append(dvals[0])           # order-only top-1 selection
                beammin[k].append(min(dvals))      # best retained hypothesis
        out[K] = dict(
            top1=[np.median(x) if x else np.nan for x in top1],
            beammin=[np.median(x) if x else np.nan for x in beammin],
            n_at=[len(x) for x in top1],
            reach=np.array(reach, float),
        )
        kbeam_stats[K] = dict(
            elapsed=float(time.perf_counter() - t0),
            starts=int(len(starts)),
            frontier_states=int(total_frontier_states),
            survivors=int(total_survivors),
            max_depth=int(max(reach) if reach else 0),
        )
    return dict(
        ell=ell,
        g_tail=np.array(g_tail, float),
        g_len=np.array(g_len, float),
        kbeam=out,
        dev=dev,
        N=emb.shape[0],
        perf=dict(
            seed=int(seed),
            intensity=float(intensity),
            elapsed_total=float(time.perf_counter() - t_seed0),
            t_link=float(t_link),
            t_starts=float(t_starts),
            t_greedy=float(t_greedy),
            n_starts=int(len(starts)),
            avg_outdeg=deg_stats["avg_outdeg"],
            max_outdeg=deg_stats["max_outdeg"],
            kbeam=kbeam_stats,
        ),
    )


# --------------------------------------------------------------------------- run
PROBE_FIELDS = [
    "seed", "intensity", "K", "start_id", "depth_k", "lineage_id",
    "survivor_rank_at_depth", "path_p", "path_q", "p_last", "q_last",
    "r_p_last", "r_q_last", "d_p_over_ell", "d_q_over_ell", "d_mid_over_ell",
    "straddles_horizon", "regscore", "is_top1", "is_minbeam_at_k",
]


def run(seeds, intensities, t_edge, device, probe_out=None, probe_k=None):
    probe_count = 0
    probe_fh = None
    probe_writer = None
    if probe_out:
        probe_fh = open(probe_out, "w", newline="", encoding="utf-8")
        probe_writer = csv.DictWriter(probe_fh, fieldnames=PROBE_FIELDS)
        probe_writer.writeheader()
    print(f"seeds={len(seeds)} {seeds}  t_edge={t_edge:.0f}  M={M}  lmax={LMAX} "
          f"min_len={MIN_LEN}  K={K_GRID}  k_ref={K_REF}  ADH={ADH:.0f}ℓ\n")
    for inten in intensities:
        t0 = time.perf_counter()
        rows = [measure_seed(s, inten, t_edge, device, probe_k=probe_k, probe_writer=probe_writer)
                for s in seeds]
        if probe_writer is not None and probe_k is not None:
            probe_count += sum(
                r["perf"]["kbeam"][probe_k]["survivors"]
                for r in rows
                if probe_k in r["perf"]["kbeam"]
            )
        ell = rows[0]["ell"]
        dev = rows[0]["dev"]
        perf_rows = [r["perf"] for r in rows]
        # single-tracer baseline
        gt = np.concatenate([r["g_tail"] for r in rows]) if rows else np.array([])
        gl = np.concatenate([r["g_len"] for r in rows]) if rows else np.array([])
        print(f"================ intensity {inten:g}  ℓ={ell:.4f}  N≈{rows[0]['N']}  "
              f"dev={dev}  [{time.perf_counter()-t0:.0f}s] ================")
        for p in perf_rows:
            print(f"  PERF seed={p['seed']} total={p['elapsed_total']:.2f}s "
                  f"link={p['t_link']:.2f}s starts={p['t_starts']:.2f}s "
                  f"greedy={p['t_greedy']:.2f}s n_starts={p['n_starts']} "
                  f"avg_outdeg={p['avg_outdeg']:.2f} max_outdeg={p['max_outdeg']}")
            for K in K_GRID:
                ks = p["kbeam"][K]
                print(f"    K={K:>2} kbeam={ks['elapsed']:.2f}s "
                      f"frontier_states={ks['frontier_states']} "
                      f"survivors={ks['survivors']} max_depth={ks['max_depth']}")
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
    if probe_fh is not None:
        probe_fh.close()
        print(f"probe_rows written: {probe_count} -> {probe_out}")


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true", help="2 seeds x {3600}, K<=8")
    ap.add_argument("--seeds", type=int, default=6)
    ap.add_argument("--device", default="auto", choices=["auto", "cpu", "gpu"])
    ap.add_argument("--intensities", default="", help="comma-separated intensities, e.g. 3600,7200")
    ap.add_argument("--probe-out", default="", help="optional CSV path for per-survivor/per-depth probe rows")
    ap.add_argument("--probe-k", type=int, default=64, help="K value to dump when --probe-out is set")
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
    if args.intensities:
        intensities = tuple(float(x) for x in args.intensities.split(",") if x.strip())
    assert_seeds(seeds)
    _xp, dev = backend.resolve_device(args.device)
    print(f"backend device = {dev}  (requested {args.device})\n")

    t0 = time.time()
    run(seeds, intensities, 6.0, args.device,
        probe_out=(args.probe_out or None),
        probe_k=args.probe_k)
    print(f"elapsed {time.time()-t0:.1f}s")
    assert_seal("post")
    print("done — exploration only; nothing frozen, no seed in RESERVED_002 touched.")


if __name__ == "__main__":
    main()
