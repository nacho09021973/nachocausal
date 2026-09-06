# Búsqueda bibliográfica crítica para la unicidad L² del operador integral antisimétrico degenerado K

> Nota de honestidad metodológica: cada referencia clave fue verificada (autor, título, año, venue, arXiv/DOI) mediante búsqueda directa y un agente de verificación dedicado. Donde no pude confirmar un número de teorema, una sección exacta o la aplicabilidad de un resultado, lo digo explícitamente. No se ha inventado ninguna referencia, arXiv ID ni enunciado.

---

## TL;DR

- **El operador K es, en su núcleo estructural, un modelo de Friedrichs** (multiplicación por la función degenerada (y−x) que se anula en la diagonal + perturbación de tipo Hardy/Cesàro/Volterra de estructura tensorial "de rango bajo"). Por tanto la pregunta "ker(K|Λ²L²)=span{g_t}" es exactamente **"el modelo de Friedrichs asociado no tiene autovalor cero salvo g_t"**, un problema de **inyectividad en un umbral embebido** — y esta familia de teoremas da inyectividad **sin coercividad**, que es justo lo que el usuario necesita.
- **Tres rutas de ataque reales y complementarias**: (1) reducir ker K a la anulación de un determinante de Weinstein–Aronszajn / ecuación de Birman–Schwinger (modelo de Friedrichs, Kato, Faddeev); (2) reducir Kg=0 a un sistema de EDOs con puntos singulares regulares en x=0,1 y usar los **exponentes indiciales** para forzar que solo g_t sea L² en ambos bordes (ruta más constructiva, donde el usuario ya tiene avances); (3) usar análisis de Mellin/operadores límite **solo** para clasificar los cuasimodos de borde y confirmar el espectro esencial, sabiendo que ese método da Fredholmicidad pero es **ciego a la inyectividad**.
- **El teorema más cercano "casi a medida"** es Iakovlev (2005) sobre modelos de Friedrichs con multiplicador que se anula en un umbral y donde el **rango de la perturbación controla la presencia/ausencia de autovalor**; pero ningún trabajo publicado enuncia exactamente "multiplicador que se anula en una diagonal (codimensión 1) + perturbación de rango tensorial bajo ⟹ inyectividad L²", lo que sugiere que el resultado del usuario, si se prueba, sería **genuinamente nuevo**.

---

## Key Findings

1. **Reclasificación del problema.** K = M + 6P, con M = multiplicación por (y−x) y P = (L⊗C − C⊗L + R⊗E − E⊗R). Esto es la firma exacta del modelo de Friedrichs: multiplicación por una función real + perturbación estructurada. El 0 es un valor **interior** del rango esencial de (y−x) (umbral embebido), lo que explica mecánicamente por qué falla la coercividad y aparecen cuasimodos, **sin** implicar núcleo no trivial.

2. **La inyectividad sin coercividad es el fenómeno estándar de estos modelos.** En el modelo de Friedrichs, "¿hay autovalor en z?" se reduce a "¿tiene núcleo no trivial I − A(z), A(z)=−V·R₀(z)?", es decir a la anulación de una función analítica/determinante finito — no a una cota inferior. El espectro esencial puede tocar 0 y aun así el autovalor cero puede estar ausente.

3. **El operador de Cesàro real C sobre L²(0,1) no tiene autovalores** (σ_p(C)=∅), confirmado en Belli–Gul–Ross–Siskakis, "The Cesàro operator on L²(0,1)", arXiv:2604.19691 (v2, 23 abr 2026; autores A. Belli, U. Gul, W. T. Ross [U. of Richmond], A. G. Siskakis [U. of Thessaloniki]), que establece norma, adjunto, normalidad y propiedades espectrales vía semigrupos de operadores de composición ponderados. Como C aparece dentro de P, su ausencia de autovalores es un ingrediente heredable.

4. **La carpeta "biblioteca" de Google Drive SÍ fue accesible pero NO contiene literatura de análisis funcional relevante** (ver sección (e)).

---

## Details

### (a) Diagnóstico estructural: a qué familia pertenece realmente K

Cuatro sub-estructuras identificables:

- **Multiplicación degenerada (y−x)** = el "H₀" del modelo de Friedrichs. Rango esencial = intervalo simétrico alrededor de 0; el 0 es umbral **interior** (embebido). Es lo que hace fallar la coercividad.
- **L, R, C, E** = operadores de Hardy–Cesàro–Volterra con núcleos polinómicos. C es esencialmente Cesàro; L es promedio de Hardy; los pesos 1/x, 1/x², 1/(1−x), 1/(1−x)² son de tipo Hardy de exponente **crítico** en los bordes.
- **L⊗C − C⊗L + R⊗E − E⊗R** = conmutador antisimetrizado / forma de tipo wedge; da a la perturbación su carácter de "rango bajo" respecto a estructuras tensoriales.
- **Λ²L²** = fuerza análisis de núcleos antisimétricos.

Reorientación central: el corazón del problema **no** es Fredholmicidad (que efectivamente falla), sino **inyectividad en umbral**.

### (b) Rutas de ataque

**Ruta 1 (la más prometedora): modelo de Friedrichs — inyectividad en umbral vía determinante de Fredholm / Birman–Schwinger.**
Escribir g∈ker K ⟺ (y−x)g = −6Pg. Como (y−x) se anula en la diagonal, dividir exige que Pg se anule en la diagonal (la "condición diagonal" que el usuario ya observó). Fuera de la diagonal g = −6Pg/(y−x); sustituir de vuelta da una ecuación de punto fijo cuyo núcleo se controla por un determinante.
Literatura (verificada): Friedrichs, "On the perturbation of continuous spectra", Comm. Pure Appl. Math. 1(4) (1948) 361–406, DOI 10.1002/cpa.3160010404 (hipótesis: núcleo Hölder que se anula en el borde + acoplamiento pequeño ⟹ equivalencia unitaria con la multiplicación, espectro puramente a.c.). Faddeev, Trudy Mat. Inst. Steklov 73 (1964) 292–313 / AMS Transl. Ser. 2, 62 (1967) 177–203 (Hölder α₀∈(1/2,1], simetría, anulación del núcleo en los extremos ⟹ sin espectro singular continuo; espectro puntual = conjunto finito de autovalores de multiplicidad finita).
**Encaja**: la estructura multiplicación + rango bajo. **Falla**: la hipótesis de que el núcleo se anule y sea Hölder **hasta el borde** — los pesos 1/x², 1/(1−x)² son singulares con exponente crítico. Por tanto los teoremas clásicos no se aplican directamente; hay que ver si la anulación en la diagonal + la regularidad interior ya probada bastan.
**¿Da unicidad sin coercividad? SÍ** — es precisamente lo que caracteriza a estos modelos.

**Ruta 2: fórmula de Weinstein–Aronszajn / determinante finito.**
Si P es genuinamente reducible a estructura finita módulo la multiplicación, ker K se reduce a la anulación de ω(z)=det(I+V·R₀(z)) evaluado en z=0. Fuentes verificadas: R. Bouldin, Pacific J. Math. 31(1) (1969); J. S. Howland, "On the Weinstein–Aronszajn formula", Arch. Rational Mech. Anal. 39 (1970) 323–339, DOI 10.1007/BF00251295; S. T. Kuroda, Sci. Papers Coll. Gen. Ed. Univ. Tokyo 11 (1961) 1–12; libro base T. Kato, "Perturbation Theory for Linear Operators", Springer (1966; 2ª ed. 1976, que reescribió los §§ V-4.5, VI-4.3, VIII-1.4). **Encaja** si el rango efectivo es finito; **falla** la finitud literal (L,R,C,E son de rango infinito), pero la estructura ⊗ antisimetrizada podría tener rango efectivo bajo por bloques (armónicos/grados) — es una comprobación algebraica concreta, no abstracta.

**Ruta 3 (la más constructiva): reducción a EDO con puntos singulares regulares (Frobenius/exponentes indiciales).**
L,R,C,E tienen núcleos polinómicos en (x,s) del tipo (x−s), s, (1−s). Derivando Kg=0 respecto a x, y un número finito de veces, se eliminan las integrales y queda un sistema de EDOs con coeficientes racionales singulares en x=0,1. Los pesos 1/x, 1/x², 1/(1−x), 1/(1−x)² son exactamente coeficientes de tipo Euler/Fuchs; los **exponentes indiciales** en cada borde dicen qué soluciones son L². La ecuación hipergeométrica (puntos singulares regulares en 0,1,∞) es el análogo canónico. Marco preciso exponentes↔pesos L²: M. Lesch, "Operators of Fuchs type, conical singularities and asymptotic methods", Teubner-Texte Math. 136 (1997); b-calculus de Melrose. **Encaja muy bien** (el usuario ya tiene "kernel polinómico = span{g_t}" y "regularidad interior"). **Dificultad**: la diagonal x=y es una segunda superficie singular que acopla las variables; puede requerir tratarla como característica. Estrategia: calcular la ecuación indicial en x→0 y x→1, y demostrar que solo la combinación correspondiente a g_t es simultáneamente L² en ambos bordes, antisimétrica y compatible en la diagonal — un problema de conexión donde solo un modo "cuantizado" sobrevive.

**Ruta 4: análisis de Mellin / operadores límite — por qué da Fredholm pero NO unicidad.**
Fuentes verificadas: Rabinovich–Roch–Silbermann, "Limit Operators and Their Applications in Operator Theory", OT 150, Birkhäuser (2004) (Fredholm ⟺ todos los operadores límite invertibles); Duduchava, "Mellin Convolution Equations", Springer (2019); arXiv:1704.08932 (álgebra de Mellin+Wiener–Hopf, ecuación transcendental con funciones gamma que determina Fredholmicidad e índice); operador de Wiener–Hopf con símbolo con ceros = NO Fredholm. **Clave**: el método caracteriza invertibilidad módulo compactos y el espectro esencial, pero es **ciego a la inyectividad global** — un operador puede tener todos sus operadores límite no invertibles y aun así ser inyectivo. El "modelo normal lateral con kernel L² infinito-dimensional" que reporta el usuario es un operador límite con núcleo grande (explica el fallo de Fredholm y los cuasimodos), **no** implica núcleo grande de K global. Usar Mellin para: (i) confirmar que 0 es umbral embebido; (ii) clasificar los cuasimodos de borde como no-L² o pertenecientes a operadores límite pero no a K.

**Ruta 5 (complementaria, baja prioridad): Liouville/Choquet–Deny/Mourre/positividad.**
Choquet–Deny (C.R. Acad. Sci. Paris 250 (1960) 799–801); Liouville no local (Fall–Weth, Potential Anal. 45 (2016) 187–200; arXiv:2301.08540); Mourre (Amrein–Boutet de Monvel–Georgescu). **Especulativo**: la positividad degenerada ya falla y K es antisimétrico (no generador de Markov evidente); Mourre requiere operador conjugado y es delicado para operadores no autoadjuntos. Útil solo como control cruzado.

### (c) Teoremas "casi hechos a medida"

**Candidato principal — Iakovlev (2005).** S. I. Iakovlev, "Friedrichs model operators of absolute type with one singular point", Electron. J. Differential Equations, Conference 13 (2005), 49–56 (8 pp.; verificado en EuDML doc/125487). Para A_m = |t|^m·+V en L²(ℝ), con el multiplicador |t|^m que se anula en el umbral t=0 de orden m>0 y V perturbación integral (traza, ≥0), da condiciones **necesarias y suficientes** para la ausencia de espectro puntual y singular continuo cerca del origen. Cita verbatim del abstract: *"These absolute type operators have one singular point t=0 of positive order. We find conditions that guarantee the absence of point spectrum and the singular continuous spectrum for such operators near the [singular point]."* Para m∈(1,3] la condición depende del **rango de V**: si rank V<∞ y el módulo de continuidad del núcleo cumple ω(t)=O(t^((m−1)/2)) cuando t→0, no hay espectro singular cerca de 0. **Agudeza** (paper hermano de Iakovlev, Int. J. Math. Math. Sci., vol. 2003): *"For every m>3/2, we construct a rank-1 perturbation from the class Lip 1 such that the corresponding operator has a sequence of eigenvalues converging to zero"* — para m>3/2 no hay condición de finitud del espectro singular en términos del módulo de continuidad.
**Por qué es casi a medida**: es la estructura exacta — multiplicador que se anula en un umbral + rango de la perturbación controlando la presencia de autovalor. **Qué comprobar en nuestro caso**: (1) traducir "(y−x) se anula en la diagonal" (codimensión 1) a la geometría de un umbral puntual — **esta es la brecha principal**; (2) el orden de anulación (aquí (y−x) se anula a orden 1 transversalmente); (3) el módulo de continuidad de L,R,C,E cerca de diagonal y bordes; (4) el análogo tensorial de "rango finito". **Advertencia**: el agente de verificación confirmó que **ningún** paper enuncia exactamente "cero interior del multiplicador + rango finito ⟹ inyectividad"; Iakovlev es para un multiplicador escalar |t|^m en ℝ con umbral en el extremo de [0,∞), no para una diagonal en un producto. Es una **plantilla, no una solución**.

**Candidato secundario — Faddeev (1964).** Da el **paradigma de demostración** (t-operador, ecuación característica) más que un teorema aplicable, porque sus hipótesis de regularidad en el borde fallan en el borde crítico.

### (d) Ranking de lecturas prioritarias

1. **T. Kato, "Perturbation Theory for Linear Operators", Springer (1966; 2ª ed. 1976).** Contiene la fórmula de Weinstein–Aronszajn (reducción a ceros de un determinante finito — Ruta 2), perturbaciones de rango finito, estabilidad del espectro esencial. *[Sección exacta no confirmada; Kato cita a Howland 1970 en su bibliografía.]*
2. **L. D. Faddeev (1964/1967).** Trudy Mat. Inst. Steklov 73, 292–313 / AMS Transl. Ser. 2, 62 (1967), 177–203. El paradigma completo de ausencia de autovalores embebidos vía t-operador. *[Verificado; números de teorema internos no confirmados.]*
3. **S. I. Iakovlev (2005), EJDE Conf. 13, 49–56.** El teorema estructuralmente más cercano (multiplicador que se anula en umbral + rango controla autovalor). *[Verificado, incl. abstract verbatim.]*
4. **H. Isozaki, S. Richard, "On the wave operators for the Friedrichs-Faddeev model", Ann. Henri Poincaré 13 (2012), 1469–1482; arXiv:1108.5813.** Presentación moderna con hipótesis exactas (Hölder α₀>1/2, anulación en extremos) y la correspondencia autofunciones ↔ soluciones de A(λ±i0)g=g (la ecuación de inyectividad a analizar). *[Verificado.]*
5. **A. Belli, U. Gul, W. T. Ross, A. G. Siskakis, "The Cesàro operator on L²(0,1)", arXiv:2604.19691 (presentado 21 abr 2026, v2 23 abr 2026)** y el compañero **"Crescents and the real variable Cesàro operator", arXiv:2606.08600 (7 jun 2026)** (espectro = dominio en forma de creciente dependiente de p en L^p). Norma, adjunto, normalidad y σ_p(C)=∅. Directamente relevante porque C aparece en K. *[Verificado; preprints muy recientes de 2026 — corroborar antes de citar como definitivo.]*
6. **I. C. Gohberg, M. G. Krein, "Theory and Applications of Volterra Operators in Hilbert Space", Transl. Math. Monogr. 24, AMS (1970).** Para L,R (Volterra): espectro {0}, sin autovalores; factorización triangular. *[Verificado.]*
7. **V. Rabinovich, S. Roch, B. Silbermann, "Limit Operators and Their Applications in Operator Theory", OT 150, Birkhäuser (2004).** Para entender por qué el método da Fredholm pero no unicidad, y caracterizar espectro esencial y cuasimodos. *[Verificado.]*
8. **R. Melrose, "The Atiyah–Patodi–Singer Index Theorem" (b-calculus) / M. Lesch, "Operators of Fuchs type, conical singularities and asymptotic methods" (Teubner-Texte Math. 136, 1997).** Ruta 3: raíces indiciales ↔ pesos L² admisibles, regularidad conormal en bordes. *[Verificado como marco; teoremas específicos no confirmados individualmente.]*

Complementos (segunda línea): L. Sakhnovich, "Integral triangular operators and Friedrichs model", arXiv:1504.05007 (verificado: construye modelos de Friedrichs triangulares similares a un autoadjunto con espectro a.c.); **S. Albeverio, S. Lakaev, Z. Muminov, "The threshold effects for a family of Friedrichs models under rank one perturbations", arXiv:math/0604277 (12 abr 2006)** — prueba existencia de autovalor único bajo el fondo del espectro esencial y obtiene la expansión en umbral del **determinante de Fredholm**; y su compañero arXiv:math/0604282 ("Low energy effects...") y arXiv:1412.0598 (Lakaev et al., familia con perturbación de rango uno).

---

## Recommendations

**Secuencia de trabajo escalonada:**

1. **Primer paso (Ruta 3 — máxima probabilidad de cerrar el problema):** llevar a cabo la reducción a EDO. Aplicar los operadores diferenciales que aniquilan los núcleos polinómicos (p. ej. x²∂ₓ sobre los términos con 1/x² y núcleo lineal) para convertir Kg=0 en un sistema diferencial con puntos singulares regulares en x=0,1. Calcular la ecuación indicial en cada borde. **Benchmark de éxito**: si se demuestra que en cada borde solo un exponente indicial da g∈L², y que solo g_t satisface simultáneamente ambos bordes + antisimetría + compatibilidad en la diagonal, la conjetura queda probada. **Umbral que cambiaría la estrategia**: si aparecen exponentes indiciales confluentes (raíces que difieren en un entero, con términos logarítmicos) o si la diagonal resulta ser una singularidad no-Fuchsiana, pasar a la Ruta 1/2.

2. **En paralelo (Ruta 1/2):** identificar el rango efectivo de P por bloques (armónicos/grados) y comprobar si ker K se reduce a la anulación de un determinante de Weinstein–Aronszajn analítico explícito. **Benchmark**: si el rango efectivo por bloque es finito, escribir ω(z) y verificar que solo se anula en el modo g_t. **Umbral**: si el rango efectivo no se factoriza en bloques finitos, este camino se abandona a favor de la Ruta 3 pura.

3. **Blindaje (Ruta 4):** usar Mellin/operadores límite para clasificar rigurosamente los cuasimodos de borde y demostrar que **no** pertenecen al núcleo L² de K global. **Benchmark**: mostrar que cada cuasimodo lateral es o bien no-L² o bien un elemento del operador límite pero no de K. Esto no prueba unicidad por sí solo, pero cierra la objeción de los canales de borde.

4. **No invertir esfuerzo** en coercividad (global o módulo compactos), en el método de operadores límite como vía **directa** de unicidad, ni en argumentos de positividad/Markov/Mourre, salvo como controles cruzados (justificación en Caveats).

**Sobre la novedad:** dado que no existe un teorema publicado exactamente adaptado (multiplicador que se anula en una diagonal de codimensión 1 + perturbación de rango tensorial bajo ⟹ inyectividad L²), conviene enmarcar el resultado, si se obtiene, como una **extensión del modelo de Friedrichs a multiplicadores que se anulan en subvariedades de codimensión 1**, citando Iakovlev y Faddeev como precursores del caso puntual.

---

## Caveats — lo que NO he podido verificar y callejones descartados

**Acceso a la carpeta "biblioteca" de Google Drive: SÍ accedí,** pero **NO contiene literatura de análisis funcional relevante**. Contiene: el manuscrito propio del usuario (`manuscript_limits_draft.md`, sobre límites de identificabilidad "order-only" de parches de Schwarzschild en causal sets — un problema distinto del de este operador), dos páginas .mht de causal sets, un documento largo de biblioteca de causal sets, y papers no relacionados (conjetura de Erdős–Hajnal, convergencia de Collatz). No hay ningún PDF sobre modelo de Friedrichs, operadores de Hardy/Cesàro/Volterra ni edge calculus. **La biblioteca del usuario no aportó fuentes para este problema.**

**No he podido verificar:**
- La **sección/número de teorema exactos en Kato** para Weinstein–Aronszajn (la 2ª ed. de 1976 reescribió los §§ V-4.5, VI-4.3, VIII-1.4; Kato cita a Howland 1970 en bibliografía, pero no confirmé la ubicación precisa).
- Que exista un teorema publicado que enuncie **exactamente** "multiplicador que se anula en una diagonal (codimensión 1) + perturbación de rango tensorial bajo ⟹ inyectividad L²". No lo encontré; parece un **hueco genuino** en la literatura.
- Los **números de teorema específicos** dentro de Faddeev (1964) y de las monografías de Melrose/Lesch (solo verifiqué contenido y existencia generales, no numeraciones internas).
- Los preprints de Cesàro (arXiv:2604.19691, arXiv:2606.08600) son de **2026** y muy recientes; conviene reconfirmar sus enunciados antes de citarlos como definitivos.

**Callejones descartados y por qué:**
- **Coercividad global / módulo compactos**: descartado (el usuario ya lo constató; estructuralmente inevitable porque 0 es umbral embebido). No insistir.
- **Operadores límite como vía directa de unicidad**: da Fredholmicidad (que falla) y espectro esencial, pero es **intrínsecamente ciego a la inyectividad**. Útil solo como diagnóstico.
- **Positividad/Markov (Choquet–Deny, Liouville)**: especulativo y de baja prioridad — la positividad degenerada ya falla y K es antisimétrico, no generador de Markov evidente.
- **Teoría de Mourre**: baja prioridad por el carácter no autoadjunto de K y la dificultad de construir el operador conjugado en el umbral.

**Honestidad sobre el grado de certeza:** ninguna de las rutas es una demostración lista; son plantillas verificadas cuya aplicabilidad exige comprobaciones concretas (señaladas una a una). La afirmación más sólida es el **diagnóstico**: este es un problema de inyectividad de un modelo de Friedrichs en umbral, y esa familia de resultados es la única que da unicidad sin coercividad. La Ruta 3 (EDO/exponentes indiciales) es la que más probablemente cierre el problema por ser constructiva y compatible con los avances ya logrados por el usuario.