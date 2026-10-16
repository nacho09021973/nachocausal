<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ fbc5b3c984372ec865171c5a727c7f8bb3c3482f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, max_tokens=por defecto de la API, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 753521e17b73e295419aaa30fcd73bb99bc26874cde1774329c2fe98f4863e08
inicio: 2026-10-16T08:03:26Z  fin: 2026-10-16T08:16:44Z
documento: /home/ignac/nachocausal/revisiones/2026-10-16-cociente-horizonte-ciego/nota_cociente.md ; último commit observado: sin versionar ; sha256 de la copia enviada 8ffaddbaa9d47602cab602af8594ef3ed1503103aeb813df6bf911ab169cd8da
entrada_deepseek.txt sha256 3023b53dde26d2a976e1790bbd617891644c9a8f6b141b56a1e26bc27cd9dab0
respuesta sha256 58f49975007adca8aa79a61b6f0c0d475f63dc878b9266e376cd1ef862cdc070
-->

**Veredicto: correcta con salvedades menores.** No encuentro un paso roto. Paso por los puntos pedidos.

## L1 y L2: reducción exacta a φ

La reducción es exacta salvo empates de probabilidad cero.

Para \(r\neq \tau\),
\[
W_\tau(r)=e^{r/\tau}(r/\tau-1)
\]
tiene el signo de \(r-\tau\). Por tanto
\[
u_\tau=-e^{-v/(2\tau)}W_\tau(r)<0 \iff r>\tau.
\]
Así, todo punto exterior tiene \(u<0\) y todo punto interior tiene \(u>0\); luego los exteriores preceden en \(u\) a los interiores.

Dentro de cada lado, con \(\varepsilon=+1\) en exterior y \(\varepsilon=-1\) en interior, \(t=|r-\tau|\), \(t_b=|b_J-\tau|\), se tiene
\[
|W_\tau(b_J)|/|W_\tau(r)|= e^{\varepsilon(t_b-t)/\tau}\, t_b/t,
\]
por lo que
\[
D=2\tau\log(t_b/t)+2\varepsilon(t_b-t).
\]
El signo es correcto y \(D\ge 0\) porque \(|W_\tau|\) es monótono hacia el borde correspondiente. Además
\[
\log|u|=\log|W_\tau(b_J)|-\frac{D+V}{2\tau}.
\]
En el exterior \(u=-|u|\), luego \(u<u'\iff D+V<D'+V'\). En el interior \(u=|u|\), luego \(u<u'\iff D+V>D'+V'\). Por tanto, con \(S=D+V\), la regla
\[
\text{exteriores por \(S\) creciente, después interiores por \(S\) decreciente}
\]
es correcta.

En los bordes radiales \(r=b_J\) se tiene \(D=0\) y la regla se reduce a \(S=V\), que da el orden correcto. Muy cerca del horizonte, \(D\to\infty\); los exteriores tienden a \(u\to 0^-\) y los interiores a \(u\to 0^+\), lo que también es coherente con la regla. No hay contraejemplo.

## L3: densidad \(f_\tau(j,d)\)

La densidad es correcta. Lo verifico por supervivencia.

Para un lado fijo \(j\), sea \(t_d\) la solución de
\[
t e^{\varepsilon t/\tau}=t_b e^{\varepsilon t_b/\tau}e^{-d/(2\tau)}.
\]
Como \(D\) es estrictamente decreciente en \(t\), \(D>d\iff t<t_d\). La probabilidad de ese suceso en el lado correspondiente es
\[
P_\tau(J=j,D>d)=\frac{t_d}{L},
\]
porque en coordenada \(r\) corresponde a un intervalo de longitud \(t_d\). Derivando la ecuación implícita respecto de \(d\),
\[
\left(\frac1t+\frac{\varepsilon}{\tau}\right)\frac{dt_d}{dd}
=
-\frac1{2\tau},
\]
luego
\[
\frac{dt_d}{dd}
=
-\frac{t}{2(\tau+\varepsilon t)}.
\]
Por tanto la densidad respecto de \(d\) es
\[
f_\tau(j,d)=\frac1L\left|\frac{dt_d}{dd}\right|
=
\frac{t}{2L(\tau+\varepsilon t)}.
\]
La normalización por lado es correcta:
\[
\int_0^\infty f_\tau(j,d)\,dd
=
\int_0^{t_b}\frac{dt}{L}
=
\frac{t_b}{L}
=
\begin{cases}
(\tau-r_a)/L,& j=\mathrm{int},\\
(r_b-\tau)/L,& j=\mathrm{ext}.
\end{cases}
\]

## L4: regularidad, borde \(d=0\), cola, cita

La regularidad es esencialmente correcta, con una salvedad de presentación.

Para cada \(d>0\), la función implícita
\[
G(t,\tau,d)=\log t+\varepsilon t/\tau-\log t_b-\varepsilon t_b/\tau+d/(2\tau)=0
\]
satisface
\[
\frac{\partial G}{\partial t}=\frac1t+\frac{\varepsilon}{\tau}>0.
\]
En el interior, \(t<\tau-r_a<\tau\), así que incluso para \(\varepsilon=-1\) el denominador es positivo. Por el teorema de la función implícita, \(t_\tau(d)\) es \(C^\infty\) en \(\tau\).

El borde \(d=0\) no es un problema. Ahí la densidad como función de \(d\) tiene una discontinuidad de borde, pero el soporte es fijo y QMD se refiere a diferenciabilidad en \(\tau\) en \(L^2\), no a continuidad en la observación. El valor en \(d=0\) tiene medida cero y no afecta a la derivada \(L^2\).

La cola es exponencial: como \(\varepsilon(t_b-t)\ge 0\),
\[
D\ge 2\tau\log(t_b/t),
\]
luego
\[
t\le t_b e^{-D/(2\tau)}\le L e^{-d/(2\tau)}.
\]
Como \(K\Subset(r_a,r_b)\), hay \(\tau_{\max}\) tal que
\[
t\le L e^{-d/(2\tau_{\max})}.
\]
Además \(r=\tau+\varepsilon t\ge r_a>0\), así que
\[
f_\tau(j,d)\le C e^{-d/(2\tau_{\max})}.
\]
Derivando la ecuación implícita se obtiene \(t_\tau/t=O(1+d)\) uniformemente en \(K\), y
\[
\partial_\tau\log f
=
\frac{t_\tau}{t}-\frac{1+\varepsilon t_\tau}{\tau+\varepsilon t}
=
O(1+d).
\]
Por tanto
\[
J(\tau)=E[(\partial_\tau\log f)^2]<\infty
\]
y, por convergencia dominada, es continua en \(K\).

La cita “van der Vaart, lema 7.6” puede no ser exacta con ese número, pero el enunciado usado es un criterio estándar: si \(\tau\mapsto\sqrt{f_\tau}\) es \(L^2\)-diferenciable, la familia es QMD. Aquí se obtiene acotando
\[
|\partial_\tau\sqrt{f_\tau}|
=
\frac12\sqrt{f_\tau}\,|\partial_\tau\log f_\tau|
\le
C(1+d)e^{-d/(4\tau_{\max})},
\]
que es \(L^2\), y usando el teorema del valor medio para la dominación local. Así que L4 es correcto si se añade explícitamente esa dominación.

## L5: derivación bajo la integral y Cauchy–Schwarz

Es legítimo. En la representación auxiliar,
\[
\pi_\sigma(\tau)=E_\tau[1\{\varphi(X)=\sigma\}],
\]
donde \(X=(J_i,D_i,V_i)_i\). Aquí \(\varphi\) es fija; no hay dependencia oculta en \(\tau\) dentro del evento \(\{\varphi(X)=\sigma\}\). La dependencia en \(\tau\) está solo en la densidad de \(X\).

La densidad de \(X\) es producto de densidades \(f_\tau(j,d)\) y de la densidad uniforme de \(V\). Usando las cotas de L4,
\[
|\partial_\tau\log f_\tau|\le C(1+d),
\]
y la densidad tiene cola exponencial, así que hay dominación uniforme en \(K\) para derivar bajo la integral. Por tanto
\[
\pi_\sigma'(\tau)
=
E_\tau[A_n 1\{\varphi(X)=\sigma\}],
\]
con
\[
A_n=\sum_i \partial_\tau\log f_\tau(J_i,D_i).
\]
Como la densidad integra a 1, \(E[\partial_\tau\log f]=0\), luego \(E[A_n]=0\) y \(E[A_n^2]=nJ(\tau)\).

Por Cauchy–Schwarz,
\[
\pi_\sigma'^2
=
(E[A_n 1_A])^2
\le
E[A_n^2 1_A]\,P(A),
\]
donde \(A=\{\varphi(X)=\sigma\}\). Dividiendo por \(\pi_\sigma=P(A)\),
\[
\frac{\pi_\sigma'^2}{\pi_\sigma}
\le
E[A_n^2 1_A].
\]
Sumando en \(\sigma\),
\[
I_n^\Pi(\tau)
\le
E[A_n^2]
=
nJ(\tau).
\]
Este paso es correcto.

## Compatibilidad con el no-QMD de un punto

No hay contradicción. La ley de un punto en \((u,v)\) tiene soporte móvil y no es QMD. La ley auxiliar \((J,D,V)\) tiene soporte fijo y sí es QMD. La transformación \((v,r)\mapsto(J,D,V)\) depende de \(\tau\), así que no es una función fija de \((u,v)\). Por tanto, una familia puede ser regular después de una biyección dependiente del parámetro aunque la familia original no lo sea.

En cuanto a la frase previa:

> “Un mapa dependiente de τ puede fijar el soporte, pero entonces el canal de orden también depende de τ”,

es ambigua. Si se interpreta literalmente como que la regla de orden debe depender de \(\tau\), la construcción de la nota la refuta, porque \(\varphi\) es fija. Si se interpreta como que el mapa de regularización depende de \(\tau\), entonces es compatible. La frase no es un teorema con la lectura fuerte.

## Conclusión final

La afirmación es **correcta con salvedades enumeradas**:

1. L1–L2 son exactos salvo empates de probabilidad cero.
2. L3 es correcta.
3. L4 es correcta, pero conviene explicitar la dominación \(L^2\) para obtener QMD; el borde \(d=0\) no afecta.
4. L5 es correcto.
5. No hay contradicción con el no-QMD de un punto.

La cota \(I_n^\Pi\le nJ(\tau)\) es natural en orden \(n\) por data processing, pero no es afilada en constante: \(\varphi\) descarta información cardinal, así que cabe esperar una constante efectiva menor. Mejorarla exigiría calcular directamente la información de Fisher de la permutación o de los órdenes relativos por pares, no solo acotar por la muestra auxiliar completa.
