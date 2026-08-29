# `DOMAIN_BRIDGE` para la caja EF fija — obstrucción QMD del experimento puntual

```text
ESTADO: PROVED
FECHA: 2026-08-28
GOBERNANZA: docs/program_domain_bridge_authorization_2026-08-28.md
ENTRADA: docs/physical_reentry_audit_001_2026-08-28.md §12
NATURALEZA: prueba analítica; cero simulación, cero semillas
```

## 1. Enunciado y techo

Fijemos

\[
B=[0,T]\times[r_a,r_b],\qquad 0<r_a<r_b,
\]

y un intervalo compacto de parámetros \(K\Subset(0,\infty)\). En coordenadas
EF ingoing la medida puntual normalizada es uniforme en \(B\). En coordenadas
nulas globales

\[
v=v,\qquad
u_\tau(v,r)=-e^{-v/(2\tau)}W_\tau(r),\qquad
W_\tau(r)=e^{r/\tau}(r/\tau-1),
\]

el orden es el orden producto y la ley tiene soporte móvil \(S_\tau\).

**Teorema (obstrucción de dominio).** Para cada
\(\tau\in\operatorname{int}K\),

\[
H^2(p_\tau,p_{\tau+\delta})\ge c_\tau|\delta|
\]

para \(|\delta|\) suficientemente pequeño y alguna \(c_\tau>0\). Por tanto la
familia puntual \(\{p_\tau\}\) no es QMD. No existe un isomorfismo estadístico
común, independiente de \(\tau\), que la transforme en una familia QMD de
soporte fijo. En particular, el transporte de coordenadas requerido en la
auditoría física §12 no existe dentro de esa clase natural.

El teorema no afirma que la ley finita de `Pi_n` o `[P_{Pi_n}]` sea no-QMD:
un canal puede regularizar una familia no regular. Tampoco identifica Fisher
con el localizador `O=|future|`.

## 2. Densidad y cotas uniformes locales

Como

\[
\partial_r W_\tau(r)=\frac{r}{\tau^2}e^{r/\tau}>0,
\]

el mapa \(r\mapsto u_\tau(v,r)\) es estrictamente decreciente. Es un
difeomorfismo sobre cada fibra y

\[
S_\tau=\left\{(u,v):0\le v\le T,\quad
-e^{-v/(2\tau)}W_\tau(r_b)\le u\le
-e^{-v/(2\tau)}W_\tau(r_a)\right\}.
\]

El cambio de variables desde la densidad \(1/[T(r_b-r_a)]\) da

\[
p_\tau(u,v)=
\frac{\tau^2 e^{v/(2\tau)-r/\tau}}
     {T(r_b-r_a)r},
\qquad r=r_\tau(u,v),
\]

en \(S_\tau\), y cero fuera. En cualquier vecindad compacta de un
\(\tau\in\operatorname{int}K\), continuidad y \(r\in[r_a,r_b]\) proporcionan
constantes \(0<m\le p_\sigma\le M<\infty\), uniformes en \(\sigma\).

## 3. Velocidad de los bordes

Para un borde generado por \(r=r_j\), \(j\in\{a,b\}\), escribamos

\[
b_{j,\tau}(v)=-e^{(r_j-v/2)/\tau}(r_j/\tau-1).
\]

La derivación directa da

\[
\partial_\tau b_{j,\tau}(v)
=\frac{e^{(r_j-v/2)/\tau}}{\tau^2}
\left[(r_j-v/2)(r_j/\tau-1)+r_j\right].
\]

El corchete es afín en \(v\). Si \(r_j\ne\tau\), tiene a lo sumo un cero;
si \(r_j=\tau\), vale \(r_j>0\). Por tanto

\[
A_\tau:=\sum_{j\in\{a,b\}}\int_0^T
|\partial_\tau b_{j,\tau}(v)|\,dv>0.
\]

La diferenciabilidad uniforme de los bordes y el hecho de que la anchura de
cada fibra es positiva implican, para \(\delta\to0\),

\[
|S_\tau\triangle S_{\tau+\delta}|
=A_\tau|\delta|+o(|\delta|).
\]

En particular, existe \(d_\tau>0\) tal que la diferencia simétrica tiene área
al menos \(d_\tau|\delta|\). Al menos una de las dos diferencias orientadas
tiene la mitad de esa área.

## 4. Cota Hellinger y fallo QMD

Con la convención

\[
H^2(p,q)=\int(\sqrt p-\sqrt q)^2,
\]

en \(S_\tau\setminus S_{\tau+\delta}\) el integrando es \(p_\tau\), y en la
diferencia opuesta es \(p_{\tau+\delta}\). La cota inferior uniforme de §2
produce

\[
H^2(p_\tau,p_{\tau+\delta})
\ge m\max\{|S_\tau\setminus S_{\tau+\delta}|,
|S_{\tau+\delta}\setminus S_\tau|\}
\ge \frac{m d_\tau}{2}|\delta|.
\]

Una familia QMD tendría

\[
H^2(p_\tau,p_{\tau+\delta})=O(\delta^2).
\]

La cota lineal lo contradice. Queda probado

```text
MOVING_SUPPORT_QMD_STATUS = PROVED_NON_QMD_FOR_POINT_EXPERIMENT
```

## 5. Invariancia y cierre del candidato de transporte

Sea \(T\) un isomorfismo medible común, independiente de \(\tau\), y sean
\(q_\tau=T_\#p_\tau\). La afinidad de Hellinger, y por tanto \(H^2\), se
preserva exactamente bajo \(T\). Si \(\{q_\tau\}\) fuera QMD, su distancia
Hellinger sería \(O(\delta^2)\), en contradicción con §4. Por consiguiente no
hay un cambio de coordenadas paramétricamente común que convierta el
experimento puntual de la caja EF en el experimento regular de S1/S2.

Un mapa dependiente de \(\tau\) puede fijar el soporte, pero entonces el
canal de orden también depende de \(\tau\); no es el transporte común exigido
por `DOMAIN_BRIDGE`.

## 6. Lema de soporte cuantitativo completo para el canal de rangos

Para \(n\ge1\), sean \(X_i=(U_i,V_i)\), \(1\le i\le n\), puntos iid con
densidad \(p_\tau\). Fuera del conjunto nulo de empates, definimos \(\Pi_n\) con la
convención ya usada en el programa: se ordenan los puntos por `U`, y
`Pi_n(i)=j` si el punto de rango `i` en `U` tiene rango `j` en `V`. Para
\(\sigma\in\mathfrak S_n\), escribimos

\[
\pi_\sigma(\tau):=\mathbb P_\tau(\Pi_n=\sigma).
\]

**Lema (`QUANTITATIVE_FULL_SUPPORT_LEMMA`).** Para todo \(\tau_0>0\) existen
\(\varepsilon>0\), un rectángulo abierto no vacío
\(R=I_u\times I_v\) y \(m>0\), dependientes de \(\tau_0\) pero no de
\(n\), tales que, para todo \(\tau>0\) con
\(|\tau-\tau_0|<\varepsilon\), se cumple

\[
R\Subset\operatorname{int}S_\tau,
\qquad
p_\tau(u,v)\ge m\quad ((u,v)\in R).
\tag{6.1}
\]

En consecuencia, para todo \(n\ge1\), simultáneamente para todo
\(\sigma\in\mathfrak S_n\) y todo \(\tau\) del mismo entorno,

\[
\boxed{
\pi_\sigma(\tau)\ge \frac{(m|R|)^n}{n!}>0.
}
\tag{6.2}
\]

En particular,

\[
\boxed{
\operatorname{supp}\mathcal L_\tau(\Pi_n)=\mathfrak S_n.
}
\tag{6.3}
\]

### 6.1. Prueba geométrica

Las fórmulas demostradas en §2 son

\[
b_{j,\tau}(v)
=-e^{(r_j-v/2)/\tau}(r_j/\tau-1),\qquad j\in\{a,b\},
\tag{6.4}
\]

y

\[
S_\tau=\{(u,v):0\le v\le T,\quad
b_{b,\tau}(v)\le u\le b_{a,\tau}(v)\}.
\tag{6.5}
\]

En efecto, `b_{j,tau}(v)=u_tau(v,r_j)`. Como

\[
\partial_r u_\tau(v,r)
=-e^{-v/(2\tau)}\frac{r}{\tau^2}e^{r/\tau}<0
\qquad (r>0),
\tag{6.6}
\]

para cada `v` se tiene

\[
b_{b,\tau}(v)<b_{a,\tau}(v).
\tag{6.7}
\]

Fijemos cualquier \(v_0\in(0,T)\) y pongamos

\[
u_0=\frac{b_{a,\tau_0}(v_0)+b_{b,\tau_0}(v_0)}2.
\]

La desigualdad (6.7) muestra que \((u_0,v_0)\) es interior a
\(S_{\tau_0}\). Las funciones de borde (6.4) son suaves en \((\tau,v)\)
sobre \((0,\infty)\times[0,T]\). Por continuidad conjunta, existen
intervalos abiertos no vacíos \(I_u\) alrededor de \(u_0\) e \(I_v\)
alrededor de \(v_0\), con \(\overline I_v\subset(0,T)\), y
\(\varepsilon>0\), que podemos reducir para que
\(\tau_0-\varepsilon>0\), tales que

\[
b_{b,\tau}(v)<\inf I_u\le \sup I_u<b_{a,\tau}(v)
\tag{6.8}
\]

para \(|\tau-\tau_0|\le\varepsilon\) y \(v\in\overline I_v\). Los intervalos se
escogen con cierre compacto y con margen estricto; reduciendo de nuevo
`epsilon` si es preciso, ese margen persiste en todo el producto compacto.
Así, para el rectángulo **fijo** \(R=I_u\times I_v\), (6.8) da

\[
\overline R\subset\operatorname{int}S_\tau
\]

para todos esos \(\tau\), y la inclusión es compacta. El argumento no cambia
si \(\tau_0=r_a\) o \(\tau_0=r_b\): en esos valores uno de los bordes puede
pasar por \(u=0\), pero (6.6)--(6.7) conservan la anchura estrictamente positiva.

En el abierto interior de los soportes, la inversa `r=r_tau(u,v)` es suave
por (6.6). Por tanto la fórmula de §2,

\[
p_\tau(u,v)=
\frac{\tau^2 e^{v/(2\tau)-r_\tau(u,v)/\tau}}
     {T(r_b-r_a)r_\tau(u,v)},
\tag{6.9}
\]

es continua y estrictamente positiva en

\[
[\tau_0-\varepsilon,\tau_0+\varepsilon]\times\overline R.
\]

Este conjunto es compacto. El mínimo de (6.9) sobre él es, pues, una
constante \(m>0\). Tras restringir a
\(|\tau-\tau_0|<\varepsilon\), queda probada (6.1). La construcción de
\(\varepsilon\), \(R\) y \(m\) precede a la elección de \(n\); las tres
cantidades son independientes del tamaño de muestra.

El rectángulo obtenido es fijo sólo localmente en `tau`. No se afirma que
un único rectángulo esté contenido en todos los soportes al recorrer un
compacto de parámetros: la intersección global de esos soportes puede ser
vacía.

### 6.2. Prueba del volumen de las cámaras de rangos

Sea \(A_\sigma\subset R^n\) el conjunto de configuraciones etiquetadas cuyos
\(n\) puntos están **todos** en \(R\) y cuya permutación **global** de rangos
es \(\sigma\). La palabra global es esencial: estos son todos los puntos de la
muestra completa, de modo que los rangos calculados entre los puntos de
`R` son los rangos de la muestra, sin puntos exteriores que los alteren.

Los conjuntos donde `u_i=u_j` o `v_i=v_j` para algún `i!=j` son uniones
finitas de hiperplanos y tienen medida de Lebesgue cero. En su complemento,
cada configuración tiene un único orden absoluto de las etiquetas por `u`
y un único orden absoluto por `v`. Hay `(n!)^2` pares de órdenes absolutos.
Cada celda correspondiente tiene volumen

\[
\frac{|I_u|^n}{n!}\frac{|I_v|^n}{n!}
=\frac{|R|^n}{(n!)^2}.
\tag{6.10}
\]

la igualdad se obtiene permutando las etiquetas en cada factor
`I_u^n` e `I_v^n`; las `n!` celdas de cada factor son congruentes y lo
particionan módulo empates.

Fijado un orden absoluto de las etiquetas por `u`, la convención de
`Pi_n` determina de manera única el orden absoluto por `v` que produce
`sigma`. Por tanto exactamente `n!` de las `(n!)^2` celdas producen cada
`sigma`: una por cada orden absoluto en `u`. En consecuencia,

\[
|A_\sigma|=n!\frac{|R|^n}{(n!)^2}
=\frac{|R|^n}{n!}.
\tag{6.11}
\]

Por independencia y por (6.1), para todo `tau` del entorno local,

\[
\begin{aligned}
\pi_\sigma(\tau)
&\ge \int_{A_\sigma}\prod_{i=1}^n
 p_\tau(u_i,v_i)\,du_1\,dv_1\cdots du_n\,dv_n\\
&\ge m^n|A_\sigma|
=\frac{(m|R|)^n}{n!}.
\end{aligned}
\tag{6.12}
\]

Esto prueba (6.2). Puesto que `S_n` es finito y cada uno de sus elementos
tiene probabilidad positiva, (6.3) es inmediato.

## 7. Corolario uniforme sobre compactos a tamaño fijo

Sea \(K\Subset(0,\infty)\) compacto y admisible. Los entornos locales
del lema cubren \(K\); extraigamos una subcubierta finita
\(U_1,\ldots,U_k\). Para cada \(i\), la construcción da \(R_i\), \(m_i\)
y, a \(n\) fijo,

\[
c_i(n):=\frac{(m_i|R_i|)^n}{n!}>0.
\]

Si `tau in K`, pertenece a algún `U_i`, y la cota local correspondiente
vale simultáneamente para todo `sigma in S_n`. Por ello

\[
\boxed{
\inf_{\tau\in K}\min_{\sigma\in\mathfrak S_n}
\pi_\sigma(\tau)
\ge \min_{1\le i\le k}c_i(n)>0.
}
\tag{7.1}
\]

Este corolario es para cada `n` fijo. Las constantes pueden degenerar
rápidamente con `n`; no se afirma control asintótico alguno:

```text
NO_UNIFORM_IN_N_CLAIM
```

## 8. Corolario para el canal de posets

El push-forward de una medida de soporte total en `S_n` por

\[
\sigma\longmapsto[P_\sigma]
\]

tiene soporte exactamente igual a la imagen de ese mapa: cada fibra no
vacía es finita y contiene al menos una permutación de probabilidad positiva.
Esto no afirma que la imagen contenga todos los posets de `n` elementos,
sino sólo los realizables por el canal correspondiente.

Para la interpretación geométrica directa, un rectángulo doble-nulo es
causalmente convexo. Si `p prec q` y ambos pertenecen a `R`, entonces

\[
J^+(p)\cap J^-(q)
\subseteq [u_p,u_q]\times[v_p,v_q]
\subseteq R.
\tag{8.1}
\]

Por tanto el orden causal inducido sobre las configuraciones de `R` coincide
con la restricción del orden causal ambiente. Esta observación sólo hace
hermética la interpretación del mismo corolario; no abre un segundo gate.

## 9. Techo del lema de soporte por sí solo

La cota (6.2) elimina ceros en los denominadores del Fisher formal

\[
I_n(\tau)=\sum_\sigma
\frac{\pi_\sigma'(\tau)^2}{\pi_\sigma(\tau)},
\]

pero, por sí sola, no demuestra que las derivadas existan ni controla sus
numeradores o su comportamiento al crecer `n`. En particular, el lema de
soporte no permite concluir que el canal causal regularice la familia
puntual. La diferenciabilidad se trata separadamente en §§10--11.

```text
QUANTITATIVE_FULL_SUPPORT_LEMMA = PROVED
FINITE_CHANNEL_SUPPORT = FULL_FOR_PERMUTATION_CHANNEL
SUPPORT_LEMMA_ALONE_DOES_NOT_PROVE_DIFFERENTIABILITY
SUPPORT_LEMMA_ALONE_DOES_NOT_PROVE_QMD
NO_UNIFORM_IN_N_CLAIM
```

Estas son limitaciones lógicas del lema de soporte, no el estado final del
documento después de §§10--11.

## 10. Lema de volumen para cámaras paramétricas

Usaremos la siguiente forma elemental del cálculo de dominios móviles. Se
incluye la prueba para no ocultar en una cita las esquinas de la caja.

**Lema de cámaras.** Sea \(D\subset\mathbb R^d\) una caja compacta, sea
\(J\) un intervalo abierto y sean \(g_1,\ldots,g_q\) funciones \(C^2\) en
un entorno de \(J\times D\). Sea \(C\subset D\) una cámara fija definida
por un número finito de desigualdades lineales estrictas. Supongamos,
localmente uniformemente en \(t\in J\), que:

1. \(d_xg_j(t,x)\ne0\) cuando \(g_j(t,x)=0\);
2. la intersección de dos caras móviles distintas, la parte no transversal
   de la intersección de una cara móvil con una cara fija de codimensión uno,
   y la intersección con una arista fija de codimensión al menos dos están
   contenidas en una unión finita de subvariedades \(C^1\) de codimensión al
   menos dos, con cartas tubulares localmente uniformes en \(t\);
3. fuera de ese conjunto excepcional, cada cara móvil corta
   transversalmente las caras fijas de codimensión uno.

Entonces

\[
V(t):=\operatorname{Leb}\{x\in C:g_1(t,x)>0,\ldots,g_q(t,x)>0\}
\tag{10.1}
\]

es \(C^1\) en \(J\).

**Prueba.** Fijemos un compacto \(J_0\Subset J\). En la parte de
\(\{g_j=0\}\) que queda fuera de las intersecciones de codimensión dos, el
teorema de la función implícita proporciona un número finito de cartas,
uniformes para \(t\in J_0\), en las que la última coordenada es
\(z=g_j(t,x)\). Una partición de la unidad reduce allí (10.1) a integrales
con un extremo \(z=0\) y con integrando y jacobiano \(C^1\). El teorema
fundamental del cálculo y la derivación bajo la integral dan una derivada
continua; las caras fijas no producen velocidad normal.

Queda justificar que los cruces excluidos de esas cartas no esconden un
término de primer orden. Por las hipótesis 2--3 y la compacidad, admiten
finitas cartas tubulares con al menos dos coordenadas normales. En un tubo
de radio \(\rho\), la parte barrida al cambiar \(t\) en \(h\) tiene volumen

\[
O(|h|\rho+h^2),
\tag{10.2}
\]

uniformemente en \(t\in J_0\): una coordenada normal recorre
\(O(|h|)\), mientras la segunda tiene longitud \(O(\rho+|h|)\). Dividiendo
por \(|h|\), haciendo primero \(h\to0\) y después \(\rho\to0\), la
contribución de esos tubos desaparece. Las expresiones locales de las caras
regulares convergen además uniformemente al variar \(t\), de modo que la
derivada obtenida es continua. Esto prueba el lema. \(\square\)

La misma prueba permite reemplazar las desigualdades lineales que definen
\(C\) por caras fijas \(C^2\) que satisfagan las mismas condiciones de
intersección. Aquí sólo necesitaremos órdenes estrictos de coordenadas y las
caras de la caja.

## 11. Diferenciabilidad de las probabilidades de permutación

**Teorema (`FINITE_CHANNEL_DIFFERENTIABILITY`).** Fijados \(n\ge1\) y
\(\sigma\in\mathfrak S_n\), la función

\[
\tau\longmapsto\pi_\sigma(\tau)
\]

es \(C^1\) en \((0,\infty)\). La afirmación es local en \(\tau\), no
uniforme en \(n\).

Para \(n=1\), \(\pi_{\mathrm{id}}\equiv1\), así que el resultado es
inmediato. En lo que sigue suponemos \(n\ge2\).

### 11.1. Retorno a la caja EF fija

Trabajamos en

\[
B^n=([0,T]\times[r_a,r_b])^n,
\]

donde la densidad conjunta es la constante

\[
c_B^n:=\frac1{[T(r_b-r_a)]^n}
\tag{11.1}
\]

para todo \(\tau\). Así no se deriva una densidad de soporte móvil: toda la
dependencia paramétrica está en

\[
u_i(\tau):=u_\tau(v_i,r_i)
=-e^{-v_i/(2\tau)}W_\tau(r_i).
\tag{11.2}
\]

Los empates en \(u\) o \(v\) tienen medida cero para cada \(\tau\), por el
mismo argumento de difeomorfismo fibroso usado en §§2 y 6.

Para cada orden absoluto \(\alpha\in\mathfrak S_n\) de las etiquetas por
\(u\), escrito de modo que \(\alpha(i)\) es la etiqueta de rango \(i\) en
\(u\), la convención de \(\Pi_n\) determina un único orden absoluto
\(\beta=\beta(\alpha,\sigma)\) por \(v\). Explícitamente, si \(\beta(j)\) es
la etiqueta de rango \(j\) en \(v\), entonces

\[
\beta(j)=\alpha(\sigma^{-1}(j)).
\tag{11.3}
\]

Por tanto, módulo empates, \(\{\Pi_n=\sigma\}\) es la unión disjunta de las
\(n!\) cámaras

\[
\begin{split}
C_{\alpha,\sigma}(\tau)=\{(v_i,r_i)_{i=1}^n\in B^n:\;&
u_{\alpha(1)}(\tau)<\cdots<u_{\alpha(n)}(\tau),\\
&v_{\beta(1)}<\cdots<v_{\beta(n)}\}.
\end{split}
\tag{11.4}
\]

En consecuencia,

\[
\pi_\sigma(\tau)
=c_B^n\sum_{\alpha\in\mathfrak S_n}
\operatorname{Leb}C_{\alpha,\sigma}(\tau).
\tag{11.5}
\]

La suma es finita. Basta probar que cada sumando es \(C^1\).

### 11.2. Verificación de las hipótesis del lema de cámaras

Fijemos \(\tau_0>0\) y un intervalo compacto
\(J_0\Subset(0,\infty)\) que lo contenga en su interior. Las caras móviles
de (11.4) están dadas por las \(n-1\) funciones

\[
g_k(\tau,x)
:=u_{\alpha(k+1)}(\tau)-u_{\alpha(k)}(\tau),
\qquad 1\le k<n.
\tag{11.6}
\]

Son suaves en un entorno de \(J_0\times B^n\). Además, por (6.6), existen
constantes \(0<c<C<\infty\), dependientes de \(J_0\) y de la caja pero no
de \(x\), tales que

\[
c\le |\partial_r u_\tau(v,r)|\le C
\qquad
((\tau,v,r)\in J_0\times B).
\tag{11.7}
\]

En particular, sobre \(g_k=0\), las componentes de \(d_xg_k\) en
\(r_{\alpha(k)}\) y \(r_{\alpha(k+1)}\) son no nulas. Cada cara móvil es,
por tanto, un nivel regular, uniformemente en \(J_0\).

Si se anulan dos \(g_k\) distintos, aparecen dos igualdades independientes
entre coordenadas \(u_i\). Si las parejas de índices son disjuntas, la
independencia de sus diferenciales es inmediata. Si comparten un índice,
las filas correspondientes son dos filas independientes de la matriz de
incidencia de un camino, multiplicadas por los factores no nulos
\(\partial_{r_i}u_i\). La intersección tiene codimensión dos. El mismo
argumento da codimensión \(s-1\) para un empate de \(s\) coordenadas.

Las caras fijas \(v_i=v_j\) son transversales a una cara \(g_k=0\), porque
el diferencial de esta última tiene componentes radiales no nulas. En una
cara radial de \(B^n\), una igualdad \(g_k=0\) sigue siendo regular en la
dirección radial del otro punto. La única excepción posible exige que las
dos coordenadas radiales involucradas estén simultáneamente en caras de la
caja; eso ya es una esquina de codimensión dos. Lo mismo ocurre en particular
cuando \(\tau_0=r_a\) o \(\tau_0=r_b\): aunque \(u=0\) para todo \(v\) en
esa esquina radial, se han fijado dos coordenadas radiales, de modo que el
estrato excepcional sigue teniendo codimensión dos y queda cubierto por
(10.2). Las caras \(v_i=0,T\) tampoco contienen una cara móvil, nuevamente
por las derivadas radiales no nulas.

Se verifican así las tres hipótesis del lema de cámaras para cada
\(C_{\alpha,\sigma}(\tau)\). Su volumen es \(C^1\) en un entorno de
\(\tau_0\). Como \(\tau_0\) era arbitrario y (11.5) es una suma finita,
\(\pi_\sigma\in C^1((0,\infty))\). \(\square\)

### 11.3. Techo del gate de diferenciabilidad por sí solo

La prueba es para cada \(n\) fijo. No proporciona cotas uniformes en \(n\)
para \(\pi_\sigma'\), no intercambia derivación con \(n\to\infty\) y no
calcula por sí sola información Fisher. En particular, el teorema \(C^1\)
aislado no es todavía la verificación escrita de QMD ni abre el puente hacia
localización. El ensamblaje separado se lleva a cabo en §§12--13.

```text
QUANTITATIVE_FULL_SUPPORT_LEMMA = PROVED
FINITE_CHANNEL_SUPPORT = FULL_FOR_PERMUTATION_CHANNEL
FINITE_CHANNEL_DIFFERENTIABILITY = PROVED_C1_LOCAL
C1_GATE_ALONE_DOES_NOT_CONSTITUTE_QMD_PROOF
NO_UNIFORM_IN_N_CLAIM
```

## 12. Ensamblaje QMD en el alfabeto finito

**Teorema (`FINITE_CHANNEL_QMD`).** Para cada \(n\ge1\) fijo, la familia
de leyes

\[
\mathcal E_n^\Pi
=\{\mathcal L_\tau(\Pi_n):\tau>0\}
\]

sobre \(\mathfrak S_n\) es QMD en cada \(\tau>0\). Su score y su
información Fisher son

\[
\dot\ell_{\tau,n}(\sigma)
=\frac{\pi_\sigma'(\tau)}{\pi_\sigma(\tau)},
\qquad
I_n^\Pi(\tau)
=\sum_{\sigma\in\mathfrak S_n}
\frac{\pi_\sigma'(\tau)^2}{\pi_\sigma(\tau)}<\infty.
\tag{12.1}
\]

**Prueba.** Fijemos \(n\) y \(\tau\). Por el lema de soporte cuantitativo,
\(\pi_\sigma(\tau)>0\) para toda \(\sigma\), y por el teorema de §11 cada
\(\pi_\sigma\) es \(C^1\). La regla de la cadena da, para cada \(\sigma\),

\[
\sqrt{\pi_\sigma(\tau+\delta)}
=\sqrt{\pi_\sigma(\tau)}
+\frac{\pi_\sigma'(\tau)}{2\sqrt{\pi_\sigma(\tau)}}\,\delta
+o_\sigma(\delta).
\tag{12.2}
\]

Como \(\mathfrak S_n\) es finito, el máximo de los restos
\(|o_\sigma(\delta)|/|\delta|\) tiende a cero. Por tanto

\[
\sum_{\sigma\in\mathfrak S_n}
\left[
\sqrt{\pi_\sigma(\tau+\delta)}-
\sqrt{\pi_\sigma(\tau)}-
\frac12\dot\ell_{\tau,n}(\sigma)
\sqrt{\pi_\sigma(\tau)}\,\delta
\right]^2
=o(\delta^2).
\tag{12.3}
\]

Esta es exactamente la definición de QMD respecto de la medida de conteo
en el alfabeto finito. Además, derivando
\(\sum_\sigma\pi_\sigma(\tau)=1\),

\[
\sum_\sigma\pi_\sigma(\tau)\dot\ell_{\tau,n}(\sigma)
=\sum_\sigma\pi_\sigma'(\tau)=0,
\tag{12.4}
\]

y (12.1) es la norma cuadrática del score. Es finita porque la suma es
finita y todos sus denominadores son positivos. \(\square\)

### 12.1. Expansiones locales Hellinger y KL

Con la convención de §4, (12.2) implica directamente

\[
\boxed{
H^2\!\left(\pi_\tau^{(n)},\pi_{\tau+\delta}^{(n)}\right)
=\frac14 I_n^\Pi(\tau)\delta^2+o(\delta^2).
}
\tag{12.5}
\]

Para KL no hace falta suponer \(C^2\). Escribamos

\[
\Delta_\sigma(\delta)
:=\pi_\sigma(\tau+\delta)-\pi_\sigma(\tau)
=\pi_\sigma'(\tau)\delta+o_\sigma(\delta).
\tag{12.6}
\]

La positividad sobre el alfabeto finito permite usar uniformemente
\(-\log(1+x)=-x+x^2/2+o(x^2)\), con
\(x=\Delta_\sigma/\pi_\sigma(\tau)\). Como
\(\sum_\sigma\Delta_\sigma(\delta)=0\) exactamente, el término lineal se
cancela y resulta

\[
\boxed{
D_{\mathrm{KL}}\!\left(
\pi_\tau^{(n)}\middle\|\pi_{\tau+\delta}^{(n)}
\right)
=\frac12 I_n^\Pi(\tau)\delta^2+o(\delta^2).
}
\tag{12.7}
\]

Así, a cardinalidad fija, la ley puntual no-QMD de §§3--4 y su imagen
finita tienen comportamientos locales distintos:

\[
H^2(p_\tau,p_{\tau+\delta})\gtrsim|\delta|,
\qquad
H^2(\pi_\tau^{(n)},\pi_{\tau+\delta}^{(n)})
=\frac14I_n^\Pi(\tau)\delta^2+o(\delta^2).
\tag{12.8}
\]

La comparación (12.8) es exclusivamente para cada \(n<\infty\). No se le
atribuye contenido uniforme o asintótico.

## 13. Push-forward al canal de posets y techo

Sea \(\mathcal Y_n\) la imagen finita del mapa
\(\sigma\mapsto[P_\sigma]\), y sea

\[
q_y(\tau):=\mathbb P_\tau([P_{\Pi_n}]=y)
=\sum_{\sigma:[P_\sigma]=y}\pi_\sigma(\tau).
\tag{13.1}
\]

Cada \(q_y\) es \(C^1\), por ser una suma finita, y es estrictamente
positiva para \(y\in\mathcal Y_n\), por el corolario de §8. Aplicando el
mismo argumento de §12 sobre \(\mathcal Y_n\), la familia de clases de
posets también es QMD para cada \(n\) fijo, con

\[
\dot\ell_{\tau,n}^{[P]}(y)=\frac{q_y'(\tau)}{q_y(\tau)},
\qquad
I_n^{[P]}(\tau)=\sum_{y\in\mathcal Y_n}
\frac{q_y'(\tau)^2}{q_y(\tau)}<\infty.
\tag{13.2}
\]

Esto no afirma que \(\mathcal Y_n\) contenga todos los posets de \(n\)
elementos.

Nada de lo anterior controla \(I_n^\Pi(\tau)\) o \(I_n^{[P]}(\tau)\) al
crecer \(n\). En particular, no se afirma que sean acotadas, sublineales o
lineales, ni se excluye que diverjan. Tampoco se ensambla aquí la mezcla
Poisson no condicionada. No se adopta ninguna formulación global según la
cual el canal causal regularice la familia.

```text
QUANTITATIVE_FULL_SUPPORT_LEMMA = PROVED
FINITE_CHANNEL_SUPPORT = FULL_FOR_PERMUTATION_CHANNEL
FINITE_CHANNEL_DIFFERENTIABILITY = PROVED_C1_LOCAL
FINITE_CHANNEL_QMD = PROVED_FOR_EACH_FIXED_N
FINITE_POSET_CHANNEL_QMD = PROVED_ON_CHANNEL_IMAGE_FOR_EACH_FIXED_N
UNIFORM_IN_N_REGULARITY = OPEN
POISSON_MIXTURE_REGULARITY = OPEN
DOMAIN_BRIDGE = CLOSED_FOR_EACH_FIXED_N_CHANNEL
DOMAIN_BRIDGE_BEYOND_FIXED_N = OPEN
FISHER_TO_LOCALISATION_BRIDGE = NOT_OPENED
NEXT_RUN_AUTHORIZED = NO
```

## 14. Veredicto y siguiente frontera

```text
COMMON_POINT_ISOMORPHISM = REFUTED
MOVING_SUPPORT_QMD_STATUS = PROVED_NON_QMD_FOR_POINT_EXPERIMENT
FINITE_CHANNEL_DIFFERENTIABILITY = PROVED_C1_LOCAL
FINITE_CHANNEL_QMD = PROVED_FOR_EACH_FIXED_N
FINITE_POSET_CHANNEL_QMD = PROVED_ON_CHANNEL_IMAGE_FOR_EACH_FIXED_N
UNIFORM_IN_N_REGULARITY = OPEN
POISSON_MIXTURE_REGULARITY = OPEN
DOMAIN_BRIDGE = CLOSED_FOR_EACH_FIXED_N_CHANNEL
DOMAIN_BRIDGE_BEYOND_FIXED_N = OPEN
FISHER_TO_LOCALISATION_BRIDGE = NOT_OPENED
NEXT_RUN_AUTHORIZED = NO
```

El esqueleto finito `Pi_n -> [P_{Pi_n}]` continúa siendo exacto y ahora se ha
probado que, a cada cardinalidad finita, su canal de permutaciones tiene
soporte total y es QMD, y que el push-forward a la imagen del canal de posets
también es QMD. Permanecen abiertas la mezcla Poisson y cualquier regularidad
uniforme al crecer \(n\). Ninguno de estos resultados abre el puente entre
Fisher y localización.

## 15. `UNIFORM_IN_N_PREFLIGHT`

```text
NATURALEZA = EXPLORATORY_ANALYTIC_PREFLIGHT
UNIFORM_IN_N_PREFLIGHT = PASS_ANALYTIC_ROUTE_IDENTIFIED
BEST_ROUTE = U3_CELL_BOUNDARY_DIFFERENTIATION
NO_UNIFORM_IN_N_THEOREM
NO_POISSON_MIXTURE_PROOF
NO_FISHER_TO_LOCALISATION
NEXT_RUN_AUTHORIZED = NO
```

### 15.1. Pregunta y punto de partida

Las identidades disponibles son (11.5), para las probabilidades,

\[
\pi_\sigma(\tau)
=c_B^n\sum_{\alpha\in\mathfrak S_n}
\operatorname{Leb}C_{\alpha,\sigma}(\tau),
\qquad
c_B=[T(r_b-r_a)]^{-1},
\tag{15.1}
\]

y (12.1), para el Fisher fixed-\(n\),

\[
I_n^\Pi(\tau)=\sum_\sigma
\frac{\pi_\sigma'(\tau)^2}{\pi_\sigma(\tau)}.
\tag{15.2}
\]

El preflight pregunta qué control cuantitativo adicional permitiría comparar
estas cantidades entre distintos \(n\), sin afirmar todavía uniformidad QMD
ni una escala asintótica.

### 15.2. Ruta U2: por qué el complete-data Fisher no da la cota

En la caja EF fija, la variable latente

\[
X_n=((V_i,R_i))_{i=1}^n\in B^n
\]

tiene densidad uniforme \(c_B^n\), independiente de \(\tau\). Su score
ordinario sería cero. Sin embargo, el mapa

\[
X_n\longmapsto\Pi_n
\]

ordena las coordenadas \(u_\tau(V_i,R_i)\) y, por tanto, depende de
\(\tau\). No es un kernel de Markov común e independiente del parámetro.
La desigualdad de procesamiento de Fisher no es aplicable a esta
factorización: aplicarla formalmente produciría la contradicción
\(I_n^\Pi\le0\).

En coordenadas nulas \((u,v)\), el mapa de rangos sí es fijo, pero la ley
complete-data es precisamente la familia \(p_\tau^{\otimes n}\) de soporte
móvil que no es QMD (§4). No posee un score \(L^2\) ordinario cuyo Fisher
finito pueda dominar al del canal. Por tanto U2 no suministra una cota
complete-data regular.

La segunda flecha

\[
\Pi_n\longmapsto[P_{\Pi_n}]
\]

sí es un canal fijo. En este tramo data processing es legítimo y da

\[
\boxed{I_n^{[P]}(\tau)\le I_n^\Pi(\tau).}
\tag{15.3}
\]

En efecto, si \(F_y=\{\sigma:[P_\sigma]=y\}\), entonces
\(q_y'=\sum_{\sigma\in F_y}\pi_\sigma'\), y Cauchy--Schwarz da

\[
\frac{q_y'^2}{q_y}
\le\sum_{\sigma\in F_y}\frac{\pi_\sigma'^2}{\pi_\sigma};
\]

sumando sobre las fibras se obtiene (15.3).

### 15.3. Rutas U1/U3: representación exacta por flujo de caras

Fijemos un compacto \(K\Subset(0,\infty)\), escribamos
\(d_r=r_b-r_a\), y definamos las constantes finitas y positivas

\[
A_K:=\sup_{\tau\in K,(v,r)\in B}|\partial_\tau u_\tau(v,r)|,
\qquad
c_K:=\inf_{\tau\in K,(v,r)\in B}|\partial_r u_\tau(v,r)|,
\qquad
\kappa_K:=\frac{2A_K}{c_Kd_r}.
\tag{15.4}
\]

Para la cámara (11.4), sea

\[
g_{\alpha,k}(\tau,x)
=u_{\alpha(k+1)}(\tau)-u_{\alpha(k)}(\tau).
\]

La prueba de §§10--11, escrita en forma de coárea, proporciona la
representación exacta

\[
\begin{aligned}
\pi_\sigma'(\tau)
=c_B^n\sum_{\alpha\in\mathfrak S_n}\sum_{k=1}^{n-1}
\int_{B^n}&
\mathbf 1_{\{v_{\beta(1)}<\cdots<v_{\beta(n)}\}}
\prod_{\ell\ne k}\mathbf 1_{\{g_{\alpha,\ell}>0\}}\\
&\times\delta_0(g_{\alpha,k})
\,\partial_\tau g_{\alpha,k}\,dx .
\end{aligned}
\tag{15.5}
\]

Aquí \(\delta_0(g)\,dx\) significa la medida de coárea
\(d\mathcal H^{2n-1}/|\nabla_xg|\) sobre \(g=0\); los cruces de caras
tienen codimensión al menos dos y no añaden términos. Esta fórmula no
supone simetría de las \(\pi_\sigma\).

Para acotar una integral de (15.5), integramos la delta en la variable
\(r_{\alpha(k+1)}\). Por (15.4), el cociente jacobiano satisface

\[
\frac{|\partial_\tau g_{\alpha,k}|}
{|\partial_{r_{\alpha(k+1)}}g_{\alpha,k}|}
\le\frac{2A_K}{c_K}.
\tag{15.6}
\]

Para \(\alpha\) fijo, la cámara de orden en \(v\) tiene volumen
\(T^n/n!\); al sumar sobre \(\alpha\), esas cámaras particionan el conjunto
sin empates. Las restantes \(n-1\) variables radiales tienen volumen
\(d_r^{n-1}\). Después de multiplicar por \(c_B^n\), (15.5)--(15.6) dan
la cota uniforme en \(\sigma\)

\[
\boxed{
\sup_{\tau\in K}|\pi_\sigma'(\tau)|
\le(n-1)\kappa_K.
}
\tag{15.7}
\]

También puede evitarse sumar esta cota sobre las \(n!\) celdas. Toda
variación de una celda se produce a través de una igualdad \(u_i=u_j\).
Hay \(\binom n2\) pares; cada interfaz se cuenta a lo sumo dos veces al
sumar variaciones absolutas de las celdas. Aplicando (15.6) sin restringir
el orden de \(v\),

\[
\boxed{
\sup_{\tau\in K}
\sum_{\sigma\in\mathfrak S_n}|\pi_\sigma'(\tau)|
\le n(n-1)\kappa_K.
}
\tag{15.8}
\]

Las cotas (15.7)--(15.8) son polinómicas para la masa de flujo, pero Fisher
pondera cada derivada por \(1/\pi_\sigma\). Cubramos \(K\) por los finitos
entornos del corolario de §7, con constantes \((m_i,R_i)\), y pongamos

\[
a_K:=\min_i m_i|R_i|>0.
\]

No se usa un rectángulo global: para cada \(\tau\in K\) se aplica uno de
los rectángulos locales de la subcubierta. Entonces

\[
\inf_{\tau\in K}\min_\sigma\pi_\sigma(\tau)
\ge\frac{a_K^n}{n!}.
\tag{15.9}
\]

Usando
\(\sum\pi_\sigma'^2\le
(\max|\pi_\sigma'|)\sum|\pi_\sigma'|\), obtenemos la cota explícita

\[
\boxed{
I_n^{[P]}(\tau)\le I_n^\Pi(\tau)
\le
\frac{n!}{a_K^n}\,n(n-1)^2\kappa_K^2.
}
\tag{15.10}
\]

Esto satisface `U-PASS-1`: existe una cota rigurosa con dependencia
explícita en \(n\). No es una cota polinómica de Fisher; el factor
\(n!/a_K^n\) procede exclusivamente de usar la probabilidad mínima global de
celda y puede ser extremadamente grosero. No se afirma que describa el
crecimiento real de \(I_n^\Pi\).

### 15.4. Ruta U4: lugar exacto donde se pierde uniformidad QMD

Definamos el vector de raíces

\[
s_n(\tau):=(\sqrt{\pi_\sigma(\tau)})_{\sigma\in\mathfrak S_n}
\in\ell^2(\mathfrak S_n).
\]

La prueba fixed-\(n\) de (12.3) usa que, para un alfabeto finito,
el máximo de \(n!\) restos escalares es \(o(\delta)\). Ese paso no da
control al variar \(n\). Por el teorema fundamental del cálculo,

\[
\|s_n(\tau+\delta)-s_n(\tau)-\delta\dot s_n(\tau)\|_2
\le |\delta|\sup_{|h|\le|\delta|}
\|\dot s_n(\tau+h)-\dot s_n(\tau)\|_2.
\tag{15.11}
\]

Así, el primer lema suficiente para ventanas \(\delta_n\) es un control del
módulo

\[
\Omega_{n,K}(\eta):=
\sup_{\substack{\tau,\tau+h\in K\\|h|\le\eta}}
\|\dot s_n(\tau+h)-\dot s_n(\tau)\|_2.
\tag{15.12}
\]

En concreto, \(\Omega_{n,K}(|\delta_n|)\to0\) implicaría un resto QMD
uniforme a lo largo de esa ventana. La cota de Fisher
\(4\|\dot s_n(\tau)\|_2^2=I_n^\Pi(\tau)\) controla el tamaño de la derivada,
pero no su módulo de continuidad; (15.10) no implica (15.12).

```text
FIRST_MISSING_LEMMA = UNIFORM_SQRT_SCORE_MODULUS_LEMMA
TARGET = find delta_n and prove Omega_{n,K}(|delta_n|) -> 0
```

Para mejorar primero la escala de Fisher, el sublema cuantitativo natural
es una desigualdad de flujo ponderado que controle directamente
\(\sum_\sigma\pi_\sigma'^2/\pi_\sigma\), sin sustituir todos los
denominadores por \(\min_\sigma\pi_\sigma\).

### 15.5. Evaluación de rutas, falsificador y recomendación

- **U1:** usable a través de (15.5), pero el log-score introduce los
  denominadores de celdas raras; no cierra por sí solo una escala útil.
- **U2:** no aplicable entre complete data y permutaciones por las razones de
  §15.2; sí da la contracción finita (15.3) entre permutaciones y posets.
- **U3:** mejor ruta del preflight; produce (15.7)--(15.10) sin enumerar
  permutaciones.
- **U4:** identifica mediante (15.11)--(15.12) el término exacto ausente para
  ventanas dependientes de \(n\).

El falsificador temprano es la concentración del flujo de frontera en
celdas cuya probabilidad sea factorial o exponencialmente pequeña. Si una
familia de tales celdas hace que el Fisher ponderado o
\(\Omega_{n,K}(h)\) sature necesariamente factores del orden de
\(n!/a_K^n\) en toda ventana candidata, no habrá una ventana cuantitativa útil
por esta ruta. Las cotas actuales detectan ese riesgo, pero no demuestran que
la saturación ocurra.

El siguiente run mínimo, si se autorizara, debería atacar únicamente el
`UNIFORM_SQRT_SCORE_MODULUS_LEMMA`, precedido por una cota de flujo ponderado
que evite el mínimo global de celda. No se autoriza aquí ese run.

## 16. `AGGREGATE_BOUNDARY_FLUX_PREFLIGHT`

```text
NATURALEZA = EXPLORATORY_ANALYTIC_PREFLIGHT
AGGREGATE_BOUNDARY_FLUX_PREFLIGHT = PASS_AGGREGATE_LEMMA_IDENTIFIED
UNIFORM_SQRT_SCORE_MODULUS = DEFERRED_NOT_OPENED
POISSON_MIXTURE_REGULARITY = OPEN_NOT_STARTED
FISHER_TO_LOCALISATION_BRIDGE = NOT_OPENED
NEXT_RUN_AUTHORIZED = NO
```

### 16.1. Auditoría exacta de la cota factorial

Con \(F_{\sigma,n}=\pi_\sigma'\), la cadena de §15 es

\[
\begin{aligned}
\mathcal B_n(\tau)
&=\sum_\sigma\frac{F_{\sigma,n}^2}{\pi_\sigma}\\
&\le \frac1{\min_\sigma\pi_\sigma}
       \sum_\sigma F_{\sigma,n}^2\\
&\le \frac1{\min_\sigma\pi_\sigma}
       \left(\max_\sigma|F_{\sigma,n}|\right)
       \sum_\sigma|F_{\sigma,n}|\\
&\le \frac{n!}{a_K^n}\,
       [(n-1)\kappa_K]\,[n(n-1)\kappa_K].
\end{aligned}
\tag{16.1}
\]

Las pérdidas son distintas y deben mantenerse separadas:

```text
LOSS-1 = tomar valores absolutos cara a cara en (15.5), perdiendo
         cancelaciones dentro del flujo firmado F_sigma
LOSS-2 = eliminar las demás restricciones de cámara al acotar cada integral
         de coárea por el volumen completo de su proyección
LOSS-3 = usar sum F_sigma^2 <= max|F_sigma| sum|F_sigma|
LOSS-4 = desacoplar flujo y masa mediante
         1/pi_sigma <= 1/min_eta pi_eta
LOSS-5 = minorar cada celda por el evento suficiente "todos los puntos en R"
LOSS-6 = asignar a cada permutación sólo 1/n! del volumen de R^n
```

El factor \(a_K^{-n}\) nace en `LOSS-5`: exigir que los \(n\) puntos caigan
simultáneamente en un rectángulo local de masa al menos \(a_K\). El factor
\(n!\) nace en `LOSS-6`: dentro de ese rectángulo, las \(n!\) permutaciones
de rangos tienen igual volumen. Ambos entran en Fisher sólo después de
`LOSS-4`, cuando todos los denominadores se sustituyen por la peor celda.
Por tanto no está probado que ninguno de esos factores describa el Fisher
agregado real.

### 16.2. B1: interfaces compartidas y flujo antisimétrico

Fuera de empates múltiples, una cara móvil de una cámara está dada por el
intercambio de dos posiciones adyacentes en el orden por \(u\). Si
\(s_k=(k,k+1)\), las dos permutaciones de rango a ambos lados difieren por
el intercambio correspondiente de las entradas en las posiciones \(k\) y
\(k+1\). Agregando todos los componentes geométricos que separan dos
celdas \(\sigma\) y \(\eta\), definamos \(J_{\sigma,\eta}(\tau)\) como el
flujo firmado orientado hacia la celda \(\sigma\).

La misma interfaz con la orientación opuesta da exactamente

\[
J_{\sigma,\eta}=-J_{\eta,\sigma}.
\tag{16.2}
\]

La fórmula (15.5), agrupada por interfaces, se convierte en la identidad de
divergencia

\[
\boxed{
F_{\sigma,n}(\tau)
=\sum_{\eta\sim\sigma}J_{\sigma,\eta}(\tau).
}
\tag{16.3}
\]

La suma total de (16.3) es cero por (16.2), en acuerdo con
\(\sum_\sigma\pi_\sigma'=0\). Esta antisimetría es exacta, pero por sí sola
no controla la energía ponderada: las cancelaciones pueden reducir
\(F_\sigma\), nunca proporcionar automáticamente el factor \(\pi_\sigma\)
que exige Fisher.

### 16.3. B2/B3: reducción a una desigualdad flujo--masa local

Sea \(Q_{\sigma,\eta}=Q_{\eta,\sigma}\ge0\) el flujo absoluto de la interfaz:
se integra el valor absoluto de la velocidad normal con la misma medida de
coárea que en (15.5), sumando todos sus componentes. Entonces

\[
|J_{\sigma,\eta}|\le Q_{\sigma,\eta},
\qquad
Q_\sigma:=\sum_{\eta\sim\sigma}Q_{\sigma,\eta}.
\tag{16.4}
\]

El recuento agregado de §15.3 ya demuestra

\[
\sum_{\{\sigma,\eta\}}Q_{\sigma,\eta}
\le\binom n2\kappa_K,
\tag{16.5}
\]

donde cada interfaz no orientada se cuenta una sola vez. Así, el área/flujo
total relevante tiene una cota polinómica; no contiene un factor \(n!\).

Aplicando Cauchy--Schwarz **antes** de dividir por la masa de la celda,

\[
F_{\sigma,n}^2
\le Q_\sigma
\sum_{\eta\sim\sigma}
\frac{J_{\sigma,\eta}^2}{Q_{\sigma,\eta}},
\tag{16.6}
\]

con la convención \(0/0=0\). Por tanto basta una comparación local entre el
flujo incidente y la masa:

```text
AGGREGATE_FLUX_MASS_TRACE_LEMMA

Existe C_{n,K} explícita, sin crecimiento factorial impuesto a priori,
tal que para toda sigma y tau in K,

    Q_sigma(tau) <= C_{n,K} pi_sigma(tau).
```

Si este lema vale, (16.4)--(16.6) implican rigurosamente

\[
\begin{aligned}
\mathcal B_n(\tau)
&\le C_{n,K}
\sum_\sigma\sum_{\eta\sim\sigma}
\frac{J_{\sigma,\eta}^2}{Q_{\sigma,\eta}}\\
&\le C_{n,K}
\sum_\sigma\sum_{\eta\sim\sigma}Q_{\sigma,\eta}\\
&\le C_{n,K}\,n(n-1)\kappa_K.
\end{aligned}
\tag{16.7}
\]

Esta reducción conserva conjuntamente masa y flujo hasta el único paso
\(Q_\sigma/\pi_\sigma\le C_{n,K}\), y evita por completo
\(1/\min_\sigma\pi_\sigma\). Probar una cota subfactorial para
\(C_{n,K}\) produciría una mejora subfactorial de Fisher. El preflight no
demuestra esa desigualdad de traza ni propone una escala para
\(C_{n,K}\).

### 16.4. B4: estado del falsificador de celdas raras

Una masa pequeña \(\pi_{\sigma_n}\) no es por sí sola una obstrucción.
Para probar `OBSTRUCTION_RARE_CELLS_PROVED` haría falta una familia explícita
con una cota inferior del tipo

\[
\frac{F_{\sigma_n,n}(\tau)^2}{\pi_{\sigma_n}(\tau)}
\ge L_n,
\tag{16.8}
\]

para una sucesión \(L_n\) que fuerce crecimiento fuerte del Fisher. La
representación disponible no proporciona tal cota inferior: (15.7),
(15.8) y (16.5) son cotas superiores de flujo y permiten cancelaciones
firmadas. Tampoco se ha probado que \(Q_{\sigma_n}/\pi_{\sigma_n}\) sea
grande para una familia explícita.

```text
RARE_CELL_MASS_SMALL = POSSIBLE_BUT_NOT_A_FISHER_OBSTRUCTION
RARE_CELL_FISHER_LARGE = NOT_PROVED
RARE_CELL_OBSTRUCTION = OPEN
```

### 16.5. Evaluación y techo

- **B1:** pasa estructuralmente; (16.2)--(16.3) dan el balance exacto sobre
  el grafo de interfaces.
- **B2:** reduce el problema a un único lema local de traza flujo--masa.
- **B3:** (16.5) prueba que el flujo absoluto total se cuenta por pares y
  tiene cota polinómica, no factorial.
- **B4:** no produce obstrucción; falta toda cota inferior rare-cell del
  tipo (16.8).

El preflight no demuestra una cota subfactorial para \(\mathcal B_n\), pero
sí elimina la necesidad lógica de usar la probabilidad mínima global y
reduce una mejora agregada a `AGGREGATE_FLUX_MASS_TRACE_LEMMA`. No se abre
el `UNIFORM_SQRT_SCORE_MODULUS_LEMMA`, no se estudia la mezcla Poisson y no
se extrae ninguna consecuencia de localización.

## 17. `AGGREGATE_FLUX_MASS_TRACE_LEMMA`

```text
AGGREGATE_FLUX_MASS_TRACE_LEMMA = OPEN_REDUCED
BEST_POSITIVE_ROUTE = INTEGRATED_ADJACENT_GAP_HAZARD
NO_SUBFACTORIAL_CONSTANT_PROVED
NO_RARE_CELL_OBSTRUCTION_PROVED
UNIFORM_SQRT_SCORE_MODULUS = DEFERRED_NOT_OPENED
POISSON_MIXTURE_REGULARITY = OPEN_NOT_STARTED
FISHER_TO_LOCALISATION_BRIDGE = NOT_OPENED
KERR_SPIN_SIGN_CONJECTURE = ARCHIVED_NOT_OPENED
NEXT_RUN_AUTHORIZED = NO
```

### 17.1. Definición exacta del cociente

Para \(\alpha\in\mathfrak S_n\), \(1\le k<n\) y
\(\beta(j)=\alpha(\sigma^{-1}(j))\), definamos la masa de la cámara
etiquetada

\[
p_{\alpha,\sigma}(\tau)
:=c_B^n\int_{B^n}
\mathbf 1_{\{v_{\beta(1)}<\cdots<v_{\beta(n)}\}}
\prod_{\ell=1}^{n-1}
\mathbf 1_{\{g_{\alpha,\ell}>0\}}\,dx
\tag{17.1}
\]

y la traza absoluta de su cara \(k\),

\[
q_{\alpha,k,\sigma}(\tau)
:=c_B^n\int_{B^n}
\mathbf 1_{\{v_{\beta(1)}<\cdots<v_{\beta(n)}\}}
\prod_{\ell\ne k}
\mathbf 1_{\{g_{\alpha,\ell}>0\}}
\delta_0(g_{\alpha,k})
|\partial_\tau g_{\alpha,k}|\,dx.
\tag{17.2}
\]

Estas son exactamente las integrales ya presentes en (15.5), con valor
absoluto antes de agregar las orientaciones. Las definiciones de §§11 y 16
dan

\[
\pi_\sigma=\sum_\alpha p_{\alpha,\sigma},
\qquad
Q_\sigma=\sum_\alpha\sum_{k=1}^{n-1}q_{\alpha,k,\sigma}.
\tag{17.3}
\]

Por tanto, si

\[
h_{\alpha,\sigma}(\tau)
:=\frac{\sum_{k=1}^{n-1}q_{\alpha,k,\sigma}(\tau)}
        {p_{\alpha,\sigma}(\tau)},
\tag{17.4}
\]

entonces el cociente buscado es exactamente

\[
\boxed{
R_{\sigma,n}(\tau)
:=\frac{Q_\sigma(\tau)}{\pi_\sigma(\tau)}
=\sum_\alpha
\frac{p_{\alpha,\sigma}(\tau)}{\pi_\sigma(\tau)}
h_{\alpha,\sigma}(\tau).
}
\tag{17.5}
\]

Es una media convexa de trazas por unidad de masa, no una razón entre el
área total del arreglo de \(n!\) celdas y la masa de una sola celda. Además,
la permutación simultánea de las etiquetas preserva \(B^n\), la medida
uniforme, (17.1) y la suma sobre \(k\) en (17.2), y lleva cualquier
\(\alpha\) a cualquier otra. En consecuencia,

\[
p_{\alpha,\sigma}=\frac{\pi_\sigma}{n!},
\qquad
h_{\alpha,\sigma}=R_{\sigma,n}
\quad\text{para toda }\alpha.
\tag{17.6}
\]

La cancelación de \(n!\) en (17.5)--(17.6) es exacta. No prueba una cota
subfactorial, pero descarta que el **número de cámaras etiquetadas** fuerce
por sí mismo un factor factorial en \(R_{\sigma,n}\).

Geométricamente, \(R_{\sigma,n}\) es la suma, sobre las \(n-1\) caras de
colisión adyacente de una cámara etiquetada, de la velocidad normal absoluta
integrada en la cara, dividida por el volumen de esa misma cámara. Es una
razón de traza móvil/masa celular, o equivalentemente un hazard agregado de
gaps adyacentes en cero.

### 17.2. Slicing radial exacto y fallo de la traza punto a punto

Fijemos \((\alpha,k)\) y tomemos
\(r_j=r_{\alpha(k+1)}\) como coordenada transversal. Denotemos por \(y\)
las restantes \(2n-1\) coordenadas. Como
\(|\partial_{r_j}g_{\alpha,k}|\ge c_K\), para cada \(y\) hay a lo sumo una
raíz \(r_j=\rho_{\alpha,k}(\tau,y)\) de \(g_{\alpha,k}=0\).

Las desigualdades de la cámara restringen \(r_j\) a un intervalo abierto
posiblemente vacío

\[
I_{\alpha,k}(\tau,y)
=(L_{\alpha,k}(\tau,y),U_{\alpha,k}(\tau,y))
\subseteq(r_a,r_b),
\tag{17.7}
\]

porque \(r_j\mapsto u_\tau(v_j,r_j)\) es estrictamente decreciente y las
únicas restricciones móviles sobre esa variable son comparaciones con sus
vecinos en el orden por \(u\). Escribamos
\(\ell_{\alpha,k}=|I_{\alpha,k}|\).

Fubini y coárea expresan la masa y la traza, suprimiendo sólo indicadores
fijos comunes, en la forma

\[
p_{\alpha,\sigma}
=c_B^n\int \ell_{\alpha,k}(\tau,y)\,d\nu_{\alpha,k}(y),
\tag{17.8}
\]

\[
q_{\alpha,k,\sigma}
=c_B^n\int
\mathbf 1_{\{\rho_{\alpha,k}(\tau,y)
\text{ es el extremo activo de }I_{\alpha,k}(\tau,y)\}}
w_{\alpha,k}(\tau,y)\,d\nu_{\alpha,k}(y),
\tag{17.9}
\]

donde

\[
0\le w_{\alpha,k}(\tau,y)
=\frac{|\partial_\tau g_{\alpha,k}|}
       {|\partial_{r_j}g_{\alpha,k}|}
\le\frac{2A_K}{c_K}.
\tag{17.10}
\]

Las fórmulas (17.8)--(17.10) muestran por qué las cotas disponibles no
bastan para una traza por slices: no proporcionan una cota inferior positiva
para \(\ell_{\alpha,k}\), ni relacionan su posible pequeñez con la de
\(w_{\alpha,k}\) en el extremo activo. En particular, no permiten deducir
una cota punto a punto

\[
w_{\alpha,k}\mathbf 1_{\{\text{extremo activo}\}}
\le C\,\ell_{\alpha,k}
\tag{17.11}
\]

con \(C\) uniforme basada sólo en (15.4). Esto bloquea la derivación ingenua
del trace lemma, pero no prueba que la desigualdad punto a punto sea falsa
para la geometría EF completa. Tampoco decide la desigualdad integrada: los
slices delgados podrían ocupar una medida
\(d\nu_{\alpha,k}\) proporcionalmente pequeña.

### 17.3. Reducción a un sublema de hazard integrado

La condición suficiente estrictamente más concreta es:

```text
INTEGRATED_ADJACENT_GAP_HAZARD_LEMMA

Existen H_{n,K} explícitas y subfactoriales tales que, uniformemente en
tau in K, sigma, alpha y k,

  integral 1_{active endpoint} w_{alpha,k} dnu_{alpha,k}
    <= H_{n,K}
       integral ell_{alpha,k} dnu_{alpha,k}.
```

Si este lema vale, (17.8)--(17.10) dan

\[
q_{\alpha,k,\sigma}\le H_{n,K}p_{\alpha,\sigma},
\]

y al sumar las \(n-1\) caras y usar (17.5),

\[
\boxed{
Q_\sigma(\tau)
\le C_{n,K}\pi_\sigma(\tau),
\qquad
C_{n,K}:=(n-1)H_{n,K}.
}
\tag{17.12}

El factor \(n-1\) es el grado local de la cámara de orden, no el número
\(n!\) de permutaciones. Si \(H_{n,K}\) es subfactorial, también lo es
\(C_{n,K}\). Este run no prueba ninguna cota para \(H_{n,K}\): hacerlo
requiere controlar la medida agregada de slices con intervalo factible
pequeño, usando la geometría conjunta de los gaps vecinos.

### 17.4. Ataque adversarial

El mecanismo adversarial concreto sugerido por (17.8)--(17.10) son slices
con

\[
\ell_{\alpha,k}(\tau,y)\ll1,
\qquad
w_{\alpha,k}(\tau,y)\ge w_0>0.
\tag{17.13}

Esto demuestra solamente una razón slice-wise grande. Para convertirlo en
una obstrucción hace falta además una familia explícita \(\sigma_n\) y un
conjunto de \(y\) de medida suficientemente grande que produzca una cota
inferior factorial para el cociente de las integrales (17.9)/(17.8). No se
ha obtenido tal familia ni tal cota de medida.

```text
ADVERSARIAL_CANDIDATE = THIN_FEASIBLE_RADIAL_SLICES
CLASSIFICATION = RARE_MASS_ONLY_AT_PRESENT
RARE_MASS_WITH_LARGE_TRACE = NOT_PROVED
OBSTRUCTION_STATUS = OPEN
```

### 17.5. Veredicto y techo

La ruta positiva logra dos avances exactos: cancela el \(n!\) de cámaras
etiquetadas en el cociente (17.5)--(17.6), y reduce la constante buscada a
\((n-1)H_{n,K}\), donde \(H_{n,K}\) es un único hazard integrado de gap
adyacente. No demuestra que \(H_{n,K}\) sea subfactorial. El ataque
adversarial identifica slices delgados, pero no prueba que tengan masa
suficiente para obstruir una cota subfactorial.

Por tanto el único veredicto justificado es

```text
AGGREGATE_FLUX_MASS_TRACE_LEMMA = OPEN_REDUCED
EXACT_C_NK = (n-1) H_{n,K} CONDITIONAL_ON_MISSING_LEMMA
ASYMPTOTIC_CLASS_C_NK = NOT_PROVED
HIDDEN_MIN_CELL_MASS_USED = NO
FIRST_MISSING_LEMMA = INTEGRATED_ADJACENT_GAP_HAZARD_LEMMA
```

## 18. `INTEGRATED_ADJACENT_GAP_HAZARD_LEMMA`

```text
INTEGRATED_ADJACENT_GAP_HAZARD_LEMMA = OPEN_REDUCED
BEST_ROUTE = ACTIVE_ENDPOINT_TO_MEAN_THICKNESS
NO_SUBFACTORIAL_H_NK_PROVED
NO_INTEGRATED_THIN_SLICE_OBSTRUCTION_PROVED
UNIFORM_SQRT_SCORE_MODULUS = DEFERRED_NOT_OPENED
POISSON_MIXTURE_REGULARITY = OPEN_NOT_STARTED
FISHER_TO_LOCALISATION_BRIDGE = NOT_OPENED
KERR_SPIN_SIGN_CONJECTURE = ARCHIVED_NOT_OPENED
NEXT_RUN_AUTHORIZED = NO
```

### 18.1. Definición óptima y completamente cuantificada de \(H_{n,K}\)

Fijemos \(n\ge2\), un compacto \(K\Subset(0,\infty)\),
\(\tau\in K\), \(\sigma,\alpha\in\mathfrak S_n\) y
\(1\le k<n\). Conservamos literalmente el slicing de §17.2:

- el gap adyacente es
  \(g_{\alpha,k}=u_{\alpha(k+1)}-u_{\alpha(k)}\);
- la variable transversal es \(r_j=r_{\alpha(k+1)}\);
- \(y\) reúne las otras \(2n-1\) coordenadas;
- \(d\nu_{\alpha,k}^{\tau,\sigma}(y)\) es Lebesgue en esas
  coordenadas, restringida por el orden fijo en \(v\), por la caja y por
  los indicadores de cámara independientes de \(r_j\) que fueron
  suprimidos en (17.8)--(17.9);
- \(I_{\alpha,k}(\tau,y)\) es el intervalo factible de \(r_j\) después
  de imponer las restricciones restantes, y
  \(\ell_{\alpha,k}=|I_{\alpha,k}|\);
- \(E_{\alpha,k}(\tau)\) es el conjunto de \(y\) para los que la raíz
  \(\rho_{\alpha,k}(\tau,y)\) de \(g_{\alpha,k}=0\) existe y es el
  endpoint activo de ese intervalo;
- la densidad de velocidad de la traza es

\[
w_{\alpha,k}(\tau,y)
=\frac{|\partial_\tau g_{\alpha,k}|}
       {|\partial_{r_j}g_{\alpha,k}|}
\,\mathbf 1_{E_{\alpha,k}(\tau)}(y).
\tag{18.1}
\]

La condición de factibilidad aparece exactamente en
\(\ell_{\alpha,k}>0\) para la masa y en
\(E_{\alpha,k}(\tau)\) para la traza. Con esta notación, (17.8)--(17.9)
son

\[
p_{\alpha,\sigma}
=c_B^n\int\ell_{\alpha,k}\,d\nu_{\alpha,k}^{\tau,\sigma},
\qquad
q_{\alpha,k,\sigma}
=c_B^n\int w_{\alpha,k}\,d\nu_{\alpha,k}^{\tau,\sigma}.
\tag{18.2}
\]

Como \(p_{\alpha,\sigma}>0\) por el lema de soporte completo, la constante
óptima requerida por §17.3 queda definida sin ninguna constante oculta:

\[
\boxed{
H^*_{n,K}:=
\sup_{\substack{\tau\in K,\ \sigma,\alpha\in\mathfrak S_n\\
                  1\le k<n}}
\frac{\displaystyle
      \int w_{\alpha,k}(\tau,y)
      \,d\nu_{\alpha,k}^{\tau,\sigma}(y)}
     {\displaystyle
      \int\ell_{\alpha,k}(\tau,y)
      \,d\nu_{\alpha,k}^{\tau,\sigma}(y)}
=
\sup_{\tau,\sigma,\alpha,k}
\frac{q_{\alpha,k,\sigma}(\tau)}
     {p_{\alpha,\sigma}(\tau)}.
}
\tag{18.3}
\]

Esta es la forma más explícita disponible en el WP. La uniformidad exigida
es simultánea en \(\tau\in K\), en las dos permutaciones etiquetadas y en
la cara adyacente. La medida depende de esos datos y no se sustituye por
una ley iid de gaps ni por una distribución estándar de estadísticos de
orden.

La simetría simultánea de etiquetas de (17.6) elimina el supremo en
\(\alpha\), pero no los de \(\sigma\), \(k\) o \(\tau\). En particular,
no convierte los gaps condicionados por el orden en \(v\) en gaps de
estadísticos iid. Por ello la ruta H1 no autoriza ninguna identidad estándar
de order statistics con las hipótesis actualmente demostradas.

### 18.2. Separación exacta entre velocidad y geometría thin-slice

De (17.10), uniformemente en todos los índices,

\[
0\le w_{\alpha,k}
\le W_K\mathbf 1_{E_{\alpha,k}(\tau)},
\qquad
W_K:=\frac{2A_K}{c_K}.
\tag{18.4}
\]

Definamos la constante geométrica óptima

\[
\boxed{
D^*_{n,K}:=
\sup_{\tau,\sigma,\alpha,k}
\frac{\nu_{\alpha,k}^{\tau,\sigma}
      (E_{\alpha,k}(\tau))}
     {\displaystyle
      \int\ell_{\alpha,k}(\tau,y)
      \,d\nu_{\alpha,k}^{\tau,\sigma}(y)}.
}
\tag{18.5}
\]

Tonelli y (18.4) dan la desigualdad demostrada

\[
\boxed{H^*_{n,K}\le W_KD^*_{n,K}.}
\tag{18.6}
\]

Así, toda posible dependencia factorial ha quedado confinada a
\(D^*_{n,K}\). Ni \(W_K\), ni el paso (18.6), ni la simetría de etiquetas
contienen \(n!\), \(1/\min_\sigma\pi_\sigma\) o un gap mínimo global.
El cociente (18.5) tiene una interpretación exacta: medida de los slices
que alcanzan la cara adyacente, dividida por el espesor radial total de la
propia cámara. Es una comparación endpoint/mean-thickness puramente
geométrica.

Por consiguiente, el sublema único estrictamente menor que queda es:

```text
ACTIVE_ENDPOINT_TO_MEAN_THICKNESS_LEMMA

Probar una cota explícita subfactorial D_{n,K} para D^*_{n,K},
uniformemente en tau in K, sigma, alpha y k, usando la geometría conjunta
de los dos gaps vecinos que determinan I_{alpha,k}(tau,y).
```

Si se prueba, puede tomarse

\[
H_{n,K}=W_KD_{n,K}=\frac{2A_K}{c_K}D_{n,K}.
\tag{18.7}
\]

La reducción es estricta respecto de (18.3): la velocidad normal móvil ya
está eliminada mediante una constante \(K\)-local explícita e independiente
de \(n\); sólo permanece la ocupación geométrica de slices finos.

### 18.3. H1/H2 y test adversarial H3

La suma de gaps radiales de una configuración telescopa sólo después de
fijar un mismo orden radial. Aquí los endpoints de
\(I_{\alpha,k}(\tau,y)\) se obtienen de comparaciones en \(u_\tau\), cuyos
umbrales dependen también de los distintos \(v_i\). El orden fijo en \(v\)
está además enlazado con \(\sigma\) por (11.3). Por tanto, con los resultados
actuales no hay una normalización telescópica demostrada que acote (18.5).
Usarla sería importar precisamente la hipótesis iid que debe probarse.

La integración antes del supremo puntual sí está preservada en (18.3) y
(18.5): no aparece \(\sup 1/\ell\). Sin embargo, la mera descomposición

\[
E_{\alpha,k}
=\bigl(E_{\alpha,k}\cap\{\ell<s\}\bigr)
 \cup
 \bigl(E_{\alpha,k}\cap\{\ell\ge s\}\bigr)
\tag{18.8}
\]

sólo controla la segunda parte por
\(s^{-1}\int\ell\,d\nu\). Para la primera hace falta una cota cuantitativa
de

\[
\nu_{\alpha,k}^{\tau,\sigma}
\bigl(E_{\alpha,k}\cap\{0<\ell<s\}\bigr)
\tag{18.9}
\]

en términos de la masa de espesor de la misma cámara. Ninguna estimación
del WP controla actualmente (18.9), uniformemente en \(\sigma\) y \(n\).
Esta es la forma distributiva concreta del sublema (18.5).

El candidato adversarial sigue siendo una familia que concentre una
fracción apreciable de la medida de endpoints en \(\ell\downarrow0\). Pero
(17.13) sólo exhibe la geometría posible de un slice fino: no proporciona
una familia explícita \(\sigma_n\), ni una cota inferior para (18.9), ni
crecimiento no subfactorial de (18.5). La clasificación rigurosa permanece

```text
THIN_SLICE_GEOMETRY = PRESENT
INTEGRATED_HAZARD_DIVERGENCE = NOT_PROVED
ADVERSARIAL_CLASSIFICATION = RARE_MASS_ONLY_AT_PRESENT
```

### 18.4. Veredicto y consecuencias condicionales

No se ha demostrado ninguna clase asintótica para \(D^*_{n,K}\) y, por
tanto, tampoco para \(H^*_{n,K}\). Sí se ha reemplazado la constante
existencial de §17.3 por el supremo exacto (18.3) y se ha reducido éste a
una sola razón geométrica endpoint/mean-thickness, sin extremos por celda.

El único veredicto justificado es

```text
INTEGRATED_ADJACENT_GAP_HAZARD_LEMMA = OPEN_REDUCED
EXACT_H_NK_DEFINITION = H^*_{n,K} IN (18.3)
PROVED_H_NK_BOUND = H^*_{n,K} <= (2 A_K/c_K) D^*_{n,K}
ASYMPTOTIC_CLASS_H_NK = NOT_PROVED
MIN_GAP_OR_MIN_CELL_MASS_USED = NO
FIRST_MISSING_SUBLEMMA = ACTIVE_ENDPOINT_TO_MEAN_THICKNESS_LEMMA
```

Condicionalmente a una cota subfactorial explícita
\(D^*_{n,K}\le D_{n,K}\), (17.12), (18.7) y (16.7) darían

\[
C_{n,K}=(n-1)\frac{2A_K}{c_K}D_{n,K},
\tag{18.10}
\]

\[
\boxed{
I_n^{[P]}(\tau)\le I_n^\Pi(\tau)
\le n(n-1)^2\kappa_K\frac{2A_K}{c_K}D_{n,K}.
}
\tag{18.11}
\]

No se abre el sublema (18.5), ni uniformidad QMD, mezcla Poisson,
Fisher--localización o Kerr.
