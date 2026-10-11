<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 783f078e04c4a82d48968494714aefbb25acc81b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 fa4f0575278ab314cd659ff67b13395712b70abef383df903fbf0afe37ea9e97; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.162.1)
inicio: 2026-10-10T21:22:54Z  fin: 2026-10-10T21:25:19Z
documento: /home/adnac/nachocausal/dev/S4W_NOTA_DE_CIERRE_2026-10-10.md ; último commit observado: 82ebbc1 ; sha256 de la copia enviada f3b45b2d3dc2f461a6db3fd00130ab38848bf05e1787df35cd7705ff55bb8069
documento: /home/adnac/nachocausal/dev/S4W_5LAYER_KRETSCHMANN_CANDIDATE.md ; último commit observado: 82ebbc1 ; sha256 de la copia enviada ed93902419c71fc926738fc6debdf8c29effaecaf7b84fcca0a155a035ebb2d3
documento: /home/adnac/nachocausal/dev/S4W_5LAYER_INDEPENDENT_AUDIT_2026-10-10.md ; último commit observado: 1e03a54 ; sha256 de la copia enviada f68540d935e1b7b54e2d5986f5cb7f3ef2027191619e2ae7b8b4d3777e16d056
documento: /home/adnac/nachocausal/dev/S4W_R6PP_Q2_WEYL_COEFFICIENT_2026-10-10.md ; último commit observado: 38cfd39 ; sha256 de la copia enviada fcaaa02929fcbfd1122a6750cef5c6536d20b16da101285277270341bc65ce73
documento: /home/adnac/nachocausal/biblioteca/derived-md/Wang_2019_Geometry_Small_Causal_Diamonds_arXiv1904.01034.md ; último commit observado: sin versionar ; sha256 de la copia enviada 5c466a127a55724b6ad8a2ee9e06ceb2efd1f4d63ab1e6d8d249742478c2275d
documento: /home/adnac/nachocausal/biblioteca/derived-md/Belenchia_Benincasa_Dowker_2016_Continuum_Limit_4D_arXiv1510.04656.md ; último commit observado: sin versionar ; sha256 de la copia enviada e04e24f5d393a1431aaac9f6fcdc6beabaea8cb73b51d022682a3a9ce3559e2f
documento: /home/adnac/nachocausal/biblioteca/derived-md/Belenchia_2016_Universal_GCD_Curved_arXiv1510.04665.md ; último commit observado: sin versionar ; sha256 de la copia enviada ef7693c767e80c113eff9c9b41fb482e4dcd01b57229f8179ff3d9cd18635900
documento: /home/adnac/nachocausal/biblioteca/derived-md/Causal_Set_dAlembertians_Various_Dimensions_arXiv1305.2588.md ; último commit observado: sin versionar ; sha256 de la copia enviada 15384e9de0fe1ee5eda6639e2089645b23b8c42750cc04692b47ee1fdca3c9ee
documento: /home/adnac/nachocausal/biblioteca/pfeiffer2022_higher_curvature_terms_causal_sets_MSc.pdf ; último commit observado: sin versionar ; sha256 de la copia enviada 39beffd1f8696be66c35a4285dcd90cd61ce87b143cc7ccc69743d79078b7eba
entrada_astra.txt sha256 48a6cd4222e681c51fdd96e61a5bbfee2ced47b9961f69b4b4e33f031fda081a
respuesta sha256 1bbe52ac9036e2c2bcfd7c1006aef470876485e3259735311be7f61e17dcb1aa
-->

El coeficiente local se sostiene. La objeción al argumento de Pfeiffer también. La nota necesita correcciones de alcance, de atribución bibliográfica y de historia de la revisión antes de quedar como registro final.

1. **La distinción entre BBD y Pfeiffer es correcta para los pasos señalados.**

En BBD (25) la desigualdad se obtiene sobre el integrando de \(I_{2,3}\):
\[
|P(z)|\leq 1+9z+8z^2+\tfrac43z^3,\qquad z=\sigma u^2v^2.
\]
Después se representa ese kernel positivo mediante
\[
1-9H_1+8H_2-\tfrac43H_3.
\]
Esto es una identidad aplicada a la integral que ya sirve de cota. No es aplicar el operador original de (15) a ambos lados de una desigualdad.

El orden de esa cota procede de
\[
\sigma^j\int_0^{a^2/v}u^{3+2j}e^{-\sigma v^2u^2}\,du
=O(\sigma^{-2}),
\]
uniformemente para \(v\) en el intervalo compacto separado de cero. BBD lo dicen explícitamente después de (26): la expansión transversal ha llegado suficientemente lejos.

Hay dos precisiones necesarias:

- La ec. (25) pertenece al caso **plano** y acota el **resto \(I_{2,3}\)**. Para justificar el resultado en espacio curvo hay que citar III.B, especialmente (68)–(75).
- Las raíces sí intervienen en el tratamiento de los términos explícitos de orden inferior. En el caso curvo, BBD lo indican después de (69). «Sale del desarrollo en \(u\), no de raíces» es correcto para la cota del resto; no describe por sí solo toda la demostración sobre \(W2\).

En Pfeiffer el defecto está efectivamente en el original suministrado. En (3.18)–(3.19) sustituye la amplitud por normas supremas manteniendo \(O_d\) sobre la integral restante. En (3.22) vuelve a hacerlo con \(f_1^l\). Después utiliza las raíces del mismo \(O_d\) en (3.27)–(3.32). La identidad invocada en (3.17) no permite estas operaciones.

Puede comprobarse sin depender de la colocación de las barras en la extracción del PDF. En \(d=4\), con fase \(fU^2\), \(f>0\), intervalo \(0\leq U\leq L\) y amplitud positiva y suave \(A(U)=1+\varepsilon U^3\),
\[
\widehat O_{BD}\int_0^L A(U)e^{-\rho fU^2}\,dU
=-\frac{\varepsilon}{2f^2\rho^2}
+\text{términos exponencialmente pequeños}.
\]
En cambio,
\[
\widehat O_{BD}\int_0^L e^{-\rho fU^2}\,dU
\]
es exponencialmente pequeño. Sustituir \(A\) por su norma suprema dentro de esa operación pierde una contribución algebraica. Tomar un valor absoluto al final no lo repara.

La fórmula exacta para \(A_{\lambda,l}(n)\) puede ser correcta y su uso como cota seguir siendo inválido. La nota distingue bien esas dos cosas. También restringe correctamente el ejemplo con \(U^3\log U\): demuestra insuficiencia de la mera acotación, no un contraejemplo geométrico suave.

2. **El número local y la cancelación en el canal solicitado son correctos. Hay sobreafirmaciones auxiliares en §1.**

La reducción de Wang (79) en cuatro dimensiones da
\[
2032E^2+360H^2=82K+1376W,
\]
con \(H^2=2B^2\), \(K=8(E^2-B^2)\) y \(W=E^2+B^2\). La identidad
\[
Q(y)=\tfrac12T(y,y,y,y)+\tfrac{K}{16}(y\cdot y)^2
\]
es consistente con esa convención y con Wang (2), (5) y (76).

La cancelación relevante se comprueba mediante
\[
(v-u)^2(u^4+u^3v+u^2v^2+uv^3+v^4)
=u^6-u^5v-uv^5+v^6.
\]
Desaparece el monomio diagonal; no desaparece toda la contribución direccional. La nota de cierre acota expresamente la cancelación a ese canal y evita aquí el exceso del documento 4.

La normalización puede comprobarse con las integrales diagonales de BBD (94), sin adoptar los veredictos de las revisiones. Con \(s=\pi\rho/6\),
\[
\widehat O_*Z_{3,3}=-\frac1{16s^2},\qquad
\widehat O_*[\rho Z_{5,5}]=-\frac1{8(\pi/6)s^2},
\]
hasta términos exponencialmente pequeños. Con los coeficientes del documento 4 resultan
\[
-\frac{\sqrt6}{30\pi}K\rho^{-1/2},
\qquad
-\frac{41\sqrt6}{3150\pi}K\rho^{-1/2}.
\]
Su suma es la declarada. Esto confirma el coeficiente algebraico local, sin establecer el resto global.

Pero «su teorema de universalidad da límite local \(\Box-R/2\)» omite condiciones materiales. Belenchia §2.2 y §4 formulan expresamente el resultado **cuando existe el límite local**, y restringen su prueba al soporte compacto pequeño respecto de la escala de curvatura. La extensión que incluye las regiones lejanas para todos los operadores no mínimos se presenta como conjetura respaldada, no como teorema general demostrado. Cumplir (3a)–(3c) establece la pertenencia a la familia y la normalización; no elimina esas condiciones.

También está inflada la certificación «confirmado por tres casas». El documento 4 registra dos revisores favorables y uno contrario cuya objeción fue refutada. Refutar su objeción no convierte su informe en una confirmación independiente. Si la tercera casa es la autora del cálculo, debe identificarse así. Además, rederivar el \(-1/180\) verifica un ingrediente, no constituye por sí solo una tercera derivación completa del coeficiente.

3. **La ausencia de un resultado global está bien declarada; algunas formulaciones convierten falta de prueba en imposibilidad.**

Es fiel mantener abiertos \(F1\), \(C0\), el resto global y el estimador. Es fiel reconocer el problema de uniformidad cuando \(u\to0\): compacidad en coordenadas no implica rapidez acotada.

La extensión de la cota conservadora de BBD a cinco capas es justificable bajo sus hipótesis. En sus términos de tipo (70), cada derivada adicional produce contribuciones cuya escala es
\[
\rho^{q+j}\int U^{n+3q+2j}e^{-\rho f_0U^2}\,dU
=O\!\left(\rho^{-(n+q+1)/2}\right).
\]
La cuarta derivada no empeora ese orden. El resto de la serie exponencial admite el mismo tipo de tratamiento. Así se conserva una cota \(O(\rho^{-1/2})\) tras el prefactor, sin usar raíces sobre desigualdades.

Pero esa es una **cota superior**. No demuestra una contribución no nula de ese tamaño, ni excluye \(o(\rho^{-1/2})\) u \(O(\rho^{-1})\). «\(W2\) vive en el orden de la señal» sólo es fiel si significa que la cota disponible no permite separarlo de ella.

La frase «la mejora […] requeriría que las raíces del operador aniquilen la cota» es incorrecta como condición necesaria. Eso describe el procedimiento fallido. Una mejora puede obtenerse conservando las cancelaciones en una expansión de la integral exacta y acotando después el resto.

Igualmente, del soporte compacto exigido por Pfeiffer no se deduce que \(B_*1\) sea indefinible sobre **todo** pasado no compacto. Se deduce que esa aplicación queda fuera de su resultado y necesita una definición y un control de convergencia propios. El estado prudente es «no definido o justificado aquí sin prescripción adicional», no una imposibilidad general.

4. **§6 describe el hueco de forma demasiado exclusiva y, a la vez, incompleta.**

BBD (63) ya introduce
\[
V(y)=U^2f_0+U^3f_1+U^4f_2+U^5F
\]
bajo hipótesis de diferenciabilidad. Su declaración de desconocimiento en III.D se refiere a expresiones explícitas de esos coeficientes y a la interpretación de las correcciones. No equivale a demostrar que ninguna separación asintótica sea posible sin calcularlos explícitamente.

Por ejemplo, si se justificara uniformemente el cambio \(w=\sqrt{V(y)}\) y la amplitud transformada tuviera expansión
\[
\widetilde A(w,z)=a_0(z)+a_1(z)w+a_2(z)w^2+a_3(z)w^3+O(w^4),
\]
las cuatro raíces eliminarían las cuatro potencias integradas correspondientes. El resto daría \(O(\rho^{-5/2})\) antes del prefactor. No sería necesario conocer fórmulas explícitas para los \(a_j\). Lo pendiente es justificar las hipótesis y la uniformidad.

Por tanto:

- «Una sola cosa» y «NO sirve […]» exceden lo demostrado. Se ha descartado un argumento, no todas las posibles reparaciones.
- «\(f_0\) y los dos órdenes siguientes» no especifica el control adicional que falta respecto de lo ya supuesto en BBD.
- Separar \(O(\rho^{-1/2})\) de \(O(\log\rho\,\rho^{-1/2})\) no basta para identificar el coeficiente completo: sigue siendo necesario controlar cualquier contribución desconocida de orden \(\rho^{-1/2}\).
- Resolver \(W2\) no resolvería automáticamente la uniformidad de \(W1\) ni la definición sobre un pasado no compacto. Llamarlos «huecos menores» no está justificado por su efecto lógico.

La decisión de no continuar puede mantenerse. Su fundamento debe ser una obligación de prueba pendiente, no un no-go que los documentos no establecen.

5. **La identificación con Dowker–Glaser es correcta; la declaración de ausencia de antecedentes necesita corregirse.**

De (13),
\[
O_6\big|_{H_{DG}=4H}
=\frac{(4H+2)(4H+4)(4H+6)(4H+8)}{384}
=\widehat O_*.
\]
Aplicado a \(e^{-z}\) produce
\[
e^{-z}\left(1-14z+\frac{41}{2}z^2-\frac{22}{3}z^3+\frac23z^4\right),
\]
y, restituyendo los factoriales de las capas, el vector \((1,-14,41,-44,16)\). El control con la fila de seis dimensiones exige usar \(H_{DG}=6H\); da el vector distinto que figura en su tabla.

Es falso que la tesis «no contiene Weyl». En el capítulo 6, página 61, menciona expresamente obtener información sobre el tensor de Weyl comparando las construcciones de bola geodésica e intervalo de Alexandrov. La propia auditoría §6.3 ya había registrado esa aparición. No constituye antecedente del coeficiente, pero debe constar correctamente.

«No hay antecedente exacto» debe limitarse a «no se encontró en las fuentes examinadas». La ausencia en una tesis no certifica ausencia bibliográfica general. Respecto del vector, tampoco debe confundirse ausencia de una fila impresa con ausencia de una construcción publicada que lo determina exactamente.

El original de de Brito–Eichhorn–Pfeiffer no figura entre los documentos suministrados. Su cita está reproducida en los documentos internos; su literalidad no queda contrastada aquí con ese original.

6. **§7 omite errores relevantes y §5 no neutraliza los excesos anteriores.**

La tabla debería registrar la aceptación de la prueba inválida de \(W2\), que sostuvo la revocación de \(F2\) y varias promociones posteriores. Promover el coeficiente local a resultado global es una consecuencia; no sustituye el registro del error de prueba que lo permitió.

También omite la anterior lectura del resto \(O(\log\rho/\sqrt\rho)\) como incompatibilidad establecida, corregida por Grok en la auditoría, y la cancelación de \(W\) formulada inicialmente para toda la contribución, restringida por Astra al canal.

Las atribuciones a Grok y Astra están explícitas; no encuentro una apropiación de esos hallazgos. Sí encuentro un recuento incompleto de errores y una presentación incorrecta del grado de acuerdo entre revisores.

§5 conserva adecuadamente la frontera relativa a fluctuaciones, realizaciones individuales y aplicaciones físicas; Dowker–Glaser §2 respalda la advertencia sobre las fluctuaciones. Pero esa lista no corrige la universalidad sin condiciones, la prioridad absoluta ni las exclusiones de §6.

```text
N1_ESTABLECIDO     = SOBREAFIRMA — El coeficiente y la cancelación en el canal son correctos; §1 omite condiciones del resultado de universalidad y exagera la confirmación independiente.
N2_NO_ESTABLECIDO  = SOBREAFIRMA — Es fiel dejar abiertos resto, F1, C0 y estimador; la cota disponible no demuestra un orden efectivo ni imposibilidad de mejora o de definición general.
N3_BBD_VS_PFEIFFER = CORRECTA — BBD acota el integrando antes de la identidad; Pfeiffer conserva el operador con raíces tras sustituciones por normas que no justifican la desigualdad. Debe distinguirse BBD (25), plano, de III.B, curvo.
N4_PRIORIDAD       = INCORRECTA — La identidad con O6 y el vector son correctos; la tesis sí menciona Weyl y no queda certificada una ausencia universal de antecedentes.
VEREDICTO_CIERRE = APTA_CON_CORRECCIONES
DEFECTOS_ENCONTRADOS = universalidad sin condiciones; confirmación por tres casas mal descrita; cita plana usada para el caso curvo; cota superior presentada como orden efectivo; mejora ligada indebidamente a aniquilar una cota; indefinición general inferida del soporte compacto; §6 exclusivo e insuficiente; ausencia de Weyl falsa; prioridad negativa sin delimitar corpus; tabla de errores incompleta.
```