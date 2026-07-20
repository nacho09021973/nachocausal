# MINK control-only measurement

STATUS: MINK_CONTROL_ONLY_MEASUREMENT_COMPLETE

Scope: MINK coverage and non-degeneration only. No BH rows were computed; no BH-vs-MINK signal or p-value was calculated.

Previous R-VAR closure remains intact: `CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]`.

Terminal:

```text
MINK_CONTROL_NONDEGENERATE_ON_NEW_GEOMETRY
layer=contract/design
```

Summary by intensity:

```json
{
  "1200.0": {
    "median_cv_L_MINK": 0.04542512520706844,
    "median_cv_V_MINK": 0.11665174015233362,
    "passes_support": true,
    "total_mink_seeds": 24,
    "valid_mink_seeds": 24
  },
  "2400.0": {
    "median_cv_L_MINK": 0.031294678411653065,
    "median_cv_V_MINK": 0.11599322670960069,
    "passes_support": true,
    "total_mink_seeds": 24,
    "valid_mink_seeds": 24
  },
  "4800.0": {
    "median_cv_L_MINK": 0.027567137189878483,
    "median_cv_V_MINK": 0.11362586664737001,
    "passes_support": true,
    "total_mink_seeds": 24,
    "valid_mink_seeds": 24
  },
  "9600.0": {
    "median_cv_L_MINK": 0.019746455489398754,
    "median_cv_V_MINK": 0.11488594284354918,
    "passes_support": true,
    "total_mink_seeds": 24,
    "valid_mink_seeds": 24
  }
}
```
