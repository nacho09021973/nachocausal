# PR006 Order-Only H_hat Estimator - Minimal Preregistration Draft

STATUS: PREREGISTRATION_DRAFT
VALIDATION_STATUS: NOT_RUN
SCOPE: PREREG_ONLY / NO_CODE / NO_EXPERIMENTS
RELATION_TO_PR005: NEW_FIXED_K_ESTIMATOR_AFTER_PR005_INCONCLUSIVE
ORDER_ONLY_PRIMARY: YES_PENDING_GUARD_REVIEW

## 1. Motivation

PR005 held-out validation was `INCONCLUSIVE`, but it replicated an early-emptying
localization signal:

- `median(first_empty_depth) = 4`;
- high depth-4 empty fraction at the frozen PR005 `K=8`;
- no PR005 barrier confirmation because the frozen seed-stability tree did not pass.

The PR005 K-stability sweep showed that transition sharpness is not K-invariant. PR006
therefore treats `K` as a frozen algorithmic hyperparameter, not as a physical invariant
axis. PR006 does not inherit any K-invariant barrier claim from PR005.

## 2. Physical Question

Can a fixed-K, order-only estimator produce a reproducible coarse localization marker
from the early-emptying signal without using embedded geometry or horizon-side labels?

This is not a horizon reconstruction claim. The target of PR006 is a frozen estimator
contract for a scalar order-only localization marker, not a geometric curve, radial
coordinate, shell, or extended horizon segment.

## 3. Definition of H_hat

For a causet processed by the frozen PR006 fixed-K beam protocol, define one sequence for
each deterministic start:

```text
sequence = (seed, intensity, start_id, K_REF)
```

For each sequence, define:

```text
first_empty_depth(sequence) =
  the smallest depth_k in [1, 25] with slice_status = EMPTY,
  or 26 if no EMPTY slice occurs in [1, 25].
```

The PR006 estimator is the fixed-K median early-emptying depth:

```text
H_hat(seed, intensity) =
  median over start_id of first_empty_depth(seed, intensity, start_id, K_REF).
```

Across a validation block, the reported primary summary is:

```text
H_hat_block =
  median over (seed, intensity) of H_hat(seed, intensity).
```

`H_hat` is a depth-index estimator. It is not a radial coordinate and must not be
converted into a physical horizon location inside PR006.

Median rule: if an even number of values is present, use the lower median after numeric
sort. This keeps `H_hat` an integer depth index.

## 4. Frozen Hyperparameters

PR006 freezes:

- `K_REF = 8`;
- `MAX_DEPTH = 25`;
- `NO_EMPTY_SENTINEL = 26`;
- primary unit: `(seed, intensity, start_id, K_REF, depth_k)`;
- primary per-sequence statistic: `first_empty_depth`;
- primary per-causet statistic: lower median over `start_id`;
- primary block statistic: lower median over `(seed, intensity)`.

No multi-K aggregation is part of this preregistration. Any later multi-K estimator must
freeze its aggregation rule before validation in a separate preregistration.

## 5. Allowed Inputs

The primary estimator uses only the order-only PR005 depth-slice contract fields:

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

For the minimal PR006 `H_hat` defined in Section 3, only `K`, `start_id`, `depth_k`, and
`slice_status` are primary inputs after grouping by `seed` and `intensity`.

`seed` and `intensity` are grouping metadata for validation summaries. They are not
allowed to change the estimator rule.

Seed and intensity groups are defined as follows:

- seed group: all rows sharing the same `seed`, across all preregistered intensities
  and all `start_id` values at `K_REF`;
- intensity group: all rows sharing the same `intensity`, across all preregistered
  seeds and all `start_id` values at `K_REF`.

## 6. Forbidden Inputs and Ground-Truth Leakage

The following are forbidden in the PR006 primary estimator:

- embedded coordinates;
- radial position;
- shell labels;
- horizon-side labels;
- straddle status;
- radial spread;
- modal shell;
- distance to the Schwarzschild radius;
- `minbeam` if it is defined by embedded radial distance or any other non-order-only
  criterion;
- any column labeled `GROUND_TRUTH_READOUT / NOT_ORDER_ONLY_EVIDENCE`;
- any post-output visual inspection of geometry before freezing thresholds or terminal
  labels.

These quantities may appear only in a separate diagnostic section after the primary PR006
terminal label is fixed. They must not alter `H_hat`, thresholds, exclusions, seed sets,
intensity sets, or the fixed `K_REF`.

## 7. Data Contract

Validation run block status:

```text
VALIDATION RUN BLOCK: NOT FROZEN IN THIS DRAFT.
```

No PR006 validation run may be executed until the command, seed set, intensity grid,
output path, and expected report path are frozen in a follow-up preregistration commit.

A valid PR006 validation input must satisfy the PR005 depth-slice data contract for
`K_REF=8`:

1. Mandatory PR005 primary columns are present in the frozen order.
2. There is at most one row for each `(seed, intensity, K, start_id, depth_k)`.
3. Every sequence has explicit rows for `depth_k = 1..25`.
4. Empty slices are represented as `slice_status = EMPTY`, not dropped rows.
5. No non-order-only diagnostic column is required to compute `H_hat`.

If any item fails, PR006 terminal label is `FAILED_DATA_CONTRACT`.

## 8. Validation Tree

Allowed terminal labels:

- `FAILED_RUNTIME`;
- `FAILED_DATA_CONTRACT`;
- `REPLICATED_FIXED_K_LOCALIZATION_SIGNAL`;
- `NO_FIXED_K_LOCALIZATION_SIGNAL`;
- `INCONCLUSIVE`.

Primary success condition:

```text
REPLICATED_FIXED_K_LOCALIZATION_SIGNAL iff:
  H_hat_block = 4
  and every seed group has median(first_empty_depth) <= 4
  and every intensity group has median(first_empty_depth) <= 4.
```

Primary null condition:

```text
NO_FIXED_K_LOCALIZATION_SIGNAL iff:
  H_hat_block >= 8
  and every seed group has median(first_empty_depth) >= 8
  and every intensity group has median(first_empty_depth) >= 8.
```

`INCONCLUSIVE` applies if the data contract passes but neither full condition is met.

These thresholds are intentionally coarse. PR006 tests whether the fixed-K early-emptying
localization marker replicates as an order-only estimator; it does not test a sharp
barrier or a K-invariant physical transition.

## 9. Post-Hoc Validation and Prohibited Adjustments

After any PR006 validation output is observed, the following are post-hoc and forbidden
inside the same preregistration:

- changing `K_REF`;
- adding, dropping, or reweighting K values;
- changing `MAX_DEPTH` or `NO_EMPTY_SENTINEL`;
- changing the median rule;
- changing seed or intensity inclusion rules;
- replacing `first_empty_depth` with another statistic;
- using `empty_fraction(4)` or K-sweep sharpness to rescue the terminal label;
- using radial, straddle, shell, or horizon-side diagnostics to tune the estimator;
- converting `INCONCLUSIVE` into success by weakening seed or intensity requirements.

Any such change requires a separately committed preregistration before validation.

## 10. Prohibited Claims

PR006 may not claim:

- K-invariance;
- a population-depth barrier;
- a physical invariant axis in `K`;
- horizon reconstruction;
- radial localization;
- an extended horizon segment;
- universality across K, intensity, or spacetime dimension;
- rescue or reinterpretation of PR004 or PR005 terminal labels.

Allowed claim if the success condition passes:

```text
Under the frozen K_REF=8 order-only estimator contract, H_hat reproduces a coarse
early-emptying localization marker on the validation block.
```

Allowed claim if the result is inconclusive:

```text
The fixed-K order-only H_hat contract passed or failed the data contract as reported,
but did not validate a reproducible coarse localization marker under the frozen tree.
```

## 11. Future Outputs

- `data/reports/pr006_order_only_h_hat_validation.csv` - NOT_CREATED
- `data/reports/PR006_ORDER_ONLY_H_HAT_VALIDATION_REPORT.md` - NOT_CREATED
