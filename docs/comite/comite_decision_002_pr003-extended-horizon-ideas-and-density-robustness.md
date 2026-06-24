# Comité Decision 002 — PR-003: ideas para un objeto de horizonte extendido y robustez a densidad

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question
En la frontera de PR-003, tras `BARE_RELOCALISATION`, la Fase #1 dio: expansion-horizon **PARCIAL**
(reproduce el cambio de signo de Θ_out de EGS en R_S a intensidad 3600, pero degrada / no converge a
7200, interior submuestreado), e iterative-reseed v0 **POSITIVO preliminar** (96→146 frentes/semilla,
d⊥ 0.52→0.63 ℓ, conexo 90→95 %, Guard-v 6/6, control MINK pasa, pero `covers` R_S cae 74→65 % y solo
2 densidades). El usuario no sabe qué camino tomar y pide: **(1)** ¿hay alguna OTRA idea/ángulo
order-only, NO en la cascada #1/#2/#3, que pueda reconstruir un objeto de horizonte **extendido**?, y/o
**(2)** ¿hay algún paper (arXiv o biblioteca) que ayude a hacer la señal interior de expansión
robusta a densidad, o a definir una regla de parada order-only? Quiere ideas concretas y una
recomendación de camino, con la disciplina dev/validación y el sello `6e2c3888…` intactos.

## 2. Verified state
Hechos comprobados **esta sesión**, cada uno con su comando / file:line.

- **Sello intacto:** `make verify-seal` → `nachocausal/thresholds.py` sha256 =
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, coincide con
  `docs/preregistration_002.md` (líneas del bloque **Seal**). `RESPECT_SEAL_FREEZE` ✓.
- **Git:** HEAD `32697c2`; working tree limpio salvo `cpp/` sin trackear (binario de la rama
  `formula` de otro agente, **fuera de alcance**, verificado por el chair).
- **prereg-002 `PASS`** (localización order-only del borde asociado al horizonte en parche finito
  1+1D, a ciegas).
- **Disciplina de semillas:** todas las mediciones Fase #1 usan `EXPLORE_POOL` (`dev/explore_seeds.py`);
  la banda `RESERVED_002 [2_000_000, 2_999_999]` sigue **virgen**.
- **Naturaleza de la pregunta:** se pide recomendar un **siguiente paso dev** (exploratorio,
  reversible), **no** una corrida de validación committing. Por eso NO se ejecutó `/auditor` previo:
  no hay PROCEED propuesto sobre un número publicado/congelado; los resultados Fase #1 son dev/v0
  explícitamente no congelados / no validados / no auditados.

## 3. Dossier
Ficheros y referencias suministrados al comité:
- `docs/hoja_de_ruta_24_jun_2026.md` — cascada #1/#2/#3 y disciplina.
- `docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md` — decisión previa.
- `dev/measure_truncated_head.py` + `dev/PR003_NEAR_HORIZON_NOTES.md` — `BARE_RELOCALISATION`.
- `dev/measure_expansion_horizon.py` + `dev/PR003_EXPANSION_NOTES.md` — Fase #1-B (EGS Eq.14), PARCIAL.
- `dev/measure_iterative_reseed.py` + `dev/PR003_ITERATIVE_RESEED_NOTES.md` — v0, POSITIVO preliminar.
- `docs/preregistration.md`, `docs/preregistration_001_addendum.md`, `docs/preregistration_002.md`,
  `docs/estimator_v2_seal.md` / `_freeze.md`, `docs/pr003_leakage_gate.md`.
- `nachocausal/thresholds.py` (SELLADO), `Makefile` (`verify-seal`/`dry-run`/`test`), `CLAUDE.md`.
- `biblioteca/` — EGS arXiv:2605.06813; `biblioteca/derived-md/`; `biblioteca/Anticadenas_Benincasa.md`;
  Benincasa–Dowker 2010 (BD2010); tesis de Benincasa.

## 4. Expert briefs (wave 1 — blind, parallel)
### Reproducibility engineer brief
- **Proposed artefact(s):** `dev/measure_iterative_reseed_v1.py` (endurecer el v0 en
  `dev/measure_iterative_reseed.py:1`) + notas `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md`. **Sin cambio**
  bajo `nachocausal/` — reusa el localizador v2 sellado sin tocar (`two_means_split` + `gate.abstains`
  + `tau(n)`, como en `measure_iterative_reseed.py:62-65`). El avance v1 es solo en agregación
  dev-side: (i) **3ª densidad** (14400, ya cableada como `--full`) para el criterio (d) de
  convergencia; (ii) **regla de parada/abstención order-only** para frentes no-cubrientes, solo de
  cantidades derivadas de `C`, con `r` revelada SOLO en `score_locus` (`measure_iterative_reseed.py:111`).
- **Environment & seal:** numpy 1.26.4 (`thresholds.PINNED_NUMPY`); re-verificar el sello **antes y
  después** con `make verify-seal` = `6e2c3888…`. Package-diff-clean: `git status` solo dev/ + el
  `cpp/` preexistente; sin editar `thresholds.py`/`gate.py`/`estimator.py`/`validate.py`. El clon Minz
  externo NO hace falta (imports solo `nachocausal.{estimator,gate,generator,thresholds}`, puro numpy).
- **Provenance capture:** imprimir a stdout git HEAD (`32697c2`), SHA del sello, `numpy.__version__`,
  `uname -a`, lista de semillas `EXPLORE_POOL[:6]` con aserción de que ninguna entra en
  `[2_000_000, 2_999_999]` (reusar `explore_seeds.in_reserved_002`), timestamp UTC. Solo log dev.
- **Run mechanics:** invocación única `python dev/measure_iterative_reseed_v1.py --full`
  (6 semillas × {3600,7200,14400}). **Pre-flight totalmente reversible** — lee nubes EXPLORE_POOL,
  computa loci order-only, revela `r` solo para puntuar, NO escribe nada en el repo ni en estado
  sellado; abortar deja el árbol limpio. **NO es paso committing**: no llama `validate.run()` en
  semillas default/reserved, no dibuja RESERVED_002, no cambia umbrales. 14400 ~cuadruplica N; si tarda,
  background con stdout.
- **Reproducibility risks / ambiguities:**
  - La **nueva regla de parada** es el único sitio donde podría entrar fuga: DEBE ser función del
    O-multiset / `L_past` derivado de `C`, nunca de `r` ni de `covers` (puntuado en
    `measure_iterative_reseed.py:115`). Si se ajustara para *mejorar* `covers`, sería
    `NO_GROUND_TRUTH_LEAKAGE` / `NO_POST_HOC_TUNING`. La Guard-v relabel debe seguir 6/6.
    `[UNVERIFIED — spec; la regla no está escrita]`
  - 14400 es el test de convergencia; `expansion` ya falló convergencia a 7200, así que un v1 que
    degrade a 14400 es un NEGATIVO legítimo, no licencia para bajar la densidad. Pre-comprometer que
    14400 se reporta pase lo que pase.
  - Runtime/memoria a 14400 sin medir `[UNVERIFIED]`; `past_matrix_fast` construye `C` densa N×N
    (`measure_iterative_reseed.py:147`) — confirmar que cabe antes de un background largo.
  - "connected" es la noción débil documentada (cualquier enlace causal, no through-chain); v1 no
    debe redefinirla para inflar la métrica.
  - Hazard de alcance: el binario `cpp/` de la rama "formula" es de otro agente; v1 no debe importarlo.

### Mathematician brief
- **Computability:** todo lo propuesto es decidible solo sobre `≺` (orden parcial estricto;
  Anticadenas_Benincasa.md §2.1; BD2010 md:40). Primitivas ya en código: `O(i)=|future(i)|` (v2
  sellado), `L_past` (tiempo discreto order-only cuyos level-sets son anticadenas genuinas), intervalo
  inclusivo `I(x,y)` y `|I(x,y)|` (BD2010 md:40). Las puertas de abstención/dominio siguen siendo el
  guard de parcialidad correcto: `τ(n)` abstiene (gate.py:9-11,53-57) y `T_EDGE_MIN=6 ⇒ OUT_OF_DOMAIN`
  (thresholds.py:37). Todo campo nuevo DEBE heredar ambas puertas por elemento/frente — un valor de
  operador BD o conteo de moléculas en un vecindario sub-cardinalidad es **indefinido, no cero**, y
  debe abstener. Ninguna propuesta requiere `r` para construir; `r` solo puntúa.
- **Order observable:** tres construcciones de horizonte extendido NO en la cascada, order-only:
  1. **Campo escalar de curvatura Benincasa–Dowker 2D.** `Bφ(x) = (2/l²)[ -2φ(x) + Σ_{L1}c₁ -
     Σ_{L2}c₂ + Σ_{L3}c₃ ]`, `Lₖ(x)={y≺x : |I(x,y)|-2 = k-1}` capas pasadas order-definidas. `φ≡-2`
     da un estimador por-elemento de `-2R(x)`. Objeto extendido (campo escalar intrínseco sobre todo
     el parche), no un trazador que se pela. Caveat: estima curvatura, NO la superficie nula.
  2. **Antichain = hipersuperficie espacial.** Una anticadena `A` (Anticadenas §3.1) es la rebanada
     espacial order-only; la estructura de distancia espacial *dentro de UNA anticadena maximal que
     cruza el parche* da, por rebanada, el split interior/exterior a lo largo de toda la rebanada a la
     vez. Ángulo genuinamente distinto del re-sembrado por niveles de `L_past`.
  3. **Acción BD localizada como término de frontera/molécula (SMI de Sorkin).**
     `S^{(2)}[C]/ℏ = N − 2N₁ + 4N₂ − 2N₃` (BD2010 Eq.13), `Nᵢ` = nº de intervalos inclusivos de
     (i+1) elementos. La tesis de Benincasa: la parte de **frontera** ∝ área codim-2 de una partición
     definida por horizonte (md:56,960,1015,1499-1545: horizonte causal ≡ `{P(γ),P̄(γ)}`; SMI ∝ área).
     Locus de "moléculas de frontera" = objeto extendido order-only directo.
- **Relevant invariants:** ordering fraction / dim. Myrheim–Meyer (Anticadenas §2.2); altura
  `L_past`; future-volume `O(i)` (v2 sellado); `|I(x,y)|` y abundancias de intervalos pequeños
  `C_k ≡ N_k` (BD2010 md:123); operador BD `B` (BD2010 Eq.2); acción `N−2N₁+4N₂−2N₃` (BD2010 Eq.13).
- **Analytic / continuum target:** campo BD → `(□ − ½R)φ` (BD2010 Eq.12); campo de antichain →
  `Θ_out(r)=(1/r)(1−2M/r)`, cero en 2M (EGS Eq.12); término de frontera BD → SMI ∝ área de horizonte
  codim-2 (tesis md:1015,1545).
- **Caveats:**
  - **El vacío 1+1D suprime la señal de Ricci.** La métrica EGS es un *embedding* 1+1D, no Schwarzschild
    4D; `R` puede ser pequeño/degenerado donde vive el focusing → el ángulo 1 puede llevar la señal en
    fluctuaciones de la parte-`□`, no en `R` limpio. `[UNVERIFIED]` si el campo BD separa interior/
    exterior en el toy EGS — requiere medición dev.
  - **Las fluctuaciones BD crecen con N a IR fijo** salvo suavizado a escala intermedia `l_k` (BD2010
    md:75-88). Es **el mismo problema de robustez a densidad** del 7200, y el fix publicado (suavizado
    `l_k`, amortiguación por ley de grandes números) es la respuesta de literatura a la pregunta (2).
    Un `l_k` congelado (elegido en EXPLORE_POOL, sellado antes de validación) es la vía disciplinada.
  - **Regla de parada order-only:** la puerta `τ(n)` (gate.py:53-57) YA ES una regla de parada
    order-only principiada y debería gobernar cualquier campo BD/molécula por frente — abstener donde
    la cardinalidad local `n` es muy pequeña. Aborda directamente el `covers` 74→65 %: los frentes
    no-cubrientes son mayormente sub-cardinalidad y deberían **abstener, no localizar**. `[UNVERIFIED]`.
  - Coste: `C_k`/moléculas es `O(N²)–O(N³)`; las capas BD solo necesitan `L₁..L₃`, tratable por elemento.
  - **El límite de honestidad vale para los tres:** cada uno da un objeto extendido order-only
    *localizado en el parche finito*, NO reconstrucción métrica, NO horizonte asintótico/Killing, NO
    3+1D. El "área" del ángulo 3 debe quedarse en recuperabilidad, no entropía.
- **Recomendación (orden-teórica):** la vía order-teóricamente más limpia y robusta a densidad es el
  **campo de frontera/molécula de la acción BD (ángulo 3) con suavizado `l_k` (BD2010 md:79-88)**,
  porque reusa conteos de intervalos pequeños ya decidibles, apunta a un objeto *extendido* genuino, y
  tiene benchmark continuo (SMI ∝ área). Continuar iterative-reseed v0 como baseline empírico líder,
  pero medir el campo BD en EXPLORE_POOL antes de comprometer, y congelar `l_k` + la regla `τ(n)` antes
  de tocar RESERVED_002.

### Physicist brief
- **Coordinates & patch:** mantener las coords ingoing Eddington–Finkelstein `(t*,r)` de EGS (md:139,
  Eq.6: `t* = t + 2M ln|(r−2M)/2M|`), métrica `ds² = −f dt² + f⁻¹ dr²`, `f=1−r_S/r` (md:131, Eq.5).
  Son la elección correcta porque el determinante inducido es constante → densidad de sprinkling
  uniforme (sin gradiente espurio interior/exterior) y las geodésicas nulas son analíticas (md:139,
  Eq.7), la única info que usa el sprinkling. La finitud **prohíbe el horizonte de eventos** (EGS:
  requiere sprinkling infinito, md:175; puntos sin futuro cerca de r=0 indistinguibles de J⁺, md:175-179)
  → ninguna afirmación global/asintótica es admisible. Sobre mitigar la submuestra interior por
  patch/coord: **sí, parcialmente** — las figuras de EGS usan caja con razón temporal/espacial grande,
  **t\*/r_S ∈ [0,50], r/r_S ∈ [0,2]** (md:450), y dicen que el contraste interior/exterior y la
  bimodalidad de longest-chain "se vuelven aún más pronunciados al aumentar la extensión temporal del
  sprinkling" (md:188-191, md:390). Los runs dev usan **t_edge=6** (notes:17), extensión temporal
  ~8× menor que la 50 de EGS; la **caja alta** es una palanca de coord/dominio **neutral al umbral
  congelado** (cambia la región, no el localizador ni ningún umbral).
- **Physical meaning of the signal:** (i) *split longest-chain / future-cardinality* (iterative-reseed
  vía `L_past` y `O=|future|`): curvas interiores llegan a r=0 en tiempo propio finito (futuros
  truncados por la singularidad) → cadenas interiores cortas, exteriores largas → split **bimodal** en
  r_S (md:181-193); firma de incompletitud geodésica, objeto intrínsecamente *marginal*. (ii)
  *expansión discreta E* (md:276-287, Eq.14): el observable de **horizonte aparente** genuino, contrapartida
  de `Θ_out=(1/r)(1−2M/r)` (md:225, Eq.12), + fuera, − dentro, 0 en r_S. El PARCIAL a 7200 (la
  negatividad interior desaparece) NO es coincidencia: es **la misma física de truncación** — las
  escaleras outgoing interiores se quedan sin futuro antes de acumular rungs. EGS definen el borde
  recuperable como el **horizonte aparente** (Θ_out=0, MOTS), que en Schwarzschild *coincide* con el
  de eventos (md:225) — pero solo se explota la coincidencia; se detecta el aparente, nunca el de
  eventos. El "peeling" del trazador único (BARE_RELOCALISATION, md:443,474) es por qué un objeto
  extendido no sale de una geodésica y hay que ensamblarlo a trozos.
- **Sprinkling domain:** Poisson `ρ=ℓ⁻ᵈ` (md:117, Eq.4) en el parche finito `(t*,r)`; única entrada
  son las geodésicas nulas analíticas (md:148). Intensidades probadas 3600/7200 (ℓ=0.0447/0.0316);
  iterative-reseed tiene una 3ª densidad (14400) **no corrida aún** (notes:51). ¿Submuestra interior
  intrínseca o artefacto? **Mixto, y la distinción es el quid.** Es *físicamente real* que los futuros
  outgoing interiores se truncan (techo inamovible a patch fijo). Pero la *severidad* en estos runs es
  mayormente **artefacto de dominio**: t_edge=6 es ~8× más corto que la caja t\*/r_S∈[0,50] de EGS
  (md:450), diseñada para que el diagnóstico longest-chain "funcione bien" (md:450) y el contraste se
  afile con la extensión temporal (md:188-191). Lectura honesta: **una caja más alta (mayor t\* a
  r∈[0,2r_S] fijo) es el fix de mayor palanca y avalado por literatura**, distinto de subir ρ (que
  encoge ℓ y, por el resultado dev, *empeora* la variante de expansión al adelgazar las escaleras
  interiores, notes:24-26). Subir densidad solo es la palanca equivocada; alargar el dominio temporal
  futuro es la correcta.
- **Claim boundary:** un veredicto reclama **localización order-only del borde asociado al horizonte
  en un parche finito 1+1D** — nada más. NO: reconstrucción métrica; horizonte de **eventos**/asintótico
  (necesita sprinkling infinito, md:175); 3+1D (md:~495, futuro). Lo recuperable es el **horizonte
  aparente** (Θ_out=0, MOTS, md:213-225), igual al de eventos *solo porque* Schwarzschild es estático
  (md:225) — para un agujero dependiente del tiempo o regular esa coincidencia se rompe. Caveat de
  agujero regular (md:201,463-470): el split por longest-chain es **inaplicable** a agujeros
  geodésicamente completos (Hayward); solo sobrevive la expansión (md:472). Cualquier afirmación que
  se apoye en la bimodalidad de cadenas es implícitamente una afirmación de Schwarzschild *singular*.
- **Caveats:**
  - La variante de expansión es el diagnóstico más defendible físicamente (es el observable de
    horizonte aparente real, Θ_out, md:225) pero falla convergencia a 7200 (notes:36-45) — y EGS
    marcan exactamente este inconveniente: el método de escaleras/expansión "requiere numerosos
    sprinklings para converger, porque el número de escaleras no es suficientemente denso en un
    sprinkling dado" (md:472). La robustez a densidad es **problema abierto conocido en el paper
    fuente**, no defecto del proyecto.
  - La submuestra interior a t_edge=6 está plausiblemente dominada por extensión temporal insuficiente
    (EGS afilan el contraste solo a t\*/r_S∈[0,50], md:450,188-191). `[UNVERIFIED]` si re-correr en
    caja alta restaura la negatividad interior — es cambio de dominio, no de umbral, pero no medido.
  - El proxy order-only `sep(u,v)=√|menor diamante|` es v0 para la distancia EGS (notes:14,51); EGS
    avisan del "silencio asintótico" a separación espacial pequeña (md:441) — el interior del proxy no
    está validado.
  - El `covers R_S` cayendo 74→65 % (notes:48-50) significa que un tercio de frentes localizan *fuera*
    de r_S; consistente con la misma física de inanición interior sesgando frentes hacia dentro — la
    vía iterativa **hereda, no escapa** el problema de truncación.
  - Ningún discriminador ingoing/outgoing intrínseco; EGS usaron embedding y citan los *cruces* de
    escaleras como alternativa intrínseca (rara estadísticamente). El `relphi` dev es no fiable
    (notes:53). Cualquier afirmación "solo outgoing" no está hoy bien fundada order-only.
  - "Connected" en iterative-reseed es cualquier enlace causal entre frentes adyacentes, no una sola
    through-chain a lo largo de r_S (notes:53-54) — más débil que "una geodésica nula extendida".

## 5. Falsifier attack
**Concrete failure modes**
1. **El discriminador de dirección en Fase #1-B es no fiable y su fallo no está contenido.**
   `measure_expansion_horizon.py:98-99` parte escaleras con `relphi_mean > median(relphi_mean)`
   ("outgoing"/"ingoing"); las propias notas lo marcan ABSTAIN (`PR003_EXPANSION_NOTES.md:53`). Un
   split corrupto contamina el estimador Eq.14 — el cambio de signo a 3600 podría ser artefacto de la
   población de escaleras, no física. El POSITIVO a 3600 se reclama sin evidencia de que la etiqueta de
   dirección sea mejor que azar a esa densidad.
2. **El POSITIVO a 3600 es una afirmación de densidad única con señal que degrada a la siguiente.** La
   región interior-negativa desaparece del todo a 7200. El criterio EGS (Θ_out<0 dentro) no se cumple
   a 7200. Llamar "reproduce EGS" desde una densidad que se rompe es sobre-afirmar.
3. **"Connected" en v0 es demasiado débil.** `measure_iterative_reseed.py:88-100` define conectividad
   como cualquier enlace causal entre un testigo del frente inferior y uno del superior — no
   continuidad del locus a lo largo de r_S. El 90→95 % puede venir mayormente de la cola de outliers.
4. **`covers` cae 74→65 % al subir densidad — dirección equivocada, tratada como mero caveat.** La
   `std` (0.097→0.071) supera `theta_stab` a 7200 (`thresholds.py:111-113`). El criterio de éxito de
   Fase #1 incluye "no degradar con densidad" (`hoja_de_ruta_24_jun_2026.md:80`); bajo ese criterio
   esto es FAIL de convergencia, no caveat.
5. **El ángulo de campo BD (ángulo 1) es conocidamente inaplicable al vacío 1+1D Schwarzschild.** En
   1+1D el Riemann ∝ Ricci escalar y el Schwarzschild de vacío cumple R_μν=0 (exterior localmente plano
   en 2D). El operador BD aproxima `(□ − R/2)φ` (BD2010 Eq.12); con R=0, `B_kφ → □φ` — **no hay señal
   de curvatura**. El campo `Bφ(x)` sería idéntico al de Minkowski a primer orden. El "caveat" del
   matemático es en realidad un **resultado nulo definitivo** para esta geometría.
6. **El ángulo molécula/acción BD (ángulo 3) usa un resultado SMI∝área de 3D/4D.** El resultado de la
   tesis de Benincasa es para d=3 y d=4 (Cap.6, pp.77-82); en 1+1D un área codim-2 es un punto (0D) y
   la acción 2D es topológica (carácter Gauss-Bonnet, Cap.5). La afirmación "frontera ∝ área de
   horizonte" en 1+1D es un **non-sequitur dimensional** `[UNVERIFIED]`.
7. **El ángulo antichain (ángulo 2) requiere una anticadena maximal (inextensible), pero los level-sets
   de `L_past` no están garantizados maximales.** Elementos del borde del sprinkling sin futuro causal
   dentro de la caja pueden extender la anticadena → no funciona como rebanada de Cauchy, no soporta la
   interpretación "regime change de distancia dentro de la rebanada".

**Ground-truth leakage**
1. **Frontera de scoring del campo BD: "congelar `l_k` en EXPLORE_POOL antes de validación" confunde
   fijar un parámetro con fijarlo tras mirar un score.** Si el procedimiento es (a) computar `Bφ` para
   varios `l_k`, (b) elegir el `l_k` que mejor localiza r_S en EXPLORE_POOL, (c) congelarlo → `l_k`
   queda guiado por `r`. El contrato 5 del leakage gate (`pr003_leakage_gate.md`) prohíbe re-seleccionar
   una regla tras ver cualquier resultado puntuado. Es el riesgo de anti-reverse-engineering que el
   guardián marcó como "máximo riesgo estructural".
2. **Fase #1-B: el split por `relphi_mean` se computa sobre una cantidad (Lfut relativa a Lpast) que
   correlaciona con la geometría interior/exterior.** A r<R_S los futuros se truncan, suprimiendo Lfut
   → esos elementos caen bajo la mediana y se etiquetan "ingoing" (respuesta física correcta, pero el
   etiquetado lo guía la geometría de `C` que refleja `r`). Es order-only (solo `C`), pero hace falta
   mostrar que el split está balanceado en MINK para confirmar que no explota la geometría del BH.
3. **El cambio "caja alta" es la palanca del físico, condicionalmente permitida como dev.** El riesgo
   no es fuga directa a `r` sino a la meta-decisión sobre qué cambio de dominio proponer si un run a
   t_edge mayor "se ve mejor".
4. **El ángulo antichain usa el mismo proxy `sep` que Fase #1-B.** En el interior hay menos candidatos
   de pasado común (truncación) → `sep` sistemáticamente NaN/pequeño en el lado interior → apariencia de
   "regime change" que es artefacto de muestreo, no orden puro.

**Freeze violations**
1. **La puerta `τ(n)` ya está congelada en `fixtures/tau_table.json` (`estimator_v2_seal.md:19`)** con
   α=0.01, MC_SEED=20260621, etc. La "regla de parada order-only para frentes no-cubrientes" del
   ingeniero, si es **nueva** sobre `τ(n)`, es un parámetro sin ancla congelada (máximo riesgo del
   guardián). Usar la `τ(n)` **existente** como criterio de parada (abstener por frente) **esquiva** el
   riesgo. La regla nueva está hoy sin congelar ni definir.
2. **Caja alta t_edge.** El freeze fija `T_EDGE_MIN=6.0` y `BOX_AREA=7.2` (thresholds.py:41). El
   addendum sanciona un *chequeo de invariancia* t_edge 6.0 vs 8.0 como guard dev, no un cambio de
   dominio para una corrida committing. Subir a t\*/r_S∈[0,50] es factor ~8 en extensión temporal y en
   BOX_AREA; `theta_stab`/`theta_loc` escalan con ℓ que escala con BOX_AREA. Un resultado a t_edge=12
   contra θ_stab calculado para t_edge=6 usaría un umbral demasiado estricto por ~√2. Permitido como
   dev; el fallo es comparar contra el umbral equivocado y creer que "pasa".
3. **La secuencia de freeze de `l_k`** es post-hoc por construcción si se elige tras ver scores dev. Un
   ángulo nuevo requiere un documento de freeze nuevo que fije el ancla principiada de `l_k` (la fórmula
   BD2010 de supresión de fluctuaciones) **antes** de mirar cualquier d_perp en EXPLORE_POOL.

**Verdict coercion**
1. **"PARCIAL" para Fase #1-B colapsa una situación tipo FAIL-de-convergencia en una palabra
   matizada.** Bajo el criterio "no degradar con densidad", el veredicto correcto del conjunto es FAIL
   de convergencia, no PARCIAL.
2. **v0 "POSITIVO preliminar" pese a dos criterios fallando** (`covers` baja; `std` a 7200 supera
   θ_stab). "INCONCLUSIVE pendiente de 3ª densidad" sería más honesto.
3. **Abstain-a-excluir silencioso:** los frentes que abstienen vía `τ(n)` se excluyen del locus sin
   contar como "miss" en la cobertura → si `τ(n)` abstiene sistemáticamente en frentes interiores, la
   cobertura está sesgada al alza.

**Premature / over-broad claims**
1. **El marco "horizonte aparente" en Fase #1-B está prohibido por el guardián** y no es la afirmación
   congelada (`preregistration_002.md`: "recovers hidden r_S within bracket width"). El docstring
   (`measure_expansion_horizon.py:7`) usa "apparent horizon".
2. **SMI∝área en 1+1D** no transfiere (tesis d=3/4; codim-2=punto en 2D) `[UNVERIFIED]`.
3. **"Bimodalidad implícitamente Schwarzschild-singular"** — cualquier paso que re-enmarque la salida
   como "estructura de horizonte de eventos" cruza `NO_RECONSTRUCTION_CLAIM`. El marco correcto ya está
   en las notas (`PR003_ITERATIVE_RESEED_NOTES.md:55`): el avance es el subconjunto ordenado extendido
   conexo, no un principio nuevo.

**Independent-falsification gate**
NO satisfecho para los tres ángulos nuevos: propuestos, descritos y respaldados por el mismo rol
(matemático). El verificador de literatura confirmó la fórmula BD2010 Eq.13, pero las afirmaciones
críticas (campo BD detecta curvatura en 1+1D; SMI∝área transfiere a 1+1D; level-sets de L_past
inextensibles) no las verificó ningún rol independiente — solo el falsador (y las refuta). Para Fase
#1-B, el POSITIVO a 3600 lo verifica solo el mismo script que lo generó; el control MINK corre con el
mismo código. Falta un chequeo independiente real (segunda implementación o scorer distinto).

**Minimal falsification test**
El fallo más peligroso es que el split de dirección corrompa la señal de Fase #1-B. Chequeo ejecutable:
correr `dev/measure_expansion_horizon.py --smoke` con `out_mask` = `np.ones(len(ladders), bool)` (TODAS
las escaleras, sin split outgoing/ingoing). Si el cambio de signo de mean(E) en r*≈R_S **sobrevive sin
el filtro de dirección**, la señal es robusta al discriminador no fiable; si **desaparece**, el POSITIVO
a 3600 es enteramente artefacto de la selección de escaleras y Fase #1-B es nulo. Sin datos nuevos, <5
min, precondición necesaria antes de reclamar reproducción order-only del cambio de signo Θ_out.

## 6. Pre-registration verdict
- **Verdict: PASS** (para los pasos dev/exploratorios descritos; no se propone corrida committing).
- **Freeze status: INTACTO.** El fichero sellado es `thresholds.py` SHA `6e2c3888…`
  (`preregistration_002.md`). Ningún paso fija/cambia un umbral PASS/FAIL. El freeze futuro de `l_k`/
  regla `τ` debe documentarse por escrito y establecerse **antes** de ver cualquier semilla de
  RESERVED_002 (`preregistration.md`, `preregistration_001_addendum.md`); ese freeze es una **puerta
  futura** que debe pasar `/comite` + `/auditor` (`hoja_de_ruta_24_jun_2026.md:136-137`). Medir en
  EXPLORE_POOL es exploración pre-freeze, permitida.
- **Seal integrity: INTACTO** si los pasos se ejecutan como se describe (localizador v2 reusado sin
  tocar, `make verify-seal` antes+después, sin `validate.run()` en default/reserved). La caja alta
  cambia el dominio (`t_edge`) pero no `thresholds.py` ni el localizador.
- **Seed discipline: LIMPIO.** Las tres propuestas operan solo en `EXPLORE_POOL`; `RESERVED_002`
  virgen; el set de validación prereg-001 (≤65537) está QUEMADO y no se reusa.
- **Reporting rule: VINCULANTE.** PASS/FAIL/INCONCLUSIVE/OUT_OF_DOMAIN se reportan igual; degradaciones
  (7200) y nulls se registran sin filtrar.
- **Forbidden moves present? Tres ítems de vigilancia:** (1) el freeze futuro de `l_k`/regla `τ` debe
  declarar ancla principiada (fórmula BD2010, no el resultado dev) **antes** de comparar con verdad
  oculta — anti-reverse-engineering, máximo riesgo estructural; (2) cambio de caja alta CONDICIONALMENTE
  permitido como dev (`estimator_v2_freeze.md:69` ya sanciona el chequeo de invariancia t_edge 6.0 vs
  8.0), pero `BOX_AREA=7.2` y la tabla ℓ_λ/θ_loc asumen t_edge=6/area=7.2 — una corrida committing con
  otra área necesita una **nueva prereg**, no se injerta en prereg-002; (3) el marco "horizonte aparente"
  NO debe entrar en ninguna afirmación — la afirmación congelada es "recupera r_S oculto dentro del
  ancho del bracket".

## 7. Literature verdict
| Cita | Reclamada por | Estado |
| --- | --- | --- |
| EGS Eq.12: Θ_out=(1/r)(1−2M/r), =0 en r=2M [derived-md 221-225] | Físico & Matemático | CONFIRMED |
| EGS Eq.14: expansión discreta, pares de escaleras, cambio de signo de mean(E) [derived-md 276-289,376-384] | Físico | CONFIRMED (nota: "cambio logarítmico" es la analogía continua Eq.11; Eq.14 es un ratio — la sustancia es correcta) |
| EGS Eqs.5-7: coords EF ingoing, métrica f=1−r_S/r [derived-md 130-145] | Físico | CONFIRMED |
| EGS: horizonte de eventos requiere sprinkling INFINITO; puntos sin futuro ≈ J⁺ [derived-md 173-179] | Físico | CONFIRMED |
| EGS: bimodalidad más pronunciada con mayor extensión TEMPORAL; caja t\*/r_S∈[0,50] [derived-md 188-191,450] | Físico | CONFIRMED |
| EGS: método de escaleras "requiere numerosos sprinklings para converger…" [derived-md 469] | Físico | CONFIRMED (verbatim) |
| EGS: split longest-chain inaplicable a agujeros regulares; solo sobrevive expansión [derived-md 463-469] | Físico | CONFIRMED |
| EGS: trazador único se pela tras O(1) rungs; horizonte a trozos = trabajo futuro [derived-md 443-444,474] | Físico/cascada | CONFIRMED (texto dice "a few rungs") |
| BD2010 Eq.2: operador d'Alembertian 2D con capas L1,L2,L3; límite (□−R/2)φ [Eq.12] | Matemático | **UNCONFIRMED** — BD2010 Eq.2 es el operador **4D** (capas L1-L4), NO el 2D. El 2D (3 capas) es de Sorkin [18], no una ecuación numerada en BD2010. Eq.12 (límite continuo) sí confirmada. |
| BD2010 Eq.13: S²=N−2N1+4N2−2N3; Nk=#intervalos de (k+1) elementos [derived-md 117,123] | Matemático | CONFIRMED |
| BD2010: fluctuaciones crecen con N salvo suavizado a escala l_k [derived-md 75-88] | Matemático | CONFIRMED |
| Tesis Benincasa: parte de frontera ∝ área codim-2; horizonte ≡ partición {P(γ),P̄(γ)}; SMI∝área [md 56,960,1015,1499-1545,1642] | Matemático | CONFIRMED (resultado en d=3/4; ver nota del falsador sobre 1+1D) |
| Anticadenas_Benincasa.md §2.1,§2.2,§3.1: antichain = hipersuperficie tipo Cauchy order-only | Matemático | CONFIRMED (distancia espacial está en §3.2, no §3.1, pero el documento la soporta) |

- **Notas:** la única cita francamente UNCONFIRMED es BD2010 Eq.2 (es el operador 4D, no el 2D). El
  resultado SMI∝área de la tesis está CONFIRMADO **pero en d=3/4** — el falsador señala (correctamente)
  que no transfiere a 1+1D. Esto degrada la motivación del ángulo 3, no su existencia como observable.

## 8. Synthesis
**Respuesta directa a la pregunta del usuario:**

**(1) ¿Hay otras ideas order-only fuera de la cascada?** Sí — el matemático aportó tres (campo de
curvatura BD, antichain=hipersuperficie, frontera/molécula de la acción BD). **Pero el falsador y el
análisis dimensional desmontan las dos más vistosas en esta geometría 1+1D de vacío:**
- **Campo de curvatura BD (ángulo 1): NULO esperado.** En vacío 1+1D, R=0 ⇒ el operador BD → `□` puro;
  no hay señal de curvatura que detectar. No vale la pena perseguirlo como detector de horizonte (sí
  como chequeo nulo barato de una línea, si se quiere documentar el null).
- **Frontera/área de la acción BD (ángulo 3): motivación rota en 1+1D.** El resultado SMI∝área es 3D/4D;
  en 2D el "área" codim-2 es un punto y la acción es topológica. La abundancia de moléculas `N_k` sigue
  siendo un observable order-only legítimo, pero **sin** el respaldo "área de horizonte" — pierde su
  razón de ser como objeto extendido de horizonte.
- **Antichain=hipersuperficie (ángulo 2):** conceptualmente el más interesante (lee el split a lo largo
  de toda una rebanada a la vez), pero (i) requiere una anticadena **maximal/inextensible**, no
  garantizada por los level-sets de `L_past`, y (ii) reusa el mismo proxy `sep` cuyo comportamiento
  interior no está validado y puede fabricar un "regime change" artefactual. Es una idea **de reserva**,
  no la apuesta.

**(2) ¿Hay un paper que ayude con la robustez a densidad / regla de parada?** Sí, dos hallazgos sólidos
y CONFIRMADOS por literatura:
- **EGS (md:469) declara la no-convergencia como problema abierto conocido** del método de escaleras, y
  **EGS (md:188-191,450) da el remedio: mayor extensión temporal de la caja** (t\*/r_S∈[0,50] vs el
  t_edge=6 actual). El físico lo identifica como la **palanca de mayor impacto, avalada por literatura,
  y neutral al umbral congelado**. Subir densidad (ρ) es la palanca *equivocada* (adelgaza las
  escaleras interiores, empeora la señal). Esta es la respuesta más concreta y disciplinada a la
  pregunta (2).
- **BD2010 (md:75-88) da el suavizado mesoescala `l_k`** como fix de robustez a densidad — pero aplica
  al campo BD, que aquí es nulo, así que su utilidad es marginal en esta geometría.
- **La regla de parada order-only ya existe: la puerta `τ(n)` congelada.** El matemático y el ingeniero
  coinciden: abstener por frente con `τ(n)` es la regla principiada para los frentes no-cubrientes —
  **sin** inventar una regla nueva sin ancla (que el guardián marca como máximo riesgo).

**Dirección recomendada (ordenada):** el camino de mayor valor y menor riesgo NO es perseguir los
ángulos matemáticos nuevos (degradados en 1+1D), sino **consolidar la física que ya funciona**:
1. **Test de falsación mínimo primero** (gratis, <5 min): re-correr expansión sin el split de dirección.
   Si el cambio de signo Θ_out no sobrevive, Fase #1-B es nulo y se reetiqueta — precondición antes de
   cualquier otra cosa.
2. **Probar la hipótesis de la caja alta** (palanca del físico, avalada por EGS, neutral al sello): un
   run dev de expansión a `t_edge` mayor (p. ej. 12, 24) en EXPLORE_POOL, comparando la negatividad
   interior y su persistencia con densidad. Es el experimento que decide si la submuestra interior es
   artefacto de dominio (arreglable) o intrínseca.
3. **Endurecer iterative-reseed v0** con la 3ª densidad (14400) y la puerta `τ(n)` **existente** como
   regla de parada de frentes no-cubrientes (NADA de regla nueva sin congelar). Reportar pase lo que
   pase, incluida una posible reetiqueta a INCONCLUSIVE.

**Disenso explícito (no oculto):**
- **Matemático vs Falsador/Físico sobre los ángulos nuevos.** El matemático recomienda el ángulo 3 (BD
  acción/área) como vía más limpia; el falsador y el análisis dimensional lo refutan en 1+1D (SMI∝área
  no transfiere; campo BD nulo). **El comité se pone del lado del falsador**: los ángulos nuevos no son
  la apuesta en esta geometría; a lo sumo `N_k` como observable sin la narrativa de área.
- **Etiquetas "PARCIAL"/"POSITIVO preliminar" (notas/roadmap) vs FAIL-de-convergencia (falsador).** El
  falsador sostiene que bajo el criterio "no degradar con densidad" lo honesto es INCONCLUSIVE/FAIL. El
  comité acepta el reproche: el paso 3 debe reportar con esa vara, sin colorear.

Sin BLOCK de pre-registración ni falsación irresuelta que impida un **paso dev**; por eso el veredicto
es un PROCEED con alcance acotado a exploración reversible.

## 9. Next-step spec
**Reversibles (pueden correrse YA si el usuario lo pide; nada se congela, nada committing):**

- **S1 — Test de falsación mínimo (precondición).** Re-correr `dev/measure_expansion_horizon.py` (smoke,
  2 semillas × 3600 de EXPLORE_POOL) con `out_mask = np.ones(len(ladders), bool)` (sin split de
  dirección). Registrar si el cambio de signo de mean(E) en r*≈R_S sobrevive. **Si desaparece**:
  reetiquetar Fase #1-B como nulo en `dev/PR003_EXPANSION_NOTES.md` antes de seguir.
- **S2 — Sonda de caja alta (el experimento decisivo de la pregunta 2).** Run dev de expansión en
  EXPLORE_POOL a `t_edge ∈ {12, 24}` (y baseline 6), midiendo negatividad interior, cruce r* y su
  persistencia entre densidades. **Pre-comprometido:** es solo dev; NO se compara contra `theta_stab`/
  `theta_loc` congelados (calculados a t_edge=6/area=7.2) — un t_edge distinto cambia ℓ y haría la
  comparación inválida; se reporta la *forma* de la señal (negatividad interior y su tendencia), no un
  PASS/FAIL de umbral. NO toca `thresholds.py` ni el localizador. `make verify-seal` = `6e2c3888…`
  antes y después.
- **S3 — Endurecer iterative-reseed (`dev/measure_iterative_reseed_v1.py`).** Añadir la 3ª densidad
  14400 y usar la puerta **`τ(n)` ya congelada** para abstener en frentes no-cubrientes (SIN regla
  nueva). Reportar `covers`, conectividad, d⊥, Guard-v y MINK a las 3 densidades, **contando los
  frentes que abstienen como "miss" en la cobertura** (evita el sesgo abstain-a-excluir que marcó el
  falsador). Confirmar antes que `C` densa N×N a 14400 cabe en memoria.

**Reglas vinculantes pre-comprometidas para S1-S3:**
- Solo semillas `EXPLORE_POOL`; `RESERVED_002` intacta. `r`/`d⊥` SOLO puntúan, nunca siembran/
  construyen/cortan/seleccionan (contrato 5 del leakage gate). Guard-v relabel debe seguir pasando.
- `make verify-seal` = `6e2c3888…` antes y después de cada run; sin editar `thresholds.py`/`gate.py`/
  `estimator.py`/`validate.py`; sin `validate.run()` en semillas default/reserved.
- Reportar PASS/FAIL/INCONCLUSIVE/null **igual**, incluida una posible reetiqueta de Fase #1-B (S1) o
  de v0 a INCONCLUSIVE (S3). NADA del marco "horizonte aparente" en afirmaciones; solo "localización
  de r_S dentro del bracket en parche finito 1+1D".

**Committing (SOLO con autorización explícita del usuario, y cada uno tras `/comite` + `/auditor`):**
- Cualquier **freeze** de un parámetro nuevo (`l_k`, una regla de parada distinta de `τ(n)`, o un
  `t_edge`/`BOX_AREA` nuevos): requiere un **documento de pre-registración nuevo** con ancla principiada
  declarada ANTES de ver scores en EXPLORE_POOL, y no se injerta en prereg-002 (guardián, ítems 1-2).
- Cualquier corrida sobre `RESERVED_002`.

**Test de falsación mínimo incluido:** S1 (arriba) es el chequeo único que expone el peor fallo
(corrupción de la señal por el split de dirección) sin datos nuevos y en <5 min; es precondición.

## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
