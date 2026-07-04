# PR-003 — R-VAR spec v2: selector variacional de consenso con abstención tipada (revisión post-comité 015)

> **SUPERSEDED (2026-07-04) por `dev/PR003_R_VAR_SELECTOR_SPEC_V2_1.md`.** Comité 017
> (`docs/comite/comite_decision_017_r-var-v2-reconvene.md`) encontró que tres de los nueve
> cierres autoreportados abajo — (a) el cuantificador de V.1a, (c) el testigo de separación
> C.1, (d) el rol real de F3 — estaban cerrados en la letra pero no en la sustancia. Conservado
> aquí solo como registro histórico; donde v2 y v2.1 difieran, **v2.1 gobierna**.

Status: **dev nota de especificación, solo escritura. Sin código, sin simulación, sin
enumeración, sin Alloy, sin Lean, sin datos, sin freeze, sin commit.** Autorizada por el PI
tras el veredicto de comité 015 (`docs/comite/comite_decision_015_r-var-selector-adjudication.md`,
`COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE`, §9 paso reversible 3). Cierra por
escrito los nueve puntos (a)–(i) exigidos por ese brief. Sustituye a
`dev/PR003_R_VAR_SELECTOR_SPEC.md` (v1), que queda como registro histórico; donde v1 y v2
difieren, **v2 gobierna**.

Preservado sin reapertura (tokens vinculantes, verificados por el comité 015 §2):
`Q_DISPOSITION = Q_DIAGNOSTIC_CANDIDATE_ONLY` | `OVERALL_VERDICT (014) =
Q_REFERENCE_PATH_REMAINS_BLOCKED` | `R=Max(C) = REJECTED_TRIVIAL` | `GROUNDEDNESS_DECISION = G1`
| `CONVEXITY_REQUIREMENT = MANDATORY_FOR_C1` (comité 012 D2) | `PHYSICAL_IDENTIFIABILITY_STATUS
= NOT_ESTABLISHED` | prohibiciones de ejecución de comité 014 vigentes hasta autorización nueva.

**Etiqueta obligatoria heredada de auditor 005** (`docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md`,
`AUDIT_VERDICT=AUDIT_FAIL`): el respaldo crudo del PASS de prereg-002 es hoy
`[UNVERIFIED-raw-artifact]` (transcripción commiteada `fee12d5` sin artefacto vivo en esta
máquina; recuperación desde la segunda máquina pendiente, `results/README.md`). Toda invocación
del PASS en este documento porta esa etiqueta. La transcripción sigue siendo el registro oficial;
la etiqueta se levanta al poblar `results/prereg002/`.

## 0. Fuentes leídas esta sesión (además de las de v1)

| Archivo | Uso |
|:---|:---|
| `docs/comite/comite_decision_015_r-var-selector-adjudication.md` | Los 7 briefs y el mandato §8-§9; cada cierre de abajo cita el hallazgo que lo motiva |
| `docs/comite/comite_decision_012_c1-admissible-completion-class.md` (bloque normativo :330-360) | D1 (cláusulas MANDATORY/DEFERRED de la clase admisible), D2 (convexidad MANDATORY; dim≤2 solo para 𝔄_Schw) |
| `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` (§3-§4, §7) | Vocabulario de cláusulas (a)-(e); requisitos de testigo C1 |
| `docs/auditor/auditor_report_005_...md` | Etiqueta [UNVERIFIED-raw-artifact] del PASS |
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
v2 separa:

```text
V.1a (banda de pared; conjetura formalizable, escenario Alloy candidato):
  ∀ O finito con Max(O) ≠ ∅, ∀ m ∈ Max(O): ∃ C₁, C₂ ∈ 𝒦_adm(O) tales que m ∈ down(escape(C₁))
  y m ∉ down(escape(C₂)) — donde escape(Cᵢ) es cualquier referencia anclada propia de Cᵢ.
  ALCANCE: solo elementos cuyo estatus depende de la última banda (la banda Le Cam ya
  concedida). NO implica nada sobre el pasado profundo.

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

**Afirmación C.1 (no determinación funcional, clase por clase).** Ninguna composición de
P1-P6 determina funcionalmente `O(x) = |↑x|` sobre ninguna clase de elementos relevante para el
PASS (que evalúa `O(i)` sobre **minimales**, `dev/PR003_C1_BCE_CLOSED_CANDIDATE.md` Parte V):

- Sobre `x ∈ Min(C)`: las primitivas ven de `x` su indicador P1, su `d⁺` (radio 1) y su
  pertenencia a interfaces/anclajes. `O(x)` es una cantidad de clausura transitiva global.
  **Testigo de separación (obligación de verificación en el tier de juguete, cuando se
  autorice):** sean `P₁ := ⟨x ⋖ a, a ⋖ b⟩` (cadena de 3) y `P₂ := ⟨x ⋖ a⟩ ⊕ {b}` con `b`
  incomparable a `x` y a `a` salvo `a ⋖ b` removido — construcción estándar "cadena larga
  colgada lejos": dos posets con vecindades de Hasse de radio 1 de `x` isomorfas
  (`d⁺(x)=1`, mismos indicadores) y `O(x)` distinto (2 vs 1). P3/P4 no restauran la
  determinación: son funciones de la estructura global del cut, no de `|↑x|`. [derivación de
  esta sesión, verificable a mano en 5 elementos; se registra como obligación de test]
- Sobre `x ∈ Max(C)`: `O(x)=0` es determinado trivialmente por P1 — pero también lo determina
  la propia definición de maximal, conocida por cualquier observador del orden; no es el
  estadístico del PASS (que corre sobre minimales) ni información nueva.
- La única cantidad agregada que el selector expone es `S` (contrastes de `d⁺` promediados
  sobre H): una función de a lo sumo `2|H|` grados de cobertura, no de ningún `|↑x|`.

**Declaración honesta C.2 (el solapamiento estadístico persiste y se somete a adjudicación).**
La corrección del matemático de 015 se incorpora: la derivación de v1 `E[d⁺] ≈ ln(ρV)+γ` omitía
el jacobiano nulo ½ y los límites finitos; la forma corregida es
`E[d⁺] ∼ ln(ρ·Área futura) + const`, coeficiente dependiente del esquema — la relación
**monótona en media** con el volumen futuro se mantiene. Por tanto: R-VAR es no circular en el
estándar **funcional** (C.1) y correlacionado en el estándar **estadístico-medio**. v2 no
resuelve cuál estándar gobierna; lo formula como el fork que el comité reconvocado debe adjudicar:

```text
CIRCULARITY_STANDARD ∈ { FUNCTIONAL_ONLY , FUNCTIONAL_PLUS_MEAN_MONOTONE_BAN }
```

con esta consecuencia sobre la mesa, en registro llano: bajo
`FUNCTIONAL_PLUS_MEAN_MONOTONE_BAN` muere el eje `d⁺` — y, dado que **cualquier** estadístico
sensible al horizonte en este parche debe correlacionar con la truncación de futuros (es el
único imprint order-visible; físico de 015: "the same future-truncation imprint... read
locally"), ese estándar plausiblemente prohíbe *todo* selector funcional. El comité que lo
adopte debe poseer esa consecuencia explícitamente. El firewall que v2 ofrece bajo
`FUNCTIONAL_ONLY`: separación de roles (selector define / estimador sellado valida / embedding
solo puntúa), calibración **solo sobre nulos** (Parte F), y el test de falsación mínima del
falsificador de 015 ejecutado ANTES de cualquier claim sobre parches BH.

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
F3 (CERRADO): H_MIN := 1, congelado.
```

Base principiada: cualquier entero mayor carecería hoy de base documental y sería numerología
(exclusión II.1); la carga estadística contra interfaces pequeños no se lleva con un umbral
duro sino con la calibración de valor extremo de μ (Parte F), que incluye por construcción el
ruido de los cuts de |H| pequeño en la distribución nula de `max S`. Obligación de reporte
(D.4) acompaña.

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

`ESTATUS: PLAUSIBLE, no implementado, no probado` — el paso 2 (que el cruce de cada arista sea
función local del camino-escalera) es la obligación técnica que el tier de juguete debe
verificar PRIMERO, en posets escritos a mano, antes de cualquier sprinkling.

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
lado del camino) ⟹ `n` tests ⟹ polinomial total, todo en ℤ. `ESTATUS: PLAUSIBLE, misma
obligación de verificación de juguete que D.2.1.`

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

α := 0.05, congelado AHORA. Base principiada: es θ_fp, el umbral de falso positivo ya
     congelado por prereg-002 (docs/preregistration_002.md, eje (iv)) — un solo estándar de FP
     en todo el proyecto, no un número nuevo.

Semillas: derivadas EXCLUSIVAMENTE de EXPLORE_POOL (dev/explore_seeds.py:23 — cita corregida,
     cierre (i); la cita de v1 a thresholds.py:57-62 era errónea, literature verifier de 015).
     Sub-semillas por spawning determinista del RNG raíz de cada semilla EXPLORE
     (numpy default_rng(seed).spawn), M ≥ 200, M exacto fijado en el addendum de freeze.
     PROHIBIDO: cualquier semilla de VALIDATION_SEEDS (banda virgen [2_000_000, 2_999_999]);
     el guard de pre-vuelo del ingeniero de 015 aborta si se viola.

Anti-fuga (falsificador de 015): μ se calcula SOLO de la distribución nula — nunca eligiendo
     el valor que "separa" ensembles BH de MINK etiquetados. El embedding no toca μ.
     La corrección de valor extremo es estructural: el cuantil es de max S (el máximo sobre
     TODA la familia 𝒜), no de S por cut — el efecto max-of-many queda dentro del nulo.

Congelación: la tabla μ_n resultante se congela en un addendum commiteado ANTES de puntuar
     ningún parche BH (patrón del sello de prereg-002: el commit de freeze precede al uso).
     El orden vinculante es: (1) autorización scoped de comité → (2) tier de juguete
     determinista (verifica D.2.1/D.2.2 y el testigo C.1) → (3) tabla μ sobre nulos EXPLORE →
     (4) commit de freeze de la tabla + predicciones D.4.3 → (5) test de falsación mínima de
     015 (solo nulos) → (6) solo entonces, parches BH EXPLORE.
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
  USO PERMITIDO EN V2: únicamente como generadora de la predicción falsable (P-BH) de D.4.3.
    Ningún objeto de la definición del selector (𝒜, S, μ, T/E/U) depende de C-COL.
  PROHIBIDO: usar κ, 1/κ o cualquier cantidad de la geometría oculta para fijar F1-F3, μ,
    o ventanas de reporte (inyección de geometría en umbrales — falsificador de 015).
```

Las identificaciones T1/T2 de v1 conservan su estatus de 015: motivación correcta,
[UNVERIFIED] como teoremas, condicionales al generador sellado.

---

# Parte H — Bloque normativo

```text
DOCUMENT_ID = PR003_R_VAR_SELECTOR_SPEC_V2
SUPERSEDES = PR003_R_VAR_SELECTOR_SPEC (v1; conservada como registro)
CANDIDATE_PATH = C1 vía R directa (Q_DISPOSITION sin cambio)

CLOSURES_DELIVERED (mandato comité 015 §9.3):
  (a) 𝒦_comb/𝒦_adm/𝒦_Schw definidas por herencia de comité 012 D1/D2; V.1 dividida en
      V.1a (conjetura formalizable, alcance banda de pared) y V.1b (abierta,
      NEEDS_PRECISE_WITNESS, prohibido citarla como establecida); el selector ya NO depende
      de V.1                                                                    [CERRADO]
  (b) fork colapsado: SIG_LK_ONLY_SIG_SP_REJECTED, razón principiada pre-datos   [CERRADO]
  (c) chequeo composicional C.1 exhibido con testigo de separación verificable;
      solapamiento estadístico declarado; fork CIRCULARITY_STANDARD formulado
      para adjudicación con su consecuencia explícita                    [ENTREGADO — la
      adjudicación del estándar es del comité, no de este documento]
  (d) abstenciones DISCONNECTED_HASSE añadida, UNDEFINED_SCORE subsumida tipadamente en
      EMPTY_FAMILY vía H≠∅ en 𝒜; F3 := 1 congelado con base principiada          [CERRADO]
  (e) aritmética racional exacta obligatoria; Dinkelbach entero sobre escaleras (D.2.1);
      forced-in/forced-out para T/E sin enumerar 𝒜* (D.2.2) — ambos PLAUSIBLE con
      obligación de verificación de juguete                                     [CERRADO como
      especificación; verificación pendiente de autorización]
  (f) Parte IV → CONJETURA C-COL con obligación de cita y prohibición de uso en umbrales
                                                                                 [CERRADO]
  (g) F2: procedimiento μ completo — α=0.05 ≡ θ_fp congelado ya; nulos-solo; valor extremo
      sobre max S; sub-semillas EXPLORE deterministas; orden de freeze vinculante [CERRADO
      como algoritmo; tabla numérica pendiente de ejecución autorizada]
  (h) FP-channel con reporte simétrico; AMBIGUOUS_CONFIDENT para U=∅; predicciones
      congeladas antes de correr                                                [CERRADO]
  (i) EXPLORE_POOL citado en dev/explore_seeds.py:23                             [CERRADO]

FREEZE_STATE:
  F1 = CERRADO (media como racional exacto, comparación entera)
  F2 = PROCEDIMIENTO CERRADO / TABLA PENDIENTE DE EJECUCIÓN AUTORIZADA
  F3 = CERRADO (H_MIN = 1)
  fork sig = CERRADO (Parte B)

PASS_DEPENDENCY_LABEL = [UNVERIFIED-raw-artifact] (auditor 005) — toda mención del PASS de
  prereg-002 en este documento la porta; se levanta al poblar results/prereg002/

BLOCKING_ADJUDICATIONS_FOR_RECONVENED_COMITE:
  (1) CIRCULARITY_STANDARD (Parte C.2) — con su consecuencia explícita si se adopta el
      estándar fuerte
  (2) autorización scoped: implementación dev + tier de juguete determinista + nulos EXPLORE
      + tabla μ + test de falsación mínima de 015, en el ORDEN vinculante de la Parte F
      (supersede parcial y explícitamente los NEXT_FORBIDDEN_ACTIONS de comité 014)
  (3) aceptación de V.1a como escenario candidato de un futuro Alloy 003 (no autorizado aquí)
NEXT_RECOMMENDED_ACTION = /comite sobre (1)-(3) con este documento como brief; idealmente tras
  resolver la recuperación del artefacto del PASS (auditor 005) para que la reconvocatoria no
  se apoye en un AUDIT_FAIL abierto
NEXT_FORBIDDEN_WITHOUT_COMITE = implementación | simulación | enumeración | Alloy | Lean |
  freeze de la tabla μ | commit o push de este documento sin autorización del PI
```
