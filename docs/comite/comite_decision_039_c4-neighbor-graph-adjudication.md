# Comite Decision 039 - C4.1 neighbor-graph adjudication

STATUS: C4.1_CONCEPTUAL_ADJUDICATION_COMPLETE / NO_IMPLEMENTATION / NO_SYNTHETIC_EXECUTION / NO_SEEDS
DATE: 2026-07-20
BASE_HEAD: 136c193688bc863635e6d0c87cdb133e7f502522

> This is a one-file conceptual adjudication. It does not amend or freeze the C4 note, define a
> fifth localizer, authorize implementation, authorize synthetic execution, allocate seed ranges,
> or authorize any real-generator run.

## 1. Decision question

Can either of the following published causal-order constructions define a graph

```text
E_M subset {{i,j} : i,j in Min(C), i != j}
```

that is simultaneously:

1. order-only;
2. invariant under relabeling;
3. non-circular with respect to the C4 persistence score `S_ij`;
4. computable from the finite observed patch;
5. closed under ties and degeneracies?

Only two families are in scope:

- Rideout-Wallden spacelike predistance, `2-link` distance, and the derived `s-link` relation;
- Boguna-Krioukov distance from causal overlaps.

The only admissible terminals are:

```text
C4_NEIGHBOR_GRAPH_VIABLE
C4_REJECTED_NO_INTRINSIC_NEIGHBOR_GRAPH
C4_RECLASSIFIED_NON_ORDER_ONLY
```

## 2. Repository state and binding C4 requirements

The committed C4 concept is
`dev/PR003_C4_COMMON_FUTURE_CONVERGENCE_NOTES.md` at base commit
`136c193688bc863635e6d0c87cdb133e7f502522`.

Binding facts from that note and the third-localizer contract are:

- The localizer receives only the finite partial order. Coordinates and `R_S` are available only
  after selection for scoring
  (`docs/preregistration_square_box_truncated_futures_localization_draft.md:129-140`).
- The two causal models are `1+1D` Schwarzschild-EF and `1+1D` Minkowski on the same finite point
  cloud (same file, lines 133-140).
- `M=Min(C)` is an antichain and `J+(i)` is strict (same file, lines 157-179).
- Pairwise future overlap was explicitly left open as a possible order-only profile, not certified
  as a neighbor construction (same file, lines 355-368).
- C4 forbids coordinates, `r`, `t`, labels, or spatial order in construction of `E_M`
  (`dev/PR003_C4_COMMON_FUTURE_CONVERGENCE_NOTES.md:183-193`).
- The required neighbor graph, degree behavior, tie handling, connectivity/abstention,
  degeneracies, and computational cost are unresolved (same file, lines 325-368).
- Selection remains conditional:

  ```text
  {i*,j*} = argmax_{{i,j} in E_M} S_ij
  ```

  and is not executable while `E_M` is unresolved (same file, lines 370-397).

The repository past-matrix convention is `C[a,b]=true` iff `b` precedes `a`, implemented in
`nachocausal/generator.py:88-129`. This adjudication does not alter that convention or any C4
formula.

## 3. Meaning of independence from the C4 score

Both a graph and a score are ultimately functions of the same finite order, so "independent" here
cannot mean probabilistic independence. It means design independence:

- `E_M` must not select or rank pairs by `c_q=|F_i^q cap F_j^q|`;
- it must not use a monotone transform, threshold, proxy, or preferred subset of the same
  prefix-restricted common future that C4 later rewards;
- it must not select pairs because their common futures already converge unusually strongly;
- its free parameters and tie rules must be fixed without observing the C4 score.

This condition prevents the graph from preselecting the signal that the conditional maximization
is supposed to test. Sharing the causal order as input is permitted. Conditioning directly on the
same common-future structure is not.

## 4. Structural fact about distinct minimals

For every `i in Min(C)`, the strict past is empty:

```text
J-(i) = empty set.
```

Proof: if some `x` satisfied `x < i`, then `i` would not be minimal. Therefore, for two distinct
minimals `i,j`:

```text
J-(i) cap J-(j) = empty set.
```

This is not a finite-sample accident or a low-support branch. It follows identically from the
domain chosen by C4. Any spatial-distance construction requiring a reference element or a
minimizer in the strict common past is undefined for every candidate pair in `binom(M,2)`.

Although `M` is an antichain, that alone does not provide a spatial adjacency. In this finite
causet it also lies at the observed past boundary, unlike the central, two-sided antichains used in
some spatial-reconstruction studies.

## 5. Family A: Rideout-Wallden / 2-link

### 5.1 Primary-source definitions

Primary source: David Rideout and Petros Wallden, *Spacelike distance from discrete causal order*,
[arXiv:0810.1768](https://arxiv.org/abs/0810.1768), especially sections IV-VI.

For an `n`-element antichain, section IV, definitions 2a-2b, defines a future `n-link` as an
element linked to every antichain element, and analogously for a past `n-link`. These predicates
are order-only, finite-order computable, symmetric in the antichain elements, and invariant under
relabeling.

For two unrelated elements `x,y`, section V.A defines the `2-link distance` by:

1. finding each future `2-link f_k` of `x,y`;
2. finding `p_k` in the common past of `x,y` that minimizes timelike distance to `f_k`;
3. recording that timelike distance;
4. averaging over all future `2-links`.

The paper notes the time-dual option: start from past `2-links`, minimize over the common future,
or average both orientations. Section VI.A then defines an `s-link` between unrelated elements
when their `2-link distance` is below a fixed threshold `lambda`.

These distinctions are binding:

```text
future 2-link exists
!=
2-link distance is defined
!=
s-link / spatial-neighbor relation is defined.
```

The paper's nearest-neighbor relation is the thresholded predistance, not mere sharing of one
future `2-link`.

### 5.2 Failure on the minimal antichain

The future-oriented `2-link distance` cannot be evaluated on `M`: step 2 minimizes over
`J-(i) cap J-(j)`, which is empty for every distinct minimal pair. The past-oriented construction
cannot start either, because no minimal has a past link and hence no pair of minimals has a past
`2-link`.

This gives a structural terminal for the published predistance on the C4 domain:

```text
RW_COMMON_PAST_EMPTY_FOR_ALL_MINIMAL_PAIRS
```

The issue is not repaired by the fact that the ambient model is `1+1D`. In `M^2`, two elements
form the `n=d` case. Rideout-Wallden derive a finite, generally small expected number of future
`2-links`, with an upper bound that decreases to zero with pair separation. In section V.A they
state that their `2-link distance` requires such links and point to the naive predistance instead
for `1+1D`. The naive predistance also minimizes between the common past and common future, so it
is equally undefined on distinct minimals.

Thus the published construction does not provide an evaluable distance for all, or even a defined
nonempty subset selected independently, of `binom(M,2)`.

### 5.3 Why future-2-link incidence is not an admissible repair

One could invent the graph

```text
{i,j} is an edge iff i and j possess at least one future 2-link.
```

That rule would be order-only, relabel-invariant, and computable. It is nevertheless inadmissible
for this adjudication for two independent reasons:

1. It is not the Rideout-Wallden `s-link` relation supported by their numerical nearest-neighbor
   study. Treating it as a spatial neighbor graph would be a new, unvalidated construction.
2. A future `2-link` is an element of the common future satisfying an additional cover condition.
   Conditioning `E_M` on its existence preselects pairs by a rare feature of the same joint future
   that `c_q` and `S_ij` later reward. It therefore fails C4's design-independence requirement.

In `1+1D`, where future `2-links` are not abundant and their probability decreases with
separation, the rule also has no closed degree, connectivity, or nonempty-graph guarantee. Adding
degree caps or selecting a fixed number of pairs would require a new score and relabel-invariant
tie rule not supplied by the paper.

### 5.4 Threshold, geometry, and transfer

Rideout-Wallden define `s-link` using a fixed threshold `lambda`, but the numerical value reported
for typical neighbors was calibrated in a finite `M^3` cube using an embedded nearest unrelated
element. The paper uses `lambda=2.186178` in that experiment and later `2.7` for a graph on a
central, thickened inextendible antichain because that antichain was sparse.

Consequences for C4:

- no source-derived threshold is supplied for a `1+1D` curved finite patch;
- the numerical calibration used embedding information and a different dimension and domain;
- the demonstrated antichain was central and had causal support on both sides, not `Min(C)`;
- the paper's curved-spacetime discussion proposes local-flatness transfer but does not validate
  the relation in this Schwarzschild-EF patch or at a horizon;
- a threshold imported from those experiments would not close degree or tie behavior here.

The full order computation is polynomial in a finite causet once covers and longest-chain
distances are available, but it is substantially heavier than future incidence alone. Computability
in principle does not cure the empty common-past domain or the missing transferable threshold.

### 5.5 Family-A disposition

```text
ORDER_ONLY_IN_SOURCE_DOMAIN: YES
RELABEL_INVARIANT: YES
COMPUTABLE_ON_FINITE_TWO_SIDED_DOMAIN: YES
DEFINED_ON_DISTINCT_MINIMALS: NO
INDEPENDENT_FUTURE_2_LINK_REPAIR: NO
THRESHOLD_CLOSED_FOR_THIS_PATCH: NO
DEGREE_AND_TIES_CLOSED: NO
```

Rideout-Wallden does not yield an admissible `E_M` for C4.

## 6. Family B: Boguna-Krioukov causal overlaps

### 6.1 Primary-source definition

Primary source: Marian Boguna and Dmitri Krioukov, *Measuring spatial distances in causal sets via
causal overlaps*, [arXiv:2401.17376](https://arxiv.org/abs/2401.17376), especially section III,
equations (16)-(31), section IV.A, and section VI.

For spacelike-separated events `a,b`, their causal overlap is defined relative to an arbitrary
reference event

```text
c in Past(a,b) = Past(a) cap Past(b).
```

Writing `I(x,c)` for the relevant Alexandrov intervals, equations (17)-(19) split their union into
the two noncommon regions `A,B` and common region `C`. Equation (16) normalizes the volume of `C`
by the smaller interval volume; equation (28) translates those volumes into element counts in a
causet. The reference is chosen so that `a` and `b` are approximately equidistant in proper time
from `c`.

The numerical procedure in section IV.A uses two filters for `c`. Its first filter uses sprinkling
density and embedding dimension for efficiency. Its second filter uses interval cardinalities and
can be evaluated from the causal set alone. Both filters presuppose that candidate references
`c in Past(a,b)` exist.

The construction is therefore order-only after an admissible reference has been selected by an
order-only rule, but common-past support is part of its mathematical domain, not an optional
implementation detail.

### 6.2 Failure on the minimal antichain

For every distinct `i,j in M`:

```text
Past(i,j) = empty set.
```

There is no candidate `c`, no interval `I(i,c)` or `I(j,c)`, and no causal overlap of the form
defined in equations (16)-(19). Neither the order-only second filter nor the distance formula can
be entered.

This gives the structural terminal:

```text
BK_COMMON_PAST_REFERENCE_ABSENT_FOR_ALL_MINIMAL_PAIRS
```

Supplying a reference outside the observed patch would change the input object and require causal
relations not retained by the pipeline. Adding an artificial root would not reconstruct the
missing intervals and is not part of the cited construction.

### 6.3 Time reversal is not an admissible repair

A formal time-dual could replace the missing common-past reference with a common-future reference.
That does not rescue C4.1:

- the cited paper defines and tests the past-reference construction, not this finite-patch dual;
- the curved BH patch and its singular/top boundary are not time-symmetric;
- the dual would use intersections and cardinalities inside the pair's common future, exactly the
  information channel C4 scores through `F_i^q cap F_j^q`;
- selecting short-distance pairs by that dual overlap would precondition `E_M` on the convergence
  signal later maximized by `S_ij`;
- the result would inherit the top-truncation sensitivity that C4's two-prefix minimum and maximal
  peeling are intended to falsify.

This is both an unsupported transfer and a design-circular graph.

### 6.4 Distance does not by itself close a graph

Boguna-Krioukov provide a pairwise distance estimator, not a graph construction with a fixed
degree, connectivity rule, exact tie behavior, or finite-patch abstention terminal. Even if the
distance were defined on `M`, converting all pairwise distances to `E_M` would still require one of:

- a distance threshold;
- `k` nearest neighbors;
- a global minimum structure such as a spanning graph;
- a tie-expanded relation.

None is selected or validated by the source for this application. Choosing one now would add a new
ad hoc construction and at least one new degree of freedom.

The paper's experiments are in finite Minkowski boxes. It explicitly reports finite-box bias when
intervals used in causal overlaps extend outside the simulation domain. Its conclusion argues that
local-flatness may permit extension when the curvature scale is sufficiently large relative to the
minimum reliable neighborhood; it does not demonstrate the estimator in a curved horizon patch.

### 6.5 Family-B disposition

```text
ORDER_ONLY_WITH_VALID_REFERENCE: YES
RELABEL_INVARIANT_WITH_CLOSED_REFERENCE_RULE: YES
COMPUTABLE_ON_FINITE_SUPPORTED_DOMAIN: YES
REFERENCE_EXISTS_FOR_DISTINCT_MINIMALS: NO
TIME_DUAL_VALIDATED: NO
TIME_DUAL_INDEPENDENT_OF_S_IJ: NO
GRAPH_THRESHOLD_DEGREE_AND_TIES_CLOSED: NO
```

Boguna-Krioukov does not yield an admissible `E_M` for C4.

## 7. Eichhorn-Gamito-Stokes scope

Primary repository source:
`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`,
derived from [arXiv:2605.06813](https://arxiv.org/abs/2605.06813) and checked against that primary
record.

Section IV.A defines causal ladders as linked rung sequences used to approximate null geodesics
(local lines 232-266). Section IV.B studies changes in predistance between pairs of ladders as a
focusing diagnostic (lines 274-294). This supports the physical motivation for looking for joint
causal structure, but it does not define adjacency among the elements of `Min(C)`.

Later selections in that paper use ladder objects, predistances, and, for a horizon construction,
an interior/exterior split. Importing those choices would change C4's object and observation
channel. EGS therefore supplies no missing neighbor graph for the present candidate.

## 8. Comparative gate

| Requirement | Rideout-Wallden | Boguna-Krioukov |
|---|---|---|
| Order-only in published domain | yes | yes, with admissible reference |
| Relabel-invariant in published domain | yes | yes, with closed reference rule |
| Defined for two observed minimals | no | no |
| Needs strict common past | yes for future-oriented predistance | yes |
| Validated in this `1+1D` curved finite patch | no | no |
| Produces a graph without extra threshold/rule | no | no |
| Degree/connectivity/ties closed for `M` | no | no |
| Independent repair using only observed future | no | no |

No row can be repaired merely by abstaining on exceptional pairs: the missing common past affects
every distinct pair in `binom(M,2)`. A method that abstains for all candidate pairs is not a
localizer domain.

## 9. Falsifier attack on apparent alternatives

The following alternatives are explicitly rejected by this adjudication:

1. **Order the minimals by `r`, `t`, another coordinate, or raw labels.** This is computable but not
   order-only. It would be a different, reclassified candidate.
2. **Connect pairs sharing any future element.** This is almost the unnormalized common-future
   channel and preselects the C4 signal.
3. **Connect pairs sharing a future `2-link`.** This is not the published `s-link`, can be sparse or
   empty in `1+1D`, has uncontrolled degree, and preselects common-future convergence.
4. **Add an artificial common-past root.** This changes the observed poset and supplies no missing
   causal interval geometry.
5. **Use a time-reversed causal-overlap distance.** This is unvalidated in the source, sensitive to
   the observed roof, and circular with C4's future-overlap score.
6. **Import `lambda=2.186178` or `2.7`.** These values come from different finite `M^3` experiments
   and do not close a `1+1D` minimal graph.
7. **Use all pairs.** `E_M=binom(M,2)` is order-only and relabel-invariant but is not a neighbor
   graph, has degree `|M|-1`, and removes the proposed local spatial precondition. It also changes
   the multiplicity and physical meaning of the candidate.
8. **Choose the closest pair using C4's own `S_ij`.** This collapses graph construction into score
   maximization and is exactly the circularity the C4.1 gate forbids.

## 10. Decision

Both audited families contain genuine order-only spatial information in domains with sufficient
causal support. Neither supplies a closed graph on the observed minimal antichain:

- Rideout-Wallden's published nearest-neighbor relation requires a bilateral predistance that is
  undefined without a common past, and its `s-link` threshold is not closed for this domain.
- Boguna-Krioukov requires a common-past reference that provably does not exist for distinct
  minimals.
- Future-only repairs would either be new ad hoc constructions or condition on the same joint
  future used by `S_ij`.
- Coordinate ordering would change the candidate rather than resolve it intrinsically.

Therefore the gate closes as:

```text
C4_REJECTED_NO_INTRINSIC_NEIGHBOR_GRAPH
```

This is a rejection of C4 as a closed order-only localizer on `Min(C)` under the two audited
families. It is not a theorem that no order-only spatial adjacency can ever be defined on any
causet, and it does not refute focusing, causal-overlap distances, `2-link` methods, or information
in `J+(i) cap J+(j)` generally.

The alternative terminal `C4_RECLASSIFIED_NON_ORDER_ONLY` is not used because this adjudication
does not adopt a coordinate-based graph. Such a reclassification would require a separately
specified candidate and claim boundary.

## 11. Operational boundary

This acta closes the single documentary opportunity granted to C4. It does not authorize:

- implementation of `Z_ij`, `S_ij`, either distance family, or any graph;
- construction or execution of synthetic posets;
- real-generator execution or any seed allocation;
- reuse of third-localizer development or evaluation seeds;
- modification of the committed C4 note or any frozen contract;
- automatic opening, definition, or implementation of C5.

Final state:

```text
C4_REJECTED_NO_INTRINSIC_NEIGHBOR_GRAPH
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
C5_NOT_OPENED
```

---

# Current-schema migration — 2026-07-28

> Compatibility appendix only. It preserves the scoped negative in this act and records that
> decision 042 later absorbed it into the C1–C5 line closure.

```text
ACTA_DISPOSITION = ABSORBED_AS_HISTORICAL_PRECURSOR_BY_DECISION_042
HISTORICAL_FINDINGS = PRESERVED
ANNULLED = NO
SCHEMA_MIGRATION_ONLY = YES
```

## 1. Decision question

Maps to the original §1 question on a closed intrinsic neighbor graph for C4.

## 2. Verified state

Maps to original §§2–4. No evidence, code, seeds, or sealed state changed in this migration.

## 3. Dossier

The historical dossier is the repository anchors and two published families reviewed in §§5–8.

## 4. Expert briefs

The legacy act used an integrated adjudication rather than separate current-schema briefs.

### Reproducibility engineer brief

Mapped to the operational boundary in original §11.

### Mathematician brief

Mapped to the domain and closure arguments in §§4–8.

### Mathematical logic brief

No separate legacy role existed; no retrospective opinion is asserted.

### Physicist brief

Mapped to the domain-transfer and physical-meaning restrictions in §§5–8.

## 5. Falsifier attack

Maps directly to original §9; its scope limitation is preserved.

## 6. Pre-registration verdict

- Verdict: PASS
- Reason: documentary adjudication only; no implementation, execution, seeds, or seal change.

## 7. Literature verdict

No new literature adjudication is asserted. The two audited source families retain their original
scoped treatment.

## 8. Synthesis

C4 was rejected only as a closed order-only localizer on the observed minimal antichain under the
two audited families. Decision 042 later incorporated this result without upgrading it to a
universal theorem.

## 9. Next-step spec

No C4 restart is authorized. Any future target must come from a separate scientific contract.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_DO_NOT_PROCEED

## 11. User sign-off

The user authorized this schema migration on 2026-07-28. It is not a new scientific adjudication
and authorizes no execution.
