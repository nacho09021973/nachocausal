"""Bounded unit tests for the frozen summary family Xi^A subset Xi^B subset Xi^C.

No thinning, no mask enumeration and no target quantity (q_p, q_p_star, e_p, a_k, b_k)
is computed anywhere in these tests.
"""

from __future__ import annotations

from itertools import permutations

from emergencia import p1a_paisaje_niveles_d2 as landscape
from emergencia import p1a_xi_familia_fibras_d2 as xi


def test_declared_dimensions_are_constant_in_n() -> None:
    assert xi.MEMBER_DIMENSION == {"XI_A": 5, "XI_B": 10, "XI_C": 18}
    for n in (6, 7, 8, 9):
        vectors = xi.xi_live(tuple(range(n)))
        for member, dimension in xi.MEMBER_DIMENSION.items():
            assert len(vectors[member]) == dimension


def test_members_are_nested_prefixes() -> None:
    vectors = xi.xi_live((0, 1, 2, 3, 4, 5, 6, 7, 8))
    assert vectors["XI_B"][: len(vectors["XI_A"])] == vectors["XI_A"]
    assert vectors["XI_C"][: len(vectors["XI_B"])] == vectors["XI_B"]


def test_empty_candidate_set_is_na_never_zero() -> None:
    vectors = xi.xi_live(tuple(reversed(range(9))))
    assert vectors["XI_A"] == (0, None, None, None, None)
    assert vectors["XI_B"] == (0, None, None, None, None) * 2
    # The three trailing totals L, |Q|, R are genuine counts, not NA.
    assert vectors["XI_C"][-3:] == (0, 0, 0)


def test_top_block_reproduces_rho_and_the_frozen_top_level() -> None:
    for permutation in permutations(range(7)):
        result = landscape.score_landscape(permutation)
        vector = xi.xi_live(permutation)["XI_A"]
        if result.n_candidates == 0:
            assert vector[0] == 0
            continue
        top = result.levels[0]
        assert vector == (
            1,
            top.primary_score,
            top.secondary_score,
            top.candidate_count,
            top.orbit_count,
        )


def test_unavailable_depth_is_flagged_not_silently_zero() -> None:
    # A permutation whose landscape has exactly one level: depth 2 and 3 are NA.
    single = next(
        permutation
        for permutation in permutations(range(8))
        if landscape.score_landscape(permutation).n_score_levels == 1
    )
    vector = xi.xi_live(single)["XI_C"]
    assert vector[5] == 0 and vector[6:10] == (None, None, None, None)
    assert vector[10] == 0 and vector[11:15] == (None, None, None, None)
    assert vector[15] == 1


def test_two_independent_paths_agree_on_the_smallest_size() -> None:
    rows = xi._read_landscape_csv(xi.LANDSCAPE_CSV, (6,))
    for permutation in permutations(range(6)):
        encoded = landscape.encode_permutation(permutation)
        assert xi.xi_from_csv_rows(rows[(6, encoded)]) == xi.xi_live(permutation)


def test_family_is_not_injective_and_admits_non_isomorphic_collisions() -> None:
    rows = xi._read_landscape_csv(xi.LANDSCAPE_CSV, (7,))
    report = xi.study_fibres(7, rows)
    xi.validate_report(report)
    for member in xi.MEMBERS:
        block = report[member]
        assert block["injective"] is False
        assert block["available_fibres_with_several_isomorphism_classes"] > 0
        assert block["non_isomorphic_collision_witness_available_domain"] is not None
        assert block["non_isomorphic_collision_witness_unavailable_fibre"] is not None
