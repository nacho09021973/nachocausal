# Direcciones visibles en órdenes causales finitos

José Ignacio Martín Gandul

Autor de correspondencia: jmartin596@alumno.uned.es

## Resumen

Estudiamos un modelo de interacción conforme explícito en $1+1$ dimensiones sobre un diamante causal, al que llamamos modelo S1, a través de su canal de orden causal no etiquetado, desarrollado en torno a una geometría de referencia independiente. Para cada cardinalidad $N$ determinamos exactamente qué perturbaciones de primer orden sobreviven al paso de la cópula continua a la ley del orden causal no etiquetado. La respuesta es $V_N=\operatorname{Sym}^2P_{N-1}$, donde $P_{N-1}\subset L^2_0([0,1])$ está generado por los primeros $N-1$ modos de Legendre desplazados y centrados. Estos espacios visibles tienen dimensión $\binom N2$, están estrictamente encajados y tienen unión densa en el espacio de Hilbert simétrico de interacción. El diferencial del score factoriza como $D\mathscr S_N=B_NP_N^{\rm vis}$ con $B_N$ inyectivo, de modo que su núcleo es el complemento ortogonal simétrico de $V_N$ junto con todo el sector antisimétrico. Visibilidad y resolución estadística son cuestiones distintas: el operador de Fisher sobre $V_N$ es definido positivo pero anisótropo, y no tiene por qué ser diagonal en la base modal; normalizado por $N$ observaciones continuas de la cópula converge a la proyección simétrica en la topología fuerte de operadores, pero no en norma de operador. Una órbita exponencial antisimétrica explícita tiene una ley finita de posets par cuyo primer jet no nulo es exactamente de orden dos para todo $N\ge2$.

## 1. Introducción

En todo el trabajo, S1 designa la configuración concreta que aquí se estudia: un diamante causal plano de $1+1$ dimensiones en coordenadas nulas, dotado del orden causal producto y de una medida de referencia uniforme, perturbado por exponenciales conformes normalizadas en volumen y observado únicamente a través del orden causal no etiquetado de un sprinkling condicionado a su cardinalidad. §2 lo hace preciso.

En este modelo, ¿qué componentes de una perturbación conforme siguen siendo visibles tras pasar de la cópula continua a la ley de orden causal no etiquetado a cardinalidad fija $N$?

El objeto en cuestión se debe a [Bombelli2000]: la ley completa de un poset causal no etiquetado a cardinalidad fija $N$, muestreado a partir de una geometría lorentziana. [Janson2011] aporta el marco límite de núcleos de posets y leyes finitas consistentes en el que se inscribe la construcción, y [Surya2026] ofrece un relato afín, mediante abundancias esperadas de intervalos, de cómo el aumento de $N$ levanta degeneraciones. Ninguno de los tres calcula el diferencial de la ley a $N$ finito en una geometría de referencia.

Dos ingredientes de una respuesta existen en literaturas contiguas. Al nivel de las permutaciones *etiquetadas*, y no de los posets bidimensionales *no etiquetados*, el diferencial de un estadístico de patrones de permutación en torno a la referencia uniforme se conoce bien: [EvenZohar2020] descompone las densidades de patrones mediante la teoría de representaciones de $S_N$ y aísla el bloque de la representación estándar realizado a través de matrices de permutación comprimidas a $\mathbf1^\perp$, y [Kurecka2022] deriva la densidad de patrones directamente en una base de tipo Bernstein sobre $E_N=\mathbf1^\perp$. En forma matricial los dos niveles están separados por

$$
\mathbb R^{\mathcal C_N}
\xrightarrow{\ J_N\ }
\mathbb R^{S_N}
\xrightarrow{\ T_N\ }
\operatorname{End}(E_N),
\qquad
J_Ne_C=\mathbf1_{\Gamma_C},
\qquad
T_N(t)=\Bigl.\sum_{\pi\in S_N}t_\pi P_\pi\Bigr|_{E_N},
\tag{1.1}
$$

donde $\mathcal C_N$ indexa las clases de posets bidimensionales no etiquetados y $\Gamma_C\subset S_N$ es la fibra de $C$. La aplicación gradiente de Kurečka tiene núcleo $\ker T_N$. El cociente por el orden causal restringe el dominio al subespacio constante sobre fibras $\operatorname{im}J_N$; lo que hace falta es la *imagen* de esa restricción. El módulo objetivo abstracto también es clásico — [Diaconis1989] da $M^{(N-2,2)}\simeq S^{(N)}\oplus S^{(N-1,1)}\oplus S^{(N-2,2)}$ de dimensión $\binom N2$ para efectos de pares no ordenados sobre rankings — y lo es igualmente la correspondencia entre permutaciones y posets, cuyas fibras describen [BayoumiElZaharKhamis1994].

Queda sumar el diferencial a nivel de permutaciones sobre estas fibras y preguntar qué generan las sumas de clase. Para todo $N\ge2$ generan el módulo objetivo simétrico completo,

$$
\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}
=V_N=\operatorname{Sym}^2P_{N-1},
\qquad
\dim V_N=\binom N2,
$$

equivalentemente $T_N(\operatorname{im}J_N)=\operatorname{Sym}(E_N)$. El Teorema 1 de §4 lo demuestra de forma constructiva para todo $N$, sin enumerar posets. Del generado se siguen el núcleo exacto, el cociente identificable y la factorización $D\mathscr S_N=B_NP_N^{\rm vis}$ con $F_N=B_N^*B_N$ definido positivo sobre $V_N$ (§5), junto con el encaje estricto $V_N\subsetneq V_{N+1}$ y la densidad de $\bigcup_NV_N$ en el sector simétrico.

El generado zanja qué direcciones sobreviven, no con qué fuerza las codifica la ley. En el sector simétrico de Hilbert–Schmidt fijo la información de Fisher se retiene asintóticamente: normalizada por $N$ observaciones continuas de la cópula, $\widehat F_N\to\Pi_{\rm sym}$ en la topología fuerte de operadores, y no en norma (§6). Una órbita antisimétrica explícita tiene $r_N(\gamma_\psi)=2$ para todo $N\ge2$ — invisible a primer orden, detectada a segundo (§7) —, un enunciado de existencia para un único testigo, no una clasificación del sector antisimétrico.

Todo esto concierne al modelo S1 en un diamante causal de $1+1$ dimensiones, a primer orden, o a segundo orden en §7, en torno al punto de referencia independiente. Ningún enunciado de aquí concierne a dimensiones superiores, espaciotiempos lorentzianos generales, Schwarzschild u horizontes, identificabilidad no lineal a distancia finita, o reconstrucción de una geometría a partir de un causet; §9 consigna los límites con precisión.

## 2. El modelo S1 y el canal finito de orden causal

Trabajamos en el diamante causal plano de $1+1$ dimensiones en coordenadas nulas, reparametrizado a $D=[0,1]^2$ con el orden producto $(u,v)\preceq(u',v')\iff u\le u',\ v\le v'$ y la medida de referencia uniforme $\mu_0(du\,dv)=du\,dv$. Un generador conforme $\psi\in C(D;\mathbb R)$ define la familia exponencial que preserva el volumen

$$
g_\varepsilon=\frac{e^{2\varepsilon\psi}}{Z(\varepsilon)}\,g_0,
\qquad
Z(\varepsilon)=\int_De^{2\varepsilon\psi}\,d\mu_0,
\tag{2.1}
$$

cuya densidad de muestreo para un sprinkling de Poisson condicionado a $N$ puntos es $q_\varepsilon=e^{2\varepsilon\psi}/Z(\varepsilon)$. Derivando en $\varepsilon=0$ se obtiene $\dot g_0=2(\psi-\bar\psi)g_0$.

Mantenemos separados cuatro objetos a lo largo de la cadena que va de la geometría al estadístico: el generador $\psi$; la log-tangente $t_\psi=2(\psi-\bar\psi)$ de la densidad conjunta normalizada; la tangente de la densidad de la cópula obtenida tras uniformizar ambas marginales,

$$
h_\psi=2\bigl[\psi-\psi_U-\psi_V+\bar\psi\bigr]=2\mathcal P\psi,
\qquad
\mathcal P=(I-M_u)(I-M_v),
\tag{2.2}
$$

con $\psi_U,\psi_V$ las medias marginales; y el score del experimento discreto finito. Ambas familias tienen densidad de referencia $1$ en $\varepsilon=0$, pero sus tangentes difieren en general, en los términos marginales $2(\psi_U+\psi_V-2\bar\psi)$; pasar a rangos aplica la transformada integral de probabilidad marginal y elimina la información marginal, de modo que el experimento finito solo ve $h_\psi$.

Una muestra de $N$ puntos da tres observaciones progresivamente más gruesas. La muestra continua $(U_k,V_k)_{k\le N}$ tiene score $T_{N,\psi}=\sum_kh_\psi(U_k,V_k)$. Ordenar por $U$ y registrar el rango inducido en $V$ da una permutación de rangos *etiquetada* $\Pi_N\in S_N$. Lo que un conjunto causal expone es aún más grueso: la clase de isomorfía *no etiquetada* $[P_{\Pi_N}]$ de la matriz de permutación, invariante bajo la elección de realizador lineal.

Escribimos $\mathcal C_N$ para las clases de isomorfía de posets bidimensionales realizados a cardinalidad $N$ y $\Gamma_C=\{\sigma\in S_N:[P_\sigma]=C\}$. La ley que se estudia en todo el trabajo es

$$
\mu_{N,\varepsilon}^{[P]}(C):=\mathbb P_\varepsilon\bigl([P_{\Pi_N}]=C\bigr)
=\sum_{\sigma\in\Gamma_C}p_\varepsilon(\sigma),
\qquad
\mu_{N,0}^{[P]}(C)=\frac{|\Gamma_C|}{N!}>0,
\tag{2.3}
$$

que cierra la cadena $\psi\to\dot g_0\to t_\psi\to h_\psi\to S_{N,\psi}\to\mu_{N,\varepsilon}^{[P]}$.

En todo el trabajo, $H=L^2_0([0,1])$ es el espacio de media nula con base de Legendre desplazada $(p_m)_{m\ge1}$, ortonormalizada como $(\ell_m)_{m\ge1}$ donde convenga, $P_{N-1}=\operatorname{span}\{p_1,\ldots,p_{N-1}\}$, y $\mathcal X=H\widehat\otimes H$ con sus partes simétrica y antisimétrica $\mathcal X_{\rm sym}=H\widehat\otimes_{\rm sym}H$ y $\mathcal X_{\rm alt}=\bigwedge^2H$. La involución de intercambio de coordenadas $(\mathfrak sf)(u,v)=f(v,u)$ es unitaria y autoadjunta, con proyecciones $\Pi_{\rm sym}=(I+\mathfrak s)/2$ y $\Pi_{\rm alt}=(I-\mathfrak s)/2$.

## 3. Scores y el cociente a posets no etiquetados

**Diferenciabilidad en media cuadrática (QMD).** Fijemos un generador admisible $\psi\in C(D)$ y pongamos $f=\mathcal P\psi$. La densidad de la cópula satisface $c_\varepsilon=1+2\varepsilon f+o(\varepsilon)$ uniformemente en $D$, con ambas marginales de $f$ nulas. La positividad y la continuidad en el dominio compacto dan una cota inferior positiva común para $c_\varepsilon$ con $|\varepsilon|$ pequeño, de modo que el desarrollo de Taylor de la raíz cuadrada con resto uniforme da $\int(\sqrt{c_\varepsilon}-1-\varepsilon f)^2=o(\varepsilon^2)$: el experimento de cópula con una observación es QMD en cero con score $2f=h_\psi$. Tomando el producto $N$-ésimo se obtiene el score muestral $T_{N,\psi}=2\sum_kf(U_k,V_k)$.

El suceso $\{\Pi_N=\sigma\}$ está definido por desigualdades estrictas entre coordenadas y es independiente de $\varepsilon$ (los empates son nulos), y $c_\varepsilon$ y su derivada en $\varepsilon$ están uniformemente acotadas cerca de cero, de modo que derivar bajo la integral es válido. Con $p_\varepsilon(\sigma)=\int_{\{\Pi_N=\sigma\}}\prod_kc_\varepsilon(U_k,V_k)$ y $p_0(\sigma)=1/N!$,

$$
S_N^\Pi(f)(\sigma)=\partial_\varepsilon\log p_\varepsilon(\sigma)\big|_0
=\mathbb E_0\bigl[T_{N,\psi}\mid\Pi_N=\sigma\bigr].
\tag{3.1}
$$

Se sigue de la verosimilitud, y no supone independencia tras condicionar.

**Representantes.** Sean

$$
d_i^{(N)}(t):=N\binom{N-1}{i-1}t^{i-1}(1-t)^{N-i},
\qquad
b_i^{(N)}:=d_i^{(N)}-1
\tag{3.2}
$$

la densidad del $i$-ésimo estadístico de orden uniforme y su versión centrada. Bajo la ley de referencia los estadísticos de orden son independientes de los rangos, de modo que los dos vectores de estadísticos de orden son independientes entre sí y conjuntamente independientes de $\Pi_N$. Dado $\Pi_N=\sigma$, el punto con $U$-rango $i$ se empareja con el punto con $V$-rango $\sigma(i)$, y ese par sigue teniendo densidad $d_i^{(N)}\otimes d_{\sigma(i)}^{(N)}$, así que (3.1) da $S_N^\Pi(f)(\sigma)=2\sum_i\langle f,d_i^{(N)}\otimes d_{\sigma(i)}^{(N)}\rangle$ y por tanto

$$
p_\sigma'(0;f)=\frac2{N!}\sum_{i=1}^N\bigl\langle f,d_i^{(N)}\otimes d_{\sigma(i)}^{(N)}\bigr\rangle.
\tag{3.3}
$$

Como ambas marginales de $f$ se anulan, escribir $d_i^{(N)}=1+b_i^{(N)}$ elimina los términos constante y de una sola coordenada, de modo que $\langle f,d_i^{(N)}\otimes d_j^{(N)}\rangle=\langle f,b_i^{(N)}\otimes b_j^{(N)}\rangle$ y

$$
\boxed{\;R_\sigma^{(N)}:=\frac2{N!}\sum_{i=1}^Nb_i^{(N)}\otimes b_{\sigma(i)}^{(N)},
\qquad
p_\sigma'(0;f)=\bigl\langle f,R_\sigma^{(N)}\bigr\rangle.\;}
\tag{3.4}
$$

Las funciones $d_i^{(N)}/N$ forman la base de Bernstein de grado $N-1$; como $\sum_id_i^{(N)}=N$, el centrado deja la única relación $\sum_ib_i^{(N)}=0$, y por tanto $\operatorname{span}\{b_i^{(N)}\}=P_{N-1}$, de modo que $R_\sigma^{(N)}\in P_{N-1}\otimes P_{N-1}$. La fórmula (3.4), deducida para tangentes continuas admisibles, define un funcional lineal acotado de todo $f\in\mathcal X$; usamos abajo esta extensión al espacio de Hilbert sin afirmar que todo $f$ así sea geométricamente realizable.

Sumar (3.4) sobre una fibra, que es finita e independiente de $\varepsilon$, da el representante de clase y el score de la ley observable:

$$
R_C^{(N)}:=\sum_{\sigma\in\Gamma_C}R_\sigma^{(N)},
\qquad
\partial_\varepsilon\mu_{N,\varepsilon}^{[P]}(C)\big|_0=\bigl\langle f,R_C^{(N)}\bigr\rangle,
\qquad
(D\mathscr S_Nf)(C)=\frac{\langle f,R_C^{(N)}\rangle}{\mu_{N,0}^{[P]}(C)}.
\tag{3.5}
$$

Como $\mathcal C_N$ es finito y toda masa de referencia es positiva, la diferenciabilidad coordenada a coordenada equivale aquí al desarrollo QMD discreto con score (3.5). Ese score tiene media nula: sumando (3.4) sobre todos los $\sigma$, cada $b_j^{(N)}$ aparece $(N-1)!$ veces en cada posición fija, y $\sum_jb_j^{(N)}=0$, de modo que $\sum_CR_C^{(N)}=0$.

**Simetría de las sumas de clase.** Cada fibra es cerrada bajo inversión. Si $i<j$ y $\sigma(i)<\sigma(j)$, poniendo $a=\sigma(i),b=\sigma(j)$ se tiene $a<b$ y $\sigma^{-1}(a)<\sigma^{-1}(b)$, así que $i\mapsto\sigma(i)$ es un isomorfismo de posets $P_{\sigma^{-1}}\cong P_\sigma$: intercambiar las dos coordenadas de rango envía $\sigma$ a $\sigma^{-1}$ sin cambiar el poset abstracto. Como $(R_\sigma^{(N)})^\top=R_{\sigma^{-1}}^{(N)}$,

$$
\sigma\in\Gamma_C\iff\sigma^{-1}\in\Gamma_C,
\qquad
\bigl(R_C^{(N)}\bigr)^\top=R_C^{(N)},
\qquad
R_C^{(N)}\in\operatorname{Sym}^2P_{N-1}.
\tag{3.6}
$$

**Forma de Fisher y espacio visible.** Polarizando (3.5),

$$
G_{[P]}^{(N)}(f,g)
=\bigl\langle D\mathscr S_Nf,D\mathscr S_Ng\bigr\rangle_{L^2(\mu_{N,0})}
=\sum_{C\in\mathcal C_N}\frac{\langle f,R_C^{(N)}\rangle\langle g,R_C^{(N)}\rangle}{\mu_{N,0}^{[P]}(C)}.
\tag{3.7}
$$

Como toda masa de referencia es estrictamente positiva, $\ker D\mathscr S_N=\ker G_{[P]}^{(N)}=\operatorname{span}\{R_C^{(N)}\}^{\perp}$, y por (3.6)

$$
V_N:=(\ker D\mathscr S_N)^\perp=\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}\subseteq\operatorname{Sym}^2P_{N-1}.
\tag{3.8}
$$

**Reducción finita.** Pongamos $E_N:=\mathbf1^\perp\subset\mathbb R^N$ y

$$
\Lambda_N:E_N\to P_{N-1},
\qquad
\Lambda_Nz:=\sum_{i=1}^Nz_ib_i^{(N)}.
\tag{3.9}
$$

Para $z\in E_N$ se tiene $\sum_iz_ib_i^{(N)}=\sum_iz_id_i^{(N)}$, que se anula solo cuando $z=0$ por la independencia lineal de la base de Bernstein; como $\dim E_N=\dim P_{N-1}=N-1$, $\Lambda_N$ es un isomorfismo. Fijemos

$$
P_\sigma:=\sum_{i=1}^Ne_ie_{\sigma(i)}^\top,
\qquad
A_C:=\sum_{\sigma\in\Gamma_C}P_\sigma,
\tag{3.10}
$$

de modo que $A_C\mathbf1=|\Gamma_C|\mathbf1$ y $\mathbf1^\top A_C=|\Gamma_C|\mathbf1^\top$, luego $E_N$ es $A_C$-invariante, y el cierre bajo inversión de $\Gamma_C$ hace que $A_C|_{E_N}\in\operatorname{Sym}(E_N)$. Identificando $\operatorname{Sym}(E_N)$ con $\operatorname{Sym}^2E_N$ mediante el producto interno euclídeo, sea $\mathfrak T_N=(\Lambda_N\otimes\Lambda_N)|_{\operatorname{Sym}^2E_N}$, un isomorfismo lineal sobre $\operatorname{Sym}^2P_{N-1}$ (no una isometría: preserva generados y rangos, no autovalores de Fisher). Como $\sum_ib_i^{(N)}=0$, proyectar sobre $E_N$ en cualquiera de los dos índices deja inalterado el tensor transportado, y (3.4)–(3.5) dan exactamente

$$
R_C^{(N)}=\frac2{N!}\,\mathfrak T_N\bigl(A_C|_{E_N}\bigr).
\tag{3.11}
$$

El escalar $2/N!$ es no nulo, de modo que la inclusión recíproca en (3.8) equivale a un enunciado puramente combinatorio:

$$
\boxed{\;V_N=\operatorname{Sym}^2P_{N-1}
\iff
\operatorname{span}\{A_C|_{E_N}:C\in\mathcal C_N\}=\operatorname{Sym}(E_N).\;}
\tag{3.12}
$$

## 4. Visibilidad tangente exacta

**Teorema 1 (generado de las sumas de clase).** *Para todo $N\ge2$,*

$$
\boxed{\;V_N=\operatorname{Sym}^2P_{N-1},
\qquad
\dim V_N=\operatorname{rank}G_{[P]}^{(N)}=\binom N2.\;}
$$

*Equivalentemente, $T_N(\operatorname{im}J_N)=\operatorname{Sym}(E_N)$. La demostración exhibe una familia explícita de $\binom N2$ clases de posets cuyas sumas de clase generan el objetivo, para todo $N$, sin enumerar posets ni extrapolar desde $N$ pequeño.*

*Demostración.* Por (3.12) basta probar $\operatorname{span}\{A_C|_{E_N}\}=\operatorname{Sym}(E_N)$.

**Paso 1: una familia de $\binom N2$ clases casi-cadena.** Para enteros $0\le a<b\le N-1$, sea $C_{a,b}$ la formada por una cadena $c_1<\cdots<c_{N-1}$ y un elemento adicional $z$ con

$$
c_i<z\ (i\le a),
\qquad
z<c_i\ (i>b),
\qquad
z\parallel c_i\ (a<i\le b).
\tag{4.1}
$$

Toda extensión lineal $L_k$ de $C_{a,b}$ inserta $z$ tras exactamente $k\in\{a,\ldots,b\}$ elementos de la cadena. La intersección $L_s\cap L_t$ sitúa $c_1,\ldots,c_{\min(s,t)}$ por debajo de $z$ y $c_{\max(s,t)+1},\ldots,c_{N-1}$ por encima, de modo que

$$
L_s\cap L_t=C_{a,b}\iff\{s,t\}=\{a,b\}.
\tag{4.2}
$$

Todo $\sigma$ con $P_\sigma\cong C_{a,b}$ retrae el orden natural y el $\sigma$-orden a un par ordenado de realizadores; recíprocamente, enumerar los elementos en el primer orden de un par ordenado de realizadores y registrar los rangos en el segundo produce un $\sigma$ así. Aplicar un automorfismo o un reetiquetado simultáneo a ambos órdenes deja inalterada la permutación de rangos relativos, de modo que la elección del isomorfismo no aporta nada más. Por (4.2) los únicos pares ordenados de realizadores son $(L_a,L_b)$ y $(L_b,L_a)$; normalizar la primera extensión al orden natural hace que la permutación relativa sea un ciclo $\tau_{a,b}$ sobre el intervalo consecutivo $I_{a,b}=\{a+1,\ldots,b+1\}$, e invertir el par da su inverso. Por tanto

$$
\Gamma_{C_{a,b}}=\{\tau_{a,b},\tau_{a,b}^{-1}\}
\tag{4.3}
$$

como conjunto sin multiplicidad; para $b=a+1$ el ciclo es una transposición y ambos coinciden. Estas clases son distintas dos a dos: el multiconjunto de cardinalidades del pasado estricto es $\{0,\ldots,b-1,b+1,\ldots,N-1\}\uplus\{a\}$, que omite $b$ y repite $a$, de modo que determina $(a,b)$.

**Paso 2: de los ciclos de intervalo a los laplacianos de arista.** Para $1\le i<j\le N$ pongamos $L_{ij}:=(e_i-e_j)(e_i-e_j)^\top$, entendidos abajo como restringidos a $E_N$. Cada uno aniquila $\mathbf1$; una combinación que se anule en $E_N$ se anula por tanto en todo $\mathbb R^N$, y su entrada $(i,j)$ es $-w_{ij}$, de modo que todo coeficiente es nulo. Como hay $\binom N2=\dim\operatorname{Sym}(E_N)$ de ellos, forman una base, y sumar todas las aristas da

$$
\sum_{1\le i<j\le N}L_{ij}=NI_{E_N}.
\tag{4.4}
$$

Pongamos $S_{a,b}:=P_{\tau_{a,b}}+P_{\tau_{a,b}}^\top$, de modo que por (4.3)

$$
S_{a,b}=2A_{C_{a,b}}\ (b=a+1),
\qquad
S_{a,b}=A_{C_{a,b}}\ (b>a+1),
\tag{4.5}
$$

un múltiplo escalar no nulo en ambos casos, y pongamos $Q_{a,b}:=2I_{E_N}-S_{a,b}|_{E_N}$. Como $\tau_{a,b}$ es el ciclo consecutivo sobre $I_{a,b}$, $Q_{a,b}$ es exactamente el laplaciano del grafo de ese ciclo, con la única arista contada dos veces cuando el intervalo tiene longitud dos:

$$
Q_{a,a+1}=2L_{a+1,a+2},
\qquad
Q_{a,b}=L_{a+1,b+1}+\sum_{k=a+1}^bL_{k,k+1}\quad(b>a+1).
\tag{4.6}
$$

Estos son triangulares en la longitud del intervalo y se invierten como

$$
L_{i,i+1}=\tfrac12Q_{i-1,i},
\qquad
L_{ij}=Q_{i-1,j-1}-\tfrac12\sum_{k=i}^{j-1}Q_{k-1,k}\quad(j>i+1),
\tag{4.7}
$$

de modo que $\operatorname{span}\{Q_{a,b}\}=\operatorname{span}\{L_{ij}\}=\operatorname{Sym}(E_N)$. Esto todavía no da las sumas de clase, porque el término común $2I_{E_N}$ se ha restado de cada $Q_{a,b}$.

**Paso 3: la identidad es ella misma una combinación de sumas de clase.** Por (4.4) y (4.7) existen coeficientes $c_{a,b}$ con $I_{E_N}=\sum_{a<b}c_{a,b}Q_{a,b}$. Sus valores individuales no hacen falta, pero su suma sí. Por (4.7) una arista $L_{ij}$ a distancia $d=j-i$ lleva coeficiente total $1-d/2$ en su expresión mediante los $Q$: esto es $1/2$ para $d=1$, y para $d>1$ es un término de intervalo largo de coeficiente $1$ menos $d$ términos adyacentes de coeficiente $1/2$. Hay $N-d$ aristas a distancia $d$, de modo que dividiendo (4.4) entre $N$,

$$
s_N:=\sum_{a<b}c_{a,b}
=\frac1N\sum_{d=1}^{N-1}(N-d)\Bigl(1-\frac d2\Bigr)
=\frac{(N-1)(5-N)}{12}.
\tag{4.8}
$$

Sustituyendo $Q_{a,b}=2I_{E_N}-S_{a,b}|_{E_N}$ se obtiene $(1-2s_N)I_{E_N}=-\sum_{a<b}c_{a,b}S_{a,b}|_{E_N}$, y

$$
\boxed{\;1-2s_N=\frac{N^2-6N+11}{6}=\frac{(N-3)^2+2}{6}>0\;}
\tag{4.9}
$$

para todo entero $N$ — nunca se anula, ni en $N=3$ ni en ningún otro sitio. Por tanto $I_{E_N}\in\operatorname{span}\{S_{a,b}|_{E_N}\}$; reintroducir esto en $Q_{a,b}=2I_{E_N}-S_{a,b}|_{E_N}$ sitúa todo $Q_{a,b}$ en el mismo generado, y el Paso 2 da $\operatorname{span}\{S_{a,b}|_{E_N}\}=\operatorname{Sym}(E_N)$. Por (4.5) las propias sumas de clase generan, que es (3.12). $\square$

**Corolario 2 (filtración y densidad).** *Para $N\ge2$,*

$$
V_N=\operatorname{Sym}^2P_{N-1}\subsetneq\operatorname{Sym}^2P_N=V_{N+1},
\qquad
\dim V_N=\binom N2,
\qquad
\overline{\bigcup_{N\ge2}V_N}=\mathcal X_{\rm sym}.
\tag{4.10}
$$

*Demostración.* Escribamos $x\odot y=x\otimes y+y\otimes x$. La ortogonalidad de la base de Legendre desplazada da $P_N=P_{N-1}\oplus\operatorname{span}\{p_N\}$, y de ahí la descomposición ortogonal

$$
V_{N+1}=V_N\oplus\{x\odot p_N:x\in P_{N-1}\}\oplus\operatorname{span}\{p_N\otimes p_N\},
\tag{4.11}
$$

de modo que $p_1\odot p_N\in V_{N+1}\setminus V_N$ y la inclusión es estricta en cada paso, con sucesión de rangos $1,3,6,10,15,\ldots$. Para la densidad: si polinomios $q_m\to h$ en $L^2$ entonces $\|q_m-\int q_m-h\|\le2\|q_m-h\|\to0$, de modo que los polinomios centrados son densos en $H$; las sumas finitas de tensores elementales de un subespacio denso son densas en $\mathcal X$, y aplicar la proyección continua $\Pi_{\rm sym}$ muestra que todo tensor de Hilbert–Schmidt simétrico es aproximable por sumas finitas de tensores polinómicos simetrizados, cada uno en algún $\operatorname{Sym}^2P_m=V_{m+1}$. $\square$

## 5. Núcleo, cociente y resolución de Fisher

Sea $\mathcal K_N:=L^2_0(\mathcal C_N,\mu_{N,0})$ el espacio de scores de media nula de la ley finita de posets no etiquetados, y $D\mathscr S_N:\mathcal X\to\mathcal K_N$ el diferencial acotado del score de §3. Pongamos

$$
P_N^{\rm vis}:=\Pi_{V_N}\Pi_{\rm sym},
\qquad
\mathcal X=V_N\oplus V_N^{\perp_{\rm sym}}\oplus\mathcal X_{\rm alt},
\tag{5.1}
$$

donde $\perp_{\rm sym}$ denota el complemento ortogonal tomado dentro de $\mathcal X_{\rm sym}$. Como $V_N\subset\mathcal X_{\rm sym}$, $P_N^{\rm vis}$ es la proyección ortogonal ambiente sobre $V_N$.

**Corolario 3 (factorización, núcleo, cociente identificable).** *Para $N\ge2$ sea $B_N:=D\mathscr S_N|_{V_N}$. Entonces $B_N$ es inyectivo,*

$$
\boxed{\;D\mathscr S_N=B_NP_N^{\rm vis},
\qquad
\ker D\mathscr S_N=V_N^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H
=\bigl(\operatorname{Sym}^2P_{N-1}\bigr)^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H,\;}
\tag{5.2}
$$

*y, con $q_N$ la aplicación cociente, $U_N([f]):=P_N^{\rm vis}f$ es un isomorfismo isométrico canónico que da la factorización inducida $D\mathscr S_N=B_NU_Nq_N$ y*

$$
\boxed{\;\mathcal X/\ker D\mathscr S_N\simeq V_N=\operatorname{Sym}^2P_{N-1},
\qquad
\dim\bigl(\mathcal X/\ker D\mathscr S_N\bigr)=\binom N2.\;}
\tag{5.3}
$$

*Demostración.* Por (3.8) y el Teorema 1, $(\ker D\mathscr S_N)^\perp=V_N$; escindir el complemento ambiente a lo largo de $\mathcal X=\mathcal X_{\rm sym}\oplus\mathcal X_{\rm alt}$ da el núcleo de (5.2) y $\ker P_N^{\rm vis}=\ker D\mathscr S_N$, de donde $D\mathscr S_Nf=D\mathscr S_NP_N^{\rm vis}f=B_NP_N^{\rm vis}f$. Un vector de $\ker B_N$ está en $V_N\cap V_N^\perp$, así que $B_N$ es inyectivo. Entonces $U_N$ está bien definido, es biyectivo e isométrico porque $\|[f]\|=\inf_{k\in\ker}\|f+k\|=\|P_N^{\rm vis}f\|$. $\square$

En consecuencia, para $f,g\in\mathcal X$,

$$
D\mathscr S_Nf=D\mathscr S_Ng
\iff
P_N^{\rm vis}f=P_N^{\rm vis}g.
\tag{5.4}
$$

Combinar (5.2) con el Corolario 2 da además $\bigcap_{N\ge2}\ker D\mathscr S_N=\bigwedge^2H$: el sector antisimétrico es invisible a primer orden simultáneamente en toda resolución. §7 muestra qué implica y qué no implica esto.

**Resolución dentro del sector visible.** La proyección $P_N^{\rm vis}$ registra *qué* direcciones sobreviven. Su peso en la ley es un segundo dato,

$$
F_N:=B_N^*B_N:V_N\to V_N,
\qquad
D\mathscr S_N^*D\mathscr S_N=P_N^{\rm vis}F_NP_N^{\rm vis},
\tag{5.5}
$$

definido positivo sobre $V_N$ porque $B_N$ es inyectivo y $V_N$ tiene dimensión finita. El experimento de referencia continuo de $N$ observaciones independientes de la cópula tiene score $2\sum_kf(U_k,V_k)$ y forma de Fisher $4N\langle f,g\rangle$. Como $D\mathscr S_Nf$ es la esperanza condicional de ese score dado $[P_{\Pi_N}]$ y la esperanza condicional contrae $L^2$ ([Pollard2013]), $I_N^{[P]}(f)\le4N\|f\|^2$; normalizar por esa forma da

$$
\widehat F_N:=\frac1{4N}\,D\mathscr S_N^*D\mathscr S_N\quad\text{en }\mathcal X,
\qquad
0\le\widehat F_N\le I_{\mathcal X},
\qquad
\operatorname{supp}\widehat F_N=V_N.
\tag{5.6}
$$

En general $\widehat F_N\ne P_N^{\rm vis}$, equivalentemente $F_N\ne4NI_{V_N}$.

**Espectros exactos en $N=2,3,4$.** Pongamos

$$
x(t):=t-\tfrac12,
\qquad
q(t):=\bigl(t-\tfrac12\bigr)^2-\tfrac1{12},
\qquad
r(t):=\bigl(t-\tfrac12\bigr)^3-\tfrac3{20}\bigl(t-\tfrac12\bigr),
\tag{5.7}
$$

mutuamente ortogonales y que generan sucesivamente $P_1,P_2,P_3$, y definamos $e_{11}=x\otimes x$, $e_{12}=x\otimes q+q\otimes x$, $e_{13}=x\otimes r+r\otimes x$, $e_{22}=q\otimes q$, $e_{23}=q\otimes r+r\otimes q$, $e_{33}=r\otimes r$. Para $N=2$, $G_{[P]}^{(2)}(f,g)=256\langle f,e_{11}\rangle\langle g,e_{11}\rangle$. Para $N=3$, en la base $e_{11},e_{12},e_{22}$,

$$
\bigl[G_{[P]}^{(3)}\bigr]=\operatorname{diag}\Bigl(\tfrac1{32},\tfrac1{1200},\tfrac1{180000}\Bigr),
\qquad
\bigl[G_{\rm full}^{(3)}\bigr]=\operatorname{diag}\Bigl(\tfrac1{12},\tfrac1{90},\tfrac1{2700}\Bigr).
\tag{5.8}
$$

En $N=4$ tres autovectores generalizados siguen siendo puros,

$$
\widehat F_4e_{11}=\tfrac{12}{25}e_{11},
\qquad
\widehat F_4e_{12}=\tfrac4{25}e_{12},
\qquad
\widehat F_4e_{23}=\tfrac4{525}e_{23},
\tag{5.9}
$$

mientras que $\operatorname{span}\{e_{13},e_{22},e_{33}\}$ es un bloque invariante sobre el que, en esa base ordenada,

$$
\bigl[G_{[P]}^{(4)}\bigr]_{\rm mix}
=\begin{pmatrix}
1/55125&1/354375&1/38587500\\
1/354375&11/455625&-1/49612500\\
1/38587500&-1/49612500&11/5402250000
\end{pmatrix},
\qquad
\bigl[G_{\rm full}^{(4)}\bigr]_{\rm mix}=\operatorname{diag}\Bigl(\tfrac1{1050},\tfrac1{2025},\tfrac1{490000}\Bigr),
\tag{5.10}
$$

con autovalores generalizados las tres raíces reales positivas de

$$
144703125\lambda^3-9975000\lambda^2+142000\lambda-128=0,
\tag{5.11}
$$

numéricamente $0.0494521212879\ldots$, $0.0185160720400\ldots$, $0.000966047034941\ldots$ (solo a título orientativo). Recopilando:

| $N$ | $\operatorname{spec}_+(\widehat F_N)$ |
|---|---|
| $2$ | $\{2/9\}$ |
| $3$ | $\{3/8,\ 3/40,\ 3/200\}$, autovectores $e_{11},e_{12},e_{22}$ |
| $4$ | $\{12/25,\ 4/25,\ 4/525\}$ de (5.9), junto con las tres raíces de (5.11) |

de modo que en $N=4$ el orden decreciente exacto es

$$
\tfrac{12}{25}>\tfrac4{25}>0.0494521212879\ldots>0.0185160720400\ldots>\tfrac4{525}>0.000966047034941\ldots>0.
\tag{5.12}
$$

El espectro ya es anisótropo en $N=3$, y las entradas fuera de la diagonal de (5.10) son la primera mezcla modal: $e_{13},e_{22},e_{33}$ son visibles pero no son individualmente autovectores de Fisher. La pertenencia a $V_N$ es por tanto lógicamente previa a la fuerza de Fisher retenida, y no la determina. Estos son cálculos exactos a $N$ fijo: no dan ninguna fórmula espectral para todo $N$ ni monotonía de los autovalores en $N$.

## 6. Retención de Fisher al crecer $N$

Sea $I_N^\Pi(f):=\mathbb E_0[S_N^\Pi(f)^2]$ la información de Fisher antes del cociente, cuando se observa la permutación de rangos completa, $I_N^{[P]}(f):=G_{[P]}^{(N)}(f,f)$, y, como forma bilineal semidefinida positiva, $\Delta_N(f,g):=\mathbb E_0[S_N^\Pi(f)S_N^\Pi(g)]-G_{[P]}^{(N)}(f,g)=\mathbb E_0[\operatorname{Cov}_0(S_N^\Pi(f),S_N^\Pi(g)\mid[P_{\Pi_N}])]$, escrita $\Delta_N(f):=\Delta_N(f,f)=I_N^\Pi(f)-I_N^{[P]}(f)$ en la diagonal.

**Teorema 4 (resolución de Fisher y retención asintótica).** *La esperanza condicional de los scores a lo largo de $\Pi_N\mapsto[P_{\Pi_N}]$ da*

$$
\Delta_N(f)=\mathbb E_0\bigl[\operatorname{Var}_0\bigl(S_N^\Pi(f)\mid[P_{\Pi_N}]\bigr)\bigr]\ge0.
\tag{6.1}
$$

*Para todo $f\in\mathcal X$,*

$$
\frac{I_N^\Pi(f)}N\longrightarrow4\|f\|_{\mathcal X}^2,
\tag{6.2}
$$

*y si además $f\in\mathcal X_{\rm sym}$,*

$$
\frac{\Delta_N(f)}N\longrightarrow0,
\qquad
\frac{I_N^{[P]}(f)}N\longrightarrow4\|f\|_{\mathcal X}^2.
\tag{6.3}
$$

*Para $f$ simétrico no nulo, (6.2) da un umbral finito, en general no uniforme, $N_0(f)$ con $I_N^\Pi(f)>0$ para $N\ge N_0(f)$; en ese rango pongamos*

$$
\rho_N(f):=\frac{I_N^\Pi(f)}{4N\|f\|^2},
\qquad
\kappa_N(f):=\frac{I_N^{[P]}(f)}{I_N^\Pi(f)},
\qquad
\eta_N^{\rm tot}(f):=\rho_N(f)\kappa_N(f)=\frac{I_N^{[P]}(f)}{4N\|f\|^2}.
\tag{6.4}
$$

*Entonces*

$$
\boxed{\;\rho_N(f)\to1,
\qquad
\kappa_N(f)\to1,
\qquad
\eta_N^{\rm tot}(f)\to1,
\qquad\text{lo último equivalente a nivel de operadores a}\qquad
\widehat F_N\xrightarrow{\ \rm SOT\ }\Pi_{\rm sym}.\;}
\tag{6.5}
$$

*Más en general, para $0\ne f=f_s+f_a$ descompuesto en partes simétrica y antisimétrica,*

$$
\frac{I_N^{[P]}(f)}{4N\|f\|^2}\longrightarrow\frac{\|f_s\|^2}{\|f_s\|^2+\|f_a\|^2};
\tag{6.6}
$$

*el sector antisimétrico contribuye cero al numerador para todo $N$, no solo asintóticamente.*

El primer límite de (6.5) concierne a las observaciones continuas frente a los rangos, el segundo a los rangos frente al poset no etiquetado. Son afirmaciones distintas, y ninguna se sigue de las inclusiones estrictas del Corolario 2.

*Demostración.* Pongamos $H_{ij}^{(N)}(f):=\langle f,d_i^{(N)}\otimes d_j^{(N)}\rangle$, de modo que $S_N^\Pi(f)(\sigma)=2\sum_iH_{i\sigma(i)}^{(N)}(f)$ por §3. Como $\sum_id_i^{(N)}=N$ y ambas marginales de $f$ se anulan, $H^{(N)}(f)$ tiene sumas por filas y por columnas nulas.

*(i) Identidad de Gram exacta.* Si $H,K$ tienen sumas por filas y por columnas nulas y $\Pi_N$ es uniforme, separar el promedio en $i=j$ e $i\ne j$ da $\mathbb E_0[\sum_iH_{i\Pi_N(i)}\sum_jK_{j\Pi_N(j)}]=\langle H,K\rangle_F/(N-1)$: la diagonal contribuye $N^{-1}\langle H,K\rangle_F$, mientras que las identidades de suma nula reducen el numerador fuera de la diagonal a $\langle H,K\rangle_F$ con factor de probabilidad $1/[N(N-1)]$. Por tanto

$$
I_N^\Pi(f)=\frac4{N-1}\bigl\|H^{(N)}(f)\bigr\|_F^2.
\tag{6.7}
$$

*(ii) Límite (6.2).* Sea $\mathcal O_Na:=(\langle a,d_i^{(N)}\rangle)_{i\le N}$, de modo que $H^{(N)}=(\mathcal O_N\otimes\mathcal O_N)f$, y $\widetilde{\mathcal O}_N:=N^{-1/2}\mathcal O_N$. El operador positivo $\widetilde{\mathcal O}_N^*\widetilde{\mathcal O}_N$ es el operador de Bernstein–Durrmeyer de grado $N-1$. Es triangular sobre los espacios de polinomios encajados, y la fórmula de la integral beta da a un monomio de grado $m\le N-1$ el coeficiente diagonal $N!(N-1)!/[(N+m)!(N-1-m)!]$; la autoadjunción hace entonces invariantes las diferencias ortogonales entre espacios de polinomios sucesivos, de modo que los $\ell_m$ son autofunciones con

$$
\lambda_{N-1,m}=\prod_{r=1}^m\frac{N-r}{N+r}\in[0,1]\ \ (1\le m\le N-1),
\qquad
\lambda_{N-1,m}=0\ \ (m\ge N),
\tag{6.8}
$$

y $\lambda_{N-1,m}\to1$ para cada $m$ fijo. Escribiendo $f=\sum_{j,k}c_{jk}\ell_j\otimes\ell_k$, (6.7) queda $I_N^\Pi(f)/N=\frac{4N}{N-1}\sum_{j,k}\lambda_{N-1,j}\lambda_{N-1,k}|c_{jk}|^2$, y la convergencia dominada en el array de cuadrado sumable da (6.2). La desigualdad de Jensen con $\sum_id_i^{(N)}=N$ da $\|\mathcal O_Na\|_{\ell^2}\le\sqrt N\|a\|$, y de ahí la cota uniforme

$$
0\le\frac{I_N^\Pi(f)}N\le\frac{4N}{N-1}\|f\|_{\mathcal X}^2\le8\|f\|_{\mathcal X}^2
\qquad(N\ge2).
\tag{6.9}
$$

*(iii) El suceso de la fibra.* Sea $\mathcal G_N$ el suceso de que el árbol de intervalos fuertes de $\Pi_N$ tenga raíz prima y de que todo hijo de la raíz sea o bien una hoja o bien un gemelo — un nodo lineal con dos hijos hoja. Este *no* es el suceso de que todo el grafo de incomparabilidad sea primo; se admiten gemelos. El árbol de intervalos fuertes es el árbol de descomposición modular del grafo de permutación ([BouvelChauveMishnaRossin2009], Observación 1), de modo que $\mathcal G_N$ es medible respecto de $[P_{\Pi_N}]$, pues el poset no etiquetado determina su grafo de incomparabilidad salvo isomorfismo. El Teorema 2 de [BouvelChauveMishnaRossin2009], cuya demostración aplica su Lema 1 con $c=1$, afirma que el complementario de este suceso tiene probabilidad $O(N^{-1})$; existen pues $C_{\rm fib},N_{\rm fib}$ finitos con $\mathbb P_0(\mathcal G_N^c)\le C_{\rm fib}/N$ para $N\ge N_{\rm fib}$ (la fuente no especifica estas constantes y nosotros no las afinamos).

En $\mathcal G_N$ la fibra es exactamente $\{\Pi_N,\Pi_N^{-1}\}$. En efecto, fijemos $\pi\in\mathcal G_N$ con bloques fuertes maximales $B_1,\ldots,B_m$ bajo la raíz e inflación $\pi=\alpha[\tau_1,\ldots,\tau_m]$; la condición sobre la raíz hace primo el grafo de incomparabilidad de $\alpha$ y fuerza $|B_s|\le2$, de modo que $\tau_s\in\{1,12,21\}$. Si $[P_\sigma]=[P_\pi]$, un isomorfismo de posets lleva los módulos fuertes maximales canónicos unos a otros preservando tamaños y tipos inducidos, así que al contraer se obtienen posets cociente isomorfos. El teorema de unicidad de Gallai para las dos orientaciones transitivas de un grafo de comparabilidad primo ([Gallai1967]), tras normalizar por rango ambos órdenes lineales, fuerza a que la permutación cociente de $\sigma$ sea $\alpha$ o $\alpha^{-1}$. En el primer caso cada patrón interno queda fijo, ya que en un bloque de dos elementos $12$ induce una cadena y $21$ una anticadena y un isomorfismo no puede intercambiarlos; en el segundo se aplica la fórmula del inverso de una inflación y los patrones internos $1,12,21$ son todos involuciones, lo que da $\pi^{-1}$.

*(iv) Momento cuarto para rango finito simétrico.* Sea $f=\sum_{r\le R}\alpha_ra_r\otimes a_r$ con $a_r$ ortonormales y centrados. Pongamos $x_i=(\mathcal O_Na)_i$ para un perfil fijo, $S_2=\sum_ix_i^2$, $S_4=\sum_ix_i^4$, $(N)_r=N(N-1)\cdots(N-r+1)$. Entonces $\sum_ix_i=0$, $N^{-1}S_2\to\|a\|^2$ y $\max_i|x_i|=o(\sqrt N)$: para lo último, elíjase $b$ acotada y próxima a $a$ en $L^2$ y úsese $0\le d_i^{(N)}\le N$, $\int d_i^{(N)}=1$ para obtener $|(\mathcal O_Na)_i|/\sqrt N\le\|b\|_\infty/\sqrt N+\|a-b\|_2$ uniformemente en $i$, y hágase después $N\to\infty$ y $b\to a$. Para $X_N(a)=\sum_ix_ix_{\Pi_N(i)}$, agrupar los cuatro índices por patrón de coincidencia da, para $N\ge4$,

$$
\mathbb E_0\bigl[X_N(a)^4\bigr]
=\frac{S_4^2}N+\frac{4S_4^2}{(N)_2}+\frac{3(S_2^2-S_4)^2}{(N)_2}
+\frac{6(2S_4-S_2^2)^2}{(N)_3}+\frac{9(S_2^2-2S_4)^2}{(N)_4}.
\tag{6.10}
$$

Con $S_2=O(N)$ y $S_4\le(\max_i|x_i|)^2S_2=o(N^2)$ esto es $o(N^3)$; como $S_N^\Pi(f)=2\sum_r\alpha_rX_N(a_r)$, la desigualdad de Minkowski en $L^4$ da $\mathbb E_0[S_N^\Pi(f)^4]=o(N^3)$.

*(v) Retención.* Para $f$ simétrico, $H^{(N)}(f)$ es simétrica, de modo que $S_N^\Pi(f)(\sigma^{-1})=S_N^\Pi(f)(\sigma)$ y por (iii) la varianza condicional de (6.1) se anula en $\mathcal G_N$. Cauchy–Schwarz junto con (iii) y (iv) da, para $f$ simétrico de rango finito fijo,

$$
0\le\Delta_N(f)\le\mathbb E_0\bigl[S_N^\Pi(f)^2\mathbf1_{\mathcal G_N^c}\bigr]
\le\mathbb P_0(\mathcal G_N^c)^{1/2}\,\mathbb E_0\bigl[S_N^\Pi(f)^4\bigr]^{1/2}=o(N).
\tag{6.11}
$$

Para eliminar la restricción de rango, obsérvese que $\mathcal L_N(f,g):=\Delta_N(f,g)/N$ es una forma positiva con $\mathcal L_N(f,f)\le8\|f\|^2$ por (6.1) y (6.9). Elíjanse $f_R\to f$ simétricos de rango finito; la desigualdad triangular para la seminorma inducida da $\sqrt{\mathcal L_N(f,f)}\le\sqrt{\mathcal L_N(f_R,f_R)}+\sqrt8\|f-f_R\|$. Tomar $N\to\infty$ con $R$ fijo y solo después $R\to\infty$ demuestra (6.3), y (6.4)–(6.5) se siguen por división una vez que el denominador es positivo.

*(vi) Parte antisimétrica y SOT.* La transformación $f\mapsto H^{(N)}(f)$ entrelaza el intercambio de coordenadas con la transposición de matrices, de modo que $H^{(N)}(f_s)$ es simétrica y $H^{(N)}(f_a)$ antisimétrica; la ortogonalidad de Frobenius en (6.7) da $I_N^\Pi(f)=I_N^\Pi(f_s)+I_N^\Pi(f_a)$, mientras que (5.2) da $I_N^{[P]}(f)=I_N^{[P]}(f_s)$. Con (6.2) y (6.3) esto es (6.6). Por último $\langle f,\widehat F_Nf\rangle=I_N^{[P]}(f)/(4N)\to\|\Pi_{\rm sym}f\|^2$; la polarización da convergencia en la topología débil de operadores, y como $0\le\widehat F_N\le I$ implica $\widehat F_N^2\le\widehat F_N$,

$$
\|\widehat F_Nf-\Pi_{\rm sym}f\|^2
\le\langle f,\widehat F_Nf\rangle+\|\Pi_{\rm sym}f\|^2-2\operatorname{Re}\langle\widehat F_Nf,\Pi_{\rm sym}f\rangle\longrightarrow0,
$$

lo que eleva la convergencia a SOT. $\square$

La convergencia de (6.5) no es en norma de operador. Para el vector unitario $h_N:=p_N\otimes p_N/\|p_N\|_{L^2}^2$, el Teorema 1 da $h_N\perp V_N$, de modo que

$$
\widehat F_Nh_N=0,
\qquad
\Pi_{\rm sym}h_N=h_N,
\qquad
\|\widehat F_N-\Pi_{\rm sym}\|\ge1
\quad\text{para todo }N.
\tag{6.12}
$$

Tampoco es $\widehat F_N$ una proyección a $N$ finito: su autovalor no nulo en $N=2$ es $2/9$. La tasa genérica en (6.3)–(6.6) es solo $o_f(1)$, sin tasa ni umbral uniformes sobre la esfera unidad de Hilbert–Schmidt; la tasa disponible $1-\kappa_N(f)=O(N^{-1/2})$ se aplica únicamente a la subclase continua acotada de rango finito. Estos enunciados conciernen a la compleción de Hilbert de las tangentes de interacción S1 y se transfieren directamente a tangentes de las que ya se sabe que provienen de caminos S1 admisibles.

## 7. Un testigo antisimétrico de segundo orden

Sean $\ell_1(t)=\sqrt3(2t-1)$ y $\ell_2(t)=\sqrt5(6t^2-6t+1)$, y pongamos

$$
\psi(u,v):=\ell_1(u)\ell_2(v)-\ell_2(u)\ell_1(v)
=-2\sqrt{15}\,(u-v)\bigl(6uv-3u-3v+2\bigr).
\tag{7.1}
$$

Es antisimétrica bajo el intercambio de coordenadas, tiene marginales nulas y media nula, y satisface

$$
\mathcal P\psi=\psi\ne0,
\qquad
h_\psi=2\psi\in\bigwedge\nolimits^2H,
\qquad
\|\psi\|_{L^2(D)}^2=2,
\qquad
\|h_\psi\|_{L^2(D)}^2=8,
\tag{7.2}
$$

de modo que $\psi\notin\ker\mathcal P$: su invisibilidad a primer orden no es el gauge marginal de §2. Como $\psi$ está acotada, la familia normalizada $\gamma_\psi:\varepsilon\mapsto g_\varepsilon$ de (2.1) es un camino S1 admisible para todo $\varepsilon$ real.

Sea $\iota(u,v)=(v,u)$. Preserva el orden producto, la medida de referencia y la métrica plana, mientras que $\psi\circ\iota=-\psi$ y, por cambio de variables, $Z(-\varepsilon)=Z(\varepsilon)$. Por tanto

$$
\iota^*g_\varepsilon=g_{-\varepsilon}
\qquad(\varepsilon\in\mathbb R):
\tag{7.3}
$$

los dos signos quedan identificados por una isometría discreta de la familia S1.

**Teorema 5 (paridad).** *Para $\gamma_\psi$, toda ley finita de posets no etiquetados es una función par y real-analítica de $\varepsilon$; en particular se anulan todos los jets impares en $\varepsilon=0$, de modo que $\partial_\varepsilon\mu_{N,\varepsilon}^{[P]}|_0=0$ para todo $N\ge2$.*

*Demostración.* Para $\pi\in S_N$ pongamos $T_\pi:=\sum_i\psi(U_{(i)},V_{(\pi(i))})$, con $U_{(1)}<\cdots<U_{(N)}$ y $V_{(1)}<\cdots<V_{(N)}$ dos vectores independientes de estadísticos de orden uniformes y $\langle\cdot\rangle_0$ su esperanza conjunta. La verosimilitud finita es

$$
p_\pi(\varepsilon)=\frac{\bigl\langle e^{2\varepsilon T_\pi}\bigr\rangle_0}{N!\,Z(\varepsilon)^N}.
\tag{7.4}
$$

La acotación de $\psi$ en el compacto $D$ domina $e^{2\varepsilon T_\pi}$, $e^{2\varepsilon\psi}$ y todas sus derivadas en $\varepsilon$ sobre intervalos compactos de $\varepsilon$, de modo que derivar bajo la integral es válido a todo orden y tanto el numerador como $Z$ son real-analíticos, con $Z>0$ en todo momento. Como $\psi(v,u)=-\psi(u,v)$ y las dos familias de estadísticos de orden son i.i.d., intercambiar sus papeles es un cambio de variables válido que, tras reindexar $j=\pi(i)$, convierte $T_\pi$ en $-T_{\pi^{-1}}$ y $Z(\varepsilon)$ en $Z(-\varepsilon)=Z(\varepsilon)$. Por tanto $p_\pi(-\varepsilon)=p_{\pi^{-1}}(\varepsilon)$, y sumar sobre una fibra, cerrada bajo inversión por (3.6), da $\mu_{N,\varepsilon}^{[P]}(C)=\mu_{N,-\varepsilon}^{[P]}(C)$. $\square$

Para medir la primera respuesta no nula de la ley finita completa, definimos

$$
r_N(\gamma_\psi):=\inf\Bigl\{k\ge1:\ \partial_\varepsilon^k\mu_{N,\varepsilon}^{[P]}\big|_0\ne0\ \text{como vector en }\mathcal C_N\Bigr\},
\tag{7.5}
$$

con $r_N=\infty$ si todos los jets se anulan; el invariante se refiere al camino completo, no solo a su tangente de primer orden nula.

**El segundo jet en $N=2$.** Como $\bar\psi=0$, desarrollar (7.4) con $Z'(0)=0$ y $Z''(0)=4\|\psi\|^2_{L^2(D)}$ da

$$
p_\pi'(0)=\frac2{N!}\langle T_\pi\rangle_0,
\qquad
p_\pi''(0)=\frac4{N!}\bigl(\langle T_\pi^2\rangle_0-N\|\psi\|_{L^2(D)}^2\bigr).
\tag{7.6}
$$

En $N=2$ la identidad tiene la cadena como clase y la transposición la anticadena, siendo cada fibra una única involución, de modo que $\mu_2''(C)=p_\pi''(0)$ con $\mu_{2,0}(\text{chain})=\mu_{2,0}(\text{antichain})=\tfrac12$. Al ser ambas permutaciones involuciones, $p_\pi(-\varepsilon)=p_\pi(\varepsilon)$ individualmente y $\langle T_{\rm chain}\rangle_0=\langle T_{\rm antichain}\rangle_0=0$. Para los momentos segundos, desarróllese $\psi=\ell_1\otimes\ell_2-\ell_2\otimes\ell_1$ dentro de cada cuadrado; la independencia de los procesos en $U$ y en $V$ factoriza todo término cruzado, de modo que con

$$
A_{jk}:=\mathbb E\bigl[\ell_j(U_{(1)})\ell_k(U_{(2)})\bigr],
\qquad
M_i(jk):=\mathbb E\bigl[\ell_j(U_{(i)})\ell_k(U_{(i)})\bigr],
\tag{7.7}
$$

la integración directa contra la densidad del par $2$ en $0<t_1<t_2<1$ y las marginales $2(1-t)$, $2t$ da

$$
A_{11}=A_{22}=0,
\quad
A_{12}=-A_{21}=\tfrac1{\sqrt{15}},
\qquad
M_i(11)=M_i(22)=1,
\quad
M_1(12)=-\tfrac2{\sqrt{15}}=-M_2(12).
\tag{7.8}
$$

Desarrollando $\psi(x,y)^2=\ell_1(x)^2\ell_2(y)^2-2\ell_1(x)\ell_2(x)\ell_1(y)\ell_2(y)+\ell_2(x)^2\ell_1(y)^2$ y agrupando los factores en $U$ frente a los factores en $V$,

$$
\begin{aligned}
\bigl\langle\psi(U_{(i)},V_{(i)})^2\bigr\rangle_0&=2M_i(11)M_i(22)-2M_i(12)^2=\tfrac{22}{15},\\
\bigl\langle\psi(U_{(1)},V_{(2)})^2\bigr\rangle_0&=M_1(11)M_2(22)-2M_1(12)M_2(12)+M_1(22)M_2(11)=\tfrac{38}{15},\\
\bigl\langle\psi(U_{(1)},V_{(1)})\psi(U_{(2)},V_{(2)})\bigr\rangle_0&=2A_{11}A_{22}-2A_{12}A_{21}=\tfrac2{15},\\
\bigl\langle\psi(U_{(1)},V_{(2)})\psi(U_{(2)},V_{(1)})\bigr\rangle_0&=-\bigl(A_{12}^2+A_{21}^2\bigr)=-\tfrac2{15},
\end{aligned}
\tag{7.9}
$$

de donde $\langle T_{\rm chain}^2\rangle_0=2\cdot\tfrac{22}{15}+2\cdot\tfrac2{15}=\tfrac{16}5$ y $\langle T_{\rm antichain}^2\rangle_0=2\cdot\tfrac{38}{15}-2\cdot\tfrac2{15}=\tfrac{24}5$. Con $N\|\psi\|^2=4$ y prefactor $4/2!=2$, (7.6) da

$$
\boxed{\;\partial_\varepsilon^2\mu_{2,\varepsilon}^{[P]}(\mathrm{antichain})\big|_0=\tfrac85,
\qquad
\partial_\varepsilon^2\mu_{2,\varepsilon}^{[P]}(\mathrm{chain})\big|_0=-\tfrac85,\;}
\tag{7.10}
$$

que suman cero como exige la masa total constante, es decir

$$
\mu_{2,\varepsilon}^{[P]}(\mathrm{antichain})=\tfrac12+\tfrac45\varepsilon^2+O(\varepsilon^4),
\qquad
\mu_{2,\varepsilon}^{[P]}(\mathrm{chain})=\tfrac12-\tfrac45\varepsilon^2+O(\varepsilon^4).
\tag{7.11}
$$

La magnitud de la deformación es así localmente visible ya en la cardinalidad más pequeña que admite dos órdenes causales distintos, mientras que su signo permanece identificado por (7.3).

**Propagación por borrado uniforme.** Para $m\ge3$, $C\in\mathcal C_m$, $D\in\mathcal C_{m-1}$ definimos

$$
K_{m,m-1}(C,D):=\frac1m\#\bigl\{v\in C:[C\setminus\{v\}]=D\bigr\}.
\tag{7.12}
$$

Esto está bien definido sobre clases: un isomorfismo $\phi:C\to C'$ se restringe a un isomorfismo $C\setminus\{v\}\to C'\setminus\{\phi(v)\}$, de modo que lleva biyectivamente el conjunto contado. Es un núcleo de Markov, ya que cada $v$ borra hacia exactamente una clase y hay $m$ elementos, y es puramente combinatorio, luego independiente de $\varepsilon$. Si $X_1,\ldots,X_m$ son i.i.d. según $q_\varepsilon$ y $V$ es uniforme en $\{1,\ldots,m\}$ e independiente de ellas, entonces para cada $j$ fijo el subvector $(X_i)_{i\ne j}$ es una muestra i.i.d. de tamaño $m-1$, y promediar sobre la elección uniforme independiente deja esa ley inalterada; pasar a rangos y después al poset no etiquetado da $\mu_{m-1,\varepsilon}^{[P]}=K_{m,m-1}\mu_{m,\varepsilon}^{[P]}$ para todo $\varepsilon$. Componiendo,

$$
K_{N\to2}:=K_{3,2}\circ\cdots\circ K_{N,N-1},
\qquad
\mu_{2,\varepsilon}^{[P]}=K_{N\to2}\,\mu_{N,\varepsilon}^{[P]},
\tag{7.13}
$$

con $K_{2\to2}=I$. Ambos lados son funciones de $\varepsilon$ con valores en espacios de dimensión finita unidos por una aplicación lineal fija, de modo que la derivación conmuta término a término con ella:

$$
\bigl(\mu_2^{[P]}\bigr)^{(k)}(0)=K_{N\to2}\bigl(\mu_N^{[P]}\bigr)^{(k)}(0)
\qquad(k\ge1).
\tag{7.14}
$$

**Corolario 6.** *Para el camino (7.1),*

$$
\boxed{\;r_N(\gamma_\psi)=2\qquad\forall N\ge2.\;}
\tag{7.15}
$$

*Demostración.* El Teorema 5 da $r_N\ge2$. Si $(\mu_N^{[P]})''(0)$ se anulara para algún $N$, entonces (7.14) con $k=2$ daría $(\mu_2^{[P]})''(0)=0$, contradiciendo (7.10). $\square$

El corolario es un enunciado de existencia para una órbita admisible: ni clasifica el segundo diferencial sobre $\bigwedge^2H$ ni afirma que toda dirección antisimétrica tenga orden dos, y no se introduce ningún operador general de segundo orden, cono nulo cuadrático, estimador ni tasa. El cero de primer orden es el pliegue isométrico exacto $\varepsilon\leftrightarrow-\varepsilon$ de (7.3), de modo que la pertenencia a $\ker D\mathscr S_N$ no implica invariancia de la ley no lineal completa.

## 8. Relación con trabajos previos

El marco es el de [Bombelli2000]: la ley completa de un poset causal no etiquetado a cardinalidad fija, junto con una comparación estadística de dos leyes así. En torno a él, [Janson2011] aporta la teoría límite de núcleos de posets y leyes finitas consistentes, mientras que [Surya2026] muestra que aumentar la resolución levanta degeneraciones — aunque mediante abundancias esperadas de intervalos y no mediante la ley completa de posets no etiquetados. Ninguno de ellos calcula el diferencial de la ley a $N$ finito, su rango ni su núcleo.

La correspondencia entre permutaciones y posets sobre la que se suma en §3 es clásica: [BayoumiElZaharKhamis1994] trabajan explícitamente con realizadores, con el cierre de una fibra bajo $\sigma\mapsto\sigma^{-1}$ y con la casi-unicidad de los realizadores para posets primos.

Antes del cociente, la estructura diferencial relevante está próxima a dos construcciones existentes. [EvenZohar2020] descompone las densidades de patrones mediante la teoría de representaciones de $S_N$, aislando el bloque de la representación estándar de dimensión $(N-1)^2$ realizado a través de matrices de permutación comprimidas a $\mathbf1^\perp$; su régimen asintótico concierne a las fluctuaciones del perfil de patrones de una permutación aleatoria a medida que crece el tamaño anfitrión, una cuestión distinta de la derivada local en $\varepsilon$ que se usa aquí. La comparación con [Kurecka2022] puede hacerse exacta usando (1.1): para $t=(t_\pi)$, póngase $M(t)=\sum_\pi t_\pi P_\pi$; su Lema 9 expresa todo coeficiente del polinomio gradiente como un múltiplo no nulo de $\beta_i^\top M(t)\beta_j$ sobre una base $\beta_2,\ldots,\beta_N$ de $E_N$, de modo que la aplicación gradiente tiene núcleo $\ker T_N$, y como $M(t)$ tiene sumas por filas y por columnas constantes, $T_N(t)=0$ si y solo si $M(t)$ es constante — su Lema 12. El diferencial a nivel de permutaciones, la base de Bernstein, la compresión a $E_N$, la técnica de matrices de recubrimiento y este núcleo ambiente pertenecen todos a ese trabajo.

El cociente por el orden causal añade la primera flecha de (1.1). Conocer el núcleo ambiente reescribe, pero no resuelve, el problema de la imagen restringida,

$$
\operatorname{rank}(T_NJ_N)=\dim(\operatorname{im}J_N)-\dim\bigl(\operatorname{im}J_N\cap\ker T_N\bigr),
\tag{8.1}
$$

y Kurečka no estudia ni $\operatorname{im}J_N$ ni esta intersección. El cierre bajo inversión da solo $T_N(\operatorname{im}J_N)\subseteq\operatorname{Sym}(E_N)$; la construcción casi-cadena de §4 aporta la inclusión recíproca y por tanto $T_N(\operatorname{im}J_N)=\operatorname{Sym}(E_N)$, que es el Teorema 1. [ChanKralNoelPehovaSharifzadehVolec2020] y [GarbeKralMalekshahianPenaguiao2025], sobre sumas de patrones que fuerzan cuasialeatoriedad y sobre la dimensión de la región factible de densidades de patrones, son contiguos pero no dan un enunciado de generado indexado por fibras.

El módulo objetivo tampoco es nuevo. [Diaconis1989] descompone funciones sobre rankings y da $M^{(N-2,2)}\simeq S^{(N)}\oplus S^{(N-1,1)}\oplus S^{(N-2,2)}$ para efectos de pares no ordenados — el módulo y la dimensión $\binom N2$ que hay detrás de una reformulación de $\operatorname{Sym}(E_N)$ en el esquema de Johnson — y la monografía [Diaconis1988] desarrolla la familia de modelos asociada. Ninguno introduce fibras de posets bidimensionales no etiquetados ni sus sumas de clase. Lo que aquí se afirma es el enunciado más estrecho de que las sumas sobre esas fibras generan exactamente ese módulo.

La información de Fisher tras el paso de las observaciones continuas a los rangos también se ha estudiado. [HallinMelloukRifi2001] encuentran polinomios de tipo Bernstein en proyecciones de Hájek de estadísticos de rangos, asintóticamente y no a $N$ finito exacto; [Hoff2007] establece la verosimilitud de rangos como verosimilitud semiparamétrica libre de marginales; [HoffNiuWellner2014] y [SeiMatsumoto2020] desarrollan la información y la divergencia inducidas de modelos de cópula gaussiana y de rangos. Ninguno alcanza el cociente ulterior $\Pi_N\to[P_{\Pi_N}]$. La identidad de operadores que conecta los dos niveles es estándar una vez que se conoce el núcleo: [Pollard2013] muestra en el marco QMD que el score de un estadístico es la esperanza condicional del score original, y todo operador acotado en un espacio de Hilbert factoriza tautológicamente a través de la proyección sobre el complemento de su núcleo. Así que (5.2) no es una construcción independiente; el Teorema 1 es lo que fija el complemento de forma exacta.

§7 ensambla mecanismos establecidos. [RotnitzkyCoxBottaiRobins2000] relacionan el orden de la primera derivada no nula con el comportamiento inferencial en modelos con información singular, incluida la ambigüedad de signo cuando ese orden es par. Dentro de la literatura sobre permutones, [Chan2021] y [CrudeleDukesNoel2024] calculan hessianas de combinaciones de densidades de patrones en torno al permutón uniforme una vez que el gradiente se anula. La consistencia proyectiva bajo borrado uniforme es estándar. El Teorema 5 y el Corolario 6 combinan estos elementos para una órbita S1 explícita.

Los precedentes cubren el diferencial a nivel de permutaciones, el objetivo abstracto en términos de teoría de representaciones, y la mecánica general de los scores inducidos por un estadístico y de la información singular de primer orden. Lo que aquí se determina es el efecto del cociente adicional que va de las permutaciones de rangos etiquetadas a las leyes finitas de orden causal no etiquetadas, para todo $N$ fijo.

## 9. Alcance y conclusión

En el punto de referencia independiente del modelo S1 en $1+1$ dimensiones, la ley finita de orden causal no etiquetado tiene una estructura diferencial local exactamente calculable. Los representantes del score de §3 reducen la cuestión a sumas de clase sobre las fibras de la aplicación de permutaciones a posets; el argumento constructivo de §4 da, para todo $N\ge2$,

$$
\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}=V_N=\operatorname{Sym}^2P_{N-1},
\qquad
\dim V_N=\binom N2,
\tag{9.1}
$$

y por tanto

$$
D\mathscr S_N=B_NP_N^{\rm vis},
\qquad
\ker D\mathscr S_N=V_N^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H,
\qquad
\mathcal X/\ker D\mathscr S_N\simeq V_N.
\tag{9.2}
$$

Los espacios visibles están estrictamente encajados y su unión es densa, de modo que ninguna tangente simétrica fija no nula permanece invisible en toda resolución. Visibilidad no es sensibilidad: $F_N=B_N^*B_N$ es definido positivo pero anisótropo sobre $V_N$, y en $N=4$ los modos visibles se mezclan antes de que emerjan autovectores de Fisher. Normalizado por $N$ observaciones continuas de la cópula,

$$
\widehat F_N\xrightarrow{\ \rm SOT\ }\Pi_{\rm sym},
\qquad
\|\widehat F_N-\Pi_{\rm sym}\|\ge1\ \text{ para todo }N,
\tag{9.3}
$$

de modo que toda tangente simétrica de Hilbert–Schmidt fija se retiene asintóticamente, pero no uniformemente sobre la esfera unidad. Separar las dos etapas — de las observaciones continuas a los rangos, de los rangos a los posets no etiquetados — es lo que localiza las pérdidas de Fisher correspondientes. Por último, la órbita antisimétrica de §7 tiene $r_N(\gamma_\psi)=2$ para todo $N\ge2$: un cero de primer orden forzado por simetría puede aun así portar un segundo jet no nulo.

El alcance de estos enunciados está limitado en varios aspectos concretos.

**Alcance del modelo.** Todo teorema concierne al modelo de interacción S1 explícito en un diamante causal de $1+1$ dimensiones, desarrollado en torno al punto de referencia independiente. Nada de lo aquí expuesto establece un análogo en $2+1$ o $3+1$ dimensiones, para un espaciotiempo lorentziano general, para Schwarzschild u horizontes, o para un modelo de muestreo de conjuntos causales arbitrario.

**Tangentes ambiente frente a realizabilidad geométrica.** $\mathcal X$ es el dominio analítico de los operadores de score, y las identidades para $V_N$, $\ker D\mathscr S_N$ y $F_N$ clasifican el canal finito sobre ese espacio ambiente. No demuestran que toda dirección de Hilbert–Schmidt esté generada por una curva admisible de geometrías lorentzianas; la realizabilidad sigue abierta y no hace falta para la clasificación.

**Identificación diferencial frente a reconstrucción no lineal.** El Corolario 3 identifica el cociente que ve $D\mathscr S_N$. No implica inyectividad de $\mathscr S_N$ a distancia finita, ni recuperación de coordenadas o de una métrica a partir de un causet, ni reconstrucción a partir de la familia de leyes finitas. El Corolario 6 concreta la brecha para una órbita; ni un operador general de segundo orden, ni su cono nulo, ni una clasificación de $\bigwedge^2H$ se desarrollan aquí.

**Asintótica puntual.** (9.3) es convergencia en la topología fuerte de operadores, sin tasa uniforme sobre la esfera unidad. Los espectros de Fisher exactos se limitan a $N=2,3,4$; no se afirma ninguna fórmula espectral para todo $N$, ni cota uniforme de condicionamiento, ni estimador.

**Prioridad.** La comparación estadística de leyes finitas de orden causal, y la expectativa de que muestras mayores afinen la resolución, tienen ambas precedentes claros, revisados en §8 junto con precedentes parciales sustanciales para los ingredientes individuales. No hemos encontrado una contrapartida exacta del teorema de generado por sumas de clase para todo $N$, ni del enunciado sobre la órbita antisimétrica, en la literatura allí considerada; esa ausencia no constituye por sí misma una reivindicación de prioridad, y la búsqueda no fue exhaustiva.

*For Karim.*

*What is forgotten is not always gone; sometimes it is merely hidden between what was and what is yet to come.*

## Referencias

- **[BayoumiElZaharKhamis1994]** Bayoumi I. Bayoumi, Mohamed H. El-Zahar, and Soheir M. Khamis. Counting two-dimensional posets. *Discrete Mathematics*, 131 (1–3): 29–37, 1994. doi: 10.1016/0012-365X(94)90370-0.
- **[Bombelli2000]** Luca Bombelli. Statistical Lorentzian geometry and the closeness of Lorentzian manifolds. *Journal of Mathematical Physics*, 41 (10): 6944–6958, 2000. doi: 10.1063/1.1288494.
- **[BouvelChauveMishnaRossin2009]** Mathilde Bouvel, Cédric Chauve, Marni Mishna, and Dominique Rossin. Average-case analysis of perfect sorting by reversals. In *Combinatorial Pattern Matching (CPM 2009)*, volume 5577 of *Lecture Notes in Computer Science*, pages 314–325, 2009. doi: 10.1007/978-3-642-02441-2_28.
- **[Chan2021]** Timothy F. N. Chan. *Substructure Densities in Extremal Combinatorics*. PhD thesis, Monash University and University of Warwick, February 2021.
- **[ChanKralNoelPehovaSharifzadehVolec2020]** Timothy F. N. Chan, Daniel Král', Jonathan A. Noel, Yanitsa Pehova, Maryam Sharifzadeh, and Jan Volec. Characterization of quasirandom permutations by a pattern sum. *Random Structures \& Algorithms*, 57 (4): 920–939, 2020. doi: 10.1002/rsa.20956.
- **[CrudeleDukesNoel2024]** Gabriel Crudele, Peter Dukes, and Jonathan A. Noel. Six permutation patterns force quasirandomness. *Discrete Analysis*, (8), 2024. doi: 10.19086/da.122973.
- **[Diaconis1988]** Persi Diaconis. *Group Representations in Probability and Statistics*, volume 11 of *Institute of Mathematical Statistics Lecture Notes–Monograph Series*. Institute of Mathematical Statistics, 1988. doi: 10.1214/lnms/1215467407.
- **[Diaconis1989]** Persi Diaconis. A generalization of spectral analysis with application to ranked data. *The Annals of Statistics*, 17 (3): 949–979, 1989. doi: 10.1214/aos/1176347251.
- **[EvenZohar2020]** Chaim Even-Zohar. Patterns in random permutations. *Combinatorica*, 40 (6): 775–804, 2020. doi: 10.1007/s00493-020-4212-z.
- **[Gallai1967]** Tibor Gallai. Transitiv orientierbare graphen. *Acta Mathematica Academiae Scientiarum Hungaricae*, 18 (1–2): 25–66, 1967. doi: 10.1007/BF02020961.
- **[GarbeKralMalekshahianPenaguiao2025]** Frederik Garbe, Daniel Král', Alexandru Malekshahian, and Raul Penaguiao. The dimension of the feasible region of pattern densities. *Mathematical Proceedings of the Cambridge Philosophical Society*, 178 (1): 1–14, 2025. doi: 10.1017/S0305004124000380.
- **[HallinMelloukRifi2001]** Marc Hallin, Amal Mellouk, and Khalid Rifi. Projection de hájek et polyn\^omes de bernstein. *Canadian Journal of Statistics*, 29 (1): 141–154, 2001. doi: 10.2307/3316057.
- **[Hoff2007]** Peter D. Hoff. Extending the rank likelihood for semiparametric copula estimation. *The Annals of Applied Statistics*, 1 (1): 265–283, 2007. doi: 10.1214/07-AOAS107.
- **[HoffNiuWellner2014]** Peter D. Hoff, Xiaoyue Niu, and Jon A. Wellner. Information bounds for Gaussian copulas. *Bernoulli*, 20 (2): 604–622, 2014. doi: 10.3150/12-BEJ499.
- **[Janson2011]** Svante Janson. Poset limits and exchangeable random posets. *Combinatorica*, 31 (5): 529–563, 2011. doi: 10.1007/s00493-011-2591-x.
- **[Kurecka2022]** Martin Kurečka. Lower bound on the size of a quasirandom forcing set of permutations. *Combinatorics, Probability and Computing*, 31 (2): 304–319, 2022. doi: 10.1017/S0963548321000298.
- **[Pollard2013]** David Pollard. A note on insufficiency and the preservation of Fisher information. In *From Probability to Statistics and Back: High-Dimensional Models and Processes — A Festschrift in Honor of Jon A. Wellner*, volume 9 of *Institute of Mathematical Statistics Collections*, pages 266–275. 2013. doi: 10.1214/12-IMSCOLL919.
- **[RotnitzkyCoxBottaiRobins2000]** Andrea Rotnitzky, D. R. Cox, Matteo Bottai, and James Robins. Likelihood-based inference with singular information matrix. *Bernoulli*, 6 (2): 243–284, 2000. doi: 10.2307/3318576.
- **[SeiMatsumoto2020]** Tomonari Sei and Kazuya Matsumoto. Properties of divergence for semiparametric copula models. *Proceedings of the Institute of Statistical Mathematics*, 68 (1): 25–44, 2020. URL https://www.ism.ac.jp/editsec/toukei/pdf/68-1-025.pdf.
- **[Surya2026]** Sumati Surya. Closeness function on coarse grained Lorentzian geometries. *Physical Review D*, 113: 024034, 2026. doi: 10.1103/txbf-hvz3.
