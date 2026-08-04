# P1a — Primer selector de cobertura para dos intervalos

> **ESTADO: CONTRATO MATEMÁTICO v0.1 · SELECTOR PARCIAL CONGELADO · SIN
> EJECUCIÓN NUMÉRICA.**
>
> Esta nota concreta el primer selector de P1a. Su finalidad es disponer de un
> objeto determinista, equivariante y comprobable que no optimice la razón temporal
> que se estudiará después. No demuestra correspondencia con tiempo propio, no fija
> todavía un estimador métrico definitivo y no reclama novedad.

## 0. Decisión

La primera regla no buscará un midpoint ni intentará equilibrar dos duraciones.
Seleccionará, cuando exista un ganador único, dos intervalos:

1. causalmente ordenados;
2. sin elementos comunes;
3. con soporte mínimo no degenerado;
4. y con cobertura total máxima.

Si hay empate, la salida puntual queda indefinida y se conserva el conjunto completo
de maximizadores.

```text
P1A_SELECTOR = F_cov,3
P1A_SELECTION_STATISTIC = TOTAL_INTERVAL_CARDINALITY
P1A_ESTIMATION_STATISTIC = NOT_YET_FROZEN
P1A_TIE_POLICY = ABSTAIN_AND_RETAIN_ARGMAX_SET
```

## 1. Canal y objeto observado

La entrada es únicamente un poset finito no etiquetado `C=(V,prec_C)`. Su
cardinalidad `N=|V|` forma parte de la observación. No se proporcionan:

- coordenadas;
- embedding;
- elementos extremos;
- orden de almacenamiento;
- etiquetas naturales;
- ni una geometría latente para seleccionar candidatos.

Las construcciones siguientes son funciones del orden y de conteos derivados de él.

## 2. Intervalos candidatos

Para `x prec_C y`, escribimos

```text
[x,y]_C = {z in V : x <=_C z <=_C y},
n_C(x,y) = |[x,y]_C|.
```

Congelamos el soporte mínimo inicial en

```text
k_0 = 3.
```

Así se excluyen los intervalos formados únicamente por un link y sus dos extremos.
Este umbral permite formular el problema más pequeño no trivial; no constituye una
afirmación de suficiencia estadística. Un uso métrico posterior requerirá estudiar
umbrales crecientes o bastante mayores.

Definimos el conjunto de cuádruplas admisibles

```text
Q_3(C) = {
  (a,b,c,d) in V^4 :
  a prec_C b prec_C c prec_C d,
  n_C(a,b) >= 3,
  n_C(c,d) >= 3
}.
```

A cada cuádrupla `q=(a,b,c,d)` le asociamos el par ordenado

```text
J_-(q) = [a,b]_C,
J_+(q) = [c,d]_C.
```

La relación `b prec_C c` determina la orientación del par sin recurrir a etiquetas:
`J_-` es el intervalo anterior y `J_+` el posterior.

### Lema P1a-C.1 — disjunción

Para toda `q in Q_3(C)`,

```text
J_-(q) interseccion J_+(q) = vacio.
```

**Demostración.** Si `z` perteneciera a ambos intervalos, tendríamos

```text
z <=_C b prec_C c <=_C z,
```

lo que contradice la antisimetría del orden. `QED`

La disjunción evita reutilizar un mismo elemento en ambos intervalos. No implica
independencia probabilística entre las dos mediciones.

## 3. Score de cobertura

Para `q in Q_3(C)`, definimos

```text
S_cov,C(q)
  = |J_-(q) union J_+(q)|
  = n_C(a,b) + n_C(c,d).
```

La segunda igualdad usa la disjunción probada en §2.

Este score favorece pares que aprovechan más elementos observados dentro de los dos
intervalos. Deliberadamente no utiliza:

- `L_C(a,b)` ni `L_C(c,d)`;
- el cociente de cardinalidades;
- la diferencia entre los tamaños;
- el mínimo o el producto de los dos tamaños;
- una condición de balance;
- ni una reconstrucción de coordenadas.

Por ello no fija algebraicamente el valor de una futura razón de longitudes de
cadenas. Sí puede introducir selección estadística y sesgo geométrico; esas cuestiones
pertenecen a P1b y no se consideran resueltas aquí.

## 4. Selector puntual y salida conjuntista

Definimos

```text
M_cov(C) =
  Argmax_{q in Q_3(C)} S_cov,C(q), si Q_3(C) no es vacio;
  vacio,                              si Q_3(C) es vacio.
```

Definimos el selector parcial

```text
F_cov,3(C) =
  (J_-(q_*),J_+(q_*)),  si M_cov(C)={q_*};
  UNDEFINED_NO_CANDIDATE, si Q_3(C)=vacio;
  UNDEFINED_TIE,          si |M_cov(C)|>1.
```

En los dos casos de abstención se conserva una salida secundaria:

```text
G_cov,3(C) = {
  (J_-(q),J_+(q)) : q in M_cov(C)
}.
```

Cuando `Q_3(C)` es vacío, `G_cov,3(C)` también es vacío.

No se elige el primer elemento de `M_cov(C)` ni se aplica una ordenación de etiquetas.

## 5. Proposición P1a-C.2 — equivariancia

Sea `phi:C -> C'` un isomorfismo de posets. Entonces:

```text
phi(Q_3(C)) = Q_3(C'),
S_cov,C'(phi(q)) = S_cov,C(q),
phi(M_cov(C)) = M_cov(C').
```

En consecuencia:

1. `G_cov,3` es una salida conjuntista equivariante para todo poset finito;
2. el dominio donde `F_cov,3` está definido es invariante bajo isomorfismos;
3. y, sobre ese dominio, `F_cov,3` es un selector determinista equivariante.

### Demostración

Un isomorfismo preserva comparabilidades, intervalos y cardinalidades. Por tanto,
lleva biyectivamente cuádruplas admisibles a cuádruplas admisibles y preserva
`S_cov`. De aquí se sigue la igualdad de los conjuntos de maximizadores. Si el
maximizador es único, su imagen también lo es; si hay empate o ausencia de
candidatos, ese estado se conserva. `QED`

## 6. Relación con la obstrucción por automorfismos

Para todo `alpha in Aut(C)`,

```text
alpha(M_cov(C)) = M_cov(C).
```

Si una órbita no trivial de cuádruplas alcanza la cobertura máxima, todos sus
miembros empatan. Ningún score invariante puede escoger uno de ellos. La política de
abstención implementa exactamente el criterio establecido en
`P1a_seleccion_intrinseca_y_automorfismos.md`.

La unicidad del máximo es suficiente para que la cuádrupla seleccionada sea fijada
por `Aut(C)`. No se afirma que sea frecuente en causal sets manifold-like.

## 7. Controles analíticos elementales

### 7.1 Posets sin una cadena suficientemente larga

Si `C` no contiene cuatro elementos `a prec b prec c prec d` con ambos intervalos de
cardinalidad al menos tres, entonces

```text
Q_3(C) = vacio
```

y la regla se abstiene como `UNDEFINED_NO_CANDIDATE`.

### 7.2 Cadena total

Sea `C_n` la cadena de `n` elementos. La cobertura máxima es `n`: se alcanza usando
el mínimo y el máximo de la cadena y cortándola entre dos elementos consecutivos,
siempre que cada bloque contenga al menos tres elementos.

El número de cortes máximos admisibles es

```text
n - 2 k_0 + 1 = n - 5.
```

Por tanto:

```text
n < 6 : UNDEFINED_NO_CANDIDATE,
n = 6 : UNIQUE_MAXIMIZER,
n > 6 : UNDEFINED_TIE.
```

Este comportamiento es deliberado. Un score basado en balance escogería un midpoint
en cadenas mayores, pero predeterminaría que los dos intervalos tengan tamaños casi
iguales. `F_cov,3` prefiere abstenerse antes que introducir ese resultado en la regla
de selección.

### 7.3 Simetrías ramificadas

Si dos ramas isomorfas producen pares de cobertura máxima, el automorfismo que
intercambia las ramas genera un empate. La salida puntual se abstiene y `G_cov,3`
retiene ambos candidatos.

### 7.4 Poset rígido

La rigidez elimina empates obligados por automorfismos, pero no excluye empates
accidentales de cobertura entre cuádruplas estructuralmente distintas. Tampoco en ese
caso se introduce un desempate secundario.

## 8. Qué significa aquí “no circular”

La separación conseguida es limitada pero exacta:

```text
seleccion: maximizar n_C(a,b) + n_C(c,d),
estimacion candidata posterior: usar L_C(a,b) / L_C(c,d).
```

El selector no contiene el estimador, su cociente ni una condición que lo fuerce a
ser `1`. Esto es **separación algebraica**, no independencia estadística.

Como cardinalidad y altura provienen del mismo poset y ambas responden a la geometría
latente, siguen abiertas:

- la distribución condicional de las alturas después de seleccionar;
- el sesgo por maximización de cobertura;
- la dependencia entre ambos intervalos;
- el efecto del espacio entre `b` y `c`;
- el borde de la región observada;
- y la estabilidad del selector al aumentar la densidad.

Ninguna prueba posterior podrá utilizar resultados de cadenas para justificar a
posteriori la elección de `S_cov` sin declarar una nueva versión del contrato.

## 9. Target provisional inducido

Cuando `F_cov,3(C)` está definido, puede escribirse el estadístico provisional

```text
R_L(C) = L_C(a,b) / L_C(c,d).
```

Para la salida conjuntista puede conservarse el multiconjunto

```text
R_set(C) = {
  L_C(a,b) / L_C(c,d) :
  (a,b,c,d) in M_cov(C)
}.
```

Estas expresiones son estadísticas observables del poset. Todavía no se les atribuye
el significado de una razón de tiempos propios. Esa atribución exigiría fijar una
familia geométrica y demostrar que los endpoints seleccionados poseen una contraparte
latente estable.

## 10. Criterios de fallo antes de P1b

El selector no debe promocionarse a estimador métrico si ocurre cualquiera de estas
situaciones:

1. la probabilidad de `UNDEFINED_NO_CANDIDATE` no se hace pequeña en la familia
   propuesta;
2. la probabilidad de `UNDEFINED_TIE` permanece grande;
3. cambios pequeños del poset producen cambios macroscópicos del par seleccionado;
4. la maximización concentra sistemáticamente los intervalos en el borde;
5. uno de los dos intervalos queda típicamente en el umbral mínimo;
6. el target latente cambia discontinuamente bajo perturbaciones pequeñas del
   embedding;
7. o la selección por cobertura determina asintóticamente una razón degenerada.

El cierre de este selector no cerraría P1: demostraría únicamente que esta
representación no es adecuada.

## 11. Próxima prueba teórica

Antes de cualquier simulación se debe escoger una familia generativa sencilla y
analizar:

```text
p_def(n,d)
  = P(|M_cov(C_n)|=1 | N=n,d),

p_empty(n,d)
  = P(Q_3(C_n)=vacio | N=n,d),

p_tie(n,d)
  = P(|M_cov(C_n)|>1 | N=n,d).
```

La puerta teórica adopta un diamante causal de Minkowski y conserva toda la ley
condicionada a `N=n`, sin condicionar adicionalmente a la existencia de cadenas. P1a
no presupone que el selector tenga buena cobertura en esa familia.

Por construcción,

```text
p_def(n,d) + p_empty(n,d) + p_tie(n,d) = 1.
```

Esta puerta teórica se desarrolla y resuelve parcialmente en:

```text
emergencia/P1a_puerta_teorica_en_Minkowski.md
```

El evento vacío queda identificado con altura menor que seis y se prueba que su
probabilidad tiende a cero. La separación selección única/empate queda reducida a un
conteo exacto de permutaciones en `d=2`, todavía no ejecutado.

## 12. Estado congelado

```text
P1A_COVERAGE_SELECTOR_DEFINITION = FROZEN_V0_1
P1A_MIN_INTERVAL_CARDINALITY = 3
P1A_INTERVAL_RELATION = STRICTLY_TEMPORALLY_ORDERED_AND_DISJOINT
P1A_PRIMARY_SCORE = TOTAL_COVERAGE_ONLY
P1A_SECONDARY_TIEBREAK = NONE
P1A_POINT_OUTPUT = UNIQUE_OR_ABSTAIN
P1A_SET_OUTPUT = ALL_MAXIMIZERS
P1A_CHAIN_RATIO = PROVISIONAL_OBSERVABLE_ONLY
P1A_EXACT_2D_ENUMERATION = COMPLETED_FROZEN_CONTRACT
P1A_MONTE_CARLO_EXECUTION = COMPLETED_D2_FROZEN_CONTRACT
P1A_THINNING_STABILITY = PASS
P1A_MINIMUM_SUPPORT_QUALITY = FAIL_PASS_THRESHOLD
P1A_STABILITY_GATE = INCONCLUSIVE_STABILITY_GATE
P1A_METRIC_RATIO_EXECUTION = NOT_RECOMMENDED
P1A_BALANCED_SUCCESSOR_COMPARISON = COMPLETED
P1A_BALANCED_SUCCESSOR = MIN_COVERAGE_LEX
P1A_BALANCED_SUCCESSOR_HEIGHT_GATE = PARK_LEX_HEIGHT_REPRESENTATION
P1A_HEIGHT_RATIO_PREREGISTRATION = NOT_AUTHORIZED
P1A_COUNT_VOLUME_REPRESENTATION = OPEN_BELOW_QUALIFICATION_THRESHOLD
P1A_HEIGHT_WIDTH_REPRESENTATION = PARKED
P1A_NOVELTY_CLAIM = NO
```

La enumeración y simulación autorizadas se documentan en
`emergencia/P1a_resultados_enumeracion_y_monte_carlo_d2.md`. El terminal
`POINT_SELECTOR_OPERATIONALLY_VIABLE` se refiere solo a frecuencia de salida única;
no promueve `R_L` a observable métrico validado.

El gate posterior se documenta en
`emergencia/P1a_resultados_estabilidad_y_sesgo_d2.md`. La cuádrupla es estable bajo
thinning, pero el criterio 5 de §10 se activa descriptivamente: en `n=64,96,128`, la
probabilidad de que el intervalo menor tenga cardinalidad tres está entre 0.74 y
0.78. El terminal congelado es `INCONCLUSIVE_STABILITY_GATE`; no se modifica
retroactivamente `F_cov,3` y no se ejecuta aún el cociente de alturas.

La comparación de sucesores se completó en
`emergencia/P1a_resultados_comparacion_selectores_balanceados_d2.md`. No cambia el
resultado histórico de `F_cov,3`: selecciona una regla nueva,
`MIN_COVERAGE_LEX`, para el siguiente gate de alturas. El cociente métrico continúa
cerrado.

Ese gate se completó en `emergencia/P1a_resultados_gate_altura_duracion_lex_d2.md`.
La calibración media y la estabilidad del target pasan, pero la resolución individual
altura–duración falla de forma fuerte. `MIN_COVERAGE_LEX` no se promociona a un
cociente de alturas en el régimen evaluado.

Las representaciones alternativas se evalúan en
`emergencia/P1a_resultados_representaciones_alternativas_d2.md`. El conteo interno
mejora la resolución frente a altura y altura–anchura, pero permanece por debajo del
gate y plantea circularidad porque el selector también usa cardinalidades.
