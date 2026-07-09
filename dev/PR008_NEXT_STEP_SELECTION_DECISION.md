# PR008 Next-Step Selection Decision

STATUS: DECISION_ONLY
SCOPE: NEXT_STEP_SELECTION / NO_CODE / NO_EXPERIMENTS / NO_NEW_RUNS
RELATION_TO_PR007_A: AFTER_CLOSURE_DECISION

## Decision

Choose Option B:

```text
PR008 = baseline comparison + leakage audit for the existing fixed-K H_hat result.
```

Do not proceed to Option A (`PR007-B`) yet.

## Reason

PR006 validated the fixed-K order-only scalar estimator `H_hat`.

PR007-A validated seed/density robustness for that estimator under a preregistered grid.

The next minimal auditable risk is not another robustness axis. The next minimal risk is
whether the existing `H_hat` result is:

- stronger than explicit baseline comparators;
- free of ground-truth leakage;
- insulated from radial, shell, straddle, horizon-side, or reporting-path contamination;
- defensible before any movement toward a Schwarzschild 3+1D claim.

PR007-B would require contract/CLI review for patch size, `M`, or `MAX_STARTS`, and could
expand the robustness surface before the estimator has passed baseline and leakage
scrutiny. That is not the minimal next step.

## Authorized Scope

This decision authorizes only the direction:

```text
Draft a PR008 preregistration for baseline comparison and leakage audit.
```

This decision does not authorize:

- code edits;
- experiments;
- new runs;
- PR007-B;
- changes to `K_REF`;
- multi-K aggregation;
- patch-size, `M`, or `MAX_STARTS` variation;
- publication claims;
- horizon reconstruction claims;
- radial localization claims;
- physical barrier claims.

## Required PR008 Preregistration Content

The next PR008 preregistration must freeze:

1. baseline comparator definitions;
2. leakage channels to audit;
3. exact input artifacts;
4. exact output paths;
5. read-only inspections versus executable checks;
6. data contract for any generated audit table;
7. terminal labels;
8. stop rule against adding baselines or leakage probes after seeing results.

## Closure Statement

PR007-A is closed as seed/density robustness for fixed-K `H_hat`.

The next minimal auditable step toward a defensible Schwarzschild 3+1D result is PR008:
baseline comparison plus leakage audit of the existing fixed-K order-only scalar signal.
