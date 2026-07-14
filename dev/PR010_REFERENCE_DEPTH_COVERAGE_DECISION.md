# PR010 Reference Depth-Coverage Decision

STATUS: DECISION_ONLY
DESIGN_STATUS: FROZEN_FOR_AUDIT
SCOPE: NEW_PHASE / COVERAGE_DESIGN / NO_EXECUTION_AUTHORIZATION
RELATION_TO_PR009: SUCCESSOR_WITHOUT_DATA_REUSE

## Decision

Open PR010 to redesign reference coverage for a future effective-expansion test. PR010
addresses a statistical-design problem, not a performance problem and not a PR009
scientific result.

PR010 begins from only the public contract-level fact that PR009 terminated before
publication because its preregistered reference-MINK coverage requirement was not met at
depth 7. No unpublished PR009 value is an admissible PR010 input.

## Scientific Depth Window

Freeze the only transitions eligible for a future PR010 scientific score as:

```text
depth_k = {3, 4, 5}
```

These are three consecutive transitions after the algorithmic memory `M = 3`. They are
the minimum window adopted by PR010 for observing evolution and minimal local stability.
Computing the transition at `depth_k = 5` requires the slice at depth 6, so the required
slice set is exactly:

```text
required_slices = {3, 4, 5, 6}
```

This window is a new methodological decision. It is not asserted as a conclusion of the
literature and is not selected in reaction to the PR009 failure at depth 7. No depth
outside `{3, 4, 5}` may enter a future PR010 scientific score.

## Development Coverage Study

Freeze the development configuration as:

```text
DEVELOPMENT_SEEDS = 1101000..1101023
N_DEVELOPMENT_SEEDS = 24
SPACETIME_KINDS = BH,MINK
INTENSITY = 4800
M = 3
K = 64
MAX_STARTS = 40
REQUIRED_SLICES = 3..6
```

Every development seed is used for both `BH` and `MINK`. Development measures only
order-side coverage by depth.

The independent coverage unit is exactly:

```text
(seed, spacetime_kind, depth_k)
```

Starts are nested within a seed and are not independent units. A seed-kind-depth unit is
supported if and only if at least five emitted starts have an evaluable transition at that
depth:

```text
seed_depth_supported = (n_transition_evaluable_starts >= 5)
```

The development output schema contains exactly these fields, in this order:

```text
seed
spacetime_kind
depth_k
n_emitted_starts
n_transition_evaluable_starts
seed_depth_supported
```

There is exactly one row per independent unit for all 24 seeds, both spacetime kinds, and
`depth_k in {3,4,5}`. `n_emitted_starts` is an integer in `0..40`;
`n_transition_evaluable_starts` is an integer in `0..n_emitted_starts`; and
`seed_depth_supported` is the exact Boolean predicate above.

It must not:

- reuse any PR009 seed;
- recover, inspect, or reconstruct unpublished PR009 rows;
- compute or inspect horizon zones, radii, contrasts, signs, effect sizes, or terminal
  statistics;
- emit widths, `theta` values, or any other statistic outside the six-field coverage
  schema;
- optimize enclosing-diamond separation further;
- present development coverage as confirmatory evidence.

The development study still requires a separately reviewed implementation and exact
artifact/publication protocol before execution. This decision does not authorize that
run.

## Resolved Design Fork

The fork is resolved permanently as:

```text
LIMIT_SCORABLE_DEPTHS
```

PR010 will not enlarge its frozen confirmatory reference block in response to development
or confirmatory coverage. If the fixed window `{3,4,5}` is not viable under the rule
below, the design terminates as infeasible. Hybrid, adaptive, or post-execution switching
to a larger reference block is forbidden.

## Mechanical Coverage and Infeasibility Rule

For each of the six cells in:

```text
spacetime_kind x depth_k = {BH,MINK} x {3,4,5}
```

let `x` be the number of supported independent seed units among the 24 development seeds.
Define `L_90(x;24)` as the exact one-sided 90% Clopper-Pearson lower confidence bound for
the support probability. The convention is:

```text
L_90(0;24) = 0
L_90(x;24) = BetaQuantile(0.10; x, 25-x)  for x > 0
```

where `BetaQuantile(q; a, b)` is the lower `q` quantile of the `Beta(a,b)` distribution.
Using only this lower bound, both inequalities must hold for every cell:

```text
P[Binomial(24, L_90) >= 12] >= 0.95
P[Binomial(12, L_90) >= 8] >= 0.90
```

The binomial tails are inclusive exact upper tails. The counts 24 and 12 represent
independent seeds, never starts or transition rows. The two inequalities and all six
cells are conjunctive; no multiplicity averaging, cell pooling, rounding rescue, or
spacetime/depth substitution is allowed.

If either inequality fails in any cell, the only design terminal is:

```text
PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE
```

That terminal forbids a confirmatory preregistration for this PR010 design. Development
may not be extended, repeated, or supplemented to reverse it.

## Reserved Confirmatory Seeds

Freeze the confirmatory bands as:

```text
REFERENCE_SEEDS = 1102000..1102023
N_REFERENCE_SEEDS = 24
EVALUATION_SEEDS = 1103000..1103011
N_EVALUATION_SEEDS = 12
```

These bands are disjoint from PR009 and from PR010 development. They are reserved only;
this decision does not authorize generating, inspecting, or scoring them. They may not be
expanded, shortened, replaced, or supplemented.

## Computational Budget

Freeze the complete development-run budget as:

```text
processes = 1
threads <= 4
aggregate_cpu_time <= 4 CPU-hours
wall_time <= 60 minutes
peak_resident_memory <= 1 GiB
development_seeds = 24
```

Aggregate CPU time is user plus system CPU time across the process and all its threads.
Peak resident memory is the maximum resident set size of the development process. Any
limit breach is a fail-closed operational failure: terminate the process, remove temporary
artifacts, publish no final development artifact, and do not use partial results to revise
`LIMIT_SCORABLE_DEPTHS` or to decide coverage viability.

## Confirmatory Boundary

Only if every development coverage cell passes may PR010 create:

- a new preregistration;
- the already-reserved, disjoint confirmatory seed bands frozen above;
- a new implementation and leakage/data-contract audit;
- an explicit `PASS_READY_TO_RUN` gate;
- separate authorization for the confirmatory execution.

The new preregistration must freeze the reference/evaluation order, coverage minimums,
scorable depths, terminal precedence, artifact separation, and failure behavior before
any confirmatory seed is generated.

This design decision does not authorize code, the development run, a confirmatory
preregistration, or any confirmatory execution. The immediate next gate is a read-only
design audit of this file.

## Claim Boundary

PR010 is currently a design phase only. It makes no claim about effective expansion,
horizon sensitivity, trapping, or the scientific viability of the PR009 observable.
The PR009 terminal remains exactly `FAILED_DATA_CONTRACT`.
