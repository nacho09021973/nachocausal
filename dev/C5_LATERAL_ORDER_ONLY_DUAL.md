# C5 — Order-only dual for side walls (lateral S4)

STATUS: THEORETICAL_ARGUMENT_ONLY / NOT_A_CANDIDATE / CANDIDATE_5_NOT_YET_OPENED  
NO_IMPLEMENTATION / NO_SYNTHETIC_EXECUTION / NO_SEEDS / NO_FREEZE / NO_RECONSTRUCTION_CLAIM  
DATE: 2026-07-20

BINDS_TO:

- `dev/C5_NAMED_MAP_PHI_STAR.md` (Φ★ has roof peel, no lateral control)
- `dev/C5_NONCOLLAPSE_A_VS_MARGINAL_V.md`
- `dev/C5_ORDER_ONLY_THRESHOLD_FREE_MAP_EXISTENCE.md`
- Decision 040 §5, §9 (lateral truncation as mandatory falsifier)
- Decision 039 (no intrinsic neighbor graph on minimals)
- Claim grammar §3 (finite patch ≠ global horizon)

This note answers option (2) from the C5 continuation fork:

> Is there an order-only, threshold-free dual of Φ★’s maximal peel that plays the same role for
> **side walls** that `peel(C) = C \ Max(C)` plays for the **roof**?

---

## 0. Verdict first

```text
CANONICAL_INTERNAL_SIDE_PEEL_DUAL_TO_MAX     = NO     [PROVED as non-existence of embedding-faithful dual]
PARTIAL_ORDER_ONLY_LATERAL_PROXIES            = YES    [named below; none equals Max-peel]
S4_SIDE_COMPLETION_FOR_PHI_STAR               = GENERATIVE / EXTERNAL  [honest locus]
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SEEDS
```

The asymmetry is not a failure of imagination. It is structural: **the roof is order-theoretic;
side walls of a continuum box are not.**

---

## 1. What the roof dual is, precisely

### 1.1 Why `Max` works

On a finite poset `C = (E, ≺)`:

```text
Max(C) := { x ∈ E | ∄ y with x ≺ y }
```

is:

1. defined from `≺` alone;
2. unique (as a set);
3. relabel-invariant: `Max(σ·C) = σ(Max(C))`;
4. functorial under order embeddings that preserve maximality in the obvious way;
5. operationally a **single** layer deletion with no free parameter.

Φ★ uses one application:

```text
C' = peel(C) := C without Max(C)
require Π_row(A(C)) = Π_row(A(C'))
```

Physically, in a Poisson sprinkling of a region with a smooth future boundary, `Max(C)` concentrates
near that future boundary (the “roof” of the box). So the order operation tracks a continuum
boundary component that is **timelike-transverse / future-facing**.

### 1.2 What a side dual would need to be

A true dual `side(C)` would need all of:

| Requirement | Meaning |
|---|---|
| D1 | Function of the finite poset alone |
| D2 | No calibrable threshold / no coordinates |
| D3 | Relabel-invariant |
| D4 | Closed ties (unique set, or abstention) |
| D5 | **Embedding fidelity:** when `C` arises as a sprinkling of a continuum box with spatial walls `∂_side R`, the set `side(C)` (or the deleted layer) concentrates on those walls in the continuum limit, not on the roof/floor alone |
| D6 | Operational use: a peel or stability test internal to a map like Φ★ |

Φ★’s roof control uses D1–D4 + a soft version of D5 for the future boundary.  
The question is whether anything satisfies D1–D6 for **spatial** walls.

---

## 2. Non-existence of an embedding-faithful side peel — [PROVED in spirit]

### 2.1 Embedding ambiguity

The same abstract finite poset can be realized (approximately) by sprinklings of continuum regions
with **different** spatial boundary shapes, or by regions with **no** distinguished side walls
(e.g. a causal diamond / Alexandrov interval whose entire boundary is null-related to the
extremal points).

More sharply, at the combinatorial level:

**Lemma (side walls are not poset invariants).**  
There is no map

```text
Σ : {finite posets} → {subsets of the ground set}
```

such that, for every continuum region `R` with a well-defined spatial wall set `∂_side R` and every
high-density sprinkling `C ⊂ R`, one has `Σ(C)` concentrated on `∂_side R`, **and** `Σ` depends
only on the isomorphism type of `(C, ≺)`, while also agreeing with the intended walls for all
isometric embeddings of the same point set into regions with rotated or deformed walls.

**Reason.** “Side wall” is defined by the embedding `(C ↪ R, g)`, not by `(C, ≺)`. Any two
embeddings that induce the same causal order on the point set but place the continuum boundary
differently relative to continuum coordinates will demand different `∂_side` sets while leaving
`≺` fixed. A function of `≺` alone cannot track both.

Even without exotic re-embeddings: pure order-isomorphic copies of a causet cannot know which
direction was “x” vs “t” in the chart. Spatial walls are chart-dependent decorations.

**Label.** This is a structural observation about invariants, not a measure-theoretic theorem about
Poisson processes. It is enough to kill the hope of a Max-like **canonical** side layer.

### 2.2 Contrast table

| Boundary | Continuum locus | Order image | Canonical? |
|---|---|---|---|
| Future roof | future boundary of `R` | `Max(C)` (approx.) | **Yes** |
| Past floor | past boundary of `R` | `Min(C)` (approx.) | **Yes** |
| Spatial side walls | lateral boundary of `R` | **none canonical** | **No** |
| Null boundary of diamond | ∂(Alexandrov) | mixed min/max structure | partial, not “side” |

`Min` is canonical but it is Φ★’s **index set**, not something one peels without destroying the
object. The past dual of roof is real; it is not lateral.

### 2.3 Why height levels are not side walls

Mirsky rank

```text
h(x) = length of longest chain ending at x
Σ_ℓ = { x | h(x) = ℓ }
```

is order-only and canonical. Deleting `Σ_ℓ` removes a **temporal** (or rank) slice — a spacelike
antichain layer in manifoldlike regimes — not a vertical wall. That is the dual of a **foliation**,
not of a side boundary.

Using a free `ℓ` reintroduces a calibrable choice. Using all `ℓ` is a trajectory object (Decision
040 family C), not a side peel.

---

## 3. Attempted duals — adjudicated

Only constructions that are order-only and threshold-free are considered. None is adopted into Φ★
by this note.

### 3.1 Order opposite `C^op`

```text
x ≺^op y  ⇔  y ≺ x
Max(C^op) = Min(C),   Min(C^op) = Max(C)
```

Peeling `Max(C^op)` peels the **floor**, not the sides.  
**State:** real dual of roof; **not lateral.**  
**Use:** a floor-stability variant of Φ★ could require stability after adjoining a formal past
layer — usually unavailable in the observed patch (no exterior past; Decision 040 restriction 6).

### 3.2 Past common matrix on maximals

```text
N := Max(C)
B_ab := |J⁻(a) ∩ J⁻(b)|    (a,b ∈ N)
```

Row partition of maximals by common **pasts**.  
**State:** order-only dual object in time-reversed sense; probes **past** reconvergence toward the
floor/roof interface, not spatial walls.  
**Threat:** still boundary-dominated by bottom walls.  
**Not a side dual.**

### 3.3 Roof-supported overlap (already near Φ★)

```text
A^Max_ij := | J⁺(i) ∩ J⁺(j) ∩ Max(C) |
```

Partition by rows of `A^Max`. If `Π_row(A) = Π_row(A^Max)`, the pattern is carried entirely by the
maximal layer — a roof diagnostic closely related to peel instability.  
**State:** useful **roof** probe; not lateral.

### 3.4 Maximum antichain deletion

Delete a maximum-cardinality antichain `W`.  
**Blockers:**

- `W` is not unique in general → D4 fails unless one abstains on non-uniqueness;
- finding maximum antichains is global and expensive;
- when unique, `W` is a widest spacelike cut, typically **bulk or mid-height**, not a side wall.

**State:** `REJECTED` as side dual; optional fragility test only if uniqueness is forced to abstain.

### 3.5 Incomparability counts / “spatial degree”

For each `x`, `ι(x) = |{y : x ∥ y}|`. High incomparability is a bulk spacelike-degree proxy, not a
wall marker; walls often **reduce** available spacelike partners. Thresholding `ι` is calibration.  
**State:** `REJECTED` for closed side peel.

### 3.6 Neighbor graphs on minimals (Rideout–Wallden, Boguñá–Krioukov)

Decision 039 already: no admissible order-only `E_M` for the C4 design.  
Even if a spatial predistance existed, “delete boundary of the neighbor graph” would need a graph
boundary definition and would smuggle the unresolved `E_M` problem into Φ★.  
**State:** `BLOCKED` by Decision 039; not reopened here.

### 3.7 1+1D 2-order left/right (dimension-specific)

In 1+1D, manifoldlike causets are related to 2-orders (intersection of two total orders). Extremal
elements in the two linear realisers correspond roughly to “left” and “right” boundaries of a
box.

**State:**

- interesting for `SQUARE_BOX` 1+1D;
- **not** a general C5 dual (fails in 3+1D; realisers not unique; choosing a realiser is not
  forced by the poset alone without extra structure);
- using it would **reclassify** the lateral control as dimension-locked, not as a universal
  order-only dual to `Max`.

**Not adopted** as the C5 side dual.

### 3.8 ε-neighborhoods of equal rows / soft clustering

Would restore robustness under Poisson noise and might glue wall-adjacent minimals — but **ε is a
calibrated threshold**, forbidden by the present discipline.  
**State:** `REJECTED_REQUIRES_CALIBRATED_THRESHOLD`.

---

## 4. What *can* be named: a lateral control package (not a peel)

Since no Max-like `side(C)` exists, lateral discipline must be stated as a **control package**
with two layers: weak internal diagnostics, and strong generative falsifiers.

### 4.1 Internal diagnostics (order-only, optional, not peel-equivalent)

These may be computed alongside Φ★ in a future design; they do **not** repair S4 by themselves.

| ID | Diagnostic | Pass / fail idea |
|---|---|---|
| L-int-1 | Roof-supported agreement: `Π_row(A)` vs `Π_row(A^Max)` | agreement ⇒ roof-carried pattern (kill / abstain) |
| L-int-2 | One maximal peel (already in Φ★) | instability ⇒ roof |
| L-int-3 | Exact automorphism symmetry of `A` | total symmetry ⇒ abstain (already) |
| L-int-4 | Past dual on `Max` (matrix `B`) emits a partition while Φ★ emits on `Min` | descriptive only; no automatic kill rule without overclaim |

None of L-int-1…4 is a side wall detector. They tighten **roof/symmetry** discipline only.

### 4.2 Generative lateral suite — the real S4_side — [MANDATORY for any future physics claim]

These are **not** functions of a single observed poset alone. They are comparisons across
generative interventions, exactly as Decision 040 already required. Restated for Φ★:

```text
LAT-1  Symmetric lateral truncation synthetic
       Same bulk rule, add/remove only spatial walls (continuum or discrete surrogate).
       If Φ★ emission pattern matches the wall-only construction → REJECTED_SIDE_WALL_DOMINATED.

LAT-2  MINK same-cloud
       Same point set, flat causal relation.
       If Φ★(C_MINK) reproduces Φ★(C_BH) pattern up to the design’s equivalence
       → REJECTED_BOX_OR_GLOBAL_GEOMETRY.

LAT-3  Density lobe synthetic
       Inhomogeneous intensity without horizon.
       If Φ★ lights up the lobe → REJECTED_DENSITY_DOMINATED.

LAT-4  Height-domain / roof translation
       Shift the temporal window.
       If the partition merely tracks the new roof/walls → REJECTED_BOUNDARY_TRACKING.

LAT-5  Pure spatial-wall poset
       Order generated so that only lateral truncation creates reconvergence asymmetry.
       Φ★ must abstain or be labelled wall-dominated, not “detection”.
```

**Key point:** LAT-1…5 live in the **experimental design**, not inside `Φ★(C)`.  
That is not a philosophical dodge. It is the only place side walls exist as controlled variables.

### 4.3 Named completion of S4 for the Φ★ *program line* (not a new map)

Define the **claim envelope** `Env(Φ★)`:

```text
Env(Φ★) := Φ★
        + roof peel internal (already in Φ★)
        + generative suite LAT-1…5 + Decision 040 roof/MINK/density/height controls
        + non-collapse posture from C5_NONCOLLAPSE note (C-ens still OPEN)
```

Then:

```text
Φ★           formally closed map
Env(Φ★)      only honest locus of a future physical claim
S4_side      ∈ Env(Φ★) \ Φ★
```

No object `Φ★_side` is defined as a poset endomap that “peels walls”.

---

## 5. Why this is the frontier answer, not a cop-out

At the edge of order-only continuum reconstruction:

1. **Time-asymmetric boundaries** (past/future) are aligned with the order relation itself.  
2. **Space-asymmetric boundaries** are orthogonal to `≺`; the order sees them only through
   *indirect* distortions of futures and pasts.  
3. Those distortions are real (they affect `A`), but they are **entangled** with density, roof,
   depth, and geometry — which is why C3 looked edge-dominated and why C4 wanted a neighbor graph
   it could not have.  
4. Demanding an internal side peel with the same cleanliness as `Max` is demanding that the poset
   forget it does not know the embedding. It cannot.

Talent here is refusing a fake dual.

---

## 6. Consequences for Φ★ and C5

| Item | Status after this note |
|---|---|
| Φ★ definition | unchanged |
| Internal S4 roof | still yes |
| Internal S4 side | **impossible in Max-like form** |
| Path to any future candidate using Φ★ | must treat LAT-1…5 (and Dec. 040 suite) as **definitional for the claim**, not as optional afterthought |
| Temptation to import `E_M` as side dual | **forbidden** by Decision 039 |
| Temptation to use ε-clustering for wall blocks | **forbidden** as calibrated threshold |
| `CANDIDATE_5` | still not opened |

### Sharp restatement of the scientific fork

```text
Either:
  (A) accept that lateral control is generative/external,
      and design Env(Φ★) accordingly before any seed; or
  (B) abandon partition-of-minimals-from-A as a localization channel
      if a purely internal S4_side is required as a matter of principle.
```

There is no option (C) “find the clever side peel we missed” under D1–D6 as stated.  
If someone proposes a new `Σ(C)`, it must be checked against §2.1 and Decision 039; the default
prior is failure.

---

## 7. Optional research directions that are *not* side peels

Listed so they are not confused with a solution:

1. **Partition-valued continuum limit of overlap kernels** (Boguñá–Krioukov-type) — spatial geometry
   from overlaps, still not wall deletion.  
2. **1+1D 2-order boundary markers** — dimension-locked diagnostic.  
3. **Equitable refinement robustness studies** — noise, not walls.  
4. **Multi-peel roof towers** — stronger roof, zero side.

---

## 8. Terminal

```text
LATERAL_ORDER_ONLY_DUAL_RESULT = NO_CANONICAL_SIDE_PEEL
ROOF_DUAL = Max_PEEL   [exists, already in Φ★]
FLOOR_DUAL = Min       [exists, is index set / past dual, not lateral]
SIDE_WALL_CONTROL = GENERATIVE_SUITE_LAT_1_TO_5
PHI_STAR_UNCHANGED
ENV_PHI_STAR = PHI_STAR + GENERATIVE_BOUNDARY_SUITE
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
NO_FREEZE
NO_RECONSTRUCTION_CLAIM
```

---

## 9. One-sentence verdict

**There is no order-only Max-like peel for side walls — because side walls are embedding data, not poset data — so lateral S4 cannot live inside Φ★ and must live in a generative control envelope; anything that pretends otherwise is smuggling coordinates or thresholds under another name.**
