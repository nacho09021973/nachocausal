"""dev seed hygiene — keep exploration seeds disjoint from everything that must
stay clean, and RESERVE an untouched band for a future pre-registration 002.

NOT sealed (dev/). Rules the committee pre-committed (2026-06-21):
  * DEV_SEEDS (sealed, small ints) and VALIDATION_SEEDS (<=65537, now BURNED)
    are off-limits for new tuning except as the canonical dev set.
  * EXPLORATION may draw fresh seeds for statistics/tuning, from a HIGH band that
    cannot collide with the above.
  * A separate band is RESERVED for prereg-002's held-out seeds and is NEVER
    evaluated during exploration, so the eventual confirmatory run is truly blind.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import thresholds  # noqa: E402

# Exploration tuning pool (seen freely during dev).
EXPLORE_POOL = tuple(1_000_000 + k for k in range(40))  # 1000000 .. 1000039

# Reserved, VIRGIN band for prereg-002 held-out seeds. Do NOT sprinkle/evaluate
# any seed in this band during exploration. The actual 002 set is drawn from here
# only at sealing time.
RESERVED_002_LO, RESERVED_002_HI = 2_000_000, 2_999_999


def in_reserved_002(seed: int) -> bool:
    return RESERVED_002_LO <= seed <= RESERVED_002_HI


def _assert_hygiene() -> None:
    dev = set(thresholds.DEV_SEEDS)
    val = set(thresholds.VALIDATION_SEEDS)
    pool = set(EXPLORE_POOL)
    assert pool.isdisjoint(dev), "explore pool collides with DEV_SEEDS"
    assert pool.isdisjoint(val), "explore pool collides with VALIDATION_SEEDS (burned)"
    assert not any(in_reserved_002(s) for s in pool), "explore pool enters reserved 002 band"
    assert all(in_reserved_002(s) for s in (RESERVED_002_LO, RESERVED_002_HI))


_assert_hygiene()

if __name__ == "__main__":
    print(f"EXPLORE_POOL: {len(EXPLORE_POOL)} seeds {EXPLORE_POOL[0]}..{EXPLORE_POOL[-1]}")
    print(f"RESERVED for prereg-002 held-out: [{RESERVED_002_LO}, {RESERVED_002_HI}] "
          f"(never evaluated in exploration)")
    print("hygiene asserts: OK (disjoint from DEV + burned VALIDATION; outside reserved band)")
