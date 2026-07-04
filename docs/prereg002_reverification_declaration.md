# Pre-registration 002 — SUPERVISED_REVERIFICATION launch declaration

Status: **PREPARATORY DOCUMENT ONLY. NO LAUNCH HAS OCCURRED.**

This document is Next-step-spec item 1 of `docs/comite/comite_decision_016_prereg002-supervised-reverification.md`
(§9, "Reversible steps ... may be done now if the user asks; no launch, no
seeds consumed"). Committing this file does **not** authorise the launch in
§3 of that spec. The launch remains a separate, committing step gated by
explicit user (PI) authorisation, taken only after this declaration is
committed.

## 0. What this is not

**This exercise cannot recreate the lost primary blind PASS artifact.**

The original blind evaluation — `python -m nachocausal.validate` executed
once on 2026-06-22, raw output `results/validation.json`, transcribed into
`docs/preregistration_002_result.md` (commit `fee12d5`) — happened once and
its raw artifact is gone (`docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md`,
`AUDIT_VERDICT=AUDIT_FAIL`; second machine unavailable, PI determination
2026-07-04, `results/README.md`). No rerun, however faithful, produces that
missing artifact. A rerun produces a **new**, distinct artifact: evidence
*about* the transcription's fidelity, not a substitute for the original run.

**The result of the future run will be reported as `SUPERVISED_REVERIFICATION_MATCH`
or `SUPERVISED_REVERIFICATION_MISMATCH` — never as a recovered original PASS,
never as "the blind evaluation," never as "confirmed by re-running the
validation."** The phrase "First and only evaluation of the held-out band"
(`docs/preregistration_002_result.md:12`) refers exclusively to the
historical 2026-06-22 event, whose primary artifact is lost; it is not
re-instantiated by anything described here.

Any future reader encountering artifacts, commits, or prose produced by this
declaration MUST be able to tell, from the label alone, that they are looking
at a reverification of a transcription, not the original blind run.

## 1. Purpose

Verify, by deterministic replay, that the transcription committed at
`fee12d5` (`docs/preregistration_002_result.md`) is the actual output of the
sealed instrument on the sealed inputs — i.e. decide the proposition

```
M := transcription(fee12d5) == validate.run() at commit 573cfcb / thresholds sha 6e2c3888...
```

This is **verification of transcription fidelity**, not a second evaluation
(`docs/comite/comite_decision_016...md` §4, mathematical-logic brief; §6,
"formally, what changed is not the evaluation ... but who has audited it").
The committee's construction (§8, disagreement 1) is recorded here again for
the avoidance of doubt: this decision explicitly construes the *purpose* of
`docs/preregistration_002.md:61-63` ("launched once ... the only evaluation")
over its plain *letter*, and owns that construction rather than claiming the
letter is silent. This is a one-time, committee-authorised construction, not
a precedent for reading any other freeze down to its enumerated prohibitions.

## 2. Publish-either-way

MATCH, MISMATCH, crash, and abort are recorded and reported **alike**, with
equal reporting force, mirroring `docs/preregistration_002.md`'s binding rule
("the outcome ... is recorded and reported regardless of which it is").
Concretely, whichever of the following cells obtains is written to the
result note in the same commit shape, with no cell suppressed or softened
relative to another:

- `SUPERVISED_REVERIFICATION_MATCH`
- `SUPERVISED_REVERIFICATION_MISMATCH` (transcription retracted; rerun's own
  verdict reported alongside, whatever it is — see §3)
- crash / abort during the run (reported as such; not silently retried)

No party may choose, after seeing the outcome, to report only a favourable
cell or to omit the launch from the record. The launch, once it occurs, is
disclosed unconditionally.

## 3. Comparison predicate P (mechanical, fixed before launch)

`P` compares the rerun's output, printed at the record's own precision
(round-half-even), field-by-field against `docs/preregistration_002_result.md`:

- **Exact-equality fields** (discrete, k/20 grid or boolean): the verdict
  token (`PASS`/`FAIL`/`INCONCLUSIVE`/`OUT_OF_DOMAIN`); the six boolean
  checks (`i_significant_primary_and_above_3000`, `ii_localisation_primary`,
  `ii_convergence_slack`, `iii_stability_primary`, `iv_false_positive_primary`,
  `v_order_only`); `n_valid`; `fp` (`fp_fraction`); `coverage` (`coverage_frac`);
  abstain fractions (BH/MINK) — all of these live on a `k/20` denominator
  (`n_valid = 20`, `nachocausal/thresholds.py:71`) and must match exactly.
- **Printed-precision fields** (continuous floats: `p_perm`, `med|dr|/2M`,
  `θ_loc`, `θ_stab`, `r_std`, `N̄`): equality is evaluated at the number of
  significant digits the transcription itself prints
  (`docs/preregistration_002_result.md`'s per-level table), round-half-even.
  No wider tolerance may be introduced after the rerun exists.

**Outcome rule:** ANY field mismatch under the above ⟹
`SUPERVISED_REVERIFICATION_MISMATCH`. On mismatch, the `fee12d5` record is
retracted **as a transcription** (it is no longer treated as a faithful
record of a validate.run() output); the rerun's own verdict is reported
under the label `REVERIFICATION_RUN_RESULT=<PASS|FAIL|INCONCLUSIVE|OUT_OF_DOMAIN>`
(whatever it is), and prereg-002's status becomes
`RETRACTED_TRANSCRIPTION [REVERIFICATION_RUN_RESULT=<...>]`.

**The "mismatch-but-PASS" cell can NEVER be reported as "PASS confirmed."**
A rerun that itself yields PASS while disagreeing with even one transcribed
field is a `MISMATCH` in full, exactly as defined above — not a near-match,
not "PASS confirmed with a typo." This is fixed now, before any rerun exists,
precisely so it cannot be softened after the fact
(`docs/comite/comite_decision_016...md` §5, falsifier mode 4).

**No machine-drift excuse is admissible.** Cross-machine bit-identity is
analytically well-supported (pure numpy, PCG64, no BLAS/matmul on the sealed
path) but empirically `[UNVERIFIED]` (comité 016 §4, reproducibility brief).
This machine's rerun is definitive for the `M`-claim regardless: "the other
machine would have drifted" is not an admissible excuse for a mismatch on
*this* machine's own rerun.

## 4. Float-drift / partial-match rule

This is folded into §3: printed-precision, round-half-even comparison for
continuous fields, exact comparison for discrete/boolean fields, fixed
**before** the replay is launched. No tolerance wider than the transcription's
own printed precision may be adopted at any point after the rerun's numbers
are known. If a genuine platform-level float perturbation is ever observed,
it is reported as a MISMATCH under this predicate, not adjudicated away.

## 5. Author/verifier separation

Full disjointness of author and verifier is not achievable here: the
operator, the machine, the AI assistant, and the transcription's original
author coincide, and every possible verifier already knows the target
numbers (comité 016 §5, falsifier; §8, disagreement 3). The adopted
substitute, per the committee's resolution, is **mechanical, not personal**:

- The comparison predicate `P` (§3) is committed in writing, in this
  document, **before** the launch — it is executed by script/checklist
  against the rerun's output, not adjudicated by post-hoc judgment.
- All raw artifacts, checksums, and provenance from the rerun are committed
  (per §7) so that a **future third party**, who is genuinely disjoint from
  every party involved today, can independently re-check the predicate.
- The word "SUPERVISED" in `SUPERVISED_REVERIFICATION` denotes this
  mechanical-predicate-plus-committed-evidence regime. It does not connote,
  and must never be read as implying, the presence of a second human
  verifier at launch time.

## 6. Leakage quarantine

- Per-seed logs (seed, N, `sep_BH`, `sep_MINK`, abstain flags, bracket) are
  captured for self-corroboration but stay in the git-ignored
  `results/prereg002_reverification/` directory — never committed in full.
- Only checksums (`SHA256SUMS`) and level-aggregate fields (the same schema
  already used for the archived prereg-001 FAIL: verdict, checks, per-level
  aggregate table) are committed to a tracked path.
- The virgin band `VALIDATION_SEEDS` (`nachocausal/thresholds.py:66-70`,
  seeds `2076703`…`2983811`) is declared **permanently burned** for any
  future protocol comparison, dev calibration, or selector design —
  including R-VAR (`dev/PR003_R_VAR_SELECTOR_SPEC_V2.md`, currently paused
  pending this decision closing).
- A fresh virgin band ("prereg-002b" on new seeds ≥ 3,000,000) is recorded
  as **forbidden forever** as an escape hatch from a MISMATCH or a
  non-auditable PASS: drawing new seeds after seeing an outcome is exactly
  the "re-running on fresh seeds after seeing a result" prohibition
  (`docs/preregistration_002.md`, binding rules).
- The reverification opens no new estimator-side path: the embedding scores
  exactly as sealed (`nachocausal/validate.py:22` imports only
  `scoring.blind_bracket`; unchanged between `573cfcb` and HEAD). No ground
  truth is exposed to any selector as a result of this exercise.

## 7. Output routing (pre-declared; no mid-run improvisation)

Fixed now, to be executed verbatim at launch time with no on-the-fly
deviation:

1. **Before launch:** compute and commit `sha256sum results/prereg001/*`
   (the archived prereg-001 FAIL raw artifacts — currently the *only*
   surviving raw artifact corroborating any published verdict,
   `docs/auditor/auditor_report_005...md` §4) so that evidence survives the
   rerun regardless of what the invocation does.
2. **Launch:** the unmodified sealed entrypoint, `python -m nachocausal.validate`
   (`nachocausal/validate.py:225-233`; `run()` called with defaults —
   `seeds=None` → `VALIDATION_SEEDS`, `label="validation"`, `guard=True`,
   `write=True`, `nachocausal/validate.py:154-155`). No `seeds=`, no
   `guard=False`, no threshold or code edit.
3. This writes `results/validation.json` as designed (`_write`,
   `nachocausal/validate.py:217-222`).
4. **Immediately post-run:** the file is **copied** (not moved) to
   `results/prereg002_reverification/validation_SUPERVISED_REVERIFICATION_<date>.json`.
5. `results/validation.json` is then **removed** so no stale pointer
   survives that could later be mistaken for either the prereg-001 FAIL or
   the lost prereg-002 PASS raw output.
6. Run log (full stdout/stderr) and a provenance snapshot are captured
   alongside, using the same schema the prereg-001 FAIL run recorded
   (`results/prereg001/validation_provenance_launch.txt`): `captured_utc`,
   `start_utc`, `finish_utc`, `elapsed`, full commit sha, `git status
   --porcelain` (must be clean on the sealed path), `thresholds_sha256`
   before and after (`make verify-seal`), `uname -a`, `python --version`,
   full `pip freeze`, `make test` result, `NACHOCAUSAL_MINZ_PATH` /
   `OMP_NUM_THREADS` state.
7. `SHA256SUMS` of every output file (the copied JSON, the run log, the
   provenance file, plus the pre-launch `results/prereg001/*` checksums from
   step 1) is committed to a tracked companion note alongside this
   declaration.

**Environment:** detached checkout of `573cfcb` (the commit the PASS record
names, `docs/preregistration_002_result.md:11`) — the sealed subset is
byte-identical to HEAD `abf90f0` (`git diff --stat 573cfcb..HEAD --
nachocausal/` shows only two additive, unimported files:
`nachocausal/c1_selector.py`, `nachocausal/selection_guard.py`; verified this
session, sha256 `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
re-confirmed at both commits) — sealed venv `numpy==1.26.4`
(`nachocausal/thresholds.py:18`, `assert_environment()` at :21-30, called at
`validate.py:157`). `make verify-seal` must be run and must print the SHA
above, both immediately before and immediately after the launch.

## 8. Wall-time rule

Rerun duration is recorded in the provenance snapshot but **adjudicates
nothing** about the original host or about auditor 005 WARN 2 (the 13m14s
seal→PASS-record window implausible for this machine's ~30-70 min expected
runtime). That finding remains open regardless of this rerun's outcome or
duration.

## 9. Label discipline (binding, permanent)

- On MATCH: prereg-002's status becomes
  `PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]`.
  Never bare `"PASS"`. Never "confirmed by re-running the blind evaluation."
  The `TRANSCRIPTION_REVERIFIED` tag denotes that `M` (transcription =
  sealed-function output) was verified by replay. The
  `BLINDNESS_DOCUMENTARY_ONLY` tag denotes that the historical claim `H`
  (that an original blind run occurred as described, unshopped) rests solely
  on the git timeline (single introduction of `VALIDATION_DRAW_SEED` at
  `573cfcb`, no alternate value anywhere in git history — falsification test
  already executed, comité 016 §5) plus a probabilistic-plausibility
  argument (the `p_perm` floor at exactly `2^-20` at all four levels), and
  is explicitly **not** verified by this replay. Replay is constitutionally
  blind to off-git seed-shopping on the now-unavailable second machine.
- On MISMATCH: per §3, `RETRACTED_TRANSCRIPTION [REVERIFICATION_RUN_RESULT=<...>]`.
- `docs/preregistration_002_result.md` receives an annotation, in the same
  commit as this declaration's companion result note, clarifying that
  "First and only evaluation of the held-out band" (line 12) refers to the
  historical 2026-06-22 event whose primary artifact is lost, and pointing
  to this declaration and its outcome record.
- The `RE-`/`SUPERVISED_REVERIFICATION` prefix is permanent and non-optional
  in every future reference to this exercise's outcome, in any document.

## 10. Gate: launch requires explicit user authorisation

Nothing in this document authorises execution. Per
`docs/comite/comite_decision_016...md` §9 item 3, the launch
(`python -m nachocausal.validate` under the routing in §7) is a **committing
step** and may proceed **only** after:

1. This declaration is committed to a tracked path.
2. `sha256sum results/prereg001/*` is computed and committed (§7 step 1).
3. The user (PI) gives **explicit** authorisation for the launch itself, as
   a separate act from authorising this document.

Until then: no seeds are consumed, no validation code path is executed, and
no output under `results/prereg002_reverification/` exists.

## 11. Provenance of this document

- Prepared per `docs/comite/comite_decision_016_prereg002-supervised-reverification.md`
  §9 item 1 (reversible step), 2026-07-04.
- Seal re-checked while drafting: `make verify-seal` →
  `nachocausal/thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
  — matches `docs/preregistration_002.md:8`.
- `git rev-parse HEAD` at drafting time: `abf90f0b0f06435e78f4a1121f42a1424feb8693`.
- No `python -m nachocausal.validate` invocation, no seed consumption, no
  write under `results/` occurred in the preparation of this document.
- Optional `make test` (§9 item 2 of comité 016's next-step spec) was
  attempted in this session and could not run: the interactive shell's
  `python3` has no `pytest`/`numpy` installed, and no sealed venv pinned to
  `numpy==1.26.4` was found on this machine at drafting time (only
  `~/venvs/torch-gpu` exists, unrelated). This touches no validation output
  either way; `make test` remains outstanding and should be run, in the
  correct sealed venv, as part of §7's pre-launch checklist, with its result
  recorded in the provenance snapshot at launch time.
