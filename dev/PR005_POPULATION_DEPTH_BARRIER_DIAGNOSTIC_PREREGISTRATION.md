# PR005 Population-Depth Barrier Diagnostic — Preregistration

STATUS: PREREGISTRATION_DRAFT
VALIDATION_STATUS: NOT_RUN
RELATION_TO_PR004: NEW_OBSERVABLE_AFTER_PR004_FAILED_DATA_CONTRACT
ORDER_ONLY_PRIMARY: YES_PENDING_FINAL_CONTRACT
COMMAND_TO_FREEZE_BEFORE_RUN: NOT_SET

## 1. Motivation

PR004 is closed as `FAILED_DATA_CONTRACT`, not repaired in place.

The PR004 V2 validation report established that the implementation-level contract was
structurally satisfied: mandatory columns were present, `lineage_id` continuity was
auditable, path-prefix continuity held, recorded depth gaps were absent, and path lengths
matched `depth_k`. The terminal failure came from the physical/geometry of the output:
individual lineages were too short for a long-lineage primary observable.

PR005 therefore does not change `MIN_LEN`, `K`, `LMAX`, window width, denominators, or
lineage definitions to rescue PR004. It defines a new observable after observing the PR004
failure.

## 2. Physical Question

Can an order-only depth-slice population observable detect an information-barrier or
horizon-like transition in Schwarzschild without requiring long-lived individual beam
lineages?

Operational translation: instead of following one branch for many depths, PR005 evaluates
the population of surviving beam endpoints at each depth slice. Branch death and
replacement are treated as part of the signal, not as a censoring failure.

## 3. Primary Unit

The primary unit is:

```text
(seed, intensity, start_id, K, depth_k)
```

This unit is called a `depth_slice`.

`lineage_id` is not a primary unit and must not appear in the primary denominator.
It may be retained only for secondary diagnostics: turnover, top1 persistence, minbeam
identity changes, and lineage churn.

## 4. Primary Observable

Primary observable:

```text
depth-slice concentration profile
```

For each `depth_slice`, compute the distribution of survivor endpoints using order-only
quantities available from the beam output. Here `endpoint` means causal-set element
identity or beam endpoint identity, not embedded radial position, shell, coordinate, or
horizon-side label:

- endpoint multiplicity profile;
- concentration of endpoint mass in the top survivor ranks;
- entropy-like concentration of survivor identities;
- effective number of occupied endpoint identities;
- slice-to-slice population turnover.

The primary comparison is early-depth versus late-depth behavior within the same
`(seed, intensity, start_id, K)` run.

Endpoint identity must be frozen before any implementation can be used for PR005. The
default candidate is:

```text
endpoint_pair_id = (p_last, q_last)
```

This candidate is order-only as an element-identity pair. It is not a radial coordinate
or horizon-side label.

## 5. Ground-Truth Readouts

The following Schwarzschild-embedded quantities may be reported only as calibration or
diagnostic readouts:

- radial spread;
- modal shell;
- straddle fraction;
- radial location of concentration changes;
- horizon-side balance of endpoints.
- minbeam/top1 agreement, if `minbeam` is defined by embedded radial distance or any
  other non-order-only criterion.

They are not primary order-only features. Any report using them must label them
`GROUND_TRUTH_READOUT / NOT_ORDER_ONLY_EVIDENCE`.

## 6. Mandatory Data Contract

The PR005 output must contain one row per `depth_slice` and must include at least:

- `seed`
- `intensity`
- `K`
- `start_id`
- `depth_k`
- `n_survivors`
- `n_endpoint_identities`
- `top1_endpoint_mass_fraction`
- `top3_endpoint_mass_fraction`
- `endpoint_entropy`
- `effective_endpoint_count`
- `turnover_from_previous_depth`

Optional diagnostic columns may include:

- `radial_spread_over_ell`
- `modal_shell_over_ell`
- `straddle_fraction`
- `minbeam_equals_top1`
- `lineage_turnover`
- `top1_persistence`
- `minbeam_identity_changed`

Rows with `n_survivors == 0` are terminal slice failures for that
`(seed, intensity, start_id, K)` sequence and must be reported, not silently dropped.

## 7. Censoring Rule

PR005 has no long-lineage censoring gate. A depth slice is evaluable if it has at least
one recorded survivor at that depth.

The following are reported as diagnostics, not as exclusion reasons:

- short individual lineage length;
- high lineage turnover;
- top1 identity changes;
- minbeam identity changes;
- disappearance of a lineage that was present at an earlier depth.

If too few depth slices exist to compare early and late windows under the frozen run
parameters, the terminal label is `FAILED_DATA_CONTRACT`, not a recovered PR004 label.

## 8. Required Implementation Change Before Command Freeze

The runner must provide a dedicated PR005 depth-slice output path, distinct from the
existing PR004 `--probe-out` path.

The PR005 output must emit one row per:

```text
depth_slice = (seed, intensity, K, start_id, depth_k)
```

The PR005 output must not apply the PR004 `MIN_LEN` lineage filter before emitting
`depth_slice` rows.

Rows with `n_survivors == 0` must be represented explicitly up to the frozen maximum
depth, because population extinction is part of the observable rather than a censoring
failure.

The existing `--probe-out` flag remains PR004/per-survivor semantics and must not be used
as the frozen PR005 command. Renaming the output path to
`data/reports/pr005_population_depth_barrier_slices.csv` while using `--probe-out` is not
a valid PR005 run.

No flag name for the future PR005 slice output is frozen here.

## 9. Decision Criteria To Freeze Before Run

The final PR005 preregistration must freeze, before any PR005 output is observed:

- the producing command;
- the output path;
- seed set;
- intensity grid;
- K grid or single-K choice;
- maximum depth;
- early-depth window;
- late-depth window;
- primary concentration statistic;
- threshold for `BARRIER_SIGNAL`;
- threshold for `NO_BARRIER_SIGNAL`;
- fallback rule for `INCONCLUSIVE`.

Until those items are frozen, PR005 remains `PREREGISTRATION_DRAFT` and must not be run
as a validating experiment.

## 9.1 Decision Tree To Freeze Before Run

The final PR005 decision tree must start with the data contract:

1. If the frozen command fails, the output path is absent, or mandatory columns are
   missing or malformed: `FAILED_RUNTIME` or `FAILED_DATA_CONTRACT`, as applicable.
2. If the primary order-only `depth_slice` features cannot be computed without radial,
   horizon, shell, straddle, coordinate, or minbeam-ground-truth inputs:
   `FAILED_DATA_CONTRACT`.
3. If too few evaluable depth slices exist to compare the frozen early and late windows:
   `FAILED_DATA_CONTRACT`.
4. Only after steps 1-3 pass may PR005 evaluate `BARRIER_SIGNAL`, `NO_BARRIER_SIGNAL`,
   or `INCONCLUSIVE`.

No `GROUND_TRUTH_READOUT / NOT_ORDER_ONLY_EVIDENCE` column may participate in steps 1-4
except as an optional diagnostic readout after the primary terminal label is fixed.

## 10. Allowed Terminal Labels

Allowed terminal labels:

- `FAILED_RUNTIME`
- `FAILED_DATA_CONTRACT`
- `BARRIER_SIGNAL`
- `NO_BARRIER_SIGNAL`
- `INCONCLUSIVE`

No `CONCENTRATED`, `DISPERSED`, `PEELED`, or PR004 lineage-window label is allowed as a
PR005 terminal label.

## 11. Prohibited Claims

- No claim that PR004 has been rescued.
- No claim that changing PR005 definitions changes the PR004 terminal verdict.
- No horizon reconstruction claim.
- No order-only claim for any statistic that uses embedded radial position, shell,
  straddle status, or horizon-side labels.
- No use of `lineage_id` as a primary denominator.
- No use of the existing PR004 `--probe-out` per-survivor output as the frozen PR005
  command or as a disguised PR005 slice output.
- No post-output threshold adjustment to force `BARRIER_SIGNAL` or `NO_BARRIER_SIGNAL`.

## 12. Future Outputs

- `data/reports/pr005_population_depth_barrier_slices.csv` — NOT_CREATED
- `data/reports/PR005_POPULATION_DEPTH_BARRIER_VALIDATION_REPORT.md` — NOT_CREATED
