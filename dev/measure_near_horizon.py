"""dev measurement (PR-003 roadmap point 3) — near-horizon, BRACKET-SEEDED
direction + localisation.

Turns the nan near-horizon AUC of explore_direction.py into a real number. The
two changes vs explore_direction:
  - seed ladders from the ORDER-ONLY v2 bracket boundary (boundary_minimals_
    invariant), not from random links -> ladders concentrate where it matters;
  - pool over the full EXPLORE_POOL and bin the near band in ELL units
    (k in {2,3,5} ell), reporting per band the #ladders and the out/in split so
    a reported AUC is only reported when BOTH classes are present.

Order-only throughout: the bracket and the ladders are built from the poset C
alone. Coordinates (r) are revealed ONLY to score — the truth direction
sign(delta r), the near-band mask, and d_perp. Never to seed, build, or select.
Leakage gate: docs/pr003_leakage_gate.md.

Run:  python3 dev/measure_near_horizon.py            # default pool
      python3 dev/measure_near_horizon.py --smoke    # few seeds, fast
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
FEATURES = ["phi_slope", "relphi_slope", "relphi_mean"]


def collect_bracket_ladders(seed, intensity, t_edge, min_len=6, lmax=120,
                            M=3, budget=30000):
    """Bracket-seeded LONGEST fuzzy ladders for one sprinkling (the abundant
    sample; the greedy 'first path' starves at this seeding). Returns rows
    (phi_slope, relphi_slope, relphi_mean, dir_true, mean_r, dperp_over_ell, ln,
    complete). Order-only build; r revealed only for the score fields."""
    emb, _, _ = generator.numpy_sprinkle(seed, float(intensity), float(t_edge))
    C = generator.past_matrix_fast(emb, "BH")
    ell = thresholds.ell(intensity)
    Lpast, Lfut = order_only_heights(C)
    rel_phi = rel_field(Lfut, Lpast)
    _, indptr, idx = XL.link_future_csr(C)
    bmin = boundary_minimals_invariant(C)            # ORDER-ONLY seed set
    rows = []
    for m in bmin:
        for t in range(int(indptr[m]), int(indptr[m + 1])):
            q1 = int(idx[t])
            bl, comp, _, _, _, lpb, _ = longest_censored(
                int(m), q1, indptr, idx, C, M, lmax, budget)
            if bl < min_len:
                continue
            p = lpb[:bl]
            i = np.arange(bl, dtype=float)
            relphi = rel_phi[p]
            f_relphi_mean = float(relphi.mean())
            f_relphi_slope = float(np.polyfit(i, relphi, 1)[0])
            f_phi_slope = float(np.polyfit(i, Lfut[p].astype(float), 1)[0])
            r = emb[p, 1]                              # TRUTH — score only
            dir_true = float(np.sign(r[-1] - r[0]))
            mean_r = float(r.mean())
            dperp = float(np.median(np.abs(r - R_S)) / ell)
            rows.append((f_phi_slope, f_relphi_slope, f_relphi_mean,
                         dir_true, mean_r, dperp, bl, int(comp)))
    return rows, ell


def _band_report(rows, ell, k):
    """rows = pooled (feat0,feat1,feat2,dir,mean_r,dperp/ell,ln). Restrict to the
    |mean_r - R_S| < k*ell band and print AUC per feature + class counts + d_perp."""
    a = np.array([r[:3] for r in rows], float)
    dir_true = np.array([r[3] for r in rows])
    mean_r = np.array([r[4] for r in rows])
    dperp = np.array([r[5] for r in rows])
    mask = np.abs(mean_r - R_S) < k * ell
    pos = dir_true > 0
    n = int(mask.sum())
    n_out = int((mask & pos).sum())
    n_in = int((mask & ~pos).sum())
    head = f"  band <{k}ell : ladders={n:>4}  (out {n_out:>3} / in {n_in:>3})"
    if n_out == 0 or n_in == 0:
        print(head + "   AUC undefined (one class empty)")
        return
    dmed = float(np.median(dperp[mask]))
    aucs = "  ".join(f"{name}={auc(a[mask, j], pos[mask]):.3f}"
                     for j, name in enumerate(FEATURES))
    print(head + f"   d_perp/ell(med)={dmed:.2f}")
    print(f"            AUC[{aucs}]")


def run(seeds, intensity=3600.0, t_edge=6.0):
    ell = thresholds.ell(intensity)
    print(f"PR-003 point 3 — near-horizon, bracket-seeded direction + d_perp")
    print(f"seeds={len(seeds)}  intensity={intensity:.0f}  t_edge={t_edge:.0f}  "
          f"ell={ell:.4f}  R_S={R_S}\n")
    pooled = []
    for s in seeds:
        t0 = time.perf_counter()
        rows, _ = collect_bracket_ladders(s, intensity, t_edge)
        pooled += rows
        print(f"  seed={s}  bracket-seeded ladders>=6 = {len(rows):>3} "
              f"[{time.perf_counter()-t0:.1f}s]")
    if not pooled:
        print("\nno ladders pooled"); return pooled
    pos_all = np.array([r[3] for r in pooled]) > 0
    print(f"\n=== POOLED ({len(pooled)} ladders; out {int(pos_all.sum())} / "
          f"in {int((~pos_all).sum())}) ===")
    a = np.array([r[:3] for r in pooled], float)
    for j, name in enumerate(FEATURES):
        print(f"  AUC(all bands)  {name:<13} = {auc(a[:, j], pos_all):.3f}")
    print()
    for k in (2, 3, 5):
        _band_report(pooled, ell, k)
    return pooled


if __name__ == "__main__":
    smoke = "--smoke" in sys.argv
    pool = EXPLORE_POOL[:3] if smoke else EXPLORE_POOL[:12]
    run(list(pool))
