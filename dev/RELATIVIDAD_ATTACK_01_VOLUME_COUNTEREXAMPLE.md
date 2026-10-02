# Relatividad — ATTACK 01: contraejemplo de volumen normalizado

**Objetivo:** intentar falsar Gate S antes de ejecutar Gate M a gran escala.

**Estado:** ataque analítico; sin simulación, sin búsqueda, sin ajuste y sin cambio de Gate.

## 1. Claim atacado

La versión amplia bajo ataque sería:

> Toda dinámica de frontera que sea intrínseca, retardada, invariante por relabeling y libre de
> embedding o métrica de fondo produce, al aumentar la densidad del sprinkling, una frontera que
> satura el cono nulo.

El documento no ataca una `D` más estrecha ya especificada. Pregunta si las cuatro condiciones
anteriores, por sí solas, tienen esa consecuencia.

## 2. Familia admisible

Sea `x ≺ y` y sea `I(x,y)` el intervalo causal abierto entre ambos. Definimos

```text
n(x,y)   = |I(x,y)|
N_ref    = |I_ref|
chi_f(y,x) = f(n(x,y)/N_ref),       x ≺ y,
```

donde `I_ref` es una región de referencia seleccionada por una regla puramente relacional, y `f`
es monótona. Para evitar la degeneración de la palabra “nivel”, se supone que `f` es estrictamente
monótona en el rango usado y que `theta` pertenece a su imagen.

Esta familia cumple las condiciones atacadas:

| Condición | Verificación |
|---|---|
| Intrínseca | Usa sólo cardinalidades de intervalos y una referencia definida en el propio orden. |
| Retardada | `chi_f(y,x)` sólo depende del pasado causal de `y` relativo a `x`. |
| Relabeling-invariant | Cardinalidades e intervalos se preservan bajo isomorfismos del causal set. |
| Sin embedding ni métrica de fondo | No recibe coordenadas, `g_mu nu` ni una función de distancia externa. |

La referencia `I_ref` no puede ser una región elegida mirando el embedding. Si la teoría no ofrece
una regla relacional para seleccionarla, la familia queda condicionada a esa regla; eso sería una
carencia de definición, no una refutación. Si sí existe tal regla —por ejemplo, un intervalo
canónico o una clase de referencia fijada por cardinalidad/estructura— el contraejemplo es
admisible bajo las cuatro condiciones.

## 3. Límite manifoldlike

Para un sprinkling de densidad `rho` en una geometría manifoldlike,

```text
n(x,y)   / rho -> V(x,y),
N_ref    / rho -> V_ref,
```

por lo que

```text
n(x,y)/N_ref -> V(x,y)/V_ref.
```

Un nivel fijo `chi_f = theta` satisface, en el límite,

```text
V(x,y)/V_ref = c_theta,    c_theta = f^{-1}(theta).
```

El factor `rho` se cancela. Por tanto el límite `rho -> infinity` no fuerza por sí mismo que
`V(x,y)` tienda a cero.

## 4. Contraejemplo explícito en 1+1

En Minkowski `1+1`, para una separación temporal `t` y espacial `r`,

```text
V(x,y) = C (t^2-r^2),       t>|r|,
```

con `C>0` dependiente sólo de la convención de volumen. Si `V_ref` es fijo en la geometría de
referencia, el nivel de respuesta queda dado por

```text
t^2-r^2 = (c_theta V_ref)/C = tau_theta^2,
tau_theta > 0.
```

Así, la frontera converge a una hipérbola de profundidad propia finita `tau_theta`, no al cono
nulo `t^2-r^2=0`. Aumentar la densidad mejora la aproximación del conteo al volumen; no cambia la
razón normalizada que define la superficie.

Esto es un contraejemplo a la implicación universal

```text
intrínseca + retardada + relabeling-invariant + emb-free
    ==> null-cone saturation.
```

La conclusión es negativa incluso antes de discutir errores estadísticos, resolución angular o
el comportamiento de un kernel concreto de sprinkling.

## 5. Dos especies sobre la misma causalidad

El efecto no es sólo una elección de coordenada o de presentación. Sean `f_1` y `f_2` dos funciones
estrictamente monótonas, o sean `N_ref,1` y `N_ref,2` dos escalas internas relacionales distintas.
En general,

```text
c_1 = f_1^{-1}(theta_1) != c_2 = f_2^{-1}(theta_2),
```

y por tanto

```text
tau_1^2 = c_1 V_ref,1 / C != c_2 V_ref,2 / C = tau_2^2.
```

Las dos dinámicas pueden vivir sobre el mismo orden causal y obedecer todas las condiciones
formales, pero producir fronteras distintas. La densidad no elimina esta diferencia.

## 6. Qué queda formalmente demostrado

Si las hipótesis de selección relacional de `I_ref` se cumplen, el argumento establece:

```text
ADVERSARIAL_RESULT = PASS
CLAIM_UNDER_ATTACK  = FAIL
```

en el sentido preciso de que las cuatro condiciones generales no implican saturación universal.
No establece todavía que Gate S completo sea imposible: `D` podría imponer restricciones
adicionales físicamente motivadas.

Tampoco demuestra que toda dinámica relacional tenga una frontera de volumen normalizado, ni que
el límite de sprinkling sea uniforme para todas las reglas intrínsecas. Sólo basta un miembro
admisible de la familia para romper la implicación universal.

## 7. Test de no circularidad para una restricción adicional

Una condición candidata `R` que excluya esta familia debe pasar simultáneamente:

1. **Definición previa:** `R` se formula antes de mirar si produce el cono.
2. **Contenido físico independiente:** `R` tiene una motivación dinámica o microscópica que no sea
   simplemente “la frontera debe aproximar el cono nulo”.
3. **Aplicabilidad:** `R` se puede verificar en el formalismo permitido, sin reintroducir embedding
   o métrica de fondo por la puerta trasera.
4. **Exclusión real:** `R` excluye el cociente `n/N_ref`, no sólo una elección particular de `f`.
5. **No vacuidad:** queda al menos una clase no circular de dinámicas candidata a `D`.

Ejemplos de restricciones que **no** cuentan por sí solas:

```text
"la respuesta debe volverse singular en el cono";
"el nivel debe depender de un número fijo de elementos";
"D contiene sólo kernels que saturan el cono".
```

La primera es la conclusión disfrazada; la segunda cambia sustancialmente la clase de kernels y
debe justificarse físicamente; la tercera es directamente circular.

## 8. Decisión de programa

Antes de Gate M a gran escala, Gate S debe responder a una de estas dos salidas:

```text
SURVIVES_ATTACK
    si existe una restricción R previa, físicamente independiente y no vacía
    que excluye la familia de volumen normalizado.

STOPS_AS_OVERBROAD
    si toda R disponible equivale a imponer propagación nula, o no puede excluir
    la familia sin usar la conclusión como definición.
```

Hasta obtener la primera salida, no debe afirmarse “saturación universal”. La formulación segura
es:

```text
Las condiciones generales de intrinsequedad, retardo, relabeling-invarianza y
ausencia de embedding no bastan para derivar saturación nula.
```

**No se ejecutan Gate M, Gate S ni Gate U en este documento.** El propósito es decidir si merece la
pena intentar salvar Gate S mediante una restricción adicional no circular.
