<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 783f078e04c4a82d48968494714aefbb25acc81b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 fa4f0575278ab314cd659ff67b13395712b70abef383df903fbf0afe37ea9e97; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.162.1)
inicio: 2026-10-10T20:30:07Z  fin: 2026-10-10T20:33:21Z
documento: /home/adnac/nachocausal/dev/S4W_R6PP_Q2_WEYL_COEFFICIENT_2026-10-10.md ; último commit observado: 0c3f07f ; sha256 de la copia enviada 07fe49a784c432452efec92d393c45a70b2832269b9574ab7ec91893813779b8
documento: /home/adnac/nachocausal/dev/S4W_R6PRIMEPRIME_NOGO_2026-10-10.md ; último commit observado: 30f7fda ; sha256 de la copia enviada cd015afcbb0ddab460d98f2b44b305bca754cc8a092145aebca20a391124106e
documento: /home/adnac/nachocausal/dev/S4W_R6PRIME_W1_CHANNEL_2026-10-10.md ; último commit observado: 30f7fda ; sha256 de la copia enviada 0a9a439f671ccab4201b9826e7707bfac552042d2e6d25e8ee2bb8dff760d02f
documento: /home/adnac/nachocausal/dev/S4W_5LAYER_INDEPENDENT_AUDIT_2026-10-10.md ; último commit observado: 1e03a54 ; sha256 de la copia enviada f68540d935e1b7b54e2d5986f5cb7f3ef2027191619e2ae7b8b4d3777e16d056
documento: /home/adnac/nachocausal/biblioteca/derived-md/Wang_2019_Geometry_Small_Causal_Diamonds_arXiv1904.01034.md ; último commit observado: sin versionar ; sha256 de la copia enviada 5c466a127a55724b6ad8a2ee9e06ceb2efd1f4d63ab1e6d8d249742478c2275d
documento: /home/adnac/nachocausal/biblioteca/pfeiffer2022_higher_curvature_terms_causal_sets_MSc.pdf ; último commit observado: sin versionar ; sha256 de la copia enviada 39beffd1f8696be66c35a4285dcd90cd61ce87b143cc7ccc69743d79078b7eba
entrada_astra.txt sha256 fc7468d71cebcd4ecfaef37d4243dce77dd6d0adc7b9531767cbb5c5a7487674
respuesta sha256 598ee9b8076dc1ddf65c587673b820b90e1a8a3916b8b8a14bd533b91138c8ed
-->

El coeficiente **algebraico local** se reproduce: \(-73\sqrt6/(1575\pi)\). La cancelación de \(W\) en el canal de orden \(\rho^{-1/2}\) es correcta. No encuentro un ajuste numérico necesario para obtenerlo.

El documento necesita correcciones: contiene un control aritmético falso, describe la cancelación con demasiado alcance y presenta como establecida una fórmula para el valor medio completo cuyo control de restos no está demostrado por los argumentos adjuntos. Hay además un problema material en la justificación heredada de \(W_2\).

**P0.** La lectura de los índices es correcta. En la extracción de Wang (76) aparecen intercalados:
\[
C^\gamma{}_\mu{}^\alpha{}_\nu C_{\gamma\rho\alpha\sigma}.
\]
La ecuación (6) confirma la estructura:
\[
\eta^{\alpha\beta}R^\gamma{}_{\mu\alpha\nu}
R_{\gamma\rho\beta\sigma}.
\]
Las coordenadas ocupan los slots segundo y cuarto; no contraen entre sí un par antisimétrico.

Se puede verificar también el coeficiente del determinante directamente desde (6). En vacío, escribiendo \(g=\eta+h_2+h_4+\cdots\), las contribuciones algebraicas son
\[
\frac12\operatorname{tr}h_4=\frac1{45}Q,\qquad
-\frac14\operatorname{tr}(h_2^2)=-\frac1{36}Q.
\]
Su suma es \(-Q/180\), como en (76). La objeción de nulidad por antisimetría queda descartada.

**P1.** Ambas formas cuárticas son correctas para \(E,B\) generales.

Póngase \(t=-(u+v)/\sqrt2\), \(r=(v-u)/\sqrt2\). La simetría completa y la ausencia de trazas del Bel–Robinson en cuatro dimensiones, junto con las integrales angulares (7)–(8), dan
\[
\int d\Omega\,T(y^4)
=4\pi W\left(t^4+2t^2r^2+\frac{r^4}{5}\right)
=\frac{16\pi}{5}W\,S_4,
\]
donde
\[
S_4=u^4+u^3v+u^2v^2+uv^3+v^4.
\]
Aquí \(W\) corresponde al marco fijo utilizado para definir \(t,r\); la dependencia de \(U_y\) está incorporada en \(T(y^4)\).

La identidad utilizada en §7.2 tiene la normalización correcta:
\[
Q(y)=\frac12T(y^4)+\frac K{16}(y\cdot y)^2.
\]
Como \((y\cdot y)^2=4u^2v^2\), resulta
\[
\int d\Omega\,Q
=\frac{8\pi}{5}W\,S_4+\pi K u^2v^2.
\]
No se ha supuesto \(B=0\).

El control de §7.1, sin embargo, está mal escrito. Para \(u=v\),
\[
4\pi E^2(y^0)^4=16\pi E^2u^4,
\]
y
\[
8\pi Wu^4+\pi Ku^4=16\pi E^2u^4.
\]
El resultado correcto es **16**, no 32. La identidad se verifica después de corregir ambas líneas; ese control no constituye la comprobación numérica que el documento dice haber realizado.

**P2.** La cancelación diagonal es legítima, pero multiplicar por la medida no aniquila el polinomio completo. Exactamente,
\[
(v-u)^2S_4=u^6-u^5v-uv^5+v^6.
\]
Desaparecen los coeficientes interiores, incluido \(u^3v^3\). Al multiplicar además por \(u^2v^2\), desaparece también \(u^5v^5\). Esto cuenta todas las contribuciones de las cuárticas consideradas a esos canales.

Los cuatro monomios restantes no son cero. Por tanto, «la medida aniquila cualquier reparto uniforme» debe restringirse a **la proyección sobre el canal relevante**. Tampoco queda demostrado que la contribución de \(W\) al valor medio a densidad finita sea exactamente cero.

La exclusión de una reentrada de esos monomios se puede comprobar sin aceptar la clasificación anterior por autoridad. Para
\[
J_{\kappa\mu}(s)=
\int_0^A dx\int_0^A dz\,x^\kappa z^\mu e^{-sxz},
\qquad \mu>\kappa,
\]
la integral exacta es
\[
J_{\kappa\mu}(s)=
\frac{
A^{\mu-\kappa}s^{-\kappa-1}\gamma(\kappa+1,sA^2)
-
A^{\kappa-\mu}s^{-\mu-1}\gamma(\mu+1,sA^2)
}{\mu-\kappa}.
\]
Con el \(\rho^l\) incluido, sus potencias efectivas son
\(\rho^{-(k+1)/2}\) y \(\rho^{-(m+1)/2}\).
Las raíces del operador eliminan las correspondientes a índices \(0,1,2,3\). Para las particiones no diagonales de \(m+k=6\), la potencia que puede sobrevivir produce, después del prefactor, como máximo \(O(\rho^{-1})\). No reentra en \(\rho^{-1/2}\).

**P3.** La identificación geométrica con Wang es correcta. Su §III define explícitamente el ACD como
\[
I^+(p)\cap I^-(q),
\]
y §VI calcula su volumen **espaciotemporal**, no el volumen de una hipersuperficie. Es el objeto \(V(x,y)\) de Pfeiffer, tomando los mismos vértices.

Wang evalúa la curvatura en el punto medio. Transportarla al extremo \(x\) cambia el término cuadrático mediante términos con derivadas, de grado superior en la separación; no cambia el coeficiente algebraico cuártico. La identificación requiere un intervalo contenido en el entorno normal apropiado.

En (79), para \(d=4\), obtengo directamente
\[
V=\frac{2\pi}{3}l_W^4+
\frac{4\pi l_W^8}{453600}
(2068E^2+360H^2-9D^2).
\]
Usando \(D^2=4E^2\), \(H^2=2B^2\),
\[
\delta V=\frac{\pi l_W^8}{56700}(41K+688W).
\]
La longitud entre vértices es \(2l_W=\sqrt{2uv}\). Por ello,
\[
\epsilon_2=
\frac{41K}{151200}u^2v^2+
\frac{688}{604800}T(y^4).
\]
Coincide con el documento.

Los dos coeficientes diagonales son entonces
\[
[u^3v^3]\left(-\frac{(v-u)^2}{360}\int Q\,d\Omega\right)
=\frac{\pi K}{180},
\]
y
\[
[u^5v^5]\left(
-\frac{(v-u)^2}{2}V_0\int\epsilon_2\,d\Omega
\right)
=\frac{41\pi^2K}{226800}.
\]
En la segunda expresión he separado el factor \(\rho\), que permanece dentro del operador. El signo positivo incluye el **menos de la expansión exponencial**; §3 debería explicitarlo.

**P4.** El ensamblado también es correcto. Las funciones diagonales satisfacen
\[
G_\nu(s)=s^{-\nu-1}
\left[\Gamma(\nu+1)\log(sA^2)-\Gamma'(\nu+1)\right]
+\text{resto exponencial}.
\]
De ahí,
\[
\widehat O_*G_1=-\frac1{2s^2}+\text{resto exponencial},
\qquad
\widehat O_*[\rho G_2]=-\frac1{c_4s^2}+\text{resto exponencial}.
\]
La simetrización introduce \(1/2\): los polinomios aquí utilizados son simétricos bajo \(u\leftrightarrow v\). El cambio a cuadrados introduce otro \(1/4\). No hay duplicación del factor angular, ya incluido en los coeficientes anteriores.

Con \(b_0=8\sqrt6/3\) y \(c_4=\pi/6\), las contribuciones son
\[
-\frac{\sqrt6}{30\pi}K\rho^{-1/2},
\qquad
-\frac{41\sqrt6}{3150\pi}K\rho^{-1/2}.
\]
Su suma da el número anunciado.

El recuento de vías queda cerrado **para el sector algebraico local especificado**. En vacío, las correcciones lineales del determinante y del volumen se anulan. A orden cuadrático quedan el término cuártico del determinante y la inserción lineal de \(\delta V_{R^2}\). Los productos de dos correcciones de volumen empiezan en \(R^4\). Por homogeneidad, ambas vías tienen \(\alpha+\beta=4\).

La justificación por «\(\alpha+\beta\) impar muere por paridad» es falsa en general: la integración angular elimina un número impar de componentes **espaciales**, no un grado total impar. Un término temporal \(t^3\) sobrevive. Esto no añade una vía algebraica \(R^2\), pero invalida ese argumento auxiliar.

También debe corregirse que \(\nabla\nabla\mathrm{Riem}\) sea sencillamente «de otro orden»: aparece al mismo grado cuártico en Wang (6). En vacío exacto, la traza correspondiente del determinante se reduce a derivadas de Ricci y se anula; para el volumen, Wang ya ha tratado las contribuciones pertinentes antes de (79). Esa es la justificación adecuada.

La rapidez no acotada no invalida las integrales **truncadas**. Para \(\tau^2=2uv\),
\[
\tau^4W(U_y)=T(y^4),\qquad l_W^4W(U_y)=\frac1{16}T(y^4).
\]
Las expresiones utilizadas se extienden como polinomios finitos hasta \(u=0\). Con corte fijo, sus integrales y las derivadas finitas en \(\rho\) convergen. La cancelación algebraica puede aplicarse bajo esas integrales.

Esto no convierte automáticamente el resto de Wang, formulado para diamantes pequeños a orientación fija, en una estimación uniforme cuando \(U_y\) se aproxima a una dirección nula. Compactitud de las coordenadas y acotación de un resto expresado en variables de boost son cuestiones diferentes.

Finalmente, hay una laguna material que impide aceptar literalmente §0 y §5. La prueba heredada de \(W_2=O(\rho^{-1})\) utiliza los pasos (3.15)–(3.22) de Pfeiffer, que trasladan valores absolutos y cotas a través de un operador diferencial que **no preserva desigualdades**. La identidad (3.17) no legitima esa operación. Que el factor \(A_{\lambda,l}\) anule la integral de un monomio es correcto; que anule una cota obtenida sustituyendo funciones por sus normas supremas no se sigue.

Las hipótesis heredadas de mera acotación tampoco bastan. Como ejemplo funcional, una amplitud positiva y acotada que contenga \(U^3\log U\), con fase \(V=U^2f_0\), produce
\[
\int U^3\log U\,e^{-\rho f_0U^2}dU
=
-\frac{\log\rho}{4f_0^2\rho^2}
+\frac{\text{constante}}{\rho^2}
+\text{resto exponencial}.
\]
La cuarta raíz transforma ese logaritmo en una contribución de orden \(\rho^{-1/2}\) al operador. Esto demuestra insuficiencia de las hipótesis funcionales citadas; no constituye un contraejemplo geométrico Ricci-flat suave. Una expansión transversal con regularidad suficiente podría reparar la prueba, pero debe proporcionarse.

Por tanto, no está justificado afirmar que «sobreviven sólo los fallos documentales». El coeficiente local calculado no establece por sí solo el resto global \(o(\rho^{-1/2})\), ni define \(B_*1\) sobre un pasado no compacto. Pfeiffer presupone soporte compacto.

El texto sí respeta las prohibiciones sobre varianza, convergencia por realización y detección de horizontes. Su exceso está en promover el cálculo local a una afirmación completa sobre la media. El veredicto siguiente confirma el resultado local de Q2 y exige restringir esa promoción.

```text
P0_INDICES_WANG76   = CORRECTA — los slots contraídos con y pertenecen a pares antisimétricos distintos; Wang (6), (76) y (77) concuerdan.
P1_FORMAS_CUARTICAS = CORRECTA — promedio angular general y normalización de Bel–Robinson correctos; §7.1 contiene un factor 2 erróneo.
P2_CANCELACION     = CORRECTA — exactamente en el canal rho^(-1/2); no aniquila el polinomio ni toda la contribución finita de W.
P3_COEFICIENTES    = CORRECTA — Wang (79) mide el intervalo causal requerido y da ambos coeficientes indicados.
P4_ENSAMBLADO      = CORRECTA — rho^l, signo exponencial, factores 1/2 y 1/4 y normalización reproducen -73 sqrt6/(1575 pi).
VEREDICTO_Q2 = CONFIRMADO_CON_CORRECCIONES
DEFECTOS_ENCONTRADOS =
- §7.1: 32 debe ser 16 en ambas evaluaciones.
- Cancelación descrita con alcance excesivo: sólo desaparece W del canal objetivo.
- §3 omite explicitar el signo negativo de la inserción exponencial.
- Paridad angular confundida con paridad del grado total.
- Orden de las derivadas de curvatura descrito incorrectamente.
- Uniformidad de los restos cerca de u=0 no establecida.
- Justificación heredada de W2 mediante cotas y operador diferencial inválida; requiere reparación.
- Fórmula global para E[B_*1] y cierre de C0 sobreafirmados respecto del cálculo local demostrado.
```