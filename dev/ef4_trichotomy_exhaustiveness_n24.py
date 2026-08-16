"""FORO001-F1: exhaustive trichotomy enumeration for EF-4.3 at n=24, rho=2.

Authorised by `docs/scope_note_2026-08-16_foro001_falsification_test.md` §3.
Specified by `docs/foro/foro_decision_001_ef4-falsacion-adversarial.md:581-587`
(called `R-1` there; renamed `FORO001-F1` by the scope note §2).

The predicates are a literal replication of
`tests/test_p1a_entropia_fibras_ef4.py:63-154`; that sealed test is not modified.
This script only enlarges `n` from 12 to 24 and vectorises the enumeration.

Deterministic, seedless, read-only with respect to every sealed artefact.

Decision predicate, precommitted in scope note §5:
  * any tuple failing all three disjuncts  -> trichotomy REFUTED at finite n;
  * none failing                           -> NOT refuted at n=24 (no promotion);
  * `small_product = False` count == 0     -> the test is vacuous at n=24 too.

Run:  .venv/bin/python dev/ef4_trichotomy_exhaustiveness_n24.py
"""

from __future__ import annotations

import json
import sys
import time
from itertools import combinations
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from emergencia import p1a_entropia_fibras_ef4 as ef4  # noqa: E402


class Case:
    """All box-level tables for one (n, rho), mirroring the sealed test's setup."""

    def __init__(self, n: int, rho: int) -> None:
        self.n = n
        self.rho = rho
        self.half = n // 2
        prescribed = ef4.build_even_prescription(n, rho=rho)
        self.prescribed_points = sorted(prescribed.items())
        free_rows = sorted(set(range(1, n + 1)) - set(prescribed))
        free_columns = sorted(set(range(1, n + 1)) - set(prescribed.values()))
        self.free_count = len(free_rows)
        self.threshold = 1.0 / 8.0 + rho / self.free_count
        self.lower_stair = [
            point
            for point in self.prescribed_points
            if self.half - rho + 1 <= point[0] <= self.half - 1
        ]
        self.upper_stair = [
            point
            for point in self.prescribed_points
            if self.half + 2 <= point[0] <= self.half + rho
        ]

        # Interval tables over the C(n,2) ordered pairs (lo <= hi taken from a
        # 4-combination, so lo < hi always).
        self.pairs = list(combinations(range(1, n + 1), 2))
        self.pair_index = {pair: i for i, pair in enumerate(self.pairs)}
        n_pairs = len(self.pairs)

        self.row_free = np.array(
            [sum(lo <= r <= hi for r in free_rows) for lo, hi in self.pairs],
            dtype=np.int64,
        )
        self.col_free = np.array(
            [sum(lo <= c <= hi for c in free_columns) for lo, hi in self.pairs],
            dtype=np.int64,
        )

        # Box-level tables, indexed [row_pair, col_pair].
        self.n_prescribed = np.zeros((n_pairs, n_pairs), dtype=np.int8)
        self.hits_lower = np.zeros((n_pairs, n_pairs), dtype=bool)
        self.hits_upper = np.zeros((n_pairs, n_pairs), dtype=bool)
        row_lo = np.array([lo for lo, _ in self.pairs])[:, None]
        row_hi = np.array([hi for _, hi in self.pairs])[:, None]
        col_lo = np.array([lo for lo, _ in self.pairs])[None, :]
        col_hi = np.array([hi for _, hi in self.pairs])[None, :]
        for point_row, point_col in self.prescribed_points:
            inside = (
                (row_lo <= point_row)
                & (point_row <= row_hi)
                & (col_lo <= point_col)
                & (point_col <= col_hi)
            )
            self.n_prescribed += inside.astype(np.int8)
            if (point_row, point_col) in self.lower_stair:
                self.hits_lower |= inside
            if (point_row, point_col) in self.upper_stair:
                self.hits_upper |= inside

        # Quadruple tables: past box = (q0,q1), future box = (q2,q3).
        quads = list(combinations(range(1, n + 1), 4))
        self.n_quads = len(quads)
        self.past_pair = np.array(
            [self.pair_index[(q[0], q[1])] for q in quads], dtype=np.int64
        )
        self.future_pair = np.array(
            [self.pair_index[(q[2], q[3])] for q in quads], dtype=np.int64
        )
        # fixed_inner: past_upper == (half, half) and future_lower == (half+1, half+1)
        self.fixed_axis = np.array(
            [q[1] == self.half and q[2] == self.half + 1 for q in quads], dtype=bool
        )


def enumerate_case(case: Case) -> dict[str, object]:
    """Exhaustive sweep. Returns counts plus the first violating tuple, if any."""
    fc2 = float(case.free_count) ** 2
    col_free_past = case.col_free[case.past_pair].astype(np.float64)
    col_free_future = case.col_free[case.future_pair].astype(np.float64)

    # Per-row-pair gathers, precomputed once (n_pairs x n_quads).
    npresc_past = case.n_prescribed[:, case.past_pair]
    npresc_future = case.n_prescribed[:, case.future_pair]
    hits_lower_past = case.hits_lower[:, case.past_pair]
    hits_upper_past = case.hits_upper[:, case.past_pair]
    hits_lower_future = case.hits_lower[:, case.future_pair]
    hits_upper_future = case.hits_upper[:, case.future_pair]

    total = 0
    failures = 0
    non_vacuous = 0
    fixed_inner_true = 0
    loss_case_true = 0
    max_min_ratio = 0.0
    failing: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    biting: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    cap = case.rho + 2

    quads = list(combinations(range(1, case.n + 1), 4))

    for i in range(case.n_quads):
        row_past = case.past_pair[i]
        row_future = case.future_pair[i]

        past_product = case.row_free[row_past] * col_free_past / fc2
        future_product = case.row_free[row_future] * col_free_future / fc2
        min_product = np.minimum(past_product, future_product)
        small_product = min_product <= case.threshold

        past_crosses = hits_upper_past[row_past]
        future_crosses = hits_lower_future[row_future]
        past_loses = ~hits_lower_past[row_past]
        future_loses = ~hits_upper_future[row_future]
        past_prescribed = npresc_past[row_past]
        future_prescribed = npresc_future[row_future]

        loss_case = (
            (~past_crosses)
            & (~future_crosses)
            & (
                (past_loses & (past_prescribed <= 3) & (future_prescribed <= cap))
                | (future_loses & (future_prescribed <= 3) & (past_prescribed <= cap))
            )
        )
        fixed_inner = case.fixed_axis if case.fixed_axis[i] else False
        ok = small_product | loss_case
        if case.fixed_axis[i]:
            ok = ok | case.fixed_axis

        total += case.n_quads
        failures += int((~ok).sum())
        non_vacuous += int((~small_product).sum())
        loss_case_true += int(loss_case.sum())
        if case.fixed_axis[i]:
            fixed_inner_true += int(np.count_nonzero(fixed_inner))
        batch_max = float(min_product.max())
        if batch_max > max_min_ratio:
            max_min_ratio = batch_max
        if not small_product.all():
            for j in np.flatnonzero(~small_product):
                biting.append((quads[i], quads[int(j)]))
        if not ok.all():
            for j in np.flatnonzero(~ok):
                failing.append((quads[i], quads[int(j)]))

    return {
        "total": total,
        "failures": failures,
        "non_vacuous": non_vacuous,
        "fixed_inner_true": fixed_inner_true,
        "loss_case_true": loss_case_true,
        "max_min_ratio": max_min_ratio,
        "witness": failing[0] if failing else None,
        "failing": failing,
        "biting": biting,
    }


def report(case: Case, result: dict[str, object], label: str) -> None:
    print(f"[{label}] n={case.n} rho={case.rho}")
    print(f"[{label}] prescribed        = {case.prescribed_points}")
    print(f"[{label}] free_count        = {case.free_count}")
    print(f"[{label}] threshold         = {case.threshold:.6f}")
    print(f"[{label}] lower_stair       = {case.lower_stair}")
    print(f"[{label}] upper_stair       = {case.upper_stair}")
    print(f"[{label}] tuples            = {result['total']}")
    print(f"[{label}] max_min_ratio     = {result['max_min_ratio']:.6f}")
    print(f"[{label}] small_product=False (non-vacuous tuples) = {result['non_vacuous']}")
    print(f"[{label}] loss_case=True    = {result['loss_case_true']}")
    print(f"[{label}] fixed_inner=True  = {result['fixed_inner_true']}")
    print(f"[{label}] FAILURES (all three disjuncts false) = {result['failures']}")
    distinct_rows = sorted({rows for rows, _ in result["failing"]})
    distinct_cols = sorted({columns for _, columns in result["failing"]})
    print(f"[{label}] distinct failing row-quadruples    = {len(distinct_rows)}")
    print(f"[{label}] distinct failing column-quadruples = {len(distinct_cols)}")
    print(f"[{label}] failing row-quadruples  = {distinct_rows}")
    print(f"[{label}] first_witness     = {result['witness']}")


def main() -> int:
    # Control: n=12 must reproduce the sealed test's behaviour and the foro's
    # reported vacuity diagnostic (245025/245025 tuples with small_product=True).
    control = Case(12, 2)
    started = time.time()
    control_result = enumerate_case(control)
    report(control, control_result, "CONTROL n=12")
    print(f"[CONTROL n=12] elapsed_s = {time.time() - started:.1f}")
    assert control_result["total"] == 245_025, control_result["total"]
    assert control_result["failures"] == 0, "sealed n=12 test must pass"
    assert control_result["non_vacuous"] == 0, (
        "n=12 must be fully vacuous: small_product is unconditionally true there"
    )
    print()

    # FORO001-F1 proper.
    case = Case(24, 2)
    started = time.time()
    result = enumerate_case(case)
    report(case, result, "FORO001-F1 n=24")
    print(f"[FORO001-F1 n=24] elapsed_s = {time.time() - started:.1f}")
    assert result["total"] == 112_911_876, result["total"]
    assert case.threshold < 0.25, "n=24 must be the first size where the test can bite"

    payload = {
        key: value
        for key, value in result.items()
        if key not in ("failing", "biting")
    }
    payload["failing_tuples"] = [
        {"rows": list(rows), "columns": list(columns)}
        for rows, columns in result["failing"]
    ]
    payload["biting_tuples"] = [
        {"rows": list(rows), "columns": list(columns)}
        for rows, columns in result["biting"]
    ]
    payload["n"] = case.n
    payload["rho"] = case.rho
    payload["threshold"] = case.threshold
    payload["free_count"] = case.free_count
    payload["prescribed"] = [list(point) for point in case.prescribed_points]
    out_path = Path(__file__).resolve().parent / "EF4_TRICHOTOMY_N24_RESULT.json"
    out_path.write_text(json.dumps(payload, indent=2, default=list) + "\n")
    print(f"[FORO001-F1 n=24] wrote {out_path.name}")

    print()
    if result["failures"] > 0:
        print("VERDICT: TRICHOTOMY_REFUTED_AT_N24")
    elif result["non_vacuous"] == 0:
        print("VERDICT: VACUOUS_AT_N24 (test certifies nothing at this size)")
    else:
        print("VERDICT: NOT_REFUTED_AT_N24 (no promotion of any EF-4 token)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
