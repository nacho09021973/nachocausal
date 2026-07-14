"""PR012 (draft) — certified TV(τ0,τ1) vs Δτ curve at fixed n, on the frozen PR011 family G_◊.

Scope (per docs/comite/comite_decision_023_pr012-scope-adjudication.md, candidate (a), and the
PI's direct scoping directive superseding a follow-up /comite session — see
research_program/synthesis/pr012_tv_curve_scope.md §0 provenance note): reuse PR011's frozen
geometry G_◊ and N=n-conditioned channel exactly; do NOT extend the n-ladder (shown uninformative
at tractable n — see the scope doc); fix n and vary Δτ around the family center τ=1.0.

Two corrections over `dev/pr011_tv_certification_enumeration.py`, both required before any curve
point is trusted:

1. **Corrected tensorization.** PR011's fallback used `ε = ceil(n · copula_TV_upper)`, a loose
   n-fold union/data-processing bound, linear in n by construction (auditor_report_010/011). The
   analytically correct combination of n i.i.d. copula samples is via the Bhattacharyya
   coefficient: `BC_n = BC^n`, `H²_n = 2(1-BC_n)`, then the same Le Cam TV-from-Hellinger step
   applied to `H²_n`. This is **not** a negligible correction even at PR011's tractable n: for
   H² this small, `TV_tensorized/TV_naive ≈ 1/√n` exactly (verified in tests) — a ~2.8x tighter
   certified bound already at n=8 (0.00326 vs the published 0.00922), growing with n. The naive
   bound is the generic triangle-inequality/union bound (always valid, always looser); the
   tensorized one is the bound the Hellinger/Le Cam machinery actually supports.
2. **Two distinct, pre-existing error floors — neither invented after seeing a failure.**
   (a) A deep floating-point/quadrature noise floor: H²(Δτ) tracks the proved Fisher/QMD
   asymptotic `(Δτ²/4)·Ībar` to within a stable ~2% (a genuine higher-order Taylor residual, not
   noise) across eleven decades of Δτ, only departing from that law below Δτ≈1e-13. Frozen hard
   floor `DELTA_TAU_FLOOR = 1e-9` carries a >10,000x safety margin below that measured breakdown —
   no curve point is ever attempted below it.
   (b) A much coarser, already-frozen grid-RESOLUTION gate: PR011's own
   `verify_hellinger_stability` (unmodified, imported below) rejects any `(tau_a,tau_b)` where the
   `M=100` vs `M=72` quadrature grids disagree by more than `HELLINGER_H2_REL_TOL=1e-3` — this is
   PR011's frozen instability guard, not a new PR012 threshold, and it binds well before (a) does
   (empirically, around Δτ≲0.03 at the M=100/72 pair, vs Δτ≈1e-13 for (a)). Any curve point this
   gate rejects is reported as an explicit `GRID_RESOLUTION_ABSTAIN` row (falsifier's ask,
   comite_decision_023 §5) — never silently dropped, never re-tried at a hand-picked resolution
   after seeing it fail.

Run:
  python3 dev/pr012_tv_curve_certification.py sanity
  python3 dev/pr012_tv_curve_certification.py curve --dry-run
  python3 dev/pr012_tv_curve_certification.py curve
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent
sys.path.insert(0, str(_ROOT))
sys.path.insert(0, str(_ROOT / "research_program" / "work_packages"))

from dev.pr011_tv_certification_enumeration import (  # noqa: E402
    R_P,
    R_Q,
    TAU_FAMILY,
    V_P,
    V_Q,
    TERMINAL_DISTINGUISHABLE,
    TERMINAL_INCOMPLETE,
    TERMINAL_INDISTINGUISHABLE,
    build_diamond_family,
    certified_tv_upper,
    terminal_for_epsilon,
    verify_hellinger_stability,
)

# Reused from PR011's frozen anchor (research_program/synthesis/pr011_mass_distinguishability_viability.md
# §3.1) — not redefined, imported, so PR012 cannot silently drift from PR011's geometry.
assert (R_P, V_P, R_Q, V_Q) == (2.0, 0.0, 0.5, 1.0)
assert TAU_FAMILY == (0.8, 1.2)

# --- PR012 frozen numeric anchor (candidate (a): fixed n, Δτ curve) ---
TAU_CENTER = 1.0
FAMILY_FULL_SPAN = TAU_FAMILY[1] - TAU_FAMILY[0]  # 0.4
FIXED_N = 8  # largest already-certified, most-audited rung of the PR011 ladder; not extended.

# Frozen BEFORE any point is computed — fractions of the full family span, not chosen from data.
DELTA_TAU_LADDER: tuple[float, ...] = tuple(
    round(FAMILY_FULL_SPAN * frac, 10) for frac in (1 / 32, 1 / 16, 1 / 8, 1 / 4, 1 / 2, 1)
)  # (0.0125, 0.025, 0.05, 0.1, 0.2, 0.4) — includes PR011's own certified Δτ=0.1 as a cross-check.

# Derived from an error model (module docstring point 2), not from an observed failure.
DELTA_TAU_FLOOR = 1e-9

REPORT_DIR = _ROOT / "data" / "reports"
CURVE_CSV_PATH = REPORT_DIR / "pr012_tv_curve_n8.csv"
CURVE_SHA256_PATH = REPORT_DIR / "pr012_tv_curve_n8.sha256"

CURVE_CSV_FIELDS = (
    "n",
    "tau_a",
    "tau_b",
    "delta_tau",
    "method",
    "epsilon_certified_upper",
    "epsilon_naive_linear_for_comparison",
    "minimax_error_floor",
    "terminal",
    "hellinger_H2",
    "hellinger_H2_crosscheck",
)


TERMINAL_GRID_ABSTAIN = "GRID_RESOLUTION_ABSTAIN"


@dataclass(frozen=True)
class CurvePoint:
    n: int
    tau_a: float
    tau_b: float
    delta_tau: float
    method: str
    epsilon_certified_upper: float | None
    epsilon_naive_linear_for_comparison: float | None
    minimax_error_floor: float | None
    terminal: str
    hellinger_H2: float | None
    hellinger_H2_crosscheck: float | None


def bhattacharyya_tv_upper(h2_single: float, n: int) -> float:
    """Correctly tensorized Le Cam TV upper bound for n i.i.d. copula samples.

    BC_n = BC^n (Bhattacharyya coefficient tensorizes exactly under independence);
    H^2_n = 2(1 - BC_n); TV_n <= sqrt(H^2_n) * sqrt(1 - H^2_n/4) (same Le Cam step PR011 already
    uses, applied here to the exact H^2_n instead of the loose product bound n*H^2_single).
    """
    if not (0.0 <= h2_single <= 2.0):
        raise ValueError(f"Hellinger squared out of range: {h2_single}")
    bc = 1.0 - h2_single / 2.0
    bc_n = bc**n
    h2_n = 2.0 * (1.0 - bc_n)
    if h2_n <= 0.0:
        return 0.0
    return math.sqrt(h2_n) * math.sqrt(1.0 - h2_n / 4.0)


def naive_linear_tv_upper(h2_single: float, n: int) -> float:
    """PR011's original (loose) n-fold union bound, kept only as a documented comparison
    column — never the certified value in PR012."""
    copula_bound = math.sqrt(h2_single) * math.sqrt(1.0 - h2_single / 4.0)
    return min(1.0, n * copula_bound)


def n_for_target_tv(h2_single: float, target_tv: float) -> float:
    """Diagnostic only (not part of certification): analytically invert bhattacharyya_tv_upper
    to find the n at which the tight bound would reach `target_tv`. Used in this module's own
    tests as a sanity check on the closed-form inversion, and documents the scale discussed with
    the PI (n ~ 1e5-1e7 for near-certain separation at the PR011 anchor's H^2)."""
    if not (0.0 < target_tv < 1.0):
        raise ValueError("target_tv must be in (0,1)")
    bc = 1.0 - h2_single / 2.0
    x = 2.0 - 2.0 * math.sqrt(1.0 - target_tv**2)  # x = H^2_n
    bc_n = 1.0 - x / 2.0
    return math.log(bc_n) / math.log(bc)


def assert_not_scale_related(tau_a: float, tau_b: float) -> None:
    """Sanity check re-run at every curve point (mathematician brief, comite_decision_023 §4).

    Theorem A's TV=0 degeneracy (first_witness_pair_candidates.md §2) applies only to a pair
    related by a pure dilation Phi_s, which requires BOTH tau and the corners to scale by
    s=tau_b/tau_a together. `build_diamond_family` (imported above) closes over the module-level
    constants R_P,V_P,R_Q,V_Q and never rescales them by tau -- every curve point uses the
    identical, tau-independent corners. So no two curve points can be a Phi_s-image of each other
    by construction, not by a per-pair numeric coincidence; the only thing left to guard at
    runtime is that a genuine (non-degenerate) pair was requested."""
    if tau_a == tau_b:
        raise ValueError("delta_tau=0: not a comparison pair")


def certify_curve_point(delta_tau: float, n: int = FIXED_N) -> CurvePoint:
    if delta_tau < DELTA_TAU_FLOOR:
        raise ValueError(
            f"delta_tau={delta_tau} is below the frozen numerical floor "
            f"DELTA_TAU_FLOOR={DELTA_TAU_FLOOR} (see module docstring point 2) -- abstain, "
            "do not certify below this floor"
        )
    tau_a = TAU_CENTER - delta_tau / 2
    tau_b = TAU_CENTER + delta_tau / 2
    if not (TAU_FAMILY[0] <= tau_a <= tau_b <= TAU_FAMILY[1]):
        raise ValueError(f"(tau_a={tau_a}, tau_b={tau_b}) outside frozen family {TAU_FAMILY}")
    assert_not_scale_related(tau_a, tau_b)

    try:
        h2, h2_x = verify_hellinger_stability(tau_a, tau_b)
    except RuntimeError:
        # PR011's own frozen M=100/M=72 stability gate rejected this point (module docstring
        # point 2(b)) -- report an explicit abstain row, never silently drop it or retry at a
        # hand-picked resolution chosen after seeing the failure.
        return CurvePoint(
            n=n,
            tau_a=tau_a,
            tau_b=tau_b,
            delta_tau=delta_tau,
            method="HELLINGER_FALLBACK_TENSORIZED",
            epsilon_certified_upper=None,
            epsilon_naive_linear_for_comparison=None,
            minimax_error_floor=None,
            terminal=TERMINAL_GRID_ABSTAIN,
            hellinger_H2=None,
            hellinger_H2_crosscheck=None,
        )
    epsilon = certified_tv_upper(bhattacharyya_tv_upper(h2, n))
    epsilon_naive = certified_tv_upper(naive_linear_tv_upper(h2, n))
    terminal = terminal_for_epsilon(epsilon)
    minimax_floor = (1.0 - epsilon) / 2.0 if epsilon < 1.0 else 0.0

    return CurvePoint(
        n=n,
        tau_a=tau_a,
        tau_b=tau_b,
        delta_tau=delta_tau,
        method="HELLINGER_FALLBACK_TENSORIZED",
        epsilon_certified_upper=epsilon,
        epsilon_naive_linear_for_comparison=epsilon_naive,
        minimax_error_floor=minimax_floor,
        terminal=terminal,
        hellinger_H2=h2,
        hellinger_H2_crosscheck=h2_x,
    )


def certify_curve(
    delta_tau_ladder: Sequence[float] = DELTA_TAU_LADDER, n: int = FIXED_N
) -> list[CurvePoint]:
    return [certify_curve_point(dt, n=n) for dt in delta_tau_ladder]


def render_curve_csv(points: Sequence[CurvePoint]) -> bytes:
    lines = [",".join(CURVE_CSV_FIELDS)]
    for p in points:
        row = {
            "n": str(p.n),
            "tau_a": repr(p.tau_a),
            "tau_b": repr(p.tau_b),
            "delta_tau": repr(p.delta_tau),
            "method": p.method,
            "epsilon_certified_upper": repr(p.epsilon_certified_upper),
            "epsilon_naive_linear_for_comparison": repr(p.epsilon_naive_linear_for_comparison),
            "minimax_error_floor": repr(p.minimax_error_floor),
            "terminal": p.terminal,
            "hellinger_H2": repr(p.hellinger_H2),
            "hellinger_H2_crosscheck": repr(p.hellinger_H2_crosscheck),
        }
        lines.append(",".join(row[f] for f in CURVE_CSV_FIELDS))
    return ("\n".join(lines) + "\n").encode("utf-8")


def publish_curve(points: Sequence[CurvePoint]) -> None:
    if CURVE_CSV_PATH.exists() or CURVE_SHA256_PATH.exists():
        raise RuntimeError("refusing to overwrite existing pr012 curve artifact")
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    data = render_curve_csv(points)
    CURVE_CSV_PATH.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    CURVE_SHA256_PATH.write_bytes(f"{digest}  {CURVE_CSV_PATH.name}\n".encode("ascii"))


def _fmt(value: float | None, spec: str) -> str:
    return format(value, spec) if value is not None else "n/a"


def _print_curve(points: Sequence[CurvePoint]) -> None:
    print("PR012_CURVE=OK (DRAFT -- not yet frozen for publication, see scope doc §0)")
    print(f"n={FIXED_N}  tau_center={TAU_CENTER}  method=HELLINGER_FALLBACK_TENSORIZED")
    for p in points:
        print(
            f"delta_tau={p.delta_tau:<8} eps_certified={_fmt(p.epsilon_certified_upper, '.12f')}  "
            f"eps_naive_linear={_fmt(p.epsilon_naive_linear_for_comparison, '.12f')}  "
            f"minimax_error_floor={_fmt(p.minimax_error_floor, '.6f')}  terminal={p.terminal}"
        )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("sanity", help="geometry-only checks, no TV computation")

    curve_cmd = sub.add_parser("curve", help="certify the frozen Delta-tau curve at n=8")
    curve_cmd.add_argument("--dry-run", action="store_true")

    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.command == "sanity":
        for dt in DELTA_TAU_LADDER:
            assert_not_scale_related(TAU_CENTER - dt / 2, TAU_CENTER + dt / 2)
        print("PR012_SANITY=PASS")
        return 0

    points = certify_curve()
    if not args.dry_run:
        publish_curve(points)
    _print_curve(points)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
