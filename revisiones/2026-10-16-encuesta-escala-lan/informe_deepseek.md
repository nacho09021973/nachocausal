<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ fbc5b3c984372ec865171c5a727c7f8bb3c3482f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, max_tokens=por defecto de la API, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 bc293b7f160f399b388be71eac1f8dd0b9f02249f741bbcc28823799b085e3c1
inicio: 2026-10-16T08:31:21Z  fin: 2026-10-16T08:34:35Z
documento: /home/ignac/nachocausal/revisiones/2026-10-16-encuesta-escala-lan/dossier.md ; último commit observado: sin versionar ; sha256 de la copia enviada 25484cda4291c63ef60661dbaec0f2a76112a9a3facaba6717ba26118c240334
entrada_deepseek.txt sha256 07e59b4102723db4466fac2c116356a375405a5fea7cb8aa1ddb8198334a76e6
respuesta sha256 d79cadcb6b916afe236e7469059ed298cf4a8ef5da7147def8b584eaedc0558c
-->

VEREDICTO: DEPENDE (de si el objetivo es eficiencia asintótica/normalidad con constante óptima o solo tasa minimax).

**1. ¿Importa la QMD uniforme en la escala LAN?**

No importa para los resultados de tasa minimax/cotas inferiores de dos puntos. La cota del manuscrito y la de la caja EF que se puede obtener con el Teorema A usan una desigualdad integrada de Hellinger/TV a partir de la información de Fisher, más el lema de dos puntos de Le Cam. Esa prueba no usa expansión LAN: solo usa que la ley es QMD a \(n\) fijo y que la información de Fisher crece como \(n\).  
Tampoco importa para afirmar que la tasa óptima es \(n^{-1/2}\), si se demuestra por cota inferior de dos puntos y cota superior emparejada.

Sí importa, en cambio, para:

- **LAN y teorema de convolución / cota minimax local de Hájek–Le Cam con constante óptima**: necesitan una expansión cuadrática del log-cociente de verosimilitud en vecindades \(\delta_n=h/\sqrt n\), con resto \(o_p(1)\). La QMD uniforme en escala LAN es una vía estándar para obtenerla. El Teorema B solo da QMD uniforme para \(n\delta_n\to0\), es decir \(\delta_n=o(1/n)\), que es más pequeña que la escala LAN, y el resto en \(\delta=h/\sqrt n\) queda \(O(h^2)\), no \(o(1)\).
- **Normalidad asintótica y eficiencia de un estimador**: si se quiere probar que un estimador sellado es asintóticamente normal con varianza óptima, normalmente hay que linealizar el score o expandir la verosimilitud alrededor de \(\tau+O(1/\sqrt n)\). Eso exige control en escala \(1/\sqrt n\), no el que da el Teorema B.
- Si “eficiencia del estimador sellado” significa solo tasa \(n^{-1/2}\), no la necesita; si significa varianza asintótica óptima o constante de Hájek–Le Cam, sí.

Por tanto, la QMD uniforme en escala LAN no es necesaria para el programa si el objetivo es tasa; sí es necesaria si el objetivo es eficiencia asintótica fina.

**2. ¿Basta el Teorema A para una cota inferior de dos puntos de orden \(1/\sqrt{n\bar J}\) en la caja EF?**

Sí, esencialmente basta, con los ingredientes ya declarados en el dossier. El argumento es:

Para \(\Pi_n\), se tiene a \(n\) fijo que la ley es QMD. El Teorema A da \(I_n^\Pi(\tau)\le nJ(\tau)\), uniforme en \(n\), con \(J\) finita y continua en \(K\). Entonces, para \(\tau,\tau+\delta\in K\), la desigualdad integrada de Hellinger para una familia QMD da
\[
H^2(P_{n,\tau}^\Pi,P_{n,\tau+\delta}^\Pi)
\le \frac{\delta^2}{4}\, n\sup_{K} J
\]
o una constante análoga, y por tanto
\[
\mathrm{TV}(P_{n,\tau}^\Pi,P_{n,\tau+\delta}^\Pi)
\le \frac{|\delta|}{2}\sqrt{n\bar J}.
\]
Tomando \(\delta_n=c/\sqrt{n\bar J}\) con \(c\) pequeño, la TV queda acotada por \(c/2<1\). El lema de dos puntos de Le Cam da entonces una cota inferior de orden \(1/\sqrt{n\bar J}\).

Para el poset sin etiquetas, el dossier dice que el Teorema A vale también para el poset; además, como el poset es una imagen del esqueleto de permutación, la información de Fisher no aumenta por procesamiento, así que también se tiene \(I_n^{\mathrm{poset}}\le nJ\). Si la ley del poset es QMD a \(n\) fijo, el mismo argumento se aplica.

Posibles huecos, menores, serían:

- la regularidad necesaria para la desigualdad integrada de Hellinger: hay que poder escribir la raíz de la densidad como absolutamente continua en \(\tau\) con derivada en \(L^2\). Eso es exactamente la QMD a \(n\) fijo, que el dossier declara;
- uniformidad en \(K\): \(J\) continua en compacto \(K\) da \(\bar J<\infty\); para \(n\) grande, \(\tau+\delta_n\) permanece en un compacto interior, salvo en frontera, lo cual no afecta a la tasa minimax;
- el paso al poset: si no estuviera ya cubierto por el Teorema A, se cubre por procesamiento de la información y QMD del poset.

No hay hueco grave si las afirmaciones del dossier son exactas.

**3. Recomendación**

No perseguiría la escala LAN ahora si el objetivo inmediato es la tasa minimax o la recuperación geométrica de la frontera, porque el Teorema A ya da la tasa \(n^{-1/2}\) por dos puntos.

La perseguiría solo si se quiere demostrar normalidad asintótica o eficiencia asintótica con constante óptima para el estimador sellado. En ese caso, el siguiente lema mínimo sería un **lema de LAN para la imagen fija de una muestra i.i.d. regular**, aprovechando la representación del Teorema A. Concretamente, habría que probar:

\[
\log\frac{dP_{\Pi_n,\tau+h/\sqrt n}}{dP_{\Pi_n,\tau}}
=
h\, S_n^\Pi(\tau)
-\frac{h^2}{2}J(\tau)
+o_p(1),
\]
uniforme para \(h\) en compactos, donde
\[
S_n^\Pi(\tau)
=
n^{-1/2}\,E_\tau\!\left[\sum_i \dot\ell_\tau(X_i)\;\middle|\;\Pi_n\right]
\]
y
\[
S_n^\Pi(\tau)\Rightarrow N(0,J(\tau)).
\]

Lo que lo cerraría sería un teorema de tipo CLT/LLN condicional: convergencia normal del score condicional dado \(\Pi_n\) o el poset, y convergencia uniforme de la información condicional
\[
\sup_{|t|\le h/\sqrt n}
\left|n^{-1}I_n^\Pi(\tau+t)-J(\tau)\right|\to 0.
\]
No lo atacaría vía el módulo \(\Omega_{n,K}\), porque el Teorema B ya muestra que esa vía es demasiado cruda en escala \(h/\sqrt n\). La vía natural es explotar la estructura de imagen fija de una muestra regular y hacer un análisis condicional del score.
