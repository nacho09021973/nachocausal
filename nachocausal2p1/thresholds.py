"""prereg-004 FROZEN thresholds and protocol constants for the 2+1D equatorial bench.

STATUS: FROZEN at C1, the unique commit introducing docs/preregistration_004.md (committee 052
§9; comités 052 and 053 signed by the PI on 2026-10-15; C1 authorised by the PI on 2026-10-15).
Any change after C1 is a new pre-registration.

Every value carries its source. Sources:
  [PI-052]  PI decisions transcribed in comité 052 §11 (2026-10-13);
  [C052-n]  comité 052 §8 synthesis item n (recommendation; signed by the PI on 2026-10-14,
            prereg-004 draft O7);
  [ASTRA]   blind theta anchor, revisiones/2026-10-13-anclaje-theta-ciego/astra.md;
  [PI-S3]   PI choices made in chat on 2026-10-13 for the step-3 port (the two 1+1 clauses
            with no 2+1 definition, comité 052 §5 item 3 / §8 item 8; signed 2026-10-14);
  [PI-O1], [PI-O3]  PI decisions of 2026-10-14 on the prereg-004 draft open items O1 and O3
            (O1 revised the same day after the O8 review, D5);
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

STATUS = "FROZEN"

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


# Thread count of the blind run [PI-O3, 2026-10-14]. The thread-determinism probe of comité 052
# step 5 was not run (the PI accepted the partial pre-flight), so the blind run is fixed to the
# only configuration with a measured parity: seed 7_000_100 on 20 numba threads
# (dev/PREREG004_STEP_5_2026-10-13.md, attempt 2).
BLIND_NUMBA_THREADS = 20


def assert_blind_threads() -> None:
    """Hard-fail the validation run unless numba runs on exactly BLIND_NUMBA_THREADS threads,
    set through the environment (NUMBA_NUM_THREADS) before numba is imported."""
    import numba

    env = os.environ.get("NUMBA_NUM_THREADS")
    got = numba.get_num_threads()
    if env != str(BLIND_NUMBA_THREADS) or got != BLIND_NUMBA_THREADS:
        raise RuntimeError(f"the blind run needs NUMBA_NUM_THREADS={BLIND_NUMBA_THREADS} "
                           f"(environment: {env!r}, numba: {got}).")


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
# C1 freezes this file, including the draw recipe. C2 records freeze_commit, draw_seed and
# seeds in docs/validation_004_seeds.json; it NEVER edits the instrument sealed at C1.
# The SHA rule is reproducible, not a guarantee of unpredictability to the author of C1.
# No manifest exists yet, and no draw is performed at import. [PI-O1; auditor 045 E1/W1]


def draw_seed_from_commit(sha: str) -> int:
    """The C2 draw seed: the first 8 hex digits of the full SHA-1 of the C1 freeze commit, as
    an integer (0 .. 2**32 - 1)."""
    if len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
        raise ValueError("draw_seed_from_commit needs the full 40-hex lowercase commit SHA.")
    return int(sha[:8], 16)
# Burned Phase-A seeds (comité 052:20, dev/2P1_PHASE_A_RESULT_2026-10-12.md): never reusable.
BURNED_PHASE_A_SEEDS = (1, 2, 3, 4, 7, 99, 12345)


def check_validation_seeds(seeds) -> None:
    """Runnable disjointness guard (comité 052:353; auditor report 043, finding 2). Empty = not
    drawn yet. Once drawn: exactly ENSEMBLE distinct seeds, all in VIRGIN_BAND, none in
    EXPLORE_BAND or among the burned Phase-A seeds. RAISES otherwise."""
    seeds = tuple(int(s) for s in seeds)
    if not seeds:
        return
    if len(seeds) != ENSEMBLE or len(set(seeds)) != ENSEMBLE:
        raise ValueError(f"VALIDATION_SEEDS must be {ENSEMBLE} distinct seeds.")
    if not all(VIRGIN_BAND[0] <= s <= VIRGIN_BAND[1] for s in seeds):
        raise ValueError("VALIDATION_SEEDS must lie in VIRGIN_BAND.")
    if any(EXPLORE_BAND[0] <= s <= EXPLORE_BAND[1] for s in seeds) \
            or set(seeds) & set(BURNED_PHASE_A_SEEDS):
        raise ValueError("VALIDATION_SEEDS overlap the exploration band or burned seeds.")


assert all(EXPLORE_BAND[0] <= s <= EXPLORE_BAND[1] for s in DRY_RUN_SEEDS)
assert not set(DRY_RUN_SEEDS) & set(BURNED_PHASE_A_SEEDS)


def validation_seeds() -> tuple:
    """Read the committed C2 manifest only after C1. Never draw seeds at import."""
    if STATUS != "FROZEN":
        return ()
    from .seed_manifest import load_manifest

    return tuple(load_manifest()["seeds"])

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
