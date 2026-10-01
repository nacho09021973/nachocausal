# Auditor Report 041 — provenance-reachability-final-closure

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repository root `/home/ignac/nachocausal`, branch `emergencia/p1a-canal-sigma-m`, commit
`db13f98a35c30abf20d3cb334d3358668d885ba7` ("Fix provenance audit reachability"). Trigger: final
narrow re-audit of the provenance remediation after report 040 returned `AUDIT_FAIL` on the
previous implementation (`b5f93b4`).

This audit targets **the code at `db13f98`**, not the remediation narrative. Every claim below is
re-derived from the script's control flow and from adversarial execution in disposable clones; no
statement is taken from the remediation commit message. WP6 S1 mathematics, manuscript claims,
Kurečka priority, Appendix E, Lean and unrelated scientific tracks were not reopened; no concrete
inconsistency in those areas surfaced.

Two commits are in scope:

```text
71051b9  Record failed provenance-remediation audit
A	docs/auditor/auditor_report_040_provenance-remediation-closure.md

db13f98  Fix provenance audit reachability
M	.claude/skills/auditor/audit.sh
M	tests/test_auditor_provenance.py
```

**Report 040 preserved unedited.** It is touched by exactly one commit in the entire history
(`git log --all -- docs/auditor/auditor_report_040_*.md` → `71051b9` only); the committed blob
carries `AUDIT_ERRORS=1`, `AUDIT_WARNINGS=3`, `AUDIT_VERDICT=AUDIT_FAIL`; and
`git diff 71051b9 db13f98 -- <that file>` is empty. The failure record stands intact.

`db13f98` touches no manuscript, Lean source, bibliography, threshold, preregistration,
`research_program/`, or data/result artifact — a pattern grep over the commit's file list returns
nothing, and none of the 23 registered artifacts appears in it. The registry itself is byte-identical
to `b5f93b4` (`git diff --stat b5f93b4 db13f98 -- provenance/committed_artifact_generators.tsv`
empty), so the fix was achieved without editing the provenance data it validates.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh`, exit code `0`; verbatim output:

```text
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/auditor/auditor_report_015_phase1-theory-package.md,docs/auditor/auditor_report_016_phase1-provenance-reaudit.md,docs/auditor/auditor_report_017_op21-terminal-run.md,docs/auditor/auditor_report_018_op21-terminal-second-pass.md,docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md,docs/auditor/auditor_report_020_op22-bd-dossier-rev3-fix-verification.md,docs/auditor/auditor_report_021_truncated-futures-freeze-preflight.md,docs/auditor/auditor_report_022_freeze-commit-scoped-audit.md,docs/auditor/auditor_report_023_ficha-tv-order-only-precommit.md,docs/auditor/auditor_report_024_wp4-annex-c-comparable-pair-separation-precommit.md,docs/auditor/auditor_report_025_wp4-annex-c-remediation-reaudit.md,docs/auditor/auditor_report_026_wp4-annex-c-variance-addendum-precommit.md,docs/auditor/auditor_report_027_wp4-ibar-interval-design-precommit.md,docs/auditor/auditor_report_028_wp4-ibar-executable-contract-precommit.md,docs/auditor/auditor_report_031_p1a-seccion-13-certificado-familia-prescrita.md,docs/auditor/auditor_report_032_emergencia-viz-figuras-del-fracaso.md,docs/auditor/auditor_report_033_emergencia-viz-remediacion-032-reauditoria.md,docs/auditor/auditor_report_034_emergencia-viz-cierre-avisos-033.md,docs/auditor/auditor_report_035_viz-figuras-generales-6-agosto.md,docs/auditor/auditor_report_036_viz-cierre-e1-y-avisos-035.md,docs/auditor/auditor_report_037_wp6-s1-paper-and-lean-evidence.md,docs/auditor/auditor_report_038_w16-closure-verification.md,docs/auditor/auditor_report_039_wp6-s1-manuscript-v1-post-referee.md,docs/auditor/auditor_report_040_provenance-remediation-closure.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/comite/comite_decision_027_phase1-theory-package-first-review.md,docs/comite/comite_decision_028_phase1-theory-package-second-review.md,docs/comite/comite_decision_029_phase1-theory-package-third-review.md,docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md,docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md,docs/comite/comite_decision_032_phase1-theory-closure-handoff.md,docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md,docs/comite/comite_decision_034_op21-certifier-opening.md,docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md,docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md,docs/comite/comite_decision_037_candidate-b-viability-gate-review.md,docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md,docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md,docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md,docs/comite/comite_decision_045_candidate-7-1-fixed-n-logical-status.md,docs/comite/comite_decision_046_weyl-level-sheet-page-shoom-adjudication.md,docs/comite/comite_decision_047_phase2-b2-documentation-publication.md,docs/comite/comite_decision_048_q-fmots-target-adjudication.md,docs/comite/comite_decision_049_program-closure-adjudication.md,docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md,docs/comite/comite_decision_051_s1-gate-geometric-tangent-classification.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_24_jul_2026.md,docs/hoja_de_ruta_25_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jul_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/manuscript_limits_draft.md,docs/physical_reentry_audit_001_2026-08-28.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/program_closure_note_2026-07-30.md,docs/program_reopening_note_2026-08-28_R4.md,docs/rvar_closure_negative_result.md
----------------------------------------
Auditor: 0 error(s), 0 warning(s)
```

`MECHANICAL_AUDIT_ERRORS=0`, `MECHANICAL_AUDIT_WARNINGS=0`. Unlike the 0/0 at `b5f93b4`, §4 below
establishes by execution that this one is produced *by the registry*.

| Command | Result |
| --- | --- |
| `bash .claude/skills/auditor/audit.sh` | exit `0` — `Auditor: 0 error(s), 0 warning(s)` |
| `make verify-seal` | exit `0` — `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` |
| `make verify-audit` | exit `0` — 39 × `AUDIT_CHECK=PASS`, 0 × `AUDIT_CHECK=FAIL` (39 reports on disk) |
| `make test` | `456 passed, 1 warning in 406.37s (0:06:46)` — 0 failed, 0 skipped |
| `git diff --check` | exit `0`, no output |

`make test` matches the handoff expectation: **456 passed, 0 failed**. The single pytest warning is
the pre-existing environmental Matplotlib `Axes3D` import warning in `tests/test_emergencia_viz.py`
— a Python runtime warning, **not** an auditor warning; the auditor's own warning count is 0.
Arithmetic check against the previous audit: 447 (report 040) − 6 removed provenance tests + 15
current provenance tests = 456, so no test was lost or silenced.

## 3. Seal & freeze integrity

`make verify-seal` prints `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, and
the mechanical audit confirms that SHA is recorded across the freeze chain
(`docs/preregistration_002.md`, `docs/preregistration_003.md`, the auditor/comité series). This is
the same `6e2c3888…` carried since report 037: **no drift**. `db13f98` does not touch
`nachocausal/thresholds.py` or any freeze record.

## 4. Reproducibility of published numbers

No numeric claim in `README.md`/`docs/` changed at `db13f98`. In scope instead is the central
question report 040 answered negatively: **is the registry actually executed?**

**Control-flow proof (structural).** Inside the artifact loop (`audit.sh:126-214`) the registry
lookup happens at `audit.sh:137-142`, before any literal reference is consulted. The only `git grep`
in the loop is at `audit.sh:197` (verified by `awk 'NR>=126 && NR<=214 && /git grep/'`, which
returns that single line). The branch structure makes bypass impossible:

- `registry_count > 1` → ERROR + `continue` (`:144-148`);
- `registry_count == 1` → full validation, each failure ERROR + `continue` (`:150-189`), and on
  success an unconditional `continue` at `:192`;
- the fallback at `:195-210` is therefore reachable **only** when `registry_count == 0`.

A declared registry row cannot be eclipsed by a literal filename match.

**Execution proof (behavioural), in disposable `git clone -s` checkouts at `db13f98`, deleted
afterwards; the project tree was never modified:**

| # | Setup | Result |
| --- | --- | --- |
| 1 | normal registry | `0 error(s), 0 warning(s)` |
| 2 | registry removed | `0 error(s), **23 warning(s)**` — 23 `WARN` lines |
| 3 | all 23 anchors → `git:0…0` | **`23 error(s)`**, 0 warnings — 23 `ERROR` lines |
| 4 | one row anchored to `git:71051b9…` (a real commit that does not touch that artifact) | **`1 error(s)`** — `anchor commit does not introduce or modify the artifact` |
| 5 | one row anchored `hg:abc123` | **`1 error(s)`** — `unsupported provenance anchor: hg:abc123` |

Experiment 2 proves all 23 depend on the registry (nothing else clears them); experiment 3 proves
all 23 execute the anchor-validation branch. **HISTORICAL_ROWS_REACHED = 23/23**, against 0/23 at
`b5f93b4`. The live 0/0 is earned.

**W-4 (unchanged and correctly bounded).** `PROVENANCE_CONFIRMED = 23/23` — every row has a tracked
generator and a `git:` anchor whose commit provably touches the artifact.
`EXACT_COMMANDS_DOCUMENTED = 21/23`; two rows remain `NOT_DOCUMENTED`
(`data/reports/kbeam_braiding_diagnostic_per_survivor.csv`,
`evidence/new_geometry_20260719/mink_control_metrics.csv`). No command was invented, the registry
was not edited, and provenance is not being presented as bit-for-bit reproducibility.
`tests/test_auditor_provenance.py:test_provenance_confirmed_is_distinct_from_reproduction_command_documented`
pins the distinction and additionally asserts that each of the 21 documented commands invokes its
own registered generator.

## 5. dev/validation separation & ground-truth leakage

`db13f98` touches only audit tooling and its tests. No threshold, seed band, sealed estimator path
or validation code is affected; the registry references `dev/` scripts only as provenance metadata
and creates no execution path from `dev/` into the sealed estimator. No embedding/ground-truth
access is introduced. The provenance tests build throwaway `git init` repositories under pytest
`tmp_path` and never write to the project tree. **No separation or leakage defect found.**

**W-17 remains CLOSED.** Main worktree `/home/ignac/nachocausal` is clean at `db13f98`; the WIP work
remains preserved separately on `wip/wp6-3plus1` in
`/home/ignac/nachocausal-wip-wp6-3plus1`, clean, local HEAD `908e2cb…` equal to
`origin/wip/wp6-3plus1`, with both `dev/OCCUPANCY_GENERATING_SYSTEM_3plus1.md` and
`research_program/work_packages/wp6_full_class_sum_rank_theorem.md` present. No WIP content entered
either audited commit.

## 6. Claim-boundary check

No claim text changed at `db13f98`. The commit is engineering-only and asserts nothing about 1+1D
localisation, metric reconstruction, asymptotic horizons or 3+1D. Unlike `b5f93b4` — whose message
claimed a provenance-awareness the code did not deliver — the `db13f98` message's technical claims
were re-verified against the code and hold. **No claim-boundary violation found.**

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | **WARN** | **`*_test.ipynb` is not barred from the literal fallback**, a narrow deviation from the specified `*_test.*` exclusion. The guard enumerates six extensions — `*_test.py|*_test.sh|*_test.js|*_test.ts|*_test.go|*_test.rs` — but `.ipynb` is inside the fallback's own search set (`audit.sh:198`), so a notebook named `*_test.ipynb` satisfies the fallback. Measured directly: a fixture whose sole reference is `spoof_test.ipynb` clears the audit (`0 warnings`) where `spoof_test.py` correctly warns. No such file exists in the repository today and no artifact currently rides the fallback (§4 experiment 2), so this is residual spoof surface, not a live false pass. | `.claude/skills/auditor/audit.sh:121`, `:198`; fixture probe (§7 note) |
| 2 | **WARN** | **Three further plausible test-infrastructure paths are not barred**: root-level `conftest.py` (pytest's canonical configuration file), a singular `test/` directory, and `mytests/`. Each was measured to clear the audit as the sole reference for an artifact. The specified list (`tests/**`, `test_*`, `*_test.*`, `.claude/**`, `docs/**`, `provenance/**`) does not name them, so this is a hardening gap rather than a spec violation — but `conftest.py` in particular is unambiguously test infrastructure and would spoof the fallback. | `.claude/skills/auditor/audit.sh:112-124`; fixture probe (§7 note) |
| 3 | **WARN** | **No regression test pins the exclusion list.** The suite covers the six specified exclusions only through two cases (`tests/…` and `docs/…`); none of the four bypasses in findings 1–2 is tested, and no test asserts the membership of `is_generator_candidate`'s deny-list. The list is therefore free to narrow silently — the same class of drift that produced the 040 failure, one level up. | `tests/test_auditor_provenance.py:test_deleted_registry_warns_even_though_basename_is_in_tests`, `:test_docs_and_auditor_paths_cannot_satisfy_the_fallback` |
| 4 | OK | **Registry precedence holds structurally and behaviourally.** Registry lookup at `audit.sh:137-142` precedes the loop's only `git grep` at `:197`; a validated row exits at `:192`; the fallback is reachable only when `registry_count == 0`. | `audit.sh:126-214`; `awk 'NR>=126 && NR<=214 && /git grep/'` |
| 5 | OK | **All 23 historical rows execute the registry validation path** — 0/23 at `b5f93b4`, 23/23 here. Registry removed → exactly 23 warnings; all anchors bogus → exactly 23 errors. | §4 experiments 2–3 |
| 6 | OK | The five required adversarial real-repo checks all behave as specified: `0/0`; 23 warnings; 23 errors; non-touching real anchor → ERROR; unsupported scheme → ERROR. | §4 table |
| 7 | OK | **All six specified fallback exclusions are enforced.** Measured individually: `tests/test_x.py`, `tests/helper.py`, `pkg/tests/x.py`, `test_spoof.py`, `spoof_test.py`, `spoof_test.sh`, `.claude/x.sh`, `docs/x.py`, `provenance/x.py` each fail to satisfy the fallback and produce the `WARN`. | fixture probe (§7 note) |
| 8 | OK | **The legitimate fallback is preserved**: `dev/real_generator.py` and `Makefile` naming an artifact still clear it without a registry row, so the historical mechanism survives for genuine generator code. | fixture probe (§7 note) |
| 9 | OK | **Tests genuinely exercise `audit.sh`**: 12 of 15 invoke the script against fixture repositories; the 3 that do not are content assertions about the registry and the W-4 distinction, not substitutes for behavioural coverage. All ten required failure modes are covered behaviourally — test-only spoof, reachability despite a tests mention, missing registry, malformed row, duplicate row, missing/untracked generator, invalid anchor, non-touching real anchor, unsupported scheme, legitimate fallback. | `tests/test_auditor_provenance.py`; per-test `_audit(` scan |
| 10 | OK | Fixtures deliberately reproduce the 040 trap: `HISTORICAL_ARTIFACTS` still lists all 23 basenames in the test file, and `mention_in_tests` plants the basename inside `tests/…` in the fixture repo, so the original defect cannot return silently. | `tests/test_auditor_provenance.py:17-45`, `_init_fixture` |
| 11 | OK | Report 040 preserved unedited as historical evidence: one commit only (`71051b9`), `AUDIT_VERDICT=AUDIT_FAIL` intact, zero diff to HEAD. | `git log --all --`; `git diff 71051b9 db13f98 --` |
| 12 | OK | Commit scope clean: `db13f98` changes only `audit.sh` and its test file; no manuscript, Lean, bibliography, threshold, or data artifact; the registry is byte-identical to `b5f93b4`. | `git show --name-status db13f98`; `git diff --stat b5f93b4 db13f98 -- provenance/…` |
| 13 | OK | W-4 correctly bounded: `PROVENANCE_CONFIRMED=23/23`, `EXACT_COMMANDS_DOCUMENTED=21/23`; no command invented; the distinction is pinned by a test. | `provenance/committed_artifact_generators.tsv`; `test_provenance_confirmed_is_distinct_from_reproduction_command_documented` |
| 14 | OK | Seal intact (`6e2c3888…`), `make verify-audit` 39/39, `make test` 456 passed / 0 failed, `git diff --check` clean, W-17 closed with WIP preserved on `wip/wp6-3plus1` at `908e2cb…`. | §2, §5 |

**Note — fixture probes.** Findings 1, 2, 7 and 8 were measured with a disposable `git init`
repository containing one artifact `data/reports/target_artifact.csv` and exactly one file naming
its basename, rebuilt per path under the session scratchpad and deleted afterwards. A path is
"blocked" when the audit still emits the provenance `WARN`. Results: blocked — `tests/test_x.py`,
`tests/helper.py`, `pkg/tests/x.py`, `test_spoof.py`, `spoof_test.py`, `spoof_test.sh`,
`.claude/x.sh`, `docs/x.py`, `provenance/x.py`; **not blocked** — `spoof_test.ipynb`,
`conftest.py`, `test/x.py`, `mytests/x.py`; intentionally not blocked (legitimate) —
`dev/real_generator.py`, `Makefile`.

AUDIT_ERRORS=0
AUDIT_WARNINGS=3

## 8. Verdict

The defect report 040 recorded is closed, and closed on the evidence rather than on assertion. The
registry is now consulted before any literal fallback — provable from control flow and confirmed by
execution — and all 23 historical rows genuinely run the validation path, against 0 of 23 before.
Removing the registry restores exactly 23 warnings, corrupting every anchor produces exactly 23
errors, and a real-but-non-touching anchor and an unsupported scheme each error. The six specified
fallback exclusions are enforced while the legitimate generator fallback still works, twelve of
fifteen tests drive the script itself across all ten required failure modes, report 040 stands
unedited, the seal is intact, the suite is green at 456, and W-17 remains closed with the WIP work
preserved on its own branch.

Three warnings remain, all in the same place: the fallback deny-list is narrower than it reads.
`*_test.ipynb` escapes the specified `*_test.*` rule outright, and `conftest.py`, `test/` and
`mytests/` escape it in spirit; no test pins the list, so it can narrow again without anyone
noticing. None is a live false pass — no such file exists here and no artifact currently rides the
fallback — so these do not reopen the closure. They are the next hardening step, and remediation is
the user's call.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
