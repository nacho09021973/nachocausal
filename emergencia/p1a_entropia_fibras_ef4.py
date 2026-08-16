#!/usr/bin/env python3
"""EF-4 deterministic checks for the prescribed-family certificate in d=2.

The proof in ``docs/hoja_de_ruta_agosto_2026.md`` is asymptotic and deductive.
This module checks its integer construction, exact balance, analytic rival bounds,
and representative finite-n margins.  It performs no random sampling, enumerates
no permutations, and writes no artifacts.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class CertificateBounds:
    n: int
    rho: int
    prescribed_count: int
    free_count: int
    planted_prescribed_per_side: int
    discrepancy_radius: float
    discrepancy_failure_bound: float
    small_product_threshold: float
    loss_gap: float
    small_product_gap: float

    @property
    def well_defined(self) -> bool:
        return self.rho < self.n // 4 and self.free_count > 0

    @property
    def uniqueness_margin_positive(self) -> bool:
        return (
            self.well_defined
            and self.loss_gap > 2.0 * self.discrepancy_radius
            and self.small_product_gap > 2.0 * self.discrepancy_radius
            and self.discrepancy_failure_bound < 1.0
        )


def rho_for_n(n: int) -> int:
    """Return the fixed EF-4 staircase width ceil((n^2 log n)^(1/3))."""

    if n < 2:
        raise ValueError("n must be at least 2")
    return math.ceil((n * n * math.log(n)) ** (1.0 / 3.0))


def append_incomparable(permutation: Sequence[int]) -> tuple[int, ...]:
    """Embed a zero-based permutation and append the incomparable point (n, 0)."""

    values = tuple(int(value) for value in permutation)
    if sorted(values) != list(range(len(values))):
        raise ValueError("expected a permutation of range(n)")
    return tuple(value + 1 for value in values) + (0,)


def build_even_prescription(n: int, rho: int | None = None) -> dict[int, int]:
    """Build the 1-based partial permutation prescribed in EF-4.1."""

    if n < 8 or n % 2:
        raise ValueError("the prescribed family requires an even n >= 8")
    width = rho_for_n(n) if rho is None else int(rho)
    if width < 1 or width >= n // 4:
        raise ValueError("rho must satisfy 1 <= rho < floor(n/4)")

    half = n // 2
    first_quartile = n // 4
    third_quartile = (3 * n) // 4
    prescribed = {1: 1, half: half, half + 1: half + 1, n: n}
    for offset in range(1, width):
        prescribed[half - width + offset] = first_quartile + offset
        prescribed[half + 1 + offset] = third_quartile + offset

    expected = 2 * width + 2
    if len(prescribed) != expected or len(set(prescribed.values())) != expected:
        raise RuntimeError("prescribed rows or columns collide")
    if any(not 1 <= row <= n or not 1 <= column <= n for row, column in prescribed.items()):
        raise RuntimeError("prescription leaves the permutation square")
    return prescribed


def validate_even_balance(n: int, rho: int | None = None) -> bool:
    """Check that exactly half the residual rows and columns lie on each side."""

    prescribed = build_even_prescription(n, rho)
    half = n // 2
    lower_rows = sum(row <= half for row in prescribed)
    lower_columns = sum(column <= half for column in prescribed.values())
    expected = len(prescribed) // 2
    return lower_rows == lower_columns == expected


def loss_case_mean_upper(free_count: int, planted_prescribed: int) -> float:
    """Maximum rival primary mean in EF-4.4's staircase-loss case."""

    if free_count <= 0 or planted_prescribed < 3:
        raise ValueError("invalid loss-case parameters")
    offset = planted_prescribed - 2
    return (
        free_count / 4.0
        + planted_prescribed / 2.0
        + 2.0
        + offset * offset / (4.0 * free_count)
    )


def loss_case_objective(
    free_count: int, planted_prescribed: int, free_product: float
) -> float:
    """Upper envelope before optimizing over the losing block's free product."""

    if not 0.0 <= free_product <= 1.0:
        raise ValueError("free_product must lie in [0,1]")
    other_product = (1.0 - math.sqrt(free_product)) ** 2
    return min(
        3.0 + free_count * free_product,
        planted_prescribed + 1.0 + free_count * other_product,
    )


def certificate_bounds(n: int) -> CertificateBounds:
    """Evaluate the explicit EF-4 finite-n margins for an even size."""

    if n < 8 or n % 2:
        raise ValueError("certificate bounds require an even n >= 8")
    rho = rho_for_n(n)
    prescribed_count = 2 * rho + 2
    free_count = n - prescribed_count
    if free_count <= 0:
        raise ValueError("the asymptotic prescription is not defined at this n")
    planted_prescribed = rho + 1
    discrepancy_radius = math.sqrt(3.0 * free_count * math.log(n))
    discrepancy_failure_bound = min(1.0, 2.0 / (n * n))
    small_product_threshold = 1.0 / 8.0 + rho / free_count

    planted_mean = free_count / 4.0 + planted_prescribed
    loss_gap = planted_mean - loss_case_mean_upper(
        free_count, planted_prescribed
    )
    small_product_gap = (
        planted_mean
        - (2.0 * planted_prescribed + free_count * small_product_threshold)
    )
    return CertificateBounds(
        n=n,
        rho=rho,
        prescribed_count=prescribed_count,
        free_count=free_count,
        planted_prescribed_per_side=planted_prescribed,
        discrepancy_radius=discrepancy_radius,
        discrepancy_failure_bound=discrepancy_failure_bound,
        small_product_threshold=small_product_threshold,
        loss_gap=loss_gap,
        small_product_gap=small_product_gap,
    )


def validate_loss_optimization(bounds: CertificateBounds, grid_size: int = 100_000) -> bool:
    """Numerically falsify, but do not replace, the exact one-variable proof."""

    analytic = loss_case_mean_upper(
        bounds.free_count, bounds.planted_prescribed_per_side
    )
    for index in range(grid_size + 1):
        free_product = index / grid_size
        observed = loss_case_objective(
            bounds.free_count,
            bounds.planted_prescribed_per_side,
            free_product,
        )
        if observed > analytic + 1e-7:
            return False
    return True


def entropy_log_upper_bound(n: int) -> float:
    """Return log((n)_R) <= R log n for the prescribed event."""

    bounds = certificate_bounds(n)
    return bounds.prescribed_count * math.log(n)


def main() -> int:
    checkpoints = (100_000, 1_000_000, 10_000_000)
    for n in checkpoints:
        bounds = certificate_bounds(n)
        if not validate_even_balance(n):
            raise RuntimeError(f"prescribed balance failed at n={n}")
        if not validate_loss_optimization(bounds, grid_size=10_000):
            raise RuntimeError(f"loss optimization failed at n={n}")
        print(
            "EF4_CHECK "
            f"N={n} RHO={bounds.rho} FREE={bounds.free_count} "
            f"LOSS_GAP_OVER_2ETA={bounds.loss_gap / (2 * bounds.discrepancy_radius):.6g} "
            "SMALL_PRODUCT_GAP_OVER_2ETA="
            f"{bounds.small_product_gap / (2 * bounds.discrepancy_radius):.6g} "
            f"CERTIFICATE={'PASS' if bounds.uniqueness_margin_positive else 'PREASYMPTOTIC'}"
        )

    final_bounds = certificate_bounds(checkpoints[-1])
    if not final_bounds.uniqueness_margin_positive:
        raise RuntimeError("representative asymptotic certificate did not close")
    print("EF4_PRESCRIBED_ROWS_COLUMNS=PASS")
    print("EF4_RESIDUAL_HALF_BALANCE=PASS")
    print("EF4_LOSS_CASE_OPTIMIZATION=PASS")
    print("EF4_TERMINAL=FIBER_CONCENTRATION")
    print("EF4_MONTE_CARLO=NOT_RUN")
    print("EF4_GAUSS_KUZMIN=NOT_USED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
