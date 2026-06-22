"""dev exploration — estimator-v2 SEED-stability axis (prerequisite #1 toward
prereg-002). Committee framing 2026-06-22.

The FP pre-flight (dev/explore_fp_gated.py) showed the VOLUME observable + the
data-independent tau(n) abstaining gate closes false-positives (iv) without
hurting BH coverage. That is necessary but NOT sufficient: before estimator-v2
can be integrated + re-sealed, its localisation must be shown STABLE, not just
on-average correct. This script isolates the SEED axis: at each FIXED intensity
it runs the full GATED pipeline over the whole EXPLORE_POOL (40 replicate seeds,
more than the FP test's 30) and reports the across-seed DISPERSION of:

  * abstention rate     -- how often the gate fires on BH (should be low/steady)
  * coverage            -- fraction of claiming seeds whose bracket covers R_S
  * boundary midpoint   -- mean, std, and |mean - R_S|: is the localised boundary
                           centred on the true horizon AND tight across seeds?
  * bracket width / 2M  -- median + std: localisation precision and its spread
  * sep (gated)         -- mean + std of the separation statistic

Stability claim passes the eye-test when, at fixed intensity, coverage is high,
the midpoint sits near R_S with SMALL std, and abstention is low and steady.
Density/patch/resolution axes are deliberately out of scope here (seed only,
per the 2026-06-22 decision); they are separate sweeps.

Nothing here is sealed. The gate, null, tau(n) MC, and observable are imported
verbatim from explore_fp_gated.py so this script cannot drift from the pre-flight.

Run:  python3 dev/explore_stability.py
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import generator, estimator, thresholds  # noqa: E402
from nachocausal.scoring import blind_bracket  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402
# Reuse the EXACT gate/observable/null from the FP pre-flight -- no reimplementation.
from explore_fp_gated import (  # noqa: E402
    improvement, minimal_volume, build_tau_table, INTENS, ALPHA, NULL_MC_SEED,
    NULL_MC_REPS,
)

POOL = EXPLORE_POOL          # all 40 replicate seeds (FP test used [:30])
R_S = thresholds.R_S
TWO_M = thresholds.TWO_M


def collect_bh(inten):
    """Per seed (BH only): (n, improvement, sep, bracket)."""
    rows = []
    for s in POOL:
        emb, _, _ = generator.numpy_sprinkle(s, inten)
        C = generator.past_matrix_fast(emb, "BH")
        Ob, mi = minimal_volume(C)
        vals = [Ob[i] for i in mi]
        n = len(mi)
        imp = improvement(vals)
        thr, sep = estimator.two_means_split(vals)
        br = blind_bracket(Ob, mi, thr, emb)
        rows.append((n, imp, sep, br))
    return rows


def stability(rows, tau):
    """Across-seed dispersion under the gate (abstain when imp < tau(n))."""
    abst = 0
    seps = []
    mids = []          # bracket midpoints of CLAIMING (non-abstained, valid) seeds
    widths = []        # width/2M of clean claiming seeds
    covers = []        # coverage among claiming seeds
    for (n, imp, sep, br) in rows:
        gated_out = imp < tau.get(n, np.inf)
        if gated_out:
            abst += 1
            seps.append(0.0)
            continue
        seps.append(sep)
        if br is not None and br["valid"]:
            covers.append(br["covers"])
            mids.append(br["midpoint"])
            if br["clean"]:
                widths.append(br["width"] / TWO_M)
    seps = np.array(seps, float)
    mids = np.array(mids, float)
    widths = np.array(widths, float)
    return dict(
        n_seeds=len(rows),
        abst=abst, abst_rate=abst / len(rows),
        n_claim=len(mids),
        cov=float(np.mean(covers)) if covers else float("nan"),
        mid_mean=float(np.mean(mids)) if mids.size else float("nan"),
        mid_std=float(np.std(mids)) if mids.size else float("nan"),
        mid_bias=float(np.mean(mids) - R_S) if mids.size else float("nan"),
        w_med=float(np.median(widths)) if widths.size else float("nan"),
        w_std=float(np.std(widths)) if widths.size else float("nan"),
        sep_mean=float(np.mean(seps)), sep_std=float(np.std(seps)),
    )


def run():
    print(f"SEED-stability axis  |  POOL={len(POOL)} seeds "
          f"{POOL[0]}..{POOL[-1]}  |  R_S={R_S}  2M={TWO_M}")
    print(f"gate: tau(n)=p{int((1-ALPHA)*100)} uniform null, "
          f"MC seed={NULL_MC_SEED} reps={NULL_MC_REPS}\n")
    all_rows = {inten: collect_bh(inten) for inten in INTENS}
    all_n = [r[0] for inten in INTENS for r in all_rows[inten]]
    tau = build_tau_table(all_n)
    for inten in INTENS:
        rows = all_rows[inten]
        ns = [r[0] for r in rows]
        m = stability(rows, tau)
        print(f"--- intensity {inten:.0f} ---  n in [{min(ns)},{max(ns)}]  "
              f"(fixed intensity; varying seed)")
        print(f"  abstention : {m['abst']}/{m['n_seeds']} "
              f"({m['abst_rate']:.2f})   claiming seeds: {m['n_claim']}")
        print(f"  coverage   : {m['cov']:.2f}  (fraction of claiming seeds "
              f"whose bracket covers R_S)")
        print(f"  midpoint   : mean={m['mid_mean']:.4f}  std={m['mid_std']:.4f}  "
              f"bias(mean-R_S)={m['mid_bias']:+.4f}")
        print(f"  width/2M   : median={m['w_med']:.3f}  std={m['w_std']:.3f}")
        print(f"  sep(gated) : mean={m['sep_mean']:.2f}  std={m['sep_std']:.2f}")
        print()


if __name__ == "__main__":
    run()
