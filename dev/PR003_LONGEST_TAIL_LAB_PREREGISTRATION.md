# PR-003 Longest-Tail Laboratory Preregistration

## Status

LAB_STATUS: PRIVATE_EXPLORATORY
PAPER_I_SCOPE: OUT_OF_SCOPE_FROZEN
NO_EXECUTION_IN_THIS_PREREGISTRATION: YES

This document preregisters a future exploratory laboratory follow-up for PR-003
`LONGEST_TAIL`. It is not a Paper I artifact, not a sealed validation result,
not a public claim, and not an execution log. No new sweep, simulation, data
generation, or analysis execution is authorized by this document alone.

## Scope Boundary

This preregistration concerns only the private PR-003 laboratory question:

- `LONGEST_TAIL_PHYSICAL_CONVERGENCE`
- `LONGEST_TAIL_SCALING_EXPONENT`

The scope is limited to deciding, in a future execution not performed here,
whether the longest-ladder tail distance converges in physical units, stabilizes
at a positive finite value, grows, or remains unresolved.

Paper I is out of scope and frozen. It must not be used as context,
justification, comparison, or documentary destination for this follow-up. This
document also does not open Paper II or any general theoretical program.

## Existing Evidence

CANONICAL_EXISTING_ARTIFACT: dev/PR003_NEAR_HORIZON_NOTES.md

The initial existing 3-density table is:

```text
intensity / ell / tail_d_perp_over_ell / physical_d_perp_tail
3600  / 0.0447 / 4.37 / 0.1953
7200  / 0.0316 / 6.17 / 0.1950
14400 / 0.0224 / 7.56 / 0.1693
```

Existing interpretation before this preregistration:

```text
LONGEST_TAIL_PHYSICAL_CONVERGENCE=UNRESOLVED
LONGEST_TAIL_SCALING_EXPONENT=-0.103012
EXPONENT_STATUS=DESCRIPTIVE_ONLY_N3
ROUTE_IMPLICATION=UNRESOLVED_KEEP_PR003_OPEN
```

The same canonical artifact contains a later exploratory extension to five
densities, including `21600` and `28800`.

```text
EXISTING_5_DENSITY_EXTENSION_STATUS: EXISTING_EXPLORATORY_NOT_PREREGISTERED
```

That extension may motivate this future preregistered follow-up, but it must
not be treated as preregistered evidence or converted into a closed claim.

## Existing Limitations

The existing 3-density evidence is insufficient to distinguish slow decay,
finite plateau, physical growth, or unresolved behavior.

The 5-density extension is existing exploratory evidence, but it is post-hoc
relative to this preregistration. It cannot be used as if it were executed under
this preregistered protocol.

No canonical per-seed uncertainty for the primary observable
`physical_d_perp_tail` is available from the existing artifact. Existing sweep
summaries are pooled over ladders, and pooled-ladder dispersion is not a
substitute for per-seed uncertainty.

Completeness/censoring is not fully resolved for the 5-density extension,
including the higher-density levels `21600` and `28800`.

## Physical Question

For the PR-003 bracket-seeded LONGEST ladder selector, does the tail distance
from the horizon converge toward zero in physical units as density increases,
stabilize at a positive finite physical limit, grow in physical units, or remain
empirically unresolved?

## Primary Observable

The primary observable for any future decision is:

```text
physical_d_perp_tail = ell * tail_d_perp_over_ell
```

This value must be computed per seed first, then summarized across seeds at each
density. The primary decision must be based on `physical_d_perp_tail`, not on
`tail_d_perp_over_ell` alone.

## Secondary Observables

Secondary observables are:

- `tail_d_perp_over_ell` as discrete/operational cost.
- Search completeness/censoring status or fraction.
- Ladder count per seed.
- First-3/head `d_perp/ell` for context only.
- Direction metrics, if produced by an existing future runner, for context only.

Secondary observables may explain operational behavior but may not override the
primary physical decision.

## Units and Scaling Variable

The primary unit is physical `d_perp_tail`.

The secondary operational unit is discreteness-scale distance,
`tail_d_perp_over_ell`.

The scaling variable is `ell -> 0`, equivalently increasing `intensity` at fixed
physical patch geometry and fixed `t_edge`. Where density notation is used,
`ell` is interpreted by the existing convention as the inverse square root of
the density scale.

## Future Density Grid Requirement

A future execution must preregister at least five density levels before running.
A stable power-law interpretation is forbidden with fewer than five
preregistered densities.

If computationally feasible, seven preregistered density levels are preferred.
Exact future intensity values are not fixed by this document and remain
`PROPOSED_NOT_VERIFIED` until explicitly frozen before execution.

The existing 5-density exploratory extension cannot satisfy this requirement
retroactively.

## Future Seed Requirement

A future execution must use at least 20 seeds per density. A 40-seed design is
preferred because `dev/measure_pr003.py` documents a per-sprinkling aggregation
precedent over 40 `EXPLORE_POOL` seeds.

Fewer than 20 seeds per density forces `UNRESOLVED` or `DESCRIPTIVE_ONLY`.

## Future Data Required

For each future density and seed, the execution must record enough information
to compute or audit:

- intensity
- ell
- tail_d_perp_over_ell
- physical_d_perp_tail
- ladder count
- finite/NaN status
- completeness/censoring status or fraction

Exact future file paths, flags, functions, and column names are
`PROPOSED_NOT_VERIFIED` until implemented or selected from existing tooling in a
separate future step.

## Future Uncertainty Required

Each density must report uncertainty across seeds for the primary observable.
Minimum required summaries are:

- median across seeds
- IQR or MAD across seeds
- a nonparametric confidence interval across seeds

Pooled-ladder uncertainty is insufficient for physical convergence, plateau, or
growth decisions.

## Completeness and Censoring Requirement

Future execution must report search completeness/censoring for each density.
If the longest search is censored or budget-limited, the result must identify
whether the reported tail is a complete-search value or a lower-bound/censored
quantity.

Where possible, complete-only and all-ladder summaries must be compared. If
high-density completeness/censoring remains unresolved, the decision must be
`LONGEST_TAIL_PHYSICAL_CONVERGENCE=UNRESOLVED`.

## Allowed Descriptive Models

Allowed descriptive models for future preregistered analysis are:

- zero-limit slow decay: `d(ell) = A * ell^alpha, alpha > 0`
- finite plateau: `d(ell) = c + A * ell^alpha, c > 0`
- local monotone trend / pairwise effective exponents
- physical growth trend in `d_perp_tail` as `ell -> 0`

All fitted exponents remain descriptive unless the density grid, seed
uncertainty, and model-comparison requirements below are satisfied.

## Forbidden Inferences

Forbidden inferences:

- Accepting a stable power law with fewer than five preregistered densities.
- Accepting physical convergence without per-seed uncertainty.
- Accepting a finite plateau without comparing against slow decay.
- Accepting physical non-convergence solely because `tail_d_perp_over_ell`
  grows.
- Treating the existing 5-density extension as preregistered.
- Converting exploratory or post-hoc evidence into a public or sealed claim.
- Using Paper I to reinterpret PR-003.
- Opening Paper II or a general theoretical program from this follow-up.

Growth of `tail_d_perp_over_ell` must be reported as discrete/operational cost.
It is not, by itself, physical divergence.

## Preregistered Decision Criteria

`LONGEST_TAIL_PHYSICAL_CONVERGENCE=LIKELY_YES_EXPLORATORY`

Allowed only if all of the following hold:

- at least five densities were preregistered before execution;
- per-seed uncertainty is available at each density;
- `physical_d_perp_tail` is compatible with decay toward zero;
- the zero-limit slow-decay model is preferred over a finite plateau;
- the qualitative conclusion is stable under leave-one-density-out checks;
- completeness/censoring does not block interpretation.

`LONGEST_TAIL_PHYSICAL_CONVERGENCE=PLAUSIBLE_FINITE_LIMIT_EXPLORATORY`

Allowed only if all of the following hold:

- at least five densities were preregistered before execution;
- per-seed uncertainty is available at each density;
- the finite-plateau model is explicitly compared against slow decay;
- the plateau `c` is positive and stable;
- uncertainty for `c` excludes zero;
- completeness/censoring does not block interpretation.

`LONGEST_TAIL_PHYSICAL_CONVERGENCE=NO_EVIDENCE_OF_CONVERGENCE`

Allowed only if `physical_d_perp_tail` grows with density or is incompatible
with both zero-limit decay and finite plateau under per-seed uncertainty.
Growth of `tail_d_perp_over_ell` alone is insufficient.

`LONGEST_TAIL_PHYSICAL_CONVERGENCE=UNRESOLVED`

Mandatory if any of the following hold:

- fewer than five densities were preregistered;
- per-seed uncertainty for `physical_d_perp_tail` is absent;
- completeness/censoring is unresolved;
- zero-limit decay and finite plateau are indistinguishable;
- grid, seed, or model choices were made post-hoc;
- the only negative signal is growth in `tail_d_perp_over_ell`.

`LONGEST_TAIL_SCALING_EXPONENT` may be reported as a physical exponent only if
the relevant model is accepted under the criteria above. Otherwise it must be
reported as `DESCRIPTIVE_ONLY` or `UNRESOLVED`.

## Route Implication Criteria

`QUANTITATIVE_BOUND_ROUTE_FAVORED`

Allowed only if future preregistered execution favors decay toward zero or a
small finite upper bound with per-seed uncertainty and resolved
completeness/censoring.

`NON_IDENTIFIABILITY_ROUTE_FAVORED`

Allowed only if future preregistered execution favors a positive physical
plateau or physical growth incompatible with zero-limit convergence under
per-seed uncertainty.

`UNRESOLVED_KEEP_PR003_OPEN`

Required if slow decay and plateau remain indistinguishable, censoring remains
unresolved, per-seed uncertainty is absent, or the evidence remains exploratory
or post-hoc.

## Blocking Conditions Before Execution

Execution is blocked until all of the following are fixed before running:

- density grid;
- seed count and seed-selection rule;
- primary per-seed output plan;
- uncertainty summaries;
- completeness/censoring summaries;
- order-only construction and scoring-only use of hidden coordinates;
- treatment of the existing 5-density extension as exploratory background only.

Any attempt to seed, select, truncate, or tune ladders using hidden coordinates
blocks execution.

## Expected Future Artifacts

Expected future artifacts are not created by this preregistration. They remain
`PROPOSED_NOT_VERIFIED` until a later authorized step:

- a per-seed primary table;
- a density-level aggregate table;
- a completeness/censoring report;
- a decision note that preserves exploratory status.

## Forbidden Future Actions

Forbidden future actions:

- executing sweeps before this preregistration is accepted as the governing
  laboratory protocol;
- executing simulations in the same step as creating this document;
- modifying Paper I or sending results there;
- changing code or data without a separate authorization;
- treating post-hoc exploratory values as preregistered;
- publishing a claim from this laboratory evidence;
- changing the ladder selection rule after inspecting `physical_d_perp_tail`.

## Caveats

This document freezes a laboratory analysis design, not a result. It does not
validate any existing exploratory extension. It does not certify an exponent,
plateau, convergence, or non-convergence.

The future primary decision is physical. The ell-unit longest-tail growth is an
operational cost that must be reported, but it cannot alone decide physical
non-convergence.

## Execution Status

NO_EXECUTION_IN_THIS_PREREGISTRATION: YES
NO_NEW_SWEEPS_EXECUTED: YES
NO_SIMULATIONS_EXECUTED: YES
NO_DATA_GENERATED: YES
NO_CODE_MODIFIED_BY_THIS_PREREGISTRATION: YES
FUTURE_EXECUTION_STATUS: NOT_PERFORMED
