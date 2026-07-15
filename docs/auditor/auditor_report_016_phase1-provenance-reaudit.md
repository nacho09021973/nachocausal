# Auditor Report 016 — Phase 1 provenance re-audit

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Strictly read-only re-audit authorized by signed committee decision 032, section 9. Scope:

- decisions 027--032, including corrected decision-031 hash
  `2c448f6a818075045ca11a0e3cb378fcc66e69d132c844edd2a60dbb42a7e86a` and signed decision-032 hash
  `e6748ebb264c7c94cc553563914971d3a2a0feaa03721fd81db51585a1bf0f16`;
- historical auditor report 015,
  `4abd0bd0e40eb3d010d766cda7071303bc76790971943d6e8899868272ecaf00`;
- OP-1.1 `6d024df0376d701b6c26c061d2c565942ebd3ab19a687f2c480551cae84f3024`;
- OP-1.2 `0bfb9eeddc9ad14354956a99e522c1ca5b0ed05e7838d31be84c4fe63ac1663f`;
- OP-1.3 `60e874813c44ebe31bbed40cde507c18fe8e8e686447d76ca96452553d64fb1b`;
- Phase-1 plan, claim grammar, authorization chain, source-status markers and durable citation
  portability.

The trigger was the decision-032 falsifier finding that two decision-031 role citations depended on
an ephemeral external dossier. The PI authorized only their replacement by repo-local anchors and
this re-audit. No scientific code, simulation, test, seed, commit or push was run.

## 2. Mechanical audit

Command: `bash .claude/skills/auditor/audit.sh`

Verbatim output:

```text
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/rvar_closure_negative_result.md
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

Exit code: `0`. All 22 mechanical warnings remain repo-wide legacy-data warnings outside this
documentary package and remain counted.

## 3. Seal & freeze integrity

- `make verify-seal` returned exit code 0 and full live SHA256
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- `docs/preregistration_002.md:8` contains the identical binding hash.
- Decisions 031 and 032 both return `BRIEF_CHECK=PASS` after the authorized replacements/sign-off.
- The three scientific hashes are byte-identical to reports 015 and decisions 031--032.
- `make test`, `dry-run`, `gate`, validation and every seed-consuming path were not run.

## 4. Reproducibility of published numbers

No empirical output or executed certificate is introduced. Source and theorem status remain as in
report 015:

- OP-1.1 retains the exact Kruskal normalization as an explicitly unverified declared convention
  (`research_program/synthesis/op11_spherical_dual_target.md:25-37,340-345`).
- OP-1.2 remains scoped to the co-scaled candidate family and marks unavailable primaries
  (`research_program/synthesis/op12_tv_zero_3p1.md:47-80,184-192`).
- OP-1.3 presents a conditional in-text bound, not an executed result, and preserves unavailable
  source markers (`research_program/work_packages/op13_positive_evidence_protocol.md:24-80,233-239`).

No generator or scientific test was run under the signed scope.

## 5. dev/validation separation & ground-truth leakage

- The authorized delta is limited to two citation targets in decision 031 and the decision-032
  sign-off. The candidate hashes did not change.
- A repository-wide search over decisions 027--032, report 015 and OP-1.1--OP-1.3 returns no
  references to an external temporary directory after repair.
- Decision 031 now cites its own durable sections for the exact hashes and the no-execution rule
  (`docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md:10-28,86,95,132-148,163-169`).
- OP-1.1 and OP-1.3 retain the embedding/scoring separation and fail-closed abstention rules
  (`research_program/synthesis/op11_spherical_dual_target.md:235-245,263-283`;
  `research_program/work_packages/op13_positive_evidence_protocol.md:83-108`).

No portability, leakage or separation error remains in the scoped surface.

## 6. Claim-boundary check

The three author terminals, negative limits and source markers are unchanged. `PHASE_1_THEORY_READY`
remains a proposed documentary gate, not estimator existence, implementation readiness or recovery
(`research_program/synthesis/op11_spherical_dual_target.md:328-338`;
`research_program/synthesis/op12_tv_zero_3p1.md:155-181`;
`research_program/work_packages/op13_positive_evidence_protocol.md:163-174,223-230`).

Decision 032 explicitly leaves the terminal at
`SUBSTANTIVELY_SATISFIED_PROVENANCE_REAUDIT_PENDING` and forbids commit, push and OP-2.1 until a new
committee decision (`docs/comite/comite_decision_032_phase1-theory-closure-handoff.md:118-158,160-172`).

No over-claim or verdict coercion was found.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | WARN | Mechanical audit emitted 22 repo-wide legacy-data warnings outside this package; all remain counted. | `bash .claude/skills/auditor/audit.sh`, exit 0; section 2 |
| 2 | WARN | Historical report 015 omitted the ephemeral-citation portability defect later found by committee 032. The two citations are corrected and this report supersedes report 015 for Phase-1 closure. | `docs/comite/comite_decision_032_phase1-theory-closure-handoff.md:118-158`; decision 031 `:86,95` |
| 3 | OK | No durable scoped document now depends on an external temporary path. | repository-wide `rg` check over the scoped paths, exit 1/no matches |
| 4 | OK | All three scientific hashes remain exactly unchanged. | `sha256sum`; section 1 |
| 5 | OK | Both corrected/signed committee briefs pass the structural checker. | `check_comite_brief.py` on decisions 031 and 032, exit 0 |
| 6 | OK | Live seal matches prereg-002 and no test or scientific execution ran. | `make verify-seal`, exit 0; `docs/preregistration_002.md:8` |
| 7 | OK | Claim boundaries and unavailable-source markers remain intact. | OP-1.1 `:328-345`; OP-1.2 `:155-192`; OP-1.3 `:163-174,223-239` |

AUDIT_ERRORS=0
AUDIT_WARNINGS=23

## 8. Verdict

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
