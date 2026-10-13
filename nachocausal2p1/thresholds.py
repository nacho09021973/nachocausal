"""prereg-004 CANDIDATE thresholds and protocol constants for the 2+1D equatorial bench.

STATUS: CANDIDATE — NOT FROZEN. This file becomes the prereg-004 seal only at step C1 of
committee 052 (docs/comite/comite_decision_052_prereg004-2p1-design.md §9), committed together
with docs/preregistration_004.md, after steps 3-7 are green and with explicit PI authorisation.
Until then any value may change; after C1, a change is a new pre-registration.

Every value carries its source. Sources:
  [PI-052]  PI decisions transcribed in comité 052 §11 (2026-10-13);
  [C052-n]  comité 052 §8 synthesis item n (recommendation, not yet signed);
  [ASTRA]   blind theta anchor, revisiones/2026-10-13-anclaje-theta-ciego/astra.md;
  [PI-S3]   PI choices made in chat on 2026-10-13 for the step-3 port (the two 1+1 clauses
            with no 2+1 definition, comité 052 §5 item 3 / §8 item 8);
  [GEN]     values copied from dev/gen2p1_efbox.py (frozen with the generator, C052-1).
Nothing here is reverse-engineered from a dev outcome. The theta values have NOT been compared
with dev widths and must not be before the freeze (comité 052 falsifier, leakage (c)).

The sealed 1+1 package (nachocausal/thresholds.py, SHA 6e2c3888...) is NOT edited or imported
for any threshold; only its frozen estimator primitives and tau procedure are reused.
"""

from __future__ import annotations

import math
import os
import sys

STATUS = "CANDIDATE_NOT_FROZEN"

# --- Pinned numeric environment (C052-1: hard-pin numba, llvmlite, scipy) -------------------
# Versions of the sealed CPU .venv (requirements-lock.txt, Python 3.12.3).
PINNED_NUMPY = "1.26.4"
PINNED_NUMBA = "0.66.0"
PINNED_LLVMLITE = "0.48.0"
PINNED_SCIPY = "1.17.1"
PINNED_PYTHON = "3.12.3"


def assert_environment() -> None:
    """Hard-fail outside the pinned CPU environment. The blind run is CPU-only (acta
    gpu_dev_only): CuPy must not be loaded and NC2P1_DEVICE must be unset or 'cpu'.
    Called by validate.run and dry_run (not at import)."""
    import llvmlite
    import numba
    import numpy as np
    import scipy

    found = {"python": sys.version.split()[0], "numpy": np.__version__,
             "numba": numba.__version__, "llvmlite": llvmlite.__version__,
             "scipy": scipy.__version__}
    want = {"python": PINNED_PYTHON, "numpy": PINNED_NUMPY, "numba": PINNED_NUMBA,
            "llvmlite": PINNED_LLVMLITE, "scipy": PINNED_SCIPY}
    bad = {k: (found[k], want[k]) for k in want if found[k] != want[k]}
    if bad:
        raise RuntimeError(f"nachocausal2p1 environment differs from the pins: {bad}")
    if any(m == "cupy" or m.startswith("cupy.") for m in sys.modules):
        raise RuntimeError("CuPy is loaded: the 2+1 blind path is CPU-only (gpu_dev_only).")
    if os.environ.get("NC2P1_DEVICE", "cpu") != "cpu":
        raise RuntimeError("NC2P1_DEVICE must be unset or 'cpu' on the 2+1 blind path.")


# --- Geometry -------------------------------------------------------------------------------
# Ingoing-EF box t* in [0, T_EDGE], r in [R_LO, R_HI], phi in S^1; 2M = 0.5 (mirrors 1+1).
T_EDGE = 16.0                  # [PI-052] a MARGIN above t_min = 10 (max over the grid); not a
                               # Decision-2 pass; the plateau [T, 2T] is unmeasured at T = 16.
R_LO, R_HI = 0.1, 1.3          # [GEN] = sealed 1+1 r-range (C052: do not vary it)
TWO_M = 0.5                    # 2M; used ONLY as a scoring unit
VOL_PER_T = math.pi * (R_HI ** 2 - R_LO ** 2)   # 2+1 volume per unit t* (sqrt(-g) = r)
BOX_VOLUME = T_EDGE * VOL_PER_T

# Domain gate: T_EDGE < T_EDGE_MIN -> OUT_OF_DOMAIN (never a physical FAIL). [C052-9]
# Re-pinned at the max measured t_min over the grid (8/10/10). Non-firing at T = 16: it is
# NOT counted as a safeguard.
T_EDGE_MIN = 10.0

# --- Density grid and ensemble ------------------------------------------------------------------
# Thresholds are keyed by rho (points per unit 2+1 volume) at the frozen T, never by realised N.
RHO_GRID = (32.0, 63.0, 126.0)     # [C052-4] ascending
PRIMARY_RHO = 126.0                # [C052-4] highest rho with measured t_min
ENSEMBLE = 20                      # [C052-3] (i) needs >= 14 valid seeds to be passable
MIN_VALID_SEEDS = 18               # [C052-3] fewer generator-valid seeds -> INCONCLUSIVE


def n_mean(rho: float) -> int:
    """Poisson mean of the sprinkle at density rho (as dev/sweep_2p1_T.py)."""
    return int(round(rho * BOX_VOLUME))


# --- Seeds -------------------------------------------------------------------------------------
EXPLORE_BAND = (7_000_000, 7_000_999)   # 2+1 exploration band (dev)
VIRGIN_BAND = (8_000_000, 8_999_999)    # reserved for the single prereg-004 blind draw
# Burned dev seeds used for the T sweeps at rho = 32/63/126; dry runs and the step-4
# can-fail test may reuse them (comité 052 §9 step 4), never virgin seeds.
DRY_RUN_SEEDS = tuple(range(7_000_100, 7_000_110))
# Not drawn yet: step C2 draws 20 seeds ONCE and BLIND from VIRGIN_BAND, after C1.
VALIDATION_DRAW_SEED = None
VALIDATION_SEEDS: tuple = ()
assert all(EXPLORE_BAND[0] <= s <= EXPLORE_BAND[1] for s in DRY_RUN_SEEDS)
assert all(VIRGIN_BAND[0] <= s <= VIRGIN_BAND[1] for s in VALIDATION_SEEDS)
assert set(VALIDATION_SEEDS).isdisjoint(DRY_RUN_SEEDS)

# --- Generator numerics (frozen with the generator; C052-1, mathematician brief) --------------
TOL, REL_MARGIN = 1e-6, 1e-3       # [GEN]
COARSE = (128, 512)                # [GEN] (steps in ln V, steps in U)
FINE = (2048, 8192)                # [GEN]
COARSE_MARGIN = 0.05               # [GEN]
N_HYP = 48                         # [GEN]
AUDIT_PAIRS = 20000                # [GEN default] stage-1/2 and coarse-shot pairs re-shot FINE;
                                   # any endpoint failure or disagreement -> seed INVALID

# --- Gate (estimator-v2 tau(n), extended by the sealed procedure; step 1) ----------------------
GATE_ALPHA = 0.01
GATE_NULL_MC_SEED = 20260621
GATE_NULL_MC_REPS = 40000
GATE_TAU_N_MAX = 256               # n > 256 ABORTS the run (never extrapolate)
TAU_FIXTURE_SHA256 = "4bc4aec839257af7fed210030c0afa9041c265cacf43802bb735fb99df367a28"

# --- Criteria ----------------------------------------------------------------------------------
POOLED_SD_FLOOR = 0.5              # inherited (sealed two_means_split uses the 1+1 constant)
PERM_EXACT_MAX_N = 20
PERM_RANDOM_SAMPLES = 1_000_000
P_PERM_THRESHOLD = 1e-4            # (i) per required level
SIGNIFICANCE_MIN_RHO = 63.0        # [PI-S3] (i) required at every rho >= 63 (all but the lowest),
                                   # the literal analogue of the 1+1 "every N >= 3000"
BH_ABSTAIN_FAIL = 3                # [PI-052] >= 3 BH abstentions at a required level FAIL (i)
MAX_MINK_ESCAPES = 1               # [C052-7] (iv) as a count: flat-control non-abstentions <= 1
COVERAGE_FLOOR = 0.5               # [C052-6] deliberately weak floor; never raised or lowered

# Localisation / stability anchor (c1) [PI-052 + ASTRA]: radial order-statistic spacing of the
# minimal-element layer, evaluated at the mean box perimeter P* = pi (R_LO + R_HI) = 1.4 pi
# (box ends only, no ground truth). K_LOC unchanged from 1+1.
K_LOC = 2
PERIMETER_EVAL = math.pi * (R_LO + R_HI)


def ell_rad(rho: float) -> float:
    """Radial discreteness scale rho^(-2/3) / (1.4 pi) [ASTRA]."""
    return rho ** (-2.0 / 3.0) / PERIMETER_EVAL


def theta_loc(rho: float) -> float:
    """(ii) bound on the median bracket width over 2M: K_LOC * ell_rad / 2M."""
    return K_LOC * ell_rad(rho) / TWO_M


def theta_stab(rho: float) -> float:
    """(iii) bound on the std of the blind boundary r-location: K_LOC * ell_rad."""
    return K_LOC * ell_rad(rho)


def convergence_slack(rho: float) -> float:
    """(ii) clause F in 2+1 [PI-S3]: m(rho_{k+1}) <= m(rho_k) + ell_rad(rho_k)/2M, the 1+1 form
    m_{k+1} <= m_k + ell_k/2M with the 2+1 scale (= theta_loc/K_LOC, as in 1+1)."""
    return ell_rad(rho) / TWO_M
