#!/usr/bin/env python3
"""Bounded structural probe for the existing exponential lower-bound family.

This does not enumerate ``S_n``.  It generates exactly the binary decorations
used in the proof ``|B_(8+k)| >= 2^floor(k/2)`` for at most three cells, applies
every single transposition, and delegates the global TIE/Aut recomputation to
the existing exact diagnostic.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product

from emergencia.p1a_tie_aut_repeated_block_probe import exact_diagnostic


KAPPA = (0, 1, 2, 4, 5, 7, 3, 6)
CORE_SIZE = len(KAPPA)
MAX_CELLS = 3
EXPECTED_GOOD_PAIRS = {
    (3, 6, "core_core"),
    (4, 5, "core_core"),
    (4, 6, "core_core"),
    (4, 7, "core_core"),
    (5, 6, "core_core"),
    (6, 7, "core_core"),
}


def decoration(word: tuple[int, ...], odd_residual: bool) -> tuple[int, ...]:
    """Return precisely the paired decreasing decoration from the proof."""

    size = 2 * len(word) + int(odd_residual)
    values = list(reversed(range(size)))
    for cell, bit in enumerate(word):
        if bit not in (0, 1):
            raise ValueError("decoration word must be binary")
        if bit:
            left = 2 * cell
            values[left], values[left + 1] = values[left + 1], values[left]
    return tuple(values)


def family_permutation(
    word: tuple[int, ...], odd_residual: bool
) -> tuple[int, ...]:
    suffix = decoration(word, odd_residual)
    return tuple(value + len(suffix) for value in KAPPA) + suffix


def transposition_class(
    left: int, right: int, word_length: int, odd_residual: bool
) -> str:
    if right < CORE_SIZE:
        return "core_core"
    if left < CORE_SIZE:
        if odd_residual and right == CORE_SIZE + 2 * word_length:
            return "core_residual"
        return "core_cell"

    left_local = left - CORE_SIZE
    right_local = right - CORE_SIZE
    residual = 2 * word_length
    if odd_residual and (left_local == residual or right_local == residual):
        return "cell_residual"
    if left_local // 2 == right_local // 2:
        return "within_cell"
    return "between_cells"


def probe(word: tuple[int, ...], odd_residual: bool) -> None:
    permutation = family_permutation(word, odd_residual)
    base = exact_diagnostic(permutation)
    if base.score != (3, 6) or base.n_orbits != 2:
        raise RuntimeError("lower-bound family member did not reproduce B")

    tested: Counter[str] = Counter()
    good: Counter[str] = Counter()
    good_pairs: list[tuple[int, int, str]] = []
    for left, right in combinations(range(len(permutation)), 2):
        category = transposition_class(left, right, len(word), odd_residual)
        tested[category] += 1
        modified = list(permutation)
        modified[left], modified[right] = modified[right], modified[left]
        diagnostic = exact_diagnostic(tuple(modified))
        if diagnostic.score is not None and diagnostic.n_orbits == 1:
            good[category] += 1
            good_pairs.append((left, right, category))

    if set(good_pairs) != EXPECTED_GOOD_PAIRS:
        raise RuntimeError("bounded word falsified the candidate exact outdegree law")

    encoded_word = "".join(str(bit) for bit in word)
    print(
        f"CELLS={len(word)} ODD={int(odd_residual)} WORD={encoded_word} "
        f"G={sum(good.values())} GOOD_BY_CLASS={dict(sorted(good.items()))} "
        f"TESTED_BY_CLASS={dict(sorted(tested.items()))} "
        f"GOOD_PAIRS={good_pairs}"
    )


def main() -> None:
    print("KNOWN_B_FAMILY_PROBE=BOUNDED_BINARY_WORDS_NO_S_N_SWEEP")
    for cells in range(1, MAX_CELLS + 1):
        for odd_residual in (False, True):
            for word in product((0, 1), repeat=cells):
                probe(word, odd_residual)


if __name__ == "__main__":
    main()
