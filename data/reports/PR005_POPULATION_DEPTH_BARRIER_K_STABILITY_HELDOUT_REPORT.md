# PR005 Population-Depth Barrier K-Stability Held-Out Report

STATUS: FINAL
CONTRACT_VERDICT: PASS_DATA_CONTRACT
SCIENTIFIC_TERMINAL_LABEL: INCONCLUSIVE

## Scope

This report checks whether the PR005 early-empty transition is stable under beam-width
changes on a held-out seed/intensity block.

- Command:
  `python3 dev/measure_kbeam_peeloff.py --seed-offset 18 --seeds 6 --intensities 4800,9600,19200 --slice-out-prefix data/reports/pr005_k_stability_heldout --slice-k-list 2,4,8,16,32,64 --probe-k 8`
- Producing code commit: `9b74638`
- Output prefix: `data/reports/pr005_k_stability_heldout`

Per-K CSV outputs:

| K | rows | sequences | CSV SHA256 |
|---:|---:|---:|---|
| 2 | 50,075 | 2,003 | `f95d874dfca349b458533584730de1e22aa37546edca5b63a698eeb932324a02` |
| 4 | 50,075 | 2,003 | `2ea34c4dcb65abb9f2b0006574488d6948d8b3a32331f9931dce1b278327e0c3` |
| 8 | 50,075 | 2,003 | `ab1c95eb198c4f8c0863ac23e2197a9a082fcac060bf75d8f633b6d6e5a0c8a4` |
| 16 | 50,075 | 2,003 | `130f21adaf839ba8031f327b4e2526ec6c34db411771e976d8d7e2f02e16ccd1` |
| 32 | 50,075 | 2,003 | `d00c0b1de8228d1c410d54befa888c9abf8c09fae986d3bcbd06e1666e9001b0` |
| 64 | 50,075 | 2,003 | `78509c2a354aab62802e898c289da50bb3dcd1e8c033c23af0a1403bffd67e11` |

The run completed with pre/post seal checks:

- Pre seal: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
- Post seal: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`

## Contract Checks

All six CSVs pass the PR005 depth-slice contract.

- Duplicate `(seed, intensity, K, start_id, depth_k)` rows: 0 in every file.
- Coverage failures for `depth_k = 1..25`: 0 in every file.
- Mandatory primary prefix present and ordered correctly: yes.
- Empty slices are explicit through the frozen maximum depth: yes.

## K-Stability Result

The early-empty transition is not K-invariant.

Summary by K:

| K | median(first_empty_depth) | mean(first_empty_depth) | fraction(first_empty_depth <= 4) | fraction(first_empty_depth <= 8) | empty_fraction(4) |
|---:|---:|---:|---:|---:|---:|
| 2 | 4 | 4.0489 | 0.9591 | 0.9935 | 0.9591 |
| 4 | 4 | 4.2247 | 0.9366 | 0.9810 | 0.9366 |
| 8 | 4 | 4.4898 | 0.9071 | 0.9651 | 0.9071 |
| 16 | 4 | 4.9621 | 0.8497 | 0.9361 | 0.8497 |
| 32 | 4 | 5.9231 | 0.7574 | 0.8782 | 0.7574 |
| 64 | 4 | 7.0924 | 0.6470 | 0.8038 | 0.6470 |

Depth 1..3 remain uniformly low-empty across K:

- `empty_fraction(1) = 0.0`
- `empty_fraction(2) = 0.0235`
- `empty_fraction(3) = 0.0349`

But the transition at depth 4 shifts materially with K:

- `empty_fraction(4)` drops from `0.9591` at `K=2` to `0.6470` at `K=64`.
- The mean first-empty depth increases monotonically from `4.0489` to `7.0924`.

## Interpretation

The transition is stable in the narrow sense that the median first-empty depth stays at
4 for all K values tested.

It is not stable in the stronger sense needed for a K-invariant barrier claim: wider
beams retain evaluable population longer, and the depth-4 vacating fraction degrades
monotonically as K increases.

Scientific readout:

```text
beam-width dependent transition; not yet a K-invariant barrier
```

This is still a valid PR005 result because the data contract passes. It is not a barrier
confirmation.

## PR006 Interpretation Decision

PR006 will not assume K-invariance.

For PR006, `K` is treated as a frozen algorithmic hyperparameter of the estimator.
It is not an invariant physical axis. A multi-K estimator is allowed only if its
aggregation rule is preregistered before validation; otherwise multi-K aggregation
belongs to a later robustness stage.

This fixes the PR006 interpretation as Option A:

- Demonstrate first that there exists a reasonable order-only `H_hat` under a frozen
  estimator contract.
- Do not optimize, average, or select across `K` after seeing validation output.
- Reserve any explicit multi-K aggregation rule for PR007 or a separate robustness
  preregistration.

Closing interpretation:

```text
The K sweep downgrades PR005 from a strong population-depth barrier claim to a
weaker but still useful early-emptying localization signal. PR006 must therefore
treat K as a frozen estimator hyperparameter, not as an invariant physical axis,
unless a multi-K aggregation rule is preregistered before validation.
```
