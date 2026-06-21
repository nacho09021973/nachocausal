"""dev exploration — false-positive (iv) axis + confirm coverage (ii) on a fresh
exploration pool with real statistics.

NOT sealed (dev/). Uses EXPLORE_POOL (high band, disjoint from DEV + burned
VALIDATION; reserved 002 band untouched). Thresholds & sealed estimator unchanged.

Per intensity, over the pool, for variants:
  H/sealed : height observable + sealed two_means_split   (the v1 baseline)
  V/sealed : volume observable + sealed two_means_split   (coverage winner)
  V/gated  : volume + an ABSTAINING split (sep->0 when the 2-means "improvement"
             statistic is below tau, i.e. no real bimodality)  -> targets FP
reports: coverage (bracket covers R_S), median width/2M, fp (LOO), p_perm, sig.

Gate diagnostic: mean split-improvement (1 - SSE2/SSE1) for BH vs MINK. A gate can
cut FP only if BH improvement >> MINK improvement. tau is chosen BETWEEN the two
means here purely to SEE if separation exists (exploratory; a frozen tau would
need a principled, data-independent anchor in prereg-002).

Run:  .venv/bin/python dev/explore_fp.py
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import estimator, generator, thresholds, validate  # noqa: E402
from nachocausal.scoring import blind_bracket  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402

POOL = EXPLORE_POOL[:30]
INTENS = (3000.0, 6000.0, 12000.0)
TWO_M = thresholds.TWO_M


def observable(C, name):
    has_past = C.any(axis=1)
    minimal = [i for i in range(C.shape[0]) if not has_past[i]]
    if name == "height":
        O_by_min, min_idx, _ = estimator.estimate_O(C)
        return O_by_min, min_idx
    vol = C.sum(axis=0).astype(int)
    return {i: int(vol[i]) for i in minimal}, minimal


def split_stats(values):
    """sealed (thr, sep) plus the 2-means variance-explained 'improvement'."""
    thr, sep = estimator.two_means_split(values)
    o = np.sort(np.asarray(values, float)); n = o.size
    if n < 2:
        return thr, sep, 0.0
    best = np.inf
    for i in range(1, n):
        lo, hi = o[:i], o[i:]
        best = min(best, lo.var() * lo.size + hi.var() * hi.size)
    sse1 = o.var() * n
    imp = 1.0 - best / sse1 if sse1 > 0 else 0.0
    return thr, sep, float(imp)


def collect(inten):
    acc = {k: {"sepBH": [], "sepMK": [], "cov": [], "w": [], "impBH": [], "impMK": []}
           for k in ("height", "volume")}
    for s in POOL:
        emb, _, _ = generator.numpy_sprinkle(s, inten)  # one cloud, both kinds
        Cbh = generator.past_matrix_fast(emb, "BH")
        Cmk = generator.past_matrix_fast(emb, "MINK")
        for name in ("height", "volume"):
            ObBH, miBH = observable(Cbh, name)
            thrB, sepB, impB = split_stats([ObBH[i] for i in miBH])
            br = blind_bracket(ObBH, miBH, thrB, emb)
            ObMK, miMK = observable(Cmk, name)
            _, sepM, impM = split_stats([ObMK[i] for i in miMK])
            a = acc[name]
            a["sepBH"].append(sepB); a["sepMK"].append(sepM)
            a["impBH"].append(impB); a["impMK"].append(impM)
            if br["valid"] and np.isfinite(sepM):
                a["cov"].append(br["covers"])
                if br["clean"]:
                    a["w"].append(br["width"] / TWO_M)
    return acc


def variant_metrics(sepBH, sepMK, cov, w):
    sepBH, sepMK = np.array(sepBH, float), np.array(sepMK, float)
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
    print(f"EXPLORE_POOL[:30] = {POOL[0]}..{POOL[-1]}  (THETA_FP={thresholds.THETA_FP}, "
          f"P_PERM<={thresholds.P_PERM_THRESHOLD})\n")
    for inten in INTENS:
        acc = collect(inten)
        H, V = acc["height"], acc["volume"]
        impBH, impMK = np.mean(V["impBH"]), np.mean(V["impMK"])
        tau = 0.5 * (impBH + impMK)
        print(f"--- intensity {inten:.0f} ---")
        print(f"  split-improvement (volume): BH={impBH:.3f}  MINK={impMK:.3f}  "
              f"-> gate tau={tau:.3f}")
        print("  " + fmt("H/sealed", variant_metrics(H["sepBH"], H["sepMK"], H["cov"], H["w"])))
        print("  " + fmt("V/sealed", variant_metrics(V["sepBH"], V["sepMK"], V["cov"], V["w"])))
        # gated: zero sep where improvement < tau (abstain on no real bimodality)
        gBH = [s if i >= tau else 0.0 for s, i in zip(V["sepBH"], V["impBH"])]
        gMK = [s if i >= tau else 0.0 for s, i in zip(V["sepMK"], V["impMK"])]
        print("  " + fmt("V/gated", variant_metrics(gBH, gMK, V["cov"], V["w"])))
        print()


if __name__ == "__main__":
    run()
