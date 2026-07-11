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
