"""Shared style for the pedagogical figures.

Colourblind-safe palette (Okabe–Ito) and large type: these figures are meant to be
projected in a lecture room, not squinted at in a PDF at 400 %.
"""

from __future__ import annotations

import matplotlib as mpl
import numpy as np

# Okabe–Ito
BLUE = "#0072B2"
ORANGE = "#E69F00"
GREEN = "#009E73"
RED = "#D55E00"
PURPLE = "#CC79A7"
SKY = "#56B4E9"
YELLOW = "#F0E442"
GREY = "#5A5A5A"

HORIZON = "#111111"
POINT = "#0072B2"


def use_style():
    mpl.rcParams.update({
        "figure.dpi": 130,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.18,
        "grid.linewidth": 0.6,
        "legend.frameon": False,
        "lines.dash_capstyle": "round",
    })


def draw_horizon(ax, rs, label=True):
    """Vertical horizon line `r = rs`, with the interior region shaded."""
    ax.axvline(rs, color=HORIZON, lw=2.0, zorder=3)
    lo, hi = ax.get_ylim()
    ax.fill_betweenx([lo, hi], 0, rs, color=HORIZON, alpha=0.07, zorder=0)
    ax.set_ylim(lo, hi)
    if label:
        ax.text(rs, hi, "  horizon  $r=r_s$", ha="left", va="top",
                fontsize=9, color=HORIZON, rotation=90)


def draw_cones(ax, t, r, rs, scale=0.35, color=GREY, alpha=0.55):
    """Light cones in `(t, r)`: null rays have `dt/dr = ±(1 - rs/r)^{-1}`.

    They narrow as the horizon is approached — which is *the* picture to see.
    """
    for ti, ri in zip(np.atleast_1d(t), np.atleast_1d(r)):
        slope = 1.0 / (1.0 - rs / ri)
        dr = scale
        dt = slope * dr
        # future cone
        ax.plot([ri, ri + dr], [ti, ti + dt], color=color, lw=1.1, alpha=alpha, zorder=2)
        ax.plot([ri, ri - dr], [ti, ti + dt], color=color, lw=1.1, alpha=alpha, zorder=2)


def order_layout(rel, layer, edges=None, sweeps=6):
    """Hasse positions derived **only from the order**, never from coordinates.

    `y` = height in the order (real content).  `x` = position within the layer, set
    first by a canonical rule and then refined by a barycentre heuristic to reduce
    edge crossings.  The `x` axis **carries no information**: it is legibility only,
    and reordering within a layer does not change the poset.
    """
    npred = rel.sum(axis=0)
    nsucc = rel.sum(axis=1)
    layers = {int(L): sorted(np.nonzero(layer == L)[0].tolist(),
                             key=lambda i: (int(npred[i]), -int(nsucc[i]), int(i)))
              for L in np.unique(layer)}

    if edges:
        up = {i: [] for i in range(rel.shape[0])}
        down = {i: [] for i in range(rel.shape[0])}
        for i, j in edges:
            up[i].append(j)
            down[j].append(i)

        def ranking(layer_nodes):
            return {node: k for k, node in enumerate(layer_nodes)}

        levels = sorted(layers)
        for sweep in range(sweeps):
            sequence = levels[1:] if sweep % 2 == 0 else levels[-2::-1]
            for L in sequence:
                reference = ranking(layers[L - 1]) if sweep % 2 == 0 else ranking(layers[L + 1])
                side = down if sweep % 2 == 0 else up

                def barycentre(node):
                    vs = [reference[v] for v in side[node] if v in reference]
                    return sum(vs) / len(vs) if vs else -1.0

                layers[L] = sorted(layers[L], key=lambda node: (barycentre(node), int(node)))

    pos = {}
    for L, idx in layers.items():
        k = len(idx)
        for j, i in enumerate(idx):
            x = 0.0 if k == 1 else (j - (k - 1) / 2.0) / max(k - 1, 1) * 2.0
            pos[i] = (x, float(L))
    return pos


def draw_hasse(ax, rel, edges, layer, pos=None, node_color=POINT,
               values=None, cmap="viridis", size=110, edgecolor="white", edgewidth=1.2):
    """Hasse diagram.  `values` colours the nodes by an order-theoretic scalar."""
    if pos is None:
        pos = order_layout(rel, layer, edges)
    for i, j in edges:
        x0, y0 = pos[i]
        x1, y1 = pos[j]
        ax.plot([x0, x1], [y0, y1], color=GREY, lw=0.9, alpha=0.55, zorder=1)
    xs = [pos[i][0] for i in range(rel.shape[0])]
    ys = [pos[i][1] for i in range(rel.shape[0])]
    if values is None:
        ax.scatter(xs, ys, s=size, c=node_color, edgecolor=edgecolor,
                   linewidth=edgewidth, zorder=3)
        sc = None
    else:
        sc = ax.scatter(xs, ys, s=size, c=values, cmap=cmap, edgecolor=edgecolor,
                        linewidth=edgewidth, zorder=3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_visible(False)
    return sc


def strip_axes(ax):
    """Remove ticks, grid and left/bottom spines — for pure order panels."""
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_visible(False)
