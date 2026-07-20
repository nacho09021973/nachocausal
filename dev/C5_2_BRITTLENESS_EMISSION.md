# C5.2 — Brittleness and emission of Φ★ (exact row partition)

STATUS: PATH_A_THEORY / NOT_A_CANDIDATE / CANDIDATE_5_NOT_YET_OPENED  
NO_IMPLEMENTATION / NO_SYNTHETIC_EXECUTION / NO_SEEDS / NO_FREEZE / NO_RECONSTRUCTION_CLAIM  
DATE: 2026-07-20

BINDS_TO:

- `dev/C5_NAMED_MAP_PHI_STAR.md` (Φ★ = exact rows + one maximal peel)
- `dev/C5_NONCOLLAPSE_A_VS_MARGINAL_V.md` (definitional non-collapse; flags ALWAYS_ABSTAIN)
- `dev/C5_LATERAL_ORDER_ONLY_DUAL.md` (Env, not side peel)
- Decisions 040–041; commit package `9df27fa`

Question:

> On manifoldlike finite sprinklings (and any ensemble where common-future counts fluctuate),  
> does Φ★ ever **emit**, or does exact row equality force chronic `ABSTAIN_OVERREFINED` / triviality?

---

## 0. Verdict

```text
PHI_STAR_EXACT_ROW_ENSEMBLE_EMISSION = NOT_VIABLE
DEATH_MODE = CHRONIC_ABSTAIN_OVERREFINED   (primary)
DEATH_MODE_SECONDARY = ROOF_OR_NOISE_UNSTABLE_PEEL
DEFINITIONAL_STATUS = STILL_FORMALLY_CLOSED_MAP
MARGINAL_COLLAPSE = STILL_FALSE
CANDIDATE_5_NOT_YET_OPENED
```

Φ★ remains a correct **formal** object. As a **channel that must emit a nontrivial partition** on
Poisson-like causets, exact row equality is the wrong base rule.

Successor analysis is C5.2b (`dev/C5_2B_PHI_STAR_L_SPECTRAL.md`), not a silent retune of Φ★.

---

## 1. What “emission” means

Φ★ emits only if all hold:

1. `m = |Min(C)| ≥ 4`
2. `P = Π_row(A)` has ≥ 2 blocks
3. every block has size ≥ 2 (no singletons)
4. the same `P` after one maximal peel

Failure of (2)–(3) is `ABSTAIN_TRIVIAL_PARTITION` or `ABSTAIN_OVERREFINED`.  
Failure of (4) is `ABSTAIN_ROOF_UNSTABLE`.

**Ensemble viability** (Path A sense): under a generative law `E` of interest (boxed Minkowski /
Schwarzschild sprinklings at working densities), the probability of EMIT must not be negligible for
the object to be a localization *channel*. Chronic abstention is a clean negative — not a bug in
the code that does not exist.

---

## 2. Exact row equality is a zero-measure condition under noise

### 2.1 Deterministic continuum shadow

Let continuum points `p1,…,pm` in a region `R` be the continuum analogues of minimals (or of a
past-most layer). Define

```text
a(p,q) := vol( J⁺(p) ∩ J⁺(q) ∩ R ).
```

The continuum “row” of `p_i` is the map `q ↦ a(p_i, q)` on the finite sample.

For generic positions (no continuous symmetry relating `p_i` and `p_j`),

```text
a(p_i, ·) ≠ a(p_j, ·) as functions on {p1,…,pm}.
```

So even **before** discreteness, exact row equality is non-generic. It requires a continuum
symmetry (isometry of the chart fixing the future region in a strong sense) or accidental equality
of several real numbers.

### 2.2 Poisson / counting noise — [PROVED sketch]

Conditional on the sprinkled set, each

```text
A_ij = | J⁺(i) ∩ J⁺(j) |
```

is an integer count of points in a random region (the common future inside the causet). In the
standard continuum approximation at density `ρ`,

```text
A_ij = ρ · a(p_i,p_j) + ξ_ij
```

with fluctuations of typical scale

```text
σ_ij  ≍  √(ρ · a(p_i,p_j))   (order of magnitude; Poisson-like)
```

in bulk regimes where the continuum volume is the right mean.

**Lemma (pairwise exact match is rare at large counts).**  
If `X,Y` are integer-valued with means `μ_X, μ_Y → ∞` and fluctuations `≍ √μ`, and the continuum
means differ by a fixed continuum gap `δ > 0`, then

```text
P(X = Y) → 0
```

as `ρ → ∞`. If continuum means coincide (`δ = 0`) but noise is not perfectly shared,

```text
P(X = Y) = O(ρ^{-1/2})
```

under standard local CLT heuristics for lattice distributions with variance `≍ ρ`.

**Corollary (full row match).**  
A row match `i ∼ j` requires simultaneous equalities

```text
A_ik = A_jk   for all k ∈ M
```

(`m` constraints, highly dependent but still `m-1` nontrivial off-diagonal matches plus diagonal).  
If even one coordinate has `P(match) = O(ρ^{-1/2})` and residual freedom remains in others,

```text
P(i ∼ j) → 0    as ρ → ∞
```

for each fixed pair not forced by an exact automorphism of the realized poset.

**Corollary (nontrivial emission).**  
For `Π_row` to avoid singletons, **every** minimal must share its exact row with at least one other.
That is a covering of `M` by exact-equality classes of size ≥ 2. Under independent-ish noise across
pairs, this probability vanishes super-polynomially in `m` as soon as typical counts are large.

```text
P( Φ★ emits | manifoldlike high-ρ sprinkling ) → 0.     [PLAUSIBLE-TRANSFER / standard concentration]
```

Label: not a measure-theoretic theorem certified in-repo; it is the standard reason exact combinatorial
equality is unused as a continuum estimator. For program purposes it is strong enough to reject
exact-row Φ★ as an ensemble channel.

### 2.3 Finite toy where emission works — does not save the ensemble

On hand-built posets with large discrete symmetries (identical future sets), Φ★ can emit
(`P_close` in the non-collapse note). Those are **zero-noise, symmetry-forced** configurations.
Poisson sprinklings destroy that forcing.

---

## 3. Peel stability makes emission harder, not easier

Even if a noisy `A` accidentally produced a multi-block partition without singletons, step (4)
requires the **same** partition after deleting `Max(C)`.

Deleting maximals changes every `J⁺` that touched the roof. Counts `A_ij` jump by integers of size
comparable to the roof layer contribution. Exact equality of rows is discontinuous under those
jumps:

```text
one roof point in F_i \ F_j  ⇒  several A_i· entries shift by 1 while A_j· do not.
```

So peel stability of **exact** partitions is rarer than partition existence itself.

```text
P(EMIT) ≤ P(nontrivial exact Π_row) ≪ 1
```

and the inequality is typically strict.

---

## 4. Low-density regime does not rescue the channel

At very low `ρ`, accidental equalities of small integers (`0,1,2`) become common. Then:

- emission may occur by chance;
- the partition is dominated by sampling noise and box combinatorics;
- non-marginality and horizon physics are not credible.

Path A does not treat “emits on tiny noisy posets” as viability. The program’s working regime is
manifoldlike enough for continuum geometry to matter (C3 densities, box sprinklings). In that
regime §2 applies.

---

## 5. Death mode classification

| Mode | Applies to exact-row Φ★? |
|---|---|
| Definitional collapse to `{V(i)}` | **No** (C5 non-collapse) |
| Chronic abstain / over-refined | **Yes — primary** |
| Roof-unstable when rarely nontrivial | **Yes — secondary** |
| Side-wall dominated when emits | **Open, mostly moot if never emits** |
| Useful ensemble channel | **No** |

```text
PHI_STAR_STATUS_AFTER_C5_2 =
  FORMALLY_CLOSED_MAP
  + ENSEMBLE_CHANNEL_REJECTED_EXACT_ROWS
```

---

## 6. What this does *not* authorize

- No replacement of exact rows by an `ε`-tolerance (“almost equal rows”). That is a calibrated
  threshold and reopens Decision 041’s rejection class.
- No implementation, seeds, or generator runs to “check emission rates”. The theoretical case
  against exact rows at working density is sufficient for Path A.
- No opening of `CANDIDATE_5`.

---

## 7. Mandatory fork after C5.2

```text
IF base partition = exact rows     →  STOP as ensemble channel (this document)
IF C5 continues                    →  only with a different NAMED base partition
                                      that can emit without ε-thresholds
```

The only threshold-free base rules already on the table that can partition when all rows are
distinct are:

1. **Named spectral sign bipartition** (uses geometry of `A`, not equality of rows)
2. Equitable refinement (still often trivial/all-singletons on generic weighted complete graphs)
3. Max-weight support components (often one big component or dust)

C5.2b names (1) completely and adjudicates emission plausibility.  
(2) and (3) are secondary and are not adopted in Path A “vamos con todo” unless spectral fails closure.

---

## 8. Terminal

```text
C5_2_RESULT = EXACT_ROW_PHI_STAR_ENSEMBLE_REJECTED
DEATH_MODE = CHRONIC_ABSTAIN_OVERREFINED
FORMAL_MAP_RETAINED_AS_DIAGNOSTIC_ONLY
NEXT = C5_2B_NAMED_SPECTRAL_SUCCESSOR
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SEEDS
NO_RECONSTRUCTION_CLAIM
```
