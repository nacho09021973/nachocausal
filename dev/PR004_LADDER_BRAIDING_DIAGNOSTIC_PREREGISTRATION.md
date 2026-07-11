# PR004 Ladder Braiding / Peel-Off Diagnostic Preregistration

## 1. Status

STATUS: PRIVATE EXPLORATORY PREREGISTRATION

- Not part of Paper I public claim.
- No confirmation claim allowed.

## 2. Motivation

Existing PR003 / K-beam logs show aggregate peel-off: early rungs remain
relatively adherent, while tails drift away.

Existing scripts already contain per-survivor / per-depth state in memory, but
the current aggregation discards it before persistence.

The goal of this exploratory preregistration is to test whether peel-off is
random per ladder or whether it shows collective structure compatible with a
braiding-defect hypothesis.

## 3. Physical Question

Does the peel-off of fuzzy ladders occur independently and diffusely, or do
multiple ladders lose adherence around a common depth / radial region?

## 4. Diagnostic Table

Name:

`kbeam_braiding_diagnostic_per_survivor.csv`

Columns:

- `seed`
- `intensity`
- `K`
- `start_id`
- `sp`
- `sq`
- `depth_k`
- `survivor_rank`
- `p_last`
- `q_last`
- `r_p_last`
- `r_q_last`
- `d_p_over_ell`
- `d_q_over_ell`
- `d_mid_over_ell`
- `straddles_horizon`
- `regscore`
- `is_top1`
- `is_minbeam_at_k`
- `path_p`
- `path_q`

## 5. Definitions

- `r_mid_last = 0.5 * (r_p_last + r_q_last)`
- `d_mid_over_ell = abs(r_mid_last - R_S) / ell`
- `straddles_horizon = (r_p_last - R_S) * (r_q_last - R_S) <= 0`

## 6. Primary Peel-Off Definition

`PEEL_OFF_K_MEDIAN3`:

first `depth_k` where `d_mid_over_ell > 3` and remains `> 3` for all later
recorded depths of that survivor.

## 7. Secondary Peel-Off Definition

`PEEL_OFF_K_STRADDLE_LOSS`:

first `depth_k` after which `straddles_horizon` is `False` and never returns to
`True`, restricted to ladders that straddled at least once in the early
segment.

## 8. Preliminary Braiding-Defect Criterion

Exploratory only:

compatible with collective braiding if, within the same intensity and `K`,
multiple starts / seeds show similar `peel_off_k` and concentrated `r_mid_last`
near peel-off.

Compatible with random peel-off if `peel_off_k` and `r_mid_last` are broadly
dispersed.

## 9. What This Can Test

- whether peel-off is concentrated in depth;
- whether peel-off is radially concentrated;
- whether `top1` and `minbeam` behave differently;
- whether the signal depends on `K`, seed, or start.

## 10. What This Cannot Claim

- no proof of a physical defect;
- no order-only intrinsic localization, because embedded `r` is used for
  diagnosis;
- no 3+1D claim;
- no horizon reconstruction claim;
- no asymptotic stability claim;
- no update to Paper I public result.

## 11. Stop Rule

No run should be interpreted as confirmatory unless a later preregistration
freezes:

- data-producing command;
- intensities;
- seeds;
- `K` values;
- output path;
- pass/fail or descriptive-only status.
