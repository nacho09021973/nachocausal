# PR008 H_hat Baseline and Leakage Audit Decision

STATUS: DECISION_ONLY
SCOPE: NEXT_DIRECTION / NO_CODE / NO_EXPERIMENTS
RELATION_TO_PR007_A: NEXT_STEP_AFTER_ROBUST_FIXED_K_H_HAT_SIGNAL

## Decision

PR008 will be a baseline and leakage audit for the fixed-K `H_hat` estimator.

This is the next natural step before any further robustness expansion or any movement
toward a defensible Schwarzschild 3+1D claim.

## Rationale

PR006 validated a fixed-K order-only scalar estimator:

```text
H_hat_block = 4
```

PR007-A validated seed/density robustness under the preregistered grid:

```text
ROBUST_FIXED_K_H_HAT_SIGNAL
```

The next risk is not another unmotivated seed or density grid. The next risk is whether
the `H_hat` signal is genuinely estimator-specific and leakage-clean relative to explicit
baselines and forbidden ground-truth channels.

## PR008 Question

Does the fixed-K order-only scalar estimator `H_hat` remain meaningful after a
preregistered audit of:

- baseline comparators;
- leakage paths;
- forbidden ground-truth dependence;
- implementation/reporting routes that could allow radial, shell, straddle, or
  horizon-side information to affect the estimator or terminal label?

## Scope Boundaries

PR008 does not authorize:

- code edits;
- new experiments;
- additional PR007 runs;
- patch-size, `M`, or `MAX_STARTS` variation;
- multi-K aggregation;
- publication claims;
- horizon reconstruction claims;
- radial localization claims;
- K-invariance or physical-barrier claims.

## Required Future Preregistration Content

Before any PR008 execution, a separate preregistration must freeze:

1. baseline comparator definitions;
2. leakage channels to audit;
3. exact input files and output paths;
4. permitted read-only inspections versus executable checks;
5. data contract for any generated audit table;
6. terminal labels;
7. stop rule against adding baselines or leakage probes after seeing results.

## Allowed Claim Shape

If PR008 eventually passes, the allowed claim shape is:

```text
The fixed-K order-only scalar estimator H_hat survived the preregistered baseline and
leakage audit within the audited PR008 scope.
```

The disallowed claim shape remains:

```text
H_hat reconstructs the geometric horizon, proves radial localization, or establishes a
K-invariant physical barrier.
```
