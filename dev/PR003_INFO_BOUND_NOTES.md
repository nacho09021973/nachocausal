# PR-003 R1 — information-theoretic lower bound on order-only horizon localisation (dev derivation, NOT a frozen result)

Authorised by `docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md` §9 step R1.
**This is an analytic dev derivation, not a measurement and not a frozen claim.** It develops the
Le Cam / Fano lower bound proposed in `dev/PR003_SILVER_BULLET_SYNTHESIS.md:54-59` as the candidate
**Fase #3 result**, under the exact scope the committee imposed:

> A lower bound **for THIS sealed estimator** at the **actual finite patch volume V and density ρ** —
> NOT a universal/asymptotic no-go, NOT a 3+1D claim. The `C·ℓ` scaling is derived **in-repo**, not
> attributed to EGS (the EGS "fuzzy O(ℓ)" remark is UNCONFIRMED as a *quantified* bound — comité-003
> literature verdict 1c).

Provenance: HEAD `6b3649e`, branch `main`, `make verify-seal` = `6e2c3888…`. This note runs no
sealed code and burns no seed; any numerical illustration (open item O3 below) would use EXPLORE_POOL
+ a MINK control only, never `RESERVED_002`.

## 0. What is being bounded (matched to the sealed v2 observable)

Frozen setting (`nachocausal/thresholds.py`):
- Finite 1+1D patch: `BOX_AREA = T_EDGE·R_EDGE = 6.0·1.2 = 7.2`; `r ∈ [0.1, 1.3]` spans the hidden
  `r_S = 2M = 0.5` (`thresholds.py:36-43`).
- Poisson sprinkling, density `ρ = intensity / BOX_AREA`; discreteness scale
  `ℓ = ρ^(-1/2) = (intensity/7.2)^(-1/2)` (`thresholds.py:101-103`). Same point cloud for BH and
  MINK; they differ ONLY in the causal matrix (`thresholds.py:51-54`, `SAME_CLOUD = True`).
- The estimator observes the **order alone** and computes, for each minimal element `i`, the
  future-volume `O(i) = |future(i)| = C[:,i].sum()` (`estimator.py:113-131`), then splits the sorted
  `{O(i)}` by the best 1-D 2-means partition and reports a boundary threshold `thr` and separation
  `sep` (`estimator.py:96-107`). The boundary in O-space maps to a radial location estimate `r̂`.

We bound `inf_{r̂} sup E|r̂ − r_S|` over **any** estimator that is a function of the causal order
`C` (the v2 observable is one such function), in this finite patch at density ρ.

## 1. Le Cam two-point reduction

Pose the two-point sub-problem (Tsybakov 2009, *Introduction to Nonparametric Estimation*, Thm 2.2 /
the Le Cam two-point method): place the hidden boundary at either
`r_0 = r_S − s` or `r_1 = r_S + s`, separation `2s`. Each induces a distribution on the observed
causal set, `P_0` and `P_1`. For any estimator `r̂`,

```
inf_{r̂} max_{j∈{0,1}} E_j |r̂ − r_j|  ≥  (s/2) · (1 − TV(P_0, P_1)).            (LC)
```

By Bretagnolle–Huber, `1 − TV(P_0,P_1) ≥ (1/2) exp(−KL(P_0 ‖ P_1))`, so

```
inf_{r̂} max_j E_j |r̂ − r_j|  ≥  (s/4) · exp(−KL(P_0 ‖ P_1)).                   (BH)
```

The whole question is: **how large can the separation `2s` be while keeping `KL(P_0 ‖ P_1) = O(1)`
(i.e. the two order-distributions remain statistically near-indistinguishable)?** If `KL = O(1)` at
`2s = C'·ℓ`, then (BH) gives a minimax error `≥ const · ℓ`.

## 2. Information content of a boundary shift, for the future-volume observable

Under `SAME_CLOUD`, `P_0` and `P_1` are distributions over the causal matrix `C` on the *same* N
points; they differ only on the causal relations a δ-shift of the boundary flips. The v2 estimator
does not see all of `C` — it sees only the future-volumes `{O(i)}` of minimal elements. So the
relevant information is the change in the future-volume *histogram* under the shift.

Scaling count (heuristic, marked [HEURISTIC] — see open items):
- The future-volume `O(i)` of a minimal element changes under a radial boundary shift δ **only if**
  the shift moves the singularity-truncation boundary across that element's future cone — i.e. only
  for minimal elements lying within a radial shell of width `~δ` about `r_S`. [HEURISTIC: the
  near-boundary localisation of the sensitive elements follows the EGS truncation picture,
  `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md:56`, but the cone-geometry factor is not computed here.]
- Number of minimal elements in a radial shell of width δ along the boundary of length `L_bdy`
  (timelike extent ~`T_EDGE`): `n_shell ≈ ρ · δ · L_bdy`. With `ρ = ℓ^(-2)`,
  `n_shell ≈ δ · L_bdy / ℓ²`.
- For the two order-distributions to remain near-indistinguishable we need `O(1)` elements to change
  their future-volume in a statistically resolvable way. The smallest resolvable δ is when
  `n_shell = O(1)`, i.e. `δ ≈ ℓ² / L_bdy`. With `L_bdy = O(T_EDGE)` this is `O(ℓ²)` — **too strong**
  (would give an `ℓ²` floor). The reason it is too strong: a single element flipping its O by ±1 is
  NOT resolvable, because the 2-means split sees the *histogram*, whose two clusters have spread
  `≳ √ρ` in O-units (Poisson fluctuation of `|future|`). [HEURISTIC]
- The resolvability condition is therefore not "≥1 element changes" but "the **cluster means move by
  more than the cluster noise**." The boundary threshold `thr` is the midpoint of two O-clusters
  whose means differ by `Δ_O` and whose pooled spread is floored at `POOLED_SD_FLOOR = 0.5`
  O-units ("one O-discreteness unit", `thresholds.py:78`). A boundary shift δ moves `thr` by an
  amount that maps back to δ; the shift is resolvable only when the induced mean-shift exceeds the
  pooled spread `~√(per-cluster O-variance) ≈ √(ρ·area) ∝ 1/ℓ`. Carrying the radial→O Jacobian
  through, the minimal resolvable radial shift is `δ_min ∝ ℓ`. [HEURISTIC — the Jacobian
  `dO/dr` near the boundary is the missing factor; see O2.]

Net: the *consistent* scaling, once the histogram-resolution (not pair-counting) is used, is

```
δ_min  ≈  K · ℓ ,        equivalently   Error(r̂ − r_S)  ≳  K · ℓ  =  K · ρ^(-1/2).     (★)
```

This is the same `ℓ = ρ^(-1/2)` discreteness scale, with a dimensionless constant `K = O(1)`.

## 3. In-repo anchor: the frozen thresholds already adopt (★)

The project did not wait for this derivation to adopt the `K·ℓ` floor — it is **already the basis of
the sealed thresholds**:
- `theta_loc(intensity) = K_LOC · ℓ / (2M)` with `K_LOC = 2` and the comment *"cannot localise finer
  than ~ell"* (`thresholds.py:98,106-108`).
- `theta_stab(intensity) = K_LOC · ℓ` (`thresholds.py:111-113`).
- `POOLED_SD_FLOOR = 0.5` = *"one O-discreteness unit"* (`thresholds.py:78`).

So the frozen instrument encodes exactly (★) with the empirically-chosen constant `K = K_LOC = 2`.
**This derivation supplies the information-theoretic justification for why `K_LOC·ℓ` — not some
tighter bound — is the right floor:** below `O(ℓ)` the Schwarzschild and shifted-boundary order
distributions are not separable by the histogram the v2 observable reads. The measured S3 data is
consistent: physical `d⊥` plateaus at `O(ℓ) ≈ 0.020` while `d⊥/ℓ` grows
(`dev/PR003_ITERATIVE_RESEED_V1_NOTES.md:40-42`) — i.e. the wall sits at the `ℓ` scale, not below it.

## 4. Scope and honesty (binding, per comité-003)

- **For THIS estimator, this patch, this density.** (★) bounds order-only estimators of `r_S` in the
  finite `BOX_AREA = 7.2` patch at `ρ = intensity/7.2`. It is NOT a universal no-go and NOT an
  asymptotic-horizon statement (the event horizon needs an infinite sprinkling — EGS, comité-003
  literature 1a CONFIRMED).
- **Singular-Schwarzschild-specific.** The truncation mechanism that makes O(i) carry the boundary
  fails for a regular (Hayward) black hole (EGS derived-md:463-465, comité-003 literature 1f
  CONFIRMED); (★) inherits this.
- **`C·ℓ` is derived here, not borrowed from EGS.** The EGS "fuzzy O(ℓ)" remark is qualitative
  (comité-003 literature 1c UNCONFIRMED as a quantified bound).
- **Not falsifiable by a single faster method.** A lower bound cannot be empirically refuted by one
  estimator beating it — such a result would instead signal ground-truth leakage and must be audited
  against the leakage gate (`docs/pr003_leakage_gate.md`). This is stated as a caveat, per the
  falsifier (comité-003 §5).

## 5. Open items before this could become a *frozen* Fase #3 result (committing — needs new prereg + /comite + /auditor)

- **O1 [rigour].** Replace the §2 [HEURISTIC] scaling with a clean bound: compute (or numerically
  estimate) `KL(P_0 ‖ P_1)` between the two order-distributions as a function of `2s/ℓ`, and exhibit
  the `2s` at which `KL = O(1)`. The Bretagnolle–Huber step (BH) then gives the constant.
- **O2 [Jacobian].** Make the radial→future-volume map `dO/dr` near the boundary explicit, so the
  histogram-resolution argument yields `K` rather than asserting `δ_min ∝ ℓ`.
- **O3 [numerical illustration, EXPLORE_POOL only].** A dev script estimating the affinity / KL
  between BH and box-matched MINK future-volume histograms across the frozen INTENSITIES
  `(1500, 3000, 6000, 12000)` (`thresholds.py:46`) to check `K ≈ K_LOC = 2`. Same provenance header
  discipline as the S3 scripts; MINK control mandatory; `RESERVED_002` untouched.
- **O4 [literature].** If the Le Cam framing is to cite causal-set information-theory precedent,
  source it into `biblioteca/` first (the synthesis' TDA citations are UNVERIFIED; the bound itself
  rests on Tsybakov 2009, a standard statistics text, not yet in `biblioteca/`).

Until O1–O2 are closed this is a **derivation sketch with a verified in-repo anchor (§3)**, not a
theorem. It freezes nothing.
