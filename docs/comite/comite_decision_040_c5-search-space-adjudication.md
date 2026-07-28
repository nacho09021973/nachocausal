# Comite Decision 040 - C5 search-space adjudication

STATUS: C5_SEARCH_SPACE_ADJUDICATION / CANDIDATE_5_NOT_YET_OPENED / NO_IMPLEMENTATION / NO_SYNTHETIC_EXECUTION / NO_SEEDS
DATE: 2026-07-20

This is a one-file conceptual adjudication of the C5 search space. It does not define
`CANDIDATE_5`, freeze an observable, authorize implementation, authorize synthetic tests, allocate
seed ranges, or authorize any generator run.

## 1. Decision question

Does there exist a class of objects that is:

```text
order-only
non-marginal
potentially horizon-sensitive
independent of a neighbor graph E_M
independent of exterior past beyond the observed patch
equipped from the design stage with a direct boundary falsifier
```

and that could plausibly be developed after the C3 and C4 failures?

The task is to adjudicate search-space families only. No final selection formula, threshold,
parameter grid, seed band, or success terminal is chosen here.

## 2. State of entry

```text
C4_REJECTED_NO_INTRINSIC_NEIGHBOR_GRAPH
DECISION_039_COMMITTED
C5_NOT_OPENED
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
```

Decision 039 is committed as
`docs/comite/comite_decision_039_c4-neighbor-graph-adjudication.md` at commit
`a5276bb7e2df62b7446ce01702a38d1a1d59342a`. Its binding conclusion is that the C4 score may be a
legitimate joint-future idea, but no admissible order-only graph

```text
E_M subset binom(Min(C),2)
```

is available for the observed minimal antichain.

This document does not modify the committed C4 note
`dev/PR003_C4_COMMON_FUTURE_CONVERGENCE_NOTES.md` and does not reopen C4.

## 3. Repository anchors reviewed

Read-only internal sources used for this adjudication:

| Source | Relevant fact |
|---|---|
| `docs/preregistration_square_box_truncated_futures_localization_draft.md` §§4, 6-9, 9.1 | The localizer receives only the finite partial order; coordinates score only after selection. `Min(C)`, strict `J+(i)`, `L(i)`, `V(i)`, postselection `d_edge`, and same-cloud BH/MINK discipline are fixed there. |
| `evidence/square_box_truncated_futures_localization_20260719/dev_support_report.md` | C3 development support completed, but terminal was `INCONCLUSIVE_TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION`; synergy layer was descriptive-only `INSUFFICIENT_VALID_PAIRS`. |
| `dev/PR003_C4_COMMON_FUTURE_CONVERGENCE_NOTES.md` §§1-2, 7-13 | C4 introduced conditioned common futures, proved non-redundancy of pairwise overlaps against individual `L,V` in a finite toy construction, and blocked on `NEIGHBOR_GRAPH_UNRESOLVED`. |
| `docs/comite/comite_decision_039_c4-neighbor-graph-adjudication.md` §§4-11 | Rideout-Wallden and Boguna-Krioukov do not supply a usable `E_M` on distinct minimals; future-only repairs are circular; all-pairs is not a neighbor graph. |
| `dev/X0_Qn_wellposedness_NOTES.md` §§11-12 | Earlier C1/C2 trail: C1 used height cuts and forward flux across ideals; C2 used common futures of antichains; C3 future-width collapse was rejected as singularity/truncation specific. Height convention is element-count longest chain ending at `x`. |
| `docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md` §§8-10 | C1 and C2 were not closed definitions at that stage; C1 lacked a closed search/threshold, C2 lacked a correct intrinsic `E_indep` and had a truncation confound. |
| `docs/comite/comite_decision_009_c1-relational-closure-preflight.md` §§4-10 | The closed `R=Max(C)` C1 reference trivializes in finite posets: `down(Max(C))=C`, `B_R=empty`, `H[C;R]=empty`. |
| `docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md` §§5, 8-9 | Completion/truncation non-identifiability remained physically open; the Alloy witness was not a manifoldlike physical witness. |
| `docs/comite/comite_decision_013_c1-bce-review.md` §§2-4 | Later BCE/Q-track work remained partial; global reference rules can be perturbed by hidden disconnected structure unless groundedness is specified. |
| `dev/PR003_KBEAM_PEELOFF_NOTES.md` | Peeling/beam exploration was development-only, not a frozen result; it illustrates that peeling can be diagnostic but not yet a primary object. |
| `docs/new_geometry_future_observables_addendum.md` §§1-8 | Global dispersion summaries of `L,V` distinguish BH from MINK in `SQUARE_BOX_2P4`, but explicitly do not localize a horizon. |
| `evidence/square_box_boundary_localization_20260719/dev_localization_report.md` | Largest-gap localization development had support in a prior run, but this did not become a confirmatory localization result. |

No prior run or audit already answers the C5 question. Existing results show that marginal future
dispersion can classify BH vs MINK and that scalarized minimal selectors can be edge-dominated,
but they do not close a non-marginal, order-only localization object with a boundary falsifier.

## 4. Binding restrictions for any C5 family

An admissible family must simultaneously satisfy:

1. construction and selection use only the finite order;
2. relabeling invariance is exact;
3. no neighbor graph `E_M` is required;
4. selection is not simply "pick the best minimal by another scalar";
5. the object is not determined by `{L(i),V(i): i in Min(C)}` or their ranks;
6. no past exterior to the observed patch is required;
7. a preselector may not condition on the same structure later interpreted as the signal;
8. coordinates, `r`, `t`, `R_S`, and box-wall distances may enter only after selection;
9. boundary/roof falsification is designed before seeds;
10. a synthetic counterexample must separate the object from C3 and C4 marginal channels;
11. the object is computable from structures retained in the repository;
12. no free calibration may be chosen after observing seeds.

## 5. Family A - Global common-future distributions and matrices

### Object class

Use all unordered pairs of minimals, or all pairs passing algebraic validity checks, without first
declaring spatial neighbors. The family includes:

```text
{|J+(i) cap J+(j)| : i,j in M, i != j}
```

and richer objects such as the full overlap matrix on `M`, overlap profiles conditioned on marginal
future sizes, residual overlap matrices, spectra, quantiles, and block structure of the pairwise
common-future relation.

The scalar multiset alone is not enough for localization: it can classify a causet as having more
or less global common-future convergence, but it forgets which minimals participate. The viable
subfamily is therefore the full pair-indexed matrix/profile, not a single scalar distribution.

### Assessment

| Field | Adjudication |
|---|---|
| Object mathematical | Pair-indexed common-future overlap matrix/profile over `Min(C)`, with optional conditioning on fixed marginal sizes. No formula is frozen. |
| Order-only information used | `Min(C)`, strict futures `J+(i)`, set intersections, pairwise cardinalities, and order-derived marginal strata. |
| Unit of analysis | Whole causet plus a relation on minimal pairs; possible downstream output is a subset/block of minimals, not a single winner. |
| Potential localization capacity | Plausible only through relabel-invariant block/subset structure in the matrix. A scalar histogram is classification-only. |
| Independence from `L,V` | Yes for the matrix/profile in general: two finite constructions can keep all individual future sizes and future depths fixed while changing pairwise intersections. C4 already records the two-pair toy separation in `dev/PR003_C4_COMMON_FUTURE_CONVERGENCE_NOTES.md` §11. |
| Boundary or roof dependence | Serious. Common futures can grow because all futures hit the same roof, singular funnel, side wall, density lobe, or global box shape. |
| Free parameters | High unless the downstream block/subset map is closed before data. Candidate parameter hazards include normalization, marginal bins, spectral rank, number of blocks, and tie rules. |
| Approximate cost | For `m=|M|`, naive pairwise bitset intersections are `O(m^2 N / word_size)` after futures are represented as bitsets; spectral/block analysis adds at least cubic cost in `m` unless sparse or approximate methods are justified. |
| Synthetic falsifier minimum | Two finite posets with identical `{L(i),V(i)}` over minimals but different overlap matrices, different invariant block structure, and different selected subset/terminal under a future closed map. Include a relabeling permutation test. |
| Main reason for viability | It uses genuinely joint information and avoids the C4 neighbor-graph blocker by treating all pairwise common futures as the object. |
| Main reason for rejection risk | Without a closed map from matrix to region it remains a global classifier; with an ad hoc map it reintroduces hidden degrees of freedom. |
| Family state | `VIABLE_FOR_CONCEPT_DEVELOPMENT` for the full matrix/block family; scalar-only summaries are `REJECTED_NO_LOCALIZATION_MAP`. |

### Non-marginality requirement

The load-bearing non-marginal object is not the list of future sizes. It is the incidence pattern
of which pairs share which future elements. Holding all individual `V(i)=|J+(i)|` and link-depth
values fixed does not fix `|J+(i) cap J+(j)|` for every pair. A future synthetic falsifier must
extend the C4 toy construction from one pair to two whole finite posets:

```text
same multiset of minimal L values
same multiset of minimal V values
same per-minimal L,V assignment up to relabeling
different common-future overlap matrix
different invariant block/subset output under the closed C5 map
```

This test is conceptual only here. No posets are constructed or executed.

### Localization map status

There is a possible non-circular map class: derive a relabel-invariant subset of minimals from the
overlap matrix itself, such as a block, orbit, eigenspace-supported partition, or extremal
submatrix, provided the rule is fixed without coordinates, labels, or observed seeds.

That statement does not choose such a map. It only identifies the one family where a map could
exist without spatial neighbors or single-minimal scalar selection. The map is the main C5
precondition.

### Direct boundary falsifier

Before any generator seed, a future development of this family must include at least:

- symmetric top truncation: if an artificial roof alone creates the same block/matrix structure,
  reject as `REJECTED_BOUNDARY_DOMINATED`;
- symmetric lateral truncation: if side walls create the same subset/block, reject;
- maximal peeling: recompute after fixed removal of maximal layers; if the block/subset changes
  materially or appears only near the roof, reject as truncation dominated;
- MINK same-cloud: if the same point cloud under flat causality reproduces the structure, reject;
- density inhomogeneity: if denser regions alone create the structure, reject;
- height-domain variation: if the structure tracks only absolute depth or number of layers, reject;
- conceptual ceiling extension: if extending the roof erases or translates the structure, reject.

## 6. Family B - Intrinsic cuts, shadows, and order frontiers

### Object class

Use order-intrinsic cuts or frontiers: height levels, antichains, ideals/filters, shadows of cuts,
interfaces between downsets and complements, interval profiles, or changes in these structures
between cuts.

This family is close to the earlier C1/C2 trail. It should not be renamed as C5 unless it avoids
the exact prior blockers: undefined search class, wall/roof coupling, missing physical map, and
post-hoc normalization.

### Assessment

| Field | Adjudication |
|---|---|
| Object mathematical | Height cuts `L_k={x:h(x)=k}`, ideals `D_k={x:h(x)<=k}`, shadows/frontiers of ideals or filters, and interval-profile changes between cuts. |
| Order-only information used | Height, antichain membership, downsets/upsets, relations crossing cuts, interval cardinalities, maximal/minimal layers. |
| Unit of analysis | Cut, frontier, ideal, or layer family, usually over all elements rather than minimals. |
| Potential localization capacity | Possible as a cut or band of elements, but previous C1 work shows this map is not automatically physical. Height cuts can localize temporal depth rather than horizon structure. |
| Independence from `L,V` | Mixed. Some cut profiles use higher-order relation counts or interval distributions, but many height/future-shadow summaries collapse to depth, volume, or roof proximity. |
| Boundary or roof dependence | Very high. Height and ideal frontiers are naturally sensitive to finite top/bottom walls; `R=Max(C)` already trivialized in finite posets. |
| Free parameters | High: choice of cut family, bulk exclusion, local minimum rule, shadow definition, interval profile, and tie handling. |
| Approximate cost | Height and cut profiles are polynomial; exhaustive antichain searches can be exponential; interval-profile matrices can be expensive but finite-order computable. |
| Synthetic falsifier minimum | Two posets with identical height profile and minimal `L,V`, but different cut-frontier interval profiles and different selected cut; plus a top-wall-only construction that must be rejected. |
| Main reason for viability | It changes the mathematical object away from minimals and can output a cut/subset directly. |
| Main reason for rejection | Prior C1/BCE history shows unresolved definition and boundary dominance; no currently closed cut object distinguishes horizon from temporal depth or roof without new choices. |
| Family state | `BLOCKED_BY_UNRESOLVED_DEFINITION` |

### Localisation versus classification

Cuts can output a subset without selecting a minimal or pair, so the family has the right shape in
principle. The problem is that an intrinsic cut is not automatically a horizon-adjacent region.
The prior `R=Max(C)` rule produced a universal finite-poset triviality, while height/flux cuts
require a closed bulk rule and a direct top/side-wall falsifier. No repository artifact currently
answers those gaps.

For C5 search-space purposes, this family is not rejected as impossible, but it does not survive
as the next narrow family because too much of C1's unresolved machinery would be inherited.

## 7. Family C - Stability as the primary object under causal peeling

### Object class

Instead of computing a signal and then using peeling as a control, define the object by persistence
under a preregistered removal of maximal layers. Examples include stable matrix blocks, stable cut
features, stable interval-profile changes, or stable distributions across peeling depths.

Peeling here means removal of one or more maximal layers by a fixed order-only rule. It must not
use coordinates or target labels.

### Assessment

| Field | Adjudication |
|---|---|
| Object mathematical | A sequence of order-derived objects on `C`, `C\Max(C)`, and further peeled subposets, with signal defined by persistence across the sequence. |
| Order-only information used | Maximal elements/layers, induced subposets, and a base object recalculated at each level. |
| Unit of analysis | Trajectory of objects across peeled causets. |
| Potential localization capacity | Depends entirely on the base object and a rule matching objects across peel levels. Peeling alone does not define a region. |
| Independence from `L,V` | Not guaranteed. Stability of marginal `L,V` summaries would still be marginal; stability of overlap matrices or cuts could be non-marginal. |
| Boundary or roof dependence | It is designed to attack roof dependence, but stable side-wall artifacts and density structures can persist under top peeling. |
| Free parameters | High: number of layers removed, stopping rule, matching rule, stability metric, material-change threshold, and base-object choice. |
| Approximate cost | Multiplicative overhead over the base object; if recomputing pairwise matrices for `p` peel levels, roughly `p` times the base cost. |
| Synthetic falsifier minimum | A roof-only poset where the apparent signal vanishes under peeling, and a side-wall/density artifact where top peeling falsely appears stable and must still be rejected by a separate lateral/density control. |
| Main reason for viability | It makes the roof falsifier primary rather than auxiliary. |
| Main reason for rejection | Without a base non-marginal localization object and an order-only matching rule, stability is a property of something else, not a standalone C5 object. |
| Family state | `BLOCKED_BY_UNRESOLVED_DEFINITION` |

### Matching blocker

A stability object must say what is "the same" feature before and after peeling. Matching by labels
of surviving elements may be relabel-invariant only if the selected subset itself conjugates under
permutation and no deleted element is needed to identify it. Matching by coordinates is forbidden.
Matching by the score that will later be interpreted is circular.

Therefore peeling is mandatory as a falsifier for any surviving C5 family, and may become part of
the eventual object, but it cannot by itself narrow the search space today.

## 8. Cross-family comparison

| Requirement | A. Common-future matrix | B. Cuts/frontiers | C. Peeling-primary |
|---|---|---|---|
| Order-only possible | yes | yes | yes |
| Relabel-invariant possible | yes | yes | yes |
| Avoids `E_M` | yes | yes | yes |
| Avoids single-minimal scalar selector | yes, if matrix/block output | yes | yes |
| Non-marginal vs `L,V` | yes for full matrix | unresolved/mixed | depends on base object |
| No exterior past needed | yes | yes | yes |
| Non-circular preselection possible | possible but not yet closed | unresolved | unresolved |
| Built-in boundary falsifier possible | yes, mandatory | possible but inherited blockers | yes for roof, not side walls |
| Localizes rather than classifies | possible via invariant block/subset | possible via cut, but not closed | not without base object |
| Main blocker | matrix-to-subset map | prior C1 definition/boundary blockers | object matching/base-object dependence |
| State | `VIABLE_FOR_CONCEPT_DEVELOPMENT` | `BLOCKED_BY_UNRESOLVED_DEFINITION` | `BLOCKED_BY_UNRESOLVED_DEFINITION` |

Only family A survives this search-space gate, and only in its pair-indexed matrix/block form. A
scalar histogram of common-future sizes is explicitly not sufficient.

## 9. Boundary-falsifier contract for the surviving family

Any later C5 concept based on family A must define, before code or seeds, a synthetic falsifier
suite with at least these contracts:

1. **Marginal separation:** same `{L(i),V(i)}` over minimals, different common-future matrix, and
   different matrix-derived subset/terminal.
2. **Relabeling:** exact conjugacy of matrix, blocks/subsets, terminal, and all abstentions under
   arbitrary label permutations.
3. **Top truncation:** a symmetric roof-only construction must not produce a positive localized
   subset; if it does, reject as boundary dominated.
4. **Lateral truncation:** symmetric side-wall truncation must not produce the same subset class;
   if it does, reject as boundary dominated.
5. **Peeling:** fixed maximal-layer peeling must distinguish roof-driven convergence from
   persistent structure; instability or roof-only emergence rejects the design.
6. **MINK same-cloud:** flat causality on the same point cloud must not reproduce the same matrix
   block/subset signal.
7. **Density inhomogeneity:** a density lobe alone must not create the selected subset.
8. **Height-domain variation:** changing the intrinsic height range must not merely translate the
   selected subset to the new roof.
9. **Degeneracy:** empty `M`, too few minimals, all-equal overlap matrix, automorphism orbits too
   large for unique subset, and non-finite normalizations must have abstention terminals.

These are conceptual contracts only. No synthetic poset is built here.

## 10. What a later C5 concept may and may not do

Permitted next conceptual direction:

- work on a full common-future matrix/profile over all minimals;
- define a relabel-invariant map from that matrix to a subset, block, cut, or abstention;
- make boundary falsification part of the definition before any generator run;
- compare historically to C3/C4 only as prior failures, not as tunable baselines.

Forbidden without a new authorization:

- implement any matrix computation;
- run synthetic or real seeds;
- choose a spectral rank, clustering rule, threshold, alpha, effect floor, or seed range;
- use coordinates, `r`, `t`, `R_S`, `d_edge`, or labels during construction or selection;
- reopen C4 by calling all pairs a neighbor graph;
- claim horizon detection from a global classifier;
- define `CANDIDATE_5`.

## 11. Decision

The search space is not empty. One family survives at the level of concept development:

```text
global pair-indexed common-future matrix/profile over minimals,
with localization only through a future relabel-invariant block/subset map
```

The surviving class is genuinely different from C3's marginal `L,V` scalarization and from C4's
neighbor-edge maximization. It does not need exterior past and does not require a minimal-neighbor
graph. Its direct boundary falsifier is available in principle through roof/lateral truncation,
maximal peeling, MINK same-cloud, density, and height-domain variation.

The main unresolved bottleneck is not the joint information itself. It is the closed, non-circular,
relabel-invariant transformation from the overlap matrix to a localized subset or abstention.

Final terminal:

```text
C5_SEARCH_SPACE_NARROWED
C5_SURVIVING_FAMILY=GLOBAL_COMMON_FUTURE_MATRIX_PROFILE
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
```

---

# Current-schema migration — 2026-07-28

> Compatibility appendix only. It preserves the original search-space result and records that
> decisions 041–042 later resolved its forward status.

```text
ACTA_DISPOSITION = ABSORBED_AS_HISTORICAL_PRECURSOR_BY_DECISION_042
HISTORICAL_FINDINGS = PRESERVED
ANNULLED = NO
SCHEMA_MIGRATION_ONLY = YES
```

## 1. Decision question

Maps to original §1 on whether any C5 concept family deserved one bounded conceptual step.

## 2. Verified state

Maps to original §§2–3. No evidence, code, seeds, or sealed state changed in this migration.

## 3. Dossier

The historical dossier is the anchor inventory and three-family comparison in §§3–8.

## 4. Expert briefs

The legacy act integrated its assessments by family rather than by current-schema role.

### Reproducibility engineer brief

Mapped to the boundary-falsifier contract and forbidden actions in §§9–10.

### Mathematician brief

Mapped to the closure and invariance requirements for the matrix-to-block map.

### Mathematical logic brief

No separate legacy role existed; no retrospective opinion is asserted.

### Physicist brief

Mapped to the localization-versus-classification distinction and boundary controls.

## 5. Falsifier attack

Maps to original §9 and the map bottleneck stated in §11.

## 6. Pre-registration verdict

- Verdict: PASS
- Reason: concept-only narrowing; no candidate, implementation, execution, seeds, or thresholds.

## 7. Literature verdict

No new literature adjudication is asserted in this migration.

## 8. Synthesis

040 permitted only one documentary C5.1 adjudication. Decision 041 found no closed map, and
decision 042 then closed the C1–C5 localizer line.

## 9. Next-step spec

The historical C5.1 step was discharged by decision 041 and is not reopened here.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off

The user authorized this schema migration on 2026-07-28. It is not a new scientific adjudication
and authorizes no execution.
