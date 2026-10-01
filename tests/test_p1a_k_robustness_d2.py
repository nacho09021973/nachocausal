"""Focused instrument tests for the K-robustness runner."""

from __future__ import annotations

import csv
import hashlib
import io
import json

import pytest

from emergencia import p1a_large_n_orbital_baseline_d2 as baseline
from emergencia import p1a_k_robustness_d2 as krob
from emergencia import p1a_orbital_backend_preflight_d2 as orbital


def test_contract_is_frozen_and_sealed() -> None:
    digest = hashlib.sha256(krob.CONTRACT_PATH.read_bytes()).hexdigest()
    sidecar = krob.CONTRACT_PATH.with_suffix(krob.CONTRACT_PATH.suffix + ".sha256")
    assert sidecar.exists()
    assert digest in sidecar.read_text(encoding="utf-8")
    text = krob.CONTRACT_PATH.read_text(encoding="utf-8")
    assert "CONGELADO_ANTES_DE_EJECUCION" in text
    assert "W = {22, 24}" in text


def test_sealed_selector_is_untouched() -> None:
    assert krob.validate_sealed_selector_untouched() == krob.SEALED_SELECTOR_SHA256


def test_injected_floor_equals_sealed_selector_at_the_anchor() -> None:
    """The whole design rests on this: at K=3 nothing may differ."""

    for n in (7, 9, 14, 18):
        for permutation in baseline._uniform_permutations(n, 25, 31_337 + n):
            mine = krob.materialize_lex_maximizers_k(permutation, krob.K_ANCHOR)
            theirs = orbital.materialize_lex_maximizers(permutation)
            assert mine[0] == theirs[0]
            assert mine[1] == theirs[1]
            assert mine[2] == theirs[2]


def test_raising_the_floor_never_admits_a_slacker_candidate() -> None:
    """Every maximizer must satisfy its own floor; the floor really binds."""

    for n in (12, 16):
        for permutation in baseline._uniform_permutations(n, 20, 555 + n):
            for k in krob.K_VALUES:
                _, maximizers, score = krob.materialize_lex_maximizers_k(permutation, k)
                if not maximizers:
                    continue
                assert score is not None
                assert score[0] >= k, "primary_score is floored by K by construction"


def test_seed_depends_on_n_only_so_arms_are_paired() -> None:
    for n in krob.N_VALUES:
        seed = krob.multiplicity.scientific_seed(n)
        assert seed == krob.SCIENTIFIC_SEED_BASE + n
        first = list(baseline._uniform_permutations(n, 5, seed))
        second = list(baseline._uniform_permutations(n, 5, seed))
        assert first == second


def test_operational_plateau_reproduces_the_frozen_window_on_the_anchor() -> None:
    """Applied to the sealed campaign, the criterion must return W itself."""

    with krob.PRIOR_SUMMARY_PATH.open(newline="", encoding="utf-8") as handle:
        rows = [r for r in csv.DictReader(handle) if int(r["n"]) in krob.N_VALUES]
    points = {
        int(r["n"]): (
            float(r[krob.PRIMARY_OBSERVABLE]),
            float(r[f"{krob.PRIMARY_OBSERVABLE}_ci95_low"]),
            float(r[f"{krob.PRIMARY_OBSERVABLE}_ci95_high"]),
        )
        for r in rows
    }
    argmax, plateau = krob.operational_plateau(points)
    assert argmax == (24,)
    assert plateau == tuple(krob.REFERENCE_WINDOW)
    assert krob.classify_arm(points, [])[0] == krob.ARM_MAINTAINS


def test_plateau_absorbs_overlapping_intervals() -> None:
    points = {20: (0.05, 0.04, 0.06), 22: (0.09, 0.08, 0.10), 24: (0.10, 0.09, 0.11)}
    argmax, plateau = krob.operational_plateau(points)
    assert argmax == (24,)
    assert plateau == (22, 24)


def test_arm_shifts_only_when_the_whole_plateau_leaves_the_window() -> None:
    shifted = {
        22: (0.02, 0.018, 0.022),
        24: (0.03, 0.028, 0.032),
        26: (0.09, 0.088, 0.092),
        28: (0.10, 0.098, 0.102),
    }
    verdict, argmax, plateau = krob.classify_arm(shifted, [])
    assert verdict == krob.ARM_SHIFTS
    assert set(plateau).isdisjoint(krob.REFERENCE_WINDOW)
    # A one-cell move is still a shift: the rule decides, not the magnitude.
    assert argmax == (28,)


def test_censoring_inside_the_window_can_never_yield_maintains() -> None:
    points = {26: (0.09, 0.08, 0.10), 28: (0.08, 0.07, 0.09)}
    assert krob.classify_arm(points, [22])[0] == krob.ARM_UNDETERMINED
    assert krob.classify_arm(points, [24])[0] == krob.ARM_UNDETERMINED


def test_terminals_are_conservative() -> None:
    clean = {k: [] for k in krob.K_VALUES}
    maintains = {k: krob.ARM_MAINTAINS for k in krob.K_VALUES}
    assert krob.decide_terminal(maintains, clean) == krob.TERMINAL_ROBUST

    shifted = {**maintains, 4: krob.ARM_SHIFTS}
    assert krob.decide_terminal(shifted, clean) == krob.TERMINAL_DEPENDENT

    undetermined = {**maintains, 5: krob.ARM_UNDETERMINED}
    assert krob.decide_terminal(undetermined, clean) == krob.TERMINAL_INCONCLUSIVE

    # a demonstrated shift dominates an undetermined arm
    mixed = {**maintains, 2: krob.ARM_SHIFTS, 5: krob.ARM_UNDETERMINED}
    assert krob.decide_terminal(mixed, clean) == krob.TERMINAL_DEPENDENT

    # ROBUST_TO_K is unreachable with any censored cell
    assert (
        krob.decide_terminal(maintains, {**clean, 4: [20]})
        == krob.TERMINAL_INCONCLUSIVE
    )

    # the anchor's own verdict never decides the terminal
    anchor_broken = {**maintains, krob.K_ANCHOR: krob.ARM_SHIFTS}
    assert krob.decide_terminal(anchor_broken, clean) == krob.TERMINAL_ROBUST


def test_long_recomposition_fails_closed_on_a_mismatch() -> None:
    rows = [{"K": 3, "n": 22, "N_total": 10, "N_nonempty": 7}]
    good = krob._csv_bytes(
        [
            {"PHASE": krob.PHASE, "K": 3, "n": 22, "seed": 1, "R": 0, "count": 3},
            {"PHASE": krob.PHASE, "K": 3, "n": 22, "seed": 1, "R": 1, "count": 7},
        ],
        krob.LONG_FIELDS,
    )
    krob.validate_long_recomposition(good, rows)

    bad = krob._csv_bytes(
        [
            {"PHASE": krob.PHASE, "K": 3, "n": 22, "seed": 1, "R": 0, "count": 3},
            {"PHASE": krob.PHASE, "K": 3, "n": 22, "seed": 1, "R": 1, "count": 6},
        ],
        krob.LONG_FIELDS,
    )
    with pytest.raises(RuntimeError):
        krob.validate_long_recomposition(bad, rows)


def test_anchor_reproduction_guard_rejects_a_drifted_arm() -> None:
    with pytest.raises(RuntimeError):
        krob.validate_anchor_reproduces_sealed(
            [
                {
                    "K": krob.K_ANCHOR,
                    "n": 22,
                    krob.PRIMARY_OBSERVABLE: "0.999",
                    f"{krob.PRIMARY_OBSERVABLE}_ci95_low": "0.9",
                    f"{krob.PRIMARY_OBSERVABLE}_ci95_high": "1.0",
                    **{name: "0" for name in krob.SECONDARY_OBSERVABLES},
                }
            ]
        )


@pytest.mark.skipif(
    not (krob.RESULTS_DIR / krob.JSON_FILENAME).exists(),
    reason="scientific artifacts are written only after the frozen run",
)
def test_completed_artifacts_are_sealed_and_recomposable() -> None:
    summary_path = krob.RESULTS_DIR / krob.SUMMARY_CSV_FILENAME
    long_path = krob.RESULTS_DIR / krob.LONG_CSV_FILENAME
    json_path = krob.RESULTS_DIR / krob.JSON_FILENAME
    for path in (summary_path, long_path, json_path):
        baseline._verify_sidecar(path)
    with summary_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    krob.validate_long_recomposition(long_path.read_bytes(), rows)
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    assert payload["result_status"] in (
        krob.TERMINAL_ROBUST,
        krob.TERMINAL_DEPENDENT,
        krob.TERMINAL_INCONCLUSIVE,
    )
    assert payload["controls"]["K3_ARM_REPRODUCES_SEALED_CAMPAIGN"] == "PASS"
    assert payload["controls"]["PAIRED_SAMPLE_IDENTITY"] == "PASS"
    assert payload["controls"]["BACKEND_FAILURES"] == 0
    assert len(rows) == len(krob.K_VALUES) * len(krob.N_VALUES)
