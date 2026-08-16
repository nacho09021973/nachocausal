"""Is any n=24 abstract counterexample realizable under the prescription F_n?

`ef4_trichotomy_exhaustiveness_n24.py` swept the *abstract* domain that
`tests/test_p1a_entropia_fibras_ef4.py:63-154` enumerates: every 4-combination of
rows crossed with every 4-combination of columns, with no constraint tying the
two together. It found 560 tuples falsifying all three disjuncts.

That domain is larger than the set of configurations the certificate actually
has to cover. A quadruple corresponds to four points `(r_i, c_i)` of a
permutation in `F_n`, so a *realizable* quadruple must respect the prescription:
a prescribed row may only be paired with its prescribed column, and vice versa.
An abstract counterexample pairing row 11 with column 11, when `F_n` prescribes
`11 -> 7`, is not a permutation in `F_n` and refutes nothing about the family.

This script decides the question, using the key containment: every F_n-compatible
quadruple IS an abstract quadruple, so the compatible counterexamples are exactly
the compatible members of the already-computed abstract sets. No second sweep of
the big domain is needed.

Reported, mirroring the (n=30, rho=2) analysis:
  REQUIRES_LOSS_CASE   -- compatible quadruples with small_product False
  LOSS_CASE_PASS       -- of those, how many are carried by loss_case/fixed_inner
  COMPATIBLE_FAILURES  -- compatible quadruples failing all three disjuncts

Exact rational arithmetic throughout, so the verdict cannot turn on a float.

Run:  .venv/bin/python dev/ef4_trichotomy_prescription_compatibility_n24.py
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from emergencia import p1a_entropia_fibras_ef4 as ef4  # noqa: E402

from ef4_trichotomy_witness_check_n24 import scalar_disjuncts  # noqa: E402

N = 24
RHO = 2


def prescription(n: int, rho: int) -> tuple[dict[int, int], dict[int, int]]:
    forward = ef4.build_even_prescription(n, rho=rho)
    return dict(forward), {column: row for row, column in forward.items()}


def is_compatible(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    forward: dict[int, int],
    inverse: dict[int, int],
) -> bool:
    """Can these four corner points sit inside some permutation of F_n?"""
    for row, column in zip(rows, columns):
        if row in forward and forward[row] != column:
            return False
        if column in inverse and inverse[column] != row:
            return False
    return True


def staircases(n: int, rho: int) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    """The two staircases, as the sealed test defines them. Each has rho-1 points."""
    forward, _ = prescription(n, rho)
    half = n // 2
    points = sorted(forward.items())
    lower = [p for p in points if half - rho + 1 <= p[0] <= half - 1]
    upper = [p for p in points if half + 2 <= p[0] <= half + rho]
    return lower, upper


def has_partial_staircase(
    rows: tuple[int, ...], columns: tuple[int, ...], n: int, rho: int
) -> bool:
    """Does either box contain a strict, non-empty subset of either staircase?

    This is the configuration the trichotomy's case analysis actually has to
    adjudicate: a box that swallows part of a staircase but not all of it. With
    one-point staircases it cannot occur -- containment is 0 or all.
    """
    lower, upper = staircases(n, rho)
    past_lower, past_upper, future_lower, future_upper = tuple(zip(rows, columns))
    boxes = ((past_lower, past_upper), (future_lower, future_upper))
    for low, high in boxes:
        for stair in (lower, upper):
            if not stair:
                continue
            held = sum(
                low[0] <= point[0] <= high[0] and low[1] <= point[1] <= high[1]
                for point in stair
            )
            if 0 < held < len(stair):
                return True
    return False


def float_safety(n: int, rho: int) -> tuple[Fraction, Fraction, bool]:
    """Is any product/threshold comparison an exact tie at this (n, rho)?"""
    forward, _ = prescription(n, rho)
    free_count = n - len(forward)
    threshold = Fraction(1, 8) + Fraction(rho, free_count)
    # Products are k / free_count**2 with k an integer, so a comparison can only
    # tie when the scaled threshold is itself an integer.
    scaled = threshold * free_count**2
    return threshold, scaled, scaled.denominator == 1


def count_compatible_chains(n: int, rho: int) -> int:
    """Size of the realizable domain: 4-chains of points allowed by F_n."""
    forward, _ = prescription(n, rho)
    free_rows = [row for row in range(1, n + 1) if row not in forward]
    free_columns = [
        column for column in range(1, n + 1) if column not in set(forward.values())
    ]
    points = sorted(forward.items()) + [
        (row, column) for row in free_rows for column in free_columns
    ]
    points.sort()
    chains = [1] * len(points)  # chains of length 1 ending at each point
    total = 0
    for _ in range(3):
        nxt = [0] * len(points)
        for j, (row_j, col_j) in enumerate(points):
            running = 0
            for i, (row_i, col_i) in enumerate(points):
                if row_i < row_j and col_i < col_j:
                    running += chains[i]
            nxt[j] = running
        chains = nxt
    total = sum(chains)
    return total


def main() -> int:
    threshold, scaled, has_ties = float_safety(N, RHO)
    print(f"[FP] threshold                = {threshold} = {float(threshold):.6f}")
    print(f"[FP] threshold * free_count^2 = {scaled}")
    print(f"[FP] exact ties possible      = {has_ties}")
    assert not has_ties, (
        "an exact tie exists at this (n, rho): the float sweep may misclassify "
        "boundary comparisons and must be redone in rationals"
    )
    print("[FP] no comparison can tie, so the float sweep is exact at n=24")
    print()

    forward, inverse = prescription(N, RHO)
    print(f"[F_n] prescription = {sorted(forward.items())}")
    domain = count_compatible_chains(N, RHO)
    print(f"[F_n] realizable 4-chains  = {domain}")
    print(f"[F_n] abstract quadruples  = 112911876")
    print()

    payload = json.loads(
        (Path(__file__).resolve().parent / "EF4_TRICHOTOMY_N24_RESULT.json").read_text()
    )

    biting = [
        (tuple(entry["rows"]), tuple(entry["columns"]))
        for entry in payload["biting_tuples"]
    ]
    failing = [
        (tuple(entry["rows"]), tuple(entry["columns"]))
        for entry in payload["failing_tuples"]
    ]
    assert len(biting) == payload["non_vacuous"] == 1504
    assert len(failing) == payload["failures"] == 560

    compatible_biting = [
        pair for pair in biting if is_compatible(*pair, forward, inverse)
    ]
    compatible_failing = [
        pair for pair in failing if is_compatible(*pair, forward, inverse)
    ]

    loss_case_pass = 0
    partial_staircase_cases = 0
    for rows, columns in compatible_biting:
        verdict = scalar_disjuncts(N, RHO, rows, columns)
        assert not verdict["small_product"], (rows, columns)
        if verdict["loss_case"] or verdict["fixed_inner"]:
            loss_case_pass += 1
        if has_partial_staircase(rows, columns, N, RHO):
            partial_staircase_cases += 1

    print(f"[n=24] abstract biting     = {len(biting)}")
    print(f"[n=24] abstract failures   = {len(failing)}")
    print(f"REQUIRES_LOSS_CASE={len(compatible_biting)}")
    print(f"LOSS_CASE_PASS={loss_case_pass}")
    print(f"COMPATIBLE_FAILURES={len(compatible_failing)}")
    print()

    lower, upper = staircases(N, RHO)
    print(f"[stairs] lower_stair = {lower}  (|lower| = {len(lower)})")
    print(f"[stairs] upper_stair = {upper}  (|upper| = {len(upper)})")
    print(f"[stairs] staircase size is rho-1 = {RHO - 1}")
    print(f"PARTIAL_STAIRCASE_CASES={partial_staircase_cases}")
    if len(lower) <= 1 and len(upper) <= 1:
        print(
            "[stairs] STRUCTURALLY_IMPOSSIBLE: with one-point staircases a box holds "
            "0 or all of a staircase, never a strict non-empty subset, so no sweep at "
            f"rho={RHO} can exercise partial containment at any n"
        )
        assert partial_staircase_cases == 0
    print()

    witness = failing[0]
    print(f"[witness] rows    = {witness[0]}")
    print(f"[witness] columns = {witness[1]}")
    for row, column in zip(*witness):
        if row in forward and forward[row] != column:
            print(
                f"[witness] INCOMPATIBLE: row {row} is prescribed to column "
                f"{forward[row]}, not {column}"
            )
        elif column in inverse and inverse[column] != row:
            print(
                f"[witness] INCOMPATIBLE: column {column} is prescribed to row "
                f"{inverse[column]}, not {row}"
            )
    print()

    if compatible_failing:
        print("VERDICT: COMPATIBLE_COUNTEREXAMPLE_AT_N24_RHO2")
        print(f"first compatible counterexample: {compatible_failing[0]}")
    else:
        print("VERDICT: NO_COMPATIBLE_COUNTEREXAMPLE_AT_N24_RHO2")
        print(
            "The 560 abstract failures are all unrealizable under F_n; the n=24 run "
            "refutes the trichotomy only as a statement about arbitrary quadruples."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
