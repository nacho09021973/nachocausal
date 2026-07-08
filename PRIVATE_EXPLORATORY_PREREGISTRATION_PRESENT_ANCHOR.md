# Private Exploratory Preregistration: Present-Anchor Experiment

## 1. Status

STATUS: PRIVATE EXPLORATORY PREREGISTRATION

- Private exploratory preregistration.
- Not a publication claim.
- Not a replacement for PR003 / K-beam.
- No execution authorized by this document.

## 2. Motivation

The current ladder workflow in this repo starts from boundary-adjacent starts
and extends forward. That geometry may bias interpretation because the anchor is
effectively born with little or no usable past.

This document records an exploratory alternative whose purpose is not to repair
PR003 retroactively, but to distinguish:

- intrinsic geometric structure of the causal set;
- from boundary-conditioned artifacts induced by starts with no effective past.

The motivating concern is that a peel-off or adherence signal measured from a
boundary start may partly reflect one-sided anchoring rather than a more
intrinsic bilateral causal structure.

## 3. Physical Question

Given a present point `p`, does the local causal structure around `p` show
symmetry, asymmetry, return behavior, or a limiting geometric transition when
the past cone and future cone are compared without privileging boundary starts?

This is the binding question for this preregistration. It replaces the
boundary-seeded reading

- "does a ladder launched from near the boundary peel off?"

with the bilateral point-anchored reading

- "does the causal structure around a single present event reorganize in a
  nontrivial way when its past and future cones are compared?"

## 4. Definition of "Present"

### Primary definition

`PRESENT_POINT = p`

A single causal-set element `p` chosen without embedding leakage, used as the
common vertex of two opposite causal cones.

Derived objects:

- `PAST_CONE(p) = C^-(p) = {x : x ≺ p}`
- `FUTURE_CONE(p) = C^+(p) = {y : p ≺ y}`

Forbidden interpretation:

- the present must not be treated as a spatial slice;
- the present must not be treated as a thickened antichain;
- the present must not be treated as a launch boundary;
- the present must not be treated as an extended hypersurface;
- unless a future diagnostic variant explicitly declares such a construction as
  a separate non-primary object.

This point-like definition is primary and binding. Any broader object must be
treated as a secondary diagnostic variant, not as "the" present of this
experiment.

### Secondary diagnostic variants

These variants may be explored later, but they are not interchangeable with the
primary point definition and must never overwrite it retroactively.

#### A. Rung-like diagnostic anchor

A rung `(p, q)` used as a present anchor, analogous to the current ladder
grammar but explicitly not chosen from a boundary start.

#### B. Local causal diamond diagnostic anchor

A small finite causal nucleus `P` or diamond-like local subposet, used as the
present anchor for bilateral extension counts and stability diagnostics.

#### C. Operational finite-window diagnostic anchor

A finite causal window defined by an order-only operational rule, intended to
approximate a present slice or local present neighborhood without claiming a
literal hypersurface.

These variants are inherited as faithfully as possible from
[experimento_presente.md](/home/ignac/nachocausal/experimento_presente.md:1),
but their role here is explicitly subordinate to the point-present definition.

## 5. Observable

The experiment is not authorized to run yet. This section defines what would be
measured in a future execution.

### Primary observables

- `past_crossing_fraction`
  - fraction of present-anchored probes on `C^-(p)` whose diagnostic crosses the
    selected threshold.
- `future_crossing_fraction`
  - fraction of present-anchored probes on `C^+(p)` whose diagnostic crosses the
    selected threshold.
- `past_return_fraction`
  - fraction of past-cone probes whose signal crosses and later returns.
- `future_return_fraction`
  - fraction of future-cone probes whose signal crosses and later returns.
- `past_future_asymmetry`
  - frozen asymmetry statistic comparing matched past/future diagnostics around
    the same anchor `p`.
- `cone_depth_dependence`
  - dependence of the signal on depth inside `C^-(p)` and `C^+(p)`.
- `boundary_distance_control`
  - dependence of the bilateral signal on distance from `p` to boundary-like
    proxies.

Binding caution:

- "bilateral" or "symmetric" comparison does not imply an expectation of exact
  numerical equality between past and future observables.
- finite-window effects, horizons, temporal orientation, and boundary
  truncation may generate genuine or artifact-induced asymmetry.
- the role of the paired observables is to measure that asymmetry explicitly,
  not to assume it away.

### Secondary diagnostic observables

- past crossing depth distribution;
- future crossing depth distribution;
- number of past crossings / oscillations;
- number of future crossings / oscillations;
- dependence on present definition variant;
- dependence on trajectory length cutoff;
- dependence on density / intensity;
- number of compatible chains entering `p`;
- number of compatible chains leaving `p`;
- local balance `|C^+(p)| - |C^-(p)|`;
- local ratio `|C^+(p)| / max(1, |C^-(p)|)`.

The distinction is binding: secondary diagnostics may explain behavior but may
not be used post hoc to rescue a failed primary reading.

## 6. Allowed Inputs

Before any execution, the following classes of inputs may be chosen and frozen:

### Geometric inputs

- rule for selecting the present point `p`;
- matching rule for comparing `C^-(p)` against `C^+(p)`;
- finite window size if variant C is used;
- any order-only locality constraint used to define the anchor.

Anchor-selection status must be declared explicitly:

- `GEOMETRY_ASSISTED` if `p` is selected using embedding coordinates or any
  hidden geometric information;
- `ORDER_ONLY` if `p` is selected using only internal order-theoretic criteria.

This distinction is binding. A geometry-assisted anchor may support a controlled
diagnostic comparison, but it must not be presented as evidence of order-only
recoverability.

### Sampling inputs

- seed list or seed family rule;
- intensity / density grid;
- number of repetitions per setting.

### Trajectory-selection inputs

- minimum trajectory length cutoff;
- bilateral extension depth budget;
- crossing threshold definition, if changed from the current exploratory
threshold, provided it is frozen before execution.

### Comparison inputs

- boundary-distance control variable;
- comparison surface against the existing boundary-start workflow.

No parameter in these classes may be tuned after inspecting outcomes.

## 7. Forbidden Inputs / Forbidden Adaptivity

Forbidden:

- choosing the present after looking at successful outcomes;
- replacing the point-present definition with an antichain or slice after
  seeing results;
- presenting a geometry-assisted choice of `p` as if it were an order-only
  selection;
- moving thresholds to rescue percentages;
- comparing only favorable runs;
- redefining the present variant after observing results;
- changing the question from "does the signal survive?" to "does any signal
  exist?" after a failure;
- reinterpreting a failure as a success by changing the target observable;
- selecting only trajectory lengths that make the conclusion look cleaner.

This document forbids adaptive reinterpretation of a failed design.

## 8. Hypotheses

### H0_boundary_artifact

The main signals observed in boundary-start experiments weaken or disappear once
the analysis is re-anchored on a single present point with usable past and
future cones.

### H1_intrinsic_geometric_signal

Matched diagnostics on `C^-(p)` and `C^+(p)` show a reproducible bilateral
structure that is not reducible to boundary-start artifacts alone.

### H2_mixed_regime

Part of the signal was boundary-conditioned, but part survives as an intrinsic
geometric structure once the anchor is moved to a single present point and its
paired cones.

These hypotheses are qualitative and exploratory. They do not authorize
over-claim language about proof, universality, or horizon reconstruction.

They also do not authorize treating a successful geometry-assisted anchor
selection as evidence that the same present point is recoverable from the order
alone.

## 9. Relation to PR003 / K-beam

This preregistration inherits the conceptual concern from PR003 / K-beam:

- ladder adherence and peel-off are meaningful diagnostics;
- branching and stability matter;
- boundary anchoring may strongly affect interpretation.

What changes:

- anchor selection moves from boundary start to a present point `p`;
- the geometry becomes `C^-(p)` versus `C^+(p)`, not just future-directed;
- the primary interpretation becomes bilateral asymmetry / symmetry around an
  event rather than unilateral peel-off from a boundary seed.

This document does not invalidate PR003, does not confirm PR003, and does not
replace PR003 / K-beam. It only defines a separate exploratory line whose
results would need independent interpretation.

## 10. Future Table

| run_id | present_definition | intensity | min_length | n_trajectories | past_crossing_fraction | future_crossing_fraction | past_return_fraction | future_return_fraction | past_future_asymmetry | cone_depth_dependence | boundary_distance_control | qualitative_verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Any future execution table should also record whether the anchor rule was
`GEOMETRY_ASSISTED` or `ORDER_ONLY`.

## 11. Forbidden Claims

Even if the future experiment looks favorable, this preregistration forbids
claiming:

- horizon reconstruction;
- uncertainty principle demonstrated;
- universality;
- complete independence from boundary effects;
- validity outside the toy model;
- publishable evidence without additional controls.

This document records an exploratory design only.

## 12. Minimal Next Action

The next minimal permitted action is:

design a parameter table before executing anything.

No execution is authorized by this document.
