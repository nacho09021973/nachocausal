# P1a — Resultados de estabilidad y sesgo post-selección en `d=2`

> **ESTADO: RESULTADO COMPUTACIONAL v1.0 · CONTRATO CUMPLIDO ·
> `INCONCLUSIVE_STABILITY_GATE`.**
>
> El terminal es inconcluso en el sentido exacto del gate congelado. El experimento
> sí resuelve el diagnóstico: el selector es estable bajo thinning, pero concentra
> uno de los dos intervalos en el soporte mínimo. No se ha calculado una razón de
> alturas ni se ha abierto P1b métrico.

## 1. Contrato y ejecución

Contrato previo a resultados:

```text
emergencia/P1a_contrato_estabilidad_y_sesgo_d2.md
```

Instrumento:

```text
emergencia/p1a_estabilidad_d2.py
```

Ejecución primaria:

```text
PYTHONDONTWRITEBYTECODE=1 \
  python3 -m emergencia.p1a_estabilidad_d2
```

Entorno registrado:

```text
Python 3.12.3
NumPy 1.26.4
RNG numpy.random.Generator(numpy.random.PCG64)
```

Se ejecutaron 12 000 realizaciones para cada uno de cinco tamaños, dos thinnings
independientes por realización y 4 000 baselines por cada tamaño de intervalo
observado.

## 2. Controles de integridad

Las pruebas específicas de P1a, incluidas las del experimento anterior, dan:

```text
25 passed in 0.72s
```

Entre otros controles:

- el extractor de la cuádrupla coincide con una implementación ingenua y con el
  clasificador sellado para todas las permutaciones de `n=6,7`;
- el thinning preserva exactamente las comparabilidades del subposet inducido;
- las alturas y el baseline de tamaño tres satisfacen casos analíticos;
- las semillas reproducen una ejecución reducida;
- y los hashes y terminales generados están fijados por tests.

La supervivencia observada de los cuatro extremos superó los diez controles frente
a `p^4` con la tolerancia preespecificada:

```text
P1A_SURVIVAL_CONTROLS_PASS = TRUE
```

Una segunda ejecución completa en `/tmp/p1a_estabilidad_repro_20260803` produjo los
cuatro artefactos y sus sidecars byte a byte idénticos. Los cuatro sidecars SHA-256
se verificaron correctamente.

```text
stability_csv_sha256 = aea397394886f9eec161dc90fb02c4ed13f079f10bba433befe5768d60281448
thinning_csv_sha256  = 681e0fd0b05a447046092c8ce5e270075c9095f796f161a06fa69016a46ab842
baseline_csv_sha256  = 3c2807fb88d17186e71409db2d2e34bf61d03cb079b6d0e18591e90ffde21184
summary_sha256       = 6ec69648666bca250aa7cbca93a2b21e2fb1a7ddabec087eafd5d38df9967dbb
```

## 3. Disponibilidad del selector en la nueva muestra

| `n` | Selecciones únicas | `p_unique` | Wilson 95 % |
|---:|---:|---:|---:|
| 32 | 5 056 / 12 000 | 0.4213 | [0.4125, 0.4302] |
| 48 | 5 918 / 12 000 | 0.4932 | [0.4842, 0.5021] |
| 64 | 6 472 / 12 000 | 0.5393 | [0.5304, 0.5482] |
| 96 | 6 935 / 12 000 | 0.5779 | [0.5691, 0.5867] |
| 128 | 7 160 / 12 000 | 0.5967 | [0.5879, 0.6054] |

Esta cuadrícula independiente reproduce el patrón de disponibilidad anterior y lo
extiende hasta `n=128`. No prueba monotonía ni un límite asintótico.

## 4. Estabilidad bajo thinning

La tabla muestra la probabilidad de reseleccionar exactamente los mismos cuatro
elementos, condicionada a que los cuatro hayan sobrevivido.

| `n` | `p_same`, retención 0.90 | Wilson 95 % | `p_same`, retención 0.80 | Wilson 95 % |
|---:|---:|---:|---:|---:|
| 32 | 0.7469 | [0.7319, 0.7614] | 0.6177 | [0.5966, 0.6385] |
| 48 | 0.7678 | [0.7542, 0.7808] | 0.6445 | [0.6251, 0.6634] |
| 64 | 0.7783 | [0.7656, 0.7905] | 0.6486 | [0.6301, 0.6667] |
| 96 | 0.7951 | [0.7831, 0.8066] | 0.6670 | [0.6496, 0.6840] |
| 128 | 0.8028 | [0.7912, 0.8139] | 0.6969 | [0.6799, 0.7134] |

La estabilidad supera holgadamente los dos umbrales de paso en los tres tamaños del
gate. Esto es más fuerte que observar que el poset reducido aún tiene alguna salida
única: se exige identidad exacta de la cuádrupla original.

Sin condicionar por supervivencia, la reselección exacta con retención 0.90 va de
0.4915 a 0.5282. Esta caída es esperable porque la supervivencia de cuatro puntos
tiene probabilidad `0.9^4=0.6561`; no contradice la estabilidad condicional.

## 5. Degeneración de tamaños

| `n` | `p(m_min=3)` | Wilson 95 % | media `m_min` | balance medio |
|---:|---:|---:|---:|---:|
| 32 | 0.6845 | [0.6716, 0.6972] | 3.566 | 0.3479 |
| 48 | 0.7158 | [0.7042, 0.7271] | 3.539 | 0.1860 |
| 64 | 0.7434 | [0.7326, 0.7539] | 3.433 | 0.1160 |
| 96 | 0.7619 | [0.7518, 0.7718] | 3.336 | 0.0635 |
| 128 | 0.7782 | [0.7684, 0.7877] | 3.282 | 0.0426 |

La mediana de `m_min` es exactamente tres en todos los tamaños. Aunque los tamaños
medios de cada lado crecen, el balance medio cae de 0.348 a 0.043. El mecanismo es,
por tanto, un intervalo grande acompañado típicamente por otro clavado en el soporte
mínimo. La simetría aproximada entre las medias anterior y posterior indica que no es
una orientación temporal fija: cualquiera de los dos lados puede asumir el papel
pequeño.

Este diagnóstico responde a uno de los criterios de fallo escritos antes de la
simulación: el score de cobertura total admite mejorar un lado mientras deja el otro
en `k_0`.

## 6. Frontera latente

| `n` | Extremos cerca del borde | Referencia uniforme | Enriquecimiento | clearance medio |
|---:|---:|---:|---:|---:|
| 32 | 0.2918 | 0.1900 | 1.536 | 0.1468 |
| 48 | 0.3344 | 0.1900 | 1.760 | 0.1196 |
| 64 | 0.3772 | 0.1900 | 1.985 | 0.1003 |
| 96 | 0.4309 | 0.1900 | 2.268 | 0.0804 |
| 128 | 0.4721 | 0.1900 | 2.485 | 0.0691 |

Los extremos seleccionados aparecen progresivamente más cerca de la frontera del
cuadrado nulo latente. La comparación de referencia es con un punto uniforme
arbitrario; no separa el efecto de ser extremo causal del efecto adicional de
maximizar cobertura. Por eso este resultado es una alarma geométrica, no una medida
aislada del sesgo del selector.

Las coordenadas se consultaron solo después de la selección y no alteraron ninguna
salida.

## 7. Sesgo post-selección de alturas

| `n` | Residuo medio `H_selected-E[H_0(m)]` | error estándar descriptivo | pasado | futuro |
|---:|---:|---:|---:|---:|
| 32 | -0.2873 | 0.0057 | -0.2992 | -0.2754 |
| 48 | -0.2821 | 0.0065 | -0.2708 | -0.2933 |
| 64 | -0.2677 | 0.0073 | -0.2659 | -0.2694 |
| 96 | -0.2616 | 0.0082 | -0.2537 | -0.2695 |
| 128 | -0.2455 | 0.0088 | -0.2637 | -0.2273 |

Condicionado al mismo número de elementos, los intervalos seleccionados tienen en
promedio una altura algo menor que un intervalo bidimensional independiente no
seleccionado. Los errores estándar de la tabla describen la dispersión entre
intervalos seleccionados y no incorporan como una inferencia formal toda la
incertidumbre del baseline ni la dependencia entre los dos lados. No se emite un
test de significación.

El efecto es secundario frente a la degeneración: cuando `m=3`, que domina el lado
menor, la altura es exactamente tres y no existe resolución interna para una futura
medición fina.

## 8. Gate congelado

Los umbrales de estabilidad pasan para `n=64,96,128`, pero el límite superior de
`p_floor` está muy por encima del máximo de paso `0.25` en los tres casos. El
terminal fuerte de aparcamiento exigía que el límite inferior superara `0.75` en
todos los tamaños; esto ocurre en `n=96,128`, pero no en `n=64`.

Por tanto, sin reinterpretar reglas después de observar los datos:

```text
P1A_STABILITY_TERMINAL = INCONCLUSIVE_STABILITY_GATE
```

“Inconcluso” no significa que los dos efectos sean inciertos. Significa que el
patrón observado cae entre los dos terminales compuestos preespecificados:

- identidad del selector: favorable y estable;
- calidad del soporte de ambos intervalos: desfavorable y cerca del criterio fuerte
  de aparcamiento.

## 9. Decisión científica

No conviene ejecutar todavía el cociente provisional de alturas con `F_cov,3`. Una
ejecución produciría muchas razones en las que uno de los numeradores tiene altura
exactamente tres; cuantificar ese cociente no resolvería la representación defectuosa.

El siguiente paso recomendado dentro de `d=2` es volver a P1a y diseñar una familia
de scores order-only que penalice el colapso de `m_min` sin utilizar alturas ni fijar
directamente la razón buscada. Dos candidatos transparentes para una nueva puerta
teórica son:

```text
S_min(q)  = min(n_C(a,b), n_C(c,d)),
S_lex(q)  = (min(n_- ,n_+), n_-+n_+) en orden lexicográfico.
```

No se elige todavía ninguno: ambos cambian el target aleatorio, la frecuencia de
empate y la posible concentración en borde. Requieren un contrato nuevo y repetir
primero disponibilidad y estabilidad. El terminal actual no autoriza modificar
`F_cov,3` retroactivamente.

La comparación posterior se realizó en una muestra nueva bajo contrato independiente
y seleccionó `MIN_COVERAGE_LEX`. El resultado se encuentra en
`emergencia/P1a_resultados_comparacion_selectores_balanceados_d2.md`. Esta decisión
no altera el terminal histórico de este documento ni autoriza aún un cociente de
alturas.

## 10. Artefactos

- `emergencia/resultados/p1a_estabilidad_d2.csv`
- `emergencia/resultados/p1a_thinning_d2.csv`
- `emergencia/resultados/p1a_alturas_baseline_d2.csv`
- `emergencia/resultados/p1a_estabilidad_resumen.json`
- sidecars `*.sha256` en el mismo directorio

```text
P1A_STABILITY_RESULT_STATUS = COMPLETE_REPRODUCIBLE
P1A_POINT_IDENTITY_STABILITY = PASS
P1A_MINIMUM_SUPPORT_QUALITY = FAIL_PASS_THRESHOLD
P1A_METRIC_RATIO_EXECUTION = NOT_RECOMMENDED
P1A_METRIC_IDENTIFIABILITY = OPEN
P1A_NOVELTY_CERTIFIED = NO
```
