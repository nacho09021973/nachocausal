"""FROZEN thresholds and protocol constants for pre-registration 001.

Every value here is frozen BEFORE any validation seed is generated/analysed, per
docs/preregistration.md:66-67. Each carries a principled anchor in a comment; no
value is reverse-engineered from a dev outcome (preregistration.md:49,55). The
written freeze with full justification is docs/preregistration_001_addendum.md;
a SHA256 of THIS file is recorded there as the seal.

Do not edit after the seal commit. A change here is a new pre-registration, not a
tweak.
"""

from __future__ import annotations

# --- Pinned numeric environment (cmte SWE CRITICAL-1) ------------------------
# The accelerator was verified bit-for-bit vs Minz under this numpy
# (commit 1e61bec, N=10017). The sealed estimator must run under the same.
PINNED_NUMPY = "1.26.4"


def assert_environment() -> None:
    """Hard-fail if the numpy version differs from the one the freeze was sealed
    under. Called by validate.py and dry_run.py (not at import, so tests and
    third-party inspection still import the package)."""
    import numpy as np

    if np.__version__ != PINNED_NUMPY:
        raise RuntimeError(
            f"nachocausal is sealed against numpy=={PINNED_NUMPY}; found "
            f"{np.__version__}. The frozen poset/estimator are only guaranteed "
            f"bit-reproducible under the pinned version (see addendum)."
        )


# --- Geometry (frozen): the tall box that sharpens the jump ------------------
# PHASE0_NOTES.md:41 "freeze the TALL geometry"; r in [0.1, 1.3] spans r_S.
T_EDGE = 6.0
R_EDGE = 1.2
R_CENTER = 0.7
R_S = 0.5                      # hidden Schwarzschild radius = 2M
BOX_AREA = T_EDGE * R_EDGE     # = 7.2
TWO_M = R_S                    # 2M = r_S = 0.5
M = R_S / 2.0                  # M = 0.25

# --- Ensemble / sampling (frozen) --------------------------------------------
INTENSITIES = (1500.0, 3000.0, 6000.0, 12000.0)   # 4 N levels -> convergence
PRIMARY_INTENSITY = 12000.0                        # single primary endpoint (cmte m1)
ENSEMBLE = 20                                      # seeds per (N, kind) (user decision)
MIN_VALID_SEEDS = 18                               # else that N is inconclusive (cmte m3)

# Same point cloud per seed: BH and MINK differ ONLY in causality
# (prototype_o.py:404-409) — the strongest box-match. The paired sign-flip
# permutation below is exact on this design.
SAME_CLOUD = True

# --- Seeds (frozen, disjoint) ------------------------------------------------
DEV_SEEDS = (20240617, 13, 101, 7, 42, 99, 2718, 31415)     # sweep_o2.py:27
VALIDATION_SEEDS = (
    11, 23, 57, 88, 137, 271, 314, 577, 911, 1618,
    2024, 4099, 5040, 6700, 7777, 8191, 9001, 12289, 27644, 65537,
)
assert len(VALIDATION_SEEDS) == ENSEMBLE
assert set(VALIDATION_SEEDS).isdisjoint(DEV_SEEDS), \
    "validation seeds must be disjoint from dev seeds (preregistration.md:66)"

# --- Boundary / significance machinery (frozen) ------------------------------
POOLED_SD_FLOOR = 0.5         # one O-discreteness unit; floors `sep` denom (cmte m2)

# theta_sig (i): paired sign-flip permutation on d_s = sep_BH(s) - sep_MINK(s)
# over the same-cloud seeds. Exact (enumerate 2^n flips for n <= this), else a
# random subsample. PASS if p_perm <= P_PERM_THRESHOLD. Replaces "z >= 5 (5 sigma)"
# (cmte CRITICAL): exact, tie-robust, no 1e-12 blow-up. Recorded as the
# dip -> permutation amendment in the addendum.
PERM_EXACT_MAX_N = 20          # enumerate 2^n exactly up to n=20
PERM_RANDOM_SAMPLES = 1_000_000
P_PERM_THRESHOLD = 1e-4

# theta_fp (iv): leave-one-out. A MINK seed is a "positive" iff its sep exceeds
# the FP_PERCENTILE of the held-out MINK null; require flagged fraction <= THETA_FP.
# One control calibration WITH (i), not independent evidence (cmte C2).
FP_PERCENTILE = 95.0
THETA_FP = 0.05

# --- Localisation / stability (frozen; anchored to the DISCRETENESS scale) ----
# ell is computed from the FROZEN INTENSITY and the FIXED box area, NEVER from
# the realized Poisson N (cmte C2), so the thresholds are literal constants.
K_LOC = 2                      # user decision; cannot localise finer than ~ell


def ell(intensity: float) -> float:
    """2D discreteness scale ell = rho^(-1/2), rho = intensity / box area."""
    return (intensity / BOX_AREA) ** -0.5


def theta_loc(intensity: float) -> float:
    """Bound on the order-statistic bracket width |dr|/(2M): k * ell / (2M)."""
    return K_LOC * ell(intensity) / TWO_M


def theta_stab(intensity: float) -> float:
    """Bound on the std of the blind boundary r-location across seeds: k * ell."""
    return K_LOC * ell(intensity)


# Frozen numeric table (for the addendum / quick reference).
THETA_LOC = {lam: theta_loc(lam) for lam in INTENSITIES}
THETA_STAB = {lam: theta_stab(lam) for lam in INTENSITIES}
ELL = {lam: ell(lam) for lam in INTENSITIES}

# --- Estimator-v2 (frozen; contract docs/estimator_v2_freeze.md) --------------
# Three changes vs prereg-001: (A) VOLUME observable, (C) tau(n) abstaining gate,
# (D) minimum-extent domain gate. Everything above is inherited verbatim.

# (D) Domain gate: a configuration with t_edge < T_EDGE_MIN is OUT-OF-DOMAIN
# (reported as outside the experiment's validity, NEVER a physical FAIL). Pinned
# to 6 by dev/explore_tmin.py (= the sealed T_EDGE, so BOX_AREA and the frozen
# ell/theta_loc table are unchanged). [freeze cl. D]
T_EDGE_MIN = 6.0

# (C) tau(n) abstaining gate: abstain (sep -> 0, no boundary claimed) iff
# improvement(O_min) < tau(n), where tau(n) is the (1 - GATE_ALPHA) quantile of
# `improvement` under an abstract Uniform[0,1] null at matched n, by Monte Carlo
# with the FROZEN seed/reps below. n = number of minimal elements (order-only).
# The table is precomputed into fixtures/tau_table.json over n in [2, N_MAX]
# (regenerate: scripts/gen_tau_table.py). Data-independent: no project seeds,
# no sprinkling, no ground truth enter it. [freeze cl. C]
GATE_ALPHA = 0.01                # tau = p99 of the abstract uniform null
GATE_NULL_MC_SEED = 20260621     # frozen MC seed
GATE_NULL_MC_REPS = 40000        # reps per n
GATE_TAU_N_MAX = 128             # table covers n in [2, 128]; production n <= ~71
