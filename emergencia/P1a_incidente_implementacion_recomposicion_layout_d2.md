# P1a — Incidente de implementación: reparación de reproducibilidad numérica

ESTADO = REGISTRO_DE_INCIDENTE (no es un resultado científico)
FECHA = 2026-08-27
FASE = `POST_HOC_EXPLORATORY_R2_VS_RGE5_MECHANISTIC_CONTRAST`
CONTRATO = `P1a_contrato_contraste_mecanistico_r2_rge5_d2.md` — **NO modificado**
(sha256 `0b85bb13f4eaa61b03a3311bdbb79ed8f686e4aefb4441efca42e9bbe55d1691`)

Este registro existe para que un auditor no tenga que reconstruir el incidente a
posteriori. No enmienda el contrato retroactivamente ni reinterpreta ninguna
cláusula congelada.

---

## 1. Estado de los intentos

| # | Instrumento | Desenlace |
|---|---|---|
| 1 | pre-reparo | terminado sin salida; ningún artefacto |
| 2 | pre-reparo | `ABORTED_BY_NUMERICAL_VALIDATION_FALSE_POSITIVE` |
| 3 | post-reparo | **único run científicamente interpretable** |

**Intento 1.** Lanzado como proceso en segundo plano hijo de la sesión de Claude.
La sesión se reinició y se llevó por delante al hijo. No se conservó log, de modo
que su causa de terminación **no es recuperable a partir de evidencia**; lo
observable es que no quedó proceso vivo, no se escribió ningún artefacto y el
directorio de resultados quedó intacto. Se registra como terminado sin salida,
no como aborto por control.

**Intento 2.** Relanzado desacoplado (`setsid nohup`). Completó los tres tamaños
(`n=22`, `n=24`, `n=40`; 100 000 réplicas cada uno; los tres `COMPLETE`) y abortó
en el control de auto-consistencia, **antes** de `write_artifacts`. Ningún
artefacto llegó a disco.

**Intento 3.** Relanzado con el instrumento reparado. Es el único cuyos números
son interpretables.

Los números vistos durante el diagnóstico del intento 2 **no constituyen
resultado científico** y no se propagan a ninguna conclusión.

---

## 2. Mensaje exacto del fallo

```
Traceback (most recent call last):
  ...
  File "emergencia/p1a_r2_vs_rge5_mechanistic_contrast_d2.py", line 673, in run_all
    controls = validate_results(results, summary_rows, long_data, source_validation)
  File "emergencia/p1a_r2_vs_rge5_mechanistic_contrast_d2.py", line 555, in validate_results
    validate_long_recomposition(long_data, summary_rows)
  File "emergencia/p1a_r2_vs_rge5_mechanistic_contrast_d2.py", line 525, in validate_long_recomposition
    raise RuntimeError("long recomposition disagrees with summary points")
RuntimeError: long recomposition disagrees with summary points
```

El guardarraíl actuó como debía: falló cerrado y bloqueó la escritura.

---

## 3. Diagnóstico: layout C frente a layout F

Las dos rutas parten de los mismos descriptores y difieren **solo** en la
disposición en memoria:

| ruta | construcción | layout |
|---|---|---|
| `summarize` → `_arrays` | `np.asarray([record.values …])` → `(N,6)` | C-contigua |
| `validate_long_recomposition` | `np.asarray(columns, …).T` | **F-contigua** |

`np.var(axis=0)` acumula en distinto orden según el layout una vez la columna
supera el bloque de suma *pairwise* de numpy. Como

$$d = \frac{\Delta}{\sqrt{\text{pooled\_var}}}$$

la varianza es el único punto donde entra la dependencia de layout, y `cohen_d`
la propaga. Por eso `μ` y `Δ` quedan intactos y solo `d` se desplaza.

### Igualdad bit a bit de los datos crudos

Reproducido sobre la muestra sellada real `n=22` (33 952 registros;
27 136 × 6 en `R_EQ_2`):

```
raw data identical A vs B: r2=True  rge5=True      (np.array_equal)
layout A: C=True  F=False
layout B: C=False F=True
```

Los datos son **idénticos bit a bit**. No hay discrepancia de datos, de orden de
filas ni de serialización: `_number` usa `.17g`, que hace round-trip exacto en
float64.

### Magnitud máxima observada del desacuerdo

De las 24 celdas `(observable × estadístico)` de `n=22`:

- las 6 `μ_R2`, las 6 `μ_Rge5` y las 6 `Δ` coinciden con `absdiff = 0.000e+00`,
  salvo `mean_orbit_size` (`3.109e-15`, muy por debajo del umbral);
- el desacuerdo se concentra íntegramente en `cohen_d`;
- **una sola celda cruza el umbral**: `primary_score`,
  `absdiff = 1.366e-13`, `reldiff = 1.834e-13`, contra `rel_tol = 1e-13`.

$$-0.74473082009872982 \;\longrightarrow\; -0.74473082009886638$$

Idénticos a 12 cifras significativas; sin interpretación científica.

**Alcance de lo verificado.** El diagnóstico se ejecutó **solo sobre `n=22`**,
que es el primer elemento de `N_VALUES` y por tanto el primero que evalúa el
bucle de validación, lo que es consistente con que fuera el disparador real del
aborto. **No se comprobó** si `n=24` o `n=40` presentaban además celdas fuera de
tolerancia: el control lanza en el primer desacuerdo.

Control independiente sobre datos sintéticos de la misma forma, aislando el
layout como única variable:

```
F-layout (pre-reparo)  bitwise-identical: False   worst cohen_d reldiff: 7.748e-14
C-layout (post-reparo) bitwise-identical: True    worst cohen_d reldiff: 0.000e+00
```

---

## 4. Diff exacto del reparo (única modificación)

```diff
@@ -504,7 +504,13 @@
             lengths = {len(column) for column in columns}
             if len(lengths) != 1:
                 raise RuntimeError("long artifact lost configuration-grain descriptors")
-            matrices[group] = np.asarray(columns, dtype=np.float64).T
+            # ``.T`` of a column stack is F-contiguous, and ``var(axis=0)``
+            # accumulates in a layout-dependent order; that shifted ``cohen_d``
+            # by ~1e-13 on bit-identical data.  Match the summary path's
+            # C-contiguous layout so the comparison is exact.
+            matrices[group] = np.ascontiguousarray(
+                np.asarray(columns, dtype=np.float64).T
+            )
         mu2, mu5, delta, d = point_statistics(
             matrices[GROUP_R2], matrices[GROUP_RGE5]
         )
```

`rel_tol=1e-13` **permanece intacto**. El control no se hizo pasar aflojando la
tolerancia: pasa por exactitud (0 ULP), que es un guardarraíl más fuerte que el
que había, no más débil.

---

## 5. Test añadido

`tests/test_p1a_r2_vs_rge5_mechanistic_contrast_d2.py::test_long_recomposition_matches_the_summary_memory_layout`

El test de recomposición preexistente usa 4 registros; por debajo del bloque de
suma *pairwise* ambas rutas suman igual, de modo que el defecto era **invisible**
para la suite. El margen real es marginal y depende de los datos: no se consiguió
fabricar una muestra sintética que cruzara `1e-13` de forma fiable, y un primer
intento de test de regresión **pasaba también sin el reparo** (comprobado).

Por eso el test final vigila el **invariante de layout** —que la recomposición
sea C-contigua y que los estadísticos coincidan bit a bit— en lugar de una
fixture calibrada para cruzar el umbral, que sería frágil y poco significativa.

Verificado en ambas direcciones:

```
sin reparo  → FAILED  AssertionError: recomposition drifted off the summary layout
con reparo  → 10 passed, 1 skipped
```

---

## 6. Estado del instrumento

| | sha256 |
|---|---|
| pre-reparo (abortó, intentos 1–2) | `012c8f77983638ed7a9c2d962721ae300f3a02f0bd347dbd5efc88114f12ce0a` |
| post-reparo (relanzado, intento 3) | `7f10a4343415faab1863c280648781156e2fa255980ea4410ba59c488276c6c6` |
| tests post-reparo | `dae1f57c6a3fbcc373ba532fa13af789b26ea7c315e780f7086c29cb7ca21a09` |

---

## 7. Afirmación explícita de invariancia

Entre el instrumento pre-reparo y el post-reparo **no cambiaron**:

- los datos ni la muestra (`N_MC = 100 000`, `N_VALUES = (22, 24, 40)`);
- las semillas (`SCIENTIFIC_SEED_BASE`, `BOOTSTRAP_SEED_BASE`, PCG64);
- los seis observables congelados ni sus unidades;
- la definición de $R$ ni la partición exacta por órbitas;
- el bootstrap (`BOOTSTRAP_REPLICATES = 1000`, `PERCENTILE_95_LINEAR`);
- los estadísticos (`μ`, `Δ`, Cohen $d$ con varianza agrupada);
- los umbrales científicos ni los criterios de éxito;
- las tolerancias de validación (`rel_tol=1e-13`, `abs_tol=1e-13`);
- el contrato.

La modificación normaliza el **orden de acumulación en coma flotante** de dos
rutas que parten de datos idénticos bit a bit. Es una reparación de
reproducibilidad numérica, no una decisión analítica.

---

## 8. Pendiente al cierre del intento 3

Auditar primero la cadena, y solo después los valores científicos:

$$\text{COMPLETE}_{22,24,40} \to \text{LONG\_RECOMPOSITION PASS} \to \text{artefactos} \to \text{hashes} \to \text{tests}$$

**Read-back desde disco: el control existe.** El control que falló opera sobre la
representación larga *en memoria* (`long_data`), no sobre el CSV serializado. El
control complementario —CSV realmente escrito → relectura independiente →
resumen— es
`test_completed_artifacts_are_sealed_and_recomposable`, que verifica los tres
sidecars con `baseline._verify_sidecar`, relee `summary` y `long` **desde disco**
y vuelve a ejecutar la recomposición sobre los bytes leídos. Está bajo
`@pytest.mark.skipif(not JSON.exists())` —es el `1 skipped` de todas las
ejecuciones previas de la suite— y **se arma solo** en cuanto exista el JSON.

No se añadió ni modificó ningún control durante el intento 3 en curso.
