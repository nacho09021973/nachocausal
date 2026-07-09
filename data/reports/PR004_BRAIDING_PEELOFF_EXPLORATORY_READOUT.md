# PR004 Braiding / Peel-Off — Exploratory Readout

STATUS: EXPLORATORY_READOUT_ONLY
VERDICT: INCONCLUSIVE_WITH_DEFINITION_BLOCKERS
VALIDATION_STATUS: NOT_VALIDATION_GRADE
NEXT_ALLOWED_USE: DESIGN_INPUT_FOR_PR004_BRAIDING_V2_ONLY

## 1. Files Read

- `dev/PR004_LADDER_BRAIDING_DIAGNOSTIC_PREREGISTRATION.md`
- `data/reports/kbeam_braiding_diagnostic_per_survivor.csv`

No scripts were touched, no seals were touched, and the CSV was not regenerated. This
readout is a post-hoc description of an exploratory console analysis run against the
existing, already-generated CSV.

## 2. Real CSV Schema

- 90,446 rows
- 15 columns
- Real columns: `seed, intensity, K, start_id, depth_k, survivor_rank, p_last, q_last,
  r_p_last, r_q_last, d_mid_over_ell, straddles_horizon, regscore, path_p, path_q`

Discrepancy against preregistration §4: `sp`, `sq`, `d_p_over_ell`, `d_q_over_ell`,
`is_top1`, `is_minbeam_at_k` are declared in the preregistration's diagnostic table but
are **not present** in the actual CSV.

## 3. Structural Finding

`survivor_rank` is reassigned per depth — it is a rank *within that depth's population*,
not a persistent survivor identifier. It cannot be used on its own to track "the same
survivor" across increasing `depth_k`.

To reconstruct per-survivor lineages across depths, path prefixes of `path_p` / `path_q`
were used (a child row's path is its parent row's path plus one element). This is a
necessary operational interpretation required to even evaluate the preregistration's own
§6 language ("remains > 3 for all later recorded depths of that survivor") — it is not a
column or definition that the preregistration explicitly specifies.

## 4. Descriptive Results

### PEEL_OFF_K_MEDIAN3

- Defined in 42,304 / 58,215 lineages (72.7%)
- Mean: 4.60
- Median: 2
- Std: 5.50
- Min: 1
- Max: 25
- Mode: k=1 (30.7% of defined cases)
- By intensity: means similar across 3600 / 7200 / 14400 (~4.13–5.04 range, no sharp
  separation)
- Seed-to-seed variation is real: per-seed means range roughly between 3.0 and 6.4

### r_mid_at_peel

- Global mean: 0.50
- Std: 0.16
- Range: [0.13, 1.27]
- Std by intensity decreases roughly from 0.245 (intensity 3600) to 0.112 (intensity
  14400) — a mild narrowing, not a collapse to a point

### PEEL_OFF_K_STRADDLE_LOSS

The exact preregistered version (§7) is blocked: it is restricted to lineages that
straddled "in the early segment," and "early segment" has no numeric definition anywhere
in the preregistration.

Descriptive, non-confirmatory numbers (unrestricted — straddled at least once, at any
depth):

- 15,667 lineages straddle at least once
- 12,225 of those lose the straddle permanently at some point
- Mean k: 9.18
- Median k: 9
- Std: 6.42

## 5. Classification

**Not CONCENTRATED_SIGNAL:**
- There is marginal concentration in low k and around r_mid ≈ 0.4–0.6
- But there is no preregistered numeric threshold for "concentrated"
- There is real seed-to-seed dispersion
- There is a long tail out to k=25
- 27.3% of lineages never peel off within the recorded depth range

**Not DISPERSED_SIGNAL:**
- There is likewise no preregistered numeric threshold for "dispersed"
- There is a strong mode at k=1 and non-trivial early concentration

**Conclusion: INCONCLUSIVE_WITH_DEFINITION_BLOCKERS.**

## 6. Methodological Warnings

- Survivor bias: lineages that "never peel off" are plausibly correlated with early
  elimination from the beam (shorter chains); the apparent low-k concentration may partly
  reflect which lineages survive long enough to be measured, not a collective braiding
  defect.
- This data has already been observed in this exploratory pass — it cannot be reused
  retroactively as confirmatory/validation data under a later preregistration's stop
  rule.
- This is not order-only evidence: the diagnostic reads embedded radii (`r_p_last`,
  `r_q_last`) for scoring, per preregistration §10's own caveat.
- This does not validate PR004.
- This does not definitively refute the braiding/peel-off hypothesis either.
- Present-anchor work remains parked and separate; it is not mixed into this line of
  analysis.

## 7. Operational Consequence

No further analysis of this CSV should be used as validation.

The only permitted use of the already-observed CSV is to design a PR004 braiding V2 with:

- frozen columns (including persistent lineage/survivor identity, `is_top1`, and
  `is_minbeam_at_k` if those distinctions are wanted)
- persistent lineage/survivor identity (not depth-relative `survivor_rank`)
- a numeric definition of "early segment" for PEEL_OFF_K_STRADDLE_LOSS
- quantitative thresholds for "concentrated" vs "dispersed" under §8
- data-producing command, seeds, intensities, K, and output path frozen before any new
  data is generated
