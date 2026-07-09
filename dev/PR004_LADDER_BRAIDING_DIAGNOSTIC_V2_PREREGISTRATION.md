# PR004 Ladder Braiding / Peel-Off Diagnostic — V2 Preregistration

STATUS: PREREGISTRATION_DRAFT_V2
VALIDATION_STATUS: NOT_RUN
DATA_REUSE_POLICY: OLD_CSV_FOR_DESIGN_ONLY
OLD_CSV_VALIDATION_USE: FORBIDDEN
THRESHOLD_PROVENANCE: PROSPECTIVE_THRESHOLDS_AFTER_EXPLORATORY_V1

## 1. Relation to V1

- V1 (`dev/PR004_LADDER_BRAIDING_DIAGNOSTIC_PREREGISTRATION.md`) produced one exploratory
  readout: `data/reports/PR004_BRAIDING_PEELOFF_EXPLORATORY_READOUT.md`, classified
  `INCONCLUSIVE_WITH_DEFINITION_BLOCKERS`.
- The CSV behind that readout
  (`data/reports/kbeam_braiding_diagnostic_per_survivor.csv`) has already been observed.
  No additional analysis of that CSV — under any new framing — can count as validation
  of anything defined below. Its only sanctioned role was as **design input** for this V2
  document (see `NEXT_ALLOWED_USE` in the V1 readout).
- V2 requires **new data**, generated after the command, columns, seeds, intensities, K
  grid, and output path below are frozen (i.e. this file is committed as-is, unedited,
  before the producing command is run).
- Any numeric threshold chosen in §6 below is anchored to constants already frozen
  elsewhere in the codebase (`M`, `ADH`, `LMAX`, `MIN_LEN` in
  `dev/measure_kbeam_peeloff.py`) or to standard, named statistical rules of thumb
  (uniform-baseline multiples, small/large coefficient-of-variation cutoffs) — not fit to
  reproduce the V1 exploratory numbers. Where a V1 number happens to fall inside a
  threshold band, that is noted as a consistency check, not as the basis for the
  threshold.

## 2. Mandatory Columns (frozen data contract)

The V2 per-depth, per-lineage output CSV MUST contain exactly these columns:

- `seed`
- `intensity`
- `K`
- `start_id`
- `depth_k`
- `lineage_id`
- `survivor_rank_at_depth`
- `path_p`
- `path_q`
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

Rules:

- `lineage_id` MUST be persistent across all recorded `depth_k` values of the same
  survivor (assigned once when a candidate is first created, inherited unchanged by
  every deeper row that extends it). It is the sole key for grouping a lineage's
  depth-series.
- `survivor_rank_at_depth` MUST NOT be used, by itself or elsewhere in this document, as
  a persistent survivor identity. It is a within-depth rank only (this is the exact
  failure mode identified in the V1 structural finding: `survivor_rank` is reassigned
  every depth).
- `path_p` / `path_q` are retained for auditability (independent reconstruction check
  against `lineage_id`), not as the primary lineage key.

## 3. Operational Definitions

### 3.1 PEEL_OFF_K_MEDIAN3

- Criterion variable: `d_mid_over_ell` only (not `d_p_over_ell`/`d_q_over_ell`
  individually, and not `straddles_horizon`). `d_p_over_ell` and `d_q_over_ell` are
  recorded as diagnostic companions to check post hoc whether peel-off is symmetric
  between the `p` and `q` rungs, but they are not part of the primary criterion — mixing
  three criteria into one definition is exactly the ambiguity V1 left open.
- Threshold: `d_mid_over_ell > 3`, using the value `3` already frozen as `ADH` in
  `dev/measure_kbeam_peeloff.py` ("adherence band in ℓ"), not a new number.
- Window: exactly 3 **consecutive recorded depths** (`depth_k = k0, k0+1, k0+2`), matching
  the window size named in `PEEL_OFF_K_MEDIAN3` itself and matching `M = 3` already
  frozen in the same script. This replaces V1's open-ended "remains > 3 for all later
  recorded depths," which was vacuously satisfiable at a lineage's last recorded depth.
- Per-lineage evaluation, using `chain_len` = the number of consecutive recorded depths
  of that `lineage_id` (1..chain_len, no gaps, since a lineage's path grows by exactly
  one rung per depth):
  - `PEEL_OFF_K_MEDIAN3 := min { k0 : k0 + 2 ≤ chain_len AND d_mid_over_ell(k) > 3 for all k in [k0, k0+2] }`
  - If no such `k0` exists in `[1, chain_len - 2]`: status = `NOT_PEELED_WITHIN_RECORDED_DEPTH`.
  - If `chain_len < 3`: status = `UNDEFINED_TOO_SHORT` (the window cannot even be
    evaluated once). This is reported and denominatored separately — see §5.

### 3.2 PEEL_OFF_K_STRADDLE_LOSS

- Early-segment definition (chosen from the three options offered): **Option A**,
  `depth_k ≤ 3`.
- Justification: this is anchored to `M = 3` (the EGS fuzziness parameter already frozen
  in `dev/measure_kbeam_peeloff.py`), giving the same window size used in §3.1 rather
  than an independently invented number. It is also guaranteed non-degenerate for every
  lineage that clears the existing `MIN_LEN = 6` filter already applied upstream (every
  such lineage has ≥ 6 recorded depths, so depths 1–3 are always inside its recorded
  range). Option B (first 25% of observed depths) was rejected because `chain_len` varies
  per lineage (6–25 in the V1 data), making "early" a different absolute window per
  lineage and breaking cross-lineage comparability — exactly the kind of
  after-the-fact-adjustable definition this V2 is meant to eliminate.
- `PEEL_OFF_K_STRADDLE_LOSS` is defined only for lineages with `straddles_horizon == True`
  for at least one `depth_k ∈ [1,3]`. Lineages without an early straddle get status
  `NOT_APPLICABLE_NO_EARLY_STRADDLE` and are excluded from this metric's denominator by
  construction (matching V1 §7's own restriction language, now made precise).
- For qualifying lineages: `PEEL_OFF_K_STRADDLE_LOSS := min { k1 : straddles_horizon(k) == False for all k in [k1, chain_len] }`.
  - If no such `k1` exists (still straddling at the last recorded depth): status =
    `NOT_LOST_WITHIN_RECORDED_DEPTH` (right-censored, not "never loses").

## 4. Survivor Bias / Censoring

- `UNDEFINED_TOO_SHORT` and `NOT_LOST_WITHIN_RECORDED_DEPTH` / `NOT_PEELED_WITHIN_RECORDED_DEPTH`
  lineages are never silently folded into "not peeled" or dropped. Each gets its own
  status label (§3) and its own count.
- Denominators:
  - Proportion `PEELED` = `count(PEELED) / count(lineages with chain_len ≥ 3)`.
    `UNDEFINED_TOO_SHORT` lineages are excluded from this denominator, not counted as
    non-peeling.
  - Censoring rate = `count(UNDEFINED_TOO_SHORT) / count(all lineages)`, reported
    alongside every headline PEEL_OFF_K_MEDIAN3 number, unconditionally.
  - The same exclude-from-denominator / report-rate-separately rule applies to
    `PEEL_OFF_K_STRADDLE_LOSS` using `NOT_LOST_WITHIN_RECORDED_DEPTH` and
    `NOT_APPLICABLE_NO_EARLY_STRADDLE`.
- Mandatory censoring sensitivity check: every headline number in §6 MUST be computed
  twice — once over all lineages with `chain_len ≥ 3`, and once restricted to lineages
  with `chain_len ≥ MIN_LEN` (`MIN_LEN = 6`, the filter already applied upstream to
  ladders in `dev/measure_kbeam_peeloff.py`). If the two computations disagree on the
  final classification (§6), the result is automatically downgraded to `INCONCLUSIVE`
  regardless of what either computation alone would have said. This directly targets the
  survivor-bias warning raised in the V1 readout §6.

## 5. Denominators — Summary Table (to be filled by the run, not now)

| Quantity | Denominator |
|---|---|
| Proportion PEELED (MEDIAN3) | lineages with chain_len ≥ 3, excluding UNDEFINED_TOO_SHORT |
| Censoring rate (MEDIAN3) | all lineages with chain_len ≥ 3 |
| Proportion lost (STRADDLE_LOSS) | lineages with an early straddle (depth_k∈[1,3]), excluding NOT_LOST_WITHIN_RECORDED_DEPTH |
| Right-censoring rate (STRADDLE_LOSS) | lineages with an early straddle |

## 6. Quantitative Decision Criteria

Replaces V1 §8's qualitative "concentrated vs dispersed" language entirely. Let
`LMAX = 25` (frozen ladder depth cap in `dev/measure_kbeam_peeloff.py`).

Binning for concentration: partition depths `[1, LMAX]` into `ceil(LMAX/3) = 9`
contiguous bins of width 3 (bins `[1-3],[4-6],...,[25]`), the same window width as §3.1.
Uniform-null bin fraction = `1/9 ≈ 11.1%`.

**Threshold provenance.** Every numeric threshold below is labeled
`PROSPECTIVE_THRESHOLDS_AFTER_EXPLORATORY_V1` (see status block). They were chosen after
the V1 exploratory readout had already been produced and inspected in this same line of
work. Anchoring them to constants already frozen before V1 ran (`M`, `ADH`, `LMAX`,
`MIN_LEN`) and to standard rule-of-thumb multipliers reduces, but does not eliminate, the
risk that the specific multiples chosen (3×, 1.5×, the 0.15/0.35 CV cutoffs, the LMAX/2
tail split, the 30% censoring cap) were shaped by hindsight. This document and any
downstream report MUST NOT describe these thresholds as fixed independently of, or prior
to, V1 — they are prospective relative to the V2 run they gate, but retrospective
relative to V1's exploratory numbers. A future preregistration whose thresholds are meant
to be free of this caveat must set them before any exploratory pass over the relevant
data; this one does not qualify.

### Order of Evaluation (decision tree)

Evaluate strictly in this order; stop at the first applicable terminal label. This is the
single authoritative decision path — nothing below may be reordered or short-circuited
differently at analysis time.

1. **Data contract.** Check the mandatory columns (§2), `lineage_id` persistence, and
   evaluability of the §3 definitions. If any is violated → `FAILED_DATA_CONTRACT`, stop.
   If the frozen command (§7) itself did not complete → `FAILED_RUNTIME`, stop.
2. **Censoring.** Compute the censoring rate (§4/§5). If it exceeds 30% of all lineages
   with `chain_len ≥ 3` → `FAILED_DATA_CONTRACT`, stop. (This is part of the same
   data-contract gate as step 1, evaluated immediately after the column/persistence
   checks, not a separate later gate.)
3. **Computability.** For every remaining lineage, evaluate `PEEL_OFF_K_MEDIAN3` (§3.1)
   and `PEEL_OFF_K_STRADDLE_LOSS` (§3.2), producing the per-lineage statuses defined
   there (`PEELED` / `NOT_PEELED_WITHIN_RECORDED_DEPTH` / `UNDEFINED_TOO_SHORT`, and the
   STRADDLE_LOSS equivalents). This step never itself yields a run-level classification —
   it only produces the per-lineage inputs step 4 consumes.
4. **Concentration / dispersion gates.** Using `PEELED` lineages only, test
   `CONCENTRATED_SIGNAL` then `DISPERSED_SIGNAL` against the criteria below. These two
   are mutually exclusive by construction: the modal-bin thresholds do not overlap
   (`≥ 33%` vs `≤ 17%`), so no run can satisfy both.
5. **Fallback.** If neither gate in step 4 is fully satisfied, or the censoring
   sensitivity check (§4) flips the result between the two `chain_len` cutoffs →
   `INCONCLUSIVE`.

**Data-contract gate (checked first, applies to every run):**

- `FAILED_DATA_CONTRACT` if any of: a mandatory column (§2) is missing or malformed;
  `lineage_id` is not verifiably persistent (spot-check: reconstructing lineage via
  `path_p`/`path_q` prefixes must agree with `lineage_id` grouping); the early-segment or
  window definitions in §3 cannot be evaluated as specified; OR the censoring rate for
  `PEELED` (§4/§5) exceeds 30% of all lineages with `chain_len ≥ 3`.
- `FAILED_RUNTIME` if the frozen command (§7) does not complete: crash, seal mismatch
  (pre or post), timeout, or an output file that does not match the frozen path/schema.

**If the data-contract gate passes, evaluate on PEELED lineages only:**

- `CONCENTRATED_SIGNAL` requires ALL of:
  - modal 3-depth bin holds ≥ 33% of PEELED lineages (3× the uniform-null baseline);
  - seed dispersion `CV_seed = std(per-seed mean PEEL_OFF_K_MEDIAN3) / mean(per-seed mean PEEL_OFF_K_MEDIAN3)`,
    computed within each `intensity` group, is `≤ 0.15` for every intensity group;
  - long-tail fraction (`PEEL_OFF_K_MEDIAN3 > LMAX/2`, i.e. `k > 12`) is `≤ 10%`.
- `DISPERSED_SIGNAL` requires ALL of:
  - modal 3-depth bin holds `≤ 17%` of PEELED lineages (1.5× the uniform-null baseline)
    AND no single bin exceeds 20%;
  - `CV_seed ≥ 0.35` for every intensity group.
- `INCONCLUSIVE`: data-contract gate passes, but neither the full `CONCENTRATED_SIGNAL`
  criterion set nor the full `DISPERSED_SIGNAL` criterion set is jointly satisfied (e.g.
  a tight modal bin with high seed dispersion, or vice versa), OR the censoring
  sensitivity check in §4 flips the classification.

`r_mid_at_peel` (the embedded `r_mid` value at each lineage's `PEEL_OFF_K_MEDIAN3` depth,
where recorded) is reported descriptively — `CV_r = std/mean` — but is **never** part of
the gating logic above. It is labeled `DIAGNOSTIC_ONLY / GROUND_TRUTH_READOUT`, per §10.

## 7. Command To Freeze Before Run

```
COMMAND_TO_FREEZE_BEFORE_RUN:
python3 dev/measure_kbeam_peeloff.py --seeds 6 --intensities 3600,7200,14400 \
  --probe-out data/reports/pr004_braiding_v2_per_lineage.csv --probe-k 8
```

**Scope of this first run (Option A — single-K).** `--probe-k 8` uses `K_REF = 8`,
already frozen in `dev/measure_kbeam_peeloff.py` as "the reference tail depth for the
adherence-vs-K read" — not a new number invented for this freeze. `--seeds 6` and
`--intensities 3600,7200,14400` reuse the same seed count and intensity grid already used
to produce the V1 CSV (`data/reports/kbeam_braiding_diagnostic_per_survivor.csv`),
unchanged here because V2 revises the per-lineage *definitions and columns*, not the
sampling grid.

This first V2 run is a single-K primary diagnostic at `K_REF = 8`. Multi-K output
(`REQUIRED_IMPLEMENTATION_CHANGE` item 6 below) remains unresolved and is **not required**
for the primary `CONCENTRATED_SIGNAL` / `DISPERSED_SIGNAL` / `INCONCLUSIVE` classification
in §6. It is explicitly out of scope for this run and does not gate it.

Items 1–5 below are implemented in the working tree of `dev/measure_kbeam_peeloff.py` as
of this preregistration edit (persistent `lineage_id` in `kbeam()`, the renamed
`survivor_rank_at_depth` field, `d_p_over_ell`/`d_q_over_ell`, `is_top1`, and
`is_minbeam_at_k` all present in `PROBE_FIELDS` and wired into the probe-writer path) —
not yet committed as of this edit. Item 6 is deliberately not implemented and is deferred,
per the scope note above.

**REQUIRED_IMPLEMENTATION_CHANGE** (items 1–5 landed in the working tree and reviewed as
of this edit; item 6 deferred and out of scope for this first run):

1. Assign a persistent `lineage_id` at candidate-creation time in `kbeam()` and thread it
   through `by_depth`, so each row in the probe writer carries the same `lineage_id` its
   parent had, extended only by growth, never reassigned. — **DONE** (working tree, not
   committed).
2. Rename the existing `survivor_rank` probe field to `survivor_rank_at_depth` (no logic
   change — it already is depth-relative; this is a naming-contract fix only). —
   **DONE** (working tree, not committed).
3. Compute and emit `d_p_over_ell = abs(r_p_last - R_S) / ell` and
   `d_q_over_ell = abs(r_q_last - R_S) / ell` in the probe writer (currently only
   `d_mid_over_ell` is computed). — **DONE** (working tree, not committed).
4. Emit `is_top1` explicitly (currently only implicit via `survivor_rank_at_depth == 0`
   under the existing sort order — must be materialized as its own column so the
   contract does not silently depend on sort-order stability). — **DONE** (working tree,
   not committed).
5. Emit `is_minbeam_at_k`: the row within the same
   `(seed, intensity, K, start_id, depth_k)` group whose `d_mid_over_ell` is the minimum
   (ties broken by lowest `lineage_id`, to keep it deterministic). — **DONE** (working
   tree, not committed).
6. **DEFERRED — out of scope for this first run.** Decide and implement how multiple `K`
   values enter one frozen per-lineage output (the current `--probe-k` mechanism dumps
   exactly one `K` per invocation): either extend the probe writer to emit all `K` in
   `K_GRID` in one pass, or freeze a documented concatenation-of-runs procedure. This
   preregistration does not resolve that choice. It does not need to be resolved for the
   frozen command above (single-`K`, `K_REF=8`); it must be resolved and reviewed in a
   separate preregistration before any multi-K analysis is attempted.

No other flags, columns, or behaviors are assumed to exist beyond what is read in
`dev/measure_kbeam_peeloff.py` as of this preregistration.

## 8. Future Outputs (NOT_CREATED)

- `data/reports/pr004_braiding_v2_per_lineage.csv` — NOT_CREATED
- `data/reports/PR004_BRAIDING_V2_VALIDATION_REPORT.md` — NOT_CREATED

## 9. Stop Rule

- The output files in §8 may only be looked at after: (a) items 1–5 in §7 have landed and
  been reviewed (item 6 is explicitly deferred per §7's Option A scope note and does not
  gate this run), (b) the seal check (`assert_seal` pre and post, per
  `dev/measure_kbeam_peeloff.py`) has passed, (c) §7's `COMMAND_TO_FREEZE_BEFORE_RUN` has
  been filled in verbatim and committed unedited, and (d) the run has completed without
  `FAILED_RUNTIME`.
- Before those four conditions hold, no one may open, sample, or summarize
  `pr004_braiding_v2_per_lineage.csv`, by construction (it will not exist).
- Contract failure (`FAILED_DATA_CONTRACT`) blocks any further scientific interpretation
  of that specific run's output; it does not permit patching thresholds after the fact to
  rescue a classification.
- Prohibited after observing the V2 output: adjusting any threshold in §6, adding seeds,
  extending `LMAX`/`K_GRID`, or re-running with different parameters in response to a
  preliminary read of the result. Any such change requires a new, separately numbered
  preregistration (V3), not an edit to this file post-hoc.
- `VALIDATION_STATUS` MUST remain `NOT_RUN` until conditions (a)–(d) above all hold. Once
  they hold and the run completes, it MUST be updated to exactly one of
  `FAILED_RUNTIME`, `FAILED_DATA_CONTRACT`, `CONCENTRATED_SIGNAL`, `DISPERSED_SIGNAL`, or
  `INCONCLUSIVE` — matching the terminal label reached by §6's decision tree — and never
  left at `NOT_RUN` once a run has completed, nor set to any value before those
  conditions hold.

## 10. Prohibited Claims

- No claim of horizon reconstruction.
- No claim that PR004 (global) passes or fails.
- No order-only claim for any statistic that uses `r_p_last`, `r_q_last`, `r_mid_last`,
  `d_p_over_ell`, `d_q_over_ell`, `d_mid_over_ell`, or `r_mid_at_peel` — these are
  embedded-radius quantities. They are labeled `DIAGNOSTIC_ONLY / GROUND_TRUTH_READOUT`
  throughout this document and MUST be labeled that way in any report that uses them; the
  `kbeam` search itself remains order-only (per `dev/measure_kbeam_peeloff.py`'s existing
  protocol), but the peel-off *diagnostic* is not, and never becomes, order-only evidence.
- No reuse of the V1 CSV (`data/reports/kbeam_braiding_diagnostic_per_survivor.csv`) for
  validation of anything in this document.
- No converting this preregistration, or its future exploratory runs, into confirmatory
  evidence without a further, separately-committed sign-off that this document itself
  does not grant.
