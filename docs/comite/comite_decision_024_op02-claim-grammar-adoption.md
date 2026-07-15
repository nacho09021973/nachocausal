# Comité Decision 024 — OP-0.2 claim grammar adoption

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Should `docs/claim_grammar.md` be adopted as the normative OP-0.2 claim grammar, or must it be
revised or blocked before adoption?

## 2. Verified state

- Branch `main`; committed source HEAD
  `726c8c1eda16334a1b30b9f4ad82927f0c834382` (`git rev-parse HEAD`).
- `origin/main` contains the same committed HEAD; the working tree contains only documentary
  untracked candidates: OP-0.1 matrix, audit 013 and OP-0.2 claim grammar
  (`git status --short --branch`).
- Live `nachocausal/thresholds.py` SHA256 is
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
  (`make verify-seal`), matching `docs/preregistration_002.md:7-12`.
- `make test` completed successfully before committee dispatch; no scientific path, seed, data or
  simulation was run for OP-0.2.
- OP-0.1 gate: `SURVIVAL_MATRIX_COMPLETE`; repo-level audit
  `AUDIT_PASS_WITH_WARNINGS` due 22 historical generator-reference warnings
  (`docs/auditor/auditor_report_013_op01-survival-matrix.md:122-145`).
- `data/reports/pr012_tv_curve_n8.csv` is absent; PR012 remains draft/unpublished
  (`research_program/synthesis/pr012_tv_curve_scope.md:176-190`).
- Candidate state is `COMMITTEE_PENDING / DOCUMENT_ONLY / NO_NEW_RESULT`; its committee and audit
  gates are pending (`docs/claim_grammar.md:1-8`, `:295-307`).

## 3. Dossier

- `docs/claim_grammar.md`
- `docs/plan_operativo_15_julio_2026.md:140-167`
- `research_program/synthesis/survival_matrix_1p1_to_3p1.md`
- `docs/auditor/auditor_report_013_op01-survival-matrix.md`
- `research_program/synthesis/geometric_indeterminacy_decision.md`
- `research_program/work_packages/wp4_two_point_theorem.md`
- `research_program/models/first_witness_pair_candidates.md`
- `research_program/bibliography/next_observable_theory_review.md`
- `dev/PR003_C1_RELATIONAL_SPEC.md`
- `formal/HorizonFormal/`
- `docs/preregistration.md`
- `docs/preregistration_001_addendum.md`
- `docs/preregistration_002.md`
- `docs/estimator_v2_seal.md`
- Local literature under `biblioteca/` and `biblioteca/derived-md/`, including EGS, Surya,
  Benincasa-Dowker and Chevalier.

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief
- Proposed artefact(s): **Revise before normative adoption; no scientific block.** Keep `docs/claim_grammar.md` at `CLAIM_GRAMMAR_DRAFT_READY`, make the minimal wording/state-transition corrections identified below, then produce the scoped follow-up `docs/auditor/auditor_report_014_op02-claim-grammar.md`. Only after `/comite` adoption and that audit passes may the grammar expose `CLAIM_GRAMMAR_ADOPTED`, exactly as required by `docs/plan_operativo_15_julio_2026.md:158-167` and `docs/claim_grammar.md:295-307`. No code, preregistration, threshold, `data/`, `results/`, simulation or PR012 curve artefact belongs to OP-0.2.
- Environment & seal: This is document-only; no sealed scientific environment, external Minz clone or RNG is invoked (`CLAUDE.md:27-29`). Any mechanical repo gates must use the pinned environment `numpy==1.26.4` (`requirements.txt:1-10`; `Makefile:1-17`). Re-verify `make verify-seal` against `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, the current prereg-002 seal (`docs/preregistration_002.md:7-9`), not the historical estimator-v2 instrument hash (`docs/estimator_v2_seal.md:7-12`). Package-diff-clean means `git status --short` remains limited to the three documentary candidates and shows no `nachocausal/`, dependency, threshold or result change; current command output lists exactly those three `??` paths. The chair reports `make test` successful; no scientific rerun is required.
- Provenance capture: Record branch `main`, source HEAD `726c8c1eda16334a1b30b9f4ad82927f0c834382`, UTC audit/adoption timestamps, exact gate commands and exit codes, and the pre-audit content hashes: claim grammar `08a34ea4bc699ba58717718c3ff621a4de740fb0ff4b66c1939360b4affa9c91`, matrix `dfe792ce1df2fbe07fcf8f040d3f53cc047d17b6956e71d214d1386e47f53727`, and audit 013 `d40535a8961d8189450de0a9e949147db2fea78dfa0cd9d237b92110188e5bd2` (`sha256sum ...` output). `pip freeze` and `uname -a` need recording only if mechanical Python gates are rerun; they do not determine documentary semantics. Seed band: `NONE`; no dev, validation or reserved seed is read. Record explicitly that `data/reports/pr012_tv_curve_n8.csv` is absent (`docs/auditor/auditor_report_013_op01-survival-matrix.md:77-86`).
- Run mechanics: One foreground, reversible documentary pre-flight only: validate every `file:line` anchor, confirm no objective is promoted to evidence, run `make verify-seal`, the already-green `make test` if the auditor requires repetition, and validate the resulting reports through `make verify-comite` / `make verify-audit` (`Makefile:28-47`). Abort cleanly on an absent/misrepresented anchor, seal mismatch, nonzero checker/test exit, appearance of code/data/result changes, or any attempted `EMPIRICAL`/`VALIDATED` claim sourced from the absent PR012 curve. No background process is justified. Commit/push and any status promotion are separate committing actions and are not authorized here.
- Reproducibility risks / ambiguities:
  - Audit 013 cannot close OP-0.2: it explicitly says it audits OP-0.1 and “does not authorize OP-0.2” (`docs/auditor/auditor_report_013_op01-survival-matrix.md:9-18`). Therefore `CLAIM_GRAMMAR_ADOPTED` is blocked pending a grammar-specific audit, while committee adoption of a revised candidate may proceed.
  - All three foundations are currently untracked: `git status --short` reports them as `??`, and `git ls-files --error-unmatch <path>` exits `1` for each. The committed HEAD therefore cannot reproduce their content without preserving the hashes above or committing the exact audited versions.
  - The state transition is underspecified: the document says it already “fija” normative vocabulary (`docs/claim_grammar.md:10-15`) while its author, committee and audit gates remain draft/pending (`docs/claim_grammar.md:295-307`). Freeze an explicit progression such as `DRAFT_READY -> COMMITTEE_ADOPTED_AUDIT_PENDING -> ADOPTED`; otherwise a status-only edit after audit changes the audited blob.
  - The permission to write “recupera” after merely “declarar una garantía positiva” (`docs/claim_grammar.md:66-68`) is weaker than the document’s own evidence rule that objectives remain objectives until evidence exists (`docs/claim_grammar.md:12-15,32-45`). Revise it to require an established, anchored guarantee carrying an admissible evidence label before normative adoption.
  - The permitted-form template is syntactically incomplete: `el estimador ... f [nivel de evidencia] el proxy` lacks a verb (`docs/claim_grammar.md:58-64`). Fixing that template is necessary so independent authors can apply the grammar deterministically.

### Mathematician brief
- Computability: A finite causal set is a locally finite **partial**, not total, order (`biblioteca/derived-md/Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md:40-42`). Minimality, futures, future cardinality, longest-chain height, ordering fraction and finite interval/chain counts are decidable from that order. The frozen `τ(n)` gate is intrinsic: `n` counts minimal elements and `improvement(O_min)=1-SSE2/SSE1` uses only order-derived future volumes (`docs/estimator_v2_freeze.md:48-60`). The `T_EDGE_MIN=6` gate instead reads external patch metadata and returns `OUT-OF-DOMAIN`, not estimator abstention or physical FAIL (`docs/estimator_v2_freeze.md:62-70,94-100`). OP-0.2 must require these two gate types separately; `docs/claim_grammar.md:17-27` currently combines abstention and negative terminals without a distinct domain-gate field.
- Order observable: For each minimal element \(i\), the literature diagnostic uses \(h(i)=\max\{|c|:c\text{ is a chain beginning at }i\}\); estimator-v2 replaces this with \(O_{\min}(i)=|\operatorname{Fut}_C(i)|\), the corresponding column sum of the past matrix (`docs/estimator_v2_freeze.md:34-38`). In finite 1+1D Schwarzschild sprinklings, interior futures are truncated because timelike curves reach \(r=0\) in finite proper time, while exterior chains are patch-limited, producing a bimodal transition near the horizon; future cardinality shows the same signal but is explicitly more boundary-sensitive (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-195`). Thus this is a singularity-and-truncation-dependent, family-conditioned signal, not automatically a quasi-local expansion observable or a dimension-transferable horizon invariant.
- Relevant invariants: The ordering fraction is \(r=2R/[n(n-1)]\) and yields the Myrheim–Meyer dimension only for the stated sprinkling ensemble; its fluctuations require ensemble treatment and a matching value does not establish manifoldlikeness (`biblioteca/derived-md/The causal set approach to quantum gravity.md:1001-1015,1054-1082`). Longest-chain height is the standard order proxy for timelike distance (`biblioteca/derived-md/The causal set approach to quantum gravity.md:1221-1233`). Future volume is relabel-invariant but truncation-sensitive (`docs/estimator_v2_freeze.md:34-38`; EGS `derived-md:191-195`). The \(k\)-chain abundances \(C_k\) are finite-poset order invariants with ensemble continuum formulae, not horizon localizers by themselves (`biblioteca/derived-md/The causal set approach to quantum gravity.md:1092-1118,1151-1152`).
- Analytic / continuum target: Three targets must remain disjoint: the global causal horizon \(\mathcal H_c=\partial\operatorname{Past}(\gamma_0)\) for a future-inextendible infinite-proper-length curve (EGS Eq. 9, `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:175-179`); the frozen-family Schwarzschild cut localized by the future-truncation diagnostic (`ibid.:181-195`); and the quasi-local marginal surface defined by \(\Theta_{\rm out}=0\), with Schwarzschild \(\Theta_{\rm out}=r^{-1}(1-2M/r)\) (EGS Eqs. 10-12, `ibid.:197-225`). Density and patch-extension limits must be separate (`docs/claim_grammar.md:70-82`), but the density clause must also specify the experiment sequence: conditioned on fixed \(N=n\), the point law is normalized volume and does not depend on \(rho\) (`research_program/models/first_witness_pair_candidates.md:23-31`), so “\(rho\to\infty\)” at unchanged fixed \(n\) is vacuous.
- Caveats:
  - **Disposition: BLOCK adoption pending revision.** The current document has `CLAIM_GRAMMAR_ANCHOR_FAIL`: the Poisson/scale assertions at `docs/claim_grammar.md:146-158` and the duality assertions at `docs/claim_grammar.md:97-117` lack direct literature or proof anchors, despite the document’s own normative requirement at `docs/claim_grammar.md:17-30`.
  - The duality contract is incomplete for unlabeled poset laws. Because the channel observes isomorphism classes (`research_program/synthesis/survival_matrix_1p1_to_3p1.md:74-76`), relabel-equivariance must be stated. On a self-dual class, that requirement together with `chi_hat(P^op)=-chi_hat(P)` forces `chi_hat=0`; the grammar must declare this forced abstention and require the support map to be well-defined on isomorphism classes (`docs/claim_grammar.md:101-110`).
  - The scale clause must distinguish an unconditioned Poisson sequence, where \(N\sim\operatorname{Poisson}(rho V)\), from a conditional \(n\to\infty\) sequence; fixed \(n\) removes the \(rho V\) count channel (`research_program/work_packages/wp4_two_point_theorem.md:149-157`; `research_program/synthesis/survival_matrix_1p1_to_3p1.md:70-85`).
  - The witness inequality \(TV(P,Q)\geq|\mathbb E_Pf-\mathbb E_Qf|\) for \(0\leq f\leq1\) is correct under \(TV=\sup_A|P(A)-Q(A)|\), and `docs/claim_grammar.md:225-233` supplies a valid layer-cake proof. For `CERTIFIED` use, the grammar should require a simultaneous lower confidence bound after Monte Carlo error, not the raw plug-in expectation gap (`docs/claim_grammar.md:235-238`).
  - The dynamics boundary is correct but must retain its probabilistic scope: sprinkling supplies inherited order and Poisson volume sampling (`biblioteca/derived-md/Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md:40-42`), whereas generic finite-poset/Kleitman–Rothschild dominance and its suppression are separate dynamical questions (`biblioteca/derived-md/Chevalier_2023_Discrete_Causal_Action_and_Holes_in_Spacetime.md:204-213`).

### Mathematical logic brief
- Formal status: `docs/claim_grammar.md` is a normative vocabulary and classification scheme, not a scientific result (`docs/claim_grammar.md:10-45`). Its bounded-witness inequality is an elementary proved lemma (`docs/claim_grammar.md:225-238`). The exact-support identifiability iff and Le Cam bound are proved in prose, while the horizon corollary remains conditional on an unproved adversarial pair (`research_program/work_packages/wp4_two_point_theorem.md:57-140`). The exact 1+1D scale witness proves only `TV=0` for absolute location at fixed `n` (`research_program/models/first_witness_pair_candidates.md:62-105`). Lean proves the old interface empty, the one-way no-escape property, and a corrected nonempty witness; it proves no physical horizon or duality claim (`formal/HorizonFormal/HorizonFormal/Horizon.lean:110-125`, `:195-249`). The 3+1D target, dual closure, positive witness, limits, alternatives, and selector remain open blockers (`research_program/synthesis/survival_matrix_1p1_to_3p1.md:174-187`).
- Quantifier / dependency order: Before data, choose the generative family, patch/extension rule, channel, target/output/loss, dual action, estimator or witness, alternatives, probability law, and abstention rule (`docs/claim_grammar.md:17-30`, `:235-246`). The duality equations omit the required `forall P in G_dual`, the type and coherence of `iota_P`, compatibility with relabellings, and whether equality is pointwise or in law for randomized estimators (`docs/claim_grammar.md:97-111`). Anti-equivariance also forces `chi_hat(P)=0` on a literally self-dual input, so self-dual cases and abstention must be specified before adoption (`docs/claim_grammar.md:101-110`).
- Equivalence claims: The only relevant proved iff is exact zero-error identifiability iff the target is constant on every support-compatible class (`research_program/work_packages/wp4_two_point_theorem.md:57-79`). The proposed duality equalities are explicitly `TARGET`, not theorems (`docs/claim_grammar.md:101-111`). The TV witness argument proves only `TV(P,Q) >= |E_P f-E_Q f|`; it proves neither equality nor witness optimality and requires both laws on one common measurable experiment (`docs/claim_grammar.md:225-238`). Likewise, `TV <= epsilon` yields a target-recovery floor only after naming models with distinct targets and the relevant loss separation, as required by the actual two-point theorem (`research_program/work_packages/wp4_two_point_theorem.md:81-124`); the unrestricted wording at `docs/claim_grammar.md:221-223` is too strong.
- Type / object discipline: `RelationalHorizon R` is a set of ordered cover pairs, not an event horizon or a set-valued geometric localizer (`formal/HorizonFormal/HorizonFormal/Horizon.lean:38-68`; `dev/PR003_C1_RELATIONAL_SPEC.md:30-37`). `IdealEnd` is a subtype of non-principal `Order.Ideal`, while `ChainEndInIdeal` is a quotient of nonterminal cofinal chains and `ChainEnd` packages that quotient with an ambient ideal; these objects are not interchangeable (`formal/HorizonFormal/HorizonFormal/Ends.lean:7-23`; `formal/HorizonFormal/HorizonFormal/ChainEnds.lean:157-201`). The grammar also overloads `P` between a realized poset and membership in a generative/geometric family; the dual operation must be typed separately at model, law, labeled-poset, and isomorphism-class levels before `iota_P(H_hat(P))` is well formed (`docs/claim_grammar.md:97-110`; `research_program/work_packages/wp4_two_point_theorem.md:29-47`).
- Caveats:
  - Adoption must be blocked for revision: the permitted TV-upper-bound sentence omits target separation, and the duality contract is not yet a closed quantified proposition. The current applicable terminal is `CLAIM_GRAMMAR_OVERCLAIM`, not `CLAIM_GRAMMAR_ADOPTED` (`docs/claim_grammar.md:221-223`, `:295-307`).
  - Add a common-sample-space clause to the witness lemma and explicit model/target/loss hypotheses to every minimax consequence; otherwise the grammar permits `TV` comparisons across incompatible `fixed_n` experiments despite separately prohibiting that move (`docs/claim_grammar.md:139-170`, `:221-238`).
  - The terminal system is not exhaustive: incompleteness of quantifiers/types is neither an anchor failure nor necessarily an evidentiary overclaim, so a defective grammar can evade both negative terminals. Add an explicit incompleteness/revision terminal and a precedence rule before the committee/auditor adoption sequence (`docs/plan_operativo_15_julio_2026.md:158-167`; `docs/claim_grammar.md:295-307`).

### Physicist brief
- **Coordinates & patch:** **Revise before adoption.** OP-0.2 is document-only, but its mandatory fields must add the coordinate chart and physical patch construction: the existing benchmark uses 1+1D Schwarzschild in ingoing Eddington–Finkelstein coordinates, with the frozen finite box `t in [0,6]`, `r in [0.1,1.3]`, and `r_S=2M=0.5` (`docs/preregistration.md:59-65`; `docs/preregistration_001_addendum.md:35-45`). The draft requires a patch and extension rule but omits coordinates from its nine-field contract (`docs/claim_grammar.md:17-27`). Finiteness removes future null infinity and therefore any direct global event-horizon identification; exterior futures are box-limited (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:171-193`).
- **Physical meaning of the signal:** The established order signal is a **singularity-truncation proxy**, not yet a trapping observable: interior timelike futures terminate at `r=0`, exterior futures terminate mainly at the box boundary, producing longest-chain/future-cardinality bimodality with a transition near `r=2M` (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-195`). In Schwarzschild, `Theta_out=(1/r)(1-2M/r)` changes sign at `r=2M`, where apparent, Killing, and event horizons coincide, but the 1+1D toy model has no spatial two-surfaces and cannot compute the true null expansion; it uses a one-dimensional distance proxy (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:221-230`). The grammar must keep these two physical mechanisms distinct.
- **Sprinkling domain:** Require a finite-region natural-volume Poisson process, `N~Poisson(rho V)` and `ell=rho^(-1/d)`; this is the construction stated by EGS (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:102-115`). For the frozen benchmark, `{1500,3000,6000,12000}` are expected-count levels `lambda`, with `rho=lambda/7.2`, not four physical densities stated independently of the patch (`docs/preregistration_001_addendum.md:39-62`). The draft correctly separates `fixed_n` from `order+number` and density from patch limits (`docs/claim_grammar.md:70-82,135-164`), but must require those quantities and units in every Schwarzschild claim.
- **Claim boundary:** Physicist verdict: **REVISE_BEFORE_ADOPTION, not block**. Preserve the draft’s teleology, scale, ensemble, and dynamics rules, but add: coordinate/chart declaration; literal `NO_RECONSTRUCTION_CLAIM`; an explicit choice between `(a)` localisation of the singularity-truncation cut in the frozen singular-Schwarzschild family and `(b)` a separately defined quasi-local expansion/trapping proxy; 1+1D-only scope; and the regular-black-hole caveat. No wording may promote either proxy to metric reconstruction, a global/asymptotic event horizon, a true marginally trapped surface, or a 3+1D result (`docs/claim_grammar.md:47-91`; `docs/preregistration_001_addendum.md:75-107`).
- **Caveats:**
  - The longest-chain/future-cardinality bimodality is specific to geodesically incomplete singular Schwarzschild and is expected to fail for regular Hayward-type black holes, where interior timelike curves need not terminate; an expansion-based diagnostic is a different candidate that may survive (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:195-230`).
  - `P^op` reverses the causal arrow, but BH/WH anti-equivariance has physical content only after freezing a time-oriented BH/WH family, its time-reversed continuation, the support identification, and the sign convention. The draft correctly leaves its equations as `TARGET`, but should state these physical prerequisites explicitly (`docs/claim_grammar.md:93-124`).
  - A density ladder at fixed patch can sharpen a finite-patch proxy but cannot recover the missing asymptotic continuation; density and patch limits must remain separate (`docs/claim_grammar.md:70-82`; `research_program/synthesis/geometric_indeterminacy_decision.md:355-387`).
  - Sprinkling a prescribed Schwarzschild geometry establishes only conditional kinematic recoverability. It neither derives manifoldlikeness nor shows that causal-set dynamics selects Schwarzschild; EGS calls sprinkling an auxiliary construction, while the draft’s dynamics terminal correctly preserves this separation (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:102-119`; `docs/claim_grammar.md:250-275`).

## 5. Falsifier attack

### Falsifier attack
- Concrete failure modes: `DECISION=REVISE_BEFORE_ADOPTION`. (1) La forma supuestamente permitida carece de verbo (`docs/claim_grammar.md:60-64`) y la corrección implícita permite escribir `recupera` tras meramente **declarar**, no establecer, una garantía positiva (`docs/claim_grammar.md:66-68`), contradiciendo la regla que distingue objetivos de resultados (`docs/claim_grammar.md:12-15`). (2) El contrato dual no cuantifica sobre `P`, no tipa `iota_P`, no exige `iota_{P^op} o iota_P = id`, no cubre equivariancia por relabeling ni estimadores aleatorios/en ley; además, para un objeto autodual sus propias ecuaciones fuerzan `chi_hat=0`, pero no se prescribe `0` o abstención (`docs/claim_grammar.md:97-111`). (3) `TV(P,Q) >= |E_P f-E_Q f|` necesita que `P,Q` vivan en un experimento medible común y que sus targets estén separados bajo la pérdida; sin esto certifica distinguibilidad, no recoverability. La mención de cobertura simultánea no define una cota inferior computable con IC ni su terminal de fallo (`docs/claim_grammar.md:214-238`), mientras la matriz exige cerrar target/pérdida y alternativas (`research_program/synthesis/survival_matrix_1p1_to_3p1.md:174-185`). (4) `rho -> infinity` puede ser vacuo bajo `fixed_n` si no se declara cómo crece `n`; la plantilla de límites no fija el canal ni la secuencia de experimentos (`docs/claim_grammar.md:70-77`, `:139-148`, `:189-199`). (5) Los nueve campos obligatorios omiten dimensión/carta, truncación singular frente al target, y la distinción entre exclusión del dominio generativo y abstención del estimador (`docs/claim_grammar.md:17-27`); esos riesgos ya aparecen como dependencia de carta, truncación y bulk/domain frente a abstención (`research_program/synthesis/survival_matrix_1p1_to_3p1.md:93-99`, `:108-116`, `:160-168`). Tampoco hay regla de transición entre etiquetas de evidencia (`docs/claim_grammar.md:32-45`) ni terminal para gramática incompleta (`docs/claim_grammar.md:303-307`; `docs/plan_operativo_15_julio_2026.md:163-167`).
- Ground-truth leakage: La lista normativa exige declarar el uso permitido del embedding (`docs/claim_grammar.md:17-27`), pero la plantilla publicable lo elimina y solo pide target/salida/pérdida (`docs/claim_grammar.md:277-293`). Así, un target, carta, frontera o regla de dominio derivados del embedding podría guiar el observable y aun completar literalmente la plantilla. Debe exigirse que embedding/coordenadas entren únicamente en scoring y nunca en construcción, selección, abstención o frontera, coherente con el contrato order-only existente (`dev/PR003_C1_RELATIONAL_SPEC.md:10-14`).
- Freeze violations: OP-0.2 es documental y no ejecuta directamente código, datos ni semillas (`docs/plan_operativo_15_julio_2026.md:111-114`). Sin embargo, “convención congelada antes de datos” y “testigo preespecificado” no exigen artefacto versionado, SHA, fecha de freeze, población reservada ni transición autorizada (`docs/claim_grammar.md:121-124`, `:235-246`); una elección posterior a exploración podría recibir esas etiquetas retrospectivamente. La adopción debe bloquearse hasta que la gramática defina el estado anterior, la evidencia necesaria y el acto auditable de promoción.
- Verdict coercion: La plantilla nombra abstención pero no establece que prevalece sobre cualquier PASS/FAIL ni separa `OUT_OF_DOMAIN`, fallo del generador, fallo numérico y abstención del estimador (`docs/claim_grammar.md:277-293`). Esto deja abierta la coerción que OP-0.1 preservó explícitamente para `GRID_RESOLUTION_ABSTAIN` y `NO_INTERFACE` (`research_program/synthesis/survival_matrix_1p1_to_3p1.md:151`, `:168`; `docs/auditor/auditor_report_013_op01-survival-matrix.md:118-120`). Además, una gramática incompleta solo puede caer artificialmente en overclaim o anchor-fail porque no existe `CLAIM_GRAMMAR_INCOMPLETE` (`docs/claim_grammar.md:303-307`).
- Premature / over-broad claims: El documento no presenta por sí mismo un resultado 3+1D (`docs/claim_grammar.md:5-15`), pero su regla permitiría promover a “recupera” una separación TV meramente declarada, incluso sin pérdida geométrica ni separación de targets. Eso excede tanto la distinción testigo/localizador (`docs/claim_grammar.md:235-246`) como los bloqueos 3+1D aún abiertos (`research_program/synthesis/survival_matrix_1p1_to_3p1.md:174-187`). Deben añadirse campos explícitos de dimensión y clase de BH, incluida la salvedad regular/singular; la necesidad específica de esta última queda `[UNVERIFIED]` en el dossier.
- Independent-falsification gate: No está satisfecho: el propio candidato declara `/comite=PENDING` y `/auditor=PENDING` (`docs/claim_grammar.md:295-301`), y el plan exige ambos gates antes de adopción (`docs/plan_operativo_15_julio_2026.md:158-167`). La identidad del autor y si sería su único verificador no consta en el dossier `[UNVERIFIED]`. Veredicto: revisión obligatoria y nueva ronda independiente antes de `CLAIM_GRAMMAR_ADOPTED`.
- Minimal falsification test: Ejecutar `bash -c "! rg -q 'después de declarar una garantía positiva' docs/claim_grammar.md && rg -q 'CLAIM_GRAMMAR_INCOMPLETE' docs/claim_grammar.md"`; el candidato actual debe devolver código distinto de cero porque conserva el criterio débil en `docs/claim_grammar.md:66-68` y carece del terminal de incompletitud en `docs/claim_grammar.md:303-307`.

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: BLOCK
- Freeze status: N/A for numerical thresholds: OP-0.2 is explicitly document-only, with no code or simulations (`docs/plan_operativo_15_julio_2026.md:111-114`), but the grammar is still `COMMITTEE_PENDING` and its adoption/audit gates remain pending (`docs/claim_grammar.md:3-8`, `docs/claim_grammar.md:295-307`); it must be revised before it is frozen for future texts.
- Seal integrity: The proposed documentary step does not run or modify the sealed validation path. The live `nachocausal/thresholds.py` SHA256 is `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching the operative prereg-002 seal (`docs/preregistration_002.md:7-12`); the earlier addendum seal was superseded through the documented reseal sequence (`docs/estimator_v2_seal.md:52-59`).
- Seed discipline: No seed band is used or burned by OP-0.2. The prereg-002 dev and held-out bands are documented as disjoint (`docs/preregistration_002.md:14-33`), and the historical held-out evaluation and later reverification are already disclosed (`docs/preregistration_002_result.md:3-16`).
- Reporting rule: Report this `BLOCK` and the required revision without coercion into adoption. Any future confirmatory outcome remains subject to report-alike, no retuning, no fresh-seed rerun and no threshold loosening (`docs/preregistration_002.md:59-68`).
- Forbidden moves present? No threshold tuning, seal change, seed reuse, validation rerun or ground-truth access is proposed. Adoption of the current draft would nevertheless permit a recoverability over-claim because `recupera` is licensed after an underspecified “garantía positiva” (`docs/claim_grammar.md:60-68`) despite the document's own mandatory target/loss/regime fields (`docs/claim_grammar.md:17-30`).
- Reasons:
  - The duality contract lacks explicit quantification and complete typing of `P`, `P^op`, `iota_P`, `H_hat` and their codomains, so its equations are not yet a fail-closed normative rule (`docs/claim_grammar.md:97-111`).
  - The TV witness clause does not require a common measurable sample space or state the confidence-valid lower endpoint whose positivity licenses a separation claim; it only lists coverage and Monte Carlo ingredients (`docs/claim_grammar.md:225-238`).
  - The grammar does not yet make the frozen chart/patch contract mandatory, although the source program requires patch and coordinates to be frozen independently (`research_program/synthesis/geometric_indeterminacy_decision.md:316-320`).
  - The grammar omits the operational `OUT_OF_DOMAIN` reporting category already established as distinct from physical FAIL (`docs/preregistration_002.md:43-57`) and does not require controls separating trapping sensitivity from boundary, density and singularity effects (`research_program/bibliography/next_observable_theory_review.md:169-176`).
  - The state machine has no explicit revision-required terminal between `CLAIM_GRAMMAR_DRAFT_READY` and adoption; its listed effective terminals cover only adoption, overclaim and anchor failure (`docs/claim_grammar.md:295-307`).

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| Eichhorn–Gamito–Stokes, *Towards black-hole horizons and geodesic focusing in causal sets*, §II, Eq. (4), derived-md lines 102–119 | Causet mathematician — sprinklings are Poisson samples of a continuum region, inherit its causal order, and discard embedding data afterward | CONFIRMED |
| Eichhorn–Gamito–Stokes, §III, derived-md lines 171–175 | Physicist — the event horizon is the boundary of the causal past of future null infinity and its direct causal-set definition requires an infinite sprinkling | CONFIRMED |
| Eichhorn–Gamito–Stokes, §III, Eq. (9), derived-md lines 175–179 | Physicist — the cited causal horizon is defined as the boundary of the past of a future-inextendible curve of infinite proper length | CONFIRMED |
| Eichhorn–Gamito–Stokes, §III, derived-md lines 181–193 | Physicist — finite-patch longest-chain and future-cardinality diagnostics obtain their interior/exterior signal from finite proper-time termination at the singularity and are boundary-sensitive | CONFIRMED |
| Eichhorn–Gamito–Stokes, §III–IV, derived-md lines 195–201 | Physicist — the singularity-truncation partition is expected to fail for regular Hayward-type black holes, motivating a trapping/expansion diagnostic | CONFIRMED |
| Eichhorn–Gamito–Stokes, §IV, Eqs. (10)–(12), derived-md lines 201–225 | Physicist — trapped surfaces have both future-null expansions negative, while in Schwarzschild \(Theta_{out}=0\) at \(r=2M\), coincident with the apparent and event horizons | CONFIRMED |
| Eichhorn–Gamito–Stokes, §IV, derived-md lines 199–225 | Physicist — the pointwise symmetry-sphere trapping target is independent of foliation | UNCONFIRMED |
| Chevalier, *Discrete Causal Action and Holes in Spacetime*, §2.2, Conjecture 2.2.1, derived-md lines 196–202 | Causet mathematician — the Hauptvermutung is an unproved approximate-uniqueness conjecture, supported by continuum limits of order invariants | CONFIRMED |
| Chevalier, §2.3, derived-md lines 204–213 | Causet mathematician / claim grammar §8 — asymptotically typical finite orders are KR-type and suppressing their non-manifoldlike entropic dominance is a separate dynamics problem | CONFIRMED |
| Benincasa–Dowker, *The Scalar Curvature of a Causal Set*, derived-md lines 40–42 | Causet mathematician — a causal set is a locally finite partial order and sprinkling is a Poisson process with expected count \(rho V\), with order inherited from the manifold | CONFIRMED |
| Surya, *The causal set approach to quantum gravity*, §4.1, Eq. (14), derived-md lines 1001–1015 | Causet mathematician — ordering fraction is an order invariant whose ensemble expectation supplies the Myrheim–Meyer dimension estimator | CONFIRMED |
| Surya, §4.1, derived-md lines 1054–1082 | Causet mathematician — ordering-fraction fluctuations obstruct inference from one realization at finite density, and matching this statistic alone establishes neither manifoldlikeness nor full geometric recovery | CONFIRMED |
| Surya, §4.1, Eq. (19), derived-md lines 1092–1118 and 1151–1152 | Causet mathematician — \(k\)-chain abundances yield dimension estimators and are finite-causet order invariants | CONFIRMED |
| Surya, §4.3, Eqs. (21)–(22), derived-md lines 1221–1246 | Causet mathematician — longest-chain length is the discrete timelike-distance candidate, with an ensemble asymptotic and large finite-density fluctuations | CONFIRMED |

- Notes: EGS supports the local expansion formulas and the coincidence at \(r=2M\), but the cited passage does not establish that a symmetry-sphere target is foliation-independent; that stronger clause needs a separate geometric source or proof. All explicit literature claims in `docs/claim_grammar.md` are otherwise supported by the located sources.

## 8. Synthesis

The committee unanimously supports the purpose and six scientific boundaries of OP-0.2, but no
role supports adoption of the current blob. Reproducibility, mathematics, logic and physics all
return `REVISE_BEFORE_ADOPTION`; the preregistration warden emits `BLOCK`; the falsifier supplies a
minimal test that the draft currently fails. Therefore the committee cannot emit a proceed or
adoption verdict.

Required corrections, in precedence order:

1. close the evidence/state machine and require an established, anchored positive guarantee before
   using recovery language;
2. type and quantify duality over a dual-closed family, including relabeling, involution coherence,
   randomized estimators and self-dual abstention;
3. add common-experiment, distinct-target/loss and confidence-valid lower-bound hypotheses to TV
   claims;
4. distinguish fixed-`n`, Poisson and asymptotic experiment sequences;
5. make dimension, coordinate chart, physical patch, embedding-only-scores and the precise
   singularity-truncation versus trapping target mandatory;
6. separate `OUT_OF_DOMAIN`, generator/numerical failure and estimator abstention with precedence;
7. add a fail-closed incomplete/revision state and auditable content-hash transition.

The only literature dissent is narrow: EGS does not support the stronger proposition that the
pointwise symmetry-sphere trapping target is foliation-independent. That clause must remain absent
or receive a separate proof/source. No other cited literature claim was rejected.

## 9. Next-step spec

**Reversible revision, only after user sign-off:**

1. Patch `docs/claim_grammar.md` only; no code, data, result, threshold or preregistration file.
2. Replace the malformed allowed template and require an established evidence label plus anchored
   positive guarantee before `recupera`.
3. Expand mandatory fields with dimension/chart, target mechanism/class, embedding-only-scores,
   domain gate, estimator abstention and terminal precedence.
4. Replace the duality sketch with a typed `TARGET` proposition on unlabeled isomorphism classes:
   explicit universal quantifier, support/relabel map, involution coherence, deterministic versus
   in-law form, and forced `chi=0`/abstention for self-dual cases.
5. State TV upper-bound consequences only for named models with separated targets/loss; state the
   witness lower bound only on a common measurable experiment and require a simultaneous
   confidence lower endpoint above zero for a certified separation claim.
6. Specify density and patch sequences per channel; prohibit `rho -> infinity` at unchanged
   `fixed_n`.
7. Separate singularity-truncation localization, quasi-local trapping proxy and global event
   horizon; add 1+1D/regular-BH caveats and literal `NO_RECONSTRUCTION_CLAIM`.
8. Add `CLAIM_GRAMMAR_INCOMPLETE` and state progression
   `DRAFT_READY -> COMMITTEE_ADOPTED_AUDIT_PENDING -> ADOPTED`, recording content hash at each gate.
9. Run the falsifier's minimal text test and structural anchor checks; both must pass.
10. Reconvene `/comite` on the revised blob. Only if it removes the `BLOCK`, run the scoped
    `/auditor` and consider `CLAIM_GRAMMAR_ADOPTED`.

**Committing steps:** commit/push, status promotion to `ADOPTED`, and any use of this grammar as a
freeze require separate explicit user authorization. OP-0.2 authorizes no science execution.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off

Signed: Nacho / PI

Date: 2026-07-15

Decision: authorize the reversible revision in §9 and reconvene `/comite`; no commit, push,
scientific execution or status promotion is authorized by this sign-off.
