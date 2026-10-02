# P1a — Contrato de robustez en K del fenómeno 22–24

ESTADO = CONGELADO_ANTES_DE_EJECUCION
FECHA = 2026-08-27
FASE = `POST_HOC_EXPLORATORY_K_ROBUSTNESS_OF_COMPETITION_PEAK`
NO EJECUTADO. Ninguna cifra nueva ha sido observada al redactar este contrato.

---

## 0. Procedencia exacta de `K0` (recuperación documental, sin inferencia)

**Valor:** `K0 = 3`.

**Definición única en el repositorio:**
`emergencia/p1a_enumeracion_simulacion.py:32`

| | |
|---|---|
| fichero | `emergencia/p1a_enumeracion_simulacion.py` |
| sha256 | `71594620005e2b83c22874a9a554a254755a468fd1c63429309d2264f79bda2b` |
| estado git | **tracked y limpio** (sin modificaciones locales) |
| commit | `0992277` — «emergencia: linea P1a (identificabilidad orden+numero, d=2) + resultado del canal CV-4» |

**Semántica operativa.** `K0` es un **suelo de admisibilidad sobre la
cardinalidad de intervalo**, no una escala ni un umbral estadístico. En el
selector congelado `MIN_COVERAGE_LEX`
(`p1a_orbital_backend_preflight_d2.py:122–143`), una cuádrupla candidata
`(a,b,c,d)` con `a ≺ b ≺ c ≺ d` es admisible **solo si**

```
past   = C[a,b] >= K0        y        future = C[c,d] >= K0
```

y su score es lexicográfico `(min(past,future), past+future)`, es decir
`primary_score = min(past,future)` y `secondary_score = past+future`.

**Consecuencia estructural, derivada del run ya cerrado.** Por construcción
`primary_score >= K0 = 3`. En la campaña cerrada, `mu_R2(primary_score)` vale
**3.71** en `n=22` y **3.98** en `n=24`, frente a **6.58** en `n=40`. Es decir,
**la ventana 22–24 es exactamente la región donde el selector opera pegado a su
propio suelo de admisibilidad**, mientras que en `n=40` opera lejos de él. Esto
es la motivación del presente test y **no** un resultado: es la razón a priori
para sospechar dependencia en `K`.

**¿Se ha probado alguna vez `K != 3`?** **No.** Búsqueda exhaustiva
(`grep -rn "K0\s*=\s*[0-9]"` sobre `*.py` y `*.md` en todo el repositorio):
cero ocurrencias de un valor distinto de 3. Todos los módulos que lo usan
—`p1a_estabilidad_d2.py`, `p1a_paisaje_niveles_d2.py`,
`p1a_orbital_backend_preflight_d2.py`, `p1a_macrotest_exploratorio_d2.py`—
importan la **misma** constante sellada de `p1a_enumeracion_simulacion`. Los
contratos previos lo declaran `K0 = 3 (INVARIABLE)` y «no se varía `K0`».
**No existen runs alternativos en `K`.**

**Aviso de homonimia — no confundir dos parámetros distintos.** El fichero
`resultados/p1a_macrotest_exploratorio_n_k_d2.csv` tiene una columna `k_retained`
que **no es `K0`**: es el número de posiciones retenidas bajo *thinning* iid,
un parámetro de coarse-graining. Este contrato **no** lo toca.

---

## 1. Hipótesis a falsar

> El extremo de la competencia observado en la ventana 22–24 es una propiedad
> del objeto combinatorio, y no la escala del propio selector.

Falsador mínimo: variar el suelo `K` y comprobar si **la localización en `n`**
del extremo se mantiene.

---

## 2. Observable primario (congelado, único)

```
p_n(K) = P(R >= 5 | E ; n, K)
```

donde `E` es el evento `M != empty` y `R` el número exacto de órbitas de
maximizadores. Es la columna `P_R_ge_5_given_E` del esquema ya existente.

**Es el único observable que decide el terminal.**

## 2b. Observables secundarios (solo concordancia)

`U_n^\star`, `Sbar_n_tie`, `H_tie_n`.

Se registran con sus IC95 y **no pueden alterar el terminal** bajo ninguna
circunstancia. Su función es exclusivamente documentar si acompañan o no al
primario. Queda prohibido promover un secundario a primario después de ver datos.

Ningún otro observable se añade. Ninguna métrica nueva se define.

---

## 3. Mallas congeladas

**Malla de `K`:** `K ∈ {2, 3, 4, 5}`.

- `K=3` es el ancla sellada (brazo de reproducción, §6).
- `K=2` es el único punto por debajo que mantiene intervalos con contenido
  múltiple (`K=1` degenera el suelo a «intervalo no vacío» y cambia la
  naturaleza del selector, no su escala).
- `K=4,5` son los dos primeros puntos por encima.

**Malla de `n`:** `n ∈ {20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40}`, es decir
`range(20, 41, 2)`, idéntica a la del run cerrado
(`p1a_orbital_curve_refinement_d2.py:28`). No se añade ni se quita ningún `n`.

**Muestreo:** `N_MC = 100_000` por `n`, semilla `260_828_000 + n`, idénticos al
run cerrado.

**Diseño pareado (congelado).** La semilla depende **solo de `n`, no de `K`**:
los cuatro brazos re-puntúan **exactamente la misma muestra de permutaciones**
bajo distinto suelo. La comparación entre `K` queda por tanto libre de ruido de
muestreo; toda diferencia observada es atribuible al suelo.

---

## 4. Ventana de referencia (derivada solo del run cerrado)

```
W = {22, 24}
```

**`W` se deriva EXCLUSIVAMENTE del observable primario `p_n` en `K=3`**, aplicando
la misma regla de meseta operacional de §5. Los secundarios **no participan** en
su definición: importar el argmin de `U_n^\star` volvería a mezclar primario y
secundarios, y queda prohibido.

Artefacto: `p1a_orbital_multiplicity_summary_d2.csv`, sha `a9e8a76d1329cc93…dac6f641`.

| n | `p_n = P(R≥5\|E)` | IC95 | ¿solapa con `n*`? |
|---|---|---|---|
| 20 | 0.06553 | [0.06389, 0.06720] | no |
| **22** | 0.07340 | [0.07174, 0.07510] | **sí** |
| **24** | 0.07608 | [0.07443, 0.07777] | **`n* = argmax`** |
| 26 | 0.07264 | [0.07104, 0.07427] | no |
| 28 | 0.07030 | [0.06872, 0.07190] | no |

`n* = 24` es el argmax observado del primario en la malla. La meseta operacional
de `p_n` en `K=3` es `{22, 24}`, y por tanto `W = {22, 24}`.

**Margen declarado.** `n=26` queda fuera por **1.6 × 10⁻⁴** en probabilidad
(`0.07427` frente a `0.07443`). El borde de `W` está decidido por un margen
estrecho. Se declara aquí y **no** se ensancha `W` por ello: la regla es la regla.
Un auditor debe saber que `W` habría sido `{22,24,26}` bajo un IC marginalmente
más ancho.

`W` queda congelada aquí y no se redefine después de ver datos.

---

## 5. Criterio de localización (congelado)

Para cada `K`, sobre la malla de `n`:

1. `n*(K) = argmax_n p_n(K)`. Si hay empate exacto, `n*(K)` es el conjunto de
   todos los argmax empatados.
2. **Meseta operacional** (`OPERATIONAL_PLATEAU`):
   `P(K) = { n : IC95(p_n(K)) solapa con IC95(p_{n*}(K)) }`,
   con `n*` cualquier elemento del argmax. Absorbe explícitamente los IC
   solapados: un `n` cuyo IC toca al del máximo no se considera distinguible
   de él.

   **Advertencia estadística, congelada con el resto del contrato.** El
   solapamiento de IC95 **marginales** es una *definición operacional* de
   meseta, y **NO** un intervalo de confianza al 95 % para la localización del
   argmax. No se le atribuye cobertura nominal, no se reporta como tal, y
   ninguna afirmación del informe puede leerse como «el máximo está en `W` con
   confianza 95 %». Para este falsador exploratorio no se sofistica más; si en
   el futuro hiciera falta un conjunto de confianza real para `argmax`, exigiría
   su propio contrato.

Clasificación del brazo `K`:

| resultado | condición |
|---|---|
| `MANTIENE` | `n*(K) ⊆ W` **y** `P(K) ∩ W ≠ ∅` |
| `DESPLAZA` | `P(K) ∩ W = ∅` (la meseta entera es disjunta de `W`) |
| `INDETERMINADO` | cualquier otro caso |

El criterio es **de localización en `n`, nunca de altura**: un cambio en el valor
de `p_n` que preserve la localización **no** cuenta como desplazamiento, y una
altura idéntica en otra posición **sí** cuenta.

### Censura declarada de antemano

Una celda `(n,K)` es **analizable** solo si el número de muestras con `M != empty`
es `>= 1_000`. Subir `K` aumenta la fracción `EMPTY`, y en el run cerrado
`1-E_n` ya vale 0.1413 en `n=20` con `K=3`; con `K=4,5` algunos `n` bajos pueden
volverse vacíos.

- Las celdas no analizables se **declaran censuradas**, nunca se descartan en
  silencio.
- Si la censura elimina algún punto de `W` en un brazo, ese brazo es
  `INDETERMINADO` por construcción — jamás `MANTIENE`.

---

## 6. Controles duros (fallo cerrado, sin escritura de artefactos)

- `K3_ARM_REPRODUCES_SEALED_CAMPAIGN`: el brazo `K=3` debe reproducir
  **exactamente** los `P(R≥5|E)`, `U_n^\star`, `Sbar_n_tie` y `H_tie_n` del
  artefacto sellado, en los 11 valores de `n`. Si falla, **todo el run es nulo**.
- `SEALED_SELECTOR_UNTOUCHED`: `p1a_enumeracion_simulacion.py` conserva el sha256
  `71594620005e2b83c2…f79bda2b`. `K` se inyecta por parámetro; **queda prohibido
  editar el fichero sellado**.
- `BACKEND_FAILURES = 0`.
- `PAIRED_SAMPLE_IDENTITY`: los cuatro brazos operan sobre las mismas
  permutaciones para cada `n`.
- `COUNTS_PARTITION_TOTAL`, `EXACT_R_FROM_N_ORBITS_ON_M`,
  `ORBIT_SIZES_PARTITION_M` como en los contratos previos.
- `LONG_RECOMPOSITION`: recomposición desde el CSV largo, **con la disposición
  C-contigua** fijada en `P1a_incidente_implementacion_recomposicion_layout_d2.md`.
- Read-back desde disco de los tres artefactos y sus sidecars.

---

## 7. Terminales (exactamente uno)

Lógica **conservadora**: el terminal afirmativo es el más difícil de obtener.

| terminal | condición |
|---|---|
| `K_DEPENDENT_LOCATION` | **algún** `K ≠ 3` analizable sitúa **toda** su meseta operacional fuera de `W` |
| `ROBUST_TO_K` | los **tres** brazos `K ∈ {2,4,5}` son analizables **y** los tres mantienen contacto con `W` |
| `INCONCLUSIVE_K_ROBUSTNESS` | cualquier censura o ambigüedad que impida decidir, **sin** desplazamiento demostrado |

Precedencia: `DESPLAZA` domina. Un solo desplazamiento demostrado falsa la
robustez, aunque los demás brazos la mantengan. `ROBUST_TO_K` **no** puede
emitirse con ningún brazo censurado o `INDETERMINADO`: en ese caso el terminal
es `INCONCLUSIVE_K_ROBUSTNESS`.

---

## 8. Salidas

CSV resumen por `(n, K, observable)`; CSV largo; JSON de diseño, procedencia,
controles y resultado; sidecars SHA-256; sin sobrescritura; tests focalizados.

---

## 9. Prohibiciones explícitas

- No se propone ni se evalúa **ningún otro selector** en este contrato.
- No se reinterpreta este test como continuación del problema abierto de
  Dou–Sorkin (2003): Dou (2023, `biblioteca/2307.04150v1.pdf`) declara las
  variantes Max/Min esencialmente agotadas y difiere la cuestión tras el
  bloqueo IR en dimensión superior. La motivación aquí es **el falsador mínimo
  de nuestra propia afirmación**, no herencia de aquel problema.
- No se emiten afirmaciones de escala crítica, transición, RG, universalidad,
  asintótica ni entropía física. `n*` es siempre «extremo observado en la malla».
- No se extrapola fuera de `n ∈ [20,40]` ni de `K ∈ {2,3,4,5}`.
