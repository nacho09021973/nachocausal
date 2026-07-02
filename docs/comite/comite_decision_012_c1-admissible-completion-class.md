# Comité Decision 012 — C1 admissible completion class adjudication

> Convocado por instrucción explícita del usuario a partir del expediente
> `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` (R4, `C1_DEFINITION_STATUS = READY_FOR_COMMITTEE_012`).
> Sesión **exclusivamente deliberativa y documental**: no se ejecutó ninguna simulación, sprinkling,
> búsqueda de contraejemplos, prueba Alloy, formalización Lean, análisis estadístico ni modificación
> de código. Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`. El comité PROPONE; el usuario/PI AUTORIZA.

## 1. Decision question

> ¿Qué definición exacta, mínima y físicamente defendible debe adoptar el proyecto para la clase de
> completaciones admisibles C1, y qué requisitos deben quedar cerrados antes de que C1 pueda usarse
> para evaluar identificabilidad física?

## 2. Verified state (lectura, no ejecución)

Archivos leídos íntegros esta sesión, cada uno con su rol en la adjudicación:

| Archivo | Rol en esta sesión |
|:---|:---|
| `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` (R4) | Expediente de entrada — cinco cláusulas C1 (a–e), obligaciones físicas §4, cinco términos comité 011 §5, estados Alloy/boundary-bracket, decisiones abiertas §8 |
| `dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md` (R3) | Fórmula exacta de `cov_honest`, tabla por densidad, veredicto `LOCALISED_TO_BOUNDARY_BRACKET`, `CONFIDENCE = MEDIUM` |
| `docs/comite/comite_decision_011_patch-ensemble-architecture.md` | Origen exacto de los cinco términos arquitectónicos ("parches locales", "ensamblaje", "compatibilidad causal", "cobertura transversal", "S¹/S²"), dissent del físico sobre coverage en 1+1D, `BLOCK-1..5` |
| `docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md` | Origen exacto de los cinco términos C1 (observed subposet class, admissible completion class 𝔄, induced reference rule, pullback rule, incompatibility predicate), verdict `NEEDS_PRECISE_COMPLETION_CLASS`, minimal falsification test prescrito §9 step 1 |
| `dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md` | Proposición original `COMPLETION_AND_TRUNCATION_NONIDENTIFIABILITY`, cinco términos "Required definitions before proof" (líneas 91–106), estado `LOGICAL_NONIDENTIFIABILITY_LAYER_SUPPORTED / PHYSICAL_LAYER_OPEN` (pre-R1) |
| `docs/alloy/alloy_verification_002_completion-nonidentifiability-interface.md` | Reporte Alloy 002 original: `ALLOY_VERDICT=ALLOY_COUNTEREXAMPLE_FOUND`, scope `exactly 4 Element`, traza literal |
| `dev/alloy/product_order_check_alloy002_witness_note.md` | R1 ejecutado: chequeo de convexidad + `dim_DM ≤ 2` sobre el testigo Alloy 002; veredicto `PHYSICAL_LAYER_EMPTY_EVIDENCE` |
| `nachocausal/c1_selector.py`, `nachocausal/selection_guard.py` | Único selector C1 implementado (`R=Max(C)`, trivial `NO_INTERFACE`) y único guard de relabel-invarianza (por selector, no por unión) |
| `dev/PR003_C1_RELATIONAL_SPEC.md` | Confirma `ASYMMETRY_SCORE`, `PERSISTENCE_THRESHOLD`, `BULK_CONTROL`, `C1_PROMOTION` todos `OPEN` |
| `docs/preregistration.md`, `docs/preregistration_001_addendum.md`, `docs/preregistration_002.md` | Búsqueda de definiciones preexistentes de convexidad/dimensión/orden-producto/completación admisible/subposet observado — **ninguna encontrada** (`rg` sin resultados); confirma que estos términos no tienen ancla previa fuera de R4 |

No se generaron nuevos archivos de evidencia. Ningún seed fue extraído. `thresholds.py` no fue leído
ni modificado (no aplica: esta sesión es puramente conceptual, no toca el path sellado).

**Terminología preservada sin sinónimos** (obligación explícita): `boundary-bracket`, `S3`,
`cov_honest`, `𝔄`, `PHYSICAL_LAYER_EMPTY_EVIDENCE`, `dim_DM ≤ 2`, "parches locales", "ensamblaje",
"compatibilidad causal", "cobertura transversal", "S¹/S²" — usados exactamente como aparecen en
las fuentes citadas, sin reemplazo por paráfrasis.

## 3. Jerarquía conceptual (obligatoria, sin inferencia automática entre niveles)

| Nivel | Objeto | Estado actual | Evidencia |
|:---:|:---|:---|:---|
| **1. Testigo lógico** | Dos completaciones abstractas con el mismo observable inducido | `PRESENT` | Alloy 002, traza literal (`alloy_verification_002...md` §4) |
| **2. Testigo de orden causal** | Ambas extensiones son órdenes parciales estrictos válidos | `SATISFIED` por A y B | `product_order_check_alloy002_witness_note.md` §4, fila "Valid strict partial order: ✓✓" |
| **3. Testigo bidimensional** | Ambas extensiones son realizables como orden producto (`dim_DM ≤ 2`) | `SATISFIED` por A **y** B — no discrimina | `product_order_check_alloy002_witness_note.md` §4, ambas filas "2D product-order realizable: ✓" |
| **4. Testigo físico** | Extensión compatible con la clase física 𝔄 (una vez cerrada) | Completion A: satisface convexidad. Completion B: **viola** convexidad. Ninguna completación satisface simultáneamente 𝔄 (aún sin cerrar del todo) Y produce la decisión incompatible — el único par que discrepa en interfaz depende de la completación no admisible | `witness_note.md` §4, fila convexidad |
| **5. Resultado del estimador** | Comportamiento de `boundary-bracket`/S3 bajo el protocolo estadístico (densidad, seeds) | `FAILED_BASELINE_UNDER_PRECOMMITTED_DENSITY_COVERAGE_CRITERION` — **eje completamente distinto**, no es un testigo de completación en absoluto | `dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md` §4,6,8 |

**Regla de no-inferencia:** superar el nivel 1 (existencia lógica) no implica nada sobre el nivel 2
(ya lo cumplen ambas, trivialmente). Superar 2 no implica 3 (ambas también lo cumplen, lo cual
sorprendió la predicción previa de comité 010 — ver D2). Superar 3 no implica 4 (B pasa el nivel 3 y
falla el nivel 4). El nivel 5 no es una escala superior de los niveles 1–4: es un eje ortogonal
(desempeño estadístico de un selector concreto bajo densidad), y no debe usarse para certificar ni
refutar nada sobre 𝔄 o sobre no-identificabilidad física, ni al revés.

## 4. Cinco decisiones obligatorias

### D1. Contenido exacto de la clase admisible 𝔄

| Condición | Posición PI | Posición matemático/formalista | Posición físico | Posición ingeniería/reproducibilidad | Objeciones | Decisión consolidada | Confianza | Evidencia |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Preservación literal del subposet observado | Exigido desde el inicio de R1–R4; sin esto no hay "completación de `C`" en absoluto | Es la definición misma de completación: `i: C ↪ C1` order-embedding | Corresponde a "el observado no cambia al completar" — condición física trivial | Ya implementado implícitamente en el testigo (`witness_note.md` §2: Observation `{E2,E3}` idéntica en A y B) | Ninguna | `MANDATORY` | ALTA | R4 §2-3; `witness_note.md` §2 |
| Orden parcial causal (irreflexivo, transitivo) | Exigido; sin esto no hay "extensión de un causal set" | Definitorio de "poset" | Definitorio de "orden causal" | Ya chequeado ejecutablemente (`product_order_check...py` §3 punto 2) | Ninguna | `MANDATORY` | ALTA | `witness_note.md` §3-4 |
| Ausencia de elementos ocultos causalmente inadmisibles (formulación general) | Aceptado como principio; su formalización concreta es la fila de convexidad | Es la misma obligación que convexidad, redactada con otras palabras (R4 §4 "Nota de disciplina") | Corresponde exactamente a "un elemento oculto no puede truncar el interior de forma físicamente espuria" | De acuerdo en no duplicar el chequeo | Falsificador (voz retenida de comité 010): riesgo de contarla dos veces y aparentar dos obligaciones independientes cuando es una sola | `MANDATORY` (idéntica a convexidad, ver D2) | ALTA | R4 §4, nota de disciplina |
| Convexidad del observado | Ver D2 | Ver D2 | Ver D2 | Ver D2 | Ver D2 | **Ver D2** | Ver D2 | Ver D2 |
| Realizabilidad como orden producto | Ver D2 | Ver D2 | Ver D2 | Ver D2 | Ver D2 | **Ver D2** | Ver D2 | Ver D2 |
| Dimensión de orden ≤ 2 | Ver D2 (misma obligación matemática que la fila anterior, dos nombres) | Confirma equivalencia: `dim_DM ≤ 2 ⟺` realizable como orden producto de 2 órdenes lineales (Dushnik–Miller) | — | — | — | **Ver D2** (una sola obligación, dos redacciones) | Ver D2 | Ver D2 |
| Compatibilidad con una región de Schwarzschild | Deseable a largo plazo; no bloquea el cierre parcial de hoy | No hay predicado ejecutable; formalizarlo ahora sería inventar contenido no respaldado | Coincide con la descripción de comité 010 ("2D-product-order manifoldlike extensions of the f(r) family") pero eso es descriptivo, no un test | No hay código que lo implemente sobre una completación arbitraria — solo el generador produce instancias concretas | Riesgo de fuga de ground truth si se define usando `r=2M` directamente (comité 010 §8, riesgo 1) | `DEFERRED` | MEDIA | R4 §4 fila 5; `comite_decision_010.md:101` |
| Manifoldlikeness | Igual que arriba | Igual — sin predicado ejecutable sobre completaciones arbitrarias | El generador SÍ verifica esto para sus propias salidas (`generator.py:53-82`, χ² gate), pero eso no cubre completaciones combinatorias externas | Confirma: `generator.py:53-82` es un gate del generador, no un test de admisibilidad de 𝔄 | Ninguna nueva | `DEFERRED` | MEDIA | R4 §4 fila 6 |
| Procedencia mediante sprinkling | No debe exigirse como necesaria — bastaría con que la completación sea consistente con *algún* sprinkling, no que haya sido literalmente generada por uno | De acuerdo: sprinkling-origen es una condición suficiente construible, no necesaria para admisibilidad lógica | El sprinkling es cómo el proyecto construye instancias concretas, pero la admisibilidad física de una completación abstracta no requiere haber sido muestreada | Es la vía práctica para construir testigos futuros (`Alloy 003`, si se autoriza) | Ninguna | `OPTIONAL_DIAGNOSTIC` | MEDIA | R4 §4 fila 6; `generator.py:53-82` |
| Restricciones de **localización** de elementos ocultos | Ya cubierta por convexidad | Idéntica a convexidad (ver arriba) | Idéntica a convexidad | Ya ejecutada | Ninguna | `MANDATORY` (= convexidad, D2) | ALTA | `witness_note.md` §3-4 |
| Restricciones de **número** de elementos ocultos | No hay evidencia de que el número importe — el testigo Alloy 002 solo varía posición (un elemento oculto en cada completación), no cantidad | Ningún argumento matemático a favor de un límite de cardinalidad ha sido propuesto en el repo | Ninguna intuición física registrada distingue "un elemento oculto" de "varios" siempre que la posición sea admisible | No hay chequeo ejecutable para esto | Falsificador: no confundir ausencia de evidencia con evidencia de innecesariedad | `DEFERRED` — ni se adopta ni se rechaza; no probado en ninguna dirección | BAJA | Ausencia de evidencia (§2 de esta acta) |

**Nota explícita:** ninguna fila recibe una etiqueta compartida con otra que pudiera merecer una
decisión distinta (instrucción explícita cumplida): convexidad/dimensión se resuelven por separado
en D2 con su propio vocabulario, aunque D1 registra la etiqueta genérica que les correspondería.

---

### D2. Convexidad y dimensión de orden

```text
CONVEXITY_REQUIREMENT = MANDATORY_FOR_C1
ORDER_DIMENSION_LE_2_REQUIREMENT = REQUIRED_ONLY_FOR_A_NAMED_SUBCLASS
```

**Subclase nombrada:** `𝔄_Schw` — completaciones que además de satisfacer 𝔄 provienen de la
familia de generadores 1+1D Eddington–Finkelstein sellada (`generator.py`), para las cuales
`dim_DM ≤ 2` se espera por regularidad de Kruskal–Szekeres (Prop 7.3, citada en
`comite_decision_010.md:72,95`). Para la clase general 𝔄 (no restringida a `𝔄_Schw`), la exigencia
de dimensión ≤ 2 queda `UNRESOLVED` — no se adopta ni se descarta.

| | Posición PI | Posición matemático/formalista | Posición físico | Posición ingeniería/reproducibilidad |
|:---|:---|:---|:---|:---|
| **Convexidad** | Es la única obligación que, ejecutada, discrimina el testigo disponible; adoptarla es el mínimo defendible hoy | La formalización operacional ya existe y ya se ejecutó (`witness_note.md` §3 punto 4); no hay razón para no adoptarla como mínimo | Coincide exactamente con el mecanismo físico documentado del proyecto — el observable rastrea truncación por posición causal (interior vs exterior), no por número de elementos ocultos | El chequeo ya es código ejecutable, reproducible, sin nuevas dependencias | Falsificador: la evidencia es un único testigo combinatorio de 4 elementos (`exactly 4 Element`), no una prueba general; adoptar convexidad como `MANDATORY` sobre la base de n=1 es una generalización, no una demostración |
| **Dimensión ≤ 2** | No debe deducirse obligatoria solo porque el generador actual produce completaciones 2D (instrucción explícita del brief) | El propio testigo Alloy 002 **refuta** la expectativa previa de comité 010: la predicción de que "one-element extensions... are neither convex nor product-order-realisable" (`comite_decision_010.md:78`) resultó **falsa** para la realizabilidad-producto — ambas completaciones A y B pasan `dim_DM ≤ 2` (`witness_note.md` §4). El chequeo de dimensión no hizo ningún trabajo discriminante en este testigo | Prop 7.3 es "asserted by generator audit, not measured" (`comite_decision_010.md:72`) — no hay una fuente que pruebe que la admisibilidad física exige dimensión ≤ 2 en general, solo que el generador concreto la produce | De acuerdo en no generalizar; el chequeo de dimensión sigue siendo útil como diagnóstico dentro de `𝔄_Schw`, no como filtro universal |

**Decisión consolidada:** `CONVEXITY_REQUIREMENT = MANDATORY_FOR_C1` (confianza MEDIA — único
discriminante disponible, pero basado en un solo testigo de escala 4); `ORDER_DIMENSION_LE_2_REQUIREMENT
= REQUIRED_ONLY_FOR_A_NAMED_SUBCLASS` (`𝔄_Schw`; confianza BAJA-MEDIA — la propia Prop 7.3 en la que
se apoya está marcada "asserted, not measured", y el testigo disponible muestra que la dimensión no
discrimina nada por sí sola).

**Objeción retenida (falsificador):** ninguna de las dos decisiones anteriores está probada más allá
del testigo de 4 elementos disponible. Escalar el chequeo de convexidad/dimensión a un scope Alloy
mayor (5, 6, ... elementos) — **no ejecutado en esta sesión, por restricción explícita del usuario**
— sigue siendo la obligación pendiente que podría revertir o reforzar D2.

---

### D3. Cobertura transversal

**Decisión:** opción 3 del brief — **ambas como métricas distintas**, con nombres separados y
prohibición explícita de equipararlas.

```text
S3_HONEST_COVERAGE := cov_honest = n_covering / n_cand
  (definida exactamente en dev/measure_iterative_reseed_v1.py; reportada en
  dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md §3; NO se modifica aquí)

GENUINE_TRANSVERSAL_COVERAGE := UNDEFINED
  (requeriría una sección espacial genuina del horizonte — S¹ en 2+1D, S² en 3+1D —
  que no existe en el dominio 1+1D actual; fuera de alcance, BLOCK-4 comité 011)
```

| | Posición PI | Posición matemático/formalista | Posición físico | Posición ingeniería/reproducibilidad |
|:---|:---|:---|:---|:---|
| Posición sobre la identidad de los dos términos | Deben distinguirse por nombre para que ningún resultado futuro sobre `S3_HONEST_COVERAGE` se lea accidentalmente como progreso sobre cobertura genuina | De acuerdo — son objetos de tipo distinto: uno es una fracción sobre frentes 1D, el otro requeriría un objeto límite (nervio, persistencia) inexistente en el repo | Es quien primero señaló el dissent (comité 011 §8): en 1+1D el horizonte es `S⁰` (dos puntos), no hay superficie que cubrir; `S3_HONEST_COVERAGE` mide *tiling* de un generador nulo a lo largo de `t*`, no cobertura transversal | Ninguna objeción — el código de `S3_HONEST_COVERAGE` es el único ejecutable y no debe tocarse |

**Preservación obligatoria y explícita:**

```text
coverage: 51% → 48% → 44%  (S3_HONEST_COVERAGE, intensidades 3600/7200/14400)
```

sigue siendo un **`FAIL`** del ensamblaje/localizador S3 bajo el criterio precomprometido
`"coverage no se degrada (idealmente mejora) con densidad"` (`docs/hoja_de_ruta_24_jun_2026.md:64,80`).
Este comité **no sustituye** ese criterio ni lo reinterpreta. `GENUINE_TRANSVERSAL_COVERAGE` no tiene
ningún valor medido — no existe el dominio (2+1/3+1) donde evaluarla.

**Regla de uso:** ningún documento futuro puede citar `S3_HONEST_COVERAGE` como evidencia sobre
`GENUINE_TRANSVERSAL_COVERAGE`, ni viceversa. Son nombres distintos por decisión de este comité.

---

### D4. Cierre previo de la arquitectura

Se distinguen explícitamente los tres niveles exigidos por el brief: (i) definir C1 como objeto
matemático; (ii) evaluar C1 en la arquitectura concreta del proyecto; (iii) certificar
identificabilidad física.

| Término (comité 011) | (i) Definir C1 | (ii) Evaluar C1 en la arquitectura | (iii) Certificar identificabilidad física |
|:---|:---|:---|:---|
| Parches locales | `NOT_REQUIRED_FOR_C1` | `MAY_REMAIN_PROVISIONAL` — solo importa si algún testigo futuro se construye *usando* parches como mecanismo | `NOT_REQUIRED_FOR_C1` — el único testigo actual (Alloy 002) es abstracto, no usa parches |
| Ensamblaje | `NOT_REQUIRED_FOR_C1` | `MAY_REMAIN_PROVISIONAL` — pertenece a la pregunta arquitectónica de comité 011/013, no a C1 | `NOT_REQUIRED_FOR_C1` |
| Compatibilidad causal | `NOT_REQUIRED_FOR_C1` | `MUST_CLOSE_BEFORE_C1_EVALUATION` **solo si** la arquitectura de parches/ensamblaje llega a proponerse como mecanismo de testigo C1 — no es necesaria para adjudicar C1 en abstracto | `NOT_REQUIRED_FOR_C1` |
| Cobertura transversal | `NOT_REQUIRED_FOR_C1` (ver D3: ya resuelto como dos métricas separadas) | `NOT_REQUIRED_FOR_C1` — `S3_HONEST_COVERAGE` ya está medida y ya falló; no bloquea nada adicional | `NOT_REQUIRED_FOR_C1` |
| S¹/S² | `NOT_REQUIRED_FOR_C1` | `NOT_REQUIRED_FOR_C1` — fuera de alcance (`BLOCK-4`) | `NOT_REQUIRED_FOR_C1` |

**Posiciones:**

- **PI:** la pregunta C1 (comité 010) y la pregunta arquitectónica (comité 011) fueron
  intencionalmente secuenciadas por separado; mezclarlas de nuevo aquí reintroduciría exactamente
  la confusión que motivó blindar R4 a un solo archivo de salida.
- **Matemático/formalista:** C1 es una pregunta sobre completaciones de *cualquier* subposet
  observado; su cierre no depende de qué mecanismo concreto (parches, frentes, u otro) produzca ese
  subposet. Confirma `NOT_REQUIRED_FOR_C1` en la columna (i) para los cinco términos.
- **Físico:** de acuerdo, con una advertencia: si en el futuro se intenta certificar
  no-identificabilidad física usando un testigo construido a partir de un ensamblaje de parches
  concreto, entonces sí haría falta cerrar "compatibilidad causal" — pero eso es un testigo
  hipotético no construido hoy.
- **Ingeniería/reproducibilidad:** confirma que ningún código de parches/ensamblaje existe
  (`rg -il "parche"` solo devuelve prosa); no hay nada que evaluar ejecutablemente hoy.

**Objeción retenida (falsificador):** este resultado no debe leerse como que la arquitectura de
comité 011 queda descartada — solo que **no es un prerrequisito** de la pregunta C1 estrictamente
definida por comité 010. La arquitectura sigue bloqueada por sus propios cinco motivos
(`comite_decision_011.md` §8, BLOCK-1..5), independientemente de esta decisión.

---

### D5. Necesidad y target de Lean

```text
LEAN_REQUIRED = NO
LEAN_DEFERRAL_REASON =
  Las cláusulas (b) contenido exacto de 𝔄, (c) regla de referencia inducida no trivial, y (e)
  predicado de incompatibilidad permanecen UNRESOLVED tras esta sesión (ver D1-D2). Formalizar en
  Lean un teorema sobre 𝔄 antes de que estas tres cláusulas estén cerradas por escrito formalizaría
  un objetivo móvil — exactamente el riesgo de post-hoc tuning que comité 010 señaló para un
  hipotético "Alloy 003" ("a refinement that tightens admissibility after observing that Alloy 002
  witnesses are non-admissible is tuning the model class to fit the known result",
  comite_decision_010.md §5 falsifier, freeze violations punto 2). El mismo argumento aplica a Lean.
```

**Distinción de los seis objetos nombrados por el brief** (evaluados por separado, ninguno agrupado):

| Objeto | Cobertura Lean actual | Suficiente hoy? |
|:---|:---|:---|
| Resultado order-only abstracto | `formal/HorizonFormal/` cubre ideales, `ChainEnd`, covarianza bajo isomorfismos de orden (`dev/LEAN_HYPOTHESIS_AUDIT.md` §Current theorem inventory) | Sí, para lo que ya prueba (order-theoretic core); no cubre completaciones/embeddings |
| Resultado de coordenadas fijas | No existe ni se espera en Lean — es un objeto numérico/físico (generador, sprinkling), no una prueba formal | N/A — no es un objetivo Lean |
| Preservación de dimensión ≤ 2 | No hay teorema Lean; el chequeo actual es una búsqueda combinatoria en Python (`product_order_check_alloy002_witness.py`) | No formalizado; no bloquea D2 porque D2 ya se resolvió sin necesitar una prueba general |
| Compatibilidad física con 𝔄 | Imposible de formalizar mientras 𝔄 (b) no esté cerrada | No — es la razón principal del `LEAN_DEFERRAL_REASON` |
| Observable de maximalidad de un elemento | Existe cobertura tangencial en mathlib (`Order.Ideal`/`hasMaximum`, lemas citados en `dev/LEAN_HYPOTHESIS_AUDIT.md` filas 20-24) pero **no** para la maximalidad-bajo-completación que Alloy 002 encodifica (`isInterface`) | Parcial/tangencial; no cierra la pregunta C1 |
| Observable agregado usado por el `PASS` (prereg-002) | No es un objetivo Lean — es un estimador estadístico validado empíricamente por el protocolo de pre-registro sellado, no por prueba formal | N/A — categoría distinta (nivel 5 de la jerarquía §3) |

**Posiciones:**

- **PI:** ninguna formalización externa sustituye una prueba en este repositorio; se reconfirma que
  "Variant A"/"Bruno" (checkout `xinhjBrant/mathlib4`, commit `f008ff9931c6d541d0dc819eef11f93479f6cb96`)
  **no cuenta como Lean auditable de este proyecto** (R2, `BLOCKED_WRONG_REPOSITORY_CONTEXT`), y esta
  decisión no depende de esa prueba externa en ningún grado.
- **Matemático/formalista:** de acuerdo con el diferimiento; añade que el único teorema con target
  claro y alcanzable *ahora* sería sobre transporte de decisiones bajo *embeddings* (no solo
  isomorfismos) — pero ese target pertenece a "compatibilidad causal" (D4), no a C1 propiamente, y
  D4 ya determinó que ese término es `NOT_REQUIRED_FOR_C1`.
- **Físico:** sin objeción — ningún resultado físico depende de Lean en esta fase; el testigo actual
  es combinatorio (Alloy), no una prueba de teorema.
- **Ingeniería/reproducibilidad:** confirma que ningún archivo `.lean` fue tocado ni se propone
  tocar en esta sesión, cumpliendo la restricción del usuario.

**Confianza:** ALTA en el diferimiento (la razón — cláusulas abiertas que bloquean cualquier target
formal preciso — está directamente respaldada por D1/D2 de esta misma acta, no por evidencia externa).

---

## 5. Tratamiento de Alloy 002

```text
ALLOY_002_LOGICAL_WITNESS = PRESENT
ALLOY_002_PHYSICAL_WITNESS = NOT_ESTABLISHED
ALLOY_002_C1_WITNESS_STATUS = INVALID_UNDER_CONVEXITY_REQUIREMENT
```

Alloy 002 **sí** aporta evidencia de ambigüedad lógica: en un modelo acotado de 4 elementos, la
misma relación de orden observada (`{(E2,E3)}`) admite dos completaciones (A, B) que inducen
decisiones de interfaz incompatibles sobre `Element$3` (`alloy_verification_002...md` §4-5). Este
hecho combinatorio es real y queda registrado sin reinterpretar.

Bajo la interpretación de convexidad adoptada en D2 (`MANDATORY_FOR_C1`), **Completion B incumple
convexidad**: el elemento oculto `E0` satisface `E2 < E0 < E3`, quedando causalmente interpuesto
dentro del rango observado (`witness_note.md` §4, fila Completion B). Por tanto Alloy 002 **no
certifica no-identificabilidad** dentro de una clase que exija convexidad — el único par de
completaciones que produce decisiones distintas depende exactamente de la completación no
admisible.

Alloy 002 **tampoco demuestra identificabilidad física** — no prueba que *toda* completación
admisible produzca la misma decisión; solo muestra que la completación concreta que sí la cambiaba
(B) es la que falla la obligación física. Ausencia de un contraejemplo admisible no es prueba de
identificabilidad (regla de adjudicación, §"no conviertas ausencia de contraejemplo en prueba").

**Función actual de Alloy 002:** delimitar qué hipótesis físicas resultan decisivas. Muestra que,
de las obligaciones evaluadas en D1/D2, es la **convexidad** — no la dimensión ≤ 2 ni la validez
como orden parcial — la que hace el trabajo discriminante en este testigo. Esa es información útil
para diseñar cualquier testigo físico futuro (nivel 4 de la jerarquía §3): concentrar el esfuerzo en
la obligación de convexidad, no en repetir chequeos de dimensión que ya se sabe que no discriminan
aquí.

## 6. Tratamiento de boundary-bracket

```text
BOUNDARY_BRACKET_STATUS = FAILED_BASELINE_UNDER_PRECOMMITTED_DENSITY_COVERAGE_CRITERION
BOUNDARY_BRACKET_ALLOWED_USE = DIAGNOSTIC_COMPARATOR
```

Aprobado explícitamente por el comité (unanimidad de las cuatro posiciones registradas) como
`DIAGNOSTIC_COMPARATOR` únicamente. Quedan **prohibidas**, sin excepción:

- reclasificar el `FAIL` (`S3_HONEST_COVERAGE` 51%→48%→44%) como `PASS`;
- sustituir retroactivamente el criterio precomprometido (`hoja_de_ruta_24_jun_2026.md:64,80`);
- usar `boundary-bracket`/S3 como evidencia positiva de reconstrucción;
- usar cualquier mejora futura del localizador para borrar o reinterpretar este resultado histórico.

Esto es una decisión completamente separada de D1-D5: `boundary-bracket` es un objeto de nivel 5
(§3), no de niveles 1-4. Su estado no afecta ni es afectado por la clase 𝔄.

## 7. Síntesis

**Lo que se cerró hoy:** tres de las diez obligaciones candidatas de 𝔄 quedan `MANDATORY` (literal
preservation, causal partial order, convexidad — las tres únicas con evidencia ejecutable directa);
dos quedan `DEFERRED` explícitamente (compatibilidad Schwarzschild, manifoldlikeness) por falta de
predicado ejecutable, no por rechazo; una queda `OPTIONAL_DIAGNOSTIC` (procedencia por sprinkling);
la dimensión ≤ 2 queda acotada a una subclase nombrada (`𝔄_Schw`), evitando la generalización que el
brief prohibió explícitamente; el número de elementos ocultos queda `DEFERRED` por ausencia de
evidencia en cualquier dirección. Cobertura transversal queda escindida en dos nombres no
intercambiables. Los cinco términos de comité 011 quedan `NOT_REQUIRED_FOR_C1` para definir o evaluar
C1 en abstracto (aunque siguen siendo prerrequisitos de la pregunta arquitectónica separada, comité
013). Lean queda diferido con una razón concreta y verificable.

**Lo que sigue abierto (no se fuerza cierre):**

- Contenido exacto y cerrado de 𝔄 más allá de las tres obligaciones `MANDATORY` (cláusula (b) de R4
  sigue sin una redacción única y final).
- La regla de referencia inducida (c): el único candidato existente (`c1_selector.maximal_elements`,
  `R=Max(C)`) sigue siendo trivial (`NO_INTERFACE` universal); ninguna alternativa no trivial ha sido
  propuesta ni adjudicada.
- El predicado de incompatibilidad (e): ninguna fórmula ejecutable existe todavía.
- Si `𝔄_Schw` (D2) debe generalizarse alguna vez a completaciones no generadas por el generador
  sellado.
- Escalar el chequeo Alloy más allá de `exactly 4 Element` (mencionado pero explícitamente NO
  ejecutado en esta sesión por restricción del usuario).
- `GENUINE_TRANSVERSAL_COVERAGE` permanece sin ninguna definición — no se intentó definirla, solo se
  la nombró para prevenir su confusión con `S3_HONEST_COVERAGE`.

Ninguna de estas aperturas se cierra con `UNRESOLVED` genérico sin más: cada una tiene, arriba, la
obligación concreta pendiente que la resolvería (regla de adjudicación cumplida).

## 8. Próximo paso autorizado (reversible)

Redactar por escrito, en un nuevo documento dev (no en este archivo, no en R4), las tres cláusulas
que permanecen `UNRESOLVED`: (b) contenido cerrado de 𝔄 incorporando las tres obligaciones
`MANDATORY` ya fijadas por este comité; (c) una regla de referencia no trivial candidata; (e) un
predicado de incompatibilidad ejecutable candidato. Esto es puramente redacción — ninguna búsqueda de
testigos, ninguna ejecución, ningún modelo Alloy nuevo — hasta que un comité posterior revise ese
borrador. Solo entonces (comité 010 §9 step 4) se autorizaría un modelo Alloy 003, y solo si además
se opta por escalar el scope combinatorio más allá de 4 elementos.

## 9. User sign-off

_(dejado en blanco para el usuario — decisión, fecha, y cualquier nota que prevalezca)_

---

## Bloque normativo

```text
COMMITTEE_ID = 012

C1_CLASS_STATUS = PARTIALLY_DEFINED
C1_EVALUABILITY_STATUS = NOT_YET_EVALUABLE_FOR_PHYSICAL_WITNESSES
PHYSICAL_IDENTIFIABILITY_STATUS = OPEN

D1_ADMISSIBLE_CLASS_DECISION =
  literal_subposet_preservation: MANDATORY |
  causal_partial_order: MANDATORY |
  absence_of_inadmissible_hidden_elements_general_principle: MANDATORY (= convexity) |
  convexity: MANDATORY_FOR_C1 (see D2) |
  product_order_realizability: REQUIRED_ONLY_FOR_A_NAMED_SUBCLASS (see D2) |
  order_dimension_le_2: REQUIRED_ONLY_FOR_A_NAMED_SUBCLASS (see D2) |
  schwarzschild_region_compatibility: DEFERRED |
  manifoldlikeness: DEFERRED |
  sprinkling_provenance: OPTIONAL_DIAGNOSTIC |
  hidden_element_localisation_restriction: MANDATORY (= convexity) |
  hidden_element_count_restriction: DEFERRED

D2_CONVEXITY_DECISION = MANDATORY_FOR_C1
D2_ORDER_DIMENSION_DECISION = REQUIRED_ONLY_FOR_A_NAMED_SUBCLASS (named subclass: 𝔄_Schw)

D3_TRANSVERSAL_COVERAGE_DECISION =
  TWO_DISTINCT_METRICS: S3_HONEST_COVERAGE (= cov_honest, MEASURED, FAILED 51%->48%->44%)
  != GENUINE_TRANSVERSAL_COVERAGE (UNDEFINED, requires 2+1/3+1, out of scope)

D4_ARCHITECTURE_CLOSURE_DECISION =
  parches_locales: NOT_REQUIRED_FOR_C1 |
  ensamblaje: NOT_REQUIRED_FOR_C1 |
  compatibilidad_causal: NOT_REQUIRED_FOR_C1 |
  cobertura_transversal: NOT_REQUIRED_FOR_C1 (resolved as two distinct metrics, see D3) |
  S1_S2: NOT_REQUIRED_FOR_C1

D5_LEAN_DECISION = LEAN_REQUIRED = NO ; LEAN_DEFERRAL_REASON = clauses (b)/(c)/(e) of 𝔄 remain
  UNRESOLVED; formalising before closure would formalise a moving target (same post-hoc hazard
  flagged for a hypothetical Alloy 003, comite_decision_010.md §5)

ALLOY_002_LOGICAL_WITNESS = PRESENT
ALLOY_002_PHYSICAL_WITNESS = NOT_ESTABLISHED
ALLOY_002_C1_WITNESS_STATUS = INVALID_UNDER_CONVEXITY_REQUIREMENT

BOUNDARY_BRACKET_STATUS = FAILED_BASELINE_UNDER_PRECOMMITTED_DENSITY_COVERAGE_CRITERION
BOUNDARY_BRACKET_ALLOWED_USE = DIAGNOSTIC_COMPARATOR

NEXT_AUTHORIZED_ACTION =
  Draft (writing only, no execution) closed candidate text for 𝔄 clauses (b) full content, (c)
  a non-trivial induced reference rule, and (e) an executable incompatibility predicate, in a new
  dev document, incorporating the MANDATORY/DEFERRED/OPTIONAL_DIAGNOSTIC decisions fixed by D1-D2
  above. Committee review of that draft precedes any witness search.

NEXT_FORBIDDEN_ACTIONS =
  new Alloy 003 model before (b)/(c)/(e) are closed in writing |
  any witness search under an unclosed 𝔄 |
  reclassifying boundary-bracket FAIL as PASS |
  using dim_DM<=2 pass as evidence of physical admissibility |
  opening 2+1D or 3+1D scope |
  new Lean formalisation before 𝔄 is closed |
  citing "Variant A"/"Bruno" (f008ff9931c6d541d0dc819eef11f93479f6cb96, xinhjBrant/mathlib4) as
  evidence in this repository |
  equating S3_HONEST_COVERAGE with GENUINE_TRANSVERSAL_COVERAGE |
  commit or push of this document or any R1-R4 artefact without explicit PI authorisation

OVERALL_VERDICT = C1_DEFINITION_PARTIALLY_CLOSED
```
