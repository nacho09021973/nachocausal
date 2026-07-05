# Auditor Report 006 — rvar-mu-freeze-addendum-preflight

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/adnac/nachocausal`, branch `main`, HEAD at audit time = `0271fd9` ("dev: freeze
R-VAR mu calibration addendum (Part F object choice)"). Trigger: pre-`/comite` foundation — the
PI has asked to convene the committee to authorize execution of R-VAR v2.2 Part F step 3 (μ-table
computation over EXPLORE nulls). Before that committee deliberates a PROCEED, this audit verifies:
(1) Gate 0 Tier 0 (`b142377`) and Tier 1 (`55e19b8`) PASS claims are real, not just asserted; (2)
the just-committed μ-freeze addendum (`0271fd9`, `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md`) matches
comité 018's adjudication (`docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md`)
without silent deviation; (3) seal integrity; (4) no `EXPLORE_POOL`/`VALIDATION_SEEDS` seed has
been touched by Part F execution yet.

## 2. Mechanical audit

```
$ bash .claude/skills/auditor/audit.sh
Auditor — auditing: /home/adnac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md
----------------------------------------
Auditor: 0 error(s), 0 warning(s)
```
Exit code: 0.

## 3. Seal & freeze integrity

- `make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- `docs/preregistration_002.md:8` records the identical hash verbatim. **MATCH.**
- The live instrument (`nachocausal/thresholds.py`) is the one the current, binding prereg names.
  Nothing under audit here touches this file — Part F is entirely `dev/`-side.

## 4. Reproducibility of published numbers

- **Gate 0 Tier 0** (`b142377`): `git show b142377:dev/gate0_tier0_result.json` →
  `{'gate': 'Gate 0 Tier 0', 'spec': 'dev/PR003_R_VAR_SELECTOR_SPEC_V2_1.md', 'OVERALL_STATUS':
  'PASS'}`. Matches `dev/PR003_RVAR_GATE0_TIER0_REPORT.md`'s claimed verdict and the commit
  message's scope statement (no `EXPLORE_POOL`/`VALIDATION_SEEDS` touched, hand-built posets
  only). **Reproducible artefact present, committed, consistent.**
- **Gate 0 Tier 1** (`55e19b8`): `git show 55e19b8:dev/gate0_tier1_result.json` →
  `total_posets_generated=382, n_empty_family=282, n_nonempty_family_tested=100, n_mismatches=0,
  n_degenerate_raw_ties=83, OVERALL_STATUS=GATE0_TIER1_PASS`. Matches
  `dev/PR003_RVAR_GATE0_TIER1_REPORT.md`'s claimed numbers exactly (independently re-verified this
  session; also cross-checked against the prior session's identical re-verification — no drift
  between the two checks). Generator script `dev/measure_pr003_rvar_gate0_tier1.py` is committed
  at the same commit, so the numbers are reproducible from a real, committed script, not asserted.
- **μ-freeze addendum content fidelity** (`0271fd9`): `git diff HEAD -- dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md`
  against the working tree is **empty** — no silent post-commit edit. Spot-checked the committed
  blob (`git show 0271fd9:dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md`) for the specific tokens comité
  018 §9.1 required: `EMPTY_FAMILY_CONVENTION := COND_ON_A(C)_NEQ_EMPTY_WITH_SEPARATE_RATE_REPORT`
  (line 31), asymmetric partition excluding root `1_000_000` (lines 124-131, 167), explicit
  root→intensity-level allocation tables (§4b), `OUT_OF_DOMAIN_UNCALIBRATED` rule frozen at the
  block level (lines 99, 170-184), `NON_CORROBORATION` tie-in for the `EMPTY_FAMILY` rate (line
  202), and the step-5 `INCONCLUSIVE`-not-`PASS` floor (line 230) — **all present, none diluted
  or silently dropped relative to comité 018's §9.1 text.**
- `README.md` contains **zero** mentions of R-VAR, μ-calibration, or Gate 0 — no published,
  user-facing claim currently rests on this work; nothing to reconcile there. All R-VAR claims
  live exclusively in `dev/` and `docs/comite/`, correctly scoped as exploratory/pre-decision.
- `make test` (sealed `.venv/bin/python -m pytest -q tests/`): **28 passed in 271.74s**, no
  failures, no skips. The sealed-path fixtures this project already claims elsewhere reproduce
  bit-exact under the pinned environment; this is the baseline the μ-freeze work must not
  perturb, and it hasn't (no file under `nachocausal/` changed).

## 5. dev/validation separation & ground-truth leakage

- No file under `nachocausal/` (the sealed package) was touched by either Gate 0 run or the
  addendum commit — confirmed via `git show <commit> --stat` for `b142377`, `55e19b8`, `6687357`,
  `6591f5f`, `0271fd9`: every touched path is under `dev/` or `docs/`.
- `EXPLORE_POOL`/`VALIDATION_SEEDS` seed status: `git status --short` shows no new artefact
  resembling a Part F execution output (no `dev/mu_freeze_table_raw.json`, no
  `gate0_tier2*`, no calibration-table file of any kind exists in the tree or in any commit
  reachable from HEAD). The only seed-touching script ever run is
  `dev/measure_pr003_rvar_gate0_tier1.py`, scoped to `EXPLORE_POOL` roots and already
  reported/committed at `55e19b8` — Part F itself has not executed. **No leakage path found; the
  hidden embedding is not implicated at all in this dev-side, order-only work.**
- The μ-freeze addendum's own text (§0, this session's revision) explicitly strikes reliance on
  the observed Tier-1 toy empty-rate as justification for its statistical-object choice, resting
  instead on the already-frozen D.3 type ordering — a textual anti-leakage discipline the auditor
  independently confirms is present in the committed blob (line ~40-46 of the committed file,
  "La justificación de este addendum... NO se apoya en la tasa observada").

## 6. Claim-boundary check

- No text audited here claims metric reconstruction, an asymptotic/global event horizon, or a
  3+1D result. `README.md` is silent on R-VAR entirely (§4), so there is no over-claim surface to
  check there.
- `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` explicitly labels the `EMPTY_FAMILY` rate
  `CLAIM-INERT`/provenance-only and ties it to the permanent `NON_CORROBORATION` clause (comité
  017 §8) — the addendum itself pre-empts the over-claim risk the falsifier flagged in comité 018
  rather than leaving it implicit.
- No abstain/`OUT_OF_DOMAIN` verdict is coerced to PASS/FAIL anywhere in the audited commits;
  `OUT_OF_DOMAIN_UNCALIBRATED` and the step-5 `INCONCLUSIVE` floor are both explicit, named,
  third states in the frozen text, not folded into a binary.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | Mechanical audit clean, seal recorded consistently | `bash .claude/skills/auditor/audit.sh` → 0 errors, 0 warnings |
| 2 | OK | Live seal matches frozen record | `make verify-seal` vs `docs/preregistration_002.md:8` |
| 3 | OK | Gate 0 Tier 0 result committed and consistent with its report | `git show b142377:dev/gate0_tier0_result.json` |
| 4 | OK | Gate 0 Tier 1 result committed and consistent with its report, independently re-verified | `git show 55e19b8:dev/gate0_tier1_result.json` |
| 5 | OK | μ-freeze addendum commit matches comité 018's required tokens verbatim, no silent deviation | `git show 0271fd9:dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md`, `git diff HEAD -- dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` (empty) |
| 6 | OK | No Part F execution artefact exists; no `EXPLORE_POOL`/`VALIDATION_SEEDS` seed touched beyond the already-reported Gate 0 Tier 1 run | `git status --short`; repo-wide search for `mu_freeze_table_raw.json`/`gate0_tier2*` (none found) |
| 7 | OK | Sealed-path test suite reproduces bit-exact under the pinned venv | `.venv/bin/python -m pytest -q tests/` → 28 passed |
| 8 | OK | No over-claim surface; `README.md` makes no R-VAR claim; addendum text itself pre-empts the `NON_CORROBORATION` over-claim risk | `README.md` (grep, no hits); `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md:202` |

AUDIT_ERRORS=0
AUDIT_WARNINGS=0

## 8. Verdict

AUDIT_VERDICT=AUDIT_PASS
