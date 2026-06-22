"""dev exploration — pin t_min, the minimum-extent validity boundary
(docs/estimator_v2_decision_spec.md, Decision 2). Design pre-flight, reversible.

Finding 4 jumped t_edge 3->6, leaving the in-domain boundary t_min in (3, 6]
unpinned. This fine-sweeps t_edge between and beyond, at MATCHED density, and
applies the frozen Decision-2 criterion per cell:

    in-domain  <=>  |bias| <= bracket half-width  AND  coverage >= 0.5,
                    confirmed flat (plateau) up to 2*t_edge.

where bias = mean(midpoint) - R_S and half-width = median(bracket width)/2, both
in r-units. t_min = the smallest t_edge that passes and stays passing (plateau).

Primary reference density rho = 833.3 (Finding 4's matched density); a second
pass at rho = 1666.7 (the prereg-001 primary endpoint density) checks whether
t_min is density-dependent. Matched density => intensity = rho * t_edge * R_EDGE.

EXPLORE_POOL only; sealed package / thresholds / seal SHA untouched; reserved
prereg-002 band never evaluated. Gate/observable/null + the across-seed metric
are imported verbatim from the earlier dev scripts, so this cannot drift.

Run:  python3 dev/explore_tmin.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import thresholds  # noqa: E402
from explore_seeds import EXPLORE_POOL  # noqa: E402
from explore_fp_gated import build_tau_table  # noqa: E402
from explore_axes import collect_bh  # noqa: E402  (collect_bh(intensity, t_edge), BH only, all 40)
from explore_stability import stability  # noqa: E402

R_EDGE = thresholds.R_EDGE       # 1.2
TWO_M = thresholds.TWO_M         # 0.5
R_S = thresholds.R_S             # 0.5

# rho -> t_edge values to sweep. Primary rho=833 spans (3,6] and the plateau;
# the high-rho check stays to {4,5,6} because its cells are expensive.
SWEEPS = [
    (833.3, [4, 5, 6, 8, 10]),
    (1666.7, [4, 5, 6]),
]


def run_rho(rho, t_edges):
    cells = [(te, round(rho * te * R_EDGE)) for te in t_edges]   # matched density
    allrows = {te: collect_bh(I, te) for te, I in cells}
    tau = build_tau_table([r[0] for te in allrows for r in allrows[te]])
    print(f"=== reference rho = {rho:.0f} pts/area  (intensity = rho * t_edge * "
          f"R_EDGE) ===", flush=True)
    print("  Decision-2: in-domain <=> |bias| <= half-width AND cov >= 0.5", flush=True)
    first_pass = None
    for te, I in cells:
        m = stability(allrows[te], tau)
        half_w = m["w_med"] * TWO_M / 2.0          # median full width (r) / 2
        bias = m["mid_bias"]
        ok = (abs(bias) <= half_w) and (m["cov"] >= 0.5)
        if ok and first_pass is None:
            first_pass = te
        print(f"  t_edge={te:<2} (I={I:<5})  cov={m['cov']:.2f}  "
              f"bias={bias:+.4f}  half_w={half_w:.4f}  "
              f"-> {'IN-DOMAIN' if ok else 'OUT'}", flush=True)
    print(f"  smallest in-domain t_edge in this sweep: {first_pass}  "
          f"(plateau = it stays in-domain for all larger t_edge above)\n", flush=True)


def run():
    print(f"t_min fine sweep  |  POOL={len(EXPLORE_POOL)} seeds "
          f"{EXPLORE_POOL[0]}..{EXPLORE_POOL[-1]}  |  R_S={R_S}\n", flush=True)
    for rho, t_edges in SWEEPS:
        run_rho(rho, t_edges)


if __name__ == "__main__":
    run()
