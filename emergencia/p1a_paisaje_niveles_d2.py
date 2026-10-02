#!/usr/bin/env python3
"""Exact static score-level landscape of MIN_COVERAGE_LEX, with its orbit structure.

For every permutation of size n<=9 this module records the COMPLETE list of distinct
values of the frozen lexicographic score

    S_C(a,b,c,d) = ( min(C_ab, C_cd), C_ab + C_cd ),

over the admissible candidate set Q(C), together with, for each level, its candidate
count and the partition of that level into Aut(C)-orbits.

The extraction is deliberately CHOICE-FREE.  It fixes no top-k, no epsilon window, no
scalar gap, no primary/secondary deficit, no weighting between the two score
coordinates and no fixed-dimension summary.  The whole landscape permitted by n<=9 is
preserved so that any later coordinate proposal can be derived from it rather than
being selected against an observed target.

Scope, per emergencia/P1a_contrato_admisibilidad_resumen_coarse_graining_d2.md sec. 4,
which admits as information sources: "el numero y los scores de los candidatos de
Q(C)", "la particion en orbitas de candidatos situados en niveles de score previamente
definidos" and "cardinalidades de orbitas y estabilizadores".  Levels here are defined
before, and independently of, any target access.

NOT computed, NOT approximated and NOT inferred anywhere in this module:
q_p, q_p_star, e_p, the exact coefficients a_k / b_k, thinning masks, induced
subposets, retention rates, or any function of them.  This module never imports
emergencia.p1a_estabilidad_d2 and performs no Monte Carlo simulation.

The frozen instrument emergencia/p1a_tie_aut_diagnostic.py is NOT modified: its
sha256 is recorded inside emergencia/resultados/p1a_tie_aut_exacto_d2.json.  Its
sealed primitives are imported and reused instead.

    PYTHONDONTWRITEBYTECODE=1 python -m emergencia.p1a_paisaje_niveles_d2 \
        --n 6 7 8 9 --write-artifact
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from dataclasses import dataclass
from itertools import combinations, permutations
from pathlib import Path
from typing import Iterable, Sequence

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_tie_aut_diagnostic as tie_aut


EXACT_N = (6, 7, 8, 9)
MAX_EXACT_N = tie_aut.MAX_EXACT_N

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = HERE / "resultados"
LANDSCAPE_FILENAME = "p1a_paisaje_niveles_d2.csv"
SUMMARY_FILENAME = "p1a_paisaje_niveles_resumen.json"

LANDSCAPE_FIELDS = (
    "n",
    "permutation",
    "n_candidates",
    "n_score_levels",
    "n_automorphisms",
    "candidates_available",
    "level_index",
    "primary_score",
    "secondary_score",
    "candidate_count",
    "orbit_count",
    "orbit_sizes",
)

PERMUTATION_ENCODING = (
    "concatenated one-digit element images in index order; n<=9 so every image is 0..8"
)

Quadruple = tie_aut.Quadruple
Score = tie_aut.Score


@dataclass(frozen=True)
class ScoreLevel:
    """One distinct value of the lexicographic score, with its orbit structure."""

    primary_score: int
    secondary_score: int
    candidates: tuple[Quadruple, ...]
    orbits: tuple[tuple[Quadruple, ...], ...]

    @property
    def score(self) -> Score:
        return (self.primary_score, self.secondary_score)

    @property
    def candidate_count(self) -> int:
        return len(self.candidates)

    @property
    def orbit_count(self) -> int:
        return len(self.orbits)

    @property
    def orbit_sizes(self) -> tuple[int, ...]:
        return tuple(sorted((len(orbit) for orbit in self.orbits), reverse=True))


@dataclass(frozen=True)
class PermutationLandscape:
    """The complete exact score landscape of one permutation."""

    n: int
    permutation: tuple[int, ...]
    candidates: tuple[Quadruple, ...]
    levels: tuple[ScoreLevel, ...]
    n_automorphisms: int | None

    @property
    def n_candidates(self) -> int:
        return len(self.candidates)

    @property
    def n_score_levels(self) -> int:
        return len(self.levels)


def score_candidates(
    permutation: Sequence[int],
) -> tuple[tuple[tuple[Quadruple, Score], ...], tie_aut.Relation]:
    """Materialize EVERY admissible candidate with its exact score, not just the argmax.

    The admissibility test and the score expression are the ones of the frozen
    selector, evaluated from the sealed interval-count matrix
    (``p1a_enumeracion_simulacion.interval_count_matrix``) and the sealed threshold
    ``K0``.  ``p1a_tie_aut_diagnostic.materialize_lex_maximizers`` builds the same list
    internally and then discards everything below the argmax; that function is frozen
    and is used unchanged as the cross-check reference in :func:`validate_landscape`.
    """

    perm = sealed.validate_permutation(permutation)
    if len(perm) > MAX_EXACT_N:
        raise ValueError(f"exact landscape extraction is limited to n<={MAX_EXACT_N}")
    counts, comparable = sealed.interval_count_matrix(perm)
    relation = tie_aut._as_relation(comparable)

    scored: list[tuple[Quadruple, Score]] = []
    for a, b, c, d in combinations(range(len(perm)), 4):
        if not (comparable[a, b] and comparable[b, c] and comparable[c, d]):
            continue
        past = int(counts[a, b])
        future = int(counts[c, d])
        if past < sealed.K0 or future < sealed.K0:
            continue
        scored.append(((a, b, c, d), (min(past, future), past + future)))
    return tuple(scored), relation


def score_landscape(permutation: Sequence[int]) -> PermutationLandscape:
    """Group Q(C) into its exact score levels and split each level into Aut(C)-orbits."""

    perm = tuple(int(value) for value in sealed.validate_permutation(permutation))
    scored, relation = score_candidates(perm)

    if not scored:
        return PermutationLandscape(
            n=len(perm),
            permutation=perm,
            candidates=(),
            levels=(),
            n_automorphisms=None,
        )

    grouped: dict[Score, list[Quadruple]] = {}
    for candidate, score in scored:
        grouped.setdefault(score, []).append(candidate)

    automorphisms = tie_aut.exact_automorphisms(relation)
    levels: list[ScoreLevel] = []
    for score in sorted(grouped, reverse=True):
        members = tuple(sorted(grouped[score]))
        orbits = tie_aut._orbit_partition(members, automorphisms)
        levels.append(
            ScoreLevel(
                primary_score=score[0],
                secondary_score=score[1],
                candidates=members,
                orbits=orbits,
            )
        )

    return PermutationLandscape(
        n=len(perm),
        permutation=perm,
        candidates=tuple(sorted(candidate for candidate, _ in scored)),
        levels=tuple(levels),
        n_automorphisms=len(automorphisms),
    )


def validate_landscape(landscape: PermutationLandscape) -> None:
    """The five mandated invariants, checked against the frozen instrument."""

    perm = landscape.permutation

    # 1. the levels partition Q(C) exactly once.
    flattened = [
        candidate for level in landscape.levels for candidate in level.candidates
    ]
    if len(flattened) != landscape.n_candidates:
        raise RuntimeError(f"level partition lost candidates at {perm}")
    if set(flattened) != set(landscape.candidates):
        raise RuntimeError(f"level partition does not cover Q(C) at {perm}")
    if len({level.score for level in landscape.levels}) != landscape.n_score_levels:
        raise RuntimeError(f"score levels are not distinct at {perm}")
    if list(landscape.levels) != sorted(
        landscape.levels, key=lambda level: level.score, reverse=True
    ):
        raise RuntimeError(f"score levels are not in descending order at {perm}")

    diagnostic = tie_aut.evaluate_tie_aut(perm)

    # 2. the top level is exactly M(C) as materialized by the frozen instrument.
    if landscape.n_candidates == 0:
        if diagnostic.optimized_state != comparison.STATE_EMPTY:
            raise RuntimeError(f"empty Q(C) disagrees with the selector state at {perm}")
        if landscape.levels or landscape.n_automorphisms is not None:
            raise RuntimeError(f"empty Q(C) acquired a level or a group at {perm}")
        return
    if diagnostic.optimized_state == comparison.STATE_EMPTY:
        raise RuntimeError(f"nonempty Q(C) disagrees with EMPTY at {perm}")
    top = landscape.levels[0]
    if top.candidates != tuple(sorted(diagnostic.maximizers)):
        raise RuntimeError(f"top level does not equal M(C) at {perm}")
    if top.score != (diagnostic.primary_score, diagnostic.secondary_score):
        raise RuntimeError(f"top level score disagrees with the frozen score at {perm}")

    _, relation = score_candidates(perm)
    automorphisms = tie_aut.exact_automorphisms(relation)
    if landscape.n_automorphisms != len(automorphisms):
        raise RuntimeError(f"automorphism order mismatch at {perm}")
    if len(automorphisms) != diagnostic.n_automorphisms:
        raise RuntimeError(f"automorphism order disagrees with the frozen one at {perm}")

    for level in landscape.levels:
        # 3. the orbit partition covers the level exactly once.
        members = [candidate for orbit in level.orbits for candidate in orbit]
        if len(members) != level.candidate_count or set(members) != set(level.candidates):
            raise RuntimeError(f"orbit partition does not cover level {level.score} at {perm}")
        if sum(level.orbit_sizes) != level.candidate_count:
            raise RuntimeError(f"orbit sizes do not sum to the level size at {perm}")

        # 4. the level is closed under every automorphism.
        level_set = set(level.candidates)
        for automorphism in automorphisms:
            for candidate in level.candidates:
                if tie_aut.act_on_candidate(automorphism, candidate) not in level_set:
                    raise RuntimeError(f"level {level.score} is not Aut-closed at {perm}")

    # 5. the top-level orbit count reproduces the frozen diagnostic.
    if top.orbit_count != diagnostic.n_orbits:
        raise RuntimeError(f"top-level orbit count disagrees with n_orbits at {perm}")


def encode_permutation(permutation: Sequence[int]) -> str:
    values = [int(value) for value in permutation]
    if any(not 0 <= value <= 9 for value in values):
        raise ValueError("one-digit encoding requires every image in 0..9")
    return "".join(str(value) for value in values)


def landscape_rows(landscape: PermutationLandscape) -> list[dict[str, object]]:
    """Long format: one row per (permutation, level); one NA row when Q(C) is empty."""

    base: dict[str, object] = {
        "n": landscape.n,
        "permutation": encode_permutation(landscape.permutation),
        "n_candidates": landscape.n_candidates,
        "n_score_levels": landscape.n_score_levels,
        "n_automorphisms": landscape.n_automorphisms,
        "candidates_available": int(landscape.n_candidates > 0),
    }
    if not landscape.levels:
        return [
            {
                **base,
                "level_index": None,
                "primary_score": None,
                "secondary_score": None,
                "candidate_count": None,
                "orbit_count": None,
                "orbit_sizes": None,
            }
        ]
    return [
        {
            **base,
            "level_index": index,
            "primary_score": level.primary_score,
            "secondary_score": level.secondary_score,
            "candidate_count": level.candidate_count,
            "orbit_count": level.orbit_count,
            "orbit_sizes": "-".join(str(size) for size in level.orbit_sizes),
        }
        for index, level in enumerate(landscape.levels)
    ]


@dataclass
class LandscapeAggregate:
    """Purely static per-n summary.  No external variable enters any field."""

    n: int
    permutations: int = 0
    empty: int = 0
    rows: int = 0

    def __post_init__(self) -> None:
        self.n_candidates_counts: Counter[int] = Counter()
        self.n_score_levels_counts: Counter[int] = Counter()
        self.top_level_candidate_counts: Counter[int] = Counter()
        self.top_level_orbit_counts: Counter[int] = Counter()
        self.orbit_count_by_level_index: dict[int, Counter[int]] = {}
        self.orbit_count_all_levels: Counter[int] = Counter()
        self.candidate_count_all_levels: Counter[int] = Counter()
        self.automorphism_order_counts_nonempty: Counter[int] = Counter()
        self.primary_score_top_counts: Counter[int] = Counter()
        self.secondary_score_top_counts: Counter[int] = Counter()

    def add(self, landscape: PermutationLandscape, rows: int) -> None:
        self.permutations += 1
        self.rows += rows
        self.n_candidates_counts[landscape.n_candidates] += 1
        self.n_score_levels_counts[landscape.n_score_levels] += 1
        if landscape.n_candidates == 0:
            self.empty += 1
            return
        assert landscape.n_automorphisms is not None
        self.automorphism_order_counts_nonempty[landscape.n_automorphisms] += 1
        top = landscape.levels[0]
        self.top_level_candidate_counts[top.candidate_count] += 1
        self.top_level_orbit_counts[top.orbit_count] += 1
        self.primary_score_top_counts[top.primary_score] += 1
        self.secondary_score_top_counts[top.secondary_score] += 1
        for index, level in enumerate(landscape.levels):
            bucket = self.orbit_count_by_level_index.setdefault(index, Counter())
            bucket[level.orbit_count] += 1
            self.orbit_count_all_levels[level.orbit_count] += 1
            self.candidate_count_all_levels[level.candidate_count] += 1

    def as_dict(self) -> dict[str, object]:
        def ordered(counter: Counter) -> dict[str, int]:
            return {str(key): counter[key] for key in sorted(counter)}

        nonempty = self.permutations - self.empty
        return {
            "n": self.n,
            "permutations": self.permutations,
            "permutations_with_empty_candidate_set": self.empty,
            "permutations_with_candidates": nonempty,
            "landscape_rows": self.rows,
            "max_candidates": max(self.n_candidates_counts, default=0),
            "max_score_levels": max(self.n_score_levels_counts, default=0),
            "n_candidates_distribution": ordered(self.n_candidates_counts),
            "n_score_levels_distribution": ordered(self.n_score_levels_counts),
            "top_level_candidate_count_distribution": ordered(
                self.top_level_candidate_counts
            ),
            "top_level_orbit_count_distribution": ordered(self.top_level_orbit_counts),
            "top_level_primary_score_distribution": ordered(self.primary_score_top_counts),
            "top_level_secondary_score_distribution": ordered(
                self.secondary_score_top_counts
            ),
            "orbit_count_distribution_all_levels": ordered(self.orbit_count_all_levels),
            "candidate_count_distribution_all_levels": ordered(
                self.candidate_count_all_levels
            ),
            "orbit_count_distribution_by_level_index": {
                str(index): ordered(self.orbit_count_by_level_index[index])
                for index in sorted(self.orbit_count_by_level_index)
            },
            "automorphism_order_counts_nonempty": ordered(
                self.automorphism_order_counts_nonempty
            ),
        }


def validate_aggregate(aggregate: LandscapeAggregate) -> None:
    expected = math.factorial(aggregate.n)
    if aggregate.permutations != expected:
        raise RuntimeError(f"factorial total mismatch at n={aggregate.n}")
    if sum(aggregate.n_candidates_counts.values()) != expected:
        raise RuntimeError(f"candidate distribution total mismatch at n={aggregate.n}")
    if sum(aggregate.n_score_levels_counts.values()) != expected:
        raise RuntimeError(f"level distribution total mismatch at n={aggregate.n}")
    if aggregate.n_candidates_counts[0] != aggregate.empty:
        raise RuntimeError(f"empty count mismatch at n={aggregate.n}")
    if aggregate.n_score_levels_counts[0] != aggregate.empty:
        raise RuntimeError(f"zero-level count mismatch at n={aggregate.n}")
    nonempty = expected - aggregate.empty
    if sum(aggregate.top_level_orbit_counts.values()) != nonempty:
        raise RuntimeError(f"top-level orbit total mismatch at n={aggregate.n}")
    if sum(aggregate.automorphism_order_counts_nonempty.values()) != nonempty:
        raise RuntimeError(f"automorphism order total mismatch at n={aggregate.n}")
    if aggregate.rows != aggregate.empty + sum(
        level * count for level, count in aggregate.n_score_levels_counts.items()
    ):
        raise RuntimeError(f"row accounting mismatch at n={aggregate.n}")


def enumerate_landscape(
    n_values: Iterable[int] = EXACT_N, *, validate: bool = True
) -> tuple[list[dict[str, object]], list[LandscapeAggregate]]:
    """Exhaustive static extraction over S_n.  No thinning, no target quantity."""

    n_sequence = tuple(int(n) for n in n_values)
    if not n_sequence or any(n not in EXACT_N for n in n_sequence):
        raise ValueError(f"n values must be a nonempty subset of {EXACT_N}")

    rows: list[dict[str, object]] = []
    aggregates: list[LandscapeAggregate] = []
    for n in n_sequence:
        aggregate = LandscapeAggregate(n=n)
        for permutation in permutations(range(n)):
            landscape = score_landscape(permutation)
            if validate:
                validate_landscape(landscape)
            permutation_rows = landscape_rows(landscape)
            rows.extend(permutation_rows)
            aggregate.add(landscape, len(permutation_rows))
        validate_aggregate(aggregate)
        aggregates.append(aggregate)
        print(
            "PAISAJE_NIVELES "
            f"N={n} PERMUTATIONS={aggregate.permutations} "
            f"EMPTY={aggregate.empty} "
            f"NONEMPTY={aggregate.permutations - aggregate.empty} "
            f"MAX_CANDIDATES={max(aggregate.n_candidates_counts, default=0)} "
            f"MAX_LEVELS={max(aggregate.n_score_levels_counts, default=0)} "
            f"ROWS={aggregate.rows}",
            flush=True,
        )
    return rows, aggregates


def _source_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def summary_payload(
    aggregates: Sequence[LandscapeAggregate], landscape_digest: str
) -> dict[str, object]:
    return {
        "artifact_schema": "P1A_PAISAJE_NIVELES_D2_V1",
        "result_status": "OBSERVED_REPRODUCIBLE_STATIC_LANDSCAPE",
        "scientific_scope": {
            "dimension": 2,
            "n": [aggregate.n for aggregate in aggregates],
            "law": "uniform enumeration of all permutations in S_n",
            "causal_set_construction": "product order of identity and permutation",
            "selector": comparison.MIN_COVERAGE_LEX,
            "k0": sealed.K0,
            "selector_score": ["min(m_minus,m_plus)", "m_minus+m_plus"],
            "score_order": "lexicographic, descending",
            "candidate": "ordered endpoint quadruple (a,b,c,d)",
            "extraction": (
                "complete list of distinct score levels over Q(C), with per-level "
                "candidate count and Aut(C)-orbit partition"
            ),
            "claim_ceiling": (
                "exact finite-n static landscape only; no coordinate proposal, no "
                "metric, no near-maximizer window, no asymptotic extrapolation and "
                "no statement about any thinning target"
            ),
        },
        "choice_free_extraction": {
            "top_k_fixed": False,
            "epsilon_window_fixed": False,
            "scalar_gap_defined": False,
            "primary_or_secondary_deficit_defined": False,
            "coordinate_weighting_defined": False,
            "fixed_dimension_summary_defined": False,
            "levels_defined_as": "every distinct value of S_C on Q(C), no truncation",
        },
        "target_guard": {
            "q_p_computed": False,
            "q_p_star_computed": False,
            "e_p_computed": False,
            "a_k_or_b_k_computed": False,
            "thinning_masks_enumerated": False,
            "induced_subposets_evaluated": False,
            "retention_used": False,
            "target_based_coordinate_selection": False,
            "xi_n_defined": False,
            "monte_carlo": False,
        },
        "level_semantics": {
            "levels_sorted": "descending lexicographic in (primary_score, secondary_score)",
            "level_index_0": "the argmax level, equal to M(C)",
            "empty_candidate_set": (
                "Q(C) empty is reported as one row with candidates_available=0 and "
                "every level field NA; it is never silently coerced to zero"
            ),
            "n_automorphisms_when_empty": (
                "NA; Aut(C) is not enumerated when Q(C) is empty, mirroring the frozen "
                "diagnostic which also skips it"
            ),
            "orbit_sizes": "hyphen-joined orbit cardinalities in descending order",
        },
        "permutation_encoding": PERMUTATION_ENCODING,
        "validation": {
            "per_permutation_guards": [
                "levels partition Q(C) exactly once",
                "score levels are distinct and descending",
                "top level equals M(C) from the frozen materialize_lex_maximizers",
                "top level score equals the frozen lexicographic score",
                "orbit partition covers each level exactly once",
                "orbit sizes sum to the level size",
                "every level is closed under every exact automorphism",
                "automorphism order equals the frozen diagnostic order",
                "top-level orbit count equals the frozen n_orbits",
            ],
            "exhaustive_over_all_permutations": True,
            "reference_instrument": "emergencia/p1a_tie_aut_diagnostic.py",
        },
        "provenance": {
            "generator": "emergencia/p1a_paisaje_niveles_d2.py",
            "generator_sha256": _source_sha256(),
            "frozen_instrument": "emergencia/p1a_tie_aut_diagnostic.py",
            "frozen_instrument_sha256": hashlib.sha256(
                Path(tie_aut.__file__).read_bytes()
            ).hexdigest(),
            "frozen_instrument_modified": False,
            "landscape_csv": LANDSCAPE_FILENAME,
            "landscape_csv_sha256": landscape_digest,
            "randomness": None,
            "new_dependencies": [],
        },
        "aggregates": [aggregate.as_dict() for aggregate in aggregates],
    }


def write_artifacts(
    rows: Sequence[dict[str, object]],
    aggregates: Sequence[LandscapeAggregate],
    output_dir: Path,
    *,
    overwrite: bool = False,
) -> list[tuple[Path, str]]:
    csv_bytes = comparison.rows_to_csv(rows, LANDSCAPE_FIELDS).encode("utf-8")
    csv_path = output_dir / LANDSCAPE_FILENAME
    csv_digest = comparison._write_with_sidecar(
        csv_path, csv_bytes, overwrite=overwrite
    )

    payload = summary_payload(aggregates, csv_digest)
    summary_bytes = (
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    summary_path = output_dir / SUMMARY_FILENAME
    summary_digest = comparison._write_with_sidecar(
        summary_path, summary_bytes, overwrite=overwrite
    )
    return [(csv_path, csv_digest), (summary_path, summary_digest)]


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--n",
        nargs="+",
        type=int,
        default=list(EXACT_N),
        help=f"exact sizes to enumerate; subset of {EXACT_N}",
    )
    parser.add_argument(
        "--write-artifact",
        action="store_true",
        help="write the landscape table and its summary with sha256 sidecars",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="artifact directory",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="replace existing artifacts and sidecars",
    )
    parser.add_argument(
        "--no-validate",
        action="store_true",
        help="skip the per-permutation cross-check against the frozen instrument",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    rows, aggregates = enumerate_landscape(args.n, validate=not args.no_validate)
    if args.write_artifact:
        for path, digest in write_artifacts(
            rows, aggregates, args.output_dir, overwrite=args.overwrite
        ):
            print(f"ARTIFACT={path} SHA256={digest}")
    else:
        print(
            json.dumps(
                {"aggregates": [aggregate.as_dict() for aggregate in aggregates]},
                indent=2,
                sort_keys=True,
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
