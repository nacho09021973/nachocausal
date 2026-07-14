# Auditor Report 007 — pr011-viability-freeze-text

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

**Trigger:** `/auditor` after comité 022 and user sign-off on PR011 spec freeze (G2 on freeze text).

**Target:** `research_program/synthesis/pr011_mass_distinguishability_viability.md` (status
`FROZEN_VIABILITY_SPEC`), supporting artefacts (`dev/pr011_freeze_sanity_check.py`,
`tests/test_pr011_freeze_sanity.py`, `docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md`),
and repo integrity at commit `11ef1d64d72a337bfdc8723e917a3477c171a825` (branch `main`).

**Out of scope:** TV certification execution (not authorized; no `ε` claimed); sealed validation
path; `docs/preregistration_*` amendment.

## 2. Mechanical audit

Verbatim output of `bash .claude/skills/auditor/audit.sh`:

```
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/rvar_closure_negative_result.md
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
WARN: committed data file with no generator reference: data/reports/present_anchor_clean_v3_kill_test.csv
WARN: committed data file with no generator reference: data/reports/present_anchor_sanity_pilot.csv
----------------------------------------
Auditor: 0 error(s), 12 warning(s)
```

Exit code: `0`.

## 3. Seal & freeze integrity

- **Live seal:** `make verify-seal` → `thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
- **Frozen record:** matches `docs/preregistration_002.md:8`, `docs/preregistration_003.md:9`.
- **Sealed package:** `git status --short` shows **no** `M nachocausal/` entries this session.
- **PR011 freeze:** lives in `research_program/synthesis/` — does **not** modify `thresholds.py` or
  any `docs/preregistration_*.md` frozen file. `docs/preregistration_003.md` §7 OPEN minimax-over-`C`
  remains; PR011 does not present itself as amending (★).

## 4. Reproducibility of published numbers

**PR011 spec numeric anchor (the only numbers in scope):**

| Claim | Generator | This session |
|---|---|---|
| `V(τ=1) ≈ 1.471720` | `research_program/work_packages/wp4_kappa_numeric_reference.py` shape A | `V=1.471720` (script stdout) |
| `κ ≈ 7.97×10^{-4}` | same | `kappa=7.969751e-04` |
| Geometry constraints | `dev/pr011_freeze_sanity_check.py` | `PR011_FREEZE_SANITY=PASS` |
| `pytest` harness | `tests/test_pr011_freeze_sanity.py` | 1 passed |

**No `TV` or `ε` value is published** — no certification script exists (`pr011 spec §9`:
`dev/pr011_tv_certification_enumeration.py` absent). Correct for current authorization state.

**Not re-run:** full `make test` suite (out of PR011 scope); frozen `docs/` PASS numbers unchanged
at HEAD.

## 5. dev/validation separation & ground-truth leakage

- PR011 channel is order-only on unlabeled posets; **no** embedding in the estimator class
  (`pr011 spec §4.1`, `§2.2`).
- Pair `(τ_0,τ_1)=(0.95,1.05)` fixed by `MIDPOINT_QUARTER_SPAN` rule (`§5`) — not from PR009/PR010
  outputs (`§12` checklist).
- `dev/pr011_freeze_sanity_check.py` uses geometry only — no seeds, no `validate.run()`.
- **Risk:** working tree mixes PR010 dev edits (`dev/run_pr010_reference_depth_coverage_development.py`
  M) with untracked PR011 files — commit discipline needed so PR011 freeze is not co-mingled with
  PR010 science in one undifferentiated commit (`git status --short`).

## 6. Claim-boundary check

**PR011 freeze text — OK on bounded claims:**

- Explicitly **not** prereg, not recoverability, not sealed estimator floor (`§2.2`).
- **not** absolute-unit `R_H` outside `G_◊` (`§2.2`, Theorem A anchor).
- Minimax language is **conditional** on future certified `ε` (`§7`, `§8` terminals) — no
  established indeterminacy result emitted.
- Execution and terminals **blocked** (`§10`, `§13`: `EXECUTION BLOCKED`).

**Stale internal text — WARN (not over-claim, but inconsistent):**

- `pr011_mass_distinguishability_viability.md:10-11` still says "PR010 must close … before PR011 is
  **frozen** or executed" while `§10` discharges G0a (spec freeze) and status is `FROZEN_VIABILITY_SPEC`.
  Does not authorize execution (`§284-285`) but confuses readers.

**`research_program/README.md` §1.2:** states spec frozen, execution blocked — consistent with §10.

**No** metric reconstruction, 3+1D, or global event-horizon claim found in PR011 synthesis files.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | Seal intact; matches prereg-002/003 | `make verify-seal`; `docs/preregistration_003.md:9` |
| 2 | OK | `nachocausal/` unmodified | `git status --short` |
| 3 | OK | No TV/ε/certification terminal claimed | absent `dev/pr011_tv_certification_*`, `data/reports/pr011_*` |
| 4 | OK | Anchor `V`, `κ` match kappa script | `wp4_kappa_numeric_reference.py` stdout; `pr011 spec §3.1` |
| 5 | OK | Geometry sanity reproducible | `pytest tests/test_pr011_freeze_sanity.py`; `pr011_freeze_sanity_check.py` |
| 6 | OK | Claim boundary: viability spec, not minimax result or reconstruction | `pr011 spec §2.2`, `§13` |
| 7 | OK | Does not amend frozen `prereg-003` (★) | `pr011 spec` + `geometric_indeterminacy_decision.md:20-22` |
| 8 | WARN | Mechanical audit: 12 committed CSVs without generator refs (pre-existing) | `audit.sh` verbatim §2 |
| 9 | WARN | Freeze bundle **untracked**: `research_program/synthesis/`, comité 022, pr011 sanity test | `git status --short` |
| 10 | WARN | PR011 lines 10–11 stale vs G0a split (says freeze needs PR010) | `pr011_mass_distinguishability_viability.md:10-11` vs `§274-285` |
| 11 | WARN | Comité 022 §11 sign-off blank while spec cites user sign-off | `comite_decision_022:§11` vs `pr011 spec:5-6` |
| 12 | WARN | PR010 coverage CSV/sha256 untracked alongside PR011 work | `git status`: `?? data/reports/pr010_*` |
| 13 | WARN | G2 in spec still marked OPEN — this audit covers **freeze text only**; pre-execution G2 remains for any `ε` report | `pr011 spec §281` |

AUDIT_ERRORS=0
AUDIT_WARNINGS=16

## 8. Verdict

Freeze-text integrity for PR011 is **sound**: no false TV claim, seal intact, claim boundaries
honored, anchor numbers trace to committed deterministic scripts. Warnings are procedural
(untracked artefacts, stale sentence, pre-existing CSV hygiene) — not falsification of the freeze.

**G2 partial discharge:** freeze-text / claim-boundary audit **PASS_WITH_WARNINGS**. TV
certification execution still requires G0b + a fresh pre-execution audit on any reported `ε`.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS