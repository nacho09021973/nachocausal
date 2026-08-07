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

    _, c_t, c_r, c_band, n_band, ci_band = fig04_box_wall.draw(OUTPUT / "fig04_box_wall.png")
    print(f"fig04  box wall                 corr(|J+|,t) = {c_t:+.3f}   "
          f"corr(|J+|,r) = {c_r:+.3f}")
    print(f"       band corr = {c_band:+.3f}  (n = {n_band}, "
          f"95 % CI [{ci_band[0]:+.3f}, {ci_band[1]:+.3f}])")

    _, gap, gap_in_se = fig05_what_is_recoverable.draw(OUTPUT / "fig05_what_is_recoverable.png")
    print(f"fig05  what is recoverable      |rs=1 - rs=7| max = {gap:.4f} = "
          f"{gap_in_se:.2f} Monte Carlo SE of the difference")
    print("       (a diagnostic, NOT an acceptance criterion: the equality is proved,")
    print("        and agreement within MC error would never establish equivalence)")

    print("=" * 76)
    print(f"figures in {OUTPUT}")


if __name__ == "__main__":
    main()
