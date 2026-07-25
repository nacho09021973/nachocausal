# Auditor Report 024 — wp4-annex-c-comparable-pair-separation-precommit

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/adnac/nachocausal`, branch `main`, commit `5a53a6b` (working tree carries two
**untracked** files, the audit target). Trigger: **precommit audit** requested before the ficha's
`[PROVED]`/`[OPEN]` labels are touched, as `docs/hoja_de_ruta_24_jul_2026.md` §2.4 requires
("Cualquier resultado que emerja de (1)-(3) … debe pasar por `/auditor` antes de tocarse el estado
`[PROVED]`/`[OPEN]` de la ficha").

Target artefacts (both untracked at audit time):

- `research_program/work_packages/wp4_comparable_pair_separation.md` (285 lines) — WP4 Annex C,
  claiming to settle ingredient **(a)** of `research_program/bibliography/ficha_se_busca_tv_order_only.md`
  §7.1, i.e. `p(theta) != p(theta')`, for the WP4 §4 causal-diamond family.
- `research_program/work_packages/wp4_comparable_pair_separation_checks.py` (330 lines) — its
  verification script.

Scope hint asked specifically for: literal-output provenance of every number; honesty of the
`[PROVED]`/`[NUMERICAL]`/`[OPEN]` labels (especially Theorem C4's argued analyticity step and the
non-effective `dv_0`); whether §5's "what is NOT closed" understates the channel obstructions;
absence of over-claim toward Forma L or beyond finite-patch 1+1D; seal and dev/validation
separation untouched.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh`, exit code **0**:

```text
Auditor — auditing: /home/adnac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/auditor/auditor_report_015_phase1-theory-package.md,docs/auditor/auditor_report_016_phase1-provenance-reaudit.md,docs/auditor/auditor_report_017_op21-terminal-run.md,docs/auditor/auditor_report_018_op21-terminal-second-pass.md,docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md,docs/auditor/auditor_report_020_op22-bd-dossier-rev3-fix-verification.md,docs/auditor/auditor_report_021_truncated-futures-freeze-preflight.md,docs/auditor/auditor_report_022_freeze-commit-scoped-audit.md,docs/auditor/auditor_report_023_ficha-tv-order-only-precommit.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/comite/comite_decision_027_phase1-theory-package-first-review.md,docs/comite/comite_decision_028_phase1-theory-package-second-review.md,docs/comite/comite_decision_029_phase1-theory-package-third-review.md,docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md,docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md,docs/comite/comite_decision_032_phase1-theory-closure-handoff.md,docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md,docs/comite/comite_decision_034_op21-certifier-opening.md,docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md,docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md,docs/comite/comite_decision_037_candidate-b-viability-gate-review.md,docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md,docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md,docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_24_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/rvar_closure_negative_result.md
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

The 23 warnings are the **pre-existing mechanical baseline** of the repo (identical set to
`docs/auditor/auditor_report_023_ficha-tv-order-only-precommit.md` §2); none is attributable to
this audit's target, which adds no file under `data/`, `results/` or `outputs/`. They are carried
into the §7 counts as the audit protocol requires, but they are not findings against Annex C.

## 3. Seal & freeze integrity

| Item | Value | Anchor |
| --- | --- | --- |
| Live seal | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` | `make verify-seal` |
| Frozen record | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` | `docs/preregistration_002.md:8` |
| Drift | **none** — exact match | — |

The value also matches the seal the roadmap's own closing checklist names
(`docs/hoja_de_ruta_24_jul_2026.md` §4.2). `nachocausal/thresholds.py` is untouched: it does not
appear in `git status --short`, whose only entries are the two untracked target files. **OK.**

## 4. Reproducibility of published numbers

Method: every numeric literal with ≥4 decimal places was extracted from the note and required to
appear **verbatim** in a fresh capture of the script's stdout.

- Script re-run twice from a clean shell: exit `0` both times, and the two captures are
  **byte-identical** (`diff -q` → no differences), so the seeded MC in check [4] is genuinely
  deterministic as §7 of the note claims.
- 13 literals with ≥5 decimals + the ≥4-decimal sweep: **all matched except four**, of which three
  are real provenance gaps (finding 1) and one is a precision overstatement (finding 4).
- The §6 table (`0.500591097337296`, `0.500705392489878`, `+1.142952e-04`, `+1.199901e-04`,
  `0.548382340298801`, `0.547994788251956`, `-3.875520e-04`, `+2.399802e-02`) and the Kendall
  values (`0.001182194675`, `0.001410784980`) are **all literal script output** (check [9]). **OK.**

**Finding 1 (ERROR) — three load-bearing numbers have no committed generator.** At
`research_program/work_packages/wp4_comparable_pair_separation.md:213-214`, §5 item 1 cites
`V(1.2) = 10.7943…` at `dv = 4`, and `0.049968…` / `0.049922…` at `dv = 0.02`. None appears in the
script's output. The script prints `A_tot` only inside check [4], and only for `tau = 1.0` and
`tau = 2.5` at `dv = 4` (`checks.py:296-297`), so `V(1.2)` and both `dv = 0.02` volumes are
emitted nowhere. The generating function `area_sub` **is** committed (`checks.py:67,123`), but it is
never exercised at those arguments with printed output — i.e. a reader following the note's own
reproduction instruction (§7, the single script command) cannot obtain these digits. The note
compounds this by representing its numbers as script-derived ("Full output: check [9] of the
script", `:250`). These three values are load-bearing: they are the entire quantitative support for
§5 item 1, which is the note's central honesty argument (the cardinality confounder that blocks
Forma L). Graded ERROR rather than WARN because the affected claim is load-bearing *and* the note
misrepresents its provenance; the fix is small (emit `V(tau)` for the cited configurations) and is
the user's to apply. Mitigating, but not exculpating: the *qualitative* claim that `V` depends on
`tau` is independently established by two numbers that **are** in the output
(`A_tot = 11.501608` at `tau = 1.0` vs `6.583486` at `tau = 2.5`), so the argument of §5 item 1
survives; only the specific cited digits are unbacked.

**Independent verification performed by this audit** (not merely re-reading the script's own
self-checks):

- *Control A — ordering logic.* Uniform measure on a product null box must give `p = 1/2` exactly.
  Measured `0.499736 ± 0.000500` over 2·10⁶ points → 0.53σ. The comparability test used in check
  [4] is correct.
- *Control B — the relation is a partial order.* On 2874 in-diamond points the relation built from
  `(Utilde, v)` is transitive and antisymmetric (explicit matrix check). Confirms §2's "the causal
  order is the product order" as implemented.
- *Control C — the reduction itself (Props C2/C3).* An independent-pair Monte-Carlo estimator (each
  sampled point used once, separate RNG stream, seed 11) converges onto the quadrature value:
  `0.550617 ± 0.001847` (1.21σ), `0.547664 ± 0.000583` (1.23σ), `0.548485 ± 0.000292` (**0.35σ**)
  at 1.45·10⁵ / 1.46·10⁶ / 5.82·10⁶ retained points against quadrature `0.548382`. The 4-fold →
  2-fold reduction is corroborated independently of the script.
- *Lemma C1* is verified symbolically (residual exactly `0`) and against direct quadrature. **OK.**

**Finding 4 (WARN) — precision overstated by rounding.** `…separation.md:98` says Lemma C1 agrees
with direct quadrature "to `1.1e-15`"; the script prints `|diff| = 1.11e-15`. The stated bound is
*tighter than the measured value*. Trivial, but it is a number in a doc that is not the literal
output, in the direction of flattering the result.

**Finding 5 (WARN) — un-backed historical number.** `…separation.md:110-112` recounts that an
earlier draft of the MC "disagreed with the quadrature at 78 sigma before being fixed". This audit
confirms the bug was real and the diagnosis correct (interior rays descend in `v`, so
`min_D r = r_q`; the WP4 source states this at `wp4_fisher_localization_floor.md` §4, "its minimal
`r`-value over the closed box is `r_q > 0`"). But `78` is not reproducible from the repo as
committed — it is a number from a discarded intermediate state. Non-load-bearing and transparently
framed as history; flagged for completeness rather than as a defect of the result.

## 5. dev/validation separation & ground-truth leakage

- **No contact with the sealed path.** `checks.py` imports exactly `numpy`, `sympy`,
  `scipy.special.lambertw` (`checks.py:32-34`). It imports nothing from `nachocausal/`, references
  no threshold, no seed band, no `dev/` path, no generator, no estimator, and writes no file. Grep
  for `nachocausal|thresholds|seed_band|dev/` over the script returns only the docstring sentence
  disclaiming such use.
- **No validation artefact produced.** The target adds no file under `data/`, `results/`,
  `evidence/` or `outputs/`; `git status --short` shows only the two untracked target files.
- **Ground-truth leakage: not applicable in the strict sense, and clean in spirit.** There is no
  hidden embedding and no observable here: the object is a closed-form functional of the *continuum*
  copula, computed analytically. No estimator is defined, tuned or scored, so the
  "hidden-embedding-only-scores" rule has no surface to be violated on. The one adjacent risk —
  an order-only statistic that secretly reads the scale parameter — is explicitly tested and
  **passes**: check [6] confirms `p` is invariant under the joint dilation to `< 1e-15`
  (`6.66e-16`, `5.55e-16`, `1.11e-16`), i.e. the statistic cannot separate a Theorem-A scale-orbit
  pair. That is the ficha §4 mandatory orbit test, and it is the correct direction of caution.
- **Pause discipline.** The work is a calculation, which is what `docs/hoja_de_ruta_24_jul_2026.md`
  §2.1 authorises ("no una ejecución ni una implementación de estimador"). None of the roadmap §3
  "No hacer" items is breached: `dev/pr011_tv_certification_enumeration.py` was not run, no
  threshold touched, no `/comite` convened, and — see finding 2 — the ficha's status labels have
  **not** yet been edited, which is precisely the ordering §2.4 demands. **OK.**

## 6. Claim-boundary check

The note is, if anything, unusually restrictive rather than over-claiming:

- Forma L is labelled `[OPEN]` in the status table (`:275`) and denied in the headline
  ("It does **not** close Forma L", `:22`) and in §5's heading (`:208`).
- No metric-reconstruction, asymptotic-horizon or 3+1D claim. §5 "Also not claimed" (`:239-245`)
  explicitly disclaims the 3+1D Schwarzschild pairs of FWP §2 / OP-1.2, disclaims global
  monotonicity in `tau`, and states that nothing touches the sealed prereg-002 result, the C1–C6
  negative ledger, or the programme's pause.
- No PASS/verdict language is coerced from anything; no verdict token is emitted at all.
- §5's four-item obstruction list does **not** understate the channel problem. It correctly
  identifies the decisive one — Reitzner–Schulte's CLT lives in the *unconditioned Poisson* channel
  where the `tau`-dependent `V(tau)` lets the `N`-marginal separate on its own (ficha §1.2, §9.2) —
  and adds the de-Poissonisation gap for `fixed_n`, the uncomputed variance non-degeneracy
  (`zeta_1`), and the fact that ficha §6.4's consistency check passes only at the level of *rates*
  with the constant-level comparison (`kappa*dv` vs `sqrt(zeta_1*Ibar)`) not performed for want of
  `Ibar` at these corners. This audit finds no obstruction omitted from that list.
- The claim actually made — a scalar copula functional separates `tau` on one named finite 1+1D
  patch family — sits inside the finite-patch 1+1D localisation boundary. **OK.**

Two label-honesty defects, both in the area the scope hint asked to be scrutinised:

**Finding 2 (WARN) — the count of argued-but-unwritten steps is understated.** §6's label reads
"`[PROVED (leading order)]`, with **the single step** noted in §4 (analyticity of `p` in `dv` at
`0^+`) argued rather than written out" (`:270-272`). But Corollary C6's proof contains a *second*
such step: "the remainder is `O(dv^2)` **uniformly in `tau`** over the compact `[tau_0, tau_1]` (the
expansion's coefficients are continuous in `tau` there)" (`:189-190`). Continuity of each
coefficient does not by itself deliver a uniform remainder bound; that needs joint control (e.g.
analyticity in `(dv, tau)`). The step is plausible and is at least *stated* in the proof, so this is
a miscount in the label, not a hidden gap — but "the single step" should read "the two steps". The
non-effectivity of `dv_0` **is** properly disclosed, twice (`:197-199`, `:271-272`); on that half of
the scope hint the note is clean.

**Finding 3 (WARN) — quantifier slip in Corollary C6.** The corollary reads "For each admissible
corner pair `(r_p, r_q, dv)` there is `dv_0 > 0` such that for all `0 < dv < dv_0` …" (`:180-182`),
which quantifies `dv_0` over `dv` itself. As intended (and as the proof actually supports), `dv_0`
depends on `(r_p, r_q, tau_0, tau_1)` only. A drafting error inside a `[PROVED]`-labelled statement,
hence worth fixing before the ficha cites it.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | ERROR | Three load-bearing numbers (`V(1.2)=10.7943…`, `0.049968…`, `0.049922…`) are emitted by no committed script; the note nonetheless presents its numbers as script-derived | `wp4_comparable_pair_separation.md:213-214` vs `..._checks.py:296-297`; `grep -F` over fresh stdout capture |
| 2 | WARN | Label says "the single step" argued-not-written, but Corollary C6 adds a second (uniformity in `tau` of the `O(dv^2)` remainder) | `wp4_comparable_pair_separation.md:270-272` vs `:189-190` |
| 3 | WARN | Corollary C6 quantifies `dv_0` over `dv` itself; should depend on `(r_p, r_q, tau_0, tau_1)` only | `wp4_comparable_pair_separation.md:180-182` |
| 4 | WARN | Lemma C1 agreement stated as "to `1.1e-15`"; script prints `1.11e-15` — stated bound tighter than measured | `wp4_comparable_pair_separation.md:98` vs check [3] |
| 5 | WARN | "78 sigma" historical figure from a discarded draft is not reproducible from the repo (non-load-bearing, framed as history) | `wp4_comparable_pair_separation.md:110-112` |
| 6 | WARN ×23 | Pre-existing mechanical baseline: committed data files under `data/reports/`, `evidence/` with no generator reference — **not attributable to this target** | `bash .claude/skills/auditor/audit.sh` (§2) |
| 7 | OK | Seal matches the frozen record exactly; `thresholds.py` untouched | `make verify-seal`; `docs/preregistration_002.md:8` |
| 8 | OK | Script deterministic: two runs byte-identical, exit 0 both times | `diff -q` over two stdout captures |
| 9 | OK | §6 table, Kendall values and check [7b] column are literal script output | `wp4_comparable_pair_separation.md:252-263` |
| 10 | OK | Reduction (Props C2/C3) independently corroborated: 0.35σ at 5.82·10⁶ points, separate RNG stream | audit Control C |
| 11 | OK | Ordering logic independently corroborated: uniform null box gives `0.499736 ± 0.000500` vs exact `1/2`; relation verified transitive + antisymmetric | audit Controls A, B |
| 12 | OK | No contact with sealed path: imports only numpy/sympy/scipy; no threshold, seed band, `dev/` path or validation artefact | `..._checks.py:32-34`; `git status --short` |
| 13 | OK | Orbit test passes to `< 1e-15`; statistic provably cannot separate a Theorem-A scale-orbit pair | check [6] |
| 14 | OK | No over-claim: Forma L `[OPEN]`, no reconstruction / 3+1D / asymptotic-horizon claim, prereg-002 explicitly untouched | `wp4_comparable_pair_separation.md:22,208,239-245,275` |
| 15 | OK | §5's obstruction list omits no channel obstruction this audit could identify | `wp4_comparable_pair_separation.md:208-238` |
| 16 | OK | Ficha status labels not yet edited — correct ordering per roadmap §2.4 | `git status --short` (ficha not modified) |

AUDIT_ERRORS=1
AUDIT_WARNINGS=27

## 8. Verdict

The mathematics survived every independent check this audit could mount: the reduction, the
ordering logic, the orbit test, determinism, and the seal are all sound, and the note's restraint
about what remains open (§5) is accurate and complete. The single ERROR is a **provenance** defect,
not a mathematical one — three cited volume values that no committed script emits, in a note that
tells the reader all its numbers come from one script. Repo discipline is explicit that a number
without a committed generator is not a result, so this cannot be waived; it is also cheap to
remediate (print `V(tau)` for the cited configurations and re-run), after which findings 2–5 are
one-line textual fixes.

Recommendation to the PI: **fix findings 1–4, re-run the script, and re-audit before the ficha's
`[OPEN por par]` label is changed.** Finding 5 may be left as-is or attributed. The auditor applies
none of this. Until finding 1 is closed, the note should not be cited as the backing for a ficha
status change, and no `/comite` should be convened on top of it.

AUDIT_VERDICT=AUDIT_FAIL
