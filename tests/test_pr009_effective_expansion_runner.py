from __future__ import annotations

import csv
import io
import inspect
from pathlib import Path

import numpy as np
import pytest

from dev import run_pr009_effective_expansion as runner


def causal_matrix(n: int, covers: list[tuple[int, int]]) -> np.ndarray:
    matrix = np.zeros((n, n), dtype=bool)
    for past, future in covers:
        matrix[future, past] = True
    for middle in range(n):
        for future in range(n):
            if matrix[future, middle]:
                matrix[future] |= matrix[middle]
    return matrix


def tied_beam_poset() -> np.ndarray:
    # Start rung 0<*1. Four equal-score depth-2 candidates are generated from
    # p children 1,2,3 and q children 4,5. The legacy insertion-order beam
    # selected different terminal rungs after the permutation used below.
    return causal_matrix(
        6,
        [
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 4),
            (1, 5),
            (2, 4),
            (2, 5),
            (3, 4),
            (3, 5),
        ],
    )


def evaluable_beam_poset() -> tuple[np.ndarray, np.ndarray]:
    # Three exchangeable rail pairs survive at depths two and three.  The
    # shared final element encloses each same-rail survivor pair, so both
    # depths have evaluable widths and depth two has an evaluable transition.
    covers = [(0, 1)]
    for a, b, c, d in zip((2, 3, 4), (5, 6, 7), (8, 9, 10), (11, 12, 13)):
        covers.extend(
            [
                (0, a),
                (1, b),
                (a, b),
                (a, c),
                (b, d),
                (c, d),
                (d, 14),
            ]
        )
    matrix = causal_matrix(15, covers)
    # Prefer a_i over q_0 at depth two and c_i over b_i at depth three.
    rank_order = (2, 3, 4, 8, 9, 10, 0, 1, 5, 6, 7, 11, 12, 13, 14)
    tie_rank = np.empty(15, dtype=np.int64)
    for rank, element in enumerate(rank_order):
        tie_rank[element] = rank
    return matrix, tie_rank


def relabel(
    matrix: np.ndarray, tie_rank: np.ndarray, permutation: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    # permutation[old] = new; inverse[new] = old.
    inverse = np.argsort(permutation)
    return matrix[np.ix_(inverse, inverse)], tie_rank[inverse], inverse


def normalize_beam(
    by_depth: list[list[tuple[int, float, list[int], list[int]]]],
    new_to_old: np.ndarray | None = None,
) -> list[list[tuple[int, float, tuple[int, ...], tuple[int, ...]]]]:
    if new_to_old is None:
        new_to_old = np.arange(max(max(p + q) for depth in by_depth for _, _, p, q in depth) + 1)
    return [
        [
            (
                lineage,
                score,
                tuple(int(new_to_old[item]) for item in p_path),
                tuple(int(new_to_old[item]) for item in q_path),
            )
            for lineage, score, p_path, q_path in depth
        ]
        for depth in by_depth
    ]


def run_tied_beam(
    matrix: np.ndarray,
    tie_rank: np.ndarray,
    start: tuple[int, int],
) -> list[list[tuple[int, float, list[int], list[int]]]]:
    _links, indptr, indices = runner.XL.link_future_csr(matrix)
    return runner.kbeam_exchangeable(
        start[0],
        start[1],
        indptr,
        indices,
        matrix,
        tie_rank,
        beam_size=2,
        max_depth=2,
    )


def test_exchangeable_ranks_are_unique_reproducible_and_seeded():
    first = runner.make_exchangeable_tie_ranks(100, 1_100_000)
    second = runner.make_exchangeable_tie_ranks(100, 1_100_000)
    other = runner.make_exchangeable_tie_ranks(100, 1_100_001)
    assert np.array_equal(first, second)
    assert not np.array_equal(first, other)
    assert np.array_equal(np.sort(first), np.arange(100))
    with pytest.raises(runner.DataContractError):
        runner.validate_tie_ranks(np.array([0, 0, 1]), 3)


def test_whole_beam_falsifier_is_relabeling_equivariant():
    matrix = tied_beam_poset()
    tie_rank = np.array([4, 1, 5, 0, 3, 2], dtype=np.int64)
    original_beam = run_tied_beam(matrix, tie_rank, (0, 1))
    expected = normalize_beam(original_beam)

    # This exact permutation changed the legacy beam's mapped-back terminals.
    permutation = np.array([5, 2, 4, 0, 3, 1])
    changed, changed_ranks, inverse = relabel(matrix, tie_rank, permutation)
    actual = run_tied_beam(
        changed, changed_ranks, (int(permutation[0]), int(permutation[1]))
    )
    assert normalize_beam(actual, inverse) == expected

    original_rows = runner.build_order_only_slices(
        matrix,
        original_beam,
        run_block="REFERENCE",
        seed=1_100_000,
        spacetime_kind="BH",
        start_id=0,
    )
    relabeled_rows = runner.build_order_only_slices(
        changed,
        actual,
        run_block="REFERENCE",
        seed=1_100_000,
        spacetime_kind="BH",
        start_id=0,
    )
    original_bytes = runner.render_csv(
        runner.finalize_order_rows(original_rows, {}), runner.ORDER_FIELDS
    )
    relabeled_bytes = runner.render_csv(
        runner.finalize_order_rows(relabeled_rows, {}), runner.ORDER_FIELDS
    )
    assert relabeled_bytes == original_bytes


def test_whole_beam_survives_many_random_relabelings():
    matrix, tie_rank = evaluable_beam_poset()
    _links, indptr, indices = runner.XL.link_future_csr(matrix)
    starts = runner.sample_starts_exchangeably(
        matrix,
        indptr,
        indices,
        tie_rank,
        max_starts=4,
        selector=lambda _causal: [0],
    )
    start_id = starts.index((0, 1))
    original_beam = runner.kbeam_exchangeable(
        0,
        1,
        indptr,
        indices,
        matrix,
        tie_rank,
        beam_size=4,
        max_depth=3,
    )
    expected_beam = normalize_beam(original_beam)
    original_rows = runner.build_order_only_slices(
        matrix,
        original_beam,
        run_block="REFERENCE",
        seed=1_100_000,
        spacetime_kind="BH",
        start_id=start_id,
    )
    assert original_rows[1].slice_status == "TRANSITION_EVALUABLE"
    original_values = [
        (
            row.n_survivors,
            row.n_valid_pair_separations,
            row.width_lower_median,
            row.theta_raw,
            row.survivor_growth_baseline,
        )
        for row in original_rows
    ]
    original_bytes = runner.render_csv(
        runner.finalize_order_rows(original_rows, {2: 0.0}),
        runner.ORDER_FIELDS,
    )
    rng = np.random.default_rng(20260713)
    for _ in range(100):
        permutation = rng.permutation(matrix.shape[0])
        changed, changed_ranks, inverse = relabel(matrix, tie_rank, permutation)
        _links2, indptr2, indices2 = runner.XL.link_future_csr(changed)
        changed_starts = runner.sample_starts_exchangeably(
            changed,
            indptr2,
            indices2,
            changed_ranks,
            max_starts=4,
            selector=lambda _causal, p=int(permutation[0]): [p],
        )
        mapped_starts = [
            (int(inverse[p]), int(inverse[q])) for p, q in changed_starts
        ]
        assert mapped_starts == starts
        changed_start = (int(permutation[0]), int(permutation[1]))
        assert changed_starts.index(changed_start) == start_id
        actual_beam = runner.kbeam_exchangeable(
            *changed_start,
            indptr2,
            indices2,
            changed,
            changed_ranks,
            beam_size=4,
            max_depth=3,
        )
        assert normalize_beam(actual_beam, inverse) == expected_beam
        actual_rows = runner.build_order_only_slices(
            changed,
            actual_beam,
            run_block="REFERENCE",
            seed=1_100_000,
            spacetime_kind="BH",
            start_id=start_id,
        )
        actual_values = [
            (
                row.n_survivors,
                row.n_valid_pair_separations,
                row.width_lower_median,
                row.theta_raw,
                row.survivor_growth_baseline,
            )
            for row in actual_rows
        ]
        assert actual_values == original_values
        actual_bytes = runner.render_csv(
            runner.finalize_order_rows(actual_rows, {2: 0.0}),
            runner.ORDER_FIELDS,
        )
        assert actual_bytes == original_bytes


def test_start_sampling_is_relabeling_equivariant_past_the_cap():
    # One selected boundary element with ten future-link children; choose four.
    matrix = causal_matrix(11, [(0, child) for child in range(1, 11)])
    tie_rank = np.array([10, 8, 1, 9, 2, 7, 3, 6, 4, 5, 0])
    _links, indptr, indices = runner.XL.link_future_csr(matrix)
    starts = runner.sample_starts_exchangeably(
        matrix,
        indptr,
        indices,
        tie_rank,
        max_starts=4,
        selector=lambda _causal: [0],
    )
    rng = np.random.default_rng(909)
    for _ in range(100):
        permutation = rng.permutation(matrix.shape[0])
        changed, changed_ranks, inverse = relabel(matrix, tie_rank, permutation)
        _links2, indptr2, indices2 = runner.XL.link_future_csr(changed)
        selected = runner.sample_starts_exchangeably(
            changed,
            indptr2,
            indices2,
            changed_ranks,
            max_starts=4,
            selector=lambda _causal, p=int(permutation[0]): [p],
        )
        mapped = [(int(inverse[p]), int(inverse[q])) for p, q in selected]
        assert mapped == starts


def three_rung_diamond() -> tuple[np.ndarray, list[tuple[int, int]]]:
    covers = [(0, node) for node in range(1, 7)]
    covers += [(node, 7) for node in range(1, 7)]
    return causal_matrix(8, covers), [(1, 4), (2, 5), (3, 6)]


def synthetic_by_depth(
    rungs: list[tuple[int, int]], repeat: int = 2
) -> list[list[tuple[int, float, list[int], list[int]]]]:
    result = []
    for _depth in range(repeat):
        result.append(
            [
                (index, 0.0, [p], [q])
                for index, (p, q) in enumerate(rungs)
            ]
        )
    return result


def test_order_builder_has_no_embedding_or_truth_input():
    parameters = set(inspect.signature(runner.build_order_only_slices).parameters)
    assert "embedding" not in parameters
    assert not any("truth" in parameter for parameter in parameters)


def test_order_rows_statuses_residuals_and_canonical_roundtrip():
    matrix, rungs = three_rung_diamond()
    raw = runner.build_order_only_slices(
        matrix,
        synthetic_by_depth(rungs),
        run_block="REFERENCE",
        seed=1_100_000,
        spacetime_kind="MINK",
        start_id=0,
    )
    assert raw[0].slice_status == "TRANSITION_EVALUABLE"
    assert raw[1].slice_status == "WIDTH_ONLY"
    assert all(row.slice_status == "EMPTY" for row in raw[2:])
    finalized = runner.finalize_order_rows(raw, {1: 0.125})
    assert finalized[0]["theta_residual"] == pytest.approx(-0.125)
    data = runner.render_csv(finalized, runner.ORDER_FIELDS)
    rows = runner.validate_order_csv_bytes(data, {"REFERENCE"})
    assert len(rows) == runner.MAX_DEPTH
    assert data.endswith(b"\n") and b"\r" not in data
    assert b",NA," in data


def test_truth_rows_are_separate_and_use_current_depth_zone():
    _matrix, rungs = three_rung_diamond()
    embedding = np.zeros((8, 2), dtype=float)
    embedding[:, 1] = [0.0, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 1.0]
    rows = runner.build_truth_slices(
        embedding,
        synthetic_by_depth(rungs, repeat=1),
        seed=1_100_006,
        spacetime_kind="BH",
        start_id=0,
    )
    assert rows[0]["truth_zone"] == "INTERIOR"
    assert rows[0]["truth_r_mid"] == pytest.approx(0.15)
    assert rows[1]["truth_zone"] is None
    data = runner.render_csv(rows, runner.TRUTH_FIELDS)
    parsed = runner.validate_truth_csv_bytes(data)
    assert len(parsed) == runner.MAX_DEPTH


def order_data(block: str, seed: int, n_starts: int = 1) -> bytes:
    matrix, rungs = three_rung_diamond()
    raw = [
        row
        for start_id in range(n_starts)
        for row in runner.build_order_only_slices(
            matrix,
            synthetic_by_depth(rungs),
            run_block=block,
            seed=seed,
            spacetime_kind="MINK",
            start_id=start_id,
        )
    ]
    return runner.render_csv(
        runner.finalize_order_rows(raw, {1: 0.0}), runner.ORDER_FIELDS
    )


def test_reference_mapping_and_combined_artifact():
    reference = order_data("REFERENCE", 1_100_000, n_starts=12)
    evaluation = order_data("EVALUATION", 1_100_006)
    assert runner.reference_depths_from_csv(reference) == {1: 0.0}
    combined = runner.combine_order_csv(reference, evaluation)
    rows = runner.validate_order_csv_bytes(
        combined, {"REFERENCE", "EVALUATION"}
    )
    assert len(rows) == 13 * runner.MAX_DEPTH
    assert combined.count((",".join(runner.ORDER_FIELDS) + "\n").encode()) == 1


def test_schema_validator_rejects_duplicate_and_noncanonical_float():
    valid = order_data("REFERENCE", 1_100_000)
    lines = valid.splitlines(keepends=True)
    duplicate = b"".join([*lines, lines[1]])
    with pytest.raises(runner.DataContractError, match="duplicate"):
        runner.validate_order_csv_bytes(duplicate, {"REFERENCE"})

    parsed = list(csv.reader(io.StringIO(valid.decode(), newline=""), strict=True))
    theta_index = runner.ORDER_FIELDS.index("theta_raw")
    parsed[1][theta_index] = "0.000"
    stream = io.StringIO(newline="")
    csv.writer(stream, lineterminator="\n").writerows(parsed)
    with pytest.raises(runner.DataContractError, match="canonical"):
        runner.validate_order_csv_bytes(
            stream.getvalue().encode(), {"REFERENCE"}
        )


def test_atomic_publication_refuses_existing_and_rolls_back(tmp_path, monkeypatch):
    first = tmp_path / "first.bin"
    second = tmp_path / "second.bin"
    runner.publish_set(((first, b"one"), (second, b"two")))
    assert first.read_bytes() == b"one" and second.read_bytes() == b"two"
    with pytest.raises(runner.PublicationError):
        runner.publish_set(((first, b"changed"),))
    assert first.read_bytes() == b"one"

    third = tmp_path / "third.bin"
    fourth = tmp_path / "fourth.bin"
    real_replace = runner.os.replace
    calls = 0

    def fail_second_replace(source: Path, target: Path) -> None:
        nonlocal calls
        calls += 1
        if calls == 2:
            raise KeyboardInterrupt
        real_replace(source, target)

    monkeypatch.setattr(runner.os, "replace", fail_second_replace)
    with pytest.raises(KeyboardInterrupt):
        runner.publish_set(((third, b"three"), (fourth, b"four")))
    assert not third.exists() and not fourth.exists()
    assert not Path(str(third) + ".tmp").exists()
    assert not Path(str(fourth) + ".tmp").exists()


def test_cli_exposes_only_frozen_block_choice():
    assert runner.parse_args(["--block", "REFERENCE"]).block == "REFERENCE"
    assert runner.parse_args(["--block", "EVALUATION"]).block == "EVALUATION"
    with pytest.raises(SystemExit):
        runner.parse_args(["--block", "REFERENCE", "--seed", "1"])
