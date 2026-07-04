# Pre-registration 002 — SUPERVISED_REVERIFICATION result: **MATCH**

Governed by `docs/prereg002_reverification_declaration.md` (comité 016 step 1) and
`docs/comite/comite_decision_016_prereg002-supervised-reverification.md` (comité 016 step 3,
user-authorised 2026-07-04). Full provenance and raw output live in the git-ignored
`results/prereg002_reverification/` (checksummed below); this note is the tracked, durable record.

**This is not a recovery of the lost primary blind PASS artifact and must never be read as one.**
It is a deterministic replay of the sealed instrument on the same frozen seeds, compared
field-by-field against the committed transcription (`docs/preregistration_002_result.md`, commit
`fee12d5`).

## Outcome

`SUPERVISED_REVERIFICATION_MATCH` — every field checked by predicate `P` (declaration §3) matches
the transcription exactly, at the transcription's own printed precision, round-half-even. No
tolerance beyond that precision was used or needed: no field showed any drift.

## Predicate P — full field-by-field result

Compared against `docs/preregistration_002_result.md`'s per-level table (N̄ rounded to nearest
int; p_perm/med|dr|/2M/θ_loc/r_std/θ_stab at 3 decimals or the record's own sig-figs; fp/coverage/
abstain at 2 decimals — all as printed in the record):

| λ | N̄ | n_valid | p_perm | sig | med\|dr\|/2M | θ_loc | loc | coverage | r_std | θ_stab | stab | fp | fp_ok | abstain BH/MINK | Field match |
|---:|---:|:--:|---:|:--:|---:|---:|:--:|:--:|---:|---:|:--:|---:|:--:|:--:|:--:|
| 1500 | 1518 | 20 | 9.54e-07 | True | 0.172 | 0.277 | True | 0.95 | 0.022 | 0.139 | True | 0.00 | True | 0.00/1.00 | MATCH (all cells) |
| 3000 | 3026 | 20 | 9.54e-07 | True | 0.137 | 0.196 | True | 0.85 | 0.019 | 0.098 | True | 0.05 | True | 0.00/0.95 | MATCH (all cells) |
| 6000 | 6037 | 20 | 9.54e-07 | True | 0.072 | 0.139 | True | 0.85 | 0.013 | 0.069 | True | 0.10 | **False** | 0.00/0.90 | MATCH (all cells, incl. the flagged non-primary fp_ok=False) |
| **12000** (primary) | 12052 | 20 | 9.54e-07 | True | 0.064 | 0.098 | True | 0.95 | 0.008 | 0.049 | True | 0.00 | True | 0.00/1.00 | MATCH (all cells) |

Six frozen checks (`nachocausal/validate.py:198-206`):

| Check | Transcription | Rerun | Match |
|---|:--:|:--:|:--:|
| i_significant_primary_and_above_3000 | True | True | MATCH |
| ii_localisation_primary | True | True | MATCH |
| ii_convergence_slack | True | True | MATCH |
| iii_stability_primary | True | True | MATCH |
| iv_false_positive_primary | True | True | MATCH |
| v_order_only | True | True | MATCH |
| **verdict** | **PASS** | **PASS** | **MATCH** |

Seeds: rerun's 20 seeds (`2076703, 2110290, ..., 2983811`) are byte-identical to
`nachocausal/thresholds.py:66-70` `VALIDATION_SEEDS`. `t_edge = 6.0` in both. `n_valid = 20/20` at
every level in both.

**No field, at any level, showed any discrepancy.** The mismatch-but-PASS trap (declaration §3) is
moot: there is no mismatch of any kind to adjudicate.

## What this MATCH does and does not establish

- **Establishes (M):** the transcription at `fee12d5` is the actual output of the sealed
  `validate.run()` on commit `573cfcb` / thresholds sha `6e2c3888…`, run on the frozen
  `VALIDATION_SEEDS`. This is the strongest available guarantee that the published PASS numbers
  are real, not fabricated or mistranscribed.
- **Does not establish (H):** that the original blind run occurred exactly as described on
  2026-06-22, or that its seeds were not shopped off-git on the now-unavailable second machine.
  Replay is constitutionally blind to input provenance — a shopped PASS would replay as a perfect
  MATCH too. The only support for H is documentary: `VALIDATION_DRAW_SEED` has a single
  introduction in git history at `573cfcb` with no alternate value ever present (falsification
  test executed, comité 016 §5), plus the analytic implausibility of the exact `2^-20` p_perm floor
  recurring at all four levels under a shopped null. This is probabilistic comfort, not
  verification, and is reported as such.
- **Does not restore** the primary raw artifact. `results/prereg002/` remains empty; the original
  `results/validation.json` from 2026-06-22 is still lost. This rerun's raw output is a *new*,
  distinct artifact (`results/prereg002_reverification/validation_SUPERVISED_REVERIFICATION_2026-07-04.json`),
  never to be presented as the recovered original.
- **Does not widen** the scientific claim. The bounded claim (order-only localisation of `r=2M` in
  a finite 1+1D EF patch, `t_edge=6`; not metric reconstruction, not the global event horizon, not
  3+1D/Kerr/manifoldlikeness) is unchanged — this exercise verifies backing, not scope.

## Updated status label (binding, per declaration §9)

**prereg-002 status: `PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]`.**

Never bare "PASS." Never "confirmed by re-running the blind evaluation." The `RE-`/
`SUPERVISED_REVERIFICATION` prefix is permanent in all future references to this exercise.

## Provenance & checksums

Raw run output, full run log, and provenance snapshot are in the git-ignored
`results/prereg002_reverification/` (per-seed granularity was never emitted by the sealed
instrument in the first place — `validate.run()`'s output contains level aggregates only, so there
is no separate per-seed file to quarantine beyond what is already in the checksummed JSON below).

```
$ cat results/prereg002_reverification/SHA256SUMS
cc11d1100765ae3b8337349c73fe672bee47699776f88a677f651a1fccc7e32f  results/prereg001/validation.json
1c8078bb69bfec3d4e4f113278098a6222d4c9e452c9e6078977fa30e7a32bc9  results/prereg001/validation_provenance_launch.txt
2d698e36afa3c4144d4f56c3eec923bb94188334510f6d287d7592b29e04442b  results/prereg001/validation_run.log

ded75ad7748a6cbff2f1c413dcbd09a7116de9ba363db754997d5bb8ab201595  validation_SUPERVISED_REVERIFICATION_2026-07-04.json
356a371c8f96aaaa2020669818065d5059a7a3e83b379192f7a7cfa0656708d6  reverification_run.log
9a19ef6b3720e5e0a415e22d7c52e4ff76b06aaa31bcd16186e12723a017001e  reverification_provenance.txt
```

The `results/prereg001/*` checksums were computed and recorded **before** launch (declaration §7
step 1), confirming the last surviving raw artifact from the earlier FAIL run was preserved intact
through this exercise.

- Seal: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, verified before and
  after the run, matches `docs/preregistration_002.md:8`.
- Commit at launch: `f08bc04` (sealed subset byte-identical to `573cfcb` — only additive, unimported
  `nachocausal/c1_selector.py` / `nachocausal/selection_guard.py` differ; see
  `results/prereg002_reverification/reverification_provenance.txt` for the full environment
  snapshot, deviation note on running from HEAD rather than a detached `573cfcb` checkout, `pip
  freeze`, `uname`, and timing).
- Elapsed: 2:36.93 wall clock (2026-07-04T07:45:56Z → 07:48:33Z). Per declaration §8 this
  adjudicates nothing about auditor 005 WARN 2 (the original 13m14s seal→PASS-record gap); it is
  recorded only.
- Environment: sealed `.venv`, `numpy==1.26.4`, `pytest==8.4.2`, Python 3.12.3 — rebuilt this
  session after the pre-existing `.venv` was found non-functional (no `pyvenv.cfg`, no working
  `pip`). `make test`: 28 passed, 289.88s, immediately prior to launch.

## Leakage quarantine

The virgin band `VALIDATION_SEEDS` (`nachocausal/thresholds.py:66-70`) is declared permanently
burned for any future protocol comparison, dev calibration, or selector design, per declaration §6.
A fresh virgin band ("prereg-002b") remains forbidden forever as an escape hatch. R-VAR v2
(`dev/PR003_R_VAR_SELECTOR_SPEC_V2.md`) was paused pending this decision; this MATCH closes the
prereg-002 audit question but does **not** itself authorise resuming R-VAR — that remains subject
to comité 015's `RECOMMEND_REVISE_AND_RECONVENE` and its own open items (F1-F3, the V.1 completion
class, etc.).
