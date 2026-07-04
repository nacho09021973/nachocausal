# PR-003 — R-VAR spec v2.1: selector variacional de consenso con abstención tipada (revisión post-comité 017)

Status: **dev nota de especificación, solo escritura. Sin código, sin simulación, sin
enumeración, sin Alloy, sin Lean, sin datos, sin freeze, sin commit de ejecución.** Escrita en
respuesta a `docs/comite/comite_decision_017_r-var-v2-reconvene.md` (§9, paso reversible 1),
que independientemente verificó los nueve cierres (a)-(i) autoreportados por v2 y encontró que
tres — (a) el cuantificador de V.1a, (c) el testigo de separación C.1, (d) el rol real de F3 —
estaban cerrados en la letra pero no en la sustancia (falsifier de 017). Esta revisión v2.1
corrige exactamente esos tres, más cuatro ajustes menores (§9 de 017), y añade el Gate 0 de
falsación silenciosa que el falsifier de 017 identificó como el hallazgo de mayor severidad.
Sustituye a `dev/PR003_R_VAR_SELECTOR_SPEC_V2.md` (v2), que queda como registro histórico junto
con `dev/PR003_R_VAR_SELECTOR_SPEC.md` (v1); donde v2 y v2.1 difieren, **v2.1 gobierna**. Esta
revisión en sí misma NO constituye ni solicita la autorización scoped de comité 017 §9 paso 3
(S1-S5) — esa sigue pendiente de autorización explícita del PI.

Preservado sin reapertura (tokens vinculantes, verificados por comité 015 §2 y re-confirmados por
comité 017 §2): `Q_DISPOSITION = Q_DIAGNOSTIC_CANDIDATE_ONLY` | `OVERALL_VERDICT (014) =
Q_REFERENCE_PATH_REMAINS_BLOCKED` | `R=Max(C) = REJECTED_TRIVIAL` | `GROUNDEDNESS_DECISION = G1`
| `CONVEXITY_REQUIREMENT = MANDATORY_FOR_C1` (comité 012 D2) | `PHYSICAL_IDENTIFIABILITY_STATUS
= NOT_ESTABLISHED` | `ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED` | prohibiciones de
ejecución de comité 014 vigentes hasta autorización scoped nueva (comité 017 §9 paso 3, S1-S5).

**Etiqueta de dependencia de prereg-002, corregida (comité 017 §2, hallazgo de "cita stale" —
la etiqueta heredada de auditor 005 en v2:17-22 predata y es superseded por lo siguiente):**
prereg-002 fue objeto de una `SUPERVISED_REVERIFICATION` (autorizada por
`docs/comite/comite_decision_016_prereg002-supervised-reverification.md`, ejecutada bajo
`docs/prereg002_reverification_declaration.md`), con resultado **MATCH** en cada uno de los ~60
campos comparados contra la transcripción `fee12d5`
(`docs/prereg002_reverification_result.md`, commit `82b4ede`). El status vinculante de prereg-002
es ahora **`PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]`**
— nunca "PASS" desnudo. Este MATCH verifica que la transcripción es el output real del
instrumento sellado (M); NO restaura el artefacto primario perdido ni la afirmación histórica
"primera y única evaluación" (H), que descansa solo en evidencia documental/git. Toda invocación
del PASS en este documento porta la etiqueta completa entre corchetes. La banda virgen
`VALIDATION_SEEDS` queda **permanentemente quemada** para cualquier comparación de protocolo o
calibración de selector futura (comité 016) — esto vincula directamente a R-VAR v2.1, que debe
usar exclusivamente `EXPLORE_POOL`.

## 0. Fuentes leídas esta sesión (además de las de v1/v2)

| Archivo | Uso |
|:---|:---|
| `docs/comite/comite_decision_017_r-var-v2-reconvene.md` | El mandato de esta revisión — falsifier §5, síntesis §8, next-step spec §9 |
| `docs/comite/comite_decision_015_r-var-selector-adjudication.md` | Los 7 briefs y el mandato §8-§9 originales; cada cierre de abajo cita el hallazgo que lo motiva |
| `docs/comite/comite_decision_016_prereg002-supervised-reverification.md`, `docs/prereg002_reverification_result.md`, `docs/prereg002_reverification_declaration.md` | Cierre del audit de prereg-002 (MATCH), etiqueta de status corregida arriba |
| `docs/comite/comite_decision_012_c1-admissible-completion-class.md` (bloque normativo :330-360) | D1 (cláusulas MANDATORY/DEFERRED de la clase admisible), D2 (convexidad MANDATORY; dim≤2 solo para 𝔄_Schw) |
| `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` (§3-§4, §7) | Vocabulario de cláusulas (a)-(e); requisitos de testigo C1 |
| `dev/explore_seeds.py:23` | Cita correcta de EXPLORE_POOL (cierre (i)) |

---

# Parte A — Cierre (a): la clase de completación 𝒦 y la re-registración de V.1

## A.1 Definición de 𝒦 (por herencia, no por invención)

v1 cuantificaba V.1 sobre una "clase de completación puramente combinatoria" nunca definida —
el lógico de 015 mostró que así V.1 "no tiene valor de verdad", y el matemático que los testigos
Alloy 001/002 viven en completaciones que comité 010:77-78 ya declaró **no admisibles**
(no-convexas, no orden-producto). v2 define dos clases, ambas por referencia a decisiones ya
adoptadas:

```text
𝒦_comb(O) := extensiones finitas C ⊇ O que satisfacen SOLO:
  literal_subposet_preservation (MANDATORY, comité 012 D1) ∧ causal_partial_order (MANDATORY).
  — La clase de los contraejemplos Alloy 001/002. Combinatoria pura, SIN convexidad.

𝒦_adm(O) := 𝒦_comb(O) ∩ {C : convexity(O en C) (MANDATORY_FOR_C1, comité 012 D2) ∧
  hidden_element_localisation_restriction (MANDATORY = convexidad, D1)}.
  — La clase C1 vinculante. Las cláusulas DEFERRED de D1 (schwarzschild_region_compatibility,
  manifoldlikeness, hidden_element_count_restriction) NO se añaden aquí: siguen DEFERRED.

𝒦_Schw(O) := 𝒦_adm(O) ∩ {C : dim_DM(C) ≤ 2} — la subclase nombrada de D2, usada SOLO por la
  nota de computabilidad (Parte E), nunca por la definición del selector.
```

## A.2 V.1 re-registrada (dos proposiciones separadas, estatus honesto)

El falsificador de 015 mostró además que la V.1 de v1 **probaba menos de lo que concluía**: la
reversibilidad cuantificaba sobre `Max(C)` pero la conclusión hablaba de *todos* los elementos.
v2 separa V.1a/V.1b; **el falsifier de comité 017 mostró que V.1a en su forma v2 era, a su vez,
trivialmente satisfacible o ambigua** — fix aplicado abajo (v2.1):

```text
[FIX comité 017 — testigo de trivialidad, cerrado]: la formulación v2 leía "donde escape(Cᵢ) es
CUALQUIER referencia anclada propia de Cᵢ". Bajo esa lectura, tomando C₁=C₂=O, M₁={m},
M₂=Max(O)∖{m}, la proposición se cumple con CERO contenido de completación siempre que
|Max(O)|≥2 y m∉↓M₂ — "cualquier" dejaba la referencia como un grado de libertad elegible POST
HOC por quien prueba la proposición, exactamente el defecto de cuantificador-bajo-especificado
que mató la V.1 de v1 (comité 015), reintroducido un nivel más abajo. v2.1 cierra esto fijando
escape(Cᵢ) a un objeto NO elegible: el núcleo de escape que el propio selector R-VAR calcula.

V.1a (banda de pared; conjetura formalizable, escenario Alloy candidato — v2.1, cuantificador
cerrado):
  ∀ O finito con Max(O) ≠ ∅, ∀ m ∈ Max(O): ∃ C₁, C₂ ∈ 𝒦_adm(O) tales que
  R-VAR(C₁) ≠ ⊥, R-VAR(C₂) ≠ ⊥, m ∈ down(E(C₁)) y m ∉ down(E(C₂)) — donde E(Cᵢ) es,
  específicamente, el núcleo de escape E(C) devuelto por R-VAR(C)=(T,E,U) (Parte D.3) cuando
  R-VAR no abstiene sobre Cᵢ. Ya NO es "cualquier referencia anclada propia": es el output fijo,
  computado, no discrecional, del propio selector.
  ALCANCE: solo elementos cuyo estatus depende de la última banda (la banda Le Cam ya
  concedida). NO implica nada sobre el pasado profundo.
  CONSECUENCIA DE LA REFORMULACIÓN: V.1a ahora es una afirmación SOBRE R-VAR mismo (¿el
  selector, cuando no abstiene, produce núcleos de escape que varían con la completación de la
  forma descrita?), no una afirmación order-teórica independiente que pudiera luego invocarse
  para justificar a R-VAR — la dependencia circular queda evitada porque V.1a sigue sin ser
  premisa del selector (ver más abajo), solo una PREDICCIÓN falsable sobre su comportamiento,
  registrable como candidato de un futuro Alloy 003 únicamente bajo esta forma cerrada.

V.1b (no-go fuerte; conjetura ABIERTA, NO establecida, NO usada por el selector):
  ningún invariante lógico order-only condena a ningún elemento de O bajo 𝒦_adm(O).
  ESTATUS: NEEDS_PRECISE_WITNESS — los testigos existentes (Alloy 001/002) viven en
  𝒦_comb ∖ 𝒦_adm y NO transfieren (comité 010:77-78). Sin testigo en 𝒦_adm, V.1b es solo
  marco. PROHIBIDO citarla como establecida.
```

**Cambio de rol estructural (degradación deliberada):** en v1, V.1 era premisa del programa
("⟹ el selector debe ser estadístico"). En v2 **el selector no depende de V.1**: R-VAR se
sostiene por sus propias garantías (equivarianza, abstención tipada, calibración nula) tanto si
V.1b resulta cierta como si no. V.1a/V.1b quedan como conjeturas motivadoras registradas para
eventual formalización Alloy (V.1a es el escenario natural de un futuro Alloy 003, si un comité
lo autoriza), no como carga estructural.

---

# Parte B — Cierre (b): colapso del fork sig_lk / sig_sp

```text
DECISION_FORK = SIG_LK_ONLY_SIG_SP_REJECTED
```

El único funcional de score de R-VAR es `d⁺(z) := #{w : z ⋖ w}` (grado de cobertura futuro,
segunda componente de `sig_lk`, `dev/PR003_Q_A6_4_ROBUST_ABSTENTION_SPEC.md:302`, estatus
`ADMISSIBLE_COMPONENT` :319). La alternativa `sig_sp` (perfil de incomparabilidad) que v1
ofrecía como escape queda **RECHAZADA**, no diferida, por la razón del falsificador de 015:
sobre elementos minimales, `|spacelike(x)|` determina `O(x)` **exactamente**
(`|spacelike(x)| = |C|−1−|↓x|−|↑x|` con `|↓x|=0`; canal residual II.1 de A6.4:186-195), y la
única guardia real de R-VAR (N3) privilegia precisamente `Min(C)` — sig_sp es el canal *peor*
exactamente donde más importa. Motivo: principiado y estructural, decidido **antes** de ver
ningún dato, como exige la exclusión II.1 ("parámetros elegidos tras observar el resultado").

Queda así eliminado el grado de libertad post-hoc señalado por el lógico de 015 ("segundo fork
sin congelar").

---

# Parte C — Cierre (c): chequeo composicional del selector completo

Obligación II.1 de A6.4 (:186-195): la exclusión de `O(i)` se evalúa sobre el **conjunto** de
primitivas del selector, no primitiva a primitiva. Inventario exhaustivo de primitivas de R-VAR
v2:

```text
P1  pertenencia a Min(C), Max(C)                    (indicadores extremales)
P2  relación de cobertura ⋖ y grado d⁺              (radio 1 en el diagrama de Hasse)
P3  clausura ↓M para M ⊆ Max(C)                     (estructura de anclaje)
P4  pertenencia al interfaz H[C;D] y |H|            (pares de cobertura que cruzan el cut)
P5  aritmética entera exacta sobre sumas de d⁺      (score, Parte D)
P6  cuantil nulo μ_n de max S                       (calibración, Parte F — corre sobre
                                                     ensembles nulos, nunca sobre el patch BH)
```

**[FIX comité 017 — test-object fijado por escrito, antes de cualquier otra cosa.]** El
falsifier de 017 mostró que la obligación II.1 nunca se resolvía en v2 sobre QUÉ objeto exige
la no-determinación: ¿el conjunto de primitivas P1-P6 crudo, o los outputs expuestos del
selector (S, T, E, U, τ)? Bajo la lectura "primitivas crudas", la afirmación es trivialmente
falsa (P2 = la relación de cobertura ⋖, cuya clausura transitiva ES el orden, que determina
`O(x)` exactamente). v2.1 fija, por escrito, que **el objeto del chequeo composicional C.1 son
los outputs expuestos (S, T, E, U, τ) — nunca las primitivas P1-P6 en crudo**. Esta es también
la definición que gobierna `CIRCULARITY_STANDARD = FUNCTIONAL_ONLY` (ver abajo).

**Afirmación C.1 (no determinación funcional de los outputs expuestos, clase por clase).**
Ningún valor de `(S, T, E, U, τ)` producido por R-VAR determina funcionalmente `O(x) = |↑x|`
sobre ninguna clase de elementos relevante para el PASS (que evalúa `O(i)` sobre **minimales**,
`dev/PR003_C1_BCE_CLOSED_CANDIDATE.md` Parte V):

- Sobre `x ∈ Min(C)`: las primitivas ven de `x` su indicador P1, su `d⁺` (radio 1) y su
  pertenencia a interfaces/anclajes; `O(x)` es una cantidad de clausura transitiva global.
  **Testigo de separación, corregido (comité 017 falsifier: el testigo v2 usaba un poset con
  diagrama de Hasse DESCONECTADO — fuera del propio dominio efectivo de R-VAR — y por tanto no
  probaba nada sobre el objeto que R-VAR realmente procesa).** v2.1 usa dos posets, cada uno
  **individualmente conexo** (cadenas simples, sin componentes aisladas):
  `P₁ := cadena x ⋖ a ⋖ b` (3 elementos) y `P₂ := cadena x ⋖ a` (2 elementos). En ambos, `x` es
  el único minimal, `d⁺(x)=1` con el mismo (único) cover `a`, y la vecindad de Hasse de radio 1
  de `x` es isomorfa entre `P₁` y `P₂` (un indicador `Min`, un cover, sin atributos adicionales
  visibles a radio 1). Pero `O(x) = |↑x|` difiere: `2` en `P₁` (`{a,b}`), `1` en `P₂` (`{a}`).
  **Obligación de verificación en el tier de juguete (Gate 0, antes de cualquier freeze):**
  confirmar que, además de `d⁺(x)` coincidir, el output expuesto completo — `S`, la partición
  `(T,E,U)`, y el motivo típico `τ` — coincide (o es indistinguible salvo por la propia
  diferencia de tamaño del poset) entre ambos ejemplos, mientras `O(x)` difiere; solo esa
  construcción, verificada, cierra genuinamente C.1 sobre el objeto correcto (outputs
  expuestos). Esta spec fija el ejemplo y el criterio; la verificación en sí es una obligación
  de Gate 0 (Parte D.3-bis), no algo ya exhibido por este documento.
- Sobre `x ∈ Max(C)`: `O(x)=0` es determinado trivialmente por P1 — pero también lo determina
  la propia definición de maximal, conocida por cualquier observador del orden; no es el
  estadístico del PASS (que corre sobre minimales) ni información nueva.
- La única cantidad agregada que el selector expone es `S` (contrastes de `d⁺` promediados
  sobre H): una función de a lo sumo `2|H|` grados de cobertura, no de ningún `|↑x|`.

**Declaración honesta C.2 (el solapamiento estadístico persiste; adjudicado por comité 017).**
La corrección del matemático de 015 se incorpora: la derivación de v1 `E[d⁺] ≈ ln(ρV)+γ` omitía
el jacobiano nulo ½ y los límites finitos; la forma corregida es
`E[d⁺] ∼ ln(ρ·Área futura) + const`, coeficiente dependiente del esquema — la relación
**monótona en media** con el volumen futuro se mantiene, y su signo es robusto a la corrección
(comité 017, mathematician brief). Por tanto: R-VAR es no circular en el estándar **funcional**
(C.1, ahora definido sobre outputs expuestos) y correlacionado en el estándar
**estadístico-medio**.

```text
CIRCULARITY_STANDARD = FUNCTIONAL_ONLY   [ADJUDICADO por comité 017, §8]
```

**Adopción, con las tres condiciones vinculantes que comité 017 exige (ninguna estaba presente
en v2; sin las tres, `FUNCTIONAL_ONLY` es decoración — falsifier de 017):**

1. **Test-object fijado:** la no-determinación funcional se evalúa sobre los outputs expuestos
   (`S`, `T`, `E`, `U`, `τ`), NUNCA sobre el conjunto crudo de primitivas P1-P6 (ver arriba).
2. **Cláusula NON_CORROBORATION, permanente:** ningún acuerdo futuro entre un veredicto de
   R-VAR sobre un parche BH y el estimador sellado `O_min` puede citarse jamás como
   corroboración independiente del PASS de prereg-002. R-VAR y `O_min` leen el mismo imprint de
   truncación de futuros (comité 015 físico; comité 017 físico) — cualquier coincidencia es
   parcialmente garantizada por construcción, no evidencia independiente.
3. **Etiqueta de limitación permanente:** todo artefacto de R-VAR (spec, resultado, figura)
   debe declarar explícitamente la correlación monótona en media con el volumen futuro
   (`E[d⁺] ∼ ln(ρ·Área futura)+const`) como una limitación reconocida, no silenciarla.

**Nota importante (comité 017, adjudicación explícita, NO el argumento de v2/mathematician
015):** `FUNCTIONAL_ONLY` NO se adopta aquí por el argumento "el estándar fuerte también
condenaría a nuestro propio `O_min` ya sellado" — ese argumento fue señalado por el falsifier de
017 como **razonamiento circular** (toma la admisibilidad de `O_min` como punto fijo en vez de
justificarla independientemente). Se adopta en cambio porque la determinación funcional (una
propiedad decidible, por instancia) es la formalización correcta de lo que
`NO_GROUND_TRUTH_LEAKAGE` realmente prohíbe — que el embedding oculto *defina* el observable —
mientras que la correlación monótona en media con un estadístico order-only *distinto* y ya
aceptado no es ese modo de fallo.

**El fork tal como lo planteaba v2 era, además, un falso dilema (falsifier 017):** adoptar
`FUNCTIONAL_PLUS_MEAN_MONOTONE_BAN` sin más mataría `d⁺` (comité 017 mathematician: el signo de
`∂E[d⁺]/∂(volumen futuro)>0` es robusto a la corrección del jacobiano) y plausiblemente todo
selector funcional en este parche — un guardrail que puede matar el programa. Pero adoptar
`FUNCTIONAL_ONLY` desnudo (sin las tres condiciones arriba) sería un guardrail que NO PUEDE
fallar, porque "determinación funcional" sin fijar el objeto de prueba es trivialmente violable
o casi imposible de violar según la lectura. Las tres condiciones cierran ese hueco.

El firewall real bajo `FUNCTIONAL_ONLY`, con las tres condiciones: separación de roles (selector
define / estimador sellado valida / embedding solo puntúa), calibración **solo sobre nulos**
(Parte F), y el test de falsación mínima del falsificador de 015/017 ejecutado ANTES de
cualquier claim sobre parches BH.

---

# Parte D — El selector v2 (incorpora cierres (d), (e), (h))

## D.1 Familia y guardia (sin cambio de v1, con la condición de conectividad explicitada)

```text
𝒜(C) := { D ⊆ C : D = ↓(D ∩ Max(C)),  ∅ ≠ D ≠ C,  (C∖D) ∩ Min(C) ≠ ∅,  H[C;D] ≠ ∅ }
```

Cambio vs v1: `H[C;D] ≠ ∅` es ahora **condición de pertenencia** (cierra el modo de fallo 2 del
falsificador: "S is not even well-defined on all of 𝒜"). El Lema 3 de v1 garantiza que sobre un
Hasse débilmente conexo esta condición no excluye ningún cut propio — pero la conectividad es
una **hipótesis real** (matemático de 015: sprinklings de baja densidad pueden violarla), de ahí
la abstención tipada D.3.

```text
F3 (CERRADO, pero honestamente REDUNDANTE — relabel comité 017): H_MIN := 1, congelado.
```

**[FIX comité 017 — relabel honesto, no "cierre sustantivo"]:** `H ≠ ∅` ya es condición de
pertenencia de `𝒜(C)` (D.1 arriba), de modo que `H_MIN := 1` NO excluye ningún cut adicional —
coincide exactamente con "S está bien definido" y no añade ningún parámetro libre. v2 llamaba a
esto "cierre... con base principiada"; v2.1 lo etiqueta con precisión: **F3 es un umbral nulo,
redundante con la condición de pertenencia ya existente, NO una salvaguarda independiente
contra el ruido de interfaces pequeños.** Esa carga se traslada íntegramente a la calibración de
valor extremo de μ (Parte F), que incluye por construcción el ruido de los cuts de `|H|`
pequeño en la distribución nula de `max S`. Obligación de reporte (D.4) acompaña.

**Consecuencia compuesta que debe declararse explícitamente (falsifier comité 017, no
observada por ningún brief de comité 015 ni 017-wave-1 individualmente):** dado que
`INCOHERENT_ARGMAX` no puede dispararse bajo un argmax singleton (D.3 abajo, admitido por v2),
y dado que F3 no excluye nada por sí mismo, **la escalera tipada de cuatro motivos de abstención
colapsa, en el caso más común (un óptimo único), a UNA sola comprobación operativa:
`LOW_CONTRAST` frente a μ.** Los otros tres tipos (`DISCONNECTED_HASSE`, `EMPTY_FAMILY`,
`INCOHERENT_ARGMAX`) siguen siendo order-decidables y disparan en sus casos propios, pero no
son cuatro salvaguardas independientes en el caso típico — son una escalera con un solo peldaño
operativo la mayor parte del tiempo. Esto no invalida el diseño (la calibración de valor
extremo de μ es precisamente la respuesta correcta a este hecho), pero debe declararse, no
disimularse detrás de la apariencia de cuatro tipos.

## D.2 Score y regla de argmax con aritmética exacta (cierre (e))

Para `D ∈ 𝒜(C)`, con `H = H[C;D]`:

```text
A(D) := Σ_{(x,y)∈H} [ d⁺(x) − d⁺(y) ]  ∈ ℤ        B(D) := |H| ∈ ℤ₊        S(D) := A(D)/B(D)
```

```text
F1 (CERRADO): S = media aritmética del contraste por link (A/B), representada y comparada
SIEMPRE como racional exacto: S(D₁) ≥ S(D₂) ⟺ A(D₁)·B(D₂) ≥ A(D₂)·B(D₁) en ℤ.
PROHIBIDO comparar en coma flotante (habría hecho el conjunto argmax dependiente de plataforma,
anulando en la práctica el determinismo y la equivarianza — falsificador de 015, modo 6).
Sin mediana (no admite la maquinaria de ratio exacto ni el DP paramétrico), sin normalización
adicional: la media por link es la forma cuya expectativa es el contraste físico predicho
(independiente de |H| en media) y la única con algoritmo exacto cerrado (D.2.1-D.2.2).
```

### D.2.1 Optimización: Dinkelbach entero sobre escaleras (esbozo obligatorio, estatus PLAUSIBLE)

Bajo `dim_DM(C) ≤ 2` (garantizado para la familia generadora — matemático de 015: conformidad
plana 2D; comités 010:72,78 y 011:137), fijado un realizador `ρ=(L_U,L_V)` (solo estructura de
búsqueda; el resultado depende únicamente de `≤`):

1. Los down-sets anclados son caminos-escalera monótonos en la retícula del realizador.
2. Para λ = p/q ∈ ℚ fijo, `max_D [ q·A(D) − p·B(D) ]` es un objetivo **aditivo por arista de
   Hasse cruzada** (cada par de cobertura (x,y) contribuye `q·(d⁺(x)−d⁺(y)) − p` si cruza el
   cut, 0 si no): un camino óptimo en un DAG de pasos de escalera, resoluble por programación
   dinámica en tiempo polinomial con pesos enteros.
3. Iteración de Dinkelbach: λ₀ arbitrario admisible; λ_{k+1} := A(D_k)/B(D_k) como racional
   exacto; parar cuando `max_D [q_k·A − p_k·B] = 0`. Con A,B enteros acotados polinomialmente,
   converge en un número polinomial de iteraciones.

`ESTATUS: SPECIFICATION-CLOSED, PROOF-OPEN` (relabel comité 017 — nunca `[CERRADO]` a secas en
el bloque normativo, Parte H, hasta que Gate 0 (D.2.3) pase) — el paso 2 (que el cruce de cada
arista sea función local del camino-escalera) es la obligación técnica que el tier de juguete
debe verificar PRIMERO, en posets escritos a mano, antes de cualquier sprinkling.

### D.2.2 Intersecciones de consenso: forced-in / forced-out (cierre (e), algoritmo antes ausente)

Sea `λ* = A*/B*` el valor óptimo exacto. Definir el objetivo entero
`G(D) := A(D)·B* − B(D)·A*` (así `max_D G = 0`, alcanzado exactamente por 𝒜*). Entonces, sin
enumerar 𝒜* (que puede ser exponencial — matemático de 015):

```text
z ∈ T(C)  (núcleo atrapado)   ⟺  max{ G(D) : D ∈ 𝒜(C), z ∈ D } < 0     (z forced-out)
z ∈ E(C)  (núcleo de escape)  ⟺  max{ G(D) : D ∈ 𝒜(C), z ∉ D } < 0     (z forced-in)
U(C) := C ∖ (T ∪ E)
```

Cada test es UNA optimización restringida (mismo DP de D.2.1 con la celda de `z` forzada a un
lado del camino) ⟹ `n` tests ⟹ polinomial total, todo en ℤ. `ESTATUS: SPECIFICATION-CLOSED,
PROOF-OPEN`, misma obligación de verificación de juguete que D.2.1, misma restricción de
relabel (nunca `[CERRADO]` a secas hasta Gate 0).

### D.2.3 Gate 0 — falsación de la corrupción silenciosa (NUEVO, comité 017, hallazgo de mayor severidad)

**El problema que ningún tipo de la escalera de abstención puede ver:** si el lema de
localidad-de-arista de D.2.1 (paso 2) es falso en el régimen sprinkleado, la DP optimiza
silenciosamente sobre una SUBFAMILIA equivocada de `𝒜(C)` — Dinkelbach converge igual, `T/E/U`
se emiten igual, ningún tipo de abstención se dispara. Peor: el mismo código calcula tanto la
tabla `μ_n` (Parte F, paso 3) como el test de falsación mínima (paso 5), así que la corrupción
es autoconsistente — `FP_RATE ≈ α` por construcción y el test *pasa* mientras la tabla μ
congelada y todo `T/E/U` corriente pertenecen a un selector distinto, no documentado, del que
dice implementar esta spec. Verificar "en posets escritos a mano" (como decía v2) es
insuficiente: un autor eligiendo sus propios posets pequeños puede pasar por alto exactamente
la geometría de enlaces largos que rompe la localidad.

**Gate 0 (dos niveles, MANDATORIO, bloquea todo lo demás en caso de discrepancia):**

```text
Gate 0 — Tier 0 (a mano, por un miembro del comité que NO sea el autor de esta spec, ANTES de
  autorizar siquiera el tier de juguete):
  (i) construir a mano el par testigo de la Parte C (P₁ = cadena de 3, P₂ = cadena de 2) y
      verificar que d⁺(x) coincide y O(x) difiere, como se afirma arriba;
  (ii) construir a mano UN poset adicional de ~15-20 elementos y verificar que la partición
      T/E/U que produciría el DP de Dinkelbach/escalera (D.2.1-D.2.2) coincide con la
      enumeración por fuerza bruta de 𝒜(C) sobre ese mismo poset.
  Más barato que la propia tabla μ; debe ser el PRIMER entregable del tier de juguete, no un
  extra opcional.

Gate 0 — Tier 1 (automatizado, dentro del tier de juguete, ANTES de cualquier cómputo de tabla
  μ): sobre ≥100 posets sprinkleados con N suficientemente pequeño para enumeración exhaustiva
  de 𝒜(C) (N ≲ 14, sub-sembrados de EXPLORE_POOL con claves de spawn registradas, cajas MINK y
  BH ambas), comparar el output exacto (λ*, T, E, U, τ) de la DP de Dinkelbach contra la
  enumeración por fuerza bruta con aritmética racional exacta.

REGLA DE ACEPTACIÓN CONGELADA: CERO discrepancias, en cualquiera de los dos niveles. Cualquier
  discrepancia, aunque sea una sola, FALSIFICA el mecanismo D.2.1/D.2.2 y BLOQUEA
  incondicionalmente el freeze de la tabla μ (Parte F, paso 4). No se ajusta la DP ni el test;
  se reconvoca al comité con el fallo como hallazgo.
```

## D.3 Abstención tipada completa (cierre (d))

```text
R-VAR(C) := ⊥(τ) con motivo tipado τ, evaluado en este orden:
  τ = DISCONNECTED_HASSE   si el diagrama de Hasse de C no es débilmente conexo
                           (condición order-decidable; NUEVO en v2 — antes colapsaba en crash
                           o mislabel, coerción señalada por el falsificador de 015)
  τ = EMPTY_FAMILY         si 𝒜(C) = ∅ (incluye el caso "todo cut propio tiene H=∅", que en
                           v1 era el UNDEFINED_SCORE implícito; con D.1 queda subsumido aquí
                           de forma tipada, no silenciosa)
  τ = LOW_CONTRAST         si max S < μ_n (margen congelado de la Parte F)
  τ = INCOHERENT_ARGMAX    si T(C) = ∅ ∨ E(C) = ∅
En cualquier otro caso: R-VAR(C) = (T, E, U) con T, E ≠ ∅.
```

**Limitación estructural declarada (no resuelta, honestidad de 015 conservada):** con argmax
singleton `{D}`, T = C∖D ≠ ∅ y E = D ≠ ∅ siempre — `INCOHERENT_ARGMAX` no puede dispararse. La
carga de abstención recae entonces íntegramente sobre μ. v2 no lo disimula: lo compensa con la
calibración de valor extremo (μ se calcula sobre la distribución de `max S`, que ES la
distribución del ganador singleton bajo el nulo) y con el diagnóstico obligatorio D.4.

## D.4 Canal de reporte de falsos positivos y desambiguación de U=∅ (cierre (h))

Reglas de reporte vinculantes para cualquier ejecución futura (juguete o EXPLORE), congeladas
aquí ANTES de la primera ejecución:

1. **FP-channel:** toda campaña reporta, con la misma prominencia que cualquier detección, la
   fracción de parches nulos que emiten salida no-⊥ (`FP_RATE_NULL`), por nivel de intensidad.
   PASS/FAIL/INCONCLUSIVE del test de falsación se reportan por igual.
2. **U=∅:** una salida con banda de abstención vacía se etiqueta `AMBIGUOUS_CONFIDENT` y es
   inválida como claim salvo que vaya acompañada de: `|𝒜*|` (o el certificado forced-in/out de
   que |𝒜*|>1), la distribución de `|H|` de los óptimos, y el margen exacto `max S − μ_n`. Un
   U=∅ con |𝒜*|=1 y |H| pequeño es la firma del argmax de ruido (falsificador de 015) y se
   reporta como tal.
3. **Predicciones congeladas antes de correr** (falsificador de 015, remedio iii): (P-null)
   `FP_RATE_NULL ≤ α` por construcción de μ; (P-BH) en parches BH, U(C) se concentra en la
   última banda temporal y T/E recuperan interior/exterior en el pasado profundo [esta segunda
   es la predicción falsable derivada de la conjetura C-COL, Parte G — su fallo falsifica a
   R-VAR, no se reinterpreta como exploración].

---

# Parte E — Nota de computabilidad (revisada)

La vía del realizador (D.2.1) usa `dim_DM ≤ 2`, que comité 012 D2 exige **solo para 𝔄_Schw** —
coherente: el DP es una técnica de cómputo para la familia generadora (que la satisface por
conformidad plana 2D), no una condición de la definición de R-VAR, que permanece definida por
`≤` para todo poset finito (a coste exponencial general). Si un poset de entrada no admite
realizador, el cómputo cae al camino general o se abstiene por presupuesto — decisión de
implementación que el tier de juguete debe fijar y documentar; **ningún cap de presupuesto
puede introducirse en sprinkling sin reabrir la herida de censura documentada en
`dev/measure_pr003.py` (wounds #1/#2)** — si el DP exacto no escala, la respuesta es reducir N,
no truncar la búsqueda.

---

# Parte F — Cierre (g): procedimiento congelado de μ (F2)

```text
F2 (PROCEDIMIENTO CERRADO; números pendientes solo de la ejecución autorizada):

μ_n := cuantil empírico (1−α) de { max_{D∈𝒜(C_j)} S(C_j) : j = 1..M } sobre M parches NULOS
       (sprinkling Minkowski del mismo box, sin horizonte), por nivel de intensidad n.
       Niveles n a enumerar EXACTAMENTE en el addendum de freeze (mismos 4 niveles de
       intensidad que el resto del proyecto, thresholds.INTENSITIES); INTERPOLACIÓN PROHIBIDA
       entre niveles no calibrados.

α := 0.05, congelado AHORA. Base: es θ_fp, el umbral de falso positivo ya congelado por
     prereg-002 (docs/preregistration_002.md, eje (iv)) — reusar el número es defendible como
     freeze anterior a los datos, pero [FIX comité 017] esto es reutilización de convención,
     NO derivación: θ_fp gobierna una fracción de banderas LOO sobre un estadístico distinto en
     un rol distinto; no se cite después como si α=0.05 estuviera matemáticamente derivado para
     μ.

Semillas: derivadas EXCLUSIVAMENTE de EXPLORE_POOL (dev/explore_seeds.py:23 — cita corregida,
     cierre (i); la cita de v1 a thresholds.py:57-62 era errónea, literature verifier de 015).
     Sub-semillas por spawning determinista del RNG raíz de cada semilla EXPLORE
     (numpy default_rng(seed).spawn). [FIX comité 017 — falsifier: "M≥200" era un PISO, no un
     valor congelado; un piso deja abierta la posibilidad de elegir M tras mirar la estabilidad
     preliminar de la tabla, que es afinación post-hoc de la potencia estadística aunque no
     toque el embedding.] v2.1 exige: el valor EXACTO de M (no un piso) y la forma exacta de la
     llamada de spawn (`Generator.spawn(k)` vs `SeedSequence(seed).spawn(k)` — deben coincidir
     bit a bit) se fijan en el addendum de freeze ANTES de que el paso (3) (cómputo de la tabla)
     COMIENCE — no meramente antes de su commit de freeze (paso 4). PROHIBIDO: cualquier
     semilla de VALIDATION_SEEDS (banda virgen [2_000_000, 2_999_999], permanentemente quemada
     por comité 016); el guard de pre-vuelo del ingeniero de 015/017 aborta duro si se viola.

Anti-fuga (falsificador de 015/017): μ se calcula SOLO de la distribución nula — nunca eligiendo
     el valor que "separa" ensembles BH de MINK etiquetados. El embedding no toca μ.
     La corrección de valor extremo es estructural: el cuantil es de max S (el máximo sobre
     TODA la familia 𝒜), no de S por cut — el efecto max-of-many queda dentro del nulo.
     [FIX comité 017 — falsifier: higiene de freeze, no fuga de ground-truth] la tabla μ (paso
     4, congelada) y el test de falsación mínima (paso 5) NO pueden extraerse del mismo sub-pool
     de nulos EXPLORE sin más, o el test de falsación quedaría parcialmente verificado contra
     los datos que definieron su propio umbral. v2.1 exige que el paso 3 (cómputo de tabla) y el
     paso 5 (test) usen sub-pools de semilla-spawn DISJUNTOS dentro de EXPLORE_POOL, registrados
     como tales en el addendum.

Congelación: la tabla μ_n resultante se congela en un addendum commiteado ANTES de puntuar
     ningún parche BH (patrón del sello de prereg-002: el commit de freeze precede al uso). El
     commit de freeze (paso 4) es su propio punto de control — el addendum (M exacto, esquema
     de spawn, niveles enumerados) debe estar YA commiteado antes de este paso, no integrado en
     él después del hecho [fix comité 017, falsifier: evita colapsar "correr" y "congelar un
     umbral" en un solo evento autorizante].
     El orden vinculante, con Gate 0 insertado: (1) autorización scoped de comité → (2) tier de
     juguete determinista, INCLUYENDO Gate 0 (D.2.3) — bloquea todo lo siguiente ante cualquier
     discrepancia → (3) tabla μ sobre nulos EXPLORE (sub-pool de calibración) → (4) commit de
     freeze de la tabla + predicciones D.4.3 → (5) test de falsación mínima de 015 (solo nulos,
     sub-pool DISJUNTO del de calibración) → (6) solo entonces, y solo con reporte de vuelta
     separado al comité, parches BH EXPLORE.
```

---

# Parte G — Cierre (f): colimación degradada a conjetura

La Parte IV de v1 ("las fronteras de TODOS los cuts admisibles coinciden con el horizonte salvo
O(e^{-κΔt})") pasa de registro fáctico a:

```text
CONJETURA C-COL (sin cambio de contenido, cambio de estatus):
  ESTATUS = CONJETURA FÍSICA, [no anclada a cita primaria en biblioteca/]
  OBLIGACIÓN DE CITA: antes de cualquier freeze que dependa de C-COL, anclar el peeling
    near-horizon (κ como exponente de Lyapunov del horizonte) a una fuente primaria, o
    degradar los usos dependientes. EGS ancla SOLO el cambio de signo de Θ_out en r=2M
    (derived-md:288), no la tasa de colimación hacia atrás (matemático de 015).
  CONTESTACIÓN ABIERTA REGISTRADA: dev/measure_kbeam_peeloff.py trata el peel-off como
    falsación abierta ("PHYSICAL o greedy myopia") — C-COL no está establecida ni siquiera
    en dev/.
  USO PERMITIDO EN V2.1: únicamente como generadora de la predicción falsable (P-BH) de D.4.3.
    Ningún objeto de la definición del selector (𝒜, S, μ, T/E/U) depende de C-COL.
  PROHIBIDO (elevado por comité 017 a REGLA VINCULANTE ENTRE DOCUMENTOS, no solo local a este
    archivo — cualquier revisión futura de R-VAR o documento sucesor hereda esta prohibición
    por nombre, no debe re-derivarla): usar κ, 1/κ o cualquier cantidad de la geometría oculta
    para fijar F1-F3, μ, o ventanas de reporte (inyección de geometría en umbrales —
    falsificador de 015/017). Esta prohibición debe aplicarse como GUARDIA DURA por el
    pre-flight guard del ingeniero de reproducibilidad, no quedar como texto advisorio.
```

Las identificaciones T1/T2 de v1 conservan su estatus de 015: motivación correcta,
[UNVERIFIED] como teoremas, condicionales al generador sellado.

---

# Parte H — Bloque normativo

```text
DOCUMENT_ID = PR003_R_VAR_SELECTOR_SPEC_V2_1
SUPERSEDES = PR003_R_VAR_SELECTOR_SPEC (v1) y PR003_R_VAR_SELECTOR_SPEC_V2 (v2); ambos
  conservados como registro histórico
CANDIDATE_PATH = C1 vía R directa (Q_DISPOSITION sin cambio)
REVISION_MANDATE = docs/comite/comite_decision_017_r-var-v2-reconvene.md §9 paso reversible 1

CLOSURES_DELIVERED (re-verificadas por comité 017, corregidas donde el falsifier encontró que
  el cierre v2 era de letra, no de sustancia):
  (a) 𝒦_comb/𝒦_adm/𝒦_Schw definidas por herencia de comité 012 D1/D2 — GENUINO, confirmado
      independientemente (comité 017: mathematician, logician, literature verifier). V.1a
      REVISADA en v2.1 (Parte A.2): cuantificador `escape(Cᵢ)` ligado a `E(Cᵢ)` (núcleo de
      escape del propio selector), cerrando el testigo de trivialidad del falsifier de 017;
      V.1b sigue abierta, NEEDS_PRECISE_WITNESS, prohibido citarla como establecida; el
      selector sigue sin depender de V.1                                        [CERRADO,
      v1a re-cerrada en v2.1]
  (b) fork colapsado: SIG_LK_ONLY_SIG_SP_REJECTED, razón principiada pre-datos   [CERRADO]
  (c) REVISADO en v2.1 (Parte C): objeto del chequeo composicional fijado por escrito =
      outputs expuestos (S,T,E,U,τ), NUNCA primitivas crudas; testigo de separación
      reconstruido con par Hasse-CONEXO (cadenas de 3/2 elementos, ya no un poset
      desconectado); verificación completa (que el output expuesto completo, no solo d⁺,
      coincide) queda como obligación de Gate 0 Tier 0                          [ESPECIFICACIÓN
      CERRADA; verificación es obligación de Gate 0, no reclamada como ya exhibida]
  (d) abstenciones DISCONNECTED_HASSE añadida, UNDEFINED_SCORE subsumida tipadamente en
      EMPTY_FAMILY vía H≠∅ en 𝒜 — GENUINO. F3 := 1 RELABELED en v2.1: redundante con H≠∅, no
      un cierre sustantivo independiente; declarada explícitamente la consecuencia compuesta
      (la escalera de 4 tipos colapsa a 1 gate operativo bajo argmax singleton) [CERRADO el
      hazard; F3 relabeled honesto; consecuencia compuesta declarada]
  (e) aritmética racional exacta obligatoria; Dinkelbach entero sobre escaleras (D.2.1);
      forced-in/forced-out para T/E sin enumerar 𝒜* (D.2.2) — ambos con Gate 0 (D.2.3, NUEVO
      en v2.1) como obligación de verificación mandatoria, DOS niveles (hand-check + brute
      force automatizado), regla de aceptación cero-discrepancias            [SPECIFICATION-
      CLOSED, PROOF-OPEN — nunca "[CERRADO]" a secas hasta que Gate 0 pase]
  (f) Parte IV → CONJETURA C-COL con obligación de cita y prohibición de uso en umbrales,
      ELEVADA en v2.1 a regla vinculante entre documentos, guardia dura no advisoria [CERRADO]
  (g) F2: procedimiento μ completo — α=0.05 ≡ θ_fp (reutilización de convención, no derivación,
      aclarado en v2.1); nulos-solo; valor extremo sobre max S; sub-semillas EXPLORE
      deterministas; M EXACTO (no piso) y esquema de spawn fijados antes del paso 3 (v2.1,
      no antes del paso 4 como en v2); sub-pools DISJUNTOS para calibración (paso 3) y test
      (paso 5) (v2.1, cierra higiene de freeze); orden de freeze vinculante con Gate 0
      insertado                                     [CERRADO como algoritmo; tabla numérica
      pendiente de ejecución autorizada]
  (h) FP-channel con reporte simétrico; AMBIGUOUS_CONFIDENT para U=∅; predicciones
      congeladas antes de correr                                                [CERRADO]
  (i) EXPLORE_POOL citado en dev/explore_seeds.py:23                             [CERRADO]

FREEZE_STATE:
  F1 = CERRADO (media como racional exacto, comparación entera)
  F2 = PROCEDIMIENTO CERRADO / TABLA PENDIENTE DE EJECUCIÓN AUTORIZADA / sub-pools disjuntos
       calibración-vs-test fijados en v2.1
  F3 = CERRADO pero REDUNDANTE (relabel v2.1: H_MIN = 1 no excluye nada más allá de H≠∅)
  fork sig = CERRADO (Parte B)
  CIRCULARITY_STANDARD = FUNCTIONAL_ONLY [ADJUDICADO por comité 017, con 3 condiciones
       vinculantes: test-object=outputs expuestos, cláusula NON_CORROBORATION permanente,
       etiqueta de limitación permanente — Parte C.2]

PASS_DEPENDENCY_LABEL = PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED;
  BLINDNESS_DOCUMENTARY_ONLY] (docs/prereg002_reverification_result.md, commit 82b4ede) —
  toda mención del PASS de prereg-002 en este documento porta la etiqueta completa entre
  corchetes; NUNCA "PASS" desnudo. [FIX comité 017: la etiqueta v2
  ([UNVERIFIED-raw-artifact]/auditor 005) estaba stale — corregida aquí.]

GATE_0_STATUS = NOT_YET_EXECUTED — mandatorio, primer entregable del tier de juguete, bloquea
  todo lo posterior (incluida la tabla μ) ante cualquier discrepancia (D.2.3)

BLOCKING_ADJUDICATIONS_RESOLVED_BY_COMITE_017:
  (1) CIRCULARITY_STANDARD = FUNCTIONAL_ONLY, con las 3 condiciones vinculantes (Parte C.2) —
      RESUELTO, no por el argumento "protegería a O_min" (circular, falsifier 017) sino sobre
      bases independientes
  (2) autorización scoped S1-S5 (falsifier/warden de 017) — RESUELTA EN ALCANCE, pendiente de
      autorización EXPLÍCITA del PI como paso comprometido separado de esta revisión escrita
      (comité 017 §9 paso 3; ver ese documento para S1-S5 verbatim)
  (3) aceptación de V.1a (forma v2.1, cuantificador cerrado) como escenario candidato de un
      futuro Alloy 003 — ACEPTADA, NO autoriza Alloy 003 en sí (ALLOY_003_AUTHORIZATION_STATUS
      = NOT_AUTHORIZED sigue vigente)
NEXT_RECOMMENDED_ACTION = commit de esta revisión v2.1 (con v1 y v2 marcados superseded en el
  mismo commit); después, autorización explícita del PI para el paso comprometido S1-S5 de
  comité 017 §9 (implementación dev-only + tier de juguete con Gate 0 + calibración μ sobre
  nulos EXPLORE + test de falsación) — nada de esto se auto-otorga por escribir esta revisión
NEXT_FORBIDDEN_WITHOUT_AUTORIZACION_S1_S5 = implementación | simulación | enumeración | Alloy |
  Lean | scoring de parches BH | citar output de R-VAR como evidencia sobre Q o como
  corroboración del PASS de prereg-002 | cualquier semilla fuera de EXPLORE_POOL con
  proveniencia de spawn registrada | commit o push de código de ejecución sin autorización
  explícita del PI
```
