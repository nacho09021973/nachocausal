# `NC-2E` — escala de varianza seleccionada: reducción exacta a una discrepancia relativa

> **ESTADO: AVANCE ANALÍTICO PARCIAL · SE PRUEBA UNA DESIGUALDAD RELATIVA
> PARAMETRIZADA POR `|mathcal S_n|` Y UNA REDUCCIÓN EXACTA DE `NC2E-O3` A UNA
> COTA DE DISCREPANCIA RELATIVA · `NC2E.1` NO SE PRUEBA NI SE REFUTA ·
> SIN DATOS, SIMULACIONES, SEMILLAS, CÓDIGO NI ARTEFACTOS NUMÉRICOS NUEVOS.**

Autorización firmada:
`docs/program_reopening_note_2026-08-18_nc2e_selected_clt_scale_DRAFT.md` §9.
El sufijo histórico `_DRAFT` del nombre de esa nota no describe su estado.

## 1. Dominio condicionado, notación y medida

El experimento congelado es el de
`P1a_count_volume_lema_kl_d2.md` §1: `n` puntos iid uniformes en el cuadrado,
condicionados a `N=n`, con el orden producto y la representación por la
permutación de rangos \(\Pi_n\in\mathfrak S_n\). El grupo simétrico se denota
siempre \(\mathfrak S_n\) y no se abrevia.

El selector congelado `MIN_COVERAGE_LEX` recorre las cuádruplas

\[
Q_3(C)=\{(a,b,c,d):a\prec b\prec c\prec d,\ |[a,b]|\ge3,\ |[c,d]|\ge3\}
\]

y maximiza lexicográficamente \((\min(m_-,m_+),\,m_-+m_+)\). El suceso `S` es la
existencia de un maximizador único `q*`. Para el lado
`h in {PAST,FUTURE}` se escriben `M_h` para la cardinalidad del intervalo
cerrado correspondiente, `(K_h,L_h)` para los gaps de rangos de sus endpoints en
las dos coordenadas, y

\[
q_{n,h}=\sqrt{K_hL_h},
\qquad
Z_{n,h}=\frac{q_{n,h}}{n+1},
\qquad
\ell_h=\text{duración relativa del lado }h.
\tag{1.1}
\]

`NC-2B` garantiza que

\[
\mathcal S_n=\{\pi\in\mathfrak S_n:S(\pi)\}\ne\varnothing
\qquad(n\ge6),
\]

de modo que la medida uniforme seleccionada

\[
\nu_n(\pi)=\frac1{|\mathcal S_n|},\qquad\pi\in\mathcal S_n,
\tag{1.2}
\]

está bien definida. Todas las esperanzas y varianzas con subíndice \(\nu_n\) se
toman respecto de (1.2); coinciden con las esperanzas condicionadas
`E[.|n,h,S]` usadas en `NC-2C` y `NC-2D`, porque condicionar la medida uniforme
de \(\mathfrak S_n\) por `S` produce exactamente (1.2). Se escribe

\[
p_n=\Pr_n(S)=\frac{|\mathcal S_n|}{n!}.
\tag{1.3}
\]

Objetivo firmado `NC2E-O3`: decidir si existen `C_q<infinity` y `n_0` explícitos,
comunes a ambos lados, con `Var_{nu_n}(q_{n,h})<=C_q n`.

Esta nota **no** decide `NC2E-O3`. Prueba una desigualdad relativa nueva,
parametrizada por `|mathcal S_n|`, y reduce el objetivo a una única obligación
relativa explícita. No se creó ni ejecutó código, simulación, semilla, dato ni
artefacto numérico, y no se consultaron los tamaños sellados `n in {64,96,128}`
para elegir constantes ni rutas.

## 2. Identidades exactas utilizadas

Toda descomposición posterior se apoya únicamente en las cuatro identidades de
esta sección y en la identidad geométrica 2.5.

**2.1 Minimalidad de la media.** Para toda variable `X` en `L^2(nu_n)` y toda
constante `c`,

\[
\operatorname{Var}_{\nu_n}(X)
=\mathbb E_{\nu_n}[(X-\mathbb E_{\nu_n}X)^2]
\le\mathbb E_{\nu_n}[(X-c)^2].
\tag{2.1}
\]

Se usará con `c=(n+1)/2`, es decir con `Z-1/2`.

**2.2 Forma de pares.** Si `pi,sigma` son independientes con ley \(\nu_n\),

\[
\operatorname{Var}_{\nu_n}(q_{n,h})
=\frac1{2|\mathcal S_n|^2}
\sum_{\pi,\sigma\in\mathcal S_n}
\bigl(q_{n,h}(\pi)-q_{n,h}(\sigma)\bigr)^2 .
\tag{2.2}
\]

Es la identidad `(3.2)` de la nota firmada; se obtiene desarrollando el cuadrado
y usando \(\mathbb E[q(\pi)q(\sigma)]=(\mathbb E q)^2\).

**2.3 Capas.** Para `Y>=0`,
\(\mathbb E[Y^2\mathbf 1_S]=\int_0^\infty 2s\Pr(\{Y>s\}\cap S)\,ds\), de donde,
para todo `t>=0`,

\[
\mathbb E[Y^2\mathbf 1_S]
\le t^2\,p_n+\int_t^\infty 2s\Pr(Y>s)\,ds .
\tag{2.3}
\]

**2.4 División controlada.** Para toda `Y>=0`,

\[
\mathbb E_{\nu_n}[Y^2]=\frac{\mathbb E[Y^2\mathbf 1_S]}{p_n}.
\tag{2.4}
\]

Ninguna cola incondicional se usará sin dividir explícitamente por `p_n`; el
parámetro `p_n` aparece en el enunciado final y no se oculta en una constante.

**2.5 Intervalo igual a rectángulo de rangos.** En el orden producto,
`z in [a,b]` equivale a que los rangos de `z` estén entre los de `a` y los de `b`
en ambas coordenadas. Por tanto, si `I,J` son los intervalos cerrados de rangos
del lado `h`,

\[
|I|=K_h+1,\qquad |J|=L_h+1,\qquad M_h=N_{\Pi_n}(I,J),
\tag{2.5}
\]

donde `N_{Pi}(I,J)` es el número de puntos de la permutación en `I x J`. Con la
discrepancia rectangular

\[
\Delta_n=\max_{I,J}
\left|\frac{N_{\Pi_n}(I,J)}n-\frac{|I||J|}{n^2}\right|
\tag{2.6}
\]

(máximo sobre pares de intervalos de rangos, como en `NC-2C` §5 y `NC-2D` §4.2),
(2.5) da la identidad determinista

\[
q_{n,h}^2=K_hL_h=(K_h+1)(L_h+1)-(K_h+L_h+1)
= n\,M_h+n^2\theta_h-(K_h+L_h+1),
\qquad|\theta_h|\le\Delta_n .
\tag{2.7}
\]

(2.7) vale punto a punto en `S`, sin promediar. Muestra que la forma del ganador
está determinada por su conteo salvo el error de discrepancia de su propio
rectángulo; es la razón estructural por la que toda la sección 8 se reduce a
controlar \(\Delta_n\) bajo \(\nu_n\).

## 3. Grupo exacto de simetrías de la medida seleccionada

**Proposición 3.1.** Sean

\[
(D\pi)(i)=n+1-\pi(n+1-i),
\qquad
T\pi=\pi^{-1}.
\]

Entonces `D` y `T` son involuciones de \(\mathfrak S_n\), conmutan, preservan
\(\mathcal S_n\) y por tanto preservan \(\nu_n\). El grupo `{id,D,T,DT}` es un
grupo de Klein que actúa sobre \(\mathcal S_n\) por biyecciones que preservan la
medida. Además

\[
q_{n,h}(T\pi)=q_{n,h}(\pi),
\qquad
q_{n,\rm PAST}(D\pi)=q_{n,\rm FUTURE}(\pi).
\tag{3.1}
\]

**Demostración.** Que `D` preserva `S` y permuta los dos lados está probado en
`NC-2C` §2: la rotación de 180 grados revierte el orden producto, envía la cadena
`a prec b prec c prec d` a `Dd prec Dc prec Db prec Da`, intercambia los dos
intervalos y deja invariante el par
\((\min(m_-,m_+),m_-+m_+)\); luego conserva el número de maximizadores. Los gaps
de rangos del intervalo pasado de `D pi` son los del intervalo futuro de `pi`, de
donde la segunda igualdad de (3.1).

Que `T` preserva `S` está probado en `P1a_count_volume_lema_kl_d2.md` §7.1.1: la
inversión de la permutación intercambia los dos ejes de rangos, conserva el
poset, el score, `M` y la unicidad, y permuta `K_h` y `L_h`. Como
`q=sqrt(K L)` es simétrico en sus dos argumentos, `q` es invariante por `T`.

`D` actúa sobre los pares `(i,pi(i))` por
`(i,j) -> (n+1-i,n+1-j)` y `T` por `(i,j) -> (j,i)`; ambas son involuciones del
plano de rangos y conmutan entre sí, luego conmutan como transformaciones de
\(\mathfrak S_n\). Una biyección de un conjunto finito que lo preserva preserva
su medida uniforme. `QED`

**Corolario 3.2 (obligación de ambos lados, cerrada exactamente).**

\[
\operatorname{Var}_{\nu_n}(q_{n,\rm PAST})
=\operatorname{Var}_{\nu_n}(q_{n,\rm FUTURE}),
\qquad
\mathcal L_{\nu_n}(K_h,L_h)=\mathcal L_{\nu_n}(L_h,K_h).
\tag{3.2}
\]

Por tanto basta demostrar o refutar `NC2E.1` para un lado: la constante `C_q` y
el umbral `n_0` obtenidos valen automáticamente para el otro. Todos los enunciados
posteriores se formulan para un lado `h` arbitrario y valen simultáneamente para
los dos.

**Observación 3.3.** La inyección impar-par de `NC-2C` §4.4 (añadir un punto
aislado) **no** es una biyección y no preserva \(\nu_n\); sirve para transferir
cotas de `Pr(S)` entre paridades, no para simetrizar la medida seleccionada. No se
usa en esta nota.

## 4. Sensibilidad del ganador: lo probado y lo no probado

**Proposición 4.1 (dos testigos exactos, reprobados aquí).** Sea `n=2r>=8`.

1. La identidad `pi=id` pertenece a \(\mathcal S_n\) y su ganador único es
   `(1,r,r+1,n)`, con `K_h=L_h=r-1` y `q_{n,h}=n/2-1`.
2. La permutación `(n,n-1,...,7,1,2,3,4,5,6)` pertenece a \(\mathcal S_n\) y su
   ganador único tiene `K_h=L_h=2`, es decir `q_{n,h}=2`.

**Demostración.** (1) La identidad induce una cadena total de `n` elementos, en la
que `|[a,b]|=b-a+1`. Para `a<b<c<d` se tiene `m_-+m_+<=n`, luego
`min(m_-,m_+)<=r`; el valor `r` obliga a `m_-=m_+=r` y a `b-a+1=d-c+1=r` con
`b<c`, `a>=1`, `d<=n`, lo que fuerza `(a,b,c,d)=(1,r,r+1,n)`. El maximizador es
único y `K_h=L_h=r-1`.

(2) Las posiciones `1,...,n-6` reciben los valores `n,...,7` en orden decreciente:
forman una anticadena. Las posiciones `n-5,...,n` reciben `1,...,6` en orden
creciente: forman una 6-cadena. Un punto del primer grupo y otro del segundo son
incomparables, porque el primero tiene posición menor y valor mayor. Toda cuádrupla
admisible vive por tanto en la 6-cadena, y en una cadena de seis elementos la única
elección con `|[a,b]|>=3` y `|[c,d]|>=3` es tomar los elementos `1,3,4,6` de la
cadena. Ese ganador es único, con gaps `K_h=L_h=2`. `QED`

**Corolario 4.2 (no-go de soporte).** Para todo `n=2r>=8` existe una medida de
probabilidad soportada en \(\mathcal S_n\) cuya varianza de `q_{n,h}` es

\[
\frac14\left(\frac n2-3\right)^2=\Theta(n^2).
\]

En consecuencia, ninguna demostración de `NC2E.1` puede usar solamente el soporte
de \(\nu_n\), ni solamente una cota inferior para `|mathcal S_n|`: ambas cosas son
compatibles con varianza de orden `n^2`. Toda prueba debe usar cómo se reparte la
masa dentro de \(\mathcal S_n\).

**Lo que no está probado.** No se dispone de ninguna cota para la sensibilidad del
ganador bajo una modificación local. Concretamente:

- una transposición cambia las coordenadas de dos puntos, y por tanto cambia la
  cardinalidad de cualquier intervalo **cuyos endpoints no se muevan** en a lo
  sumo dos unidades; pero no acota el cambio del *máximo* del score, porque el
  ganador puede usar un punto movido y porque borrar un punto puede destruir todas
  las cuádruplas admisibles (el testigo 2 de la Proposición 4.1 lo exhibe: eliminar
  un punto de su 6-cadena deja `Q_3(C)` vacío);
- por tanto **no se supone** que una modificación local de la permutación cambie
  localmente al ganador, conforme a la prohibición explícita de la nota firmada;
- la oscilación determinista `Theta(n)` del Corolario 4.2 **no** es una varianza de
  ese orden: sólo prohíbe los argumentos de soporte.

## 5. Lema determinista de anclaje

Para `r in (0,1/8]` sea `m=floor(r n)` y sean, en cada eje de rangos,

\[
\begin{aligned}
B_1&=\{1,\ldots,m\}, &
B_2&=\{\lfloor n/2\rfloor-m+1,\ldots,\lfloor n/2\rfloor\},\\
B_3&=\{\lfloor n/2\rfloor+1,\ldots,\lfloor n/2\rfloor+m\}, &
B_4&=\{n-m+1,\ldots,n\},
\end{aligned}
\tag{5.1}
\]

y sea `A(r)` el suceso de que cada caja diagonal `B_j x B_j` contenga un punto de
la permutación. Los cuatro bloques crecen con `m`, luego `A(r)` es monótono
creciente en `r`. Defínase el **radio de anclaje**

\[
R=\min\{r\in\{2/n,3/n,\ldots,\lfloor n/8\rfloor/n\}:A(r)\ \text{ocurre}\},
\tag{5.2}
\]

con `R=1/8` si ningún `r` de la rejilla funciona. `R` es una variable aleatoria
con `2/n<=R<=1/8`.

**Lema 5.1 (cota puntual en `S`).** Existe `n_1` absoluto tal que, para todo
`n>=n_1`, todo `pi in mathcal S_n` y ambos lados,

\[
|Z_{n,h}-1/2|\le 2R+5\Delta_n+\frac{10}n
\quad\text{si }R\le\frac1{40}\text{ y }\Delta_n\le\frac1{100},
\tag{5.3}
\]

y, sin ninguna hipótesis adicional,

\[
\boxed{\,|Z_{n,h}-1/2|\le 50\,(R+\Delta_n)+\frac{10}n
\quad\text{en todo }\mathcal S_n. }
\tag{5.4}
\]

**Demostración.** Supóngase `R<=1/40` y `Delta_n<=1/100`, y tómese `r=R`, de modo
que `A(r)` ocurre. Elíjase un punto en cada caja diagonal. Los cuatro bloques son
disjuntos y crecientes en ambas coordenadas, luego los cuatro puntos forman una
4-cadena `p_1 prec p_2 prec p_3 prec p_4`.

Los dos rectángulos laterales de esa cadena tienen, en cada eje, longitud de rangos
al menos `n(1/2-2r)-1`. Escríbase

\[
u=\frac12-2r-\frac1n\ \ (\ge0.44\text{ para }r\le1/40,\ n\ge100).
\]

Por (2.6), sus cardinalidades cumplen `M_\pm/n>=u^2-\Delta_n>=0.1836>1/6`, en
particular `M_\pm>=3` para `n>=17`: la cuádrupla pertenece a `Q_3(C)`. Como el
ganador maximiza `min(m_-,m_+)`, ambos lados del ganador satisfacen

\[
\frac{M_h}n\ge u^2-\Delta_n .
\tag{5.5}
\]

Aplicando (2.6) al propio rectángulo del ganador, ahora en el sentido inverso,

\[
\frac{(K_h+1)(L_h+1)}{n^2}\ \ge\ \frac{M_h}n-\Delta_n\ \ge\ u^2-2\Delta_n\ \ge\ 0.1736 .
\tag{5.6}
\]

Sea `x_h=sqrt((K_h+1)(L_h+1))/n`, de modo que `x_h>=0.41`. Como
`0<=2Delta_n<=u^2`, se tiene `sqrt(u^2-2Delta_n)>=u-2Delta_n/u>=u-5Delta_n`,
porque `(u-b/u)^2<=u^2-b` para `0<=b<=u^2` y `u>=0.44`. Luego

\[
x_h\ \ge\ \frac12-2r-\frac1n-5\Delta_n .
\tag{5.7}
\]

Por otra parte `Z_{n,h}<=x_h` y

\[
x_h-Z_{n,h}
=\frac{\sqrt{(K_h+1)(L_h+1)}-\sqrt{K_hL_h}}n
+\frac{\sqrt{K_hL_h}}{n(n+1)}
\le\frac{2n+1}{n^2x_h}+\frac1n
\le\frac9n ,
\tag{5.8}
\]

donde se racionalizó la diferencia de raíces y se usó `x_h>=0.41` y
`sqrt(K_hL_h)<=n`. De (5.7)–(5.8),

\[
Z_{n,h}\ \ge\ \frac12-2r-5\Delta_n-\frac{10}n .
\tag{5.9}
\]

Los dos intervalos de una 4-cadena son disjuntos en ambos ejes de rangos, luego
`K_-+K_+<=n-2` y `L_-+L_+<=n-2`; Cauchy–Schwarz da

\[
Z_{n,-}+Z_{n,+}
=\frac{\sqrt{K_-L_-}+\sqrt{K_+L_+}}{n+1}
\le\frac{n-2}{n+1}<1 .
\tag{5.10}
\]

Aplicando (5.9) al lado opuesto y (5.10) se obtiene la cota superior simétrica, lo
que prueba (5.3) con `r=R`.

Para (5.4): si `R>1/40`, entonces `50R>1`; si `Delta_n>1/100`, entonces
`50Delta_n>1/2`. En ambos casos el miembro derecho de (5.4) supera `1/2>=|Z-1/2|`,
pues `0<=Z_{n,h}<1`. Y si ambas hipótesis se cumplen, (5.4) se sigue de (5.3). `QED`

El Lema 5.1 es la forma puntual de la sección 5 de `NC-2D`, con dos diferencias que
se usan después: el radio de anclaje es una **variable aleatoria** en vez de un
umbral fijado a priori, y la desigualdad vale en todo \(\mathcal S_n\) sin
descomponer el espacio en suceso bueno y complemento.

## 6. Colas y momentos relativos

**Lema 6.1 (anclaje).** Para `2/n<=r<=1/8`,

\[
\Pr(R>r)\le4\exp\left(-\frac{r^2n}{16}\right),
\qquad
\mathbb E[R^2]\le\frac{65}n .
\tag{6.1}
\]

**Demostración.** Por monotonía, `{R>r}` está contenido en el complemento de
`A(r')`, donde `r'` es el mayor punto de la rejilla `<=r`, de modo que
`r'>=r-1/n>=r/2`. Para un bloque de `m'=floor(r'n)` filas y `m'` columnas, la
probabilidad de que la permutación no ponga ningún punto en la caja diagonal es
\(\binom{n-m'}{m'}/\binom n{m'}\le(1-m'/n)^{m'}\le e^{-m'^2/n}\), y `m'>=r'n/2`
para `r'n>=2`; la unión sobre las cuatro cajas da (la primera parte de) (6.1) con
exponente `r'^2n/4>=r^2n/16`. Para la segunda parte, con `R<=1/8`,

\[
\mathbb E[R^2]\le\left(\frac2n\right)^2
+\int_0^\infty 2s\cdot4e^{-s^2n/16}ds
+\frac1{64}\cdot4e^{-n/1024}
\le\frac4{n^2}+\frac{64}n+\frac1{16}e^{-n/1024}
\le\frac{65}n
\]

para `n>=n_1`. `QED`

Obsérvese que (6.1) **no** contiene factor logarítmico: el anclaje es, ya sin
condicionar, de escala raíz-`n`.

**Lema 6.2 (discrepancia).** Para todo `delta>0`,

\[
\Pr(\Delta_n>\delta)\le2n^4\exp\left(-\frac{n\delta^2}2\right),
\qquad 0\le\Delta_n\le1 .
\tag{6.2}
\]

Es el Lema 3.1 de `NC-2C` con `t=n delta`, unido sobre menos de `n^4` pares de
intervalos de rangos, tal como se usó en `NC-2D` §4.2. El factor `n^4` proviene de
la unión y no de la geometría del problema; su papel se analiza en la Proposición
7.4.

**Lema 6.3 (momentos relativos).** Sean

\[
L_n=\log\frac1{p_n}+\log n,
\qquad
L_n'=\log\frac1{p_n}+4\log n .
\]

Para todo `n>=n_1` con `n>=10^{40}`,

\[
\mathbb E_{\nu_n}[R^2]\le\frac{17L_n}n,
\qquad
\mathbb E_{\nu_n}[\Delta_n^2]\le\frac{3L_n'}n .
\tag{6.3}
\]

**Demostración.** Por (2.3)–(2.4) con `t^2=16L_n/n`, que cumple `2/n<=t<=1/8`
porque `L_n<=n/1024` en esta cola,

\[
\mathbb E_{\nu_n}[R^2]
\le t^2+\frac1{p_n}
\left[\int_t^\infty 2s\cdot4e^{-s^2n/16}ds
+\frac1{64}\cdot4e^{-n/1024}\right]
= t^2+\frac1{p_n}\left[\frac{64}ne^{-t^2n/16}+\frac1{16}e^{-n/1024}\right].
\]

Con `t^2n/16=L_n` se tiene `e^{-L_n}=p_n/n`, luego el primer corchete aporta
`64/n^2`. Para el segundo se usa la cota probada en `NC-2C` (4.14),

\[
p_n\ge\tfrac12n^{-(2n^{4/5}+4)},
\qquad\text{es decir}\qquad
\log\frac1{p_n}\le(2n^{4/5}+4)\log n+\log2,
\tag{6.4}
\]

que para `n>=10^{40}` es mucho menor que `n/2048`; por tanto
`e^{-n/1024}/p_n<=e^{-n/2048}<=1/n^2`. Sumando,
`E_{nu}[R^2]<=16L_n/n+65/n^2<=17L_n/n`, pues `L_n>=1`.

Para la discrepancia, (2.3)–(2.4) con `t^2=2L_n'/n` dan

\[
\mathbb E_{\nu_n}[\Delta_n^2]
\le t^2+\frac1{p_n}\int_t^\infty 2s\cdot2n^4e^{-ns^2/2}ds
= t^2+\frac{4n^3}{p_n}e^{-nt^2/2}
= \frac{2L_n'}n+\frac{4n^3}{p_n}\cdot\frac{p_n}{n^4}
= \frac{2L_n'}n+\frac4n ,
\]

y `L_n'>=4`. `QED`

El único ingrediente externo de la prueba es (6.4), y se usa **sólo** para absorber
dos términos de orden `n^{-2}`. El enunciado del teorema siguiente es monótono en
`p_n`: cualquier mejora futura de (6.4) lo mejora automáticamente.

## 7. Desigualdad relativa parametrizada por `|mathcal S_n|`

**Teorema 7.1.** Para ambos lados `h` y todo `n>=10^{40}`,

\[
\boxed{
\operatorname{Var}_{\nu_n}(q_{n,h})
\ \le\ 10^6\,n
\left[\log\frac{n!}{|\mathcal S_n|}+4\log n\right] }
\tag{7.1}
\]

o, en forma de conteo relativo con denominador `|mathcal S_n|`,

\[
\sum_{\pi\in\mathcal S_n}
\bigl(q_{n,h}(\pi)-\bar q_{n,h}\bigr)^2
\ \le\ 10^6\,n
\left[\log\frac{n!}{|\mathcal S_n|}+4\log n\right]|\mathcal S_n| .
\tag{7.2}
\]

**Demostración.** Por (2.1) con `c=(n+1)/2` y (1.1),

\[
\operatorname{Var}_{\nu_n}(q_{n,h})
\le(n+1)^2\,\mathbb E_{\nu_n}[(Z_{n,h}-1/2)^2].
\]

Por el Lema 5.1 y `(a+b)^2<=2a^2+2b^2` dos veces,

\[
\mathbb E_{\nu_n}[(Z_{n,h}-1/2)^2]
\le 2\cdot50^2\,\mathbb E_{\nu_n}[(R+\Delta_n)^2]+\frac{200}{n^2}
\le 10^4\bigl(\mathbb E_{\nu_n}[R^2]+\mathbb E_{\nu_n}[\Delta_n^2]\bigr)+\frac{200}{n^2}.
\]

Por el Lema 6.3 y `L_n<=L_n'`, el paréntesis es a lo sumo `20L_n'/n`. Luego

\[
\mathbb E_{\nu_n}[(Z_{n,h}-1/2)^2]
\le\frac{2\cdot10^5L_n'}n+\frac{200}{n^2}
\le\frac{2.1\cdot10^5L_n'}n ,
\]

y `(n+1)^2<=4n^2` da
`Var<=8.4*10^5 n L_n'<=10^6 n L_n'`. Finalmente
`L_n'=log(1/p_n)+4log n=log(n!/|mathcal S_n|)+4log n` por (1.3). La forma (7.2) es
(7.1) multiplicada por `|mathcal S_n|`. El resultado vale para ambos lados por el
Corolario 3.2 (y también directamente, porque `R` y `Delta_n` no dependen del
lado). `QED`

**Corolario 7.2 (consistencia con `NC-2D`; no es una mejora numérica).**
Sustituyendo (6.4) en (7.1),

\[
\operatorname{Var}_{\nu_n}(q_{n,h})
\le10^6n\left[(2n^{4/5}+8)\log n+1\right]
\le3\cdot10^6\,n^{9/5}\log n .
\tag{7.3}
\]

El exponente coincide con el de `NC-2D` (1.4), y la constante de (7.3) es **peor**
que la constante `2800` allí probada. El contenido nuevo de (7.1) no es numérico:
es la dependencia explícita en `|mathcal S_n|`, que `NC-2D` dejaba absorbida en una
elección fija de umbrales. La mejor cota explícita disponible en el nivel `n^{9/5}`
sigue siendo la de `NC-2D`.

**Corolario 7.3 (qué compra exactamente una mejora de `Pr(S)`).** Si
`p_n>=n^{-gamma}` con `gamma>=0` constante, entonces

\[
\operatorname{Var}_{\nu_n}(q_{n,h})\le10^6(\gamma+4)\,n\log n,
\qquad
\operatorname{Var}_{\nu_n}(\ell_h)\le\frac{C(\gamma)\log n}n .
\tag{7.4}
\]

Si `p_n>=c>0`, entonces
`Var_{nu_n}(q_{n,h})<=10^6 n[4log n+log(1/c)]`. En ningún caso este argumento
alcanza `O(n)`: incluso con `p_n=1` produce `Theta(n log n)`.

La segunda desigualdad de (7.4) usa la transferencia ya probada en `NC-2D`
(2.1)–(2.4): de `Var(q)<=C_q n` se sigue
`Var(ell_h|n,h,S)<=[1+(sqrt(C_q)+1/2)^2]/n`. Con `C_q=10^6(gamma+4)log n` esto da
`O(log n/n)`, que **no** basta para el objetivo `liminf T_n^h>0`: combinado con la
cota de numerador `3/(64,000,000 n)` de `NC-2A`+`NC-2C`, sólo produce
`T_n^h>=c/log n`, que tiende a cero.

**Proposición 7.4 (óptimo exacto de la familia auditada).** Considérese la familia
de cotas obtenidas del Lema 5.1 junto con las colas (6.1)–(6.2) y la división
controlada (2.3)–(2.4), parametrizada por el umbral `t` de la parte de
discrepancia. Su valor óptimo es

\[
\min_{t>0}\left[t^2+\frac{4n^3}{p_n}e^{-nt^2/2}\right]
=\frac2n\left[\log2+4\log n+\log\frac1{p_n}\right]+\frac2n ,
\tag{7.5}
\]

alcanzado en `e^{-nt^2/2}=p_n/(2n^4)`. En particular el óptimo es siempre al menos
`8(log n)/n`, cualquiera que sea `p_n<=1`, y la cota resultante para
`Var_{nu_n}(q_{n,h})` es siempre al menos de orden `n log n`.

**Demostración.** Derivando en `t` el corchete se obtiene
`2t=4n^3\cdot nt\,e^{-nt^2/2}/p_n`, es decir `e^{-nt^2/2}=p_n/(2n^4)`; el segundo
sumando vale entonces `4n^3/(2n^4)=2/n` y el primero
`(2/n)log(2n^4/p_n)`. La función es convexa en `t^2`, luego el punto crítico es el
mínimo. Como `p_n<=1`, el óptimo es `>=(2/n)\cdot4\log n`. `QED`

La Proposición 7.4 identifica el origen exacto del factor logarítmico residual: la
unión sobre menos de `n^4` pares de intervalos del Lema 6.2. El anclaje, por el
Lema 6.1, ya es libre de logaritmo. Esto es un enunciado sobre el óptimo de esta
familia explícita de cotas, no sobre todas las demostraciones posibles.

## 8. Reducción exacta de `NC2E-O3` a una discrepancia relativa

**Teorema 8.1 (reducción suficiente).** Supóngase que existen `C_\Delta<infinity` y
`n_2` tales que, para todo `n>=n_2`,

\[
\boxed{
\sum_{\pi\in\mathcal S_n}
\bigl(R(\pi)+\Delta_n(\pi)\bigr)^2
\ \le\ \frac{C_\Delta}n\,|\mathcal S_n| . }
\tag{8.1}
\]

Entonces, para ambos lados y todo `n>=max(n_1,n_2)`,

\[
\operatorname{Var}_{\nu_n}(q_{n,h})\le C_q\,n,
\qquad
C_q=4\cdot10^4\,C_\Delta+1 ,
\tag{8.2}
\]

es decir, `NC2E.1` con constantes explícitas; y en consecuencia valen las
consecuencias precomprometidas (4.1) y (4.2) de la nota firmada, con
`Var(ell_h|n,h,S)<=[1+(sqrt(C_q)+1/2)^2]/n` y `liminf T_n^h>0` en el canal
`sigma(M_h)`, `fixed-n`, `d=2`.

**Demostración.** (8.1) es exactamente `E_{nu_n}[(R+Delta_n)^2]<=C_\Delta/n`. Por
el Lema 5.1,

\[
\mathbb E_{\nu_n}[(Z_{n,h}-1/2)^2]
\le2\cdot50^2\frac{C_\Delta}n+\frac{200}{n^2},
\]

y multiplicando por `(n+1)^2<=4n^2`,

\[
\operatorname{Var}_{\nu_n}(q_{n,h})
\le4n^2\left[\frac{5000C_\Delta}n+\frac{200}{n^2}\right]
=2\cdot10^4C_\Delta\,n+800
\le(4\cdot10^4C_\Delta+1)\,n .
\]

La transferencia a `ell_h` y a `T_n^h` es la ya probada en `NC-2D` §2 y en la nota
firmada §4. `QED`

**Corolario 8.2 (par suficiente más fuerte y más legible).** (8.1) se sigue de la
conjunción de

- **(A)** `p_n>=c>0` para todo `n` grande, y
- **(B)** `E[\Delta_n^2]<=c_1/n` **incondicionalmente**,

con `C_\Delta=2(65+c_1)/c`, usando el Lema 6.1 y
`E_{nu_n}[X^2]<=E[X^2]/p_n`.

**Observaciones sobre las dos obligaciones.**

1. (B) es un enunciado **sin selector**: afirma que la discrepancia rectangular
   uniforme de una permutación uniforme tiene segundo momento de orden `1/n`, sin
   el factor `log n` que introduce la unión del Lema 6.2. Es auditable de forma
   completamente independiente de `S`, y su ruta natural —encadenamiento sobre la
   clase de rectángulos de rangos, de dimensión de Vapnik–Chervonenkis finita, con
   incrementos concentrados— no está desarrollada en este repositorio. Aquí no se
   afirma que (B) sea cierto: se afirma que es lo que falta.
2. (A) es mucho más fuerte que todo lo probado: la mejor cota disponible es (6.4),
   `p_n>=exp(-O(n^{4/5}log n))`.
3. (8.1) es **estrictamente más débil** que la conjunción (A)+(B): no exige que
   `p_n` esté acotado inferiormente, sino sólo que la selección no infle el segundo
   momento de la discrepancia más allá de su escala incondicional. Ésa es la
   obligación literal que falta, y es una desigualdad relativa con denominador
   `|mathcal S_n|`, del tipo exigido por el test de terminado.
4. La identidad (2.7) explica por qué la discrepancia es el único objeto que queda:
   sobre `S`, la forma `q_{n,h}^2` está determinada por el conteo `M_h` salvo
   `n^2\Delta_n+2n+1`. Controlar `Delta_n` en `L^2(nu_n)` a escala `n^{-1/2}`
   controla simultáneamente la geometría del ganador y su conteo.

**Lo que el Teorema 8.1 no dice.** No dice que (8.1) sea necesaria para `NC2E.1`;
no se ha probado ninguna implicación recíproca. Tampoco dice que (8.1) sea cierta.

## 9. Rutas auditadas y sus obligaciones exactas

### 9.1 Cadena de switchings y desigualdad de Poincaré

Sea `P` el núcleo sobre \(\mathcal S_n\) que, desde `pi`, elige una transposición
`tau` uniforme entre las \(\binom n2\) posibles y se mueve a `tau pi` si
`tau pi in mathcal S_n`, quedándose quieto en caso contrario. `P` es simétrico
(`P(pi,sigma)=P(sigma,pi)`), luego **reversible respecto de \(\nu_n\)**; esto es
inmediato y no requiere hipótesis. Si `P` es irreducible sobre \(\mathcal S_n\) con
gap espectral `lambda_n>0`, la desigualdad de Poincaré da

\[
\operatorname{Var}_{\nu_n}(q_{n,h})
\le\frac1{\lambda_n}\,
\mathcal E(q_{n,h},q_{n,h}),
\qquad
\mathcal E(q,q)=\frac1{2\binom n2}
\mathbb E_{\nu_n}\!\!\sum_{\tau}
\bigl(q(\tau\pi)-q(\pi)\bigr)^2
\mathbf 1\{\tau\pi\in\mathcal S_n\}.
\tag{9.1}
\]

Para obtener `NC2E.1` por esta vía haría falta demostrar las **tres** obligaciones:

1. **conectividad**: \(\mathcal S_n\) es conexo bajo transposiciones;
2. **gap**: `lambda_n>=c/n` (la escala del paseo de transposiciones sobre
   \(\mathfrak S_n\) completo; restringir a un subconjunto puede degradarla
   arbitrariamente);
3. **energía**: `E(q,q)<=C`, es decir, cambio cuadrático medio `O(1)` de
   `q_{n,h}` bajo una transposición que permanece en \(\mathcal S_n\).

Ninguna de las tres está probada. La obligación 3 es exactamente la sensibilidad
del ganador discutida en §4, y el Corolario 4.2 muestra que no puede deducirse del
soporte. Ninguna de las tres se supone en esta nota.

### 9.2 Pares intercambiables y Efron–Stein

El par `(pi,tau pi)` con `tau` uniforme y `pi ~ nu_n` es intercambiable **sólo si**
se condiciona a `tau pi in mathcal S_n`, y entonces su núcleo es el de §9.1. La
desigualdad de Efron–Stein para coordenadas independientes **no es aplicable**:
\(\nu_n\) no es una medida producto ni el condicionamiento por `S` deja
independientes las coordenadas de la permutación. Aplicarla exigiría construir
previamente el núcleo o la filtración correspondiente, con las mismas tres
obligaciones de §9.1. La nota firmada prohíbe expresamente ese atajo y aquí no se
toma.

### 9.3 Inyección de multiplicidad controlada

Cerraría `NC2E-O3` una aplicación
`phi:mathcal S_n^{ext} -> mathcal S_n^{cen}` desde los niveles extremos de `q`
hacia los centrales, con multiplicidad acotada uniformemente y ganancia por nivel;
transformaría (2.2) en una suma telescópica acotada. No existe en el repositorio
ninguna inyección de ese tipo, y el Corolario 4.2 muestra que no puede construirse
sólo a partir del soporte. No se ha construido aquí.

### 9.4 Cola relativa integrable

`NC-2D` (7.2) formuló la cola relativa subgaussiana centrada en `n/2` como
condición suficiente más fuerte que el objetivo. El Teorema 8.1 la sustituye por
una condición **más débil y de segundo momento**: (8.1). En ese sentido la ruta de
cola queda subsumida.

### 9.5 Mejora de `Pr(S)`

La Proposición 7.4 calcula el techo exacto de esta ruta dentro de la familia
auditada: incluso `p_n=1` deja `Theta(n log n)`, de modo que **una mejora de
`Pr(S)` no alcanza por sí sola la escala requerida**. Conforme a la lista cerrada
de §5 de la nota firmada, que autoriza esa ruta auxiliar sólo si alcanza por sí
misma la escala necesaria, no se desarrolla aquí ninguna mejora de la cota (6.4) y
no se altera ningún token de `NC-2C`. Se corrige, eso sí, la lectura de `NC-2D` §7
según la cual una cota marginal más fuerte para `Pr(S)` sería «otra ruta
suficiente»: dentro de la maquinaria auditada lo es sólo en conjunción con (B) del
Corolario 8.2.

## 10. Separaciones obligatorias

**10.1 Cota demostrada, escala requerida y varianza real.** Lo demostrado aquí es
(7.1): una **cota superior** relativa. La escala requerida por `NC2E-O3` es `C_q n`.
Con el `p_n` hoy disponible, (7.1) da `O(n^{9/5}log n)` (Corolario 7.2), y el
cociente entre lo demostrado y lo requerido sigue siendo `n^{4/5}log n`. Nada de
esto afirma que la varianza real de `q_{n,h}` bajo \(\nu_n\) tenga ese orden: la
varianza real podría ser `Theta(n)`, menor, o no tener un orden único a lo largo de
`n`. La identidad (2.7) sugiere heurísticamente la escala `n`, pero una sugerencia
heurística no es una cota y no se usa en ninguna implicación.

**10.2 Escala `O(n)` frente a teorema central del límite.** `NC2E.1` es un enunciado
de **orden de varianza** y nada más. Ni (7.1) ni (8.2) afirmarían, si se probasen,
convergencia en distribución, normalidad asintótica, existencia de una constante
asintótica de varianza, ni colas subgaussianas. La expresión «escala CLT» de la nota
firmada es una descripción de orden, no un teorema límite.

**10.3 Bloqueo frente a refutación.** No se ha refutado `NC2E.1`. El fallo de las
rutas auditadas no es una refutación, y una eventual refutación de `NC2E.1` tampoco
implicaría `liminf T_n^h=0`: numerador y denominador podrían requerir un análisis
conjunto distinto.

## 11. Techo de afirmación

Esta nota demuestra: la Proposición 3.1 y el Corolario 3.2 (simetrías exactas y
cierre exacto de la obligación de ambos lados), la Proposición 4.1 y el Corolario
4.2 (dos testigos y el no-go de soporte), el Lema 5.1 (cota puntual determinista en
\(\mathcal S_n\)), los Lemas 6.1–6.3, el Teorema 7.1 con (7.2), los Corolarios
7.2–7.3, la Proposición 7.4 y el Teorema 8.1 con el Corolario 8.2.

No demuestra ni refuta:

- `Var_{nu_n}(q_{n,h})=O(n)` (`NC2E-O3`);
- `Var(ell_h|n,h,S)=O(1/n)`;
- `liminf T_n^h>0`;
- (8.1), (A) ni (B);
- ninguna afirmación para canales enriquecidos, poset completo, horizontes, escala
  absoluta o `d>=3`;
- novedad o prioridad bibliográfica.

No se cambió el selector, `Q_3`, `S`, `M_h`, `(K_h,L_h)`, `ell_h` ni la abstención.
No se tocó el sello, no se usaron semillas y no se modificó la PR #7. No se
consultaron los tamaños sellados `n in {64,96,128}` para elegir constantes ni ruta
de prueba. No se ejecutó ni creó código, simulación, dato o artefacto numérico.

## 12. Terminal

Se obtuvo una desigualdad relativa nueva con denominador `|mathcal S_n|`, una
identidad determinista exacta que liga forma, conteo y discrepancia, el cierre
exacto de la dualidad de lados, y una reducción de `NC2E-O3` a una única obligación
relativa explícita. No se probó ni se refutó `NC2E.1`. El terminal único es:

```text
NC2E_TERMINAL = NC2E_PARTIAL_RELATIVE_VARIANCE_REDUCTION
NC2E_SIDE_SYMMETRY_GROUP = KLEIN_FOUR_PROVED_MEASURE_PRESERVING
NC2E_BOTH_SIDES = CLOSED_BY_EXACT_BIJECTION
NC2E_EXACT_SHAPE_COUNT_IDENTITY = q^2 = n*M + n^2*theta - (K+L+1), |theta| <= Delta_n
NC2E_POINTWISE_ANCHOR_LEMMA = PROVED_ON_ALL_OF_S
NC2E_RELATIVE_VARIANCE_BOUND = 10^6*n*(log(n!/|S_n|)+4*log(n))
NC2E_RECOVERS_NC2D_ORDER = YES_WITH_WORSE_CONSTANT
NC2E_BEST_EXPLICIT_CONSTANT_AT_EXPONENT_9_5 = NC2D_2800
NC2E_FAMILY_OPTIMUM = THETA(n*(log(1/Pr(S))+log n))
NC2E_FAMILY_FLOOR_AT_PR_S_EQUAL_1 = ORDER_N_LOG_N
NC2E_SUFFICIENT_REDUCTION = RELATIVE_MEAN_SQUARE_DISCREPANCY_SUM_(R+Delta)^2 <= C*|S_n|/n
NC2E_SUFFICIENT_PAIR = PR_S_BOUNDED_BELOW_AND_UNCONDITIONAL_E[Delta^2]=O(1/n)
NC2E_MISSING_OBJECT_A = LOWER_BOUND_ON_PR_S_BEYOND_NC2C
NC2E_MISSING_OBJECT_B = UNCONDITIONAL_CHAINING_BOUND_E[Delta_n^2]=O(1/n)
NC2E_PR_S_ROUTE_CEILING = INSUFFICIENT_ALONE
NC2E_POINCARE_ROUTE = REVERSIBILITY_PROVED_CONNECTIVITY_GAP_ENERGY_OPEN
NC2E_EFRON_STEIN = NOT_APPLICABLE_NO_PRODUCT_STRUCTURE
NC2E_SUPPORT_ONLY_ARGUMENTS = PROVED_INSUFFICIENT
NC2E_O3 = OPEN
NC2E_CLT_CLAIMED = NO
NC2E_LIMINF_T_N = NOT_PROVED
NC2E_NEW_DATA = NO
NC2E_NEW_CODE = NO
NC2E_SEEDS_USED = NONE
NC2E_SEAL_TOUCHED = NO
NC2E_PR7_MODIFIED = NO
NOVELTY_CERTIFIED = NO
```
