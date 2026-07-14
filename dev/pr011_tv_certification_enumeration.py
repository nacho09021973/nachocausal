"""PR011 TV certification enumeration scaffold — dev pre-flight only.

Computes unlabeled poset laws P_n(tau) on the frozen diamond family via exact
permutation enumeration (Lemma 1 / null-box copula reduction).  Emits no viability
terminal and writes no ``data/reports/pr011_*`` artifacts until G2b + user execution
authorization.

Falsifier probe (comité 022 §5): at n=4, tau0=0.95, tau1=1.05, check TV=0 vs TV>0.

Run:
  python3 dev/pr011_tv_certification_enumeration.py falsifier
  python3 dev/pr011_tv_certification_enumeration.py probe --n 4 --grid-m 20
"""

from __future__ import annotations

import argparse
import math
import sys
from decimal import ROUND_UP, Decimal
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations, permutations
from pathlib import Path
from typing import Callable, Mapping, Sequence

import numpy as np


_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent
_WP4 = _ROOT / "research_program" / "work_packages"
sys.path.insert(0, str(_WP4))

from wp4_kappa_numeric_reference import make_builder  # noqa: E402


# Frozen anchor — shape A moderate (pr011_mass_distinguishability_viability.md §3.1–3.2)
R_P, V_P = 2.0, 0.0
R_Q, V_Q = 0.5, 1.0
TAU_FAMILY = (0.8, 1.2)
TAU_PAIR = (0.95, 1.05)
N_LADDER = (4, 5, 6, 7, 8)
DEFAULT_GRID_M = 20
TV_ROUND_UP = 1e-12
RAW_MASS_SUM_MIN = 0.25
ORDER_FACTORIAL_CACHE: dict[int, int] = {}


@dataclass(frozen=True)
class EnumerationResult:
    n: int
    grid_m: int
    tau_a: float
    tau_b: float
    raw_mass_sum_a: float
    raw_mass_sum_b: float
    mass_sum_a: float
    mass_sum_b: float
    tv: float
    tv_certified_upper: float
    n_poset_classes: int


def factorial(n: int) -> int:
    if n not in ORDER_FACTORIAL_CACHE:
        ORDER_FACTORIAL_CACHE[n] = math.factorial(n)
    return ORDER_FACTORIAL_CACHE[n]


def build_diamond_family(tau: float):
    build_family, copula_density = make_builder(R_P, R_Q, V_P, V_Q)
    return build_family(tau), copula_density


def copula_grid(
    copula_density: Callable[[object, float, float], float],
    family,
    grid_m: int,
) -> np.ndarray:
    xs = (np.arange(grid_m) + 0.5) / grid_m
    grid = np.empty((grid_m, grid_m), dtype=float)
    for i, x in enumerate(xs):
        for j, y in enumerate(xs):
            grid[i, j] = copula_density(family, float(x), float(y))
    return grid


def poset_signature_from_permutation(sigma: Sequence[int]) -> frozenset[tuple[int, int]]:
    n = len(sigma)
    return frozenset(
        (i, j) for i in range(n) for j in range(i + 1, n) if sigma[i] < sigma[j]
    )


def permutation_mass(
    grid: np.ndarray,
    sigma: Sequence[int],
    ordered_indices: np.ndarray,
) -> float:
    n = len(sigma)
    grid_m = grid.shape[0]
    cell = factorial(n) * (1.0 / grid_m) ** (2 * n)
    accumulator = np.ones((len(ordered_indices), len(ordered_indices)), dtype=float)
    for rank in range(n):
        accumulator *= grid[
            ordered_indices[:, rank][:, None],
            ordered_indices[:, sigma[rank] - 1][None, :],
        ]
    return float(accumulator.sum() * cell)


def poset_law_from_grid(grid: np.ndarray, n: int) -> dict[frozenset[tuple[int, int]], float]:
    grid_m = grid.shape[0]
    if n > grid_m:
        raise ValueError(f"grid_m={grid_m} must be >= n={n}")
    ordered_indices = np.array(list(combinations(range(grid_m), n)), dtype=int)
    masses: dict[frozenset[tuple[int, int]], float] = defaultdict(float)
    for sigma in permutations(range(1, n + 1)):
        signature = poset_signature_from_permutation(sigma)
        masses[signature] += permutation_mass(grid, sigma, ordered_indices)
    return dict(masses)


def total_variation(
    law_a: Mapping[frozenset[tuple[int, int]], float],
    law_b: Mapping[frozenset[tuple[int, int]], float],
) -> float:
    keys = set(law_a) | set(law_b)
    return 0.5 * sum(abs(law_a.get(key, 0.0) - law_b.get(key, 0.0)) for key in keys)


def certified_tv_upper(tv: float) -> float:
    if tv <= 0.0:
        return 0.0
    step = Decimal(str(TV_ROUND_UP))
    scaled = Decimal(str(tv)) / step
    return float(scaled.to_integral_value(rounding=ROUND_UP) * step)


def normalize_law(
    masses: Mapping[frozenset[tuple[int, int]], float],
) -> tuple[dict[frozenset[tuple[int, int]], float], float]:
    raw_sum = sum(masses.values())
    if raw_sum <= 0.0:
        raise RuntimeError("poset law quadrature sum is non-positive")
    return {key: value / raw_sum for key, value in masses.items()}, raw_sum


def enumerate_tv(
    n: int,
    tau_a: float,
    tau_b: float,
    grid_m: int = DEFAULT_GRID_M,
) -> EnumerationResult:
    fam_a, copula_a = build_diamond_family(tau_a)
    fam_b, copula_b = build_diamond_family(tau_b)
    grid_a = copula_grid(copula_a, fam_a, grid_m)
    grid_b = copula_grid(copula_b, fam_b, grid_m)
    raw_law_a = poset_law_from_grid(grid_a, n)
    raw_law_b = poset_law_from_grid(grid_b, n)
    law_a, raw_mass_sum_a = normalize_law(raw_law_a)
    law_b, raw_mass_sum_b = normalize_law(raw_law_b)
    if raw_mass_sum_a < RAW_MASS_SUM_MIN or raw_mass_sum_b < RAW_MASS_SUM_MIN:
        raise RuntimeError(
            "quadrature under-coverage: increase grid_m before certification "
            f"(raw sums={raw_mass_sum_a:.8f}, {raw_mass_sum_b:.8f})"
        )
    tv = total_variation(law_a, law_b)
    return EnumerationResult(
        n=n,
        grid_m=grid_m,
        tau_a=tau_a,
        tau_b=tau_b,
        raw_mass_sum_a=raw_mass_sum_a,
        raw_mass_sum_b=raw_mass_sum_b,
        mass_sum_a=sum(law_a.values()),
        mass_sum_b=sum(law_b.values()),
        tv=tv,
        tv_certified_upper=certified_tv_upper(tv),
        n_poset_classes=len(set(law_a) | set(law_b)),
    )


def run_falsifier(grid_m: int = DEFAULT_GRID_M) -> EnumerationResult:
    return enumerate_tv(4, TAU_PAIR[0], TAU_PAIR[1], grid_m=grid_m)


def falsifier_verdict(result: EnumerationResult) -> str:
    if result.tv_certified_upper <= 0.0:
        return "PAIR_INDISTINGUISHABLE_TV_ZERO"
    return "PAIR_DISTINGUISHABLE_TV_POSITIVE"


def _print_result(result: EnumerationResult, *, label: str) -> None:
    print(f"PR011_ENUM_{label}=OK")
    print(f"n={result.n} grid_m={result.grid_m}")
    print(f"tau_pair=({result.tau_a}, {result.tau_b})")
    print(
        f"raw_mass_sum=({result.raw_mass_sum_a:.12f}, {result.raw_mass_sum_b:.12f})"
    )
    print(f"mass_sum=({result.mass_sum_a:.12f}, {result.mass_sum_b:.12f})")
    print(f"n_poset_classes={result.n_poset_classes}")
    print(f"TV={result.tv:.15f}")
    print(f"TV_certified_upper={result.tv_certified_upper:.12f}")
    print(f"falsifier_verdict={falsifier_verdict(result)}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    falsifier = sub.add_parser("falsifier", help="n=4 TV probe at frozen certification pair")
    falsifier.add_argument(
        "--grid-m",
        type=int,
        default=DEFAULT_GRID_M,
        help="unit-square copula quadrature resolution (default: %(default)s)",
    )

    probe = sub.add_parser("probe", help="deterministic TV probe (no terminal, no reports)")
    probe.add_argument("--n", type=int, required=True, choices=N_LADDER)
    probe.add_argument("--tau-a", type=float, default=TAU_PAIR[0])
    probe.add_argument("--tau-b", type=float, default=TAU_PAIR[1])
    probe.add_argument("--grid-m", type=int, default=DEFAULT_GRID_M)

    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.command == "falsifier":
        result = run_falsifier(grid_m=args.grid_m)
        _print_result(result, label="FALSIFIER")
        return 0

    result = enumerate_tv(args.n, args.tau_a, args.tau_b, grid_m=args.grid_m)
    _print_result(result, label="PROBE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())