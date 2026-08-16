"""Figure 2 — Theorem 3.1: absolute scale is invisible to the order.

The pedagogical point in one sentence: **in 1+1 Schwarzschild, changing the mass is
exactly changing the units**, and the order cannot read units.

The four panels carry the whole argument:

  A  a patch with horizon `r_s = 1`, on its own axes;
  B  its image under `Phi_s(t,r) = (st, sr)` with `r_s = 2`, on its own axes
     — same shape, different labels;
  C  the two patches on **common axes**: they are different objects, and an observer
     with coordinates tells them apart at a glance;
  D  the Hasse diagram: **just one**, because both induce literally the same labelled
     poset.

Honesty of the picture (it matters, and it belongs in the paper's caption)
-------------------------------------------------------------------------
The identity in panel D holds **by construction**: `Phi_s` is an order isomorphism,
so the same point set, transported, is a legitimate sprinkling of the other model
with the same relations.  What Theorem 3.1 adds is that this construction is
**generic**: since `Phi_s` carries the sprinkling law to the sprinkling law, the laws
of the unlabelled posets coincide and `TV = 0`.

What this figure does NOT say: that two *independent* sprinklings at different masses
come out equal.  They do not.  They come out with the **same distribution**, which is
precisely what stops any estimator from telling them apart.
"""

from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import numpy as np

from causet_core import (causal_matrix, check_dilation_identity, dilate,
                         hasse_edges, layer_of, sprinkle_exterior)
from style import BLUE, ORANGE, draw_cones, draw_hasse, draw_horizon, use_style

SEED = 20260806
N = 12
RS_A = 1.0
S = 2.0
T_RANGE = (0.0, 5.0)
R_RANGE = (1.15, 3.0)


def build():
    rng = np.random.default_rng(SEED)
    t_a, r_a = sprinkle_exterior(RS_A, T_RANGE, R_RANGE, N, rng)
    t_b, r_b, rs_b = dilate(t_a, r_a, RS_A, S)

    rel_a = causal_matrix(t_a, r_a, RS_A)
    rel_b = causal_matrix(t_b, r_b, rs_b)
    identical, discrepancies = check_dilation_identity(t_a, r_a, RS_A, S)
    if not identical:
        raise AssertionError(
            f"Phi_s did not preserve the order ({discrepancies} discrepancies): "
            "the figure would assert something false, so it is not drawn."
        )
    return (t_a, r_a, rel_a), (t_b, r_b, rs_b, rel_b), discrepancies


def draw(out):
    (t_a, r_a, rel_a), (t_b, r_b, rs_b, rel_b), discrepancies = build()

    use_style()
    fig, axes = plt.subplots(2, 2, figsize=(11.0, 8.6))
    axA, axB, axC, axD = axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1]

    # --- A: original model --------------------------------------------------
    axA.set_xlim(0.0, 3.4)
    axA.set_ylim(T_RANGE[0] - 0.3, T_RANGE[1] + 0.3)
    draw_horizon(axA, RS_A)
    draw_cones(axA, t_a[:5], r_a[:5], RS_A, scale=0.22)
    axA.scatter(r_a, t_a, s=46, c=BLUE, edgecolor="white", linewidth=1.0, zorder=4)
    axA.set_xlabel("$r$")
    axA.set_ylabel("$t$")
    axA.set_title(f"A · small mass:  $r_s = {RS_A:g}$", loc="left", pad=22)

    # --- B: dilated model ---------------------------------------------------
    axB.set_xlim(0.0, 3.4 * S)
    axB.set_ylim(T_RANGE[0] * S - 0.6, T_RANGE[1] * S + 0.6)
    draw_horizon(axB, rs_b)
    draw_cones(axB, t_b[:5], r_b[:5], rs_b, scale=0.22 * S)
    axB.scatter(r_b, t_b, s=46, c=ORANGE, edgecolor="white", linewidth=1.0, zorder=4)
    axB.set_xlabel("$r$")
    axB.set_ylabel("$t$")
    axB.set_title(f"B · double mass:  $r_s = {rs_b:g}$   (image under $\\Phi_s$, $s={S:g}$)",
                  loc="left", pad=22)
    axB.text(0.5, 1.0, "same picture as A: only the axis labels change",
             transform=axB.transAxes, ha="center", va="baseline", fontsize=9, color="#5A5A5A")

    # --- C: common axes -----------------------------------------------------
    axC.set_xlim(0.0, 3.4 * S)
    axC.set_ylim(T_RANGE[0] * S - 0.6, T_RANGE[1] * S + 0.6)
    axC.axvline(RS_A, color="#111111", lw=2.0, zorder=3)
    axC.axvline(rs_b, color="#111111", lw=2.0, zorder=3)
    axC.text(RS_A, T_RANGE[0] * S - 0.4, " $r_s=1$", ha="left", va="bottom",
             fontsize=9, color="#111111", rotation=90)
    axC.text(rs_b, T_RANGE[0] * S - 0.4, " $r_s=2$", ha="left", va="bottom",
             fontsize=9, color="#111111", rotation=90)
    axC.scatter(r_a, t_a, s=46, c=BLUE, edgecolor="white", linewidth=1.0,
                zorder=4, label=f"$r_s={RS_A:g}$")
    axC.scatter(r_b, t_b, s=46, c=ORANGE, edgecolor="white", linewidth=1.0,
                zorder=4, label=f"$r_s={rs_b:g}$")
    axC.legend(loc="upper left", fontsize=10)
    axC.set_xlabel("$r$")
    axC.set_ylabel("$t$")
    axC.set_title("C · on common axes they differ", loc="left", pad=22)
    axC.text(0.5, 1.0, "this is what an observer with coordinates can tell apart",
             transform=axC.transAxes, ha="center", va="bottom", fontsize=9, color="#5A5A5A")

    # --- D: the poset, just one ---------------------------------------------
    layer = layer_of(rel_a)
    draw_hasse(axD, rel_a, hasse_edges(rel_a), layer, node_color=BLUE,
               edgecolor=ORANGE, edgewidth=2.6, size=170)
    axD.set_title("D · the order both induce", loc="left", pad=22)
    axD.text(0.5, 1.0,
             "every node is at once a point of A (fill) and one of B (ring)",
             transform=axD.transAxes, ha="center", va="bottom", fontsize=9, color="#5A5A5A")
    axD.text(0.5, -0.04,
             f"identical element by element: {discrepancies} discrepancies "
             f"across {N}×{N} relations",
             transform=axD.transAxes, ha="center", va="top", fontsize=9.5, color="#5A5A5A")

    fig.suptitle(
        "In 1+1 Schwarzschild, changing the mass is changing the units — and the order cannot read units",
        fontsize=13.0, y=0.985)
    fig.text(0.5, 0.005,
             "Theorem 3.1:  $\\mathrm{TV}\\left(P_n(r_s;P),\\,P_n(s\\,r_s;\\Phi_s(P))\\right) = 0$ "
             "for every $n$ and every $s>0$.",
             ha="center", fontsize=11)
    fig.tight_layout(rect=(0, 0.022, 1, 0.965))
    fig.savefig(out)
    plt.close(fig)
    return out, discrepancies


if __name__ == "__main__":
    target = pathlib.Path(__file__).parent / "output" / "fig02_invisible_scale.png"
    target.parent.mkdir(exist_ok=True)
    path, d = draw(target)
    print(f"written {path}  (order discrepancies: {d})")
