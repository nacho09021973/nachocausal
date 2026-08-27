#!/usr/bin/env python3
"""Bounded falsifier for inflating interiors of the resistant core.

The two maximizers of ``KAPPA`` share positions 1 and 4 as score-contributing
interval interiors; position 6 is neutral.  This probe replaces either the two
score interiors, or those two plus the neutral position, by equally sized
arbitrary permutation blocks.  It checks all local ``S_2`` choices and three
fixed diagonal ``S_3`` choices.  It never enumerates ``S_n`` and delegates every
global maximizer/orbit calculation to the existing exact diagnostic.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product, permutations

from emergencia.p1a_tie_aut_repeated_block_probe import exact_diagnostic


KAPPA = (0, 1, 2, 4, 5, 7, 3, 6)
SCORE_INTERIORS = (1, 4)
OPTIONAL_NEUTRAL_POSITION = 6


def inflate_interiors(
    local_blocks: dict[int, tuple[int, ...]],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Inflate selected positions, returning the permutation and module labels."""

    sizes = {
        position: len(local_blocks.get(position, (0,)))
        for position in range(len(KAPPA))
    }
    offsets: dict[int, int] = {}
    offset = 0
    for base_value in range(len(KAPPA)):
        position = KAPPA.index(base_value)
        offsets[position] = offset
        offset += sizes[position]

    values: list[int] = []
    module_labels: list[int] = []
    for position in range(len(KAPPA)):
        local = local_blocks.get(position, (0,))
        if tuple(sorted(local)) != tuple(range(len(local))):
            raise ValueError("each local block must be a permutation")
        values.extend(offsets[position] + value for value in local)
        module_labels.extend([position] * len(local))
    return tuple(values), tuple(module_labels)


def transposition_class(
    left: int,
    right: int,
    module_labels: tuple[int, ...],
    inflated_positions: tuple[int, ...],
) -> str:
    left_module = module_labels[left]
    right_module = module_labels[right]
    if left_module == right_module:
        return "within_interior_module"
    left_inflated = left_module in inflated_positions
    right_inflated = right_module in inflated_positions
    if left_inflated and right_inflated:
        return "between_interior_modules"
    if left_inflated or right_inflated:
        return "interior_singleton"
    return "singleton_singleton"


def probe(
    inflated_positions: tuple[int, ...],
    name: str,
    blocks: tuple[tuple[int, ...], ...],
) -> None:
    if len(blocks) != len(inflated_positions):
        raise ValueError("one local block is required per inflated position")
    local_blocks = dict(zip(inflated_positions, blocks))
    permutation, module_labels = inflate_interiors(local_blocks)
    twin_size = len(blocks[0])
    if any(len(block) != twin_size for block in blocks):
        raise ValueError("the three interior blocks must have equal size")

    base = exact_diagnostic(permutation)
    expected_score = (twin_size + 2, 2 * twin_size + 4)
    if base.score != expected_score or base.n_orbits != 2:
        print(
            f"POSITIONS={inflated_positions} T={twin_size} BLOCKS={name} "
            f"N={len(permutation)} "
            f"BASE_SCORE={base.score} BASE_R={base.n_orbits} FAMILY_MEMBER=NO"
        )
        return

    tested: Counter[str] = Counter()
    good: Counter[str] = Counter()
    good_module_pairs: Counter[tuple[int, int]] = Counter()
    good_46_local: list[tuple[int, int]] = []
    first_good: dict[str, tuple[int, int]] = {}
    module_offsets: dict[int, int] = {}
    for index, module in enumerate(module_labels):
        module_offsets.setdefault(module, index)
    for left, right in combinations(range(len(permutation)), 2):
        category = transposition_class(
            left, right, module_labels, inflated_positions
        )
        tested[category] += 1
        modified = list(permutation)
        modified[left], modified[right] = modified[right], modified[left]
        diagnostic = exact_diagnostic(tuple(modified))
        if diagnostic.score is not None and diagnostic.n_orbits == 1:
            good[category] += 1
            good_module_pairs[(module_labels[left], module_labels[right])] += 1
            if (module_labels[left], module_labels[right]) == (4, 6):
                good_46_local.append(
                    (left - module_offsets[4], right - module_offsets[6])
                )
            first_good.setdefault(category, (left, right))

    print(
        f"POSITIONS={inflated_positions} T={twin_size} BLOCKS={name} "
        f"N={len(permutation)} FAMILY_MEMBER=YES "
        f"G={sum(good.values())} GOOD_BY_CLASS={dict(sorted(good.items()))} "
        f"GOOD_BY_MODULE_PAIR={dict(sorted(good_module_pairs.items()))} "
        f"GOOD_46_LOCAL={good_46_local} "
        f"TESTED_BY_CLASS={dict(sorted(tested.items()))} "
        f"FIRST_GOOD={dict(sorted(first_good.items()))}"
    )


def main() -> None:
    print("INTERIOR_INFLATION_PROBE=BOUNDED_NO_S_N_SWEEP")
    two_blocks = tuple(permutations(range(2)))
    position_sets = (
        SCORE_INTERIORS,
        SCORE_INTERIORS + (OPTIONAL_NEUTRAL_POSITION,),
    )
    for inflated_positions in position_sets:
        for indices in product(
            range(len(two_blocks)), repeat=len(inflated_positions)
        ):
            probe(
                inflated_positions,
                "".join(map(str, indices)),
                tuple(two_blocks[index] for index in indices),
            )

    three_blocks = {
        "increasing": tuple(range(3)),
        "decreasing": tuple(reversed(range(3))),
        "zigzag": (0, 2, 1),
    }
    for inflated_positions in position_sets:
        for name, block in three_blocks.items():
            probe(
                inflated_positions,
                name,
                (block,) * len(inflated_positions),
            )


if __name__ == "__main__":
    main()
