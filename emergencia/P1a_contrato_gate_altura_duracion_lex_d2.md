# P1a — Contrato del gate altura–duración para `MIN_COVERAGE_LEX` en `d=2`

> **ESTADO: CONTRATO CONGELADO v1.0 · MUESTRA INDEPENDIENTE · EJECUCIÓN
> AUTORIZADA · COCIENTE DE ALTURAS NO AUTORIZADO.**
>
> Este gate se fija después de seleccionar `MIN_COVERAGE_LEX`, pero antes de observar
> alturas o duraciones latentes bajo esa regla en una muestra nueva. Estudia los dos
> intervalos por separado. No calcula `H_minus/H_plus` ni
> `ell_minus/ell_plus`.

## 1. Pregunta

Determinar si cada intervalo seleccionado por `MIN_COVERAGE_LEX` posee, en la familia
bidimensional mínima, soporte y calibración suficientes para justificar el diseño
posterior de un estimador de razón temporal.

Se evaluarán cuatro propiedades:

1. sesgo de altura a cardinalidad de intervalo fija;
2. resolución de una calibración asintótica de altura;
3. asociación entre altura y duración latente para cada lado por separado;
4. estabilidad del par de duraciones latentes bajo thinning.

## 2. Canal y convención geométrica

La observación sigue siendo el poset condicionado a `N=n` generado por

```text
(u_i,v_i) iid Uniform([0,1]^2),
x_i prec x_j iff u_i<u_j y v_i<v_j.
```

Se fija la convención nula normalizada

```text
ds^2 = du dv,
ell(x,y) = sqrt((u_y-u_x)(v_y-v_x)).
```

`ell` es una duración adimensional dentro del cuadrado normalizado. No es una escala
física absoluta. Multiplicar la métrica por una constante cambiaría simultáneamente
esta convención y su constante de calibración.

El selector recibe solo la permutación de rangos. Las coordenadas se consultan
después de seleccionar.

Este contrato pertenece al canal fijo `N=n`. No debe reinterpretarse como un
sprinkling Poisson de densidad física fija.

## 3. Selector congelado

Se usa exclusivamente:

```text
MIN_COVERAGE_LEX:
  maximiza lexicográficamente
  (min(m_minus,m_plus),m_minus+m_plus)

k_0=3,
unique maximizer or abstain.
```

La implementación debe coincidir con
`p1a_comparar_selectores_d2.evaluate_selectors`. No se modifica el score usando
alturas o coordenadas.

## 4. Muestra, semillas y presupuesto

Se usa una tercera muestra, independiente de las ejecuciones anteriores:

```text
BASE_N = (64,96,128)
BASE_REPLICATES_PER_N = 12000
BASE_BATCHES = 8
BASE_REPLICATES_PER_BATCH = 1500
RETENTION = (0.90,0.80)
RNG = numpy.random.Generator(numpy.random.PCG64)

COORDINATE_SEED_BASE = 2608040000
COORDINATE_SEED(n,batch) = COORDINATE_SEED_BASE + 100*n + batch

THINNING_SEED_BASE = 2608041000
THINNING_SEED(n,batch) = THINNING_SEED_BASE + 100*n + batch

BASELINE_SEED_BASE = 2608042000
BASELINE_SEED(m) = BASELINE_SEED_BASE + m
BASELINE_REPLICATES_PER_SIZE = 4000

BOOTSTRAP_SEED_BASE = 2608043000
BOOTSTRAP_SEED(n,side) = BOOTSTRAP_SEED_BASE + 100*n + side_code
side_code(PAST)=0, side_code(FUTURE)=1
BOOTSTRAP_REPLICATES = 1000
```

No hay parada temprana ni adaptación a resultados intermedios.

## 5. Altura y baseline condicionado por tamaño

Para cada intervalo seleccionado `I=[x,y]` se registran:

```text
m(I)=|I|,
H(I)=longitud de la cadena mas larga, incluidos los extremos.
```

El baseline no seleccionado de tamaño total `m` es

```text
H_0(m)=2+LIS(Pi_(m-2)),
Pi_(m-2) uniforme en S_(m-2).
```

Con 4000 réplicas por cada tamaño observado se estima

```text
mu_0(m)=E[H_0(m)],
B_H(I)=H(I)-mu_0(m(I)).
```

El bootstrap de `B_H` trata `mu_0(m)` como tabla independiente ya estimada; su error
Monte Carlo se reporta por separado y no queda absorbido en el intervalo bootstrap.

## 6. Calibración de duración individual

La ley clásica de LIS en dos dimensiones motiva, sin convertirla todavía en un
teorema finito para el selector,

```text
ell_hat_H(I) = H(I)/(2 sqrt(n)).
```

Por cada `(n,side)` se reportan:

- sesgo medio `ell_hat_H-ell`;
- MAE y RMSE;
- mediana del error relativo absoluto
  `|ell_hat_H-ell|/ell`;
- correlación de Pearson entre `ell_hat_H` y `ell`;
- pendiente e intercepto OLS descriptivos de `ell_hat_H` sobre `ell`.

No se reajusta la constante `2` a los datos y no se usa una calibración aprendida.

Se generan intervalos bootstrap percentiles del 95 % para:

```text
media B_H,
mediana del error relativo absoluto,
correlacion de Pearson.
```

El remuestreo se realiza dentro de cada `(n,side)` sobre realizaciones seleccionadas.
Los intervalos de los dos lados no se presentan como independientes.

## 7. Estabilidad del target latente bajo thinning

Para cada retención se comparan las duraciones siempre que tanto el poset base como
el inducido produzcan una salida única, incluso si cambian los endpoints. Tras mapear
los endpoints reducidos a los puntos originales se define

```text
D_ell = max(
  |log(ell_minus_thin/ell_minus_base)|,
  |log(ell_plus_thin/ell_plus_base)|
).
```

El evento primario es

```text
TARGET_WITHIN_25_PERCENT = 1{D_ell <= log(1.25)}.
```

Se reportan su proporción y Wilson 95 %, la mediana de `D_ell`, la proporción dentro
de un factor `1.50` y la frecuencia de reselección exacta. Condicionar a unicidad en
ambos posets forma parte explícita del estimando.

## 8. Gate congelado

El selector pasa a preregistrar —no ejecutar— una razón de alturas solo si, para cada
`n` en `(64,96,128)` y para `PAST` y `FUTURE`:

```text
bootstrap95(media B_H) contenido en [-0.50,0.50],
bootstrap95_lower(cor(ell_hat_H,ell)) >= 0.80,
bootstrap95_upper(mediana error relativo absoluto) <= 0.30,
```

y, para cada `n`:

```text
Wilson95_lower(P(TARGET_WITHIN_25_PERCENT | p=0.90)) >= 0.50,
Wilson95_lower(P(TARGET_WITHIN_25_PERCENT | p=0.80)) >= 0.35.
```

Terminales:

```text
si se cumplen todas las condiciones:
  PASS_LEX_TO_PREREGISTER_HEIGHT_RATIO_D2

si, para todo n, algun lado cumple una de estas condiciones fuertes:
  bootstrap95_upper(correlacion) < 0.50,
  bootstrap95_lower(mediana error relativo absoluto) > 0.50:
    PARK_LEX_HEIGHT_REPRESENTATION

en otro caso:
  INCONCLUSIVE_LEX_HEIGHT_GATE
```

Los umbrales son operacionales. Un fallo cierra esta representación o exige más
teoría; no refuta la identificabilidad temporal desde orden y número.

## 9. Controles de implementación

Antes de la ejecución completa se exige:

- coincidencia del selector con el artefacto comparativo sellado;
- casos analíticos de altura y duración;
- baseline exacto `H_0(3)=3`;
- identidad `ell_hat_H=H/(2 sqrt(n))`;
- thinning preservando comparabilidades y coordenadas mapeadas;
- bootstrap reproducible y correlación acotada en `[-1,1]`;
- particiones y denominadores consistentes.

Cualquier fallo produce `IMPLEMENTATION_INVALID` y bloquea el terminal científico.

## 10. Artefactos

```text
emergencia/p1a_gate_altura_duracion_lex_d2.py
tests/test_p1a_gate_altura_duracion_lex_d2.py
emergencia/resultados/p1a_lex_intervalos_d2.csv
emergencia/resultados/p1a_lex_altura_calibracion_d2.csv
emergencia/resultados/p1a_lex_altura_baseline_por_tamano_d2.csv
emergencia/resultados/p1a_lex_target_thinning_d2.csv
emergencia/resultados/p1a_lex_altura_duracion_resumen.json
emergencia/resultados/*.sha256
emergencia/P1a_resultados_gate_altura_duracion_lex_d2.md
```

CSV con LF, escritura atómica, rechazo de sobrescritura y regeneración byte a byte.

## 11. Techo de afirmación

Un `PASS` autoriza únicamente redactar un contrato posterior para una razón. No
demuestra:

- identificabilidad métrica general;
- consistencia asintótica del selector aleatorio;
- ausencia de sesgo en un cociente;
- independencia entre intervalos;
- escala temporal absoluta;
- validez en `d>=3`;
- ni novedad certificada.

```text
P1A_LEX_HEIGHT_GATE_EXECUTION_AUTHORIZED = YES
P1A_DIMENSION = 2
P1A_FIXED_N_CHANNEL = YES
P1A_HEIGHT_RATIO_COMPUTED = NO
P1A_HIGHER_DIMENSIONS_AUTHORIZED = NO
P1A_LEX_HEIGHT_CONTRACT_STATUS = FROZEN_BEFORE_RESULTS
```
