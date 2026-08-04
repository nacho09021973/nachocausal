# P1a — Resultados de comparación de selectores balanceados en `d=2`

> **ESTADO: RESULTADO COMPUTACIONAL v1.0 · CONTRATO CUMPLIDO ·
> `SELECT_MIN_COVERAGE_LEX_FOR_HEIGHT_BIAS_GATE`.**
>
> La comparación selecciona `MIN_COVERAGE_LEX` para el siguiente gate interno. La
> decisión no atribuye significado temporal a la regla y no autoriza todavía un
> cociente de alturas.

## 1. Contrato y ejecución

Contrato congelado antes de los nuevos resultados:

```text
emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md
```

Reglas comparadas sobre una muestra nueva y común:

```text
COVERAGE:
  maximiza m_minus+m_plus

MIN_ONLY:
  maximiza min(m_minus,m_plus)

MIN_COVERAGE_LEX:
  maximiza lexicográficamente
  (min(m_minus,m_plus),m_minus+m_plus)
```

Ejecución:

```text
PYTHONDONTWRITEBYTECODE=1 \
  python3 -m emergencia.p1a_comparar_selectores_d2
```

Se ejecutaron 60 000 posets base. En cada realización, los tres selectores recibieron
la misma permutación y las mismas máscaras de thinning.

## 2. Integridad y reproducibilidad

La implementación de los tres argmax coincide con una enumeración ingenua para todas
las permutaciones de `n=6,7`; `COVERAGE` coincide además con el clasificador sellado.
La batería específica completa de P1a da:

```text
35 passed in 1.38s
```

Los controles de supervivencia de extremos frente a `p^4` pasaron en todas las
combinaciones ejecutables:

```text
P1A_COMPARE_SURVIVAL_CONTROLS_PASS = TRUE
```

La regeneración completa en `/tmp/p1a_comparacion_repro_20260803` produjo los cuatro
artefactos y sidecars byte a byte idénticos.

```text
selector_csv_sha256 = fa8b5fe9989658ee8b4de7df14ab2c5bbb5cd1319a0de646142f769a9062e0bf
thinning_csv_sha256 = 7734986acc5661985a3c05f3c42e0dfd845ebfb031b172cd741e62f8cefa6fe0
paired_csv_sha256   = 65cdeaffc1c687e12ddfddda8eea9ddc3385048e161f7f9daa3317acae725bdb
summary_sha256      = 798282701e9bafc10af3d6a5899d52bb793b15829c6394215ab6ca25ebc515e7
```

## 3. Comparación primaria en el gate

### 3.1 Disponibilidad

| Selector | `p_unique(64)` | `p_unique(96)` | `p_unique(128)` |
|---|---:|---:|---:|
| `COVERAGE` | 0.5429 | 0.5813 | 0.6064 |
| `MIN_ONLY` | 0.2320 | 0.2571 | 0.2858 |
| `MIN_COVERAGE_LEX` | 0.5922 | 0.6528 | 0.6966 |

`MIN_ONLY` protege el soporte al precio de muchos empates. El segundo componente de
`MIN_COVERAGE_LEX` reduce esos empates sin volver al colapso de cobertura: su
disponibilidad supera incluso a `COVERAGE` en los tres tamaños.

### 3.2 Protección del intervalo menor

| Selector | Magnitud | `n=64` | `n=96` | `n=128` |
|---|---|---:|---:|---:|
| `COVERAGE` | `p_floor` | 0.7365 | 0.7616 | 0.7885 |
|  | mediana `m_min` | 3 | 3 | 3 |
|  | balance medio | 0.1166 | 0.0633 | 0.0426 |
| `MIN_ONLY` | `p_floor` | 0 | 0 | 0 |
|  | mediana `m_min` | 12 | 19 | 25 |
|  | balance medio | 0.9374 | 0.9458 | 0.9519 |
| `MIN_COVERAGE_LEX` | `p_floor` | 0 | 0 | 0 |
|  | mediana `m_min` | 11 | 18 | 24 |
|  | balance medio | 0.8475 | 0.8780 | 0.8964 |

Los dos scores nuevos eliminan todos los casos observados con `m_min=3`. Para el
lexicográfico, los límites superiores Wilson del 95 % son `5.40e-4`, `4.90e-4` y
`4.59e-4`. No se interpreta el cero observado como imposibilidad teórica.

`MIN_ONLY` produce el mejor balance, como cabe esperar por construcción. El
lexicográfico cede una parte limitada de ese balance a cambio de mucha más unicidad.

## 4. Estabilidad bajo thinning

### Retención `0.90`

| Selector | `n=64` | Wilson inferior | `n=96` | Wilson inferior | `n=128` | Wilson inferior |
|---|---:|---:|---:|---:|---:|---:|
| `COVERAGE` | 0.7667 | 0.7538 | 0.7913 | 0.7793 | 0.8136 | 0.8023 |
| `MIN_ONLY` | 0.5385 | 0.5157 | 0.5186 | 0.4969 | 0.5074 | 0.4869 |
| `MIN_COVERAGE_LEX` | 0.7052 | 0.6919 | 0.6738 | 0.6609 | 0.6662 | 0.6538 |

### Retención `0.80`

| Selector | `n=64` | Wilson inferior | `n=96` | Wilson inferior | `n=128` | Wilson inferior |
|---|---:|---:|---:|---:|---:|---:|
| `COVERAGE` | 0.6543 | 0.6359 | 0.6743 | 0.6570 | 0.6905 | 0.6737 |
| `MIN_ONLY` | 0.4028 | 0.3747 | 0.3923 | 0.3662 | 0.4044 | 0.3786 |
| `MIN_COVERAGE_LEX` | 0.5863 | 0.5683 | 0.5592 | 0.5421 | 0.5395 | 0.5227 |

`MIN_ONLY` supera disponibilidad, suelo y thinning `0.80`, pero no alcanza el límite
inferior `0.50` preespecificado para thinning `0.90` en `n=96,128`. La diferencia es
pequeña respecto del umbral, pero la regla se aplica sin reinterpretación post hoc.

`MIN_COVERAGE_LEX` supera los cuatro requisitos en todos los tamaños del gate.

## 5. Relación entre `MIN_ONLY` y el lexicográfico

En las cinco muestras se observa:

```text
MIN_ONLY unique
  => MIN_COVERAGE_LEX unique
  => misma cuadrupla.
```

Los conteos de coincidencia son exactamente `2138`, `2504`, `2784`, `3085` y `3429`.
Esto no es una regularidad accidental. Si `q` es el único maximizador de `S_min`,
todos los demás candidatos tienen un primer componente estrictamente menor; añadir
la cobertura como segundo componente no puede desplazarlo ni crear un empate.

Por tanto, el lexicográfico extiende de forma conservadora el dominio puntual de
`MIN_ONLY`: conserva todas sus selecciones únicas y resuelve una parte de sus empates
mediante un segundo criterio todavía order-only.

## 6. Separación respecto de `COVERAGE`

Condicionando a que `COVERAGE` y `MIN_COVERAGE_LEX` sean ambos únicos, seleccionan la
misma cuádrupla en:

| `n` | Coincidencias / ambos únicos | Fracción |
|---:|---:|---:|
| 32 | 719 / 3 110 | 0.2312 |
| 48 | 94 / 3 738 | 0.0251 |
| 64 | 16 / 4 319 | 0.0037 |
| 96 | 0 / 4 924 | 0 |
| 128 | 0 / 5 361 | 0 |

Los scores no son dos parametrizaciones del mismo observable seleccionado. En el
régimen alto inducen targets aleatorios esencialmente distintos en esta muestra.

## 7. Frontera latente

| Selector | Magnitud | `n=64` | `n=96` | `n=128` |
|---|---|---:|---:|---:|
| `COVERAGE` | cerca del borde | 0.3744 | 0.4278 | 0.4700 |
|  | clearance medio | 0.1011 | 0.0808 | 0.0693 |
| `MIN_ONLY` | cerca del borde | 0.3649 | 0.3999 | 0.4277 |
|  | clearance medio | 0.1984 | 0.2039 | 0.2077 |
| `MIN_COVERAGE_LEX` | cerca del borde | 0.3564 | 0.3932 | 0.4227 |
|  | clearance medio | 0.1981 | 0.2044 | 0.2080 |

Los selectores balanceados mantienen los extremos mucho más alejados del borde en
clearance medio que `COVERAGE`, aunque la fracción dentro de la banda `0.05` sigue
por encima de la referencia uniforme `0.19`. Este bloque continúa siendo diagnóstico
y no identifica por sí solo el efecto causal del score.

## 8. Terminal congelado

```text
MIN_ONLY_QUALIFIES = FALSE
MIN_COVERAGE_LEX_QUALIFIES = TRUE
P1A_COMPARE_TERMINAL = SELECT_MIN_COVERAGE_LEX_FOR_HEIGHT_BIAS_GATE
P1A_SELECTED_CANDIDATE = MIN_COVERAGE_LEX
```

La elección significa únicamente que `MIN_COVERAGE_LEX` ofrece, en esta cuadrícula
bidimensional, una combinación preespecificada aceptable de disponibilidad,
estabilidad y soporte bilateral.

## 9. Próximo gate permitido

El paso siguiente puede estudiar para `MIN_COVERAGE_LEX`:

1. sesgo de altura condicionado por cada tamaño individual;
2. resolución y fluctuación de las dos alturas cuando `m_min` crece;
3. estabilidad de los endpoints y del target latente bajo thinning;
4. relación entre duración latente y altura para cada intervalo por separado.

Solo después de esas comprobaciones debería congelarse, si procede, un cociente de
alturas. La presente ejecución no lo calcula ni lo valida.

## 10. Artefactos

- `emergencia/resultados/p1a_comparacion_selectores_d2.csv`
- `emergencia/resultados/p1a_comparacion_thinning_d2.csv`
- `emergencia/resultados/p1a_comparacion_pareada_selectores_d2.csv`
- `emergencia/resultados/p1a_comparacion_selectores_resumen.json`
- sidecars `*.sha256`

```text
P1A_BALANCED_SELECTOR_RESULT = COMPLETE_REPRODUCIBLE
P1A_BALANCED_SELECTOR_CHOICE = MIN_COVERAGE_LEX
P1A_HEIGHT_BIAS_GATE = AUTHORIZED_TO_DESIGN_NOT_EXECUTED
P1A_HEIGHT_RATIO_EXECUTION = NOT_AUTHORIZED
P1A_METRIC_IDENTIFIABILITY = OPEN
P1A_NOVELTY_CERTIFIED = NO
```

El gate posterior autorizado se completó en
`emergencia/P1a_resultados_gate_altura_duracion_lex_d2.md`. Su terminal fue
`PARK_LEX_HEIGHT_REPRESENTATION`: la escala media es razonable, pero la altura no
resuelve la variación individual de duración dentro del target seleccionado. Este
resultado no modifica la elección comparativa histórica; cierra su promoción directa
a un cociente de alturas.
