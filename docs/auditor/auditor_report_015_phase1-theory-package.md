# Auditor Report 015 — Phase 1 theory package

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Strictly read-only documentary audit authorized by signed committee decision 031, section 9, on
`main` at base commit `496985dbecd464a57267e607b7d3b48c323b510b` (`HEAD=origin/main`). The exact
candidate blobs are:

```text
OP-1.1  6d024df0376d701b6c26c061d2c565942ebd3ab19a687f2c480551cae84f3024
OP-1.2  0bfb9eeddc9ad14354956a99e522c1ca5b0ed05e7838d31be84c4fe63ac1663f
OP-1.3  60e874813c44ebe31bbed40cde507c18fe8e8e686447d76ca96452553d64fb1b
```

Scope includes decisions 027--031, `docs/plan_operativo_15_julio_2026.md`,
`docs/claim_grammar.md`, exact claim boundaries, authorization provenance and cited local-source
status. Per PI instruction, no scientific code, simulation, test, seed, commit or push was run.
The only new file written by the auditor is this report.

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

Exit code: `0`.

The 22 warnings are repo-wide heuristic findings on previously committed data and are outside the
eight-document Phase-1 package. They remain counted and are not silently discarded.

## 3. Seal & freeze integrity

- `make verify-seal` returned exit code 0 and
  `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- The binding record contains the identical full value at `docs/preregistration_002.md:8`.
- The mechanical audit independently found the live hash recorded in the repository freeze chain.
- `make test`, `dry-run`, `gate` and every validation path were not run by explicit PI scope.
- The Phase-1 candidates are documents and do not modify the frozen estimator or its seal.

## 4. Reproducibility of published numbers

The three candidates introduce no empirical result table, fitted value, seed-derived number or
validation verdict. Their quantitative content is theorem/definition level:

- OP-1.1 labels the exact `32 M^3/r` Kruskal normalization as
  `[UNVERIFIED_EXACT_KRUSKAL_NORMALIZATION_LOCAL_SNAPSHOT]` adjacent to the formula and again in
  sources (`research_program/synthesis/op11_spherical_dual_target.md:25-37,340-345`).
- OP-1.2 confines its exact scaling statements to fixed patch shape and sector and marks missing
  primary snapshots (`research_program/synthesis/op12_tv_zero_3p1.md:47-80,184-192`).
- OP-1.3 derives the bounded-witness/Hoeffding certificate in the text and marks absent local
  primary snapshots; it does not report an executed certificate (`research_program/work_packages/op13_positive_evidence_protocol.md:24-80,233-239`).

The 22 mechanical warnings concern older committed data files, not numbers claimed by this package.
No generator was rerun because tests and scientific execution were outside the signed scope.

## 5. dev/validation separation & ground-truth leakage

- `git status --short --branch` showed only eight untracked Markdown documents after decision 031:
  decisions 027--031 and OP-1.1--OP-1.3. No code, data or sealed artifact appeared in the audit
  surface.
- OP-1.1 prohibits coordinates, `r`, `M`, expansions and continuous labels in construction,
  selection, orientation and abstention; they enter only the scoring layer
  (`research_program/synthesis/op11_spherical_dual_target.md:235-245`).
- Same-carrier duality is purely combinatorial, with `iota_P=id` and relabeling naturality, rather
  than an embedding correspondence (`research_program/synthesis/op11_spherical_dual_target.md:190-203`).
- Element-wise abstention counts as error and remains in denominators, with separate rates; empty
  denominators fail closed (`research_program/synthesis/op11_spherical_dual_target.md:263-283`).
- OP-1.3 requires development/confirmation separation and forbids embedding-derived quantities
  from guiding promotion, features, orientation, boundary or abstention
  (`research_program/work_packages/op13_positive_evidence_protocol.md:83-108`).

No ground-truth-leakage or freeze-separation error was found in the exact documents.

## 6. Claim-boundary check

- OP-1.1 is `NO_IMPLEMENTATION / NO_RECOVERY_RESULT`, defines no reconstructor, does not identify an
  event horizon of an arbitrary continuation, and denies estimator existence, selector,
  convergence and 3+1D recovery (`research_program/synthesis/op11_spherical_dual_target.md:3-21,328-338`).
- OP-1.2 is a scoped candidate-family classification, not a general 3+1D TV-zero class or
  Hauptvermutung (`research_program/synthesis/op12_tv_zero_3p1.md:3,21-22,155-180`).
- OP-1.3 is `NO_EXECUTION_AUTHORIZED`, says a TV lower bound does not itself localize a target, and
  leaves implementation pending a generator/witness spec
  (`research_program/work_packages/op13_positive_evidence_protocol.md:3,19-22,163-174,223-230`).
- The decisions and candidates preserve missing-source statuses rather than promoting them.

No reconstruction, asymptotic-horizon, executed 3+1D recovery or coerced PASS claim was found.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | WARN | Mechanical audit emitted 22 repo-wide heuristic warnings for previously committed data files without a detected generator reference; none belongs to this package, but all remain counted. | `bash .claude/skills/auditor/audit.sh`, exit 0; verbatim output in section 2 |
| 2 | OK | All three adopted candidate hashes match committee decision 031 exactly. | `sha256sum` output; `docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md:10-14` |
| 3 | OK | Decisions 027--031 contain the required PI signatures and the candidates record authorizations 027--030. | `docs/comite/comite_decision_027_phase1-theory-package-first-review.md:172-177`; decision 031 `:163-169`; candidate lines 9--14/5--10 |
| 4 | OK | All blockers from decisions 027--030 are present in the exact blobs: temporal duality, total outputs, empty/abstain distinction, domains, precedence, natural support map, fail-closed losses and source marker. | `rg` audit output; OP-1.1 `:88-108,190-242,263-326,340-345`; OP-1.2 `:81-103`; OP-1.3 `:176-230` |
| 5 | OK | Live seal matches the binding prereg-002 record. | `make verify-seal`, exit 0; `docs/preregistration_002.md:8` |
| 6 | OK | No code/data/sealed artifact is in the package audit surface and no scientific execution was run. | `git status --short --branch`; signed decision 031 `:163-169` |
| 7 | OK | Claim boundaries explicitly exclude reconstruction, convergence, executed recovery and implementation readiness. | OP-1.1 `:328-338`; OP-1.2 `:155-180`; OP-1.3 `:163-174,223-230` |

AUDIT_ERRORS=0
AUDIT_WARNINGS=22

## 8. Verdict

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
