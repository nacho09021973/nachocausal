# F1 — Identidad de flujo para el Fisher del poset en la caja EF (cualquier dimensión)

```text
ESTADO: LEMMA_S_PROVED; LEMMA_F_PROVED (hipótesis de regularidad enunciadas); REDUCTION_STATED
FECHA: 2026-10-16
ENTRADA: RELEVO.md (siguiente paso: probar I_n <= C n por la identidad de flujo)
NATURALEZA: análisis; sin simulación, sin semillas, sello intacto
ORDER_ONLY_FISHER_LINEAR_3P1 (I_n <= C n) = NOT_PROVED
FLUX_IDENTITY = PROVED (Lema F)
FISHER_BOUNDARY_TRACE_REPRESENTATION = PROVED (Corolario F2)
POINTWISE_TAU_FREE_REPRESENTATION_3P1 = OBSTRUCTED_CONDITIONAL_ON_RIGIDITY [UNVERIFIED citation]
BOUNDARY_CV_EXPERIMENT_SCOPE = LOWER_BOUND_ON_FOUR_COARSE_STATISTICS (no dice nada de I_n)
NO_HORIZON_OBJECT_CLAIM
REVIEW = NONE_YET
```

## 0. Procedencia

Escrito por Claude (Opus 5.5) el 2026-10-16, a petición del PI ("Prueba I_n ≤ Cn").
No he tenido acceso a `~/herramientas/CREATE/runs/2026-10-16-tasa-3p1/` (ruta Opus 1), así
que **no sé si la "identidad de flujo" de esa ruta es la misma que la de aquí**. Lo de abajo
se deriva desde cero. Sin revisión de otra familia ni lectura humana.

**Resultado en una línea.** No he probado \(I_n\le Cn\) en 3+1D. Lo que sí queda probado es
que, en Schwarzschild, el parámetro \(\tau=2M\) entra en la ley del poset **solo a través de
una frontera móvil** (Lema S), y que el Fisher del poset es exactamente \(n^2\) veces la
varianza de una traza de frontera de la posterior de un elemento (Lema F, Corolario F2).
\(I_n\le Cn\) equivale a que esa traza tenga varianza \(O(1/n)\). Ese es el enunciado que
queda abierto.

## 1. Modelo

Caja EF fija \(B=[0,T]\times[r_a,r_b]\times S^{d-1}\), \(0<r_a\), en Schwarzschild de dimensión
\(d+1\) con la métrica de `M1_metric_comparison_and_upper_rate.md` §1. Condicionado a
\(N=n\), \(n\) puntos iid uniformes respecto a \(\mu_\tau=\sqrt{-g_\tau}\,dv\,dr\,d\Omega\)
(por M1, \(\sqrt{-g}\) no depende de \(M\)). La relación es la causalidad ambiente en
\(r>0\). \(C\) es la clase de isomorfismo del poset sin etiquetas, \(\pi_c(\tau)=P_\tau(C=c)\)
e \(I_n(\tau)=\sum_c\pi_c'^2/\pi_c\).

## 2. Lema S (la masa es una escala)

Sea \(h_\lambda(v,r,\Omega)=(\lambda v,\lambda r,\Omega)\). Entonces
\(h_\lambda^*g_{\lambda M}=\lambda^2g_M\).

*Prueba.* \(1-2\lambda M/(\lambda r)=1-2M/r\), \(d(\lambda v)^2=\lambda^2dv^2\),
\(2\,d(\lambda v)\,d(\lambda r)=2\lambda^2dv\,dr\) y \((\lambda r)^2d\Omega^2=\lambda^2r^2d\Omega^2\). \(\square\)

Un factor conforme constante conserva la relación causal y multiplica el volumen por una
constante \(\lambda^{d+1}\), así que conserva la ley del sprinkling uniforme condicionado a
\(N=n\). Tomando \(\lambda=1/\tau\):

> **La ley de \(C\) bajo \((B,g_\tau)\) es la ley de \(C\) para un sprinkling uniforme en
> \(D_\tau:=h_{1/\tau}(B)\) dentro de la geometría **fija** \(g_{\tau=1}\).**

El parámetro solo mueve el dominio \(D_\tau=[0,T/\tau]\times[r_a/\tau,r_b/\tau]\times S^{d-1}\).
La relación sobre el espacio de puntos ya no depende de \(\tau\), pero el **soporte sí**: es la
misma patología de familia uniforme con soporte móvil que la Observación 3.4 del manuscrito
señala para la ley de un punto. Vale en cualquier \(d\), también en 1+1D.

## 3. Lema F (identidad de flujo)

Sea \(\mu=\mu_{\tau=1}\), \(|D|=\mu(D_\tau)\) y \(h_c(y)=P(C=c\mid Y_1=y)\), es decir, la
probabilidad de la clase \(c\) cuando un punto está fijo en \(y\) y los otros \(n-1\) son
uniformes en \(D_\tau\). Sea \(\beta_\tau\) la medida con signo sobre \(\partial D_\tau\) dada por
la velocidad normal de la frontera:
\(\frac{d}{d\tau}\int_{D_\tau}F\,d\mu=\int_{\partial D_\tau}F\,d\beta_\tau\) para \(F\) continua
(transporte de Reynolds). En particular \(\beta_\tau(\partial D_\tau)=\frac{d}{d\tau}|D|\).

**Lema F.** Supóngase que \(h_c\) es continua en un entorno de \(\partial D_\tau\). Entonces

\[
\pi_c'(\tau)=\frac{n}{|D|}\int_{\partial D_\tau}\bigl(h_c(y)-\pi_c\bigr)\,d\beta_\tau(y).
\tag{F}
\]

*Prueba.* \(\pi_c=|D|^{-n}\int_{D_\tau^n}1_c\,d\mu^{\otimes n}\). Al derivar el dominio
producto, cada uno de los \(n\) factores aporta, por intercambiabilidad, el mismo término
\(|D|^{-1}\int_{\partial D}h_c\,d\beta\). La normalización aporta \(-n\pi_c|D|'/|D|\), y
\(|D|'=\int_{\partial D}d\beta\). \(\square\)

**Sobre la hipótesis.** Con los demás puntos fijos, \(1_c\) cambia como función de \(y\) solo
cuando \(y\) cruza un cono de luz de otro punto o el lugar donde se anula una relación, que son
conjuntos \(\mu\)-nulos. Por convergencia dominada, \(h_c\) es continua. No he escrito el
detalle en las esquinas de la caja (la frontera es solo \(C^\infty\) a trozos). La fórmula
de Reynolds vale para dominios lipschitzianos con velocidad suave, pero la cita concreta
no está comprobada.

**Comprobación de signo (solo de control, no es evidencia del resultado).** En
\(D_s=[0,1]\times[0,s]\) de Minkowski 1+1 con \(n=2\), la derivada por diferencias finitas de
\(P(\text{relacionados})\) y el lado derecho de (F) coincidieron al 1 % (error de Monte
Carlo). El script es de borrador y no está commiteado, así que no cito los números.

## 4. Corolario F2 (el Fisher como traza de frontera)

Sea \(\ell_c(y)=h_c(y)/\pi_c\): es la densidad, respecto a la uniforme, de la posición de un
elemento elegido al azar condicionada a \(C=c\). Por (F),

\[
I_n(\tau)=n^2\,E_\tau\bigl[T(C)^2\bigr],\qquad
T(c):=\frac{1}{|D|}\int_{\partial D_\tau}\bigl(\ell_c(y)-1\bigr)\,d\beta_\tau(y),
\tag{F2}
\]

con \(E_\tau T(C)=0\), porque \(\sum_c\pi_c\ell_c(y)=1\).

**Por tanto \(I_n\le Cn\iff E_\tau T(C)^2\le C/n\)**, uniformemente en \(K\). Es decir: la traza
en la frontera, ponderada por la velocidad de la frontera, de la posterior de un elemento
típico tiene que fluctuar entre clases solo a escala \(n^{-1/2}\).

**Por qué la cota trivial no sirve.** Si \(\psi_\varepsilon\) es una capa de grosor
\(\varepsilon\) que aproxima \(\beta\), se tiene
\(T(C)=\lim_\varepsilon E[\bar\psi_\varepsilon\mid C]-\text{media}\), con
\(\bar\psi_\varepsilon=\frac1n\sum_k\psi_\varepsilon(Y_k)\). La desigualdad
\(\operatorname{Var}E[\cdot\mid C]\le\operatorname{Var}(\cdot)\) da
\(\operatorname{Var}T\lesssim 1/(n\varepsilon)\to\infty\). Así que una cota lineal tiene que usar
que **el poset no resuelve cuántos puntos hay en capas finas junto a la frontera**. Ese es el
contenido físico de la pregunta.

## 5. Por qué el truco de 1+1D no se traslada (obstrucción, condicional)

El Teorema A de `wp6_uniform_n_horizon_quotient.md` usó una representación
\(\Pi_n=\varphi((\varepsilon_i,D_i,V_i))\) con \(\varphi\) independiente de \(\tau\) y etiquetas de
**soporte fijo** y ley regular. Si hubiera algo análogo en 3+1D (un embebimiento de orden
punto a punto \((B,\prec_\tau)\to(Y_0,\prec_Y)\) con imagen \(Y_0\) fija), se tendrían
isomorfismos de orden \((B,\prec_\tau)\cong(B,\prec_{\tau'})\) para todo \(\tau,\tau'\in K\). Por
rigidez (Zeeman para Minkowski y Levichev en el caso general; véase la auditoría de
prioridad del 16 de octubre), esos isomorfismos serían conformes. Las únicas
aplicaciones conformes entre regiones de Schwarzschild con masas distintas serían las
homotecias del Lema S compuestas con isometrías, y estas no llevan \(B\) en sí misma
porque \(r_a>0\).

`[UNVERIFIED]`: el enunciado de rigidez para regiones abiertas acotadas con frontera
(no espaciotiempos completos), y que el grupo conforme local de Schwarzschild se reduce
a homotecias e isometrías, no están comprobados en fuente primaria. Las fuentes (Zeeman
1964, Levichev) no están descargadas.

En 1+1D, en cambio, el grupo conforme es de dimensión infinita, y eso es exactamente lo
que permitió fijar el soporte. Es coherente con lo que dice el RELEVO: la diferencia
entre 2D y 3+1D es el grupo de automorfismos.

## 6. Coherencia con 1+1D

El Lema F vale también en 1+1D. Combinado con el Teorema A (\(I_n^\Pi\le nJ\)), da en la caja
EF de 1+1D \(E\,T(C)^2\le J/n\). Por tanto la cancelación que se busca en 3+1D **existe** en
1+1D, y allí la impone la libertad conforme. No conozco un argumento que la imponga sin esa
libertad.

## 7. Qué dice y qué no dice el experimento LINEAR_CONSISTENT

`dev/explore_information_growth_boundary_cv.py` estima \(\tilde I_n=d^\top\Sigma^{-1}d\) sobre
**cuatro estadísticos gruesos**: la fracción de pares relacionados, \(n_{\max}\), \(n_{\min}\) y
la altura. Eso es una **cota inferior** de \(I_n\) restringida a esos estadísticos. Además,
el parámetro del juguete es la razón de aspecto \(a\) de una caja de Minkowski, no la masa;
también es una familia de frontera móvil.

Que \(\tilde I_n\) crezca linealmente dice que **esos cuatro** no ganan información
superlineal. No dice nada sobre el estadístico que haría falta según el §4: una medida
fina de la ocupación de capas junto a la frontera. La lectura "evidencia de que la tasa sigue
siendo \(n^{-1/2}\)" del RELEVO hay que restringirla así: evidencia de que estos
estadísticos no la mejoran.

## 8. Lo que falta

1. **El enunciado abierto**: \(E_\tau T(C)^2\le C/n\) en 3+1D, uniformemente en \(K\). Tampoco
   tengo una prueba de lo contrario.
2. El detalle de Reynolds en las esquinas de la caja y la continuidad de \(h_c\) en la
   frontera.
3. La obstrucción del §5 en fuente primaria.
4. Revisión ciega de otra familia y lectura del PI.
