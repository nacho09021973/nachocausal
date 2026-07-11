# PRESENT_ANCHOR_CLEAN_V3_KILL_DECISION

Status: PRIVATE_EXPLORATORY_KILL_TEST

expanded_kill_test_mode=True

This is not a publication result, not a horizon reconstruction claim, not an order-only recovery claim, and not evidence for universality.

Fresh seeds: 2000000-2000011
Intensity: 1200
Max anchors per rule: 10

Total rows / anchors: 480

## Verdicts And Medians By Rule

| anchor_rule_id | n | promising | mixed | boundary | degenerate | promising_fraction | boundary_fraction | median_volume_asymmetry | median_depth_asymmetry | median_past_volume | median_future_volume | median_past_depth | median_future_depth |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BALANCED_PAST_FUTURE_VOLUME_POINT | 120 | 118 | 0 | 2 | 0 | 0.983333 | 0.0166667 | 0.00914467 | 0.223051 | 366 | 366.5 | 45 | 28 |
| CENTRAL_EMBEDDING_POINT | 120 | 120 | 0 | 0 | 0 | 1 | 0 | 0.131199 | 0.135135 | 342.5 | 444 | 40.5 | 30 |
| MIDRANK_ORDER_POINT | 120 | 110 | 8 | 2 | 0 | 0.916667 | 0.0166667 | 0.28391 | 0 | 267.5 | 478 | 35 | 35 |
| RANDOM_ELIGIBLE_INTERNAL_POINT | 120 | 68 | 16 | 36 | 0 | 0.566667 | 0.3 | 0.691118 | 0.519568 | 313 | 276.5 | 37.5 | 22.5 |

## Primary Decision Rule

Primary rule: RANDOM_ELIGIBLE_INTERNAL_POINT

KEEP_PRESENT_ANCHOR iff:
- promising_fraction >= 0.65
- boundary_fraction <= 0.20
- median_volume_asymmetry <= 0.45
- median_depth_asymmetry <= 0.45

PRESENT_ANCHOR_CLEAN_V3_DECISION=PARK_PRESENT_ANCHOR

Decision checks: promising_fraction >= 0.65: FAIL; boundary_fraction <= 0.20: FAIL; median_volume_asymmetry <= 0.45: FAIL; median_depth_asymmetry <= 0.45: FAIL

## Secondary Decision Rule

MIDRANK_ORDER_POINT: promising_fraction=0.917, boundary_fraction=0.017, median_volume_asymmetry=0.284, median_depth_asymmetry=0.000

## Interpretation Constraints

- BALANCED_PAST_FUTURE_VOLUME_POINT is diagnostic only because it can manufacture volume symmetry by construction.
- MIDRANK_ORDER_POINT is secondary because it partially constrains depth by construction.
- CENTRAL_EMBEDDING_POINT is geometry-assisted and cannot support order-only claims.
- RANDOM_ELIGIBLE_INTERNAL_POINT is the primary kill-test rule because it is the least tuned anchor rule in this pilot.

## End State

The present-anchor line should be parked unless there is a separate physical reason to revisit it.
