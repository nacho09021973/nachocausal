#!/usr/bin/env python3
"""Exact TIE/Aut instrumentation for the frozen MIN_COVERAGE_LEX selector.

This module is diagnostic-only.  It does not reinterpret or replace the existing
EMPTY/UNIQUE/TIE states.  For the complete maximizer set M(C), it computes the
componentwise action of Aut(C) on endpoint quadruples and reports
|M(C) / Aut(C)|.

Precommit retained verbatim in operational form:

    If TIE is dominated by r=1, the existing selector is still not unique.  A
    new orbit-valued output may deserve study; its magnitude would be Pr(r=1).
    If r>1 dominates, relevant ties survive the automorphism quotient and the
    global-rival problem is not explained by the fixed-point obstruction.
    If both have appreciable weight, they remain distinct mechanisms.

    PREDICTION: For n=7, TIE_AUT_ONLY count = 0.
    STATUS: conjectural finite-n prediction; intended to be falsified.

The prediction is metadata, not an assertion or a PASS/FAIL condition.  The exact
runner is deterministic and performs no Monte Carlo simulation.  Artifact publication
is explicit, atomic, and refuses overwrites by default.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from itertools import combinations, permutations
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_enumeracion_simulacion as sealed


DIAGNOSTIC_UNIQUE = "UNIQUE"
DIAGNOSTIC_TIE_AUT_ONLY = "TIE_AUT_ONLY"
DIAGNOSTIC_TIE_NONAUT = "TIE_NONAUT"
DIAGNOSTIC_STATES = (
    DIAGNOSTIC_UNIQUE,
    DIAGNOSTIC_TIE_AUT_ONLY,
    DIAGNOSTIC_TIE_NONAUT,
)

MAX_EXACT_N = 9
EXACT_N = (6, 7, 8, 9)
INDEPENDENT_CROSSCHECK_N = (6, 7)
PREDICTION_N = 7
PREDICTION_TIE_AUT_ONLY_COUNT = 0
PREDICTION_STATUS = "conjectural finite-n prediction; intended to be falsified"

HERE = Path(__file__).resolve().parent
REPOSITORY_ROOT = HERE.parent
DEFAULT_OUTPUT_DIR = HERE / "resultados"
ARTIFACT_FILENAME = "p1a_tie_aut_exacto_d2.json"
BASE_HEAD_BEFORE_TIE_AUT = "f6256b617d2234657992e2a1a32108667aeb1710"
ORIGIN_MAIN_AT_INSTRUMENTATION = "256d9e76fbed186463770af666602f8e592debcc"

Quadruple = tuple[int, int, int, int]
ElementPermutation = tuple[int, ...]
Relation = tuple[tuple[bool, ...], ...]
Score = tuple[int, int]


@dataclass(frozen=True)
class TieAutDiagnostic:
    """Parallel diagnostic attached to one existing selector outcome."""

    optimized_state: str
    diagnostic_state: str | None
    n_maximizers: int
    n_automorphisms: int | None
    n_orbits: int
    primary_score: int | None
    secondary_score: int | None
    maximizers: tuple[Quadruple, ...]
    orbits: tuple[tuple[Quadruple, ...], ...]


@dataclass
class ExactTieAutAggregate:
    """Exact permutation-weighted aggregate for one n."""

    n: int
    permutations: int = 0
    optimized_state_counts: Counter[str] = field(default_factory=Counter)
    diagnostic_state_counts: Counter[str] = field(default_factory=Counter)
    r_counts: Counter[int] = field(default_factory=Counter)
    tie_r_counts: Counter[int] = field(default_factory=Counter)
    n_maximizer_counts: Counter[int] = field(default_factory=Counter)
    automorphism_order_counts_nonempty: Counter[int] = field(default_factory=Counter)
    independent_crosschecks: int = 0

    def add(self, diagnostic: TieAutDiagnostic) -> None:
        self.permutations += 1
        self.optimized_state_counts[diagnostic.optimized_state] += 1
        self.n_maximizer_counts[diagnostic.n_maximizers] += 1
        if diagnostic.optimized_state == comparison.STATE_EMPTY:
            if diagnostic.diagnostic_state is not None or diagnostic.n_orbits != 0:
                raise RuntimeError("EMPTY outcome acquired a nonempty orbit diagnostic")
            self.r_counts[0] += 1
            return

        if diagnostic.diagnostic_state not in DIAGNOSTIC_STATES:
            raise RuntimeError("non-EMPTY outcome is missing a diagnostic state")
        if diagnostic.n_automorphisms is None:
            raise RuntimeError("non-EMPTY outcome is missing its automorphism order")
        self.diagnostic_state_counts[diagnostic.diagnostic_state] += 1
        self.r_counts[diagnostic.n_orbits] += 1
        self.automorphism_order_counts_nonempty[diagnostic.n_automorphisms] += 1
        if diagnostic.optimized_state == comparison.STATE_TIE:
            self.tie_r_counts[diagnostic.n_orbits] += 1

    def as_dict(self) -> dict[str, object]:
        nonempty = self.permutations - self.optimized_state_counts[comparison.STATE_EMPTY]
        ties = self.optimized_state_counts[comparison.STATE_TIE]

        def ordered(counter: Counter) -> dict[str, int]:
            return {str(key): counter[key] for key in sorted(counter)}

        def probabilities(counter: Counter, denominator: int) -> dict[str, float]:
            if denominator == 0:
                return {}
            return {
                str(key): counter[key] / denominator
                for key in sorted(counter)
            }

        return {
            "n": self.n,
            "permutations": self.permutations,
            "optimized_state_counts": ordered(self.optimized_state_counts),
            "diagnostic_state_counts": ordered(self.diagnostic_state_counts),
            "diagnostic_probability_all_permutations": probabilities(
                self.diagnostic_state_counts, self.permutations
            ),
            "diagnostic_probability_given_nonempty": probabilities(
                self.diagnostic_state_counts, nonempty
            ),
            "tie_decomposition_given_tie": probabilities(
                Counter(
                    {
                        DIAGNOSTIC_TIE_AUT_ONLY: self.diagnostic_state_counts[
                            DIAGNOSTIC_TIE_AUT_ONLY
                        ],
                        DIAGNOSTIC_TIE_NONAUT: self.diagnostic_state_counts[
                            DIAGNOSTIC_TIE_NONAUT
                        ],
                    }
                ),
                ties,
            ),
            "r_counts_all_permutations": ordered(self.r_counts),
            "r_probability_all_permutations": probabilities(
                self.r_counts, self.permutations
            ),
            "r_counts_given_tie": ordered(self.tie_r_counts),
            "r_probability_given_tie": probabilities(self.tie_r_counts, ties),
            "n_maximizer_counts": ordered(self.n_maximizer_counts),
            "automorphism_order_counts_nonempty": ordered(
                self.automorphism_order_counts_nonempty
            ),
            "independent_crosschecks": self.independent_crosschecks,
        }


def _as_relation(comparable: np.ndarray) -> Relation:
    relation = np.asarray(comparable, dtype=np.bool_)
    if relation.ndim != 2 or relation.shape[0] != relation.shape[1]:
        raise ValueError("expected a square strict-order relation")
    if bool(np.diag(relation).any()):
        raise ValueError("strict-order relation must be irreflexive")
    return tuple(tuple(bool(value) for value in row) for row in relation)


def _refine_colors(relation: Relation) -> tuple[int, ...]:
    """Exact automorphism-invariant 1-WL refinement.

    Adapted from ``dev/r3_bridge_e_fibers.py:refine_colors``.  Refinement only
    prunes impossible mappings; every surviving mapping is checked against the
    complete directed relation below.
    """

    n = len(relation)
    colors = [0] * n
    while True:
        signatures = []
        for i in range(n):
            down = sorted(colors[j] for j in range(n) if relation[j][i])
            up = sorted(colors[j] for j in range(n) if relation[i][j])
            signatures.append((colors[i], tuple(down), tuple(up)))
        palette = {
            signature: color
            for color, signature in enumerate(sorted(set(signatures)))
        }
        refined = [palette[signature] for signature in signatures]
        if refined == colors:
            return tuple(colors)
        colors = refined


def exact_automorphisms(relation: Relation) -> tuple[ElementPermutation, ...]:
    """Enumerate every relation-preserving relabeling exactly for n <= 9."""

    n = len(relation)
    if n == 0 or any(len(row) != n for row in relation):
        raise ValueError("expected a nonempty square relation")
    if n > MAX_EXACT_N:
        raise ValueError(f"exact TIE/Aut instrumentation is limited to n<={MAX_EXACT_N}")

    colors = _refine_colors(relation)
    classes: defaultdict[int, list[int]] = defaultdict(list)
    for element, color in enumerate(colors):
        classes[color].append(element)
    blocks = [tuple(classes[color]) for color in sorted(classes)]

    mapping = list(range(n))
    found: list[ElementPermutation] = []

    def build(block_index: int) -> None:
        if block_index == len(blocks):
            candidate = tuple(mapping)
            if all(
                relation[i][j] == relation[candidate[i]][candidate[j]]
                for i in range(n)
                for j in range(n)
            ):
                found.append(candidate)
            return

        sources = blocks[block_index]
        for images in permutations(sources):
            for source, image in zip(sources, images):
                mapping[source] = image
            build(block_index + 1)

    build(0)
    automorphisms = tuple(sorted(set(found)))
    identity = tuple(range(n))
    if identity not in automorphisms:
        raise RuntimeError("exact automorphism enumeration lost the identity")
    return automorphisms


def act_on_candidate(
    automorphism: ElementPermutation, candidate: Quadruple
) -> Quadruple:
    """Apply an order automorphism componentwise to (a,b,c,d)."""

    if sorted(automorphism) != list(range(len(automorphism))):
        raise ValueError("automorphism must be a permutation of the element set")
    if any(not 0 <= element < len(automorphism) for element in candidate):
        raise ValueError("candidate endpoint outside the automorphism domain")
    a, b, c, d = candidate
    return automorphism[a], automorphism[b], automorphism[c], automorphism[d]


def materialize_lex_maximizers(
    permutation: Sequence[int],
) -> tuple[Relation, tuple[Quadruple, ...], Score | None]:
    """Materialize the exact MIN_COVERAGE_LEX argmax set M(C)."""

    perm = sealed.validate_permutation(permutation)
    if len(perm) > MAX_EXACT_N:
        raise ValueError(f"exact TIE/Aut instrumentation is limited to n<={MAX_EXACT_N}")
    counts, comparable = sealed.interval_count_matrix(perm)
    relation = _as_relation(comparable)

    scored: list[tuple[Quadruple, Score]] = []
    for a, b, c, d in combinations(range(len(perm)), 4):
        if not (comparable[a, b] and comparable[b, c] and comparable[c, d]):
            continue
        past = int(counts[a, b])
        future = int(counts[c, d])
        if past < sealed.K0 or future < sealed.K0:
            continue
        scored.append(((a, b, c, d), (min(past, future), past + future)))

    if not scored:
        return relation, (), None
    best_score = max(score for _, score in scored)
    maximizers = tuple(
        candidate for candidate, score in scored if score == best_score
    )
    return relation, maximizers, best_score


def _interval_size_naive(permutation: Sequence[int], i: int, j: int) -> int:
    if not (i < j and permutation[i] < permutation[j]):
        return 0
    return sum(
        i <= element <= j
        and permutation[i] <= permutation[element] <= permutation[j]
        for element in range(len(permutation))
    )


def materialize_lex_maximizers_naive(
    permutation: Sequence[int],
) -> tuple[tuple[Quadruple, ...], Score | None]:
    """Independent direct definition used for exhaustive n=6,7 crosschecks."""

    perm = tuple(int(value) for value in permutation)
    if sorted(perm) != list(range(len(perm))):
        raise ValueError("expected a permutation of range(n)")

    scored: list[tuple[Quadruple, Score]] = []
    for a, b, c, d in combinations(range(len(perm)), 4):
        if not perm[a] < perm[b] < perm[c] < perm[d]:
            continue
        past = _interval_size_naive(perm, a, b)
        future = _interval_size_naive(perm, c, d)
        if past < sealed.K0 or future < sealed.K0:
            continue
        scored.append(((a, b, c, d), (min(past, future), past + future)))

    if not scored:
        return (), None
    best_score = max(score for _, score in scored)
    maximizers = tuple(
        candidate for candidate, score in scored if score == best_score
    )
    return maximizers, best_score


def _orbit_partition(
    maximizers: tuple[Quadruple, ...],
    automorphisms: tuple[ElementPermutation, ...],
) -> tuple[tuple[Quadruple, ...], ...]:
    maximizer_set = set(maximizers)

    for automorphism in automorphisms:
        for candidate in maximizers:
            image = act_on_candidate(automorphism, candidate)
            if image not in maximizer_set:
                raise RuntimeError("automorphism image escaped the maximizer set")

    remaining = set(maximizers)
    orbits: list[tuple[Quadruple, ...]] = []
    while remaining:
        representative = min(remaining)
        orbit = {
            act_on_candidate(automorphism, representative)
            for automorphism in automorphisms
        }
        if not orbit <= maximizer_set:
            raise RuntimeError("candidate orbit escaped the maximizer set")
        orbits.append(tuple(sorted(orbit)))
        remaining -= orbit

    partition = tuple(sorted(orbits))
    flattened = [candidate for orbit in partition for candidate in orbit]
    if len(flattened) != len(maximizers) or set(flattened) != maximizer_set:
        raise RuntimeError("orbit partition does not cover M(C) exactly once")
    return partition


def evaluate_tie_aut(permutation: Sequence[int]) -> TieAutDiagnostic:
    """Compute the parallel TIE/Aut diagnostic for one permutation."""

    optimized = comparison.evaluate_selectors(permutation)[comparison.MIN_COVERAGE_LEX]
    relation, maximizers, best_score = materialize_lex_maximizers(permutation)

    if len(maximizers) != optimized.n_maximizers:
        raise RuntimeError("len(M) does not equal optimized lex_nmax")

    if optimized.state == comparison.STATE_EMPTY:
        if maximizers or best_score is not None or optimized.n_maximizers != 0:
            raise RuntimeError("EMPTY state disagrees with the materialized argmax set")
        return TieAutDiagnostic(
            optimized_state=optimized.state,
            diagnostic_state=None,
            n_maximizers=0,
            n_automorphisms=None,
            n_orbits=0,
            primary_score=None,
            secondary_score=None,
            maximizers=(),
            orbits=(),
        )

    if best_score is None:
        raise RuntimeError("non-EMPTY state is missing a best lexicographic score")
    if best_score != (optimized.primary_score, optimized.secondary_score):
        raise RuntimeError("materialized and optimized lexicographic scores disagree")

    automorphisms = exact_automorphisms(relation)
    orbits = _orbit_partition(maximizers, automorphisms)

    if len(maximizers) == 1:
        diagnostic_state = DIAGNOSTIC_UNIQUE
    elif len(orbits) == 1:
        diagnostic_state = DIAGNOSTIC_TIE_AUT_ONLY
    else:
        diagnostic_state = DIAGNOSTIC_TIE_NONAUT

    if (diagnostic_state == DIAGNOSTIC_UNIQUE) != (
        optimized.state == comparison.STATE_UNIQUE
    ):
        raise RuntimeError("diagnostic UNIQUE does not match STATE_UNIQUE")
    if diagnostic_state in (DIAGNOSTIC_TIE_AUT_ONLY, DIAGNOSTIC_TIE_NONAUT):
        if optimized.state != comparison.STATE_TIE:
            raise RuntimeError("orbit diagnostic TIE does not match STATE_TIE")
    if optimized.state == comparison.STATE_UNIQUE:
        if optimized.selection is None:
            raise RuntimeError("STATE_UNIQUE is missing the existing selection")
        if optimized.selection.quadruple != maximizers[0]:
            raise RuntimeError("existing unique selection disagrees with M(C)")

    return TieAutDiagnostic(
        optimized_state=optimized.state,
        diagnostic_state=diagnostic_state,
        n_maximizers=len(maximizers),
        n_automorphisms=len(automorphisms),
        n_orbits=len(orbits),
        primary_score=best_score[0],
        secondary_score=best_score[1],
        maximizers=maximizers,
        orbits=orbits,
    )


def validate_exact_aggregate(aggregate: ExactTieAutAggregate) -> None:
    expected = math.factorial(aggregate.n)
    if aggregate.permutations != expected:
        raise RuntimeError(f"factorial total mismatch at n={aggregate.n}")
    if sum(aggregate.optimized_state_counts.values()) != expected:
        raise RuntimeError(f"optimized state partition mismatch at n={aggregate.n}")

    empty = aggregate.optimized_state_counts[comparison.STATE_EMPTY]
    unique = aggregate.optimized_state_counts[comparison.STATE_UNIQUE]
    ties = aggregate.optimized_state_counts[comparison.STATE_TIE]
    if empty + unique + ties != expected:
        raise RuntimeError(f"EMPTY/UNIQUE/TIE partition mismatch at n={aggregate.n}")
    if sum(aggregate.diagnostic_state_counts.values()) != expected - empty:
        raise RuntimeError(f"nonempty diagnostic partition mismatch at n={aggregate.n}")
    if aggregate.diagnostic_state_counts[DIAGNOSTIC_UNIQUE] != unique:
        raise RuntimeError(f"UNIQUE diagnostic mismatch at n={aggregate.n}")
    if (
        aggregate.diagnostic_state_counts[DIAGNOSTIC_TIE_AUT_ONLY]
        + aggregate.diagnostic_state_counts[DIAGNOSTIC_TIE_NONAUT]
        != ties
    ):
        raise RuntimeError(f"TIE diagnostic partition mismatch at n={aggregate.n}")
    if sum(aggregate.r_counts.values()) != expected:
        raise RuntimeError(f"r distribution total mismatch at n={aggregate.n}")
    if aggregate.r_counts[0] != empty:
        raise RuntimeError(f"r=0 does not reproduce EMPTY at n={aggregate.n}")
    if (
        aggregate.r_counts[1]
        != unique + aggregate.diagnostic_state_counts[DIAGNOSTIC_TIE_AUT_ONLY]
    ):
        raise RuntimeError(f"r=1 partition mismatch at n={aggregate.n}")
    if sum(aggregate.tie_r_counts.values()) != ties:
        raise RuntimeError(f"conditional TIE r distribution mismatch at n={aggregate.n}")
    if (
        aggregate.tie_r_counts[1]
        != aggregate.diagnostic_state_counts[DIAGNOSTIC_TIE_AUT_ONLY]
    ):
        raise RuntimeError(f"TIE_AUT_ONLY does not equal tied r=1 at n={aggregate.n}")
    if (
        sum(count for r, count in aggregate.tie_r_counts.items() if r > 1)
        != aggregate.diagnostic_state_counts[DIAGNOSTIC_TIE_NONAUT]
    ):
        raise RuntimeError(f"TIE_NONAUT does not equal tied r>1 at n={aggregate.n}")

    expected_crosschecks = expected if aggregate.n in INDEPENDENT_CROSSCHECK_N else 0
    if aggregate.independent_crosschecks != expected_crosschecks:
        raise RuntimeError(f"independent crosscheck total mismatch at n={aggregate.n}")


def enumerate_exact(
    n_values: Iterable[int] = INDEPENDENT_CROSSCHECK_N,
) -> list[ExactTieAutAggregate]:
    """Enumerate the authorized exact permutation law, with n=6,7 crosschecks."""

    n_sequence = tuple(int(n) for n in n_values)
    if not n_sequence or any(n not in EXACT_N for n in n_sequence):
        raise ValueError(f"n values must be a nonempty subset of {EXACT_N}")

    aggregates: list[ExactTieAutAggregate] = []
    for n in n_sequence:
        aggregate = ExactTieAutAggregate(n=n)
        for permutation in permutations(range(n)):
            diagnostic = evaluate_tie_aut(permutation)
            if n in INDEPENDENT_CROSSCHECK_N:
                naive_maximizers, naive_score = materialize_lex_maximizers_naive(
                    permutation
                )
                if (
                    naive_maximizers != diagnostic.maximizers
                    or naive_score
                    != (
                        None
                        if diagnostic.primary_score is None
                        else (diagnostic.primary_score, diagnostic.secondary_score)
                    )
                ):
                    raise RuntimeError(
                        "independent naive M(C) mismatch "
                        f"at n={n}, permutation={permutation}"
                    )
                aggregate.independent_crosschecks += 1
            aggregate.add(diagnostic)

        validate_exact_aggregate(aggregate)
        aggregates.append(aggregate)
        print(
            "TIE_AUT_EXACT "
            f"N={n} PERMUTATIONS={aggregate.permutations} "
            f"EMPTY={aggregate.optimized_state_counts[comparison.STATE_EMPTY]} "
            f"UNIQUE={aggregate.diagnostic_state_counts[DIAGNOSTIC_UNIQUE]} "
            "TIE_AUT_ONLY="
            f"{aggregate.diagnostic_state_counts[DIAGNOSTIC_TIE_AUT_ONLY]} "
            f"TIE_NONAUT={aggregate.diagnostic_state_counts[DIAGNOSTIC_TIE_NONAUT]}",
            flush=True,
        )
    return aggregates


def _source_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def frozen_artifact_payload(
    aggregates: Sequence[ExactTieAutAggregate],
) -> dict[str, object]:
    """Build the deterministic finite-n artifact; no asymptotic claim is encoded."""

    if tuple(aggregate.n for aggregate in aggregates) != EXACT_N:
        raise ValueError(f"frozen artifact requires exactly n={EXACT_N}")
    for aggregate in aggregates:
        validate_exact_aggregate(aggregate)

    n7 = next(aggregate for aggregate in aggregates if aggregate.n == PREDICTION_N)
    observed_n7 = n7.diagnostic_state_counts[DIAGNOSTIC_TIE_AUT_ONLY]
    return {
        "artifact_schema": "P1A_TIE_AUT_EXACT_D2_V1",
        "result_status": "OBSERVED_REPRODUCIBLE_FROZEN_FINITE_N",
        "scientific_scope": {
            "dimension": 2,
            "n": list(EXACT_N),
            "law": "uniform enumeration of all permutations in S_n",
            "causal_set_construction": "product order of identity and permutation",
            "selector": comparison.MIN_COVERAGE_LEX,
            "selector_score": ["min(m_minus,m_plus)", "m_minus+m_plus"],
            "candidate": "ordered endpoint quadruple (a,b,c,d)",
            "claim_ceiling": (
                "exact finite-n decomposition only; no asymptotic extrapolation, "
                "no THINNING-RG conclusion, and no temporal interpretation"
            ),
        },
        "state_semantics": {
            "changed": False,
            "original_states_retained": [
                comparison.STATE_EMPTY,
                comparison.STATE_UNIQUE,
                comparison.STATE_TIE,
            ],
            "diagnostic_states": list(DIAGNOSTIC_STATES),
            "definitions": {
                DIAGNOSTIC_UNIQUE: "|M(C)| = 1",
                DIAGNOSTIC_TIE_AUT_ONLY: "|M(C)| > 1 and |M(C)/Aut(C)| = 1",
                DIAGNOSTIC_TIE_NONAUT: "|M(C)/Aut(C)| > 1",
            },
        },
        "orbit_action": {
            "formula": "alpha.(a,b,c,d)=(alpha(a),alpha(b),alpha(c),alpha(d))",
            "automorphisms": "all exact relation-preserving element relabelings",
            "candidate_invariance_checked": True,
        },
        "precommit": {
            "interpretation": [
                (
                    "If TIE is dominated by r=1, the existing selector is still not "
                    "unique; an orbit-valued output may deserve study, with magnitude "
                    "Pr(r=1)."
                ),
                (
                    "If r>1 dominates, relevant ties survive the automorphism quotient "
                    "and the global-rival problem is not explained by the fixed-point "
                    "obstruction."
                ),
                "If both have appreciable weight, they remain distinct mechanisms.",
            ],
            "prediction": {
                "n": PREDICTION_N,
                "tie_aut_only_count": PREDICTION_TIE_AUT_ONLY_COUNT,
                "status": PREDICTION_STATUS,
                "used_as_assert_or_terminal": False,
                "observed_count": observed_n7,
                "falsified_by_exact_result": (
                    observed_n7 != PREDICTION_TIE_AUT_ONLY_COUNT
                ),
            },
        },
        "validation": {
            "aggregate_guards_passed": True,
            "per_permutation_guards": [
                "diagnostic UNIQUE iff STATE_UNIQUE",
                "TIE_AUT_ONLY implies STATE_TIE",
                "TIE_NONAUT implies STATE_TIE",
                "len(M) equals lex_nmax",
                "materialized best score equals optimized lex score",
                "orbit partition size equals len(M)",
                "alpha(q) is in M for every exact automorphism and q in M",
                "original UNIQUE candidate equals the sole element of M",
            ],
            "independent_naive_M_crosscheck_n": list(INDEPENDENT_CROSSCHECK_N),
            "independent_naive_M_crosschecks": {
                str(aggregate.n): aggregate.independent_crosschecks
                for aggregate in aggregates
            },
        },
        "provenance": {
            "generator": "emergencia/p1a_tie_aut_diagnostic.py",
            "generator_sha256": _source_sha256(),
            "tests": "tests/test_p1a_tie_aut_diagnostic.py",
            "base_head_before_tie_aut": BASE_HEAD_BEFORE_TIE_AUT,
            "origin_main_at_instrumentation": ORIGIN_MAIN_AT_INSTRUMENTATION,
            "command": (
                "python -m emergencia.p1a_tie_aut_diagnostic "
                "--n 6 7 8 9 --write-artifact"
            ),
            "new_dependencies": [],
            "networkx_used": False,
            "randomness": None,
        },
        "aggregates": [aggregate.as_dict() for aggregate in aggregates],
    }


def frozen_artifact_bytes(
    aggregates: Sequence[ExactTieAutAggregate],
) -> bytes:
    payload = frozen_artifact_payload(aggregates)
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _atomic_write(path: Path, data: bytes, *, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"refusing to overwrite existing artifact: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    temporary.write_bytes(data)
    temporary.replace(path)


def write_frozen_artifact(
    aggregates: Sequence[ExactTieAutAggregate],
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    *,
    overwrite: bool = False,
) -> tuple[Path, str]:
    path = output_dir / ARTIFACT_FILENAME
    sidecar = path.with_suffix(path.suffix + ".sha256")
    if not overwrite:
        existing = [candidate for candidate in (path, sidecar) if candidate.exists()]
        if existing:
            raise FileExistsError(
                "refusing to overwrite: " + ", ".join(str(item) for item in existing)
            )
    data = frozen_artifact_bytes(aggregates)
    digest = hashlib.sha256(data).hexdigest()
    _atomic_write(path, data, overwrite=overwrite)
    _atomic_write(
        sidecar,
        f"{digest}  {path.name}\n".encode("utf-8"),
        overwrite=overwrite,
    )
    return path, digest


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--n",
        nargs="+",
        type=int,
        default=list(INDEPENDENT_CROSSCHECK_N),
        help=f"exact sizes to enumerate; subset of {EXACT_N}",
    )
    parser.add_argument(
        "--write-artifact",
        action="store_true",
        help="freeze the complete n=6,7,8,9 result with a sha256 sidecar",
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
        help="replace an existing artifact and sidecar",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    aggregates = enumerate_exact(args.n)
    if args.write_artifact:
        path, digest = write_frozen_artifact(
            aggregates, args.output_dir, overwrite=args.overwrite
        )
        print(f"ARTIFACT={path} SHA256={digest}")
        payload = frozen_artifact_payload(aggregates)
    else:
        payload = {
            "instrument": "TIE_AUT_MIN_COVERAGE_LEX_EXACT",
            "prediction": {
                "n": PREDICTION_N,
                "tie_aut_only_count": PREDICTION_TIE_AUT_ONLY_COUNT,
                "status": PREDICTION_STATUS,
                "used_as_assert_or_terminal": False,
            },
            "aggregates": [aggregate.as_dict() for aggregate in aggregates],
        }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
