# Un resultado L² para el modelo de vértice del operador conforme

Fecha: 2026-09-06.

**Estado:** esta nota no demuestra la unicidad para el operador completo K y no construye un contraejemplo. Demuestra la inyectividad L² de su modelo de escala en un vértice, mediante identidades de momentos válidas por aproximación en L². Incluye una consecuencia precisa para límites de reescalados y una reconstrucción explícita de la reducción de Markov.

## 1. Teorema para el modelo de vértice

En H_a=L²(0,a), a>0, sean

\[
L_0f(x)=\frac1x\int_0^x(x-s)f(s)\,ds,
\qquad C_0f(x)=\frac1{x^2}\int_0^x sf(s)\,ds.
\]

Definimos, sobre funciones antisimétricas,

\[
\mathcal H_\lambda g=(y-x)g+
\lambda(L_0\otimes C_0-C_0\otimes L_0)g.
\]

**Teorema.** Para todo λ real con λ≤8,

\[
\ker(\mathcal H_\lambda\vert_{\Lambda^2H_a})=\{0\}.
\]

En particular, esto vale para el coeficiente físico λ=6. No se afirma que el umbral 8 sea óptimo.

### 1.1. Una primitiva que conserva las condiciones en x=0 e y=0

Pongamos D_x=x∂_x, D_y=y∂_y, y

\[
u(x,y)=\frac1{x^2y^2}
\int_0^x\int_0^y (x-s)(y-t)g(s,t)\,dt\,ds.
\]

Entonces u es antisimétrica y, en distribuciones,

\[
g=(D_x+1)(D_x+2)(D_y+1)(D_y+2)u.
\tag{1}
\]

Además,

\[
(L_0\otimes C_0)g=x(D_y+1)u,
\qquad (C_0\otimes L_0)g=y(D_x+1)u.
\tag{2}
\]

Es esencial usar esta primitiva definida por integrales: una solución arbitraria de (1) podría contener términos de integración singulares que no corresponden a g.

Por Cauchy–Schwarz,

\[
|u(x,y)|\leq\frac{\|g\|_{L^2((0,x)\times(0,y))}}{3\sqrt{xy}}.
\tag{3}
\]

Para n≥1 definimos

\[
U_n(y)=\int_0^y x^{n-1}u(x,y)\,dx.
\]

Con ε(y)=‖g‖_{L²((0,y)²)}→0, (3) implica

\[
|U_n(y)|\leq
\frac{\varepsilon(y)}{3(n-\tfrac12)}y^{n-1},
\qquad U_n(y)=o(y^{n-1}).
\tag{4}
\]

### 1.2. La traza diagonal se obtiene de L², no se impone

El término T₀g=(L₀⊗C₀−C₀⊗L₀)g es continuo en el interior: sus núcleos de evaluación dependen continuamente de x,y en L². Si λ≠0 y H_λg=0, necesariamente

\[
T_0g(y,y)=0.
\]

En caso contrario, g=−λT₀g/(y−x) no sería localmente L² en un entorno de un punto de la diagonal.

Las primeras derivadas de u son continuas en el interior, directamente por su representación integral. Sea

\[
q(y)=\partial_yu(y,y).
\]

La antisimetría y (2) dan

\[
T_0g(y,y)=2y^2q(y).
\]

Por tanto q=0 para una solución exacta. El caso λ=0 es inmediato y se puede excluir en lo que sigue.

### 1.3. Identidad de momentos con todos los términos diagonales

Escribamos D=y∂_y y A=(D+1)(D+2). Para cualquier g antisimétrica en L², no necesariamente solución, se tiene en distribuciones sobre (0,a):

\[
\begin{split}
\int_0^y x^{n-1}(\mathcal H_\lambda g)(x,y)\,dx
={}&y(1-n)\big[(2-n)A-\lambda\big]U_n\\
&-(D+1)\big[n(n-1)(D+2)-\lambda\big]U_{n+1}\\
&+y^{n+3}q'(y)+(2n+2)y^{n+2}q(y).
\end{split}
\tag{5}
\]

Justificación de las trazas y de la integración por partes: se demuestra primero para aproximaciones suaves antisimétricas g_j. Para ellas u_j(x,x)=0 y ∂_x∂_yu_j(x,x)=0; en consecuencia q_j'=∂²_yu_j(y,y). Integrando el operador en x, su adjunto formal es

\[
\big[(D_x+1)(D_x+2)\big]^*\phi=x^2\phi''.
\]

Se aplica con φ=x^{n−1}(y−x). Los términos diagonales que quedan son exactamente la última línea de (5). Al pasar g_j→g en L², H_λg_j→H_λg en L², U_{n,j}→U_n localmente, y q_j→q uniformemente en compactos interiores por las fórmulas integrales de las primeras derivadas de u. Las derivadas de q_j convergen en distribuciones. Esto prueba (5) sin suponer trazas clásicas de derivadas de orden superior de g o u.

Para una solución exacta, H_λg=0 y q=0, de modo que

\[
y(1-n)\big[(2-n)(D+1)(D+2)-\lambda\big]U_n
-(D+1)\big[n(n-1)(D+2)-\lambda\big]U_{n+1}=0.
\tag{6}
\]

### 1.4. Se anulan todos los momentos

Con n=1 y λ≠0, (6) da

\[
(D+1)U_2=0.
\]

Así U₂=c/y; (4) fuerza c=0.

Supongamos U_n=0, con n≥2. Entonces

\[
(D+1)\left(D+2-\frac{\lambda}{n(n-1)}\right)U_{n+1}=0.
\tag{7}
\]

Las soluciones distribucionales de esta ecuación de Euler son combinaciones de

\[
y^{-1},\qquad y^{-2+\lambda/[n(n-1)]},
\]

o de y⁻¹ y y⁻¹log y cuando coinciden los exponentes. Para λ≤8, el segundo exponente es ≤n para todo n≥2; la igualdad sólo puede darse aquí en n=2, λ=8. Todos estos términos son incompatibles con

\[
U_{n+1}=o(y^n).
\]

Por inducción, U_n=0 para todo n≥2. Para casi todo y, la función x↦xu(x,y) es integrable y todos sus momentos polinómicos en (0,y) son cero. La densidad uniforme de los polinomios en C([0,y]) implica xu(x,y)=0 casi en todas partes. Luego u=0 y, por (1), g=0. Esto prueba el teorema.

En λ=6 los exponentes sucesivos son −1 y 1 (n=2), el exponente doble −1 (n=3), y −1 junto con un exponente menor que −1 (n≥4).

## 2. Qué implica para el problema original

Como C=(1−x)C₀ y L=L₀, el operador original satisface exactamente

\[
K g=\mathcal H_6g+
6\big[-y(L_0\otimes C_0)+x(C_0\otimes L_0)
+R\otimes E-E\otimes R\big]g.
\tag{8}
\]

Los dos primeros términos adicionales ganan un factor de escala al dilatar simultáneamente x,y hacia cero. Los términos R,E conservan información del resto del cuadrado. La reflexión da el modelo correspondiente en (1,1).

Dos consecuencias rigurosas:

1. No existe un modo homogéneo no nulo del modelo H₆ que sea antisimétrico y L² en un cuadrado de vértice. En particular, si g(rx,ry)=r^βg(x,y), con Re β>−1 y perfil angular integrable al cuadrado, no puede satisfacer H₆g=0.
2. Para una solución exacta del operador completo, los reescalados de amplitud divergente no pueden tener un límite fuerte L² no nulo, como se precisa a continuación.

### 2.1. Una obstrucción precisa a los límites de reescalados

Sean r_j↓0, c_j escalares con |c_j|→∞, y

\[
G_j(x,y)=c_j^{-1}g(r_jx,r_jy),\qquad 0<x,y<1.
\]

Si Kg=0 y G_j→G fuertemente en L²((0,1)²), entonces G=0.

En efecto, al dividir (8) evaluada en (r_jx,r_jy) por r_jc_j, la parte izquierda de Volterra se transforma en H₆G_j más un término que es O(r_j) en L² para G_j acotados. Para X,Y<r<1/2,

\[
|(R\otimes E-E\otimes R)g(X,Y)|
\leq \frac83(X+Y)\|g\|_2.
\]

Esta estimación se obtiene de ‖R_X‖₂≤2/√3 y ‖E_X‖₂≤4X/√3 para los núcleos de evaluación. El término restante, dividido por r_jc_j, tiende uniformemente a cero. Así H₆G_j→0; por continuidad y el teorema, G=0.

Por ejemplo, si ‖g(r_j·,r_j·)‖₂→∞, los reescalados normalizados a norma uno no pueden poseer una subsucesión fuertemente convergente en L². Esta conclusión no exige homogeneidad.

**Límite de este avance.** Ni la inyectividad de H₆ ni la ausencia de modos homogéneos proporcionan por sí solas una estimación de su inversa. Todavía pueden faltar compacidad de los reescalados, control de capas con x/y→0 y estimaciones para la fuente no local de R,E. Además, f=g/(y−x) puede divergir aunque g permanezca acotada o tienda a cero. El corolario de reescalados de amplitud divergente no cubre ese caso. No es legítimo concluir de (8) que el cociente f se extiende continuamente al vértice.

## 3. Núcleo explícito de Markov y condición adicional exacta

Esta reconstrucción se obtiene directamente de K; no se presupone que todo punto fijo de P resuelva K.

Para g antisimétrica, sea

\[
A(z)=\int_{0<s<t<z}(t-s)g(s,t)\,ds\,dt,
\quad
B(z)=\int_{z<s<t<1}(t-s)g(s,t)\,ds\,dt,
\]

\[
a(z)=\frac{1-z}{z^2},\quad b(z)=\frac{z}{(1-z)^2},
\quad \mathcal D(z)=a(z)A(z)+b(z)B(z).
\]

Para una solución exacta de K, el mismo argumento L² en la diagonal da D=0.

Pongamos d=y−x, f=g/d. Un núcleo de la reducción de Markov es

\[
p(x,y;s,t)=
\begin{cases}
\displaystyle\frac{6s(x+y-xy-t)(t-s)}{d x^2y^2},
&0<s<x<t<y,\\[4pt]
\displaystyle\frac{6}{d^2}\left(\frac{1-y}{y^2}+\frac{x}{(1-x)^2}\right)(t-s)^2,
&x<s<t<y,\\[4pt]
\displaystyle\frac{6(1-t)(s-xy)(t-s)}{d(1-x)^2(1-y)^2},
&x<s<y<t<1,\\[4pt]
0,&\text{en los demás casos.}
\end{cases}
\tag{9}
\]

Es no negativo. La integración directa da P1=1, P(s+t)=x+y, P(st)=(x+y)²/4 y Ph=(9/10)h para la h del enunciado.

La identidad exacta, para x<y, es

\[
K g(x,y)=d^2\,[f(x,y)-Pf(x,y)]
+6[\mathcal D(x)+\mathcal D(y)].
\tag{10}
\]

En particular,

\[
Kg=0\quad\Longleftrightarrow\quad Pf=f\ \text{y}\ \mathcal D=0
\]

en el espacio natural y con las igualdades casi en todas partes correspondientes. Para puntos interiores de Δ las integrales de P están bien definidas por Cauchy–Schwarz aplicada a g.

Una comprobación útil es f=1: entonces D(z)=z(1−z)/12 y

\[
K(y-x)=\frac{x(1-x)+y(1-y)}2\ne0.
\]

Para f=x+y−1, D=0. Así se mantiene explícita la diferencia entre la condición de punto fijo y la ecuación original.

## 4. Verificación y alcance

La prueba principal es analítica. Se verificó además con aritmética simbólica la identidad (5), incluidos los términos q y q′, en ejemplos polinómicos antisimétricos con traza diagonal derivada nula y no nula. También se comprobaron las identidades de P citadas arriba. Estas comprobaciones no sustituyen la prueba por aproximación L².

El resultado establecido es la inyectividad del modelo H₆ y el corolario de reescalados. La igualdad ker K=span{(y−x)(x+y−1)} sigue sin demostrarse en esta nota.
