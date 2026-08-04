# P1a — Resultados de representaciones alternativas en `d=2`

> **ESTADO: RESULTADO COMPUTACIONAL v1.0 · CONTRATO CUMPLIDO ·
> `INCONCLUSIVE_ALTERNATIVE_REPRESENTATIONS`.**
>
> `HEIGHT_WIDTH` queda fuertemente aparcada. `COUNT_VOLUME` mejora de forma clara la
> resolución de la altura, pero no alcanza el umbral para preregistrar un cociente y
> permanece como rama abierta.

## 1. Contrato y representaciones

Contrato previo:

```text
emergencia/P1a_contrato_representaciones_alternativas_d2.md
```

Sobre el mismo selector `MIN_COVERAGE_LEX` se compararon, en una cuarta muestra
independiente:

```text
HEIGHT_ONLY   = H/(2 sqrt(n))                     [benchmark no elegible]
COUNT_VOLUME  = sqrt((m-2)/(n-2))                [representacion nueva]
HEIGHT_WIDTH  = (H+W)/(4 sqrt(n))                [representacion nueva]
```

`W` es la anchura del intervalo, equivalente a una LDS en `d=2`. Ninguna fórmula
fue ajustada a los datos y no se calculó un cociente entre lados.

## 2. Integridad y reproducibilidad

La anchura coincide con enumeración ingenua de antichains para todas las
permutaciones hasta `n=6`. También se validaron cadenas, antichains, fórmulas,
selector, bootstrap, terminales y ausencia de ratios.

La batería específica completa de P1a da:

```text
59 passed
```

La regeneración completa en `/tmp/p1a_alt_rep_repro_20260803` produjo artefactos y
sidecars byte a byte idénticos:

```text
intervals_sha256 = 5110688b89142bf06e738a6f66bb41fa7c248e29352392b8bc763480ebd3ab08
metrics_sha256   = 4d98f014612af57212190a86e91f3445a111289cd55b66cca1adbde827e48cec
summary_sha256   = 7176a3a6e55cf309911a636592780880c55574773d398a9a620a1536ea7899dc
```

## 3. Muestra seleccionada

| `n` | Posets | Selecciones únicas | Intervalos |
|---:|---:|---:|---:|
| 64 | 12 000 | 7 014 | 14 028 |
| 96 | 12 000 | 7 918 | 15 836 |
| 128 | 12 000 | 8 334 | 16 668 |

Las tres representaciones se evaluaron sobre exactamente los mismos intervalos.

## 4. Benchmark de altura

La muestra nueva reproduce el fallo anterior:

| `n` | Lado | Correlación | Mediana error relativo |
|---:|---|---:|---:|
| 64 | pasado | 0.2658 | 0.1420 |
| 64 | futuro | 0.2686 | 0.1379 |
| 96 | pasado | 0.2359 | 0.1139 |
| 96 | futuro | 0.2345 | 0.1145 |
| 128 | pasado | 0.2600 | 0.1029 |
| 128 | futuro | 0.2396 | 0.1027 |

La repetición independiente descarta que el `PARK` anterior fuera una particularidad
de sus semillas.

## 5. `COUNT_VOLUME`

| `n` | Lado | Sesgo | Mediana error relativo | Correlación | Bootstrap 95 % correlación |
|---:|---|---:|---:|---:|---:|
| 64 | pasado | +0.0313 | 0.1116 | 0.5660 | [0.5502, 0.5824] |
| 64 | futuro | +0.0317 | 0.1110 | 0.5664 | [0.5497, 0.5815] |
| 96 | pasado | +0.0233 | 0.0822 | 0.5420 | [0.5268, 0.5568] |
| 96 | futuro | +0.0228 | 0.0836 | 0.5300 | [0.5141, 0.5453] |
| 128 | pasado | +0.0182 | 0.0696 | 0.5322 | [0.5168, 0.5473] |
| 128 | futuro | +0.0188 | 0.0695 | 0.5458 | [0.5299, 0.5612] |

Los seis intervalos de sesgo quedan dentro de `[-0.05,0.05]`, y los errores relativos
quedan muy por debajo del máximo `0.30`. La cardinalidad aproximadamente duplica la
correlación obtenida con altura.

Sin embargo, los límites inferiores de correlación están entre `0.51` y `0.55`, no
cerca del `0.80` requerido. Por ello:

```text
COUNT_VOLUME_QUALIFIES = FALSE
COUNT_VOLUME_STRONGLY_PARKED = FALSE
```

El resultado es genuinamente intermedio. La representación porta señal individual
moderada y mejora al benchmark, pero no tiene aún resolución suficiente para abrir
un cociente bajo el contrato actual.

El sesgo positivo observado no contradice la identidad de conteo para endpoints
fijados: el estimador aplica una raíz y los endpoints son elegidos por un selector
que usa precisamente las cardinalidades. No se atribuye el sesgo a un mecanismo
único sin una teoría condicionada por selección.

## 6. `HEIGHT_WIDTH`

| `n` | Lado | Sesgo | Mediana error relativo | Correlación | Bootstrap 95 % correlación |
|---:|---|---:|---:|---:|---:|
| 64 | pasado | -0.0392 | 0.1324 | 0.4658 | [0.4469, 0.4838] |
| 64 | futuro | -0.0394 | 0.1365 | 0.4561 | [0.4380, 0.4753] |
| 96 | pasado | -0.0457 | 0.1281 | 0.4023 | [0.3834, 0.4208] |
| 96 | futuro | -0.0467 | 0.1301 | 0.3944 | [0.3754, 0.4133] |
| 128 | pasado | -0.0493 | 0.1275 | 0.3737 | [0.3555, 0.3914] |
| 128 | futuro | -0.0483 | 0.1240 | 0.3908 | [0.3728, 0.4089] |

Añadir anchura mejora la correlación respecto de la altura sola en `n=64`, pero la
mejora disminuye al crecer `n`. Todos los límites superiores de correlación quedan
por debajo de `0.50`; además, un intervalo de sesgo cruza ligeramente el límite
`-0.05` en `n=128` pasado.

```text
HEIGHT_WIDTH_QUALIFIES = FALSE
HEIGHT_WIDTH_STRONGLY_PARKED = TRUE
```

Este terminal cierra la media no ajustada `(H+W)/(4 sqrt(n))`. No prueba que todo
perfil de cadenas y antichains sea inútil, pero impide promover esta fórmula concreta.

## 7. Terminal conjunto

La regla congelada seleccionaba una representación solo si superaba correlación
`0.80` en ambos lados y los tres tamaños. Ninguna lo consigue. El aparcamiento de
ambas exigía además que las dos incurrieran en fallo fuerte; `COUNT_VOLUME` no lo
hace.

```text
P1A_ALT_REP_TERMINAL = INCONCLUSIVE_ALTERNATIVE_REPRESENTATIONS
P1A_COUNT_VOLUME_STATUS = OPEN_BELOW_QUALIFICATION_THRESHOLD
P1A_HEIGHT_WIDTH_STATUS = PARKED
P1A_RATIO_COMPUTED = NO
P1A_RATIO_PREREGISTRATION = NOT_AUTHORIZED
```

## 8. Interpretación

La comparación localiza mejor el cuello de botella:

1. la altura sola pierde gran parte de la información individual;
2. una segunda estadística extremal, la anchura, no resuelve el problema;
3. la cardinalidad interna sí contiene bastante más información sobre duración;
4. pero el selector comprime la dispersión temporal y la fluctuación de conteo sigue
   impidiendo una resolución cercana a `0.80`.

La rama `COUNT_VOLUME` merece teoría adicional, no un cociente inmediato. El paso
natural sería construir la ley condicionada por selección

```text
P(ell | m,n, MIN_COVERAGE_LEX unique)
```

o una cota de resolución para demostrar si la correlación moderada es un efecto
finito corregible o una limitación inducida por el selector. Ajustar una regresión a
estos mismos datos y declarar victoria violaría el contrato.

También debe vigilarse la circularidad: `MIN_COVERAGE_LEX` selecciona usando `m`, de
modo que un futuro cociente basado en cardinalidades podría quedar parcialmente
predeterminado por la propia regla.

## 9. Artefactos

- `emergencia/resultados/p1a_representaciones_intervalos_d2.csv`
- `emergencia/resultados/p1a_representaciones_metricas_d2.csv`
- `emergencia/resultados/p1a_representaciones_resumen.json`
- sidecars `*.sha256`

```text
P1A_ALTERNATIVE_RESULT = COMPLETE_REPRODUCIBLE
P1A_COUNT_VOLUME_BRANCH = OPEN_THEORY_REQUIRED
P1A_HEIGHT_WIDTH_BRANCH = CLOSED_CURRENT_FORMULA
P1A_CURRENT_RATIO_GATE = CLOSED
P1A_METRIC_IDENTIFIABILITY = OPEN
P1A_NOVELTY_CERTIFIED = NO
```
