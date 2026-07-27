"""Fail-closed verifier for the WP4 Ibar executable contract.

This is intentionally separate from ``wp4_kappa_numeric_reference.py``.  It implements the
primary fixed ladders, the endpoint formulas, and the independent adaptive validation specified in
``wp4_ibar_interval_executable_contract.md``.  It writes no scientific artifact: stdout is the
execution record and a non-success terminal is a valid result.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import exp, isfinite, sqrt

import numpy as np
from scipy.integrate import cumulative_trapezoid, quad
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq


RP, RQ, VP, VQ = 3.0, 0.5, 0.0, 0.02
TAU_LO, TAU_HI = 1.0, 1.2
SPATIAL_LEVELS = ((160, 160, 32, 32), (240, 240, 48, 48), (360, 360, 72, 72), (540, 540, 108, 108))
DELTAS = (0.04, 0.02, 0.01, 0.005, 0.0025)
A_POINT, R_POINT = 1e-8, 1e-2
ROOT_XTOL = ROOT_RTOL = 1e-12
MASS_TOL, DENSITY_TOL = 1e-10, -1e-13


class Terminal(str, Enum):
    CONVERGED_POINTWISE_AND_ENVELOPE = "CONVERGED_POINTWISE_AND_ENVELOPE"
    POINTWISE_CONVERGED_ENVELOPE_UNRESOLVED = "POINTWISE_CONVERGED_ENVELOPE_UNRESOLVED"
    NUMERICAL_NONCONVERGENCE = "NUMERICAL_NONCONVERGENCE"
    DOMAIN_OR_SCORE_SINGULARITY = "DOMAIN_OR_SCORE_SINGULARITY"


class ContractFailure(RuntimeError):
    pass


class DomainFailure(ContractFailure):
    pass


def W(tau: float, r: float) -> float:
    return exp(r / tau) * (r / tau - 1.0)


def Wp(tau: float, r: float) -> float:
    return r * exp(r / tau) / tau**2


def utilde(tau: float, v: float, r: float) -> float:
    return -exp(-v / (2.0 * tau)) * W(tau, r)


@dataclass(frozen=True)
class Family:
    tau: float
    area: float
    us: np.ndarray
    vs: np.ndarray
    m1_values: np.ndarray
    m2_values: np.ndarray
    finv: PchipInterpolator
    ginv: PchipInterpolator
    m1: PchipInterpolator
    m2: PchipInterpolator


def r_of_u(tau: float, v: float, target: float) -> float:
    def residual(r: float) -> float:
        return utilde(tau, v, r) - target

    lo, hi = 1e-10, 60.0
    flo, fhi = residual(lo), residual(hi)
    if not (isfinite(flo) and isfinite(fhi) and flo * fhi < 0.0):
        raise DomainFailure("root bracket does not enclose a unique radial root")
    root = brentq(residual, lo, hi, xtol=ROOT_XTOL, rtol=ROOT_RTOL)
    if not (lo < root < hi and isfinite(root)):
        raise DomainFailure("invalid radial root")
    return root


def _strictly_increasing(values: np.ndarray, label: str) -> None:
    if not np.all(np.isfinite(values)) or not np.all(np.diff(values) > 0.0):
        raise DomainFailure(f"{label} is not strictly increasing")


def build_family(tau: float, nu: int, nv: int) -> Family:
    if not (TAU_LO <= tau <= TAU_HI):
        raise DomainFailure("family tau is outside the frozen interval")
    up, uq = utilde(tau, VP, RP), utilde(tau, VQ, RQ)
    if not (up < 0.0 < uq):
        raise DomainFailure("diamond fails frozen horizon-straddling geometry")
    us = np.linspace(up, uq, nu)
    vs = np.linspace(VP, VQ, nv)
    h = np.empty((nv, nu), dtype=float)
    for i, v in enumerate(vs):
        for j, u in enumerate(us):
            r = r_of_u(tau, float(v), float(u))
            h[i, j] = exp(v / (2.0 * tau)) / Wp(tau, r)
    if not np.all(np.isfinite(h)) or np.min(h) < DENSITY_TOL:
        raise DomainFailure("non-finite or negative pushed-forward density")
    m1_values = np.trapz(h, vs, axis=0)
    m2_values = np.trapz(h, us, axis=1)
    area = float(np.trapz(m2_values, vs))
    area_cross = float(np.trapz(m1_values, us))
    if not (isfinite(area) and area > 0.0 and abs(area - area_cross) / area <= MASS_TOL):
        raise DomainFailure("mass normalisation/cross-axis check failed")
    f = cumulative_trapezoid(m1_values, us, initial=0.0) / area
    g = cumulative_trapezoid(m2_values, vs, initial=0.0) / area
    f[-1], g[-1] = 1.0, 1.0
    _strictly_increasing(f, "first CDF")
    _strictly_increasing(g, "second CDF")
    return Family(tau, area, us, vs, m1_values, m2_values, PchipInterpolator(f, us), PchipInterpolator(g, vs),
                  PchipInterpolator(us, m1_values), PchipInterpolator(vs, m2_values))


def copula_density(family: Family, x: float, y: float) -> float:
    if not (0.0 < x < 1.0 and 0.0 < y < 1.0):
        raise DomainFailure("copula evaluation outside open unit square")
    u, v = float(family.finv(x)), float(family.ginv(y))
    if not (isfinite(u) and isfinite(v)):
        raise DomainFailure("quantile inversion returned non-finite coordinate")
    r = r_of_u(family.tau, v, u)
    denominator = float(family.m1(u) * family.m2(v))
    value = family.area * exp(v / (2.0 * family.tau)) / Wp(family.tau, r) / denominator
    if not (isfinite(value) and value >= DENSITY_TOL):
        raise DomainFailure("invalid copula density")
    return max(value, 0.0)


def h2_midpoint(left: Family, right: Family, mx: int, my: int) -> float:
    total = 0.0
    for x in (np.arange(mx) + 0.5) / mx:
        for y in (np.arange(my) + 0.5) / my:
            cl, cr = copula_density(left, float(x), float(y)), copula_density(right, float(x), float(y))
            total += (sqrt(cl) - sqrt(cr)) ** 2
    result = total / (mx * my)
    if not (isfinite(result) and result >= 0.0):
        raise DomainFailure("invalid Hellinger integral")
    return result


def estimate_i(tau: float, delta: float, level: tuple[int, int, int, int]) -> float:
    nu, nv, mx, my = level
    if tau - delta / 2.0 >= TAU_LO and tau + delta / 2.0 <= TAU_HI:
        left, right = tau - delta / 2.0, tau + delta / 2.0
    elif tau + delta <= TAU_HI:
        left, right = tau, tau + delta
    elif tau - delta >= TAU_LO:
        left, right = tau - delta, tau
    else:
        raise DomainFailure("no declared symmetric or unilateral derivative stencil")
    h2 = h2_midpoint(build_family(left, nu, nv), build_family(right, nu, nv), mx, my)
    value = 4.0 * h2 / delta**2
    if not (isfinite(value) and value >= 0.0):
        raise DomainFailure("invalid Fisher estimate")
    return value


def close(a: float, b: float) -> bool:
    return abs(a - b) <= A_POINT + R_POINT * max(abs(a), abs(b))


def pointwise_primary(tau: float) -> tuple[bool, list[float], list[float]]:
    spatial = [estimate_i(tau, 0.01, level) for level in SPATIAL_LEVELS]
    derivative = [estimate_i(tau, delta, SPATIAL_LEVELS[-1]) for delta in DELTAS]
    spatial_ok = all(close(spatial[i], spatial[i + 1]) for i in range(3))
    derivative_ok = all(close(derivative[i], derivative[i + 1]) for i in range(4))
    return spatial_ok and derivative_ok, spatial, derivative


def _cdf_by_quad(family: Family, x: float, first: bool) -> float:
    # Independent CDF evaluator: adaptive integral of a piecewise-linear raw marginal, then root;
    # it deliberately does not reuse the primary PCHIP inverse or its interpolation.
    if first:
        lo, hi, grid, values = float(family.us[0]), float(family.us[-1]), family.us, family.m1_values
    else:
        lo, hi, grid, values = float(family.vs[0]), float(family.vs[-1]), family.vs, family.m2_values
    target = x * family.area
    def residual(z: float) -> float:
        return quad(lambda q: float(np.interp(q, grid, values)), lo, z, epsabs=1e-10, epsrel=1e-8)[0] - target
    return brentq(residual, lo, hi, xtol=ROOT_XTOL, rtol=ROOT_RTOL)


def h2_adaptive(left: Family, right: Family) -> float:
    # Independent adaptive integration in (x,y); coordinate inversions use the adaptive-CDF root route.
    def density_from_roots(family: Family, x: float, y: float) -> float:
        u, v = _cdf_by_quad(family, x, True), _cdf_by_quad(family, y, False)
        r = r_of_u(family.tau, v, u)
        m1 = float(np.interp(u, family.us, family.m1_values))
        m2 = float(np.interp(v, family.vs, family.m2_values))
        return family.area * exp(v / (2.0 * family.tau)) / Wp(family.tau, r) / (m1 * m2)
    def inner(x: float) -> float:
        return quad(lambda y: (sqrt(density_from_roots(left, x, y)) - sqrt(density_from_roots(right, x, y))) ** 2,
                    0.0, 1.0, epsabs=1e-10, epsrel=1e-8, points=[0.0, 1.0], limit=100)[0]
    return quad(inner, 0.0, 1.0, epsabs=1e-10, epsrel=1e-8, points=[0.0, 1.0], limit=100)[0]


def independent_i(tau: float, delta: float = 0.0025) -> float:
    # The independent path intentionally has no primary-grid/PCHIP inverse reuse.  It uses the S4
    # density construction only as a source of marginals for adaptive CDF integration.
    if tau - delta / 2.0 >= TAU_LO and tau + delta / 2.0 <= TAU_HI:
        left, right = tau - delta / 2.0, tau + delta / 2.0
    elif tau + delta <= TAU_HI:
        left, right = tau, tau + delta
    else:
        left, right = tau - delta, tau
    family_left = build_family(left, *SPATIAL_LEVELS[-1][:2])
    family_right = build_family(right, *SPATIAL_LEVELS[-1][:2])
    return 4.0 * h2_adaptive(family_left, family_right) / delta**2


def run_contract() -> Terminal:
    print("IBAR_EXECUTABLE_CONTRACT=RUNNING deterministic/no-seed/no-artifact")
    point_values: dict[float, float] = {}
    for tau in (TAU_LO + j / 800.0 for j in range(161)):
        try:
            passed, spatial, derivative = pointwise_primary(tau)
        except DomainFailure as exc:
            print(f"tau={tau:.6f} DOMAIN_FAILURE={exc}")
            return Terminal.DOMAIN_OR_SCORE_SINGULARITY
        print(f"tau={tau:.6f} spatial_d0.01={spatial}")
        print(f"tau={tau:.6f} derivative_S4={derivative}")
        if not passed:
            print("POINTWISE_GATE=FAIL no post-hoc refinement permitted")
            return Terminal.NUMERICAL_NONCONVERGENCE
        point_values[tau] = derivative[-1]
    for tau in (TAU_LO, 1.1):
        try:
            independent = independent_i(tau)
        except DomainFailure as exc:
            print(f"tau={tau:.6f} INDEPENDENT_DOMAIN_FAILURE={exc}")
            return Terminal.DOMAIN_OR_SCORE_SINGULARITY
        primary = point_values[tau]
        print(f"tau={tau:.6f} primary={primary:.17g} independent={independent:.17g}")
        if not close(primary, independent):
            print("INDEPENDENT_VALIDATION=FAIL")
            return Terminal.NUMERICAL_NONCONVERGENCE
    # The certified directed-rounding interval backend is intentionally a distinct implementation
    # obligation.  Until it is supplied, its absence is a terminal rather than a mesh maximum.
    print("INTERVAL_ENVELOPE=UNAVAILABLE directed-rounding backend not implemented")
    return Terminal.POINTWISE_CONVERGED_ENVELOPE_UNRESOLVED


if __name__ == "__main__":
    terminal = run_contract()
    print(f"TERMINAL={terminal.value}")
    if terminal != Terminal.CONVERGED_POINTWISE_AND_ENVELOPE:
        print("IBAR_DIAMOND_INTERVAL=INCONCLUSIVE_NUMERICAL_NONCONVERGENCE")
        print("CONSTANT_LEVEL_DEFEATER=NOT_EVALUATED_IBAR_UNAVAILABLE")
