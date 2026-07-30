"""dev exploration -- visualize p(tau) as it actually looks, for the C6 /
Theorem 3.9 priority audit (research_program/bibliography/
c6_theorem39_priority_audit.md).

The audit's open question (T39-B/C) is whether the *shape* of p(tau) -- the
comparable-pair probability on the Schwarzschild EF diamond family D_tau --
is really the claimed p(tau) = 1/2 + kappa(r_p,r_q)*tau*dv + O(dv^2), strictly
increasing and Lipschitz-separated on 0 < dv < dv_0. This script does not
re-derive anything: it imports the already-verified numerics from
research_program/work_packages/wp4_comparable_pair_separation_checks.py
(quadrature p_comparable, closed-form kappa, Richardson extrapolation) and
plots them, so the shape can be inspected directly instead of read off
printed assertions.

Mathematics only. NOT part of the sealed instrument: no threshold, no seed
band, no generator, no estimator, no validation artifact; imports nothing
from `nachocausal/`. Reuses the WP4 checks module (also outside the seal).

Run with:
    PYTHONDONTWRITEBYTECODE=1 python3 dev/explore_p_tau_shape.py
Writes PNGs to dev_ensemble_raw/p_tau_shape/ (git-ignored).
"""
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                 "research_program", "work_packages"))
from wp4_comparable_pair_separation_checks import (   # noqa: E402
    p_comparable, kappa_closed_form, K_extrapolated,
)

OUT_DIR = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..",
    "dev_ensemble_raw", "p_tau_shape"))

# The diamond of record used throughout the WP4 note and its checks script.
R_P, R_Q = 3.0, 0.5
TAU0, TAU1 = 0.6, 1.8   # a compact K = [tau0, tau1]


def plot_p_of_tau():
    """p(tau) over K, at a few fixed dv -- is it really monotone increasing?"""
    taus = np.linspace(TAU0, TAU1, 60)
    fig, ax = plt.subplots(figsize=(7, 5))
    for dv in (0.02, 0.1, 0.5, 2.0):
        ps = [p_comparable(t, R_P, R_Q, dv, 120, 120)[0] for t in taus]
        ax.plot(taus, ps, marker="o", markersize=3, label=f"dv={dv}")
        mono = np.all(np.diff(ps) > 0)
        print(f"  dv={dv:<5} strictly increasing over the grid: {mono}")
    ax.axhline(0.5, color="gray", lw=0.8, ls=":")
    ax.set_xlabel("tau")
    ax.set_ylabel("p(tau)  (comparable-pair probability)")
    ax.set_title(f"p(tau) on D_tau, r_p={R_P}, r_q={R_Q}, K=[{TAU0},{TAU1}]")
    ax.legend()
    fig.tight_layout()
    path = os.path.join(OUT_DIR, "p_of_tau.png")
    fig.savefig(path, dpi=140)
    plt.close(fig)
    print(f"  wrote {path}")


def plot_kappa_shape():
    """kappa(r_p, r_q) as a function of the single ratio x = r_p/r_q > 1."""
    xs = np.linspace(1.02, 8.0, 200)
    r_q = 1.0
    kap = kappa_closed_form(xs * r_q, r_q) * r_q  # kappa*r_q vs x = r_p/r_q, r_q fixed
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(xs, kap)
    ax.axhline(0.0, color="gray", lw=0.8, ls=":")
    ax.set_xlabel("x = r_p / r_q")
    ax.set_ylabel("kappa(r_p, r_q) * r_q")
    ax.set_title("Closed-form kappa: strictly positive for x > 1, -> 0 as x -> 1")
    fig.tight_layout()
    path = os.path.join(OUT_DIR, "kappa_shape.png")
    fig.savefig(path, dpi=140)
    plt.close(fig)
    print(f"  wrote {path}")
    print(f"  kappa*r_q range on x in [{xs[0]:.2f},{xs[-1]:.2f}]: "
          f"[{kap.min():.6f}, {kap.max():.6f}]  (all > 0: {bool(np.all(kap > 0))})")


def plot_residual_order():
    """R(tau,dv) := p(tau) - (1/2 + kappa*tau*dv) vs dv, log-log -- is it O(dv^2)?"""
    tau = 1.0
    kap = kappa_closed_form(R_P, R_Q)
    dvs = np.array([0.32, 0.16, 0.08, 0.04, 0.02, 0.01, 0.005])
    resid = np.array([
        p_comparable(tau, R_P, R_Q, dv, 220, 220)[0] - (0.5 + kap * tau * dv)
        for dv in dvs
    ])
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.loglog(dvs, np.abs(resid), marker="o", label="|R(tau,dv)|")
    ax.loglog(dvs, np.abs(resid[0]) * (dvs / dvs[0]) ** 2, ls="--",
              label="reference slope dv^2")
    ax.set_xlabel("dv")
    ax.set_ylabel("|residual|")
    ax.set_title(f"Residual of the linear-in-dv term, tau={tau}, r_p={R_P}, r_q={R_Q}")
    ax.legend()
    fig.tight_layout()
    path = os.path.join(OUT_DIR, "residual_order.png")
    fig.savefig(path, dpi=140)
    plt.close(fig)
    print(f"  wrote {path}")
    # empirical local slope in log-log, halving dv each step
    slopes = np.log(np.abs(resid[:-1]) / np.abs(resid[1:])) / np.log(2.0)
    print("  local log2-slope between successive halvings (expect ~2):",
          np.round(slopes, 2))


def plot_lipschitz_separation():
    """|p(tau') - p(tau)| vs the claimed lower bound kappa*dv/2*|tau'-tau|."""
    dv = 0.05
    kap = kappa_closed_form(R_P, R_Q)
    tau_ref = TAU0
    taus = np.linspace(TAU0 + 0.02, TAU1, 40)
    p_ref = p_comparable(tau_ref, R_P, R_Q, dv, 200, 200)[0]
    diffs = np.array([abs(p_comparable(t, R_P, R_Q, dv, 200, 200)[0] - p_ref) for t in taus])
    bound = kap * dv / 2.0 * (taus - tau_ref)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(taus, diffs, marker="o", markersize=3, label="|p(tau) - p(tau_ref)|")
    ax.plot(taus, bound, ls="--", label="claimed lower bound kappa*dv/2*|tau-tau_ref|")
    ax.set_xlabel("tau")
    ax.set_ylabel("separation")
    ax.set_title(f"Uniform separation vs Theorem 3.9(1) lower bound, dv={dv}")
    ax.legend()
    fig.tight_layout()
    path = os.path.join(OUT_DIR, "lipschitz_separation.png")
    fig.savefig(path, dpi=140)
    plt.close(fig)
    print(f"  wrote {path}")
    print("  bound holds pointwise on grid (diff >= bound):",
          bool(np.all(diffs >= bound - 1e-12)))


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print("[A] p(tau) over K, several dv:")
    plot_p_of_tau()
    print()
    print("[B] kappa(r_p, r_q) shape vs x = r_p/r_q:")
    plot_kappa_shape()
    print()
    print("[C] residual order (is it really O(dv^2)?):")
    plot_residual_order()
    print()
    print("[D] Lipschitz/monotone separation vs the proved lower bound:")
    plot_lipschitz_separation()
    print()
    print(f"All figures written to {OUT_DIR}/ (git-ignored, dev_ensemble_raw).")


if __name__ == "__main__":
    main()
