# PR-003 — Desarrollo de la regla de referencia Q (fase escrita, autorizada por comité 013)

> Autorizado por `docs/comite/comite_decision_013_c1-bce-review.md`,
> `NEXT_AUTHORIZED_ACTION`: especificación escrita únicamente (sin código, sin Alloy, sin Lean) del
> candidato Q — formalización del caso `|A|=1`, regla order-only de selección del marcador `A` para
> `|A|>1`, y evaluación de primalidad modular / regla de desempate. **Sesión exclusivamente
> conceptual y documental.** No se ejecutó ninguna simulación, búsqueda, script, Alloy, Lean ni
> modificación de código. Sin commit ni push.
>
> Preservado sin reapertura: `GROUNDEDNESS_DECISION = G1` para `𝔄_C1(O)`; `G3 =
> RECOMMENDED_FOR_SCHW_ONLY` (no adoptada); pullback condicionalmente cerrado como familia tipada
> por codominio (`down_closure(C,R(C))∩O` para tipo subconjunto; aplicación componente a componente
> para tipo estructura/partición); `CONVEXITY_REQUIREMENT = MANDATORY_FOR_C1`; `R=Max(C)` sigue
> `REJECTED_TRIVIAL`, definitivo, no reabierto.

## 0. Fuentes leídas íntegramente esta sesión

| Archivo | Uso |
|:---|:---|
| `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` (completo, incluyendo §7.1–7.6 y §9) | Definición real de `A`, orden conjugado `Q`, tripartición, lema de dos caras, primalidad modular, `H[C;R]` |
| `dev/PR003_C1_BCE_CLOSED_CANDIDATE.md` | Parte III (candidato Q ya auditado como `DEFERRED`), Parte IV (esquema E) |
| `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` | Terminología de las cinco cláusulas |
| `docs/comite/comite_decision_012_c1-admissible-completion-class.md` | D1/D2 preservados |
| `docs/comite/comite_decision_013_c1-bce-review.md` | Groundedness (G1/G3), pullback tipado, autorización de esta fase |
| `docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md` | Falsifier ataque 2 sobre `R=Max(C)`; mathematician brief sobre equivarianza de automorfismos y asimetría genérica de Poisson (`comite_decision_010.md:81`) |
| `nachocausal/c1_selector.py`, `nachocausal/selection_guard.py` | Precedente de código para `Max(C)`, `down_closure`, Guard-v |

**Búsqueda adicional realizada** (`rg` sobre todo el repositorio, excluyendo `biblioteca/`): los
únicos artefactos que mencionan "orden conjugado", "marcador A", "tripartición", "primalidad
modular", "two-face", "isInterface" o "automorfismo" son exactamente los cinco documentos listados
arriba más `dev/INTRINSIC_OBSERVABLE_AUDIT_NOTES.md` (mención tangencial de "automorfismos
(reetiquetados)" sin relación con la selección de marcadores). No existe ningún otro documento que
defina estos términos de forma independiente. No se encontró terminología de nodos
serie/paralelo/primo de la descomposición modular en ningún documento del proyecto — se cita
Gallai 1967 y Trotter genéricamente (`dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §8) sin
desarrollar el árbol de descomposición en detalle; no se inventa aquí esa estructura.

---

# Parte I — Reconstrucción exacta del candidato Q existente

```text
Q_SOURCE_DEFINITION =
  Dado un realizador P_C = L_U ∩ L_V (orden-producto 2D, condicional a la Proposición 7.3 —
  ver caveat abajo), el orden conjugado se define x <_Q y :⇔ U_x<U_y ∧ V_x>V_y — la
  orientación transitiva del grafo de incomparabilidad de P_C (`dev/PR003_RELATIONAL_HORIZON_
  DEFINITION_NOTES.md` §7.4.1). Dado un marcador A ⊆ C (antichain candidata a "membrana"),
  se define N(A) como una losa spacelike (todo x∈N(A)\A es P-incomparable a todo A — §7.4).
  Para |A|=1 (A={a}): L_a={x∈spacelike(a): x<_Q a}, R_a={x∈spacelike(a): a<_Q x},
  spacelike(a)=N(a), bipartición EXHAUSTIVA y limpia, canónica salvo swap de Q (§7.4.1,
  "Resultado positivo 1"). Para |A|≥2: tripartición {L_A,core_A,R_A} con
  L_A={x:x<_Q a ∀a∈A}, R_A={x:a<_Q x ∀a∈A}, core_A=(N(A)\A)∖(L_A∪R_A) — el "grosor
  relacional de la membrana" (§7.4.1, "Resultado positivo 2").

Q_SOURCE_DOMAIN =
  Completaciones C con dim_DM(C)≤2 (Prop. 7.3, CONDICIONAL — ver caveat), más DOS elecciones no
  cerradas por ningún documento: (i) el marcador A⊆C; (ii) la extensión exacta de N(A) (el
  texto usa "losa spacelike" cualitativamente; ningún documento fija un radio, ventana de
  altura, o criterio de vecindad preciso más allá del ejemplo trabajado de §7.4.1).

Q_SOURCE_CODOMAIN =
  NO es un subconjunto simple ni una relación: para |A|=1, una partición de dos clases
  {L_a,R_a} de N(a); para |A|≥2, una partición de tres clases {L_A,core_A,R_A} de N(A)\A.
  Es un objeto de tipo "partición etiquetada", consistente con el candidato "P5 — pullback
  estructural" ya fijado por comité 013.

Q_SOURCE_REQUIRED_CHOICES =
  1. El marcador A (qué elemento(s) de C representan "la membrana") — NO especificado por
     ningún documento existente, es exactamente el objeto de la Parte III de este documento.
  2. La extensión de N(A) ("vecindad" spacelike) — tampoco especificada de forma general,
     solo ejemplificada.
  3. Si la descomposición modular no es prima: una regla de desempate para orientar módulos
     independientemente — mencionada como posibilidad ("orientar el módulo por su propio
     sub-conjugado, recursivamente", §7.4.1) pero NO desarrollada ni cerrada.
  4. La Proposición 7.3 misma es CONDICIONAL: "Supóngase que la relación producida por
     past_matrix_fast coincide exactamente con la causalidad radial de la métrica
     Schwarzschild en el parche ingoing-EF utilizado" (§7.3) — el paso "parche EF =
     restricción del producto Kruskal" está marcado [UNVERIFIED] vs. cita primaria, "pero es
     estándar". `dim_DM(C)≤2` para la familia generadora NO es, por tanto, un hecho
     incondicionalmente establecido en estos documentos — es una hipótesis físicamente
     plausible y auditada por lectura de código, no una medición ni una prueba formal cerrada.
     Se preserva esta distinción explícitamente; no se trata Prop. 7.3 como un teorema
     incondicional en el resto de este documento.

Q_SOURCE_KNOWN_COUNTEREXAMPLES =
  Contraejemplo de intercalado trabajado explícitamente (§7.4.1): A={a₁,a₂}, a₁=(U,V)=(0,2),
  a₂=(2,0) (antichain spacelike, a₁<_Q a₂); vecino x=(1,1) es spacelike a ambos y queda
  a₁<_Q x <_Q a₂ — INTERCALADO, ni en L_A ni en R_A. Refuta la bipartición exhaustiva para
  |A|≥2 de forma genérica ("cualquier antichain de extensión espacial >0 tiene vecinos
  spacelike en su hueco interior").

Q_SOURCE_OPEN_LEMMAS =
  1. Lema de dos caras (§7.4): losa spacelike + Q-convexidad de A + exhaustividad
     N(A)\A=L_A⊔R_A sin residuo — PROBADO solo para |A|=1; REFUTADO en forma fuerte para
     |A|≥2 (sobrevive la tripartición, no la bipartición).
  2. Primalidad de la descomposición modular del grafo de incomparabilidad — marcada
     [PLAUSIBLE, UNVERIFIED], "no anclado a cita primaria en biblioteca" (§7.4.1).
  3. La hipótesis de la Proposición 7.3 misma (ver Q_SOURCE_REQUIRED_CHOICES punto 4).
```

**Preservado sin conversión a "laguna":**

```text
BIPARTITION_STATUS = REFUTED_FOR_|A|>=2
TRIPARTITION_STATUS = PROVISIONAL
III_PENDING_TWO_FACE_LEMMA = OPEN
```

El propio documento fuente es explícito: "El lema de bipartición EXHAUSTIVA, tal como se pidió, es
FALSO en general. **[refutación, no laguna]**" (§7.4.1). Este documento preserva esa distinción sin
suavizarla.

---

# Parte II — Caso canónico `|A|=1`

## Formalización

Sea `a∈C` un marcador único (fijado externamente — su selección se aborda en la Parte III, no
aquí).

1. **Determinación de `a`:** NO se determina en esta sección — es la entrada externa que la Parte
   III debe proveer mediante una regla order-only. Esta sección formaliza únicamente la
   construcción **dado** `a`.

2. **Orden conjugado, dado `a`:**
   ```
   P_C = L_U ∩ L_V                                    (realizador, condicional a Prop. 7.3)
   x <_Q y :⇔ U_x < U_y ∧ V_x > V_y                    (orientación transitiva de incomparabilidad)
   ```
   Construcción idéntica a la general (Parte I); no depende de propiedades especiales de `a` más
   allá de ser un único elemento.

3. **Tripartición (degenerada a bipartición para `|A|=1`):**
   ```
   spacelike(a) := {x∈C : x incomparable a a bajo P_C}
   L_a := {x∈spacelike(a) : x <_Q a}
   R_a := {x∈spacelike(a) : a <_Q x}
   ```
   Exhaustividad: `spacelike(a) = L_a ⊔ R_a` — para un único marcador, todo `x` spacelike a `a`
   satisface exactamente una de `x<_Q a` o `a<_Q x` (orden conjugado total sobre pares
   incomparables, §7.4.1). **No hay clase `core` residual** cuando `|A|=1` — a diferencia del caso
   general, aquí no hay "hueco interior" entre múltiples elementos del marcador.

4. **Independencia de elecciones, dado `a` fijo:** una vez fijado `a`, `{L_a,R_a}` queda
   **completamente determinado** por la relación `≺` de `C` — no hay una segunda elección libre
   (a diferencia de `|A|≥2`, donde además de `A` hace falta fijar `N(A)` y, potencialmente, una
   regla de desempate modular). La única ambigüedad residual es el **swap global** `Q↔Q⁻¹`
   (equivalente a `L_a↔R_a`) — una libertad de orientación reconocida explícitamente por la fuente,
   no una falta de definición.

5. **Comportamiento bajo isomorfismos:** si `φ:C→C'` es un isomorfismo de orden y `a'=φ(a)`, el
   realizador de `C'` se obtiene transportando `(U,V)` a través de `φ` (la construcción de `P_C`
   depende solo de la estructura de orden, no de etiquetas), por lo que `Q` transporta
   correctamente: `φ(L_a)=L_{a'}` y `φ(R_a)=R_{a'}`, salvo el mismo swap global reconocido en el
   punto 4. Esta es exactamente la propiedad que la fuente reclama en §7.6 ("order-only y
   relabel-invariante"); no existe, sin embargo, una prueba Lean o formal explícita de esta
   naturalidad — es una afirmación conceptual del dev note, no verificada mecánicamente.

6. **Referencia física pretendida:** los dos lados laterales/espaciales del marcador candidato de
   membrana `a`, construidos deliberadamente **sin** usar la asimetría de futuro que el estimador
   del PASS mide después (§7.5, restricción anti-circularidad vinculante). No se ha establecido que
   `{L_a,R_a}` corresponda a la referencia de horizonte real — es la interpretación aspiracional,
   marcada `PROVISIONAL` por la propia fuente (§7.6).

7. **Pullback componente a componente:** siguiendo la familia tipada de comité 013
   (`docs/comite/comite_decision_013_c1-bce-review.md` D3), para un objeto de tipo
   partición/estructura, `PB_O` se aplica componente a componente:
   ```
   PB_O({L_a,R_a}) := (down_closure(C,L_a)∩O , down_closure(C,R_a)∩O)
   ```
   **Nota abierta no cerrada por ningún comité:** el esquema de comité 013 fue fijado
   genéricamente ("aplicar la misma regla base [down-closure] componente a componente"), motivado
   originalmente por la lectura de "accesibilidad desde la referencia" (apta para candidatos tipo
   subconjunto como `Max(C)`). Para `L_a`/`R_a`, que son conjuntos definidos por **incomparabilidad
   espacial** (no por accesibilidad causal hacia abajo), aplicar `down_closure` literalmente podría
   incorporar a `O` elementos que están causalmente por debajo de algún elemento de `L_a` pero que
   **no son ellos mismos spacelike a `a`** — alterando el carácter "lateral" del objeto. **Esto se
   registra como pregunta abierta, no se resuelve aquí**: podría ser más fiel usar la intersección
   literal `L_a∩O` (P1≡P2) en vez de `down_closure(C,L_a)∩O` (P3) para este candidato específico,
   precisamente porque `L_a`/`R_a` ya son conjuntos extensionales completos, no "semillas" a
   expandir. Ninguna decisión se toma aquí; se deja para revisión de comité.

8. **Cuándo produce referencias distintas para completaciones observacionalmente equivalentes:**
   dadas dos completaciones `C_A,C_B∈𝔄_C1(O)` con `C_A|_O=C_B|_O=O` (misma relación inducida), el
   par `{L_a,R_a}` pullback a `O` puede diferir entre ambas exactamente cuando: (i) la regla de
   selección de `a` (aún no cerrada, Parte III) elige elementos distintos concretos en `C_A` vs.
   `C_B` — lo cual es legítimo si la regla puede depender de `H_C` (que difiere entre
   completaciones que comparten `O`); o (ii) incluso con el mismo `a`, la estructura global de
   comparabilidad de `C_A` difiere de la de `C_B` (por tener sectores ocultos distintos), alterando
   el realizador `(L_U,L_V)` y por tanto `Q` mismo. **Esta dependencia del sector oculto es
   precisamente el mecanismo que podría hacer a `E` genuinamente no trivial** — pero solo si la
   regla de selección de `a` es en sí misma order-only, no circular y total (Parte III).

## Auditoría

```text
UNIQUE_MARKER_WELL_DEFINED = ESTABLISHED_DOCUMENTALLY
  (la construcción {L_a,R_a} DADO un `a` fijo está completamente especificada y es exhaustiva,
  §7.4.1 "Resultado positivo 1"; la SELECCIÓN de `a` en sí no es parte de este campo — se
  audita en la Parte III)
UNIQUE_MARKER_ISOMORPHISM_INVARIANT = ESTABLISHED_DOCUMENTALLY
  (afirmado explícitamente por la fuente como order-only/relabel-invariante, §7.6; salvo el
  swap global reconocido, no una prueba formal/Lean independiente)
UNIQUE_MARKER_NONTRIVIALITY = UNRESOLVED
  (ningún par de completaciones ha sido evaluado; la fuente establece la ESTRUCTURA, no un
  testigo de no-trivialidad)
UNIQUE_MARKER_PHYSICAL_INTERPRETATION = PLAUSIBLE_NOT_ESTABLISHED
  (evita la circularidad §7.5, ventaja metodológica real; no establecida como "la" referencia
  de horizonte — token de la fuente es PROVISIONAL)
UNIQUE_MARKER_PULLBACK_COMPATIBILITY = PLAUSIBLE_NOT_ESTABLISHED
  (la familia tipada de comité 013 se aplica formalmente; la elección down-closure vs.
  intersección literal para este objeto lateral específico queda abierta, punto 7 arriba)
```

```text
CASE_|A|=1_STATUS = PARTIAL_DEFINITION_CANDIDATE
```

La construcción **dado un marcador** está cerrada y es copiable; lo que falta es exactamente (a) la
selección order-only de ese marcador (Parte III) y (b) la resolución de la nota de pullback abierta
(punto 7).

---

# Parte III — Selección order-only del marcador `A`

## Candidatos auditados

### A1 — Órbita de automorfismos

```text
CANDIDATE_NAME = Órbita de Aut(C)
FORMAL_RULE = A := órbita de un elemento bajo Aut(C), o unión de órbitas seleccionada
  canónicamente
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = SÍ (por construcción)
UNIQUE = NO — no discrimina en el caso genérico (ver KNOWN_FAILURES)
EXISTS_ON_ALL_ADMISSIBLE_COMPLETIONS = NO en el sentido útil
NONCIRCULAR = SÍ
NONTRIVIAL = NO EVALUABLE (falla antes, por totalidad)
PHYSICAL_INTERPRETATION = ninguna — no selecciona nada por sí sola
KNOWN_FAILURES =
  Comité 010 (mathematician brief, `comite_decision_010.md:81`): "generic finite Poisson
  sprinklings are asymmetric" — Aut(C) es TRIVIAL casi seguramente para un sprinkling continuo
  genérico. Con Aut(C) trivial, TODA órbita es un singleton — "elegir una órbita" no
  discrimina absolutamente nada entre los elementos de C; el problema de selección
  reaparece intacto. Solo sería útil si Aut(C) es no trivial (caso NO genérico, medida cero).
STATUS = REJECTED_NOT_TOTAL
```

### A2 — Clases modulares

```text
CANDIDATE_NAME = Módulo no trivial del grafo de incomparabilidad
FORMAL_RULE = A := un módulo M no trivial de la descomposición modular
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = SÍ (la descomposición modular es canónica, ver Parte IV)
UNIQUE = NO — depende de cuántos módulos no triviales existan
EXISTS_ON_ALL_ADMISSIBLE_COMPLETIONS = NO en el caso genérico
NONCIRCULAR = SÍ
NONTRIVIAL = NO EVALUABLE (falla antes, por totalidad)
PHYSICAL_INTERPRETATION = un módulo se interpreta como "degeneración geométrica" (§7.4.1) —
  no como una localización física de membrana
KNOWN_FAILURES =
  Simétrico al fallo de A1: §7.4.1 marca [PLAUSIBLE, UNVERIFIED] que "2D-order Poisson es
  primo c.s. para N grande" — si esto se confirma, NO HAY módulos no triviales en el caso
  genérico, y este candidato no tiene nada que seleccionar precisamente cuando más se
  necesitaría (el caso típico de un sprinkling continuo). Falla en el mismo régimen que A1,
  por una razón estructuralmente paralela (ambos dependen de una degeneración no genérica).
STATUS = REJECTED_NOT_TOTAL
```

### A3 — Primalidad modular

```text
CANDIDATE_NAME = Selección vía primalidad de la descomposición modular
FORMAL_RULE = (evaluado como candidato de selección de A)
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = N/A — ver más abajo
UNIQUE = N/A
EXISTS_ON_ALL_ADMISSIBLE_COMPLETIONS = N/A
NONCIRCULAR = SÍ
NONTRIVIAL = N/A
PHYSICAL_INTERPRETATION = N/A
KNOWN_FAILURES =
  Este candidato responde una pregunta DISTINTA a la que se le pide (confusión de nivel,
  advertencia explícita del brief de convocatoria): la primalidad modular determina si `Q`
  es único-salvo-swap DADO que ya se construyó sobre todo `P_C` — no selecciona NINGÚN
  marcador `A`. No es un candidato de selección de marcador; es una condición de unicidad de
  una construcción ya distinta (ver Parte IV para su tratamiento propio).
STATUS = REJECTED_NOT_TOTAL
  (no aplicable como regla de selección — falla por no responder la pregunta planteada,
  tratado en detalle en la Parte IV)
```

### A4 — Extremos order-only

```text
CANDIDATE_NAME = Extremos del poset (mínimos/máximos/irreducibles/perfiles de ideal-filtro)
FORMAL_RULE = A := elemento(s) extremales según algún criterio order-only (p. ej. Max(C),
  Min(C), elementos join/meet-irreducibles)
ORDER_ONLY = SÍ (en general)
ISOMORPHISM_INVARIANT = SÍ (en general, para criterios bien definidos)
UNIQUE = DEPENDE del criterio concreto
EXISTS_ON_ALL_ADMISSIBLE_COMPLETIONS = SÍ (Max(C)/Min(C) siempre existen y son no vacíos para
  C finito no vacío)
NONCIRCULAR = SÍ (en general)
NONTRIVIAL = NO EVALUADO
PHYSICAL_INTERPRETATION = depende del extremo elegido
KNOWN_FAILURES =
  La instanciación más obvia y ya disponible en código, `A:=Max(C)`, es FÍSICAMENTE
  INAPROPIADA: `Max(C)` es la "pared de muestreo" (borde superior de la caja,
  `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §2 — "el único 'futuro inalcanzable'
  disponible es el borde superior de la caja"), no una localización a media altura donde se
  espera el horizonte. Usar `Max(C)` como marcador reproduciría exactamente el artefacto de
  pared que la propia nota fuente distingue cuidadosamente del horizonte (tabla §2). Además,
  `Max(C)` es el mismo objeto ya usado por el candidato `R=Max(C)` rechazado
  (`REJECTED_TRIVIAL`) por un motivo distinto (trivialización del interfaz) — reusarlo aquí
  no hereda esa trivialidad automáticamente (el mecanismo de Q es distinto), pero sí hereda
  el defecto físico de "pared, no horizonte".
STATUS = RECOMMENDED_FOR_FURTHER_STUDY
  (la CATEGORÍA general de extremos order-only sigue siendo válida; la instanciación
  concreta `Max(C)` queda explícitamente descartada por razón física, no formal)
```

### A5 — Firma relacional

```text
CANDIDATE_NAME = Selección por firma invariante (perfiles de intervalo, incomparabilidad,
  C_k, ordering fraction)
FORMAL_RULE = A := elemento(s) que alcanzan un valor distinguido de un invariante order-only
  ya reconocido en el repo (p. ej. abundancias de intervalo C_k, fracción de orden, perfil
  de incomparabilidad)
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = SÍ (los invariantes citados son, por construcción, invariantes de
  isomorfismo — Benincasa-Dowker C_k, ordering fraction/Myrheim-Meyer, ambos citados en
  comité 010 mathematician brief)
UNIQUE = DEPENDE del invariante y de si hay empates
EXISTS_ON_ALL_ADMISSIBLE_COMPLETIONS = PLAUSIBLE (los invariantes están definidos para todo
  poset finito; existencia de un extremo bien definido no garantiza unicidad — empates
  posibles, ver Parte V)
NONCIRCULAR = CONDICIONAL — ver KNOWN_FAILURES
NONTRIVIAL = NO EVALUADO
PHYSICAL_INTERPRETATION = PLAUSIBLE — invariantes con respaldo en la literatura citada
  (Benincasa-Dowker 2010, Myrheim-Meyer/Surya LRR 2019 §4, ambos CONFIRMED en el literature
  verdict de comité 010)
KNOWN_FAILURES =
  RIESGO DE CIRCULARIDAD si el invariante elegido es el volumen futuro `O(i)=|future(i)|` —
  esta es EXACTAMENTE la cantidad que el estimador sellado (estimator-v2, prereg-002 PASS)
  usa para su señal bimodal. Usar `O(i)` para seleccionar el marcador `A` Y usar después una
  asimetría derivada de `A` para evaluar identificabilidad reintroduciría el riesgo de
  circularidad que §7.5 prohíbe explícitamente ("la asimetría debe leerse de la estructura
  de enlaces... nunca la accesibilidad futura que el estadístico luego mide"). Otros
  invariantes (C_k, ordering fraction, perfil de incomparabilidad) NO son la cantidad que
  mide el PASS y por tanto tienen riesgo de circularidad menor — pero esto no ha sido
  verificado formalmente para ninguno de ellos.
STATUS = RECOMMENDED_FOR_FURTHER_STUDY
  (prometedor; requiere excluir explícitamente O(i)/volumen-futuro como firma de selección,
  y verificar ausencia de circularidad para cualquier invariante concreto que se proponga)
```

### A6 — Marcador multivaluado

```text
CANDIDATE_NAME = Familia admisible de marcadores + agregación
FORMAL_RULE = 𝔄(C) := {A⊆C : A satisface un criterio de admisibilidad order-only aún no
  especificado por ningún documento};
  R_Q(C) definida como una FAMILIA {Q(C,A) : A∈𝔄(C)}, o una agregación (intersección, unión,
  clase de equivalencia) sobre ella
ORDER_ONLY = SÍ (si el criterio de admisibilidad de 𝔄(C) lo es — no especificado aún)
ISOMORPHISM_INVARIANT = PLAUSIBLE — una familia definida por un criterio invariante, agregada
  por una función simétrica (intersección/unión/mayoría), es automáticamente covariante bajo
  isomorfismos; ESTO ES UNA VENTAJA TÉCNICA REAL de esta forma frente a A1-A5
UNIQUE = NO REQUIERE serlo — es exactamente su punto: evita forzar una elección única
EXISTS_ON_ALL_ADMISSIBLE_COMPLETIONS = SÍ trivialmente (todo C finito no vacío tiene al menos
  los marcadores de un solo elemento {x}, x∈C, como candidatos base de 𝔄(C))
NONCIRCULAR = SÍ, si el criterio de admisibilidad de 𝔄(C) no usa el output del estimador ni
  la identidad A/B
NONTRIVIAL = UNRESOLVED — depende enteramente de qué función de agregación se especifique;
  una intersección sobre el conjunto entero de `a∈C` podría colapsar trivialmente a ∅ o a todo C
PHYSICAL_INTERPRETATION = PLAUSIBLE — "todas las membranas candidatas admisibles, agregadas
  robustamente" es una lectura física razonable, pero no está desarrollada en ningún
  documento existente
KNOWN_FAILURES =
  Ninguna refutación — es la forma MENOS atacada, precisamente porque convierte "elegir UN A"
  en "elegir el CRITERIO de admisibilidad de la familia 𝔄(C) y la función de agregación",
  que son preguntas nuevas, no cerradas por ningún documento, pero potencialmente más
  tratables (ver Parte VI).
STATUS = RECOMMENDED_FOR_FURTHER_STUDY
  (la dirección más prometedora identificada en esta sesión; no cerrada — el criterio de
  admisibilidad y la agregación quedan por especificar)
```

**Ningún candidato recibe `RECOMMENDED_FOR_CLOSED_CANDIDATE`**: A1 y A2 fallan totalidad de forma
genérica (por razones estructuralmente paralelas — ambas dependen de una degeneración de medida
cero bajo sprinkling Poisson continuo); A3 no responde la pregunta planteada; A4 tiene una
instanciación obvia (`Max(C)`) físicamente descartada, aunque la categoría general queda abierta;
A5 es prometedor pero condicionado a evitar la circularidad de `O(i)`; A6 es la dirección más
robusta pero no especifica todavía su criterio ni su agregación. Ninguno cierra simultáneamente
existencia, invarianza y no-circularidad de forma verificada.

---

# Parte IV — Primalidad modular

```text
MODULAR_DECOMPOSITION_AVAILABLE = SÍ, en principio (teoría de grafos estándar, Gallai 1967,
  aplicable al grafo de comparabilidad de cualquier orden finito), NO IMPLEMENTADA en este
  proyecto (verificado: ningún archivo `.py` calcula descomposición modular)

MODULAR_DECOMPOSITION_CANONICAL = SÍ para la descomposición en sí (teorema clásico de Gallai:
  todo grafo tiene un árbol de descomposición modular único). Lo NO establecido es si esa
  descomposición es TRIVIAL (grafo primo, sin módulos propios no triviales) para los causal
  sets de este proyecto — eso es la afirmación [PLAUSIBLE, UNVERIFIED] de §7.4.1, no un
  hecho probado.

MODULAR_PRIMALITY_SELECTS_A = NO
  Distinción explícita exigida por el brief: la primalidad modular es una propiedad de
  UNICIDAD de la construcción de `Q` sobre el `P_C` completo, dado que `Q` ya se construyó — NO es
  un mecanismo de SELECCIÓN de qué antichain `A` marca la membrana. Son preguntas
  ortogonales. Ningún documento del repositorio conecta primalidad con selección de
  marcador; esta sesión no inventa esa conexión.

MODULAR_PRIMALITY_TOTAL = NO / UNRESOLVED
  Incluso limitada a su propia pregunta (unicidad de Q), la primalidad no es total: en el
  caso no primo (módulos no triviales), §7.4.1 solo APUNTA a una posible regla de desempate
  ("orientar el módulo por su propio sub-conjugado, recursivamente") sin desarrollarla ni
  cerrarla. El caso no-genérico permanece sin regla.

MODULAR_PRIMALITY_ISOMORPHISM_INVARIANT = SÍ para la descomposición modular en sí (invariante
  de isomorfismo estándar); esto NO transfiere a una garantía de invarianza para la selección
  de `A`, porque la primalidad no selecciona `A` (ver arriba).

MODULAR_PRIMALITY_PHYSICAL_MEANING =
  Un módulo no trivial corresponde a una "degeneración geométrica no genérica bajo sprinkling
  Poisson continuo" (§7.4.1) — físicamente, una coincidencia de medida cero. Si la primalidad
  casi-segura se confirmara, el caso problemático (Q no único) sería físicamente
  despreciable para el régimen de interés (sprinkling continuo genérico) — pero esto sigue
  siendo una plausibilidad, no un teorema, y en cualquier caso no ayuda a resolver CUÁL `A`
  usar, solo si `Q` (dado algún `A`/losa ya fijados) es único.
```

**Conclusión de esta parte:** la primalidad modular **reduce la incertidumbre sobre la unicidad de
`Q`**, no reduce el espacio de candidatos para `A`. Ambas preguntas deben tratarse por separado; no
se confunden en este documento.

---

# Parte V — Reglas de desempate

**Nota de alcance:** ningún candidato de la Parte III llegó a producir una lista corta de
marcadores empatados que necesite desempate — el problema actual es la ausencia de CUALQUIER regla
cerrada, no un empate entre varias reglas cerradas. Esta parte audita estrategias de desempate
**disponibles para cuando** (si acaso) una lista corta de candidatos sobreviva un futuro criterio de
admisibilidad (p. ej. dentro de la Parte VI, A6).

1. **Desempate lexicográfico por invariantes estructurales** — comparar candidatos empatados por
   una tupla de invariantes order-only (p. ej. `(|down-set|, |up-set|, grado de
   incomparabilidad, ...)`) en orden lexicográfico. Ventaja: computable, order-only. Fallo: en
   configuraciones exactamente simétricas (bajo un automorfismo no trivial), cada uno de los invariantes
   estructurales pueden coincidir entre elementos de una misma órbita — el desempate lexicográfico
   no puede entonces romper el empate y debe recurrir a otra estrategia (p. ej. la 2 siguiente).
   **Prohibido explícitamente por el brief:** ordenar por identificador/índice de elemento — eso
   rompería relabel-invarianza (Guard-v). Este documento no propone eso en ningún punto.
2. **Elegir la órbita completa en vez de un elemento** — si varios candidatos empatan y forman una
   única órbita de automorfismo, tratar la ÓRBITA como el marcador canónico (multivaluado),
   evitando romper la simetría artificialmente. Compatible directamente con A6.
3. **Agregación sobre todos los marcadores equivalentes** — combinar (intersección/unión) los
   objetos `Q(C,A)` de todos los candidatos empatados en un solo objeto agregado. Efecto sobre el
   pullback: el pullback tipado de comité 013 se aplicaría al objeto agregado resultante, no a cada
   candidato por separado — requiere especificar la agregación ANTES del pullback.
4. **Declaración explícita de referencia multivaluada** — no forzar un colapso a un único
   marcador; `R_Q(C)` es, por diseño, la familia entera (adopción directa de A6). Evita el problema
   de desempate por completo, al precio de que `E-set`/`E-element` deban generalizarse a
   comparación de familias, no de objetos singulares (ver Parte VII).
5. **Restricción del dominio a completaciones con marcador canónico** — excluir del dominio de
   `R_Q` cualquier completación donde el criterio de selección no produzca un único candidato (o
   una única órbita), aceptando una regla parcial pero limpia sobre un subconjunto de `𝔄_C1(O)`.

**Evaluación:** las estrategias 4 y 5 son las más robustas porque **evitan** el problema de
desempate estructuralmente, en vez de resolverlo caso por caso. La estrategia 1 es útil solo como
herramienta secundaria dentro de 4/5, nunca como solución única (falla en simetría exacta). Ninguna
estrategia se adopta aquí de forma definitiva — se recomienda 4 o 5 como dirección preferente para
la Parte VI.

---

# Parte VI — Propuesta de regla cerrada candidata

Dado que ningún candidato de marcador (Parte III) alcanzó `RECOMMENDED_FOR_CLOSED_CANDIDATE`, **no
se fuerza una fórmula única**. Se registra la dirección mejor respaldada como propuesta de
DESARROLLO, no de adopción:

```text
PROPOSED_Q_RULE_STATUS = BLOCKED

PROPOSED_Q_RULE_NAME =
  Candidato de dirección: "familia agregada / dominio restringido" (combinación de A6 con la
  forma "Dominio restringido" del brief) — NO CERRADO.

PROPOSED_Q_RULE_FORMAL_DEFINITION =
  Esquema: R_Q : 𝔄_Q(O) → ℛ, donde 𝔄_Q(O) ⊆ 𝔄_C1(O) contiene las completaciones para las que
  𝔄(C) (familia de marcadores admisibles, criterio aún no especificado — Parte III, A6) es no vacía y su
  agregación Agg_{A∈𝔄(C)} Q(C,A) está bien definida y es no trivial. FALTA ESPECIFICAR: (i) el
  criterio de admisibilidad para A∈𝔄(C) — candidato preferente: firma relacional (A5) EXCLUYENDO
  el volumen futuro O(i); (ii) la función de agregación Agg (intersección/unión/clase de
  equivalencia); (iii) la extensión exacta de N(A) (vecindad spacelike, Parte I).

PROPOSED_Q_RULE_DOMAIN =
  𝔄_Q(O) ⊆ 𝔄_C1(O) con dim_DM(C)≤2 (bajo la hipótesis condicional de la Prop. 7.3) — subconjunto
  exacto NO especificado (depende del criterio de admisibilidad pendiente).

PROPOSED_Q_RULE_CODOMAIN =
  Familia de tripartición/biparticiones {Q(C,A) : A∈𝔄(C)}, o su agregado — objeto de tipo
  partición-etiquetada o familia de tales, distinto del tipo subconjunto de candidato 1.

PROPOSED_Q_RULE_TOTALITY = NO ESTABLECIDA (depende del criterio de admisibilidad pendiente)
PROPOSED_Q_RULE_ISOMORPHISM_INVARIANCE = PLAUSIBLE (la forma agregada sobre una familia
  invariante es covariante por construcción; el criterio de admisibilidad concreto aún no
  especificado podría o no preservar esto según cómo se defina)
PROPOSED_Q_RULE_NONCIRCULARITY = CONDICIONAL (depende de excluir O(i) del criterio de
  admisibilidad, per A5 KNOWN_FAILURES)
PROPOSED_Q_RULE_NONTRIVIALITY = UNRESOLVED
PROPOSED_Q_RULE_PHYSICAL_INTERPRETATION = PROVISIONAL (hereda la interpretación aspiracional de
  Q — evitar circularidad futuro/lateral — sin establecer todavía correspondencia con el
  horizonte real)
PROPOSED_Q_RULE_PULLBACK =
  Familia tipada de comité 013 aplicable formalmente (componente a componente); pregunta abierta
  no resuelta sobre down-closure vs. intersección literal para objetos definidos por
  incomparabilidad espacial (Parte II, punto 7).
```

**Bloqueo mínimo exacto:** no existe en ningún documento del proyecto un criterio de admisibilidad
order-only, total, no circular e invariante bajo isomorfismo para la familia `𝔄(C)`, ni una función
de agregación especificada sobre ella. Cerrar esto es trabajo de especificación nuevo, no una
lectura de material existente — exactamente lo que `NEXT_AUTHORIZED_ACTION` de esta sesión autoriza
para el futuro, no lo que esta sesión cierra.

---

# Parte VII — Compatibilidad con E y C1

```text
1. R_Q(C) definida para toda completación del dominio declarado:
   NO — bloqueada por la ausencia de criterio de admisibilidad de marcador (mismo bloqueo de
   Parte VI).

2. Pullback produce objetos comparables sobre el mismo O:
   SÍ, condicionalmente — la familia tipada de comité 013 (componente a componente) aplica al
   tipo partición de Q; queda abierta la pregunta down-closure vs. intersección literal
   (Parte II punto 7), sin afectar la comparabilidad de tipo (ambas opciones producen objetos
   del mismo tipo entre C_A y C_B).

3. E-set bien definido:
   SÍ, estructuralmente (comité 013 D4: desigualdad de particiones inducidas, ya generalizada
   para objetos tipo estructura) — no evaluable hasta cerrar R_Q.

4. E-element aplicable cuando el codominio lo permite:
   SÍ — para un codominio de partición finita, un testigo puntual (elemento cuya clase difiere
   entre PB_O(R_Q(C_A)) y PB_O(R_Q(C_B))) es la forma constructiva equivalente, igual que en
   el candidato BCE original.

5. Sin acceso a metadatos ocultos prohibidos:
   SÍ — la construcción de Q usa solo la relación de orden ≺ de C (las coordenadas auxiliares
   U,V son, en palabras de la propia fuente, "sólo para razonar, NO entran en nada", §7.4.1);
   ningún candidato de marcador auditado en la Parte III accede a r, t*, ni a etiquetas del
   generador.

6. Independencia de nombres de elementos:
   SÍ — toda la construcción (Q, tripartición, candidatos A1-A6 salvo el descarte explícito de
   Max(C) por razón FÍSICA, no de nombres) es relabel-invariante por diseño; ningún candidato
   propone ordenar por índice/etiqueta.

7. Suficiencia de groundedness G1 frente a perturbación por ocultos desconectados:
   PARCIAL — G1 (comité 013) impide que un oculto TOTALMENTE desconectado de O participe en
   pullbacks locales, pero Q depende del realizador GLOBAL (L_U,L_V) de TODA la completación
   C, no solo de su relación con O. Un oculto que satisface G1 (tiene alguna relación con
   algún x∈O) podría aun así, a través de sus relaciones con OTROS elementos ocultos no
   directamente vinculados a O, alterar la estructura de incomparabilidad global y por tanto
   Q — un modo de perturbación que G1, tal como está formulado, no cierra completamente. Esto
   NO fue identificado por comité 013 en esta forma específica; se registra aquí como
   observación nueva, no como una falla de la decisión de comité 013 sino como un matiz
   adicional relevante específicamente para candidatos de tipo Q (no para candidatos de tipo
   subconjunto local, donde G1 sí basta).

8. G3 necesario solo para 𝔄_Schw:
   Confirmado, sin cambio — G3 (futuro + no-retorno) responde a una hipótesis física distinta
   (trampeo/no-retorno), ortogonal al mecanismo de Q. No es necesario para que Q funcione
   formalmente; sigue reservado para 𝔄_Schw, no readoptado aquí.
```

```text
Q_COMPATIBLE_WITH_G1 = PARTIALLY_SUFFICIENT
Q_REQUIRES_G3 = NO
Q_PULLBACK_TYPED = YES_WITH_OPEN_SUBQUESTION
Q_E_SET_EVALUABLE = NOT_YET (bloqueado por selección de marcador)
Q_E_ELEMENT_EVALUABLE = NOT_YET (mismo bloqueo)
Q_OBSERVATIONAL_EQUIVALENCE_PRESERVED = YES (sin cambio respecto a comité 013)
```

---

# Parte VIII — Gate para la siguiente fase

```text
GATE_DECISION = Q_RULE_REQUIRES_FORMAL_DEFINITION_WORK
```

No se autoriza Alloy 003 (ninguna modalidad): el marcador, la agregación y el criterio de
admisibilidad siguen móviles. Cualquier auditoría de casos pequeños (p. ej. verificar A5/A6 sobre
posets de juguete escritos a mano, sin sprinkling) queda explícitamente para una **fase posterior**,
no ejecutada ahora. Lean no se propone en ningún punto — no hay todavía una definición cerrada que
formalizar; usarlo ahora sería exactamente el uso prohibido de Lean como sustituto de una definición
física ausente.

---

## Bloque normativo

```text
DOCUMENT_ID = PR003_Q_REFERENCE_RULE_DEVELOPMENT

SOURCE_Q_STATUS =
  PARCIALMENTE ESTABLECIDO: construcción de Q (dado marcador+realizador, condicional a Prop.
  7.3) cerrada y order-only; bipartición exhaustiva REFUTADA para |A|≥2; tripartición
  sobrevive como objeto canónico PROVISIONAL; caso |A|=1 cerrado dado un marcador fijo.
BIPARTITION_STATUS = REFUTED_FOR_|A|>=2
TRIPARTITION_STATUS = PROVISIONAL
TWO_FACE_LEMMA_STATUS = OPEN (III_PENDING_TWO_FACE_LEMMA)

CASE_|A|=1_STATUS = PARTIAL_DEFINITION_CANDIDATE

MARKER_SELECTION_STATUS = BLOCKED
MARKER_SELECTION_RECOMMENDED_RULE =
  NINGUNO CERRADO. Dirección recomendada para desarrollo futuro: A6 (familia admisible +
  agregación) combinada con A5 (firma relacional, excluyendo volumen futuro O(i) por riesgo
  de circularidad) y forma de dominio restringido.
MARKER_SELECTION_ISOMORPHISM_STATUS = UNRESOLVED (A1/A2 fallan por totalidad, no por
  invarianza; A6 es plausiblemente invariante pero su agregación no está especificada)
MARKER_SELECTION_TOTALITY_STATUS =
  FAILS_GENERICALLY_FOR_A1_A2 (Aut(C) trivial y descomposición modular prima casi seguramente
  bajo sprinkling Poisson continuo — mismo mecanismo de fallo para ambos); UNRESOLVED para
  A4 (categoría general)/A5/A6 (instanciación concreta pendiente)

MODULAR_PRIMALITY_STATUS =
  AVAILABLE_BUT_DOES_NOT_SELECT_A (descomposición canónica en principio, no implementada;
  primalidad genérica [PLAUSIBLE, UNVERIFIED]; responde unicidad de Q, no selección de A)
TIE_BREAK_STATUS =
  NO_SHORTLIST_YET_TO_BREAK (ningún candidato cerrado produjo empates que desempatar);
  estrategia recomendada si surgiera: declaración multivaluada explícita (A6) o restricción
  de dominio, nunca orden lexicográfico sobre índices de elemento

PROPOSED_Q_RULE_STATUS = BLOCKED
PROPOSED_Q_RULE_NAME =
  Familia agregada / dominio restringido (A6 + dominio restringido) — dirección de
  desarrollo, no candidato cerrado
PROPOSED_Q_RULE_FORMAL_DEFINITION =
  R_Q : 𝔄_Q(O) → ℛ, 𝔄_Q(O)={C∈𝔄_C1(O) : dim_DM(C)≤2 ∧ 𝔄(C)≠∅ ∧ Agg_{A∈𝔄(C)}Q(C,A) bien
  definida y no trivial} — criterio de admisibilidad de 𝔄(C) y función Agg SIN ESPECIFICAR
PROPOSED_Q_RULE_DOMAIN =
  Subconjunto de 𝔄_C1(O) con dim_DM≤2 (condicional a Prop. 7.3); extensión exacta pendiente
PROPOSED_Q_RULE_CODOMAIN =
  Familia de biparticiones/triparticiones {Q(C,A)}, o su agregado — tipo partición-etiquetada
PROPOSED_Q_RULE_PHYSICAL_STATUS = PROVISIONAL

Q_PULLBACK_STATUS = TYPED_FAMILY_APPLIES_WITH_OPEN_SUBQUESTION
  (componente a componente per comité 013; down-closure vs. intersección literal para
  objetos definidos por incomparabilidad espacial queda sin resolver)
Q_E_EVALUABILITY_STATUS = NOT_YET_EVALUABLE_PENDING_MARKER_SELECTION_CLOSURE

ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED
PHYSICAL_IDENTIFIABILITY_STATUS = NOT_ESTABLISHED

NEXT_REVIEW_REQUIRED =
  Revisión de comité de: (i) el argumento de rechazo de A1/A2 (degeneración genérica de
  medida cero, mecanismo paralelo para ambos); (ii) la formalización del caso |A|=1; (iii)
  si priorizar A5 (con salvaguarda anti-circularidad explícita) o A6 (familia+agregación)
  como dirección principal de desarrollo.
NEXT_AUTHORIZED_ACTION =
  Especificación escrita únicamente (sin código, sin Alloy, sin Lean, sin ejecución):
  proponer y definir formalmente un criterio de admisibilidad order-only para 𝔄(C) (A6)
  y/o una firma estructural no circular (A5) que excluya explícitamente el volumen futuro
  O(i); resolver por escrito la pregunta abierta de pullback (down-closure vs. intersección
  literal) para objetos de tipo lateral/espacial.
NEXT_FORBIDDEN_ACTIONS =
  Alloy 003 en cualquier modalidad |
  formalización Lean de una regla todavía no cerrada |
  usar Max(C) como marcador de Q (conflación pared-de-muestreo/horizonte, razón física, no
  formal) |
  usar el volumen futuro O(i) como firma de selección sin resolver el riesgo de
  circularidad señalado |
  desempate lexicográfico sobre índices/etiquetas de elemento |
  tratar A5/A6 como adoptadas en vez de en estudio |
  reabrir GROUNDEDNESS_DECISION=G1 o G3=RECOMMENDED_FOR_SCHW_ONLY |
  commit o push de este documento sin autorización explícita del PI

OVERALL_DEVELOPMENT_STATUS = Q_REQUIRES_FURTHER_DEFINITION
```
