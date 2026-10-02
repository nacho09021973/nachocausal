# WP6 — Auditoría adversarial de prioridad de los tres blancos S1 congelados

> **STATUS: P1_P2_P3_PRIORITY_NOT_REFUTED /
> INTERNAL_LITERATURE_AUDIT_CLOSED /
> EXACT_EQUIVALENT_PRECEDENT_NOT_FOUND /
> EVEN_ZOHAR_STRONG_PARTIAL_PRECURSOR /
> KURECKA_MANDATORY_PARTIAL_PRECURSOR /
> DIACONIS_1989_PARTIALLY_ADJUDICATED /
> DIACONIS_1988_CH8_CH9_INDEX_VERIFIED_2026-09-02_NO_POSET_OR_SPAN_THEOREM_FOUND /
> DIACONIS_1988_CH5_VERIFIED_2026-09-02_NO_CLASS_SUM_EQUIVALENT_FOUND /
> DIACONIS_1988_INTERNAL_LITERATURE_AUDIT_CLOSED /
> P1_CLASS_SUM_SPAN_IS_THE_PRIORITY_GATE /
> P2_GENERIC_FACTORIZATION_PRECEDED /
> P2_EXACT_SUPPORT_REDUCES_TO_P1 /
> P3_PRIORITY_NOT_REFUTED /
> NO_NOVELTY_CERTIFICATE /
> EXTERNAL_SPECIALIST_REVIEW_STILL_REQUIRED.**

Fecha: 2026-09-02.

Baseline editorial auditado:
`cc2c72e` (`freeze WP6 S1 paper outline baseline`).

Esta auditoría no abre `Q_N`, dimensiones superiores ni el desarrollo de
Hoeffding. Somete a falsificación únicamente los tres blancos congelados del
outline:

\[
\tag{P1}
V_N=\operatorname{Sym}^2P_{N-1},
\]

\[
\tag{P2}
D\mathscr S_N=B_NP_N^{\rm vis},
\]

\[
\tag{P3}
r_N(\gamma_\psi)=2\qquad\forall N\ge2
\]

para la órbita exponencial antisimétrica explícita ya construida.

El veredicto global es `PRIORITY_NOT_REFUTED` para los tres blancos, tras
cerrar el 2026-09-02 la auditoría bibliográfica interna de P1 con la lectura
íntegra de Cap. 8, Cap. 9, Cap. 5 y el índice completo del monográfico
Diaconis 1988 (§3.6bis, §3.6ter). La búsqueda acotada no localizó un
resultado matemáticamente equivalente, pero sí antecedentes parciales muy
próximos, y el riesgo residual queda bajo pero no nulo (Cap. 1-4/6-7 solo
cubiertos por índice y por la hoja de ruta del propio autor, no leídos
página por página). En ningún caso esto certifica prioridad: la revisión de
un especialista externo sigue siendo obligatoria antes de cualquier
afirmación final de novedad.

## 1. Método, lenguajes y límites

Se cruzaron los documentos locales vigentes y las auditorías WP6 anteriores
con búsquedas de fuente primaria o texto completo en seis vocabularios:

1. causal sets, leyes de posets finitos y geometría estadística;
2. posets bidimensionales, realizadores y fibras de permutaciones;
3. estadística de rangos, rank likelihood y cópulas;
4. permutones, densidades de patrones y perturbaciones del permutón uniforme;
5. matrices de cobertura y representación estándar de \(\mathfrak S_N\);
6. información singular, gradiente nulo, Hessianos y primer jet no nulo de
   orden superior.

Se buscaron tanto las fórmulas literales como formulaciones equivalentes:
span o rango de gradientes de densidades de patrones, espacio de scores de la
ley de rangos, matrices de permutación comprimidas a
\(E_N=\mathbf1^\perp\), sumas cerradas por inversión, Hessianos en el permutón
uniforme y pérdida de identificabilidad bajo un cociente por isomorfismo.

La cobertura no es una revisión sistemática exhaustiva. No hubo acceso
completo y reproducible a MathSciNet, zbMATH, Scopus o Web of Science, ni se
cribaron todas las tesis y actas no indexadas. La ausencia de un hit exacto no
es una prueba de novedad.

### 1.1 Auditorías externas conservadas y peso probatorio

Se conservan sin modificación las dos auditorías fechadas recibidas:

- `biblioteca/Auditoría Bibliográfica Claude Sep 2026.md`;
- `biblioteca/Auditoría Bibliográfica Gemini Sep 2026.md`.

La auditoría de Claude recibe mayor peso metodológico para la adjudicación:
identifica a Even-Zohar como antecedente parcial fuerte, distingue el bloque
completo anterior al cociente del class-sum span y mantiene abierto el riesgo
Diaconis/Johnson. La auditoría de Gemini sirve como búsqueda independiente,
pero su conclusión de prioridad plenamente respaldada excede su evidencia y
su bibliografía contiene contaminación verificable: la entrada presentada
como apoyo a Pollard enlaza en realidad un artículo de regresión tensorial y
la entrada de arXiv:2309.10203 atribuye el trabajo a autores distintos de los
del preprint. No se usa por ello como autoridad para elevar el veredicto.

## 2. Resultado ejecutivo

| Blanco | Antecedente más peligroso | Veredicto acotado |
|---|---|---|
| P1: \(V_N=\operatorname{Sym}^2P_{N-1}\) | Even-Zohar 2020 para el bloque estándar completo de dimensión \((N-1)^2\); Kurečka 2022 para el aparato diferencial matricial; Diaconis 1989 para módulos de rankings y pares no ordenados; Bayoumi--El-Zahar--Khamis 1994 para las fibras de posets 2D | **No se encontró la igualdad después del cociente a posets no etiquetados, ahora incluida la lectura íntegra del Capítulo 5. `PRIORITY_NOT_REFUTED` (auditoría bibliográfica interna cerrada; revisión externa sigue obligatoria).** |
| P2: \(D\mathscr S_N=B_NP_N^{\rm vis}\) | Pollard 2011/2012 y geometría Hilbert elemental del score tras una estadística | **La factorización abstracta está precedida. Lo específico —que el soporte exacto sea P1 y que la restricción sea inyectiva— hereda el estado de P1.** |
| P3: \(r_N(\gamma_\psi)=2\) para todo \(N\) | teoría de información singular; Hessianos de densidades de patrones en el permutón uniforme; consistencia por borrado | **No se encontró la órbita S1 ni la propagación exacta all-\(N\). Prioridad no refutada; paridad, Hessianos y jets superiores no son por sí solos nuevos.** |

Conclusión editorial:

```text
FRAMEWORK_NOVELTY = NO
FINITE_PATTERN_DIFFERENTIAL_AT_UNIFORM_PERMUTON_IS_NEW = NO
BERNSTEIN_OR_COVER_MATRIX_TECHNIQUE_IS_NEW = NO
ABSTRACT_SCORE_PROJECTION_FACTORIZATION_IS_NEW = NO
UNLABELED_2D_POSET_FIBER_SPAN_EQUALS_SYM_EN = PRIORITY_NOT_REFUTED (INTERNAL_LITERATURE_AUDIT_CLOSED)
EXACT_S1_VISIBLE_SPACE_AND_KERNEL = STATUS_INHERITED_FROM_CLASS_SUM_SPAN
EXPLICIT_ANTISYMMETRIC_ORBIT_RN_EQUALS_2_ALL_N = PRIORITY_NOT_REFUTED
NOVELTY_CERTIFICATE = NO
```

## 3. P1 — espacio visible exacto

### 3.1 El antecedente directo en CST sigue siendo Bombelli

Bombelli, [*Statistical Lorentzian geometry and the closeness of Lorentzian
manifolds*](https://arxiv.org/abs/gr-qc/0002053) (2000), define la ley completa
de posets no etiquetados a cardinalidad fija y su comparación estadística.
Precede el marco, la compresión a una lista finita de probabilidades y la
pregunta por variaciones geométricas pequeñas. No calcula el diferencial S1,
su rango ni su kernel.

Janson, [*Poset limits and exchangeable random
posets*](https://arxiv.org/abs/0902.0306) (2011), proporciona el marco global
de kernels de poset y leyes finitas consistentes. No resuelve el espacio
tangente visible a un \(N\) fijo.

Surya, [*A Closeness Function on Coarse Grained Lorentzian
Geometries*](https://arxiv.org/abs/2510.19403) (2025/2026), precede la
narrativa general de que aumentar \(N\) puede levantar degeneraciones de una
compresión causal, en su caso mediante abundancias esperadas de intervalos.
No identifica el span de scores de la ley completa de posets ni el espacio
\(\operatorname{Sym}^2P_{N-1}\).

### 3.2 Precedencia combinatoria de la correspondencia poset--permutación

Bayoumi, El-Zahar y Khamis, [*Counting two-dimensional
posets*](https://doi.org/10.1016/0012-365X(94)90370-0) (1994), trabajan
explícitamente con la correspondencia muchos-a-uno entre permutaciones y
posets de dimensión dos. Registran que intercambiar los dos órdenes envía una
permutación a su inversa y que los posets primos tienen un realizador único
salvo ese intercambio. Esta literatura precede:

- la codificación de un poset 2D mediante una permutación relativa;
- la clausura de una fibra bajo \(\sigma\mapsto\sigma^{-1}\);
- el uso de realizadores únicos o casi únicos para controlar una fibra.

No se encontró allí una suma matricial sobre cada fibra, un diferencial de
probabilidades de muestreo ni un teorema de span sobre \(E_N\).

### 3.3 Antecedente parcial más peligroso: Even-Zohar 2020

Chaim Even-Zohar, [*Patterns in Random
Permutations*](https://arxiv.org/abs/1811.07883) (Combinatorica 40, 2020,
775--804), descompone el espacio completo de densidades de patrones mediante
representaciones de \(\mathfrak S_N\):

\[
\mathbb R^{N!}=V^{\rm EZ}_0\oplus\cdots\oplus V^{\rm EZ}_{N-1},
\]

donde \(V^{\rm EZ}_r\) está generado por los elementos matriciales de las
irreducibles indexadas por particiones \(\lambda\vdash N\) con
\(\lambda_1=N-r\). En particular, \(V^{\rm EZ}_1\) procede de la
representación estándar \(S^{(N-1,1)}\), tiene dimensión \((N-1)^2\) y se
realiza explícitamente mediante

\[
U^TA(\sigma)U,
\qquad U:\mathbb R^{N-1}\longrightarrow \mathbf1^\perp.
\]

Éste es el vecino más próximo al lado **anterior al cociente** de P1. Sin
embargo, Even-Zohar estudia órdenes de fluctuación del perfil de patrones de
una permutación aleatoria cuando el tamaño anfitrión tiende a infinito. Su
componente de escala \(n^{-1/2}\) no debe identificarse sin demostración con
el primer jet en el parámetro local \(\varepsilon\) de S1.

Tampoco suma las matrices dentro de las fibras de isomorfismo de posets no
etiquetados. La operación adicional que debe probar nuestro teorema es

\[
\underbrace{\operatorname{End}(E_N)}_{(N-1)^2}
\quad\xrightarrow{\ \text{suma por fibras de poset}\ }\quad
\underbrace{\operatorname{Sym}(E_N)}_{\binom N2},
\]

y, crucialmente, que las sumas de fibra no sólo sean simétricas sino que
generen **todo** el codominio. Ese paso no aparece en Even-Zohar.

### 3.4 Antecedente diferencial obligatorio: Kurečka 2022

Martin Kurečka, [*Lower bound on the size of a quasirandom forcing set of
permutations*](https://doi.org/10.1017/S0963548321000298) (publicado online
en 2021; volumen de 2022), es el antecedente diferencial obligatorio y debe
entrar en la bibliografía central del paper.

El artículo perturba permutones escalonados alrededor del permutón uniforme,
diferencia exactamente la densidad \(d(\pi,\mu)\) de un patrón de permutación
y define un polinomio gradiente \(P_\pi(\alpha,\beta)\). Sus coeficientes se
expresan mediante

\[
c_{ij}(P_\pi)=K_{ij,N}\,
(\mathbf b_{i+2}^{N})^{\!T}A_\pi\mathbf b_{j+2}^{N},
\]

donde \(A_\pi\) es la matriz de permutación y
\(\mathbf b_2^N,\ldots,\mathbf b_N^N\) forman una base de
\(E_N=\mathbf1^\perp\). También caracteriza la anulación de combinaciones de
polinomios gradiente mediante la matriz de cobertura
\(\sum_\pi t_\pi A_\pi\).

Esto precede sustancialmente el nivel de **permutaciones etiquetadas/rangos**
de nuestra reducción:

\[
\text{primer diferencial de densidad de patrón}
\longleftrightarrow
A_\pi|_{E_N}
\longleftrightarrow
\text{polinomio bivariado finito}.
\]

Por tanto, no es defendible presentar como nuevas la aparición de
polinomios finitos, la base de Bernstein asociada a rangos, la compresión de
matrices de permutación a \(E_N\), las matrices de cobertura ni el análisis
del gradiente en el nulo uniforme.

La diferencia que no se encontró en Kurečka es exactamente nuestro cociente
adicional:

\[
A_C=\sum_{\sigma\in\Gamma_C}A_\sigma,
\qquad
\Gamma_C=\{\sigma:\text{el poset producto de }\sigma
\text{ es isomorfo a }C\},
\]

seguido por

\[
\operatorname{span}\{A_C|_{E_N}:C\in\mathcal C_N\}
=\operatorname{Sym}(E_N).
\]

Kurečka estudia patrones de permutación individuales o combinaciones
elegidas para *forcing*. No agrupa exhaustivamente por isomorfismo de posets
2D no etiquetados y no prueba que esas sumas de fibra generen todo el espacio
simétrico. Tampoco formula el kernel del canal a la ley de posets.

### 3.5 Otros vecinos de permutones que no son el mismo teorema

Chan, Král', Noel, Pehova, Sharifzadeh y Volec,
[*Characterization of quasirandom permutations by a pattern
sum*](https://arxiv.org/abs/1909.11027) (2019/2020), estudian sumas de
densidades de patrones que fuerzan el permutón uniforme. Kurečka desarrolla
la versión diferencial usada para cotas de forcing.

Garbe, Král', Malekshahian y Penaguiao,
[*The dimension of the feasible region of pattern
densities*](https://arxiv.org/abs/2309.10203) (2023/2025), determinan la
dimensión global del espacio factible de densidades de patrones mediante
permutaciones de Lyndon. Su dimensión y su noción de independencia son las
de todas las densidades de patrones de tamaños acotados en el espacio de
permutones; no son el rango local, a cardinalidad exactamente \(N\), después
del cociente a posets no etiquetados.

Estos resultados impiden usar frases genéricas como “primera clasificación
de los grados de libertad de densidades de patrones”. No proporcionan un sink
de P1.

### 3.6 Diaconis, pares no ordenados y el riesgo Johnson

Diaconis, [*A generalization of spectral analysis with application to ranked
data*](https://doi.org/10.1214/aos/1176347251) (Annals of Statistics 17,
1989, 949--979), fue comprobado sobre el texto completo. El artículo
descompone funciones sobre rankings mediante representaciones de
\(\mathfrak S_N\), distingue efectos de pares ordenados y no ordenados y da
para la representación sobre pares no ordenados la descomposición

\[
M^{(N-2,2)}
\simeq
S^{(N)}\oplus S^{(N-1,1)}\oplus S^{(N-2,2)}.
\]

En el rango estable \(N\ge4\), éste es precisamente el tipo de módulo y la
dimensión \(\binom N2\) que hacen plausible una reformulación Johnson de
\(\operatorname{Sym}(E_N)\). Por tanto, la representación simétrica y su
descomposición no son nuevas.

No obstante, el artículo analiza datos de rankings y sus proyecciones. No
introduce fibras de posets bidimensionales no etiquetados, sus class sums ni
prueba que esos vectores concretos generen el módulo completo. El artículo de
1989 queda así adjudicado como antecedente parcial, no como refutación.

Permanece sin inspección integral el monográfico de Diaconis de 1988,
*Group Representations in Probability and Statistics*, junto con la
literatura específica del esquema de Johnson y análisis espectral de rankings.
El riesgo residual ya no es que allí aparezca el espacio abstracto
\(M^{(N-2,2)}\), pues eso está precedido, sino que aparezca un teorema de
rango/base para las sumas concretas equivalentes a nuestras fibras.

### 3.6bis Verificación directa del monográfico Diaconis 1988

Fecha de esta verificación: 2026-09-02. Fuente: Institute of Mathematical
Statistics Lecture Notes-Monograph Series, vol. 11 (1988), acceso abierto vía
Project Euclid
(<https://projecteuclid.org/ebooks/institute-of-mathematical-statistics-lecture-notes-monograph-series/group-representations-in-probability-and-statistics/toc/10.1214/lnms/1215467407>).

Se leyó íntegramente, imagen por imagen (el volumen es un escaneo, no texto
OCR):

- Capítulo 8, *Spectral Analysis*, pp. 141–166 (DOI
  `10.1214/lnms/1215467417`) — el capítulo señalado como de mayor riesgo
  porque cubre expresamente análisis espectral de datos de rankings y de
  homogeneous spaces.
- Capítulo 9, *Models*, pp. 167–178 (DOI `10.1214/lnms/1215467418`).
- Índice completo, pp. 193–198 (DOI `10.1214/lnms/1215467420`) — cubre
  terminológicamente los capítulos 1–7 (teoría de representación, paseos
  aleatorios, métricas, teoría de \(S_n\)) que no se leyeron página por
  página.

El Capítulo 5, *Examples of Data on Permutations and Homogeneous Spaces*,
pp. 92–101 (DOI `10.1214/lnms/1215467414`), se intentó pero quedó bloqueado
por la protección anti-bot (Incapsula) de Project Euclid; **no fue leído**.
Los capítulos 1–4, 6 y 7 tampoco se leyeron página por página; su cobertura
es solo indirecta, vía el índice.

Resultado sobre los cuatro puntos planteados:

1. **¿Trata el espacio de pares no ordenados / módulo tipo Johnson?** Sí,
   explícitamente. p. 148 (Cap. 8B, Caso 2, pares ordenados de \(n\)):
   \(L(X)=S^n\oplus2S^{n-1,1}\oplus S^{n-2,2}\oplus S^{n-2,1,1}\). p. 155
   (Cap. 8C, Ejemplo 3, *The Diallel Cross Design*), para pares **no
   ordenados** \(\{i,j\}\) indexados por cruces de \(n\) variedades: *"the
   standard ANOVA decomposition corresponds to the decomposition of what we
   have called \(M^{n-2,2}\cong S^n\oplus S^{n-1,1}\oplus S^{n-2,2}\)"*. p. 151
   (Remark 2) trata el caso análogo de tríos no ordenados de un conjunto de
   6 elementos.
2. **¿Identifica \(\operatorname{Sym}(E_N)\) o un módulo equivalente de
   dimensión \(\binom N2\)?** Sí: el \(M^{n-2,2}\) del Ejemplo 3 anterior
   (p. 155) tiene dimensión \(\binom n2\) y es exactamente ese módulo,
   presentado con un ejemplo de diseño experimental concreto. No añade
   novedad frente a lo ya adjudicado para Diaconis 1989 — refuerza que el
   módulo abstracto, e incluso este caso concreto de pares no ordenados,
   estaban ya en el monográfico de 1988 con más detalle que en el artículo
   de 1989.
3. **¿Aparece alguna operación equivalente a sumar por las fibras
   permutación → poset 2D no etiquetado?** No localizada. Ni "poset" ni
   "partially ordered set" aparecen en ninguna entrada del índice completo
   (pp. 193–198), que por construcción cubre terminológicamente todo el
   libro. Todos los objetos que Diaconis suma o proyecta son siempre
   \(G\)-órbitas de conjuntos, pares o rankings bajo el grupo simétrico (o
   algún otro grupo clásico) sobre un homogeneous space \(X=G/H\); en ningún
   punto aparecen clases de isomorfismo de un poset bajo su propio grupo de
   automorfismos.
4. **¿Algún teorema implica
   \(\operatorname{span}\{A_C|_{E_N}\}=\operatorname{Sym}(E_N)\)?** No
   encontrado. El aparato formal más próximo es el Radon transform (Método
   3, pp. 151–152, Lemma 1: \(R^+R^-\) es una proyección ortogonal de
   \(M^{n-k,k}\) sobre la copia de \(M^{n-j,j}\)) y el Teorema 1 (p. 149,
   fórmula de proyección \(\Pi_i=\frac{d_i}{|G|}\sum_t\chi_i(t)^*\rho(t)\)).
   Ambos son teoremas de proyección/rango sobre los módulos \(M^\lambda\)
   clásicos de conjuntos etiquetados bajo \(S_n\), no un teorema de que las
   sumas concretas sobre fibras de isomorfismo de posets no etiquetados
   generen \(\operatorname{Sym}^2(P_{N-1})\).

Adjudicación: los puntos 1–2 (precedidos) no cambian el veredicto de P1 —
solo lo refuerzan, deflactando aún más cualquier reclamo de novedad sobre el
módulo abstracto, algo que ya estaba asumido desde Diaconis 1989. Los puntos
3–4, que son el ingrediente específicamente reclamado como potencialmente
nuevo, no aparecen en las ~44 páginas leídas íntegramente (Cap. 8 + Cap. 9)
ni en el índice completo del libro. El riesgo residual se reduce de "todo el
monográfico sin inspeccionar" a un remanente concreto y acotado: el
Capítulo 5 (10 páginas, bloqueado por acceso) y los capítulos 1–4/6/7
(cubiertos solo indirectamente vía índice).

```text
DIACONIS_1988_CH8_MODELS_INDEX_VERIFIED = YES (pp. 141-178, 193-198 full text)
DIACONIS_1988_CH5_VERIFIED = NO (access blocked, Incapsula)
DIACONIS_1988_CH1_4_6_7_VERIFIED = INDEX_ONLY
DIACONIS_1988_POSET_OR_JOHNSON_SCHEME_TERM_FOUND = NO
DIACONIS_1988_CLASS_SUM_SPAN_THEOREM_FOUND = NO
P1_RESIDUAL_RISK_UPDATED = NARROWED_TO_CH5_AND_CH1_4_6_7_UNVERIFIED
```

### 3.6ter Verificación directa del Capítulo 5 (cierre del riesgo residual)

Fecha de esta verificación: 2026-09-02, segunda sesión. Mismo volumen y DOI de
capítulo que en 3.6bis (`10.1214/lnms/1215467414`, pp. 92-101). El acceso
directo vía navegación de página quedó bloqueado por Incapsula en la sesión
anterior; en esta sesión, una descarga `curl` directa del enlace de PDF con
una cabecera `User-Agent` de navegador de escritorio superó el bloqueo y
entregó el PDF completo (10/10 páginas, escaneado). Se leyó íntegramente,
imagen por imagen.

El Capítulo 5, *Examples of Data on Permutations and Homogeneous Spaces*, es
un capítulo puramente motivacional y no contiene ni un solo teorema, lema o
resultado formal. Sus secciones:

- **A. Permutation data**: rankings de encuesta (ciudad/suburbio/campo,
  NORC 1972), la lotería del reclutamiento de EE.UU. de 1970 (una
  permutación de \(S_{365}\)).
- **B. Partially ranked data**: elección de la American Psychological
  Association por el método Hare (\(S_{40}/S_{30}\) y espacios homogéneos
  análogos), subconjuntos de \(k\) de \(n\) (lotería Lotto 6/49,
  \(S_n/S_k\times S_{n-k}\)), datos Q-sort, y una nota general sobre otras
  acciones de \(S_n\) (particiones, árboles binarios etiquetados).
- **C. The \(d\)-sphere \(S^d\)**: datos de orientación magnética,
  \(O(n)/O(n-1)\).
- **D. Other groups**: \(\mathbb Z_2^k\), \(\mathbb Z_{365}\times
  \mathbb Z_{365}\), grupos ortogonal y unitario.
- **E. Statistics on groups**: enunciado general de problemas (test de
  uniformidad, test de dos muestras, asociación, ajuste y bondad de ajuste de
  modelos), sin desarrollo formal.

Ni "poset" ni "partially ordered set" ni ninguna operación de suma sobre
fibras de isomorfismo aparecen en ninguna de las diez páginas. No hay
teorema de span ni de rango en todo el capítulo, precisamente porque el
capítulo no contiene teoremas de ningún tipo.

El propio cierre del capítulo (p. 101, sección E) da el mapa de autor de lo
que sigue, y es relevante para el riesgo residual sobre los capítulos aún no
leídos página por página:

> "Chapter 6 develops measures of distance on groups and homogeneous
> spaces... Chapter 8 develops an analog of the spectral analysis of time
> series for group valued data... Chapter 7 is devoted to a self-contained
> development of this [representation] theory. Chapter 9 uses representation
> theory to develop a natural family of models."

Es decir, según la propia hoja de ruta de Diaconis: el Capítulo 7 es el
aparato de teoría de representación de \(S_n\) que alimenta los Capítulos 8 y
9 (ya leídos íntegramente en 3.6bis, sin rastro del ingrediente buscado); el
Capítulo 6 son medidas de distancia genéricas sobre grupos y espacios
homogéneos, no una construcción de fibras de poset. Esto no es lectura
página por página de los Capítulos 6-7, pero sí es una confirmación, en voz
del propio autor, de que su contenido temático no apunta al ingrediente
reclamado. Los Capítulos 1-4 (introducción, teoría de representación básica,
paseos aleatorios, teoría de \(S_n\)) permanecen cubiertos solo por el
índice completo, que ya no contiene "poset" en ninguna entrada (3.6bis).

```text
DIACONIS_1988_CH5_VERIFIED = YES (full text, 10/10 pages, curl + browser UA
  bypassed the Incapsula block from the prior session)
DIACONIS_1988_CH5_CONTAINS_THEOREMS = NO (purely motivational examples chapter)
DIACONIS_1988_CH5_POSET_OR_SPAN_TERM_FOUND = NO
DIACONIS_1988_CH6_CH7_CROSS_CHECKED_VIA_AUTHORS_OWN_ROADMAP = YES (p.101:
  distance metrics / Sn representation-theory foundations for Ch.8-9, not a
  poset-fiber class-sum construction)
P1_RESIDUAL_RISK_UPDATED = LOW (Ch.1-4 index-only, Ch.6-7 index-only +
  author's-own-roadmap cross-check; non-exhaustive search caveat of Sec. 1
  still applies)
```

### 3.7 Estadística de rangos y cópulas

La aparición de polinomios de Bernstein en proyecciones de estadísticas de
rangos tiene precedencia explícita en Hallin, Mellouk y Rifi,
[*Projection de Hájek et polynômes de
Bernstein*](https://doi.org/10.2307/3316057) (2001). Su objeto son
proyecciones de Hájek para estadísticas de rangos lineales y aproximación
asintótica, no el span exacto de scores de nuestra ley finita.

Hoff, [*Extending the rank likelihood for semiparametric copula
estimation*](https://arxiv.org/abs/math/0610413) (2007), establece el rank
likelihood como likelihood marginal libre de las distribuciones marginales.
Sei y Matsumoto, [*Properties of Divergence for Semiparametric Copula
Models*](https://www.ism.ac.jp/editsec/toukei/pdf/68-1-all.pdf) (2020),
definen la divergencia inducida por la distribución finita del estadístico
multirrango, remarcan que puede perder identificabilidad a \(n\) finito y
comparan numéricamente su crecimiento con \(n\). La geometría eficiente de
modelos gaussianos de cópula y rangos también está desarrollada por Hoff,
Niu y Wellner,
[*Information bounds for Gaussian
copulas*](https://arxiv.org/abs/1110.3572) (2014).

Estos trabajos preceden el experimento de rangos, la pérdida de información a
tamaño finito y la comparación Fisher/eficiencia en modelos de cópula. No se
encontró en ellos el cociente adicional desde la permutación completa al
poset no etiquetado, ni la igualdad P1 para un tangente no paramétrico S1.

### 3.8 Adjudicación de P1

La parte no precedida localizada es estrecha y concreta:

> Para la ley del poset bidimensional no etiquetado obtenida a partir de una
> muestra S1 de tamaño exactamente \(N\), las sumas de representantes de
> score sobre todas las fibras de isomorfismo generan exactamente
> \(\operatorname{Sym}^2P_{N-1}\).

```text
P1_EXACT_STATEMENT_FOUND = NO
P1_PRIORITY = PRIORITY_NOT_REFUTED
P1_CLOSEST_PRECURSOR = EVEN_ZOHAR_2020
P1_MANDATORY_DIFFERENTIAL_PRECURSOR = KURECKA_2022
P1_ABSTRACT_SYMMETRIC_MODULE_PRECEDED = DIACONIS_1988_AND_1989
P1_NOVEL_INGREDIENT_IF_CONFIRMED = UNLABELED_POSET_FIBER_CLASS_SUM_SPAN
P1_RESIDUAL_RISK = LOW (see 3.6bis + 3.6ter; Cap.8 + Cap.9 + Cap.5 read in
  full, 2026-09-02: no trace of "poset", "Johnson scheme" or a span/rank
  theorem on fibre class sums anywhere read; Cap.1-4/6/7 remain index-only
  but Cap.6-7 are cross-checked against the author's own chapter-6-9 roadmap
  in Cap.5§E, p.101, which does not point to the claimed ingredient)
P1_EXTERNAL_SPECIALIST_CHECK = STILL_REQUIRED (per Founding Rules: a
  guardrail that cannot fail is decoration; internal literature search is
  not a substitute for external adjudication of novelty)
NO_NOVELTY_CERTIFICATE = YES (unaffected by this closure -- this audit
  narrows risk, it does not certify novelty)
```

## 4. P2 — factorización del diferencial

Pollard, [*A note on insufficiency and the preservation of Fisher
information*](https://arxiv.org/abs/1107.3797) (2011/2012), prueba en el
marco DQM que el score después de aplicar una estadística es la esperanza
condicional del score original. En Hilbert, cualquier operador lineal
acotado \(T\) se factoriza tautológicamente por la proyección ortogonal sobre
\((\ker T)^\perp\), y su restricción a ese soporte es inyectiva.

Por tanto, tomada aisladamente,

\[
D\mathscr S_N=B_NP_N^{\rm vis}
\]

no constituye un teorema de prioridad independiente. Es la formulación
operatorial canónica una vez conocido el kernel. Lo específico de S1 es:

\[
(\ker D\mathscr S_N)^\perp
=\operatorname{Sym}^2P_{N-1},
\]

y eso es equivalente al contenido de P1. La inyectividad de
\(B_N=D\mathscr S_N|_{V_N}\) es entonces inmediata.

La descomposición entre soporte visible y operador Fisher
\(F_N=B_N^*B_N\) es matemáticamente importante para el paper, pero no debe
venderse como una nueva construcción general de información estadística.

```text
P2_ABSTRACT_FACTORIZATION = KNOWN_THEOREM_SPECIALIZATION
P2_CONDITIONAL_SCORE_MECHANISM = PRECEDED_BY_DQM_STATISTIC_THEORY
P2_EXACT_S1_PROJECTOR = PRIORITY_STATUS_INHERITED_FROM_P1
P2_INDEPENDENT_NOVELTY_CLAIM = NO
```

## 5. P3 — primer jet no nulo de orden dos

### 5.1 Qué está claramente precedido

La literatura de información singular estudia modelos identificables cuyo
score o información Fisher se anulan en un punto y donde el primer término
informativo aparece en una derivada superior. Rotnitzky, Cox, Bottai y
Robins, [*Likelihood-Based Inference with Singular Information
Matrix*](https://doi.org/10.2307/3318576) (2000), relacionan explícitamente
las tasas y la inferencia con el orden \(s\) de la primera derivada no nula;
para \(s\) par aparece además una ambigüedad de signo. Por tanto, “invisible a
primer orden pero visible a orden superior” y el papel de la paridad no son
claims generales nuevos.

Dentro de la literatura de permutones, los trabajos de forcing no se detienen
en el gradiente. Chan (tesis, 2021) y Crudele, Dukes y Noel,
[*Six Permutation Patterns Force
Quasirandomness*](https://arxiv.org/abs/2303.04776) (2023), calculan
Hessianos de densidades o combinaciones de densidades de patrones alrededor
del permutón uniforme cuando el gradiente se anula. Esto precede el uso de un
segundo diferencial de leyes de patrones para detectar perturbaciones
ocultas al primer orden.

Finalmente, que una ley de tamaño \(2\) sea el push-forward de la ley de
tamaño \(N\) por borrado uniforme es consistencia proyectiva estándar del
muestreo iid. Diferenciar una identidad exacta con kernel independiente del
parámetro es una consecuencia formal. Esa propagación no debe aislarse como
una nueva teoría general.

### 5.2 Qué no se encontró

No se localizó un trabajo que reúna las cuatro piezas específicas siguientes:

1. la senda exponencial S1 generada por el \(\psi\) antisimétrico concreto;
2. la igualdad exacta de la ley de posets no etiquetados bajo
   \(\varepsilon\leftrightarrow-\varepsilon\);
3. el cálculo \(\mu_2''(0)\ne0\) para esa senda;
4. la conclusión all-\(N\)
   \(r_N(\gamma_\psi)=2\) mediante los kernels exactos de borrado.

Así, el resultado defendible no es la existencia abstracta de singularidades
de orden dos ni el uso de Hessianos, sino esa órbita causal S1 explícita y su
propagación a toda cardinalidad.

```text
P3_GENERIC_HIGHER_ORDER_IDENTIFIABILITY = PRECEDED
P3_PATTERN_DENSITY_HESSIAN_AT_UNIFORM_NULL = PRECEDED
P3_PROJECTIVE_DELETION_ARGUMENT = FORMAL_STANDARD_MECHANISM
P3_EXACT_S1_ORBIT_ALL_N_STATEMENT_FOUND = NO
P3_PRIORITY = NOT_REFUTED
```

## 6. Claim ceiling recomendado para el manuscrito

### 6.1 Formulación resistente

> Building on Bombelli's finite causal-order laws, and using the differential
> and representation-theoretic language for permutation-pattern densities
> developed in the permuton and rank-statistics literature, we identify the
> exact effect of the additional quotient by unlabeled
> two-dimensional-poset isomorphism in the S1 tangent model. Whereas the
> pre-quotient standard-representation block has dimension \((N-1)^2\), at
> sample size \(N\) the class-sum score span is precisely
> \(\operatorname{Sym}^2P_{N-1}\). This yields the exact support projection,
> kernel and identifiable quotient of the first differential. We also exhibit
> a specific antisymmetric exponential orbit whose first nonzero finite-poset
> jet is of order two at every cardinality.

Hasta una revisión externa, es preferible escribir “we identify” o “we
prove” y no “for the first time”.

### 6.2 Claims que la auditoría refuta o no autoriza

No afirmar:

- que se introduce la geometría estadística de leyes de causal sets;
- que se descubre por primera vez la compresión a cardinalidad finita;
- que se introduce el diferencial de densidades de patrones en el permutón
  uniforme;
- que la base Bernstein, los polinomios gradiente, las matrices de cobertura
  o la compresión a \(E_N\) son nuevos;
- que la descomposición del bloque estándar completo de dimensión
  \((N-1)^2\), o la representación abstracta de los efectos de pares no
  ordenados, son nuevas;
- que la factorización de un score por su soporte visible es una nueva teoría
  operatorial;
- que se descubre en general la identificabilidad de segundo orden o el uso
  del Hessiano cuando Fisher se anula;
- que la ausencia de un resultado exacto en esta búsqueda prueba prioridad.

### 6.3 Unidad matemática que sí merece revisión externa

El paquete mínimo que debe enviarse a un especialista en permutones/rank
statistics no son las tres fórmulas aisladas. Es esta implicación:

\[
\begin{aligned}
&\text{gradiente de patrón individual}
\longleftrightarrow A_\sigma|_{E_N}
&&\text{(cercano a Kurečka)},\\
&\text{cociente por isomorfismo de poset}
\longleftrightarrow
A_C=\sum_{\sigma\in\Gamma_C}A_\sigma,
&\\
&\operatorname{span}\{A_C|_{E_N}\}
=\operatorname{Sym}(E_N)
&&\text{(blanco de prioridad)},\\
&\text{por tanto }V_N=\operatorname{Sym}^2P_{N-1}
\text{ y }D\mathscr S_N=B_NP_N^{\rm vis}.&
\end{aligned}
\]

Ésta es la formulación más fácil de falsar por un experto y la que evita
confundir antecedentes de técnica con un antecedente del teorema exacto.

## 7. Decisión operativa

```text
OUTLINE_BASELINE = cc2c72e
OUTLINE_REOPEN_REQUIRED_BY_AUDIT = NO
EVEN_ZOHAR_2020_MUST_BE_ADDED_TO_PAPER = YES
KURECKA_2022_MUST_BE_ADDED_TO_PAPER = YES
BAYOUMI_ET_AL_1994_MUST_BE_ADDED_TO_PAPER = YES
DIACONIS_1989_MUST_BE_USED_TO_DEFLATE_ABSTRACT_MODULE_CLAIM = YES
POLLARD_2011_2012_MUST_BE_USED_TO_DEFLATE_P2 = YES
SINGULAR_INFORMATION_AND_PERMUTON_HESSIAN_CONTEXT_FOR_P3 = YES
GENERAL_Q_N = DO_NOT_OPEN
HIGHER_DIMENSIONS = DO_NOT_OPEN
HOEFFDING_DEVELOPMENT = DO_NOT_OPEN
DIACONIS_1988_CH5_MUST_BE_USED_TO_CLOSE_RESIDUAL_RISK_NOTE_IN_PAPER = OPTIONAL
INTERNAL_BIBLIOGRAPHIC_AUDIT_OF_P1 = CLOSED_2026-09-02
NEXT_GATE = RETURN_TO_MANUSCRIPT (internal literature audit of P1 closed;
  EXTERNAL_SPECIALIST_REVIEW remains a standing, non-blocking requirement
  before any final novelty claim, per Founding Rules)
```

La auditoría no obliga a cambiar la arquitectura del paper. Sí cambia el
posicionamiento: el bloque estándar completo, el núcleo diferencial a nivel
de patrones de permutación y el módulo abstracto de pares no ordenados tienen
precedentes directos o parciales. La aportación estrecha sometida aún a
auditoría está en resolver exactamente qué sobrevive después del cociente
causal a posets no etiquetados y en demostrar que sus class sums generan el
soporte simétrico completo. No se abre mientras tanto \(Q_N\), Hoeffding ni
dimensiones superiores.
