# Auditor Report 013 — OP-0.1 survival matrix

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Scoped gate for `docs/plan_operativo_15_julio_2026.md` OP-0.1. The audited candidate is
`research_program/synthesis/survival_matrix_1p1_to_3p1.md`, authored against source snapshot
`726c8c1eda16334a1b30b9f4ad82927f0c834382` on branch `main`.

The gate asks only whether all seven constructs have all nine rubric cells, whether each cell has
a real `file:line` anchor or an honest `NO_ESPECIFICABLE`, whether every row can fail, and whether
the transfer verdicts remain inside the no-code/no-simulation/no-3+1D-claim boundary. It does not
audit the whole scientific history of PR011/PR012 anew and does not authorize OP-0.2 or Fase 1.

## 2. Mechanical audit

Command: `bash .claude/skills/auditor/audit.sh`

Exit code: `0`

```text
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/rvar_closure_negative_result.md
WARN: committed data file with no generator reference: data/reports/kbeam_braiding_diagnostic_per_survivor.csv
WARN: committed data file with no generator reference: data/reports/pr004_braiding_v2_per_lineage.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K16.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K2.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K32.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K4.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K64.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K8.csv
WARN: committed data file with no generator reference: data/reports/pr005_population_depth_barrier_slices.csv
WARN: committed data file with no generator reference: data/reports/pr005_population_depth_barrier_slices_heldout.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n4.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n4.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n5.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n5.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n6.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n6.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n7.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n7.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n8.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n8.sha256
WARN: committed data file with no generator reference: data/reports/present_anchor_clean_v3_kill_test.csv
WARN: committed data file with no generator reference: data/reports/present_anchor_sanity_pilot.csv
----------------------------------------
Auditor: 0 error(s), 22 warning(s)
```

The warnings are repo-level heuristic findings predating OP-0.1. They do not invalidate the
matrix, but this report counts them exactly as required by the auditor contract.

## 3. Seal & freeze integrity

- `make verify-seal` exited `0` and printed
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- The same full hash is frozen in `docs/preregistration_002.md:8`.
- OP-0.1 changed no seal, threshold, preregistration or result artifact. At audit time
  `git status --short --branch` listed only the untracked survival matrix.

Seal verdict: `OK_NO_DRIFT`.

## 4. Reproducibility of published numbers

The candidate matrix publishes no new numerical scientific output. Its numeric references are
scope identifiers or already-recorded design values: seven constructs by nine axes, the PR011
ladder `{4,...,8}`, PR012's fixed `n=8`, and the named scalar pair. The matrix points back to the
frozen/draft sources rather than restating uncertified computations
(`survival_matrix_1p1_to_3p1.md:41-51`, `:87-102`, `:122-154`).

Checks performed:

- row-count command returned `63`;
- anchor parser returned `ANCHORS=63 ERRORS=0`;
- each of the nine negative terminals occurred exactly seven times;
- `make test` completed successfully using the target declared at `Makefile:9-10`;
- `data/reports/pr012_tv_curve_n8.csv` remains absent, consistent with PR012's open publication
  gate at `research_program/synthesis/pr012_tv_curve_scope.md:176-190`.

Reproducibility verdict: `OK_NO_NEW_NUMERIC_RESULT`.

## 5. dev/validation separation & ground-truth leakage

The matrix is documentary. Its scope clause forbids code, simulations, PR012 publication and
changes to frozen artifacts (`survival_matrix_1p1_to_3p1.md:9-13`). It defines no estimator and
does not read embedding data. The only working-tree candidate before this report was the matrix;
no `data/`, `results/`, package, test or threshold path changed.

The matrix also preserves the order-only output boundary for `H[C;R]` and explicitly leaves its
3+1D geometric loss unspecified (`survival_matrix_1p1_to_3p1.md:156-172`).

Separation/leakage verdict: `OK_DOCUMENT_ONLY`.

## 6. Claim-boundary check

The transfer classifications are bounded correctly:

- the opening disclaims dimensional transfer and 3+1D implementation
  (`survival_matrix_1p1_to_3p1.md:9-13`);
- `G_diamond`, the fixed-`n` ladder and PR012 survive only as protocols, not as dimensional
  theorems (`survival_matrix_1p1_to_3p1.md:41-51`);
- scalar `tau` is explicitly rejected as a 3+1D localizer
  (`survival_matrix_1p1_to_3p1.md:87-102`);
- Hellinger is retained only conditionally and only in the upper-bound direction
  (`survival_matrix_1p1_to_3p1.md:104-120`);
- the open target, dual closure, `TV=0` class, positive witness, two limits, adversarial class and
  selector are carried forward as blockers, not results
  (`survival_matrix_1p1_to_3p1.md:174-187`);
- the final WP5 clause forbids promotion of PR011/PR012 geometry or numbers
  (`survival_matrix_1p1_to_3p1.md:189-205`).

No PASS is coerced from PR012's `GRID_RESOLUTION_ABSTAIN`; the matrix retains it only as a
fail-closed protocol precedent. No reconstruction, global event-horizon, continuum-convergence or
3+1D recoverability result is claimed.

Scoped OP-0.1 terminal: `SURVIVAL_MATRIX_COMPLETE`.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | The matrix contains 63/63 required cells: seven constructs times nine axes. | `rg -c '^\\| (Target|Orientacion/dualidad|Canal/escala|Patch|Limite continuo|Salida/perdida|Alternativas|Garantia|Abstencion) \\|' ...` -> `63` |
| 2 | OK | Every matrix row has an existing source range or an explicit scoped `NO_ESPECIFICABLE`; the anchor parser found no invalid file/range. | anchor parser -> `ANCHORS=63 ERRORS=0`; `survival_matrix_1p1_to_3p1.md:15-39` |
| 3 | OK | Every negative terminal is operational: each of the nine required terminals occurs once for every construct. | terminal-count command -> nine counts of `7`; `survival_matrix_1p1_to_3p1.md:53-172` |
| 4 | OK | The matrix preserves the positive/negative evidence asymmetry and does not transfer the 2D copula reduction as a 3+1D theorem. | `survival_matrix_1p1_to_3p1.md:104-120` |
| 5 | OK | PR012 remains draft-only and unpublished; abstention is not converted into PASS. | `research_program/synthesis/pr012_tv_curve_scope.md:176-190`; absence check for `data/reports/pr012_tv_curve_n8.csv` |
| 6 | OK | No seal drift, code change, simulation, result write or embedding input occurred. | `make verify-seal`; `git status --short --branch`; `survival_matrix_1p1_to_3p1.md:9-13` |
| 7 | WARN | Mechanical audit reports 22 pre-existing committed-data generator-reference warnings. They are outside OP-0.1 but remain unresolved repo-level warnings. | verbatim mechanical output in section 2 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=22

## 8. Verdict

The OP-0.1 scoped gate passes with terminal `SURVIVAL_MATRIX_COMPLETE`. The repo-level audit
verdict remains warning-bearing because the mandatory mechanical audit emitted 22 historical
warnings.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
