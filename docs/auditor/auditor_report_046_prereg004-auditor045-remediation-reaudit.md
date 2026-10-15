# Auditor Report 046 — prereg004-auditor045-remediation-reaudit

> Producido por Codex aplicando `.claude/skills/auditor/SKILL.md`, el 2026-10-14.
> Auditoría retrospectiva del delta publicado. Se informa; no se remedia.

## 1. Scope & target

- Repo: `/home/ignac/nachocausal/.worktrees/prereg004-step3`.
- Rama: `prereg004/step3-port`.
- Base: `3cc152a`; HEAD: `782d031f05f000ce193c75522d7820388944ebc3`.
- Alcance: `3cc152a..782d031`, correcciones E1/E2/W1/W2 del informe 045, nuevo productor/lector de manifiesto, integración, tests y textos. No se reaudita el historial científico ajeno al delta.
- Petición del PI: «comenzamos con la proxima sesion». Este turno audita el candidato publicado sin modificar su implementación. La continuidad de conversación no acredita por sí sola una sesión técnica distinta; este informe no certifica ese hecho de procedencia.
- Estado inicial: `git status --short` vacío. `git ls-remote origin refs/heads/prereg004/step3-port` devuelve el SHA completo de HEAD, exit 0.
- La única escritura permanente de esta auditoría es este informe. No se ejecutaron C1/C2/C3, sorteos reales, preflight ni validación; tampoco commit/push o envíos a terceros.
- La biblioteca está en el repo principal, no en este worktree; se consultó su índice para orientar el alcance. No se usan sus etiquetas ni textos de modelos como evidencia de las correcciones.

## 2. Mechanical audit

Comando: `bash .claude/skills/auditor/audit.sh`. Salida literal:

```text
Auditor — auditing: /home/ignac/nachocausal/.worktrees/prereg004-step3
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/PR9_INTEGRATION_2026-10-02.md,docs/archive/relatividad_875d2c3/manuscript_limits_draft.md,docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/auditor/auditor_report_015_phase1-theory-package.md,docs/auditor/auditor_report_016_phase1-provenance-reaudit.md,docs/auditor/auditor_report_017_op21-terminal-run.md,docs/auditor/auditor_report_018_op21-terminal-second-pass.md,docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md,docs/auditor/auditor_report_020_op22-bd-dossier-rev3-fix-verification.md,docs/auditor/auditor_report_021_truncated-futures-freeze-preflight.md,docs/auditor/auditor_report_022_freeze-commit-scoped-audit.md,docs/auditor/auditor_report_023_ficha-tv-order-only-precommit.md,docs/auditor/auditor_report_024_wp4-annex-c-comparable-pair-separation-precommit.md,docs/auditor/auditor_report_025_wp4-annex-c-remediation-reaudit.md,docs/auditor/auditor_report_026_wp4-annex-c-variance-addendum-precommit.md,docs/auditor/auditor_report_027_wp4-ibar-interval-design-precommit.md,docs/auditor/auditor_report_028_wp4-ibar-executable-contract-precommit.md,docs/auditor/auditor_report_031_p1a-seccion-13-certificado-familia-prescrita.md,docs/auditor/auditor_report_032_emergencia-viz-figuras-del-fracaso.md,docs/auditor/auditor_report_033_emergencia-viz-remediacion-032-reauditoria.md,docs/auditor/auditor_report_034_emergencia-viz-cierre-avisos-033.md,docs/auditor/auditor_report_035_viz-figuras-generales-6-agosto.md,docs/auditor/auditor_report_036_viz-cierre-e1-y-avisos-035.md,docs/auditor/auditor_report_037_wp6-s1-paper-and-lean-evidence.md,docs/auditor/auditor_report_038_w16-closure-verification.md,docs/auditor/auditor_report_039_wp6-s1-manuscript-v1-post-referee.md,docs/auditor/auditor_report_040_provenance-remediation-closure.md,docs/auditor/auditor_report_041_provenance-reachability-final-closure.md,docs/auditor/auditor_report_042_wp6-s1-fisher-fiber-event-and-referee-closure.md,docs/auditor/auditor_report_043_prereg004-2p1-candidate-package.md,docs/auditor/auditor_report_044_prereg004-2p1-remediation-reaudit.md,docs/auditor/auditor_report_045_prereg004-post-044-delta.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/comite/comite_decision_027_phase1-theory-package-first-review.md,docs/comite/comite_decision_028_phase1-theory-package-second-review.md,docs/comite/comite_decision_029_phase1-theory-package-third-review.md,docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md,docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md,docs/comite/comite_decision_032_phase1-theory-closure-handoff.md,docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md,docs/comite/comite_decision_034_op21-certifier-opening.md,docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md,docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md,docs/comite/comite_decision_037_candidate-b-viability-gate-review.md,docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md,docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md,docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md,docs/comite/comite_decision_045_candidate-7-1-fixed-n-logical-status.md,docs/comite/comite_decision_046_weyl-level-sheet-page-shoom-adjudication.md,docs/comite/comite_decision_047_phase2-b2-documentation-publication.md,docs/comite/comite_decision_048_q-fmots-target-adjudication.md,docs/comite/comite_decision_049_program-closure-adjudication.md,docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md,docs/comite/comite_decision_051_s1-gate-geometric-tangent-classification.md,docs/comite/comite_decision_052_prereg004-2p1-design.md,docs/foro/foro_decision_001_ef4-falsacion-adversarial.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_24_jul_2026.md,docs/hoja_de_ruta_25_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jul_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/manuscript_release_checklist.md,docs/physical_reentry_audit_001_2026-08-28.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/prereg004_auditor045_remediation.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/preregistration_004_draft.md,docs/program_closure_note_2026-07-30.md,docs/program_reopening_note_2026-08-28_R4.md,docs/rvar_closure_negative_result.md
----------------------------------------
Auditor: 0 error(s), 0 warning(s)
```

Exit code: `0`.

## 3. Seal & freeze integrity

`make verify-seal verify-2p1 PY=/home/ignac/nachocausal/.venv/bin/python`, exit 0:

```text
thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4
nachocausal2p1/thresholds.py 2bf954fb1164f94b42b2e34512aac1d10d5e76e77915b15c14a640bf7186908e
nachocausal2p1/fixtures/tau_table_2p1.json 4bc4aec839257af7fed210030c0afa9041c265cacf43802bb735fb99df367a28
```

El sello 1+1 coincide con `docs/preregistration_002.md:7-9`. El SHA 2+1 es del candidato, no un sello.
`git diff 3cc152a..782d031 -- nachocausal/ nachocausal2p1/generator.py nachocausal2p1/estimator.py nachocausal2p1/gate.py nachocausal2p1/scoring/ nachocausal2p1/fixtures/` no produce salida.
Los SHAs antiguos del borrador están rotulados «at drafting time» (`draft:96`), y se prescribe retomarlos en C1.

**E1 corregido.** C1 introduce el documento no-draft y sella el instrumento; C2 añade un manifiesto fuera de los caminos sellados sin modificar thresholds; C3 usa C2 publicado como HEAD y C1 como referencia del diff (`docs/preregistration_004_draft.md:299-310`).
`seed_manifest.py:22-43` identifica C1 mediante el único commit de adición del documento y exige diff nulo del instrumento; `:54-71` comprueba esquema, SHA, banda, cardinalidad, tipos y receta exacta; `:74-100` exige manifiesto comprometido, árbol limpio y rechazo de sobrescritura.
Segunda vía: `tests/test_004_seed_manifest.py:126-159` usa Git real en un repo temporal con documento, instrumento y sorteo sintéticos; acepta C1/C2 distintos y rechaza manifiesto no comprometido y deriva.
La publicación remota de C2 y la autorización humana siguen siendo requisitos del procedimiento, no comprobaciones automáticas del lector.

## 4. Reproducibility of published numbers

Comprobación actual: `make test PY=/home/ignac/nachocausal/.venv/bin/python`.

```text
557 passed in 430.37s (0:07:10)
exit 0
```

`pytest --collect-only -q tests/test_004_seed_manifest.py tests/test_2p1_package.py tests/test_004_criteria_can_fail.py`, en el mismo Python, recoge **61 tests**, exit 0. Están incluidos en la suite canónica; no se atribuye a este candidato el total histórico de 564 del informe 045.
Los nuevos tests del manifiesto sustituyen el sorteo por IDs sintéticos o un RNG falso (`tests/test_004_seed_manifest.py:15-29,109-123,144-147`); no generan realizaciones vírgenes.

**E2 corregido.** `validate.py:160-197` calcula agregados antes de asignar el estado. `verdict_from_levels:229-233` conserva INCONCLUSIVE si cualquier nivel es corto; `run_level:214-223` conserva también las filas.
Segunda vía: tests de 17 válidas y 20 inválidas (`tests/test_2p1_package.py:164-181`) comprueban contadores, estadísticas y NaN; el test del nivel secundario corto conserva el veredicto INCONCLUSIVE (`tests/test_004_criteria_can_fail.py`).
El registro de remediación identifica los comandos permanentes y sus resultados históricos; los tiempos de aquella ejecución no se presentan como mediciones actuales.

## 5. dev/validation separation & ground-truth leakage

`thresholds.py:31` conserva `CANDIDATE_NOT_FROZEN`; `:153-159` no lee ni sortea semillas en ese estado. `git ls-files docs/preregistration_004.md docs/validation_004_seeds.json` no produce salida y no existen esos archivos reales.
`validate.py:85-102,262-283` exige manifiesto verificado para semillas vírgenes y mantiene las guardas de etiqueta, escritura, Guard-v y hilos antes de generar. Tests permanentes rechazan candidato, manifiesto ausente, receta incorrecta y deriva (`tests/test_004_seed_manifest.py:46-106`).
El estimador permanece sin cambios; `validate.py:143-151` sigue estimando antes de revelar r al scoring.
`git check-ignore results/validation_004.progress.jsonl results/validation_004_provenance_launch.txt` confirma que ambos archivos de ejecución están ignorados: su escritura prevista no ensucia por sí sola el árbol para el lector por semilla.
No se cambia el alcance documental de D11 ni se acredita un manejador automático de abortos.

**W1 corregido.** El borrador limita la derivación del SHA a reproducibilidad y declara que el autor puede calcular el hash antes de publicar (`draft:138-145`); thresholds hace la misma distinción (`:117-120`). La receta no incorpora entropía externa. Esto no demuestra ausencia histórica de anticipación; elimina la garantía absoluta que motivó W1.

## 6. Claim-boundary check

El borrador limita la afirmación al parche ecuatorial finito 2+1 y la presenta como algo que se registraría, no como un resultado validado (`draft:3-11,20-32`). No se promociona a reconstrucción métrica ni 3+1.
El añadido al comité declara expresamente que no constituye nuevo veredicto ni autorización C1-C3 (`docs/comite/comite_decision_052_prereg004-2p1-design.md:509-517`); su verificador devuelve `BRIEF_CHECK=PASS`, exit 0, únicamente de estructura.

**W2 corregido.** El ejemplo dice 10/20 no cubiertas (`draft:230-233`). El código compara cobertura con suelo 0.5 (`validate.py:248`, `thresholds.py:186`); segunda vía aritmética: 10 cubiertas / 20 válidas = 0.5. La frase describe el componente de cobertura, siempre subordinado a los demás criterios del PASS. No cambia el umbral.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| E1 | OK | Contrato C1/C2/C3 coherente; manifiesto externo al instrumento, verificado contra C1 y HEAD. | §3; seed_manifest.py:22-100; tests/test_004_seed_manifest.py:126-159 |
| E2 | OK | INCONCLUSIVE conserva agregados y filas sin convertirse en PASS. | validate.py:160-197,214-233; tests/test_2p1_package.py:164-181 |
| W1 | OK | Garantía limitada a reproducibilidad; límite de impredecibilidad declarado. | draft:138-145; thresholds.py:117-120 |
| W2 | OK | Ejemplo de cobertura corregido a 10/20. | draft:230-233; validate.py:248 |
| SEAL | OK | Sello 1+1 y tabla tau intactos; 2+1 permanece candidato. | §3; thresholds.py:31 |
| TEST | OK | Suite canónica y 61 tests del alcance verificados. | §4 |
| BOUNDARY | OK | Sin validación ni promoción de claim; firma y decisión C1 pendientes. | §5-6 |
| MECH | OK | Auditoría mecánica sin errores ni avisos. | §2 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=0

## 8. Verdict

AUDIT_VERDICT=AUDIT_PASS

E1/E2/W1/W2 del informe 045 están corregidos en este delta. PASS del alcance técnico auditado: no es validación científica, revisión independiente entre familias ni autorización de congelación.
Corresponde llevar el borrador y este informe al paso 7 de `/comite` en Claude Code; después el PI firma y decide C1. El auditor no convoca un comité propio ni ejecuta ese paso.
El informe queda local, sin commit/push; HEAD permanece en el candidato auditado.

