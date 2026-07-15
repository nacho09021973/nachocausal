# Auditor Report 014 — OP-0.2 claim grammar

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Scoped OP-0.2 gate under `docs/plan_operativo_15_julio_2026.md:141-174`. The audited candidate is
`docs/claim_grammar.md`, SHA256
`7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786`, authored against source
snapshot `726c8c1eda16334a1b30b9f4ad82927f0c834382` on branch `main`.

Committee decision 026 adopted that exact blob into `COMMITTEE_ADOPTED_AUDIT_PENDING` and
authorized this hash-specific audit (`docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md:137-164`).
This audit asks whether the anchors are valid, the claim boundaries and terminal precedence are
complete, no objective is promoted to a result, and no code, data, result, seed or seal changed.
It does not certify a recovery theorem, authorize scientific execution, or authorize commit/push.

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

The 22 warnings are repo-level heuristic findings predating OP-0.2. They do not invalidate this
documentary grammar, but this report counts them exactly as required by the auditor contract.

## 3. Seal & freeze integrity

- `make verify-seal` exited `0` and printed
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- The same full hash is frozen in `docs/preregistration_002.md:8`.
- `sha256sum docs/claim_grammar.md` recomputed the committee-adopted hash
  `7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786`.
- OP-0.2 changed no threshold, seal, preregistration, seed, code, data or result artifact.

Seal verdict: `OK_NO_DRIFT`.

## 4. Reproducibility of published numbers

The grammar publishes no new numerical scientific result (`docs/claim_grammar.md:14-19`). Its
equations define claim contracts or restate bounded results with source anchors; they are not
outputs of a new run. Checks performed:

- the path-and-range parser returned `ANCHORS=17 ERRORS=0`, including the four bibliography paths
  containing spaces;
- `make test` exited `0`: `261 passed in 395.17s`;
- the committee checker returned `BRIEF_CHECK=PASS` for decision 026;
- the required-clause control returned `HASH_AND_REQUIRED_CLAUSES=PASS` for the exact adopted blob;
- `data/reports/pr012_tv_curve_n8.csv` remains absent.

Reproducibility verdict: `OK_NO_NEW_NUMERIC_RESULT`.

## 5. dev/validation separation & ground-truth leakage

The candidate is documentary and defines no implementation or estimator. Its minimum result
template requires embedding information to be used only for scoring and requires evidence that it
does not define construction, selection, abstention or boundary (`docs/claim_grammar.md:386-403`).
The gate precedence makes data-contract failure, out-of-domain and abstentions dominate scientific
PASS/FAIL (`docs/claim_grammar.md:369-384`).

The scoped status check returned `CODE_DATA_RESULT_PATHS=UNCHANGED`; the working tree contains only
untracked documentary OP-0 files, including this report. No sealed validation path or scientific
execution was run.

Separation/leakage verdict: `OK_DOCUMENT_ONLY`.

## 6. Claim-boundary check

The adopted grammar is fail-closed and does not exceed current evidence:

- finite-patch order does not identify the global event horizon, and every permitted localization
  form disclaims that global claim (`docs/claim_grammar.md:57-81`);
- the 1+1D observable is explicitly an inter-geodesic-distance proxy, not a true null expansion or
  a 3+1D codimension-two marginal surface (`docs/claim_grammar.md:83-97`);
- representative-level and quotient-level duality are typed separately, the model law obeys an
  explicit pushforward contract, and estimator covariance remains `TARGET`
  (`docs/claim_grammar.md:123-188`);
- `fixed_n` and `order+number` remain distinct, and no 1+1D scale degeneracy is promoted into a
  characterization of the 3+1D `TV=0` class (`docs/claim_grammar.md:190-231`);
- the direct TV impossibility consequence is restricted to exact 0-1 recovery; generic loss
  requires disjoint success regions or a proved binary reduction, while positive evidence requires
  a bounded witness and confidence-valid lower gap (`docs/claim_grammar.md:273-338`);
- sprinkling a known geometry is kept separate from a causal-set dynamics result
  (`docs/claim_grammar.md:340-367`).

The state machine correctly leaves the audited blob unchanged and assigns the final terminal in
this external report (`docs/claim_grammar.md:407-442`). No recovery, continuum-convergence, event-
horizon, 3+1D or quantum-gravity result is claimed.

Scoped OP-0.2 terminal: `CLAIM_GRAMMAR_ADOPTED`.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | The audited bytes equal the exact committee-adopted blob. | `sha256sum docs/claim_grammar.md` -> `7b28c14c...2786`; decision 026 lines 11-19 |
| 2 | OK | All 17 documentary anchors resolve to existing files and valid line ranges. | path-and-range parser -> `ANCHORS=17 ERRORS=0` |
| 3 | OK | Teleology, true 1+1D proxy status, dual typing, channel/scale and dynamics boundaries are explicit and fail-closed. | `docs/claim_grammar.md:57-231`, `:340-367` |
| 4 | OK | Upper-TV difficulty and lower-TV positive evidence are separated; generic-loss transport requires a valid reduction. | `docs/claim_grammar.md:273-338` |
| 5 | OK | Mandatory domain, embedding-only-score, abstention and terminal-precedence fields are present. | `docs/claim_grammar.md:369-405` |
| 6 | OK | Tests, seal, committee checker and forbidden-path controls pass; no scientific result path changed or ran. | `make test`; `make verify-seal`; `BRIEF_CHECK=PASS`; `CODE_DATA_RESULT_PATHS=UNCHANGED` |
| 7 | WARN | Mechanical audit reports 22 pre-existing committed-data generator-reference warnings. They are outside OP-0.2 but remain unresolved repo-level warnings. | verbatim mechanical output in section 2 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=22

## 8. Verdict

The exact committee-adopted OP-0.2 blob passes its scoped audit and receives terminal
`CLAIM_GRAMMAR_ADOPTED`. Together with OP-0.1 terminal `SURVIVAL_MATRIX_COMPLETE`, this satisfies
the documentary gate `PHASE_0_AUDIT_READY` defined in `docs/plan_operativo_15_julio_2026.md:172-174`.
The repo-level audit verdict remains warning-bearing because the mandatory mechanical audit emitted
22 historical warnings.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
