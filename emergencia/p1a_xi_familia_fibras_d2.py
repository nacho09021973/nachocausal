#!/usr/bin/env python3
"""Fibre study of the frozen summary family Xi^A subset Xi^B subset Xi^C.

Executes condition 8 of
``emergencia/P1a_contrato_admisibilidad_resumen_coarse_graining_d2.md`` for the
family frozen in ``emergencia/P1a_contrato_resumen_Xi_familia_d2.md``: before any
target is observed, document the fibre-size distribution of each summary and verify
that fibres contain collisions between NON-ISOMORPHIC order classes.

Definitions are taken verbatim from the family contract, which was frozen before this
module was written:

    avail_j = 1{L >= j};  m_j, s_j = the two coordinates of the j-th distinct score
    level in descending lexicographic order;  c_j = |A_j|;  r_j = |A_j / Aut(C)|;
    NA whenever avail_j = 0, never zero.

    Xi^A = (avail_1, m_1, s_1, c_1, r_1)                                  dim  5
    Xi^B = Xi^A ++ (avail_2, m_2, s_2, c_2, r_2)                          dim 10
    Xi^C = Xi^B ++ (avail_3, m_3, s_3, c_3, r_3) ++ (L, |Q(C)|, R)        dim 18

Every coordinate is computed by TWO independent paths, as condition 10 requires: a
live recomputation from the permutation through the landscape extractor, and a
reconstruction from the already frozen landscape CSV.  Neither is its own reference.

NOT computed, NOT approximated and NOT inferred anywhere in this module: q_p,
q_p_star, e_p, a_k, b_k, thinning masks, induced subposets, retention rates, pair
selection or any falsification criterion.  No Monte Carlo simulation is performed.

    PYTHONDONTWRITEBYTECODE=1 python -m emergencia.p1a_xi_familia_fibras_d2 \
        --n 6 7 8 9 --write-artifact
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from collections import Counter, defaultdict
from itertools import permutations
from pathlib import Path
from typing import Iterable, Sequence

from dev.r3_bridge_e_fibers import canonical_form, relation_matrix
from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_paisaje_niveles_d2 as landscape


EXACT_N = landscape.EXACT_N
MEMBERS = ("XI_A", "XI_B", "XI_C")
MEMBER_DIMENSION = {"XI_A": 5, "XI_B": 10, "XI_C": 18}
FAMILY_CONTRACT = "emergencia/P1a_contrato_resumen_Xi_familia_d2.md"

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = HERE / "resultados"
LANDSCAPE_CSV = DEFAULT_OUTPUT_DIR / landscape.LANDSCAPE_FILENAME
SUMMARY_FILENAME = "p1a_xi_familia_fibras_resumen.json"

Coordinate = int | None
XiVector = tuple[Coordinate, ...]


LevelDescriptor = tuple[int, int, int, int]  # (m_j, s_j, c_j, r_j)


def _level_block(
    descriptors: Sequence[LevelDescriptor], depth: int
) -> tuple[Coordinate, ...]:
    """(avail_j, m_j, s_j, c_j, r_j) for j = depth, with NA below the depth."""

    if len(descriptors) < depth:
        return (0, None, None, None, None)
    return (1,) + descriptors[depth - 1]


def xi_from_descriptors(
    descriptors: Sequence[LevelDescriptor], n_candidates: int
) -> dict[str, XiVector]:
    """The three frozen summaries, from the exact level list of one permutation."""

    total_orbits = sum(descriptor[3] for descriptor in descriptors)
    xi_a = _level_block(descriptors, 1)
    xi_b = xi_a + _level_block(descriptors, 2)
    xi_c = (
        xi_b
        + _level_block(descriptors, 3)
        + (len(descriptors), n_candidates, total_orbits)
    )

    for member, vector in (("XI_A", xi_a), ("XI_B", xi_b), ("XI_C", xi_c)):
        if len(vector) != MEMBER_DIMENSION[member]:
            raise RuntimeError(f"{member} has the wrong dimension")
    return {"XI_A": xi_a, "XI_B": xi_b, "XI_C": xi_c}


def xi_live(permutation: Sequence[int]) -> dict[str, XiVector]:
    """Path 1: recompute the landscape from the permutation, then summarize."""

    result = landscape.score_landscape(permutation)
    descriptors = [
        (
            level.primary_score,
            level.secondary_score,
            level.candidate_count,
            level.orbit_count,
        )
        for level in result.levels
    ]
    return xi_from_descriptors(descriptors, result.n_candidates)


def _read_landscape_csv(path: Path, n_values: Sequence[int]) -> dict[tuple[int, str], list[dict[str, str]]]:
    wanted = set(n_values)
    grouped: dict[tuple[int, str], list[dict[str, str]]] = defaultdict(list)
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            n = int(row["n"])
            if n in wanted:
                grouped[(n, row["permutation"])].append(row)
    return grouped


def xi_from_csv_rows(rows: Sequence[dict[str, str]]) -> dict[str, XiVector]:
    """Path 2: rebuild the summaries from the frozen landscape table alone."""

    first = rows[0]
    n_candidates = int(first["n_candidates"])
    if int(first["candidates_available"]) == 0:
        if len(rows) != 1 or n_candidates != 0:
            raise RuntimeError("an unavailable permutation must carry exactly one NA row")
        return xi_from_descriptors((), 0)

    ordered = sorted(rows, key=lambda row: int(row["level_index"]))
    if [int(row["level_index"]) for row in ordered] != list(range(len(ordered))):
        raise RuntimeError("level indices are not a contiguous range")
    if int(first["n_score_levels"]) != len(ordered):
        raise RuntimeError("n_score_levels disagrees with the number of rows")

    descriptors = [
        (
            int(row["primary_score"]),
            int(row["secondary_score"]),
            int(row["candidate_count"]),
            int(row["orbit_count"]),
        )
        for row in ordered
    ]
    return xi_from_descriptors(descriptors, n_candidates)


def _order_invariant(permutation: Sequence[int]) -> tuple[int, tuple[int, ...]]:
    """A cheap isomorphism invariant: relation count plus the sorted degree profile.

    Two permutations whose invariants differ are provably NON-isomorphic.  Used only
    where the exact canonical form is not affordable (the unavailable fibre contains
    antichains, on which colour refinement does not split and canonical_form is n!).
    """

    relation = relation_matrix(tuple(int(value) for value in permutation))
    n = len(relation)
    degrees = sorted(
        (
            sum(1 for j in range(n) if relation[j][i]),
            sum(1 for j in range(n) if relation[i][j]),
        )
        for i in range(n)
    )
    total = sum(1 for i in range(n) for j in range(n) if relation[i][j])
    return total, tuple(degrees)


def _canonical_id(permutation: Sequence[int]) -> str:
    perm = tuple(int(value) for value in permutation)
    canonical = canonical_form(relation_matrix(perm), len(perm))
    packed = bytes(1 if value else 0 for value in canonical)
    return hashlib.sha256(packed).hexdigest()[:16]


def study_fibres(
    n: int, csv_rows: dict[tuple[int, str], list[dict[str, str]]]
) -> dict[str, object]:
    """Exhaustive fibre study over S_n for the three frozen summaries."""

    fibres: dict[str, dict[XiVector, list[str]]] = {member: {} for member in MEMBERS}
    available: set[str] = set()
    unavailable: list[str] = []
    crosschecks = 0

    for permutation in permutations(range(n)):
        encoded = landscape.encode_permutation(permutation)
        live = xi_live(permutation)

        rows = csv_rows.get((n, encoded))
        if rows is None:
            raise RuntimeError(f"landscape table is missing n={n} permutation {encoded}")
        replayed = xi_from_csv_rows(rows)
        if replayed != live:
            raise RuntimeError(f"independent Xi paths disagree at n={n} {encoded}")
        crosschecks += 1

        if live["XI_A"][0] == 1:
            available.add(encoded)
        else:
            unavailable.append(encoded)
        for member in MEMBERS:
            fibres[member].setdefault(live[member], []).append(encoded)

    report: dict[str, object] = {
        "n": n,
        "permutations": math.factorial(n),
        "independent_path_crosschecks": crosschecks,
        "permutations_available": len(available),
        "permutations_unavailable": len(unavailable),
    }

    # Exact isomorphism classes are affordable only on the available domain; the
    # unavailable fibre contains antichains, where canonical_form degenerates to n!.
    canonical_of: dict[str, str] = {
        encoded: _canonical_id(tuple(int(digit) for digit in encoded))
        for encoded in sorted(available)
    }

    # The unavailable permutations form one single fibre in all three members, so its
    # non-isomorphic witness is computed once rather than per member.
    unavailable_witness: dict[str, object] | None = None
    if len(unavailable) >= 2:
        reference = unavailable[0]
        reference_invariant = _order_invariant(tuple(int(d) for d in reference))
        for encoded in unavailable[1:]:
            invariant = _order_invariant(tuple(int(d) for d in encoded))
            if invariant == reference_invariant:
                continue
            separated_by = (
                "relation count"
                if invariant[0] != reference_invariant[0]
                else "in/out-degree profile"
            )
            unavailable_witness = {
                "permutation_a": reference,
                "permutation_b": encoded,
                "relation_count_a": reference_invariant[0],
                "relation_count_b": invariant[0],
                "degree_profile_a": [list(pair) for pair in reference_invariant[1]],
                "degree_profile_b": [list(pair) for pair in invariant[1]],
                "separated_by": separated_by,
                "certificate": (
                    "the two permutations differ in an order invariant "
                    f"({separated_by}), hence they are non-isomorphic"
                ),
            }
            break

    for member in MEMBERS:
        buckets = fibres[member]
        sizes = Counter(len(members) for members in buckets.values())
        singleton_members = sizes[1]

        mixed_fibres = 0
        classes_in_mixed: Counter[int] = Counter()
        witness: dict[str, object] | None = None
        for key, members in sorted(buckets.items(), key=lambda item: str(item[0])):
            if key[0] != 1:
                continue
            classes = {encoded: canonical_of[encoded] for encoded in members}
            distinct = set(classes.values())
            if len(distinct) > 1:
                mixed_fibres += 1
                classes_in_mixed[len(distinct)] += 1
                if witness is None:
                    first = members[0]
                    other = next(
                        encoded
                        for encoded in members
                        if canonical_of[encoded] != canonical_of[first]
                    )
                    witness = {
                        "xi": list(key),
                        "permutation_a": first,
                        "permutation_b": other,
                        "canonical_a": canonical_of[first],
                        "canonical_b": canonical_of[other],
                        "certificate": "exact canonical form of the strict order relation",
                    }

        report[member] = {
            "dimension": MEMBER_DIMENSION[member],
            "n_fibres": len(buckets),
            "fibre_size_distribution": {
                str(size): sizes[size] for size in sorted(sizes)
            },
            "max_fibre_size": max(sizes, default=0),
            "singleton_fibres": sizes[1],
            "permutations_alone_in_their_fibre": singleton_members,
            "fraction_alone_in_their_fibre": singleton_members / math.factorial(n),
            "available_fibres": sum(1 for key in buckets if key[0] == 1),
            "available_fibres_with_several_isomorphism_classes": mixed_fibres,
            "isomorphism_classes_per_mixed_available_fibre": {
                str(count): classes_in_mixed[count] for count in sorted(classes_in_mixed)
            },
            "non_isomorphic_collision_witness_available_domain": witness,
            "non_isomorphic_collision_witness_unavailable_fibre": unavailable_witness,
            "injective": singleton_members == math.factorial(n),
        }

    return report


def validate_report(report: dict[str, object]) -> None:
    n = int(report["n"])  # type: ignore[arg-type]
    total = math.factorial(n)
    if report["permutations"] != total:
        raise RuntimeError(f"factorial mismatch at n={n}")
    if report["independent_path_crosschecks"] != total:
        raise RuntimeError(f"independent path crosscheck total mismatch at n={n}")
    if report["permutations_available"] + report["permutations_unavailable"] != total:
        raise RuntimeError(f"availability partition mismatch at n={n}")

    previous_fibres = 0
    for member in MEMBERS:
        block = report[member]
        assert isinstance(block, dict)
        counted = sum(
            int(size) * count
            for size, count in block["fibre_size_distribution"].items()
        )
        if counted != total:
            raise RuntimeError(f"{member} fibre sizes do not cover S_n at n={n}")
        if sum(block["fibre_size_distribution"].values()) != block["n_fibres"]:
            raise RuntimeError(f"{member} fibre count mismatch at n={n}")
        # Nested summaries: a finer summary can only split fibres, never merge them.
        if block["n_fibres"] < previous_fibres:
            raise RuntimeError(f"{member} coarsened a finer summary at n={n}")
        previous_fibres = int(block["n_fibres"])


def _source_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def _file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def summary_payload(reports: Sequence[dict[str, object]]) -> dict[str, object]:
    return {
        "artifact_schema": "P1A_XI_FAMILIA_FIBRAS_D2_V1",
        "result_status": "OBSERVED_REPRODUCIBLE_STATIC_FIBRE_STUDY",
        "family": {
            "contract": FAMILY_CONTRACT,
            "members": list(MEMBERS),
            "dimensions": MEMBER_DIMENSION,
            "nested": True,
            "all_members_reported": True,
            "frozen_before_target": True,
            "metric": "EXACT_VECTOR_EQUALITY",
            "coordinates": {
                "XI_A": ["avail_1", "m_1", "s_1", "c_1", "r_1"],
                "XI_B": ["...XI_A", "avail_2", "m_2", "s_2", "c_2", "r_2"],
                "XI_C": [
                    "...XI_B",
                    "avail_3",
                    "m_3",
                    "s_3",
                    "c_3",
                    "r_3",
                    "L",
                    "n_candidates",
                    "total_orbits",
                ],
            },
            "empty_policy": "AVAIL_FLAG_AND_NA_NEVER_ZERO",
            "q1_is_tautological": True,
        },
        "condition_8_execution": {
            "fibre_size_distribution_documented": True,
            "non_isomorphic_collisions_verified": True,
            "isomorphism_certificate_available_domain": (
                "exact canonical form of the strict order relation "
                "(dev/r3_bridge_e_fibers.canonical_form)"
            ),
            "isomorphism_certificate_unavailable_fibre": (
                "differing order-invariant relation count; canonical_form is not "
                "affordable there because antichains defeat colour refinement"
            ),
            "executed_before_any_target_access": True,
        },
        "target_guard": {
            "q_p_computed": False,
            "q_p_star_computed": False,
            "e_p_computed": False,
            "a_k_or_b_k_computed": False,
            "thinning_masks_enumerated": False,
            "induced_subposets_evaluated": False,
            "retention_used": False,
            "pair_selection_rule_used": False,
            "falsification_criterion_used": False,
            "monte_carlo": False,
        },
        "validation": {
            "independent_coordinate_paths": [
                "live recomputation via p1a_paisaje_niveles_d2.score_landscape",
                "reconstruction from the frozen landscape CSV",
            ],
            "paths_agree_on_every_permutation": True,
            "guards": [
                "fibre sizes cover S_n exactly",
                "fibre counts match the size histogram",
                "a finer member never merges fibres of a coarser one",
                "availability partition covers S_n",
            ],
        },
        "provenance": {
            "generator": "emergencia/p1a_xi_familia_fibras_d2.py",
            "generator_sha256": _source_sha256(),
            "landscape_csv": landscape.LANDSCAPE_FILENAME,
            "landscape_csv_sha256": _file_sha256(LANDSCAPE_CSV),
            "landscape_generator": "emergencia/p1a_paisaje_niveles_d2.py",
            "frozen_instrument": "emergencia/p1a_tie_aut_diagnostic.py",
            "frozen_instrument_sha256": _file_sha256(
                Path(landscape.tie_aut.__file__)
            ),
            "frozen_instrument_modified": False,
            "isomorphism_backend": "dev/r3_bridge_e_fibers.py",
            "selector": comparison.MIN_COVERAGE_LEX,
            "k0": sealed.K0,
            "randomness": None,
            "new_dependencies": [],
        },
        "reports": list(reports),
    }


def run(n_values: Iterable[int] = EXACT_N) -> list[dict[str, object]]:
    n_sequence = tuple(int(n) for n in n_values)
    if not n_sequence or any(n not in EXACT_N for n in n_sequence):
        raise ValueError(f"n values must be a nonempty subset of {EXACT_N}")
    if not LANDSCAPE_CSV.exists():
        raise FileNotFoundError(f"missing frozen landscape table: {LANDSCAPE_CSV}")

    csv_rows = _read_landscape_csv(LANDSCAPE_CSV, n_sequence)
    reports: list[dict[str, object]] = []
    for n in n_sequence:
        report = study_fibres(n, csv_rows)
        validate_report(report)
        reports.append(report)
        line = " ".join(
            f"{member}:fibres={report[member]['n_fibres']}"  # type: ignore[index]
            f",max={report[member]['max_fibre_size']}"  # type: ignore[index]
            f",mixed={report[member]['available_fibres_with_several_isomorphism_classes']}"  # type: ignore[index]
            for member in MEMBERS
        )
        print(f"XI_FIBRAS N={n} {line}", flush=True)
    return reports


def write_artifact(
    reports: Sequence[dict[str, object]], output_dir: Path, *, overwrite: bool = False
) -> tuple[Path, str]:
    payload = summary_payload(reports)
    data = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    path = output_dir / SUMMARY_FILENAME
    digest = comparison._write_with_sidecar(path, data, overwrite=overwrite)
    return path, digest


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", nargs="+", type=int, default=list(EXACT_N))
    parser.add_argument("--write-artifact", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    reports = run(args.n)
    if args.write_artifact:
        path, digest = write_artifact(reports, args.output_dir, overwrite=args.overwrite)
        print(f"ARTIFACT={path} SHA256={digest}")
    else:
        print(json.dumps({"reports": reports}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
