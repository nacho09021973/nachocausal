"""Tests for EF-2 exact COUNT_VOLUME fiber enumeration in d=2."""

from __future__ import annotations

import hashlib
import json
import math
from itertools import permutations
from pathlib import Path

import pytest

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_entropia_fibras_enumeracion_d2 as ef2


_ROOT = Path(__file__).resolve().parent.parent
_RESULTS = _ROOT / "emergencia" / "resultados"


def test_contract_constants_and_artifact_names() -> None:
    assert ef2.EXACT_N == (6, 7, 8, 9)
    assert ef2.INDEPENDENT_CROSSCHECK_N == (6, 7)
    assert ef2.SIDES == ("PAST", "FUTURE")
    assert ef2.STATES == ("EMPTY", "UNIQUE", "TIE")
    assert len(
        {
            ef2.STATE_FILENAME,
            ef2.OMEGA_FILENAME,
            ef2.C_FILENAME,
            ef2.SUMMARY_FILENAME,
        }
    ) == 4
    assert all("entropia_fibras" in name for name in (
        ef2.STATE_FILENAME,
        ef2.OMEGA_FILENAME,
        ef2.C_FILENAME,
        ef2.SUMMARY_FILENAME,
    ))


def test_naive_and_optimized_lex_match_for_every_n6_permutation() -> None:
    for permutation in permutations(range(6)):
        optimized = comparison.evaluate_selectors(permutation)[
            comparison.MIN_COVERAGE_LEX
        ]
        independent = ef2.evaluate_lex_naive(permutation)
        assert ef2._optimized_signature(optimized) == ef2._independent_signature(
            independent
        )


def test_exact_n6_fiber_is_the_single_chain_shape() -> None:
    legacy, _ = ef2.load_legacy_coverage_counts()
    aggregate = ef2.enumerate_exact((6,), legacy_expected=legacy)[0]
    assert aggregate.permutations == math.factorial(6)
    assert aggregate.state_counts == {"EMPTY": 719, "UNIQUE": 1}
    assert aggregate.omega == {
        ("PAST", 3, 2, 2, 4): 1,
        ("FUTURE", 3, 2, 2, 4): 1,
    }
    assert aggregate.c_counts == {
        ("PAST", 3, 4): 1,
        ("FUTURE", 3, 4): 1,
    }


def test_coordinate_and_time_reversal_transform_selected_shapes() -> None:
    selected = None
    for permutation in permutations(range(7)):
        outcome = comparison.evaluate_selectors(permutation)[
            comparison.MIN_COVERAGE_LEX
        ]
        if outcome.state != comparison.STATE_UNIQUE or outcome.selection is None:
            continue
        past = ef2._shape_for_side(permutation, outcome.selection, "PAST")
        future = ef2._shape_for_side(permutation, outcome.selection, "FUTURE")
        if past[1] != past[2] or past != future:
            selected = (permutation, past, future)
            break
    assert selected is not None
    permutation, past, future = selected

    inverse = [0] * len(permutation)
    for index, value in enumerate(permutation):
        inverse[value] = index
    inverse_outcome = comparison.evaluate_selectors(inverse)[
        comparison.MIN_COVERAGE_LEX
    ]
    assert inverse_outcome.selection is not None
    inverse_past = ef2._shape_for_side(inverse, inverse_outcome.selection, "PAST")
    assert inverse_past == (past[0], past[2], past[1], past[3])

    n = len(permutation)
    reverse = tuple(n - 1 - permutation[n - 1 - index] for index in range(n))
    reverse_outcome = comparison.evaluate_selectors(reverse)[
        comparison.MIN_COVERAGE_LEX
    ]
    assert reverse_outcome.selection is not None
    reverse_past = ef2._shape_for_side(reverse, reverse_outcome.selection, "PAST")
    assert reverse_past == future


def test_frozen_coverage_control_has_expected_collapsed_counts() -> None:
    counts, digest = ef2.load_legacy_coverage_counts()
    assert len(digest) == 64
    assert counts[6] == {"EMPTY": 719, "UNIQUE": 1, "TIE": 0}
    assert counts[7] == {"EMPTY": 5003, "UNIQUE": 32, "TIE": 5}
    assert counts[8] == {"EMPTY": 39429, "UNIQUE": 674, "TIE": 217}
    assert counts[9] == {"EMPTY": 344837, "UNIQUE": 12076, "TIE": 5967}


def test_atomic_writer_refuses_implicit_overwrite(tmp_path: Path) -> None:
    path = tmp_path / "artifact.csv"
    ef2._atomic_write(path, b"first\n", overwrite=False)
    with pytest.raises(FileExistsError):
        ef2._atomic_write(path, b"second\n", overwrite=False)
    assert path.read_bytes() == b"first\n"


def test_generated_artifacts_match_sidecars_and_summary() -> None:
    expected = {
        ef2.STATE_FILENAME: (
            "ce589a5eeaa6fa1606df6064c53255efc8c3c80f52cb166dee6b71aaee175293"
        ),
        ef2.OMEGA_FILENAME: (
            "03624db88f582c2180b6064deda199fd6735651c8a21d9a8a79c2b3c5b988858"
        ),
        ef2.C_FILENAME: (
            "1f3c55582690d6bbb32f6a4e0849c51d1599c99033ab9ab9ea7d30ea9e927dd1"
        ),
        ef2.SUMMARY_FILENAME: (
            "c97284ff7a610cf55cf2779e3653c8c89d6bd929feaf288bf30f5aead612d38e"
        ),
    }
    for filename, expected_digest in expected.items():
        path = _RESULTS / filename
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        assert b"\r" not in data
        assert digest == expected_digest
        assert path.with_suffix(path.suffix + ".sha256").read_text() == (
            f"{digest}  {filename}\n"
        )

    summary = json.loads((_RESULTS / ef2.SUMMARY_FILENAME).read_text())
    assert summary["contract_status"] == "EF0_EF1_FIXED_BEFORE_ENUMERATION"
    assert summary["terminal"] == "EXACT_SMALL_N_FIBER_TABLES_VALIDATED"
    assert summary["claim_ceiling"] == "EXACT_N_6_TO_9_ONLY_NO_ASYMPTOTIC_INFERENCE"
    assert summary["monte_carlo"] == "NOT_RUN"
    assert summary["gauss_kuzmin"] == "NOT_USED"
    assert all(summary["validations"].values())
    assert summary["environment"]["generator_sha256"] == hashlib.sha256(
        Path(ef2.__file__).read_bytes()
    ).hexdigest()
    assert [record["n"] for record in summary["by_n"]] == [6, 7, 8, 9]
    assert [record["state_counts"] for record in summary["by_n"]] == [
        {"EMPTY": 719, "UNIQUE": 1, "TIE": 0},
        {"EMPTY": 5003, "UNIQUE": 32, "TIE": 5},
        {"EMPTY": 39429, "UNIQUE": 677, "TIE": 214},
        {"EMPTY": 344837, "UNIQUE": 12220, "TIE": 5823},
    ]
