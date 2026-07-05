# R-VAR EGS-object falsification test — measurement report

Follow-up to `docs/comite/comite_decision_021_rvar-egs-truncation-object.md` §5/§9 step 1 (the
falsifier's mandatory minimal falsification test, adopted before any candidate-object spec is
treated as more than a draft). Scope discipline: dev seeds only (`20240617/13/101`, the exact
three draws already consumed by `dev/measure_pr003_rvar_structure_probe.py`, commit `6347459` —
**zero new seed consumption**), MINK + BH, the 4 frozen production intensities, read-only against
the sealed generator. No μ computed, no spec frozen, no `EXPLORE_POOL`/`VALIDATION_SEEDS`, no
threshold frozen, no reconstruction claim.

Artifact: `dev/measure_pr003_rvar_egs_falsification_test.py` →
`dev/rvar_egs_falsification_test_result.json`.

## What was measured

For every minimal element `i ∈ Min(C)`, order-only (no coordinate enters either statistic):

- `L(i)` — length (edges) of the longest chain starting at `i`, via the exact DAG-longest-path
  recursion over the full transitively-closed relation (PRIMARY candidate, comité 021 §8).
- `future_card(i) = |future(i)|` — the sealed `O_min(i)` restricted to `i ∈ Min(C)` (SECONDARY /
  diagnostic candidate, `NON_CORROBORATION`-tagged per comité 021 §8).

`r` is used **only** as a post-hoc diagnostic label to split BH minimals into interior
(`r<R_S`)/exterior for the scaling check — never as input to either statistic (`NO_GROUND_TRUTH_LEAKAGE`).

## Finding 1 — the MINK null is quasi-degenerate on THIS box geometry (falsifier failure mode 1, CONFIRMED)

`L` and `future_card` coefficients of variation across `Min(C)`, all 4 intensities, all 3 dev
seeds:

| Intensity | L_cv range (MINK) | future_card_cv range (MINK) |
| --- | --- | --- |
| 1500 | 0.013 – 0.022 | 0.012 – 0.024 |
| 3000 | 0.006 – 0.008 | 0.017 – 0.018 |
| 6000 | 0.007 – 0.015 | 0.017 – 0.018 |
| 12000 | 0.008 – 0.009 | 0.014 – 0.016 |

Every MINK draw, at every intensity, both variants: **CV ≈ 0.006–0.024** — essentially every
minimal element has nearly identical longest-chain length and nearly identical future
cardinality. Contrast with BH, same statistics, same draws: **CV ≈ 0.72–1.01** (40–100× larger).

This is exactly the mechanism the falsifier predicted (`comite_decision_021_...md` §5, failure
mode 1): the frozen tall-box aspect ratio (`R_EDGE=1.2 ≪ T_EDGE=6`, `nachocausal/thresholds.py:37-38`)
that already certified `𝒜(C)=∅` for MINK 12/12 (`6347459`) makes every MINK minimal's future
cover nearly the whole set — so both graded statistics collapse to a near-delta spike rather than
EGS's "varies between n and √n" spread, which the literature verifier (comité 021 §7) confirmed is
textually scoped to a **causal diamond**, not this project's box. **The transfer failure the
falsifier warned about is empirically realized**, not merely a citation-scope worry.

This directly overturns the wave-1 physicist's reading (comité 021 §4) that MINK non-degeneracy
follows from physical necessity ("no singularity ⇒ unimodal contrast is the signal") — the null is
not merely unimodal, it is a near-point-mass, structurally the same character of degeneracy that
made Part F's μ-calibration vacuous (comité 020), just manifested as near-zero-variance instead of
a literal empty set.

No accept/reject numeric floor was pre-frozen (freezing one now, after seeing these numbers, would
itself be `NO_POST_HOC_TUNING`) — but a 40–100× separation between the MINK and BH coefficients of
variation is not a borderline read.

## Finding 2 — BH interior/exterior separation is real and strong; occupancy SCALES with n_min (falsifier failure mode 2, test PASSES)

Cohen's-d effect size between BH exterior and interior `L` values, all draws: **d ≈ 5.9–9.2** — an
extremely large, consistent separation (same order for `future_card`). This is strong evidence
that whatever the calibration-null problem above, the BH signal itself is genuine and well
separated, not noise.

Interior occupancy (`r<R_S`) vs `n_min` across the four frozen intensities (pooled example, seed
`20240617`): `n_interior` = 10 → 12 → 19 → 30 as `n_min` = 21 → 32 → 49 → 73. Interior fraction
stays roughly stable (≈0.37–0.52) across all three seeds and four intensities, and **`n_interior`
grows with `n_min`** rather than staying constant. This is the opposite signature from the prior
`𝒜(C)`-object's corner artifact (`|D*|≈N−few, B∈{3..8}` independent of N, comité 020 §4) — this
check does **not** flag a corner artifact.

(Observed fraction ≈0.4–0.5 runs a bit above the naive geometric prediction
`(R_S−0.1)/R_EDGE ≈ 0.333` — plausible finite-`n_min` effect, not investigated further here; not a
disqualifying finding.)

## Reading against comité 021 §9 step 3

The next-step spec conditioned step 3 (spec-commit) on this test's result: *"if step 1 fails
(degenerate MINK null or non-scaling BH occupancy), this step becomes a negative-result commit
instead... never a redesign-and-retry on the same dev seeds."*

**Check (b) (corner-artifact/scaling) PASSES cleanly.** **Check (a) (MINK non-degeneracy) shows a
strong, consistent, large-magnitude failure signature** — not a formal Gate-0 FAIL (no threshold
was frozen to fail against), but the empirical picture the falsifier's test was designed to
surface. This is a PI-level decision point, not something to resolve unilaterally: whether to (i)
proceed treating this as the pre-committed negative-closure trigger for the height/cardinality
object as currently defined, (ii) consider a geometry-normalized or different order-only statistic
(a genuinely new object, requiring its own committee question — not a tuning of this one on these
same seeds), or (iii) something else the PI specifies.

Provenance: git commit, numpy version (`1.26.4`, asserted), uname, and UTC timestamp are recorded
in `dev/rvar_egs_falsification_test_result.json` (closing reproducibility-engineer Risk 5, comité
021 §4).
