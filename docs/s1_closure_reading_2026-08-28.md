# Lectura congelada del cierre S1

```text
ESTADO: LECTURA_CONGELADA — NO ABRE S2
ANCLA_CIENTIFICA: 2219f21dea2cbd82ba9d959a6d55e1cf87a0bcf6
GOBERNANZA: docs/program_reopening_note_2026-08-28_R4.md (firmada)
FECHA: 2026-08-28
NATURALEZA: lectura de gobernanza y de lenguaje. Cero matemática nueva,
            cero semillas, cero simulación, sello intacto.
S2: NOT_OPEN
DECISION_S2: PENDING_FUTURE_PI_DECISION
NO_HORIZON_CLAIM
NO_BENCHMARK_TRANSFER_CLAIM
NO_T20
```

Esta nota no enmienda `2219f21`. No toca el work package, la hoja de ruta,
T20, el benchmark, horizontes ni dimensiones superiores. Fija cómo debe
leerse el cierre S1.

## 1. Precisión de lenguaje físico

No se dirá que «la geometría es un diamante plano de Minkowski».

> **El experimento local está construido sobre un diamante de Minkowski
> \(1+1\) como punto base, perturbado conformemente por \(g_\varepsilon\).**

El punto \(\varepsilon=0\) es plano. Las perturbaciones con componente de
interacción \(\mathcal P\psi\neq 0\) no tienen por qué serlo: precisamente
queremos que \(\mathcal P\psi\) contenga información geométrica no
marginal.

El token `MINKOWSKI_DIAMOND_PERTURBATIVE` del artefacto anclado se lee
así, no como planitud de \(g_\varepsilon\) para \(\varepsilon\neq 0\).
La línea de alcance del WP que nombra un «diamante plano de Minkowski»
designa el **punto base**, no la familia perturbada.

## 2. Separación que permanece

```text
teorema combinatorio          = PROVED
clasificacion geometrica S1   = PROVED
S2                            = NOT_OPEN
```

La suma de los dos `PROVED` **no implica**, por gobernanza, la apertura
de S2.

## 3. Qué es S2, y qué no es

El límite Fisher (11.6) ya se sigue internamente de los resultados
existentes. S2 **no** tiene una obligación matemática nueva escondida.
Sería elevar esa composición a un teorema autónomo, con hipótesis,
experimento estadístico y claim ceiling formulados de una sola vez.

El próximo gate no pregunta «¿podemos demostrar S2?». La respuesta
parece esencialmente sí. La pregunta correcta es:

> ¿Merece la pena convertir este corolario compuesto en un resultado
> autónomo S2?

Ahí entran valor científico, claridad conceptual y, más tarde, prioridad
bibliográfica. No una nueva búsqueda de matemática.

## 4. Fuera de esta lectura

T20, el puente al benchmark histórico, horizontes y \(2+1\)/\(3+1\)
permanecen fuera. `2219f21` es, por sí mismo, un punto de parada
científicamente coherente.

```text
FIRMADA_POR: Ignacio Martin (PI)
FECHA_FIRMA: 2026-08-28
DECISION_S2: PENDING_FUTURE_PI_DECISION
```
