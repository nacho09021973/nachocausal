# P1a — Contraejemplo al grado lineal por una transposición

## Estado y techo de claim

```text
RESULT = CONSTRUCTIVE_COUNTEREXAMPLE_TO_SINGLE_TRANSPOSITION_LINEAR_OUTDEGREE
FINITE_BASE = EXACT_COMPUTER_ASSISTED_WITH_GUARDS
ASYMPTOTIC_LIFT = ANALYTIC
SELECTOR_CHANGED = NO
GENERAL_TRANSPORT_INEQUALITY_REFUTED = NO
THINNING_RG_CLAIM = NONE
```

Este resultado refuta únicamente la ruta que relaciona una configuración mala
con sus vecinas buenas obtenidas mediante **una transposición** y que requiere un
grado de salida mínimo lineal. No refuta una comparación de cardinalidades
`|B_n| <= C |G_n|` obtenida mediante otras relaciones, fibras o cirugías.

## Definiciones

Para una permutación etiquetada `sigma` sea

```text
M(sigma) = argmax_q S_MIN_COVERAGE_LEX(C_sigma,q),
r(sigma) = |M(C_sigma)/Aut(C_sigma)|,
G_n = {sigma in S_n : M(sigma) != empty and r(sigma)=1},
B_n = {sigma in S_n : r(sigma)>=2}.
```

Para `sigma in B_n`, el grado bueno por transposiciones es

```text
g_n(sigma) = #{(i,j) : i<j and sigma o (i,j) in G_n}.
```

La relación causal implementada es el orden producto

```text
i <_C j  iff  i<j and sigma[i]<sigma[j].
```

`C_ab` es la cardinalidad del intervalo cerrado: el número de puntos dentro del
rectángulo inclusivo con esquinas `(a,sigma[a])` y `(b,sigma[b])`. El score
implementado para `(a,b,c,d)` es

```text
(min(C_ab,C_cd), C_ab+C_cd)
```

en orden lexicográfico, con `C_ab,C_cd >= K0=3`.

## Entrada finita certificada

Fijamos

```text
kappa = (0,1,2,4,5,7,3,6).
```

El diagnóstico exacto da

```text
M(kappa) = {(0,2,3,5), (0,2,3,7)},
r(kappa) = 2,
```

con ambas órbitas unitarias. Para la cirugía genérica `D_x`, realizada con diez
gemelos intermedios, el vector exacto es

```text
(r(D_x(kappa)))_{x=0}^7 = (2,0,0,0,0,2,2,2).
```

En particular `a(kappa)=#{x:r(D_x(kappa))=1}=0`. Este hecho está protegido por
`tests/test_p1a_tie_aut_generic_cross.py` y procede del artefacto exacto
`emergencia/resultados/p1a_tie_aut_generic_cross_exact_n7_n9.json`.

## Familia adversarial

Para cada `k>=0` definimos

```text
sigma_(8+k) = (kappa[0]+k,...,kappa[7]+k,k-1,k-2,...,0).
```

Los ocho puntos del núcleo aparecen antes que el padding y tienen valores
mayores. Por tanto no hay comparabilidades núcleo--padding. El bloque decreciente
es una antichain y

```text
C_sigma = C_kappa disjoint_union A_k.
```

El poset `C_kappa` es conexo y tiene altura seis, mientras que cada punto de
`A_k` es aislado. Todo automorfismo preserva el componente del núcleo. En
consecuencia `M` y su partición orbital son los de `kappa`, de modo que

```text
sigma_(8+k) in B_(8+k)  for every k>=0.
```

## Clasificación exhaustiva de una transposición

Toda transposición pertenece exactamente a una de las tres clases siguientes.

### 1. Núcleo--núcleo

Solo existen

```text
binom(8,2)=28
```

pares. Tras cualquiera de ellos el padding sigue siendo una antichain disjunta.
No es necesario decidir cuáles reparan el núcleo para obtener la cota uniforme:

```text
g_core-core <= 28.
```

### 2. Padding--padding

Sean `y<z` dos posiciones dentro del bloque decreciente. Después de intercambiar
sus valores, las únicas relaciones nuevas del padding son

```text
p_y < p_j < p_z  for y<j<z,
```

además de su cierre transitivo; los otros puntos siguen aislados. El componente
nuevo tiene altura como máximo tres y continúa disjunto del núcleo. No puede
contener una cadena candidata de cuatro elementos.

El componente del núcleo, de altura seis, es invariante bajo automorfismos. Por
tanto `M` y sus dos órbitas no cambian:

```text
g_pad-pad = 0.
```

### 3. Núcleo--padding

Intercambiemos el índice `x` del núcleo con la posición `y` del padding, contando
`y=0` desde el comienzo del bloque decreciente. El valor pequeño trasladado al
nucleo define `L`, el valor grande trasladado al padding define `H`, y los `y`
puntos anteriores del padding forman una clase de gemelos `T_y` con

```text
L < T < H,
strict_past(T) = {L},
strict_future(T) = {H}.
```

Los puntos posteriores a `y` son aislados. Ningún `T` puede pertenecer a una
cadena de cuatro elementos: solo tiene un predecesor y un sucesor estrictos.

La multiplicidad `|T_y|` tampoco altera el score de ningún candidato. Un gemelo
solo puede pertenecer al intervalo `[L,H]`; pero `(L,H)` no puede ser `(a,b)` ni
`(c,d)` en una cadena `a<b<c<d`, pues `L` no tiene predecesor estricto y `H` no
tiene sucesor estricto. Todos los conjuntos de candidatos y sus scores dependen
solo del esqueleto finito formado por el núcleo modificado y `H`.

Si `y>=10=m+2`, la clase gemela contiene más elementos que los nueve vértices
no gemelos del componente. Los puntos posteriores, aunque puedan ser numerosos,
son componentes aislados con pasado y futuro vacíos y no pueden mezclarse con
`T_y`. Tampoco existe fuera de `T_y` otra clase no aislada de tamaño `y`. Por
tanto `T_y` es setwise invariante bajo automorfismos y los puntos aislados actúan
trivialmente sobre candidatos. Al colapsar la clase gemela se obtiene exactamente
el diagnóstico coloreado `D_x(kappa)`, con independencia de `y` y de `k`.

Como ninguno de los ocho valores de `r(D_x(kappa))` es uno, ninguna transposición
con `y>=10` llega a `G_(8+k)`. Solo pueden reparar las diez posiciones de frontera
`y=0,...,9`, por lo que

```text
g_cross <= 8*10 = 80.
```

## Teorema

Para todo `k>=0`,

```text
sigma_(8+k) in B_(8+k)
```

y

```text
g_(8+k)(sigma_(8+k))
  = g_core-core + g_pad-pad + g_cross
  <= 28 + 0 + 80
  = 108.
```

Por tanto

```text
g_(8+k)(sigma_(8+k))/(8+k) <= 108/(8+k) -> 0.
```

Para cualquier `c>0` y cualquier `N`, basta escoger
`k>max(N-8,108/c-8)` para obtener un elemento de `B_(8+k)` cuyo grado bueno es
menor que `c(8+k)`. En consecuencia es falsa la afirmación

```text
exists c>0,N such that
min_{sigma in B_n} g_n(sigma) >= c*n for every n>=N.
```

## Consecuencia metodológica

La cota de congestión de entrada `b_n(tau)` ya no puede rescatar esta relación:
falla primero la condición necesaria de grado de salida lineal. El contraejemplo
no autoriza inferencias sobre transportes de mayor radio, relaciones multivaluadas
distintas, comparaciones de fibras ni el comportamiento asintótico de `p_n`.

## Provenance

```text
BASE_HEAD = a716bc128abef12f47b403fede1867c1d85bea2c
TIE_AUT_SOURCE_SHA256 = 5614a5f33da0611170aaf5e77f24f2f19b646ec3f3559191c21d74fed402b7b4
TIE_AUT_FROZEN_ARTIFACT_SHA256 = 1bd9d882337b0aec56ff1bf87b0dd8de2fa415dc50b494eddb3bcfa4cf5c68f3
GENERIC_CROSS_SOURCE_SHA256 = 1e3fb2362dfefb6059e7ad6eb1757fdd65c82ac6b4d16b25f29511849a28755f
GENERIC_CROSS_EXACT_RUNNER_SHA256 = c808d3d36351eb4c8a56237bb74941d57834d76592af3ababeb3745dcf1b8158
GENERIC_CROSS_EXACT_ARTIFACT_SHA256 = ed0e90614f1b1285cd0773b6de43dbdb6435a937f09bd96351d9ac98143c54e2
NEW_DEPENDENCIES = NONE
NEW_FACTORIAL_RUN_FOR_THIS_PROOF = NO
```
