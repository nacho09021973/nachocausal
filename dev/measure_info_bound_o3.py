"""dev measurement — PR-003 R1 / open item O3: NUMERICAL ILLUSTRATION of the
Le Cam two-point lower bound on order-only horizon localisation.
EXPLORATION ONLY — nothing frozen, not validated, not audited, no claim.

Авал: docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md §9 R1 /
open item O3 in dev/PR003_INFO_BOUND_NOTES.md:132-135. This is the numerical
companion to the analytic sketch there. It freezes nothing; it only measures, on
EXPLORE_POOL + a MINK control, how separable the *order distributions* are as the
hidden boundary is shifted, to check the constant K against the frozen K_LOC = 2.

What it measures (matched to the SEALED v2 observable)
-----------------------------------------------------
The sealed estimator reads the future-volume histogram O(i)=|future(i)| of the
minimal elements and reports a 2-means boundary -> a location estimate
r̂ = midpoint = 0.5*(r_lo+r_hi) (nachocausal/scoring/scorer.py:43,57). For a
two-point Le Cam reduction we place the TRUE boundary at r_S - s or r_S + s (the
SAME Poisson cloud, only the causal matrix r_S changes — exactly SAME_CLOUD,
thresholds.py:54) and ask: can ANY function of the order tell the two apart?

  (LC)  inf_{r̂} max_j E_j|r̂ - r_j|  >=  (s/2) * (1 - TV(P_0, P_1)).

We estimate, per frozen intensity (-> ℓ), three views of (P_0,P_1):
  A. ESTIMATOR-FAITHFUL (the bound "for THIS sealed estimator"): TV between the
     ensembles of the estimator's OWN output r̂ under r_S-s vs r_S+s. The Le Cam
     functional  bound(s) = (s/2)*(1 - TV(s))  is maximised over s; its argmax s*
     and value give  K_LeCam = bound(s*)/ℓ  to compare with K_LOC = 2.
  B. OBSERVABLE-MARGINAL (the §2 histogram-resolution object): Hellinger
     affinity / TV / KL between the pooled per-element future-volume pmfs at
     r_S-s vs r_S+s.
  C. BH-vs-MINK separability (the committee's literal O3 wording): Hellinger
     affinity between the pooled future-volume pmf of BH(r_S) and box-matched
     MINK on the same cloud.

r enters ONLY as a GENERATIVE parameter of the two known synthetic families
(this is a minimax information-geometry computation, not an estimator being
tuned): the estimator/observable never sees r. No RESERVED_002 seed is touched.

Honesty / scope (binding, per comité-003 §8 Le-Cam-scope resolution)
--------------------------------------------------------------------
  * This is an ILLUSTRATION of a lower bound FOR THIS estimator at the actual
    finite V, ρ — NOT a universal/asymptotic no-go, NOT a 3+1D claim, NOT a
    theorem (O1/O2 stay open).
  * View A (TV of r̂) is the genuine per-estimator quantity. Views B/C are
    *processed* statistics: by data-processing they UNDER-estimate the full-data
    TV, so a (1-TV) read off B/C OVER-states the floor — they are reported as
    context/sanity, NOT as the bound. The bound number quoted is from A.
  * GPU build is NOT bit-identical to the sealed CPU instrument (dev/backend.py
    docstring: np.log ulp flips near the horizon). --gpu-check quantifies that
    divergence at the ensemble level; the illustration tolerates it, the seal
    never uses it.

Run:
  dev/run-gpu.sh  with NACHO_MODULE=dev.measure_info_bound_o3   (WSL libcuda fix)
  or:  python3 dev/measure_info_bound_o3.py --smoke            # 4 seeds x {1500}
       python3 dev/measure_info_bound_o3.py                    # 24 seeds x all
       python3 dev/measure_info_bound_o3.py --device cpu       # CPU reference
       python3 dev/measure_info_bound_o3.py --gpu-check        # GPU vs CPU O agree
"""

from __future__ import annotations

import argparse
import hashlib
import math
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

from nachocausal import estimator, thresholds, generator  # noqa: E402
from nachocausal.scoring import blind_bracket  # noqa: E402
import explore_seeds  # noqa: E402
from explore_seeds import EXPLORE_POOL, in_reserved_002  # noqa: E402
import backend  # noqa: E402  (dev GPU backend)

# ---------------------------------------------------------------------------
# Frozen anchors (read-only; this script writes none of them).
# ---------------------------------------------------------------------------
SEAL_SHA = "6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4"
R_S = thresholds.R_S
K_LOC = thresholds.K_LOC

# Half-separation grid in units of ℓ (declared here, NOT tuned to the outcome).
S_OVER_ELL = (0.1, 0.15, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0, 4.0)
# TV histogram bin width as a principled fraction of the discreteness scale.
TV_BIN_FRAC = 0.25  # bins of width ℓ/4 over [r_S-5ℓ, r_S+5ℓ]


def seal_sha() -> str:
    p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     "nachocausal", "thresholds.py")
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def assert_seal(tag: str) -> None:
    got = seal_sha()
    print(f"[{tag}] thresholds.py sha256 = {got}")
    if got != SEAL_SHA:
        raise SystemExit(f"SEAL MISMATCH ({tag}): {got} != {SEAL_SHA}; aborting.")


def assert_seeds(seeds) -> None:
    pool = set(EXPLORE_POOL)
    for s in seeds:
        if s not in pool:
            raise SystemExit(f"seed {s} not in EXPLORE_POOL — refusing (leakage guard).")
        if in_reserved_002(s):
            raise SystemExit(f"seed {s} is in the RESERVED_002 band — refusing.")


def git_branch() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()
    except Exception:
        return "?"


# ---------------------------------------------------------------------------
# Order-only observable on the chosen device.
# ---------------------------------------------------------------------------
def o_and_min(C, xp):
    """Future-volume O(i)=|future(i)| for minimal elements, from C ALONE.
    Keeps the N x N matrix on-device; only moves O(N) vectors to host."""
    has_past = C.any(axis=1)            # (N,) device bool
    vol = C.sum(axis=0)                 # (N,) device int = |future(i)|
    has_past_h = backend.to_host(has_past)
    vol_h = backend.to_host(vol).astype(int)
    min_idx = np.nonzero(~has_past_h)[0].tolist()
    O_by_min = {int(i): int(vol_h[i]) for i in min_idx}
    return O_by_min, min_idx


def r_hat_and_O(emb, kind, rs, device):
    """Build the (BH or MINK) order on the same cloud at boundary rs, return the
    estimator's location estimate r̂ (=midpoint) and the per-element O list."""
    C, dev = backend.past_matrix(emb, kind, r_S=rs, device=device)
    O_by_min, min_idx = o_and_min(C, np)  # backend funcs return xp arrays; to_host inside
    del C
    if len(min_idx) < 2:
        return float("nan"), [], dev
    vals = [O_by_min[i] for i in min_idx]
    thr, sep = estimator.two_means_split(vals)
    br = blind_bracket(O_by_min, min_idx, thr, emb)
    return (br["midpoint"] if br["valid"] else float("nan")), vals, dev


# ---------------------------------------------------------------------------
# Divergences between empirical distributions.
# ---------------------------------------------------------------------------
def hellinger_affinity_pmf(a, b):
    """Bhattacharyya/Hellinger affinity Σ√(p·q) of two integer-valued samples."""
    a = np.asarray(a, int)
    b = np.asarray(b, int)
    if a.size == 0 or b.size == 0:
        return float("nan"), float("nan"), float("nan")
    lo = min(a.min(), b.min())
    hi = max(a.max(), b.max())
    bins = np.arange(lo, hi + 2)
    pa = np.histogram(a, bins=bins)[0].astype(float); pa /= pa.sum()
    pb = np.histogram(b, bins=bins)[0].astype(float); pb /= pb.sum()
    aff = float(np.sum(np.sqrt(pa * pb)))           # Hellinger affinity in [0,1]
    tv = float(0.5 * np.sum(np.abs(pa - pb)))       # total variation in [0,1]
    m = (pa > 0) & (pb > 0)
    kl = float(np.sum(pa[m] * np.log(pa[m] / pb[m])))
    return aff, tv, kl


def tv_gaussian(mu0, mu1, sd):
    """TV between N(mu0,sd^2) and N(mu1,sd^2) (equal-variance closed form)."""
    if not (sd > 0) or not math.isfinite(mu0) or not math.isfinite(mu1):
        return float("nan")
    d = abs(mu1 - mu0)
    return float(math.erf(d / (2.0 * sd * math.sqrt(2.0))))


def tv_histogram(x0, x1, ell):
    """Empirical TV between two r̂ samples on ℓ/4 bins over [r_S-5ℓ, r_S+5ℓ]."""
    x0 = np.asarray([v for v in x0 if math.isfinite(v)], float)
    x1 = np.asarray([v for v in x1 if math.isfinite(v)], float)
    if x0.size == 0 or x1.size == 0:
        return float("nan")
    w = TV_BIN_FRAC * ell
    bins = np.arange(R_S - 5 * ell, R_S + 5 * ell + w, w)
    p0 = np.histogram(x0, bins=bins)[0].astype(float); p0 /= max(p0.sum(), 1)
    p1 = np.histogram(x1, bins=bins)[0].astype(float); p1 /= max(p1.sum(), 1)
    return float(0.5 * np.sum(np.abs(p0 - p1)))


# ---------------------------------------------------------------------------
# GPU/CPU agreement diagnostic (O3 honesty: GPU build is not bit-identical).
# ---------------------------------------------------------------------------
def gpu_check(seeds, intensity):
    print("\n=== GPU-vs-CPU agreement on per-element future-volume O (BH, r_S) ===")
    for seed in seeds:
        emb, _, _ = generator.numpy_sprinkle(seed, intensity)
        Cg, dg = backend.past_matrix(emb, "BH", r_S=R_S, device="gpu")
        Cc, dc = backend.past_matrix(emb, "BH", r_S=R_S, device="cpu")
        og, mg = o_and_min(Cg, np)
        oc, mc = o_and_min(Cc, np)
        va = np.array(sorted(og.values())); vb = np.array(sorted(oc.values()))
        same_min = (mg == mc)
        if va.size == vb.size:
            md = int(np.max(np.abs(va - vb))) if va.size else 0
            mism = int(np.sum(va != vb))
        else:
            md, mism = -1, -1
        print(f"  seed {seed}: N={emb.shape[0]} |min| gpu={len(mg)} cpu={len(mc)} "
              f"same_min={same_min} O-multiset maxdiff={md} mismatches={mism}")
        del Cg, Cc


# ---------------------------------------------------------------------------
# Main sweep.
# ---------------------------------------------------------------------------
def run(seeds, intensities, device):
    print(f"\nseeds: {len(seeds)} from EXPLORE_POOL {seeds[0]}..{seeds[-1]}")
    print(f"intensities: {intensities}")
    print(f"s/ℓ grid: {S_OVER_ELL}    K_LOC (frozen) = {K_LOC}\n")
    for lam in intensities:
        ell = thresholds.ell(lam)
        print(f"================ intensity {lam:g}  (ℓ = {ell:.4f}) ================")
        # Pre-sample clouds + the BH(r_S)/MINK pools (for view C) once per seed.
        O_bh_true, O_mink, rhat_true = [], [], []
        clouds = {}
        for seed in seeds:
            emb, _, _ = generator.numpy_sprinkle(seed, lam)
            clouds[seed] = emb
            r0, ob, _ = r_hat_and_O(emb, "BH", R_S, device)
            _, om, _ = r_hat_and_O(emb, "MINK", R_S, device)
            O_bh_true += ob
            O_mink += om
            rhat_true.append(r0)
        # Precision floor: scatter of the estimator's own r̂ at the TRUE boundary.
        sd_true = float(np.nanstd(rhat_true))
        bias_true = float(np.nanmean(rhat_true) - R_S)
        print(f"  [view A: precision]  r̂ at r_S: scatter sd={sd_true:.4f} "
              f"= {sd_true/ell:.2f}·ℓ   bias={bias_true:+.4f} = {bias_true/ell:+.2f}·ℓ")
        affC, tvC, klC = hellinger_affinity_pmf(O_bh_true, O_mink)
        print(f"  [view C] BH(r_S) vs MINK   Hellinger affinity={affC:.3f} "
              f"TV={tvC:.3f} KL={klC:.3f}   (sanity; not the bound)")
        print(f"  {'s/ℓ':>5} {'2s':>7} {'TVg(r̂)':>8} {'TVh(r̂)':>8} "
              f"{'bound':>8} {'b/ℓ':>6} | {'affO':>6} {'TVo':>6} {'KLo':>6}")
        best = (-1.0, None)  # (bound, s)
        tv_curve = []        # (s/ℓ, TVg) for the resolvable-separation read
        for q in S_OVER_ELL:
            s = q * ell
            r0, r1, Oa, Ob = [], [], [], []
            for seed in seeds:
                emb = clouds[seed]
                rm, oa, _ = r_hat_and_O(emb, "BH", R_S - s, device)
                rp, ob, _ = r_hat_and_O(emb, "BH", R_S + s, device)
                r0.append(rm); r1.append(rp)
                Oa += oa; Ob += ob
            m0 = np.nanmean(r0); m1 = np.nanmean(r1)
            sd = np.sqrt(0.5 * (np.nanvar(r0) + np.nanvar(r1)))
            tvg = tv_gaussian(m0, m1, sd)
            tvh = tv_histogram(r0, r1, ell)
            bound = 0.5 * s * (1.0 - tvg) if math.isfinite(tvg) else float("nan")
            affO, tvO, klO = hellinger_affinity_pmf(Oa, Ob)
            print(f"  {q:>5.2f} {2*s:>7.4f} {tvg:>8.3f} {tvh:>8.3f} "
                  f"{bound:>8.4f} {bound/ell:>6.2f} | {affO:>6.3f} {tvO:>6.3f} {klO:>6.3f}")
            if math.isfinite(bound) and bound > best[0]:
                best = (bound, s)
            if math.isfinite(tvg):
                tv_curve.append((q, tvg))
        bnd, sstar = best
        # Resolvable half-separation: interpolate s/ℓ where TVg crosses 0.5.
        s50 = float("nan")
        for (qa, ta), (qb, tb) in zip(tv_curve, tv_curve[1:]):
            if (ta - 0.5) * (tb - 0.5) <= 0 and tb != ta:
                s50 = qa + (0.5 - ta) * (qb - qa) / (tb - ta)
                break
        print(f"  -> resolvable separation: TVg(r̂)=0.5 at s/ℓ≈{s50:.2f} "
              f"(2s/ℓ≈{2*s50:.2f}); Le Cam max (s/2)(1-TV)={bnd:.4f}={bnd/ell:.2f}·ℓ "
              f"at s*/ℓ={sstar/ell:.2f}   [floor ∝ ℓ; K_LOC={K_LOC} is conservative]\n")


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true", help="4 seeds x intensity 1500")
    ap.add_argument("--seeds", type=int, default=24, help="how many EXPLORE_POOL seeds")
    ap.add_argument("--device", default="auto", choices=["auto", "cpu", "gpu"])
    ap.add_argument("--gpu-check", action="store_true",
                    help="report GPU-vs-CPU O agreement and exit")
    return ap.parse_args()


def main():
    args = parse_args()
    print("PR-003 R1/O3 — Le Cam two-point numerical illustration (dev, NOT a result)")
    print(f"UTC {datetime.now(timezone.utc).isoformat()}  host {platform.node()}")
    print(f"git branch = {git_branch()}  python {platform.python_version()} "
          f"numpy {np.__version__}")
    assert_seal("pre")

    if args.smoke:
        seeds = list(EXPLORE_POOL[:4]); intensities = (1500.0,)
    else:
        seeds = list(EXPLORE_POOL[:args.seeds]); intensities = thresholds.INTENSITIES
    assert_seeds(seeds)

    # Touch device once to print which backend we got.
    _xp, dev = backend.resolve_device(args.device)
    print(f"backend device = {dev}  (requested {args.device})")

    t0 = time.time()
    if args.gpu_check:
        gpu_check(EXPLORE_POOL[:2], 1500.0)
        gpu_check(EXPLORE_POOL[:2], 12000.0)
    else:
        run(seeds, intensities, args.device)
    print(f"elapsed {time.time()-t0:.1f}s")
    assert_seal("post")
    print("done — exploration only; nothing frozen, no seed in RESERVED_002 touched.")


if __name__ == "__main__":
    main()
