#!/usr/bin/env python3
"""Bounded falsifier for the chain-dominant factorial family.

No permutation space is enumerated.  For k=2,3,4 this checks three fixed block
realizers and recomputes the global TIE/Aut diagnostic after every transposition.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from emergencia.p1a_tie_aut_repeated_block_probe import exact_diagnostic


K_VALUES = (2, 3, 4)


def block_realizers(k: int) -> dict[str, tuple[int, ...]]:
    return {
        "increasing": tuple(range(k)),
        "decreasing": tuple(reversed(range(k))),
        "zigzag": tuple(range(0, k, 2)) + tuple(range(1, k, 2)),
    }


def factorial_member(block: tuple[int, ...]) -> tuple[tuple[int, ...], int]:
    k = len(block)
    chain_size = 2 * k + 3
    chain = tuple(range(k, k + chain_size))
    return chain + block, chain_size


def transposition_class(left: int, right: int, chain_size: int) -> str:
    if right < chain_size:
        return "chain_chain"
    if left >= chain_size:
        return "block_block"
    return "chain_block"


def probe(name: str, block: tuple[int, ...]) -> None:
    permutation, chain_size = factorial_member(block)
    base = exact_diagnostic(permutation)
    expected_score = ((chain_size - 1) // 2, chain_size)
    if base.score != expected_score or base.n_orbits != 2:
        raise RuntimeError("factorial-family base did not reproduce B")

    tested: Counter[str] = Counter()
    good: Counter[str] = Counter()
    chain_good: list[tuple[int, int]] = []
    cross_good: list[tuple[int, int]] = []
    for left, right in combinations(range(len(permutation)), 2):
        category = transposition_class(left, right, chain_size)
        tested[category] += 1
        modified = list(permutation)
        modified[left], modified[right] = modified[right], modified[left]
        diagnostic = exact_diagnostic(tuple(modified))
        if diagnostic.score is not None and diagnostic.n_orbits == 1:
            good[category] += 1
            if category == "chain_chain":
                chain_good.append((left, right))
            elif category == "chain_block":
                cross_good.append((left, right - chain_size))

    bulk_cross = {
        (chain_index, block_index)
        for chain_index in range(2, chain_size - 2)
        for block_index in range(len(block))
    }
    if not bulk_cross <= set(cross_good):
        raise RuntimeError("bounded block falsified the uniform bulk-cross rectangle")
    if good["block_block"] != 0:
        raise RuntimeError("a block-only swap unexpectedly repaired the dominant chain")

    print(
        f"K={len(block)} BLOCK={name} N={len(permutation)} G={sum(good.values())} "
        f"GOOD_BY_CLASS={dict(sorted(good.items()))} "
        f"TESTED_BY_CLASS={dict(sorted(tested.items()))} "
        f"CHAIN_GOOD={chain_good} CROSS_GOOD={cross_good}"
    )


def main() -> None:
    print("FACTORIAL_FAMILY_PROBE=BOUNDED_FIXED_BLOCKS_NO_S_K_SWEEP")
    for k in K_VALUES:
        for name, block in block_realizers(k).items():
            probe(name, block)


if __name__ == "__main__":
    main()
