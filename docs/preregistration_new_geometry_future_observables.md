# New Geometry Future Observables — Frozen Contract

STATUS: FROZEN_CONTRACT / NO_DATA_GENERATED_AT_FREEZE / NEW_SCIENTIFIC_QUESTION
DATE: 2026-07-19

## 0. Scope

This is a new scientific question about the behavior of future observables on minimal elements
under a different finite patch geometry.

This is not a repair, continuation, reinterpretation, or re-evaluation of R-VAR.

The previous R-VAR closure remains intact:

```text
CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]
```

No result from this protocol may be cited as correcting, rescuing, superseding, or explaining
away that closure.

## 1. New scientific question

Given a finite 1+1D causal-set sprinkling into a patch whose aspect ratio is not the previous tall
box, do the order-only future observables

- `L(i)`: longest future-chain length from each minimal element `i`;
- `V(i)`: future cardinality `|J⁺(i)|` from each minimal element `i`;

retain a non-degenerate Minkowski control distribution while showing a distinguishable BH-vs-MINK
difference under the same point cloud?

The primary target is not horizon reconstruction. The target is narrower:

> Does changing the patch geometry remove the near-delta Minkowski-null degeneracy that closed
> R-VAR on the tall-box geometry?

## 2. Previous result boundary

The prior R-VAR result is fixed as:

```text
R_VAR_STATUS = CLOSED_NEGATIVE_RESULT [
  NO_NONDEGENERATE_MINK_NULL_FOUND_ON_FROZEN_GEOMETRY;
  GEOMETRY_SPECIFIC;
  T_EDGE=6.0;
  R_EDGE=1.2
]
```

This protocol does not reuse:

- R-VAR seeds;
- R-VAR thresholds;
- R-VAR evaluation artifacts;
- PR009 internal outputs;
- PR010 coverage artifacts;
- prereg-002 validation seeds or artifacts.

Any agreement or disagreement with R-VAR is non-corroborative.

## 3. New patch geometry

Geometry label:

```text
PATCH_GEOMETRY = SQUARE_BOX_2P4
```

Coordinates:

```text
t ∈ [0.0, 2.4]
r ∈ [0.1, 2.5]
```

Parameters:

```text
T_EDGE_NEW = 2.4
R_EDGE_NEW = 2.4
R_CENTER_NEW = 1.3
R_S = 0.5
BOX_AREA_NEW = 5.76
ASPECT_RATIO_NEW = T_EDGE_NEW / R_EDGE_NEW = 1.0
```

Reason for this geometry:

The closed R-VAR geometry used:

```text
T_EDGE_OLD = 6.0
R_EDGE_OLD = 1.2
ASPECT_RATIO_OLD = 5.0
```

That tall-box aspect ratio allowed light in the flat control to cross the spatial width on a
timescale much shorter than the total temporal extent. The resulting Minkowski control for
per-minimal future observables was near-degenerate.

The new square box has aspect ratio `1.0`, so the flat-control degeneracy mechanism from the old
tall box does not automatically transfer.

This is not a claim that the new patch fixes the issue. It only makes the new question meaningfully
different.

## 4. Observation channel

For each seed and intensity:

1. Draw one coordinate-uniform Poisson point cloud in `SQUARE_BOX_2P4`.
2. Build two causal matrices on the same point cloud:
   - `BH`: 1+1D Schwarzschild EF causal relation with `R_S=0.5`;
   - `MINK`: 1+1D flat Minkowski causal relation.
3. The estimator receives only the finite partial order.
4. Coordinates are used only for generating the two causal relations and for provenance, never as
   observable input.

Same-cloud pairing is mandatory.

## 5. Intensities

Frozen evaluation intensities:

```text
INTENSITIES_NEW = (1200.0, 2400.0, 4800.0, 9600.0)
PRIMARY_INTENSITY_NEW = 9600.0
```

These are Poisson means, not realized `N`.

Approximate densities:

```text
rho = intensity / 5.76
```

Approximate discreteness scales:

```text
ell = rho^(-1/2)
```

The protocol reports realized `N`, number of minimals, and `ell` for every seed and kind.

## 6. Seeds

All seed ranges are new and disjoint from known burned or used ranges:

Known excluded ranges / sets:

```text
DEV_SEEDS = (20240617, 13, 101, 7, 42, 99, 2718, 31415)
EXPLORE_POOL = 1_000_000..1_000_039
PR010 development seeds = 1_101_000..1_101_023
prereg-002 validation band = 2_000_000..2_999_999
OP-2.1 synthetic band = 3_000_000..3_999_999
```

New development smoke seeds:

```text
NEW_GEOM_DEV_SEEDS = 4_100_000..4_100_011
```

New evaluation seeds:

```text
NEW_GEOM_EVAL_SEEDS = 4_200_000..4_200_023
```

The evaluation uses exactly 24 seeds per intensity.

No seed may be substituted after inspection.

## 7. Observables

For a finite poset `C`, let:

```text
Min(C) = {i : no j precedes i}
```

For each `i ∈ Min(C)`:

```text
V(i) = |{j : i precedes j}|
L(i) = length of the longest chain starting at i into its future
```

Both are order-only.

Per seed and spacetime kind, compute the paired multiset:

```text
F(C) = {(L(i), V(i)) : i ∈ Min(C)}
```

Derived per-seed summaries:

```text
cv_L = std(L(i)) / mean(L(i))
cv_V = std(V(i)) / mean(V(i))
iqr_L = IQR(L(i))
iqr_V = IQR(V(i))
range_L = max(L(i)) - min(L(i))
range_V = max(V(i)) - min(V(i))
```

If `|Min(C)| < MIN_MINIMALS`, the seed is `SUPPORT_ABSTAIN`.

Frozen support threshold:

```text
MIN_MINIMALS = 8
```

## 8. Primary non-degeneration gate

The primary gate is on the Minkowski control only.

At the primary intensity `9600.0`, among valid MINK seeds:

```text
median(cv_L_MINK) >= 0.05
OR
median(cv_V_MINK) >= 0.05
```

and

```text
valid_MINK_seeds >= 20 / 24
```

If this fails, terminal is:

```text
MINK_CONTROL_DEGENERATE_ON_NEW_GEOMETRY
```

This is a design/contract terminal, not a scientific negative result about BH physics.

Rationale:

The old R-VAR closure observed MINK CV around `0.006–0.024`. The new geometry must exceed that
near-delta regime by a pre-frozen margin before any BH-vs-MINK contrast is scientifically
interpretable.

## 9. Secondary support gates

For every intensity and kind:

```text
valid_seeds(kind, intensity) >= 20 / 24
```

A seed is valid iff:

```text
|Min(C)| >= 8
mean(L(i)) > 0
mean(V(i)) > 0
all summaries finite
```

If support fails before the primary scientific contrast:

```text
FAILED_SUPPORT_CONTRACT
```

No scientific conclusion is reported.

## 10. Scientific contrast

Only if the Minkowski non-degeneration gate passes, evaluate BH-vs-MINK separation.

Primary contrast at `PRIMARY_INTENSITY_NEW`:

For each valid paired seed:

```text
D_L(seed) = cv_L_BH(seed) - cv_L_MINK(seed)
D_V(seed) = cv_V_BH(seed) - cv_V_MINK(seed)
```

Primary scientific success requires:

```text
median(D_L) > 0
OR
median(D_V) > 0
```

and paired sign-flip permutation p-value:

```text
p_perm <= 0.01
```

for at least one of `D_L`, `D_V`.

This is a weak scientific contrast: it tests whether the new geometry produces a BH-vs-MINK
difference in future-observable dispersion. It does not localize a horizon and does not
reconstruct geometry.

## 11. Boundary and censoring controls

Report, but do not tune on:

```text
n_min = |Min(C)|
N = total number of elements
mean_L, mean_V
cv_L, cv_V
iqr_L, iqr_V
range_L, range_V
```

Mandatory diagnostic flags:

```text
LOW_MINIMAL_SUPPORT
NEAR_DELTA_MINK_L
NEAR_DELTA_MINK_V
HIGH_POISSON_N_DRIFT
BH_SUPPORT_ASYMMETRY
```

No threshold may be changed after evaluation.

## 12. Terminal precedence

Exactly one terminal is emitted, with this precedence:

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
MINK_CONTROL_DEGENERATE_ON_NEW_GEOMETRY
INSUFFICIENT_VALID_PAIRS
```

### Scientific

```text
BH_MINK_DISPERSION_DIFFERENCE_DETECTED
NO_BH_MINK_DISPERSION_DIFFERENCE_DETECTED
INCONCLUSIVE_SCIENTIFIC_CONTRAST
```

Interpretation rule:

A contract/design terminal must not be converted into a scientific result.

## 13. Reporting rules

The final report must state:

1. This is a new question under `SQUARE_BOX_2P4`.
2. The R-VAR closure remains intact:
   `CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]`.
3. No old seeds, thresholds, or artifacts were reused.
4. The terminal emitted under this contract.
5. Whether the terminal is integrity, contract/design, or scientific.
6. No horizon reconstruction claim is made.

## 14. Evidence directory

All outputs must go under:

```text
evidence/new_geometry_20260719/
```

Required files:

```text
manifest.json
claim_ledger.md
summary_report.md
per_seed_metrics.csv
terminal.txt
environment.txt
```

No output may be written to the old R-VAR artifact locations.

## 15. Freeze condition

This contract is frozen by PI instruction "adelante" on 2026-07-19 after review of the proposed
geometry and contract text.

At freeze:

```text
NO_DATA_GENERATED
NO_EVALUATION_RUN
NO_SCIENTIFIC_RESULT
```

## CONTRACT FROZEN

Frozen by human review on 2026-07-19.
Geometry: SQUARE_BOX_2P4 (T=2.4, R=2.4, aspect ratio = 1.0)
Seeds: 4_200_000 .. 4_200_023 (disjoint)
Non-degeneracy threshold (primary intensity 9600.0): median(cv_L_MINK) >= 0.05 OR median(cv_V_MINK) >= 0.05, with ≥20/24 valid MINK seeds.
Previous R-VAR closure CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC] remains intact and untouched.
This is a new scientific question.
