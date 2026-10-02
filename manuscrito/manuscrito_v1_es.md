# Visibilidad tangente exacta de las leyes finitas de orden causal y resolución de Fisher en el modelo S1

## Resumen

La geometría estadística de las leyes finitas de conjuntos causales de [Bombelli2000] nos proporciona el objeto que estudiamos aquí: el canal de orden causal no etiquetado de un modelo de interacción S1 explícito de dimensión $1+1$, desarrollado en una geometría de referencia independiente. Para cada cardinalidad fija $N$, la derivada del score factoriza a través de la proyección ortogonal sobre $V_N=\operatorname{Sym}^2P_{N-1}$, donde $P_{N-1}$ está generado por los primeros $N-1$ modos de Legendre desplazado centrados, y esta restricción a $V_N$ es inyectiva, de modo que su núcleo es el complemento simétrico ortogonal de $V_N$ junto con todo el sector antisimétrico. Los espacios $V_N$ tienen dimensión $\binom N2$, están estrictamente anidados y su unión es densa en el espacio de Hilbert simétrico de interacción. Visibilidad y resolución estadística resultan ser cuestiones distintas: un operador de Fisher definido positivo sobre $V_N$ gobierna la segunda, es en general anisótropo y no tiene por qué ser diagonal en la base modal natural, de modo que los modos visibles pueden mezclarse antes de ser resueltos. Exhibimos además una órbita exponencial antisimétrica cuya ley de posets finitos es par en el parámetro de perturbación y cuyo primer jet no nulo es, sin embargo, exactamente de orden dos para todo $N\ge2$. Esto es una resolución diferencial local de la construcción de leyes finitas de [Bombelli2000] en S1, no una afirmación de reconstrucción no lineal ni de determinación causal universal, y no se extiende más allá de este modelo.

## 1. Introducción

[Bombelli2000] introdujo el objeto que este artículo estudia: la ley completa de un poset causal no etiquetado a cardinalidad fija $N$, muestreado a partir de una geometría lorentziana, junto con una noción estadística de cercanía entre dos leyes de ese tipo. [Janson2011] aporta el marco límite general de núcleos de posets y leyes finitas consistentes en el que se inscribe esta construcción. [Surya2026] ofrece, mediante abundancias esperadas de intervalos, un relato estrechamente relacionado de cómo aumentar $N$ puede levantar degeneraciones en esta clase de compresión causal. Ninguno de los tres calcula el diferencial de la ley a $N$ finito en una geometría de referencia, ni su núcleo, ni su rango.

Trabajamos en un modelo explícito de diamante causal de dimensión $1+1$ (S1) con una geometría nula de referencia independiente. La pregunta que planteamos es estrecha: a primer orden en una perturbación de la geometría lorentziana subyacente, ¿qué sobrevive a la aplicación que va de una perturbación continua a la ley finita del poset no etiquetado?

Dos piezas de una respuesta existen ya, en literaturas adyacentes, sin haber sido combinadas. Al nivel de permutaciones *etiquetadas* en lugar de *posets bidimensionales no etiquetados*, el diferencial de un estadístico de patrones de permutación alrededor de la referencia uniforme se conoce con cierto detalle. [EvenZohar2020] descompone el espacio completo de densidades de patrones mediante la teoría de representaciones de $S_N$, aislando el bloque de la representación estándar $V_1^{\rm EZ}$ de dimensión $(N-1)^2$, realizado explícitamente mediante $U^TA(\sigma)U$. [Kurecka2022] deriva la densidad de patrones directamente, expresando el gradiente en una base de tipo Bernstein sobre $E_N=\mathbf1^\perp$ mediante matrices de permutación comprimidas $A_\pi|_{E_N}$ y sumas de matrices de recubrimiento $\sum_\pi t_\pi A_\pi$. En nuestro convenio matricial, la distinción puede exhibirse como

$$
\mathbb R^{\mathcal C_N}
\xrightarrow{\ J_N\ }
\mathbb R^{S_N}
\xrightarrow{\ T_N\ }
\operatorname{End}(E_N),
\qquad
J_Ne_C=\mathbf1_{\Gamma_C},
\qquad
T_N(t)=\left.\sum_{\pi\in S_N}t_\pi P_\pi\right|_{E_N}.
\tag{1.1}
$$

Kurečka identifica el diferencial a nivel de permutaciones a través de la segunda flecha: su aplicación de polinomios gradiente tiene núcleo $\ker T_N$. El cociente adicional de orden causal restringe el dominio al subespacio constante sobre las fibras $\operatorname{im}J_N$. El resultado que aquí se demuestra determina la imagen de esa restricción, no meramente el núcleo de la aplicación ambiente.

El módulo objetivo abstracto tampoco es nuevo. [Diaconis1989] y la monografía ([Diaconis1988]) dan, para efectos de pares no ordenados sobre rankings, la descomposición $M^{(N-2,2)}\simeq S^{(N)}\oplus S^{(N-1,1)}\oplus S^{(N-2,2)}$ — un módulo de dimensión $\binom N2$ que es, salvo por el nombre, nuestro espacio objetivo $\operatorname{Sym}^2P_{N-1}$, ilustrado ya en 1988 con el Diallel Cross Design. Y la aplicación muchos-a-uno de permutaciones etiquetadas a posets bidimensionales no etiquetados por la que tomamos cociente es ella misma combinatoria clásica: [BayoumiElZaharKhamis1994] describen las fibras de esta aplicación explícitamente, incluida su clausura bajo $\sigma\mapsto \sigma^{-1}$ y la casi unicidad de los realizadores para posets primos.

Ninguno de estos cinco resultados da el paso adicional que los conecta: sumar el diferencial a nivel de permutaciones sobre las fibras $\Gamma_C$ de la aplicación de permutación a poset no etiquetado, y demostrar que los representantes de score dados por sumas de clase resultantes *generan* el módulo objetivo simétrico completo,

$$
\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\} =\operatorname{Sym}^2P_{N-1}.
$$

 Equivalentemente, el Teorema 1 ($\S4$) demuestra la identidad específica del orden causal

$$
\boxed{T_N(\operatorname{im}J_N)=\operatorname{Sym}(E_N).}
\tag{1.2}
$$

El núcleo exacto, el cociente identificable y el enunciado de resolución de Fisher dependen todos de este teorema de span. Los Corolarios 2 y 3 y el Teorema 4 se siguen de él; el Teorema 5 y el Corolario 6 son un enunciado de segundo orden separado y autocontenido sobre una órbita antisimétrica explícita. La Sección 8 compara (1.1)–(1.2) directamente con la técnica de matrices de recubrimiento de Kurečka.

Dicho de forma estricta, ésta es la contribución:

$$
\boxed{\begin{aligned} &\text{trabajos previos identifican la estructura ambiente a nivel de permutaciones;}\\ &\text{nosotros identificamos exactamente qué sobrevive al cociente a leyes}\\ &\text{finitas de orden causal no etiquetadas.} \end{aligned}}
$$

 Escribimos "identificamos" y "demostramos", no "por primera vez" ni "novedoso". Los ingredientes individuales anteriores tienen precedentes sustanciales, discutidos en §8. No tenemos noticia de que este teorema exacto de span de sumas de clase haya sido enunciado ya en la literatura, pero eso no es lo mismo que afirmar que no exista (§10).

No afirmamos reconstrucción no lineal, identificabilidad geométrica a distancia finita, ni resultado alguno sobre Schwarzschild, horizontes o dimensiones superiores.

Nuestras contribuciones son:

- **C1**  La identificación exacta del subespacio visible para todo $N$, $V_N=\operatorname{Sym}^2P_{N-1}$, junto con su rango $\binom N2$, su anidamiento estricto y su densidad simétrica en el espacio de Hilbert de interacción. Ésta es la principal contribución matemática del artículo, establecida a primer orden en el modelo S1 en la geometría de referencia independiente.

- **C2**  La factorización exacta de operadores $D\mathscr S_N=B_NP_N^{\rm vis}$, su núcleo y el cociente identificable que induce, junto con la separación resultante entre qué direcciones tangentes son visibles y con qué intensidad las resuelve la ley finita a través de $F_N$. Ésta es la principal formulación operatorial del artículo; es un corolario funcional del span exacto de C1, no una teoría nueva independiente.

- **C3**  La retención asintótica de información de Fisher en el sector simétrico de Hilbert–Schmidt, junto con espectros finitos exactos ilustrativos. Éste es un resultado cuantitativo de resolución, enunciado para un canal explícito y una normalización de referencia.

- **C4**  La detectabilidad exacta de segundo orden $r_N(\gamma_\psi)=2$ para todo $N\ge2$ de una órbita antisimétrica explícita. Ésta es una extensión breve y autocontenida que establece existencia estructural, no una clasificación del sector antisimétrico completo $\bigwedge^2H$.

## 2. El modelo S1 y los experimentos finitos de orden causal

Trabajamos en el diamante causal plano de dimensión $1+1$ en coordenadas nulas, reparametrizado a $D=[0,1]^2$ con el orden producto $(u,v)\preceq(u',v')\iff u\le u',\,v\le v'$, y la medida de referencia uniforme $\mu_0(du\,dv)=du\,dv$. Un generador conforme $\psi\in C(D;\mathbb R)$ define la familia exponencial normalizada

$$
g_\varepsilon=\frac{e^{2\varepsilon\psi}}{Z(\varepsilon)}g_0,\qquad Z(\varepsilon)=\int_De^{2\varepsilon\psi}\,d\mu_0,
$$

 que preserva el volumen total para todo $\varepsilon$ — no sólo a primer orden — e induce la densidad de muestreo $q_\varepsilon=e^{2\varepsilon \psi}/Z(\varepsilon)$ para un sprinkling de Poisson condicionado a $N$ puntos. Derivando en $\varepsilon=0$ se obtiene la tangente métrica $\dot g_0=2(\psi-\bar\psi)g_0$, siendo $\bar\psi$ la media de $\psi$ bajo $\mu_0$.

Cuatro objetos distintos aparecen a lo largo de la cadena que va de la geometría al estadístico, y los mantenemos separados notacionalmente en todo el texto: el generador geométrico $\psi$; la log-tangente de la densidad conjunta normalizada $t_\psi=2(\psi-\bar\psi)$; la tangente de la densidad de cópula $h_\psi$, obtenida tras uniformizar ambas marginales,

$$
h_\psi(u,v)=2\big[\psi(u,v)-\psi_U(u)-\psi_V(v)+\bar\psi\big] =2\mathcal P\psi,\qquad \mathcal P=(I-M_u)(I-M_v),
$$

 siendo $\psi_U,\psi_V$ las dos medias marginales de $\psi$ y $\mathcal P$ la proyección de doble centrado usada a lo largo de §§4–6; y el score $S_{N,\psi}$ del experimento discreto finito, definido más abajo. Las densidades conjunta y de cópula valen ambas $1$ en $\varepsilon=0$, de modo que $t_\psi$ y $h_\psi$ coinciden allí en valor pero no son el mismo objeto — difieren en los dos términos marginales, y sólo $h_\psi$ es lo que el experimento finito ve realmente, puesto que pasar a rangos aplica la transformada integral de probabilidad marginal y elimina la información marginal.

Una muestra de $N$ puntos genera tres observaciones progresivamente más gruesas. En el nivel más fino está la muestra continua $(U_k,V_k)_{k=1}^N$ misma, con score $T_{N,\psi}=\sum_kh_\psi(U_k,V_k)$. Ordenar por $U$ y registrar el rango inducido en $V$ produce una permutación de rangos *etiquetada* $\Pi_N\in S_N$; su score es la esperanza condicional

$$
S_{N,\psi}(\pi)=\mathbb E_0[T_{N,\psi}\mid\Pi_N=\pi],
$$

 una identidad que no requiere hipótesis de independencia tras condicionar y se sigue directamente de la verosimilitud. Finalmente — y éste es el nivel en el que vive realmente la ley finita de orden causal — el poset bidimensional *no etiquetado* es la clase de isomorfismo $[P_{\Pi_N}]$ de la matriz de permutación: $\Pi_N$ depende de qué realizador lineal de $U$ y de $V$ se use, pero el dato de orden puro que un conjunto causal expone es exactamente esta clase de isomorfismo, invariante bajo el realizador. El cociente de la permutación etiquetada $\Pi_N$ al poset no etiquetado $[P_{\Pi_N}]$ — y qué sobrevive exactamente a él — es el tema de §§4–5.

Escribimos $\mathcal C_N$ para el conjunto de clases de isomorfismo de posets bidimensionales realizados por algún $\sigma\in S_N$, y para $C\in\mathcal C_N$ sea $\Gamma_C:=\{\sigma\in S_N:[P_\sigma]=C\}$ su fibra bajo $\sigma\mapsto[P_\sigma]$. El objeto sobre el que trata el enunciado tangente de este artículo es la ley del poset no etiquetado misma,

$$
\mu_{N,\varepsilon}^{[P]}(C) :=\mathbb P_\varepsilon\big([P_{\Pi_N}]=C\big) =\sum_{\sigma\in\Gamma_C}p_\varepsilon(\sigma), \qquad C\in\mathcal C_N,
$$

 con valor de referencia $\mu_{N,0}(C)=|\Gamma_C|/N!$. Esto cierra la cadena con la que trabaja el resto del artículo:

$$
\psi\ \longrightarrow\ \dot g_0\ \longrightarrow\ t_\psi\ \longrightarrow\ h_\psi\ \longrightarrow\ S_{N,\psi}\ \longrightarrow\ \mu_{N,\varepsilon}^{[P]}.
$$

En todo el texto, $H=L_0^2([0,1])$ denota el espacio $L^2$ de media cero con la base de Legendre desplazado, $P_{N-1}=\operatorname{span}\{p_1,\ldots, p_{N-1}\}\subset H$ sus primeros $N-1$ modos, y las derivadas de las leyes a $N$ finito en $\varepsilon=0$ se leen como scores bajo la identificación de diferenciabilidad en media cuadrática (QMD), especializando la construcción de leyes finitas de [Bombelli2000] a esta familia exponencial S1.

## 3. Representantes de score de la ley finita

Para $i=1,\ldots,N$, sea

$$
d_i^{(N)}(t) :=N\binom{N-1}{i-1}t^{i-1}(1-t)^{N-i} \tag{3.1}
$$

 la densidad del $i$-ésimo estadístico de orden en una muestra de $N$ variables uniformes independientes, y defínase su versión centrada

$$
b_i^{(N)}:=d_i^{(N)}-1. \tag{3.2}
$$

 Las funciones normalizadas $d_i^{(N)}/N$ forman la base de Bernstein de grado $N-1$. Puesto que

$$
\sum_{i=1}^N d_i^{(N)}=N, \qquad \sum_{i=1}^N b_i^{(N)}=0,
$$

 el centrado deja exactamente una relación lineal y por tanto

$$
\operatorname{span}\{b_1^{(N)},\ldots,b_N^{(N)}\}=P_{N-1}. \tag{3.3}
$$

Sea $f=\mathcal P\psi\in H\widehat\otimes H$ una tangente de interacción S1 admisible, de modo que el score de una observación de la cópula en el modelo de referencia es $2f$. Si $p_\varepsilon(\sigma)$ denota la probabilidad de la permutación de rangos $\sigma\in S_N$, la derivación de su verosimilitud finita da

$$
p_\sigma'(0;f) =\frac2{N!}\sum_{i=1}^N \left\langle f, d_i^{(N)}\otimes d_{\sigma(i)}^{(N)}\right\rangle. \tag{3.4}
$$

 Ambas marginales de $f$ se anulan. Por tanto cada $d_i^{(N)}$ en (3.4) puede sustituirse por $b_i^{(N)}$, y el representante a nivel de permutaciones se define por

$$
\boxed{ R_\sigma^{(N)} :=\frac2{N!}\sum_{i=1}^N b_i^{(N)}\otimes b_{\sigma(i)}^{(N)}, \qquad p_\sigma'(0;f)=\langle f,R_\sigma^{(N)}\rangle.} \tag{3.5}
$$

 En particular, $R_\sigma^{(N)}\in P_{N-1}\otimes P_{N-1}$. La fórmula (3.5), obtenida inicialmente para tangentes continuas admisibles, define también un funcional lineal continuo de todo $f\in H\widehat\otimes H$; más abajo usamos esta extensión al espacio de Hilbert sin afirmar que todo $f$ de ese tipo sea geométricamente realizable.

Recuérdese de §2 que $\mathcal C_N$ es el conjunto de clases de posets bidimensionales no etiquetados generadas a cardinalidad $N$, y $\Gamma_C=\{\sigma\in S_N:[P_\sigma]=C\}$ es la fibra de $C\in\mathcal C_N$. El representante de clase es

$$
\boxed{ R_C^{(N)}:=\sum_{\sigma\in\Gamma_C}R_\sigma^{(N)}.} \tag{3.6}
$$

 Puesto que $\mu_{N,0}(C)=|\Gamma_C|/N!>0$, sumar (3.5) sobre la fibra da

$$
\left.\frac{d}{d\varepsilon} \mu_{N,\varepsilon}^{[P]}(C)\right|_{\varepsilon=0} =\langle f,R_C^{(N)}\rangle, \qquad (D\mathscr S_Nf)(C) =\frac{\langle f,R_C^{(N)}\rangle}{\mu_{N,0}(C)}. \tag{3.7}
$$

 Así, $D\mathscr S_Nf$ es exactamente el score de la ley finita del poset no etiquetado. Su media respecto de $\mu_{N,0}$ es cero porque las derivadas en (3.7) suman cero sobre $C$.

Cada fibra es cerrada bajo inversión: si $i<j$ entonces $\sigma(i)<\sigma(j)$, de modo que tomando $a=\sigma(i)$, $b=\sigma(j)$ se obtiene $a<b$ y $\sigma^{-1}(a)=i<j=\sigma^{-1}(b)$, es decir, $i\mapsto\sigma(i)$ es un isomorfismo de posets $P_{\sigma^{-1}}\cong P_\sigma$, de modo que intercambiar las dos coordenadas de rango envía $\sigma$ a $\sigma^{-1}$ sin cambiar el poset abstracto. En consecuencia,

$$
\sigma\in\Gamma_C\Longleftrightarrow\sigma^{-1}\in\Gamma_C, \qquad \left(R_\sigma^{(N)}\right)^\top=R_{\sigma^{-1}}^{(N)},
$$

 y por tanto

$$
\boxed{ \left(R_C^{(N)}\right)^\top=R_C^{(N)}, \qquad R_C^{(N)}\in\operatorname{Sym}^2P_{N-1}.} \tag{3.8}
$$

La forma bilineal de Fisher del experimento del poset no etiquetado se define, por tanto, mediante

$$
\boxed{ G_{[P]}^{(N)}(f,g) :=\langle D\mathscr S_Nf,D\mathscr S_Ng\rangle_{L^2(\mu_{N,0})} =\sum_{C\in\mathcal C_N} \frac{\langle f,R_C^{(N)}\rangle \langle g,R_C^{(N)}\rangle}{\mu_{N,0}(C)}.} \tag{3.9}
$$

 Como toda masa de referencia es estrictamente positiva,

$$
\ker D\mathscr S_N=\ker G_{[P]}^{(N)} =\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}^{\perp},
$$

 y el espacio visible es equivalentemente

$$
\boxed{ V_N :=(\ker D\mathscr S_N)^\perp =\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\} \subseteq\operatorname{Sym}^2P_{N-1}.} \tag{3.10}
$$

 Ésta es la inclusión superior usada en §4.

Para enunciar la reducción finita restante, pongamos

$$
E_N:=\mathbf1^\perp\subset\mathbb R^N, \qquad \Lambda_N:E_N\longrightarrow P_{N-1}, \qquad \Lambda_Nz:=\sum_{i=1}^Nz_i b_i^{(N)}. \tag{3.11}
$$

 La ecuación (3.3) y la única relación $\sum_i b_i^{(N)}=0$ muestran que $\Lambda_N$ es un isomorfismo. Fijemos el convenio de matrices de permutación

$$
P_\sigma:=\sum_{i=1}^Ne_i e_{\sigma(i)}^\top, \qquad A_C:=\sum_{\sigma\in\Gamma_C}P_\sigma. \tag{3.12}
$$

 La clausura de $\Gamma_C$ bajo inversión hace $A_C$ simétrica, y (3.5)–(3.6) dan exactamente

$$
R_C^{(N)} =\frac2{N!}\sum_{i,j=1}^N(A_C)_{ij} b_i^{(N)}\otimes b_j^{(N)}. \tag{3.13}
$$

 Transportar mediante el isomorfismo $\Lambda_N$ reduce por tanto la inclusión recíproca de (3.10) a

$$
\boxed{ V_N=\operatorname{Sym}^2P_{N-1} \quad\Longleftrightarrow\quad \operatorname{span}\{A_C|_{E_N}:C\in\mathcal C_N\} =\operatorname{Sym}(E_N).} \tag{3.14}
$$

 La Sección 4 demuestra el enunciado de la derecha de forma constructiva para todo $N\ge2$. La maquinaria diferencial de Bernstein y a nivel de permutaciones de esta sección no se reivindica como nueva; la contribución para todo $N$ aislada en §4 es el span que sobrevive tras sumar sobre las fibras del poset no etiquetado.

## 4. Subespacios visibles exactos para todo $N$

Por (3.10), el espacio visible $V_N=\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}$ satisface $V_N\subseteq\operatorname{Sym}^2P_{N-1}$. Bajo el isomorfismo $\Lambda_N$ de (3.11), la ecuación (3.14) reduce la inclusión recíproca al siguiente enunciado puramente combinatorio sobre las sumas de clase definidas en (3.12):

$$
\operatorname{span}\{A_C|_{E_N}:C\in\mathcal C_N\}=\operatorname{Sym}(E_N). \tag{4.1}
$$

**Teorema 1 (span de sumas de clase).** *Para todo $N\ge2$,*

$$
\boxed{V_N=\operatorname{Sym}^2P_{N-1},\qquad \dim V_N=\operatorname{rank}G_{[P]}^{(N)}=\binom N2.}
$$

 *Equivalentemente, $T_N(\operatorname{im}J_N)=\operatorname{Sym}(E_N)$. La demostración es constructiva para todo $N$: exhibe una familia explícita de $\binom N2$ clases de posets cuyos representantes de score generan el espacio objetivo, sin enumerar posets ni extrapolar desde $N$ pequeños.*

*Demostración.* Establecemos (4.1) en tres pasos.

**Una familia de $\binom N2$ posets casi cadena.** Para enteros $0\le a<b\le N-1$, defínase $C_{a,b}$ sobre una cadena $c_1<\cdots<c_{N-1}$ junto con un elemento adicional $z$ que satisface $c_i<z$ para $i\le a$, $z<c_i$ para $i>b$, y $z$ incomparable con $c_{a+1},\ldots,c_b$. Toda extensión lineal inserta $z$ tras exactamente $k\in\{a,\ldots,b\}$ elementos de la cadena, y dos extensiones realizan la misma relación de orden exactamente cuando $\{s,t\}=\{a,b\}$: el poset tiene exactamente dos pares de extensiones lineales, lo que da, una vez normalizada la cadena a $1<\cdots<N$, un único ciclo $\tau_{a,b}$ sobre el intervalo consecutivo $I_{a,b}=\{a+1,\ldots, b+1\}$ y su inverso. Por tanto

$$
\Gamma_{C_{a,b}}=\{\tau_{a,b},\tau_{a,b}^{-1}\}
$$

 (una única transposición, sin multiplicidad, cuando $b=a+1$). El multiconjunto de cardinalidades del pasado estricto $\{|\mathrm{Past}(y)|:y\in C_{a,b}\}=\{0,\ldots,b-1,b+1,\ldots,N-1\}\uplus\{a\}$ omite $b$ y repite $a$, de modo que determina el par $(a,b)$: las $\binom N2$ clases $C_{a,b}$ son distintas dos a dos.

**De ciclos de intervalo a laplacianos de arista.** Para $1\le i<j\le N$ sea $L_{ij}:=(e_i-e_j)(e_i-e_j)^\top$ el laplaciano de la arista $\{i,j\}$ en el grafo completo sobre $N$ vértices. Restringidas a $E_N$, las $\binom N2$ matrices $\{L_{ij}\}$ son linealmente independientes — una combinación nula fuerza a anularse a todo coeficiente fuera de la diagonal, y por tanto a todo $w_{ij}$ — de modo que forman una base de $\operatorname{Sym}(E_N)$; satisfacen además $\sum_{i<j}L_{ij}=NI_{E_N}$. Pongamos $S_{a,b}:=P_{\tau_{a,b}}+P_{\tau_{a,b}}^\top$ — igual a $2A_{C_{a,b}}$ cuando $b=a+1$ y a $A_{C_{a,b}}$ en otro caso, un escalar no nulo en ambos casos — y $Q_{a,b}:=2I_{E_N}-S_{a,b}|_{E_N}$. Como $\tau_{a,b}$ es el ciclo consecutivo sobre $I_{a,b}$, $Q_{a,b}$ es exactamente el laplaciano de grafo de ese ciclo: $Q_{a,a+1}=2L_{a+1,a+2}$, y para $b>a+1$, $Q_{a,b}=L_{a+1,b+1}+\sum_{k=a+1}^bL_{k,k+1}$. Estas dos identidades triangularizan por longitud de intervalo y se invierten limpiamente — $L_{i,i+1}=\tfrac12Q_{i-1,i}$, y para $j>i+1$, $L_{ij}=Q_{i-1,j-1}-\tfrac12\sum_{k=i}^{j-1}Q_{k-1,k}$ — de modo que

$$
\operatorname{span}\{Q_{a,b}\}=\operatorname{span}\{L_{ij}:i<j\} =\operatorname{Sym}(E_N). \tag{4.2}
$$

 Queda exactamente una laguna: (4.2) usa el término común $2I_{E_N}$ restado de todo $Q_{a,b}$, de modo que no muestra por sí sola que las sumas de clase $S_{a,b}$ generen el mismo espacio.

**Cerrando la laguna: la identidad es ella misma una combinación de sumas de clase.** De $\sum_{i<j}L_{ij}=NI_{E_N}$ y de las identidades triangularizadas anteriores, $I_{E_N}=\sum_{a<b}c_{a,b}Q_{a,b}$ para coeficientes explícitos $c_{a,b}$ cuya suma depende únicamente de cuántas aristas hay a cada distancia $d=j-i$:

$$
s_N:=\sum_{a<b}c_{a,b} =\frac1N\sum_{d=1}^{N-1}(N-d)\Bigl(1-\frac d2\Bigr) =\frac{(N-1)(5-N)}{12}.
$$

 Sustituyendo $Q_{a,b}=2I_{E_N}-S_{a,b}|_{E_N}$ se obtiene $(1-2s_N)I_{E_N}=-\sum_{a<b}c_{a,b}S_{a,b}|_{E_N}$, y el coeficiente

$$
1-2s_N=\frac{N^2-6N+11}6=\frac{(N-3)^2+2}6
$$

 es estrictamente positivo para todo entero $N$ — nunca se anula, ni en $N=3$ ni en ningún otro sitio — de modo que $I_{E_N}\in\operatorname{span}\{S_{a,b}|_{E_N}\}$. Reintroduciendo esto en $Q_{a,b}=2I_{E_N}-S_{a,b}|_{E_N}$ se ve que todo $Q_{a,b}$ está él mismo en ese span y, junto con (4.2),

$$
\operatorname{span}\{S_{a,b}|_{E_N}:a<b\}=\operatorname{Sym}(E_N).
$$

 Puesto que cada $S_{a,b}$ es $A_{C_{a,b}}$ salvo un escalar no nulo, esto es exactamente (4.1). Combinado con la reducción de §3, esto demuestra el Teorema 1. $\square$

**Corolario 2 (filtración).** Puesto que $P_{N-1}\subsetneq P_N$,

$$
V_N=\operatorname{Sym}^2P_{N-1}\subsetneq\operatorname{Sym}^2P_N=V_{N+1} \qquad(N\ge2),
$$

 con sucesión de rangos $1,3,6,10,15,\ldots,\binom N2,\ldots$ — una inclusión estricta, no meramente no decreciente, en cada paso. Un testigo universal de cada nuevo grado es $p_1\otimes p_N+p_N\otimes p_1\in V_{N+1}\setminus V_N$: como la forma de Fisher es definida positiva sobre $V_{N+1}$ y se anula en $V_N^\perp$, $I_N^{[P]}(p_1\otimes p_N)=0$ mientras que $I_{N+1}^{[P]}(p_1\otimes p_N)>0$ — el mismo testigo reaparece en los cálculos de Fisher de §6. Como los polinomios centrados son densos en $H=L_0^2([0,1])$, el Teorema 1 da también, incondicionalmente,

$$
\overline{\bigcup_{N\ge2}V_N}=H\widehat\otimes_{\mathrm{sym}}H.
$$

El núcleo exacto de $D\mathscr S_N$ — el complemento ortogonal de $V_N$ junto con el sector antisimétrico permanentemente invisible $\bigwedge^2H$ — no se deriva aquí; es el Corolario 3, §5, la consecuencia funcional directa del Teorema 1 una vez conocido el span.

La reducción finita usada en el argumento queda registrada en el Apéndice B, mientras que el Apéndice C recoge la construcción casi cadena y laplaciana con todo detalle.

## 5. Factorización de operadores y cociente identificable

Sea

$$
\mathcal X:=H\widehat\otimes H, \qquad \mathcal K_N:=L_0^2(\mathcal C_N,\mu_{N,0}),
$$

 donde $\mathcal K_N$ es el espacio de Hilbert de scores de media cero de la ley finita del poset no etiquetado en el modelo de referencia. Bajo la identificación QMD de §2, escribimos

$$
D\mathscr S_N:\mathcal X\longrightarrow\mathcal K_N
$$

 para su diferencial de score acotado. El subespacio visible es, por definición,

$$
V_N=(\ker D\mathscr S_N)^\perp. \tag{5.1}
$$

 El Teorema 1 identifica este soporte abstracto de forma exacta:

$$
V_N=\operatorname{Sym}^2P_{N-1}. \tag{5.2}
$$

 Denotemos por $\Pi_{\rm sym}$ la proyección ortogonal de $\mathcal X$ sobre $H\widehat\otimes_{\rm sym}H$, por $\Pi_{V_N}$ la proyección de este último espacio sobre $V_N$, y pongamos

$$
P_N^{\rm vis}:=\Pi_{V_N}\Pi_{\rm sym}. \tag{5.3}
$$

 Así,

$$
\mathcal X =V_N\oplus V_N^{\perp_{\rm sym}} \oplus\bigwedge\nolimits^2H, \qquad \ker P_N^{\rm vis} =V_N^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H. \tag{5.4}
$$

**Corolario 3 (factorización exacta, núcleo y cociente identificable).** *Para todo $N\ge2$, sea*

$$
B_N:=D\mathscr S_N|_{V_N}:V_N\longrightarrow\mathcal K_N.
$$

 *Entonces $B_N$ es inyectiva y*

$$
\boxed{D\mathscr S_N=B_NP_N^{\rm vis}}, \tag{5.5}
$$

$$
\boxed{ \ker D\mathscr S_N =V_N^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H =\left(\operatorname{Sym}^2P_{N-1}\right)^{\perp_{\rm sym}} \oplus\bigwedge\nolimits^2H.} \tag{5.6}
$$

 *Si $q_N:\mathcal X\to\mathcal X/\ker D\mathscr S_N$ es la aplicación cociente, entonces*

$$
U_N:\mathcal X/\ker D\mathscr S_N\longrightarrow V_N, \qquad U_N([f])=P_N^{\rm vis}f, \tag{5.7}
$$

 *es un isomorfismo isométrico canónico para la norma cociente de Hilbert, y el diferencial admite la factorización inducida única*

$$
\mathcal X\xrightarrow{\ q_N\ } \mathcal X/\ker D\mathscr S_N \xrightarrow{\ U_N\ }V_N \xrightarrow{\ B_N\ }\mathcal K_N, \qquad D\mathscr S_N=B_NU_Nq_N. \tag{5.8}
$$

 *En particular,*

$$
\boxed{ \mathcal X/\ker D\mathscr S_N \simeq V_N=\operatorname{Sym}^2P_{N-1}, \qquad \dim\bigl(\mathcal X/\ker D\mathscr S_N\bigr)=\binom N2.} \tag{5.9}
$$

*Demostración.* La descomposición ortogonal $\mathcal X=(\ker D\mathscr S_N)^\perp\oplus\ker D\mathscr S_N$ da $D\mathscr S_Nf=D\mathscr S_NP_N^{\rm vis}f$, que es (5.5). La restricción $B_N$ es inyectiva porque su dominio es $(\ker D\mathscr S_N)^\perp$. Las ecuaciones (5.2) y (5.4) dan entonces (5.6). Por último, (5.6) hace que (5.7) esté bien definida y sea biyectiva, mientras que

$$
\|[f]\|_{\mathcal X/\ker D\mathscr S_N} =\inf_{k\in\ker D\mathscr S_N}\|f+k\|_{\mathcal X} =\|P_N^{\rm vis}f\|_{\mathcal X};
$$

 de modo que $U_N$ es isométrica y (5.8) se sigue. $\square$

En particular, para dos tangentes de interacción $f,g\in\mathcal X$,

$$
D\mathscr S_Nf=D\mathscr S_Ng \quad\Longleftrightarrow\quad [f]=[g]\text{ en }\mathcal X/\ker D\mathscr S_N \quad\Longleftrightarrow\quad P_N^{\rm vis}f=P_N^{\rm vis}g. \tag{5.10}
$$

 Éste es el sentido preciso en el que la ley finita identifica el cociente: es un enunciado sobre su primer diferencial en el modelo de referencia, no sobre identificabilidad no lineal de geometrías a distancia finita.

El Apéndice D recoge los argumentos de núcleo, cociente, anidamiento estricto y densidad usados aquí.

La proyección $P_N^{\rm vis}$ especifica **qué** direcciones tangentes sobreviven; no especifica con qué intensidad codifica la ley finita las distintas direcciones supervivientes. Ese segundo dato es

$$
F_N:=B_N^*B_N:V_N\longrightarrow V_N, \qquad D\mathscr S_N^*D\mathscr S_N =P_N^{\rm vis}F_NP_N^{\rm vis}. \tag{5.11}
$$

 Puesto que $B_N$ es inyectiva y $V_N$ es de dimensión finita, $F_N$ es definido positivo sobre $V_N$; no tiene por qué ser la identidad y no debe confundirse con la proyección de soporte. Su espectro y su anisotropía corresponden a §6.

## 6. Resolución de Fisher dentro del sector visible

Para $f\in\mathcal X=H\widehat\otimes H$, la información de Fisher en la ley finita del poset no etiquetado es

$$
I_N^{[P]}(f) :=G_{[P]}^{(N)}(f,f) =\|D\mathscr S_Nf\|_{L^2(\mu_{N,0})}^2 =\big\langle P_N^{\rm vis}f, F_NP_N^{\rm vis}f\big\rangle. \tag{6.1}
$$

 El experimento continuo de referencia consta de $N$ observaciones independientes de la cópula, cuyo score es $2\sum_{k=1}^Nf(U_k,V_k)$. Su forma de Fisher es por tanto $4N\langle f,g\rangle$. La usamos únicamente como normalización explícita y ponemos

$$
\widehat F_N :=\frac1{4N}P_N^{\rm vis}F_NP_N^{\rm vis} =\frac1{4N}D\mathscr S_N^*D\mathscr S_N \quad\text{en }\mathcal X. \tag{6.2}
$$

 Por procesamiento de datos y el Corolario 3,

$$
0\le\widehat F_N\le I_{\mathcal X}, \qquad \operatorname{supp}\widehat F_N=V_N, \qquad \ker\widehat F_N=\ker D\mathscr S_N. \tag{6.3}
$$

 Así, $P_N^{\rm vis}$ fija el soporte, mientras que los autovalores no nulos de $\widehat F_N$ cuantifican la resolución dentro de ese soporte. En general

$$
\widehat F_N\ne P_N^{\rm vis} \qquad\text{y, equivalentemente,}\qquad F_N\ne4N I_{V_N}. \tag{6.4}
$$

**Espectros exactos a cardinalidad baja.** Para obtener fórmulas racionales compactas pongamos

$$
x(t):=t-\frac12,\qquad q(t):=\left(t-\frac12\right)^2-\frac1{12},\qquad r(t):=\left(t-\frac12\right)^3       -\frac3{20}\left(t-\frac12\right). \tag{6.5}
$$

 Éstos son mutuamente ortogonales y generan sucesivamente $P_1,P_2,P_3$. Para $N=2$, con $e_{11}=x\otimes x$,

$$
G_{[P]}^{(2)}(f,g) =256\langle f,e_{11}\rangle\langle g,e_{11}\rangle, \qquad \operatorname{spec}_+(\widehat F_2)=\left\{\frac29\right\}. \tag{6.6}
$$

 Para $N=3$, en la base ortogonal

$$
e_{11}=x\otimes x,\qquad e_{12}=x\otimes q+q\otimes x,\qquad e_{22}=q\otimes q,
$$

 las formas del poset y de la referencia continua son respectivamente

$$
[G_{[P]}^{(3)}] =\operatorname{diag}\left(\frac1{32},\frac1{1200}, \frac1{180000}\right), \qquad [G_{\rm full}^{(3)}] =\operatorname{diag}\left(\frac1{12},\frac1{90}, \frac1{2700}\right). \tag{6.7}
$$

 Por tanto

$$
\boxed{ \operatorname{spec}_+(\widehat F_3) =\left\{\frac38,\frac3{40},\frac3{200}\right\},} \tag{6.8}
$$

 con autovectores $e_{11},e_{12},e_{22}$, en ese orden. El espacio visible es ya anisótropo: la pertenencia al soporte no determina por sí sola la intensidad de Fisher retenida.

En $N=4$, úsese

$$
\begin{aligned} e_{11}&:=x\otimes x,& e_{12}&:=x\otimes q+q\otimes x,& e_{13}&:=x\otimes r+r\otimes x,\\ e_{22}&:=q\otimes q,& e_{23}&:=q\otimes r+r\otimes q,& e_{33}&:=r\otimes r. \end{aligned} \tag{6.9}
$$

 Tres autovectores generalizados permanecen puros:

$$
\widehat F_4e_{11}=\frac{12}{25}e_{11}, \qquad \widehat F_4e_{12}=\frac4{25}e_{12}, \qquad \widehat F_4e_{23}=\frac4{525}e_{23}. \tag{6.10}
$$

 El bloque invariante restante es $\operatorname{span}\{e_{13},e_{22},e_{33}\}$. En esa base ordenada, las restricciones de las dos formas bilineales son

$$
[G_{[P]}^{(4)}]_{\rm mix} =\begin{pmatrix} 1/55125&1/354375&1/38587500\\ 1/354375&11/455625&-1/49612500\\ 1/38587500&-1/49612500&11/5402250000 \end{pmatrix},
$$

$$
[G_{\rm full}^{(4)}]_{\rm mix} =\operatorname{diag}\left(\frac1{1050},\frac1{2025}, \frac1{490000}\right). \tag{6.11}
$$

 Sus tres autovalores generalizados son las raíces reales positivas de

$$
144703125\lambda^3-9975000\lambda^2+142000\lambda-128=0, \tag{6.12}
$$

 a saber, sólo a título orientativo,

$$
0.0494521212879\ldots,\qquad 0.0185160720400\ldots,\qquad 0.000966047034941\ldots.
$$

 Por tanto el espectro exacto queda especificado por (6.10) y (6.12), y su orden numérico decreciente es

$$
\frac{12}{25}>\frac4{25}>0.0494521212879\ldots> 0.0185160720400\ldots>\frac4{525}> 0.000966047034941\ldots>0. \tag{6.13}
$$

 Las entradas fuera de la diagonal en (6.11) constituyen la primera mezcla modal explícita: $e_{13},e_{22},e_{33}$ son visibles pero no son individualmente autovectores de Fisher.

**Teorema 4 (resolución de Fisher y retención asintótica).** Sea $S_N^\Pi(f)$ el score antes del cociente, cuando se observa la permutación de rangos completa $\Pi_N$, y pongamos

$$
I_N^\Pi(f):=\mathbb E_0[S_N^\Pi(f)^2], \qquad \Delta_N(f):=I_N^\Pi(f)-I_N^{[P]}(f). \tag{6.14}
$$

 La esperanza condicional de los scores a lo largo de $\Pi_N\mapsto[P_{\Pi_N}]$ da

$$
\Delta_N(f) =\mathbb E_0\!\left[ \operatorname{Var}_0\!\left(S_N^\Pi(f)\mid[P_{\Pi_N}]\right) \right]\ge0. \tag{6.15}
$$

 Para todo $f\in\mathcal X$,

$$
\frac{I_N^\Pi(f)}N\longrightarrow4\|f\|_{\mathcal X}^2. \tag{6.16}
$$

 Si además $f\in H\widehat\otimes_{\rm sym}H$, entonces

$$
\frac{\Delta_N(f)}N\longrightarrow0, \qquad \frac{I_N^{[P]}(f)}N\longrightarrow4\|f\|_{\mathcal X}^2. \tag{6.17}
$$

 Para toda $f$ simétrica no nula, (6.16) da un umbral finito, en general no uniforme, $N_0(f)$ tal que $I_N^\Pi(f)>0$ para todo $N\ge N_0(f)$. En ese rango definimos las dos etapas y su producto con la notación siguiente; se usa $\kappa_N$ para la segunda etapa porque $q_N$ ya denota la aplicación cociente en el Corolario 3:

$$
\rho_N(f):=\frac{I_N^\Pi(f)}{4N\|f\|^2}, \qquad \kappa_N(f):=\frac{I_N^{[P]}(f)}{I_N^\Pi(f)}, \qquad \eta_N^{\rm tot}(f):=\rho_N(f)\kappa_N(f) =\frac{I_N^{[P]}(f)}{4N\|f\|^2}. \tag{6.18}
$$

 Entonces

$$
\boxed{ \rho_N(f)\longrightarrow1, \qquad \kappa_N(f)\longrightarrow1, \qquad \eta_N^{\rm tot}(f)\longrightarrow1.} \tag{6.19}
$$

 El primer límite concierne a las observaciones continuas frente a los rangos; el segundo, a los rangos frente al poset no etiquetado. Son afirmaciones distintas y ninguna se infiere de las inclusiones estrictas $V_N\subsetneq V_{N+1}$.

Equivalentemente, sobre el espacio de Hilbert de interacción completo,

$$
\boxed{ \widehat F_N\xrightarrow{\rm SOT}\Pi_{\rm sym}.} \tag{6.20}
$$

 Más generalmente, si $0\ne f=f_s+f_a$ es su descomposición ortogonal simétrica–antisimétrica, entonces

$$
\frac{I_N^{[P]}(f)}{4N\|f\|^2} \longrightarrow \frac{\|f_s\|^2}{\|f_s\|^2+\|f_a\|^2}. \tag{6.21}
$$

 En particular, el sector antisimétrico contribuye cero al numerador para todo $N$, no meramente de forma asintótica.

*Demostración.* Defínase

$$
H_{ij}^{(N)}(f) :=\iint f(s,t)d_i^{(N)}(s)d_j^{(N)}(t)\,ds\,dt. \tag{6.22}
$$

 Sus sumas por filas y por columnas se anulan para $f\in\mathcal X$, y el score de la permutación es $S_N^\Pi(f)=2\sum_iH_{i,\Pi_N(i)}^{(N)}(f)$. Promediar directamente sobre una permutación uniforme da la identidad de Gram exacta

$$
I_N^\Pi(f)=\frac4{N-1}\|H^{(N)}(f)\|_F^2. \tag{6.23}
$$

 El operador normalizado de estadísticos de orden tiene los autovalores de Legendre desplazado

$$
\lambda_{N-1,m} =\prod_{r=1}^m\frac{N-r}{N+r}\in[0,1], \qquad \lambda_{N-1,m}\longrightarrow1 \quad(m\text{ fijo}). \tag{6.24}
$$

 Desarrollar $f$ en la base tensorial de Legendre y aplicar convergencia dominada a (6.23) demuestra (6.16). Para tensores simétricos de rango finito, el teorema de la fibra da $\Delta_N(f)/N\to0$. La cota uniforme

$$
0\le\frac{\Delta_N(f)}N\le8\|f\|_{\mathcal X}^2 \tag{6.25}
$$

 extiende este límite a la clausura simétrica de Hilbert–Schmidt completa mediante una aproximación de rango fijo seguida de $N\to\infty$, lo que demuestra (6.17). Las ecuaciones (6.18)–(6.19) se siguen por división sólo una vez que el denominador es positivo. La simetría de inversión aniquila el score condicional antisimétrico en toda fibra de posets, lo que da (6.21). Por último, (6.17), (6.21), la polarización y $0\le\widehat F_N\le I$ implican (6.20). $\square$

La convergencia en (6.20) no es convergencia en norma de operadores. En efecto, para el vector unitario $h_N:=p_N\otimes p_N/\|p_N\|_{L^2}^2$, el Teorema 1 da $h_N\perp V_N$, de modo que

$$
\widehat F_Nh_N=0, \qquad \Pi_{\rm sym}h_N=h_N, \qquad \|\widehat F_N-\Pi_{\rm sym}\|\ge1 \quad\text{para todo }N. \tag{6.26}
$$

 Tampoco (6.20) convierte a $\widehat F_N$ en una proyección a $N$ finito: ya (6.6) da su autovalor no nulo $2/9$. La tasa genérica en (6.17)–(6.21) es sólo $o_f(1)$, sin tasa ni umbral uniformes sobre la esfera unidad de Hilbert–Schmidt. La tasa disponible $1-\kappa_N(f)=O(N^{-1/2})$ se aplica únicamente a la subclase continua acotada de rango finito.

Estos enunciados conciernen a la compleción de Hilbert de las tangentes de interacción S1. Se transfieren directamente a las trayectorias geométricas admisibles ya construidas en esa clase, pero no afirman la realizabilidad geométrica de un tensor de Hilbert–Schmidt arbitrario. Los espectros finitos anteriores comparan la ley del poset no etiquetado con $N$ observaciones continuas de la cópula; no son fracciones de la geometría completa, no implican reconstrucción y no establecen monotonía de los autovalores de Fisher individuales con $N$.

El Apéndice E hace explícito el paso de retención: (E.15) identifica el evento de fibra de alta probabilidad, (E.16) demuestra la cota de pérdida a rango finito, y (E.17)–(E.19) pasan a la clausura simétrica de Hilbert–Schmidt completa. El Apéndice F registra las matrices exactas y los espectros generalizados para $N=2,3,4$.

## 7. Una órbita antisimétrica visible a segundo orden

Sean $\ell_1,\ell_2\in H$ los dos primeros modos ortonormales de Legendre desplazado,

$$
\ell_1(t)=\sqrt3(2t-1), \qquad \ell_2(t)=\sqrt5(6t^2-6t+1),
$$

 y defínase el generador polinómico

$$
\boxed{ \psi(u,v):=\ell_1(u)\ell_2(v)-\ell_2(u)\ell_1(v).} \tag{7.1}
$$

 Es antisimétrico bajo intercambio de coordenadas, tiene marginales nulas y satisface

$$
\mathcal P\psi=\psi\ne0, \qquad h_\psi=2\psi\in\bigwedge\nolimits^2H, \qquad \|\psi\|_{L^2(D)}^2=2, \quad \|h_\psi\|_{L^2(D)}^2=8. \tag{7.2}
$$

 En particular, $\psi\notin\ker\mathcal P$: su invisibilidad a primer orden no es el gauge marginal de §2. Como $\psi$ está acotado, la familia exponencial normalizada

$$
\gamma_\psi:\varepsilon\longmapsto g_\varepsilon =\frac{e^{2\varepsilon\psi}}{Z(\varepsilon)}g_0, \qquad Z(\varepsilon)=\int_De^{2\varepsilon\psi}\,d\mu_0, \tag{7.3}
$$

 es una trayectoria S1 admisible para todo $\varepsilon$ real.

Sea $\iota:D\to D$ el intercambio de las dos coordenadas nulas, $\iota(u,v)=(v,u)$. Preserva el orden producto, la medida de referencia y la métrica plana, mientras que $\psi\circ\iota=-\psi$. Un cambio de variables da además $Z(-\varepsilon)=Z(\varepsilon)$, y por tanto

$$
\boxed{\iota^*g_\varepsilon=g_{-\varepsilon}} \qquad(\varepsilon\in\mathbb R). \tag{7.4}
$$

 Los dos signos quedan así identificados por una isometría discreta de la familia S1. Como el observable finito registra únicamente el orden causal abstracto,

$$
\boxed{ \mu_{N,\varepsilon}^{[P]}(C) =\mu_{N,-\varepsilon}^{[P]}(C)} \qquad(N\ge2,\ C\in\mathcal C_N). \tag{7.5}
$$

**Teorema 5 (paridad exacta de la órbita antisimétrica).** *Para la trayectoria $\gamma_\psi$ de (7.3), toda ley finita de posets no etiquetados es una función par real-analítica de $\varepsilon$. En consecuencia, todos sus jets impares en el punto de referencia se anulan, en particular*

$$
\left.\frac d{d\varepsilon} \mu_{N,\varepsilon}^{[P]}\right|_{\varepsilon=0}=0 \qquad\forall N\ge2. \tag{7.6}
$$

*Demostración.* Si $p_\pi(\varepsilon)$ es la probabilidad de la permutación de rangos $\pi\in S_N$, entonces

$$
p_\pi(\varepsilon) =\frac{\left\langle e^{2\varepsilon T_\pi}\right\rangle_0}        {N!\,Z(\varepsilon)^N}, \qquad T_\pi:=\sum_{i=1}^N \psi(U_{(i)},V_{(\pi(i))}), \tag{7.7}
$$

 donde el corchete es la esperanza sobre dos vectores independientes de estadísticos de orden uniformes. El acotamiento de $\psi$ permite derivar bajo la integral a todo orden, de modo que $p_\pi$ es real-analítica. El intercambio de coordenadas da $p_\pi(-\varepsilon)=p_{\pi^{-1}}(\varepsilon)$. Cada fibra $\Gamma_C$ es cerrada bajo inversión (§3); sumar (7.7) sobre la fibra demuestra (7.5) y, con ello, la afirmación. $\square$

Para medir la primera respuesta no nula de la ley finita completa, definimos el invariante de trayectoria

$$
r_N(\gamma_\psi) :=\inf\left\{k\ge1: \left.\frac{d^k}{d\varepsilon^k} \mu_{N,\varepsilon}^{[P]}\right|_{\varepsilon=0} \ne0\ \text{como vector en }\mathcal C_N\right\}, \tag{7.8}
$$

 con $r_N(\gamma_\psi)=\infty$ si todos los jets se anulan. La notación se refiere a la trayectoria completa, no meramente a su tangente nula de primer orden.

La misma fórmula de verosimilitud finita da

$$
p_\pi'(0)=\frac2{N!}\langle T_\pi\rangle_0, \qquad p_\pi''(0)=\frac4{N!} \left(\langle T_\pi^2\rangle_0-N\|\psi\|_{L^2(D)}^2\right). \tag{7.9}
$$

 En $N=2$, la integración polinómica exacta sobre los dos símplices de orden da

$$
\boxed{ \left.\frac{d^2}{d\varepsilon^2} \mu_{2,\varepsilon}^{[P]}(\mathrm{antichain})\right|_{0}=\frac85, \qquad \left.\frac{d^2}{d\varepsilon^2} \mu_{2,\varepsilon}^{[P]}(\mathrm{chain})\right|_{0}=-\frac85.} \tag{7.10}
$$

 Equivalentemente,

$$
\mu_{2,\varepsilon}^{[P]}(\mathrm{antichain}) =\frac12+\frac45\varepsilon^2+O(\varepsilon^4), \qquad \mu_{2,\varepsilon}^{[P]}(\mathrm{chain}) =\frac12-\frac45\varepsilon^2+O(\varepsilon^4). \tag{7.11}
$$

 Así, la magnitud de la deformación es localmente visible ya en la cardinalidad más pequeña que soporta dos órdenes causales distintos, mientras que su signo permanece identificado por (7.4).

Para $m\ge3$, defínase el núcleo de borrado independiente del parámetro

$$
K_{m,m-1}(C,D) :=\frac1m\#\{v\in C:[C\setminus\{v\}]=D\}, \tag{7.12}
$$

 y sea

$$
K_{N\to2}:=K_{3,2}\circ K_{4,3}\circ\cdots\circ K_{N,N-1}, \qquad K_{2\to2}:=I. \tag{7.13}
$$

 Borrar puntos uniformemente de una muestra iid deja una submuestra iid, de modo que para todo $\varepsilon$,

$$
\mu_{2,\varepsilon}^{[P]} =K_{N\to2}\mu_{N,\varepsilon}^{[P]}. \tag{7.14}
$$

 Como el núcleo no depende de $\varepsilon$, la derivación da

$$
\left(\mu_2^{[P]}\right)^{(k)}(0) =K_{N\to2}\left(\mu_N^{[P]}\right)^{(k)}(0) \qquad(k\ge1). \tag{7.15}
$$

**Corolario 6 (primer jet no nulo en toda cardinalidad).** *Para la trayectoria explícita (7.3),*

$$
\boxed{r_N(\gamma_\psi)=2\qquad\forall N\ge2.} \tag{7.16}
$$

*Demostración.* El Teorema 5 da $r_N(\gamma_\psi)\ge2$. Si $(\mu_N^{[P]})''(0)$ fuese cero, (7.15) con $k=2$ forzaría $(\mu_2^{[P]})''(0)=0$, contradiciendo (7.10). Por tanto el segundo jet es no nulo para todo $N\ge2$, lo que demuestra (7.16). $\square$

El Corolario 6 es un enunciado de existencia para una órbita admisible. No clasifica el segundo diferencial sobre $\bigwedge^2H$ ni afirma que toda dirección antisimétrica tenga orden dos. No se introduce ningún operador general $Q_N$, ni cono nulo cuadrático, ni estimador, ni tasa, ni reconstrucción no lineal. El cero de primer orden se explica por el pliegue isométrico exacto $\varepsilon\leftrightarrow-\varepsilon$; no debe describirse como pérdida física de información.

El Apéndice G da las derivadas de la verosimilitud finita, la integración exacta en $N=2$ y el argumento del núcleo de borrado.

## 8. Relación con trabajos previos

[Bombelli2000] establece ya el marco que aquí se estudia: la ley completa de un poset causal no etiquetado a cardinalidad fija, y una comparación estadística entre dos leyes de ese tipo obtenidas de geometrías distintas. [Janson2011] aporta el marco límite general de núcleos de posets y leyes finitas consistentes en el que se inscribe esta construcción. [Surya2026] cuenta una historia relacionada: aumentar la resolución puede levantar degeneraciones de una compresión causal, aunque a través de un observable distinto — abundancias esperadas de intervalos en lugar de la ley completa del poset no etiquetado usada aquí. Ninguno de los tres calcula el diferencial de la ley a $N$ finito en una geometría de referencia, ni su rango, ni su núcleo. Ese cálculo es lo que hacen §§2–7.

La correspondencia muchos-a-uno entre permutaciones y posets bidimensionales sobre la que hay que sumar este diferencial es ella misma clásica. [BayoumiElZaharKhamis1994] trabajan explícitamente con esta correspondencia, sus realizadores, la clausura de una fibra bajo $\sigma\mapsto\sigma^{-1}$ y la casi unicidad de los realizadores para posets primos. Recuperar esa correspondencia no es la contribución aquí; lo que hacemos es sumar un representante de score diferencial sobre la fibra entera,

$$
A_C=\sum_{\sigma\in\Gamma_C}P_\sigma,
$$

 y preguntar qué generan estos representantes de sumas de clase una vez que pasamos a clases de posets no etiquetados.

Antes de tomar ese cociente, la estructura diferencial relevante está próxima a dos construcciones existentes. [EvenZohar2020] descompone el espacio de densidades de patrones mediante la teoría de representaciones de $S_N$ y aísla el bloque de la representación estándar de dimensión $(N-1)^2$, realizado a través de matrices de permutación comprimidas a $\mathbf1^\perp$; su régimen asintótico concierne a las fluctuaciones del perfil de patrones de una permutación aleatoria cuando crece el tamaño anfitrión, una cuestión de escala distinta de la derivada local en $\varepsilon$ usada aquí.

La comparación con [Kurecka2022] puede hacerse exacta usando (1.1). Para $t=(t_\pi)_{\pi\in S_N}$, pongamos $M(t)=\sum_\pi t_\pi P_\pi$. El Lema 9 de Kurečka expresa todo coeficiente del polinomio gradiente como un múltiplo escalar no nulo de $b_i^TM(t)b_j$, donde $b_2,\ldots,b_N$ forman una base de $E_N$. Por tanto

$$
\ker(\text{aplicación de polinomios gradiente})=\ker T_N.
\tag{8.1}
$$

Como $M(t)$ tiene todas sus sumas por filas y por columnas iguales a $\sum_\pi t_\pi$, la condición $T_N(t)=0$ equivale a que $M(t)$ sea constante, que es el Lema 12 de Kurečka. Así pues, el diferencial a nivel de permutaciones, la base de Bernstein, la compresión a $E_N$, la técnica de matrices de recubrimiento y el núcleo ambiente en (8.1) pertenecen todos a ese trabajo previo.

El cociente de orden causal añade la primera flecha de (1.1). Conocer el núcleo ambiente reescribe, pero no resuelve, el problema de la imagen restringida:

$$
\operatorname{rank}(T_NJ_N)
=\dim(\operatorname{im}J_N)
-\dim\bigl(\operatorname{im}J_N\cap\ker T_N\bigr).
\tag{8.2}
$$

Kurečka no estudia el subespacio constante sobre las fibras $\operatorname{im}J_N$ ni determina la intersección de (8.2). La clausura bajo inversión de todo $\Gamma_C$ da únicamente $T_N(\operatorname{im}J_N)\subseteq\operatorname{Sym}(E_N)$. La construcción casi cadena de §4 aporta la inclusión recíproca y demuestra el enunciado residual exacto

$$
\boxed{T_N(\operatorname{im}J_N)=\operatorname{Sym}(E_N).}
\tag{8.3}
$$

Ésta es la afirmación de span de sumas de clase del Teorema 1. El enunciado es más estrecho que una afirmación de novedad para el diferencial ambiente o para el módulo simétrico abstracto. [ChanKralNoelPehovaSharifzadehVolec2020] y [GarbeKralMalekshahianPenaguiao2025] son resultados adyacentes de forzamiento de permutones y de región factible, sobre sumas de patrones que fuerzan cuasialeatoriedad y sobre la dimensión de la región factible de densidades de patrones respectivamente, y tampoco dan este enunciado de span indexado por fibras.

El módulo objetivo abstracto y su dimensión aparecen ya en la literatura de teoría de representaciones sobre rankings. [Diaconis1989] descompone funciones sobre rankings mediante la teoría de representaciones de $S_N$ y da, para efectos de pares no ordenados, $M^{(N-2,2)}\simeq S^{(N)}\oplus S^{(N-1,1)}\oplus S^{(N-2,2)}$, que es ya el módulo, y la dimensión $\binom N2$, detrás de una reformulación en el esquema de Johnson de $\operatorname{Sym}(E_N)$. La monografía ([Diaconis1988]) concreta esto con una instancia trabajada sobre pares no ordenados de variedades experimentales, el Diallel Cross Design, y desarrolla la familia de modelos asociada. Ninguno de los dos trabajos introduce fibras de posets bidimensionales no etiquetados, sus sumas de clase, ni un teorema de rango para esas sumas específicas. Así que $\operatorname{Sym}(E_N)$ y su dimensión no son aquí una representación nueva; la afirmación más estrecha que realmente hacemos es que las sumas sobre fibras de isomorfismo de posets bidimensionales no etiquetados generan exactamente ese módulo.

La información de Fisher tras pasar de observaciones continuas a rangos tampoco es una idea nueva. [HallinMelloukRifi2001] tienen ya polinomios de tipo Bernstein apareciendo en proyecciones de Hájek de estadísticos de rangos, aunque de forma asintótica y no en nuestro $N$ finito exacto. [Hoff2007] establece la verosimilitud de rangos como verosimilitud semiparamétrica libre de marginales, y [HoffNiuWellner2014] junto con [SeiMatsumoto2020] desarrollan la información y la divergencia inducidas de modelos de cópula gaussiana y de rangos, incluida la pérdida de identificabilidad en muestra finita. Ninguno de éstos alcanza el cociente adicional de una permutación de rangos completa a un poset no etiquetado, $\Pi_N\to[P_{\Pi_N}]$, ni clasifica su soporte S1 como hacen §§3–6.

La identidad de operadores que conecta estos dos niveles es estándar una vez conocido su núcleo. [Pollard2013] muestra, en el marco de diferenciabilidad en media cuadrática, que el score de un estadístico es la esperanza condicional del score original; en un espacio de Hilbert, todo operador lineal acotado factoriza tautológicamente a través de la proyección ortogonal sobre el complemento de su núcleo, con una restricción inyectiva a ese complemento. Así que la factorización $D\mathscr S_N=B_NP_N^{\rm vis}$, usada a partir de §5, no es una construcción de operadores independiente. El Teorema 1 es lo que fija el complemento de forma exacta, $(\ker D\mathscr S_N)^\perp=\operatorname{Sym}^2P_{N-1}$, y la inyectividad de $B_N$ se sigue inmediatamente de ello.

§7 se sitúa frente a varios mecanismos establecidos en lugar de introducirlos. [RotnitzkyCoxBottaiRobins2000] estudian modelos de verosimilitud con información singular, relacionando el orden de la primera derivada no nula con el comportamiento inferencial y señalando la ambigüedad de signo que surge cuando ese orden es par; una ley invisible a primer orden y visible sólo a un orden superior, y el papel que la paridad juega en ello, no es una contribución general de este artículo. Dentro de la literatura de permutones, los resultados de forzamiento van más allá del gradiente: [Chan2021] y [CrudeleDukesNoel2024] calculan hessianos de combinaciones de densidades de patrones alrededor del permutón uniforme una vez que el gradiente se anula, precedente del uso de un segundo diferencial de una ley de patrones de permutación para detectar perturbaciones ocultas a primer orden. La consistencia proyectiva bajo borrado uniforme es también estándar. El Teorema 5 y el Corolario 6 combinan estos ingredientes para una órbita antisimétrica S1 explícita; no introducen una clasificación general de orden superior.

En conjunto, los precedentes anteriores cubren el diferencial a nivel de permutaciones, el objetivo abstracto de teoría de representaciones y la mecánica general de scores inducidos por estadísticos e información singular de primer orden. Este artículo determina lo que queda: el efecto exacto del cociente adicional que va de permutaciones de rangos etiquetadas a leyes finitas de orden causal no etiquetadas, en toda cardinalidad fija $N$.

## 9. Discusión: compresión causal

La expresión *compresión causal* es un nombre compacto para la factorización S1 exacta

$$
D\mathscr S_N=B_NP_N^{\rm vis}, \qquad V_N=\operatorname{Sym}^2P_{N-1}. \tag{9.1}
$$

 Leída literalmente, al nivel efectivamente demostrado aquí: el primer diferencial de una tangente de interacción de dimensión infinita se comprime a la componente de dimensión finita $P_N^{\rm vis}f$, y esa componente se codifica después inyectivamente como score de la ley finita del poset no etiquetado. La proyección selecciona lo que es visible, $B_N$ realiza la codificación estadística, y $F_N=B_N^*B_N$ mide su intensidad direccional. Éstas son tres partes distintas de un mismo canal, no tres nombres para el mismo operador.

La palabra *causal* no es aquí decorativa. En el diamante de dimensión $1+1$, la relación de orden queda fijada por el patrón conjunto de los dos rankings nulos. Pasar de coordenadas continuas a rangos descarta información marginal; pasar de una permutación de rangos a un poset no etiquetado descarta la elección de realizador lineal. Lo que sobrevive a ambos pasos a primer orden es exactamente el sector polinómico simétrico de interacción de (9.1). En este sentido restringido y específico del modelo, el pasado y el futuro causales comprimen el presente: el orden finito no preserva una perturbación punto por punto, sino que registra una colección finita de modos simétricos de interacción a través de las relaciones entre los eventos muestreados.

**La resolución crece, pero no uniformemente.** El Teorema 1 y el Corolario 2 convierten esta interpretación en una filtración exacta,

$$
V_N\subsetneq V_{N+1}, \qquad \dim V_N=\binom N2, \qquad \overline{\bigcup_{N\ge2}V_N} =H\widehat\otimes_{\rm sym}H. \tag{9.2}
$$

 Cada cardinalidad adicional abre direcciones polinómicas genuinamente nuevas, de modo que ninguna tangente simétrica no nula fija permanece invisible a toda resolución suficientemente grande. Este enunciado es, sin embargo, puntual en la tangente. La dirección móvil $p_N\otimes p_N$ queda más allá de la resolución del experimento de tamaño $N$, y el Teorema 4 da correspondientemente

$$
\widehat F_N\xrightarrow{\rm SOT}\Pi_{\rm sym}, \qquad \|\widehat F_N-\Pi_{\rm sym}\|\ge1. \tag{9.3}
$$

 Así, aumentar $N$ resuelve toda interacción simétrica fija en el límite, pero no hay resolución uniforme sobre la esfera unidad de Hilbert–Schmidt ni convergencia en norma de operadores.

**Visibilidad no es sensibilidad.** Los espectros exactos en $N=2,3,4$ muestran que dos direcciones pueden pertenecer ambas a $V_N$ y ser sin embargo codificadas con intensidades de Fisher muy distintas. En $N=4$, los modos polinómicos visibles incluso se mezclan antes de que emerjan los autovectores de Fisher. Por tanto, la pregunta binaria que responde el Teorema 1 — si una dirección sobrevive al diferencial — es lógicamente previa a la pregunta cuantitativa tratada por el Teorema 4, pero no la responde. En particular, ni $F_N$ ni su extensión ambiente normalizada es una proyección de soporte a $N$ finito.

**Un núcleo de primer orden no es un teorema de borrado no lineal.** El sector antisimétrico completo pertenece a $\ker D\mathscr S_N$ en toda cardinalidad, pero §7 muestra por qué ese hecho no debe llamarse pérdida física de información. Para la trayectoria impar admisible explícita $\gamma_\psi$, el intercambio de coordenadas es una isometría que satisface $\iota^*g_\varepsilon=g_{-\varepsilon}$; la ley finita pliega por tanto los dos signos juntos. Su término lineal se anula por simetría, mientras que

$$
r_N(\gamma_\psi)=2\qquad\forall N\ge2. \tag{9.4}
$$

 La magnitud de esta deformación se detecta a segundo orden en toda resolución finita no trivial. Esta única órbita demuestra que la pertenencia al núcleo de primer orden no implica invariancia de la ley no lineal completa; no clasifica el comportamiento de orden superior en todo $\bigwedge^2H$.

Las secciones §§3–7 describen en conjunto la anatomía local de un canal. Los representantes de score dan sus funcionales lineales finitos; el teorema de span para todo $N$ fija su soporte exacto; el cociente delimita la clase de equivalencia que el diferencial identifica; el operador de Fisher resuelve después direcciones dentro de ese soporte, y la órbita antisimétrica de §7 muestra que un cero de primer orden forzado por simetría puede aun así portar un segundo jet no nulo. El resultado es un enunciado sobre visibilidad tangente y resolución estadística para el experimento de leyes finitas S1, no un teorema de reconstrucción.

En particular, *el pasado y el futuro causales comprimen el presente* no debe leerse como que los datos causales determinan universalmente una geometría presente. Los resultados no reconstruyen coordenadas continuas ni una métrica lorentziana a partir de un causet, no establecen inyectividad global, no realizan geométricamente toda tangente de Hilbert–Schmidt, ni se extienden más allá de S1 y de $1+1$ dimensiones. La expresión nombra la compresión exacta y específica del modelo de (9.1), y nada más amplio.

## 10. Limitaciones y problemas abiertos

**Alcance del modelo.** Todo teorema de este artículo concierne al modelo de interacción S1 explícito en un diamante causal de dimensión (1+1), desarrollado en el punto de referencia independiente. Los argumentos no establecen un análogo en dimensión (2+1) o (3+1), para un espacio-tiempo lorentziano general, ni para un modelo arbitrario de muestreo de conjuntos causales. Tales extensiones requerirían nuevo material geométrico y combinatorio y quedan fuera del presente artículo.

**Tangentes ambiente frente a realizabilidad geométrica.** El espacio de Hilbert $\mathcal X=H\widehat\otimes H$ es el dominio analítico de los operadores de score. Las identidades exactas para $V_N$, $\ker D\mathscr S_N$ y $F_N$ clasifican por tanto el canal finito sobre ese espacio tangente ambiente. No demuestran que toda dirección de Hilbert–Schmidt esté generada por una curva admisible de geometrías lorentzianas. La realizabilidad geométrica de una tangente ambiente arbitraria permanece abierta y no es necesaria para la clasificación del canal finito.

**Identificación diferencial frente a reconstrucción no lineal.** El Corolario 3 identifica exactamente el cociente visto por $D\mathscr S_N$; no implica inyectividad de la aplicación completa $\mathscr S_N$ a distancia finita, ni recuperación de coordenadas o de una métrica a partir de un causet, ni reconstrucción a partir de la familia de leyes finitas. La órbita antisimétrica de §7 concreta la distinción: su primer jet se anula y su segundo jet no. Ese cálculo trata una única órbita admisible explícita. Un operador general de segundo orden $Q_N$, el cono nulo cuadrático asociado y una clasificación del sector antisimétrico no se desarrollan aquí.

**Retención asintótica puntual.** La convergencia $\widehat F_N\to\Pi_{\rm sym}$ es convergencia fuerte de operadores. Da retención asintótica para cada tangente simétrica de Hilbert–Schmidt fija, pero ninguna tasa uniforme sobre la esfera unidad. En efecto, las direcciones móviles no resueltas de (6.26) dan $\|\widehat F_N-\Pi_{\rm sym}\|\ge1$ para todo $N$, y descartan por tanto la convergencia en norma de operadores. Los espectros exactos de Fisher calculados aquí se limitan a $N=2,3,4$; no se afirma ninguna fórmula espectral para todo $N$, ni cota uniforme de condicionamiento, ni estimador no lineal.

**Estado de prioridad.** La comparación estadística de leyes finitas de orden causal, y la expectativa general de que muestras mayores puedan afinar la resolución, tienen ambas precedentes claros; §8 los revisa, junto con precedentes parciales sustanciales para los ingredientes específicos que hay detrás de nuestros resultados. No hemos encontrado una contrapartida exacta del teorema S1 de span de sumas de clase para todo $N$, ni del enunciado sobre la órbita antisimétrica, en la literatura allí considerada, pero esa ausencia no constituye por sí misma una afirmación de prioridad, y nuestra búsqueda no fue exhaustiva. Se necesitaría una revisión especializada más amplia antes de cualquier afirmación afirmativa de novedad.

## 11. Conclusión

La ley finita de orden causal no etiquetado tiene, en el punto de referencia independiente del modelo S1 de dimensión $1+1$, una estructura diferencial local que ahora podemos enunciar de forma exacta. Los representantes de score de §3 reducen el problema a sumas de clase sobre las fibras de la aplicación de permutación a poset, y el argumento constructivo para todo $N$ de §4 da

$$
\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\} =V_N=\operatorname{Sym}^2P_{N-1}, \qquad \dim V_N=\binom N2 \quad(N\ge2). \tag{11.1}
$$

 Éstos son exactamente los modos de interacción de primer orden que sobreviven al cociente adicional que va de una permutación de rangos a un orden causal no etiquetado.

La imagen operatorial lo precisa. Para todo $N$,

$$
D\mathscr S_N=B_NP_N^{\rm vis}, \qquad \ker D\mathscr S_N =V_N^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H, \qquad \mathcal X/\ker D\mathscr S_N\simeq V_N. \tag{11.2}
$$

 Los espacios visibles están estrictamente anidados y su unión es densa en el espacio de Hilbert simétrico de interacción: aumentar la cardinalidad sigue abriendo nuevas direcciones de primer orden, mientras que (11.2) misma enuncia únicamente identificabilidad diferencial en el modelo de referencia.

Una cosa es la visibilidad y otra la sensibilidad estadística. El operador positivo $F_N=B_N^*B_N$ resuelve direcciones dentro de $V_N$, y los espectros exactos en $N=2,3,4$ muestran tanto anisotropía fuerte como, en $N=4$, mezcla modal. Normalizado por la información de Fisher de $N$ observaciones continuas de la cópula, el Teorema 4 da

$$
\widehat F_N\xrightarrow{\rm SOT}\Pi_{\rm sym}, \qquad \|\widehat F_N-\Pi_{\rm sym}\|\ge1 \quad\text{para todo }N. \tag{11.3}
$$

 Toda tangente simétrica de Hilbert–Schmidt fija se retiene asintóticamente, pero no uniformemente sobre la esfera unidad; mantener separadas las dos etapas, observaciones continuas $\to$ rangos y rangos $\to$ posets no etiquetados, es lo que nos permite localizar las pérdidas de Fisher correspondientes.

La órbita antisimétrica explícita de §7 completa el cuadro. El intercambio de coordenadas pliega $g_\varepsilon$ sobre la geometría isométrica $g_{-\varepsilon}$, de modo que las leyes finitas son pares y sus primeras derivadas se anulan. El Corolario 6 combina la segunda derivada exacta en $N=2$ con la consistencia proyectiva bajo borrado uniforme para dar un testigo admisible de segundo orden en toda resolución, no una clasificación del sector antisimétrico.

Tres capas componen el cuadro resultante:

$$
\boxed{\begin{aligned} &\text{visibilidad tangente}=V_N, \qquad \text{resolución estadística}=F_N,\\ &\text{detectabilidad de orden superior}=r_N(\gamma_\psi)=2 \text{ para el testigo explícito}. \end{aligned}} \tag{11.4}
$$

 Éste es un relato exacto y local de lo que el canal finito de orden causal retiene en S1, no una reconstrucción de la geometría a partir de un causet, ni una afirmación de identificabilidad global o no lineal, ni un resultado más allá del modelo S1 de dimensión $1+1$; §10 enuncia los límites completos. El marco estadístico mismo se hereda de trabajos previos — lo que aquí se aísla es la clasificación diferencial explícita y sus consecuencias dentro de ese alcance fijo.

## Apéndice A. QMD y representantes de score

Fíjese un generador admisible $\psi\in C([0,1]^2)$, póngase $f=\mathcal P\psi$, y sea $c_\varepsilon$ la densidad de cópula obtenida a partir de la densidad S1 normalizada mediante las dos transformadas integrales de probabilidad marginales de §2. El cálculo allí realizado da, uniformemente sobre el cuadrado unidad,

$$
c_\varepsilon(u,v) =1+2\varepsilon f(u,v)+o(\varepsilon), \qquad \int_0^1f(u,v)\,du= \int_0^1f(u,v)\,dv=0. \tag{A.1}
$$

 La positividad de la densidad S1 exponencial y la continuidad sobre el dominio compacto dan una cota inferior positiva común para $c_\varepsilon$ cuando $|\varepsilon|$ es pequeño. El desarrollo de Taylor de la raíz cuadrada, con el resto uniforme de (A.1), produce por tanto

$$
\int_{[0,1]^2} \left( \sqrt{c_\varepsilon}-1-\varepsilon f \right)^2du\,dv=o(\varepsilon^2). \tag{A.2}
$$

 Así, el experimento de cópula con una observación es QMD en cero con score $2f=h_\psi$.

Para un $N$ fijo, escribimos $L_{N,\varepsilon}=\prod_{k=1}^Nc_\varepsilon(U_k,V_k)$ para la densidad de la muestra iid de la cópula respecto de la medida de Lebesgue en $([0,1]^2)^N$. Tomando el producto finito en (A.2) se obtiene

$$
\int \left( \sqrt{L_{N,\varepsilon}}-1 -\varepsilon\sum_{k=1}^Nf(U_k,V_k) \right)^2=o(\varepsilon^2). \tag{A.3}
$$

 Por tanto, el score de la muestra completa es

$$
T_{N,\psi} =2\sum_{k=1}^Nf(U_k,V_k) =\sum_{k=1}^Nh_\psi(U_k,V_k). \tag{A.4}
$$

Sea $\mathcal A_\sigma$ el conjunto de muestras cuya permutación de rangos relativa es $\sigma\in S_N$. Este suceso está definido enteramente por desigualdades estrictas entre coordenadas y es independiente de $\varepsilon$; los empates tienen probabilidad cero. Como $c_\varepsilon$ y su derivada respecto del parámetro están uniformemente acotadas en un entorno de cero, la derivación bajo la integral sobre $\mathcal A_\sigma$ es válida. Con $p_\varepsilon(\sigma)=\int_{\mathcal A_\sigma}L_{N,\varepsilon}$ y $p_0(\sigma)=1/N!$,

$$
\begin{aligned} p_\sigma'(0;f) &=\mathbb E_0\!\left[ \mathbf1_{\{\Pi_N=\sigma\}}T_{N,\psi} \right],\\ S_N^\Pi(f)(\sigma) &:=\left.\partial_\varepsilon \log p_\varepsilon(\sigma)\right|_0 =\mathbb E_0[T_{N,\psi}\mid\Pi_N=\sigma]. \end{aligned} \tag{A.5}
$$

 Ésta es la identidad de score condicional usada en §2; se sigue de la verosimilitud y no supone que las observaciones ordenadas sigan siendo independientes tras condicionar.

Bajo la ley de referencia uniforme, los dos vectores de estadísticos de orden son independientes, y condicionalmente a $\Pi_N=\sigma$ el punto de $U$-rango $i$ se empareja con el punto de $V$-rango $\sigma(i)$. Si $d_i^{(N)}$ es la densidad del estadístico de orden de (3.1), (A.4)–(A.5) dan

$$
S_N^\Pi(f)(\sigma) =2\sum_{i=1}^N \left\langle f, d_i^{(N)}\otimes d_{\sigma(i)}^{(N)}\right\rangle, \tag{A.6}
$$

 y en consecuencia

$$
p_\sigma'(0;f) =\frac2{N!}\sum_{i=1}^N \left\langle f, d_i^{(N)}\otimes d_{\sigma(i)}^{(N)}\right\rangle. \tag{A.7}
$$

 Como ambas marginales de $f$ se anulan, escribir $d_i^{(N)}=1+b_i^{(N)}$ elimina los términos constante y de una sola coordenada:

$$
\left\langle f,d_i^{(N)}\otimes d_j^{(N)}\right\rangle =\left\langle f,b_i^{(N)}\otimes b_j^{(N)}\right\rangle. \tag{A.8}
$$

 Combinando (A.7)–(A.8) se demuestra la fórmula del representante

$$
R_\sigma^{(N)} =\frac2{N!}\sum_{i=1}^N b_i^{(N)}\otimes b_{\sigma(i)}^{(N)}, \qquad p_\sigma'(0;f)=\langle f,R_\sigma^{(N)}\rangle. \tag{A.9}
$$

El último paso es pasar de rangos etiquetados al poset no etiquetado observable. Para $C\in\mathcal C_N$, la fibra $\Gamma_C$ es finita y fija, de modo que la suma directa de (A.9) da

$$
\begin{aligned} \mu_{N,0}^{[P]}(C)&=\frac{|\Gamma_C|}{N!},\\ \left.\partial_\varepsilon \mu_{N,\varepsilon}^{[P]}(C)\right|_0 &=\left\langle f,R_C^{(N)}\right\rangle, \qquad R_C^{(N)}:=\sum_{\sigma\in\Gamma_C}R_\sigma^{(N)}. \end{aligned} \tag{A.10}
$$

 Toda masa de referencia en (A.10) es positiva. Como $\mathcal C_N$ es finito, la diferenciabilidad coordenada a coordenada de sus probabilidades equivale aquí al desarrollo QMD discreto

$$
\sum_{C\in\mathcal C_N} \left[ \sqrt{\mu_{N,\varepsilon}^{[P]}(C)} -\sqrt{\mu_{N,0}^{[P]}(C)} -\frac{\varepsilon}{2} (D\mathscr S_Nf)(C) \sqrt{\mu_{N,0}^{[P]}(C)} \right]^2 =o(\varepsilon^2), \tag{A.11}
$$

 con score

$$
(D\mathscr S_Nf)(C) =\frac{\langle f,R_C^{(N)}\rangle} {\mu_{N,0}^{[P]}(C)}. \tag{A.12}
$$

 Además, $\sum_{C\in\mathcal C_N}R_C^{(N)}=0$: tras sumar (A.9) sobre $\sigma$, cada $b_j^{(N)}$ aparece $(N-1)!$ veces en cada posición fija y $\sum_jb_j^{(N)}=0$. Así que (A.12) tiene media cero, como debe tenerla un score; la polarización da

$$
G_{[P]}^{(N)}(f,g) =\sum_{C\in\mathcal C_N} \frac{\langle f,R_C^{(N)}\rangle \langle g,R_C^{(N)}\rangle} {\mu_{N,0}^{[P]}(C)}. \tag{A.13}
$$

Las ecuaciones (A.9)–(A.13) se dedujeron para tangentes S1 continuas. Puesto que todo $R_C^{(N)}$ es una suma finita de tensores polinómicos, los miembros de la derecha definen funcionales lineales acotados sobre $\mathcal X=H\widehat\otimes H$. Ésta es la extensión al espacio de Hilbert usada en §§3–6; no es una afirmación de que todo elemento de $\mathcal X$ sea geométricamente realizable.

## Apéndice B. Reducción finita a $\operatorname{Sym}(E_N)$

Sea

$$
E_N=\mathbf1^\perp\subset\mathbb R^N, \qquad P_{N-1}=\operatorname{span}\{p_1,\ldots,p_{N-1}\} \subset H. \tag{B.1}
$$

 Las funciones $d_i^{(N)}/N$ forman la base de Bernstein de los polinomios de grado a lo sumo $N-1$. Puesto que $1=N^{-1}\sum_i d_i^{(N)}$, sus versiones centradas satisfacen

$$
b_i^{(N)} =d_i^{(N)}-\frac1N\sum_{j=1}^Nd_j^{(N)}, \qquad \sum_{i=1}^Nb_i^{(N)}=0. \tag{B.2}
$$

 Ésta es su única relación lineal. En efecto, todo vector de coeficientes $a\in\mathbb R^N$ se descompone como $a=\bar a\mathbf1+z$ con $z\in E_N$; la parte constante da la relación de (B.2), mientras que

$$
\sum_{i=1}^Nz_i b_i^{(N)} =\sum_{i=1}^Nz_i d_i^{(N)}, \tag{B.3}
$$

 y la independencia lineal de la base de Bernstein hace que el miembro de la derecha sea cero sólo cuando $z=0$. En consecuencia,

$$
\Lambda_N:E_N\longrightarrow P_{N-1}, \qquad \Lambda_Nz=\sum_{i=1}^Nz_i b_i^{(N)}, \tag{B.4}
$$

 es inyectiva y, como ambos espacios tienen dimensión $N-1$, es un isomorfismo.

Usamos el producto escalar euclídeo para identificar $\operatorname{Sym}(E_N)$, los endomorfismos autoadjuntos de $E_N$, con $\operatorname{Sym}^2E_N$. Para $M\in\operatorname{Sym}(E_N)$, sea $\widetilde M$ su extensión autoadjunta a $\mathbb R^N$ que se anula en $\operatorname{span}\{\mathbf1\}$. El transporte tensorial inducido por (B.4) es

$$
\begin{aligned} \mathfrak T_N:\operatorname{Sym}(E_N) &\longrightarrow\operatorname{Sym}^2P_{N-1},\\ M&\longmapsto \sum_{i,j=1}^N \widetilde M_{ij} b_i^{(N)}\otimes b_j^{(N)}, \end{aligned} \tag{B.5}
$$

 Equivalentemente, $\mathfrak T_N$ es $\Lambda_N\otimes\Lambda_N$ restringido al cuadrado tensorial simétrico. Es por tanto un isomorfismo lineal. No tiene por qué ser una isometría; esta reducción preserva únicamente spans y rangos, no autovalores de Fisher.

Con el convenio de (3.12),

$$
P_\sigma=\sum_{i=1}^Ne_i e_{\sigma(i)}^\top, \qquad A_C=\sum_{\sigma\in\Gamma_C}P_\sigma. \tag{B.6}
$$

 Toda matriz de permutación tiene sumas por filas y por columnas iguales a uno. Por tanto

$$
A_C\mathbf1=|\Gamma_C|\mathbf1, \qquad \mathbf1^\top A_C=|\Gamma_C|\mathbf1^\top, \tag{B.7}
$$

 de modo que $E_N$ es invariante bajo $A_C$. Además, $P_\sigma^\top=P_{\sigma^{-1}}$, y la fibra $\Gamma_C$ es cerrada bajo inversión (§3). Así pues,

$$
A_C^\top=A_C, \qquad A_C|_{E_N}\in\operatorname{Sym}(E_N). \tag{B.8}
$$

Como $\sum_i b_i^{(N)}=0$, proyectar sobre $E_N$ en cualquiera de los dos índices matriciales no cambia el tensor transportado. Las ecuaciones (3.13) y (B.5) dan por tanto la identidad exacta

$$
R_C^{(N)} =\frac2{N!}\, \mathfrak T_N\!\left(A_C|_{E_N}\right). \tag{B.9}
$$

 El escalar $2/N!$ es no nulo para todo $N$. Como $\mathfrak T_N$ es un isomorfismo, (B.9) demuestra

$$
\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\} =\operatorname{Sym}^2P_{N-1} \quad\Longleftrightarrow\quad \operatorname{span}\{A_C|_{E_N}:C\in\mathcal C_N\} =\operatorname{Sym}(E_N). \tag{B.10}
$$

 En particular, tras elegir cualquier base de $E_N$, el miembro de la derecha equivale a la condición de rango finito

$$
\operatorname{rank} \left( \operatorname{vec}_{\rm sym}(A_C|_{E_N}) \right)_{C\in\mathcal C_N} =\frac{N(N-1)}2. \tag{B.11}
$$

 El Apéndice C demuestra este rango estructuralmente a partir de la familia casi cadena; ninguna enumeración de cardinalidad finita forma parte de la reducción anterior.

## Apéndice C. Clases casi cadena y triangularización laplaciana

Fíjese $N\ge2$. Para cada par de enteros $0\le a<b\le N-1$, sea $C_{a,b}$ el poset formado por una cadena

$$
c_1<\cdots<c_{N-1} \tag{C.1}
$$

 y un elemento adicional $z$, con

$$
c_i<z\quad(i\le a), \qquad z<c_i\quad(i>b), \qquad z\parallel c_i\quad(a<i\le b). \tag{C.2}
$$

 Toda extensión lineal de $C_{a,b}$ se obtiene insertando $z$ tras exactamente $k\in\{a,\ldots,b\}$ elementos de la cadena; denotemos esta extensión por $L_k$. Para dos extensiones así, su intersección sitúa $c_1,\ldots,c_{\min(s,t)}$ por debajo de $z$ y $c_{\max(s,t)+1},\ldots,c_{N-1}$ por encima. Por tanto

$$
L_s\cap L_t=C_{a,b} \quad\Longleftrightarrow\quad \{s,t\}=\{a,b\}. \tag{C.3}
$$

 Todo $\sigma$ con $P_\sigma\cong C_{a,b}$ retrotrae el orden natural y el $\sigma$-orden a un par ordenado de realizadores de $C_{a,b}$. Recíprocamente, enumerar los elementos en el primer orden de cualquier par ordenado de realizadores y registrar sus rangos en el segundo produce uno de tales $\sigma$. Aplicar un automorfismo o un reetiquetado simultáneo a ambos órdenes no cambia esta permutación de rangos relativa, de modo que no surgen permutaciones adicionales de la elección de un isomorfismo.

Así pues, los únicos pares ordenados de realizadores son $(L_a,L_b)$ y $(L_b,L_a)$. Tras normalizar la primera extensión al orden natural, la permutación relativa es un ciclo $\tau_{a,b}$ sobre el intervalo consecutivo

$$
I_{a,b}=\{a+1,a+2,\ldots,b+1\}, \tag{C.4}
$$

 e invertir el par ordenado da su inverso. Por tanto

$$
\Gamma_{C_{a,b}} =\{\tau_{a,b},\tau_{a,b}^{-1}\}, \tag{C.5}
$$

 como conjunto sin multiplicidad. Cuando $b=a+1$, el ciclo es una transposición y las dos permutaciones exhibidas coinciden.

Estas $\binom N2$ clases son distintas dos a dos. En efecto, el multiconjunto de cardinalidades del pasado estricto es

$$
\bigl\{|\operatorname{Past}(y)|:y\in C_{a,b}\bigr\} =\{0,1,\ldots,b-1,b+1,\ldots,N-1\}\uplus\{a\}. \tag{C.6}
$$

 Omite $b$ y contiene $a$ dos veces, de modo que determina $(a,b)$. Esto significa que la construcción proporciona exactamente una clase distinta para cada uno de los $\binom N2$ pares $a<b$.

Para $1\le i<j\le N$, defínase el laplaciano de arista

$$
L_{ij}:=(e_i-e_j)(e_i-e_j)^\top. \tag{C.7}
$$

 Cada $L_{ij}$ aniquila $\mathbf1$ y preserva $E_N$. Si una combinación lineal de sus restricciones se anula en $E_N$, se anula también en $\operatorname{span}\{\mathbf1\}$, y por tanto en todo $\mathbb R^N$; su entrada $(i,j)$ es $-w_{ij}$, de modo que todo coeficiente es cero. Hay $\binom N2=\dim\operatorname{Sym}(E_N)$ matrices de este tipo, y por consiguiente

$$
\{L_{ij}|_{E_N}:1\le i<j\le N\} \quad\text{es una base de }\operatorname{Sym}(E_N). \tag{C.8}
$$

 Sumar todas las aristas da el laplaciano del grafo completo

$$
\sum_{1\le i<j\le N}L_{ij} =NI-\mathbf1\mathbf1^\top, \qquad \sum_{i<j}L_{ij}|_{E_N}=NI_{E_N}. \tag{C.9}
$$

Simetrícese el ciclo de intervalo poniendo

$$
S_{a,b}:=P_{\tau_{a,b}}+P_{\tau_{a,b}}^\top. \tag{C.10}
$$

 La ecuación (C.5) implica

$$
S_{a,b} =\begin{cases} 2A_{C_{a,b}},&b=a+1,\\ A_{C_{a,b}},&b>a+1. \end{cases} \tag{C.11}
$$

 El escalar que relaciona $S_{a,b}$ con la suma de clase es no nulo en ambos casos. En $E_N$, póngase

$$
Q_{a,b}:=2I_{E_N}-S_{a,b}|_{E_N}. \tag{C.12}
$$

 La matriz $Q_{a,b}$ es el laplaciano de grafo del ciclo consecutivo sobre $I_{a,b}$, con la arista única contada dos veces cuando el intervalo tiene longitud dos. En las fórmulas siguientes, cada $L_{ij}$ se entiende como su restricción a $E_N$. Así

$$
Q_{a,a+1}=2L_{a+1,a+2}, \tag{C.13}
$$

 mientras que, cuando $b>a+1$,

$$
Q_{a,b} =L_{a+1,b+1}+\sum_{k=a+1}^{b}L_{k,k+1}. \tag{C.14}
$$

 Estas identidades son triangulares en la longitud del intervalo. Se invierten como

$$
L_{i,i+1}=\frac12Q_{i-1,i}, \qquad L_{ij}=Q_{i-1,j-1} -\frac12\sum_{k=i}^{j-1}Q_{k-1,k} \quad(j>i+1). \tag{C.15}
$$

 Por (C.8),

$$
\operatorname{span}\{Q_{a,b}:0\le a<b\le N-1\} =\operatorname{Sym}(E_N). \tag{C.16}
$$

El término identidad común de (C.12) todavía debe eliminarse. De (C.9) y (C.15), existen coeficientes $c_{a,b}$ tales que

$$
I_{E_N}=\sum_{a<b}c_{a,b}Q_{a,b}. \tag{C.17}
$$

 Sus valores individuales son innecesarios, pero su suma no lo es. Una arista $L_{ij}$ a distancia $d=j-i$ contribuye con coeficiente total $1-d/2$ en su expresión a través de los $Q$: esto es $1/2$ para $d=1$, y para $d>1$ es un término de intervalo largo menos $d$ términos adyacentes de coeficiente $1/2$. Como hay $N-d$ aristas a distancia $d$, (C.9) da

$$
\begin{aligned} s_N:=\sum_{a<b}c_{a,b} &=\frac1N\sum_{d=1}^{N-1}(N-d)\left(1-\frac d2\right)\\ &=\frac{(N-1)(5-N)}{12}. \end{aligned} \tag{C.18}
$$

 Sustituir $Q_{a,b}=2I_{E_N}-S_{a,b}|_{E_N}$ en (C.17) produce

$$
(1-2s_N)I_{E_N} =-\sum_{a<b}c_{a,b}S_{a,b}|_{E_N}. \tag{C.19}
$$

 El coeficiente de la identidad nunca se anula:

$$
1-2s_N =\frac{N^2-6N+11}{6} =\frac{(N-3)^2+2}{6}>0. \tag{C.20}
$$

 Así pues, $I_{E_N}$ está en el span de los $S_{a,b}|_{E_N}$. La ecuación (C.12) sitúa entonces todo $Q_{a,b}$ en ese mismo span, y (C.16) da

$$
\operatorname{span}\{S_{a,b}|_{E_N}:a<b\} =\operatorname{Sym}(E_N). \tag{C.21}
$$

 El paso restante, (C.11), muestra que las propias sumas de clase seleccionadas generan $\operatorname{Sym}(E_N)$. El Apéndice B transporta después (C.21) a $V_N=\operatorname{Sym}^2P_{N-1}$, completando la demostración constructiva del Teorema 1 para todo $N\ge2$.

## Apéndice D. Núcleo, anidamiento estricto y densidad

Sea

$$
\mathcal X=H\widehat\otimes H, \qquad \mathcal X_{\rm sym}=H\widehat\otimes_{\rm sym}H, \qquad \mathcal X_{\rm alt}=\bigwedge\nolimits^2H. \tag{D.1}
$$

 La involución de intercambio de coordenadas $(\mathfrak s f)(u,v)=f(v,u)$ es unitaria y autoadjunta. Sus dos autoespacios son ortogonales, con proyecciones

$$
\Pi_{\rm sym}=\frac{I+\mathfrak s}{2}, \qquad \Pi_{\rm alt}=\frac{I-\mathfrak s}{2}, \qquad \mathcal X=\mathcal X_{\rm sym}\oplus\mathcal X_{\rm alt}. \tag{D.2}
$$

Por (B.8)–(B.9), todo representante de clase $R_C^{(N)}$ pertenece a $\mathcal X_{\rm sym}$. El Apéndice A da

$$
(D\mathscr S_Nf)(C) =\frac{\langle f,R_C^{(N)}\rangle}{\mu_{N,0}^{[P]}(C)}, \qquad \mu_{N,0}^{[P]}(C)>0. \tag{D.3}
$$

 Por tanto

$$
\ker D\mathscr S_N =\ker G_{[P]}^{(N)} =\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}^{\perp_{\mathcal X}}. \tag{D.4}
$$

 La primera igualdad usa $G_{[P]}^{(N)}(f,f)=\|D\mathscr S_Nf\|_{\mathcal K_N}^2$. El Teorema 1 identifica el span de (D.4) con $V_N=\operatorname{Sym}^2P_{N-1}\subset\mathcal X_{\rm sym}$. Descomponer el complemento ortogonal ambiente según (D.2) demuestra

$$
\boxed{ \ker D\mathscr S_N =V_N^{\perp_{\rm sym}}\oplus\mathcal X_{\rm alt} =\left(\operatorname{Sym}^2P_{N-1}\right)^{\perp_{\rm sym}} \oplus\bigwedge\nolimits^2H.} \tag{D.5}
$$

 Aquí $\perp_{\rm sym}$ denota el complemento ortogonal dentro de $\mathcal X_{\rm sym}$, no dentro del producto tensorial completo.

Sea $P_N^{\rm vis}=\Pi_{V_N}\Pi_{\rm sym}$. Como $V_N\subset\mathcal X_{\rm sym}$, ésta es la proyección ortogonal ambiente sobre $V_N$, y (D.5) da

$$
\ker P_N^{\rm vis}=\ker D\mathscr S_N. \tag{D.6}
$$

 Si $B_N=D\mathscr S_N|_{V_N}$, entonces $B_N$ es inyectiva: un vector de su núcleo pertenece simultáneamente a $V_N$ y a $V_N^\perp$. Para todo $f\in\mathcal X$, (D.6) da además

$$
D\mathscr S_Nf =D\mathscr S_NP_N^{\rm vis}f =B_NP_N^{\rm vis}f. \tag{D.7}
$$

 Esto demuestra la factorización exacta sin identificar $B_N$ con la proyección de soporte.

Para completar, sea $q_N:\mathcal X\to\mathcal X/\ker D\mathscr S_N$ la aplicación cociente. La aplicación

$$
U_N:\mathcal X/\ker D\mathscr S_N\longrightarrow V_N, \qquad U_N([f])=P_N^{\rm vis}f, \tag{D.8}
$$

 está bien definida por (D.6), es sobreyectiva y es inyectiva por la misma razón. La descomposición ortogonal $\mathcal X=V_N\oplus\ker D\mathscr S_N$ da

$$
\|[f]\|_{\mathcal X/\ker D\mathscr S_N} =\inf_{k\in\ker D\mathscr S_N}\|f+k\|_{\mathcal X} =\|P_N^{\rm vis}f\|_{\mathcal X}. \tag{D.9}
$$

 Así, $U_N$ es un isomorfismo isométrico canónico y $D\mathscr S_N=B_NU_Nq_N$. Ésta es una identificación del cociente diferencial únicamente.

Demostramos a continuación el anidamiento estricto. La ortogonalidad de la base de Legendre desplazado da

$$
P_N=P_{N-1}\oplus\operatorname{span}\{p_N\}. \tag{D.10}
$$

 Escribimos $x\odot y=x\otimes y+y\otimes x$. Tomando cuadrados tensoriales simétricos y usando el Teorema 1,

$$
\begin{aligned} V_{N+1}=\operatorname{Sym}^2P_N &=\operatorname{Sym}^2P_{N-1} \oplus\{x\odot p_N:x\in P_{N-1}\} \oplus\operatorname{span}\{p_N\otimes p_N\}\\ &=V_N\oplus\{x\odot p_N:x\in P_{N-1}\} \oplus\operatorname{span}\{p_N\otimes p_N\}, \end{aligned} \tag{D.11}
$$

 y los sumandos son ortogonales. En particular,

$$
p_1\odot p_N\in V_{N+1}\setminus V_N, \qquad V_N\subsetneq V_{N+1} \quad(N\ge2). \tag{D.12}
$$

 El mismo testigo da el enunciado de Fisher del Corolario 2. Para la tangente no simetrizada $p_1\otimes p_N$, su componente simétrica es $(p_1\odot p_N)/2$. La ecuación (D.5) la aniquila a tamaño $N$, mientras que la inyectividad de $B_{N+1}$ sobre $V_{N+1}$ da

$$
I_N^{[P]}(p_1\otimes p_N)=0, \qquad I_{N+1}^{[P]}(p_1\otimes p_N)>0. \tag{D.13}
$$

Por último, los polinomios centrados son densos en $H=L_0^2([0,1])$. En efecto, si polinomios ordinarios $q_m$ convergen en $L^2$ a $h\in H$, entonces

$$
\left\|q_m-\int_0^1q_m-h\right\|_{L^2} \le2\|q_m-h\|_{L^2}\longrightarrow0. \tag{D.14}
$$

 Las sumas finitas de tensores elementales de un subespacio denso son densas en el producto tensorial de Hilbert. Aplicando la proyección continua $\Pi_{\rm sym}$, todo tensor simétrico de Hilbert–Schmidt puede por tanto aproximarse mediante sumas finitas de tensores polinómicos simetrizados. Cada suma finita de ese tipo pertenece a $\operatorname{Sym}^2P_m=V_{m+1}$ para algún $m$. Así pues,

$$
\boxed{ \overline{\bigcup_{N\ge2}V_N}^{\,\|\cdot\|_{\mathcal X}} =\mathcal X_{\rm sym}.} \tag{D.15}
$$

 Combinar (D.5), el anidamiento estricto y (D.15) da también

$$
\bigcap_{N\ge2}\ker D\mathscr S_N =\bigwedge\nolimits^2H. \tag{D.16}
$$

 La ecuación (D.16) concierne a la invisibilidad simultánea de primer orden a través de todas las resoluciones finitas. No dice que las trayectorias geométricas antisimétricas sean invisibles para la ley no lineal: la trayectoria explícita de §7 tiene un segundo jet no nulo. Del mismo modo, la densidad en el espacio de Hilbert de (D.15) no afirma que todo elemento de $\mathcal X_{\rm sym}$ esté generado por una curva geométrica admisible.

## Apéndice E. Cotas de Hilbert–Schmidt y retención de Fisher

Para $a\in H$, defínase la transformada de estadísticos de orden

$$
\mathcal O_Na :=\bigl(\langle a,d_1^{(N)}\rangle,\ldots, \langle a,d_N^{(N)}\rangle\bigr)\in\mathbb R^N, \tag{E.1}
$$

 y, para $f\in\mathcal X$, defínase

$$
H_{ij}^{(N)}(f) :=\langle f,d_i^{(N)}\otimes d_j^{(N)}\rangle. \tag{E.2}
$$

 Así, $H^{(N)}(f)=(\mathcal O_N\otimes\mathcal O_N)f$. Como $\sum_i d_i^{(N)}=N$ y ambas marginales de $f$ se anulan, esta matriz tiene sumas por filas y por columnas nulas. El Apéndice A da el score de la permutación de rangos como

$$
S_N^\Pi(f)(\sigma)=2\sum_{i=1}^NH_{i,\sigma(i)}^{(N)}(f). \tag{E.3}
$$

Si $H$ y $K$ tienen sumas por filas y por columnas nulas y $\Pi_N$ es uniforme sobre $S_N$, separar el promedio según $i=j$ y $i\ne j$ da

$$
\mathbb E_0\!\left[ \sum_iH_{i,\Pi_N(i)}\sum_jK_{j,\Pi_N(j)} \right] =\frac1{N-1}\langle H,K\rangle_F. \tag{E.4}
$$

 En efecto, la contribución diagonal es $N^{-1}\langle H,K\rangle_F$, mientras que las identidades de suma nula reducen el numerador fuera de la diagonal a $\langle H,K\rangle_F$, con factor de probabilidad $1/[N(N-1)]$. En consecuencia,

$$
G_N^\Pi(f,g) =\frac4{N-1} \left\langle H^{(N)}(f),H^{(N)}(g)\right\rangle_F, \qquad I_N^\Pi(f)=\frac4{N-1}\|H^{(N)}(f)\|_F^2. \tag{E.5}
$$

La desigualdad de Jensen y $\sum_i d_i^{(N)}=N$ implican $\|\mathcal O_Na\|_{\ell^2}\le\sqrt N\|a\|_{L^2}$. Por tanto

$$
\|H^{(N)}(f)\|_F\le N\|f\|_{\mathcal X}, \qquad 0\le\frac{I_N^\Pi(f)}N \le\frac{4N}{N-1}\|f\|_{\mathcal X}^2 \le8\|f\|_{\mathcal X}^2. \tag{E.6}
$$

 Ésta es la cota uniforme de Hilbert–Schmidt usada más abajo.

El límite de la forma de Fisher de rangos es más preciso. Sea $(\ell_m)_{m\ge1}$ una base ortonormal de Legendre desplazado de $H$ y póngase $\widetilde{\mathcal O}_N=N^{-1/2}\mathcal O_N$. El operador positivo $\widetilde{\mathcal O}_N^*\widetilde{\mathcal O}_N$ es el operador de Bernstein–Durrmeyer de grado $N-1$. Es triangular sobre los espacios polinómicos anidados: la fórmula de la integral beta aplicada a un monomio de grado $m\le N-1$ da el coeficiente diagonal

$$
\frac{N!(N-1)!}{(N+m)!(N-1-m)!} =\prod_{r=1}^m\frac{N-r}{N+r}.
$$

 La autoadjunción hace entonces invariantes las diferencias ortogonales entre espacios polinómicos sucesivos, de modo que las $\ell_m$ son autofunciones, con

$$
\lambda_{N-1,m} =\prod_{r=1}^m\frac{N-r}{N+r} \quad(1\le m\le N-1), \qquad \lambda_{N-1,m}=0\quad(m\ge N). \tag{E.7}
$$

 Para cada $m$ fijo, estos autovalores están en $[0,1]$ y convergen a uno. Si $f=\sum_{j,k\ge1}c_{jk}\ell_j\otimes\ell_k$, entonces

$$
\frac{I_N^\Pi(f)}N =\frac{4N}{N-1} \sum_{j,k\ge1} \lambda_{N-1,j}\lambda_{N-1,k}|c_{jk}|^2. \tag{E.8}
$$

 La convergencia dominada en el array de coeficientes de cuadrado sumable produce

$$
\boxed{ \frac{I_N^\Pi(f)}N\longrightarrow4\|f\|_{\mathcal X}^2 \qquad(f\in\mathcal X).} \tag{E.9}
$$

Aislamos ahora el segundo canal. La esperanza condicional de los scores bajo $\Pi_N\mapsto[P_{\Pi_N}]$ y la ley de la varianza total dan

$$
\Delta_N(f,g):=G_N^\Pi(f,g)-G_{[P]}^{(N)}(f,g) =\mathbb E_0\!\left[ \operatorname{Cov}_0(S_N^\Pi(f),S_N^\Pi(g)\mid[P_{\Pi_N}]) \right]. \tag{E.10}
$$

 Así, $\Delta_N$ es semidefinida positiva y $0\le\Delta_N(f,f)\le I_N^\Pi(f)$.

Supongamos primero que $f\in\mathcal X_{\rm sym}$ tiene rango finito. Su descomposición espectral tiene la forma $f=\sum_{r=1}^R\alpha_r a_r\otimes a_r$, con $a_r\in H$ ortonormales centradas. Póngase $x_i=(\mathcal O_Na)_i$ para un perfil fijo. La convergencia espectral anterior y una aproximación por funciones acotadas dan

$$
\frac1N\sum_{i=1}^Nx_i^2\longrightarrow\|a\|_2^2, \qquad \max_i|x_i|=o(\sqrt N), \qquad \sum_i x_i=0. \tag{E.11}
$$

 Para la segunda afirmación, elíjase $b$ acotada próxima a $a$ en $L^2$. Como $0\le d_i^{(N)}\le N$ y $\int d_i^{(N)}=1$, uniformemente en $i$,

$$
\frac{|(\mathcal O_Na)_i|}{\sqrt N} \le\frac{\|b\|_\infty}{\sqrt N}+\|a-b\|_2. \tag{E.12}
$$

 Tomando $N\to\infty$ y después $b\to a$ se demuestra (E.11).

Sean $X_N(a)=\sum_i x_i x_{\Pi_N(i)}$, $S_2=\sum_i x_i^2$, $S_4=\sum_i x_i^4$ y $(N)_r=N(N-1)\cdots(N-r+1)$. Agrupar directamente los cuatro índices por patrón de coincidencia da, para $N\ge4$,

$$
\begin{aligned} \mathbb E_0[X_N(a)^4] ={}&\frac{S_4^2}{N} +\frac{4S_4^2}{(N)_2} +\frac{3(S_2^2-S_4)^2}{(N)_2}\\ &+\frac{6(2S_4-S_2^2)^2}{(N)_3} +\frac{9(S_2^2-2S_4)^2}{(N)_4}. \end{aligned} \tag{E.13}
$$

 La ecuación (E.11) da $S_2=O(N)$ y $S_4\le(\max_i|x_i|)^2S_2=o(N^2)$. La sustitución en (E.13) produce $\mathbb E_0[X_N(a)^4]=o(N^3)$. Puesto que $S_N^\Pi(f)=2\sum_{r=1}^R\alpha_rX_N(a_r)$, la desigualdad de Minkowski en $L^4$ da

$$
\mathbb E_0[S_N^\Pi(f)^4]=o(N^3) \qquad(f\text{ simétrica y de rango finito fijo}). \tag{E.14}
$$

Identificamos ahora exactamente el evento de alta probabilidad usado en el paso del cociente. Sea $\mathcal G_N$ el evento de que el árbol de intervalos fuertes de $\Pi_N$ tenga raíz prima y de que todo hijo de la raíz sea o bien una hoja o bien un twin, es decir, un nodo lineal con dos hijos hoja. Éste no es el evento de que el grafo de incomparabilidad completo sea primo: los twins están permitidos. El árbol de intervalos fuertes es equivalentemente el árbol de descomposición modular del grafo de permutación ([BouvelChauveMishnaRossin2009], Remark 1); por tanto $\mathcal G_N$ es medible respecto de $[P_{\Pi_N}]$, puesto que el poset no etiquetado determina su grafo de incomparabilidad salvo isomorfismo. El Teorema 2 de [BouvelChauveMishnaRossin2009], cuya demostración aplica su Lema 1 con $c=1$, afirma exactamente que el complemento de este evento de raíz prima con hojas o twins tiene probabilidad $O(N^{-1})$. Existen por tanto constantes finitas $C_{\rm fib}$ y $N_{\rm fib}$ tales que $\mathbb P_0(\mathcal G_N^c)\le C_{\rm fib}/N$ para $N\ge N_{\rm fib}$; la fuente no especifica estas constantes y nosotros no las afinamos.

Para completar, demostramos que este mismo evento da la fibra requerida, incluidos los twins permitidos. Fíjese $\pi\in\mathcal G_N$, sean $B_1,\ldots,B_m$ los bloques fuertes maximales por debajo de la raíz, y escríbase la inflación correspondiente como $\pi=\alpha[\tau_1,\ldots,\tau_m]$. La condición sobre la raíz dice que el grafo de incomparabilidad del cociente $\alpha$ es primo, mientras que todo $B_s$ tiene tamaño uno o dos y por tanto $\tau_s\in\{1,12,21\}$. Si $[P_\sigma]=[P_\pi]$, un isomorfismo de posets lleva los módulos fuertes maximales canónicos de uno a otro, preservando sus tamaños y sus tipos de poset inducidos. Contraerlos da por tanto posets cociente isomorfos. El teorema de unicidad de Gallai para las dos orientaciones transitivas de un grafo de comparabilidad primo ([Gallai1967]), seguido de la normalización de ambos órdenes lineales por rango, fuerza a que la permutación cociente de $\sigma$ sea o bien $\alpha$ o bien $\alpha^{-1}$. En el primer caso cada patrón interno queda fijado: en un bloque de dos elementos, $12$ induce una cadena y $21$ una anticadena, de modo que un isomorfismo no puede intercambiarlos. En el segundo caso se aplica la fórmula exacta del inverso de una inflación; los únicos patrones internos $1,12,21$ son todos involuciones, y el resultado es $\pi^{-1}$. En consecuencia

$$
\mathbb P_0(\mathcal G_N^c)\le\frac{C_{\rm fib}}N
\quad(N\ge N_{\rm fib}),
\qquad
\Gamma_{[P_{\Pi_N}]}=\{\Pi_N,\Pi_N^{-1}\}
\quad\text{en }\mathcal G_N,
\tag{E.15}
$$

entendiéndose el conjunto sin multiplicidad para las involuciones.

Para $f$ simétrica, (E.2) da $H^{(N)}(f)^\top=H^{(N)}(f)$ y, por tanto, $S_N^\Pi(f)(\sigma^{-1})=S_N^\Pi(f)(\sigma)$. La varianza condicional de (E.10) se anula en consecuencia sobre $\mathcal G_N$. Cauchy–Schwarz y (E.14)–(E.15) implican

$$
\begin{aligned} 0\le\Delta_N(f,f) &\le\mathbb E_0\!\left[S_N^\Pi(f)^2 \mathbf1_{\mathcal G_N^c}\right]\\ &\le\mathbb P_0(\mathcal G_N^c)^{1/2} \mathbb E_0[S_N^\Pi(f)^4]^{1/2} =o(N). \end{aligned} \tag{E.16}
$$

Para eliminar la restricción de rango finito, póngase $\mathcal L_N(f,g)=\Delta_N(f,g)/N$ sobre $\mathcal X_{\rm sym}$. Las ecuaciones (E.6) y (E.10) dan la cota uniforme

$$
0\le\mathcal L_N(f,f)\le8\|f\|_{\mathcal X}^2. \tag{E.17}
$$

 Elíjanse $f_R\to f$ simétricas de rango finito en norma de Hilbert–Schmidt antes de tomar $N\to\infty$. La desigualdad triangular para la seminorma inducida por la forma positiva $\mathcal L_N$ da

$$
\sqrt{\mathcal L_N(f,f)} \le\sqrt{\mathcal L_N(f_R,f_R)} +\sqrt8\,\|f-f_R\|_{\mathcal X}. \tag{E.18}
$$

 Con $R$ fijo, (E.16) hace que el primer término se anule cuando $N\to\infty$; sólo después se toma $R\to\infty$. Por tanto

$$
\boxed{ \frac{\Delta_N(f,f)}N\longrightarrow0, \qquad \frac{I_N^{[P]}(f)}N\longrightarrow4\|f\|_{\mathcal X}^2 \quad(f\in\mathcal X_{\rm sym}).} \tag{E.19}
$$

Para $0\ne f\in\mathcal X_{\rm sym}$, (E.9) proporciona un umbral finito $N_0(f)$ tal que $I_N^\Pi(f)>0$ para todo $N\ge N_0(f)$. En ese rango los tres cocientes de (6.18) están bien definidos, y (E.9) y (E.19) dan

$$
\rho_N(f)\longrightarrow1, \qquad \kappa_N(f)\longrightarrow1, \qquad \eta_N^{\rm tot}(f)\longrightarrow1. \tag{E.20}
$$

 El umbral depende de $f$; no se asigna ningún cociente cuando su denominador es cero.

Para el espacio tensorial completo, escríbase $f=f_s+f_a$ de acuerdo con (D.2). La transformada de (E.2) entrelaza el intercambio de coordenadas con la trasposición matricial, de modo que $H^{(N)}(f_s)$ es simétrica y $H^{(N)}(f_a)$ es antisimétrica. La ortogonalidad de Frobenius en (E.5), junto con el núcleo antisimétrico exacto de (D.5), da

$$
I_N^\Pi(f)=I_N^\Pi(f_s)+I_N^\Pi(f_a), \qquad I_N^{[P]}(f)=I_N^{[P]}(f_s). \tag{E.21}
$$

 Combinando (E.9), (E.19) y (E.21),

$$
\frac{I_N^{[P]}(f)}{4N\|f\|_{\mathcal X}^2} \longrightarrow \frac{\|f_s\|_{\mathcal X}^2} {\|f_s\|_{\mathcal X}^2+\|f_a\|_{\mathcal X}^2} \qquad(f\ne0). \tag{E.22}
$$

Por último, por la definición de (6.2),

$$
\langle f,\widehat F_Nf\rangle =\frac{I_N^{[P]}(f)}{4N} \longrightarrow\|\Pi_{\rm sym}f\|_{\mathcal X}^2. \tag{E.23}
$$

 La polarización da convergencia débil de operadores a $\Pi_{\rm sym}$. Como $0\le\widehat F_N\le I$, también $\widehat F_N^2\le\widehat F_N$; usar esta desigualdad en la norma al cuadrado da

$$
\begin{aligned} \|\widehat F_Nf-\Pi_{\rm sym}f\|^2 &\le\langle f,\widehat F_Nf\rangle +\|\Pi_{\rm sym}f\|^2 -2\operatorname{Re} \langle\widehat F_Nf,\Pi_{\rm sym}f\rangle \longrightarrow0. \end{aligned}
$$

 Esto eleva la convergencia débil a

$$
\boxed{\widehat F_N\xrightarrow{\rm SOT}\Pi_{\rm sym}.} \tag{E.24}
$$

 Esta convergencia no es uniforme. Para $h_N=p_N\otimes p_N/\|p_N\|_{L^2}^2$, se tiene $\|h_N\|=1$, $h_N\perp V_N$ y por tanto

$$
\widehat F_Nh_N=0, \qquad \Pi_{\rm sym}h_N=h_N, \qquad \|\widehat F_N-\Pi_{\rm sym}\|\ge1 \quad\text{para todo }N. \tag{E.25}
$$

 El resultado es un teorema de retención en el espacio de Hilbert ambiente. Su aplicación a la geometría se restringe a tangentes de las que ya se sabe que provienen de trayectorias S1 admisibles.

## Apéndice F. Matrices y espectros exactos para $N=2,3,4$

Póngase

$$
x(t):=t-\frac12,\qquad q(t):=\left(t-\frac12\right)^2-\frac1{12},\qquad r(t):=\left(t-\frac12\right)^3       -\frac3{20}\left(t-\frac12\right). \tag{F.1}
$$

 La integración directa da las normas modales mutuamente ortogonales

$$
\|x\|^2=\frac1{12},\qquad \|q\|^2=\frac1{180},\qquad \|r\|^2=\frac1{2800}. \tag{F.2}
$$

 Para cardinalidad $N$, el experimento continuo de referencia consta de $N$ observaciones iid de la cópula. Por (A.4), su score es $2\sum_{k=1}^N f(U_k,V_k)$ y, por tanto,

$$
G_{\rm full}^{(N)}(f,g)=4N\langle f,g\rangle. \tag{F.3}
$$

 En cualquier base de $V_N$, los autovalores no nulos de $\widehat F_N$ son los autovalores generalizados de

$$
G_{[P]}^{(N)}v=\lambda\,G_{\rm full}^{(N)}v. \tag{F.4}
$$

 Así pues, la matriz de la forma de Fisher en una base no normalizada no es la matriz del operador $\widehat F_N$; la matriz de Gram continua de (F.4) proporciona la métrica respecto de la cual se representa el operador.

**Cardinalidad $N=2$.** Sea $e_{11}=x\otimes x$. La fórmula (6.6), equivalentemente (A.13) especializada a las dos clases de posets, da

$$
G_{[P]}^{(2)}(f,g) =256\langle f,e_{11}\rangle\langle g,e_{11}\rangle. \tag{F.5}
$$

 Puesto que $\|e_{11}\|^2=\|x\|^4=1/144$, evaluar (F.5) en $e_{11}$, junto con (F.3), produce

$$
[G_{[P]}^{(2)}]=\left(\frac1{81}\right), \qquad [G_{\rm full}^{(2)}]=\left(\frac1{18}\right). \tag{F.6}
$$

 Su cociente generalizado es por tanto

$$
\operatorname{spec}_+(\widehat F_2) =\left\{\frac{1/81}{1/18}\right\} =\left\{\frac29\right\}. \tag{F.7}
$$

**Cardinalidad $N=3$.** Úsese la base ortogonal ordenada

$$
e_{11}=x\otimes x,\qquad e_{12}=x\otimes q+q\otimes x,\qquad e_{22}=q\otimes q. \tag{F.8}
$$

 La sustitución de las cinco derivadas de clase en la fórmula de Fisher (A.13) da la primera matriz de abajo. Para la segunda, (F.2)–(F.3) dan $12\|e_{11}\|^2=1/12$, $12\|e_{12}\|^2=12\cdot2\|x\|^2\|q\|^2=1/90$ y $12\|e_{22}\|^2=1/2700$. Por tanto

$$
[G_{[P]}^{(3)}] =\operatorname{diag}\left( \frac1{32},\frac1{1200},\frac1{180000} \right), \qquad [G_{\rm full}^{(3)}] =\operatorname{diag}\left( \frac1{12},\frac1{90},\frac1{2700} \right). \tag{F.9}
$$

 Ambas matrices son diagonales en la misma base, de modo que sus cocientes generalizados entrada a entrada dan

$$
\operatorname{spec}_+(\widehat F_3) =\left\{\frac38,\frac3{40},\frac3{200}\right\}, \tag{F.10}
$$

 con autovectores $e_{11},e_{12},e_{22}$, respectivamente. Esto registra únicamente la anisotropía de Fisher dentro del soporte visible tridimensional fijado en §4.

**Cardinalidad $N=4$.** Exactamente en el orden usado en (6.9), póngase

$$
\begin{aligned} e_{11}&=x\otimes x,& e_{12}&=x\otimes q+q\otimes x,& e_{13}&=x\otimes r+r\otimes x,\\ e_{22}&=q\otimes q,& e_{23}&=q\otimes r+r\otimes q,& e_{33}&=r\otimes r. \end{aligned} \tag{F.11}
$$

 El cálculo exacto de los scores de clase a partir de (A.13) da

$$
[G_{[P]}^{(4)}] = \begin{pmatrix} 4/75&0&0&0&0&0\\ 0&8/3375&0&0&0&0\\ 0&0&1/55125&1/354375&0&1/38587500\\ 0&0&1/354375&11/455625&0&-1/49612500\\ 0&0&0&0&2/4134375&0\\ 0&0&1/38587500&-1/49612500&0&11/5402250000 \end{pmatrix}. \tag{F.12}
$$

 La ortogonalidad y (F.2)–(F.3) dan la matriz de Gram continua correspondiente

$$
[G_{\rm full}^{(4)}] =\operatorname{diag}\left( \frac19,\frac2{135},\frac1{1050}, \frac1{2025},\frac1{15750},\frac1{490000} \right). \tag{F.13}
$$

 Las entradas diagonales aisladas de (F.12)–(F.13) producen inmediatamente los tres canales puros

$$
\lambda_{11}=\frac{4/75}{1/9}=\frac{12}{25},\qquad \lambda_{12}=\frac{8/3375}{2/135}=\frac4{25},\qquad \lambda_{23}=\frac{2/4134375}{1/15750}=\frac4{525}. \tag{F.14}
$$

 Sobre el bloque invariante restante $\operatorname{span}\{e_{13},e_{22},e_{33}\}$, tomar $\det(G_{[P],\rm mix}^{(4)}-\lambda G_{\rm full,\rm mix}^{(4)})$ da, salvo un factor racional no nulo,

$$
144703125\lambda^3 -9975000\lambda^2 +142000\lambda -128. \tag{F.15}
$$

 Sus tres raíces son positivas porque el operador de Fisher $F_4$ es definido positivo sobre su soporte $V_4$. Sólo a título orientativo, como en §6, son

$$
0.0494521212879\ldots,\qquad 0.0185160720400\ldots,\qquad 0.000966047034941\ldots. \tag{F.16}
$$

 Combinar los tres factores puros con el bloque mezclado da el determinante característico generalizado completo, de nuevo salvo un factor racional no nulo:

$$
(25\lambda-12)(25\lambda-4)(525\lambda-4) \left( 144703125\lambda^3 -9975000\lambda^2 +142000\lambda -128 \right). \tag{F.17}
$$

Este apéndice únicamente documenta los cálculos exactos a $N$ fijo usados en §6. No proporciona ninguna fórmula espectral para todo $N$, no demuestra monotonía alguna de los autovalores con $N$, y no identifica $F_N$ con $P_N^{\rm vis}$. Los cocientes generalizados comparan la ley del poset no etiquetado con $N$ observaciones continuas de la cópula de referencia. No son fracciones de la geometría y no son resultados de reconstrucción. Aquí no se añade ninguna afirmación nueva.

## Apéndice G. Derivadas de segundo orden y núcleo de borrado uniforme

**El testigo y la verosimilitud finita.** Con $\ell_1,\ell_2$ como en (7.1) y el generador $\psi$ de (7.1)–(7.2),

$$
\bar\psi=0, \qquad \|\psi\|_{L^2(D)}^2=2,
$$

 establecido ya en §7; la realizabilidad no se reabre aquí. Para la integración polinómica exacta conviene usar la forma factorizada equivalente, obtenida de (7.1) por desarrollo directo en $u,v$:

$$
\psi(u,v) =-2\sqrt{15}\,(u-v)\bigl(6uv-3u-3v+2\bigr). \tag{G.1}
$$

 Para $\pi\in S_N$ y dos familias independientes de estadísticos de orden uniformes $U_{(1)}<\dots<U_{(N)}$, $V_{(1)}<\dots<V_{(N)}$, póngase

$$
T_\pi:=\sum_{i=1}^N\psi\bigl(U_{(i)},V_{(\pi(i))}\bigr). \tag{G.2}
$$

 Como $\psi$ está acotado sobre el compacto $D$, el integrando $e^{2\varepsilon T_\pi}$ que define el numerador y el integrando $e^{2\varepsilon\psi}$ que define $Z(\varepsilon)$, junto con sus derivadas en $\varepsilon$ de todo orden, están uniformemente dominados en todo intervalo compacto de $\varepsilon$; la derivación bajo la integral es por tanto válida a todo orden, de modo que tanto el numerador como $Z(\varepsilon)$ son real-analíticos, y $Z(\varepsilon)>0$ para todo $\varepsilon\in\mathbb R$ porque el integrando es estrictamente positivo. Así pues, exactamente como en (7.7),

$$
\boxed{ p_\pi(\varepsilon) =\frac{\bigl\langle e^{2\varepsilon T_\pi}\bigr\rangle_0}        {N!\,Z(\varepsilon)^N}, } \qquad Z(\varepsilon)=\int_De^{2\varepsilon\psi}\,d\mu_0, \tag{G.3}
$$

 donde $\langle\cdot\rangle_0$ es la esperanza, en $\varepsilon=0$, bajo los dos vectores independientes de estadísticos de orden, y $p_\pi$ es real-analítica en todo $\mathbb R$.

**Primera y segunda derivadas.** Puesto que $\bar\psi=0$, $Z'(0)=2\int_D\psi\,d\mu_0=0$ y

$$
Z''(0)=4\int_D\psi^2\,d\mu_0=4\|\psi\|_{L^2(D)}^2.
$$

 Desarrollar $\langle e^{2\varepsilon T_\pi}\rangle_0 =1+2\varepsilon\langle T_\pi\rangle_0 +2\varepsilon^2\langle T_\pi^2\rangle_0+O(\varepsilon^3)$ y $Z(\varepsilon)^{-N}=1-2N\|\psi\|_{L^2(D)}^2\varepsilon^2+O(\varepsilon^4)$ en (G.3) e igualar coeficientes da

$$
\boxed{ p_\pi'(0)=\frac2{N!}\langle T_\pi\rangle_0, } \qquad \boxed{ p_\pi''(0)=\frac4{N!} \left(\langle T_\pi^2\rangle_0-N\|\psi\|_{L^2(D)}^2\right). } \tag{G.4}
$$

 Esto reproduce (7.9); es una identidad escalar asociada a la única trayectoria (G.3), no la definición de un operador sobre $\bigwedge^2H$.

**Paridad.** Puesto que $\psi(v,u)=-\psi(u,v)$, reetiquetar las variables mudas en (G.2)–(G.3) — las familias de estadísticos de orden en $U$ y en $V$ son independientes e idénticamente distribuidas, de modo que intercambiar sus papeles es un cambio de variables válido — convierte $T_\pi$ en $-T_{\pi^{-1}}$ tras reindexar $j=\pi(i)$, y convierte $Z(\varepsilon)$ en $Z(-\varepsilon)$ con $Z(-\varepsilon)=Z(\varepsilon)$. Por tanto

$$
p_\pi(-\varepsilon)=p_{\pi^{-1}}(\varepsilon), \tag{G.5}
$$

 que es (7.7). Cada fibra $\Gamma_C$ es cerrada bajo inversión (§3), de modo que sumar (G.5) sobre $\Gamma_C$ da

$$
\boxed{ \mu_{N,\varepsilon}^{[P]}(C)=\mu_{N,-\varepsilon}^{[P]}(C) } \qquad(N\ge2,\ C\in\mathcal C_N), \tag{G.6}
$$

 que es (7.5). Toda derivada impar de toda probabilidad de clase se anula en $\varepsilon=0$; esto documenta el cálculo de §7 y no es un teorema de paridad nuevo.

**Cálculo autocontenido en $N=2$.** Las dos permutaciones de $S_2$ son la identidad, cuya fibra es la cadena, y la transposición, cuya fibra es la anticadena:

$$
T_{\rm chain}=\psi(U_{(1)},V_{(1)})+\psi(U_{(2)},V_{(2)}), \qquad T_{\rm antichain}=\psi(U_{(1)},V_{(2)})+\psi(U_{(2)},V_{(1)}),
$$

 con $(U_{(1)},U_{(2)})$ y $(V_{(1)},V_{(2)})$ dos pares independientes de estadísticos de orden de dos uniformes en $[0,1]$, distribuidos conjuntamente con densidad $2$ en cada símplex $0<t_1<t_2<1$.

Ambas permutaciones de $S_2$ son involuciones ($\mathrm{id}^{-1}=\mathrm{id}$, $\mathrm{swap}^{-1}=\mathrm{swap}$), de modo que (G.5) da $p_\pi(-\varepsilon)=p_\pi(\varepsilon)$ para cada una individualmente y, en particular,

$$
\langle T_{\rm chain}\rangle_0=\langle T_{\rm antichain}\rangle_0=0, \tag{G.7}
$$

 ya al nivel de una única permutación, no sólo de su clase — reproduciendo exactamente la anulación registrada para $N=2$ en (7.9).

Para los segundos momentos, desarróllese $\psi=\ell_1\otimes\ell_2-\ell_2\otimes \ell_1$ dentro de cada cuadrado. Como el proceso en $U$ es independiente del proceso en $V$, todo término cruzado factoriza en un producto de un momento de dos puntos en $U$ y un momento de dos puntos en $V$ (idénticamente distribuido a los momentos en $U$). Escríbase, para $j,k\in\{1,2\}$ y $i\in\{1,2\}$,

$$
A_{jk}:=\mathbb E\bigl[\ell_j(U_{(1)})\,\ell_k(U_{(2)})\bigr], \qquad M_i(jk):=\mathbb E\bigl[\ell_j(U_{(i)})\,\ell_k(U_{(i)})\bigr]. \tag{G.8}
$$

 La integración directa contra la densidad del par $2$ en $0<t_1<t_2<1$ y las densidades marginales de los estadísticos de orden $2(1-t)$ ($i=1$) y $2t$ ($i=2$) da los valores elementales

$$
A_{11}=A_{22}=0, \qquad A_{12}=-A_{21}=\frac1{\sqrt{15}}, \tag{G.9}
$$

$$
M_1(11)=M_1(22)=M_2(11)=M_2(22)=1, \qquad M_1(12)=-\frac2{\sqrt{15}}=-M_2(12). \tag{G.10}
$$

 Desarrollando $\psi(x,y)^2=\ell_1(x)^2\ell_2(y)^2 -2\ell_1(x)\ell_2(x)\ell_1(y)\ell_2(y)+\ell_2(x)^2\ell_1(y)^2$ y usando la independencia de los estadísticos de orden de índice igual o distinto de los dos procesos,

$$
\begin{aligned} \bigl\langle\psi(U_{(i)},V_{(i)})^2\bigr\rangle_0 &=2M_i(11)M_i(22)-2M_i(12)^2,\\ \bigl\langle\psi(U_{(1)},V_{(2)})^2\bigr\rangle_0 &=M_1(11)M_2(22)-2M_1(12)M_2(12)+M_1(22)M_2(11), \end{aligned}
$$

 y, desarrollando los productos cruzados $\psi(U_{(1)},V_{(1)})\psi(U_{(2)},V_{(2)})$ y $\psi(U_{(1)},V_{(2)})\psi(U_{(2)},V_{(1)})$ en cuatro términos cada uno y agrupando los factores en $U$ frente a los factores en $V$,

$$
\bigl\langle\psi(U_{(1)},V_{(1)})\psi(U_{(2)},V_{(2)})\bigr\rangle_0 =2A_{11}A_{22}-2A_{12}A_{21}, \qquad \bigl\langle\psi(U_{(1)},V_{(2)})\psi(U_{(2)},V_{(1)})\bigr\rangle_0 =-\bigl(A_{12}^2+A_{21}^2\bigr).
$$

 Sustituyendo (G.9)–(G.10): cada término diagonal de $T_{\rm chain}^2$ vale $2(1)(1)-2(2/\sqrt{15})^2=22/15$, y el término cruzado vale $2(0)(0)-2(1/\sqrt{15})(-1/\sqrt{15})=2/15$; cada término diagonal de $T_{\rm antichain}^2$ vale $1-2(-2/\sqrt{15})(2/\sqrt{15})+1=38/15$, y el término cruzado vale $-(1/15+1/15)=-2/15$. Sumando,

$$
\boxed{ \langle T_{\rm chain}^2\rangle_0 =2\cdot\frac{22}{15}+2\cdot\frac2{15}=\frac{16}5, \qquad \langle T_{\rm antichain}^2\rangle_0 =2\cdot\frac{38}{15}+2\left(-\frac2{15}\right)=\frac{24}5. } \tag{G.11}
$$

 Con $N\|\psi\|_{L^2(D)}^2=2\cdot2=4$, (G.4) y (G.11) dan

$$
\boxed{ \mu_2''(\mathrm{antichain})=\frac45\left(\frac{24}5-4\right)=\frac85, \qquad \mu_2''(\mathrm{chain})=\frac45\left(\frac{16}5-4\right)=-\frac85, } \tag{G.12}
$$

 junto con $\mu_{2,0}(\mathrm{antichain})=\mu_{2,0}(\mathrm{chain}) =\tfrac12$ a partir de la ley de referencia uniforme sobre $S_2$, y la comprobación exacta $\sum_C\mu_2''(C)=\tfrac85-\tfrac85=0$, consistente con (G.6) sumada sobre una masa total independiente de $\varepsilon$. Estas fracciones reproducen (7.10); la derivación anterior es autocontenida.

**El núcleo de borrado uniforme.** Para $m\ge3$ y clases no etiquetadas $C\in\mathcal C_m$, $D\in\mathcal C_{m-1}$, defínase

$$
K_{m,m-1}(C,D) :=\frac1m\#\{v\in C:[C\setminus\{v\}]=D\}. \tag{G.13}
$$

 *Bien definido sobre clases.* Fíjese un representante etiquetado de $C$; si $\phi:C\to C'$ es un isomorfismo de posets sobre otro representante, entonces para todo $v\in C$ la restricción $\phi|_{C\setminus\{v\}}$ es un isomorfismo $C\setminus\{v\}\to C'\setminus\{\phi(v)\}$, de modo que $\phi$ lleva $\{v\in C:[C\setminus v]=D\}$ biyectivamente sobre $\{v'\in C':[C'\setminus v']=D\}$. El recuento de (G.13), y por tanto $K_{m,m-1}(C,D)$, no depende del representante etiquetado elegido para $C$.

*Núcleo de Markov.* Cada sumando es un recuento no negativo, de modo que $K_{m,m-1}(C,D)\ge0$. Todo $v\in C$ se borra a un poset que está exactamente en una clase $D\in\mathcal C_{m-1}$, de modo que sumar el recuento sobre todos los $D$ cuenta cada uno de los $m$ elementos de $C$ exactamente una vez:

$$
\sum_{D\in\mathcal C_{m-1}}K_{m,m-1}(C,D)=\frac1m\sum_{v\in C}1=1. \tag{G.14}
$$

*Independencia del parámetro.* (G.13) es un recuento puramente combinatorio sobre posets finitos no etiquetados; no hace referencia alguna a $\varepsilon$ ni a $\mu_{m,\varepsilon}^{[P]}$.

*Borrado de un punto iid.* Sean $X_1,\dots,X_m$ iid de $q_\varepsilon$, y sea $V$ uniforme sobre $\{1,\dots,m\}$, independiente de la muestra. Para todo $j$ fijo, $(X_i)_{i\ne j}$ es una muestra iid de tamaño $m-1$ de $q_\varepsilon$, por ser un subvector fijo de un vector iid; promediar sobre la elección uniforme e independiente del índice borrado deja esta ley inalterada, de modo que la ley conjunta de $(X_i)_{i\ne V}$ es exactamente el producto $(m-1)$-ésimo de $q_\varepsilon$. Pasar a rangos y después al poset no etiquetado da, coordenada a coordenada,

$$
\boxed{ \mu_{m-1,\varepsilon}^{[P]}(D) =\sum_{C\in\mathcal C_m} \mu_{m,\varepsilon}^{[P]}(C)\,K_{m,m-1}(C,D) } \qquad(D\in\mathcal C_{m-1},\ m\ge3). \tag{G.15}
$$

**Composición hasta $N=2$.** Como en (7.13), defínase

$$
K_{N\to2}:=K_{3,2}\circ K_{4,3}\circ\cdots\circ K_{N,N-1}, \qquad K_{2\to2}:=I. \tag{G.16}
$$

 Iterar (G.15) desde $m=N$ hasta $m=3$ da, para todo $\varepsilon$ y todo $N\ge2$,

$$
\mu_{2,\varepsilon}^{[P]}=K_{N\to2}\,\mu_{N,\varepsilon}^{[P]}. \tag{G.17}
$$

**Conmutación con los jets.** Para $N$ fijo, ambos miembros de (G.17) son funciones de $\varepsilon$ con valores en los espacios de dimensión finita $\mathbb R^{\mathcal C_2}$ y $\mathbb R^{\mathcal C_N}$, y $K_{N\to2}$ es una aplicación lineal fija entre ellos, independiente de $\varepsilon$ por la tercera propiedad de (G.13). Derivar (G.17) $k$ veces conmuta por tanto término a término con esta aplicación lineal — una cuestión de linealidad sobre un espacio de dimensión finita, sin ningún argumento de límite ni asintótico:

$$
\boxed{ \bigl(\mu_2^{[P]}\bigr)^{(k)}(0) =K_{N\to2}\bigl(\mu_N^{[P]}\bigr)^{(k)}(0) } \qquad(k\ge1). \tag{G.18}
$$

**Cierre del Corolario 6.** Ensamblando las piezas anteriores: la paridad (G.6) da $r_N(\gamma_\psi)\ge2$ para todo $N\ge2$, por la definición (7.8). Si $(\mu_N^{[P]})''(0)$ se anulase para algún $N\ge2$, (G.18) con $k=2$ forzaría $K_{N\to2}(\mu_N^{[P]})''(0)=0$, es decir, $(\mu_2^{[P]})''(0)=0$ — contradiciendo los valores exactos $(8/5,-8/5)$ de (G.12). Por tanto, exactamente como en el Corolario 6 de §7,

$$
\boxed{ r_N(\gamma_\psi)=2\qquad\forall N\ge2. } \tag{G.19}
$$

 Esto cierra ese corolario; no se presenta como un resultado distinto.

Este apéndice trata una única trayectoria antisimétrica explícita, (G.1)–(G.3); no clasifica el segundo diferencial general sobre $\bigwedge^2H$, no define un operador $Q_N$ y no define un cono nulo cuadrático. No afirma que todo elemento de $\bigwedge^2H$ tenga $r_N=2$: (G.19) es un enunciado de existencia y no anulación para el único testigo $\psi$ de (7.1), propagado a todo $N\ge2$ mediante el núcleo de borrado independiente del parámetro de (G.13)–(G.18), no un resultado de clasificación. No se introduce ningún estimador, enunciado de consistencia ni tasa, y no se afirma ninguna reconstrucción no lineal. La anulación del jet de primer orden en (G.6) es el pliegue isométrico exacto $\varepsilon\leftrightarrow-\varepsilon$ del Teorema 5 y (7.4)–(7.6); no debe describirse como pérdida física de información. Lo que (G.19) detecta es la magnitud local de esta deformación a segundo orden, no su signo, que permanece identificado por el pliegue.

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
