# WP7 — Extensión dimensional de la cadena plantada

```text
ESTADO: BORRADOR MATEMÁTICO v0.2 / D3--D4 PROVED_MODULO_SOURCE_SCOPE
FECHA: 2026-08-11
DIMENSIÓN: d es la dimensión del espaciotiempo; d=3 significa 2+1 y d=4 significa 3+1
ALCANCE: lectura regional de Madsen + norma de curvatura bajo una de las dos convenciones estándar
NOVEDAD: TARGETED_AUDIT_NO_SUBSUMING_PRECEDENT / NO_ABSOLUTE_PRIORITY
```

## 0. Resultado

La construcción de WP7 no es específica de `1+1`. La misma perturbación por una cadena
timelike de masa evanescente produce, para cada dimensión fija \(d\ge2\), configuraciones
que preservan exactamente el orden causal, satisfacen la tolerancia cuantitativa F2 de
Madsen con una constante fija y violan F3 por un margen macroscópico.

> **Teorema (extensión dimensional, bajo el mismo alcance regional).** Fije
> \(d\ge2\), \(\ell>0\) y el parche planar de de Sitter
>
> \[
> M_{\ell}^{d}=\{(\eta,\mathbf x):\eta<0,\ \mathbf x\in\mathbb R^{d-1}\},
> \qquad
> g=\frac{\ell^2}{\eta^2}
> \left(-d\eta^2+d\mathbf x^2\right).
> \]
>
> Adopte la lectura regional de la Remark 5.4 de Madsen: se fija una región
> precompacta \(K\Subset M_\ell^d\), se reemplaza \(V_M\) por \(V_K\), y F2 se
> exige para todos los diamantes causales completos, admisibles y profundos contenidos
> en \(K\). Bajo cualquiera de las dos normas estándar de curvatura auditadas en el
> contrato principal, existen constantes fijas \(c_*,K_d,A,\varepsilon>0\), una región
> fija \(K\) y, para toda densidad suficientemente grande \(\rho\), un conjunto finito
> \(P_\rho\subset K\) tal que:
>
> 1. la inclusión con el orden causal inducido satisface F1 exactamente;
> 2. \(P_\rho\) satisface F2 con la misma constante \(K_d\), independiente de \(\rho\);
> 3. un par plantado \(x_\rho\prec y_\rho\) viola la desigualdad F3 completa por un
>    margen positivo independiente de \(\rho\).
>
> En particular, el resultado vale en \(d=3\) (`2+1`) y \(d=4\) (`3+1`).

El sufijo de alcance es exactamente el de `P5.2` en el contrato principal: Madsen no
define la norma de \(\operatorname{Rm}[g]\) y su Remark 5.4 no reescribe literalmente
todos los cuantificadores regionales de la Def. 2.6. No aparece una nueva reserva
matemática al aumentar la dimensión.

## 1. Geometría de fondo en dimensión arbitraria

Ponga

\[
t=-\ell\log(-\eta/\ell),
\qquad
g=-dt^2+e^{2t/\ell}d\mathbf x^2,
\qquad
T=\partial_t.
\]

El campo \(T\) es timelike unitario y procede de un tiempo de Cauchy. Su auxiliar es

\[
h_T=dt^2+e^{2t/\ell}d\mathbf x^2
=\frac{\ell^2}{y^2}\left(dy^2+d\mathbf x^2\right),
\qquad y=-\eta>0,
\]

es decir, el espacio hiperbólico \(\mathbb H^d_\ell\). Por tanto \(h_T\) es completo,
simplemente conexo y tiene radio de inyectividad infinito. El parche planar es
globalmente hiperbólico: sus conos son los del semiespacio de Minkowski \(\eta<0\),
cada nivel de \(\eta\) es de Cauchy y cada diamante está cerrado, acotado y separado de
\(\eta=0\).

De Sitter tiene curvatura seccional constante \(+1/\ell^2\),

\[
R_{abcd}=\ell^{-2}(g_{ac}g_{bd}-g_{ad}g_{bc}).
\]

En una base \(g\)-ortonormal adaptada a cualquier campo timelike unitario \(S\), que es
también \(h_S\)-ortonormal, se obtiene

\[
|\operatorname{Rm}[g]|_{\mathrm{HS},h_S}^2
=\frac{2d(d-1)}{\ell^4}.
\]

Así, para la norma Hilbert--Schmidt,

\[
\lambda=[2d(d-1)]^{-1/4}\ell,
\]

y para la norma de operador o cota seccional, \(\lambda=\ell\). El campo \(T\) alcanza
el supremo de la Def. 2.6 porque \(\operatorname{inj}(M,h_T)=\infty\). En ambos casos

\[
\lambda=c_{\mathrm{norm},d}\ell,
\qquad 0<c_{\mathrm{norm},d}<\infty.
\]

## 2. Volumen de un diamante y cota uniforme de traza

Sea \(D(a,b)=J^+(a)\cap J^-(b)\) un diamante timelike completo de altura propia
\(\tau=\tau_g(a,b)\). En la completación conforme, el parche planar es el futuro causal
de un punto de la frontera pasada de de Sitter. Es, por tanto, un conjunto futuro: si
\(a\preceq z\preceq b\) y \(a\) pertenece al parche, también pertenece \(z\). Esto
prueba que el parche es causalmente convexo. En consecuencia, el diamante calculado
dentro del parche coincide con el diamante completo de de Sitter entre sus puntas. Como
el grupo de isometrías de de Sitter actúa transitivamente sobre los pares timelike
ordenados con separación propia fija, su volumen sólo depende de \(\tau\). Es suficiente
tomar puntas comóviles

\[
(\eta_-,\mathbf0)=(-\ell e^s,\mathbf0),
\qquad
(\eta_+,\mathbf0)=(-\ell e^{-s},\mathbf0),
\qquad
s=\frac{\tau}{2\ell}.
\]

Si \(\omega_{d-1}\) es el volumen de la bola unidad de \(\mathbb R^{d-1}\), una
integración por rebanadas da

\[
\operatorname{Vol}_g(D)=\omega_{d-1}\ell^d I_d(s),
\tag{HD-1}
\]

donde, con \(a=e^{-s}\), \(b=e^s\) y \(m=(a+b)/2=\cosh s\),

\[
I_d(s)=
\int_a^m\frac{(y-a)^{d-1}}{y^d}\,dy
+\int_m^b\frac{(b-y)^{d-1}}{y^d}\,dy.
\tag{HD-2}
\]

Para las tres dimensiones relevantes,

\[
\begin{aligned}
I_2(s)&=2\log\cosh s,\\
I_3(s)&=2(s-\tanh s),\\
I_4(s)&=2\log\cosh s-\tanh^2s.
\end{aligned}
\tag{HD-3}
\]

En particular,

\[
\begin{aligned}
V_2(\tau)&=4\ell^2\log\cosh s,\\
V_3(\tau)&=2\pi\ell^3(s-\tanh s),\\
V_4(\tau)&=\frac{4\pi}{3}\ell^4
\left(2\log\cosh s-\tanh^2s\right).
\end{aligned}
\tag{HD-4}
\]

Estas expresiones tienen los límites planos correctos

\[
V_d(\tau)=\zeta_d\tau^d(1+O(\tau^2/\ell^2)),
\qquad
\zeta_d=\frac{\omega_{d-1}}{d\,2^{d-1}}.
\tag{HD-5}
\]

Fije

\[
\beta_d:=\frac{c_*\lambda}{2\ell}>0,
\qquad
\kappa_{d,\beta}:=
\min_{0\le s\le\beta_d}
\frac{\omega_{d-1}I_d(s)}{(2s)^d},
\tag{HD-6}
\]

interpretando el valor en \(s=0\) por continuidad como \(\zeta_d\). El integrando de
(HD-2) es positivo para \(s>0\), de modo que la función de (HD-6) es continua y
estrictamente positiva en el compacto indicado. Por consiguiente

\[
\boxed{
\operatorname{Vol}_g(D)\ge
\kappa_{d,\beta}\,\tau(D)^d
}
\qquad
\text{para }0<\tau(D)\le c_*\lambda.
\tag{HD-7}
\]

Considere ahora la geodésica comóvil

\[
\gamma_0(u)=(u,\mathbf0),
\qquad -\tau_0/2\le u\le\tau_0/2.
\]

Cada subsegmento es maximizante, porque para toda curva causal parametrizada por \(t\),

\[
L_g\le\int dt.
\]

La intersección de \(\gamma_0\) con un diamante causalmente convexo es un intervalo.
Si sus extremos son \(r\preceq s\), la desigualdad triangular inversa da

\[
\operatorname{len}_g(\gamma_0\cap D)
=\tau_g(r,s)\le\tau_g(a,b)=\tau(D).
\]

Junto con (HD-7),

\[
\boxed{
\operatorname{len}_g(\gamma_0\cap D)
\le\kappa_{d,\beta}^{-1/d}
\operatorname{Vol}_g(D)^{1/d}.
}
\tag{HD-8}
\]

Este es el único lema geométrico que sustituye a la identidad
`diamante = rectángulo` del caso `1+1`.

## 3. Región, fondo y cadena plantada

Fije \(0<\varepsilon<c_*\), \(\tau_0=\varepsilon\lambda\), y tome como puntas

\[
p=(-\tau_0/2,\mathbf0),
\qquad
q=(\tau_0/2,\mathbf0).
\]

El diamante testigo \(D_0=D(p,q)\) es compacto. Como \(h_T=\mathbb H^d_\ell\), una
bola hiperbólica abierta \(K=B_R^{h_T}(0)\) con radio suficientemente grande tiene
clausura compacta, volumen positivo y finito, contiene \(D_0\) y satisface

\[
d_{h_T}(D_0,\partial K)>c_*\lambda.
\]

Escriba

\[
\mathcal N_\rho:=\rho V_K,
\qquad
\tau_{\min}(\rho)
=c_*^{-1}\rho^{-1/d}(\log\mathcal N_\rho)^{2/d}.
\tag{HD-9}
\]

Como \(\tau_{\min}(\rho)\to0\), el rango
\([\tau_{\min},c_*\lambda]\) es no vacío y contiene \(\tau_0\) para toda \(\rho\)
suficientemente grande. También se satisface finalmente la jerarquía de escala del Lema
5.2 de Madsen,

\[
\rho\lambda^d\ge c_*^{-2d}(\log\mathcal N_\rho)^2.
\]

Bajo la lectura regional, ese lema permite escoger una realización Poisson de fondo
\(\Pi_\rho\subset K\) que satisface F1--F2 con una constante fija
\(K_{\mathrm{bg}}\). Fije \(K_d>K_{\mathrm{bg}}\), denote por \(C_d\) la constante
de F3 y elija

\[
A>1+C_d\varepsilon^2.
\tag{HD-10}
\]

Sobre \(\gamma_0\), incluidos \(p,q\), plante

\[
k_\rho=
\left\lceil A(m_d\rho)^{1/d}\tau_0\right\rceil
\tag{HD-11}
\]

puntos equiespaciados, llame \(\Gamma_\rho\) al conjunto resultante y defina

\[
P_\rho=\Pi_\rho\cup\Gamma_\rho
\]

con el orden causal inducido. Casi seguramente el fondo no toca \(\gamma_0\), así que no
hay colisiones; F1 es exacta.

## 4. F2 en dimensión \(d\)

La discrepancia de una rejilla unidimensional sobre cualquier intervalo y (HD-8) dan,
para cada diamante F2-admisible \(D\),

\[
\begin{aligned}
\#(\Gamma_\rho\cap D)
&\le A(m_d\rho)^{1/d}
\operatorname{len}_g(\gamma_0\cap D)+2\\
&\le A m_d^{1/d}\kappa_{d,\beta}^{-1/d}
(\rho\operatorname{Vol}_gD)^{1/d}+2.
\end{aligned}
\tag{HD-12}
\]

Ponga \(B_d=A m_d^{1/d}\kappa_{d,\beta}^{-1/d}\). Sumando F2 para el fondo,

\[
\frac{|\#(P_\rho\cap D)-\rho\operatorname{Vol}_gD|}
{\sqrt{\rho\operatorname{Vol}_gD\log\mathcal N_\rho}}
\le K_{\mathrm{bg}}
+\frac{B_d(\rho\operatorname{Vol}_gD)^{1/d-1/2}}
{\sqrt{\log\mathcal N_\rho}}
+\frac{2}{\sqrt{\rho\operatorname{Vol}_gD\log\mathcal N_\rho}}.
\tag{HD-13}
\]

Por (HD-7) y (HD-9), todo diamante admisible cumple

\[
\rho\operatorname{Vol}_gD
\ge\kappa_{d,\beta}c_*^{-d}(\log\mathcal N_\rho)^2.
\tag{HD-14}
\]

Como \(1/d-1/2\le0\), (HD-13)--(HD-14) acotan el exceso sobre el fondo por

\[
\Xi_{A,d}(\rho):=
B_d(\kappa_{d,\beta}c_*^{-d})^{1/d-1/2}
(\log\mathcal N_\rho)^{2/d-3/2}
+\frac{2c_*^{d/2}}{\sqrt{\kappa_{d,\beta}}}
(\log\mathcal N_\rho)^{-3/2}.
\tag{HD-15}
\]

Para todo \(d\ge2\), \(2/d-3/2<0\), luego

\[
\Xi_{A,d}(\rho)\longrightarrow0.
\tag{HD-16}
\]

Tomando \(\rho\) suficientemente grande para que
\(\Xi_{A,d}(\rho)\le K_d-K_{\mathrm{bg}}\), queda probada F2 con la misma constante
final fija \(K_d\).

Las tasas del término principal son

| Espaciotiempo | \(d\) | coste plantado normalizado en F2 |
|---|---:|---:|
| `1+1` | 2 | \(O((\log\mathcal N_\rho)^{-1/2})\) |
| `2+1` | 3 | \(O((\log\mathcal N_\rho)^{-5/6})\) |
| `3+1` | 4 | \(O((\log\mathcal N_\rho)^{-1})\) |

La cadena resulta, por tanto, **más invisible para F2** al aumentar la dimensión.

## 5. Violación de F3

Sean \(x_\rho,y_\rho\) los extremos plantados. Según la convención de longitud de
cadena se pierde a lo sumo un término \(O(1)\), por lo que

\[
\frac{\ell_{P_\rho}(x_\rho,y_\rho)}{(m_d\rho)^{1/d}}-\tau_0
\ge(A-1)\tau_0-o(1).
\tag{HD-17}
\]

Para el mismo par, F3 sólo permite

\[
C_d\left(
\varepsilon^2+
\frac{\log^{3/2}\mathcal N_\rho}
{\mathcal N_\rho^{1/(2d)}}
\right)\tau_0.
\tag{HD-18}
\]

Por (HD-10),

\[
\mu_d:=A-1-C_d\varepsilon^2>0,
\]

y el segundo término de (HD-18) tiende a cero. Para toda densidad suficientemente
grande, (HD-17) supera (HD-18), por ejemplo, en al menos
\(\mu_d\tau_0/3\). Esta es una violación de la desigualdad F3 completa por margen
constante, no sólo de su tasa.

## 6. Auditoría de obligaciones

| Obligación | \(d=3\) | \(d=4\) | Evidencia |
|---|---|---|---|
| hiperbolicidad global y auxiliar completo | `PROVED` | `PROVED` | §1 |
| \(0<\lambda<\infty\) | `PASS_WITH_NORM_SCOPE` | `PASS_WITH_NORM_SCOPE` | §1 |
| volumen \(V_d(\tau)\) y cota \(V\ge\kappa\tau^d\) | `PROVED` | `PROVED` | (HD-1)--(HD-7) |
| cota uniforme de traza | `PROVED` | `PROVED` | (HD-8) |
| rango mesoscópico y testigo profundo | `PASS_WITH_REGIONAL_SCOPE` | `PASS_WITH_REGIONAL_SCOPE` | §3 |
| F1 exacta | `PROVED` | `PROVED` | orden inducido |
| F2 con constante fija | `PROVED_MODULO_SOURCE_SCOPE` | `PROVED_MODULO_SOURCE_SCOPE` | (HD-12)--(HD-16) |
| fallo F3 por margen constante | `PROVED_MODULO_SOURCE_SCOPE` | `PROVED_MODULO_SOURCE_SCOPE` | (HD-17)--(HD-18) |
| novedad bibliográfica | `TARGETED_PASS` | `TARGETED_PASS` | §7; sin prioridad absoluta |

```text
MATHEMATICAL_D3_D4: CLOSED
HIGHER_D_RESULT: PROVED_FOR_EACH_FIXED_D_GE_2_MODULO_SOURCE_SCOPE
CURVATURE_NORM: UNDEFINED_IN_MADSEN / BOTH_STANDARD_READINGS_PASS
REGIONAL_DEFINITION_2_6: NOT_LITERAL_IN_MADSEN_REMARK_5_4
NOVELTY_D_GE_3: TARGETED_AUDIT_NO_SUBSUMING_PRECEDENT
PRIORITY_LANGUAGE: ABSOLUTE_PRIORITY_PROHIBITED
POSTER_PROMOTION: MATHEMATICALLY_AUTHORIZED_WITH_SOURCE_SCOPE
```

## 7. Auditoría bibliográfica dirigida en \(d\ge3\)

Se repitieron las búsquedas de la auditoría principal con términos específicos de dimensión
superior, plantación de cadenas, uniformidad de cuentas, embeddings fieles y
longest-chain/proper-time. También se buscaron respuestas o contraejemplos que citaran
explícitamente el preprint de Madsen. No apareció un trabajo que contenga la conjunción

\[
\text{una configuración de alta densidad}
+\text{F1 exacta}
+\text{F2 cuantitativa uniforme}
+\text{fallo explícito de F3 por cadena}
\]

en \(d=3\) o \(d=4\).

| Fuente primaria | Lo que cubre en dimensión superior | Por qué no subsume esta extensión |
|---|---|---|
| Madsen, Def. 2.6 y nota 1 | Formula F1--F3 para dimensión general \(d\) y declara abierta la relación F1--F2 frente a F3 | Es la fuente del problema; no construye un contraejemplo |
| Müller, arXiv:2503.01719v2, Thm. 2 y pp. 3--4 | Uniformidad de cuentas a escala de Planck junto con geometría de tiempo propio globalmente equivocada | Compara dos geometrías y leyes de órdenes a \(K\) fijo; no da una configuración, un embedding fijo ni un certificado F3 por longest chain |
| Braun, Thm. 1.4 | Para \(d\ge3\), igualdad exacta de las leyes de matrices de adyacencia para todo \(k\) reconstruye el espaciotiempo | Sus cuantificadores de ensemble para todo \(k\) son mucho más fuertes y distintos de F2 sobre una configuración adversarial |
| Aghili--Bombelli--Pilgrim, arXiv:1807.08701 | Distribuciones de cadenas y cadenas maximales de sprinklings uniformes en varias dimensiones | Parte de uniformidad aleatoria; no estudia una perturbación adversarial que conserve F2 y rompa F3 |
| Johnston, arXiv:2111.09331 | Algoritmo de embedding en Minkowski con ejemplos en \(d=2,3,4\) | Reconstruye coordenadas usando volúmenes inferidos; no prueba F2\(\Rightarrow\)F3 ni exhibe F2 sin F3 |

El veredicto bibliográfico prudente es
`TARGETED_AUDIT_NO_SUBSUMING_PRECEDENT`. Esto autoriza describir el resultado y preguntar
por precedentes, pero no afirmar prioridad absoluta.

## 8. Fuentes y comprobaciones externas

- [N. Madsen, *On the Uniqueness of Embeddings of Causal Sets*](https://arxiv.org/html/2607.05840v1),
  Def. 2.6, Lemma 5.2 y Remark 5.4: cuantificadores y normalizaciones de F1--F3.
- [G. W. Gibbons y S. N. Solodukhin, *The Geometry of Large Causal Diamonds and the No Hair Property of Asymptotically de-Sitter Spacetimes*](https://arxiv.org/abs/0706.0603):
  su fórmula cuatridimensional coincide con \(V_4\) en (HD-4) al restaurar \(\ell\).
- [M. Aghili, L. Bombelli y B. B. Pilgrim, *Discrete Spacetime: a Web of Chains*](https://arxiv.org/abs/1807.08701):
  distribuciones de cadenas en sprinklings uniformes de varias dimensiones.
- [S. Johnston, *Embedding Causal Sets into Minkowski Spacetime*](https://arxiv.org/abs/2111.09331):
  método de embedding con resultados en \(d=2,3,4\).
- [M. Braun, *Spacetime reconstruction by order and number*](https://arxiv.org/abs/2507.01907):
  reconstrucción probabilística para \(d\ge3\) desde las leyes exactas para todo \(k\).

Las fórmulas \(d=3\) y \(d=4\) de (HD-3) también se obtienen directamente integrando
(HD-2); no se toman como hipótesis de las fuentes. La comprobación algebraica reproducible
está en `wp7_f2_f3_higher_dimensional_checks.py`.
