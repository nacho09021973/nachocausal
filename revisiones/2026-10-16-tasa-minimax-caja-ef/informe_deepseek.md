<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 14929ebaaf557162cec5fab1f54a14a51da636d4; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 bcaf2d80615ed82c36faf282a64d7adbc0b664f07a1dc8847202f14ee861082f; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, max_tokens=por defecto de la API, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 e8183ed550388d3f529e60c86e35eb7e082c90aba86a5f7456558c4135806138
inicio: 2026-10-16T09:47:08Z  fin: 2026-10-16T09:56:35Z
documento: /home/ignac/nachocausal/revisiones/2026-10-16-tasa-minimax-caja-ef/nota_8_9.md ; último commit observado: sin versionar ; sha256 de la copia enviada da60785344b2ca44771a019058e2a80604d2f2e0dbc11fc68fa21a1a4b453c92
entrada_deepseek.txt sha256 7516ff36423c522fbb04f04fa4664b13a46cc2c259846e1a3b4e92fb762a15ab
respuesta sha256 2d443cf6a676ea41e20b6e3848d9ab0b50cea68a4b83a4bb8f164e55abfa4233
-->

Veredicto global: **correcto con salvedades enumeradas**. Los pasos D–H son esencialmente correctos; hay justificaciones implícitas y, en el protocolo Poisson, la constante superior no está literalmente probada para Λ fijo, aunque la tasa sí es la afirmada.

---

### D. Mezcla de Poisson

La igualdad
\[
\mathrm{TV}=\sum_n w_n \mathrm{TV}_n
\]
es correcta: para \(N=n\) los soportes de \(\Pi_n\) son disjuntos para distintos \(n\), y \(w_n\) no depende de \(\tau\). Por tanto la variación total de la mezcla es la media ponderada de las variaciones totales de cada bloque.

La información de Fisher de la mezcla también es
\[
I^{\mathrm{Pois}}=\sum_n w_n I_n^\Pi,
\]
porque el score de la observación \((N,\Pi_N)\) en el bloque \(N=n\) es \(\partial_\tau\log\pi_\sigma(\tau)\), sin término de \(w_n\). Con (A),
\[
I^{\mathrm{Pois}}\le \sum_n w_n\,nJ(\tau)=\Lambda J(\tau).
\]
La ley de \(N\) no depende de \(\tau\) porque \(\Lambda=\lambda TL\) y, en coordenadas \((v,r)\), \(\sqrt{-g}=1\), luego la medida uniforme en \(B\) es fija.

Para \(S=(\sqrt{w_n}s_n)_n\), la derivabilidad en \(\ell^2\) se justifica así: para cada \(n\),
\[
s_n(\tau+h)-s_n(\tau)-h\dot s_n(\tau)
=\frac{h^2}{2}\int_0^1(1-t)s_n''(\tau+th)\,dt
\]
en norma finito-dimensional. Por tanto
\[
\|S(\tau+h)-S(\tau)-h\dot S\|^2
\le \frac{h^4}{4}\sum_n w_n\sup_K\|s_n''\|^2
\le \frac{h^4}{4}C_K^2(\Lambda+\Lambda^2),
\]
usando (B). Esto da el residuo \(O(h^2)\). La continuidad de \(\dot S\) se obtiene igualmente de
\[
\|\dot S(\tau+h)-\dot S(\tau)\|^2
\le h^2\sum_n w_n\sup_K\|s_n''\|^2
\le h^2C_K^2(\Lambda+\Lambda^2).
\]
Así que las dos sumas declaradas bastan; no hace falta nada más, salvo la observación de que también dan la continuidad de la derivada.

El paso (3) es correcto: por Jensen,
\[
\sum_n w_n \sqrt{n}\le \sqrt{\sum_n w_n n}=\sqrt{\Lambda}.
\]

**D correcto.**

---

### E. Cota inferior de Fisher

\(U_n\) es la fracción de pares comparables. Para un par \((i,j)\), la comparabilidad equivale a que los puntos tengan el mismo orden relativo en \(u\) y en \(v\). Eso está determinado por \(\Pi_n\) y es invariante por reetiquetado, luego \(U_n\) es función de \(\Pi_n\) y del poset no etiquetado.

La fórmula de Hoeffding para un \(U\)-estadístico de grado 2 es
\[
\operatorname{Var}U_n=\binom n2^{-1}\bigl(2(n-2)\zeta_1+\zeta_2\bigr).
\]
Aquí \(\zeta_2=\operatorname{Var}(h)=p(1-p)\). Para Bernoulli, \(\zeta_1=\operatorname{Cov}(h_{12},h_{13})\le p(1-p)=\zeta_2\), pues la covarianza entre dos Bernoulli con marginal \(p\) no puede superar \(p(1-p)\). Entonces
\[
\operatorname{Var}U_n
\le \binom n2^{-1}(2(n-2)+1)p(1-p)
=\frac{2(2n-3)}{n(n-1)}p(1-p)
\le \frac{4p(1-p)}n.
\]
La última desigualdad equivale a \(2(2n-3)\le 4(n-1)\), cierta para \(n\ge2\).

Como \(U_n\) es función de \(\Pi_n\), para el score de \(\Pi_n\),
\[
\frac{d}{d\tau}\mathbb E_\tau U_n
=\operatorname{Cov}_\tau(U_n,\text{score}).
\]
Por Cauchy–Schwarz,
\[
|p'(\tau)|
\le \sqrt{\operatorname{Var}U_n\cdot I_n^\Pi}.
\]
Despejando se obtiene
\[
I_n^\Pi\ge \frac{n p'(\tau)^2}{4p(1-p)}.
\]

**E correcto.**

---

### F. Cota superior

La cota es correcta. Si \(p\) es estrictamente monótona y \(m=\min_K|p'|>0\), entonces \(p^{-1}:p(K)\to K\) es \(1/m\)-Lipschitz. El recorte a \(p(K)\) es una proyección sobre un intervalo que contiene a \(p(\tau)\), luego no aleja:
\[
|\operatorname{clip}_{p(K)}U_n-p(\tau)|\le |U_n-p(\tau)|.
\]
Por tanto
\[
\mathbb E_\tau|\hat\tau-\tau|
\le m^{-1}\mathbb E_\tau|U_n-p(\tau)|
\le m^{-1}\sqrt{\operatorname{Var}U_n}
\le \frac{2\sqrt{p(1-p)}}{m\sqrt n}.
\]
Tomando supremo en \(\tau\in K\), sale la cota de F.

**F correcto.**

---

### G. Monotonía

Para \(v_2>v_1\), la relación \(x_1\le x_2\) en el orden producto \((u,v)\) equivale a
\[
u_1\le u_2.
\]
Con \(u=-e^{-v/(2\tau)}W_\tau(r)\), esto da
\[
W(r_1)e^{\Delta v/(2\tau)}> W(r_2),
\]
como dice la nota.

Los cuatro casos de signo están bien:

1. **Exterior–exterior** (\(r_1,r_2>\tau\)): \(W>0\). La relación es
   \[
   \Delta v>\Delta\phi,
   \]
   con \(\Delta\phi=\phi(r_2)-\phi(r_1)\). Si \(r_2\le r_1\), \(\Delta\phi\le0\) y la relación se cumple siempre. Si \(r_2>r_1\),
   \[
   \partial_\tau\Delta\phi=\gamma(r_2)-\gamma(r_1).
   \]
   Para \(r>\tau\),
   \[
   \gamma'(r)=\frac{2}{r-\tau}+\frac{2\tau}{(r-\tau)^2}
   =\frac{2r}{(r-\tau)^2}>0,
   \]
   luego el umbral sube y el indicador no puede pasar de 0 a 1.

2. **Interior–interior** (\(r_1,r_2<\tau\)): aquí \(W<0\). Cambiando signos, la relación equivale a
   \[
   \Delta v<\phi(r_2)-\phi(r_1)
   \]
   si \(r_2<r_1\), y no se da si \(r_2\ge r_1\). Para \(r<\tau\),
   \[
   \gamma_{\mathrm{int}}'(r)=\frac{2r}{(\tau-r)^2}>0.
   \]
   Por tanto, para \(r_2<r_1\), \(\gamma(r_2)-\gamma(r_1)<0\) y el umbral baja, lo que hace la condición más difícil.

3. **Exterior antes que interior** (\(r_1>\tau>r_2\)): \(W_1>0>W_2\), luego
   \[
   W_1 e^{\Delta v/(2\tau)}>W_2
   \]
   se cumple siempre.

4. **Interior antes que exterior** (\(r_2>\tau>r_1\)): \(W_1<0<W_2\), luego la desigualdad anterior nunca se cumple.

En los cruces del horizonte, \(\phi\to-\infty\) cuando \(r\to\tau\), lo que produce a lo sumo saltos de 1 a 0, no de 0 a 1. Por ejemplo, si \(r_2>r_1\) y ambos exteriores, al acercarse \(\tau\) a \(r_1\) desde abajo, \(\Delta\phi\to+\infty\), de modo que la condición \(\Delta v>\Delta\phi\) falla antes del cruce; después del cruce se cae en “interior antes que exterior”, que también falla. Si \(r_1>r_2\), el caso exterior–exterior con \(r_2\le r_1\) es siempre relacionado, y al cruzar \(r_2\) se pasa a “exterior antes que interior”, también siempre relacionado; el posible salto posterior en el cruce de \(r_1\) es de 1 a 0. No encuentro ningún par fijo cuyo indicador pase de 0 a 1 al crecer \(\tau\).

La expresión de \(c(\tau)\) es correcta como derivada de la contribución exterior–exterior. Para pares exteriores con \(r_2>r_1\), tras integrar la variable \(v\), la contribución a \(p\) es proporcional a
\[
\int_{\tau<r_1<r_2<r_b}(T-\Delta\phi)_+^2\,dr_1dr_2.
\]
Derivando respecto de \(\tau\) sale exactamente
\[
c(\tau)=L^{-2}\int_{\tau<r_1<r_2<r_b}
\frac2T\left(1-\frac{\Delta\phi}{T}\right)_+
(\gamma(r_2)-\gamma(r_1))\,dr_1dr_2.
\]
Como todos los demás cambios del indicador son no crecientes, sus contribuciones a \(-p'\) son no negativas. Aplicando Fatou a los cocientes incrementales no negativos,
\[
-p'(\tau)\ge c(\tau).
\]
La \(p\) es \(C^1\) porque es \(\pi_{\mathrm{id}}\) con \(n=2\), y las \(\pi_\sigma\) son \(C^1\) por hipótesis aceptada.

La semicontinuidad inferior de \(c\) se obtiene por Fatou, usando que el integrando es no negativo y, para cada \(r_1,r_2\), continuo en \(\tau\) salvo en \(r_1=\tau\), donde el factor \((1-\Delta\phi/T)_+\) anula la singularidad de \(\gamma\). Puntualmente \(c(\tau)>0\) porque para \(r_2\) suficientemente cercano a \(r_1\) se tiene \(\Delta\phi<T\) y \(\gamma(r_2)-\gamma(r_1)>0\). En compacto \(K\subset(r_a,r_b)\), la semicontinuidad inferior y la positividad puntual dan
\[
\min_K c>0.
\]
Por tanto \(m=\min_K|p'|\ge \min_K c>0\).

**G correcto**, con la salvedad de que la semicontinuidad inferior de \(c\) está afirmada pero no demostrada en detalle en la nota; es cierta por el argumento anterior.

---

### H. Tasa minimax

Con G, se cumplen las condiciones de F: \(p\) es \(C^1\), estrictamente decreciente y \(m>0\). La cota superior de F es
\[
\inf_{\hat\tau}\sup_K \mathbb E|\hat\tau-\tau|
\le \frac{2\sup_K\sqrt{p(1-p)}}{m\sqrt n}.
\]
La cota inferior es la aceptada en C, de orden \(1/\sqrt{n\bar J}\). Por tanto la tasa \(n^{-1/2}\) es correcta.

En el protocolo Poisson, la cota inferior se obtiene de D(3), que da
\[
\mathrm{TV}\le \frac{|\delta|}{2}\sqrt{\bar J\Lambda}.
\]
Eso produce la tasa \(\Lambda^{-1/2}\). La cota superior también es de tasa \(\Lambda^{-1/2}\), pero para \(\Lambda\) fijo no está probada con la misma constante literal de F: hay que controlar \(\mathbb E[N^{-1/2}\mathbf 1_{N\ge2}]\) y el evento \(N<2\). Asintóticamente \(\Lambda\to\infty\) esos términos son despreciables frente a \(\Lambda^{-1/2}\). La constante \(c_1\) de la cota inferior no está explicitada, pero eso no afecta a la tasa.

**H correcto como enunciado de tasa**, con la salvedad menor de que la constante Poisson superior no es exactamente la misma que en el caso fijo si se exige una desigualdad no asintótica.

---

### Salvedades finales

1. En D conviene añadir explícitamente la continuidad de \(\dot S\), aunque se deduce de la segunda suma.
2. En G conviene demostrar la semicontinuidad inferior de \(c\), no solo afirmarla.
3. En H, para Poisson con \(\Lambda\) fijo, la constante superior puede requerir un factor adicional por \(\mathbb E[N^{-1/2}]\) y por \(P(N<2)\); la tasa \(\Lambda^{-1/2}\) es correcta.

No hay ningún fallo matemático grave en D–H; el argumento es correcto con esas salvedades.
