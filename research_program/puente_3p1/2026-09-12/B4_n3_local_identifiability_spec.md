# B4 — Especificación de auditoría de identificabilidad local a `n=3`

> **STATUS: `PARKED / N3_RANK_UNRESOLVED / NO_REOPENING_WORK`.**
> **POINT:** el mismo `lambda* = lambda(t0)` de B2/B3.

## 1. Espacio físico congelado

Se conserva el chart de rango tres de B3,

```text
x=(I1,I2,I3)=(v1/v0, u_in/u_out, u_in*v1),
v0=0.35,
lambda*=(0.35,0.9,1.5,0.7,0.1),
x*=(2.5714285714,0.4666666667,0.63).
```

No se permite cambiar el punto, introducir una nueva curva o volver a los cinco parámetros brutos
de `lambda` como coordenadas físicas.

## 2. Ley completa a `n=3`

La reducción exacta previa está cerrada en `B4_0_n3_moment_reduction.md`: no hace falta empezar
por una integral triple sobre las cinco clases.

Hay exactamente cinco clases de poset no etiquetado:

```text
A  antichain                         (0 comparabilities)
E  one relation + isolated point     (1 comparability)
V  one minimal element, two maxima    (2 relations)
Lambda  two minima, one maximal       (2 relations)
C  three-chain                        (3 relations)
```

Se define

```text
p^(3)(x) = (p_A,p_E,p_V,p_Lambda,p_C),
sum_a p_a = 1.
```

Por tanto sólo cuatro componentes son independientes, por ejemplo
`q=(p_E,p_V,p_Lambda,p_C)`, con `p_A=1-sum(q)`.

Para el núcleo radial `w(U,V)=G(UV)` y el kernel causal angular `H` de B1.2, cada probabilidad
tiene la forma exacta

```text
p_a(x) = Z(x)^(-3) integral_{K_x^3} w1 w2 w3 K_a(omega1,omega2,omega3;
                                                       radial_1,radial_2,radial_3)
                                                       d^2z1 d^2z2 d^2z3,
```

donde `K_a` es la indicatriz de que el poset inducido por las tres relaciones causales pertenece
a la clase `a`, y `Z=integral_K w`. Las integrales angulares están acopladas: no se sustituyen
por tres copias independientes de la probabilidad de comparabilidad de B1.

## 3. Criterio diferencial

Sea `Dq(x*)` la matriz `4 x 3` de diferenciales de las componentes independientes. La condición
necesaria y suficiente para que `phi` sea localmente función de la ley `n=3` es

```text
ker Dq(x*) subset ker dphi(x*)
```

Equivalentemente,

```text
dphi(x*) in rowspan(Dq(x*)).
```

El resultado más fuerte sería

```text
rank Dq(x*) = 3
```

que daría identificabilidad local de los tres parámetros físicos. El resultado mínimo perseguido
es sólo la pertenencia de `dphi` al espacio fila; no se afirma que eso identifique toda la familia.

## 4. Terminales previstos

```text
B4_STRONG_POSITIVE
    rank Dm = 3
    => full local identifiability of the 3D physical family
    => phi locally reconstructible

B4_PHI_FIRST_ORDER_POSITIVE
    rank Dm < 3 and dphi in rowspan(Dm)
    => no first-order invisible direction for phi
    => NOT YET local reconstruction of phi

B4_NEGATIVE_FOR_PHI
    exists v: Dm v = 0 and dphi(v) != 0

B4_INCONCLUSIVE_BY_BOUNDS
    the differential/rank enclosure is not decisive
```

Un terminal negativo motivaría estudiar `n=4` u otra estadística de la ley; no autoriza por sí
solo escoger un nuevo punto. Ningún terminal equivale a reconstrucción global.

## 5. Gobernanza

```text
B4.0_N3_MOMENT_REDUCTION = VERIFIED
B4_EXECUTION = PARKED
```

```text
B4_SPECIFICATION = AUTHORIZED
B4_EXECUTION = AUTHORIZED
N3_MONTE_CARLO = NOT_AUTHORIZED
PARAMETER_SEARCH = NOT_AUTHORIZED
NEW_WITNESS_POINT = NOT_AUTHORIZED
```

La ejecución queda aparcada. Sólo puede reabrirse si aparece una cuadratura certificada con resto
formal para las integrales concretas de B4.3, manteniendo punto, chart, escalado y familia.

## Primera ejecución

La evaluación determinista preliminar del menor `(rho,E[f^2],E[p^2])` produce
`-8.26e-13`, pero sin una envolvente certificada. El terminal correcto es:

```text
B4_INCONCLUSIVE_BY_BOUNDS
```

Esto no demuestra `rank Dm<3`; tampoco autoriza un terminal negativo. El artefacto queda en
`verification_b4_execution.json`.

## Terminal canónico

```text
B1 = POSITIVE_3P1_ORDER_NONDEGENERACY
B2 = POSITIVE_LOCAL_IDENTIFIABILITY_ON_FROZEN_PATH
B3 = NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY
B4 = PARKED
N3_RANK = UNRESOLVED
B4_REOPEN_ONLY_IF = CERTIFIED_QUADRATURE_WITH_FORMAL_REMAINDER
```

No se construirá una biblioteca general de cuadratura intervalar ni se abrirán `n=4`, nuevos
puntos, charts, escalados, rescates por diferencias finitas o Monte Carlo.
