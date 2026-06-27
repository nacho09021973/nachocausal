# PR-003 — Inaccesibilidad futura quasi-local: hacia una definición relacional de horizonte (dev conceptual, sin código)

Nota de sandbox, **conceptual, sin código, ningún claim, nada congelado.** Paso autorizado (usuario,
esta sesión, AskUserQuestion): formular la condición relacional de *atrapamiento / inaccesibilidad
futura* que (i) tenga sentido en un poset causal finito o localmente finito, (ii) sea
relabel-invariante, sin métrica ni embedding, sin saber dónde está `r=2M`, sin construirse por
comparación con Schwarzschild, y (iii) **separe la pérdida de acceso a un futuro INTERNO del simple
contacto con el borde de muestreo.** Decide si C2 (futuro común) es el objeto o debe reformularse.

Contexto: reanuda la pista comité-006 (C1/C2 → `REFINE_CANDIDATES_BEFORE_PROMOTION`); ver
[[strategic-refocus-relational-definition]] y `docs/comite/comite_decision_006_*`. L₁/LPP/Berry–Esseen
CONGELADOS. El PASS sellado = recuperabilidad (el orden RECUERDA el horizonte), NO definición (que el
orden lo DEFINA). Esta nota ataca la definición.

---

## 1. El contenido clásico que hay que capturar (y cuál NO)

- **Horizonte de sucesos** = `∂J⁻(𝒥⁺)`: frontera del pasado del infinito nulo futuro. **Global,
  teleológico** — requiere `𝒥⁺`. **NO capturable en un poset finito** (no hay `𝒥⁺`). Teorema
  teleológico del informe `biblioteca/Horizontes…md` §6 [THEOREM-CONFIRMED]: un poset finito sólo
  puede portar un precursor **aparente / de atrapamiento**, jamás el horizonte de sucesos.
- **Horizonte aparente / superficie atrapada** = quasi-local: la expansión nula saliente se anula
  (`Θ_out=0`); incluso los rayos causales "hacia afuera" dejan de aumentar la sección. Contenido
  esencial (pregunta Q-a del usuario): **pérdida ESTRUCTURAL de acceso causal a un futuro genérico**
  — el futuro de la región "se captura" / se estrecha en un canal.
- **Lo que NO debe capturar:** ni una singularidad pura (futuro que TERMINA; C3 ya RECHAZADO, falla
  Hayward), ni un mero focusing (convergencia geodésica sin atrapamiento), ni el borde de muestreo.

**Objetivo operativo (alcanzable):** una propiedad relabel-invariante del orden, sin métrica, que en
causal sets manifoldlike distinga una **frontera de inaccesibilidad futura quasi-local** y converja al
horizonte clásico.

## 2. El obstáculo de la finitud, con precisión (por qué Q-b es difícil)

"Inaccesibilidad al futuro exterior" presupone un *infinito* inalcanzable. En un parche finito **el
único 'futuro inalcanzable' disponible es el borde superior de la caja** (la pared de muestreo: no
hay puntos sprinkled más allá). Por tanto cualquier definición que mida "futuro pequeño / truncado"
en términos ABSOLUTOS confunde horizonte con pared:

| | Pared de muestreo (borde top) | Horizonte de atrapamiento |
|---|---|---|
| Localización | en ALTURA (todo lo cercano al tope) | en un SUB-LUGAR, a TODA altura |
| Simetría | isótropa: todo punto del tope pierde futuro igual | ASIMÉTRICA: interior pierde acceso al exterior; exterior intacto |
| Persistencia | sólo en los niveles superiores | banda persistente a través de muchos niveles (tubo quasi-timelike) |
| Dirección de enlaces | ausencia simétrica (no hay otro lado) | válvula de una vía (one-way membrane) |

**Esta tabla ES la respuesta a Q-b.** Los discriminadores son **persistencia** y **asimetría**, no la
magnitud del déficit de futuro.

**Cautela [usuario]:** la fila "isótropa" para la pared NO es universal — depende de la FORMA del
parche. Una caja `(t,r)` da un borde top aproximadamente isótropo en `r`, pero un parche de forma
arbitraria (p.ej. el diamante inclinado en `(u,v)`, o cortes oblicuos) puede dar una pared
anisótropa que imite parcialmente la asimetría de un horizonte. Por tanto **"la pared es isótropa"
debe tratarse como HIPÓTESIS A FALSAR en cada geometría de control, no como propiedad garantizada** —
de ahí los controles adversariales (§5) con formas de parche variadas.

## 3. Definir "alcance futuro" de forma intrínseca — y la contaminación de cada opción

Candidatos orden-only para "cuánto futuro alcanza `x` (o un antichain `A`)":
1. **Volumen futuro** `|J⁺(x)|` (observable estimator-v2). Contaminado por el tope: puntos altos
   tienen `|J⁺|` chico sólo por la pared. → no separa horizonte de pared por sí solo.
2. **Anchura futura** = antichain máximo en `J⁺(x)`. Colapsa para atrapamiento Y para singularidad
   (= embudo) → falla Hayward (C3). → insuficiente solo.
3. **Futuro común de un wavefront** `κ(A)=|⋂_i J⁺(a_i)|/E_indep` (C2). Mide captura del frente en un
   canal estrecho. Problema comité-006: `E_indep` no intrínseco; confound de truncación.
4. **Asimetría de enlaces de cobertura a través de un antichain** (nuevo eje): `#{links A→exterior}`
   vs `#{links exterior→A}` y, sobre todo, `J⁺(interior) ∩ bulk-exterior` ≈ ∅ mientras
   `J⁺(exterior)` lleno. Es la **válvula de una vía** — el contenido de "one-way membrane".

Ninguno SOLO sirve. La tesis de esta nota: **la inaccesibilidad futura relacional NO es un escalar
local sino la conjunción persistencia + asimetría de (3)/(4).**

## 4. Propuesta: "membrana de atrapamiento persistente y de una vía" (C2′ — conceptual, NO cerrada)

Un **precursor relacional de horizonte** = una banda `B` (una **cadena de antichains** `{A_ℓ}` a
través de niveles de altura consecutivos) tal que, todo medido por invariantes de orden:

- **(I) Atrapamiento = SOBRE-SOLAPAMIENTO (convergencia) del futuro común, RELATIVO al bulk al MISMO
  nivel ℓ** — con `κ(A)=|⋂_i J⁺(a_i)|/E_indep`, el atrapamiento fuerza a los futuros del wavefront a
  **converger** en un canal compartido ⇒ la intersección es anómalamente **GRANDE** ⇒
  **`κ(A_ℓ) ≫ κ_bulk(ℓ)`** (sobre-solapamiento).
  - *Corrección de signo [usuario, esta sesión]:* el nombre comité-006 "future-overlap **collapse**"
    es un **MISNOMER**. Con esta `κ`, el atrapamiento da `κ≫`, NO `κ≪`; la lectura "colapso/déficit"
    sólo sería correcta con la inversa `κ⁻¹` o una puntuación de anomalía. Se adopta `κ≫` y el nombre
    correcto **convergencia / captura del futuro común**.
  - **NO usar la anchura futura ≪** como diagnóstico: eso es C3 (anchura→0 = embudo = singularidad),
    RECHAZADO por fallar Hayward. (κ≫ y anchura≪ tienen signos opuestos; eran una conflación.)
  - *Relativo al bulk* intrínseca `E_indep` (= el propio causet al mismo `ℓ`), evita el confound del
    tope, y es Hayward-safe (captura en un canal regular, sin terminación). [responde Q-a]
- **(II) Persistencia (tubo quasi-timelike)** — el lugar de `κ≫` forma una **secuencia conexa a
  través de muchos niveles** `ℓ` consecutivos (una cadena de antichains enlazada por orden), NO un
  evento de un solo nivel ni confinado a los niveles superiores. Separa horizonte (tubo a toda
  altura) de pared (sólo top) y de inhomogeneidad TRANSITORIA (un nivel). [responde Q-b, 1]
  - **Cautela [usuario]:** la persistencia **NO excluye por sí sola** una inhomogeneidad — puede
    existir una **inhomogeneidad persistente y tubular** (p.ej. una banda de densidad estable). La
    separación real NO descansa en (II) sola, sino en la **combinación (II)+(III)+controles
    adversariales** (§5). (II) es necesaria, no suficiente.
- **(III) Asimetría / una vía** — el flujo de enlaces a través de `B` está direccionalmente
  desbalanceado: la cara "capturada" no alcanza el bulk futuro de la otra cara
  (`J⁺(captured) ∩ bulk_other ≈ ∅`), mientras la cara exterior conserva su futuro. Separa horizonte
  (válvula) de pared (ausencia simétrica) y de singularidad (terminación de dos caras). [responde
  Q-b, 2; y separa atrapamiento de focusing — el talón de C1 solo]

**Relación con los candidatos previos:**
- **C1** (β = flujo de enlaces mínimo) es el **localizador** del lugar candidato a `A_ℓ` (la
  membrana de cuello), pero es un escalar SIMÉTRICO → no distingue atrapamiento de focusing. Aporta
  (II) parcialmente (si se escanea por nivel) pero NO (III).
- **C2** (κ) es exactamente la condición (I), pero necesita `E_indep` intrínseco y la versión
  *relativa al bulk al mismo ℓ* (la nota la precisa: comparar contra el propio bulk, no contra un
  modelo externo — eso intrínseca el `E_indep`).
- **C3** (anchura→0) RECHAZADO = singularidad; (III) es justo lo que lo habría salvado/distinguido.
- **TIPs** (pasados indescomponibles terminales; frontera causal GKP) son el objeto correcto
  *asintótico* para "inaccesibilidad", pero requieren cadenas futuro-inextensibles → **no disponibles
  en un parche finito** (informe §F, L₆ Dowker–Zalel). La banda persistente (II) es el **sucedáneo
  quasi-local finito** de la separación de TIPs.

**Síntesis conceptual:** el objeto no es C1 *ni* C2 por separado, sino **C1 como localizador +
(I)+(II)+(III) como la condición de horizonte**. La novedad respecto a comité-006 son (II)
persistencia y (III) asimetría como los discriminadores que faltaban; (I) es C2 re-planteada en forma
relativa-al-bulk (lo que la intrínseca).

## 5. Los controles conceptuales que debe pasar (paso 3 del programa del usuario)

| Control | (I) κ≫ rel. al bulk | (II) persistencia | (III) una vía | Veredicto deseado |
|---|---|---|---|---|
| Minkowski (sin horizonte) | no | no | no | NO dispara ✓ |
| Schwarzschild 1+1D (singular) | sí | sí (tubo `r=2M`) | sí | DISPARA ✓ |
| Parche truncado (borde, sin horizonte) | aparente sólo cerca top | **no (sólo top)** | **no (simétrico)** | NO dispara — (II)+(III) lo matan ✓ |
| Inhomogeneidad TRANSITORIA (bump de densidad) | quizá un nivel | **no (transitoria)** | no | NO dispara — (II) lo mata ✓ |
| **Inhomogeneidad PERSISTENTE tubular** (banda de densidad estable) | quizá | **sí (¡pasa II!)** | **no (simétrica)** | NO dispara — **SÓLO (III) + controles adversariales lo matan, NO (II)** ⚠ |
| Hayward (regular, sin singularidad) | sí (canal, no cero) | sí | sí | DEBE disparar (horizonte sin singularidad) — (I)-relativo + (III) lo permiten ✓ |

Esta tabla es el **diseño de falsación conceptual**. **La fila ⚠ es la lección de la cautela del
usuario:** una inhomogeneidad persistente y tubular **pasa (II)** — luego (II) NO es un discriminador
suficiente; la carga discriminante recae en **(III) asimetría** + **controles adversariales** (variar
forma de parche, densidad, perfil de inhomogeneidad). Si (III) no separa la banda de densidad
persistente de Schwarzschild, la propuesta cae. Versión cualitativa de los controles negativos del
informe (§Controles Negativos Mínimos) y de comité-006.

## 6. Honestidad: qué falta para que esto sea una definición CERRADA

Esto es una **formulación conceptual, no una definición cerrada ni un teorema.** Para cerrarla (per el
spec de comité-006 §9, ahora con (II)+(III)):
- **(I)** `E_indep` intrínseco = el bulk al mismo nivel `ℓ` del MISMO causet (auto-calibrado), con
  regla explícita de qué es "bulk" sin coordenadas (p.ej. mediana de κ sobre antichains de igual
  `|A|` y nivel). [abierto]
- **(II)** métrica de persistencia: cuántos niveles consecutivos, qué significa "lugar conexo" en
  orden puro (cadena de antichains enlazada), umbral congelado. [abierto]
- **(III)** estimador de asimetría order-only que NO reintroduzca una dirección espacial prohibida
  (el riesgo `relphi`/"outward" del comité-006): la asimetría debe leerse de la *estructura de
  enlaces* (`J⁺(parte) ∩ otra parte`), no de una coordenada. **Riesgo de fuga a verificar con
  Guard-v.** [abierto, crítico]
- **Puerta de falsación independiente vinculante** (comité-006): una pasada ciega, sesión separada,
  debe intentar romper la definición cerrada antes de cualquier promoción.
- **Caveat teleológico permanente:** esto es, en el mejor caso, un precursor *aparente / de
  atrapamiento* en un parche finito 1+1D — NUNCA un horizonte de sucesos, NUNCA reconstrucción.
  `NO_RECONSTRUCTION_CLAIM` se mantiene.

## 7. Backing

- Contenido clásico (horizonte aparente, `Θ_out=0`, teleológico): `biblioteca/Horizontes…md` §1, §6
  [THEOREM-CONFIRMED]; EGS `biblioteca/derived-md/Towards black-hole horizons…md:223-225` (`Θ_out`),
  :175 (no `𝒥⁺` en finito), :195,:463 (Hayward, fallo de bimodalidad de cadena para BH regular).
- C1/C2/C3 y la arquitectura evento+validador: `docs/comite/comite_decision_006_*` (§ Candidate
  summary; verdict `REFINE_CANDIDATES_BEFORE_PROMOTION`); `dev/X0_Qn_wellposedness_NOTES.md` §11.
- TIPs / frontera causal: `biblioteca/Horizontes…md` §F (candidato 5, TIPs sobre covtree); Minguzzi
  (lectura #12 del informe) — citados como objeto asintótico NO disponible en finito.
- Riesgo de fuga "outward"/dirección espacial: `docs/pr003_leakage_gate.md`;
  `nachocausal/estimator.py` Guard-v `verify_order_only`.
- Pivote y scope: [[strategic-refocus-relational-definition]]; observable de enlaces = rectángulo de
  Alexandrov vacío `dev/PR003_L1B_LPP_MAPPING_NOTES.md` §1.

## §9 — Pregeometric relational horizons and finite persistent growth

### 9.1. The Pregeometric Relational Horizon Hypothesis

We reformulate the problem of the horizon to align with a purely pregeometric, quantum-covariant framework, removing any dependence on coordinates, metrics, or background manifolds.

*   `[DEFINITION] 9.1.1 (Pregeometric Relational Horizon).` Let $C = (X, \preceq)$ be a causal poset and let $R \subset X$ be an internally defined, relational reference subset representing "escape" or "asymptotic future". The *relational past of escape* is the down-set:
    $$\mathcal A_R := \downarrow R = \{ x \in X : \exists y \in R, \ x \preceq y \}$$
    The *relational black hole region* relative to $R$ is the complement:
    $$\mathcal B_R := X \setminus \mathcal A_R$$
    The *pregeometric relational horizon* is the relational boundary interface:
    $$\mathcal H[C; R] := \{ (x, y) \in \mathcal B_R \times \mathcal A_R : x \prec \text{link} \ y \}$$
    where $x \prec \text{link} \ y$ denotes a causal link (an immediate relation with no intermediate elements).

---

### 9.2. The Relational Reference $R$ in Finite Posets

*   `[PROVED] Proposition 9.2.1 (The Triviality of Static Absolute Ends).` *If $C$ is a finite causal set, defining $R$ as the set of future ends $\mathscr E^+(C)$ yields a trivial horizon:*
    $$R = \mathscr E^+(C) \implies \mathcal H[C; R] = \varnothing$$

    *Proof.* By Proposition 8.8.1, for any finite poset $C$, $\mathscr E^+(C) = \varnothing$. Thus, $R = \varnothing \implies \mathcal A_R = \varnothing \implies \mathcal B_R = X$. Since $\mathcal A_R$ is empty, the Cartesian product $\mathcal B_R \times \mathcal A_R$ is empty, meaning $\mathcal H[C; R] = \varnothing$. $\blacksquare$

*   `[CONJECTURE] 9.2.2 (Dynamic Escape via Truncated Flow).` In a finite causal set $C$ representing a partial history, the relational reference $R$ cannot be absolute. It must be defined dynamically, either as:
    1.  The set of maximal elements of $C$: $R = \operatorname{max}(C) = \{ x \in X : \nexists y \in X, \ x \prec y \}$.
    2.  A subset of maximal elements selected by a "growth flow" or sequential growth process (such as Classical Sequential Growth, CSG).
    3.  A family of discrete "ladders" approximating null geodesics that do not experience discrete focusing (cf. Eichhorn, Gamito, & Stokes, 2026).

---

### 9.3. Semiclassical Consistency Constraints (The No-Spurious Horizon Test)

Any proposed pregeometric operator $\mathcal{H}[C; R]$ must satisfy two strict classical correspondence limits when evaluated on manifoldlike causal sets obtained via Poisson sprinkling $C_{\rho, R}$ of density $\rho$ in a compact region $M_R \uparrow M$:

1.  **Black Hole Limit:** If $M$ is Schwarzschild, the spatial concentration of $\mathcal{H}[C_{\rho, R}; R']$ must converge to the classical event horizon $r = 2M$ as $\rho, R \to \infty$.
2.  **Minkowski Limit (No Spurious Horizons):** If $M$ is flat Minkowski space, the expectation value of the horizon size or its persistence must vanish:
    $$\lim_{R \to \infty} \lim_{\rho \to \infty} \mathbb P \left( \mathcal H[C_{\rho, R}; R'] \neq \varnothing \right) = 0$$
    A pregeometric proposal that detects a stable, non-vanishing boundary in flat space is physically invalid.

---

### 9.4. Quantum Formulations: The Horizon as a Covariant Event

In a sum-over-histories formulation of causal set quantum gravity, a horizon cannot be localized as a surface on a single, fixed poset. It must be formulated as a *covariant event* (a property of the configuration space of posets):

*   `[CONJECTURE] 9.4.1 (Horizon Covariant Event).` Let $\Omega$ be the space of all finite causal sets. The quantum horizon is represented by a covariant event (a subset of histories) $\Omega_{\mathcal H} \subset \Omega$, defined by the relational structure of $\mathcal H[C; R]$:
    $$\Omega_{\mathcal H} := \{ C \in \Omega : \mathcal H[C; R] \text{ satisfies a specific relational partition} \}$$
    The quantum dynamics (via the decoherence functional or partition function) assigns a quantum measure or quantum probability to the existence and stability of this relational partition.
