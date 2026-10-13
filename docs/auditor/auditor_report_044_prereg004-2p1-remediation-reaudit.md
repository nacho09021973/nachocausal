# Auditor Report 044 — prereg004-2p1-remediation-reaudit

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target
- **Repo:** `~/nachocausal`, worktree `.worktrees/prereg004-step3`.
- **Branch:** `prereg004/step3-port`, at commit `c16fb12`.
- **Trigger:** re-audit after the remediation of report 043
  (`docs/auditor/auditor_report_043_prereg004-2p1-candidate-package.md`: 2 errors, 3 warnings).
- **Scope:** the same as 043. That is the comité 052 §9 step-6 scope (τ fixture SHA, hard-coded T,
  guard port, seed guard), plus the numbers in the step records.
- **Package status:** the candidate is NOT frozen. No validation seed is drawn, and no sealed
  validation path was run.

## 2. Mechanical audit
`bash .claude/skills/auditor/audit.sh`, verbatim:

```
Auditor — auditing: /home/ignac/nachocausal/.worktrees/prereg004-step3
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/PR9_INTEGRATION_2026-10-02.md,docs/archive/relatividad_875d2c3/manuscript_limits_draft.md,docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/auditor/auditor_report_015_phase1-theory-package.md,docs/auditor/auditor_report_016_phase1-provenance-reaudit.md,docs/auditor/auditor_report_017_op21-terminal-run.md,docs/auditor/auditor_report_018_op21-terminal-second-pass.md,docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md,docs/auditor/auditor_report_020_op22-bd-dossier-rev3-fix-verification.md,docs/auditor/auditor_report_021_truncated-futures-freeze-preflight.md,docs/auditor/auditor_report_022_freeze-commit-scoped-audit.md,docs/auditor/auditor_report_023_ficha-tv-order-only-precommit.md,docs/auditor/auditor_report_024_wp4-annex-c-comparable-pair-separation-precommit.md,docs/auditor/auditor_report_025_wp4-annex-c-remediation-reaudit.md,docs/auditor/auditor_report_026_wp4-annex-c-variance-addendum-precommit.md,docs/auditor/auditor_report_027_wp4-ibar-interval-design-precommit.md,docs/auditor/auditor_report_028_wp4-ibar-executable-contract-precommit.md,docs/auditor/auditor_report_031_p1a-seccion-13-certificado-familia-prescrita.md,docs/auditor/auditor_report_032_emergencia-viz-figuras-del-fracaso.md,docs/auditor/auditor_report_033_emergencia-viz-remediacion-032-reauditoria.md,docs/auditor/auditor_report_034_emergencia-viz-cierre-avisos-033.md,docs/auditor/auditor_report_035_viz-figuras-generales-6-agosto.md,docs/auditor/auditor_report_036_viz-cierre-e1-y-avisos-035.md,docs/auditor/auditor_report_037_wp6-s1-paper-and-lean-evidence.md,docs/auditor/auditor_report_038_w16-closure-verification.md,docs/auditor/auditor_report_039_wp6-s1-manuscript-v1-post-referee.md,docs/auditor/auditor_report_040_provenance-remediation-closure.md,docs/auditor/auditor_report_041_provenance-reachability-final-closure.md,docs/auditor/auditor_report_042_wp6-s1-fisher-fiber-event-and-referee-closure.md,docs/auditor/auditor_report_043_prereg004-2p1-candidate-package.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/comite/comite_decision_027_phase1-theory-package-first-review.md,docs/comite/comite_decision_028_phase1-theory-package-second-review.md,docs/comite/comite_decision_029_phase1-theory-package-third-review.md,docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md,docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md,docs/comite/comite_decision_032_phase1-theory-closure-handoff.md,docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md,docs/comite/comite_decision_034_op21-certifier-opening.md,docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md,docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md,docs/comite/comite_decision_037_candidate-b-viability-gate-review.md,docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md,docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md,docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md,docs/comite/comite_decision_045_candidate-7-1-fixed-n-logical-status.md,docs/comite/comite_decision_046_weyl-level-sheet-page-shoom-adjudication.md,docs/comite/comite_decision_047_phase2-b2-documentation-publication.md,docs/comite/comite_decision_048_q-fmots-target-adjudication.md,docs/comite/comite_decision_049_program-closure-adjudication.md,docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md,docs/comite/comite_decision_051_s1-gate-geometric-tangent-classification.md,docs/comite/comite_decision_052_prereg004-2p1-design.md,docs/foro/foro_decision_001_ef4-falsacion-adversarial.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_24_jul_2026.md,docs/hoja_de_ruta_25_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jul_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/manuscript_release_checklist.md,docs/physical_reentry_audit_001_2026-08-28.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/program_closure_note_2026-07-30.md,docs/program_reopening_note_2026-08-28_R4.md,docs/rvar_closure_negative_result.md
----------------------------------------
Auditor: 0 error(s), 0 warning(s)
```
Exit code: `0`.

## 3. Seal & freeze integrity
- **1+1 seal: unchanged.** `make verify-seal` printed
  `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- **2+1 candidate thresholds:** `make verify-2p1` printed `nachocausal2p1/thresholds.py
  e7a69934dff0219f4d3560e1f892eeb9ecf8accb5fa72996e1e0cf73f7e326eb`. It changed from `5d574b52…`,
  and the change is limited to the seed block (`git show c16fb12 -- nachocausal2p1/thresholds.py`).
  The new SHA is recorded in `dev/PREREG004_STEP_6_2026-10-13.md`.
- **τ fixture: unchanged.** It is `4bc4aec8…` and equals `TAU_FIXTURE_SHA256`
  (`nachocausal2p1/thresholds.py:116`, unchanged line). The gate still raises on a mismatch.
- **Hard-coded T:** `grep -rn "os.environ|getenv|cache=True" nachocausal2p1/` finds only the
  CPU-device check at `thresholds.py:58`.
- **Still open at C1, as in 043** (`comite_decision_052…md:352`):
  - freezing the thresholds SHA;
  - listing the SHAs of the imported 1+1 modules.

## 4. Reproducibility of published numbers
| Claim | Generator (committed in c16fb12) | Re-run now |
|---|---|---|
| Step 1: 360 decisions / 69 with n > 128 / 0 flips / min margin 0.0358 | `dev/regate_2p1_sweeps.py` | `decisions 360  n>128 69  flips 0  min_margin 0.0358` |
| Step 4 mutation table (5 mutations, each caught) | `dev/mutation_check_004.py` (mutates a temporary copy, not the repo) | `caught 5/5` |
| Step 3: 8652 / 5125 relations | `tests/test_2p1_package.py::test_port_relation_count_and_T_discrimination` | in the `28 passed` below |
| 2+1 tests | `pytest tests/test_2p1_package.py tests/test_004_criteria_can_fail.py` | `28 passed` |
| Full suite: 549 passed, 2 skipped | `pytest` (run by the remediation author before c16fb12, recorded in `dev/PREREG004_STEP_6_2026-10-13.md`) | not re-run by the auditor; the 2+1 subset was re-run |

## 5. dev/validation separation & ground-truth leakage
- **043 error 1 (Guard-v bypass): resolved.**
  - `verdict_from_levels(levels, *, guard_ran: bool)` has no default (`validate.py:195`), and
    `"v_order_only": bool(guard_ran)` (`validate.py:222`).
  - `run()` passes `guard_ran=guard` (`validate.py:260`).
  - Under `validation_004`, `guard=False` RAISES (`validate.py:242`).
  - Can fail: `test_v_guard_off_fails_v_only` (only (v) false → FAIL),
    `test_validation_label_requires_guard`, and mutation 5 of `dev/mutation_check_004.py`.
- **043 error 2 (seed guard): resolved.**
  - `check_seed()` (`validate.py:72`) is the first statement of `generate()` (`validate.py:89`), and
    `run()` checks every seed before any generation (`validate.py:237`).
  - Admitted seeds: the exploration band, or the drawn `VALIDATION_SEEDS` only when
    `STATUS == "FROZEN"`. Burned Phase-A seeds are refused explicitly
    (`thresholds.py:99`).
  - `check_validation_seeds(VALIDATION_SEEDS)` runs at import (`thresholds.py:120`). It is vacuous
    only while nothing is drawn, and it can fail: `test_check_validation_seeds_can_fail` passes 4
    bad sets, each raising.
  - The tests replace `generate` with a function that fails if called, so no virgin seed is ever
    generated (`test_run_refuses_bad_seeds_before_generation`).
  - Every entry point goes through `generate()`: `per_seed`, `dry_run`, and
    `dev/preflight_2p1.py` via `validate.generate`.
- **Leakage: unchanged from 043, which found no path.** The estimator does not import `scoring`,
  and r is revealed only after the estimate.

## 6. Claim-boundary check
- The new and changed texts are `dev/PREREG004_STEP_6_2026-10-13.md` and the docstrings in
  `validate.py`/`thresholds.py`. `grep -i "3+1|horizon|reconstru|validated"` finds no over-claim.
- The step-6 record states "No se congela nada".

## 7. Findings
| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | 043-E1 resolved: (v) reflects whether Guard-v ran, and the validation run refuses `guard=False`. Each part can fail in a test and under mutation. | `validate.py:195,222,242,260`; tests; `dev/mutation_check_004.py` |
| 2 | OK | 043-E2 resolved: a runnable seed guard runs before any generation, and virgin seeds are admitted only when drawn and FROZEN. The disjointness check against the exploration band and the burned seeds can fail. | `validate.py:72,89,237`; `thresholds.py:99,120`; tests |
| 3 | OK | 043-W3 resolved: the step-1 gate numbers have a committed generator, and it reproduces them. | `dev/regate_2p1_sweeps.py` |
| 4 | OK | 043-W4 resolved: the step-4 mutation table has a committed generator, which reports 5/5 caught. | `dev/mutation_check_004.py` |
| 5 | OK | 043-W5 resolved: the relation counts are pinned by a test. | `tests/test_2p1_package.py` |
| 6 | OK | The 1+1 seal is unchanged; the τ fixture is unchanged; T is a literal. | `make verify-seal`; `make verify-2p1`; grep |
| 7 | OK | Mechanical audit clean. | §2 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=0

## 8. Verdict
One of: `AUDIT_PASS` (no errors, no warnings), `AUDIT_PASS_WITH_WARNINGS` (no errors, ≥1 warning),
`AUDIT_FAIL` (≥1 error). Must match the counts in §7.
AUDIT_VERDICT=AUDIT_PASS
