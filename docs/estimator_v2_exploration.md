# Estimator-v2 exploration record (toward pre-registration 002)

Status: **EXPLORATION / DEV PRE-FLIGHT — NOT a confirmatory result.** This file
records dev-sandbox findings made *after* the pre-registration 001 blind
validation returned **FAIL** (`docs/preregistration_001_result.md`). It is a
committed record of exploration only: all work here used the **EXPLORE_POOL**
seeds (high band, disjoint from `DEV_SEEDS` and from the now-burned
`VALIDATION_SEEDS`); the reserved prereg-002 held-out band `[2_000_000,
2_999_999]` was **never** evaluated. The sealed `nachocausal/` package,
`thresholds.py`, and the seal SHA256 are **untouched**. Nothing here is a
threshold set on outcome — see the anchoring discipline below.

The underlying dev scripts live in `dev/` (git-ignored by design;
`CLAUDE.md`). This doc is self-contained enough to **reconstruct** them.

## What prereg-001 FAIL left open

The v1 estimator (sealed) was significant at every N (sign-flip p ≈ 1e-6) but
missed two checks at the primary N (intensity 12000):
- **(ii) localisation** — bracket width passed, but **coverage of true R_S = 0.30
  < 0.50**.
- **(iv) false-positive** — LOO fp = 0.10 > 0.05 (the v1 `two_means_split` always
  splits, so pure-Minkowski controls get a spurious `sep`).

## Finding 1 — observable swap fixes coverage (ii)

Swapping the minimal-element observable from future **HEIGHT** (sealed: longest
future chain — an extreme/brittle statistic) to future **VOLUME** (`|future(i)|`
= column sum of the past matrix C; order-only, permutation-invariant) lifts
primary coverage from ~0.30 to ~0.80–0.90 without inflating width. Diagnostic:
even sealed height is already `separable=1.0`, |Spearman(O,r)|≈1.0 — the v1
coverage failure was the **threshold placement**, not the observable's
discriminating power. Volume's O-distribution puts the natural 2-means gap at the
horizon.

## Finding 2 — an ABSTAINING gate with a principled tau(n) fixes false positives (iv)

Volume alone does **not** fix (iv): false positives are an orthogonal axis tied to
the split/`sep` statistic, not the observable. The fix is an **abstaining gate**:
set `sep -> 0` (abstain — "no horizon claimed") when the minimal-element
observable shows no real bimodality, i.e. when

```
improvement(O_min) = 1 - SSE2/SSE1   <   tau(n)
```

where `improvement` is the fraction of variance explained by the best 1-D
2-partition (== 2-means in 1D) of the minimal-element O-values, and `SSE1` is the
single-cluster SSE.

### The principled, data-INDEPENDENT anchor for tau(n) (committee, 2026-06-21)

The exploratory bench first used `tau = 0.5*(impBH + impMK)` — **illegitimate**
(reverse-engineered from seen BH/MINK data). The committee replaced it with a
data-independent anchor that mirrors `preregistration.md:52` ("a standard
bimodality test at a level fixed in advance"):

> **tau(n) = the (1 - alpha) quantile of `improvement` under an ABSTRACT UNIFORM
> null at matched n**, with **alpha = 0.01** (so tau = p99), computed by Monte
> Carlo with a **FROZEN seed** and fixed reps. `n` = number of minimal elements
> per cloud (order-only, observable WITHOUT the embedding — a count of empty
> columns of C).

Why this is legitimate and data-independent:
- The null is a pure `Uniform[0,1]` Monte Carlo — **no project seeds, no
  sprinkling, no ground truth** enter the threshold.
- It is finite-n correct: the bare asymptotic value `1 - 1/k^2 = 0.75` (uniform,
  k=2) does **not** gate MINK (~0.77); the finite-n quantile rises with smaller n
  and tracks the inflation exactly.
- Physical reading: the MINK control's `improvement` (~0.774) **equals the uniform
  null's mean** — the control is statistically a featureless continuum. `tau = p99`
  of that null says "abstain unless bimodality beats what a structureless
  continuum produces by finite-n chance". BH (~0.977) clears it at every scale.

**Decided combination (by principle, NOT by best-FP selection):** form = tau(n)
null-quantile table; alpha = 0.01; null = uniform. (Alternatives considered:
single conservative constant; off-the-shelf Hartigan dip test — weak at small n.
Gaussian null gives tau too close to MINK; uniform-discretized is an optional
refinement since O is integer.)

### Frozen Monte-Carlo parameters used in the pre-flight

- `ALPHA = 0.01` (tau = p99)
- `NULL_MC_SEED = 20260621`, `NULL_MC_REPS = 40000`
- null draws: `numpy.random.default_rng(NULL_MC_SEED).random(n)` per rep

### Reference Monte-Carlo (data-independent; uniform & gaussian nulls)

`improvement` (variance explained by best 2-means) under unimodal nulls:

| n | uniform mean / p95 / p99 | gauss mean / p95 / p99 |
|---:|---|---|
| 8 | 0.799 / 0.924 / 0.960 | 0.758 / 0.890 / 0.939 |
| 15 | 0.774 / 0.876 / 0.910 | 0.703 / 0.818 / 0.864 |
| 25 | 0.763 / 0.844 / 0.874 | 0.677 / 0.776 / 0.815 |
| 50 | 0.757 / 0.819 / 0.841 | 0.657 / 0.729 / 0.756 |
| 200 | 0.752 / 0.783 / 0.795 | 0.642 / 0.679 / 0.696 |
| ∞ (theory) | **0.750 = 1 − 1/k²** | **0.637 = 2/π** |

## Pre-flight result (EXPLORE_POOL[:30], seeds 1000000..1000029)

Run: `dev/explore_fp_gated.py` (exit 0). `n` per cloud measured in
[16, 71] — **no clouds with n ≤ 8** (resolves the "tau(n) clips BH at tiny n"
concern); tau(n) ∈ [0.89, 0.91] over the observed range, sitting cleanly between
MINK (~0.77) and BH (~0.977).

tau(n) sample: n=16 → 0.906, 17 → 0.901, 18 → 0.897, 19 → 0.894, 20 → 0.890.

| intensity | n range | impr BH / MINK | variant | coverage | fp (θ=0.05) | p_perm |
|---:|:--:|:--:|---|:--:|:--:|:--:|
| 3000 | [16,41] | 0.978 / 0.764 | V/sealed (ungated) | 0.90 | 0.100 **NO** | sig |
| | | | **V/gated(tau_n)** | 0.90 | **0.000 ok** | sig |
| 6000 | [26,49] | 0.977 / 0.778 | V/sealed (ungated) | 0.90 | 0.067 **NO** | sig |
| | | | **V/gated(tau_n)** | 0.90 | **0.000 ok** | sig |
| 12000 | [35,71] | 0.976 / 0.774 | V/sealed (ungated) | 0.80 | 0.067 **NO** | sig |
| | | | **V/gated(tau_n)** | 0.80 | **0.033 ok** | sig |

**Reading:** the gate closes (iv) at all intensities (fp 0.000 / 0.000 / 0.033, all
≤ θ_fp = 0.05) **without touching BH** — coverage and width identical to the
ungated volume estimator, significance preserved. The dev numbers only **confirm
feasibility** of the principled tau(n); they do not set it (`preregistration.md:55`).

## Reconstruction spec for `dev/explore_fp_gated.py`

For each intensity in (3000, 6000, 12000), over EXPLORE_POOL[:30]:
1. `emb, _, _ = generator.numpy_sprinkle(seed, intensity)` (one cloud, both kinds).
2. `C = generator.past_matrix_fast(emb, "BH" | "MINK")`.
3. minimal = empty-past columns; `O = C.sum(axis=0)` on minimals (volume).
4. `imp = improvement(O_min)`; `thr, sep = estimator.two_means_split(O_min)`;
   bracket via `scoring.blind_bracket(O, minimal, thr, emb)` (BH only).
5. `n = len(minimal)`; `tau[n]` from the frozen uniform-null MC (params above).
6. gated sep = `0.0 if imp < tau[n] else sep`.
7. metrics: coverage = mean of `bracket.covers` (valid); fp =
   `validate.loo_fp_fraction(sep_MINK)`; p_perm = `validate.signflip_perm_p(sep_BH
   - sep_MINK)`; thresholds `THETA_FP=0.05`, `P_PERM_THRESHOLD=1e-4`.

`improvement(values)`: sort; for each split i in 1..n-1 take
`lo.var()*lo.size + hi.var()*hi.size`, keep the min as SSE2; `SSE1 = var*n`;
return `1 - SSE2/SSE1`.

## Discipline / next steps

- A 12-way grid (form{table, const} × alpha{.01, .05} × null{uniform, gauss,
  disc-uniform}) is permitted **only as a robustness annex** (sensitivity map),
  **never as a selector** — selecting by best dev FP would re-introduce the
  reverse-engineering banned by `preregistration.md:49`.
- **Committing step (needs user authorisation + a new pre-registration 002):**
  freeze alpha, null, the MC script + seed, and the tau(n) table into a re-sealed
  estimator-v2 (new seal SHA), with **fresh held-out seeds drawn from the reserved
  002 band** `[2_000_000, 2_999_999]`. The frozen thresholds, geometry, ensemble,
  and primary endpoint (intensity 12000) do **not** move. The 20 prereg-001
  validation seeds stay burned.
