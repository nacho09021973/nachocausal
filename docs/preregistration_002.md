# Pre-registration 002 — frozen (estimator-v2 blind run)

Status: **FROZEN pre-registration.** The git commit introducing this file
together with the held-out seeds in `nachocausal/thresholds.py` is the
**prereg-002 seal**. After this commit nothing here may be tuned on a result.

- **Seal:** `nachocausal/thresholds.py` SHA256 =
  **`6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`**
  (`make verify-seal`).
- **Instrument:** estimator-v2, sealed at `2f4c4a99…` (commit `22b7660`,
  `docs/estimator_v2_seal.md`), implementing the frozen contract
  `docs/estimator_v2_freeze.md` (`7d25c34`); decision `bb21147`.

## Held-out seeds — drawn once, blind

The 20 held-out validation seeds were drawn **once and blind** from the reserved
**virgin** band `[2_000_000, 2_999_999]` (`dev/explore_seeds.py`), which was never
evaluated during exploration (all dev work used `EXPLORE_POOL = 1_000_000..1_000_039`):

```
numpy(1.26.4).default_rng(VALIDATION_DRAW_SEED=20260622)
    .choice(arange(2_000_000, 3_000_000), size=20, replace=False)  -> sorted
```

= `2076703, 2110290, 2123378, 2126638, 2167164, 2198840, 2266288, 2282260,
2326739, 2362116, 2401239, 2472372, 2596866, 2696605, 2789254, 2833485, 2871428,
2928587, 2948610, 2983811`.

The draw is deterministic (reproducible under the pinned numpy) and auditable; it
is blind **by construction** — no seed in the band has ever been scored. The
prereg-001 set (≤ 65537) is **BURNED** and intentionally not reused. A runnable
guard in `thresholds.py` asserts all 20 lie in the reserved band and are disjoint
from `DEV_SEEDS`.

## Frozen analysis (inherited verbatim; nothing new set here)

Geometry, ensemble, intensities, primary endpoint, and the success-criteria forms
+ thresholds are inherited from `docs/preregistration_001_addendum.md`; the
estimator changes are exactly the three sealed in `docs/estimator_v2_freeze.md`
(VOLUME observable; τ(n) abstaining gate; `T_EDGE_MIN=6` domain gate). In
particular, immutable for this run:

- **Observable:** future VOLUME `O(i)=|future(i)|`; point estimate = bracket
  midpoint.
- **Gate:** abstain (`sep→0`, no boundary claimed) iff `improvement < τ(n)`;
  `τ(n)` from `fixtures/tau_table.json` (α=0.01→p99, MC seed 20260621, 40000
  reps, uniform null), n = #minimal elements.
- **Domain:** `t_edge < 6 ⇒ OUT_OF_DOMAIN` (never a physical FAIL). Production
  runs at the sealed `t_edge = 6`.
- **Localisation (ii):** median `|dr|/(2M) ≤ θ_loc = 2ℓ_λ/(2M)`, not
  IQR-inconclusive, **coverage ≥ 0.5** (a deliberately weak floor, NOT nominal
  coverage; the interval is not recalibrated).
- **Significance (i):** sign-flip `p_perm ≤ 1e-4`, significant at every N ≥ 3000.
- **Stability (iii):** boundary r-std `≤ θ_stab = 2ℓ_λ`. **FP (iv):** LOO fraction
  `≤ 0.05`. **Guard-v (v):** raises on any non-order-only causet.
- **PASS iff ALL** hold at the primary endpoint (intensity 12000); a level with
  < 18/20 valid seeds → **INCONCLUSIVE**; `t_edge < 6` → **OUT_OF_DOMAIN**.

## Binding rules

- **One-way:** the single blind `validate.run()` on these seeds is the only
  evaluation and **has not been run yet**. It is launched once, as an explicit
  step, with `guard=True`, writing `results/validation.json`.
- **Report alike:** the outcome — PASS, FAIL, INCONCLUSIVE, or OUT_OF_DOMAIN — is
  recorded and reported regardless of which it is. No post-hoc tuning, no
  re-running on fresh seeds after seeing a result, no loosening a frozen
  threshold. An unmet principled threshold is informative, never a licence to
  retune (`preregistration.md:55-57`).

## Provenance & sequence

decision `bb21147` (SHA256 `44f54495…`) → freeze #1 `7d25c34` → estimator-v2 seal
#2 `2f4c4a99` (`22b7660`) → **prereg-002 seal #3 (this)** → **single blind run #4
(pending explicit authorisation)**.
