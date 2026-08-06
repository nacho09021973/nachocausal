# Regularidad de $U$ — demostración con cuantificadores generales ($m=4$, $k=3$, todo $n$)

Objetivo fijado por el PI (2026-08-06): demostrar
$$\operatorname{Max}(Q)\cap U\neq\varnothing$$
para las amalgamas admisibles con $m=4$, $k=3$, cuantificando sobre **todo $n$**, no sólo
$n=6$; y afirmar "exactamente uno" **sólo** si lo respalda la estructura y no la enumeración.

**Veredicto.** La regularidad de $U$ queda **DEMOSTRADA** para todo $n$ y todo $m\ge 3$
(§4–§5). El "exactamente uno" **NO** queda demostrado: la estructura sólo entrega
$\ge 1$ (§6).

Como subproducto obligado, la verificación descubrió un **error de clase** en el banco de
pruebas de la sesión anterior: la clase §5 estaba sobre-contada $284$ contra $8$ reales.
Las consecuencias se listan en §7–§8 y **retiran** dos afirmaciones previas.

Todo lo importado del artículo se cita por lema y se ha leído literalmente en el texto:
Gutzeit–Shaban–Yeats–Zalel, *Sizes of witnesses in Covtree*, arXiv:2605.00622v1.

### Cuadro de estatus (leer antes que nada)

| enunciado | estatus | alcance |
|---|---|---|
| $\operatorname{Max}(Q)\cap U\neq\varnothing$ | **DEMOSTRADO** (§4–§5) | todo $n$, todo $m\ge3$, $k=3$, amalgamas §5-admisibles |
| $\lvert\operatorname{Max}(Q)\cap U\rvert=1$ ("exactamente uno") | **ABIERTO** (§6) | evidencia finita $8/8$ en $n=6,m=4$; **sin** respaldo estructural |
| $\lvert\operatorname{Max}(Q)\rvert=2\iff Q$ irreducible | **PROBADO en $n=6$, $m=4$** (§8.3) | ⟸ por teorema (todo $n$, $m\ge3$); ⟹ **por vacuidad** en $n=6$ |
| §5-admisible $\iff$ irreducible | verificado $8/8$ y $740/740$ (§8.1) | ⟸ demostrado por camino corto; ⟹ vía el teorema + vacuidad |
| conjetura $n+3$ para $n\ge7$ | **NO ABIERTA** | decisión permanente en pie |

El recíproco de la tercera fila es **vacuo** en $n=6$: no existe ninguna instancia
§5-admisible con $\lvert\operatorname{Max}(Q)\rvert\ge3$ a esa talla. Su contenido no
trivial vive sólo en $n\ge7$, que **no se abre**.

---

## §0. Marco y cuantificadores

Sea $\Gamma_n=\{A,B,C\}$ un nodo con $k=3$ tipos de orden dos a dos no isomorfos, de talla
$n$, y sea $Q$ un testigo: el conjunto de tipos de isomorfía de los $n$-downsets de $Q$ es
exactamente $\Gamma_n$. Sea $G_n(Q)$ el grafo de intercambio (Def. 4.2): vértices = los
$n$-downsets de $Q$ (no sus clases de isomorfía), aristas = pares que difieren en
exactamente un elemento.

**Definición (amalgama §5-admisible).** Siguiendo el montaje de la p. 14 y el de §5
(l. 1855–1866 del texto extraído), $Q$ es *§5-admisible con parámetro $m$* si:

1. existe en $G_n(Q)$ un camino $P$ de la forma $P_1-P_2-\cdots-P_2-P_3$ con los tres
   $P_i$ de tipos distintos, y **no existe ningún camino más corto de esa forma para
   ninguna terna de tipos distintos** (minimalidad FUERTE, literal en la p. 14);
2. $Q$ es la unión de $P$; con $\ge 2$ copias interiores, el Lema 4.6(1) da
   $Q=A\cup C$, donde $A,C$ son las copias ancla;
3. $X:=A\cap C$, $\;m:=|A\setminus X|=|C\setminus X|$, luego $|Q|=n+m$.

En todo lo que sigue $\tau(\cdot)$ es el tipo de isomorfía, $\tau_A=\tau(A)$,
$\tau_C=\tau(C)$, y $\tau_B$ es el tercer tipo (el de las copias interiores del camino).
$\operatorname{Max}(S)$ = maximales de $S$ **en el orden inducido en $S$**.

El objetivo se instancia en $m=4$, pero **ningún paso usa $m=4$ ni $n=6$**: se marca en
cada enunciado la hipótesis mínima efectivamente usada.

### §0.1 La condición 1 es **minimalidad fuerte global**, y es la que decide todo

Este punto merece quedar aislado porque su lectura débil es la que produjo el error de
clase de §7. El artículo escribe, literalmente (p. 14, l. 1535–1540 del texto extraído):

> «*we have a path $P$ of the form $P_1-P_2-P_2-\cdots-P_2-P_3$ in $G_n(Q)$ and **no
> shorter path of this form for any three distinct $P_i$** exists in $G_n(Q)$*»

Es decir, la minimalidad se cuantifica sobre **todas las ternas de tipos distintos** y
sobre **todas las copias**, no sobre la terna que uno tenía en mente. Con $k=3$ hay tres
asignaciones de rol esencialmente distintas (según cuál sea el tipo medio), y el camino
$P$ debe realizar el **mínimo global** entre todas ellas.

Consecuencias, ambas necesarias para no equivocarse:

- **No basta** con que exista *algún* camino $A-B-B-B-C$ de longitud 4 entre las mitades
  pegadas. Que la longitud 4 coincida con $\operatorname{dist}(A,C)=m$ (Prop. 4.4) prueba
  que ese camino es el más corto **entre $A$ y $C$**, no que sea el más corto **de la
  forma especial en $G_n(Q)$**: otra terna puede admitir uno de longitud 2 o 3.
- Si el mínimo global es $L<m$, el montaje de §5 aplicado a ese mismo $Q$ elige **otras
  anclas** y **otro $m$**. El Lema 5.2 pasa entonces a hablar de esa otra descomposición,
  y sobre la nuestra es simplemente **falso** (§7: 5782 violaciones).

En este documento, "§5-admisible" significa siempre la versión fuerte. El programa
`s5_xtab.cpp` la implementa por BFS con el interior restringido al tipo medio, minimizando
sobre las tres asignaciones de rol; `regularity_u.cpp` implementa la versión débil y se
conserva únicamente como registro del fallo.

---

## §1. Hechos base (todo $n$, todo $m\ge 1$; no requieren minimalidad)

**(F1) $X$ es un downset de $Q$.**
$X=A\cap C$ e intersección de downsets es downset. $\square$

**(F2) Ningún elemento de $A\setminus X$ es comparable con uno de $C\setminus X$.**
Sean $a\in A\setminus X$, $c\in C\setminus X$. Si $c<a$: $A$ es downset de $Q$ y $a\in A$,
luego $c\in A$; como además $c\in C$, sale $c\in A\cap C=X$, contradicción. Si $a<c$,
simétrico con $C$. $\square$

De (F2) y $Q=A\cup C$ sale la partición
$$Q \;=\; X \;\sqcup\; (A\setminus X)\;\sqcup\;(C\setminus X).$$

---

## §2. Lema A (maximales de cada mitad) — todo $n$, todo $m\ge 1$

> **Lema A.** $\operatorname{Max}(A\setminus X)\neq\varnothing$ y
> $\operatorname{Max}(A\setminus X)\subseteq\operatorname{Max}(Q)$.
> Idem para $C\setminus X$.

*Demostración.* $|A\setminus X|=m\ge 1$ y es finito, luego tiene maximales.
Sea $q\in\operatorname{Max}(A\setminus X)$ y supongamos $q<u$ con $u\in Q$. Por la
partición de §1 hay tres casos:

- $u\in C\setminus X$: imposible por (F2);
- $u\in X$: imposible, pues $X$ es downset por (F1) y $q<u\in X$ forzaría $q\in X$,
  contra $q\in A\setminus X$;
- $u\in A\setminus X$: imposible por maximalidad de $q$ **dentro de** $A\setminus X$.

No hay tal $u$, luego $q\in\operatorname{Max}(Q)$. $\square$

Obsérvese que el Lema A vale para **toda** amalgama de esta forma, sea o no §5-admisible:
sólo usa $Q=A\cup C$, (F1) y (F2). Es la pieza que hace local el argumento.

---

## §3. Lema B (multiplicidad de $\tau_B$) — todo $n$, todo $m\ge 2$

> **Lema B.** En una amalgama §5-admisible, el número de $n$-downsets de $Q$ de tipo
> $\tau_B$ es $\ge m-1$.

*Demostración.* Por la Prop. 4.4 (conexión y **distancia** en $G_n(Q)$):
$\operatorname{dist}(A,C)=|A\setminus(A\cap C)|=m$. El camino $P$ va de $A$ a $C$, luego
su longitud es $\ge m$, luego tiene $\ge m-1$ vértices interiores. Los vértices de un
camino son distintos, y por la forma de $P$ todos los interiores son copias de $\tau_B$;
son $n$-downsets **distintos** de $Q$. $\square$

No hace falta el Lema 4.6(2) (que daría la igualdad $m-1$): la desigualdad basta y depende
de menos hipótesis.

**Corolario B'.** Si $m\ge 3$ entonces $\tau_B$ tiene multiplicidad $\ge 2$; para $m=4$,
multiplicidad $\ge 3$. Luego **un tipo de multiplicidad 1 nunca es $\tau_B$.**

---

## §4. Teorema R (regularidad) — todo $n$, todo $m\ge 3$

> **Teorema R.** Sea $Q$ §5-admisible con $m\ge 3$. Entonces **todo** $n$-downset $D$ de
> $Q$ con $\tau(D)\neq\tau_B$ corta a $\operatorname{Max}(Q)$:
> $$\forall D \in \mathcal D_n(Q):\quad \tau(D)\neq\tau_B \;\Longrightarrow\; D\cap\operatorname{Max}(Q)\neq\varnothing .$$

*Demostración.* El **Lema 5.2** del artículo (l. 1881–1883; hipótesis: montaje de §5 y
$m\ge 3$) dice que todo $n$-downset de $Q$ que no contiene ni todo $A\setminus X$ ni todo
$C\setminus X$ es isomorfo a $B$. Por contraposición, $\tau(D)\neq\tau_B$ implica
$$A\setminus X\subseteq D \quad\text{o}\quad C\setminus X\subseteq D .$$
En el primer caso $D\supseteq\operatorname{Max}(A\setminus X)$, que por el Lema A es no
vacío y está contenido en $\operatorname{Max}(Q)$; en el segundo, lo mismo con
$C\setminus X$. $\square$

**Forma fuerte, que es la que realmente se prueba:**
$$\tau(D)\neq\tau_B \;\Longrightarrow\; \operatorname{Max}(A\setminus X)\subseteq D \ \ \text{o}\ \ \operatorname{Max}(C\setminus X)\subseteq D,$$
y por tanto $|D\cap\operatorname{Max}(Q)|\ \ge\ \min\bigl(|\operatorname{Max}(A\setminus X)|,\,|\operatorname{Max}(C\setminus X)|\bigr)$.

---

## §5. Corolario U — el objetivo del PI ($m=4$ incluido)

> **Corolario U (regularidad de $U$).** Sea $Q$ §5-admisible con $m\ge 3$ (en particular
> $m=4$), y sea $\gamma\in\Gamma_n$ un tipo de **multiplicidad 1** en $Q$, con copia única
> $U$. Entonces
> $$\operatorname{Max}(Q)\cap U\neq\varnothing .$$

*Demostración.* Por el Corolario B', $\gamma\neq\tau_B$. Aplíquese el Teorema R a $D=U$. $\square$

Cuantificadores efectivamente cubiertos: **todo $n$**, **todo $m\ge 3$**, $k=3$, toda
amalgama §5-admisible, todo tipo de multiplicidad 1. Nada usa $n=6$.

---

## §6. Lo que la estructura NO da: "exactamente uno"

La demostración entrega $\ge 1$ y, en su forma fuerte, $\ge|\operatorname{Max}(A\setminus X)|$
o $\ge|\operatorname{Max}(C\setminus X)|$. **No hay** ningún paso que acote por arriba
$|\operatorname{Max}(Q)\cap U|$. Por tanto, siguiendo la instrucción del PI, se afirma
$\neq\varnothing$ y **no** "exactamente uno".

Estado del "exactamente uno" tras la corrección de clase (§7):

- La **refutación** anterior ($|\operatorname{Max}(Q)\cap U|\in\{1,2,3,4\}$ con
  $210/94/16/6$) se calculó sobre las 748 amalgamas, es decir mayoritariamente **fuera**
  de §5, donde las hipótesis del Teorema R ni siquiera se cumplen. **Esa refutación queda
  retirada**: no refuta un enunciado §5.
- Sobre la clase §5 **verdadera** ($n=6$, $m=4$): $|\operatorname{Max}(Q)\cap U|=1$ en
  $8/8$ instancias (`U_MAXHITS_STRICT_1=8`).
- Conclusión honesta: "exactamente uno" está **ABIERTO**, con evidencia finita $8/8$ y
  **sin** respaldo estructural. No se afirma.

---

## §7. ERROR DE CLASE: sólo $8$ de $748$ son §5-admisibles

> **Titular.** De las 748 amalgamas testigo del barrido, **$8$ son realmente
> §5-admisibles**. Las otras **$740$** quedan explicadas —y su reducibilidad
> *demostrada*, §8.1— por el lema de camino corto, pero **no pueden usarse para
> contrastar el Lema 5.2**: en ellas sus hipótesis no se cumplen, de modo que ni lo
> confirman ni lo refutan. Cualquier estadística anterior calculada "dentro de §5" sobre
> 284 instancias está medida en la clase equivocada.

### La sobre-contabilización $284\to 8$

La sesión anterior marcaba como "§5" la existencia de **algún** camino $A-B-B-B-C$ de
longitud 4 (bandera LOOSE). El montaje del artículo exige la minimalidad **fuerte**: que
no exista camino más corto de esa forma *para ninguna terna de tipos distintos*
(bandera STRICT). Resultado sobre el barrido completo de 748 amalgamas testigo:

| | LOOSE | STRICT |
|---|---|---|
| instancias marcadas §5 | 284 | **8** |
| violaciones del Lema 5.2 | 5782 (en LOOSE∖STRICT) | **0** |

Es decir: en 276 de las 284 instancias "§5" de la sesión anterior **el Lema 5.2 es falso**,
porque sus hipótesis no se cumplen. Esas instancias no sostienen ni contradicen nada.

**Contraejemplo verificado a mano.** `Q_ROWS=192,0,0,0,0,0,0,0,0,0`: el poset sobre
$\{0,\dots,9\}$ con $X=\{0,1\}$, $A\setminus X=\{2,3,4,5\}$, $C\setminus X=\{6,7,8,9\}$ y
como únicas relaciones $0<6$ y $0<7$. El downset $D=\{0,1,2,3,6,7\}$ tiene talla 6,
$|D\cap(A\setminus X)|=2<4$ y $|D\cap(C\setminus X)|=2<4$ — no contiene ninguna mitad — y
sin embargo $D\cong C$ (un elemento con dos por encima, tres aislados), **no** $\cong B$.
El mínimo global de camino especial en ese $Q$ es 2, no 4: nunca fue una instancia §5.

**El Teorema R sobrevive intacto**, y ahora está verificado sobre la clase correcta:
`TR_VIOLATIONS_STRICT=0`, `MULT1_TYPE_IS_B_STRICT=0`, `CU_VIOLATIONS_STRICT=0`.
(El Lema A, que no depende de §5, da 0 violaciones en las 748:
`LA_SIDEMAX_NOT_GLOBAL_MAX=0`, `LA_EMPTY_SIDE_MAX=0`.)

**El sello del gate `N6_K3_N_PLUS_3` NO se ve afectado**: el gate sólo necesita que lo
barrido sea un superconjunto de los testigos mínimos de talla 10, y la sobre-enumeración
sólo puede añadir supervivientes, nunca ocultarlos.

---

## §8. Lo que la corrección cambia en lo que estaba abierto

**(8.1) Lema de camino corto — DEMOSTRADO, todo $n$.** Sea $Q$ un testigo cualquiera de
$\Gamma_n$ ($k=3$) y sea $L$ la longitud del camino especial mínimo global en $G_n(Q)$.
Sea $R$ la unión de los vértices de ese camino. Entonces $R$ es un downset de $Q$ (unión
de downsets), es un testigo de $\Gamma_n$ (contiene una copia de cada tipo, y todos sus
$n$-downsets lo son de $Q$), y
$$|R|\;\le\;\begin{cases} n+3 & L=2 \quad(R=P_1\cup P_2\cup P_3,\ \text{Obs. 4.7}),\\[2pt] n+L & L\ge 3\quad (R=P_1\cup P_3\ \text{por Lema 4.6(1)};\ |P_1\cup P_3|=n+\operatorname{dist}=n+L).\end{cases}$$
**Corolario.** $L\le 3\Rightarrow Q$ tiene un sub-testigo de talla $\le n+3$. Para $n=6$,
$|Q|=10$: $L\le3\Rightarrow Q$ **reducible**. Contrarrecíproco: $Q$ irreducible de talla
$n+4$ $\Rightarrow L=4$ y $Q=R$, es decir $Q$ **es** §5-admisible con $m=4$.

Esto reproduce $740$ de las $748$ reducibilidades **por estructura, sin enumerar
downsets**, y explica exactamente la tabla observada:

```
XTAB_STRICT_IRRED=8  STRICT_RED=0  NONSTRICT_IRRED=0  NONSTRICT_RED=740
GLOBAL_MIN_SPECIAL_PATH_LEN_2=714   _3=26   _4=8
```

es decir **§5-admisible $\iff$ irreducible**, $8/8$ y $740/740$, sin excepción. La
dirección $\Leftarrow$ es el corolario recién probado; la dirección $\Rightarrow$ es el
teorema "$|\operatorname{Max}(Q)|=2\Rightarrow$ irreducible" ya probado, más (8.3).

**(8.2) Reformulación de la conjetura $n+3$ ($k=3$).** Por (8.1), la conjetura equivale a:
*todo nodo $\Gamma_n$ admite un testigo cuyo camino especial mínimo global tiene longitud
$\le 3$.* Es una reformulación limpia y enteramente en términos de $G_n(Q)$.

**(8.3) El recíproco abierto es VACÍO en $n=6$.** La conjetura pendiente era
$|\operatorname{Max}(Q)|\ge 3\Rightarrow Q$ reducible, apoyada en "276 instancias §5 con
$\max\ge 3$, todas reducibles". Esas 276 son LOOSE∖STRICT: **no son §5**. Sobre la clase
verdadera, las 8 instancias §5 tienen todas $|\operatorname{Max}(Q)|=2$
(`MAXQ=2` en las ocho). Luego en $n=6$, $m=4$ **no existe ninguna instancia con
$|\operatorname{Max}(Q)|\ge3$**: el recíproco es cierto por vacuidad y $n=6$ **no puede
probarlo ni refutarlo**. La evidencia finita que se le atribuía queda retirada.

Consecuencia operativa: la equivalencia $\max(Q)=2\iff$ irreducible queda **demostrada**
en $n=6$, $m=4$ (una dirección por teorema, la otra por vacuidad), y el contenido no
trivial del recíproco vive **sólo** en $n\ge 7$. La decisión permanente de no abrir $n=7$
sigue en pie; lo que cambia es que ya no hay nada que ganar buscándole evidencia a $n=6$.

---

## §9. Verificación

### §9.1 El sello de `87c2d49` sigue intacto — estos hashes se AÑADEN, no lo sustituyen

Esta rama (`covtree/regularidad-u`) nace de `87c2d49` y **no la avanza**. El sello previo
se ha re-verificado en este mismo árbol antes de commitear, y **reproduce exactamente**:

| sello de `87c2d49` | SHA-256 | estado |
|---|---|---|
| fuente `covtree_n6_gate.cpp` | `f2264bdfcf63c07edf97de76ff9a41a636daf983077fdadc913bcc52d0671cd3` | **coincide** |
| salida de `--run-pairs` | `bf314aa2949c548b8f14e8571a01c07e796d6da634ebe851e5780e78b6ac3bfe` | **coincide**, exit 0 |

Nada de este documento modifica, sustituye ni invalida ese sello. El resultado sellado
(`N6_K3_N_PLUS_3=PASS_EVERY_GAMMA6_HAS_WITNESS_LE_9`) es independiente de la corrección de
§7: el gate sólo exige que lo barrido sea un **superconjunto** de los testigos mínimos de
talla 10, y la sobre-enumeración únicamente puede añadir supervivientes, nunca ocultarlos.
Lo que §7 corrige es el uso *interpretativo* de la submuestra, no el veredicto del gate.

### §9.2 Artefactos nuevos de esta rama

Compilar con `g++ -std=c++20 -O2 -Wall -Wextra -Wno-unused-function`; ambos compilan sin
avisos y corren en ~1 s.

| artefacto | SHA-256 | exit |
|---|---|---|
| `covtree/regularity_u.cpp` | `a65493288da85bdd2c5e3da7b9d3957bd7078d46c81766bda8ca796c01d21827` | — |
| salida de `./regularity_u` | `385bb9fb141acbbe2f8264fc00edee4fdb23eec2481a0cb672196324d9078925` | **4** (esperado) |
| `covtree/s5_xtab.cpp` | `2a6cd92858ecbccf6cce693625f91dedec8c269bc80333759b84f867f83d91c2` | — |
| salida de `./s5_xtab` | `69700503466edecab90f9205c983d9e55c25114fe5139c54b1ff9a2077e6e660` | 0 |

Ambos reutilizan **sin modificar** las líneas 1–308 de `covtree_n6_gate.cpp` (318 posets no
etiquetados $=$ A000112(6), canonicalización exacta, downsets exactos), de modo que la
maquinaria de enumeración es literalmente la sellada.

- `regularity_u.cpp` — comprueba F1, F2 y el Lema A (0 violaciones en 748/748), y R/B′/U
  separando dentro y fuera de la bandera **LOOSE**. **Sale con código 4 a propósito**: su
  criterio de §5 es el débil, que es el equivocado, y el propio programa lo delata
  (`L52_VIOLATIONS_INSIDE_S5=5782`). Se conserva como registro reproducible del fallo, no
  como evidencia de nada.
- `s5_xtab.cpp` — implementa la bandera **STRICT** (mínimo global sobre las tres
  asignaciones de rol, por BFS con el interior restringido al tipo medio), la tabla cruzada
  §5 $\times$ reducibilidad, y las comprobaciones de R, B′ y U sobre la clase correcta.
  Cifras de registro: `STRICT_S5=8`, `LOOSE_S5=284`, `L52_VIOLATIONS_STRICT=0`,
  `TR_VIOLATIONS_STRICT=0`, `MULT1_TYPE_IS_B_STRICT=0`, `CU_VIOLATIONS_STRICT=0`,
  `U_MAXHITS_STRICT_1=8`, `XTAB_STRICT_IRRED=8 STRICT_RED=0 NONSTRICT_IRRED=0
  NONSTRICT_RED=740`.

Importaciones del artículo, leídas literalmente en el texto extraído:

| import | dónde | hipótesis usada |
|---|---|---|
| Def. 4.2 (grafo de intercambio) | l. 1267–1272 | — |
| Prop. 4.4 ($\operatorname{dist}=|A\setminus(A\cap B)|$) | l. 1335–1341 | — |
| Lema 4.6(1) ($R=P_1\cup P_3$) | l. 1550–1567 | $\ge2$ copias interiores |
| Obs. 4.7 (caso de una sola copia interior) | l. 1764–1795 | — |
| montaje §5 y minimalidad fuerte | p. 14 (l. 1522–1549), l. 1855–1866 | — |
| Lema 5.2 | l. 1881–1883 | montaje §5 y $m\ge3$ |

Nada de lo anterior se re-deriva; se importa y se cita. Los teoremas propios (Lema A,
Lema B, Teorema R, Corolario U, §8.1) sí se demuestran aquí.
