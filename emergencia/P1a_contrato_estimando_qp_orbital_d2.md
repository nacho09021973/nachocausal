# P1a — Contrato del estimando orbital bajo thinning en `d=2`

> **ESTADO: ESTIMANDO CONGELADO v1.0 · SOLO DOCUMENTO · SIN EJECUCIÓN
> AUTORIZADA · `Xi_n`, MÉTRICA ENTRE PARES Y BANDA NULA FUERA DE ALCANCE.**
>
> Fecha de congelación: 26 de agosto de 2026.

Este contrato fija únicamente qué significa `q_p` para el falsador piloto exacto
en `n<=9`. No autoriza implementar el cálculo, ejecutar enumeraciones, buscar
pares, escoger una métrica después de observar resultados ni reutilizar los
estados históricos `EMPTY/UNIQUE/TIE` con una semántica nueva.

La base semántica local de este contrato es:

- `emergencia/p1a_tie_aut_diagnostic.py`, para materializar `M(C)`, enumerar
  `Aut(C)` y construir la partición orbital exacta;
- `emergencia/resultados/p1a_tie_aut_exacto_d2.json`, para la descomposición
  congelada `UNIQUE/TIE_AUT_ONLY/TIE_NONAUT`;
- `emergencia/p1a_estabilidad_d2.py::induced_permutation`, reutilizable solo
  como operación de inducción y reranking, no como selector posterior.

## 1. Dominio y selector

Sea `sigma in S_n`. Su permutación representa el `2-order` estricto

```text
i <_{C_sigma} j  iff  i<j y sigma(i)<sigma(j).
```

Se conserva sin cambios el selector `MIN_COVERAGE_LEX`, con `K0=3`. Para una
cuádrupla admisible `x=(a,b,c,d)`, con

```text
a prec b prec c prec d,
|[a,b]|>=3,
|[c,d]|>=3,
```

su score es

```text
S(C,x) = (min(|[a,b]|,|[c,d]|), |[a,b]|+|[c,d]|),
```

maximizado en orden lexicográfico. Se define

\[
M(C):=\operatorname{Argmax}_x S(C,x).
\]

`M(C)` es el conjunto completo de maximizadores. Este contrato no usa el
selector histórico `F_cov,3` ni su score de cobertura total.

## 2. Número orbital e indicador de unicidad orbital

`Aut(C)` es el grupo de todos los relabelings de los elementos que preservan la
relación estricta. Actúa componente a componente sobre `M(C)`:

\[
\alpha\cdot(a,b,c,d)
=(\alpha(a),\alpha(b),\alpha(c),\alpha(d)).
\]

Se congelan dos símbolos distintos:

\[
\rho(C):=|M(C)/\operatorname{Aut}(C)|,
\]

con la convención `rho(C)=0` si `M(C)=emptyset`, y

\[
r_{\rm orb}(C)
:=\mathbf 1\{M(C)\ne\varnothing,\ \rho(C)=1\}.
\]

Por tanto,

```text
r_orb(C)=1  iff  diagnostic_state in {UNIQUE,TIE_AUT_ONLY};
r_orb(C)=0  if   diagnostic_state == TIE_NONAUT;
r_orb(C)=0  if   M(C) is empty.
```

`STATE_UNIQUE` conserva su significado histórico: `|M(C)|=1`. No se renombra,
no se amplía y no se usa como sustituto de `r_orb`.

## 3. Operación de thinning

Para una retención `p in [0,1]`, sean

\[
Z_i\overset{\mathrm{iid}}\sim\operatorname{Bernoulli}(p),
\qquad
A:=\{i:Z_i=1\}.
\]

`R_p(sigma)` es el subposet inducido `C_sigma[A]`. Volver a rankear los valores
retenidos para obtener una permutación inducida es solo una representación del
mismo subposet; no añade un criterio de selección.

Después del thinning se recalculan desde cero:

1. el conjunto de candidatos admisibles;
2. sus scores `MIN_COVERAGE_LEX`;
3. el nuevo conjunto completo de maximizadores;
4. los automorfismos del subposet inducido;
5. su partición orbital.

No se condiciona a la supervivencia de los maximizadores ni de los endpoints del
poset original. Tampoco se restringe la nueva búsqueda a candidatos procedentes
de `M(C_sigma)`.

Si el subposet retenido tiene menos de seis elementos, no puede contener dos
intervalos cerrados disjuntos en cadena con cardinalidad al menos tres. En ese
caso `M(R_p(sigma))=emptyset`, `rho=0` y `r_orb=0`.

## 4. Estimando principal: `EMPTY=0`

Para cada `sigma` fija, la única aleatoriedad de este estimando es la máscara de
thinning:

\[
q_p(\sigma)
:=\Pr\!\left(
r_{\rm orb}(R_p(\sigma))=1
\mid \sigma
\right).
\]

Equivalentemente,

\[
q_p(\sigma)
=\sum_{A\subseteq[n]}
p^{|A|}(1-p)^{n-|A|}
r_{\rm orb}(C_\sigma[A]).
\]

`EMPTY` aporta cero a esta suma. Esta es la convención primaria porque la pérdida
de todos los candidatos bajo coarse-graining forma parte de la estabilidad que se
quiere medir.

Los extremos de control son

\[
q_0(\sigma)=0,
\qquad
q_1(\sigma)=r_{\rm orb}(C_\sigma).
\]

## 5. Diagnóstico auxiliar condicionado a disponibilidad

Se define primero

\[
e_p(\sigma)
:=\Pr\!\left(
M(R_p(\sigma))\ne\varnothing
\mid\sigma
\right).
\]

Solo cuando `e_p(sigma)>0` se define

\[
q_p^\star(\sigma)
:=\Pr\!\left(
\rho(R_p(\sigma))=1
\mid M(R_p(\sigma))\ne\varnothing,\sigma
\right)
=\frac{q_p(\sigma)}{e_p(\sigma)}.
\]

Si `e_p(sigma)=0`, `q_p^star(sigma)` es `NA`, no cero. Todo reporte futuro de
`q_p^star` deberá incluir `e_p`; el diagnóstico condicionado no puede sustituir
al estimando principal ni ocultar pérdida de disponibilidad.

## 6. Evaluación exacta autorizable para `n<=9`

El piloto pequeño se define mediante suma exacta sobre las `2^n` máscaras, no
mediante Monte Carlo. Para

\[
a_k(\sigma)
:=|\{A\subseteq[n]:|A|=k,\ r_{\rm orb}(C_\sigma[A])=1\}|,
\]

y

\[
b_k(\sigma)
:=|\{A\subseteq[n]:|A|=k,\ M(C_\sigma[A])\ne\varnothing\}|,
\]

se tiene

\[
q_p(\sigma)=\sum_{k=0}^n a_k(\sigma)p^k(1-p)^{n-k},
\]

\[
e_p(\sigma)=\sum_{k=0}^n b_k(\sigma)p^k(1-p)^{n-k}.
\]

Los coeficientes `a_k` y `b_k` contienen conteos de subconjuntos, no frecuencias
normalizadas. Esta representación congela la función completa de `p`; no obliga a
escoger una rejilla de retenciones antes de definir el estimando.

Al ser exacto, este piloto no tiene escala de error Monte Carlo en `q_p`. Por
tanto, la estadística normalizada por una banda nula de dos estimaciones MC no
pertenece a este contrato. Seguirá siendo necesaria para una eventual campaña
aproximada de mayor tamaño, bajo otro contrato.

## 7. Obligaciones antes de cualquier ejecución

Una implementación futura deberá, como mínimo:

- usar únicamente `MIN_COVERAGE_LEX` después de cada thinning;
- tratar cada subconjunto retenido como subposet inducido y verificar que el
  reranking preserva exactamente sus comparabilidades;
- materializar el `M(C)` completo antes de formar órbitas;
- reproducir por separado casos `EMPTY`, `UNIQUE`, `TIE_AUT_ONLY` y
  `TIE_NONAUT` ya conocidos;
- verificar `q_0=0` y `q_1=r_orb(C_sigma)`;
- contrastar la suma directa sobre máscaras con los polinomios definidos por
  `a_k` y `b_k`;
- producir `NA`, nunca cero, para `q_p^star` cuando `e_p=0`;
- rechazar cualquier dependencia de etiquetas, coordenadas latentes o del
  conjunto de maximizadores anterior al thinning.

Estas obligaciones no autorizan todavía escribir ni ejecutar esa implementación.

## 8. Objetos deliberadamente no congelados

Quedan fuera de este contrato:

- la definición conjunta de `Xi_n`;
- la métrica o pseudométrica en espacio-`Xi`;
- la regla para escoger pares `(sigma,tau)`;
- la función de `p` que se compararía entre pares;
- cualquier máximo sobre muchos pares y su corrección por multiplicidad;
- una banda nula Monte Carlo para una futura estimación aproximada;
- retenciones concretas para una campaña posterior;
- un backend escalable de automorfismos para `n>9`;
- cualquier conclusión WALL o NO-WALL.

No se buscarán pares ni se diseñará el falsador final hasta que `Xi_n`, su métrica
y la regla de búsqueda hayan quedado congelados sin observar `q_p`.

## 9. Techo de afirmación y estado operativo

Este documento define una probabilidad de unicidad orbital bajo thinning
independiente para un selector combinatorio concreto. No demuestra estabilidad,
coarse-graining físico, dinámica de renormalización, metastabilidad, WALL,
NO-WALL ni relevancia asintótica.

```text
P1A_QP_ESTIMAND_VERSION = 1.0
P1A_QP_SELECTOR = MIN_COVERAGE_LEX
P1A_QP_PRIMARY_EMPTY_POLICY = ZERO
P1A_QP_AUXILIARY_EMPTY_POLICY = CONDITION_AND_REPORT_AVAILABILITY
P1A_QP_PILOT_MAX_N = 9
P1A_QP_PILOT_EVALUATION = EXACT_MASK_SUM
P1A_QP_ESTIMAND_STATUS = FROZEN_DOCUMENT_ONLY
P1A_QP_IMPLEMENTATION_AUTHORIZED = NO
P1A_QP_EXECUTION_AUTHORIZED = NO
P1A_XI_N_STATUS = NOT_LOCATED_NOT_FROZEN
P1A_PAIR_METRIC_STATUS = NOT_FROZEN
P1A_PAIR_SEARCH_AUTHORIZED = NO
P1A_LARGE_N_MONTE_CARLO_AUTHORIZED = NO
```
