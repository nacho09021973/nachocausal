# Comite Decision 041 - C5.1 matrix-to-block map adjudication

STATUS: C5_1_MATRIX_TO_BLOCK_MAP_ADJUDICATION / CANDIDATE_5_NOT_YET_OPENED / NO_IMPLEMENTATION / NO_SYNTHETIC_EXECUTION / NO_SEEDS
DATE: 2026-07-20

This is a documentary adjudication only. It does not open `CANDIDATE_5`, implement a matrix,
construct synthetic posets, allocate seeds, modify any frozen contract, or authorize any run.

## 1. Question

The only admissible question is whether there exists a closed map of the shape

```text
common-future matrix  -->  block / subset / partition  or  abstention
```

that is simultaneously:

1. deterministic;
2. order-only (finite partial order only);
3. exactly relabel-invariant under conjugation of the matrix index set;
4. free of coordinates, `r`, `t`, `R_S`, wall distances, seed labels, kind labels, and exterior past;
5. free of a neighbor graph `E_M`;
6. free of calibrated thresholds, chosen `k`, learned rank, or post-seed tuning.

The input object is the C5 surviving family from Decision 040:

```text
GLOBAL_COMMON_FUTURE_MATRIX_PROFILE
```

No score-to-horizon interpretation is made here. No localization claim is made here.

## 2. State of entry

```text
C5_1_MATRIX_TO_BLOCK_MAP_ADJUDICATION_AUTHORIZED
C5_SEARCH_SPACE_NARROWED
C5_SURVIVING_FAMILY=GLOBAL_COMMON_FUTURE_MATRIX_PROFILE
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
```

Binding source:
`docs/comite/comite_decision_040_c5-search-space-adjudication.md` at commit
`d5759e626150cfbffc25cb058e6d6cfa4e2d9071`.

Decision 040 established only a surviving object family, not a localizer. Its unresolved
bottleneck is exactly the map adjudicated here:

```text
common-future matrix -> relabel-invariant localized subset/block/abstention
```

## 3. Admissible comparison set

Only three map families are compared. No others are admitted in this brief.

1. **Exact equivalence or equitable refinement** of rows / weighted color classes of the matrix.
2. **Canonical spectral partition** of a self-adjoint operator derived from the matrix.
3. **Hierarchical partition** only if it is completely defined without any calibrable threshold.

Families that require neighbor graphs, single-minimal scalar selectors, coordinate scoring, or
post-hoc cut levels are outside the comparison set.

## 4. Simultaneous success criteria

A family **passes** C5.1 only if it provides **all four** of the following at once, as a closed
definition, not as a future research promise:

| ID | Requirement | Meaning for a closed map |
|---|---|---|
| S1 | Nontrivial partition when it emits | When the map does not abstain, the output is a partition or block structure that is not the universal one-cell partition and not the all-singletons partition used as a disguised ranking of minimals. |
| S2 | Closed tie-breaks | Every algebraic or combinatorial ambiguity (equal rows, equal merge costs, repeated eigenvalues, sign flip, label order, equal block scores) is resolved by a fixed rule or by mandatory abstention. No input-order or label-order default is allowed. |
| S3 | Abstention under degeneration | Empty or too-small `M`, non-symmetric or nonfinite matrix, exact total symmetry, all-equal rows, non-simple selected spectrum, zero components that break the emission rule, and other listed degeneracies produce named abstention terminals rather than arbitrary outputs. |
| S4 | Direct symmetry / boundary control | The map itself encodes symmetry and boundary discipline: exact exchange symmetry without a distinguished side must abstain or emit a conjugacy-closed object; roof-only / side-wall-only degeneracy classes are not free to emit a preferred physical block without a built-in control. External "write falsifiers later" lists do **not** count as direct control for C5.1. |

### Negative-termination rule

```text
IF no family simultaneously satisfies S1 ∧ S2 ∧ S3 ∧ S4
THEN terminal is negative:
  C5_1_NO_CLOSED_MAP
  CANDIDATE_5_NOT_YET_OPENED
  NO_IMPLEMENTATION
  NO_SYNTHETIC_EXECUTION
  NO_SEEDS
```

A family that is "promising if later closed" fails. A family that needs one extra selector,
threshold, operator choice, or post-hoc falsifier suite to become closed fails S2 or S4.

States used below:

```text
PASS_C5_1
FAIL_S1_NONTRIVIALITY
FAIL_S2_TIEBREAKS
FAIL_S3_DEGENERACY
FAIL_S4_SYMMETRY_BOUNDARY
FAIL_MULTIPLE
REJECTED_REQUIRES_CALIBRATED_THRESHOLD
NOT_COMPLETELY_DEFINED
```

No empirical `PASS` status is used. No synthetic matrix is constructed.

## 5. Input discipline (shared)

Let `M = Min(C)` be the minimal antichain of the observed finite causet. A future implementation
may form a symmetric pair-indexed matrix `A` on `M` from common-future information. This
adjudication does **not** freeze normalization or residualization of `A`.

Shared structural assumptions if a map is ever defined later:

1. rows/columns indexed by elements of `M`;
2. under any relabeling permutation `P`, `A -> P A P^T`;
3. construction of `A` uses only the finite order;
4. coordinates and exterior past are absent from construction and partitioning;
5. the map may not reduce to a function of marginal ranks `{L(i), V(i)}` alone.

Shared pre-map degeneracy terminals (necessary for any family, not sufficient for S3):

```text
NO_MINIMALS_ABSTAIN
TOO_FEW_MINIMALS_FOR_PARTITION_ABSTAIN
MATRIX_NOT_SYMMETRIC_ABSTAIN
MATRIX_NONFINITE_ABSTAIN
MATRIX_RELABELING_CONTRACT_UNSPECIFIED_ABSTAIN
```

## 6. Family A - Exact equivalence or equitable refinement

### Mechanism

Partition `M` by exact row equality of `A` (modulo the diagonal/self-coordinate convention), or by
iterative equitable refinement / color refinement on the weighted complete graph induced by `A`:
two minimals stay in the same color class only if their connection profiles to all current color
classes are identical.

These operations are order-only once `A` is order-only, deterministic, and conjugate under
relabeling when color classes are unlabeled sets.

### Score against S1-S4

| Criterion | Result | Reason |
|---|---|---|
| S1 nontrivial emission | **FAIL** | Generic finite causets produce all-singletons (over-refinement) or a single cell (trivial). Medium multi-cell partitions occur, but the mechanism returns an unordered partition, not a distinguished block/subset. Selecting "largest cell", "most anomalous cell", or any size floor is an extra rule not supplied by exact equivalence. |
| S2 closed ties | **partial** | Exact equality has no numeric threshold. Multi-cell output without a distinguished-block rule is an unresolved emission ambiguity: several blocks, no closed choice of which block (if any) is the map output. |
| S3 degeneracy abstention | **partial** | All-singletons and single-cell can be named as abstentions. Automorphic multi-cell ambiguity without a further rule is not closed as a single block map. |
| S4 direct symmetry/boundary | **FAIL** | The mechanism has no intrinsic roof/side-wall/symmetry control. Exact total exchange symmetry yields one cell or automorphic cells; it does not encode boundary discipline. External synthetic falsifiers are not part of the map. |

Named abstentions that would be needed (still insufficient for S1/S4):

```text
EQUITABLE_ALL_SINGLETONS_ABSTAIN
EQUITABLE_SINGLE_CELL_ABSTAIN
EQUITABLE_NO_DISTINGUISHED_BLOCK_ABSTAIN
EQUITABLE_AUTOMORPHIC_AMBIGUITY_ABSTAIN
EQUITABLE_TOLERANCE_REQUIRED_ABSTAIN
```

### Adjudication

```text
FAMILY_A_STATE=FAIL_MULTIPLE
FAILS=S1,S2,S4
```

Exact/equitable refinement remains a legitimate **diagnostic** and relabeling oracle. It is not a
closed C5.1 map from matrix to block/subset/abstention.

## 7. Family B - Canonical spectral partition

### Mechanism

Conceptually:

```text
matrix A -> self-adjoint operator B(A) -> distinguished eigenspace -> sign pattern -> unordered bipartition {B_-, B_+} or abstention
```

Sign orientation is not part of the output: only the unordered pair of blocks. If a future
operator and simple eigenspace were fixed, eigenvector sign flip would not label-dependently
change the unordered bipartition, and permutation conjugacy would hold when
`B(P A P^T) = P B(A) P^T`.

### Score against S1-S4

| Criterion | Result | Reason |
|---|---|---|
| S1 nontrivial emission | **conditional only** | A simple eigenvector with both signs present can emit a nontrivial bipartition. This is not available as a closed rule today: without a fixed operator and fixed eigen-object, emission is undefined, not nontrivial. |
| S2 closed ties | **FAIL** | The family is incomplete. Unspecified choices include: matrix normalization of `A`; which self-adjoint operator `B(A)`; which eigenvalue/eigenspace; how to treat multiplicity; how to treat exact zero components; numerical vs exact arithmetic. Each unspecified choice is a free parameter or an open tie. Listing `SPECTRAL_*_ABSTAIN` names does not close those choices. |
| S3 degeneracy abstention | **partial, not closed** | Named terminals (non-simple spectrum, zero component, one-sign vector, etc.) are the right *shape*, but they presuppose a fully specified spectral object. An incomplete definition cannot claim closed degeneracy handling. |
| S4 direct symmetry/boundary | **FAIL** | Exact exchange symmetry can be forced to abstain *if* the operator and selection rule are fixed and the rule says so. Boundary/roof/side-wall discipline is not part of the spectral rule itself. Decision-040-style falsifier lists ("top truncation synthetic must reject…") are **external** contracts for a later candidate, not direct control inside the map. C5.1 does not credit them as S4. |

Prospective abstention names (not sufficient while the operator is unspecified):

```text
SPECTRAL_OPERATOR_UNSPECIFIED_ABSTAIN
SPECTRAL_EIGENVALUE_NOT_SIMPLE_ABSTAIN
SPECTRAL_ZERO_COMPONENT_ABSTAIN
SPECTRAL_ONE_SIGN_VECTOR_ABSTAIN
SPECTRAL_BLOCK_TOO_SMALL_ABSTAIN
SPECTRAL_AUTOMORPHISM_AMBIGUITY_ABSTAIN
SPECTRAL_NUMERICAL_STABILITY_UNSPECIFIED_ABSTAIN
```

### Why this is not a positive C5.1 survival

Earlier informal language ("viable for concept development") confuses two levels:

1. **C5.1 (this document):** is there a *closed* map satisfying S1-S4 simultaneously?
2. **Later concept work:** might some spectral construction eventually be closed?

C5.1 answers only (1). An incomplete spectral sketch fails S2 and S4. It therefore fails the
simultaneous criterion. Retaining spectral ideas for optional later theory is not a C5.1 pass and
does **not** open `CANDIDATE_5`.

### Adjudication

```text
FAMILY_B_STATE=FAIL_MULTIPLE
FAILS=S2,S4
NOTE=S1_AND_S3_NOT_CLOSED_WHILE_OPERATOR_UNSPECIFIED
```

## 8. Family C - Hierarchical partition

### Mechanism

Use `A` to build a hierarchy (agglomerative/divisive clustering, dendrogram, ultrametric, repeated
merge/split) and emit one level, one block, or abstention.

### Completeness gate

Hierarchical methods enter the comparison set **only if** completely defined without calibrable
thresholds. Standard forms require at least one of: distance threshold, target cluster count, gap
statistic, linkage plus cut height, size floor/ceiling, stability threshold, or label/order
tie-break among equal merges.

A purely algebraic exception would require, for example, a unique maximal gap in an exact merge
cost spectrum with mandatory abstention on all ties — specified fully, with no disguised
calibration. No such complete definition is present in the repository, and none is introduced
here.

### Score against S1-S4

| Criterion | Result | Reason |
|---|---|---|
| S1 | **not available** | Emission level unspecified. |
| S2 | **FAIL** | Merge ties and cut level are open; label-order resolution is forbidden and not replaced by a closed rule. |
| S3 | **FAIL** | Degeneracy terminals cannot be closed without linkage and cut rules. |
| S4 | **FAIL** | No direct symmetry/boundary control; hierarchical cuts track global scale, not boundary discipline. |

```text
HIERARCHICAL_LINKAGE_UNSPECIFIED_ABSTAIN
HIERARCHICAL_CUT_LEVEL_UNSPECIFIED_ABSTAIN
HIERARCHICAL_TIE_MERGE_AMBIGUITY_ABSTAIN
HIERARCHICAL_LABEL_ORDER_DEPENDENCE_ABSTAIN
HIERARCHICAL_THRESHOLD_REQUIRED_ABSTAIN
HIERARCHICAL_MULTIPLE_PARTITIONS_ABSTAIN
```

### Adjudication

```text
FAMILY_C_STATE=REJECTED_REQUIRES_CALIBRATED_THRESHOLD
ALSO=NOT_COMPLETELY_DEFINED
FAILS=S1,S2,S3,S4
```

Hierarchical partitioning is not carried forward. Reconsideration requires a later, fully
algebraic, threshold-free, tie-closed hierarchy written before any data — and a fresh
authorization. That is not granted here.

## 9. Comparison under the simultaneous criterion

| Requirement | Exact / equitable | Spectral canonical | Hierarchical |
|---|---|---|---|
| S1 nontrivial when emits | FAIL | not closed (operator free) | not closed |
| S2 closed ties | FAIL (no distinguished block) | FAIL (operator / eigenobject free) | FAIL |
| S3 degeneracy abstention | partial only | partial names only | FAIL |
| S4 direct symmetry/boundary | FAIL | FAIL (external falsifiers ≠ direct control) | FAIL |
| Calibrated threshold free | yes for pure equality | not while operator/rank free | no under current forms |
| Simultaneous S1∧S2∧S3∧S4 | **NO** | **NO** | **NO** |
| C5.1 state | `FAIL_MULTIPLE` | `FAIL_MULTIPLE` | `REJECTED_REQUIRES_CALIBRATED_THRESHOLD` |

## 10. What this does and does not decide

### Decided

- No method in the admissible comparison set simultaneously provides a nontrivial emission rule,
  closed ties, closed degeneracy abstention, and direct symmetry/boundary control.
- Therefore C5.1 terminates **negatively** under the binding rule in §4.
- The C5 object family from Decision 040 (`GLOBAL_COMMON_FUTURE_MATRIX_PROFILE`) is **not**
  upgraded to a localizer.
- `CANDIDATE_5` remains unopened.

### Not decided / not authorized

- No rejection of all future mathematics about spectral or algebraic maps outside this brief.
- No freeze of a matrix normalization, operator, threshold, or seed band.
- No implementation, synthetic construction, or generator run.
- No modification of Decision 039 (C4) or Decision 040 (C5 search space), except to record that
  the map bottleneck they left open is **not** closed by C5.1.

### Explicit non-survival

The following terminal is **not** used and is not authorized by this brief:

```text
C5_1_MAP_SPACE_NARROWED
C5_1_SURVIVING_MAP_FAMILY=...
```

A prior draft posture that treated an incomplete spectral sketch as a surviving map family is
superseded by the simultaneous criterion in §4. Incomplete sketches are not survivors.

## 11. Decision

Under the only admissible question and the simultaneous success criteria S1-S4:

```text
no closed map
  common-future matrix -> block/subset/partition or abstention
survives among
  (exact/equitable, spectral canonical, hierarchical-without-threshold).
```

Final terminal:

```text
C5_1_NO_CLOSED_MAP
C5_1_FAMILIES_COMPARED=EXACT_EQUITABLE,CANONICAL_SPECTRAL,HIERARCHICAL
C5_1_SIMULTANEOUS_CRITERION=S1_NONTRIVIAL_AND_S2_TIES_AND_S3_DEGENERACY_AND_S4_SYMMETRY_BOUNDARY
C5_1_RESULT=NEGATIVE
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
```

---

# Current-schema migration — 2026-07-28

> Compatibility appendix only. It preserves the negative C5.1 terminal and records its later
> absorption into decision 042.

```text
ACTA_DISPOSITION = ABSORBED_AS_HISTORICAL_PRECURSOR_BY_DECISION_042
HISTORICAL_FINDINGS = PRESERVED
ANNULLED = NO
SCHEMA_MIGRATION_ONLY = YES
```

## 1. Decision question

Maps to original §1 on a closed matrix-to-block/subset/partition-or-abstention map.

## 2. Verified state

Maps to original §§2–6. No evidence, code, seeds, or sealed state changed in this migration.

## 3. Dossier

The historical dossier is the three-family comparison under simultaneous criteria S1–S4.

## 4. Expert briefs

The legacy act integrated the technical assessments rather than separating current-schema roles.

### Reproducibility engineer brief

Mapped to input discipline, abstention terminals, and the no-execution boundary.

### Mathematician brief

Mapped to the algebraic, spectral, and hierarchical family assessments.

### Mathematical logic brief

No separate legacy role existed; no retrospective opinion is asserted.

### Physicist brief

Mapped to S4 symmetry/boundary control and the localization claim ceiling.

## 5. Falsifier attack

Maps to the simultaneous S1–S4 criterion and explicit non-survival in original §§9–10.

## 6. Pre-registration verdict

- Verdict: PASS
- Reason: documentary negative; no implementation, synthetic construction, generator run, or seed.

## 7. Literature verdict

No new literature adjudication is asserted in this migration.

## 8. Synthesis

No compared family supplied a closed map. `CANDIDATE_5` remained unopened, and decision 042 later
made this terminal part of the C1–C5 line closure.

## 9. Next-step spec

No construction step is authorized. A different future target requires a separate contract.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_DO_NOT_PROCEED

## 11. User sign-off

The user authorized this schema migration on 2026-07-28. It is not a new scientific adjudication
and authorizes no execution.

## 12. Next-step posture (documentary only; not authorized work)

No next construction step is authorized by this decision. If a later, separate authorization is
ever granted, it would have to supply a **fully closed** map definition that hits S1-S4 in the
definition itself, not in a postscript of falsifiers. Until then:

```text
C5_MAP_BOTTLENECK_REMAINS_OPEN
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
```
