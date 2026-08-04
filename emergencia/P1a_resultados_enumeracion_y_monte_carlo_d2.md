# P1a — Resultados de enumeración exacta y Monte Carlo en `d=2`

> **ESTADO: RESULTADO COMPUTACIONAL v1.0 · CONTRATO CUMPLIDO ·
> `POINT_SELECTOR_OPERATIONALLY_VIABLE`.**
>
> Este resultado evalúa únicamente la frecuencia con la que el selector de
> cobertura produce un par único en posets producto bidimensionales. No evalúa una
> razón de cadenas, no demuestra correspondencia con tiempo propio y no se extiende
> a dimensiones superiores.

## 1. Contrato y ejecución

Contrato previo:

```text
emergencia/P1a_contrato_enumeracion_y_monte_carlo_d2.md
```

Instrumento:

```text
emergencia/p1a_enumeracion_simulacion.py
```

Ejecución primaria:

```text
PYTHONDONTWRITEBYTECODE=1 \
  python3 emergencia/p1a_enumeracion_simulacion.py
```

Entorno registrado:

```text
Python 3.12.3
NumPy 1.26.4
RNG numpy.random.Generator(numpy.random.PCG64)
```

Se enumeraron exactamente

```text
6! + 7! + 8! + 9! = 408960
```

permutaciones y se ejecutaron

```text
10 tamaños * 20000 replicas = 200000
```

réplicas Monte Carlo.

## 2. Controles de integridad

### Pruebas específicas

```text
13 passed in 0.31s
```

Incluyen:

- comparación exhaustiva entre el clasificador vectorizado y una implementación
  ingenua para las 720 permutaciones de `n=6`;
- control exacto `EMPTY=719`, `UNIQUE=1`, `TIE=0` para `n=6`;
- control RSK `EMPTY=5003` para `n=7`;
- equivalencia vacío–`LIS<6` para todas las permutaciones de `n=6`;
- reproducibilidad del RNG en un lote reducido;
- hashes, finales de línea y terminal del resumen generado.

La suite histórica completa del repositorio fue iniciada y no mostró fallos en los
bloques completados, pero se interrumpió por duración en una prueba preexistente sin
progreso. No se declara como `PASS`.

### Cruce exacto–Monte Carlo

Las seis categorías para cada `n=6,7,8,9` —24 comparaciones— cumplieron la tolerancia
congelada. Los estados de probabilidad exacta cero también produjeron cero
observaciones.

```text
P1A_CROSSCHECK_PASS = TRUE
```

### Regeneración

Una segunda ejecución completa en `/tmp/p1a_repro_20260803` produjo artefactos byte
a byte idénticos. Los sidecars SHA-256 verifican correctamente.

```text
exact_csv_sha256  = 650ce526e1e88626ce41d8e9925d5b19fbb94c143c63714c0e51ebd9fcafd224
mc_csv_sha256     = a760fb72b31cd4a783fa13c94b5426bc73ede00208f9609dd1e9d91cf79fa3e9
summary_sha256    = fa1c24ff46bb183f5c2d6b0e8cbe422ce2eae7e514ce3f81a2328fabba2f7073
```

## 3. Enumeración exacta

| `n` | Permutaciones | `p_empty` | `p_def` | `p_tie` |
|---:|---:|---:|---:|---:|
| 6 | 720 | 0.998611 | 0.001389 | 0.000000 |
| 7 | 5 040 | 0.992659 | 0.006349 | 0.000992 |
| 8 | 40 320 | 0.977902 | 0.016716 | 0.005382 |
| 9 | 362 880 | 0.950278 | 0.033278 | 0.016443 |

La enumeración confirma la fórmula analítica del vacío y muestra que la selección
única ya aumenta entre `n=6` y `n=9`. Estos tamaños siguen estando dominados por
`EMPTY`; no son el régimen operativo del selector.

## 4. Monte Carlo

| `n` | `p_empty` | `p_def` | `p_tie` |
|---:|---:|---:|---:|
| 6 | 0.99845 | 0.00155 | 0.00000 |
| 7 | 0.99360 | 0.00545 | 0.00095 |
| 8 | 0.97640 | 0.01740 | 0.00620 |
| 9 | 0.95260 | 0.03145 | 0.01595 |
| 12 | 0.77435 | 0.11175 | 0.11390 |
| 16 | 0.41110 | 0.22870 | 0.36020 |
| 24 | 0.03190 | 0.36250 | 0.60560 |
| 32 | 0.00050 | 0.41685 | 0.58265 |
| 48 | 0.00000 | 0.49580 | 0.50420 |
| 64 | 0.00000 | 0.52640 | 0.47360 |

Los ceros observados para `EMPTY` en `n=48,64` no son ceros teóricos. Con 20 000
réplicas, el límite superior Wilson bilateral del 95 % es aproximadamente
`1.92e-4`.

## 5. Gate congelado

| `n` | Selecciones únicas | `p_def` | Wilson 95 % |
|---:|---:|---:|---:|
| 32 | 8 337 / 20 000 | 0.41685 | [0.41003, 0.42370] |
| 48 | 9 916 / 20 000 | 0.49580 | [0.48887, 0.50273] |
| 64 | 10 528 / 20 000 | 0.52640 | [0.51948, 0.53331] |

Los tres límites inferiores superan ampliamente el umbral congelado `0.10`.

```text
P1A_TERMINAL = POINT_SELECTOR_OPERATIONALLY_VIABLE
```

“Operativamente viable” significa únicamente que la regla puntual no se abstiene
casi siempre en el régimen evaluado. En `n=64` selecciona un par único en alrededor
del 52.6 % de las realizaciones; todavía se abstiene por empate en alrededor del
47.4 %.

## 6. Anatomía de los empates

| `n` | Puente solo | Extremo pasado | Extremo futuro | Mixto |
|---:|---:|---:|---:|---:|
| 32 | 0.22930 | 0.08195 | 0.08155 | 0.18985 |
| 48 | 0.20400 | 0.08270 | 0.08170 | 0.13580 |
| 64 | 0.18940 | 0.08505 | 0.08765 | 0.11150 |

El empate de puente es el mecanismo individual más frecuente. La proximidad entre
los empates pasado y futuro funciona como control de la simetría temporal de la ley;
la enumeración exacta da conteos idénticos para ambas categorías en `n=7,8,9` y el
Monte Carlo solo muestra fluctuaciones pequeñas.

Condicionado a empate, el número medio de maximizadores disminuye de aproximadamente
`3.61` en `n=32` a `2.91` en `n=64`. El máximo observado fue 72, 36 y 26,
respectivamente. Estos máximos son diagnósticos de cola, no estimaciones estables de
un parámetro.

## 7. Interpretación permitida

El resultado elimina dos objeciones al selector:

1. `EMPTY` deja de dominar al crecer `n` en el régimen estudiado;
2. la unicidad no colapsa: supera el 40 % en los tres tamaños del gate y aumenta en
   la cuadrícula observada.

No elimina tres problemas posteriores:

1. casi la mitad de las realizaciones de `n=64` siguen produciendo una salida
   conjuntista;
2. seleccionar por cobertura puede sesgar la localización y las longitudes internas;
3. no se ha demostrado que `L_C(a,b)/L_C(c,d)` converja a una razón temporal latente.

No debe extrapolarse monotonicidad ni un límite asintótico a partir de diez tamaños
finitos. En particular, `p_def(64,2)>p_def(48,2)` es un resultado descriptivo del
contrato, no una prueba de convergencia.

## 8. Decisión siguiente

P1a no necesita reemplazar inmediatamente el selector. El siguiente gate debe
estudiar, antes de medir una razón temporal:

- estabilidad del par único bajo thinning order-only;
- localización respecto del borde, usada solo para evaluación y nunca para selección;
- distribución de los tamaños individuales condicionada a selección;
- y sesgo post-selección de las alturas.

La futura capa métrica deberá mantener:

```text
selection statistic = interval cardinality coverage
estimation statistic = chain height ratio
```

y tratar explícitamente la selección como parte del target aleatorio.

## 9. Artefactos

- `emergencia/resultados/p1a_enumeracion_exacta_d2.csv`
- `emergencia/resultados/p1a_monte_carlo_d2.csv`
- `emergencia/resultados/p1a_ejecucion_resumen.json`
- sidecars `*.sha256` en el mismo directorio

```text
P1A_RESULT_STATUS = COMPLETE_REPRODUCIBLE
P1A_POINT_SELECTOR_GATE = PASS_OPERATIONAL_AVAILABILITY_ONLY
P1A_METRIC_IDENTIFIABILITY = OPEN
P1A_NOVELTY_CERTIFIED = NO
```
