# PR005 Population-Depth Barrier Held-Out Validation Report

STATUS: FINAL
CONTRACT_VERDICT: PASS_DATA_CONTRACT
SCIENTIFIC_TERMINAL_LABEL: INCONCLUSIVE

## Scope

This report validates a confirmatory held-out PR005 depth-slice run against the frozen
scientific tree in the preregistration.

- Command:
  `python3 dev/measure_kbeam_peeloff.py --seeds 6 --seed-offset 6 --intensities 4800,9600,19200 --slice-out data/reports/pr005_population_depth_barrier_slices_heldout.csv --probe-k 8`
- Producing code commit: `7ebab56`
- CSV: `data/reports/pr005_population_depth_barrier_slices_heldout.csv`
- CSV SHA256: `a9c719230fbf8842e1230897f522938ed5bee08dbcb55d59db9c9512a155679d`
- Data rows: 49,650
- Sequences `(seed, intensity, K, start_id)`: 1,986

The run completed with pre/post seal checks:

- Pre seal: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
- Post seal: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`

## Contract Checks

- Mandatory CSV prefix matches the PR005 contract: yes.
- Duplicate `(seed, intensity, K, start_id, depth_k)` rows: 0.
- Coverage failures for `depth_k = 1..25`: 0 sequences.
- `EVALUABLE` rows: 6,440.
- `EMPTY` rows: 39,310.

## Frozen Scientific Tree

Held-out summary values:

- `median(first_empty_depth) = 4`
- `empty_fraction(4) = 0.8967774420946626`
- `median(empty_fraction(depth_k), depth_k = 1..3) = 0.01812688821752266`
- `median(empty_fraction(depth_k), depth_k = 5..25) = 0.9818731117824774`

Seed stability at `first_empty_depth <= 4`:

- `1000006`: `0.8317757009345794`
- `1000007`: `0.9096989966555183`
- `1000008`: `0.9145077720207254`
- `1000009`: `0.9171779141104295`
- `1000010`: `0.9100000000000000`
- `1000011`: `0.8954802259887006`

Intensity stability at `first_empty_depth <= 4`:

- `4800.0`: `0.8941176470588236`
- `9600.0`: `0.9028571428571428`
- `19200.0`: `0.8929088277858177`

## Scientific Verdict

`BARRIER_SIGNAL` is not satisfied because at least one seed group falls below the frozen
`0.85` stability requirement for `first_empty_depth <= 4`.

`NO_BARRIER_SIGNAL` is not satisfied because `median(first_empty_depth) = 4`, not `>= 8`.

Terminal label: `INCONCLUSIVE`.

Interpretation: the held-out run reproduces the early-puncture / high-empty-fraction
pattern, but it is not uniform enough across seeds to freeze a barrier claim under the
current tree.
