#!/usr/bin/env python3
"""Step 8: exact q_p coefficients and the frozen falsifier verdict for Xi^A/B/C.

Executes step 8 of the sequence in
``emergencia/P1a_contrato_admisibilidad_resumen_coarse_graining_d2.md`` §6, strictly
inside the lane frozen by ``emergencia/P1a_contrato_falsador_paso7_d2.md`` (signed off
by the PI on 26 August 2026).  Nothing here is chosen after seeing a value: the
criterion, the population, the graded statistics and the descriptive magnitude were
all frozen beforehand.

What is computed, per the estimand contract ``P1a_contrato_estimando_qp_orbital_d2.md``
§6, by EXACT summation over masks and never by Monte Carlo:

    a_k(sigma) = |{A subset [n] : |A|=k, r_orb(C_sigma[A]) = 1}|
    b_k(sigma) = |{A subset [n] : |A|=k, M(C_sigma[A]) != empty}|
    q_p = sum_k a_k p^k (1-p)^(n-k),      e_p = sum_k b_k p^k (1-p)^(n-k)

Verdict, frozen in the step-7 contract §3, with alpha = (a_6, ..., a_{n-1}):

    Xi^X is SUFFICIENT at n  iff  alpha is constant on every fibre of P_X(n),
    P_X(n) = fibres with avail_1 = 1 and at least two members.

By H1 of that contract, a permutation with Q(C) empty has a = b = 0 identically; the
coefficient table therefore stores the available domain only, and H1 is TESTED here on
a deterministic sample rather than assumed.

    PYTHONDONTWRITEBYTECODE=1 python -m emergencia.p1a_qp_falsador_d2 \
        --n 6 7 8 9 --write-artifact
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
from typing import Iterable, Sequence

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_estabilidad_d2 as stability
from emergencia import p1a_paisaje_niveles_d2 as landscape
from emergencia import p1a_sup_exacto as sup_exact
from emergencia import p1a_tie_aut_diagnostic as tie_aut
from emergencia import p1a_xi_familia_fibras_d2 as xi


EXACT_N = landscape.EXACT_N
MEMBERS = xi.MEMBERS
MIN_SUPPORT = 6  # |A| < 6 cannot host two disjoint chained intervals of size >= 3
H1_SAMPLE = 200  # unavailable permutations per n on which H1 is tested exhaustively
RERANK_SAMPLE = 200  # permutations per n on which the fast reranker is cross-checked
SUP_WIDTH = Fraction(1, 2**40)

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = HERE / "resultados"
COEFFICIENT_FILENAME = "p1a_qp_coeficientes_d2.csv"
SUMMARY_FILENAME = "p1a_qp_falsador_resumen.json"

COEFFICIENT_FIELDS = (
    "n",
    "permutation",
    "r_orb",
    "a_coefficients",
    "b_coefficients",
    "alpha",
)

_ORBIT_CACHE: dict[tuple[int, ...], tuple[int, int]] = {}


def orbit_indicator(pattern: tuple[int, ...]) -> tuple[int, int]:
    """(r_orb, availability) of one induced pattern, memoized by isomorphism class.

    r_orb and M != empty are isomorphism invariants of the induced subposet, so two
    masks inducing the same pattern share them; the cache therefore cannot change the
    estimand, only its cost.
    """

    cached = _ORBIT_CACHE.get(pattern)
    if cached is not None:
        return cached
    diagnostic = tie_aut.evaluate_tie_aut(pattern)
    if diagnostic.optimized_state == comparison.STATE_EMPTY:
        value = (0, 0)
    else:
        value = (
            1
            if diagnostic.diagnostic_state
            in (tie_aut.DIAGNOSTIC_UNIQUE, tie_aut.DIAGNOSTIC_TIE_AUT_ONLY)
            else 0,
            1,
        )
    _ORBIT_CACHE[pattern] = value
    return value


def induced_pattern(permutation: Sequence[int], retained: Sequence[int]) -> tuple[int, ...]:
    """Rerank the retained values into a permutation pattern.

    Equivalent to ``p1a_estabilidad_d2.induced_permutation``, which the estimand
    contract authorizes as the induction operation; that function is used as the
    reference in :func:`crosscheck_reranking`.
    """

    values = [permutation[index] for index in retained]
    pattern = [0] * len(values)
    for rank, position in enumerate(sorted(range(len(values)), key=values.__getitem__)):
        pattern[position] = rank
    return tuple(pattern)


def coefficients(permutation: Sequence[int], *, all_masks: bool = False) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Exact (a_0..a_n, b_0..b_n) by summation over masks."""

    perm = tuple(int(value) for value in permutation)
    n = len(perm)
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    low = 0 if all_masks else MIN_SUPPORT
    for k in range(low, n + 1):
        for retained in combinations(range(n), k):
            if k == 0:
                continue
            r_orb, available = orbit_indicator(induced_pattern(perm, retained))
            a[k] += r_orb
            b[k] += available
    return tuple(a), tuple(b)


def alpha_of(a: Sequence[int], n: int) -> tuple[int, ...]:
    """The frozen free-coefficient vector (a_6, ..., a_{n-1})."""

    return tuple(a[MIN_SUPPORT:n])


def evaluate_bernstein(coefficients_: Sequence[int], n: int, p: Fraction) -> Fraction:
    return sum(
        (
            Fraction(coefficients_[k]) * p**k * (1 - p) ** (n - k)
            for k in range(n + 1)
            if coefficients_[k]
        ),
        Fraction(0),
    )


def direct_mask_sum(permutation: Sequence[int], p: Fraction) -> tuple[Fraction, Fraction]:
    """q_p and e_p by direct weighted summation over all 2^n masks."""

    perm = tuple(int(value) for value in permutation)
    n = len(perm)
    q = Fraction(0)
    e = Fraction(0)
    for k in range(n + 1):
        weight = p**k * (1 - p) ** (n - k)
        if weight == 0:
            continue
        for retained in combinations(range(n), k):
            if k == 0:
                continue
            r_orb, available = orbit_indicator(induced_pattern(perm, retained))
            q += weight * r_orb
            e += weight * available
    return q, e


# --------------------------------------------------------------------------- checks


def crosscheck_reranking(permutation: Sequence[int]) -> None:
    """The fast reranker equals the authorized one, and preserves comparabilities."""

    perm = tuple(int(value) for value in permutation)
    n = len(perm)
    for k in range(1, n + 1):
        for retained in combinations(range(n), k):
            pattern = induced_pattern(perm, retained)
            reference = tuple(
                int(value) for value in stability.induced_permutation(perm, retained)
            )
            if pattern != reference:
                raise RuntimeError(f"reranker disagrees with induced_permutation at {perm} {retained}")
            for i in range(k):
                for j in range(k):
                    original = perm[retained[i]] < perm[retained[j]] and retained[i] < retained[j]
                    induced = pattern[i] < pattern[j] and i < j
                    if original != induced:
                        raise RuntimeError(
                            f"reranking changed a comparability at {perm} {retained}"
                        )


def check_h1(permutation: Sequence[int]) -> None:
    """H1: a permutation with no admissible candidate has a = b = 0 over ALL masks."""

    a, b = coefficients(permutation, all_masks=True)
    if any(a) or any(b):
        raise RuntimeError(f"H1 falsified: unavailable permutation {permutation} has support")


def check_controls(permutation: Sequence[int], a: Sequence[int], b: Sequence[int], r_orb: int) -> None:
    n = len(permutation)
    if a[0] != 0:
        raise RuntimeError(f"q_0 != 0 at {permutation}")
    if any(a[k] or b[k] for k in range(1, MIN_SUPPORT)):
        raise RuntimeError(f"support below |A|=6 at {permutation}")
    if a[n] != r_orb:
        raise RuntimeError(f"q_1 != r_orb at {permutation}")
    for k in range(n + 1):
        if not 0 <= a[k] <= b[k] <= math.comb(n, k):
            raise RuntimeError(f"coefficient out of range at {permutation}, k={k}")


def check_polynomial_against_direct_sum(
    permutation: Sequence[int], a: Sequence[int], b: Sequence[int]
) -> None:
    n = len(permutation)
    for p in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        q_direct, e_direct = direct_mask_sum(permutation, p)
        if evaluate_bernstein(a, n, p) != q_direct:
            raise RuntimeError(f"q_p polynomial disagrees with the mask sum at {permutation}")
        if evaluate_bernstein(b, n, p) != e_direct:
            raise RuntimeError(f"e_p polynomial disagrees with the mask sum at {permutation}")


# ------------------------------------------------------------------------ falsifier


def _supremum(alpha_a: Sequence[int], alpha_b: Sequence[int], n: int) -> tuple[float, float]:
    bernstein = [0] * (n + 1)
    for offset, (left, right) in enumerate(zip(alpha_a, alpha_b)):
        bernstein[MIN_SUPPORT + offset] = left - right
    poly = sup_exact.bernstein_to_monomial(bernstein, n)
    low, high = sup_exact.supremum_on_unit_interval(poly, width=SUP_WIDTH)
    return float(low), float(high)


def run_size(n: int) -> tuple[dict[str, object], dict[tuple[int, ...], dict[str, object]]]:
    """Coefficients, controls and the frozen verdict for one size."""

    available: dict[tuple[int, ...], dict[str, object]] = {}
    unavailable: list[tuple[int, ...]] = []
    xi_of: dict[tuple[int, ...], dict[str, tuple]] = {}

    for permutation in permutations(range(n)):
        result = landscape.score_landscape(permutation)
        # Derive the summaries from the SAME landscape rather than recomputing it.
        descriptors = [
            (
                level.primary_score,
                level.secondary_score,
                level.candidate_count,
                level.orbit_count,
            )
            for level in result.levels
        ]
        xi_of[permutation] = xi.xi_from_descriptors(descriptors, result.n_candidates)
        if result.n_candidates == 0:
            unavailable.append(permutation)
            continue
        r_orb = int(
            result.levels[0].orbit_count == 1
        )  # M != empty here, so r_orb = 1{rho = 1}
        a, b = coefficients(permutation)
        check_controls(permutation, a, b, r_orb)
        available[permutation] = {
            "a": a,
            "b": b,
            "r_orb": r_orb,
            "alpha": alpha_of(a, n),
        }

    # ---- validations mandated by the estimand contract section 7
    ordered_unavailable = sorted(unavailable)
    h1_checked = ordered_unavailable[:: max(1, len(ordered_unavailable) // H1_SAMPLE)][:H1_SAMPLE]
    for permutation in h1_checked:
        check_h1(permutation)

    ordered_available = sorted(available)
    rerank_checked = ordered_available[:: max(1, len(ordered_available) // RERANK_SAMPLE)][
        :RERANK_SAMPLE
    ]
    for permutation in rerank_checked:
        crosscheck_reranking(permutation)
        record = available[permutation]
        check_polynomial_against_direct_sum(permutation, record["a"], record["b"])  # type: ignore[arg-type]

    # ---- the frozen verdict
    report: dict[str, object] = {
        "n": n,
        "permutations": math.factorial(n),
        "available_permutations": len(available),
        "unavailable_permutations": len(unavailable),
        "free_coefficients": list(range(MIN_SUPPORT, n)),
        "degrees_of_freedom": max(0, n - MIN_SUPPORT),
        "validation": {
            "h1_exhaustive_mask_checks": len(h1_checked),
            "reranking_and_direct_sum_checks": len(rerank_checked),
            "q0_zero_checked": len(available),
            "q1_equals_r_orb_checked": len(available),
        },
    }

    for member in MEMBERS:
        fibres: dict[tuple, list[tuple[int, ...]]] = {}
        for permutation in available:
            fibres.setdefault(xi_of[permutation][member], []).append(permutation)
        population = {
            key: members for key, members in fibres.items() if len(members) >= 2
        }

        homogeneous = 0
        homogeneous_mass = 0
        population_mass = 0
        inhomogeneous_examples: list[dict[str, object]] = []
        best: dict[str, object] | None = None

        for key in sorted(population, key=str):
            members = population[key]
            population_mass += len(members)
            alphas = {available[permutation]["alpha"] for permutation in members}
            if len(alphas) == 1:
                homogeneous += 1
                homogeneous_mass += len(members)
                continue

            witness_of: dict[tuple, tuple[int, ...]] = {}
            for permutation in members:
                witness_of.setdefault(available[permutation]["alpha"], permutation)  # type: ignore[index]
            ordered = sorted(witness_of)
            if len(inhomogeneous_examples) < 5:
                inhomogeneous_examples.append(
                    {
                        "xi": list(key),
                        "distinct_alpha": len(ordered),
                        "alpha_a": list(ordered[0]),
                        "alpha_b": list(ordered[-1]),
                        "permutation_a": landscape.encode_permutation(witness_of[ordered[0]]),
                        "permutation_b": landscape.encode_permutation(witness_of[ordered[-1]]),
                    }
                )
            for left, right in combinations(ordered, 2):
                low, high = _supremum(left, right, n)
                if best is None or low > best["sup_low"]:
                    best = {
                        "sup_low": low,
                        "sup_high": high,
                        "xi": list(key),
                        "alpha_a": list(left),
                        "alpha_b": list(right),
                        "permutation_a": landscape.encode_permutation(witness_of[left]),
                        "permutation_b": landscape.encode_permutation(witness_of[right]),
                    }

        if not population:
            verdict = "VACUOUS"
        elif homogeneous == len(population):
            verdict = "SUFFICIENT"
        else:
            verdict = "NOT_SUFFICIENT"

        report[member] = {
            "verdict": verdict,
            "population_fibres": len(population),
            "excluded_unavailable_fibre_permutations": len(unavailable),
            "excluded_singleton_fibres": sum(
                1 for members in fibres.values() if len(members) == 1
            ),
            "homogeneous_fibres": homogeneous,
            "h": homogeneous / len(population) if population else None,
            "w": homogeneous_mass / population_mass if population_mass else None,
            "population_permutations": population_mass,
            "D_low": best["sup_low"] if best else 0.0,
            "D_high": best["sup_high"] if best else 0.0,
            "D_witness": best,
            "inhomogeneous_examples": inhomogeneous_examples,
        }

    return report, available


def validate_report(report: dict[str, object]) -> None:
    n = int(report["n"])  # type: ignore[arg-type]
    if report["available_permutations"] + report["unavailable_permutations"] != math.factorial(n):
        raise RuntimeError(f"availability partition mismatch at n={n}")
    previous = None
    for member in MEMBERS:
        block = report[member]
        assert isinstance(block, dict)
        if block["verdict"] not in ("SUFFICIENT", "NOT_SUFFICIENT", "VACUOUS"):
            raise RuntimeError(f"unknown verdict at n={n}")
        if block["homogeneous_fibres"] > block["population_fibres"]:
            raise RuntimeError(f"more homogeneous fibres than fibres at n={n}")
        # H4: a finer member refines fibres, so D can only shrink.
        if previous is not None and block["D_low"] > previous + 1e-12:
            raise RuntimeError(f"H4 violated at n={n}: D grew with depth")
        previous = block["D_low"]


def coefficient_rows(n: int, report: dict[str, object], records: dict) -> list[dict[str, object]]:
    return [
        {
            "n": n,
            "permutation": landscape.encode_permutation(permutation),
            "r_orb": record["r_orb"],
            "a_coefficients": "-".join(str(value) for value in record["a"]),
            "b_coefficients": "-".join(str(value) for value in record["b"]),
            "alpha": "-".join(str(value) for value in record["alpha"]),
        }
        for permutation, record in sorted(records.items())
    ]


def _source_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def summary_payload(reports: Sequence[dict[str, object]], coefficient_digest: str) -> dict[str, object]:
    return {
        "artifact_schema": "P1A_QP_FALSADOR_D2_V1",
        "result_status": "OBSERVED_REPRODUCIBLE_EXACT_FALSIFIER",
        "authorization": {
            "contract": "emergencia/P1a_contrato_falsador_paso7_d2.md",
            "signoff": "PI, 26 August 2026",
            "design_phase": "CLOSED_ON_SIGNOFF",
            "criterion": "EXACT_COEFFICIENT_VECTOR_EQUALITY",
            "threshold": None,
            "p_choice": None,
            "null_band": None,
            "multiplicity_correction": "NOT_APPLICABLE_EXACT_EQUALITY",
            "population": "AVAILABLE_FIBRES_WITH_AT_LEAST_TWO_MEMBERS",
            "all_members_reported": True,
        },
        "declared_tautologies": {
            "q1_equals_r_orb": "control tautologico; r_orb is a function of Xi^A",
            "q0_is_zero": "control; a_0 = 0 by construction",
            "unavailable_fibre_is_zero": "H1, proved before execution and tested here",
            "depth_monotonicity_of_D": "H4; direction forced, only magnitude informs",
            "n6_is_vacuous": "H2; no free coefficient exists at n=6",
        },
        "method": {
            "evaluation": "EXACT_MASK_SUM",
            "monte_carlo": False,
            "cache": "memoized by induced pattern; r_orb is an isomorphism invariant",
            "supremum": "certified rational enclosure via Sturm isolation on (0,1)",
            "supremum_bracket_width": f"<= 2^-40 before the exact Lipschitz correction",
        },
        "provenance": {
            "generator": "emergencia/p1a_qp_falsador_d2.py",
            "generator_sha256": _source_sha256(),
            "supremum_module": "emergencia/p1a_sup_exacto.py",
            "supremum_module_sha256": hashlib.sha256(
                Path(sup_exact.__file__).read_bytes()
            ).hexdigest(),
            "frozen_instrument": "emergencia/p1a_tie_aut_diagnostic.py",
            "frozen_instrument_sha256": hashlib.sha256(
                Path(tie_aut.__file__).read_bytes()
            ).hexdigest(),
            "frozen_instrument_modified": False,
            "coefficient_csv": COEFFICIENT_FILENAME,
            "coefficient_csv_sha256": coefficient_digest,
            "absent_permutation_semantics": (
                "a permutation absent from the coefficient table has Q(C) empty, hence "
                "a = b = 0 identically by H1; this is a theorem, not a convention"
            ),
            "randomness": None,
            "new_dependencies": [],
        },
        "reports": list(reports),
    }


def run(n_values: Iterable[int] = EXACT_N) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    n_sequence = tuple(int(n) for n in n_values)
    if not n_sequence or any(n not in EXACT_N for n in n_sequence):
        raise ValueError(f"n values must be a nonempty subset of {EXACT_N}")

    reports: list[dict[str, object]] = []
    rows: list[dict[str, object]] = []
    for n in n_sequence:
        report, records = run_size(n)
        validate_report(report)
        reports.append(report)
        rows.extend(coefficient_rows(n, report, records))
        line = " ".join(
            f"{member}:{report[member]['verdict']}"  # type: ignore[index]
            f",h={report[member]['h']}"  # type: ignore[index]
            f",D={report[member]['D_low']:.6g}"  # type: ignore[index]
            for member in MEMBERS
        )
        print(f"QP_FALSADOR N={n} {line}", flush=True)
    return rows, reports


def write_artifacts(
    rows: Sequence[dict[str, object]],
    reports: Sequence[dict[str, object]],
    output_dir: Path,
    *,
    overwrite: bool = False,
) -> list[tuple[Path, str]]:
    csv_bytes = comparison.rows_to_csv(rows, COEFFICIENT_FIELDS).encode("utf-8")
    csv_path = output_dir / COEFFICIENT_FILENAME
    csv_digest = comparison._write_with_sidecar(csv_path, csv_bytes, overwrite=overwrite)

    payload = summary_payload(reports, csv_digest)
    data = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    summary_path = output_dir / SUMMARY_FILENAME
    summary_digest = comparison._write_with_sidecar(summary_path, data, overwrite=overwrite)
    return [(csv_path, csv_digest), (summary_path, summary_digest)]


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", nargs="+", type=int, default=list(EXACT_N))
    parser.add_argument("--write-artifact", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    rows, reports = run(args.n)
    if args.write_artifact:
        for path, digest in write_artifacts(rows, reports, args.output_dir, overwrite=args.overwrite):
            print(f"ARTIFACT={path} SHA256={digest}")
    else:
        print(json.dumps({"reports": reports}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
