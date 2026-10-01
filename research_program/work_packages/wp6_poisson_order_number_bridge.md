# WP6 — Puente Poisson order+number

~~~text
ESTADO: POISSON_ORDER_NUMBER_BRIDGE = PROVED_IN_CURRENT_SCOPE
ALCANCE: rho conocida; poset no etiquetado junto con su cardinalidad
CANAL: Poisson no condicionado, separado de fixed-N
NORMALIZED_S1_NUMBER_SIGNAL = NONE (N es ancilar)
NORMALIZED_S1_POISSON_MIXTURE_QMD_IN_THETA = PROVED_ONE_SIDED
SCALE_ORBIT_NUMBER_SIGNAL = EXACT_AND_SUFFICIENT
NO_HORIZON_CLAIM
NO_SINGLE_REALIZATION_RECONSTRUCTION_CLAIM
NO_HAUPTVERMUTUNG_CLAIM
~~~

## 0. Resultado en una frase

El canal Poisson no hace una sola cosa. Para la familia S1 normalizada no
añade una señal de cardinalidad, pero conserva la señal de forma al mezclar
los canales fixed-\(N\); para una deformación que cambia el volumen a densidad
conocida, la cardinalidad aporta además una componente Fisher ortogonal y
detecta exactamente la escala.

Esta distinción evita identificar indebidamente:

1. observar un \(N\) aleatorio;
2. obtener información paramétrica *de* \(N\);
3. observar el orden condicionado a ese \(N\).

## 1. Factorización exacta del experimento

Sea \(g_t\) una familia de regiones lorentzianas de volumen finito
\(V_t>0\), y sea \(\rho>0\) conocida. Definimos

\[
\lambda_t:=\rho V_t.
\tag{1.1}
\]

Una aspersión de Poisson tiene
\(N\sim\operatorname{Pois}(\lambda_t)\). Condicionada a \(N=n\), sus puntos
son iid con la medida de volumen normalizada y generan una clase de poset
\(C\) con probabilidad

\[
p_{t,n,C}:=\mathbb P_t([P_n]=C\mid N=n).
\tag{1.2}
\]

Por tanto la ley conjunta order+number sobre el alfabeto numerable
\(\{(n,C):n\ge0,\ C\in\mathcal Y_n\}\) es exactamente

\[
\boxed{
Q_t(n,C)
=e^{-\lambda_t}\frac{\lambda_t^n}{n!}\,p_{t,n,C}.
}
\tag{1.3}
\]

No hay una aproximación de gran densidad en (1.3). Es la descomposición
elemental de una aspersión de Poisson por su cardinalidad.

## 2. Score e información: suma ortogonal de número y orden

Fijemos un punto \(t_0\) con \(\lambda_0:=\lambda_{t_0}>0\). Supongamos que
\(\lambda_t\) es diferenciable y que, para cada \(n\), la ley condicional
admite un score \(\dot\ell_n(C)\) centrado bajo \(p_{t_0,n}\). Al derivar el
logaritmo de (1.3),

\[
\boxed{
\dot\ell^{\mathrm{ord+num}}(n,C)
=\lambda_0'\left(\frac n{\lambda_0}-1\right)+\dot\ell_n(C).
}
\tag{2.1}
\]

Las dos sumas son ortogonales. En efecto,

\[
\mathbb E_{t_0}[\dot\ell_n(C)\mid N=n]=0,
\tag{2.2}
\]

de modo que el producto cruzado con cualquier función de \(N\) tiene esperanza
cero. Siempre que la serie condicional sea finita, la información se separa:

\[
\boxed{
I^{\mathrm{ord+num}}(t_0)
=\frac{(\lambda_0')^2}{\lambda_0}
+\sum_{n=0}^{\infty}
e^{-\lambda_0}\frac{\lambda_0^n}{n!}\,I_n^{[P]}(t_0).
}
\tag{2.3}
\]

El primer término es información de **número**; el segundo, información media
de **orden dado el número**. Ninguno debe atribuirse al otro.

La misma identidad vale con derivadas por la derecha y scores laterales si
\(t_0\) es una frontera, una vez probada la QMD unilateral y la sumabilidad
correspondientes.

## 3. Aplicación a S1: el número es ancilar

La familia S1 del diamante se definió por

\[
g_\varepsilon
=\frac{e^{2\varepsilon\psi}}{Z(\varepsilon)}\,g_0,
\qquad
Z(\varepsilon)
=\int_D e^{2\varepsilon\psi}\,d\mu_0.
\tag{3.1}
\]

En dimensión \(1+1\), el factor conforme de (3.1) es también el factor de la
medida de volumen. La división por \(Z(\varepsilon)\) da

\[
V_\varepsilon=V_0
\qquad\text{y por tanto}\qquad
\lambda_\varepsilon=\rho V_0
\tag{3.2}
\]

exactamente para todo \(\varepsilon\). En esta familia,

\[
\boxed{
\lambda_\varepsilon'=0:
\quad N\text{ es ancilar para }\varepsilon.
}
\tag{3.3}
\]

Así, order+number no recupera aquí el signo ni añade información de volumen.
Su única función es revelar qué experimento condicional fixed-\(N\) se realizó.

## 4. QMD unilateral de la mezcla Poisson en
\(\theta=\varepsilon^2\)

Tomemos el witness antisimétrico

\[
\psi=e_1\otimes e_2-e_2\otimes e_1
\tag{4.1}
\]

y \(\theta=\varepsilon^2\ge0\). Para cada \(n\) fijo, el Teorema 20 de la hoja
de ruta prueba

\[
p_{\theta,n,C}
=p_{0,n,C}
+a_{n,C}\theta+O_{n,C}(\theta^2),
\qquad
\dot\ell^{(+)}_n(C)
=\frac{a_{n,C}}{p_{0,n,C}}
=\frac{p_{n,C}''(0)}{2p_{0,n,C}}.
\tag{4.2}
\]

El paso nuevo es justificar la suma sobre todos los \(n\).

### 4.1 Cota sumable del score

Sea \(M:=\|\psi\|_\infty<\infty\) y
\(\sigma^2:=\int_D\psi^2\,d\mu_0\). Para una permutación \(\pi\),

\[
T_\pi=\sum_{i=1}^n\psi(U_{(i)},V_{(\pi(i))}),
\qquad |T_\pi|\le nM.
\tag{4.3}
\]

La fórmula exacta de segundo orden da

\[
\frac{p_\pi''(0)}{p_\pi(0)}
=4\bigl(\mathbb E T_\pi^2-n\sigma^2\bigr).
\tag{4.4}
\]

El cociente correspondiente a una clase \(C\) es el promedio de (4.4) sobre
su fibra. En consecuencia,

\[
\boxed{
\left|\dot\ell_n^{(+)}(C)\right|
\le 2\bigl(n^2M^2+n\sigma^2\bigr).
}
\tag{4.5}
\]

Por tanto

\[
I_{n,\theta}^{(+)}
\le4\bigl(n^2M^2+n\sigma^2\bigr)^2=O(n^4).
\tag{4.6}
\]

Todo momento polinómico de una variable Poisson es finito, luego

\[
\sum_{n\ge0}e^{-\lambda}\frac{\lambda^n}{n!}
I_{n,\theta}^{(+)}<\infty.
\tag{4.7}
\]

### 4.2 Intercambio del límite QMD y la mezcla

No basta citar (4.7) sin controlar el resto. Para hacerlo, escribimos la razón
de probabilidad condicional de una permutación:

\[
R_{\pi,n}(\varepsilon)
:=\frac{p_{\pi,n}(\varepsilon)}{p_{\pi,n}(0)}
=\frac{\mathbb E e^{2\varepsilon T_\pi}}
       {Z(\varepsilon)^n}.
\tag{4.8}
\]

De \(|T_\pi|\le nM\) y
\(e^{-2M|\varepsilon|}\le Z(\varepsilon)\le e^{2M|\varepsilon|}\) se obtiene

\[
e^{-4nM|\varepsilon|}
\le R_{\pi,n}(\varepsilon)
\le e^{4nM|\varepsilon|}.
\tag{4.9}
\]

Las derivadas de (4.8) hasta orden cuatro están acotadas, para
\(|\varepsilon|\le\delta\), por un polinomio en \(n\) multiplicado por
\(e^{c n\delta}\), con \(c\) dependiente sólo de \(M\). La misma cota vale para
el promedio sobre cualquier fibra. La paridad elimina las potencias impares,
así que el resto en la expansión de la raíz de la razón, dividido por
\(\theta\), queda dominado por

\[
\operatorname{poly}(n)e^{c n\delta}.
\tag{4.10}
\]

Su cuadrado es sumable contra
\(e^{-\lambda}\lambda^n/n!\) para todo \(\delta<\infty\), porque la ley de
Poisson tiene momentos exponenciales de todos los órdenes. Para cada \(n,C\)
el cociente tiende a cero por (4.2); convergencia dominada permite sumar.
Resulta

\[
\sum_{n,C}Q_0(n,C)
\left[
\sqrt{\frac{Q_\theta(n,C)}{Q_0(n,C)}}-1
-\frac{\theta}{2}\dot\ell_n^{(+)}(C)
\right]^2
=o(\theta^2),
\qquad \theta\downarrow0.
\tag{4.11}
\]

Esto prueba QMD unilateral de la mezcla Poisson order+number.

### 4.3 Información y Hellinger

Como \(\lambda\) es constante en S1, (2.3) se reduce a

\[
\boxed{
I_{\mathrm{Pois},\theta}^{(+)}
=\sum_{n=0}^{\infty}
e^{-\lambda}\frac{\lambda^n}{n!}\,
I_{n,\theta}^{(+)}
<\infty.
}
\tag{4.12}
\]

El término \(n=2\) ya da la cota estricta

\[
\boxed{
I_{\mathrm{Pois},\theta}^{(+)}
\ge e^{-\lambda}\frac{\lambda^2}{2}\frac{64}{25}
=\frac{32}{25}e^{-\lambda}\lambda^2>0.
}
\tag{4.13}
\]

Por tanto una aspersión Poisson de intensidad media positiva conserva la
visibilidad local de \(|\varepsilon|\), aunque con probabilidad positiva
produzca cardinalidades \(0\) o \(1\), que no pueden distinguir tipos de orden.
Con la convención Hellinger del repositorio,

\[
\boxed{
H^2(Q_\theta,Q_0)
=\frac14I_{\mathrm{Pois},\theta}^{(+)}\theta^2+o(\theta^2).
}
\tag{4.14}
\]

## 5. Órbita de escala: el número sí lleva toda la señal nueva

Consideremos ahora una familia para la que las leyes condicionadas del orden
son idénticas,

\[
p_{t,n,C}=p_{0,n,C}\quad\forall n,C,
\tag{5.1}
\]

pero el volumen, y por tanto \(\lambda_t=\rho V_t\), cambia. Éste es el caso
de la órbita de co-escalado que era invisible en el canal fixed-\(N\). De
(1.3), la razón de verosimilitudes depende sólo de \(N\): la cardinalidad es
estadístico suficiente para \(t\) dentro de esta subfamilia.

Para dos medias \(\lambda,\mu>0\), la afinidad de Bhattacharyya es

\[
\sum_{n\ge0}\sqrt{
e^{-\lambda}\frac{\lambda^n}{n!}
e^{-\mu}\frac{\mu^n}{n!}}
=\exp\!\left[-\frac12(\sqrt\lambda-\sqrt\mu)^2\right].
\tag{5.2}
\]

Luego, en la convención \(H^2=\sum(\sqrt p-\sqrt q)^2\),

\[
\boxed{
H^2(\operatorname{Pois}(\lambda),\operatorname{Pois}(\mu))
=2\left\{
1-\exp\!\left[-\frac12(\sqrt\lambda-\sqrt\mu)^2\right]
\right\}.
}
\tag{5.3}
\]

Es positiva si y sólo si \(\lambda\ne\mu\). Localmente,

\[
\boxed{
I^{\mathrm{number}}(t_0)
=\frac{(\lambda_{t_0}')^2}{\lambda_{t_0}}.
}
\tag{5.4}
\]

Si una dilatación \(s\) en dimensión \(d\) da
\(V_s=s^dV_0\) y usamos \(\alpha=\log s\), entonces
\(\lambda_\alpha=\lambda_0e^{d\alpha}\) y

\[
\boxed{
I_\alpha^{\mathrm{number}}(0)=d^2\lambda_0.
}
\tag{5.5}
\]

Ésta es la restauración precisa de la escala por “Order + Number” a densidad
conocida. No depende de un observable combinatorio sofisticado: en la órbita
de escala, la parte nueva de la información está ya en \(N\).

## 6. Techo de claims

~~~text
POISSON_ORDER_PLUS_NUMBER_FACTORIZATION = PROVED_EXACT
POISSON_ORDER_NUMBER_BRIDGE = PROVED_IN_CURRENT_SCOPE
NUMBER_PLUS_CONDITIONAL_ORDER_FISHER_SPLITTING = PROVED_ORTHOGONAL

NORMALIZED_S1:
  TOTAL_VOLUME = CONSTANT_EXACTLY
  N_ANCILLARY_FOR_EPSILON_AND_THETA = YES
  POISSON_MIXTURE_ONE_SIDED_QMD_IN_THETA = PROVED
  I_POIS_THETA = E_POISSON[I_N_THETA] < infinity
  I_POIS_THETA >= (32/25) exp(-lambda) lambda^2 > 0

SCALE_ORBIT_WITH_KNOWN_RHO:
  CONDITIONAL_ORDER_LAW = UNCHANGED
  N_IS_SUFFICIENT_WITHIN_ORBIT = YES
  NUMBER_SUFFICIENT_FOR_SCALE = EXACT
  HELLINGER_POISSON_SEPARATION = EXACT
  NUMBER_FISHER = (lambda')^2 / lambda

UNIFORM_FIXED_N_QMD = NOT_NEEDED_FOR_THIS_BOUNDED_WITNESS
UNKNOWN_RHO_SCALE_IDENTIFIABILITY = NOT_CLAIMED
SINGLE_REALIZATION_RECONSTRUCTION = NOT_CLAIMED
HAUPTVERMUTUNG = NOT_CLAIMED
LOCAL_METRIC_RECONSTRUCTION = NOT_CLAIMED
HORIZON_LOCALIZATION = NOT_CLAIMED
~~~
