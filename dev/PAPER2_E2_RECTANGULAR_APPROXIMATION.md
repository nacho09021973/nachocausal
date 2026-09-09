# Paper II: E2 para la caja transformada, orden inducido y fronteras

STATUS: DEMOSTRACION_PROPUESTA / REVISION_INDEPENDIENTE_PENDIENTE
DATE: 2026-09-08
CAPA: dev/. No es contrato, preregistro ni resultado sellado.

Esta nota sustituye el argumento insuficiente basado en area pequena por una
construccion de curvas y aproximaciones. Conserva la caja coordenada. El alcance
es un compacto de **un solo bloque**, separado del horizonte y de r = 0; no se
afirma uniformidad al retirar esos cortes. La caja congelada completa, que cruza
el horizonte, sigue fuera del resultado.

Dependencias locales: `PAPER2_DOUBLE_NULL_REDUCTION.md`, Teoremas 1-2, y
`PAPER2_DEUSCHEL_ZEITOUNI_APPLICABILITY.md`. Insumo probabilistico externo:
Deuschel--Zeitouni (1995), Teorema 2(i), p. 855, bajo sus hipotesis originales
(A1)-(A2). PDF local:
`biblioteca/Deuschel_Zeitouni_1995_AnnProb_23_852_Limiting_Curves_for_IID_Records.pdf`.
[Fuente primaria](https://projecteuclid.org/journals/annals-of-probability/volume-23/issue-2/Limiting-Curves-for-IID-Records/10.1214/aop/1176988293.full).
Se inspeccionaron las imagenes de pp. 855 y 863; no se usa el OCR para formulas.
Las extensiones necesarias se argumentan abajo, no se atribuyen a los Remarks.

## 1. El funcional del orden inducido

Sea B un rectangulo ambiente fijo. Para una intensidad base a >= 0, definimos

\[
 V(a)=\sup_{\gamma\in\Gamma_B}
       \int\sqrt{a(\gamma(u))\dot v(u)\dot w(u)}\,du,
 \qquad
 \Gamma_B=\{\gamma=(v,w)\text{ absolutamente continua}:\dot v,\dot w\geq0\}.
 \tag{1}
\]

Los extremos son libres. Se pueden completar hasta las esquinas de B; para
pesos no negativos esto no disminuye el supremo. Para un soporte G usamos
`a = q 1_G`. **No se exige gamma contenida en G**: los tramos fuera de G tienen
peso cero. Esto representa los saltos permitidos por el orden inducido.
En cambio, escribiremos

\[
 I_q(G)=\sup_{\gamma\in\Gamma_B,\ \gamma\subset G}
       \int\sqrt{q(\gamma)\dot v\dot w}\,du.                 \tag{2}
\]

No identificamos (1) y (2) para conjuntos generales. Tampoco afirmamos un
teorema para toda densidad medible: cambiar valores sobre una curva creciente
de area cero puede cambiar (1). Abajo fijamos la traza continua de q en la caja
cerrada y demostramos que es aproximable desde su interior. Para las funciones
escalonadas, las convenciones en las lineas de la rejilla son irrelevantes:
una curva sobre una linea horizontal o vertical tiene producto de derivadas cero
casi en todas partes en ese conjunto.

El contraejemplo de la franja vertical refuta el argumento anterior para (2).
Con (1), el puente a traves de la franja esta permitido; su coste perdido es
acotable por Cauchy--Schwarz, no por el area de un conjunto arbitrario.

## 2. Geometria exacta y extension exterior de la densidad

Fijemos `D = [t0,t1] x [r_-,r_+]`, con `t0<t1` y `r_-<r_+`, dentro de un
bloque y un punto fijo x en D.
La caja puede ser un corte compacto auxiliar de la caja original; no cambia el
generador ni autoriza retirar el corte. Sea `F = Phi(D) cap {v>=v_x,w>=w_x}`.
Usamos la clausura, sin cambiar el proceso puntual casi seguramente.

Escribimos `f=1-r_S/r`, `R=r+2r_S log(|r-r_S|/r_S)`, `psi=r+R` y `h=psi^{-1}`
en el bloque elegido. La coordenada temporal inversa es T:

| Bloque | Variable radial z | T(v,w) | Intervalo radial [a,b] |
|---|---|---|---|
| Exterior, w=U | d=v-w | v-h(d) | [psi(r_-),psi(r_+)] |
| Interior, w=-U | s=v+w | v-h(s) | [psi(r_+),psi(r_-)] |

En ambos casos, F viene dado exactamente por las seis desigualdades

\[
 z-a\geq0,\quad b-z\geq0,\quad T-t_0\geq0,\quad t_1-T\geq0,
 \quad v-v_x\geq0,\quad w-w_x\geq0.                       \tag{3}
\]

Extendemos primero el intervalo radial a otro compacto ligeramente mayor del
**mismo bloque**. En la banda nula correspondiente siguen definidas T y

\[
 q(v,w)=|f(h(z))|/2,\qquad 0<q_*\leq q\leq M.             \tag{4}
\]

Es la misma formula geometrica en un entorno exterior real de F. No se exige
que las aproximaciones exteriores esten contenidas en la clausura de F.
Fuera de esta banda no hace falta evaluar h: los pesos utilizados valen cero.
Elegimos B suficientemente grande para contener F y todas las ampliaciones
pequenas de (3). q y sqrt(q) son Lipschitz en el compacto relevante.

La identidad `h'=f/2` da

\[
 (T_v,T_w)=
 \begin{cases}(1-f/2,f/2)&\text{exterior},\\
 (1-f/2,-f/2)&\text{interior}.
 \end{cases}
 \qquad T_v,T_w\geq m>0.                                 \tag{5}
\]

Las constantes m, M y las cotas Lipschitz dependen del compacto. En particular,
no se mantienen uniformes al acercarse al horizonte.

## 3. Accesibilidad: cuando se puede volver al funcional intrinseco

Denotemos por F_{+eta} el conjunto que sustituye cada `g>=0` de (3) por
`g>=-eta`, y por F_{-eta} el que exige `g>=eta`. Para eta pequeno, cada uno
permanece en la banda extendida.

**Lema de conexion.** Dos puntos comparables p <= q de cualquiera de estos
conjuntos pueden unirse por su segmento recto, contenido en el mismo conjunto.

En efecto, z es afin y conserva sus dos cotas en el segmento. Las coordenadas
v,w crecen; por (5), T tambien crece, por lo que permanece entre sus valores
en p y q. Las dos restricciones de futuro se conservan. Esta prueba no afirma
que todo el rectangulo de orden [p,q] este contenido en F.

**Consecuencia, con prueba para huecos multiples:**

\[
 V(q1_{F_{\pm\eta}})=I_q(F_{\pm\eta}),\qquad
 V(q1_F)=I_q(F).                                          \tag{6}
\]

Parametrizamos una curva ambiente por s=v+w, suprimiendo tramos constantes.
Sus coordenadas son 1-Lipschitz. El conjunto K de parametros donde visita el
soporte cerrado es compacto. Si no tiene visitas, su accion es cero; si solo
tiene una, tambien. En otro caso, quitamos lo anterior a la primera visita y
lo posterior a la ultima. Cada componente abierta del complemento de K tiene
extremos en el soporte y comparables. Reemplazamos alli por el segmento del
lema, parametrizado por el mismo s.

Incluso para infinitos huecos, la curva resultante es 1-Lipschitz en cada
coordenada: es monotona y la suma de sus coordenadas sigue siendo s. Coincide
con la original en K y sus derivadas coinciden casi en todas partes en K
(aplicar diferenciabilidad en los puntos de densidad de K a su diferencia).
Conserva toda la accion que antes se contaba y anade accion no negativa en los
huecos. Esto prueba la desigualdad no trivial de (6).

El mismo lema permite anteponer el segmento de x al primer punto de una curva
en F. Por tanto `I_q(F)` tambien es el supremo sobre curvas **desde x**, con
extremo final libre, contenidas en F. Esta identificacion se demuestra para F;
no se impone a las uniones rectangulares aproximantes, que pueden desconectarse.

## 4. Estimaciones de curvas en cada frontera

Sean W_v,W_w cotas fijas para las variaciones totales de v,w en B y sus pequenas
deformaciones. Para una curva monotona y un conjunto de parametros E:

\[
 \int_E\sqrt{q\dot v\dot w}
 \leq\sqrt M\sqrt{\int_E\dot v\int_E\dot w}.               \tag{7}
\]

**Fronteras nulas del futuro.** En una franja `c<=v<=c+ell`, la primera
integral de derivada es <=ell; se pierde como mucho `sqrt(M ell W_w)`.
Para una franja de w se intercambian los indices. Esto incluye tramos sobre
la propia frontera, que no aportan accion.

**Dos fronteras temporales.** Por (5), `dT >= m(dv+dw)` sobre curvas futuras.
En una franja temporal de anchura ell, la variacion de s es <=ell/m. Como
`sqrt(dv dw) <= (dv+dw)/2`, la perdida es <=`sqrt(M) ell/(2m)`.

**Dos fronteras radiales interiores.** Son `s=a,b`. Una franja de anchura ell
en s cuesta como mucho `sqrt(M) ell/2` por la misma desigualdad.

**Dos fronteras radiales exteriores.** Son `d=a,b`, de pendiente positiva.
No se les aplica una cota por area ni se descartan. Se usa la siguiente
deformacion explicita, que retiene la accion de curvas pegadas a esas paredes.

## 5. Deformacion F_{+eta} -> F_{-eta}

### Exterior

Para una curva en F_{+eta}, definimos

\[
 c_\eta(d)=\min\{b-\eta,\max\{a+\eta,d\}\},\qquad
 P_\eta(v,w)=\left(\frac{s+c_\eta(d)}2,
                       \frac{s-c_\eta(d)}2\right).         \tag{8}
\]

Se requiere `2eta<b-a`. Como `d` estaba en `[a-eta,b+eta]`, cada coordenada
se mueve como mucho eta. Para derivadas casi en todas partes,

\[
 |(c_\eta\circ d)'|\leq|d'|\leq s',\qquad
 \dot v_\eta,\dot w_\eta\geq0,\qquad
 \dot v_\eta\dot w_\eta
   =\frac{(s')^2-((c_\eta\circ d)')^2}{4}
   \geq\frac{(s')^2-(d')^2}{4}=\dot v\dot w.               \tag{9}
\]

Esto vale tambien en los puntos de quiebre del recorte por la regla de cadena
para funciones Lipschitz. La curva conserva accesibilidad futura.

Sea H>=1 una cota Lipschitz de T en norma infinito. Antes de aplicar (8),
retenemos solo el intervalo de parametros donde

\[
 t_0+(H+1)\eta\leq T\leq t_1-(H+1)\eta,
 \qquad v\geq v_x+2\eta,\quad w\geq w_x+2\eta.            \tag{10}
\]

Es un intervalo, posiblemente vacio, porque T,v,w son monotonas. Los tramos
descartados estan en dos franjas temporales de anchura `(H+2)eta` y dos nulas
de anchura `3eta`. Por (7) y las cotas de la seccion 4, su accion es <=C sqrt(eta)
para `eta<=1`. Tras (8), (10) garantiza las cuatro restricciones temporales y
nulas de F_{-eta}; las radiales las garantiza el recorte.

Si K_q es una cota Lipschitz de sqrt(q), (9) implica para la porcion retenida

\[
 \mathcal A_q(P_\eta\gamma)
 \geq \mathcal A_q(\gamma)-K_q\eta\sqrt{W_vW_w}.           \tag{11}
\]

Se obtiene usando primero (9), con el coeficiente no negativo sqrt(q(P_eta gamma)),
y luego comparando las raices de q en puntos a distancia <=eta; la integral
del producto original se acota por
Cauchy--Schwarz. No hace falta controlar derivadas de la curva original.
Si el intervalo retenido es vacio, toda su accion ya estaba en las franjas
descartadas y la misma cota global vale con accion resultante cero.

### Interior

No hay paredes radiales temporales que desplazar. Retenemos el intervalo donde

\[
 a+\eta\leq s\leq b-\eta,\quad
 t_0+\eta\leq T\leq t_1-\eta,\quad
 v\geq v_x+\eta,\quad w\geq w_x+\eta.                    \tag{12}
\]

Es un intervalo por monotonia de s,T,v,w. Solo se eliminan dos franjas
radiales, dos temporales y dos nulas, todas de anchura `2eta`. Las estimaciones
anteriores dan de nuevo perdida <=C sqrt(eta). La curva retenida ya esta en
F_{-eta}.

**Conclusion cuantitativa en ambos bloques**, usando tambien (6):

\[
 0\leq V(q1_{F_{+\eta}})-V(q1_{F_{-\eta}})
       \leq C\sqrt\eta.                                  \tag{13}
\]

El supremo del conjunto sin curvas se toma como cero. Las constantes son
uniformes sobre las curvas, pero dependen de la caja compacta fija. Esta es la
estimacion de frontera que faltaba; no es semicontinuidad invocada sin prueba.
Mas explicitamente, antes de absorber los terminos O(eta), la cota exterior es

\[
 \frac{\sqrt M(H+2)}m\eta
 +\sqrt{3M\eta}(\sqrt{W_v}+\sqrt{W_w})
 +K_q\eta\sqrt{W_vW_w},
\]

y la interior es

\[
 2\sqrt M(1+1/m)\eta
 +\sqrt{2M\eta}(\sqrt{W_v}+\sqrt{W_w}).
\]

## 6. Aproximaciones rectangulares concretas

Fijamos una rejilla diadica de B con diametro en norma infinito <=h. Usamos
las clausuras de sus celdas Q para decidir la inclusion:

\[
 R_h^- =\bigcup_{Q\subset F}Q,\qquad
 R_h^+ =\bigcup_{Q\cap F\ne\varnothing}Q.                 \tag{14}
\]

Las interiores crecen y las exteriores decrecen al refinar. Sea H_0>=1 una
cota Lipschitz comun de las seis funciones de (3), en el entorno elegido.
Con `eta=2H_0 h` y h suficientemente pequeno,

\[
 F_{-\eta}\subset R_h^-\subset F\subset R_h^+
       \subset F_{+\eta}.                                \tag{15}
\]

Para la primera inclusion, toda celda que contiene un punto con margen eta
permanece en F: cada desigualdad cambia como mucho H_0 h. Para la ultima,
todo punto de una celda exterior esta a distancia <=h de algun punto de F.
En particular `R_h^+ subset {dist_infty(.,F)<=h}`, un **entorno exterior**;
q esta definida alli por (4).

Para tener densidades exactamente constantes por celda, definimos

\[
 a_h^-|_Q=\begin{cases}\inf_Qq&Q\subset F,\\0&\text{resto},\end{cases}
 \qquad
 a_h^+|_Q=\begin{cases}\sup_Qq&Q\cap F\ne\varnothing,\\0&\text{resto}.
 \end{cases}                                             \tag{16}
\]

Las celdas activas estan en el entorno donde existe q. Se toma cualquier
convencion disjunta en las aristas para las densidades. El emparedado puntual
vale fuera de esas aristas, suficiente para el acoplamiento Poisson; las
aristas tampoco aportan accion en (1).

La oscilacion de sqrt(q) en una celda es O(h), y
`integral sqrt(v' w') <= sqrt(W_v W_w)`. Por tanto la sustitucion por infimos o
supremos cambia V a lo sumo C h. Combinando (13)-(16),

\[
 a_h^-\leq q1_F\leq a_h^+\quad\text{casi por doquier},
 \qquad
 V(a_h^-)\longrightarrow V(q1_F)\longleftarrow V(a_h^+),
 \qquad V(a_h^+)-V(a_h^-)\leq C\sqrt h.                  \tag{17}
\]

La accesibilidad usada en esta prueba es la del orden inducido: se permiten
puentes de peso cero en R_h^-. Ademas, (8)-(12) construyen para cualquier curva
casi optima de F una curva continua dentro de F_{-eta}, y por tanto de R_h^-,
con perdida controlada. No se deduce conectividad global de R_h^- de su area.

## 7. Por que las cadenas rectangulares tienen precisamente el limite (1)

Demostramos la pieza finita necesaria: para cualquier peso a no negativo y
constante en las celdas de una rejilla finita de B, si L_rho(a) es la altura
del Poisson de intensidad `rho a dv dw` en el orden inducido, entonces

\[
 L_\rho(a)/\sqrt\rho\ \xrightarrow{\mathbb P}\ 2V(a).
                                                               \tag{18}
\]

**Insumo liso y poissonizacion.** Para a suave y estrictamente positiva en B,
normalizamos por `m_a=integral_B a` y reescalamos B afinmente al cuadrado.
DZ 2(i) da `L_n/sqrt(n) -> 2V(a)/sqrt(m_a)`. Condicionalmente a
`N~Poisson(rho m_a)`, la nube son N puntos i.i.d. de esa densidad. Dado un
umbral n0, la probabilidad de desviacion se acota por `P(N<n0)` mas el supremo
de las probabilidades de desviacion para `n>=n0`; ambos tienden a cero haciendo
primero rho tender a infinito y despues n0. Finalmente `N/rho -> m_a` en
probabilidad. Esto prueba la version lisa Poisson de (18), sin atribuir la
poissonizacion al articulo. Para intensidad constante c en un rectangulo Q,
resulta el limite `2 sqrt(c area(Q))`.
La forma parametrica de DZ, p. 863, coincide con (1): al completar el grafico
monotono y parametrizar por v+w, los saltos verticales y las partes singulares
aportan cero al producto de derivadas.

**Cota inferior por concatenacion.** Fijamos una curva cuya accion este a
distancia epsilon de V(a). Visita un numero finito de interiores de celdas,
cada uno en un unico intervalo de parametros; los tramos sobre lineas de
rejilla tienen accion cero. En una celda de peso c, con puntos de entrada p
y salida q, Cauchy--Schwarz acota su accion por
`sqrt(c (q_v-p_v)(q_w-p_w))`. Si ambos incrementos son positivos, el rectangulo
entre p y q esta en la clausura de esa celda. Lo recortamos ligeramente por
sus cuatro lados para situarlo estrictamente dentro, con perdida arbitrariamente
pequena de esa expresion; si un incremento es cero su contribucion era cero.

Todos los puntos de cada rectangulo recortado preceden a todos los del
siguiente: la esquina superior del primero es <= la inferior del siguiente
antes del recorte, y el recorte da margen. Esto sigue siendo cierto al saltar
celdas con peso cero. Concatenamos sus cadenas maximas. El limite homogeneo
aplicado a los finitemente muchos rectangulos, con una union finita de eventos
de error, da la cota inferior en probabilidad `2(V(a)-epsilon)` con una perdida
de recorte arbitraria. No se exige que los segmentos entre cadenas queden en
el soporte.

**Cota superior por mayorante liso y franjas nulas.** Para cada celda cerrada
Q de peso c_Q>0 tomamos una funcion suave `chi_Q,delta` entre 0 y 1, igual a
1 en Q y cero fuera de su engrosamiento por delta. Puede construirse como
producto de dos funciones meseta unidimensionales. Sea

`e(u)=exp(-1/u)` si `u>0`, y cero en otro caso, y
`S(u)=e(u)/(e(u)+e(1-u))`. Para un intervalo `[l,r]`, el factor explicito es
`S((z-l+delta)/delta) S((r+delta-z)/delta)`; el producto de los factores de
las dos coordenadas da chi. Definimos

\[
 b_\delta=\delta+\sum_Q c_Q\chi_{Q,\delta}.
\]

Es suave y estrictamente positiva en B y mayoriza a a casi por doquier. Fuera
de franjas de anchura 2delta alrededor de las finitemente muchas lineas de la
rejilla, `b_delta=a+delta`. La densidad esta acotada uniformemente en delta
(por ejemplo por `1+sum_Q c_Q`, para delta<=1). Usando (7) en cada franja
vertical u horizontal, y `sqrt(a+delta)-sqrt(a)<=sqrt(delta)` fuera de ellas,
obtenemos

\[
 0\leq V(b_\delta)-V(a)\leq C_{\rm rejilla}\sqrt\delta.
\]

Acoplamos los procesos por adicion de puntos y aplicamos la version lisa de
(18) a b_delta. Primero rho tiende a infinito con delta fijo; despues delta
tiende a cero. Junto con la cota inferior, esto demuestra (18). El numero de
lineas es fijo en este paso: no se afirma una cota uniforme al refinar la rejilla.

**Emparedado final.** En un Poisson marcado comun, (16) permite realizar

\[
 L_\rho(a_h^-)\leq L_\rho(q1_F)\leq L_\rho(a_h^+).
\]

Para cada tolerancia, elegimos primero h fijo suficientemente pequeno usando
(17), y despues hacemos rho tender a infinito usando (18). Se obtiene

\[
 \boxed{L_\rho(q1_F)/\sqrt\rho
       \xrightarrow{\mathbb P}2V(q1_F)=2I_q(F).}          \tag{19}
\]

No se intercambian limites, no se necesita concentracion uniforme de curvas y
no se infiere una tasa probabilistica en rho de la cota determinista O(sqrt(h)).
Un punto inicial fijo x anadido a la nube cambia el conteo de vertices a lo
sumo en uno. Esto no demuestra uniformidad sobre anclas seleccionadas de la
nube ni sobre cortes que dependan de rho.

## 8. Geometria medida y techo de la conclusion

Con (4) y `ds^2=|f|dv dw`, la identificacion que ahora tiene justificacion es

\[
 2V(q1_F)=\sqrt2\sup_{\gamma:x\to F,\ \gamma\subset F}
                         \int\sqrt{|f|\,dv\,dw}
          =\sqrt2\,\tau_F(x),
 \qquad L_\rho/\sqrt{2\rho}\xrightarrow{\mathbb P}\tau_F(x). \tag{20}
\]

tau_F es tiempo propio maximo **restringido a la caja**, con extremo libre.
El lema de conexion garantiza existencia de curvas en F entre puntos
comparables; no afirma que el maximizador lorentziano del espacio ambiente
entre esos puntos permanezca en F. No se sustituye tau_F por una distancia
ambiente sin otra prueba.

Para un intervalo curvo, rectangularidad nula no implica densidad constante
ni `A=tau^2/2`. Si `R_2=L^2/N` y `N/rho -> A>0`, la consecuencia de una ley de
altura aplicable es `R_2 -> 2 tau^2/A`; el valor 4 requiere ademas la relacion
plana `A=tau^2/2`. Un diamante queda solo como posible referencia posterior.

Esta es una demostracion propuesta, revisable paso a paso, del E2 compacto y
de las piezas probabilisticas que necesita su emparedado. No se cambia la
clasificacion sellada del proyecto ni se da por superada la revision
independiente. El cruce de horizonte, la retirada uniforme de los cortes y
las anclas aleatorias seleccionadas quedan fuera del enunciado.
