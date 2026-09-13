# Relatividad — ATTACK 04: confusión frente/umbral

**Objetivo:** intentar destruir la identificación

```text
llegada por umbral = frente dinámico
```

antes de ejecutar cualquier batería costosa.

**Estado:** ataque analítico; sin simulación, sin búsqueda, sin ajuste y sin cambio de umbrales ni
preregistraciones.

## 1. Tres objetos distintos

Sea `K` el cono cinemático permitido y sea `s` una coordenada abstracta de profundidad transversal
que aumenta desde el interior hacia `partial K`, con `s=1` en la frontera. Para una respuesta
retardada `chi(s)`, hay que distinguir:

```text
soporte:                 closure({s: chi(s) != 0});
frente:                  frontera física/matemática de propagación;
llegada a amplitud finita: T_dyn^(theta) = boundary({s: chi(s) >= theta}).
```

El soporte está limitado por `K` si la respuesta es retardada, pero esa inclusión no determina qué
parte de la respuesta es físicamente el frente. Un nivel `theta` selecciona una amplitud, no una
frontera causal por definición.

## 2. Caso A — falso negativo

Construimos una respuesta cuyo soporte llega hasta `partial K`, pero cuya amplitud dominante está
profundamente dentro. Para `0<=s<=1`, sea

```text
chi_A(s) = A exp(-(s-s_0)^2/sigma^2)
          + eps exp(-(1-s)/delta),
```

con

```text
0 < s_0 < 1,
0 < sigma << 1,
0 < eps << A,
delta > 0.
```

Extendemos `chi_A` a cero fuera de `K`. El segundo término es una cola no nula arbitrariamente
cerca de `s=1`, de modo que el cierre del soporte alcanza `partial K`. La primera contribución es
un pico dominante en `s_0`, lejos de la frontera.

Elija un umbral finito que satisfaga

```text
eps < theta < A exp(-q^2),
```

para un `q` tal que la superación del umbral ocurra sólo en una vecindad del pico interior. En ese
caso,

```text
closure(support chi_A) reaches partial K,
T_dyn^(theta) is strictly inside K,
Delta_theta > 0.
```

Por tanto es posible que el frente verdadero sea `partial D=partial K`, mientras un observable de
umbral clasifica la dinámica como subsaturada. El falso negativo es robusto ante perturbaciones
pequeñas de `eps`, `sigma` y `theta` dentro del intervalo anterior; no depende de ajustar un punto
exacto.

Interpretación: una cola causal débil puede transportar el frente hasta `partial K` sin dominar la
respuesta usada por el umbral.

## 3. Caso B — falso positivo

Invertimos la lectura física. Sea

```text
chi_B(s) = A exp(-(s-s_0)^2/sigma^2)
          + eps exp(-(1-s)/delta),
```

pero ahora interpretamos como “dinámicamente relevante” la masa integrada o energía de la
respuesta, y tomamos `eps/A` tan pequeño como se desee. Entonces

```text
mass(tail near partial K) / mass(chi_B) -> 0  as eps/A -> 0,
support(chi_B) reaches partial K.
```

El soporte puro declara alcance de `partial K`. Asimismo, un procedimiento que envíe
`theta -> 0` eventualmente detectará la cola y puede declarar saturación. Sin embargo, para todo
`eps/A` suficientemente pequeño, la respuesta macroscópicamente relevante sigue concentrada cerca
de `s_0<1`, estrictamente dentro de `K`.

Así,

```text
support reaches partial K,
theta -> 0 can declare saturation,
dominant response remains subluminal/subsaturating.
```

El falso positivo también es robusto: no requiere que la cola sea exactamente cero, sólo que su
peso sea menor que la resolución física o estadística declarada.

## 4. Ningún extremo resuelve el problema

Los dos casos dan:

```text
support != good observable of front,
threshold != canonical observable of front.
```

El soporte puro es demasiado permisivo: confunde una cola precursora infinitesimal con la
propagación dominante. Un umbral fijo es demasiado selectivo: puede ocultar una cola que ya alcanza
`partial K`. Llevar `theta` a cero cambia el falso negativo por el falso positivo, pero no define
qué amplitud es físicamente el frente.

Además, un umbral fijo no es estable frente a reescalado de amplitud:

```text
chi -> a chi  (a>0)
```

cambia `T_dyn^(theta)` salvo que se renormalice `theta`; una transformación monótona general cambia
los niveles aunque preserve el soporte. La renormalización necesaria ya introduce una elección que
debe justificarse antes del resultado.

## 5. Pregunta central

¿Existe una definición intrínseca de “frente dinámico” que sea simultáneamente:

- independiente del embedding;
- no trivialmente igual al soporte retardado;
- no dependiente de un `theta` arbitrario;
- estable frente a reescalado de amplitud;
- robusta frente a fluctuaciones de sprinkling;
- compatible con la trivialización lorentziana de ATTACK_02;
- compatible con la ambigüedad de límites de ATTACK_03;
- definida realización por realización;
- capaz de distinguir una cola precursora de un frente realmente saturante?

Este documento no postula que la respuesta sea negativa en toda teoría. Exige que cualquier
definición candidata pase ambos contraejemplos sin consultar el embedding ni introducir `partial K`
como objetivo oculto.

## 6. Test de supervivencia no circular

Una definición candidata sólo puede pasar si, antes de ver el resultado:

1. fija qué funcional de la respuesta representa relevancia física;
2. especifica cómo trata colas, nodos y soporte de medida cero;
3. es invariante frente a `chi -> a chi` y declara el tratamiento de transformaciones monótonas;
4. tiene una regla de estabilidad por realización, no sólo en promedio;
5. distingue el Caso A del Caso B;
6. mide además profundidad causal/invariante y declara el camino de límite;
7. no define el frente como “la parte que coincide con `partial K`”.

Una norma, cuantíl, flujo o susceptibilidad podría ser candidato, pero no se introduce aquí como
solución: habría que demostrar que su elección tiene una motivación física independiente y que no
reproduce la conclusión por construcción.

## 7. Salidas preregistradas

```text
SURVIVES_ATTACK
    Existe al menos una definición candidata de frente que evita claramente ambos
    contraejemplos sin consultar embedding ni introducir partial K como objetivo.

STOPS_AS_FRONT_UNDEFINED
    No se encuentra una definición no circular y robusta que distinga soporte,
    cola y llegada de amplitud finita.

STOPS_AS_THRESHOLD_DEPENDENT
    La conclusión de saturación cambia esencialmente con theta o con
    normalizaciones monótonas de chi.

STOPS_AS_SUPPORT_TAUTOLOGY
    La única definición estable termina siendo el soporte causal impuesto por
    retardo, y por tanto Tesis S se vuelve tautológica.
```

Si Attack 04 termina en cualquiera de las tres salidas de parada, no debe “salvarse” la idea con
un umbral elegido post hoc. La consecuencia debe quedar escrita aunque detenga Tesis S.

## 8. Decisión provisional

Los dos kernels muestran que ni el soporte ni la llegada a amplitud finita son, por sí solos, un
frente físico bien definido. Hasta encontrar una definición que supere el test de §6, la afirmación
segura es:

```text
FRONT_STATUS = UNDEFINED_UNDER_CURRENT_PRIMITIVES
GATE_S       = NOT_INTERPRETABLE_FROM_SUPPORT_OR_FIXED_THRESHOLDS
```

No se ejecutan Gate M, Tesis S, E3 ni E4 en este documento.
