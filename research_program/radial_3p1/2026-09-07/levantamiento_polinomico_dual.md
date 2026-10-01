# El levantamiento dual no tiene una solucion polinomica exacta no trivial

Fecha: 2026-09-07. Nota de trabajo analitica. Se conservan intactos los
archivos del [criterio conjunto congelado](FROZEN_JOINT_CRITERION.json).

El objetivo sigue siendo demostrar \(\kappa_{N,k}\to0\). Esta nota examina
una construccion concreta de los aproximantes de
[capacidades como distancias](capacidades_como_distancias.md): resolver
primero la ecuacion dual mediante una prueba polinomica mas general que
\(\omega^2P\), y despues aproximar esa prueba por \(\omega^2P_n\).

El resultado es negativo para esa construccion exacta: **ningun polinomio
simetrico produce un objetivo no nulo de la forma \(B^*(a^2p)\)**, con
\(p\) polinomico. Se demuestra para todos los grados, no mediante una
extrapolacion del calculo finito. Esto no excluye aproximantes ni soluciones
duales no polinomicas y no decide la unicidad radial.

## 1. Resultado preciso

Con \(a(z)=z(1-z)\), \(\omega=a(x)a(y)\), \(d=y-x\), sean
\[
I=(1-x)(1-y),\qquad J=xy,\qquad
\vartheta=2(J^2-I^2)
=2(x+y-1)(1-x-y+2xy).
\tag{1}
\]
El adjunto \(K^*:H_{\rm sym}\to H_{\rm alt}\) es el del operador acotado
de las notas anteriores. Se prueba:
\[
\boxed{K^*1=d,\qquad K^*\vartheta=0,}
\tag{2}
\]
\[
\boxed{\ker K^*\cap\mathbb C[x,y]_{\rm sym}
=\operatorname{span}\{\vartheta\},}
\tag{3}
\]
y, para todo polinomio unidimensional \(p\),
\[
\boxed{K^*\theta=B^*(a^2p),\quad\theta\in\mathbb C[x,y]_{\rm sym}
\quad\Longrightarrow\quad p=0,\quad\theta\in\operatorname{span}\{\vartheta\}.}
\tag{4}
\]
La igualdad (3) clasifica solo el nucleo polinomico del adjunto. No se
afirma que todo \(\ker K^*\) sea unidimensional, ni que \(K\) sea Fredholm.

## 2. Una ecuacion necesaria sin terminos de borde

Tomemos una funcion antisimetrica suave \(w\) de soporte compacto en
\((0,1)^2\), y pongamos \(g=\partial_x^2\partial_y^2w\). Sus dos marginales
ponderadas por \(1-x\) y \(x\) son cero, por integracion por partes. Por tanto
\(Bg=0\). La primitiva canonica es \(W=w/\omega\), y la descomposicion
congelada da
\[
Kg=d\,\partial_x^2\partial_y^2w+6\mathcal X(w/\omega),
\]
\[
\mathcal X=-c_x\partial_x+c_y\partial_y,\quad
c_x=x^2+2xy-2x-y+1,\quad
c_y=y^2+2xy-x-2y+1,
\quad \operatorname{div}\mathcal X=0.
\]
Si \(K^*\theta=B^*\phi\) para cualquier \(\phi\in L^2(0,1)\), entonces
\(\langle Kg,\theta\rangle=\langle Bg,\phi\rangle=0\).
Integrando sobre el soporte compacto de \(w\) resulta la ecuacion necesaria
\[
\boxed{\mathcal L\theta:=
\omega\,\partial_x^2\partial_y^2(d\theta)-6\mathcal X\theta=0.}
\tag{5}
\]
Para \(\theta\) simetrico, la expresion es antisimetrica; las pruebas
antisimetrizadas detectan toda la distribucion. No se han supuesto trazas
de una funcion \(L^2\) general. En lo que sigue \(\theta\) es polinomico y
(5) es una identidad de polinomios.

## 3. Clasificacion polinomica de la ecuacion necesaria

**Lema.** Las soluciones polinomicas simetricas de (5) son exactamente
\(\operatorname{span}\{1,\vartheta\}\).

**Demostracion.** Sea \(n>0\) el grado total maximo de una solucion, con
parte homogenea
\[
\theta_n=\sum_{i=0}^n v_i x^iy^{n-i},\qquad v_{n-i}=v_i.
\]
El operador \(\mathcal L\) aumenta el grado a lo sumo en uno. La componente
de grado \(i+j+1\) de \(\mathcal L(x^iy^j)\) es
\[
A_{ij}x^{i+1}y^j+B_{ij}x^iy^{j+1},
\]
\[
A_{ij}=-i(i+1)j(j-1)+6(i-2j),\qquad
B_{ij}=i(i-1)j(j+1)+6(2i-j).
\tag{6}
\]
Se obtiene tomando la parte superior \(x^2y^2\) de \(\omega\) y la parte
cuadratica de los coeficientes de \(\mathcal X\).

El coeficiente de \(y^{n+1}\) es \(B_{0n}v_0=-6nv_0\), luego \(v_0=0\).
Los coeficientes sucesivos satisfacen
\[
A_{k-1,n-k+1}v_{k-1}+B_{k,n-k}v_k=0,
\qquad 1\le k\le n.
\tag{7}
\]
Para \(k=1\), \(B_{1,n-1}=6(3-n)\). Para todos \(i\ge2\), \(j\ge0\),
\[
B_{ij}\ge 2j(j+1)+24-6j
=2(j-1)^2+22>0.
\tag{8}
\]
Si \(n\ne3\), (7) fuerza sucesivamente \(v_1=\cdots=v_n=0\), contradiciendo
la eleccion del grado. El unico grado positivo posible es \(n=3\).
En ese caso (7) da
\[
v_0=v_3=0,\qquad v_2=v_1,
\quad\theta_3=v_1xy(x+y).
\]

La funcion \(\vartheta\) de (1) tiene parte superior \(4xy(x+y)\) y satisface
\(\mathcal L\vartheta=0\). En efecto, \(\mathcal X\vartheta=0\) por expansion
directa; ademas \(d\vartheta\) es antisimetrico de grado cuatro, por lo que
\(\partial_x^2\partial_y^2(d\vartheta)=0\). Restar
\((v_1/4)\vartheta\) deja una solucion de grado a lo sumo dos, que por el
argumento anterior es constante. Las constantes tambien satisfacen (5).
Esto prueba el lema.

## 4. Identidades exactas del adjunto

Las formulas unidimensionales del adjunto dan
\[
L^*1=C^*1,\qquad R_+^*1=E^*1,
\]
lo que prueba \(K^*1=d\). Para comprobar el segundo modo sin omitir
terminos de borde, usamos
\[
L^*(z^2)=\frac{(1-z)^2(z+2)}6,\qquad
C^*(z^2)=\frac{z(1-z)^2}2,
\tag{9}
\]
\[
C^*((1-z)^2)=3L^*((1-z)^2),\qquad
E^*(z^2)=3R_+^*(z^2).
\tag{10}
\]
La ultima identidad procede de la anterior por reflexion. El determinante
del par de (9) es
\[
(L^*z^2)(x)(C^*z^2)(y)-(C^*z^2)(x)(L^*z^2)(y)
=\frac{d I^2}{6}.
\]
El par reflejado se anula al actuar sobre \(J^2\), por (10), y se obtiene
\[
\boxed{K^*(J^2)=d(J^2+I^2)=K^*(I^2).}
\tag{11}
\]
La segunda igualdad sigue tambien por reflexion, pues \(K^*\) cambia la
paridad. Restando se prueba \(K^*\vartheta=0\).

Para cualquier polinomio simetrico en \(\ker K^*\), (5) y el lema obligan
a \(\theta=c_0+c_1\vartheta\). Su imagen es \(c_0d\), de modo que
\(c_0=0\). Queda probado (3).

## 5. Imposibilidad del levantamiento polinomico de los momentos

Si \(K^*\theta=B^*(a^2p)\), el lema de la seccion 3 da
\(\theta=c_0+c_1\vartheta\), por tanto
\[
c_0d=B^*(a^2p).
\tag{12}
\]
Ambos miembros son polinomios. La formula de las pruebas de retorno da
\[
B^*(a^2p)(0,y)=\frac y2\int_y^1(1-z)^3p(z)\,dz.
\tag{13}
\]
Evaluar en \((x,y)=(0,1)\) fuerza \(c_0=0\). Entonces la expresion (13)
se anula identicamente; dividir por \(y\) en el interior y derivar fuerza
\((1-y)^3p(y)=0\), luego \(p=0\). Se ha probado (4).

En particular, el objetivo dual \(d_k-\lambda d_1\), con
\(d_k=B^*\psi_k\), corresponde a
\[
p(z)=(2z-1)^k-\lambda(2z-1).
\]
Para \(k\ne1\), este polinomio es no nulo para cualquier \(\lambda\).
Por tanto **no hay un levantamiento polinomico exacto para ningun momento
no trivial**, ni siquiera permitiendo la correccion temporal. Para los
momentos pares se toma \(\lambda=0\), como exige la paridad.

## 6. Consecuencia para la construccion de aproximantes

El modo \(\vartheta\) es un elemento exacto del nucleo del adjunto. No es
otro elemento del nucleo original: este ultimo vive en el subespacio
antisimetrico. Tampoco se obtiene una dimension del nucleo original a
partir de (3).

La ruta de resolver exactamente con un polinomio \(\theta\) y aproximarlo
despues por \(\omega^2P_n\) queda descartada para todos los momentos no
triviales. Siguen siendo posibles una solucion dual no polinomica o una
sucesion de pruebas sin solucion exacta limite. La no existencia de un
levantamiento polinomico no implica distancia positiva al cierre del rango.
Tampoco prueba que toda sucesion de aproximantes tenga norma divergente.

El paso pendiente conserva la forma
\[
\|F_{P_n}+12B^*r_{P_n}-d_k+\lambda_nd_1\|_2\to0.
\]
Ahora sabemos que no puede cerrarse mediante una identidad polinomica
exacta de grado fijo, incluso ampliando la clase de pruebas. No se ha
demostrado todavia este limite, ni \(c_N\to0\), ni la unicidad radial.

## 7. Verificacion reproducible

[verify_polynomial_dual_lift.py](verify_polynomial_dual_lift.py) construye el
adjunto sobre monomios incluyendo los logaritmos de ambos extremos. Comprueba
(2), (5) para los dos modos, los coeficientes de (6), la cota simbolica de
(8), y dualidad contra la formula directa de \(K\) en varios polinomios.

Como comprobacion independiente del primer objetivo par, resuelve el sistema
lineal exacto para \(K^*\theta=B^*(a^2)\), con \(\theta\) simetrico, par y
de grado total a lo sumo ocho. Hay 15 incognitas, rango 15 en la matriz y
rango 16 en la ampliada: el sistema es incompatible. Este calculo verifica
un caso finito; la exclusion para todos los grados procede de la prueba
analitica de las secciones 2-5.

```bash
python3 research_program/radial_3p1/2026-09-07/verify_polynomial_dual_lift.py --degree 8
```

Los resultados y el hash del codigo estan en
[verification_polynomial_dual_lift.json](verification_polynomial_dual_lift.json).
Los hashes de los tres archivos congelados se verifican antes y despues de
ejecutar el calculo. Estos son resultados de trabajo con verificacion interna,
sin una adjudicacion independiente de la demostracion.
