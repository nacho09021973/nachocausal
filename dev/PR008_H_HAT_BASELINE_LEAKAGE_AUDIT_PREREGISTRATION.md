# PR008 H_hat Baseline and Leakage Audit - Preregistration Draft

STATUS: PREREGISTRATION_DRAFT
VALIDATION_STATUS: NOT_RUN
SCOPE: PREREG_ONLY / NO_CODE / NO_EXPERIMENTS / NO_VALIDATION_AUTHORIZED
RELATION_TO_PR007_A: BASELINE_AND_LEAKAGE_AUDIT_AFTER_ROBUST_FIXED_K_H_HAT_SIGNAL

## 1. Question

Does the fixed-K order-only scalar estimator `H_hat` remain meaningful after a
preregistered audit of:

- baseline comparators;
- leakage paths;
- forbidden ground-truth dependence;
- reporting routes that could allow non-order-only information to affect the estimator
  or terminal label?

PR008 is an audit of the existing `H_hat` result. It is not a new robustness run, not a
new estimator, not a horizon reconstruction, and not a publication claim.

## 2. Frozen Estimator Under Audit

PR008 audits the existing PR006/PR007-A estimator only:

```text
first_empty_depth(sequence) =
  the smallest depth_k in [1, 25] with slice_status = EMPTY,
  or 26 if no EMPTY slice occurs in [1, 25].

H_hat(seed, intensity) =
  lower median over start_id of first_empty_depth(seed, intensity, start_id, K_REF).

H_hat_block =
  lower median over (seed, intensity) of H_hat(seed, intensity).
```

Frozen inherited constants:

- `K_REF = 8`;
- `MAX_DEPTH = 25`;
- `NO_EMPTY_SENTINEL = 26`;
- lower-median rule unchanged.

PR008 may not change this estimator.

## 3. Leakage Definition

For PR008, leakage means any use of non-order-only information to define, compute,
select, tune, rescue, report, or relabel `H_hat`.

Leakage includes:

- embedded coordinates;
- radial position;
- shell labels;
- horizon-side labels;
- straddle status;
- distance to the Schwarzschild radius;
- geometric `minbeam` or any comparator ranked by embedded distance;
- columns explicitly labeled `GROUND_TRUTH_READOUT / NOT_ORDER_ONLY_EVIDENCE`;
- visual or console inspection of geometry before fixing the audit terminal label;
- adding or removing baselines after seeing their performance;
- changing the comparison metric after seeing baseline results;
- using PR004/PR005/PR006/PR007 diagnostic plots or radial readouts to alter the audit
  label.

Leakage does not include:

- using `seed`, `intensity`, `K`, `start_id`, `depth_k`, or `slice_status` as declared
  order-only / grouping inputs;
- reading already committed preregistration and validation reports to verify declared
  scope, hashes, and terminal labels;
- computing deterministic summaries from permitted columns only.

## 4. Input Artifacts

Allowed input artifacts:

- `dev/PR006_ORDER_ONLY_H_HAT_PREREGISTRATION.md`;
- `data/reports/PR006_ORDER_ONLY_H_HAT_VALIDATION_REPORT.md`;
- `data/reports/pr006_order_only_h_hat_validation.csv`;
- `dev/PR007_H_HAT_ROBUSTNESS_PREREGISTRATION.md`;
- `data/reports/PR007_H_HAT_ROBUSTNESS_VALIDATION_REPORT.md`;
- `data/reports/pr007_h_hat_robustness_seed_density.csv`;
- `dev/PR007_A_H_HAT_ROBUSTNESS_CLOSURE_DECISION.md`.

Frozen artifact split:

- Reference/training artifacts: PR006 preregistration, PR006 validation report, and
  `data/reports/pr006_order_only_h_hat_validation.csv`.
- Evaluation artifacts: PR007-A preregistration, PR007-A validation report,
  `data/reports/pr007_h_hat_robustness_seed_density.csv`, and PR007-A closure decision.

All seven listed artifacts are required. The preregistrations, validation reports, and
closure decision provide contract metadata only; they may not supply numerical baseline
predictions or evaluation values. Both empirical baselines are derived only from
`data/reports/pr006_order_only_h_hat_validation.csv`. All evaluation values and metrics
are derived only from `data/reports/pr007_h_hat_robustness_seed_density.csv`, with frozen
SHA256 `b0da043bd16554066d262ad897d7240052530e652475f62c9df3570c40463afd`.

Forbidden input artifacts for PR008 terminal logic:

- any file containing embedded coordinates or radial distances;
- any figure or table whose primary variable is radius, shell, straddle, or horizon side;
- any uncommitted diagnostic output not listed above.

## 5. Allowed Columns

PR008 terminal logic may use only these CSV columns:

- `seed`;
- `intensity`;
- `K`;
- `start_id`;
- `depth_k`;
- `slice_status`;
- `n_survivors`;
- `n_endpoint_identities`;
- `top1_endpoint_pair`;
- `top1_endpoint_count`;
- `top1_endpoint_mass_fraction`;
- `top3_endpoint_count`;
- `top3_endpoint_mass_fraction`;
- `endpoint_entropy_nats`;
- `effective_endpoint_count`;
- `turnover_from_previous_depth`.

For the primary `H_hat` and baseline comparisons, only `seed`, `intensity`, `K`,
`start_id`, `depth_k`, and `slice_status` are required.

Any column outside this list is prohibited for PR008 terminal logic.

## 6. Admissible Baselines

All baselines must be computed from the allowed columns only and must be frozen before
audit execution.

Frozen baseline IDs:

1. `constant_depth_8`: predicts `8` for every `(seed, intensity)` evaluation cell.
2. `constant_depth_26`: predicts `26` for every `(seed, intensity)` evaluation cell.
3. `pr006_block_h_hat`: predicts the lower median over all 18 frozen PR006
   `H_hat(seed, intensity)` values for every `(seed, intensity)` evaluation cell.
4. `pr006_intensity_h_hat`: for each evaluation intensity `I`, predicts the lower median
   over the frozen PR006 seed set of the PR006 `H_hat(seed, I)` values defined below.

Both empirical baselines are derived exclusively from
`data/reports/pr006_order_only_h_hat_validation.csv` with frozen SHA256
`e9f9d2dd861795454b32267477d7510ba1f48ddc0ba75fae66363a4a33cf0255`. Only the
columns `seed`, `intensity`, `K`, `start_id`, `depth_k`, and `slice_status` may enter the
derivation. The frozen PR006 seed set is
`{1000024, 1000025, 1000026, 1000027, 1000028, 1000029}`. For each seed and intensity,
compute `first_empty_depth` for every `start_id` using Section 2, then compute
`H_hat(seed, intensity)` as the lower median over `start_id`. For each intensity `I`,
`pr006_intensity_h_hat(I)` is the lower median of those six `H_hat(seed, I)` values.
Every PR007-A evaluation cell with intensity `I` receives that same scalar prediction;
no PR007-A seed value enters the baseline.

No other PR006 artifact, rerun, seed subset, interpolation, extrapolation,
nearest-neighbor substitution, cross-intensity fallback, or alternative aggregation is
permitted. A missing frozen PR006 seed, a missing evaluation intensity in the PR006
artifact, more than one derived `H_hat` value for the same `(seed, intensity)` cell, or
a duplicate raw `(seed, intensity, K, start_id, depth_k)` row is
`FAILED_DATA_CONTRACT`.

`constant_depth_4` is excluded from the primary frozen baseline set because it is an
oracle baseline for the already observed PR006/PR007 result `H_hat=4`. Including it
would make the baseline comparison non-informative by construction.

`constant_depth_4` may be retained only as `DEGENERATE_ORACLE_SANITY_CHECK`, and it is
excluded from `max_baseline_cell_agreement_with_H4`, `BASELINE_DOMINATED`, and the
primary pass/fail comparison.

Inadmissible baselines:

- any baseline using radial, shell, straddle, horizon-side, or embedding information;
- any baseline outside the frozen baseline IDs above;
- any baseline selected after seeing PR008 baseline outcomes;
- any baseline tuned to force `H_hat` to pass or fail;
- any multi-K baseline unless a separate preregistration freezes the aggregation rule;
- any baseline that changes `K_REF`, `MAX_DEPTH`, `NO_EMPTY_SENTINEL`, or the lower-median
  rule.

## 7. Comparison Metric

The primary comparison metric is:

```text
cell_agreement_with_H4 = fraction of (seed, intensity) cells whose estimator value is 4.
```

For `H_hat`, the estimator value is `H_hat(seed, intensity)`.

For a baseline, the estimator value is the baseline's preregistered scalar prediction for
the same `(seed, intensity)` cell.

The primary audit comparison is:

```text
max_baseline_cell_agreement_with_H4 =
  max(cell_agreement_with_H4(baseline_id) for baseline_id in
      {constant_depth_8, constant_depth_26,
       pr006_block_h_hat, pr006_intensity_h_hat})

delta_agreement = cell_agreement_with_H4(H_hat) - max_baseline_cell_agreement_with_H4.
```

This metric is intentionally scalar and order-only. It does not use radial error,
distance-to-horizon, shell accuracy, or any geometric target.

The secondary reporting set is frozen and all of the following must be reported:

- `H_hat_block`: lower median over all PR007-A evaluation `H_hat(seed, intensity)` cells;
- `cell_fraction_H4`: fraction of PR007-A evaluation `(seed, intensity)` cells with
  `H_hat(seed, intensity) = 4`;
- `seed_group_median(seed)`: lower median of `first_empty_depth` over all PR007-A
  evaluation intensities and `start_id` values for that seed;
- `intensity_group_median(intensity)`: lower median of `first_empty_depth` over all
  PR007-A evaluation seeds and `start_id` values for that intensity;
- the count for each frozen data-contract failure class: missing required artifacts,
  artifact SHA256 mismatches, missing or malformed required CSV columns, duplicate raw
  `(seed, intensity, K, start_id, depth_k)` rows, incomplete depth-coverage sequences,
  rows with `K != 8`, missing frozen PR006 seed-intensity cells, and duplicate derived
  PR006 `(seed, intensity)` cells.

These secondary summaries are descriptive only and must not override the primary
terminal tree. No additional secondary metric, subgroup, transformation, baseline, or
visualization may be selected for reporting after observing PR008 results.

## 8. Output Artifacts

Expected future outputs, if PR008 is later authorized:

- audit table: `data/reports/pr008_h_hat_baseline_leakage_audit.csv`;
- report: `data/reports/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_REPORT.md`.

No PR008 output is authorized by this draft.

## 9. Terminal Labels

Allowed terminal labels:

- `FAILED_RUNTIME`;
- `FAILED_DATA_CONTRACT`;
- `FAILED_LEAKAGE_AUDIT`;
- `BASELINE_DOMINATED`;
- `PASSED_BASELINE_AND_LEAKAGE_AUDIT`;
- `INCONCLUSIVE`.

No other terminal label is allowed.

Terminal precedence is exactly:

```text
FAILED_RUNTIME > FAILED_DATA_CONTRACT > FAILED_LEAKAGE_AUDIT > BASELINE_DOMINATED >
PASSED_BASELINE_AND_LEAKAGE_AUDIT > INCONCLUSIVE
```

Exactly one terminal label is assigned to each run. The labels are evaluated in the
frozen precedence order above, and the terminal label is the first applicable label.
Once a label applies, no lower-precedence label is evaluated or assigned.

## 10. Failure Conditions

`FAILED_DATA_CONTRACT` applies if:

- any required input artifact is missing;
- any required CSV column is missing or malformed;
- duplicate `(seed, intensity, K, start_id, depth_k)` rows are present;
- depth coverage `1..25` is incomplete for any sequence;
- any `K` value other than `8` enters terminal logic.

`FAILED_RUNTIME` applies if the PR008 audit script or report cannot complete due to an
exception, a missing executable dependency, an unreadable input file, malformed CSV, or
any nonzero command exit not already classified as `FAILED_DATA_CONTRACT`.

`FAILED_LEAKAGE_AUDIT` applies if:

- any forbidden artifact or column is used in terminal logic;
- any radial, shell, straddle, horizon-side, or embedded-coordinate information affects
  `H_hat`, a baseline, the comparison metric, or the terminal label;
- baselines are added, dropped, or reweighted after results are observed;
- the comparison metric is changed after results are observed.

`BASELINE_DOMINATED` applies if:

```text
max_baseline_cell_agreement_with_H4 >= cell_agreement_with_H4(H_hat)
```

and neither `FAILED_DATA_CONTRACT` nor `FAILED_LEAKAGE_AUDIT` applies.

`PASSED_BASELINE_AND_LEAKAGE_AUDIT` applies if all are true:

1. Data contract passes.
2. Leakage audit passes.
3. `cell_agreement_with_H4(H_hat) = 1.0`.
4. `delta_agreement > 0`.

`INCONCLUSIVE` applies if the data contract and leakage audit pass but neither
`BASELINE_DOMINATED` nor `PASSED_BASELINE_AND_LEAKAGE_AUDIT` applies.

## 11. Stop Rule

After PR008 output is observed, the following are prohibited:

- adding or removing baselines;
- changing baseline definitions;
- changing the comparison metric;
- changing terminal thresholds;
- changing allowed columns;
- adding radial, shell, straddle, or horizon-side diagnostics;
- converting `BASELINE_DOMINATED` or `INCONCLUSIVE` into a pass by weakening the audit.

Any such change requires a separate preregistration before execution.

## 12. Prohibited Claims

PR008 may not claim:

- horizon reconstruction;
- radial localization;
- K-invariance;
- a physical barrier;
- Schwarzschild 3+1D reconstruction;
- robustness over patch size, `M`, or `MAX_STARTS`;
- superiority over baselines not preregistered before audit execution.

Allowed claim if PR008 passes:

```text
The fixed-K order-only scalar estimator H_hat survived the preregistered baseline and
leakage audit within the audited PR008 scope.
```
