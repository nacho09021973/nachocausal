# Geometría local y horizontes globales en órdenes causales Schwarzschild 1+1

José Ignacio Martín Gandul

Autor de correspondencia: jmartin596@alumno.uned.es

## Resumen

Estudiamos el orden causal no etiquetado de un proceso de Poisson homogéneo en una caja Schwarzschild de dimensión \(1+1\) que atraviesa \(r=r_S\). Una carta nula regular representa exactamente el orden por comparabilidad coordenada y transforma el volumen en una densidad suave y positiva. La altura, normalizada por \(\sqrt{2\rho}\), converge al tiempo propio máximo restringido a la caja. La longitud máxima de las cadenas que cruzan la superficie distinguida tiene un límite análogo, definido con el embedding conocido. Estos resultados métricos coexisten con una imposibilidad exacta de certificación del horizonte global: construimos dos extensiones suaves, temporalmente orientadas y fuertemente causales de una misma vecindad relativamente compacta de la caja. Una contiene la superficie observada en su horizonte de sucesos; la otra posee infinito nulo futuro y no tiene horizonte. Las extensiones inducen exactamente el mismo volumen y orden sobre la caja, y por tanto la misma ley del poset, incluida su cardinalidad, para cada intensidad positiva. Todo test binario basado en ese dato tiene error máximo al menos \(1/2\) sobre el par.

## 1. Introducción

El orden causal y el número de elementos de un sprinkling pueden informar sobre la geometría de la región observada. Una cuestión diferente es si determinan el papel de esa región dentro de un espaciotiempo completo. Un horizonte de sucesos se define mediante el pasado causal del infinito nulo futuro; su definición involucra una extensión global.

Este artículo separa ambas preguntas en una configuración explícita. Mantenemos una caja Schwarzschild \(1+1\), con su métrica y orientación temporal conocidas para la interpretación geométrica. Por una parte, relacionamos alturas de cadenas con funcionales de tiempo propio dentro de la caja. Por otra, preservamos exactamente la geometría de una vecindad de la observación y construimos dos extensiones con predicados globales de horizonte opuestos.

El resultado positivo usa una ley de cadenas crecientes de Deuschel y Zeitouni [DZ95]. La transferencia a la caja requiere controlar sus fronteras y el cruce de \(r=r_S\); esas piezas se explicitan en §4 y el apéndice A. El resultado negativo no depende de esa ley límite: se obtiene de dos isometrías locales, una prueba de ausencia de relaciones causales nuevas y dos completaciones conformes explícitas.

La altura total es un observable del poset sin etiquetas. La longitud cruzada se define aquí mediante la partición exterior/interior del modelo conocido. No se presenta esa partición como información recuperada del poset. En el teorema de imposibilidad, el dato disponible es exclusivamente el poset no etiquetado, incluida su cardinalidad.

No se reclama novedad de la carta de Kruskal, del principio estadístico de indistinguibilidad ni del teorema de cadenas crecientes. El contenido que se desarrolla es su realización y compatibilidad exactas para la caja y la clase local de extensiones fijadas aquí.

## 2. Modelo observado y enunciados

Fijamos \(s=r_S>0\) y una caja Schwarzschild 1+1:

\[
D=[t_0,t_1]\times[r_-,r_+],\qquad
t_0<t_1,\qquad 0<r_-<s<r_+.
\]

La métrica local, con signatura \((+,-)\), es

\[
g=f\,d{t^*}^2-2(1-f)\,dt^*dr+(f-2)\,dr^2,
\qquad f=1-\frac sr,\qquad \det g=-1.
\]

Sea \(\Phi:(t^*,r)\mapsto(U,V)\) la carta regular definida en §3, cuya imagen para \(r>0\) es

\[
\Omega=\{(U,V)\in\mathbb R^2:V>0,\ UV<1\}.
\]

El dato local preservado es la restricción Schwarzschild \(g_{U_0}\) a un entorno abierto **fijado antes de los datos** tal que

\[
\overline D\subset U_0,\qquad
K:=\Phi(\overline{U_0})\Subset\Omega.
\]

El símbolo \(U_0\) designa el entorno y \(U\) la coordenada nula. Se preserva exactamente todo \(U_0\).

\[
\Sigma_S := \{r=r_S\}\cap D.
\]

Dato del experimento: exclusivamente el poset no etiquetado \(P_\rho|_D\), incluida su cardinalidad, inducido por un proceso de Poisson homogéneo de intensidad \(\rho>0\) respecto de \(\mathrm{vol}_{g_{U_0}}\) sobre \(D\).

Una extensión del dato local es un cuádruplo
\[
e=(M,g,\varphi,\mathscr{I}^+_e)
\]
donde \(\varphi:(U_0,g_{U_0})\hookrightarrow(M,g)\) es una incrustación isométrica \(C^2\) sobre imagen abierta que preserva la orientación temporal, \(M\) es time-oriented y fuertemente causal, y \(\mathscr{I}^+_e\) es una frontera conforme nula futura explícita que hace que
\[
\mathcal{H}^+(e)\,:=\,\partial_M J^-_M(\mathscr{I}^+_e)
\]
esté definido. Aquí \(J^-_M(\mathscr I^+_e)\) es el conjunto de puntos físicos desde los que existe una curva causal futura con extremo en \(\mathscr I^+_e\) y con su parte anterior al extremo en \(M\). La frontera del pasado se toma dentro de \(M\), no dentro de la completación conforme.

Usamos \(p\prec q\) para la relación causal futura con la diagonal excluida; incluye separación nula. Las relaciones y medidas sobre \(D\) se comparan mediante las incrustaciones \(\varphi_e\).


Definimos \(\tau_D\) como el supremo del tiempo propio de curvas causales futuras contenidas en \(D\), con extremos libres. Definimos \(\tau_D^{\mathrm{cross}}\) restringiendo el supremo a curvas que visitan tanto \(r>r_S\) como \(r<r_S\). La altura del poset vacío es cero. \(L_{\mathrm{cross}}\) es el máximo número de vértices de una cadena que contiene puntos de ambos bloques, y vale cero si no existe tal cadena.

**Teorema 1 (tiempo propio en la caja conocida).** Para el proceso homogéneo de intensidad física \(\rho\),
\[
\frac{H(P_\rho|_D)}{\sqrt{2\rho}}\xrightarrow{\mathbb P}\tau_D,
\qquad
\frac{L_{\mathrm{cross}}}{\sqrt{2\rho}}
\xrightarrow{\mathbb P}\tau_D^{\mathrm{cross}}.
\]
La segunda estadística usa el embedding y la partición Schwarzschild conocidos. Ninguno de estos límites certifica que \(r=r_S\) sea un horizonte global.

**Teorema 2 (No-go B).** Existen dos extensiones fijas del mismo \((U_0,g_{U_0})\), independientes de \(\rho\) y de los datos, tales que
\[
\prec_{e_H}|_{D\times D}
=\prec_{U_0}|_{D\times D}
=\prec_{e_0}|_{D\times D},
\qquad
d\operatorname{vol}_{e_H}|_D
=d\operatorname{vol}_{e_0}|_D
=d\operatorname{vol}_{g_{U_0}}|_D,
\]
pero
\[
\varphi_H(\Sigma_S)\subset\mathcal H^+(e_H),
\qquad
J^-_{M_0}(\mathscr I_0^+)=M_0,\qquad
\mathcal H^+(e_0)=\varnothing.
\]
En consecuencia, para cada \(\rho>0\), las leyes de \(P_\rho|_D\) coinciden exactamente, incluida cardinalidad. Para cualquier test binario, determinista o aleatorizado con una regla común,
\[
\Pr_{e_H}(\delta_\rho=0)+\Pr_{e_0}(\delta_\rho=1)=1,
\qquad
\max\{\operatorname{error}_H,\operatorname{error}_0\}\ge\frac12.
\]
Aquí \(1\) decide por la alternativa con horizonte y \(0\) por la alternativa sin horizonte.

## 3. Carta regular y extensiones explícitas

Definimos

\[
v=t^*+r,\qquad
U=\left(1-\frac rs\right)e^{r/s-v/(2s)},\qquad
V=e^{v/(2s)}>0.
\]

La sustitución \(dt^*=dv-dr\) en la métrica de §2 da

\[
g=f\,dv^2-2\,dv\,dr.
\]

Además,

\[
UV=h(r):=\left(1-\frac rs\right)e^{r/s},\qquad
h'(r)=-\frac r{s^2}e^{r/s}<0.
\]

La función \(h:(0,\infty)\to(-\infty,1)\) es biyectiva, por lo que \(r=h^{-1}(UV)\) es suave donde \(UV<1\). Junto con \(v=2s\log V\) y \(t^*=v-r\), esto prueba que \(\Phi\) es un difeomorfismo sobre \(\Omega\).

A \(v\) fijo, \(U_r=-r e^{r/s-v/(2s)}/s^2\), y \(U_v=-U/(2s)\). Sustituyendo estas derivadas en la métrica se obtiene

\[
g=2q\,dv\,dU,\qquad
q=\frac{s^2}{r}e^{-r/s+v/(2s)}.
\]

Como \(dv=2s\,dV/V\), resulta

\[
\boxed{g=2Q(U,V)\,dU\,dV,\qquad
Q(U,V)=\frac{2s^3}{r(U,V)}e^{-r(U,V)/s}>0.}
\]

La fórmula para \(Q\) es suave en todo \(\{UV<1\}\). En particular,

\[
U<0\iff r>s,\qquad U=0\iff r=s,\qquad U>0\iff r<s
\quad\text{en }\Omega,
\qquad Q(0,V)=\frac{2s^2}{e}.
\]

### 3.1. El par de extensiones

**Testigo con horizonte.** Tomamos el Kruskal radial completo

\[
M_H=\{(U,V)\in\mathbb R^2:UV<1\},\qquad
g_H=2Q\,dU\,dV,\qquad \varphi_H=\Phi|_{U_0}.
\]

Su frontera nula futura será \(\mathscr I_H^+=\mathscr I_R^+\sqcup\mathscr I_L^+\), definida en B.3.

**Testigo sin horizonte.** Fijamos \(c>0\) y

\[
\chi\in C_c^\infty(\Omega),\qquad 0\le\chi\le1,
\qquad \chi=1\text{ en una vecindad de }K=\Phi(\overline{U_0}).
\]

Para construirla, sea \(d=\operatorname{dist}(K,\mathbb R^2\setminus\Omega)>0\) y fijemos \(0<\varepsilon<d/4\). Sea \(\eta\) la mollificadora normalizada proporcional a \(\exp[-1/(1-|z|^2)]\) para \(|z|<1\), y cero fuera; ponemos \(\eta_\varepsilon(z)=\varepsilon^{-2}\eta(z/\varepsilon)\). Entonces sirve

\[
\chi=\mathbf 1_{\{\operatorname{dist}(\cdot,K)<2\varepsilon\}}*\eta_\varepsilon.
\]

Esta función vale uno si \(\operatorname{dist}(\cdot,K)<\varepsilon\), y su soporte compacto queda en \(\{\operatorname{dist}(\cdot,K)\le3\varepsilon\}\subset\Omega\).

Definimos

\[
F(U,V)=
\begin{cases}
\chi(U,V)\log\!\bigl(Q(U,V)/c\bigr),&(U,V)\in\Omega,\\
0,&(U,V)\notin\Omega,
\end{cases}
\qquad Q_0=ce^F.
\]

Como \(\operatorname{supp}\chi\Subset\Omega\), la extensión por cero de \(F\) es suave. En consecuencia,

\[
Q_0\in C^\infty(\mathbb R^2),\qquad Q_0>0,\qquad
Q_0=Q\text{ cerca de }K,\qquad
Q_0=c\text{ fuera de un compacto}.
\]

Tomamos

\[
M_0=\mathbb R^2,\qquad g_0=2Q_0\,dU\,dV,
\qquad \varphi_0=\Phi|_{U_0}.
\]

Su \(\mathscr I_0^+\) se define en B.3. Tanto \(c\) como \(\varepsilon\), \(\chi\) y las dos extensiones quedan fijados antes de observar datos, independientemente de \(\rho\). Ambas incrustaciones satisfacen exactamente

\[
\varphi_H^*g_H=\varphi_0^*g_0=g_{U_0}
\quad\text{en todo }U_0.
\]

**Orientación temporal.** En ambos testigos elegimos el futuro mediante el campo timelike \(T=\partial_U+\partial_V\). Si \(Q_e\) denota \(Q\) o \(Q_0\), para un vector no nulo \(X=a\partial_U+b\partial_V\),

\[
g_e(X,X)=2Q_eab,\qquad g_e(X,T)=Q_e(a+b).
\]

Por ello,

\[
X\text{ es causal futuro}\iff a\ge0,\ b\ge0.
\]

Esta orientación coincide con la del dato local. En efecto, en \(\Omega\), \(h'(r)<0\) da \(r_U=V/h'(r)\) y \(r_V=U/h'(r)\), de modo que

\[
\frac{\partial t^*}{\partial U}=-\frac V{h'(r)}>0,
\qquad
\frac{\partial t^*}{\partial V}
=\frac{2s}{V}-\frac U{h'(r)}
=\frac{s(1+s/r)}V>0.
\]

Toda curva causal futura tiene \(U,V\) no decrecientes, también para curvas localmente absolutamente continuas, aplicando las desigualdades a sus tangentes casi por doquier.

**Causalidad fuerte.** Alrededor de cada punto de \(M_H\) o \(M_0\) hay rectángulos coordenados abiertos arbitrariamente pequeños contenidos en el espaciotiempo. Si los extremos de una curva causal están en uno de esos rectángulos, la monotonía obliga a toda la curva a permanecer en él. Estos rectángulos forman una base de entornos causalmente convexos. Ambos testigos son, por tanto, fuertemente causales, además de suaves y temporalmente orientados.

## 4. Alturas y tiempo propio: demostración del Teorema 1

### 4.1. Funcionales y descomposición finita

Para el argumento probabilístico usamos \((v,U)\), con
\[
g=2q(v,U)\,dv\,dU,\qquad
q(v,U)=\frac{s^2}{r}e^{-r/s+v/(2s)}.
\]
En una vecindad de la caja transformada \(q\) es suave y está acotada entre dos constantes positivas. Sea \(B\) un rectángulo que contiene esa caja. Para un peso \(a\ge0\) definido sobre \(B\), ponemos
\[
\mathcal V(a)=
\sup_{\substack{\gamma\subset B\\ \dot v,\dot U\ge0}}
\int\sqrt{a(\gamma)\dot v\dot U}\,d\lambda.
\]
Las curvas son absolutamente continuas y tienen extremos libres. Si \(a=q\mathbf1_G\), se permite que la curva salga de \(G\), con peso cero fuera. No identificamos este funcional con uno intrínseco para soportes arbitrarios.

Escribimos \(D_{\rm ext}=D\cap\{r>s\}\) y \(D_{\rm int}=D\cap\{r<s\}\), identificados con sus imágenes. Definimos
\[
e(\xi)=\sqrt2\,\mathcal V(q\mathbf1_{D_{\rm ext}\cap\{v\le\xi\}}),
\qquad
i(\xi)=\sqrt2\,\mathcal V(q\mathbf1_{D_{\rm int}\cap\{v\ge\xi\}}).
\]
La traza de \(q\) se fija por la métrica suave; una curva sobre \(U=0\) tiene acción cero.

Para la nube, fuera del suceso nulo de contener puntos en \(r=s\), sean
\[
E_\rho(\xi)=H(P_\rho^{\rm ext}\cap\{v\le\xi\}),\qquad
I_\rho(\xi)=H(P_\rho^{\rm int}\cap\{v\ge\xi\}),
\]
\[
A_\rho=\{\xi:P_\rho^{\rm ext}\cap\{v\le\xi\}\ne\varnothing,\
P_\rho^{\rm int}\cap\{v\ge\xi\}\ne\varnothing\}.
\]
El orden producto da, para un exterior \(p\) y un interior \(q\),
\[
p\prec q\iff v_p\le v_q;
\]
el cruce inverso es imposible. Toda cadena cruzada se separa, por tanto, en un tramo exterior seguido de uno interior. Cortando en el último exterior o concatenando cadenas óptimas obtenemos exactamente
\[
H(P_\rho|_D)=\max_{\xi\in J}[E_\rho(\xi)+I_\rho(\xi)],
\]
\[
L_{\rm cross}=\max_{\xi\in A_\rho}[E_\rho(\xi)+I_\rho(\xi)],
\qquad J=[t_0+r_-,t_1+r_+].
\]
El máximo cruzado vacío vale cero. Los extremos de \(J\) permiten incluir las cadenas puramente interiores o exteriores en la primera identidad. Exigir dos lados no vacíos es indispensable en la segunda.

### 4.2. Continuidad y corte alrededor de \(r=s\)

Sean \(M\) una cota de \(q\) sobre el soporte y \(W_v,W_U\) las anchuras de un rectángulo ambiente fijo. Por Cauchy–Schwarz, la acción sobre una franja \(\xi\le v\le\zeta\) es a lo sumo \(\sqrt{M(\zeta-\xi)W_U}\). Así, para \(\xi<\zeta\),
\[
0\le e(\zeta)-e(\xi)\le\sqrt{2MW_U(\zeta-\xi)},
\]
\[
0\le i(\xi)-i(\zeta)\le\sqrt{2MW_U(\zeta-\xi)}.
\]
En particular, ambos perfiles son continuos y monótonos en sentidos opuestos.

Sea \(C_\epsilon=D\cap\{|r-s|<\epsilon\}\). De la fórmula de \(U\),
\[
\Phi(C_\epsilon)\subset
J\times[-C_0\epsilon,C_0\epsilon],
\qquad
C_0=\frac1s
\exp\!\left(\frac{r_+}{s}-\frac{t_0+r_-}{2s}\right).
\]
El área del rectángulo es \(A_\epsilon=2C_0W_v\epsilon\). El proceso de la banda está dominado por un Poisson homogéneo planar de intensidad \(\rho M\) en ese rectángulo.

Para un Poisson de intensidad \(\lambda\) sobre un rectángulo de área \(A\), el número \(N_k\) de cadenas de \(k\) puntos satisface
\[
\mathbb EN_k=\frac{(\lambda A)^k}{(k!)^2}.
\]
Cada coordenada ordenada aporta un factor \(1/k!\), y cada cadena tiene una sola enumeración creciente. Por Markov y \(k!\ge(k/e)^k\),
\[
\Pr(H\ge k)\le
\frac{(\lambda A)^k}{(k!)^2}
\le\left(\frac{e^2\lambda A}{k^2}\right)^k.
\]
Tomando \(k=\lceil\eta\sqrt{2\rho}\rceil\) y fijando primero \(\epsilon\) suficientemente pequeño, obtenemos
\[
\lim_{\epsilon\downarrow0}\limsup_{\rho\to\infty}
\Pr\!\left(\frac{H_\rho(C_\epsilon)}{\sqrt{2\rho}}>\eta\right)=0
\qquad(\eta>0).
\]

Sean \(E_{\rho,\epsilon},I_{\rho,\epsilon}\) los perfiles después de borrar esa banda y \(e_\epsilon,i_\epsilon\) sus versiones variacionales. Borrar puntos de una cadena conserva una cadena; los puntos borrados forman otra cadena dentro de \(C_\epsilon\). Por ello, simultáneamente en \(\xi\),
\[
0\le E_\rho(\xi)-E_{\rho,\epsilon}(\xi)\le H_\rho(C_\epsilon),
\qquad
0\le I_\rho(\xi)-I_{\rho,\epsilon}(\xi)\le H_\rho(C_\epsilon).
\]
La misma franja, por Cauchy–Schwarz, da
\[
\|e-e_\epsilon\|_\infty,\ \|i-i_\epsilon\|_\infty
\le\sqrt{2MW_v(2C_0\epsilon)}.
\]

### 4.3. Del límite compacto al límite uniforme

El apéndice A demuestra, para cada \(\epsilon>0\) fijo suficientemente pequeño y cada \(\xi\) determinista,
\[
\frac{E_{\rho,\epsilon}(\xi)}{\sqrt{2\rho}}
\xrightarrow{\mathbb P}e_\epsilon(\xi),
\qquad
\frac{I_{\rho,\epsilon}(\xi)}{\sqrt{2\rho}}
\xrightarrow{\mathbb P}i_\epsilon(\xi).
\]
Solo usa [DZ95, Teorema 2(i)] en rectángulos con densidad suave positiva; la poissonización y el tratamiento de los soportes curvos se prueban por separado.

Recordemos un lema elemental. Si \(f_\rho\) es monótona en un compacto \(J\), converge puntualmente en probabilidad a \(f\), y \(f\) es continua, entonces
\[
\|f_\rho-f\|_\infty\xrightarrow{\mathbb P}0.
\]
Para probarlo, elegimos una malla finita donde la oscilación de \(f\) entre vecinos sea menor que \(\delta\). La monotonía controla cada valor de \(f_\rho\) por los valores en los extremos vecinos; una unión finita de eventos controla el error de esos extremos. El error uniforme queda acotado por el error en la malla más \(\delta\).

Aplicamos el lema a cada perfil recortado. La desigualdad triangular, las cotas de §4.2 y la elección de \(\epsilon\) antes de llevar \(\rho\) a infinito dan
\[
\left\|\frac{E_\rho}{\sqrt{2\rho}}-e\right\|_\infty
+
\left\|\frac{I_\rho}{\sqrt{2\rho}}-i\right\|_\infty
\xrightarrow{\mathbb P}0.
\]
No se elige un corte dependiente de \(\rho\) ni se intercambian límites. La identidad finita implica
\[
\frac{H(P_\rho|_D)}{\sqrt{2\rho}}
\xrightarrow{\mathbb P}\max_{\xi\in J}[e(\xi)+i(\xi)].
\]

Si ambos bloques de la nube son no vacíos, escribimos
\[
a_\rho=\min v(P_\rho^{\rm ext}),\qquad
b_\rho=\max v(P_\rho^{\rm int}).
\]
Cuando \(a_\rho\le b_\rho\), \(A_\rho=[a_\rho,b_\rho]\). Los extremos deterministas son
\[
a=t_0+s,\qquad b=t_1+s,\qquad a<b.
\]
Siempre \(a_\rho\ge a\), \(b_\rho\le b\), y las vecindades unilaterales de los extremos contienen regiones de volumen positivo. La probabilidad de no observar puntos en una de esas regiones es \(\exp(-\rho\,\mathrm{vol})\). Por tanto, \(a_\rho\to a\) y \(b_\rho\to b\) en probabilidad, y \(A_\rho\) es no vacío con probabilidad tendente a uno. La convergencia de intervalos y la continuidad de \(e+i\) dan
\[
\frac{L_{\rm cross}}{\sqrt{2\rho}}
\xrightarrow{\mathbb P}\max_{\xi\in[a,b]}[e(\xi)+i(\xi)].
\]

### 4.4. Identificación con tiempo propio restringido

Para una curva en la caja,
\[
\tau(\gamma)=\int\sqrt{2q(\gamma)\dot v\dot U}\,d\lambda.
\]
Los segmentos por bloques del Lema B.2, demostrado en §5, preservan además cualquier restricción \(v\le\xi\) o \(v\ge\xi\) satisfecha por sus extremos. En los soportes compactos recortados, cada excursión de una curva ambiente fuera del soporte puede reemplazarse por uno de esos segmentos, sin perder acción acumulada dentro del soporte.

Este reemplazo es válido para infinitos huecos: parametrizamos por \(v+U\); las coordenadas son 1-Lipschitz. Sustituimos cada componente abierta del conjunto de parámetros fuera del soporte por una conexión monótona, parametrizada por el mismo \(v+U\). La curva resultante sigue siendo 1-Lipschitz. En el conjunto de visita retenido coincide con la original y sus derivadas coinciden casi por doquier. Los tramos añadidos tienen acción no negativa.

Así, los funcionales recortados coinciden con supremos de tiempo propio en sus soportes. Al retirar el corte, la cota determinista de §4.2 da la misma identificación para \(e(\xi)\) e \(i(\xi)\).

Toda curva en \(D\) es pura o se descompone en un tramo exterior, un posible tramo sobre \(r=s\) de tiempo propio cero y un tramo interior. En el caso cruzado, podemos elegir \(\xi\) entre el primer y el último valor de \(v\) sobre el horizonte. Entonces su tiempo propio no excede \(e(\xi)+i(\xi)\). Para una curva pura basta uno de los perfiles.

Recíprocamente, tomamos curvas casi óptimas en los dos soportes que definen \(e(\xi)\) e \(i(\xi)\). Sus extremos a concatenar satisfacen \(v_{\rm ext}\le\xi\le v_{\rm int}\), luego admiten el conector futuro dentro de \(D\) construido en B.2. Su tiempo propio es no negativo. Si un soporte es vacío, se conserva la curva pura. Por tanto,
\[
\tau_D=\max_{\xi\in J}[e(\xi)+i(\xi)].
\]
Para \(\xi\in(a,b)\), ambos soportes contienen puntos de sus respectivos bloques; el mismo argumento construye curvas que efectivamente cruzan, incluso si uno de los supremos es cero, utilizando un punto como tramo degenerado. La continuidad de \(e+i\) permite aproximar los extremos \(a,b\) por umbrales interiores. Toda curva cruzada cruza \(r=s\) a un tiempo entre \(t_0\) y \(t_1\), por lo que el umbral correspondiente está en \([a,b]\). Concluimos
\[
\tau_D^{\rm cross}=\max_{\xi\in[a,b]}[e(\xi)+i(\xi)].
\]
Esto completa la identificación geométrica y la prueba del Teorema 1. La distancia utilizada está restringida a la caja; no se sustituye por la distancia lorentziana ambiente.

## 5. No-go B: demostración del Teorema 2

### Lema B.1 (volumen)

La matriz de \(2Q_e\,dU\,dV\) tiene determinante \(-Q_e^2\), luego

\[
d\operatorname{vol}_{g_e}=Q_e\,|dU\,dV|.
\]

La naturalidad del volumen bajo las isometrías de todo \(U_0\) da

\[
\varphi_H^*d\operatorname{vol}_{g_H}
=\varphi_0^*d\operatorname{vol}_{g_0}
=d\operatorname{vol}_{g_{U_0}}.
\]

Como \(\det g_{U_0}=-1\) en \((t^*,r)\), sobre \(D\) obtenemos exactamente

\[
\boxed{
d\operatorname{vol}_{e_H}|_D
=d\operatorname{vol}_{e_0}|_D
=d\operatorname{vol}_{g_{U_0}}|_D
=|dt^*\,dr|.}
\]

### Lema B.2 (no atajos)

La monotonía global prueba, para cualquiera de los dos testigos,

\[
p\prec_e q\Longrightarrow U_p\le U_q,\quad V_p\le V_q.
\]

**Rectángulo ambiente.** Si \(p,q\in\Phi(D)\) son comparables coordenadamente, cualquier \((U,V)\) de su rectángulo de orden satisface

\[
0<V_p\le V\le V_q.
\]

Si \(U\le0\), entonces \(UV\le0<1\). Si \(U>0\), entonces \(U\le U_q\) y

\[
UV\le U_qV_q<1.
\]

Por tanto,

\[
[U_p,U_q]\times[V_p,V_q]\subset\Omega.
\]

Esto acredita accesibilidad en Schwarzschild ambiente, pero no presupone que el rectángulo esté en \(\Phi(U_0)\). Para probar la relación intrínseca en \(U_0\), construimos una curva dentro de \(D\).

**Dos extremos exteriores.** Sea

\[
R(r)=r+2s\log(|r-s|/s),\qquad
w=t^*-R(r),\qquad \psi(r)=r+R(r).
\]

En el exterior,

\[
U=-e^{-w/(2s)},\qquad v-w=\psi(r),\qquad \psi'(r)=2/f>0.
\]

La comparabilidad implica que \(v,w\) no disminuyen. Unimos los extremos por el segmento en \((v,w)\). Como \(v-w\) es afín y \(r=\psi^{-1}(v-w)\), el radio permanece entre los radios extremos. Escribiendo \(T_*(v,w)=t^*\),

\[
\frac{\partial T_*}{\partial v}=1-\frac f2>0,
\qquad \frac{\partial T_*}{\partial w}=\frac f2>0.
\]

El tiempo también permanece entre sus valores extremos. El segmento creciente representa una curva causal futura enteramente contenida en \(D\).

**Dos extremos interiores.** Tomamos ahora

\[
w=R(r)-t^*,\qquad U=e^{w/(2s)},\qquad v+w=\psi(r),
\qquad \psi'(r)=2/f<0.
\]

El segmento creciente en \((v,w)\) mantiene el radio entre los valores extremos porque \(v+w\) es afín y \(\psi\) es estrictamente decreciente. Además,

\[
\frac{\partial T_*}{\partial v}=1-\frac f2>0,
\qquad \frac{\partial T_*}{\partial w}=-\frac f2>0.
\]

El tiempo permanece entre los valores extremos y la curva está en \(D\). Estos argumentos se aplican a cada par fijo; no usan uniformidad de las cartas antiguas al acercarse al horizonte.

**Cruce y extremos en el horizonte.** Los casos comparables restantes satisfacen

\[
r_p\ge s\ge r_q,\qquad v_p\le v_q.
\]

Primero aumentamos \(v\) desde \(v_p\) hasta \(v_q\) a radio constante \(r_p\). Este tramo es causal futuro porque \(f(r_p)\ge0\); cuando \(r_p=s\), es nulo. Después disminuimos \(r\) desde \(r_p\) hasta \(r_q\), manteniendo \(v=v_q\): es un rayo nulo entrante futuro. Los tramos de longitud cero se omiten. En todo el recorrido,

\[
t_p=v_p-r_p\le v_q-r_p\le v_q-r_q=t_q,
\qquad r_q\le r\le r_p.
\]

Así, ambos tramos quedan dentro de \(D\). Esto incluye dos extremos sobre el horizonte. La salida desde el interior al horizonte o al exterior es incompatible con \(U_p\le U_q\).

Hemos demostrado para todos los puntos distintos de \(D\), incluidos los del horizonte,

\[
U_p\le U_q,\quad V_p\le V_q
\Longrightarrow p\prec_{U_0}q.
\]

La isometría temporalmente orientada lleva cualquier curva causal de \(U_0\) a ambos testigos. En consecuencia,

\[
\boxed{p\prec_{e_H}q\iff p\prec_{U_0}q\iff p\prec_{e_0}q
\quad\text{para todo }p,q\in D.}
\]

Una curva que salga de \(\varphi_e(U_0)\) y regrese sigue sometida a la monotonía global. Si conecta dos puntos observados, estos ya admiten la conexión construida dentro de \(D\); salir no crea una relación nueva. No afirmamos que todas las curvas permanezcan en \(U_0\), ni que \(D\) sea causalmente convexo.

### Lema B.3 (horizonte global)

#### Testigo \(e_H\): dos componentes de infinito nulo futuro

En el exterior derecho \(U<0,V>0\), definimos

\[
u_R=-2s\log(-U)
=v-2r-2s\log(r/s-1),\qquad x=1/r.
\]

Sustituyendo en la métrica,

\[
g_H=f\,du_R^2+2\,du_R\,dr.
\]

El factor conforme \(\omega_H=1/r\), positivo en todo \(M_H\), da en este extremo

\[
\widetilde g_H=\omega_H^2g_H
=(x^2-sx^3)\,du_R^2-2\,du_R\,dx.
\]

Adjuntamos, mediante esta carta para \(r>2s\),

\[
\mathscr I_R^+=\{x=0,\ u_R\in\mathbb R\}.
\]

La métrica conforme es suave y no degenerada en la frontera, con determinante \(-1\). Allí \(\omega_H=0\), \(d\omega_H=dx\ne0\) y

\[
\widetilde g_H^{-1}(dx,dx)=-(x^2-sx^3)=0.
\]

La frontera es nula; la dirección saliente futura tiene \(u_R\) constante y \(x\) decreciente. Los rayos \(u_R\) constante tienen \(r\) como parámetro afín físico, pues \(\Gamma^a_{rr}=0\) en \((u_R,r)\); alcanzan \(r\to\infty\) con parámetro afín futuro infinito.

En el exterior izquierdo \(V<0,U>0\), la simetría \(U\leftrightarrow V\) da la misma construcción con

\[
u_L=-2s\log(-V),\qquad x=1/r,\qquad
\mathscr I_L^+=\{x=0,\ u_L\in\mathbb R\}.
\]

Los dos extremos son disjuntos; estas cartas adjuntan una frontera conforme suave con

\[
\mathscr I_H^+=\mathscr I_R^+\sqcup\mathscr I_L^+.
\]

Si \(U_p<0\), el rayo \(U=U_p\), \(V\uparrow\infty\), permanece en \(M_H\), ya que \(U_pV\) disminuye desde un valor menor que uno. Alcanza \(\mathscr I_R^+\). Si \(V_p<0\), el rayo \(V=V_p\), \(U\uparrow\infty\), alcanza \(\mathscr I_L^+\).

Si \(U_p,V_p\ge0\), ninguna curva futura puede adquirir una coordenada negativa. Para terminar en \(\mathscr I_R^+\) tendría que entrar en el exterior derecho, donde \(U<0\); para terminar en \(\mathscr I_L^+\), en el izquierdo, donde \(V<0\). Ambas posibilidades están excluidas. Por tanto,

\[
\boxed{J^-_{M_H}(\mathscr I_H^+)=\{U<0\}\cup\{V<0\}.}
\]

La frontera relativa a \(M_H\) es

\[
\mathcal H^+(e_H)
=\{U=0,V\ge0\}\cup\{V=0,U\ge0\}.
\]

En \(\Omega\), donde \(V>0\), esta frontera es exactamente \(\{U=0\}\). Como \(U=0\iff r=s\) en la región observada,

\[
\boxed{\varphi_H(\Sigma_S)\subset\mathcal H^+(e_H).}
\]

El lado exterior observado alcanza \(\mathscr I_H^+\); el interior y el propio horizonte no la alcanzan.

#### Testigo \(e_0\): infinito nulo futuro Minkowskiano

Definimos

\[
a=\arctan U,\qquad b=\arctan V,\qquad
\omega_0=\frac{\cos a\cos b}{\sqrt c}.
\]

Entonces

\[
\widetilde g_0=\omega_0^2g_0
=2\frac{Q_0(\tan a,\tan b)}c\,da\,db.
\]

La imagen del soporte de \(F\) es compacta dentro del cuadrado abierto \((-\pi/2,\pi/2)^2\). Cerca de los bordes, \(Q_0=c\), y la métrica conforme es exactamente \(2\,da\,db\). Se extiende suavemente al cuadrado cerrado sin sus cuatro vértices. Declaramos las dos componentes futuras

\[
\mathscr I_0^+
=\{a=\pi/2,\ -\pi/2<b<\pi/2\}
\ \sqcup\
\{b=\pi/2,\ -\pi/2<a<\pi/2\}.
\]

En ambas, \(\omega_0=0\), \(d\omega_0\ne0\), la métrica conforme es no degenerada y la frontera es nula. Es la compactificación nula de Minkowski 1+1 aplicada a los extremos exactamente planos de \(g_0\); véase como referencia de la construcción estándar [Tong, General Relativity, §4.3.3](https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S4.html).

Desde cualquier \(p=(U_p,V_p)\in M_0\) existe el rayo

\[
\boxed{\gamma_p(\lambda)=(U_p,V_p+\lambda),\qquad \lambda\ge0.}
\]

Su tangente es \(\partial_V\), nula y futura para \(g_0\). En coordenadas conformes,

\[
(a,b)\longrightarrow(\arctan U_p,\pi/2)\in\mathscr I_0^+.
\]

El rayo termina entrando en la zona exactamente plana y tiene parámetro afín físico futuro infinito. La frontera alcanzada es infinito nulo, no un corte a distancia finita. En consecuencia,

\[
\boxed{J^-_{M_0}(\mathscr I_0^+)=M_0,\qquad
\mathcal H^+(e_0)=\partial_{M_0}M_0=\varnothing.}
\]

El factor conforme positivo conserva exactamente los conos y las curvas causales; la causalidad fuerte fue probada en §3. No se ha eliminado \(\mathscr I^+\), truncado \(M_0\) ni impuesto ecuaciones de campo.

### 5.1. Ley exacta del poset, incluida cardinalidad

Después de B.1 y B.2, sea

\[
\mu=d\operatorname{vol}_{g_{U_0}}|_D,\qquad
A=\mu(D)=(t_1-t_0)(r_+-r_-).
\]

Ambos procesos restringidos a \(D\) tienen intensidad medida \(\rho\mu\). En particular,

\[
N\sim\operatorname{Poisson}(\rho A),\qquad
\Pr(N=n)=e^{-\rho A}\frac{(\rho A)^n}{n!}.
\]

Condicionado a \(N=n\), los puntos son independientes con distribución \(\mu/A\) en ambos casos. B.2 garantiza que cualquier configuración de puntos distintos induce las mismas relaciones, incluidos los pares que contienen puntos del horizonte.

Podemos usar una misma nube de Poisson en \(D\) y enviarla por \(\varphi_H\) y \(\varphi_0\). Bajo la identificación de sus puntos, los posets coinciden realización por realización; al olvidar etiquetas, sus clases de isomorfismo coinciden. Así,

\[
\boxed{\operatorname{Law}_{e_H}(P_\rho|_D)
=\operatorname{Law}_{e_0}(P_\rho|_D)\qquad\forall\rho>0.}
\]

Si se requieren procesos en los espaciotiempos completos, se añaden procesos independientes sobre los complementos de las imágenes de \(D\), con intensidad \(\rho\,d\operatorname{vol}_{g_e}\). Cada proceso global sigue siendo homogéneo respecto de su propio volumen.

### 5.2. Consecuencia minimax exacta

Sea \(\mathsf L_\rho\) la ley común del poset. Para cualquier test binario determinista,

\[
\begin{aligned}
\operatorname{error}_H+\operatorname{error}_0
&=\Pr_{e_H}(\delta_\rho=0)+\Pr_{e_0}(\delta_\rho=1)\\
&=\mathsf L_\rho(\delta_\rho=0)+\mathsf L_\rho(\delta_\rho=1)=1.
\end{aligned}
\]

Para un test aleatorizado, sea \(\alpha_\rho(P)\in[0,1]\) su probabilidad de devolver \(1\). La misma regla en ambos modelos da

\[
\operatorname{error}_H+\operatorname{error}_0
=\int(1-\alpha_\rho)\,d\mathsf L_\rho
+\int\alpha_\rho\,d\mathsf L_\rho=1.
\]

Por tanto, para todo \(\rho>0\),

\[
\boxed{\max\{\operatorname{error}_H,\operatorname{error}_0\}\ge\frac12.}
\]

La cota vale para cualquier test del poset y en cualquier clase de alternativas que contenga el par. No hay condicionamiento a cardinalidad fija ni paso al límite en \(\rho\).


## 6. Alcance e interpretación

Los dos teoremas tienen cuantificadores distintos. El primero describe un límite de alta intensidad dentro de la caja Schwarzschild conocida. El segundo construye un par fijo de extensiones que induce la misma ley para cada intensidad positiva. Aumentar la densidad mejora la aproximación de ciertos funcionales métricos, pero no distingue los dos predicados globales del Teorema 2.

El entorno preservado \(U_0\) es relativamente compacto y se fija antes de observar datos. No se exige conservar un parche Schwarzschild arbitrariamente extenso, en particular uno que alcance radios arbitrariamente próximos a cero. Tampoco se permite modificar la intensidad física del proceso para obtener la igualdad de leyes.

La clase de extensiones solo impone regularidad \(C^2\), orientación temporal, causalidad fuerte, isometría de \(U_0\) e infinito nulo futuro explícito. El par construido es suave. No se afirma que ambas extensiones satisfagan ecuaciones de Einstein, vacío, condiciones de energía, materia prescrita, analiticidad global o pertenencia obligatoria a la familia Schwarzschild/Kruskal.

La reconstrucción de la superficie distinguida \(r=r_S\) bajo una promesa previa de pertenencia a Schwarzschild es una pregunta diferente. Permanece abierta en este trabajo y no se necesita para ninguno de los dos teoremas. No se deduce un procedimiento para reconstruir la partición exterior/interior a partir del poset.

El resultado tampoco es un lema de extensión para gérmenes lorentzianos arbitrarios o para hipersuperficies nulas arbitrarias. No contiene un teorema en \(3+1\) dimensiones. La conclusión establecida es concreta: la geometría intrínseca recuperable dentro de una observación no determina, en la clase indicada, que su superficie Schwarzschild distinguida sea un horizonte de sucesos.

## Apéndice A. Transferencia compacta a cajas con umbral

Este apéndice recoge la transferencia usada en §4.3. Se fija primero un corte radial \(\epsilon>0\). Todas las constantes pueden depender de ese corte y de la caja.

### A.1. Geometría del soporte y control de sus fronteras

En las coordenadas antiguas de cada bloque, \(g=|f|\,dv\,dw\) y la densidad de volumen es \(q_{\rm old}=|f|/2\). En el exterior escribimos \(z=v-w\), y en el interior \(z=v+w\). En ambos casos \(r=h_{\rm bl}(z)\), \(h_{\rm bl}'=f/2\), y
\[
T_*(v,w)=v-h_{\rm bl}(z),\qquad
(T_{*,v},T_{*,w})=(1-f/2,|f|/2).
\]
En un entorno compacto del bloque, \(q_{\rm old}\) y su raíz son Lipschitz, están acotados y son estrictamente positivos. Ambas derivadas de \(T_*\) están acotadas inferiormente por una constante \(m>0\).

Los soportes recortados con umbral tienen la forma
\[
F_\xi=\{a_0\le z\le b_0,\ t_0\le T_*\le t_1,\
\sigma(v-\xi)\ge0\},
\]
con \(\sigma=-1\) en el exterior y \(\sigma=+1\) en el interior. Los extremos \(a_0,b_0\) son las imágenes ordenadas del intervalo radial recortado. Sean \(F_{\xi,+\eta}\) y \(F_{\xi,-\eta}\) los conjuntos obtenidos relajando o reforzando cada una de estas cinco desigualdades en \(\eta\).

El segmento entre dos puntos comparables de cualquiera de estos soportes conserva las cotas de \(z\), por afinidad, y las de \(T_*\) y \(v\), por monotonía. El reemplazo de huecos descrito en §4.4 prueba que el funcional del orden inducido coincide con el supremo sobre curvas contenidas en cada soporte.

La acción en una franja vertical de anchura \(\ell\) se acota por
\[
\sqrt{M\ell W_w},
\]
y en una horizontal por \(\sqrt{M\ell W_v}\). En una franja temporal de anchura \(\ell\), la desigualdad \(dT_*\ge m(dv+dw)\) controla la acción por una constante por \(\ell\). En el interior, \(z=v+w\) proporciona también ese control lineal para las franjas radiales.

Para las paredes radiales exteriores usamos un recorte explícito. Escribimos \(u=v+w\), \(d=v-w\) y
\[
c_\eta(d)=\operatorname{clip}_{[a_0+\eta,b_0-\eta]}d,
\qquad
(v,w)\mapsto
\left(\frac{u+c_\eta(d)}2,\frac{u-c_\eta(d)}2\right).
\]
Para \(\eta\) pequeño, cada coordenada cambia a lo sumo \(\eta\). Como
\[
|(c_\eta\circ d)'|\le|d'|\le u',
\]
las nuevas coordenadas siguen siendo no decrecientes y
\[
\dot v_\eta\dot w_\eta
=\frac{u'^2-(c_\eta\circ d)'^2}{4}
\ge\frac{u'^2-d'^2}{4}
=\dot v\dot w.
\]
Antes de aplicar el recorte, retenemos la porción que satisface
\[
t_0+(H+1)\eta\le T_*\le t_1-(H+1)\eta,\qquad
v\le\xi-2\eta,
\]
donde \(H\ge1\) es una constante Lipschitz de \(T_*\) en norma infinito. La porción retenida es un intervalo de parámetros. Después del recorte queda en \(F_{\xi,-\eta}\).

La acción eliminada está en dos franjas temporales de anchura \((H+2)\eta\) y una franja en \(v\) de anchura \(3\eta\). Las cotas anteriores dan una pérdida \(O(\sqrt\eta)\). La variación de \(\sqrt{q_{\rm old}}\) bajo el recorte aporta \(O(\eta)\); el producto de derivadas no disminuye.

En el interior basta retener
\[
a_0+\eta\le v+w\le b_0-\eta,\qquad
t_0+\eta\le T_*\le t_1-\eta,\qquad
v\ge\xi+\eta.
\]
Todas estas restricciones son monótonas a lo largo de la curva. Lo descartado queda en dos franjas radiales, dos temporales y una nula, con la misma cota \(O(\sqrt\eta)\). Si la porción retenida es vacía, toda la acción está en la unión de esas franjas y satisface la misma estimación.

Así, escribiendo \(\mathcal V_{\rm old}\) para el funcional en \((v,w)\),
\[
0\le
\mathcal V_{\rm old}(q_{\rm old}\mathbf1_{F_{\xi,+\eta}})
-\mathcal V_{\rm old}(q_{\rm old}\mathbf1_{F_{\xi,-\eta}})
\le C_\epsilon\sqrt\eta.
\]

### A.2. Aproximación rectangular

Fijamos una rejilla de diámetro máximo \(h\) en un rectángulo ambiente. Sean \(R_h^-\) la unión de celdas cuyas clausuras están en \(F_\xi\), y \(R_h^+\) la unión de celdas cuyas clausuras lo intersectan. Las cinco funciones de frontera son Lipschitz en un entorno compacto. Para una constante \(H_0\) común y \(\eta=2H_0h\),
\[
F_{\xi,-\eta}\subset R_h^-\subset F_\xi
\subset R_h^+\subset F_{\xi,+\eta}.
\]
En las celdas interiores ponemos el ínfimo de \(q_{\rm old}\); en las exteriores activas, el supremo; en las demás, cero. Denotamos los pesos escalonados por \(a_h^-,a_h^+\). Se usa la fórmula geométrica de \(q_{\rm old}\) en un entorno real de las celdas activas. Entonces
\[
a_h^-\le q_{\rm old}\mathbf1_{F_\xi}\le a_h^+
\quad\text{casi por doquier},
\]
\[
\mathcal V_{\rm old}(a_h^+)-\mathcal V_{\rm old}(a_h^-)
\le C_\epsilon\sqrt h.
\]
La oscilación de la raíz del peso en cada celda aporta \(O(h)\); el control de frontera procede de A.1. Las convenciones en las aristas de la rejilla son irrelevantes para el Poisson y para la acción, pues una curva sobre una arista horizontal o vertical tiene producto de derivadas cero casi por doquier allí.

### A.3. Rectángulos suaves, poissonización y pesos escalonados

Para un peso \(b\) suave y positivo en un rectángulo, normalizamos por \(m_b=\int b\) y reescalamos al cuadrado unidad. El Teorema 2(i) de [DZ95] da
\[
\frac{H_n}{\sqrt n}\xrightarrow{\mathbb P}
\frac{2\mathcal V_{\rm old}(b)}{\sqrt{m_b}}.
\]
La forma paramétrica del funcional coincide con la forma gráfica del teorema: aproximaciones poligonales monótonas y continuidad uniforme del peso permiten pasar entre ambas, mientras los tramos horizontales o verticales aportan cero.

Condicionado a \(N\sim\operatorname{Poisson}(\rho m_b)\), la nube consta de \(N\) puntos independientes de densidad \(b/m_b\). Para \(n\ge n_0\), las probabilidades de desviación son uniformemente pequeñas por la definición de convergencia; la mezcla añade a lo sumo \(\Pr(N<n_0)\). Usando \(N/\rho\to m_b\) en probabilidad,
\[
\frac{H_\rho(b)}{\sqrt\rho}\xrightarrow{\mathbb P}
2\mathcal V_{\rm old}(b).
\]

Extendemos esta afirmación a un peso \(a\ge0\) constante en finitísimas celdas rectangulares.

Para la cota inferior, fijamos una curva monótona casi óptima. Visita el interior de cada celda en un único intervalo. Si entra en \(p\) y sale en \(q\) de una celda de peso \(c\), su acción allí no excede
\[
\sqrt{c(q_v-p_v)(q_w-p_w)}.
\]
Un rectángulo ligeramente recortado entre esos extremos tiene altura homogénea normalizada arbitrariamente próxima al doble de esa cantidad. Los rectángulos pueden recortarse preservando que todos los puntos de cada uno precedan a todos los del siguiente. Concatenamos sus cadenas máximas y aplicamos el límite homogéneo a los finitísimos rectángulos. Esto da la cota inferior \(2\mathcal V_{\rm old}(a)\).

Para la cota superior, elegimos funciones suaves \(\chi_{Q,\delta}\) iguales a uno en cada celda cerrada \(Q\), entre cero y uno, y soportadas en su engrosamiento por \(\delta\). Definimos
\[
b_\delta=\delta+\sum_Qc_Q\chi_{Q,\delta}.
\]
Es suave, positivo y mayoriza \(a\) casi por doquier. Fuera de franjas de anchura \(2\delta\) alrededor de las líneas de la rejilla coincide con \(a+\delta\). La cota de acción en franjas y
\(\sqrt{a+\delta}-\sqrt a\le\sqrt\delta\) dan
\[
0\le\mathcal V_{\rm old}(b_\delta)-\mathcal V_{\rm old}(a)
\le C_{\rm rejilla}\sqrt\delta.
\]
El acoplamiento por dominación Poisson y el resultado suave, primero con \(\delta\) fijo y después \(\delta\downarrow0\), prueban la cota superior. Por tanto, el límite vale para estos pesos escalonados.

### A.4. Cierre de la transferencia compacta

Acoplamos por dominación los procesos de A.2. Sus alturas satisfacen
\[
H_\rho(a_h^-)\le
H_\rho(q_{\rm old}\mathbf1_{F_\xi})
\le H_\rho(a_h^+).
\]
Para una tolerancia dada fijamos primero \(h\) con error variacional pequeño, y después llevamos \(\rho\) a infinito usando A.3. Resulta
\[
\frac{H_\rho(q_{\rm old}\mathbf1_{F_\xi})}{\sqrt{2\rho}}
\xrightarrow{\mathbb P}
\sqrt2\,\mathcal V_{\rm old}(q_{\rm old}\mathbf1_{F_\xi}).
\]
Los casos vacíos o degenerados quedan cubiertos por el mismo emparedado.

En cada bloque recortado, el cambio creciente \(w\mapsto U\) es suave con inversa suave. Sus densidades satisfacen
\[
q(v,U)\frac{dU}{dw}=q_{\rm old}(v,w),
\]
de modo que conserva exactamente la acción y transforma curvas monótonas en curvas monótonas. El límite es, por tanto, el correspondiente \(e_\epsilon(\xi)\) o \(i_\epsilon(\xi)\) utilizado en §4.3.

## Referencias

[DZ95] Jean-Dominique Deuschel y Ofer Zeitouni. *Limiting Curves for I.I.D. Records*. The Annals of Probability **23**(2), 852–878 (1995). [DOI: 10.1214/aop/1176988293](https://doi.org/10.1214/aop/1176988293). Se utiliza el Teorema 2(i), p. 855, con densidad suave positiva; las extensiones de soporte y poissonización se prueban en el apéndice A.

[Tong] David Tong. *General Relativity*, §4.3.3, diagramas de Penrose y compactificación conforme de Minkowski. [Notas del autor](https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S4.html). Se usa como referencia de contexto para la construcción explícita de §5.
