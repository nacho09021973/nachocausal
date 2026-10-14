<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ c12c10eb4de36669f2048754d2df20a9747adf1f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=high, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 f83f39410dc97de90d127abd91b75e176bbd14d2e7799e9958db6157620597f4
inicio: 2026-10-14T09:53:04Z  fin: 2026-10-14T09:57:23Z
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/docs/preregistration_004_draft.md ; último commit observado: 5afb33d ; sha256 de la copia enviada 88e3d82cd987ef62eec0758588da5a7095336761d7480a86fb9d33551e386508
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/thresholds.py ; último commit observado: 5afb33d ; sha256 de la copia enviada d576d47b41929be639fa901c30361d5aac9b27d8071059750e4a088dc7c054e6
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/validate.py ; último commit observado: 5afb33d ; sha256 de la copia enviada ecc5d9d39dd99734d4f58581b5c9867c7294ecade9d2be65e2c29fe8ea6cca41
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/estimator.py ; último commit observado: 2d71bc0 ; sha256 de la copia enviada 3a5010c403dd5083fcc2c4256c6e235ca092546d1e86dc83e3a980ecb4424ec4
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/gate.py ; último commit observado: 2d71bc0 ; sha256 de la copia enviada b688535636be2ac3a585fd34b5a2ed97481886452fac1be92de619f49124629c
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/scoring/scorer.py ; último commit observado: 2d71bc0 ; sha256 de la copia enviada b9097beb20a3c7e3457f756a5d2cb469172ff9022fbf4bef83febd754265d144
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/nachocausal2p1/generator.py ; último commit observado: 2d71bc0 ; sha256 de la copia enviada 5324a924f7ef923984841199249e9a571626004efbdf85ca6dcd006c97e88b55
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/tests/test_004_criteria_can_fail.py ; último commit observado: c16fb12 ; sha256 de la copia enviada f0ce62bca70f8cf6acf0773185f307b41e019da88804374a5b22ee5db6a3f0ad
documento: /home/ignac/nachocausal/.worktrees/prereg004-step3/tests/test_2p1_package.py ; último commit observado: 5afb33d ; sha256 de la copia enviada ada50f291a8b54895e96612729cf05f60b6e3f5fecd8c637e9ff2e17c3c6e866
entrada_gemini.txt sha256 c8417b274e80bb9a258f0b416651a30d58882b652343bf2369aae0d89c074d9e
respuesta sha256 f02bd65ce8dbdc453ca72b7d7320cfc1443b56fb73120f7bf69e0e631f031442
-->

### 1. Criterios que no pueden fallar (o que fallan/pasan por defectos de construcción)

Evaluación de las seis claves de `checks` en `validate.verdict_from_levels` (`nachocausal2p1/validate.py`):

1. **`i_significant_every_rho_ge_min`**
   * **Casi garantizado por construcción una vez superada la compuerta (demostrado en `validate.py:signflip_perm_p`, `estimator.py:estimate` y `validate.py:summarise_level`, asumiendo que `sealed.two_means_split` devuelve `sep > 0` cuando `improvement >= tau(n)`):** Si en una semilla el control plano (`MINK`) se abstiene (`sep_MINK = 0.0`) y `BH` no se abstiene (`sep_BH > 0`), entonces $d_i = \text{sep}_{\text{BH}} > 0$. Si `BH` y `MINK` se abstienen ambos, $d_i = 0.0$. En `signflip_perm_p`, cuando todos los $d_i \neq 0$ son positivos (de magnitud $> 10^{-12} n$), la media observada `obs` es el máximo global estricto sobre todas las asignaciones de signos salvo por los empates de los ceros ($+0 = -0$). Con $n_{\text{ok}} \ge 18$ semillas válidas y la regla `n_abstain_BH < 3` ($k \le 2$ ceros de `BH`), si `MINK` se abstiene en todas las semillas hay al menos $m = n_{\text{ok}} - k \ge 16$ valores $d_i > 0$. El valor $p$ exacto es entonces **idénticamente** $p_{\text{perm}} = 2^k / 2^{n_{\text{ok}}} = 2^{-m} \le 2^{-16} \approx 1.53 \times 10^{-5} \le 10^{-4}$, **con independencia absoluta del valor numérico de `sep_BH`**. Por tanto, `p_perm <= 1e-4` no aporta poder discriminante adicional sobre `n_abstain_BH < 3` y `n_escape_MINK <= 1`.
   * **Fallo trivial (demostrado en `validate.py:summarise_level` y `verdict_from_levels`):** Si el nivel secundario $\rho = 63$ tiene $< 18$ semillas válidas del generador (`status = "inconclusive"`), `summarise_level` retorna antes de definir `"significant"`. En `verdict_from_levels`, `levels[63].get("significant", False)` evalúa a `False` y convierte una invalidez del generador en $\rho = 63$ en un **`FAIL`** físico de `(i)`, en vez de `INCONCLUSIVE`.
   * **Cláusula correctora:** Declarar explícitamente que `p_perm` es un test de signo sobre decisiones de compuerta cuando `MINK` se abstiene, y en `verdict_from_levels` devolver `INCONCLUSIVE` si *cualquier* nivel requerido tiene `status == "inconclusive"`.

2. **`ii_localisation_primary`**
   * **Paso por exclusión de horquillas invertidas / `NaN` en IQR (demostrado en `validate.py:summarise_level`, `_iqr` y `scorer.py:blind_bracket`):** `widths` se filtra solo sobre `clean = [r for r in brk if r["clean"]]` (`width >= 0`). Las semillas con `valid=True` pero `width < 0` ($r_{\text{lo}} > r_{\text{hi}}$, clases solapadas radialmente) se descartan silenciosamente de la mediana y del IQR. Aunque en $\rho^* = 126$ la condición `coverage_frac >= 0.5` sobre `brk` obliga a tener al menos $\lceil 0.5 \times 16 \rceil = 8$ semillas que cubren $2M$ (y por `scorer.py`, `r_lo <= 0.5 <= r_hi` implica `width >= 0`, luego `clean=True`), hasta 10 de 20 semillas pueden tener `width < 0` y ser ignoradas al calcular `median_width_over_2M` e `iqr_width_over_2M`. Además, si en otro contexto `len(clean) == 1`, `_iqr` devuelve `NaN` y `res["loc_inconclusive"] = bool(nan > theta_loc)` evalúa a **`False`** en IEEE-754.
   * **Cláusula correctora:** Definir `loc_inconclusive = not (res["iqr_width_over_2M"] <= res["theta_loc"])` y exigir un mínimo de semillas `clean` (o calcular mediana/IQR sobre todas las `brk` penalizando `width < 0`).

3. **`ii_convergence_slack`**
   * **Paso vacío por `NaN` (demostrado en `validate.py:verdict_from_levels` y `summarise_level`):** En `verdict_from_levels`:
     ```python
     if b["median_width_over_2M"] > a["median_width_over_2M"] + a["slack_over_2M"]:
         slack_ok = False
     ```
     Si en $\rho = 32$ (donde el criterio `(i)` no aplica y pueden abstenerse las 20 semillas de `BH`) o en $\rho = 63$ hay $\ge 18$ semillas válidas del generador (`status == "scored"`) pero **ninguna horquilla es `clean`** (`len(clean) == 0`), entonces `median_width_over_2M` es `float("nan")`. En Python, cualquier comparación `x > float("nan")` es **`False`**. Por tanto, `slack_ok` permanece **`True`** y el criterio pasa de forma vacía.
   * **Fallo trivial:** Si $\rho = 32$ tiene $< 18$ semillas válidas del generador (`status == "inconclusive"`), `slack_ok` pasa a `False` y el veredicto global es **`FAIL`** (no `INCONCLUSIVE`).
   * **Cláusula correctora:** Cambiar la condición en `verdict_from_levels` a `if not (b["median_width_over_2M"] <= a["median_width_over_2M"] + a["slack_over_2M"]): slack_ok = False`, y devolver `INCONCLUSIVE` si algún nivel de la rejilla tiene `< MIN_VALID_SEEDS` semillas válidas.

4. **`iii_stability_primary`**
   * **Paso sesgado por filtrado `clean` (demostrado en `validate.py:summarise_level`):** `mids = np.array([r["midpoint"] for r in clean])` descarta las semillas con `width < 0` aunque su punto medio `0.5 * (r_lo + r_hi)` está bien definido en `brk`. Además usa `np.std(mids)` con `ddof=0`. Si `len(clean) == 1`, `np.std` vale `0.0 <= theta_stab` (aunque en $\rho^*$ la cobertura exige $\ge 8$ semillas limpias).
   * **Cláusula correctora:** Calcular `boundary_r_std` sobre `brk` (todas las semillas que reclaman frontera) con `ddof=1`, y usar `not (std <= theta_stab)`.

5. **`iv_flat_escapes_primary`**
   * **Casi garantizado por calibración de $\tau(n)$ (demostrado en `gate.py` y `thresholds.py`, sujeto a que $O$ en Minkowski no sea bimodal):** La tabla $\tau(n)$ se construye a $\alpha = 0.01$ bajo el nulo uniforme. Con tasa de falsos positivos $\approx 0.01$ por semilla en $N=20$, $\mathbb{P}(\text{escapes} \le 1) = 0.99^{20} + 20(0.01)(0.99)^{19} = 0.983$. Es solo un control de sanidad de la compuerta en $\rho^*=126$, como reconoce §7.

6. **`v_order_only`**
   * **100 % garantizado como `True` en cualquier veredicto `validation_004` (demostrado en `validate.py:run`, `verdict_from_levels` y `estimator.py:estimate`):** En `validate.run`, si `label == VALIDATION_LABEL` y `not guard`, se lanza `RuntimeError` antes de empezar. Si `guard=True` y `sealed.verify_order_only` falla en cualquier causet, lanza `ValueError` y **aborta el proceso sin escribir `results/validation_004.json`**. Por tanto, ningún fichero `validation_004.json` puede contener jamás `"v_order_only": false`.
   * **Cláusula correctora:** Capturar `ValueError` de `verify_order_only` en `per_seed`, registrar `guard_failed=True` y emitir `v_order_only: False` ($\implies$ `FAIL`) en el JSON final en lugar de abortar como si fuera una caída del sistema.

---

### 2. Fugas

1. **Hacia el estimador (demostrado sin fuga en el código adjunto):** En `validate.per_seed`, `estimator.estimate` recibe únicamente la matriz booleana `order` (`g["bh"]` o `g["mk"]`) y `guard_seed=int(seed)`. En `generator.sprinkle`, los vectores `t, r, phi` se muestrean i.i.d. sin ordenar, por lo que el índice de matriz $i \in \{0, \dots, N-1\}$ es estadísticamente independiente de $r$. `blind_bracket` (`scorer.py`) solo se invoca tras fijar `thr`.
2. **Fuga del veredicto en tiempo real hacia el operador mediante `PROGRESS_FIELDS` (demostrado en `validate.py:run_level`, `PROGRESS_FIELDS`):**
   Cada semilla escribe y hace `fsync` en `results/validation_004.progress.jsonl` con `("seed", "rho", "invalid", "abstained_BH", "abstained_MINK", "seconds")`. Aunque no incluye `r`, **revela el fallo del veredicto horas antes de que termine la corrida**:
   * En cuanto aparecen 3 líneas con `"abstained_BH": true` en $\rho = 63$ (tras ~1 h de las 4.4 h totales) o en $\rho = 126$, el operador sabe con certeza del 100 % que el criterio `(i)` y el veredicto global son **`FAIL`**.
   * En cuanto aparecen 2 líneas con `"abstained_MINK": false` en $\rho = 126$, sabe que `(iv)` y el veredicto global son **`FAIL`**.
   * En cuanto aparecen 3 líneas con `"invalid": true` en un nivel, sabe que ese nivel será `inconclusive` (`FAIL` en $\rho=32, 63$; `INCONCLUSIVE` en $\rho=126$).
3. **Incompatibilidad entre la regla de caídas (§9) y `validate.per_seed` (demostrado en `validate.py:per_seed`):**
   El §9 autoriza relanzar tras una caída *"only if no scoring output was produced"*. Sin embargo, `per_seed` ejecuta `blind_bracket(..., g["r"])` **en cada semilla dentro del bucle**, acumulando la puntuación en RAM (`rows`) desde la primera semilla de $\rho = 32$, aunque solo escribe el JSON al final de las 60 evaluaciones. Para cumplir §9 estrictamente, `validate.run` debería ejecutar primero la fase ciega de las 60 semillas/niveles, volcar a disco las particiones ciegas (`thr`, `min_idx`, `O_by_min`), y **solo al final** invocar `blind_bracket` leyendo `r`.

---

### 3. Texto frente a código

Discrepancias entre el borrador (§6–§10, y referencias de §3) y `thresholds.py` / `validate.py`:

1. **`validate.py` carece de punto de entrada CLI (`__main__`) y de `dry_run` (demostrado en `validate.py` y `thresholds.py`):**
   * El §9 establece: *"the single blind `python -m nachocausal2p1.validate` on the drawn seeds, with `guard=True`, is the only evaluation"*. Pero `validate.py` **no tiene bloque `if __name__ == "__main__":`**; ejecutar `python -m nachocausal2p1.validate` termina inmediatamente sin hacer nada.
   * El docstring de `thresholds.assert_environment` dice *"Called by validate.run and dry_run (not at import)"*, pero `dry_run` no existe en `validate.py`.
2. **Semillas quemadas de `prereg-001` y `prereg-002` no verificadas (demostrado en §6 frente a `thresholds.py:check_validation_seeds` y `validate.py:check_seed`):**
   * El §6 declara quemadas y bloqueadas las semillas de `prereg-001` y `prereg-002`, pero `thresholds.py` solo define y comprueba `EXPLORE_BAND = (7_000_000, 7_000_999)` y `BURNED_PHASE_A_SEEDS = (1, 2, 3, 4, 7, 99, 12345)`.
3. **Contradicción interna en §7 sobre abstenciones de `BH` en `(i)`:**
   * La tabla de §7, O5.1 (§10) y `thresholds.BH_ABSTAIN_FAIL = 3` permiten hasta 2 abstenciones de `BH` (`n_abstain_BH < 3`), pero el texto explicativo de §7 afirma: *"With the flat control abstaining, (i) reduces to 'no BH seed abstained'"* (0 abstenciones).
4. **Semillas inválidas en $\rho = 32$ o $\rho = 63$ producen `FAIL` en vez de `INCONCLUSIVE` (§6, §7, §9 frente a `validate.py:verdict_from_levels`):**
   * El §9 dice *"Invalid seeds (§3) count toward the < 18/20 INCONCLUSIVE rule"*, pero `verdict_from_levels` solo devuelve `INCONCLUSIVE` si falla el nivel primario ($\rho = 126$); si $\rho = 32$ o $\rho = 63$ tiene $< 18$ semillas válidas, devuelve `FAIL`.
5. **Omisión de "clean" en la tabla de §7 frente a `validate.py:summarise_level`:**
   * En §7, la tabla define para `(ii)` el IQR como *"IQR of widths/2M ≤ θ_loc"* y para la cláusula F *"m = median width/2M"*, sin especificar que `validate.py` calcula ambos exclusivamente sobre el subconjunto `clean` (`width >= 0`), no sobre todas las `bracket-valid`.
6. **Fichero de procedencia inexistente en el código (§9 frente a `validate.py`):**
   * El §9 especifica que `results/validation_004_provenance_launch.txt` registra UTC, SHAs, `git diff`, `git status --porcelain`, variables OMP/MKL, etc. Ninguna función del código adjunto genera ni verifica dicho fichero.
7. **Evidencia *can-fail* incompleta (§7 y §10 O6 frente a `test_004_criteria_can_fail.py`):**
   * El docstring de `test_004_criteria_can_fail.py` exige probar que *cada* criterio puede fallar individualmente, pero no incluye ningún test de fallo aislado para `i_significant_every_rho_ge_min` (p. ej. $\ge 3$ abstenciones de `BH`), ni para `ii_convergence_slack`, ni para `iii_stability_primary`, ni para `loc_inconclusive` (IQR).
8. **Nombre de constante en §6/§10 frente a `thresholds.py`:**
   * El §6 y la tabla O1 de §10 llaman a la semilla `VALIDATION_DRAW_SEED_004 = 20261014` (aunque §6 aclara entre paréntesis que en `thresholds.py` se llama `VALIDATION_DRAW_SEED`). Asimismo, el SHA de `thresholds.py` en §3 (`e7a699...`) es previo a los cambios O1/O3/O4 descritos en §10.

---

### 4. Diseño estadístico

1. **`p_perm` con `sep = 0` para `BH` abstenido y regla «$\ge 3$ abstenciones = FAIL de (i)»:**
   * Como se demostró en §1.1, truncar `sep = 0.0` mediante la compuerta ($\alpha = 0.01$) hace que $\ge 98\%$ de las semillas `MINK` tengan $\text{sep}_{\text{MINK}} = 0$. Cuando `MINK` se abstiene, el signo de $d_i$ depende solo de si `BH` supera la compuerta ($d_i > 0$) o se abstiene ($d_i = 0$). Con $n_{\text{ok}} \ge 18$ y $< 3$ abstenciones de `BH`, hay al menos 16 diferencias positivas y ninguna negativa, forzando $p_{\text{perm}} \le 2^{-16} < 10^{-4}$ con independencia de la magnitud de $\text{sep}_{\text{BH}}$. El test de permutación no mide la magnitud de la separación frente al control plano; solo recuenta aperturas de compuerta.
2. **Sesgo de selección en la cobertura sobre `bracket-valid` (`brk`):**
   * En `validate.py:summarise_level`, `brk` excluye las semillas donde `BH` se abstiene (`valid=False`). Si `BH` se abstiene en 2 semillas (permitido por `< 3`), el denominador de `coverage_frac` baja a 18, permitiendo pasar con 9/20 (45 %) semillas totales cubriendo $2M$. Además, un suelo de `0.5` sobre 18–20 semillas carece de potencia frente a coberturas reales bajas (con cobertura verdadera $0.35$, $\text{Bin}(18, 0.35)$ alcanza $\ge 9$ aciertos el $16.3\%$ de las veces).
3. **Acoplamiento de flujo PRNG no declarado entre niveles de $\rho$ (`ii_convergence_slack` y `(i)`):**
   * **Demostrado en `validate.py:generate` y `generator.py:sprinkle`:** Se pasan las **mismas 20 semillas enteras** `s` a `np.random.default_rng(s)` en $\rho = 32, 63, 126$. En `sprinkle`:
     ```python
     n = rng.poisson(n_mean)
     t = rng.uniform(0.0, T_EDGE, n)
     r = np.sqrt(rng.uniform(R_LO ** 2, R_HI ** 2, n))
     phi = rng.uniform(0.0, 2.0 * math.pi, n)
     ```
     Tras extraer `n`, los tres niveles consumen la **misma secuencia de flotantes uniformes $u_1, u_2, \dots$** con longitudes $n(32) \approx 2702$, $n(63) \approx 5320 \approx 2 n(32)$ y $n(126) \approx 10641 \approx 4 n(32)$. En consecuencia, los primeros $n(32)$ valores de $t$ en $\rho = 63$ y $\rho = 126$ son idénticos a $t$ en $\rho = 32$; ¡y el segundo bloque de $n(32)$ valores de $t$ en $\rho = 63$ y $\rho = 126$ son exactamente los mismos números pseudoaleatorios que generaron la coordenada radial $r^2$ en $\rho = 32$! No son ni sembrados independientes ni adelgazamientos de Poisson anidados, sino realizaciones con acoplamiento cruzado entre coordenadas $(t, r, \phi)$ a través de $\rho$. Debe usarse `np.random.default_rng((seed, int(rho)))`.
4. **Sesgo de supervivencia sobre horquillas `clean` (`width >= 0`):**
   * Filtrar `widths` y `mids` por `clean` (`r_hi >= r_lo`) elimina de `median_width_over_2M`, `iqr_width_over_2M` y `boundary_r_std` precisamente aquellas semillas en las que las dos clases estimadas se solapan en $r$ (`max(lo_r) > min(hi_r)`). En $\rho^* = 126$ hasta el 60 % de las semillas pueden ser no limpias y quedar ocultas de la mediana de anchura y de la desviación típica del punto medio; en $\rho = 32, 63$ no hay cota inferior alguna sobre `n_clean`.

---

### 5. Corrida única y reproducibilidad

1. **Las 20 semillas «vírgenes» de C2 ya están determinadas antes de congelar C1 (demostrado en `thresholds.py` y §6/§10):**
   * `VALIDATION_DRAW_SEED = 20261014` y el algoritmo exacto de extracción están ya fijados en el código antes de C1. Cualquier persona puede ejecutar hoy esas 3 líneas de NumPy, conocer las 20 semillas de `VALIDATION_SEEDS` antes de congelar los umbrales en C1 y evaluarlas fuera de registro. Para que el sorteo C2 sea genuinamente ciego y posterior a C1, la semilla de sorteo debe derivarse de un artefacto posterior al sellado (p. ej., los primeros 8 bytes del SHA256 del commit de congelación C1).
2. **Resquicio de ejecución sin escritura a disco (`write=False`, demostrado en `validate.py:run`):**
   * `validate.run(seeds=None, label=VALIDATION_LABEL, guard=True, write=False)` supera todos los controles de `VALIDATION_LABEL` pero **no crea `results/validation_004.json` ni `results/validation_004.progress.jsonl`**, permitiendo ejecutar la corrida ciega en memoria tantas veces como se quiera. En `validate.run`, bajo `label == VALIDATION_LABEL`, debe exigirse `if not write: raise RuntimeError(...)`.
3. **Dependencia del entorno y paralelismo:**
   * En `generator.py:transitivity_violations`, `A @ A` en `float32` ($N \approx 10641$) invoca BLAS (`OpenBLAS`/`MKL`), cuyos hilos (`OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `OPENBLAS_NUM_THREADS`) no están fijados en `thresholds.assert_blind_threads()`.
   * En `generator.py:stage1` y `shoot_pairs_fast`, los bucles `@njit(parallel=True)` (`prange`) escriben en índices disjuntos sin reducciones entre hilos, por lo que fijar `NUMBA_NUM_THREADS=20` en la misma CPU (`i7-13700`) es determinista salvo que cambie la microarquitectura SIMD/FMA (no verificada por `assert_environment()`).
   * En `gate.py:tau`, si una sola semilla en $\rho = 126$ supera `n_minimal > 256`, `ValueError` aborta toda la corrida sin escribir el JSON de resultado, dejando la corrida en un limbo indistinguible de una caída.

---

### 6. Veredicto global

**Veredicto: NO LISTO.**

Defectos ordenados por gravedad (de bloqueante a menor):

1. **[Bloqueante — Semillas C2 predecibles antes de C1]** `VALIDATION_DRAW_SEED = 20261014` está fijada antes de congelar el pre-registro (`thresholds.py`, §6). Las 20 semillas vírgenes pueden calcularse y probarse antes de C1. *Solución:* derivar `VALIDATION_DRAW_SEED` en C2 a partir del hash SHA256 del commit de congelación C1.
2. **[Bloqueante — Paso vacío por `NaN` en `ii_convergence_slack` e IQR]** En `validate.py:verdict_from_levels` y `summarise_level`, `b["median_width_over_2M"] > a["median_width_over_2M"] + ...` y `iqr > theta_loc` evalúan a `False` cuando hay `NaN` (`n_clean == 0` en $\rho=32, 63$ o `n_clean < 2`), haciendo que los criterios pasen de forma vacía. *Solución:* negar comparaciones `<=` (`not (x <= bound)`) y exigir un mínimo de semillas `clean`.
3. **[Bloqueante — `validate.py` no es ejecutable como `-m` y permite `write=False` en `VALIDATION_LABEL`]** `python -m nachocausal2p1.validate` (§9) no hace nada porque falta `if __name__ == "__main__":`, y `validate.run(..., write=False)` permite correr `validation_004` sin dejar rastro en disco.
4. **[Grave — Acoplamiento PRNG entre niveles de $\rho$]** `generate(seed, rho)` inicializa `default_rng(seed)` sin incluir `rho`, reutilizando los mismos números aleatorios desplazados entre las coordenadas $(t, r, \phi)$ de $\rho = 32, 63, 126$. *Solución:* `np.random.default_rng((int(seed), int(rho)))`.
5. **[Grave — Sesgo de supervivencia por filtrado `clean` (`width >= 0`)]** Descartar las horquillas invertidas (`width < 0`) al calcular la mediana/IQR de anchura y la desviación típica del punto medio oculta los fallos de separación radial.
6. **[Grave — Fuga de estado de fallo en `.progress.jsonl` y puntuación en RAM antes de finalizar]** `PROGRESS_FIELDS` permite saber en vivo si `(i)` o `(iv)` ya han fallado horas antes de acabar, mientras `blind_bracket` ya ha leído `r` en memoria en cada semilla contra la regla de caídas de §9.
7. **[Moderado — Semillas inválidas en $\rho = 32, 63$ producen `FAIL` en vez de `INCONCLUSIVE`, y aborto por `n > 256` o `Guard-v`]** `verdict_from_levels` solo comprueba `status != "scored"` en `PRIMARY_RHO` para `INCONCLUSIVE`; y los fallos de `verify_order_only` o `n_minimal > 256` abortan el proceso sin escribir el JSON de veredicto.
8. **[Menor — Discrepancias documentales y de tests]** Faltan las semillas quemadas de `prereg-001/002` en `thresholds.py`, el generador de `validation_004_provenance_launch.txt`, la función `dry_run`, corregir la frase *"no BH seed abstained"* en §7, y añadir a `test_004_criteria_can_fail.py` los tests de fallo aislado para `(i)`, `(ii)-slack`, `(ii)-IQR` y `(iii)`.
