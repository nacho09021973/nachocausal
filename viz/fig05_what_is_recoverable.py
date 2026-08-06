"""Figure 5 — What the order DOES recover: position relative to the horizon.

This is the obligatory partner of Figure 2, and together they state the whole paper:

    Figure 2:  the order does NOT see  r_s        (absolute scale)
    Figure 5:  the order DOES see      r / r_s    (relative position)

The statistic is the simplest one there is: the **fraction of comparable pairs**.
Count how many pairs of elements are related and divide by the total.  No thresholds,
no fitting, no coordinates.

Panel A: the fraction drops sharply as the patch is moved towards the horizon — the
cones narrow, and the order notices.
Panel B: the same curve computed at `r_s = 1` and at `r_s = 7`, with **independent**
sprinklings, falls on top of itself.  Multiplying the mass by seven does not move the
curve at all: the statistic depends on `r/r_s` and on nothing else.  That is
Theorem 3.1 seen from the other side.
"""

from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import numpy as np

from causet_core import causal_matrix, comparable_fraction, sprinkle_exterior
from style import BLUE, GREY, ORANGE, use_style

SEED = 4242
N_POINTS = 60
REPEATS = 80
WIDTH = 1.0        # patch width, in units of r_s
DURATION = 3.0     # patch duration, in units of r_s
XS = np.array([1.05, 1.15, 1.3, 1.5, 1.8, 2.2, 2.8, 3.6, 5.0, 7.0, 9.0])


def sweep(rs, rng):
    """Mean and sd of the comparable fraction, patch shape FIXED in units of r_s."""
    means, sds = [], []
    for x in XS:
        vals = []
        for _ in range(REPEATS):
            t, r = sprinkle_exterior(
                rs, (0.0, DURATION * rs), (x * rs, (x + WIDTH) * rs), N_POINTS, rng)
            vals.append(comparable_fraction(causal_matrix(t, r, rs)))
        vals = np.asarray(vals)
        means.append(vals.mean())
        sds.append(vals.std())
    return np.asarray(means), np.asarray(sds)


def draw(out):
    rng = np.random.default_rng(SEED)
    m1, s1 = sweep(1.0, rng)
    m7, s7 = sweep(7.0, rng)          # INDEPENDENT sprinklings, not rescaled ones
    gap = float(np.max(np.abs(m1 - m7)))

    use_style()
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(12.0, 5.0))

    # --- A: the signal -------------------------------------------------------
    axA.fill_between(XS, m1 - s1, m1 + s1, color=BLUE, alpha=0.18)
    axA.plot(XS, m1, "o-", color=BLUE, lw=2.0, ms=6)
    axA.axvline(1.0, color="#111111", lw=2.0)
    axA.text(1.0, axA.get_ylim()[0], "  horizon", ha="left", va="bottom",
             fontsize=9, color="#111111", rotation=90)
    axA.set_xscale("log")
    axA.set_xticks([1, 2, 3, 5, 9])
    axA.set_xticklabels(["1", "2", "3", "5", "9"])
    axA.set_xlabel("patch position  $r/r_s$   (dimensionless)")
    axA.set_ylabel("fraction of comparable pairs")
    axA.set_title("A · the order notices the horizon", loc="left", pad=10)
    axA.annotate("near the horizon the cones narrow:\nfewer causal pairs",
                 xy=(1.15, m1[1]), xytext=(2.1, m1[0] + 0.02), fontsize=9.5, color=GREY,
                 ha="left", va="bottom",
                 arrowprops=dict(arrowstyle="->", color=GREY, lw=1.2,
                                 connectionstyle="arc3,rad=0.15"))

    # --- B: scale invariance -------------------------------------------------
    axB.errorbar(XS, m1, yerr=s1, fmt="o-", color=BLUE, lw=2.0, ms=6,
                 capsize=3, label="$r_s = 1$")
    axB.errorbar(XS, m7, yerr=s7, fmt="s--", color=ORANGE, lw=2.0, ms=6,
                 capsize=3, label="$r_s = 7$  (independent sprinklings)")
    axB.set_xscale("log")
    axB.set_xticks([1, 2, 3, 5, 9])
    axB.set_xticklabels(["1", "2", "3", "5", "9"])
    axB.set_xlabel("patch position  $r/r_s$")
    axB.set_ylabel("fraction of comparable pairs")
    axB.set_title("B · multiplying the mass by seven does not move the curve",
                  loc="left", pad=10)
    axB.legend(loc="lower right", fontsize=9.5)
    axB.text(0.03, 0.95,
             f"largest discrepancy: {gap:.3f}\n(typical sd ≈ {s1.mean():.3f})",
             transform=axB.transAxes, ha="left", va="top", fontsize=9.5, color=GREY)

    fig.suptitle("The order reads distance to the horizon in units of the horizon — never in metres",
                 fontsize=13.0, y=0.99)
    fig.text(0.5, 0.005,
             "Partner of Figure 2: there, $r_s$ was invisible; here, $r/r_s$ is not.",
             ha="center", fontsize=10.5)
    fig.tight_layout(rect=(0, 0.04, 1, 0.93))
    fig.savefig(out)
    plt.close(fig)
    return out, gap, float(s1.mean())


if __name__ == "__main__":
    target = pathlib.Path(__file__).parent / "output" / "fig05_what_is_recoverable.png"
    target.parent.mkdir(exist_ok=True)
    path, gap, sd = draw(target)
    print(f"written {path}")
    print(f"  largest gap between rs=1 and rs=7: {gap:.4f}  (typical sd {sd:.4f})")
