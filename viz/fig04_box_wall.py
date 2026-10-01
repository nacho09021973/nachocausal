"""Figure 4 — Why the localisers died: the box wall eats the signal.

This is the honest figure of the failure ledger (`docs/comite/comite_decision_042`,
the C1–C5 line).  The most natural observable the order offers is the future volume
`|J^+(i)|`.  It looks as if it ought to grow near the horizon.  It does grow, a
little.  But the dominant effect is not physical: the simulation patch **ends**, and
an element near the ceiling has a small future for the simple reason that the ceiling
is there.

The number that sums it up: a **linear** fit of `|J^+|` on height in the box has
`R^2 = rho^2 ~ 0.91`.  It is a linear summary of a visibly curved relation, and it is
conservative: a quadratic fit in `t` reaches `0.93`.  No variance decomposition is
claimed — `t` and `r` are drawn independently, but the non-linearity means the two
marginal `rho^2` do not add.  Radius on its own gives `rho^2 ~ 0.03`, and adding `r`
to the linear fit in `t` moves `R^2` from `0.905` to `0.912`.

The physics is present, but buried under an artefact of the apparatus.  Conditioning
on a narrow time band brings it back — exactly the kind of repair the C1–C5 ledger
records as necessary and that none of those lines ever closed.  That band is thin
(`n = 22` of `900`), and panel C now says so: its correlation carries a wide interval
and must not be read as precisely as the whole-patch number beside it (audit 035, W1).

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


def _fisher_ci(rho, n, z=1.96):
    """95 % interval for a correlation, from the sample size that produced it.

    Arithmetic on quantities already computed — no new sampling.  It exists because
    the band correlation comes from far fewer points than the whole-patch one, and
    the two are drawn side by side (audit 035, W1).
    """
    zeta = np.arctanh(rho)
    se = 1.0 / np.sqrt(n - 3)
    return float(np.tanh(zeta - z * se)), float(np.tanh(zeta + z * se))


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
    n_band = int(band.sum())
    ci_all = _fisher_ci(c_r, len(t))
    ci_band = _fisher_ci(c_r_band, n_band)

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
    axB.text(0.5, 1.0, f"linear $R^2 = \\rho^2 = {c_t ** 2:.2f}$ against the box height",
             transform=axB.transAxes, ha="center", va="baseline",
             fontsize=9.5, color=RED)

    # --- C: against radius ---------------------------------------------------
    axC.scatter(r, fv, s=12, c=GREY, alpha=0.35, linewidth=0,
                label=f"whole patch, $n={len(t)}$:  $\\rho={c_r:+.3f}$\n"
                      f"     95 % CI [{ci_all[0]:+.2f}, {ci_all[1]:+.2f}]")
    axC.scatter(r[band], fv[band], s=42, c=ORANGE, edgecolor="white",
                linewidth=0.6, zorder=3,
                label=f"band only, $n={n_band}$:  $\\rho={c_r_band:+.3f}$\n"
                      f"     95 % CI [{ci_band[0]:+.2f}, {ci_band[1]:+.2f}]")
    axC.set_xlabel("$r$  (radial position)")
    axC.set_ylabel("$|J^+(i)|$")
    axC.set_title("C · the physics, buried and barely recovered", loc="left", pad=22)
    axC.legend(loc="upper left", fontsize=8.2, labelspacing=0.9)

    fig.suptitle("The order's most natural observable mostly measures the edge of the patch",
                 fontsize=13.5, y=0.99)
    fig.text(0.5, 0.005,
             "This is the failure mode that killed the C1–C5 localisers: "
             "the box wall competes with the signal being sought.",
             ha="center", fontsize=10.5)
    fig.tight_layout(rect=(0, 0.04, 1, 0.92))
    fig.savefig(out)
    plt.close(fig)
    return out, c_t, c_r, c_r_band, n_band, ci_band


if __name__ == "__main__":
    target = pathlib.Path(__file__).parent / "output" / "fig04_box_wall.png"
    target.parent.mkdir(exist_ok=True)
    path, a, b, c, nb, ci = draw(target)
    print(f"written {path}")
    print(f"  corr(|J+|, t) = {a:+.3f}   corr(|J+|, r) = {b:+.3f}")
    print(f"  band corr = {c:+.3f}  (n = {nb}, 95 % CI [{ci[0]:+.3f}, {ci[1]:+.3f}])")
