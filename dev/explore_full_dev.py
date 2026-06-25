"""dev exploration — joint check of an observable swap on BOTH failing axes.

NOT sealed (dev/). DEV_SEEDS only; thresholds & sealed estimator untouched.
Runs the FULL frozen validate pipeline on DEV_SEEDS with the order-only
observable swapped from future-HEIGHT (sealed) to future-VOLUME, by monkey-
patching estimator.estimate_O with a dev variant that returns |future(i)| for
each minimal element. Everything downstream (two_means_split, blind_bracket,
sep, p_perm, LOO false-positive) is the unmodified sealed code, so this is an
apples-to-apples read on whether volume fixes (ii) coverage AND (iv) FP at once
WITHOUT regressing significance.

Verdicts are DISCARDED (write=False); this is exploration, not a committing run.
A real claim would need a new pre-registration 002 with fresh held-out seeds.

Run:  .venv/bin/python dev/explore_full_dev.py
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import estimator, thresholds, validate  # noqa: E402

_orig_estimate_O = estimator.estimate_O


def estimate_O_volume(past_matrix):
    """Order-only observable = future VOLUME |J+(i)| (column sum of C) for each
    minimal element. Permutation-invariant -> trivially order-only (Guard-v safe).
    Returns the same 3-tuple shape as the sealed estimate_O."""
    C = past_matrix if past_matrix.dtype == bool else past_matrix.astype(bool)
    vol = C.sum(axis=0).astype(int)          # |future(i)| for every element
    has_past = C.any(axis=1)
    minimal = [i for i in range(C.shape[0]) if not has_past[i]]
    O_by_min = {i: int(vol[i]) for i in minimal}
    return O_by_min, minimal, vol


def _summary(label, verdict):
    print(f"\n===== {label}  ->  verdict={verdict['verdict']} =====")
    print(f"{'inten':>7}{'p_perm':>11}{'sig':>5}{'cov':>6}{'medW/2M':>9}{'fp':>6}{'fp_ok':>7}{'loc_ok':>7}")
    for lam, l in verdict["levels"].items():
        print(f"{l['intensity']:>7.0f}{l.get('p_perm', float('nan')):>11.2e}"
              f"{str(l.get('significant')):>5}{l.get('coverage_frac', float('nan')):>6.2f}"
              f"{l.get('median_width_over_2M', float('nan')):>9.3f}"
              f"{l.get('fp_fraction', float('nan')):>6.2f}{str(l.get('fp_pass')):>7}"
              f"{str(l.get('loc_pass') and not l.get('loc_inconclusive')):>7}")
    c = verdict.get("checks", {})
    print("checks:", {k: c[k] for k in c})


def run():
    seeds = list(thresholds.DEV_SEEDS)
    print(f"DEV_SEEDS={seeds}  (guard=False for speed; order-only re-checked below)")

    # order-only sanity for the volume observable (Guard-v style): invariance
    # under a pure relabelling.
    rng = np.random.default_rng(0)
    from nachocausal import generator
    emb, _, _ = generator.numpy_sprinkle(seeds[0], 1500.0)
    C = generator.past_matrix_fast(emb, "BH")
    o0 = sorted(estimate_O_volume(C)[0].values())
    p = rng.permutation(C.shape[0])
    o1 = sorted(estimate_O_volume(C[p][:, p])[0].values())
    print(f"volume order-only under relabel: {'OK' if o0 == o1 else 'VIOLATED'}")

    # MIN_VALID_SEEDS=18 is the 20-seed validation floor; for the 8 dev seeds use
    # the SAME dev-sized floor as dry_run.py (restored in finally). No frozen
    # threshold VALUE is changed for any real purpose; this only runs the path.
    saved_floor = thresholds.MIN_VALID_SEEDS
    thresholds.MIN_VALID_SEEDS = max(3, len(seeds) - 2)
    try:
        # baseline (sealed height)
        estimator.estimate_O = _orig_estimate_O
        base = validate.run(seeds=seeds, label="dev_height", guard=False, write=False)
        _summary("HEIGHT (sealed baseline)", base)

        # swap -> volume
        estimator.estimate_O = estimate_O_volume
        vol = validate.run(seeds=seeds, label="dev_volume", guard=False, write=False)
        _summary("VOLUME (dev candidate)", vol)
    finally:
        estimator.estimate_O = _orig_estimate_O
        thresholds.MIN_VALID_SEEDS = saved_floor


if __name__ == "__main__":
    run()
