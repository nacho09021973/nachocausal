"""dev exploration — pre-flight for the prereg-002 ABSTAINING gate with a
PRINCIPLED, data-independent tau(n).

Committee decision (2026-06-21): gate = abstain (sep->0) when the 2-means
variance-explained 'improvement' of the minimal-element observable is below
tau(n), where
    tau(n) = (1-alpha) quantile of 'improvement' under an ABSTRACT UNIFORM null
             at matched n  (alpha = 0.01 -> p99),
precomputed by Monte Carlo with a FIXED seed. Data-independent: the null is a
pure Uniform[0,1] MC, no project seeds, no sprinkling, no ground truth. n = the
number of minimal elements per cloud (order-only, observable without the
embedding).

This is dev/ pre-flight ONLY: it (a) measures the real n distribution to check
the auditor's red (n<=8 clouds where tau(n) could clip BH), and (b) re-runs the
FP bench with the gate improvement >= tau(n) to confirm (iv) still closes without
hurting BH coverage. Nothing here is sealed; thresholds & sealed estimator
untouched.

Run:  .venv/bin/python dev/explore_fp_gated.py
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import generator, thresholds, validate  # noqa: E402
from nachocausal.scoring import blind_bracket  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402

POOL = EXPLORE_POOL[:30]
INTENS = (3000.0, 6000.0, 12000.0)
TWO_M = thresholds.TWO_M
ALPHA = 0.01                 # fixed in advance -> tau(n) = p(1-alpha) = p99
NULL_MC_SEED = 20260621      # FROZEN MC seed for the abstract uniform null
NULL_MC_REPS = 40000


def improvement(values) -> float:
    """variance explained by the best 1-D 2-partition (== 2-means in 1D)."""
    o = np.sort(np.asarray(values, float)); n = o.size
    if n < 2:
        return 0.0
    best = np.inf
    for i in range(1, n):
        lo, hi = o[:i], o[i:]
        best = min(best, lo.var() * lo.size + hi.var() * hi.size)
    tot = o.var() * n
    return float(1.0 - best / tot) if tot > 0 else 0.0


def minimal_volume(C):
    has_past = C.any(axis=1)
    minimal = [i for i in range(C.shape[0]) if not has_past[i]]
    vol = C.sum(axis=0).astype(int)
    return {i: int(vol[i]) for i in minimal}, minimal


def build_tau_table(n_values):
    """tau(n) = (1-ALPHA) quantile of 'improvement' under Uniform[0,1] at each n.
    Pure abstract null; FROZEN seed; independent of any project data."""
    rng = np.random.default_rng(NULL_MC_SEED)
    tau = {}
    for n in sorted(set(int(n) for n in n_values if n >= 2)):
        vals = np.fromiter(
            (improvement(rng.random(n)) for _ in range(NULL_MC_REPS)),
            dtype=float, count=NULL_MC_REPS)
        tau[n] = float(np.quantile(vals, 1.0 - ALPHA))
    return tau


def collect(inten):
    rows = {"BH": [], "MK": []}   # each: (n, imp, sep, br or None)
    for s in POOL:
        emb, _, _ = generator.numpy_sprinkle(s, inten)
        for kind in ("BH", "MK"):
            C = generator.past_matrix_fast(emb, "BH" if kind == "BH" else "MINK")
            Ob, mi = minimal_volume(C)
            vals = [Ob[i] for i in mi]
            n = len(mi)
            imp = improvement(vals)
            from nachocausal import estimator
            thr, sep = estimator.two_means_split(vals)
            br = blind_bracket(Ob, mi, thr, emb) if kind == "BH" else None
            rows[kind].append((n, imp, sep, br))
    return rows


def metrics(rows, tau, gated):
    sepBH = []; cov = []; w = []
    for (n, imp, sep, br) in rows["BH"]:
        s = 0.0 if (gated and imp < tau.get(n, np.inf)) else sep
        sepBH.append(s)
        if br is not None and br["valid"]:
            cov.append(br["covers"])
            if br["clean"]:
                w.append(br["width"] / TWO_M)
    sepMK = []
    for (n, imp, sep, br) in rows["MK"]:
        s = 0.0 if (gated and imp < tau.get(n, np.inf)) else sep
        sepMK.append(s)
    sepBH = np.array(sepBH, float); sepMK = np.array(sepMK, float)
    d = sepBH - sepMK
    p = validate.signflip_perm_p(d)
    fp = validate.loo_fp_fraction(sepMK)
    return dict(cov=np.mean(cov) if cov else float("nan"),
                w=np.median(w) if w else float("nan"),
                fp=fp, p=p, sig=p <= thresholds.P_PERM_THRESHOLD,
                fp_ok=fp <= thresholds.THETA_FP)


def fmt(tag, m):
    return (f"{tag:<14}cov={m['cov']:.2f}  medW/2M={m['w']:.3f}  "
            f"fp={m['fp']:.3f} ({'ok' if m['fp_ok'] else 'NO'})  "
            f"p={m['p']:.2e} ({'sig' if m['sig'] else '--'})")


def run():
    print(f"alpha={ALPHA} (tau=p{int((1-ALPHA)*100)} uniform null)  "
          f"MC seed={NULL_MC_SEED} reps={NULL_MC_REPS}\n")
    all_rows = {inten: collect(inten) for inten in INTENS}
    all_n = [r[0] for inten in INTENS for k in ("BH", "MK") for r in all_rows[inten][k]]
    tau = build_tau_table(all_n)
    nmin, nmax = min(all_n), max(all_n)
    print(f"n (minimal elements per cloud): min={nmin} max={nmax}  "
          f"AUDITOR RED (n<=8)? {'YES -> '+str(sum(1 for n in all_n if n<=8))+' clouds' if any(n<=8 for n in all_n) else 'no'}")
    print("tau(n) sample:", {n: round(tau[n], 3) for n in sorted(set(all_n))[:6]}, "...\n")
    for inten in INTENS:
        rows = all_rows[inten]
        ns = [r[0] for k in ("BH", "MK") for r in rows[k]]
        print(f"--- intensity {inten:.0f} ---  n in [{min(ns)},{max(ns)}]")
        impBH = np.mean([r[1] for r in rows["BH"]])
        impMK = np.mean([r[1] for r in rows["MK"]])
        print(f"  improvement: BH={impBH:.3f}  MINK={impMK:.3f}")
        print("  " + fmt("V/sealed", metrics(rows, tau, gated=False)))
        print("  " + fmt("V/gated(tau_n)", metrics(rows, tau, gated=True)))
        print()


if __name__ == "__main__":
    run()
