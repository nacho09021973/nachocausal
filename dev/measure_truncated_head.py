"""dev measurement (PR-003 roadmap point 3 -> the SINGLE next question) — does a
head truncated by a rule defined ONLY on causal observables produce a CONNECTED
sequence whose distance to the horizon stays O(ell)?

Yesterday's verdict (dev/PR003_NEAR_HORIZON_NOTES.md): the LONGEST bracket-seeded
ladder gets length by DRIFTING — its tail d_perp/ell grows 4.37 -> 6.17 -> 7.56 over
a 4x density sweep, while the head (first-3 rungs) stays bounded ~2.5 ell. Horizon
information concentrates in the head; later growth optimises length, not adherence.

Before BRANCHING into several "near-staying" selection rules (roadmap point 2), this
script measures the one thing that forces the design: the d_perp/ell PROFILE per
prefix length k along the longest ladder, across the density sweep. It answers,
without inventing a stopping rule:

  * CONNECTED?  Every truncated prefix is a chain of future links by construction;
    we VERIFY it (consecutive p- and q-rungs are causally related in C) and report
    the connected fraction.
  * O(ell)?  For each prefix length k we report median d_perp/ell, so we can read off
    k* = the longest prefix that still adheres at the discreteness floor, and whether
    k* (in rungs and in physical units) is STABLE / GROWS as density rises. A head
    that only ever reaches k*~3 is just the seed re-localisation (prereg-002), NOT a
    reconstructed horizon segment; a k* that grows with density is a real segment.
  * Order-only DETECTABLE?  We overlay the cumulative rel_phi (the #2 direction
    feature) so we can later check whether the adherence breakpoint is visible in an
    order observable alone (precondition for a freeze-able truncation rule).
  * GREEDY contrast.  The greedy ladder (stop at first-stuck) is the order-only
    truncation already in the codebase. We report its length and d_perp so we know
    whether "staying near" is bought by staying SHORT (trivial) or not.

Order-only build; coordinates reveal only to score d_perp (never to seed/build/cut).
Leakage gate: docs/pr003_leakage_gate.md. NOTHING here is frozen.

Run:  python3 dev/measure_truncated_head.py            # 6 seeds x {3600,7200,14400}
      python3 dev/measure_truncated_head.py --smoke    # 2 seeds x {3600,7200}
"""

from __future__ import annotations

import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import generator, thresholds  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402
import explore_ladders as XL  # noqa: E402
from explore_direction import (greedy_ladder, order_only_heights,  # noqa: E402
                               rel_field)
from measure_pr003 import boundary_minimals_invariant, longest_censored  # noqa: E402

R_S = thresholds.R_S
KMAX = 16                      # report the profile out to this prefix length (rungs)
ADH = 3.0                      # reference adherence band in ell (NOT a frozen threshold)


def _connected(p, q, C):
    """True iff every consecutive rung is causally related in C (a chain)."""
    for i in range(len(p) - 1):
        if not (C[p[i + 1], p[i]] and C[q[i + 1], q[i]]):
            return False
    return True


def collect(seed, intensity, t_edge, min_len=6, lmax=120, M=3, budget=30000):
    """Per bracket-seeded longest ladder: the full per-rung d_perp/ell array, the
    cumulative-mean rel_phi per prefix, length, completeness, connectedness; plus
    the greedy ladder length and d_perp/ell from the same seed rung."""
    emb, _, _ = generator.numpy_sprinkle(seed, float(intensity), float(t_edge))
    C = generator.past_matrix_fast(emb, "BH")
    ell = thresholds.ell(intensity)
    Lpast, Lfut = order_only_heights(C)
    rel_phi = rel_field(Lfut, Lpast)
    _, indptr, idx = XL.link_future_csr(C)
    bmin = boundary_minimals_invariant(C)
    long_rows, greedy_lens, greedy_tail = [], [], []
    for m in bmin:
        for t in range(int(indptr[m]), int(indptr[m + 1])):
            q1 = int(idx[t])
            bl, comp, _, _, _, lpb, lqb = longest_censored(
                int(m), q1, indptr, idx, C, M, lmax, budget)
            if bl >= min_len:
                p = lpb[:bl]
                q = lqb[:bl]
                d = np.abs(emb[p, 1] - R_S) / ell           # TRUTH — score only
                rphi_cum = np.cumsum(rel_phi[p]) / np.arange(1, bl + 1)
                long_rows.append((d, rphi_cum, int(bl), int(comp),
                                  _connected(p, q, C)))
            gln, gpb = greedy_ladder(int(m), q1, indptr, idx, C, M, lmax)
            if gln >= min_len:
                gp = gpb[:gln]
                gd = np.abs(emb[gp, 1] - R_S) / ell
                greedy_lens.append(int(gln))
                greedy_tail.append(float(np.median(gd[3:])) if gln > 3
                                   else float("nan"))
    return long_rows, greedy_lens, greedy_tail, ell


def _profile(long_rows):
    """median d_perp/ell and median cumulative rel_phi at each prefix length k."""
    dprof, pprof, nprof = [], [], []
    for k in range(KMAX):
        dk = [r[0][k] for r in long_rows if r[2] > k]
        pk = [r[1][k] for r in long_rows if r[2] > k]
        nprof.append(len(dk))
        dprof.append(float(np.median(dk)) if dk else float("nan"))
        pprof.append(float(np.median(pk)) if pk else float("nan"))
    return dprof, pprof, nprof


def _kstar(dprof):
    """longest prefix whose median d_perp/ell stays <= ADH (contiguous from k=0)."""
    ks = 0
    for k in range(KMAX):
        if np.isfinite(dprof[k]) and dprof[k] <= ADH:
            ks = k + 1
        else:
            break
    return ks


def run(seeds, intensities, t_edge=6.0):
    print("PR-003 — single next question: how long a CONNECTED order-only head "
          "stays O(ell)?")
    print(f"seeds={len(seeds)}  t_edge={t_edge:.0f}  R_S={R_S}  "
          f"adherence ref={ADH:.0f}ell  Kmax={KMAX}\n")
    summary = []
    for inten in intensities:
        pooled, glens, gtail, per_seed_kstar = [], [], [], []
        t0 = time.perf_counter()
        for s in seeds:
            lr, gl, gt, ell = collect(s, inten, t_edge)
            pooled += lr
            glens += gl
            gtail += gt
            if lr:                                    # per-seed k* (dispersion, R1)
                per_seed_kstar.append(_kstar(_profile(lr)[0]))
        if not pooled:
            print(f"intensity={inten:.0f}: no ladders"); continue
        dprof, pprof, nprof = _profile(pooled)
        kstar = _kstar(dprof)                         # pooled k*
        conn = np.mean([r[4] for r in pooled])
        comp_frac = np.mean([r[3] for r in pooled])   # complete-search fraction (R1)
        ell = thresholds.ell(inten)
        psk = np.array(per_seed_kstar, float)
        psk_str = (f"{np.median(psk):.0f} [{psk.min():.0f},{psk.max():.0f}] n={psk.size}"
                   if psk.size else "n/a")
        print(f"intensity={inten:>6.0f}  ell={ell:.4f}  longest_ladders={len(pooled):>4}"
              f"  connected={conn:.0%}  complete={comp_frac:.0%}  "
              f"[{time.perf_counter()-t0:.0f}s]")
        head = " ".join(f"{dprof[k]:4.1f}" if np.isfinite(dprof[k]) else "  . "
                        for k in range(KMAX))
        nrow = " ".join(f"{nprof[k]:4d}" for k in range(KMAX))
        prow = " ".join(f"{pprof[k]:+4.1f}" if np.isfinite(pprof[k]) else "  . "
                        for k in range(KMAX))
        print(f"   k        : " + " ".join(f"{k:4d}" for k in range(KMAX)))
        print(f"   d_perp/ell: {head}")
        print(f"   relphi_cum: {prow}")
        print(f"   n(len>k)  : {nrow}")
        gl = np.array(glens, float)
        gt = np.array([x for x in gtail if np.isfinite(x)], float)
        print(f"   k* (prefix staying <= {ADH:.0f}ell) = {kstar} rungs  "
              f"->  physical {kstar*ell:.3f}  ({kstar} ell-floors)   "
              f"per-seed k* median[min,max]={psk_str}")
        print(f"   GREEDY  len median={np.median(gl):.0f} "
              f"[{np.percentile(gl,25):.0f},{np.percentile(gl,75):.0f}]  "
              f"n={gl.size}  tail d_perp/ell median="
              f"{(np.median(gt) if gt.size else float('nan')):.2f}\n")
        summary.append((inten, ell, kstar, conn,
                        float(np.median(gl)) if gl.size else float("nan"),
                        float(np.median(gt)) if gt.size else float("nan")))

    print("=== VERDICT READ-OFF ===")
    print(f"{'intensity':>9} {'ell':>7} {'k*(rungs)':>9} {'k*·ell':>8} "
          f"{'connected':>9} {'greedy_len':>10} {'greedy_tail':>11}")
    for inten, ell, kstar, conn, gl, gt in summary:
        print(f"{inten:>9.0f} {ell:>7.4f} {kstar:>9d} {kstar*ell:>8.3f} "
              f"{conn:>8.0%} {gl:>10.1f} {gt:>11.2f}")
    if len(summary) >= 2:
        ells = [s[1] for s in summary]
        phys = [s[2] * s[1] for s in summary]            # k* in physical units
        # The discriminating quantity is the PHYSICAL extent of the adherent head.
        #   * tracks ell down (phys/ell ~ const)  -> seed re-localisation only.
        #   * stays ~constant while ell shrinks    -> a FIXED physical near-horizon
        #                                             segment (real, but bounded).
        #   * grows                                -> a lengthening segment.
        ratio = [p / e for p, e in zip(phys, ells)]      # == k* in ell-floors
        ell_drop = ells[0] / ells[-1]
        phys_drop = phys[0] / phys[-1] if phys[-1] else float("inf")
        print()
        print(f"   physical k*·ell : {phys[0]:.3f} -> {phys[-1]:.3f} "
              f"(x{1/phys_drop:.2f})   while ell shrank x{1/ell_drop:.2f}")
        print(f"   k* in ell-floors: {ratio[0]:.1f} -> {ratio[-1]:.1f}")
        if phys[-1] > phys[0] * 1.15:
            print("   => physical adherent length GROWS with density: a lengthening "
                  "order-only horizon segment.")
        elif phys[-1] < phys[0] * 0.85 and phys_drop >= 0.6 * ell_drop:
            print("   => physical adherent length tracks ell down: consistent with SEED "
                  "RE-LOCALISATION (prereg-002 floor), NOT a growing segment.")
        else:
            print("   => physical adherent length ~CONSTANT while ell shrinks: a FIXED "
                  "physical near-horizon segment captured at finer resolution (bounded, "
                  "but more than the bare seed floor).")
    return summary


if __name__ == "__main__":
    smoke = "--smoke" in sys.argv
    if smoke:
        run(list(EXPLORE_POOL[:2]), [3600.0, 7200.0])
    else:
        run(list(EXPLORE_POOL[:6]), [3600.0, 7200.0, 14400.0])
