#!/usr/bin/env python3
"""B1.7 formal separation certificate for the true 1+1D control.

The control uses the product order and the natural radial Schwarzschild
volume density H(UV)=exp(-s)/s, where (1-s) exp(s)=UV.  A uniform rational
partition of the patch gives cellwise enclosures of H from the four corners:
H is increasing in w=UV, and a bilinear product reaches its extrema at the
corners of a rectangle.  Ordered-pair blocks then have exact rectangular or
triangular volumes.

The final comparison is outward-directed:

    rho(lambda0) <= U0 < L1 <= rho(lambda1).

No Monte Carlo, seeds, pair search, or n>2 calculation is used.  This script
is a finite enclosure for the frozen pair only.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
from mpmath import iv


iv.dps = 35
INF = float("inf")

LAMBDA0 = (Fraction("0.5"), Fraction("1.0"), Fraction("1.0"), Fraction("0.5"), Fraction("0.1"))
LAMBDA1 = (Fraction("0.2"), Fraction("0.8"), Fraction("2.0"), Fraction("0.9"), Fraction("0.1"))
DEFAULT_CELLS = 160


def up(x: float) -> float:
    return math.nextafter(float(x), INF)


def dn(x: float) -> float:
    return math.nextafter(float(x), -INF)


def add_up(a: float, b: float) -> float:
    return up(np.add(a, b))


def add_dn(a: float, b: float) -> float:
    return dn(np.add(a, b))


def mul_up(a, b):
    return np.nextafter(np.multiply(a, b), INF)


def mul_dn(a, b):
    return np.nextafter(np.multiply(a, b), -INF)


def div_up(a: float, b: float) -> float:
    return up(np.divide(a, b))


def div_dn(a: float, b: float) -> float:
    return dn(np.divide(a, b))


def sum_up(values) -> float:
    values = np.asarray(values, dtype=float).ravel()
    if values.size == 0:
        return 0.0
    while values.size > 1:
        if values.size & 1:
            values = np.concatenate((values, np.array([0.0])))
        values = np.nextafter(values[0::2] + values[1::2], INF)
    return float(values[0])


def sum_dn(values) -> float:
    values = np.asarray(values, dtype=float).ravel()
    if values.size == 0:
        return 0.0
    while values.size > 1:
        if values.size & 1:
            values = np.concatenate((values, np.array([0.0])))
        values = np.nextafter(values[0::2] + values[1::2], -INF)
    return float(values[0])


def frac_bounds(value: Fraction) -> tuple[float, float]:
    exact = value.numerator / value.denominator
    return dn(exact), up(exact)


def iv_lo(value) -> float:
    return dn(float(value.a))


def iv_hi(value) -> float:
    return up(float(value.b))


def rational_iv(value: Fraction):
    return iv.mpf(value.numerator) / value.denominator


def f_iv(s: float):
    S = iv.mpf(s)
    return (iv.mpf(1) - S) * iv.exp(S)


_S_CACHE: dict[Fraction, tuple[float, float]] = {}
_H_CACHE: dict[Fraction, tuple[float, float]] = {}


def s_approx(w: float) -> float:
    lo, hi = 1e-300, 1.0
    while (1.0 - hi) * math.exp(hi) > w:
        hi *= 2.0
    for _ in range(220):
        mid = (lo + hi) / 2.0
        if (1.0 - mid) * math.exp(mid) > w:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def s_encl(w: Fraction) -> tuple[float, float]:
    if w in _S_CACHE:
        return _S_CACHE[w]
    w_float = w.numerator / w.denominator
    w_lo, w_hi = dn(w_float), up(w_float)
    center = s_approx(w_float)
    pad = 1e-13
    for _ in range(100):
        lo = max(1e-300, center - pad * max(1.0, abs(center)))
        hi = center + pad * max(1.0, abs(center))
        # f is strictly decreasing on s>0.  The tests compare outward
        # endpoints against an outward enclosure of the exact rational w.
        if iv_lo(f_iv(lo)) >= w_hi and iv_hi(f_iv(hi)) <= w_lo:
            _S_CACHE[w] = (lo, hi)
            return lo, hi
        pad *= 4.0
    raise RuntimeError(f"no scalar enclosure for w={w}")


def h_encl(w: Fraction) -> tuple[float, float]:
    """Outward enclosure of H(w)=exp(-s(w))/s(w)."""

    if w in _H_CACHE:
        return _H_CACHE[w]
    slo, shi = s_encl(w)
    S = iv.mpf([slo, shi])
    H = iv.exp(-S) / S
    out = (iv_lo(H), iv_hi(H))
    _H_CACHE[w] = out
    return out


def partition(lo: Fraction, hi: Fraction, cells: int) -> list[Fraction]:
    width = (hi - lo) / cells
    return [lo + width * i for i in range(cells + 1)]


def cell_density_bounds(U: list[Fraction], V: list[Fraction]):
    n_u, n_v = len(U) - 1, len(V) - 1
    lo = np.empty((n_u, n_v), dtype=float)
    hi = np.empty((n_u, n_v), dtype=float)
    for i in range(n_u):
        for k in range(n_v):
            corners = (
                U[i] * V[k],
                U[i] * V[k + 1],
                U[i + 1] * V[k],
                U[i + 1] * V[k + 1],
            )
            w_lo, w_hi = min(corners), max(corners)
            lo[i, k], hi[i, k] = h_encl(w_lo)[0], h_encl(w_hi)[1]
    return lo, hi


def normalization_bounds(U: list[Fraction], V: list[Fraction], h_lo, h_hi):
    lo_terms, hi_terms = [], []
    for i in range(len(U) - 1):
        for k in range(len(V) - 1):
            area = (U[i + 1] - U[i]) * (V[k + 1] - V[k])
            area_lo, area_hi = frac_bounds(area)
            lo_terms.append(float(mul_dn(area_lo, h_lo[i, k])))
            hi_terms.append(float(mul_up(area_hi, h_hi[i, k])))
    return sum_dn(lo_terms), sum_up(hi_terms)


def suffix_dn(values: np.ndarray) -> np.ndarray:
    out = np.zeros(len(values) + 1)
    running = 0.0
    for i in range(len(values) - 1, -1, -1):
        out[i + 1] = running
        running = add_dn(running, float(values[i]))
    return out


def suffix_up(values: np.ndarray) -> np.ndarray:
    out = np.zeros(len(values) + 1)
    running = 0.0
    for i in range(len(values) - 1, -1, -1):
        out[i + 1] = running
        running = add_up(running, float(values[i]))
    return out


def ordered_v_bounds(row_x, row_y, dv: list[Fraction]) -> tuple[float, float]:
    dv_lo = np.array([frac_bounds(x)[0] for x in dv])
    dv_hi = np.array([frac_bounds(x)[1] for x in dv])

    ax_lo = mul_dn(row_x, dv_lo)
    by_lo = mul_dn(row_y, dv_lo)
    off_lo = sum_dn(mul_dn(ax_lo, suffix_dn(by_lo)[1:]))
    diag_lo = div_dn(sum_dn(mul_dn(ax_lo, by_lo)), 2.0)
    v_lo = add_dn(off_lo, diag_lo)

    ax_hi = mul_up(row_x, dv_hi)
    by_hi = mul_up(row_y, dv_hi)
    off_hi = sum_up(mul_up(ax_hi, suffix_up(by_hi)[1:]))
    diag_hi = div_up(sum_up(mul_up(ax_hi, by_hi)), 2.0)
    v_hi = add_up(off_hi, diag_hi)
    return v_lo, v_hi


def ordered_pair_bounds(U: list[Fraction], V: list[Fraction], h_lo, h_hi):
    du = [U[i + 1] - U[i] for i in range(len(U) - 1)]
    dv = [V[k + 1] - V[k] for k in range(len(V) - 1)]
    du_lo = [frac_bounds(x)[0] for x in du]
    du_hi = [frac_bounds(x)[1] for x in du]
    lower_terms, upper_terms = [], []
    for i in range(len(du)):
        for j in range(i, len(du)):
            uvol_exact = du[i] * du[j] / (2 if i == j else 1)
            uvol_lo, uvol_hi = frac_bounds(uvol_exact)
            v_lo, v_hi = ordered_v_bounds(h_lo[i], h_lo[j], dv)
            v2_lo, v2_hi = ordered_v_bounds(h_hi[i], h_hi[j], dv)
            lower_terms.append(float(mul_dn(uvol_lo, v_lo)))
            upper_terms.append(float(mul_up(uvol_hi, v2_hi)))
    return sum_dn(lower_terms), sum_up(upper_terms)


def certify(lam: tuple[Fraction, ...], cells: int) -> dict:
    v0, v1, uout, uin, _ = lam
    U = partition(-uout, uin, cells)
    V = partition(v0, v1, cells)
    h_lo, h_hi = cell_density_bounds(U, V)
    z_lo, z_hi = normalization_bounds(U, V, h_lo, h_hi)
    i_lo, i_hi = ordered_pair_bounds(U, V, h_lo, h_hi)
    rho_lo = div_dn(mul_dn(2.0, i_lo), mul_up(z_hi, z_hi))
    rho_hi = div_up(mul_up(2.0, i_hi), mul_dn(z_lo, z_lo))
    return {
        "cells": cells,
        "rho_lower": rho_lo,
        "rho_upper": rho_hi,
        "Z_lower": z_lo,
        "Z_upper": z_hi,
        "ordered_pair_mass_lower": i_lo,
        "ordered_pair_mass_upper": i_hi,
    }


def run(cells: int) -> dict:
    _S_CACHE.clear()
    _H_CACHE.clear()
    c0 = certify(LAMBDA0, cells)
    c1 = certify(LAMBDA1, cells)
    U0 = c0["rho_upper"]
    L1 = c1["rho_lower"]
    gap = L1 - U0
    return {
        "unit": "PUENTE-3P1/B1.7-formal",
        "status": "FROZEN_PAIR / DIRECTED_ROUNDING_ENCLOSURE",
        "frozen_pair": True,
        "lambda_pair": [[float(x) for x in LAMBDA0], [float(x) for x in LAMBDA1]],
        "cells": cells,
        "radial_density": "H(UV)=exp(-s)/s, (1-s) exp(s)=UV",
        "causal_predicate": "Ux < Uy and Vx < Vy",
        "scalar_layer": {
            "s_enclosure": "monotone scalar inequality with mpmath.iv",
            "h_enclosure": "monotonicity of H in w=UV and corner extrema",
        },
        "arithmetic": {
            "mode": "outward directed rounding",
            "partition_nodes": "exact Fractions",
            "sums": "directed pairwise trees",
            "global_slack_constant": None,
        },
        "lambda0": c0,
        "lambda1": c1,
        "U0_1p1d": U0,
        "L1_1p1d": L1,
        "formal_gap": gap,
        "separated": bool(U0 < L1),
        "no_search": True,
        "no_seeds": True,
        "no_monte_carlo": True,
        "n": 2,
        "terminal": (
            "B1.7_TRUE_1P1D_FORMAL_SEPARATION_ESTABLISHED"
            if U0 < L1
            else "B1.7_TRUE_1P1D_FORMAL_CONTROL_INCONCLUSIVE"
        ),
        "claim_ceiling": (
            "For the frozen pair at n=2, the natural 1+1D radial measure and "
            "product order have distinct non-labelled poset laws."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cells", type=int, default=DEFAULT_CELLS)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.cells < 2:
        parser.error("cells must be >= 2")
    result = run(args.cells)
    payload = json.dumps(result, indent=2) + "\n"
    print(payload, end="")
    if args.output is not None:
        args.output.write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    main()
