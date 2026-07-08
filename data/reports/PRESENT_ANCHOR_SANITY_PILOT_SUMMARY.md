# PRESENT_ANCHOR_SANITY_PILOT_SUMMARY

STATUS: PRIVATE_EXPLORATORY

SCOPE: DIAGNOSTIC_ONLY

KBEAM_USED=NO

COMMAND=dev/present_anchor_sanity_pilot.py --seeds 1000000,1000001,1000002 --intensity 600 --max-anchors-per-rule 5

| metric | value |
|---|---|
| n_runs | 3 |
| n_anchors | 60 |
| median_past_volume | 169.5 |
| median_future_volume | 199.0 |
| median_volume_asymmetry | 0.1299 |
| median_depth_asymmetry | 0.1667 |
| verdict_counts | {'BOUNDARY_DOMINATED': 18, 'MIXED': 3, 'PROMISING': 39} |

PRESENT_ANCHOR_SANITY_RESULT=PROMISING

INTERPRETATION_LIMITS:

- No horizon claim.
- No order-only recoverability claim.
- No uncertainty-principle claim.
- No universality claim.
