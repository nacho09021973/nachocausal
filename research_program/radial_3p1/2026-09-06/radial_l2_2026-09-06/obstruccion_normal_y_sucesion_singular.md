# Un obstáculo explícito para la unicidad radial L²: el modelo del borde lateral

Fecha: 2026-09-06.

**Resultado y límite.** No se demuestra aquí que el núcleo del operador completo sea unidimensional, ni se construye un elemento adicional de ese núcleo. Se demuestra algo más preciso que «falta una estimación»: **la estimación coerciva L², incluso módulo el modo temporal y bajo la condición diagonal exacta, es falsa**. Se construye una sucesión singular que lo prueba. Además, se identifica otro modelo de frontera, el del borde lateral, cuyo núcleo L² es infinito-dimensional. Esto explica un mecanismo concreto de pérdida de compacidad que la inyectividad del modelo isotrópico del vértice no elimina.

La fuente del operador y de la condición diagonal es la nota local
`/home/adnac/analisis_kernel_conforme_2026-09-06.md`, especialmente sus fórmulas (9)-(10). Las demostraciones siguientes son directas; no dependen de un teorema externo de cálculo de operadores de borde.

## 1. Convenciones y enunciado

Trabajamos en el cuadrado (Q=(0,1)^2), con medida de Lebesgue, y en su subespacio antisimétrico (H_\mathrm{alt}). Para evitar ambigüedades de signo en el operador reflejado, definimos explícitamente

\[
Lf(x)=\frac1x\int_0^x(x-s)f(s)\,ds,
\quad C_0f(x)=\frac1{x^2}\int_0^x sf(s)\,ds,
\quad C=(1-x)C_0,
\]
\[
R_+f(x)=\frac1{1-x}\int_x^1(s-x)f(s)\,ds,
\quad Ef(x)=\frac{x}{(1-x)^2}\int_x^1(1-s)f(s)\,ds.
\]

Con esta **convención positiva** para (R_+), la expresión del operador compatible con la reducción de Markov de la nota anterior es

\[
Kg=(y-x)g+6(L\otimes C-C\otimes L-R_+\otimes E+E\otimes R_+)g.
\tag{1}
\]

Si se escribe el último par con el signo (+R\otimes E-E\otimes R), debe usarse (R=-R_+). En particular, (1) da exactamente (K[(y-x)(x+y-1)]=0). El signo se ha comprobado también contra la identidad de Markov en un polinomio que no está en el núcleo.

Sea (d=y-x), (g_t=d(x+y-1)), y

\[
A_g(z)=\int_{0<s<t<z}(t-s)g(s,t)\,ds\,dt,
\quad B_g(z)=\int_{z<s<t<1}(t-s)g(s,t)\,ds\,dt,
\]
\[
\mathcal D_g(z)=\frac{1-z}{z^2}A_g(z)+\frac{z}{(1-z)^2}B_g(z).
\tag{2}
\]

**Teorema.** Existe una sucesión real (v_n\in H_\mathrm{alt}) tal que

\[
\boxed{
\|v_n\|_2=1,\quad
v_n\rightharpoonup0,\quad
\langle v_n,g_t\rangle=0,\quad
\mathcal D_{v_n}\equiv0,\quad
\|Kv_n\|_2\longrightarrow0.
}
\tag{3}
\]

También puede imponerse, y nuestra construcción lo hace,

\[
\int_{s<t}(t-s)v_n(s,t)\,ds\,dt=0.
\tag{4}
\]

La velocidad obtenida es (O(n^{-1/2})). La corrección que hace exacta la condición diagonal tiene norma (O(e^{-3n/2})).

Por tanto no existen una constante (C) y un operador compacto (J), hacia un espacio normado cualquiera, que den

\[
\|v\|_2\le C(\|Kv\|_2+\|Jv\|)
\tag{5}
\]

para todo (v\perp g_t) con (\mathcal D_v=0). En particular, (K) restringido a ese subespacio no es superiormente semi-Fredholm: no puede tener simultáneamente núcleo finito-dimensional e imagen cerrada.

Esto **no implica** que exista un segundo vector exacto del núcleo.

## 2. El modelo lateral y su núcleo

La variable apropiada cerca de (x=0), manteniendo (y) sin reescalar, es (t=-\log x). La transformación unitaria unidimensional es

\[
(Uf)(t)=e^{-t/2}f(e^{-t}).
\]

Una sustitución directa da

\[
UC_0U^{-1}F(t)=\int_0^\infty e^{-3r/2}F(t+r)\,dr.
\tag{6}
\]

En particular, (\|C_0\|\le2/3). Sobre la recta logarítmica completa llamemos (H) al operador de (6). El modelo lateral que queda de (1) es

\[
(\mathcal NG)(t,y)=yG(t,y)-6\int_0^\infty e^{-3r/2}(L_yG)(t+r,y)\,dr.
\tag{7}
\]

El cálculo con tensores de la sección 4 justifica esta extracción del término principal sin presuponer ningún formalismo microlocal.

Usando modos (e^{-i\tau t}), sus fibras son

\[
N(\tau)=M_y-\frac6{3/2+i\tau}L_y.
\tag{8}
\]

Escribamos

\[
\beta(\tau)=\frac{-3+\sqrt{1+24/(3/2+i\tau)}}2,
\tag{9}
\]

con la raíz de parte real positiva. Entonces

\[
N(\tau)y^{\beta(\tau)}=0
\quad\text{si}\quad \Re\beta(\tau)>-\tfrac12.
\tag{10}
\]

En efecto,

\[
L(y^\beta)=\frac{y^{\beta+1}}{(\beta+1)(\beta+2)}.
\]

Para (\tau=0),

\[
\boxed{\beta=\frac{\sqrt{17}-3}{2}=0.5615528128\ldots,
\qquad yh=4Lh,\quad h(y)=y^\beta.}
\tag{11}
\]

Hay un intervalo abierto (I) alrededor de cero en el que (10) sigue siendo L². Para cualquier (a\in L^2(I)), con soporte en un compacto de (I),

\[
G(t,y)=\frac1{\sqrt{2\pi}}\int_I a(\tau)e^{-i\tau t}y^{\beta(\tau)}\,d\tau
\tag{12}
\]

pertenece a (L^2(\mathbb R\times(0,1))) y satisface (\mathcal NG=0). Esto se sigue de Plancherel y de la cota uniforme de (\|y^{\beta(\tau)}\|_2) en ese compacto. Para obtener funciones reales basta imponer (a(-\tau)=\overline{a(\tau)}).

Así, **el modelo lateral posee un núcleo L² infinito-dimensional**, aunque el modelo isotrópico antisimétrico del vértice sea inyectivo.

El margen (6<8) de la prueba previa por momentos no proporciona una separación coerciva: para un coeficiente general positivo (\lambda), la misma fibra en (\tau=0) tiene una raíz L² en cuanto (2\lambda/3>3/4), es decir, (\lambda>9/8). Son dos umbrales de naturaleza diferente.

La fibra también se clasifica directamente: al derivar dos veces (y^2h=\kappa I^2h), se obtiene

\[
y^2h''+4yh'+(2-\kappa)h=0,
\quad \kappa=6/(3/2+i\tau).
\]

La otra raíz tiene suma (-3) con (\beta(\tau)), y no es L² cuando (10) es L². Las condiciones de integración en cero se cumplen para la raíz admisible. Por tanto, en (I), el núcleo de cada fibra es exactamente unidimensional.

## 3. Una sucesión crítica con dos momentos exactamente nulos

Sea (\varepsilon=e^{-n}), con (n\to\infty), y

\[
a_n^{(0)}(x)=\frac{x^{-1/2}}{\sqrt n}\mathbf1_{(\varepsilon^2,\varepsilon)}(x).
\tag{13}
\]

Tiene norma uno, soporte que se aproxima al borde, y converge débilmente a cero. Por (6), o integrando directamente en las dos discontinuidades de su perfil logarítmico,

\[
\|(C_0-\tfrac23)a_n^{(0)}\|_2=O(n^{-1/2}).
\tag{14}
\]

Para disponer de cancelaciones exactas, pongamos

\[
r_0=2(1-\sqrt\varepsilon),\qquad
r_1=\tfrac23(1-\varepsilon^{3/2}),
\]
\[
p_0=4r_0-6r_1,\qquad p_1=-6r_0+12r_1,
\]
\[
a_n(x)=a_n^{(0)}(x)
-\frac{\varepsilon^{-1/2}}{\sqrt n}
\left(p_0+p_1\frac{x}{\varepsilon}\right)\mathbf1_{(0,\varepsilon)}(x).
\tag{15}
\]

La matriz de momentos de (1,u) en ((0,1)) es

\[
\begin{pmatrix}1&1/2\\1/2&1/3\end{pmatrix},
\quad\text{con inversa}\quad
\begin{pmatrix}4&-6\\-6&12\end{pmatrix}.
\]

Por ello

\[
\int a_n=\int xa_n=0,
\qquad
\|a_n\|_2^2=1-\frac{r_0p_0+r_1p_1}{n}\longrightarrow1.
\tag{16}
\]

La modificación tiene norma (O(n^{-1/2})), de modo que (14) sigue siendo cierta para (a_n).

Ambos momentos nulos implican que (La_n) y (C_0a_n) también tienen soporte en ((0,\varepsilon)). Por escala y por las fórmulas de los operadores,

\[
\|Ma_n\|_2+\|La_n\|_2=O(\varepsilon),
\quad
\|Ca_n-\tfrac23a_n\|_2=O(n^{-1/2}+\varepsilon),
\tag{17}
\]
\[
\|R_+a_n\|_2+\|Ea_n\|_2=O(\varepsilon^2).
\tag{18}
\]

Para (18) se pueden usar, sobre ese soporte, las identidades exactas

\[
R_+a_n=\frac{x}{1-x}La_n,
\qquad
Ea_n=-\frac{x}{(1-x)^2}\int_0^x(1-s)a_n(s)\,ds.
\]

## 4. Cancelación en el operador completo

Sea (h(y)=y^\beta) con (11), (h_\varepsilon=h\mathbf1_{(\varepsilon,1)}), y

\[
w_n=a_n\otimes h_\varepsilon-h_\varepsilon\otimes a_n.
\tag{19}
\]

Los soportes unidimensionales son disjuntos. En consecuencia,

\[
\|w_n\|_2^2=2\|a_n\|_2^2\|h_\varepsilon\|_2^2
\longrightarrow2\|h\|_2^2>0,
\quad w_n\rightharpoonup0.
\]

Escribamos (S(u,v)=u\otimes v+v\otimes u). La fórmula (1) da exactamente

\[
\begin{split}
K(a\wedge h)={}&S(a,Mh)-S(Ma,h)
+6S(La,Ch)-6S(Ca,Lh)\\
&-6S(R_+a,Eh)+6S(Ea,R_+h).
\end{split}
\tag{20}
\]

En (20), el término principal es

\[
S(a_n,Mh_\varepsilon-4Lh_\varepsilon),
\]

que tiende a cero porque (Mh=4Lh) y (h_\varepsilon\to h) en L². Más precisamente, su norma es (O(\varepsilon^{\beta+1/2})), suficiente aquí. Todos los demás términos se controlan con (17)-(18). Resulta

\[
\boxed{\|Kw_n\|_2=O(n^{-1/2}).}
\tag{21}
\]

No se han omitido los términos reflejados ni la región exterior al soporte inicial.

El mismo argumento sirve para (\mathcal H_6), reemplazando (C) por (C_0) y omitiendo el par reflejado.

## 5. La condición diagonal: primero casi exacta

Para (w_n), los dos momentos de (a_n) dan

\[
A_{w_n}(z)=0\quad\text{para todo }z.
\tag{22}
\]

Si (z\le\varepsilon), el triángulo inferior no encuentra el soporte de (h_\varepsilon). Si (z>\varepsilon), contiene todo el soporte de (a_n), y las dos integrales se anulan por (16).

Por tanto esta sucesión **ya satisface exactamente la condición diagonal del modelo del vértice**. Para el operador completo queda

\[
\mathcal D_{w_n}(z)=\frac{z}{(1-z)^2}B_\times(z),
\quad \operatorname{supp}B_\times\subset[0,\varepsilon],
\tag{23}
\]

donde, poniendo (H_j=\int_\varepsilon^1t^jh(t)\,dt),

\[
B_\times(z)=-H_1\int_0^za_n(s)\,ds
+H_0\int_0^zsa_n(s)\,ds.
\tag{24}
\]

En particular (B_\times(0)=B_\times(\varepsilon)=0),

\[
B_\times'(z)=-(H_1-zH_0)a_n(z),
\quad |B_\times(z)|\le C\sqrt z\,\|a_n\|_2.
\tag{25}
\]

El defecto diagonal es (O(\varepsilon^{3/2})) uniformemente. La siguiente construcción lo elimina **exactamente**.

## 6. Corrección exacta en un cuadrado pequeño

Buscamos una corrección antisimétrica (u_n), soportada en ((0,\varepsilon)^2), de la forma

\[
u_n(s,t)=(t-s)k(t),\qquad 0<s<t<\varepsilon.
\tag{26}
\]

Su espacio natural es (W=L^2((0,\varepsilon),t^3dt)), porque

\[
\|u_n\|_{L^2(Q)}^2=\frac23\|k\|_W^2.
\tag{27}
\]

Las dos integrales triangulares son

\[
A_c(z)=\frac13\int_0^zt^3k(t)\,dt,
\qquad
B_c(z)=\frac13\int_z^\varepsilon(t-z)^3k(t)\,dt.
\tag{28}
\]

La condición (\mathcal D_{w_n+u_n}=0), para (0<z<\varepsilon), equivale a

\[
A_c(z)=-c(z)[B_\times(z)+B_c(z)],
\qquad c(z)=\frac{z^3}{(1-z)^3}.
\tag{29}
\]

Al derivar (29) obtenemos (k=F+Tk), con

\[
F(z)=-\frac{9B_\times(z)}{z(1-z)^4}
-\frac{3B_\times'(z)}{(1-z)^3},
\tag{30}
\]
\[
(Tk)(z)=-\frac{9B_c(z)}{z(1-z)^4}
+\frac3{(1-z)^3}\int_z^\varepsilon(t-z)^2k(t)\,dt.
\tag{31}
\]

Tras conjugar por (k\mapsto z^{3/2}k), los dos núcleos están acotados en valor absoluto por

\[
\frac{3z^{1/2}t^{3/2}}{(1-\varepsilon)^4}\mathbf1_{z<t},
\qquad
\frac{3z^{3/2}t^{1/2}}{(1-\varepsilon)^3}\mathbf1_{z<t}.
\]

Sus normas Hilbert–Schmidt dan

\[
\|T\|_{W\to W}\le\varepsilon^3
\left[\frac{\sqrt3}{2(1-\varepsilon)^4}
+\frac{\sqrt{3/8}}{(1-\varepsilon)^3}\right]<0.066
\quad (\varepsilon\le1/4).
\tag{32}
\]

Además, (25) y Cauchy–Schwarz implican

\[
\|F\|_W\le C\varepsilon^{3/2}\|a_n\|_2.
\tag{33}
\]

Así, la serie convergente (k=(I-T)^{-1}F) proporciona una corrección exacta con

\[
\boxed{\|u_n\|_2=O(\varepsilon^{3/2}).}
\tag{34}
\]

La ecuación diferenciada no ha perdido una constante: ambos miembros de (29) tienden a cero en (z=0). En (z=\varepsilon), (B_\times=B_c=0), luego (A_c(\varepsilon)=0). Para (z>\varepsilon), (A_c) permanece cero y ambos términos superiores son cero. Por ello la condición diagonal se cumple en **todo** ((0,1)).

También (A_{w_n+u_n}(1)=0), lo que prueba (4) antes de proyectar.

## 7. Finalización de la sucesión singular

Los operadores (L,R_+) son Hilbert–Schmidt y (C,E) son acotados por Hardy, de modo que (K) es acotado en L². En consecuencia, (21) y (34) dan

\[
\|K(w_n+u_n)\|_2=O(n^{-1/2}).
\]

Proyectamos ahora exactamente fuera de (g_t):

\[
\widetilde v_n=w_n+u_n
-\frac{\langle w_n+u_n,g_t\rangle}{\|g_t\|_2^2}g_t,
\qquad v_n=\widetilde v_n/\|\widetilde v_n\|_2.
\tag{35}
\]

El coeficiente proyectado tiende a cero por convergencia débil. Puesto que (Kg_t=0), (\mathcal D_{g_t}=0) y (\int_{s<t}(t-s)g_t=0), las tres condiciones exactas se conservan. La norma del denominador tiene límite positivo. Esto prueba (3)-(4).

Si (5) fuese cierta, la compacidad daría (Jv_n\to0), contradiciendo (\|v_n\|_2=1). Equivalentemente, cero pertenece al espectro esencial del operador positivo (K_V^*K_V), donde (K_V) es la restricción a

\[
V=\{g\in H_\mathrm{alt}:\mathcal D_g=0,\ g\perp g_t\}.
\]

Este subespacio es cerrado: cada evaluación interior de (\mathcal D_g) es un funcional L² acotado.

## 8. Dónde se pierde la masa

La sucesión no se concentra en la diagonal interior. Antes de correcciones tiene soporte en dos rectángulos disjuntos:

\[
(0,\varepsilon)\times(\varepsilon,1),
\quad (\varepsilon,1)\times(0,\varepsilon).
\]

Las correcciones tienden a cero en norma. Para cualquier función continua (\varphi) en el cuadrado cerrado, la sucesión normalizada satisface

\[
\lim_n\int_Q\varphi(x,y)|v_n(x,y)|^2dxdy
=\frac1{2\|h\|_2^2}
\int_0^1[\varphi(0,y)+\varphi(y,0)]y^{2\beta}dy.
\tag{36}
\]

La medida límite está en los bordes laterales y **no tiene átomos en los vértices**. Su masa cerca de ((0,0)) decrece como (\delta^{2\beta+1}). El mecanismo es la concentración en una variable, a escalas logarítmicas cada vez más largas, mientras la otra mantiene el perfil (y^\beta).

Para (\mathcal H_6), la sucesión (w_n) ya tiene su traza diagonal exacta nula por (22), y su residuo también tiende a cero. Así, incluso el modelo de vértice inyectivo posee esta pérdida de coercividad.

## 9. Una identidad global adicional

Para cualquier (f\in L^2(0,1)), Fubini da

\[
\int Lf=\int Cf,
\qquad \int R_+f=\int Ef.
\]

Los cuatro términos tensoriales de (1) se cancelan al integrar en el cuadrado. Por ello

\[
\int_Q Kg=\int_Q(y-x)g.
\tag{37}
\]

Toda solución exacta tiene (B_g(0)=0). Este hecho cancela el momento global que podría alimentar el primer término no local del vértice, pero no elimina la obstrucción: nuestra sucesión satisface esa cancelación exactamente.

## 10. Qué queda abierto, ahora con un obstáculo identificado

La inyectividad del modelo isotrópico no basta para una prueba por compacidad. El problema no es simplemente que no se haya encontrado una buena constante: (3) prueba que **ninguna constante de ese tipo existe en la norma L² original**, incluso con la condición diagonal exacta y cualquier resto compacto.

El nuevo dato que una prueba debe afrontar es el núcleo lateral (8)-(12). Una solución adicional del operador completo tendría que satisfacer además las compatibilidades globales y entre escalas; nuestros modos aproximados no lo demuestran. La existencia de vectores aproximados no permite corregirlos automáticamente a vectores exactos: precisamente falta una inversa acotada.

Una vía aún posible sería demostrar que **las soluciones exactas** no pueden realizar los coeficientes de esos modos laterales, utilizando la ecuación global, o encontrar una identidad de energía/dualidad que determine el núcleo sin necesitar imagen cerrada. Una estimación con una norma más fuerte o una condición adicional podría ser válida, pero habría que demostrar que todas las soluciones L² la satisfacen; no puede suponerse.

Por tanto, el desenlace de esta investigación es una obstrucción normal explícita y demostrada, no una prueba completa de unicidad ni un contraejemplo exacto.

## 11. Comprobaciones reproducibles

`verify_edge_sequence.py` comprueba con SymPy:

- (Kg_t=0) con la convención de signos explícita;
- la identidad de Markov suministrada, en un polinomio ajeno al núcleo y un punto racional;
- los dos momentos exactamente nulos de (15);
- la ecuación característica (11);
- la identidad diferencial de la corrección diagonal y la cota de Neumann (32).

También evalúa el residuo del operador completo sobre (19), antes de la corrección de esquina, mediante matrices de Gram de los tensores separados y cuadratura logarítmica. La corrección exacta se justifica analíticamente por (29)-(34); no se presenta la cuadratura como comprobación de esa corrección ni como prueba de unicidad.

| (n) | (\|Kw_n\|_2/\|w_n\|_2) | (\sqrt n\) por ese cociente |
|---:|---:|---:|
| 16 | 0.1791707632 | 0.7166830527 |
| 32 | 0.1134601656 | 0.6418276201 |
| 64 | 0.0764948565 | 0.6119588518 |
| 128 | 0.0529010946 | 0.5985075641 |

El refinamiento de 24 a 40 nodos por intervalo logarítmico en (n=128) cambia el cociente menos de (10^{-9}). Las pruebas de (3) y del núcleo de (7) son analíticas y no dependen de esos números.

Como verificación independiente de la corrección de esquina, el programa aplica (29)-(31) a un perfil de Legendre de grado dos, con sus dos momentos nulos, a escala (\varepsilon=0.1). Resuelve la ecuación triangular discretizada con 80, 160 y 320 nodos y evalúa luego las integrales originales de (\mathcal D) en nueve puntos. El defecto máximo es menor de (8\times10^{-15}), y el momento total corregido es menor de (2\times10^{-16}). Esta comprobación a escala finita permite detectar errores de signo que quedarían ocultos al usar únicamente correcciones exponencialmente pequeñas.
