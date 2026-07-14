# PR010 Reference Depth-Coverage Decision

STATUS: DECISION_ONLY
SCOPE: NEW_PHASE / COVERAGE_DESIGN / NO_EXECUTION_AUTHORIZATION
RELATION_TO_PR009: SUCCESSOR_WITHOUT_DATA_REUSE

## Decision

Open PR010 to redesign reference coverage for a future effective-expansion test. PR010
addresses a statistical-design problem, not a performance problem and not a PR009
scientific result.

PR010 begins from only the public contract-level fact that PR009 terminated before
publication because its preregistered reference-MINK coverage requirement was not met at
depth 7. No unpublished PR009 value is an admissible PR010 input.

## Phase 1: Development Coverage Study

Use a completely new development seed band to study only order-side coverage by depth.
This phase may measure whether a slice supplies an evaluable transition and may aggregate
those coverage indicators by depth, seed, and spacetime kind.

It must not:

- reuse any PR009 seed;
- recover, inspect, or reconstruct unpublished PR009 rows;
- compute or inspect horizon zones, radii, contrasts, signs, effect sizes, or terminal
  statistics;
- optimize enclosing-diamond separation further;
- present development coverage as confirmatory evidence.

The development study requires its own written protocol before execution, including a
new seed band, exact row unit, allowed coverage fields, output boundary, and stopping
rule. This decision does not choose those values and does not authorize that run.

## Mandatory Design Fork

Before a new confirmatory preregistration is frozen, PR010 must make one explicit choice:

1. increase the reference block enough to support the intended depth range; or
2. limit the depths that are eligible for scoring under a coverage rule fixed before
   confirmatory data exist.

The choice must be based only on the new PR010 development coverage study and principled
resource/statistical arguments. It may not be calibrated to a desired scientific label.
Hybrid or adaptive switching after confirmatory execution is forbidden.

## Confirmatory Boundary

After the fork is decided, PR010 must create:

- a new preregistration;
- a new, disjoint confirmatory seed band not used in PR009 or PR010 development;
- a new implementation and leakage/data-contract audit;
- an explicit `PASS_READY_TO_RUN` gate;
- separate authorization for the confirmatory execution.

The new preregistration must freeze the reference/evaluation order, coverage minimums,
scorable depths, terminal precedence, artifact separation, and failure behavior before
any confirmatory seed is generated.

## Claim Boundary

PR010 is currently a design phase only. It makes no claim about effective expansion,
horizon sensitivity, trapping, or the scientific viability of the PR009 observable.
The PR009 terminal remains exactly `FAILED_DATA_CONTRACT`.
