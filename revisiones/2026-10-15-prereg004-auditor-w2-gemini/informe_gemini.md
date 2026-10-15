<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ c12c10eb4de36669f2048754d2df20a9747adf1f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=high, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 533297ef9465d955c8d2c5d48e3c61d129536b8b99944cdc1770a1947f6f07f9
inicio: 2026-10-15T08:03:04Z  fin: 2026-10-15T08:04:16Z
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/revisiones/2026-10-15-prereg004-auditor-w2-gemini/delta.diff ; último commit observado: 94422d7 ; sha256 de la copia enviada d6d03863dcc05dd43592042470321f69c36dbbdb85b7bae49a321920e59a494c
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/revisiones/2026-10-15-prereg004-auditor-w2-gemini/mecanica.txt ; último commit observado: 94422d7 ; sha256 de la copia enviada d50dfeb5f4372ec295b49ba68ee048925656c6c83e776ef114b7629c2d648dbf
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/validate.py ; último commit observado: e6b5bfe ; sha256 de la copia enviada 1dc539b6cd6d0b8711b80ca1a4da3abc79308807f7e1416a47ba5e136177749f
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/docs/preregistration_004_draft.md ; último commit observado: e6b5bfe ; sha256 de la copia enviada e73800a2dd2241b427277eaf20b9e91edd27079bbc2c51d5e4878043c5448fa2
entrada_gemini.txt sha256 7f8172768c1dca97a707fa299a5904c9699a8040ed933ae78264348014b39852
respuesta sha256 b17a2937dea940f453b0efee1c43db19d33be733d49409851aec6e6d1766c7a9
-->

## 1. Scope

Auditoría de integridad sin ejecución de comandos sobre el delta `6f76d21..e6b5bfe`, centrada en la remediación del aviso `W2` de la auditoría previa (`revisiones/2026-10-15-prereg004-auditor-delta-gemini/`) y la actualización documental correspondiente. Artefactos inspeccionados (entregados en el prompt):

- `delta.diff` (`6f76d21..e6b5bfe` sobre `docs/preregistration_004_draft.md` y `nachocausal2p1/validate.py`).
- `mecanica.txt` (salida capturada por el autor en `e6b5bfe`, no verificable por ejecución en esta sesión).
- `nachocausal2p1/validate.py` (versión completa en `e6b5bfe`).
- `docs/preregistration_004_draft.md` (versión completa en `e6b5bfe`).

## 2. Mechanical audit

- **Límites epistémicos (demostrado vs. conjeturado):**
  - *Demostrado por inspección directa:* el contenido línea a línea de `delta.diff`, la estructura sintáctica y semántica de `nachocausal2p1/validate.py`, la coincidencia textual de los 15 hashes SHA256 entre la tabla del §3 de `docs/preregistration_004_draft.md` y `mecanica.txt`, y la coherencia interna del borrador.
  - *No demostrado (dependiente de `mecanica.txt` sin ejecución local):* que el hash SHA256 calculado sobre los bytes en disco de `nachocausal2p1/validate.py` sea efectivamente `1dc539b6cd6d0b8711b80ca1a4da3abc79308807f7e1416a47ba5e136177749f`, que `make verify-seal verify-seal-004` y `make test-004` (64 tests) terminen con `exit=0`, y que la comparación programática del AST (`ast_equal True`) se haya ejecutado tal como se reporta.
- **Tarea 1 — Naturaleza del cambio en `validate.py` (demostrado):**
  - La lectura línea a línea de `delta.diff` y `validate.py` demuestra que las únicas modificaciones en `nachocausal2p1/validate.py` son:
    1. Hunk `@@ -23,7 +23,8 @@` (`validate.py:26-27`): sustitución de una viñeta dentro del docstring de módulo (`"""..."""`, `validate.py:1-30`).
    2. Hunk `@@ -192,7 +193,9 @@` (`validate.py:196-198`): sustitución de líneas de comentario (`# ...`) dentro de `summarise_level` antes de `res["status"] = ...`.
  - No se ha alterado ninguna sentencia ejecutable, firma, constante ni flujo de control.
- **Tarea 2 — Exactitud de los nuevos comentarios frente al código (demostrado):**
  - *Docstring (`validate.py:26-27`):* afirma que toda comparación de pase es falsa en `NaN` (`<=`; `>=` para el suelo de cobertura; `<` para el conteo entero de abstenciones). Esto describe exactamente las comparaciones del código:
    - `<=` en `summarise_level` (`validate.py:176, 185, 186, 191, 192`: `p_perm`, `median_width_over_2M`, `iqr_width_over_2M`, `boundary_r_std`, `n_escape_MINK`) y en `verdict_from_levels` (`validate.py:243`: holgura de convergencia `b["median_width_over_2M"] <= a["median_width_over_2M"] + a["slack_over_2M"]`).
    - `>=` en `verdict_from_levels` (`validate.py:249`: `prim["coverage_frac"] >= thresholds.COVERAGE_FLOOR`).
    - `<` en `summarise_level` (`validate.py:177`: `res["n_abstain_BH"] < thresholds.BH_ABSTAIN_FAIL`, donde `n_abstain_BH` es un `int` construido en `validate.py:169`).
  - *Comentario en `summarise_level` (`validate.py:195-198`):* describe con exactitud el comportamiento de `summarise_level` y `verdict_from_levels`. Con cero semillas válidas (`len(ok) == 0`), las estadísticas retienen `NaN` y los conteos valen `0`; `res["status"]` pasa a `"inconclusive"` (`validate.py:199`); `verdict_from_levels` devuelve `"INCONCLUSIVE"` (`validate.py:229-233`) antes de construir `checks`; y los booleanos basados en conteos como `res["escape_pass"]` (`0 <= thresholds.MAX_MINK_ESCAPES`, `validate.py:192`) evalúan a `True` en el resumen de nivel pero se reportan como «not evaluable» según el §7 del borrador.
- **Tarea 3 — Coherencia del borrador en §3, §7, §9 y §10 (demostrado):**
  - El SHA de `nachocausal2p1/validate.py` en la tabla del §3 (`preregistration_004_draft.md:110`) es `1dc539b6cd6d0b8711b80ca1a4da3abc79308807f7e1416a47ba5e136177749f`, idéntico al reportado en `mecanica.txt:17`. Los otros 14 hashes de la tabla también coinciden exactamente con `mecanica.txt:7-21`.
  - El nuevo bloque en el §10 (`preregistration_004_draft.md:487-496`) describe fielmente la auditoría previa sobre `782d031..616c55d` (`AUDIT_PASS_WITH_WARNINGS`, 0 errores, 2 avisos, sin ejecución de comandos), el contenido y cierre de `W1` y `W2`, el alcance solo de comentarios en `validate.py` (con cambio de SHA reflejado en §3) y los elementos que quedan abiertos antes de C1 (esta auditoría del delta `6f76d21..`, las firmas del PI en los comités 052 y 053, y la decisión C1).
  - No quedan contradicciones internas entre el §7 (tratamiento de `INCONCLUSIVE`, muestras vacías y `NaN`), el §9 (`Sequence` y `Audit trail`, donde `W1` ya quedó subsanado en `preregistration_004_draft.md:429-431`) y el §10.

## 3. Findings

| # | Severity | Finding | Anchor |
|---|---|---|---|
| — | NONE | Sin hallazgos de error ni de aviso. El cierre de W2 en `validate.py` es exclusivamente de docstring/comentarios, refleja con exactitud la lógica de `summarise_level` y `verdict_from_levels`, y es consistente con los §§3, 7, 9 y 10 del borrador. | `delta.diff`, `nachocausal2p1/validate.py:26-27,169-199,226-259`, `docs/preregistration_004_draft.md:110,429-431,487-496` |

`AUDIT_ERRORS=0`
`AUDIT_WARNINGS=0`

## 4. Verdict

El delta `6f76d21..e6b5bfe` resuelve íntegramente `W2` sin tocar código ejecutable y mantiene la trazabilidad documental e integridad de hashes en el borrador.

`AUDIT_VERDICT=AUDIT_PASS`
