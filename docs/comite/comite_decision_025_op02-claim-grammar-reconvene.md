# Comité Decision 025 — OP-0.2 claim grammar reconvene

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Does revision 1 of `docs/claim_grammar.md`, SHA256
`434b95d6a1fdd3fc9f44d5831447425412cbbc10807add06c682734d97d5a534`, close committee 024's
blockers and qualify for `COMMITTEE_ADOPTED_AUDIT_PENDING`?

## 2. Verified state

- Branch `main`; source HEAD `726c8c1eda16334a1b30b9f4ad82927f0c834382`.
- Candidate hash recomputed before dispatch:
  `434b95d6a1fdd3fc9f44d5831447425412cbbc10807add06c682734d97d5a534`.
- PI sign-off authorizing revision and reconvening is recorded in
  `docs/comite/comite_decision_024_op02-claim-grammar-adoption.md:207-214`.
- Candidate remains `REVISION_1 / COMMITTEE_RECONVENE_PENDING / DOCUMENT_ONLY / NO_NEW_RESULT`
  (`docs/claim_grammar.md:3-12`).
- Live seal remained
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`; no code, data,
  result, threshold, seed or scientific execution entered this revision.
- Structural preflight passed: 15 anchors with zero missing files/ranges; committee-024 checker
  passed; its original minimal falsification text test passed after revision.
- Working tree contains only five untracked documentary artifacts: OP-0.1 matrix/audit,
  claim grammar, committee 024 and this brief.

## 3. Dossier

- `docs/claim_grammar.md` at exact hash above
- `docs/comite/comite_decision_024_op02-claim-grammar-adoption.md`
- `docs/auditor/auditor_report_013_op01-survival-matrix.md`
- `research_program/synthesis/survival_matrix_1p1_to_3p1.md`
- `research_program/work_packages/wp4_two_point_theorem.md`
- `research_program/synthesis/geometric_indeterminacy_decision.md`
- `research_program/models/first_witness_pair_candidates.md`
- `docs/estimator_v2_freeze.md`
- EGS, Surya, Benincasa-Dowker and Chevalier sources under `biblioteca/derived-md/`

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief
- Proposed artefact(s): The prior reproducibility objections are closed. `/comite` may adopt the exact `docs/claim_grammar.md` blob SHA256 `434b95d6a1fdd3fc9f44d5831447425412cbbc10807add06c682734d97d5a534` into `COMMITTEE_ADOPTED_AUDIT_PENDING`; the scoped follow-up remains `docs/auditor/auditor_report_014_op02-claim-grammar.md`. Final `CLAIM_GRAMMAR_ADOPTED` remains reserved for that auditor (`docs/claim_grammar.md:375-410`; `docs/comite/comite_decision_024_op02-claim-grammar-adoption.md:194-201`).
- Environment & seal: This remains `DOCUMENT_ONLY / NO_NEW_RESULT` (`docs/claim_grammar.md:3-5`). No scientific environment, external Minz clone, code, data, simulation or RNG is required. If mechanical gates are rerun, use the repository pin `numpy==1.26.4` (`requirements.txt:1-10`) and re-check the prereg-002 seal `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (`docs/preregistration_002.md:7-9`). Current `git status --short` contains only four untracked documentary paths and no package, threshold, code, data or result path.
- Provenance capture: Record branch `main`, committed source HEAD `726c8c1eda16334a1b30b9f4ad82927f0c834382`, predecessor draft hash `08a34ea4bc699ba58717718c3ff621a4de740fb0ff4b66c1939360b4affa9c91` (`docs/claim_grammar.md:7-12`), adopted candidate hash `434b95d6a1fdd3fc9f44d5831447425412cbbc10807add06c682734d97d5a534` (`sha256sum docs/claim_grammar.md`), committee decision, auditor decision and UTC timestamps. User authorization for revision and reconvening is recorded at `docs/comite/comite_decision_024_op02-claim-grammar-adoption.md:207-214`. `pip freeze`, `uname -a` and seed-band capture are not scientifically operative; seed band is `NONE`.
- Run mechanics: No scientific invocation or background process. The committee records the exact hash without editing the blob; the scoped auditor must independently recompute that hash, validate every anchor and claim boundary, and emit the final terminal in its report. A hash mismatch, anchor failure, overclaim or incomplete required field aborts fail-closed (`docs/claim_grammar.md:383-410`). Commit, push and any outward status promotion remain unauthorized by the recorded sign-off (`docs/comite/comite_decision_024_op02-claim-grammar-adoption.md:200-201,207-214`).
- Reproducibility risks / ambiguities:
  - The malformed-template objection is closed: the allowed form now requires an admissible evidence label plus an explicit “verbo y garantía” slot (`docs/claim_grammar.md:68-76`), and `recupera` requires an already established, anchored positive guarantee; a future declaration is expressly insufficient (`docs/claim_grammar.md:78-81`).
  - The state/hash objection is closed: the progression is explicit, all failure terminals dominate adoption, the committee and auditor operate on the same blob hash, and no post-audit status edit may change it (`docs/claim_grammar.md:383-410`).
  - Documentary scope is closed: the grammar disclaims any theorem, measurement or estimator property (`docs/claim_grammar.md:14-19`), and the result template requires evidence tier, embedding-only scoring, domain gate, abstentions, terminal precedence and `NO_RECONSTRUCTION_CLAIM` (`docs/claim_grammar.md:337-373`).
  - Residual non-blocking provenance risk: the candidate and its foundations remain untracked, so durability still depends on a later explicitly authorized commit. Hash-based committee adoption nevertheless fixes the exact content for the pending audit; any byte change requires reconvening or a newly recorded hash.
  - Final normative adoption is still blocked, by design, until the scoped auditor confirms this exact hash; audit 013 covers OP-0.1 and explicitly does not authorize OP-0.2 (`docs/auditor/auditor_report_013_op01-survival-matrix.md:9-18`).

### Mathematician brief
- Computability: The revised grammar correctly treats the input as a finite partial order, for which minimal elements, futures, longest-chain height, ordering fraction and finite interval/chain counts are decidable (`biblioteca/derived-md/Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md:40-42`). It now separates the order-intrinsic `τ(n)` estimator abstention (`docs/estimator_v2_freeze.md:48-60`) from an external generative-domain gate such as `T_EDGE_MIN` (`docs/estimator_v2_freeze.md:62-70`), both in the mandatory fields (`docs/claim_grammar.md:21-34`) and in the fail-closed precedence `FAILED_DATA_CONTRACT > OUT_OF_DOMAIN > NUMERICAL_ABSTAIN > ESTIMATOR_ABSTAIN > SCIENTIFIC_PASS_OR_FAIL` (`docs/claim_grammar.md:337-352`). The prior domain/abstention blocker is closed.
- Order observable: The operative distinction is now correct: longest-chain height from each minimal element and estimator-v2 future cardinality \(O_{\min}(i)=|\operatorname{Fut}_C(i)|\) are order-only, relabel-invariant observables (`docs/estimator_v2_freeze.md:34-38`). Their 1+1D Schwarzschild signal arises because interior timelike futures terminate at the singularity while exterior futures are limited mainly by the finite box, yielding a bimodal transition; future cardinality is explicitly more boundary-sensitive (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-195`). The revision now forbids renaming this singularity-truncation mechanism as a quasi-local trapping observable (`docs/claim_grammar.md:83-91`) and requires dimension, chart, physical patch, truncations and mechanism in every claim (`docs/claim_grammar.md:21-34,354-370`). The prior chart/dimension and physical-mechanism blockers are closed.
- Relevant invariants: Ordering fraction \(r=2R/[n(n-1)]\) is an ensemble dimension statistic, not a single-instance manifoldlikeness certificate (`biblioteca/derived-md/The causal set approach to quantum gravity.md:1001-1015,1054-1082`). Longest-chain height is the standard causal-set proxy for timelike distance (`ibid.:1221-1233`); \(C_k\) chain abundances are finite-causet order invariants with ensemble continuum formulae (`ibid.:1092-1118,1151-1152`); future volume remains a truncation-sensitive invariant (`docs/estimator_v2_freeze.md:34-38`; EGS `derived-md:191-195`). The revised ensemble clauses correctly require the sampling unit, changing law, fixed parameters and independence structure (`docs/claim_grammar.md:216-245`).
- Analytic / continuum target: The grammar now keeps distinct the global event horizon, the singular-Schwarzschild truncation cut, and a separately defined expansion/trapping proxy (`docs/claim_grammar.md:61-91`). It also correctly separates Poisson density sequences \(N_k\sim\operatorname{Poisson}(rho_kV_k)\), conditional sequences \(n_k\to\infty\), and patch-extension sequences (`docs/claim_grammar.md:93-106`). Conditioned on \(N=n\), the sampling law is normalized volume and contains no observable \(rho\) parameter (`research_program/models/first_witness_pair_candidates.md:23-31`), exactly as the revised prohibitions and ensemble rule now state (`docs/claim_grammar.md:206-212,230-245`). The prior fixed-`n`/\(rho\) blocker is closed.
- Caveats:
  - **Disposition: committee adoption is mathematically supportable for this exact revised blob, with audit still pending.** The appropriate next state is `COMMITTEE_ADOPTED_AUDIT_PENDING`, not final `CLAIM_GRAMMAR_ADOPTED`; the latter requires the hash-specific auditor gate (`docs/claim_grammar.md:375-407`; authorization boundary at `docs/comite/comite_decision_024_op02-claim-grammar-adoption.md:207-214`).
  - The duality contract is now sufficiently typed for normative use: it freezes a dual-closed model family and involution, common isomorphism-class channel, coherent support bijection, relabel-equivariance and randomized-estimator coupling (`docs/claim_grammar.md:121-146`). For deterministic character outputs, self-duality correctly forces `chi_hat=0` and the explicit `CHARACTER_ABSTAIN_SELF_DUAL` terminal (`docs/claim_grammar.md:137-149`). Any future empirical duality claim must instantiate these declared structures; the grammar does not claim an existing estimator satisfies them.
  - The TV witness statement is correct on a common measurable experiment for \(f:\Omega\to[0,1]\) (`docs/claim_grammar.md:267-283`). With simultaneous expectation intervals, \(L_{\rm gap}=\max(0,L_P-U_Q,L_Q-U_P)\) is a valid confidence lower bound, and the revision permits certified separation only when `L_gap>0` under a predeclared witness and Monte Carlo budget (`docs/claim_grammar.md:285-296`). The prior common-experiment and confidence-validity blockers are closed.
  - The regular-black-hole caveat must retain the source’s scope: EGS specifically discusses failure of this diagnostic for geodesically complete regular examples such as Hayward in 3+1D (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:195-201`). The revised wording says only that transfer is not automatic and mandates dimension and physical class, so it does not overclaim (`docs/claim_grammar.md:23,83-91`).
  - The kinematics/dynamics boundary is correctly stated: sprinkling constructs a prescribed-background causet through Poisson sampling and inherited order, but does not show dynamical selection (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:102-119`; `docs/claim_grammar.md:308-335`). KR-type entropic dominance remains a separate dynamics problem (`biblioteca/derived-md/Chevalier_2023_Discrete_Causal_Action_and_Holes_in_Spacetime.md:204-213`).

### Mathematical logic brief
- Formal status: Revision 1 remains a normative definition, not a theorem or result (`docs/claim_grammar.md:14-19`). The duality equations remain correctly labeled `TARGET` (`docs/claim_grammar.md:137-149`); the bounded-witness inequality and confidence lower endpoint are proved mathematical consequences (`docs/claim_grammar.md:274-296`); target recovery from either TV direction remains conditional on a separately closed target/output/loss contract (`docs/claim_grammar.md:267-272`, `:295-304`). User sign-off authorized revision and reconvening only, not adoption or execution (`docs/comite/comite_decision_024_op02-claim-grammar-adoption.md:207-214`).
- Quantifier / dependency order: The revision now freezes model involution, channel, dual-stable observation space, support bijection, involution coherence, relabel-equivariance, and randomized-estimator semantics before asserting the universal deterministic equations (`docs/claim_grammar.md:126-149`). However, the displayed quantifier still ranges over `P in Omega_K`, where `Omega_K` was typed as isomorphism classes, while `S(P)`, `iota_P`, and `H_hat(P) subset S(P)` require a labeled representative (`docs/claim_grammar.md:121-144`). It must quantify over every representative of each class, or define an equivariant family over the representative groupoid. The model involution `D:G_dual->G_dual` must also be linked explicitly to dual pushforward of the corresponding observation laws; otherwise “verified over `G_dual`” does not follow from the proposition over `Omega_K` (`docs/claim_grammar.md:128-146`).
- Equivalence claims: Relabel invariance plus anti-equivariance now correctly forces `chi_hat=0` on self-dual classes, with typed abstention rather than BH/WH promotion (`docs/claim_grammar.md:132-149`). The witness statement is a valid one-way bound for two laws on one measurable space, and `L_gap=max(0,L_P-U_Q,L_Q-U_P)` is a simultaneous-confidence lower endpoint with the declared coverage (`docs/claim_grammar.md:274-295`). The upper-TV consequence is correct for the exact-error two-point theorem with distinct targets (`research_program/work_packages/wp4_two_point_theorem.md:81-124`); for a generic geometric loss, “separación declarada” must additionally mean disjoint acceptable-decision regions, or a numeric target separation plus loss geometry sufficient to derive them. Without that condition, `docs/claim_grammar.md:267-272` does not yet determine the claimed loss floor.
- Type / object discipline: The revision correctly keeps a bounded scalar witness `f:Omega->[0,1]` distinct from a set-valued localizer and expressly forbids promoting existence of a test into existence of a geometric localizer (`docs/claim_grammar.md:274-304`). It also keeps continuous target, physical mechanism, discrete output, loss, and embedding-only scoring as separate mandatory fields (`docs/claim_grammar.md:21-34`, `:354-370`). The remaining class-versus-representative mismatch in the duality block is a genuine type defect, not merely notation (`docs/claim_grammar.md:123-144`).
- Caveats:
  - The state machine is now fail-closed and exhaustive for incompleteness, overclaim, and anchor failure, with explicit precedence and same-hash committee/auditor handoff (`docs/claim_grammar.md:375-410`). The dossier hash is confirmed by `sha256sum docs/claim_grammar.md` as `434b95d6a1fdd3fc9f44d5831447425412cbbc10807add06c682734d97d5a534`; the reconvened decision must record that exact hash before any audit.
  - Current logical terminal: `CLAIM_GRAMMAR_INCOMPLETE`, because the duality proposition still mixes quotient classes with carrier-bearing representatives and the generic-loss upper-TV clause lacks the condition that converts target separation into disjoint success events (`docs/claim_grammar.md:267-272`, `:390-410`).
  - After those two narrow corrections, the mathematical-logic objections from committee 024 are closed; `CLAIM_GRAMMAR_ADOPTED` must still wait for the scoped auditor confirmation required by the machine (`docs/claim_grammar.md:394-410`).

### Physicist brief
- **Coordinates & patch:** The reviewed blob matches SHA256 `434b95d6a1fdd3fc9f44d5831447425412cbbc10807add06c682734d97d5a534` (`sha256sum docs/claim_grammar.md`). The revision now requires dimension, physical class, chart, patch, truncations, extension rule, channel, and experimental sequence in every claim (`docs/claim_grammar.md:21-34,354-370`). This correctly accommodates the existing finite 1+1D EF box while preventing its coordinate patch from being silently generalized (`docs/preregistration_001_addendum.md:35-45`).
- **Physical meaning of the signal:** Teleology/truncation/trapping are now separated explicitly: global event horizon, singularity-truncation cut, and independently defined quasi-local proxy are distinct objects (`docs/claim_grammar.md:57-91`). The regular-BH caveat is also present. One residual physical sentence is still needed: in 1+1D EGS cannot compute the continuum null expansion or a genuine marginally trapped codimension-two surface and instead uses a one-dimensional inter-geodesic-distance proxy (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:221-230`). Without that literal caveat, “proxy de expansión/trapping” remains vulnerable to being read as the continuum object.
- **Sprinkling domain:** The density and patch sequences are physically closed: Poisson `rho_k` at fixed patch, conditional `n_k` for `fixed_n`, and patch growth with declared resolution/extension are distinguished (`docs/claim_grammar.md:93-106,173-214,216-245`). The scale contract `N~Poisson(rho V)` and `ell=rho^(-1/d)` is correct, and the grammar forbids treating an unchanged fixed-`n` experiment as `rho→∞` (`docs/claim_grammar.md:184-212`).
- **Claim boundary:** Physics closure is nearly complete, but normative adoption should wait for three surgical corrections: add the explicit 1+1D expansion caveat above; repair the class-versus-representative typing in duality; and state the exact loss condition under which a TV upper bound yields a risk floor. The current duality rule defines `Omega_K` as isomorphism classes but then quantifies `P∈Omega_K` while using representative-level support `S(P)` (`docs/claim_grammar.md:121-144`). It should quantify over representatives with `[P]∈Omega_K`, define duality on `[P]`, and reserve `iota_P` for representative-level equivariance.
- **Caveats:**
  - The singularity-truncation diagnostic is correctly restricted: EGS states it is inapplicable to geodesically complete black holes, whereas the ladder expansion proxy is a different candidate (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:463-469`).
  - The physical prerequisites for BH/WH character are now substantially closed: time-oriented model family, involution, dual-stable channel, support map, relabeling equivariance, randomized coupling, and self-dual abstention are all specified (`docs/claim_grammar.md:126-155`). Only the class/representative type mismatch remains.
  - “Targets distinct and separation declared under the loss” is insufficient for an arbitrary loss (`docs/claim_grammar.md:267-272`). The cited theorem is exact for target misclassification (`research_program/work_packages/wp4_two_point_theorem.md:81-124`); metric risk requires an explicit target separation `Delta_T` and the nearest-target reduction (`research_program/synthesis/geometric_indeterminacy_decision.md:214-234`). A generic loss needs disjoint low-loss decision regions or another stated reduction.
  - Kinematics versus dynamics is closed correctly: sprinkling a supplied geometry licenses conditional kinematic recoverability only, not manifold emergence or dynamical selection (`docs/claim_grammar.md:308-335`; `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:102-119`).
  - **Physicist verdict:** `REVISE_BEFORE_ADOPTION`; no new scientific execution or result is implicated.

## 5. Falsifier attack

### Falsifier attack
- Concrete failure modes: `DECISION=CLAIM_GRAMMAR_INCOMPLETE`. El SHA fue verificado exactamente con `sha256sum docs/claim_grammar.md` -> `434b95d6a1fdd3fc9f44d5831447425412cbbc10807add06c682734d97d5a534`. Persisten tres fallos normativos. (1) `Omega_K` se define como espacio de clases de isomorfismo, pero después se cuantifica `P in Omega_K` usando portador `S(P)`, relabeling `sigma.P` y biyección `iota_P`; una clase no posee un portador canónico (`docs/claim_grammar.md:121-144`). Deben separarse el espacio de representantes etiquetados, el cociente y su mapa, y formular allí la equivariancia. (2) La involución de modelos `D:G_dual->G_dual` no se enlaza con la dualidad del canal mediante una identidad de pushforward de leyes, por ejemplo `Law_K(Dg)=d_#Law_K(g)` (`docs/claim_grammar.md:126-146`). Sin ella, las ecuaciones del estimador no establecen covariancia sobre la familia generativa. (3) Para pérdida genérica, “targets distintos y separación declarada” no basta para transportar el suelo TV: deben fijarse un umbral `delta`, regiones aceptables disjuntas `A_theta={a:L(a,T(theta))<=delta}` y la reducción numérica correspondiente. El teorema citado solo prueba la versión de acierto exacto/0-1 (`research_program/work_packages/wp4_two_point_theorem.md:81-121`), mientras la gramática omite esas regiones y afirma que la cota “activa” el suelo (`docs/claim_grammar.md:267-272`).
- Ground-truth leakage: La plantilla general ya exige `embedding-only-scores` (`docs/claim_grammar.md:21-34`, `:354-370`), pero la ambigüedad representante/clase permite construir `iota_P`, acoplar muestras duales o escoger representantes usando la correspondencia del embedding. Además, EGS reconoce que clasificó ladders ingoing/outgoing mediante embedding, no de forma intrínseca (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:480-482`). La identidad de pushforward y la regla sobre representantes deben ser parte del contrato previo, no una elección durante scoring.
- Freeze violations: No hay ejecución ni violación directa de sellos en OP-0.2, y la revisión prohíbe promociones retrospectivas (`docs/claim_grammar.md:51-55`). Sin embargo, quedan sin congelar el mapa dual observado, el acoplamiento/elección de representantes y las regiones de decisión para pérdida genérica; elegir cualquiera tras observar resultados cambiaría la garantía sin cambiar formalmente el testigo. Esos objetos deben constar en el artefacto preregistrado antes de datos.
- Verdict coercion: La precedencia explícita de `FAILED_DATA_CONTRACT`, dominio y abstenciones corrige el defecto anterior (`docs/claim_grammar.md:337-352`), y el caso autodual ahora fuerza correctamente `CHARACTER_ABSTAIN_SELF_DUAL` (`docs/claim_grammar.md:146-149`). El riesgo residual está en la cota superior: sin regiones aceptables disjuntas y reducción numérica, una cota TV puede coercionarse a un FAIL de recoverability aunque exista una decisión aceptable para ambos targets bajo la pérdida. Debe activar `ADVERSARIAL_GUARANTEE_CLAIM_FAIL` o `CLAIM_GRAMMAR_INCOMPLETE`, nunca un resultado científico.
- Premature / over-broad claims: La gramática presenta expansión/trapping como alternativa cuasi-local (`docs/claim_grammar.md:61-66`, `:83-87`) pero omite la salvedad literal de que el experimento EGS 1+1D carece de superficies espaciales bidimensionales, no puede calcular la expansión nula verdadera y usa la distancia espacial unidimensional entre geodésicas como proxy (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:201-230`). Sin esa frase, “expansión discreta” puede leerse como expansión de una superficie marginal codimensión 2 y promover indebidamente el toy model 1+1D a un target geométrico 3+1D.
- Independent-falsification gate: No está satisfecho. El blob exacto sigue declarando `COMMITTEE_RECONVENE_PENDING` y `AUDIT_PENDING` (`docs/claim_grammar.md:375-380`), y su propia máquina exige `CLAIM_GRAMMAR_INCOMPLETE` cuando falta un tipo, cuantificador o gate (`docs/claim_grammar.md:383-410`). La adopción debe esperar una segunda revisión que cierre los tres defectos y una auditoría del nuevo hash.
- Minimal falsification test: Ejecutar `python -c "d=.75; a=.5; assert abs(a-0)<=d and abs(a-1)<=d; print('OVERLAPPING_ACCEPTABLE_REGIONS')"`; produce un estimador constante aceptable para ambos targets distintos `0` y `1`. Por tanto, una cota TV no implica el suelo de error genérico anunciado hasta exigir regiones de decisión disjuntas, exponiendo directamente el defecto de `docs/claim_grammar.md:267-272`.

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: BLOCK
- Freeze status: N/A for numerical thresholds: OP-0.2 remains document-only, but the exact revised blob `434b95d6a1fdd3fc9f44d5831447425412cbbc10807add06c682734d97d5a534` is still `COMMITTEE_RECONVENE_PENDING`, not adopted or audited (`docs/claim_grammar.md:3-12`, `docs/claim_grammar.md:375-410`). Decision 024 authorized revision and reconvening only, explicitly withholding status promotion (`docs/comite/comite_decision_024_op02-claim-grammar-adoption.md:207-214`).
- Seal integrity: The documentary revision does not run or alter the sealed path. The live `nachocausal/thresholds.py` SHA256 remains `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching the operative prereg-002 seal (`docs/preregistration_002.md:7-12`).
- Seed discipline: No seed is used or burned. The prereg-002 dev and held-out bands remain the documented disjoint historical populations (`docs/preregistration_002.md:14-33`); OP-0.2 authorizes no scientific execution (`docs/comite/comite_decision_024_op02-claim-grammar-adoption.md:200-201`).
- Reporting rule: Report this `BLOCK` without coercion into adoption. The grammar's fail-closed state machine permits `CLAIM_GRAMMAR_INCOMPLETE` from any state (`docs/claim_grammar.md:383-410`), while future confirmatory outcomes remain subject to report-alike and no retuning or rerun after inspection (`docs/preregistration_002.md:59-68`).
- Forbidden moves present? No post-hoc tuning, threshold loosening, seed reuse, validation rerun or ground-truth leakage occurred. Promoting this blob to `ADOPTED` would exceed the PI sign-off and would freeze three remaining specification gaps (`docs/comite/comite_decision_024_op02-claim-grammar-adoption.md:207-214`).
- Reasons:
  - The duality clause defines `Omega_K` as a space of isomorphism classes, then quantifies `P in Omega_K` while applying representative-level objects `S(P)`, `P^op` and `iota_P`; the class/representative typing is therefore still inconsistent (`docs/claim_grammar.md:121-144`). It also declares a model involution `D:G_dual->G_dual` but gives no induced channel-law pushforward connecting `D(g)` to dualization on `Omega_K` (`docs/claim_grammar.md:126-146`).
  - The upper-TV rule says distinct targets plus unspecified separation under a generic loss activate the two-point floor (`docs/claim_grammar.md:267-272`), but the cited theorem is proved for exact target recovery via disjoint equality events (`research_program/work_packages/wp4_two_point_theorem.md:81-110`). A generic-loss consequence additionally needs disjoint success regions and an explicit test reduction or equivalent loss hypotheses.
  - The draft distinguishes singularity truncation from trapping and mentions regular-black-hole non-transfer (`docs/claim_grammar.md:83-91`), but it still omits the literal dimensional caveat required by Decision 024: in 1+1D the spatial codimension-two surfaces needed for true null expansions are unavailable, so the ladder construction is only an analogue (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:197-230`; `docs/comite/comite_decision_024_op02-claim-grammar-adoption.md:192-193`).
  - These are `CLAIM_GRAMMAR_INCOMPLETE`, not grounds to touch the seal or rerun evidence. After correction, the exact new hash requires another committee decision and then the independent auditor gate before `CLAIM_GRAMMAR_ADOPTED` (`docs/claim_grammar.md:394-410`).

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| Eichhorn–Gamito–Stokes, *Towards black-hole horizons and geodesic focusing in causal sets*, §II, Eq. (4), derived-md lines 102–119 | Causet mathematician / revised grammar §§5,8 — sprinkling is a finite-region Poisson construction with \(N\sim\mathrm{Poisson}(rho V)\), \(ell=rho^{-1/d}\), inherited causal order and no retained embedding | CONFIRMED |
| Eichhorn–Gamito–Stokes, §III, Eq. (9), derived-md lines 171–179 | Physicist — a global event horizon requires future-null-infinity information, while the cited causal horizon is the boundary of the past of a future-inextendible infinite-proper-length curve | CONFIRMED |
| Eichhorn–Gamito–Stokes, §III–IV, derived-md lines 181–201 | Causet mathematician / Physicist / revised grammar §3 — longest-chain and future-cardinality bimodality is a singularity- and finite-boundary-truncation diagnostic, expected to fail for regular geodesically complete black holes | CONFIRMED |
| Eichhorn–Gamito–Stokes, §IV, Eqs. (11)–(12), derived-md lines 214–230 | Physicist — Schwarzschild null expansions change sign at \(r=2M\), but a 1+1D sprinkling has no spatial two-surfaces and therefore cannot compute the true null expansion; the paper substitutes one-dimensional inter-geodesic distance | CONFIRMED |
| Eichhorn–Gamito–Stokes, §VI, derived-md lines 463–469 | Physicist — the first diagnostic is restricted to geodesically incomplete black holes; the ladder diagnostic is only a discrete counterpart based on neighboring-geodesic distance, reproduces expected signs, and requires numerous sprinklings for convergence | CONFIRMED |
| Eichhorn–Gamito–Stokes, §IV and §VI, derived-md lines 221–230 and 463–469 | Any claim that the current longest-chain/future-cardinality estimator computes a true codimension-two marginal surface or true null expansion in 1+1D | UNCONFIRMED |
| `research_program/work_packages/wp4_two_point_theorem.md` §3, lines 81–124 | Mathematical logician / revised grammar §7 — for distinct targets under exact classification loss, every order-only estimator has summed error at least \(1-TV\), with equality attainable by a likelihood-ratio classifier | CONFIRMED |
| `research_program/work_packages/wp4_two_point_theorem.md` §3, lines 81–124 | Revised grammar §7 — the same cited theorem directly supplies a lower bound for an arbitrary geometric metric loss merely from “separation under the loss” | UNCONFIRMED |
| `research_program/synthesis/geometric_indeterminacy_decision.md` §6.2, lines 214–234 | Mathematical logician — nearest-target reduction converts the binary classification bound into a metric tail bound at \(Delta_T/2\) and expected-risk bound \(Delta_T(1-epsilon)/4\) | CONFIRMED |
| Chevalier, *Discrete Causal Action and Holes in Spacetime*, §2.2, Conjecture 2.2.1, derived-md lines 196–202 | Causet mathematician — the Hauptvermutung is an unproved approximate-uniqueness conjecture | CONFIRMED |
| Chevalier, §2.3, derived-md lines 204–213 | Causet mathematician / revised grammar §8 — KR dominance is non-manifoldlike and its suppression is a separate dynamics problem | CONFIRMED |
| Benincasa–Dowker, *The Scalar Curvature of a Causal Set*, derived-md lines 40–42 | Causet mathematician — a causal set is a locally finite partial order and sprinkling is a Poisson process with inherited causal order | CONFIRMED |
| Surya, *The causal set approach to quantum gravity*, §4.1, derived-md lines 1001–1015 and 1054–1082 | Causet mathematician — ordering-fraction dimension inference is ensemble-scoped, has finite-density fluctuations, and matching it does not establish manifoldlikeness | CONFIRMED |
| Surya, §4.1 and §4.3, derived-md lines 1092–1118, 1151–1152 and 1221–1246 | Causet mathematician — chain abundances are order invariants and longest-chain distance has an ensemble asymptotic with large finite-density fluctuations | CONFIRMED |

- Notes: The exact revised blob was verified at SHA256 `434b95d6a1fdd3fc9f44d5831447425412cbbc10807add06c682734d97d5a534`. The sources support both requested surgical revisions: add the explicit 1+1D caveat that the available construction is a one-dimensional distance proxy, not a true null expansion or codimension-two marginal surface; and distinguish the exact classification-loss theorem in `wp4_two_point_theorem.md` from the separate nearest-target reduction needed for metric loss. EGS does not license renaming the current truncation estimator as the ladder/expansion proxy.

## 8. Synthesis

Revision 1 closes the original defects in evidence labels, state/hash transition, channel limits,
abstention precedence, positive-TV confidence and the singular/regular distinction. Reproducibility
and the causal-set mathematician support adoption pending audit. Mathematical logic and physics
independently identify the same remaining type/loss defects; the preregistration warden emits
`BLOCK`, and literature confirms that the two missing caveats are substantive. The current terminal
is therefore `CLAIM_GRAMMAR_INCOMPLETE`.

Three corrections are necessary and sufficient for another reconvening:

1. separate labeled representatives from isomorphism classes; define duality on both levels,
   relabel-equivariant support maps, and the model-law identity
   `Law_K(Dg)=d_#Law_K(g)`;
2. restrict the direct two-point consequence to exact classification, and for generic loss require
   disjoint `delta`-success regions plus an explicit reduction, with the nearest-target metric
   reduction as a named special case;
3. state literally that 1+1D lacks the codimension-two spatial surfaces needed for true null
   expansion and that the EGS construction uses a one-dimensional inter-geodesic-distance proxy.

No threshold, seal, seed, implementation, empirical result or scientific direction is implicated.

## 9. Next-step spec

**Reversible revision, after user sign-off:**

1. Patch only the three clauses named in §8 of `docs/claim_grammar.md`.
2. Freeze the new candidate hash and run structural anchor/whitespace checks.
3. Run the falsifier overlap example; the revised text must explicitly explain why distinct targets
   alone do not yield a generic-loss floor.
4. Reconvene `/comite` on the exact new hash. A single unresolved class/representative, loss or
   1+1D-expansion issue emits `CLAIM_GRAMMAR_INCOMPLETE`.
5. If and only if the warden returns PASS and the committee adopts, run the scoped `/auditor` on
   the identical hash.

No commit, push, status promotion or scientific execution is authorized by this brief.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off

Signed: Nacho / PI

Date: 2026-07-15

Decision: authorize the three reversible corrections in §8-§9, reconvene `/comite` on the new
hash and, only after committee adoption, run the scoped `/auditor`. No commit, push or scientific
execution is authorized.
