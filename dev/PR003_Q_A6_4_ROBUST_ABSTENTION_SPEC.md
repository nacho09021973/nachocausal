# PR-003 — Especificación A6.4: clasificador lateral robusto con abstención explícita (Q, uso diagnóstico únicamente)

> Autorizado por `docs/comite/comite_decision_014_q-reference-rule-disposition.md`, D9
> (`NEXT_AUTHORIZED_ACTION = Q_A6_AGGREGATION_SPECIFICATION_ONLY`): redacción, solo escritura, de
> (i) un criterio de admisibilidad order-only para `A∈𝔄(C)` basado en A5 excluyendo `O(i)`; (ii) la
> formalización completa de A6.4 (clases robustas con abstención) como única forma de agregación
> autorizada; (iii) evaluación conceptual de la formalizabilidad de QG3. **Sesión exclusivamente de
> especificación matemática y auditoría conceptual.** No se ejecutó ninguna simulación, sprinkling,
> enumeración, búsqueda de contraejemplos, prueba Alloy, formalización Lean, análisis estadístico,
> script ni código. Sin commit ni push. Único archivo escrito por esta sesión: este documento.
>
> **Este documento NO desarrolla una referencia física adoptada.** `Q` permanece
> `Q_DISPOSITION = Q_DIAGNOSTIC_CANDIDATE_ONLY` (comité 014 D8); todo lo que sigue es la
> especificación de una **regla diagnóstica** con abstención, no de una regla de referencia física
> de C1. No se afirma identificabilidad física en ningún punto.
>
> **Disciplina terminológica (preservado sin reinterpretación, verificado por lectura directa de
> las fuentes esta sesión):**
>
> ```text
> Q_DISPOSITION = Q_DIAGNOSTIC_CANDIDATE_ONLY
> OVERALL_VERDICT (comité 014) = Q_REFERENCE_PATH_REMAINS_BLOCKED
> Q_REPRESENTATION_FOUNDATION = CONDITIONALLY_ESTABLISHED
> UNIQUE_MARKER_ALLOWED_USE = DIAGNOSTIC_ONLY
> MARKER_SELECTION_DECISION = NO_CANDIDATE_CLOSED
> MODULAR_PRIMALITY_STATUS = AVAILABLE_BUT_DOES_NOT_SELECT_A
> Q_CURRENTLY_MEETS_ABANDONMENT_CRITERIA = NO
> BIPARTITION_STATUS = REFUTED_FOR_|A|>=2
> TRIPARTITION_STATUS = PROVISIONAL
> TWO_FACE_LEMMA_STATUS = OPEN            (token exacto de la fuente: III_PENDING_TWO_FACE_LEMMA)
> Q_REALIZER_UNIQUENESS_STATUS = UNVERIFIED
> Q_REALIZER_INVARIANCE_STATUS = NOT_ESTABLISHED_IN_GENERAL
> Q_GROUNDEDNESS_DECISION = QG3_ADOPTED_AS_DOMAIN_EXCLUSION_SUPPLEMENT_TO_G1
> Q_PULLBACK_DECISION = P1_LITERAL_INTERSECTION_FOR_LATERAL_TYPE
> GROUNDEDNESS_DECISION (comité 013) = G1_ADOPTED_FOR_C1_G3_RESERVED_FOR_SCHW
> CONVEXITY_REQUIREMENT (comité 012) = MANDATORY_FOR_C1
> ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED
> LEAN_AUTHORIZATION_STATUS = NOT_AUTHORIZED
> PHYSICAL_SEARCH_AUTHORIZATION_STATUS = NOT_AUTHORIZED
> PHYSICAL_IDENTIFIABILITY_STATUS = NOT_ESTABLISHED
> ```
>
> La disposición diagnóstica de `Q` **no se reabre**. Ninguna decisión de este documento la revisa.

## 0. Fuentes leídas íntegramente esta sesión

| Archivo | Uso |
|:---|:---|
| `docs/comite/comite_decision_014_q-reference-rule-disposition.md` | Disposición vinculante D1-D9; QG3 (D5); pullback lateral P1 (D6); criterios de abandono (D7); autorización exacta de esta tarea (D9) |
| `dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md` | Reconstrucción de Q (Parte I), caso `\|A\|=1` (Parte II), candidatos A1-A6 (Parte III), primalidad modular (Parte IV), desempates (Parte V), esquema R_Q (Parte VI), compatibilidad E/G1 (Parte VII) |
| `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` (completo, §7.1-7.6, §9) | Definición original del orden conjugado `Q`, Proposición 7.3, contraejemplo de intercalado, tripartición `{L_A, core_A, R_A}`, restricción anti-circularidad §7.5, descomposición modular §7.4.1 |
| `docs/comite/comite_decision_013_c1-bce-review.md` | G1 (D1), R2_AUTHORIZE_DEVELOPMENT (D2), familia de pullbacks tipada por codominio (D3), generalización de E-set a desigualdad de particiones (D4) |
| `dev/PR003_C1_BCE_CLOSED_CANDIDATE.md` | Notación común (Parte I: `O`, `C`, `H_C`, `ι_C`, `R(C)`, `PB_O`), cláusula (e) (Parte IV: E-set/E-element, co-pertenencia para particiones), observable del PASS (Parte V, "Relación con el PASS") |

**Verificación de cobertura terminológica:** la búsqueda `rg` sobre el repositorio (excluyendo
`biblioteca/`) confirma que la terminología de orden conjugado, tripartición, marcador `A`,
realizadores, Proposición 7.3, primalidad modular y firmas relacionales solo está definida en los
archivos de la tabla anterior (más menciones derivadas en comités 009-012, leídas vía sus citas
literales en los comités 013/014). Coincide con la verificación ya registrada en
`dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md` §0. No se reconstruye terminología desde informes de
terminal: todas las definiciones usadas abajo citan archivo y sección de origen.

**Verificación de ausencia de artefacto:** no se generó ningún archivo de evidencia; no se tocó
`thresholds.py`; no se modificó ningún selector, test, modelo Alloy ni archivo Lean; no se ejecutó
ningún script. Único comando de búsqueda: un `rg` de localización terminológica (lectura, no
análisis).

---

# Parte I — Reconstrucción tipada de la tripartición `Q(C,A,ρ)`

## I.1 Estructura exacta según las fuentes

La construcción proviene de `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §7.3-7.4.1 y de su
reconstrucción en `dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md` Parte I (`Q_SOURCE_DEFINITION`). Se
escribe aquí con el realizador como argumento **explícito**, siguiendo la precisión de comité 014
D1 ("dos realizadores distintos y admisibles de la misma completación pueden producir referencias
`Q` distintas" cuando el grafo de incomparabilidad no es primo):

1. **Realizador.** `ρ = (L_U, L_V)`: par de órdenes lineales sobre el carrier de `C` con
   `P_C = L_U ∩ L_V` (la fuente escribe `P_C = L_U ∩ L_V`, §7.3, Prop. 7.3). Su existencia es
   equivalente a `dim_DM(C) ≤ 2` (Dushnik–Miller, citado en §7.2/§8) y está
   `CONDITIONALLY_ESTABLISHED` (comité 014 D1), condicional a la Proposición 7.3 — que es una
   auditoría de código condicional, no una medición ni un teorema incondicional (paso
   "parche EF = restricción del producto Kruskal" marcado `[UNVERIFIED]` en la fuente).
2. **Orden conjugado, dado ρ.** `x <_Q y :⇔ U_x < U_y ∧ V_x > V_y` — la orientación transitiva del
   grafo de incomparabilidad de `P_C` (§7.4.1). Las coordenadas `U, V` son las posiciones en
   `L_U, L_V`; la fuente subraya que las coordenadas auxiliares "sólo [son] para razonar, NO entran
   en nada" — la construcción es order-only dado `ρ`.
3. **Marcador.** `A ⊆ C`, antichain bajo `P_C` ("antichain candidata a 'membrana'", Parte I del
   documento de desarrollo). `N(A)` es una **losa spacelike**: todo `x ∈ N(A)\A` es
   `P`-incomparable a todo `A` (§7.4). La extensión exacta de `N(A)` **no está fijada por ningún
   documento** (`Q_SOURCE_DOMAIN` punto (ii)); para `|A|=1` la fuente sí la fija:
   `N(a) = spacelike(a)`.
4. **Salida, caso `|A|=1` (`A={a}`).** Bipartición limpia y exhaustiva de `spacelike(a)`:
   `L_a = {x ∈ spacelike(a) : x <_Q a}`, `R_a = {x ∈ spacelike(a) : a <_Q x}`,
   `spacelike(a) = L_a ⊔ R_a` — "Resultado positivo 1", §7.4.1. Sin clase `core`.
5. **Salida, caso `|A|≥2`.** Tripartición `{L_A, core_A, R_A}` de `N(A)\A`:
   `L_A = {x : x <_Q a ∀a∈A}`, `R_A = {x : a <_Q x ∀a∈A}`,
   `core_A = (N(A)\A) ∖ (L_A ∪ R_A)` — "Resultado positivo 2", §7.4.1. La bipartición exhaustiva
   está **refutada** para `|A|≥2` (contraejemplo de intercalado trabajado: `x=(1,1)` con
   `a₁=(0,2)`, `a₂=(2,0)`).

Los nombres `L_a`, `R_a`, `L_A`, `core_A`, `R_A`, `spacelike(a)`, `N(A)` son los de las fuentes;
no se inventa ningún nombre nuevo para las partes.

## I.2 Campos obligatorios

```text
Q_OBJECT_INPUT_COMPLETION =
  C ∈ 𝔄_C1(O) con dim_DM(C) ≤ 2 (Q_VALID_DOMAIN, comité 014 D1 — subconjunto de 𝔄_C1(O),
  solapado no idéntico a 𝔄_Schw(O); condicional a Prop. 7.3, CONDITIONALLY_ESTABLISHED)

Q_OBJECT_INPUT_MARKER =
  A ⊆ C, antichain bajo P_C ("marcador"/"membrana candidata"); caso base cerrado |A|=1 (A={a});
  caso |A|≥2 dependiente además de la extensión de N(A), no fijada por ningún documento

Q_OBJECT_INPUT_REALIZER =
  ρ = (L_U, L_V), par de órdenes lineales con P_C = L_U ∩ L_V; explícito como argumento porque
  Q_REALIZER_UNIQUENESS_STATUS = UNVERIFIED y Q_REALIZER_INVARIANCE_STATUS =
  NOT_ESTABLISHED_IN_GENERAL (comité 014 D1): en el caso no primo, realizadores distintos
  producen Q distintas

Q_OBJECT_OUTPUT_TYPE =
  Partición etiquetada PARCIAL sobre C: exhaustiva SOBRE SU DOMINIO PROPIO (spacelike(a) para
  |A|=1; N(A)\A para |A|≥2) pero no definida fuera de él (elementos timelike a A, elementos de
  A mismo, y elementos fuera de la losa N(A) quedan sin clasificar). Definida solo salvo el
  intercambio global de caras (clase salvo swap) — NO es una estructura orientada

Q_OBJECT_COMPONENTS =
  |A|=1: {L_a, R_a}          (dos clases, sin core — "Resultado positivo 1")
  |A|≥2: {L_A, core_A, R_A}  (tres clases; core_A = intercalados — "grosor relacional de la
                              membrana", "Resultado positivo 2"; TRIPARTITION_STATUS =
                              PROVISIONAL, no adoptada)

Q_OBJECT_SWAP_SYMMETRY =
  Reversión global Q ↔ Q⁻¹ ⟺ intercambio L ↔ R (L_a↔R_a; L_A↔R_A con core_A fijo). Libertad de
  orientación LEGÍTIMA reconocida por la fuente (Parte II punto 4 del documento de desarrollo),
  no una falta de definición. Fijarla externamente fue rechazado como AD_HOC por comité 014 D4.
  core_A es invariante bajo el swap

Q_OBJECT_DOMAIN_CONDITIONS =
  (i) dim_DM(C) ≤ 2 (existencia de ρ; condicional a Prop. 7.3);
  (ii) A antichain bajo P_C;
  (iii) N(A) losa spacelike — extensión general NO especificada (abierta), salvo |A|=1 donde
        N(a) = spacelike(a) queda fijada por la fuente;
  (iv) para unicidad de Q salvo swap: primalidad modular del grafo de incomparabilidad
       [PLAUSIBLE, UNVERIFIED] — NO exigida aquí como condición de dominio; su fallo se trata
       en la Parte IX (QG3) como generador de abstención, no como exclusión
```

**Aclaración de tipo exigida por el brief:** la salida es una **partición exhaustiva de su dominio
propio** (`spacelike(a)` o `N(A)\A`), que vista sobre `C` completo es una **tripartición parcial**
(no cubre `C`), entregada como **estructura etiquetada solo salvo intercambio de caras** (clase
salvo swap). No es una familia de subconjuntos sin estructura: la relación de co-pertenencia entre
clases está definida, aunque la orientación `L`/`R` no lo esté.

**Preservado sin conversión a laguna:**

```text
BIPARTITION_STATUS = REFUTED_FOR_|A|>=2
TRIPARTITION_STATUS = PROVISIONAL
TWO_FACE_LEMMA_STATUS = OPEN
```

---

# Parte II — Familia de marcadores admisibles `𝔄(C)`

El nombre `𝔄(C)` ("familia de marcadores admisibles") es el ya usado por
`dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md` Parte III (A6) y por comité 014 D3/D4. Esta parte
escribe el criterio `MarkerAdmissible(C,A)` que ningún documento había escrito — el "bloqueo 1" de
comité 014 D8.

## II.1 Exclusiones obligatorias (verificadas contra cada firma abajo)

`MarkerAdmissible` no puede depender de: `O(i) = |futuro(i)|` (volumen futuro — la cantidad exacta
del observable agregado del PASS, bimodalidad de futuro-volumen sobre elementos minimales,
`dev/PR003_C1_BCE_CLOSED_CANDIDATE.md` Parte V) ni de ningún estadístico usado por el PASS; de la
salida del estimador; de coordenadas externas (`r`, `t*`, `U`, `V` como datos — solo la relación
`≺`); de etiquetas del generador; de índices, nombres u orden de almacenamiento (Guard-v,
`nachocausal/selection_guard.py`); de la identidad de la completación como "A" o "B"; del
conocimiento de qué marcador produce incompatibilidad; de parámetros elegidos tras observar el
resultado.

**Regla de cierre composicional (nueva, esta sesión).** La exclusión de `O(i)` debe aplicarse al
**conjunto conjunto de firmas usadas**, no firma a firma: si la combinación de firmas admitidas
determina funcionalmente `O(i)` sobre alguna clase de elementos, la combinación es circular aunque
cada componente por separado no lo sea. Ejemplo concreto (identificado en II.2): para un elemento
minimal `x` (`|↓x| = 0`), el grado de incomparabilidad determina `|↑x| = O(x)` exactamente vía
`|spacelike(x)| = |C| − 1 − |↓x| − |↑x|`. Como el PASS evalúa `O(i)` precisamente sobre elementos
minimales, cualquier gate sobre `|spacelike(x)|` aplicado a minimales re-codifica el estadístico
del PASS. Este es un **canal de circularidad residual no identificado previamente** en ningún
documento — se registra explícitamente como material para el criterio de abandono (3) de comité
014 D7 ("circularidad residual"), y motiva la mitigación M1 de II.3.

## II.2 Auditoría de firmas candidatas mínimas

Las nueve firmas exigidas por el brief, auditadas por separado. `STATUS` usa exactamente los seis
valores permitidos. `DISTINGUISHES_ANY_MARKER` es `UNRESOLVED` en todos los casos donde afirmaría
un hecho empírico: ninguna evaluación se ha ejecutado (sesión sin datos) y ninguna fuente registra
que firma alguna localice una membrana.

### Firma 1 — Isomorphism type del ideal principal

```text
SIGNATURE_NAME = Tipo de isomorfismo del ideal principal ↓x = {y : y ≺ x} ∪ {x}
FORMAL_DEFINITION = sig_↓(x) := clase de isomorfismo de orden del subposet inducido por ↓x
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = SÍ (por construcción)
TOTAL = SÍ (definida para todo x de todo poset finito)
DISTINGUISHES_ANY_MARKER = UNRESOLVED (sin evaluación; ninguna fuente lo registra)
CIRCULAR_WITH_PASS = NO literalmente (determina |↓x|, volumen PASADO; el PASS mide volumen
  FUTURO sobre minimales) — PERO combinada con el grado de incomparabilidad determina |↑x| = O(x)
  (regla de cierre composicional, II.1): prohibida en combinación con la firma 3
PHYSICAL_INTERPRETATION = profundidad causal hacia el pasado; cerca del borde INFERIOR de la caja
  degenera en artefacto de pared (mecanismo simétrico al de Max(C), A4 del desarrollo Q)
KNOWN_DEGENERACIES = |↓x| pequeño para todo x cercano al borde inferior de muestreo,
  independientemente de la posición lateral
STATUS = UNRESOLVED
  (no circular por sí sola, pero eje temporal —no lateral—, riesgo de pared inferior, y prohibida
  en combinación con la firma 3; no se adopta como componente sin un argumento nuevo)
```

### Firma 2 — Isomorphism type del filtro principal

```text
SIGNATURE_NAME = Tipo de isomorfismo del filtro principal ↑x = {y : x ≺ y} ∪ {x}
FORMAL_DEFINITION = sig_↑(x) := clase de isomorfismo de orden del subposet inducido por ↑x
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = SÍ
TOTAL = SÍ
DISTINGUISHES_ANY_MARKER = NO_EVALUABLE (rechazada antes, por circularidad)
CIRCULAR_WITH_PASS = SÍ — el tipo de isomorfismo de ↑x determina |↑x| = O(x), el estadístico
  exacto del estimador sellado (prereg-002 PASS). Es un REFINAMIENTO ESTRICTO de la cantidad
  prohibida: admitirla equivaldría a admitir O(i) con información extra. Viola directamente la
  restricción §7.5 ("la asimetría debe leerse de la estructura de enlaces... nunca la
  accesibilidad futura que el estadístico luego mide") y la exclusión explícita de O(i)
  ordenada por comité 014 D9
PHYSICAL_INTERPRETATION = N/A (rechazada)
KNOWN_DEGENERACIES = N/A
STATUS = REJECTED_CIRCULAR
```

### Firma 3 — Perfil de incomparabilidad

```text
SIGNATURE_NAME = Perfil de incomparabilidad
FORMAL_DEFINITION = sig_sp(x) := |spacelike(x)| = |{y ∈ C : y ⊀ x ∧ x ⊀ y ∧ y ≠ x}|
  (grado del grafo de incomparabilidad; extensible a perfiles de mayor orden — distribución de
  grados dentro de spacelike(x) — manteniendo las mismas propiedades)
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = SÍ
TOTAL = SÍ
DISTINGUISHES_ANY_MARKER = UNRESOLVED (sin evaluación ejecutada)
CIRCULAR_WITH_PASS = NO por sí sola sobre elementos NO extremales (determina la SUMA
  |↓x| + |↑x|, no O(x) individualmente) — PERO sobre elementos minimales determina O(x)
  exactamente (canal residual de II.1). Mitigación M1 (II.3): excluir Min(C) ∪ Max(C) de la
  candidatura a marcador. Prohibida en combinación con las firmas 1/2 (cierre composicional)
PHYSICAL_INTERPRETATION = anchura lateral relacional del elemento; es la firma más alineada con
  el carácter LATERAL de Q (mide extensión spacelike, no accesibilidad temporal). Es
  paridad-simétrica (§7.2, M2: un punto y su espejo lateral comparten firma) — para
  ADMISIBILIDAD de marcador esto es aceptable e incluso deseable (el criterio no debe
  pre-orientar las caras; la orientación es exactamente lo que el swap deja libre)
KNOWN_DEGENERACIES = paridad-simétrica (no distingue lado — irrelevante para admisibilidad);
  parcialmente correlacionada con la altura (elementos centrales en tiempo tienen más
  spacelike); en minimales/maximales codifica O(x)/|↓x| (excluidos por M1)
STATUS = ADMISSIBLE_COMPONENT
  (condicional a M1 — exclusión de extremales — y al cierre composicional de II.1)
```

### Firma 4 — Multiconjunto de tipos de intervalos

```text
SIGNATURE_NAME = Multiconjunto de tipos de intervalos que contienen a x
FORMAL_DEFINITION = sig_int(x) := multiconjunto de clases de isomorfismo de los intervalos
  [u,v] = {w : u ≼ w ≼ v} con u ≺ x ≺ v (versión localizada de las abundancias de intervalo
  C_k de Benincasa-Dowker, citadas como invariante reconocido en A5 del desarrollo Q)
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = SÍ
TOTAL = SÍ (multiconjunto vacío para extremales)
DISTINGUISHES_ANY_MARKER = UNRESOLVED
CIRCULAR_WITH_PASS = EXPOSICIÓN PARCIAL identificada esta sesión: el cardinal del multiconjunto
  es |{(u,v) : u ≺ x ≺ v}| = |↓x∖{x}| · |↑x∖{x}| (por transitividad, todo par pasado×futuro de x
  forma intervalo que contiene a x). El PRODUCTO |↓x|·|↑x|, combinado con la SUMA (firma 3),
  determina el par NO ordenado {|↓x|, |↑x|} — y sobre cualquier clase de elementos donde una de
  las dos coordenadas sea conocida (p. ej. minimales), determina O(x). No es el estadístico del
  PASS por sí sola, pero su margen de seguridad composicional es estrecho
PHYSICAL_INTERPRETATION = abundancias de intervalo = proxy de curvatura/estructura local
  (Benincasa-Dowker 2010, respaldo CONFIRMED en el literature verdict de comité 010, citado en
  A5) — respaldo de literatura real, pero para la versión GLOBAL, no para esta localización
KNOWN_DEGENERACIES = vacía en extremales; cardinal = producto pasado×futuro (arriba)
STATUS = UNRESOLVED
  (no rechazada — la dirección A5 la cita explícitamente — pero su exposición composicional
  requiere adjudicación de comité antes de admitirla como componente)
```

### Firma 5 — Grados de cobertura y cocobertura

```text
SIGNATURE_NAME = Grados de cobertura (links)
FORMAL_DEFINITION = sig_lk(x) := (#{y : y ⋖ x}, #{y : x ⋖ y}) — número de enlaces (relaciones de
  cobertura, sin intermediarios) entrantes y salientes de x
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = SÍ
TOTAL = SÍ
DISTINGUISHES_ANY_MARKER = UNRESOLVED
CIRCULAR_WITH_PASS = NO — el número de LINKS futuros no es el volumen futuro |↑x| (un link es
  una relación de cobertura; O(i) cuenta el futuro COMPLETO). La estructura de enlaces es
  exactamente el material que §7.5 SANCIONA como permitido ("la asimetría debe leerse de la
  estructura de enlaces"). No determina O(x) ni en composición con la firma 3 (los links no
  fijan el volumen)
PHYSICAL_INTERPRETATION = valencia causal inmediata; en el marco del proyecto, los enlaces son
  el material del interfaz H[C;R] (pares de cobertura) y del eje (III) de asimetría de la nota
  fuente (§3, punto 4: "asimetría de enlaces de cobertura a través de un antichain")
KNOWN_DEGENERACIES = fluctuación de Poisson alta elemento a elemento (esperable
  conceptualmente); grado futuro 0 ⟺ x ∈ Max(C), grado pasado 0 ⟺ x ∈ Min(C) — bajo M1 los
  extremales ya están excluidos
STATUS = ADMISSIBLE_COMPONENT
  (condicional a M1; el componente con mejor respaldo textual directo en §7.5)
```

### Firma 6 — Altura y coaltura order-theoretic

```text
SIGNATURE_NAME = Altura y coaltura
FORMAL_DEFINITION = sig_h(x) := (h(x), h*(x)) — longitud de la cadena máxima dentro de ↓x y
  dentro de ↑x respectivamente
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = SÍ
TOTAL = SÍ
DISTINGUISHES_ANY_MARKER = UNRESOLVED
CIRCULAR_WITH_PASS = NO (longitudes de cadena, no volúmenes; no determinan O(x) ni en
  composición conocida)
PHYSICAL_INTERPRETATION = posición TEMPORAL relacional. h*(x) = 0 ⟺ x ∈ Max(C): el uso
  EXTREMAL de esta firma reconstruye exactamente Max(C), descartado por razón física como
  marcador ("pared de muestreo, no horizonte", A4 del desarrollo Q, NEXT_FORBIDDEN_ACTIONS del
  mismo documento). Un uso NO extremal ("banda de altura media") requeriría un umbral de banda
  sin base principiada — riesgo directo de parámetro elegido tras ver resultados (exclusión
  II.1, última fila)
KNOWN_DEGENERACIES = eje temporal puro; extremos = paredes
STATUS = UNRESOLVED
  (admisible solo si algún día existe una regla de banda no extremal principiada; hoy no existe;
  el uso extremal está prohibido por herencia directa del descarte de Max(C))
```

### Firma 7 — Órbita de automorfismos

```text
SIGNATURE_NAME = Órbita de Aut(C)
FORMAL_DEFINITION = sig_orb(x) := órbita de x bajo Aut(C)
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = SÍ (por construcción)
TOTAL = SÍ (toda órbita existe)
DISTINGUISHES_ANY_MARKER = NO en el régimen genérico
CIRCULAR_WITH_PASS = NO
PHYSICAL_INTERPRETATION = ninguna en el caso genérico
KNOWN_DEGENERACIES = Aut(C) trivial casi seguramente bajo sprinkling Poisson continuo ("generic
  finite Poisson sprinklings are asymmetric", mathematician brief de comité 010, citado en A1
  del desarrollo Q y preservado por comité 014 D3): toda órbita es un singleton y la firma
  degenera en la identidad — no discrimina nada exactamente en el régimen de interés
STATUS = REJECTED_TRIVIAL
  (mismo mecanismo por el que A1 fue REJECT en comité 014 D3; se preserva ese veredicto)
```

### Firma 8 — Firma conjunta ideal–filtro–incomparabilidad

```text
SIGNATURE_NAME = Firma conjunta (sig_↓, sig_↑, sig_sp)
FORMAL_DEFINITION = tupla de las firmas 1, 2 y 3
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = SÍ
TOTAL = SÍ
DISTINGUISHES_ANY_MARKER = NO_EVALUABLE (rechazada antes, por circularidad)
CIRCULAR_WITH_PASS = SÍ, doblemente: (i) contiene la firma 2 (REJECTED_CIRCULAR — determina
  O(x) directamente); (ii) incluso sin la componente de filtro, ideal + incomparabilidad
  determinan O(x) por el cierre composicional de II.1 (suma + una coordenada)
PHYSICAL_INTERPRETATION = N/A (rechazada)
KNOWN_DEGENERACIES = N/A
STATUS = REJECTED_CIRCULAR
```

### Firma 9 — Invariantes de descomposición modular

```text
SIGNATURE_NAME = Invariantes de descomposición modular por elemento
FORMAL_DEFINITION = sig_mod(x) := posición de x en el árbol de descomposición modular del grafo
  de incomparabilidad de P_C (p. ej. módulo no trivial mínimo que contiene a x, o "ninguno")
ORDER_ONLY = SÍ
ISOMORPHISM_INVARIANT = SÍ (la descomposición modular es canónica — teorema de Gallai 1967,
  citado en Parte IV del desarrollo Q)
TOTAL = SÍ
DISTINGUISHES_ANY_MARKER = NO en el régimen genérico
CIRCULAR_WITH_PASS = NO
PHYSICAL_INTERPRETATION = un módulo no trivial = "degeneración geométrica no genérica" (§7.4.1)
  — no una localización de membrana
KNOWN_DEGENERACIES = si la primalidad genérica se confirma ([PLAUSIBLE, UNVERIFIED], §7.4.1),
  la firma es CONSTANTE ("ninguno") para todo elemento en el caso típico — no distingue nada
  precisamente en el régimen de interés. Mismo mecanismo que A2 (REJECT, comité 014 D3)
STATUS = REJECTED_TRIVIAL
  (como firma SELECTORA por elemento; se preserva sin cambio MODULAR_PRIMALITY_STATUS =
  AVAILABLE_BUT_DOES_NOT_SELECT_A — su papel legítimo es la condición de estabilidad QG3 a
  nivel de DOMINIO/realizador, Parte IX, no la selección de marcadores)
```

**Balance de la auditoría:** dos firmas alcanzan `ADMISSIBLE_COMPONENT` (perfil de
incomparabilidad, grados de cobertura — ambas condicionales a M1 y al cierre composicional);
tres quedan `UNRESOLVED` (ideal principal, tipos de intervalo, altura/coaltura); cuatro quedan
rechazadas (filtro principal y firma conjunta por circularidad; órbitas e invariantes modulares
por trivialidad genérica). **Ninguna firma admisible tiene establecido que DISTINGA un marcador
de membrana** — `DISTINGUISHES_ANY_MARKER = UNRESOLVED` en ambas supervivientes, sin evaluación
ejecutable en esta sesión y sin registro previo en ninguna fuente.

## II.3 Construcción de la familia

**Restricción estructural previa (no opcional): solo marcadores de un elemento.** De las cinco
formas de construir la familia que lista el brief, cualquier forma que incluya marcadores con
`|A| ≥ 2` hereda tres aperturas simultáneas: `TRIPARTITION_STATUS = PROVISIONAL` (la tripartición
no está adoptada), `TWO_FACE_LEMMA_STATUS = OPEN`, y la extensión de `N(A)` sin especificar
(`Q_SOURCE_DOMAIN` (ii)). La única construcción documentalmente **cerrada** es la del caso
`|A| = 1` ("Resultado positivo 1": bipartición limpia, exhaustiva, canónica salvo swap, con
`N(a) = spacelike(a)` fijado por la fuente). Coherente con
`UNIQUE_MARKER_CASE_DECISION = DIAGNOSTIC_EXAMPLE_NOT_YET_OPERATIONAL_REFERENCE` y
`UNIQUE_MARKER_ALLOWED_USE = DIAGNOSTIC_ONLY` (comité 014 D2) — y A6.4 es exactamente un uso
diagnóstico — esta especificación restringe:

```text
𝔄(C) ⊆ { {a} : a ∈ C }
```

Los marcadores multivaluados (`|A|≥2`) quedan registrados como **extensión bloqueada** (no
rechazada): reabrirlos exige antes cerrar el lema de dos caras y la extensión de `N(A)`.

**Mitigación M1 (exclusión de extremales, principiada).** Se excluyen `Min(C) ∪ Max(C)` de la
candidatura, por dos razones independientes ya documentadas: (i) física — `Max(C)` es la pared de
muestreo, no una localización a media altura (tabla §2 de la nota fuente; descarte explícito de
`Max(C)` como marcador en A4 y en `NEXT_FORBIDDEN_ACTIONS` del desarrollo Q; `Min(C)` es el
artefacto simétrico del borde inferior); (ii) anti-circularidad — sobre extremales, la firma 3
determina `O(x)` o `|↓x|` exactamente (canal residual II.1). M1 es order-only, total, invariante
bajo isomorfismo y no usa ningún parámetro ajustable.

**Forma de la familia (esquema con gate, único punto no cerrado):**

```text
𝔄(C) := { {a} : a ∈ C ∖ (Min(C) ∪ Max(C)),  Gate(a) }
```

donde `Gate(a)` es un predicado order-only construido exclusivamente con las firmas
`ADMISSIBLE_COMPONENT` (3 y 5), respetando el cierre composicional de II.1, **sin desempate a un
único elemento** (la familia retiene todas las clases de equivalencia de firma que satisfacen el
predicado — forma "todas las órbitas/clases que satisfacen un predicado" del brief, no "elemento
de firma extrema con desempate").

**Por qué el gate no puede cerrarse en esta sesión.** Un `Gate` no trivial necesita un umbral o
una condición de extremalidad sobre `sig_sp`/`sig_lk`. No existe en ninguna fuente una base
principiada para ese umbral, y elegirlo ahora sin base sería exactamente "parámetros elegidos
después de observar el resultado" en potencia (exclusión II.1) o un rescate artificial (la
objeción del falsificador en comité 014 D4). La alternativa sin gate:

```text
𝔄₀(C) := { {a} : a ∈ C ∖ (Min(C) ∪ Max(C)) }
```

es canónica, total, no vacía (para todo `C` con al menos un elemento no extremal), invariante y
trivialmente independiente del PASS — pero tiene un **mecanismo de colapso por abstención**
identificado conceptualmente en esta sesión (Parte VII.2): bajo `𝔄₀`, el consenso de A6.4 se
vacía genéricamente. Por tanto:

```text
MARKER_FAMILY_FORMAL_DEFINITION =
  Esquema: 𝔄(C) = { {a} : a ∈ C ∖ (Min(C) ∪ Max(C)), Gate(a) }, con Gate construido solo con
  las firmas ADMISSIBLE_COMPONENT (perfil de incomparabilidad, grados de cobertura) bajo el
  cierre composicional II.1, reteniendo clases de firma completas (sin desempate a un elemento).
  Instanciación base sin gate: 𝔄₀(C) = { {a} : a ∈ C ∖ (Min(C) ∪ Max(C)) } — cerrada y canónica
  pero conjeturalmente trivializante (VII.2). El Gate no trivial NO está cerrado: no existe base
  documental para su umbral. ESTE ES EL BLOQUEO DECLARADO.

MARKER_FAMILY_NONEMPTY_STATUS =
  ESTABLISHED_FOR_𝔄₀ (no vacía siempre que C tenga un elemento no extremal — condición
  order-only verificable); UNRESOLVED para cualquier 𝔄 con Gate no trivial (depende del gate
  inexistente)

MARKER_FAMILY_ISOMORPHISM_STATUS =
  PLAUSIBLE_BY_CONSTRUCTION_NOT_MECHANICALLY_VERIFIED — 𝔄₀ y todo gate construido con firmas
  invariantes de isomorfismo se transportan bajo φ:C≅C' por construcción; no existe prueba
  formal/mecánica (mismo estatus que la naturalidad de Q, Parte II punto 5 del desarrollo)

MARKER_FAMILY_TOTALITY_STATUS =
  TOTAL_FOR_𝔄₀ (definida para toda completación del dominio); UNRESOLVED con gate

MARKER_FAMILY_PASS_INDEPENDENCE =
  ENFORCED_BY_CONSTRUCTION — exclusión de O(i) y de todo refinamiento suyo (firma 2 y firma 8
  REJECTED_CIRCULAR); regla de cierre composicional II.1; mitigación M1 sobre el canal residual
  de minimales (nuevo, esta sesión). Verificación formal de ausencia de CUALQUIER canal residual: NO
  establecida (la fuente A5 ya advertía que la no-circularidad "no ha sido verificada
  formalmente para ninguno en concreto"; el canal de II.1 muestra que la advertencia era
  fundada)

MARKER_FAMILY_PHYSICAL_STATUS =
  NOT_ESTABLISHED — ninguna firma admisible tiene interpretación establecida como localizador de
  membrana; la familia es un objeto diagnóstico, coherente con Q_DISPOSITION
```

**Declaración de bloqueo (exigida por el brief si la familia no puede cerrarse):** una familia no
vacía y canónica **existe** (`𝔄₀`), pero es conjeturalmente trivializante; toda familia con gate
no trivial **no puede definirse hoy** sin inventar un umbral sin base documental. El componente
más consecuente de A6.4 permanece por tanto **bloqueado en su instanciación no trivial** — mismo
bloqueo 1 de comité 014 D8, ahora reducido de "criterio sin escribir" a "esquema escrito con
umbral de gate sin base principiada", con las firmas admisibles ya adjudicadas.

---

# Parte III — Familia de realizadores admisibles

Ninguna fuente da nombre a esta familia; se introduce aquí la notación `ℜ(C)` **declarada como
nueva de este documento** (no existe en disco), definida exclusivamente con material de las
fuentes:

```text
ℜ(C) := { ρ = (L_U, L_V) : L_U, L_V órdenes lineales sobre el carrier de C
                            con P_C = L_U ∩ L_V }
```

"Realizador admisible" significa, según las fuentes: **realización de `P_C` como intersección de
dos órdenes lineales** (§7.3, Prop. 7.3: `P_C = L_U ∩ L_V`; §7.2: teorema de dimensión de
Dushnik–Miller 1941). No hay en ninguna fuente condiciones adicionales de admisibilidad sobre el
realizador (ninguna condición de primalidad se exige para SER realizador; la primalidad gobierna
la UNICIDAD del conjugado, no la existencia). No se asume unicidad en ningún punto.

- **Compatibilidad con Proposition 7.3:** para completaciones con la procedencia auditada
  (generador sellado), la Prop. 7.3 exhibe un realizador concreto (orden de las coordenadas nulas
  de Kruskal), condicional a su hipótesis. Para completaciones combinatorias abstractas con
  `dim_DM(C)≤2`, la existencia es el teorema de Dushnik–Miller. En ambos casos:
  `CONDITIONALLY_ESTABLISHED` (comité 014 D1, `Q_REALIZER_EXISTENCE_STATUS`).
- **Dimensión requerida:** `ℜ(C) ≠ ∅ ⟺ dim_DM(C) ≤ 2` (definición de dimensión de orden ≤ 2).
- **Equivalencias:** (i) el **intercambio del par** `(L_U, L_V) ↦ (L_V, L_U)` es también un
  realizador y produce `Q ↦ Q⁻¹` (el swap global de caras — es la MISMA libertad de orientación de
  la Parte I, vista desde el realizador); (ii) dos realizadores se declaran **Q-equivalentes**
  cuando inducen el mismo conjugado salvo reversión global: `ρ ∼ ρ' :⇔ Q_ρ = Q_{ρ'} ∨
  Q_ρ = (Q_{ρ'})⁻¹`. Por Gallai (§7.4.1), TODOS los realizadores son Q-equivalentes **sii** el
  grafo de incomparabilidad de `P_C` es primo; en el caso no primo existen clases de
  Q-equivalencia múltiples (módulos orientables independientemente).

```text
REALIZER_FAMILY_FORMAL_DEFINITION =
  ℜ(C) = { (L_U,L_V) : órdenes lineales sobre C con L_U ∩ L_V = P_C }, notación nueva de este
  documento; cociente relevante ℜ(C)/∼ con ρ ∼ ρ' ⟺ Q_ρ ∈ {Q_{ρ'}, (Q_{ρ'})⁻¹}

REALIZER_EXISTENCE_STATUS =
  CONDITIONALLY_ESTABLISHED (ℜ(C)≠∅ ⟺ dim_DM(C)≤2; garantizado condicionalmente por Prop. 7.3
  para la familia generadora; comité 014 D1, sin cambio)

REALIZER_EQUIVALENCE_RELATION =
  ρ ∼ ρ' ⟺ Q_ρ = Q_{ρ'} ∨ Q_ρ = (Q_{ρ'})⁻¹  (misma orientación lateral salvo reversión global;
  |ℜ(C)/∼| = 1 ⟺ grafo de incomparabilidad primo — Gallai, §7.4.1)

REALIZER_SWAP_EQUIVALENCE =
  (L_U,L_V) ↦ (L_V,L_U) ∈ ℜ(C) siempre, con Q ↦ Q⁻¹: el swap de caras es interno a la relación
  ∼ (todo realizador es ∼-equivalente a su intercambiado). El clasificador de la Parte IV es
  invariante bajo esta operación por construcción (forma par a par)

REALIZER_ISOMORPHISM_STATUS =
  PLAUSIBLE_BY_CONSTRUCTION_NOT_MECHANICALLY_VERIFIED — φ:C≅C' transporta biyectivamente órdenes
  lineales y preserva intersecciones, luego φ(ℜ(C)) = ℜ(C') y el transporte respeta ∼;
  argumento directo, sin prueba mecánica (mismo estatus que Parte II punto 5 del desarrollo)

REALIZER_STABILITY_STATUS =
  NOT_ESTABLISHED_IN_GENERAL — preserva Q_REALIZER_UNIQUENESS_STATUS = UNVERIFIED y
  Q_REALIZER_INVARIANCE_STATUS = NOT_ESTABLISHED_IN_GENERAL (comité 014 D1): la primalidad
  genérica es [PLAUSIBLE, UNVERIFIED]; en el caso no primo, clases ∼ distintas producen
  clasificaciones distintas — tratado por QG3 en la Parte IX
```

---

# Parte IV — Clasificador robusto A6.4

## IV.1 Resolución previa de la simetría de intercambio de caras

**Opción S1 — etiquetas orientadas ("izquierda"/"derecha" físicamente distintas).**
Requiere una orientación canónica order-only del conjugado. No existe: la fuente reconoce el swap
como libertad legítima (Parte II punto 4 del desarrollo); comité 014 D4 rechazó explícitamente
como `AD_HOC` cualquier fijación de orientación ("no hay ninguna regla order-only propuesta en
ningún documento para romper este swap de forma no arbitraria"); y las coordenadas del generador
están prohibidas como fuente de orientación (II.1). **S1: RECHAZADA.**

**Opción S2 — etiquetas salvo swap (referencia no orientada `{L,R}`).**
Válida, pero su formalización ingenua ("etiquetas L/R módulo intercambio global") tiene un defecto
técnico que esta sesión identifica: comparar clasificaciones "salvo swap global" **a través de la
familia** `𝔄(C) × ℜ(C)` exige elegir un alineamiento de orientación por cada par `(A,ρ)`, y esa
elección es una optimización global no canónica (y, peor, sensible al sector oculto si se alinea
sobre `C` completo). La formalización correcta y canónica de S2 es **relacional**: en vez de
etiquetas por elemento, la relación binaria de **co-lateralidad** ("misma cara" / "caras
opuestas"), que es invariante bajo el swap de cada `(A,ρ)` POR PAR, sin ningún alineamiento. Es
exactamente la noción que el candidato BCE ya usa para comparar particiones ("relación de
co-pertenencia a una misma clase", `dev/PR003_C1_BCE_CLOSED_CANDIDATE.md` Parte IV,
generalización endosada por comité 013 D4). **S2 (forma relacional): ADOPTADA.**

**Opción S3 — pertenencia al objeto lateral robusto (sin distinguir cara).**
Definible como proyección de S2: `x` pertenece al "objeto lateral robusto" si participa en algún
par clasificado sin abstención. Pierde el contenido de dos caras (no distingue `SAME` de `OPP`),
que es precisamente lo que el eje (III) de asimetría necesita. **S3: REGISTRADA como proyección
diagnóstica más gruesa, no adoptada como forma principal.**

## IV.2 Definición formal del clasificador

Sea `C` con `𝔄(C)` (Parte II) y `ℜ(C)` (Parte III). Para un par no ordenado `{x,y} ⊆ C`, `x≠y`:

**Dominio de definición por par.** El conjunto de testigos que clasifican al par:

```text
D(x,y) := { (A,ρ) ∈ 𝔄(C) × ℜ(C) :  A = {a},  x,y ∈ spacelike(a),  x ≠ a ≠ y }
```

(Con la restricción a singletons de II.3, todo `x ∈ spacelike(a)` cae en `L_a ⊔ R_a`
exhaustivamente — "Resultado positivo 1" — así que pertenecer al dominio ⟹ estar clasificado
lateralmente; no hay clase `core` para `|A|=1`.)

**Veredicto por testigo.** Para `(A,ρ) ∈ D(x,y)`:

```text
σ_{A,ρ}(x,y) := SAME  si  {x,y} ⊆ L_a  ∨  {x,y} ⊆ R_a     (bajo Q_ρ)
                OPP   si  |{x,y} ∩ L_a| = 1
```

`σ` es invariante bajo `Q_ρ ↔ Q_ρ⁻¹` (el swap intercambia `L_a ↔ R_a` y preserva tanto
co-pertenencia como separación): **el swap queda resuelto por construcción, por testigo, sin
alineamiento global.** En esta representación, "acuerdo exacto" y "acuerdo salvo swap global"
coinciden — la distinción solo existe en la representación orientada, rechazada con S1.

**Clasificador robusto (forma par a par, total con abstención tipada):**

```text
χ_Q^rob(C, {x,y}) :=
  SAME_FACE      si D(x,y) ≠ ∅  ∧  ∀(A,ρ)∈D(x,y): σ_{A,ρ}(x,y) = SAME
  OPPOSITE_FACE  si D(x,y) ≠ ∅  ∧  ∀(A,ρ)∈D(x,y): σ_{A,ρ}(x,y) = OPP
  ABSTAIN(τ)     en cualquier otro caso, con motivo tipado τ:
    τ = EMPTY_FAMILY           si 𝔄(C) = ∅ ∨ ℜ(C) = ∅
    τ = NOT_DEFINED            si 𝔄(C),ℜ(C) ≠ ∅ ∧ D(x,y) = ∅
                               (par no definido por la construcción — p. ej. x,y timelike a
                               todo marcador admisible; el análogo |A|=1 de "no definida por
                               la tripartición provisional")
    τ = REALIZER_DISAGREEMENT  si ∃A, ∃ρ₁,ρ₂: σ_{A,ρ₁}(x,y) ≠ σ_{A,ρ₂}(x,y)
    τ = MARKER_DISAGREEMENT    si ∃ρ, ∃A₁,A₂: σ_{A₁,ρ}(x,y) ≠ σ_{A₂,ρ}(x,y)
    (τ puede contener ambos motivos; el motivo es metadato de auditoría, no parte del valor
    lógico — el codominio lógico es {SAME_FACE, OPPOSITE_FACE, ABSTAIN})
```

La condición de consenso cuantifica sobre `A ∈ 𝔄(C)` **y** `ρ ∈ ℜ(C)` simultáneamente, como exige
el brief. Los seis casos exigidos quedan distinguidos: acuerdo exacto y acuerdo salvo swap
(coinciden en la forma relacional — resuelto por construcción); desacuerdo entre marcadores
(`τ = MARKER_DISAGREEMENT`); desacuerdo entre realizadores (`τ = REALIZER_DISAGREEMENT`); familia
vacía (`τ = EMPTY_FAMILY`); no definido por la construcción (`τ = NOT_DEFINED`).

**Forma unaria derivada (etiquetas de cara como bloques, no como orientación).** Sea `G(C)` el
grafo con vértices `{x : ∃y, χ_Q^rob(C,{x,y}) ≠ ABSTAIN}` y aristas etiquetadas
`SAME`/`OPP` según `χ_Q^rob`. Una **componente conexa** de `G(C)` es **coherente** si no contiene
ningún ciclo con número impar de aristas `OPP` (condición de 2-coloreabilidad respetando `SAME`).
Entonces:

- en una componente coherente, los vértices se parten en dos bloques no orientados `{F₁, F₂}`
  (posiblemente uno vacío) — las "dos caras" locales, definidas salvo intercambio;
- `χ_Q^rob(C, x) :=` el bloque de `x` (como clase, sin orientación) si `x` pertenece a una
  componente coherente; `ABSTAIN(τ = INCOHERENCE)` si su componente contiene un ciclo impar de
  `OPP`.

**Dos honestidades estructurales nuevas registradas por esta formalización:**

1. **La coherencia no es automática.** Pares distintos pueden estar definidos por subconjuntos
   distintos de `𝔄(C)×ℜ(C)`; la relación robusta par a par puede ser globalmente incoherente
   (ciclo impar de `OPP`) aunque cada testigo individual sea una bipartición limpia. A6.4 declara
   abstención tipada (`INCOHERENCE`) en ese caso, en vez de forzar un coloreo. Ningún documento
   previo había identificado esta condición.
2. **"Dos caras" solo por componente.** Si `G(C)` tiene varias componentes coherentes, la
   referencia robusta es una **familia de bi-coloreos locales**, no un par global de caras. Que
   exista una estructura global de dos caras requiere conectividad del subgrafo no abstenido —
   condición order-only bien definida, **no evaluada** (sin ejecución). Esto acota honestamente lo
   que A6.4 puede afirmar incluso en el mejor caso.

## IV.3 Campos obligatorios

```text
ROBUST_CLASSIFIER_NAME =
  χ_Q^rob — clasificador lateral robusto por consenso marcador-realizador con abstención
  explícita, en forma relacional de co-lateralidad (A6.4)

ROBUST_CLASSIFIER_FORMAL_DEFINITION =
  Forma par a par (principal): χ_Q^rob(C,{x,y}) ∈ {SAME_FACE, OPPOSITE_FACE, ABSTAIN} por
  consenso universal de σ_{A,ρ}(x,y) sobre D(x,y) ⊆ 𝔄(C)×ℜ(C) (definición completa en IV.2).
  Forma unaria derivada: bloques no orientados {F₁,F₂} por componente coherente del grafo
  SAME/OPP; ABSTAIN(INCOHERENCE) en componentes con ciclo impar de OPP

ROBUST_CLASSIFIER_CODOMAIN =
  Pares: {SAME_FACE, OPPOSITE_FACE} ∪ {ABSTAIN} (con motivo tipado τ como metadato de
  auditoría). Unario: bloques de cara NO orientados por componente ∪ {ABSTAIN}. En ningún caso
  etiquetas orientadas L/R

ROBUST_CLASSIFIER_SWAP_HANDLING =
  S2 en forma relacional: σ es invariante por swap POR TESTIGO (co-lateralidad), eliminando todo
  alineamiento global de orientación. S1 rechazada (sin orientación canónica order-only; fijarla
  es AD_HOC per comité 014 D4). S3 registrada como proyección más gruesa no adoptada

ROBUST_CLASSIFIER_EMPTY_FAMILY_BEHAVIOR =
  ABSTAIN(EMPTY_FAMILY) para todo par — el clasificador permanece total; la familia vacía no es
  un fallo silencioso sino una abstención auditada

ROBUST_CLASSIFIER_MARKER_DISAGREEMENT_BEHAVIOR =
  ABSTAIN(MARKER_DISAGREEMENT) — ningún mecanismo de mayoría, peso o desempate entre marcadores
  (el desempate a un elemento está prohibido; Parte V del desarrollo Q recomienda exactamente
  la declaración multivaluada/robusta, nunca el desempate lexicográfico)

ROBUST_CLASSIFIER_REALIZER_DISAGREEMENT_BEHAVIOR =
  ABSTAIN(REALIZER_DISAGREEMENT) — la inestabilidad de realizador se ABSTIENE, no se excluye del
  dominio dentro de A6.4 (justificación en Parte IX; la exclusión de dominio QG3 de comité 014
  D5 se preserva para la ruta sin abstención, no se reabre)

ROBUST_CLASSIFIER_TOTAL_WITH_ABSTENTION =
  SÍ, condicional a que 𝔄(C) y ℜ(C) estén definidas: todo par de elementos distintos recibe
  exactamente un valor de {SAME_FACE, OPPOSITE_FACE, ABSTAIN}; toda situación no clasificable
  produce ABSTAIN tipado, nunca indefinición. La condicionalidad efectiva reside en el gate de
  𝔄(C) (bloqueado, II.3)
```

---

# Parte V — Pullback lateral

## V.1 Formalización

Comité 014 D6 adjudicó `Q_PULLBACK_DECISION = P1_LITERAL_INTERSECTION_FOR_LATERAL_TYPE`: para el
tipo "subconjunto lateral/espacial" (los `L_a`, `R_a` "y sus formas agregadas A6.3/A6.4", texto
literal de D6), el pullback es la intersección literal, no la down-closure. Se formaliza aquí
tipado componente a componente, extendido a la forma relacional de IV.2:

```text
PB^lat_O(R) := R ∩ O                                  (componente de tipo subconjunto lateral)
PB^lat_O(χ_Q^rob(C,·)) := restricción de χ_Q^rob(C,·) a pares {x,y} ⊆ O
                                                       (forma relacional par a par)
PB^lat_O({F₁,F₂}) := {F₁ ∩ O, F₂ ∩ O}                  (bloques unarios, componente a componente)
```

**Por qué down-closure cambiaría el tipo del objeto** (razonamiento de comité 014 D6, preservado):
`L_a`/`R_a` son conjuntos **extensionales completos** definidos por incomparabilidad espacial
respecto a `a`, no semillas de accesibilidad causal. `down_closure(C, L_a)` añadiría el pasado
causal completo de cada elemento de `L_a` — elementos en general **no spacelike a `a`** (incluso
timelike-anteriores a elementos de `L_a`, un tipo de relación excluido de la definición de
`L_a`/`R_a`) — convirtiendo silenciosamente una afirmación de incomparabilidad espacial en una de
accesibilidad causal: exactamente la conflación que la construcción de `Q` existe para evitar
(§7.5). La decisión de comité 013 D3 (down-closure) permanece correcta para el tipo
subconjunto-causal (`Max(C)`); no se reabre.

**Tratamiento de los casos exigidos:**

- **Referencia multivaluada** (familia `{Q(C,A,ρ)}` antes de agregar, forma A6.1): `PB^lat_O` se
  aplica miembro a miembro, produciendo la familia de restricciones. En A6.4 la multivaluación ya
  está absorbida por el consenso, así que el caso operativo es la restricción de `χ_Q^rob`.
- **Referencia salvo swap:** sin contenido adicional en la forma relacional — la co-lateralidad ya
  es swap-invariante, y la restricción de una relación swap-invariante es swap-invariante.
- **`ABSTAIN`:** se transporta, no se convierte: si `χ_Q^rob(C,{x,y}) = ABSTAIN(τ)` y
  `{x,y} ⊆ O`, entonces el objeto pullback contiene `ABSTAIN(τ)` para ese par. El pullback nunca
  convierte abstención en etiqueta ni etiqueta en abstención.

## V.2 Orden de operaciones: pullback vs. agregación

Las dos composiciones del brief, instanciadas:

- **Pullback-then-aggregate:** `Agg( PB^lat_O(Q(C,A,ρ)) : (A,ρ) )` — restringir cada testigo a
  `O` y tomar el consenso sobre pares de `O`.
- **Aggregate-then-pullback:** `PB^lat_O( Agg(Q(C,A,ρ) : (A,ρ)) )` — consenso sobre `C` completo
  y restricción posterior.

**Análisis de conmutación (no se declara sin justificar).** Para un par `{x,y} ⊆ O`:

1. En **aggregate-then-pullback**, el valor es el consenso de `σ_{A,ρ}(x,y)` sobre `D(x,y)`.
2. En **pullback-then-aggregate**, el valor es el consenso de los mismos `σ_{A,ρ}(x,y)` sobre el
   mismo `D(x,y)`: la restricción a `O` no altera ni el conjunto de testigos `(A,ρ)` (los
   marcadores siguen recorriendo `C` — son parte de la referencia sobre la completación, no del
   observado) ni el veredicto de cada testigo sobre un par fijo (σ es una función del par y del
   testigo, puntual en pares).

Como la agregación de A6.4 es **puntual en pares** y `PB^lat` es **restricción de pares**, ambas
composiciones coinciden sobre `O`: **conmutan para la forma relacional adoptada** [argumento
directo de dos líneas, documental, no verificado mecánicamente]. La conmutación **fallaría** para
una agregación orientada con alineamiento global de swap (el alineamiento óptimo sobre `C` puede
diferir del óptimo sobre `O`, y el alineamiento sobre `C` haría depender etiquetas observadas de
clasificaciones del sector oculto) — una razón adicional e independiente para la forma relacional
de IV.2. **Convención adoptada:** aggregate-then-pullback como orden canónico (la referencia
robusta es una propiedad de `C`; el pullback es su lectura sobre `O`), con la conmutación anotada
haciendo la elección inmaterial en la forma adoptada.

**Cualificación honesta:** la forma unaria derivada (bloques por componente coherente, IV.2) **no**
conmuta automáticamente: la coherencia y la conectividad de `G(C)` pueden diferir de las de su
restricción `G(C)|_O` (un ciclo impar puede pasar por elementos ocultos; una componente conexa en
`C` puede desconectarse en `O`). Para la forma unaria se fija por tanto: **los bloques se computan
sobre la restricción** `G(C)|_O` de la relación par a par ya pullback (pullback-then-blocks). Esto
mantiene la comparación E enteramente dentro de material observado y evita que la coherencia
dependa de pares con soporte oculto — al precio, registrado, de que los bloques observados pueden
ser más finos o más coherentes que los de `C` completo. No se declara conmutación donde no la hay.

## V.3 Campos obligatorios

```text
LATERAL_PULLBACK_FORMAL_DEFINITION =
  PB^lat_O(R) = R ∩ O por componente de tipo lateral (comité 014 D6, P1, preservado); en la
  forma relacional: restricción de χ_Q^rob a pares {x,y} ⊆ O; ABSTAIN se transporta con su tipo,
  nunca se convierte

LATERAL_PULLBACK_ORDER_OF_OPERATIONS =
  Canónico: aggregate-then-pullback para la relación par a par (conmuta con
  pullback-then-aggregate en la forma adoptada — argumento en V.2). Para los bloques unarios:
  pullback-then-blocks (los bloques y su coherencia se computan sobre G(C)|_O), decisión fijada
  precisamente porque ahí la conmutación NO vale

LATERAL_PULLBACK_COMMUTATION_STATUS =
  CONMUTA_PARA_LA_FORMA_RELACIONAL (agregación puntual en pares ∘ restricción de pares;
  argumento directo, documental, no mecánico); NO_CONMUTA_EN_GENERAL para agregaciones
  orientadas con alineamiento global ni para la derivación de bloques unarios (coherencia y
  conectividad no se preservan bajo restricción) — resuelto por convención explícita, no por
  declaración de conmutación

LATERAL_PULLBACK_SWAP_STATUS =
  Sin interacción: la co-lateralidad es swap-invariante por testigo y la restricción preserva
  esa invariancia; ningún alineamiento de orientación interviene en el pullback

LATERAL_PULLBACK_ABSTENTION_STATUS =
  ABSTAIN(τ) se restringe como valor de primera clase con su motivo; el pullback no reclasifica;
  los motivos τ sobreviven al pullback como metadato de auditoría
```

---

# Parte VI — E robusto

Comparación de dos completaciones observacionalmente equivalentes `C_A, C_B ∈ 𝔄(O)` con
`C_A|_O = C_B|_O = O` (mismo carrier y misma relación inducida — el nivel de equivalencia fijado
en `dev/PR003_C1_BCE_CLOSED_CANDIDATE.md` Parte IV y `OBSERVATIONAL_EQUIVALENCE_STATUS = CLOSED`,
comité 013 D4), cuando la regla permite abstención. Notación: `χ_X := PB^lat_O(χ_Q^rob(C_X,·))`
(relación par a par sobre `O`), `Dom(χ_X) := { {x,y} ⊆ O : χ_X({x,y}) ≠ ABSTAIN }`.

```text
E_STRICT_FORMAL_DEFINITION =
  E-strict(C_A,C_B) :⟺ ∃{x,y} ∈ Dom(χ_A) ∩ Dom(χ_B) :  χ_A({x,y}) ≠ χ_B({x,y})
  (ambas completaciones clasifican el par SIN abstención y las clasificaciones son incompatibles
  — una dice SAME_FACE, la otra OPPOSITE_FACE. Forma par a par: swap-safe por construcción, sin
  necesidad de alinear orientaciones entre completaciones — es la generalización directa del
  E-set de particiones por co-pertenencia del candidato BCE)

E_DOMAIN_FORMAL_DEFINITION =
  E-domain(C_A,C_B) :⟺ Dom(χ_A) ≠ Dom(χ_B)
  (cambia el dominio de clasificación no abstencionista)

E_ABSTENTION_FORMAL_DEFINITION =
  E-abstention(C_A,C_B) :⟺ ∃{x,y} ⊆ O :  ({x,y} ∈ Dom(χ_A) ∧ χ_B({x,y}) = ABSTAIN) ∨
                                          ({x,y} ∈ Dom(χ_B) ∧ χ_A({x,y}) = ABSTAIN)
  (una clasifica, la otra se abstiene; para dominios finitos, E-abstention ⟺ E-domain — misma
  relación testigo↔conjunto que E-element ⟺ E-set en el candidato BCE; se registran como dos
  formas del mismo predicado, no como dos predicados independientes)

E_SET_FORMAL_DEFINITION =
  E-set(C_A,C_B) :⟺ χ_A ≠ χ_B como funciones tipadas sobre los pares de O
  (difieren las referencias robustas completas, incluyendo dominio y valores;
  E-set ⟺ E-strict ∨ E-domain. Los motivos τ NO cuentan para ≠ — son metadato de auditoría, no
  contenido de la referencia)

E_PRIMARY_FOR_DIAGNOSTIC_Q =
  E_STRICT — es el único predicado donde ambas completaciones hacen AFIRMACIONES positivas
  incompatibles sobre el mismo par observado. La abstención no es una afirmación: que C_A
  clasifique donde C_B se abstiene (E-domain/E-abstention) es DEGRADACIÓN DIAGNÓSTICA
  (sensibilidad de la clasificabilidad al sector oculto — información diagnóstica real sobre
  robustez), no una contradicción lógica entre referencias. E-set se usa solo como agregado de
  reporte. Esta adjudicación es la extensión natural, con abstención, del
  CLAUSE_E_PRIMARY_PREDICATE = E-set del candidato BCE: allí sin abstención E-set y el testigo
  puntual coinciden en fuerza; aquí la abstención obliga a separar incompatibilidad (E-strict)
  de degradación (E-domain)

E_COUNTS_AS_PHYSICAL_INCOMPATIBILITY = NO
  (sin excepción: ni E-strict. Regla de no-inferencia entre niveles de comité 012 §3, citada en
  el candidato BCE Parte V: incompatibilidad lógica en 𝔄_C1(O) no constituye
  no-identificabilidad física sin pertenencia establecida a una clase físicamente interpretable
  — y 𝔄_Schw carece de caracterización intrínseca. Una diferencia de abstención NUNCA equivale
  a dos horizontes físicos distintos; ni siquiera un E-strict verdadero lo haría hoy.
  PHYSICAL_IDENTIFIABILITY_STATUS = NOT_ESTABLISHED, sin cambio)
```

---

# Parte VII — No trivialidad y criterio de abandono

## VII.1 Tipología conceptual de la abstención (sin ejecutar datos)

| Tipo | Definición conceptual | Lectura |
|:---|:---|:---|
| Abstención legítima | `ABSTAIN(MARKER_DISAGREEMENT)` localizado en pares cuya clasificación lateral depende genuinamente de qué membrana candidata se tome (p. ej. pares cerca del "cuello", el mecanismo de intercalado §7.4.1) | Contenido diagnóstico real: mide el grosor efectivo de la zona de no consenso |
| Abstención estructural inevitable | `ABSTAIN(NOT_DEFINED)` (par timelike a todo marcador admisible) y `ABSTAIN(EMPTY_FAMILY)` | No es información sobre la membrana; debe EXCLUIRSE del numerador y denominador de la métrica de colapso para no confundir "no definido" con "sin consenso" |
| Colapso a abstención casi total | `ABSTAIN(MARKER_DISAGREEMENT ∨ REALIZER_DISAGREEMENT)` en casi todos los pares elegibles | Criterio de abandono (4) de comité 014 D7 |
| Regla no trivial | Fracción no evanescente de pares elegibles con `SAME_FACE`/`OPPOSITE_FACE`, organizada en una estructura de dos bloques no degenerada | Lo que A6.4 debe demostrar para sobrevivir |

## VII.2 Mecanismo de colapso identificado para la familia sin gate `𝔄₀` (conceptual, sin ejecución)

`[CONCEPTUAL, UNVERIFIED — razonamiento con las coordenadas auxiliares (τ,ξ) de §7.4.1, "sólo
para razonar"]`. Bajo `𝔄₀(C)` (todos los singletons no extremales), para un par spacelike
`{x,y}`: un marcador `a` con ambos en `spacelike(a)` da `OPP` exactamente cuando `a` está
Q-intercalado entre `x` e `y`, y `SAME` cuando no lo está. En un sprinkling genérico, un par con
separación lateral apreciable tiene **ambos** tipos de testigo (marcadores dentro y fuera de su
hueco Q) ⟹ `ABSTAIN(MARKER_DISAGREEMENT)`. Los únicos supervivientes conceptuales son:
`SAME_FACE` para pares sin ningún marcador admisible Q-intercalado (vecindad lateral inmediata) y
`OPPOSITE_FACE` para pares tales que **todo** marcador que los define está entre ellos (pares de
extremos laterales del parche). Es decir: **la referencia degeneraría en "adyacencia lateral +
extremidad lateral", no en dos caras de una membrana** — colapso funcional por abstención en la
zona de interés. Este es el mismo mecanismo de intercalado que refutó la bipartición exhaustiva
(§7.4.1) y que comité 014 D3 ya señaló para A6.3, aquí propagado a A6.4-sin-gate.

**Consecuencias, con dos cautelas obligatorias:** (i) esto **no** activa hoy el criterio de
abandono (4) — es un argumento conceptual no ejecutado sobre la instanciación **sin gate**, no una
demostración sobre "la práctica totalidad de los casos" para toda instanciación de A6.4; (ii) sí
establece que el gate de II.3 no es un refinamiento opcional sino **constitutivo**: sin él, A6.4
tiene un mecanismo de colapso documentado. Ambas cosas se elevan al comité (Parte X).

## VII.3 Criterio precomprometido futuro (propuesto, no adoptado, no evaluado)

```text
ABSTENTION_RATE_METRIC =
  α(C) := |{ pares elegibles con ABSTAIN(MARKER_DISAGREEMENT ∨ REALIZER_DISAGREEMENT) }|
          / |{ pares elegibles }|
  donde "par elegible" := {x,y} ⊆ O con D(x,y) ≠ ∅ (definido por al menos un testigo). Las
  abstenciones estructurales (NOT_DEFINED, EMPTY_FAMILY) quedan FUERA de numerador y
  denominador por diseño — medir el colapso, no la cobertura

ABSTENTION_RATE_DENOMINATOR =
  Pares elegibles de O (no todos los pares de O, no elementos): la métrica es par a par porque
  el clasificador lo es

ABSTENTION_RATE_SCOPE =
  Sobre el observado O (post-pullback), que es donde la regla diagnóstica opera; por completación
  y, en uso futuro, agregada sobre un ensemble PRE-DECLARADO — nunca elegido tras ver α

NONTRIVIALITY_MINIMUM_REQUIREMENT =
  Forma (no valor): (i) α(C) acotada lejos de 1 en el régimen genérico declarado; (ii) el
  subgrafo no abstenido G(C)|_O contiene al menos una componente coherente con DOS bloques de
  más de un elemento cada uno (estructura de dos caras no degenerada — excluye el colapso a
  "adyacencia + extremidad" de VII.2 aunque α fuese favorable); (iii) las clasificaciones no
  abstenidas no se reducen a pares Q-adyacentes

ABANDONMENT_THRESHOLD_CANDIDATE =
  Forma propuesta, sin valor numérico (no existe base documental para un porcentaje — comité 014
  D7 solo registra "abstención ≈100%"): declarar colapso si α(C) → 1 en el régimen genérico en
  el sentido preciso de que la fracción de pares elegibles clasificados sea compatible con la
  producida solo por adyacencia lateral (el suelo estructural de VII.2). El valor operativo
  exacto deberá fijarse ANTES de cualquier evaluación, por comité, sobre una base declarada

THRESHOLD_STATUS = PROPOSED_NOT_ADOPTED
```

**Criterios de abandono de comité 014 D7, preservados sin cambio:** (1) imposibilidad genérica de
selección de `A` para cualquier forma de A6; (2) inestabilidad genérica de realizador (no
excepcional); (3) circularidad residual no eliminable en ningún criterio de admisibilidad;
(4) abstención ≈100% de A6.4 en el régimen genérico. Aportes de esta sesión a su evaluación
futura: el canal de circularidad residual de II.1 es material para (3) — con mitigación M1
propuesta, no una demostración de ineliminabilidad; el mecanismo VII.2 es material para (4) —
restringido a la instanciación sin gate. `Q_CURRENTLY_MEETS_ABANDONMENT_CRITERIA = NO` se
preserva: ninguno de los cuatro está demostrado.

---

# Parte VIII — Auditoría de invariancia

Isomorfismo `φ : C ≅ C'` que preserva el observado identificado (`φ|_O = id_O` sobre el carrier
etiquetado de `O`, la convención `ι_C` del candidato BCE). Recorrido conceptual, sin prueba
mecánica — por instrucción del brief, no se usa `ESTABLISHED` donde solo hay plausibilidad
documental:

1. **Transporte de marcadores.** `Min/Max` y las firmas 3 y 5 son invariantes de isomorfismo
   (auditadas en II.2), luego `φ({a}) ∈ 𝔄(C') ⟺ {a} ∈ 𝔄(C)` para `𝔄₀` y para todo gate construido
   con esas firmas. Condicional al gate (que no existe cerrado).
2. **Transporte de realizadores.** `ρ = (L_U,L_V) ↦ φ(ρ) = (φ(L_U), φ(L_V))` biyecta `ℜ(C)` con
   `ℜ(C')` y respeta `∼` (Parte III).
3. **Transporte de la tripartición.** Dado `(A,ρ)` fijo: `φ(L_a) = L_{φ(a)}`, `φ(R_a) = R_{φ(a)}`
   bajo `φ(ρ)`, salvo swap — es exactamente la afirmación de la fuente (Parte II punto 5 del
   desarrollo), que ella misma marca como "afirmación conceptual del dev note, no verificada
   mecánicamente".
4. **Tratamiento del swap.** La forma relacional es swap-invariante por testigo (IV.2); el
   transporte no necesita alinear orientaciones — la fuente clásica de fallo de invariancia en
   objetos "salvo swap" queda eliminada por construcción.
5. **Transporte del pullback.** `φ|_O = id_O` ⟹ `φ(R ∩ O) = φ(R) ∩ O`; la restricción de pares
   conmuta con `φ` trivialmente.
6. **Transporte de abstenciones.** Los motivos `τ` están definidos por condiciones invariantes
   (vacuidad de familias, vacuidad de `D(x,y)`, existencia de testigos discrepantes), luego
   `χ_Q^rob(C',{x,y}) = χ_Q^rob(C,{x,y})` para pares de `O`, motivo incluido — condicional a 1-3.
7. **Transporte del predicado E.** E-strict/E-domain/E-abstention/E-set están definidos sobre
   `χ_X` restringidas a `O` con `φ|_O = id`, luego son invariantes si 1-6 lo son.

```text
MARKER_TRANSPORT_STATUS = PLAUSIBLE_BY_CONSTRUCTION_CONDITIONAL_ON_GATE
  (invariante para 𝔄₀ y para gates de firmas invariantes; el gate no existe cerrado — no
  puede declararse más)
REALIZER_TRANSPORT_STATUS = PLAUSIBLE_BY_CONSTRUCTION_NOT_MECHANICALLY_VERIFIED
Q_OBJECT_TRANSPORT_STATUS = PLAUSIBLE_DOCUMENTALLY_NOT_MECHANICALLY_VERIFIED
  (estatus heredado literal de la fuente, Parte II punto 5 del desarrollo Q)
ROBUST_CLASSIFIER_INVARIANCE_STATUS = PLAUSIBLE_CONDITIONAL_ON_1_TO_3_NOT_ESTABLISHED
PULLBACK_INVARIANCE_STATUS = PLAUSIBLE_BY_CONSTRUCTION (única pieza con argumento trivial
  directo — intersección/restricción con O fijo — aun así no mecánicamente verificada)
E_INVARIANCE_STATUS = PLAUSIBLE_CONDITIONAL_ON_UPSTREAM_NOT_ESTABLISHED
```

---

# Parte IX — Relación con G1 y QG3

**Preservado:** `G1_IS_ONLY_PARTIALLY_SUFFICIENT_FOR_Q` — hallazgo literal de la Parte VII punto 7
del desarrollo Q (`Q_COMPATIBLE_WITH_G1 = PARTIALLY_SUFFICIENT`): un oculto que satisface G1
puede, a través de sus relaciones con otros ocultos, alterar la estructura de incomparabilidad
global y por tanto el realizador y `Q`, sin tocar `O` causalmente. Ni G1 ni la decisión de comité
013 D1 se reabren.

**QG3, formalización conceptual (comité 014 D5, instanciada con el pullback lateral de D6):**

```text
QG3(C,A) :⟺ ∀ρ₁,ρ₂ ∈ ℜ(C):  PB^lat_O(Q(C,A,ρ₁)) = PB^lat_O(Q(C,A,ρ₂))
```

donde la igualdad, en la forma relacional de este documento, es igualdad de las relaciones de
co-lateralidad restringidas a `O` (swap-safe sin cláusula "módulo swap" adicional: la reversión
global es `∼`-interna, Parte III).

**Decisión de papel (las tres opciones del brief, adjudicadas):**

- *¿Requisito de pertenencia al dominio?* Es la opción de comité 014 D5 para la ruta `𝔄_Q(O)`
  (regla sin abstención): **se preserva ahí, no se reabre**. Pero adoptarla TAMBIÉN dentro de
  A6.4 excluiría del dominio exactamente las completaciones difíciles, encogiendo el denominador
  de `α(C)` y haciendo la regla **artificialmente favorable** — el riesgo que el brief ordena
  evitar.
- *¿Parte del clasificador robusto?* Ya lo es implícitamente: la cuantificación `∀ρ ∈ ℜ(C)` de
  IV.2 evalúa la estabilidad de realizador par a par.
- *¿Genera abstención cuando falla?* **Sí — opción adoptada para A6.4.** El fallo de QG3 en un
  par produce `ABSTAIN(REALIZER_DISAGREEMENT)` localizado, auditable y contabilizado en `α(C)`,
  en vez de desaparecer por exclusión de dominio. La inestabilidad se MIDE, no se oculta. QG3
  como predicado global queda entonces caracterizado dentro de A6.4:
  `QG3(C,A) ⟺ ningún par de O recibe ABSTAIN(REALIZER_DISAGREEMENT) bajo el marcador A` —
  formalizable en principio (cuantificación sobre objetos finitos), no implementado, no ejecutado.

```text
QG3_ROLE =
  Dentro de A6.4: GENERADOR_DE_ABSTENCIÓN (vía la cuantificación ∀ρ∈ℜ(C) del clasificador, con
  motivo tipado REALIZER_DISAGREEMENT). Fuera de A6.4: se preserva sin reabrir
  Q_GROUNDEDNESS_DECISION = QG3_ADOPTED_AS_DOMAIN_EXCLUSION_SUPPLEMENT_TO_G1 (comité 014 D5)
  para la ruta sin abstención — dos usos del mismo predicado, declarados explícitamente para
  evitar doble contabilidad

QG3_FORMAL_RULE =
  ∀ρ₁,ρ₂ ∈ ℜ(C): PB^lat_O(Q(C,A,ρ₁)) = PB^lat_O(Q(C,A,ρ₂)) (igualdad de relaciones de
  co-lateralidad sobre pares de O; requerida exactamente cuando se pretende clasificar SIN
  abstención)

QG3_FAILURE_BEHAVIOR =
  ABSTAIN(REALIZER_DISAGREEMENT) par a par — localizado donde la orientación de módulos no
  primos afecta al par, no exclusión de C completa. Justificación anti-sesgo: la exclusión de
  dominio dentro de A6.4 construiría una subclase artificialmente favorable (denominador de α
  encogido exactamente en los casos difíciles); la abstención mantiene el caso difícil dentro de
  la contabilidad del criterio de abandono (2)

QG3_RELATION_TO_A_Q =
  𝔄_Q(O) (comité 014 D4: dim_DM≤2 ∧ 𝔄(C)≠∅ ∧ QG3) queda como el dominio de la eventual ruta SIN
  abstención; A6.4 opera sobre el dominio más amplio {C ∈ 𝔄_C1(O) : dim_DM(C)≤2} absorbiendo las
  violaciones de QG3 como abstenciones — sobre 𝔄_Q(O), A6.4 no produce ningún
  ABSTAIN(REALIZER_DISAGREEMENT) por construcción

QG3_RELATION_TO_A_C1 =
  Ninguna condición de QG3 se añade a 𝔄_C1(O) (clase causal mínima B1∧B2∧B3∧G1∧finitud,
  comités 012/013 — intacta); QG3 es específico de reglas tipo Q, no de la clase

QG3_RELATION_TO_A_SCHW =
  Ortogonal por definición (𝔄_Schw es por procedencia del generador, comité 012). Se ESPERA que
  las salidas del generador satisfagan QG3 vía primalidad genérica — [PLAUSIBLE, UNVERIFIED],
  §7.4.1 — pero no está establecido; G3 (futuro + no-retorno) sigue
  RECOMMENDED_FOR_SCHW_ONLY, sin relación con QG3 (comité 014 D5, QG4: ortogonal)
```

---

# Parte X — Resultado de la especificación

## X.1 Estado alcanzado

De los cuatro componentes de A6.4: el **clasificador robusto** queda cerrado como esquema (forma
relacional swap-safe, abstención tipada total, coherencia y conectividad identificadas como
condiciones nuevas — IV); el **pullback lateral** queda cerrado (P1 heredado de comité 014 D6,
orden de operaciones adjudicado con análisis de conmutación — V); **E** queda tipado
(E-strict/E-domain/E-abstention/E-set con adjudicación de qué cuenta como incompatibilidad — VI);
la **familia de realizadores** queda definida condicionalmente (III). El componente restante — la
**familia de marcadores** — queda en esquema con firmas adjudicadas, mitigación M1 y forma de
gate, pero su instanciación no trivial está bloqueada por ausencia de base principiada para el
umbral del gate, y la instanciación sin gate tiene un mecanismo de colapso documentado (VII.2).

El estado es por tanto, de los seis permitidos:

```text
A6_4_REQUIRES_MARKER_DEFINITION
```

No se alcanza (ni podría alcanzarse) ningún estado de referencia física.

## X.2 Próxima fase

La auditoría de casos pequeños **no** se autoriza: de sus cinco precondiciones, falla la primera
(la familia de marcadores no está completamente definida — solo su esquema). Elección única:

```text
COMMITTEE_REVIEW_OF_A6_4_SPEC
```

Materia mínima para esa revisión: (i) la restricción de `𝔄(C)` a singletons (II.3) y el estatus
de la extensión bloqueada `|A|≥2`; (ii) el canal de circularidad residual de II.1 y la mitigación
M1 — material para el criterio de abandono (3); (iii) el mecanismo de colapso VII.2 — material
para el criterio (4), restringido a `𝔄₀`; (iv) la adopción de la forma relacional S2 y la
abstención tipada; (v) QG3 como generador de abstención dentro de A6.4 (IX) manteniendo la
exclusión de dominio de comité 014 D5 para la ruta sin abstención; (vi) si el bloqueo del gate
justifica activar la posición de repliegue QG5 registrada por comité 014 D5, o una ronda más.

No se autoriza Alloy 003 ni Lean en ninguna modalidad.

---

# Bloque normativo final

```text
DOCUMENT_ID = PR003_Q_A6_4_ROBUST_ABSTENTION_SPEC

Q_DISPOSITION_INHERITED = Q_DIAGNOSTIC_CANDIDATE_ONLY

MARKER_FAMILY_STATUS = BLOCKED_NONTRIVIAL_GATE_UNDEFINED
  (𝔄₀(C) = singletons no extremales: cerrada, canónica, total, no vacía, PASS-independiente —
  pero conjeturalmente trivializante por el mecanismo de colapso VII.2; ningún gate no trivial
  tiene base principiada para su umbral)
MARKER_FAMILY_FORMAL_DEFINITION =
  𝔄(C) = { {a} : a ∈ C ∖ (Min(C) ∪ Max(C)), Gate(a) } con Gate construido solo con firmas
  ADMISSIBLE_COMPONENT (perfil de incomparabilidad, grados de cobertura) bajo el cierre
  composicional II.1, reteniendo clases de firma completas, sin desempate a un único elemento;
  instanciación base 𝔄₀ = forma sin Gate; solo marcadores de un elemento (|A|≥2 = extensión
  bloqueada por TRIPARTITION_STATUS = PROVISIONAL, TWO_FACE_LEMMA_STATUS = OPEN y N(A) sin fijar)
MARKER_FAMILY_PASS_INDEPENDENCE = ENFORCED_BY_CONSTRUCTION
  (O(i) y su refinamiento sig_↑ excluidos — REJECTED_CIRCULAR; regla de cierre composicional
  sobre combinaciones de firmas; mitigación M1 del canal residual sobre minimales identificado
  esta sesión; verificación formal de ausencia de todo canal residual NO establecida)

REALIZER_FAMILY_STATUS = DEFINED_CONDITIONALLY_ON_DIM_LE_2
  (existencia CONDITIONALLY_ESTABLISHED vía Prop. 7.3 / Dushnik-Miller; unicidad salvo swap
  UNVERIFIED — primalidad modular [PLAUSIBLE, UNVERIFIED]; no se asume unicidad en ningún punto)
REALIZER_FAMILY_FORMAL_DEFINITION =
  ℜ(C) = { (L_U,L_V) : órdenes lineales con L_U ∩ L_V = P_C } (notación nueva de este
  documento), con equivalencia ρ ∼ ρ' ⟺ Q_ρ ∈ {Q_{ρ'}, (Q_{ρ'})⁻¹}; el intercambio del par
  (L_U,L_V) ↦ (L_V,L_U) realiza el swap global de caras y es ∼-interno

ROBUST_CLASSIFIER_STATUS = CLOSED_SCHEMA_CONDITIONAL_ON_MARKER_FAMILY
  (totalidad con abstención, tipado de motivos, coherencia y conectividad cerrados como esquema;
  no evaluable mientras el gate de 𝔄(C) no exista)
ROBUST_CLASSIFIER_FORMAL_DEFINITION =
  χ_Q^rob(C,{x,y}) = SAME_FACE / OPPOSITE_FACE si TODOS los testigos (A,ρ) ∈ D(x,y) ⊆ 𝔄(C)×ℜ(C)
  coinciden en σ_{A,ρ}(x,y) (co-lateralidad bajo Q_ρ respecto del marcador), con D(x,y) ≠ ∅;
  ABSTAIN(τ) en otro caso, τ ∈ {EMPTY_FAMILY, NOT_DEFINED, MARKER_DISAGREEMENT,
  REALIZER_DISAGREEMENT, INCOHERENCE}; forma unaria derivada: bloques no orientados por
  componente coherente (sin ciclo impar de OPP) del grafo SAME/OPP restringido a O
ROBUST_CLASSIFIER_CODOMAIN =
  {SAME_FACE, OPPOSITE_FACE, ABSTAIN} sobre pares no ordenados (motivo τ como metadato de
  auditoría); bloques de cara no orientados sobre elementos — nunca etiquetas orientadas L/R
ROBUST_CLASSIFIER_SWAP_HANDLING =
  S2 en forma relacional de co-lateralidad, swap-invariante POR TESTIGO, sin alineamiento
  global de orientación; S1 rechazada (orientación canónica order-only inexistente; fijarla =
  AD_HOC, comité 014 D4); S3 registrada como proyección más gruesa no adoptada
ROBUST_CLASSIFIER_ABSTENTION_RULE =
  Consenso universal sobre 𝔄(C) × ℜ(C): cualquier desacuerdo entre marcadores o entre
  realizadores, familia vacía, par no definido, o incoherencia de coloreo ⟹ ABSTAIN tipado;
  la abstención es salida válida de primera clase, nunca fallo silencioso, y sobrevive al
  pullback sin reclasificarse

LATERAL_PULLBACK_STATUS = CLOSED_INHERITED_FROM_COMMITTEE_014_D6_EXTENDED_TO_PAIR_FORM
LATERAL_PULLBACK_FORMAL_DEFINITION =
  PB^lat_O(R) = R ∩ O por componente de tipo lateral (P1); en forma relacional: restricción de
  χ_Q^rob a pares {x,y} ⊆ O; down-closure excluida porque inyectaría elementos no spacelike al
  marcador, convirtiendo incomparabilidad espacial en accesibilidad causal (tipo distinto)
LATERAL_PULLBACK_ORDER_OF_OPERATIONS =
  Aggregate-then-pullback (canónico; conmuta con pullback-then-aggregate para la forma
  relacional — argumento V.2); bloques unarios computados post-pullback sobre G(C)|_O
  (pullback-then-blocks) porque la coherencia/conectividad NO conmutan con la restricción —
  conmutación no declarada donde no vale

E_STRICT_STATUS = TYPED_CLOSED_NOT_EVALUABLE
  (definición cerrada; inevaluable mientras 𝔄(C) esté bloqueada — ningún par de completaciones
  ha sido evaluado; única forma que cuenta como incompatibilidad lógica)
E_ABSTENTION_STATUS = TYPED_CLOSED_DIAGNOSTIC_DEGRADATION_ONLY
  (equivalente a E-domain en dominios finitos; NO cuenta como incompatibilidad lógica — la
  abstención no es una afirmación)
E_PRIMARY_FOR_DIAGNOSTIC_Q = E_STRICT
E_COUNTS_AS_PHYSICAL_INCOMPATIBILITY = NO

QG3_ROLE = ABSTENTION_GENERATOR_WITHIN_A6_4_DOMAIN_EXCLUSION_PRESERVED_FOR_NON_ABSTENTION_PATH
QG3_FAILURE_BEHAVIOR = ABSTAIN(REALIZER_DISAGREEMENT) localizado par a par
  (no exclusión de dominio dentro de A6.4 — evita construir una subclase artificialmente
  favorable encogiendo el denominador de abstención; la decisión de comité 014 D5 sobre 𝔄_Q(O)
  se preserva sin reabrir para la ruta sin abstención)

ISOMORPHISM_INVARIANCE_STATUS = PLAUSIBLE_BY_CONSTRUCTION_NOT_ESTABLISHED
  (los siete pasos de transporte recorridos, Parte VIII; ninguno con prueba mecánica; el eslabón
  Q-objeto hereda "afirmación conceptual, no verificada mecánicamente" de la fuente)
NONTRIVIALITY_STATUS = UNRESOLVED_WITH_DOCUMENTED_COLLAPSE_MECHANISM_FOR_UNGATED_FAMILY
  (mecanismo VII.2 [CONCEPTUAL, UNVERIFIED] para 𝔄₀; ninguna instanciación evaluada; el gate es
  constitutivo, no opcional)
ABSTENTION_THRESHOLD_STATUS = PROPOSED_NOT_ADOPTED

ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED
LEAN_AUTHORIZATION_STATUS = NOT_AUTHORIZED
PHYSICAL_IDENTIFIABILITY_STATUS = NOT_ESTABLISHED

NEXT_REVIEW_REQUIRED =
  Revisión de comité de esta especificación (materia mínima en X.2): restricción a singletons;
  canal de circularidad residual II.1 + mitigación M1 (material para criterio de abandono 3);
  mecanismo de colapso VII.2 (material para criterio 4, restringido a 𝔄₀); forma relacional S2 y
  abstención tipada; QG3 como generador de abstención; disposición del bloqueo del gate (ronda
  adicional vs. activación del repliegue QG5 registrado por comité 014 D5)
NEXT_AUTHORIZED_ACTION = COMMITTEE_REVIEW_OF_A6_4_SPEC
NEXT_FORBIDDEN_ACTIONS =
  Alloy 003 en cualquier modalidad | Lean en cualquier modalidad | simulaciones, sprinklings,
  enumeraciones o búsquedas de contraejemplos | análisis estadístico | implementación de código
  para Q, 𝔄(C), ℜ(C), χ_Q^rob o PB^lat | auditoría de casos pequeños mientras la familia de
  marcadores no esté completamente definida (precondición fallida, X.2) | fijar el umbral del
  Gate o cualquier umbral de abstención sin base declarada y previa a toda evaluación | tratar
  esta especificación como referencia física adoptada o como desarrollo de una | usar la firma
  del filtro principal o cualquier combinación de firmas que determine O(i) | desempate a un
  único marcador | fijar la orientación del swap | reabrir Q_DISPOSITION, QG3 (D5), P1 (D6) o
  los criterios de abandono (D7) | commit o push sin autorización explícita del PI

OVERALL_A6_4_STATUS = A6_4_REQUIRES_MARKER_DEFINITION
```
