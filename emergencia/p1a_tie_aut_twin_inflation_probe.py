#!/usr/bin/env python3
"""Bounded falsifier for antichain-twin inflations of the resistant core.

This checks t=1,2 and three fixed arbitrary suffix blocks.  It never enumerates
``S_k`` and delegates every global maximizer/orbit calculation to the existing
exact diagnostic.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from emergencia.p1a_tie_aut_repeated_block_probe import exact_diagnostic


KAPPA = (0, 1, 2, 4, 5, 7, 3, 6)


def inflated_core(twin_size: int) -> tuple[int, ...]:
    values: list[int] = []
    for base_value in KAPPA:
        block = range(base_value * twin_size, (base_value + 1) * twin_size)
        values.extend(reversed(tuple(block)))
    return tuple(values)


def block_realizers(size: int) -> dict[str, tuple[int, ...]]:
    return {
        "increasing": tuple(range(size)),
        "decreasing": tuple(reversed(range(size))),
        "zigzag": tuple(range(0, size, 2)) + tuple(range(1, size, 2)),
    }


def family_member(twin_size: int, block: tuple[int, ...]) -> tuple[int, ...]:
    core = inflated_core(twin_size)
    return tuple(value + len(block) for value in core) + block


def transposition_class(
    left: int, right: int, core_size: int, twin_size: int
) -> str:
    if right < core_size:
        if left // twin_size == right // twin_size:
            return "within_twin_class"
        return "between_core_classes"
    if left >= core_size:
        return "block_block"
    return "core_block"


def probe(twin_size: int, name: str, block: tuple[int, ...]) -> None:
    permutation = family_member(twin_size, block)
    core_size = 8 * twin_size
    base = exact_diagnostic(permutation)
    expected_score = (twin_size + 2, 2 * twin_size + 4)
    if base.score != expected_score or base.n_orbits != 2:
        raise RuntimeError("twin inflation did not preserve the resistant core")

    tested: Counter[str] = Counter()
    good: Counter[str] = Counter()
    first_good: dict[str, tuple[int, int]] = {}
    good_pairs: list[tuple[int, int, str]] = []
    for left, right in combinations(range(len(permutation)), 2):
        category = transposition_class(left, right, core_size, twin_size)
        tested[category] += 1
        modified = list(permutation)
        modified[left], modified[right] = modified[right], modified[left]
        diagnostic = exact_diagnostic(tuple(modified))
        if diagnostic.score is not None and diagnostic.n_orbits == 1:
            good[category] += 1
            first_good.setdefault(category, (left, right))
            good_pairs.append((left, right, category))

    print(
        f"T={twin_size} K={len(block)} BLOCK={name} N={len(permutation)} "
        f"G={sum(good.values())} GOOD_BY_CLASS={dict(sorted(good.items()))} "
        f"TESTED_BY_CLASS={dict(sorted(tested.items()))} "
        f"FIRST_GOOD={dict(sorted(first_good.items()))} "
        f"GOOD_PAIRS={good_pairs}"
    )


def main() -> None:
    print("TWIN_INFLATION_PROBE=BOUNDED_NO_S_K_SWEEP")
    for twin_size in (1, 2):
        block_size = twin_size + 1
        for name, block in block_realizers(block_size).items():
            probe(twin_size, name, block)


if __name__ == "__main__":
    main()
