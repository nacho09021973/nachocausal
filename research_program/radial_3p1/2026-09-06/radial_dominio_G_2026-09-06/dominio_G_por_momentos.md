# Dominio de G: cierre, criterio exacto por momentos y modelo normal de reconstrucción

Fecha: 2026-09-06.

**Resultado principal.** Se caracteriza exactamente el dominio de admisibilidad mediante una sucesión creciente de formas cuadráticas en los momentos unidimensionales de \(b\). Todas sus matrices se calculan por operaciones finitas sobre polinomios, con coeficientes racionales:
\[
\boxed{b\in\mathcal D(G)\iff \sup_{N\ge0}Q_N(b)<\infty.}
\]
En ese caso, \(\|Gb\|_2^2=\lim_NQ_N(b)\). No aparece una reconstrucción desconocida \(W_b\) en la definición de \(Q_N\).

Esto es una caracterización por sumabilidad global; no es todavía una clasificación del dominio mediante un espacio de Sobolev, una familia finita o coeficientes asintóticos de borde. No determina la dimensión de \(\ker(I-T)\). En particular, una sección finita del criterio no prueba admisibilidad.

La entrada analítica es la identidad positiva de la [nota anterior](../radial_l2_global_2026-09-06/energia_positiva_y_reduccion_de_borde.md). La construcción presente estudia exclusivamente el dominio de la reconstrucción; no requiere estudiar el adjunto de \(I-T\).

## 1. Notación y ecuación de reconstrucción

Trabajamos en \(Q=(0,1)^2\), \(H_{\rm alt}\subset L^2(Q)\). Ponemos
\[
a(x)=x(1-x),\quad \omega=a(x)a(y),\quad d=y-x,\quad m=x+y-1,
\]
\[
c_x=(1-x)^2(1-y)+x^2y,\qquad
c_y=(1-x)(1-y)^2+xy^2,\qquad
\mathcal X=-c_x\partial_x+c_y\partial_y.
\]
Sea \(S\) el inverso de Dirichlet de \(\partial_x^2\), \(J=a^{-1}S\). Para \(g\in H_{\rm alt}\),
\[
w_g=(S\otimes S)g,\qquad W_g=(J\otimes J)g,\qquad w_g=\omega W_g.
\]
Sea \(B\) el dato canónico de la nota anterior, y \(Ub(x,y)=b(x)+b(y)\). El operador acotado e inyectivo
\[
\mathscr A=K-6UB
\]
admite la fórmula exacta
\[
\mathscr A g=d\,g+6\mathcal XW_g.
\tag{1}
\]

La reconstrucción de Lax–Milgram, \(b\mapsto W_b\), resuelve
\[
\mathfrak a(W_b,V)=-12\langle b,r_V\rangle,
\quad
r_V(x)=\int_0^1\frac{\omega(x,y)V(x,y)}{y-x}\,dy.
\tag{2}
\]
Es acotada \(L^2(0,1)\to\mathcal H_{\mathcal E}\). Definimos
\[
Gb=\partial_x^2\partial_y^2(\omega W_b),\qquad
\mathcal D(G)=\{b\in L^2:Gb\in L^2(Q)\}.
\]
La unicidad de la reconstrucción implica la equivalencia fundamental
\[
\boxed{
b\in\mathcal D(G),\ g=Gb
\iff
g\in H_{\rm alt},\quad \mathscr A g=-6Ub.}
\tag{3}
\]
En la implicación de derecha a izquierda se prueba (2) con \(W_g\); la unicidad identifica \(W_g=W_b\). No se impone aquí \(Bg=b\).

## 2. G es cerrado; su dominio con norma de grafo es Hilbert

Supongamos \(b_n\in\mathcal D(G)\), \(b_n\to b\) en \(L^2(0,1)\) y \(Gb_n\to g\) en \(L^2(Q)\). La acotación de \(\mathscr A\) y \(U\), aplicada a (3), da
\[
\mathscr A g=-6Ub.
\]
Por (3), \(b\in\mathcal D(G)\) y \(Gb=g\). Por tanto,
\[
\boxed{G\text{ es un operador cerrado}.}
\tag{4}
\]
No se ha supuesto, ni se concluye, que su dominio sea denso o todo \(L^2\).

En consecuencia, el dominio con norma
\[
\|b\|_{\mathcal D(G)}^2=\|b\|_2^2+\|Gb\|_2^2
\tag{5}
\]
es un espacio de Hilbert. Como \(B\) es acotado en el espacio original,
\[
T=BG:\mathcal D(G)_{\rm grafo}\longrightarrow L^2(0,1)
\]
es acotado. Esto no prueba que \(T\) sea cerrado como operador en el \(L^2\) sin norma de grafo.

Hay además una propiedad útil:
\[
\operatorname{Ran}G
=\{g\in H_{\rm alt}:\mathscr A g\in\operatorname{Ran}U\}
\quad\text{es cerrado en }H_{\rm alt}.
\tag{6}
\]
En efecto,
\[
\|Ub\|_2^2=2\|b\|_2^2+2\left|\int_0^1b\right|^2,
\]
de modo que \(\operatorname{Ran}U\) es cerrado, y (6) es su preimagen por un operador acotado. También
\[
6\sqrt2\,\|b\|_2\le\|\mathscr A\|\,\|Gb\|_2.
\tag{7}
\]
En particular \(G\) es inyectivo y \(\|Gb\|_2\) es una norma completa equivalente a (5) sobre su dominio. Esta propiedad de \(G\) no proporciona coercividad \(L^2\) para \(K\).

## 3. Pruebas polinómicas que eliminan W

Sea \(P(x,y)\) un polinomio simétrico y elijamos la función de prueba
\[
\theta_P=\omega^2P.
\]
Definimos dos polinomios explícitos:
\[
\boxed{
F_P=d\,\omega^2P
-6(S\otimes S)\big[2(\mathcal X\omega)P+\omega\mathcal XP\big],}
\tag{8}
\]
\[
\boxed{
r_P(z)=a(z)^2\int_0^1a(y)^2P(z,y)\,dy.}
\tag{9}
\]
El polinomio \(F_P\) es antisimétrico. Para todo \(g\in H_{\rm alt}\),
\[
\boxed{\langle\mathscr A g,\omega^2P\rangle=\langle g,F_P\rangle.}
\tag{10}
\]
Usamos producto escalar lineal en el primer argumento. Las fórmulas siguientes se escriben con polinomios de coeficientes reales; su extensión compleja es inmediata.

**Demostración.** Por \(\operatorname{div}\mathcal X=0\) y la anulación de \(\omega^2P\) en los lados,
\[
\int_Q(\mathcal XW_g)\omega^2P
=-\int_QW_g\,\mathcal X(\omega^2P).
\]
Pero
\[
\mathcal X(\omega^2P)
=\omega[2(\mathcal X\omega)P+\omega\mathcal XP].
\]
La división por \(\omega\) que aparece al escribir \(W_g=w_g/\omega\) se cancela. Finalmente \(S\otimes S\) es autoadjunto, lo que da (8)-(10). Primero se demuestra para \(g\) suave y se pasa a \(L^2\) por continuidad de ambos lados.

El uso de \(\omega^2\) es concreto: mantiene polinómicas las pruebas después de eliminar la primitiva. Con una sola potencia de \(\omega\), esta cancelación ya no es automática.

De (3) y (10), todo dato admisible satisface
\[
\boxed{\langle Gb,F_P\rangle=-12\langle b,r_P\rangle.}
\tag{11}
\]
El factor 12 procede de la simetría de \(\theta_P\).

Nada en (8)-(9) requiere resolver una ecuación diferencial o integral. Para calcular \(S\) basta
\[
S(x^k)=\frac{x^{k+2}-x}{(k+1)(k+2)}.
\tag{12}
\]

## 4. Independencia y completitud de las pruebas F_P

Sea \(\mathcal P_N^{\rm sym}\) el espacio de polinomios simétricos de grado total a lo sumo \(N\). Usamos la base
\[
P_{ij}=
\begin{cases}
x^iy^j+x^jy^i,&i<j,\\
x^iy^i,&i=j,
\end{cases}
\qquad 0\le i\le j,\quad i+j\le N.
\tag{13}
\]
Su dimensión es \(n_N=\lfloor(N+2)^2/4\rfloor\).

**Independencia.** Si \(F_P=0\), sea \(V=d\omega P\) y
\[
g=\partial_x^2\partial_y^2(\omega V).
\]
Entonces \(W_g=V\) y \(\omega V/d=\omega^2P\). La identidad positiva anterior da
\[
0=\langle g,F_P\rangle
=\langle\mathscr A g,\omega^2P\rangle
=\mathfrak a(V,V).
\]
Tomar parte real fuerza \(\mathcal E(V)=0\), de donde \(V=0\) y \(P=0\). Por tanto todos los sistemas finitos \(\{F_{ij}\}_{i+j\le N}\) son linealmente independientes.

**Completitud.** Si \(g\in H_{\rm alt}\) es ortogonal a todos los \(F_P\), (10) implica que \(\mathscr A g\) es ortogonal a todas las funciones \(\omega^2P\). Estas son densas en el subespacio simétrico de \(L^2(Q)\): si \(h\) es ortogonal a ellas, \(\omega^2h\) es ortogonal a todos los polinomios simétricos, luego \(\omega^2h=0\), y \(h=0\) casi por doquier.

Así, \(\mathscr A g=0\). La inyectividad demostrada mediante energía obliga a \(g=0\). Hemos probado
\[
\boxed{\overline{\operatorname{span}\{F_{ij}:i\le j\}}=H_{\rm alt}.}
\tag{14}
\]
Aquí la densidad se aplica a una familia de pruebas cuya completitud se ha demostrado para todo \(L^2\); no se está deduciendo unicidad a partir del núcleo polinómico.

## 5. Caracterización exacta del dominio mediante matrices finitas

Para la base (13), definimos
\[
(M_N)_{\alpha\beta}=\int_QF_\alpha F_\beta,\qquad
(c_N(b))_\alpha=-12\int_0^1b(z)r_\alpha(z)\,dz.
\tag{15}
\]
Las matrices \(M_N\) son reales, racionales y estrictamente positivas. Pongamos
\[
\boxed{Q_N(b)=c_N(b)^*M_N^{-1}c_N(b).}
\tag{16}
\]

**Teorema.** Para todo \(b\in L^2(0,1)\):
\[
\boxed{b\in\mathcal D(G)\iff\sup_NQ_N(b)<\infty.}
\tag{17}
\]
Además \(Q_N(b)\) es creciente. Si el supremo es finito,
\[
\boxed{\|Gb\|_2^2=\lim_{N\to\infty}Q_N(b).}
\tag{18}
\]
Si \(b\notin\mathcal D(G)\), necesariamente \(Q_N(b)\to+\infty\).

**Demostración constructiva.** Sea
\[
g_N(b)=\sum_{\alpha}(M_N^{-1}c_N(b))_\alpha F_\alpha.
\tag{19}
\]
Este es el vector de menor norma que satisface las ecuaciones finitas
\(\langle g_N,F_\alpha\rangle=(c_N(b))_\alpha\), y su norma al cuadrado es \(Q_N(b)\).

Las restricciones se anidan. Para \(M\ge N\), la diferencia \(g_M-g_N\) es ortogonal al espacio generado por los primeros \(F_\alpha\), y
\[
\|g_M-g_N\|_2^2=Q_M(b)-Q_N(b).
\tag{20}
\]
En particular los \(Q_N\) son crecientes. Si están acotados, (20) muestra que \(g_N\) converge fuertemente a algún \(g\in H_{\rm alt}\). Ese límite satisface (11) para todos los polinomios simétricos. Usando (10) y la densidad de \(\omega^2P\), resulta
\[
\mathscr A g=-6Ub.
\]
La equivalencia (3) demuestra \(b\in\mathcal D(G)\) y \(g=Gb\).

Recíprocamente, si \(b\in\mathcal D(G)\), (11) muestra que \(g_N\) es la proyección ortogonal de \(Gb\) sobre \(\operatorname{span}\{F_\alpha:i+j\le N\}\). Por (14), estas proyecciones convergen a \(Gb\), lo que prueba (18).

También obtenemos la identidad exacta del error:
\[
\|Gb-g_N(b)\|_2^2=\lim_MQ_M(b)-Q_N(b).
\tag{21}
\]
Los incrementos de \(Q_N\) son energías ortogonales, no oscilaciones numéricas de una aproximación de Galerkin.

## 6. El criterio utiliza solamente N+1 momentos de b

Definamos
\[
\mu_k=\int_0^1a(z)^2z^k\,dz
=\frac{2}{(k+3)(k+4)(k+5)},
\]
\[
u_k(b)=\int_0^1a(z)^2z^kb(z)\,dz,\qquad
\mathbf u_N(b)=(u_0,\ldots,u_N)^T.
\]
Por (9),
\[
\langle b,r_{ij}\rangle=
\begin{cases}
\mu_j u_i(b)+\mu_i u_j(b),&i<j,\\
\mu_i u_i(b),&i=j.
\end{cases}
\tag{22}
\]
Sea \(R_N\) la matriz racional que realiza estas combinaciones. Entonces
\[
c_N(b)=-12R_N\mathbf u_N(b),
\qquad
H_N=144R_N^TM_N^{-1}R_N,
\]
y el teorema se escribe enteramente en una variable:
\[
\boxed{
\mathcal D(G)=
\left\{b\in L^2(0,1):
\sup_N\mathbf u_N(b)^*H_N\mathbf u_N(b)<\infty\right\}.}
\tag{23}
\]
Cada \(H_N\) tiene tamaño \((N+1)\times(N+1)\) y se calcula de antemano con aritmética racional. \(R_N\) tiene rango \(N+1\), por ejemplo usando \(P_{0j}\); por tanto \(H_N\) también es estrictamente positiva.

Este criterio no contiene \(W_b\), coeficientes singulares desconocidos ni un operador inverso global sin especificar. Consiste en integraciones de momentos de \(b\) y matrices finitas universales. Su dificultad restante es controlar su comportamiento cuando \(N\to\infty\).

El primer paso es particularmente sencillo:
\[
F_{00}=\frac{\omega d}{10}(1+2m^2+11\omega),\quad
r_{00}=\frac{a^2}{30},\quad
\|F_{00}\|_2^2=\frac{23}{12936000}.
\]
Así,
\[
\boxed{Q_0(b)=\frac{2069760}{23}\left|\int_0^1a(z)^2b(z)\,dz\right|^2.}
\tag{24}
\]

Equivalentemente, aplicar Gram–Schmidt a los \(F_{ij}\) y las mismas combinaciones lineales a los \(-12r_{ij}\) produce una base ortonormal explícita \(e_n\) de \(H_{\rm alt}\) y polinomios unidimensionales \(q_n\) tales que
\[
b\in\mathcal D(G)\iff\sum_n|\langle b,q_n\rangle|^2<\infty,
\qquad
Gb=\sum_n\langle b,q_n\rangle e_n.
\tag{25}
\]
La formulación matricial evita tener que introducir raíces cuadradas de racionales.

## 7. La admisibilidad ya contiene una familia de dimensión dos

Además del dato temporal
\[
b_t(z)=-\frac{(2z-1)(3z^2-3z+1)}{24},\qquad Gb_t=g_t,
\]
hay otro dato admisible exacto:
\[
\boxed{
b_d(z)=-\frac{3z^2-3z+1}{12},\qquad Gb_d=y-x.}
\tag{26}
\]
En efecto, una integración directa en la fórmula completa de \(K\) da
\[
K(y-x)=\frac{a(x)+a(y)}2,\qquad
B(y-x)(z)=-\frac{(2z-1)^2}{12}.
\]
Por consiguiente
\[
\mathscr A(y-x)=-6U b_d,
\]
y (3) prueba (26). Los datos \(b_d,b_t\) son independientes, respectivamente par e impar respecto de \(z\mapsto1-z\). Por tanto
\[
\operatorname{span}\{b_d,b_t\}\subset\mathcal D(G),\qquad
\dim\mathcal D(G)\ge2.
\tag{27}
\]
El segundo dato no es un punto fijo:
\[
Tb_d-b_d=\frac{a}{12}\ne0.
\tag{28}
\]
La condición de admisibilidad por sí sola no puede seleccionar únicamente \(b_t\).

Las normas exactas son
\[
\|Gb_d\|_2^2=\frac16,\qquad \|Gb_t\|_2^2=\frac1{90}.
\]
Las secciones del criterio por momentos, verificadas en aritmética racional, dan:

| \(N\) | Número de pruebas | \(Q_N(b_d)\) | \(Q_N(b_t)\) | \(Q_N(1)\) |
|---:|---:|---:|---:|---:|
| 0 | 1 | 0.0885668277 | 0 | 99.9884058 |
| 1 | 2 | 0.0885668277 | 0.0063920224 | 99.9884058 |
| 2 | 4 | 0.1168206554 | 0.0063920224 | 100.9361742 |
| 3 | 6 | 0.1168206554 | 0.0084126760 | 100.9361742 |
| 4 | 9 | 0.1316042655 | 0.0084126760 | 113.2048511 |

Estas son cotas inferiores certificadas, no aproximaciones asumidas de la norma total. La tabla no decide si \(1\in\mathcal D(G)\).

### 7.1. Clasificación completa de las reconstrucciones polinómicas

Se puede precisar (27):
\[
\boxed{\{b\in\mathcal D(G):Gb\text{ es polinómico}\}
=\operatorname{span}\{b_d,b_t\}.}
\tag{28a}
\]
Esto no clasifica \(\mathcal D(G)\cap\mathbb C[z]\): un dato polinómico podría tener reconstrucción no polinómica.

Para probar (28a), observemos que (3) implica que \(Kg\) es aditivo, es decir, de la forma \(q(x)+q(y)\). Sea \(g\) un polinomio antisimétrico de grado total máximo \(n\ge3\), con parte homogénea
\[
g_n=\sum_{i=0}^n u_i x^iy^{n-i},\qquad u_{n-i}=-u_i.
\]
El operador \(K\) aumenta el grado a lo sumo en uno. Si \(A_i=(i+1)(i+2)\), los coeficientes mixtos de grado \(i+j+1\) en \(K(x^iy^j)\) son
\[
\alpha_{ij}=-1+\frac{6(2j-i)}{A_iA_j}
\quad\text{en }x^{i+1}y^j\ (j>0),
\]
\[
\beta_{ij}=1+\frac{6(j-2i)}{A_iA_j}
\quad\text{en }x^iy^{j+1}\ (i>0).
\]
Se obtienen integrando monomios en \(L,C,R_+,E\); las contribuciones de grado \(i+j+2\) se cancelan entre los pares reflejados.

Para \(i+j=n\ge3\), todos los \(\alpha_{ij}\) utilizados son negativos y todos los \(\beta_{ij}\) utilizados son positivos. En los índices interiores basta \(A_i,A_j\ge6\). En los extremos, el signo se reduce a
\((n+1)(n+2)-6n=(n-1)(n-2)>0\).

La anulación de los coeficientes mixtos del polinomio aditivo \(Kg\) exige
\[
u_{k-1}\alpha_{k-1,n-k+1}+u_k\beta_{k,n-k}=0,
\qquad k=1,\ldots,n.
\]
Por tanto cada \(u_k\) es un múltiplo real estrictamente positivo de \(u_{k-1}\). Si \(u_0\ne0\), esto contradice \(u_n=-u_0\), también para coeficientes complejos. Si \(u_0=0\), todos los coeficientes se anulan. No puede existir tal parte homogénea de grado \(n\ge3\).

Así, \(g\) tiene grado a lo sumo dos y pertenece a
\(\operatorname{span}\{y-x,y^2-x^2\}=\operatorname{span}\{d,g_t\}\).
La inyectividad de la reconstrucción y (26) prueban (28a).

## 8. Modelo lateral: los canales libres se convierten en respuestas forzadas

Hay también un cálculo normal útil para interpretar la reconstrucción. Separamos explícitamente este resultado de la caracterización global (23).

Sea \(\alpha=-1/2+i\tau\) y considérese la extracción formal del término \(x^\alpha\) al aproximarse al lado \(x=0\). La fibra normal del operador \(\mathscr A\) sobre el perfil \(h(y)\) es
\[
\mathscr A_\tau h
=yh-\kappa(\tau)(1-y)Jh,\qquad
\kappa(\tau)=\frac6{3/2+i\tau}.
\tag{29}
\]
Se obtiene usando que la parte \(x^{\alpha+1}\) de \(J(x^\alpha)\) tiene coeficiente \(1/[(\alpha+1)(\alpha+2)]\), y que el término normal de \(\mathcal X\) es \(-(1-y)\partial_x\).

Como \(Lh=(1-y)Jh+m(h)\), \(m(h)=\int(1-y)h(y)\,dy\),
\[
\boxed{\mathscr A_\tau=N(\tau)+\kappa(\tau)\,\mathbf1\,m.}
\tag{30}
\]
Esta es una corrección genuina de rango uno en la fibra tangencial. No es una afirmación de rango finito para el operador global.

El núcleo de \(\mathscr A_\tau\) en \(L^2(0,1)\) es trivial para todo \(\tau\in\mathbb R\). Para demostrarlo, sea \(U=Sh\). La ecuación homogénea equivale a
\[
y^2U''-\kappa U=0,\qquad U(0)=U(1)=0,\qquad U''\in L^2.
\]
Sus exponentes son \(r_\pm=(1\pm\sqrt{1+4\kappa})/2\). Puesto que \(\operatorname{Re}\kappa>0\), \(\operatorname{Re}r_-<0\), y el término \(y^{r_-}\) queda excluido. El otro término, si es admisible, queda eliminado por \(U(1)=0\).

Si el dato de entrada tiene amplitud formal \(b(x)\sim\eta x^\alpha\), la ecuación de reconstrucción de la fibra es
\[
\mathscr A_\tau h=-6\eta.
\tag{31}
\]
Su única solución posible es
\[
\boxed{h(y)=-6\eta\,y^{\beta(\tau)},\qquad
\beta(\tau)=\frac{-3+\sqrt{1+24/(3/2+i\tau)}}2.}
\tag{32}
\]
En efecto, para \(\kappa=(\beta+1)(\beta+2)\),
\[
(1-y)J(y^\beta)=\frac{y^{\beta+1}-1}{\kappa},
\qquad \mathscr A_\tau(y^\beta)=1.
\]
La solución no nula de (31) pertenece a \(L^2_y\) exactamente cuando
\[
\operatorname{Re}\beta(\tau)>-\frac12
\iff
|\tau|<\sqrt{\frac{39}{4}+3\sqrt{13}}.
\tag{33}
\]
Fuera de ese intervalo, no existe respuesta \(L^2_y\) a una amplitud constante no nula en la fibra.

Así, el canal libre del modelo normal de \(K\) pasa a estar fijado por la amplitud del dato en la reconstrucción. La ausencia de núcleo homogéneo de \(\mathscr A_\tau\) no implica invertibilidad acotada de la fibra.

**Límite de esta afirmación.** Los modos \(x^{-1/2+i\tau}\) son modos generalizados críticos, no datos globales \(L^2_x\). No se ha demostrado un teorema de expansión Mellin de \(W_b\), ni que la transformada de un dato global admisible deba tener soporte en el intervalo (33). Tal conclusión requeriría controlar los términos restantes y el encuentro de los bordes. La teoría de [Lesch sobre operadores de Fuchs y singularidades cónicas](https://arxiv.org/abs/dg-ga/9607005) es un marco para investigar ese paso; no se importa aquí ningún teorema suyo sin verificar hipótesis.

## 9. Alcance y comprobaciones reproducibles

El archivo [verify_domain_moments.py](./verify_domain_moments.py) construye (8)-(9), calcula matrices de Gram exactas, verifica su positividad mediante LDL racional y comprueba:

- La identidad de pruebas (10) contra la fórmula directa de \(\mathscr A\).
- Los dos datos admisibles (26)-(27).
- La monotonía de las secciones calculadas.
- Las cotas \(Q_N(b_d)\le1/6\), \(Q_N(b_t)\le1/90\).
- Las primeras matrices comprimidas \(H_N\).

Los resultados exactos están en [verification_domain_moments.json](./verification_domain_moments.json).

Lo demostrado es el cierre de \(G\), su rango cerrado, el criterio necesario y suficiente (23), y una reconstrucción convergente (19) desde momentos cuando el criterio se cumple. El criterio elimina la dependencia de coeficientes desconocidos de una solución global; sustituye esa dificultad por el control explícito de una sucesión universal de matrices.

Sigue pendiente obtener estimaciones uniformes o asintóticas de \(H_N\) que permitan reconocer clases amplias de datos, probar divergencia para candidatos concretos o reducir \(\mathcal D(G)\) a una familia pequeña. No se ha probado que \(\mathcal D(G)\) sea denso, propio, finito-dimensional o igual a \(\operatorname{span}\{b_d,b_t\}\). Tampoco se ha cerrado la unicidad radial.
