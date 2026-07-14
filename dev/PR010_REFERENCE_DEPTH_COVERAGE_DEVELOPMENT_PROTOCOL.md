# PR010 Reference Depth-Coverage Development Protocol

STATUS: PROTOCOL_ONLY / PENDING_TEXT_AUDIT
SCOPE: DEVELOPMENT_COVERAGE_ONLY / NO_CODE / NO_EXECUTION
NORMATIVE_DECISION: `dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md`
FROZEN_DECISION_SHA: `ff98ae1`

## 1. Purpose and Non-Authorization

This protocol specifies the complete development-only coverage measurement required by
the frozen PR010 decision. It does not authorize implementation, generation of any seed,
execution, confirmatory preregistration, or scientific scoring.

The development question is only whether the fixed transition window
`depth_k = {3,4,5}` has adequate independent seed-level support under the frozen design.
No width, expansion value, geometry, effect, or PR009 value is a development result.

## 2. Fixed Program Surfaces and Commands

The future implementation may create exactly these program surfaces:

```text
dev/run_pr010_reference_depth_coverage_development.py
dev/evaluate_pr010_reference_depth_coverage_development.py
```

The sole generator command is:

```text
python3 dev/run_pr010_reference_depth_coverage_development.py
```

The separate evaluator command is:

```text
python3 dev/evaluate_pr010_reference_depth_coverage_development.py
```

Neither program accepts positional arguments, options, environment-driven configuration
overrides, alternate paths, seed bands, depth ranges, resource limits, or output formats.
Any argument produces an operational refusal before generation or artifact reading.

The generator is the only program allowed to call the sprinkling generator or construct
the coverage artifact. The evaluator must not import or call a sprinkling generator,
construct a causal relation, run a beam, or reconstruct omitted values. It reads only the
final CSV and sidecar named below.

## 3. Frozen Development Configuration

The generator constants are exactly:

```text
DEVELOPMENT_SEEDS = 1101000..1101023
N_DEVELOPMENT_SEEDS = 24
SPACETIME_KINDS = BH,MINK
INTENSITY = 4800
M = 3
K = 64
MAX_STARTS = 40
REQUIRED_SLICES = 3..6
TRANSITION_DEPTHS = 3,4,5
```

Seeds are processed in ascending order. Each seed uses the same sprinkled point set for
its matched `BH` and `MINK` causal relations. Kind order is `BH` then `MINK`. The runner
must materialize enough order-only state for slices 3 through 6 and must not generate or
retain any development output row outside transition depths 3 through 5.

The runner must refuse any seed, kind, intensity, `M`, `K`, start count, required slice,
or transition depth outside this block. PR009 seeds and the reserved PR010 confirmatory
bands are forbidden.

## 4. Independent Unit and Support Predicate

The independent unit is exactly:

```text
(seed, spacetime_kind, depth_k)
```

Starts are nested within a seed and never count as independent observations. For each
unit, count the emitted starts and the starts whose transition at `depth_k` is evaluable.
A transition is evaluable only when both its current and following slices satisfy the
frozen order-only width-evaluability predicate. The numeric widths and any derived
expansion values are transient implementation details and may not be serialized, logged,
returned by the evaluator, or exposed through an auxiliary artifact.

The support predicate is exactly:

```text
seed_depth_supported = 1  if n_transition_evaluable_starts >= 5
seed_depth_supported = 0  otherwise
```

No other support state, missing state, rescue rule, weighting, interpolation, or
cross-seed pooling is allowed.

## 5. Frozen Artifact Set

The only development artifact set is:

```text
CSV = data/reports/pr010_reference_depth_coverage_development.csv
SIDECAR = data/reports/pr010_reference_depth_coverage_development.sha256
CSV_TMP = data/reports/pr010_reference_depth_coverage_development.csv.tmp
SIDECAR_TMP = data/reports/pr010_reference_depth_coverage_development.sha256.tmp
```

The CSV header is exactly this single comma-delimited line:

```text
seed,spacetime_kind,depth_k,n_emitted_starts,n_transition_evaluable_starts,seed_depth_supported
```

The CSV contains exactly 144 data rows:

```text
24 seeds x 2 spacetime kinds x 3 transition depths = 144
```

Row order is lexicographic under these frozen categorical orders:

1. `seed`: `1101000` through `1101023` ascending;
2. `spacetime_kind`: `BH`, then `MINK`;
3. `depth_k`: `3`, `4`, `5`.

Each primary key appears exactly once. Integer fields use unsigned base-10 notation.
`seed_depth_supported` is the literal `0` or `1`. The CSV uses UTF-8, comma delimiter,
RFC-4180 quoting only if required, LF line endings, and one final newline. Empty fields,
extra columns, comments, `NA`, booleans other than `0/1`, negative integers, and duplicate
or missing keys are forbidden.

For every row:

```text
0 <= n_emitted_starts <= 40
0 <= n_transition_evaluable_starts <= n_emitted_starts
seed_depth_supported == int(n_transition_evaluable_starts >= 5)
```

## 6. Forbidden Information

The CSV, sidecar, stdout, stderr, exceptions, logs, temporary files, and evaluator output
must not serialize or reveal:

- width values or pair-separation values;
- `theta_raw`, `theta_residual`, or any expansion statistic;
- embedding coordinates, radii, zones, horizon labels, distances, or truth fields;
- signs, contrasts, p-values, effect sizes, or scientific terminal statistics;
- survivor identities, paths, rung identifiers, or per-start rows;
- any PR009 seed, row, artifact value, cached value, or reconstructed unpublished value.

Only fixed metadata, the six CSV fields, publication status, validation errors that do not
reveal forbidden values, and the exact terminal line defined below may be exposed.

## 7. Atomic Publication and Sidecar

The generator must fail closed before generation if any final or temporary path already
exists. Existing artifacts are never overwritten, appended, repaired in place, or used to
resume a partial run.

After all 24 seeds, both kinds, and all required slices complete within budget, the runner
must validate the full in-memory 144-row artifact before writing. Publication order is:

1. create `CSV_TMP` exclusively, write all CSV bytes, flush, and `fsync`;
2. compute lowercase SHA-256 over the exact persisted CSV bytes;
3. create `SIDECAR_TMP` exclusively with exactly:
   `<sha256><two spaces><CSV basename><LF>`, then flush and `fsync`;
4. reread and validate both temporary files and their digest relation;
5. atomically replace `CSV_TMP` with `CSV`;
6. atomically replace `SIDECAR_TMP` with `SIDECAR` as the commit marker;
7. `fsync` the containing directory.

The artifact set is valid only when both final files exist and the sidecar matches the CSV
bytes. A lone final, lone temporary, mixed final/temporary set, malformed sidecar, or hash
mismatch is never a partial success.

Any caught exception during write, validation, rename, or directory sync must remove all
temporary and final paths created by that invocation. If cleanup cannot restore the absent
pre-run state, the terminal is `PR010_FAILED_RUNTIME`; no rerun or manual artifact repair is
authorized by this protocol.

On successful publication the generator prints exactly:

```text
PR010_DEVELOPMENT_COVERAGE_PUBLISHED
```

It does not compute or print the coverage terminal.

## 8. Separate Evaluator and Mechanical Terminal

The evaluator first validates, without generating data:

- both final files exist and no temporary path exists;
- sidecar syntax, basename, and SHA-256;
- exact header, serialization, final newline, and 144-row count;
- exact key set and frozen row order;
- seed, kind, and depth membership;
- integer domains and the support predicate;
- absence of every forbidden or extra field.

For each of the six cells in:

```text
{BH,MINK} x {3,4,5}
```

the evaluator sums `seed_depth_supported` over the 24 independent seeds. It performs no
pooling across kind or depth and uses no partial row set.

The exact valid-artifact terminal is:

```text
PASS_DEVELOPMENT_COVERAGE
    if all six cells have at least 22 of 24 supported seeds

PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE
    otherwise
```

This integer rule is the frozen mechanical equivalent of the Clopper-Pearson/binomial-tail
rule in the decision document. The evaluator must not recompute, relax, round, tune, or
replace the threshold.

For a valid complete artifact, the evaluator prints exactly one line to stdout:

```text
PR010_DEVELOPMENT_TERMINAL=<terminal>
```

Both valid-artifact terminals exit zero. `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE` is a
binding design result: it forbids confirmatory preregistration, extension, replacement,
supplementation, or rerun of this development band.

## 9. Operational Failures and Precedence

Operational precedence is:

```text
PR010_FAILED_RUNTIME
> PR010_FAILED_DATA_CONTRACT
> PR010_FAILED_BUDGET
> PASS_DEVELOPMENT_COVERAGE or PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE
```

Definitions are:

- `PR010_FAILED_RUNTIME`: unexpected exception, incomplete or failed atomic publication,
  cleanup failure, unreadable required path, or evaluator/generator boundary violation not
  classified below;
- `PR010_FAILED_DATA_CONTRACT`: wrong command shape, unauthorized configuration, malformed
  or incomplete CSV/sidecar, schema/key/order/domain/support-predicate drift, forbidden
  field or value exposure, hash mismatch, or evaluator use of anything outside the final
  artifact pair;
- `PR010_FAILED_BUDGET`: a classified wall-time, aggregate-CPU, peak-memory, process-count,
  or thread-count breach before any higher-precedence failure.

An operational failure prints exactly one line to stderr and exits nonzero:

```text
PR010_DEVELOPMENT_TERMINAL=<operational failure>
```

No operational failure may be relabeled as either valid-artifact terminal. A generator
operational failure publishes no artifact. An evaluator operational failure leaves the
existing final artifact pair byte-unchanged.

## 10. Resource Contract

The complete generator invocation is limited to:

```text
processes = 1
threads <= 4
aggregate_cpu_time <= 4 CPU-hours
wall_time <= 60 minutes
peak_resident_memory <= 1 GiB
development_seeds = 24
```

Wall time starts before the first seed and ends only after final directory `fsync`.
Aggregate CPU time is user plus system CPU time across the process and every thread. Peak
resident memory is the process maximum resident set size. No child process is allowed.
The implementation must enforce or monitor all five resource dimensions and fail closed
when any cannot be measured reliably.

On a budget breach, stop generation, remove every temporary or final path created by the
invocation, print only `PR010_FAILED_BUDGET`, and retain no partial artifact. Budget values
may not be increased after any seed is generated.

## 11. Completeness and No Early Stopping

The generator must attempt all 24 frozen development seeds in order. It must not evaluate
the `22/24` rule, stop early for apparent pass/fail, skip later seeds, or publish a prefix.
Coverage viability is computed only by the separate evaluator after a complete, validated,
atomically published 144-row artifact exists.

Partial in-memory rows, progress counts, temporary bytes, resource-failure prefixes, and
rows from an interrupted invocation may not be used to infer coverage, revise the depth
window, alter `LIMIT_SCORABLE_DEPTHS`, select a seed replacement, or guide a future design.

## 12. Required Tests Before Implementation Clearance

Tests must be synthetic or mocked and must not generate any PR009, PR010 development, or
reserved confirmatory seed. The minimum required test set covers:

1. exact CLI refusal for every argument and override attempt;
2. exact frozen seed/kind/depth traversal and prohibition of seeds outside development;
3. exact 144-row header, key set, row order, domains, and final newline;
4. missing, duplicate, extra, and out-of-order row refusal;
5. support predicate boundaries at four versus five evaluable starts;
6. one synthetic cell at `21/24` supported seeds produces
   `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`;
7. the same cell at `22/24`, with every other cell passing, produces
   `PASS_DEVELOPMENT_COVERAGE`;
8. each of the six cells can independently force infeasibility;
9. forbidden columns and forbidden value leakage through CSV, sidecar, stdout, stderr,
   exceptions, logs, and temporary paths are refused;
10. exact SHA-256 sidecar bytes, malformed sidecars, hash mismatch, and swapped/stale pair
    refusal;
11. evaluator cannot call generator, causal-relation, beam, or geometry code;
12. injected failures at temporary creation, write, flush, `fsync`, reread, validation,
    each rename, and directory `fsync` exercise rollback and incomplete-set refusal;
13. wall-time, aggregate-CPU, peak-memory, process-count, and thread-count exhaustion each
    produce `PR010_FAILED_BUDGET` and leave no artifact;
14. runtime, data-contract, and budget precedence edges;
15. no early stopping for apparent pass, apparent infeasibility, or partial 21/22 support;
16. evaluator leaves a valid final artifact pair byte-identical for both valid terminals
    and every evaluator refusal.

## 13. Separate Gates

Gate 1 is textual and precedes implementation:

```text
PASS_READY_FOR_IMPLEMENTATION
```

It may be issued only after a read-only audit confirms that this protocol matches the
frozen decision, closes every artifact/terminal/resource ambiguity, preserves PR009
non-reuse, and authorizes no data generation.

Only after Gate 1 may the runner, evaluator, and synthetic tests be written. Their source
and tests then require a separate implementation audit. Gate 2 is:

```text
PASS_READY_TO_RUN
```

Gate 2 requires exact source-to-protocol conformance, all required tests passing, clean
artifact paths, a frozen implementation commit, and a separate explicit authorization.
Neither this protocol nor Gate 1 authorizes execution.
