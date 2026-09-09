# Paper II (1+1D): umbral finito, carta regular y control del horizonte

DATE: 2026-09-09
STATUS: RESULTADOS_DETERMINISTAS_CON_PRUEBA / LIMITE_CON_PRUEBA_PROPUESTA
REVIEW: REVISION_MATEMATICA_INDEPENDIENTE_PENDIENTE
CAPA: dev/. No es contrato, resultado sellado ni detector order-only.

Dependencias: [descomposición finita](PAPER2_HORIZON_O4_FINITE_DECOMPOSITION.md),
[reducción por bloques](PAPER2_DOUBLE_NULL_REDUCTION.md), Teorema 1.
La [propuesta E2](PAPER2_E2_RECTANGULAR_APPROXIMATION.md) sigue pendiente de
revisión. Las secciones 6-7 aíslan el insumo K; el apéndice A aporta una
demostración propuesta de K, incluidos los semiplanos de umbral. La cadena
analítica completa queda escrita, pero no se presenta como resultado revisado.

## 1. Identidades finitas, incluidos los lados vacíos

Trabajamos con puntos distintos fuera del horizonte y el orden exacto de O4.
Sea H la altura (número de vértices), con H(vacío)=0. Definimos

\[
 E_\rho(s)=H(P_\rho^{ext}\cap\{v\le s\}),\qquad
 I_\rho(s)=H(P_\rho^{int}\cap\{v\ge s\}).
 \tag{1}
\]

Son respectivamente creciente y decreciente. Coinciden con los máximos de las
longitudes ancladas de la nota anterior: v es monótona sobre cada cadena.
Sea

\[
 A_\rho=\{s:P_\rho^{ext}\cap\{v\le s\}\ne\varnothing,\
                P_\rho^{int}\cap\{v\ge s\}\ne\varnothing\}.
\]

Con máximo vacío igual a cero,

\[
 L_{\rm cross}=\max_{s\in A_\rho}[E_\rho(s)+I_\rho(s)],\qquad
 H(P_\rho)=\max_{s\in\mathbb R}[E_\rho(s)+I_\rho(s)].
 \tag{2}
\]

**Prueba.** Si ambos lados contienen puntos, elegimos cadenas óptimas y sus
extremos e,i. Entonces v(e)<=s<=v(i); O4 permite concatenarlas. Recíprocamente,
una cadena cruzada se separa en su último exterior e y primer interior i;
el umbral s=v(e) incluye ambos tramos. Si un lado está vacío, la suma es la
altura de una cadena pura. Toda cadena pura se incluye eligiendo s por encima
de todos los v exteriores o por debajo de todos los v interiores. Esto prueba
ambas igualdades, también para la nube vacía.

Para el máximo cruzado basta s en los valores v de los puntos exteriores.
Dado cualquier umbral admisible, sustitúyase por el mayor v exterior <=s:
E no cambia e I no disminuye. Para la altura total se añaden los dos valores
puros H(P_ext), H(P_int). No hace falta discretizar un continuo arbitrario.

**Contraejemplo a omitir A_rho.** Un exterior con v=1 y un interior con v=-1
son incomparables: L_cross=0, pero el máximo sin restricción vale 1.

## 2. El máximo no requiere por sí mismo un nuevo teorema probabilístico

**Lema de malla.** Sean f_rho funciones aleatorias monótonas en un intervalo
compacto J, todas con el mismo sentido. Si para cada s fijo
f_rho(s) -> f(s) en probabilidad y f es determinista y continua, entonces

\[
 \sup_{s\in J}|f_\rho(s)-f(s)|\xrightarrow{\mathbb P}0.
 \tag{3}
\]

**Prueba.** Tratamos el caso creciente; el decreciente se obtiene cambiando
el signo. El límite f también es creciente: un orden casi seguro entre dos
variables que convergen en probabilidad a constantes pasa al límite.
Elegimos una malla finita a=s_0<...<s_m=b tal que la oscilación de f entre
extremos consecutivos sea <=omega. Si el error en todos los nodos es <=eta,
la monotonía da, para s_j<=s<=s_{j+1},

\[
 f(s_j)-\eta\le f_\rho(s)\le f(s_{j+1})+\eta,\qquad
 |f_\rho(s)-f(s)|\le\eta+\omega.
\]

Una unión de m+1 eventos controla el fallo. Primero se fija la malla usando
continuidad uniforme; después rho tiende a infinito. No se requiere
independencia entre nodos, acoplamiento entre densidades ni tasa de concentración.
Para nuestros perfiles finitos los supremos son medibles: tienen finitísimos
saltos, y se pueden aproximar usando nodos racionales y los extremos de J.

Aplicamos (3) a E_rho/sqrt(2rho) e I_rho/sqrt(2rho), no a las alturas sin
normalizar. Si convergen uniformemente a e,i, respectivamente,

\[
 \left|\max_J\frac{E_\rho+I_\rho}{\sqrt{2\rho}}
                 -\max_J(e+i)\right|
 \le\left\|\frac{E_\rho}{\sqrt{2\rho}}-e\right\|_\infty+
     \left\|\frac{I_\rho}{\sqrt{2\rho}}-i\right\|_\infty.
 \tag{4}
\]

La monotonía de la suma no se supone. El conjunto aleatorio A_rho requiere
además el argumento de la sección 7 para hablar específicamente de L_cross.

## 3. Una sola carta nula regular para los dos bloques

Fijamos r_S>0 y la misma caja D=[t_0,t_1] x [r_-,r_+], con
0<r_-<r_S<r_+ y t_0<t_1. No cambiamos la caja ni el generador.
Definimos

\[
 v=t^*+r,\qquad
 Z=(1-r/r_S)\exp\!\left(\frac r{r_S}-\frac v{2r_S}\right).
 \tag{5}
\]

Z no es la W de la nota anterior. Es negativa en el exterior, cero en el
horizonte y positiva en el interior. En las coordenadas antiguas:

\[
 Z=-e^{-U/(2r_S)}\quad (ext),\qquad
 Z=e^{W/(2r_S)}\quad (int),\qquad W=-U.
 \tag{6}
\]

Cada transformación en (6) es estrictamente creciente en la coordenada
saliente orientada al futuro de su bloque. El Teorema 1 da por tanto

\[
 \boxed{p\prec q\ \Longleftrightarrow\
            v(p)\le v(q)\ \text{y}\ Z(p)\le Z(q)}
 \tag{7}
\]

para puntos distintos fuera del horizonte, **también entre bloques**:
Z(ext)<Z(int) hace automática la segunda desigualdad al entrar, e imposible
al salir. No se ha recuperado Z del poset; (7) es una representación con
coordenadas ocultas. Los puntos exactamente en el horizonte tienen medida cero;
no atribuimos al código con log(0) una implementación regular allí.

La transformación exponencial saliente es la construcción estándar de Kruskal,
manteniendo aquí v sin exponenciar. Referencia primaria de contexto:
[Harvey Reall, General Relativity, ecuaciones (12.30)-(12.31)](https://www.damtp.cam.ac.uk/user/hsr1000/lecturenotes_2012.pdf).
Las identidades (5)-(9) se derivan aquí para el t* del generador; no se atribuye
esta aplicación probabilística a esa referencia ni se reclama novedad de carta.

### Jacobiano y métrica

A v fijo,

\[
 Z_r=-\frac r{r_S^2}e^{r/r_S-v/(2r_S)}<0,\qquad
 Z_v=-Z/(2r_S).
 \tag{8}
\]

La estricta monotonía radial prueba inyectividad global; el jacobiano no se
anula para r>0, luego la inversa es suave en la imagen. La imagen del dominio
r>0 es Z<exp(-v/(2r_S)), y la caja queda compactamente dentro de ella.
Con r=r(v,Z), escribimos

\[
 q(v,Z)=\frac{r_S^2}{r}\exp\!\left(-\frac r{r_S}+\frac v{2r_S}\right),
 \qquad dt^*\,dr=q\,dv\,dZ,\qquad ds^2=2q\,dv\,dZ.
 \tag{9}
\]

Aquí la igualdad de volumen usa el valor absoluto del jacobiano. En el
horizonte q=r_S exp(-1+v/(2r_S)), estrictamente positiva.
En un entorno de la caja transformada hay constantes 0<q_*<=q<=M<infinito.
Dependen de la caja fija, pero **no de un corte |r-r_S|>=epsilon**.
No se afirma uniformidad al llevar r_- a cero o t_1 a infinito.

Esto corrige la lectura demasiado fuerte de O1-O3: no impiden una carta
producto global en este parche 1+1D. La discontinuidad de orientación, el
infinito nulo y la densidad que se anula pertenecen a la elección anterior.
El dominio transformado sigue sin ser rectangular; (9) por sí solo no
autoriza aplicar DZ directamente a su indicador.

## 4. Los perfiles variacionales son continuos, incluido el horizonte

Sea B un rectángulo compacto que contiene la imagen de D, con anchuras W_v,W_Z.
Para un peso a no negativo, fijado también en las fronteras, definimos

\[
 V(a)=\sup_{\gamma\subset B,\ \dot v,\dot Z\ge0}
               \int\sqrt{a(\gamma)\dot v\dot Z}.
 \tag{10}
\]

Las curvas son absolutamente continuas y sus extremos son libres. Fuera del
soporte el peso vale cero: son curvas para el **orden inducido**; no se exige
que permanezcan en la caja transformada. En el soporte usamos la traza suave
de q. Sobre Z=0 la acción es cero, de modo que incluir o excluir el horizonte
en uno u otro bloque no cambia V.

Con D_ext,D_int sus imágenes, ponemos

\[
 e(s)=\sqrt2\,V(q1_{D_{ext}\cap\{v\le s\}}),\qquad
 i(s)=\sqrt2\,V(q1_{D_{int}\cap\{v\ge s\}}).
 \tag{11}
\]

Son monótonos en los sentidos respectivos. Para s<t, Cauchy--Schwarz en la
franja s<=v<=t, y la monotonía de v,Z sobre cualquier curva, dan

\[
 0\le e(t)-e(s)\le\sqrt{2M W_Z(t-s)},\qquad
 0\le i(s)-i(t)\le\sqrt{2M W_Z(t-s)}.
 \tag{12}
\]

En efecto la diferencia de las acciones sobre una misma curva se concentra
en esa franja; su variación de v es <=t-s y la de Z es <=W_Z. Tomar supremos
conserva la cota. No usamos área pequeña de un conjunto arbitrario.
El mismo módulo sirve para perfiles recortados radialmente.
Así queda demostrada la continuidad que pide la sección 2.

## 5. La banda del horizonte es despreciable para alturas, uniformemente en s

Sea C_epsilon=D cap {|r-r_S|<epsilon}. Por (5), para epsilon suficientemente
pequeño existe C_0, dependiente sólo de D,r_S, tal que

\[
 \Phi(C_\epsilon)\subset
 [t_0+r_-,t_1+r_+]\times[-C_0\epsilon,C_0\epsilon].
 \tag{13}
\]

Por ejemplo puede tomarse
C_0=exp(r_+/r_S-(t_0+r_-)/(2r_S))/r_S.
Esta banda está en un rectángulo de área A_epsilon=2C_0 W_v epsilon
(elegimos W_v=t_1+r_+-t_0-r_-).
El proceso de puntos de la banda queda dominado por un Poisson homogéneo de
intensidad rho M en ese rectángulo. Sólo hace falta q<=M sobre el soporte.

**Cota elemental de cadenas.** Si N_k cuenta cadenas de k puntos en un Poisson
homogéneo planar de intensidad lambda en un rectángulo de área A,

\[
 \mathbb E N_k=\frac{(\lambda A)^k}{(k!)^2},\qquad
 \mathbb P(H\ge k)\le\frac{(\lambda A)^k}{(k!)^2}
                    \le\left(\frac{e^2\lambda A}{k^2}\right)^k .
 \tag{14}
\]

La primera igualdad resulta de integrar k puntos con ambas coordenadas
ordenadas: cada coordenada aporta 1/k!. Cada cadena tiene una única enumeración
creciente. La segunda es Markov y la tercera k!>=(k/e)^k, que se sigue de
sum(log j)>=integral_1^k log x dx>=k log k-k. La e de (14) es el número de Euler.

Con k=ceil(eta sqrt(2rho)), la base de la última potencia tiene límite
e^2 M A_epsilon/(2eta^2). Se hace menor que uno fijando epsilon pequeño.
Por tanto, para H_rho(C_epsilon),

\[
 \forall\eta>0,\qquad
 \lim_{\epsilon\downarrow0}\limsup_{\rho\to\infty}
 \mathbb P\!\left(\frac{H_\rho(C_\epsilon)}{\sqrt{2\rho}}>\eta\right)=0.
 \tag{15}
\]

Se usa inclusión de eventos cuando eta sqrt(2rho) es entero. No se invoca DZ,
un ajuste numérico ni una estimación basada sólo en el número de puntos.

Sean E_rho,epsilon,I_rho,epsilon los perfiles tras borrar la banda. Al borrar
puntos de una cadena, el resto sigue siendo cadena. Sus puntos borrados
también forman una cadena en C_epsilon. Determinísticamente,

\[
 0\le E_\rho(s)-E_{\rho,\epsilon}(s)\le H_\rho(C_\epsilon),\quad
 0\le I_\rho(s)-I_{\rho,\epsilon}(s)\le H_\rho(C_\epsilon)
 \quad\text{para todo }s.
 \tag{16}
\]

Esta cota es simultánea en s y no necesita controlar anclas aleatorias.
La versión variacional de (13), por Cauchy--Schwarz, da

\[
 \|e-e_\epsilon\|_\infty,\ \|i-i_\epsilon\|_\infty
                \le\sqrt{2M W_v(2C_0\epsilon)}.
 \tag{17}
\]

No se pierde conectividad: (10) permite puentes de peso cero.

## 6. Teorema de transferencia: qué queda condicionado exactamente

**Insumo K para esta familia, con prueba propuesta en el apéndice A.** Para cada
epsilon fijo suficientemente pequeño y cada s determinista,

\[
 \frac{E_{\rho,\epsilon}(s)}{\sqrt{2\rho}}
      \xrightarrow{\mathbb P}e_\epsilon(s),\qquad
 \frac{I_{\rho,\epsilon}(s)}{\sqrt{2\rho}}
      \xrightarrow{\mathbb P}i_\epsilon(s).
 \tag{K}
\]

Son alturas con extremos libres en las dos cajas compactas recortadas por un
semiplano v<=s o v>=s, respectivamente. No son automáticamente el mismo
enunciado que el futuro anclado F_x de E2. El apéndice A escribe esa adaptación,
incluidos los casos vacíos o degenerados, y explicita el insumo probabilístico.
Su revisión sigue pendiente. La regularidad de la carta no sustituye esa prueba.

**Teorema condicional a K.** En J=[t_0+r_-,t_1+r_+],

\[
 \left\|\frac{E_\rho}{\sqrt{2\rho}}-e\right\|_\infty
 +\left\|\frac{I_\rho}{\sqrt{2\rho}}-i\right\|_\infty
                  \xrightarrow{\mathbb P}0,
 \qquad
 \frac{H(P_\rho)}{\sqrt{2\rho}}\xrightarrow{\mathbb P}\max_J(e+i).
 \tag{18}
\]

**Prueba.** Para epsilon fijo, K, (12) y el lema de malla dan convergencia
uniforme de los perfiles recortados. La desigualdad triangular separa el error
total en (16)/sqrt(2rho), el error recortado y (17).
Para una tolerancia dada se elige epsilon primero, haciendo pequeños (15)
y (17); luego rho tiende a infinito. Finalmente se aplican (2) y (4).
No se intercambian límites sin justificación ni se elige epsilon=rho^{-alpha}.

## 7. El máximo de cadenas que efectivamente cruzan

Si ambos bloques están presentes,
A_rho=[a_rho,b_rho] cuando a_rho<=b_rho, donde
a_rho=min v(P_ext), b_rho=max v(P_int); en caso contrario es vacío.
Para la caja fijada, sean a=t_0+r_S y b=t_1+r_S, con a<b.
Entonces a_rho -> a y b_rho -> b en probabilidad:
siempre a_rho>=a y b_rho<=b, y cada vecindad unilateral de esos extremos
contiene una región de volumen positivo del bloque correspondiente.
La probabilidad de no ver puntos allí es exp(-rho volumen).
La probabilidad de un bloque vacío también tiende a cero.

En particular A_rho no es vacío con probabilidad tendente a uno y converge
al intervalo [a,b] en distancia de Hausdorff. Para una función continua F,
la diferencia entre sus máximos sobre dos intervalos compactos se acota por
su módulo de continuidad evaluado en esa distancia. Combinando con (18):

\[
 \boxed{\frac{L_{\rm cross}}{\sqrt{2\rho}}
       \xrightarrow{\mathbb P}\max_{s\in[t_0+r_S,t_1+r_S]}[e(s)+i(s)]}
 \quad\text{condicional a K}.
 \tag{19}
\]

Esto justifica el dominio de maximización, además de la uniformidad.
No identifica por sí solo el funcional límite con tiempo propio restringido a
D: sigue haciendo falta probar accesibilidad dentro de D para esa identificación.
No demuestra localización del horizonte desde el poset ni un resultado 3+1D.

## 8. Verificación y techo de evidencia

Código permanente: [verify_horizon_threshold.py](verify_horizon_threshold.py).
Ejecución desde la raíz:

~~~bash
python3 dev/verify_horizon_threshold.py
~~~

Comprueba seis identidades simbólicas, la carta contra el generador congelado
en 5832 pares y dos empates nulos, las dos identidades finitas por enumeración
de los 512 subposets de una rejilla 3x3, y 1225 pares de perfiles monótonos.
Incluye un contraejemplo explícito a permitir lados vacíos para L_cross.
Son comprobaciones finitas independientes de las pruebas asintóticas; no son
sprinklings científicos ni evidencia de detección.

Formalización parcial:
[HorizonThreshold.lean](../formal/HorizonFormal/HorizonFormal/HorizonThreshold.lean).

~~~bash
cd formal/HorizonFormal
lake env lean HorizonFormal/HorizonThreshold.lean
~~~

Lean verifica monotonía exponencial en ambos bloques, compatibilidad cruzada
y exclusión de salida, equivalencia de testigos par/umbral y la desigualdad
determinista de malla. Sus siete declaraciones auditadas sólo usan
propext, Classical.choice y Quot.sound; no usan sorryAx.
No formaliza el jacobiano, la igualdad de alturas máximas, el proceso Poisson,
las pruebas (12)-(19) ni la relación completa del generador.

También se ejecutó `lake build HorizonFormal`: terminó correctamente
(2376 jobs), con avisos en módulos anteriores S1Paper y E2Segment.
No se modificaron ni silenciaron esos avisos. El módulo nuevo compiló sin
avisos en su comprobación directa. `git diff --check` pasó.

**Avance concreto:** la fórmula finita está cerrada con sus casos vacíos;
la continuidad de los perfiles variacionales y la eliminación uniforme de la
banda del horizonte tienen pruebas explícitas. El límite completo se reduce
al insumo compacto puntual K, cuya prueba propuesta figura a continuación.
Quedan pendientes la revisión matemática y la identificación geométrica final;
no se declara cerrado el teorema de detección del horizonte.

## Apéndice A. Prueba propuesta de K en cajas con umbral

Este apéndice completa el argumento analítico, con revisión pendiente.
Usa el Teorema 2(i) de
[Deuschel--Zeitouni (1995)](https://projecteuclid.org/journals/annals-of-probability/volume-23/issue-2/Limiting-Curves-for-IID-Records/10.1214/aop/1176988293.full)
solamente para densidades suaves estrictamente positivas en un rectángulo,
tras normalizar y reescalar al cuadrado unidad. Se inspeccionaron directamente
las imágenes de pp. 853-855 del PDF local: (A1), (A2), definición de J y
Teorema 2(i). No se usa el OCR para las fórmulas ni se invocan las extensiones
de los Remarks para indicadores curvos.

### A.1 Geometría compacta y modificación exacta de E2

Fijamos epsilon>0 antes de tomar rho->infinito. En cada caja radial recortada
usamos las coordenadas antiguas (v,w) y q_old=|f|/2. Son suaves, con
0<q_*<=q_old<=M_epsilon; todas las constantes de este apéndice pueden depender
de epsilon. En el exterior z=v-w, en el interior z=v+w; r=h(z) y
T(v,w)=v-h(z). Como h'=f/2, en un entorno compacto del mismo bloque

\[
 T_v=1-f/2>0,\qquad T_w=|f|/2>0.
\]

El dominio de cada perfil es

\[
 F_s=\{a\le z\le b,\ t_0\le T\le t_1,\ \sigma(v-s)\ge0\},
 \quad \sigma=-1\ (ext),\quad \sigma=+1\ (int).
 \tag{A1}
\]

Son cinco desigualdades, sin ancla. F_{s,+eta} las relaja a margen -eta;
F_{s,-eta} exige margen +eta. Dos puntos comparables en cualquiera de estos
conjuntos se unen por su segmento: z es afín, T es creciente sobre el segmento
y la restricción en v se conserva. El argumento de reemplazo de huecos de
E2 §3 da V(q_old 1_F)=I(q_old,F), también para F_{s,+eta} y F_{s,-eta}.
Para recordar la justificación de huecos infinitos: parametrícese por v+w;
las coordenadas son 1-Lipschitz, se reemplaza cada intervalo fuera del soporte
por el segmento entre sus extremos, y la curva resultante sigue siendo
1-Lipschitz. Coincide con la original y tiene las mismas derivadas casi en
todas partes en el conjunto de parámetros retenidos, de modo que no pierde
acción allí. Los segmentos añadidos aportan acción no negativa.

En el exterior, a una curva en F_{s,+eta} se le retiene la parte que satisface

\[
 t_0+(H+1)\eta\le T\le t_1-(H+1)\eta,\qquad v\le s-2\eta,
\]

con H>=1 una constante Lipschitz de T. Es un intervalo porque T y v crecen.
Se aplica después, con u=v+w y d=v-w,

\[
 (v,w)\longmapsto
 \left(\frac{u+\operatorname{clip}_{[a+\eta,b-\eta]}d}{2},
       \frac{u-\operatorname{clip}_{[a+\eta,b-\eta]}d}{2}\right).
 \tag{A2}
\]

Cada coordenada se desplaza a lo sumo eta; las derivadas siguen siendo
no negativas, y su producto no disminuye, porque
(u'^2-clip(d)'^2)/4 >= (u'^2-d'^2)/4.
El resultado está en F_{s,-eta}. Se pierden dos franjas temporales de anchura
(H+2)eta y una franja en v de anchura 3eta. Las primeras cuestan O(eta),
ya que T'>=m(v'+w'); la última cuesta O(sqrt(eta)) por Cauchy--Schwarz.
La variación del peso aporta O(eta), usando que sqrt(q_old) es Lipschitz.

En el interior basta retener
a+eta<=v+w<=b-eta, t_0+eta<=T<=t_1-eta y v>=s+eta.
Son restricciones monótonas; lo descartado está en dos franjas radiales,
dos temporales y una nula, todas de anchura 2eta. El mismo argumento acota
la pérdida por C sqrt(eta). Si el intervalo retenido es vacío, toda la acción
está en las franjas descartadas y satisface esa cota.
Así, también cuando F_s es vacío o degenerado,

\[
 0\le V(q_{old}1_{F_{s,+\eta}})
           -V(q_{old}1_{F_{s,-\eta}})\le C_\epsilon\sqrt\eta.
 \tag{A3}
\]

Esto es el cambio necesario respecto del futuro anclado: se elimina la
restricción en w y se conserva, o se invierte, la del umbral en v.

### A.2 Rejillas y densidades constantes por celda

En un rectángulo ambiente fijo del plano (v,w), tomamos celdas diádicas de
diámetro <=h en norma infinito. Las celdas interiores tienen clausura contenida
en F_s; las exteriores tienen clausura que lo intersecta. Para una constante
Lipschitz H_0 de las cinco restricciones y eta=2H_0 h,

\[
 F_{s,-\eta}\subset R_h^-\subset F_s\subset R_h^+
      \subset F_{s,+\eta}.
\]

En las celdas activas ponemos el ínfimo o supremo de q_old, respectivamente;
en las demás, cero. Se usa la extensión suave de q_old a un entorno real
del compacto. Las celdas activas están dentro de ese entorno para h pequeño.
Resultan pesos a_h^-<=q_old 1_{F_s}<=a_h^+ casi por doquier.
Por (A3) y la oscilación Lipschitz de sqrt(q_old),

\[
 V(a_h^+)-V(a_h^-)\le C_\epsilon\sqrt h.
 \tag{A4}
\]

Sobre aristas horizontales o verticales el producto de derivadas es cero
casi en todas partes. Por ello las convenciones disjuntas de las celdas
no cambian el funcional, además de ser irrelevantes para el Poisson.

### A.3 Insumo probabilístico y pesos escalonados

Para un peso b suave y estrictamente positivo en un rectángulo B, sea
m_b=integral_B b. Condicionado a N~Poisson(rho m_b), los puntos son i.i.d.
con densidad b/m_b. DZ 2(i), tras el reescalado afín de B, da
H_n/sqrt(n)->2V(b)/sqrt(m_b) en probabilidad. Una mezcla sobre N conserva
el límite: para n>=n_0 las probabilidades de error son uniformemente pequeñas,
y P(N<n_0)->0. Como N/rho->m_b,

\[
 H_\rho(b)/\sqrt\rho\xrightarrow{\mathbb P}2V(b).
 \tag{A5}
\]

La forma gráfica de J en p. 854 y la forma paramétrica V coinciden para b
continuo. Puede comprobarse mediante polígonos monótonos: en cada tramo,
Cauchy--Schwarz acota la acción por sqrt(sup b Delta v Delta w); el segmento
recto aporta al menos sqrt(inf b Delta v Delta w). Una partición fina por
v+w hace pequeña la oscilación de sqrt(b), y la suma de sqrt(Delta v Delta w)
es <=sqrt(W_v W_w). Esto aproxima también gráficos monótonos con saltos al
completar sus partes verticales. En sentido inverso, un polígono monótono
se aproxima por uno con incrementos de v estrictamente positivos, que es
un gráfico admisible. Los tramos verticales u horizontales aportan cero.

Ahora sea a>=0 constante en finitísimas celdas rectangulares.
Para la **cota inferior**, fijamos una curva casi óptima para V(a). En cada
interior de celda visitado, entrada p y salida q delimitan un rectángulo:
su altura homogénea tiene límite 2sqrt(c Delta v Delta w), por (A5).
Este valor domina el doble de la acción de la curva en esa celda.
Se recortan esos rectángulos ligeramente para hacerlos interiores y preservar
que todos los puntos de uno preceden a todos los del siguiente.
La curva sólo visita finitísimas celdas, cada una en un intervalo; los tramos
en líneas de rejilla aportan cero. Concatenar cadenas y una unión finita de
eventos prueban la cota inferior 2V(a).

Para la **cota superior**, sean chi_{Q,delta} mesetas suaves, entre cero y uno,
iguales a uno en cada celda cerrada Q de peso c_Q>0, y cero fuera de su
engrosamiento por delta. Ponemos b_delta=delta+sum_Q c_Q chi_{Q,delta}.
Es suave, positivo y mayoriza a. Fuera de franjas de anchura 2delta alrededor
de la rejilla, b_delta=a+delta. La densidad está uniformemente acotada para
esta rejilla fija. Cauchy--Schwarz en cada franja y
sqrt(a+delta)-sqrt(a)<=sqrt(delta) fuera de ellas dan
0<=V(b_delta)-V(a)<=C_rejilla sqrt(delta).
La dominación Poisson y (A5), primero con delta fijo y luego delta->0,
prueban la cota superior. Por tanto (A5) vale para los pesos escalonados.
No se usa una extensión no verificada de DZ a densidades discontinuas.

### A.4 Cierre de K y alcance

Acoplamos las tres intensidades de A.2 por un Poisson marcado:
H_rho(a_h^-)<=H_rho(q_old 1_{F_s})<=H_rho(a_h^+).
Para una tolerancia dada fijamos primero h pequeño usando (A4), y después
rho grande usando A.3. Esto prueba el límite puntual de altura
H_rho(q_old 1_{F_s})/sqrt(2rho)->sqrt(2)V(q_old 1_{F_s}).
Si el soporte tiene área cero, la nube está vacía casi seguramente; (A3)-(A4)
también fuerzan V=0, así que el mismo enunciado cubre ese caso.

Finalmente (6) es un cambio suave, creciente y con inversa suave sobre cada
compacto recortado. Para la transformación w->Z, q_new=q_old/(dZ/dw),
por lo que q_new v' Z'=q_old v' w'; transforma curvas ambiente monótonas
en curvas del mismo tipo y conserva las acciones con peso cero fuera del
soporte. Se pueden elegir rectángulos ambiente correspondientes; agrandarlos
no cambia V, porque las partes antes o después de las visitas se eliminan
y los huecos se pueden reemplazar por segmentos monótonos.
Los valores obtenidos son exactamente e_epsilon(s),i_epsilon(s) de K.

**Estado:** K tiene ahora una prueba propuesta explícita, y con ella
(18)-(19) tienen una derivación completa apoyada en DZ 2(i).
La revisión matemática independiente de A.1-A.4 y de E2 §7 sigue pendiente.
No se eleva por ello el estado de documentos sellados, ni se confunde esta
prueba escrita con la formalización parcial de la sección 8.
