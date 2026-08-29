# WP6 — `FULL_CLASS_SUM_RANK_THEOREM`

```text
STATUS = PROVED
Vn_EQUALS_SYM2_Pnminus1 = PROVED_FOR_ALL_n_GE_2
RANK_G_POSET_n = n_choose_2
VISIBLE_SPACES_STRICTLY_NESTED = PROVED
SYMMETRIC_DENSITY = PROVED
ALL_N_ANTISYMMETRIC_KERNEL = PROVED
N5_NOT_USED
NO_NOVELTY_CERTIFICATE
```

## 1. Teorema

Con las definiciones de
`wp6_finite_n_visible_span_pattern_preflight.md`, sea

\[
P_{n-1}=\operatorname{span}\{p_1,\ldots,p_{n-1}\}
\subset L_0^2([0,1]),
\tag{1.1}
\]

donde \(p_k\) es el polinomio de Legendre desplazado y centrado de grado
\(k\), con normalización arbitraria no nula. Sea \(V_n\) el span de los
representantes de score de la ley del poset no etiquetado inducido por \(n\)
observaciones iid de la cópula S1 en el nulo independiente.

**Teorema 1 (`FULL_CLASS_SUM_RANK_THEOREM`).** Para todo \(n\ge2\),

\[
\boxed{
V_n=\operatorname{Sym}^2P_{n-1}.
}
\tag{1.2}
\]

En particular,

\[
\boxed{
\operatorname{rank}G_{[P]}^{(n)}
=\dim V_n
=\frac{n(n-1)}2.
}
\tag{1.3}
\]

La prueba no enumera posets a \(n=5\) ni usa inducción empírica desde
\(n=2,3,4\). Construye para cada \(n\) una familia explícita de
\(\binom n2\) clases cuyos representantes generan todo el espacio objetivo.

## 2. Reducción ya probada

El preflight demostró

\[
V_n\subseteq\operatorname{Sym}^2P_{n-1}
\tag{2.1}
\]

y redujo la igualdad a

\[
\operatorname{span}
\{A_C|_{E_n}:C\in\mathcal C_n\}
=\operatorname{Sym}(E_n),
\qquad
E_n:=\mathbf1^\perp\subset\mathbb R^n,
\tag{2.2}
\]

donde

\[
A_C=\sum_{\sigma\in\Gamma_C}P_\sigma
\tag{2.3}
\]

es la suma de las matrices de permutación que representan una misma clase de
poset bidimensional. Basta demostrar (2.2).

## 3. Una familia de \(\binom n2\) posets casi cadena

Fijemos enteros

\[
0\le a<b\le n-1.
\tag{3.1}
\]

Definimos \(C_{a,b}\) sobre los elementos

\[
c_1<\cdots<c_{n-1}
\tag{3.2}
\]

y un elemento adicional \(z\), imponiendo

\[
c_i<z\quad(i\le a),
\qquad
z<c_i\quad(i>b),
\tag{3.3}
\]

y dejando \(z\) incomparable con

\[
c_{a+1},\ldots,c_b.
\tag{3.4}
\]

Cada extensión lineal de \(C_{a,b}\) se obtiene insertando \(z\) en la cadena
después de exactamente \(k\) elementos, para algún

\[
k\in\{a,a+1,ldots,b\}.
\tag{3.5}
\]

Sean \(L_s,L_t\) dos extensiones así obtenidas. Su intersección ordenada pone
por debajo de \(z\) exactamente a \(c_1,\ldots,c_{\min(s,t)}\), y por encima
exactamente a \(c_{\max(s,t)+1},\ldots,c_{n-1}\). Por tanto

\[
L_s\cap L_t=C_{a,b}
\quad\Longleftrightarrow\quad
\{s,t\}=\{a,b\}.
\tag{3.6}
\]

Así, los únicos realizadores ordenados de dimensión dos son
\((L_a,L_b)\) y \((L_b,L_a)\). Al normalizar el primer orden como
\(1<\cdots<n\), sus permutaciones relativas son un ciclo sobre el intervalo
consecutivo

\[
I_{a,b}:=\{a+1,a+2,\ldots,b+1\}
\tag{3.7}
\]

y su inverso. Denotemos ese ciclo por \(\tau_{a,b}\). Por consiguiente,

\[
\Gamma_{C_{a,b}}
=\{\tau_{a,b},\tau_{a,b}^{-1}\},
\tag{3.8}
\]

entendiendo el conjunto sin multiplicidad: si \(b=a+1\), el ciclo es una
transposición y coincide con su inverso.

Las clases \(C_{a,b}\) son distintas. En efecto, el multiconjunto invariante
de cardinalidades de pasados estrictos es

\[
\bigl\{|\mathop{\rm Past}(y)|:y\in C_{a,b}\bigr\}
=\{0,1,\ldots,b-1,b+1,\ldots,n-1\}\uplus\{a\}.
\tag{3.9}
\]

Es decir, falta \(b\) y aparece \(a\) con multiplicidad dos. Como \(a<b\),
este multiconjunto determina \((a,b)\). Hay exactamente

\[
\#\{(a,b):0\le a<b\le n-1\}=\binom n2
\tag{3.10}
\]

clases en esta familia.

## 4. De ciclos de intervalo a laplacianos de aristas

Para \(1\le i<j\le n\), escribimos

\[
L_{ij}:=(e_i-e_j)(e_i-e_j)^\top.
\tag{4.1}
\]

Estas son las matrices laplacianas de las aristas del grafo completo. Tienen
sumas de filas y columnas nulas y, restringidas a \(E_n\), forman una base de
\(\operatorname{Sym}(E_n)\). En efecto, son \(\binom n2\) matrices; si
\(\sum_{i<j}w_{ij}L_{ij}=0\), cada entrada fuera de la diagonal es
\(-w_{ij}\), luego todos los coeficientes se anulan. Además

\[
\sum_{i<j}L_{ij}=nI_{E_n}.
\tag{4.2}
\]

Usamos las sumas simetrizadas

\[
S_{a,b}:=
P_{\tau_{a,b}}+P_{\tau_{a,b}}^\top.
\tag{4.3}
\]

Para \(b=a+1\), \(S_{a,b}=2A_{C_{a,b}}\); para \(b>a+1\),
\(S_{a,b}=A_{C_{a,b}}\). Los factores escalares no nulos no cambian el span.

Definimos sobre \(E_n\)

\[
Q_{a,b}:=2I_{E_n}-S_{a,b}|_{E_n}.
\tag{4.4}
\]

Como \(\tau_{a,b}\) es el ciclo consecutivo sobre
\(a+1,\ldots,b+1\), \(Q_{a,b}\) es el laplaciano de ese ciclo. Por tanto,

\[
Q_{a,a+1}=2L_{a+1,a+2},
\tag{4.5}
\]

y, para \(b>a+1\),

\[
Q_{a,b}
=L_{a+1,b+1}
+\sum_{k=a+1}^{b}L_{k,k+1}.
\tag{4.6}
\]

Las ecuaciones (4.5)--(4.6) son triangulares por la longitud del intervalo.
Primero recuperan todas las aristas adyacentes:

\[
L_{i,i+1}=\frac12Q_{i-1,i}.
\tag{4.7}
\]

Después, para \(j>i+1\),

\[
L_{ij}
=Q_{i-1,j-1}
-\frac12\sum_{k=i}^{j-1}Q_{k-1,k}.
\tag{4.8}
\]

Así,

\[
\boxed{
\operatorname{span}\{Q_{a,b}\}
=\operatorname{span}\{L_{ij}:i<j\}
=\operatorname{Sym}(E_n).
}
\tag{4.9}
\]

Todavía debemos retirar el término común \(2I_{E_n}\) de (4.4), es decir,
probar que las propias sumas de clase \(S_{a,b}\) tienen el mismo span. Ése es
el único detalle que no se obtiene sólo por triangularidad.

## 5. El operador identidad pertenece al span de las sumas de clase

Por (4.2),

\[
I_{E_n}=\frac1n\sum_{i<j}L_{ij}.
\tag{5.1}
\]

Sustituyendo (4.7)--(4.8), existen coeficientes explícitos \(c_{a,b}\) tales
que

\[
I_{E_n}=\sum_{a<b}c_{a,b}Q_{a,b}.
\tag{5.2}
\]

No necesitamos cada coeficiente por separado, pero sí su suma. Una arista a
distancia \(d=j-i\) aporta suma de coeficientes \(1-d/2\) en su expresión por
los \(Q\)'s. Hay \(n-d\) aristas de distancia \(d\). Por tanto

\[
\begin{aligned}
s_n:=\sum_{a<b}c_{a,b}
&=\frac1n\sum_{d=1}^{n-1}(n-d)\left(1-\frac d2\right)\\
&=\frac{(n-1)(5-n)}{12}.
\end{aligned}
\tag{5.3}
\]

Usando \(Q_{a,b}=2I_{E_n}-S_{a,b}|_{E_n}\) en (5.2),

\[
(1-2s_n)I_{E_n}
=-\sum_{a<b}c_{a,b}S_{a,b}|_{E_n}.
\tag{5.4}
\]

El coeficiente no se anula para ningún entero \(n\):

\[
1-2s_n
=1-\frac{(n-1)(5-n)}6
=\frac{n^2-6n+11}{6}
=\frac{(n-3)^2+2}{6}>0.
\tag{5.5}
\]

En consecuencia,

\[
I_{E_n}\in
\operatorname{span}\{S_{a,b}|_{E_n}:a<b\}.
\tag{5.6}
\]

Ahora (4.4) implica que cada \(Q_{a,b}\) pertenece al span de los
\(S_{a,b}|_{E_n}\). Junto con (4.9),

\[
\boxed{
\operatorname{span}\{S_{a,b}|_{E_n}:a<b\}
=\operatorname{Sym}(E_n).
}
\tag{5.7}

Como cada \(S_{a,b}\) es una suma de clase \(A_{C_{a,b}}\) salvo un factor
no nulo, (5.7) demuestra (2.2). Por la reducción del preflight queda probado
el Teorema 1.

## 6. Consecuencias exactas

### 6.1 Saturación universal y nesting estricto

De (1.2),

\[
V_n=\operatorname{Sym}^2P_{n-1}
\subsetneq
\operatorname{Sym}^2P_n=V_{n+1},
\tag{6.1}
\]

porque \(P_{n-1}\subsetneq P_n\). Por tanto

\[
\boxed{V_n\subsetneq V_{n+1}\qquad(n\ge2).}
\tag{6.2}
\]

La sucesión de rangos es exactamente

\[
\boxed{1,3,6,10,15,\ldots,\frac{n(n-1)}2,\ldots.}
\tag{6.3}
\]

### 6.2 Witness universal de cada nuevo grado

Sea \(p_n\) el modo ortogonal de grado \(n\). Entonces

\[
p_1\otimes p_n+p_n\otimes p_1
\in V_{n+1}\setminus V_n.
\tag{6.4}
\]

Como la forma Fisher es positiva definida sobre \(V_{n+1}\) y se anula sobre
\(V_n^\perp\),

\[
\boxed{
I_n^{[P]}(p_1\otimes p_n)=0,
\qquad
I_{n+1}^{[P]}(p_1\otimes p_n)>0.
}
\tag{6.5}
\]

Aquí se usa, como en los witnesses de §§14--15, que la parte simétrica es
\((p_1\otimes p_n+p_n\otimes p_1)/2\) y que la parte antisimétrica está en el
kernel para toda cardinalidad.

### 6.3 Densidad del sector visible acumulado

Los polinomios centrados son densos en
\(H=L_0^2([0,1])\). Aplicando (1.2),

\[
\boxed{
\overline{\bigcup_{n\ge2}V_n}
=H\widehat\otimes_{\mathrm{sym}}H.
}
\tag{6.6}
\]

Esto ya no es condicional.

### 6.4 Kernel permanente

Para todo \(n\), el cociente a posets no etiquetados es invariante bajo
intercambio de las dos coordenadas. Por tanto

\[
\boxed{
\bigwedge^2H\subseteq\ker G_{[P]}^{(n)}
\qquad\text{para todo }n,
}
\tag{6.7}
\]

y, combinando (1.2) con la descomposición simétrica/antisimétrica,

\[
\boxed{
\ker G_{[P]}^{(n)}
=\left(\operatorname{Sym}^2P_{n-1}\right)^{\perp_{\rm sym}}
\oplus\bigwedge^2H.
}
\tag{6.8}
\]

El primer complemento de (6.8) se toma dentro del producto tensorial
simétrico. La suma ortogonal completa se entiende dentro de
\(H\widehat\otimes H
=(H\widehat\otimes_{\mathrm{sym}}H)\oplus\bigwedge^2H\).

## 7. Techo físico y bibliográfico

El teorema da una versión precisa de recuperación progresiva **tangente** en
S1:

```text
PROGRESSIVELY_DENSE_RECOVERY = symmetric S1 interaction sector only
PERMANENT_INFORMATION_LOSS = antisymmetric S1 interaction sector
FINITE_N_RESOLUTION = polynomial degree at most n-1 in each coordinate
```

No afirma reconstrucción no lineal de una geometría, identificabilidad a
distancia finita, recuperación de coordenadas, comportamiento fuera de S1 ni
ningún resultado sobre Schwarzschild, horizontes o dimensión mayor.

Tampoco certifica novedad. Bombelli sigue siendo el antecedente del marco
estadístico y Surya el vecino directo de resolución creciente mediante
abundancias de intervalos. La aportación matemática estrecha que debe someterse
a revisión externa es la caracterización exacta (1.2), su prueba por sumas de
clase y las consecuencias (6.2)--(6.8).

```text
FRAMEWORK_NOVELTY = NO
MORE_N_MORE_RESOLUTION_NOVELTY = NO
FULL_CLASS_SUM_RANK_THEOREM = PROVED_IN_PROJECT
EXTERNAL_MATHEMATICAL_REVIEW = REQUIRED
NOVELTY_CERTIFICATE = NO
N5 = UNNECESSARY_FOR_RANK_THEOREM
```
