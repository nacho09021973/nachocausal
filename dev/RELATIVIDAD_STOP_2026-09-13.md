# Relatividad — parada del programa de saturación

**Fecha:** 2026-09-13
**Estado:** `STOPPED_BEFORE_LARGE_SCALE_COMPUTATION`

## Conclusión

> **The original saturation program is stopped before large-scale computation. The blocking issue
> is definitional rather than numerical: under the current primitives there is no intrinsic,
> non-tautological, realization-level notion of dynamical characteristic front.**

Esto no demuestra que la Tesis S sea falsa en sentido absoluto. Demuestra que todavía no está
formulada mediante un objeto físico inequívoco que pueda someterse a una prueba de universalidad.
No se autoriza gastar el presupuesto de sprinklings ni abrir una batería experimental para suplir
esa carencia conceptual.

## Cadena adversarial

```text
ATTACK_01 -> retardo + intrínseco + relabeling no fuerzan saturación;
ATTACK_02 -> v_front -> c puede ser geometría asintótica;
ATTACK_03 -> Delta -> 0 depende del camino de límite y la normalización;
ATTACK_04 -> soporte y umbral no definen un frente canónico;
ATTACK_05 -> wavefront set / singular support no tienen un análogo order-only
             disponible bajo las primitivas actuales.
```

La objeción final es definicional: en un causal set finito no hay literalmente distribución
diferencial, cotangente ni singular support. Las construcciones conocidas que recuperan
propagadores o `Box` causal comparan con Minkowski, AQFT o Klein–Gordon y usan la estructura
continua para definir la noción característica. Eso dinamiza campos sobre una geometría lorentziana
ya dada; no proporciona el objeto discreto que el programa necesitaba hacer emerger.

## Estado lógico

```text
GATE_M_LARGE = CANCELLED / NOT JUSTIFIED
TESIS_S      = BLOCKED_UNDER_CURRENT_PRIMITIVES
E3           = BLOCKED_BY_S
E4           = NOT_OPENED
```

La etiqueta correcta no es `TESIS_S = FALSE`: el programa no ha encontrado un contraejemplo a una
formulación bien definida de S, sino que ha mostrado que esa formulación todavía falta. La versión
amplia quedó además debilitada por ATTACK_01–03, y la interpretación de frente quedó sin observable
canónico tras ATTACK_04–05.

## Único criterio de reapertura

La línea sólo puede reabrirse si aparece un objeto del tipo

```text
Char_C[G]
```

definido únicamente a partir de orden + dinámica, que sea:

- intrínseco y libre de embedding o métrica reconstruida;
- no idéntico por construcción al soporte retardado;
- independiente de un umbral arbitrario y estable frente a reescalado;
- definido realización por realización;
- estable bajo refinamiento o un camino de límite explícito;
- capaz de distinguir cola causal, característica y masa principal de la señal;
- convergente, cuando proceda, al `wavefront set` continuo sin importar la conclusión `partial D=partial K`.

Un nuevo umbral, gradiente, máximo, percentil o cuantíl no satisface este criterio automáticamente:
sería ATTACK_04 con otra parametrización hasta demostrar lo contrario.

## Backlog, no programa activo

La intuición inicial —que distintas dinámicas podrían compartir una frontera causal— se conserva
como hipótesis de backlog. No es una tarea activa, no genera runs y no justifica Gate M grande.

El resultado positivo de esta ronda es metodológico: los ataques han localizado el cuello de botella
antes de la simulación y han evitado convertir una definición ambigua en una señal numérica
aparentemente universal.

**No se ejecutaron Gate M, Tesis S, E3 ni E4. No se hicieron simulaciones nuevas.**
