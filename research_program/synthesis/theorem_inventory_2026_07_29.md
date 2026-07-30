# Inventario de núcleos con rango de teorema — revisión literal del repositorio

> **STATUS: LITERAL_INVENTORY / UPDATED_2026-07-29_AFTER_C6_CLOSURE_AND_PROMOTION /
> NOT_A_COMITE_ACTA / NO_NEW_MATHEMATICS / NO_CODE / NO_SIMULATION / NO_SEEDS /
> SEALED_PATH_UNTOUCHED.**
>
> Encargo del PI (2026-07-29): inventariar el cuerpo completo de resultados con rango de teorema
> mediante revisión literal del repositorio, **sin contar decisiones, experimentos ni etiquetas
> como teoremas**, y valorar si ya existe la columna vertebral de un trabajo matemático
> independiente. La versión inicial no promovía ni re-etiquetaba resultados. Esta actualización
> registra el cierre de C6 en `141cccc` y su promoción documental como Teorema 3.9, sin alterar el
> techo matemático ni convertir la revisión interna en validación externa por pares.

## 0. Criterios de inclusión y método

**Cuenta como núcleo de rango teorema:** un enunciado matemático preciso con demostración
completa escrita en el repositorio (verificable línea a línea) o verificada por máquina.
**No cuenta:** veredictos y etiquetas de comité (un `[PROVED]` sin prueba residente no es prueba),
resultados numéricos/Monte Carlo, heurísticas marcadas `[UNVERIFIED]`, y lemas subsidiarios
internos de líneas cerradas (p. ej. las notas espectrales `dev/C5_*` de la línea localizadora
cerrada por actas 042/046) — estos últimos existen pero no se cuentan como núcleos independientes.

Método: búsqueda literal (`grep`) de enunciados y marcadores de estatus sobre `docs/`,
`research_program/`, `dev/`, `formal/`, seguida de lectura dirigida de cada fuente primaria.
Los ocho candidatos señalados por el PI fueron localizados todos; la revisión añadió dos entradas
que el listado del PI no incluía (núcleo 2 y el ítem calificado Q2). Tras el cierre de C6, el
antiguo Q1 pasa a núcleo pleno 9.

## 1. Resultado del conteo

```text
NUCLEOS_RANGO_TEOREMA_PLENO = 9
ITEMS_CALIFICADOS_NO_CONTADOS_COMO_PLENOS = 1
```

## 2. Los nueve núcleos plenos

### Núcleo 1 — Ambigüedad de la maximalidad futura (finita e infinita, clase 2D)

*(El "Teorema de Bruno" del PI: ese nombre no aparece en el repositorio — "Bruno" figura solo
como alias de un checkout de mathlib en `docs/comite/comite_decision_012:212`. El contenido está,
bajo otro nombre.)*

- **Enunciado:** para todo poset finito `O` con `dim_DM(O) ≤ 2`, `|O| ≥ 2`, y todo `e ∈ Max(O)`,
  existen extensiones futuras contables, localmente finitas, de dimensión ≤ 2, `Q_A` y `Q_B`,
  con `e ∉ Max(Q_A)` y `e ∈ Max(Q_B)` — el subposet observado admite completaciones con
  propiedades globales opuestas; corolario directo: maximalidad interna ⇏ maximalidad global.
- **Dónde:** `dev/PR003_INFINITE_MAXIMALITY_NONCERTIFIABILITY.md:18-68` (`VERDICT = PROVED`,
  prueba explícita por realizadores en §4–§5). Capa finita previa:
  `dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md` y verificación acotada por máquina
  `docs/alloy/alloy_verification_001_completion-maximality-counterexample.md`.
- **Estatus literal:** PROBADO, autocontenido, con anclajes primarios (Dushnik–Miller, Rideout).
- **Caveats vigentes (del propio documento):** teorema combinatorio sobre 2-órdenes, **no** un
  no-go físico (sin sprinkling ni manifoldlikeness); `|O|=1` excluido bajo la lectura fuerte.
- **Residencia anómala:** vive en `dev/` (nota matemática committeada) y **no está incorporado al
  manuscrito** — la única mención tangencial de maximalidad está en
  `docs/manuscript_limits_draft.md` §5.3.

### Núcleo 2 — Teorema A / Teorema 3.1: órbita de dilatación con TV = 0 exacta

- **Enunciado:** en 1+1 Schwarzschild, la órbita de dilatación `Φ_s` da
  `TV(P_n(r_s;P), P_n(s·r_s;Φ_s(P))) = 0` para todo `n` y todo `s>0` — el orden observado no
  contiene información alguna sobre la escala absoluta; versión 3+1 en clase acotada
  (`op12_tv_zero_3p1.md`), no como Hauptvermutung general.
- **Dónde:** `docs/manuscript_limits_draft.md` §3.1 (`[PROVED]`); prueba completa en
  `research_program/models/first_witness_pair_candidates.md` §2 (Theorem A, `PROVED`, :62-86);
  consecuencia estimacional vía Teorema 2 de dos puntos.
- **Estatus literal:** PROBADO (el propio expediente lo califica de "modest content" — exacto
  pero de contenido modesto; la honestidad de esa calificación debe conservarse).

### Núcleo 3 — Teorema 3.2: el horizonte de eventos global no es funcional del parche finito

- **Enunciado:** `T_EH` no es medible respecto de los datos de un parche causalmente convexo
  finito (par de completaciones con horizonte opuesto compatible con el mismo parche).
- **Dónde:** `docs/manuscript_limits_draft.md` §3.2 (`[PROVED]`, etiqueta
  `PROVED_NON_IDENTIFIABILITY`).
- **Caveat vigente:** específico de `T_EH` (teleología); no es un no-go para cualquier noción de
  horizonte — el manuscrito lo dice explícitamente (:485-489, "What Theorem 3.2 does not say").

### Núcleo 4 — Teoremas de dos puntos para indeterminación order-only

- **Enunciado:** Teorema 1 (caracterización exacta de identificabilidad con error cero);
  Teorema 2 (cota de dos puntos: para todo estimador order-only, riesgo ≥ (1−TV)/2, transportada
  al canal de posets finitos); Corolario 3 (aplicación a target binario de horizonte).
- **Dónde:** `research_program/work_packages/wp4_two_point_theorem.md:17-137` — "Teorema 1,
  PROBADO", "Teorema 2, PROBADO", "Corolario 3, PROBADO como condicional".
- **Caveat estructural (del propio documento):** el Corolario 3 exige exhibir un par geométrico
  admisible no trivial; sin él "el Teorema 2 es un arma sin munición" (:198-204). La parte
  matemática es incondicional; la aplicación física es la que queda condicionada.

### Núcleo 5 — Teorema 3.8: suelo de localización order-only (QMD/Hellinger, familia diamante)

- **Enunciado:** cota TV ≤ (|δ|/2)√(n·Ī), reducción estimación→test, y radio minimax de orden
  `1/√(n·Ī)` a `n` fijo, para **todo** estimador order-only (aleatorizado incluido) sobre la
  familia diamante 1+1 declarada.
- **Dónde:** `docs/manuscript_limits_draft.md` §3.3, Teorema 3.8 (`[PROVED]`); anexo
  `research_program/work_packages/wp4_fisher_localization_floor.md` (Props 1-5, Lemas 2.1-2.2,
  R) con chequeos simbólicos en `wp4_fisher_localization_floor_symbolic_checks.py`.
- **Sobre la parte delicada señalada por el PI (el canal de clases de isomorfismo):** está
  tratada — la independencia-del-parámetro del mapa muestra→poset se prueba en coordenadas de
  cópula (Lema 2.2 del anexo; toda la dependencia en τ queda en la densidad), y el data
  processing hace el resto. La cota **hereda** del nivel puntual y puede ser holgada para posets;
  el manuscrito lo declara en “What Theorems 3.8–3.9 do and do not claim”. Finitud de Ī probada;
  su valor numérico `[NUMERICAL]`.
- **Caveat obligatorio del manuscrito (§3.3):** prohibido narrarlo como "cota de detector de
  horizonte" — τ es simultáneamente radio de horizonte y única amplitud de curvatura.

### Núcleo 6 — Anexo C: resultados exactos de separación del estadístico de pares comparables

- **Enunciado:** Prop C7 (`h_1` en forma cerrada), Prop C8 (`ζ_1 > 0` estricto), Teorema C9
  (`ζ_1 → 1/36` cuando `dv → 0⁺`, límite exacto), Corolario C6 (`Δp ≠ 0` para todo
  `dv < dv_0`, con `dv_0` no efectivo).
- **Dónde:** `research_program/work_packages/wp4_comparable_pair_separation.md` §4–§4b.
- **Caveats literales:** el orden `O(dv²)` de la corrección de C9 está apoyado en evidencia
  numérica (ratios `2.17…3.85→4`; acta 045: "`[NUMERICAL]` only… not on the `TV→1` path");
  en cambio, la extensión analítica y la cota \(C^1\)-uniforme usadas por el Corolario C6 están
  escritas y probadas desde `141cccc`. El \(dv_0\) existe de forma no numérica; no se certifica un
  valor concreto. El límite `1/36` en sí es exacto y probado.

### Núcleo 7 — La cintura `W(p,q)` es una anticadena order-only

- **Enunciado:** para todo par `p ≺ q`, `W(p,q)` (bi-enlaces internos del intervalo de
  Alexandrov) es una anticadena.
- **Dónde:** demostración completa por casos en
  `docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md:126-165`.
- **Residencia anómala:** la prueba vive **dentro de un acta de comité** — cuenta como prueba
  (es matemática literal, verificable), pero no existe como nota matemática independiente
  citable. Lo NO probado, per la propia acta (:193-216) y la revisión 044: abundancia,
  estabilidad, y carácter de pantalla de codimensión dos; "existencia de pantallas: SÍ
  (probada)" se refiere solo a la buena definición y anticadena.

### Núcleo 8 — Obstrucción a la coorientación natural de "exterior" (2026-07-29)

- **Enunciado:** (i) Lema 1: `θ_{fℓ} = f·θ_ℓ` exacto — el signo/anulación de la expansión es
  propiedad del rayo, no del representante; (ii) Lema 2: covariancia por difeomorfismos de la
  clase y de θ; (iii) test falsificador: existe `(g,U)` (loncha `Σ≅S³`, esfera ecuatorial `S`)
  con isometría propia y ortócrona `ψ` que deja `S` invariante como conjunto e intercambia sus
  dos presentaciones como borde de región compacta — el selector "exterior = fuera de Ω" queda
  `REFUTED` en la clase local compacta declarada; (iv) dicotomía del extremo: dotar de contenido
  a "extremo asintótico" con `Σ` compacta es contradicción topológica; toda lectura con contenido
  colapsa en información exterior a `U` (define `Q_end(N,g,U;e)`) o en la componente de `∂U`.
- **Dónde:** `research_program/work_packages/phase3_b2_decision048_conditions_review.md`
  (Condición 1: Lemas 1-2 probados, test S³ ejecutado y concluyente; commit `5924b6b`);
  `research_program/work_packages/phase3_b2_asymptotic_end_restriction_review.md` §1, §4
  (commit `edd6bb6`); terminal en `phase3_b2_qfmots_terminal_decision.md` (commit `d12ea86`).
- **Caveats vigentes:** `FATAL_FOR_CURRENT_TARGET, NOT_UNIVERSAL_NO_GO` — refuta ese selector en
  esa clase, no toda definición intrínseca posible; la construcción es geometría diferencial
  autocontenida, sin anclaje en `biblioteca/` (que carece de textos de GR matemática).

### Núcleo 9 — Separación `fixed_n` y exponente de frontera vía pares comparables

- **Enunciado:** para cada intervalo compacto admisible
  \(K=[\tau_0,\tau_1]\) existe un \(dv_0>0\), uniforme en \(\tau\in K\), tal que
  para todo \(0<dv<dv_0\) la probabilidad \(p(\tau)\) de comparabilidad de dos puntos
  es estrictamente creciente y satisface una cota inferior Lipschitz uniforme. Para
  cada par fijo \(\tau\ne\tau'\),
  \(\mathrm{TV}(Q_\tau^n,Q_{\tau'}^n)\to1\) mediante el estadístico order-only
  \(S_n\) de pares comparables. El \(n_0\) es dependiente del par; solo es uniforme
  bajo \(|\tau-\tau'|\ge\eta>0\).
- **Dónde:** prueba analítica completa y cota uniforme en
  `research_program/work_packages/wp4_comparable_pair_separation.md` §4–§4b,
  cerrada en `141cccc`; promoción en `docs/manuscript_limits_draft.md`, Teorema 3.9
  y Corolario 3.10.
- **Consecuencia de tasa:** junto con el Teorema 3.8, el exponente
  \(n^{-1/2}\) queda cerrado en el sentido \(o/\omega\): indistinguibilidad para
  \(o(n^{-1/2})\) y test consistente para \(\omega(n^{-1/2})\).
- **Caveats vigentes:** no se certifica un \(dv\) numérico; no hay \(n_0\) uniforme
  sin separación \(\eta\); no se resuelve la constante crítica en
  \(\delta_n\asymp n^{-1/2}\), la eficiencia constante de \(S_n\), el canal Poisson
  no condicionado, 3+1 ni reconstrucción de horizonte. Es cierre interno
  reproducible, no validación externa por pares.

## 3. El ítem calificado no contado como pleno

### Q2 — Pista Lean verificada por máquina

`formal/HorizonFormal/HorizonFormal/Horizon.lean`: ~25 teoremas compilados, incluidos el
tombstone `relationalHorizonOld_eq_empty` (:120-125; una definición plausible probada vacía para
todo `R` en todo preorden) y el testigo de no-vacuidad de la definición corregida (:246+).
Máximo nivel de verificación del repositorio, contenido matemático modesto (teoría de órdenes
elemental); su papel es de estándar metodológico (no-vacuidad exigible a toda clase nueva — el
estándar que los contratos B2 heredan), no de núcleo publicable por sí mismo.

## 4. Valoración: ¿existe la columna vertebral de un trabajo matemático independiente?

**Sí — con una precisión.** Los nueve núcleos no son bloqueos dispersos: forman una familia con un
enunciado organizador único, *qué información geométrica global determina —y a qué tasa— un dato
causal local finito*:

| Capa | Núcleos | Lo que dicen |
|---|---|---|
| Orden puro | 1 | lo observado no determina propiedades globales de la completación (maximalidad) |
| Grados de libertad globales exactamente invisibles | 2 (escala), 3 (teleología), 8 (coorientación) | tres teoremas de no-determinación, cada uno con testigo o refutación explícita |
| Cuantitativa: lo que sí se ve, se ve a tasa `√n` | 4, 5, 9 | suelo minimax (todo estimador) **y** separación positiva por \(S_n\), con exponente probado por ambos lados en el sentido \(o/\omega\) |
| Constantes exactas | 6 | `1/36`, `ζ_1>0`, formas cerradas |
| Objetos order-only bien definidos | 7, Q2 | anticadena probada; estándar de no-vacuidad mecanizado |

La precisión: **el vehículo natural ya existe** — `docs/manuscript_limits_draft.md` (línea de
consolidación firmada en el acta 046) contiene los núcleos 2, 3, 5 y 9 como sus
Teoremas 3.1/3.2/3.8/3.9.
Lo que la valoración del PI cambia no es "hace falta otro paper", sino el **centro de gravedad**
del que ya está en marcha: hoy el manuscrito narra "límites de recuperabilidad + positivo sellado
+ ledger de fracasos"; el inventario muestra que cuatro núcleos plenos (1, 6, 7, 8)
siguen **fuera** de él, y que con ellos dentro la contribución dominante sería una familia coherente
de teoremas, no un informe de bloqueos con teoremas de apoyo.

**Huecos de promoción concretos (trabajo documental, sin matemática nueva salvo donde se indica):**

1. Núcleo 1: promover la nota de `dev/` a nota matemática citable (o sección del manuscrito),
   conservando verbatim su caveat "combinatorio, no no-go físico".
2. Núcleo 7: extraer la prueba de anticadena del acta 043 a nota independiente antes de citarla
   en un paper; declarar explícitamente lo no probado (abundancia/estabilidad/codim-2).
3. Núcleo 8: incorporar la obstrucción de coorientación al manuscrito como miembro de la capa de
   grados de libertad invisibles (analogía estructural con 3.2 ya redactada con las cautelas
   correctas en el expediente del extremo, §3).
4. Núcleos 2, 6: anclar a fuente primaria de GR/estadística donde el texto lo pide; `biblioteca/`
   sigue sin textos de relatividad matemática (déficit ya registrado en los expedientes B2).

**Qué no autoriza esta valoración:** ningún claim de novedad frente a literatura (el ítem 5 de
Fase 2 cerró sin certificado de novedad); ninguna promoción de etiqueta sin ejecutar el trabajo
listado; ningún cambio del techo de reclamo de ningún núcleo.

## 5. Relación con la decisión B2 de esta misma fecha

El terminal `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL` (`phase3_b2_qfmots_terminal_decision.md`)
**no se revierte ni se debilita** — este inventario lo refuerza: la obstrucción de coorientación
queda ahora clasificada como miembro de la familia (núcleo 8), no como incidente de la línea B2.
Sí cambia una prioridad de secuencia, que se deja registrada como recomendación al PI: la
adjudicación del contrato v2 (`phase3_b2_trapped_surface_preopening_contract.md`) puede esperar
sin coste — el corpus gana lo mismo con el núcleo 8 dentro del manuscrito sea cual sea el destino
de `Q_trap` — mientras que los pasos de promoción §4.1-4.4 tienen valor inmediato para el track
de consolidación ya firmado (acta 046). La ordenación fina entre ambos es un acto del PI.
