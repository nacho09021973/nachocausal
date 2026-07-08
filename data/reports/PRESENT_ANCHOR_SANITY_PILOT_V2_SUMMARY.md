# PRESENT_ANCHOR_SANITY_PILOT_V2_SUMMARY

STATUS: PRIVATE_EXPLORATORY

SCOPE: DIAGNOSTIC_ONLY

POSTHOC_REPAIR=YES

CHEAP_VERDICT_VERSION=v2_proxy_separated

KBEAM_USED=NO

COMMAND=dev/present_anchor_sanity_pilot.py --seeds 1000000,1000001,1000002 --intensity 600 --max-anchors-per-rule 5 --output data/reports/present_anchor_sanity_pilot_v2.csv --summary-output data/reports/PRESENT_ANCHOR_SANITY_PILOT_V2_SUMMARY.md

## Status of v2

- v2 repairs a diagnostic scale bug found after v1.
- v2 is not a clean preregistered result.
- v2 may be used only to decide whether a future clean preregistered pilot is worth designing.

| metric | value |
|---|---|
| n_runs | 3 |
| n_anchors | 60 |
| median_past_volume | 169.5 |
| median_future_volume | 199.0 |
| median_volume_asymmetry | 0.1299 |
| median_depth_asymmetry | 0.1667 |
| verdict_counts | {'BOUNDARY_DOMINATED': 3, 'MIXED': 3, 'PROMISING': 54} |

PRESENT_ANCHOR_SANITY_RESULT=PROMISING

PRESENT_ANCHOR_V2_RESULT=PROMISING_BUT_POSTHOC

INTERPRETATION_LIMITS:

- No horizon claim.
- No order-only recoverability claim.
- No uncertainty-principle claim.
- No universality claim.
