# SQUARE_BOX_2P4 Truncated-Futures Boundary-Localization Draft

STATUS: CONTRACT_FROZEN
FROZEN_BY: human review
FROZEN_DATE: 2026-07-20
DATE: 2026-07-19

## 0. Scope

This is a new localization-contract draft for a different localizer. It is not a retune of the
frozen largest-gap localizer in `docs/preregistration_square_box_boundary_localization.md`.

The frozen largest-gap localizer remains a separate object. Its development diagnostic showed
support was fine but the selected band landed far from `R_S`; no confirmatory localization result
was emitted.

The previous R-VAR closure remains intact:

```text
CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]
```

The sealed dispersion result remains separately bounded:

```text
BH_MINK_DISPERSION_DIFFERENCE_DETECTED
```

This draft asks whether the boundary can be localized by explicitly targeting the low-future
region among minimal elements: low longest future-chain length `L(i)` and low future cardinality
`V(i)`.

## 1. Scientific question

In `SQUARE_BOX_2P4`, can an order-only localizer that targets the onset of future truncation among
minimal elements produce a localized candidate boundary band near the hidden Schwarzschild radius
`r=R_S`?

Target:

```text
TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION
```

Claim boundary:

- candidate boundary band only;
- no global event-horizon claim;
- no metric reconstruction;
- no 3+1D transfer;
- no repair, reopening, or supersession of R-VAR;
- no silent modification of the frozen largest-gap contract.

### 1.1 Falsifiable physical hypothesis

Pre-registered wording (does not presuppose the observable's success):

> Los minimales causalmente próximos a la región objetivo presentan futuros conjuntamente
> reducidos en profundidad (L) y volumen (V). Se evaluará si esta señal bivariada enriquece la
> localización de la región objetivo respecto a los componentes aislados y si dicho
> enriquecimiento persiste después de controlar la proximidad a la frontera del dominio.

Explicit boundaries on interpretation, fixed before any evaluation:

- `low L` and `low V`, separately or combined, can detect **generic censorship** (any mechanism
  that truncates a minimal element's future within a finite box), not specifically a horizon.
  A finite patch boundary is itself one source of generic censorship (§9.1, §11).
- A pass of `T(i)`'s primary success criterion (§10) does not by itself imply horizon detection.
  It only shows that the combined low-`L`/low-`V` band is closer to `r=R_S` than the same-cloud
  Minkowski control allows by chance, under the frozen thresholds.
- Any positive interpretation must distinguish, and this draft's controls (§9.1, §11) are built to
  help distinguish, at least four candidate explanations for an apparent localization signal:
  (a) genuine horizon-adjacent censorship, (b) domain-boundary censorship, (c) generic low causal
  height/volume unrelated to either boundary, and (d) discreteness fluctuation at the evaluated
  intensities.

## 2. Geometry

Geometry is fixed to the same square patch used by the sealed dispersion result:

```text
PATCH_GEOMETRY = SQUARE_BOX_2P4
T_EDGE = 2.4
R_EDGE = 2.4
R_CENTER = 1.3
r ∈ [0.1, 2.5]
R_S = 0.5
BOX_AREA = 5.76
ASPECT_RATIO = 1.0
```

This geometry is not re-selected after localization inspection.

## 3. Seed discipline

All prior observed seeds are excluded from confirmatory evaluation.

Excluded prior ranges / sets:

```text
DEV_SEEDS = (20240617, 13, 101, 7, 42, 99, 2718, 31415)
EXPLORE_POOL = 1_000_000 .. 1_000_039
PR010 development seeds = 1_101_000 .. 1_101_023
prereg-002 validation band = 2_000_000 .. 2_999_999
OP-2.1 synthetic band = 3_000_000 .. 3_999_999
new-geometry dispersion dev seeds = 4_100_000 .. 4_100_011
new-geometry dispersion eval seeds = 4_200_000 .. 4_200_023
largest-gap localization dev seeds = 4_300_000 .. 4_300_015
largest-gap localization proposed eval seeds = 4_400_000 .. 4_400_031
```

The largest-gap development seeds `4_300_000 .. 4_300_015` may be cited only as the diagnostic
motivation for this new contract. They must not be used for confirmatory evaluation.

Proposed development seeds for this truncated-futures localizer:

```text
TRUNC_FUT_DEV_SEEDS = 4_500_000 .. 4_500_015
```

Proposed confirmatory evaluation seeds:

```text
TRUNC_FUT_EVAL_SEEDS = 4_600_000 .. 4_600_031
```

No seed substitution after inspection.

## 4. Observation channel

For each seed and intensity:

1. Draw one coordinate-uniform Poisson point cloud in `SQUARE_BOX_2P4`.
2. Build two causal matrices on the same point cloud:
   - `BH`: 1+1D Schwarzschild EF causal relation with `R_S=0.5`;
   - `MINK`: 1+1D flat Minkowski causal relation.
3. The localizer receives only the finite partial order.
4. Coordinates and `R_S` are used only after selection, for scoring.

Same-cloud pairing is mandatory.

## 5. Intensities

Proposed evaluation intensities:

```text
TRUNC_FUT_INTENSITIES = (1200.0, 2400.0, 4800.0, 9600.0)
TRUNC_FUT_PRIMARY_INTENSITY = 9600.0
```

The discreteness scale is:

```text
ell = (intensity / 5.76)^(-1/2)
```

## 6. Order-only observables

For a finite poset `C`, let:

```text
Min(C) = {i : no j precedes i}
```

By construction `C` is a strict partial order (irreflexive and transitive: the causal relation
computed directly from the coordinate-based causality test, `nachocausal/generator.py:88-129`, is
a geometric precedence test that is transitive on its own terms, without a separate
transitive-closure step). Consequently `Min(C)` is an antichain: no two minimal elements are
related, because if `j` preceded `i` then `i` would not be minimal. This fact is used in §9.1.

### 6.1 Future volume

```text
J⁺(i) = {j : i precedes j}     (strict causal future of i; excludes i itself)
V(i) = |J⁺(i)|
```

In the past-matrix convention already used by this project (`C[a,b]` true iff `b` precedes `a`,
`nachocausal/generator.py:94`), `J⁺(i)` is the set of `j` with `C[j,i]` true, i.e. column `i`.

### 6.2 Future length — link (cover-relation) convention

```text
L(i) = max_{j ∈ J⁺(i)} d_link(i,j)
```

where `d_link(i,j)` is the length, counted in covering-relation steps ("links"), of the longest
directed chain of cover relations from `i` to `j`. Equivalently, using the covering relation
`i ⋖ j` ("`j` covers `i`": `i` precedes `j` and no `k` satisfies `i` precedes `k` precedes `j`,
`nachocausal/c1_selector.py:48-61`, `cover_relations`):

```text
L(i) = 0                              if J⁺(i) = ∅   (i is maximal)
L(i) = 1 + max_{j : i ⋖ j} L(j)        otherwise
```

**Read-only verification against the existing repository convention.** `dev/
run_new_geometry_future_observables.py:174-187` (`longest_chain_lengths`) already computes `L` in
this exact link convention: `H[i] = 0` when `i` has an empty future, `H[i] = 1 + H[fut_mask].max()`
otherwise, recursed over the full future set `C[:, i]` rather than only the cover successors. This
is the same value as the cover-only recursion above: in a finite strict partial order, the
memoized longest-path recursion over the *full* transitive relation is realized through a chain of
covering successors (any successor `j` reachable through an intermediate `k`, `i ⋖ k ⋖ ... ⋖ j`,
contributes `H[j] < H[k] < ...`, so the `max` is always attained at, or dominated by, a covering
successor). No conversion is needed for that script's convention; this draft's `L(i)` is defined
identically to it.

**Conversion bridge (documentation-only, not applied to any code path here).** If some other
component of the repository or a future implementation instead reports future length as an
*element count* along a chain (base case `1` for a maximal element, since the chain then consists
of the single element itself), the deterministic conversion for non-empty futures is:

```text
L_elements = L_links + 1
```

No code is changed to adapt one convention to the other. Unless explicitly relabeled, every `L(i)`
in this document refers to `L_links`, i.e. the definition above.

Both `L(i)` and `V(i)` are order-only: neither uses coordinates, `R_S`, or a kind label.

## 7. Truncated-futures localizer

The output is a subset of minimal elements:

```text
H_hat_trunc(C) ⊆ Min(C)
```

The rule is deterministic and order-only.

### 7.1 Low-future score

Let `m = |Min(C)|` (the abstention gate in §8 guarantees `m >= 8` before this stage is reached, so
the `m = 1` case below is a totality convention, not a case that occurs on an evaluated seed).

For `X ∈ {L, V}`, let `r_X(i)` be the 1-indexed **ascending** average rank of `X(i)` among the `m`
values `{X(j) : j ∈ Min(C)}`: sort the `m` values ascending, assign integer ranks `1..m`, and for
every group of tied values replace their ranks by the arithmetic mean of the ranks the group
occupies (standard fractional / average ranking, i.e. midrank). A low `X(i)` value receives a low
`r_X(i)`.

Normalize to `[0,1]`:

```text
rank_X(i) = (r_X(i) - 1) / (m - 1)     for m > 1
rank_X(i) = 0.5                         for m = 1   (degenerate placeholder; never triggers under §8)
```

`rank_X(i) = 0` marks the (possibly tied) lowest `X` value in the realization; `rank_X(i) = 1`
marks the (possibly tied) highest.

Define the low-future score:

```text
T(i) = 1.0 - 0.5 * rank_L(i) - 0.5 * rank_V(i)
```

High `T(i)` means both `L(i)` and `V(i)` are low relative to other minimals.

`rank_L`, `rank_V`, and `T` use only within-realization comparisons among `Min(C)`. No cross-seed
information and no target-region label enter any of these formulas, consistent with §4 and the
founding rule that the hidden embedding only scores.

Final ties in `T(i)` are resolved by the deterministic tie-expansion-or-abstain rule already fixed
in §7.2 below (tied `T` values straddling the selection boundary are either all included, up to
`k_cap`, or the seed abstains under `TIE_OVER_CAP_ABSTAIN`). No random tie-break and no
target-region label are used anywhere in selection.

### 7.2 Selection rule

Sort all minimals by descending `T(i)`.

Let:

```text
k_floor = 2
k_cap = max(2, floor(0.20 * |Min(C)|))
```

Select the top truncated-futures band:

```text
H_hat_trunc(C) = {i ∈ Min(C) : T(i) is among the top k_floor elements}
```

Tie expansion rule:

If the `k_floor` boundary cuts through a tied `T` value, include all minimals with that tied
value, but never exceed `k_cap`. If including the full tied level would exceed `k_cap`, abstain:

```text
TIE_OVER_CAP_ABSTAIN
```

No coordinate, `r`, `R_S`, kind label, or seed-specific outcome enters the selection.

## 8. Abstention rules

A seed abstains before scoring if:

```text
|Min(C)| < 8
fewer than 3 distinct T values
non-finite summary
|H_hat_trunc(C)| = 0
|H_hat_trunc(C)| > k_cap
TIE_OVER_CAP_ABSTAIN
```

Terminals distinguish support failure from scientific failure.

## 9. Scoring

Scoring uses hidden coordinates only after `H_hat_trunc(C)` has been selected.

For each selected element:

```text
d_perp(i) = |r_i - R_S|
d_ell(i) = d_perp(i) / ell
```

Per seed:

```text
loc_med(seed) = median_{i ∈ H_hat_trunc(C)} d_ell(i)
loc_q75(seed) = q75_{i ∈ H_hat_trunc(C)} d_ell(i)
band_size(seed) = |H_hat_trunc(C)|
```

`loc_med(seed)` is a distance: `d_ell(i) = |r_i - R_S| / ell` is the radial offset from `R_S`,
itself a length in the same `(t, r)` coordinate units fixed in §2, measured in units of the
discreteness scale `ell` (§5), which is also a length (`ell = (intensity/BOX_AREA)^(-1/2)`).
`loc_med` is therefore dimensionless *as a ratio*, but that ratio's physical content is "radial
distance to `R_S`, expressed in discreteness units" — it is not an arbitrary unitless score. This
is used in §12.

**Median convention (applies throughout this document).** Every median in this document — `loc_med`
and `loc_q75` above, `edge_rank_med` (§9.1), and `median_s(Delta_{c,s})` (§12) — over a finite
multiset of even cardinality is the arithmetic mean of the two middle order statistics (the
standard definition); over odd cardinality it is the single middle order statistic. No alternative
convention (e.g. lower/upper median) is used anywhere in this contract.

### 9.1 Edge control (domain-boundary diagnostic)

This is a scoring-time-only covariate, exactly parallel in role to `d_perp`/`d_ell` above: it is
computed only **after** `H_hat_trunc(C)` (or a baseline control set, §11) has been selected, using
the same hidden coordinates that already enter scoring. It never enters selection and never enters
`L(i)`, `V(i)`, `rank_L`, `rank_V`, or `T(i)`. This keeps it inside the observation-channel
discipline already fixed in §4 ("coordinates ... are used only after selection, for scoring") and
the founding rule (`CLAUDE.md`) that the hidden embedding only scores and never guides the
observable.

**What the antichain fact does and does not establish.** §6 shows `Min(C)` is an antichain: the
suborder *induced among minimal elements* carries no internal relational information (no
`i, j ∈ Min(C)` are related to each other). That rules out proxies built from relations *between*
minimal elements. It does **not** rule out order-only proxies built from each minimal's profile
against the *rest* of the causal set — candidates not evaluated in this draft include the detailed
(non-scalarized) structure of `J⁺(i)`, pairwise future overlap `J⁺(i) ∩ J⁺(j)` for `i, j ∈ Min(C)`,
total degree, shadow/interval structure, or future-branching statistics at fixed rank. No such
proxy has been identified or validated in this repository as computable, independent of `L` and
`V`, and non-circular. **This is a current gap in this draft's design, not a proven
impossibility.** Verified read-only: neither `nachocausal/generator.py` nor
`nachocausal/c1_selector.py` currently implements any of these candidates, so none is adopted here
— but their absence from the repository is not evidence that they cannot exist. A future revision
should either validate one of them or rule it out individually; this draft does neither, and does
not claim to.

**What is adopted instead, and why it stays out of the order-only channel.** Pending that open
question, this draft adopts a coordinate-based diagnostic, defined below, used *exclusively* as a
post-selection scoring-time covariate — never as a selector. This is licensed by the same channel
already used for `d_perp`/`d_ell`: §4/§9 already permit hidden coordinates and box geometry
(`T_EDGE`, `R_EDGE`, `R_CENTER`, §2; produced by `nachocausal/generator.py:37-50`,
`numpy_sprinkle`) to enter *after* a selector's output is fixed. Using that same license for a
second post-selection projection of the coordinates is not a new capability granted to the
pipeline. It is explicitly **not** proposed as a replacement order-only selector, and must not be
read as one anywhere in this document (see §11.4).

**Adopted definition.** Let:

```text
T_LOW = 0.0,                     T_HIGH = T_EDGE
R_LOW = R_CENTER - R_EDGE / 2,   R_HIGH = R_CENTER + R_EDGE / 2
```

(numerically, under §2: `T_LOW=0.0, T_HIGH=2.4, R_LOW=0.1, R_HIGH=2.5`).

Only the three walls that can truncate a future cone **within** the box are used: the late-time
wall `t=T_HIGH` and both radial walls `r=R_LOW`, `r=R_HIGH`. The early-time wall `t=T_LOW` is
excluded on principle, not by omission: proximity to `t=T_LOW` *maximizes*, rather than truncates,
the room available for a future inside the box, so including it would run backwards against the
mechanism this control is meant to catch.

```text
d_edge(i) = min(T_HIGH - t_i, r_i - R_LOW, R_HIGH - r_i)
d_edge_ell(i) = d_edge(i) / ell
```

(`ell` as defined in §5.) `d_edge_ell(i) -> 0` means `i` sits near a future-truncating wall of the
box; a larger value means `i` is more interior.

Per seed, for a given selected set `S` (either `H_hat_trunc(C)` or a baseline control set from
§11):

```text
edge_med(seed, S) = median_{i ∈ S} d_edge_ell(i)
```

**Direction / use — concrete diagnostic procedure.** `edge_med` and everything derived from it below
are reported; none of it is thresholded into the selection rule and none of it is used to tune
`k_floor`, `k_cap`, or any rank formula. The concrete procedure that operationalizes abandonment
criterion 2 (§15, "Confusión de frontera") is fixed here, not left to be improvised at evaluation
time:

1. **Within-realization edge rank.** For each seed, apply the identical fractional/average-rank
   formula already defined in §7.1 to `d_edge_ell` over `Min(C)`:

   ```text
   edge_rank(i) = same midrank/normalization construction as rank_X in §7.1, applied to
                  {d_edge_ell(j) : j ∈ Min(C)} in place of {X(j) : j ∈ Min(C)}
   ```

   so `edge_rank(i) ∈ [0,1]`, low meaning `i` is near a truncating wall *relative to the other
   minimals of that same realization*, high meaning interior. Reusing §7.1's construction avoids
   introducing a second, unrelated normalization convention.

2. **Selected-set edge rank.** For a selected set `S` (any of `H_hat_trunc(C)`, `H_hat_L(C)`,
   `H_hat_V(C)`, `H_hat_rand(C)`):

   ```text
   edge_rank_med(seed, S) = median_{i ∈ S} edge_rank(i)
   ```

   `0.5` is the realization-neutral reference: it is the value any selection *unrelated* to edge
   proximity would hit in expectation, purely from the `[0,1]` normalization already fixed in
   §7.1 — not a new empirically tuned constant.

3. **Boundary-confound contrast.** Over the same paired-valid BH seeds used in §12:

   ```text
   Delta_edge(seed) = 0.5 - edge_rank_med(seed, H_hat_trunc)
   ```

   `Delta_edge(seed) > 0` means `H_hat_trunc(C)` selected elements systematically nearer the box
   walls than a generic subset of that realization's minimals would be. Test the sign of
   `Delta_edge` with the same one-sided exact sign test machinery adopted in §12 (explicit
   conditional null, tie accounting, `MIN_N(alpha, d)` formula), but as its **own separate
   diagnostic family, not folded into the primary family's `d = 2`** — PI-adjudicated: this is a
   single test (`d_edge = 1`), with its own significance level:

   ```text
   alpha_edge = 0.01     (d_edge = 1, no Bonferroni split — a single test)
   MIN_N_edge = max( ceil(0.5 * n_pair), ceil(log2(1/alpha_edge)) )
              = max( ceil(0.5 * 26), ceil(log2(100)) ) = max(13, 7) = 13   (at n_pair = N_PAIR_MIN)
   ```

   `Delta_edge` never contributes to, and is never Bonferroni-pooled with, the primary synergy
   family's `p_L`/`p_V` (§12) — it does not participate in the primary synergy claim at all, only
   in the separate boundary-confound abandonment check below.

4. **Exclusion robustness check.** Recompute `loc_med` after dropping the below-median-edge-rank
   elements of `H_hat_trunc(C)`:

   ```text
   loc_med_excl_near_edge(seed) = median_{i ∈ H_hat_trunc(C), edge_rank(i) >= 0.5} d_ell(i)
   ```

   Report `loc_med_excl_near_edge` next to `loc_med` for every BH seed (descriptive, "report
   without retuning," §14).

**What counts as "confusión de frontera" — conjunctive, not either/or.** Proximity to the box wall
alone does not kill this design: a selector can legitimately prefer near-boundary minimals if the
horizon-localization advantage survives once those elements are set aside. Abandonment criterion 2
(§15) requires **both**:

```text
(a) step 3's sign test on Delta_edge is significant in its own separate family
    (p_edge <= alpha_edge = 0.01, n_c >= MIN_N_edge = 13 at n_pair = N_PAIR_MIN, same
    conditional-null formulation as §12's p_c, but NOT Bonferroni-pooled with p_L/p_V);
AND
(b) the §12 synergy advantage is materially reduced or reversed once near-edge elements are
    excluded — operationally, loc_med_excl_near_edge(seed) no longer clears the same
    directional-significance-plus-EFFECT_FLOOR bar of §12 against H_hat_L(C)/H_hat_V(C),
    recomputed with H_hat_trunc(C) replaced by its near-edge-excluded band.
```

If (a) holds without (b) — `H_hat_trunc(C)` skews near-wall but the localization advantage persists
after exclusion — this is reported as a descriptive flag, not an abandonment trigger: proximity to
the boundary is then incidental, not explanatory. If (b) holds without (a), the loss under exclusion
is attributed to reduced band size / statistical noise, not to a boundary artifact, and is reported
under §14 rather than §15. This conjunctive test is a concrete, deterministic computation at the
now-adopted `alpha_edge`, `alpha_FWER`, and `EFFECT_FLOOR` (§12) — it introduces no numeric
parameter beyond the ones already pinned there.

`d_edge`, `d_edge_ell`, and `edge_rank` are geometric/rank quantities computed from `(t, r)`
coordinates and are not derived from `L(i)` or `V(i)`, so they are not algebraically redundant with
either — independent of whether an order-only alternative is later found (see above).

**EDGE_CONTROL status: RESOLVED as a post-selection diagnostic only.** It is not, and must not be
treated as, a selector or a competing baseline that chooses its own subset of `Min(C)` (§11.4). The
open question of whether a non-circular order-only proxy independent of `L`/`V` exists (above) is
left unresolved for future work; it does not block this diagnostic, which relies on the coordinate
license already granted by §4/§9, not on that open question being settled.

## 10. Primary success criterion

The primary scientific endpoint is BH localization at `9600.0`.

Success requires all of:

```text
valid_BH_seeds >= 26 / 32
median_BH(loc_med) <= 3.0
median_BH(loc_q75) <= 5.0
```

and the MINK same-cloud control must not spuriously localize to the same hidden radius:

```text
false_positive_MINK_fraction <= 0.25
```

where a MINK seed is a false positive if:

```text
loc_med_MINK(seed) <= 3.0
```

The MINK threshold is a control against a box-boundary artifact selecting the arbitrary coordinate
`r=R_S` even when no BH causal relation is present.

This is a necessary, not sufficient, condition for calling `T(i)` a useful localizer: §11 and §12
must also hold before any synergy claim.

## 11. Baseline controls

`T(i)` is not judged useful merely by passing §10 in isolation. The following controls are
mandatory before any synergy claim, run under the identical observation channel (§4), abstention
gate (§8), and scoring machinery (§9, §9.1) as `H_hat_trunc(C)`, on the same seeds and intensities.

### 11.1 Low-`L` control

Single-component score using only `rank_L` from §7.1:

```text
T_L(i) = 1.0 - rank_L(i)
```

Selected via the identical procedure of §7.2 (same `k_floor`, `k_cap`, tie-expansion-or-abstain
rule), substituting `T_L` for `T`. Output set: `H_hat_L(C)`.

### 11.2 Low-`V` control

```text
T_V(i) = 1.0 - rank_V(i)
```

Selected via the identical procedure of §7.2, substituting `T_V` for `T`. Output set: `H_hat_V(C)`.

### 11.3 Random-uniform control

For each seed, draw `band_size(seed) = |H_hat_trunc(C)|` elements uniformly without replacement
from `Min(C)`, using a deterministic RNG stream independent of the sprinkle RNG and of `L`, `V`,
and coordinates:

```text
rng_control(seed) = numpy.random.default_rng((seed, RANDOM_CONTROL_SALT))
H_hat_rand(C) = rng_control(seed).choice(Min(C), size=band_size(seed), replace=False)
```

**`RANDOM_CONTROL_SALT = 20260720` — pinned in this revision.** A fixed integer constant, chosen
before any run and independent of any run output (no seed has been drawn or evaluated under this
contract at the time this value is fixed, so it cannot leak or tune to a result). Follows this
repository's own existing convention for a fixed, documented, date-derived constant, e.g.
`VALIDATION_DRAW_SEED = 20260622` and `GATE_NULL_MC_SEED = 20260621` (`nachocausal/thresholds.py:65,139`)
— an 8-digit `YYYYMMDD` literal recording the date the constant was fixed, not a data-dependent
quantity. `20260720` also numerically falls outside every seed range excluded or reserved in §3
(all of which are 7-digit numbers `<= 4_600_031`), so it cannot be mistaken for a realization seed.
`numpy.random.default_rng` accepts a tuple of integers as `SeedSequence` entropy, so
`(seed, RANDOM_CONTROL_SALT)` gives a stream that is distinct from, but deterministically derived
from, the sprinkle RNG for the same seed integer — it uses the seed as an index only, never a
coordinate, `L`, or `V` value, so it stays order-only-safe.

**What `RANDOM_CONTROL_SALT` is and is not.** `RANDOM_CONTROL_SALT = 20260720` is a deterministic
stream-separation and reproducibility constant. It does not constitute a source of entropy and
does not by itself guarantee statistical independence: the actual entropy and the independence of
`rng_control(seed)` from the sprinkle RNG come from `numpy`'s `SeedSequence` construction combining
this fixed tag with the per-realization `seed` integer, not from `RANDOM_CONTROL_SALT` alone. Its
only job is to make the random-uniform control's stream provably distinct, per seed, from every
other RNG use keyed by that same `seed` integer elsewhere in the pipeline — a labelling device, not
a randomness source.

If `band_size(seed) = 0` (i.e. `H_hat_trunc(C)` itself abstained), this control abstains for that
seed too; no separate abstention branch is introduced.

Matching the control's band size to `H_hat_trunc(C)`'s own band size keeps `loc_med`/`loc_q75`
comparisons apples-to-apples in `|S|`, without referencing any target-region label — the band size
is derived from `T`'s own order-only output for that seed, not from `r`, `R_S`, or kind.

### 11.4 Edge control

**Not a fifth competing selector, by design choice — not because none could exist.** §9.1's
edge-proximity diagnostic (`d_edge`, `d_edge_ell`, `edge_rank`) is a post-selection covariate
reported for `H_hat_trunc(C)`, `H_hat_L(C)`, `H_hat_V(C)`, and `H_hat_rand(C)`. It is deliberately
kept out of the order-only selection channel because it is coordinate-based, and §4 restricts
selection to the finite partial order only. §9.1 explicitly does **not** claim that no order-only
edge-proximity selector could ever be constructed — only that none has been identified or
validated in this repository, which is a design gap, not a redundancy theorem.

A coordinate-based **`low d_edge` selector** — picking the `k_floor`/`k_cap` band of minimals with
the smallest `d_edge_ell` — is a distinct, structurally possible idea: a *geometric negative
control* that would test whether ranking directly on box-wall proximity alone reproduces
`H_hat_trunc(C)`'s apparent localization. If such a selector is added in a future revision, it
must be explicitly flagged as using coordinates at selection time and as falling **outside** the
order-only channel of §4 — it would not be a peer of `H_hat_L(C)`/`H_hat_V(C)`/`H_hat_rand(C)`, all
three of which are order-only. This draft does not adopt it; it is noted here only so the
distinction between "diagnostic" (§9.1, adopted) and "selector" (not adopted) is unambiguous.

### 11.5 Global causal-height confound

Checked read-only against `docs/preregistration_square_box_boundary_localization.md` and `docs/
preregistration_new_geometry_future_observables.md`: neither sibling contract defines a
realization-level "global causal height" or "realization depth" variable distinct from per-minimal
`L(i)`. No such variable currently exists in this repository's frozen contracts to inherit as a
confound. This item is left absent, not fabricated. If a future contract defines one, it should be
added here as a further reported covariate.

## 12. Synergy / superiority criterion

This is the quantitative contract required before `T(i)` may be called an improvement over its
isolated components. **PI-adjudicated in this revision**: `alpha_FWER`, `EFFECT_FLOOR`,
`N_PAIR_MIN`, and the general `MIN_N(alpha, d)` floor are now pinned (below), closing the last
open numeric items flagged in the prior round. This closes the quantitative contract required for
`READY_FOR_FINAL_PREREGISTRATION_REVIEW` (§18); it does not by itself freeze the document (§18).

**Unit of analysis.** One BH-kind seed at `TRUNC_FUT_PRIMARY_INTENSITY`, restricted to seeds where
`H_hat_trunc(C)`, `H_hat_L(C)`, and `H_hat_V(C)` are all non-abstained (paired comparison; an
abstention in any one of the three excludes that seed from that pairwise comparison, mirroring the
paired-validity logic already used for `D_L`/`D_V` in
`dev/run_new_geometry_future_observables.py:319-328`).

**Primary metric.** `loc_med(seed)` (§9) for each of `H_hat_trunc`, `H_hat_L`, `H_hat_V`.

**Contrasts.**

```text
Delta_L(seed) = loc_med_{H_hat_L}(seed) - loc_med_{H_hat_trunc}(seed)
Delta_V(seed) = loc_med_{H_hat_V}(seed) - loc_med_{H_hat_trunc}(seed)
```

`T` is directionally better than a component on a given seed when the corresponding `Delta > 0`
(the component's localization error exceeds `T`'s).

**Why not the repository's existing sign-flip permutation test.** `exact_sign_flip_pvalue`
(`dev/run_new_geometry_future_observables.py:270-284`) tests the *sign-flip-invariant symmetry* of
a set of paired differences: it enumerates random sign flips of the differences and asks how often
the flipped sum is at least as extreme as the observed sum. That null is justified in its original
use (`D_L = cv_L_BH - cv_L_MINK` on the same cloud, §10 of
`docs/preregistration_new_geometry_future_observables.md`) because "BH" and "MINK" are two labels
applied to an otherwise exchangeable pair of causal laws on the same cloud: under the null that the
two laws behave identically, swapping which label is which is a genuine symmetry of the generative
model, which is what licenses treating each difference's sign as an independent coin flip with
magnitude preserved.

`Delta_L(seed)` and `Delta_V(seed)` here compare two **deterministic** selectors (`T` vs `T_L`, or
`T` vs `T_V`) applied to the *same* realization. There is no label-swap symmetry between "the `T`
selector" and "the `T_L` selector" analogous to the BH/MINK case — they are not two exchangeable
draws from a common null process, they are two fixed functions of the same poset. Reusing the
sign-flip-on-magnitude test here would need a separate justification for why the *magnitude* of
`Delta_L(seed)` is symmetric about zero under the null, which this draft does not have and will not
assert without one.

**Adopted test: exact one-sided sign test, explicit null.** For each control `c ∈ {L, V}`, write
the paired difference as `Delta_{c,s} = M_s(T) - M_s(c)`, where `M_s(sel) := loc_med(seed=s)` (§9)
for the set selected by `sel` — i.e. `M_s(sel) = median_{i ∈ selected set} |r_i - R_S| / ell`, oriented
so `Delta_{c,s} > 0` means `T` improved on control `c` for seed `s` (in the `Delta_L`/`Delta_V`
notation above, `Delta_L(seed) ≡ Delta_{L,seed}`, `Delta_V(seed) ≡ Delta_{V,seed}`).

Seed-to-seed independence (each seed keys an independent `numpy.random.default_rng` stream, §3/§4;
the evaluation seed set is disjoint across seeds) licenses a binomial model **across realizations**,
but independence alone does not fix the null success probability at `1/2` — that has to be stated
as part of `H0`, not assumed implicitly. The hypotheses, conditioned on a nonzero difference (an
exact tie carries no directional information and is excluded, not treated as a half-count in either
direction):

```text
H0_c:  Pr(Delta_{c,s} > 0 | Delta_{c,s} != 0) <= 1/2
H1_c:  Pr(Delta_{c,s} > 0 | Delta_{c,s} != 0) >  1/2
```

```text
n_c = #{s : Delta_{c,s} != 0}          (paired-valid BH seeds with a nonzero difference)
k_c = #{s : Delta_{c,s} > 0}
p_c = P(Binomial(n_c, 1/2) >= k_c)      (exact one-sided binomial tail)
```

**Tie accounting.** Seeds with `Delta_{c,s} = 0` are excluded from `n_c`, per the conditional null
above; both `n_c` and the excluded-tie count `#{s : Delta_{c,s} = 0}` are reported for every `c`, so
an unusually large tie fraction is visible rather than silently reducing test power.

**Entry floor on `n_pair` — `N_PAIR_MIN = 26` (ADOPTED, PI-adjudicated).** `n_pair` is the number
of paired-valid BH seeds from the "unit of analysis" above (all three of `H_hat_trunc(C)`,
`H_hat_L(C)`, `H_hat_V(C)` non-abstained). Require `n_pair >= N_PAIR_MIN = 26`, reusing exactly the
`26/32` joint-validity fraction §10 already anchors for `T`'s own primary criterion, applied here to
the joint (triple-selector) validity requirement instead of `T` alone. If `n_pair < 26`, §12 is not
entered at all: terminal is `INSUFFICIENT_VALID_PAIRS` (contract/design tier, mirroring the
precedent in `dev/run_new_geometry_future_observables.py:325-328`, formalized in §16.1), and no
synergy claim — positive or negative — is made.

**Family size `d` and `alpha_FWER` — ADOPTED, PI-adjudicated.** The primary synergy family has
`d = 2` comparisons: `T` vs low-`L`, `T` vs low-`V`. The family-wise error rate is
`alpha_FWER = 0.01`; with the Bonferroni split already fixed under "Multiplicity correction" below,
the per-contrast threshold is:

```text
alpha_per_contrast = alpha_FWER / d = 0.01 / 2 = 0.005
```

**Minimum-`n_c` floor, general form parametrized by `d` — ADOPTED (new in this revision).** A test
run on very few nonzero differences can be uninformative without triggering any formal abstention,
and — independently — a test cannot pass at all if even a unanimous run of `n_c` cannot reach the
required significance once the family's multiplicity correction is applied. Both constraints are
folded into one floor, written to keep the multiplicity factor `d` visible rather than folding it
silently into a single "2/alpha" constant:

```text
n_c >= MIN_N(alpha, d),   MIN_N(alpha, d) = max( ceil(0.5 * n_pair),  ceil( log2( d / alpha ) ) )
```

(here `alpha` is the *family-wise* `alpha_FWER`, not the already-Bonferroni-divided per-contrast
value — `log2(d/alpha) = log2(1/(alpha/d)) = log2(1/alpha_per_contrast)`, so this is exactly the
smallest `n` with `2^-n <= alpha_per_contrast`, just written to show the `d` provenance explicitly.)
`ceil(0.5 * n_pair)` is the structural informativeness component — "at least half of the
paired-valid seeds must actually discriminate `T` from control `c`." `ceil(log2(d/alpha))` is the
**exact reachability floor**: for a one-sided exact sign test on `n_c` nonzero differences, the
smallest achievable one-sided p-value is `p_min(n_c) = 2^-n_c` (a unanimous `k_c = n_c` win); if
`2^-n_c > alpha/d`, the test cannot pass *even with a perfect result*, regardless of the
informativeness floor. Taking the `max` guarantees `MIN_N` never permits a test that is structurally
unwinnable at the adopted `alpha_FWER`.

If `n_c < MIN_N(alpha_FWER, d)` for either `c`, the synergy test for that component is
`INCONCLUSIVE_TIE_DOMINATED` (§16.1) rather than reported as a (possibly spurious) pass or fail.

**Reachability at the adopted parameters, `alpha_FWER = 0.01`, `d = 2`, worst case
`n_pair = N_PAIR_MIN = 26`** (verified by exact enumeration, not asymptotics):

```text
n_reach = ceil(log2(2/0.01)) = ceil(log2(200)) = 8
MIN_N   = max(ceil(0.5*26), 8) = max(13, 8) = 13     (the 0.5-floor dominates)
```

At `n_c = MIN_N = 13`, the exact critical value is `k_c >= 12` (i.e. `p = P(Binomial(13,0.5)>=12)
≈ 1.71e-3 <= 0.005`, while `k_c=11` gives `p ≈ 1.12e-2 > 0.005`) — a demanding but reachable bar,
confirming the 13-seed informativeness floor does not by itself make the test unwinnable at
`alpha_FWER = 0.01`. `MIN_N(0.01, 2)` must still be recomputed with the *realized* `n_pair` (which
may exceed 26, only raising the floor) before the synergy test is run.

**Why `alpha_FWER = 0.01`, not `1e-4` (PI-adjudicated rationale, verified by exact enumeration).**
At `alpha_FWER = 0.01` (`alpha_per_contrast = 0.005`), the minimum passing margin at each of the
three seed counts that can arise in this contract is:

```text
n_c = 13 (= MIN_N at n_pair = 26):  need k_c >= 12/13
n_c = 26 (= n_pair = N_PAIR_MIN, no ties):  need k_c >= 20/26
n_c = 32 (= n_pair at full support, no ties):  need k_c >= 24/32
```

At `alpha_FWER = 1e-4` (`alpha_per_contrast = 5e-5`), the same three counts require:

```text
n_c = 15 (= MIN_N(1e-4, 2) at n_pair = 26, reachability floor dominates):  need k_c = 15/15 (unanimous)
n_c = 26:  need k_c >= 23/26
n_c = 32:  need k_c >= 28/32
```

Both figures were checked by exact binomial enumeration, not the asymptotic reachability bound
alone. `1e-4` would turn this exploratory kill-test into a near-unanimity requirement (`15/15` at
the informativeness floor, `>=88%` of seeds even at full support `32/32`), which conflates "no
effect" with "insufficient power against an extraordinarily severe threshold" — a failure at that
level would be difficult to interpret either way. `alpha_FWER = 0.01` remains a demanding bar
(`>=12/13`, `>=20/26`, `>=24/32`, i.e. never below roughly `75%` directional agreement) while
staying interpretable as a test of *reproducible superiority*, not near-universal signal. This is
the PI's stated basis for adopting `0.01` over `1e-4` for this specific test.

**Minimum effect size — required in addition to directional significance.** A directionally
significant but immaterial `Delta` is not the kind of synergy this contract wants to claim. Both of
the following are required, not just the sign test:

```text
median_s(Delta_{L,s}) >= EFFECT_FLOOR
median_s(Delta_{V,s}) >= EFFECT_FLOOR
```

The median for this floor is taken over **all `n_pair` paired-valid seeds, including seeds where
`Delta_{c,s} = 0`** — unlike `n_c`/`p_c` above, which exclude exact ties by construction of the
sign test. This is a deliberate difference, stated explicitly to avoid ambiguity: the sign test asks
"does `T` win more often than not, among seeds where there is a difference at all," while the effect
floor asks "is `T`'s typical advantage, across the whole evaluated population, at least material" —
including seeds contributing a zero difference is the correct denominator for that second question.
Uses the even-`n` median convention of §9.

**`EFFECT_FLOOR = 1.0` — ADOPTED, PI-adjudicated as a materiality threshold, not an instrumental
resolution limit.** A coordinate-uniform Poisson sprinkling is *not* quantized in steps of `ell` —
`ell` is a mean spacing scale (`ell = (intensity/BOX_AREA)^(-1/2)`, §5), not a measurement grid, so
it is not claimed that a `Delta_{c,s}` smaller than one `ell` is unmeasurable or indistinguishable
from noise as a matter of instrument resolution. `EFFECT_FLOOR = 1.0` is adopted as:

> a pre-registered threshold of *material relevance*, expressed in units of the discreteness scale
> `ell`; it is not a claim about minimum measurable difference or coordinate quantization.

Concretely, `median_s(Delta_{c,s}) >= 1.0` means "`T`'s typical advantage over control `c` is at
least one discreteness scale," which this contract treats as the smallest advantage worth calling
physically interesting — the same `ell`-unit scale §10's own primary criterion already uses as its
unit of account for `loc_med`/`loc_q75` — not the smallest advantage that could in principle be
measured. `POOLED_SD_FLOOR`/`K_LOC` (`nachocausal/thresholds.py:78,98`) are cited only as precedent
for choosing an `ell`-unit-sized constant as a materiality threshold in this repository's style, not
as evidence of an instrumental resolution limit.

**Direction required for a synergy claim (full statement, all constants ADOPTED).** For both
`c ∈ {L, V}`:

```text
n_pair                 >= N_PAIR_MIN = 26
n_c                    >= MIN_N(alpha_FWER=0.01, d=2) = 13   (recompute at realized n_pair)
p_c                    <= alpha_per_contrast = 0.005
median_s(Delta_{c,s})  >= EFFECT_FLOOR = 1.0                 (median over all n_pair seeds, ties included)
```

`T` must beat **both** isolated components, on a sufficiently large and sufficiently informative
seed set, directionally at the pre-registered significance level, and by at least the pre-registered
materiality margin — not just one component, not on a tie-dominated or reachability-infeasible
sample, and not by a sub-`EFFECT_FLOOR` margin.

**Multiplicity correction.** Two directional tests are run (`Delta_L`, `Delta_V`) against the same
primary question; this fixes `d = 2` and the Bonferroni split `alpha_per_contrast = alpha_FWER / 2
= 0.005` used above. No further correction is applied across intensities: only the primary
intensity (`TRUNC_FUT_PRIMARY_INTENSITY`) feeds the synergy claim; other intensities are
secondary/descriptive only (§14).

**`alpha_FWER = 0.01` — ADOPTED, PI-adjudicated.** Two literal precedents existed elsewhere in the
repository: `P_PERM_THRESHOLD = 1e-4` (`nachocausal/thresholds.py:87`, `theta_sig`) and
`P_PERM_THRESHOLD = 0.01` (`docs/preregistration_new_geometry_future_observables.md` §10, mirrored
in `dev/run_new_geometry_future_observables.py:61`). Both were anchored for a
sign-flip-on-magnitude test with a different null-symmetry justification (above), so neither
transferred automatically to the sign test adopted here; the PI adjudication above selects
`alpha_FWER = 0.01` for *this* test, with the rationale given above under "Why `alpha_FWER = 0.01`,
not `1e-4`."

**Consequence for freeze status.** With `alpha_FWER`, `d`, `N_PAIR_MIN`, `MIN_N(alpha, d)`, and
`EFFECT_FLOOR` all pinned, the quantitative synergy contract is now fully specified. This closes the
last open item blocking `READY_FOR_FINAL_PREREGISTRATION_REVIEW` (§18). It does not by itself mark
this document `FROZEN`: a final literal review, contract sealing, and controlled update of the
evidence-directory scaffolding (§17) still remain, per PI instruction.

## 13. Development gate before confirmatory evaluation

**Ordering rule (explicit, not left to session memory).** No evaluation on `TRUNC_FUT_DEV_SEEDS`
or `TRUNC_FUT_EVAL_SEEDS` may occur before this contract's freeze commits. Running the dev-only
support check below while the design (geometry, `T`, thresholds) is still legally revisable would
be "explore then lock" on ground-truth-scored descriptive output — exactly what `RESPECT_SEAL_FREEZE`
and the founding no-post-hoc-tuning rule exist to forbid. The freeze commit is the boundary; only
after it may any seed in either band be drawn.

Before any confirmatory evaluation on `TRUNC_FUT_EVAL_SEEDS`, a development-only support check may
be run on `TRUNC_FUT_DEV_SEEDS` and may report only:

```text
abstention fraction
band_size distribution
median_BH(loc_med) and median_BH(loc_q75), descriptive only
false_positive_MINK_fraction, descriptive only
edge_med distribution (§9.1), descriptive only
support/contract triggers
```

It may not emit a scientific terminal.

If the development check shows catastrophic support failure, the protocol may be closed as a
design failure before confirmatory evaluation. If the development check merely suggests weak
localization, the allowed choices are: execute the frozen confirmatory evaluation anyway, or close
this localizer as a documented design-negative. Redesign requires a new contract.

## 14. Secondary robustness checks

Report without retuning:

```text
median_BH(loc_med) by intensity
median_BH(loc_q75) by intensity
median band_size by kind and intensity
MINK false-positive fraction by intensity
abstention fraction by kind and intensity
median edge_med and median edge_rank_med by kind, intensity, and selection arm
  (H_hat_trunc, H_hat_L, H_hat_V, H_hat_rand)
median Delta_edge and loc_med_excl_near_edge at the primary intensity, BH only (§9.1)
```

No threshold may be changed after evaluation.

## 15. Abandonment criteria

Any of the following closes this localizer design as a documented negative result for **this**
observable and **this** geometry — not a refutation of horizon physics in general, and not a
retroactive claim about the frozen largest-gap contract (`docs/
preregistration_square_box_boundary_localization.md`) or the sealed dispersion result
(`docs/new_geometry_future_observables_addendum.md`).

1. **Falta de sinergia (no synergy).** This is the genuine scientific negative — `§16.1` Step 3's
   "definitive failure": for either `c ∈ {L, V}`, `p_c > 0.005` (with `n_c >= 1`), or
   `median_s(Delta_{c,s}) < 1.0` (always evaluable, over all `n_pair` seeds) — a directionally
   significant but below-materiality-threshold margin abandons the design just as a null direction
   does. `n_pair < N_PAIR_MIN` (`INSUFFICIENT_VALID_PAIRS`) and `n_c < MIN_N(0.01, 2)` without a
   definitive failure (`INCONCLUSIVE_TIE_DOMINATED`) are deliberately **not** listed here: per §16's
   own rule that contract/design terminals must not be reported as scientific negatives, an
   insufficient or tie-dominated sample means the design was not conclusively tested, not that it
   failed — it does not by itself abandon the design (though a *persistent* inability to clear
   `N_PAIR_MIN`/`MIN_N` across repeated evaluation would be a separate, support-level concern to
   raise with the PI, outside this criterion's scope).
2. **Confusión de frontera (boundary confound).** The conjunctive condition fixed in §9.1 holds:
   (a) the sign test on `Delta_edge` is significant in its own separate family
   (`p_edge <= alpha_edge = 0.01`, `n_c >= MIN_N_edge`) in the direction of `H_hat_trunc(C)`
   selecting near-wall elements, **and** (b) the §12 synergy advantage is materially reduced or
   reversed once near-edge elements are excluded (§9.1's exclusion robustness check). Near-wall
   selection alone, without loss of the localization advantage under exclusion, is a descriptive
   flag (§14), not an abandonment trigger. A signal not distinguishable from a global causal-height
   confound, if one is later defined (§11.5), is a separate, independent trigger under this same
   criterion.
3. **Falso positivo topológico (topological false positive).** `H_hat_trunc(C)` systematically
   selects corners, bounding-box edges, or other artifact-censored regions instead of a candidate
   band near `r=R_S`, as diagnosed via `edge_med`/`edge_rank` and the coordinate distributions
   reported under §9/§9.1.
4. **Fragilidad de convención (convention fragility).** Results change materially if fractional
   (average) ranking is swapped for a pre-registered alternative tie convention, run as a
   sensitivity check, not a retune.
5. **Control de frontera irresoluble (edge control irresolvable).** Part of the fixed abandonment
   list for any future revision of this draft. It does not currently apply as stated: §9.1 adopts a
   working coordinate-based post-selection diagnostic, licensed by §4/§9 independent of whether an
   order-only alternative exists. The narrower, still-open question — whether a non-circular
   order-only proxy independent of `L`/`V` can be identified (§9.1) — remains genuinely unresolved,
   but does not by itself trigger this criterion, since the adopted diagnostic does not depend on
   resolving it. If a later revision narrows or removes the scoring-time coordinate license this
   diagnostic relies on, this criterion becomes live and must be re-evaluated before freeze.
6. **Redundancia (redundancy).** `T` turns out to be functionally/practically indistinguishable
   from `low L` alone or `low V` alone (e.g. `H_hat_trunc(C) == H_hat_L(C)` or `== H_hat_V(C)` on
   essentially all evaluated seeds).

Any of the above is a design-inviability conclusion for this specific truncated-futures localizer,
not a general statement about event-horizon recoverability from causal order.

## 16. Terminal precedence

Exactly one terminal is emitted with this precedence:

### Integrity / provenance

```text
INTEGRITY_FAILURE
SEED_OVERLAP_FAILURE
PATCH_CONTRACT_MISMATCH
IMPLEMENTATION_CONTRACT_FAILURE
```

### Contract / design

```text
FAILED_SUPPORT_CONTRACT
LOCALIZER_OVERBROAD_BAND
MINK_SPURIOUS_LOCALIZATION_CONTROL_FAIL
INSUFFICIENT_VALID_BH_SEEDS
```

### Scientific

```text
TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION_DETECTED
NO_TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION_DETECTED
INCONCLUSIVE_TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION
```

Contract/design terminals must not be reported as scientific negatives.

The terminals above answer one question: does `H_hat_trunc(C)` alone localize BH near `R_S` (§10)?
They say nothing about whether `T` improves on its isolated components (§12). §16.1 answers that
second, separate question with its own terminal, reported alongside whichever terminal above
applies to `H_hat_trunc(C)` on its own — the two are never merged into one verdict.

### 16.1 Synergy-layer terminal precedence (§11-§12)

Now that `alpha_FWER`, `N_PAIR_MIN`, `EFFECT_FLOOR`, and `MIN_N(alpha, d)` are pinned (§12), this
layer has its own terminal, evaluated after (and independently of) §16's terminal, by the following
deterministic, mutually-exclusive procedure — evaluated in this exact order, each step's condition
checked only if no earlier step already returned a terminal:

```text
Step 1. n_pair < N_PAIR_MIN (= 26)?
        -> INSUFFICIENT_VALID_PAIRS.  (§12 not entered further; stop.)

Step 2. For each c in {L, V}, compute n_c, k_c, p_c (undefined if n_c = 0) and
        median_s(Delta_{c,s}) (always defined: computed over all n_pair seeds, ties included).

Step 3. "Definitive failure" for a contrast c :=
            (n_c >= 1 AND p_c > alpha_per_contrast)   OR   (median_s(Delta_{c,s}) < EFFECT_FLOOR).
        Note the EFFECT_FLOOR clause is always evaluable, including at n_c = 0 (all-tied seeds give
        median_s(Delta_{c,s}) = 0 < EFFECT_FLOOR, itself a definitive failure — no special-casing
        of n_c = 0 is needed).
        If c=L definitively fails, OR c=V definitively fails (checked for BOTH, independently of
        the other contrast's n_c) ->  NO_TRUNCATED_FUTURES_SYNERGY_DETECTED.  (stop.)
        A definitive failure on one contrast is never suppressed or hidden by tie-domination on the
        other contrast — Step 3 is evaluated for both c before Step 4 is reached for either.

Step 4. Neither contrast definitively failed (Step 3). If n_c < MIN_N(alpha_FWER, d) for c=L or
        c=V (a numeric pass that is not yet trustworthy, or no data at all beyond what Step 3
        already ruled out) ->  INCONCLUSIVE_TIE_DOMINATED.  (stop.)

Step 5. Neither contrast failed (Step 3) and both cleared MIN_N (Step 4): a genuine synergy signal
        exists on both contrasts. Only now is the §9.1 boundary-confound diagnostic evaluated:
            (a) H_hat_trunc(C) selects significantly near-wall elements (edge-family sign test,
                alpha_edge, MIN_N_edge, §9.1)   AND
            (b) the synergy advantage established in Steps 3-4 is materially reduced or reversed
                once near-edge elements are excluded (§9.1's exclusion robustness check).
        (a) AND (b) both hold -> BOUNDARY_CONFOUND_DETECTED.
        Otherwise             -> TRUNCATED_FUTURES_SYNERGY_DETECTED.
```

This ordering resolves two ambiguities by construction, not by convention:

- A contrast that is already, definitively negative (Step 3) can never be masked by tie-domination
  on the *other* contrast, because Step 3 is checked for both `c ∈ {L, V}` before Step 4 is reached
  for either.
- `BOUNDARY_CONFOUND_DETECTED` (Step 5) is only reachable after both contrasts have already cleared
  significance, materiality, *and* the informativeness floor (Steps 3-4) — it is a check on whether
  an already-established synergy signal is a boundary artifact, never a way to reach a "confound"
  verdict when no synergy advantage existed to begin with.

**Terminal codes, by tier (for reference; Step order above is authoritative):**

```text
Contract / design:  INSUFFICIENT_VALID_PAIRS, INCONCLUSIVE_TIE_DOMINATED, BOUNDARY_CONFOUND_DETECTED
Scientific:          TRUNCATED_FUTURES_SYNERGY_DETECTED, NO_TRUNCATED_FUTURES_SYNERGY_DETECTED
```

Exactly one of the five is emitted per evaluation. A `BOUNDARY_CONFOUND_DETECTED` or
`INCONCLUSIVE_TIE_DOMINATED` terminal must not be reported as `NO_TRUNCATED_FUTURES_SYNERGY_DETECTED`
— the contract/design tier here mirrors §16's own separation between design failure and scientific
negative.

### 16.2 Downstream reporting conditions (binding on any future summary/addendum)

Two conditions, closing gaps identified during committee review
(`docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md`), on how results under
this contract may later be reported outside this document:

1. **Co-statement requirement.** Any future summary or addendum that cites the §16
   primary-localization terminal (`TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION_DETECTED` or its
   negatives) must, in the same statement, also cite the §16.1 synergy terminal. The two terminals
   answer different questions — does `H_hat_trunc(C)` alone localize; does `T` add anything over
   its isolated components — and can diverge. Citing one without the other risks implying a
   validated *combined* observable when only one half was established.
2. **Independent certification before a confirmatory terminal is treated as settled.** Before any
   future confirmatory-evaluation terminal produced under this contract is cited as a result
   (in `README.md`, a roadmap document, or elsewhere), an `/auditor` pass over the produced
   `evaluation_summary.json`/`RESULT_SEALED.txt` must certify it. The session that runs the
   evaluation is not, by itself, its own sole verifier.

### 16.3 Programmatic context (stated plainly, not filed silently)

This is the third localizer design evaluated in the `SQUARE_BOX_2P4`/tall-box causal-truncation
lineage: R-VAR (`CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]`) → the frozen largest-gap localizer
(dev-only diagnostic landed far from `R_S`, no confirmatory result emitted, §0) → this
truncated-futures design, whose low-`L`/low-`V` observable choice was itself motivated by reading
the largest-gap contract's dev-diagnostic outcome. Each individual contract's thresholds remain
independently anchored before its own validation seeds are seen (no single-contract violation of
`RESPECT_SEAL_FREEZE`), but across the sequence the observable itself has been iteratively
re-designed in response to ground-truth-scored feedback from prior attempts on `dev/` seeds. That
is within the founding rules as long as it stays on `dev/`, but it is exactly the mechanism
`NO_GROUND_TRUTH_LEAKAGE` exists to bound program-wide, not just contract-by-contract — and it
should be visible, not accumulate silently as "not a reopening" is repeated at each new contract.

## 17. Evidence directory

If this protocol is later frozen and executed, outputs must go under:

```text
evidence/square_box_truncated_futures_localization_20260719/
```

Required files:

```text
manifest.json
claim_ledger.md
per_seed_localization.csv
evaluation_summary.json
evaluation_report.md
terminal.txt
RESULT_SEALED.txt
```

### 17.1 Seal mechanism (clarified in this revision)

**The seal for this contract, once frozen, is the git commit SHA that first tracks this file in
its `FROZEN` state — not a separate SHA256 computed over the document's own text.** This matches
the established pattern for every seal already in this repository's chain
(`docs/preregistration_001_addendum.md`, `docs/preregistration_002.md`,
`docs/estimator_v2_seal.md`): each is a git-commit SHA over a tracked file, re-checkable by
inspecting that commit. There is no `Makefile verify-seal`-style target for hashing a prereg
document's own body, and no sibling contract in this cluster used one — `docs/preregistration_square_box_boundary_localization.md`
froze via a `STATUS: CONTRACT_FROZEN` header block, not a document hash. An unrecheckable seal is
decoration, not a guardrail; this contract does not adopt one. The commit that first tracks this
file with a `FROZEN` status line **is** the seal, full stop.

**Two valid ways to realize this at freeze time; no self-reference.**

1. **Single commit.** The freezing commit itself constitutes the seal, via git's own history — its
   SHA is the seal and is looked up from `git log`/`git show` when needed. The SHA is **not**
   inserted into any file inside that same commit.
2. **Two commits.** An immutable freeze commit (the `FROZEN` status line, the design text, no
   seal-value field) followed by a separate attestation commit that literally records the first
   commit's SHA (e.g. in `evidence/square_box_truncated_futures_localization_20260719/manifest.json`
   or a short addendum).

Either is acceptable; which one is used is a Stage B implementation detail, not a further open
question in this draft. What is **not** acceptable under either option: amending the freeze commit
(`git commit --amend`) to insert its own SHA into itself after the fact. A commit cannot attest to
its own hash before that hash exists, and `--amend` would rewrite history to fake that
self-reference — this is a `RESPECT_SEAL_FREEZE` violation, not a shortcut.

## 18. Current status

This contract is now frozen (`FROZEN_DATE: 2026-07-20`, header above). No seeds have been executed
and no data has been generated under this contract — freezing pins the design; it does not run it.

Resolved in earlier revision rounds (cumulative, still valid):

- `L(i)` pinned to link (cover-relation-step) units, verified against the existing repository
  convention, with the `L_elements = L_links + 1` bridge documented for any component that reports
  element counts instead (§6.2).
- `rank_L`, `rank_V` given an exact, deterministic fractional-ranking formula with a defined `m=1`
  edge case (§7.1); final `T`-ties are resolved by the pre-existing tie-expansion-or-abstain rule
  (§7.2).
- Four mandatory baseline controls are fully specified: low-`L`, low-`V`, random-uniform (§11),
  and the edge-proximity diagnostic (§9.1). The edge diagnostic is explicitly a coordinate-based,
  post-selection-only covariate, never a selector (§9.1, §11.4) — the earlier draft's claim that no
  order-only alternative could exist was walked back: §9.1 now states this as an open, unresolved
  question (a design gap), not a theorem, and the adopted diagnostic is justified independently of
  that question by the coordinate license already granted in §4/§9.
- A concrete, conjunctive boundary-confound procedure is fixed: within-realization `edge_rank`, the
  `Delta_edge` sign test (reusing the same `alpha` as §12), and an exclusion robustness check on
  `loc_med` — "confusión de frontera" requires *both* near-wall selection *and* loss of the
  localization advantage under exclusion; near-wall selection alone does not abandon the design
  (§9.1, §15.2).
- The synergy/superiority test is an exact one-sided sign test on `Delta_{c,s} = M_s(T) - M_s(c)`
  for `c ∈ {L, V}`, with an explicit conditional null (`Pr(Delta_{c,s} > 0 | Delta_{c,s} != 0)`),
  explicit tie accounting, and a justification for why the repository's existing
  sign-flip-on-magnitude test does not transfer to a comparison of two deterministic selectors on
  the same realization (§12).
- Two additional precisions were made in the prior revision round, both requested by review:
  (1) `MIN_N(alpha) =
  max(ceil(0.5*n_pair), n_reach(alpha))` now folds in an exact reachability check
  (`n_reach(alpha) = ceil(log2(2/alpha))`, the smallest `n_c` for which even a unanimous sign-test
  result could clear `alpha/2`) so the informativeness floor can never permit a structurally
  unwinnable test; a compatibility table verifies both `alpha` candidates against a new entry floor
  `N_PAIR_MIN = 26` (anchored to §10's own `26/32` fraction, applied to joint triple-selector
  validity). (2) `EFFECT_FLOOR = 1.0` is now explicitly reframed as a **pre-registered materiality
  threshold**, not an instrumental resolution limit — a Poisson sprinkling is not quantized in steps
  of `ell`, so no claim is made that sub-`ell` differences are unmeasurable, only that they are
  treated as below the threshold of physical interest this contract cares about. The effect-floor
  median is now explicitly computed over all `n_pair` paired seeds including ties, distinct from the
  tie-excluding `n_c` used by the sign test — both conventions are now stated unambiguously (§12).
- A uniform even-cardinality median convention is fixed once (§9) and reused by every median in the
  document (`loc_med`, `loc_q75`, `edge_rank_med`, `median_s(Delta_{c,s})`).
- The falsifiable physical hypothesis is stated without presupposing success, with explicit
  boundaries against over-interpretation (§1.1).
- Abandonment criteria are enumerated and updated to match the corrected §9.1/§12 mechanisms (§15).

PI-adjudicated in this revision (closes the quantitative contract):

- `alpha_FWER = 0.01` for the primary synergy family (`d = 2`: `T` vs low-`L`, `T` vs low-`V`),
  giving `alpha_per_contrast = 0.005` via Bonferroni — adopted over the `1e-4` candidate with an
  explicit, exact-enumeration-verified rationale (§12: `1e-4` would demand near-unanimity, `15/15`
  at the informativeness floor, and would make a failure uninterpretable between "no effect" and
  "insufficient power against an extraordinary threshold").
- `EFFECT_FLOOR = 1.0`, reframed and adopted as a pre-registered *materiality* threshold in `ell`
  units — explicitly not an instrumental resolution claim, since the sprinkling is not quantized in
  steps of `ell` (§12).
- `N_PAIR_MIN = 26`, reusing §10's own `26/32` joint-validity fraction for the triple-selector case
  (§12).
- `MIN_N(alpha, d) = max(ceil(0.5*n_pair), ceil(log2(d/alpha)))`, general and parametrized by the
  family size `d` so the multiplicity provenance stays visible; evaluated at the adopted primary
  parameters this gives `MIN_N(0.01, 2) = 13` at `n_pair = N_PAIR_MIN = 26`, verified reachable by
  exact binomial enumeration (§12).
- The `Delta_edge` boundary-confound check (§9.1) is fixed as its own separate diagnostic family,
  `alpha_edge = 0.01`, `d_edge = 1` — never pooled with the primary family's `p_L`/`p_V` and never
  contributing to the primary synergy claim, per PI instruction.
- Synergy-layer terminals are now defined by a deterministic, mutually-exclusive 5-step precedence
  procedure (§16.1) — `INSUFFICIENT_VALID_PAIRS`, then per-contrast definitive failure
  (`NO_TRUNCATED_FUTURES_SYNERGY_DETECTED`), then tie-domination (`INCONCLUSIVE_TIE_DOMINATED`),
  then the boundary-confound diagnostic (`BOUNDARY_CONFOUND_DETECTED` vs
  `TRUNCATED_FUTURES_SYNERGY_DETECTED`) — reported alongside, never merged into, §16's own
  primary-localization terminal. The ordering guarantees a definitive failure on one contrast is
  never hidden by tie-domination on the other, and that `BOUNDARY_CONFOUND_DETECTED` is only
  reachable once a genuine synergy signal has already been established on both contrasts.
  Abandonment criterion 1 (§15) was correspondingly narrowed to only the genuine scientific
  negative (Step 3), since §16's own rule already says contract/design terminals
  (`INSUFFICIENT_VALID_PAIRS`, `INCONCLUSIVE_TIE_DOMINATED`) must not be reported as scientific
  negatives.

Closed by committee adjudication (`/comite`, `docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md`,
`COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE`, pre-registration-warden `Verdict:
BLOCK`) — the two items the warden found this contract's own §18 named as freeze-blocking but the
committee's decision question did not include closing:

- `RANDOM_CONTROL_SALT` pinned to `20260720`, with a stated, run-output-independent derivation
  matching the repository's own date-literal convention (§11.3).
- The seal mechanism is now specified: the freezing git commit's own SHA, matching every existing
  seal in this repository's chain — no separate document-hash mechanism (§17.1).
- Two further conditions the committee's falsifier and warden roles surfaced, now written into the
  contract rather than left as external review notes: the co-statement requirement and independent
  auditor-certification condition for any future summary of results (§16.2), and the explicit
  freeze-before-evaluate ordering rule (§13).

Still open (does not block `READY_FOR_FINAL_PREREGISTRATION_REVIEW`, and per the committee's
mathematician/logician roles does not block `FROZEN` either — the adopted §9.1 diagnostic does not
depend on it):

- Whether a non-circular order-only edge-proximity proxy independent of `L`/`V` exists (§9.1) is an
  open research question, left explicitly unresolved rather than claimed impossible.

Done in this revision (Stage B, PI authorization "procede con el freeze commit"):

- Status line (top and bottom) flipped to `CONTRACT_FROZEN`, matching the sibling contract's
  `STATUS`/`FROZEN_BY`/`FROZEN_DATE` header convention
  (`docs/preregistration_square_box_boundary_localization.md:3-5`). Filename convention: the
  `_draft` suffix is **kept** — no precedent exists in this repo for renaming a `_draft`-suffixed
  file upon freezing (the sibling contract never had that suffix to begin with), and the frozen
  status header is the authoritative, unambiguous signal rather than the path. This can be revisited
  as a follow-up rename if preferred; nothing downstream depends on the current filename.
- `evidence/square_box_truncated_futures_localization_20260719/{manifest.json,claim_ledger.md,terminal.txt}`
  updated to the current (not the stale 2026-07-19-original) design content — §12's `alpha_FWER`,
  `EFFECT_FLOOR`, `N_PAIR_MIN`, `MIN_N` formula, `RANDOM_CONTROL_SALT`, and the §16/§16.1
  two-layer terminal scheme.
- The freeze commit (or, per §17.1 option 2, a following attestation commit) constitutes the seal.

```text
NO_DATA_GENERATED
NO_EVALUATION_RUN
NO_LOCALIZATION_RESULT
```

## CONTRACT FROZEN

Frozen by human review on 2026-07-20, after `/comite` adjudication
(`docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md`,
`COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE`) identified two closeable
pre-registration-warden `BLOCK` items — `RANDOM_CONTROL_SALT` unassigned and no seal mechanism
specified — both closed in a Stage A revision, followed by explicit Stage B PI authorization
("procede con el freeze commit") for this freeze.

Geometry: `SQUARE_BOX_2P4` (`T_EDGE=2.4`, `R_EDGE=2.4`, `R_CENTER=1.3`, `R_S=0.5`, aspect ratio
`1.0`).
Question: `TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION` (primary, §10) and synergy over isolated
low-`L`/low-`V` components (§12).
Seal: the git commit that introduces this `CONTRACT_FROZEN` state (§17.1) — not a document-text
hash.
`RANDOM_CONTROL_SALT = 20260720` (a stream-separation/reproducibility constant, not an entropy
source, §11.3).
Synergy contract: `alpha_FWER = 0.01`, `d = 2`, `alpha_per_contrast = 0.005`, `EFFECT_FLOOR = 1.0`
(materiality threshold, not an instrumental resolution claim), `N_PAIR_MIN = 26`,
`MIN_N(alpha, d) = max(ceil(0.5*n_pair), ceil(log2(d/alpha)))`. Edge-confound diagnostic: separate
family, `alpha_edge = 0.01`, `d_edge = 1`.
Previous R-VAR closure (`CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]`), the sealed dispersion result
(`BH_MINK_DISPERSION_DIFFERENCE_DETECTED`), and the frozen largest-gap contract remain intact and
untouched.
No data generated at freeze time. Freezing does not authorize running `TRUNC_FUT_DEV_SEEDS` or
`TRUNC_FUT_EVAL_SEEDS` — that remains a separate, later, explicitly-authorized step (§13).
