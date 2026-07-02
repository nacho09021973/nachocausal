# PR-003 — C1 completion-class definitions (draft for committee 012)

> Paso R4 ordenado por `docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md`
> §9 step 2 y reiterado por `docs/comite/comite_decision_011_patch-ensemble-architecture.md` §9 R4.
> **Draft conceptual, no un resultado.** Definiciones operativas para que comité 012 decida si la
> pregunta C1 está suficientemente especificada — no se afirma aquí que C1 exista, sea consistente,
> o que la no-identificabilidad física esté establecida o refutada. No se ejecutaron sprinklings,
> no se tocaron thresholds, no se modificó ningún selector. Sin commit ni push.

---

## 1. Scope and non-goals

- C1 es una **clase candidata de completaciones** (un conjunto de restricciones a especificar),
  no una afirmación de existencia. Este documento no prueba que 𝔄 (la clase admisible) sea
  no vacía, ni que dos completaciones distintas satisfaciendo 𝔄 existan.
- Este documento **define términos**; no prueba identificabilidad ni no-identificabilidad física.
- No incluye Schwarzschild 2+1 ni 3+1. Esas rutas están fuera de alcance en la fase actual
  (`comite_decision_011` §8, BLOCK-4: "hard scope violation"; §10: `RECOMMEND_DO_NOT_PROCEED`
  incondicional sobre 2+1/3+1).
- No repara el `FAIL` de `boundary-bracket` (§6 abajo). `R3` (`dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md`)
  localiza la degradación de cobertura en el localizador con confianza media; este documento no
  reabre ni reinterpreta ese veredicto.
- No usa "Variant A" / "Bruno" como evidencia presente en este repositorio. Se confirmó
  (sesión anterior, R2) que esa formalización pertenece a un checkout local distinto asociado a
  `xinhjBrant/mathlib4`, commit no publicado `f008ff9931c6d541d0dc819eef11f93479f6cb96`, y **no
  fue trasladada** a `nachocausal`. `R2_STATUS = BLOCKED_WRONG_REPOSITORY_CONTEXT` se mantiene sin
  cambios. Ninguna cláusula de este documento depende de esa prueba externa.

---

## 2. Observable base

**Poset observado (`C`):** el causal set finito producido por `generator.py` para el parche
1+1D Eddington–Finkelstein sellado (`t*∈[0,6]`, `r∈[0.1,1.3]`, `R_S=0.5`, `M=0.25`,
`thresholds.py:37-43`). Concretamente, la matriz booleana de pasado (`past_matrix`, orden causal
estricto, transitivamente cerrada) sobre los elementos sembrados — no las coordenadas `(t*, r)`
que la generaron.

**Qué información permanece visible:** únicamente la relación de orden entre los elementos
sembrados (`C`, la matriz `past_matrix`) y cualquier cantidad derivable de ella sin coordenadas
(future-volume `O(i)=|future(i)|`, alturas `L_past`/`L_fut`, antichains, intervalos). Las
coordenadas `(t*, r)` de la incrustación (`emb`) permanecen ocultas al observable; solo puntúan
(regla fundacional, `CLAUDE.md`).

**Elemento/subconjunto/propiedad objetivo:** no está cerrado por este documento. Candidatos en
juego en el repo: (i) el conjunto de fronteras `boundary-bracket` (frentes `L_past`-nivel con
`|F|≥NMIN`, ver §6); (ii) el conjunto interfaz `H[C;R]` del selector C1 (`nachocausal/c1_selector.py`,
`R=Max(C)`, actualmente trivial: `NO_INTERFACE` para todo poset finito no vacío). Cuál de estos (u
otro) es el "target property" de C1 es precisamente uno de los **REQUIRED** por cerrar (§3(c)).

**Distinciones que NO deben tratarse como equivalentes** (obligación explícita del brief):

| Noción | Qué fija | Ejemplo en el repo |
|---|---|---|
| Mismo carrier observado | El conjunto subyacente de elementos `C` es el mismo | dos completaciones que solo añaden elementos por encima/fuera de `C` comparten carrier |
| Misma relación inducida sobre el observado | El orden restringido a `C` (`C`, `<↾C`) coincide | Alloy 002: ambas completaciones A y B inducen exactamente `{(E2,E3)}` sobre `{E2,E3}` — carrier y relación inducida idénticos |
| Mismo output del observable ejecutable | La función que corre sobre `C` (p. ej. `c1_selector`, `estimate_O_volume`, `build_locus`) produce el mismo valor | No verificado en general; para `c1_selector` con `R=Max(C)` el output es trivialmente idéntico (`NO_INTERFACE`) porque no depende de nada fuera de `C` |
| Misma geometría oculta | Las coordenadas `(t*, r)` (o la variedad completada) coinciden | Nunca es el caso entre completaciones A y B del testigo Alloy 002 — E1 (completion A) y E0 (completion B) ocupan posiciones geométricas distintas por construcción |

Dos completaciones "observacionalmente indistinguibles" para C1 deben declarar **cuál** de las
tres primeras nociones usan (carrier / relación inducida / output ejecutable) — no es lo mismo
exigir que compartan solo el orden inducido que exigir que un ensamblador concreto produzca el
mismo output. El testigo Alloy 002 solo establece indistinguibilidad en el sentido más débil
(relación inducida idéntica sobre `{E2,E3}`); no se ha probado indistinguibilidad de ningún output
ejecutable del proyecto (`c1_selector`, `estimate_O_volume`, `build_locus`) entre A y B.

---

## 3. Completion

Los cinco términos de `comité 010` (`comite_decision_010_c1-completion-truncation-nonidentifiability.md:34-36,`
§9 step 2) en el orden de dependencia que la lógica del comité exige (a→b→c→d→e):

| Cláusula | Definición operativa propuesta | Marca |
|---|---|---|
| **(a) Clase de subposet observado** | Un poset finito `C` que es la restricción de una completación a un down-set/región convexa (a definir en (b)), producido por el generador sellado (`generator.py`), matriz booleana `past_matrix`. | `REQUIRED` — sin esto no hay objeto de partida |
| **(b) Clase de completación admisible 𝔄** | El conjunto de extensiones de `C` a un poset mayor `C1 ⊇ C` que satisfacen TODAS las obligaciones de §4 marcadas `REQUIRED` en esa sección, y NINGUNA de las prohibiciones. Es el **grado de libertad que carga la prueba** (comité 010 lógico: "(b) y (e)... el peligro post-hoc vive enteramente aquí"). | `REQUIRED`, contenido exacto `UNRESOLVED` — §4 enumera obligaciones candidatas sin fusionarlas en una 𝔄 cerrada |
| **(c) Regla de referencia inducida (order-only)** | Una función `ref: 𝔄 → 2^C1` computable **solo** desde `past_matrix` de la completación, sin leer `r=2M` ni ninguna coordenada. Candidato existente: `c1_selector.maximal_elements` (`nachocausal/c1_selector.py:19-25`) — pero produce `R=Max(C)` que trivializa a `NO_INTERFACE` (comité 009 preflight). | `REQUIRED`; candidato actual **trivial**, por tanto `UNRESOLVED` como regla útil |
| **(d) Regla de pullback** | Cómo restringir la decisión tomada en `C1` (completación) de vuelta al `C` compartido — p. ej. `interface ∩ C` o `down_closure` restringida. Candidato: `c1_selector.down_closure` (`nachocausal/c1_selector.py:28-36`) ya opera order-only sobre cualquier referencia dada. | `OPTIONAL_CANDIDATE` — la maquinaria existe y es order-only, pero no ha sido probada como la única regla de pullback válida ni acordada por comité |
| **(e) Predicado de incompatibilidad** | Cuándo dos pullbacks de dos completaciones distintas cuentan como "incompatibles" sobre el `C` compartido — p. ej. `interface_A ∩ C ≠ interface_B ∩ C`, o una noción más débil (cardinalidad, posición relativa). No existe ninguna versión ejecutable en el repo. | `REQUIRED`; `UNRESOLVED` — comité 010 lo señala como el segundo lugar (junto con (b)) donde el post-hoc tuning es posible |

**No se declara ninguna de estas cláusulas suficiente por sí sola** para cerrar C1; §8 lista las
decisiones que comité 012 debe tomar sobre ellas.

---

## 4. Physical admissibility

Obligaciones candidatas, **presentadas por separado, sin fusionar**. Ninguna se afirma aquí
necesaria o suficiente sin respaldo explícito.

| Obligación | Definición operacional disponible | Evidencia existente | Estado | Alloy 002 |
|---|---|---|---|---|
| **Orden parcial causal** | Relación irreflexiva y transitivamente cerrada (`past_matrix` booleana, antisimétrica). | `dev/alloy/product_order_check_alloy002_witness.py` §3 punto 2: chequeo explícito de "valid strict partial order". | `DEFINED` | Ambas completaciones A y B **satisfacen** esto (`product_order_check_alloy002_witness_note.md` §4, ambas filas "Valid strict partial order: ✓"). |
| **Convexidad del subconjunto observado** | Para todo `x,y` en el subconjunto observado y todo elemento oculto `h` de la completación: no `x < h < y`. | `product_order_check_alloy002_witness_note.md` §3 punto 4, §4 (chequeo explícito, ejecutado). | `DEFINED` (como test ejecutable sobre un testigo concreto; no se ha generalizado a un predicado sobre 𝔄 completa) | Completion A **satisface** (E1 está por encima de todo lo observado); Completion B **viola** (E0 satisface E2<E0<E3, causalmente interpuesto). Esta es la razón exacta de `PHYSICAL_LAYER_EMPTY_EVIDENCE`. |
| **Realizabilidad mediante orden producto / embedding (`dim_DM ≤ 2`)** | Búsqueda exhaustiva de un par de extensiones lineales `(L1, L2)` tal que `x <_P y ⟺ x <_L1 y ∧ x <_L2 y`. | `product_order_check_alloy002_witness_note.md` §3 punto 3, §4 (chequeo ejecutado, ambas completaciones). | `DEFINED` (como test ejecutable) | **Ambas** completaciones A y B **pasan** `dim_DM ≤ 2` (`witness_note.md` filas "2D product-order realizable: ✓" para A y B). Este chequeo por sí solo **no discrimina** el testigo — solo la convexidad lo hace. |
| **Dimensionalidad como obligación general** | Si `dim_DM(C) ≤ 2` debe exigirse a TODA completación de 𝔄, o solo es una propiedad esperada del generador Schwarzschild concreto. | Comité 010 mathematician brief: "asserted by generator audit, **not measured** — Prop 7.3" (`comite_decision_010.md:72`). | `UNDEFINED` como obligación de 𝔄 — no hay fuente ni prueba de que sea necesaria o suficiente para admisibilidad física general. **No se declara aquí necesaria ni suficiente** (restricción explícita del brief). | N/A — el chequeo de dimensión se hizo, pero no se ha decidido si debía ser vinculante. |
| **Compatibilidad con una región Schwarzschild** | Ninguna definición ejecutable existe. El physicist brief describe descriptivamente "extensiones manifoldlike de la familia `f(r)`" (`comite_decision_010.md:101`) pero no hay predicado computable sobre una completación combinatoria arbitraria que verifique esto. | Ninguna (descriptivo únicamente). | `UNDEFINED` | No evaluable — ninguna completación del testigo Alloy 002 fue construida como región Schwarzschild; ambas son extensiones combinatorias abstractas de 1 elemento. |
| **Manifoldlikeness / sprinkling** | Ninguna definición ejecutable existe como predicado sobre una completación combinatoria arbitraria (a diferencia de: el generador SÍ produce sprinklings verificados por `χ²` gate para densidades conocidas, `generator.py:53-82` — pero eso es una propiedad del generador, no un test aplicable a un testigo Alloy). | `generator.py:53-82` (χ² gate, solo para el generador, no para completaciones arbitrarias). | `UNDEFINED` como predicado de admisibilidad de 𝔄 | No evaluable — Alloy 002 no es una salida del generador de sprinkling. |
| **Ausencia de elementos ocultos causalmente interpuestos de forma físicamente inadmisible** | Formulación equivalente a la fila de convexidad arriba (mismo test). | Igual que convexidad. | `DEFINED` (misma evidencia que convexidad) | Igual que convexidad: A satisface, B viola. |

**Nota de disciplina:** dos filas de esta tabla (convexidad; ausencia de elementos ocultos
interpuestos) son la misma obligación con dos redacciones — se listan por separado porque el
brief las nombra por separado, no porque sean obligaciones independientes.

---

## 5. Los cinco términos de comité 011

Localizados mediante `rg` en `docs/comite/comite_decision_011_patch-ensemble-architecture.md:123-124,346-347`
(mathematical logic brief + síntesis §8 punto 2): **"parches locales"**, **"ensamblaje"**,
**"compatibilidad causal"**, **"cobertura transversal"**, **"S¹/S²"**. Verificado independientemente
con `rg -il "parche"` (solo prosa en roadmap/comité, ningún `.py`/`.lean`) y `rg "S1|S2"` en `*.py`
(únicos hits son identificadores Python no relacionados, p. ej. `s2 = heights(...)` en
`dev/measure_bl_localization_l1a.py:105`).

### 1. "Parches locales" (local patches)

1. **Definición matemática/ejecutable:** ninguna existe en el repo. Candidato informal (comité 011
   §1): "cabezas cortas sembradas desde la frontera" — un segmento de cadena/escalera corto
   iniciado en un elemento de un frente `boundary-bracket`.
2. **Inputs:** (candidato) un elemento semilla + una regla de parada.
3. **Output:** (candidato) subconjunto ordenado conexo de `C`.
4. **Unidad/normalización:** ninguna declarada.
5. **Dependencia de densidad:** sí, presumiblemente (vía `NMIN`, `ℓ`), pero no medida porque el
   objeto no existe ejecutablemente.
6. **Condición de éxito/fallo:** ninguna definida.
7. **Relación con código existente:** el más cercano es `dev/measure_truncated_head.py` (cabeza
   acumulada con parada `k*`) y el `build_locus` de `dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md`
   §2 (frentes `L_past`-nivel) — pero ninguno se llama "parche" formalmente ni coincide
   necesariamente con la noción propuesta.
8. **Ambigüedades abiertas:** la regla de parada de cabeza (`k*`) **no es order-only** — lee
   `d_perp` de la incrustación oculta (`measure_truncated_head.py:113-119`; comité 011 falsifier
   Attack 1). Ningún observable order-only con breakpoint alineado ha sido encontrado en el
   codebase (comité 011 falsifier: "No such observable exists in the codebase"). Este es el
   `BLOCK-5` de comité 011: no una advertencia, una falsación del supuesto arquitectónico central.

### 2. "Ensamblaje" (assembly)

1. **Definición matemática/ejecutable:** ninguna cerrada. Candidato: unión de "parches locales"
   (arriba) a través de semillas/frentes.
2. **Inputs:** (candidato) una colección de parches locales.
3. **Output:** (candidato) un subconjunto ordenado conexo mayor, o una relación de compatibilidad
   entre piezas.
4. **Unidad/normalización:** ninguna.
5. **Dependencia de densidad:** el objeto ejecutable más próximo (`_locus` en S3,
   `dev/measure_iterative_reseed_v1.py`, descrito en `dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md`
   §2-4) sí depende de densidad: `n_loc` crece 96→146→234 con intensidad 3600→7200→14400.
6. **Condición de éxito/fallo:** para el objeto S3 existente, la condición pre-comprometida era
   "coverage no se degrada con densidad" (`hoja_de_ruta_24_jun_2026.md:64,80`) — **FAIL**
   (§6 abajo). Para la noción de "ensamblaje de parches locales" propiamente dicha (unión de
   cabezas cortas, no de frentes), ninguna condición de éxito ha sido escrita.
7. **Relación con código existente:** `dev/measure_iterative_reseed_v1.py` (unión de frentes
   `L_past`, no de cabezas cortas) es el precedente ejecutable más cercano, pero comité 011
   distingue explícitamente el objeto nuevo propuesto (ensamblaje de cabezas) del objeto S3 ya
   medido (unión de frentes) — no son el mismo objeto.
8. **Ambigüedades abiertas:** Guard-v para la unión multi-semilla **no está demostrado**
   (`selection_guard.verify_selection_order_only`, `nachocausal/selection_guard.py:52-84`, testea
   un único selector sobre una única matriz; la unión no tiene test correspondiente — comité 011
   Attack 4, `BLOCK-4`). Se confunde si "ensamblaje" se refiere al objeto S3 ya fallido o a un
   objeto nuevo no construido (cabezas cortas).

### 3. "Compatibilidad causal" (causal compatibility)

1. **Definición matemática/ejecutable:** ninguna existe. Ninguna fórmula candidata ha sido
   propuesta en ningún dossier del repo.
2. **Inputs:** (aspiracional) un par de parches locales vecinos.
3. **Output:** (aspiracional) un booleano de compatibilidad/empalme.
4. **Unidad/normalización:** N/A.
5. **Dependencia de densidad:** no evaluable — no existe la función.
6. **Condición de éxito/fallo:** no evaluable.
7. **Relación con código existente:** ninguna. El único artefacto formal relacionado es negativo:
   todos los teoremas de transporte en Lean (`mapIdealEndOrderIso`, `mapChainEndOrderIso`,
   `dev/LEAN_HYPOTHESIS_AUDIT.md` §4-§5) están probados **solo para isomorfismos de orden**, no
   para *embeddings*; unir parches a través de semillas es exactamente el caso de embedding no
   cubierto (comité 011 logician brief: "'Causal compatibility between neighbouring pieces' IS
   precisely this unproved embedding-gluing case").
8. **Ambigüedades abiertas:** el término es enteramente indefinido — ni siquiera existe una
   fórmula candidata que evaluar. Es el término con menor especificación de los cinco.

### 4. "Cobertura transversal" (transversal coverage)

1. **Definición matemática/ejecutable:** existe un precedente ejecutable parcial —
   `cov_honest = n_covering / n_cand` (`dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md` §3, definida
   exactamente en `dev/measure_iterative_reseed_v1.py`). **No se cambia esta definición aquí** —
   se reporta tal como produjo el FAIL medido.
2. **Inputs:** frentes candidatos (`|F|≥NMIN`), su clasificación (`LOCALISED`/`ABSTAIN`/`DEGEN`),
   y `R_S` (revelada solo para puntuar, nunca para seleccionar).
3. **Output:** fracción en `[0,1]`.
4. **Unidad/normalización:** adimensional (fracción); denominador = todos los candidatos
   (incluye abstain+degen como *miss*, corrigiendo el sesgo v0).
5. **Dependencia de densidad:** sí, medida: 51%→48%→44% (honesta), 74%→65%→54% (optimista) en
   intensidades 3600/7200/14400 (`dev/iterative_reseed_v1.log:14,25,36` y `:13,24,35`
   respectivamente).
6. **Condición de éxito/fallo:** pre-comprometida — "no se degrada (idealmente mejora) con
   densidad" (`hoja_de_ruta_24_jun_2026.md:64,80`). Resultado: **FAIL** (monótono, comité 011
   Attack 2, "no future risk — it is a past FAIL").
7. **Relación con código existente:** `dev/measure_iterative_reseed_v1.py` implementa exactamente
   esta métrica; es la misma cuyo FAIL R3 diagnosticó.
8. **Ambigüedades abiertas:** el physicist brief de comité 011 (dissent registrado, §8) señala que
   **en 1+1D el horizonte no tiene superficie que cubrir** (sección espacial `S⁰`, dos puntos) —
   "la motivación de 'coverage de superficie' es físicamente vacía en 1+1D"; lo que `cov_honest`
   mide en 1+1D es *tiling* de un generador nulo a lo largo de `t*`, no una cobertura transversal
   2D genuina. Esa noción "transversal" solo adquiere contenido físico en 2+1 (`S¹`) o 3+1 (`S²`),
   que están fuera de alcance (§1, §5.5 abajo). **No se resuelve aquí si "cobertura transversal"
   es sinónimo del `cov_honest` ya medido y ya fallido, o una noción distinta aún sin definir** —
   esa es una decisión abierta para comité 012 (§8).

### 5. "S¹/S²"

1. **Definición matemática/ejecutable:** ninguna. Alusión verbal a la topología de la sección
   espacial del horizonte en 2+1D (`S¹`) y 3+1D (`S²`).
2. **Inputs:** N/A — ningún dominio de sprinkling 2+1/3+1 existe (`generator.past_matrix_fast`
   acepta solo `"BH"` 1+1D).
3. **Output:** N/A.
4. **Unidad/normalización:** N/A.
5. **Dependencia de densidad:** no evaluable — no hay observable ni dominio.
6. **Condición de éxito/fallo:** no evaluable.
7. **Relación con código existente:** ninguna. Verificado (`rg "S1|S2" *.py`): los únicos hits en
   `.py` son identificadores no relacionados (p. ej. `s2` como variable local en
   `dev/measure_bl_localization_l1a.py:105`).
8. **Ambigüedades abiertas:** sin ancla en literatura (`comite_decision_011.md:301,308`: "no
   literatura anchor"; "[UNVERIFIED against any source]"). El logician brief lo marca como un
   posible **category mistake** — atribuir tipo topológico de continuo a un conjunto discreto
   finito sin un objeto límite explícito mediador (nervio, complejo de persistencia, límite de
   densidad de Poisson) que no existe en el repo (`comite_decision_011.md:143-151`). Fuera de
   alcance por `BLOCK-4` (§1 de este documento).

---

## 6. Boundary-bracket status

```text
BOUNDARY_BRACKET_STATUS =
  FAILED_BASELINE_UNDER_PRECOMMITTED_DENSITY_COVERAGE_CRITERION
```

- Puede conservarse para diagnóstico o comparación (p. ej. como referencia de qué NO converge).
- **No puede asumirse como base válida de un ensamblaje C1.** Cualquier "ensamblaje" (§5.2) que
  reutilice el localizador `two_means_split` sobre `O` hereda la degradación medida.
- R3 (`dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md` §6-8) localiza la degradación en la calidad
  per-frente del localizador (`cov_opt`: 74%→65%→54%) con `CONFIDENCE = MEDIUM`, no en el
  pipeline posterior (τ(n) mejora con densidad, no empeora).
- El mecanismo interno exacto (empobrecimiento de futuros interiores) permanece parcialmente no
  resuelto: R3 §9 registra que no existe desglose per-frente de la distribución de `O` interior/
  exterior que confirme directamente el estrechamiento del contraste bimodal; el mecanismo se
  infiere, no se mide directamente.

---

## 7. C1 witness requirements

Un testigo válido de no-identificabilidad C1 debe aportar, todos a la vez:

1. **Dos completaciones distintas** `C1_A ≠ C1_B`, ambas extendiendo el mismo `C` observado.
2. **Misma observación inducida** — mismo carrier Y misma relación inducida sobre `C` (§2, fila 1
   y 2 de la tabla de distinciones; declarar explícitamente cuál de las dos se exige, o ambas).
3. **Ambas satisfacen todas las restricciones de 𝔄** (§3(b), §4) — no solo una subcolección
   escogida ad hoc.
4. **Cambian la misma propiedad objetivo** — el output de la regla de referencia inducida (c) tras
   pullback (d) difiere entre `C1_A` y `C1_B` según el predicado de incompatibilidad (e).
5. **Certificado de cada restricción** — no basta declarar que una completación "es admisible"; cada
   obligación de §4 marcada `REQUIRED` (una vez que comité 012 decida cuáles lo son) debe tener un
   chequeo ejecutable y registrado, como el que ya existe para convexidad y `dim_DM≤2`
   (`dev/alloy/product_order_check_alloy002_witness.py`).
6. **Ausencia de uso de geometría oculta para construir el testigo**, salvo que 𝔄 lo autorice
   expresamente (y en tal caso, declarado por escrito antes de la búsqueda del testigo, para
   evitar la construcción post-hoc que comité 010 §8 identifica como riesgo de fuga de ground
   truth — "the induced reference rule... must not identify r=2M using the hidden embedding").

```text
ALLOY_002_C1_WITNESS_STATUS =
  INVALID_UNDER_CONVEXITY_REQUIREMENT
```

Esto **no afirma que la no-identificabilidad física sea falsa** — solo que este testigo concreto
no satisface la obligación de convexidad (§4), y por tanto no certifica nada bajo una clase
físicamente admisible tal como está actualmente entendida. `PHYSICAL_LAYER_EMPTY_EVIDENCE`
(R1, commit `c2e64b5`) significa ausencia de evidencia física válida en *este* testigo, no una
prueba de imposibilidad.

```text
ALLOY_002_LOGICAL_WITNESS = PRESENT
ALLOY_002_PHYSICAL_WITNESS = NOT_ESTABLISHED
```

---

## 8. Open decisions for committee 012

Únicamente las decisiones que siguen abiertas — no se responden aquí:

- Qué restricciones de §4 forman finalmente 𝔄 (¿todas las `REQUIRED` candidatas? ¿un subconjunto?).
- Si la convexidad es obligatoria para toda 𝔄, o solo se aplica al testigo concreto ya evaluado.
- Si `dim_DM ≤ 2` (product-order realizability) es obligatoria, opcional, o irrelevante para 𝔄 —
  no hay fuente que la fije como necesaria o suficiente (Prop 7.3 es "asserted... not measured").
- Si "compatibilidad con región Schwarzschild" y "manifoldlikeness/sprinkling" deben tener
  definiciones ejecutables propias antes de cerrar 𝔄, o si convexidad + `dim_DM≤2` bastan como
  proxy.
- Si `boundary-bracket` queda fuera de C1 por completo, o se mantiene solo como baseline fallido
  (§6) para comparación diagnóstica.
- Si "cobertura transversal" (§5.4) debe identificarse con el `cov_honest` ya medido y ya fallido,
  o si es una noción genuinamente distinta que requiere un objeto límite (nervio, persistencia)
  aún no construido.
- Si "parches locales", "ensamblaje" y "compatibilidad causal" (§5.1-5.3) necesitan definiciones
  ejecutables cerradas antes de que la pregunta arquitectónica (comité 011) pueda siquiera
  reabrirse, o si son independientes de la pregunta C1 estricta de este documento.
- Si se necesita una formalización Lean adicional para el caso de embedding (compatibilidad
  causal / transporte de parches) — y si es así, quién la produciría y en qué checkout (dado que
  "Variant A" NO está en este repositorio, R2 `BLOCKED_WRONG_REPOSITORY_CONTEXT`).
- Si la pregunta C1, tal como está especificada en este documento, está lista para pasar a un
  modelo Alloy 003 (comité 010 §9 step 4) o si requiere primero una prueba matemática cerrada de
  alguna cláusula de §3/§4.
- Si el predicado de incompatibilidad (e) debe ser una igualdad estricta de outputs o una noción
  más débil (p. ej. divergencia de posición relativa).

---

## 9. Entry criterion for committee 012

```text
C1_DEFINITION_STATUS = READY_FOR_COMMITTEE_012
```

**Justificación de la marca:** el objetivo de este documento no era cerrar C1 (eso excede el
alcance de R4 y del propio comité 010, que exige congelar las definiciones *antes* de buscar
testigos, no resolverlas unilateralmente en un documento dev). El objetivo era producir una
estructura suficientemente precisa — cláusulas §3 etiquetadas `REQUIRED`/`OPTIONAL_CANDIDATE`/
`UNRESOLVED`, obligaciones físicas de §4 clasificadas y evaluadas contra el único testigo
disponible, los cinco términos de comité 011 con su estructura de 8 puntos y ambigüedades
explícitas, y una lista cerrada de decisiones pendientes (§8) — para que comité 012 pueda
**decidir si la pregunta está suficientemente especificada**, incluyendo la opción de devolverla
con instrucciones de mayor precisión. Esa es la lectura correcta de "READY": listo para
adjudicación, no listo para búsqueda de testigos ni para implementación.

Permanecen `UNRESOLVED`/`UNDEFINED` explícitamente: §3(b) (contenido exacto de 𝔄), §3(c) (regla
de referencia no trivial), §3(e) (predicado de incompatibilidad), y en §4: dimensionalidad como
obligación general, compatibilidad Schwarzschild, manifoldlikeness/sprinkling. Ninguno de estos
vacíos impide que comité 012 delibere sobre §8; todos ellos SON el contenido de §8.

---

## Registro de validación (R4)

- Archivos leídos íntegros antes de escribir: `docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md`,
  `docs/comite/comite_decision_011_patch-ensemble-architecture.md`,
  `dev/alloy/product_order_check_alloy002_witness_note.md`,
  `dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md`, `docs/hoja_de_ruta_24_jun_2026.md` (secciones
  citadas), `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md`, `dev/LEAN_HYPOTHESIS_AUDIT.md`,
  `nachocausal/c1_selector.py`, `nachocausal/selection_guard.py`.
- Cinco términos de comité 011 localizados con `rg` y citados exactamente
  (`comite_decision_011...md:123-124,346-347`); no se sustituyó por una lista alternativa.
- No se modificó Lean, Alloy, ni ningún script. No se propuso una clase C1 definitiva, ni la
  pista Q, ni una alternativa a `boundary-bracket`. No se abrió 2+1/3+1 salvo para documentar por
  qué está fuera de alcance. No se tocaron thresholds. No se ejecutaron sprinklings ni análisis
  numéricos. No se modificaron los briefs de comité ni ninguna definición histórica.
- Único archivo escrito: `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` (nuevo).
