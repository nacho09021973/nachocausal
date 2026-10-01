"""Bounded tests for the fail-closed NetworkX orbital backend wrapper."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from emergencia import p1a_orbital_backend_preflight_d2 as backend
from emergencia import p1a_tie_aut_diagnostic as frozen


def test_unbounded_m_materializer_matches_frozen_fixtures() -> None:
    for permutation in (
        tuple(reversed(range(7))),
        tuple(range(6)),
        tuple(range(7)),
        (0, 1, 3, 2, 4, 5, 6),
    ):
        _, observed, score = backend.materialize_lex_maximizers(permutation)
        expected = frozen.evaluate_tie_aut(permutation)
        expected_score = (
            None
            if expected.primary_score is None
            else (expected.primary_score, expected.secondary_score)
        )
        assert observed == expected.maximizers
        assert score == expected_score


def test_directed_relation_graph_has_exact_twin_automorphisms() -> None:
    permutation = (0, 1, 3, 2, 4, 5, 6)
    relation, _, _ = backend.materialize_lex_maximizers(permutation)
    graph = backend.relation_to_digraph(relation)
    mappings = tuple(backend.DiGraphMatcher(graph, graph).isomorphisms_iter())
    assert len(mappings) == 2
    assert {mapping[2] for mapping in mappings} == {2, 3}


def test_four_public_states_keep_orbital_semantics() -> None:
    fixtures = {
        tuple(reversed(range(7))): backend.STATUS_EMPTY,
        tuple(range(6)): backend.STATUS_ORBITAL_UNIQUE,
        tuple(range(7)): backend.STATUS_ORBITAL_NONUNIQUE,
        (0, 1, 3, 2, 4, 5, 6): backend.STATUS_ORBITAL_UNIQUE,
    }
    for permutation, status in fixtures.items():
        result = backend.evaluate_orbital_backend(permutation, complete_orbits=True)
        assert result.status == status
        assert result.error_type is None


def test_minimal_route_and_complete_partition_agree() -> None:
    permutation = (0, 1, 3, 2, 4, 5, 6)
    minimal = backend.evaluate_orbital_backend(permutation, complete_orbits=False)
    complete = backend.evaluate_orbital_backend(permutation, complete_orbits=True)
    assert minimal.status == complete.status == backend.STATUS_ORBITAL_UNIQUE
    assert minimal.n_orbits_on_m == complete.n_orbits_on_m == 1
    assert minimal.n_automorphisms is None
    assert complete.n_automorphisms == 2


def test_backend_exception_is_fail_closed(monkeypatch) -> None:
    class BrokenMatcher:
        def __init__(self, *args, **kwargs):
            raise RuntimeError("synthetic backend failure")

    monkeypatch.setattr(backend, "DiGraphMatcher", BrokenMatcher)
    result = backend.evaluate_orbital_backend(tuple(range(7)))
    assert result.status == backend.STATUS_BACKEND_FAILURE
    assert result.error_type == "RuntimeError"
    assert result.n_orbits_on_m is None


def test_timeout_is_fail_closed() -> None:
    result = backend.evaluate_orbital_backend(tuple(range(7)), timeout_s=1e-9)
    assert result.status == backend.STATUS_BACKEND_FAILURE
    assert result.error_type == "BackendTimeout"


def test_benchmark_design_is_predeclared() -> None:
    assert backend.BENCHMARK_N == (10, 12, 16)
    assert backend.BENCHMARK_INSTANCES == 100
    assert backend.BENCHMARK_SEED == 260_826
    assert backend.READY_P95_S < backend.PROMISING_P95_S


def test_committed_preflight_report_is_sealed_and_non_scientific() -> None:
    path = backend.DEFAULT_OUTPUT
    encoded = path.read_bytes()
    digest = hashlib.sha256(encoded).hexdigest()
    assert path.with_suffix(path.suffix + ".sha256").read_text() == (
        f"{digest}  {path.name}\n"
    )
    payload = json.loads(encoded)
    assert payload["exhaustive_equivalence"]["total"] == backend.EXPECTED_TOTAL
    assert payload["exhaustive_equivalence"]["backend_equivalence"] == "PASS"
    assert payload["engineering_verdict"] == "READY"
    assert payload["scientific_guard"] == {
        "frozen_artifacts_overwritten": False,
        "large_n_e_estimated": False,
        "large_n_u_estimated": False,
        "state_unique_used_as_proxy": False,
    }
    assert payload["provenance"]["generator_sha256"] == hashlib.sha256(
        Path(backend.__file__).read_bytes()
    ).hexdigest()
