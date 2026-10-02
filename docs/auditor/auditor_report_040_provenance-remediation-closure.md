# Auditor Report 040 — provenance-remediation-closure

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repository root `/home/ignac/nachocausal`, branch `emergencia/p1a-canal-sigma-m`, commit
`b5f93b4e5973e53b41194a1a80b55895257cda0f` ("Make auditor provenance-aware for generated
artifacts"). Trigger: narrow **closure audit** of the historical 23 "committed data file with no
generator reference" warnings carried in reports 037–039, and of **W-17** (worktree hygiene).

Scope discipline applied as instructed: the WP6 S1 manuscript mathematics, the Kurečka priority
analysis, Appendix E and the Lean development were **not** reopened. No concrete inconsistency in
those areas surfaced during this audit, so none was pursued. This audit is confined to the
remediation mechanism, its tests, and worktree state.

Commit scope verified (`git show --name-status --format="" b5f93b4`), exactly three files:

```text
M	.claude/skills/auditor/audit.sh
A	provenance/committed_artifact_generators.tsv
A	tests/test_auditor_provenance.py
```

No manuscript, Lean source, bibliography, threshold, historical CSV/data artifact, or scientific
result file is touched. `nachocausal/thresholds.py` appears zero times in the commit's file list.
`provenance/committed_artifact_generators.tsv` is audit metadata, not a scientific data artifact,
and `audit.sh` explicitly skips it in its own scan (`audit.sh:109`).

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh`, exit code `0`; verbatim output:

```text
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/auditor/auditor_report_015_phase1-theory-package.md,docs/auditor/auditor_report_016_phase1-provenance-reaudit.md,docs/auditor/auditor_report_017_op21-terminal-run.md,docs/auditor/auditor_report_018_op21-terminal-second-pass.md,docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md,docs/auditor/auditor_report_020_op22-bd-dossier-rev3-fix-verification.md,docs/auditor/auditor_report_021_truncated-futures-freeze-preflight.md,docs/auditor/auditor_report_022_freeze-commit-scoped-audit.md,docs/auditor/auditor_report_023_ficha-tv-order-only-precommit.md,docs/auditor/auditor_report_024_wp4-annex-c-comparable-pair-separation-precommit.md,docs/auditor/auditor_report_025_wp4-annex-c-remediation-reaudit.md,docs/auditor/auditor_report_026_wp4-annex-c-variance-addendum-precommit.md,docs/auditor/auditor_report_027_wp4-ibar-interval-design-precommit.md,docs/auditor/auditor_report_028_wp4-ibar-executable-contract-precommit.md,docs/auditor/auditor_report_031_p1a-seccion-13-certificado-familia-prescrita.md,docs/auditor/auditor_report_032_emergencia-viz-figuras-del-fracaso.md,docs/auditor/auditor_report_033_emergencia-viz-remediacion-032-reauditoria.md,docs/auditor/auditor_report_034_emergencia-viz-cierre-avisos-033.md,docs/auditor/auditor_report_035_viz-figuras-generales-6-agosto.md,docs/auditor/auditor_report_036_viz-cierre-e1-y-avisos-035.md,docs/auditor/auditor_report_037_wp6-s1-paper-and-lean-evidence.md,docs/auditor/auditor_report_038_w16-closure-verification.md,docs/auditor/auditor_report_039_wp6-s1-manuscript-v1-post-referee.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/comite/comite_decision_027_phase1-theory-package-first-review.md,docs/comite/comite_decision_028_phase1-theory-package-second-review.md,docs/comite/comite_decision_029_phase1-theory-package-third-review.md,docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md,docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md,docs/comite/comite_decision_032_phase1-theory-closure-handoff.md,docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md,docs/comite/comite_decision_034_op21-certifier-opening.md,docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md,docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md,docs/comite/comite_decision_037_candidate-b-viability-gate-review.md,docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md,docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md,docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md,docs/comite/comite_decision_045_candidate-7-1-fixed-n-logical-status.md,docs/comite/comite_decision_046_weyl-level-sheet-page-shoom-adjudication.md,docs/comite/comite_decision_047_phase2-b2-documentation-publication.md,docs/comite/comite_decision_048_q-fmots-target-adjudication.md,docs/comite/comite_decision_049_program-closure-adjudication.md,docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md,docs/comite/comite_decision_051_s1-gate-geometric-tangent-classification.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_24_jul_2026.md,docs/hoja_de_ruta_25_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jul_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/manuscript_limits_draft.md,docs/physical_reentry_audit_001_2026-08-28.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/program_closure_note_2026-07-30.md,docs/program_reopening_note_2026-08-28_R4.md,docs/rvar_closure_negative_result.md
----------------------------------------
Auditor: 0 error(s), 0 warning(s)
```

`MECHANICAL_AUDIT_ERRORS=0`, `MECHANICAL_AUDIT_WARNINGS=0`. The 23 historical warnings recorded in
report 039 §2 no longer appear. **§7 finding 1 establishes that this 0/0 is not produced by the
provenance registry**, and therefore does not by itself evidence provenance verification.

Companion mandatory checks:

| Command | Result |
| --- | --- |
| `bash .claude/skills/auditor/audit.sh` | exit `0` — `Auditor: 0 error(s), 0 warning(s)` |
| `make verify-seal` | exit `0` — `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` |
| `make verify-audit` | exit `0` — 38 × `AUDIT_CHECK=PASS`, 0 × `AUDIT_CHECK=FAIL` |
| `make test` | `447 passed, 1 warning in 405.54s (0:06:45)` — 0 failed, 0 skipped |
| `git diff --check` | exit `0`, no output |

`make test` matches the remediation handoff expectation exactly: **447 passed, 0 failed, 0
skipped**. The single pytest warning is the pre-existing environmental Matplotlib `Axes3D` import
warning raised in `tests/test_emergencia_viz.py`; it is a Python runtime warning and is **not** an
auditor warning — the auditor's own warning count is 0. Report 039 recorded `441 passed`; the new
`tests/test_auditor_provenance.py` contributes exactly 6 test functions, so 441 + 6 = 447 is
consistent with no test having been lost or silenced.

Existing auditor reports: **38 files**, numbered `001`–`028` and `030`–`039`; `029` is absent.
`make verify-audit` emits 38 `AUDIT_CHECK=PASS` lines, i.e. it validates every existing report.
The count is 38, not 39 — the highest number (039) exceeds the file count because of the 029 gap.

## 3. Seal & freeze integrity

`make verify-seal` prints
`6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`. The mechanical audit
independently confirms this live SHA256 of `nachocausal/thresholds.py` is recorded across the
freeze/report chain (`docs/preregistration_002.md`, `docs/preregistration_003.md`, and the
auditor/comité report series). This is the same seal `6e2c3888…` carried in reports 037–039: **no
drift**. Commit `b5f93b4` does not touch `nachocausal/thresholds.py` or any freeze record, so the
seal could not have been perturbed by this remediation.

## 4. Reproducibility of published numbers

Out of scope for this narrow closure audit (no numeric claim in `README.md`/`docs/` changed at
`b5f93b4`). What *is* in scope is the provenance registry's own reproducibility content, audited
directly and independently of `audit.sh`:

| Property | Method | Result |
| --- | --- | --- |
| Artifact rows | `awk 'NR>1 && NF' \| wc -l` | **23** |
| Duplicate `artifact_path` | `awk … \| sort \| uniq -d` | **0** |
| Rows with ≠ 4 fields | `awk -F'\t' 'NF!=4'` | **0** |
| Empty/blank fields | `awk` per-field blank scan | **0** |
| Orphan artifacts (registry row whose artifact is untracked) | `git ls-files --error-unmatch` per row | **0** |
| Missing/untracked generators | `[ -f ]` + `git ls-files --error-unmatch` over the 4 distinct generators | **0** |
| Invalid anchors (bad format or nonexistent commit) | `grep -Eq '^[0-9a-f]{40}$'` + `git cat-file -e` | **0** |
| Anchors that do **not** introduce/modify their artifact | `git diff-tree --root --no-commit-id --name-only -r <anchor> -- <artifact>` | **0** |

All four distinct generators (`dev/measure_kbeam_peeloff.py`,
`dev/pr011_tv_certification_enumeration.py`, `dev/present_anchor_sanity_pilot.py`,
`dev/run_new_geometry_future_observables.py`) exist and are tracked — consistent with `CLAUDE.md`,
under which `dev/explore_*`-style exploration **scripts** are committed as scoped exceptions.

Two rows carry `command_or_template = NOT_DOCUMENTED` (see §7 finding 4): the registry names a
generator and a valid anchor for them but no re-runnable command, so those two artifacts are not
reproducible from the registry alone.

## 5. dev/validation separation & ground-truth leakage

No change at `b5f93b4` touches the sealed estimator path, any threshold, any seed band, or any
validation code. The registry references `dev/` scripts only as *provenance metadata* for
already-committed historical artifacts; it creates no execution path from `dev/` into the sealed
estimator. No ground-truth/embedding access is introduced. `tests/test_auditor_provenance.py`
builds throwaway `git init` fixture repositories under pytest `tmp_path` and never writes to the
project tree. **No separation or leakage defect found.**

Worktree hygiene (**W-17**, defined in report 038 §7 row 14 as: modified
`research_program/work_packages/wp6_full_class_sum_rank_theorem.md`, untracked
`dev/OCCUPANCY_GENERATING_SYSTEM_3plus1.md`, plus untracked reports 037/038):

- Main worktree `/home/ignac/nachocausal` — `git status --short` **empty (clean)**, HEAD
  `b5f93b4e5973e53b41194a1a80b55895257cda0f`, branch `emergencia/p1a-canal-sigma-m`.
- The two prior WIP files are preserved in the separate worktree
  `/home/ignac/nachocausal-wip-wp6-3plus1` on branch `wip/wp6-3plus1`, HEAD
  `908e2cb75d509b3f210ece0e4fc211d3ef9bbc34` ("Backup WP6 and 3plus1 work in progress",
  2 files changed, 465 insertions), that worktree also clean.
- No WIP content entered this remediation: `dev/OCCUPANCY_GENERATING_SYSTEM_3plus1.md` is absent
  and untracked in the main worktree, and the 23-line WP6 addition exists only on `wip/wp6-3plus1`
  (`git diff --stat b5f93b4 908e2cb -- research_program/work_packages/wp6_full_class_sum_rank_theorem.md`
  → `23 ++`).

**W-17 is CLOSED without loss of work.**

## 6. Claim-boundary check

No claim text changed at `b5f93b4`. The commit message ("Make auditor provenance-aware for
generated artifacts") is an engineering statement, not a scientific claim, and asserts nothing
about 1+1D localisation, metric reconstruction, asymptotic horizons, or 3+1D. The registry records
provenance only and promotes no threshold, no PASS, and no result. **No claim-boundary violation
found.**

One accuracy caveat belonging here rather than to the science: the commit's *stated* effect —
making the auditor provenance-aware — is **not** what the deployed script does at HEAD (§7 finding
1). The overstatement is about tooling, not about a physical or mathematical claim.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | **ERROR** | **The provenance registry is unreachable dead code at HEAD, so the 23 warnings were silenced by a filename mention, not by provenance verification.** `tests/test_auditor_provenance.py:17-41` hardcodes all 23 artifact paths in the `HISTORICAL_ARTIFACTS` literal. The pre-existing literal check `git grep -q -- "$base" -- '*.py' …` (`audit.sh:111`) therefore matches every one of the 23 in that test file and `continue`s **before** any registry logic runs. Measured: of the 57 scanned data files, **0 reach the registry code path**, and the test file is the **sole** code-type reference for all 23. Proven by controlled experiment in an isolated `git clone -s` at `b5f93b4`: deleting `provenance/committed_artifact_generators.tsv` entirely still yields `Auditor: 0 error(s), 0 warning(s)`; rewriting **every** anchor to the bogus commit `git:000…0` also still yields `0 error(s), 0 warning(s)`. A guardrail that cannot fail is decoration. | `tests/test_auditor_provenance.py:17-41`; `.claude/skills/auditor/audit.sh:111`; clone experiments A/B (§7 note) |
| 2 | **WARN** | **Three of the seven required failure modes have no regression test**, and they include the strongest check in the mechanism: (a) malformed rows — field count ≠ 4 or an empty field (`audit.sh:135-142`); (b) invalid or unsupported provenance anchors — bad hex format, nonexistent commit, or a non-`git:` scheme (`audit.sh:154-158, 168-171`); (c) **git anchors that do not introduce or modify the artifact** (`audit.sh:160-165`). The invalid-registry-header ERROR path (`audit.sh:94-100`) is likewise untested. I verified all of these behave correctly today by direct experiment (corrupting all anchors with the test file removed produced exactly 23 `ERROR: … invalid git commit anchor` and exit 1), so the code is sound — but nothing locks it against regression. | `tests/test_auditor_provenance.py:135-171`; `.claude/skills/auditor/audit.sh:94-100,135-142,154-171` |
| 3 | **WARN** | **The tests never exercise the real repository's audit behaviour**, which is why finding 1 escaped notice. Every behavioural test runs `_audit(repo)` against a synthetic `tmp_path` fixture whose stub `tests/test_fixture.py` does not name the artifacts (`tests/test_auditor_provenance.py:78-81`), so the literal-grep short-circuit never fires there and the registry path is always reached. The two tests that do read the real registry (`:118`, `:127`) assert only its *contents*, never `audit.sh`'s behaviour on this repo. No test would fail if the registry were deleted from the working tree. | `tests/test_auditor_provenance.py:53-59,78-81,118-133` |
| 4 | **WARN** | **Two of the 23 rows document no re-runnable command**, recording `NOT_DOCUMENTED` in the `command_or_template` field: `data/reports/kbeam_braiding_diagnostic_per_survivor.csv` ("parameterized probe output; artifact records K=64") and `evidence/new_geometry_20260719/mink_control_metrics.csv` ("metric_row over frozen MINK seed/intensity grid; exact MINK-only shell command absent"). The label is honest and the schema check passes (the field is non-empty), but provenance for these two artifacts stops at generator + anchor and is not reproducible from the registry alone. | `provenance/committed_artifact_generators.tsv:2,24` |
| 5 | OK | Registry structure is exactly as claimed: 23 artifact rows, 0 duplicates, 0 malformed rows, 0 empty fields, 0 orphan artifacts, 0 missing/untracked generators, 0 invalid anchors, and every anchor commit genuinely introduces or modifies its named artifact — each verified by an independent command, not by trusting `audit.sh`. | §4 table |
| 6 | OK | The registry logic **is not a blind whitelist by design**. With the literal-grep short-circuit removed (test file absent), corrupting every anchor produces 23 `ERROR` lines and exit 1; deleting the registry restores exactly the 23 historical `WARN` lines. Registered artifacts are re-verified against git reality on every run — when the code is reached. | Clone experiments D/E (§7 note) |
| 7 | OK | Commit scope is exactly the three declared files; no manuscript, Lean, bibliography, threshold, historical data artifact, or scientific result file changed. | `git show --name-status --format="" b5f93b4` |
| 8 | OK | Seal intact and undrifted: `6e2c3888…`, recorded in the freeze chain; not touched by `b5f93b4`. | `make verify-seal`; §2 mechanical output |
| 9 | OK | `make test` → 447 passed, 0 failed, 0 skipped; consistent with 441 (report 039) + 6 new tests. The 1 pytest warning is the pre-existing Matplotlib `Axes3D` environmental warning, distinct from the auditor's 0 warnings. | `make test` |
| 10 | OK | `make verify-audit` validates all 38 existing reports (38 PASS / 0 FAIL); numbering `001`–`028`, `030`–`039` with `029` absent. | `make verify-audit`; `ls docs/auditor/` |
| 11 | OK | **W-17 closed without loss of work**: main worktree clean at `b5f93b4`; both WIP files preserved on `wip/wp6-3plus1` at `908e2cb`; no WIP content committed into the remediation. | `git status --short`; `git worktree list`; `git diff --stat b5f93b4 908e2cb` |
| 12 | OK | `git diff --check` clean (exit 0, no whitespace defects). | `git diff --check` |

**Note — controlled experiments.** All four experiments ran in a throwaway `git clone -s
/home/ignac/nachocausal` checked out at `b5f93b4` under the session scratchpad, then deleted. The
project tree was never modified; `git status --short` in the main worktree is empty before and
after, HEAD unchanged at `b5f93b4`.

| Exp | Setup | `audit.sh` result |
| --- | --- | --- |
| A | registry **deleted**, test file present (= HEAD) | `0 error(s), 0 warning(s)` |
| B | **every anchor** rewritten to `git:000…0`, test file present | `0 error(s), 0 warning(s)` |
| C | registry intact, test file **removed** | `0 error(s), 0 warning(s)` |
| D | every anchor bogus, test file **removed** | **`23 error(s)`, 0 warning(s)**, exit 1 |
| E | registry **deleted**, test file **removed** | `0 error(s), **23 warning(s)**` |

A and B are the proof of finding 1: with the test file in place the registry's content is
irrelevant to the outcome. D and E are the proof of finding 6: when reached, the mechanism
enforces and the historical 23 are exactly the set at stake.

AUDIT_ERRORS=1
AUDIT_WARNINGS=3

## 8. Verdict

The remediation is well-built but mis-wired. The registry is complete and truthful (finding 5) and
its verification logic is genuinely adversarial rather than a whitelist (finding 6); the commit is
correctly scoped, the seal is intact, the suite is green at 447, and W-17 is closed with the WIP
work safely preserved on its own branch. But the mechanism does not run: the test file's own list
of the 23 filenames satisfies the older, weaker literal-reference check first, so provenance
awareness is bypassed for every artifact in the repository, and `audit.sh`'s 0/0 at HEAD is not
evidence that provenance was verified. Any future committed data artifact can be silenced the same
way — by naming it in any Python file. That is an unearned 0/0, and it is reported as an error
rather than reclassified to reach a clean result.

The defect is one of ordering/reachability, not of logic, and is repairable without weakening
anything — e.g. consult the registry **before** the literal-grep shortcut, or exclude `tests/` from
the shortcut's search scope — but remediation is the user's call, not the auditor's.

AUDIT_VERDICT=AUDIT_FAIL
