# PR007-A H_hat Robustness Closure Decision

STATUS: DECISION_ONLY
SCOPE: CLOSURE / NO_CODE / NO_EXPERIMENTS
RELATION_TO_PR007_A: AFTER_ROBUST_FIXED_K_H_HAT_SIGNAL

## Decision

PR007-A upgrades PR006 from a replicated fixed-K scalar localization signal to a
seed/density-robust fixed-K scalar order-only signal under the preregistered PR007-A
protocol.

It does not establish radial localization, K-invariance, a physical barrier, or
geometric horizon reconstruction.

## Established By PR007-A

PR007-A terminal label:

```text
ROBUST_FIXED_K_H_HAT_SIGNAL
```

Validated summaries:

- `H_hat_block = 4`;
- `cell_fraction_H4 = 1.0`;
- `intensity_median_drift = 0`;
- all seed-group medians are `4`;
- all intensity-group medians are `4`;
- data contract passed;
- seal state was preserved.

## Allowed Interpretation

The allowed interpretation is:

```text
The fixed-K order-only scalar estimator H_hat remains robust over the preregistered
seed and intensity/density grid tested in PR007-A.
```

## Disallowed Interpretation

PR007-A must not be described as:

- horizon reconstruction;
- radial localization;
- K-invariant barrier evidence;
- a physical barrier claim;
- general Schwarzschild 3+1D reconstruction;
- evidence over untested nuisance axes such as patch size, `M`, or `MAX_STARTS`.

## Next Decision Boundary

No further PR007 run is authorized by this closure.

The next step must be a separate decision choosing one of:

- PR007-B: preregistered nuisance-axis expansion requiring contract/CLI review for patch
  size, `M`, or `MAX_STARTS`;
- PR008: baseline and leakage audit for the fixed-K `H_hat` estimator.

Any such step must be separately preregistered before execution.
