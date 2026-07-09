# PR007 H_hat Robustness Validation Report

STATUS: FINAL
CONTRACT_VERDICT: PASS_DATA_CONTRACT
SCIENTIFIC_TERMINAL_LABEL: ROBUST_FIXED_K_H_HAT_SIGNAL

## Scope

This report validates the frozen PR007-A seed-density robustness preregistration:

- `dev/PR007_H_HAT_ROBUSTNESS_PREREGISTRATION.md`
- Frozen preregistration commit: `2b02d66`

Frozen command executed:

```bash
python3 dev/measure_kbeam_peeloff.py --seeds 10 --seed-offset 30 \
  --intensities 4800,9600,19200 \
  --slice-out data/reports/pr007_h_hat_robustness_seed_density.csv \
  --probe-k 8
```

Validation block:

- seed source: `EXPLORE_POOL[30:40]`
- seed set: `1000030,1000031,1000032,1000033,1000034,1000035,1000036,1000037,1000038,1000039`
- intensity grid: `4800,9600,19200`
- `K_REF = 8`
- CSV: `data/reports/pr007_h_hat_robustness_seed_density.csv`
- CSV SHA256: `b0da043bd16554066d262ad897d7240052530e652475f62c9df3570c40463afd`
- data rows: `81,275`
- sequences `(seed, intensity, K, start_id)`: `3,251`

The run completed with pre/post seal checks:

- Pre seal: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
- Post seal: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`

Runtime reported by the runner: `885.8s`.

## Data Contract Checks

- Mandatory primary column prefix matches the PR007-A input contract: yes.
- Unique `K` values present: `8`.
- Seed set matches the preregistered grid: yes.
- Intensity grid matches the preregistered grid: yes.
- Duplicate `(seed, intensity, K, start_id, depth_k)` rows: `0`.
- Coverage failures for `depth_k = 1..25`: `0`.
- `EVALUABLE` rows: `11,533`.
- `EMPTY` rows: `69,742`.
- No non-order-only diagnostic column was required to compute `H_hat`.

## H_hat Definition Applied

For each sequence:

```text
first_empty_depth(sequence) =
  the smallest depth_k in [1,25] with slice_status = EMPTY,
  or 26 if no EMPTY slice occurs in [1,25].
```

For each `(seed, intensity)` cell:

```text
H_hat(seed, intensity) =
  lower median over start_id of first_empty_depth(seed, intensity, start_id, K_REF).
```

For the validation block:

```text
H_hat_block =
  lower median over all (seed, intensity) cells.
```

Only `seed`, `intensity`, `K`, `start_id`, `depth_k`, and `slice_status` were used.

## Primary Results

`H_hat(seed, intensity)`:

| seed | intensity | H_hat | n_start |
|---:|---:|---:|---:|
| 1000030 | 4800.0 | 4 | 121 |
| 1000030 | 9600.0 | 4 | 118 |
| 1000030 | 19200.0 | 4 | 123 |
| 1000031 | 4800.0 | 4 | 112 |
| 1000031 | 9600.0 | 4 | 107 |
| 1000031 | 19200.0 | 4 | 111 |
| 1000032 | 4800.0 | 4 | 83 |
| 1000032 | 9600.0 | 4 | 120 |
| 1000032 | 19200.0 | 4 | 126 |
| 1000033 | 4800.0 | 4 | 82 |
| 1000033 | 9600.0 | 4 | 97 |
| 1000033 | 19200.0 | 4 | 137 |
| 1000034 | 4800.0 | 4 | 103 |
| 1000034 | 9600.0 | 4 | 107 |
| 1000034 | 19200.0 | 4 | 136 |
| 1000035 | 4800.0 | 4 | 109 |
| 1000035 | 9600.0 | 4 | 125 |
| 1000035 | 19200.0 | 4 | 117 |
| 1000036 | 4800.0 | 4 | 85 |
| 1000036 | 9600.0 | 4 | 85 |
| 1000036 | 19200.0 | 4 | 112 |
| 1000037 | 4800.0 | 4 | 88 |
| 1000037 | 9600.0 | 4 | 100 |
| 1000037 | 19200.0 | 4 | 119 |
| 1000038 | 4800.0 | 4 | 97 |
| 1000038 | 9600.0 | 4 | 108 |
| 1000038 | 19200.0 | 4 | 114 |
| 1000039 | 4800.0 | 4 | 108 |
| 1000039 | 9600.0 | 4 | 97 |
| 1000039 | 19200.0 | 4 | 104 |

Block and robustness summaries:

```text
H_hat_block = 4
cell_fraction_H4 = 1.0
intensity_median_drift = 0
```

Seed group medians:

| seed | seed_group_median |
|---:|---:|
| 1000030 | 4 |
| 1000031 | 4 |
| 1000032 | 4 |
| 1000033 | 4 |
| 1000034 | 4 |
| 1000035 | 4 |
| 1000036 | 4 |
| 1000037 | 4 |
| 1000038 | 4 |
| 1000039 | 4 |

Intensity group medians:

| intensity | intensity_group_median |
|---:|---:|
| 4800.0 | 4 |
| 9600.0 | 4 |
| 19200.0 | 4 |

## Validation Tree

`ROBUST_FIXED_K_H_HAT_SIGNAL` requires:

1. `H_hat_block = 4`.
2. Every seed group has `seed_group_median <= 4`.
3. Every intensity group has `intensity_group_median = 4`.
4. `cell_fraction_H4 >= 0.90`.
5. `intensity_median_drift <= 1`.

All five conditions are satisfied.

`NO_ROBUST_FIXED_K_H_HAT_SIGNAL` is not satisfied because `H_hat_block = 4`, not `>= 8`.

Terminal label:

```text
ROBUST_FIXED_K_H_HAT_SIGNAL
```

## Diagnostic Empty Fractions

These values are order-only descriptive diagnostics and do not alter the terminal label:

| depth_k | empty_fraction |
|---:|---:|
| 1 | 0.000000 |
| 2 | 0.025223 |
| 3 | 0.046755 |
| 4 | 0.899108 |
| 5 | 0.928945 |
| 6 | 0.943710 |
| 7 | 0.950169 |
| 8 | 0.956629 |

## Interpretation Limits

This validates only the frozen PR007-A statement:

```text
The fixed-K order-only scalar estimator H_hat remains robust over the preregistered
seed and intensity grid tested in PR007-A.
```

This report does not claim:

- horizon reconstruction;
- radial localization;
- a geometric horizon surface;
- K-invariance;
- a population-depth physical barrier;
- universality across patch size, `M`, start population size, or spacetime dimension;
- rescue or reinterpretation of PR004 or PR005 terminal labels.
