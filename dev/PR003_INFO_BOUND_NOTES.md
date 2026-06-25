# PR-003 R1 — operational (estimator-induced) resolution floor for order-only horizon localisation (dev derivation, NOT a frozen result)

> **Reclassified 2026-06-25 (user logical review).** The firm content of this note is an
> **operational / estimator-induced** resolution bound for the *sealed v2 channel* `C ↦ r̂`
> (`Error ∝ ℓ`): §3 anchor + §6 measurement + §7-O2 Jacobian. It is **not** a Le Cam **minimax**
> lower bound over all functions of the full causal set `C`: §7-O1 measures the KL of the estimator
> *output*, which by the data-processing inequality bounds the full-data KL from the wrong side. The
> minimax floor over `C` is a **separate, unproven target** (see §0). Phrase any C1 freeze as the
> sealed estimator's resolution, never as a universal information limit.

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

**Two distinct quantities must be kept rigorously apart (this is the crux of the O1 reclassification):**
- **(Operational — the firm result here.)** The resolution of the **sealed v2 channel** `T: C ↦ r̂`,
  i.e. `E|r̂ − r_S|` for THIS estimator, in this finite patch at density ρ. This is what §6 *measures*
  and §7-O2 *derives*: it scales `∝ ℓ`, constant `≈0.4`.
- **(Minimax over `C` — the TARGET, NOT established here.)** `inf_{r̂} sup E|r̂ − r_S|` over **any**
  estimator that is a function of the full causal order `C`. A genuine Le Cam/Fano bound on this needs
  an **upper** bound on `TV(P^C_0,P^C_1)` / `KL(P^C_0‖P^C_1)` of the **full data** `C`. This note does
  NOT supply that: the only KL we can read off (§7-O1) is of the *output* `r̂=T(C)`, and by the
  data-processing inequality `KL(P^{r̂}_0‖P^{r̂}_1) ≤ KL(P^C_0‖P^C_1)` it bounds the full-data KL from
  **below** — the wrong direction for a minimax lower bound. The minimax statement over `C` is left as
  **future work**; everything below that says "floor" or "bound" without qualifier means the
  **operational** (estimator-induced) one.

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
  through, the minimal resolvable radial shift is `δ_min ∝ ℓ`. [the Jacobian `dO/dr` near the
  boundary — the missing factor flagged here — is now derived in §7 (O2★): `dO/dr=ρ·dA_fut/dr`,
  log-enhanced near `r_S`, giving `δr ∝ ℓ` with constant `≈0.4` pinned by §6.]

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

- **For THIS estimator, this patch, this density.** (★) bounds the resolution of the **sealed v2
  estimator** `C ↦ r̂` of `r_S` in the finite `BOX_AREA = 7.2` patch at `ρ = intensity/7.2`. It is NOT
  a minimax bound over all functions of `C` (§0), NOT a universal no-go, and NOT an asymptotic-horizon
  statement (the event horizon needs an infinite sprinkling — EGS, comité-003 literature 1a CONFIRMED).
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

- **O1 [rigour]. RECLASSIFIED as an OPERATIONAL (estimator-induced) bound — see §7.** `KL` of the
  **estimator output** `r̂=T(C)` `≈ 3.1·(2s/ℓ)²` reaches `O(1)` at `2s ≈ 0.57·ℓ` (anchored on the
  §6-measured `σ(r̂)≈0.40ℓ`), matching the measured `TVg=0.5` crossing; Bretagnolle–Huber turns this
  into the **sealed channel's** resolution floor `∝ ℓ`. This is a bound on the channel `C ↦ r̂`, **NOT**
  a Le Cam minimax bound over all functions of `C`: by data-processing the output KL bounds the
  full-data KL from *below*, the wrong direction. The observation that full-data KL `∝ n_min` reaches
  `O(1)` even *sooner* makes the full hypotheses *more* distinguishable and therefore **weakens** (not
  supports) any universal-impossibility reading — so the minimax floor over `C` stays OPEN.
- **O2 [Jacobian]. CLOSED as a sketch — see §7.** `dO/dr = ρ·dA_fut/dr` (log-enhanced near `r_S` from
  the tortoise term `func`); with `σ_O ∝ 1/ℓ` and `dO/dr ∝ 1/ℓ²` the `ρ` cancels to give `δr ∝ ℓ`
  (O2★), constant `1/(dA_fut/dr|_{r_S}) ≈ 0.4` pinned by §6.
- **O3 [numerical illustration, EXPLORE_POOL only].** **ILLUSTRATED this session — see §6.**
  `dev/measure_info_bound_o3.py` (GPU build via `dev/backend.py`; log `dev/info_bound_o3.log`),
  24 EXPLORE_POOL seeds × the frozen INTENSITIES `(1500, 3000, 6000, 12000)` (`thresholds.py:46`),
  MINK control included; `RESERVED_002` untouched; seal `6e2c3888…` asserted before+after.
- **O4 [literature].** If the Le Cam framing is to cite causal-set information-theory precedent,
  source it into `biblioteca/` first (the synthesis' TDA citations are UNVERIFIED; the bound itself
  rests on Tsybakov 2009, a standard statistics text, not yet in `biblioteca/`).

O2 is closed as a **derivation sketch (§7)**; O1 is **reclassified** (§7) as an *operational*
(estimator-induced) bound on the channel `C ↦ r̂`, NOT a minimax bound over `C`. With the in-repo
anchor (§3), the numerical illustration (§6) and the analytic Jacobian (§7), this is a **grounded
operational resolution bound for the sealed estimator**, still not a theorem and explicitly NOT a
universal information floor over the full causal set (§0). It freezes nothing; a *frozen* Fase #3
result needs the committing path (new prereg + `/comite` + `/auditor`) and O4, and must be phrased as
the sealed estimator's resolution — the minimax bound over `C` is separate, future work.

## 6. O3 — numerical illustration of the scaling (dev, NOT a frozen result)

Авал: comité-003 §9 R1 / O3. Script `dev/measure_info_bound_o3.py`, run on the local NVIDIA RTX
5060 via `dev/backend.py` (CuPy); 24 EXPLORE_POOL seeds × INTENSITIES `(1500,3000,6000,12000)`;
MINK same-cloud control; seal `6e2c3888…` confirmed before+after; no `RESERVED_002` seed touched;
`git status` shows no `M nachocausal/`. Log: `dev/info_bound_o3.log` (git-ignored). HEAD `5081f4e`,
branch `main`, numpy 2.4.6 in the GPU venv (dev only — the seal is a file-SHA, not numpy-version).

**Method (two-point Le Cam, matched to the sealed v2 observable).** Place the TRUE boundary at
`r_S − s` or `r_S + s` on the *same* Poisson cloud (only the BH causal matrix `r_S` changes —
exactly `SAME_CLOUD`), run the sealed v2 pipeline (future-volume `O` → `two_means_split` →
`blind_bracket` midpoint = `r̂`), and measure how separable the two order-induced `r̂`-distributions
are as a function of the half-separation `s` in units of `ℓ`. `r` enters only as a generative
parameter of the two known synthetic families; the estimator never sees it. The genuine
per-estimator quantity is **view A** (TV between the `r̂` ensembles); views B (per-element `O` pmf
divergence) and C (BH-vs-MINK affinity) are data-processed statistics reported only for context.

**GPU honesty.** `--gpu-check`: the GPU `np.log` ulp-flips near the horizon (`backend.py` docstring)
do **not** move any minimal element's future-volume — GPU vs CPU `O`-multiset `maxdiff = 0,
mismatches = 0` at both `N≈1490` and `N≈11970`. For *this* observable at these densities the GPU
build is bit-identical to the sealed CPU instrument.

**Result — the localisation floor scales as `ℓ = ρ^(-1/2)` (★ confirmed at the order level):**

| intensity | ℓ | scatter `sd(r̂)/ℓ` at `r_S` | resolvable `2s/ℓ` (TVg=0.5) |
|---|---|---|---|
| 1500  | 0.0693 | 0.34 | 0.60 |
| 3000  | 0.0490 | 0.45 | 0.47 |
| 6000  | 0.0346 | 0.39 | 0.62 |
| 12000 | 0.0245 | 0.40 | 0.71 |

- The estimator's own `r̂` scatter is **`≈ 0.4·ℓ`, density-invariant** across a ×8 density range; the
  bias is `≤ 0.11·ℓ` with no systematic drift. The two boundaries become order-distinguishable only
  when separated by `≈ 0.5–0.7·ℓ`. The whole `TVg(r̂)` curve **collapses onto a single function of
  `s/ℓ`** across the four densities (e.g. at `s/ℓ=1.0`: TVg = 0.99, 0.99, 0.99, 0.95) — the collapse
  IS the demonstration that `ℓ` is the resolution scale, i.e. `Error ∝ ℓ = ρ^(-1/2)`, the claim (★).
- **`K_LOC = 2` is conservative, not tight.** The measured order-only floor constant is `O(1)` but
  `< 2` (scatter `~0.4`, resolvable separation `~0.6`), so the frozen `theta_stab = K_LOC·ℓ` is a
  *safe* floor, with margin — exactly the honest direction (the instrument does not under-claim its
  own resolution). This supplies the §3 anchor with a measured, density-invariant constant.
- **View C:** BH-vs-MINK Hellinger affinity `0.30–0.46` (TV `0.69–0.79`) — the *presence* of the
  horizon is clearly detectable order-only; it is the fine *localisation* of `r_S` that floors at `ℓ`.

**Honesty / what this is NOT.** The two-point Le Cam *functional value* itself
(`max_s (s/2)(1−TV) ≈ 0.07–0.08·ℓ`) is a **loose** lower bound, as a single two-point reduction
must be; the robust, reportable content is the **ℓ-collapse / scaling**, not that precise constant.
This is an illustration of a lower bound **for THIS sealed estimator at the actual finite V, ρ** —
NOT a universal/asymptotic no-go, NOT a theorem. §7 closes the analytic legs O1/O2 as derivation
sketches grounded in this measurement; this section closes O3's *numerical* leg; nothing is frozen.

## 7. O1–O2 closure (analytic derivation sketch, grounded in the §6 measurement)

Both items are closed as **derivation sketches** that replace the §2 `[HEURISTIC]` assertions with a
reasoned chain anchored on the robust §6 number `σ(r̂) ≈ 0.40·ℓ` (density-invariant). They are NOT
theorems; they freeze nothing. They do remove the two "missing factor" gaps the §2 sketch flagged.

### O2 — the radial→future-volume Jacobian `dO/dr` near `r_S`  (the missing factor)

For a minimal element near the bottom edge at radius `r`, the future-volume is
`O(r) = ρ · A_fut(r)`, where `A_fut(r)` is the 1+1D spacetime area of its causal future inside the
box. The future cone is bounded by the two null rays read off the sealed BH relations
(`nachocausal/generator.py:104,117-127`):

- **ingoing** ray `r(t) = r − t` (slope −1; smooth across `r_S` in EF — the `t_in = r_j − r_i`
  branch);
- **outgoing** ray `func(r') = func(r) + t`, with `func(r) = r + 2r_S·log(|r−r_S|/r_S)` the tortoise
  term (the `t_out = func_i − func_j` branch).

Because `d func/dr = 1 + 2r_S/(r−r_S)` for `r>r_S` and `= 1 − 2r_S/(r_S−r)` for `r<r_S`, the outgoing
ray opens **outward** for exterior seeds (`r>r_S`) and folds **inward** for interior seeds (`r<r_S`,
where `func` decreases steeply): the interior future is *truncated* toward the singularity. This is
exactly the EGS truncation that makes `O` carry the boundary (`PR003_ITERATIVE_RESEED_V1_NOTES.md:56`).
The Jacobian is

```
dO/dr = ρ · dA_fut/dr ,    and near r_S   dA_fut/dr  is LOG-ENHANCED  (∝ 1 + 2r_S/|r−r_S|),
```

i.e. `O` is *most* sensitive to `r` right at the boundary — sharpening localisation there. The
localisation resolution is set by O-noise / slope. With Poisson cluster noise `σ_O ≈ √O = √(ρ·A_fut)`
and slope `dO/dr = ρ·dA_fut/dr`:

```
δr  ≈  σ_O / (dO/dr)  =  √(ρ·A_fut) / (ρ·dA_fut/dr)  =  ℓ · √(A_fut) / (dA_fut/dr) .       (O2★)
```

The factor `√(A_fut)/(dA_fut/dr)` is **dimensionless and O(1)** (in 1+1D, `A_fut` is a length², so
`√(A_fut)` and `dA_fut/dr` are both lengths). All `ρ`-dependence cancels — `σ_O ∝ 1/ℓ` over
`dO/dr ∝ 1/ℓ²` — leaving **`δr ∝ ℓ`**, which is what §2 asserted and O2 now derives. The constant
`√(A_fut)/(dA_fut/dr)|_{r_S}` is *small* because `dA_fut/dr` is log-enhanced at `r_S` (sharp boundary
→ `δr < ℓ`). The §6 measurement pins it: `σ(r̂)/ℓ ≈ 0.40` is the empirical value of this geometric
factor. (`POOLED_SD_FLOOR = 0.5` O-units, `thresholds.py:78`, floors `σ_O` so this stays finite when
a cluster is a single element.)

### O1 — operational KL of the SEALED channel `C ↦ r̂` (estimator-induced; NOT a minimax bound over `C`)

> **Scope flag (the data-processing direction).** What follows bounds the resolution of the *output*
> `r̂ = T(C)` of the sealed v2 estimator. It is an **operational / estimator-induced** bound, not a
> Le Cam minimax bound over all functions of the full causal set `C`. The latter would require an
> **upper** bound on `KL(P^C_0‖P^C_1)`; the KL computed below is on the output and, by
> `KL(P^{r̂}_0‖P^{r̂}_1) ≤ KL(P^C_0‖P^C_1)`, only bounds the full-data KL from the wrong side. The
> minimax floor over `C` is left OPEN (see §0).

The estimator's output `r̂` (=midpoint) has, at true boundary `r_S±s`, an approximately Gaussian law
with the measured spread `σ ≈ 0.40·ℓ` and means separated by `Δμ ≈ 2s` (§6: `r̂` tracks the boundary,
bias `≤ 0.11·ℓ`). [These are working approximations — Gaussianity, equal variance across the two
hypotheses, `Δμ = 2s`, and negligible bias/abstention — adequate as a *local diagnostic*, NOT yet a
theorem.] Under them the two-point KL of the **estimator's own output** is

```
KL(P^{r̂}_0‖P^{r̂}_1)  ≈  (Δμ)² / (2σ²)  =  (2s)² / (2·(0.40 ℓ)²)  ≈  3.1 · (2s/ℓ)² .
```

So `KL = 1` at `2s ≈ 0.57·ℓ` — matching the independently-read resolvable separation
`2s/ℓ ≈ 0.6` (§6, `TVg=0.5`). Bretagnolle–Huber `1−TV ≥ ½·exp(−KL)` then turns this into the
**sealed channel's** resolution floor `Error ≳ (s/4)·exp(−KL) = O(0.03–0.08·ℓ)` at the maximising `s`
— the same order as §6's `max_s (s/2)(1−TV)`. **The sealed estimator's `r̂`-distributions become
statistically distinguishable only at the `ℓ` scale (`2s ≈ 0.6 ℓ`), so the SEALED estimator resolves
`r_S` no finer than `O(ℓ)` — claim (★), operational, with constant `O(1) < K_LOC=2`.** This does NOT
license "no estimator of `C` can do better."

Honest caveat (the data-processing direction, per comité-003 §8 falsifier): the KL above is of the
estimator's *output*. The full-data sufficient statistic (the whole `{O(i)}` multiset of `n_min`
minimal elements) has `KL_full ≈ n_min · KL_per-element`, which reaches `O(1)` at an even *smaller*
`2s` (the per-element pmf KL `KLo`, §6, is `~0.1`, and `n_min ≈ 19→62` grows with density). Critically,
a *larger* full-data KL means the full hypotheses are **more** distinguishable — so it **weakens** any
"universal `O(ℓ)` impossibility" reading rather than supporting it, and it says nothing about whether a
*better* function of `C` could beat `0.4 ℓ`. The only thing it confirms is internal consistency of the
**operational** floor for THIS estimator (its output cannot resolve below what its sufficient statistic
carries). The minimax bound over `C` remains the separate, unproven target of §0.

### Status after O1–O2

The **operational** resolution of the sealed channel `C ↦ r̂` is now established on three legs: the
in-repo anchor (§3), the numerical `ℓ`-collapse (§6), and the analytic Jacobian `δr ∝ ℓ` (O2★, §7)
with constant `≈0.4` fixed by §6; the distinguishability scale `2s ≈ 0.6 ℓ` is **derived** from the
measured `σ(r̂)` and matches the `TVg=0.5` crossing (O1). The two §2 `[HEURISTIC]` gaps (the
cone-geometry factor and the `dO/dr` Jacobian) are closed at sketch level. **What this is and is
NOT:** it IS a grounded operational/estimator-induced resolution bound for THIS sealed estimator at
finite V, ρ; it is NOT a theorem, and it is NOT a Le Cam **minimax** lower bound over all functions
of the full causal set `C` — O1 measures the output channel, the wrong side of the data-processing
inequality for a universal floor, so the minimax statement over `C` stays explicitly OPEN (§0).
A *frozen* Fase #3 result would (a) be phrased as the **sealed estimator's resolution** (operational),
not a universal information limit, and (b) need the committing path (new prereg + `/comite` +
`/auditor`); a future, *separate* minimax bound over `C` would need an upper bound on the full-data
`KL(P^C_0‖P^C_1)`. O4 (sourcing Tsybakov 2009 / causal-set info-theory precedent into `biblioteca/`)
is for the citations, and by itself does not close this inequality-direction gap.
