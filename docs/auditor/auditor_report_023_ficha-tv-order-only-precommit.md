# Auditor Report 023 — ficha-tv-order-only-precommit

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

- **Target:** `research_program/bibliography/ficha_se_busca_tv_order_only.md` (v2, 2026-07-24),
  **untracked, pre-first-commit** (`git status --short` → `?? research_program/bibliography/
  ficha_se_busca_tv_order_only.md`; only entry). A bibliographic-search specification for
  order-only TV identifiability; contains no new results, only attributions to internal sources
  and desiderata.
- **Repo state:** branch `main`, commit `01698c3630e98a704beaf8f8e4b3079b4a2733ab`, working tree
  otherwise clean.
- **Trigger:** PI request — audit the ficha before its first commit. Specific charges: (a) every
  attribution to WP4 / `first_witness_pair_candidates.md` (FWP) / OP-1.2 / PR012 reflects the
  literal status in the source (PROVED / NUMERICAL / prose / OPEN / dry-run); (b) no partial
  result promoted to theorem; (c) cited numbers (PR011 `0.009223798457`; PR012 `<= 0.0133`;
  `kappa ~ 8e-4`; `~35 ell`) match sources; (d) no over-claim beyond finite-patch 1+1D
  localisation.
- **Sources read in full this session:** `research_program/work_packages/
  wp4_fisher_localization_floor.md`, `research_program/models/first_witness_pair_candidates.md`,
  `research_program/synthesis/op12_tv_zero_3p1.md`,
  `research_program/synthesis/pr012_tv_curve_scope.md`.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh` — exit code `0`. Verbatim output:

```text
Auditor — auditing: /home/adnac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/auditor/auditor_report_015_phase1-theory-package.md,docs/auditor/auditor_report_016_phase1-provenance-reaudit.md,docs/auditor/auditor_report_017_op21-terminal-run.md,docs/auditor/auditor_report_018_op21-terminal-second-pass.md,docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md,docs/auditor/auditor_report_020_op22-bd-dossier-rev3-fix-verification.md,docs/auditor/auditor_report_021_truncated-futures-freeze-preflight.md,docs/auditor/auditor_report_022_freeze-commit-scoped-audit.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/comite/comite_decision_027_phase1-theory-package-first-review.md,docs/comite/comite_decision_028_phase1-theory-package-second-review.md,docs/comite/comite_decision_029_phase1-theory-package-third-review.md,docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md,docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md,docs/comite/comite_decision_032_phase1-theory-closure-handoff.md,docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md,docs/comite/comite_decision_034_op21-certifier-opening.md,docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md,docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md,docs/comite/comite_decision_037_candidate-b-viability-gate-review.md,docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md,docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md,docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/rvar_closure_negative_result.md
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
WARN: committed data file with no generator reference: evidence/new_geometry_20260719/mink_control_metrics.csv
----------------------------------------
Auditor: 0 error(s), 23 warning(s)
```

All 23 warnings are pre-existing, repo-wide heuristic warnings (data files without an in-tree
generator *reference*, a known recurring finding of prior reports); none involves the audited
file or is caused by it.

## 3. Seal & freeze integrity

- `make verify-seal` →
  `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`,
  exit 0.
- Frozen record match: `docs/preregistration_002.md:8` records exactly
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`. **No drift.**
- The audited ficha does not touch `nachocausal/thresholds.py`, any frozen doc, or any code path
  (`git status --short` shows the ficha as the only change, untracked).

## 4. Reproducibility of published numbers

Every number the ficha cites, traced to its source and (where applicable) its committed artifact:

| Ficha claim (line) | Source anchor | Verified |
| --- | --- | --- |
| PR011 published naive bound `epsilon = 0.009223798457` at `n=8`, `delta_tau=0.1` (ficha:118) | `research_program/synthesis/pr012_tv_curve_scope.md:96,131`; **committed artifact** `data/reports/pr011_tv_certification_n8.csv` row: `HELLINGER_FALLBACK,8,0.95,1.05,0.009223798457,…` (`tau_a=0.95, tau_b=1.05` ⟹ `delta_tau=0.1`), with sha256 sidecar `data/reports/pr011_tv_certification_n8.sha256` | ✔ bit-exact |
| PR012 tensorized preview `<= 0.0133` (ficha:120) | `pr012_tv_curve_scope.md:133` max certified `epsilon = 0.013307085972` at `delta_tau=0.4`; ficha correctly labels it **dry-run preview, not published, gate G2b open** (`pr012_tv_curve_scope.md:123-124,183`) | ✔ value; see Finding 2 for scope wording |
| minimax floor `~0.49–0.50` (ficha:120-121) | `pr012_tv_curve_scope.md:139` ("every minimax floor is still ≈0.49-0.50") | ✔ |
| `kappa ~ 8e-4`, `delta_tau ~ 35 ell` (ficha:111), tagged `[NUMERICAL, no probado]` | `wp4_fisher_localization_floor.md:374` (`kappa ~= 7.97e-4`, `delta_tau/ell ~= 35.4`; generator `research_program/work_packages/wp4_kappa_numeric_reference.py`, committed; WP4 itself labels it NUMERICAL, not proved, wp4:357) | ✔ rounding fair, tag preserved |
| empirical `kappa ~ lambda^6` reshaping (ficha:112) | `wp4_fisher_localization_floor.md:382` ("empirical power law", exponent 5.9–6.0), labeled NUMERICAL in both | ✔ |

No number in the ficha lacks a committed source; the only unpublished figure (PR012 preview) is
explicitly labeled as such.

## 5. dev/validation separation & ground-truth leakage

Not implicated: the ficha is a `research_program/bibliography/` document with no code, no seeds,
no estimator, no threshold, no reference to the hidden embedding. It cites `dev/` nowhere. It
introduces no path from exploration into the sealed instrument. `git status` confirms no other
file changed. **OK.**

## 6. Claim-boundary check

- The ficha claims no new mathematics as established: internal results carry the source's own
  status labels (`[PROVED]`, `[NUMERICAL, no probado]`, `[PROSE-REMARK, promoción pendiente]`,
  `[OPEN]`, `PUBLICADO`/`DRY-RUN PREVIEW` — ficha:96-127), verified against the literal source
  texts (FWP:12-14,86; wp4:15-24,357; PR012:4,123-124,183).
- No 3+1D over-claim: the only 3+1D statements are attributed to OP-1.2 within its own scope
  (mass orbit at `fixed_n`, order+number separation — ficha:113-116 vs `op12_tv_zero_3p1.md:71-79,
  114-123`, including "identifica `rho*M^4`, no separa `rho` de `M`", op12:123).
- The rigidity remark is **not** promoted: ficha:100-104 states it is prose inside FWP §4's
  Attempt C analysis with promotion pending, exactly matching `first_witness_pair_candidates.md:
  199-207` and `pr012_tv_curve_scope.md:46-52,191-193`.
- The ficha's own §9.2 (ficha:390-401) forbids reading PR011/PR012 numerics as an asymptotic
  theorem and labeled-level bounds as quotient lower bounds — the audit confirms the body obeys
  its own rules, with the one wording exception in Finding 2.
- `R19` appears nowhere in the document (grep: no match). `N_A` appears only inside the
  delimited motivational note (ficha §1.5), marked "NO bibliográfica, NO antecedente del repo",
  claiming no scientific role — as directed.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | All internal attributions match the literal status in WP4/FWP/OP-1.2/PR012; all four charged numbers verified, one to its committed artifact bit-exact | §4 table; §6 |
| 2 | WARN | Ficha:119-121 summarizes PR012 as "cotas tensorizadas `<= 0.0133` **en todo el rango** `delta_tau <= 0.4`" y "suelo minimax ~0.49–0.50 **en toda la familia congelada**": silently drops the two `GRID_RESOLUTION_ABSTAIN` ladder points (`delta_tau = 0.0125, 0.025`, `pr012_tv_curve_scope.md:128-129`), which have **no** certified bound. PR012:70 requires abstain rows "never silently dropped". Wording should scope the claim to the four certified points | ficha:119-121 vs `pr012_tv_curve_scope.md:70,128-129` |
| 3 | WARN | Inline elementary statistical claims stated without citation or `[UNVERIFIED]` marker: deficiency bridge `TV(Q) >= TV(P) - 2*delta` (ficha:167); labeled-pair separation `TV(P^n) -> 1` for the Theorem A pair, which also uses the unstated premise `P != Phi_s(P)` mod null sets for `s != 1` (ficha:216); two-moment bound `TV >= 1 - 8*sigma^2/Delta_mu^2` (ficha:260); Gaussian triangle bound (ficha:262-265). Auditor re-derived all four and found them **correct** (midpoint Chebyshev with tail `4*sigma^2/Delta_mu^2` per side; two-hypothesis testing risk `1-TV` shifted `<= 2*delta` under deficiency `delta`; TV triangle inequality; a compact patch with `r` bounded away from 0 cannot be `Phi_s`-invariant for `s != 1`). Per the founding rule (claims carry backing or `[UNVERIFIED]`), each should carry a one-line derivation note or a citation (e.g. Tsybakov §2.4, already in the ficha's own table as `UNVERIFIED` standard) | ficha:167,216,260-265; founding rules `CLAUDE.md` |
| 4 | WARN | Label inconsistency in the ficha's own state system: ficha:246 tags the Malliavin–Stein genre `[CONFIRMED_TOOL_ONLY como género…]` while ficha:352 defines `CONFIRMED_TOOL_ONLY` as "leída/verificada localmente" and the corresponding table row (ficha:366, Last–Penrose) correctly says `POSSIBLE_BRIDGE`/`UNVERIFIED` local. Same family: Kleitman–Rothschild row (ficha:371) uses `NOT_APPLICABLE`, defined at ficha:354 as "revisada", though KR is memory-cited (its "3 niveles" characterization is locally unverified) | ficha:246,352,354,366,371 |
| 5 | OK | Seal intact and matching the binding freeze record; audited file touches no frozen artifact | §3; `make verify-seal`; `docs/preregistration_002.md:8` |
| 6 | OK | No dev/validation implication, no ground-truth reference, no claim-boundary violation, no `R19`, `N_A` properly quarantined | §5, §6 |
| 7 | WARN ×23 | Pre-existing repo-wide `audit.sh` warnings (committed data files without generator reference), unrelated to and unaffected by the audited file; carried in the count per skill rule | §2 verbatim output |

AUDIT_ERRORS=0
AUDIT_WARNINGS=26

## 8. Verdict

`AUDIT_PASS_WITH_WARNINGS` — 0 errors; 26 warnings (23 pre-existing mechanical, repo-wide;
3 specific to the ficha, all wording/labeling precision, none a fabricated or misattributed
result). The three ficha-specific warnings (Findings 2–4) are each fixable with a line-level
edit before commit; none blocks the document's function as a search specification.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
