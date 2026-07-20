# SQUARE_BOX_2P4 Boundary-Localization

STATUS: CONTRACT_FROZEN
FROZEN_BY: human review
FROZEN_DATE: 2026-07-19
DATE: 2026-07-19

## 0. Scope

This document opens a new boundary-localization question motivated by the sealed
`SQUARE_BOX_2P4` dispersion result.

It is not an execution authorization. It freezes nothing until explicit human review accepts the
final text.

This is not a repair, continuation, re-evaluation, or reinterpretation of R-VAR.

The previous R-VAR closure remains intact:

```text
CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]
```

The sealed dispersion result remains separately bounded:

```text
BH_MINK_DISPERSION_DIFFERENCE_DETECTED
```

That result showed a BH-vs-MINK difference in future-observable dispersion. It did not localize a
boundary. This draft asks the next question.

## 1. Scientific question

In the frozen square patch `SQUARE_BOX_2P4`, can the order-only future observables on minimal
elements produce a localized candidate boundary band near the hidden Schwarzschild radius `r=R_S`,
rather than only detecting a global BH-vs-MINK dispersion difference?

Target:

```text
BOUNDARY_LOCALIZATION_FROM_FUTURE_OBSERVABLES
```

Claim boundary:

- local boundary-candidate output only;
- no global event-horizon claim;
- no metric reconstruction;
- no 3+1D transfer;
- no repair or supersession of R-VAR.

## 2. Geometry

Geometry is inherited from the separate square-box result, not chosen anew after localization
inspection:

```text
PATCH_GEOMETRY = SQUARE_BOX_2P4
T_EDGE = 2.4
R_EDGE = 2.4
R_CENTER = 1.3
r ∈ [0.1, 2.5]
R_S = 0.5
BOX_AREA = 5.76
ASPECT_RATIO = 1.0
```

The old R-VAR tall-box geometry remains:

```text
T_EDGE_OLD = 6.0
R_EDGE_OLD = 1.2
ASPECT_RATIO_OLD = 5.0
R_VAR_STATUS = CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]
```

## 3. Seed discipline

The dispersion-evaluation seeds are burned for confirmatory localization:

```text
DISPERSION_EVAL_SEEDS = 4_200_000 .. 4_200_023
```

They may be cited as motivation only. They must not be used for confirmatory localization.

Excluded prior ranges / sets:

```text
DEV_SEEDS = (20240617, 13, 101, 7, 42, 99, 2718, 31415)
EXPLORE_POOL = 1_000_000 .. 1_000_039
PR010 development seeds = 1_101_000 .. 1_101_023
prereg-002 validation band = 2_000_000 .. 2_999_999
OP-2.1 synthetic band = 3_000_000 .. 3_999_999
new-geometry dispersion dev seeds = 4_100_000 .. 4_100_011
new-geometry dispersion eval seeds = 4_200_000 .. 4_200_023
```

Proposed development seeds for localization design sanity only:

```text
BOUNDARY_LOC_DEV_SEEDS = 4_300_000 .. 4_300_015
```

Proposed confirmatory evaluation seeds:

```text
BOUNDARY_LOC_EVAL_SEEDS = 4_400_000 .. 4_400_031
```

No seed substitution after inspection.

## 4. Observation channel

For each seed and intensity:

1. Draw one coordinate-uniform Poisson point cloud in `SQUARE_BOX_2P4`.
2. Build two causal matrices on the same point cloud:
   - `BH`: 1+1D Schwarzschild EF causal relation with `R_S=0.5`;
   - `MINK`: 1+1D flat Minkowski causal relation.
3. The localization rule receives only the finite partial order.
4. Coordinates and `R_S` are used only after selection, for scoring.

Same-cloud pairing is mandatory.

## 5. Intensities

Proposed evaluation intensities:

```text
BOUNDARY_LOC_INTENSITIES = (1200.0, 2400.0, 4800.0, 9600.0)
BOUNDARY_LOC_PRIMARY_INTENSITY = 9600.0
```

The discreteness scale is:

```text
ell = (intensity / 5.76)^(-1/2)
```

## 6. Order-only observables

For a finite poset `C`, let:

```text
Min(C) = {i : no j precedes i}
```

For every `i ∈ Min(C)`:

```text
L(i) = longest future-chain length from i
V(i) = |J⁺(i)|
```

Both are order-only.

## 7. Proposed localizer

The proposed output is a subset of minimal elements:

```text
H_hat(C) ⊆ Min(C)
```

The rule is deterministic and order-only.

For every `i ∈ Min(C)`:

1. Compute midrank percentiles within `Min(C)`:

```text
rank_L(i) = midrank percentile of L(i)
rank_V(i) = midrank percentile of V(i)
```

Ties receive the same midrank. No random tie-break is used.

2. Compute the scalar future score:

```text
A(i) = 0.5 * rank_L(i) + 0.5 * rank_V(i)
```

3. Sort the distinct values of `A`.

4. Let `g*` be the largest adjacent gap between distinct `A` values.

5. Output the two endpoint level sets around that largest gap:

```text
H_hat(C) = {i ∈ Min(C) : A(i) = A_left(g*) OR A(i) = A_right(g*)}
```

If multiple adjacent gaps tie for largest size, choose the tied gap whose midpoint is closest to
`0.5`. If still tied, output the union of all endpoint level sets for the remaining tied gaps and
mark:

```text
TIE_EXPANDED_BAND
```

This tie rule is order-only because it depends only on score values.

## 8. Abstention rules

A seed abstains before scoring if:

```text
|Min(C)| < 8
fewer than 3 distinct A values
non-finite summary
|H_hat(C)| = 0
|H_hat(C)| > 0.5 * |Min(C)|
```

Terminals distinguish support failure from scientific failure.

## 9. Scoring

Scoring uses hidden coordinates only after `H_hat(C)` has been selected.

For each selected element:

```text
d_perp(i) = |r_i - R_S|
d_ell(i) = d_perp(i) / ell
```

Per seed:

```text
loc_med(seed) = median_{i ∈ H_hat(C)} d_ell(i)
loc_q75(seed) = q75_{i ∈ H_hat(C)} d_ell(i)
band_size(seed) = |H_hat(C)|
```

## 10. Primary success criterion

The primary scientific endpoint is BH localization at `9600.0`.

Success requires all of:

```text
valid_BH_seeds >= 26 / 32
median_BH(loc_med) <= 3.0
median_BH(loc_q75) <= 5.0
```

and the MINK same-cloud control must not spuriously localize to the same hidden radius:

```text
false_positive_MINK_fraction <= 0.25
```

where a MINK seed is a false positive if:

```text
loc_med_MINK(seed) <= 3.0
```

The MINK threshold is a control against a box-boundary artifact selecting the arbitrary coordinate
`r=R_S` even when no BH causal relation is present.

## 11. Secondary robustness checks

Report without retuning:

```text
median_BH(loc_med) by intensity
median_BH(loc_q75) by intensity
median band_size by kind and intensity
MINK false-positive fraction by intensity
abstention fraction by kind and intensity
```

No threshold may be changed after evaluation.

## 12. Terminal precedence

Exactly one terminal is emitted with this precedence:

### Integrity / provenance

```text
INTEGRITY_FAILURE
SEED_OVERLAP_FAILURE
PATCH_CONTRACT_MISMATCH
IMPLEMENTATION_CONTRACT_FAILURE
```

### Contract / design

```text
FAILED_SUPPORT_CONTRACT
LOCALIZER_OVERBROAD_BAND
MINK_SPURIOUS_LOCALIZATION_CONTROL_FAIL
INSUFFICIENT_VALID_BH_SEEDS
```

### Scientific

```text
BOUNDARY_LOCALIZATION_DETECTED
NO_BOUNDARY_LOCALIZATION_DETECTED
INCONCLUSIVE_BOUNDARY_LOCALIZATION
```

Contract/design terminals must not be reported as scientific negatives.

## 13. Evidence directory

If this protocol is later frozen and executed, outputs must go under:

```text
evidence/square_box_boundary_localization_20260719/
```

Required files:

```text
manifest.json
claim_ledger.md
per_seed_localization.csv
evaluation_summary.json
evaluation_report.md
terminal.txt
RESULT_SEALED.txt
```

## 14. Current status

This document is only a draft for human review.

```text
NO_CONTRACT_FREEZE
NO_DATA_GENERATED
NO_EVALUATION_RUN
NO_LOCALIZATION_RESULT
```

## CONTRACT FROZEN

Frozen by human review on 2026-07-19.
Geometry: SQUARE_BOX_2P4
Question: BOUNDARY_LOCALIZATION_FROM_FUTURE_OBSERVABLES
Previous dispersion result and R-VAR closure remain intact.
No data generated at freeze time.
