# PRESENT_ANCHOR_SANITY_PILOT_V2_SUMMARY

STATUS: PRIVATE_EXPLORATORY

SCOPE: DIAGNOSTIC_ONLY

POSTHOC_REPAIR=YES

CHEAP_VERDICT_VERSION=v2_proxy_separated

expanded_kill_test_mode=True

KBEAM_USED=NO

COMMAND=dev/present_anchor_sanity_pilot.py --allow-expanded-kill-test --seeds 2000000,2000001,2000002,2000003,2000004,2000005,2000006,2000007,2000008,2000009,2000010,2000011 --intensity 1200 --max-anchors-per-rule 10 --output data/reports/present_anchor_clean_v3_kill_test.csv --summary-output data/reports/PRESENT_ANCHOR_CLEAN_V3_KILL_TEST_SUMMARY.md

## Status of v2

- v2 repairs a diagnostic scale bug found after v1.
- v2 is not a clean preregistered result.
- v2 may be used only to decide whether a future clean preregistered pilot is worth designing.

| metric | value |
|---|---|
| n_runs | 12 |
| n_anchors | 480 |
| median_past_volume | 329.5 |
| median_future_volume | 409.0 |
| median_volume_asymmetry | 0.1917 |
| median_depth_asymmetry | 0.1842 |
| verdict_counts | {'BOUNDARY_DOMINATED': 40, 'MIXED': 24, 'PROMISING': 416} |

PRESENT_ANCHOR_SANITY_RESULT=PROMISING

PRESENT_ANCHOR_V2_RESULT=PROMISING_BUT_POSTHOC

INTERPRETATION_LIMITS:

- No horizon claim.
- No order-only recoverability claim.
- No uncertainty-principle claim.
- No universality claim.
