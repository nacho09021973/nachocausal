<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 783f078e04c4a82d48968494714aefbb25acc81b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 fa4f0575278ab314cd659ff67b13395712b70abef383df903fbf0afe37ea9e97; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.6, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.41 (4220f3b224a6) [stable])
grok.json sha256 1ebec250aa8db544826d7a0f0412138c407f6468f8acf1abb8553c2c6339f0fd
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-10-10T18:31:01Z  fin: 2026-10-10T18:40:44Z
documento: /home/adnac/nachocausal/dev/S4W_5LAYER_INDEPENDENT_AUDIT_2026-10-10.md ; último commit observado: sin versionar ; sha256 de la copia enviada 7322457f4c2c215ed116702582bd6316cb5686db046dd6e2a2d830fe7b63ae61
documento: /home/adnac/nachocausal/dev/S4W_5LAYER_KRETSCHMANN_CANDIDATE.md ; último commit observado: 15eb7a5 ; sha256 de la copia enviada 44795104c8bd8c0af87c2af48f5ca494d62c86e0e4ba04af3691c896f30cb36f
documento: /home/adnac/nachocausal/revisiones/2026-10-10-s4w-auditoria/pfeiffer2022_higher_curvature_terms_causal_sets_MSc.pdf ; último commit observado: sin versionar ; sha256 de la copia enviada 39beffd1f8696be66c35a4285dcd90cd61ce87b143cc7ccc69743d79078b7eba
entrada_grok.txt sha256 49cbb423966c7071ea5cc93119810e848188373b5128fbadabbacd2c2e8982e9
respuesta sha256 f6409b9ac434f2c63a1cc4bc3a441e2f5969618acbd39174ed80f574e4ed01bd
-->

La unicidad por covariancia, dimensión y paridad clasifica escalares locales hechos con la métrica. En vacío 4D esa base se reduce a \(C_{abcd}C^{abcd}\). El objeto que el candidato escribe en su §7 es otro: el volumen de un diamante de Alexandrov con eje \(U\) fijo, tomado de Wang. Ese volumen mezcla el invariante \(K\) con la densidad de superenergía \(W=T_{abcd}U^aU^bU^cU^d\). Con las identificaciones \(K=8(E^2-B^2)\), \(W=E^2+B^2\), \(B^2=H^2/2\) se verifica

\[
2032\,E^2+360\,H^2=82K+1376W,
\]

porque \(E^2=W/2+K/16\), \(B^2=W/2-K/16\) y \(H^2=2B^2\). \(W\) es escalar de dimensión cuatro independiente de \(K\); entra con coeficiente ~17 veces mayor. El atajo «luego la corrección es \(C^2\)» aplicado a ese diamante es inválido, y especializar \(H=0\) en el tétrada estático descarta el término dominante del integrando. Eso es F3/F4.

La vía de que la integral sobre \(U_y\) colapse a un invariante existe como posibilidad: el operador discreto se define por orden y recuento, sin marco preferido, y un funcional local Lorentz-invariante del jet métrico en \(x\) tendría que ser múltiplo de \(C^2\). Esa vía es el cálculo que la auditoría deja abierto en R6''. El promedio angular a rapidez fija ya calculado para Schwarzschild, \(\langle W\rangle=(6/5)(16\gamma^4-12\gamma^2+1)\), depende de \(\gamma\); contraer esa densidad con el núcleo de Poisson no está hecho. Una posibilidad no calculada no autoriza el atajo de unicidad ni a congelar \(U\). \(U_y\) rompe el argumento de estructura tal como se usó. D_COVARIANT_STRUCTURE = FAIL se sostiene.

En Pfeiffer, \(\lambda=l+(2/d)(l+1)\) sale de la geometría de W2: \(V=U^{d/2}f_0+U^{d/2+1}f_1\), el cambio \(x=U^{d/2}\) y el jacobiano \(\propto x^{2/d-1}\,dx\). Ese \(d\) es la dimensión del espacio-tiempo. De ahí \(d(l-\lambda)=-2(l+1)\) para cualquier número de raíces. El factor

\[
A_{\lambda,l}(n)=\prod_{j=0}^n\bigl(d(l-\lambda)+2j+2\bigr)=\prod_{j=0}^n 2(j-l)
\]

es el producto de las \(n+1\) raíces de \(O_{2n}=(d\rho\partial_\rho+2)\cdots(d\rho\partial_\rho+2n+2)/[2^{n+1}(n+1)!]\). El apéndice A prueba la acción sobre \(\gamma(\lambda,b\rho)/\rho^{\lambda-l}\) por inducción en \(n\), sin imponer \(n=\lfloor d/2\rfloor\): cada factor nuevo multiplica \(A\) por \(d(l-\lambda)+2(n+1)+2\). Luego \(A=0\) si y solo si \(l\le n\) (\(l\) entero \(\ge 0\)).

En \(d=4\) el candidato conserva esa medida, esa \(\lambda\) y el \(d\) de \(d\rho\partial_\rho=4\rho\partial_\rho\). Solo alarga el producto a \(n=3\) (cuatro raíces, el \(O_6\) de Dowker–Glaser evaluado con \(H_{\mathrm{DG}}=4\rho\partial_\rho\)). Entonces \(A=0\) para \(l=0,1,2,3\), el primer \(l\) vivo es 4 y la contribución de W2 a \(\bar B\) es \(\rho^{1-2l/d}=\rho^{-1}\). La fila \(n=2\) reproduce el \(O(\rho^{-2/d})\) publicado. La normalización \(2^{n+1}(n+1)!\) cambia constantes, no los ceros. (h1)–(h2) son las hipótesis literales de Pfeiffer §3.3. (h3) es inferencia y es legítima. F2 cae; \(B_{W2}=\mathrm{PASS\_CONDITIONAL}\) se sostiene.

F1 está bien planteada frente a la forma \(o(\rho^{-1/2})\) del §7 del candidato: \(\ln\rho\cdot\rho^{-1/2}\) no es \(o(\rho^{-1/2})\), y BBD declaran ese resto para W1 curvo con el operador de tres raíces. El \(A\) de Pfeiffer §3.3 actúa en W2 y no limpia F1. En W1 hay otro factor \(A_{\kappa+1,l}(n)=\prod_{\zeta=0}^n 2(\zeta-k)\); con \(n=3\) anula \(k\le 3\). Además \((H+s)(\ln\rho\cdot\rho^{-s})=\rho^{-s}\), de modo que una raíz extra no borra logaritmos como borra potencias. Si esos logs —y el propio canal \(y^4\) de \(C^2\), que puede ocupar \(k=3\)— caen o sobreviven con cuatro raíces es R6', abierto. El §3.3 de la auditoría declara incompatibilidad estructural con el resto publicado; el §8 rev.2 lo deja abierto. Vale el segundo.

El token AUDIT_REQUIRES_MAJOR_FIX se sostiene: el álgebra de cinco capas está reproducida y el operador es GCD con límite \(\Box-R/2\); el estimador con coeficiente \(-73\sqrt{6}/(1575\pi)\) no está determinado. F3 y F4 se mantienen. La línea del operador queda reabierta en el sentido estrecho de W2; el estimador físico sigue sin definición sin prescripción extra.

Defectos de la auditoría, ninguno de los cuales revoca el token. La caja de §6.4 deja \(E_{\mathrm{PRIOR\_ART}}\) con «PFEIFFER_2022_SIN_COMPROBAR» mientras §6.3 lo da por leído y despejado: resto de rev.1. La tabla de §2.3 escribe \(n=\lceil d/2\rceil\); Pfeiffer usa \(n=\lfloor d/2\rfloor\) (coincide en \(d=4\)). El §3.3 trata el resto log de BBD como si aplicara ya a \(\widehat{\mathcal O}_*\); el §8 lo corrige. «La construcción no es \(U\)-libre» nombra al operador discreto, que está definido por orden y recuento; quien lleva \(U\) es el integrando de Wang. El fallo de la afirmación 1 se mantiene. La auditoría no examina la cara W1 de (h3): \(A_{\kappa+1,l}(n=3)\) puede anular el canal \(k=3\) donde entran a la vez el resto log y el \(y^4\) de \(C^2\). R6' pregunta solo por los logs. El enunciado de que la quinta capa separa W2 del orden \(\rho^{-1/2}\) local queda condicionado también a que ese canal local sobreviva.

```
J1_VEREDICTO = CORRECTA
La unicidad métrica no se aplica al diamante de Wang con eje U_y, donde W es independiente de C² y dominante (82K+1376W). La vía de que la integral sobre direcciones colapse a un invariante es el cálculo abierto R6'', no una disolución del atajo. U_y rompe la afirmación 1 tal como se usó.

J2_VEREDICTO = LEGITIMA
A_{λ,l}(n) y la inducción del apéndice A dependen de n como número de raíces y de d solo vía λ y vía dρ∂_ρ. En d=4 el candidato conserva medida, λ y d, y solo alarga n de 2 a 3; A=0 ⇔ l≤n da W2 = O(ρ^{-1}). (h3) es inferencia directa de (3.28), no un salto oculto.

VEREDICTO_GLOBAL_DE_LA_AUDITORIA = CONFIRMADA_CON_CORRECCIONES
AUDIT_REQUIRES_MAJOR_FIX se sostiene: álgebra PASS, estimador no determinado, F2 cae con (h3) legítima, F1 abierta, F3 y F4 en pie. Las correcciones son de formulación y de un hueco W1 en el alcance de (h3), no de token.

DEFECTOS_ENCONTRADOS =
1. Resto de rev.1 en la caja de §6.4 («PFEIFFER_2022_SIN_COMPROBAR») contradice §6.3.
2. n=⌈d/2⌉ en §2.3; Pfeiffer usa ⌊d/2⌋ (inocuo en d=4).
3. §3.3 declara incompatibilidad estructural de F1 con el resto de BBD; §8 rev.2 lo deja abierto para cuatro raíces. Vale §8.
4. «La construcción no es U-libre» atribuye al operador discreto lo que es propiedad del integrando.
5. No se examina que A_{κ+1,l}(n=3) en W1 (Pfeiffer §3.4) puede anular el canal k=3, compartido por el resto log y por el y^4 de C²; R6' pregunta solo por logs, y la «separación de un orden» de rev.2 queda condicionada a que ese canal local sobreviva.
```
