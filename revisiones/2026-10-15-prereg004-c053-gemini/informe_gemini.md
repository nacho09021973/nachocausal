<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ c12c10eb4de36669f2048754d2df20a9747adf1f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=high, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 571ffe438318a6485d77f655adc7005f084bb9770b0ac90749712838bb6fda2f
inicio: 2026-10-15T07:35:09Z  fin: 2026-10-15T07:40:25Z
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/docs/preregistration_004_draft.md ; último commit observado: 007947e ; sha256 de la copia enviada 7c39399d727bcec7cb433af5d37bfd7efafc04146083b6833e87a0736e565155
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/thresholds.py ; último commit observado: 782d031 ; sha256 de la copia enviada 2bf954fb1164f94b42b2e34512aac1d10d5e76e77915b15c14a640bf7186908e
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/validate.py ; último commit observado: 782d031 ; sha256 de la copia enviada ad68e34b11fe758f8a28ed943ae91d9d43f85806038514e2fa8871b3aa19f4e6
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/seed_manifest.py ; último commit observado: 782d031 ; sha256 de la copia enviada e4047104d9683331e90e6826737dd77c6d0d187302b8bc6f6b7e7766e26aecf8
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/estimator.py ; último commit observado: 2d71bc0 ; sha256 de la copia enviada 3a5010c403dd5083fcc2c4256c6e235ca092546d1e86dc83e3a980ecb4424ec4
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/gate.py ; último commit observado: 2d71bc0 ; sha256 de la copia enviada b688535636be2ac3a585fd34b5a2ed97481886452fac1be92de619f49124629c
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/scoring/scorer.py ; último commit observado: 2d71bc0 ; sha256 de la copia enviada b9097beb20a3c7e3457f756a5d2cb469172ff9022fbf4bef83febd754265d144
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/tests/test_004_criteria_can_fail.py ; último commit observado: 007947e ; sha256 de la copia enviada 2cb3a795318deed34c7e5e1e1871dfd3b8898fe262ea9fd17a84b1e88790bc13
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/tests/test_004_seed_manifest.py ; último commit observado: 782d031 ; sha256 de la copia enviada 437c7cf7bf0d290250e99eafd7c8a727069d3b9fa811f93f0d9d1f50ef088dbc
entrada_gemini.txt sha256 9faf03a82612165340b6e28a23b468abbb423ce4c6ec2239442a3ee7107fd673
respuesta sha256 df2917b8533035153c4898aea0650952e604d0766ac04a7c2fbd7c1b8772dbd5
-->

### 1. Precedencia del veredicto

El texto del §7 coincide con el comportamiento real de `validate.run` (`validate.py:249-296`) y `validate.verdict_from_levels` (`validate.py:210-243`):

1. **Pre-guardas de ejecución (`validate.run`, l. 251-262):** Antes de evaluar el dominio o generar causets, el código verifica el entorno (`thresholds.assert_environment`), la existencia y validez de las semillas (`check_seed`), las restricciones de la etiqueta `validation_004` (`write=True`, `guard=True`, `STATUS == "FROZEN"`, coincidencia con `validation_seeds()`, inexistencia previa de `results/validation_004.json`) y los hilos (`thresholds.assert_blind_threads`). Cualquier fallo aquí lanza `RuntimeError` o `ValueError` antes de crear el archivo de progreso.
2. **`OUT_OF_DOMAIN` (`validate.run`, l. 263-269):** Se evalúa inmediatamente después de las pre-guardas y antes de `run_level`. Si `t_edge < thresholds.T_EDGE_MIN` (`10.0`), devuelve `{"verdict": "OUT_OF_DOMAIN", ...}` sin ejecutar el generador. Con `T_EDGE = 16.0` congelado, esta rama es inalcanzable en la corrida ciega.
3. **`ABORTED_GUARD_V` / `ABORTED_TAU_RANGE` (`estimator.estimate`, l. 36; `gate.abstains` / `gate.tau`, l. 43-53):** Durante `run_level` → `per_seed`, si falla `sealed.verify_order_only` (tratado como auditado) o si `gate.tau(n)` recibe `n > 256`, se lanza una excepción que detiene la corrida antes de `verdict_from_levels` y antes de `write_atomic`.
   * *Matiz sobre el código:* Los literales `"ABORTED_GUARD_V"` y `"ABORTED_TAU_RANGE"` **no existen en el código Python**; son etiquetas procedimentales (§9) para documentar la excepción en el informe de resultados.
   * *Matiz sobre `n < 2`:* En `gate.abstains` (`gate.py:50-51`), si `n < 2` devuelve `True` (abstención) sin llamar a `tau(n)`. Por tanto, `n ∈ {0, 1}` produce abstención y no aborto `ABORTED_TAU_RANGE`, lo cual coincide con el texto del §3 y §9 (`n > 256` / `n_minimal > 256`).
4. **`INCONCLUSIVE` antes que (i)-(iv) y sin `checks` (`validate.verdict_from_levels`, l. 212-217):** `verdict_from_levels` calcula `short = [rho for rho in thresholds.RHO_GRID if levels[rho].get("status") != "scored"]` como primera instrucción y, si no es vacía, retorna `{"verdict": "INCONCLUSIVE", "reason": ...}` sin construir el diccionario `checks` ni evaluar (i)-(iv).
5. **Las abstenciones de BH nunca causan `INCONCLUSIVE` (`validate.per_seed`, l. 113-128; `validate.summarise_level`, l. 139, 170):** En `per_seed`, `row["invalid"]` depende exclusivamente de `generate(seed, rho)`. Si el generador es válido y BH se abstiene (`bh["abstained"] == True`), se asigna `abstained_BH=True` y `valid=False`, pero `invalid` permanece `False`. En `summarise_level`, `ok = [r for r in rows if not r["invalid"]]`, por lo que `len(ok)` (`n_generator_valid`) incluye todas las abstenciones de BH. Si hay `< 18` semillas válidas del generador es `INCONCLUSIVE`; si hay `≥ 18` y `≥ 3` abstenciones de BH en `ρ ≥ 63`, `res["significant"]` es `False` y produce `FAIL` en (i).

**¿Hay algún camino hacia un estado no listado o un PASS espurio?**
* No hay ningún camino en `verdict_from_levels` que produzca `PASS` cuando el texto exige `FAIL` o `INCONCLUSIVE`.
* En `validate.generate` (`validate.py:80-83`), solo se captura `AssertionError` de `generator.bh_order` para marcar la semilla como `invalid=True`. Cualquier otra excepción no capturada en `generator.py` (no adjunto) abortaría el proceso sin escribir `results/validation_004.json`.

---

### 2. NaN y muestras pequeñas

1. **Comparaciones con `NaN` (`validate.summarise_level`, l. 151-168; `validate.verdict_from_levels`, l. 218-235):**
   * Todas las condiciones de paso usan operadores IEEE-754 directos (`<=`, `>=`, `<`) que evalúan a `False` ante `NaN`:
     * (i): `res["p_perm"] <= thresholds.P_PERM_THRESHOLD` (`NaN <= 1e-4` es `False` cuando `ok` es vacío).
     * (ii) anchura: `res["median_width_over_2M"] <= res["theta_loc"]` (`False` si `n_clean == 0`).
     * (ii) IQR: `res["loc_inconclusive"] = not bool(res["iqr_width_over_2M"] <= res["theta_loc"])` y en `verdict_from_levels` se exige `not prim["loc_inconclusive"]`. Si `n_clean < 2`, `_iqr` (`validate.py:51-57`) devuelve `NaN`, `NaN <= theta_loc` es `False`, `loc_inconclusive` es `True` y `not prim["loc_inconclusive"]` es `False`.
     * (ii) cobertura: `prim["coverage_frac"] >= thresholds.COVERAGE_FLOOR` (`False` si `n_bracket_valid == 0`).
     * (ii) convergencia F: `if not (b["median_width_over_2M"] <= a["median_width_over_2M"] + a["slack_over_2M"]): slack_ok = False` (`slack_ok` pasa a `False` si `a` o `b` tiene mediana `NaN`).
     * (iii) estabilidad: `res["boundary_r_std"] <= res["theta_stab"]` (`False` si `n_clean == 0`).
2. **Caso de exactamente una horquilla limpia (`n_clean == 1`):**
   * En `summarise_level` (`validate.py:157-166`), con `n_clean == 1`, `np.median(widths)` está definida, `_iqr(widths)` devuelve `NaN` (`x.size < 2`) y `np.std(mids)` usa `ddof=0` por defecto en NumPy, devolviendo `0.0 <= theta_stab` (`stab_pass = True`).
   * **Imprecisión del texto en §7 (niveles secundarios):** El §7 afirma: *«With exactly one clean bracket the median is defined, the IQR is NaN and the midpoint std is 0.0, not NaN: (iii) then passes on its own, but (ii) fails through the IQR, so the run cannot PASS»*. Esto es cierto **solo si la horquilla limpia única ocurre en el nivel primario `ρ* = 126`**. En `verdict_from_levels` (`validate.py:229-234`), el IQR (`loc_inconclusive`) y `stab_pass` se evalúan únicamente en `prim` (`ρ* = 126`). Si `ρ = 32` o `ρ = 63` tiene `n_clean == 1` (con `≥ 18` semillas válidas, p. ej. 17 horquillas invertidas `width < 0` y 1 limpia) y `ρ = 126` tiene `n_clean ≥ 2`, la mediana en el nivel secundario no es `NaN`, su IQR `NaN` no se consulta en `verdict_from_levels`, y la corrida **sí puede dar `PASS`**. El texto debe especificar *«At ρ\*, with exactly one clean bracket...»*.
3. **¿Hay algún criterio que pase en vacío (`n_generator_valid == 0`)?**
   * Si un nivel tiene 0 semillas válidas del generador (`len(ok) == 0`), el veredicto global es `INCONCLUSIVE`. Sin embargo, en `summarise_level` (`validate.py:145, 168`), `n_escape_MINK` vale `0`, por lo que `res["escape_pass"] = bool(0 <= 1)` evalúa a **`True`** en vacío (y `n_abstain_BH = 0 < 3` también se cumple, aunque `significant` da `False` porque `p_perm` es `NaN`). Por tanto, al reportar bajo `INCONCLUSIVE` el valor *non-verdict* que habrían tomado (i)-(iv) (§7), el criterio (iv) (`escape_pass`) pasa en vacío cuando `ok` está vacío en `ρ*`.
4. **Precondición (v):**
   * Bajo `label == "validation_004"`, `validate.run` (`validate.py:255-256`) rechaza `guard=False` con `RuntimeError`, y un fallo de `verify_order_only` aborta la ejecución. No puede ser `False` en un JSON de validación. Conviene notar que `verdict_from_levels` (`validate.py:241`) sigue incluyendo `"v_order_only": bool(guard_ran)` dentro del diccionario `checks` del JSON de salida, aunque el §7 aclare que conceptualmente es una precondición y no se cuenta como criterio superado.

---

### 3. Resto del texto frente al código (§6, §7, §9)

1. **Reporte *non-verdict* de (i)-(iv) bajo `INCONCLUSIVE` y código muerto en cláusula F (§7 vs `validate.verdict_from_levels`, l. 213-225):**
   * El §7 dice: *«Under INCONCLUSIVE, the result document also reports, from the recorded level aggregates, the value each clause (i)-(iv) would have taken, labelled non-verdict»*.
   * `verdict_from_levels` retorna en la línea 215 antes de calcular `checks`, por lo que `results/validation_004.json` **no contiene** esos valores *non-verdict* a nivel de corrida; deben transcribirse manualmente en `docs/preregistration_004_result.md` a partir de `levels[rho]`.
   * Además, en `verdict_from_levels` (`validate.py:223-225`), el bucle de `ii_convergence_slack` contiene código muerto:
     ```python
     if a.get("status") != "scored" or b.get("status") != "scored":
         slack_ok = False
         break
     ```
     Nunca se ejecuta porque las líneas 213-217 ya retornaron `INCONCLUSIVE` si algún nivel no es `"scored"`. El texto del §7 debe dejar claro que bajo `INCONCLUSIVE` el valor *non-verdict* de la cláusula F en el documento de resultados evalúa la desigualdad `m(ρ_{k+1}) ≤ m(ρ_k) + slack(ρ_k)` de los agregados registrados, ignorando ese `status != "scored"`.
2. **Reducción de (i) y (iv) a conteos de la puerta (§7 vs `validate.summarise_level` y `verdict_from_levels`):**
   * El §7 afirma: *«With the flat control abstaining, `d ≥ 0` on every seed and the exact sign-flip test gives `p = 2^-m`... So (i) reduces to "fewer than 3 BH seeds abstained" at each required level»*.
   * Suponiendo que la primitiva sellada 1+1 `two_means_split` devuelve `sep > 0` siempre que `improvement >= tau(n)`, la igualdad `p_perm = 2^-m` es exacta **solo cuando ninguna semilla del control plano escapa** (`n_escape_MINK == 0`) en ese nivel (con `n_valid ≥ 18` y `< 3` abstenciones de BH, `m ≥ 16`, dando `p_perm ≤ 2^-16 = 1.53e-5 ≤ 1e-4`).
   * Sin embargo, (iv) permite hasta 1 escape plano en `ρ* = 126` (`MAX_MINK_ESCAPES = 1`, `thresholds.py:137`) y **no restringe en absoluto** `n_escape_MINK` en `ρ = 63` (`verdict_from_levels` evalúa `iv_flat_escapes_primary` solo en `prim`, `validate.py:238`). Si hay `≥ 1` escape plano en `ρ = 63` o 1 escape en `ρ = 126`, `d` puede ser negativo o menor que `obs` al permutar signos, y (i) deja de reducirse al mero conteo de abstenciones de BH.
3. **Definición de *bracket-valid* (§4 y §7 vs `scorer.blind_bracket`, l. 19-21, y `validate.per_seed`, l. 124-127):**
   * El §1, §7 y §10 usan el término *«bracket-valid seeds»* (`n_bracket_valid`), pero el §4 no enuncia su condición exacta en código: una semilla tiene `valid=True` si y solo si es válida en el generador (`not invalid`), BH no se abstiene (`not abstained_BH`) **y** ambas clases del corte (`O < thr` y `O >= thr`) son no vacías en `scorer.blind_bracket`.
4. **Semillas de exploración en `validate.check_seed` tras congelar (§6 vs `validate.check_seed`, l. 67-68):**
   * El §6 declara que la banda de exploración está quemada (*«Burned and never reusable: the whole exploration band...»*), pero `validate.check_seed` permite `EXPLORE_BAND` (`7_000_000..7_000_999`) incondicionalmente incluso cuando `STATUS == "FROZEN"`. La corrida C3 está protegida porque `validate.run` (`validate.py:258`) exige `tuple(seeds) == tuple(validation_seeds)` bajo `VALIDATION_LABEL` y `thresholds.check_validation_seeds` exige `VIRGIN_BAND`.
5. **Nombres simbólicos y tabla de θ (§6, §7 vs `thresholds.py`):**
   * En §6 se llama `VALIDATION_DRAW_SEED_004` al entero que en `thresholds.py` y `seed_manifest.py` se obtiene mediante `draw_seed_from_commit(sha)` y se guarda como `"draw_seed"`. En §7 se escribe `slack(ρ)` para la función `thresholds.convergence_slack(rho)` (campo `"slack_over_2M"` en `summarise_level`).
   * Los 6 valores numéricos de la tabla de `theta_loc` y `theta_stab` en §7 para `ρ ∈ {32, 63, 126}` coinciden exactamente (a las 5 cifras decimales mostradas) con `thresholds.theta_loc` y `thresholds.theta_stab`.

---

### 4. C1→C2→C3

**Lo que impide el código (`seed_manifest.py`, `thresholds.py`, `validate.py`):**
* Impide ejecutar C2 o C3 si `STATUS != "FROZEN"`, si el entorno no coincide con los *pins*, si el árbol de trabajo tiene cambios o archivos no ignorados sin confirmar (`git status --porcelain`), o si `nachocausal/`, `nachocausal2p1/` o `docs/preregistration_004.md` difieren respecto a `freeze_commit` (`git diff --exit-code`).
* Impide usar un commit posterior arbitrario de la misma rama lineal como `freeze_commit`, porque `_check_freeze` (`seed_manifest.py:40-42`) exige que `git log --diff-filter=A --format=%H -- docs/preregistration_004.md` devuelva exactamente `[freeze_commit]`.
* Impide modificar `docs/validation_004_seeds.json` sin confirmarlo en `HEAD` (`load_manifest`, l. 72) o elegir semillas distintas de las que dicta `_draw(freeze_commit)`.
* Impide sobrescribir `results/validation_004.json` si ya existe en disco (`validate.py:261`).

**Lo que solo impide el procedimiento y grados de libertad residuales:**
1. **Minado de SHA antes de publicar C1 (reconocido en §6, solo procedimental):** Como `draw_seed_from_commit` toma los primeros 8 dígitos hexadecimales del SHA de C1, el autor puede variar localmente la marca temporal o el mensaje del commit C1 antes de hacer `push` para previsualizar las 20 semillas (o probarlas en otra copia). El código no puede detectarlo.
2. **Simplificación de historial de Git en `_check_freeze` (`seed_manifest.py:40`, hueco en código pero con rastro en Git):**
   * `_check_freeze` ejecuta `git log --diff-filter=A --format=%H -- docs/preregistration_004.md` **sin `--full-history`**.
   * En Git, `git log -- <ruta>` por defecto activa la *simplificación de historial* en merges: si en un commit de merge `M` el archivo `<ruta>` es idéntico al de uno de sus padres (p. ej. el primer padre), Git poda el otro padre y no recorre su historial.
   * Si alguien ramifica desde el padre de C1 (`C1^`), crea un commit alternativo `C1_alt` añadiendo exactamente el mismo `docs/preregistration_004.md` e instrumento (pero con distinta fecha → distinto SHA → otras 20 semillas), y fusiona el `C1` original como segundo padre (`git merge -s ours C1`), entonces:
     * `C1` sigue estando en el historial del merge (cumpliendo en apariencia la regla de *merge commit*),
     * pero `git log --diff-filter=A --format=%H -- docs/preregistration_004.md` sigue únicamente la rama del primer padre y devuelve **`[C1_alt]`** (un único SHA), pasando todas las comprobaciones de `seed_manifest.py` sin lanzar error.
   * **¿Deja rastro?** Sí: deja rastro evidente en el grafo de Git (`git log --graph --full-history` mostraría ambos commits `C1` y `C1_alt`) y contradiría el SHA de C1 anotado y firmado antes de C2 (§9). *(Nota: añadir `"--full-history"` en `seed_manifest.py:40` cerraría este hueco en el propio código).*
3. **Borrado local de `results/` para repetir u ocultar C3 (solo procedimental):**
   * En `validate.run` (`validate.py:251-291`), cada llamada a `per_seed` → `generate` → `check_seed` invoca `thresholds.validation_seeds()` → `seed_manifest.load_manifest()`, que exige `git status --porcelain` vacío (60 veces durante la corrida). Por eso `results/` **tiene** que estar en `.gitignore`.
   * Como consecuencia, `results/validation_004.json`, `.progress.jsonl`, `_run.log` y `_provenance_launch.txt` no están rastreados por Git hasta el `git add -f` manual posterior a la corrida. Si se borra `results/` tras un fallo o aborto, Git no guarda rastro. No obstante, una vez fijado C2, repetir la corrida en el mismo host y con 20 hilos es determinista y producirá el mismo resultado (no permite obtener otras 20 semillas).

---

### 5. Declaración de potencia de (ii)

* **Verificación aritmética (exacta):**
  * $c_3 = \Gamma(4/3)(3/\pi)^{1/3} = 0.89298 \times 0.98475 = 0.87936 \approx 0.879$.
  * Con $2M = 0.5$, $\lambda_r(2M) = c_3 \rho^{2/3} \cdot 2\pi(0.5)\sqrt{2} = 3.90688\,\rho^{2/3}$, luego $\delta = 1/\lambda_r(2M) = 0.25596\,\rho^{-2/3} \approx 0.256\,\rho^{-2/3}$.
  * Cota: $\theta_{\text{loc}}\cdot 2M = 2\rho^{-2/3}/(1.4\pi) = 0.45473\,\rho^{-2/3} \approx 0.455\,\rho^{-2/3}$.
  * Cociente cota/$\delta$: $0.45473 / 0.25596 = 1.7766 \approx 1.78\,\delta$.
  * Para $W \sim \text{Gamma}(2, \delta)$: $P(W \le 1.78\delta) = 1 - (1 + 1.78)e^{-1.78} = 0.531 \approx 0.53$ ($0.530$ con $1.7766$).
  * Mediana poblacional: solución de $(1+u)e^{-u} = 0.5 \Rightarrow u = 1.6783\,\delta \approx 1.678\,\delta$, que es $1.6783/1.7766 = 0.9447 \approx 0.94$ de la cota.
  * IQR poblacional: $u_{0.75} - u_{0.25} = (2.6926 - 0.9613)\delta = 1.7314\,\delta \approx 1.73\,\delta$, que es $1.7314/1.7766 = 0.9746 \approx 0.97$ de la cota.
  * En $\rho^* = 126$, $\rho^{-1/3} = 126^{-1/3} = 0.1995 \approx 0.2$. Con 20 semillas i.i.d. cuya mediana e IQR poblacionales están en $0.945$ y $0.975$ de la cota, la probabilidad conjunta de que la mediana muestral y el IQR muestral caigan ambos por debajo de la cota ronda efectivamente el 50 %.
* **Simetría de la redacción:** Es estrictamente simétrica. Las frases *«A FAIL is reported as FAIL, with no qualifier added after the result»* y *«No result of this run may be used to re-derive, rescale or loosen θ_loc, θ_stab or K_LOC, here or in any successor pre-registration»* cierran cualquier puerta a reinterpretar un `FAIL` como «casi PASS por baja potencia» o a relajar umbrales después.

---

### 6. Comandos de procedencia del §9

El bloque de shell del §9 tiene **tres defectos concretos**:

1. **`NUMBA_NUM_THREADS=20` no queda registrado en el volcado de `env` del archivo de procedencia:**
   * Dentro del bloque `{ ... } > $F 2>&1`, se ejecuta `env | grep -E '^(NUMBA_|OMP_|MKL_|OPENBLAS_|NC2P1_)' | sort`.
   * Sin embargo, `NUMBA_NUM_THREADS=20` solo se define como prefijo en la línea posterior de lanzamiento (`NUMBA_NUM_THREADS=20 nohup $PY -m nachocausal2p1.validate ...`). Si `NUMBA_NUM_THREADS=20` no se ha exportado antes (`export NUMBA_NUM_THREADS=20`), `env | grep ...` en el bloque de procedencia no capturará `NUMBA_NUM_THREADS=20`.
2. **Sustitución de procesos `<(...)` en un bloque etiquetado ```` ```sh ````:**
   * La línea `diff <(sort /tmp/pf.txt) <(grep -v '^#' requirements-lock.txt | sort)` usa sustitución de procesos `<(...)`, que es sintaxis exclusiva de `bash`/`zsh`. Si se ejecuta bajo `/bin/sh` POSIX (en Ubuntu/WSL2 `/bin/sh` es `dash`), falla con `Syntax error: "(" unexpected`. Debe ejecutarse en `bash` (y etiquetarse ```` ```bash ````) o usar un archivo temporal.
3. **Posibles líneas en blanco en `requirements-lock.txt`:**
   * `grep -v '^#' requirements-lock.txt | sort` conserva las líneas vacías si existen en el archivo, haciendo que `diff ... | wc -l` sea distinto de 0 frente a `pip freeze`. Es más seguro `grep -vE '^(#|$)' requirements-lock.txt | sort`.

---

### 7. Veredicto global

**Veredicto: «listo con cambios menores enumerados»** (todos resolubles en el texto del borrador antes de C1 sin tocar los archivos de `nachocausal2p1/`, cuyos SHAs candidatos ya están fijados):

1. **(Medio — §9, bloque de comandos de procedencia):** Exportar `export NUMBA_NUM_THREADS=20` *antes* del bloque `{ ... } > $F 2>&1` (o incluirlo explícitamente) para que `env | grep ...` lo registre realmente en `validation_004_provenance_launch.txt`; cambiar ```` ```sh ```` a ```` ```bash ```` (por el uso de `<(...)`) y usar `grep -vE '^(#|$)' requirements-lock.txt`.
2. **(Menor — §7, alcance del caso `n_clean == 1` y vaciedad en conteos):** Precisar que la afirmación *«With exactly one clean bracket... (ii) fails through the IQR, so the run cannot PASS»* se refiere a **una horquilla limpia en `ρ* = 126`** (en `ρ = 32` o `63` el IQR no interviene en `verdict_from_levels`), y aclarar que con 0 semillas válidas del generador (`INCONCLUSIVE`), los conteos como `n_escape_MINK = 0 <= 1` dan `True` en vacío aunque las estadísticas basadas en `NaN` den `False`.
3. **(Menor — §7, cláusulas *non-verdict* bajo `INCONCLUSIVE`):** Aclarar que los valores *non-verdict* de (i)-(iv) bajo `INCONCLUSIVE` los calcula el informe `docs/preregistration_004_result.md` a partir de `levels[rho]` (y no `verdict_from_levels`, que retorna antes de construir `checks` y contiene una guarda inalcanzable `status != "scored"` en `slack_ok`).
4. **(Menor — §7 y §4, precisión descriptiva):** En §7, recordar junto a la reducción de (i) a `p = 2^-m` que en `ρ = 63` el código no evalúa (iv) y en `ρ = 126` permite 1 escape plano; en §4, explicitar que `bracket-valid` (`valid=True` en `scorer.blind_bracket`) exige semilla válida del generador, no abstención de BH y conjuntos `lo_r` y `hi_r` no vacíos; y en §9 (procedimiento C1/C2), exigir que la verificación de historial de C1 incluya `git log --full-history --diff-filter=A -- docs/preregistration_004.md` para descartar merges con simplificación de historial.
