# Auditor Report 021 — truncated-futures-freeze-preflight

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/adnac/nachocausal`, branch `main`, working tree at commit `0a41358` plus an
uncommitted batch of files dated 2026-07-19. Trigger: pre-`/comite` foundation, requested
explicitly ahead of a committee deliberation on whether to authorize freezing
`docs/preregistration_square_box_truncated_futures_localization_draft.md` (the SQUARE_BOX_2P4
truncated-futures boundary-localization draft). Scope was narrowed by the calling agent to three
checks: (1) live seal vs recorded seal; (2) the evidence trail behind the cited sealed dispersion
result (`docs/new_geometry_future_observables_addendum.md`, `BH_MINK_DISPERSION_DIFFERENCE_DETECTED`);
(3) that the draft under review makes no empirical claim and does not silently modify
`nachocausal/thresholds.py` or the frozen largest-gap contract. The draft's internal statistical
design (rank formulas, sign test, `alpha`/`EFFECT_FLOOR`/`N_PAIR_MIN`/`MIN_N`) was reviewed
iteratively in the authoring session and is **not** re-litigated here.

## 2. Mechanical audit

```
$ bash .claude/skills/auditor/audit.sh
Auditor — auditing: /home/adnac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/auditor/auditor_report_015_phase1-theory-package.md,docs/auditor/auditor_report_016_phase1-provenance-reaudit.md,docs/auditor/auditor_report_017_op21-terminal-run.md,docs/auditor/auditor_report_018_op21-terminal-second-pass.md,docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md,docs/auditor/auditor_report_020_op22-bd-dossier-rev3-fix-verification.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/comite/comite_decision_027_phase1-theory-package-first-review.md,docs/comite/comite_decision_028_phase1-theory-package-second-review.md,docs/comite/comite_decision_029_phase1-theory-package-third-review.md,docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md,docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md,docs/comite/comite_decision_032_phase1-theory-closure-handoff.md,docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md,docs/comite/comite_decision_034_op21-certifier-opening.md,docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md,docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md,docs/comite/comite_decision_037_candidate-b-viability-gate-review.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/rvar_closure_negative_result.md
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
EXIT_CODE=0
```

All 22 warnings are pre-existing, committed `data/reports/*` files from earlier PR004/PR005/PR011/
present-anchor tracks, unrelated to the truncated-futures draft or the SQUARE_BOX_2P4 cluster under
review. They are noted (§7, finding 6) but are outside this audit's decision-relevant scope and
were already visible to the mechanical check before this session began.

## 3. Seal & freeze integrity

```
$ make verify-seal
thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4
$ sha256sum nachocausal/thresholds.py
6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4  nachocausal/thresholds.py
```

This matches the prereg-002 seal recorded at `docs/preregistration_003.md:9` (`6e2c3888…`) and
independently cross-referenced at `docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md:98`
and multiple `docs/hoja_de_ruta_*.md` entries — consistent, no drift. Live instrument is the one the
current prereg chain names.

`docs/estimator_v2_seal.md:7-8` records an *older* seal (`2f4c4a99…`) for `nachocausal/thresholds.py`
and explicitly states it will be superseded once prereg-002 re-freezes (`docs/estimator_v2_seal.md`,
under "VALIDATION_SEEDS — NOT prereg-002 yet"). That supersession is exactly what happened — the
live hash is the *newer* prereg-002 seal, not the estimator-v2 one. No inconsistency; this is
expected provenance, not drift.

The truncated-futures draft under review does not reference, cite, or modify
`nachocausal/thresholds.py` anywhere (`grep -c thresholds docs/preregistration_square_box_truncated_futures_localization_draft.md` = 0); its own `alpha_FWER`/`EFFECT_FLOOR`/`N_PAIR_MIN`/`MIN_N`
constants are pre-registered in the draft's prose only, not in the sealed instrument. The seal is
unaffected by, and irrelevant to, whether this draft freezes.

## 4. Reproducibility of published numbers

The draft under review contains **no empirical numeric claims** to trace — it is a pre-registration
contract, not a result. Verified: `grep -n "DETECTED\b" docs/preregistration_square_box_truncated_futures_localization_draft.md`
shows every occurrence of a `*_DETECTED` string is either (a) the cited, separately-sealed prior
result (`BH_MINK_DISPERSION_DIFFERENCE_DETECTED` at line 24, explicitly framed as "the sealed
dispersion result remains separately bounded" — not claimed by this draft) or (b) a terminal-name
*definition* within the not-yet-executed contract (§16, §16.1) — never asserted as having occurred.
The document's status lines (`grep -n "NO_DATA_GENERATED\|NO_EVALUATION_RUN\|NO_LOCALIZATION_RESULT"`)
are consistent top-to-bottom: `NO_DATA_GENERATED` at both the header (line 3) and the closing block
(lines 1137-1142), plus explicit `NO_EVALUATION_RUN` / `NO_LOCALIZATION_RESULT`.

The one number that *is* real and traced: the cited `BH_MINK_DISPERSION_DIFFERENCE_DETECTED` result
is backed by a committed evidence directory (see §5) — `evidence/new_geometry_20260719/terminal.txt`
and `RESULT_SEALED.txt` both read `BH_MINK_DISPERSION_DIFFERENCE_DETECTED`, matching the addendum's
claim (`docs/new_geometry_future_observables_addendum.md:12-18`) verbatim, and the directory
contains `per_seed_metrics.csv` (33,794 bytes) and `mink_control_metrics.csv` (17,730 bytes) —
sized consistently with real per-seed rows, not placeholders. `dev/run_new_geometry_future_observables.py:174-187`
is the committed generator this evidence traces to (`longest_chain_lengths`, the function whose
link-count convention the truncated-futures draft's §6.2 explicitly cites and verifies against).
This was not re-run (running it would consume the sealed evaluation seeds); the check here is
file-level: the evidence exists, is internally consistent, and traces to a committed script.

## 5. dev/validation separation & ground-truth leakage

The truncated-futures draft's own observation channel (§4) and repeated explicit statements
(`grep -n "r_i\b\|R_S\b"`) confine every use of hidden coordinates / `R_S` to post-selection
scoring and diagnostic sections (§9 `d_perp`/`d_ell`, §9.1 `d_edge`/`d_edge_ell`/`edge_rank`, §12
`M_s`) or to plain contract prose (geometry constants, scope text). Two explicit guardrail
sentences are present verbatim: "`Both L(i) and V(i) are order-only: neither uses coordinates,
R_S, or a kind label`" (§6.2) and "`No coordinate, r, R_S, kind label, or seed-specific outcome
enters the selection`" (§7.2). The edge-proximity diagnostic (§9.1) — the one component that does
use coordinates — is explicitly and repeatedly scoped as post-selection-only, never a selector
(§9.1, §11.4), consistent with `CLAUDE.md`'s founding rule that the hidden embedding only scores.
No leakage path found.

**Pre-existing evidence scaffold, checked for premature data (potential leak vector).**
`evidence/square_box_truncated_futures_localization_20260719/` already exists (created 2026-07-19,
predating this session's revisions) with `manifest.json`, `claim_ledger.md`, `terminal.txt`. This
was checked in full: `terminal.txt` reads `DRAFT_FOR_PI_REVIEW_NO_EVALUATION_RUN`; `manifest.json`
has `"evaluation_status": "NOT_RUN"` and no per-seed data field; `claim_ledger.md`'s "Forbidden
claims" list includes "No truncated-futures localization result exists yet" / "This draft is not
frozen." No CSV, no `evaluation_summary.json`, no `RESULT_SEALED.txt` are present in this
directory (unlike the two sibling evidence directories for the already-frozen/sealed contracts,
which do have those). This is a benign draft-stage scaffold, not premature data — no evaluation
was run, no leak occurred. It is, however, **stale**: it reflects the draft's *original*
2026-07-19 content and does not mention any of `alpha_FWER`/`EFFECT_FLOOR`/`N_PAIR_MIN`/`MIN_N`/
edge-control/synergy material added across this session's revisions (finding 5, §7).

## 6. Claim-boundary check

No text in the draft claims metric reconstruction, an asymptotic event horizon, a 3+1D result, or
a PASS coerced from an abstain state — the scope section (§1) explicitly disclaims all of these
("no global event-horizon claim," "no metric reconstruction," "no 3+1D transfer"), and this
disclaimer is unchanged from the original draft through every revision round. The cited prior
sealed result is bounded identically in its own addendum (`docs/new_geometry_future_observables_addendum.md:31-37`,
"does not localize a horizon; does not reconstruct geometry"). Consistent.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | Live `thresholds.py` seal matches the recorded prereg-002 seal; no drift | `make verify-seal`; `docs/preregistration_003.md:9` |
| 2 | OK | Cited `BH_MINK_DISPERSION_DIFFERENCE_DETECTED` result has a real, internally-consistent evidence trail matching the addendum | `evidence/new_geometry_20260719/terminal.txt`, `RESULT_SEALED.txt`; `docs/new_geometry_future_observables_addendum.md:12-18` |
| 3 | OK | Draft under review makes no empirical claim; `NO_DATA_GENERATED` consistent throughout | `docs/preregistration_square_box_truncated_futures_localization_draft.md:3,1137-1142` |
| 4 | OK | No hidden-embedding leakage into selection; coordinates/`R_S` confined to post-selection scoring/diagnostic sections | `docs/preregistration_square_box_truncated_futures_localization_draft.md:218,294` |
| 5 | WARN | `evidence/square_box_truncated_futures_localization_20260719/` scaffold (`manifest.json`, `claim_ledger.md`) is benign (no data, `NOT_RUN`) but stale relative to this session's revisions — will need the controlled update the PI already flagged as part of the (not-yet-authorized) freeze operation | `evidence/square_box_truncated_futures_localization_20260719/manifest.json` |
| 6 | WARN | Entire 2026-07-19 SQUARE_BOX_2P4 cluster — including the already-"CONTRACT FROZEN"-labeled `docs/preregistration_square_box_boundary_localization.md`, the "sealed" `docs/new_geometry_future_observables_addendum.md`, and all three `evidence/` subdirectories — remains uncommitted (`??` in `git status`) from before this session started. Text claiming "FROZEN"/"SEALED" status is not backed by a git commit; a `PREREG_002` regression stress-test of the current working tree exists nowhere in git history for this batch | `git status --short` |
| 7 | WARN | 22 pre-existing `data/reports/*.csv` files with no generator reference, flagged by the mechanical audit on every run; unrelated to this decision, not newly introduced | `bash .claude/skills/auditor/audit.sh` (§2) |

AUDIT_ERRORS=0
AUDIT_WARNINGS=24

## 8. Verdict

Everything decision-relevant for the truncated-futures freeze question checks out: the seal is
intact, the cited prior sealed result is real and matches its own addendum, the draft under review
makes no premature empirical claim, and no ground-truth leakage exists in its design. The two WARN
findings that are new to this report (5, 6) do not block the freeze decision on their own terms —
finding 5 is exactly the controlled update the PI already scoped as part of the freeze act itself,
and finding 6 (the whole cluster being uncommitted) is a pre-existing condition from before this
session, not something the truncated-futures draft introduced — but `/comite` should weigh finding
6 explicitly: an authorized "freeze" that is not also committed to git would repeat the same
non-durability gap already present across every other document in this cluster.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
