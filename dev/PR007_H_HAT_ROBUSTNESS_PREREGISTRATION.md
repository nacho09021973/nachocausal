# PR007 H_hat Robustness - Preregistration Draft

STATUS: PREREGISTRATION_DRAFT
VALIDATION_STATUS: NOT_RUN
SCOPE: PREREG_ONLY / NO_CODE / NO_EXPERIMENTS
RELATION_TO_PR006: ROBUSTNESS_AFTER_REPLICATED_FIXED_K_LOCALIZATION_SIGNAL

## 1. Physical Question

Does the scalar estimator

```text
H_hat = lower-median first_empty_depth at fixed K_REF = 8
```

remain stable under preregistered nuisance-axis variation that does not change its
definition?

PR007 is a robustness/convergence test of the PR006 estimator object. It is not a
horizon reconstruction, not a radial localization test, and not a K-invariance test.

## 2. Inherited Estimator

PR007 inherits the PR006 estimator without modification:

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

## 3. Nuisance Axes

PR007-A tests only nuisance axes currently exposed by the existing frozen runner
interface:

- seed block;
- intensity / density.

Frozen PR007-A grid:

- seed source: `EXPLORE_POOL[30:40]`;
- seed set: `1000030,1000031,1000032,1000033,1000034,1000035,1000036,1000037,1000038,1000039`;
- intensity grid: `4800,9600,19200`;
- `K_REF = 8`.

The following candidate nuisance axes are explicitly not part of PR007-A:

- patch size / `t_edge`;
- EGS fuzziness parameter `M`;
- start population cap / `MAX_STARTS`.

Those axes require a separate preregistration and, if needed, a separately authorized code
change or CLI exposure before validation. They must not be varied by editing constants
inside the runner after observing PR007-A output.

## 4. Frozen Validation Run Block

Validation run block status:

```text
VALIDATION RUN BLOCK: FROZEN_FOR_FUTURE_AUTHORIZATION.
```

Frozen command:

```bash
python3 dev/measure_kbeam_peeloff.py --seeds 10 --seed-offset 30 \
  --intensities 4800,9600,19200 \
  --slice-out data/reports/pr007_h_hat_robustness_seed_density.csv \
  --probe-k 8
```

Expected outputs:

- CSV: `data/reports/pr007_h_hat_robustness_seed_density.csv`;
- report: `data/reports/PR007_H_HAT_ROBUSTNESS_VALIDATION_REPORT.md`.

This preregistration freezes the run block but does not authorize execution by itself.
No PR007 run may be executed until the PI explicitly authorizes execution after this
draft is committed.

## 5. Data Contract

A valid PR007-A input must satisfy the PR006/PR005 depth-slice contract for `K_REF = 8`:

1. Mandatory primary columns are present in the frozen order.
2. There is at most one row for each `(seed, intensity, K, start_id, depth_k)`.
3. Every sequence has explicit rows for `depth_k = 1..25`.
4. Empty slices are represented as `slice_status = EMPTY`, not dropped rows.
5. No non-order-only diagnostic column is required to compute `H_hat`.
6. The only `K` value present is `8`.
7. The seed set and intensity grid match Section 3 exactly.

If any item fails, PR007-A terminal label is `FAILED_DATA_CONTRACT`.

## 6. Stability / Convergence Rule

For each `(seed, intensity)` cell, compute `H_hat(seed, intensity)` using the inherited
PR006 rule.

Derived summaries:

- `H_hat_block`: lower median over all `(seed, intensity)` cells.
- `seed_group_median(seed)`: lower median over all intensities and `start_id` values for
  that seed.
- `intensity_group_median(intensity)`: lower median over all seeds and `start_id` values
  for that intensity.
- `cell_fraction_H4`: fraction of `(seed, intensity)` cells with `H_hat = 4`.
- `intensity_median_drift`: `max(intensity_group_median) - min(intensity_group_median)`.

`ROBUST_FIXED_K_H_HAT_SIGNAL` requires all of:

1. `H_hat_block = 4`.
2. Every seed group has `seed_group_median <= 4`.
3. Every intensity group has `intensity_group_median = 4`.
4. `cell_fraction_H4 >= 0.90`.
5. `intensity_median_drift <= 1`.

`NO_ROBUST_FIXED_K_H_HAT_SIGNAL` requires all of:

1. `H_hat_block >= 8`.
2. Every intensity group has `intensity_group_median >= 8`.
3. `cell_fraction_H4 <= 0.25`.

`INCONCLUSIVE` applies if the data contract passes but neither full criterion set is
satisfied.

## 7. Terminal Labels

Allowed terminal labels:

- `FAILED_RUNTIME`;
- `FAILED_DATA_CONTRACT`;
- `ROBUST_FIXED_K_H_HAT_SIGNAL`;
- `NO_ROBUST_FIXED_K_H_HAT_SIGNAL`;
- `INCONCLUSIVE`.

No other label is allowed for PR007-A.

## 8. Stop Rule Against Post-Hoc Adjustment

After any PR007-A output is observed, the following are prohibited inside this
preregistration:

- changing `K_REF`;
- adding or dropping seeds;
- changing the intensity grid;
- changing `MAX_DEPTH` or `NO_EMPTY_SENTINEL`;
- changing the lower-median rule;
- changing the stability thresholds in Section 6;
- adding patch size, `M`, or `MAX_STARTS` variation;
- using radial, shell, straddle, horizon-side, or other ground-truth diagnostics to tune
  `H_hat`;
- converting `INCONCLUSIVE` into success by weakening seed, intensity, or cell-fraction
  requirements.

Any such change requires a separately committed preregistration before validation.

## 9. Prohibited Claims

PR007-A may not claim:

- horizon reconstruction;
- radial localization;
- a geometric horizon surface;
- K-invariance;
- a population-depth physical barrier;
- universality across patch size, `M`, start population size, or spacetime dimension;
- rescue or reinterpretation of PR004 or PR005 terminal labels.

Allowed claim if PR007-A passes:

```text
The fixed-K order-only scalar estimator H_hat remains robust over the preregistered
seed and intensity grid tested in PR007-A.
```

Disallowed claim:

```text
H_hat reconstructs the geometric horizon or proves a K-invariant physical barrier.
```
