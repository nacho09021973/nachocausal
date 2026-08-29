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

### 11.3. Techo de este gate

La prueba es para cada \(n\) fijo. No proporciona cotas uniformes en \(n\)
para \(\pi_\sigma'\), no intercambia derivación con \(n\to\infty\) y no
calcula todavía información Fisher. En particular, en este gate no se
promueve QMD ni se abre el puente hacia localización.

```text
QUANTITATIVE_FULL_SUPPORT_LEMMA = PROVED
FINITE_CHANNEL_SUPPORT = FULL_FOR_PERMUTATION_CHANNEL
FINITE_CHANNEL_DIFFERENTIABILITY = PROVED_C1_LOCAL
FINITE_CHANNEL_QMD = OPEN
UNIFORM_IN_N_REGULARITY = OPEN
DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL
FISHER_TO_LOCALISATION_BRIDGE = NOT_OPENED
NEXT_RUN_AUTHORIZED = NO
```

## 12. Veredicto y siguiente frontera

```text
COMMON_POINT_ISOMORPHISM = REFUTED
MOVING_SUPPORT_QMD_STATUS = PROVED_NON_QMD_FOR_POINT_EXPERIMENT
FINITE_CHANNEL_DIFFERENTIABILITY = PROVED_C1_LOCAL
FINITE_CHANNEL_QMD = OPEN
DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL
FISHER_TO_LOCALISATION_BRIDGE = NOT_OPENED
NEXT_RUN_AUTHORIZED = NO
```

El esqueleto finito `Pi_n -> [P_{Pi_n}]` continúa siendo exacto y ahora se ha
probado que su canal de permutaciones tiene soporte total y probabilidades
\(C^1\) a cada cardinalidad finita. La promoción posterior a QMD no forma
parte de este gate: requiere una decisión separada y no queda autorizada por
este resultado.
