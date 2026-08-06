# P1a — Resultados del gate altura–duración para `MIN_COVERAGE_LEX` en `d=2`

> **ESTADO: RESULTADO COMPUTACIONAL v1.0 · CONTRATO CUMPLIDO ·
> `PARK_LEX_HEIGHT_REPRESENTATION`.**
>
> La altura está bien calibrada en promedio, pero no resuelve la variación individual
> de duración entre los intervalos seleccionados. El cociente de alturas no fue
> calculado y no queda autorizado.

## 1. Contrato y ejecución

Contrato previo:

```text
emergencia/P1a_contrato_gate_altura_duracion_lex_d2.md
```

Se ejecutó una tercera muestra independiente:

```text
BASE_N = (64,96,128)
12000 realizaciones por n
selector = MIN_COVERAGE_LEX
canal = condicionado a N=n
duracion latente = sqrt(Delta u Delta v)
estimador de altura = H/(2 sqrt(n))
```

La regla de selección recibió únicamente el orden. Coordenadas, alturas y duración
se consultaron después de obtener una salida única.

## 2. Integridad y reproducibilidad

La batería específica completa de P1a da:

```text
47 passed
```

Incluye controles analíticos de duración nula, constante de calibración no ajustada,
baseline `H_0(3)=3`, correlación, bootstrap, selector congelado, terminales sintéticos,
hashes y ausencia explícita del cociente.

La regeneración completa en `/tmp/p1a_lex_height_repro_20260803` produjo cinco
artefactos y sidecars byte a byte idénticos:

```text
intervals_sha256   = 4db6001ceba4716696bc4ac63e36452863675408fd88a632b65a2d561dce85ba
calibration_sha256 = bb1e38d8c99fdcbfae8aed329aad3c7d19f130058f600b45e0bc7e6f5aaee018
baseline_sha256    = bf41a0ba47462994b47889606e3e82c7611748fc00eef13509b993d099738f56
thinning_sha256    = f7062580b90224ac2e0c936fb38b066fbead907f5ac6b11202c2b8b5aeb65ae5
summary_sha256     = 395d3aba30948cfc0211aa752cac5836a4731494f306a0e87a7e1651b12fa49d
```

## 3. Muestra seleccionada

| `n` | Posets | Selecciones únicas | Intervalos evaluados |
|---:|---:|---:|---:|
| 64 | 12 000 | 7 057 | 14 114 |
| 96 | 12 000 | 7 781 | 15 562 |
| 128 | 12 000 | 8 264 | 16 528 |

Cada selección aporta un intervalo `PAST` y otro `FUTURE`. Los análisis se mantienen
separados por lado; no se forma su cociente.

## 4. Sesgo de altura a tamaño fijo

La magnitud es

```text
B_H = H_selected - E[H_0(m)].
```

| `n` | Lado | Media `B_H` | Bootstrap 95 % |
|---:|---|---:|---:|
| 64 | pasado | -0.0589 | [-0.0792, -0.0382] |
| 64 | futuro | -0.0988 | [-0.1180, -0.0780] |
| 96 | pasado | -0.0956 | [-0.1207, -0.0721] |
| 96 | futuro | -0.0880 | [-0.1125, -0.0649] |
| 128 | pasado | -0.0806 | [-0.1043, -0.0550] |
| 128 | futuro | -0.0882 | [-0.1121, -0.0646] |

El sesgo post-selección es negativo, reproducible y pequeño: alrededor de una décima
de elemento de cadena. Los seis intervalos bootstrap quedan muy dentro del límite
congelado `[-0.50,0.50]`.

Este bloque pasa. El error Monte Carlo del baseline por tamaño se reporta por
separado y no está incluido en los intervalos bootstrap.

## 5. Calibración media de duración

| `n` | Lado | Media `ell` | Media `H/(2√n)` | Sesgo medio | Mediana error relativo |
|---:|---|---:|---:|---:|---:|
| 64 | pasado | 0.3806 | 0.4006 | +0.0201 | 0.1370 |
| 64 | futuro | 0.3792 | 0.3990 | +0.0198 | 0.1418 |
| 96 | pasado | 0.4033 | 0.4048 | +0.0014 | 0.1142 |
| 96 | futuro | 0.4031 | 0.4048 | +0.0016 | 0.1130 |
| 128 | pasado | 0.4163 | 0.4103 | -0.0061 | 0.1019 |
| 128 | futuro | 0.4175 | 0.4103 | -0.0072 | 0.1043 |

Los errores relativos medianos disminuyen de aproximadamente 14 % a 10 %. Sus seis
límites superiores bootstrap permanecen por debajo del umbral `0.30`.

La calibración de escala media pasa. Esto, sin embargo, no implica resolución
individual.

## 6. Fallo de resolución individual

| `n` | Lado | Correlación Pearson | Bootstrap 95 % | Pendiente OLS | Intercepto |
|---:|---|---:|---:|---:|---:|
| 64 | pasado | 0.2910 | [0.2696, 0.3123] | 0.3017 | 0.2858 |
| 64 | futuro | 0.2733 | [0.2516, 0.2921] | 0.2793 | 0.2931 |
| 96 | pasado | 0.2362 | [0.2163, 0.2574] | 0.2795 | 0.2920 |
| 96 | futuro | 0.2759 | [0.2559, 0.2961] | 0.3261 | 0.2733 |
| 128 | pasado | 0.2275 | [0.2074, 0.2483] | 0.2877 | 0.2905 |
| 128 | futuro | 0.2238 | [0.2041, 0.2429] | 0.2856 | 0.2911 |

El gate exigía un límite inferior de correlación de al menos `0.80`. Los seis límites
superiores están por debajo de `0.32` y también por debajo del umbral fuerte de
aparcamiento `0.50`.

La aparente paradoja —error relativo pequeño y correlación baja— se explica porque
el selector concentra las duraciones en una banda estrecha. Por ejemplo, los
percentiles 10–90 de `ell` pasan aproximadamente de `[0.30,0.46]` en `n=64` a
`[0.36,0.47]` en `n=128`. Un estimador cercano a la media puede tener poco error
absoluto sin discriminar qué intervalo es realmente más largo dentro de esa banda.

Las pendientes OLS próximas a `0.3`, con interceptos próximos a `0.29`, muestran la
misma compresión. La cadena conserva una escala media razonable, pero sus
fluctuaciones dominan la variación de duración que deja disponible el selector.

## 7. Estabilidad del target bajo thinning

El evento exige que ambas duraciones del nuevo par queden dentro del 25 % de las
duraciones base, aun cuando cambien los endpoints.

| `n` | Retención | Ambos únicos | Target dentro del 25 % | Wilson 95 % | Reselección exacta |
|---:|---:|---:|---:|---:|---:|
| 64 | 0.90 | 5 413 | 0.8653 | [0.8560, 0.8742] | 0.6030 |
| 64 | 0.80 | 4 654 | 0.7232 | [0.7102, 0.7359] | 0.3543 |
| 96 | 0.90 | 6 169 | 0.9339 | [0.9274, 0.9398] | 0.5781 |
| 96 | 0.80 | 5 497 | 0.8321 | [0.8220, 0.8417] | 0.3158 |
| 128 | 0.90 | 6 656 | 0.9633 | [0.9586, 0.9676] | 0.5481 |
| 128 | 0.80 | 6 135 | 0.9141 | [0.9068, 0.9209] | 0.3073 |

El target latente es mucho más estable que la identidad de sus endpoints. En
`n=128`, retención `0.80`, solo el 30.7 % reselecciona la misma cuádrupla, pero el
91.4 % conserva ambas duraciones dentro del 25 %.

Este bloque supera ampliamente los umbrales congelados. También muestra que el fallo
de altura no se debe a una inestabilidad macroscópica de la duración seleccionada.

## 8. Terminal congelado

Los bloques de sesgo, error relativo y estabilidad pasan. El bloque de correlación
no solo falla: satisface la condición fuerte de aparcamiento en ambos lados y los
tres tamaños.

```text
P1A_LEX_HEIGHT_TERMINAL = PARK_LEX_HEIGHT_REPRESENTATION
P1A_HEIGHT_RATIO_COMPUTED = NO
P1A_HEIGHT_RATIO_PREREGISTRATION = NOT_AUTHORIZED
```

El terminal cierra la representación

```text
MIN_COVERAGE_LEX + altura individual H/(2 sqrt(n))
```

como vía directa al cociente temporal en este régimen. No cierra P1 ni refuta la
relación asintótica clásica entre altura y tiempo propio para endpoints fijados.

## 9. Interpretación científica

La distinción central es:

```text
calibracion ensemble-level: favorable;
resolucion individual dentro del target seleccionado: desfavorable.
```

La selección max–min produce intervalos bien soportados y de duraciones parecidas.
Precisamente por ello reduce la señal relativa que una altura entera y fluctuante
debe resolver. Ejecutar ahora `H_minus/H_plus` eludiría el gate y podría convertir
ruido de cadena en una razón aparentemente métrica.

No se excluye que:

- densidades mucho mayores cambien la resolución;
- otro selector conserve una dispersión temporal mayor;
- un observable order-only más rico que la altura mejore la inferencia;
- o un tratamiento conjuntista/ensemble-level sea identificable aunque la salida
  puntual no lo sea.

Cada alternativa requiere una nueva formulación y no puede reutilizar este `PARK`
como evidencia positiva.

## 10. Artefactos

- `emergencia/resultados/p1a_lex_intervalos_d2.csv`
- `emergencia/resultados/p1a_lex_altura_calibracion_d2.csv`
- `emergencia/resultados/p1a_lex_altura_baseline_por_tamano_d2.csv`
- `emergencia/resultados/p1a_lex_target_thinning_d2.csv`
- `emergencia/resultados/p1a_lex_altura_duracion_resumen.json`
- sidecars `*.sha256`

```text
P1A_LEX_HEIGHT_RESULT = COMPLETE_REPRODUCIBLE
P1A_ENSEMBLE_SCALE_CALIBRATION = FAVORABLE
P1A_INDIVIDUAL_DURATION_RESOLUTION = STRONG_FAIL
P1A_LATENT_TARGET_STABILITY = PASS
P1A_CURRENT_REPRESENTATION = PARKED
P1A_METRIC_IDENTIFIABILITY = OPEN
P1A_NOVELTY_CERTIFIED = NO
```

La apertura posterior de dos representaciones distintas se documenta en
`emergencia/P1a_resultados_representaciones_alternativas_d2.md`. `HEIGHT_WIDTH` queda
fuertemente aparcada; `COUNT_VOLUME` mejora la resolución y permanece abierta, pero
no cualifica para un cociente. Este resultado no reabre la representación de altura
cerrada aquí.
