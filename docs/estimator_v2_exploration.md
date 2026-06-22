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

## Finding 3 — seed-stability axis holds (prerequisite #1, 2026-06-22)

Closing (iv) is necessary but not sufficient: before estimator-v2 can be
integrated + re-sealed, its localisation must be shown **stable**, not just
correct on average. This isolates the **seed** axis — the only truly-open prior
scientific gap (density `ρ`, patch extent, resolution are separate sweeps, out of
scope here per the 2026-06-22 decision). At each **fixed** intensity the full
**gated** pipeline ran over the whole `EXPLORE_POOL` (**40 replicate seeds**,
1000000..1000039 — more than the FP test's 30), reporting the across-seed
**dispersion** of localisation. Run: `dev/explore_stability.py` (exit 0).

| intensity | n range | abstention | coverage | midpoint mean ± std (bias vs R_S) | width/2M med ± std | sep ± std |
|---:|:--:|:--:|:--:|:--:|:--:|:--:|
| 3000 | [22,41] | 0/40 (0.00) | 0.93 | 0.4983 ± 0.0212 (−0.0017) | 0.120 ± 0.052 | 15.07 ± 4.28 |
| 6000 | [37,49] | 0/40 (0.00) | 0.93 | 0.4978 ± 0.0130 (−0.0022) | 0.086 ± 0.041 | 14.21 ± 3.59 |
| 12000 | [53,71] | 0/40 (0.00) | 0.85 | 0.5018 ± 0.0109 (+0.0018) | 0.064 ± 0.033 | 14.20 ± 3.06 |

**Reading (R_S = 0.5):**
- **Centred + low-bias:** the localised boundary midpoint sits on the true
  horizon at every intensity — |bias| ≤ 0.0022, i.e. < 0.5 % of R_S.
- **Dispersion shrinks with density (the stability signal):** seed-to-seed
  midpoint std falls 0.0212 → 0.0130 → 0.0109 and width/2M std falls
  0.052 → 0.041 → 0.033 as intensity rises. The estimator converges, it does not
  scatter.
- **Gate never fires on BH:** abstention 0/40 at all intensities (n ∈ [22,71],
  far above where tau(n) could clip) — consistent with Finding 2's "no n ≤ 8".
- **Caveat — coverage/precision tension at the primary endpoint:** coverage is
  0.93 / 0.93 but drops to **0.85** at intensity 12000. The bracket tightens
  faster than the residual bias closes, so on ~6/40 seeds the (now very narrow)
  bracket just excludes R_S. This is the axis prereg-002's localisation PASS/FAIL
  (`θ_loc` / coverage) criterion must be set against, *before* any held-out run —
  not a false-positive or abstention failure, but a precision-vs-coverage trade.

This is exploration (EXPLORE_POOL only; sealed package, thresholds, and seal SHA
untouched). It **confirms feasibility** of the stability prerequisite; it does not
set any threshold.

## Reconstruction spec for `dev/explore_stability.py`

Imports the EXACT gate/observable/null from `dev/explore_fp_gated.py`
(`improvement`, `minimal_volume`, `build_tau_table`, `INTENS`, MC params) so it
cannot drift from the pre-flight. For each intensity in (3000, 6000, 12000), over
`EXPLORE_POOL` (all 40), **BH only**:
1. `emb,_,_ = generator.numpy_sprinkle(seed, intensity)`; `C =
   generator.past_matrix_fast(emb, "BH")`.
2. `Ob, mi = minimal_volume(C)`; `vals = [Ob[i] for i in mi]`; `n = len(mi)`.
3. `imp = improvement(vals)`; `thr, sep = estimator.two_means_split(vals)`;
   `br = scoring.blind_bracket(Ob, mi, thr, emb)`.
4. gate: a seed **abstains** when `imp < tau[n]` (excluded from coverage/midpoint/
   width — makes no boundary claim; `sep → 0`).
5. across the 40 seeds per intensity report: abstention rate; coverage =
   `mean(br.covers)` over claiming valid seeds; midpoint mean/std and
   `mean − R_S`; `width/2M` median/std over clean claiming seeds; sep mean/std.

## Finding 4 — patch-extent and density/resolution axes (prerequisite #1, cont. 2026-06-22)

Geometric subtlety made explicit: in this **fixed-box** generator (box =
`[t_edge, R_EDGE]`, area = `t_edge·R_EDGE`, `intensity` = expected #points),
**density `ρ` and "resolution at fixed physical area" are the SAME knob** —
raising intensity at a fixed box raises `ρ` *and* shrinks the discreteness scale
`ℓ ~ 1/√ρ`. So the density/resolution axis is the **intensity sweep at the fixed
box** (Finding 3's 3000/6000/12000, here **extended** with 1500 and 24000); the
genuinely separable axis is **patch extent**, swept by varying `t_edge` at
**matched density** (`intensity = 1000·t_edge ⇒ ρ ≡ 833.3`). `R_EDGE`/`R_CENTER`
are frozen thresholds, left untouched (so the r-window stays `[0.1, 1.3]`, R_S
inside). Same gated pipeline, 40 EXPLORE_POOL seeds, BH only. Run:
`dev/explore_axes.py` (exit 0). Gate never fires (abstention 0/40 everywhere).

**Patch-extent axis (matched `ρ = 833`):**

| t_edge | I | coverage | midpoint mean ± std | bias vs R_S | width/2M |
|---:|:--:|:--:|:--:|:--:|:--:|
| 3 | 3000 | **0.35** | 0.5262 ± 0.0146 | **+0.0262** | 0.086 |
| 6 | 6000 | 0.93 | 0.4978 ± 0.0130 | −0.0022 | 0.086 |
| 12 | 12000 | **1.00** | 0.4986 ± 0.0132 | −0.0014 | 0.088 |

**Density/resolution axis (fixed box `t_edge = 6`; 1500 & 24000 extend Finding 3):**

| I | ρ | coverage | midpoint mean ± std | bias vs R_S | width/2M |
|---:|:--:|:--:|:--:|:--:|:--:|
| 1500 | 208 | 0.97 | 0.5017 ± 0.0305 | +0.0017 | 0.159 |
| 3000 | 417 | 0.93 | 0.4983 ± 0.0212 | −0.0017 | 0.120 |
| 6000 | 833 | 0.93 | 0.4978 ± 0.0130 | −0.0022 | 0.086 |
| 12000 | 1667 | 0.85 | 0.5018 ± 0.0109 | +0.0018 | 0.064 |
| 24000 | 3333 | **0.78** | 0.5028 ± 0.0074 | +0.0028 | 0.043 |

**Reading — the two axes move coverage in OPPOSITE directions:**
- **Density → precision up, coverage DOWN.** As `ρ` rises, midpoint std
  (0.0305→0.0074) and width/2M (0.159→0.043) shrink **monotonically** (the
  estimator is *consistent* — it converges, it does not scatter), but coverage
  falls **monotonically** (0.97→0.78). The order-statistic bracket tightens
  faster than the small residual bias/scatter closes, so at high density it
  **under-covers**: it is a localisation bracket, **not a calibrated coverage
  interval**.
- **Patch extent → bias/centring.** At matched density, a **short** time-patch
  (`t_edge = 3`) is badly biased **outward** (+0.026) and coverage collapses to
  **0.35**, while a tall patch (`t_edge = 12`) is unbiased and covers 1.00 — at
  near-constant width (~0.086). Plausibly: short time-extent leaves minimal
  elements too little future to integrate, and the EF `log` term near the horizon
  then skews the volume outward. Extent sets *accuracy*; density sets *precision*.

**Bounded conclusion (versioned):**
> Estimator-v2's seed-stability holds in the sense of **consistency** — across 40
> seeds the boundary midpoint sits on R_S with bias < 0.5 % and the seed-to-seed
> dispersion *and* bracket width shrink monotonically to zero as density rises.
> But two stability caveats are now explicit and must be resolved **before**
> freezing prereg-002's localisation criterion, not after: (a) the order-statistic
> bracket is **not a calibrated coverage interval** — coverage falls monotonically
> with density (0.97→0.78 over ρ = 208→3333), so the criterion cannot be set as
> unconditional coverage ≈ 1 and must either fix a density/extent regime where
> coverage is adequate or **recalibrate/inflate** the bracket; (b) localisation is
> **not patch-extent-invariant** — a short time-patch biases the boundary outward
> and collapses coverage (0.35 at t_edge = 3, matched density), so a **minimum
> time-extent** is a precondition. The sealed endpoint (t_edge = 6, I = 12000)
> sits at coverage 0.85.

Exploration only (EXPLORE_POOL; sealed package, thresholds, seal SHA untouched;
reserved prereg-002 band never evaluated). Confirms/maps feasibility; sets no
threshold.

## Reconstruction spec for `dev/explore_axes.py`

Imports the gate/observable/null verbatim from `dev/explore_fp_gated.py` and the
across-seed metric `stability()` from `dev/explore_stability.py` (no drift). Adds
`collect_bh(intensity, t_edge)` = `collect_bh` of Finding 3 but passing `t_edge`
into `generator.numpy_sprinkle(seed, intensity, t_edge)`. Two sweeps over
`EXPLORE_POOL` (all 40), BH only:
1. **patch:** cells `(t_edge, I) ∈ {(3,3000),(6,6000),(12,12000)}` (so
   `ρ = I/(t_edge·R_EDGE) ≡ 833.3`); one tau(n) table over the realized n.
2. **density:** `t_edge = 6` fixed, `I ∈ {1500,3000,6000,12000,24000}`; its own
   tau(n) table.
Per cell report `stability()` fields: coverage, midpoint mean/std, `mean − R_S`,
width/2M median/std, abstention. `R_EDGE = 1.2`, `R_CENTER = 0.7`, `R_S = 0.5`,
`T_EDGE = 6` from `thresholds.py`.

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
