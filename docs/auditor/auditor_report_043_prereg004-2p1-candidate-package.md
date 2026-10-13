# Auditor Report 043 — prereg004-2p1-candidate-package

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target
- **Repo:** `~/nachocausal`, worktree `.worktrees/prereg004-step3`.
- **Branch:** `prereg004/step3-port`, at commit `27f3c74`. The base is `main` `1dbae26`, which
  equals `origin/main` after `git fetch`.
- **Trigger:** comité 052 §9, step 6 (`docs/comite/comite_decision_052_prereg004-2p1-design.md:472`),
  requested by the PI. Scope named there: the τ fixture SHA, the hard-coded T, the guard port and
  the seed guard.
- **Also covered:** the numbers stated in the step 1–5 records (`dev/PREREG004_STEP*_2026-10-13.md`)
  and the README 2+1 status lines.
- **Package status:** the candidate is NOT frozen (`STATUS = "CANDIDATE_NOT_FROZEN"`) and no
  validation seed is drawn.
- **No sealed validation path was run.** Every check that touched seeds used only `DRY_RUN_SEEDS`.

## 2. Mechanical audit
`bash .claude/skills/auditor/audit.sh`, verbatim:

```
Auditor — auditing: /home/ignac/nachocausal/.worktrees/prereg004-step3
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/PR9_INTEGRATION_2026-10-02.md,docs/archive/relatividad_875d2c3/manuscript_limits_draft.md,docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/auditor/auditor_report_015_phase1-theory-package.md,docs/auditor/auditor_report_016_phase1-provenance-reaudit.md,docs/auditor/auditor_report_017_op21-terminal-run.md,docs/auditor/auditor_report_018_op21-terminal-second-pass.md,docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md,docs/auditor/auditor_report_020_op22-bd-dossier-rev3-fix-verification.md,docs/auditor/auditor_report_021_truncated-futures-freeze-preflight.md,docs/auditor/auditor_report_022_freeze-commit-scoped-audit.md,docs/auditor/auditor_report_023_ficha-tv-order-only-precommit.md,docs/auditor/auditor_report_024_wp4-annex-c-comparable-pair-separation-precommit.md,docs/auditor/auditor_report_025_wp4-annex-c-remediation-reaudit.md,docs/auditor/auditor_report_026_wp4-annex-c-variance-addendum-precommit.md,docs/auditor/auditor_report_027_wp4-ibar-interval-design-precommit.md,docs/auditor/auditor_report_028_wp4-ibar-executable-contract-precommit.md,docs/auditor/auditor_report_031_p1a-seccion-13-certificado-familia-prescrita.md,docs/auditor/auditor_report_032_emergencia-viz-figuras-del-fracaso.md,docs/auditor/auditor_report_033_emergencia-viz-remediacion-032-reauditoria.md,docs/auditor/auditor_report_034_emergencia-viz-cierre-avisos-033.md,docs/auditor/auditor_report_035_viz-figuras-generales-6-agosto.md,docs/auditor/auditor_report_036_viz-cierre-e1-y-avisos-035.md,docs/auditor/auditor_report_037_wp6-s1-paper-and-lean-evidence.md,docs/auditor/auditor_report_038_w16-closure-verification.md,docs/auditor/auditor_report_039_wp6-s1-manuscript-v1-post-referee.md,docs/auditor/auditor_report_040_provenance-remediation-closure.md,docs/auditor/auditor_report_041_provenance-reachability-final-closure.md,docs/auditor/auditor_report_042_wp6-s1-fisher-fiber-event-and-referee-closure.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/comite/comite_decision_027_phase1-theory-package-first-review.md,docs/comite/comite_decision_028_phase1-theory-package-second-review.md,docs/comite/comite_decision_029_phase1-theory-package-third-review.md,docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md,docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md,docs/comite/comite_decision_032_phase1-theory-closure-handoff.md,docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md,docs/comite/comite_decision_034_op21-certifier-opening.md,docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md,docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md,docs/comite/comite_decision_037_candidate-b-viability-gate-review.md,docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md,docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md,docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md,docs/comite/comite_decision_045_candidate-7-1-fixed-n-logical-status.md,docs/comite/comite_decision_046_weyl-level-sheet-page-shoom-adjudication.md,docs/comite/comite_decision_047_phase2-b2-documentation-publication.md,docs/comite/comite_decision_048_q-fmots-target-adjudication.md,docs/comite/comite_decision_049_program-closure-adjudication.md,docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md,docs/comite/comite_decision_051_s1-gate-geometric-tangent-classification.md,docs/comite/comite_decision_052_prereg004-2p1-design.md,docs/foro/foro_decision_001_ef4-falsacion-adversarial.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_24_jul_2026.md,docs/hoja_de_ruta_25_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jul_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/manuscript_release_checklist.md,docs/physical_reentry_audit_001_2026-08-28.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/program_closure_note_2026-07-30.md,docs/program_reopening_note_2026-08-28_R4.md,docs/rvar_closure_negative_result.md
----------------------------------------
Auditor: 0 error(s), 0 warning(s)
```
Exit code: `0`.

## 3. Seal & freeze integrity
- **1+1 seal: unchanged.**
  - `make verify-seal` printed `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
  - That is the SHA named in `docs/preregistration_002.md`, which `audit.sh` lists among the
    records holding it.
- **2+1 candidate:** `make verify-2p1` printed
  - `nachocausal2p1/thresholds.py 5d574b52…`;
  - `nachocausal2p1/fixtures/tau_table_2p1.json 4bc4aec8…`.
- **τ fixture: matches.**
  - `sha256sum` gives `4bc4aec839257af7…` for both `nachocausal2p1/fixtures/tau_table_2p1.json`
    and `dev/tau_table_2p1_candidate_2026-10-13.json`.
  - That value equals `TAU_FIXTURE_SHA256` (`nachocausal2p1/thresholds.py:116`).
  - The gate RAISES on a SHA mismatch (`nachocausal2p1/gate.py:30-31`), on parameter drift
    (`gate.py:38`) and for n outside [2, 256] (`gate.py:47`).
  - `tests/test_2p1_package.py::test_tau_fixture_sha_and_prefix` checks n ≤ 128 against the sealed
    table.
- **Hard-coded T: confirmed.**
  - `grep -rn "os.environ|getenv|NC2P1_T_EDGE|cache=True" nachocausal2p1/` finds two hits only.
    One is the docstring at `generator.py:5`. The other is the device check at `thresholds.py:58`,
    which rejects a non-CPU device.
  - `generator.T_EDGE = _th.T_EDGE` (`generator.py:25`).
- **Nothing is frozen yet, as expected before C1:**
  - the candidate thresholds SHA `5d574b52…` is not recorded in any `docs/` or `dev/` file;
  - the SHAs of the imported 1+1 modules (estimator and gate) are not listed anywhere.

  The comité requires both at C1 (`comite_decision_052…md:352`), so neither is a finding at this
  stage.

## 4. Reproducibility of published numbers
| Claim | Where | Generator | Re-derived now |
|---|---|---|---|
| Re-gating the dev sweeps with the new τ: 360 decisions, 69 with n > 128, 0 flips, min margin 0.0358 | `dev/PREREG004_STEPS_1_2_2026-10-13.md:21-24` | **none committed**: `dev/gen_tau_table_2p1.py` has no decision or margin code (grep) | Yes, by an inspection one-liner over both v2 sweeps and the fixture: `decisions 360 n>128 69 flips 0 min_margin 0.0358` |
| Port vs dev: 8652 relations at T = 16, 5125 at T = 6 (seed 7000100, n = 150) | `dev/PREREG004_STEP_3_2026-10-13.md` | the test asserts hash equality only; the counts come from an inspection command | Yes: `port T=16 relations 8652`, `dev T=6 relations 5125` |
| Step-4 mutation table (4 mutations, each caught) | `dev/PREREG004_STEP_4_2026-10-13.md`, "Comprobación por mutación" | **none committed**: produced by `sed -i` plus `git checkout` in the shell | No (not re-run: it would edit `validate.py`) |
| Step 4: 9 passed; suite 543 passed, 2 skipped | `dev/PREREG004_STEP_4_2026-10-13.md` | `pytest` | Partly: `tests/test_2p1_package.py` plus `tests/test_004_criteria_can_fail.py` → `22 passed` |
| Step 5: "> 22.5 min per realisation on this PC" | `dev/PREREG004_STEP_5_2026-10-13.md` | an observation of a stopped run, with no output | Not reproducible by design; it is stated as an observation |

## 5. dev/validation separation & ground-truth leakage
- **The package does not import dev code.**
  - `grep "import.*dev|sys.path|dev/" nachocausal2p1/` finds docstrings and comments only.
  - Imports: `estimator.py:19-21` (sealed `nachocausal.estimator`, local `gate`) and
    `gate.py:14-20`.
- **The estimator never sees r.**
  - The estimator does not import `scoring` (`test_estimator_and_gate_do_not_import_scoring`).
  - Its source has no coordinate tokens (`test_estimator_source_is_coordinate_free`).
  - `validate.per_seed` estimates both kinds before calling `blind_bracket` (`validate.py:113-121`).
- **The Guard-v port can fail in a test** (`test_guard_v_can_fail`).
- **But Guard-v can be turned off in the blind run while (v) still reports PASS.**
  - `run(..., guard: bool = True, ...)` (`validate.py:212`) passes `guard` down to `per_seed` and
    `estimator.estimate`.
  - The validation-label check (`validate.py:217-223`) refuses a wrong STATUS, wrong seeds or an
    existing file, but not `guard=False`.
  - The verdict hard-codes `"v_order_only": True` (`validate.py:204`).
  - So `run(label="validation_004", guard=False)` after freeze would report (v) as passed without
    running the guard. **ERROR.**
- **Seed guard: absent where the comité requires it.**
  - `comite_decision_052…md:353` asks for "a runnable disjointness guard against EXPLORE_BAND …
    and the burned Phase-A seeds 1,2,3,4,7,99,12345", and says that no virgin seed may be touched
    during a dry run.
  - The only seed asserts (`nachocausal2p1/thresholds.py:98-100`) check `VALIDATION_SEEDS`, which
    is currently `()`, so they pass vacuously.
  - `run()` with any label other than `validation_004` accepts any seed list (`validate.py:212-233`;
    read from code, NOT executed). A run with virgin-band seeds `8_000_000..8_999_999` would
    therefore burn them silently.
  - `nachocausal2p1/dry_run.py:16` and `dev/preflight_2p1.py` restrict themselves to
    `DRY_RUN_SEEDS`, but the library entry point does not. **ERROR.**
- **CPU-only:** `run()` calls `thresholds.assert_environment()` first (`validate.py:213`).
  `test_environment_assertion_can_fail` covers it.
- **Step 4 vs leakage (c):** the step-4 record itself discloses that a mutation run showed (ii)
  false at T = 8 also through localisation, and that the value was not inspected.
  - That is a θ–width comparison at T = 8, which is out of domain (`T_EDGE_MIN = 10`) and not the
    candidate configuration.
  - The disclosure is adequate. No θ–width comparison at T = 16 was found in the code or the
    records.

## 6. Claim-boundary check
- `grep -i "3+1|horizon|horizonte|reconstru|einstein|regular"` over
  `dev/PREREG004_STEP_[345]_2026-10-13.md` and `nachocausal2p1/*.py` finds no hits.
- The README 2+1 status ends: "**Nothing is frozen or validated yet**, and the virgin band
  `8_000_000..8_999_999` is untouched." (`README.md`, 2+1 front section).
- No over-claim was found.

## 7. Findings
| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | ERROR | Guard-v can be disabled in the one-shot validation run (`guard=False` is not refused) while the verdict hard-codes `v_order_only: True`. Criterion (v) cannot fail. | `nachocausal2p1/validate.py:204`, `:212`, `:217-223` |
| 2 | ERROR | There is no runnable seed guard in the package. Seed lists for non-validation labels are unchecked, so virgin-band seeds could be burned silently. The comité-required disjointness guard against EXPLORE_BAND and the burned Phase-A seeds is absent, and the `thresholds.py` asserts are vacuous while `VALIDATION_SEEDS = ()`. | `nachocausal2p1/validate.py:212-233`; `nachocausal2p1/thresholds.py:98-100`; `comite_decision_052…md:353` |
| 3 | WARN | Step-1 gate-decision numbers (360 / 69 / 0 flips / 0.0358) have no committed generator. They re-derive exactly by an inspection command. | `dev/PREREG004_STEPS_1_2_2026-10-13.md:21-24`; `dev/gen_tau_table_2p1.py` |
| 4 | WARN | The step-4 mutation table was produced by uncommitted shell edits (`sed -i` + `git checkout`), and no script reproduces it. | `dev/PREREG004_STEP_4_2026-10-13.md` ("Comprobación por mutación") |
| 5 | WARN | The step-3 relation counts (8652 / 5125) come from an inspection command, and the test asserts hashes only. They re-derive exactly. | `dev/PREREG004_STEP_3_2026-10-13.md`; `tests/test_2p1_package.py:45-59` |
| 6 | OK | The 1+1 seal is unchanged (`6e2c3888…`). | `make verify-seal` |
| 7 | OK | The τ fixture SHA matches the step-1 candidate and `TAU_FIXTURE_SHA256`. The gate raises on a SHA mismatch, parameter drift and n > 256. | `thresholds.py:116`; `gate.py:30-47` |
| 8 | OK | T is a literal: there is no env knob and the numba cache is off. | grep (§3); `generator.py:25` |
| 9 | OK | The estimator is order-only and isolated from `scoring`. Guard-v can fail in a test. r is revealed only after the estimate. | `estimator.py:19-21`; `validate.py:113-121`; tests |
| 10 | OK | The CPU-only assertion is enforced at `run()`. | `validate.py:213`; `thresholds.py:58` |
| 11 | OK | No claim-boundary over-claim was found. | §6 grep |
| 12 | OK | The 2+1 tests pass. | `pytest tests/test_2p1_package.py tests/test_004_criteria_can_fail.py` → `22 passed` |

AUDIT_ERRORS=2
AUDIT_WARNINGS=3

## 8. Verdict
One of: `AUDIT_PASS` (no errors, no warnings), `AUDIT_PASS_WITH_WARNINGS` (no errors, ≥1 warning),
`AUDIT_FAIL` (≥1 error). Must match the counts in §7.
AUDIT_VERDICT=AUDIT_FAIL
