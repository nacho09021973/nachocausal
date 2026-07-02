# PR-003 — Candidato cerrado (b)(c)(e) para la clase C1

> Autorizado por `docs/comite/comite_decision_012_c1-admissible-completion-class.md`,
> `NEXT_AUTHORIZED_ACTION` (bloque normativo): redactar por escrito, sin ejecutar búsquedas ni
> formalizaciones, un candidato matemáticamente cerrado para las cláusulas (b), (c) y (e) de C1.
> **Sesión exclusivamente de especificación matemática y auditoría lógica.** No se ejecutó ninguna
> simulación, sprinkling, búsqueda de contraejemplos, prueba Alloy, formalización Lean, análisis
> estadístico ni código de producción. Sin commit ni push. No se reabren ni reinterpretan las
> decisiones de comité 012.
>
> Preservado sin cambios: `CONVEXITY_REQUIREMENT = MANDATORY_FOR_C1`;
> `ORDER_DIMENSION_LE_2_REQUIREMENT = REQUIRED_ONLY_FOR_A_NAMED_SUBCLASS` (subclase `𝔄_Schw`);
> `ALLOY_002_LOGICAL_WITNESS = PRESENT`; `ALLOY_002_PHYSICAL_WITNESS = NOT_ESTABLISHED`;
> `ALLOY_002_C1_WITNESS_STATUS = INVALID_UNDER_CONVEXITY_REQUIREMENT`;
> `BOUNDARY_BRACKET_STATUS = FAILED_BASELINE_UNDER_PRECOMMITTED_DENSITY_COVERAGE_CRITERION`;
> `BOUNDARY_BRACKET_ALLOWED_USE = DIAGNOSTIC_COMPARATOR`.

---

## 0. Fuentes leídas íntegramente esta sesión

| Archivo | Uso |
|:---|:---|
| `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` (R4) | Cinco cláusulas §3, obligaciones físicas §4, tabla de distinciones §2 |
| `dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md` (R3) | Fórmula `cov_honest`, veredicto S3 |
| `docs/comite/comite_decision_011_patch-ensemble-architecture.md` | Origen de los cinco términos arquitectónicos, BLOCK-1..5 |
| `docs/comite/comite_decision_012_c1-admissible-completion-class.md` | D1–D5, jerarquía de niveles §3, tratamiento Alloy 002 / boundary-bracket |
| `docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md` | Definiciones originales de los cinco términos: clase de subposet observado, clase de completación admisible 𝔄, regla de referencia inducida, regla de pullback, predicado de incompatibilidad (mathematical-logic brief, §4) |
| `docs/alloy/alloy_verification_002_completion-nonidentifiability-interface.md` | Traza literal del testigo Alloy 002 |
| `dev/alloy/product_order_check_alloy002_witness_note.md` | Chequeo ejecutado de convexidad + `dim_DM≤2` sobre el testigo, veredicto `PHYSICAL_LAYER_EMPTY_EVIDENCE` |
| `nachocausal/c1_selector.py`, `nachocausal/selection_guard.py` | Único candidato de referencia (`R=Max(C)`) y único mecanismo de invarianza por reetiquetado (Guard-v) |
| `dev/PR003_C1_RELATIONAL_SPEC.md` | Definición de `H[C;R]`, `ASYMMETRY_SCORE`/`PERSISTENCE_THRESHOLD`/`BULK_CONTROL`/`C1_PROMOTION` todos `OPEN` |

No se generó ningún archivo de evidencia nuevo. No se tocó `thresholds.py`. No se modificó ningún selector ni test.

---

# Parte I — Notación común

| Símbolo | Objeto | Tipo |
|:---|:---|:---|
| `O` | Poset causal finito observado (`past_matrix` booleana, orden estricto `<_O`, irreflexivo y transitivamente cerrado) | Poset finito |
| `C` | Completación candidata, `C ⊇ O` como conjunto subyacente, finito | Poset finito |
| `H_C = C \ O` | Sector oculto de `C` | Subconjunto de elementos |
| `ι_C : O ↪ C` | Inclusión identificada de elementos (misma etiqueta/entero, no solo isomorfismo) | Inclusión literal de carriers |
| `R(C)` | Objeto de referencia inducido por la regla (c) sobre la completación | Depende de la regla: subconjunto de `C`, o partición de `C`, o conjunto de pares (ver Parte III) |
| `PB_O(R(C))` | Pullback de la referencia al dominio observado (regla (d)) | Objeto del mismo tipo que `R(C)` pero restringido a `O` |
| `𝔄(O)` | Clase de completaciones C1 admisibles de `O` (genérico; en este documento se instancia en dos clases concretas, `𝔄_C1(O)` y `𝔄_Schw(O)`) | Familia de posets finitos |

**Orden estricto vs. no estricto.** Todo el aparato del proyecto usa `<` estricto (matriz booleana
irreflexiva, transitivamente cerrada — `witness_note.md` §3 punto 2: "Valid strict partial order —
irreflexive and transitively closed"). Este documento **no introduce** una relación `≤` distinta;
donde el brief de convocatoria escribe "reflexividad para `≤`", se traduce aquí como
**irreflexividad de `<_C`** (la formulación equivalente y correcta bajo la convención ya vigente en
el repo). No se define ningún `≤_C` adicional.

**Maximalidad global vs. relativa.** `Max(C) = {x∈C : ¬∃y∈C, x<_C y}` es maximalidad **global** en
toda la completación — el objeto que `c1_selector.maximal_elements` calcula
(`nachocausal/c1_selector.py:18-25`) y que el predicado `isInterface` de Alloy 002 codifica
elemento a elemento (`no ((e→Element) & c.lt)` ⟺ `e∈Max(C)`; comité 010 mathematician brief,
`comite_decision_010.md:73`: *"isInterface[c,e] ⇔ e∈Obs ∧ e is maximal in c… equivalently
R=Max(C)"*). Es distinto de la maximalidad **relativa** que produce `c1_selector.c1_selector`:
`accessible = down_closure(C, reference)`, `black_region = C \ accessible`, y el interfaz
`H[C;R] = {(x,y) : x∈black_region, y∈accessible, x covers y}` (`c1_selector.py:56-75`;
`dev/PR003_C1_RELATIONAL_SPEC.md:60`). Un elemento puede ser maximal en `black_region` (relativo)
sin ser maximal en `C` (global).

**Conjunto de maximales vs. interfaz física.** `Max(C)` es un subconjunto de elementos. `H[C;R]` es
un conjunto de **pares ordenados de cobertura** (aristas, no elementos) — un objeto de tipo
distinto. No se identifican en este documento.

**Igualdad literal vs. isomorfismo.** La cláusula (b1) exige `∀x,y∈O: x<_C y ⟺ x<_O y` bajo la
inclusión fija `ι_C` — igualdad **literal** de la relación inducida sobre las mismas etiquetas, no
solo la existencia de algún isomorfismo de orden entre `O` y algún subposet de `C`. Esta distinción
es la que R4 §2 marca como obligatoria (tabla de distinciones, fila "Misma relación inducida sobre
el observado").

---

# Parte II — Cláusula (b): clase admisible `𝔄(O)`

## Núcleo obligatorio (ya decidido por comité 012, D1–D2 — no se reabre)

### B1. Preservación literal del observado

```
∀x,y∈O:  x <_C y  ⟺  x <_O y      (bajo ι_C)
```

Subposet inducido **literal** mediante la inclusión identificada — no basta una copia isomorfa
(comité 012 D1, fila 1: `MANDATORY`, confianza ALTA).

### B2. Orden causal

`<_C` es un orden parcial estricto válido: irreflexivo y transitivamente cerrado (traducción de
"antisimetría + transitividad" a la convención estricta del repo — ver Parte I). Ya verificado
ejecutablemente para ambas completaciones del testigo Alloy 002
(`product_order_check_alloy002_witness_note.md` §4, filas "Valid strict partial order: ✓✓"; comité
012 D1 fila 2: `MANDATORY`, confianza ALTA).

### B3. Convexidad causal del observado

```
∀a,b∈O, ∀h∈H_C:  a <_C h <_C b  ⟹  ⊥
```

Comité 012 (D1 fila 3, D2) identifica esta condición con "ausencia de elementos ocultos
causalmente inadmisibles" y con "restricciones de localización de elementos ocultos" — **misma
obligación, tres redacciones**, no tres obligaciones independientes (nota de disciplina de R4 §4,
confirmada por comité 012 D1 nota explícita). Esta identificación es una decisión de comité 012, no
una equivalencia matemática derivada aquí; se preserva sin reabrir. `CONVEXITY_REQUIREMENT =
MANDATORY_FOR_C1` (comité 012 D2, preservado sin cambios).

### Finitud de `C`

Presupuesta sin excepción en R4 §1 ("poset causal finito"), en el mathematician brief de comité
010 (decidibilidad en tiempo polinomial "from the order matrix", `comite_decision_010.md:72`) y en
todo el aparato de Alloy (scope `exactly 4 Element`). **Este ítem no fue votado explícitamente por
comité 012** — se propone aquí `INCLUDED_IN_MINIMAL_C1` por no estar nunca en disputa en ningún
documento existente; queda marcado para confirmación explícita en la revisión de este candidato,
no como decisión ya comprometida por un comité.

## Componentes no cerrados por comité 012 — evaluados por separado

| Componente | Etiqueta | Justificación |
|:---|:---|:---|
| Número de elementos ocultos (`|H_C|`) | `EXCLUDED_FROM_MINIMAL_C1` | Comité 012 D1: `DEFERRED` — "ni se adopta ni se rechaza; no probado en ninguna dirección". Para una clase **mínima**, ausencia de restricción decidida = ausencia de la condición en la definición. Esto **no** afirma que la cardinalidad sea irrelevante — solo que ninguna cota ha sido adoptada. |
| Finitud de `C` | `INCLUDED_IN_MINIMAL_C1` | Ver arriba — nunca disputada, propuesta aquí por primera vez explícitamente, pendiente de confirmación. |
| Localización temporal del sector oculto | (subsumida en B3) | Idéntica a convexidad por decisión de comité 012 (D1 fila "Restricciones de localización" = `MANDATORY` = convexidad). No se introduce como cláusula separada — sería doble conteo. |
| Que cada oculto esté relacionado con algún observado ("groundedness") | `UNRESOLVED_BLOCKER` | **Ningún comité ha evaluado esta condición.** No aparece en la tabla D1 de comité 012 ni en R4 §4. El mathematician brief de comité 010 describe la construcción de Alloy 002 como agregando "**un elemento no fundamentado** [ungrounded]" (`comite_decision_010.md:77`, cita directa del caveat 1) — término sugerente pero nunca promovido a obligación. Se registra aquí como bloqueo explícito nuevo, no como decisión. |
| Compatibilidad con región de Schwarzschild | `DEFERRED_TO_PHYSICAL_SUBCLASS` | Comité 012 D1: `DEFERRED`, sin predicado ejecutable sobre completaciones arbitrarias. Pertenece a `𝔄_Schw` (ver abajo), no al núcleo mínimo. |
| Manifoldlikeness | `DEFERRED_TO_PHYSICAL_SUBCLASS` | Idéntico razonamiento; comité 012 D1: `DEFERRED`. |
| Origen mediante sprinkling | `OPTIONAL_DIAGNOSTIC` | Comité 012 D1: `OPTIONAL_DIAGNOSTIC` literal — preservado. |
| Dimensión de orden ≤ 2 (`dim_DM≤2`) | `DEFERRED_TO_PHYSICAL_SUBCLASS` | Comité 012 D2: `REQUIRED_ONLY_FOR_A_NAMED_SUBCLASS` (`𝔄_Schw`). No se deduce obligatoria para el núcleo mínimo por el hecho de que el testigo disponible sea 2D — instrucción explícita preservada. |

## Dos clases

### `𝔄_C1(O)` — clase causal mínima

```
𝔄_C1(O) := { C : C ⊇ O finito,  (B1) ∧ (B2) ∧ (B3) }
```

Sin restricción sobre `|H_C|`. La condición de "groundedness" queda **explícitamente fuera** de
esta definición por ahora — ni incluida ni excluida por una decisión adjudicada; es un
`UNRESOLVED_BLOCKER` (ver tabla arriba), no una premisa silenciosa.

### `𝔄_Schw(O) ⊆ 𝔄_C1(O)` — subclase física nombrada

```
𝔄_Schw(O) := { C ∈ 𝔄_C1(O) :
                 C es producido (o es literalmente reproducible) por la familia de
                 generadores 1+1D Eddington–Finkelstein sellada (generator.py,
                 thresholds.py:37-43, R_S=0.5, M=0.25) }
```

Esta es una definición **por procedencia**, no por un predicado geométrico intrínseco evaluable
sobre una completación combinatoria arbitraria — exactamente porque comité 012 (D1, filas
Schwarzschild-compat/manifoldlikeness) constató que ningún predicado así existe hoy, y que
definirlo usando `r=2M` directamente sería fuga de ground truth (riesgo 1, comité 010 §8, citado en
comité 012 D1). Se espera adicionalmente `dim_DM(C)≤2` para miembros de `𝔄_Schw(O)` por regularidad
de Kruskal–Szekeres (Prop 7.3, `comite_decision_010.md:72,95`), pero esa expectativa está
"`asserted by generator audit, not measured`" — **no** se declara aquí como condición necesaria
demostrada, solo como propiedad esperada de la familia generadora, consistente con comité 012 D2.

**No hay hoy una caracterización intrínseca y cerrada de `𝔄_Schw(O)`** aplicable a una completación
combinatoria abstracta (como las de Alloy) que no provenga literalmente del generador. Esto se
registra como brecha abierta, no se rellena con una fórmula inventada.

## Resultado exigido para (b)

```text
CLAUSE_B_STATUS = PARTIAL_CANDIDATE
```

El núcleo mínimo `𝔄_C1(O)` (B1+B2+B3+finitud) es cerrado y copiable directamente a una
especificación Alloy o Lean. Permanece abierto: (i) la condición de groundedness del sector oculto
(`UNRESOLVED_BLOCKER`, nunca antes evaluado); (ii) `𝔄_Schw(O)` solo está operacionalizada por
procedencia, no por un predicado intrínseco sobre completaciones abstractas.

**Definición compacta de `𝔄_C1(O)`** (copiable):

```
𝔄_C1(O) = { C ⊇ O finito :
              ∀x,y∈O (x<_C y ⟺ x<_O y)          [B1, literal, vía ι_C]
              ∧ <_C irreflexiva y trans. cerrada  [B2]
              ∧ ∀a,b∈O,∀h∈H_C ¬(a<_C h<_C b) }   [B3, convexidad — MANDATORY_FOR_C1]
```

---

# Parte III — Cláusula (c): regla de referencia inducida

## Candidatos localizados en los documentos existentes

### Candidato 1 — `R(C) = Max(C)` / `isInterface`

```text
NAME = Bare global maximality (R=Max(C))
FORMAL_DEFINITION = R(C) := {x∈C : ¬∃y∈C, x<_C y}   (nachocausal/c1_selector.maximal_elements;
                     equivalente a Alloy 002 isInterface[c,e] ⇔ e∈Max(C), comite_decision_010.md:73)
DOMAIN = todo poset finito no vacío
CODOMAIN = subconjunto de C
ISOMORPHISM_INVARIANCE = SÍ — Max(C) es invariante bajo reetiquetado (Guard-v cubre selectores
                          de este tipo, nachocausal/selection_guard.py:52-84)
PULLBACK_COMPATIBILITY = trivialmente sí (es un subconjunto, restringible a O), pero el pullback
                          resultante es siempre vacío (ver abajo)
NONTRIVIALITY = NO — down(Max(C)) = C para todo poset finito no vacío (comité 010 falsifier
                ataque 2, `comite_decision_010.md:111`); por tanto down_closure(reference)=C,
                black_region=∅, H[C;R]=∅ SIEMPRE. Confirmado ejecutablemente
                (`dev/PR003_C1_RELATIONAL_SPEC.md §9`, comité 009 preflight: NO_INTERFACE)
PHYSICAL_INTERPRETATION = ninguna declarada más allá de "frontera/maximalidad" genérica; no
                           corresponde a ningún observable físico nombrado en el repo
KNOWN_FAILURES = trivializa universalmente a NO_INTERFACE; comité 010 falsifier: "the unique closed
                 selector cannot produce a decision, incompatible or otherwise"
STATUS = REJECTED_TRIVIAL
```

### Candidato 2 — Tripartición lateral por orden conjugado (Q-track)

```text
NAME = Conjugate-order lateral tripartition
FORMAL_DEFINITION = con realizador P = L_U ∩ L_V (requiere dim_DM(C)≤2): x <_Q y :⇔ U_x<U_y ∧
                     V_x>V_y; tripartición canónica {L_A, core_A, R_A}
                     (dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md §7.4.1, citado en
                     comite_decision_010.md:73,79-80)
DOMAIN = subconjunto de 𝔄(O) con dim_DM(C)≤2 (aproximadamente 𝔄_Schw, no todo 𝔄_C1)
CODOMAIN = partición de C en tres clases (no un subconjunto simple — objeto de tipo distinto al
           candidato 1)
ISOMORPHISM_INVARIANCE = UNVERIFIED — unicidad-salvo-intercambio requiere primalidad modular
                          (Gallai), "PLAUSIBLE a.s. bajo Poisson pero [UNVERIFIED] vs cita primaria"
                          (comite_decision_010.md:80)
PULLBACK_COMPATIBILITY = no implementada; no existe código ejecutable en nachocausal/ para Q ni
                          para la tripartición
NONTRIVIALITY = no evaluada contra ningún testigo — es "el candidato que la obstrucción de Alloy
                002 no alcanza" (comite_decision_010.md:80), pero eso es ausencia de ataque, no
                prueba de no-trivialidad
PHYSICAL_INTERPRETATION = capta la señal lateral/espacial (spacelike), ortogonal a la señal de
                           futuro que usa el estimador del PASS — no se ha establecido que sea
                           EL objeto de referencia del horizonte; es un candidato para serlo
KNOWN_FAILURES = bipartición exhaustiva refutada para |A|≥2 (contraejemplo de intercalación,
                  solo sobrevive la tripartición, NOTES §7.4.1); etiquetado
                  `III_PENDING_TWO_FACE_LEMMA`, no un cierre
STATUS = DEFERRED
```

## Otros candidatos descartados por confusión de nivel

`boundary-bracket` / `two_means_split` (S3) **no es un candidato para (c)**: es el objeto de nivel 5
de la jerarquía de comité 012 §3 (comportamiento de un estimador concreto bajo densidad), no una
regla de referencia inducida sobre pares de completaciones. Confundirlos violaría la regla de
no-inferencia de comité 012 §3. No se evalúa aquí como candidato de (c).

## Prohibiciones verificadas

Ningún candidato evaluado usa la salida del propio estimador, un criterio ajustado tras ver el
flip, coordenadas externas (`r`, `t*`), etiquetas del generador no conservadas en `past_matrix`, ni
el conocimiento de cuál completación es "A" o "B". El candidato 1 fue rechazado por trivialidad, no
por leakage. El candidato 2 no ha sido implementado, por lo que no puede auditarse contra estas
prohibiciones todavía — se marca como pendiente, no como aprobado.

## Resultado exigido para (c)

```text
CLAUSE_C_STATUS = BLOCKED
CLAUSE_C_RECOMMENDED_RULE = NONE
CLAUSE_C_BLOCKER =
  Ningún candidato satisface simultáneamente los siete requisitos. El candidato 1 (R=Max(C)) es
  bien-definido, order-only, invariante y con pullback trivial, pero es REJECTED_TRIVIAL (no
  distingue nada). El candidato 2 (tripartición Q) tiene interpretación física más prometedora y
  no ha sido atacado por Alloy 002, pero carece de: (i) implementación ejecutable en
  nachocausal/; (ii) prueba de invarianza bajo isomorfismo (primalidad modular UNVERIFIED); (iii)
  cualquier chequeo de no-trivialidad contra un testigo concreto. Decisión física pendiente antes
  de poder cerrar (c): ¿debe el proyecto invertir en implementar y probar el candidato 2, o buscar
  un tercer candidato? Esa es una decisión de PI/comité, no derivable de los artefactos existentes.
```

---

# Parte IV — Cláusula (e): predicado de incompatibilidad

## Formalización auditada del predicado base

```
Incompatible_O(C_A, C_B) ⟺
    C_A, C_B ∈ 𝔄(O)
  ∧ C_A|_O = C_B|_O = O           [misma relación inducida, R4 §2 fila 2]
  ∧ PB_O(R(C_A)) ≠ PB_O(R(C_B))
```

**Dependencia explícita de (c):** este predicado no puede evaluarse hoy porque `R` no está cerrada
(`CLAUSE_C_STATUS = BLOCKED`). Lo que sigue es una auditoría **estructural** del esquema, no una
evaluación.

## Interpretación de `≠`

`PB_O(R(C))` es, para el único candidato con representación como subconjunto (candidato 1), un
elemento de `2^O` — un conjunto. Para conjuntos finitos, desigualdad de conjuntos es lógicamente
equivalente a la existencia de un elemento en la diferencia simétrica:

```
A ≠ B  ⟺  ∃e (e∈A ↮ e∈B)      (A, B ⊆ O finito)
```

Para el candidato 2 (tripartición), `PB_O(R(C))` no es un subconjunto simple sino una partición
inducida de `O` en tres clases; `≠` ahí significa **desigualdad de particiones** (existe un par
`x,y∈O` cuya relación de co-pertenencia a una misma clase difiere entre `PB_O(R(C_A))` y
`PB_O(R(C_B))`) — es incompatibilidad de **estructura**, no solo de cardinalidad o pertenencia
puntual (opción 5 del brief). **Qué forma exacta de `≠` aplica depende de qué candidato de (c) se
cierre eventualmente — no se fija aquí una única forma universal.**

## Dos niveles

### E-element

```
E-element(C_A,C_B) :⟺ ∃e∈O :  e∈PB_O(R(C_A))  ↮  e∈PB_O(R(C_B))
```

Forma constructiva/Skolemizada — corresponde exactamente al patrón del testigo Alloy 002, donde el
elemento skolemizado `Element$3` es precisamente un testigo E-element para el candidato 1
(`alloy_verification_002...md` §4: `skolem $SameObservationForcesSameInterfaceDecision_e =
{Element$3}`).

### E-set

```
E-set(C_A,C_B) :⟺  PB_O(R(C_A)) ≠ PB_O(R(C_B))
```

**Predicado principal:** `E-set`, porque es la forma literal en que la cláusula base del brief está
escrita (comparación directa de los dos pullbacks) y porque generaliza sin cambios a objetos que no
son subconjuntos (particiones, candidato 2). `E-element` es la **consecuencia equivalente**
cuando `PB_O(R(C))` es representable como subconjunto de `O` (candidato 1 únicamente) — no es una
noción independiente en ese caso, es el testigo constructivo de `E-set`.

## Indistinguibilidad observacional exigida

Debe coincidir entre `C_A` y `C_B`, exactamente en el sentido más débil que R4 §2 permite declarar
sin ambigüedad:

- mismo conjunto literal `O` (carrier, R4 §2 fila 1);
- mismo orden inducido sobre `O` (R4 §2 fila 2) — **este es el nivel que Alloy 002 efectivamente
  estableció** ("relación inducida idéntica sobre `{E2,E3}`"), no más;
- mismas etiquetas/datos permitidos al estimador (solo `past_matrix`, ninguna coordenada);
- ausencia de acceso a `H_C` por parte de cualquier regla downstream;
- misma convención de pullback (un único operador `PB_O` fijo, no uno distinto por completación).

**No** se exige (ni se ha establecido para ningún candidato) coincidencia del "mismo output
ejecutable" (R4 §2 fila 3) — eso sería una noción más fuerte, no probada para ningún par existente.

## Resultado exigido para (e)

```text
CLAUSE_E_STATUS = PARTIAL_CANDIDATE
CLAUSE_E_PRIMARY_PREDICATE = E-set:  PB_O(R(C_A)) ≠ PB_O(R(C_B))
CLAUSE_E_ELEMENTWISE_FORM = E-element:  ∃e∈O, e∈PB_O(R(C_A)) ↮ e∈PB_O(R(C_B))  (equivalente a
                             E-set cuando PB_O(R(C)) es representable como subconjunto de O)
CLAUSE_E_SETWISE_FORM = PB_O(R(C_A)) ≠ PB_O(R(C_B))  (forma general, incluye desigualdad de
                          particiones para referencias no-subconjunto)
CLAUSE_E_OBSERVATIONAL_EQUIVALENCE = mismo carrier O + misma relación inducida sobre O (R4 §2,
                                       filas 1-2) + ausencia de acceso a H_C + un único operador
                                       PB_O fijo. NO se exige (ni se ha probado) coincidencia de
                                       output ejecutable completo.
```

El esquema está completo; lo que falta para volverlo operativo es exclusivamente la cláusula (c)
— no hay ninguna brecha adicional propia de (e).

---

# Parte V — Auditoría conjunta de coherencia

## No vacuidad

`𝔄_C1(O)` es no vacío para todo `O` finito: la completación trivial `C=O` (`H_C=∅`) satisface B1
(idéntica trivialmente), B2 (heredada de `O`) y B3 (vacuamente verdadera, no hay `h∈H_C`). Además,
**Completion A del testigo Alloy 002 es un segundo miembro no trivial**: `H_C={E1}`, y satisface
B1–B3 según `witness_note.md` §4 (orden válido ✓, convexo ✓ — E1 está por encima de todo lo
observado, no interpuesto). `𝔄_C1(O)` tiene, por tanto, al menos dos miembros distintos para el `O`
del testigo — no es una clase degenerada de un solo elemento.

## No trivialidad de E

El candidato 1 de (c) hace que `E` sea **siempre falso**: como `H[C;R]=∅` para todo `C` (down(Max(C))=C
siempre), `PB_O(R(C))=∅` para toda completación, luego `PB_O(R(C_A))=PB_O(R(C_B))=∅` para
cualquier par — `E-set` es idénticamente falso bajo el candidato 1. Este es exactamente el
mecanismo que el falsificador de comité 010 señaló ("the unique closed selector cannot produce a
decision, incompatible or otherwise", `comite_decision_010.md:111`) y confirma por qué (c) debe
cerrarse con un candidato no trivial **antes** de que (e) pueda ser no vacuamente verdadero para
ningún par. Bajo el candidato 2 (no implementado), la no-trivialidad de `E` es simplemente
**desconocida** — no se afirma ni se refuta aquí.

## Separación de niveles (mapeo a la jerarquía de comité 012 §3)

| Nivel de este documento | Corresponde a comité 012 §3 | Estado |
|:---|:---|:---|
| 1. Incompatibilidad lógica | Nivel 1 (testigo lógico) | `PRESENT` (Alloy 002) |
| 2. Incompatibilidad dentro de `𝔄_C1` | Nivel 4 restringido al núcleo mínimo | NO establecida — el único par candidato (A,B) tiene `B∉𝔄_C1(O)` (falla B3); no hay par admisible conocido que produzca `E` verdadero |
| 3. Incompatibilidad dentro de `𝔄_Schw` | Nivel 4, subclase física completa | A fortiori no establecida (subconjunto estricto de 2, y (c) sigue `BLOCKED`) |
| 4. No-identificabilidad física | Sección de síntesis de comité 012 | `OPEN`, no establecida ni refutada |
| 5. Fallo/éxito de `boundary-bracket`/S3 | Nivel 5 (estimador) | `FAILED_BASELINE_UNDER_PRECOMMITTED_DENSITY_COVERAGE_CRITERION` — eje ortogonal, no afectado por nada de lo anterior |

**Regla explícita:** aunque un `R` futuro hiciera `E` verdadero para un par en `𝔄_C1(O)` (nivel 2),
eso **no** constituiría no-identificabilidad física (nivel 4) sin además establecer pertenencia a
una clase físicamente interpretable (`𝔄_Schw` u otra superclase físicamente motivada) — exactamente
la regla de no-inferencia automática entre niveles que exige comité 012 §3.

## Relación con Alloy 002 (deductiva, sin ejecución)

- **¿Pertenece a `𝔄_C1(O)`?** Completion A: **SÍ** (satisface B1, B2, B3 según
  `witness_note.md` §4). Completion B: **NO** (falla B3 — `E2<E0<E3`, `E0` causalmente interpuesto).
- **¿Su incumplimiento de convexidad sigue excluyéndolo?** Sí, y ahora de forma más fuerte: B3 es
  parte de la definición misma del núcleo mínimo `𝔄_C1(O)`, no solo de una subclase física
  adicional — Completion B queda excluida incluso de la clase causal más permisiva definida en
  este documento.
- **¿Pertenece Completion A a `𝔄_Schw(O)`?** `UNRESOLVED` — `𝔄_Schw(O)` se define aquí por
  procedencia del generador sellado; Completion A es un objeto combinatorio abstracto de Alloy, no
  una salida literal de `generator.py`, por lo que su procedencia no está establecida en ninguna
  dirección. No se afirma que pertenezca ni que no pertenezca.
- **¿Qué condiciones necesitaría Alloy 003?** Codificar un par `(C_A', C_B')` ambos en `𝔄_C1(O)`
  (idealmente también con procedencia `𝔄_Schw`), usando un `R` `RECOMMENDED` (no
  `REJECTED_TRIVIAL`) con pullback bien definido, tal que `E-set(C_A',C_B')` sea verdadero. Dado
  que `(c)` está `BLOCKED`, **ningún Alloy 003 puede construirse hoy de forma no vacía** — cualquier
  intento heredaría o bien la trivialidad del candidato 1, o bien un candidato 2 sin implementación
  ni prueba de invarianza.

## Relación con el PASS

El predicado `E`, bajo cualquiera de los dos candidatos evaluados, afecta como máximo: (candidato 1)
la maximalidad global de un elemento y el conjunto de maximales — objetos que **no** son el
observable agregado del PASS; (candidato 2, si se implementara) una tripartición lateral, que
**tampoco** es el observable del PASS. El observable agregado que produjo el `PASS` (prereg-002) es
la bimodalidad de futuro-volumen `O(i)=|future(i)|` sobre elementos minimales — un objeto de nivel 5
(§3 comité 012), enteramente distinto y no conectado por ningún lema existente a `Max(C)`, a
`H[C;R]`, ni a la tripartición `Q`. **No se transfiere ningún resultado entre estos objetivos sin
un lema explícito que hoy no existe.** Cualquier futuro intento de conectar un flip de maximalidad
con el observable del PASS requiere construir y probar ese lema puente — no puede asumirse.

---

# Parte VI — Gate para Alloy 003

```text
ALLOY_003_GATE_B = PARTIALLY_SATISFIED
  (núcleo 𝔄_C1: B1+B2+B3+finitud CERRADO y copiable; groundedness UNRESOLVED_BLOCKER; 𝔄_Schw solo
  operacionalizada por procedencia, sin predicado intrínseco — insuficiente para un modelo Alloy
  que necesite generar completaciones "Schwarzschild-admisibles" sin invocar el generador mismo)

ALLOY_003_GATE_C = NOT_SATISFIED
  (ningún candidato de referencia tiene STATUS=RECOMMENDED; candidato 1 REJECTED_TRIVIAL,
  candidato 2 DEFERRED sin implementación ni prueba de invarianza)

ALLOY_003_GATE_D = NOT_SATISFIED
  (la regla de pullback nunca fue adjudicada por ningún comité — R4 §3(d) la marca
  OPTIONAL_CANDIDATE; c1_selector.down_closure es el único candidato existente y se usa en este
  documento como base de trabajo para las fórmulas de la Parte IV, pero su cierre como regla única
  válida permanece un bloqueo explícito, no una decisión)

ALLOY_003_GATE_E = NOT_SATISFIED
  (el esquema formal de (e) está completo, pero es inevaluable mientras GATE_C no se satisfaga —
  bloqueo derivado, no una brecha propia de (e))

ALLOY_003_GATE_PHYSICAL_SUBCLASS = NOT_SATISFIED
  (𝔄_Schw solo operacionalizada por procedencia del generador; ningún modelo Alloy combinatorio
  puede hoy codificar "pertenece a 𝔄_Schw" sin invocar directamente r=2M, lo cual violaría
  NO_GROUND_TRUTH_LEAKAGE)

ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED
```

No se autoriza Alloy 003 en ninguna modalidad (ni siquiera restringida al C1 lógico/mínimo): la
regla `R` y la regla de pullback siguen siendo móviles (`GATE_C`, `GATE_D` ambos `NOT_SATISFIED`),
que es exactamente la condición que el brief de convocatoria prohíbe ignorar.

---

# Bloque normativo

```text
DOCUMENT_ID = PR003_C1_BCE_CLOSED_CANDIDATE

CLAUSE_B_STATUS = PARTIAL_CANDIDATE
CLAUSE_B_DEFINITION =
  𝔄_C1(O) = { C ⊇ O finito : (B1) ∀x,y∈O (x<_C y ⟺ x<_O y) [literal, vía ι_C]
              ∧ (B2) <_C irreflexiva y transitivamente cerrada
              ∧ (B3) ∀a,b∈O,∀h∈H_C ¬(a<_C h<_C b) [convexidad, MANDATORY_FOR_C1] }
  Sin restricción sobre |H_C| (EXCLUDED_FROM_MINIMAL_C1); groundedness de H_C UNRESOLVED_BLOCKER.
  𝔄_Schw(O) ⊆ 𝔄_C1(O) := completaciones con procedencia en la familia generadora 1+1D
  Eddington-Finkelstein sellada (generator.py, thresholds.py:37-43); dim_DM≤2 esperado
  (Prop 7.3, no verificado como necesario) — sin predicado intrínseco cerrado sobre
  completaciones combinatorias abstractas.

CLAUSE_C_STATUS = BLOCKED
CLAUSE_C_RECOMMENDED_RULE = NONE
CLAUSE_C_BLOCKER =
  Candidato 1 (R=Max(C)): REJECTED_TRIVIAL (down(Max(C))=C siempre, H[C;R]=∅ siempre).
  Candidato 2 (tripartición de orden conjugado Q): DEFERRED — sin implementación ejecutable,
  invarianza bajo isomorfismo UNVERIFIED (primalidad modular de Gallai), no-trivialidad no
  evaluada contra ningún testigo. Ningún tercer candidato existe en el repo. Decisión física
  pendiente: invertir en el candidato 2 o buscar uno nuevo.

CLAUSE_D_STATUS = UNRESOLVED_BLOCKER
  (nunca adjudicada por ningún comité; R4 §3(d) la marca OPTIONAL_CANDIDATE; único candidato
  existente = nachocausal.c1_selector.down_closure, usado aquí como base de trabajo sin cerrarla)

CLAUSE_E_STATUS = PARTIAL_CANDIDATE
CLAUSE_E_PRIMARY_PREDICATE = E-set:  PB_O(R(C_A)) ≠ PB_O(R(C_B))
CLAUSE_E_OBSERVATIONAL_EQUIVALENCE =
  mismo carrier O + misma relación inducida sobre O + ausencia de acceso a H_C + un único
  operador PB_O fijo. No se exige coincidencia de output ejecutable completo (no probada para
  ningún par existente).

C1_MINIMAL_CLASS_STATUS = PARTIAL_CANDIDATE
  (núcleo B1-B3+finitud cerrado; groundedness de H_C UNRESOLVED_BLOCKER)
C1_SCHWARZSCHILD_SUBCLASS_STATUS = PARTIAL_CANDIDATE
  (solo operacionalizada por procedencia del generador; sin predicado intrínseco cerrado)

ALLOY_002_STATUS_UNDER_CANDIDATE =
  Completion A ∈ 𝔄_C1(O) (pertenencia a 𝔄_Schw UNRESOLVED — no es salida literal del generador);
  Completion B ∉ 𝔄_C1(O) (falla B3/convexidad). ALLOY_002_C1_WITNESS_STATUS se preserva sin
  cambios: INVALID_UNDER_CONVEXITY_REQUIREMENT.
ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED

PHYSICAL_IDENTIFIABILITY_STATUS = NOT_ESTABLISHED

NEXT_REVIEW_REQUIRED =
  Revisión por comité (012 reconvocado o nuevo) de este candidato B/C/E antes de cualquier
  búsqueda de testigos, modelo Alloy 003, o formalización Lean. Decisión de PI requerida sobre
  si invertir en implementar/probar el candidato Q-track de (c) o buscar una alternativa.

NEXT_AUTHORIZED_ACTION =
  Revisión de comité de este documento. Si se endosa: redacción (solo escritura, sin ejecución)
  de (i) una decisión explícita sobre groundedness de H_C para 𝔄_C1(O); (ii) una especificación
  matemática completa (no implementación) del candidato Q-track suficiente para evaluar por
  escrito su invarianza bajo isomorfismo antes de programarlo.

NEXT_FORBIDDEN_ACTIONS =
  Alloy 003 en cualquier modalidad antes de cerrar (c) y (d) |
  tratar la pertenencia de Completion A a 𝔄_C1(O) como pertenencia a 𝔄_Schw(O) |
  usar R=Max(C) como si fuera un candidato no trivial |
  usar dim_DM≤2 como evidencia de admisibilidad física fuera de 𝔄_Schw |
  citar "Variant A"/"Bruno" (checkout xinhjBrant/mathlib4,
  f008ff9931c6d541d0dc819eef11f93479f6cb96) como evidencia en este repositorio |
  reclasificar boundary-bracket FAIL como PASS, o usarlo como evidencia de identificabilidad |
  transferir cualquier resultado sobre Max(C)/H[C;R]/tripartición Q al observable agregado del
  PASS sin un lema explícito nuevo |
  commit o push de este documento sin autorización explícita del PI

OVERALL_CANDIDATE_STATUS = BCE_PARTIAL_CANDIDATE_READY_FOR_REVIEW
```
