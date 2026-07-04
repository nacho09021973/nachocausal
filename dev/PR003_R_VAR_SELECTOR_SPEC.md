# PR-003 — Especificación R-VAR: selector variacional intrínseco de la referencia R (vía C1 directa, candidato cerrado-salvo-freeze)

> **SUPERSEDED (2026-07-03/04) por `dev/PR003_R_VAR_SELECTOR_SPEC_V2_1.md`**, vía v2
> (`dev/PR003_R_VAR_SELECTOR_SPEC_V2.md`, también superseded). Comité 015 encontró V.1
> mal definida y otros gaps sobre esta v1; comité 017 encontró que la revisión v2 seguía
> cerrando tres puntos en la letra, no en la sustancia. Conservada aquí solo como registro
> histórico; donde v1 y v2.1 difieran, **v2.1 gobierna**.

Status: **dev nota conceptual, solo escritura. Sin código, sin simulación, sin enumeración, sin
Alloy, sin Lean, sin datos, sin freeze, sin commit.** Esta sesión responde a la instrucción directa
del PI: "busco [el] único R distinguible intrínsecamente que produzca un horizonte no degenerado y
causalmente coherente; esa es tu misión, encontrarlo".

Esta nota pertenece a la **vía R directa de C1** (el vocabulario de
`dev/PR003_C1_REFERENCE_ALTERNATIVES.md` la llama "R selector"; comité 010 dejó como salida
explícita `COMPLETION_NONIDENTIFIABILITY_NOT_ESTABLISHED_RETURN_TO_R_SELECTOR`). **No reabre la
vía Q**: se preservan sin cambio `Q_DISPOSITION = Q_DIAGNOSTIC_CANDIDATE_ONLY`,
`OVERALL_VERDICT (comité 014) = Q_REFERENCE_PATH_REMAINS_BLOCKED`, `R=Max(C) = REJECTED_TRIVIAL`,
`GROUNDEDNESS_DECISION = G1`, `CONVEXITY_REQUIREMENT = MANDATORY_FOR_C1`, y todos los tokens del
encabezado de `dev/PR003_Q_A6_4_ROBUST_ABSTENTION_SPEC.md`. Las prohibiciones de ejecución del
comité 014 ("cualquier simulación, sprinkling, enumeración o búsqueda de contraejemplos") se
respetan literalmente: **nada de lo derivado aquí ha sido ejecutado ni verificado numéricamente**.

## 0. Fuentes leídas esta sesión

| Archivo | Uso |
|:---|:---|
| `formal/HorizonFormal/HorizonFormal/Horizon.lean` (versión commiteada, `git show HEAD`, commit 110e4af) | Definiciones `RelationalPast`, `RelationalBlackRegion`, `RelationalHorizon` (orientación corregida, líneas 64-68), `relationalBlackRegion_no_escape` (línea 110), tombstone `relationalHorizonOld_eq_empty` (línea 120) |
| `dev/PR003_C1_REFERENCE_ALTERNATIVES.md` | Requisito vinculante de todo candidato R; rechazo de R=Max(C); R1/R2/R3 y sus bloqueos |
| `dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md` | Auditoría A1-A6; exclusión de O(i); regla anti-desempate; primalidad modular |
| `dev/PR003_Q_A6_4_ROBUST_ABSTENTION_SPEC.md` | Firmas admisibles (perfil de incomparabilidad, grados de cobertura); regla de cierre composicional II.1; mitigación M1; familia de realizadores ℜ(C); forma relacional S2; abstención tipada |
| `docs/comite/comite_decision_014_q-reference-rule-disposition.md` (bloques normativos) | Prohibiciones vigentes; disposición diagnóstica de Q |
| `docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md` (veredicto) | `RECOMMEND_REVISE_AND_RECONVENE`; contraejemplos Alloy 001/002 a escala `exactly 4 Element`; obstrucción lógica "supported" |
| `dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md` | Estatus de la obstrucción: soportada como obstrucción lógica, sin no-go físico |

**Advertencia de estado del repositorio (registrada, no corregida por esta sesión):** el working
tree actual de `Horizon.lean` ha revertido la corrección de orientación del commit 110e4af — la
definición en disco es la orientación `B_R→A_R`, **provablemente vacía para todo R** (el propio
tombstone `relationalHorizonOld_eq_empty` lo demuestra). Toda esta especificación usa la
**orientación corregida commiteada** (links infalling, `A_R→B_R`, Dou–Sorkin). Si la reversión del
working tree es accidental, debe restaurarse antes de cualquier trabajo formal.

---

# Parte I — Colapso del espacio de candidatos

Notación: `C` poset finito; `↓X := {x : ∃y∈X, x ≤ y}`; para una referencia `R ⊆ C`,
`A_R := ↓R` (`RelationalPast`), `B_R := C ∖ ↓R` (`RelationalBlackRegion`), y

```text
H[C;R] := { (x,y) : x ∈ A_R, y ∈ B_R, x ⋖ y }        (orientación corregida, Horizon.lean:64-68)
```

**Lema 1 (colapso).** `A_R`, `B_R` y `H[C;R]` dependen de `R` solo a través de `↓R`, que es un
down-set; y todo down-set `D` cumple `D = ↓D`. Por tanto el espacio de candidatos es,
canónicamente, el **retículo de down-sets** `𝒟(C)`, no el conjunto `2^C` de referencias crudas.
Dos referencias con el mismo down-closure son indistinguibles para toda la maquinaria H.
*Prueba:* inmediata de las definiciones; `↓↓R = ↓R` por transitividad. **[derivación de esta
sesión, no verificada mecánicamente — formalizable en Lean en una línea cuando se autorice]**

**Compromiso definicional D-ANCHOR (única decisión física de la Parte I).** Se restringe a cuts
**anclados al borde futuro**:

```text
D = ↓( D ∩ Max(C) )
```

es decir, todo elemento que "escapa" escapa *a través del final del parche*. Base principiada: la
lectura física de `R` es "futuro de escape/asintótico" (`Horizon.lean:17`); en un parche finito el
único futuro disponible es su borde futuro, y un sector de escape que muere a media altura del
parche declararía escape sin testigo de salida. Nota: esto **no** reintroduce `R=Max(C)`
(rechazado `REJECTED_TRIVIAL`): el cut usa un **subconjunto propio** del borde futuro; Max(C)
entero es exactamente el caso excluido por N1 abajo.

```text
𝒜₀(C) := { D ∈ 𝒟(C) : D = ↓(D ∩ Max(C)), D ≠ ∅, D ≠ C }
```

`𝒜₀(C)` es order-only, sin parámetros, invariante bajo isomorfismos (transporte obvio), y
equivale a la elección de un subconjunto propio no vacío `M ⊆ Max(C)` módulo `↓M = ↓M'`.

---

# Parte II — Lemas de decoración (qué condiciones NO pueden discriminar)

La regla fundacional del proyecto ("a guardrail that cannot fail is decoration") obliga a auditar
qué condiciones "duras" son automáticas antes de ponerlas en una definición.

**Lema 2 (one-way automático).** Para todo `D ∈ 𝒟(C)`: ninguna relación causal sale de `B_D`
hacia `A_D` (es `relationalBlackRegion_no_escape`, Horizon.lean:110 en HEAD). Por tanto
"orientación one-way" **no puede ser condición de admisibilidad ni término del score**: la
satisface todo candidato.

**Lema 3 (interfaz no vacía casi-automática).** Si el diagrama de Hasse de `C` es débilmente
conexo y `D ∉ {∅, C}`, entonces `H[C;D] ≠ ∅`; y **toda** arista de Hasse entre `D` y `B_D` está
orientada de `D` hacia `B_D` (si `y ⋖ x` con `x∈D`, `y∈B_D`, entonces `y < x ∈ D` da `y ∈ D`,
contradicción). *Consecuencia:* "produce interfaz no vacía" tampoco discrimina entre candidatos
propios sobre un causal set conexo. **[derivación de esta sesión]**

**Corolario (inventario honesto).** De la lista de siete condiciones duras propuesta en la sesión
previa del PI, son automáticas para todo `D ∈ 𝒜₀(C)` sobre C conexo: no-vacuidad de H (Lema 3),
orientación one-way (Lema 2), testigos de cover (Lema 3), separación causal a ambos lados
(`D ≠ ∅ ≠ B_D` por definición), y no-coincidencia con `C` o `R` (por properness y Lema 1). La
**única** condición dura no automática disponible al nivel puramente lógico es:

```text
N3 (testigo de atrapamiento ab initio):   B_D ∩ Min(C) ≠ ∅
```

Base principiada de N3: un horizonte de eventos en el parche Schwarzschild eterno atrapa **desde
la rebanada inicial**; un artefacto de pared de muestreo solo "atrapa" a tiempos tardíos. N3 es
order-only, sin parámetros, invariante, y excluye exactamente los cuts de losa tardía
(pared superior). Su dual `D ∩ Min(C) ≠ ∅` es automático (todo down-set no vacío contiene un
minimal). Definimos:

```text
𝒜(C) := { D ∈ 𝒜₀(C) : B_D ∩ Min(C) ≠ ∅ }        (familia admisible, cerrada, sin parámetros)
```

---

# Parte III — Dos teoremas de degeneración (por qué ningún score ingenuo funciona)

Ambos son análisis geométricos sobre el parche continuo intencionado (1+1D Schwarzschild,
ingoing-EF, caja `[0,T]×[0,R_max]` con truncación en la singularidad r=0), **no verificados
numéricamente** (sin ejecución esta sesión) y condicionales a la geometría del generador sellado.

**T1 (degeneración por techo — máximo).** Los elementos ⊆-maximales de `𝒜(C)` no localizan el
horizonte: agrandar `D` añadiendo maximales de pared interiores (r<2M, t*=T) sigue siendo
admisible mientras quede algún minimal cerca de la singularidad que no alcance a ningún elemento
de `M`. El cut ⊆-maximal separa "lo que sobrevive hasta t*=T" de la **cuenca de la singularidad**,
no el exterior del interior. Maximizar `|D|` (o `|H|`, correlacionado) selecciona la cuenca —
exactamente la solución degenerada que la sesión previa del PI anticipó.

**T2 (degeneración por suelo — mínimo).** Los elementos ⊆-minimales de `𝒜(C)` son conos pasados
de maximales individuales de pared lejana (`D = ↓{m}`), admisibles (los minimales interiores
quedan en `B`), pero su `B` contiene además exterior tardío no atrapado en ningún sentido físico.
Por tanto la **intersección ingenua** `⋂{B_D : D ∈ 𝒜(C)}` y `⋂{D : D ∈ 𝒜(C)}` localizan
respectivamente la cuña profunda de la singularidad y una esquina del parche — no el horizonte.
El agregado "core/envelope" sobre la familia admisible **cruda** es canónico pero apunta al
objeto equivocado.

**Conclusión de la Parte III.** La estructura de orden de `𝒜(C)` bajo ⊆, por sí sola, no
distingue el cut-horizonte. Cualquier selector que funcione necesita un funcional adicional.

---

# Parte IV — Colimación: la estructura real de la familia admisible

Hecho geométrico del continuo **[estándar, no anclado a cita primaria esta sesión — verificar
contra biblioteca/ antes de freeze]**: la frontera de todo cut anclado `↓M` es una curva causal
acronal generada (en su tramo relevante) por el rayo nulo saliente que llega al punto de anclaje
en la pared. En Schwarzschild, el horizonte r=2M es el **atractor pasado de la congruencia nula
saliente**: todo rayo nulo saliente, exterior o interior, trazado hacia atrás converge a r=2M a
ritmo exponencial `e^{-κΔt}` con κ la gravedad superficial (κ como exponente de Lyapunov del
horizonte). Consecuencia:

```text
COLIMACIÓN: las fronteras de TODOS los cuts admisibles coinciden con el horizonte salvo
O(e^{-κΔt}) a profundidad Δt bajo la pared. El desacuerdo entre cuts admisibles se concentra
en la última banda ~1/κ del parche.
```

Esto da significado geométrico a dos resultados ya aceptados del proyecto: (i) el **suelo de
Le Cam O(ℓ)** (la banda de desacuerdo cerca de la pared es exactamente la región que
completaciones admisibles distintas reclasifican — comités 010/012, Alloy 001/002); (ii) el FAIL
de cobertura de prereg-002 v1 y la mejora del observable de volumen. La familia admisible es un
**lápiz nulo colimado sobre el horizonte en el pasado profundo, que se abre en abanico solo cerca
de la pared**.

---

# Parte V — No-go lógico ⟹ necesidad estadística

**Tesis V.1 (registrada como conjetura formalizable, no como teorema).** Bajo la clase de
completación puramente combinatoria (sin física adicional más allá del orden), todo cut propio
anclado es reversible por completación: para cualquier maximal `m ∈ Max(C)` existen completaciones
admisibles donde `m` escapa y completaciones admisibles donde `m` está condenado. Entonces
**ningún invariante lógico order-only puede condenar a ningún elemento**, y por tanto no existe
"el único R" como cut lógico individual. Esto es la forma R-directa de la obstrucción de
completación/truncación (comités 010/012, obstrucción lógica "supported"); los contraejemplos
Alloy 001/002 a escala 4 elementos ya exhiben el mecanismo.

**Consecuencia V.2.** La información de horizonte que sí está en el orden finito es
**estadística**: la truncación de futuros por la singularidad (la bimodalidad de volumen futuro
sobre minimales que el PASS de prereg-002 midió). Cualquier selector que localice el horizonte
debe explotar esa asimetría estadística — y por tanto lleva una escala ℓ y hereda el suelo O(ℓ).
"Único R distinguible intrínsecamente" solo puede significar: **único objeto de consenso, con
banda de abstención del tamaño del suelo de información**.

**Tensión anti-circularidad (declarada, no resuelta aquí).** El único imprint order-visible del
horizonte en este parche es la truncación de futuro — la misma familia de cantidades que el
estimador sellado usa. La resolución propuesta para comité: (i) separación de roles — el selector
R-VAR **define** la referencia; el estimador sellado **valida** en el benchmark; el embedding
oculto solo puntúa (regla fundacional); (ii) el funcional de R-VAR se construye sobre **grados de
enlace** (`sig_lk`, componente ADMISSIBLE en la auditoría A6.4 II.2, eje sancionado por §7.5:
"la asimetría debe leerse de la estructura de enlaces"), que **no determina funcionalmente**
`O(x)` (la regla de cierre composicional A6.4 II.1 prohíbe determinación funcional; los enlaces
no fijan el volumen). Se registra honestamente: en 1+1D el grado de enlace futuro esperado crece
como `ln(volumen futuro) + γ` **[derivación estándar de sprinkling 2D, esbozo:
E[d⁺] = ∫∫ ρe^{-ρuv}du dv ≈ ln(ρV)+γ; PLAUSIBLE, no verificada, no anclada a cita]** — es un
proxy logarítmico ruidoso de la cantidad prohibida, no la cantidad. Si el comité juzga que esto
viola el espíritu de la exclusión de O(i), el funcional alternativo es el perfil de
incomparabilidad (`sig_sp`, la otra componente ADMISSIBLE), con menor alineación física.

---

# Parte VI — El candidato cerrado R-VAR

Los cuatro objetos exigidos por el planteamiento variacional:

## VI.1 Familia de candidatos

```text
𝒜(C) = { D ⊆ C : D = ↓(D ∩ Max(C)),  ∅ ≠ D ≠ C,  (C∖D) ∩ Min(C) ≠ ∅ }
```

Order-only, sin parámetros, total (computable para todo C finito), invariante.

## VI.2 Condiciones duras (con inventario de automaticidad)

| Condición | Estatus |
|:---|:---|
| `H[C;D] ≠ ∅` | AUTOMÁTICA sobre C conexo (Lema 3) — se enuncia como teorema, no como guardia |
| one-way `B→A` prohibido | AUTOMÁTICA (Lema 2) — ídem |
| separación bilateral | AUTOMÁTICA (properness) |
| anclaje al borde futuro | DEFINICIONAL (D-ANCHOR) |
| atrapamiento ab initio N3 | **la única guardia real** |
| invarianza bajo Aut/iso | POR CONSTRUCCIÓN (VI.5) |

## VI.3 Score

Para `D ∈ 𝒜(C)`, con `H = H[C;D]` y `d⁺(z) := #{w : z ⋖ w}` (grado de cobertura futuro,
firma 5 / `sig_lk` de A6.4, componente ADMISSIBLE):

```text
S(C,D) := media_{(x,y) ∈ H} [ d⁺(x) − d⁺(y) ]
```

el **contraste de valencia futura a través de la interfaz**, lado escape menos lado atrapado.
Justificación física: el lado atrapado tiene futuros truncados por la singularidad ⟹ valencia
futura deprimida; en un cut de pared ambos lados están igualmente truncados ⟹ contraste ≈ 0; en
un cut de cuenca el "exterior" inmediato también está condenado ⟹ contraste ≈ 0. El máximo de
contraste se espera en el horizonte. **[predicción física, NO evaluada — la evaluación requiere
autorización de comité]**. La forma exacta del estadístico (media vs mediana, normalización por
|H|, mínimo de |H|) es **la única elección de freeze pendiente**, a fijar con base principiada
antes de cualquier dato de validación, junto con el margen de abstención μ calibrado sobre
parches nulos sin horizonte (esto conecta directamente con el eje (iv) de falsos positivos aún
abierto de estimator-v2).

## VI.4 Regla de selección, empate y abstención

```text
𝒜*(C) := argmax_{D ∈ 𝒜(C)} S(C,D)                        (conjunto, nunca un elemento forzado)

R-VAR(C) := ( T(C), E(C), U(C) )   donde
  T(C) := ⋂_{D ∈ 𝒜*(C)} (C ∖ D)      — núcleo atrapado por consenso
  E(C) := ⋂_{D ∈ 𝒜*(C)} D            — núcleo de escape por consenso
  U(C) := C ∖ (T(C) ∪ E(C))          — banda de abstención

R-VAR(C) := ⊥ (abstención total, tipada) si:
  τ=EMPTY_FAMILY      𝒜(C) = ∅
  τ=LOW_CONTRAST      max S < μ  (margen frozen; sin señal de horizonte — parche nulo)
  τ=INCOHERENT_ARGMAX T(C) = ∅ ∨ E(C) = ∅  (los máximos no forman lápiz coherente)
```

Sin desempate lexicográfico, sin índices, sin colapso forzado a un único cut: el output es la
tri-partición de consenso — la forma multivaluada+abstención que la Parte V del desarrollo Q ya
recomendó como única estrategia robusta, aplicada ahora a R directamente. Por la colimación
(Parte IV), la **predicción falsable** es: en parches con horizonte, `U(C)` se concentra en la
banda ~1/κ bajo la pared y `T/E` recuperan interior/exterior en el pasado profundo; en parches
nulos, abstención total por LOW_CONTRAST.

## VI.5 Equivarianza

Todo objeto de VI.1–VI.4 está definido exclusivamente con `≤`: la familia es invariante, `S` es
un invariante de isomorfismo por término, `argmax` de un invariante sobre una familia invariante
es invariante como conjunto, y las intersecciones son funciones simétricas. Por tanto
`R-VAR(φC) = φ(R-VAR(C))` para todo isomorfismo φ, sin ninguna regla de desempate que romper.
**[argumento directo por construcción; sin prueba mecánica — mismo estatus que la naturalidad
de Q]**

## VI.6 Computabilidad (nota, no compromiso)

`|𝒜(C)|` es exponencial en general, pero bajo `dim_DM(C) ≤ 2` (Prop. 7.3, condicional) los
down-sets anclados son caminos-escalera monótonos en cualquier realizador `ρ ∈ ℜ(C)` (Parte III
de A6.4), y un score interfaz-local se optimiza por programación dinámica en tiempo polinomial.
El realizador se usaría **solo como estructura de búsqueda**: `S` y `𝒜` están definidos por `≤`
únicamente, de modo que el resultado es independiente del realizador elegido — el canal
`REALIZER_DISAGREEMENT` de A6.4 no existe para R-VAR. **[esbozo, PLAUSIBLE, no desarrollado]**

---

# Parte VII — Auditoría contra los requisitos vinculantes

```text
order-only                       = SÍ (≤, covers, Min, Max, cardinalidades; sin coordenadas,
                                   sin etiquetas, sin embedding)
deterministic                    = SÍ (conjunto-valuado con abstención tipada; sin aleatoriedad,
                                   sin orden de iteración)
equivariant                      = SÍ_POR_CONSTRUCCIÓN (VI.5; sin prueba mecánica)
nondegenerate                    = N3 + LOW_CONTRAST + INCOHERENT_ARGMAX; no coincide con C, ∅,
                                   Max(C) (properness + Lema 1); puede fallar limpiamente (⊥)
noncircular con el PASS          = CONDICIONAL — funcional sobre sig_lk (ADMISSIBLE en A6.4),
                                   no determina O(x); proxy logarítmico declarado (Parte V);
                                   REQUIERE ADJUDICACIÓN DE COMITÉ
stable under sprinkling/truncation = CONJETURA (colimación, Parte IV) — testable, no testeada
convergent al objeto geométrico  = CONJETURA (mismo mecanismo κ)
Guard-v-checkable                = SÍ (relabel-invarianza verificable por permutación)
hidden embedding                 = solo puntúa; no entra en 𝒜, S, ni abstención
PHYSICAL_IDENTIFIABILITY_STATUS  = NOT_ESTABLISHED (sin cambio; nada aquí lo establece)
```

Elecciones de freeze pendientes (únicas): (F1) estadístico exacto de S y normalización;
(F2) margen μ y su base principiada (nulos sin horizonte); (F3) mínimo de |H| si se adopta.

---

# Parte VIII — Bloque normativo

```text
DOCUMENT_ID = PR003_R_VAR_SELECTOR_SPEC
CANDIDATE_NAME = R-VAR (selector variacional de consenso-argmax con abstención tipada)
CANDIDATE_PATH = C1 vía R directa (no Q; Q_DISPOSITION sin cambio)

R_VAR_FAMILY_STATUS = CLOSED (𝒜(C) sin parámetros, VI.1)
R_VAR_HARD_CONDITIONS_STATUS = CLOSED (una guardia real: N3; inventario de automaticidad VI.2)
R_VAR_SCORE_STATUS = CLOSED_UP_TO_FREEZE (eje fijado: contraste de sig_lk en la interfaz;
  F1-F3 pendientes de freeze pre-validación)
R_VAR_TIE_ABSTENTION_STATUS = CLOSED (consenso-argmax + abstención tipada, VI.4)

DERIVED_THIS_SESSION =
  Lema 1 (colapso a down-sets) | Lemas 2-3 (decoración) | T1/T2 (degeneración techo/suelo) |
  colimación κ (Parte IV) | tesis de necesidad estadística V.1-V.2 | canal proxy-log de sig_lk
STATUS_OF_DERIVATIONS = CONCEPTUAL, NO VERIFICADAS (ni numérica ni mecánicamente); las
  geométricas condicionales al parche del generador sellado

BLOCKING_ADJUDICATIONS_FOR_COMITE =
  (1) tesis V.1 (no-go lógico) — ¿formalizar como proposición Alloy/Lean o aceptar como marco?
  (2) resolución de la tensión anti-circularidad de V.2 (sig_lk como proxy-log declarado)
  (3) autorización de implementación dev + prueba en posets de juguete y sprinkling EXPLORE
      (hoy prohibida por comité 014 NEXT_FORBIDDEN_ACTIONS)
  (4) F1-F3 (freeze del estadístico y margen)
NEXT_RECOMMENDED_ACTION = /comite sobre (1)-(4) con este documento como brief
NEXT_FORBIDDEN_WITHOUT_COMITE = implementación | simulación | Alloy | Lean | freeze | commit

REPO_STATE_FLAG = el working tree de formal/.../Horizon.lean revierte la corrección de
  orientación de 110e4af a la versión provablemente vacía; restaurar antes de trabajo formal
```
