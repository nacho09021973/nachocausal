"""Figure 4 — A finite order-theoretic analogy for Theorem 3.2.

An element `e` is maximal in the observed patch.  Is it *really* maximal, or is there
something above it that we simply have not seen?  **The patch does not know and
cannot know.**  This is a toy analogy for the completion dependence in Theorem 3.2,
not a literal representation of an event horizon.

Within the plotted model the construction is exact: both added elements are
legitimate sprinkled points in a later time band.  One
falls in the causal future of `e`, the other is spacelike to `e`.  The induced
subposet on the patch is **identical** in both cases, and the script verifies this
before drawing.

Corresponding formal core: `dev/PR003_INFINITE_MAXIMALITY_NONCERTIFIABILITY.md`
(`VERDICT = PROVED`), of which this figure is the finite, drawable shadow.
"""

from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import numpy as np

from causet_core import causal_matrix, hasse_edges, layer_of, sprinkle_exterior
from style import BLUE, GREEN, GREY, PURPLE, RED, order_layout, strip_axes, use_style

SEED = 2718
N = 9
RS = 1.0
T_RANGE = (0.0, 3.2)
R_RANGE = (1.2, 3.0)
EXTRA_BAND = (3.2, 5.2)


def _maximals(rel):
    return np.nonzero(~rel.any(axis=1))[0]


def build():
    """Return the patch, the witness `e`, and the two continuations."""
    rng = np.random.default_rng(SEED)
    t, r = sprinkle_exterior(RS, T_RANGE, R_RANGE, N, rng)
    rel = causal_matrix(t, r, RS)

    maxs = _maximals(rel)
    # witness: the maximal element with the largest past, so it sits well placed
    e = int(maxs[np.argmax(rel[:, maxs].sum(axis=0))])

    # look, in the later band, for one point IN the future of e and one spacelike
    above = beside = None
    for _ in range(4000):
        tq, rq = sprinkle_exterior(RS, EXTRA_BAND, R_RANGE, 1, rng)
        t_ext = np.append(t, tq)
        r_ext = np.append(r, rq)
        rel_ext = causal_matrix(t_ext, r_ext, RS)
        if rel_ext[e, N] and above is None:
            above = (float(tq[0]), float(rq[0]), rel_ext)
        if (not rel_ext[e, N]) and beside is None:
            beside = (float(tq[0]), float(rq[0]), rel_ext)
        if above and beside:
            break
    if not (above and beside):
        raise RuntimeError("could not find both continuations")

    # hard check: the induced patch must be identical in both
    for name, (_, _, rel_ext) in (("A", above), ("B", beside)):
        if not np.array_equal(rel_ext[:N, :N], rel):
            raise AssertionError(f"continuation {name} altered the observed patch")

    return t, r, rel, e, above, beside


def _panel(ax, rel_ext, n_patch, e, title, new_is_future, base_pos=None):
    layer = layer_of(rel_ext)
    edges = hasse_edges(rel_ext)
    pos = order_layout(rel_ext, layer, edges)
    if base_pos is not None:
        for i in range(n_patch):
            pos[i] = base_pos[i]
    for i, j in edges:
        x0, y0 = pos[i]
        x1, y1 = pos[j]
        new = (i >= n_patch) or (j >= n_patch)
        ax.plot([x0, x1], [y0, y1], color=PURPLE if new else GREY,
                lw=1.8 if new else 1.0, alpha=0.9 if new else 0.5,
                zorder=2 if new else 1)
    for i in range(rel_ext.shape[0]):
        if i >= n_patch:
            col, size = PURPLE, 210
        elif i == e:
            col, size = RED, 190
        else:
            col, size = BLUE, 130
        ax.scatter(*pos[i], s=size, c=col, edgecolor="white", linewidth=1.4, zorder=3)
    strip_axes(ax)
    ax.set_title(title, loc="left", pad=10)
    verdict = "$e$ is NOT maximal" if new_is_future else "$e$ IS maximal"
    ax.text(0.5, -0.02, verdict, transform=ax.transAxes, ha="center", va="top",
            fontsize=12, color=RED if new_is_future else GREEN, weight="bold")
    return pos


def draw(out):
    t, r, rel, e, above, beside = build()

    use_style()
    fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(13.0, 5.2))

    layer = layer_of(rel)
    edges = hasse_edges(rel)
    pos0 = order_layout(rel, layer, edges)
    for i, j in edges:
        x0, y0 = pos0[i]
        x1, y1 = pos0[j]
        ax0.plot([x0, x1], [y0, y1], color=GREY, lw=1.0, alpha=0.5, zorder=1)
    for i in range(len(t)):
        col = RED if i == e else BLUE
        ax0.scatter(*pos0[i], s=190 if i == e else 130, c=col,
                    edgecolor="white", linewidth=1.4, zorder=3)
    strip_axes(ax0)
    ax0.set_title("what we observe: the patch", loc="left", pad=10)
    ax0.text(0.5, -0.02, "$e$ is maximal IN HERE", transform=ax0.transAxes,
             ha="center", va="top", fontsize=12, color=GREY, weight="bold")

    _panel(ax1, above[2], len(t), e, "continuation 1 (legitimate)",
           new_is_future=True, base_pos=pos0)
    _panel(ax2, beside[2], len(t), e, "continuation 2 (just as legitimate)",
           new_is_future=False, base_pos=pos0)

    all_axes = [ax0, ax1, ax2]
    lo_y = min(ax.get_ylim()[0] for ax in all_axes)
    hi_y = max(ax.get_ylim()[1] for ax in all_axes)
    lo_x = min(ax.get_xlim()[0] for ax in all_axes)
    hi_x = max(ax.get_xlim()[1] for ax in all_axes)
    for ax in all_axes:
        ax.set_ylim(lo_y, hi_y)
        ax.set_xlim(lo_x, hi_x)

    fig.suptitle("The same patch admits futures that contradict each other",
                 fontsize=13.5, y=0.98)
    fig.text(0.5, 0.045,
             "The blue subposet is identical in all three panels — verified element by element. "
             "Only the purple point changes, and it lies outside what was observed.",
             ha="center", fontsize=10, color=GREY)
    fig.text(0.5, 0.005,
             "Toy analogy for Theorem 3.2: identical patch data do not determine a "
             "global property of the completion.",
             ha="center", fontsize=11)
    fig.tight_layout(rect=(0, 0.075, 1, 0.94))
    fig.savefig(out)
    plt.close(fig)
    return out


if __name__ == "__main__":
    target = pathlib.Path(__file__).parent / "output" / "fig04_teleology.png"
    target.parent.mkdir(exist_ok=True)
    print("written", draw(target))
