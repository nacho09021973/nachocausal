# Energía positiva global y reconstrucción desde un dato escalar

Fecha: 2026-09-06. Espacio: \(H_{\rm alt}\subset L^2(Q)\), \(Q=(0,1)^2\), con medida de Lebesgue.

**Estado del problema.** Esta nota no demuestra que \(\ker K=\operatorname{span}\{g_t\}\), ni construye un segundo elemento exacto. Demuestra una inyectividad global nueva, una reconstrucción variacional única y una reducción exacta con dominio explícito. También demuestra por qué el dato utilizado no puede extenderse por continuidad, ni siquiera por cierre de su grafo, a toda la clase de energía.

Los resultados son:

1. Existe un operador explícito y acotado \(B:H_{\rm alt}\to L^2(0,1)\) tal que \(K-6(B_x+B_y)\) tiene una identidad de energía estrictamente positiva. En particular,
   \[
   Kg=0,\quad Bg=0\quad\Longrightarrow\quad g=0.
   \]
2. Para cada dato \(b\in L^2(0,1)\), un problema auxiliar coercivo tiene una única solución \(W_b\) en un espacio de energía débil.
3. El núcleo original corresponde exactamente a los datos para los que \(g_b=\partial_x^2\partial_y^2(\omega W_b)\) pertenece a \(L^2\) y satisface \(Bg_b=b\).

El punto nuevo no es solamente escribir una ecuación sobre el borde: se resuelve de manera única el problema global con dato prescrito, en una clase débil precisa, y se excluye cualquier modo exacto invisible para ese dato. La clasificación de los datos admisibles sigue abierta.

## 1. Convenciones

Usamos la convención positiva para el operador reflejado:
\[
Lf(x)=\frac1x\int_0^x(x-s)f(s)\,ds,\qquad
Cf(x)=\frac{1-x}{x^2}\int_0^x sf(s)\,ds,
\]
\[
R_+f(x)=\frac1{1-x}\int_x^1(s-x)f(s)\,ds,\qquad
Ef(x)=\frac{x}{(1-x)^2}\int_x^1(1-s)f(s)\,ds.
\]
Entonces
\[
K=M_{y-x}+6(L\otimes C-C\otimes L-R_+\otimes E+E\otimes R_+).
\tag{1}
\]
Estos operadores son acotados en \(L^2\). En particular, \(Kg_t=0\) para
\[
g_t=(y-x)(x+y-1).
\]
El signo de \(R_+\) importa: si se escribe el último par con los signos opuestos, debe emplearse \(R=-R_+\).

## 2. Una primitiva global con valores de borde definidos

Sea \(S\) el inverso de la segunda derivada con condiciones de Dirichlet:
\[
Sf(x)=\int_0^x(x-s)f(s)\,ds-x\int_0^1(1-s)f(s)\,ds.
\tag{2}
\]
Así, \((Sf)''=f\), \(Sf(0)=Sf(1)=0\). Escribimos
\[
a(x)=x(1-x),\qquad Jf=\frac{Sf}{a}.
\]
El núcleo integral de \(J\) es
\[
j_x(s)=
\begin{cases}
-s/x,&s<x,\\
-(1-s)/(1-x),&s>x.
\end{cases}
\tag{3}
\]
Las identidades unidimensionales siguientes son exactas:
\[
Lf=(1-x)Jf+\int_0^1(1-s)f(s)\,ds,\qquad
R_+f=xJf+\int_0^1sf(s)\,ds,
\tag{4}
\]
\[
Cf=(1-x)^2(Jf)'-(1-x)Jf,\qquad
Ef=-x^2(Jf)'-xJf.
\tag{5}
\]
El núcleo (3) muestra que \(J\) es Hilbert–Schmidt. Las identidades (5), usadas respectivamente en \(x\le1/2\) y \(x\ge1/2\), muestran que \(J:L^2\to H^1\) es acotado. Sus valores extremos son
\[
Jf(0)=-\int(1-s)f(s)\,ds,\qquad Jf(1)=-\int sf(s)\,ds.
\]

Para \(g\in H_{\rm alt}\), definimos
\[
w=(S\otimes S)g,\quad W=(J\otimes J)g,\quad
\omega=a(x)a(y),\quad w=\omega W.
\tag{6}
\]
Ambas primitivas son antisimétricas. \(W\) tiene representante continuo en el cuadrado cerrado: basta la continuidad de \(x\mapsto j_x\) en \(L^2\) y (3). Además, \(W\in H^1(0,1)\widehat\otimes H^1(0,1)\).

Sean las dos marginales
\[
m_g(z)=\int_0^1(1-s)g(s,z)\,ds,\qquad
n_g(z)=\int_0^1sg(s,z)\,ds.
\]
El **dato escalar canónico** es
\[
\boxed{b_g=Bg:=Cm_g-En_g\in L^2(0,1).}
\tag{7}
\]
Es un operador acotado sobre el espacio original. No exige trazas de \(g\), ni regularidad de \(g/(y-x)\).

Si \(p=Jm_g=-W(0,\cdot)\), \(q=Jn_g=-W(1,\cdot)\), entonces
\[
b_g(z)=(1-z)\big[(1-z)p(z)\big]'
       +z\big[zq(z)\big]'.
\tag{8}
\]
Por ello tiene una interpretación como combinación de derivadas de las trazas de la primitiva. Las marginales de (7) son la definición primaria, válida en \(L^2\).

## 3. Descomposición exacta de \(K\)

Introduzcamos
\[
d=y-x,\quad m=x+y-1,\quad
\chi=1+m^2-d^2=2[(1-x)(1-y)+xy],
\]
\[
c_x=(1-x)^2(1-y)+x^2y,\qquad
c_y=(1-x)(1-y)^2+xy^2,
\]
\[
\mathcal X=-c_x\partial_x+c_y\partial_y.
\]
Entonces
\[
\boxed{Kg=d\,g+6\mathcal XW+6[b_g(x)+b_g(y)].}
\tag{9}
\]

Para verificarla directamente, sean \(F=(L\otimes L)g\) y \(G=(R_+\otimes R_+)g\). De (4) y la antisimetría resulta
\[
F=(1-x)(1-y)W+(1-y)p(y)-(1-x)p(x),
\]
\[
G=xyW+yq(y)-xq(x).
\]
La parte integral de \(K/6\) es
\[
(1-y)F_y-(1-x)F_x+yG_y-xG_x.
\]
Al expandirla, los términos sin derivadas de \(W\) se cancelan, queda \(\mathcal XW\), y los restantes son (8) en \(x\) e \(y\). Las identidades se prolongan a \(L^2\) mediante (5).

El campo tiene la estructura
\[
\operatorname{div}\mathcal X=0,\qquad
\mathcal Xm=md,\qquad
\mathcal X\chi=-d\chi,\qquad
\mathcal Xd=\frac{\chi+2m^2}{2}.
\]
En particular \(m\chi\) es una integral primera. La identidad que produce el signo positivo es
\[
\boxed{
-\operatorname{div}\left(\frac{\omega}{d}\mathcal X\right)
=\frac{\chi^2+4m^2}{8}
 +\frac{\omega(\chi+2m^2)}{2d^2}.}
\tag{10}
\]
Se puede obtener usando
\[
\omega=\frac{\chi^2-4m^2}{16},\qquad
\mathcal X\omega=-\frac d8(\chi^2+4m^2).
\]

## 4. Identidad positiva en toda la clase \(L^2\)

Definimos
\[
\boxed{
\mathcal E(W)=
\|w_{xy}\|_2^2
+\frac38\int_Q(\chi^2+4m^2)|W|^2
+\frac32\int_Q\omega(\chi+2m^2)\left|\frac Wd\right|^2.}
\tag{11}
\]
Para todo \(g\in H_{\rm alt}\), los tres términos son finitos y
\[
\boxed{
\operatorname{Re}\int_Q Kg\,\frac{\overline w}{d}
=\mathcal E(W)
+12\operatorname{Re}\int_0^1b_g(x)\overline{r_W(x)}\,dx,}
\tag{12}
\]
donde
\[
r_W(x)=\int_0^1\frac{w(x,y)}{y-x}\,dy.
\tag{13}
\]
El cociente de (13) pertenece a \(L^2(Q)\); no se requiere valor principal.

**Demostración para funciones suaves.** Multiplicamos (9) por \(\overline w/d\). La parte \(dg\) da
\[
\operatorname{Re}\int_Qg\,\overline w=\|w_{xy}\|_2^2
\]
por integración por partes y las condiciones de Dirichlet. La parte de transporte da
\[
6\operatorname{Re}\int_Q\frac{\omega}{d}(\mathcal XW)\overline W
=-3\int_Q\operatorname{div}\left(\frac{\omega}{d}\mathcal X\right)|W|^2.
\]
Los términos de los lados exteriores se anulan por \(\omega=0\). Para justificar el corte en la diagonal, \(W=dH\) con \(H\) suave; el flujo sobre \(d=\pm\varepsilon\) es \(O(\varepsilon)\). Aplicar (10) produce los dos términos restantes de (11). Finalmente \(w/d\) es simétrico, lo que convierte la suma de los dos términos de borde en el factor 12 de (12).

**Paso a \(L^2\), sin regularidad supuesta en la diagonal.** El punto delicado es \(W/d\). Para \(0<x<y<1\), una integración de (3) da
\[
\|j_x\|_2^2=\frac13,\qquad
\langle j_x,j_y\rangle=\frac13-\frac{d^2}{6y(1-x)}.
\]
Sobre funciones antisimétricas, el núcleo de \(g\mapsto W(x,y)/d\) es
\[
\frac{j_x\otimes j_y-j_y\otimes j_x}{2d}.
\]
Su norma al cuadrado está acotada por
\[
\frac{1}{2d^2}\left(\frac19-\langle j_x,j_y\rangle^2\right)
\le \frac1{18y(1-x)}.
\tag{14}
\]
La integral de esta cota sobre los dos triángulos es \(\pi^2/54\). Por tanto,
\[
g\longmapsto W/d
\quad\text{es Hilbert–Schmidt de }H_{\rm alt}\text{ a }L^2(Q).
\tag{15}
\]
También \(g\mapsto W\) y \(g\mapsto w_{xy}\) son Hilbert–Schmidt: sus factores unidimensionales son \(J\) y \(\partial S\). Todos los pesos de (11) son acotados. La aproximación por polinomios antisimétricos permite pasar al límite en cada término de (12).

**Consecuencia global.** Para \(Kg=0\),
\[
\mathcal E(W)=-12\operatorname{Re}\langle b_g,r_W\rangle.
\tag{16}
\]
Si también \(b_g=0\), entonces \(w_{xy}=0\). Como \(w\) satisface Dirichlet en ambos factores, \(w=0\), y \(g=w_{xxyy}=0\). Hemos demostrado
\[
\boxed{\ker K\cap\ker B=\{0\}.}
\tag{17}
\]
En particular, dos elementos exactos del núcleo con el mismo \(b_g\) coinciden. Si \(b_g=c\,b_{g_t}\), entonces \(g=c\,g_t\). El dato temporal es explícito:
\[
W_t=\frac{g_t}{24},\qquad
b_{g_t}(z)=-\frac{(2z-1)(3z^2-3z+1)}{24},\qquad
\mathcal E(W_t)=\frac1{30240}.
\tag{18}
\]

Más generalmente, el operador acotado
\[
\mathscr A g=Kg-6[b_g(x)+b_g(y)]
\]
es inyectivo en \(H_{\rm alt}\), pues
\[
\operatorname{Re}\langle\mathscr A g,w/d\rangle=\mathcal E(W)>0
\quad(g\ne0).
\tag{19}
\]

## 5. Por qué esta positividad respeta la ausencia de estabilidad

La aplicación de \(g\) a las tres componentes ponderadas de (11) es compacta, por (15) y sus análogas. En consecuencia
\[
g_n\rightharpoonup0,\quad \sup_n\|g_n\|_2<\infty
\quad\Longrightarrow\quad \mathcal E(W_{g_n})\longrightarrow0.
\tag{20}
\]
La energía no domina la norma original ni siquiera después de eliminar un número finito de modos.

El dato \(B\), en cambio, detecta los canales laterales previamente construidos. Para su parte principal
\[
u_n=a_n\wedge h_\varepsilon,\qquad
h_\varepsilon(y)=y^\beta{\bf1}_{y>\varepsilon},\quad
\beta=(\sqrt{17}-3)/2,
\]
con los dos momentos de \(a_n\) exactamente nulos, se obtiene
\[
Bu_n=-m(h_\varepsilon)\,Ca_n+n(h_\varepsilon)\,Ea_n.
\]
Aquí
\[
m(h_\varepsilon)\longrightarrow
\frac1{(\beta+1)(\beta+2)}=\frac14,\qquad
Ca_n=\frac23a_n+o_{L^2}(1),\qquad Ea_n=o_{L^2}(1).
\]
Por tanto \(Bu_n=-a_n/6+o_{L^2}(1)\). Las correcciones de norma tendente a cero que imponen la condición diagonal y la ortogonalidad temporal tampoco modifican este resultado, porque \(B\) es acotado en \(L^2\). Para la sucesión normalizada anterior,
\[
\|Bv_n\|_2\longrightarrow\frac{\sqrt{2\beta+1}}{6\sqrt2}>0.
\tag{21}
\]
Así, la energía pierde esos canales mientras que el dato de borde los conserva.

## 6. Reconstrucción única para un dato arbitrario en un espacio débil

Sea \(\mathcal H_{\mathcal E}\) la completación de las funciones suaves antisimétricas en el cuadrado cerrado bajo la norma \(\sqrt{\mathcal E}\), siempre con \(w=\omega W\). Es una norma, no solo una seminorma. El primer término controla \(w\) en
\[
H_0^1(0,1)\widehat\otimes H_0^1(0,1)
\]
por Poincaré en cada factor. Los términos ponderados identifican a \(W\) como función localmente \(L^2\) en el interior, con \(w=\omega W\). Toda primitiva de un \(g\in H_{\rm alt}\) pertenece a este espacio por la aproximación usada en (15).

Inicialmente sobre funciones suaves, definimos la forma sesquilineal, lineal en el primer argumento,
\[
\mathfrak a(W,V)=
\int_Qw_{xy}\overline{v_{xy}}
+6\int_Q\frac{\omega}{d}\mathcal XW\,\overline V,
\qquad v=\omega V.
\tag{22}
\]
La identidad (10) demuestra
\[
\operatorname{Re}\mathfrak a(W,W)=\mathcal E(W).
\tag{23}
\]
Para aplicar Lax–Milgram también hay que demostrar continuidad; la identidad diagonal sola no basta.

En efecto,
\[
\frac{\omega}{d}\mathcal XW
=\frac{\mathcal Xw}{d}+\frac{\chi^2+4m^2}{8}W.
\tag{24}
\]
Tenemos \(c_x,c_y\le\chi/2\), \(0<\chi\le2\), y
\[
a(y)\le |d|+\sqrt\omega,\qquad
a(x)\le |d|+\sqrt\omega.
\]
La primera de las últimas desigualdades se sigue de que \(a\) es 1-Lipschitz, considerando separadamente \(a(y)\le a(x)\) y \(a(y)>a(x)\). Por ello
\[
\frac{a(y)c_x}{|d|}
\le\frac\chi2+\frac{\sqrt{2\omega\chi}}{2|d|},
\]
y análogamente con \(x,c_y\). La desigualdad de Hardy aplicada en el factor transversal da
\[
\|w_x/a(y)\|_2\le4\|w_{xy}\|_2,\qquad
\|w_y/a(x)\|_2\le4\|w_{xy}\|_2.
\]
Los factores \(\chi V\), \(\sqrt{\omega\chi}\,V/d\) y
\(\sqrt{\chi^2+4m^2}\,V\) están controlados por \(\sqrt{\mathcal E(V)}\). Cauchy–Schwarz en (24) demuestra
\[
|\mathfrak a(W,V)|\le C\sqrt{\mathcal E(W)\mathcal E(V)}.
\tag{25}
\]
Así, la forma se prolonga continuamente a \(\mathcal H_{\mathcal E}\) y sigue siendo coerciva con constante 1.

Además, \(\omega\le\chi/8\), de donde
\[
\|r_V\|_2^2\le\|v/d\|_2^2
\le\frac18\int_Q\omega\chi|V/d|^2
\le\frac{\mathcal E(V)}{12}.
\tag{26}
\]
Para cada \(b\in L^2(0,1)\), el teorema de Lax–Milgram aplicado a (22) produce un único \(W_b\in\mathcal H_{\mathcal E}\) tal que
\[
\boxed{
\mathfrak a(W_b,V)=-12\langle b,r_V\rangle
\quad\text{para todo }V\in\mathcal H_{\mathcal E}.}
\tag{27}
\]
Y da la estimación
\[
\sqrt{\mathcal E(W_b)}\le\sqrt{12}\|b\|_2.
\tag{28}
\]
Esta es una reconstrucción global efectivamente bien planteada, con dato libre, en la norma débil especificada. La versión estándar del teorema puede consultarse en las [notas de Lax–Milgram de LMU](https://www.math.lmu.de/~michel/lax-milgram.pdf); las verificaciones particulares necesarias son (23), (25) y (26).

La reconstrucción también admite una estimación del residuo. Para cualquier \(g\in H_{\rm alt}\), restar (27) de la identidad variacional de (9) da
\[
\mathfrak a(W_g-W_{Bg},V)=\int_QKg\,\overline{v/d}.
\]
Usando (23) y (26),
\[
\boxed{\|W_g-W_{Bg}\|_{\mathcal E}\le\frac{\|Kg\|_2}{\sqrt{12}}.}
\tag{28a}
\]
En particular, si \(Bg=0\), \(\|W_g\|_{\mathcal E}\le\|Kg\|_2/\sqrt{12}\). Esta es una estabilidad demostrada en la norma débil; no es una estimación coerciva en la norma original.

## 7. Reducción exacta y su dominio obligatorio

Definamos
\[
\mathfrak D=
\left\{b\in L^2(0,1):
g_b:=\partial_x^2\partial_y^2(\omega W_b)\in L^2(Q)\right\}.
\tag{29}
\]
La derivada se toma en distribuciones. Si \(b\in\mathfrak D\), entonces \(g_b\) es antisimétrico y
\[
\omega W_b=(S\otimes S)g_b.
\tag{30}
\]
Para justificar (30), ambos miembros pertenecen al producto tensorial de \(H_0^1\), y satisfacen
\(\int w_{xy}\overline{\phi_{xy}}=\int g_b\overline\phi\)
para pruebas compactas. Estas son densas en dicho espacio; Poincaré y la unicidad del problema de Dirichlet del producto dan la igualdad.

Podemos entonces definir, solamente en este dominio,
\[
\mathfrak F:\mathfrak D\to L^2(0,1),\qquad \mathfrak Fb=Bg_b.
\tag{31}
\]
Hay una biyección lineal exacta
\[
\boxed{
\ker K\ \longleftrightarrow\
\{b\in\mathfrak D:\mathfrak Fb=b\},\qquad g\longmapsto Bg.}
\tag{32}
\]

**Demostración.** Si \(Kg=0\), (9) y la integración por partes dan (27) con \(b=Bg\). La unicidad en (27) identifica \(W=W_b\), de modo que \(b\in\mathfrak D\) y \(\mathfrak Fb=b\).

Recíprocamente, si \(b\in\mathfrak D\) y \(Bg_b=b\), combinamos (27), (30) y (9) para obtener
\[
\int_QKg_b\,\overline{v/d}=0
\]
para todo \(V\) suave antisimétrico. Para cualquier prueba compacta suave simétrica \(\psi\), podemos escoger \(V=d\psi/\omega\); entonces \(v/d=\psi\). Como \(Kg_b\) es simétrico, esto demuestra \(Kg_b=0\) en distribuciones y en \(L^2\). No queda una condición diagonal adicional pendiente.

El objetivo original se convierte, por tanto, en el enunciado preciso
\[
\{b\in\mathfrak D:\mathfrak Fb=b\}
=\operatorname{span}\left\{-\frac{(2z-1)(3z^2-3z+1)}{24}\right\}.
\tag{33}
\]

**No se ha probado** que \(\mathfrak D=L^2\), que \(\mathfrak F\) sea acotado o compacto, ni que (33) sea cierta. Tampoco es lícito identificar una solución variacional de (27) con una solución \(L^2\) del problema original antes de verificar (29) y (31).

## 8. Una dificultad real: el dato no es cerrable en la norma de energía

Hay una obstrucción explícita a eliminar la precaución anterior. Sobre las primitivas físicas, consideremos el operador \(W_g\mapsto Bg\). Es acotado respecto de \(\|g\|_2\), pero **no es cerrable** como operador desde \(\mathcal H_{\mathcal E}\) hacia \(L^2(0,1)\).

Para verlo, elijamos \(0\ne h\in C_c^\infty(0,1)\) con
\(\int h=\int zh(z)\,dz=0\); por ejemplo \(h=\phi''\), con \(\phi\) suave de soporte compacto y no nula. Sea
\[
f_\varepsilon(x)=\varepsilon^{-1}{\bf1}_{(0,\varepsilon)}(x),
\qquad
u_\varepsilon=f_\varepsilon\wedge h.
\]
Como las dos marginales de \(h\) son cero,
\[
Bu_\varepsilon=(1-\varepsilon/2)Ch-(\varepsilon/2)Eh
\longrightarrow Ch\ne0\quad\text{en }L^2.
\tag{34}
\]
Por otro lado, poniendo \(A_\varepsilon=Jf_\varepsilon\), \(H=Jh\),
\[
W_{u_\varepsilon}=A_\varepsilon\wedge H.
\]
Se calcula directamente
\[
A_\varepsilon(x)=-\frac{\varepsilon}{2x}\quad (x>\varepsilon),
\qquad
\|A_\varepsilon\|_2^2=O(\varepsilon),\qquad
\|(\partial S)f_\varepsilon\|_2^2=O(\varepsilon).
\]
Las cancelaciones de \(h\) hacen que \(H\) tenga soporte en un compacto del interior. Donde una variable está próxima a cero y la otra en ese compacto, \(d\) está separado de cero. Donde ambas están lejos de cero, \(A_\varepsilon\) y sus derivadas son \(O(\varepsilon)\), y la antisimetría cancela el cociente en la diagonal. Por tanto
\[
\|W_{u_\varepsilon}/d\|_2^2=O(\varepsilon),\qquad
\mathcal E(W_{u_\varepsilon})=O(\varepsilon)\longrightarrow0.
\tag{35}
\]
Las ecuaciones (34)-(35) prueban la falta de cerrabilidad. Las funciones escalonadas pueden aproximarse en \(L^2\) por funciones suaves para obtener también una sucesión en el dominio suave inicial.

Esto no prueba que el operador de retorno \(\mathfrak F\), restringido por la ecuación (27), sea no cerrable: esa sería una afirmación distinta. Sí prueba que no se puede extender \(B\) al espacio de energía por un argumento abstracto de densidad, y explica por qué (29) no es una formalidad.

## 9. Comprobaciones y alcance

El archivo [verify_global_energy.py](./verify_global_energy.py) verifica con aritmética simbólica exacta:

- La descomposición (9), la divergencia (10) y la identidad (12) en cinco polinomios distintos.
- La identidad polarizada de la forma (22).
- El producto de núcleos usado en (14).
- El modo temporal y los valores exactos de (18).
- Un ejemplo antisimétrico no nulo con las dos marginales cero: la energía es \(23/529200>0\).

Los resultados están en [verification_global_energy.json](./verification_global_energy.json). Estas verificaciones comprueban signos y coeficientes; la extensión a toda la clase \(L^2\) descansa en la demostración analítica de la sección 4.

Los archivos que comienzan por \(\texttt{explore\_}\) son exploraciones, no pruebas. En particular, aproximaciones de Galerkin del problema (27) muestran autovalores del retorno finito próximos a 1 además del temporal. No permiten decidir si existe un segundo punto fijo admisible en (32). Para datos polinómicos fijos también se observa que la energía puede estabilizarse mientras crece la norma \(L^2\) de la reconstrucción diferenciada; esto tampoco es una prueba de divergencia.

El avance probado es la inyectividad del problema global sin el dato escalar, la reconstrucción única con ese dato prescrito y la localización explícita del obstáculo restante en la admisibilidad \(L^2\) y el retorno (31). La unicidad global original permanece abierta.
