"""dev exploration — region-shape control for CREATE route O4.

NOT sealed. DEV_SEEDS only. Reuses the rule from
dev/explore_create_o4_geodesic_selector.py unchanged (imported, not copied).
That test gave SURVIVES_CHEAP_TEST on the sealed box (commit 2fd5ca5), with BH
median |B|/N = 0.269 (1500) and 0.263 (3000) at eps = 0.1.

Suspected artefact: B = elements outside the past of the long-lived maximals. In a
FLAT region with a wide, low wing, wing points far from the tall part cannot reach
the high maximals, the wing maximals have small height and are excluded, so B is
non-empty without any horizon.

Regions (Minkowski causality from coordinates, same density as the sealed box,
rho = intensity / 7.2):
  MINK_WIDE    tall box [0,6]x[0.1,1.3]  U  wing [0,1]x[1.3, 1.3+8]
  MINK_NARROW  tall box                  U  wing [0,1]x[1.3, 1.3+2]
NARROW is the guardrail: every wing point reaches the top of the tall part
(r - 1.3 <= 2 <= 6 - t), so B must be empty there; if not, the mechanism is
not what is claimed.

PRE-DECLARED decision (eps = 0.1, medians over DEV_SEEDS, each intensity):
  ARTEFACT_CONFIRMED  if MINK_WIDE median |B|/N >= 0.5 * BH median |B|/N of the
                      previous run (0.269 / 0.263) at both intensities, and
                      MINK_NARROW median |B|/N == 0 at both.
  ARTEFACT_NOT_FOUND  if MINK_WIDE median |B|/N < 0.5 * BH at both and NARROW == 0.
  MECHANISM_UNCLEAR   otherwise (including NARROW != 0).
Rough prediction written beforehand: the WIDE B fraction is about 2.5 / 15.2,
roughly 0.16, which is above 0.13.

Run:  .venv/bin/python dev/explore_create_o4_wing_control.py
Writes dev/explore_create_o4_wing_control_results.json (refuses to overwrite).
"""

from __future__ import annotations

import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)

from nachocausal import generator, thresholds  # noqa: E402
from explore_create_o4_geodesic_selector import heights, select  # noqa: E402

EPS = 0.1
INTENSITIES = (1500.0, 3000.0)
BH_B_FRAC_PREVIOUS = {1500.0: 0.2691260686588961, 3000.0: 0.2630796300554663}
RATIO = 0.5
TALL = ((0.0, 6.0), (0.1, 1.3))
WING_T = 1.0
WINGS = {"MINK_WIDE": 8.0, "MINK_NARROW": 2.0}
OUT = os.path.join(HERE, "explore_create_o4_wing_control_results.json")


def sprinkle_rect(rng, rho, t_range, r_range):
    area = (t_range[1] - t_range[0]) * (r_range[1] - r_range[0])
    n = rng.poisson(rho * area)
    low = np.array([t_range[0], r_range[0]])
    span = np.array([t_range[1] - t_range[0], r_range[1] - r_range[0]])
    return low + rng.random((n, 2)) * span


def main() -> int:
    if os.path.exists(OUT):
        print(f"refusing to overwrite {OUT}", file=sys.stderr)
        return 1
    rows = []
    for intensity in INTENSITIES:
        rho = intensity / thresholds.BOX_AREA
        for seed in thresholds.DEV_SEEDS:
            for kind, width in WINGS.items():
                rng = np.random.default_rng(seed)
                pts = np.vstack([sprinkle_rect(rng, rho, *TALL),
                                 sprinkle_rect(rng, rho, (0.0, WING_T), (1.3, 1.3 + width))])
                C = generator.past_matrix_fast(pts, "MINK")
                h = heights(C)
                R, _, B, links = select(C, EPS, h)
                in_wing = pts[:, 1] > 1.3
                rows.append({"kind": kind, "intensity": intensity, "seed": seed, "N": int(len(pts)),
                             "n_R": int(R.sum()), "n_max": int((~C.any(axis=0)).sum()),
                             "B_frac": float(B.mean()), "n_interface": int(len(links)),
                             "B_in_wing_frac": (float(in_wing[B].mean()) if B.any() else None)})
            print(f"done intensity={intensity:.0f} seed={seed}", flush=True)

    med = {}
    for intensity in INTENSITIES:
        for kind in WINGS:
            sel = [x for x in rows if x["kind"] == kind and x["intensity"] == intensity]
            med[f"{kind}/{intensity:.0f}"] = {k: float(np.median([x[k] for x in sel]))
                                              for k in ("N", "n_R", "n_max", "B_frac", "n_interface")}
    wide_hit = all(med[f"MINK_WIDE/{i:.0f}"]["B_frac"] >= RATIO * BH_B_FRAC_PREVIOUS[i] for i in INTENSITIES)
    wide_miss = all(med[f"MINK_WIDE/{i:.0f}"]["B_frac"] < RATIO * BH_B_FRAC_PREVIOUS[i] for i in INTENSITIES)
    narrow_zero = all(med[f"MINK_NARROW/{i:.0f}"]["B_frac"] == 0.0 for i in INTENSITIES)
    if wide_hit and narrow_zero:
        verdict = "ARTEFACT_CONFIRMED"
    elif wide_miss and narrow_zero:
        verdict = "ARTEFACT_NOT_FOUND"
    else:
        verdict = "MECHANISM_UNCLEAR"
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                            cwd=HERE).stdout.strip()
    result = {"verdict": verdict, "repo_head": commit, "eps": EPS, "seeds": list(thresholds.DEV_SEEDS),
              "bh_b_frac_previous": {f"{k:.0f}": v for k, v in BH_B_FRAC_PREVIOUS.items()},
              "medians": med, "rows": rows}
    with open(OUT, "x") as f:
        json.dump(result, f, indent=1)
    print(json.dumps({"verdict": verdict, "medians": med}, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
