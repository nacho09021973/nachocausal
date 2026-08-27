#!/usr/bin/env python3
"""Exact post-hoc thinning macrotest for the uniform permutation populations.

This runner consumes the frozen exact ``a_k,b_k`` coefficients for n=6,7,8,9.
It performs no Monte Carlo calculation and never replaces orbital uniqueness by
literal uniqueness.  Publication is explicit, atomic, and refuses to overwrite.

    PYTHONDONTWRITEBYTECODE=1 python -m emergencia.p1a_macrotest_exploratorio_d2
    PYTHONDONTWRITEBYTECODE=1 python -m emergencia.p1a_macrotest_exploratorio_d2 \
        --write-artifacts
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
from collections import defaultdict
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Sequence

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_qp_falsador_d2 as qp
from emergencia import p1a_tie_aut_diagnostic as tie_aut


PHASE = "POST_HOC_EXPLORATORY_MACROTEST"
EXACT_N = (6, 7, 8, 9)
MIN_SUPPORT = 6
P_GRID = (Fraction(0),) + tuple(Fraction(i, 20) for i in range(2, 21))

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = HERE / "resultados"
COEFFICIENT_PATH = DEFAULT_OUTPUT_DIR / "p1a_qp_coeficientes_d2.csv"
QP_SUMMARY_PATH = DEFAULT_OUTPUT_DIR / "p1a_qp_falsador_resumen.json"
TIE_AUT_PATH = DEFAULT_OUTPUT_DIR / "p1a_tie_aut_exacto_d2.json"

NP_FILENAME = "p1a_macrotest_exploratorio_n_p_d2.csv"
NK_FILENAME = "p1a_macrotest_exploratorio_n_k_d2.csv"
SUMMARY_FILENAME = "p1a_macrotest_exploratorio_resumen.json"

NP_FIELDS = (
    "PHASE",
    "n",
    "p",
    "deletion_fraction",
    "expected_retained",
    "relative_density",
    "U_orbital",
    "E_available",
    "U_orbital_given_available",
)
NK_FIELDS = (
    "PHASE",
    "n",
    "k_retained",
    "retained_fraction",
    "u_orbital_given_k",
    "e_available_given_k",
    "u_orbital_given_available_and_k",
)


@dataclass(frozen=True)
class ExactAnalysis:
    np_rows: tuple[dict[str, object], ...]
    nk_rows: tuple[dict[str, object], ...]
    np_exact: dict[tuple[int, Fraction], tuple[Fraction, Fraction, Fraction | None]]
    nk_exact: dict[tuple[int, int], tuple[Fraction, Fraction, Fraction | None]]
    baseline: dict[int, tuple[Fraction, Fraction, Fraction | None]]
    controls: dict[str, str]
    source_digests: dict[str, str]
    available_rows: dict[int, int]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _verify_sidecar(path: Path) -> str:
    sidecar = path.with_suffix(path.suffix + ".sha256")
    fields = sidecar.read_text(encoding="utf-8").strip().split()
    if len(fields) != 2 or fields[1] != path.name:
        raise RuntimeError(f"invalid SHA-256 sidecar for {path}")
    observed = _sha256(path)
    if observed != fields[0]:
        raise RuntimeError(f"SHA-256 mismatch for frozen source {path}")
    return observed


def _fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _decimal(value: Fraction) -> str:
    if value == 0:
        return "0"
    if value == 1:
        return "1"
    with localcontext() as context:
        context.prec = 25
        return format(Decimal(value.numerator) / Decimal(value.denominator), ".17g")


def _load_frozen_counts() -> tuple[dict[int, tuple[int, int]], dict[str, str], dict[int, int]]:
    source_digests = {
        COEFFICIENT_PATH.name: _verify_sidecar(COEFFICIENT_PATH),
        QP_SUMMARY_PATH.name: _verify_sidecar(QP_SUMMARY_PATH),
        TIE_AUT_PATH.name: _verify_sidecar(TIE_AUT_PATH),
    }
    qp_summary = json.loads(QP_SUMMARY_PATH.read_text(encoding="utf-8"))
    tie_summary = json.loads(TIE_AUT_PATH.read_text(encoding="utf-8"))
    if qp_summary["method"]["evaluation"] != "EXACT_MASK_SUM":
        raise RuntimeError("frozen q_p source is not exact mask summation")
    if qp_summary["method"]["monte_carlo"] is not False:
        raise RuntimeError("frozen q_p source unexpectedly uses Monte Carlo")

    available_rows = {
        int(report["n"]): int(report["available_permutations"])
        for report in qp_summary["reports"]
    }
    frozen: dict[int, tuple[int, int]] = {}
    for aggregate in tie_summary["aggregates"]:
        n = int(aggregate["n"])
        diagnostics = aggregate["diagnostic_state_counts"]
        optimized = aggregate["optimized_state_counts"]
        orbital = int(diagnostics.get(tie_aut.DIAGNOSTIC_UNIQUE, 0)) + int(
            diagnostics.get(tie_aut.DIAGNOSTIC_TIE_AUT_ONLY, 0)
        )
        available = int(aggregate["permutations"]) - int(optimized.get("EMPTY", 0))
        frozen[n] = (orbital, available)
    if tuple(sorted(frozen)) != EXACT_N:
        raise RuntimeError("frozen orbital artifact does not cover n=6,7,8,9")
    return frozen, source_digests, available_rows


def _aggregate_coefficients(
    expected_rows: dict[int, int],
) -> tuple[dict[int, list[int]], dict[int, list[int]], dict[int, int]]:
    sum_a = {n: [0] * (n + 1) for n in EXACT_N}
    sum_b = {n: [0] * (n + 1) for n in EXACT_N}
    observed_rows: defaultdict[int, int] = defaultdict(int)
    with COEFFICIENT_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            n = int(row["n"])
            if n not in EXACT_N:
                raise RuntimeError(f"unexpected n={n} in coefficient table")
            a = [int(value) for value in row["a_coefficients"].split("-")]
            b = [int(value) for value in row["b_coefficients"].split("-")]
            if len(a) != n + 1 or len(b) != n + 1:
                raise RuntimeError(f"coefficient length mismatch at n={n}")
            if any(a[k] or b[k] for k in range(MIN_SUPPORT)):
                raise RuntimeError(f"nonzero coefficient below K0 support at n={n}")
            if a[n] != int(row["r_orb"]):
                raise RuntimeError(f"top a coefficient is not r_orb at n={n}")
            if any(not 0 <= a[k] <= b[k] <= math.comb(n, k) for k in range(n + 1)):
                raise RuntimeError(f"coefficient bounds violated at n={n}")
            observed_rows[n] += 1
            for k in range(n + 1):
                sum_a[n][k] += a[k]
                sum_b[n][k] += b[k]
    if dict(observed_rows) != expected_rows:
        raise RuntimeError("coefficient rows do not reproduce frozen availability counts")
    return sum_a, sum_b, dict(observed_rows)


def _baseline_from_frozen(
    frozen: dict[int, tuple[int, int]],
) -> dict[int, tuple[Fraction, Fraction, Fraction | None]]:
    baseline: dict[int, tuple[Fraction, Fraction, Fraction | None]] = {}
    for k in range(10):
        if k < MIN_SUPPORT:
            u = e = Fraction(0)
        else:
            orbital, available = frozen[k]
            u = Fraction(orbital, math.factorial(k))
            e = Fraction(available, math.factorial(k))
        baseline[k] = (u, e, u / e if e else None)
    return baseline


def _nk_row(n: int, k: int, u: Fraction, e: Fraction) -> dict[str, object]:
    conditioned = u / e if e else None
    return {
        "PHASE": PHASE,
        "n": n,
        "k_retained": k,
        "retained_fraction": _decimal(Fraction(k, n)),
        "u_orbital_given_k": _decimal(u),
        "e_available_given_k": _decimal(e),
        "u_orbital_given_available_and_k": _decimal(conditioned) if conditioned is not None else "NA",
    }


def _np_row(n: int, p: Fraction, u: Fraction, e: Fraction) -> dict[str, object]:
    conditioned = u / e if e else None
    return {
        "PHASE": PHASE,
        "n": n,
        "p": f"{float(p):.2f}",
        "deletion_fraction": f"{float(1 - p):.2f}",
        "expected_retained": f"{float(n * p):.2f}",
        "relative_density": f"{float(p):.2f}",
        "U_orbital": _decimal(u),
        "E_available": _decimal(e),
        "U_orbital_given_available": _decimal(conditioned) if conditioned is not None else "NA",
    }


def analyze() -> ExactAnalysis:
    frozen, source_digests, expected_rows = _load_frozen_counts()
    sum_a, sum_b, observed_rows = _aggregate_coefficients(expected_rows)
    baseline = _baseline_from_frozen(frozen)

    p0_pass = True
    p1_pass = True
    support_pass = True
    polynomial_pass = True
    consistency_pass = True
    nk_rows: list[dict[str, object]] = []
    nk_exact: dict[tuple[int, int], tuple[Fraction, Fraction, Fraction | None]] = {}

    for n in EXACT_N:
        factorial = math.factorial(n)
        orbital_frozen, available_frozen = frozen[n]
        p1_pass &= sum_a[n][n] == orbital_frozen and sum_b[n][n] == available_frozen
        support_pass &= all(sum_a[n][k] == 0 and sum_b[n][k] == 0 for k in range(MIN_SUPPORT))
        for k in range(n + 1):
            denominator = factorial * math.comb(n, k)
            u = Fraction(sum_a[n][k], denominator)
            e = Fraction(sum_b[n][k], denominator)
            conditioned = u / e if e else None
            nk_exact[n, k] = (u, e, conditioned)
            nk_rows.append(_nk_row(n, k, u, e))
            consistency_pass &= (u, e) == baseline[k][:2]

    np_rows: list[dict[str, object]] = []
    np_exact: dict[tuple[int, Fraction], tuple[Fraction, Fraction, Fraction | None]] = {}
    for n in EXACT_N:
        factorial = math.factorial(n)
        for p in P_GRID:
            u_polynomial = qp.evaluate_bernstein(sum_a[n], n, p) / factorial
            e_polynomial = qp.evaluate_bernstein(sum_b[n], n, p) / factorial
            u_mixture = sum(
                Fraction(math.comb(n, k)) * p**k * (1 - p) ** (n - k) * nk_exact[n, k][0]
                for k in range(n + 1)
            )
            e_mixture = sum(
                Fraction(math.comb(n, k)) * p**k * (1 - p) ** (n - k) * nk_exact[n, k][1]
                for k in range(n + 1)
            )
            polynomial_pass &= u_polynomial == u_mixture and e_polynomial == e_mixture
            if p == 0:
                p0_pass &= u_polynomial == 0
            if p == 1:
                p1_pass &= (u_polynomial, e_polynomial) == baseline[n][:2]
            conditioned = u_polynomial / e_polynomial if e_polynomial else None
            np_exact[n, p] = (u_polynomial, e_polynomial, conditioned)
            np_rows.append(_np_row(n, p, u_polynomial, e_polynomial))

    controls = {
        "P0_ZERO": "PASS" if p0_pass else "FAIL",
        "P1_REPRODUCES_FROZEN": "PASS" if p1_pass else "FAIL",
        "K_LT_6_ZERO": "PASS" if support_pass else "FAIL",
        "POLYNOMIAL_EVALUATION": "PASS" if polynomial_pass else "FAIL",
        "EXACT_THINNING_CONSISTENCY": "PASS" if consistency_pass else "FAIL",
    }
    if any(value != "PASS" for value in controls.values()):
        raise RuntimeError(f"macrotest hard guard failed: {controls}")
    return ExactAnalysis(
        np_rows=tuple(np_rows),
        nk_rows=tuple(nk_rows),
        np_exact=np_exact,
        nk_exact=nk_exact,
        baseline=baseline,
        controls=controls,
        source_digests=source_digests,
        available_rows=observed_rows,
    )


def _exact_triplet(values: tuple[Fraction, Fraction, Fraction | None]) -> dict[str, str]:
    u, e, conditioned = values
    return {
        "U_orbital": _fraction_text(u),
        "E_available": _fraction_text(e),
        "U_orbital_given_available": _fraction_text(conditioned) if conditioned is not None else "NA",
    }


def _monotone_on_grid(
    analysis: ExactAnalysis, coordinate: int
) -> dict[int, str]:
    result: dict[int, str] = {}
    for n in EXACT_N:
        values = [analysis.np_exact[n, p][coordinate] for p in P_GRID]
        defined = [value for value in values if value is not None]
        increasing = all(left <= right for left, right in zip(defined, defined[1:]))
        decreasing = all(left >= right for left, right in zip(defined, defined[1:]))
        result[n] = "NONDECREASING" if increasing else "NONINCREASING" if decreasing else "NONMONOTONE"
    return result


def summary_payload(
    analysis: ExactAnalysis, np_digest: str, nk_digest: str
) -> dict[str, object]:
    return {
        "artifact_schema": "P1A_POST_HOC_EXPLORATORY_MACROTEST_D2_V1",
        "phase": PHASE,
        "result_status": "EXACT_MACROTEST_COMPLETED_LARGE_N_BLOCKED",
        "method": {
            "population": "uniform permutation in S_n",
            "evaluation": "EXACT_RATIONAL_BERNSTEIN_COEFFICIENT_AGGREGATION",
            "monte_carlo": False,
            "p_grid": [_fraction_text(p) for p in P_GRID],
            "empty_contributes_zero": True,
            "orbital_uniqueness_states": [
                tie_aut.DIAGNOSTIC_UNIQUE,
                tie_aut.DIAGNOSTIC_TIE_AUT_ONLY,
            ],
            "literal_STATE_UNIQUE_used_as_proxy": False,
        },
        "exact_identity": {
            "INDUCED_PATTERN_GIVEN_K_IS_UNIFORM_S_K": True,
            "EXACT_THINNING_CONSISTENCY": True,
            "proof": (
                "For fixed retained positions A and tau in S_k, choose the k retained "
                "values in C(n,k) ways; tau fixes their placement on A and the remaining "
                "values have (n-k)! orders. Thus n!/k! permutations induce tau, independent "
                "of A and tau. Conditioning iid thinning on K=k makes A uniform."
            ),
            "data_verification": "all 34 (n,k) cells agree exactly with the frozen S_k counts",
        },
        "controls": analysis.controls,
        "frozen_baseline": {
            str(n): _exact_triplet(analysis.baseline[n]) for n in EXACT_N
        },
        "grid_diagnostics": {
            "U_orbital": _monotone_on_grid(analysis, 0),
            "E_available": _monotone_on_grid(analysis, 1),
            "U_orbital_given_available": _monotone_on_grid(analysis, 2),
            "scope": "descriptive on the fixed p grid",
        },
        "large_n_preflight": {
            "LARGE_N_ORBITAL_BACKEND": "NOT_AVAILABLE",
            "first_blocker": (
                "emergencia/p1a_tie_aut_diagnostic.py::exact_automorphisms and "
                "evaluate_tie_aut reject n>9; no validated general r_orb backend was found"
            ),
        },
        "provenance": {
            "generator": "emergencia/p1a_macrotest_exploratorio_d2.py",
            "generator_sha256": _sha256(Path(__file__)),
            "exact_sources": analysis.source_digests,
            "coefficient_rows_reused": analysis.available_rows,
            "randomness": None,
            "new_dependencies": [],
        },
        "artifacts": {
            NP_FILENAME: {"sha256": np_digest, "phase": PHASE},
            NK_FILENAME: {"sha256": nk_digest, "phase": PHASE},
        },
        "claim_ceiling": (
            "Projective consistency of uniform permutations and exact finite n<=9 "
            "description only; no physical RG, power law, regression, or n->infinity claim"
        ),
    }


def _rows_to_csv(rows: Sequence[dict[str, object]], fields: Sequence[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def write_artifacts(analysis: ExactAnalysis, output_dir: Path) -> list[tuple[Path, str]]:
    np_path = output_dir / NP_FILENAME
    nk_path = output_dir / NK_FILENAME
    summary_path = output_dir / SUMMARY_FILENAME
    np_digest = comparison._write_with_sidecar(
        np_path, _rows_to_csv(analysis.np_rows, NP_FIELDS), overwrite=False
    )
    nk_digest = comparison._write_with_sidecar(
        nk_path, _rows_to_csv(analysis.nk_rows, NK_FIELDS), overwrite=False
    )
    payload = summary_payload(analysis, np_digest, nk_digest)
    summary_data = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    summary_digest = comparison._write_with_sidecar(summary_path, summary_data, overwrite=False)
    return [(np_path, np_digest), (nk_path, nk_digest), (summary_path, summary_digest)]


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-artifacts", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    analysis = analyze()
    print(f"PHASE={PHASE}")
    print("EXACT_THINNING_CONSISTENCY=YES")
    for n in EXACT_N:
        u, e, conditioned = analysis.baseline[n]
        print(
            f"N={n} U_original={_fraction_text(u)} E_original={_fraction_text(e)} "
            f"U_given_E={_fraction_text(conditioned) if conditioned is not None else 'NA'}"
        )
    for control, status in analysis.controls.items():
        print(f"{control}={status}")
    print("LARGE_N_ORBITAL_BACKEND=NOT_AVAILABLE")
    if args.write_artifacts:
        for path, digest in write_artifacts(analysis, args.output_dir):
            print(f"WROTE {path} sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
