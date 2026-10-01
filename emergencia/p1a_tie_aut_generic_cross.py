#!/usr/bin/env python3
"""Exact bounded instrumentation for the generic core--padding surgery D_x(kappa).

This module does not enumerate permutation spaces and does not modify the frozen
MIN_COVERAGE_LEX selector.  For one bad core ``kappa`` (size at most nine) and one
core index ``x``, it realizes a non-boundary core--antichain transposition with a
large class of indistinguishable intermediate padding elements.  It then computes
the complete maximizer set and its orbit count under the exact induced automorphism
action.

The padding class has size ``m + 2``, greater than the number ``m + 1`` of all
remaining vertices.  Its internal symmetric group acts trivially on candidates.
The class is therefore collapsed to one distinguished vertex only for exact
automorphism enumeration; scores and maximizers are always computed on the full
expanded permutation.

No asymptotic conclusion is encoded.  A future exhaustive search over B_7, B_8,
or B_9 is deliberately outside this instrumentation-only module.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Sequence

import numpy as np

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_tie_aut_diagnostic as tie_aut


MAX_CORE_N = 9

Quadruple = tuple[int, int, int, int]
ElementPermutation = tuple[int, ...]
Relation = tuple[tuple[bool, ...], ...]
Score = tuple[int, int]


@dataclass(frozen=True)
class GenericCrossRealization:
    """Concrete non-boundary padding realization of D_x(kappa)."""

    core: tuple[int, ...]
    core_index: int
    permutation: tuple[int, ...]
    low_index: int
    high_index: int
    middle_indices: tuple[int, ...]


@dataclass(frozen=True)
class GenericCrossDiagnostic:
    """Exact orbit diagnostic for one generic core--padding surgery."""

    core: tuple[int, ...]
    core_index: int
    expanded_size: int
    middle_size: int
    optimized_state: str
    diagnostic_state: str | None
    n_maximizers: int
    n_orbits: int
    n_skeleton_automorphisms: int | None
    primary_score: int | None
    secondary_score: int | None
    maximizers: tuple[Quadruple, ...]
    orbits: tuple[tuple[Quadruple, ...], ...]

    @property
    def is_good(self) -> bool:
        return self.n_orbits == 1


@dataclass(frozen=True)
class GenericCrossSummary:
    """The finite repairability coefficient a(kappa)."""

    core: tuple[int, ...]
    diagnostics: tuple[GenericCrossDiagnostic, ...]
    repairable_indices: tuple[int, ...]

    @property
    def a(self) -> int:
        return len(self.repairable_indices)


def generic_cross_realization(
    core: Sequence[int], core_index: int
) -> GenericCrossRealization:
    """Realize a generic, non-boundary core--antichain transposition.

    Start from ``core shifted above reverse(padding)``.  The last padding value
    (zero) is exchanged with ``core_index``.  The other ``m+2`` padding elements
    become exact twins strictly between the new low point L and high point H.
    """

    validated = tuple(int(value) for value in sealed.validate_permutation(core))
    m = len(validated)
    if m > MAX_CORE_N:
        raise ValueError(f"generic cross diagnostics require core size <= {MAX_CORE_N}")
    if not 0 <= core_index < m:
        raise ValueError("core index outside the core")

    middle_size = m + 2
    padding_size = middle_size + 1
    padded = tuple(value + padding_size for value in validated) + tuple(
        reversed(range(padding_size))
    )
    high_index = len(padded) - 1
    expanded = list(padded)
    expanded[core_index], expanded[high_index] = (
        expanded[high_index],
        expanded[core_index],
    )
    realization = GenericCrossRealization(
        core=validated,
        core_index=core_index,
        permutation=tuple(expanded),
        low_index=core_index,
        high_index=high_index,
        middle_indices=tuple(range(m, high_index)),
    )
    _validate_generic_padding_geometry(realization)
    return realization


def _validate_generic_padding_geometry(realization: GenericCrossRealization) -> None:
    _, comparable = sealed.interval_count_matrix(realization.permutation)
    low = realization.low_index
    high = realization.high_index
    middle = realization.middle_indices
    m = len(realization.core)

    if len(middle) != m + 2:
        raise RuntimeError("generic padding class does not have size m+2")
    if not all(comparable[low, item] and comparable[item, high] for item in middle):
        raise RuntimeError("generic padding does not satisfy L < T < H")
    if any(
        comparable[first, second] or comparable[second, first]
        for first, second in combinations(middle, 2)
    ):
        raise RuntimeError("generic middle padding is not an antichain")
    for item in middle:
        strict_past = set(np.flatnonzero(comparable[:, item]).tolist())
        strict_future = set(np.flatnonzero(comparable[item, :]).tolist())
        if strict_past != {low} or strict_future != {high}:
            raise RuntimeError("middle padding acquired a non-generic relation")


def _materialize_expanded_maximizers(
    permutation: Sequence[int],
) -> tuple[np.ndarray, np.ndarray, tuple[Quadruple, ...], Score | None]:
    counts, comparable = sealed.interval_count_matrix(permutation)
    scored: list[tuple[Quadruple, Score]] = []
    for a, b, c, d in combinations(range(len(permutation)), 4):
        if not (comparable[a, b] and comparable[b, c] and comparable[c, d]):
            continue
        past = int(counts[a, b])
        future = int(counts[c, d])
        if past < sealed.K0 or future < sealed.K0:
            continue
        scored.append(((a, b, c, d), (min(past, future), past + future)))
    if not scored:
        return counts, comparable, (), None
    best_score = max(score for _, score in scored)
    maximizers = tuple(
        candidate for candidate, score in scored if score == best_score
    )
    return counts, comparable, maximizers, best_score


def _refine_colored(
    relation: Relation, initial_colors: Sequence[int]
) -> tuple[int, ...]:
    n = len(relation)
    if len(initial_colors) != n:
        raise ValueError("one initial color is required per relation vertex")
    colors = [int(color) for color in initial_colors]
    while True:
        signatures = []
        for vertex in range(n):
            down = sorted(colors[other] for other in range(n) if relation[other][vertex])
            up = sorted(colors[other] for other in range(n) if relation[vertex][other])
            signatures.append((colors[vertex], tuple(down), tuple(up)))
        palette = {
            signature: color
            for color, signature in enumerate(sorted(set(signatures)))
        }
        refined = [palette[signature] for signature in signatures]
        if refined == colors:
            return tuple(colors)
        colors = refined


def _exact_colored_automorphisms(
    relation: Relation, initial_colors: Sequence[int]
) -> tuple[ElementPermutation, ...]:
    """Enumerate color- and relation-preserving relabelings with partial pruning."""

    n = len(relation)
    if n == 0 or any(len(row) != n for row in relation):
        raise ValueError("expected a nonempty square relation")
    colors = _refine_colored(relation, initial_colors)
    color_classes = {
        color: tuple(vertex for vertex, observed in enumerate(colors) if observed == color)
        for color in sorted(set(colors))
    }
    source_order = tuple(
        sorted(range(n), key=lambda vertex: (len(color_classes[colors[vertex]]), colors[vertex], vertex))
    )
    mapping = [-1] * n
    used: set[int] = set()
    found: list[ElementPermutation] = []

    def build(depth: int) -> None:
        if depth == n:
            found.append(tuple(mapping))
            return
        source = source_order[depth]
        for image in color_classes[colors[source]]:
            if image in used:
                continue
            if any(
                relation[source][previous] != relation[image][mapping[previous]]
                or relation[previous][source] != relation[mapping[previous]][image]
                for previous in source_order[:depth]
            ):
                continue
            mapping[source] = image
            used.add(image)
            build(depth + 1)
            used.remove(image)
            mapping[source] = -1

    build(0)
    automorphisms = tuple(sorted(found))
    if tuple(range(n)) not in automorphisms:
        raise RuntimeError("colored automorphism enumeration lost the identity")
    return automorphisms


def generic_cross_diagnostic(
    core: Sequence[int], core_index: int
) -> GenericCrossDiagnostic:
    """Compute r(D_x(kappa)) for one bad core and one generic cross surgery."""

    validated = tuple(int(value) for value in sealed.validate_permutation(core))
    base = tie_aut.evaluate_tie_aut(validated)
    if base.diagnostic_state != tie_aut.DIAGNOSTIC_TIE_NONAUT:
        raise ValueError("generic cross diagnostics require a TIE_NONAUT core")
    return _generic_cross_diagnostic_validated_bad(validated, core_index)


def _generic_cross_diagnostic_validated_bad(
    validated: tuple[int, ...], core_index: int
) -> GenericCrossDiagnostic:
    """Evaluate D_x after the caller has established that the core is bad."""

    realization = generic_cross_realization(validated, core_index)
    _, comparable, maximizers, best_score = _materialize_expanded_maximizers(
        realization.permutation
    )
    optimized = comparison.evaluate_selectors(realization.permutation)[
        comparison.MIN_COVERAGE_LEX
    ]
    if len(maximizers) != optimized.n_maximizers:
        raise RuntimeError("generic expanded M does not equal optimized lex_nmax")
    if best_score is None:
        if optimized.state != comparison.STATE_EMPTY:
            raise RuntimeError("generic expanded EMPTY state mismatch")
        return GenericCrossDiagnostic(
            core=validated,
            core_index=core_index,
            expanded_size=len(realization.permutation),
            middle_size=len(realization.middle_indices),
            optimized_state=optimized.state,
            diagnostic_state=None,
            n_maximizers=0,
            n_orbits=0,
            n_skeleton_automorphisms=None,
            primary_score=None,
            secondary_score=None,
            maximizers=(),
            orbits=(),
        )
    if best_score != (optimized.primary_score, optimized.secondary_score):
        raise RuntimeError("generic expanded and optimized scores disagree")
    if any(
        endpoint in realization.middle_indices
        for candidate in maximizers
        for endpoint in candidate
    ):
        raise RuntimeError("generic middle padding entered a maximizing candidate")

    m = len(validated)
    representative_middle = realization.middle_indices[0]
    keep = tuple(range(m)) + (realization.high_index, representative_middle)
    compressed = comparable[np.ix_(keep, keep)]
    relation = tie_aut._as_relation(compressed)
    # The collapsed middle module is distinguished.  Its size m+2 is larger than
    # the entire complement, so the full expanded action on candidate endpoints
    # is exactly the action of these color-preserving skeleton automorphisms.
    initial_colors = (0,) * (m + 1) + (1,)
    automorphisms = _exact_colored_automorphisms(relation, initial_colors)

    full_to_skeleton = {full: skeleton for skeleton, full in enumerate(keep)}
    skeleton_to_full = {skeleton: full for skeleton, full in enumerate(keep)}
    skeleton_maximizers = tuple(
        tuple(full_to_skeleton[endpoint] for endpoint in candidate)
        for candidate in maximizers
    )
    skeleton_orbits = tie_aut._orbit_partition(
        skeleton_maximizers, automorphisms
    )
    orbits = tuple(
        tuple(
            tuple(skeleton_to_full[endpoint] for endpoint in candidate)
            for candidate in orbit
        )
        for orbit in skeleton_orbits
    )

    if len(maximizers) == 1:
        diagnostic_state = tie_aut.DIAGNOSTIC_UNIQUE
    elif len(orbits) == 1:
        diagnostic_state = tie_aut.DIAGNOSTIC_TIE_AUT_ONLY
    else:
        diagnostic_state = tie_aut.DIAGNOSTIC_TIE_NONAUT
    if (len(maximizers) == 1) != (optimized.state == comparison.STATE_UNIQUE):
        raise RuntimeError("generic diagnostic UNIQUE disagrees with selector state")
    if len(maximizers) > 1 and optimized.state != comparison.STATE_TIE:
        raise RuntimeError("generic orbit tie disagrees with selector TIE")

    return GenericCrossDiagnostic(
        core=validated,
        core_index=core_index,
        expanded_size=len(realization.permutation),
        middle_size=len(realization.middle_indices),
        optimized_state=optimized.state,
        diagnostic_state=diagnostic_state,
        n_maximizers=len(maximizers),
        n_orbits=len(orbits),
        n_skeleton_automorphisms=len(automorphisms),
        primary_score=best_score[0],
        secondary_score=best_score[1],
        maximizers=maximizers,
        orbits=orbits,
    )


def generic_cross_repairability(core: Sequence[int]) -> GenericCrossSummary:
    """Evaluate every finite generic surgery D_x(kappa); this is not an S_n sweep."""

    validated = tuple(int(value) for value in sealed.validate_permutation(core))
    base = tie_aut.evaluate_tie_aut(validated)
    if base.diagnostic_state != tie_aut.DIAGNOSTIC_TIE_NONAUT:
        raise ValueError("repairability requires a TIE_NONAUT core")
    diagnostics = tuple(
        _generic_cross_diagnostic_validated_bad(validated, core_index)
        for core_index in range(len(validated))
    )
    repairable = tuple(
        diagnostic.core_index for diagnostic in diagnostics if diagnostic.is_good
    )
    return GenericCrossSummary(validated, diagnostics, repairable)
