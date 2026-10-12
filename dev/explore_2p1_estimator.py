"""2+1 phase B: estimator-v2 ported to the 2+1 equatorial EF box (dev exploration; NO verdict).

Order-only estimator, logic of the sealed 1+1D estimator-v2 (docs/estimator_v2_freeze.md):
  O(i) = |future(i)| over the minimal elements; 1-D 2-means split (improvement imported
  unchanged from nachocausal/estimator.py); gate: abstain iff improvement < tau(n), tau(n) the
  p99 of improvement under a Uniform[0,1] null at matched n (same MC procedure; n > 128 is
  computed here in dev with the same seed rule, since the sealed table stops at 128).
Scoring ONLY (ground truth revealed after the estimate): bracket [max r over low-O, min r over
high-O] of the minimal elements, its midpoint, width, coverage of 2M = 0.5.  The flat 2+1
control (same cloud) measures false positives.
Seeds: the 2+1 exploration band 7_000_000..7_000_999 only.
Usage: .venv/bin/python dev/explore_2p1_estimator.py N seed [seed ...]
"""
import json
import sys
from functools import lru_cache
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "dev"))
import gen2p1_efbox as gen  # noqa: E402
from nachocausal import estimator, thresholds  # noqa: E402
from nachocausal import gate as sealed_gate  # noqa: E402


@lru_cache(maxsize=None)
def tau(n):
    if n <= thresholds.GATE_TAU_N_MAX:
        return sealed_gate.tau(n)
    # same procedure as scripts/gen_tau_table.py, one rng per n beyond the sealed table (dev)
    rng = np.random.default_rng([thresholds.GATE_NULL_MC_SEED, n])
    vals = np.fromiter((estimator.improvement(rng.random(n)) for _ in range(4000)), float, 4000)
    return float(np.quantile(vals, 1.0 - thresholds.GATE_ALPHA))


def estimate(order):
    """ORDER ONLY: order[i, j] = i precedes j.  Returns minimal ids, O, threshold, gate."""
    minimal = np.nonzero(~order.any(axis=0))[0]
    O = order[minimal].sum(axis=1)
    n = minimal.size
    imp = estimator.improvement(O.astype(float)) if n >= 2 else 0.0
    thr, sep = estimator.two_means_split(O)
    abstain = (n < 2) or imp < tau(n)
    return {"minimal": minimal, "O": O, "thr": thr, "sep": sep, "improvement": imp,
            "tau": tau(n) if n >= 2 else None, "abstain": bool(abstain)}


def score(est, r):
    """GROUND TRUTH: only here.  Bracket of the minimal elements' r around the 2-means split."""
    rm = r[est["minimal"]]
    low = est["O"] < est["thr"]
    if est["abstain"] or low.all() or (~low).all():
        return {"claimed": False}
    r_lo, r_hi = float(rm[low].max()), float(rm[~low].min())
    return {"claimed": True, "r_lo": r_lo, "r_hi": r_hi, "mid": 0.5 * (r_lo + r_hi),
            "width_over_2M": (r_hi - r_lo) / gen.TWO_M, "covers_2M": bool(r_lo <= gen.TWO_M <= r_hi),
            "low_O_all_inside": bool((rm[low] < gen.TWO_M).all()),
            "high_O_all_outside": bool((rm[~low] > gen.TWO_M).all())}


def run(n_mean, seed):
    assert gen.EXPLORE_BAND[0] <= seed <= gen.EXPLORE_BAND[1]
    rng = np.random.default_rng(seed)
    t, r, phi = gen.sprinkle(n_mean, rng)
    bh, st = gen.bh_order(t, r, phi, rng=None)
    mk = gen.mink_order(t, r, phi)
    out = {"seed": seed, "n": int(t.size), "gen_seconds": st["seconds_total"]}
    for name, order in (("BH", bh), ("MINK", mk)):
        e = estimate(order)
        out[name] = {"n_minimal": int(e["minimal"].size), "improvement": round(e["improvement"], 4),
                     "tau": None if e["tau"] is None else round(e["tau"], 4),
                     "abstain": e["abstain"], "sep": round(e["sep"], 3),
                     "O_quartiles": np.quantile(e["O"], [0, .25, .5, .75, 1]).astype(int).tolist(),
                     **score(e, r)}
    return out


def main():
    n_mean = int(sys.argv[1])
    for seed in [int(s) for s in sys.argv[2:]]:
        print(json.dumps(run(n_mean, seed)), flush=True)


if __name__ == "__main__":
    main()
