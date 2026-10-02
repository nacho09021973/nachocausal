"""Bounded unit tests for the exact static score-level landscape extractor.

These tests exercise only the five mandated landscape invariants and the guarantee
that no thinning or target quantity enters the module.  They perform no Monte Carlo
simulation, enumerate no masks and never evaluate q_p, q_p_star, e_p, a_k or b_k.
"""

from __future__ import annotations

from itertools import permutations

import pytest

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_paisaje_niveles_d2 as landscape
from emergencia import p1a_tie_aut_diagnostic as tie_aut


def test_module_never_imports_the_thinning_machinery() -> None:
    import ast
    import sys

    tree = ast.parse(landscape.Path(landscape.__file__).read_text(encoding="utf-8"))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.update(alias.name for alias in node.names)
            if node.module:
                imported.add(node.module)
    assert not any("estabilidad" in name for name in imported)
    assert "p1a_estabilidad_d2" not in sys.modules or not any(
        value is sys.modules["p1a_estabilidad_d2"]
        for value in vars(landscape).values()
    )
    called = {
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }
    assert "induced_permutation" not in called
    assert "simulate_base" not in called
    assert "simulate" not in called


def test_empty_candidate_set_is_typed_na_not_zero() -> None:
    result = landscape.score_landscape(tuple(reversed(range(7))))
    assert result.n_candidates == 0
    assert result.n_score_levels == 0
    assert result.n_automorphisms is None
    row = landscape.landscape_rows(result)[0]
    assert row["candidates_available"] == 0
    assert row["orbit_count"] is None
    assert row["primary_score"] is None


def test_levels_partition_the_admissible_candidate_set() -> None:
    for permutation in ((0, 1, 2, 3, 4, 5, 6, 7), (0, 2, 1, 4, 3, 6, 5, 7)):
        result = landscape.score_landscape(permutation)
        scored, _ = landscape.score_candidates(permutation)
        members = [
            candidate for level in result.levels for candidate in level.candidates
        ]
        assert len(members) == len(scored)
        assert set(members) == {candidate for candidate, _ in scored}


def test_levels_are_distinct_and_strictly_descending() -> None:
    result = landscape.score_landscape((0, 1, 2, 3, 4, 5, 6, 7))
    scores = [level.score for level in result.levels]
    assert len(set(scores)) == len(scores)
    assert scores == sorted(scores, reverse=True)


def test_top_level_equals_the_frozen_maximizer_set() -> None:
    permutation = (0, 1, 2, 3, 4, 5, 6, 7)
    result = landscape.score_landscape(permutation)
    _, maximizers, best_score = tie_aut.materialize_lex_maximizers(permutation)
    assert result.levels[0].candidates == tuple(sorted(maximizers))
    assert result.levels[0].score == best_score


def test_top_level_orbit_count_reproduces_the_frozen_diagnostic() -> None:
    for permutation in permutations(range(7)):
        result = landscape.score_landscape(permutation)
        diagnostic = tie_aut.evaluate_tie_aut(permutation)
        if diagnostic.optimized_state == comparison.STATE_EMPTY:
            assert result.n_candidates == 0
            continue
        assert result.levels[0].orbit_count == diagnostic.n_orbits
        assert result.n_automorphisms == diagnostic.n_automorphisms


def test_every_level_is_closed_under_every_automorphism() -> None:
    for permutation in permutations(range(7)):
        result = landscape.score_landscape(permutation)
        if result.n_candidates == 0:
            continue
        _, relation = landscape.score_candidates(permutation)
        automorphisms = tie_aut.exact_automorphisms(relation)
        for level in result.levels:
            members = set(level.candidates)
            for automorphism in automorphisms:
                for candidate in level.candidates:
                    assert tie_aut.act_on_candidate(automorphism, candidate) in members


def test_orbit_sizes_sum_to_the_level_size() -> None:
    for permutation in permutations(range(7)):
        result = landscape.score_landscape(permutation)
        for level in result.levels:
            assert sum(level.orbit_sizes) == level.candidate_count
            assert level.orbit_count == len(level.orbit_sizes)


def test_exhaustive_validation_passes_on_the_smallest_two_sizes() -> None:
    _, aggregates = landscape.enumerate_landscape((6, 7), validate=True)
    assert [aggregate.permutations for aggregate in aggregates] == [720, 5040]
    assert [aggregate.empty for aggregate in aggregates] == [719, 5003]


def test_extraction_refuses_sizes_outside_the_pilot_band() -> None:
    with pytest.raises(ValueError):
        landscape.enumerate_landscape((10,))
    with pytest.raises(ValueError):
        landscape.score_candidates(tuple(range(10)))
