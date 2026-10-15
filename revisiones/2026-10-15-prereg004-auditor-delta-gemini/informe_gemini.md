<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ c12c10eb4de36669f2048754d2df20a9747adf1f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=high, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 893760d1bd2bb178dfdaff454721d37fa9278266b66ec9a404781a64260935d0
inicio: 2026-10-15T07:53:49Z  fin: 2026-10-15T07:59:19Z
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/revisiones/2026-10-15-prereg004-auditor-delta-gemini/delta.diff ; último commit observado: b18ba31 ; sha256 de la copia enviada d91240fde4bada977de562b5e8ce33ab36465d96d4db27ef549ef0ef88d5203b
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/revisiones/2026-10-15-prereg004-auditor-delta-gemini/mecanica.txt ; último commit observado: b18ba31 ; sha256 de la copia enviada 6dc472eff7a3e69b409c8f2a10b1aa3c27f35e1a78cedf48150a90f1c8d07d8e
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/docs/preregistration_004_draft.md ; último commit observado: 616c55d ; sha256 de la copia enviada fe4442b3c37e94114e201d6aaa82fb47f5347f7b167490c9615f1c8c630e7842
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/seed_manifest.py ; último commit observado: 76da124 ; sha256 de la copia enviada 299b4cc2ae02ee557e88d2210fc0ae658a6e24eb904ac73d09df555ac7d87255
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/validate.py ; último commit observado: 782d031 ; sha256 de la copia enviada ad68e34b11fe758f8a28ed943ae91d9d43f85806038514e2fa8871b3aa19f4e6
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/thresholds.py ; último commit observado: 782d031 ; sha256 de la copia enviada 2bf954fb1164f94b42b2e34512aac1d10d5e76e77915b15c14a640bf7186908e
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/tests/test_004_seed_manifest.py ; último commit observado: 76da124 ; sha256 de la copia enviada b237fe68bc4856467de914eb7a58ebaacaa4061ab1ae6733129a74f88d0e54ae
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/tests/test_004_criteria_can_fail.py ; último commit observado: 007947e ; sha256 de la copia enviada 2cb3a795318deed34c7e5e1e1871dfd3b8898fe262ea9fd17a84b1e88790bc13
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/Makefile ; último commit observado: 007947e ; sha256 de la copia enviada 2b7ab827107924940965a7d428925b43014c205008a6894070c39d2bda75d8f9
entrada_gemini.txt sha256 201696005260b3c621c233fae095a1f60c777cf2d02e9abbb902d9cc1289af5a
respuesta sha256 b109b3ddeeefc8716e2f81b245fca9d469f040c90b197f88880ce5823e3c21a1
-->

## 1. Scope

- **Objeto auditado:** delta `782d031..616c55d` en la rama `prereg004/step3-port` y estado completo en `616c55d` de `docs/preregistration_004_draft.md`, `nachocausal2p1/seed_manifest.py`, `nachocausal2p1/validate.py`, `nachocausal2p1/thresholds.py`, `tests/test_004_seed_manifest.py`, `tests/test_004_criteria_can_fail.py` y `Makefile`.
- **Restricciones de sesión:** auditoría retrospectiva sin herramientas, sin ejecución de código ni acceso al árbol de ficheros más allá de los documentos adjuntos. El paquete 1+1 (`nachocausal/`, sello `6e2c3888…`) se trata como auditado.

---

## 2. Mechanical audit

`mecanica.txt` fue capturado por Claude Opus 5.5 (autor del código y del borrador) el `2026-10-15T07:52:56Z`. **No es verificable independientemente por este auditor** al no disponer de terminal en esta sesión; se evalúa su coherencia interna contra `delta.diff` y los ficheros adjuntos:

- **Estado de Git (`HEAD = 616c55d75b375943dbfa4483c440073a8e12fe49`):** `git status --porcelain | wc -l` devuelve `1` (explicado en el encargo como la carpeta aún sin commit de esta auditoría). `git log --oneline 782d031..HEAD` lista 7 commits (`efada85..616c55d`) y `git diff --stat 782d031..HEAD` muestra 16 ficheros modificados (`2940 insertions(+), 53 deletions(-)`), coherente con los 12 ficheros de `delta.diff` más los 4 artefactos brutos omitidos (`entrada_gemini.txt`, `estado_gemini.json`, `gemini.json`, `gemini.log`).
- **Script mecánico (`bash .claude/skills/auditor/audit.sh`):** devuelve `0 error(s), 0 warning(s)`, `exit=0`, verificando la presencia del sello 1+1 (`6e2c3888…`) en los documentos del repositorio (incluidos los nuevos `auditor_report_046_...md` y `comite_decision_053_...md`).
- **Verificadores y tests:**
  - `make verify-seal verify-2p1 verify-seal-004` devuelve `exit=0` con los 15 SHA256 de los ficheros sellables en C1.
  - `make test-004` devuelve `64 passed in 13.51s` (`exit=0`), coherente con los 61 tests previos en `782d031` (`docs/auditor/auditor_report_046_prereg004-auditor045-remediation-reaudit.md:54`) más los 3 tests nuevos añadidos en este delta. (La suite global `make test` no figura re-ejecutada en `mecanica.txt`).
  - `make verify-comite verify-audit` devuelve `45 AUDIT_CHECK=PASS` y `53 BRIEF_CHECK=PASS` (`exit=0`).
  - `git check-ignore -v results/validation_004.json` confirma `.gitignore:21:results/`, y `ls` confirma la inexistencia de `docs/preregistration_004.md`, `docs/validation_004_seeds.json` y `results/`.
- **Coherencia interna de `mecanica.txt`:** no presenta ninguna contradicción interna ni con `delta.diff`.

---

## 3. Seal & freeze integrity

### Tarea 1: Sello y congelación
1. **Coincidencia de SHAs (§3 vs `mecanica.txt`):** Los 15 hashes SHA256 de la tabla del §3 de `docs/preregistration_004_draft.md:100-118` (`delta.diff` l. `+98..+118`) coinciden bit a bit con la salida de `make verify-seal-004` en `mecanica.txt`, incluidos el sello 1+1 (`nachocausal/thresholds.py` = `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`), `nachocausal2p1/thresholds.py` (`2bf954fb…`), el fixture τ (`4bc4aec8…`, idéntico a `thresholds.TAU_FIXTURE_SHA256` en `nachocausal2p1/thresholds.py:169`) y `nachocausal2p1/seed_manifest.py` (`299b4cc2ae02ee557e88d2210fc0ae658a6e24eb904ac73d09df555ac7d87255`, actualizado tras el commit `76da124`).
2. **Intangibilidad de `nachocausal/`:** Ningún fichero bajo `nachocausal/` cambió en `782d031..616c55d` (`delta.diff`, `mecanica.txt` `git diff --stat`).
3. **Único cambio bajo `nachocausal2p1/`:** El único fichero modificado bajo `nachocausal2p1/` es `nachocausal2p1/seed_manifest.py` (`delta.diff` l. `+37..+47`). En `seed_manifest._check_freeze` (`nachocausal2p1/seed_manifest.py:43-44`) se añade `"--full-history"` a la llamada `_git("log", "--full-history", "--diff-filter=A", "--format=%H", "--", FROZEN_DOC)`. Hace exactamente lo que declaran su comentario en código (`seed_manifest.py:40-42`), el mensaje del commit `76da124` (`mecanica.txt`) y el borrador en §9 (`docs/preregistration_004_draft.md:404-405`) y §10 (`docs/preregistration_004_draft.md:477-480`). El instrumento sigue en estado candidato (`STATUS = "CANDIDATE_NOT_FROZEN"` en `nachocausal2p1/thresholds.py:31`).

### Tarea 2: El arreglo G8 (`--full-history` en `_check_freeze`)
1. **¿Cierra el resquicio del merge `-s ours`?** **Sí (demostrado por el código y la semántica de Git).** Sin `--full-history`, `git log -- <ruta>` aplica simplificación de historial: en un merge cuyo árbol coincide con el de su primer padre (como `git merge -s ours C1` desde un `C1_alt` alternativo ramificado desde `C1^`), Git poda la rama del segundo padre y devuelve únicamente `[C1_alt]`. Con `--full-history` (`nachocausal2p1/seed_manifest.py:43`), Git desactiva la poda de padres al filtrar por ruta y recorre todas las ramas fusionadas; al encontrar dos commits de adición (`[C1_alt, C1]`), la guarda `if introduced != [freeze_commit]:` (`seed_manifest.py:45`) lanza `RuntimeError`.
2. **¿Puede romper el caso legítimo?** **No.**
   - En rama lineal o tras un merge *fast-forward*, solo existe un commit que añade `docs/preregistration_004.md` respecto a su padre, por lo que `introduced` es `[C1]`.
   - En un merge posterior con commit de merge `M` (por ejemplo, fusionando `prereg004/step3-port` en una rama donde `docs/preregistration_004.md` no existía), `git log` sin `-m`/`-c`/`--cc` no calcula diffs de commits de merge (`--diff-filter=A` solo filtra commits de un padre), mientras que `--full-history` recorre ambos padres y encuentra únicamente `C1` en la rama del pre-registro. Por tanto, `introduced` sigue siendo `[C1]`.
   - Si en C1 se usara `git mv` del borrador en lugar de añadir un fichero nuevo, la detección de renombrados de Git podría clasificar el cambio como `R` en vez de `A` y devolver `introduced == []` (fallo cerrado). El §9 (`docs/preregistration_004_draft.md:406-407`) prohíbe expresamente `git mv`.
3. **¿El test `test_second_c1_merged_with_ours_strategy_is_refused` puede fallar de verdad?** **Sí (demostrado).** En `tests/test_004_seed_manifest.py:162-193`, el test inicializa un repositorio Git real en `tmp_path`, crea `c1` y `alt` desde `base` añadiendo `FROZEN_DOC`, ejecuta `git merge -q -s ours --no-edit <c1>` desde `alt`, y llama a `manifest._check_freeze(candidate)` para `candidate in (alt, c1)`. Sin `--full-history`, para `candidate = alt`, `git log --diff-filter=A` devolvería `[alt]` y `git diff --exit-code <alt> -- *SEALED_PATHS` daría 0 (pues el árbol del merge `-s ours` es idéntico al de `alt`), por lo que `_check_freeze(alt)` terminaría sin lanzar excepción y `pytest.raises(RuntimeError, match="unique C1 commit")` **fallaría**.
4. **¿Queda otro modo de que dos commits distintos se presenten como C1?**
   - **En un mismo grafo de ancestros de `HEAD`:** cualquier segunda adición de `docs/preregistration_004.md` (ya sea en ramas paralelas fusionadas o tras borrar y recrear el fichero) produce `len(introduced) >= 2` bajo `--full-history --diff-filter=A` y es rechazada por `_check_freeze`. (Un "evil merge" que introdujera el fichero directamente en el commit de merge sin existir en ningún padre produciría `introduced == []` al no pasarse `-m`, siendo también rechazado).
   - **Fuera del grafo de ancestros o mediante manipulación de metadatos locales de Git:** reescribir la rama antes o después de C1 (`commit --amend`, `rebase`, `reset`, o ramificar de nuevo desde `C1^` sin fusionar el primer `C1`), o alterar localmente el grafo con `git replace` / clones superficiales (`.git/shallow`), haría que `git log --full-history` viera un único C1 distinto. Esto no lo puede impedir una consulta local a `git log`, sino el procedimiento vinculante del §9 (`docs/preregistration_004_draft.md:410-414`): hacer `push` de C1 y registrar su SHA completo en una nota firmada y publicada antes de ejecutar C2.

---

## 4. Reproducibility of published numbers

### Tarea 6: Procedencia de números
1. **Cifras de potencia del §7 (`docs/preregistration_004_draft.md:272-286`):** Tienen derivación analítica cerrada explícita en el propio texto a partir de `revisiones/2026-10-13-anclaje-theta-ciego/astra.md` y de las constantes congeladas de `nachocausal2p1/thresholds.py` (`TWO_M = 0.5`, `PERIMETER_EVAL = 1.4 * math.pi`, `K_LOC = 2`), y están rotuladas `[UNVERIFIED — closed-form arithmetic in a flat-local approximation, ρ^{-1/3} ≈ 0.2 not ≪ 2M; no simulation]`. Verificación aritmética directa:
   - $c_3 = \Gamma(4/3)(3/\pi)^{1/3} = 0.8929795\ldots \times 0.9847450\ldots = 0.879357\ldots \approx 0.879$.
   - $\lambda_r(2M) = c_3\rho^{2/3}\cdot 2\pi(0.5)\sqrt{2} = 3.90688\ldots\,\rho^{2/3} \implies \delta = 1/\lambda_r(2M) = 0.255959\ldots\,\rho^{-2/3} \approx 0.256\,\rho^{-2/3}$.
   - Cota $\theta_{\text{loc}}\cdot 2M = 2\rho^{-2/3}/(1.4\pi) = 0.454728\ldots\,\rho^{-2/3} \approx 0.455\,\rho^{-2/3} = 1.77656\ldots\,\delta \approx 1.78\,\delta$.
   - Para $\text{Gamma}(2,\delta)$: $P(W \le 1.78\delta) = 1 - 2.78\,e^{-1.78} = 0.5312 \approx 0.53$ ($0.5300$ con $1.77656\delta$); mediana $= 1.67835\,\delta \approx 1.678\,\delta = 0.9447 \approx 0.94$ de la cota; IQR $= (2.69263 - 0.96128)\delta = 1.73135\,\delta \approx 1.73\,\delta = 0.9746 \approx 0.97$ de la cota; en $\rho^* = 126$, $126^{-1/3} = 0.1995 \approx 0.2$.
2. **Tabla de θ en §7 (`docs/preregistration_004_draft.md:182-186`):** Los 6 valores (`0.09023`, `0.04511`; `0.05744`, `0.02872`; `0.03619`, `0.01809`) coinciden a 5 decimales con `thresholds.theta_loc(rho)` y `thresholds.theta_stab(rho)` (`nachocausal2p1/thresholds.py:194-207`).
3. **Recuentos de tests y SHAs:**
   - `docs/preregistration_004_draft.md:288` declara `20 tests` en `tests/test_004_criteria_can_fail.py`. El fichero adjunto contiene exactamente 20 funciones `def test_*` (18 previas + 2 nuevas en `tests/test_004_criteria_can_fail.py:280,297`).
   - `tests/test_004_seed_manifest.py` contiene 6 funciones `def test_*` simples más 1 parametrizada con 10 casos (`@pytest.mark.parametrize` en `:55-61`), sumando 16 ítems de test (15 previos + 1 nuevo en `:162`). Junto con los 28 tests de `tests/test_2p1_package.py`, suman los `64 passed` de `make test-004` en `mecanica.txt`.
   - Los 15 SHAs de §3 provienen del target `make verify-seal-004` (`Makefile:31-34`).

---

## 5. dev/validation separation & ground-truth leakage

### Tarea 3: Texto frente a código (§6, §7 y §9 vs `validate.py`, `thresholds.py`, `seed_manifest.py`)
Recorrido frase a frase de §6, §7 y §9 frente al código adjunto:
- **Concordancias verificadas:**
  - **§6 vs `thresholds.py`, `seed_manifest.py`, `validate.py`:** `ENSEMBLE = 20`, `MIN_VALID_SEEDS = 18` (`thresholds.py:102-103`); receta `default_rng(draw_seed).choice(np.arange(lo, hi + 1), size=20, replace=False)` ordenada con `VIRGIN_BAND = (8_000_000, 8_999_999)` (`seed_manifest.py:49-53`, `thresholds.py:112`); `draw_seed_from_commit` toma los primeros 8 dígitos hex en minúscula de un SHA de 40 caracteres (`thresholds.py:123-128`); `check_validation_seeds` verifica cardinalidad, disyunción y pertenencia a `VIRGIN_BAND` (`thresholds.py:133-146`); `validate.check_seed` (`validate.py:64-75`) bloquea `BURNED_PHASE_A_SEEDS`, admite `EXPLORE_BAND` (incluso tras congelar, como ahora aclara el §6 en `docs/preregistration_004_draft.md:167-170`) y exige `STATUS == "FROZEN"` más pertenencia a `thresholds.validation_seeds()` para semillas vírgenes, mientras que `validate.run` (`validate.py:257-259`) restringe la corrida `validation_004` exclusivamente a `tuple(validation_seeds)`.
  - **§7 vs `validate.py` y `thresholds.py`:** Precedencia de veredicto exacta: pre-guardas (`validate.run`, `validate.py:251-262`) > `OUT_OF_DOMAIN` (`t_edge < T_EDGE_MIN` en `validate.run`, `:263-268`) > excepciones no capturadas de Guard-v o `n > 256` en `per_seed` (`:119-120`) > `INCONCLUSIVE` evaluado en `verdict_from_levels` (`:213-217`) si cualquier nivel de `RHO_GRID` tiene `status != "scored"` (`len(ok) < 18` en `summarise_level`, `:171`), retornando sin diccionario `"checks"` > `PASS`/`FAIL` (`:218-243`). Las abstenciones de BH tienen `invalid=False` (`per_seed`, `:115-128`), entran en `ok` (`summarise_level`, `:139`) con `sep_BH = 0` y nunca causan `INCONCLUSIVE`. Con `n_clean == 1`, `np.median` está definida, `_iqr` devuelve `NaN` (`:54-55`) y `np.std` usa `ddof=0` devolviendo `0.0` (`:165`), lo que pasa `(iii)` pero falla `(ii)` en `PRIM = 126.0` y no impide `PASS` si ocurre en `ρ = 32` o `63` (`verdict_from_levels`, `:230-239`), tal como precisa ahora el §7 (`docs/preregistration_004_draft.md:236-241`).
  - **§9 vs `validate.py`, `seed_manifest.py`, `Makefile`:** Escritura atómica en `write_atomic` (`validate.py:307-321`), progreso ciego con `PROGRESS_FIELDS = ("seed", "rho", "seconds")` y línea `"start"` con hora local (`%z`, `:39, 282-283`), bloque de procedencia en `bash` con `export NUMBA_NUM_THREADS=20` previo y exclusión de líneas vacías del lockfile (`docs/preregistration_004_draft.md:361-379`), y targets `test-004`, `dry-run-004`, `verify-seal-004` presentes en `Makefile:25-34`.
- **Discrepancias y matices detectados entre texto y código (citando función):**
  1. **Contradicción interna entre §9 y §10 sobre revisiones cruzadas (`docs/preregistration_004_draft.md:425` vs `:474-485`) [WARN W1]:** En §9 ("Audit trail", `:425`, añadido en `007947e`) se afirma *"The only cross-family \*content\* review so far is Gemini O8 on `5afb33d` (§10)"*, pero el propio §10 (`:474-485`, añadido en `76da124`) documenta una segunda revisión cruzada de contenido por Gemini (`revisiones/2026-10-15-prereg004-c053-gemini/evaluacion.md`) sobre `007947e`.
  2. **Docstring desactualizado en `validate.py` (`nachocausal2p1/validate.py:26` vs `:153, :234` y `docs/preregistration_004_draft.md:234-235`) [WARN W2]:** El docstring del módulo `validate.py:26` sigue diciendo `* every pass test is written as x <= bound, so a NaN fails it (O8 review, D1);`, mientras que `summarise_level` (`validate.py:153`) usa `<` (`res["n_abstain_BH"] < thresholds.BH_ABSTAIN_FAIL`) y `verdict_from_levels` (`validate.py:234`) usa `>=` (`prim["coverage_frac"] >= thresholds.COVERAGE_FLOOR`). El §7 del borrador se corrigió, pero el docstring de `validate.py:26` quedó sin actualizar.
  3. **Valor precalculado de `escape_pass` con 0 semillas válidas, clave `v_order_only` en `checks` y guarda inalcanzable en `verdict_from_levels` (`validate.py:167-170, :223-225, :241` vs `docs/preregistration_004_draft.md:202, :212, :226-233, :263-264`):**
     - En `validate.summarise_level` (`validate.py:167`), si un nivel tiene 0 semillas válidas del generador (`len(ok) == 0`), el diccionario `levels[rho]` almacena `res["escape_pass"] = bool(0 <= 1)` = `True` (contradiciendo literalmente el comentario de `:170` *"Empty samples... cannot produce a PASS"* a nivel de campo individual, aunque el veredicto de corrida es `INCONCLUSIVE`). El §7 (`docs/preregistration_004_draft.md:231-233`) salva esta discrepancia ordenando que el documento de resultados calcule a mano los valores *non-verdict* bajo `INCONCLUSIVE` y reporte conteos sobre 0 semillas válidas como *"not evaluable"*.
     - En `validate.verdict_from_levels` (`validate.py:241`), el diccionario `"checks"` del JSON de salida sigue incluyendo una sexta clave `"v_order_only": bool(guard_ran)` aunque el §7 (`docs/preregistration_004_draft.md:202, 212`) declare que `(v)` es una precondición y no se contabiliza como criterio superado.
     - En `validate.verdict_from_levels` (`validate.py:223-225`), la rama `if a.get("status") != "scored" or b.get("status") != "scored":` dentro del bucle de convergencia F es código muerto inalcanzable porque las líneas `:213-217` retornan `INCONCLUSIVE` antes si cualquier nivel no es `"scored"`.
  4. **Nombres simbólicos en prosa frente a identificadores en Python (§6, §7, §9):** En §6 (`docs/preregistration_004_draft.md:148`), `VALIDATION_DRAW_SEED_004` designa el entero devuelto por `thresholds.draw_seed_from_commit(sha)` y guardado como `"draw_seed"` en `seed_manifest.py:57, 86`; en §7 (`:180, 209`), `slack(ρ)` designa `thresholds.convergence_slack(rho)` (`thresholds.py:210`) y la clave `"slack_over_2M"` (`validate.py:150`); en §9 (`:375`), el comando de procedencia imprime `thresholds.T_EDGE` (y `validate.run` en `:269` verifica `t_edge == generator.T_EDGE`).

### Tarea 4: Tests nuevos
- `test_inconclusive_takes_precedence_over_a_fail_of_i` (`tests/test_004_criteria_can_fail.py:280-294`): Verifica en `summarise_level` y `verdict_from_levels` que 3 abstenciones de BH en `PRIM = 126.0` (`significant == False`) combinadas con 17 < 18 semillas válidas en `ρ = 32.0` producen `verdict == "INCONCLUSIVE"` y ausencia de `"checks"`. No pasa por construcción.
- `test_one_clean_bracket_passes_iii_but_fails_ii` (`tests/test_004_criteria_can_fail.py:297-306`) y `test_nan_iqr_fails_ii_not_pass` (`:250-256`): Verifican con `n_clean == 1` en `PRIM` que `boundary_r_std == 0.0`, `stab_pass is True`, `iqr_width_over_2M` es `NaN`, `loc_inconclusive is True`, `checks["ii_localisation_primary"] is False` y `verdict == "FAIL"`. No pasan por construcción.
- `test_second_c1_merged_with_ours_strategy_is_refused` (`tests/test_004_seed_manifest.py:162-193`): Comprueba en un repositorio Git real el rechazo de `alt` y `c1` tras `git merge -s ours`; como se demostró en la Tarea 2.3, fallaría sin el arreglo en `seed_manifest._check_freeze`.

### Tarea 5 (parte 1): Separación y fugas de la verdad (`r`)
- Ningún cambio del delta permite que `r`, las anchuras o la cobertura lleguen al estimador o a una decisión antes del veredicto. En `validate.per_seed` (`validate.py:119-128`), `estimator.estimate` recibe únicamente la matriz de orden causal; `g["r"]` se pasa a `blind_bracket` exclusivamente después de fijar `bh["thr"]`. El log de progreso (`validate.py:39, 174-176`) solo escribe `seed, rho, seconds`.
- Ningún camino convierte una abstención (`valid=False`, `sep_BH=0`, anchura/IQR `NaN`), un `INCONCLUSIVE` (retorno anticipado en `validate.py:213-217`) o un `OUT_OF_DOMAIN` (retorno anticipado en `validate.py:263-268`) en `PASS`.

---

## 6. Claim-boundary check

### Tarea 5 (parte 2): Frontera de la afirmación científica
- El borrador (`docs/preregistration_004_draft.md:20-39`) limita estrictamente cualquier resultado a *"finite 2+1 equatorial patch localisation within frozen θ on the frozen ρ grid"* y excluye expresamente reconstrucción métrica, horizonte de sucesos, gravitación 2+1 de Einstein, extensión a 3+1 y afirmaciones para todo ρ o todo T.
- La declaración de baja potencia añadida en §7 (`docs/preregistration_004_draft.md:272-286`) es simétrica: establece que un `FAIL` se informa como `FAIL` sin calificativos post-hoc y prohíbe usar el resultado para re-derivar, reescalar o relajar `θ_loc`, `θ_stab` o `K_LOC`.

---

## 7. Findings

| # | Severity | Finding | Anchor |
|---|---|---|---|
| W1 | WARN | Contradicción interna en el borrador: el §9 ("Audit trail") afirma que *"The only cross-family \*content\* review so far is Gemini O8 on `5afb33d` (§10)"*, contradiciendo al §10 del mismo documento, que registra la segunda revisión cruzada de contenido con Gemini (`2026-10-15-prereg004-c053-gemini`) sobre `007947e`. Debe corregirse antes de sellar el texto en C1. | `docs/preregistration_004_draft.md:425` vs `docs/preregistration_004_draft.md:474-485` (`delta.diff` l. `+425`, `+474..+485`) |
| W2 | WARN | El docstring de `nachocausal2p1/validate.py` sigue afirmando que *"every pass test is written as `x <= bound`"* y que muestras vacías no pueden producir PASS, mientras que el código usa `<` en `summarise_level` (`n_abstain_BH < 3`), `>=` en `verdict_from_levels` (`coverage_frac >= 0.5`), y con 0 semillas válidas precalcula `levels[rho]["escape_pass"] = True` (`0 <= 1`, salvado manualmente en el informe según §7). | `nachocausal2p1/validate.py:26, 153, 167-170, 234` vs `docs/preregistration_004_draft.md:231-235` |
| OK1 | OK | Los 15 SHA256 de la tabla §3 coinciden con `make verify-seal-004` en `mecanica.txt`; `nachocausal/` permanece intacto; el único cambio en `nachocausal2p1/` es `--full-history` en `seed_manifest._check_freeze`, que cierra el resquicio G8 (`git merge -s ours`) sin romper el flujo legítimo. | `docs/preregistration_004_draft.md:100-118`; `nachocausal2p1/seed_manifest.py:43-45` |
| OK2 | OK | Los 3 tests nuevos (`test_inconclusive_takes_precedence_over_a_fail_of_i`, `test_one_clean_bracket_passes_iii_but_fails_ii`, `test_second_c1_merged_with_ours_strategy_is_refused`) comprueban lo que declaran y fallarían si la lógica probada se rompiera. | `tests/test_004_criteria_can_fail.py:280-306`; `tests/test_004_seed_manifest.py:162-193` |
| OK3 | OK | Las cifras de potencia del §7, la tabla de θ y los recuentos de tests (20 en `test_004_criteria_can_fail.py`, 64 en `make test-004`) son exactos y trazables a sus generadores o fórmulas cerradas. | `docs/preregistration_004_draft.md:182-186, 272-295`; `nachocausal2p1/thresholds.py:194-213` |
| OK4 | OK | Sin fuga de `r` al estimador ni al log de progreso; ningún camino convierte abstención, `INCONCLUSIVE` ni `OUT_OF_DOMAIN` en `PASS`; frontera de afirmación acotada al parche ecuatorial finito 2+1. | `nachocausal2p1/validate.py:39, 119-128, 213-217, 263-268`; `docs/preregistration_004_draft.md:20-39` |

AUDIT_ERRORS=0
AUDIT_WARNINGS=2

## 8. Verdict

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
