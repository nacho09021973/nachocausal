# Comité Decision 013 — revisión del candidato BCE (groundedness / R(C) / pullback)

> Convocado por instrucción explícita del usuario sobre `dev/PR003_C1_BCE_CLOSED_CANDIDATE.md`.
> Sesión **exclusivamente deliberativa y documental**: no se ejecutó ninguna simulación,
> sprinkling, búsqueda de contraejemplos, prueba Alloy, formalización Lean, análisis estadístico ni
> modificación de código. Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`,
> `NO_THRESHOLD_LOOSENING`, `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`. El comité PROPONE; el
> usuario/PI AUTORIZA. Sin commit ni push.
>
> **Disciplina terminológica:** se usa exclusivamente terminología ya registrada en el repositorio.
> No se introduce `ORDER_ONLY_MAXIMALITY_FLIP_CANDIDATE` como nombre estándar (no existe en ningún
> artefacto committeado). El testigo local se nombra siempre `ALLOY_002_LOGICAL_WITNESS`; el
> checkout externo "Variant A"/"Bruno" permanece `BLOCKED_WRONG_REPOSITORY_CONTEXT` y no se cita
> como evidencia en ningún punto de este documento.

## 1. Pregunta única

> ¿Puede cerrarse de forma no circular, no trivial y físicamente interpretable el candidato BCE
> mediante una decisión sobre groundedness, la regla de referencia `R(C)` y el pullback, o debe
> permanecer bloqueado hasta obtener nuevas definiciones físicas?

## 2. Estado de entrada (lectura, no ejecución)

| Archivo | Rol |
|:---|:---|
| `dev/PR003_C1_BCE_CLOSED_CANDIDATE.md` | Candidato bajo revisión — Partes I-VI + bloque normativo |
| `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` (R4) | Origen de las cinco cláusulas, obligaciones físicas |
| `dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md` (R3) | Estado de `boundary-bracket`/S3 (sin cambios) |
| `docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md` | Definiciones originales de los cinco términos; falsifier attack 2 sobre `R=Max(C)` |
| `docs/comite/comite_decision_011_patch-ensemble-architecture.md` | Cinco términos arquitectónicos (fuera de alcance de esta sesión) |
| `docs/comite/comite_decision_012_c1-admissible-completion-class.md` | D1-D5 previos; `OVERALL_VERDICT = C1_DEFINITION_PARTIALLY_CLOSED` |
| `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §7.4-7.6 | Construcción explícita de `Q`, refutación de la bipartición exhaustiva para `|A|≥2`, resultado positivo de tripartición canónica y de bipartición limpia para `|A|=1`, token `III_PENDING_TWO_FACE_LEMMA` — **leído esta sesión para verificar si el candidato Q puede adoptarse (R1) o solo autorizarse para desarrollo (R2)** |
| `nachocausal/c1_selector.py`, `nachocausal/selection_guard.py` | Precedente de código para `down_closure` y Guard-v |
| `dev/alloy/product_order_check_alloy002_witness_note.md`, `docs/alloy/alloy_verification_002...md` | Traza histórica del testigo Alloy 002 (no reanalizada, solo consultada) |

**Verificación de ausencia de artefacto:** `rg -rl "FutureAdmissible"` sobre todo el repositorio no
produjo ningún resultado. **No existe ningún objeto llamado `FutureAdmissible` en este proyecto.**
Este documento no relaciona groundedness con dicho nombre porque no hay nada con qué relacionarlo —
se registra la ausencia explícitamente en vez de fabricar una conexión.

**Estado literal en disco de las cláusulas del candidato BCE** (verificado por lectura directa,
`dev/PR003_C1_BCE_CLOSED_CANDIDATE.md:173,265,355,483,494,503,507,514,516,550`):

```text
CLAUSE_B_STATUS = PARTIAL_CANDIDATE
CLAUSE_C_STATUS = BLOCKED
CLAUSE_D_STATUS = UNRESOLVED_BLOCKER
CLAUSE_E_STATUS = PARTIAL_CANDIDATE
C1_MINIMAL_CLASS_STATUS = PARTIAL_CANDIDATE
C1_SCHWARZSCHILD_SUBCLASS_STATUS = PARTIAL_CANDIDATE
OVERALL_CANDIDATE_STATUS = BCE_PARTIAL_CANDIDATE_READY_FOR_REVIEW
```

**Correspondencia con el enunciado de la tarea:** el enunciado da `CLAUSE_E_STATUS =
CLOSED_SCHEMA_NOT_YET_EVALUABLE`; el valor literal en disco es `PARTIAL_CANDIDATE`. Ambos
describen el mismo hecho — el esquema formal de (e) está completo (E-set/E-element, niveles de
indistinguibilidad fijados) pero no es evaluable porque depende de una regla `R` aún no cerrada
(`dev/PR003_C1_BCE_CLOSED_CANDIDATE.md` Parte IV, "El esquema está completo; lo que falta ... es
exclusivamente la cláusula (c)"). Este documento usa el valor literal de disco
(`PARTIAL_CANDIDATE`) y anota esta correspondencia una sola vez aquí; no se reintroduce el sinónimo
del enunciado como si fuera un valor distinto.

**Preservado sin reinterpretación:**

```text
ALLOY_002_LOGICAL_WITNESS = PRESENT
ALLOY_002_PHYSICAL_WITNESS = NOT_ESTABLISHED
ALLOY_002_C1_WITNESS_STATUS = INVALID_UNDER_CONVEXITY_REQUIREMENT
BOUNDARY_BRACKET_STATUS = FAILED_BASELINE_UNDER_PRECOMMITTED_DENSITY_COVERAGE_CRITERION
BOUNDARY_BRACKET_ALLOWED_USE = DIAGNOSTIC_COMPARATOR
ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED   (entrada; reevaluado en D5)
Comité 012: OVERALL_VERDICT = C1_DEFINITION_PARTIALLY_CLOSED   (campo distinto, no se reescribe)
```

Núcleo cerrado de `𝔄_C1(O)` heredado sin cambios: preservación literal del subposet observado,
orden causal válido, convexidad causal del observado (`CONVEXITY_REQUIREMENT = MANDATORY_FOR_C1`,
comité 012 D2, no reabierto).

---

## 3. D1 — Groundedness del sector oculto

### Auditoría de opciones

| Opción | Convexidad | Ocultos desconectados | Riesgo de trivializar | `FutureAdmissible` previa | Interpretación física | Verificable en Alloy | Orientación temporal | Alcance |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **G0** — sin groundedness | Compatible (obligaciones ortogonales) | Permitidos sin restricción | Ninguno para pullbacks tipo-subconjunto (P1/P3): un elemento sin relación causal a `O` nunca puede entrar en `down_closure` ni en `R(C)∩O`. **Riesgo real solo para reglas globales tipo Q**: el realizador `(L_U,L_V)` es una propiedad de *todo* el poset `C`, así que un oculto totalmente desconectado podría alterar qué extensiones lineales existen y por tanto perturbar la tripartición restringida a `O` sin haber tocado `O` causalmente — una forma de "acción sin contacto causal" | No existe tal objeto en el repo (verificado, ver §2) | Ninguna — desconexión causal es normal en un sprinkling que cubre regiones spacelike separadas | Trivial (ausencia de restricción) | Ninguna (simétrico) | Clase general permisiva, sin nombre propio |
| **G1** — débil: `∀h∈H_C, ∃x∈O, x<_C h ∨ h<_C x` | Compatible, sin tensión lógica | Excluidos | Ninguno — restricción existencial simple, no afecta la evaluabilidad de ningún candidato de (c) | N/A | Descarta elementos "sin contacto causal" con lo observado, cerrando el riesgo de G0 para reglas globales | Trivial — cuantificador existencial de primer orden sobre relación finita | Ninguna (usa `∨`, simétrico) | `𝔄_C1(O)` |
| **G2** — futuro: `∀h∈H_C, ∃x∈O, x<_C h` | Compatible | Excluye ocultos puramente-pasado (todos sus vínculos a `O` son "antes de") | Ninguno directo, pero excluye completaciones legítimas que solo añaden historia pasada no observada | N/A | Motivación plausible solo si el objetivo es estructura de interior/trampeo (asimetría futuro-pasado, cf. `Θ_out`, EGS), pero eso es una hipótesis física específica, no una propiedad general de completaciones causales | Trivial | **Depende de una orientación temporal fija** (pasado/futuro), no simétrica | Sin justificación establecida para `𝔄_C1`; posible candidato futuro para `𝔄_Schw` si se conecta explícitamente a trampeo |
| **G3** — futuro con no-retorno: G2 `∧ ∀y∈O, ¬(h<_C y)` | Compatible | Excluye cualquier oculto con relación bidireccional a `O` | Alto para la clase general — excluye patrones de relación bidireccional perfectamente ordinarios en un causal set genérico no relacionados con trampeo | N/A | Formaliza exactamente "una vez dentro, no hay retorno al exterior observado" — corresponde de cerca al trampeo/`Θ_out` teleológico (`dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md §1`, `THEOREM-CONFIRMED`) | Trivial | Fuertemente dependiente de orientación temporal | Excesiva para `𝔄_C1`; motivada específicamente para `𝔄_Schw` (interior/trampeo) |
| **G4** — por componente causal | Compatible | Excluye solo componentes enteramente desconectados; permite cadenas de ocultos que se conectan entre sí y tocan `O` en algún punto | Ninguno, pero requiere definir "componente causal" (cierre transitivo del grafo de comparabilidad `O∪H_C`) — maquinaria no trivial hoy no implementada | N/A | Generalización razonable de G1 | Requiere una definición nueva de componente conexa antes de ser verificable — no trivial hoy | Ninguna | Refinamiento futuro válido para `𝔄_C1`, no necesario para el cierre mínimo actual |

### Posiciones

```text
POSITION_PI =
  G1 es la clausura mínima suficiente: cierra el riesgo de "acción sin contacto causal" para
  reglas globales futuras (Q-track) sin imponer una hipótesis física (dirección temporal) que
  no corresponde a la clase causal general. G3 es valioso pero debe quedar reservado
  explícitamente a 𝔄_Schw para no mezclar la pregunta C1 abstracta con una hipótesis de trampeo
  no adjudicada.

POSITION_FORMAL =
  G0 es técnicamente inofensivo para pullbacks de tipo subconjunto (P1/P3 nunca alcanzan un
  elemento desconectado), pero el candidato Q depende del realizador global (L_U,L_V) de todo
  C — un oculto desconectado SÍ puede alterar qué extensiones lineales existen y por tanto
  perturbar la tripartición restringida a O sin contacto causal con O. Esto es un defecto real,
  no hipotético, para cualquier regla que use información global del poset. G1 lo cierra con la
  restricción más débil posible. G4 es la generalización correcta a largo plazo pero requiere
  definir componente causal — innecesario para cerrar hoy.

POSITION_PHYSICS =
  G3 (futuro + no-retorno) es la formalización más fiel de "trampeo" — corresponde exactamente
  al carácter teleológico ya confirmado en el repo (Θ_out, apparent/trapping precursor). Pero
  adoptarla para la clase GENERAL 𝔄_C1 sería importar una hipótesis física específica
  (trampeo) como axioma matemático de la clase causal — eso invierte el orden correcto (primero
  la clase causal, luego la hipótesis física). Se apoya G1 para 𝔄_C1 y se registra G3 como
  candidato explícito para 𝔄_Schw, pendiente de una justificación escrita que conecte
  trampeo con la definición de referencia (c).

POSITION_ENGINEERING =
  G1 no cambia la clasificación de ningún testigo existente: se verificó a mano que tanto
  Completion A (E2<E1, E3<E1) como Completion B (E2<E0<E3) del testigo Alloy 002 YA satisfacen
  G1 — adoptarla no reclasifica retroactivamente nada. G1 es trivialmente codificable en Alloy
  (cuantificador existencial sobre relación finita). G4 requeriría implementar componentes
  conexas — coste de ingeniería no justificado hoy.

OBJECTIONS =
  (Retenida, en el espíritu del falsificador de comité 010): que G1 sea inofensivo para el
  único testigo existente no prueba que sea suficiente para CUALQUIER R futuro. Si un R
  candidato futuro depende de estructura aún más global o no local que Q, G1 podría no bastar
  y debería revisarse — esta decisión no se declara definitiva más allá de los candidatos de
  (c) auditados en esta misma sesión (D2).

CONSOLIDATED_DECISION =
  G1 se adopta como condición de groundedness de 𝔄_C1(O). G3 se registra formalmente como
  RECOMMENDED_FOR_SCHW_ONLY (no adoptada ahora; pendiente de justificación física explícita).
  G2 y G4 quedan DEFERRED. G0 queda REJECTED_TOO_WEAK.

CONFIDENCE = MEDIA
  (el argumento contra G0 — perturbación sin contacto causal de reglas globales tipo Q — es
  sólido y verificable por inspección de la construcción de Q, pero no hay una prueba
  exhaustiva de que G1 sea suficiente para todo candidato de R que pudiera proponerse en el
  futuro).
```

### Etiquetas finales D1

```text
G0 = REJECTED_TOO_WEAK
G1 = RECOMMENDED_FOR_C1
G2 = DEFERRED
G3 = RECOMMENDED_FOR_SCHW_ONLY
G4 = DEFERRED
```

### Verificación de no-reclasificación retroactiva de Alloy 002

Completion A: `H_C={E1}`, relaciones `E2<E1`, `E3<E1` (chain `E2<E3<E1`,
`product_order_check_alloy002_witness_note.md` §2). `G1` exige `∃x∈O={E2,E3}: x<_C E1 ∨
E1<_C x` — se satisface con `x=E2` (o `E3`). **G1 se cumple.**

Completion B: `H_C={E0}`, relaciones `E2<E0`, `E0<E3`. `G1` exige lo mismo para `E0` —
se satisface con `x=E2`. **G1 se cumple.**

**Conclusión:** ambas completaciones ya satisfacían G1 antes de esta sesión. Adoptar G1 **no
reclasifica** a ninguna de las dos: Completion A sigue admisible en `𝔄_C1(O)`; Completion B sigue
excluida por convexidad (B3), no por groundedness. `ALLOY_002_C1_WITNESS_STATUS =
INVALID_UNDER_CONVEXITY_REQUIREMENT` permanece la razón operativa exacta, sin cambio.

### Salida D1

```text
GROUNDEDNESS_DECISION = G1_ADOPTED_FOR_C1_G3_RESERVED_FOR_SCHW
GROUNDEDNESS_FORMULA = ∀h∈H_C, ∃x∈O, (x<_C h) ∨ (h<_C x)
GROUNDEDNESS_SCOPE = 𝔄_C1(O)  [G3 registrada para 𝔄_Schw(O), no adoptada]
GROUNDEDNESS_RATIONALE =
  Cierra el único defecto técnico identificado (perturbación sin contacto causal de reglas de
  referencia globales, relevante para el candidato Q de D2) con la restricción más débil
  posible; no impone ninguna hipótesis de orientación temporal; verificado que no reclasifica
  Alloy 002.
CLAUSE_B_REVISED_STATUS =
  PARTIAL_CANDIDATE (sin cambio en la etiqueta global, porque 𝔄_Schw sigue sin caracterización
  intrínseca — fuera del alcance de esta sesión). El bloqueo específico de groundedness que
  motivó esta sesión queda CERRADO dentro de ese estado parcial: 𝔄_C1(O) = B1 ∧ B2 ∧ B3 ∧ G1
  ∧ finitud, definición completa y copiable.
```

---

## 4. D2 — Regla de referencia inducida `R(C)`

### Candidato 1 — `R(C)=Max(C)` (no se reabre; se registra el rechazo definitivo)

`down(Max(C))=C` para todo poset finito no vacío ⟹ `H[C;R]=∅` siempre (comité 010 falsifier
ataque 2, `comite_decision_010.md:111`; confirmado ejecutablemente por comité 009 preflight,
`dev/PR003_C1_RELATIONAL_SPEC.md §9`). **`REJECTED_TRIVIAL`, definitivo, no se reabre.**

### Candidato 2 — tripartición de orden conjugado (Q-track)

Se leyó íntegramente `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §7.3-7.6 esta sesión para
decidir si es adoptable (R1) o solo desarrollable (R2). Hallazgos exactos:

- La construcción de `Q` (orientación transitiva del grafo de incomparabilidad de un realizador
  `P=L_U∩L_V`, condicional a `dim_DM(C)≤2`) está **completamente definida y es order-only** (§7.4.1).
- La **bipartición exhaustiva `{L_A,R_A}` está REFUTADA para `|A|≥2`** por un contraejemplo de
  intercalado trabajado explícitamente (§7.4.1: punto `x=(1,1)` queda `Q`-intercalado entre
  `a₁,a₂` de una antichain de marcador de dos elementos). Esto **no es una laguna, es una
  refutación** ya registrada en el propio documento fuente ("El lema de bipartición EXHAUSTIVA...
  es FALSO en general. [refutación, no laguna]").
- Lo que **sí sobrevive**: (i) bipartición limpia y canónica-salvo-swap para un marcador de **un
  solo elemento** (`|A|=1`, "Resultado positivo 1"); (ii) **tripartición** `{L_A,core_A,R_A}` para
  `|A|≥2` ("Resultado positivo 2") — el objeto que el candidato BCE ya usaba.
- **Unicidad salvo swap** depende de que la descomposición modular del grafo de incomparabilidad
  sea prima (Gallai) — marcado explícitamente `[PLAUSIBLE, UNVERIFIED]`, "no anclado a cita
  primaria en biblioteca" (§7.4.1).
- **Qué antichain `A` representa "la membrana"** no está especificado en ningún documento —
  es un parámetro de entrada aún libre, no resuelto por el material existente.
- El propio documento fuente declara el sub-problema **`III_PENDING_TWO_FACE_LEMMA`, "estado
  PROVISIONAL, NO un veredicto de cierre todavía"** (§7.6), con una "próxima ronda correcta" de
  cinco pasos explícitos (§7.6, punto final) — ninguno ejecutado.

Esto excluye directamente **R1** (adopción plena): el propio material de origen se autodeclara no
cerrado, con un lema refutado en su forma fuerte y una elección de parámetro (`A`) sin resolver. No
se fuerza un cierre que el material no sustenta.

```text
NAME = Conjugate-order lateral tripartition (Q-track)
FORMAL_DEFINITION =
  Cerrado: x<_Q y :⇔ U_x<U_y ∧ V_x>V_y, con realizador P=L_U∩L_V (requiere dim_DM(C)≤2).
  Cerrado (caso |A|=1): L_a={x spacelike a : x<_Q a}, R_a={x spacelike a : a<_Q x},
  bipartición limpia canónica-salvo-swap.
  No cerrado (caso |A|≥2, general): tripartición {L_A,core_A,R_A} con
  L_A={x:x<_Q a ∀a∈A}, R_A={x:a<_Q x ∀a∈A}, core_A=(N(A)\A)∖(L_A∪R_A) — objeto bien tipado
  pero SIN elección canónica de A todavía.
DOMAIN = subconjunto de 𝔄_C1(O) con dim_DM(C)≤2 [aprox. 𝔄_Schw], más una elección de marcador
         A⊆C NO especificada por ningún documento existente
CODOMAIN = partición de N(A) en tres clases (o dos, si |A|=1) — objeto de tipo distinto al
           candidato 1 (no un subconjunto simple de C)
ISOMORPHISM_STATUS = UNVERIFIED
  (la construcción de Q dado un A fijo es order-only y relabel-invariante; pero la unicidad
  global depende de primalidad modular (Gallai), marcada [PLAUSIBLE, UNVERIFIED] por la fuente
  misma; y la elección de A no tiene todavía una regla order-only canónica)
NONTRIVIALITY_STATUS = UNRESOLVED
  (ningún par de completaciones ha sido evaluado contra esta regla; ausencia de prueba en
  contra no se declara aquí como no-trivialidad, siguiendo la regla de adjudicación)
PHYSICAL_STATUS =
  Diseñada explícitamente para evitar la circularidad §7.5 con el estadístico de futuro que usa
  el PASS (ventaja metodológica real). Interpretación como "referencia de horizonte" es
  aspiracional, no establecida — el propio documento fuente la marca PROVISIONAL.
KNOWN_FAILURES =
  bipartición exhaustiva refutada para |A|≥2 (contraejemplo de intercalado, no hipotético)
STATUS = DEFERRED (evaluado en esta sesión, no adoptado — ver decisión de ruta abajo)
```

### Decisión de ruta

```text
POSITION_PI =
  R1 es prematuro: el propio documento que define Q se autodeclara "PROVISIONAL, no cerrado".
  Adoptarlo ahora y "completarlo" después de ver resultados sería exactamente el post-hoc
  tuning que las reglas fundacionales prohíben. R2 (autorizar desarrollo) es la ruta correcta —
  mantiene el impulso sin sobreclamar cierre.

POSITION_FORMAL =
  La construcción de Q en sí (dado un marcador A fijo) es rigurosa y cerrada. Lo que falta es
  puramente definicional, no solo de implementación: (i) una regla order-only para elegir A;
  (ii) verificación de primalidad modular (o una regla de desempate relabel-invariante si no se
  cumple, como el propio §7.4.1 sugiere). El caso |A|=1 es el sub-candidato más cercano a un
  cierre real — se recomienda priorizar su formalización como paso siguiente concreto dentro de
  R2.

POSITION_PHYSICS =
  La virtud de Q (evitar circularidad con el estadístico de futuro del PASS) es real y debe
  preservarse en cualquier candidato futuro. Pero "marcador de membrana A" necesita
  corresponder a algo físicamente motivado (p. ej. una antichain cercana al horizonte,
  order-only) — eso no está propuesto en ningún documento. Se apoya R2, con esa tarea como
  siguiente paso físico concreto.

POSITION_ENGINEERING =
  Cero código ejecutable existe para Q o la tripartición en `nachocausal/` (verificado por
  `rg` en la sesión previa que produjo el candidato BCE). Implementarlo es una tarea de
  desarrollo no trivial. Se apoya R2 explícitamente, no R1 (prematuro) ni R3 (no hay base para
  rechazar algo con un resultado parcial positivo real, el caso |A|=1) ni R4 (rechazar
  candidatos y exigir uno enteramente nuevo desperdiciaría ese resultado parcial).

OBJECTIONS =
  Autorizar "desarrollo" (R2) no debe leerse silenciosamente como autorización para tratar Q
  como si ya fuera la regla operativa en ningún documento futuro — es una autorización de
  trabajo conceptual/de especificación, no una adopción.

CONSOLIDATED_DECISION =
  R2 — se autoriza el desarrollo posterior de especificación (no implementación, no búsqueda de
  testigos) del candidato Q, priorizando: (a) el caso |A|=1 (ya canónico) como sub-candidato
  más cercano al cierre; (b) una regla order-only para elegir el marcador A en el caso general;
  (c) verificación o regla de desempate para la primalidad modular. R=Max(C) permanece
  REJECTED_TRIVIAL, definitivo.

CONFIDENCE =
  ALTA en rechazar R1 (el propio material fuente se autodeclara no cerrado, con un lema
  refutado en su forma fuerte — no es una interpretación de este comité, es literal del
  documento). MEDIA en que R2 (vs. R4) es la ruta correcta — ningún rol propuso R4 dado el
  resultado parcial positivo genuino del caso |A|=1.
```

### Salida D2

```text
REFERENCE_RULE_DECISION = R2_AUTHORIZE_DEVELOPMENT
REFERENCE_RULE_NAME = Conjugate-order lateral tripartition (Q-track), candidato en desarrollo
REFERENCE_RULE_FORMAL_DEFINITION =
  Q-order cerrada dado un marcador fijo A (ver arriba); caso |A|=1 canónico y cerrado; caso
  general |A|≥2 con tripartición bien tipada pero SIN elección canónica de A todavía.
REFERENCE_RULE_ISOMORPHISM_STATUS = UNVERIFIED (primalidad modular [PLAUSIBLE], elección de A no
  order-only todavía)
REFERENCE_RULE_NONTRIVIALITY_STATUS = UNRESOLVED (sin evaluación contra ningún par)
REFERENCE_RULE_PHYSICAL_STATUS = PROVISIONAL (evita circularidad §7.5; no establecida como "la"
  referencia de horizonte)
CLAUSE_C_REVISED_STATUS = AUTHORIZED_FOR_DEVELOPMENT
```

---

## 5. D3 — Regla de pullback

### Auditoría

```text
POSITION_PI =
  Adoptar una familia de pullbacks tipada por el codominio de R(C) es la vía correcta dado que
  D2 no cierra R todavía — evita bloquear el pullback en espera indefinida de una decisión sobre
  R, y respeta la instrucción explícita de no cerrar el pullback antes del tipo de R salvo que
  se tipifique la familia.

POSITION_FORMAL =
  P1 (intersección literal) y P2 (preimagen por ι_C) son literalmente EQUIVALENTES en este
  proyecto, siempre, sin condición adicional: ι_C es la inclusión-identidad de conjuntos con la
  misma etiqueta (obligación B1, no un embedding abstracto), por lo que
  ι_C⁻¹(R(C)) = R(C)∩O exactamente. P3 (down-closure observada) es una generalización real ya
  con precedente de código (`c1_selector.down_closure`) — estrictamente más informativa que
  P1/P2 cuando R(C) contiene elementos por encima de O. Para R(C) de tipo partición (candidato
  Q), P5 (aplicar la misma regla base componente a componente) es la extensión natural sin
  introducir maquinaria nueva.

POSITION_PHYSICS =
  La lectura de P3 como "accesibilidad desde la referencia" coincide exactamente con el marco
  ya usado por el interfaz C1 (`accessible`/`black_region` en `c1_selector.c1_selector`) — es la
  noción físicamente natural de pullback para referencias de tipo subconjunto.

POSITION_ENGINEERING =
  P3 tiene precedente de código directo y de bajo riesgo (`nachocausal/c1_selector.down_closure`,
  ya Guard-v verificado en su forma actual). P5 no requiere ninguna primitiva nueva más allá de
  aplicar P3 (o P1/P2) por separado a cada componente de una estructura tipada — desarrollo de
  bajo riesgo si Q se implementa eventualmente.

OBJECTIONS =
  R4 (`dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` §3(d)) ya señaló que `down_closure` "no ha
  sido probada como la única regla de pullback válida ni acordada por comité" — esta sesión ES
  el acto de adjudicación pendiente, no una reafirmación silenciosa. Se registra explícitamente
  que adoptar P3 como default para R de tipo subconjunto NO valida retroactivamente al
  candidato 1 (Max(C)), que permanece REJECTED_TRIVIAL por una razón independiente del
  pullback elegido (la trivialidad está en R, no en PB_O).

CONSOLIDATED_DECISION =
  Familia de pullbacks tipada por el codominio de R(C):
  - Si R(C) es un subconjunto de C: PB_O(R(C)) := down_closure(C,R(C)) ∩ O  [= P3, con P1≡P2
    registrada como hecho de equivalencia, no como regla independiente adoptada]
  - Si R(C) es una estructura tipada (partición/interfaz, p. ej. la tripartición Q):
    PB_O(R(C)) := aplicar la misma regla (down-closure) a cada componente por separado,
    produciendo una partición inducida de O del mismo tipo  [= P5]

CONFIDENCE =
  ALTA (P1≡P2 es una prueba directa de la convención de inclusión literal del proyecto; P3 tiene
  precedente de código verificado; P5 es una generalización de bajo riesgo, sin maquinaria
  nueva).
```

### Salida D3

```text
PULLBACK_DECISION = TYPED_FAMILY_BY_CODOMAIN
PULLBACK_FORMAL_DEFINITION =
  Subconjunto: PB_O(R(C)) := down_closure(C,R(C)) ∩ O   (P3; P1≡P2 exacto por convención de
  ι_C, no una regla independiente)
  Estructura/partición: PB_O(R(C)) := aplicación componente-a-componente de la misma regla (P5)
PULLBACK_DOMAIN = R(C) ∈ 2^C (subconjunto) o partición/estructura tipada de C
PULLBACK_CODOMAIN = objeto del mismo tipo que R(C), restringido a O
PULLBACK_DEPENDENCE_ON_R =
  La forma exacta de PB_O depende únicamente del TIPO (codominio) de R(C), ya fijado aquí para
  ambos tipos conocidos (subconjunto y partición); no depende de CUÁL R(C) se adopte finalmente
  dentro de cada tipo.
PULLBACK_INVARIANCE_STATUS =
  down_closure ya está Guard-v verificado en su uso actual (`nachocausal/c1_selector.py`,
  `selection_guard.py`); la extensión componente-a-componente (P5) hereda esa invarianza sin
  necesitar una prueba nueva, siempre que cada componente se procese con la misma regla base.
CLAUSE_D_REVISED_STATUS = CONDITIONALLY_CLOSED_ON_R
```

---

## 6. D4 — Coherencia conjunta B/C/D/E

Verificación documental (sin ejecución):

- **`R` definida en toda completación admisible relevante:** NO — `R` sigue `AUTHORIZED_FOR_DEVELOPMENT`,
  no `CLOSED`; el candidato Q carece de regla order-only para elegir el marcador `A` en el caso
  general y de verificación de unicidad.
- **Pullback con dominio/codominio compatibles:** SÍ, condicionalmente — la familia tipada (D3)
  cubre ambos tipos de codominio conocidos (subconjunto, partición); queda `CONDITIONALLY_CLOSED_ON_R`,
  no un bloqueo propio.
- **`E` compara objetos del mismo tipo:** SÍ, por construcción — `PB_O` siempre devuelve un objeto
  del mismo tipo que `R(C)` (Parte IV del candidato BCE, sin cambios).
- **`E` no accede a información prohibida:** SÍ — ninguna de las decisiones de esta sesión introduce
  acceso a `H_C`, coordenadas, o metadatos del generador; `G1` es una condición sobre la
  completación misma, no sobre lo que ve el estimador.
- **`E-element` y `E-set` mantienen su equivalencia cuando corresponde:** SÍ, sin cambio — la
  equivalencia es exacta para `R` de tipo subconjunto (candidato BCE, Parte IV); para `R` de tipo
  partición (Q), `E-set` se generaliza a desigualdad de particiones inducidas y `E-element` a un
  testigo puntual de co-pertenencia distinta — ambas formas siguen bien definidas, la
  equivalencia puntual-conjunto se preserva por ser dominios finitos.
- **Indistinguibilidad observacional fijada independientemente de `E`:** SÍ, sin cambio (R4 §2,
  filas 1-2: mismo carrier + misma relación inducida).
- **`E` no se vuelve tautológica:** verificado bajo el candidato 1 (`Max(C)`: `E` es idénticamente
  falso siempre — no es tautológica, es vacía, distinción ya hecha en el candidato BCE); bajo el
  candidato 2 (Q), no evaluable todavía, por lo que tampoco puede declararse tautológica ni no
  tautológica — permanece `UNRESOLVED`, dependiente del cierre de `R`.

### Salida D4

```text
CLAUSE_E_EVALUABILITY_STATUS = NOT_EVALUABLE_PENDING_REFERENCE_RULE_CLOSURE
E_ELEMENT_STATUS = STRUCTURALLY_DEFINED_EQUIVALENT_TO_E_SET_FOR_SUBSET_TYPE_R
E_SET_STATUS = STRUCTURALLY_DEFINED_GENERALIZES_TO_PARTITION_INEQUALITY_FOR_STRUCTURED_R
OBSERVATIONAL_EQUIVALENCE_STATUS = CLOSED
BCE_JOINT_COHERENCE_STATUS = BLOCKED_BY_REFERENCE_RULE
```

El único bloqueo restante para evaluar `E` no vacuamente es el cierre de `(c)`. `(b)` (groundedness)
y `(d)` (pullback) quedaron resueltos o condicionalmente cerrados en esta sesión.

---

## 7. D5 — Autorización posterior

```text
POSITION_PI =
  Autorizar exclusivamente desarrollo conceptual del candidato Q (no implementación de código,
  no Alloy, no Lean, no búsqueda de testigos) es lo único consistente con que (c) siga móvil.

POSITION_FORMAL =
  Prioridad concreta: formalizar el caso |A|=1 (ya canónico) como el primer sub-candidato
  cerrable de R; en paralelo, proponer una regla order-only para la elección de A en el caso
  general.

POSITION_PHYSICS =
  Proponer un candidato físicamente motivado para el marcador A (antichain cercana al horizonte,
  order-only) es el trabajo físico pendiente concreto — sin él, Q no tiene todavía
  interpretación física operacional más allá de "evita la circularidad §7.5".

POSITION_ENGINEERING =
  Ninguna implementación de código está autorizada por esta sesión (instrucción explícita del
  usuario); cualquier desarrollo de Q permanece en fase de especificación escrita.

CONSOLIDATED_DECISION =
  Q_CANDIDATE_DEVELOPMENT_ONLY. No se autoriza Alloy 003 (C y E siguen móviles). No se autoriza
  Lean como sustituto de la definición física ausente. No se autoriza ninguna búsqueda física
  bajo 𝔄_Schw (sigue sin caracterización intrínseca suficiente, sin cambio respecto a comité
  012).
```

### Salida D5

```text
NEXT_AUTHORIZED_ACTION =
  Redacción (solo escritura, sin código, sin Alloy, sin Lean) de: (i) la formalización completa
  del caso |A|=1 de Q como sub-candidato cerrado de referencia; (ii) una propuesta order-only
  para la elección del marcador A en el caso general |A|≥2; (iii) verificación conceptual (por
  escrito, sin ejecución) de si la primalidad modular puede argumentarse o si se necesita una
  regla de desempate explícita.
NEXT_FORBIDDEN_ACTIONS =
  Alloy 003 en cualquier modalidad mientras (c) no esté CLOSED (no solo AUTHORIZED_FOR_DEVELOPMENT) |
  usar Lean como sustituto de la definición física de R todavía ausente |
  tratar G1 como si fuera G3 (reservada exclusivamente a 𝔄_Schw, no adoptada) |
  implementar código para Q o la tripartición en esta fase |
  cualquier búsqueda de testigos físicos bajo 𝔄_Schw mientras carezca de caracterización intrínseca |
  reclasificar boundary-bracket FAIL como PASS |
  citar "Variant A"/"Bruno" (checkout externo, BLOCKED_WRONG_REPOSITORY_CONTEXT) como evidencia |
  introducir "ORDER_ONLY_MAXIMALITY_FLIP_CANDIDATE" como nombre estándar |
  commit o push de este documento o de cualquier artefacto R1-R4/BCE sin autorización explícita del PI
ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED
LEAN_AUTHORIZATION_STATUS = NOT_AUTHORIZED
PHYSICAL_SEARCH_AUTHORIZATION_STATUS = NOT_AUTHORIZED
```

---

## 8. Tratamiento de Alloy 002 (histórico, no reanalizado)

```text
ALLOY_002_LOGICAL_WITNESS = PRESENT
ALLOY_002_PHYSICAL_WITNESS = NOT_ESTABLISHED
ALLOY_002_C1_WITNESS_STATUS = INVALID_UNDER_CONVEXITY_REQUIREMENT
```

Verificado en §3 (D1): ninguna de las decisiones de esta sesión (G1, R2 sobre Q, pullback tipado)
reclasifica el testigo. Completion A sigue admisible en `𝔄_C1(O)`; Completion B sigue excluida por
convexidad. No se ejecutó Alloy en ningún momento de esta sesión.

## 9. Tratamiento de boundary-bracket (sin cambios)

```text
BOUNDARY_BRACKET_STATUS = FAILED_BASELINE_UNDER_PRECOMMITTED_DENSITY_COVERAGE_CRITERION
BOUNDARY_BRACKET_ALLOWED_USE = DIAGNOSTIC_COMPARATOR
```

Objeto de nivel 5 (comité 012 §3), ortogonal a todas las decisiones de esta sesión. No se usa como
evidencia positiva de reconstrucción en ningún punto de este documento.

---

## 10. Síntesis

Los tres bloqueos identificados avanzan de forma desigual: **groundedness (B) queda cerrada** con
la adopción de `G1` (mínima, verificada sin reclasificar Alloy 002); **el pullback (D) queda
condicionalmente cerrado** como familia tipada por codominio, dependiente solo de qué `R` se
adopte, no de una elección adicional propia; **la regla de referencia (C) permanece el bloqueo
real** — el candidato Q tiene una construcción parcial rigurosa (caso `|A|=1`) pero su forma
general está refutada en la versión fuerte (bipartición exhaustiva) y su elección de marcador `A`
no tiene todavía una regla order-only. No se fuerza un cierre que el material de origen no
sustenta: el propio `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §7.6 se autodeclara
"PROVISIONAL, no cerrado" para exactamente este punto.

El predicado `E` sigue sin ser evaluable, pero por una única razón identificada
(`BLOCKED_BY_REFERENCE_RULE`), no por múltiples causas dispersas como antes de esta sesión.

## 11. User sign-off

_(dejado en blanco para el usuario — decisión, fecha, y cualquier nota que prevalezca)_

---

## Bloque normativo

```text
COMMITTEE_ID = 013

INPUT_CANDIDATE = dev/PR003_C1_BCE_CLOSED_CANDIDATE.md
INPUT_CANDIDATE_STATUS = BCE_PARTIAL_CANDIDATE_READY_FOR_REVIEW

GROUNDEDNESS_DECISION = G1_ADOPTED_FOR_C1_G3_RESERVED_FOR_SCHW
GROUNDEDNESS_FORMULA = ∀h∈H_C, ∃x∈O, (x<_C h) ∨ (h<_C x)
GROUNDEDNESS_SCOPE = 𝔄_C1(O) [G3 reservada, no adoptada, para 𝔄_Schw(O)]
CLAUSE_B_REVISED_STATUS =
  PARTIAL_CANDIDATE (bloqueo de groundedness CERRADO vía G1; 𝔄_Schw intrínseca sigue abierta,
  fuera de alcance de esta sesión)

REFERENCE_RULE_DECISION = R2_AUTHORIZE_DEVELOPMENT
REFERENCE_RULE_NAME = Conjugate-order lateral tripartition (Q-track)
REFERENCE_RULE_FORMAL_DEFINITION =
  Q cerrada dado marcador A fijo; caso |A|=1 canónico cerrado; caso general |A|≥2 sin elección
  canónica de A ni primalidad modular verificada
REFERENCE_RULE_ISOMORPHISM_STATUS = UNVERIFIED
REFERENCE_RULE_NONTRIVIALITY_STATUS = UNRESOLVED
REFERENCE_RULE_PHYSICAL_STATUS = PROVISIONAL
CLAUSE_C_REVISED_STATUS = AUTHORIZED_FOR_DEVELOPMENT

PULLBACK_DECISION = TYPED_FAMILY_BY_CODOMAIN
PULLBACK_FORMAL_DEFINITION =
  subconjunto: down_closure(C,R(C))∩O ; estructura/partición: aplicación componente-a-componente
  de la misma regla
PULLBACK_DEPENDENCE_ON_R = solo del tipo (codominio) de R, no de cuál R se adopte dentro de un tipo
PULLBACK_INVARIANCE_STATUS = HEREDADA_DE_DOWN_CLOSURE_GUARD_V_VERIFICADO
CLAUSE_D_REVISED_STATUS = CONDITIONALLY_CLOSED_ON_R

CLAUSE_E_EVALUABILITY_STATUS = NOT_EVALUABLE_PENDING_REFERENCE_RULE_CLOSURE
OBSERVATIONAL_EQUIVALENCE_STATUS = CLOSED
BCE_JOINT_COHERENCE_STATUS = BLOCKED_BY_REFERENCE_RULE

ALLOY_002_LOGICAL_WITNESS = PRESENT
ALLOY_002_PHYSICAL_WITNESS = NOT_ESTABLISHED
ALLOY_002_C1_WITNESS_STATUS = INVALID_UNDER_CONVEXITY_REQUIREMENT

BOUNDARY_BRACKET_STATUS = FAILED_BASELINE_UNDER_PRECOMMITTED_DENSITY_COVERAGE_CRITERION
BOUNDARY_BRACKET_ALLOWED_USE = DIAGNOSTIC_COMPARATOR

ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED
LEAN_AUTHORIZATION_STATUS = NOT_AUTHORIZED
PHYSICAL_SEARCH_AUTHORIZATION_STATUS = NOT_AUTHORIZED

NEXT_AUTHORIZED_ACTION =
  Especificación escrita únicamente (sin código/Alloy/Lean) de: formalización cerrada del caso
  |A|=1 de Q; propuesta order-only para el marcador A en el caso general; evaluación conceptual
  de la primalidad modular o una regla de desempate explícita.
NEXT_FORBIDDEN_ACTIONS =
  Alloy 003 antes de que (c) esté CLOSED | Lean como sustituto de R ausente | tratar G1 como G3 |
  implementar código para Q | búsqueda física bajo 𝔄_Schw sin caracterización intrínseca |
  reclasificar boundary-bracket FAIL como PASS | citar "Variant A"/"Bruno" como evidencia |
  introducir ORDER_ONLY_MAXIMALITY_FLIP_CANDIDATE como nombre estándar | commit o push sin
  autorización explícita del PI

OVERALL_VERDICT = BCE_DEFINITION_PARTIALLY_CLOSED
```

---

# Migración al esquema vigente — 2026-07-28

> Apéndice de compatibilidad documental. No reabre la deliberación ni altera el bloque normativo
> original. La decisión 042 absorbió después la línea C1 para la planificación futura.

```text
ACTA_DISPOSITION = SUPERSEDED_FOR_FORWARD_PLANNING_BY_DECISION_042
HISTORICAL_FINDINGS = PRESERVED
ANNULLED = NO
SCHEMA_MIGRATION_ONLY = YES
```

## 1. Decision question

Correspondencia: la pregunta original de §1 sobre el cierre no circular del candidato BCE.

## 2. Verified state

Correspondencia: el estado de entrada de §2. No se añadió evidencia ni se ejecutó código en esta
migración.

## 3. Dossier

El dossier histórico es el inventario de §2 y el bloque normativo original.

## 4. Expert briefs

Las posiciones históricas están distribuidas en D1–D5; no se reconstruyen retrospectivamente.

### Reproducibility engineer brief

Mapeado a los límites de autorización y a la disciplina de no ejecución.

### Mathematician brief

Mapeado a las auditorías de groundedness, regla de referencia y pullback.

### Mathematical logic brief

No existía como rol separado en el formato original; no se le atribuye una opinión retrospectiva.

### Physicist brief

Mapeado a la interpretabilidad física y a los bloqueos de la regla de referencia.

## 5. Falsifier attack

Se preservan la no trivialidad, la invariancia y el bloqueo por regla de referencia como ataques
centrales del acta.

## 6. Pre-registration verdict

- Verdict: PASS
- Motivo: acta documental; ninguna ejecución, semilla, implementación o cambio del sello.

## 7. Literature verdict

No se hace revisión bibliográfica nueva. Solo se conservan las anclas verificadas en el documento
histórico.

## 8. Synthesis

013 cerró parcialmente BCE y dejó la cláusula C en desarrollo documental. La decisión 014 revisó
esa senda y la decisión 042 la retiró de la planificación futura.

## 9. Next-step spec

No se reactiva el paso autorizado en 013. Cualquier nueva investigación requiere un contrato
separado bajo el norte vigente.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off

La migración de esquema fue autorizada por la instrucción del usuario de 2026-07-28. No equivale
a una nueva aprobación científica ni autoriza ejecución.
