# Relatividad — ATTACK 03: ambigüedad del límite de escalado

**Objetivo:** comprobar si `Delta -> 0` puede fabricarse eligiendo de forma conveniente cómo crecen
`N`, `L`, `rho` y `N_ref`.

**Estado:** ataque analítico; sin simulación, sin búsqueda, sin ajuste y sin cambio de Gate.

## 1. Tres significados distintos de `N -> infinity`

Para una región observada de volumen físico `Vol(L)` y densidad de sprinkling `rho`, típicamente

```text
N(L,rho) ~ rho Vol(L).
```

Por tanto `N -> infinity` no define un único límite.

### Límite de resolución

```text
L fijo, rho -> infinity, N -> infinity.
```

La región física permanece fija y desaparece la discreción microscópica.

### Límite de volumen

```text
rho fijo, L -> infinity, N -> infinity.
```

La escala microscópica permanece fija y crece la región observada. Es un límite termodinámico o de
gran distancia, no un refinamiento local.

### Límite conjunto

```text
L -> infinity, rho=rho(L) -> infinity,
```

con resultado potencialmente dependiente de la relación entre ambas escalas y del orden de los
límites. Un claim que diga solamente `N -> infinity` no distingue estos casos.

## 2. Cómo se fabrica una convergencia de velocidad

Incluso manteniendo dos profundidades propias distintas,

```text
tau_1 != tau_2 > 0,
v_i(L) = L/sqrt(L^2+tau_i^2),
```

se obtiene

```text
|v_1(L)-v_2(L)|
  = |tau_1^2-tau_2^2|/(2L^2) + O(L^-4)
  -> 0.
```

Luego una discrepancia basada sólo en la pendiente puede satisfacer `Delta(L)->0` por aumentar el
volumen observado, aunque ninguna profundidad causal colapse:

```text
lim_(L->infinity) tau_i = tau_i > 0.
```

Este es un falsador directo de la lectura “`Delta -> 0` implica universalización” si `Delta` mide
únicamente velocidades.

## 3. Cómo se fabrica una convergencia por normalización

Si el observable usa una discrepancia dimensional dividida por una escala creciente, por ejemplo

```text
Delta_L = |tau_1-tau_2|/L,
```

entonces `Delta_L -> 0` es automático para cualquier diferencia finita de profundidades. La
normalización puede ocultar exactamente la información que Gate S pretende medir.

Análogamente, en un kernel de volumen normalizado,

```text
n/N_ref -> V/V_ref,
```

el crecimiento simultáneo de `n` y `N_ref` puede estabilizar la respuesta en una profundidad propia
finita. Hacer crecer `N_ref` no equivale a hacer tender esa profundidad a cero.

## 4. Auditoría obligatoria del observable `Delta`

Antes de cualquier run, Gate S debe fijar en una tabla de preregistro:

| Elemento | Debe quedar fijado |
|---|---|
| Límite primario | `rho->infinity`, `L->infinity`, o límite conjunto explícito. |
| Orden de límites | Si hay dos límites, cuál se toma primero y si se exige conmutación. |
| Escala microscópica | Cómo depende `ell ~ rho^(-1/d)` de `rho`. |
| Región de referencia | Si `N_ref` es fijo, local, proporcional a `N` o dependiente de `L`. |
| Definición de `Delta` | Fórmula exacta y unidades antes de mirar resultados. |
| Observable invariante | Profundidad propia, volumen causal o cociente fijado independientemente. |
| Control negativo | Dos especies con `tau_1 != tau_2` pero misma asintótica de velocidad. |

Sin esta tabla, `Delta->0` debe clasificarse como `SCALING_UNRESOLVED`, no como PASS.

## 5. Criterio de no fabricación

Una afirmación de colapso debe demostrar, en el mismo límite declarado,

```text
tau_front(lambda,theta;L,rho) -> 0,
```

o una desigualdad equivalente en una unidad propia fijada independientemente de `L`, `N` y
`N_ref`. Además debe comprobar que:

```text
Delta -> 0
```

no se mantiene cuando `tau_front` se mantiene separado de cero en el control adversarial.

La divergencia entre los siguientes dos resultados es decisiva:

```text
Delta -> 0, tau_front -> 0       => compatible con saturación;
Delta -> 0, tau_front -> tau_*>0 => trivialización por escalado.
```

## 6. Resultado adversarial y decisión

```text
ADVERSARIAL_RESULT = PASS
CLAIM_UNDER_ATTACK  = UNRESOLVED_UNLESS_LIMIT_IS_SPECIFIED
```

El ataque no demuestra que el observable concreto de Gate S esté mal normalizado; demuestra que
la notación `N->infinity` y una convergencia desnuda `Delta->0` no bastan para saberlo.

Gate S sólo sobrevive si fija un camino de límite y muestra colapso de profundidad invariante, no
sólo convergencia de una pendiente o de una cantidad dividida por `L`. Si no puede hacerlo, la salida
correcta es:

```text
STOPS_AS_SCALING_UNRESOLVED
```

No se ejecutan Gate M, Gate S ni Gate U en este documento.
