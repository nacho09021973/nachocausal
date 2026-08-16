"""Independent scalar cross-check of FORO001-F1.

`ef4_trichotomy_exhaustiveness_n24.py` is a *vectorised* replication of
`tests/test_p1a_entropia_fibras_ef4.py:63-154`. A vectorised replication can be
wrong in ways that a REFUTED verdict must not rest on, so this file re-derives
the three disjuncts with a **literal scalar transcription** of the sealed test
body (sets and comprehensions, no numpy, no factorisation of the box products)
and checks:

  A. Full agreement on every one of the 245025 tuples at n=12 (the size the
     sealed test actually runs), for all five counters.
  B. Every tuple the vectorised sweep reported as FAILING at n=24 really does
     falsify all three disjuncts under the literal predicates.
  C. Every tuple the vectorised sweep reported as BITING at n=24
     (`small_product = False`, i.e. the region where the test is non-vacuous)
     really is non-vacuous, and its pass/fail classification agrees.

B and C together cover the entire region on which the verdict depends: outside
the biting set `small_product` is true and the tuple passes trivially.

Run *after* the enumeration script, which writes the JSON this reads:
  .venv/bin/python dev/ef4_trichotomy_witness_check_n24.py
"""

from __future__ import annotations

import json
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from emergencia import p1a_entropia_fibras_ef4 as ef4  # noqa: E402

import ef4_trichotomy_exhaustiveness_n24 as vectorised  # noqa: E402


def scalar_disjuncts(
    n: int, rho: int, rows: tuple[int, ...], columns: tuple[int, ...]
) -> dict[str, bool]:
    """Literal transcription of tests/test_p1a_entropia_fibras_ef4.py:63-154."""
    half = n // 2
    prescribed = ef4.build_even_prescription(n, rho=rho)
    prescribed_points = set(prescribed.items())
    free_rows = set(range(1, n + 1)) - set(prescribed)
    free_columns = set(range(1, n + 1)) - set(prescribed.values())
    free_count = len(free_rows)
    threshold = 1.0 / 8.0 + rho / free_count
    lower_stair = {
        point for point in prescribed_points if half - rho + 1 <= point[0] <= half - 1
    }
    upper_stair = {
        point for point in prescribed_points if half + 2 <= point[0] <= half + rho
    }

    def inside(point, lower, upper) -> bool:
        return lower[0] <= point[0] <= upper[0] and lower[1] <= point[1] <= upper[1]

    past_lower, past_upper, future_lower, future_upper = tuple(zip(rows, columns))
    past_free_product = (
        sum(past_lower[0] <= row <= past_upper[0] for row in free_rows)
        * sum(past_lower[1] <= column <= past_upper[1] for column in free_columns)
        / free_count**2
    )
    future_free_product = (
        sum(future_lower[0] <= row <= future_upper[0] for row in free_rows)
        * sum(future_lower[1] <= column <= future_upper[1] for column in free_columns)
        / free_count**2
    )
    fixed_inner = past_upper == (half, half) and future_lower == (half + 1, half + 1)
    small_product = min(past_free_product, future_free_product) <= threshold
    past_crosses = any(inside(point, past_lower, past_upper) for point in upper_stair)
    future_crosses = any(
        inside(point, future_lower, future_upper) for point in lower_stair
    )
    past_loses = not any(inside(point, past_lower, past_upper) for point in lower_stair)
    future_loses = not any(
        inside(point, future_lower, future_upper) for point in upper_stair
    )
    past_prescribed = sum(
        inside(point, past_lower, past_upper) for point in prescribed_points
    )
    future_prescribed = sum(
        inside(point, future_lower, future_upper) for point in prescribed_points
    )
    loss_case = (
        not past_crosses
        and not future_crosses
        and (
            (past_loses and past_prescribed <= 3 and future_prescribed <= rho + 2)
            or (future_loses and future_prescribed <= 3 and past_prescribed <= rho + 2)
        )
    )
    return {
        "fixed_inner": fixed_inner,
        "small_product": small_product,
        "loss_case": loss_case,
        "past_free_product": past_free_product,
        "future_free_product": future_free_product,
        "past_prescribed": past_prescribed,
        "future_prescribed": future_prescribed,
        "past_crosses": past_crosses,
        "future_crosses": future_crosses,
        "past_loses": past_loses,
        "future_loses": future_loses,
        "ok": fixed_inner or small_product or loss_case,
    }


def part_a() -> None:
    """Full scalar sweep at n=12, compared against the vectorised counters."""
    n, rho = 12, 2
    total = failures = non_vacuous = fixed_inner_true = loss_case_true = 0
    max_min_ratio = 0.0
    for rows in combinations(range(1, n + 1), 4):
        for columns in combinations(range(1, n + 1), 4):
            verdict = scalar_disjuncts(n, rho, rows, columns)
            total += 1
            failures += not verdict["ok"]
            non_vacuous += not verdict["small_product"]
            fixed_inner_true += verdict["fixed_inner"]
            loss_case_true += verdict["loss_case"]
            max_min_ratio = max(
                max_min_ratio,
                min(verdict["past_free_product"], verdict["future_free_product"]),
            )

    reference = vectorised.enumerate_case(vectorised.Case(n, rho))
    print("[A scalar n=12] total             =", total, "| vec:", reference["total"])
    print("[A scalar n=12] failures          =", failures, "| vec:", reference["failures"])
    print(
        "[A scalar n=12] small_product=False =",
        non_vacuous,
        "| vec:",
        reference["non_vacuous"],
    )
    print(
        "[A scalar n=12] fixed_inner=True   =",
        fixed_inner_true,
        "| vec:",
        reference["fixed_inner_true"],
    )
    print(
        "[A scalar n=12] loss_case=True     =",
        loss_case_true,
        "| vec:",
        reference["loss_case_true"],
    )
    print(
        "[A scalar n=12] max_min_ratio      =",
        f"{max_min_ratio:.6f}",
        "| vec:",
        f"{reference['max_min_ratio']:.6f}",
    )
    assert total == reference["total"] == 245_025
    assert failures == reference["failures"]
    assert non_vacuous == reference["non_vacuous"]
    assert fixed_inner_true == reference["fixed_inner_true"]
    assert loss_case_true == reference["loss_case_true"]
    assert abs(max_min_ratio - reference["max_min_ratio"]) < 1e-12
    print("[A scalar n=12] IMPLEMENTATIONS_AGREE")


def part_b_and_c(payload: dict) -> None:
    n, rho = payload["n"], payload["rho"]

    failing = payload["failing_tuples"]
    print(f"[B scalar n=24] re-checking {len(failing)} reported failures")
    for entry in failing:
        rows = tuple(entry["rows"])
        columns = tuple(entry["columns"])
        verdict = scalar_disjuncts(n, rho, rows, columns)
        assert not verdict["fixed_inner"], (rows, columns)
        assert not verdict["small_product"], (rows, columns)
        assert not verdict["loss_case"], (rows, columns)
    print("[B scalar n=24] ALL_REPORTED_FAILURES_CONFIRMED")

    biting = payload["biting_tuples"]
    print(f"[C scalar n=24] re-checking {len(biting)} biting tuples")
    scalar_failures = 0
    for entry in biting:
        rows = tuple(entry["rows"])
        columns = tuple(entry["columns"])
        verdict = scalar_disjuncts(n, rho, rows, columns)
        assert not verdict["small_product"], (rows, columns)
        scalar_failures += not verdict["ok"]
    print("[C scalar n=24] scalar failures within biting set =", scalar_failures)
    assert scalar_failures == payload["failures"], (
        scalar_failures,
        payload["failures"],
    )
    print("[C scalar n=24] CLASSIFICATION_AGREES")

    witness = failing[0]
    detail = scalar_disjuncts(n, rho, tuple(witness["rows"]), tuple(witness["columns"]))
    print()
    print("[WITNESS] rows    =", witness["rows"])
    print("[WITNESS] columns =", witness["columns"])
    for key in (
        "past_free_product",
        "future_free_product",
        "past_prescribed",
        "future_prescribed",
        "past_crosses",
        "future_crosses",
        "past_loses",
        "future_loses",
        "fixed_inner",
        "small_product",
        "loss_case",
    ):
        print(f"[WITNESS] {key:<20} = {detail[key]}")
    print(f"[WITNESS] threshold            = {payload['threshold']:.6f}")


def main() -> int:
    part_a()
    print()
    path = Path(__file__).resolve().parent / "EF4_TRICHOTOMY_N24_RESULT.json"
    payload = json.loads(path.read_text())
    part_b_and_c(payload)
    print()
    print("CROSS_CHECK: PASS — the REFUTED verdict does not rest on the vectorisation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
