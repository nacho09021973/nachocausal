# PR008 H_hat Baseline and Leakage Audit Closure Decision

STATUS: CLOSED
TERMINAL_LABEL: BASELINE_DOMINATED
SCOPE: DIAGNOSTIC_CLOSURE / NO_NEW_RUNS

## Decision

Close PR008 as the diagnostic audit of the existing fixed-`K` `H_hat` observable.
PR008 is not evidence that `H_hat` can reconstruct a Schwarzschild horizon in 3+1D.

The frozen production run completed with:

```text
h_hat_cell_agreement_with_H4 = 1.0
max_baseline_cell_agreement_with_H4 = 1.0
delta_agreement = 0.0
H_hat_block = 4
cell_fraction_H4 = 1.0
terminal_label = BASELINE_DOMINATED
```

The empirical PR006 block and intensity baselines reproduce `H=4` in every PR007-A
evaluation cell. Therefore the audited result does not establish estimator-specific
signal beyond the preregistered baselines.

## Implementation Closure

The implementation contract is closed by:

- the frozen preregistration and implementation plan;
- the production auditor;
- 76 isolated contract, failure-path, publication, and terminal-label tests;
- a valid paired CSV/report publication with matching run, configuration, and input
  provenance fingerprints;
- zero counts for every frozen data-contract failure class;
- a single production execution over the frozen PR006 and PR007-A artifacts.

No PR008 rerun is authorized merely to seek a different terminal result. The valid
published pair is the normative output.

## Scientific Interpretation

The result is negative but informative. Within the audited scope, `H_hat` behaves as a
depth-derived observable that is matched by simpler empirical baselines. This does not
prove that every peel-off statistic is trivial, nor that no order-only horizon-sensitive
observable exists. It does show that the present fixed-`K` scalar has not demonstrated
independent horizon information.

`H_hat` may remain only as:

- a diagnostic auxiliary;
- a component candidate inside a demonstrably richer observable;
- a serious baseline for future order-only observables.

It is not retained as the primary route to horizon reconstruction.

## Stop Decision

Do not open another campaign that only tunes the same information channel through:

- additional `K` optimization;
- new beam-search optimizers;
- alternative loss functions;
- incremental fit-score improvements;
- greater beam-search complexity.

Any future reuse of `H_hat` must compare against the frozen PR008 baselines and must not
weaken this closure.

## Next Research Front

Move the active observable-design front to:

```text
new order-only observable sensitive to expansion or trapping
```

Candidate families may use beam, expansion, or causal-entropy structure, but each must
declare its information channel and leakage guard before evaluation. PR008 supplies a
baseline and a stopping result, not a 3+1D reconstruction claim.

## Evidence

- `dev/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_PREREGISTRATION.md`
- `dev/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_IMPLEMENTATION_PLAN.md`
- `dev/audit_pr008_h_hat_baseline_leakage.py`
- `tests/test_pr008_h_hat_baseline_leakage.py`
- `data/reports/pr008_h_hat_baseline_leakage_audit.csv`
- `data/reports/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_REPORT.md`
