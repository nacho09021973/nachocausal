# Paper III — Fase 1: ampliación de réplicas de la pierna intervalar de precisión

```text
REPORT_ID=PAPER_III_F1_REPLICATION_17
DATE=2026-09-10
MODE=CONFIRMATORY_EXTENSION_OF_THE_NULL_CALIBRATION
DECIDED_BY=PI
STATUS=UNSIGNED
REPLICATES_PER_N=17
N_VALUES=2000,8000,16000,32000
NEW_N_VALUES=NONE
OLD_SEEDS=101-108
NEW_SEEDS=109-117
NEW_OBSERVABLES=NONE
NEW_MODELS=NONE
MINIMAL_CHANNEL_USED=NO
BOX_LEG_RUN=NO
PHASE_2_STARTED=NO
CONVENTION=PAPER_III_R001
ERROR_MODEL=PAPER_III_R005
SIGNS_NOTHING=TRUE
R007=UNSIGNED
```

Ampliación única y confirmatoria decidida por el PI tras la batería exploratoria
([informe](paper_iii_fase1_model_battery.md), commit `67ebd28`). Aquella
concluyó que lo que limita este diseño es el **número de réplicas**, no el rango
de `N`: con ocho réplicas enteras, el punto `N = 8000` acarreaba el 71.7 % del
`χ²` del modelo constante sólo porque seis de sus ocho réplicas coincidían. Esta
corrida es el remedio que ese diagnóstico señalaba.

No fija `alpha`, no busca `alpha`, no firma R007, no abre `GATE_1` y no abre la
Fase 2.

## 0. Qué se corrió, y qué no se tocó

```text
generador   dev/explore_3p1_bg_reference.py  --precision17
commit      67ebd284c3e7e5e69ac0e0f78aaf90b6b7687d77   (HEAD en el momento de correr)
gen sha256  8f6a63d703d8db8bcb546423be4131fd8b6a2634ac9ee713a32ec824721bc7ce
artefacto   dev/explore_3p1_bg_reference_precision17_results.json
art sha256  62403ded8f9d784bb348dbd21c870bdfa394efc5a8ee6067ed886d75b89b5a10
semillas    101..117 (17)   =  101..108 historicas  +  109..117 anadidas
N           2000, 8000, 16000, 32000   (los mismos cuatro; ninguno nuevo)
runtime     3:02.21 wall, 59.6 MB RSS pico, exit 0
inicio/fin  2026-09-10T16:55:17+02:00 .. 2026-09-10T16:58:19+02:00
```

Invariante, y comprobado por el verificador, no afirmado: geometría, muestreador,
normalización, convención R001, definición de `L`, definición de `N`, `τ = 1`,
proceso binomial y observable. **Lo único que cambió fue el número de réplicas.**

### 0.1 Elección de las nueve semillas

Regla declarada **antes** de correr ninguna de ellas: *las nueve enteras que
continúan contiguamente el bloque de precisión existente*. Eso da `109..117` y
nada más; no hay selección basada en resultados porque la regla no admite
libertad.

Inventario completo de semillas ya consumidas en Paper III, verificado por
inspección de código, no de memoria:

| lista | semillas | dónde |
|---|---|---|
| pierna de caja | 11, 12, 13 | `dev/explore_3p1_scale_calibration.py:49` |
| pierna intervalar base | 21, 22, 23 | `dev/explore_3p1_bg_reference.py:74` |
| pierna de precisión | 101–108 | `dev/explore_3p1_bg_reference.py:119` |
| auditoría del proceso puntual | 101, 102, 103 | `dev/verify_3p1_phase0_contract.py:160` |
| auditoría de aceptación | 999 | `dev/verify_3p1_phase0_contract.py:161` |

`109..117` es disjunto de todas ellas. El verificador lo recomprueba en cada
ejecución en vez de confiar en esta tabla.

### 0.2 Procedencia: el artefacto histórico no se sobrescribió

El repo ya tenía política para esto — `ARTIFACT_POLICY=NEW_VERSIONED_ARTIFACT`
en [el contrato de la Fase 0](paper_iii_fase0_contrato.md) — y la pierna de caja
ya la usa para sus dos linajes pre-R001 / R001. La ampliación la sigue:

| artefacto | réplicas | estado |
|---|---|---|
| `..._precision_results.json` | 8 | **histórico, intacto**, `eb101d3f…91e7` sin cambio |
| `..._precision17_results.json` | 17 | nuevo, identidad propia |

El artefacto de 8 réplicas sigue respaldando §3.1 de las notas a través de
`dev/verify_3p1_notes_figures.py`, que sigue dando `ALL FIGURES MATCH`. La nota
histórica no se ha reescrito.

### 0.3 El cambio al generador es editorial, y se demuestra

El generador se parametrizó (`seeds`, `out`) con **valores por defecto iguales al
comportamiento anterior**. Dos comprobaciones, no una promesa:

1. `main_precision()` con sus argumentos por defecto reproduce el artefacto
   histórico **byte a byte** (`diff` vacío; el fichero comprometido no se tocó).
2. Como cada semilla produce su cadena de forma independiente, las **8 primeras
   entradas de la corrida de 17 tienen que ser las 8 de la corrida histórica,
   valor por valor.** Lo son, en los cuatro `N`:

```text
N=  2000  compartidas 8: [11, 12, 12, 13, 14, 14, 12, 13]   anadidas 9: [12, 13, 11, 12, 12, 12, 12, 12, 12]
N=  8000  compartidas 8: [19, 18, 18, 18, 17, 18, 18, 18]   anadidas 9: [19, 19, 18, 19, 19, 17, 19, 18, 19]
N= 16000  compartidas 8: [23, 22, 22, 23, 23, 25, 21, 22]   anadidas 9: [25, 22, 22, 23, 22, 23, 22, 22, 23]
N= 32000  compartidas 8: [27, 27, 29, 27, 28, 26, 29, 28]   anadidas 9: [27, 28, 27, 27, 27, 26, 28, 27, 26]
```

Ésa es la comprobación que importa: si la edición hubiera movido el muestreador,
fallaría ruidosamente. Está en la sección `[A3]` de
`dev/verify_3p1_phase0_contract.py`, no sólo en este documento.

---

## 1. OBSERVED

`L` bajo R001 (`= |cadena|`, extremos incluidos; sobre las `Ls` guardadas, `+2`).
`sigma_y` con la regla de error firmada en R005: `sd` **agrupada** sobre el
barrido, `sem = sd_pool/sqrt(n_rep)`.

### 1.1 Pierna de 17 réplicas (canal principal)

```text
n_points = 4    n_replicas = 17    sd_pool = 0.8880 (64 dof)    sem_L = 0.2154
```

| `N` | `⟨L⟩` (R001) | `sd` | `y = L/N^(1/4)` | `sigma_y` |
|---|---|---|---|---|
| 2 000 | 14.2941 | 0.8489 | 2.13747 | 0.03221 |
| 8 000 | 20.2941 | 0.6860 | 2.14584 | 0.02277 |
| 16 000 | 24.6471 | 1.0572 | 2.19147 | 0.01915 |
| 32 000 | 29.2941 | 0.9196 | 2.19025 | 0.01610 |

### 1.2 Contraste con la corrida histórica de 8 réplicas

| `N` | `y` (8 rép.) | `y` (17 rép.) | `sigma_y` (8) | `sigma_y` (17) |
|---|---|---|---|---|
| 2 000 | 2.18695 | 2.13747 | 0.05251 | 0.03221 |
| 8 000 | 2.11474 | 2.14584 | 0.03713 | 0.02277 |
| 16 000 | 2.18951 | 2.19147 | 0.03122 | 0.01915 |
| 32 000 | 2.21499 | 2.19025 | 0.02626 | 0.01610 |

**O1 — la no monotonía de `y` desapareció.** Con 8 réplicas `y` bajaba en
`N = 8000` y volvía a subir; ese perfil era el hecho observado O1 de la batería.
Con 17 réplicas `y` crece hasta `N = 16000` y se aplana. El perfil anterior era
ruido de réplica, no forma.

**O2 — la dispersión del barrido se redujo a la mitad.** `+4.74 %` → `+2.53 %`,
mientras la incertidumbre por punto bajó de `1.58 %` a `0.97 %`. La separación
entre extremos pasó de `0.48 sigma` a `1.47 sigma`: el diseño ganó resolución
real, no sólo puntos.

**O3 — la patología de empates se resolvió.** Es el objetivo declarado de la
ampliación, y se cumplió:

| `N` | `sd` (8 rép.) | `sd` (17 rép.) | valores distintos de 17 |
|---|---|---|---|
| 2 000 | 1.0607 | 0.8489 | 4 |
| **8 000** | **0.5345** | **0.6860** | 3 |
| 16 000 | 1.1877 | 1.0572 | 4 |
| 32 000 | 1.0607 | 0.9196 | 4 |

La `sd` de `N = 8000` era la mitad que la de sus vecinos con 8 réplicas; con 17
está dentro del rango de los demás. El artefacto que motivaba la cláusula de `sd`
agrupada de R005 ya no está presente en los datos.

---

## 2. Pendientes

| corrida | global `d log⟨L⟩/d log N` | locales |
|---|---|---|
| 17 réplicas | **0.2600** | 0.2528, 0.2804, 0.2492 |
| 8 réplicas | 0.2552 | 0.2258, 0.3001, 0.2667 |

Las locales se estabilizaron: su rango cayó de `0.074` a `0.031`. La global
apenas se movió.

Suelo de resolución del diseño sobre una pendiente, declarado en R005: **0.0179**
(el exponente de valor exactamente conocido sale `1.0179` en vez de `1`).

---

## 3. Modelo constante M0 — `y = m₄`

Ajuste por mínimos cuadrados ponderados con las `sigma` de R005.

| pierna | `m₄` | `χ²` | dof | `χ²/dof` | `p` | banda |
|---|---|---|---|---|---|---|
| **precisión, 17 réplicas** | **2.1762 ± 0.0103** | 4.6196 | 3 | **1.54** | **0.202** | IN |
| precisión, 8 réplicas | 2.1844 ± 0.0168 | 4.9051 | 3 | 1.64 | 0.179 | IN |
| base, 3 réplicas | 2.1111 ± 0.0262 | 4.1184 | 5 | 0.82 | 0.532 | IN |

**El modelo constante sigue siendo suficiente**, con `m₄` dentro de la banda
rigurosa `[1.8555, 2.5296]` y con la mitad de incertidumbre que antes.

### 3.1 La contribución al `χ²` ya no está en un punto

| `N` | % del `χ²` (8 rép.) | % del `χ²` (17 rép.) |
|---|---|---|
| 2 000 | 0.0 % | 31.3 % |
| **8 000** | **71.7 %** | **38.4 %** |
| 16 000 | 0.5 % | 13.8 % |
| 32 000 | 27.7 % | 16.5 % |

Con 8 réplicas dos puntos aportaban el 99.4 % del `χ²`. Con 17 la contribución
está repartida. **El contraste ya no depende de un solo punto**, que era la
condición que R005 exige para que sea admisible como evidencia.

### 3.2 El modelo de error ya casi no cambia el resultado

`UNCONSTRAINED_DIAGNOSTIC_ONLY` — usando `sem` punto a punto, que R005 prohíbe:

| corrida | `χ²/dof` agrupado (R005) | `χ²/dof` punto a punto | brecha |
|---|---|---|---|
| 8 réplicas | 1.64 | 3.26 | **×1.99** |
| 17 réplicas | 1.54 | 1.79 | ×1.16 |

Con 8 réplicas la elección del modelo de error casi duplicaba el `χ²`. Con 17 la
brecha se cierra. La cláusula de R005 sigue siendo la regla, pero ya no es lo que
sostiene el resultado.

---

## 4. `beta` frente a `1/4` — el hallazgo sustantivo

M5 descriptivo, `L = A N^beta`, ajustado sobre `L` con `sigma_L` constante. **M0
es exactamente M5 con `beta` fijado en `1/4`** (verificado numéricamente:
`χ² = 4.6196` en ambas parametrizaciones), luego la comparación es anidada y los
`χ²` viven en una sola escala.

| pierna | `A` | `beta` | intervalo `Δχ² < 1` | `Δχ²` vs `beta = 1/4` | ¿contiene `1/4`? |
|---|---|---|---|---|---|
| **precisión, 17 rép.** | 1.9687 | **0.2604** | [0.2549, 0.2660] | **3.517** | **no** |
| precisión, 8 rép. | 1.9564 | 0.2615 | [0.2524, 0.2706] | 1.590 | no (por poco) |
| base, 3 rép. | 2.0147 | 0.2554 | [0.2438, 0.2672] | 0.215 | sí |

`beta` **no se movió** al triplicar las réplicas (`0.2615 → 0.2604`); lo que se
movió fue la incertidumbre. Eso es exactamente lo que hacen más réplicas cuando
hay algo estable debajo.

Bootstrap sobre las 17 semillas comprometidas (20 000 remuestreos, semilla
`20260910`):

```text
m4   : mediana 2.1762  IC68 [2.1683, 2.1841]  IC95 [2.1606, 2.1914]  P(en banda) = 1.000
beta : mediana 0.2605  IC68 [0.2560, 0.2650]  IC95 [0.2515, 0.2695]  P(beta > 1/4) = 0.986
```

### 4.1 Calibrado contra el ruido del propio diseño

Nula explícita: verdad constante, geometría exacta de este barrido, `sigma` de
R005. No genera datos físicos; es la distribución del estadístico.

```text
nula de Dchi2(M0 -> M5), 60000 realizaciones, semilla 20260910:
   P50 = 0.458   P68 = 0.992   P90 = 2.705   P95 = 3.917   P99 = 6.708
   observado 3.517  ->  percentil 93.8   p(>=obs) = 0.0624
```

Y la distribución de `beta` cuando la verdad **es** `1/4`, en este mismo diseño:

```text
   media 0.2500   sd 0.0056   95% central [0.2390, 0.2610]
   P(beta_hat >= 0.2605) = 0.0329   ->  1.89 sigma
```

### 4.2 Contra el suelo del diseño, que es la regla firmada

R005 obliga: *«Toda desviación respecto de un valor esperado se compara
explícitamente contra el suelo de resolución del propio diseño.»*

```text
|beta - 1/4|                        = 0.0105
suelo de resolucion declarado (R005) = 0.0179
ratio                                = 0.59      ->  POR DEBAJO del suelo
sd muestral de beta_hat              = 0.0056    ->  el error ESTADISTICO ya esta
                                                     por debajo del suelo del diseno
```

**La desviación es real, reproducible y estadísticamente marginal (1.9 sigma), y
está por debajo del suelo de resolución que el propio diseño declara.** Por la
regla firmada, no cuenta como desviación.

Hay que declarar además una limitación que esto expone y que no estaba visible
con 8 réplicas: **ese suelo de `0.0179` se midió en la pierna de caja**, donde
existe un exponente de valor exactamente conocido (`d log⟨V⟩_all/d log ρ = 1`).
La pierna intervalar **no tiene un calibrador exactamente conocido propio**,
porque en ella `N` es fijo y `ρ·Vol = N` por construcción. El suelo está por
tanto **importado**, no medido in situ. Mientras siga importado, `+0.0105` no
puede promoverse ni descartarse por completo con este diseño.

---

## 5. Leave-one-out

| quitado | `m₄` (M0) | `χ²` M0 | dof | `beta` | `A` |
|---|---|---|---|---|---|
| 2 000 | 2.1806 | 3.0103 | 2 | 0.2629 | 1.9212 |
| 8 000 | 2.1839 | 2.3898 | 2 | 0.2585 | 2.0103 |
| 16 000 | 2.1700 | 3.7262 | 2 | 0.2602 | 1.9674 |
| 32 000 | 2.1665 | 3.3352 | 2 | 0.2629 | 1.9268 |

```text
m4   rango 2.1665 .. 2.1839   (amplitud 0.0174; se = 0.0103)
beta rango 0.2585 .. 0.2629   (amplitud 0.0044; NO contiene 1/4 en ninguna variante)
```

Ambos parámetros son estables. `beta` se mantiene por encima de `1/4` quitando
cualquiera de los cuatro puntos, y su excursión total (`0.0044`) es menor que su
propia `sd` muestral (`0.0056`). Con 8 réplicas, en cambio, quitar `N = 8000`
llevaba el `χ²` de M0 de `4.905` a `0.487`; ahora quitar cualquier punto lo deja
entre `2.39` y `3.73`. **Ningún punto domina.**

---

## 6. Qué cambió en el diseño

| magnitud | 8 réplicas | 17 réplicas |
|---|---|---|
| incertidumbre relativa por punto | 1.58 % | **0.97 %** |
| dispersión de `y` en el barrido | +4.74 % | +2.53 % |
| separación de extremos | 0.48 σ | **1.47 σ** |
| dof de la `sd` agrupada | 28 | **64** |
| se relativa de `sd_pool` | 13.4 % | **8.8 %** |
| fracción del `χ²` en un punto | 71.7 % | 38.4 % |

R005 exige declarar que el número de réplicas basta para que la `sd` agrupada sea
estable. Con 64 dof su error relativo es del `8.8 %`, y la brecha entre modelos
de error se cerró a `×1.16` (§3.2). **Se declara suficiente.** Con 8 réplicas y
`×1.99` de brecha, no lo era.

Lo importante para lo que viene: **el error estadístico (`0.0056`) es ahora menor
que el suelo del diseño (`0.0179`).** La limitación se ha desplazado. Ya no es un
problema de réplicas — más semillas no resolverán la pregunta de `beta`.

---

## 7. Resultado secundario, no usado para seleccionar nada

No se corrió ninguna búsqueda de `alpha`; M4 no se ajustó. Las tres correcciones
de `alpha` **fijado** salen de la misma rutina y se registran sólo por eso:

| `alpha` | `m₄` | `c` | `χ²` | `Δχ²` vs M0 |
|---|---|---|---|---|
| 0.25 | 2.2551 | −0.3771 | 1.2064 | 3.413 |
| 0.50 | 2.2102 | −1.6908 | 1.4180 | 3.202 |
| 1.00 | 2.1893 | −55.94 | 1.9640 | 2.656 |

Siguen siendo mutuamente indistinguibles entre sí y del `Δχ² = 3.517` de M5, con
`Δχ²` separados por menos de una unidad. **No se elige ninguna, no se promueve
ninguna y no se usa AIC ni AICc para decidir nada.**

---

## 8. Clasificación

```text
VERDICT = A) NULL_CALIBRATION_STABLE
```

M0 sigue siendo suficiente (`χ²/dof = 1.54`, `p = 0.202`, `m₄` en banda), y
`beta − 1/4 = +0.0105` está **por debajo** del suelo de resolución que el diseño
declara (`0.0179`). Al nivel que el diseño permite, `beta` es compatible con
`1/4`. Los datos con 17 réplicas **no proporcionan evidencia que obligue a
abandonar la calibración nula.**

**No es (B).** El criterio de B exige una desviación que supere *claramente* la
dispersión **y** el suelo del diseño. Ésta supera la dispersión sólo
marginalmente (`1.89 sigma`, `p = 0.062` contra ruido calibrado) y **no supera el
suelo** (`0.59×`). Promoverla a B sería exactamente convertir una diferencia
numérica pequeña en una ley.

**No es (C).** El diseño no está sin potencia: triplicar las réplicas redujo la
incertidumbre por punto a `0.97 %`, llevó la `sd` agrupada a 64 dof, disolvió la
dominancia de `N = 8000` y dejó el error estadístico de `beta` (`0.0056`) por
**debajo** del suelo sistemático. Eso es un diseño que ya rinde lo que puede
rendir, no uno corto de datos.

### 8.1 Lo que hay que llevarse, y no perder

Tres hechos que este informe deja establecidos y que no deben diluirse en el
veredicto:

1. **`beta` está por encima de `1/4` de forma reproducible.** `0.2615` (8
   semillas), `0.2604` (17 semillas), `0.2554` (pierna base, semillas
   independientes 21–23). Tres conjuntos disjuntos, mismo signo, misma magnitud.
   Sobrevive a leave-one-out en las cuatro variantes.
2. **Es marginal, no es evidencia.** `1.89 sigma`; `p = 0.062` contra la nula
   calibrada del propio diseño. Eso ocurre por azar una vez de cada dieciséis.
3. **Ya no es una pregunta de réplicas.** El error estadístico cayó por debajo
   del suelo del diseño. Lo que ahora limita es que **el suelo de `0.0179` está
   importado de la pierna de caja** y la pierna intervalar carece de calibrador
   exactamente conocido propio. Caracterizar ese suelo *in situ* — no añadir
   semillas — es lo que decidiría esta pregunta.

Y una observación aritmética sobre la convención, sin interpretación: bajo R001
se mide la pendiente de `L_interior + 2`, y añadir una constante positiva a una
ley de potencias **reduce** la pendiente log-log efectiva a `N` finito. El
`+0.0105` observado no lo produce la convención; la convención lo atenúa.

---

## 9. Qué NO autoriza este informe

- No firma R007 ni ninguna otra resolución.
- No fija `alpha`, no busca `alpha`, no promueve ninguna familia de corrección.
- No declara `GATE_1`. La Fase 1 no se cierra aquí.
- No autoriza más corridas, semillas, `N` ni `rho`.
- No reabre el canal de minimales, que sigue suspendido por R004 como contraste
  de escala.
- No ejecuta ni autoriza la pierna de caja ni la Fase 2.
- No extrapola a Schwarzschild ni interpreta geométricamente `R`.
- No declara alcanzado ni no alcanzado ningún régimen asintótico.

```text
GATE_0 = PASS       (revalidado tras la ampliacion; 0 bloqueos abiertos)
GATE_1 = NOT_DECLARED
R007   = UNSIGNED
```

## 10. Validación ejecutada

```text
python3 dev/verify_3p1_notes_figures.py      -> exit 0   ALL FIGURES MATCH
python3 dev/verify_3p1_phase0_contract.py    -> exit 0   STRUCTURAL CHECKS: ALL PASS
                                                         GATE_0 BLOCKERS: 0 open
```

El segundo incorpora la sección `[A3]`, que certifica el linaje de la ampliación:
hash del artefacto histórico sin cambio, hash del nuevo artefacto, diseño
idéntico salvo el recuento de réplicas, 17 réplicas declaradas y realizadas en
cada `N`, semillas añadidas disjuntas de todas las listas de Paper III, réplicas
compartidas idénticas valor por valor, y agregados re-derivados de las `Ls`
crudas. **Ningún verificador se relajó ni se modificó para acomodar un
resultado**; la única modificación de hashes fue registrar el estado editorial
declarado del generador, que es el mecanismo que el propio repo usa para
distinguir una edición declarada de una no declarada.

---

## Apéndice A — script de análisis

Lee artefactos comprometidos y hace aritmética de ajuste. No importa ningún
generador y no escribe nada.

```text
sha256 = 8462f491e87c2b7232007abbe7126eb2e1d3509b8e06ea18a1ac3ad460684cf6
```

```python
"""EXPLORATION -- Paper III, Phase 1: analysis of the 17-replicate precision leg.

Reads committed artifacts only. Runs no generator. Computes ONLY the quantities
already used in the Phase 1 model battery (commit 67ebd28):
  mean L, sd, sem, L/N^(1/4), global slope, local slopes, M0 constant fit,
  chi2/dof under R005 pooled error, comparison with beta = 1/4, M5 = A N^beta,
  and leave-one-out of M0 and beta.
No alpha search. No AIC/AICc used to decide anything. No new observable.
Convention R001: stored Ls are interior counts; L = interior + 2.
"""
import json
import numpy as np
from scipy.stats import chi2 as _chi2

BAND = (1.8555, 2.5296)
P8 = "dev/explore_3p1_bg_reference_precision_results.json"
P17 = "dev/explore_3p1_bg_reference_precision17_results.json"
BASE = "dev/explore_3p1_bg_reference_results.json"


def leg(path):
    o = json.load(open(path))
    rows = o["rows"]
    N = np.array([r["N"] for r in rows], float)
    Ls = [np.asarray(r["Ls"], float) + 2.0 for r in rows]      # R001
    L = np.array([a.mean() for a in Ls])
    sd = np.array([a.std(ddof=1) for a in Ls])
    n_rep = Ls[0].size
    sd_pool = float(np.sqrt(np.mean(sd ** 2)))
    sem = sd_pool / np.sqrt(n_rep)
    return dict(N=N, Ls=Ls, L=L, sd=sd, n_rep=n_rep, sd_pool=sd_pool, sem=sem,
                y=L / N ** 0.25, sy=sem / N ** 0.25, seeds=o.get("seeds"),
                sem_ind=sd / np.sqrt(n_rep), local=o.get("local_slopes"))


def fit_M0(N, y, s):
    w = 1.0 / s ** 2
    m = float((w * y).sum() / w.sum())
    return m, float((w * (y - m) ** 2).sum()), float(1.0 / np.sqrt(w.sum()))


def fit_M5(N, L, sem, lo=0.05, hi=0.60, n=110001):
    """L = A N^beta, WLS on L with constant sigma_L. A is linear given beta."""
    w = 1.0 / sem ** 2
    bs = np.linspace(lo, hi, n)
    F = N[None, :] ** bs[:, None]
    A = (F * L).sum(1) / (F * F).sum(1)
    chi = (w * (L - A[:, None] * F) ** 2).sum(1)
    i = int(np.argmin(chi))
    return float(A[i]), float(bs[i]), float(chi[i]), bs, chi


def beta_interval(bs, chi, thr=1.0):
    m = chi.min()
    sel = bs[chi <= m + thr]
    return float(sel.min()), float(sel.max())


def fit_fixed_alpha(N, y, s, alpha):
    X = np.column_stack([np.ones_like(N), N ** (-alpha)])
    w = 1.0 / s ** 2
    A = X.T @ (X * w[:, None])
    b = np.linalg.solve(A, X.T @ (w * y))
    r = y - X @ b
    return float(b[0]), float(b[1] / b[0]), float((w * r ** 2).sum())


def header(tag, d):
    print("=" * 96)
    print(f"{tag}: n_points={len(d['N'])}  n_replicas={d['n_rep']}  "
          f"sd_pool={d['sd_pool']:.4f} (dof {(d['n_rep']-1)*len(d['N'])})  "
          f"sem_L={d['sem']:.4f}")
    if d["seeds"]:
        print(f"  seeds: {d['seeds'][0]}..{d['seeds'][-1]}  ({len(d['seeds'])} seeds)")
    print(f"  {'N':>7}{'mean L (R001)':>15}{'sd':>9}{'sem(pool)':>11}"
          f"{'y=L/N^(1/4)':>14}{'sigma_y':>10}")
    for i in range(len(d["N"])):
        print(f"  {int(d['N'][i]):7d}{d['L'][i]:15.4f}{d['sd'][i]:9.4f}"
              f"{d['sem']:11.4f}{d['y'][i]:14.5f}{d['sy'][i]:10.5f}")


d8, d17, db = leg(P8), leg(P17), leg(BASE)

print("#" * 96)
print("# PROVENANCE: the 17-seed run contains the 8-seed run, value for value")
print("#" * 96)
o8 = json.load(open(P8))
o17 = json.load(open(P17))
allmatch = True
for r8, r17 in zip(o8["rows"], o17["rows"]):
    same = r17["Ls"][:8] == r8["Ls"]
    allmatch &= same and r8["N"] == r17["N"]
    print(f"  N={r8['N']:6d}  first 8 of 17 == historical 8: {same}   "
          f"new 9 (seeds 109-117): {r17['Ls'][8:]}")
print(f"  seeds 8-run : {o8['seeds']}")
print(f"  seeds 17-run: {o17['seeds']}")
print(f"  DESIGN_UNPERTURBED = {allmatch}")

print()
header("17-REPLICATE PRECISION LEG (primary)", d17)
print()
header("8-REPLICATE PRECISION LEG (historical, for contrast)", d8)

# ---------------------------------------------------------------------------
print("\n" + "=" * 96)
print("SLOPES (R001 convention)")
for tag, d in (("17-seed", d17), ("8-seed", d8)):
    g = float(np.polyfit(np.log(d["N"]), np.log(d["L"]), 1)[0])
    loc = [float(np.log(d["L"][i + 1] / d["L"][i]) / np.log(d["N"][i + 1] / d["N"][i]))
           for i in range(len(d["N"]) - 1)]
    print(f"  {tag}: global d log<L>/d log N = {g:.4f}   "
          f"local = {[round(v,4) for v in loc]}")
print("  design floor on a slope (R005): 0.0179  (the exactly-known exponent returns 1.0179)")

# ---------------------------------------------------------------------------
print("\n" + "=" * 96)
print("M0 CONSTANT FIT  y = m4   (R005 pooled error)")
for tag, d in (("17-seed precision", d17), ("8-seed precision", d8), ("base (3 seeds)", db)):
    m, c, se = fit_M0(d["N"], d["y"], d["sy"])
    dof = len(d["N"]) - 1
    inb = BAND[0] <= m <= BAND[1]
    print(f"  {tag:<20} m4 = {m:.4f} +/- {se:.4f}   chi2 = {c:.4f} / {dof} dof "
          f"= {c/dof:.2f}   p = {_chi2.sf(c, dof):.4f}   band: {'IN' if inb else 'OUT'}")
print("  DIAGNOSTIC_ONLY (per-point sem, which R005 forbids):")
for tag, d in (("17-seed precision", d17), ("8-seed precision", d8)):
    m, c, se = fit_M0(d["N"], d["y"], d["sem_ind"] / d["N"] ** 0.25)
    print(f"    {tag:<20} chi2/dof = {c/(len(d['N'])-1):.2f}   m4 = {m:.4f}")

# ---------------------------------------------------------------------------
print("\n" + "=" * 96)
print("PER-POINT CONTRIBUTION TO THE M0 CHI2")
for tag, d in (("17-seed", d17), ("8-seed", d8)):
    m, c, _ = fit_M0(d["N"], d["y"], d["sy"])
    print(f"  {tag}  (chi2 = {c:.4f})")
    for i in range(len(d["N"])):
        q = ((d["y"][i] - m) / d["sy"][i]) ** 2
        print(f"     N={int(d['N'][i]):6d}  (r/sigma)^2 = {q:6.3f}   {100*q/c:5.1f}%"
              f"   ties at this N: {17 if tag=='17-seed' else 8} replicas -> "
              f"{len(set(map(int, d['Ls'][i])))} distinct values")

# ---------------------------------------------------------------------------
print("\n" + "=" * 96)
print("M5 DESCRIPTIVE FIT  L = A N^beta   and COMPARISON WITH beta = 1/4")
for tag, d in (("17-seed precision", d17), ("8-seed precision", d8), ("base (3 seeds)", db)):
    A, b, chi, bs, cc = fit_M5(d["N"], d["L"], d["sem"])
    lo, hi = beta_interval(bs, cc, 1.0)
    m, c0, _ = fit_M0(d["N"], d["y"], d["sy"])
    print(f"  {tag:<20} A = {A:.4f}  beta = {b:.4f}   "
          f"Dchi2<1 interval [{lo:.4f}, {hi:.4f}]   "
          f"chi2 = {chi:.4f}   Dchi2 vs beta=1/4: {c0-chi:.4f}")
    print(f"  {'':<20} beta - 1/4 = {b-0.25:+.4f}   "
          f"{'CONTAINS 1/4' if lo <= 0.25 <= hi else 'EXCLUDES 1/4'} at Dchi2<1")
print("  (M0 is EXACTLY M5 with beta fixed at 1/4: same chi2 scale, verified below.)")
for tag, d in (("17-seed", d17), ("8-seed", d8)):
    f = d["N"] ** 0.25
    A = (f * d["L"]).sum() / (f * f).sum()
    cq = float((((d["L"] - A * f) / d["sem"]) ** 2).sum())
    _, c0, _ = fit_M0(d["N"], d["y"], d["sy"])
    print(f"     {tag}: chi2(M0) = {c0:.4f}   chi2(M5|beta=1/4) = {cq:.4f}   "
          f"identical = {abs(c0-cq) < 1e-9}")

# ---------------------------------------------------------------------------
print("\n" + "=" * 96)
print("SEED BOOTSTRAP over the committed replicas (17-seed leg, 20000 resamples, seed 20260910)")
rng = np.random.default_rng(20260910)
BGRID = np.linspace(0.05, 0.60, 1101)
FGRID = d17["N"][None, :] ** BGRID[:, None]          # beta grid x N, fixed
m4s, bes = [], []
for _ in range(20000):
    idx = rng.integers(0, d17["n_rep"], d17["n_rep"])
    L = np.array([a[idx].mean() for a in d17["Ls"]])
    sd = np.array([a[idx].std(ddof=1) for a in d17["Ls"]])
    sp = float(np.sqrt(np.mean(sd ** 2)))
    if sp == 0:
        continue
    sem = sp / np.sqrt(d17["n_rep"])
    m, _, _ = fit_M0(d17["N"], L / d17["N"] ** 0.25, sem / d17["N"] ** 0.25)
    m4s.append(m)
    A = (FGRID * L).sum(1) / (FGRID * FGRID).sum(1)   # sigma_L constant -> cancels
    chi = ((L - A[:, None] * FGRID) ** 2).sum(1) / sem ** 2
    bes.append(float(BGRID[int(np.argmin(chi))]))
m4s, bes = np.asarray(m4s), np.asarray(bes)
print(f"  m4  : median {np.median(m4s):.4f}  CI68 [{np.percentile(m4s,16):.4f}, "
      f"{np.percentile(m4s,84):.4f}]  CI95 [{np.percentile(m4s,2.5):.4f}, "
      f"{np.percentile(m4s,97.5):.4f}]  P(in band) = {np.mean((m4s>=BAND[0])&(m4s<=BAND[1])):.3f}")
print(f"  beta: median {np.median(bes):.4f}  CI68 [{np.percentile(bes,16):.4f}, "
      f"{np.percentile(bes,84):.4f}]  CI95 [{np.percentile(bes,2.5):.4f}, "
      f"{np.percentile(bes,97.5):.4f}]  P(beta > 1/4) = {np.mean(bes>0.25):.3f}")

# ---------------------------------------------------------------------------
print("\n" + "=" * 96)
print("LEAVE-ONE-OUT of M0 and beta (17-seed leg)")
print(f"  {'dropped':>9}{'M0 m4':>10}{'M0 chi2':>10}{'dof':>5}{'beta':>10}{'A':>10}")
N, y, s, L, sem = d17["N"], d17["y"], d17["sy"], d17["L"], d17["sem"]
for i in range(len(N)):
    k = [j for j in range(len(N)) if j != i]
    m, c, _ = fit_M0(N[k], y[k], s[k])
    A, b, _, _, _ = fit_M5(N[k], L[k], sem)
    print(f"  {int(N[i]):9d}{m:10.4f}{c:10.4f}{len(k)-1:5d}{b:10.4f}{A:10.4f}")
mm = [fit_M0(N[[j for j in range(len(N)) if j != i]], y[[j for j in range(len(N)) if j != i]],
             s[[j for j in range(len(N)) if j != i]])[0] for i in range(len(N))]
bb = [fit_M5(N[[j for j in range(len(N)) if j != i]], L[[j for j in range(len(N)) if j != i]],
             sem)[1] for i in range(len(N))]
print(f"  m4 range   {min(mm):.4f} .. {max(mm):.4f}   (span {max(mm)-min(mm):.4f}, "
      f"se = {fit_M0(N,y,s)[2]:.4f})")
print(f"  beta range {min(bb):.4f} .. {max(bb):.4f}   (span {max(bb)-min(bb):.4f}; "
      f"contains 1/4: {min(bb) <= 0.25 <= max(bb)})")

# ---------------------------------------------------------------------------
print("\n" + "=" * 96)
print("SECONDARY, NOT USED TO SELECT ANYTHING: fixed-alpha corrections from the same routine.")
print("No free-alpha (M4) search was run. Reported only because it costs nothing.")
m, c0, _ = fit_M0(N, y, s)
print(f"  {'alpha':>8}{'m4':>10}{'c':>12}{'chi2':>10}{'Dchi2 vs M0':>14}")
for al in (0.25, 0.5, 1.0):
    mm4, cc, ch = fit_fixed_alpha(N, y, s, al)
    print(f"  {al:8.2f}{mm4:10.4f}{cc:+12.4f}{ch:10.4f}{c0-ch:14.4f}")

# ---------------------------------------------------------------------------
print("\n" + "=" * 96)
print("DESIGN RESOLUTION with 17 replicas")
rel = d17["sem"] / d17["L"].mean()
obs = d17["y"].max() / d17["y"].min() - 1
print(f"  per-point relative uncertainty : {rel:.2%}   (8-seed run: {d8['sem']/d8['L'].mean():.2%})")
print(f"  observed spread of y over sweep: {obs:+.2%}   (8-seed run: "
      f"{d8['y'].max()/d8['y'].min()-1:+.2%})")
se_diff = float(np.sqrt(d17["sy"][0] ** 2 + d17["sy"][-1] ** 2))
print(f"  endpoint separation: {(d17['y'][-1]-d17['y'][0])/se_diff:+.2f} sigma "
      f"(8-seed run: {(d8['y'][-1]-d8['y'][0])/float(np.sqrt(d8['sy'][0]**2+d8['sy'][-1]**2)):+.2f} sigma)")
print(f"  pooled sd dof: {(d17['n_rep']-1)*len(N)}  -> relative se of sd_pool "
      f"= {1/np.sqrt(2*(d17['n_rep']-1)*len(N)):.1%}  (8-seed: "
      f"{1/np.sqrt(2*(d8['n_rep']-1)*len(N)):.1%})")


# ---------------------------------------------------------------------------
def design_noise_null(d17):
    """Design-noise calibration of Dchi2(M0 -> M5) and of beta_hat itself, under a
    CONSTANT truth, with the R005 sigmas and this exact sweep geometry.
    No generator, no new observable: the null distribution of the statistic."""
    print("\n" + "=" * 96)
    print("DESIGN-NOISE CALIBRATION (17-replicate geometry, constant truth)")
    N, L, sem = d17["N"], d17["L"], d17["sem"]
    BG = np.linspace(0.05, 0.60, 1101)
    F = N[None, :] ** BG[:, None]
    f4 = N ** 0.25

    obs_c0 = ((L - ((L * f4).sum() / (f4 * f4).sum()) * f4) ** 2).sum() / sem ** 2
    A = (L[None, :] * F).sum(1) / (F * F).sum(1)
    obs_chi = ((L[None, :] - A[:, None] * F) ** 2).sum(1) / sem ** 2
    obs_d = obs_c0 - obs_chi.min()
    bhat = float(BG[int(np.argmin(obs_chi))])
    print(f"  observed: chi2(M0) = {obs_c0:.4f}  chi2(M5) = {obs_chi.min():.4f}  "
          f"Dchi2 = {obs_d:.4f}  beta_hat = {bhat:.4f}")

    rng = np.random.default_rng(20260910)
    out = []
    for chunk in np.array_split(np.arange(60000), 30):
        Lb = 2.176 * f4 + rng.normal(0, sem, (len(chunk), len(N)))
        A0 = (Lb * f4).sum(1) / (f4 * f4).sum()
        c0 = ((Lb - A0[:, None] * f4) ** 2).sum(1) / sem ** 2
        Aa = (Lb[:, None, :] * F[None, :, :]).sum(2) / (F * F).sum(1)[None, :]
        cc = ((Lb[:, None, :] - Aa[:, :, None] * F[None, :, :]) ** 2).sum(2) / sem ** 2
        out.append(c0 - cc.min(1))
    D = np.concatenate(out)
    print("  null of Dchi2(M0->M5), 60000 draws, seed 20260910:")
    for q in (50, 68, 90, 95, 99):
        print(f"     P{q:<3d} = {np.percentile(D, q):.3f}")
    print(f"     observed {obs_d:.3f} -> percentile {100*np.mean(D <= obs_d):.1f}   "
          f"p(>=obs) = {np.mean(D >= obs_d):.4f}")

    rng2 = np.random.default_rng(20260911)
    bs = []
    for chunk in np.array_split(np.arange(40000), 20):
        Lb = 2.176 * f4 + rng2.normal(0, sem, (len(chunk), len(N)))
        Aa = (Lb[:, None, :] * F[None, :, :]).sum(2) / (F * F).sum(1)[None, :]
        cc = ((Lb[:, None, :] - Aa[:, :, None] * F[None, :, :]) ** 2).sum(2)
        bs.append(BG[np.argmin(cc, axis=1)])
    bs = np.concatenate(bs)
    print(f"\n  beta_hat when the truth IS beta = 1/4 (same design): "
          f"mean {bs.mean():.4f}  sd {bs.std():.4f}")
    print(f"     central 95%: [{np.percentile(bs,2.5):.4f}, {np.percentile(bs,97.5):.4f}]")
    print(f"     P(beta_hat >= {bhat:.4f}) = {np.mean(bs >= bhat):.4f}   "
          f"-> {abs(bhat-0.25)/bs.std():.2f} sigma")

    print(f"\n  R005 comparison against the DESIGN FLOOR (0.0179):")
    print(f"     |beta - 1/4| = {abs(bhat-0.25):.4f}   ratio to floor = "
          f"{abs(bhat-0.25)/0.0179:.2f}   -> "
          f"{'BELOW' if abs(bhat-0.25) < 0.0179 else 'ABOVE'} the declared floor")
    print(f"     sampling sd of beta_hat = {bs.std():.4f}   -> the STATISTICAL error is now "
          f"{'BELOW' if bs.std() < 0.0179 else 'ABOVE'} the design floor")
    print("     NOTE: that floor was measured on the BOX leg (an exactly-known exponent")
    print("     returning 1.0179 instead of 1). The interval leg has no exactly-known")
    print("     calibrator of its own, so the floor is IMPORTED, not measured in situ.")


design_noise_null(d17)
```

## Apéndice B — salida íntegra

```text
################################################################################################
# PROVENANCE: the 17-seed run contains the 8-seed run, value for value
################################################################################################
  N=  2000  first 8 of 17 == historical 8: True   new 9 (seeds 109-117): [12, 13, 11, 12, 12, 12, 12, 12, 12]
  N=  8000  first 8 of 17 == historical 8: True   new 9 (seeds 109-117): [19, 19, 18, 19, 19, 17, 19, 18, 19]
  N= 16000  first 8 of 17 == historical 8: True   new 9 (seeds 109-117): [25, 22, 22, 23, 22, 23, 22, 22, 23]
  N= 32000  first 8 of 17 == historical 8: True   new 9 (seeds 109-117): [27, 28, 27, 27, 27, 26, 28, 27, 26]
  seeds 8-run : [101, 102, 103, 104, 105, 106, 107, 108]
  seeds 17-run: [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117]
  DESIGN_UNPERTURBED = True

================================================================================================
17-REPLICATE PRECISION LEG (primary): n_points=4  n_replicas=17  sd_pool=0.8880 (dof 64)  sem_L=0.2154
  seeds: 101..117  (17 seeds)
        N  mean L (R001)       sd  sem(pool)   y=L/N^(1/4)   sigma_y
     2000        14.2941   0.8489     0.2154       2.13747   0.03221
     8000        20.2941   0.6860     0.2154       2.14584   0.02277
    16000        24.6471   1.0572     0.2154       2.19147   0.01915
    32000        29.2941   0.9196     0.2154       2.19025   0.01610

================================================================================================
8-REPLICATE PRECISION LEG (historical, for contrast): n_points=4  n_replicas=8  sd_pool=0.9933 (dof 28)  sem_L=0.3512
  seeds: 101..108  (8 seeds)
        N  mean L (R001)       sd  sem(pool)   y=L/N^(1/4)   sigma_y
     2000        14.6250   1.0607     0.3512       2.18695   0.05251
     8000        20.0000   0.5345     0.3512       2.11474   0.03713
    16000        24.6250   1.1877     0.3512       2.18951   0.03122
    32000        29.6250   1.0607     0.3512       2.21499   0.02626

================================================================================================
SLOPES (R001 convention)
  17-seed: global d log<L>/d log N = 0.2600   local = [0.2528, 0.2804, 0.2492]
  8-seed: global d log<L>/d log N = 0.2552   local = [0.2258, 0.3001, 0.2667]
  design floor on a slope (R005): 0.0179  (the exactly-known exponent returns 1.0179)

================================================================================================
M0 CONSTANT FIT  y = m4   (R005 pooled error)
  17-seed precision    m4 = 2.1762 +/- 0.0103   chi2 = 4.6196 / 3 dof = 1.54   p = 0.2019   band: IN
  8-seed precision     m4 = 2.1844 +/- 0.0168   chi2 = 4.9051 / 3 dof = 1.64   p = 0.1789   band: IN
  base (3 seeds)       m4 = 2.1111 +/- 0.0262   chi2 = 4.1184 / 5 dof = 0.82   p = 0.5325   band: IN
  DIAGNOSTIC_ONLY (per-point sem, which R005 forbids):
    17-seed precision    chi2/dof = 1.79   m4 = 2.1702
    8-seed precision     chi2/dof = 3.26   m4 = 2.1572

================================================================================================
PER-POINT CONTRIBUTION TO THE M0 CHI2
  17-seed  (chi2 = 4.6196)
     N=  2000  (r/sigma)^2 =  1.446    31.3%   ties at this N: 17 replicas -> 4 distinct values
     N=  8000  (r/sigma)^2 =  1.776    38.4%   ties at this N: 17 replicas -> 3 distinct values
     N= 16000  (r/sigma)^2 =  0.636    13.8%   ties at this N: 17 replicas -> 4 distinct values
     N= 32000  (r/sigma)^2 =  0.762    16.5%   ties at this N: 17 replicas -> 4 distinct values
  8-seed  (chi2 = 4.9051)
     N=  2000  (r/sigma)^2 =  0.002     0.0%   ties at this N: 8 replicas -> 4 distinct values
     N=  8000  (r/sigma)^2 =  3.519    71.7%   ties at this N: 8 replicas -> 3 distinct values
     N= 16000  (r/sigma)^2 =  0.027     0.5%   ties at this N: 8 replicas -> 4 distinct values
     N= 32000  (r/sigma)^2 =  1.357    27.7%   ties at this N: 8 replicas -> 4 distinct values

================================================================================================
M5 DESCRIPTIVE FIT  L = A N^beta   and COMPARISON WITH beta = 1/4
  17-seed precision    A = 1.9687  beta = 0.2604   Dchi2<1 interval [0.2549, 0.2660]   chi2 = 1.1026   Dchi2 vs beta=1/4: 3.5171
                       beta - 1/4 = +0.0104   EXCLUDES 1/4 at Dchi2<1
  8-seed precision     A = 1.9564  beta = 0.2615   Dchi2<1 interval [0.2524, 0.2706]   chi2 = 3.3147   Dchi2 vs beta=1/4: 1.5904
                       beta - 1/4 = +0.0115   EXCLUDES 1/4 at Dchi2<1
  base (3 seeds)       A = 2.0147  beta = 0.2554   Dchi2<1 interval [0.2438, 0.2672]   chi2 = 3.9030   Dchi2 vs beta=1/4: 0.2154
                       beta - 1/4 = +0.0054   CONTAINS 1/4 at Dchi2<1
  (M0 is EXACTLY M5 with beta fixed at 1/4: same chi2 scale, verified below.)
     17-seed: chi2(M0) = 4.6196   chi2(M5|beta=1/4) = 4.6196   identical = True
     8-seed: chi2(M0) = 4.9051   chi2(M5|beta=1/4) = 4.9051   identical = True

================================================================================================
SEED BOOTSTRAP over the committed replicas (17-seed leg, 20000 resamples, seed 20260910)
  m4  : median 2.1762  CI68 [2.1683, 2.1841]  CI95 [2.1606, 2.1914]  P(in band) = 1.000
  beta: median 0.2605  CI68 [0.2560, 0.2650]  CI95 [0.2515, 0.2695]  P(beta > 1/4) = 0.986

================================================================================================
LEAVE-ONE-OUT of M0 and beta (17-seed leg)
    dropped     M0 m4   M0 chi2  dof      beta         A
       2000    2.1806    3.0103    2    0.2629    1.9212
       8000    2.1839    2.3898    2    0.2585    2.0103
      16000    2.1700    3.7262    2    0.2602    1.9674
      32000    2.1665    3.3352    2    0.2629    1.9268
  m4 range   2.1665 .. 2.1839   (span 0.0174, se = 0.0103)
  beta range 0.2585 .. 0.2629   (span 0.0044; contains 1/4: False)

================================================================================================
SECONDARY, NOT USED TO SELECT ANYTHING: fixed-alpha corrections from the same routine.
No free-alpha (M4) search was run. Reported only because it costs nothing.
     alpha        m4           c      chi2   Dchi2 vs M0
      0.25    2.2551     -0.3771    1.2064        3.4133
      0.50    2.2102     -1.6908    1.4180        3.2016
      1.00    2.1893    -55.9407    1.9640        2.6556

================================================================================================
DESIGN RESOLUTION with 17 replicas
  per-point relative uncertainty : 0.97%   (8-seed run: 1.58%)
  observed spread of y over sweep: +2.53%   (8-seed run: +4.74%)
  endpoint separation: +1.47 sigma (8-seed run: +0.48 sigma)
  pooled sd dof: 64  -> relative se of sd_pool = 8.8%  (8-seed: 13.4%)

================================================================================================
DESIGN-NOISE CALIBRATION (17-replicate geometry, constant truth)
  observed: chi2(M0) = 4.6196  chi2(M5) = 1.1027  Dchi2 = 3.5169  beta_hat = 0.2605
  null of Dchi2(M0->M5), 60000 draws, seed 20260910:
     P50  = 0.458
     P68  = 0.992
     P90  = 2.705
     P95  = 3.917
     P99  = 6.708
     observed 3.517 -> percentile 93.8   p(>=obs) = 0.0624

  beta_hat when the truth IS beta = 1/4 (same design): mean 0.2500  sd 0.0056
     central 95%: [0.2390, 0.2610]
     P(beta_hat >= 0.2605) = 0.0329   -> 1.89 sigma

  R005 comparison against the DESIGN FLOOR (0.0179):
     |beta - 1/4| = 0.0105   ratio to floor = 0.59   -> BELOW the declared floor
     sampling sd of beta_hat = 0.0056   -> the STATISTICAL error is now BELOW the design floor
     NOTE: that floor was measured on the BOX leg (an exactly-known exponent
     returning 1.0179 instead of 1). The interval leg has no exactly-known
     calibrator of its own, so the floor is IMPORTED, not measured in situ.
```
