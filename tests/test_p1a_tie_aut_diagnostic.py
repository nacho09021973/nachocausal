"""Bounded unit tests for the diagnostic-only P1a TIE/Aut instrument."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_tie_aut_diagnostic as tie_aut


def test_precommitted_prediction_is_metadata_not_a_guard() -> None:
    assert tie_aut.PREDICTION_N == 7
    assert tie_aut.PREDICTION_TIE_AUT_ONLY_COUNT == 0
    assert tie_aut.PREDICTION_STATUS == (
        "conjectural finite-n prediction; intended to be falsified"
    )


def test_empty_keeps_existing_state_without_new_diagnostic_label() -> None:
    permutation = tuple(reversed(range(7)))
    existing = comparison.evaluate_selectors(permutation)[comparison.MIN_COVERAGE_LEX]
    diagnostic = tie_aut.evaluate_tie_aut(permutation)

    assert existing.state == comparison.STATE_EMPTY
    assert diagnostic.optimized_state == existing.state
    assert diagnostic.diagnostic_state is None
    assert diagnostic.n_automorphisms is None
    assert diagnostic.maximizers == ()
    assert diagnostic.orbits == ()


def test_unique_chain_preserves_existing_state_and_identity_action() -> None:
    permutation = tuple(range(6))
    diagnostic = tie_aut.evaluate_tie_aut(permutation)

    assert diagnostic.optimized_state == comparison.STATE_UNIQUE
    assert diagnostic.diagnostic_state == tie_aut.DIAGNOSTIC_UNIQUE
    assert diagnostic.n_maximizers == 1
    assert diagnostic.n_automorphisms == 1
    assert diagnostic.n_orbits == 1
    assert diagnostic.maximizers == ((0, 2, 3, 5),)


def test_total_chain_tie_survives_quotient_by_trivial_automorphisms() -> None:
    permutation = tuple(range(7))
    diagnostic = tie_aut.evaluate_tie_aut(permutation)

    assert diagnostic.optimized_state == comparison.STATE_TIE
    assert diagnostic.diagnostic_state == tie_aut.DIAGNOSTIC_TIE_NONAUT
    assert diagnostic.n_maximizers == 2
    assert diagnostic.n_automorphisms == 1
    assert diagnostic.n_orbits == 2


def test_twin_endpoints_form_one_exact_automorphism_orbit() -> None:
    # Ordinal levels: 0 < 1 < {2,3} < 4 < 5 < 6.  Swapping elements
    # 2 and 3 preserves the complete poset relation and exchanges both maxima.
    permutation = (0, 1, 3, 2, 4, 5, 6)
    counts, comparable = sealed.interval_count_matrix(permutation)
    relation = tie_aut._as_relation(comparable)
    automorphisms = tie_aut.exact_automorphisms(relation)
    diagnostic = tie_aut.evaluate_tie_aut(permutation)

    assert int(counts[0, 2]) == int(counts[0, 3]) == 3
    assert automorphisms == (
        (0, 1, 2, 3, 4, 5, 6),
        (0, 1, 3, 2, 4, 5, 6),
    )
    assert tie_aut.act_on_candidate(
        automorphisms[1], (0, 2, 4, 6)
    ) == (0, 3, 4, 6)
    assert diagnostic.optimized_state == comparison.STATE_TIE
    assert diagnostic.diagnostic_state == tie_aut.DIAGNOSTIC_TIE_AUT_ONLY
    assert diagnostic.n_maximizers == 2
    assert diagnostic.n_automorphisms == 2
    assert diagnostic.n_orbits == 1
    assert diagnostic.maximizers == ((0, 2, 4, 6), (0, 3, 4, 6))
    assert diagnostic.orbits == (((0, 2, 4, 6), (0, 3, 4, 6)),)


def test_independent_naive_materialization_matches_bounded_fixtures() -> None:
    fixtures = (
        tuple(reversed(range(7))),
        tuple(range(6)),
        tuple(range(7)),
        (0, 1, 3, 2, 4, 5, 6),
    )
    for permutation in fixtures:
        diagnostic = tie_aut.evaluate_tie_aut(permutation)
        naive_maximizers, naive_score = tie_aut.materialize_lex_maximizers_naive(
            permutation
        )
        observed_score = (
            None
            if diagnostic.primary_score is None
            else (diagnostic.primary_score, diagnostic.secondary_score)
        )
        assert naive_maximizers == diagnostic.maximizers
        assert naive_score == observed_score


def test_aggregate_keeps_empty_and_orbit_diagnostics_separate() -> None:
    aggregate = tie_aut.ExactTieAutAggregate(n=7)
    for permutation in (
        tuple(reversed(range(7))),
        (6, 0, 1, 2, 3, 4, 5),
        tuple(range(7)),
        (0, 1, 3, 2, 4, 5, 6),
    ):
        aggregate.add(tie_aut.evaluate_tie_aut(permutation))

    payload = aggregate.as_dict()
    assert aggregate.optimized_state_counts == {
        comparison.STATE_EMPTY: 1,
        comparison.STATE_UNIQUE: 1,
        comparison.STATE_TIE: 2,
    }
    assert aggregate.diagnostic_state_counts == {
        tie_aut.DIAGNOSTIC_UNIQUE: 1,
        tie_aut.DIAGNOSTIC_TIE_AUT_ONLY: 1,
        tie_aut.DIAGNOSTIC_TIE_NONAUT: 1,
    }
    assert aggregate.r_counts == {0: 1, 1: 2, 2: 1}
    assert aggregate.tie_r_counts == {1: 1, 2: 1}
    assert payload["tie_decomposition_given_tie"] == {
        tie_aut.DIAGNOSTIC_TIE_AUT_ONLY: 0.5,
        tie_aut.DIAGNOSTIC_TIE_NONAUT: 0.5,
    }


def test_frozen_publication_refuses_overwrite_and_writes_exact_sidecar(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Publication mechanics are isolated here; the complete exact payload and its
    # aggregate guards are exercised against the committed result below.
    data = b"{}\n"
    monkeypatch.setattr(tie_aut, "frozen_artifact_bytes", lambda aggregates: data)
    path, digest = tie_aut.write_frozen_artifact(
        [], output_dir=tmp_path, overwrite=False
    )
    assert digest == hashlib.sha256(data).hexdigest()
    assert path.read_bytes() == data
    assert path.with_suffix(path.suffix + ".sha256").read_text() == (
        f"{digest}  {path.name}\n"
    )
    with pytest.raises(FileExistsError, match="refusing to overwrite"):
        tie_aut.write_frozen_artifact([], output_dir=tmp_path, overwrite=False)


def test_committed_frozen_artifact_matches_exact_regeneration() -> None:
    artifact_path = tie_aut.DEFAULT_OUTPUT_DIR / tie_aut.ARTIFACT_FILENAME
    frozen = artifact_path.read_bytes()
    regenerated = tie_aut.frozen_artifact_bytes(
        tie_aut.enumerate_exact(tie_aut.EXACT_N)
    )
    assert regenerated == frozen

    digest = hashlib.sha256(frozen).hexdigest()
    assert artifact_path.with_suffix(artifact_path.suffix + ".sha256").read_text() == (
        f"{digest}  {artifact_path.name}\n"
    )
    payload = json.loads(frozen)
    assert payload["result_status"] == "OBSERVED_REPRODUCIBLE_FROZEN_FINITE_N"
    assert payload["scientific_scope"]["claim_ceiling"].startswith(
        "exact finite-n decomposition only"
    )
    assert payload["state_semantics"]["changed"] is False
    assert payload["provenance"]["generator_sha256"] == hashlib.sha256(
        Path(tie_aut.__file__).read_bytes()
    ).hexdigest()
    assert payload["precommit"]["prediction"]["falsified_by_exact_result"] is True
