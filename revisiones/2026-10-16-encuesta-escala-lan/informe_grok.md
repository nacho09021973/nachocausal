<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ fbc5b3c984372ec865171c5a727c7f8bb3c3482f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 8cf470859a535ef52a7f5a0d83927869c9cfad518fcbd66cc6be4988abeeecae
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-10-16T08:35:03Z  fin: 2026-10-16T08:40:23Z
documento: /home/ignac/nachocausal/revisiones/2026-10-16-encuesta-escala-lan/dossier.md ; último commit observado: sin versionar ; sha256 de la copia enviada 25484cda4291c63ef60661dbaec0f2a76112a9a3facaba6717ba26118c240334
entrada_grok.txt sha256 07e59b4102723db4466fac2c116356a375405a5fea7cb8aa1ddb8198334a76e6
respuesta sha256 9a5fe29d93a06c114b2bfadfdf6c326d53224508c4319b29b147160aaf16be25
-->

VEREDICTO: DEPENDE (de si el objetivo es el orden de la tasa o la constante del límite gaussiano)

### 1. Escala LAN

No hace falta para el análogo del manuscrito: una cota inferior del orden de la tasa. El paso que allí cierra la tasa es la desigualdad integrada de Hellinger —acota \(\mathrm{TV}\) por la norma \(L^2\) de la diferencia de raíces, y esa norma por \(\int\sqrt{I}\)— seguida del método de dos puntos. Ninguno de los dos usa la expansión del cociente de verosimilitudes ni el resto \(o_{P}(1)\).

Sí hace falta para tres resultados concretos, y en un paso identificable:

- LAN del experimento \(\{\Pi_n: \tau+h n^{-1/2}\}\) y, a partir de ella, el teorema de convolución o el minimax local de Hájek–Le Cam con constante óptima. El paso que lo exige es que el resto de la aproximación lineal de la raíz, \(\|s_n(\tau+h n^{-1/2})-s_n(\tau)-(h n^{-1/2})\dot s_n\|\), sea \(o(n^{-1/2})\) con \(h\) en compactos, de modo que el log-cociente converja al desplazamiento gaussiano. El Teorema B solo da el majorante \((\delta^2/2)\sup\|\ddot s\|\), que en esa escala es \(O(h^2)\) y no tiende a 0. Eso no prueba que el resto real falle: el propio dossier recuerda que el módulo del gaussiano producto, que sí es LAN, es del mismo orden \(n\delta\). La cota por \(\|\ddot s\|\) es demasiado gruesa; no decide la LAN.
- Normalidad asintótica de un estimador, si se quiere deducirla de la convergencia de experimentos. Una demostración directa (linealidad asintótica más un TCL) no usa LAN; lo que sí la usa es llamarla eficiente.
- Eficiencia del estimador sellado. Además de la LAN haría falta el puente entre Fisher y ese estimador, que el dossier deja abierto y no autorizado. La escala LAN no sustituye ese puente, ni la mezcla de Poisson, ni nada en 3+1D.

Opinión: para el programa tal como está escrito —recuperar el orden \(n^{-1/2}\) que el diamante ya tiene— la escala LAN no cambia ningún teorema siguiente autorizado.

### 2. Teorema A y la cota \(1/\sqrt{n\bar J}\)

A solo, no. Una cota de Fisher no acota el Hellinger. El paso que falta es la desigualdad integrada: \(\|\sqrt{\pi_{\tau+\delta}}-\sqrt{\pi_\tau}\|\le\int_0^{|\delta|}\|\dot s\|\) y \(\|\dot s\|=\sqrt{I_n}/2\). Sin identificar \(I_n^\Pi\) con la velocidad \(L^2\) de la raíz, \(I_n^\Pi\le n J\) no impide separaciones grandes.

A y B juntos sí bastan para \(\Pi_n\), y este paso no pasa por la escala LAN. B da \(s_n\) de clase \(C^2\) en el compacto, así que el teorema fundamental vale en todo el segmento y no hace falta que el resto de primer orden sea \(o(|\delta|)\). Con \(I_n=4\|\dot s_n\|^2\) y el Teorema A,
\[
\mathrm{TV}(\Pi_{n,\tau},\Pi_{n,\tau+\delta})\le\|s_n(\tau+\delta)-s_n(\tau)\|\le\frac{|\delta|}{2}\sqrt{n\bar J},
\]
mientras el segmento siga en \(K\). Aquí se usa que \(J\) es continua en un compacto, luego \(\bar J<\infty\), y la cota de A es uniforme en \(n\) y en \(\tau\in K\). Para \(\delta=h n^{-1/2}\) con \(|h|<2/\sqrt{\bar J}\) la TV queda estrictamente por debajo de 1, y el método de dos puntos da riesgo minimax de orden \(1/\sqrt{n\bar J}\). La variación \(\|\dot s(\tau+\delta)-\dot s(\tau)\|\le C_K n|\delta|\), que en la escala LAN es del mismo orden que \(\|\dot s\|\) y es justo lo que estropea la linealización, no entra: la integral solo usa el supremo, y A lo tapa.

El poset no hereda esto de B: B está escrito para las masas de \(\Pi_n\). Lo hereda si, como afirma A, es imagen medible fija de \(\Pi_n\) o de la misma muestra i.i.d. regular. La contracción de Hellinger por un núcleo que no depende de \(\tau\) pasa la cota de TV; no pasa la LAN. Si «regular» en la prueba de A significa solo Fisher finito, sin QMD de la muestra latente ni \(C^1\) de su raíz, ese hueco sigue abierto para el poset. La muestra de un punto de la caja EF no sirve de atajo: el dossier dice que no es QMD.

La constante que sale es la de la cota de TV, no la del riesgo gaussiano \(1/\sqrt{I}\).

### 3. Recomendación

No perseguir la escala LAN ahora. El resultado que falta para igualar al manuscrito es la cota de dos puntos de arriba, y A+B ya dan el ingrediente analítico; lo que queda es comprobar en la prueba de A que \(I_n=4\|\dot s_n\|^2\) en todo \(K\) y que el poset es imagen fija.

Perseguirla solo si el objetivo pasa a ser la constante óptima del límite gaussiano. El lema mínimo entonces es: el resto \(\ell^2\) de \(s_n\) en \(\delta=h n^{-1/2}\) es \(o(n^{-1/2})\) para \(h\) en compactos, no el majorante \((\delta^2/2)\|\ddot s\|\). Lo cerraría una cancelación (el gaussiano producto muestra que \(\|\ddot s\|=O(n)\) no lo impide), no un módulo más fino de \(\ddot s\). Ese lema seguiría sin autorizar el estimador sellado, la mezcla de Poisson ni 3+1D.
