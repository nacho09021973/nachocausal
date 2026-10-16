<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 14929ebaaf557162cec5fab1f54a14a51da636d4; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 bcaf2d80615ed82c36faf282a64d7adbc0b664f07a1dc8847202f14ee861082f; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 373524c2af340e98f8edee2f7a6448353b0f208d5c343a3c3a558690396829bb
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-10-16T09:47:08Z  fin: 2026-10-16T09:58:39Z
documento: /home/ignac/nachocausal/revisiones/2026-10-16-tasa-minimax-caja-ef/nota_8_9.md ; último commit observado: sin versionar ; sha256 de la copia enviada da60785344b2ca44771a019058e2a80604d2f2e0dbc11fc68fa21a1a4b453c92
entrada_grok.txt sha256 7516ff36423c522fbb04f04fa4664b13a46cc2c259846e1a3b4e92fb762a15ab
respuesta sha256 f2ea3ed1b859f800b5ac7effcfe0415c17e49f6c42022e31d36c201ab865f49b
-->

**Veredicto: correcto con salvedades enumeradas.** D–G se sostienen; la primera fisura está en H, y sólo en el protocolo de Poisson y en el rango de la constante inferior.

### D
La igualdad de información y la de variación total son exactas. Como \(w_n\) no depende de \(\tau\) y los bloques \(N=n\) tienen soportes disjuntos,
\[
I^{\mathrm{Pois}}=\sum_n w_n I_n^\Pi,\qquad
\mathrm{TV}=\sum_n w_n\,\mathrm{TV}_n.
\]
Con (A), \(I^{\mathrm{Pois}}(\tau)\le\Lambda J(\tau)\). Con (C) y Jensen (\(\sqrt{\cdot}\) cóncava),
\[
\mathrm{TV}\le\frac{|\delta|}{2}\sqrt{\bar J}\,\mathbb{E}\sqrt{N}\le\frac{|\delta|}{2}\sqrt{\bar J\Lambda}.
\]
La ley de \(N\) no depende de \(\tau\): en EF entrante \(1{+}1\), \(g_{vv}=-(1-\tau/r)\), \(g_{vr}=1\), \(g_{rr}=0\), así que \(\det g=-1\) y \(\sqrt{-g}=1\). El volumen coordenado de \(B\) es \(TL\).

Para el resto en \(\ell^2\): en cada \(n\) el espacio es finito y \(s_n\) es \(C^2\) (§1), luego
\[
\|s_n(\tau+h)-s_n(\tau)-h\dot s_n\|\le\frac{h^2}{2}C_K n.
\]
Multiplicando por \(\sqrt{w_n}\) y sumando, con \(\mathbb{E}[N^2]=\Lambda+\Lambda^2\),
\[
\|S(\tau+h)-S(\tau)-h\dot S\|\le\frac{h^2}{2}C_K\sqrt{\Lambda+\Lambda^2}.
\]
Las dos sumas declaradas bastan como dominación (\(\sum w_n\sup\|\dot s_n\|^2\le\bar J\Lambda/4\) mete a \(\dot S\) en \(\ell^2\); la de segundas derivadas domina el resto y, por convergencia dominada, da continuidad de \(\dot S\)). No hace falta otra cota global: sólo eso, más \(w_n\) libre de \(\tau\) y la \(C^2\) por bloques ya aceptada. La mezcla es QMD en \(K\), uniformemente.

### E
La fórmula de Hoeffding es la estándar de orden 2:
\[
\mathrm{Var}\,U_n=\binom{n}{2}^{-1}\bigl[2(n-2)\zeta_1+\zeta_2\bigr].
\]
Como \(h\in\{0,1\}\), \(\zeta_2=p(1-p)\). Por la descomposición de varianza, \(\zeta_1=\mathrm{Var}(\mathbb{E}[h\mid X_1])\le\zeta_2\). Además \(2n-3\le 2(n-1)\), así que
\[
\mathrm{Var}\,U_n\le\frac{4p(1-p)}{n}.
\]
(La cota fina sería \(2(2n-3)p(1-p)/(n(n-1))\); el \(4\) es válido y asintóticamente ajustado al usar sólo \(\zeta_1\le\zeta_2\).)

En el orden producto, con los puntos ordenados por \(v\), dos puntos son comparables si y sólo si forman una no inversión de \(\Pi_n\). Por tanto
\[
U_n=\bigl(\binom{n}{2}-\mathrm{inv}(\Pi_n)\bigr)/\binom{n}{2}
\]
es función de \(\Pi_n\) y, al ser el número de relaciones, también del poset sin etiquetas. En el espacio canónico \(S_n\) esa función no depende de \(\tau\): sólo su ley. Con \(S_n\) finito y \(\pi_\sigma\in C^1\),
\[
\frac{d}{d\tau}\mathbb{E}U_n=\mathrm{Cov}(U_n,\mathrm{score})\le\sqrt{\mathrm{Var}(U_n)\,I_n^\Pi}.
\]
De ahí \(I_n^\Pi\ge n\,p'^2/(4p(1-p))\), siempre que \(0<p<1\). Eso se cumple en \(K\): hay probabilidad positiva de «interior antes que exterior» (nunca relacionados, luego \(p<1\)) y de pares exteriores con radio posterior menor (siempre relacionados, luego \(p>0\)).

### F
\(p(K)\) es un intervalo compacto. La proyección sobre un intervalo no aumenta la distancia a un punto del intervalo, y \(|(p^{-1})'|=1/|p'|\le 1/m\), así que
\[
|\hat\tau-\tau|\le|U_n-p(\tau)|/m.
\]
Cauchy–Schwarz da \(\mathbb{E}|U_n-p|\le\sqrt{\mathrm{Var}}\le 2\sqrt{p(1-p)}/\sqrt{n}\). Por tanto
\[
\sup_K\mathbb{E}|\hat\tau-\tau|\le 2\sup_K\sqrt{p(1-p)}/(m\sqrt{n}),
\]
para \(n\ge 2\). El recorte y el factor \(2\) son correctos. El argumento usa la cota de varianza de E, que no está repetida en el párrafo de F pero ya está probada.

### G
No hay ningún par fijo cuyo indicador pase de \(0\) a \(1\). Criterio maestro, equivalente a \(u_1<u_2\) cuando \(v_1<v_2\): \(W(r_1)e^{\Delta v/(2\tau)}>W(r_2)\). No divide por \(W\), así que vale con cualquier signo.

- **Exterior–exterior.** Equivale a \(\Delta v>\Delta\varphi\). \(\partial_r\varphi=2+2\tau/(r-\tau)>0\), luego si \(r_2\le r_1\) se cumple siempre. Si \(r_2>r_1\), \(\gamma'(r)=2/(r-\tau)+2\tau/(r-\tau)^2>0\), el umbral sube y el indicador sólo puede pasar de \(1\) a \(0\).
- **Interior–interior.** Equivale a \(\Delta v<\varphi(r_2)-\varphi(r_1)\). \(\partial_r\varphi=-2r/(\tau-r)<0\), luego si \(r_2\ge r_1\) no se da nunca. Si \(r_2<r_1\), \(\gamma_{\mathrm{int}}'(r)=2r/(\tau-r)^2>0\) (la identidad con \(-2/(\tau-r)+2\tau/(\tau-r)^2\) es algebraica), así que \(\gamma(r_2)-\gamma(r_1)<0\): el umbral baja y el indicador sólo puede pasar de \(1\) a \(0\).
- **Exterior antes que interior.** \(W(r_1)>0>W(r_2)\): siempre. **Interior antes que exterior:** lado izquierdo negativo y derecho positivo: nunca.
- **Cruces.** Si el posterior tiene mayor radio, al acercarse \(\tau\) al radio anterior \(\varphi\to-\infty\), el umbral exterior \(\to+\infty\) y el indicador ya es \(0\) antes del cruce; después es «interior antes que exterior», sigue en \(0\). Si el posterior tiene menor radio, el indicador vale \(1\) hasta el horizonte del anterior y, justo dentro, \(\varphi(r_{\mathrm{anterior}})\to-\infty\) hace el umbral interior \(+\infty\), así que sigue en \(1\); más tarde sólo puede caer a \(0\). Radios iguales: \(1\) fuera y \(0\) en el horizonte y dentro.

El factor de \(c\) es el correcto, no el doble ni la mitad. Ordenando por \(v\) (densidad \(2/T^2\) en \(v_1<v_2\); los radios siguen siendo i.i.d.), para \(r_2>r_1>\tau\)
\[
\mathbb{P}(\Delta v>\Delta\varphi)=(T-\Delta\varphi)_+^2/T^2,
\]
y derivar en \(\tau\) produce exactamente \((2/T)(1-\Delta\varphi/T)_+(\gamma(r_2)-\gamma(r_1))\). Los interiores sólo añaden decrecimiento. El cociente incremental de los exteriores que permanecen con \(r>\tau+h\), dividido por \(h\), tiene límite puntual el integrando de \(c\); Fatou (funciones no negativas, sin dominación extra) da \(-p'\ge c\).

\(c(\tau)>0\): en \(\tau<r_1<r_2<r_b\) con \(r_2-r_1\) pequeño, \(\Delta\varphi<T\) y \(\gamma(r_2)-\gamma(r_1)>0\) en un abierto de medida positiva. La singularidad de \(\gamma\) al horizonte es integrable: \(\Delta\varphi<T\) obliga a \(u=O(s)\) y el jacobiano cancela el \(1/s\). Como \(p=\pi_{\mathrm{id}}\) (\(n=2\)) es \(C^1\), \(c\le -p'<\infty\). El integrando es \(\ge 0\) y \(\liminf_{\tau'\to\tau}f_{\tau'}\ge f_\tau\) en casi todo punto, así que Fatou da que \(c\) es semicontinua inferiormente. En el compacto \(K\) alcanza el mínimo, y ese mínimo es positivo. Luego \(m=\min_K|p'|\ge\min_K c>0\).

### H
De G, \(p\) es \(C^1\) y estrictamente monótona con \(m>0\), así que F se aplica (apoyada en la varianza de E). El lado derecho del sándwich es correcto para todo \(n\ge 2\).

El lado izquierdo sale del método de dos puntos y de (C), no de E. Con \(\mathrm{TV}\le 1/2\) se puede tomar \(|\delta|=1/\sqrt{n\bar J}\), y entonces
\[
\max\bigl(\mathbb{E}_\tau|\hat\tau-\tau|,\mathbb{E}_{\tau+\delta}|\hat\tau-\tau-\delta|\bigr)\ge|\delta|/8,
\]
siempre que ese \(\delta\) quepa en \(K\). Eso demuestra la tasa \(n^{-1/2}\) y la existencia de un \(c_1>0\), pero sólo para \(n\) grande respecto de \(|K|\) y de \(\bar J\): si \(n\) es pequeño, \(1/\sqrt{n\bar J}\) supera el diámetro y la cota literal es falsa. Salvedad de rango, no de tasa.

**Protocolo de Poisson: la frase «lo mismo vale con \(\Lambda\)» no se sigue con la constante \(2\).** De D(3), el mismo argumento de dos puntos da la cota inferior de orden \(\Lambda^{-1/2}\) para \(\Lambda\) grande. Para la superior, F no está definido si \(N<2\), y al condicionar
\[
\mathbb{E}|\hat\tau-\tau|\le\frac{2\sup\sqrt{p(1-p)}}{m}\,\mathbb{E}[N^{-1/2}1_{N\ge 2}]+\mathrm{diam}(K)\,\mathbb{P}(N<2).
\]
La función \(x^{-1/2}\) es convexa y \(\mathbb{E}[N^{-1/2}]\sim\Lambda^{-1/2}+(3/8)\Lambda^{-3/2}>\Lambda^{-1/2}\), así que este mayorante no es \(\le 2\sup\sqrt{p(1-p)}/(m\sqrt{\Lambda})\). La tasa \(\Lambda^{-1/2}\) sí se salva con otra constante: para \(N\ge 1\), \(N^{-1/2}\le\sqrt{2}/\sqrt{N+1}\) y \(\mathbb{E}[(N+1)^{-1}]\le 1/\Lambda\), luego \(\mathbb{E}[N^{-1/2}1_{N\ge 1}]\le\sqrt{2/\Lambda}\); el término \(N<2\) es \(O(\Lambda e^{-\Lambda})\) y queda absorbido para \(\Lambda\) grande. No afirmo que la desigualdad con el \(2\) literal sea falsa: el argumento de la nota no la demuestra, y la holgura \(\mathbb{E}|Z|\le\sqrt{\mathbb{E}Z^2}\) podría compensar el factor \(1+O(\Lambda^{-1})\). Eso queda como conjetura.

### Salvedades
1. H, \(n\) fijo: \(c_1/\sqrt{n\bar J}\) vale para \(n\ge n_0(K,\bar J)\), no para todo \(n\) con un \(c_1\) fijo.
2. H, Poisson: la tasa \(\Lambda^{-1/2}\) es correcta; la constante \(2\) y la sustitución literal \(n\mapsto\Lambda\) no se deducen de C, F y G, y el estimador de F hay que definirlo para \(N<2\).
