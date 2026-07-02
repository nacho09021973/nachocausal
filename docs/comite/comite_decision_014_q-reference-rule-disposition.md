# Comité Decision 014 — disposición del candidato de referencia Q

> Convocado por instrucción explícita del usuario para adjudicar el futuro del candidato de
> referencia `Q` (orden conjugado + marcador `A`), autorizado solo para desarrollo conceptual por
> `docs/comite/comite_decision_013_c1-bce-review.md` (D2, `R2_AUTHORIZE_DEVELOPMENT`) y desarrollado
> por escrito en `dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md`. Sesión **exclusivamente deliberativa y
> documental**: no se ejecutó ninguna simulación, sprinkling, enumeración, búsqueda de
> contraejemplos, prueba Alloy, formalización Lean, análisis estadístico ni modificación de código.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`. El comité PROPONE; el usuario/PI AUTORIZA. Sin
> commit ni push. Único archivo escrito por esta sesión: este documento.
>
> **Disciplina terminológica (obligación explícita cumplida):** se preservan sin reinterpretar
> `BIPARTITION_STATUS = REFUTED_FOR_|A|>=2`, `TRIPARTITION_STATUS = PROVISIONAL`,
> `TWO_FACE_LEMMA_STATUS = OPEN`, `PROPOSED_Q_RULE_STATUS = BLOCKED`,
> `OVERALL_DEVELOPMENT_STATUS = Q_REQUIRES_FURTHER_DEFINITION`,
> `ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED`, `PHYSICAL_IDENTIFIABILITY_STATUS =
> NOT_ESTABLISHED`. La bipartición **no** se trata como laguna abierta: está refutada para
> `|A|≥2`. La tripartición **no** se trata como regla adoptada: sigue provisional. No se usa
> "Teorema de Bruno" ni el checkout externo "Variant A" (`xinhjBrant/mathlib4`,
> `f008ff9931c6d541d0dc819eef11f93479f6cb96`, `R2_STATUS = BLOCKED_WRONG_REPOSITORY_CONTEXT`) como
> evidencia local en ningún punto de este documento. La evidencia local continúa denominada
> `ALLOY_002_LOGICAL_WITNESS`, con `ALLOY_002_PHYSICAL_WITNESS = NOT_ESTABLISHED`.

## 1. Pregunta única

> ¿Existe una ruta suficientemente canónica, total, no circular y físicamente interpretable para
> convertir `Q` en la regla de referencia de C1, o debe rechazarse o restringirse su uso antes de
> seguir desarrollando BCE?

## 2. Estado de entrada (lectura, no ejecución)

**Fuentes leídas íntegramente esta sesión** (primarias, no reconstruidas desde informes de
terminal):

| Archivo | Rol en esta adjudicación |
|:---|:---|
| `dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md` | Objeto bajo revisión — Partes I-VIII + bloque normativo |
| `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §7 (7.1–7.6) | Fuente original de Proposition 7.3, `P_C=L_U∩L_V`, orden conjugado `Q`, lema de dos caras, tripartición, primalidad modular, `III_PENDING_TWO_FACE_LEMMA` |
| `dev/PR003_C1_BCE_CLOSED_CANDIDATE.md` | Candidato BCE completo — Parte I (notación), Parte II (cláusula b, `𝔄_C1(O)`), Parte III (cláusula c, candidatos 1-2), Parte IV (cláusula e), bloque normativo |
| `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` | Origen de las cinco cláusulas C1 (a-e), tabla de distinciones observacionales §2, `isInterface`/`Max(C)` (§7) |
| `docs/comite/comite_decision_012_c1-admissible-completion-class.md` | D1-D5 previos, jerarquía de niveles §3, `CONVEXITY_REQUIREMENT = MANDATORY_FOR_C1`, `ORDER_DIMENSION_LE_2_REQUIREMENT = REQUIRED_ONLY_FOR_A_NAMED_SUBCLASS` |
| `docs/comite/comite_decision_013_c1-bce-review.md` | D1 (G1/G3), D2 (`R2_AUTHORIZE_DEVELOPMENT`), D3 (pullback tipado por codominio), D4 (coherencia B/C/D/E), D5 (autorización posterior) |
| `docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md` | Mathematician brief (Prop 7.3 "asserted by generator audit, not measured", automorfismos, primalidad `[PLAUSIBLE, UNVERIFIED]`), falsifier ataque 2 sobre `R=Max(C)` |
| `formal/alloy/completion_nonidentifiability_interface_counterexample.als` | Definición literal de `isInterface[c,e]` (líneas 27-30) y del assert `SameObservationForcesSameInterfaceDecision` (líneas 54-58) — testigo local ALLOY_002 |
| `dev/alloy/product_order_check_alloy002_witness_note.md` | Chequeo de convexidad + `dim_DM≤2` ejecutado sobre el testigo; origen de `ALLOY_002_C1_WITNESS_STATUS = INVALID_UNDER_CONVEXITY_REQUIREMENT` y `PHYSICAL_LAYER_EMPTY_EVIDENCE` |
| `nachocausal/c1_selector.py` | `maximal_elements` (líneas 18-25), `down_closure` (líneas 28-37) — único candidato de pullback con precedente de código |
| `nachocausal/selection_guard.py` | Guard-v, `verify_selection_order_only` (líneas 52-84) |

**Verificación de ausencia de artefacto:** no se ejecutó ningún `rg` nuevo en esta sesión (sesión
puramente documental sobre archivos ya identificados); no se generó ningún archivo de evidencia; no
se tocó `thresholds.py`; no se modificó ningún selector, test, modelo Alloy ni archivo Lean.

**Tokens preservados sin cambios** (verificados por lectura directa de los archivos de origen
citados arriba, no por memoria):

```text
BIPARTITION_STATUS = REFUTED_FOR_|A|>=2
TRIPARTITION_STATUS = PROVISIONAL
TWO_FACE_LEMMA_STATUS = OPEN                          (token exacto: III_PENDING_TWO_FACE_LEMMA)
PROPOSED_Q_RULE_STATUS = BLOCKED
OVERALL_DEVELOPMENT_STATUS = Q_REQUIRES_FURTHER_DEFINITION
ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED
PHYSICAL_IDENTIFIABILITY_STATUS = NOT_ESTABLISHED

GROUNDEDNESS_DECISION (comité 013) = G1_ADOPTED_FOR_C1_G3_RESERVED_FOR_SCHW  (no reabierto)
CONVEXITY_REQUIREMENT (comité 012) = MANDATORY_FOR_C1                        (no reabierto)
ORDER_DIMENSION_LE_2_REQUIREMENT (comité 012) = REQUIRED_ONLY_FOR_A_NAMED_SUBCLASS (𝔄_Schw, no reabierto)
CLAUSE_C_STATUS (comité 013 D2) = AUTHORIZED_FOR_DEVELOPMENT                 (esta sesión reevalúa esto, ver D8)
ALLOY_002_LOGICAL_WITNESS = PRESENT
ALLOY_002_PHYSICAL_WITNESS = NOT_ESTABLISHED
ALLOY_002_C1_WITNESS_STATUS = INVALID_UNDER_CONVEXITY_REQUIREMENT
BOUNDARY_BRACKET_STATUS = FAILED_BASELINE_UNDER_PRECOMMITTED_DENSITY_COVERAGE_CRITERION
BOUNDARY_BRACKET_ALLOWED_USE = DIAGNOSTIC_COMPARATOR
```

Ninguno de estos valores se reescribe en este documento. Donde esta sesión toma una decisión nueva
(D5, D6), se aplica exclusivamente a `Q`, a un dominio restringido `𝔄_Q(O)`, o a `𝔄_Schw` — nunca a
la definición general de `𝔄_C1(O)`.

---

## D1 — Validez del fundamento de representación

### Auditoría

`P_C = L_U ∩ L_V` y `x <_Q y :⇔ U_x<U_y ∧ V_x>V_y` provienen de la **Proposición condicional 7.3**
(`dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §7.3, texto exacto): *"Supóngase que la
relación producida por `past_matrix_fast` coincide exactamente con la causalidad radial de la
métrica Schwarzschild en el parche ingoing-EF utilizado."* Bajo esa hipótesis, la reducción radial
admite coordenadas de Kruskal `(U,V)` regulares a través del horizonte, la causalidad es el orden
producto `x≺y ⇔ U_x<U_y ∧ V_x<V_y`, y por tanto `P_C=L_U∩L_V` y `dim_DM(C)≤2`.

**No es una medición.** El propio texto lo distingue de una medición de dimensión: *"NO hay que
'atacar la dimensión de BH' midiendo: es una propiedad del generador"* (§7.3). El respaldo es una
**auditoría de código**: `nachocausal/generator.py:88` (`past_matrix_fast`) implementa la relación
EF cerrada de He–Rideout, verificada bit a bit contra Minz (`isCausal_BH2D`) hasta `N=10017`,
`100.340.289` pares (`docs/reuse_check.md:27-33`, citado en la misma nota). El paso "parche EF =
restricción del producto Kruskal" queda marcado explícitamente `[UNVERIFIED]` contra cita primaria,
"pero es estándar" (§7.3, mismo párrafo).

El comité 010 (mathematician brief, `comite_decision_010.md:72`) describe la misma proposición como
*"asserted by generator audit, not measured — Prop 7.3"* — formulación independiente, mismo
contenido, que este comité confirma sin reabrir.

### Posiciones

```text
POSITION_PI =
  La distinción entre "auditado por código" y "medido/demostrado desde primeros principios" es
  exactamente la que hay que preservar. Prop 7.3 no es una conjetura sin respaldo — tiene un
  respaldo ejecutable fuerte (bit-a-bit hasta 10^8 pares) — pero tampoco es un teorema
  incondicional sobre la clase 𝔄_C1(O) general: es una propiedad esperada de la familia
  generadora concreta, condicional a una hipótesis física declarada.

POSITION_FORMAL =
  Dados los datos disponibles, la etiqueta correcta no es ESTABLISHED (eso exigiría una prueba
  matemática de que TODA completación físicamente admisible de 𝔄_C1(O) tiene dim_DM≤2, lo cual
  no existe — comité 012 D2 ya dejó `ORDER_DIMENSION_LE_2_REQUIREMENT =
  REQUIRED_ONLY_FOR_A_NAMED_SUBCLASS`, no una obligación general) ni UNVERIFIED puro (eso
  ignoraría la verificación bit-a-bit real). `CONDITIONALLY_ESTABLISHED` es la única etiqueta de
  las cuatro permitidas que no sobre-declara ni sub-declara.

POSITION_PHYSICS =
  La física detrás de Prop 7.3 (regularidad de Kruskal-Szekeres a través del horizonte) es
  estándar en relatividad general; el riesgo no está ahí, está en el paso de traducción
  generador→orden-producto, que es exactamente el punto marcado [UNVERIFIED]. No hay ninguna
  razón física para dudar de la proposición en el régimen 1+1D Schwarzschild-EF sellado; sí hay
  motivo para no extenderla sin más a cualquier completación combinatoria abstracta de 𝔄_C1(O)
  (p. ej. los testigos Alloy 002, que son extensiones combinatorias, no salidas del generador).

POSITION_ENGINEERING =
  Ningún código en `nachocausal/` calcula el realizador `(L_U,L_V)` ni el orden conjugado `Q`
  (confirmado por búsqueda ya registrada en `dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md` §0). La
  verificación bit-a-bit citada es sobre la relación causal misma (`past_matrix_fast` vs Minz),
  no sobre la existencia de un realizador de dimensión 2 — son dos verificaciones distintas que
  no deben confundirse.

OBJECTIONS (falsificador) =
  Aceptar `CONDITIONALLY_ESTABLISHED` para la existencia del realizador no debe leerse como
  "casi seguro en la práctica". El testigo Alloy 002 (Completion A y B) muestra que completaciones
  combinatorias fuera de la procedencia del generador sellado pueden satisfacer `dim_DM≤2`
  trivialmente (ambas lo satisfacen, comité 012 D2) sin ser Schwarzschild ni siquiera físicamente
  admisibles (Completion B falla convexidad). Que `dim_DM≤2` sea fácil de satisfacer
  combinatoriamente NO implica que la hipótesis física de Prop 7.3 sea igual de fácil de
  satisfacer — son dos afirmaciones de fuerza distinta que este documento no debe fusionar.

CONSOLIDATED_DECISION =
  Q_REPRESENTATION_FOUNDATION = CONDITIONALLY_ESTABLISHED, condicional a: (i) Prop 7.3 (generador
  = causalidad radial exacta, paso EF=restricción-Kruskal [UNVERIFIED] pero estándar); (ii)
  pertenencia de la completación concreta a la subclase con `dim_DM(C)≤2` (no toda 𝔄_C1(O), per
  comité 012 D2).

CONFIDENCE = ALTA
  en que ESTABLISHED sin condiciones sería sobre-declarar (comité 012 D2 ya lo impide
  explícitamente) y UNVERIFIED puro sería ignorar el respaldo bit-a-bit real; MEDIA en que la
  frontera exacta de la subclase donde la hipótesis es válida esté completamente delimitada (el
  paso EF=Kruskal sigue [UNVERIFIED] contra cita primaria).
```

### Unicidad e invariancia del realizador

La nota fuente (§7.2) es explícita: la unicidad de `Q` salvo reversión global **no** está
garantizada en general — vale solo si el grafo de incomparabilidad de `P_C` es **primo** en su
descomposición modular (Gallai 1967). Si existe un módulo `M` no trivial, sus elementos pueden
orientarse independientemente, produciendo **múltiples `Q` no relacionados por una única
reversión global**. La primalidad genérica bajo sprinkling Poisson continuo está marcada
`[PLAUSIBLE, UNVERIFIED]`, "no anclado a cita primaria en biblioteca" (§7.4.1, confirmado también
por el mathematician brief de comité 010, `comite_decision_010.md:80`).

Esto tiene una consecuencia directa que este comité registra explícitamente: **dos realizadores
distintos y admisibles de la misma completación pueden producir referencias `Q` distintas**
siempre que el grafo no sea primo. No es un caso hipotético sin mecanismo — es exactamente la
definición de "no primo" en teoría de descomposición modular. Por tanto:

```text
Q_REALIZER_UNIQUENESS_STATUS = UNVERIFIED
  (condicionada a una propiedad — primalidad modular genérica bajo Poisson — que la propia fuente
  marca [PLAUSIBLE, UNVERIFIED], no demostrada ni refutada)
Q_REALIZER_INVARIANCE_STATUS = NOT_ESTABLISHED_IN_GENERAL
  (invariancia bajo elección de realizador se sigue exactamente de la misma condición de
  primalidad que garantiza la unicidad — son la misma propiedad matemática vista desde dos
  ángulos, no dos preguntas independientes; en el caso no primo, realizadores distintos SÍ pueden
  producir Q distintas, por construcción de la teoría de grafos de comparabilidad citada)
```

**Decisión sobre el caso no invariante:** dado que la primalidad genérica no está demostrada, `Q`
debe tratarse hoy como **potencialmente multivaluada por elección de realizador**, no solo por
elección de marcador. Este comité no elige aquí "cuál realizador preferir" (no hay ningún criterio
propuesto en ningún documento para hacerlo de forma order-only) — en su lugar, D5 más abajo
convierte esta observación en una condición de dominio (`QG3`) que excluye completaciones donde la
elección de realizador importa, en vez de arbitrar entre realizadores.

### Dominio válido

```text
Q_VALID_DOMAIN =
  Subconjunto de 𝔄_C1(O) que satisface dim_DM(C)≤2 (condicional a Prop 7.3) — NO todo 𝔄_C1(O)
  (comité 012 D2 ya estableció que dim_DM≤2 es REQUIRED_ONLY_FOR_A_NAMED_SUBCLASS, no una
  obligación general). Este subconjunto es "aproximadamente" 𝔄_Schw pero NO idéntico a él:
  𝔄_Schw(O) está definida por PROCEDENCIA del generador sellado (comité 012, Parte II del
  candidato BCE), mientras que el dominio válido de Q está definido por una PROPIEDAD INTRÍNSECA
  (dim_DM≤2) evaluable en principio sobre cualquier completación combinatoria, generador o no.
  Una completación combinatoria abstracta (p. ej. un testigo Alloy) puede satisfacer dim_DM≤2 sin
  proceder del generador sellado (de hecho, Completion A Y B del testigo Alloy 002 ambas lo
  satisfacen, comité 012 D2) — de modo que Q_VALID_DOMAIN ⊉ 𝔄_Schw(O) ni ⊆ 𝔄_Schw(O) en general;
  se solapan sin coincidir. Esta distinción NO fue señalada explícitamente por ningún comité
  anterior en esta forma y se registra aquí como precisión nueva.
```

### Salida D1

```text
Q_REPRESENTATION_FOUNDATION = CONDITIONALLY_ESTABLISHED
PROPOSITION_7_3_STATUS = CONDITIONALLY_ESTABLISHED
  (auditoría de código bit-a-bit real; paso EF=restricción-Kruskal [UNVERIFIED] contra cita
  primaria, "estándar" según la fuente; no es una medición ni una prueba general sobre 𝔄_C1(O))
Q_REALIZER_EXISTENCE_STATUS = CONDITIONALLY_ESTABLISHED
  (existe al menos un realizador dado Prop 7.3 y dim_DM(C)≤2; no establecido para 𝔄_C1(O) general)
Q_REALIZER_UNIQUENESS_STATUS = UNVERIFIED
  (depende de primalidad modular genérica, [PLAUSIBLE, UNVERIFIED] en la fuente)
Q_REALIZER_INVARIANCE_STATUS = NOT_ESTABLISHED_IN_GENERAL
  (misma condición que la unicidad; realizadores distintos producen Q distintas exactamente
  cuando el grafo de incomparabilidad no es primo)
Q_VALID_DOMAIN = Subconjunto de 𝔄_C1(O) con dim_DM(C)≤2, condicional a Prop 7.3; distinto de
  𝔄_Schw(O) (procedencia) — se solapan sin coincidir (ver arriba)
```

---

## D2 — Caso `|A|=1`

### Auditoría

Preservado sin reabrir: la construcción **dado** un marcador `a` fijo es cerrada, exhaustiva y
canónica salvo el intercambio global `L_a↔R_a` (`dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md`
§7.4.1, "Resultado positivo 1"; formalizada en detalle en
`dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md` Parte II). Se separan explícitamente las cuatro
nociones que el brief exige no confundir:

| Noción | Estado |
|:---|:---|
| Unicidad del marcador **dentro de una definición ya dada** | `{L_a,R_a}` es exhaustivo y único salvo swap **dado `a` fijo** — establecido documentalmente (Parte II punto 4 del documento de desarrollo). |
| Existencia de un marcador canónico | No se ha establecido que exista, en general, un único `a` distinguido por el orden — de hecho A1/A2 fallan precisamente porque, en el caso genérico (`Aut(C)` trivial, descomposición modular prima), NINGÚN elemento se distingue de otro por esas vías. |
| Selección order-only del marcador | `BLOCKED` (ver D3) — ningún candidato de A1-A6 alcanza cierre. |
| Interpretación física del marcador | `PLAUSIBLE_NOT_ESTABLISHED` — evita la circularidad §7.5 con el estadístico de futuro del PASS (ventaja metodológica real, Parte II punto 6), pero no se ha establecido que `{L_a,R_a}` corresponda a la referencia de horizonte real; el propio documento fuente lo marca `PROVISIONAL`. |

### Posiciones

```text
POSITION_PI =
  El caso |A|=1 es el sub-resultado más sólido de todo el desarrollo de Q — merece preservarse
  con precisión, sin inflarlo. Pero sin una regla de selección, no puede usarse como regla de
  referencia autónoma: alguien (o algo) tiene que decir cuál es "a", y hoy eso solo puede venir de
  fuera del orden observable.

POSITION_FORMAL =
  Estrictamente, "definir una regla útil en una subclase restringida" (opción 1 del brief)
  requeriría poder caracterizar, order-only, la subclase de completaciones que POSEEN un marcador
  de un solo elemento "natural" Y seleccionarlo. Ninguna de las dos partes está resuelta: A4/A5
  (los candidatos más cercanos a una selección de un único elemento) no cierran (D3). Por tanto la
  opción 1 no está disponible hoy, no por defecto de la construcción de {L_a,R_a} sino por
  ausencia de selector.

POSITION_PHYSICS =
  Como ejemplo pedagógico o comparador, el caso |A|=1 es genuinamente útil: permite construir
  ejemplos de juguete, verificar invariancia bajo isomorfismo, y estudiar el comportamiento de la
  tripartición degenerada sin la complicación del "core" intermedio. Eso es exactamente el
  contenido de un uso diagnóstico, no de una referencia física operativa.

POSITION_ENGINEERING =
  No existe código para Q ni para {L_a,R_a} en `nachocausal/` (confirmado, `dev/PR003_Q_
  REFERENCE_RULE_DEVELOPMENT.md` §0). Cualquier "uso" del caso |A|=1 hoy sería puramente
  conceptual/manual, consistente con un rol diagnóstico, no con una regla desplegable.

OBJECTIONS (falsificador) =
  Etiquetar el caso |A|=1 como `REFERENCE_SUBCLASS` sin una regla de selección sería exactamente
  la trampa que el prompt original de esta sesión describe: "demostrar que existe algún marcador
  útil no basta." El caso |A|=1 demuestra que la construcción DADA una selección es sólida — no
  demuestra que la selección exista. Confundir ambas cosas sería sobre-declarar.

CONSOLIDATED_DECISION =
  UNIQUE_MARKER_ALLOWED_USE = DIAGNOSTIC_ONLY. El caso |A|=1 sirve hoy para: construir ejemplos
  pedagógicos, verificar invariancia bajo isomorfismo de la construcción condicionada, y servir de
  sub-candidato prioritario si algún día A5/A6 produjeran una regla de selección de un único
  elemento. No sirve hoy como REFERENCE_SUBCLASS (falta el selector) ni debe declararse REJECTED
  (nada en la construcción misma está refutado) ni UNRESOLVED (la construcción dada `a` SÍ está
  resuelta; lo no resuelto es la selección, ya registrado aparte).

CONFIDENCE = ALTA
  (la distinción entre "construcción cerrada dado un marcador" y "selección de marcador abierta"
  está documentada con precisión exacta en la fuente y no admite ambigüedad razonable).
```

### Salida D2

```text
UNIQUE_MARKER_CASE_DECISION = DIAGNOSTIC_EXAMPLE_NOT_YET_OPERATIONAL_REFERENCE
UNIQUE_MARKER_DOMAIN = Completaciones con dim_DM(C)≤2 (Q_VALID_DOMAIN, D1) Y con un marcador `a`
  YA FIJADO externamente — no existe hoy una regla que identifique tal `a` dentro de esa subclase
UNIQUE_MARKER_SELECTION_RULE = NONE_CLOSED (ver D3)
UNIQUE_MARKER_PHYSICAL_INTERPRETATION = PLAUSIBLE_NOT_ESTABLISHED
  (evita circularidad §7.5; PROVISIONAL según la fuente)
UNIQUE_MARKER_ALLOWED_USE = DIAGNOSTIC_ONLY
```

---

## D3 — Disposición de los candidatos para seleccionar A

### A1 — Órbitas de automorfismos

Preservado: `Aut(C)` es trivial casi seguramente para un sprinkling Poisson continuo genérico
(mathematician brief, `comite_decision_010.md:81`, citando "generic finite Poisson sprinklings are
asymmetric"); con `Aut(C)` trivial, toda órbita es un singleton y "elegir una órbita" no discrimina
nada — el problema de selección reaparece intacto.

```text
CANDIDATE = A1 — Órbita de Aut(C)
FORMAL_RULE = A := órbita de un elemento bajo Aut(C)
TOTALITY = FAILS_GENERICALLY (Aut(C) trivial c.s. bajo Poisson continuo)
ISOMORPHISM_INVARIANCE = SÍ (por construcción)
NONCIRCULARITY = SÍ
NONTRIVIALITY = NO_EVALUABLE (falla antes, por totalidad)
PHYSICAL_INTERPRETATION = NINGUNA
PULLBACK_COMPATIBILITY = N/A (no aplicable — la regla no está definida en el régimen genérico)
DISPOSITION = REJECT
```

### A2 — Módulos

Preservado: la existencia de una descomposición modular no selecciona un módulo distinguido; si el
grafo es primo casi seguramente bajo sprinkling continuo (la misma hipótesis de primalidad
[PLAUSIBLE, UNVERIFIED] de D1), no hay módulos no triviales que elegir precisamente en el caso
típico — mismo mecanismo de fallo que A1, estructuralmente paralelo.

```text
CANDIDATE = A2 — Módulo no trivial de la descomposición modular
FORMAL_RULE = A := un módulo M no trivial
TOTALITY = FAILS_GENERICALLY (simétrico a A1; primalidad genérica ⇒ sin módulos no triviales)
ISOMORPHISM_INVARIANCE = SÍ (la descomposición modular es canónica, teorema de Gallai)
NONCIRCULARITY = SÍ
NONTRIVIALITY = NO_EVALUABLE
PHYSICAL_INTERPRETATION = "degeneración geométrica no genérica" — no localización de membrana
PULLBACK_COMPATIBILITY = N/A
DISPOSITION = REJECT
```

### A3 — Primalidad modular

Preservado exactamente:

```text
MODULAR_PRIMALITY_STATUS = AVAILABLE_BUT_DOES_NOT_SELECT_A
```

La primalidad modular es una propiedad de **unicidad** de `Q` una vez que `A` ya está fijado y el
realizador ya está construido — no selecciona ningún marcador. Es la misma condición discutida en
D1 (`Q_REALIZER_UNIQUENESS_STATUS`), no una pregunta distinta.

```text
CANDIDATE = A3 — Selección vía primalidad modular
FORMAL_RULE = N/A — confusión de nivel; responde unicidad de Q dado A, no selección de A
TOTALITY = N/A
ISOMORPHISM_INVARIANCE = N/A
NONCIRCULARITY = SÍ (no usa nada prohibido, pero no aplica a esta pregunta)
NONTRIVIALITY = N/A
PHYSICAL_INTERPRETATION = N/A
PULLBACK_COMPATIBILITY = N/A
DISPOSITION = REJECT
  (no por estar equivocado, sino por no responder la pregunta planteada — ver D1 y D5/QG3 para su
  tratamiento correcto como condición de estabilidad de realizador, no de selección de marcador)
```

### A4 — Extremos order-only

Auditado sin reintroducir `Max(C)`. La categoría general (elementos extremales por algún criterio
order-only — mínimos, máximos relativos, irreducibles) no está refutada; su única instanciación
concreta evaluada, `Max(C)`, sí lo está, por razón física: `Max(C)` es la pared de muestreo, no una
localización a media altura (`dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §2, tabla
pared-vs-horizonte). Ninguna otra instanciación (mínimos irreducibles, perfiles de ideal-filtro) ha
sido propuesta con precisión suficiente para auditar totalidad, invariancia o interpretación física.

```text
CANDIDATE = A4 — Extremos order-only (categoría general, excluyendo Max(C))
FORMAL_RULE = A := elemento(s) extremales según un criterio order-only distinto de maximalidad
  global (p. ej. elementos join/meet-irreducibles, perfiles de ideal-filtro) — SIN instanciación
  concreta propuesta todavía
TOTALITY = NO_EVALUADO (depende de la instanciación, ninguna concreta existe)
ISOMORPHISM_INVARIANCE = PLAUSIBLE (para criterios bien definidos en general; no verificado para
  ninguna instanciación concreta porque no existe ninguna)
NONCIRCULARITY = SÍ EN PRINCIPIO
NONTRIVIALITY = NO_EVALUADO
PHYSICAL_INTERPRETATION = DEPENDE_DEL_EXTREMO — ninguno propuesto evita la confusión
  pared-de-muestreo/horizonte salvo por descarte explícito de Max(C)
PULLBACK_COMPATIBILITY = NO_EVALUABLE (sin instanciación)
DISPOSITION = UNRESOLVED
  (la categoría permanece abierta a especificación futura; no se autoriza más trabajo específico
  sobre ella en esta sesión porque A6 la domina en las auditorías de D3 — ver síntesis)
```

### A5 — Firma relacional

Auditado explícitamente contra el riesgo de circularidad. El volumen futuro `O(i)=|futuro(i)|` es
exactamente la cantidad que usa el estimador sellado del PASS (`prereg-002`); usarlo para
seleccionar `A` reintroduciría la circularidad que `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md`
§7.5 prohíbe explícitamente. Otros invariantes (`C_k` de Benincasa-Dowker, fracción de orden de
Myrheim-Meyer, perfil de incomparabilidad) no son la cantidad que mide el PASS, pero su ausencia de
circularidad no ha sido verificada formalmente para ninguno en concreto.

```text
CANDIDATE = A5 — Firma relacional invariante, excluyendo volumen futuro
FORMAL_RULE = A := elemento(s) que alcanzan un valor distinguido de un invariante order-only ya
  reconocido (C_k, ordering fraction, perfil de incomparabilidad) — EXCLUYENDO explícitamente O(i)
TOTALITY = PLAUSIBLE (invariantes definidos en todo poset finito; unicidad del extremo no
  garantizada, empates posibles)
ISOMORPHISM_INVARIANCE = SÍ (los invariantes citados son invariantes de isomorfismo por
  construcción — Benincasa-Dowker, Myrheim-Meyer, ambos CONFIRMED en el literature verdict de
  comité 010)
NONCIRCULARITY = CONDICIONAL — cierta si se excluye O(i); no verificada para ningún invariante
  concreto todavía propuesto como firma final
NONTRIVIALITY = NO_EVALUADO
PHYSICAL_INTERPRETATION = PLAUSIBLE (respaldo en literatura citada, Benincasa-Dowker 2010, Surya
  LRR 2019 §4)
PULLBACK_COMPATIBILITY = NO_EVALUADO (sin instanciación concreta cerrada)
DISPOSITION = AUTHORIZE_FOR_FURTHER_SPECIFICATION
  (como componente del criterio de admisibilidad de A6, no como candidato aislado — ver síntesis)
```

### A6 — Familia multivaluada o agregada

Candidato principal superviviente. Se distinguen las cuatro formas exigidas.

#### A6.1 — Familia sin agregación

```text
CANDIDATE = A6.1 — Familia sin agregación: R_Q(C) = {Q(C,A) : A∈𝔄(C)}
FORMAL_RULE = Devolver el conjunto completo de triparticiones inducidas por cada marcador
  admisible, sin colapsar
TOTALITY = UNRESOLVED (depende enteramente del criterio de admisibilidad de 𝔄(C), aún no escrito)
ISOMORPHISM_INVARIANCE = PLAUSIBLE (si 𝔄(C) es invariante, la familia se transporta correctamente
  bajo isomorfismo por ser una construcción simétrica)
NONCIRCULARITY = SÍ, si 𝔄(C) excluye O(i) (heredado de A5)
NONTRIVIALITY = MÁXIMA_POR_CONSTRUCCIÓN (no colapsa nada — pero esto es una ventaja aparente, no
  una prueba de utilidad: retiene TODO marcador admisible, incluidos los espurios, sin ningún
  filtro de consenso)
PHYSICAL_INTERPRETATION = NINGUNA PROPIA — es la materia prima para las formas 2-4, no un objeto
  interpretable por sí mismo como "la" referencia
PULLBACK_COMPATIBILITY = TIPO NUEVO NO CUBIERTO por comité 013 (familia de particiones, no una
  partición única) — extendería la familia tipada por codominio con un tercer tipo, no
  especificado en ningún documento
DISPOSITION = DIAGNOSTIC_ONLY
  (útil como objeto intermedio para medir sensibilidad al marcador y como base de construcción de
  A6.2-A6.4; no cerrable por sí misma como regla de referencia)
```

#### A6.2 — Unión

```text
CANDIDATE = A6.2 — Unión: R_Q^∪(C) = ⋃_{A∈𝔄(C)} Q(C,A)
FORMAL_RULE = Unión componente a componente de las clases L_A, core_A, R_A a través de todos los
  marcadores admisibles
TOTALITY = UNRESOLVED
ISOMORPHISM_INVARIANCE = PLAUSIBLE, heredada de A6.1 si 𝔄(C) es invariante
NONCIRCULARITY = CONDICIONAL, igual que A6.1
NONTRIVIALITY = RIESGO_ALTO_DE_TRIVIALIZACIÓN — un elemento puede pertenecer a L_A para un
  marcador y a R_A' para otro; la unión componente a componente NO preserva disjunción, así que
  L^∪ y R^∪ pueden solaparse o, en el límite, cubrir todo N(A) conjuntamente sin discriminar nada.
  Este documento no encontró en ningún archivo del repositorio una definición previa de esta
  forma — es evaluada aquí por primera vez.
PHYSICAL_INTERPRETATION = NO EVALUABLE (el objeto resultante ya no es una tripartición sino un
  recubrimiento; su interpretación física requeriría antes decidir qué representa un elemento que
  cae en ambos lados según distintos marcadores)
PULLBACK_COMPATIBILITY = NO EVALUABLE — el tipo de objeto (recubrimiento, no partición) no está
  cubierto por la familia tipada de comité 013 ni por ningún esquema existente
DISPOSITION = UNRESOLVED
  (problema de tipo, no solo de especificación: "unión de particiones" no preserva la estructura
  de partición sin una definición adicional que ningún documento ha propuesto; no se rechaza
  definitivamente porque una reformulación como recubrimiento podría, en principio, definirse,
  pero no está hecha)
```

#### A6.3 — Intersección

```text
CANDIDATE = A6.3 — Intersección: R_Q^∩(C) = ⋂_{A∈𝔄(C)} Q(C,A)
FORMAL_RULE = Intersección componente a componente: L^∩ = ⋂_A L_A, R^∩ = ⋂_A R_A (elementos que
  todos los marcadores admisibles clasifican del mismo lado)
TOTALITY = UNRESOLVED
ISOMORPHISM_INVARIANCE = PLAUSIBLE, heredada de A6.1
NONCIRCULARITY = CONDICIONAL, igual que A6.1
NONTRIVIALITY = RIESGO_ALTO_DE_COLAPSO — el propio contraejemplo de intercalado ya documentado
  (§7.4.1: un vecino x puede quedar Q-intercalado entre dos elementos de una anticadena de dos
  puntos) muestra que marcadores distintos pueden discrepar exactamente en los puntos más
  cercanos al "cuello" — que son precisamente los de mayor interés físico. Si |𝔄(C)| crece o es
  diverso, L^∩ y R^∩ pueden reducirse monótonamente hacia el conjunto vacío. Este es el mecanismo
  concreto detrás del criterio de abandono "agregación multivaluada que trivializa la referencia"
  (D7).
PHYSICAL_INTERPRETATION = SI SOBREVIVE NO VACÍA, sería la interpretación más conservadora posible
  ("solo lo que todo marcador admisible acuerda") — pero su no vacuidad no está establecida
PULLBACK_COMPATIBILITY = MISMO TIPO QUE UNA PARTICIÓN ORDINARIA (componente a componente, comité
  013 P5) — a diferencia de A6.2, la intersección SÍ preserva un tipo de objeto bien definido
  (aunque potencialmente vacío)
DISPOSITION = UNRESOLVED
  (bien tipado, a diferencia de A6.2, pero con riesgo de colapso documentado y no descartado;
  requiere un argumento de no-trivialidad antes de cualquier adopción)
```

#### A6.4 — Clases robustas

```text
CANDIDATE = A6.4 — Clases robustas: clasificar un elemento solo cuando TODAS las elecciones
  admisibles de A coinciden; abstenerse en caso contrario
FORMAL_RULE = Para x∈N(A) genérico bajo variación de A∈𝔄(C): asignar x a L si x∈L_A para todo
  A∈𝔄(C) con x spacelike a A; asignar x a R simétricamente; de otro modo, x → ABSTAIN
TOTALITY = TOTAL_CON_ABSTENCIÓN_EXPLÍCITA — a diferencia de A6.1-A6.3, esta forma está definida
  para todo x (la abstención es una salida válida, no un fallo), condicional solo a que 𝔄(C) esté
  definida
ISOMORPHISM_INVARIANCE = PLAUSIBLE, heredada de A6.1
NONCIRCULARITY = CONDICIONAL, igual que A6.1 (depende de excluir O(i) del criterio de
  admisibilidad de 𝔄(C))
NONTRIVIALITY = MISMO_RIESGO_ESTRUCTURAL_QUE_A6.3, pero con degradación graciosa: en vez de
  colapsar a un conjunto vacío sin explicación, la clase "no acordada" se declara ABSTAIN de forma
  explícita y auditable. Esto convierte el riesgo de colapso de A6.3 en una tasa de abstención
  medible, en vez de en un fallo silencioso.
PHYSICAL_INTERPRETATION = PLAUSIBLE — "la referencia lateral robusta frente a la elección de
  marcador, con abstención honesta donde no hay consenso" es una lectura física razonable y
  compatible con el principio de "regla de abstención legítima" que el propio proyecto ya usa en
  otros lugares (p. ej. la puerta τ(n) del estimador sellado, `docs/estimator_v2_freeze.md`)
PULLBACK_COMPATIBILITY = MISMO TIPO QUE UNA PARTICIÓN DE TRES CLASES (L, R, ABSTAIN) — compatible
  con la familia tipada de comité 013 extendida trivialmente a tres clases en vez de dos o tres
  (L_A/core_A/R_A ya es de tres clases; aquí serían L/R/ABSTAIN, mismo tipo estructural)
DISPOSITION = AUTHORIZE_FOR_FURTHER_SPECIFICATION
  (la dirección mejor respaldada de las cuatro: total con abstención honesta, tipo bien definido,
  degradación no catastrófica; pendiente de: (i) el criterio de admisibilidad de 𝔄(C) mismo — ver
  D4; (ii) una prueba o argumento de que la tasa de abstención no es 100% en el régimen genérico)
```

### Síntesis D3

```text
Ningún candidato recibe ADOPT_FOR_CLOSED_DEFINITION. A1, A2 y A3 quedan REJECT (A1/A2 por fallo de
totalidad genérica bajo el mismo mecanismo de degeneración de medida cero; A3 por responder una
pregunta distinta). A4 queda UNRESOLVED como categoría, sin instanciación viable propuesta. A5
queda AUTHORIZE_FOR_FURTHER_SPECIFICATION como componente de un criterio de admisibilidad, no como
candidato aislado. De las cuatro formas de A6: A6.1 (familia sin agregación) es DIAGNOSTIC_ONLY —
materia prima, no candidato cerrable; A6.2 (unión) es UNRESOLVED por un problema de TIPO no
resuelto en ningún documento (no preserva la estructura de partición); A6.3 (intersección) es
UNRESOLVED por riesgo de colapso documentado (el mismo mecanismo de intercalado que ya refutó la
bipartición exhaustiva); A6.4 (clases robustas con abstención) es AUTHORIZE_FOR_FURTHER_SPECIFICATION
— la única forma que es simultáneamente total, bien tipada, y con una vía de degradación honesta
en vez de catastrófica. Esta sesión identifica A6.4 como la dirección única a desarrollar, no como
familia abierta de posibilidades — cumpliendo la instrucción de "una única ruta concreta".
```

---

## D4 — Dominio restringido para Q

### Auditoría de las siete restricciones candidatas

| Restricción | Etiqueta | Justificación |
|:---|:---|:---|
| Completaciones con marcador único (`\|A\|=1` existente y accesible) | `INSUFFICIENT` | La existencia de un marcador no resuelve la selección (D2/D3); restringir el dominio a "tiene un marcador único" sin una regla que lo identifique no cierra nada por sí solo. |
| Completaciones con familia de marcadores `𝔄(C)` no vacía | `MATHEMATICALLY_NECESSARY` | Precondición literal para que A6.1-A6.4 estén definidas; necesaria pero no suficiente — una familia no vacía puede seguir colapsando (A6.3) o abstenerse siempre (A6.4). |
| Completaciones con realizador bidimensional único (grafo de incomparabilidad primo) | `MATHEMATICALLY_NECESSARY` | Es la condición exacta que D1 identificó para `Q_REALIZER_UNIQUENESS_STATUS`; sin ella, `Q` mismo (antes de llegar al marcador) ya es ambiguo. |
| Completaciones donde todos los realizadores generan la misma referencia | `MATHEMATICALLY_NECESSARY` | Formulación equivalente (más débil, más robusta) de la fila anterior — permite primalidad fallida siempre que el pullback observado coincida de todos modos. Es literalmente la condición `QG3` de D5, restated como restricción de dominio en vez de exclusión de completaciones individuales. No se cuenta como una obligación independiente — es la misma obligación en dos redacciones (siguiendo la disciplina de no-doble-conteo de comité 012 D1). |
| Completaciones primas | `MATHEMATICALLY_NECESSARY` | Idéntica a la fila de "realizador bidimensional único" — mismo objeto matemático (primalidad de la descomposición modular), dos redacciones. No se cuenta por separado. |
| Completaciones con orientación temporal y lateral fijada (romper el swap `Q↔Q⁻¹`) | `AD_HOC` | El swap `L↔R` está reconocido en la fuente como una libertad de orientación LEGÍTIMA, no como una falta de definición (`dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md` Parte II punto 4: "una libertad de orientación reconocida explícitamente por la fuente, no una falta de definición"). Fijarla externamente reintroduciría exactamente el tipo de elección libre que el criterio de canonicidad prohíbe — no hay ninguna regla order-only propuesta en ningún documento para romper este swap de forma no arbitraria. |
| Completaciones procedentes del generador sellado | `GENERATOR_SPECIFIC` | Es la definición misma de `𝔄_Schw(O)` (comité 012, Parte II del candidato BCE) — una restricción por procedencia, no por propiedad intrínseca. Legítima para acotar el trabajo empírico futuro, pero no es una caracterización intrínseca de `𝔄_Q(O)`. |

### Posiciones

```text
POSITION_PI =
  El núcleo mathematically-necessary (familia no vacía + primalidad/estabilidad de realizador) no
  es un rescate artificial: es forzado por la propia matemática de realizadores de dimensión 2, la
  misma que exige Prop 7.3 para que Q exista siquiera. Eso es un fundamento legítimo, distinto de
  "restringir hasta que funcione".

POSITION_FORMAL =
  Sin embargo, el componente que más importa para responder la pregunta física — el criterio de
  admisibilidad de cada marcador individual dentro de 𝔄(C) — sigue sin escribirse. Un dominio
  cuyo filtro más importante está vacío no puede evaluarse todavía como principiado o como
  rescate: es prematuro juzgarlo en cualquier dirección.

POSITION_PHYSICS =
  La fila "orientación temporal y lateral fijada" merece explicitarse como la salida INCORRECTA:
  cualquier intento de fijar el swap Q↔Q⁻¹ con una convención ad hoc sería introducir
  exactamente la "libertad externa" que la pregunta original de esta sesión prohíbe descartar.

POSITION_ENGINEERING =
  Ninguna de las condiciones MATHEMATICALLY_NECESSARY tiene hoy una implementación (ni
  cálculo de descomposición modular, ni chequeo de estabilidad de realizador existen en
  `nachocausal/`) — son necesarias en el sentido matemático, no en el sentido de "ya verificables
  hoy".

OBJECTIONS (falsificador) =
  Nombrar una "forma" de 𝔄_Q(O) sin poder escribir su condición más importante es indistinguible,
  desde fuera, de diseñar una restricción para salvar Q. La única defensa contra esa lectura es
  que las condiciones YA fijadas (primalidad, familia no vacía) están genuinamente motivadas por
  la matemática de la construcción, no por el deseo de que Q funcione — pero eso no cubre el
  criterio de admisibilidad de marcador, que sigue siendo la pieza que falta y que SÍ podría, si
  se escribe mal, convertirse en un rescate artificial.

CONSOLIDATED_DECISION =
  El núcleo necesario (dim_DM≤2 + familia de marcadores no vacía + primalidad o estabilidad de
  realizador) se adopta como FORMA del dominio, sin ser todavía una definición cerrada, porque su
  criterio más consecuente (admisibilidad de marcador individual dentro de 𝔄(C)) permanece sin
  escribir. NO se adopta ninguna condición de orientación fija (AD_HOC, rechazada explícitamente).

CONFIDENCE = MEDIA
  (el núcleo necesario está bien fundamentado; el veredicto global sobre si 𝔄_Q(O) es
  "físicamente defendible" no puede emitirse todavía porque depende de un componente no escrito).
```

### Salida D4

```text
Q_RESTRICTED_DOMAIN_DECISION = SHAPE_IDENTIFIED_CRITERIA_UNRESOLVED
Q_RESTRICTED_DOMAIN_DEFINITION =
  𝔄_Q(O) ⊆ 𝔄_C1(O) := { C : dim_DM(C)≤2 (Prop 7.3) ∧ 𝔄(C)≠∅ ∧ [descomposición modular prima del
  grafo de incomparabilidad de P_C, O el pullback de Q coincide para todo realizador admisible —
  QG3, ver D5] } — SIN incluir ninguna condición de orientación temporal/lateral fijada
  (explícitamente AD_HOC, rechazada). El criterio de admisibilidad para A∈𝔄(C) permanece sin
  especificar (mismo bloqueo que D3/A6).
Q_RESTRICTED_DOMAIN_PHYSICAL_STATUS = PARTIALLY_PRINCIPLED_PENDING_ADMISSIBILITY_CRITERION
  (el núcleo necesario NO es un rescate artificial — está forzado por la matemática de
  realizadores de dimensión 2; pero el dominio como conjunto completo no puede calificarse de
  "físicamente defendible" mientras el criterio de admisibilidad de marcador individual, su
  componente más consecuente, no exista por escrito)
Q_RESTRICTED_DOMAIN_RELATION_TO_A_C1 = SUBCONJUNTO_PROPIO_ESTRICTO
  (dim_DM≤2 y primalidad excluyen completaciones genéricas de 𝔄_C1(O) que no los satisfagan)
Q_RESTRICTED_DOMAIN_RELATION_TO_A_SCHW = SOLAPADO_NO_IDÉNTICO
  (𝔄_Schw se define por procedencia del generador, comité 012; 𝔄_Q(O) aquí se define por
  propiedades intrínsecas — dimensión, primalidad/estabilidad — evaluables sobre cualquier
  completación combinatoria, proceda o no del generador sellado; ninguna de las dos clases
  contiene a la otra en general)
```

---

## D5 — Groundedness específico para Q

No se reabre `GROUNDEDNESS_DECISION (comité 013) = G1_ADOPTED_FOR_C1_G3_RESERVED_FOR_SCHW`. Se
preserva íntegramente el hallazgo registrado en `dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md` Parte
VII punto 7 (texto exacto, no reinterpretado): *"G1 (comité 013) impide que un oculto TOTALMENTE
desconectado de O participe en pullbacks locales, pero Q depende del realizador GLOBAL (L_U,L_V)
de TODA la completación C, no solo de su relación con O. Un oculto que satisface G1 ... podría aun
así, a través de sus relaciones con OTROS elementos ocultos no directamente vinculados a O, alterar
la estructura de incomparabilidad global y por tanto Q ... un modo de perturbación que G1, tal como
está formulado, no cierra completamente."* Etiquetado en la fuente: `Q_COMPATIBLE_WITH_G1 =
PARTIALLY_SUFFICIENT`.

### Auditoría de QG1-QG5

```text
QG1 — Mantener G1, aceptar la sensibilidad global como legítima
  Objeción: aceptar esto sin más equivaldría a declarar el riesgo de identificabilidad ya
  documentado como irrelevante, sin argumento nuevo que lo respalde. No se adopta solo.
  DISPOSITION = REJECT_AS_SOLE_CONDITION

QG2 — Invariancia frente a extensiones irrelevantes
  Conceptualmente atractivo (si un oculto no cambia "nada relevante" del observado, no debería
  cambiar el pullback de Q) pero "estructura causal relevante" no está definida en ningún
  documento — no es formalizable hoy sin trabajo adicional sustancial.
  DISPOSITION = REGISTERED_ASPIRATIONAL_NOT_FORMALIZED

QG3 — Estabilidad de realizador
  Exige que, para toda completación con realizador no único (grafo no primo), el pullback
  PB_O(Q(C,A)) sea idéntico para TODOS los realizadores admisibles; si no lo es, la completación
  queda excluida de 𝔄_Q(O). Esta condición es formalizable en principio (aunque no implementada
  hoy) y ataca DIRECTAMENTE el mecanismo identificado en la Parte VII punto 7: un oculto conectado
  que altera la estructura global de incomparabilidad es, precisamente, un caso donde el
  realizador deja de ser estable frente a esa perturbación. QG3 no "resuelve" el mecanismo — lo
  convierte en una condición de EXCLUSIÓN de dominio verificable en principio, en vez de dejarlo
  como un riesgo sin control.
  DISPOSITION = ADOPT

QG4 — Groundedness futuro G3 aplicado a 𝔄_Schw
  Ortogonal al problema de Q: G3 (futuro + no-retorno) formaliza trampeo/atrapamiento, no
  sensibilidad del realizador global. Ya está reservada para 𝔄_Schw por comité 013 y no se
  reabre. No resuelve nada específico de Q.
  DISPOSITION = ORTHOGONAL_RESERVED_FOR_SCHW_UNCHANGED

QG5 — Localidad de referencia (rechazar reglas globales como Q sin mecanismo causal explícito)
  Es la posición más fuerte: descartar toda regla de tipo global sin más. Se registra como la
  posición de repliegue natural si QG3 resultara, en trabajo futuro, insuficiente o
  inoperacionalizable (p. ej. si se demuestra que la primalidad/estabilidad de realizador falla
  para casi toda completación de interés, no solo para un conjunto de medida cero) — pero no se
  adopta hoy, porque adoptarla equivaldría a un rechazo de Q sin la evidencia que D7 exige para
  ello.
  DISPOSITION = REGISTERED_FALLBACK_NOT_ADOPTED
```

### Salida D5

```text
Q_GROUNDEDNESS_DECISION = QG3_ADOPTED_AS_DOMAIN_EXCLUSION_SUPPLEMENT_TO_G1
Q_EXTENSION_STABILITY_REQUIREMENT = ASPIRATIONAL_NOT_FORMALIZED (QG2; registrado para desarrollo
  futuro, no exigido hoy — "estructura causal relevante" carece de definición)
Q_REALIZER_STABILITY_REQUIREMENT = ADOPTED (QG3) — formalización: para C con realizador no único,
  PB_O(Q(C,A)) debe coincidir para todo realizador admisible de C, o C queda excluida de 𝔄_Q(O)
Q_LOCALITY_REQUIREMENT = NOT_ADOPTED (QG5 registrada como posición de repliegue, no adoptada;
  ver D7 para el criterio que activaría su adopción)
Q_G1_COMPATIBILITY_STATUS = PARTIALLY_SUFFICIENT_SUPPLEMENTED_BY_QG3
  (el hallazgo de la fuente se preserva literalmente sin cambio; QG3 es un complemento nuevo de
  esta sesión, no una revisión de G1 ni de la decisión de comité 013)
```

---

## D6 — Pullback apropiado para referencias laterales

`dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md` Parte II punto 7 dejó explícitamente abierta esta
pregunta, sin resolverla: *"podría ser más fiel usar la intersección literal L_a∩O (P1≡P2) en vez
de down_closure(C,L_a)∩O (P3) para este candidato específico ... Ninguna decisión se toma aquí; se
deja para revisión de comité."* Esta sesión es esa revisión.

### Auditoría

```text
POSITION_PI =
  El pullback tipado de comité 013 (D3: down_closure para tipo subconjunto, componente a
  componente para tipo partición) fue motivado explícitamente por una lectura de "accesibilidad
  desde la referencia" — apta para candidatos como Max(C), donde el pullback debe capturar "lo
  que es alcanzable desde R". L_a y R_a no son accesibilidad: son incomparabilidad espacial. Usar
  down_closure ahí inyectaría, en el pullback, elementos que son causalmente inferiores a algún
  punto de L_a pero que NO son ellos mismos spacelike a `a` — corrompiendo el carácter lateral del
  objeto.

POSITION_FORMAL =
  L_a y R_a, tal como están definidos (`x∈spacelike(a) : x<_Q a` / `a<_Q x`), son conjuntos
  EXTENSIONALES completos sobre `spacelike(a)` — no son semillas que deban expandirse por
  clausura hacia abajo. down_closure(C,L_a) añadiría el pasado causal completo de cada elemento de
  L_a, que en general contiene elementos NO spacelike a `a` (de hecho, contiene elementos
  timelike-anteriores a elementos de L_a, que son un tipo de relación explícitamente excluido de
  la construcción de L_a/R_a por definición). La intersección literal L_a∩O preserva el tipo de
  objeto sin alterarlo.

POSITION_PHYSICS =
  Una interpretación física de L_a/R_a como "los dos lados espaciales" solo tiene sentido si el
  pullback preserva esa lateralidad. Aplicar down_closure convertiría silenciosamente una
  afirmación espacial en una afirmación causal — precisamente el tipo de conflación que §7.4.1 ya
  tuvo cuidado de evitar al construir Q en primer lugar (Q es ⟂ al futuro que mide el PASS,
  exactamente para evitar esa mezcla).

POSITION_ENGINEERING =
  `nachocausal/c1_selector.down_closure` (líneas 28-37) es la única implementación existente y
  fue diseñada para el candidato `R=Max(C)` (tipo subconjunto causal). No hay ningún precedente de
  código para P1 aplicado a un objeto lateral, pero P1 (intersección de conjuntos) es
  trivialmente más simple de implementar que P3 — no introduce riesgo de ingeniería adicional.

OBJECTIONS (falsificador) =
  Adoptar P1 para el tipo lateral no debe leerse como una crítica a la decisión de comité 013 para
  el tipo subconjunto causal (Max(C)): esa decisión sigue siendo correcta para ese tipo y no se
  reabre. El riesgo real es que un lector futuro generalice mal esta decisión y aplique
  intersección literal donde debería aplicarse down_closure, o viceversa — de ahí la necesidad de
  mantener la familia tipada POR TIPO DE OBJETO, no una regla universal.

CONSOLIDATED_DECISION =
  Se extiende la familia tipada por codominio de comité 013 con un TERCER tipo, "subconjunto de
  tipo lateral/espacial" (definido por incomparabilidad respecto a un marcador, no por
  accesibilidad causal), para el cual PB_O := intersección literal (P1). Los dos tipos ya fijados
  por comité 013 (subconjunto causal → down_closure/P3; partición → componente a componente/P5)
  permanecen sin cambio. Esto es una extensión de la familia, no una revisión.

CONFIDENCE = MEDIA
  (el argumento de fidelidad de tipo es sólido y se apoya en la propia definición de L_a/R_a; no
  hay, sin embargo, ninguna verificación ejecutable de esta decisión — es una adjudicación
  conceptual, consistente con el alcance puramente documental de esta sesión).
```

### Salida D6

```text
Q_PULLBACK_DECISION = P1_LITERAL_INTERSECTION_FOR_LATERAL_TYPE
Q_PULLBACK_FORMAL_DEFINITION =
  Familia tipada por codominio, extendida (comité 013 + esta sesión):
  - Subconjunto de tipo CAUSAL (p. ej. Max(C)): PB_O(R(C)) := down_closure(C,R(C))∩O   [sin cambio]
  - Partición/estructura (p. ej. tripartición completa {L_A,core_A,R_A} vista como objeto único):
    aplicación componente a componente de la regla base                                [sin cambio]
  - Subconjunto de tipo LATERAL/ESPACIAL (L_a, R_a, y sus formas agregadas A6.3/A6.4):
    PB_O(R(C)) := R(C)∩O                                                    [NUEVO, esta sesión]
Q_PULLBACK_TYPE = TYPED_FAMILY_EXTENDED_WITH_LATERAL_SUBSET_TYPE
Q_PULLBACK_PHYSICAL_INTERPRETATION =
  Preserva el carácter espacial/lateral de L_a y R_a sin inyectar estructura causal ajena a su
  definición; evita reinterpretar tácitamente una afirmación de incomparabilidad como una
  afirmación de accesibilidad.
Q_PULLBACK_INVARIANCE_STATUS = HEREDADA_POR_CONSTRUCCIÓN
  (la intersección de conjuntos con O es trivialmente relabel-invariante si R(C) lo es; no
  requiere una prueba nueva más allá de la que ya cubre a R(C) mismo)
Q_PULLBACK_NONTRIVIALITY_STATUS = UNRESOLVED
  (la elección de P1 sobre P3 no crea ni resuelve la no-trivialidad de R(C) mismo — depende
  íntegramente de D3/D4, sin cambio por esta decisión)
```

---

## D7 — Criterio de abandono de Q

### Auditoría de los ocho criterios candidatos

| Criterio | ¿Se cumple hoy? | Evidencia |
|:---|:---|:---|
| Imposibilidad de seleccionar `A` canónicamente | `NO_MET` | A1-A5 fallan individualmente, pero A6.4 permanece vivo, no refutado (D3). No hay una prueba de imposibilidad general. |
| Dependencia de un realizador no único | `PARTIALLY_MET_MITIGATED` | Riesgo real identificado (D1); QG3 (D5) ofrece una vía de control por exclusión de dominio, no una prueba de que el control sea suficiente en la práctica. |
| Ausencia de invariancia bajo isomorfismos | `NOT_MET` | La construcción, dado marcador y realizador fijos, SÍ es invariante (Parte II punto 5 del documento de desarrollo). |
| Ausencia de interpretación física | `PARTIALLY_MET` | La interpretación sigue siendo `PLAUSIBLE_NOT_ESTABLISHED`/`PROVISIONAL`, no una interpretación establecida — el criterio más cercano a cumplirse de los ocho, pero "aspiracional" no es lo mismo que "ausente": la anti-circularidad de §7.5 es, en sí, una motivación metodológica real. |
| Sensibilidad a elementos ocultos irrelevantes | `MET_AS_DOCUMENTED_RISK_MITIGATED_BY_QG3` | Es exactamente el hallazgo de la Parte VII punto 7; QG3 (D5) es la respuesta propuesta, no verificada como suficiente. |
| Agregación multivaluada que trivializa la referencia | `MET_FOR_A6.2/A6.3, NOT_MET_FOR_A6.4` | A6.3 tiene riesgo de colapso documentado (mecanismo de intercalado); A6.4, por diseño, degrada a abstención en vez de a un conjunto vacío — no es el mismo modo de fallo. |
| Pullback lateral sin definición físicamente defendible | `RESOLVED_THIS_SESSION` | D6 adjudica esta pregunta con una decisión razonada (P1 para tipo lateral). |
| Circularidad con el observable del PASS | `NOT_MET_ACTIVELY_MANAGED` | Evitada por diseño (§7.5) y por la exclusión explícita de `O(i)` en A5/A6. |

### Salida D7

```text
Q_ABANDONMENT_CRITERIA =
  (1) imposibilidad demostrada de seleccionar A canónicamente para el régimen genérico
      (no solo para A1-A5, sino para A6 en cualquiera de sus formas);
  (2) demostración de que QG3 (estabilidad de realizador) excluye casi toda completación de
      interés, no solo un conjunto de medida cero (es decir, que la inestabilidad de realizador
      es GENÉRICA, no excepcional);
  (3) demostración de que ningún criterio de admisibilidad para 𝔄(C), al excluir O(i), puede
      evitar algún OTRO mecanismo de circularidad todavía no identificado;
  (4) demostración de que A6.4 (clases robustas) se abstiene en la práctica totalidad de los
      casos bajo sprinkling Poisson continuo genérico (abstención ≈100%, vaciando su utilidad).

Q_CURRENTLY_MEETS_ABANDONMENT_CRITERIA = NO
  (ninguno de los cuatro criterios anteriores está demostrado hoy; dos de los ocho factores
  auditados en la tabla — sensibilidad a ocultos y dependencia de realizador no único — son
  riesgos reales y documentados, no imposibilidades probadas, y ambos cuentan ya con una vía de
  mitigación propuesta en esta misma sesión, D5)

Q_CONTINUATION_JUSTIFICATION =
  No es "Q es el único candidato disponible" (razón explícitamente prohibida por el brief de
  convocatoria). Es que esta sesión logró una NARROWING concreta y verificable: de seis familias
  de selección (A1-A6) a una sola forma superviviente (A6.4, clases robustas con abstención); de
  un groundedness parcialmente suficiente sin respuesta a una condición adicional formalizable
  (QG3); y de una pregunta de pullback lateral abierta a una decisión razonada (D6, P1). Esa
  narrowing concreta —no la mera ausencia de alternativas— es lo que justifica una ronda más de
  trabajo acotado, con los cuatro criterios de abandono de arriba como disparadores explícitos y
  pre-comprometidos para la PRÓXIMA revisión, no como una promesa indefinida.
```

---

## D8 — Decisión de disposición

### Recuento de bloqueos semánticos abiertos tras D1-D7

1. Criterio de admisibilidad order-only para `A∈𝔄(C)` (D3/D4) — sin escribir.
2. Verificación o argumento de primalidad/estabilidad de realizador en el régimen genérico (D1/D5) — sin resolver.
3. Prueba de no-trivialidad de A6.4 (tasa de abstención no degenerada) (D3/D7) — sin evaluar.
4. Interpretación física operacional del marcador más allá de la anti-circularidad (D2) — aspiracional.

Son **cuatro** bloqueos semánticos distintos, no acotados a una única tarea cerrable. Por
instrucción explícita del brief de convocatoria, esto excluye `Q_FURTHER_SPECIFICATION_AUTHORIZED`.

### Posiciones

```text
POSITION_PI =
  Con cuatro bloqueos abiertos y ningún criterio de abandono cumplido, la única disposición
  honesta es DIAGNOSTIC_ONLY: Q sigue siendo la mejor herramienta disponible para comparar
  completaciones, construir contraejemplos y medir sensibilidad al marcador — pero no puede
  ocupar el papel de referencia física de C1 hoy, ni siquiera en una subclase ya delimitada.

POSITION_FORMAL =
  REJECTED_AS_REFERENCE sería sobre-declarar en la dirección opuesta: ninguno de los cuatro
  criterios de abandono (D7) está demostrado. Rechazar Q ahora cerraría una vía que todavía no ha
  fallado, solo que no ha terminado de especificarse.

POSITION_PHYSICS =
  RESTRICTED_SUBCLASS_CANDIDATE requeriría poder escribir la subclase con precisión suficiente
  para que un lector externo pudiera verificar pertenencia — hoy no se puede, porque el criterio
  de admisibilidad de marcador (bloqueo 1) es exactamente lo que definiría esa subclase.

POSITION_ENGINEERING =
  Ningún código existe para ninguna de las formas de Q; no hay una implementación que reclasificar
  ni proteger. La decisión es puramente sobre el estado documental.

CONSOLIDATED_DECISION = Q_DIAGNOSTIC_CANDIDATE_ONLY

CONFIDENCE = ALTA
  (la cuenta de cuatro bloqueos abiertos es verificable directamente en D1-D7 de este mismo
  documento; la instrucción de no elegir FURTHER_SPECIFICATION_AUTHORIZED con múltiples bloqueos
  es explícita en el brief de convocatoria).
```

### Salida D8

```text
Q_DISPOSITION = Q_DIAGNOSTIC_CANDIDATE_ONLY
```

---

## D9 — Próxima acción autorizada

Dado `Q_DISPOSITION = Q_DIAGNOSTIC_CANDIDATE_ONLY` con cuatro bloqueos identificados (D8), y dado
que `Q_CURRENTLY_MEETS_ABANDONMENT_CRITERIA = NO` (D7), la acción coherente es autorizar **una única
tarea de especificación acotada**, dirigida al bloqueo de mayor apalancamiento (el criterio de
admisibilidad de `𝔄(C)` que subyace a A6.4), sin reabrir el resto del desarrollo ni tratar `Q` como
si ya fuera la regla operativa.

```text
NEXT_AUTHORIZED_ACTION = Q_A6_AGGREGATION_SPECIFICATION_ONLY
  Alcance exacto: redacción, solo escritura, sin código/Alloy/Lean/ejecución, de: (i) un criterio
  de admisibilidad order-only para A∈𝔄(C) basado en A5 (firma relacional) excluyendo
  explícitamente el volumen futuro O(i); (ii) la formalización completa de A6.4 (clases robustas
  con abstención) como la única forma de agregación autorizada para desarrollo — A6.1/A6.2/A6.3
  quedan disponibles solo como objetos auxiliares de comparación, no como candidatos de cierre;
  (iii) verificación conceptual (por escrito) de si QG3 (D5) es formalizable como predicado
  ejecutable en principio, sin implementarlo.

NEXT_FORBIDDEN_ACTIONS =
  Alloy 003 en cualquier modalidad |
  Lean como sustituto de cualquier definición física ausente |
  cualquier simulación, sprinkling, enumeración o búsqueda de contraejemplos |
  cualquier análisis estadístico |
  implementar código para Q, la tripartición, A6.4, o cualquier pullback lateral |
  integrar Q con el observable agregado del PASS sin un lema explícito nuevo que lo justifique |
  búsqueda física bajo 𝔄_Schw mientras carezca de caracterización intrínseca cerrada |
  reclasificar boundary-bracket FAIL como PASS |
  reclasificar o reejecutar Alloy 002 |
  tratar Q_DIAGNOSTIC_CANDIDATE_ONLY como si autorizara su uso como referencia física en cualquier
  documento futuro |
  citar "Variant A"/"Bruno" (checkout xinhjBrant/mathlib4,
  f008ff9931c6d541d0dc819eef11f93479f6cb96) como evidencia en este repositorio |
  introducir nombres estándar no registrados en ningún artefacto committeado |
  commit o push de este documento o de cualquier artefacto derivado sin autorización explícita
  del PI

ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED
LEAN_AUTHORIZATION_STATUS = NOT_AUTHORIZED
PHYSICAL_SEARCH_AUTHORIZATION_STATUS = NOT_AUTHORIZED
```

---

## Tratamiento obligatorio de Alloy 002 (histórico, no reanalizado ni reejecutado)

```text
ALLOY_002_LOGICAL_WITNESS = PRESENT
ALLOY_002_PHYSICAL_WITNESS = NOT_ESTABLISHED
ALLOY_002_C1_WITNESS_STATUS = INVALID_UNDER_CONVEXITY_REQUIREMENT
```

Ninguna decisión de esta sesión (D1-D9) reclasifica el testigo Alloy 002. Verificado por lectura
directa de `formal/alloy/completion_nonidentifiability_interface_counterexample.als` (líneas 27-30,
54-58) y `dev/alloy/product_order_check_alloy002_witness_note.md` (§4-5): Completion A satisface
`𝔄_C1(O)` (convexa); Completion B queda excluida por convexidad, no por ninguna de las condiciones
nuevas de esta sesión (QG3, D6). No se ejecutó Alloy en ningún momento de esta sesión.

## Tratamiento obligatorio de boundary-bracket (sin cambios)

```text
BOUNDARY_BRACKET_STATUS = FAILED_BASELINE_UNDER_PRECOMMITTED_DENSITY_COVERAGE_CRITERION
BOUNDARY_BRACKET_ALLOWED_USE = DIAGNOSTIC_COMPARATOR
```

Objeto de nivel 5 (comité 012 §3), ortogonal a todas las decisiones de esta sesión sobre `Q`. No se
usa como evidencia positiva de reconstrucción ni de identificabilidad en ningún punto de este
documento.

---

## Síntesis

Esta sesión no cierra `Q` y no lo rechaza. Avanza en tres direcciones concretas y verificables:
**(D1)** distingue con precisión la existencia condicional del realizador de su unicidad e
invariancia — mostrando que la ambigüedad de `Q` tiene DOS fuentes independientes, no solo la
selección del marcador: la elección del marcador (ya conocida) y la elección del realizador (nueva
en esta forma explícita). **(D5)** convierte el hallazgo de "G1 parcialmente suficiente" en una
condición operacionalizable (`QG3`, estabilidad de realizador) en vez de dejarlo como un riesgo sin
respuesta. **(D6)** adjudica la pregunta de pullback lateral que comité 013 dejó abierta, mediante
un argumento de fidelidad de tipo, extendiendo —no revisando— la familia tipada por codominio.

Al mismo tiempo, la auditoría de D3 reduce el espacio de candidatos de seis familias a una única
forma superviviente (`A6.4`, clases robustas con abstención honesta), descartando explícitamente
`A6.2` (unión) por un problema de tipo no resuelto y marcando `A6.3` (intersección) con un riesgo de
colapso documentado por el mismo mecanismo que ya refutó la bipartición exhaustiva. Esa narrowing es
real, pero dos de los cuatro bloqueos que quedan (el criterio de admisibilidad de marcador, y la
prueba de que `A6.4` no se abstiene siempre) son precisamente los que determinan si `Q` llegará
alguna vez a ser una referencia física o quedará permanentemente como diagnóstico. Esta sesión no
fuerza esa respuesta: la reserva para el resultado de la única tarea autorizada en D9, con los
cuatro criterios de abandono de D7 ya pre-comprometidos como disparadores de una eventual
`Q_REJECTED_AS_REFERENCE` si esa tarea fracasa, en vez de permitir que `Q` se mantenga
indefinidamente por defecto.

## User sign-off

_(dejado en blanco para el usuario — decisión, fecha, y cualquier nota que prevalezca)_

---

## Bloque normativo

```text
COMMITTEE_ID = 014

INPUT_DEVELOPMENT_DOCUMENT = dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md
INPUT_DEVELOPMENT_STATUS = OVERALL_DEVELOPMENT_STATUS = Q_REQUIRES_FURTHER_DEFINITION (preservado)

Q_REPRESENTATION_FOUNDATION = CONDITIONALLY_ESTABLISHED
PROPOSITION_7_3_STATUS = CONDITIONALLY_ESTABLISHED
Q_REALIZER_EXISTENCE_STATUS = CONDITIONALLY_ESTABLISHED
Q_REALIZER_UNIQUENESS_STATUS = UNVERIFIED
Q_REALIZER_INVARIANCE_STATUS = NOT_ESTABLISHED_IN_GENERAL
Q_VALID_DOMAIN = Subconjunto de 𝔄_C1(O) con dim_DM(C)≤2 (Prop 7.3); solapado, no idéntico, a 𝔄_Schw(O)

UNIQUE_MARKER_CASE_DECISION = DIAGNOSTIC_EXAMPLE_NOT_YET_OPERATIONAL_REFERENCE
UNIQUE_MARKER_ALLOWED_USE = DIAGNOSTIC_ONLY

MARKER_SELECTION_DECISION = NO_CANDIDATE_CLOSED
MARKER_SELECTION_RULE = NONE — dirección única autorizada para desarrollo futuro: A6.4 (clases
  robustas con abstención), con criterio de admisibilidad basado en A5 excluyendo O(i)
MARKER_SELECTION_TOTALITY_STATUS = FAILS_GENERICALLY_FOR_A1_A2 (mismo mecanismo de degeneración de
  medida cero); UNRESOLVED_PENDING_ADMISSIBILITY_CRITERION para A6.4 (total con abstención dado el
  criterio, pero el criterio mismo no está escrito)
MARKER_SELECTION_INVARIANCE_STATUS = PLAUSIBLE_FOR_A6.4 (heredada de invariancia de 𝔄(C), si el
  criterio de admisibilidad es él mismo invariante — no verificado porque el criterio no existe)

MODULAR_PRIMALITY_STATUS = AVAILABLE_BUT_DOES_NOT_SELECT_A

Q_RESTRICTED_DOMAIN_DECISION = SHAPE_IDENTIFIED_CRITERIA_UNRESOLVED
Q_RESTRICTED_DOMAIN_DEFINITION = 𝔄_Q(O) ⊆ 𝔄_C1(O) := dim_DM(C)≤2 ∧ 𝔄(C)≠∅ ∧ estabilidad de
  realizador (QG3) — criterio de admisibilidad de marcador individual SIN ESPECIFICAR
Q_RESTRICTED_DOMAIN_PHYSICAL_STATUS = PARTIALLY_PRINCIPLED_PENDING_ADMISSIBILITY_CRITERION

Q_GROUNDEDNESS_DECISION = QG3_ADOPTED_AS_DOMAIN_EXCLUSION_SUPPLEMENT_TO_G1
Q_EXTENSION_STABILITY_REQUIREMENT = ASPIRATIONAL_NOT_FORMALIZED
Q_REALIZER_STABILITY_REQUIREMENT = ADOPTED
Q_LOCALITY_REQUIREMENT = NOT_ADOPTED

Q_PULLBACK_DECISION = P1_LITERAL_INTERSECTION_FOR_LATERAL_TYPE
Q_PULLBACK_FORMAL_DEFINITION = Familia tipada por codominio de comité 013, extendida con un tercer
  tipo (subconjunto lateral/espacial): PB_O(R(C)) := R(C)∩O para L_a/R_a y sus formas agregadas;
  sin cambio para los tipos subconjunto-causal (down_closure) y partición (componente a componente)
Q_PULLBACK_PHYSICAL_INTERPRETATION = Preserva el carácter espacial de L_a/R_a sin inyectar
  estructura causal ajena a su definición

Q_ABANDONMENT_CRITERIA = (1) imposibilidad demostrada de seleccionar A en el régimen genérico para
  cualquier forma de A6; (2) inestabilidad de realizador genérica, no excepcional; (3) circularidad
  residual no eliminable en ningún criterio de admisibilidad; (4) tasa de abstención de A6.4 ≈100%
  en el régimen genérico
Q_CURRENTLY_MEETS_ABANDONMENT_CRITERIA = NO

Q_DISPOSITION = Q_DIAGNOSTIC_CANDIDATE_ONLY

ALLOY_002_LOGICAL_WITNESS = PRESENT
ALLOY_002_PHYSICAL_WITNESS = NOT_ESTABLISHED
ALLOY_002_C1_WITNESS_STATUS = INVALID_UNDER_CONVEXITY_REQUIREMENT

BOUNDARY_BRACKET_STATUS = FAILED_BASELINE_UNDER_PRECOMMITTED_DENSITY_COVERAGE_CRITERION
BOUNDARY_BRACKET_ALLOWED_USE = DIAGNOSTIC_COMPARATOR

ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED
LEAN_AUTHORIZATION_STATUS = NOT_AUTHORIZED
PHYSICAL_SEARCH_AUTHORIZATION_STATUS = NOT_AUTHORIZED

NEXT_AUTHORIZED_ACTION = Q_A6_AGGREGATION_SPECIFICATION_ONLY — especificación escrita únicamente de
  (i) un criterio de admisibilidad order-only para 𝔄(C) basado en A5 excluyendo O(i); (ii) la
  formalización completa de A6.4 como única forma de agregación autorizada; (iii) evaluación
  conceptual de la formalizabilidad de QG3
NEXT_FORBIDDEN_ACTIONS = Alloy 003 | Lean como sustituto de definición física ausente |
  simulaciones/sprinklings/enumeraciones/búsquedas de contraejemplos | análisis estadístico |
  implementación de código para Q/A6.4/pullback lateral | integración con el observable del PASS
  sin lema explícito | búsqueda física bajo 𝔄_Schw sin caracterización intrínseca | reclasificar
  boundary-bracket FAIL como PASS | reclasificar o reejecutar Alloy 002 | tratar
  Q_DIAGNOSTIC_CANDIDATE_ONLY como autorización de uso como referencia física | citar "Variant
  A"/"Bruno" como evidencia | commit o push sin autorización explícita del PI

OVERALL_VERDICT = Q_REFERENCE_PATH_REMAINS_BLOCKED
```
