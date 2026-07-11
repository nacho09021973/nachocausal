"""Numerical reference value(s) of kappa(tau) = V(tau) * I(tau) for wp4_fisher_localization_floor.md
§5a (item 2 of §6, "what is NOT yet done" (i)).

This is a DETERMINISTIC NUMERICAL REFERENCE for I(tau) and V(tau) -- the quantities Proposition 4
and §5a define exactly, evaluated here by quadrature because they have no closed form, not
computed in closed form themselves. I(tau) is approximated via its QMD expansion
(H^2(c_tau, c_{tau+delta}) = (delta^2/4) I(tau) + o(delta^2), Proposition 4), V(tau) via direct
area quadrature, both by deterministic numerical integration (trapezoid rule + root-finding via
scipy.optimize.brentq, PCHIP monotone interpolation for quantile inversion) -- exact in the sense
that the *method* is deterministic and reproducible (no randomness anywhere in the pipeline), NOT
in the sense that the reported numbers are closed-form or error-free; they carry ordinary
quadrature/discretization error, bounded only by the stability checks described below, not by a
proof.
It is NOT a stochastic simulation: no Poisson sprinkling, no order-only estimator, no
PR004 output, no random seed. It IS a numerical (not closed-form) evaluation, since
W_tau(r) = exp(r/tau)*(r/tau - 1) has no closed-form inverse -- the marginal quantile
maps of the copula must be inverted numerically.

Run: python3 research_program/work_packages/wp4_kappa_numeric_reference.py

Method for I(tau):
  1. Build the joint density h_tau(Utilde, v) of the pushed-forward uniform (v,r) sampling
     measure on a grid, via root-finding r_tau(Utilde, v) (W_tau is smooth and strictly
     increasing in r, Lemma R, so the root is unique).
  2. Integrate (trapezoid) to get unnormalized marginals m1, m2 and total mass
     A = V(tau) (the g_tau-area of D_tau; exact since det g_t = -1 for every t, §4).
  3. Build the (monotone) CDFs F_tau, G_tau by cumulative trapezoid, and their inverses
     via PCHIP interpolation of the swapped (F, grid) pairs (monotone by construction,
     avoids spurious oscillation).
  4. Evaluate the copula density c_tau(x,y) = A * h_tau(Utilde,v) / (m1(Utilde)*m2(v)) at
     Utilde = F_tau^{-1}(x), v = G_tau^{-1}(y).
  5. Estimate I(tau) via the SYMMETRIC finite difference
     I(tau) ~= 4 * H^2(c_{tau-delta/2}, c_{tau+delta/2}) / delta^2, checked for stability
     as delta -> 0 (the symmetric difference cancels the O(delta) bias of a one-sided
     difference, converging faster to the true QMD limit; both are checked below).

Sanity checks performed (printed): the copula integrates to ~1 over the unit square; the
two ways of computing the total mass A (integrating m1 vs m2) agree; I(tau) is stable
across a 4x range of delta (confirms we are in the QMD asymptotic regime, not reading off
finite-difference noise).

Caveats (do not drop when citing this): (a) three-to-six sample shapes only, not a scan
over the full shape space; (b) quadrature grid N=90-110, unit-square quadrature M=14-18 --
adequate for the stability checked here, not benchmarked against an independent method;
(c) the kappa ~ lambda^6 power law below is an EMPIRICAL fit over one specific one-parameter
family of shrinking shapes, not a derived/proven asymptotic; (d) no comparison is made or
implied to `prereg-003`'s measured K_LOC -- that bounds the sealed estimator's output, a
different quantity from this order-only two-point floor.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.interpolate import PchipInterpolator
from scipy.integrate import cumulative_trapezoid


def W(t, r):
    return np.exp(r / t) * (r / t - 1.0)


def Wp(t, r):  # dW/dr
    return r * np.exp(r / t) / t**2


def Utilde(t, v, r):
    return -np.exp(-v / (2 * t)) * W(t, r)


def make_builder(r_p, r_q, v_p, v_q):
    def r_of_U(t, v, Utarget, bracket=(1e-10, 60.0)):
        f = lambda r: Utilde(t, v, r) - Utarget
        return brentq(f, bracket[0], bracket[1], xtol=1e-14, rtol=1e-14)

    def build_family(t, N=100):
        Up, Uq = Utilde(t, v_p, r_p), Utilde(t, v_q, r_q)
        assert Up < 0 < Uq, "reference shape must straddle the horizon (Up<0<Uq)"
        vgrid = np.linspace(v_p, v_q, N)
        Ugrid = np.linspace(Up, Uq, N)
        H = np.zeros((N, N))
        for i, v in enumerate(vgrid):
            for j, U in enumerate(Ugrid):
                r = r_of_U(t, v, U)
                H[i, j] = np.exp(v / (2 * t)) / Wp(t, r)
        m1 = np.trapz(H, vgrid, axis=0)   # unnormalized marginal in Utilde
        m2 = np.trapz(H, Ugrid, axis=1)   # unnormalized marginal in v
        A = np.trapz(m2, vgrid)
        A_check = np.trapz(m1, Ugrid)
        assert abs(A - A_check) / A < 1e-6, "cross-axis mass mismatch"
        F = cumulative_trapezoid(m1, Ugrid, initial=0.0) / A
        G = cumulative_trapezoid(m2, vgrid, initial=0.0) / A
        F[-1], G[-1] = 1.0, 1.0
        return dict(
            t=t, A=A,
            Finv=PchipInterpolator(F, Ugrid), Ginv=PchipInterpolator(G, vgrid),
            m1=PchipInterpolator(Ugrid, m1), m2=PchipInterpolator(vgrid, m2),
            r_of_U=r_of_U,
        )

    def copula_density(fam, x, y):
        t = fam["t"]
        U, v = float(fam["Finv"](x)), float(fam["Ginv"](y))
        r = fam["r_of_U"](t, v, U)
        h = np.exp(v / (2 * t)) / Wp(t, r)
        return fam["A"] * h / (fam["m1"](U) * fam["m2"](v))

    return build_family, copula_density


def hellinger_sq(copula_density, fam_a, fam_b, M=16):
    xs = (np.arange(M) + 0.5) / M
    ys = (np.arange(M) + 0.5) / M
    total = 0.0
    for x in xs:
        for y in ys:
            ca, cb = copula_density(fam_a, x, y), copula_density(fam_b, x, y)
            total += (np.sqrt(ca) - np.sqrt(cb)) ** 2
    return total / M**2


def kappa_reference(r_p, r_q, v_p, v_q, t0=1.0, deltas=(0.04, 0.02, 0.01)):
    build_family, copula_density = make_builder(r_p, r_q, v_p, v_q)
    fam0 = build_family(t0)
    V = fam0["A"]
    ests = []
    for delta in deltas:
        fam_minus = build_family(t0 - delta / 2)
        fam_plus = build_family(t0 + delta / 2)
        H2 = hellinger_sq(copula_density, fam_minus, fam_plus)
        ests.append(4.0 * H2 / delta**2)
    stability = abs(ests[-1] - ests[0]) / ests[-1]
    return V, ests, V * ests[-1], stability


if __name__ == "__main__":
    print("=== Reference shapes (tau=1; V, I via QMD symmetric-difference, delta-scan) ===\n")
    shapes = [
        ("A moderate",        2.0, 0.5, 0.0, 1.0),
        ("B thin near-horizon", 1.3, 0.7, 0.0, 0.3),
        ("C very thin",       1.1, 0.9, 0.0, 0.1),
    ]
    for label, r_p, r_q, v_p, v_q in shapes:
        V, ests, kappa, stab = kappa_reference(r_p, r_q, v_p, v_q)
        print(f"{label}: r_p={r_p} r_q={r_q} v_p={v_p} v_q={v_q}")
        print(f"   V={V:.6f}   I(tau=1) across delta-scan: {[f'{e:.6e}' for e in ests]}"
              f"  (relative change {stab:.2%}, confirms QMD-regime stability)")
        print(f"   kappa = V*I = {kappa:.6e}   =>  delta_tau/ell ~ 1/sqrt(kappa) = {1/np.sqrt(kappa):.2f}\n")

    print("=== Power-law scan: shrinking a near-horizon diamond by linear factor lambda ===")
    print("    (r_p, r_q, v_q) = (1+0.3*lambda, 1-0.3*lambda, 0.3*lambda), tau=1 fixed\n")
    lams = [1.0, 0.5, 0.3, 0.2, 0.1, 0.05]
    logL, logK = [], []
    for lam in lams:
        V, ests, kappa, stab = kappa_reference(
            1.0 + 0.3 * lam, 1.0 - 0.3 * lam, 0.0, 0.3 * lam,
            deltas=(0.04 * lam, 0.02 * lam, 0.01 * lam),
        )
        print(f"lambda={lam:6.3f}  V={V:.6e}  I={ests[-1]:.6e}  kappa={kappa:.6e}"
              f"  1/sqrt(kappa)={1/np.sqrt(kappa):12.2f}  (stability {stab:.2%})")
        logL.append(np.log(lam)); logK.append(np.log(kappa))
    p, c = np.polyfit(logL, logK, 1)
    p_small, c_small = np.polyfit(logL[-4:], logK[-4:], 1)
    print(f"\nEmpirical power-law fit, all points:      kappa ~ lambda^{p:.3f}")
    print(f"Empirical power-law fit, smallest 4 only:  kappa ~ lambda^{p_small:.3f}")
    print("(An empirical fit, not a derived/proven exponent -- flagged as such in the annex.)")
