# Auditor Report 045 — prereg004-post-044-delta

> Producido aplicando `.claude/skills/auditor/SKILL.md` por Codex, el 2026-10-14.
> Auditoría retrospectiva; se informa, no se remedia. No se ejecutó la validación,
> no se sortearon semillas y no se modificó código ni un documento de congelación.

## 1. Scope & target

- Repo: `/home/ignac/nachocausal/.worktrees/prereg004-step3`.
- Rama: `prereg004/step3-port`.
- HEAD auditado: `4190a10554dcc5e31dfa86487fb605ca570cd2d9`.
- Base: `719ceaa`, commit que incorpora el informe 044 (su código auditado era `c16fb12`).
- Alcance: delta `719ceaa..4190a10`: O3/O4, correcciones y declaraciones O8,
  borrador prereg-004, decisiones añadidas al comité 052 y registro parcial de preflight.
  No se vuelve a auditar todo el historial científico ajeno al delta.
- Petición explícita del PI: «has tu la nueva auditoria». Esta auditoría se hace sobre código
  ya publicado, sin participar en su modificación. La conversación contiene una revisión
  previa de D11; no se acredita que se haya abierto una conversación/sesión nueva.
  Por tanto este informe no certifica por sí solo el requisito literal de «otra sesión».
- Estado inicial: `git status --short` sin salida; candidato no congelado.
  `STATUS = "CANDIDATE_NOT_FROZEN"`, `VALIDATION_DRAW_SEED = None`,
  `VALIDATION_SEEDS = ()` (`thresholds.py:31,123,132`).
- Ni un PASS de tests ni el verificador de formato autorizan C1 o C3.
  No se envió texto a terceros ni se convocó comité.

## 2. Mechanical audit

Comando: `bash .claude/skills/auditor/audit.sh`. Salida literal:

```
Auditor — auditing: /home/ignac/nachocausal/.worktrees/prereg004-step3
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/PR9_INTEGRATION_2026-10-02.md,docs/archive/relatividad_875d2c3/manuscript_limits_draft.md,docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/auditor/auditor_report_015_phase1-theory-package.md,docs/auditor/auditor_report_016_phase1-provenance-reaudit.md,docs/auditor/auditor_report_017_op21-terminal-run.md,docs/auditor/auditor_report_018_op21-terminal-second-pass.md,docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md,docs/auditor/auditor_report_020_op22-bd-dossier-rev3-fix-verification.md,docs/auditor/auditor_report_021_truncated-futures-freeze-preflight.md,docs/auditor/auditor_report_022_freeze-commit-scoped-audit.md,docs/auditor/auditor_report_023_ficha-tv-order-only-precommit.md,docs/auditor/auditor_report_024_wp4-annex-c-comparable-pair-separation-precommit.md,docs/auditor/auditor_report_025_wp4-annex-c-remediation-reaudit.md,docs/auditor/auditor_report_026_wp4-annex-c-variance-addendum-precommit.md,docs/auditor/auditor_report_027_wp4-ibar-interval-design-precommit.md,docs/auditor/auditor_report_028_wp4-ibar-executable-contract-precommit.md,docs/auditor/auditor_report_031_p1a-seccion-13-certificado-familia-prescrita.md,docs/auditor/auditor_report_032_emergencia-viz-figuras-del-fracaso.md,docs/auditor/auditor_report_033_emergencia-viz-remediacion-032-reauditoria.md,docs/auditor/auditor_report_034_emergencia-viz-cierre-avisos-033.md,docs/auditor/auditor_report_035_viz-figuras-generales-6-agosto.md,docs/auditor/auditor_report_036_viz-cierre-e1-y-avisos-035.md,docs/auditor/auditor_report_037_wp6-s1-paper-and-lean-evidence.md,docs/auditor/auditor_report_038_w16-closure-verification.md,docs/auditor/auditor_report_039_wp6-s1-manuscript-v1-post-referee.md,docs/auditor/auditor_report_040_provenance-remediation-closure.md,docs/auditor/auditor_report_041_provenance-reachability-final-closure.md,docs/auditor/auditor_report_042_wp6-s1-fisher-fiber-event-and-referee-closure.md,docs/auditor/auditor_report_043_prereg004-2p1-candidate-package.md,docs/auditor/auditor_report_044_prereg004-2p1-remediation-reaudit.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/comite/comite_decision_027_phase1-theory-package-first-review.md,docs/comite/comite_decision_028_phase1-theory-package-second-review.md,docs/comite/comite_decision_029_phase1-theory-package-third-review.md,docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md,docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md,docs/comite/comite_decision_032_phase1-theory-closure-handoff.md,docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md,docs/comite/comite_decision_034_op21-certifier-opening.md,docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md,docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md,docs/comite/comite_decision_037_candidate-b-viability-gate-review.md,docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md,docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md,docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md,docs/comite/comite_decision_045_candidate-7-1-fixed-n-logical-status.md,docs/comite/comite_decision_046_weyl-level-sheet-page-shoom-adjudication.md,docs/comite/comite_decision_047_phase2-b2-documentation-publication.md,docs/comite/comite_decision_048_q-fmots-target-adjudication.md,docs/comite/comite_decision_049_program-closure-adjudication.md,docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md,docs/comite/comite_decision_051_s1-gate-geometric-tangent-classification.md,docs/comite/comite_decision_052_prereg004-2p1-design.md,docs/foro/foro_decision_001_ef4-falsacion-adversarial.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_24_jul_2026.md,docs/hoja_de_ruta_25_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jul_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/manuscript_release_checklist.md,docs/physical_reentry_audit_001_2026-08-28.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/preregistration_004_draft.md,docs/program_closure_note_2026-07-30.md,docs/program_reopening_note_2026-08-28_R4.md,docs/rvar_closure_negative_result.md
----------------------------------------
Auditor: 0 error(s), 0 warning(s)
```

Exit code: `0`. Resultado mecánico: 0 errores, 0 avisos.
Los hallazgos manuales de §7 se añaden a esos contadores.

## 3. Seal & freeze integrity

`make verify-seal verify-2p1 PY=/home/ignac/nachocausal/.venv/bin/python`,
exit 0:

```
thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4
nachocausal2p1/thresholds.py 503a9b6e49e23ccc33210aff6e8b0256f3b0a385c0c3189a96f5a54546679c70
nachocausal2p1/fixtures/tau_table_2p1.json 4bc4aec839257af7fed210030c0afa9041c265cacf43802bb735fb99df367a28
```

El sello 1+1 coincide exactamente con `docs/preregistration_002.md:7-9`.
Los SHAs de los módulos importados coinciden con el borrador §3:

```
aa4411c3d095230e0f6dde78e4a8de11240c0cb42ad14353453848d70cdf1680  nachocausal/estimator.py
d6f09fdc21b76f6cf329c33580342a068135f7ece7ed11c304552f0848216f9f  nachocausal/generator.py
f1ec7306ced3e1f948b3a147b4e8c69f201c2bb803a1cb2525b5602239a2c7b7  nachocausal/__init__.py
```

`git diff 719ceaa..4190a10 -- nachocausal/ nachocausal2p1/generator.py
nachocausal2p1/estimator.py nachocausal2p1/gate.py nachocausal2p1/scoring/` no produce salida:
esos componentes no cambiaron. El SHA candidato antiguo del borrador está explícitamente
rotulado «at drafting time»; no se trata como un sello actual.

**E1 — Falta una definición coherente del sello entre C1 y C2.**
`thresholds.py:3-6` dice que el fichero se sella en C1 y que cualquier cambio posterior es
un preregistro nuevo. Sin embargo, `thresholds.py:117-132` prescribe registrar allí el sorteo
en C2, que depende del SHA de C1, y mantiene sus valores vacíos hasta entonces.
El §9 exige además `git diff <seal> -- ... nachocausal2p1/ ...` con cero líneas
(`docs/preregistration_004_draft.md:281-290`). Si `<seal>` es C1, la edición obligatoria
de C2 rompe ese requisito. Si es C2, falta decirlo y definir la excepción al sello de C1.
El propio §3 anticipa modificaciones de los campos de semillas, pero no resuelve la
distinción C1/C2. No se ha ejecutado ninguna de las dos etapas para comprobarlo.

Remediación recomendada: fijar explícitamente qué congela C1, dónde vive el manifiesto
de C2, cuál es el commit de referencia de C3 y qué cambios administrativos se permiten;
no cambiar parámetros de análisis después de C1.

## 4. Reproducibility of published numbers

- Suite canónica (`tests/`): comando `make test PY=/home/ignac/nachocausal/.venv/bin/python`.
  Resultado consignado al terminar la ejecución en el apartado de verificación final.
  La suite usa los generadores y tests permanentes de este commit; no se añadió un script
  científico efímero.
- O3/O4: tests permanentes `test_blind_threads_can_fail`,
  `test_validation_run_checks_threads_before_generation`,
  `test_progress_line_is_blind`,
  `test_progress_log_written_per_seed_before_the_verdict`
  (`tests/test_2p1_package.py:259-321`).
- D1/D2/D9: pruebas de NaN, nivel secundario corto y fallos aislados en
  `tests/test_004_criteria_can_fail.py:191-276`. Los casos usan filas sintéticas.
- D3/D5: rechazo de `write=False` y comprobación del formato del SHA en
  `tests/test_2p1_package.py:324-342`.
- D4: verificación estática de `validate.py:342-345`: el entry point llama a `run()`
  e imprime veredicto/ruta. No se ejecutó el entry point de validación.
- No se repitió la comparación de siete tests contra `5afb33d`; la afirmación histórica
  de esa comparación no queda verificada por esta auditoría.
- Preflight: `dev/preflight_2p1.py`, generador permanente, y
  `dev/preflight_2p1_2026-10-13.jsonl`, SHA256
  `6838b4acc063b5fdab16f297d1b47c5270bc5bd055486b85bfdbaeea844eb0e7`.
  Su única fila registra semilla exploratoria 7000100, 20 hilos, 15 banderas de comparación
  verdaderas, `all_match=true`, tiempos 588.7/3.2/591.9 s. Coincide con §8.
  Se inspeccionó el registro y el generador; no se volvió a ejecutar el preflight.
  Una fila no demuestra paridad para las nueve semillas restantes ni determinismo entre hilos.
  El borrador declara ambas limitaciones; la extrapolación de 4.4 h está marcada UNVERIFIED.
- Los textos de Gemini/Claude se trataron como objetos de revisión, no como fuentes de prueba.
  No se revalidó literatura física: el alcance aquí es el delta de implementación y contrato.

**E2 — Los agregados prometidos faltan en niveles INCONCLUSIVE.**
El borrador `docs/preregistration_004_draft.md:216-218` promete por nivel, cualquiera que
sea el veredicto, contar horquillas válidas/limpias y cobertura e informar mediana, IQR,
dispersión y p_perm. `summarise_level` retorna antes de calcularlos si hay menos de 18
semillas válidas (`validate.py:176-178`), y `run_level` solo añade las filas crudas.
La nueva regla D2 devuelve correctamente INCONCLUSIVE, pero no cumple esa promesa de informe.

Inspección manual corta, usando la función sintética permanente del test, sin generar causets:

```python
# Ejecutado con .venv/bin/python -c; las únicas filas son sintéticas.
import runpy
m = runpy.run_path("tests/test_004_criteria_can_fail.py")
rows = m["_synthetic_rows"](32.0)
[r.update(invalid=True) for r in rows[:3]]
out = m["validate"].summarise_level(rows, 32.0)
print(out)
print("missing promised aggregates:", sorted({
    "n_bracket_valid", "n_clean", "coverage_count", "coverage_frac",
    "median_width_over_2M", "iqr_width_over_2M", "boundary_r_std", "p_perm"
} - out.keys()))
```

Salida relevante, exit 0:

```
n_generator_valid=17; status=inconclusive
missing promised aggregates: ['boundary_r_std', 'coverage_count', 'coverage_frac', 'iqr_width_over_2M', 'median_width_over_2M', 'n_bracket_valid', 'n_clean', 'p_perm']
```

La segunda vía es la lectura del retorno temprano y de `run_level`:
los agregados no se completan al persistir el nivel; disponer de filas crudas no equivale
a haberlos informado. Remediación: producir los agregados descriptivos sin cambiar el
veredicto, o limitar explícitamente la promesa y registrar los no evaluados.

## 5. dev/validation separation & ground-truth leakage

- O3: `thresholds.assert_blind_threads` comprueba variable de entorno y número efectivo
  de hilos (`thresholds.py:72-83`); `run` lo llama antes de generar
  (`validate.py:283,297`). Sus tests hacen fallar ambos desacuerdos.
- O4/D6: `PROGRESS_FIELDS=("seed","rho","seconds")` (`validate.py:48`);
  `progress_line` selecciona esos campos; `append_progress` hace flush/fsync
  (`validate.py:201-212`). La línea start contiene semilla/etiqueta/hora, no scoring.
  Esto elimina campos directos de veredicto; no se afirma que los tiempos sean
  matemáticamente independientes del estado del generador.
- D1: IQR y F usan comparaciones que rechazan NaN
  (`validate.py:189-190,244`); tests ejercitan casos vacíos y una sola horquilla.
- D2: se revisan los tres niveles antes de decidir PASS/FAIL
  (`validate.py:229-234`). E2 se refiere al informe, no a esa decisión.
- D3: la etiqueta de validación rechaza `write=False` (`validate.py:274-275`).
- Guardas de semillas: `check_seed` precede a la generación, y el estado actual no
  permite semillas vírgenes (`validate.py:85-104`). Los tests de ramas congeladas
  sustituyen la generación por una función que falla si se llama; las cifras de
  `VIRGIN_20` son datos de prueba y no realizaciones vírgenes.
- Estimación antes de revelar r: `validate.py:143-151`; estimator/gate/scoring sin
  cambios en el delta. D7 y D8 están declarados (`draft:202-215`) y coinciden con
  `generate` usando `default_rng(seed)` y la selección `clean` de `summarise_level`.
  No se realizó una nueva comparación de anchuras dev con theta.
- D11: `estimator.py:35-36` y `gate.py:42-48` propagan errores; el runner no los
  convierte en PASS ni escribe un resultado final al abortar. §9 prescribe guardar
  el traceback y registrar ABORTED_GUARD_V/ABORTED_TAU_RANGE, sin relanzar.
  Es un procedimiento documental; no existe una escritura automática de esos estados.
  El progreso de semillas completadas queda, pero el de la semilla que aborta no se añade
  (`validate.py:216-224`). La aceptación de D11 no se interpreta como implementación
  automática de un registro de abortos.

**W1 — D5 da reproducibilidad, pero no acredita la garantía absoluta de impredecibilidad.**
El borrador afirma que «nobody can compute the virgin seeds before the freeze»
(`draft:138-139`), y los comentarios de thresholds repiten esa justificación.
El SHA es una función del contenido del objeto commit; puede calcularse cuando se
conoce ese contenido, antes de crear la referencia de rama. No aporta entropía externa
posterior a C1 ni impide escoger entre contenidos/metadatos de commits candidatos.

Comprobación local por una segunda vía, sin crear objetos, commits ni calcular semillas:

```sh
git cat-file commit 4190a10 | git hash-object -t commit --stdin
# 4190a10554dcc5e31dfa86487fb605ca570cd2d9
```

Esto no demuestra que nadie haya anticipado o seleccionado semillas. La guarda de
ejecución antes de FROZEN sigue funcionando. Se recomienda limitar la afirmación a
derivación reproducible desde el commit identificado y explicar su límite documental;
si se exige impredecibilidad frente al autor de C1, hace falta otro contrato de sorteo.
No se recomienda cambiarlo durante esta auditoría.

## 6. Claim-boundary check

El borrador §1 limita la afirmación a localización en parche ecuatorial finito 2+1,
expone A1-A4 como supuestos y excluye reconstrucción métrica/horizonte global/3+1.
D7/D8, la paridad parcial y la relación de (i)/(iv) con la compuerta están declaradas.
No se promociona el NOT READY de Gemini a aprobación del código corregido.

**W2 — El límite ilustrativo de cobertura es 10, no 9, fallos sobre 20.**
`draft:220-221` dice «up to 9 of 20 non-covering seeds still PASS» con suelo 0.5.
La comparación real es `coverage_frac >= COVERAGE_FLOOR` (`validate.py:249`); 10/20 cubiertas alcanza el suelo.
El ejemplo subestima en uno los fallos tolerados. No cambia el umbral ni el código.

Segunda vía: caso sintético, utilizando las mismas funciones permanentes del test:

```python
import runpy
m = runpy.run_path("tests/test_004_criteria_can_fail.py")
rows = m["_synthetic_rows"](m["PRIM"])
[r.update(covers=False) for r in rows[:10]]
prim = m["validate"].summarise_level(rows, m["PRIM"])
out = m["validate"].verdict_from_levels(m["_levels"](prim), guard_ran=True)
print("coverage_count:", prim["coverage_count"],
      "coverage_frac:", prim["coverage_frac"], "verdict:", out["verdict"])
```

Salida, exit 0: `coverage_count: 10 coverage_frac: 0.5 verdict: PASS`.
Es una comprobación de lógica con filas sintéticas, no un resultado de validación.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| E1 | ERROR | Contrato C1/C2 no define una excepción coherente para editar el fichero sellado ni el commit de referencia del diff nulo de C3. | thresholds.py:3-6,117-132; draft:281-290; §3 |
| E2 | ERROR | Un nivel INCONCLUSIVE omite los agregados prometidos para todo veredicto. | validate.py:176-178,216-224; draft:216-218; inspección sintética §4 |
| W1 | WARN | Derivar del SHA de C1 no justifica la garantía absoluta de no poder calcular semillas antes del freeze. | draft:136-140; thresholds.py:119-131; hash-object §5 |
| W2 | WARN | Suelo 0.5 tolera 10/20 no cubiertas; el ejemplo del texto dice 9. | draft:220-221; comprobación sintética §6 |
| O3 | OK | Hilos efectivos y entorno comprobados antes de generar. | thresholds.py:72-83; validate.py:283; tests |
| O4 | OK | Progreso sin campos directos de scoring, con flush/fsync y start por lanzamiento. | validate.py:48,201-224,293-297; tests |
| O8 | OK | Correcciones NaN, write=False y nivel corto verificadas; fallos aislados permanentes. | validate.py:189-190,229-244,274-275; tests |
| D11 | OK | Aborto no es PASS; registro prescrito es documental y requiere conservar traceback. | draft:273-277; estimator.py:35-36; gate.py:42-48; validate.py:297-302 |
| SEAL | OK | Sello 1+1, módulos importados y tau sin deriva. | §3 |
| MECH | OK | Auditoría mecánica: 0 errores, 0 avisos. | §2 |

AUDIT_ERRORS=2
AUDIT_WARNINGS=2

## 8. Verdict

AUDIT_VERDICT=AUDIT_FAIL

Los tests no subsanan E1/E2. No se recomienda congelar con estos desajustes.
El auditor no aplica las correcciones. Tras remediarlas corresponde reauditar el delta,
y después realizar el paso 7 con el comité canónico en Claude Code y decisión del PI.
El requisito literal de sesión separada tiene la limitación de procedencia declarada en §1.

Verificación final de las suites:

```text
make test PY=/home/ignac/nachocausal/.venv/bin/python
539 passed in 420.40s (0:07:00)
exit 0

make op21-bench PY=/home/ignac/nachocausal/.venv/bin/python
25 passed, 2 skipped in 0.15s
exit 0
```

Total observado: **564 passed, 2 skipped**, coincidente con lo comunicado por el PI.
`op21-bench` ejecuta `certifier/tests`, no el objetivo `op21-terminal`.
Los 43 tests específicos de prereg-004 están incluidos en los 539 de la suite canónica
(25 de paquete, 18 de criterios; comprobado con `pytest --collect-only -q` de ambos ficheros).
No se requirió cambiar código para ejecutar las suites. El único fichero añadido por
esta auditoría es este informe; HEAD permanece en `4190a10`. El verificador de estructura
`check_audit_report.py` devuelve `AUDIT_CHECK=PASS`, que verifica el formato y la coherencia
de los contadores, no revoca el veredicto científico/técnico `AUDIT_FAIL`.
