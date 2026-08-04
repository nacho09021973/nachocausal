# P1a — Contrato de enumeración exacta y Monte Carlo en `d=2`

> **ESTADO: CONTRATO CONGELADO v1.0 · EJECUCIÓN AUTORIZADA POR EL USUARIO ·
> TARGET MÉTRICO FUERA DE ALCANCE.**
>
> Este documento se fija antes de observar los resultados. Autoriza dos ejecuciones
> sobre el selector `F_cov,3`: enumeración exacta de permutaciones y Monte Carlo de
> permutaciones uniformes. No autoriza modificar el selector, estudiar cocientes de
> cadenas, ejecutar dimensiones superiores ni interpretar correspondencia métrica.

## 1. Pregunta

Estimar o calcular exactamente, según el régimen,

```text
p_empty(n,2),
p_def(n,2),
p_tie(n,2),
```

y descomponer `p_tie` en:

```text
TIE_BRIDGE_ONLY,
TIE_PAST_ENDPOINT,
TIE_FUTURE_ENDPOINT,
TIE_MIXED.
```

La unidad de muestreo es una permutación uniforme `pi in S_n`, equivalente al poset
inducido por un sprinkling condicionado a `N=n` en un diamante de Minkowski `1+1`.

## 2. Instrumento congelado

```text
k_0 = 3
candidate = (a,b,c,d) con a prec b prec c prec d
minimum_support = |[a,b]|>=3 y |[c,d]|>=3
score = |[a,b]| + |[c,d]|
point_output = unique maximizer or abstain
set_output = all maximizers
```

No hay score secundario ni desempate por etiqueta.

## 3. Enumeración exacta

```text
EXACT_N = (6,7,8,9)
EXACT_SAMPLE = todas las n! permutaciones, una vez cada una
EXACT_WEIGHT = 1/n!
```

Para cada `n` deben satisfacerse:

```text
sum_state count(state,n) = n!,
count_empty + count_unique + count_tie = n!,
sum_tie_subtypes count = count_tie.
```

Controles analíticos obligatorios:

```text
n=6:
  empty=719, unique=1, tie=0;

n=7:
  empty=5003.
```

Una discrepancia produce `IMPLEMENTATION_INVALID` y bloquea toda interpretación.

## 4. Monte Carlo

```text
MC_N = (6,7,8,9,12,16,24,32,48,64)
MC_REPLICATES_PER_N = 20000
MC_BATCHES = 8
MC_REPLICATES_PER_BATCH = 2500
RNG = numpy.random.Generator(numpy.random.PCG64)
SEED_BASE = 2608030000
SEED(n,batch) = SEED_BASE + 100*n + batch
batch = 0,...,7
```

Cada lote genera exactamente 2500 permutaciones mediante `Generator.permutation(n)`.
No hay parada temprana ni adaptación del presupuesto a resultados intermedios.

Se reportarán intervalos Wilson bilaterales del 95 % por categoría. Son intervalos
descriptivos marginales; no se usarán como una familia de tests simultáneos.

## 5. Validación cruzada exacto–Monte Carlo

Para `n=6,7,8,9` y cada una de las seis categorías mutuamente excluyentes, se exige:

```text
|p_hat_MC - p_exact|
  <= 6 sqrt(p_exact(1-p_exact)/R) + 1/R,

R = 20000.
```

Si `p_exact=0`, la simulación debe observar exactamente cero casos: los estados
estructuralmente imposibles no se toleran como fluctuación.

Cualquier fallo produce `MC_EXACT_CROSSCHECK_FAILED` y bloquea el gate científico.

## 6. Diagnósticos secundarios congelados

Por cada `n` y método se registrarán además:

- media del número de maximizadores condicionada a `TIE`;
- máximo número de maximizadores observado;
- media de `S_cov/n` condicionada a candidato no vacío;
- número de puentes maximizadores;
- presencia de empate de extremo pasado y futuro.

Estos diagnósticos explican la degeneración; no cambian la clasificación primaria.

## 7. Gate del selector puntual

El gate usa exclusivamente `p_def` Monte Carlo en

```text
GATE_N = (32,48,64).
```

Tras superar todos los controles de implementación:

```text
si Wilson95_lower(p_def(n,2)) >= 0.10 para todo n en GATE_N:
  terminal = POINT_SELECTOR_OPERATIONALLY_VIABLE

si Wilson95_upper(p_def(n,2)) < 0.01 para todo n en GATE_N:
  terminal = POINT_SELECTOR_PARK_SET_VALUED_ONLY

en otro caso:
  terminal = POINT_SELECTOR_VIABILITY_INCONCLUSIVE
```

Los umbrales son operacionales, no físicos. `PARK_SET_VALUED_ONLY` no refuta P1 ni
el uso del conjunto completo `G_cov,3`.

## 8. Artefactos

```text
emergencia/p1a_enumeracion_simulacion.py
tests/test_p1a_enumeracion_simulacion.py
emergencia/resultados/p1a_enumeracion_exacta_d2.csv
emergencia/resultados/p1a_monte_carlo_d2.csv
emergencia/resultados/p1a_ejecucion_resumen.json
emergencia/resultados/*.sha256
emergencia/P1a_resultados_enumeracion_y_monte_carlo_d2.md
```

Los CSV usarán LF y un formato largo con una fila por `(method,n,state)`. Los
artefactos se escribirán de forma atómica y el ejecutor rechazará sobrescribirlos sin
una opción explícita.

## 9. Terminales de integridad

```text
IMPLEMENTATION_INVALID
MC_EXACT_CROSSCHECK_FAILED
POINT_SELECTOR_OPERATIONALLY_VIABLE
POINT_SELECTOR_PARK_SET_VALUED_ONLY
POINT_SELECTOR_VIABILITY_INCONCLUSIVE
```

La prioridad es fail-closed: los dos primeros terminales impiden emitir cualquiera
de los tres terminales científicos.

## 10. Techo de afirmación

La ejecución puede informar únicamente sobre frecuencia de definición y mecanismos
de empate del selector en posets producto bidimensionales a los tamaños congelados.
No puede sostener:

- que una razón de cadenas estime tiempo propio;
- que el selector sea viable en `d>=3`;
- que la selección sea estable bajo perturbaciones;
- que exista identificabilidad métrica;
- ni que el resultado tenga novedad certificada.

```text
P1A_EXECUTION_AUTHORIZED = YES
P1A_EXACT_ENUMERATION_AUTHORIZED = YES
P1A_MONTE_CARLO_D2_AUTHORIZED = YES
P1A_METRIC_RATIO_AUTHORIZED = NO
P1A_HIGHER_DIMENSIONS_AUTHORIZED = NO
P1A_CONTRACT_STATUS = FROZEN_BEFORE_RESULTS
```
