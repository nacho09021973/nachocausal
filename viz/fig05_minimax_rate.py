"""Deterministic diagnostics for the fixed-corner minimax theorem.

The figure evaluates the comparable-pair probability, the direct-score Fisher
diagnostic and its small-lapse scaling, and the two n^{-1/2} risk expressions
from Corollary 3.10.  Any expression using a maximum of a finite Fisher mesh is
labelled as a numerical diagnostic, not as a certified value of Ibar.

No sprinkling, validation seed, or sealed-instrument output is used.

Run:
    python3 viz/fig05_minimax_rate.py
"""

from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.special import lambertw


R_P = 3.0
R_Q = 0.5
V_P = 0.0
DELTA_V = 0.02
V_Q = V_P + DELTA_V
TAU_MIN = 1.0
TAU_MAX = 1.2
TAU_PLOT_NODES = 41
SCORE_NODES = 961
FINAL_SCORE_NODES = 1921
LAPSE_SWEEP = np.array([0.080, 0.040, 0.020, 0.010, 0.005])

BLUE = "#2474a6"
ORANGE = "#d97904"
GREY = "#5c6770"
RED = "#b33a3a"


def omega(r, tau):
    """omega_tau(r) = exp(r/tau) (r/tau - 1)."""
    x = np.asarray(r, dtype=float) / tau
    return np.exp(x) * (x - 1.0)


def omega_inv(value, tau):
    """Principal real inverse of omega_tau on r > 0."""
    return tau * (1.0 + np.real(lambertw(np.asarray(value) / np.e, 0)))


def ray_radius(r0, lapse, tau):
    """Radius after a null-coordinate lapse along an outgoing ray."""
    return omega_inv(np.exp(lapse / (2.0 * tau)) * omega(r0, tau), tau)


def diamond_subarea(r_x, lapse, tau):
    """Area of J+(x) intersected with the fixed-corner diamond."""
    return (
        ray_radius(r_x, lapse, tau) ** 2
        + ray_radius(R_Q, -lapse, tau) ** 2
        - r_x**2
        - R_Q**2
    )


def comparable_probability(tau, quadrature_nodes=96, lapse=DELTA_V):
    """Comparable-pair probability via the exact two-fold reduction."""
    total_area = diamond_subarea(R_P, lapse, tau)

    x_lapse, w_lapse = np.polynomial.legendre.leggauss(quadrature_nodes)
    remaining = 0.5 * lapse * (x_lapse + 1.0)
    w_lapse = 0.5 * lapse * w_lapse
    upper = ray_radius(R_P, lapse - remaining, tau)
    lower = ray_radius(R_Q, -remaining, tau)

    x_r, w_r = np.polynomial.legendre.leggauss(quadrature_nodes)
    midpoint = 0.5 * (upper + lower)[:, None]
    half_width = 0.5 * (upper - lower)[:, None]
    radius = midpoint + half_width * x_r[None, :]
    integrand = (
        ray_radius(radius, remaining[:, None], tau) ** 2
        + lower[:, None] ** 2
        - radius**2
        - R_Q**2
    )
    numerator = np.sum(w_lapse * half_width[:, 0] * np.sum(integrand * w_r, axis=1))
    return float(2.0 * numerator / total_area**2)


def kappa_separation():
    """Closed coefficient in p(tau)=1/2+kappa*tau*Delta_v+O(Delta_v^2)."""
    a, b = R_P, R_Q
    return ((a * a - b * b) - 2.0 * a * b * np.log(a / b)) / (
        12.0 * a * b * (a - b) ** 2
    )


def _corner_u(tau, v, radius):
    return -np.exp(-v / (2.0 * tau)) * omega(radius, tau)


def _corner_u_derivative(tau, v, radius):
    w_value = omega(radius, tau)
    return -np.exp(-v / (2.0 * tau)) * (
        v * w_value / (2.0 * tau**2)
        - radius**2 * np.exp(radius / tau) / tau**3
    )


def direct_fisher(tau, nodes=SCORE_NODES, lapse=DELTA_V):
    """Evaluate I(tau) from the analytic fixed-rank copula score.

    This implements research_program/work_packages/
    wp4_ibar_direct_score_derivation.md, Sections 4--8, on a tensor grid.
    It returns diagnostics for the score identities as well as the integral.
    """
    w_grid = np.linspace(0.0, 1.0, nodes)
    v_q = V_P + lapse
    v_grid = np.linspace(V_P, v_q, nodes)
    w = w_grid[:, None]
    v = v_grid[None, :]

    u_p = _corner_u(tau, V_P, R_P)
    u_q = _corner_u(tau, v_q, R_Q)
    delta_u = u_q - u_p
    u_p_prime = _corner_u_derivative(tau, V_P, R_P)
    u_q_prime = _corner_u_derivative(tau, v_q, R_Q)
    delta_u_prime = u_q_prime - u_p_prime
    beta = u_p_prime + w * delta_u_prime

    u = u_p + w * delta_u
    omega_value = -u * np.exp(v / (2.0 * tau))
    radius = omega_inv(omega_value, tau)
    w_prime = radius * np.exp(radius / tau) / tau**2
    exp_factor = np.exp(v / (2.0 * tau))

    h_tilde = exp_factor * delta_u / w_prime
    u_gradient = (1.0 / radius + 1.0 / tau) * exp_factor / w_prime
    d_log_h = (
        1.0 / tau
        - v / (2.0 * radius**2)
        + u_gradient * beta
        + delta_u_prime / delta_u
    )
    dw_log_h = u_gradient * delta_u
    dv_log_h = tau / (2.0 * radius**2)

    marginal_w = np.trapz(h_tilde, v_grid, axis=1)
    marginal_v = np.trapz(h_tilde, w_grid, axis=0)
    area = float(np.trapz(marginal_w, w_grid))
    density = h_tilde / area
    density_w = marginal_w / area
    density_v = marginal_v / area

    mean_d_given_w = np.trapz(h_tilde * d_log_h, v_grid, axis=1) / marginal_w
    mean_d_given_v = np.trapz(h_tilde * d_log_h, w_grid, axis=0) / marginal_v
    mean_d = float(np.trapz(np.trapz(h_tilde * d_log_h, v_grid, axis=1), w_grid) / area)

    d_cdf_w = cumulative_trapezoid(
        density_w * (mean_d_given_w - mean_d), w_grid, initial=0.0
    )
    d_cdf_v = cumulative_trapezoid(
        density_v * (mean_d_given_v - mean_d), v_grid, initial=0.0
    )
    a_w = -d_cdf_w / density_w
    a_v = -d_cdf_v / density_v

    mean_dw_given_w = np.trapz(h_tilde * dw_log_h, v_grid, axis=1) / marginal_w
    mean_dv_given_v = np.trapz(h_tilde * dv_log_h, w_grid, axis=0) / marginal_v
    partial_tau_g = (
        d_log_h
        - mean_d_given_w[:, None]
        - mean_d_given_v[None, :]
        + mean_d
    )
    partial_w_g = dw_log_h - mean_dw_given_w[:, None]
    partial_v_g = dv_log_h - mean_dv_given_v[None, :]
    score = partial_tau_g + a_w[:, None] * partial_w_g + a_v[None, :] * partial_v_g

    fisher = float(np.trapz(np.trapz(density * score**2, v_grid, axis=1), w_grid))
    global_score_mean = float(np.trapz(np.trapz(density * score, v_grid, axis=1), w_grid))
    slice_w = np.trapz(h_tilde * score, v_grid, axis=1) / marginal_w
    slice_v = np.trapz(h_tilde * score, w_grid, axis=0) / marginal_v

    return {
        "fisher": fisher,
        "area": area,
        "score_mean": global_score_mean,
        "slice_w_max": float(np.max(np.abs(slice_w))),
        "slice_v_max": float(np.max(np.abs(slice_v))),
        "cdf_endpoint_max": float(max(abs(d_cdf_w[-1]), abs(d_cdf_v[-1]))),
        "corner_error": float(max(abs(radius[0, 0] - R_P), abs(radius[-1, -1] - R_Q))),
    }


def diagnostic_sweep():
    """Print the complete deterministic refinement sweep used by the figure."""
    print("direct-score spatial refinement (diagnostic, not an Ibar enclosure)")
    for tau in (TAU_MIN, 0.5 * (TAU_MIN + TAU_MAX), TAU_MAX):
        values = []
        for nodes in (481, 961, 1921):
            result = direct_fisher(tau, nodes)
            values.append(result["fisher"])
            print(
                f"tau={tau:.3f} nodes={nodes:3d} I={result['fisher']:.10e} "
                f"Escore={result['score_mean']:+.2e} "
                f"slice=({result['slice_w_max']:.2e},{result['slice_v_max']:.2e}) "
                f"dCDF={result['cdf_endpoint_max']:.2e} corner={result['corner_error']:.2e}"
            )
        print(f"  relative change 961->1921: {abs(values[-1]-values[-2])/values[-1]:.3e}")

    print("small-lapse sweep at tau=1 (961 nodes per axis)")
    normalized = []
    for lapse in LAPSE_SWEEP:
        fisher = direct_fisher(TAU_MIN, SCORE_NODES, lapse)["fisher"]
        ratio = fisher / lapse**2
        normalized.append(ratio)
        print(f"Delta_v={lapse:.3f} I={fisher:.10e} I/Delta_v^2={ratio:.8f}")
    richardson = 2.0 * normalized[-1] - normalized[-2]
    print(f"linear Richardson limit from Delta_v=0.010,0.005: {richardson:.8f}")

    print("small-lapse comparable-pair remainder relative to p-1/2")
    kappa = kappa_separation()
    for lapse in (0.020, 0.005):
        taus = np.linspace(TAU_MIN, TAU_MAX, TAU_PLOT_NODES)
        p_values = np.array([comparable_probability(tau, lapse=lapse) for tau in taus])
        leading = 0.5 + kappa * taus * lapse
        relative = np.abs(p_values - leading) / np.abs(p_values - 0.5)
        print(
            f"Delta_v={lapse:.3f} relative remainder at tau=1={relative[0]:.6%} "
            f"mesh max={np.max(relative):.6%}"
        )


def draw(out):
    # Isolate this asset from any plotting state left by earlier generators.
    plt.rcdefaults()
    taus = np.linspace(TAU_MIN, TAU_MAX, TAU_PLOT_NODES)
    p_values = np.array([comparable_probability(tau) for tau in taus])
    fisher_values = np.array(
        [direct_fisher(tau, FINAL_SCORE_NODES)["fisher"] for tau in taus]
    )
    if not np.all(np.diff(p_values) > 0.0):
        raise AssertionError("comparable-pair probability is not increasing on the plotted mesh")
    if not np.all(fisher_values > 0.0):
        raise AssertionError("direct Fisher diagnostic must be positive")
    if not np.all(np.diff(fisher_values) < 0.0):
        raise AssertionError("direct Fisher diagnostic is not decreasing on the plotted mesh")
    p_derivative = np.gradient(p_values, taus, edge_order=2)
    fisher_cauchy_lower = 2.0 * p_derivative**2
    if np.any(fisher_values < fisher_cauchy_lower):
        raise AssertionError("direct Fisher diagnostic violates I(tau) >= 2 p'(tau)^2")
    cauchy_ratio_min = float(np.min(fisher_values / fisher_cauchy_lower))
    fisher_mesh_max = float(np.max(fisher_values))
    fisher_argmax = float(taus[np.argmax(fisher_values)])
    kappa = kappa_separation()

    lapse_fisher = np.array(
        [direct_fisher(TAU_MIN, SCORE_NODES, lapse)["fisher"] for lapse in LAPSE_SWEEP]
    )
    lapse_normalized = lapse_fisher / LAPSE_SWEEP**2
    richardson = float(2.0 * lapse_normalized[-1] - lapse_normalized[-2])

    sample_sizes = np.logspace(2, 12, 300)
    le_cam_diagnostic = 1.0 / (8.0 * np.sqrt(sample_sizes * fisher_mesh_max))
    plugin_upper = 2.0 / (kappa * DELTA_V * np.sqrt(sample_sizes))

    diameter = TAU_MAX - TAU_MIN
    le_cam_coefficient = 1.0 / (8.0 * np.sqrt(fisher_mesh_max))
    plugin_coefficient = 2.0 / (kappa * DELTA_V)
    le_cam_crossing = (le_cam_coefficient / diameter) ** 2
    plugin_crossing = (plugin_coefficient / diameter) ** 2

    fig, axes = plt.subplots(2, 2, figsize=(13.0, 9.0))
    ax_a, ax_b, ax_c, ax_d = axes.flat

    ax_a.plot(taus, p_values, color=BLUE, linewidth=2.5, label="deterministic quadrature")
    leading = 0.5 + kappa * taus * DELTA_V
    ax_a.plot(taus, leading, color=GREY, linestyle="--", linewidth=1.7,
              label=r"$1/2+\kappa\tau\Delta v$")
    ax_a.set_xlabel(r"parameter $\tau$")
    ax_a.set_ylabel(r"comparable-pair probability $p(\tau)$")
    ax_a.set_title(r"A · fixed corners: $p(\tau)$ is increasing", loc="left")
    ax_a.legend(frameon=False)
    ax_a.grid(alpha=0.22)

    ax_b.semilogy(taus, fisher_values, color=BLUE, linewidth=2.4,
                  label=r"direct score $I(\tau)$ (1921 nodes/axis)")
    ax_b.semilogy(taus, fisher_cauchy_lower, color=ORANGE, linestyle="--", linewidth=2.0,
                  label=r"Cauchy lower quantity $2p'(\tau)^2$")
    ax_b.set_xlabel(r"parameter $\tau$")
    ax_b.set_ylabel("information scale")
    ax_b.set_title(r"B · Fisher information and proved lower quantity", loc="left")
    ax_b.grid(alpha=0.22)
    ax_b.legend(frameon=False, fontsize=8.7)
    ax_b.text(0.03, 0.05, rf"$\min I/(2p'^2)={cauchy_ratio_min:.3f}$",
              transform=ax_b.transAxes, fontsize=9.2, color=GREY)

    ax_c.plot(LAPSE_SWEEP, lapse_normalized, color=BLUE, linewidth=2.2,
              marker="o", markersize=5.5, label=r"$I(\tau_0)/(\Delta v)^2$")
    ax_c.axhline(richardson, color=GREY, linestyle="--", linewidth=1.7,
                 label=rf"linear Richardson limit $\approx {richardson:.4f}$")
    ax_c.set_xscale("log")
    ax_c.invert_xaxis()
    ax_c.set_xlabel(r"null lapse $\Delta v$ (decreasing to the right)")
    ax_c.set_ylabel(r"normalized information $I(\tau_0)/(\Delta v)^2$")
    ax_c.set_title(r"C · small-lapse scaling at $\tau_0=1$", loc="left")
    ax_c.grid(alpha=0.22)
    ax_c.legend(frameon=False, fontsize=8.7)

    ax_d.loglog(sample_sizes, plugin_upper, color=ORANGE, linewidth=2.4,
                label=r"plug-in expression $2/(\kappa\Delta v\sqrt{n})$")
    ax_d.loglog(sample_sizes, le_cam_diagnostic, color=BLUE, linewidth=2.4,
                label=r"Le Cam expression with $\widehat{\bar I}_{\rm mesh}$")
    ax_d.axhspan(diameter, max(plugin_upper[0], diameter), color="#eceff1", alpha=0.85,
                 label=r"above parameter diameter $0.2$")
    ax_d.axhline(diameter, color=GREY, linestyle=":", linewidth=1.5)
    ax_d.axvline(le_cam_crossing, color=BLUE, linestyle=":", linewidth=1.2)
    ax_d.axvline(plugin_crossing, color=ORANGE, linestyle=":", linewidth=1.2)
    ax_d.set_xlabel(r"cardinality $n$")
    ax_d.set_ylabel("uncapped absolute-risk expression")
    ax_d.set_title(r"D · asymptotic rate and the trivial finite-$n$ region", loc="left")
    ax_d.grid(alpha=0.22, which="both")
    ax_d.legend(frameon=False, fontsize=8.2, loc="lower left")
    ax_d.text(
        0.98,
        0.96,
        rf"crossings: $8.3\times10^4$ (diagnostic)"
        "\n" + rf"$2.8\times10^8$ (plug-in)",
        transform=ax_d.transAxes,
        ha="right",
        va="top",
        fontsize=8.8,
        color=RED,
    )

    fig.suptitle("Fixed-corner shape information: signal, information, and asymptotic rate",
                 fontsize=14)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(out, dpi=180)
    plt.close(fig)
    diagnostics = {
        "lapse_fisher": lapse_fisher,
        "lapse_normalized": lapse_normalized,
        "richardson": richardson,
        "le_cam_crossing": le_cam_crossing,
        "plugin_crossing": plugin_crossing,
    }
    return (
        out,
        p_values,
        fisher_values,
        fisher_mesh_max,
        fisher_argmax,
        cauchy_ratio_min,
        diagnostics,
    )


if __name__ == "__main__":
    diagnostic_sweep()
    target = pathlib.Path(__file__).parent / "output" / "fig05_minimax_rate.png"
    target.parent.mkdir(exist_ok=True)
    (
        path,
        p_values,
        fisher_values,
        fisher_mesh_max,
        fisher_argmax,
        cauchy_ratio_min,
        diagnostics,
    ) = draw(target)
    print(f"written {path}")
    print(f"p endpoints = ({p_values[0]:.12f}, {p_values[-1]:.12f})")
    print(
        f"I mesh range = [{fisher_values.min():.10e}, {fisher_values.max():.10e}], "
        f"mesh maximum at tau={fisher_argmax:.3f}"
    )
    print(f"minimum diagnostic ratio I/(2 p_prime^2) = {cauchy_ratio_min:.6f} (must exceed 1)")
    print(f"small-lapse Richardson limit = {diagnostics['richardson']:.8f}")
    print(
        "diameter crossings: "
        f"Le Cam diagnostic={diagnostics['le_cam_crossing']:.6e}, "
        f"plug-in={diagnostics['plugin_crossing']:.6e}"
    )
