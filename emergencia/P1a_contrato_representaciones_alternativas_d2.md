# P1a — Contrato de representaciones alternativas de duración en `d=2`

> **ESTADO: CONTRATO CONGELADO v1.0 · MUESTRA INDEPENDIENTE · DOS
> REPRESENTACIONES NUEVAS · NINGÚN COCIENTE AUTORIZADO.**
>
> El gate anterior aparcó `H/(2 sqrt(n))` por falta de resolución individual dentro
> del target seleccionado. Este contrato mantiene `MIN_COVERAGE_LEX` y cambia solo la
> representación de cada intervalo, para localizar el origen del fallo.

## 1. Representaciones

### R1 — `COUNT_VOLUME`

Para un intervalo seleccionado de cardinalidad total `m` dentro de un poset con
`N=n`:

```text
A_hat_count = (m-2)/(n-2),
ell_hat_count = sqrt(A_hat_count).
```

Los dos extremos se restan porque, para endpoints fijados antes de observar los
otros puntos, el número de puntos interiores tiene esperanza `(n-2) A`, con
`A=Delta u Delta v`. La selección hace que esa identidad no sea una garantía de
insesgadez; precisamente se comprobará fuera de muestra.

Esta representación usa orden y número. No usa cadenas.

### R2 — `HEIGHT_WIDTH`

Sea

```text
H(I) = cardinalidad de una cadena maxima en I,
W(I) = cardinalidad de una antichain maxima en I.
```

En un poset producto bidimensional, `H` es una LIS y `W` una LDS. Ambas escalas son
asintóticamente del orden `2 sqrt(n A)`. Se congela sin ajuste:

```text
ell_hat_hw = (H+W)/(4 sqrt(n)).
```

Esta representación usa un perfil order-only más rico que la altura. No usa
coordenadas ni coeficientes aprendidos.

### Benchmark — `HEIGHT_ONLY`

Se repite únicamente como control contemporáneo:

```text
ell_hat_h = H/(2 sqrt(n)).
```

`HEIGHT_ONLY` no puede ser elegido porque su representación ya fue aparcada.

## 2. Selector, canal y target

El selector permanece congelado:

```text
MIN_COVERAGE_LEX:
  maximiza (min(m_minus,m_plus),m_minus+m_plus)
  en orden lexicografico;
  unique or abstain.
```

La ley y convención geométrica son:

```text
(u_i,v_i) iid Uniform([0,1]^2), condicionado a N=n,
x_i prec x_j iff u_i<u_j y v_i<v_j,
ds^2=du dv,
ell(x,y)=sqrt((u_y-u_x)(v_y-v_x)).
```

Las tres representaciones reciben solo invariantes del poset y `n`. Las coordenadas
se usan después para evaluación. Los dos lados se analizan por separado.

No se extrapola este canal fijo `N=n` a densidad Poisson física.

## 3. Muestra y semillas

Se usa una cuarta muestra independiente:

```text
BASE_N = (64,96,128)
BASE_REPLICATES_PER_N = 12000
BASE_BATCHES = 8
BASE_REPLICATES_PER_BATCH = 1500
RNG = numpy.random.Generator(numpy.random.PCG64)

COORDINATE_SEED_BASE = 2608044000
COORDINATE_SEED(n,batch) = COORDINATE_SEED_BASE + 100*n + batch

BOOTSTRAP_SEED_BASE = 2608045000
BOOTSTRAP_SEED(representation,n,side)
  = BOOTSTRAP_SEED_BASE
    + 1000*representation_code
    + 100*n
    + side_code

representation_code:
  HEIGHT_ONLY=0,
  COUNT_VOLUME=1,
  HEIGHT_WIDTH=2.

side_code(PAST)=0,
side_code(FUTURE)=1.

BOOTSTRAP_REPLICATES = 1000
```

No hay stopping ni reajuste de fórmulas.

## 4. Magnitudes

Por cada `(representation,n,side)` se reportan:

- sesgo medio `ell_hat-ell`;
- MAE y RMSE;
- mediana del error relativo absoluto;
- correlación Pearson entre `ell_hat` y `ell`;
- pendiente e intercepto OLS descriptivos;
- desviación estándar y coeficiente de variación de `ell_hat`.

Se generan intervalos bootstrap percentiles del 95 % para:

```text
sesgo medio,
mediana del error relativo absoluto,
correlacion Pearson.
```

El remuestreo se realiza dentro de `(representation,n,side)` sobre realizaciones
seleccionadas. No se interpreta independencia entre lados.

## 5. Gate común

Una representación nueva cualifica solo si para `n=64,96,128` y ambos lados:

```text
bootstrap95(sesgo medio) contenido en [-0.05,0.05],
bootstrap95_upper(mediana error relativo absoluto) <= 0.30,
bootstrap95_lower(correlacion Pearson) >= 0.80.
```

Se conserva el umbral de resolución del gate anterior; no se relaja después de
observar el fallo de `HEIGHT_ONLY`.

Una representación queda fuertemente aparcada si para todo `n` al menos un lado
cumple:

```text
bootstrap95_upper(correlacion) < 0.50,
o bootstrap95_lower(mediana error relativo absoluto) > 0.50.
```

Decisión congelada:

```text
si COUNT_VOLUME cualifica:
  SELECT_COUNT_VOLUME_FOR_RATIO_PREREGISTRATION

si COUNT_VOLUME no cualifica y HEIGHT_WIDTH cualifica:
  SELECT_HEIGHT_WIDTH_FOR_RATIO_PREREGISTRATION

si ninguna cualifica y ambas quedan fuertemente aparcadas:
  PARK_BOTH_ALTERNATIVE_REPRESENTATIONS

en otro caso:
  INCONCLUSIVE_ALTERNATIVE_REPRESENTATIONS
```

La prioridad de `COUNT_VOLUME` se fija por parsimonia y por su vínculo analítico con
volumen. Un terminal `SELECT` autorizaría preregistrar, no ejecutar, un cociente.

## 6. Controles obligatorios

- `COUNT_VOLUME` debe reproducir casos algebraicos exactos;
- `W` debe coincidir con una enumeración ingenua de antichains en posets pequeños;
- `W=1` para una cadena y `W=m` para una antichain;
- `HEIGHT_WIDTH` debe usar exactamente `(H+W)/(4 sqrt(n))`;
- el selector debe coincidir con la implementación sellada;
- las tres representaciones deben usar exactamente la misma muestra;
- bootstrap reproducible y correlaciones en `[-1,1]`;
- ningún campo ni artefacto debe contener un cociente pasado/futuro.

Un fallo produce `IMPLEMENTATION_INVALID`.

## 7. Artefactos

```text
emergencia/p1a_representaciones_alternativas_d2.py
tests/test_p1a_representaciones_alternativas_d2.py
emergencia/resultados/p1a_representaciones_intervalos_d2.csv
emergencia/resultados/p1a_representaciones_metricas_d2.csv
emergencia/resultados/p1a_representaciones_resumen.json
emergencia/resultados/*.sha256
emergencia/P1a_resultados_representaciones_alternativas_d2.md
```

CSV con LF, escritura atómica, rechazo de sobrescritura y regeneración byte a byte.

## 8. Techo de afirmación

La comparación puede determinar si alguna representación merece un contrato de
razón dentro de esta familia. No demuestra:

- identificabilidad métrica general;
- que cardinalidad o anchura sean suficientes fuera de `d=2`;
- ausencia de circularidad de un futuro cociente;
- consistencia asintótica bajo selección;
- escala temporal absoluta;
- ni novedad certificada.

```text
P1A_ALTERNATIVE_REPRESENTATIONS_EXECUTION_AUTHORIZED = YES
P1A_FIXED_N_CHANNEL = YES
P1A_DIMENSION = 2
P1A_RATIO_COMPUTED = NO
P1A_HIGHER_DIMENSIONS_AUTHORIZED = NO
P1A_ALTERNATIVE_CONTRACT_STATUS = FROZEN_BEFORE_RESULTS
```
