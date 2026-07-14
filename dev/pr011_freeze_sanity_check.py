"""PR011 freeze sanity checks — geometry only, no TV certification, no seeds.

Validates the numeric anchor in
`research_program/synthesis/pr011_mass_distinguishability_viability.md` §3.2 against the
diamond-family constraints (horizon straddle, r_q < tau < r_p).

Run: python3 dev/pr011_freeze_sanity_check.py
"""

from __future__ import annotations

import math
import sys


# Frozen anchor: shape A moderate (wp4_kappa_numeric_reference.py, wp4_fisher §5a)
V_P, R_P = 0.0, 2.0
V_Q, R_Q = 1.0, 0.5
TAU_FAMILY = (0.8, 1.2)
TAU_PAIR = (0.95, 1.05)


def w(tau: float, r: float) -> float:
    return math.exp(r / tau) * (r / tau - 1.0)


def u_tilde(tau: float, v: float, r: float) -> float:
    return -math.exp(-v / (2.0 * tau)) * w(tau, r)


def check_tau(tau: float) -> None:
    up = u_tilde(tau, V_P, R_P)
    uq = u_tilde(tau, V_Q, R_Q)
    if not (up < 0.0 < uq):
        raise AssertionError(f"tau={tau}: horizon straddle failed (Up={up}, Uq={uq})")
    if not (R_Q < tau < R_P):
        raise AssertionError(f"tau={tau}: need r_q < tau < r_p")


def main() -> int:
    for tau in (
        TAU_FAMILY[0],
        TAU_FAMILY[1],
        0.5 * (TAU_FAMILY[0] + TAU_FAMILY[1]),
        TAU_PAIR[0],
        TAU_PAIR[1],
    ):
        check_tau(tau)
    delta_commit = 0.25 * (TAU_FAMILY[1] - TAU_FAMILY[0])
    if abs(TAU_PAIR[1] - TAU_PAIR[0] - delta_commit) > 1e-12:
        raise AssertionError("certification pair separation != delta_tau_commit")
    print("PR011_FREEZE_SANITY=PASS")
    print(f"corners: p=({V_P},{R_P}) q=({V_Q},{R_Q})")
    print(f"tau_family={TAU_FAMILY} tau_pair={TAU_PAIR} delta_tau_commit={delta_commit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())