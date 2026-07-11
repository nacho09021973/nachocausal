# PR008 H_hat Baseline and Leakage Audit Report
## 1. Scope and frozen input identities

- `dev/PR006_ORDER_ONLY_H_HAT_PREREGISTRATION.md`
- `data/reports/PR006_ORDER_ONLY_H_HAT_VALIDATION_REPORT.md`
- `data/reports/pr006_order_only_h_hat_validation.csv`
- `dev/PR007_H_HAT_ROBUSTNESS_PREREGISTRATION.md`
- `data/reports/PR007_H_HAT_ROBUSTNESS_VALIDATION_REPORT.md`
- `data/reports/pr007_h_hat_robustness_seed_density.csv`
- `dev/PR007_A_H_HAT_ROBUSTNESS_CLOSURE_DECISION.md`
## 2. Data-contract checks and counts

- `missing_required_artifacts`: 0
- `artifact_sha256_mismatches`: 0
- `missing_or_malformed_required_csv_columns`: 0
- `duplicate_raw_rows`: 0
- `incomplete_depth_coverage_sequences`: 0
- `rows_with_nonreference_k`: 0
- `missing_frozen_pr006_seed_intensity_cells`: 0
- `duplicate_derived_pr006_cells`: 0
## 3. Leakage guard evidence

Access is restricted to the frozen artifact inventory; calculation columns are `seed`, `intensity`, `K`, `start_id`, `depth_k`, and `slice_status`.
## 4. Frozen baseline definitions and roles

- `constant_depth_8`
- `constant_depth_26`
- `pr006_block_h_hat`
- `pr006_intensity_h_hat`
## 5. Primary comparison metrics

The normative values are serialized in the machine-readable block.
## 6. Frozen secondary summaries

- `seed_group_median(1000030)`: 4
- `seed_group_median(1000031)`: 4
- `seed_group_median(1000032)`: 4
- `seed_group_median(1000033)`: 4
- `seed_group_median(1000034)`: 4
- `seed_group_median(1000035)`: 4
- `seed_group_median(1000036)`: 4
- `seed_group_median(1000037)`: 4
- `seed_group_median(1000038)`: 4
- `seed_group_median(1000039)`: 4
- `intensity_group_median(4800.0)`: 4
- `intensity_group_median(9600.0)`: 4
- `intensity_group_median(19200.0)`: 4
## 7. DEGENERATE_ORACLE_SANITY_CHECK

`constant_depth_4` is emitted only with this role and is excluded from primary logic.
## 8. Terminal-label evaluation

`BASELINE_DOMINATED`
## 9. Interpretation limits

PR008 does not claim horizon reconstruction, radial localization, K-invariance, a physical barrier, Schwarzschild 3+1D reconstruction, robustness over patch size, `M`, or `MAX_STARTS`, or superiority over baselines not preregistered before audit execution.

BEGIN_PR008_MACHINE_READABLE_V1
machine_schema=pr008-machine-readable-v1
run_id=f90e7663ca361dab3f2a26d985cea69b85048ffcd2f1986f031b09f6c8cea3a8
configuration_fingerprint=3728f4934064b0959a3fc0add111e48b3a20c3c97d1cb0d40d7af0b2f9e702d5
input_provenance_fingerprint=17986a551545e42bd13dc93b5fc770ad97721f93f4506eacdd2dae9de93ca13d
publication_status=VALID
terminal_label=BASELINE_DOMINATED
artifact_01_path=dev/PR006_ORDER_ONLY_H_HAT_PREREGISTRATION.md
artifact_02_path=data/reports/PR006_ORDER_ONLY_H_HAT_VALIDATION_REPORT.md
artifact_03_path=data/reports/pr006_order_only_h_hat_validation.csv
artifact_04_path=dev/PR007_H_HAT_ROBUSTNESS_PREREGISTRATION.md
artifact_05_path=data/reports/PR007_H_HAT_ROBUSTNESS_VALIDATION_REPORT.md
artifact_06_path=data/reports/pr007_h_hat_robustness_seed_density.csv
artifact_07_path=dev/PR007_A_H_HAT_ROBUSTNESS_CLOSURE_DECISION.md
artifact_03_sha256=e9f9d2dd861795454b32267477d7510ba1f48ddc0ba75fae66363a4a33cf0255
artifact_06_sha256=b0da043bd16554066d262ad897d7240052530e652475f62c9df3570c40463afd
csv_output_path=data/reports/pr008_h_hat_baseline_leakage_audit.csv
report_output_path=data/reports/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_REPORT.md
h_hat_cell_agreement_with_H4=3ff0000000000000
max_baseline_cell_agreement_with_H4=3ff0000000000000
delta_agreement=0000000000000000
H_hat_block=4
cell_fraction_H4=3ff0000000000000
END_PR008_MACHINE_READABLE_V1
