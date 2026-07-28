# Comité Decision 046 — Adjudicación conceptual: generador de hojas de nivel Weyl-sensitive + firma causal (discretización causal-set del detector de horizontes de Page–Shoom)

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

STATUS: CONCEPT_ADJUDICATION_DOCUMENTARY
NO_IMPLEMENTATION / NO_SYNTHETIC_EXECUTION / NO_SEEDS / NO_FREEZE / NO_CONTRACT
DATE: 2026-07-28
PROVENANCE: HEAD=cd92f085e7380cdd496ebeaa185c907a9ddeef3e ; seal thresholds.py
sha256=6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4 (prereg-002 seal #3, untouched)
REVISION: `[REV-A 2026-07-28, revisión PI]` — dos sobre-afirmaciones del borrador corregidas **antes
de la firma**, siguiendo el patrón de corrección acotada de `comite_decision_043` §9.5/§12 (texto
original de los roles **conservado verbatim**; las correcciones se anotan in situ y se consolidan en
§8 y §10, nunca reescribiendo en silencio el brief de un rol):
  1. el test de sustitución `\hat K → Φ(r)=r` del falsificador estaba **sobre-leído** (§5, corrección
     in situ);
  2. Gate B pasa de "bloqueo independiente" a `UNRESOLVED_FINITE_BAND_IDENTIFIABILITY` (§8, §10).
Gate A se **mantiene** como bloqueo decisivo y suficiente, con su razón reformulada. El terminal
sigue siendo negativo; lo que cambia es su alcance, no su polaridad.

## 1. Decision question

Decisión conceptual (exploración, NO confirmación; NO código, NO simulación, NO contrato
numérico): adjudicar si existe una ruta discreta defendible para un "generador de hojas de nivel
Weyl-sensitive + firma causal" como discretización causal-set del detector de horizontes de
Page–Shoom, o si debe cerrarse con un terminal BLOCKED.

**Contexto continuo (Page–Shoom, Schwarzschild, 3+1D):** `K(r) = 48M²/r⁶` (escalar de
Kretschmann); el blanco continuo exacto es `||dK||² = g^{rr}(K'(r))² = (1-2M/r)(K'(r))²`, que se
anula en `r=2M` (las hojas `K=const` cambian de timelike a nula a spacelike ahí).

**Propuesta a adjudicar (pipeline de 4 pasos):** (1) construir intrínsecamente un perfil local
Weyl-sensitive `\hat K(x)` usando solo order+number; (2) generar clases/bandas de nivel
aproximadamente radiales a partir de `\hat K`; (3) medir su carácter causal mediante comparabilidad
intra-clase (timelike/null/spacelike); (4) estudiar si esa estadística aproxima de forma
controlada el signo o el cero de `||dK||²`.

**Gate A** (generador de hojas): ¿existe un observable concreto ya disponible, o inmediatamente
derivable sin estructura externa, cuyo valor esperado en un sprinkling de Schwarzschild 3+1D (i)
sobreviva a `R=0` y sea genuinamente sensible a Weyl; (ii) dependa de `r` cerca de `2M`; (iii) sea
localmente inyectivo en `r` dentro del corredor interior; (iv) tenga varianza/resolución
controlable; (v) no necesite embedding, coordenadas, horizonte dado ni dirección radial
proporcionada?

**Gate B** (norma causal/firma), condicional a A: ¿puede la comparabilidad intra-banda aproximar
demostrablemente el carácter causal de `K=const` o una función controlada de `||dK||²`?

## 2. Verified state

Hechos comprobados **esta sesión** por el chair y re-verificados independientemente por cada rol
(reproducibility engineer, falsifier, warden), cada uno con su comando / `file:line`.

- **Working tree:** `git status --short` → limpio (nada que commitear). `HEAD =
  cd92f085e7380cdd496ebeaa185c907a9ddeef3e`.
- **Seal:** `make verify-seal` → `thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, bit-idéntico al récord
  congelado en `docs/preregistration_002.md:7-9`. Re-verificado independientemente por el warden y
  el falsifier vía `sha256sum nachocausal/thresholds.py`. Sin drift. `RESPECT_SEAL_FREEZE`
  honrado.
- **Alcance de la tarea:** doc-only, exploración conceptual pura. `NO_IMPLEMENTATION /
  NO_SYNTHETIC_EXECUTION / NO_SEEDS / NO_FREEZE / NO_CONTRACT`. Ningún seed consumido (banda
  virgen `[2_000_000, 2_999_999]` y `EXPLORE_POOL` intactos, `docs/preregistration_002.md:14-27`).
  Este documento es el único archivo nuevo de la tarea.
- **No existe generador 3+1D en el repo:** `nachocausal/generator.py:37-50` devuelve embeddings de
  2 columnas únicamente (`pts = low + rng.random((n, 2)) * edges`); el gate de verificación cruzada
  Minz construye `SprinkledCauset(dim=2, ...)` (`nachocausal/generator.py:173`). Confirmado
  independientemente por el reproducibility engineer y el physicist. Ningún `dim=4` ni sprinkler
  3+1D existe en `dev/*.py`.
  `NOT_AVAILABLE` (capacidad de ejecución) — no impide la adjudicación conceptual.
- **Cero literatura Weyl/Kretschmann order-only en el repo:** `grep -rniE "kretschmann|weyl"`
  sobre `docs/`, `research_program/`, `dev/` → **cero hits**. Sobre `biblioteca/derived-md/` →
  solo hits de Weyl-álgebra (QFT/estados SJ) y menciones bibliográficas de "Hermann Weyl", más
  una nota informal `biblioteca/Anticadenas_Benincasa.md:6` (divergencia en singularidades, no
  detector de horizonte). Reproducido independientemente por tres roles de wave 1 y confirmado de
  nuevo por el literature verifier.
- **Ausencia de fuente primaria Page–Shoom:** `grep -ril "shoom"` sobre todo el repo (incluyendo
  `biblioteca/`) → cero hits. Confirmado independientemente por el physicist, el falsifier y el
  literature verifier. Ninguna afirmación sobre "el detector de Page–Shoom" en este documento está
  verificada contra un texto primario; se reconstruye solo de las fórmulas dadas en la pregunta de
  decisión. `[UNVERIFIED — ausencia de fuente, no prueba de inexistencia del método]`.
- **`K(r)=48M²/r⁶` no está anclado en `biblioteca/`:** ningún documento de la biblioteca cita esa
  fórmula ni un método Page–Shoom; es un hecho estándar de GR en 3+1D, tratado aquí como
  `[UNVERIFIED contra fuente local]` aunque no se cuestiona su corrección matemática.
  Confirmado por el literature verifier.
- **Hallazgo dimensional decisivo, verificado en el propio repo:** para el parche 1+1D real del
  proyecto (métrica `f=1-τ/r`), el chequeo simbólico ya comprometido en el repo demuestra
  `R = -2τ/r³` (`research_program/work_packages/wp4_fisher_localization_floor_symbolic_checks.py:71`,
  `assert sp.simplify(R_g - (-2 * tau / r**3)) == 0`, commit `b044399` — no ejecutado de nuevo esta
  sesión, leído del historial ya comprometido) y la invariancia conforme `R[κg]=R[g]/κ`
  (`:72`). Con `τ=2M`: `R=-4M/r³ ≠ 0`. **`R=0` es un hecho de vacío 3+1D, FALSO en el parche 1+1D
  real del proyecto.** El tensor de Weyl se anula idénticamente en `d≤3` (hecho estándar de GR,
  `[UNVERIFIED contra biblioteca/]` pero no se ha encontrado ninguna fuente que lo contradiga); en
  2D el escalar de Kretschmann se reduce a `K_2D=R²=16M²/r⁶` — **no** el `48M²/r⁶` citado en la
  pregunta de decisión (valor 3+1D). Confirmado independientemente por el mathematical-logic
  brief, el physicist y re-verificado por el falsifier.

## 3. Dossier

Ficheros y referencias suministrados al comité (leídos y verificados independientemente por cada
rol, no solo por el chair):

- `research_program/synthesis/geometric_indeterminacy_decision.md` (marco TV/Fisher/minimax
  order-only; §9-11 Schwarzschild, §11 caveat de horizonte global teleológico)
- `research_program/work_packages/next_observable_candidate_matrix.md` (candidatos A/B/C/D ya
  rankeados; B = "intrinsic-cut BDG/SMI contrast" es el análogo más cercano)
- `docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md` +
  `docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md` (línea C6 cerrada,
  terminal `C6_BLOCKED_NO_STABLE_CODIM2_SCREEN`, bloqueo adicional
  `GATE3_TRANSPORT = NO_CLOSED_CANONICAL_TRANSPORT_AMONG_EXAMINED_MECHANISMS`)
- `docs/comite/comite_decision_039_c4-neighbor-graph-adjudication.md` (no-existencia acotada, no
  teorema universal)
- `docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md` (§6 prohibiciones, §7 menú C6)
- `dev/PR003_C1_RELATIONAL_SPEC.md`, `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md`
  (definición relacional 9.1.1; selector de `R` ABIERTO; §7 orden conjugado `Q` / dimensión de
  orden ≤2 para BH 1+1D vía Kruskal)
- `research_program/work_packages/wp4_fisher_localization_floor.md`,
  `wp4_two_point_theorem.md`, `wp5_order_only_blindness_map_definition.md`,
  `wp5_shape_scanner_design.md` (marco de indeterminación Fisher/TV; asimetría "ciego≠visible";
  régimen 3 = diamantes EF)
- `research_program/work_packages/wp4_comparable_pair_separation.md`,
  `research_program/bibliography/ficha_se_busca_tv_order_only.md`,
  `docs/comite/comite_decision_045_candidate-7-1-fixed-n-logical-status.md` (candidato 7.1)
- `research_program/bibliography/next_observable_theory_review.md`,
  `next_observable_source_manifest.md`, `identifiability_bibliography_matrix.md`
- `biblioteca/derived-md/Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md`,
  `biblioteca/derived-md/Continuum_Limit_BDG_Causal_Set_Action_arXiv2007.13192.md`,
  `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md` (EGS,
  arXiv:2605.06813), `biblioteca/derived-md/The causal set approach to quantum gravity.md` (Surya
  LRR 2019)
- `docs/claim_grammar.md` §3
- `formal/HorizonFormal/HorizonFormal/Horizon.lean` (verificado: cero objetos `Weyl`/`Kretschmann`/
  nivel-set en el proyecto; solo imports `Mathlib.Order.*`/`Mathlib.Data.Set.*`, sin
  `Analysis`/`MeasureTheory` — el Gate A no es "no probado en Lean", es **inexpresable** en el
  vocabulario formal actual)
- `.claude/skills/comite/check_comite_brief.py` (gate estructural de este documento)

Guardrails vinculantes: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
`NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

- **Proposed artefact(s):** Single doc-only artefact `docs/comite/comite_decision_046_weyl-level-sheet-page-shoom-adjudication.md` (numbering continues after `docs/comite/comite_decision_045_candidate-7-1-fixed-n-logical-status.md`, the highest existing brief per `ls docs/comite/`). It **must** satisfy the brief gate `.claude/skills/comite/check_comite_brief.py:16-33`: all 14 `REQUIRED_HEADINGS`, plus `### Mathematical logic brief` (mandatory for index ≥ 009), no unfilled template placeholders, and exactly one `^COMMITTEE_DECISION_VERDICT=<v>$` from the valid set. **Format trap:** a terminal token (e.g. `WEYL_SHEET_BLOCKED_*`) is **not** a valid `COMMITTEE_DECISION_VERDICT`. Precedent: `docs/comite/comite_decision_043_...md:574` carries `COMMITTEE_DECISION_043 = C6_BLOCKED_NO_STABLE_CODIM2_SCREEN` **in-body**, separate from the gate's verdict line. A BLOCKED terminal must be paired with `RECOMMEND_DO_NOT_PROCEED`.
- **Environment & seal:** No runtime environment is required — this is doc-only. `make test`/`make dry-run`/`make gate`/`make op21-terminal` must **not** be invoked; the external Minz clone is not needed and must stay untouched. Seal re-verified with `make verify-seal`: `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, identical to `docs/preregistration_002.md:7-9`. No drift.
- **Provenance capture:** commit HEAD `cd92f085e7380cdd496ebeaa185c907a9ddeef3e`, tree clean; `make verify-seal` output pre/post identical; `git status --short` = empty; `make verify-comite` → `BRIEF_CHECK=PASS` for the new file; **`SEEDS_CONSUMED = 0`**, no touch of the virgin band `[2_000_000, 2_999_999]` nor `EXPLORE_POOL`. Session date 2026-07-28. No numeric result is produced, so `pip freeze`/`uname` are not required.
- **Run mechanics:** single foreground authoring pass; no background job. Reversible pre-flight = writing the untracked `.md` plus read-only checks (`verify-seal`, `verify-comite`, `audit`); the only committing step is `git commit` of the `.md`. Nothing here is one-way.
- **Reproducibility risks / ambiguities:**
  - **GATE A is not executable in this repository at any thoroughness — status `NOT_AVAILABLE`.** The proposal is posed for a *3+1D* Schwarzschild sprinkling, but the frozen generator produces 2-column embeddings only (`nachocausal/generator.py:37-50`); the Minz cross-check gate builds `SprinkledCauset(dim=2, ...)` (`:173`). No `dim=4` sprinkler exists anywhere in the repo.
  - **No Weyl/Kretschmann-sensitive observable exists in the repo — `NOT_AVAILABLE`.** `grep -rniE "kretschmann|weyl"` over `docs/`, `research_program/`, `dev/` returns **zero** hits.
  - **The nearest established discrete curvature machinery targets the wrong invariant — `ESTABLISHED`, and adverse.** Benincasa–Dowker's operator family approximates `−(1/2)R` (`Benincasa_Dowker_2010_...md:16,38,112`). In 3+1D Schwarzschild vacuum `R≡0`; this removes the only `ESTABLISHED` curvature primitive the project could have reused (and the closest ranked candidate B in `next_observable_candidate_matrix.md:24` inherits the same blindness).
  - **Dimensional scope conflict, both branches fatal.** In the project's actual 1+1D domain, Weyl vanishes identically (vacuous predicate). In 3+1D, the proposal exits the benchmark's declared claim scope with no repo capability behind it (`docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md:112`: "nothing here transfers to 3+1D", citing EGS).
  - **GATE B is unreachable.** Conditional on A surviving; with A at `NOT_AVAILABLE` on independent grounds, B must be recorded as moot, not soft-passed.
  - **Circularity flags:** step (2)'s "bandas de nivel *aproximadamente radiales*" presupposes a radial direction the order has not produced — the project's own lateral/conjugate-order route stalls at precisely this gap (`dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md:253`, "§7.4 el paso que FALTA"). Any band-width/smoothing scale chosen by inspecting behaviour at `r=2M` would violate `NO_POST_HOC_TUNING`/`NO_GROUND_TRUTH_LEAKAGE`.
  - **Not distinct from C6 at the bottleneck.** C6 changed the *generator* and still died at identity/transport across depth (`comite_decision_043_...md:348`, `GATE3_TRANSPORT = NO_CLOSED_CANONICAL_TRANSPORT_AMONG_EXAMINED_MECHANISMS`). Swapping the generator from bi-link antichains to Weyl-scalar level bands leaves step (3)–(4) needing the same unbuilt capability: canonical identification of a sheet with itself at a different depth.
  - **Ambiguity flagged, not silently resolved:** the DOSSIER's GATE A wording ("sprinkling de Schwarzschild 3+1D") may be a drafting slip for 1+1D; this brief adjudicates both readings explicitly rather than picking one silently.

### Mathematician brief

- **Computability:** On order alone the decidable primitives are: `≺` (irreflexive, transitive, acyclic — genuine partial order with large antichains), Alexandrov interval cardinalities `|I(x,y)|`, inclusive-interval abundances `N_m`, longest-chain length, comparability/incomparability of any pair, ordering fraction. All four proposed steps are *decidable*: step (1)'s BD operator `B_k` is explicitly order-only (`Benincasa_Dowker_2010_...md:104`, Eqs. 8–9). **Computability is not the binding constraint — semantics is**, and the project's frozen abstention discipline (`nachocausal/thresholds.py:122,131-132`, `τ(n)` gate) is exactly what kills Gate A quantitatively.
- **Order observable:** The only **ESTABLISHED** order-only curvature channel is BD/BDG, closed form `lim_{l_k→0} B̄_k^{(i)}φ(x) = (□ − ½R(x))φ(x)` (BD 2010 Eq. 12, `:108`; Surya LRR §4.5 titled "The Ricci scalar and the Benincasa–Dowker action"). **It recovers `R`, not Weyl, not Kretschmann.** Schwarzschild is Ricci-flat: `R≡0` everywhere in 3+1D. The established observable's continuum target is identically zero across the object the step wants to detect. Status: BD operator order-only = **ESTABLISHED**; BD → `R` = **ESTABLISHED**; BD → Weyl/`K` = **NOT_AVAILABLE**; a `K̂` satisfying Gate A(i)–(v) = **NOT_AVAILABLE** (no candidate exhibited anywhere in repo or library).
- **Relevant invariants:** ordering fraction (Myrheim 1978, Surya LRR §4.1); interval abundances `N^d_m` (Glaser–Surya, Surya LRR §4.7 Eq. 51) — Surya states plainly that interval size "will not necessarily correspond to regions in which the curvature is small"; longest chain from minimal elements (EGS interior/exterior split, `:181-191`); `|W(p,q)|` antichain-waist (already closed, `comite_decision_043`).
- **Analytic / continuum target:** The nearest thing the literature offers is the BDG action's continuum limit, giving a Ricci-scalar bulk term plus an `R_00` term plus a codim-2 joint term. Crucially, that same paper's Conclusion states the extension "**to the Weyl tensor squared order, to study the correction to the next non-null curvature order in vacuum**" is **future work** (`Continuum_Limit_BDG_Causal_Set_Action_arXiv2007.13192.md:451`). There is therefore no analytic target curve against which step (4) could be "controlled".
- **Caveats:**
  - **Gate A fails on the physics, not the computability.** `R≡0` in Schwarzschild vacuum; the established order-only curvature scalar returns `R`; Weyl order explicitly open in the primary literature.
  - **Gate A(iv) variance is quantitatively catastrophic at the very value Schwarzschild sits at.** BD 2010's own flat-space (`R=0`) simulations report `N=5000 → μ=9.35, s.d.=134.8`; `N=20000 → μ=1.12, s.d.=58.8` (`Benincasa_Dowker_2010_...md:88`). Since Schwarzschild's leading BD signal *is* the Minkowski null signal (both `R=0`), a `τ(n)`-style Minkowski-calibrated abstention gate would abstain by construction at leading order — a clean pre-data falsifier.
  - **Gate B fails order-theoretically in 3+1D, independently of Gate A.** `K=const` in Schwarzschild is `r=const`, whose orbit is `R_t × S²`. Two elements on the same `r=const` band at equal `t` but different angular position are **spacelike-separated for every `r`**, inside or outside. Hence the intra-band comparability fraction is fixed by the *ratio of the patch's timelike extent to the sphere's area* — a patch-shape quantity — not by the sign of `g^{rr}`. Recovering the signature requires quotienting by the `S²` Killing orbits; the order relation does not supply that quotient.
  - **No theorem links a region-extensive count to a pointwise gradient norm.** `||dK||²` is pointwise; intra-band comparability is an extensive statistic over a slab. Status: **PLAUSIBLE_CONJECTURE** at best, killed in 3+1D by the previous bullet.
  - **Circularity, three entry points.** (1) "bandas aproximadamente radiales" imports `r`. (2) The BD nonlocality scale `l_k` and the band half-width have no order-only principled basis; fixing either by inspecting where the statistic turns over would violate `NO_POST_HOC_TUNING`/`NO_GROUND_TRUTH_LEAKAGE`. (3) Step (4)'s calibration needs the embedding — EGS's own proof-of-principle concedes exactly this: "we **use the embedding information** to identify the origin of an appropriate ladder by simply selecting a ladder that starts very close to `r = r_S`" (`Towards black-hole horizons...md:441`).
  - **Same bottleneck as C6, reached one gate earlier.** C6's `W(p,q)` at least *existed* as a closed order-only object and died on (a) no stable codim-2 screen and (b) `GATE3_TRANSPORT = NO_CLOSED_CANONICAL_TRANSPORT_AMONG_EXAMINED_MECHANISMS`. The level-band construction is **structurally isomorphic**: "is the band at level `k₁` the same surface as the band at level `k₂`" is the transport-of-identity problem with *radius* substituted for *depth* — but it fails **earlier**, because here the generating scalar `K̂` does not even exist as an established/derivable object.
  - **Scope of the negative.** What is anchored: *the specific four-step route, built on the only established order-only curvature channel, is blocked* because that channel's continuum limit is `R`, `R≡0` in vacuum, and the Weyl-order extension is acknowledged-open in the literature. This is **not** a theorem that no order-only Weyl-sensitive observable exists (cf. `comite_decision_039`'s explicit self-limitation). A concrete, checkable reopening trigger: the Weyl-squared BDG calculation (`arXiv2007.13192` §4 future work) actually appearing in the literature.
  - **Recommendation from this seat:** terminal BLOCKED at Gate A, with Gate B recorded as an independent 3+1D order-theoretic block so it survives even if Gate A is later reopened.

### Mathematical logic brief

- **Formal status:**
  - Step (1) `\hat K` "Weyl-sensitive, survives R=0" — **CONJECTURE, and its stated motivation is false in the declared domain.** Nothing in `formal/HorizonFormal/` can even *state* it: the Lean layer is purely order-theoretic (`RelationalPast`, `RelationalBlackRegion`, `IsCover`, `RelationalHorizon` in `Horizon.lean:39-78`) with no ℝ-valued field type on `P` anywhere, no `Mathlib.Analysis`/`MeasureTheory` imports. GATE A is not "unproved in Lean"; it is **not expressible** in the current formal vocabulary. The nearest literature discipline is BDG, approximating `□ − (1/2)R` — Ricci scalar only, never Weyl.
  - Step (2) "bandas de nivel aproximadamente radiales" — **DEFINITION CONTAINING A CIRCULAR PREDICATE.**
  - Step (3) intra-class comparability — genuine **DEFINITION**, decidable, order-only, relabel-invariant (the healthiest link). But "its causal character (timelike/null/spacelike)" is a **PHYSICAL INTERPRETATION** glued onto a combinatorial statistic, not a theorem.
  - Step (4) "approximates the sign/zero of `||dK||²` in a controlled way" — **CONJECTURE** with an unstated limit regime.
  - The earliest un-discharged jump is at (1)→(2), not at (4).
  - **Dimensional type error in the premise itself (load-bearing finding).** The repo's own verified symbolic check gives, for the 1+1D patch metric `f = 1 − τ/r`, `R = −2τ/r³` (`wp4_fisher_localization_floor_symbolic_checks.py:71`, `assert sp.simplify(R_g - (-2 * tau / r**3)) == 0`). With `τ = 2M`: `R = −4M/r³ ≠ 0`. **`R = 0` is a 3+1D vacuum fact; it is false in the project's 1+1D patch.** The Weyl tensor vanishes identically in `d ≤ 3`, and in 2D the Riemann tensor is fixed by `R` alone, giving `K = R² = 16M²/r⁶` — **not** the `48M²/r⁶` quoted in the decision question (the 3+1D value). Net effect: GATE A as worded is **vacuous in-domain** ("Weyl-sensitive" selects the zero tensor) while the obstacle it was invented to defeat ("survives R=0") **does not exist in-domain**. The *target* `||dK||²` still vanishes at `r=2M` regardless (via `g^{rr}→0`), but the entire motivating vocabulary must be rewritten before it can be adjudicated.
- **Quantifier / dependency order:**
  - **`\hat K` provably cannot be order-*only*; it necessarily consumes number.** `R` is not conformally invariant (repo verifies `R[κg] = R[g]/κ`, `:72`); any 1+1D metric is conformally flat and 2D causal structure is conformally invariant, so a sprinkling's order determines at most the conformal class, never a volume-dependent quantity (`docs/bibliography_claims.md:96`). The DOSSIER header says "from causal-set *order alone*" while step (1) says "order+number" — a scope switch that must be declared explicitly (`docs/claim_grammar.md` §3).
  - **GATE B has no stated quantifier at all.** Enumerating readings: (a) ∀ pairs in the band — trivially false; (b) in expectation at fixed width `δ`, density `ρ` — measures a δ-dependent slab, not the level set; (c) a.s. as `ρ→∞` at fixed `δ` — converges to the same slab answer; (d) iterated `lim_{δ→0} lim_{ρ→∞}` — the only reading targeting the actual hypersurface, but band population `∝ ρδ → 0`. The only viable regime is a **coupled** `δ(ρ)→0` with `ρδ(ρ)→∞`, and that coupling function is an unfixed free parameter.
  - **Post-hoc degrees of freedom, in dependency order:** (i) BDG's nonlocality scale `l_k` (free "by construction" per source); (ii) band width `δ`/coupling `δ(ρ)`; (iii) band count and placement; (iv) the critical value of the "null" statistic. The **only** natural-looking criterion for setting any of them is "the crossing lands at `r=2M`" — hidden-embedding ground truth — sitting **downstream** of every other choice, the worst possible position.
- **Equivalence claims:** No iff is proved anywhere. `wp5_order_only_blindness_map_definition.md:108-115` states the converse (`signal large ⇒ order-only recoverable`) is **NOT PROVED** and requires an explicit estimator. GATE A is precisely a claim in the forbidden direction — it inherits `[NOT PROVED]` by the project's **own standing rule**, not merely "unproven yet."
- **Type / object discipline:** Three distinct types are conflated by "hoja de nivel": (1) level **set** `{K=k}` (measure-zero, has a causal character via its normal); (2) **band** `{|K−k|<δ}` (positive-measure, has **no** causal character — undefined for open sets); (3) band∩causet (finite point set, only comparability statistics). Writing "medir su carácter causal" of (2)/(3) is, as literally stated, a **category mistake**.
- **Caveats:**
  - **The C6 comparison splits.** C6's primary obstruction does **not** replicate: `W(p,q)` was indexed by an unordered pair with no canonical successor, forcing multivalued/tie-broken transport. Bands here are indexed by a **scalar level `k ∈ range(\hat K)`, canonically ordered by ℝ** — band-to-band succession is single-valued and needs no element-wise identity map. This is a genuine structural improvement over C6.
  - **But C6's actual terminal replicates exactly.** 043 §17.1 fired `C6_BLOCKED_NO_STABLE_CODIM2_SCREEN` because "`W(p,q)` exists and is an antichain, but no stable family of codim-2 screens is established." The isomorphic gap here: *`\hat K(x)` exists pointwise* (plausible, BDG-anchored) vs *a **stable, identifiable** band with causal meaning exists* (unproven, and unprovable doc-only) — the same quantifier jump the committee's own diagnosis of C6 flagged (`comite_decision_044_...md:169`).
  - **Circularity test:** HARD hit — "aproximadamente radiales" in step (2) is a selection predicate that presupposes `r`, the very thing to be located; if used to filter or accept bands it is direct ground-truth leakage. SOFT — `δ` and `l_k` are only circular if tuned against the outcome; freezing them from a principled base pre-data cures this (no such base exists today).
  - **Scoped-negative discipline.** Whatever this document concludes, it must not be written as a universal non-existence (cf. `comite_decision_039`'s self-limitation).
  - **Advisory dissent (this seat's own reading, surfaced not hidden):** A `BLOCKED` terminal is **not** yet warranted on purely logical grounds alone — unlike C6, the transport obstruction is absent and steps (2)-(3) are repairable into non-circular, decidable, relabel-invariant definitions. The proposal **cannot be adjudicated as written** (its Gate A premise is dimensionally false in-domain and its Gate B claim carries no quantifier), and the logically honest intermediate would be a **restatement demand**, not closure — unless a stability criterion and an explicit quantifier cannot be written down doc-only, in which case the C6 precedent applies and a stability-flavoured BLOCKED terminal becomes the defensible negative. *(This dissent is addressed and answered by the falsifier in §5 below — see Synthesis §8.)*

### Physicist brief

- **Coordinates & patch:** The project's frozen chart is 1+1D Schwarzschild EF `(v,r)` (`docs/preregistration.md:61-62`). **The proposal is framed in 3+1D — an unauthorised scope jump**: `K(r)=48M²/r⁶` is the 3+1D Kretschmann scalar, and no 3+1D sprinkling capability exists in this repo. Finiteness forfeits any asymptotic statement (`geometric_indeterminacy_decision.md` §11; `docs/claim_grammar.md` §3).
- **Physical meaning of the signal (and why it dissolves):** **The Page–Shoom zero is not a property of `K`.** For *any* scalar `Φ` that is a function of `r` alone in a static chart, `||dΦ||² = g^{rr}(Φ'(r))² = (1-2M/r)Φ'(r)²`, and the zero at `r=2M` comes entirely from `g^{rr}=f(r)→0` — from the *causal character of the `r=const` orbit*, not from curvature. `K`'s only role is being a monotone diffeomorphism-invariant function whose level sets *are* the `r=const` Killing orbits. Consequence: step (1) contributes **no horizon information**; step (3) (causal character of the band) carries 100% of the physics — and step (3) is the object the project has already litigated (EGS's longest-chain/height split; the C6 line). A `K`-band detector would be a **third, distinct target** (a static/Killing-structure detector), needing its own registration under `docs/claim_grammar.md` §3.
- **Sprinkling domain:** In 3+1D, `{K=const}={r=const}` is `R_t × S²`, timelike for `r>2M`, null at `r=2M`, spacelike for `r<2M`. Crucially, **a timelike hypersurface in 3+1D contains a large fraction of spacelike-separated pairs** (any pair with appreciable angular separation and small `Δt`), so intra-band comparability does **not** cleanly track causal character in 3+1D. The sharp dichotomy (timelike⇒chain, spacelike⇒antichain) holds **only in 1+1D**, where `r=const` is a curve. **Pincer: the observable is sharp only where Weyl is vacuous.**
- **GATE A verdict:** NOT_ESTABLISHED in the literature, and the premise is mis-posed for this project. BD→R confirmed (Eq. 12). The only anchor on going beyond `R` is an explicit statement that it has **not** been done (`Continuum_Limit_BDG_Causal_Set_Action_arXiv2007.13192.md:451`). A systematic grep across all of `biblioteca/derived-md/` for `weyl|kretschmann` returns only Weyl-algebra/QFT and bibliographic Hermann-Weyl hits — **no order-only Weyl/Kretschmann-sensitive operator exists in the indexed literature** (absence of establishment, not proof of impossibility). The premise is inapplicable to this project's sector anyway: Weyl vanishes identically in `d≤3` (definitionally vacuous in 1+1D); the project's 1+1D metric is **not** Ricci-flat: `R_2D=4M/r³≠0`, `K_2D=R²=16M²/r⁶` — but `R=4M/r³` is **monotone with no zero, no sign change, no feature at `r=2M`**. A radial ruler, not a horizon detector.
- **GATE B verdict:** posable non-circularly (not ground-truth leakage per se) but degenerate under Poisson. (i) the continuum object is a sharp hypersurface; the discrete object is a thickened slab of thickness `~ρ^{-1/2}`; intra-slab comparability is a joint function of thickness and density — the identical density/interval-size confound that grounded the C6 closure. (ii) Band membership is estimated from local order statistics, so band definition and the comparability statistic measured inside it are statistically dependent **by construction** — an uncontrolled selection channel. EGS's own purpose-built discrete expansion recovers only the **sign** of `Θ`, and only after averaging over sprinklings *and* over locations (`:344-347`); a per-realisation reading is claimed by nobody in the literature.
- **Teleological no-go:** CONFIRMED, no collision — the proposal targets the stationary Killing horizon at fixed `M`, not `∂J⁻(𝒥⁺)`. This is route 2 of `geometric_indeterminacy_decision.md` §11, **provided** any write-up never says "event horizon" and registers the `K`-level-set detector as a distinct fourth object alongside the three `docs/claim_grammar.md` §3 requires be kept apart.
- **Quotient `(v,r)`:** REFUTED as automatic. Generating a `K=const` band in 3+1D recovers the **set** `R_t × S²`, not the quotient to `r` alone. A causal set has no canonical action of `∂_t` or `SO(3)`; the quotient requires the isometry group supplied externally — an injection of continuum structure the project's order-only channel forbids. In the project's 1+1D EF sector the question is moot in the opposite way: the reduction to `r` is built into the chart by fiat, a property of the generator, not something the causal set recovers.
- **Caveats:**
  - Page–Shoom primary source: **NOT_AVAILABLE.** `grep -ril "shoom"` over the entire repo returns nothing. Every statement about "the Page–Shoom detector" in this deliberation is reconstructed from the decision question's own formulae, not verified against a primary text.
  - The 2D curvature computations (`R_2D=4M/r³`, `K_2D=R²=16M²/r⁶`, Weyl `≡0` for `d≤3`) are derivations from standard GR, load-bearing for the GATE A conclusion, `[UNVERIFIED]` against a local `biblioteca/` anchor (though independently re-derived by the mathematical-logic brief with matching sign convention up to a sign-only discrepancy, immaterial since `K=R²`).
  - EGS verbatim, decisive: "In the present setting, we do not have spatial two-surfaces available, because we are considering (1+1)-dimensional sprinklings... we cannot compute the expansions, but instead we consider the one-dimensional spatial distance between neighboring geodesics" (`:227-230`). Curvature invariants of the induced 2D metric are **not** the 4D ones (`48M²/r⁶` vs `16M²/r⁶`, Weyl 0 vs nonzero) — any pipeline whose signal is a curvature invariant cannot inherit EGS's 1+1D causal-structure licence.
  - Regular-black-hole caveat: `K` stays finite and becomes non-monotone in `r` for regular BHs, so a `K`-band is no longer a single radius — level sets bifurcate. `[UNVERIFIED — own reasoning]`.

## 5. Falsifier attack

- **Concrete failure modes:**
  1. **The premise is a decoy — the "Weyl-sensitive" scalar carries zero horizon information.** For ANY monotone scalar `Φ(r)` in the static chart, `||dΦ||² = g^{rr}Φ'² = (1−2M/r)Φ'²`: the zero at `r=2M` comes entirely from `g^{rr}→0`, never from `Φ`. Substituting `Φ(r)=r` (no curvature content at all) yields the identical detector. Step (1) contributes nothing; 100% of the physics sits in step (3), already-litigated (EGS longest-chain/ladders; the C6 line closed at `comite_decision_043:574`, `C6_BLOCKED_NO_STABLE_CODIM2_SCREEN`, transport block `:344-352`, upheld with label fork at `comite_decision_044:165-172`).

     > **`[CORRECCIÓN REV-A — revisión PI, alcance del test de sustitución]`** Este ítem está
     > **sobre-leído** y se corrige aquí sin borrar el texto original. Lo que la sustitución
     > `\hat K → Φ(r)=r` demuestra correctamente es que **cualquier función monótona de `r` genera
     > la misma foliación**, y por tanto que el *único* trabajo que el paso (1) tiene que entregar
     > es **un escalar intrínseco monótono en `r`** — ni más, ni menos. Eso **no** prueba que el
     > generador sea inútil ni que el paso (1) "no aporte nada": prueba que su función está
     > **exactamente identificada**, y que nadie sabe cumplirla de forma intrínseca. Además
     > `Φ(r)=r` **no es una sustitución admisible bajo el contrato `order+number`**: es un oráculo
     > extrínseco (`r` es justamente la coordenada prohibida). Un test cuyo sustituto viola el
     > contrato puede **localizar** la carencia, no **vaciar** la construcción. Conclusión corregida:
     > el test es evidencia **a favor de que el bloqueo vive en Gate A** (no existe el generador
     > intrínseco), y **no** evidencia de que los pasos (2)-(4) sean vacuos ni de que la propuesta
     > sea un renombre de C6. La reducción a C6 del último inciso de este ítem se **retira**
     > (ver §8, disagreement resuelto, y §10 `COMPARISON_TO_C6`).
  2. **The `K_2D=R²` rescue fails, three independent ways.** (a) In the project's own frozen 1+1D patch, `R=−2τ/r³` (machine-verified assert, `wp4_fisher_localization_floor_symbolic_checks.py:70`), so `K_2D=R²=16M²/r⁶` is strictly monotone with no zero, no sign change, no feature at `r=2M` — the rescue only relabels failure mode 1. (b) `R` is volume-dependent; order alone recovers at most the conformal class (`docs/bibliography_claims.md:92-100`). Step (1) silently switches to "order+number" while the dossier header says "order alone" — an undeclared scope switch. (c) The only established estimator (BD) has per-realisation sd ≫ mean even in flat space (`N=5000: μ=9.35, sd=134.8`; `N=20000: μ=1.12, sd=58.8` — `Benincasa_Dowker_2010_...md:88`). With sd/mean ~10–50×, the empirical band `{|K̂−k|<δ}` is a noise partition scattered across all radii — step (2)'s "bandas aproximadamente radiales" is empirically false before any horizon question is even posed.
  3. **The 3+1D branch is triply dead:** no 3+1D sprinkler exists (`nachocausal/generator.py:37-50` is 2-column only); no order-only Weyl operator exists in the indexed literature (`arXiv2007.13192` §4 Conclusion explicitly lists it as future work); and intra-band comparability on `R_t×S²` does not track hypersurface causal character (spacelike pairs abound on timelike `r=const` hypersurfaces). The observable is sharp only in 1+1D, where Weyl is identically zero.
  4. **Category error at step (3):** a positive-measure band has no causal character; band∩causet has only a comparability fraction, a joint function of band thickness, density, and patch aspect ratio — the same density/interval-size confound that grounded the C6 closure. No theorem links this region-extensive count to the pointwise gradient norm `||dK||²`.
  5. **The proposal claims the forbidden inference direction:** "large order signal ⇒ recoverable" is exactly what `wp5_order_only_blindness_map_definition.md:104-118` marks **NO PROBADO** by the project's own standing rule.
- **Ground-truth leakage:** Four free parameters — `l_k`, band half-width `δ`, band placement/count, and the critical value of the "null" statistic — have no order-only principled fixing. Because `K̂_2D` is monotone and featureless, no intrinsic criterion can select which band is "the null one"; the only natural calibration is "the crossing lands at `r=2M`", i.e. reading the hidden embedding. Not hypothetical: EGS's own proof-of-principle concedes it verbatim — "we use the embedding information to identify... a ladder that starts very close to `r=r_S`" (`Towards black-hole horizons...md:441`). Additionally: "aproximadamente radiales" is itself embedding vocabulary; and band membership and the intra-band comparability statistic are computed from the same order data — statistically dependent by construction, an uncontrolled selection channel.
- **Freeze violations:** The pipeline structurally invites them because nothing is pre-registrable: any pilot scan over `(l_k, δ, K*)` until a transition appears is threshold shopping; each scan burns seeds; "confirming" afterwards launders exploration into confirmation. The honest per-realisation BD output at this variance is ABSTAIN under the frozen `τ(n)` discipline — the only route to a signal is averaging over sprinklings AND locations (EGS: recovers "at best... the signs", `:342-348`); presenting that ensemble sign as per-patch localisation would be a silent re-run-until-signal pattern.
- **Verdict coercion:** (1) Gate B must be recorded as **moot** given Gate A's failure, not soft-passed as "posable". (2) A BLOCKED terminal token is not a valid `COMMITTEE_DECISION_VERDICT`; the in-body terminal must sit separate from the gate verdict, paired with `RECOMMEND_DO_NOT_PROCEED`. (3) The logician's minority ("restatement, not closure") risks reporting a terminal as INCONCLUSIVE: but the "repaired" restatement (`K_2D` bands + comparability) is, by failure mode 1, the already-closed C6/EGS object under a new name — keeping it alive as INCONCLUSIVE would reopen a closed line without the declared reopening trigger (an actual Weyl² BDG result appearing in the literature).
- **Premature / over-broad claims:** (1) "Detector de horizontes de Page–Shoom" is over-claimed twice: the primary source is absent from the repo, so every statement about it is `[UNVERIFIED]`; and the target is a stationary Killing horizon at fixed `M`, not `∂J⁻(𝒥⁺)` — calling it a "horizon detector" without registering it as a distinct 4th object per `docs/claim_grammar.md` §3 is a `TELEOLOGY_CLAIM_FAIL` waiting to happen. (2) The question quotes `K=48M²/r⁶` (3+1D) inside a benchmark whose frozen scope is 1+1D-only — an undeclared dimensional jump; the in-domain value is `16M²/r⁶`. (3) "Weyl-sensitive" in 1+1D is a predicate on the zero tensor — vacuously over-broad. (4) Any success at step (4) would still be finite-patch statistics, not metric reconstruction; the standing precedent that physically-plausible definitions can be machine-proved EMPTY (`formal/HorizonFormal/HorizonFormal/Horizon.lean:120-125`, `relationalHorizonOld_eq_empty`) forbids asserting band occupancy doc-only.
- **Independent-falsification gate:** Satisfied. Four wave-1 briefs converge on Gate A failure from independent grounds (capability `NOT_AVAILABLE`; BD→R not Weyl + variance; dimensional type error + missing quantifier; physics dissolution). No author is sole verifier of their own claim; the falsifier independently re-verified every load-bearing anchor this session. The lone dissent (logician's restatement option) is answered above under verdict coercion.
- **Minimal falsification test:** Pencil-and-paper substitution invariance (analogue of 044's total-chain counterexample): replace `K̂` everywhere in the pipeline by `Φ(r)=r`, a scalar with no curvature content whatsoever. Then `||dΦ||²=(1−2M/r)·1` has *exactly the same zero at `r=2M`*, the level bands are *the same `r=const` bands*, and steps (2)–(4) are *unchanged*. The pipeline's output is invariant under deleting its own premise — "Weyl-sensitivity" does no work, and the entire burden falls on step (3), the object already closed by C6 and already shown by EGS to require embedding information at precisely the identification step. No executable test is needed beyond this: Gate A is additionally closed on independent dimensional grounds (Weyl≡0 in 1+1D; no 3+1D capability; no Weyl operator in literature), so the terminal BLOCKED stands over-determined. Reopening trigger: an order-only Weyl²-sensitive operator actually established in the literature.

  > **`[CORRECCIÓN REV-A — revisión PI]`** El test se **conserva** como diagnóstico válido pero se
  > **reetiqueta**: no es un test de falsación de la construcción, es un **test de localización del
  > gap**. Su conclusión admisible es "el paso (1) debe entregar un escalar intrínseco monótono en
  > `r`, y no existe" (= Gate A), **no** "la Weyl-sensibilidad no hace trabajo / los pasos (2)-(4)
  > son C6 renombrado". Las razones dimensionales/de literatura que cierran Gate A son
  > independientes de este test y **se mantienen intactas**; el terminal sigue siendo BLOCKED en
  > Gate A por esas razones, no por la sustitución.

## 6. Pre-registration verdict

- **Verdict:** PASS
- **Freeze status:** All thresholds for the only frozen contract in play (prereg-002/estimator-v2) are frozen in writing prior to any validation seed being touched (`docs/preregistration_002.md:1-9,38-59`). This step touches none of it: it proposes a new candidate-generator concept for a possible future line; it does not modify, extend, or pre-empt any frozen threshold, criterion form, or gate. No prereg-003-style contract exists and none is being written here.
- **Seal integrity:** Confirmed directly this session — `sha256sum nachocausal/thresholds.py` → `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching `docs/preregistration_002.md:7-9` exactly, no drift. `git status --short` clean, HEAD `cd92f085` confirmed. The sealed path (`validate.run`) is not run, touched, or referenced by any brief.
- **Seed discipline:** No seed of any kind is drawn or consumed (`SEEDS_CONSUMED=0`). `EXPLORE_POOL` (`1_000_000..1_000_039`) and the reserved virgin validation band `[2_000_000, 2_999_999]` (`docs/preregistration_002.md:14-27`) remain untouched — this doc-only conceptual adjudication has no contact with either band.
- **Reporting rule:** `docs/preregistration_002.md:63-67` ("the outcome — PASS, FAIL, INCONCLUSIVE, or OUT_OF_DOMAIN — is recorded and reported regardless of which it is... no loosening a frozen threshold") is the binding template for the terminal this committee reaches: the wave-1/wave-2 consensus resolving to a BLOCKED terminal must be recorded plainly as a negative result on this candidate line — structurally identical to `comite_decision_043`'s `C6_BLOCKED_NO_STABLE_CODIM2_SCREEN` — not softened, not silently reclassified as INCONCLUSIVE, and not stretched into a PROCEED.
- **Forbidden moves present?** None found in the seven briefs as presented. All are explicitly read-only: grep counts, citations to already-published literature, and one citation to a symbolic assertion already committed at `b044399` (not freshly executed by any expert). No brief reports drawing a seed, running `validate.run`, building a sprinkled causet, touching `thresholds.py`, or proposing/discussing a real threshold value. No reconstruction over-claim is present. **One item flagged for vigilance downstream, not a violation now:** several briefs independently identify that the *only* non-circular criterion available to fix the proposal's free parameters (`l_k`, `δ`, band count/null-criterion) is "the crossing lands at `r=2M`" — ground truth. This is not a leakage that has occurred (no execution took place), but it is the single largest hazard flagged for any future write-up of this candidate.
- **Reasons:**
  - `docs/preregistration_002.md:1-9` — frozen scope of prereg-002; this proposal is outside it and does not touch it.
  - `docs/preregistration_002.md:14-27` — reserved virgin band; uninvolved here.
  - `docs/preregistration_002.md:63-67`, `docs/preregistration.md:55-57` — binding "report alike" rule governing this candidate's terminal.
  - `sha256sum nachocausal/thresholds.py` (run this session) = `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` — no drift.
  - `git rev-parse HEAD` = `cd92f085e7380cdd496ebeaa185c907a9ddeef3e`, clean tree.
  - `.claude/skills/comite/check_comite_brief.py` — defines the verdict/heading gate governing how §10 must be phrased.
  - `docs/comite/comite_decision_043/044/045_...md` — precedent that a doc-only, no-execution, no-threshold-touching conceptual adjudication of this shape has PASSed this procedural test before under materially identical conditions.

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| BD 2010 abstract/`:38` "approximate −½R... Ricci scalar curvature" | Reproducibility engineer | CONFIRMED — verbatim at `Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md:16,38` |
| BD 2010 Eq.(12) `lim B̄_k^(i)φ(x) = (□−½R(x))φ(x)` | Mathematician | CONFIRMED — literal eq. at `:108` |
| BD 2010 flat-space (R=0) sim variance table N=5000/10000/20000 | Mathematician | CONFIRMED (values exact: 9.35/134.8, −4.00/102.6, 1.12/58.8) but at `:88`, not `:80` as cited — minor line-number drift |
| BDG continuum-limit paper: Weyl-tensor-squared / "next non-null curvature order in vacuum" = future work | Mathematician, Physicist | CONFIRMED verbatim at `Continuum_Limit_BDG_Causal_Set_Action_arXiv2007.13192.md:451` |
| EGS "we do not have spatial two-surfaces... (1+1)-dim sprinklings... cannot compute the expansions" | Physicist | CONFIRMED at `Towards black-hole horizons and geodesic focusing in causal sets.md:227,230` |
| EGS "use the embedding information to identify... a ladder that starts very close to r=r_S" | Mathematician | CONFIRMED verbatim at same file `:441` |
| EGS discrete expansion recovers only sign of Θ after averaging over sprinklings/locations | Physicist | CONFIRMED at `:344` (range 344-347 accurate) |
| EGS longest-chain / height interior-exterior split | Mathematician | CONFIRMED at `:181,188,191` |
| Page–Shoom primary source in `biblioteca/` | Physicist | CONFIRMED absent — zero hits for "shoom" anywhere in repo or `biblioteca/` |
| K(r)=48M²/r⁶ Kretschmann formula, any primary source in `biblioteca/` | Physicist (implicit) | UNCONFIRMED — no source in `biblioteca/` states this formula; only an informal, non-authoritative note found |
| `grep -rniE "kretschmann\|weyl"` over `docs/`,`research_program/`,`dev/` → zero hits | Reproducibility engineer, Physicist | CONFIRMED — zero hits reproduced independently |
| Same grep over `biblioteca/derived-md/` → only Weyl-algebra/QFT and bibliographic Hermann-Weyl hits | Physicist | CONFIRMED — all hits are Weyl-algebra/SJ-state QFT texts or "Weyl, H." bibliography entries |
| `biblioteca/Anticadenas_Benincasa.md:6` sole informal "Kretschmann" hit, singularity-divergence context | Physicist | CONFIRMED verbatim — curvature invariants diverge at singularities, not a horizon-detection formula |
| `wp4_fisher_localization_floor_symbolic_checks.py` `R=-2τ/r³` and `R[κg]=R[g]/κ` asserted | Mathematical logic | CONFIRMED — actual asserts at `:71` and `:72`; cited as `:70` (docstring header) in one brief, off by one line, same object |
| Surya LRR §4.5 title "The Ricci scalar and the Benincasa–Dowker action" | Mathematician | CONFIRMED at `The causal set approach to quantum gravity.md:58,1482` |
| Surya LRR §4.1 ordering fraction / Myrheim 1978 | Mathematician | CONFIRMED at `:986-1010` |
| Surya LRR §4.7 eq.(51) interval abundances N^d_m; "will not necessarily correspond to regions in which curvature is small" | Mathematician | CONFIRMED — eq.(51) at `:1903`, quote verbatim at `:1870` |
| `comite_decision_043` terminal `C6_BLOCKED_NO_STABLE_CODIM2_SCREEN` | Chair (pre-verified) | CONFIRMED — at `:574`, precedence stated `:517` |
| `GATE3_TRANSPORT = NO_CLOSED_CANONICAL_TRANSPORT_AMONG_EXAMINED_MECHANISMS` | Chair (pre-verified) | CONFIRMED verbatim at `:348,547`, marked in-file as a secondary/additional block, not the primary terminal |

- **Notes:** `:80` (BD 2010 variance table) and `:70` (symbolic-check asserts) are off-by-a-few/off-by-one line citations relative to the actual location (`:88` and `:71-72`); values/content are exact matches — citation-line drift, not misrepresentation. No primary source anywhere in `biblioteca/` states `K(r)=48M²/r⁶` or discusses a "Page–Shoom" detector; the only Kretschmann mention in the entire library is the informal note used purely to illustrate curvature-divergence at singularities. Any argument resting on `K(r)=48M²/r⁶` or "Page–Shoom" as a literature-grounded object must be flagged `[UNVERIFIED]` (standard-GR fact, not sourced from the library) rather than treated as a confirmed citation. `comite_decision_044` uses a differently-named terminal (`C6_BLOCKED_NO_INTRINSIC_SCREEN_TRANSPORT`) for the pre-revision draft of the same underlying blockage discussed in 043 (043's terminal was itself revised from that name to `NO_STABLE_CODIM2_SCREEN` during the 044 review) — this is a naming-history artifact already understood from reading both documents, not a fresh citation error. All priority-citation groups checked; no citation was found to misstate its source's content.

## 8. Synthesis

**Where the panel agrees (unanimous or near-unanimous):**

- **Gate A is blocked — con los motivos separados por tipo** `[REFINADO REV-A: el borrador mezclaba
  bloqueos científicos con bloqueos prácticos y los presentaba todos como "mutually reinforcing"]`:
  - **(2) es el bloqueo científico decisivo y suficiente.** El único canal de curvatura order-only
    **ESTABLISHED** (Benincasa–Dowker) recupera demostrablemente el escalar de Ricci `R`, no Weyl ni
    Kretschmann (BD 2010 eq. 12, confirmado por el literature verifier); Schwarzschild en vacío tiene
    `R≡0` en 3+1D, luego ese canal **no distingue radios** y es ciego al blanco a orden dominante; y
    la extensión a orden Weyl² está **explícitamente declarada trabajo futuro no realizado** en la
    literatura primaria (`arXiv:2007.13192` §4 Conclusión, verbatim confirmado). Esto es una
    **ausencia de establecimiento**, no una imposibilidad demostrada — y es exactamente lo que hace
    que el paso (1) no tenga hoy ningún candidato. `NOT_AVAILABLE`, no `IMPOSSIBLE`.
  - **(1) y (3) son bloqueos de otro tipo y NO deben leerse como razones físicas de cierre**
    `[CORREGIDO REV-A — revisión PI]`. (1) *Capacidad*: no existe sprinkler 3+1D en el repo — es un
    **bloqueo práctico/de infraestructura**, no una razón física para cerrar la construcción.
    (3) *Consistencia dimensional*: en el sector 1+1D real del proyecto, "Weyl-sensitive" es vacuo
    (Weyl ≡ 0 en `d≤3`) y el `R=-2τ/r³≠0` verificado en repo es monótono sin rasgo en `r=2M`. Esto
    **impide validar en 1+1D un generador Weyl 3+1D y rompe la reutilización directa del arsenal
    1+1D del proyecto** — que es una restricción severa y real para *este* repositorio — pero **no
    refuta la propuesta 3+1D en sí**. Ambos son razones de peso para **no implementar aquí y ahora**;
    ninguno es una razón para declarar la vía físicamente cerrada.
  - **(4) el test de sustitución** queda reetiquetado como **localizador del gap**, no como prueba de
    vacuidad — ver la corrección in situ en §5.
- **Gate B: `UNRESOLVED`, no "bloqueo independiente"** `[CORREGIDO REV-A — revisión PI; el borrador
  decía "fails independently" y era una sobre-afirmación]`. Lo que los roles establecieron
  correctamente es que la imagen **"cadena fuera / anticadena dentro" es demasiado fuerte**: una
  hipersuperficie timelike en 3+1D contiene una fracción grande de pares spacelike (mathematician,
  physicist), de modo que la dicotomía nítida solo vale en 1+1D. Pero **eso no mata la estadística**:
  el discriminante continuo sobrevive en forma probabilística — una hoja exacta `r=const` **interior**
  es spacelike y por tanto tiene `p_comp = 0` **idénticamente** (ningún par causal dentro de ella),
  mientras que la exterior (timelike) tiene `p_comp > 0`. El criterio `p_comp > 0` fuera vs
  `p_comp = 0` dentro **no queda refutado por el argumento de las órbitas de Killing**.
  El problema real de Gate B es **cuantitativo y de resolución finita**, y está **sin resolver**, no
  refutado: (i) con bandas de grosor finito `δ` aparecen pares comparables **también dentro**
  (contaminación de la banda), y (ii) la fracción comparable exterior **tiende continuamente a cero**
  al acercarse a `r→2M`, de modo que el cero verdadero compite con "un valor pequeño" — el problema
  de identificabilidad estadística que la pregunta de decisión ya anticipaba. Decidir si eso es
  estadísticamente distinguible **exige una derivación de `p_band(r; δ, patch, ρ)`**; no se deduce de
  que la hoja exterior no sea una cadena. Se mantienen como reales, pero **subordinadas a esa
  derivación pendiente**, la observación de tipo/categoría (una banda de medida positiva no tiene
  "carácter causal", solo un estadístico — mathematical logic) y los confounds de grosor/densidad
  (physicist, falsifier). **Etiqueta:** `UNRESOLVED_FINITE_BAND_IDENTIFIABILITY`.
- **Relación con C6: parentesco estructural, NO identidad** `[CORREGIDO REV-A — el borrador afirmaba
  que cualquier versión reparada "colapsa sobre el objeto ya cerrado"; esa reducción se **retira**]`.
  C6 (`comite_decision_043`/`044`) cerró un objeto **distinto** (la cintura de bi-enlaces `W(p,q)` y
  su **transporte** entre profundidades). El generador aquí es una **mejora estructural genuina**
  sobre C6: un nivel escalar está canónicamente ordenado por ℝ, a diferencia de un par no ordenado,
  de modo que la sucesión banda-a-banda es univaluada y **no necesita** el mapa de identidad
  elemento-a-elemento que mató a C6 (mathematical logic brief). Lo que **sí** comparten —y esto es el
  hallazgo profundo de esta sesión, más informativo que el terminal mismo— es el **cuello de botella
  común**: ambos necesitan una **partición/foliación intrínseca canónica** del causet, y ese es
  exactamente el objeto que C4 (grafo de vecinos), C5 (peel lateral) y C6 (pantalla + transporte) no
  lograron construir, cada uno por su vía. **Page–Shoom no falla por razones de curvatura: falla
  porque necesita una foliación intrínseca, y la foliación intrínseca es el problema abierto
  permanente de este programa.** El ángulo Weyl/Kretschmann resulta ser un arenque rojo en **ambas
  direcciones** — ni era la esperanza (la firma causal, paso 3, es lo que el orden sí sabe leer
  nativamente), ni es la refutación (el bloqueo no es curvatura, es foliación).
- **Teleology and the `(v,r)` quotient are correctly out of the way of the negative, not causes of it.** The proposal does not collide with the teleological no-go (it targets a stationary Killing horizon, not the global event horizon — physicist), but it also does **not** automatically recover the reduction to `r`: a `K=const` band in 3+1D retains the full `R_t×S²` orbit, and quotienting by the Killing/rotation group is an externally-supplied structure the causal order does not provide (physicist). This is a further, independent reason Gate B cannot be closed as stated, not a saving grace.
- **Discipline is clean.** Warden PASS: no execution, no seeds, no threshold touched, no reconstruction over-claim; seal re-verified independently by three separate roles with no drift. Literature verifier confirms essentially every load-bearing citation (with only immaterial line-number drift), and independently confirms the negative findings: no Weyl/Kretschmann operator anywhere in the repo's own code/docs, and no Page–Shoom or `K=48M²/r⁶` primary source anywhere in `biblioteca/` (an absence, correctly not converted into a proof of impossibility by any role).

**Open disagreement (surfaced, not hidden):**

- **The mathematical-logic brief's minority position.** That brief argued a `BLOCKED` terminal is "not yet warranted on purely logical grounds alone" — unlike C6, the transport obstruction is structurally absent here (bands are canonically ℝ-ordered), and steps (2)-(3) are, in principle, repairable into non-circular, decidable, relabel-invariant definitions. It recommended a **restatement demand** (rewrite the target in 1+1D-correct terms, declare the order-alone→order+number scope switch, give Gate B an explicit quantifier, name a stability criterion) rather than immediate closure, reserving BLOCKED only if that restatement proves impossible to write down doc-only.
- **The falsifier's rebuttal, accepted by the chair.** The falsifier directly engaged this dissent and showed that the best-faith restatement the logician's brief itself proposes (`K_2D` bands + intra-band comparability, in the project's real 1+1D sector) is, by the substitution-invariance test, *exactly* the already-closed C6/EGS object under a new name: `K_2D=R²` is a monotone reparametrisation of `R`, itself a monotone reparametrisation of `r`, so a `K_2D`-band is just an `r=const` band with extra algebra in front of it, and its causal-character question is the identical one C6 closed. No restatement of *this specific pipeline* escapes that reduction, because the reduction does not depend on which monotone function of `r` seeds step (1) — it depends only on step (3)'s already-adjudicated object. The chair adopts the falsifier's reading: the restatement is not a way to keep the line open, it is a proof that the line was never doing independent work. This does not contradict the logician's technical findings (the type-error and missing-quantifier diagnoses are correct and are incorporated into the terminal's reasoning below); it resolves the *disposition* question the logician left open.
- **Resolution:** given (a) Gate A fails on capability, established-literature, and in-domain-dimensional grounds simultaneously, (b) Gate B fails independently on Killing-orbit and density-confound grounds, and (c) the falsifier's substitution test shows no restatement of this construction escapes the already-closed C6 object, the chair finds the disagreement resolved *within this document* — no second reconvene is needed, unlike the C6 043→044 sequence, because the rebuttal to the sole dissent is already assembled and unanimous once stated.

## 9. Next-step spec

This is a doc-only conceptual adjudication. There is no committing step, no execution, no seeds — nothing here touches the sealed path. All items below describe what a future line would need, **not** an authorization to pursue it.

**No implementation, no synthetic contract, no seeds, no freeze, no `CANDIDATE` opening is proposed or authorised by this document.**

- **Reversible (informational only, no user action required):** none — this document itself is the complete reversible artefact of this session.
- **Committing (only on explicit user authorisation, and only if the reopening trigger below is met):** none proposed. If the user wishes to keep a narrow door open for a *future* reconsideration, the only defensible reopening trigger, per the mathematician and falsifier briefs, is: **an order-only Weyl²-sensitive (or higher-curvature-invariant-sensitive) operator with a proven, non-degenerate continuum limit actually appearing in the peer-reviewed causal-set literature** (the extension `arXiv:2007.13192` §4 explicitly flags as unfinished future work). Absent that, this specific four-step construction should not be revisited under a new name.
- **Falsifier's minimal test, already discharged (no execution needed):** the substitution-invariance argument (`\hat K → Φ(r)=r` leaves the pipeline unchanged) is a pencil-and-paper proof, included verbatim in §5, that requires no seeds and can be cited directly in any future candidate-matrix update.
- **Documentation housekeeping (optional, at the user's discretion, not authorised by this document alone):** `research_program/work_packages/next_observable_candidate_matrix.md` could record this adjudication as a closed line (analogous to how C6 is referenced there), so a future session does not re-propose the same construction under a different name without checking this decision first.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_DO_NOT_PROCEED

**In-body terminal (not itself the `COMMITTEE_DECISION_VERDICT` token — separate field, per the precedent of `comite_decision_043:574`):**

```text
WEYL_LEVEL_SHEET_TERMINAL = BLOCKED_NO_INTRINSIC_WEYL_SENSITIVE_LEVEL_SET_GENERATOR
                            # alcance: NO_IMPLEMENTAR con el repertorio actual.
                            # NO es un cierre conceptual de Page-Shoom. Ver SCOPE_OF_NEGATIVE.

GATE_A = BLOCKED (decisivo y suficiente por si solo).
   Razon cientifica: no existe hoy ningun observable order+number ESTABLISHED ni DERIVED_HERE que
   sea genuinamente sensible a Weyl y sobreviva a R=0. El unico canal de curvatura order-only
   establecido (BD/BDG) recupera el escalar de Ricci R; R=0 en vacio Schwarzschild 3+1D, luego ese
   canal no distingue radios; y la extension a orden Weyl^2 esta declarada explicitamente como
   trabajo futuro NO realizado en la literatura primaria (arXiv:2007.13192 §4). Estado = NOT_AVAILABLE,
   NO = IMPOSSIBLE.
   Razones adicionales, de tipo distinto, que NO se cuentan como cierre fisico:
     - PRACTICA: no existe sprinkler 3+1D en el repo (bloqueo de infraestructura).
     - DIMENSIONAL: en el sector 1+1D del proyecto Weyl es identicamente 0 y R=-2tau/r^3 es monotono
       sin rasgo en r=2M. Esto impide VALIDAR aqui un generador Weyl 3+1D y rompe la reutilizacion
       del arsenal 1+1D; no refuta la propuesta 3+1D en si.

GATE_B = UNRESOLVED_FINITE_BAND_IDENTIFIABILITY        # [REV-A] antes: "bloqueo independiente".
   No refutado. El discriminante continuo SOBREVIVE en forma probabilistica: una hoja exacta
   r=const interior es spacelike => p_comp = 0 identicamente; la exterior es timelike => p_comp > 0.
   El argumento de las orbitas de Killing refuta la imagen fuerte "cadena vs anticadena", NO el
   criterio p_comp>0 / p_comp=0.
   Lo que queda ABIERTO y exige derivacion, no asercion: con grosor de banda finito delta aparecen
   pares comparables tambien DENTRO (contaminacion), mientras la fraccion exterior tiende
   CONTINUAMENTE a cero cuando r->2M; el cero verdadero compite con "un valor pequeno". Decidirlo
   exige calcular p_band(r; delta, patch, rho). Subordinadas a esa derivacion: el desajuste de
   categoria banda-vs-hoja y los confounds grosor/densidad.

COMPARISON_TO_C6 = SHARED_BOTTLENECK_NOT_IDENTITY      # [REV-A] reduccion a C6 RETIRADA.
   El generador es una MEJORA estructural real sobre C6 (niveles escalares canonicamente ordenados
   por R vs. par no ordenado => sucesion banda-a-banda univaluada, sin necesidad del mapa de
   identidad que mato a C6). Lo compartido es el cuello de botella de fondo: ambos requieren una
   FOLIACION/PARTICION INTRINSECA CANONICA, el mismo objeto que C4, C5 y C6 no lograron construir.
   HALLAZGO DE FONDO: Page-Shoom no falla por curvatura, falla por foliacion. El angulo
   Weyl/Kretschmann es un arenque rojo en ambas direcciones.

TELEOLOGY = NO_COLLISION — apunta a horizonte de Killing estacionario, no al horizonte de sucesos.
QUOTIENT_v_r = NOT_AUTOMATIC — una banda K=const retiene la orbita R_t x S^2; el cociente a r exige
   un grupo de isometrias suministrado externamente, prohibido al canal order-only.

SCOPE_OF_NEGATIVE = NOT_A_UNIVERSAL_THEOREM / NOT_A_PROOF_OF_INDISCRETIZABILITY
   Este documento NO demuestra que el detector de Page-Shoom sea indiscretizable. Demuestra que el
   repositorio, y la literatura causal-set establecida a fecha de hoy, NO poseen el ingrediente
   necesario (un generador de hojas intrinseco y Weyl-sensitive) para discretizarlo de forma
   intrinseca. La distincion es vinculante y ninguna cita futura de este terminal puede colapsarla.

REOPENING_TRIGGER = un operador order-only sensible a Weyl^2 (o a un invariante de curvatura
   superior) con limite continuo probado y no degenerado, aparecido en literatura revisada por pares.
CANDIDATE_OPENED = NONE
C1_C6_LOCALIZER_LINE = STILL_CLOSED_NOT_REOPENED
```

## 11. User sign-off

**2026-07-28 — revisión del PI sobre el borrador (input literal del usuario, registrado como hecho
de sesión, no como firma formal):**

- **Conforme con detener la implementación** ("Estoy de acuerdo con detener la implementación").
- **Gate A se conserva como bloqueo decisivo y suficiente**; el terminal
  `BLOCKED_NO_INTRINSIC_WEYL_SENSITIVE_LEVEL_SET_GENERATOR` se considera correcto.
- **Dos sobre-afirmaciones señaladas y exigidas corregir antes de firmar** (aplicadas como REV-A):
  1. el test de sustitución `Φ(r)=r` estaba sobre-leído — cualquier función monótona de `r` genera
     las mismas hojas, luego el test identifica la *función* del generador, no su inutilidad; y `r`
     es una entrada extrínseca, no una sustitución permitida por el contrato;
  2. Gate B **no** falla de forma independiente por el argumento de órbitas de Killing — el criterio
     `p_comp>0` fuera / `p_comp=0` dentro sobrevive en el continuo; el problema real es de
     **resolución finita** y exige derivación → `UNRESOLVED_FINITE_BAND_IDENTIFIABILITY`.
- **Lectura vinculante del alcance** fijada por el PI: *"el comité no ha demostrado que Page–Shoom
  sea indiscretizable, sino que el repositorio no posee actualmente el ingrediente necesario para
  discretizarlo de forma intrínseca"* — recogida literalmente en `SCOPE_OF_NEGATIVE` (§10).
- **Condición declarada para integrar en la matriz de candidatos:** aplicar primero esas dos
  correcciones. Aplicadas en REV-A; la integración en
  `research_program/work_packages/next_observable_candidate_matrix.md` **no** se ha ejecutado en esta
  sesión y sigue requiriendo autorización explícita.

**FIRMA FORMAL — 2026-07-28, PI (adnacho@gmail.com).** Ratificada la recomendación estratégica del
chair:

- **La línea de localizadores/detectores intrínsecos queda CERRADA de forma permanente.** C1–C6 más
  esta adjudicación suman siete ataques independientes bloqueados por el **mismo** obstáculo: la
  ausencia de una foliación/partición intrínseca canónica. No se abre `C7` ni ninguna variante
  renombrada de las vías cerradas.
- **El programa pivota a consolidación/publicación** de lo ya probado: prereg-002 recoverability
  PASS; prereg-003 suelo operacional O(ℓ); WP4 teorema de dos puntos; Teorema A (ceguera exacta,
  `TV=0`); suelo Fisher `O(1/sqrt(n·Ībar))` con `κ=V·I` invariante bajo dilatación; candidato 7.1
  separación asintótica `fixed_n` (no efectiva).
- **Tesis del trabajo de consolidación:** *el orden RECUERDA el horizonte pero no lo DEFINE.*
- **Integración en la matriz de candidatos:** AUTORIZADA y ejecutada (`next_observable_candidate_matrix.md`
  §8, commit `e954fe2`), cerrando cero candidatos de §2 y sin autorizar nada.
- **Trigger de reapertura:** el único registrado en §10. Condición externa, no tarea pendiente.
- **Gate previo al envío:** el Paso D de `wp5_order_only_blindness_map_definition.md` §5 (revisión
  bibliográfica independiente) sigue siendo condición de bloqueo para **cualquier claim público de
  novedad**, y debe descargarse antes de someter nada.

`STATUS_046 = SIGNED_AND_CLOSED`
