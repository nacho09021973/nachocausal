# Paper III — Fase 1: batería de modelos sobre la pierna intervalar no restringida

```text
REPORT_ID=PAPER_III_F1_MODEL_BATTERY
DATE=2026-09-10
MODE=EXPLORATORY
STATUS=UNSIGNED_EXPLORATION
NEW_SIMULATIONS=NONE
NEW_SEEDS=NONE
NEW_N=NONE
NEW_RHO=NONE
NEW_OBSERVABLES=NONE
INPUTS=COMMITTED_ARTIFACTS_ONLY
CONVENTION=PAPER_III_R001
ERROR_MODEL=PAPER_III_R005
CHANNEL=UNRESTRICTED_ONLY
MINIMAL_CHANNEL=SUSPENDED_R004
SIGNS_NOTHING=TRUE
```

Este documento es **exploración, no confirmación**. No firma R007, no fija
`alpha`, no elige un modelo físico, no abre la Fase 1 y no toca ninguna puerta.
Es el mapa de qué familias de corrección de tamaño finito son siquiera
*distinguibles* con los datos ya comprometidos, antes de que nadie decida qué
medir.

## 0. Qué se ha usado y qué no

Entradas, exclusivamente artefactos comprometidos y certificados en el paso 1 de
la secuencia obligatoria de [R001 §5](paper_iii_resolucion_001_convencion_L.md):

| artefacto | sha256 (certificado en el contrato) | papel |
|---|---|---|
| `dev/explore_3p1_bg_reference_precision_results.json` | `eb101d3f…91e7` | pierna de **precisión**, 4 `N`, 8 semillas — **canal principal** |
| `dev/explore_3p1_bg_reference_results.json` | `5dbb04bc…7bc6` | pierna **base**, 6 `N`, 3 semillas — contraste |

No se ha ejecutado ningún generador. No se ha añadido ninguna semilla, ningún
`N`, ningún `rho`, ningún observable. Las únicas operaciones sobre los datos son
aritmética de ajuste sobre las `Ls` ya guardadas.

**Canal de minimales: no utilizado.** Queda suspendido por
[R004](paper_iii_resolucion_004_lineas_base_minimales.md) y excluido de la
calibración primaria por [R002 C3](paper_iii_resolucion_002_reescopado_fase1.md).
Ninguna cifra de este informe procede de él, ni para seleccionar modelos ni para
interpretar `alpha`.

### 0.1 Elecciones declaradas antes de mirar los ajustes

1. **Convención `L`.** R001: `L = |cadena|`, extremos incluidos. Sobre las `Ls`
   guardadas eso es `+2`. Verificado: la pendiente log-log OLS no ponderada sobre
   `⟨L⟩` reproduce exactamente la tabla de R001 §3.1 — `0.2552` (precisión) y
   `0.2516` (base).
2. **Modelo de error.** R005, literal: la `sd` **no** se estima punto a punto
   sino agrupada sobre el barrido. Se usa `sd_pool = sqrt(mean(sd_i²))` por
   pierna, y `sem = sd_pool/sqrt(n_rep)`, idéntica en unidades de `L` en todos
   los puntos. En la variable de trabajo `y = L/N^(1/4)` eso da
   `sigma_y = sem / N^(1/4)`. **No se ha construido ningún otro modelo de error.**
   El único punto donde se usa la `sem` punto a punto está marcado
   `DIAGNOSTIC_ONLY` y sirve precisamente para mostrar por qué R005 la prohíbe.
3. **Dominio de `alpha` en M4.** Declarado **antes** del ajuste:

   ```text
   ALPHA_DOMAIN = [0.05, 2.00]
   ```

   Razón, y es puramente geométrica sobre el rango corrido, no física: por debajo
   de `0.05` el factor `N^(-alpha)` varía menos de un 25 % entre `N = 500` y
   `N = 32000`, es decir se vuelve indistinguible de una constante y se degenera
   exactamente con `m₄`; por encima de `2.00` la corrección queda confinada al
   `N` más pequeño y se degenera con un desplazamiento de un solo punto. El
   dominio es la ventana en la que el término es *siquiera* un término.
4. **Banda rigurosa.** `1.8555 ≤ m₄ ≤ 2.5296`. Se reporta el ajuste libre marcado
   `UNCONSTRAINED_DIAGNOSTIC_ONLY` y, cuando cae fuera, el ajuste restringido.
5. **Suelo de ruido del diseño.** Se calibra explícitamente la distribución de
   `Δχ²` que produce el propio diseño cuando la verdad *es* una constante, con
   las `sigma` de R005. Ninguna comparación de modelos se interpreta sin
   contrastarla contra ese suelo. **No se usa R² en ninguna parte de este
   informe.**

### 0.2 Reproducibilidad

Este informe es autocontenido: el **Apéndice A** trae el script completo y el
**Apéndice B** su salida íntegra. Extrayendo A y corriéndolo desde la raíz del
repositorio contra los dos JSON comprometidos se reobtiene B carácter a carácter
(la parte Monte Carlo lleva semilla fija `20260910`).

```text
script sha256 = 6fb171f1de9cbc2a0aaf60a1e55e46031bb3f8526b64a9bb8fab98f8a7ea1997
comando       = python3 fase1_model_battery.py      (desde la raiz del repo)
```

---

## 1. OBSERVED

Lo que dicen los datos antes de ajustar nada.

### 1.1 Pierna de precisión (8 semillas) — canal principal

```text
n_points = 4    n_replicas = 8    sd_pool = 0.9933 (28 dof)    sem_L = 0.3512
```

| `N` | `⟨L⟩` (R001) | `sd` | `y = L/N^(1/4)` | `sigma_y` |
|---|---|---|---|---|
| 2 000 | 14.6250 | 1.0607 | 2.18695 | 0.05251 |
| 8 000 | 20.0000 | 0.5345 | 2.11474 | 0.03713 |
| 16 000 | 24.6250 | 1.1877 | 2.18951 | 0.03122 |
| 32 000 | 29.6250 | 1.0607 | 2.21499 | 0.02626 |

### 1.2 Pierna base (3 semillas) — contraste

```text
n_points = 6    n_replicas = 3    sd_pool = 0.8819 (12 dof)    sem_L = 0.5092
```

| `N` | `⟨L⟩` (R001) | `sd` | `y` | `sigma_y` |
|---|---|---|---|---|
| 500 | 10.3333 | 1.1547 | 2.18523 | 0.10768 |
| 1 000 | 11.3333 | 0.5774 | 2.01538 | 0.09055 |
| 2 000 | 13.6667 | 0.5774 | 2.04364 | 0.07614 |
| 4 000 | 17.3333 | 1.1547 | 2.17955 | 0.06403 |
| 8 000 | 19.6667 | 0.5774 | 2.07950 | 0.05384 |
| 16 000 | 24.0000 | 1.0000 | 2.13394 | 0.04527 |

### 1.3 Tres hechos observados, sin modelo

**O1 — `y` no es monótona en ninguna de las dos piernas.** En precisión baja en
`N = 8000` y vuelve a subir. En base el valor **más alto** de todo el barrido
está en el `N` **más pequeño** (`N = 500`, `y = 2.185`). Una familia
`m₄(1 + c N^(-alpha))` con `c` de signo fijo es monótona por construcción.
Ninguno de los dos barridos exhibe esa monotonía. Lo que se ve es dispersión, no
una aproximación ordenada.

**O2 — la dispersión total del barrido es del tamaño de la barra de error.** En
precisión `y` recorre `2.115 … 2.215`, un `+4.7 %`, con `sigma_y` entre `0.026` y
`0.053`, es decir un `1.2 %`–`2.4 %` por punto. Con cuatro puntos, eso no es una
curva: es un rango de dos a cuatro sigmas repartido entre cuatro medidas.

**O3 — `L` es un entero pequeño y hay empates severos.** En `N = 8000` seis de
las ocho réplicas valen lo mismo, y su `sd` muestral sale la mitad que la de los
otros tres puntos. Ésta es exactamente la patología que motivó la cláusula de
`sd` agrupada de R005, y §6 muestra que es la que gobierna toda la comparación
de modelos si se la deja actuar.

---

## 2. DESCRIPTIVE_FIT

Ajuste por mínimos cuadrados ponderados con las `sigma` de R005. `AIC = χ² + 2k`
con las `sigma` tratadas como conocidas; la constante aditiva es común a todos
los modelos, luego sólo las diferencias significan algo.

### 2.1 Pierna de precisión (canal principal)

| modelo | `k` | `χ²` | dof | `χ²/dof` | `Δχ²` vs M0 | AIC | AICc | `m₄`/`A` | `c`/`beta` | banda |
|---|---|---|---|---|---|---|---|---|---|---|
| **M0** `y = m₄` | 1 | 4.905 | 3 | 1.64 | — | 6.91 | 8.91 | 2.1844 | — | IN |
| M1 `N^(-1/4)` | 2 | 3.767 | 2 | 1.88 | 1.138 | 7.77 | 19.77 | 2.2586 | −0.3544 | IN |
| M2 `N^(-1/2)` | 2 | 4.152 | 2 | 2.08 | 0.753 | 8.15 | 20.15 | 2.2113 | −1.3362 | IN |
| M3 `N^(-1)` | 2 | 4.648 | 2 | 2.32 | 0.257 | 8.65 | 20.65 | 2.1911 | −28.372 | IN |
| M4 `alpha` libre | 3 | 3.422 | 1 | 3.42 | 1.483 | 9.42 | **UNDEF** | 2.6512 | −0.2844 | **OUT** |
| M5 `L = A N^beta` | 2 | 3.315 | 2 | 1.66 | 1.590 | 7.31 | 19.31 | 1.9558 | 0.2615 | n/a |

`M0` ajusta con `p = 0.179`; `m₄ = 2.1844 ± 0.0168`, dentro de la banda.

**M0 y M5 están anidados exactamente.** `M0` *es* `M5` con `beta` fijado en
`1/4`: con `sigma_L` constante, `Σ((L/N^(1/4) − m₄)/sigma_y)² = Σ((L − m₄N^(1/4))/sigma_L)²`.
Verificado numéricamente (`4.9051` en ambas parametrizaciones, ambas piernas).
Por tanto **todos** los `χ²` de la tabla viven en una única escala y `Δχ²` es
directamente comparable, incluido el de M5.

### 2.2 Pierna base

| modelo | `k` | `χ²` | dof | `χ²/dof` | `Δχ²` vs M0 | AIC | AICc | `m₄`/`A` | `c`/`beta` | banda |
|---|---|---|---|---|---|---|---|---|---|---|
| **M0** | 1 | 4.118 | 5 | 0.82 | — | 6.12 | 7.12 | 2.1111 | — | IN |
| M1 | 2 | 3.965 | 4 | 0.99 | 0.153 | 7.97 | 11.97 | 2.1461 | −0.1348 | IN |
| M2 | 2 | 4.031 | 4 | 1.01 | 0.087 | 8.03 | 12.03 | 2.1233 | −0.3617 | IN |
| M3 | 2 | 4.114 | 4 | 1.03 | 0.004 | 8.11 | 12.11 | 2.1123 | −1.6265 | IN |
| M4 | 3 | 3.915 | 3 | 1.31 | 0.203 | 9.92 | 21.92 | 2.3282 | −0.1432 | IN |
| M5 | 2 | 3.903 | 4 | 0.98 | 0.215 | 7.90 | 11.90 | 2.0135 | 0.2555 | n/a |

`M0` ajusta con `p = 0.532`. En esta pierna la constante no sólo sobrevive: **no
deja residuo que ningún término de corrección pueda comprar.** `M3` mejora el
`χ²` en `0.004` a cambio de un parámetro.

### 2.3 Residuos, en unidades de sigma

Precisión:

```text
       N=2000   N=8000  N=16000  N=32000
  M0    +0.05    -1.88    +0.16    +1.16
  M1    +0.91    -1.60    +0.07    +0.62
  M2    +0.79    -1.71    +0.05    +0.77
  M3    +0.51    -1.85    +0.07    +0.99
  M4    +0.98    -1.49    +0.10    +0.48
  M5    +1.00    -1.45    +0.11    +0.44
```

Ningún residuo pasa de `1.9 sigma` en ningún modelo, y **el patrón de residuos es
el mismo en los seis**: todos dejan `N = 8000` bajo y `N = 32000` alto. Las
familias de corrección no reorganizan la estructura del residuo; sólo le quitan
medio sigma al mismo punto. Eso es la firma de un término que está absorbiendo
ruido de un punto, no describiendo una tendencia.

Base:

```text
       N=500   N=1000  N=2000  N=4000  N=8000 N=16000
  M0   +0.69    -1.06   -0.89   +1.07   -0.59   +0.50
  M5   +0.94    -0.84   -0.73   +1.13   -0.67   +0.23
```

Residuos alternantes en signo, sin deriva sistemática con `N`.

### 2.4 El suelo de ruido del diseño

Calibración Monte Carlo de `Δχ²` **bajo la hipótesis de que la verdad es una
constante**, con las `sigma` de R005 y la geometría exacta del barrido de
precisión (400 000 realizaciones, semilla `20260910`). Esto no genera datos
físicos: es la distribución nula del propio estadístico de comparación.

Un parámetro extra:

```text
  P50 = 0.457    P68 = 0.992    P90 = 2.712    P95 = 3.852    P99 = 6.612
```

Dos parámetros extra (`M0 -> M4`, con `alpha` perfilada sobre el dominio
declarado):

```text
  P50 = 0.787    P68 = 1.434    P90 = 3.386    P95 = 4.681    P99 = 7.730
```

Y ahora lo observado, contra ese suelo:

| comparación | `Δχ²` observado | percentil del ruido | `p(≥ obs)` |
|---|---|---|---|
| M0 → M1 | 1.138 | 71.4 | **0.286** |
| M0 → M2 | 0.753 | 61.4 | **0.386** |
| M0 → M3 | 0.257 | 38.6 | **0.614** |
| M0 → M4 | 1.483 | 68.9 | **0.311** |
| M0 → M5 | 1.590 | 79.2 | **0.207** |

**Ninguna familia llega siquiera al percentil 80 del ruido que este diseño
produce por sí solo cuando no hay nada que encontrar.** La mejora más grande de
toda la batería, `Δχ² = 1.590`, ocurre por azar una de cada cinco veces. La
diferencia entre el mejor y el peor modelo de corrección (`1.590` frente a
`0.257`) es más pequeña que la diferencia entre dos realizaciones del ruido.

### 2.5 Sobre AICc — y por qué no se usa

`AICc = AIC + 2k(k+1)/(n−k−1)`.

- **Pierna de precisión, `k = 3` (M4): `n − k − 1 = 0`. AICc es indefinido.** No
  se reporta un número, se reporta `UNDEF`. Con cuatro puntos, un modelo de tres
  parámetros está fuera del dominio de validez de la corrección de muestra
  pequeña, y forzarla sería inventar una cifra.
- **Pierna de precisión, `k = 2`: AICc = AIC + 12.** Está definido, pero el
  término de corrección (`12`) es **ocho veces mayor** que el `Δχ²` más grande de
  toda la batería (`1.590`). El orden que produce AICc lo decide íntegramente el
  recuento de parámetros; los datos no participan.
- **Pierna base:** `+4` para `k = 2`, `+24` para `k = 3`. Mismo problema, más
  suave.

```text
AICc_USED_AS_EVIDENCE = NO
AICc_STATUS = UNDEFINED_FOR_K3_AT_N4 ; PARAMETER-COUNT-DOMINATED_FOR_K2
```

La comparación se hace contra la nula del diseño (§2.4), que sí está bien
definida a este `n`. Que AICc y esa nula coincidan en el veredicto es una
comprobación, no el argumento.

---

## 3. NON_IDENTIFIABLE

### 3.1 `m₄` y `c` son casi el mismo parámetro

| modelo | `alpha` | `m₄` | `c` | `\|c\|/se(c)` | `corr(m₄, m₄c)` |
|---|---|---|---|---|---|
| M1 (precisión) | 0.25 | 2.2586 ± 0.0716 | −0.3544 ± 0.3213 | **1.10** | **−0.972** |
| M2 (precisión) | 0.50 | 2.2113 ± 0.0352 | −1.3362 ± 1.5213 | **0.88** | −0.880 |
| M3 (precisión) | 1.00 | 2.1911 ± 0.0213 | −28.37 ± 55.76 | **0.51** | −0.616 |
| M1 (base) | 0.25 | 2.1461 ± 0.0932 | −0.1348 ± 0.3390 | 0.40 | −0.960 |
| M2 (base) | 0.50 | 2.1233 ± 0.0489 | −0.3617 ± 1.2178 | 0.30 | −0.844 |
| M3 (base) | 1.00 | 2.1123 ± 0.0323 | −1.6265 ± 25.27 | 0.06 | −0.585 |

**En las seis filas `c` es compatible con cero.** Ninguna pasa de `1.1 sigma`.
Y la correlación `−0.972` de M1 dice que constante y amplitud son, con estos
puntos, prácticamente la misma dirección del espacio de parámetros: mover `m₄`
hacia arriba y `c` hacia abajo deja el ajuste intacto. Es exactamente la
advertencia de [R002 C2](paper_iii_resolucion_002_reescopado_fase1.md), ahora
cuantificada.

### 3.2 M4: el `alpha` libre no tiene mínimo interior

**El óptimo de M4 cae sobre el borde inferior del dominio declarado en las dos
piernas** (`alpha = 0.050`). No es una estimación: es una solución de frontera.
Y hacia esa frontera `m₄` se dispara: en la pierna de precisión
`m₄ = 2.6512`, **fuera de la banda rigurosa** `[1.8555, 2.5296]`.

`UNCONSTRAINED_DIAGNOSTIC_ONLY` — reimponiendo la banda, el mejor M4 de la pierna
de precisión es `alpha = 0.067`, `m₄ = 2.5292` (pegado al techo de la banda),
`c = −0.2579`, `χ² = 3.4507` frente a `3.4218` libre. La banda cuesta `0.029`
unidades de `χ²`: **la banda no está restringiendo nada porque el ajuste no está
determinando nada.**

### 3.3 Múltiples `(c, alpha)` prácticamente indistinguibles

Éste es el diagnóstico que el prompt pide explícitamente. Barrido de `alpha`
sobre el dominio declarado, con `(m₄, c)` reajustados en cada punto:

Pierna de precisión:

| `alpha` | `m₄` | `c` | `χ²` | `Δχ²` |
|---|---|---|---|---|
| 0.05 | 2.6512 | −0.2844 | 3.4218 | 0.0000 |
| 0.10 | 2.4054 | −0.2393 | 3.5093 | 0.0875 |
| 0.25 | 2.2586 | −0.3544 | 3.7671 | 0.3453 |
| 0.50 | 2.2113 | −1.336 | 4.1521 | 0.7303 |
| 1.00 | 2.1911 | −28.37 | 4.6477 | 1.2259 |
| 2.00 | 2.1852 | −11 540 | 4.8926 | 1.4707 |

```text
region Dchi2 < 1     alpha in [0.050, 0.724]   m4 in [2.198, 2.651]   c in [-5.155, -0.239]
region Dchi2 < 2.71  alpha in [0.050, 2.000]   m4 in [2.185, 2.651]   c in [-11540, -0.239]
```

Dentro de `Δχ² < 1` — es decir, dentro de lo que este diseño **no puede
distinguir** — `|c|` varía en un factor **21.6** y `m₄` recorre casi un cuarto de
la banda rigurosa entera. Dentro de `Δχ² < 2.71` (el intervalo nominal al 90 %
para un parámetro) `alpha` ocupa **todo el dominio declarado** y `c` recorre
cuatro órdenes de magnitud.

Pierna base, peor todavía:

```text
region Dchi2 < 1     alpha in [0.050, 2.000]   m4 in [2.108, 2.328]   c in [-1.648, +4280]
```

**Todo el dominio de `alpha` cabe dentro de `Δχ² < 1`, y `c` cambia de signo
dentro de esa región.** No hay información sobre `alpha` en esta pierna: la hay
sobre `m₄`, y `alpha` es libre de valer lo que quiera.

```text
M4_IDENTIFIABLE = NO   (solucion de frontera en ambas piernas; alpha no acotada
                        ni siquiera en signo de c en la pierna base)
```

---

## 4. ROBUST_ACROSS_LEGS

### 4.1 Las dos piernas concuerdan donde se solapan

Mismo generador, semillas disjuntas, `N` comunes, `sigma` de R005 en ambas:

| `N` | precisión | base | diferencia | sigma |
|---|---|---|---|---|
| 2 000 | 2.1869 ± 0.0525 | 2.0436 ± 0.0761 | 0.1433 | 1.55 |
| 8 000 | 2.1147 ± 0.0371 | 2.0795 ± 0.0538 | 0.0352 | 0.54 |
| 16 000 | 2.1895 ± 0.0312 | 2.1339 ± 0.0453 | 0.0556 | 1.01 |

```text
chi2 conjunto = 3.712 / 3 dof = 1.24     BASE_PRECISION_CONSISTENCY = CONSISTENT
```

### 4.2 Qué sobrevive a las dos piernas

- **M0 dentro de la banda:** `2.1844` (precisión) y `2.1111` (base). Ambos.
- **M5 `beta`:** `0.2615` y `0.2555`. Ambos compatibles entre sí y con `1/4`
  dentro del suelo de resolución del diseño (`0.0179`, R005). Bootstrap sobre las
  semillas comprometidas de la pierna de precisión: `beta` mediana `0.2615`, IC95
  `[0.2440, 0.2775]` — **contiene `0.25`**, con `P(beta > 0.25) = 0.898`.
- **El signo de `c`:** negativo en M1/M2/M3 en las dos piernas con los datos
  completos. Es lo único direccional que sobrevive, y §5 muestra que no sobrevive
  a quitar un punto.
- **Bootstrap sobre semillas** (4 000 remuestreos de las 8 réplicas
  comprometidas, semilla `20260910`, pierna de precisión):

  ```text
  M0 m4   mediana 2.1846  IC68 [2.1764, 2.1922]  IC95 [2.1679, 2.1992]  P(en banda) = 1.000
  M1 c    mediana -0.3602 IC68 [-0.6482,-0.0558] IC95 [-0.8802,+0.2660] P(c<0) = 0.877
  M5 beta mediana  0.2615 IC68 [0.2530, 0.2705]  IC95 [0.2440, 0.2775]  P(beta>0.25) = 0.898
  ```

  `m₄` es la única cantidad que el remuestreo determina bien. **El IC95 de `c`
  contiene el cero.**

### 4.3 Una tensión que sí hay que declarar

Las constantes M0 de las dos piernas difieren en `+0.0733`, que son `2.36 sigma`.

Esto **no** es un contraste nulo: las piernas cubren rangos de `N` distintos
(base `500–16000`, precisión `2000–32000`), y bajo cualquier modelo con `c ≠ 0`
sus constantes *deben* diferir. Se registra porque es el único indicio en toda la
batería de que M0 podría no bastar, y porque va en la dirección correcta para
`c < 0`. Pero es un indicio débil y contaminado: en los `N` solapados las piernas
son consistentes (§4.1), y el punto que más lo empuja es `N = 500`, que tiene el
`y` **más alto** del barrido base — es decir, empuja en la dirección contraria a
una corrección monótona.

Además la pierna base tiene **3 réplicas**, luego su `sd` agrupada descansa sobre
12 dof, y R005 exige que el número de réplicas se declare suficiente para que esa
estimación sea estable. **Esa declaración no se ha hecho para 3 semillas.** Por
eso la pierna base es contraste y no canal principal.

---

## 5. SENSITIVE_TO_SINGLE_POINT

Aquí es donde se decide el informe.

### 5.1 El `χ²` de la pierna de precisión es un punto

Contribución de cada punto al `χ²` de M0:

| `N` | `(r/sigma)²` | % del `χ² = 4.905` |
|---|---|---|
| 2 000 | 0.002 | 0.0 % |
| **8 000** | **3.519** | **71.7 %** |
| 16 000 | 0.027 | 0.5 % |
| 32 000 | 1.357 | 27.7 % |

Dos puntos aportan el 99.4 % del `χ²`; uno solo aporta casi tres cuartas partes.
Y ese uno es precisamente `N = 8000`, el de los seis empates.

### 5.2 Quitando `N = 8000`

```text
completo    : M0  m4 = 2.1844   chi2 = 4.905 / 3 dof = 1.64   p = 0.179   M1 c = -0.3544
sin N=8000  : M0  m4 = 2.2022   chi2 = 0.487 / 2 dof = 0.24   p = 0.784   M1 c = -0.1648
```

**El `χ²` de la constante cae de `4.905` a `0.487`.** Toda la tensión que
cualquier familia de corrección podría estar comprando reside en ese punto. Y la
amplitud `c` de M1 se reduce a menos de la mitad.

Además, sin `N = 8000` la pierna de precisión tiene tres puntos: **M4 pasa a
tener tres parámetros para tres datos, dof 0, interpolación exacta.** No es un
ajuste.

### 5.3 El modelo de error prohibido fabrica la preferencia

`UNCONSTRAINED_DIAGNOSTIC_ONLY` — usando `sem` punto a punto en vez de agrupada,
que es exactamente lo que R005 prohíbe:

| modelo de error | `χ²/dof` de M0 | `c` de M1 | `Δχ²(M0→M1)` |
|---|---|---|---|
| **agrupado (R005)** | **1.64** | **−0.354** | **1.138** |
| punto a punto (prohibido) | 3.26 | −0.567 | 2.918 |

La "evidencia" a favor de una corrección **se multiplica por 2.6 en cuanto se
adopta el modelo de error que R005 declara inadmisible**, y por la razón
identificada allí: la `sd` de ocho extracciones muy empatadas en `N = 8000`
subestima la dispersión real y ese punto pasa a dominar el `χ²`. Un contraste
cuyo resultado dependa de la `sem` de un único punto no es admisible como
evidencia — y éste dependía.

### 5.4 Leave-one-out

Pierna de precisión — reajuste quitando cada `N`:

| quitado | M0 `m₄` | M1 `m₄` | M1 `c` | M2 `c` | M3 `c` | M5 `beta` |
|---|---|---|---|---|---|---|
| 2 000 | 2.1841 | 2.4536 | −1.2726 | −7.5935 | −475.03 | 0.2810 |
| 8 000 | 2.2022 | 2.2351 | −0.1648 | −0.6741 | −20.497 | 0.2550 |
| 16 000 | 2.1823 | 2.2572 | −0.3518 | −1.3222 | −27.315 | 0.2615 |
| 32 000 | 2.1634 | 2.1716 | −0.0357 | +0.0641 | **+13.465** | 0.2525 |

- **`m₄` de M0 es estable**: `2.163 … 2.202`, un rango de `0.039` frente a
  `se = 0.017`. Poco más de dos sigmas de excursión total, y siempre en banda.
- **`c` de M1 no es estable**: `−1.273 … −0.036`, un **factor 36**.
- **`c` de M2 y M3 cambian de signo** al quitar `N = 32000`.
- **`beta` de M5 es estable**: `0.2525 … 0.2810`, y contiene `0.25` en todas las
  variantes salvo la que quita `N = 2000`.
- **M4 no admite leave-one-out en esta pierna**: 3 parámetros, 3 puntos, dof 0.

Pierna base — reajuste quitando cada `N`:

| quitado | M0 `m₄` | M1 `c` | M3 `c` | **M4 `alpha`** | M5 `beta` |
|---|---|---|---|---|---|
| 500 | 2.1065 | −0.4767 | −56.889 | 1.469 | 0.2645 |
| 1 000 | 2.1199 | **+0.0667** | +11.292 | **2.000** | 0.2490 |
| 2 000 | 2.1202 | −0.0425 | +0.994 | **2.000** | 0.2520 |
| 4 000 | 2.0974 | −0.1605 | +1.198 | **0.050** | 0.2575 |
| 8 000 | 2.1209 | −0.1989 | −6.431 | **0.050** | 0.2575 |
| 16 000 | 2.0996 | +0.0031 | +6.077 | **2.000** | 0.2505 |

**El `alpha` de M4 salta entre los dos extremos del dominio declarado —
`0.050` y `2.000` — según qué único punto se retire.** Es la demostración más
directa posible de no identificabilidad: el parámetro no está determinado por los
datos, está determinado por cuál de seis puntos se mire. `c` de M1 también cambia
de signo. `m₄` y `beta`, otra vez, aguantan.

```text
LEAVE_ONE_OUT_STABILITY:
  m4 (M0)      STABLE
  beta (M5)    STABLE
  c  (M1-M3)   UNSTABLE  (factor 36 en precision; cambio de signo en ambas piernas)
  alpha (M4)   UNSTABLE  (salta entre las dos fronteras del dominio declarado)
```

---

## 6. NOT_SUPPORTED

Nada de lo siguiente está sostenido por estos datos. Se listan porque son las
lecturas que el informe podría inducir si se leyera sólo la columna de `χ²`.

1. **Que alguna familia de corrección sea preferida.** `p ≥ 0.207` en las cinco
   comparaciones. La mejor mejora de la batería ocurre por azar una vez de cada
   cinco.
2. **Cualquier valor ajustado de `alpha` como estimación.** El óptimo es de
   frontera en las dos piernas, salta entre `0.050` y `2.000` bajo
   leave-one-out, y en la pierna base todo el dominio cabe en `Δχ² < 1`.
   **`alpha = 0.05` no es un resultado; es el borde de una caja que declaramos
   nosotros.**
3. **Cualquier valor de `c`.** Compatible con cero en las seis filas de §3.1; IC95
   del bootstrap cruza el cero; cambia de signo bajo leave-one-out.
4. **Que `m₄ = 2.6512`.** Es el `m₄` de la solución de frontera de M4 y viola la
   banda rigurosa. Marcado `UNCONSTRAINED_DIAGNOSTIC_ONLY` y no reportable.
5. **Una aproximación monótona a una constante.** `y` no es monótona en ninguna
   de las dos piernas (O1).
6. **Que `beta = 0.2615` sea distinto de `1/4`.** IC95 del bootstrap
   `[0.2440, 0.2775]`; la desviación `0.0115` está por debajo del suelo de
   resolución declarado del diseño (`0.0179`, R005).
7. **Cualquier lectura del canal de minimales.** No se ha usado. Sigue suspendido.
8. **Cualquier afirmación sobre si el régimen asintótico se ha alcanzado o no.**
   Este informe no la hace, ni en un sentido ni en el otro. Mide qué puede
   distinguir el diseño, no qué hace la teoría.

---

## 7. Veredicto

```text
VERDICT = C) CONSTANT_MODEL_SUFFICIENT_AT_CURRENT_RESOLUTION
```

En las dos piernas, con el modelo de error firmado en R005 y bajo la convención
firmada en R001, el modelo constante `y = m₄` ajusta los datos comprometidos
(`p = 0.179` en precisión, `p = 0.532` en base) con un `m₄` dentro de la banda
rigurosa, y **ninguna de las cinco familias de corrección compra una mejora que
supere el ruido que el propio diseño genera cuando no hay nada que encontrar.**

Dentro de ese veredicto, y subordinado a él, **también se cumple (B)**: M1, M2,
M3, M4 y M5 son mutuamente indistinguibles entre sí, con `Δχ²` separados por
menos de lo que separa a dos realizaciones del ruido. Es un hecho relevante para
la Fase 2 — si alguna vez hubiera una corrección, este diseño no podría decir
cuál es — pero no es el veredicto, porque el veredicto sólo requiere que la
constante baste, y basta.

**No es (A)**: ninguna familia sobrevive robustamente; la única que lo parecía
(M5, `Δχ² = 1.590`) es la que más claramente reproduce lo que hace el ruido.

**No es (D)**: los datos no son demasiado débiles para *todo*. Determinan `m₄`
con `± 0.017` y lo sitúan en banda, determinan `beta` con IC95 `[0.244, 0.278]`,
y son consistentes entre piernas. Lo que no pueden hacer es discriminar entre
correcciones — que es precisamente el contenido de (B), ya recogido arriba.

**Esto no dice que no exista corrección de tamaño finito.** Dice que si existe,
su amplitud está por debajo del suelo de este diseño, y que este diseño no puede
decir de qué familia es. Es una afirmación sobre la resolución, no sobre la
naturaleza — exactamente en la forma que exige
[R002 C1](paper_iii_resolucion_002_reescopado_fase1.md).

### 7.1 Lo que este resultado implica para el diseño

Coincide con lo ya establecido en [R002 §3.3](paper_iii_resolucion_002_reescopado_fase1.md)
y lo refuerza desde otro ángulo: el `χ²` de la pierna de precisión está dominado
por un punto cuya `sd` está subestimada por empates entre ocho réplicas enteras.
La limitación que muerde es el **número de réplicas**, no el rango de `N` ni la
elección de familia. Añadir un `N` mayor a este barrido añadiría un punto más con
la misma barra de error a un ajuste que ya no distingue nada.

## 8. Qué NO autoriza este informe

- No firma R007 ni ninguna otra resolución.
- No fija `alpha`, ni la parametrización, ni el número de réplicas.
- No autoriza ninguna corrida, semilla, `N` ni `rho`.
- No reabre el canal de minimales.
- No extrapola a Schwarzschild ni interpreta geométricamente `R`.
- No declara alcanzado ni no alcanzado ningún régimen asintótico.
- No toca el orden obligatorio de [R001 §5](paper_iii_resolucion_001_convencion_L.md):
  reproducir → convertir → reejecutar.

```text
GATE_1 = NOT_EVALUATED   (este informe es exploracion; GATE_1 lo decide la Fase 1 firmada)
```

---

## Apéndice A — script

Lectura de artefactos comprometidos y aritmética de ajuste. No importa ningún
generador, no crea ningún fichero, no escribe nada.

```text
sha256 = 6fb171f1de9cbc2a0aaf60a1e55e46031bb3f8526b64a9bb8fab98f8a7ea1997
```

```python
"""EXPLORATION -- Paper III, Phase 1: model battery on the UNRESTRICTED interval leg.

Reads ONLY committed artifacts. Runs no generator, adds no seed/N/rho/observable.
Error model: R005 (pooled sd across the sweep, sem = sd_pool/sqrt(n_rep)).
Convention: R001 (L = |chain|, endpoints included) -> stored Ls + 2.
"""
import json, itertools
import numpy as np

BAND = (1.8555, 2.5296)
ALPHA_DOMAIN = (0.05, 2.00)          # declared M4 domain
PREC = "dev/explore_3p1_bg_reference_precision_results.json"
BASE = "dev/explore_3p1_bg_reference_results.json"


def leg(path):
    o = json.load(open(path))
    rows = o["rows"]
    N = np.array([r["N"] for r in rows], float)
    Ls = [np.asarray(r["Ls"], float) + 2.0 for r in rows]      # R001
    L = np.array([a.mean() for a in Ls])
    sd = np.array([a.std(ddof=1) for a in Ls])
    n_rep = Ls[0].size
    sd_pool = float(np.sqrt(np.mean(sd**2)))
    sem = sd_pool / np.sqrt(n_rep)                              # same in L units at every point
    y = L / N**0.25
    sy = sem / N**0.25
    return dict(N=N, Ls=Ls, L=L, sd=sd, n_rep=n_rep, sd_pool=sd_pool,
                sem=sem, y=y, sy=sy, sd_dof=n_rep and (n_rep - 1) * len(N))


# ---- fitters (all weighted least squares with the R005 sigmas) --------------
def wls_linear(X, y, s):
    w = 1.0 / s**2
    A = X.T @ (X * w[:, None]); b = X.T @ (w * y)
    beta = np.linalg.solve(A, b)
    r = y - X @ beta
    return beta, float((w * r**2).sum()), r, np.linalg.inv(A)


def fit_M0(N, y, s):
    beta, chi2, r, C = wls_linear(np.ones((len(N), 1)), y, s)
    return dict(name="M0", k=1, p={"m4": beta[0]}, se={"m4": np.sqrt(C[0, 0])},
                chi2=chi2, res=r, cov=C)


def fit_Malpha(N, y, s, alpha, tag):
    X = np.column_stack([np.ones_like(N), N**(-alpha)])
    beta, chi2, r, C = wls_linear(X, y, s)
    m4, c = beta[0], beta[1] / beta[0]
    # delta-method se for c = b1/b0
    g = np.array([-beta[1] / beta[0]**2, 1.0 / beta[0]])
    se_c = float(np.sqrt(g @ C @ g))
    rho = C[0, 1] / np.sqrt(C[0, 0] * C[1, 1])
    return dict(name=tag, k=2, alpha=alpha, p={"m4": m4, "c": c},
                se={"m4": np.sqrt(C[0, 0]), "c": se_c}, chi2=chi2, res=r,
                cov=C, corr_m4_b1=float(rho))


def profile_M4(N, y, s, lo=ALPHA_DOMAIN[0], hi=ALPHA_DOMAIN[1], n=3901):
    al = np.linspace(lo, hi, n)
    out = []
    for a in al:
        X = np.column_stack([np.ones_like(N), N**(-a)])
        try:
            beta, chi2, r, C = wls_linear(X, y, s)
        except np.linalg.LinAlgError:
            continue
        out.append((a, beta[0], beta[1] / beta[0], chi2))
    return np.array(out)


def fit_M5(N, L, sL, lo=0.05, hi=0.60, n=1101):
    """L = A N^beta, WLS on L with constant sigma_L. A is linear given beta."""
    w = np.full(len(N), 1.0 / sL**2)
    bs = np.linspace(lo, hi, n); best = None
    for b in bs:
        f = N**b
        A = (w * f * L).sum() / (w * f * f).sum()
        r = L - A * f
        chi2 = float((w * r**2).sum())
        if best is None or chi2 < best[2]:
            best = (A, b, chi2, r)
    A, b, chi2, r = best
    return dict(name="M5", k=2, p={"A": A, "beta": b}, chi2=chi2, res=r)


def aicc(chi2, k, n):
    aic = chi2 + 2 * k
    den = n - k - 1
    return aic, (aic + 2 * k * (k + 1) / den if den > 0 else None), den


def band_ok(m4):
    return BAND[0] <= m4 <= BAND[1]


def show_leg(tag, d, models_alpha=(0.25, 0.5, 1.0)):
    N, y, s, L = d["N"], d["y"], d["sy"], d["L"]
    n = len(N)
    print("=" * 96)
    print(f"LEG {tag}: n_points={n}  n_replicas={d['n_rep']}  "
          f"sd_pool={d['sd_pool']:.4f} (dof {d['sd_dof']})  sem_L={d['sem']:.4f}")
    print(f"  {'N':>7}{'mean L (R001)':>15}{'sd':>8}{'y=L/N^(1/4)':>14}{'sigma_y':>10}")
    for i in range(n):
        print(f"  {int(N[i]):7d}{L[i]:15.4f}{d['sd'][i]:8.4f}{y[i]:14.5f}{s[i]:10.5f}")

    fits = [fit_M0(N, y, s)]
    for a, tg in zip(models_alpha, ("M1", "M2", "M3")):
        fits.append(fit_Malpha(N, y, s, a, tg))
    prof = profile_M4(N, y, s)
    i = int(np.argmin(prof[:, 3]))
    a4, m44, c4, chi4 = prof[i]
    fits.append(dict(name="M4", k=3, alpha=a4, p={"m4": m44, "c": c4}, chi2=chi4,
                     res=y - m44 * (1 + c4 * N**(-a4)), prof=prof))
    m5 = fit_M5(N, L, np.full(n, d["sem"]))
    print(f"\n  {'model':<6}{'k':>3}{'chi2':>9}{'dof':>5}{'chi2/dof':>10}{'Dchi2 vs M0':>13}"
          f"{'AIC':>8}{'AICc':>9}{'m4/A':>10}{'c/beta':>12}{'band':>7}")
    chi0 = fits[0]["chi2"]
    for f in fits:
        dof = n - f["k"]
        aic, ac, den = aicc(f["chi2"], f["k"], n)
        p = f["p"]
        m = p.get("m4"); c = p.get("c", float("nan"))
        acs = f"{ac:9.2f}" if ac is not None else "   UNDEF"
        cdof = f"{f['chi2']/dof:10.2f}" if dof > 0 else "     n/a  "
        print(f"  {f['name']:<6}{f['k']:>3}{f['chi2']:9.3f}{dof:5d}{cdof}"
              f"{chi0-f['chi2']:13.3f}{aic:8.2f}{acs}{m:10.4f}"
              f"{c:12.4f}{'IN' if band_ok(m) else 'OUT':>7}")
    dof5 = n - 2
    aic5, ac5, _ = aicc(m5["chi2"], 2, n)
    acs5 = f"{ac5:9.2f}" if ac5 is not None else "   UNDEF"
    print(f"  {'M5':<6}{2:>3}{m5['chi2']:9.3f}{dof5:5d}{m5['chi2']/dof5:10.2f}"
          f"{chi0-m5['chi2']:13.3f}{aic5:8.2f}{acs5}{m5['p']['A']:10.4f}"
          f"{m5['p']['beta']:12.4f}{'n/a':>7}")
    print("  (M5 is fitted on L with constant sigma_L; M0 is EXACTLY M5 with beta fixed\n   at 1/4, so every chi2 in this table is on ONE common scale -- see the nesting check.)")

    print("\n  residuals in sigma units:")
    for f in fits:
        print(f"    {f['name']:<4} " + "  ".join(f"{v:+7.2f}" for v in f["res"] / s))
    print(f"    {'M5':<4} " + "  ".join(f"{v:+7.2f}" for v in m5["res"] / d["sem"]))

    print("\n  parameter uncertainty / degeneracy (M1-M3):")
    for f in fits[1:4]:
        print(f"    {f['name']}  alpha={f['alpha']:.2f}  m4={f['p']['m4']:.4f}+/-{f['se']['m4']:.4f}"
              f"  c={f['p']['c']:+.4f}+/-{f['se']['c']:.4f}"
              f"  |c|/se={abs(f['p']['c'])/f['se']['c']:.2f}"
              f"  corr(m4,b1)={f['corr_m4_b1']:+.4f}")
    return fits, m5, prof


def m4_degeneracy(prof, chimin, tag):
    print(f"\n  M4 degeneracy scan over declared alpha domain "
          f"[{ALPHA_DOMAIN[0]}, {ALPHA_DOMAIN[1]}] ({tag}):")
    for thr, lbl in ((1.0, "Dchi2<1"), (2.71, "Dchi2<2.71")):
        sel = prof[prof[:, 3] <= chimin + thr]
        if len(sel):
            print(f"    {lbl:12s} alpha in [{sel[:,0].min():.3f}, {sel[:,0].max():.3f}]  "
                  f"m4 in [{sel[:,1].min():.4f}, {sel[:,1].max():.4f}]  "
                  f"c in [{sel[:,2].min():+.4g}, {sel[:,2].max():+.4g}]")
    print(f"    {'alpha':>8}{'m4':>10}{'c':>14}{'chi2':>10}{'Dchi2':>9}")
    for a in (0.05, 0.10, 0.25, 0.40, 0.50, 0.75, 1.00, 1.50, 2.00):
        j = int(np.argmin(np.abs(prof[:, 0] - a)))
        print(f"    {prof[j,0]:8.2f}{prof[j,1]:10.4f}{prof[j,2]:+14.4g}"
              f"{prof[j,3]:10.4f}{prof[j,3]-chimin:9.4f}")


def loo(tag, d, alpha_list=(0.25, 0.5, 1.0)):
    N, y, s, L = d["N"], d["y"], d["sy"], d["L"]
    n = len(N)
    print(f"\n  LEAVE-ONE-OUT ({tag}):  refit with each N dropped")
    print(f"    {'dropped':>9}{'M0 m4':>10}{'M1 m4':>10}{'M1 c':>10}"
          f"{'M2 c':>10}{'M3 c':>12}{'M4 alpha':>10}{'M4 m4':>10}{'M5 beta':>10}")
    for i in range(n):
        k = [j for j in range(n) if j != i]
        Nk, yk, sk, Lk = N[k], y[k], s[k], L[k]
        f0 = fit_M0(Nk, yk, sk)
        fa = [fit_Malpha(Nk, yk, sk, a, "x") for a in alpha_list]
        if len(k) > 3:
            pr = profile_M4(Nk, yk, sk); jj = int(np.argmin(pr[:, 3]))
            a4, m44 = pr[jj, 0], pr[jj, 1]
            a4s, m4s = f"{a4:10.3f}", f"{m44:10.4f}"
        else:
            a4s, m4s = "  EXACT/0", "  EXACT/0"     # 3 params, 3 points -> dof 0
        f5 = fit_M5(Nk, Lk, np.full(len(k), d["sem"]))
        print(f"    {int(N[i]):9d}{f0['p']['m4']:10.4f}{fa[0]['p']['m4']:10.4f}"
              f"{fa[0]['p']['c']:+10.4f}{fa[1]['p']['c']:+10.4f}{fa[2]['p']['c']:+12.3f}"
              f"{a4s}{m4s}{f5['p']['beta']:10.4f}")


def null_calibration(d, n_mc=200000, seed=20260910):
    """How big is Dchi2(M0->M1) PURELY from the design's own noise?
    No generator, no new observable: a Gaussian null on the R005 sigmas, plus a
    nonparametric bootstrap over the COMMITTED per-seed Ls."""
    N, s = d["N"], d["sy"]
    rng = np.random.default_rng(seed)
    n = len(N)
    X1 = np.column_stack([np.ones_like(N), N**(-0.25)])
    out = []
    Y = 2.2 + rng.normal(0, 1, (n_mc, n)) * s           # constant truth
    w = 1.0 / s**2
    A = X1.T @ (X1 * w[:, None]); Ai = np.linalg.inv(A)
    for Yb in np.array_split(Y, 20):
        m = (w * Yb).sum(1) / w.sum()
        c0 = (w * (Yb - m[:, None])**2).sum(1)
        B = (Yb * w) @ X1 @ Ai.T
        r = Yb - B @ X1.T
        c1 = (w * r**2).sum(1)
        out.append(c0 - c1)
    dchi = np.concatenate(out)
    print(f"\n  DESIGN-NOISE CALIBRATION of Dchi2(M0 -> 2-parameter), Gaussian null, "
          f"{n_mc} draws, seed {seed}:")
    for q in (50, 68, 90, 95, 99):
        print(f"    P{q:<3d} = {np.percentile(dchi, q):.3f}")
    return dchi


def seed_bootstrap(d, n_b=4000, seed=20260910):
    """Nonparametric bootstrap over the committed seeds (no new data)."""
    rng = np.random.default_rng(seed)
    N, Ls = d["N"], d["Ls"]
    nr = d["n_rep"]
    m4s, cs, als, bes = [], [], [], []
    for _ in range(n_b):
        idx = rng.integers(0, nr, nr)                # same seed resample at every N
        L = np.array([a[idx].mean() for a in Ls])
        sd = np.array([a[idx].std(ddof=1) for a in Ls])
        sp = float(np.sqrt(np.mean(sd**2)))
        if sp == 0:
            continue
        sem = sp / np.sqrt(nr)
        y = L / N**0.25; s = sem / N**0.25
        m4s.append(fit_M0(N, y, s)["p"]["m4"])
        f1 = fit_Malpha(N, y, s, 0.25, "x")
        cs.append(f1["p"]["c"])
        bes.append(fit_M5(N, L, np.full(len(N), sem))["p"]["beta"])
    m4s, cs, bes = map(np.asarray, (m4s, cs, bes))
    print(f"\n  SEED BOOTSTRAP over the committed replicas ({len(m4s)} resamples, seed {seed}):")
    print(f"    M0 m4  : median {np.median(m4s):.4f}  CI68 [{np.percentile(m4s,16):.4f},"
          f" {np.percentile(m4s,84):.4f}]  CI95 [{np.percentile(m4s,2.5):.4f},"
          f" {np.percentile(m4s,97.5):.4f}]  P(in band)={np.mean([band_ok(v) for v in m4s]):.3f}")
    print(f"    M1 c   : median {np.median(cs):+.4f}  CI68 [{np.percentile(cs,16):+.4f},"
          f" {np.percentile(cs,84):+.4f}]  CI95 [{np.percentile(cs,2.5):+.4f},"
          f" {np.percentile(cs,97.5):+.4f}]  P(c<0)={np.mean(cs<0):.3f}")
    print(f"    M5 beta: median {np.median(bes):.4f}  CI68 [{np.percentile(bes,16):.4f},"
          f" {np.percentile(bes,84):.4f}]  CI95 [{np.percentile(bes,2.5):.4f},"
          f" {np.percentile(bes,97.5):.4f}]  P(beta>0.25)={np.mean(bes>0.25):.3f}")


# ---------------------------------------------------------------------------
def m0_goodness(P, B):
    from scipy.stats import chi2 as _chi2
    print("\n" + "=" * 96)
    print("M0 GOODNESS OF FIT and CROSS-LEG CONSTANT")
    for tag, d in (("precision", P), ("base", B)):
        f0 = fit_M0(d["N"], d["y"], d["sy"])
        dof = len(d["N"]) - 1
        print(f"  {tag:>10}: m4 = {f0['p']['m4']:.4f} +/- {f0['se']['m4']:.4f}   "
              f"chi2 = {f0['chi2']:.4f} / {dof} dof = {f0['chi2']/dof:.2f}   "
              f"p = {_chi2.sf(f0['chi2'], dof):.3f}")
    a = fit_M0(P["N"], P["y"], P["sy"]); b = fit_M0(B["N"], B["y"], B["sy"])
    dd = a["p"]["m4"] - b["p"]["m4"]
    sg = float(np.sqrt(a["se"]["m4"] ** 2 + b["se"]["m4"] ** 2))
    print(f"  cross-leg M0 constants differ by {dd:+.4f} = {dd/sg:.2f} sigma "
          f"(different N ranges, so this is NOT a null test under M1-M5)")
    k = [i for i in range(len(P["N"])) if P["N"][i] != 8000]
    fk = fit_M0(P["N"][k], P["y"][k], P["sy"][k])
    print(f"  precision without N=8000: m4 = {fk['p']['m4']:.4f}   "
          f"chi2 = {fk['chi2']:.4f} / 2 dof = {fk['chi2']/2:.2f}   "
          f"p = {_chi2.sf(fk['chi2'], 2):.3f}")


# ---------------------------------------------------------------------------
def nesting_and_null(P, B):
    """M0 is EXACTLY M5 with beta fixed at 1/4, so their chi2 ARE comparable."""
    print("\n" + "=" * 96)
    print("M0 / M5 NESTING and DESIGN-NOISE p-VALUES")
    for tag, d in (("precision", P), ("base", B)):
        N, y, s, L, sem = d["N"], d["y"], d["sy"], d["L"], d["sem"]
        c0 = fit_M0(N, y, s)["chi2"]
        f = N ** 0.25
        A = (f * L).sum() / (f * f).sum()
        cq = float((((L - A * f) / sem) ** 2).sum())
        m5 = fit_M5(N, L, np.full(len(N), sem))
        sols = float(np.polyfit(np.log(N), np.log(L), 1)[0])
        print(f"  {tag:>10}: chi2(M0)={c0:.4f}  chi2(M5|beta=1/4)={cq:.4f}  "
              f"identical={abs(c0-cq) < 1e-9}")
        print(f"  {tag:>10}: M5 free beta={m5['p']['beta']:.4f} A={m5['p']['A']:.4f} "
              f"chi2={m5['chi2']:.4f}  Dchi2 vs M0={c0-m5['chi2']:.4f} (1 extra param)")
        print(f"  {tag:>10}: unweighted log-log OLS slope on mean L (R001) = {sols:.4f}"
              f"   [reproduces R001 sec. 3.1]")

    N, y, s, sem = P["N"], P["y"], P["sy"], P["sem"]
    w = 1.0 / s ** 2
    rng = np.random.default_rng(20260910)
    n_mc = 400000
    Yb = 2.2 + rng.normal(0, 1, (n_mc, len(N))) * s
    m = (w * Yb).sum(1) / w.sum()
    c0v = (w * (Yb - m[:, None]) ** 2).sum(1)
    X1 = np.column_stack([np.ones_like(N), N ** (-0.25)])
    Ai = np.linalg.inv(X1.T @ (X1 * w[:, None]))
    d1 = c0v - (w * (Yb - ((Yb * w) @ X1 @ Ai.T) @ X1.T) ** 2).sum(1)
    print("\n  1-extra-parameter design-noise null (precision leg, 400000 draws, seed 20260910):")
    for q in (50, 68, 90, 95, 99):
        print(f"     P{q:<3d} = {np.percentile(d1, q):.3f}")
    for obs, lbl in ((1.138, "M1"), (0.753, "M2"), (0.257, "M3")):
        print(f"     Dchi2(M0->{lbl}) = {obs:.3f}  percentile {100*np.mean(d1<=obs):5.1f}"
              f"   p(>=obs) = {np.mean(d1>=obs):.3f}")

    sub = Yb[:40000]
    c4 = np.full(len(sub), np.inf)
    for a in np.linspace(ALPHA_DOMAIN[0], ALPHA_DOMAIN[1], 60):
        X = np.column_stack([np.ones_like(N), N ** (-a)])
        Aa = np.linalg.inv(X.T @ (X * w[:, None]))
        c4 = np.minimum(c4, (w * (sub - ((sub * w) @ X @ Aa.T) @ X.T) ** 2).sum(1))
    d4 = c0v[:40000] - c4
    print("\n  2-extra-parameter null (M0 -> M4, alpha profiled over the declared domain):")
    for q in (50, 68, 90, 95, 99):
        print(f"     P{q:<3d} = {np.percentile(d4, q):.3f}")
    print(f"     Dchi2(M0->M4) = 1.483  percentile {100*np.mean(d4<=1.483):5.1f}"
          f"   p(>=obs) = {np.mean(d4>=1.483):.3f}")

    n5 = 60000
    Lb = 2.2 * N ** 0.25 + rng.normal(0, sem, (n5, len(N)))
    wl = np.full(len(N), 1.0 / sem ** 2)
    f = N ** 0.25
    A0 = (Lb * f * wl).sum(1) / (wl * f * f).sum()
    c0l = (wl * (Lb - A0[:, None] * f) ** 2).sum(1)
    cb = np.full(n5, np.inf)
    for b in np.linspace(0.05, 0.60, 200):
        fb = N ** b
        Ab = (Lb * fb * wl).sum(1) / (wl * fb * fb).sum()
        cb = np.minimum(cb, (wl * (Lb - Ab[:, None] * fb) ** 2).sum(1))
    d5 = c0l - cb
    o5 = fit_M0(N, y, s)["chi2"] - fit_M5(N, P["L"], np.full(len(N), sem))["chi2"]
    print(f"\n  M5 null (beta profiled): P50={np.percentile(d5,50):.3f} "
          f"P68={np.percentile(d5,68):.3f} P90={np.percentile(d5,90):.3f}")
    print(f"     Dchi2(M0->M5) = {o5:.3f}  percentile {100*np.mean(d5<=o5):5.1f}"
          f"   p(>=obs) = {np.mean(d5>=o5):.3f}")

    f0 = fit_M0(N, y, s)
    r = f0["res"] / s
    print("\n  per-point contribution to the M0 chi2 (precision leg):")
    for i in range(len(N)):
        print(f"     N={int(N[i]):6d}  (r/sigma)^2 = {r[i]**2:6.3f}"
              f"   {100*r[i]**2/f0['chi2']:5.1f}% of chi2 = {f0['chi2']:.3f}")


P, B = leg(PREC), leg(BASE)
fp, m5p, profp = show_leg("PRECISION (8 seeds, primary)", P)
m4_degeneracy(profp, profp[:, 3].min(), "precision")
loo("precision", P)
dchi = null_calibration(P)
seed_bootstrap(P)

fb, m5b, profb = show_leg("BASE (3 seeds)", B)
m4_degeneracy(profb, profb[:, 3].min(), "base")
loo("base", B)

# --- N=8000 sensitivity, precision leg (the heavily tied point) -------------
print("\n" + "=" * 96)
print("N=8000 SENSITIVITY (precision leg): the point with 6 of 8 replicas identical")
N, y, s = P["N"], P["y"], P["sy"]
k = [i for i in range(len(N)) if N[i] != 8000]
print(f"  full      : M0 m4={fit_M0(N,y,s)['p']['m4']:.4f}  chi2={fit_M0(N,y,s)['chi2']:.3f}"
      f"  M1 c={fit_Malpha(N,y,s,0.25,'x')['p']['c']:+.4f}"
      f"  M4 alpha={profp[int(np.argmin(profp[:,3])),0]:.3f}")
f0k = fit_M0(N[k], y[k], s[k]); f1k = fit_Malpha(N[k], y[k], s[k], 0.25, "x")
print(f"  drop 8000 : M0 m4={f0k['p']['m4']:.4f}  chi2={f0k['chi2']:.3f}"
      f"  M1 c={f1k['p']['c']:+.4f}  M4: 3 params on 3 points -> EXACT, dof 0")
print("  per-point sem instead of pooled (DIAGNOSTIC ONLY, violates R005):")
sd_i = P["sd"] / np.sqrt(P["n_rep"]) / N**0.25
f0i = fit_M0(N, y, sd_i); f1i = fit_Malpha(N, y, sd_i, 0.25, "x")
print(f"    M0 chi2/dof={f0i['chi2']/3:.2f} m4={f0i['p']['m4']:.4f}   "
      f"M1 chi2/dof={f1i['chi2']/2:.2f} c={f1i['p']['c']:+.4f}  Dchi2={f0i['chi2']-f1i['chi2']:.3f}")

# --- base/precision consistency at overlapped N ----------------------------
print("\n" + "=" * 96)
print("BASE vs PRECISION at overlapped N (R005 pooled sigmas on both legs)")
chi = 0.0; nov = 0
print(f"  {'N':>7}{'precision':>22}{'base':>22}{'diff':>10}{'sigma':>8}")
for i, Ni in enumerate(P["N"]):
    j = np.where(B["N"] == Ni)[0]
    if not len(j):
        continue
    j = int(j[0]); nov += 1
    dd = P["y"][i] - B["y"][j]
    sg = np.sqrt(P["sy"][i]**2 + B["sy"][j]**2)
    chi += (dd / sg)**2
    print(f"  {int(Ni):7d}{P['y'][i]:14.4f} +/-{P['sy'][i]:6.4f}"
          f"{B['y'][j]:14.4f} +/-{B['sy'][j]:6.4f}{dd:10.4f}{dd/sg:8.2f}")
print(f"  joint chi2 = {chi:.3f} / {nov} dof = {chi/nov:.2f}")

# --- unconstrained vs band -------------------------------------------------
print("\n" + "=" * 96)
print("BAND CHECK  1.8555 <= m4 <= 2.5296   (UNCONSTRAINED_DIAGNOSTIC_ONLY where marked)")
for tag, fits, prof in (("precision", fp, profp), ("base", fb, profb)):
    for f in fits:
        m = f["p"]["m4"]
        print(f"  {tag:<10}{f['name']:<4} m4={m:9.4f}   {'IN BAND' if band_ok(m) else 'OUT OF BAND'}")
    sel = prof[(prof[:, 1] >= BAND[0]) & (prof[:, 1] <= BAND[1])]
    if len(sel):
        jj = int(np.argmin(sel[:, 3]))
        print(f"  {tag:<10}M4 restricted to band: alpha={sel[jj,0]:.3f} m4={sel[jj,1]:.4f} "
              f"c={sel[jj,2]:+.4g} chi2={sel[jj,3]:.4f}  (vs free {prof[:,3].min():.4f})")
    else:
        print(f"  {tag:<10}M4: NO alpha in the declared domain puts m4 inside the band")

nesting_and_null(P, B)
m0_goodness(P, B)
```

## Apéndice B — salida íntegra

```text
================================================================================================
LEG PRECISION (8 seeds, primary): n_points=4  n_replicas=8  sd_pool=0.9933 (dof 28)  sem_L=0.3512
        N  mean L (R001)      sd   y=L/N^(1/4)   sigma_y
     2000        14.6250  1.0607       2.18695   0.05251
     8000        20.0000  0.5345       2.11474   0.03713
    16000        24.6250  1.1877       2.18951   0.03122
    32000        29.6250  1.0607       2.21499   0.02626

  model   k     chi2  dof  chi2/dof  Dchi2 vs M0     AIC     AICc      m4/A      c/beta   band
  M0      1    4.905    3      1.64        0.000    6.91     8.91    2.1844         nan     IN
  M1      2    3.767    2      1.88        1.138    7.77    19.77    2.2586     -0.3544     IN
  M2      2    4.152    2      2.08        0.753    8.15    20.15    2.2113     -1.3362     IN
  M3      2    4.648    2      2.32        0.257    8.65    20.65    2.1911    -28.3721     IN
  M4      3    3.422    1      3.42        1.483    9.42   UNDEF    2.6512     -0.2844    OUT
  M5      2    3.315    2      1.66        1.590    7.31    19.31    1.9558      0.2615    n/a
  (M5 is fitted on L with constant sigma_L; M0 is EXACTLY M5 with beta fixed
   at 1/4, so every chi2 in this table is on ONE common scale -- see the nesting check.)

  residuals in sigma units:
    M0     +0.05    -1.88    +0.16    +1.16
    M1     +0.91    -1.60    +0.07    +0.62
    M2     +0.79    -1.71    +0.05    +0.77
    M3     +0.51    -1.85    +0.07    +0.99
    M4     +0.98    -1.49    +0.10    +0.48
    M5     +1.00    -1.45    +0.11    +0.44

  parameter uncertainty / degeneracy (M1-M3):
    M1  alpha=0.25  m4=2.2586+/-0.0716  c=-0.3544+/-0.3213  |c|/se=1.10  corr(m4,b1)=-0.9722
    M2  alpha=0.50  m4=2.2113+/-0.0352  c=-1.3362+/-1.5213  |c|/se=0.88  corr(m4,b1)=-0.8797
    M3  alpha=1.00  m4=2.1911+/-0.0213  c=-28.3721+/-55.7575  |c|/se=0.51  corr(m4,b1)=-0.6164

  M4 degeneracy scan over declared alpha domain [0.05, 2.0] (precision):
    Dchi2<1      alpha in [0.050, 0.724]  m4 in [2.1980, 2.6512]  c in [-5.155, -0.2388]
    Dchi2<2.71   alpha in [0.050, 2.000]  m4 in [2.1852, 2.6512]  c in [-1.154e+04, -0.2388]
       alpha        m4             c      chi2    Dchi2
        0.05    2.6512       -0.2844    3.4218   0.0000
        0.10    2.4054       -0.2393    3.5093   0.0875
        0.25    2.2586       -0.3544    3.7671   0.3453
        0.40    2.2228       -0.7555    4.0073   0.5855
        0.50    2.2113        -1.336    4.1521   0.7303
        0.75    2.1971        -6.048    4.4478   1.0259
        1.00    2.1911        -28.37    4.6477   1.2259
        1.50    2.1866          -609    4.8385   1.4167
        2.00    2.1852    -1.154e+04    4.8926   1.4707

  LEAVE-ONE-OUT (precision):  refit with each N dropped
      dropped     M0 m4     M1 m4      M1 c      M2 c        M3 c  M4 alpha     M4 m4   M5 beta
         2000    2.1841    2.4536   -1.2726   -7.5935    -475.027  EXACT/0  EXACT/0    0.2810
         8000    2.2022    2.2351   -0.1648   -0.6741     -20.497  EXACT/0  EXACT/0    0.2550
        16000    2.1823    2.2572   -0.3518   -1.3222     -27.315  EXACT/0  EXACT/0    0.2615
        32000    2.1634    2.1716   -0.0357   +0.0641     +13.465  EXACT/0  EXACT/0    0.2525

  DESIGN-NOISE CALIBRATION of Dchi2(M0 -> 2-parameter), Gaussian null, 200000 draws, seed 20260910:
    P50  = 0.457
    P68  = 0.991
    P90  = 2.712
    P95  = 3.863
    P99  = 6.618

  SEED BOOTSTRAP over the committed replicas (4000 resamples, seed 20260910):
    M0 m4  : median 2.1846  CI68 [2.1764, 2.1922]  CI95 [2.1679, 2.1992]  P(in band)=1.000
    M1 c   : median -0.3602  CI68 [-0.6482, -0.0558]  CI95 [-0.8802, +0.2660]  P(c<0)=0.877
    M5 beta: median 0.2615  CI68 [0.2530, 0.2705]  CI95 [0.2440, 0.2775]  P(beta>0.25)=0.898
================================================================================================
LEG BASE (3 seeds): n_points=6  n_replicas=3  sd_pool=0.8819 (dof 12)  sem_L=0.5092
        N  mean L (R001)      sd   y=L/N^(1/4)   sigma_y
      500        10.3333  1.1547       2.18523   0.10768
     1000        11.3333  0.5774       2.01538   0.09055
     2000        13.6667  0.5774       2.04364   0.07614
     4000        17.3333  1.1547       2.17955   0.06403
     8000        19.6667  0.5774       2.07950   0.05384
    16000        24.0000  1.0000       2.13394   0.04527

  model   k     chi2  dof  chi2/dof  Dchi2 vs M0     AIC     AICc      m4/A      c/beta   band
  M0      1    4.118    5      0.82        0.000    6.12     7.12    2.1111         nan     IN
  M1      2    3.965    4      0.99        0.153    7.97    11.97    2.1461     -0.1348     IN
  M2      2    4.031    4      1.01        0.087    8.03    12.03    2.1233     -0.3617     IN
  M3      2    4.114    4      1.03        0.004    8.11    12.11    2.1123     -1.6265     IN
  M4      3    3.915    3      1.31        0.203    9.92    21.92    2.3282     -0.1432     IN
  M5      2    3.903    4      0.98        0.215    7.90    11.90    2.0135      0.2555    n/a
  (M5 is fitted on L with constant sigma_L; M0 is EXACTLY M5 with beta fixed
   at 1/4, so every chi2 in this table is on ONE common scale -- see the nesting check.)

  residuals in sigma units:
    M0     +0.69    -1.06    -0.89    +1.07    -0.59    +0.50
    M1     +0.93    -0.88    -0.78    +1.09    -0.67    +0.30
    M2     +0.89    -0.92    -0.82    +1.07    -0.65    +0.37
    M3     +0.74    -1.03    -0.88    +1.06    -0.60    +0.48
    M4     +0.94    -0.85    -0.74    +1.12    -0.67    +0.25
    M5     +0.94    -0.84    -0.73    +1.13    -0.67    +0.23

  parameter uncertainty / degeneracy (M1-M3):
    M1  alpha=0.25  m4=2.1461+/-0.0932  c=-0.1348+/-0.3390  |c|/se=0.40  corr(m4,b1)=-0.9597
    M2  alpha=0.50  m4=2.1233+/-0.0489  c=-0.3617+/-1.2178  |c|/se=0.30  corr(m4,b1)=-0.8444
    M3  alpha=1.00  m4=2.1123+/-0.0323  c=-1.6265+/-25.2745  |c|/se=0.06  corr(m4,b1)=-0.5849

  M4 degeneracy scan over declared alpha domain [0.05, 2.0] (base):
    Dchi2<1      alpha in [0.050, 2.000]  m4 in [2.1078, 2.3282]  c in [-1.648, +4280]
    Dchi2<2.71   alpha in [0.050, 2.000]  m4 in [2.1078, 2.3282]  c in [-1.648, +4280]
       alpha        m4             c      chi2    Dchi2
        0.05    2.3282       -0.1432    3.9154   0.0000
        0.10    2.2145       -0.1096    3.9272   0.0118
        0.25    2.1461       -0.1348    3.9655   0.0501
        0.40    2.1290       -0.2371    4.0054   0.0900
        0.50    2.1233       -0.3617    4.0312   0.1158
        0.75    2.1159       -0.9879    4.0850   0.1696
        1.00    2.1123        -1.626    4.1143   0.1989
        1.50    2.1091        +89.73    4.0941   0.1787
        2.00    2.1078         +4280    4.0111   0.0956

  LEAVE-ONE-OUT (base):  refit with each N dropped
      dropped     M0 m4     M1 m4      M1 c      M2 c        M3 c  M4 alpha     M4 m4   M5 beta
          500    2.1065    2.2289   -0.4767   -1.9948     -56.889     1.469    2.1276    0.2645
         1000    2.1199    2.1036   +0.0667   +0.3595     +11.292     2.000    2.1150    0.2490
         2000    2.1202    2.1308   -0.0425   -0.0943      +0.994     2.000    2.1172    0.2520
         4000    2.0974    2.1385   -0.1605   -0.3598      +1.198     0.050    2.3827    0.2575
         8000    2.1209    2.1753   -0.1989   -0.6112      -6.431     0.050    2.4213    0.2575
        16000    2.0996    2.0987   +0.0031   +0.0937      +6.077     2.000    2.0916    0.2505

================================================================================================
N=8000 SENSITIVITY (precision leg): the point with 6 of 8 replicas identical
  full      : M0 m4=2.1844  chi2=4.905  M1 c=-0.3544  M4 alpha=0.050
  drop 8000 : M0 m4=2.2022  chi2=0.487  M1 c=-0.1648  M4: 3 params on 3 points -> EXACT, dof 0
  per-point sem instead of pooled (DIAGNOSTIC ONLY, violates R005):
    M0 chi2/dof=3.26 m4=2.1572   M1 chi2/dof=3.44 c=-0.5669  Dchi2=2.918

================================================================================================
BASE vs PRECISION at overlapped N (R005 pooled sigmas on both legs)
        N             precision                  base      diff   sigma
     2000        2.1869 +/-0.0525        2.0436 +/-0.0761    0.1433    1.55
     8000        2.1147 +/-0.0371        2.0795 +/-0.0538    0.0352    0.54
    16000        2.1895 +/-0.0312        2.1339 +/-0.0453    0.0556    1.01
  joint chi2 = 3.712 / 3 dof = 1.24

================================================================================================
BAND CHECK  1.8555 <= m4 <= 2.5296   (UNCONSTRAINED_DIAGNOSTIC_ONLY where marked)
  precision M0   m4=   2.1844   IN BAND
  precision M1   m4=   2.2586   IN BAND
  precision M2   m4=   2.2113   IN BAND
  precision M3   m4=   2.1911   IN BAND
  precision M4   m4=   2.6512   OUT OF BAND
  precision M4 restricted to band: alpha=0.067 m4=2.5292 c=-0.2579 chi2=3.4507  (vs free 3.4218)
  base      M0   m4=   2.1111   IN BAND
  base      M1   m4=   2.1461   IN BAND
  base      M2   m4=   2.1233   IN BAND
  base      M3   m4=   2.1123   IN BAND
  base      M4   m4=   2.3282   IN BAND
  base      M4 restricted to band: alpha=0.050 m4=2.3282 c=-0.1432 chi2=3.9154  (vs free 3.9154)

================================================================================================
M0 / M5 NESTING and DESIGN-NOISE p-VALUES
   precision: chi2(M0)=4.9051  chi2(M5|beta=1/4)=4.9051  identical=True
   precision: M5 free beta=0.2615 A=1.9558 chi2=3.3147  Dchi2 vs M0=1.5904 (1 extra param)
   precision: unweighted log-log OLS slope on mean L (R001) = 0.2552   [reproduces R001 sec. 3.1]
        base: chi2(M0)=4.1184  chi2(M5|beta=1/4)=4.1184  identical=True
        base: M5 free beta=0.2555 A=2.0135 chi2=3.9031  Dchi2 vs M0=0.2154 (1 extra param)
        base: unweighted log-log OLS slope on mean L (R001) = 0.2516   [reproduces R001 sec. 3.1]

  1-extra-parameter design-noise null (precision leg, 400000 draws, seed 20260910):
     P50  = 0.457
     P68  = 0.992
     P90  = 2.712
     P95  = 3.852
     P99  = 6.612
     Dchi2(M0->M1) = 1.138  percentile  71.4   p(>=obs) = 0.286
     Dchi2(M0->M2) = 0.753  percentile  61.4   p(>=obs) = 0.386
     Dchi2(M0->M3) = 0.257  percentile  38.6   p(>=obs) = 0.614

  2-extra-parameter null (M0 -> M4, alpha profiled over the declared domain):
     P50  = 0.787
     P68  = 1.434
     P90  = 3.386
     P95  = 4.681
     P99  = 7.730
     Dchi2(M0->M4) = 1.483  percentile  68.9   p(>=obs) = 0.311

  M5 null (beta profiled): P50=0.448 P68=0.993 P90=2.710
     Dchi2(M0->M5) = 1.590  percentile  79.2   p(>=obs) = 0.207

  per-point contribution to the M0 chi2 (precision leg):
     N=  2000  (r/sigma)^2 =  0.002     0.0% of chi2 = 4.905
     N=  8000  (r/sigma)^2 =  3.519    71.7% of chi2 = 4.905
     N= 16000  (r/sigma)^2 =  0.027     0.5% of chi2 = 4.905
     N= 32000  (r/sigma)^2 =  1.357    27.7% of chi2 = 4.905

================================================================================================
M0 GOODNESS OF FIT and CROSS-LEG CONSTANT
   precision: m4 = 2.1844 +/- 0.0168   chi2 = 4.9051 / 3 dof = 1.64   p = 0.179
        base: m4 = 2.1111 +/- 0.0262   chi2 = 4.1184 / 5 dof = 0.82   p = 0.532
  cross-leg M0 constants differ by +0.0733 = 2.36 sigma (different N ranges, so this is NOT a null test under M1-M5)
  precision without N=8000: m4 = 2.2022   chi2 = 0.4867 / 2 dof = 0.24   p = 0.784
```
