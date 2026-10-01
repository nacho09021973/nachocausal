# Admisibilidad y retorno: formas conjuntas y criterio asintotico de unicidad

Fecha: 2026-09-07. Nota de trabajo con demostraciones y comprobaciones internas.
No constituye una adjudicacion independiente ni una prueba de unicidad radial.

El avance es incorporar el retorno a la misma jerarquia de momentos que
caracteriza la admisibilidad. Se obtiene una forma cuadratica creciente
\(\widehat Q_N\), calculable mediante matrices racionales, tal que
\[
\boxed{b\in\mathcal D(G),\quad Tb=b
\iff \sup_N\widehat Q_N(b)<\infty.}
\tag{1}
\]
Ademas, la unicidad temporal equivale a que ciertas capacidades escalares
decrecientes tiendan a cero. Se demuestra esta equivalencia, pero **no** la
anulacion de sus limites ni una tasa asintotica.

## 1. Entrada y alcance

Se usan las definiciones y las demostraciones de
[dominio de G por momentos](../2026-09-06/radial_dominio_G_2026-09-06/dominio_G_por_momentos.md),
secciones 1-7, y de
[energia y reconstruccion](../2026-09-06/radial_l2_global_2026-09-06/energia_positiva_y_reduccion_de_borde.md),
secciones 2 y 7. Los archivos del 6 de septiembre son una copia archivada y
permanecen intactos.

En particular, \(H_{\rm alt}\subset L^2((0,1)^2)\), \(B:H_{\rm alt}\to L^2(0,1)\)
es acotado, \(\mathscr A\) es acotado e inyectivo y
\[
\mathscr A g=-6Ub\iff b\in\mathcal D(G),\quad g=Gb,
\qquad Ub(x,y)=b(x)+b(y).
\tag{2}
\]
El retorno \(T=BG\) solo esta definido en \(\mathcal D(G)\).

Escribimos \(a(z)=z(1-z)\), \(\phi_k(z)=a(z)^2z^k\),
\(u_k(b)=\langle b,\phi_k\rangle\), \(\mathbf u_N=(u_0,\ldots,u_N)^T\).
Los polinomios reales \(F_\alpha,r_\alpha\), indexados por \(i\le j\), \(i+j\le N\),
satisfacen
\[
\langle Gb,F_\alpha\rangle=-12\langle b,r_\alpha\rangle,
\quad c_N=-12R_N\mathbf u_N,\quad
M_N=(\langle F_\beta,F_\alpha\rangle)_{\alpha\beta}>0.
\]
Su espacio \(E_N\) es creciente y su union es densa en \(H_{\rm alt}\).
Denotamos por \(P_N\) la proyeccion ortogonal sobre \(E_N\). La reconstruccion
finita original y su norma son
\[
g_N=\sum_\alpha(M_N^{-1}c_N)_\alpha F_\alpha,
\qquad Q_N=\|g_N\|_2^2=\mathbf u_N^*H_N\mathbf u_N.
\tag{3}
\]
Todas las formulas matriciales siguientes usan bases reales; los datos pueden
ser complejos y \(^*\) denota traspuesta conjugada. El producto escalar es lineal
en el primer argumento.

## 2. Pruebas polinomicas para el retorno

La condicion \(BGb=b\) equivale, en el dominio admisible, a
\[
\langle Gb,D_k\rangle=u_k(b)\quad(k\ge0),\qquad D_k=B^*\phi_k.
\tag{4}
\]
Es suficiente esta familia porque \(\operatorname{span}\{\phi_k\}\) es denso
en \(L^2(0,1)\): si \(h\) es ortogonal, \(a^2h\) es ortogonal a todos los
polinomios y por tanto \(h=0\) casi por doquier.

Los \(D_k\) son polinomios explicitos. De las formulas de \(C,E\) se obtiene
\[
C^*\phi_k(s)=s\int_s^1z^k(1-z)^3\,dz=:c_k(s),\qquad
E^*\phi_k(s)=\frac{(1-s)s^{k+4}}{k+4}=:e_k(s).
\]
Usando las dos marginales de \(B\), y proyectando sobre el subespacio
antisimetrico,
\[
\boxed{D_k(x,y)=\tfrac12\big[(1-x)c_k(y)-xe_k(y)
                         -(1-y)c_k(x)+ye_k(x)\big].}
\tag{5}
\]
La formula procede de Fubini y del adjunto de los operadores acotados. No
introduce trazas de \(g\) ni exige resolver otra ecuacion de reconstruccion.

## 3. Independencia y una forma conjunta creciente

**Lema de independencia para todo N.** La familia formada por los
\(F_\alpha\), \(i+j\le N\), y los \(D_k\), \(0\le k\le N\), es linealmente
independiente. En efecto, todos los \(F_\alpha\) se anulan en \(x=0\): esto
se ve en su formula, por el factor \(\omega^2\) y las condiciones de Dirichlet
de \(S\otimes S\). En cambio, para un polinomio \(p\) y \(D_p=B^*(a^2p)\),
\[
D_p(0,y)=\frac y2\int_y^1(1-z)^3p(z)\,dz.
\tag{5a}
\]
Si \(D_p\in E_N\), esta expresion es cero. Dividiendo por \(y\) en el
interior y derivando, resulta \((1-y)^3p(y)=0\), luego \(p=0\).
La independencia de los \(F_\alpha\) completa la prueba. Solo se evalua una
identidad entre polinomios; no se toman trazas de funciones \(L^2\) generales.

Para \(b\in L^2(0,1)\), definimos el conjunto afin de restricciones finitas
\[
\mathcal C_N(b)=\{h\in H_{\rm alt}:
\langle h,F_\alpha\rangle=(c_N)_\alpha\ (i+j\le N),\quad
\langle h,D_k\rangle=u_k(b)\ (0\le k\le N)\}.
\]
Sea
\[
\widehat Q_N(b)=\min_{h\in\mathcal C_N(b)}\|h\|_2^2,
\tag{6}
\]
El lema implica que este conjunto es no vacio para todo dato y todo nivel.
Tiene un unico minimizador \(\widehat g_N\), en el espacio generado por las
pruebas finitas. Por tanto \(\widehat Q_N\) es finita para todo \(b\) a cada
nivel; el valor infinito puede aparecer solo en el limite.

**Proposicion.** Las formas \(\widehat Q_N\) son crecientes,
\(\widehat Q_N\ge Q_N\), y satisfacen (1). En el caso finito,
\[
\widehat g_N\longrightarrow Gb\text{ fuertemente},\qquad
\lim_N\widehat Q_N(b)=\|Gb\|_2^2.
\tag{7}
\]

**Demostracion.** Los conjuntos afines se anidan. Para \(M\ge N\),
\(\widehat g_M-\widehat g_N\) es ortogonal a todas las pruebas
de nivel \(N\), luego a \(\widehat g_N\). Asi,
\[
\|\widehat g_M-\widehat g_N\|_2^2
=\widehat Q_M(b)-\widehat Q_N(b).
\tag{8}
\]
Si las normas estan acotadas, los minimizadores convergen fuertemente a \(g\).
Las restricciones \(F_\alpha\), por la caracterizacion anterior, dan
\(b\in\mathcal D(G)\) y \(g=Gb\). Las restricciones \(D_k\) y la densidad de
\(\phi_k\) dan \(Bg=b\). Reciprocamente, para un dato admisible y fijo, \(Gb\)
satisface todas las restricciones y \(\widehat g_N\) es su proyeccion sobre el
espacio de pruebas conjunto. La densidad ya se sigue de los \(F_\alpha\).
Esto prueba (7) y completa la equivalencia.

## 4. Complemento de Schur: coste exacto del defecto de retorno

Definamos las matrices racionales
\[
(L_N)_{\alpha k}=\langle D_k,F_\alpha\rangle,\quad
(Z_N)_{jk}=\langle D_k,D_j\rangle,\quad
\Sigma_N=Z_N-L_N^TM_N^{-1}L_N>0.
\tag{9}
\]
La matriz \(\Sigma_N\) es el Gram de \((I-P_N)D_0,\ldots,(I-P_N)D_N\).
Su positividad estricta para todo \(N\) es consecuencia del lema anterior.
El defecto finito es
\[
\delta_N(b)=\mathbf u_N-L_N^TM_N^{-1}c_N
=J_N\mathbf u_N,\qquad J_N=I+12L_N^TM_N^{-1}R_N.
\tag{10}
\]
Su componente \(k\) es \(\langle b-Bg_N,\phi_k\rangle\).

Toda solucion de las restricciones \(F_\alpha\) es \(g_N+h\), con
\(h\perp E_N\). Las restricciones restantes son
\(\langle h,(I-P_N)D_k\rangle=(\delta_N)_k\). La solucion de minima norma da
\[
\boxed{
\widehat Q_N(b)=Q_N(b)+\delta_N(b)^*\Sigma_N^{-1}\delta_N(b).}
\tag{11}
\]
La matriz racional de esta forma sobre los primeros \(N+1\) momentos es
\[
\boxed{\widehat H_N=H_N+J_N^T\Sigma_N^{-1}J_N>0.}
\tag{12}
\]
Como todo vector finito de momentos se realiza mediante un dato \(L^2\),
la monotonia tambien da una desigualdad matricial para todo \(N\):
\(\widehat H_{N+1}\ge\operatorname{diag}(\widehat H_N,0)\).

**Consecuencia asintotica.** Para cada \(k\) fijo,
\[
(\Sigma_N)_{kk}=\|(I-P_N)D_k\|_2^2\longrightarrow0.
\tag{13}
\]
Por Cauchy-Schwarz,
\[
|\langle b-Bg_N,\phi_k\rangle|^2
\le(\widehat Q_N-Q_N)(\Sigma_N)_{kk}\qquad(N\ge k).
\tag{14}
\]
Si \(b\) es admisible pero no fijo, algun defecto limite es no nulo y (13)-(14)
fuerzan \(\widehat Q_N(b)\to+\infty\), incluso cuando \(Q_N(b)\) permanece
acotado. Mas generalmente, para cada bloque fijo \(0\le j,k\le m\),
las entradas de \(\Sigma_N\) tienden a cero por Cauchy-Schwarz. La norma del
inverso de ese bloque tiende a infinito. Esto identifica una degeneracion
asintotica concreta, sin establecer todavia su tasa.

Por ejemplo, \(Gb_d=y-x\) y \(Tb_d-b_d=a/12\), de modo que
\[
Q_N(b_d)\longrightarrow\frac16,\qquad
\langle b_d-Bg_N(b_d),\phi_0\rangle\longrightarrow
-\frac1{12}\int_0^1a^3=-\frac1{1680}.
\]
Por tanto \(\widehat Q_N(b_d)\to+\infty\). Para el modo temporal,
\(\widehat Q_N(b_t)\to1/90\). Estas conclusiones se deducen analiticamente de
las identidades anteriores; no se infieren de las tablas.

## 5. Paridad y eliminacion del modo conocido

Sean \(\mathcal Rb(z)=b(1-z)\) y \(\rho g(x,y)=g(1-x,1-y)\).
Las formulas de los operadores dan
\[
B\rho=-\mathcal RB,\quad \mathscr A\rho=-\rho\mathscr A,
\quad G\mathcal R=-\rho G,\quad T\mathcal R=\mathcal RT.
\tag{15}
\]
Las dos ultimas identidades se entienden en el dominio: (2) prueba tambien
que \(\mathcal R\mathcal D(G)=\mathcal D(G)\).

Los espacios de pruebas de cada nivel son invariantes por reflexion:
\(\rho F_P=-F_{\rho P}\) y \(\rho B^*\phi=-B^*\mathcal R\phi\).
La transformacion \(h\mapsto-\rho h\) lleva \(\mathcal C_N(b)\) en
\(\mathcal C_N(\mathcal Rb)\). Las partes de distinta paridad son ortogonales,
y por ello, con \(b_\pm=(b\pm\mathcal Rb)/2\),
\[
\widehat Q_N(b)=\widehat Q_N(b_+)+\widehat Q_N(b_-).
\tag{16}
\]
En las coordenadas centradas
\(v_k(b)=\langle b,a^2(2z-1)^k\rangle\), las matrices se
separan en bloques par e impar.

El modo \(b_t=-(2z-1)(3z^2-3z+1)/24\) tiene \(v_1(b_t)=-1/10080\).
Definimos el hiperplano
\[
X=\{b\in L^2:v_1(b)=0\}.
\tag{17}
\]
Como el espacio fijo es lineal y contiene \(b_t\), la unicidad equivale a
\[
\boxed{b\in X,\quad\sup_N\widehat Q_N(b)<\infty\ \Longrightarrow\ b=0.}
\tag{18}
\]
En efecto, a cualquier dato fijo se le puede restar
\(v_1(b)b_t/v_1(b_t)\). No se identifica este hiperplano con un complemento
ortogonal en la norma de reconstruccion.

## 6. Capacidades escalares: equivalencia exacta con la unicidad

Para \(N\ge\max\{1,k\}\), definimos
\[
\kappa_{N,k}=\sup\left\{|v_k(b)|^2:
b\in X,\quad \|b\|_2^2+\widehat Q_N(b)\le1\right\}.
\tag{19}
\]
Estas cantidades son finitas, no negativas y decrecientes en \(N\).
El termino \(\|b\|_2^2\) permite tratar sucesiones de datos distintos mediante
compacidad debil. La convergencia de \(g_N(b)\) para un dato fijo, por si sola,
no justificaria ese paso.

**Teorema.** Si \(\mathcal F=\{b\in\mathcal D(G):Tb=b\}\), entonces
\[
\boxed{\lim_N\kappa_{N,k}
=\sup\{|v_k(b)|^2:b\in\mathcal F\cap X,
                  \ \|b\|_2^2+\|Gb\|_2^2\le1\}.}
\tag{20}
\]
En consecuencia,
\[
\boxed{\mathcal F=\operatorname{span}\{b_t\}
\iff \lim_N\kappa_{N,k}=0\quad\text{para cada }k\ge0.}
\tag{21}
\]
El indice \(k=1\) es trivial por la normalizacion; los demas no se omiten.

**Demostracion.** Todo dato del supremo derecho satisface las restricciones
de (19) en cada nivel, lo que da una desigualdad. Para la otra, elegimos
datos casi maximizantes \(b_N\) en (19) y sus minimizadores \(h_N=\widehat g_N(b_N)\).
La pareja esta acotada en \(L^2(0,1)\oplus H_{\rm alt}\). Una subsucesion
converge debilmente a \((b,g)\). Para cada prueba fija, las restricciones se
cumplen desde algun nivel y pasan al limite:
\[
\langle g,F_\alpha\rangle=-12\langle b,r_\alpha\rangle,
\qquad \langle g,D_j\rangle=\langle b,\phi_j\rangle.
\]
Por (2) y densidad, \(g=Gb\), \(Bg=b\), y \(b\in X\).
La semicontinuidad debil da \(\|b\|_2^2+\|g\|_2^2\le1\), mientras
\(v_k(b_N)\to v_k(b)\). Se obtiene (20).
Si todos los limites son cero, todo \(b\in\mathcal F\cap X\) tiene todos sus
momentos centrados nulos, tras reescalarlo a la bola unidad. La densidad de
la familia \(a^2p\), con \(p\) polinomico, fuerza \(b=0\).
La implicacion inversa es inmediata.

## 7. Formula racional de las capacidades

El Gram de las funciones de momentos es
\[
(W_N)_{ij}=\int_0^1a(z)^4z^{i+j}\,dz,\qquad W_N>0.
\]
Todo vector de momentos se realiza mediante un dato \(L^2\); la menor norma
cuadrada que lo realiza es \(\mathbf u^*W_N^{-1}\mathbf u\). Se alcanza en
\(\operatorname{span}\{\phi_0,\ldots,\phi_N\}\).

Sea \(\ell_k\) la fila racional tal que \(v_k=\ell_k\mathbf u\), es decir,
\((\ell_k)_j=\binom{k}{j}2^j(-1)^{k-j}\) para \(j\le k\), y cero despues.
Pongamos
\[
A_N=W_N^{-1}+\widehat H_N.
\]
Si \(V_N\) tiene como columnas una base del hiperplano de momentos
\(\ell_1\mathbf u=0\), entonces
\[
\boxed{\kappa_{N,k}=\ell_kV_N(V_N^TA_NV_N)^{-1}V_N^T\ell_k^T.}
\tag{22}
\]
Esta formula es racional. Equivalentemente,
\[
\kappa_{N,k}=\ell_k\left[A_N^{-1}
-\frac{A_N^{-1}\ell_1^T\ell_1A_N^{-1}}
       {\ell_1A_N^{-1}\ell_1^T}\right]\ell_k^T.
\tag{23}
\]
Asi, (21) es una pregunta asintotica sobre matrices finitas explicitas.
Ni un valor pequeno a grado finito ni un ajuste de una tasa prueban un
limite cero. No se ha demostrado que baste comprobar un numero finito de
indices \(k\).

## 8. Verificacion y siguiente obstaculo

El archivo [verify_joint_moments.py](verify_joint_moments.py) reutiliza las
pruebas \(F_\alpha\) del verificador archivado y comprueba por aritmetica exacta:

- El adjunto (5) contra la formula directa de \(B\) para varios polinomios.
- Las trazas polinomicas empleadas en el lema de independencia.
- Las identidades de los modos temporal y adicional y el defecto \(-1/1680\).
- El complemento de Schur contra la inversion independiente del Gram conjunto.
- Positividad de \(\Sigma_N\), monotonia matricial de \(\widehat H_N\) tras
  incluir los momentos anteriores, y separacion por paridad, en los niveles calculados.
- Las cotas temporales \(\widehat Q_N(b_t)\le1/90\), la desigualdad (14),
  y la monotonia y el optimizador de las capacidades finitas.

Ejecucion desde la raiz del repositorio:

```bash
python3 research_program/radial_3p1/2026-09-07/verify_joint_moments.py --degree 4
python3 research_program/radial_3p1/2026-09-06/archive_tools.py verify
```

El resultado se guarda en
[verification_joint_moments.json](verification_joint_moments.json), con la
version de SymPy y hashes del verificador y del codigo fuente reutilizado.
Las pruebas para todo \(N\) son los argumentos analiticos de esta nota; el
verificador comprueba identidades finitas y no sustituye una revision independiente.

Primeras secciones, redondeadas solo para lectura:

| N | Q_N(b_d) | Qhat_N(b_d) | Qhat_N(b_t) | kappa_N,0 |
|---:|---:|---:|---:|---:|
| 1 | 0.08856683 | 0.12804728 | 0.00639582 | 7.649106e-6 |
| 2 | 0.11682066 | 0.19511542 | 0.00639582 | 7.248526e-6 |
| 3 | 0.11682066 | 0.19511542 | 0.00849886 | 7.248526e-6 |
| 4 | 0.13160427 | 0.31734337 | 0.00849886 | 6.448304e-6 |

Ya \(\widehat Q_2(b_d)>1/6=\|Gb_d\|_2^2\) da un certificado finito de que
ese dato admisible no es fijo: si lo fuera, \(Gb_d\) realizaria todas las
restricciones con norma cuadrada \(1/6\). Esta exclusion no se basa en
extrapolar la tabla. Los valores de las capacidades dependen de la
normalizacion de los momentos; su magnitud pequena no prueba un limite cero.

La tarea pendiente queda mas localizada: controlar el complemento de Schur
\(\Sigma_N\) junto con el defecto \(J_N\mathbf u_N\), o demostrar directamente
\(\kappa_{N,k}\to0\) para cada momento fijo despues de eliminar \(b_t\).
La descomposicion por paridad permite separar la exclusion de todos los datos
pares de la unicidad del dato temporal en el sector impar. La clasificacion
global de \(\mathcal D(G)\), las tasas y la unicidad radial siguen abiertas.
