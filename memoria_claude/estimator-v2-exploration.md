---
name: estimator-v2-exploration
description: "Post-#5-FAIL dev exploration toward estimator-v2; volume observable fixes coverage (ii), false-positive (iv) axis still open"
metadata: 
  node_type: memory
  type: project
  originSessionId: ee9b4370-6291-4acd-a813-db92c8cea73f
---

After [[next-step-blind-validation]] returned **FAIL** (2026-06-21), the committee
authorised improving the ESTIMATOR in `dev/` (DEV/exploration seeds only, frozen
thresholds untouched, sealed `nachocausal/estimator.py` not modified). State of
that exploration:

**Dev scripts created (all in `dev/`, untracked):**
- `explore_observable.py` — compares order-only observables on minimal elements
  (coverage, separability, |Spearman|, width), BH only.
- `explore_full_dev.py` — runs the FULL sealed `validate` pipeline on DEV_SEEDS
  with `estimator.estimate_O` monkey-patched (pass-through) to a candidate
  observable; needs the dev-sized validity floor (`thresholds.MIN_VALID_SEEDS`
  temporarily lowered like `dry_run.py`, restored in finally) because the sealed
  floor is 18 for the 20-seed validation set.
- `explore_seeds.py` — seed hygiene: `EXPLORE_POOL = 1_000_000..1_000_039` for
  tuning (disjoint from DEV + burned VALIDATION); `RESERVED_002` band
  `[2_000_000, 2_999_999]` kept VIRGIN for prereg-002 held-out seeds (never
  evaluated during exploration). Asserts disjointness.
- `explore_fp.py` — false-positive axis bench over EXPLORE_POOL[:30], 3 intensities
  (3000/6000/12000). RAN 2026-06-21, exit 0. Result: the ABSTAINING gate works —
  **V/gated** is the only variant with `fp <= THETA_FP (0.05)` at all intensities
  (0.033 / 0.000 / 0.000) while keeping cov (0.90/0.90/0.80) and p_perm sig. Gate
  leaves cov/width identical to V/sealed (only zeroes sep when 2-means improvement
  < tau). Separation is robust: improvement BH~0.977 vs MINK~0.77 across all scales.
  CAVEAT: tau here is exploratory (computed BETWEEN the two means on seen data);
  prereg-002 needs a principled, data-INDEPENDENT tau anchor, not this one.

**Findings so far (DEV_SEEDS, 8 seeds):**
- **Coverage (ii) — strong candidate found.** Swapping the observable from future
  HEIGHT (sealed, longest future chain — an extreme/brittle statistic) to future
  VOLUME (|future(i)| = column sum of past matrix C; order-only, perm-invariant)
  lifts primary coverage **0.38 -> 0.88** (all levels 0.88-1.00) and flips the
  localisation check False->True, width not inflated (0.039).
- **Key diagnostic:** even sealed height is already `separable=1.0`, |Spearman(O,r)|
  ~1.0 — the v1 coverage failure was NOT the observable's discriminating power but
  the **`two_means_split` threshold placement**; volume's O-distribution happens to
  put the natural 2-means gap at the horizon.
- **False-positive (iv) — FIXED by the ABSTAINING gate with a PRINCIPLED tau(n)**
  (committee 2026-06-21; `dev/explore_fp_gated.py`, exit 0). Volume alone does NOT fix
  FP (orthogonal axis tied to the split/`sep` statistic, not the observable); the gate
  (sep->0 when the 2-means variance-explained "improvement" < tau, i.e. no real
  bimodality) does. **tau is now data-INDEPENDENT:** tau(n) = (1-alpha) quantile of the
  improvement statistic under an ABSTRACT UNIFORM null at matched n, alpha=0.01 (p99),
  FROZEN MC seed 20260621 / 40k reps. n = #minimal elements per cloud (order-only,
  observable w/o ground truth). Rationale: MINK improvement (~0.774) == uniform-null
  mean -> control is statistically a featureless continuum; tau=p99 of that null = "abstain
  unless bimodality beats a structureless continuum". Asymptotics: uniform 1-1/k^2=0.75,
  gauss 2/pi=0.637.
  RESULT (EXPLORE_POOL[:30], int 3000/6000/12000): V/gated(tau_n) fp=0.000/0.000/0.033
  (all <= THETA_FP 0.05), cov 0.90/0.90/0.80 (== ungated, gate doesn't touch BH), p_perm sig.
  Auditor red resolved by data: n in [16,71], NO n<=8 clouds; tau(n) in [0.89,0.91] sits
  cleanly between MINK ~0.77 and BH ~0.977. Needed the bigger EXPLORE_POOL because
  FP/significance are NOT evaluable on 8 dev seeds (p_perm>=3.9e-3 vs 1e-4; fp granularity
  1/8=0.125 vs 0.05).
- **Decided combination (by principle, NOT by best-FP selection):** form = tau(n) null-quantile
  table; alpha = 0.01; null = uniform. A 12-way grid (form{table,const} x alpha{.01,.05} x
  null{unif,gauss,disc-unif}) is allowed ONLY as a robustness annex (sensitivity map), NEVER
  as a selector (that would re-introduce reverse-engineering banned by preregistration.md:49).
- **Next (committing, needs user auth + prereg-002):** freeze alpha/null/MC-script+seed/tau(n)
  table into sealed estimator-v2, new seal SHA, held-out seeds from RESERVED_002 band.

**Discipline:** any re-validation needs a NEW pre-registration 002 (re-sealed
estimator-v2, new seal SHA, fresh held-out seeds from the reserved 002 band,
frozen thresholds unchanged). The 20 validation seeds stay burned.
