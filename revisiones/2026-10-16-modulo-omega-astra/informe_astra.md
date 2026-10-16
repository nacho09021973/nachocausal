<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ fbc5b3c984372ec865171c5a727c7f8bb3c3482f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.162.1)
inicio: 2026-10-16T08:30:19Z  fin: 2026-10-16T08:32:26Z
documento: /home/ignac/nachocausal/revisiones/2026-10-16-modulo-omega-astra/nota_modulo.md ; último commit observado: sin versionar ; sha256 de la copia enviada ac99aad76187f608a6c93f2f3049a2f5ab29858e00f260afb8ec598b006a42d7
entrada_astra.txt sha256 f0e705f923b8ccaf2a2e3af683473ccd6572110aa35215993784e4e54f0c22be
respuesta sha256 f3d8ca9b24b655b3fbc33219ca170b7d595cad392aa33955eb07754dcea76754
-->

**Veredicto: correcta con salvedades enumeradas.** El Teorema B se demuestra con el argumento de §3. Las salvedades afectan a §4: el orden gaussiano necesita precisar el régimen, y no demuestra que la escala sea óptima para el canal de permutaciones.

**(a) Segundas derivadas, incluido el interior.** Escribamos \(\beta=b_\varepsilon\), \(q=t_b=\varepsilon(\beta-\tau)\). Entonces \(q'=-\varepsilon\) y, manteniendo \(t\) fijo,
\[
G_\tau=\frac{\varepsilon}{q}
       +\frac{\beta-\varepsilon t-d/2}{\tau^2},
\qquad
G_{\tau\tau}=\frac1{q^2}
       -\frac{2(\beta-\varepsilon t-d/2)}{\tau^3}.
\]
El término \(q^{-2}\) procede de la frontera móvil y debe incluirse. Está absorbido en el \(O(1+d)\) declarado en §3(a), porque \(K\) es compacto dentro de \((r_a,r_b)\).

La identidad implícita completa es
\[
G_t t''+G_{tt}(t')^2+2G_{t\tau}t'+G_{\tau\tau}=0.
\]
Con \(u=t'/t\),
\[
\frac{t''}{t}
=\frac{u^2+2\varepsilon t'/\tau^2-G_{\tau\tau}}
       {1+\varepsilon t/\tau}.
\]
En particular, para \(\varepsilon=-1\),
\[
G_{\tau\tau}
=\frac1{(\tau-r_a)^2}
-\frac{2(r_a+t-d/2)}{\tau^3},
\qquad
1-\frac t\tau=\frac r\tau\ge\frac{r_a}{\tau_{\max}}>0.
\]
Así, también en el interior, \(t''/t=O((1+d)^2)\), usando \(u=O(1+d)\) y \(t\le L\).

Finalmente, como \(r=\tau+\varepsilon t\),
\[
b=\frac{t''}{t}-u^2-\frac{\varepsilon t''}{r}
  +\frac{(1+\varepsilon t')^2}{r^2}
=\frac{\tau}{r}\frac{t''}{t}-u^2
  +\frac{(1+\varepsilon t')^2}{r^2}.
\]
Por tanto, **la cota uniforme es correcta**. No falta ningún término que invalide la conclusión; sí conviene explicitar los términos de frontera y el término mixto \(2G_{t\tau}t'\).

**(b) Dominación y fórmula de \(\pi''\).** Sí. Puesto que \(r\ge r_a\),
\[
f\le C e^{-d/(2\tau_{\max})},\qquad
f'=fs,\qquad f''=f(s^2+b),
\]
lo que demuestra precisamente la dominación de §3(b). Sus productos y las derivadas del producto son integrables para cada \(n\). La independencia del parámetro de \(\phi\) permite mantener fijo el indicador al derivar. Resulta
\[
\pi_\sigma''=E_\tau[(A_n^2+B_n)1_\sigma].
\]
La misma dominación justifica
\[
Es=0,\qquad E(s^2+b)=0,
\]
y, por tanto, \(Eb=-J\). También garantiza continuidad de las derivadas necesarias. En los extremos de \(K\) puede trabajarse en un intervalo compacto ligeramente mayor, todavía contenido en \((r_a,r_b)\).

**(c) Desigualdades y constante.** Todas son correctas. Escribiendo \(p=\pi_\sigma>0\), la fórmula de la segunda derivada da
\[
\ddot s_\sigma^2
\le \frac{\pi_\sigma''{}^2}{2p}
+\frac{\pi_\sigma'{}^4}{8p^3}.
\]
Para \(Z=A_n^2+B_n\), Cauchy–Schwarz da
\[
(E[Z1_\sigma])^2\le p\,E[Z^2 1_\sigma].
\]
Para el otro término se aplican sucesivamente
\[
(E[A_n1_\sigma])^2\le pE[A_n^2 1_\sigma],
\qquad
(E[A_n^2 1_\sigma])^2\le pE[A_n^4 1_\sigma].
\]
Después de sumar,
\[
\|\ddot s_n\|^2
\le \tfrac12E(A_n^2+B_n)^2+\tfrac18EA_n^4.
\]
Finalmente,
\[
(A_n^2+B_n)^2\le2A_n^4+2B_n^2
\]
produce \(1+\tfrac18=\tfrac98\). La constante es válida; el argumento no demuestra que sea óptima.

**(d) Momentos.** Como los scores son independientes y centrados, en la expansión de \(EA_n^4\) sólo sobreviven los términos con cuatro índices iguales o dos parejas:
\[
EA_n^4=nm_4+6\binom n2J^2
      =nm_4+3n(n-1)J^2.
\]
Para \(n\ge1\), esto es menor o igual que \(n^2(m_4+3J^2)\).

Asimismo,
\[
EB_n^2=n\operatorname{Var}(b)+n^2(Eb)^2
      =n\operatorname{Var}(b)+n^2J^2
      \le n^2Eb^2.
\]
Ambas fórmulas y ambas cotas son correctas. Junto con (c) prueban exactamente la constante \(c(\tau)\) de §2.

**(e) Paso al módulo.** Correcto: para cada \(n\) el espacio tiene dimensión finita y las componentes son \(C^2\), de modo que se aplica el teorema fundamental del cálculo y la desigualdad triangular para la integral.

Que \(K\) sea un intervalo garantiza que todo el segmento entre \(\tau\) y \(\tau+h\) queda donde se controla \(\ddot s_n\). Para un compacto arbitrario, la cota sólo sobre \(K\) no basta para este argumento. Podría sustituirse por una cota sobre su envolvente convexa. La nota ya incluye la hipótesis adecuada.

**§4. Cálculo gaussiano y alcance.** Sea \(\psi_\tau=\sqrt{p_\tau^{\otimes n}}\) y \(S=\sum_i(x_i-\tau)\). Entonces
\[
\dot\psi_\tau=\tfrac12S\psi_\tau,\qquad
\ddot\psi_\tau=(S^2/4-n/2)\psi_\tau.
\]
Bajo \(P_\tau\), \(ES^2=n\), \(ES^4=3n^2\), por lo que
\[
\|\ddot\psi_\tau\|^2=\frac{3n^2}{16}.
\]
Además, la afinidad es \(e^{-nh^2/8}\); derivándola en ambos parámetros,
\[
\|\dot\psi_{\tau+h}-\dot\psi_\tau\|^2
=\frac n2\left[1-\left(1-\frac{nh^2}{4}\right)e^{-nh^2/8}\right].
\]
Por tanto, si \(\sqrt n\,|h|\to0\),
\[
\|\dot\psi_{\tau+h}-\dot\psi_\tau\|
=\frac{\sqrt3}{4}n|h|\,[1+O(nh^2)].
\]
Esto verifica el orden \(n\eta\) del módulo **en ese régimen local**, para un intervalo fijo no degenerado. No es una equivalencia válida para cualquier \(\eta\): el módulo está acotado por \(\sqrt n\).

Para el canal de la nota, **la optimalidad no está demostrada**. Falta especificar \(\phi\) y controlar inferiormente la información conservada. Un contraejemplo admisible es que \(\phi\) ordene únicamente los \(V_i\): entonces todas las permutaciones tienen probabilidad \(1/n!\), independiente de \(\tau\), y el módulo es cero.

Como comprobación adicional, cualquier canal satisface
\[
\langle s_n,\ddot s_n\rangle=-\|\dot s_n\|^2=-I_n^\Pi/4,
\qquad
\|\ddot s_n\|\ge I_n^\Pi/4.
\]
Una cota inferior \(I_n^\Pi\gtrsim n\) demostraría que el coeficiente local de Lipschitz tiene necesariamente orden \(n\). La nota sólo aporta la cota superior.

Las salvedades son, pues:

1. Precisar el régimen de la comparación gaussiana.
2. No trasladar su optimalidad al canal sin información adicional sobre \(\phi\).
3. «El resultado no da QMD uniforme» es correcto como limitación de esta cota; no demuestra imposibilidad para el canal ni impide LAN mediante otros argumentos.