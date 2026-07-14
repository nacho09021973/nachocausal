"""PR011 TV certification — enumeration + Hellinger fallback (frozen §6.1).

Computes unlabeled poset laws P_n(tau) on the frozen diamond family (Lemma 1 / copula
reduction).  Certification routes (preferred order, spec §6):

1. Primary grid enumeration with convergence audit (raw mass + TV delta).
2. Fallback: copula Hellinger → TV upper bound via Le Cam + n-fold data processing.

Run:
  python3 dev/pr011_tv_certification_enumeration.py falsifier
  python3 dev/pr011_tv_certification_enumeration.py probe --n 4 --grid-m 20
  python3 dev/pr011_tv_certification_enumeration.py certify --n 4
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import math
import sys
from collections import defaultdict
from dataclasses import dataclass
from decimal import ROUND_UP, Decimal
from itertools import combinations, permutations
from pathlib import Path
from typing import Callable, Mapping, Sequence

import numpy as np


_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent
_WP4 = _ROOT / "research_program" / "work_packages"
sys.path.insert(0, str(_WP4))

from wp4_kappa_numeric_reference import hellinger_sq, make_builder  # noqa: E402


# Frozen anchor — shape A moderate (pr011_mass_distinguishability_viability.md §3.1–3.2)
R_P, V_P = 2.0, 0.0
R_Q, V_Q = 0.5, 1.0
TAU_FAMILY = (0.8, 1.2)
TAU_PAIR = (0.95, 1.05)
N_LADDER = (4, 5, 6, 7, 8)
DEFAULT_GRID_M = 20
NOMINAL_CROSSCHECK_GRID_M = 12


def nominal_annotation_grid_m(n: int) -> int:
    if n <= 4:
        return NOMINAL_CROSSCHECK_GRID_M
    return n + 3
TV_ROUND_UP = 1e-12
RAW_MASS_SUM_MIN = 0.25
RAW_MASS_SUM_TARGET = 0.99
TV_CONVERGENCE_TOL = 1e-12
PRIMARY_GRID_LADDER = (20, 24, 28, 32)
PRIMARY_CERTIFY_PROBE = (24,)
HELLINGER_M = 100
HELLINGER_CROSSCHECK_M = 72
HELLINGER_H2_REL_TOL = 1e-3
TERMINAL_DISTINGUISHABLE = "PAIR_DISTINGUISHABLE_AT_TRACTABLE_N"
TERMINAL_INDISTINGUISHABLE = "PAIR_INDISTINGUISHABLE_TV_ZERO"
TERMINAL_INCOMPLETE = "CERTIFICATION_INCOMPLETE"
ORDER_FACTORIAL_CACHE: dict[int, int] = {}

REPORT_DIR = _ROOT / "data" / "reports"
CERTIFIABLE_N = (4, 5, 6, 7, 8)
CERT_CSV_FIELDS = (
    "method",
    "n",
    "tau_a",
    "tau_b",
    "epsilon_certified_upper",
    "terminal",
    "hellinger_M",
    "hellinger_H2",
    "hellinger_H2_crosscheck",
    "primary_grid_m",
    "primary_tv_nominal",
    "primary_raw_mass_sum",
)


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


@dataclass(frozen=True)
class CertificationResult:
    method: str
    n: int
    tau_a: float
    tau_b: float
    epsilon_certified_upper: float
    terminal: str
    hellinger_M: int | None
    hellinger_H2: float | None
    hellinger_H2_crosscheck: float | None
    primary_grid_m: int | None
    primary_tv_nominal: float | None
    primary_raw_mass_sum: float | None


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
    *,
    require_coverage: bool = True,
) -> EnumerationResult:
    fam_a, copula_a = build_diamond_family(tau_a)
    fam_b, copula_b = build_diamond_family(tau_b)
    grid_a = copula_grid(copula_a, fam_a, grid_m)
    grid_b = copula_grid(copula_b, fam_b, grid_m)
    raw_law_a = poset_law_from_grid(grid_a, n)
    raw_law_b = poset_law_from_grid(grid_b, n)
    law_a, raw_mass_sum_a = normalize_law(raw_law_a)
    law_b, raw_mass_sum_b = normalize_law(raw_law_b)
    if require_coverage and (
        raw_mass_sum_a < RAW_MASS_SUM_MIN or raw_mass_sum_b < RAW_MASS_SUM_MIN
    ):
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


def copula_tv_upper_from_hellinger_sq(h2: float) -> float:
    if h2 < 0.0 or h2 > 2.0:
        raise ValueError(f"Hellinger squared out of range: {h2}")
    if h2 <= 0.0:
        return 0.0
    return math.sqrt(h2) * math.sqrt(1.0 - h2 / 4.0)


def copula_hellinger_sq(tau_a: float, tau_b: float, grid_m: int) -> float:
    fam_a, copula_a = build_diamond_family(tau_a)
    fam_b, _ = build_diamond_family(tau_b)
    return float(hellinger_sq(copula_a, fam_a, fam_b, M=grid_m))


def poset_tv_upper_via_hellinger(
    tau_a: float,
    tau_b: float,
    n: int,
    grid_m: int = HELLINGER_M,
) -> tuple[float, float]:
    """Upper bound on TV(P_n poset) via Lemma 1 data processing + n-fold product bound."""
    h2 = copula_hellinger_sq(tau_a, tau_b, grid_m)
    copula_tv = copula_tv_upper_from_hellinger_sq(h2)
    return certified_tv_upper(n * copula_tv), h2


def verify_hellinger_stability(
    tau_a: float,
    tau_b: float,
    grid_m: int = HELLINGER_M,
    crosscheck_m: int = HELLINGER_CROSSCHECK_M,
) -> tuple[float, float]:
    h2_coarse = copula_hellinger_sq(tau_a, tau_b, grid_m)
    h2_fine = copula_hellinger_sq(tau_a, tau_b, crosscheck_m)
    if h2_fine <= 0.0:
        raise RuntimeError("Hellinger cross-check denominator is non-positive")
    rel_gap = abs(h2_coarse - h2_fine) / h2_fine
    if rel_gap > HELLINGER_H2_REL_TOL:
        raise RuntimeError(
            f"Hellinger grid instability: rel_gap={rel_gap:.6e} > {HELLINGER_H2_REL_TOL}"
        )
    return h2_coarse, h2_fine


def try_primary_convergence(
    n: int,
    tau_a: float,
    tau_b: float,
    grid_ladder: Sequence[int] = PRIMARY_GRID_LADDER,
) -> EnumerationResult | None:
    if not grid_ladder:
        return None
    previous: EnumerationResult | None = None
    for grid_m in grid_ladder:
        current = enumerate_tv(n, tau_a, tau_b, grid_m=grid_m)
        raw_ok = (
            current.raw_mass_sum_a >= RAW_MASS_SUM_TARGET
            and current.raw_mass_sum_b >= RAW_MASS_SUM_TARGET
        )
        if previous is not None and raw_ok:
            delta = abs(current.tv - previous.tv)
            if delta <= TV_CONVERGENCE_TOL:
                return current
        previous = current
    return None


def certification_artifact_paths(n: int) -> tuple[Path, Path]:
    if n not in CERTIFIABLE_N:
        raise ValueError(f"n={n} is outside certifiable ladder {CERTIFIABLE_N}")
    csv_path = REPORT_DIR / f"pr011_tv_certification_n{n}.csv"
    sidecar_path = REPORT_DIR / f"pr011_tv_certification_n{n}.sha256"
    return csv_path, sidecar_path


def terminal_for_epsilon(epsilon: float) -> str:
    """§8 terminal precedence. `epsilon<=0.0` (TV=0, a valid negative result) must be checked
    before `epsilon<1.0`, which it would otherwise also satisfy, leaving
    `TERMINAL_INDISTINGUISHABLE` unreachable (auditor_report_011)."""
    if epsilon <= 0.0:
        return TERMINAL_INDISTINGUISHABLE
    if epsilon < 1.0:
        return TERMINAL_DISTINGUISHABLE
    return TERMINAL_INCOMPLETE


def certify(
    n: int,
    tau_a: float = TAU_PAIR[0],
    tau_b: float = TAU_PAIR[1],
) -> CertificationResult:
    if n not in CERTIFIABLE_N:
        raise ValueError(f"n={n} is outside certifiable ladder {CERTIFIABLE_N}")
    primary_probe = PRIMARY_CERTIFY_PROBE if n <= 4 else ()
    primary = try_primary_convergence(n, tau_a, tau_b, primary_probe)
    if primary is not None:
        epsilon = primary.tv_certified_upper
        terminal = terminal_for_epsilon(epsilon)
        return CertificationResult(
            method="PRIMARY_ENUMERATION",
            n=n,
            tau_a=tau_a,
            tau_b=tau_b,
            epsilon_certified_upper=epsilon,
            terminal=terminal,
            hellinger_M=None,
            hellinger_H2=None,
            hellinger_H2_crosscheck=None,
            primary_grid_m=primary.grid_m,
            primary_tv_nominal=primary.tv,
            primary_raw_mass_sum=min(primary.raw_mass_sum_a, primary.raw_mass_sum_b),
        )

    h2, h2_x = verify_hellinger_stability(tau_a, tau_b)
    epsilon, _ = poset_tv_upper_via_hellinger(tau_a, tau_b, n, HELLINGER_M)
    annotation_m = nominal_annotation_grid_m(n)
    nominal = enumerate_tv(
        n,
        tau_a,
        tau_b,
        grid_m=annotation_m,
        require_coverage=False,
    )
    terminal = terminal_for_epsilon(epsilon)
    return CertificationResult(
        method="HELLINGER_FALLBACK",
        n=n,
        tau_a=tau_a,
        tau_b=tau_b,
        epsilon_certified_upper=epsilon,
        terminal=terminal,
        hellinger_M=HELLINGER_M,
        hellinger_H2=h2,
        hellinger_H2_crosscheck=h2_x,
        primary_grid_m=annotation_m,
        primary_tv_nominal=nominal.tv,
        primary_raw_mass_sum=min(nominal.raw_mass_sum_a, nominal.raw_mass_sum_b),
    )


def run_falsifier(grid_m: int = DEFAULT_GRID_M) -> EnumerationResult:
    return enumerate_tv(4, TAU_PAIR[0], TAU_PAIR[1], grid_m=grid_m)


def falsifier_verdict(result: EnumerationResult) -> str:
    if result.tv_certified_upper <= 0.0:
        return "PAIR_INDISTINGUISHABLE_TV_ZERO"
    return "PAIR_DISTINGUISHABLE_TV_POSITIVE"


def _field_value(result: CertificationResult, field: str) -> str:
    value = getattr(result, field)
    if value is None:
        return ""
    if isinstance(value, float):
        return repr(value)
    return str(value)


def render_certification_csv(result: CertificationResult) -> bytes:
    row = {field: _field_value(result, field) for field in CERT_CSV_FIELDS}
    lines = [",".join(CERT_CSV_FIELDS)]
    lines.append(",".join(row[field] for field in CERT_CSV_FIELDS))
    return ("\n".join(lines) + "\n").encode("utf-8")


def publish_certification(result: CertificationResult) -> None:
    csv_path, sidecar_path = certification_artifact_paths(result.n)
    if csv_path.exists() or sidecar_path.exists():
        raise RuntimeError(
            f"refusing to overwrite existing pr011 certification artifact for n={result.n}"
        )
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    csv_data = render_certification_csv(result)
    csv_path.write_bytes(csv_data)
    digest = hashlib.sha256(csv_data).hexdigest()
    sidecar_path.write_bytes(f"{digest}  {csv_path.name}\n".encode("ascii"))


def _print_enumeration(result: EnumerationResult, *, label: str) -> None:
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


def _print_certification(result: CertificationResult) -> None:
    print("PR011_CERTIFICATION=OK")
    print(f"method={result.method}")
    print(f"n={result.n} tau_pair=({result.tau_a}, {result.tau_b})")
    print(f"epsilon_certified_upper={result.epsilon_certified_upper:.12f}")
    print(f"PR011_VIABILITY_TERMINAL={result.terminal}")
    if result.hellinger_M is not None:
        print(f"hellinger_M={result.hellinger_M} H2={result.hellinger_H2:.12e}")
        print(f"hellinger_H2_crosscheck={result.hellinger_H2_crosscheck:.12e}")
    if result.primary_tv_nominal is not None:
        print(
            f"primary_nominal_tv={result.primary_tv_nominal:.15f} "
            f"grid_m={result.primary_grid_m} raw_mass_sum={result.primary_raw_mass_sum:.6f}"
        )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    falsifier = sub.add_parser("falsifier", help="n=4 TV probe at frozen certification pair")
    falsifier.add_argument("--grid-m", type=int, default=DEFAULT_GRID_M)

    probe = sub.add_parser("probe", help="deterministic TV probe (no terminal, no reports)")
    probe.add_argument("--n", type=int, required=True, choices=N_LADDER)
    probe.add_argument("--tau-a", type=float, default=TAU_PAIR[0])
    probe.add_argument("--tau-b", type=float, default=TAU_PAIR[1])
    probe.add_argument("--grid-m", type=int, default=DEFAULT_GRID_M)

    certify_cmd = sub.add_parser(
        "certify",
        help="tier-1 certification at n (writes data/reports/pr011_tv_certification_nN.*)",
    )
    certify_cmd.add_argument("--n", type=int, default=4, choices=CERTIFIABLE_N)
    certify_cmd.add_argument("--tau-a", type=float, default=TAU_PAIR[0])
    certify_cmd.add_argument("--tau-b", type=float, default=TAU_PAIR[1])
    certify_cmd.add_argument(
        "--dry-run",
        action="store_true",
        help="compute and print without writing artifacts",
    )

    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.command == "falsifier":
        _print_enumeration(run_falsifier(grid_m=args.grid_m), label="FALSIFIER")
        return 0

    if args.command == "probe":
        _print_enumeration(
            enumerate_tv(args.n, args.tau_a, args.tau_b, grid_m=args.grid_m),
            label="PROBE",
        )
        return 0

    result = certify(args.n, args.tau_a, args.tau_b)
    if not args.dry_run:
        publish_certification(result)
    _print_certification(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())