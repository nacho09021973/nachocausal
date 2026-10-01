# P1a — Abundancia de núcleos resistentes: primera comparación de fibras

## Estado y techo de claim

```text
FINITE_N8_FIBRE_AUDIT = EXECUTED_WITH_GUARDS
EXPLICIT_ANTICHAIN_PADDED_FIBRE = PROVABLY_NEGLIGIBLE_INSIDE_B_N
ALL_A_ZERO_CORES_NEGLIGIBLE = NOT_ESTABLISHED
ALMOST_EVERYWHERE_TRANSPORT = OPEN
ASYMPTOTIC_CLAIM_FROM_N8_N9_FREQUENCIES = NONE
```

El objetivo es separar la abundancia del poset concreto
`C_kappa disjoint_union A_k` de la abundancia de cualquier mecanismo más amplio
que produzca realizadores con `a=0` o grado de transposición sublineal.

## Definiciones y medida

La medida sigue siendo uniforme sobre permutaciones etiquetadas `S_n`. Definimos

```text
R_n = {kappa in B_n : a(kappa)=0}.
```

La propiedad `B_n` es intrínseca al poset. En cambio, `a(kappa)` incluye una
cirugía sobre el realizador de permutación y no se supone invariante por
isomorfismo del poset.

## Auditoría exacta de las fibras en n=8

El cálculo exacto reproduce

```text
|B_8| = 71,
|R_8| = 14.
```

La canonicalización exacta local agrupa `B_8` en 37 clases de isomorfismo de
posets. Los 14 realizadores con `a=0` ocupan ocho clases distintas:

```text
B_8 isomorphism fibres:       37
a=0 isomorphism fibres:        8
pure a=0 fibres:               6
mixed fibres containing a=0:   2
```

Todas las ocho fibras que contienen `a=0` tienen tamaño dos. En seis, ambos
realizadores tienen `a=0`; en dos, uno tiene `a=0` y el otro `a=1`. Por tanto:

```text
a(kappa) is not a poset-isomorphism invariant.
```

El testigo

```text
kappa = (0,1,2,4,5,7,3,6)
```

pertenece a una fibra pura de tamaño dos, cuyo otro realizador es

```text
(0,1,2,6,3,4,7,5).
```

Este resultado impide explicar `14/71` como una única clase de poset con una
fibra grande, pero sigue siendo estrictamente finito y no implica persistencia
de una fracción positiva.

## Lema de fibra para una componente conexa más aislados

Sea `P` un poset de permutación cuyo grafo de comparabilidades es conexo y tiene
`m>=2` elementos. Sea `F(P)` el número de permutaciones de longitud `m` que
realizan un poset isomorfo a `P`. Entonces

```text
F(P disjoint_union A_k) = F(P) * (k+1).
```

### Demostración

Considérese un realizador de `P disjoint_union A_k`. Si un punto aislado apareciera
entre dos posiciones del bloque `P`, dividiría sus vértices en conjuntos no
vacíos `L` y `R`. La incomparabilidad con el aislado obliga a

```text
value(u) > value(isolated) > value(v)
for every u in L and v in R.
```

No existiría ninguna comparabilidad entre `L` y `R`, contradiciendo la conexidad
del grafo de comparabilidades de `P`. Por tanto los vértices de `P` ocupan un
bloque contiguo.

Los aislados se dividen de forma única en `ell` puntos anteriores y `k-ell`
posteriores, con `ell=0,...,k`. Los anteriores deben usar los valores mayores que
todo el núcleo; los posteriores, los menores. Como son mutuamente incomparables,
sus valores aparecen necesariamente en orden decreciente. Para cada realizador
interno de `P` y cada `ell` existe exactamente una permutación. Esto prueba el
lema.

## Aplicación al núcleo resistente

El poset del testigo es conexo y su fibra exacta en `S_8` tiene tamaño dos. En
consecuencia,

```text
#{sigma in S_(8+k) : C_sigma isomorphic to C_kappa disjoint_union A_k}
  = 2*(k+1).
```

Todas estas permutaciones pertenecen a `B_(8+k)`, porque el componente del núcleo
es distinguido por su altura y conserva las dos órbitas máximas.

## Una cota inferior exponencial para B_(8+k)

Para `t=floor(k/2)`, partimos la permutación decreciente de longitud `k` en `t`
pares consecutivos. En cada par elegimos independientemente mantener el orden
decreciente o intercambiarlo. Los valores de un par anterior siguen siendo
mayores que todos los de un par posterior.

Cada una de las `2^t` decoraciones resultantes es una unión disjunta de
componentes de uno o dos elementos y tiene altura como máximo dos. Al colocarla
en skew sum debajo de `kappa`, no crea candidatos ni modifica `M(C_kappa)`. El
componente del núcleo, de altura seis, no puede mezclarse por automorfismos con
la decoración. Por tanto todas las permutaciones construidas están en
`B_(8+k)` y

```text
|B_(8+k)| >= 2^floor(k/2).
```

Combinando ambas fórmulas,

```text
  #{C_kappa disjoint_union A_k realizers} / |B_(8+k)|
  <= 2*(k+1) / 2^floor(k/2)
  -> 0.
```

## Conclusión exacta

La familia isomorfa explícita `C_kappa disjoint_union A_k` es despreciable dentro
de `B_(8+k)`. El contraejemplo al grado mínimo sigue siendo válido, pero esa sola
fibra no amenaza un transporte almost-everywhere.

Esto **no** demuestra que todos los núcleos resistentes sean despreciables. Los
ocho tipos isomorfos ya presentes en `n=8`, junto con la dependencia de `a` del
realizador, muestran que el conjunto relevante es más amplio que una clase fija.
El lema que falta es decidir si existe una familia de decoraciones con entropía
exponencial que preserve `a=0` o grado de salida sublineal, o demostrar que toda
familia de ese tipo admite una descripción de cardinalidad `o(|B_n|)`.

## Provenance

```text
FIBRE_RUNNER = emergencia/p1a_tie_aut_resistant_fibers_n8.py
FIBRE_ARTIFACT = emergencia/resultados/p1a_tie_aut_resistant_fibers_n8.json
FIBRE_ARTIFACT_SHA256 = e23e69525366f9a8c37875aa5f026af7fc0091615cebc561e4ba2282addcb7c5
CANONICALIZATION = dev/r3_bridge_e_fibers.py
NEW_DEPENDENCIES = NONE
N10_RUN = NO
ASYMPTOTIC_FIT = NONE
```
