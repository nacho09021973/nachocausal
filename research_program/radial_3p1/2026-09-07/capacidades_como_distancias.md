# Capacidades como distancias: objetivo dual y limite de la ruta por densidad

Fecha: 2026-09-07. Desarrollo analitico posterior al
[criterio conjunto congelado](criterio_conjunto_momentos.md).
Los tres archivos de esa etapa se identifican por SHA-256 en
[FROZEN_JOINT_CRITERION.json](FROZEN_JOINT_CRITERION.json).

Objetivo unico: demostrar \(\kappa_{N,k}\to0\) para cada momento fijo, separando
los sectores par e impar. Esta nota identifica exactamente las capacidades
como distancias y construye una unica sucesion escalar equivalente.
**No demuestra todavia la densidad necesaria ni la unicidad radial.**

## 1. El espacio, el vector y las restricciones

Conservamos \(F_\alpha,r_\alpha,D_k,\phi_k,B,G\) y \(\widehat Q_N\) de la
nota congelada. Definimos
\[
\psi_k(z)=a(z)^2(2z-1)^k,\qquad v_k(b)=\langle b,\psi_k\rangle,
\quad \mathscr H=L^2(0,1)\oplus H_{\rm alt},
\]
\[
\|(b,g)\|_{\mathscr H}^2=\|b\|_2^2+\|g\|_2^2.
\tag{1}
\]
El vector que intentamos aproximar es \(e_k=(\psi_k,0)\). Los generadores
de las restricciones son
\[
s_\alpha=(12r_\alpha,F_\alpha),\qquad
t_j=(-\phi_j,D_j),\qquad e_1=(\psi_1,0).
\tag{2}
\]
Para \(N\ge1\), ponemos
\[
\mathscr S_N=\operatorname{span}\{s_\alpha:i+j\le N;\ t_j:0\le j\le N;\ e_1\},
\qquad \mathscr Z_N=\mathscr S_N^\perp.
\tag{3}
\]
La notacion \(i+j\le N\) en la primera familia corresponde a los indices
\(\alpha=(i,j)\) de las pruebas simetricas. En la segunda familia el indice es
unidimensional.

Por construccion, \((b,g)\in\mathscr Z_N\) si y solo si
\[
\langle g,F_\alpha\rangle=-12\langle b,r_\alpha\rangle,\qquad
\langle g,D_j\rangle=\langle b,\phi_j\rangle,\qquad v_1(b)=0.
\tag{4}
\]
La menor norma de \(g\) compatible con \(b\) es precisamente
\(\widehat Q_N(b)^{1/2}\). En consecuencia, para \(N\ge\max\{1,k\}\),
\[
\kappa_{N,k}
=\sup_{w\in\mathscr Z_N,\ \|w\|_{\mathscr H}\le1}
             |\langle w,e_k\rangle|^2.
\tag{5}
\]

## 2. Identidad exacta de distancia y el limite

Sea \(\Pi_N\) la proyeccion ortogonal sobre \(\mathscr S_N\). La representacion
de Riesz del funcional de (5) en \(\mathscr Z_N\) es \((I-\Pi_N)e_k\).
Cauchy-Schwarz, con igualdad en su direccion si es no nulo, prueba
\[
\boxed{\kappa_{N,k}=\|(I-\Pi_N)e_k\|_{\mathscr H}^2
                   =\operatorname{dist}_{\mathscr H}(e_k,\mathscr S_N)^2.}
\tag{6}
\]
Asi, la metrica no es una norma indefinida sobre sucesiones de momentos:
es la norma ordinaria del producto (1). La matriz
\(W_N^{-1}+\widehat H_N\) de la nota anterior resulta al minimizar esta norma
sobre los representantes con momentos prescritos.

Sea \(\mathscr S_\infty=\overline{\bigcup_N\mathscr S_N}\). Como los espacios
son crecientes,
\[
\boxed{\lim_N\kappa_{N,k}
=\operatorname{dist}_{\mathscr H}(e_k,\mathscr S_\infty)^2.}
\tag{7}
\]
Se puede probar sin invocar un teorema adicional: la distancia al cierre de
la union es la infima de las distancias a los espacios finitos. Tambien
\(\Pi_Ne_k\to\Pi_\infty e_k\) fuertemente, pues para \(M\ge N\)
\[
\|\Pi_Me_k-\Pi_Ne_k\|_{\mathscr H}^2
=\|\Pi_Me_k\|_{\mathscr H}^2-\|\Pi_Ne_k\|_{\mathscr H}^2.
\]

## 3. Que densidad falta, y cual no basta

Las restricciones de todos los niveles dan exactamente
\[
\boxed{\mathscr S_\infty^\perp
=\{(b,Gb):b\in\mathcal D(G),\ BGb=b,\ v_1(b)=0\}.}
\tag{8}
\]
En efecto, la familia \(F_\alpha\) y la equivalencia de reconstruccion
identifican \(g=Gb\); los \(D_j\) identifican \(Bg=b\). Esta es una
identificacion del ortogonal, no una prueba de que sea cero.

Resulta la equivalencia precisa
\[
\boxed{\kappa_{N,k}\to0\ \text{para todo }k
\iff e_k\in\mathscr S_\infty\ \text{para todo }k
\iff \mathscr S_\infty=\mathscr H.}
\tag{9}
\]
Para la ultima implicacion, si todos los \(e_k\) estan en el cierre y
\((b,g)\) es ortogonal a este, la densidad de \(\psi_k\) implica \(b=0\).
Entonces las restricciones \(F_\alpha\) y su completitud implican \(g=0\).

La completitud de los \(F_\alpha\) por separado **no** prueba (9). Sus
levantamientos son \((12r_\alpha,F_\alpha)\), con una primera componente
acoplada. Tampoco basta la densidad de los polinomios en cada factor.
Por ejemplo, los vectores \((f,f)\) tienen proyecciones densas en ambos
factores de \(L^2\oplus L^2\), pero su espacio cerrado es solo la diagonal.

Ademas, si no se anade \(e_1\), todos los generadores son ortogonales al
vector conocido \((b_t,g_t)\). Por tanto la familia sin normalizacion no
puede ser densa. Eliminar ese vector conocido no excluye automaticamente
otros vectores de (8).

La via cualitativa por densidad es valida, pero necesita una construccion
adicional de aproximantes. Usar (8) para declarar el ortogonal nulo
supondria precisamente la unicidad que se intenta probar.

## 4. Aproximantes concretos y separacion por paridad

La formula (6) equivale al siguiente problema polinomico, con
\(P\) simetrico de grado total a lo sumo \(N\), \(p\) unidimensional de grado
a lo sumo \(N\), y \(\lambda\) escalar:
\[
\boxed{\kappa_{N,k}=\min_{P,p,\lambda}
\left\|\psi_k-12r_P+a^2p-\lambda\psi_1\right\|_2^2
+\left\|F_P+B^*(a^2p)\right\|_2^2.}
\tag{10}
\]
El indice \(N\) limita los grados de las pruebas de entrada, no el grado de
los polinomios despues de aplicar los operadores. Todos los terminos se
calculan con integrales de polinomios racionales.

Definimos la involucion unitaria
\[
\mathscr R(b,g)=(\mathcal Rb,-\rho g),\qquad
\mathcal Rb(z)=b(1-z),\quad\rho g(x,y)=g(1-x,1-y).
\tag{11}
\]
Los generadores y la normalizacion muestran que \(\mathscr S_N\) es invariante
por \(\mathscr R\). Como \(\mathscr Re_k=(-1)^ke_k\), la proyeccion de \(e_k\)
queda en su mismo sector. En (10) se pueden restringir \(P\) y \(p\) a la
paridad \((-1)^k\) respecto de la reflexion simultanea y unidimensional,
respectivamente. Para \(k\) par se toma \(\lambda=0\); para \(k\) impar se
permite la correccion temporal.

Los dos objetivos son, por tanto, aproximar \((\psi_{2j},0)\) en el sector
par y \((\psi_{2j+3},0)\) en el sector impar con la normalizacion. El indice
impar \(1\) ya tiene distancia cero por construccion.

## 5. Cancelar exactamente la primera componente

Para \(N\ge\max\{1,k\}\), el cociente \(r_P/a^2\) es polinomico de grado
a lo sumo \(N\). Por ello se puede imponer
\[
a^2p=12r_P-\psi_k+\lambda\psi_1.
\tag{12}
\]
Definamos los polinomios antisimetrico y objetivo
\[
Y_P=F_P+12B^*r_P,\qquad d_k=B^*\psi_k,
\]
y la distancia auxiliar
\[
\eta_{N,k}=\operatorname{dist}_{L^2(Q)}
\big(d_k,\operatorname{span}\{Y_P:\deg P\le N;\ d_1\}\big)^2.
\tag{13}
\]
En el sector par se omite \(d_1\). Entonces
\[
\boxed{\kappa_{N,k}\le\eta_{N,k}
                  \le(1+\|B\|^2)\kappa_{N,k}.}
\tag{14}
\]
La primera desigualdad procede de (12). Para la segunda, sea
\(u=\psi_k-12r_P+a^2p-\lambda\psi_1\) y
\(v=F_P+B^*(a^2p)\) el residuo de cualquier aproximante de (10).
Sustituir \(a^2p\) por \(a^2p-u\) anula exactamente la primera componente
y deja \(v-B^*u\) en la segunda. Por acotacion de \(B\),
\[
\|v-B^*u\|_2^2\le(1+\|B\|^2)(\|u\|_2^2+\|v\|_2^2).
\]
Tomar infimos prueba (14). Este paso solo utiliza que \(B\) es acotado;
no requiere conocer una constante optima.

Asi, para cada \(k\), basta y es necesario construir polinomios \(P_n\)
y escalares \(\lambda_n\) de la paridad correspondiente tales que
\[
\boxed{\|Y_{P_n}-d_k+\lambda_nd_1\|_2\longrightarrow0.}
\tag{15}
\]
Esto identifica el objetivo de aproximacion concreto. Pero la completitud
de \(F_P\) no se transporta automaticamente a \(Y_P\). De hecho,
\(Y_P=K^*(\omega^2P)\), por la identidad
\(\mathscr A=K-6UB\) y \(U^*(\omega^2P)=2r_P\). Esta observacion localiza
la dificultad de densidad; no aporta un teorema de rango denso para ese
operador ni resuelve su nucleo.

## 6. Positividad estricta a todo grado finito

El lema de independencia congelado implica
\[
\mathscr S_N\cap\big(L^2(0,1)\oplus\{0\}\big)
=\operatorname{span}\{e_1\}.
\tag{16}
\]
En efecto, la anulacion de la segunda componente de una combinacion de
generadores fuerza que todos los coeficientes de \(F_\alpha,D_j\) sean cero.
Solo queda el generador de normalizacion.

Como \(\mathscr S_N\) es finito-dimensional y cerrado, y \(\psi_k\) no es
proporcional a \(\psi_1\) cuando \(k\ne1\),
\[
\boxed{\kappa_{N,k}>0\quad(k\ne1,\ N\ge\max\{1,k\}).}
\tag{17}
\]
Por tanto, aunque la unicidad resulte cierta, ninguna capacidad no trivial
sera exactamente cero a grado finito. La prueba debe controlar el cierre,
no esperar una anulacion algebraica en algun truncamiento.

## 7. Una unica sucesion escalar racional

Hasta aqui hay una familia numerable de limites, uno por \(k\). Se puede
construir una sola sucesion con la misma informacion. Sea
\[
s_k=\|\psi_k\|_2^2>0,\quad
c_N=\sum_{k=0}^N2^{-k-1}\frac{\kappa_{N,k}}{s_k}+2^{-N-1},\qquad N\ge1.
\tag{18}
\]
Los \(s_k\) y \(\kappa_{N,k}\) son racionales. Ademas
\(0\le\kappa_{N,k}/s_k\le1\), directamente de (5). La cola geometrica
\(2^{-N-1}\) es una cota superior para todos los indices aun no incluidos.

Al aumentar \(N\), las contribuciones existentes no crecen. La nueva
contribucion es a lo sumo \(2^{-N-2}\), y la cola disminuye en esa misma
cantidad. Por tanto
\[
\boxed{0<c_{N+1}\le c_N\le1,\qquad
c_N\to0\iff\kappa_{N,k}\to0\ \text{para cada }k.}
\tag{19}
\]
Para la implicacion directa se usa
\(2^{-k-1}\kappa_{N,k}/s_k\le c_N\). Para la inversa, se fija primero un
numero finito de indices, se pasa al limite en ellos y despues se hace
arbitrariamente pequena la cola geometrica. No se intercambian limites
sin una cota sumable.

El mismo argumento aplicado por separado a los indices pares e impares
conserva la separacion de sectores. Esta agregacion hace literal el objetivo
de una sola sucesion escalar; no demuestra la anulacion de su limite.

## 8. Alcance de la penalizacion y siguiente paso

De \(\Sigma_N\to0\) en bloques fijos no se deduce que cualquier defecto
finito no nulo produzca divergencia. Por ejemplo, para un bloque escalar
\(\Sigma_N=N^{-2}\) y \(\delta_N=N^{-2}\), la penalizacion es \(N^{-2}\).
El defecto puede decrecer mas deprisa que la escala penalizada. En el
problema actual, incluso un dato fijo exacto puede tener defectos no nulos
en sus reconstrucciones finitas.

La conclusion demostrada para \(b_d\) usa algo mas preciso: un momento fijo
del defecto tiene limite no nulo. Tampoco se ha establecido la monotonia
del termino \(\widehat Q_N-Q_N\) por separado; la forma conjunta si es creciente.

El siguiente paso analitico es construir los aproximantes de (10) o (15),
o encontrar una obstruccion exacta a esa aproximacion. La densidad requerida
en (9) sigue abierta. La reduccion a distancias no debe citarse como prueba
de que la unicidad este proxima a resolverse.

## 9. Comprobacion finita de las nuevas identidades

[verify_capacity_distances.py](verify_capacity_distances.py) comprueba, en
los mismos grados \(1\le N\le4\) ya congelados, la formula de distancia (6)
mediante el Gram de las parejas (2), y compara sus valores exactos con las
capacidades anteriores. Tambien comprueba (12) sobre los minimizadores,
la cota \(\kappa\le\eta\), la paridad de la proyeccion y la monotonia de
\(c_N\). No aumenta la tabla de grados ni busca una tasa.

El verificador valida los hashes congelados antes y despues de ejecutarse.
Sus resultados quedan en
[verification_capacity_distances.json](verification_capacity_distances.json).
Las demostraciones anteriores son analiticas; la comprobacion finita no
prueba densidad ni unicidad y no sustituye una revision independiente.
