# P1a — EF-6: auditoría bibliográfica de prioridad y precedentes

```text
ESTADO: COMPLETE_BIBLIOGRAPHIC_AUDIT
FECHA DE CORTE: 2026-08-12
RESULTADO MATEMÁTICO: FAMILY_SPECIFIC_RESULT
PRIORIDAD: PRIORITY_NOT_CERTIFIED
PRECEDENTE DIRECTO ENCONTRADO: NO_EN_EL_CORPUS_AUDITADO
DESTINO: STANDALONE_TECHNICAL_NOTE_BEFORE_MANUSCRIPT_INTEGRATION
EF5_NECESARIO_PARA_EL_CIERRE: NO
```

## 1. Veredicto ejecutivo

La auditoría no encontró una fuente que enuncie o demuestre el teorema completo de
EF-4: consistencia en error cuadrático absoluto del estimador de cardinalidad lateral,
bajo el selector adaptativo y condicionado `MIN_COVERAGE_LEX`, en el modelo
`fixed-n`, `d=2`, sobre la sucesión completa.

Sí encontró antecedentes directos para casi todos los ingredientes por separado:
estadísticos de orden uniformes y spacings, correspondencia RSK y conteo por formas,
concentración para muestreo sin reemplazo, procesos de copula/permutones, scan
statistics adaptativos, inferencia condicionada a selección y criterios de selección
única en causal sets. Esos antecedentes no controlan simultáneamente el evento de
unicidad del selector congelado, el coste subexponencial de ese condicionamiento y la
varianza dentro de las fibras de la cardinalidad observada.

Por ello la clasificación científica es `FAMILY_SPECIFIC_RESULT`: la contribución
está en el ensamblaje y, sobre todo, en el certificado específico de selección única
de EF-4. La clasificación histórica queda en `PRIORITY_NOT_CERTIFIED`. No encontrar
un precedente mediante esta búsqueda no demuestra primacía.

El destino recomendado es una **nota técnica autónoma**, sometida primero a revisión
matemática independiente. EF-5 no es requisito para redactarla ni para sostener el
terminal `FIBER_CONCENTRATION`; sería exploración combinatoria posterior.

## 2. Enunciado exacto sometido a auditoría

El objeto auditado no es el lema genérico «número corresponde a volumen», sino el
siguiente enunciado compuesto.

Sean `n` puntos iid uniformes en el cuadrado nulo, condicionado a `N=n`, y sea `S` el
evento de que `MIN_COVERAGE_LEX` tenga una cuádrupla ganadora única. Para uno de los
dos lados seleccionados, sean

\[
M=|I[a,b]|,
\qquad
\ell=\sqrt{(U_b-U_a)(V_b-V_a)},
\qquad
\widehat\ell_{\rm CV,n}(M)=\sqrt{\frac{M-2}{n-2}}.
\]

Dentro de este canal y con estas convenciones,

\[
\mathbb E_n\!\left[
  (\ell-\widehat\ell_{\rm CV,n}(M))^2\mid S
\right]\longrightarrow0.
\tag{EF6.1}
\]

En particular, el riesgo de Bayes dentro del canal `sigma(M)` también converge a
cero. La cadena interna que produce (EF6.1) es

\[
P_{1,n}\to0,
\qquad
\log(1/\Pr_n(S))=o(n),
\qquad
Q_{2,n}\to0,
\qquad
P_{2,n}\to0.
\tag{EF6.2}
\]

La auditoría no atribuye novedad a «orden + número», al número-volumen de causal set,
a la ley Beta de un spacing, a RSK ni a una cola hipergeométrica. Pregunta únicamente
si ya estaba demostrado el compuesto (EF6.1)--(EF6.2) para este selector, observable,
condicionamiento y estimando.

## 3. Protocolo y límites de la búsqueda

Se revisaron:

1. la biblioteca local y sus conversiones de texto, además de los expedientes previos
   de P1a;
2. fuentes primarias y páginas editoriales con DOI en causal sets, permutaciones
   aleatorias, estadísticos de orden, procesos empíricos, scan statistics e inferencia
   pos-selección;
3. arXiv hasta la fecha de corte, incluyendo trabajo de junio de 2026 sobre muestreo
   exacto condicionado por la longitud de LIS;
4. búsquedas por el nombre interno `COUNT_VOLUME` y por descripciones matemáticas sin
   ese nombre: interval cardinality, relative duration, random 2-orders, rank plots,
   rectangular scans, unique maximizer, conditioning on selection y planted
   permutations.

La búsqueda no fue una revisión sistemática con acceso completo a MathSciNet,
zbMATH, Scopus o Web of Science, ni una inspección exhaustiva de todas las citas hacia
delante. Tampoco existe un nombre externo estabilizado para `MIN_COVERAGE_LEX`, lo que
reduce la recuperabilidad por palabras clave. Estas dos limitaciones bastan para
impedir una certificación de prioridad.

`NO_EN_EL_CORPUS_AUDITADO` significa exactamente que las fuentes inspeccionadas no
contienen el teorema; no significa que el teorema no exista en la literatura.

## 4. Mapa de precedentes

| Bloque de EF-0--EF-4 | Precedente verificado | Qué cubre | Relación con EF-4 |
|---|---|---|---|
| Número-volumen en causal sets | Bombelli--Lee--Meyer--Sorkin (1987); Saravani--Aslanbeigi (2014) | Fundamento de `Number ~ Volume` y propiedades del muestreo de Poisson | `PRECURSOR_ONLY`: no hay selector lateral ni teorema condicionado de MSE |
| Reconstrucción en `1+1` y 2-orders | Henson (2006); Fewster--Hawkins--Minz--Rejzner (2021) | Embedding aproximado, correspondencia con 2-orders y criterios que buscan selección única de un pasado preferido | Es el vecino causal más próximo, pero su objetivo, selector y evidencia son distintos |
| Spacings de estadísticos de orden | Rényi (1953); Pyke (1965) | Leyes de estadísticos de orden y spacings uniformes; base de la representación Beta/Dirichlet | `STANDARD_COROLLARY` para la ley condicionada por una forma fija |
| LIS, RSK y recuento por formas | Schensted (1961); Knuth (1970); Regev (1981); Gessel (1990); Clifford--Clifford (2026) | LIS como primera fila, conteos por tableaux, asintótica en bandas y conteo/muestreo exacto con LIS prescrita | `STANDARD_COROLLARY` para `EMPTY`; no conserva las marcas rectangulares de `UNIQUE/TIE` |
| Concentración sin reemplazo | Hoeffding (1963); Serfling (1974) | Colas para sumas de una muestra finita sin reemplazo | `STANDARD_COROLLARY` para cada rectángulo; la uniformidad se obtiene por unión finita |
| Rank plots, copulas y permutones | Fermanian--Radulović--Wegkamp (2004); Hoppen et al. (2013) | Convergencia de procesos de copula empírica y objetos límite de secuencias de permutaciones | `PRECURSOR_ONLY`: no controlan el condicionamiento por el argmax único de EF-4 |
| Maximización adaptativa sobre ventanas | Kulldorff (1997); Walther (2010); Arias-Castro et al. (2018) | Scan statistics, rectángulos adaptativos, multiplicidad y calibración por rangos/permutaciones | `PRECURSOR_ONLY`: problema de test y potencia, no riesgo dentro de fibras tras selección |
| Condicionamiento por selección | Fithian--Sun--Taylor (2014); Lee--Sun--Sun--Taylor (2016) | Inferencia válida condicionada al evento de selección | `PRECURSOR_ONLY`: marco general, sin la probabilidad de `S` ni el certificado combinatorio de EF-4 |

### 4.1 El precedente causal más cercano

Fewster et al. estudian seis reglas para elegir un elemento del pasado de rango dos y
reportan que una de ellas selecciona un singleton con probabilidad muy alta en sus
simulaciones. El mismo trabajo usa la correspondencia entre sprinklings `1+1` y
2-orders para cálculos combinatorios. Es una proximidad real: causal set, selección
por propiedades de intervalos, unicidad y 2-orders aparecen en la misma fuente.

No anticipa (EF6.1). Su selección es local y de rango dos, no
`MIN_COVERAGE_LEX`; la unicidad se evalúa numéricamente en ese bloque; no se prueba
un coste `exp[-o(n)]` para el evento de selección; y no se estudia la suficiencia
asintótica de una cardinalidad para una duración relativa seleccionada. Se clasifica
como `PRECURSOR_ONLY`, no como precedente directo.

### 4.2 Los precedentes probabilísticos más cercanos

Los procesos de copula empírica y los permutones formalizan que un rank plot de una
permutación uniforme se aproxima al copula de independencia. Las scan statistics
tratan precisamente la elección adaptativa de ventanas y el efecto de comparaciones
múltiples; la literatura por rangos y permutaciones conserva además el carácter
distribution-free.

La brecha respecto de EF-4 es el condicionamiento. Una convergencia incondicional
uniforme no puede dividirse gratuitamente por `Pr(S)` cuando `S` depende de todo el
rank plot. EF-3 explicita esa pérdida y EF-4 prueba, mediante una familia prescrita,
que el coste de `S` es subexponencial. Ninguna de las fuentes inspeccionadas contiene
esa obligación para el score de dos intervalos de `MIN_COVERAGE_LEX`.

La inferencia selectiva ofrece el lenguaje correcto para condicionar a un evento
adaptativo, pero se orienta a tests e intervalos válidos en familias estadísticas. No
da la cota combinatoria de `Pr(S)` ni la concentración dentro de las fibras de `M`.

### 4.3 El límite exacto de RSK

Schensted y la literatura posterior hacen estándar

\[
\#\{\pi:\operatorname{LIS}(\pi)\le5\}
=\sum_{\lambda\vdash n,\lambda_1\le5}(f^\lambda)^2.
\]

Gessel proporciona fórmulas determinantes para conteos con LIS acotada, Regev da
asintóticas para tiras de diagramas y Clifford--Clifford demuestra en 2026 que
incluso el muestreo uniforme exacto con LIS prescrita puede hacerse mediante RSK y
conteos de completaciones. Esto confirma que la parte `EMPTY` de EF-3 pertenece a la
tecnología estándar de LIS/RSK.

También confirma el corte conceptual ya usado en EF-3: condicionar por LIS retiene
una sola marca global. No registra las dos cardinalidades rectangulares, el mínimo
bilateral, el segundo componente lexicográfico ni la unicidad del ganador. RSK no es
un precedente del certificado `UNIQUE` de EF-4.

## 5. Clasificación por piezas

### 5.1 `STANDARD_COROLLARY`

Se clasifican así, sin reivindicación de novedad:

- independencia entre permutación de rangos y magnitudes ordenadas para muestras iid
  continuas;
- ley Beta/Dirichlet de los gaps condicionados a rangos y el control de
  `P_{1,n}` derivado de ella;
- equivalencia `EMPTY` con `LIS<=5` y su cómputo por RSK/tableaux;
- cola hipergeométrica para un rectángulo determinista y unión sobre menos de `n^4`
  pares de intervalos;
- optimalidad de la esperanza condicionada bajo pérdida cuadrática.

### 5.2 `PRECURSOR_ONLY`

Se clasifican así:

- el principio causal `Number ~ Volume`;
- el uso de 2-orders para sprinklings de Minkowski `1+1`;
- criterios causales que buscan selección única;
- procesos de copula/permutones para rank plots;
- scan statistics por rangos o permutaciones;
- inferencia condicionada a selección.

Estas líneas justifican el marco y varias herramientas, pero no contienen el
teorema compuesto auditado.

### 5.3 `FAMILY_SPECIFIC_RESULT`

La parte que no se reduce a los precedentes encontrados es:

1. el puente cuantitativo de EF-3 que conserva el selector adaptativo y muestra
   exactamente por qué basta `-log Pr_n(S)=o(n)`;
2. la construcción prescrita de dos escaleras para el score bilateral congelado;
3. la tricotomía de rivales y el margen corregido `rho_n/2-o(rho_n)`;
4. la prueba de que la cuádrupla plantada es el único ganador con coste
   `exp[-o(n)]`;
5. la transferencia inyectiva a tamaños impares y la conclusión sobre la sucesión
   completa;
6. la combinación de lo anterior con la ley Beta-producto para obtener (EF6.1).

Estos pasos dependen materialmente de la geometría discreta y del score de
`MIN_COVERAGE_LEX`; no se presentan como un teorema universal sobre scan statistics,
permutaciones o causal sets.

## 6. Clasificación final y lenguaje permitido

La hoja de ruta ofrecía cuatro rótulos que mezclan relación matemática y fuerza de
la afirmación histórica. Para evitar una falsa disyunción, EF-6 registra dos campos:

```text
EF6_RESULT_CLASS = FAMILY_SPECIFIC_RESULT
EF6_PRIORITY_STATUS = PRIORITY_NOT_CERTIFIED
EF6_CLOSEST_PRECEDENTS = PRECURSOR_ONLY
EF6_STANDARD_COMPONENTS = RANKS_BETA_RSK_HYPERGEOMETRIC_PROJECTION
EF6_DIRECT_PRECEDENT_FOUND = NO_WITHIN_SEARCHED_CORPUS
```

Lenguaje permitido:

> Para el modelo `fixed-n`, `d=2`, el selector `MIN_COVERAGE_LEX` y el estimando
> lateral relativo declarados, se prueba que el MSE absoluto de `COUNT_VOLUME`
> converge a cero. La prueba combina ingredientes clásicos con un certificado
> específico de unicidad de coste subexponencial. No se encontró un enunciado
> equivalente en el corpus auditado; la prioridad no está certificada.

Lenguaje no permitido sin una auditoría externa adicional:

- «primer teorema de consistencia número-volumen en causal sets»;
- «primer estimador consistente de tiempo propio desde un causal set»;
- «`COUNT_VOLUME` recupera la geometría»;
- «óptimo», «universal» o «asintóticamente suficiente» sin nombrar el canal;
- cualquier extensión automática a escala absoluta, al poset completo o a `d>=3`.

## 7. Decisión de destino

El resultado merece conservarse como **nota técnica autónoma**. No se recomienda
integrarlo todavía en el manuscrito principal ni convertirlo directamente en una
reivindicación de prioridad.

La nota debería contener, en este orden:

1. modelo, selector, evento `S`, estimando y riesgo exactos;
2. separación rango--magnitud y cierre uniforme de la pieza Beta-producto;
3. lema de discrepancia y teorema condicional de EF-3;
4. certificado prescrito de EF-4, incluyendo el margen corregido y la transferencia
   a impares;
5. teorema de consistencia (EF6.1) y todos sus techos;
6. sección de trabajo relacionado basada en esta auditoría;
7. anexos reproducibles para EF-2--EF-4, sin presentar `n=6,...,9` como evidencia
   asintótica.

Antes de integrar o enviar, hacen falta dos revisiones independientes:

- una revisión de combinatoria/probabilidad del certificado completo, en especial la
  tricotomía de rivales de EF-4;
- una búsqueda de prioridad por una persona con acceso a índices bibliográficos y
  cadenas de citación completas.

EF-5 no figura entre esos requisitos. Puede abrirse después para estudiar la
organización fina de las fibras, pero no cambia el teorema, su prueba ni la decisión
de cierre.

## 8. Fuentes primarias verificadas

### Causal sets y 2-orders

- L. Bombelli, J. Lee, D. Meyer y R. D. Sorkin, *Space-Time as a Causal Set*,
  Physical Review Letters 59 (1987), 521--524,
  [doi:10.1103/PhysRevLett.59.521](https://doi.org/10.1103/PhysRevLett.59.521).
- J. Myrheim, *Statistical Geometry*, CERN-TH-2538 (1978),
  [registro CERN](https://cds.cern.ch/record/293594).
- J. Henson, *Constructing an interval of Minkowski space from a causal set*,
  Classical and Quantum Gravity 23 (2006), L29--L35,
  [arXiv:gr-qc/0601069](https://arxiv.org/abs/gr-qc/0601069).
- M. Saravani y S. Aslanbeigi, *On the Causal Set-Continuum Correspondence*,
  Classical and Quantum Gravity 31 (2014), 205013,
  [arXiv:1403.6429](https://arxiv.org/abs/1403.6429).
- C. J. Fewster, E. Hawkins, C. Minz y K. Rejzner, *Local Structure of Sprinkled
  Causal Sets*, Physical Review D 103 (2021), 086020,
  [arXiv:2011.02965](https://arxiv.org/abs/2011.02965).

### Estadísticos de orden y combinatoria enumerativa

- A. Rényi, *On the Theory of Order Statistics*, Acta Mathematica Academiae
  Scientiarum Hungaricae 4 (1953), 191--231,
  [doi:10.1007/BF02127580](https://doi.org/10.1007/BF02127580).
- R. Pyke, *Spacings*, Journal of the Royal Statistical Society B 27 (1965),
  395--436,
  [doi:10.1111/j.2517-6161.1965.tb00602.x](https://doi.org/10.1111/j.2517-6161.1965.tb00602.x).
- C. Schensted, *Longest Increasing and Decreasing Subsequences*, Canadian Journal
  of Mathematics 13 (1961), 179--191,
  [doi:10.4153/CJM-1961-015-3](https://doi.org/10.4153/CJM-1961-015-3).
- D. E. Knuth, *Permutations, Matrices, and Generalized Young Tableaux*, Pacific
  Journal of Mathematics 34 (1970), 709--727,
  [doi:10.2140/pjm.1970.34.709](https://doi.org/10.2140/pjm.1970.34.709).
- A. Regev, *Asymptotic Values for Degrees Associated with Strips of Young
  Diagrams*, Advances in Mathematics 41 (1981), 115--136,
  [doi:10.1016/0001-8708(81)90012-8](https://doi.org/10.1016/0001-8708%2881%2990012-8).
- I. M. Gessel, *Symmetric Functions and P-Recursiveness*, Journal of Combinatorial
  Theory A 53 (1990), 257--285,
  [doi:10.1016/0097-3165(90)90060-A](https://doi.org/10.1016/0097-3165%2890%2990060-A).
- P. Clifford y R. Clifford, *Exact Sampling of Permutations with a Fixed Longest
  Increasing Subsequence* (2026),
  [arXiv:2606.02263](https://arxiv.org/abs/2606.02263).

### Concentración, procesos de rangos y selección adaptativa

- W. Hoeffding, *Probability Inequalities for Sums of Bounded Random Variables*,
  Journal of the American Statistical Association 58 (1963), 13--30,
  [doi:10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830).
- R. J. Serfling, *Probability Inequalities for the Sum in Sampling without
  Replacement*, Annals of Statistics 2 (1974), 39--48,
  [doi:10.1214/aos/1176342611](https://doi.org/10.1214/aos/1176342611).
- J.-D. Fermanian, D. Radulović y M. Wegkamp, *Weak Convergence of Empirical Copula
  Processes*, Bernoulli 10 (2004), 847--860,
  [doi:10.3150/bj/1099579158](https://doi.org/10.3150/bj/1099579158).
- C. Hoppen, Y. Kohayakawa, C. G. T. A. Moreira, B. Ráth y R. M. Sampaio,
  *Limits of Permutation Sequences*, Journal of Combinatorial Theory B 103 (2013),
  93--113, [arXiv:1103.5844](https://arxiv.org/abs/1103.5844).
- M. Kulldorff, *A Spatial Scan Statistic*, Communications in Statistics: Theory and
  Methods 26 (1997), 1481--1496,
  [doi:10.1080/03610929708831995](https://doi.org/10.1080/03610929708831995).
- G. Walther, *Optimal and Fast Detection of Spatial Clusters with Scan Statistics*,
  Annals of Statistics 38 (2010), 1010--1033,
  [arXiv:1002.4770](https://arxiv.org/abs/1002.4770).
- E. Arias-Castro, R. M. Castro, E. Tánczos y M. Wang, *Distribution-Free Detection
  of Structured Anomalies: Permutation and Rank-Based Scans*, Journal of the
  American Statistical Association 113 (2018), 789--801,
  [arXiv:1508.03002](https://arxiv.org/abs/1508.03002).
- W. Fithian, D. Sun y J. Taylor, *Optimal Inference After Model Selection* (2014),
  [arXiv:1410.2597](https://arxiv.org/abs/1410.2597).
- J. D. Lee, D. L. Sun, Y. Sun y J. E. Taylor, *Exact Post-Selection Inference, with
  Application to the Lasso*, Annals of Statistics 44 (2016), 907--927,
  [doi:10.1214/15-AOS1371](https://doi.org/10.1214/15-AOS1371).

## 9. Terminal de EF-6

```text
EF6_BIBLIOGRAPHIC_CUTOFF = 2026-08-12
EF6_DIRECT_PRECEDENT_FOUND = NO_WITHIN_SEARCHED_CORPUS
EF6_RESULT_CLASS = FAMILY_SPECIFIC_RESULT
EF6_PRIORITY_STATUS = PRIORITY_NOT_CERTIFIED
EF6_DESTINATION = STANDALONE_TECHNICAL_NOTE_BEFORE_MANUSCRIPT_INTEGRATION
EF6_EXTERNAL_MATH_REVIEW_REQUIRED = YES_BEFORE_SUBMISSION
EF6_EXTERNAL_PRIORITY_REVIEW_REQUIRED = YES_BEFORE_PRIORITY_LANGUAGE
EF6_EF5_DEPENDENCY = NONE
EF6_GAUSS_KUZMIN = NOT_SEARCHED
EF6_NEW_PATTERNS = NOT_SEARCHED
EF6_TERMINAL = COMPLETE
```
