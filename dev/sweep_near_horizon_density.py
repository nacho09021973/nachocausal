"""dev measurement (PR-003 roadmap point 3, density sweep) — does the
bracket-seeded ladder track the horizon at the DISCRETENESS FLOOR?

The binding question after measure_near_horizon: the longest bracket-seeded
ladder sits at d_perp ~ 3 ell near the horizon. Is that a DENSITY artifact that
shrinks toward O(1)*ell (-> d_perp -> 0 physical as ell -> 0, convergence holds,
freeze-able) or a FIXED offset of longest selection (-> #3 must be redesigned)?

Hold the box (t_edge) fixed and raise the intensity so ell shrinks
(ell ∝ intensity^-1/2). Read the verdict off the FIRST-3-rung d_perp/ell vs
intensity: the first rungs are near the horizon by seed construction, so this is
unbiased by any position band. Constant/decreasing -> converges; increasing ->
longest selection diverges in ell units.

Order-only build; coords reveal only to score d_perp / direction / near mask.
Leakage gate: docs/pr003_leakage_gate.md.

Run:  python3 dev/sweep_near_horizon_density.py            # 6 seeds x {3600,7200,14400}
      python3 dev/sweep_near_horizon_density.py --smoke    # 2 seeds x {3600,7200}
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
from explore_direction import order_only_heights, rel_field, auc  # noqa: E402
from measure_pr003 import boundary_minimals_invariant, longest_censored  # noqa: E402

R_S = thresholds.R_S


def collect_profile(seed, intensity, t_edge, min_len=6, lmax=120, M=3, budget=30000):
    """Per bracket-seeded longest ladder, return (first3, tail, overall) d_perp/ell,
    the relphi_mean direction feature, dir_true, |mean_r-R_S|/ell, length, complete.
    first3 = rungs 0..2 (near the seed / horizon); tail = rungs 3.. ."""
    emb, _, _ = generator.numpy_sprinkle(seed, float(intensity), float(t_edge))
    C = generator.past_matrix_fast(emb, "BH")
    ell = thresholds.ell(intensity)
    Lpast, Lfut = order_only_heights(C)
    rel_phi = rel_field(Lfut, Lpast)
    _, indptr, idx = XL.link_future_csr(C)
    bmin = boundary_minimals_invariant(C)
    rows = []
    for m in bmin:
        for t in range(int(indptr[m]), int(indptr[m + 1])):
            q1 = int(idx[t])
            bl, comp, _, _, _, lpb, _ = longest_censored(
                int(m), q1, indptr, idx, C, M, lmax, budget)
            if bl < min_len:
                continue
            p = lpb[:bl]
            d = np.abs(emb[p, 1] - R_S) / ell           # TRUTH — score only
            first3 = float(np.median(d[:3]))
            tail = float(np.median(d[3:])) if bl > 3 else float("nan")
            overall = float(np.median(d))
            relphi_mean = float(rel_phi[p].mean())
            r = emb[p, 1]
            dir_true = float(np.sign(r[-1] - r[0]))
            absr = float(abs(float(r.mean()) - R_S) / ell)
            rows.append((first3, tail, overall, relphi_mean, dir_true, absr,
                         bl, int(comp)))
    return rows, ell


def _med_iqr(vals):
    v = np.array([x for x in vals if np.isfinite(x)], float)
    if v.size == 0:
        return float("nan"), float("nan"), float("nan")
    return (float(np.median(v)), float(np.percentile(v, 25)),
            float(np.percentile(v, 75)))


def run(seeds, intensities, t_edge=6.0, near_k=3.0):
    print(f"PR-003 point 3 — density sweep of near-horizon d_perp/ell")
    print(f"seeds={len(seeds)}  t_edge={t_edge:.0f}  near band <{near_k:.0f}ell  "
          f"R_S={R_S}\n")
    summary = []
    for inten in intensities:
        pooled = []
        t0 = time.perf_counter()
        for s in seeds:
            rows, ell = collect_profile(s, inten, t_edge)
            pooled += rows
        if not pooled:
            print(f"intensity={inten:.0f}: no ladders"); continue
        first3 = [r[0] for r in pooled]
        tail = [r[1] for r in pooled]
        overall = [r[2] for r in pooled]
        feat = np.array([r[3] for r in pooled])
        dir_true = np.array([r[4] for r in pooled])
        absr = np.array([r[5] for r in pooled])
        pos = dir_true > 0
        near = absr < near_k
        f3m, f3lo, f3hi = _med_iqr(first3)
        tlm, _, _ = _med_iqr(tail)
        ovm, _, _ = _med_iqr(overall)
        auc_all = auc(feat, pos)
        n_near_out = int((near & pos).sum())
        n_near_in = int((near & ~pos).sum())
        auc_near = (auc(feat[near], pos[near])
                    if n_near_out and n_near_in else float("nan"))
        ell = thresholds.ell(inten)
        print(f"intensity={inten:>6.0f}  ell={ell:.4f}  ladders={len(pooled):>4} "
              f"[{time.perf_counter()-t0:.0f}s]")
        print(f"   d_perp/ell  first3={f3m:.2f} [{f3lo:.2f},{f3hi:.2f}]   "
              f"tail={tlm:.2f}   overall={ovm:.2f}")
        print(f"   direction relphi_mean  AUC(all)={auc_all:.3f}  "
              f"AUC(<{near_k:.0f}ell)={auc_near:.3f}  "
              f"near out/in={n_near_out}/{n_near_in}\n")
        summary.append((inten, ell, f3m, tlm, ovm, auc_all))

    print("=== VERDICT READ-OFF: d_perp/ell vs intensity (head vs tail) ===")
    for inten, ell, f3m, tlm, ovm, a in summary:
        print(f"   intensity={inten:>6.0f}  ell={ell:.4f}  "
              f"first3={f3m:.2f}  tail={tlm:.2f}")

    def _trend(vals):
        v = [x for x in vals if np.isfinite(x)]
        if len(v) < 2:
            return "n/a"
        mono_up = all(v[i + 1] > v[i] for i in range(len(v) - 1))
        mono_dn = all(v[i + 1] < v[i] for i in range(len(v) - 1))
        spread = max(v) - min(v)
        if mono_up:
            return f"MONOTONE-INCREASING ({v[0]:.2f}->{v[-1]:.2f}) -> diverges in ell units"
        if mono_dn:
            return f"MONOTONE-DECREASING ({v[0]:.2f}->{v[-1]:.2f}) -> shrinks below the floor"
        return (f"NON-MONOTONIC / FLAT (range {spread:.2f}) -> bounded in ell units "
                f"=> d_perp -> 0 physical (tracks the floor)")

    if len(summary) >= 2:
        print(f"\n   first3 (head, near the seed): {_trend([s[2] for s in summary])}")
        print(f"   tail   (body of the ladder): {_trend([s[3] for s in summary])}")
    return summary


if __name__ == "__main__":
    smoke = "--smoke" in sys.argv
    if smoke:
        run(list(EXPLORE_POOL[:2]), [3600.0, 7200.0])
    else:
        run(list(EXPLORE_POOL[:6]), [3600.0, 7200.0, 14400.0])
