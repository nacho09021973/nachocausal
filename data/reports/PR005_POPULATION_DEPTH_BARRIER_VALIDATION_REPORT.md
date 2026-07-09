# PR005 Population-Depth Barrier Validation Report

STATUS: FINAL
CONTRACT_VERDICT: PASS_DATA_CONTRACT
SCIENTIFIC_TERMINAL_LABEL: NOT_EVALUATED_THRESHOLDS_NOT_FROZEN

## Scope

This report validates the first PR005 depth-slice CSV output:

- Command:
  `python3 dev/measure_kbeam_peeloff.py --seeds 6 --intensities 3600,7200,14400 --slice-out data/reports/pr005_population_depth_barrier_slices.csv --probe-k 8`
- Producing code commit: `e0ec580`
- CSV: `data/reports/pr005_population_depth_barrier_slices.csv`
- CSV SHA256: `d44720b9b411ce8ed1063741494daa26ba4eb76b4234afab692ea80c5f2e26bd`
- Data rows: 45,750
- Header + data rows: 45,751

The run completed with pre/post seal checks:

- Pre seal: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
- Post seal: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`

## Contract Checks

Mandatory CSV prefix:

- Column order matches the PR005 contract: yes.
- Duplicate `(seed, intensity, K, start_id, depth_k)` rows: 0.
- Sequences `(seed, intensity, K, start_id)`: 1,830.
- Coverage failures for `depth_k = 1..25`: 0 sequences.
- K values present: `8` only.

Slice-status counts:

| status | rows |
|---|---:|
| `EVALUABLE` | 6,440 |
| `EMPTY` | 39,310 |

Rows by intensity:

| intensity | rows | empty rows |
|---:|---:|---:|
| 3600.0 | 13,725 | 11,775 |
| 7200.0 | 15,850 | 13,574 |
| 14400.0 | 16,175 | 13,961 |

Formula checks:

- `slice_status` agrees with `n_survivors`: 0 errors.
- Empty-row payload checks: 0 errors.
- Positive-row count bounds: 0 errors.
- `top1_endpoint_mass_fraction`: 0 errors.
- `top3_endpoint_mass_fraction`: 0 errors.
- `effective_endpoint_count = exp(endpoint_entropy_nats)`: 0 errors.
- `top1_endpoint_pair` JSON shape: 0 errors.
- Basic turnover range and empty-transition checks: 0 errors.

## Scientific Label

No `BARRIER_SIGNAL`, `NO_BARRIER_SIGNAL`, or `INCONCLUSIVE` terminal scientific label is
assigned in this report.

Reason: the CSV contract and command were frozen, and the output passes the data
contract, but the PR005 preregistration still does not freeze the scientific thresholds
for `BARRIER_SIGNAL` / `NO_BARRIER_SIGNAL` or the fallback criterion for `INCONCLUSIVE`.
Assigning one of those labels from this output would be post-output threshold selection.

This report therefore closes only the PR005 depth-slice data-contract question:

```text
PR005 depth-slice CSV contract: PASS_DATA_CONTRACT
Scientific decision tree: NOT_EVALUATED_THRESHOLDS_NOT_FROZEN
```
