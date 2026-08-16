"""Generate every figure and print the numbers that appear inside them.

Single reproducible entry point:

    python3 viz/make_figures.py

Each stochastic figure fixes its own seed, and the remaining figures use
deterministic quadrature.  The numerical values printed here are reproducible in
the pinned environment.  PNG bytes are not promised identical across machines:
font/FreeType rasterization can change pixels without changing the calculations.
"""

from __future__ import annotations

import pathlib
import sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))

import fig01_dictionary            # noqa: E402
import fig02_invisible_scale       # noqa: E402
import fig03_what_is_recoverable   # noqa: E402
import fig04_teleology             # noqa: E402
import fig05_minimax_rate          # noqa: E402
import fig06_box_wall              # noqa: E402

OUTPUT = HERE / "output"


def main():
    OUTPUT.mkdir(exist_ok=True)
    print("=" * 76)

    fig01_dictionary.draw(OUTPUT / "fig01_dictionary.png")
    print("fig01  dictionary: continuum <-> order")

    _, discrepancies = fig02_invisible_scale.draw(OUTPUT / "fig02_invisible_scale.png")
    print(f"fig02  invisible scale          order discrepancies = {discrepancies}"
          "   (must be 0)")

    _, gap, sd = fig03_what_is_recoverable.draw(OUTPUT / "fig03_what_is_recoverable.png")
    print(f"fig03  what is recoverable      |rs=1 - rs=7| max = {gap:.4f}   "
          f"typical sd = {sd:.4f}   (the gap must stay below the sd)")

    fig04_teleology.draw(OUTPUT / "fig04_teleology.png")
    print("fig04  teleology                patch verified identical in both continuations")

    fig05_minimax_rate.diagnostic_sweep()
    (
        _,
        p_values,
        fisher_values,
        fisher_mesh_max,
        fisher_argmax,
        cauchy_ratio_min,
        minimax_diagnostics,
    ) = fig05_minimax_rate.draw(OUTPUT / "fig05_minimax_rate.png")
    print(f"fig05  minimax-rate diagnostic  p endpoints = "
          f"({p_values[0]:.12f}, {p_values[-1]:.12f})")
    print(f"       direct-score mesh        I range = "
          f"[{fisher_values.min():.8e}, {fisher_values.max():.8e}]   "
          f"mesh max at tau={fisher_argmax:.3f}   value={fisher_mesh_max:.8e}")
    print(f"       Fisher inequality        min I/(2 p_prime^2) = {cauchy_ratio_min:.6f}")
    print(
        f"       small-lapse scaling      Richardson limit = "
        f"{minimax_diagnostics['richardson']:.8f}"
    )
    print(
        f"       diameter crossings       diagnostic = "
        f"{minimax_diagnostics['le_cam_crossing']:.6e}   "
        f"plug-in = {minimax_diagnostics['plugin_crossing']:.6e}"
    )

    _, c_t, c_r, c_band, pop = fig06_box_wall.draw(OUTPUT / "fig06_box_wall.png")
    print(f"fig06  box wall sample          corr(|J+|,t) = {c_t:+.3f}   "
          f"corr(|J+|,r) = {c_r:+.3f}   band corr = {c_band:+.3f}")
    print(f"       population quadrature    corr(upsilon(X),t(X)) = {pop['corr_p_t']:+.8f}   "
          f"tagged corr(F,Y) = {pop['corr_k_t']:+.8f}")

    print("=" * 76)
    print(f"figures in {OUTPUT}")


if __name__ == "__main__":
    main()
