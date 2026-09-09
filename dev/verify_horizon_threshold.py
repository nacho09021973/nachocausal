"""Deterministic checks for PAPER2_HORIZON_THRESHOLD_LIMIT.md.

Run from the repository root: python3 dev/verify_horizon_threshold.py
Requires the already available numpy and sympy. Missing dependencies fail.
No sprinkling, statistical fit, validation seeds, or generated result files.
Finite checks are falsifiers; the analytic proofs are in the companion note.
"""

from __future__ import annotations

import itertools
import math
import sys
from pathlib import Path

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nachocausal.generator import past_matrix_fast  # noqa: E402


def check_symbolic() -> None:
    v, r, rs = sp.symbols("v r r_S", positive=True)
    t, dt, dr = sp.symbols("t dt dr", real=True)
    z = (1 - r / rs) * sp.exp(r / rs - v / (2 * rs))
    q = rs**2 / r * sp.exp(-r / rs + v / (2 * rs))
    z_tr = z.subs(v, t + r)
    jac = sp.Matrix([[1, 1], [sp.diff(z_tr, t), sp.diff(z_tr, r)]]).det()
    f = 1 - rs / r
    metric = f * dt**2 - 2 * (1 - f) * dt * dr + (f - 2) * dr**2
    pullback = 2 * q.subs(v, t + r) * (dt + dr) * (
        sp.diff(z_tr, t) * dt + sp.diff(z_tr, r) * dr
    )
    checks = {
        "radial derivative": sp.diff(z, r) + 1 / q,
        "ingoing derivative": sp.diff(z, v) + z / (2 * rs),
        "volume Jacobian": jac + 1 / q.subs(v, t + r),
        "metric pullback": pullback - metric,
        "horizon coordinate": z.subs(r, rs),
        "horizon density": q.subs(r, rs) - rs * sp.exp(-1 + v / (2 * rs)),
    }
    for name, residual in checks.items():
        assert sp.simplify(residual) == 0, name
    print(f"PASS symbolic identities: {len(checks)}")


def check_generator() -> None:
    comparisons = 0
    for rs in (0.5, 2.0):
        # Non-random grid, including both sides down to relative distance 1e-9.
        radii = rs * np.array([0.1, 0.4, 0.8, 1 - 1e-6, 1 - 1e-9,
                              1 + 1e-9, 1 + 1e-6, 1.2, 2.6])
        times = rs * np.array([-3.14159, -1.23456, 0.0, 0.71357, 2.34567, 7.89123])
        points = np.array(list(itertools.product(times, radii)))
        v = points[:, 0] + points[:, 1]
        z = (rs - points[:, 1]) / rs * np.exp(
            points[:, 1] / rs - v / (2 * rs)
        )
        product = (v[:, None] >= v[None, :]) & (z[:, None] >= z[None, :])
        np.fill_diagonal(product, False)
        frozen = past_matrix_fast(points, "BH", rs)
        assert np.array_equal(product, frozen), f"generator mismatch at r_S={rs}"
        comparisons += points.shape[0] ** 2
        # Exact binary ingoing-null equality across the horizon.
        null_pair = np.array([[0.0, 1.25 * rs], [0.5 * rs, 0.75 * rs]])
        null_v = null_pair[:, 0] + null_pair[:, 1]
        null_z = (rs - null_pair[:, 1]) / rs * np.exp(
            null_pair[:, 1] / rs - null_v / (2 * rs)
        )
        assert null_v[0] == null_v[1] and null_z[0] < null_z[1]
        null_product = (null_v[:, None] >= null_v[None, :]) & (
            null_z[:, None] >= null_z[None, :]
        )
        np.fill_diagonal(null_product, False)
        assert np.array_equal(null_product, past_matrix_fast(null_pair, "BH", rs))
        assert null_product[1, 0] and not null_product[0, 1]
    print(f"PASS regular chart vs frozen generator: {comparisons} ordered pairs; 2 null ties")


def check_finite_identity() -> None:
    # Every subset of a 3 x 3 product-order grid, with v ties and both blocks.
    points = list(itertools.product((-1, 0, 1), (-2, -1, 1)))
    n = len(points)
    ext = sum(1 << j for j, (_, z) in enumerate(points) if z < 0)
    full = (1 << n) - 1
    interior = full ^ ext

    def precedes(j: int, k: int) -> bool:
        return j != k and all(a <= b for a, b in zip(points[j], points[k]))

    chain = [True] * (1 << n)
    for mask in range(1 << n):
        members = [j for j in range(n) if mask & (1 << j)]
        chain[mask] = all(precedes(j, k) or precedes(k, j)
                          for j, k in itertools.combinations(members, 2))
    # Brute-force heights, independent of threshold/anchored dynamic programming.
    height = [0] * (1 << n)
    cross_height = [0] * (1 << n)
    for mask in range(1 << n):
        sub = mask
        while sub:
            if chain[sub]:
                height[mask] = max(height[mask], sub.bit_count())
                if sub & ext and sub & interior:
                    cross_height[mask] = max(cross_height[mask], sub.bit_count())
            sub = (sub - 1) & mask

    for mask in range(1 << n):
        pair_max = 0
        for e in range(n):
            if not (mask & ext & (1 << e)):
                continue
            past = sum(1 << j for j in range(n)
                       if mask & ext & (1 << j) and (j == e or precedes(j, e)))
            for i in range(n):
                if not (mask & interior & (1 << i)) or not precedes(e, i):
                    continue
                future = sum(1 << j for j in range(n)
                             if mask & interior & (1 << j) and (j == i or precedes(i, j)))
                pair_max = max(pair_max, height[past] + height[future])
        # Event thresholds plus endpoints outside the data range for pure chains.
        unrestricted = restricted = 0
        for s in (-2, -1, 0, 1, 2):
            left = sum(1 << j for j, (v, _) in enumerate(points)
                       if mask & ext & (1 << j) and v <= s)
            right = sum(1 << j for j, (v, _) in enumerate(points)
                        if mask & interior & (1 << j) and v >= s)
            score = height[left] + height[right]
            unrestricted = max(unrestricted, score)
            if left and right:
                restricted = max(restricted, score)
        assert pair_max == restricted == cross_height[mask], mask
        assert unrestricted == height[mask], mask

    # Explicit empty-side trap: both blocks present but no compatible pair.
    ext_late = points.index((1, -1))
    int_early = points.index((-1, 1))
    mask = (1 << ext_late) | (1 << int_early)
    assert height[mask] == 1 and cross_height[mask] == 0
    print(f"PASS finite identities: {1 << n} induced posets, including empty-side trap")


def check_mesh_bound() -> None:
    # All nondecreasing integer triples in a bounded range, including jumps.
    triples = list(itertools.combinations_with_replacement(range(-2, 3), 3))
    for f in triples:
        for g in triples:
            eta = max(abs(f[0] - g[0]), abs(f[2] - g[2]))
            omega = g[2] - g[0]
            assert abs(f[1] - g[1]) <= eta + omega
    # First-moment factorial inequality used for collar heights (finite check only).
    for k in range(1, 101):
        assert math.lgamma(k + 1) >= k * (math.log(k) - 1)
    print(f"PASS mesh bound: {len(triples) ** 2} monotone pairs; factorial checks k=1..100")


if __name__ == "__main__":
    check_symbolic()
    check_generator()
    check_finite_identity()
    check_mesh_bound()
    print("PASS: deterministic checks only; no asymptotic or order-only detection claim")
