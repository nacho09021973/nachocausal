# SQUARE_BOX_2P4 Future-Observable Dispersion Addendum

STATUS: SEALED_RESULT_ADDENDUM
DATE: 2026-07-19

## 1. Result in one sentence

Under the frozen `SQUARE_BOX_2P4` contract, the order-only future-observable dispersion summaries
on minimal elements distinguish `BH` from `MINK` at the primary endpoint.

Terminal:

```text
BH_MINK_DISPERSION_DIFFERENCE_DETECTED
layer=scientific
geometry=SQUARE_BOX_2P4
previous_RVAR_closure=INTACT
```

## 2. Boundary of the claim

This is a new scientific question, not a repair, continuation, re-evaluation, or reinterpretation
of R-VAR.

The previous R-VAR closure remains intact:

```text
CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]
```

This result does not:

- localize a horizon;
- reconstruct geometry;
- supersede the tall-box R-VAR closure;
- claim that the original R-VAR observable would have passed under its old contract;
- reuse old R-VAR, PR009, PR010, or prereg-002 validation seeds as evaluation data.

Allowed interpretation:

> In a square finite patch where the flat control is not near-delta under the frozen
> non-degeneration gate, the predefined order-only future-observable dispersion summaries
> `cv_L` and `cv_V` separate the BH and MINK laws on the frozen evaluation seeds.

## 3. Frozen setup

Contract:

```text
docs/preregistration_new_geometry_future_observables.md
```

Geometry:

```text
PATCH_GEOMETRY = SQUARE_BOX_2P4
T_EDGE_NEW = 2.4
R_EDGE_NEW = 2.4
R_CENTER_NEW = 1.3
R_S = 0.5
BOX_AREA_NEW = 5.76
ASPECT_RATIO_NEW = 1.0
```

Evaluation seeds:

```text
4_200_000 .. 4_200_023
```

These seeds are documented as disjoint from the old `DEV_SEEDS`, `EXPLORE_POOL`, PR010 development
seeds, prereg-002 validation band, and OP-2.1 synthetic band.

Primary endpoint:

```text
PRIMARY_INTENSITY_NEW = 9600.0
```

## 4. Observables and frozen contrast

For each minimal element `i ∈ Min(C)`:

```text
L(i) = longest future-chain length from i
V(i) = |J⁺(i)|
```

The per-seed dispersion summaries are:

```text
cv_L = std(L(i)) / mean(L(i))
cv_V = std(V(i)) / mean(V(i))
```

The frozen BH-vs-MINK contrasts are:

```text
D_L(seed) = cv_L_BH(seed) - cv_L_MINK(seed)
D_V(seed) = cv_V_BH(seed) - cv_V_MINK(seed)
```

The frozen success rule requires:

```text
median(D_L) > 0 OR median(D_V) > 0
```

and paired sign-flip:

```text
p_perm <= 0.01
```

for at least one of `D_L`, `D_V`, after the Minkowski non-degeneration gate passes.

## 5. Coverage and control

Coverage was complete:

```text
24/24 valid seeds in every BH/MINK × intensity cell
24/24 valid BH/MINK paired seeds at the primary endpoint
```

The flat control passed the frozen non-degeneration gate at the primary endpoint:

```text
MINK median cv_L = 0.019746455489398754
MINK median cv_V = 0.11488594284354918
non-degeneration condition met via median(cv_V_MINK) >= 0.05
```

## 6. Primary endpoint result

At `PRIMARY_INTENSITY_NEW = 9600.0`:

```text
BH   median cv_L = 0.5170298920626035
BH   median cv_V = 0.5894871796768844
MINK median cv_L = 0.019746455489398754
MINK median cv_V = 0.11488594284354918
```

Observed contrasts:

```text
median(D_L) = 0.4987114017481817
median(D_V) = 0.47639013575705436
p_perm(D_L) = 1.1920928955078125e-07
p_perm(D_V) = 1.1920928955078125e-07
```

Both dispersion contrasts are positive and pass the frozen paired sign-flip threshold.

## 7. Evidence

Primary evidence directory:

```text
evidence/new_geometry_20260719/
```

Key files:

```text
evidence/new_geometry_20260719/CONTRACT_FROZEN.txt
evidence/new_geometry_20260719/per_seed_metrics.csv
evidence/new_geometry_20260719/evaluation_summary.json
evidence/new_geometry_20260719/evaluation_report.md
evidence/new_geometry_20260719/claim_ledger.md
evidence/new_geometry_20260719/terminal.txt
evidence/new_geometry_20260719/RESULT_SEALED.txt
```

Final seal record:

```text
evidence/new_geometry_20260719/RESULT_SEALED.txt
```

## 8. Interpretation

This addendum establishes a positive, bounded result for a new geometry:

```text
BH_MINK_DISPERSION_DIFFERENCE_DETECTED
```

It shows that the future-observable dispersion channel is not intrinsically dead: under a square
patch with a non-degenerate flat control, the predefined `L(i)`/`V(i)` dispersion summaries
separate BH from MINK.

It does not yet show that those summaries localize the relevant boundary. A boundary-localization
question would require a separate preregistration, output object, scoring rule, and terminal
discipline.
