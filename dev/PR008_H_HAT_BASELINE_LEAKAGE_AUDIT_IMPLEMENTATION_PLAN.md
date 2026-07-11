# PR008 H_hat Baseline and Leakage Audit - Minimal Implementation Plan

STATUS: IMPLEMENTATION_PLAN_DRAFT
AUTHORIZATION: PLAN_ONLY / NO_CODE / NO_EXECUTION / NO_RESULTS_INTERPRETATION
NORMATIVE_CONTRACT: `dev/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_PREREGISTRATION.md`
CONTRACT_AUDIT: `PASS_READY_FOR_IMPLEMENTATION_PLAN`

## 1. Scope

This document specifies the minimum implementation surface for the frozen PR008
contract. It does not authorize implementation, execution against PR006 or PR007-A
artifacts, output creation, or scientific interpretation.

The statistical definitions, baselines, thresholds, precedence rules, and terminal
labels are inherited from the frozen PR008 preregistration. The two final output paths
are also inherited literally from its Section 8.

The implementation module and test-file structure, command-line interface, function
partition, CSV schema and column order, serialization formats, temporary-file protocol,
and report layout are `PLAN_DEFINED_IMPLEMENTATION_DETAILS` introduced and frozen by
this implementation plan. They operationalize the preregistered contract but are not
themselves preregistered constants. They must not alter inherited statistical or terminal
logic.

The implementation must audit the existing fixed-K estimator only. It must not rerun a
causet generator, modify `H_hat`, inspect geometry, add a robustness axis, or introduce
an unregistered baseline, metric, subgroup, visualization, or terminal label.

## 2. Minimal File Surface

After separate implementation authorization, create only:

- `dev/audit_pr008_h_hat_baseline_leakage.py`: deterministic audit CLI and pure audit
  functions;
- `tests/test_pr008_h_hat_baseline_leakage.py`: synthetic contract and terminal-tree
  tests.

Do not modify PR006/PR007 runners, frozen input artifacts, or the PR008 preregistration
during implementation. The future authorized execution is limited to creating:

- `data/reports/pr008_h_hat_baseline_leakage_audit.csv`;
- `data/reports/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_REPORT.md`.

## 3. Fixed Interface

The future audit command is:

```bash
python3 dev/audit_pr008_h_hat_baseline_leakage.py
```

The CLI accepts no path, seed, intensity, baseline, metric, threshold, output, or label
arguments. The inherited input and output paths, hashes, statistical constants, baseline
IDs, thresholds, precedence rules, and terminal labels are module constants copied from
the frozen preregistration. The argument-free CLI and serialization contracts are
`PLAN_DEFINED_IMPLEMENTATION_DETAILS`.

Internal pure functions accept in-memory rows or temporary fixture paths only for unit
tests. The production entry point must always replace those with the frozen constants.

## 4. Deterministic Control Flow

The implementation order is fixed:

1. Verify that all seven required artifacts exist and are readable.
2. Verify the frozen SHA256 values of the PR006 reference CSV and PR007-A evaluation
   CSV before parsing either CSV.
3. Parse both CSVs with the standard-library `csv` module and validate the frozen data
   contract. CSV parse/schema failures are `FAILED_DATA_CONTRACT`; infrastructure or
   uncaught execution failures are `FAILED_RUNTIME`.
4. Project calculation rows to exactly `seed`, `intensity`, `K`, `start_id`, `depth_k`,
   and `slice_status`. No other column is permitted in an estimator, baseline, metric, or
   terminal-label function.
5. Compute PR006 reference `first_empty_depth` and `H_hat(seed, intensity)`, then the two
   empirical baseline prediction maps.
6. Compute PR007-A evaluation `first_empty_depth` and `H_hat(seed, intensity)`.
7. Materialize predictions for the four frozen primary baseline IDs and the mandatory
   `constant_depth_4` `DEGENERATE_ORACLE_SANITY_CHECK`.
8. Compute the primary metric, the frozen secondary reporting set, and the frozen
   data-contract failure counts.
9. Assign exactly one terminal label by returning the first applicable label in the
   frozen precedence order.
10. Render, validate, and publish each output independently using the per-file protocol
    in Section 9.2. No joint atomicity is claimed. Validate the final output pair before
    treating either file as valid or interpretable.

No result-dependent branch is permitted to alter steps 1-10, except the frozen failure
and terminal tree. Partial scientific output must not be interpreted.

## 5. Implementation Units

The module must keep the following responsibilities separate and free of hidden I/O:

- `lower_median(values)`: numeric sort followed by the lower median rule;
- `validate_artifacts(paths, hashes)`: required-path and SHA256 checks;
- `read_and_validate_csv(path, contract)`: strict parsing, key uniqueness, `K=8`, and
  depth coverage `1..25`;
- `derive_h_hat(rows)`: `first_empty_depth` per sequence and `H_hat` per cell;
- `build_reference_baselines(reference_h_hat, evaluation_cells)`: exactly
  `pr006_block_h_hat` and `pr006_intensity_h_hat`;
- `build_constant_baselines(evaluation_cells)`: exactly `constant_depth_8`,
  `constant_depth_26`, and the separated `constant_depth_4` sanity check;
- `compute_primary_metrics(evaluation_h_hat, primary_baselines)`: exact agreements,
  maximum baseline agreement, and `delta_agreement`;
- `compute_secondary_summaries(evaluation_rows, evaluation_h_hat)`: only the frozen
  secondary set;
- `assign_terminal_label(flags, metrics)`: first-applicable precedence rule;
- `render_audit_csv(...)` and `render_report(...)`: deterministic serialization only;
- `main()`: fixed orchestration and exception classification.

No function is permitted to import or call geometry, radial, shell, straddle, horizon-side,
`minbeam`, plotting, causet-generation, or PR004/PR005 diagnostic code.

## 6. Data And Leakage Guards

The implementation must fail closed on every preregistered data-contract class and
record its exact count. Artifact SHA256 mismatch is a data-contract failure and blocks
all estimator and baseline computation.

The leakage guard is structural:

- production I/O is limited to the seven required inputs and two output paths;
- only the two frozen CSVs are permitted to provide numerical values;
- estimator and metric functions receive projected six-column records, never complete
  CSV rows;
- the production CLI has no override parameters;
- an access manifest and the exact calculation-column list are rendered in the report;
- any attempted forbidden artifact or column use sets `FAILED_LEAKAGE_AUDIT` subject to
  the frozen terminal precedence.

Presence of an unused allowed descriptive column is not evidence input. Passing such a
column into calculation or terminal logic is prohibited.

## 7. Frozen Baseline Roles

Primary baseline IDs passed to `max_baseline_cell_agreement_with_H4` are exactly:

```text
constant_depth_8
constant_depth_26
pr006_block_h_hat
pr006_intensity_h_hat
```

`constant_depth_4` must always be emitted with role
`DEGENERATE_ORACLE_SANITY_CHECK`. It must never enter the primary-baseline collection,
`max_baseline_cell_agreement_with_H4`, `delta_agreement`, `BASELINE_DOMINATED`, or the
primary pass/fail comparison.

The empirical baselines must be built before evaluation metrics are computed. Their
builders must receive only evaluation cell keys to broadcast frozen predictions; they
must not receive evaluation `H_hat`, `start_id`, depth, or `slice_status` values.

## 8. Audit CSV Contract

The CSV dialect is a `PLAN_DEFINED_IMPLEMENTATION_DETAIL`. It is UTF-8 without BOM. The
first record is the header. The field separator is ASCII comma (`,`), the quote character
is ASCII double quote (`"`), and every record, including the last, ends with one ASCII LF
(`0x0a`). CRLF is invalid output. RFC 4180 quoting applies: a field containing comma,
double quote, CR, or LF must be quoted, and a double quote inside a quoted field is
doubled as `""`. A field containing none of those four characters must not be quoted.
Backslash escaping, comments, blank lines, locale-dependent formatting, leading or
trailing spaces in numeric fields, extra columns, omitted columns, and reordered columns
are prohibited. Column names are case-sensitive.

The normative serialized types are:

- `STRING`: Unicode NFC encoded as UTF-8; empty is valid only where the column table
  explicitly permits it.
- `ENUM`: exactly one case-sensitive literal enumerated in the column table.
- `BOOL`: exactly `true` or `false`.
- `INT`: base-10 ASCII with no leading `+` or leading zero except `0`; `-` is valid only
  where the column table permits negative values.
- `FLOAT_HEX64`: exactly 16 lowercase hexadecimal characters encoding IEEE 754 binary64
  big-endian bytes under Section 8.1, including negative-zero normalization; decimal or
  scientific notation, NaN, and infinities are invalid.
- `SHA256`: exactly 64 lowercase characters in `[0-9a-f]`.
- `PATH`: repository-relative POSIX path normalized under Section 8.1.
- `NULL`: exactly `null`, permitted only by the column table. It means that the column
  does not apply to that row or terminal state; it is not an observed missing value, a
  terminal label, or a publication status.

An empty CSV field is always invalid. An absent required value is a schema violation,
not a default, and gives the output set `FAILED_OUTPUT_CONTRACT`.

Columns occur in this exact normative order:

```text
record_type,run_id,configuration_fingerprint,input_provenance_fingerprint,seed,intensity,estimator_id,estimator_role,predicted_depth,agrees_with_H4,included_in_primary_max,terminal_label,h_hat_cell_agreement_with_H4,max_baseline_cell_agreement_with_H4,delta_agreement,H_hat_block,cell_fraction_H4
```

The column contract is exhaustive:

| Column | `RUN_SUMMARY` | `CELL_ESTIMATE` | Type | Exact origin, values, and validation |
|---|---|---|---|---|
| `record_type` | required | required | `ENUM` | Literal `RUN_SUMMARY` in the summary row; literal `CELL_ESTIMATE` in every cell row. |
| `run_id` | required | required | `SHA256` | Section 8.1 `run_id`; identical in every row. |
| `configuration_fingerprint` | required | required | `SHA256` | Section 8.1 value; identical in every row. |
| `input_provenance_fingerprint` | required | required | `SHA256` | Section 8.1 value; identical in every row. |
| `seed` | `null` | required | `NULL` or `INT` | Evaluation-cell seed; nonnegative integer in cell rows. |
| `intensity` | `null` | required | `NULL` or `FLOAT_HEX64` | Evaluation-cell intensity, converted from the frozen PR007-A numeric value without changing the grouping value. |
| `estimator_id` | `null` | required | `NULL` or `ENUM` | Exactly `H_hat`, `constant_depth_8`, `constant_depth_26`, `pr006_block_h_hat`, `pr006_intensity_h_hat`, or `constant_depth_4`. |
| `estimator_role` | `null` | required | `NULL` or `ENUM` | `H_hat` -> `AUDITED_ESTIMATOR`; four primary baselines -> `PRIMARY_BASELINE`; `constant_depth_4` -> `DEGENERATE_ORACLE_SANITY_CHECK`. |
| `predicted_depth` | `null` | required | `NULL` or `INT` | Audited estimator value or frozen baseline prediction for the cell; integer in `[1,26]`. |
| `agrees_with_H4` | `null` | required | `NULL` or `BOOL` | `true` iff `predicted_depth = 4`; otherwise `false`. |
| `included_in_primary_max` | `null` | required | `NULL` or `BOOL` | `true` exactly for the four `PRIMARY_BASELINE` IDs; `false` for `H_hat` and `constant_depth_4`. |
| `terminal_label` | required | required | `ENUM` | Exactly one preregistered label: `FAILED_RUNTIME`, `FAILED_DATA_CONTRACT`, `FAILED_LEAKAGE_AUDIT`, `BASELINE_DOMINATED`, `PASSED_BASELINE_AND_LEAKAGE_AUDIT`, or `INCONCLUSIVE`; identical in every row. |
| `h_hat_cell_agreement_with_H4` | required or `null` | `null` | `FLOAT_HEX64` or `NULL` | Serialized name of preregistered `cell_agreement_with_H4(H_hat)`; required for the three non-failure labels and `null` for the three `FAILED_*` labels. |
| `max_baseline_cell_agreement_with_H4` | required or `null` | `null` | `FLOAT_HEX64` or `NULL` | Frozen primary maximum; required for the three non-failure labels and `null` for the three `FAILED_*` labels. |
| `delta_agreement` | required or `null` | `null` | `FLOAT_HEX64` or `NULL` | Frozen difference from preregistration Section 7; required for the three non-failure labels and `null` for the three `FAILED_*` labels. |
| `H_hat_block` | required or `null` | `null` | `INT` or `NULL` | Frozen secondary summary in `[1,26]`; required for the three non-failure labels and `null` for the three `FAILED_*` labels. |
| `cell_fraction_H4` | required or `null` | `null` | `FLOAT_HEX64` or `NULL` | Frozen secondary summary; required for the three non-failure labels and `null` for the three `FAILED_*` labels. |

The three failure labels are exactly `FAILED_RUNTIME`, `FAILED_DATA_CONTRACT`, and
`FAILED_LEAKAGE_AUDIT`. The three non-failure labels are exactly
`BASELINE_DOMINATED`, `PASSED_BASELINE_AND_LEAKAGE_AUDIT`, and `INCONCLUSIVE`.

`h_hat_cell_agreement_with_H4` is the implementation and serialization name for the
preregistered quantity `cell_agreement_with_H4(H_hat)` from the frozen PR008
preregistration Section 7, `Comparison Metric`. It must be computed exactly according to
that frozen formula. These are not two metrics. No alternative normalization,
aggregation, weighting, thresholding, or missing-value policy is permitted. Statistical
descriptions must use `cell_agreement_with_H4(H_hat)`; only serialized output fields use
`h_hat_cell_agreement_with_H4`.

There is exactly one `RUN_SUMMARY`, and it is the first data row. For a failure label,
there are zero `CELL_ESTIMATE` rows. For a non-failure label, there are exactly six cell
rows for every complete PR007-A `(seed, intensity)` evaluation cell, with uniqueness key
`(seed, intensity, estimator_id)` and no duplicate. Cell rows are sorted by numeric
`seed`, then numeric `intensity`, then this estimator order: `H_hat`,
`constant_depth_8`, `constant_depth_26`, `pr006_block_h_hat`,
`pr006_intensity_h_hat`, `constant_depth_4`. Unknown row classes, partial cell groups,
duplicates, extra rows, wrong order, wrong null placement, unequal shared identifiers or
labels, and any other table violation give `FAILED_OUTPUT_CONTRACT` and invalidate the
entire output set.

### 8.1 Cryptographic Identifier Contract

All three identifiers use unkeyed SHA-256 as specified by FIPS PUB 180-4. No salt, key,
prefix, or truncation is used. Each digest is exactly 64 lowercase hexadecimal ASCII
characters.

Identifier payloads use this single canonical `key=value` encoding:

- Keys are the exact case-sensitive ASCII keys listed below and occur exactly once in
  the listed order. Extra, missing, or reordered records are invalid.
- Each record is the ASCII key, one `=` byte (`0x3d`), the encoded scalar value, and one
  LF byte (`0x0a`). The payload has a final LF and no BOM, blank line, CR, or trailing
  space.
- Strings are normalized to Unicode NFC, encoded as UTF-8, and then byte-escaped. ASCII
  bytes in `[A-Za-z0-9._~/-]` remain literal; every other byte is `%HH`, where `HH` is
  uppercase hexadecimal. This escapes `%`, `=`, CR, LF, spaces, and all non-ASCII bytes.
- Paths are case-preserving repository-relative POSIX strings with `/` separators, no
  leading `./` or `/`, and no `.` or `..` component. They then use the string encoding
  above. Symlinks are not resolved for the serialized path value.
- Booleans are the ASCII strings `true` and `false`. Integers are base-10 ASCII with no
  leading `+` or leading zero, except that zero is `0`; negative integers use one leading
  `-`. Finite floating-point values are converted to IEEE 754 binary64, ordered as eight
  big-endian bytes, and serialized as exactly 16 lowercase hexadecimal characters with
  no prefix, separators, or spaces. Decimal notation, scientific notation, and any
  language- or platform-dependent representation are prohibited. Negative zero is
  normalized to positive zero before serialization and is therefore encoded as
  `0000000000000000`. `NaN`, `+Infinity`, and `-Infinity` are prohibited in every
  canonical payload.
- Null is the ASCII string `null`. A required field must not be omitted; null is allowed
  only where its field definition below explicitly permits it.

`configuration_fingerprint` is SHA-256 over the canonical payload with these fields:

| Order | Key | Type | Exact value |
|---:|---|---|---|
| 1 | `fingerprint_schema` | string | `pr008-configuration-v1` |
| 2 | `preregistration_path` | path | `dev/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_PREREGISTRATION.md` |
| 3 | `preregistration_sha256` | string | 64-character lowercase SHA-256 of the preregistration's exact raw file bytes |
| 4 | `implementation_plan_path` | path | `dev/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_IMPLEMENTATION_PLAN.md` |
| 5 | `implementation_plan_sha256` | string | 64-character lowercase SHA-256 of this plan's exact raw file bytes |
| 6 | `production_command` | string | `python3 dev/audit_pr008_h_hat_baseline_leakage.py` |

The two file digests in this payload hash raw bytes exactly as stored; no Unicode or
newline normalization is applied before those file digests. Hashing this plan does not
create a cycle because the computed fingerprint is written only to future outputs and is
never inserted into this plan.

`input_provenance_fingerprint` is SHA-256 over the canonical payload with these fields:

| Order | Key | Type | Exact value |
|---:|---|---|---|
| 1 | `fingerprint_schema` | string | `pr008-input-provenance-v1` |
| 2 | `artifact_01_path` | path | `dev/PR006_ORDER_ONLY_H_HAT_PREREGISTRATION.md` |
| 3 | `artifact_02_path` | path | `data/reports/PR006_ORDER_ONLY_H_HAT_VALIDATION_REPORT.md` |
| 4 | `artifact_03_path` | path | `data/reports/pr006_order_only_h_hat_validation.csv` |
| 5 | `artifact_04_path` | path | `dev/PR007_H_HAT_ROBUSTNESS_PREREGISTRATION.md` |
| 6 | `artifact_05_path` | path | `data/reports/PR007_H_HAT_ROBUSTNESS_VALIDATION_REPORT.md` |
| 7 | `artifact_06_path` | path | `data/reports/pr007_h_hat_robustness_seed_density.csv` |
| 8 | `artifact_07_path` | path | `dev/PR007_A_H_HAT_ROBUSTNESS_CLOSURE_DECISION.md` |
| 9 | `artifact_03_sha256` | string or null | observed lowercase SHA-256 of artifact 03 raw bytes, or null if unavailable |
| 10 | `artifact_06_sha256` | string or null | observed lowercase SHA-256 of artifact 06 raw bytes, or null if unavailable |

Observed CSV digests are computed over raw bytes with no normalization. A valid data
contract still requires them to equal the two frozen hashes in the preregistration;
recording an observed mismatch does not make it valid.

`run_id` is SHA-256 over the canonical payload with these fields:

| Order | Key | Type | Exact value |
|---:|---|---|---|
| 1 | `run_id_schema` | string | `pr008-run-id-v1` |
| 2 | `configuration_fingerprint` | string | the complete 64-character `configuration_fingerprint` |
| 3 | `input_provenance_fingerprint` | string | the complete 64-character `input_provenance_fingerprint` |

Thus `run_id` depends only on the two already computed fingerprints. Neither fingerprint
depends on `run_id`, an output file, a terminal label, a metric value, or any result, so
the dependency graph is acyclic.

## 9. Report Contract

The Markdown report contains exactly these sections in order:

1. Scope and frozen input identities.
2. Data-contract checks and counts.
3. Leakage guard evidence: accessed paths and calculation columns.
4. Frozen baseline definitions and roles.
5. Primary comparison metrics.
6. Frozen secondary summaries.
7. `DEGENERATE_ORACLE_SANITY_CHECK`, explicitly excluded from primary logic.
8. Terminal-label evaluation and the single assigned label.
9. Interpretation limits copied from the preregistration.

The report must not add plots, geometric readouts, exploratory subgroups, alternative
metrics, or narrative rescue of a failed, dominated, or inconclusive outcome.

### 9.1 Machine-Readable Report Block

The report is UTF-8 without BOM and uses LF record terminators. It contains exactly one
machine-readable block. The block begins with the literal line
`BEGIN_PR008_MACHINE_READABLE_V1` plus LF and ends with the literal line
`END_PR008_MACHINE_READABLE_V1` plus LF. Between them there is exactly one `key=value`
assignment per line, using Section 8.1 scalar encoding, keys, `=` separator, escaping,
and final LF rules. Delimiters are not payload records. Blank lines, comments, duplicate,
unknown, missing, or reordered keys, malformed values, additional blocks, and malformed
or missing delimiters give `FAILED_OUTPUT_CONTRACT`.

The keys occur exactly in this order:

| Order | Key | Type | Exact value, source, and null rule |
|---:|---|---|---|
| 1 | `machine_schema` | `ENUM` | Literal `pr008-machine-readable-v1`. |
| 2 | `run_id` | `SHA256` | Section 8.1 value; must match CSV `RUN_SUMMARY`. |
| 3 | `configuration_fingerprint` | `SHA256` | Section 8.1 value; must match CSV. |
| 4 | `input_provenance_fingerprint` | `SHA256` | Section 8.1 value; must match CSV. |
| 5 | `publication_status` | `ENUM` | Literal `VALID`; partial or failed sets cannot supply a valid report block. |
| 6 | `terminal_label` | `ENUM` | One of the six preregistered terminal labels; must match every CSV row. |
| 7 | `artifact_01_path` | `PATH` | `dev/PR006_ORDER_ONLY_H_HAT_PREREGISTRATION.md`. |
| 8 | `artifact_02_path` | `PATH` | `data/reports/PR006_ORDER_ONLY_H_HAT_VALIDATION_REPORT.md`. |
| 9 | `artifact_03_path` | `PATH` | `data/reports/pr006_order_only_h_hat_validation.csv`. |
| 10 | `artifact_04_path` | `PATH` | `dev/PR007_H_HAT_ROBUSTNESS_PREREGISTRATION.md`. |
| 11 | `artifact_05_path` | `PATH` | `data/reports/PR007_H_HAT_ROBUSTNESS_VALIDATION_REPORT.md`. |
| 12 | `artifact_06_path` | `PATH` | `data/reports/pr007_h_hat_robustness_seed_density.csv`. |
| 13 | `artifact_07_path` | `PATH` | `dev/PR007_A_H_HAT_ROBUSTNESS_CLOSURE_DECISION.md`. |
| 14 | `artifact_03_sha256` | `SHA256` or `NULL` | Observed raw-byte digest, or `null` exactly when unavailable. |
| 15 | `artifact_06_sha256` | `SHA256` or `NULL` | Observed raw-byte digest, or `null` exactly when unavailable. |
| 16 | `csv_output_path` | `PATH` | `data/reports/pr008_h_hat_baseline_leakage_audit.csv`. |
| 17 | `report_output_path` | `PATH` | `data/reports/PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_REPORT.md`. |
| 18 | `h_hat_cell_agreement_with_H4` | `FLOAT_HEX64` or `NULL` | Must match CSV summary; null exactly under the failure-label rule in Section 8. |
| 19 | `max_baseline_cell_agreement_with_H4` | `FLOAT_HEX64` or `NULL` | Must match CSV summary under the same rule. |
| 20 | `delta_agreement` | `FLOAT_HEX64` or `NULL` | Must match CSV summary under the same rule. |
| 21 | `H_hat_block` | `INT` or `NULL` | Must match CSV summary under the same rule. |
| 22 | `cell_fraction_H4` | `FLOAT_HEX64` or `NULL` | Must match CSV summary under the same rule. |

The report inventory keys 7-15 reconstruct the exact Section 8.1 input-provenance
payload. The validator must recalculate `input_provenance_fingerprint` and require exact
agreement with key 4 and the CSV. Individual inventory fields are not duplicated in the
CSV. The validator must also recalculate `configuration_fingerprint` from the exact raw
preregistration and plan files plus the frozen command, then recalculate `run_id` from
the two validated fingerprints. Missing provenance, failure to recalculate, or any
identifier or shared-field discrepancy gives `FAILED_OUTPUT_CONTRACT`.

Text outside the block is human-readable only: it does not participate in automatic
validation, cannot contradict the block, cannot define provenance or shared fields, and
cannot introduce new normative identifiers, metrics, baselines, results, or labels.

### 9.2 Per-File Publication And Recovery Protocol

The only temporary paths are:

- `data/reports/.pr008_h_hat_baseline_leakage_audit.csv.tmp`;
- `data/reports/.PR008_H_HAT_BASELINE_LEAKAGE_AUDIT_REPORT.md.tmp`.

Before any production or retry, the implementation must inspect both final and temporary
paths and then apply this sequence:

1. Delete both temporary paths if present.
2. If exactly one final exists, classify the existing set as `PARTIALLY_PUBLISHED` and
   delete that final.
3. If both finals exist but fail individual or cross-validation, classify the existing
   set as `FAILED_OUTPUT_CONTRACT` and delete both finals.
4. If both finals form a valid set, preserve them and refuse a new production or retry.
5. Verify that a permitted new attempt starts with neither temporary nor final present.
   Failure to establish this empty state aborts the attempt as a publication failure.

No invalid file is retained as an interpretable output, and cleanup creates no additional
artifact. `PARTIALLY_PUBLISHED` and `FAILED_OUTPUT_CONTRACT` are execution-publication
diagnoses only when cleanup is required.

For a permitted new attempt, publish the CSV first and the report second. For each file:

1. Write only to its defined temporary path on the same filesystem as its final path.
2. Flush user-space buffers, call `fsync` on the open file descriptor, and close it.
3. Validate the entire closed temporary file against its normative contract.
4. Atomically replace or rename the validated temporary at its final path.
5. Never parse or interpret the temporary as a final output.

There is no joint atomicity guarantee. After publishing the CSV and before publishing
the report, the set is `PARTIALLY_PUBLISHED` and is not interpretable.

On any exception, interruption, or failure before final pair validation, the
implementation must close every open descriptor, delete both temporary paths, delete
every final published during that attempt, verify both final paths are absent, classify
the attempt as `FAILED_OUTPUT_CONTRACT`, and prohibit interpretation of every fragment.

After both finals are published, the implementation must verify that no temporary exists,
validate each final independently, validate the Section 9.1 block, recalculate all three
identifiers, and require exact agreement for `run_id`, `configuration_fingerprint`,
`input_provenance_fingerprint`, terminal label, and all five summary fields. Any failure
gives `FAILED_OUTPUT_CONTRACT`, requires deletion of both finals, and prohibits
interpretation. Only a coherent pair with no temporary is valid and interpretable.

`PARTIALLY_PUBLISHED` and `FAILED_OUTPUT_CONTRACT` remain
`PLAN_DEFINED_IMPLEMENTATION_DETAIL` publication statuses. They never enter, replace,
or change the frozen PR008 terminal labels or precedence.

## 10. Synthetic Test Matrix

Implementation verification must use synthetic fixtures only. It must not open the real
PR006 or PR007-A CSVs and must cover:

- odd and even lower medians, first empty at depths `1` and `25`, and sentinel `26`;
- missing artifact, hash mismatch, missing/malformed column, duplicate raw key,
  incomplete depth coverage, and `K != 8`;
- missing PR006 seed/intensity and duplicate derived PR006 cells;
- exact six-seed intensity aggregation and independence from evaluation seed values;
- all four primary baseline IDs with no additional ID accepted;
- mandatory `constant_depth_4` emission and exclusion from every primary calculation;
- exact cell agreement, maximum baseline agreement, and `delta_agreement` boundaries;
- `BASELINE_DOMINATED` on equality;
- pass, dominated, inconclusive, leakage failure, data-contract failure, and runtime
  failure cases;
- simultaneous failure flags proving the exact terminal precedence and single-label
  assignment;
- rejection of path/CLI overrides and forbidden calculation columns;
- exact CSV schema, mandatory summary row, no partial failure rows, roles, ordering,
  report sections, and matching terminal labels in both outputs;
- exact CSV dialect, null matrix, row invariants, report delimiters, key order, and
  machine-readable types;
- byte-identical serialization from repeated runs over the same synthetic fixture.

Passing repeatability alone is insufficient. Every known-answer and negative vector in
Sections 10.1-10.5 must pass exactly before implementation approval.

### 10.1 Canonical Serialization Known-Answer Vector

This entire subsection is `TEST_VECTOR_ONLY`. Semantic inputs, in order, are: string
`TEST_VECTOR_ONLY`; ASCII string `alpha`; decomposed Unicode string U+0065 U+0301;
reserved-character string consisting of `a,b=c%` followed by LF; path
`tests/vector.txt`; boolean `true`; integer `-7`; float `1.5`; float `-0.0`; and null.

After NFC normalization and Section 8.1 encoding, the exact payload is the following;
the final displayed record is followed by one LF:

```text
vector_schema=TEST_VECTOR_ONLY
ascii=alpha
unicode=%C3%A9
reserved=a%2Cb%3Dc%25%0A
path=tests/vector.txt
boolean=true
integer=-7
float_positive=3ff8000000000000
float_negative_zero=0000000000000000
null_value=null
```

The exact payload bytes, as one uninterrupted lowercase hexadecimal sequence, are:

```text
766563746f725f736368656d613d544553545f564543544f525f4f4e4c590a61736369693d616c7068610a756e69636f64653d2543332541390a72657365727665643d6125324362253344632532352530410a706174683d74657374732f766563746f722e7478740a626f6f6c65616e3d747275650a696e74656765723d2d370a666c6f61745f706f7369746976653d336666383030303030303030303030300a666c6f61745f6e656761746976655f7a65726f3d303030303030303030303030303030300a6e756c6c5f76616c75653d6e756c6c0a
```

Expected SHA-256:
`dfc42ccbf753154ff7c74cfe46a7a1c5b0a3cfa1866002189431a5fbfd053726`.

### 10.2 Float Known-Answer And Rejection Vectors

| Semantic input | Required `FLOAT_HEX64` |
|---|---|
| `0.0` | `0000000000000000` |
| `-0.0` | `0000000000000000` after mandatory normalization |
| `1.0` | `3ff0000000000000` |
| `-1.0` | `bff0000000000000` |
| `1.5` | `3ff8000000000000` |

The serializer must reject semantic `NaN`, `+Infinity`, and `-Infinity`. The parser must
reject `0x3ff0000000000000`, `3FF0000000000000`, any 15- or 17-character hexadecimal
value, `1.0`, and `1e0` as `FLOAT_HEX64`.

### 10.3 Fingerprint And Run-ID Known-Answer Vectors

All values in this subsection are `TEST_VECTOR_ONLY`; each payload ends with one LF.

Configuration payload:

```text
fingerprint_schema=pr008-configuration-v1
preregistration_path=tests/preregistration.md
preregistration_sha256=0000000000000000000000000000000000000000000000000000000000000000
implementation_plan_path=tests/implementation_plan.md
implementation_plan_sha256=1111111111111111111111111111111111111111111111111111111111111111
production_command=python3%20tests/audit.py
```

Expected `configuration_fingerprint`:
`479af5244d580f6cd3ca938e7644a2c852b90a6a7d00259609d9fb812681b66e`.

Input-provenance payload:

```text
fingerprint_schema=pr008-input-provenance-v1
artifact_01_path=tests/input_01.md
artifact_02_path=tests/input_02.md
artifact_03_path=tests/input_03.csv
artifact_04_path=tests/input_04.md
artifact_05_path=tests/input_05.md
artifact_06_path=tests/input_06.csv
artifact_07_path=tests/input_07.md
artifact_03_sha256=2222222222222222222222222222222222222222222222222222222222222222
artifact_06_sha256=3333333333333333333333333333333333333333333333333333333333333333
```

Expected `input_provenance_fingerprint`:
`3a711d1b4019ace446653eb3ee6e2c167ddb6ac9b9311b8ff950afc409a1c4b4`.

Run-ID payload, using exactly those two expected fingerprints:

```text
run_id_schema=pr008-run-id-v1
configuration_fingerprint=479af5244d580f6cd3ca938e7644a2c852b90a6a7d00259609d9fb812681b66e
input_provenance_fingerprint=3a711d1b4019ace446653eb3ee6e2c167ddb6ac9b9311b8ff950afc409a1c4b4
```

Expected `run_id`:
`220ea523938dcddf34f8f3940133955adee73b6b56da9824e28e4dbea54f38cc`.
This construction contains no terminal label, metric, result, or output content.

### 10.4 Provenance Recalculation And Synthetic Pair Vector

This vector is `TEST_VECTOR_ONLY` and exercises pure validators with the synthetic
constants from Section 10.3; production accepts only the frozen paths in Sections 8.1
and 9.1. The exact machine-readable block is:

```text
BEGIN_PR008_MACHINE_READABLE_V1
machine_schema=pr008-machine-readable-v1
run_id=220ea523938dcddf34f8f3940133955adee73b6b56da9824e28e4dbea54f38cc
configuration_fingerprint=479af5244d580f6cd3ca938e7644a2c852b90a6a7d00259609d9fb812681b66e
input_provenance_fingerprint=3a711d1b4019ace446653eb3ee6e2c167ddb6ac9b9311b8ff950afc409a1c4b4
publication_status=VALID
terminal_label=FAILED_DATA_CONTRACT
artifact_01_path=tests/input_01.md
artifact_02_path=tests/input_02.md
artifact_03_path=tests/input_03.csv
artifact_04_path=tests/input_04.md
artifact_05_path=tests/input_05.md
artifact_06_path=tests/input_06.csv
artifact_07_path=tests/input_07.md
artifact_03_sha256=2222222222222222222222222222222222222222222222222222222222222222
artifact_06_sha256=3333333333333333333333333333333333333333333333333333333333333333
csv_output_path=tests/TEST_VECTOR_ONLY/output.csv
report_output_path=tests/TEST_VECTOR_ONLY/report.md
h_hat_cell_agreement_with_H4=null
max_baseline_cell_agreement_with_H4=null
delta_agreement=null
H_hat_block=null
cell_fraction_H4=null
END_PR008_MACHINE_READABLE_V1
```

Every displayed line, including the end delimiter, ends with LF. The corresponding exact
synthetic CSV is the following two LF-terminated records:

```text
record_type,run_id,configuration_fingerprint,input_provenance_fingerprint,seed,intensity,estimator_id,estimator_role,predicted_depth,agrees_with_H4,included_in_primary_max,terminal_label,h_hat_cell_agreement_with_H4,max_baseline_cell_agreement_with_H4,delta_agreement,H_hat_block,cell_fraction_H4
RUN_SUMMARY,220ea523938dcddf34f8f3940133955adee73b6b56da9824e28e4dbea54f38cc,479af5244d580f6cd3ca938e7644a2c852b90a6a7d00259609d9fb812681b66e,3a711d1b4019ace446653eb3ee6e2c167ddb6ac9b9311b8ff950afc409a1c4b4,null,null,null,null,null,null,null,FAILED_DATA_CONTRACT,null,null,null,null,null
```

Recalculation from the seven ordered paths and two hashes must produce
`3a711d1b4019ace446653eb3ee6e2c167ddb6ac9b9311b8ff950afc409a1c4b4`, equal to both
stored values; the pair then passes this provenance check. Altering any path, hash, key
order, or stored fingerprint must give `FAILED_OUTPUT_CONTRACT`.

### 10.5 Publication State Vectors

These are implementation-contract tests, not PR008 results:

| Initial synthetic state | Mandatory result |
|---|---|
| No temporary and no final | Clean; production permitted. |
| One or both temporaries present, no final | Delete all temporaries, verify empty, then permit production. |
| Only CSV final | `PARTIALLY_PUBLISHED`; delete CSV and all temporaries, verify empty. |
| Only report final | `PARTIALLY_PUBLISHED`; delete report and all temporaries, verify empty. |
| Both finals, one individually invalid | `FAILED_OUTPUT_CONTRACT`; delete both and all temporaries, verify empty. |
| Both individually valid, fingerprints differ | `FAILED_OUTPUT_CONTRACT`; delete both and all temporaries, verify empty. |
| Coherent pair plus residual temporary | Invalid until the temporary is deleted and the complete pair is revalidated. |
| Interruption after first final publication | Delete that final and all temporaries; leave both finals absent. |
| Coherent, cross-validated pair and no temporary | Valid and interpretable; preserve pair and refuse a new production. |

Negative conformance cases must also reject every unknown or duplicate CSV row, column,
machine-block key, block, delimiter, missing required value, invalid null placement,
wrong row/key order, CRLF output, malformed quote, and unexpected empty field. Each
publication vector must end in exactly the listed state.

## 11. Traceability Matrix

| Frozen preregistration section | Implementation responsibility | Verification |
|---|---|---|
| Section 2 | `lower_median`, `derive_h_hat` | estimator unit cases |
| Sections 3-5 | fixed I/O, projection, leakage guard | path/column rejection cases |
| Section 6 | reference and constant baseline builders | exact-ID and oracle-exclusion cases |
| Section 7 | `cell_agreement_with_H4(H_hat)` and other metric functions | formula, alias-mapping, and boundary cases |
| Section 8 | inherited output paths; CSV dialect, table, identifiers | schema, row, float, and known-answer cases |
| Sections 9-10 | report block, publication recovery, terminal assignment | block, recovery, pair, and precedence cases |
| Section 11 | plan-defined fixed CLI prevents post-result changes | override-rejection and source review |
| Section 12 | fixed report interpretation limits | report structure review |

## 12. Authorization Gates

The sequence is mandatory:

1. Read-only audit and approval of this implementation plan.
2. Separate authorization to implement the two code/test files.
3. Synthetic tests and read-only source audit against the preregistration; no real PR006
   or PR007-A data access by the implementation under test.
4. Exact passage of every Section 10 known-answer vector, byte payload, digest, negative
   rejection, publication state, and the end-to-end synthetic CSV/report pair.
5. Byte-identical repetition over the same synthetic fixture, in addition to and never
   instead of the known-answer tests.
6. Separate explicit authorization to execute the fixed PR008 command.
7. Mechanical verification that both outputs pass their individual contracts and agree
   on all shared fields required by Section 9.2, including recalculation of the report's
   `input_provenance_fingerprint` from its Section 9.1 inventory.
8. Only then, interpretation restricted to the frozen terminal label and claim boundary.

Approval of any gate does not imply approval of the next gate.
