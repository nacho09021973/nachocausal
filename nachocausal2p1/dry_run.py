"""dry_run — MECHANICS-ONLY check that the 2+1 candidate pipeline runs end to end.

Before the freeze, the frozen theta values must NOT be compared with widths from the real
rho grid (comité 052, leakage (c)). This dry run therefore uses a tiny density OFF the grid,
on burned exploration seeds, and prints only counters and statuses — no widths, no theta
comparison, no verdict. The full-grid dry run belongs after C1.

Run: <sealed .venv>/bin/python -m nachocausal2p1.dry_run
"""

from __future__ import annotations

from . import thresholds, validate

MECHANICS_RHO = 2.0          # off the grid; N ~ 168 points per realisation
MECHANICS_SEEDS = thresholds.DRY_RUN_SEEDS[:3]


def main() -> None:
    thresholds.assert_environment()
    print(f"nachocausal2p1 MECHANICS-ONLY dry run (status {thresholds.STATUS}); "
          f"rho={MECHANICS_RHO} off-grid, seeds={MECHANICS_SEEDS}")
    for seed in MECHANICS_SEEDS:
        row = validate.per_seed(seed, MECHANICS_RHO, guard=True)
        keys = ("seed", "N", "invalid", "abstained_BH", "abstained_MINK",
                "n_minimal_BH", "n_minimal_MINK", "valid", "seconds")
        print({k: row.get(k) for k in keys})
    print("Guard-v raised on no causet; generator validity checks ran. Not a result.")


if __name__ == "__main__":
    main()
