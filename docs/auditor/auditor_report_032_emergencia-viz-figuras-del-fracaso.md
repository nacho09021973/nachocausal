# Auditor Report 032 — emergencia-viz-figuras-del-fracaso

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/ignac/nachocausal`, branch `emergencia/p1a-canal-sigma-m`, commit `c87d302`
(`viz: seis figuras del fracaso de P1a, sobre los artefactos sellados`), pushed to
`origin/emergencia/p1a-canal-sigma-m`. Working tree clean at audit time (`git status --short`
empty).

Scope hint given by the user: the six new figures in `emergencia/viz/` — scripts, `README.md`,
committed PNGs — plus §22 appended to `emergencia/HOJA_DE_RUTA.md`. Trigger: routine post-commit
integrity check of newly published material.

Audited artefacts (11 added files + 1 modified):

```text
emergencia/viz/{README.md,datos.py,estilo.py,hacer_figuras.py}
emergencia/viz/fig0{1..6}_*.py
emergencia/viz/output/fig0{1..6}_*.png
emergencia/HOJA_DE_RUTA.md  §22 (added)
```

The figures make no new scientific claim: they are read-only renderings of sealed artefacts under
`emergencia/resultados/`. The audit therefore targets (a) whether every drawn number is the
literal output of a committed deterministic path, (b) whether the constants they assert match the
frozen contracts they cite, and (c) whether the accompanying prose over-claims.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh` — exit code `0`.

```text
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/auditor/auditor_report_015_phase1-theory-package.md,docs/auditor/auditor_report_016_phase1-provenance-reaudit.md,docs/auditor/auditor_report_017_op21-terminal-run.md,docs/auditor/auditor_report_018_op21-terminal-second-pass.md,docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md,docs/auditor/auditor_report_020_op22-bd-dossier-rev3-fix-verification.md,docs/auditor/auditor_report_021_truncated-futures-freeze-preflight.md,docs/auditor/auditor_report_022_freeze-commit-scoped-audit.md,docs/auditor/auditor_report_023_ficha-tv-order-only-precommit.md,docs/auditor/auditor_report_024_wp4-annex-c-comparable-pair-separation-precommit.md,docs/auditor/auditor_report_025_wp4-annex-c-remediation-reaudit.md,docs/auditor/auditor_report_026_wp4-annex-c-variance-addendum-precommit.md,docs/auditor/auditor_report_027_wp4-ibar-interval-design-precommit.md,docs/auditor/auditor_report_028_wp4-ibar-executable-contract-precommit.md,docs/auditor/auditor_report_031_p1a-seccion-13-certificado-familia-prescrita.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/comite/comite_decision_027_phase1-theory-package-first-review.md,docs/comite/comite_decision_028_phase1-theory-package-second-review.md,docs/comite/comite_decision_029_phase1-theory-package-third-review.md,docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md,docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md,docs/comite/comite_decision_032_phase1-theory-closure-handoff.md,docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md,docs/comite/comite_decision_034_op21-certifier-opening.md,docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md,docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md,docs/comite/comite_decision_037_candidate-b-viability-gate-review.md,docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md,docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md,docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md,docs/comite/comite_decision_045_candidate-7-1-fixed-n-logical-status.md,docs/comite/comite_decision_046_weyl-level-sheet-page-shoom-adjudication.md,docs/comite/comite_decision_047_phase2-b2-documentation-publication.md,docs/comite/comite_decision_048_q-fmots-target-adjudication.md,docs/comite/comite_decision_049_program-closure-adjudication.md,docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_24_jul_2026.md,docs/hoja_de_ruta_25_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jul_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/manuscript_limits_draft.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/program_closure_note_2026-07-30.md,docs/rvar_closure_negative_result.md
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

All 23 warnings are **pre-existing and outside the audited scope** (`data/reports/`,
`evidence/`); none is attributable to `c87d302`. They are carried into the counts of §7 as the
skill requires, but they are not findings of this audit. The audited paths produced **no**
mechanical warning: `emergencia/viz/output/*.png` is not gitignored-but-tracked
(`git check-ignore` returns nothing) and carries a generator reference in
`emergencia/viz/README.md` and `emergencia/viz/hacer_figuras.py`.

## 3. Seal & freeze integrity

```text
$ make verify-seal
thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4
```

Matches the frozen SHA named in `docs/preregistration_002.md:8` and `docs/preregistration_003.md:9`.
**No drift.** The audited commit touches no file under `nachocausal/`: `git show --stat c87d302`
lists only `emergencia/viz/*` and `emergencia/HOJA_DE_RUTA.md`. Seal integrity `OK`.

## 4. Reproducibility of published numbers

**4.1 The committed PNGs are the literal output of the committed scripts.** Re-ran
`PYTHONDONTWRITEBYTECODE=1 python3 emergencia/viz/hacer_figuras.py` at `c87d302` with a clean
tree and compared against the hashes recorded before the run:

```text
emergencia/viz/output/fig01_disponibilidad.png: OK
emergencia/viz/output/fig02_el_gate.png: OK
emergencia/viz/output/fig03_canal_sigma_m.png: OK
emergencia/viz/output/fig04_anatomia_del_error.png: OK
emergencia/viz/output/fig05_seleccion_y_estabilidad.png: OK
emergencia/viz/output/fig06_mapa_del_fracaso.png: OK
```

Six of six byte-identical. The `README.md` claim "dos ejecuciones dan ficheros byte a byte
idénticos (verificado)" holds.

**4.2 The SHA-256 guardrail fires.** Independently re-verified, not taken on the author's word:
copying `p1a_representaciones_metricas_d2.csv` with a single appended space and repointing
`datos.RESULTADOS` at the copy makes `datos.leer` raise `ValueError` instead of producing a
figure (`GUARDARRAIL_FIRES=YES`). `emergencia/viz/datos.py:42-59`. A guardrail that cannot fail
is decoration; this one can.

**4.3 Recomputed quantities agree with the audited executables.** `datos.anova_sigma_m`
(`emergencia/viz/datos.py:77-122`) recomputes `SST = SSB + SSW` on the observations rather than
imposing it, and refuses to draw if the resulting `rho_max` misses the value printed by
`emergencia/p1a_count_volume_canal_sigma_m_d2.py` by more than `1e-4`. Independently re-ran that
executable: `rho_max_emp = 0.5315`–`0.5681`, `BLOQUE_A_CONSISTENCIA = PASS`, matching the six
values hardcoded as controls in `datos.py:30-34`.

**4.4 Every numeric claim in §22 and `viz/README.md` traced.** All recomputed from the sealed
CSVs in this audit:

| Claim | Location | Verified value |
| --- | --- | --- |
| `SSW/SST = 0.68–0.72` | §22.1, README | `0.6773`–`0.7175` |
| `rho_max = 0.531–0.568` | §22.1, README | `0.53147`–`0.56806` |
| mejor `rho = 0.566` | §22.1, README | `0.566436` (`COUNT_VOLUME`, n=64 futuro) |
| `0.27 → 0.47 → 0.57` | §22.3, README | `0.2686 / 0.4658 / 0.5664` (máximos) |
| holgura de `B_n` `×2.26–2.55` | §22.3 | `2.2637`–`2.5519` |
| enriquecimiento `×1.52` … `×2.47` | §22.3 | `1.52375` (n=32) … `2.47355` (n=128) |
| discrepancia exacta/MC `0.0018` | §22.2 | `0.00182822` |
| disponibilidad `0.697` a `n=128` | §22.1, fig01 | `0.696583` |
| factor máx. apriete `×1.000017` | fig04, fig06 | reproducido por `p1a_count_volume_techo_apriete_d2.py` |
| `B_n` por estrato | `fig04:40-44` | reproducido por el mismo ejecutable |
| coincidencia entre selectores `= 0` a `n ≥ 96` | §22.1 | `0.0` en las tres parejas |

No number in the audited material lacks a committed generator.

**4.5 Constants that are asserted, not recomputed — one is wrong.** See §6 finding 1: the
`0.30` line drawn on the correlation axis of `fig02` does not exist as a correlation threshold in
either governing contract.

## 5. dev/validation separation & ground-truth leakage

**Separation `OK`.** Nothing in `emergencia/viz/` imports from `dev/`, writes to
`emergencia/resultados/`, or touches `nachocausal/thresholds.py`. The whole module is read-only
over already-sealed artefacts; `git show --stat c87d302` confirms no sealed artefact was modified.

**Seed band `OK`.** The suite contains exactly one RNG call,
`emergencia/viz/fig03_canal_sigma_m.py:45`, `np.random.default_rng(20260807)`, used solely for
horizontal jitter on a discrete axis. `20260807 ∉ [2000000, 2999999]`, so the reserved virgin band
recorded in `docs/program_closure_note_2026-07-30.md:136` and
`docs/program_reopening_note_2026-08-05_R3.md:9` is not consumed. The jitter affects only point
placement within `±0.30` of the integer `m`; no reported quantity depends on it.

**Ground-truth leakage `OK`.** `latent_duration` — the hidden embedding — appears exactly once,
at `emergencia/viz/datos.py:94`, as the *response* of the ANOVA and of the correlations. Every
predictor is observable (`interval_size` at `datos.py:95`, `estimate_count_volume` at
`datos.py:119`). No figure uses ground truth to define, select or guide an observable: it only
scores. This is the correct side of the rule.

## 6. Claim-boundary check

**No over-claim of recoverability or reconstruction.** A scan for `reconstru|recuperabilidad|
recovers|3+1|asintotic` over the audited files returns two hits, both negations:
`emergencia/viz/hacer_figuras.py:11` ("no se afirma recuperabilidad en ninguna parte") and
`emergencia/viz/README.md:5` ("NO AFIRMA RECUPERABILIDAD"). Nothing in the material asserts
metric reconstruction, an asymptotic horizon, or `d>=3`.

**The population/finite-sample boundary is stated correctly.** `viz/README.md` and §22.4 both say
`rho_max = sqrt(SSB/SST)` is a finite-sample identity over the sealed sample and that the
population statement remains `STRONGLY_SUPPORTED_UNDER_IID_NOT_CLOSED_FORM_THEOREM`. No figure
claims more.

**Finding 1 — ERROR. `fig02` draws a threshold that the frozen contracts do not state for that
quantity.** `emergencia/viz/fig02_el_gate.py:69-70` draws a dashed line at `0.30` on the
**correlation** axis, labelled at `:75-77` "umbral fuerte secundario 0.30";
`emergencia/viz/datos.py:25` declares it `UMBRAL_FUERTE = 0.30  # umbral "fuerte" secundario del
mismo contrato`. In both governing contracts, `0.30` bounds the **median absolute relative
error**, not the correlation:

- `emergencia/P1a_contrato_gate_altura_duracion_lex_d2.md:184-185` —
  `bootstrap95_lower(cor(...)) >= 0.80`, `bootstrap95_upper(mediana error relativo absoluto) <= 0.30`.
- `emergencia/P1a_contrato_representaciones_alternativas_d2.md:145-146,156-157` — same pair, and
  the **parking** rule on the correlation axis is `bootstrap95_upper(correlacion) < 0.50`.

The correlation-axis threshold is therefore `0.50`, not `0.30`, and
`emergencia/P1a_resultados_gate_altura_duracion_lex_d2.md:119-120` says so in words: "también por
debajo del umbral fuerte de aparcamiento `0.50`". The error is **material, not cosmetic**: with
the correct `0.50` line, `HEIGHT_WIDTH` (upper bounds `0.3914`–`0.4838`) falls entirely below it
and `COUNT_VOLUME` (`0.5453`–`0.5824`) does not — which is exactly the terminal distinction the
sealed results record (`HEIGHT_WIDTH_STRONGLY_PARKED = TRUE` /
`COUNT_VOLUME_STRONGLY_PARKED = FALSE`, `P1a_resultados_representaciones_alternativas_d2.md`
§5–§6). As drawn, the figure erases that distinction and instead suggests `HEIGHT_WIDTH` clears a
secondary threshold it was never measured against.

**Finding 2 — WARN. `datos.py` cites the wrong governing contract for `fig02`.**
`emergencia/viz/datos.py:22-25` attributes both constants to
`emergencia/P1a_contrato_gate_altura_duracion_lex_d2.md`, the *height-gate* contract. `fig02`
plots the *alternative-representations* experiment, governed by
`emergencia/P1a_contrato_representaciones_alternativas_d2.md`. The `0.80` happens to be identical
in both (`:146`), so no drawn number is wrong on this account, but the citation does not lead a
reader to the contract that actually governs the figure — and it is what allowed finding 1 to
pass unnoticed.

**Finding 3 — WARN. An interpretive claim is asserted as fact without its backing.**
`emergencia/viz/README.md` (§"Dos precisiones") and `HOJA_DE_RUTA.md` §22.4 state that the
`<=0.0007` of `P1a_count_volume_canal_sigma_m_d2.md` is "la misma comparación **con la corrección
intrabin del Bloque B**, es decir poblacional". The source document does not say this:
`emergencia/P1a_count_volume_canal_sigma_m_d2.md:197-199` calls it, without qualification, "la
ganancia de la regresión saturada sobre `m` respecto de `COUNT_VOLUME` … de `-0.0001` a
`+0.0007`". The claim is *reconstructible* and this audit reconstructed it — `sqrt(1-T_corr) -
rho_obs` over the six strata gives `-0.000045`…`+0.000703`, matching the document's range at its
printed precision in all six — but neither the README nor §22.4 cites that reconstruction, so a
reader cannot check the assertion from what is written. Per the founding rule the claim needs its
anchor or an `[UNVERIFIED]` mark. (Note for the record, outside this scope: the exact
finite-sample gain is `0.0015`–`0.0026`, so the sealed document's §6.2 range is the corrected one
and is not the Bloque A identity — the document is already flagged
`CV4_AUDIT_STATUS = PENDING_INDEPENDENT_RE_AUDIT_ROUND_4`.)

**Finding 4 — WARN. An unanchored count in a title.** `fig06_mapa_del_fracaso.py:156`
titles the figure "seis intentos contra el mismo obstáculo" and the docstring repeats it. Nothing
enumerates six: `HOJA_DE_RUTA.md` §2 lists Fases 0–6 (seven), and the figure itself draws eleven
stages. The number is rhetorical and should either be tied to an explicit list or dropped.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | ERROR | `fig02` draws `0.30` as a *correlation* threshold; in both contracts `0.30` bounds the median absolute relative error and the correlation-axis parking threshold is `0.50`. Materially erases the `HEIGHT_WIDTH` STRONGLY_PARKED / `COUNT_VOLUME` not-parked distinction | `emergencia/viz/fig02_el_gate.py:69-70,75-77`; `emergencia/viz/datos.py:25`; `P1a_contrato_representaciones_alternativas_d2.md:145-146,156-157`; `P1a_resultados_gate_altura_duracion_lex_d2.md:119-120` |
| 2 | WARN | `datos.py` cites the height-gate contract for constants governing the representations experiment | `emergencia/viz/datos.py:22-25` vs `P1a_contrato_representaciones_alternativas_d2.md:145-146` |
| 3 | WARN | The `<=0.0007` explanation is asserted as fact; the cited source does not state it and the reconstruction that supports it is not cited | `emergencia/viz/README.md` §"Dos precisiones"; `HOJA_DE_RUTA.md` §22.4; `P1a_count_volume_canal_sigma_m_d2.md:197-199` |
| 4 | WARN | "seis intentos" in the fig06 title is not anchored to any enumerated list (roadmap lists seven phases; figure draws eleven stages) | `emergencia/viz/fig06_mapa_del_fracaso.py:156` |
| 5 | WARN | 23 pre-existing mechanical warnings, all outside the audited scope (`data/reports/`, `evidence/`), none attributable to `c87d302` | §2 verbatim output |
| 6 | OK | Six of six committed PNGs are byte-identical to the output of the committed scripts | §4.1 |
| 7 | OK | The SHA-256 sidecar guardrail demonstrably fires on a one-byte perturbation | §4.2, `emergencia/viz/datos.py:42-59` |
| 8 | OK | `rho_max` recomputed in-figure reproduces the audited executable within `1e-4`; ANOVA decomposition verified, not imposed | §4.3, `emergencia/viz/datos.py:77-122` |
| 9 | OK | Every numeric claim in §22 and `viz/README.md` traces to a committed generator (11 checked) | §4.4 |
| 10 | OK | Seal `6e2c3888…` untouched and matching prereg-002/003; commit modifies nothing under `nachocausal/` | §3 |
| 11 | OK | Reserved seed band `[2000000–2999999]` not consumed; the single RNG call uses `20260807` for visual jitter only | §5, `fig03_canal_sigma_m.py:45` |
| 12 | OK | Hidden embedding used only to score; every predictor drawn is observable | §5, `datos.py:94-95,119` |
| 13 | OK | No over-claim of recoverability, reconstruction, asymptotics or `d>=3`; population/finite-sample boundary stated correctly | §6 |

AUDIT_ERRORS=1
AUDIT_WARNINGS=26

## 8. Verdict

One of: `AUDIT_PASS` (no errors, no warnings), `AUDIT_PASS_WITH_WARNINGS` (no errors, ≥1 warning),
`AUDIT_FAIL` (≥1 error). Must match the counts in §7.
AUDIT_VERDICT=AUDIT_FAIL

Counts: 1 error (finding 1) + 26 warnings (findings 2–4 manual, plus the 23 pre-existing
mechanical warnings of §2, none of which is attributable to `c87d302`).

The failure is narrow and repairable without touching data: the figure infrastructure, its
provenance guards, its reproducibility and its claim boundary all hold. What fails is one drawn
constant. Recommended remediation — **not applied; the user's call**:

1. In `emergencia/viz/datos.py`, replace `UMBRAL_FUERTE = 0.30` with the correlation-axis parking
   threshold `0.50` from `P1a_contrato_representaciones_alternativas_d2.md:156`, and cite that
   contract; or remove the secondary line from `fig02` entirely and keep only the `0.80` gate.
2. Cite the `sqrt(1-T_corr)` reconstruction in `viz/README.md` and `HOJA_DE_RUTA.md` §22.4, or
   mark the sentence `[UNVERIFIED]`.
3. Either enumerate the six attempts in `fig06` or drop the count from the title.
4. Regenerate the affected PNGs and re-verify byte-identity, since the figures are committed.

Re-audit of the corrected `fig02` is recommended before this material is cited anywhere outside
`emergencia/`.
