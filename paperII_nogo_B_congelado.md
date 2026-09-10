# Paper II — Núcleo congelado: Teorema positivo + No-go B

Fecha de congelación inicial: 2026-09-09.
Corrección del contrato local y cierre de B: 2026-09-10.
Alcance: Schwarzschild 1+1 y el par explícito de este documento. No generalizar a gérmenes arbitrarios. No interpolar métricas lorentzianas arbitrarias. No tratar A como teorema.

```text
NOGO_B=CLOSED
PAPER_II_SCIENTIFIC_CORE=CLOSED
PROBLEMA_A=OPEN_NOT_REQUIRED
```

El cierre de B corresponde al contrato corregido con un entorno relativamente compacto \(U_0\). El estado del teorema positivo se conserva del núcleo anterior; esta actualización incorpora la prueba de B y no constituye una nueva auditoría del teorema positivo. Paper II sale de investigación activa salvo que una revisión independiente encuentre un fallo.

---

## 0. Objetos fijos

Fijamos \(s=r_S>0\) y la caja Schwarzschild 1+1 del repositorio:

\[
D=[t_0,t_1]\times[r_-,r_+],\qquad
t_0<t_1,\qquad 0<r_-<s<r_+.
\]

La métrica local, con signatura \((+,-)\), es

\[
g=f\,d{t^*}^2-2(1-f)\,dt^*dr+(f-2)\,dr^2,
\qquad f=1-\frac sr,\qquad \det g=-1.
\]

Sea \(\Phi:(t^*,r)\mapsto(U,V)\) la carta regular definida en §3.0, cuya imagen para \(r>0\) es

\[
\Omega=\{(U,V)\in\mathbb R^2:V>0,\ UV<1\}.
\]

El dato local preservado es la restricción Schwarzschild \(g_{U_0}\) a un entorno abierto **fijado antes de los datos** tal que

\[
\overline D\subset U_0,\qquad
K:=\Phi(\overline{U_0})\Subset\Omega.
\]

El símbolo \(U_0\) designa el entorno; \(U\) designa exclusivamente la coordenada nula. No se exige preservar un entorno Schwarzschild arbitrariamente grande. Esta es la corrección de la formulación inicial, que exigía una isometría de un entorno \(U\) entero sin controlar su extensión: la compacidad de \(\overline D\) no justificaba ese requisito. Aquí se preserva exactamente todo \(U_0\).

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

---

## 1. Teorema positivo (embedding / modelo Schwarzschild conocido)

\[
\frac{H(P_\rho)}{\sqrt{2\rho}}\xrightarrow{\mathbb{P}}\tau_D,
\qquad
\frac{L_{\mathrm{cross}}}{\sqrt{2\rho}}\xrightarrow{\mathbb{P}}\tau_D^{\mathrm{cross}}.
\]

El causal set recupera cantidades métricas intrínsecas de la región observada. Esto no identifica \(\mathcal{H}^+\).

---

## 2. No-go B (dato local Schwarzschild fijo, par explícito)

**Teorema B.** Existen dos extensiones fijas \(e_H\) y \(e_0\) del mismo dato local \((U_0,g_{U_0})\), elegidas antes de los datos, tales que

\[
\prec_{e_H}\big|_{D\times D}
=
\prec_{U_0}\big|_{D\times D}
=
\prec_{e_0}\big|_{D\times D},
\qquad
\mathrm{vol}_{e_H}\big|_D
=
\mathrm{vol}_{e_0}\big|_D
=\mathrm{vol}_{g_{U_0}}\big|_D,
\]
pero
\[
\varphi_H(\Sigma_S)\subset\mathcal{H}^+(e_H),
\qquad
\mathcal{H}^+(e_0)=\varnothing.
\]

Entonces, para todo \(\rho>0\),

\[
\operatorname{Law}_{e_H}(P_\rho|_D)
=
\operatorname{Law}_{e_0}(P_\rho|_D).
\]

Para cualquier decisión binaria \(\delta_\rho\) medible respecto de \(P_\rho|_D\), con \(1\) indicando la alternativa con horizonte y \(0\) la alternativa sin horizonte,

\[
\Pr_{e_H}(\delta_\rho=0)+\Pr_{e_0}(\delta_\rho=1)=1,
\]
y por tanto
\[
\max\bigl\{\Pr_{e_H}(\mathrm{error}),\Pr_{e_0}(\mathrm{error})\bigr\}\ge\tfrac12.
\]

Es un no-go exacto para cada \(\rho>0\), con cardinalidad Poisson aleatoria incluida. No condiciona a un \(N=n\) fijo, no cambia la intensidad física homogénea y no depende de un límite asintótico. Incluye tests aleatorizados con una regla común de aleatorización.

---

## 3. Testigos y demostración de B.1–B.3

### 3.0. Carta regular y métrica exacta

Fuentes locales: [reducción double-null, §§1–3](dev/PAPER2_DOUBLE_NULL_REDUCTION.md), [carta regular, §3](dev/PAPER2_HORIZON_THRESHOLD_LIMIT.md) y [accesibilidad por bloques, §§2–3](dev/PAPER2_E2_RECTANGULAR_APPROXIMATION.md). Las identidades geométricas utilizadas se desarrollan aquí; no se usa ningún límite probabilístico de esas notas.

Definimos

\[
v=t^*+r,\qquad
U=\left(1-\frac rs\right)e^{r/s-v/(2s)},\qquad
V=e^{v/(2s)}>0.
\]

La sustitución \(dt^*=dv-dr\) en la métrica de §0 da

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

### 3.1. Definición del par y admisibilidad

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

### Lema B.1 (volumen) — PASS

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

### Lema B.2 (no atajos) — PASS

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

Una curva que salga de \(\varphi_e(U_0)\) y regrese sigue sometida a la monotonía global. Si conecta dos puntos observados, estos ya admiten la conexión construida dentro de \(D\); salir no crea una relación nueva. No afirmamos que todas las curvas permanezcan en \(U_0\), ni que \(D\) sea causalmente convexo. La frase de la lista inicial que prohibía toda salida era más fuerte que B.2 y queda sustituida por esta equivalencia demostrada.

### Lema B.3 (horizonte global) — PASS

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

El factor conforme positivo conserva exactamente los conos y las curvas causales; la causalidad fuerte fue probada en §3.1. No se ha eliminado \(\mathscr I^+\), truncado \(M_0\) ni impuesto ecuaciones de campo.

### 3.2. Ley exacta del poset, incluida cardinalidad — PASS

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

### 3.3. Consecuencia minimax exacta — PASS

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

---

## 4. Lo que el teorema no afirma

El resultado cubre la clase de extensiones \(C^2\), temporalmente orientadas y fuertemente causales, que preservan isométricamente el \(U_0\) relativamente compacto fijado en §0 y poseen infinito nulo futuro explícito. El par construido es suave. No se afirma que el par pertenezca a subclases definidas por ecuaciones de Einstein, vacío, materia prescrita, condiciones de energía, analiticidad global o pertenencia obligatoria a Schwarzschild/Kruskal.

- Nada sobre preservar un entorno Schwarzschild arbitrariamente grande o que alcance \(r\to0\).
- Nada sobre un germen lorentziano arbitrario.
- Nada sobre una hipersuperficie nula \(\Sigma\subset D\) arbitraria convertida en horizonte por un problema característico.
- Nada sobre interpolaciones del tipo \(g_\varepsilon=(1-\chi)g_{U_0}+\chi g_{\mathrm{Schw}}\). Esa combinación no es automáticamente lorentziana; la causalidad fuerte no se hereda por “apertura de conos” sin comprobación.
- Nada sobre las clases Einstein / vacío+esférico / analítico / Kruskal como cadena de inclusiones. Son restricciones distintas; se intersectan.

---

## 5. Problema A (abierto, no es un teorema de este paper)

\[
P_\rho\big|_D \longrightarrow \Sigma_S=\{r=r_S\}
\]
bajo la promesa previa de pertenencia a una familia Schwarzschild.

Si A se resuelve más adelante, no contradice B: A reconstruye una superficie distinguida *dentro de una familia parametrizada*; B dice que los datos de \(D\) no certifican que esa superficie sea un horizonte de sucesos en una clase más amplia de extensiones.

No desarrollar un “lema de extensión universal” como dependencia de Paper II.

---

## 6. Frase arquitectónica

El causal set puede recuperar geometría intrínseca de una región sin que esa geometría determine su significado causal global.

Reservar “horizonte” y “localización del horizonte” para \(\mathcal{H}^+\) y para el No-go B. Para A usar “superficie Schwarzschild distinguida” o “lugar \(r=r_S\) reconstruido”.

---

## 7. Cierre y congelación

La auditoría escrita del 2026-09-10, incorporada en §3, cierra las obligaciones para el contrato corregido:

| Obligación | Estado | Prueba |
|---|---|---|
| Extensiones isométricas de todo \(U_0\), suaves y temporalmente orientadas | PASS | §§3.0–3.1 |
| Causalidad fuerte de ambos testigos | PASS | §3.1 |
| B.1: igualdad exacta de volumen | PASS | Lema B.1 |
| B.2: ninguna relación observada nueva por excursiones fuera de \(U_0\) | PASS | Lema B.2 |
| B.3: dos infinitos nulos futuros explícitos y predicados globales opuestos | PASS | Lema B.3 |
| Ley exacta, cardinalidad y acoplamiento por la misma nube | PASS | §3.2 |
| Identidad de errores y cota minimax para cada \(\rho>0\) | PASS | §3.3 |

```text
PAPER_II_NOGO_B_AUDIT=PASS
FIRST_POINT_OF_FAILURE=NONE
NOGO_B=CLOSED
PAPER_II_SCIENTIFIC_CORE=CLOSED
PROBLEMA_A=OPEN_NOT_REQUIRED
```

Este cierre registra una demostración geométrica y probabilística escrita; no se presenta como una formalización Lean del No-go B ni como un resultado de simulaciones. Se conserva el teorema positivo de §1 y se mantiene A abierto, sin convertirlo en dependencia del cierre. La investigación activa de Paper II queda cerrada salvo hallazgo de un fallo por revisión independiente.
