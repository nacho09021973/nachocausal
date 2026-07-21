# Comite Decision 043 — Adjudicación conceptual C6: `INTERNAL_ALEXANDROV_WAIST_SCREENS`

STATUS: CONCEPT_ADJUDICATION_DOCUMENTARY / CANDIDATE_6_NOT_OPENED
NO_IMPLEMENTATION / NO_SYNTHETIC_EXECUTION / NO_SEEDS / NO_FREEZE / NO_CONTRACT
DATE: 2026-07-21
PROVENANCE: HEAD=050a4e2 ; seal thresholds.py sha256=6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4 (prereg-002 seal #3, untouched)
REVIEWED_BY: docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md (terminal revisado 2→1; §7/§9/§12 sobre-afirmaciones corregidas; sello re-verificado)

Estado de entrada (se registra explícitamente, sin alterarlo):

```text
C1_C5_LOCALIZER_LINE_CLOSED
C6_NOT_OPENED
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
```

Este documento evalúa **exclusivamente** si el objeto-pantalla `W(p,q)` (cintura interna de
bi-enlaces de un intervalo de Alexandrov) y su **transporte** entre profundidades pueden
definirse de forma **cerrada** y **order-only**. No diseña un observable de trapping, expansión,
clasificación ni localización. No abre `CANDIDATE_6`. No congela ni toca contratos, `thresholds.py`,
manifests, ledgers, terminales ni evidencia. No reutiliza el beam observable de PR009.

La línea C1–C5 (localización de regiones vía minimales, futuros globales y particiones de bloques)
**no se reabre bajo otro nombre**: el objeto cambia de `Min(C) → región` a
`(p,q) → W(p,q) → evolución de pantalla`.

---

## 1. Pregunta única

> ¿Define la familia de cinturas internas `{W(p,q)}` una pantalla cuasi-local *order-only* con
> noción cerrada de área y transporte entre profundidades, sin seleccionar una región espacial ni
> usar paredes, minimales o embedding?

---

## 2. Inspección read-only (anclas)

Revisado en modo lectura antes de redactar:

| Fuente | Uso en esta adjudicación | Ancla |
|---|---|---|
| Cierre C1–C5 | Estado de entrada; canal de minimales→región agotado; muerte C5 = `F3` pared↔bridge; menú C6 no autorizado | `docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md` (§3 C4/C5, §6, §7 C6-A/B/C) |
| Cierre PR009 | El cierre fue **previo al scoring** por inviabilidad de cobertura (`FAILED_DATA_CONTRACT`), no un negativo físico contra esta línea | `dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_CLOSURE_DECISION.md` (líneas 1–20, 47–61) |
| Beam observable PR009 (prohibido reutilizar) | Anchura transversal de un **ensemble** de continuaciones fuzzy-ladder; `D(u,v)=sqrt(min|[e,f]|)`, `W_k=lower_median`, `θ_raw=Δlog W` | `dev/PR009_..._PREREGISTRATION.md` §§5.2–5.4 (líneas 76–142) |
| Relación de enlace/cobertura del repo | `≺*` = reducción transitiva `L = C & ~((C·C)>0)` | `dev/measure_kbeam_peeloff.py:111` (`gpu_link_csr`) |
| Intervalo causal cerrado (endpoints incluidos) | `|[e,f]|` incluye ambos extremos | `dev/PR009_..._PREREGISTRATION.md:104` |
| Ladders / rung / side / expansión discreta / focusing | Def. 1 (causal ladder), rung `(p_i,q_i)`, `≺*` como link, `|[p_1,q_2]|=2`; expansión `Θ=(1/A)dA/dλ`; interior/exterior por signo | `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md` (§§II, IV.A, ecs. (10)–(13)) |
| C4 grafo de vecinos no resuelto | No existe `E_M ⊂ binom(Min,2)` order-only, relabel-invariante, cerrado en empates | `docs/comite/comite_decision_039_c4-neighbor-graph-adjudication.md`; C42 §3 C4 |
| C5 sin peel lateral canónico | Pared = embebimiento; `Φ★_L` mapa formal, no localizador; `F3` ambigüedad twin | C42 §3 C5 (`FAIL_WALL_BRIDGE_TWIN_AMBIGUITY`) |
| Gramática de claims / teleología del horizonte | Horizonte de eventos global no está en el patch finito; solo proxy cuasi-local con target propio | `docs/claim_grammar.md` §3 (líneas 61–74) |

**Verificación de reutilización.** El objeto de la ladder-rung `(p_i,q_i)` (par de link-lados) ya
existe en EGS y en `dev/measure_kbeam_peeloff.py`. La construcción `W(p,q)` propuesta aquí — la
antichain de *bi-enlaces internos de un único intervalo* — **no** aparece como objeto cerrado en
código, docs ni runs previos: PR009 trabaja poblaciones de trayectorias (rungs a lo largo de
profundidad), no la cintura interna de un intervalo. `Φ★_L` (C5) opera sobre la matriz global de
common-future de minimales, objeto distinto. Por tanto `W(p,q)` es un objeto nuevo, no un renombre.

---

## 3. Por qué C6 cambia el objeto (y no reabre C5)

C1–C5 agotaron la línea `partición de minimales → región`. El cierre final de C5 fue
`FAIL_WALL_BRIDGE_TWIN_AMBIGUITY` (C42 §3): sin control lateral order-only, el corte "twin" de la
señal bridge coincide con el de un surrogado de dos paredes. C6 **no** debe volver a distinguir
pared y bridge por una partición de minimales.

La sustitución de objeto es:

```text
Min(C) --------> región                (canal C1–C5, AGOTADO)
(p,q) --> W(p,q) --> evolución de pantalla interna   (objeto C6, aquí adjudicado)
```

C6 opera sobre pares internos `(p,q)`, intervalos de Alexandrov internos y antichains `W(p,q)`.
**No** usa: matrices de futuros comunes entre minimales, twins, bridges, bloques de minimales,
pared lateral como etiqueta, ni mapa a región espacial. Esta separación se comprueba formalmente en
§12.

---

## 4. Definición del objeto básico `W(p,q)`

Sea `C` un causet finito con orden estricto `≺` (irreflexivo, transitivo; "timelike o null", EGS
§II). Sea `≺*` la relación de **enlace/cobertura** del repositorio: `x ≺* y` sii `x ≺ y` y no existe
`z` con `x ≺ z ≺ y` (reducción transitiva `L = C & ~((C·C)>0)`, `dev/measure_kbeam_peeloff.py:111`).

Para un par comparable `p ≺ q` se define la **cintura de bi-enlaces**:

```text
W(p,q) = { x ∈ C : p ≺* x  ∧  x ≺* q }.
```

Es decir, `x` es simultáneamente un link-hijo de `p` y un link-padre de `q`: `x` cierra una cadena
de enlaces de longitud dos `p ≺* x ≺* q`.

Ambigüedades fijadas sin excepción (todas order-only):

1. **Exclusión de `p` y `q`.** `p ∉ W` y `q ∉ W`: `≺*` es irreflexiva, luego `p ≺* p` y `q ≺* q`
   son falsas; ningún extremo se cuenta. La cintura es estrictamente interior a `(p,q)`.
2. **Intervalo abierto.** `W(p,q) ⊆ (p,q)`, el intervalo **abierto** `{x : p ≺ x ≺ q}` (sin
   extremos). Prueba: `p ≺* x ⟹ p ≺ x`, `x ≺* q ⟹ x ≺ q`. `W` es un subconjunto propio de la
   cintura del intervalo abierto (los `x` que además son enlace de ambos extremos).
3. **Pasado de `p` no vacío.** `J⁻(p) ≠ ∅` sii `∃ a : a ≺ p` (`p` no es minimal). Order-only.
4. **Futuro de `q` no vacío.** `J⁺(q) ≠ ∅` sii `∃ b : q ≺ b` (`q` no es maximal). Order-only.
5. **Par "interno".** `(p,q)` es interno sii `p ≺ q`, `J⁻(p) ≠ ∅`, `J⁺(q) ≠ ∅`. No se introduce
   ninguna definición geométrica de "interno"; se exige únicamente que ni `p` esté en el suelo del
   patch ni `q` en el techo (condiciones intrínsecas de existencia de pasado/futuro). En §7 se
   discute reforzar con profundidad mínima.
6. **Relación exigida `p ≺ q`.** Relación causal **general** (no un enlace). Si `p ≺* q` fuese un
   enlace, no existiría intermedio y `W(p,q)=∅` por definición. La cintura solo es no trivial cuando
   `p ≺ q` se realiza a "distancia-de-enlace 2" con al menos un testigo `x` enlazado a ambos
   extremos. **No** se exige que exista *exactamente* un testigo.
7. **Caso `W(p,q)=∅`.** No se interpreta como "área cero física". Es una **abstención** del objeto
   para ese par (§11, falsificador 1). El par se marca inadmisible como pantalla, no como pantalla
   de tamaño nulo.

`W(p,q)` depende únicamente de `≺` (y de `≺*`, derivada de `≺`). Es una función de la relación de
orden, no del embedding, coordenadas, paredes ni etiquetas.

---

## 5. `W(p,q)` es una antichain — demostración

**Afirmación.** Para todo par `p ≺ q`, `W(p,q)` es una antichain: no existen `x,y ∈ W(p,q)`
distintos con `x ≺ y`.

**Prueba (solo con la definición de enlace).** Supóngase `x,y ∈ W(p,q)`, `x ≠ y`, y `x ≺ y`. Por
pertenencia, en particular:

```text
p ≺* y        (y ∈ W ⟹ p ≺* y),
```

es decir, `p ≺ y` es un **enlace** (no hay elemento estrictamente entre `p` e `y`). Pero de
`x ∈ W` se tiene `p ≺* x`, luego `p ≺ x`; y por hipótesis `x ≺ y`. Entonces:

```text
p ≺ x ≺ y,
```

de modo que `x` es un elemento intermedio estricto entre `p` e `y`. Esto **contradice** que `p ≺* y`
sea un enlace. ∎

Simétricamente, la misma hipótesis rompe el otro enlace: de `x ≺* q` se tiene `x ≺ q`, y con
`x ≺ y` resulta `x ≺ y ≺ q`, luego `y` es intermedio estricto entre `x` y `q`, contradiciendo que
`x ≺* q` sea enlace. Basta con que **una** de las dos relaciones `p ≺* y` o `x ≺* q` deje de ser un
enlace; ambas fallan, y cualquiera de las dos cierra la contradicción.

**Compatibilidad con la convención del repositorio.** La prueba usa exclusivamente que `≺*` es la
reducción transitiva de `≺` (la definición frozen de enlace en `dev/measure_kbeam_peeloff.py:111`):
`u ≺* w` implica que no existe intermedio estricto. No usa embedding, coordenadas ni cardinalidad de
intervalo. La propiedad **es válida** bajo la convención exacta del repositorio; no procede terminal
negativo por incompatibilidad. La antichain no se presenta como intuitiva: queda demostrada.

---

## 6. Interpretación permitida (y sus límites)

Interpretación admitida, y **solo** esta:

> `W(p,q)` es una **antichain interna** definida por la intersección de dos relaciones de enlace.
> Puede *investigarse* como candidata a pantalla discreta asociada a un intervalo de Alexandrov.

**No** se afirma (todas hipótesis futuras, no resultados): que sea superficie codimensión dos
demostrada; que aproxime la cintura geométrica del diamante; que sea superficie marginal; que su
cardinalidad sea área física; que permita definir expansión o trapping. Ninguna atribución de
codim-2, expansión, marginalidad o trapping se toma como establecida en este documento.

---

## 7. Gate 1 — ¿existe una familia order-only no trivial de pantallas?

Familia:

```text
W = { W(p,q) : (p,q) ∈ P_int },   P_int = { (p,q) : p ≺ q, J⁻(p)≠∅, J⁺(q)≠∅, W(p,q)≠∅ }.
```

`P_int` es **una clase cerrada order-only**: cada condición (`p ≺ q`, existencia de pasado de `p`,
existencia de futuro de `q`, `W≠∅`) es una fórmula sobre `≺`, sin coordenadas, sin paredes del
dominio, sin minimales como región de partida, sin selección post-hoc por éxito geométrico y sin
umbrales calibrados con semillas. Condiciones intrínsecas adicionales opcionales examinadas (todas
order-only): profundidad pasada mínima `height⁻(p) ≥ h` y futura `height⁺(q) ≥ h` para excluir pares
pegados al suelo/techo (`height` = longitud de la cadena más larga, el mismo diagnóstico order-only
que EGS §III usa para minimales, fuente md línea 181). Estas cotas **no** requieren coordenadas.

Distinciones exigidas por el propio gate, resueltas por separado:

- **Existencia de pantallas.** SÍ (probada). La antichain está bien definida y §5 garantiza que es
  genuina. Para pares con `|[p,q]|` moderado existen testigos `x` enlazados a ambos extremos. Esto
  es *existencia*, no *abundancia* ni *estabilidad codim-2*.
- **Abundancia / estabilidad codim-2 de pantallas.** **NO RESUELTA sin ejecución** — y explícitamente
  **no** cerrada aquí. `W(p,q)≠∅` exige que `p ≺ q` se realice a *distancia-de-enlace 2* con un
  testigo enlazado a ambos extremos (§4.6); en régimen de bajo branching la familia es
  **singleton/vacío-dominada**. Falsificador conceptual (contrato de mano, sin ejecución ni
  semillas): en una cadena total `c₁ ≺ c₂ ≺ … ≺ cₙ` la reducción transitiva `≺*` son los pares
  consecutivos; para `(p,q)=(cᵢ,cⱼ)` con `j−i≥2` el único link-hijo de `p` es `cᵢ₊₁` y el único
  link-padre de `q` es `cⱼ₋₁`, luego `W = {cᵢ₊₁} ∩ {cⱼ₋₁}` es **singleton** sii `j−i=2` y **vacío**
  para `j−i≥3`. De los `O(N²)` pares internos solo `O(N)` dan `W≠∅`, y **todos** son singletons
  (nunca una antichain de tamaño >1, pues una cadena no ramifica). Un singleton **no** es una
  superficie codim-2 (dimensión insuficiente, §11 falsif. 2). Un poset ramificado (p.ej. dos
  3-cadenas paralelas unidas arriba y abajo) sí puede dar `|W|>1`, pero el grado de enlace por nodo
  está combinatoriamente acotado, así que **no** rescata una fracción `O(N²)`. La cardinalidad del
  número de caminos de longitud-2 en la reducción transitiva está acotada por la suma de out-grados
  de enlace al cuadrado, genéricamente `O(N)`–`O(N log N)`, **no** una fracción de `O(N²)`. Que
  exista *una* familia estable de pantallas codim-2 (`|W|≥2` de forma no marginal) es exactamente lo
  que **no** puede establecerse order-only sin ejecución (prohibida en esta fase).
- **Capacidad de organizar pantallas.** NO establecida. Tener antichains admisibles no las organiza
  en trayectorias; organizar es lo que el transporte (Gate 3) debería aportar.
- **Capacidad de seguir una pantalla concreta.** NO establecida (Gate 3).

**Veredicto Gate 1.** La antichain `W(p,q)` **existe** y es un objeto order-only cerrado y
relabel-invariante (§5, §8), pero una **familia estable de pantallas codim-2** — el objeto que la
precedencia rule 1 exige como "interpretación mínima de pantalla" — **no queda establecida**:
la abundancia y la estabilidad `|W|≥2` son irresolubles sin ejecución, y el régimen accesible
doc-only es singleton/vacío-dominado (contraejemplo de la cadena, arriba). La codim-2 es además
físicamente insostenible en un patch 1+1D (§6, §14): en 1+1D no hay 2-superficie espacial (EGS §IV
no dispone de ella y sustituye por distancia 1D). Por tanto **Gate 1 NO cierra una pantalla estable
codim-2**: solo un objeto-antichain cuya interpretación como pantalla queda como hipótesis. Por
precedencia (§17), esto **activa** el terminal `C6_BLOCKED_NO_STABLE_CODIM2_SCREEN`. No se elige un
`(p,q)` ganador; el objeto inicial es la familia completa. (El bloqueo de transporte de Gate 3 se
mantiene como bloqueo **adicional independiente**, no como el terminal primario — §9, §17.)

---

## 8. Gate 2 — ¿es `A(p,q)=|W(p,q)|` un área provisional suficientemente cerrada?

Clasificación: `|W|` es **cardinalidad combinatoria**; **candidato provisional a proxy de área**;
**no** área física demostrada.

Análisis:

- **Invariancia bajo relabeling.** SÍ, exacta. `W(p,q)` es un conjunto definido por `≺`; una
  permutación de etiquetas transporta `W` a `W` del par imagen y preserva el cardinal.
- **Dependencia de densidad de sprinkling.** SÍ. `|W|` crece con la densidad (más puntos capaces de
  ser bi-enlace). Es un confound conocido (visto en C2, C42 §3).
- **Dependencia del tamaño del intervalo.** SÍ. `|W|` depende de `|[p,q]|`; intervalos mayores
  admiten más testigos. Este es el núcleo del confound escala↔profundidad (§ Gate 3, §11 falsif. 4).
- **Sensibilidad a degeneraciones.** Alta en los extremos `|W|∈{0,1}` (§11 falsif. 1–2).
- **Vacío / singleton.** `|W|=0` ⇒ abstención; `|W|=1` ⇒ antichain de un punto, dimensión insuficiente
  para hablar de "superficie" (se discute en §11 falsif. 2).
- **Igual cardinalidad, distinta estructura.** SÍ pueden existir dos pantallas con `|W|` idéntico y
  relación causal con el resto de `C` distinta; `|W|` por sí solo no distingue su entorno causal.
- **Normalización.** Corregir densidad/escala exigiría un factor externo (densidad estimada, `ℓ`),
  reintroduciendo parámetros. **No** se propone aquí ninguna otra fórmula ajustable de área.

**Veredicto Gate 2.** Como *cantidad inicial* `|W|` es **suficientemente cerrada** (bien definida,
relabel-invariante, order-only) para permitir una adjudicación posterior. **No** es físicamente
correcta como área y arrastra confounds de densidad y escala. Gate 2 pasa solo en el sentido acotado
que el propio gate pide (cerrada para adjudicar, no correcta como física).

---

## 9. Gate 3 — transporte entre pantallas (**cuello de botella principal**)

Pregunta: ¿existe una relación order-only `W(p,q) ⇝ W(p',q')` interpretable como **continuación del
mismo objeto** a otra profundidad, y no como simple cambio de intervalo/escala/forma del diamante?

Criterio de **transporte cerrado** (todas necesarias): dominio de pantallas; relación de sucesión;
dirección; casos sin sucesor; casos con varios sucesores; reglas de abstención; invariancia bajo
relabeling; ausencia de umbrales calibrables; y **separación entre evolución y cambio arbitrario de
intervalo**.

### 9.1 Mecanismo A — continuación de extremos

- **`p` fijo, `q` avanzado por enlaces (`q ≺* q'`).** `q` tiene, en general, varios link-hijos ⇒
  sucesor **multivaluado**. Además `[p,q'] ⊋ [p,q]`: el intervalo **crece**; el cambio de `|W|`
  mezcla avance con **crecimiento de escala** (falsif. 4). No hay dirección order-only que declare
  esto "evolución futura".
- **`q` fijo, `p` avanzado (`p ≺* p'`).** Simétrico: `[p',q] ⊊ [p,q]`, el intervalo **encoge**;
  multivaluado por los link-hijos de `p`.
- **Ambos extremos avanzados por reglas simétricas.** Requiere emparejar *cuál* link-hijo de `p` va
  con *cuál* link-hijo de `q`. Ese emparejamiento es exactamente una **estructura de vecindad
  intrínseca lateral** entre los dos lados del diamante — el mismo objeto que C4 demostró inexistente
  order-only (`NEIGHBOR_GRAPH_UNRESOLVED`, Decision 039; C42 §3 C4) y que C5 no pudo suplir con un
  peel lateral canónico (`F3`, C42 §3 C5). No hay pareo canónico, relabel-invariante y cerrado en
  empates. **Falla.**

### 9.2 Mecanismo B — continuación por inclusión/solape

Relacionar `W(p,q)` y `W(p',q')` por intersección, inclusión o máxima coincidencia entre las
antichains exige un **umbral libre** ("¿cuánto solape = misma pantalla?"), prohibido por calibración,
y produce **empates** sin desempate order-only admisible (desempatar por etiquetas está vetado).
**Falla.**

### 9.3 Mecanismo C — continuación por estructura del intervalo

Emparejar pantallas cuyos intervalos sean extensiones order-only uno de otro (`[p,q] ⊂ [p',q']`) es
**cambio de escala**, no evolución: intervalos anidados difieren en tamaño del diamante, no en
profundidad de una misma superficie. Además "extensión" es multivaluada. Precisamente el falsificador
4 muestra por qué comparar `|W|` entre intervalos anidados sin transporte físico es inválido.
**Falla.**

### 9.4 Mecanismo D — continuación multivaluada / ramificación

Permitir ramificación cuando no hay sucesor único es admisible en principio, pero en este objeto la
**no unicidad es genérica** (§9.1): cada avance de extremo abre tantas ramas como link-hijos. La regla
"ramificar o abstenerse" degenera en **abstención ubicua** o en un árbol que no define "la misma
pantalla" a lo largo de profundidad. No emerge una noción de identidad transportada. **Falla.**

### 9.5 Evaluación transversal de los mecanismos

| Criterio | A (extremos) | B (inclusión) | C (intervalo) | D (multivaluado) |
|---|---|---|---|---|
| Invariancia relabeling | pareo no invariante | umbral no canónico | anidamiento sí, pero escala | sí, pero sin identidad |
| Unicidad | NO (link-hijos múltiples) | NO (empates) | NO (extensiones múltiples) | NO por diseño |
| Existencia | sí localmente | sí | sí | sí |
| Empates | sin desempate order-only | sí | sí | sí |
| Circularidad | — | riesgo (umbral def. por éxito) | — | — |
| Parámetros libres | pareo lateral inexistente | umbral | — | criterio de rama |
| Estabilidad ante techo | frágil (§10.7) | frágil | frágil | frágil |
| Evolución vs escala | **confunde** | indefinido | **es escala** | indefinido |
| Coste | O(N·grado) por paso, ×pares | O(N²) por par de pantallas | anidamiento | árbol expandido |
| Dependencia de coords/embedding | ninguna, pero por eso falla el pareo | ninguna | ninguna | ninguna |

Ningún mecanismo se selecciona "porque parece geométricamente natural"; se exige justificación
puramente order-only y **ninguno de los examinados** la satisface. Se registra además un quinto
candidato no listado arriba, el **push-forward de antichain** (sucesor = minimales de la futura común
estricta `∩_{w∈W} J⁺(w)`, o los covers de `W`): es order-only y está bien definido, pero (a)
genéricamente **no** coincide con ningún `W(p',q')`, luego sale de la familia y rompe el requisito
"misma pantalla", y (b) afirmar que *es* la misma pantalla exige de nuevo un mapa de identidad
elemento-a-elemento = el mismo pareo ausente. Falla por la misma razón estructural; no abre una vía
nueva.

**Alcance honesto del obstáculo (corrección tras revisión — comité 044).** La variante *simétrica*
del mecanismo A (avanzar ambos extremos de forma coordinada) sí exige demostrablemente un **pareo
lateral intrínseco** entre los dos lados del intervalo; para *ese* subcaso, la reducción al objeto de
vecindad order-only de C4/C5 es un argumento válido. Como reducción **general** ("todo transporte
order-only cerrado ⟹ un grafo de vecinos lateral cerrado") queda **afirmada, no probada**. Y la
imposibilidad heredada de C4/C5 es ella misma **acotada**: la Decision 039 declara explícitamente que
su rechazo es "under the two audited families … **not a theorem** that no order-only spatial adjacency
can ever be defined on any causet" y **no** refuta métodos de tipo `2-link`
(`docs/comite/comite_decision_039_c4-neighbor-graph-adjudication.md:384-401`). Por tanto el nexo
C4/C5 aquí es **herencia por analogía / plausibilidad**, no una transferencia de teorema. No se
intenta salvar el diseño con coordenadas, matching geométrico ni desempates por labels (prohibido).

**Veredicto Gate 3.** No existe un transporte order-only **canónico / univaluado / preservador de
identidad** cerrado **entre los mecanismos examinados (A–D) más el push-forward**, apoyado en un
obstáculo común afirmado-no-probado. Nota de alcance: una relación order-only *ramificada* (mecanismo
D) existe trivialmente; lo que falla es una **canónica**. Este bloqueo de transporte se registra como
un **bloqueo adicional independiente** del terminal, **no** como el terminal primario:

```text
GATE3_TRANSPORT = NO_CLOSED_CANONICAL_TRANSPORT_AMONG_EXAMINED_MECHANISMS   # bloqueo adicional, no terminal primario
```

El terminal primario lo fija Gate 1 por precedencia (§17): al no quedar establecida una pantalla
estable codim-2, aplica `C6_BLOCKED_NO_STABLE_CODIM2_SCREEN`, y el fallo de transporte lo refuerza de
forma independiente.

---

## 10. Gate 4 — ramas nulas y signo de expansión (bloqueo independiente, adicional)

Aunque el terminal ya queda fijado en Gate 3 por precedencia, se registra que Gate 4 **también**
falla, reforzando la imposibilidad (no es trabajo futuro salvable):

- **¿Dos ramas análogas a las dos expansiones nulas?** Avanzar `p` y avanzar `q` da dos operaciones,
  pero **no** son ingoing/outgoing: son cambios de las dos *esquinas* del intervalo, que mezclan
  traslación y escala (crecer el diamante por arriba vs. encogerlo por abajo), no dos congruencias
  nulas de una misma superficie. No se declara la existencia de dos expansiones nulas por el mero
  hecho de que el intervalo tenga dos extremos.
- **Simetría física/combinatoria de las ramas.** No establecida order-only.
- **Futuro real vs deformación pasada.** No hay orientación intrínseca que asigne "evolución futura"
  a una rama y "deformación pasada" a la otra sin una orientación geométrica externa.
- **Signo de `ΔA`.** `|W|` puede crecer o decrecer por **puro cambio de escala** del intervalo
  (§8, §11 falsif. 4). Sin transporte cerrado (Gate 3) ni orientación order-only, **no** puede
  asignarse signo a `ΔA`. Solo cabría "cambio de cardinalidad sin interpretación de signo", que se
  registra como limitación.
- **Consecuencia.** El concepto de trapping queda **bloqueado** aunque la pantalla exista, por falta
  de separación intrínseca suficiente. Esto es coherente con — y subordinado a — el bloqueo de
  transporte de Gate 3.

---

## 11. Falsificadores conceptuales mínimos (contratos, **sin construir ni ejecutar**)

Se definen los contratos de futuros sintéticos necesarios; ninguno se implementa, sprinkla ni evalúa.

1. **Pantalla vacía.** Intervalo interno admisible con `W(p,q)=∅`. Contrato esperado: **abstención**
   del objeto, nunca "área cero" física.
2. **Pantalla singleton.** `|W(p,q)|=1`. Contrato: decidir si se acepta como pantalla o se rechaza
   por dimensión insuficiente; una antichain de un punto no sostiene noción de "superficie".
3. **Pantallas múltiples sin transporte único.** Una pantalla con dos continuaciones order-only
   igualmente válidas. Contrato: **ramificación explícita o abstención**, nunca desempate por
   etiquetas.
4. **Cambio de escala sin transporte físico.** Dos intervalos anidados `[p,q] ⊂ [p',q']` con `|W|`
   distinto pero sin razón para considerarlos la misma pantalla. Contrato: demostrar por qué comparar
   cardinalidades **sin** transporte es inválido (es el argumento de §9.3).
5. **Truncación superior.** Una pantalla/secuencia que cambia al retirar capas maximales. Contrato:
   debe poder activar en el futuro una condición `TRUNCATION_DOMINATED` (no se implementa ahora ese
   terminal empírico).
6. **Caja MINK simétrica.** La familia de pantallas no debe seleccionar arbitrariamente una secuencia
   preferente en una geometría simétrica.
7. **Inhomogeneidad de densidad.** Cambios de `|W|` provocados solo por densidad no deben confundirse
   con expansión física.
8. **Relabeling.** Familia, transporte y cualquier terminal deben ser **exactamente** invariantes
   bajo permutaciones (verificado conceptualmente para `W` y `|W|` en §5, §8; el transporte falla
   antes de poder testarse).

---

## 12. No dependencia de C5 (comprobación conceptual)

C6 **no** reutiliza el canal `partición de minimales → región`:

| Insumo prohibido de C1–C5 | ¿Usado por C6? |
|---|---|
| Matrices de futuros comunes entre minimales | NO |
| Twins | NO |
| Bridges | NO |
| Bloques de minimales | NO |
| Pared lateral como etiqueta | NO |
| Mapa a región espacial | NO |
| `Min(C)` como región de partida | NO |

C6 opera sobre pares internos `(p,q)`, intervalos internos y antichains `W(p,q)`. **Matiz honesto
(alcance corregido — comité 044):** el *bottleneck* de transporte (§9.1) **se parece** al mismo objeto
de vecindad lateral order-only que C4/C5 encontraron esquivo, y para la variante simétrica del
mecanismo A la reducción es válida (§9.5). Pero la imposibilidad de C4/C5 es **acotada**, no un
teorema universal: la Decision 039 la limita a "the two audited families" y **no** refuta métodos
`2-link` (`docs/comite/comite_decision_039_...md:384-401`). Por tanto el nexo con C4/C5 es
**herencia por analogía / plausibilidad**, no transferencia de teorema, y **no** es el terminal
primario de este documento (lo es Gate 1, §17). Esto **no** reabre C5: no se ejecuta ninguna
partición de minimales ni se reintroduce `E_M`; se respeta explícitamente la prohibición C42 §6 de
"arreglar `F3` con ε-clustering o grafo de vecinos no resuelto". El transporte se registra como
bloqueo **adicional independiente**, reforzando —no fundando— el negativo.

---

## 13. Relación con ladders y PR009

- Las **ladders** (EGS Def. 1; `dev/measure_kbeam_peeloff.py`) son **trazadores de trayectorias /
  geodésicas nulas candidatas**: rungs `(p_i,q_i)` apilados a lo largo de profundidad.
- `W(p,q)` pretende ser una **antichain-pantalla interna** de un único intervalo, no una trayectoria.
- **C6 no reutiliza el beam observable de PR009.** El beam de PR009 (prereg §§5.2–5.4) es la anchura
  transversal de un *ensemble* de continuaciones (`D(u,v)=sqrt(min|[e,f]|)`, `W_k=lower_median`,
  `θ_raw=Δlog W`): un **resumen de población de ladders**, no una cintura interna. La novedad
  pretendida de C6 es una pantalla de tipo codim-2 asociada a un intervalo, objeto distinto.
- C6 **no** depende de cruces de ladders; la generalización a dimensiones superiores de los mecanismos
  de crossing **no está resuelta** (§10, §14 riesgo 9).
- El cierre de PR009 fue `FAILED_DATA_CONTRACT` **previo al scoring** (cobertura reference-MINK
  insuficiente a profundidad 7); **no** constituye un resultado físico negativo contra esta línea, ni
  a favor. No se inspecciona, resume ni reutiliza ningún valor interno de PR009.
- **Verificación de atribución (EGS).** La motivación de *focusing* de EGS (expansión `Θ=(1/A)dA/dλ`,
  cambio de signo a través del horizonte, ec. (12)) motiva estudiar cintura↔área, pero **no**
  proporciona por sí sola transporte de pantallas: EGS obtiene expansión a lo largo de una **ladder
  ya trazada** (una trayectoria con identidad), no transportando una antichain-cintura. No se
  sobreatribuye a EGS un resultado de transporte de superficies.

---

## 14. Relación con intervalos y acción Benincasa–Dowker

Las **abundancias de intervalos**, los **perfiles de intervalos** y la **acción BD** informan sobre
**curvatura o manifoldlikeness** (Benincasa–Dowker; `biblioteca/derived-md/Benincasa_Dowker_2010_*`),
pero **no** proporcionan automáticamente: (i) una pantalla codimensión dos; (ii) transporte de la
pantalla; (iii) signo de expansión; (iv) marginalidad. Son un target físico **distinto** (curvatura,
dimensión efectiva), con su propio confound de densidad/dimensión en el null (ya visto en C2, C42
§3). **No se abre una vía BD dentro de C6** (coherente con el menú C42 §7 C6-B, no autorizado).

---

## 15. Riesgos explícitos

1. `W(p,q)` puede ser **casi siempre vacío o singleton** en el régimen relevante.
2. Puede ser **demasiado raro** hallar bi-enlaces dobles simultáneos en el patch de interés.
3. `|W|` puede medir **densidad o tamaño de intervalo**, no área.
4. El **transporte no es único** (demostrado, §9).
5. Cambiar `(p,q)` puede cambiar **escala, no profundidad**.
6. La **orientación del signo** puede no existir order-only (§10).
7. La pantalla puede **depender del techo** (truncación, §11 falsif. 5).
8. Enumerar todos los pares internos puede ser **prohibitivo** (§16).
9. El mecanismo puede funcionar **solo en dimensiones bajas** (crossing 1+1D no generaliza).
10. La interpretación de **codim-2** puede carecer de sustento suficiente.
11. La familia puede ser **globalmente descriptiva pero no formar trayectorias** de pantallas.
12. El único objeto viable podría terminar siendo un **clasificador global**, no trapping cuasi-local
    (posible caída futura al régimen `C6_ONLY_GLOBAL_CLASSIFICATION_REMAINS` si algún día se cerrara
    el transporte, cosa que aquí no ocurre).

---

## 16. Presupuesto computacional conceptual (cualitativo, sin tiempos inventados)

Estimado desde las estructuras ya presentes en el repo (matriz de pasado `C`, reducción transitiva
`L`, CSR de link-hijos en `gpu_link_csr`, `dev/measure_kbeam_peeloff.py`):

- **Pares comparables internos:** `O(N²)` en el peor caso (fracción del `N²` con `p ≺ q` y
  pasado/futuro no vacíos). Para `N` de orden miles, `N²` de orden 10⁶–10⁷ pares.
- **Identificar enlaces `≺*`:** ya disponible; la reducción transitiva `L = C & ~((C·C)>0)` es la
  operación cara (`C·C` matmul, `O(N³)` o su equivalente en bitset/GPU), pero **se reutiliza** una
  sola vez.
- **Construir `W(p,q)`:** por par, intersección de la columna de link-hijos de `p` con la fila de
  link-padres de `q` (dos slices de `L`), `O(N)` con bitset ⇒ `O(N³)` para toda la familia. Reutiliza
  índices existentes.
- **Buscar transporte:** relacionar pantallas exige comparar **pares de pantallas**, `O(N⁴)` naïf —
  **prohibitivo** y, además, sin regla cerrada que justificar (§9).

**Cuello de botella:** no es el coste de construir `W` (factible al `N` actual reutilizando `C`, `L`
y el CSR), sino (a) conceptualmente, que **no queda establecida una pantalla estable codim-2**
(Gate 1, §7) y, de forma independiente, la **ausencia de transporte order-only canónico cerrado entre
los mecanismos examinados** (§9); y (b) computacionalmente, la **enumeración de relaciones entre
pantallas** (`O(N⁴)`). El subresultado `C6_BLOCKED_UNCOMPUTABLE_SCREEN_FAMILY` sería aplicable a la
enumeración de transporte, pero es secundario: el terminal primario lo fija Gate 1 por precedencia.
El terminal final pertenece a la lista autorizada.

---

## 17. Criterio de precedencia aplicado

*(Alcance corregido tras la revisión del comité — `docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md`.)*

1. `C6_BLOCKED_NO_STABLE_CODIM2_SCREEN` — **APLICA (primer terminal por precedencia).** `W(p,q)`
   existe y es una antichain (§5), pero **no queda establecida una familia estable de pantallas
   codim-2**: la abundancia y la estabilidad `|W|≥2` son irresolubles order-only sin ejecución, el
   régimen accesible doc-only es singleton/vacío-dominado (contraejemplo de la cadena, §7), y la
   codim-2 es físicamente insostenible en un patch 1+1D (§6, §14). La precedencia usa el **primer**
   terminal aplicable: al no admitirse una interpretación mínima de pantalla *estable/codim-2*, este
   es el terminal.
2. `C6_BLOCKED_NO_INTRINSIC_SCREEN_TRANSPORT` — **no se emite como terminal**, pero el fallo de
   transporte (§9) se **conserva como bloqueo adicional independiente**: aun si existiera una familia
   estable, no hay transporte order-only canónico cerrado entre los mecanismos examinados. Refuerza el
   negativo sin fundarlo.
3. `C6_ONLY_GLOBAL_CLASSIFICATION_REMAINS` — no se alcanza (requeriría pantalla estable + transporte).
4. `C6_INTRINSIC_DIAMOND_SCREEN_CONCEPT_CLOSED` — no se alcanza; no se declara concepto cerrado con
   pantalla estable, transporte o signo como trabajo futuro indefinido (§7, Gate 3 §9, §10).

---

## 18. Terminal final

```text
C6_BLOCKED_NO_STABLE_CODIM2_SCREEN
CANDIDATE_6_NOT_OPENED
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
```

Bloqueo adicional independiente (no terminal primario):

```text
GATE3_TRANSPORT = NO_CLOSED_CANONICAL_TRANSPORT_AMONG_EXAMINED_MECHANISMS
```

Resumen de un renglón: el objeto-pantalla `W(p,q)` está bien definido y **es una antichain** (probada
order-only), y `|W|` es una cardinalidad cerrada provisional; pero **no queda establecida una familia
estable de pantallas codim-2** — la abundancia y la estabilidad `|W|≥2` son irresolubles order-only
sin ejecución, el régimen accesible doc-only es singleton/vacío-dominado (§7), y la codim-2 es
físicamente insostenible en un patch 1+1D (§6, §14). De forma **independiente**, tampoco existe un
transporte order-only canónico cerrado entre los mecanismos examinados (§9), ni un signo de expansión
asignable order-only (§10). C6 queda bloqueado en la pantalla estable codim-2, reforzado por el fallo
de transporte; no se abre `CANDIDATE_6`.

---

## 19. Confirmación de disciplina

- No se ejecutaron semillas. No se generaron datos. No se implementó código. No se añadieron tests.
  No se construyeron posets sintéticos. No se congeló ni tocó ningún contrato. No se modificó
  `thresholds.py`, manifests, ledgers, terminales ni evidencia. No se reutilizó el beam de PR009.
  No se usaron coordenadas, embedding, paredes del dominio ni etiquetas geométricas. No se seleccionó
  región vía minimales. `W(p,q)` no se presentó como superficie marginal, horizonte ni pantalla
  física demostrada. No se atribuyó codim-2, expansión ni trapping como resultado. No se convirtió la
  adjudicación en `CANDIDATE_6` operativo.
- Este documento es el **único** archivo de la tarea; no se modificó ningún otro; no hay commit ni
  push; el resto del worktree no se tocó.

```text
COMMITTEE_DECISION_043 = C6_BLOCKED_NO_STABLE_CODIM2_SCREEN
OBJECT = INTERNAL_ALEXANDROV_WAIST_SCREENS W(p,q)
ANTICHAIN_PROPERTY = PROVED_ORDER_ONLY
SCREEN_EXISTENCE = PROVED_ORDER_ONLY
SCREEN_STABLE_CODIM2 = NOT_ESTABLISHED (abundancia/|W|≥2 irresoluble sin ejecución; 1+1D sin 2-superficie)
AREA_PROXY = |W|  (CLOSED_PROVISIONAL_NOT_PHYSICAL)
TRANSPORT = NO_CLOSED_CANONICAL_TRANSPORT_AMONG_EXAMINED_MECHANISMS (bloqueo adicional independiente)
SIGN_ORIENTATION = NOT_AVAILABLE_ORDER_ONLY
CANDIDATE_6 = NOT_OPENED
C1_C5_LOCALIZER_LINE = STILL_CLOSED_NOT_REOPENED
REVISION = comite_decision_044 (terminal 2→1; over-claims de §7/§9/§12 corregidos)
```
