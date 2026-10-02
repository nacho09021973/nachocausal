# WP6 — `FINITE_N_VISIBLE_SPAN_PATTERN_PREFLIGHT`

```text
STATUS = CLOSED_BY_FULL_CLASS_SUM_RANK_THEOREM
N5_NOT_OPENED
GENERAL_EQUALITY = PROVED_IN_FOLLOWUP
GENERAL_MONOTONICITY = PROVED_IN_FOLLOWUP
DENSITY_CONCLUSION = PROVED_IN_FOLLOWUP
NOVELTY_CERTIFICATE = NO
```

> **Cierre posterior.** La reducción de este preflight fue cerrada en
> `wp6_full_class_sum_rank_theorem.md` mediante una familia explícita de posets
> casi cadena y una triangularización por laplacianos de aristas. Las marcas
> `OPEN`, `CONJECTURE` y `CONDITIONAL` que aparecen más abajo conservan el
> estado histórico del preflight en el momento de redactarse; no son el estado
> terminal vigente.

## 1. Pregunta y resultado del preflight

Sea

\[
H:=L_0^2([0,1])
=\left\{a\in L^2([0,1]):\int_0^1a(t)\,dt=0\right\},
\tag{1.1}
\]

y sea \(P_{n-1}\subset H\) el espacio de polinomios centrados de grado a lo
sumo \(n-1\). Equivalentemente,

\[
P_{n-1}=\operatorname{span}\{p_1,\ldots,p_{n-1}\},
\tag{1.2}
\]

donde \(p_k\) es cualquier normalización del polinomio de Legendre desplazado
de grado \(k\). En las convenciones de §§13--15,

\[
p_1=x,qquad p_2=q,qquad p_3=r
\tag{1.3}
\]

salvo escala.

La pauta observada es

\[
V_n\stackrel{?}{=}\operatorname{Sym}^2P_{n-1}.
\tag{1.4}
\]

Este preflight demuestra para todo \(n\ge2\) la inclusión superior

\[
\boxed{V_n\subseteq\operatorname{Sym}^2P_{n-1},}
\tag{1.5}
\]

y reduce la inclusión inversa a una condición explícita de rango sobre una
familia finita de matrices de permutación. No demuestra todavía (1.4).

## 2. Scores de permutación a cardinalidad fija

En el nulo independiente, sea

\[
d_i^{(n)}(t)
=n\binom{n-1}{i-1}t^{i-1}(1-t)^{n-i},
\qquad i=1,\ldots,n,
\tag{2.1}
\]

la densidad del estadístico de orden \(i\) de \(n\) uniformes. Cada
\(d_i^{(n)}\) es un polinomio de grado a lo sumo \(n-1\), integra uno y

\[
\sum_{i=1}^n d_i^{(n)}(t)=n.
\tag{2.2}
\]

Definimos sus versiones centradas

\[
b_i^{(n)}:=d_i^{(n)}-1.
\tag{2.3}
\]

Entonces \(b_i^{(n)}\in P_{n-1}\),
\(\sum_i b_i^{(n)}=0\), y

\[
\boxed{
\operatorname{span}\{b_1^{(n)},\ldots,b_n^{(n)}\}=P_{n-1}.
}
\tag{2.4}
\]

En efecto, los \(d_i^{(n)}/n\) son la base de Bernstein de grado \(n-1\).
Por tanto son linealmente independientes en el espacio de polinomios de
dimensión \(n\). Al centrar aparece exactamente la única relación (2.2), de
modo que el span centrado tiene dimensión \(n-1\) y coincide con
\(P_{n-1}\).

Sea \(f=\mathcal P\psi\in H\widehat\otimes H\) el tangente de interacción y
sea \(\sigma\in\mathfrak S_n\) la permutación de rangos. Como el score de una
observación de la cópula es \(2f\),

\[
p'_{\sigma}(0;f)
=\frac{2}{n!}\sum_{i=1}^n
\left\langle f,
d_i^{(n)}\otimes d_{\sigma(i)}^{(n)}
\right\rangle.
\tag{2.5}
\]

Las marginales nulas de \(f\) permiten sustituir cada \(d_i^{(n)}\) por
\(b_i^{(n)}\):

\[
\boxed{
p'_{\sigma}(0;f)
=\left\langle f,R_\sigma^{(n)}\right\rangle,
\qquad
R_\sigma^{(n)}
:=\frac2{n!}\sum_{i=1}^n
b_i^{(n)}\otimes b_{\sigma(i)}^{(n)}.
}
\tag{2.6}
\]

En particular,

\[
R_\sigma^{(n)}\in P_{n-1}\otimes P_{n-1}.
\tag{2.7}
\]

Ésta es la razón exacta por la que una muestra de \(n\) elementos no puede ver
modos univariados ortogonales a todos los polinomios de grado \(n-1\).

## 3. El cociente por isomorfismo fuerza simetría

Sea \(\mathcal C_n\) el soporte de clases de isomorfismo de posets que pueden
obtenerse como órdenes producto de dos rankings de \(n\) puntos. Para
\(C\in\mathcal C_n\), denote \(\Gamma_C\subseteq\mathfrak S_n\) el conjunto de
permutaciones que producen un poset isomorfo a \(C\). En el nulo,

\[
p_C(0)=\frac{|\Gamma_C|}{n!}>0
\tag{3.1}
\]

y su representante de derivada es

\[
R_C^{(n)}:=\sum_{\sigma\in\Gamma_C}R_\sigma^{(n)}.
\tag{3.2}
\]

Intercambiar las coordenadas \(u\leftrightarrow v\) envía \(\sigma\) a
\(\sigma^{-1}\). El poset abstracto no cambia: sólo se usa el otro ranking
como primera enumeración de sus puntos. Por tanto

\[
\sigma\in\Gamma_C
\quad\Longleftrightarrow\quad
\sigma^{-1}\in\Gamma_C.
\tag{3.3}
\]

Además,

\[
\left(R_\sigma^{(n)}\right)^\top=R_{\sigma^{-1}}^{(n)}.
\tag{3.4}
\]

Sumando sobre una clase cerrada bajo inversión,

\[
\left(R_C^{(n)}\right)^\top=R_C^{(n)}.
\tag{3.5}
\]

Así,

\[
\boxed{R_C^{(n)}\in\operatorname{Sym}^2P_{n-1}}
\qquad(C\in\mathcal C_n).
\tag{3.6}
\]

Este argumento también prueba que el sector antisimétrico
\(\bigwedge^2H\) está en el kernel del poset no etiquetado para **todo**
\(n\), no sólo para \(n=2,3,4\).

## 4. Prueba de la inclusión superior

La forma Fisher del poset es

\[
G_{[P]}^{(n)}(f,g)
=\sum_{C\in\mathcal C_n}
\frac{
\langle f,R_C^{(n)}\rangle
\langle g,R_C^{(n)}\rangle
}{p_C(0)}.
\tag{4.1}
\]

Por tanto su espacio visible —el complemento ortogonal de su kernel, o,
equivalentemente, el span de sus representantes de score— es

\[
V_n=\operatorname{span}\{R_C^{(n)}:C\in\mathcal C_n\}.
\tag{4.2}
\]

Aplicando (3.6),

\[
\boxed{
V_n\subseteq\operatorname{Sym}^2P_{n-1}
\quad\text{y}\quad
\operatorname{rank}G_{[P]}^{(n)}
\le\dim\operatorname{Sym}^2P_{n-1}
=\frac{n(n-1)}2.
}
\tag{4.3}
\]

Esto demuestra la mitad fácil de (1.4) y explica estructuralmente por qué sólo
aparecen \(x\) para \(n=2\), \(x,q\) para \(n=3\) y \(x,q,r\) para
\(n=4\). Los cálculos exactos previos saturan la cota:

\[
\operatorname{rank}G_{[P]}^{(2)}=1,
\qquad
\operatorname{rank}G_{[P]}^{(3)}=3,
\qquad
\operatorname{rank}G_{[P]}^{(4)}=6.
\tag{4.4}
\]

## 5. La inclusión difícil como problema algebraico finito

Sea

\[
E_n:=\mathbf1^\perp
=\left\{z\in\mathbb R^n:\sum_{i=1}^nz_i=0\right\}.
\tag{5.1}
\]

El mapa lineal

\[
B_n:E_n\longrightarrow P_{n-1},
\qquad
z\longmapsto\sum_{i=1}^nz_i b_i^{(n)},
\tag{5.2}
\]

es un isomorfismo por (2.4). Si \(P_\sigma\) es la matriz de permutación de
\(\sigma\), definimos la suma de clase

\[
A_C:=\sum_{\sigma\in\Gamma_C}P_\sigma.
\tag{5.3}
\]

La clausura por inversión hace simétrica a \(A_C\). Bajo el isomorfismo
inducido por \(B_n\), el tensor \(R_C^{(n)}\) es, salvo el factor no nulo
\(2/n!\), la restricción de \(A_C\) a \(E_n\). En consecuencia,

\[
\boxed{
V_n=\operatorname{Sym}^2P_{n-1}
\quad\Longleftrightarrow\quad
\operatorname{span}
\{A_C|_{E_n}:C\in\mathcal C_n\}
=\operatorname{Sym}(E_n).
}
\tag{5.4}
\]

Equivalentemente, basta probar

\[
\boxed{
\operatorname{rank}
\left(\operatorname{vec}_{\mathrm{sym}}(A_C|_{E_n})ight)_{C\in\mathcal C_n}
=\frac{n(n-1)}2.
}
\tag{5.5}
\]

La parte analítica y geométrica del problema desaparece de (5.5): queda una
afirmación puramente finita sobre clases de permutaciones que generan el mismo
poset bidimensional. Los casos \(n=2,3,4\) verifican (5.5) exactamente.

Este es el blanco correcto para la siguiente demostración. Calcular \(n=5\)
sin una idea estructural sólo comprobaría una instancia más de (5.5); por eso
permanece cerrado durante este preflight.

## 6. Consecuencia de densidad, estrictamente condicional

Los polinomios centrados son densos en \(H\):

\[
\overline{\bigcup_{m\ge1}P_m}=H.
\tag{6.1}
\]

Por tanto los tensores simétricos algebraicos construidos con ellos son densos
en el producto tensorial simétrico de Hilbert:

\[
\overline{
\bigcup_{m\ge1}\operatorname{Sym}^2P_m
}
=H\widehat\otimes_{\mathrm{sym}}H.
\tag{6.2}
\]

Si se demostrase (1.4) para todo \(n\), entonces seguiría

\[
\boxed{
\overline{\bigcup_{n\ge2}V_n}
=H\widehat\otimes_{\mathrm{sym}}H.
}
\tag{6.3}
\]

Pero (6.3) es **condicional**. Además, incluso bajo (1.4), el sector
antisimétrico seguiría siendo invisible a toda cardinalidad por §3. El posible
resultado de densidad sería recuperación progresiva del sector simétrico de
interacción S1, no de toda la geometría ni de todo \(H\widehat\otimes H\).

## 7. Claims cerrados y obligaciones abiertas

```text
FINITE_N_DEGREE_CEILING = PROVED
UNLABELED_POSET_COORDINATE_SWAP_SYMMETRY = PROVED
ALL_N_ANTISYMMETRIC_KERNEL = PROVED
RANK_UPPER_BOUND_n_nminus1_over_2 = PROVED
LOWER_INCLUSION = OPEN_AS_FINITE_CLASS_SUM_RANK
EQUALITY_Vn_SYM2_Pnminus1 = CONJECTURE_VERIFIED_FOR_n_2_3_4
DENSITY_OF_VISIBLE_UNION = CONDITIONAL_ON_EQUALITY
N5 = HOLD
NO_GENERAL_RECOVERY_CLAIM
NO_NOVELTY_CERTIFICATE
```

El siguiente paso matemático recomendado es buscar una base explícita de
\(\operatorname{Sym}(E_n)\) generada por combinaciones de las sumas de clase
\(A_C\), o una triangularización por invariantes simples de los posets de
permutación. Si esa ruta falla, \(n=5\) recupera valor como falsificador de
(5.5), no como continuación automática del catálogo.
