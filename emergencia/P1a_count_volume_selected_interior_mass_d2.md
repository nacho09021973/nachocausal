# `NC-2C` — masa interior uniforme bajo selección única

> **ESTADO: TEOREMA PROBADO · `NC2C-O2` CERRADO · CANAL `fixed-n`, `d=2` ·
> PURAMENTE DEDUCTIVO · SIN DATOS, SIMULACIONES, SEMILLAS, CÓDIGO NI ARTEFACTOS
> NUMÉRICOS NUEVOS · `NC2B-O3` NO ABIERTO.**

Autorización firmada:
`docs/program_reopening_note_2026-08-17_nc2c_selected_interior_mass_DRAFT.md`.

## 1. Objeto, fuentes y resultado

Para una permutación uniforme `Pi_n`, sea `S` el evento de que
`MIN_COVERAGE_LEX` tenga un maximizador único en

\[
Q_3(C)=\{(a,b,c,d):a\prec b\prec c\prec d,
|[a,b]|\ge3,\ |[c,d]|\ge3\}.
\]

Si el ganador es `q*`, se escriben

\[
M_{\rm PAST}=|[a,b]|,
\qquad
M_{\rm FUTURE}=|[c,d]|.
\]

`NC-2B` ya demostró que `Pr_n(S)>0` para todo `n>=6`. Esta nota vuelve a
demostrar, y no importa como teorema, toda propiedad específica del selector que
necesita. Del registro anterior solo usa:

1. la representación de orden producto, los intervalos cerrados y el selector
   congelado, comprobables directamente en
   `p1a_enumeracion_simulacion.py` y `p1a_comparar_selectores_d2.py`;
2. la observación abstracta de que, condicionada a asignaciones prescritas de una
   permutación, la biyección restante es uniforme; se prueba de nuevo en §4;
3. ninguna conclusión selector-específica de EF-4/EF-7 ni de la antigua familia
   prescrita, cuyos certificados permanecen degradados.

El resultado es explícito.

**Teorema `NC2C-O2`.** Para

\[
\boxed{
\varepsilon=\frac3{100},
\qquad p=\frac12,
\qquad n_0=10^{40},}
\tag{1.1}
\]

todo entero `n>=n_0` y ambos lados `h in {PAST,FUTURE}` satisfacen

\[
\Pr\!\left\{
\frac{3n}{100}\le M_h\le\frac{97n}{100}
\mathrel{\Big|} n,h,S
\right\}\ge\frac12.
\tag{1.2}
\]

Las constantes son deliberadamente conservadoras. No se eligieron a partir de
los tamaños sellados.

## 2. Dualidad exacta entre lados

Para una permutación escrita con rangos `1,...,n`, defínase

\[
(D\pi)(i)=n+1-\pi(n+1-i).
\tag{2.1}
\]

La rotación de 180 grados

\[
(i,\pi(i))\longmapsto(n+1-i,n+1-\pi(i))
\]

es una biyección de \(\mathfrak S_n\) y revierte el orden producto. Una cadena
`a prec b prec c prec d` se transforma, en el orden correcto, en

\[
Dd\prec Dc\prec Db\prec Da.
\]

El intervalo pasado de la cadena transformada es la imagen del intervalo futuro
original, y recíprocamente. Por tanto intercambia `M_PAST` y `M_FUTURE`. Como

\[
(\min(m_-,m_+),m_-+m_+)
\]

es simétrico en ambos lados, `D` preserva el número de maximizadores y el evento
`S`. En consecuencia, para todo `n` y `epsilon`,

\[
R_{n,{\rm PAST}}(\varepsilon)
=R_{n,{\rm FUTURE}}(\varepsilon).
\tag{2.2}
\]

La prueba posterior produce interioridad simultánea y no necesita apoyarse en
esta reducción, pero (2.2) cierra de forma exacta la obligación de ambos lados.

## 3. Concentración autocontenida para rectángulos de una permutación

Se necesitará dos veces la misma cota, una para la permutación completa y otra
para una biyección residual.

**Lema 3.1.** Sea `pi` una biyección uniforme entre dos conjuntos ordenados de
`N` elementos. Para subconjuntos fijos `I,J`, sea

\[
X=|\{i\in I:\pi(i)\in J\}|.
\]

Entonces

\[
\mathbb E X=\frac{|I||J|}{N},
\qquad
\Pr\{|X-\mathbb EX|\ge t\}
\le2\exp\!\left(-\frac{t^2}{2N}\right).
\tag{3.1}
\]

**Demostración.** `pi(I)` es una muestra uniforme sin reemplazo de tamaño
`|I|`; `X` es el número de elementos marcados por `J`, lo que da la media.
Revélense los elementos de la muestra uno a uno y sea `Z_k` la esperanza
condicionada final de `X` tras `k` revelaciones. Si antes del paso quedan `R`
elementos, `K` de ellos marcados, y `m` extracciones por hacer, el incremento del
martingala al observar `Y in {0,1}` es

\[
\frac{R-m}{R-1}\left(Y-\frac KR\right),
\]

cuyo valor absoluto es a lo sumo uno. Hay como máximo `N` incrementos. La prueba
exponencial elemental de Azuma —aplicar el lema de Hoeffding condicional a cada
incremento centrado y multiplicar las cotas— da (3.1). Si no queda aleatoriedad,
el enunciado es trivial. `QED`

Hay menos de `N^2` intervalos en cada eje y, por tanto, menos de `N^4` pares de
intervalos. Con

\[
\eta_N=\sqrt{20N\log n},
\]

la unión de (3.1) da

\[
\Pr\left\{
\max_{I,J}\left|X_{I,J}-\frac{|I||J|}{N}\right|>\eta_N
\right\}
\le 2n^{-6},
\tag{3.2}
\]

si `N<=n`. La unión se toma sobre intervalos deterministas antes de elegir
endpoints; por eso controla simultáneamente todo rectángulo adaptativo posterior.

## 4. Una familia nueva con masa de selección subexponencial

Esta sección prueba desde cero la única cota de `Pr(S)` que se usará. No promueve
ningún token histórico de EF-4/EF-7.

### 4.1 Prescripción par

Sea `n=2s` y

\[
\rho=\lfloor n^{4/5}\rfloor,
\qquad r=2\rho+2,
\qquad N=n-r.
\tag{4.1}
\]

Para `n>=10^40`, `rho<n/4`. Escríbanse

\[
q_1=\lfloor n/4\rfloor,
\qquad q_3=\lfloor3n/4\rfloor.
\]

Se prescribe la familia `F_n` mediante

```text
pi(1)=1,       pi(n)=n,
pi(s)=s,       pi(s+1)=s+1,
pi(s-rho+j)=q_1+j,   j=1,...,rho-1,
pi(s+1+j)=q_3+j,     j=1,...,rho-1.
```

La banda significa desde aquí exactamente el conjunto de filas prescritas

\[
B^-_n=\{s-\rho+1,\ldots,s\},
\qquad
B^+_n=\{s+1,\ldots,s+\rho\};
\tag{4.2a}
\]

no se redefine mediante una desigualdad geométrica susceptible de errores de
redondeo.

Las asignaciones son distintas bajo `rho<n/4`. Las `r` filas y columnas
prescritas dejan una biyección uniforme de `N` filas libres a `N` columnas libres:
cada completación tiene la misma probabilidad y hay exactamente `N!` de ellas.
Por tanto

\[
\Pr(F_n)=\frac{N!}{n!}=\frac1{(n)_r}.
\tag{4.2}
\]

La cuádrupla plantada es

\[
q_0=((1,1),(s,s),(s+1,s+1),(n,n)).
\tag{4.3}
\]

En cada mitad hay exactamente `N/2` filas libres y `N/2` columnas libres. Cada
intervalo de `q_0` contiene `rho+1` puntos prescritos. Además, para toda
completación, el número de puntos libres `L->L` coincide con el número `H->H`:
en la tabla `2 x 2` de flujos libres, ambas igualdades de márgenes son `N/2`.
Así, si `K_0,L_0` son las dos cardinalidades plantadas,

\[
K_0=L_0,
\qquad
\mathbb E[K_0\mid F_n]
=\mathbb E[L_0\mid F_n]
=\frac N4+\rho+1.
\tag{4.4}
\]

Sea `G_n` el evento (3.2) para la biyección libre. Entonces

\[
\Pr(G_n\mid F_n)\ge1-2n^{-6}
\tag{4.5}
\]

y, sobre `G_n`, todo conteo libre rectangular dista como máximo
`eta=sqrt(20N log n)` de su media.

### 4.2 Geometría libre y optimización del caso de pérdida

Para una cuádrupla rival, sean `u_-,u_+` las fracciones de filas libres de sus dos
rectángulos y `v_-,v_+` las fracciones de columnas libres. Como los dos intervalos
de una 4-cadena son disjuntos en ambos ejes,

\[
u_-+u_+\le1,
\qquad v_-+v_+\le1.
\]

Si

\[
f=u_-v_-,\qquad g=u_+v_+,
\]

Cauchy–Schwarz da

\[
\sqrt f+\sqrt g\le1,
\qquad
g\le(1-\sqrt f)^2.
\tag{4.6}
\]

Los puntos prescritos distintos de los cuatro anclajes forman dos escaleras de
`rho-1` puntos: una inmediatamente a la izquierda del centro y en el primer
cuartil de columnas; la otra inmediatamente a la derecha y en el último cuartil.

Se necesitará la siguiente optimización, que sustituye el paso defectuoso de la
antigua familia prescrita. Supóngase que un bloque rival pierde por completo su
escalera. Fuera del caso de producto pequeño tratado abajo, ese bloque contiene a
lo sumo dos puntos prescritos y el otro contiene a lo sumo su propia escalera más
tres anclajes, es decir `rho+2`. Por (4.6), sus dos conteos están acotados en
`G_n` por

\[
Nf+2+\eta,
\qquad
N(1-\sqrt f)^2+\rho+2+\eta.
\]

La primera expresión sin `eta` crece con `sqrt(f)` y la segunda decrece. Su mínimo
se maximiza cuando son iguales, en

\[
\sqrt f=\frac12+\frac{\rho}{2N},
\]

y por tanto

\[
\min(K(q),L(q))
\le
\frac N4+\frac\rho2+\frac{\rho^2}{4N}+2+\eta.
\tag{4.7}
\]

Esta es una desigualdad algebraica completa; el margen correcto es asintóticamente
`rho/2`, no `rho`.

### 4.3 Unicidad del ganador plantado

**Lema 4.1.** Para todo `n=2s>=10^40`,

\[
F_n\cap G_n\subseteq S,
\tag{4.8}
\]

y el ganador único es `q_0`.

**Demostración.** Fíjese una cuádrupla rival `q`.

1. Si sus dos puntos centrales son exactamente `(s,s)` y `(s+1,s+1)`, cambiar el
   extremo global `(1,1)` elimina al menos ese punto del primer intervalo, y
   cambiar `(n,n)` elimina al menos ese punto del segundo. Por (4.4), cualquier
   rival distinto de `q_0` tiene mínimo estrictamente menor, sin usar `G_n`.

2. Si el punto `b` está por debajo de las filas de la banda prescrita, el bloque
   pasado pierde entera la escalera baja. Si está por encima de la banda, entonces
   `c` también lo está y el bloque futuro pierde entera la escalera alta. El mismo
   segundo caso ocurre cuando `b` es uno de los dos centros y `c` queda por encima
   de la banda.

3. Si `b` está dentro de la banda, es necesariamente un punto prescrito. Si es de
   la escalera baja, el producto libre del bloque pasado es a lo sumo `1/6`; si es
   de la escalera alta, el producto libre del bloque futuro es a lo sumo `1/6`.
   Si `b` es central y `c` pertenece a la escalera alta, el producto futuro tiene
   la misma cota. En efecto, uno de los factores de filas es a lo sumo `1/2` y el
   factor de columnas correspondiente es a lo sumo

   \[
   \frac{n/4+\rho+1}{N}<\frac13
   \]

   para `n>=10^40`.

Los casos son exhaustivos. En el caso 2, si el otro bloque capturase también la
escalera opuesta, la posición de su endpoint forzaría precisamente uno de los
productos libres del caso 3; por tanto, fuera del caso 3, valen los topes de
puntos prescritos usados en (4.7).

En el caso 3, aun concediendo al rival los `r=2rho+2` puntos prescritos completos,

\[
\min(K(q),L(q))
\le\frac N6+2\rho+2+\eta.
\tag{4.9}
\]

La plantada satisface, por (4.4) y `G_n`,

\[
K_0=L_0\ge\frac N4+\rho+1-\eta.
\tag{4.10}
\]

Para `n>=10^40`, `rho/n<=10^{-8}`, `N>0.99n` y
`eta/rho<10^{-9}`. La última desigualdad se obtiene de
`rho>=n^(4/5)-1`, `N<=n` y
`sqrt(20n log n)/n^(4/5)`, que ya es menor que `10^{-9}` en `10^40` y
decrece después. De aquí

\[
\frac N{12}-\rho-1-2\eta>0,
\]

de modo que (4.10) domina estrictamente (4.9). En el caso 2, la diferencia entre
(4.10) y (4.7) es al menos

\[
\frac\rho2-1-\frac{\rho^2}{4N}-2\eta>0.
\]

Todo rival tiene, pues, primer componente estrictamente menor que `q_0`. Además
(4.10) es mayor que tres, así que `q_0 in Q_3(C)`. El maximizador del primer
componente es único; el segundo componente lexicográfico no puede cambiarlo ni
crear un empate. Por tanto ocurre `S` y su ganador es `q_0`. `QED`

### 4.4 Masa de `S` en todos los tamaños

Para `n` par y `n>=10^40`, (4.2), (4.5) y el Lema 4.1 dan

\[
\Pr_n(S)
\ge(1-2n^{-6})n^{-(2n^{4/5}+2)}.
\tag{4.11}
\]

Para `n` impar, aplíquese la inyección que envía una permutación `sigma` de
`n-1` elementos a

\[
(\sigma(1)+1,\ldots,\sigma(n-1)+1,1).
\tag{4.12}
\]

El último punto es incomparable con todos los anteriores. No pertenece a ninguna
4-cadena ni a un intervalo con endpoints anteriores; el selector, su unicidad y
las cardinalidades elegidas quedan intactos. Luego

\[
\Pr_n(S)\ge\frac1n\Pr_{n-1}(S).
\tag{4.13}
\]

Combinando ambas paridades se obtiene, para todo `n>=10^40`, la cota común

\[
\boxed{
\Pr_n(S)\ge
\frac12 n^{-(2n^{4/5}+4)}
=e^{-o(n)}.}
\tag{4.14}
\]

## 5. Discrepancia ordinaria fuerza interioridad

Para intervalos de rangos `I,J`, defínase

\[
\Delta_n=
\max_{I,J}
\left|
\frac{N_{\Pi_n}(I,J)}n-
\frac{|I||J|}{n^2}
\right|.
\]

El Lema 3.1 y la unión sobre menos de `n^4` pares dan, con
`delta=1/200`,

\[
\Pr\{\Delta_n>1/200\}
\le2n^4\exp(-n/80000).
\tag{5.1}
\]

Particiónense ambos ejes de rangos en diez intervalos consecutivos

\[
J_j=\{\lfloor(j-1)n/10\rfloor+1,\ldots,\lfloor jn/10\rfloor\},
\qquad j=1,\ldots,10.
\]

Para `n>=200`, cada `J_j` tiene longitud al menos `0.095n`. Si
`Delta_n<=1/200`, cada caja diagonal `J_j x J_j` contiene al menos un punto, pues

\[
\frac{N(J_j,J_j)}n
\ge0.095^2-0.005>0.
\]

Elíjanse puntos `a,b,c,d` respectivamente en las cajas diagonales
`1,4,7,10`. Las separaciones entre bloques aseguran

\[
a\prec b\prec c\prec d.
\]

El intervalo `[a,b]` contiene todos los puntos de
\((J_2\cup J_3)\times(J_2\cup J_3)\), y `[c,d]` contiene los de
\((J_8\cup J_9)\times(J_8\cup J_9)\). Cada unión tiene longitud al menos `0.19n`, así
que

\[
|[a,b]|,|[c,d]|
\ge n(0.19^2-0.005)>0.03n.
\tag{5.2}
\]

La cuádrupla es admisible y obliga al máximo primario de
`MIN_COVERAGE_LEX` a ser al menos `0.03n`. Por tanto, siempre que además ocurra
`S`, ambos lados seleccionados son al menos `0.03n`. Los dos intervalos de una
4-cadena son disjuntos: un punto común exigiría `c prec z prec b`, contradiciendo
`b prec c`. En consecuencia su suma es a lo sumo `n`, y cada lado es también a lo
sumo `0.97n`.

Se ha probado la inclusión determinista

\[
S\cap\{M_h\notin[0.03n,0.97n]\}
\subseteq\{\Delta_n>1/200\}
\tag{5.3}
\]

para ambos lados.

## 6. Cociente condicionado y constantes explícitas

De (4.14), (5.1) y (5.3), para todo `n>=10^40`,

\[
\Pr\{M_h\notin[0.03n,0.97n]\mid n,h,S\}
\le
4n^{2n^{4/5}+8}e^{-n/80000}.
\tag{6.1}
\]

Para `n>=10^40`, la función `(log n)/n^(1/5)` es decreciente y

\[
\frac{\log n}{n^{1/5}}<10^{-6}.
\]

Además, `(8 log n+log 8)/n<10^{-6}` en esa cola. Por ello

\[
(2n^{4/5}+8)\log n+\log 8<3\cdot10^{-6}n<\frac n{80000}.
\]

La parte derecha de (6.1) es, en particular, menor que `1/2`. Esto prueba (1.2)
con las constantes de (1.1).

Combinado con `NC-2A`, para ambos lados y la misma cola se obtiene la consecuencia
autorizada

\[
\mathbb E[b_n(M_h)\mid n,h,S]
\ge
\frac{p\varepsilon^3}{288n}
=\frac{3}{64\,000\,000}\frac1n.
\tag{6.2}
\]

## 7. Techo de afirmación

`NC2C-O2` queda probado. La prueba no estudia ni acota
`Var(ell_h|n,h,S)`, no abre `NC2B-O3` y no implica por sí sola
`liminf T_n^h>0`.

Tampoco afirma optimalidad de `epsilon`, `p` o `n_0`; no transfiere el resultado a
canales enriquecidos, poset completo, horizontes, escala absoluta o `d>=3`; y no
formula novedad ni prioridad.

## 8. Terminal

```text
NC2C_TERMINAL = NC2C_PROVED_UNIFORM_INTERIOR_MASS
NC2C_EPSILON = 3/100
NC2C_P = 1/2
NC2C_N0 = 10^40
NC2C_SIDE_DUALITY = PROVED_EXACT
NC2C_SUBEXPONENTIAL_SELECTION_MASS = PROVED_WITH_NEW_ARGUMENT
NC2C_INTERIOR_NUMERATOR_SCALE = PROVED_ORDER_1_OVER_N
NC2C_O3 = NOT_OPENED
NC2C_LIMINF_T_N = NOT_PROVED
NC2C_NEW_DATA = NO
NC2C_NEW_CODE = NO
```
