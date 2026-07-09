# PR006 Order-Only H_hat Validation Report

STATUS: FINAL
CONTRACT_VERDICT: PASS_DATA_CONTRACT
SCIENTIFIC_TERMINAL_LABEL: REPLICATED_FIXED_K_LOCALIZATION_SIGNAL

## Scope

This report validates the frozen PR006 fixed-K `H_hat` estimator contract from:

- `dev/PR006_ORDER_ONLY_H_HAT_PREREGISTRATION.md`
- Frozen validation block commit: `8cb1543`

Frozen command executed:

```bash
python3 dev/measure_kbeam_peeloff.py --seeds 6 --seed-offset 24 \
  --intensities 4800,9600,19200 \
  --slice-out data/reports/pr006_order_only_h_hat_validation.csv \
  --probe-k 8
```

Validation block:

- seed set: `1000024,1000025,1000026,1000027,1000028,1000029`
- seed source: `EXPLORE_POOL[24:30]`
- intensity grid: `4800,9600,19200`
- `K_REF = 8`
- CSV: `data/reports/pr006_order_only_h_hat_validation.csv`
- CSV SHA256: `e9f9d2dd861795454b32267477d7510ba1f48ddc0ba75fae66363a4a33cf0255`
- data rows: `47,625`
- sequences `(seed, intensity, K, start_id)`: `1,905`

The run completed with pre/post seal checks:

- Pre seal: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
- Post seal: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`

Runtime reported by the runner: `517.4s`.

## Data Contract Checks

- Mandatory PR005 primary column prefix matches the PR006 input contract: yes.
- Unique `K` values present: `8`.
- Duplicate `(seed, intensity, K, start_id, depth_k)` rows: `0`.
- Coverage failures for `depth_k = 1..25`: `0`.
- `EVALUABLE` rows: `6,637`.
- `EMPTY` rows: `40,988`.
- No non-order-only diagnostic column was required to compute `H_hat`.

## H_hat Definition Applied

For each sequence:

```text
first_empty_depth(sequence) =
  the smallest depth_k in [1,25] with slice_status = EMPTY,
  or 26 if no EMPTY slice occurs in [1,25].
```

For each `(seed, intensity)` group:

```text
H_hat(seed, intensity) =
  lower median over start_id of first_empty_depth(seed, intensity, start_id, K_REF).
```

For the validation block:

```text
H_hat_block =
  lower median over (seed, intensity) of H_hat(seed, intensity).
```

Only `seed`, `intensity`, `K`, `start_id`, `depth_k`, and `slice_status` were used.

## Primary Results

`H_hat(seed, intensity)`:

| seed | intensity | H_hat | n_start |
|---:|---:|---:|---:|
| 1000024 | 4800.0 | 4 | 107 |
| 1000024 | 9600.0 | 4 | 114 |
| 1000024 | 19200.0 | 4 | 122 |
| 1000025 | 4800.0 | 4 | 83 |
| 1000025 | 9600.0 | 4 | 102 |
| 1000025 | 19200.0 | 4 | 133 |
| 1000026 | 4800.0 | 4 | 74 |
| 1000026 | 9600.0 | 4 | 91 |
| 1000026 | 19200.0 | 4 | 128 |
| 1000027 | 4800.0 | 4 | 91 |
| 1000027 | 9600.0 | 4 | 108 |
| 1000027 | 19200.0 | 4 | 121 |
| 1000028 | 4800.0 | 4 | 84 |
| 1000028 | 9600.0 | 4 | 115 |
| 1000028 | 19200.0 | 4 | 109 |
| 1000029 | 4800.0 | 4 | 84 |
| 1000029 | 9600.0 | 4 | 114 |
| 1000029 | 19200.0 | 4 | 125 |

Block result:

```text
H_hat_block = 4
```

Seed group medians:

| seed | median(first_empty_depth) |
|---:|---:|
| 1000024 | 4 |
| 1000025 | 4 |
| 1000026 | 4 |
| 1000027 | 4 |
| 1000028 | 4 |
| 1000029 | 4 |

Intensity group medians:

| intensity | median(first_empty_depth) |
|---:|---:|
| 4800.0 | 4 |
| 9600.0 | 4 |
| 19200.0 | 4 |

## Validation Tree

`REPLICATED_FIXED_K_LOCALIZATION_SIGNAL` requires:

1. `H_hat_block = 4`.
2. Every seed group has `median(first_empty_depth) <= 4`.
3. Every intensity group has `median(first_empty_depth) <= 4`.

All three conditions are satisfied.

`NO_FIXED_K_LOCALIZATION_SIGNAL` is not satisfied because `H_hat_block = 4`, not `>= 8`.

Terminal label:

```text
REPLICATED_FIXED_K_LOCALIZATION_SIGNAL
```

## Diagnostic Empty Fractions

These values are reported as order-only descriptive diagnostics and do not alter the
terminal label:

| depth_k | empty_fraction |
|---:|---:|
| 1 | 0.000000 |
| 2 | 0.022047 |
| 3 | 0.039370 |
| 4 | 0.912336 |
| 5 | 0.932808 |
| 6 | 0.948031 |
| 7 | 0.956955 |
| 8 | 0.961155 |

## Interpretation Limits

This validates only the frozen PR006 statement:

```text
Under the frozen K_REF=8 order-only estimator contract, H_hat reproduces a coarse
early-emptying localization marker on the validation block.
```

This report does not claim:

- K-invariance;
- a population-depth barrier;
- a physical invariant axis in `K`;
- horizon reconstruction;
- radial localization;
- an extended horizon segment;
- universality across K, intensity, or spacetime dimension;
- rescue or reinterpretation of PR004 or PR005 terminal labels.
