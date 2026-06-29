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

## 7. Sub-problema previo de (III): ¿define el orden DOS CARAS no temporales alrededor de A? (conceptual, sin código)

Paso autorizado (usuario, esta sesión): **antes** de construir el estadístico one-way, resolver el
cuello de botella lógico — ¿existe, a partir de un entorno relacional `N(A)`, una **pareja no
ordenada** `{L_A, R_A}` con `L_A ⊔ R_A = N(A)\A`, que (1) dependa solo de `≺`; (2) sea
relabel-invariante; (3) equivariante bajo automorfismos; (4) NO use altura como sustituto de lado
espacial; (5) NO use `r`/embedding/`relphi`/outgoing/horizonte; (6) sea única salvo intercambio
`L_A ↔ R_A`? Si NO existe, cualquier estadístico dirigido reintroducirá geometría externa.

### 7.1 Por qué pasado/futuro es fácil y lateral es el problema real

`A` (antichain) induce `down(A)` (pasado) y complemento (futuro) — **bipartición temporal, gratis del
orden**. Pero esas no son las dos caras *laterales* que coexisten al MISMO rango de altura a ambos
lados del cuello. En 1+1D el orden `≺` codifica la estructura de **conos de luz** = estructura
causal/conforme; la dirección espacial es *precisamente la que `≺` no distingue puntualmente* (los
dos lados espaciales de un punto son ambos spacelike, simétricos). Definir "ambos lados" sin
coordenada es donde acecha la fuga (constraint 4–5).

### 7.2 Examen de los tres mecanismos (ninguno presupuesto)

**(M2) Firmas de incidencia causal con A (pasado/futuro cercano de A).** Para `x∈N(A)\A`: vector
(`#A` de cuyo pasado es `x`, `#A` de cuyo futuro, `#A` spacelike a `x`). Da la **posición TEMPORAL**
de `x` relativa a `A`, y es **paridad-simétrica** (un punto a la izquierda y su espejo a la derecha
tienen la misma firma). **NO produce split lateral. Falla** para (III).

**(M3) Partición espectral / Fiedler.** Sobre el **grafo de comparabilidad** del band, el Fiedler
separa pasado de futuro (la conectividad fuerte es por cadenas = temporal) ⇒ **reproduce la altura,
viola constraint 4**. Sobre el **grafo de incomparabilidad** de un band delgado (casi todos spacelike
⇒ grafo casi completo) el Fiedler es **plano ⇒ sin corte canónico**. Sólo funciona si se repondera
hacia la estructura conjugada — y entonces **colapsa en (M1)**. Solo, **falla**.

**(M1) Componentes/cortes del grafo de incomparabilidad — reinterpretado como ORDEN CONJUGADO.**
Componentes: en 1+1D el grafo de incomparabilidad de un band es casi completo (izq y der lejanas son
spacelike entre sí) ⇒ **una componente, no separa.** PERO hay un hecho estructural decisivo:

> **Un sprinkling de Minkowski 1+1D es, por construcción, un orden de DIMENSIÓN 2:** `x≺y ⇔ u_x<u_y ∧
> v_x<v_y` (orden producto en las dos coords nulas). Por el teorema de dimensión de orden
> (Dushnik–Miller 1941), su **grafo de incomparabilidad es un grafo de comparabilidad**, cuya
> **orientación transitiva = el orden conjugado `Q`** (la dirección ESPACIAL). `Q` es intrínseco a
> `≺`. **La reversión de `Q` corresponde al swap `L_A↔R_A`.**

**Unicidad — NO garantizada en general [corrección, usuario].** "Único salvo reversión" vale para los
**componentes PRIMOS de la descomposición modular** del grafo de comparabilidad (Gallai 1967). Un
grafo **no primo** admite elecciones independientes en distintos módulos ⇒ varias orientaciones
transitivas NO relacionadas por una reversión global. Por tanto invocar "Gallai para grafos primos"
**no cierra el caso real**. Hay que: (1) demostrar que el grafo relevante es primo; **o** (2) aceptar
la descomposición modular y probar que **todas** sus orientaciones admisibles inducen la **misma
pareja de caras**; **o** (3) declarar C2′ no cerrado en causets con módulos no triviales. [ABIERTO]

`Q` es un orden **PARCIAL** (también 2D), no lineal: linealiza sólo los pares `P`-incomparables
(spacelike); dos elementos `P`-comparables (timelike) son `Q`-incomparables. Esto importa para la
construcción de caras (§7.4): un vecino timelike a un `a∈A` no es ni `Q`-izquierda ni `Q`-derecha de
`a` — el "tercer residuo" que hay que excluir.

### 7.3 Dimensión de orden ≤ 2: TEOREMA por auditoría del generador, NO por medición [corrección, usuario]

**Retracto** dos afirmaciones erróneas de la versión previa: "la tortuga rompe el orden-producto y la
dimensión puede exceder 2 cerca del horizonte" y "el ruido de sprinkling puede dar dimensión >2".
Ambas son **falsas** si la relación observada es la restricción de un orden-producto 2D — y lo es:

- **BH es conformalmente plano en 1+1D.** En coordenadas nulas de Kruskal–Szekeres la parte radial de
  Schwarzschild es `ds² = Ω²(U,V) dU dV`, **regular a través del horizonte**; la causalidad la fija el
  orden de las dos coords nulas: `x≺y ⇔ U_x<U_y ∧ V_x<V_y`. La singularidad de `r_*` (tortuga) es de
  la CARTA Schwarzschild/EF, **no** una ruptura física del orden. El parche EF ingoing = regiones I∪II
  de Kruskal; un **suborden** de un orden-producto sigue siendo orden-producto. [razonamiento físico;
  el paso "parche EF = restricción del producto Kruskal" marcado [UNVERIFIED] vs cita primaria, pero
  es estándar.]
- **Auditoría del generador (hecha esta sesión, lectura de código):** `nachocausal/generator.py:88`
  `past_matrix_fast` implementa la relación EF cerrada de He–Rideout (Minz `isCausal_BH2D`), verificada
  **bit-a-bit** vs Minz hasta `N=10017`, `100,340,289` pares (`docs/reuse_check.md:27-33`,
  `dev/gate_highN.py`). Las ramas `b1/b2/b3` son la forma chart-dependiente de computar **el mismo**
  orden; no añaden ni quitan relaciones respecto a la causalidad exacta.

> **Proposición condicional 7.3 (representación producto del generador radial 1+1D) [usuario].**
> *Supóngase que la relación producida por `past_matrix_fast` coincide exactamente con la causalidad
> radial de la métrica Schwarzschild en el parche ingoing-EF utilizado.* La reducción radial admite
> coordenadas nulas de Kruskal `(U,V)`, regulares al cruzar el horizonte, en las que
> `ds²_(2) = −Ω²(U,V) dU dV`. Con la orientación temporal fijada, la relación causal sobre las
> regiones exterior e interior cubiertas por el parche es la restricción del orden producto
> `x ≺ y ⇔ U_x < U_y ∧ V_x < V_y`, casi seguramente bajo sprinkling continuo (sin empates). Por
> tanto `P_C = L_U ∩ L_V` y `dim_DM(C) ≤ 2`. En consecuencia **existe al menos un orden conjugado
> `Q`** sobre las parejas incomparables de `P_C`.

**Alcance de la Proposición 7.3 (lo que SÍ y lo que NO da).** Establece una **orientación lateral
order-only** (vía `Q`) para BH y MINK por igual — condicional a la hipótesis (generador = causalidad
radial exacta), NO a una medición de dimensión. **Por eso NO hay que "atacar la dimensión de BH"
midiendo: es una propiedad del generador.** La hipótesis es auditable y está fuertemente respaldada
(`past_matrix_fast` = Minz `isCausal_BH2D` bit-a-bit, `reuse_check.md:27-33`; Minz = relación
He–Rideout exacta, premisa de reuse-check). **PERO la Proposición 7.3 NO demuestra** que una antichain
`A` induzca una pareja **exhaustiva y canónica** de caras `{L_A, R_A}`: eso requiere el lema de
bipartición de §7.4 y el tratamiento de la descomposición modular de §7.2. `orden conjugado ⇏ dos
caras`.

### 7.4 El lema de DOS CARAS: orden conjugado ⇏ bipartición (el paso que FALTA) [usuario]

Recuperar `Q` es avance real, pero **no construye** `{L_A, R_A}` automáticamente. Como `A` es antichain
en `P`, `Q` lo ordena linealmente; pero un vecino `x∈N(A)\A` puede quedar `Q`-antes de todo `A`,
`Q`-después de todo `A`, **o intercalado** entre dos elementos de `A` — y, peor, si `x` es
`P`-comparable (timelike) a algún `a∈A`, es `Q`-incomparable a `a` (§7.2) ⇒ **tercera clase
residual**. Para que la bipartición exista hay que **probar un lema**, no asumirlo:

- elegir `N(A)` como una **losa spacelike** (todo `x∈N(A)\A` es `P`-incomparable a todo `A`), y
- probar que `A` es un **bloque `Q`-convexo**, y entonces definir
  `L_A = {x : x <_Q a  ∀a∈A}`, `R_A = {x : a <_Q x  ∀a∈A}`, y
- **demostrar exhaustividad y disjunción:** `N(A)\A = L_A ⊔ R_A` (sin residuo intercalado ni
  `Q`-incomparable).

Si existen elementos intercalados o `Q`-incomparables relevantes, **la bipartición NO está
construida.** Este lema es el verdadero contenido de "el orden define dos caras".

### 7.4.1 Análisis del lema (esta sesión): construcción de Q, intercalado, y resultado parcial

**Construcción explícita de `Q` (paso 2).** Con realizador `P = L_U ∩ L_V` (Prop. 7.3), define el
conjugado `x <_Q y :⇔ U_x<U_y ∧ V_x>V_y`. Es la **orientación transitiva del grafo de
incomparabilidad** de `P` (todo par `P`-incomparable = spacelike = exactamente uno de `U<,V>` o
`U>,V<`). `Q` es un orden parcial 2D. Coordenadas auxiliares (sólo para razonar, NO entran en nada):
`τ=U+V` (tiempo), `ξ=V−U` (espacio). `Q` ordena por `ξ` creciente entre pares spacelike.

**El intercalado es GENÉRICO para |A|≥2 (contraejemplo trabajado).** Sea `A={a₁,a₂}`,
`a₁=(U,V)=(0,2)`, `a₂=(2,0)` (antichain: spacelike; `a₁<_Q a₂`). Vecino `x=(1,1)`:
- vs `a₁`: `U:0→1↑, V:2→1↓` ⇒ spacelike, y `a₁<_Q x`.
- vs `a₂`: `U:1→2↑, V:1→0↓` ⇒ spacelike, y `x<_Q a₂`.
⇒ `a₁ <_Q x <_Q a₂`: **`x` está `Q`-INTERCALADO**, spacelike a todo `A`, en `τ=2` (igual que `a₁,a₂`):
geométricamente *entre* los dos puntos-membrana, en la misma rebanada. **No es ni `L_A` ni `R_A`.**
Esto NO es patológico: cualquier antichain de extensión espacial >0 tiene vecinos spacelike en su
"hueco" interior. ⇒ **`N(A)\A = L_A ⊔ R_A` FALLA para `|A|≥2`** con la definición Q-extremos. El lema
de bipartición EXHAUSTIVA, tal como se pidió, **es FALSO en general.** [refutación, no laguna]

**Resultado positivo 1 — marcador de un solo elemento (`|A|=1`).** Si la membrana se marca por un
único elemento `a`, no hay "entre": todo `x` spacelike a `a` cumple `x<_Q a` ó `a<_Q x`,
**exhaustivamente**. ⇒ `L_a={x spacelike : x<_Q a}`, `R_a={x spacelike : a<_Q x}`,
`spacelike(a)=L_a⊔R_a`, **canónico salvo swap** (reversión de `Q`). El único residuo son los vecinos
timelike (`≺a` ó `a≺`), que se excluyen definiendo `N(a)=spacelike(a)`. **Bipartición LIMPIA.** ✓

**Resultado positivo 2 — tripartición canónica (`|A|≥2`).** En general, lo canónico no es una
bipartición sino la **TRIPARTICIÓN** `{L_A, core_A, R_A}` con
`L_A={x : x<_Q a  ∀a∈A}`, `R_A={x : a<_Q x  ∀a∈A}`, `core_A = (N(A)\A) ∖ (L_A∪R_A)` (intercalados +
timelike). `core_A` ≠ ruido: es el **grosor relacional de la membrana** (los elementos
espacialmente dentro del cuello), que conecta con la persistencia (§4). El estadístico de asimetría
puede compararse sobre las **dos caras exteriores** `L_A, R_A` (intercambiables por swap), tratando
`core_A` como la propia membrana. Esto NO es la bipartición exhaustiva pedida, pero **sí un objeto
canónico order-only** suficiente para `Δ_A`.

**Descomposición modular / unicidad (paso 3, SIN asumir primalidad).** `Q` (y por tanto el split
`L/R`) es único salvo reversión **sii** el grafo de incomparabilidad es **primo** en su
descomposición modular (Gallai); equivalentemente, sii el 2D-orden `P` tiene realizador único salvo
swap. Si hay un **módulo** `M` no trivial, sus elementos pueden orientarse independientemente ⇒
múltiples `Q`. **Pero:** un módulo en este grafo = un subconjunto `M` tal que todo `x∉M` es spacelike
a todo `M` o a nada de `M` — una **degeneración geométrica no genérica** bajo sprinkling Poisson
continuo. [PLAUSIBLE, [UNVERIFIED]: "2D-orden Poisson es primo c.s. para N grande" — estándar para
órdenes aleatorios pero no anclado a cita primaria en biblioteca.] Si se confirma, `Q` es único salvo
swap **casi seguramente**; los casos no primos son medida cero / borde, a manejar con una regla de
desempate relabel-invariante (p.ej. orientar el módulo por su propio sub-conjugado, recursivamente).

### 7.5 Circularidad que el face-construction DEBE evitar (crítico)

Las dos caras del horizonte (interior/exterior) **son** distinguibles por su futuro (interior
truncado por singularidad, exterior largo). Tentación: definir "cara capturada" = la de futuro
truncado. **Eso es CIRCULAR**: el estadístico de (III) mide después la asimetría de acceso futuro; si
las caras se definen por esa misma asimetría, `Δ_A≠0` es tautológico. ⇒ **La bipartición debe usar
SOLO el orden conjugado `Q` (lateral, ⟂ futuro), nunca la accesibilidad futura que el estadístico
luego mide.** El conjugado cumple esto (es espacial, no temporal); la definición-por-truncación NO.

### 7.6 Veredicto del sub-problema — PROVISIONAL (no cerrado)

**Estado provisional, NO un veredicto de cierre todavía.** Lo establecido y lo que falta:

**Avance real (lo establecido):** en un orden causal de **dimensión 2** — que es el caso para BH y
MINK **condicional a la auditoría del generador `P_C=L_U∩L_V`** (§7.3, razonamiento Kruskal +
verificación Minz bit-a-bit) — el **orden conjugado `Q` existe** y porta una noción intrínseca de
**orientación lateral, definida solo salvo reversión** (= el swap permitido `L_A↔R_A`), order-only y
relabel-invariante. Esto es un resultado conceptual importante y descarta, *para el NULL plano*, el
veredicto `III_REQUIRES_EXTERNAL_GEOMETRIC_REFERENCE`.

**Por qué NO se declara aún `III_UNORDERED_FACES_EXIST_BUT_ASYMMETRY_NOT_CLOSED`:** ese token afirma
que las caras **existen**; pero "antichain `A` ⇒ dos caras canónicas" **no está demostrado** — falta
el **lema de bipartición §7.4** (losa spacelike + `Q`-convexidad de `A` + exhaustividad
`N(A)\A=L_A⊔R_A` sin residuo). Además la **unicidad** depende de la descomposición modular (§7.2,
ABIERTO). Hasta probar el lema, **`orden conjugado ⇏ dos caras`**.

**Token provisional:** `III_PENDING_TWO_FACE_LEMMA` (entre "existe orientación lateral salvo
reversión" y "existen dos caras canónicas"; ninguno de los cuatro tokens de cierre es aún aplicable).

**Próxima ronda correcta (secuencia del usuario; NO medir dimensión sobre BH):**
1. **Auditar la relación EXACTA del generador** y demostrar/refutar `P_C = L_U ∩ L_V` para BH y MINK
   (lectura de `generator.py` + Minz). Si cierto ⇒ `dim(C)≤2` demostrada para toda seed, sin
   experimento. [§7.3 ya da el esqueleto; falta la prueba formal del paso EF=restricción-Kruskal]
2. **Construir `Q`** explícitamente por orientación transitiva del grafo de incomparabilidad.
3. **Analizar su descomposición modular**, SIN asumir primalidad (§7.2 opción 1/2/3).
4. **Probar el lema de dos caras** (§7.4) para el `N(A)` y la `A` concretos de C2′.
5. **Sólo si** la unión es exhaustiva y única salvo swap: mantener un veredicto de cierre y, entonces,
   construir el estadístico `Δ_A=|S(L_A,R_A)−S(R_A,L_A)|` (normalizado por oportunidades, intercambiable
   por swap, robusto a cardinalidades y frontera futura) sobre los cuatro contraejemplos (borde top,
   focusing simétrico, tubo de densidad persistente, terminación singular). **La circularidad §7.5 se
   conserva como restricción vinculante.**

## 8. Backing

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
- §7 (caras no temporales): dimensión de orden 2 / realizador / orden conjugado y orientación
  transitiva única salvo reversión para grafos primos — Dushnik–Miller 1941 (order dimension);
  Gallai 1967 / Trotter *Combinatorics and Partially Ordered Sets* (comparability graphs, modular
  decomposition); sprinkling 1+1D = orden producto 2D: Surya LRR §4, `dev/PR003_L1B_LPP_MAPPING_NOTES.md`
  §2–3. **[UNVERIFIED]:** dimensión de orden del causet Schwarzschild-EF (no en biblioteca; sub-problema
  abierto). Constraint anti-fuga (cara ≠ definida por truncación futura): `docs/pr003_leakage_gate.md`,
  Guard-v `nachocausal/estimator.py`.

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

### 9.5. Lean bridge: ambient end, cofinal direction, finite interface

`[CONCEPTUAL_FORMULATION]` The current Lean formalisation supports a three-layer reading of the
relational C1 programme. This is a vocabulary bridge, not a promotion of C1 and not a physics
result.

1. **Ambient escape/end selection — `IdealEnd`.** The provisional Lean type
   `IdealEnd P := {I : Order.Ideal P // IsNonprincipalIdeal I}` should be read as the algebraic
   placeholder for an ambient escape/downstream ideal. It is intentionally broad. It does **not**
   yet choose the physical escape end, the maximal end, a GKP/TIP object, or an asymptotic boundary.
   Current Lean status: order isomorphisms preserve provisional `IdealEnd`
   (`mapIdealEndOrderIso`), but arbitrary embeddings remain `HYPOTHESES_OPEN`.

2. **Direction inside the selected end — `ChainEnd`.** Once an ambient non-principal ideal has been
   selected, `ChainEndInIdeal I` represents a cofinal direction inside it as a quotient of
   non-terminal cofinal chains. The decision for downstream C1 writing is **coexistence**, not
   replacement: `IdealEnd` selects the ambient ideal; `ChainEnd` represents the cofinal direction
   inside that ideal. Lean now proves that order isomorphisms transport these chain ends
   (`mapChainEndOrderIso`) and that mutual cofinal domination is exactly equality of the lower set
   generated by the chain (`CofinalChainEquivalent_iff_generated_eq`). Thus the quotient is
   algebraically grounded as "same represented lower-set content."

3. **Finite observable interface — `RelationalHorizon`.** For a finite causet and a relational
   reference subset `R`, `RelationalHorizon R` is the finite interface
   $$\mathcal H[C;R] = \{(x,y) : x \in \mathcal B_R,\ y \in \mathcal A_R,\ x \prec_{\mathrm{link}} y\}.$$
   Lean proves only structural facts: `RelationalPast R` is a lower set, enlarging `R` enlarges the
   past and shrinks the black-region candidate, and horizon pairs cross from
   `RelationalBlackRegion R` to `RelationalPast R` along a strict cover
   (`relationalHorizon_lt`, `relationalHorizon_fst_not_mem_past`,
   `relationalHorizon_snd_not_mem_black`). These are order-theoretic guardrails, not recovery of a
   classical horizon.

**C1 reading after the Lean bridge.** C1 should be written as an order-only finite interface
candidate built around $\mathcal H[C;R]$: a closed rule selects or approximates a relational
reference/escape structure `R`; `RelationalHorizon R` supplies the finite boundary interface; any
putative persistence/asymmetry condition must be expressed through order-invariant structure on that
interface and, if an end-direction is invoked, through the `IdealEnd`/`ChainEnd` split above. The
selection rule for `R` and for any C1 antichain/flux comparator remains **OPEN** and must be closed
before any dev probe. No `K_LOC`, `z*`, `theta_*`, validation seed, or sealed estimator quantity is
touched by this bridge.
