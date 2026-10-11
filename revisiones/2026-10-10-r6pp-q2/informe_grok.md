<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 783f078e04c4a82d48968494714aefbb25acc81b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 fa4f0575278ab314cd659ff67b13395712b70abef383df903fbf0afe37ea9e97; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.6, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.41 (4220f3b224a6) [stable])
grok.json sha256 4b488bc94e3da41ea11dcd60908125ba4b2717393409ef37ed41c3d8ddfaae98
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-10-10T20:00:26Z  fin: 2026-10-10T20:15:29Z
documento: /home/adnac/nachocausal/dev/S4W_R6PP_Q2_WEYL_COEFFICIENT_2026-10-10.md ; último commit observado: sin versionar ; sha256 de la copia enviada 1c34fad13ad259575a5c363dea786a50a3fa7f6d8a266aee3ef1fab71a4d4c75
documento: /home/adnac/nachocausal/dev/S4W_R6PRIMEPRIME_NOGO_2026-10-10.md ; último commit observado: 30f7fda ; sha256 de la copia enviada cd015afcbb0ddab460d98f2b44b305bca754cc8a092145aebca20a391124106e
documento: /home/adnac/nachocausal/dev/S4W_R6PRIME_W1_CHANNEL_2026-10-10.md ; último commit observado: 30f7fda ; sha256 de la copia enviada 0a9a439f671ccab4201b9826e7707bfac552042d2e6d25e8ee2bb8dff760d02f
documento: /home/adnac/nachocausal/dev/S4W_5LAYER_INDEPENDENT_AUDIT_2026-10-10.md ; último commit observado: 1e03a54 ; sha256 de la copia enviada f68540d935e1b7b54e2d5986f5cb7f3ef2027191619e2ae7b8b4d3777e16d056
documento: /home/adnac/nachocausal/biblioteca/pfeiffer2022_higher_curvature_terms_causal_sets_MSc.pdf ; último commit observado: sin versionar ; sha256 de la copia enviada 39beffd1f8696be66c35a4285dcd90cd61ce87b143cc7ccc69743d79078b7eba
entrada_grok.txt sha256 59de83e14f5f933c42b914894398386a93b3a36368bcf045e3fd42fde5b03f2d
respuesta sha256 7d71981d3452692663797ab23b9cff7042067848c6562461dd0b5dc4501a4902
-->

El coeficiente \(-73\sqrt{6}/(1575\pi)\) sale de álgebra independiente, sin ajuste. P1 se reobtiene de la descomposición de Bel-Robinson y de la identidad de Weyl en 4D; P2 es una identidad polinomial; P3 y P4 siguen por aritmética directa a partir de las transcripciones ya auditadas de Wang y de la normalización controlada en el canal \((2,2)\).

**P1.** En el marco de RNC, \(T_{abcd}\) es simétrico y sin traza. Con \(t=(u+v)/\sqrt{2}\), \(r=(v-u)/\sqrt{2}\) y los promedios \(\langle n^in^j\rangle=(4\pi/3)\delta^{ij}\), \(\langle n^4\rangle=(4\pi/15)(\delta\delta+\cdots)\), queda
\[\int T_{abcd}y^ay^by^cy^d\,d\Omega=\frac{16\pi}{5}W(u^4+u^3v+u^2v^2+uv^3+v^4).\]
La contracción mareal \(Q=C_{\alpha\mu\beta\nu}C^{\alpha\rho\beta\sigma}y^\mu y^\nu y^\rho y^\sigma\) cumple \(Q=\frac12 T(y^4)+\frac{K}{16}(y\cdot y)^2\) y \((y\cdot y)^2=4u^2v^2\), de modo que
\[\int Q\,d\Omega=\frac{8\pi}{5}W(u^4+\cdots+v^4)+\pi K\,u^2v^2.\]
Control en el eje (\(r=0\), \(W=E^2\), \(K=8E^2\)): ambos lados dan \(16\pi E^2 u^4\). Toda cuártica isótropa construida con Weyl² es combinación de \(T(y^4)\) y \(K(y\cdot y)^2\); la parte \(W\) es uniforme sobre los cinco monomios y el único exceso no uniforme es \(\pi K u^2v^2\).

**P2.** La medida \((v-u)^2/2\) multiplica esos polinomios antes de integrar en \((u,v)\). Al canal \(u^3v^3\) (vía (i)) solo alimentan \(u^3v\cdot v^2\), \(u^2v^2\cdot(-2uv)\) y \(uv^3\cdot u^2\), con pesos \(+\frac12,-1,+\frac12\). Al canal \(u^5v^5\) (vía (ii′), tras el \(u^2v^2\) de \(V_0\)) ocurre lo mismo. Los tres pesos suman cero y aniquilan cualquier reparto uniforme. Los monomios \(u^4\) y \(v^4\) no entran en la diagonal; las particiones \((4,2)\) y equivalentes viven en \(\rho^{-1}\) y \(A_{\kappa+1,l}(n=3)=0\) las deja fuera de \(\rho^{-1/2}\). \(T_{abcd}y^ay^by^cy^d\) es polinomio, acotado en el \(W1\) compacto (cara nula \(u=0\) incluida). La cancelación es identidad en \((u,v)\); \(\gamma\to\infty\) no la altera.

**P3.** Vía (i): \(Q_\Omega\times(v-u)^2/2\) da \(-\pi K\) en \(u^3v^3\); el \(-1/180\) de Wang (76)–(77) produce \(+\pi K/180\). Parte \(W\): \(4/5-8/5+4/5=0\). Vía (ii′): con \(l_W=\sqrt{uv/2}\) se tiene \(V_\mathrm{plano}=\pi u^2v^2/6=V_0\) y \(\varepsilon_2=u^2v^2(41K+688W)/151200\). Promoviendo \(W(U_y)=T(y^4)/(4u^2v^2)\) el término \(T\) es uniforme y se cancela. El resto \(41K\), con \(\int d\Omega=4\pi\), \(V_0=\pi/6\,u^2v^2\), medida \((v-u)^2/2\) y el \(-2uv\) diagonal, más el \((-1)^l\) de la exponencial, da \(+41\pi^2 K/226800\) en \(u^5v^5\).

Wang (79) y \(V(x,y)\) de Pfeiffer son el volumen del mismo intervalo de Alexandrov. Evaluar Riemann en el centro del diamante o en \(x\) difiere por \(\nabla\mathrm{Riem}\), fuera de la truncación algebraica \(R^2\) usada en toda la línea.

**P4.** Con \(s=c_4\rho\), \(c_4=\pi/6\), \(\hat O_*[\rho^0 G_1]=-1/(2s^2)\), \(\hat O_*[\rho^1 G_2]=-1/(c_4 s^2)\), simetrización \(1/2\) (integrando simétrico en \(u\leftrightarrow v\)) y jacobiano \(1/4\) (\(u^3v^3\,du\,dv=\frac14 xy\,dx\,dy\), \(u^5v^5\,du\,dv=\frac14 x^2y^2\,dx\,dy\)):

- vía (i): \(\rho^{3/2}\cdot(8\sqrt{6}/3)\cdot(1/8)\cdot(\pi K/180)\cdot(-1/(2s^2))=-\sqrt{6}K/(30\pi\sqrt{\rho})=-105\sqrt{6}K/(3150\pi\sqrt{\rho})\);
- vía (ii′): el mismo prefactor por \(41\pi^2 K/226800\) y \(-1/(c_4 s^2)\) da \(-41\sqrt{6}K/(3150\pi\sqrt{\rho})\).

Suma: \(-(105+41)/3150=-73/1575\). El \(41\) de Wang y el \(180\) de \(\sqrt{-g}\) fijan el entero \(73\) sin parámetro libre. El prefactor \(8\sqrt{6}/3\) es el del control \(\square-R/2\) en el canal \((2,2)\).

A orden algebraico \(R^2\) en vacío las dos vías agotan \(\alpha+\beta=4\) par: \(l=0\) del \(y^4\) de \(\sqrt{-g}\) y \(l=1\) de \(\varepsilon_2\). Los \(\alpha+\beta\) impares mueren por paridad; \(l\ge 2\) es \(R^4\); \(W2\) queda en \(O(\rho^{-1})\) con cinco capas. La exhaustividad más allá de esa clasificación sigue siendo la del autor (§6).

§5 respeta la frontera de claims (varianza, realización por realización, horizonte, Page–Shoom, reconstrucción, cono causal, prioridad). Lo calculado es \(E[B_*1]\). La frase de §0 sobre el estimador normalizado se refiere a ese valor medio.

Laguna: Wang arXiv:1904.01034 no está en el lote; (76)–(77) y (79) se toman de la transcripción ya confirmada en la auditoría y en N1/N2.

```
P1_FORMAS_CUARTICAS = CORRECTA  + identidad de Bel-Robinson + Q = T/2 + K(y·y)²/16; W uniforme, exceso π K u²v²
P2_CANCELACION      = CORRECTA  + (v-u)² aniquila los tres monomios medios; u⁴, v⁴ no entran en la diagonal; T y⁴ polinomio en W1
P3_COEFICIENTES     = CORRECTA  + +πK/180 y 41π²K/226800 siguen de P1, Wang (79) transcrito y la medida con 4π
P4_ENSAMBLADO       = CORRECTA  + aritmética exacta con ρ^l interior, 1/2, 1/4 y Ô_* calibrado en (2,2)
VEREDICTO_Q2 = CONFIRMADO
DEFECTOS_ENCONTRADOS = LAGUNA Wang 1904.01034 no adjunto (se hereda la transcripción auditada); recuento de vías a R² sin prueba de exhaustividad (§6); truncación Riemann congelado (∇Riem fuera de orden) no declarada como tal
```
