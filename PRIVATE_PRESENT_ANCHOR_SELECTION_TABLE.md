# Private Present-Anchor Selection Table

## 1. Status

- Private exploratory design table.
- No execution authorized.
- Purpose: freeze candidate rules for choosing `PRESENT_POINT = p` before
  looking at results.

## 2. Physical Risk

The choice of `p` can introduce a new bias comparable to the old bias from
boundary starts. If `p` is selected by an overly favorable rule, the experiment
may simply replace one privileged anchor with another. The point of this file is
to freeze candidate anchor rules before any outcome is seen, so that a
"present-centered" diagnostic does not become a hidden post hoc selection
device.

## 3. Anchor Rule Table

| anchor_rule_id | anchor_status | anchor_class | allowed_inputs | eligibility_constraints | matching_rule_past_future | boundary_distance_proxy | expected_bias_risk | order_only_status | allowed_verdict_scope | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| CENTRAL_EMBEDDING_POINT | CANDIDATE | GEOMETRY_ASSISTED | embedding coordinates; frozen patch-center definition; preregistered tie-break rule | `p` must be internal; `p` must satisfy a fixed exclusion margin from obvious boundary points if such a margin is declared before execution; one deterministic center-nearest rule only | symmetric truncation by matched depth/cardinality windows around the same `p` | geometry-assisted proxy only | low boundary bias but nontrivial geometry privilege; may overrepresent nominal center | NO | diagnostic comparison against boundary-start workflow only; no order-only recoverability claim | Useful as a clean control against edge starts; not admissible as intrinsic order-only evidence |
| MAX_BOUNDARY_DISTANCE_POINT | CANDIDATE | HYBRID_DIAGNOSTIC | preregistered boundary-distance proxy; preregistered maximization rule; fixed tie-break rule | `p` must be internal and eligible under the frozen proxy; ties must be resolved deterministically or by frozen random seed | same depth cap when possible; otherwise symmetric truncation and logged asymmetry | proxy must be declared as geometry-assisted, order-only, or hybrid before execution | may select atypical deep-interior regions and artificially suppress edge effects | PARTIAL | controlled robustness diagnostic only; no unique physical-anchor claim | Class remains hybrid unless a fully order-only boundary proxy is separately frozen and justified |
| MIDRANK_ORDER_POINT | CANDIDATE | ORDER_ONLY | causal rank/depth proxy; preregistered midrank interval; fixed tie-break rule | `p` must lie in a frozen interior rank band; exact band and tie policy must be frozen before results | compare cones at matched causal depth when possible; otherwise matched cardinality window with symmetric truncation | order-only proxy preferred; geometry-assisted proxy forbidden for this rule | rank may fail to correspond to geometric center; may privilege combinatorial median rather than physical interior | PARTIAL | exploratory order-only candidate with limited intrinsic-structure scope; no geometric-centrality claim | If the rank proxy depends on additional nonlocal heuristics, downgrade interpretation accordingly |
| BALANCED_PAST_FUTURE_VOLUME_POINT | CANDIDATE | ORDER_ONLY | `|C^-(p)|`; `|C^+(p)|`; frozen balance functional; preregistered tie-break rule | `p` must be internal; balance score must be frozen before execution; no threshold tuning after inspection | matched by the same balance-derived depth/cardinality cap; residual asymmetry must be recorded, not normalized away | order-only proxy only | selection may manufacture apparent symmetry because balance is built into the anchor rule | PARTIAL | exploratory asymmetry study only; cannot present symmetry-by-construction as a discovery | High conceptual relevance, but especially vulnerable to circular interpretation |
| RANDOM_ELIGIBLE_INTERNAL_POINT | CANDIDATE | ORDER_ONLY | frozen eligibility rule; preregistered random seed; preregistered sample count | eligibility set must be defined before execution and must exclude trivial boundary points by a frozen rule; randomization procedure must be fixed | same matched-depth or matched-cardinality rule for every sampled `p`; no post hoc resampling | order-only proxy if eligibility is order-only; otherwise downgrade class/status before execution | lower tuning risk but potentially high variance and unstable qualitative verdicts | YES | strongest clean order-only control among simple single-point rules, but only within the frozen eligibility class | Valuable as an anti-cherry-picking baseline if the eligibility rule remains simple |
| MATCHED_ANCHOR_SET | CANDIDATE | HYBRID_DIAGNOSTIC | frozen set-size rule; preregistered matching variables; fixed matching tolerance; optional random seed for tie resolution | anchor set must be constructed by a frozen matching protocol; no dropping unfavorable anchors after results; all selected anchors must be reported | compare each anchor with the same past/future truncation rule, then aggregate by a frozen summary rule | may use geometry-assisted, order-only, or hybrid proxy, but equivalence between proxies is forbidden | robustness gain at the cost of more design degrees of freedom; aggregation can hide heterogeneous failures | UNKNOWN | robustness-only diagnostic surface; not admissible as a single decisive physical anchor | Best used to test stability across anchor choices, not to declare one privileged present |
| FUTURE_OPTIMIZED_RETROFIT_POINT | REJECTED | HYBRID_DIAGNOSTIC | any rule that references crossing, return, adherence, or peel-off outcomes | not eligible under this file | forbidden | forbidden | maximal post hoc bias | NO | none | Explicitly rejected because it selects `p` from target outcomes |
| RUNG_OR_NUCLEUS_PRESENT_VARIANT | RESERVED | HYBRID_DIAGNOSTIC | rung-based or local-nucleus diagnostics declared separately from point-present rules | not a `PRESENT_POINT = p` rule under this file | not applicable to the primary point-present protocol | separate future diagnostic proxy only | risks reintroducing extended-present ambiguity | UNKNOWN | reserved for future non-primary diagnostics only | Included only to keep point-present and extended-anchor variants separated |

## 4. Candidate Anchor Rules

### A. `CENTRAL_EMBEDDING_POINT`

`p` is chosen near the geometric or temporal center of the patch using external
embedding information frozen before execution. This is useful as a clean control
for boundary effects because it explicitly moves the anchor away from obvious
edge starts. It does not support order-only claims.

### B. `MAX_BOUNDARY_DISTANCE_POINT`

`p` is chosen by maximizing a preregistered boundary-distance proxy. Under the
current textual framework this should be treated as `GEOMETRY_ASSISTED` only if
the proxy is purely embedding-based; otherwise it remains
`HYBRID_DIAGNOSTIC`. Its main risk is selecting atypical interior regions that
look favorable only because they are maximally insulated from boundary effects.

### C. `MIDRANK_ORDER_POINT`

`p` is chosen from a preregistered intermediate causal-rank or causal-depth
band. This is the cleanest simple internal alternative when one wants an
order-facing anchor rule, but rank does not automatically coincide with
geometric centrality. If the rank proxy is itself complicated or patched with
extra heuristics, the interpretation should remain `PARTIAL`.

### D. `BALANCED_PAST_FUTURE_VOLUME_POINT`

`p` is chosen by a frozen balance score comparing `|C^-(p)|` and `|C^+(p)|`.
This is physically suggestive because it directly targets bilateral structure,
but it is also risky because it can favor symmetry by construction. Any
observed reduction in asymmetry must therefore be interpreted with caution.

### E. `RANDOM_ELIGIBLE_INTERNAL_POINT`

`p` is chosen randomly from a preregistered eligible internal set. If the
eligibility rule is itself order-only, this is the cleanest low-tuning
single-point control. Its weakness is variance: different seeds may produce
different anchors and unstable qualitative impressions.

### F. `MATCHED_ANCHOR_SET`

This rule selects several anchors `p` matched by preregistered criteria such as
depth, boundary distance, or causal volume. It is useful for robustness and
sensitivity checks, but it should remain `HYBRID_DIAGNOSTIC` and should not be
used as the basis for a unique physical claim.

## 5. Matching Rule

`C^-(p)` and `C^+(p)` must be compared without privileging the future:

- use the same maximum causal depth when both cones support it;
- use the same cardinality window when both cones support it;
- apply symmetric truncation when one cone is shorter or smaller;
- record residual asymmetry instead of correcting it after the fact;
- keep the matching rule fixed for a given run and report any unmet matching
  condition explicitly.

## 6. Boundary Distance Proxy

The boundary-distance proxy must be classified explicitly and no equivalence may
be declared between classes without a separate argument.

### Geometry-assisted proxy

A proxy derived from embedding coordinates, hidden geometric radius, temporal
position, or any external patch geometry. This can support a clean diagnostic
control against edge starts, but it is not order-only.

### Order-only proxy

A proxy derived only from internal order structure, such as causal depth, rank,
internal cone sizes, or another frozen order-theoretic boundary surrogate. This
is the only class that can contribute to a genuine order-only anchor claim.

### Hybrid/diagnostic proxy

A proxy mixing internal order descriptors with geometry-assisted information, or
a proxy whose theoretical status as order-only is not yet clean. This class is
admissible for controlled diagnostics, but not for intrinsic recoverability
claims.

## 7. Forbidden Adaptivity

Forbidden:

- choosing `p` after looking at crossing or return fractions;
- changing `anchor_rule_id` after seeing results;
- discarding unfavorable anchors without a preregistered rule;
- redefining the boundary-distance proxy after results;
- presenting `GEOMETRY_ASSISTED` as `ORDER_ONLY`;
- converting symmetry imposed by the selection rule into a physical discovery;
- replacing a failed single-point rule with a matched-set aggregate unless that
  aggregate rule was frozen in advance;
- using target observables to break ties between candidate anchors.

## 8. Minimal Future Table

| run_id | anchor_rule_id | anchor_status | anchor_class | p_selection_seed | n_candidate_p | selected_p_count | past_depth_window | future_depth_window | past_volume | future_volume | boundary_distance_proxy_value | past_crossing_fraction | future_crossing_fraction | past_return_fraction | future_return_fraction | past_future_asymmetry | qualitative_verdict | forbidden_claims_checked | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## 9. End State

`NO_RUNS_AUTHORIZED_BY_THIS_FILE=YES`

`NO_SIMULATIONS_AUTHORIZED_BY_THIS_FILE=YES`

`NEXT_ALLOWED_STEP=manual_review_of_anchor_rules_before_any_execution`
