"""Figure 4 — Why the localisers died: the box wall eats the signal.

This is the honest figure of the failure ledger (`docs/comite/comite_decision_042`,
the C1–C5 line).  The most natural observable the order offers is the future volume
`|J^+(i)|`.  It looks as if it ought to grow near the horizon.  It does grow, a
little.  But the dominant effect is not physical: the simulation patch **ends**, and
an element near the ceiling has a small future for the simple reason that the ceiling
is there.

The number that sums it up: height in the box explains ~91 % of the variance of
`|J^+|`; radius explains ~3 %.  The physics is present, but buried under an artefact
of the apparatus.  Conditioning on a narrow time band brings it back — exactly the
kind of repair the C1–C5 ledger records as necessary and that none of those lines
ever closed.

Lesson for the student: in finite causal sets **the boundary of the box is an
observable**, and it competes with the physics you are trying to measure.
"""

from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import numpy as np

from causet_core import causal_matrix, future_volume, sprinkle_exterior
from style import BLUE, GREY, ORANGE, RED, use_style

SEED = 11
N = 900
RS = 1.0
T_RANGE = (0.0, 6.0)
R_RANGE = (1.1, 4.0)
BAND = (2.9, 3.1)


def _corr(a, b):
    return float(np.corrcoef(np.asarray(a, float), np.asarray(b, float))[0, 1])


def build():
    rng = np.random.default_rng(SEED)
    t, r = sprinkle_exterior(RS, T_RANGE, R_RANGE, N, rng)
    fv = future_volume(causal_matrix(t, r, RS))
    band = (t > BAND[0]) & (t < BAND[1])
    return t, r, fv, band


def draw(out):
    t, r, fv, band = build()
    c_t, c_r = _corr(fv, t), _corr(fv, r)
    c_r_band = _corr(fv[band], r[band])

    use_style()
    fig, (axA, axB, axC) = plt.subplots(1, 3, figsize=(14.0, 4.9))

    # --- A: the field --------------------------------------------------------
    sc = axA.scatter(r, t, c=fv, s=16, cmap="viridis", linewidth=0)
    axA.axhspan(BAND[0], BAND[1], color=RED, alpha=0.18, zorder=0)
    axA.text(R_RANGE[0], np.mean(BAND), " band", ha="left", va="bottom",
             fontsize=9, color=RED, weight="bold")
    axA.set_xlabel("$r$")
    axA.set_ylabel("$t$")
    axA.set_title("A · future volume $|J^+|$", loc="left", pad=22)
    fig.colorbar(sc, ax=axA, shrink=0.85, label="$|J^+(i)|$")
    axA.text(0.5, 1.0, "the gradient is VERTICAL, not radial",
             transform=axA.transAxes, ha="center", va="baseline",
             fontsize=9.5, color=GREY)

    # --- B: against height ---------------------------------------------------
    axB.scatter(t, fv, s=12, c=BLUE, alpha=0.5, linewidth=0)
    axB.set_xlabel("$t$  (height in the box)")
    axB.set_ylabel("$|J^+(i)|$")
    axB.set_title(f"B · artefact:  $\\rho = {c_t:+.3f}$", loc="left", pad=22)
    axB.text(0.5, 1.0, f"the box explains {100 * c_t ** 2:.0f} % of the variance",
             transform=axB.transAxes, ha="center", va="baseline",
             fontsize=9.5, color=RED)

    # --- C: against radius ---------------------------------------------------
    axC.scatter(r, fv, s=12, c=GREY, alpha=0.35, linewidth=0,
                label=f"whole patch ($\\rho={c_r:+.3f}$)")
    axC.scatter(r[band], fv[band], s=42, c=ORANGE, edgecolor="white",
                linewidth=0.6, zorder=3,
                label=f"band only ($\\rho={c_r_band:+.3f}$)")
    axC.set_xlabel("$r$  (radial position)")
    axC.set_ylabel("$|J^+(i)|$")
    axC.set_title("C · the physics, buried and recovered", loc="left", pad=22)
    axC.legend(loc="upper left", fontsize=9)

    fig.suptitle("The order's most natural observable mostly measures the edge of the patch",
                 fontsize=13.5, y=0.99)
    fig.text(0.5, 0.005,
             "This is the failure mode that killed the C1–C5 localisers: "
             "the box wall competes with the signal being sought.",
             ha="center", fontsize=10.5)
    fig.tight_layout(rect=(0, 0.04, 1, 0.92))
    fig.savefig(out)
    plt.close(fig)
    return out, c_t, c_r, c_r_band


if __name__ == "__main__":
    target = pathlib.Path(__file__).parent / "output" / "fig04_box_wall.png"
    target.parent.mkdir(exist_ok=True)
    path, a, b, c = draw(target)
    print(f"written {path}")
    print(f"  corr(|J+|, t) = {a:+.3f}   corr(|J+|, r) = {b:+.3f}   band corr = {c:+.3f}")
