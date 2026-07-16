# Auditor Report 017 — op21-terminal-run

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Audit of the OP-2.1 terminal-issuing bench run, before its terminal is recorded as the OP-2.1
outcome (decision 034 §9 R6). Repo `/home/ignac/nachocausal`, branch `main`,
HEAD = `cd3ef515d3523c884b4f2dbfa250b28cb6b707fd` ("op21: open OP-2.1 and freeze
reference-certifier dev prereg (comite decision 034)"), parent `016be8b` (Phase-1 closure).
Trigger: binding R6 step of `docs/comite/comite_decision_034_op21-certifier-opening.md` §9 after
`make op21-terminal` emitted `OP21_TERMINAL=POSITIVE_CERTIFIER_REFERENCE_PASS`
(report: `results/op21_reference_certifier_report.json`, git-ignored by design like all
`results/` artefacts; `git check-ignore` confirms).

## 2. Mechanical audit

Verbatim output of `bash .claude/skills/auditor/audit.sh` (exit code 0):

```text
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/auditor/auditor_report_015_phase1-theory-package.md,docs/auditor/auditor_report_016_phase1-provenance-reaudit.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/comite/comite_decision_027_phase1-theory-package-first-review.md,docs/comite/comite_decision_028_phase1-theory-package-second-review.md,docs/comite/comite_decision_029_phase1-theory-package-third-review.md,docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md,docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md,docs/comite/comite_decision_032_phase1-theory-closure-handoff.md,docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md,docs/comite/comite_decision_034_op21-certifier-opening.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/rvar_closure_negative_result.md
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

The 22 warnings are the same legacy `data/reports/` findings carried by reports 012–016; none
involves OP-2.1 artefacts.

## 3. Seal & freeze integrity

- `make verify-seal` (this session) →
  `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`,
  identical to the frozen record at `docs/preregistration_002.md:8`. No drift.
- All 11 pre-existing `nachocausal/*.py` + `nachocausal/scoring/*.py` SHA256 hashes match the
  pre-work baseline recorded before any `certifier/` file existed (decision 034 §9 R4;
  `sha256sum … | diff - <baseline>` → clean, this session, both after the freeze commit and after
  the terminal run). The freeze commit `cd3ef51` touched no pre-existing `nachocausal/` file
  (`git show --stat cd3ef51`: `Makefile`, 6 new `certifier/` files, the dev prereg, decision 034
  — 9 paths, nothing else).
- Import firewall verified two ways: AST test
  `certifier/tests/test_op21_reference_certifier.py` (`test_g6_certifier_never_imports_the_sealed_path`)
  passed in the committed suite, and manual inspection confirms `certifier/` imports only
  `nachocausal.thresholds` (read-only env pin + seed constants; `certifier/bench.py`).
  `validate.run()` is never invoked.

## 4. Reproducibility of published numbers

The published numbers are the terminal-run outputs (stdout of `make op21-terminal`, task log, and
`results/op21_reference_certifier_report.json`). Each was traced to its committed deterministic
generator:

- **Freeze-before-run order (dev prereg OP21 precondition):** freeze commit `cd3ef51` timestamp
  `1784127241` (git `%ct`) precedes the run's `volatile.started_unix = 1784127524.25`; the report
  binds itself to `volatile.commit = cd3ef515d…` — the exact frozen tree. The MC-gated tests were
  skipped before the freeze commit (25 passed / 2 skipped, `OP21_PREREG_FROZEN` unset), by the
  env-gate in `certifier/tests/test_op21_reference_certifier.py` (`_MC_GATE`).
- **Exact reference miscoverage `p0`:** recomputed this session by an independent code path
  (`math.comb` exact-binomial enumeration, vs the bench's `lgamma` path in
  `certifier/bench.py::_binomial_pmf`): CELL-B1 `1.73708e-08`, CELL-B0 `1.09774e-06`, CELL-CAL
  `8.7372e-04`, CELL-EPS `1.76825e-05` — all four match the report to `rel_tol=1e-9`.
- **C1/C2 limits and counts:** recomputed from the frozen formulas
  (`n_rep*alpha_j`; `n_rep*p0 + max(5*sqrt(n_rep*p0*(1-p0)), 6)`, dev prereg OP21 §5) — all match
  the report; every count is inside its bands (CELL-CAL: 176 observed vs 174.7 expected,
  band 240.8; CELL-EPS: 6 vs band 12.9; all other cells 0).
- **Reproducibility (C3):** `report_hash_run1 == report_hash_run2` (two full passes, identical
  frozen seeds, canonical-JSON SHA256), recorded in the report and re-checked this session.
- **Mutation power (C4, binding falsifier test of decision 034):** MUT-A (anti-conservative
  radius `log(2/α)`) detected via C2 on CELL-CAL and CELL-EPS; MUT-B (dropped ε) detected via
  C1+C2 on CELL-EPS — exactly the detection channels predicted in dev prereg OP21 §5 C4. Both
  `detected=True` in the report.
- **Terminal:** `POSITIVE_CERTIFIER_REFERENCE_PASS` is consistent with
  `criteria = {c1/c2/c6 fail lists empty, c3_ok, c4_ok, c5_ok, coverage_ok}` under the frozen
  precedence chain (dev prereg OP21 §6; `certifier/bench.py::run_bench`). `n_rep = 200000` equals
  the frozen `N_REP`; `issue_terminal = true`; numpy `1.26.4` equals the pin
  (`nachocausal/thresholds.py:18`).

## 5. dev/validation separation & ground-truth leakage

- **Seeds:** the bench derives every RNG seed by the frozen rule over
  `SYNTH_MC_BAND = [3_000_000, 3_999_999]` (`certifier/bench.py::synth_seed`, guarded — G3 test
  can fail). Verified programmatically this session: the band is disjoint from `DEV_SEEDS` and
  from all 20 `VALIDATION_SEEDS` (`nachocausal/thresholds.py:57,67-71`); the virgin band is
  `[2_000_000, 2_999_999]` (`docs/preregistration_002.md:14-30`) — untouched. No sprinkling
  generator was called (no `nachocausal.generator` import in `certifier/`, §3).
- **One-shot rule:** exactly one terminal-issuing run (`--terminal`, single artefact
  `results/op21_reference_certifier_report.json`; `ls results/ | grep op21` → one file). The
  pre-terminal MC activity was the env-gated dev smoke at `n_rep=1000` after the freeze commit
  (`issue_terminal=False` path) — unrestricted, uncitable dev work per dev prereg OP21 §7.
- **Ground truth:** the certifier's input type is two `[0,1]` float streams
  (`certifier/kernel.py::_validated_stream`); no embedding, coordinates or labels are reachable.
  Per decision 034 D1 this is module-level blindness only and is recorded as such — no
  end-to-end no-leakage claim is made anywhere in the OP-2.1 artefacts.
- **PR011 quarantine:** `f_bench = |relations|/6` is declared `BENCH_ONLY_NON_PROMOTABLE`
  (`certifier/bench.py::_pr011_fixture` docstring; dev prereg OP21 §4.2); PR011 laws are read
  through the same committed enumeration module the existing tests use, not re-executed as
  confirmation.

## 6. Claim-boundary check

- The terminal is presented, in every artefact, as a statistics-infrastructure outcome:
  `certifier/__init__.py:5-7` ("licenses no physical, recovery or 3+1D claim"), dev prereg OP21
  header and §9, decision 034 §9 binding rules. A grep over `certifier/*.py` for
  horizon/recovery/3+1D/physics vocabulary finds only these negative-boundary statements.
- `README.md` and all other `docs/` claims are untouched by commit `cd3ef51` (9-path surface,
  §3). No abstain/OUT_OF_DOMAIN was coerced: the C5 states in the report are distinct
  (`ABSTAIN_GENERATOR_ERROR`, `ABSTAIN_PRECISION`, `ZERO_BOUND`) and the terminal-precedence
  chain is frozen in the committed prereg.
- No `n_star`, no scaling-law, no witness, no PR012/PR013, no 3+1D statement appears in any
  OP-2.1 artefact (dev prereg OP21 §9).

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | Live seal matches frozen record; no drift | `make verify-seal` vs `docs/preregistration_002.md:8` |
| 2 | OK | 11 pre-existing `nachocausal/*.py` hashes unchanged through freeze commit and terminal run | `sha256sum … \| diff - <R4 baseline>`; `git show --stat cd3ef51` |
| 3 | OK | Prereg frozen (committed) before the terminal run; report bound to the frozen commit | commit `%ct` 1784127241 < `started_unix` 1784127524.25; `volatile.commit=cd3ef51…` |
| 4 | OK | All published numbers reproduced: exact `p0` (independent `math.comb` path, 4/4 match at 1e-9), C1/C2 limits, counts inside bands | §4 this report |
| 5 | OK | Reproducibility C3: double-pass canonical hashes identical | `report_hash_run1 == report_hash_run2` |
| 6 | OK | Binding mutation test: MUT-A and MUT-B both detected via the prereg-predicted channels | report `frozen.mutants`; dev prereg OP21 §5 C4 |
| 7 | OK | Seed discipline: `SYNTH_MC_BAND` disjoint from dev + validation bands; no validation/confirmatory seed consumed; no sprinkling | `certifier/bench.py::synth_seed`; `nachocausal/thresholds.py:57,67-71` |
| 8 | OK | Claim boundary intact: statistics-infrastructure terminal only; distinct abstain states; no coercion | `certifier/__init__.py:5-7`; dev prereg OP21 §§6,9 |
| 9-30 | WARN | 22 legacy `data/reports/` files with no generator reference (pre-existing; carried by reports 012–016; none is an OP-2.1 artefact) | audit.sh output, §2 |
| 31 | WARN | Independence is procedural, not personal: the implementer, terminal-run operator and auditor are the same agent session. Every check above is command-anchored and re-runnable by a third party, but decision 034's independent-falsification intent is only fully discharged when a separate session/person re-runs this audit. | decision 034 §5 (falsifier: independent-falsification gate); this report §1 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=23

## 8. Verdict

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
