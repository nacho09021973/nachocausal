# New Geometry Future Observables — Evaluation Report

STATUS: SCIENTIFIC_EVALUATION_COMPLETE

This is a new scientific question under `SQUARE_BOX_2P4`.

The previous R-VAR closure remains intact and untouched:

```text
CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]
```

No old R-VAR seeds, thresholds, evaluation artifacts, PR009 outputs, PR010 artifacts, or prereg-002 validation artifacts were used as evaluation data.

## Terminal

```text
BH_MINK_DISPERSION_DIFFERENCE_DETECTED
layer=scientific
```

## Coverage

```json
{
  "BH_1200.0": {
    "total": 24,
    "valid": 24
  },
  "BH_2400.0": {
    "total": 24,
    "valid": 24
  },
  "BH_4800.0": {
    "total": 24,
    "valid": 24
  },
  "BH_9600.0": {
    "total": 24,
    "valid": 24
  },
  "MINK_1200.0": {
    "total": 24,
    "valid": 24
  },
  "MINK_2400.0": {
    "total": 24,
    "valid": 24
  },
  "MINK_4800.0": {
    "total": 24,
    "valid": 24
  },
  "MINK_9600.0": {
    "total": 24,
    "valid": 24
  }
}
```

At the primary intensity `9600.0`, valid BH/MINK paired seeds: `24/24`.

## Primary endpoint summaries

```text
MINK median cv_L = 0.019746455489398754
MINK median cv_V = 0.11488594284354918
BH   median cv_L = 0.5170298920626035
BH   median cv_V = 0.5894871796768844
```

The frozen Minkowski non-degeneration condition remains satisfied at the primary endpoint via `median(cv_V_MINK) >= 0.05`.

## Scientific contrast

Frozen contrasts:

```text
D_L(seed) = cv_L_BH(seed) - cv_L_MINK(seed)
D_V(seed) = cv_V_BH(seed) - cv_V_MINK(seed)
```

Observed primary contrasts:

```text
median(D_L) = 0.4987114017481817
median(D_V) = 0.47639013575705436
p_perm(D_L) = 1.1920928955078125e-07
p_perm(D_V) = 1.1920928955078125e-07
```

The contract requires `median(D_L) > 0 OR median(D_V) > 0` and paired sign-flip `p_perm <= 0.01` for at least one contrast. This condition is met.

## Claim boundary

This result detects a BH-vs-MINK dispersion difference for the predefined future-observable summaries in the new square-box geometry. It does not localize a horizon, does not reconstruct geometry, and does not repair or supersede the prior R-VAR closure.
