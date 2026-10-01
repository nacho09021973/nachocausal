"""Figure 1 — The dictionary: from spacetime to order.

This is the figure the field is missing.  General relativity has the rubber sheet;
causal sets are drawn either as abstract Hasse diagrams or as points in Minkowski
with light cones on top, and neither shows **what gets thrown away** when you go
from one to the other.  Here you can see it: both panels have the same elements and
the same relations; the right one has lost the coordinates, and nothing else.

`order-only` = working with panel B alone, never being allowed to look at A.
"""

from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import numpy as np

from causet_core import (causal_matrix, hasse_edges, layer_of, sprinkle_exterior,
                         tortoise)
from style import (BLUE, GREEN, GREY, RED, draw_horizon, order_layout, strip_axes,
                   use_style)

SEED = 31415
N = 13
RS = 1.0
T_RANGE = (0.0, 5.0)
R_RANGE = (1.15, 3.2)


def build():
    rng = np.random.default_rng(SEED)
    t, r = sprinkle_exterior(RS, T_RANGE, R_RANGE, N, rng)
    rel = causal_matrix(t, r, RS)
    # witness: the element with the most balanced past and future, so that the
    # figure shows all three classes (past, future, incomparable) at once
    fut = rel.sum(axis=1)
    past = rel.sum(axis=0)
    p = int(np.argmax(np.minimum(fut, past)))
    return t, r, rel, p


def colours(rel, p, n):
    c = np.array([GREY] * n, dtype=object)
    c[rel[p]] = GREEN           # strict future of p
    c[rel[:, p]] = BLUE         # strict past of p
    c[p] = RED
    return c


def draw(out):
    t, r, rel, p = build()
    n = len(t)
    c = colours(rel, p, n)

    use_style()
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.6, 5.4))

    # --- A: the continuum ---------------------------------------------------
    axA.set_xlim(0.0, 3.5)
    axA.set_ylim(T_RANGE[0] - 0.35, T_RANGE[1] + 0.35)
    draw_horizon(axA, RS, label=False)
    axA.text(RS, T_RANGE[0] - 0.30, "  horizon $r=r_s$", ha="left", va="bottom",
             fontsize=9, color="#111111", rotation=90)
    # causal future of p, shaded: t >= t_p + |r*(r) - r*(p)|
    rr = np.linspace(R_RANGE[0] - 0.04, 3.5, 400)
    boundary = t[p] + np.abs(tortoise(rr, RS) - tortoise(r[p], RS))
    axA.fill_between(rr, boundary, T_RANGE[1] + 0.35, color=GREEN, alpha=0.10, zorder=0)
    axA.plot(rr, boundary, color=GREEN, lw=1.4, alpha=0.85, zorder=2)
    for i in range(n):
        axA.scatter(r[i], t[i], s=95, c=c[i], edgecolor="white", linewidth=1.2, zorder=4)
    axA.scatter([], [], s=95, c=RED, label="the element $p$")
    axA.scatter([], [], s=95, c=GREEN, label="its future $J^+(p)$")
    axA.scatter([], [], s=95, c=BLUE, label="its past $J^-(p)$")
    axA.scatter([], [], s=95, c=GREY, label="neither")
    axA.plot([], [], color=GREEN, lw=1.4, label="edge of $p$'s cone")
    axA.legend(loc="upper left", fontsize=9.0, handletextpad=0.3)
    axA.set_xlabel("$r$")
    axA.set_ylabel("$t$")
    axA.set_title("A · what an observer with coordinates sees", loc="left", pad=10)

    # --- B: the order -------------------------------------------------------
    layer = layer_of(rel)
    edges = hasse_edges(rel)
    pos = order_layout(rel, layer, edges)
    for i, j in edges:
        x0, y0 = pos[i]
        x1, y1 = pos[j]
        axB.plot([x0, x1], [y0, y1], color=GREY, lw=1.0, alpha=0.5, zorder=1)
    for i in range(n):
        axB.scatter(*pos[i], s=150, c=c[i], edgecolor="white", linewidth=1.4, zorder=3)
    strip_axes(axB)
    axB.set_title("B · what the order sees, and nothing more", loc="left", pad=10)
    axB.text(0.5, -0.02,
             "same elements, same relations, no coordinates",
             transform=axB.transAxes, ha="center", va="top", fontsize=10, color=GREY)

    fig.suptitle("What is lost in passing from spacetime to a causal set",
                 fontsize=13.5, y=0.98)
    fig.text(0.5, 0.005,
             "Vertical height in B is height in the order and carries all the content. "
             "Horizontal position carries none: it is chosen only to reduce crossings, "
             "and the crossings that remain mean nothing either.",
             ha="center", fontsize=9.5, color=GREY)
    fig.tight_layout(rect=(0, 0.03, 1, 0.94))
    fig.savefig(out)
    plt.close(fig)
    return out


if __name__ == "__main__":
    target = pathlib.Path(__file__).parent / "output" / "fig01_dictionary.png"
    target.parent.mkdir(exist_ok=True)
    print("written", draw(target))
