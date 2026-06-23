#!/usr/bin/env python
"""
DEV (Phase 0): validate Hartigan's dip test as the frozen theta_sig, in its OWN
venv (~/nachocausal-dip-venv with `diptest`), NOT the Minz venv. NOT a result.

diptest is the canonical implementation of Hartigan & Hartigan (1985); here it is
the validated reference. We do two things:

 A. CALIBRATION + POWER on synthetic data at the small sample sizes that matter
    (|minimal| ~ 15-80 in our sweeps), because the dip runs on the O multiset whose
    size is the NUMBER OF MINIMAL ELEMENTS, not N:
      - unimodal nulls (uniform, normal): fraction with p<0.01 must be ~1%
        (false-positive control; informs theta_fp too);
      - bimodal alternatives (separated 2-component mixtures): fraction with
        p<0.01 = power.
 B. REAL DATA: load dev/o_samples.json (tall box) and report dip + p for BH vs the
    box-matched MINK control, aggregated by (kind, N). theta_sig is meaningful only
    if BH reaches p<0.01 robustly while MINK does not.
"""
from __future__ import annotations
import json, os
import numpy as np
import diptest

RNG = np.random.default_rng(0)

def frac_significant(sampler, n, trials=2000, alpha=0.01):
    c = 0
    for _ in range(trials):
        x = sampler(n)
        _, p = diptest.diptest(np.asarray(x, float))
        c += (p < alpha)
    return c / trials

def unif(n):  return RNG.random(n)
def norm(n):  return RNG.standard_normal(n)
def bimodal(sep):
    def s(n):
        k = RNG.integers(0, 2, n)
        return RNG.standard_normal(n) + sep * k
    return s

def part_A():
    print("=== A. CALIBRATION + POWER (diptest, alpha=0.01) ===")
    print(f"{'n':>5} {'unif_fp':>8} {'norm_fp':>8} {'bi2.0':>7} {'bi3.0':>7} {'bi4.0':>7}")
    for n in (15, 30, 50, 80, 150, 300):
        row = [frac_significant(unif, n), frac_significant(norm, n),
               frac_significant(bimodal(2.0), n), frac_significant(bimodal(3.0), n),
               frac_significant(bimodal(4.0), n)]
        print(f"{n:>5} " + " ".join(f"{v:>8.3f}" if i < 2 else f"{v:>7.3f}"
                                    for i, v in enumerate(row)))
    print("  unif_fp/norm_fp = false-positive rate (want ~0.01); bi* = power vs "
          "2-Gaussian mixtures separated by 2/3/4 sigma.")

def part_B():
    path = "dev/o_samples.json"
    if not os.path.exists(path):
        print(f"\n(no {path} yet -- run dev/dump_o.py in the Minz venv first)")
        return
    recs = json.load(open(path))
    print("\n=== B. REAL O MULTISETS (tall box), dip p by (kind, N) ===")
    by = {}
    for r in recs:
        O = np.asarray(r["O"], float)
        if O.size < 4:
            d, p = float("nan"), float("nan")
        else:
            d, p = diptest.diptest(O)
        by.setdefault((r["kind"], r["intensity"]), []).append((r["N"], len(O), p))
    print(f"{'kind':>4} {'inten':>6} {'~N':>6} {'~|min|':>6} {'med_p':>7} {'frac_p<.01':>10}")
    for (kind, inten) in sorted(by, key=lambda k: (k[0], k[1])):
        rows = by[(kind, inten)]
        Ns = np.mean([x[0] for x in rows]); mins = np.mean([x[1] for x in rows])
        ps = np.array([x[2] for x in rows])
        medp = np.nanmedian(ps); frac = np.mean(ps < 0.01)
        print(f"{kind:>4} {inten:>6.0f} {int(Ns):>6} {int(mins):>6} "
              f"{medp:>7.3f} {frac:>10.2f}")

if __name__ == "__main__":
    part_A()
    part_B()
