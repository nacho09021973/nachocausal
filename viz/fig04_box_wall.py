"""Figure 4 — Why the localisers died: the box wall eats the signal.

This is the honest figure of the failure ledger (`docs/comite/comite_decision_042`,
the C1–C5 line).  The most natural observable the order offers is the future volume
`|J^+(i)|`.  It can display a radial trend in the chosen bank.  But the dominant
effect in this diagnostic is the simulation patch **ending**, and
an element near the ceiling has a small future for the simple reason that the ceiling
is there.

The descriptive numbers that sum it up are a sample `R^2` of ~91 % against height
and ~3 % against radius.  Conditioning on a narrow time band exposes a
residual radial correlation.  That residual is a diagnostic feature of this
fixed-seed illustration, not a recovered horizon signal or a sealed validation
result.  It is exactly the kind of conditioning the C1–C5 ledger records as
necessary and that none of those lines ever closed.

Lesson for the student: in finite causal sets **the boundary of the box is an
observable**, and it competes with the physics you are trying to measure.

Panel B distinguishes three objects.  Its plotted coefficient is the Pearson
coefficient inside one fixed-seed causet.  The window target `Corr(p(X), t(X))` and
the finite-`n` correlation for a tagged element are computed separately by
deterministic Gauss--Legendre quadrature; no additional sprinkling or seed is used.
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
QUAD_T = 200
QUAD_R = 200
QUAD_FUTURE_R = 360


def _corr(a, b):
    return float(np.corrcoef(np.asarray(a, float), np.asarray(b, float))[0, 1])


def _gauss_interval(size, lo, hi):
    """Gauss--Legendre nodes and weights mapped to `[lo, hi]`."""
    nodes, weights = np.polynomial.legendre.leggauss(size)
    return (hi - lo) * (nodes + 1.0) / 2.0 + lo, weights * (hi - lo) / 2.0


def population_diagnostics(n_points=N):
    """Return the window/chart target and exact tagged-element attenuation.

    For `X=(t,r)` uniform on the declared rectangle, define

        p(X) = Vol(J^+(X) intersect W) / Vol(W).

    At fixed `r_prime`, the allowed future-time length is

        [t_max - t - |r_star(r_prime)-r_star(r)|]_+.

    The resulting one-dimensional integral gives `p(t,r)`.  Tensor-product
    Gauss--Legendre quadrature then evaluates its moments over `X`.  This is a
    deterministic quadrature of the continuum window, not a sprinkling estimate.
    """
    if n_points < 2:
        raise ValueError("tagged-element attenuation requires n_points >= 2")

    t, wt = _gauss_interval(QUAD_T, *T_RANGE)
    r, wr = _gauss_interval(QUAD_R, *R_RANGE)
    r_future, w_future = _gauss_interval(QUAD_FUTURE_R, *R_RANGE)

    def r_star(values):
        values = np.asarray(values, dtype=float)
        return values + RS * np.log(values / RS - 1.0)

    delta_r_star = np.abs(r_star(r)[:, None] - r_star(r_future)[None, :])
    area = (T_RANGE[1] - T_RANGE[0]) * (R_RANGE[1] - R_RANGE[0])
    p = np.asarray([
        (np.maximum(T_RANGE[1] - t_i - delta_r_star, 0.0) * w_future)
        .sum(axis=1) / area
        for t_i in t
    ])
    weights = wt[:, None] * wr[None, :] / area

    mean_p = float(np.sum(weights * p))
    var_p = float(np.sum(weights * p * p) - mean_p ** 2)
    binomial_noise = float(np.sum(weights * p * (1.0 - p)))
    mean_t = float(np.sum(weights * t[:, None]))
    var_t = float(np.sum(weights * (t[:, None] - mean_t) ** 2))
    cov_p_t = float(np.sum(weights * (p - mean_p) * (t[:, None] - mean_t)))
    corr_p_t = cov_p_t / np.sqrt(var_p * var_t)

    attenuation = float(
        (1.0 + binomial_noise / ((n_points - 1) * var_p)) ** -0.5
    )
    return {
        "mean_p": mean_p,
        "var_p": var_p,
        "binomial_noise": binomial_noise,
        "corr_p_t": float(corr_p_t),
        "attenuation": attenuation,
        "corr_k_p": attenuation,
        "corr_k_t": float(corr_p_t * attenuation),
    }


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
    pop = population_diagnostics(N)

    use_style()
    fig, (axA, axB, axC) = plt.subplots(1, 3, figsize=(14.0, 4.9))

    # --- A: the field --------------------------------------------------------
    sc = axA.scatter(r, t, c=fv, s=16, cmap="viridis", linewidth=0)
    axA.axhspan(BAND[0], BAND[1], color=RED, alpha=0.18, zorder=0)
    axA.text(R_RANGE[0], np.mean(BAND), " band", ha="left", va="bottom",
             fontsize=9, color=RED, weight="bold")
    axA.set_xlabel("$r$")
    axA.set_ylabel("$t$")
    axA.set_title("A · future cardinality $F=|J^+|$", loc="left", pad=22)
    fig.colorbar(sc, ax=axA, shrink=0.85, label="$F_i=|J^+(i)|$")
    axA.text(0.5, 1.0, "the gradient is VERTICAL, not radial",
             transform=axA.transAxes, ha="center", va="baseline",
             fontsize=9.5, color=GREY)

    # --- B: against height ---------------------------------------------------
    axB.scatter(t, fv, s=12, c=BLUE, alpha=0.5, linewidth=0)
    axB.set_xlabel("$t$  (height in the box)")
    axB.set_ylabel("$F_i=|J^+(i)|$")
    axB.set_title(f"B · one causet:  $\\hat{{\\rho}}_{{\\rm cloud}} = {c_t:+.3f}$",
                  loc="left", pad=22)
    axB.text(0.5, 1.0,
             f"window target $\\rho_\\infty={pop['corr_p_t']:+.6f}$"
             f"  ·  tagged $\\rho_{{{N}}}={pop['corr_k_t']:+.6f}$",
             transform=axB.transAxes, ha="center", va="baseline",
             fontsize=8.9, color=RED)

    # --- C: against radius ---------------------------------------------------
    axC.scatter(r, fv, s=12, c=GREY, alpha=0.35, linewidth=0,
                label=f"whole patch (sample $\\hat{{\\rho}}={c_r:+.3f}$)")
    axC.scatter(r[band], fv[band], s=42, c=ORANGE, edgecolor="white",
                linewidth=0.6, zorder=3,
                label=f"band only (sample $\\hat{{\\rho}}={c_r_band:+.3f}$)")
    axC.set_xlabel("$r$  (radial position)")
    axC.set_ylabel("$F_i=|J^+(i)|$")
    axC.set_title("C · a residual radial trend after banding", loc="left", pad=22)
    axC.legend(loc="upper left", fontsize=9)

    fig.suptitle("Future cardinality in a finite Schwarzschild window",
                 fontsize=13.5, y=0.99)
    fig.text(0.5, 0.005,
             "Sample coefficients: one fixed-seed causet.  Population targets in B: "
             "deterministic quadrature.  Neither establishes horizon recovery.",
             ha="center", fontsize=10.5)
    fig.tight_layout(rect=(0, 0.04, 1, 0.92))
    fig.savefig(out)
    plt.close(fig)
    return out, c_t, c_r, c_r_band, pop


if __name__ == "__main__":
    target = pathlib.Path(__file__).parent / "output" / "fig04_box_wall.png"
    target.parent.mkdir(exist_ok=True)
    path, a, b, c, pop = draw(target)
    print(f"written {path}")
    print(f"  sample corr(|J+|, t) = {a:+.3f}   corr(|J+|, r) = {b:+.3f}"
          f"   band corr = {c:+.3f}")
    print(f"  window corr(p(X),t(X)) = {pop['corr_p_t']:+.8f}"
          f"   tagged corr(F,T) = {pop['corr_k_t']:+.8f}"
          f"   attenuation = {pop['attenuation']:.8f}")
