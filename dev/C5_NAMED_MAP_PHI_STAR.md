# C5 — Named map instance Φ★ (order-only, threshold-free)

STATUS: CONCEPT_DEFINITION_ONLY / NOT_A_CANDIDATE / CANDIDATE_5_NOT_YET_OPENED  
NO_IMPLEMENTATION / NO_SYNTHETIC_EXECUTION / NO_SEEDS / NO_FREEZE  
DATE: 2026-07-20

BINDS_TO:

- Decision 040 `docs/comite/comite_decision_040_c5-search-space-adjudication.md` (`d5759e6`)
- Decision 041 `docs/comite/comite_decision_041_c5-1-matrix-to-block-map-adjudication.md` (`bb3d1a7`)
- Existence note `dev/C5_ORDER_ONLY_THRESHOLD_FREE_MAP_EXISTENCE.md`
- C4 concept (blocked) `dev/PR003_C4_COMMON_FUTURE_CONVERGENCE_NOTES.md`
- Claim grammar `docs/claim_grammar.md` (teleology of global horizon; no reconstruction claim)

This document **names one complete map**. It does not open `CANDIDATE_5`, does not freeze an
observable, does not authorize code, seeds, synthetics, or runs, and does not claim horizon
detection.

```text
OBJECT_CLASS = named order-only map Φ★
NOT = CANDIDATE_5
NOT = frozen estimator
NOT = preregistration
```

---

## 0. Why this step is hard (and why it matters)

Causal-set recovery of horizon-adjacent structure from a **finite** partial order sits at a real
limit of the program and of the physics:

1. The global event horizon is teleological: it depends on the continuation of spacetime beyond the
   observed patch (`docs/claim_grammar.md` §3). A finite order cannot identify that global object.
2. Marginal future statistics on minimals (`L`, `V`) already showed edge-dominated, inconclusive
   localization in the third localizer development line (C3 / truncated futures).
3. Pairwise common futures are genuinely non-marginal (C4 toy separation), but C4 died on the
   absence of an intrinsic neighbor graph `E_M`.
4. Decision 040 kept the full common-future **matrix** as the only surviving search family.
5. Decision 041 showed that unfinished map *families* do not close S1–S4.
6. The existence note showed: pure `f(A)` cannot carry physical boundary control; the domain must
   be the **poset**.

What remains is not a recipe. It is to write a map so completely that every free choice is gone,
then ask — still without data — what physical proposition it could even state.

---

## 1. Ontological commitment

Φ★ is a map

```text
Φ★ : { finite posets C }  →  { unordered partitions of Min(C) }  ∪  { named abstentions }
```

It is **not** a real-valued score, not a single preferred minimal, and not a reconstruction of
`r = R_S`.

**Physical reading (motivation only, not a claim):**  
Minimals are the past-most antichain of the observed patch. The common-future matrix records how
their futures reconverge inside the patch. A stable partition of that antichain is a discrete
statement about **relational future-fingerprint clusters** among past-most events. Whether those
clusters track anything quasi-local about trapping / expansion / horizon-adjacent structure is
`OPEN`. Whether they track box walls is the main threat.

**Forbidden reading:**

```text
NO_RECONSTRUCTION_CLAIM
NO_GLOBAL_HORIZON_IDENTIFICATION
NO_METRIC_RECOVERY
```

---

## 2. Fixed primitives (every symbol named)

Let `C = (E, ≺)` be a finite strict partial order (the observed causet / poset).

### 2.1 Order primitives

```text
Min(C)  := { x ∈ E | ∄ y ∈ E with y ≺ x }
Max(C)  := { x ∈ E | ∄ y ∈ E with x ≺ y }
J⁺_C(x) := { y ∈ E | x ≺ y }                    # strict future; x ∉ J⁺(x)
peel(C) := (E \ Max(C), ≺ restricted)           # delete one maximal layer only
```

If `E \ Max(C) = ∅`, peel is the empty poset.

### 2.2 Common-future matrix (no free normalization)

Index set:

```text
M := Min(C)
m := |M|
```

Matrix (integer, symmetric, order-only):

```text
A(C) ∈ ℕ^{M×M},
A(C)_{ij} := | J⁺_C(i) ∩ J⁺_C(j) |     for all i,j ∈ M
```

Diagonal entries are `|J⁺_C(i)|` (future volumes of minimals). Off-diagonal entries are raw
pairwise common-future cardinalities. **No** residualization against hypergeometric means, **no**
row normalization, **no** rank transform, **no** kernel width. Those are free choices; they are
excluded from Φ★.

Relabeling contract: for any bijection `σ` of `E` that is an order automorphism of labels only
(permutation of element names),

```text
A(σ·C)_{σ(i)σ(j)} = A(C)_{ij}.
```

### 2.3 Base partition rule: exact row equivalence

Among threshold-free partitions, the most rigid and least ambiguous is **exact row equality**.

Define the off-diagonal row signature of `i ∈ M` by the multiset of pairs, or equivalently the
function

```text
ρ_C(i) : M \ {i} → ℕ,
ρ_C(i)(j) := A(C)_{ij}.
```

Because `A` is symmetric with fixed diagonal convention, two minimals `i ∼_C j` iff

```text
A(C)_{ik} = A(C)_{jk}  for all k ∈ M
```

(including `k = i,j` via symmetry and diagonal). This is equality of full rows of `A(C)` after
any fixed ordering is discarded: it is equality of functions on the labeled index set, and the
induced partition is label-covariant.

Equivalence classes:

```text
Π_row(A(C)) := M / ∼_C
```

as an **unordered** set of nonempty blocks.

**Why not equitable refinement or Laplacian for Φ★?**  
They remain legitimate alternatives, but each adds machinery (iterated color updates; real
eigenanalysis and multiplicity). For the first fully named instance, exact rows minimize open
implementation semantics and maximize exact-arithmetic closure. Equitable refinement is a
documented optional strengthening in §8; it is not part of Φ★.

### 2.4 Discrete emission floors (fixed constants, not calibration)

The following integers are part of the definition, chosen once, not fit to data:

```text
m_min      := 4     # need enough minimals for a nontrivial multi-block pattern
cell_min   := 2     # no singleton cells in an emitted partition
```

These are design constants of the same kind as “remove exactly one maximal layer”. They are not
seed-tuned thresholds.

---

## 3. Definition of Φ★

### 3.1 Terminal alphabet

```text
EMIT(P)                         # P unordered partition of M
ABSTAIN_TOO_FEW_MINIMALS
ABSTAIN_EMPTY_OR_DEGENERATE_POSET
ABSTAIN_TRIVIAL_PARTITION       # one cell
ABSTAIN_OVERREFINED             # any singleton cell, or all singletons
ABSTAIN_PEEL_UNDEFINED          # peel empty or Min changes
ABSTAIN_ROOF_UNSTABLE           # partition changes under one maximal peel
ABSTAIN_MATRIX_CONTRACT         # reserved if A were ill-formed (should not occur for finite C)
```

### 3.2 Algorithm (definitional, not code)

Input: finite poset `C`.

1. If `E = ∅` or `M = ∅` → `ABSTAIN_EMPTY_OR_DEGENERATE_POSET`.
2. If `m < m_min` → `ABSTAIN_TOO_FEW_MINIMALS`.
3. Compute `A ← A(C)`, `P ← Π_row(A)`.
4. If `|P| = 1` → `ABSTAIN_TRIVIAL_PARTITION`.
5. If some block `B ∈ P` has `|B| < cell_min` → `ABSTAIN_OVERREFINED`.
6. Let `C' ← peel(C)`.  
   - If `C'` is empty → `ABSTAIN_PEEL_UNDEFINED`.  
   - Let `M' ← Min(C')`. If `M' ≠ M` → `ABSTAIN_PEEL_UNDEFINED`.  
     (For a finite poset that is not an antichain, deleting maximals does not create new minimals
     and does not remove old ones; if this fails, the input is outside the intended class.)
7. Compute `A' ← A(C')` on the same index set `M`, `P' ← Π_row(A')`.
8. If `P' ≠ P` as partitions of `M` → `ABSTAIN_ROOF_UNSTABLE`.
9. Else → `EMIT(P)`.

Output on success: an unordered partition `P = {B_1, …, B_k}` with `k ≥ 2`, each `|B_r| ≥ 2`,
stable under one maximal peel, derived only from raw common-future cardinalities.

### 3.3 Relabeling

For any order-isomorphism `σ` (permutation of labels),

```text
Φ★(σ·C) = σ · Φ★(C)
```

with the natural action on partitions and identical abstention names. No step uses an enumeration
order of `M`.

### 3.4 What Φ★ deliberately does **not** do

- Does not pick a “winning” block.
- Does not score blocks by size, anomaly, or edge distance.
- Does not use coordinates, `r`, `t`, `R_S`, `d_edge`, kind labels, or exterior past.
- Does not require a neighbor graph `E_M`.
- Does not residualize against `L,V` (non-marginality is left as a **property to test later**, not
  baked into an unfixed normalizer).
- Does not claim the partition is horizon-related.

---

## 4. Checklist against Decision 041 criteria

| ID | Requirement | Φ★ |
|---|---|---|
| Order-only | finite ≺ only | **Yes** |
| No free threshold | no cut height / k / learned rank | **Yes** (only fixed `m_min`, `cell_min`, one peel) |
| Deterministic | single output | **Yes** |
| Relabel-invariant | conjugacy of partitions | **Yes** |
| S1 nontrivial when emits | ≥2 cells, no singletons | **Yes when EMIT** |
| S2 closed ties | row equality exact; no label order; full partition output | **Yes** |
| S3 degeneracy abstention | named terminals §3.1 | **Yes** |
| S4 symmetry | total symmetry → typically one cell → abstain trivial; multi-block automorphism does not force a single preferred cell because none is chosen | **Yes for emission-as-partition** |
| S4 roof | peel stability internal | **Yes (one layer)** |
| S4 side wall | | **No — not internal** (see `dev/C5_LATERAL_ORDER_ONLY_DUAL.md`: no Max-like dual exists) |
| S4 density / MINK | | **No — not internal** (generative envelope) |
| Horizon physics | | **OPEN / not claimed** |

So Φ★ is a **closed formal map** for:

```text
S1 ∧ S2 ∧ S3 ∧ S4_symmetry ∧ S4_roof-one-peel
```

It is **not** a closed answer to Decision 040’s full boundary suite and not a localizer.
Lateral S4 lives in `Env(Φ★)` (generative suite LAT-1…5), not inside `Φ★(C)`.

---

## 5. Physical content — what proposition could Φ★ even state?

### 5.1 The only proposition shape that is honest

After claim grammar, the admissible shape is roughly:

```text
TARGET / OPEN:
In a fixed generative family G (e.g. sprinklings of a finite chart of Schwarzschild vs Minkowski
in a fixed box class), dimension d, patch P, channel order-only:
does Φ★ emit more often / emit partitions with systematic post-selection geometry
under embedding-only scoring, compared to controls,
without identifying the global event horizon?
NO_RECONSTRUCTION_CLAIM.
```

That proposition is **not** tested here. It is the only kind of proposition Φ★ could support
later.

### 5.2 What the mathematics is sensitive to

`A_ij = |J⁺(i) ∩ J⁺(j)|` grows when two minimals share many common descendants in the **observed**
patch. Mechanisms that can create or destroy that pattern include:

| Mechanism | Effect on A / Π_row | Peel stability |
|---|---|---|
| Global roof (top box wall) | Shared max-layer funnel can equalize many rows | Often **unstable** under peel → Φ★ abstains (by design) |
| Persistent bulk reconvergence | Shared future structure below the roof | May be **stable** under one peel |
| Side walls | Preferential coalescence of futures along walls | Not killed by top peel → **threat** |
| Density lobe | Locally denser future cones | Not killed by top peel → **threat** |
| Horizon-adjacent truncation (C3 physics) | Marginals `L,V` already edge-sensitive; overlaps may add relational pattern | Unknown whether row-classes stabilize |
| Pure Minkowski same cloud | Different causal relation, different A | Control remains external until defined as dual construction |

### 5.3 Non-marginality (relation to C3/C4)

C4 showed, on a finite toy, that pairwise overlaps are not functions of the pair of marginal
volumes alone. Φ★ uses the full matrix of overlaps, so it is **not definitionally** a function of
the list `{V(i)}` alone. It could still be empirically redundant with ranks of `L,V` on a given
ensemble — that is an empirical/synthetic question **not authorized here**.

If later work ever shows that `Π_row(A)` is a.s. determined by sorting `V(i)` on the design
family, Φ★ dies as a non-marginal object for that family — without needing a horizon claim.

### 5.4 Why full partition, not a single block

C5 wanted “a region”. Physics often wants “the horizon-adjacent set”. Those are not the same.

Emitting a single block requires a closed selector on cells of `P` (largest, highest internal
overlap, …). Every natural selector either:

- reintroduces a free criterion, or  
- is determined by a quantity that may re-collapse to marginals, or  
- breaks under automorphisms that swap two equally large cells.

Φ★ therefore stops at the **partition**. A later theory might interpret a bipartition as
“two relational sectors of the initial antichain”. Promoting one cell to “the” region is a
**separate** definitional act and is **not** done here.

This is not timidity. At the present edge of the subject, overclaiming a single cell is how
programs launder an extra degree of freedom into a “detection”.

### 5.5 Quantum / continuum caution

Even if Φ★ emitted stably on classical sprinklings, that would not be a quantum-gravity theorem.
It would be a statement about Poisson sprinklings (or another generative class) of continuum
geometries, i.e. a semiclassical diagnostic on causet approximations. The program’s own stance
(`CREDIBLE_ONLY_AS_SEMICLASSICAL_PROGRAM` in earlier C1 trail language) remains in force. Φ★ does
not cross that barrier.

---

## 6. What is still missing for any future candidate path

Do **not** read this section as an authorization checklist to implement. It is a map of the
remaining **conceptual** debt.

### 6.1 Internal S4 debt (order-only duals not yet named)

| Gap | Why peel is not enough | Possible order-only direction (unnamed, unadopted) |
|---|---|---|
| Side walls | Max-layer peel is temporal-top, not lateral | Dual constructions using co-ideals, fixed height windows, or stability under deletion of a canonical co-maximal layer — all need full naming without coordinates |
| Density | Overlaps track count measure | Compare Φ★ on order alone cannot see intensity; generative controls are ensemble-level, not internal to Φ★ |
| MINK same-cloud | Requires a second causality on the same point set | Not a function of one poset; lives in the experimental design, not in Φ★ |
| Height-domain translation | Structure that tracks only absolute depth | Vary generative height; again ensemble design |

Honest split:

```text
Φ★  = closed map with roof-stability and partition emission
FULL_C5_BOUNDARY_SUITE = Φ★ + external generative controls (as in Decision 040 §9)
```

Decision 040 already required those controls before seeds. Φ★ does not absorb them all.

### 6.2 Definitional debt if someone wants a single region

- Closed cell selector, or a proof that |P|=2 always when EMIT on the design family (unlikely).
- Or change the scientific output to “partition-valued observable” permanently.

### 6.3 Empirical debt (explicitly not started)

- Synthetic roof-only posets: expect `ABSTAIN_ROOF_UNSTABLE` or trivial partition.
- Same `{V(i)}`, different overlaps: expect different `P` when EMIT.
- Relabeling: exact conjugacy.
- No seeds, no generators, no code in this document.

### 6.4 Candidate debt

```text
CANDIDATE_5_NOT_YET_OPENED
```

Opening a candidate would require at least: frozen text, falsifier suite, claim boundary, seed
policy, and committee/user authorization. Φ★ is none of those.

---

## 7. Comparison: Φ★ vs earlier dead ends

| Line | Object | Death / limit | Φ★ relation |
|---|---|---|---|
| C3 | marginal `L,V` ranks on minimals | edge-dominated, inconclusive localization | uses joint futures, not ranks of L,V |
| C4 | conditioned overlap on neighbor edges | `E_M` unresolved | uses all pairs; no `E_M` |
| C5 family | matrix / profile | map bottleneck | supplies one named map |
| C5.1 families | incomplete exact/spectral/hierarchical | S1–S4 simultaneous fail as families | Φ★ is a **completed instance** of exact rows + peel, not a revival of incomplete spectral |
| Pure `f(A)` | matrix only | cannot do S4 roof | Φ★ domain is the poset |

---

## 8. Optional strengthenings (not part of Φ★)

Documented so they are not silently mixed in later:

1. **Equitable refinement** instead of exact rows: finer; still threshold-free; more computation;
   same peel wrapper.
2. **Named Laplacian bipartition** instead of row classes: emits at most two blocks; needs exact
   or certified arithmetic policy for eigenvalues; abstain on multiplicity/zeros.
3. **Residual matrix** `A_ij − hypergeometric mean(V_i,V_j,|F|)`: improves non-marginality
   optics but introduces a model for the ambient future set `F`; not free of modeling choice;
   excluded from Φ★.
4. **Multi-peel stability** (`peel^k` for fixed k>1): stronger roof control; `k` must stay a fixed
   design constant, not tuned.

None of (1)–(4) is authorized for implementation by this note.

---

## 9. Decision-like terminal for this definition

```text
NAMED_MAP_INSTANCE = PHI_STAR
PHI_STAR_STATUS = FORMALLY_CLOSED_MAP
PHI_STAR_OUTPUT = UNORDERED_PARTITION_OR_ABSTENTION
PHI_STAR_S1_S2_S3 = YES
PHI_STAR_S4_ROOF_ONE_PEEL = YES
PHI_STAR_S4_SIDE_DENSITY_MINK = NO_NOT_INTERNAL
PHI_STAR_HORIZON_PHYSICS = OPEN_NOT_CLAIMED
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
NO_FREEZE
NO_RECONSTRUCTION_CLAIM
```

---

## 10. The sharp question left (for when you return)

Not “how do we code this”. Not “which library for eigenvectors”.

**Partial answer on marginal volumes:** see `dev/C5_NONCOLLAPSE_A_VS_MARGINAL_V.md`.
Definitional collapse of `A` / `Π_row(A)` onto `{V(i)}` is **false** on finite posets
`[PROVED]`. Ensemble collapse on boxed Schwarzschild (`C-ens`) remains `OPEN`. Brittleness of
exact row equality under Poisson noise is a separate death mode.

The remaining sharp question is:

> Even though overlaps are not algebraically functions of volumes, is there a continuum/causal-set
> reason to expect **peel-stable row-classes of raw common-future overlaps among minimals** to
> carry quasi-local information beyond walls and density — or does Φ★ almost always abstain
> (exact-row brittleness) or emit only box-dominated structure on the geometries we care about?

Until that has a theoretical argument or a later authorized falsifier design, talent means
**holding the line**:

```text
we have a named map;
we do not have a candidate;
we do not pretend the horizon is in the finite order.
```

---

## 11. One-sentence summary

**Φ★** is the first fully named, order-only, threshold-free map from a finite poset to a peel-stable
nontrivial partition of minimals by exact common-future row equality — closed enough to exist as
mathematics, not closed enough to be physics, and not opened as `CANDIDATE_5`.
