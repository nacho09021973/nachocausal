"""Generate every figure and print the numbers that appear inside them.

Single reproducible entry point:

    python3 viz/make_figures.py

Each figure fixes its own seed, so two runs produce byte-identical files.  The
numbers printed here are the ones printed inside the panels: if any of them changes,
the figure and the manuscript caption have stopped agreeing.
"""

from __future__ import annotations

import pathlib
import sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))

import fig01_dictionary            # noqa: E402
import fig02_invisible_scale       # noqa: E402
import fig03_teleology             # noqa: E402
import fig04_box_wall              # noqa: E402
import fig05_what_is_recoverable   # noqa: E402

OUTPUT = HERE / "output"


def main():
    OUTPUT.mkdir(exist_ok=True)
    print("=" * 76)

    fig01_dictionary.draw(OUTPUT / "fig01_dictionary.png")
    print("fig01  dictionary: continuum <-> order")

    _, discrepancies = fig02_invisible_scale.draw(OUTPUT / "fig02_invisible_scale.png")
    print(f"fig02  invisible scale          order discrepancies = {discrepancies}"
          "   (must be 0)")

    fig03_teleology.draw(OUTPUT / "fig03_teleology.png")
    print("fig03  teleology                patch verified identical in both continuations")

    _, c_t, c_r, c_band, pop = fig04_box_wall.draw(OUTPUT / "fig04_box_wall.png")
    print(f"fig04  box wall sample          corr(|J+|,t) = {c_t:+.3f}   "
          f"corr(|J+|,r) = {c_r:+.3f}   band corr = {c_band:+.3f}")
    print(f"       population quadrature    corr(p(X),t(X)) = {pop['corr_p_t']:+.8f}   "
          f"tagged corr(F,T) = {pop['corr_k_t']:+.8f}")

    _, gap, sd = fig05_what_is_recoverable.draw(OUTPUT / "fig05_what_is_recoverable.png")
    print(f"fig05  what is recoverable      |rs=1 - rs=7| max = {gap:.4f}   "
          f"typical sd = {sd:.4f}   (the gap must stay below the sd)")

    print("=" * 76)
    print(f"figures in {OUTPUT}")


if __name__ == "__main__":
    main()
