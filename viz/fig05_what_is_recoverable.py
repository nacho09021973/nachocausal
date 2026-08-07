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
sprinklings, falls on top of itself.

What panel B is, and is not (audit 035, finding E1)
---------------------------------------------------
The two curves sample **the same law**, and that is a theorem, not a measurement.
`sweep` fixes the patch shape in units of `r_s`, so `Phi_s` carries one experiment
onto the other exactly: with a common RNG stream the two give the identical order and
the identical statistic.  Theorem 3.1 is what makes this an identity of laws.

So panel B **illustrates** an equality proved analytically.  It does not test it, and
it could not: agreement within Monte Carlo error is "we did not detect a difference",
never "the curves are equivalent".  Establishing equivalence empirically would need
an equivalence margin fixed in advance, which is analysis this figure does not do and
does not claim.

Accordingly the error bars are the **Monte Carlo standard error of the plotted mean**,
`sd/sqrt(REPEATS)`, and they are labelled as such.  The earlier version drew the
single-realisation `sd` — about nine times larger — unlabelled, and printed an
acceptance criterion ("the gap must stay below the sd") that no code enforced and that
was the wrong scale for the comparison.  Both are gone.
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

    # Monte Carlo error OF THE MEAN — the uncertainty of what is plotted — and, for
    # the difference of the two means, the scale on which any gap must be read.
    se1, se7 = s1 / np.sqrt(REPEATS), s7 / np.sqrt(REPEATS)
    se_diff = np.sqrt(se1 ** 2 + se7 ** 2)
    gap = float(np.max(np.abs(m1 - m7)))
    gap_in_se = float(np.max(np.abs(m1 - m7) / se_diff))

    use_style()
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(12.0, 5.0))

    # --- A: the signal -------------------------------------------------------
    axA.fill_between(XS, m1 - se1, m1 + se1, color=BLUE, alpha=0.25)
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
    axA.text(0.03, 0.97, f"band: $\\pm 1$ Monte Carlo SE of the mean\n"
                         f"({REPEATS} repeats; single-draw sd $\\approx$ {s1.mean():.3f})",
             transform=axA.transAxes, ha="left", va="top", fontsize=8.6, color=GREY)
    axA.annotate("near the horizon the cones narrow:\nfewer causal pairs",
                 xy=(1.15, m1[1]), xytext=(2.1, m1[0] + 0.02), fontsize=9.5, color=GREY,
                 ha="left", va="bottom",
                 arrowprops=dict(arrowstyle="->", color=GREY, lw=1.2,
                                 connectionstyle="arc3,rad=0.15"))

    # --- B: scale invariance -------------------------------------------------
    axB.errorbar(XS, m1, yerr=se1, fmt="o-", color=BLUE, lw=2.0, ms=6,
                 capsize=3, label="$r_s = 1$")
    axB.errorbar(XS, m7, yerr=se7, fmt="s--", color=ORANGE, lw=2.0, ms=6,
                 capsize=3, label="$r_s = 7$  (independent sprinklings)")
    axB.set_xscale("log")
    axB.set_xticks([1, 2, 3, 5, 9])
    axB.set_xticklabels(["1", "2", "3", "5", "9"])
    axB.set_xlabel("patch position  $r/r_s$")
    axB.set_ylabel("fraction of comparable pairs")
    axB.set_title("B · the two masses sample the same law (Theorem 3.1)",
                  loc="left", pad=10)
    axB.legend(loc="lower right", fontsize=9.5)
    axB.text(0.03, 0.97,
             "bars: $\\pm 1$ Monte Carlo SE of the mean\n"
             f"largest gap {gap:.4f} = {gap_in_se:.1f} SE of the difference",
             transform=axB.transAxes, ha="left", va="top", fontsize=8.8, color=GREY)

    fig.suptitle("The order reads distance to the horizon in units of the horizon — never in metres",
                 fontsize=13.0, y=0.99)
    fig.text(0.5, 0.005,
             "Partner of Figure 2: there, $r_s$ was invisible; here, $r/r_s$ is not.  "
             "Panel B illustrates an equality that is proved, not measured: the curves agree "
             "within Monte Carlo error,\nwhich is not the same as establishing equivalence.",
             ha="center", fontsize=10.0)
    fig.tight_layout(rect=(0, 0.065, 1, 0.93))
    fig.savefig(out)
    plt.close(fig)
    return out, gap, gap_in_se


if __name__ == "__main__":
    target = pathlib.Path(__file__).parent / "output" / "fig05_what_is_recoverable.png"
    target.parent.mkdir(exist_ok=True)
    path, gap, gap_in_se = draw(target)
    print(f"written {path}")
    print(f"  largest gap between rs=1 and rs=7: {gap:.4f} = {gap_in_se:.2f} "
          "Monte Carlo SE of the difference")
