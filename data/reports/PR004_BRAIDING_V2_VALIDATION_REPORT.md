# PR004 Braiding V2 Validation Report

STATUS: FINAL
TERMINAL_VERDICT: FAILED_DATA_CONTRACT
SPEC_NOTE: SPEC_DEFECT_NON_OUTCOME_CHANGING

## Scope

This report validates the first PR004 braiding V2 single-K output:

- CSV: `data/reports/pr004_braiding_v2_per_lineage.csv`
- CSV SHA256: `5bf3bd5aa0e6d133a62c652e039c2fd8b42652bcfa78eaed7c56dfb97144720b`
- Rows: 5,789
- Lineages: 3,396
- Seeds: 6 (`1000000` through `1000005`)
- Intensities: `3600.0`, `7200.0`, `14400.0`
- K: `8`

No downstream MEDIAN3, STRADDLE_LOSS, CONCENTRATED, DISPERSED, or INCONCLUSIVE
classification is evaluated here, because the frozen decision tree stops at the
data-contract/censoring gate.

## Data Contract Checks

Mandatory schema check:

- Required columns present: 20 / 20
- Column order matches the V2 preregistration: yes
- Missing mandatory columns: 0

Lineage and path audit:

- `lineage_id` grouping checked by `(seed, intensity, K, start_id, lineage_id)`.
- Recorded `depth_k` values are consecutive within every recorded lineage: 0 gaps.
- Duplicate recorded depths within a lineage: 0.
- `path_p` and `path_q` prefix continuity mismatches: 0.
- `p_last` / `q_last` mismatches against final path entries: 0.
- Rows with `len(path_p) != depth_k` or `len(path_q) != depth_k`: 0.

Implementation-contract conclusion: the output is structurally valid. The failure below is
not caused by a broken schema, broken lineage persistence, path discontinuity, depth gaps,
or path-length mismatch.

## Chain-Length Distribution

| chain_len | lineages |
|---:|---:|
| 1 | 2,385 |
| 2 | 433 |
| 3 | 245 |
| 4 | 129 |
| 5 | 90 |
| 6 | 48 |
| 7 | 27 |
| 8 | 17 |
| 9 | 7 |
| 10 | 8 |
| 11 | 4 |
| 12 | 2 |
| 13 | 1 |

Derived survival counts:

- `chain_len >= 3`: 578 / 3,396 = 17.0200%.
- `chain_len >= MIN_LEN` with `MIN_LEN = 6`: 114 / 3,396 = 3.3569%.

## Censoring Gate

The V2 preregistration contains a denominator ambiguity between the prose rules in
section 4 and the summary/decision-tree wording in sections 5 and 6. The ambiguity does
not change the terminal outcome.

Under the all-lineages interpretation:

- `UNDEFINED_TOO_SHORT` for the MEDIAN3 window (`chain_len < 3`): 2,818 / 3,396 =
  82.9800%.
- `chain_len < MIN_LEN` sensitivity (`chain_len < 6`): 3,282 / 3,396 = 96.6431%.

Under the evaluable-denominator wording:

- `UNDEFINED_TOO_SHORT` divided by `chain_len >= 3` lineages: 2,818 / 578 =
  487.5433%.
- `chain_len < MIN_LEN` divided by `chain_len >= MIN_LEN` lineages: 3,282 / 114 =
  2,878.9474%.

In every reading, the censoring/too-short mass exceeds the frozen 30% gate by a wide
margin.

## Terminal Verdict

Terminal verdict: `FAILED_DATA_CONTRACT`.

Reason: combined data-contract/censoring gate fails because `UNDEFINED_TOO_SHORT`
exceeds the 30% threshold by either denominator interpretation. Downstream `MEDIAN3`,
`STRADDLE_LOSS`, `CONCENTRATED`, `DISPERSED`, and `INCONCLUSIVE` labels are not evaluated
under the frozen section 6 stop rule.

The denominator inconsistency is recorded as `SPEC_DEFECT_NON_OUTCOME_CHANGING`, not as
`FAILED_SPEC_AMBIGUITY`, because the terminal label is identical under both readings.
