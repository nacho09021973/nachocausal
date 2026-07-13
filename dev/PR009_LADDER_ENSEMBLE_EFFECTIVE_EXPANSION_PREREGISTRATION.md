# PR009 Ladder-Ensemble Effective-Expansion Kill-Test Preregistration

## 1. Status

STATUS: FROZEN_BEFORE_IMPLEMENTATION
SCOPE: CHEAP_KILL_TEST / ORDER_ONLY_ESTIMATOR / BLINDED_GEOMETRIC_SCORING
RELATION_TO_PR008: NEW_INFORMATION_CHANNEL_AFTER_BASELINE_DOMINATED

No PR009 seed listed below has been sprinkled, inspected, or scored before this
preregistration. This document authorizes implementation and synthetic tests, followed by
one reference run and one evaluation run under the frozen contract. It does not authorize
a hyperparameter sweep or a production reconstruction claim.

## 2. Scientific question

Does the transverse width of an order-only ensemble of fuzzy-ladder continuations carry a
signed expansion signal that:

1. is absent in a matched Minkowski control;
2. distinguishes coarse Schwarzschild interior and exterior scoring zones;
3. is not reproduced by survivor-count growth or a depth-only control?

PR009 does not test whether a single optimized ladder localizes the horizon. It tests a
new channel discarded by `H_hat`: transverse relations among multiple simultaneous
continuations.

## 3. Continuum motivation and claim boundary

A marginally outer trapped surface has vanishing outgoing null expansion. The
Raychaudhuri equation relates the evolution of a null congruence's expansion to focusing,
shear, and curvature. Ladder molecules provide an order-theoretic discrete null-tracer
candidate, and arXiv:2605.06813 reports a sign change of a discrete ladder expansion in a
1+1D toy black-hole spacetime.

This motivation does not prove that the PR009 statistic is an expansion estimator. A pass
licenses only:

```text
The frozen order-only ladder-ensemble width statistic survived its preregistered 1+1D
cheap kill test against matched Minkowski, depth, and survivor-growth controls.
```

It does not license apparent-horizon reconstruction, convergence, 3+1D transfer, an
area-law claim, or identification of a marginally outer trapped surface.

## 4. Why existing endpoint entropy is rejected

`dev/measure_kbeam_peeloff.py` deduplicates the beam by terminal rung
`(p_last, q_last)`. Therefore every retained terminal rung has multiplicity one and:

```text
n_endpoint_identities = n_survivors
endpoint_entropy_nats = log(n_survivors)
effective_endpoint_count = n_survivors
```

Those columns add no information beyond beam population. They are prohibited as the
PR009 primary observable.

## 5. Frozen order-only estimator

### 5.1 Input

The estimator accepts only an abstract finite causal set:

- element identifiers;
- the causal relation matrix or equivalent adjacency representation;
- derived link relations;
- frozen run metadata: `seed`, `spacetime_kind`, `intensity`, `K`, `start_id`, and
  `depth_k`.

Element identifiers may break output-order ties but may not define distances, directions,
zones, or inclusion. The numeric value of an identifier must not enter a statistic.

### 5.2 Ladder ensemble

Use the existing Definition-2 K-beam continuation predicate and order-only regularity
score from `dev/measure_kbeam_peeloff.py`, with:

```text
M = 3
K = 64
MAX_DEPTH = 12
MAX_STARTS = 40
```

`K=64` is chosen before PR009 execution to expose an ensemble rather than the narrow
`K=8` channel audited in PR008. It is not varied in PR009. The K-beam retains at most one
state per terminal rung.

Start rungs use the existing `boundary_minimals_invariant` predicate and deterministic
sampling rule. No embedding value may select or rank a start.

### 5.3 Minimum enclosing-diamond separation

For two distinct spacelike elements `u` and `v`, define:

```text
D(u,v) = sqrt(min |[e,f]|)
```

where the minimum is over every common-past element `e` and common-future element `f`
such that `e <= u,v <= f`, and `|[e,f]|` includes both endpoints. `D(u,v)` is undefined if
`u` and `v` are comparable or no enclosing pair exists.

The definition minimizes cardinality directly and does not select a highest/lowest
representative using embedding coordinates or element IDs.

For two distinct survivor rungs `i=(p_i,q_i)` and `j=(p_j,q_j)` at depth `k`, define:

```text
d_ij(k) = sqrt(D(p_i,p_j) * D(q_i,q_j))
```

when both factors are finite and positive.

### 5.4 Ensemble width and effective expansion

For a `(seed, spacetime_kind, intensity, start_id, depth_k)` slice, let `P_k` be the
multiset of all finite `d_ij(k)` over unordered survivor pairs. The slice is width-evaluable
only if:

```text
n_survivors >= 3
|P_k| >= 3
```

Define the width as the lower median:

```text
W_k = lower_median(P_k)
```

A transition `k -> k+1` is expansion-evaluable only when both widths are evaluable and
positive. Define:

```text
theta_raw(k) = log(W_{k+1}) - log(W_k)
```

This scalar and all inputs to it are order-only.

## 6. Frozen controls and residualization

### 6.1 Matched Minkowski control

For each seed and intensity, use the same sprinkled point set to construct two causal
relations independently:

- `BH`: Schwarzschild causal relation;
- `MINK`: Minkowski causal relation.

Coordinates are used by the generator to construct each relation and by the scorer after
estimation. They are never passed into the estimator.

### 6.2 Depth-only reference

Using only the six reference seeds and `MINK` rows, compute for each depth `k`:

```text
b_depth(k) = lower_median(theta_raw for all evaluable reference-MINK transitions at k)
theta_residual = theta_raw - b_depth(k)
```

If a depth has fewer than 12 evaluable reference-MINK transitions, the data contract
fails. No BH row or evaluation seed may enter `b_depth`.

### 6.3 Survivor-growth baseline

For every expansion-evaluable transition define:

```text
b_survivor(k) = log(n_survivors(k+1)) - log(n_survivors(k))
```

This baseline tests whether the transverse-width signal merely reproduces beam population
growth or collapse.

`first_empty_depth`, `H_hat`, endpoint entropy, endpoint effective count, radial distance,
and regularity score are descriptive-only or prohibited; none may alter terminal logic.

## 7. Frozen seed and run blocks

Create a dedicated PR009 development band, disjoint from all prior pools and the reserved
2,000,000--2,999,999 band:

```text
PR009_REFERENCE_SEEDS = 1100000,1100001,1100002,1100003,1100004,1100005
PR009_EVALUATION_SEEDS = 1100006,1100007,1100008,1100009,1100010,1100011
```

Frozen run configuration:

```text
intensity = 4800
t_edge = 6
M = 3
K = 64
MAX_DEPTH = 12
MAX_STARTS = 40
spacetime_kind = BH,MINK
device = cpu
```

CPU is frozen to avoid backend-dependent causal-relation or reduction drift. The run order
is reference first, evaluation second. Evaluation output must not be inspected until the
reference artifact is finalized and hashed.

## 8. Output separation

### 8.1 Order-only estimator artifact

Path:

`data/reports/pr009_ladder_ensemble_effective_expansion_order_only.csv`

Allowed columns:

- `run_block` (`REFERENCE` or `EVALUATION`);
- `seed`;
- `spacetime_kind`;
- `intensity`;
- `K`;
- `start_id`;
- `depth_k`;
- `slice_status`;
- `n_survivors`;
- `n_valid_pair_separations`;
- `width_lower_median`;
- `theta_raw`;
- `depth_mink_reference`;
- `theta_residual`;
- `survivor_growth_baseline`.

No coordinate, radius, horizon label, shell label, straddling flag, or path geometry may
appear in this artifact.

### 8.2 Blinded scoring artifact

Path:

`data/reports/pr009_ladder_ensemble_effective_expansion_scored.csv`

The scorer joins estimator rows to a separately held truth table after the estimator file
is complete and validated. It may add:

- `truth_r_mid`;
- `truth_zone`;
- `distance_to_horizon_over_ell`.

These fields are evaluation-only and cannot flow back into estimator construction,
reference baselines, exclusions, or missingness rules.

### 8.3 Report

Path:

`data/reports/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_REPORT.md`

The report must include configuration and input hashes, coverage counts, all terminal
metrics, the exact terminal label, and interpretation limits.

## 9. Frozen scoring zones

Let `r_mid` be the hidden lower median over survivor-rung embedded midpoints at the
current depth, and let `ell = thresholds.ell(4800)`.

```text
INTERIOR: r_mid <= R_S - 2*ell
EXTERIOR: r_mid >= R_S + 2*ell
GUARD: otherwise
```

`GUARD` rows are excluded from sign scoring by this preregistered rule, not by observed
values. They remain in both CSV artifacts.

Minkowski rows receive the same coordinate-based zones solely as a negative control; the
Minkowski estimator never consumes them.

## 10. Frozen primary statistics

Use evaluation seeds only. For each spacetime kind and score `s`, define:

```text
C_kind(s) = lower_median(s | EXTERIOR) - lower_median(s | INTERIOR)
```

Primary candidate score: `s = theta_residual`.

Baseline score: `s = survivor_growth_baseline`.

Compute a deterministic seed-stratified one-sided permutation p-value for positive
contrast. Within each seed and spacetime kind, permute `INTERIOR`/`EXTERIOR` labels while
preserving zone counts. Enumerate all assignments if their product is at most 100,000;
otherwise use exactly 100,000 permutations from NumPy `PCG64` seed `9009`. Use the
plus-one correction `(1 + exceedances)/(1 + permutations)`.

Also compute seed concordance:

```text
n_positive_seed_contrasts = number of evaluation seeds with C_seed(theta_residual) > 0
```

## 11. Data sufficiency

The result is `INCONCLUSIVE_COVERAGE` unless all conditions hold:

- all 12 seeds and both spacetime kinds complete;
- every reference depth used by evaluation has a valid `b_depth(k)`;
- at least 30 evaluation transitions occur in each `(BH, INTERIOR)`, `(BH, EXTERIOR)`,
  `(MINK, INTERIOR)`, and `(MINK, EXTERIOR)` cell;
- at least 4 of 6 evaluation seeds contribute to both zones for each spacetime kind;
- no duplicate primary key exists;
- all order-only rows pass schema and finite-value checks.

Coverage rules may not be weakened after execution.

## 12. Terminal decision tree

Terminal precedence is:

```text
FAILED_RUNTIME
> FAILED_DATA_CONTRACT
> FAILED_LEAKAGE_AUDIT
> INCONCLUSIVE_COVERAGE
> KILLED_GENERIC_OR_BASELINE_SIGNAL
> KILLED_NO_SIGNED_EXPANSION
> SURVIVED_CHEAP_KILL_TEST
```

### `KILLED_GENERIC_OR_BASELINE_SIGNAL`

Assign if any condition holds:

- `C_MINK(theta_residual) > 0` with `p_MINK <= 0.10`;
- `C_BH(theta_residual) <= C_BH(survivor_growth_baseline)`;
- `theta_residual` is exactly equal to survivor-growth baseline on every evaluable BH
  transition.

### `KILLED_NO_SIGNED_EXPANSION`

Assign if the generic/baseline kill does not apply and any condition holds:

- `C_BH(theta_residual) <= 0`;
- `p_BH > 0.01`;
- fewer than 5 of 6 evaluation seeds have positive within-seed BH contrast;
- the aggregate BH interior lower median is not negative;
- the aggregate BH exterior lower median is not positive.

### `SURVIVED_CHEAP_KILL_TEST`

Assign only if coverage passes, neither kill applies, and all signed-expansion conditions
above pass.

Survival authorizes a separate design review. It does not authorize threshold tuning, a
larger run, or a 3+1D claim automatically.

## 13. Failure and leakage conditions

`FAILED_LEAKAGE_AUDIT` applies if estimator or baseline logic reads coordinates, radius,
horizon side, straddling, shell, scorer zones, or any pre-PR009 geometric diagnostic.

`FAILED_DATA_CONTRACT` applies to schema drift, seed/config mismatch, missing reference
hash, malformed values, duplicate keys, unauthorized K/depth/start settings, or reference
baselines derived from BH or evaluation rows.

`FAILED_RUNTIME` applies to an uncaught exception or incomplete publication not classified
above.

## 14. Forbidden adaptations

After this commit, PR009 forbids:

- changing the seed blocks or adding seeds;
- varying `K`, `M`, `MAX_DEPTH`, `MAX_STARTS`, intensity, or box size;
- replacing lower medians with means or upper medians;
- adding endpoint entropy as evidence of novelty;
- changing the width formula, zones, p-values, or thresholds;
- selecting only favorable starts, depths, seeds, or orientations;
- using GPU results in terminal logic;
- rerunning the evaluation block after viewing its result;
- converting a killed or inconclusive label into survival through a new analysis.

## 15. Required implementation tests before any PR009 seed run

- exact minimum enclosing-diamond separation on hand-built posets;
- invariance under random element relabeling;
- lower-median and width vectors;
- undefined separation and coverage paths;
- `theta_raw`, depth residual, and survivor baseline vectors;
- strict reference/evaluation isolation;
- scorer unable to affect estimator artifact bytes;
- permutation p-value determinism;
- every terminal branch and precedence edge;
- output schema, hashes, and atomic publication.

No PR009 seed may be generated until these tests pass and the implementation is reviewed
against this preregistration.

## 16. Amendment A — frozen execution and artifact boundary

STATUS: FROZEN_BEFORE_IMPLEMENTATION / AMENDED_BEFORE_ANY_PR009_RUN

This amendment resolves execution details that §§7–8 require but did not name. It was
written before any PR009 seed was generated or inspected. It changes no scientific
question, estimator, seed, configuration, scoring zone, statistic, threshold, coverage
rule, terminal label, or precedence edge.

### 16.1 Fixed commands and execution order

The only production commands are, in this order:

```text
python3 dev/run_pr009_effective_expansion.py --block REFERENCE
python3 dev/run_pr009_effective_expansion.py --block EVALUATION
python3 dev/score_pr009_effective_expansion.py
```

The runner accepts no path, seed, device, K, depth, start-count, intensity, box-size, or
format override. `--block` accepts only the two literal values above. The scorer accepts no
production override. Both programs may expose a synthetic self-test entry point that
cannot call the generator or write a production path.

The evaluation command must refuse to start unless the finalized reference artifact and
its sidecar exist, validate, and reproduce the recorded SHA-256. The scorer must refuse to
start unless the canonical order-only artifact and evaluation truth artifact both exist
and validate. A valid existing production output is never overwritten.

### 16.2 Fixed intermediate and final paths

```text
REFERENCE_ORDER_ONLY = data/reports/pr009_ladder_ensemble_effective_expansion_reference_order_only.csv
REFERENCE_SHA256 = data/reports/pr009_ladder_ensemble_effective_expansion_reference_order_only.sha256
EVALUATION_ORDER_ONLY = data/reports/pr009_ladder_ensemble_effective_expansion_evaluation_order_only.csv
EVALUATION_TRUTH = data/reports/pr009_ladder_ensemble_effective_expansion_evaluation_truth.csv
CANONICAL_ORDER_ONLY = data/reports/pr009_ladder_ensemble_effective_expansion_order_only.csv
SCORED = data/reports/pr009_ladder_ensemble_effective_expansion_scored.csv
REPORT = data/reports/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_REPORT.md
```

The reference command publishes only `REFERENCE_ORDER_ONLY` and then `REFERENCE_SHA256`.
The sidecar is exactly one lowercase hexadecimal SHA-256 followed by `  `, the reference
artifact's basename, and `\n`.

The evaluation command publishes `EVALUATION_ORDER_ONLY` and `EVALUATION_TRUTH`, then
constructs `CANONICAL_ORDER_ONLY` as one header followed by the already-finalized
reference rows and then evaluation rows. It must compare the reference bytes with the
sidecar before and after publication. It may concatenate validated bytes; it may not
parse, summarize, display, or score evaluation values.

### 16.3 Primary key, rows, statuses, and canonical serialization

The primary key in every CSV is:

```text
(run_block, seed, spacetime_kind, intensity, K, start_id, depth_k)
```

There is exactly one order-only row for every emitted start and every `depth_k` in
`1..MAX_DEPTH`, including depths after beam exhaustion. `start_id` is the zero-based rank
in the frozen deterministic start sample. Rows are ordered by `run_block` (`REFERENCE`
then `EVALUATION`), seed ascending, `spacetime_kind` (`BH` then `MINK`), intensity, K,
start_id, and depth_k.

The exact order-only header is the §8.1 column list in the order printed there.
`slice_status` is exactly one of:

- `TRANSITION_EVALUABLE`: current and following widths are positive and evaluable;
- `WIDTH_ONLY`: current width is evaluable but no evaluable following width exists;
- `WIDTH_UNEVALUABLE`: current width is not evaluable;
- `EMPTY`: no survivor exists at the current depth.

For `TRANSITION_EVALUABLE`, all five numeric statistic columns from
`width_lower_median` through `survivor_growth_baseline` are finite. For `WIDTH_ONLY`, only
`width_lower_median` is finite. For `WIDTH_UNEVALUABLE` and `EMPTY`, those five columns
are missing. Integer count columns are always present and nonnegative.

All CSVs use UTF-8, comma delimiter, RFC-4180 quoting only when required, `\n` line
endings, and a final newline. Integers use unsigned base-10 notation; finite floats use
Python `format(value, '.17g')`; every missing scalar is the literal `NA`. No `NaN`,
infinity, empty field, locale-dependent decimal, or negative zero is allowed.

### 16.4 Reference residualization boundary

The reference command first holds width and `theta_raw` values in memory, derives
`b_depth(k)` exclusively from reference-Minkowski evaluable transitions, checks the frozen
minimum of 12, and only then renders the finalized reference rows. Reference-BH rows may
receive that already-derived depth reference; they may not contribute to it.

The evaluation command reads from `REFERENCE_ORDER_ONLY` only the validated mapping
`depth_k -> depth_mink_reference`. It may not read reference truth or any reference-BH
statistic to construct an evaluation value.

### 16.5 Separately held evaluation truth

`EVALUATION_TRUTH` has the exact header:

```text
run_block,seed,spacetime_kind,intensity,K,start_id,depth_k,truth_r_mid,truth_zone,distance_to_horizon_over_ell
```

It contains evaluation keys only and uses the same row order and serialization. For a
nonempty current-depth slice, `truth_r_mid` is the lower median of
`0.5*(r_p_last+r_q_last)` over all current survivor rungs, and
`distance_to_horizon_over_ell = abs(truth_r_mid-R_S)/ell`. `truth_zone` follows §9. For
an empty slice all three truth fields are `NA`; otherwise they are present, including
`GUARD`.

Truth rows are computed and written by a geometry-aware collector that receives the
embedding and survivor terminal identifiers. The order-only row builder receives only the
causal matrix, survivor terminal identifiers, and frozen metadata. The two byte streams
are rendered independently. No truth field or truth-derived missingness may enter an
order-only row.

### 16.6 Scored artifact and transition convention

`SCORED` contains evaluation rows only. Its exact header is the 15 order-only columns
followed by the three truth fields in §8.2. The scorer performs a one-to-one join on the
primary key and refuses duplicates, missing keys, or extra keys.

A statistic recorded at `depth_k = k` always describes the transition `k -> k+1` and is
scored with the truth zone of the current slice at depth `k`. Only
`TRANSITION_EVALUABLE` rows with `truth_zone` equal to `INTERIOR` or `EXTERIOR` enter the
terminal statistics. `GUARD`, missing truth, and non-transition rows remain in `SCORED`
but never enter a contrast, permutation, concordance, or coverage count.

The scorer is the sole program allowed to compute contrasts, permutation p-values,
coverage cells, terminal labels, or the report. It never writes or modifies an order-only,
reference, sidecar, evaluation, or truth artifact.

### 16.7 Amendment B — exchangeable order-only tie resolution

STATUS: FROZEN_BEFORE_IMPLEMENTATION / AMENDED_AFTER_SYNTHETIC_RELABEL_FALSIFIER

The pre-existing K-beam used Python insertion order when equal regularity scores crossed
the K cutoff, and its deterministic start sampler selected positions from a label-sorted
list. A hand-built symmetric poset demonstrated that relabeling could change retained
terminal rungs. This violates §5.1 because identifiers then determine inclusion. The core
width tests did not exercise this upstream selection path.

PR009 therefore uses an auxiliary exchangeable random rank, not an element identifier, to
resolve inclusion ties. This adds no coordinate, radius, direction, zone, distance, or
other geometric information. The estimator is a reproducible randomized order-only
estimator conditional on the frozen ranks.

```text
TIE_RANK_MASTER_SEED = 9009009
tie_rank = Generator(PCG64(SeedSequence([TIE_RANK_MASTER_SEED, seed]))).permutation(N)
```

`tie_rank[e]` is a unique integer in `0..N-1` attached to element `e`. The same vector is
used for the matched BH and MINK relations on a seed's shared point set. Under a relabeling
test, the rank vector must be permuted with the elements; regenerating ranks from the new
numeric labels is prohibited. Neither ranks nor their numeric values enter a width,
expansion, baseline, zone, contrast, permutation statistic, or output row.

Start rungs are still the complete output of `boundary_minimals_invariant` paired with
their future-link children. If more than `MAX_STARTS` exist, retain the `MAX_STARTS` rungs
with lexicographically smallest `(tie_rank[p], tie_rank[q])`. Their `start_id` order is
that same rank order. No RNG choice over a label-sorted list is allowed.

The Definition-2 predicate, cumulative regularity reward, terminal-rung deduplication,
K=64 cutoff, M, and depth limit remain unchanged. For every candidate path define:

```text
path_tie_key = ((tie_rank[p_0],tie_rank[q_0]),...,(tie_rank[p_k],tie_rank[q_k]))
```

For duplicate terminal rungs, retain the candidate with the higher cumulative regularity
score and then the lexicographically smaller `path_tie_key`. Rank the deduplicated beam by
higher cumulative regularity score and then smaller `path_tie_key`; retain the first K.
This key also fixes parent-continuation and lineage output order. Numeric element IDs may
only appear when materializing the already-selected path in the internal computation.

Required pre-run tests now include whole-beam and start-sample equivariance under many
random relabelings, with the rank vector carried through each relabeling. Tests must compare
mapped-back start sets, survivor paths at every depth, widths, transition values, and
rendered order-only rows. A test that relabels only a preselected survivor list is
insufficient.

### 16.8 Amendment C — scoring population and pre-scoring failures

STATUS: FROZEN_BEFORE_SCORER_IMPLEMENTATION

The aggregate contrast `C_kind(s)` uses every evaluation `TRANSITION_EVALUABLE` row in
the two scored zones for that spacetime kind. The seed-stratified permutation p-value uses
only seeds that contribute at least one transition to both `INTERIOR` and `EXTERIOR` for
that kind; all rows from those complete-zone seeds enter the permutation. A seed with only
one zone is not silently relabeled or borrowed by another stratum. It fails to count as a
positive seed contrast and therefore cannot help the `5 of 6` requirement.

`n_positive_seed_contrasts` is computed over the frozen six evaluation seed identifiers.
For a seed lacking either zone its positivity indicator is zero. The reported per-seed
contrast is `NA`, not zero, so absence is distinguishable from a measured nonpositive
contrast.

`INCONCLUSIVE_COVERAGE` is a scientific terminal result and publishes `SCORED` and
`REPORT`. The three higher-precedence labels are pre-scoring refusals:

- `FAILED_RUNTIME`: an input or production path cannot be read, an uncaught computation
  fails, or publication cannot complete;
- `FAILED_DATA_CONTRACT`: bytes are readable but violate a frozen schema, key,
  configuration, hash, serialization, or reference-isolation rule;
- `FAILED_LEAKAGE_AUDIT`: an order-only artifact exposes a forbidden geometric field or a
  truth key cannot be isolated one-to-one from the order-only key set.

A pre-scoring refusal prints exactly one `PR009_TERMINAL_LABEL=<label>` line to stderr,
returns nonzero, and publishes neither `SCORED` nor `REPORT`. After correcting
implementation or storage, the scorer may be rerun against the unchanged finalized runner
artifacts; the reference or evaluation generator may not be rerun. This distinction keeps
an operational failure from masquerading as a scientific kill or consuming a second seed
execution.

For every published scientific result, `REPORT` records SHA-256 values for
`REFERENCE_ORDER_ONLY`, `EVALUATION_ORDER_ONLY`, `EVALUATION_TRUTH`, and
`CANONICAL_ORDER_ONLY`, plus a configuration fingerprint over the exact frozen constants,
field lists, seeds, and terminal thresholds. The report machine block uses a fixed key
order and `NA` for unavailable metrics. `SCORED` and `REPORT` are published as one rollback
protected pair and valid existing finals are never overwritten.
