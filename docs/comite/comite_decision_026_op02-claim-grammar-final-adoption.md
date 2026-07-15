# Comité Decision 026 — OP-0.2 claim grammar final adoption

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Does `docs/claim_grammar.md`, SHA256
`7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786`, close all OP-0.2
committee blockers and qualify for `COMMITTEE_ADOPTED_AUDIT_PENDING`?

## 2. Verified state

- Branch `main`; source HEAD `726c8c1eda16334a1b30b9f4ad82927f0c834382`.
- Candidate SHA256 recomputed before both committee waves:
  `7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786`.
- Signed decision 025 authorizes the three corrections, this reconvening and the scoped auditor
  after committee adoption (`docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md`
  §11).
- Candidate remains documentary and adds no estimator, threshold, measurement or result
  (`docs/claim_grammar.md:3-19`).
- Live seal is unchanged at
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- Structural checks before dispatch: 17 anchors, zero missing files/ranges; whitespace clean;
  required dual/loss/1+1D clauses present; overlap counterexample reproduced and explicitly barred.
- No code, data, result, threshold, preregistration or seed changed or ran.

## 3. Dossier

- `docs/claim_grammar.md` at exact hash above
- `docs/comite/comite_decision_024_op02-claim-grammar-adoption.md`
- `docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md`
- `docs/auditor/auditor_report_013_op01-survival-matrix.md`
- `research_program/synthesis/survival_matrix_1p1_to_3p1.md`
- `research_program/work_packages/wp4_two_point_theorem.md`
- `research_program/synthesis/geometric_indeterminacy_decision.md`
- `research_program/models/first_witness_pair_candidates.md`
- EGS, Surya, Benincasa-Dowker and Chevalier sources under `biblioteca/derived-md/`

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief
- Proposed artefact(s): The three committee-025 residuals are closed. `/comite` may place the exact `docs/claim_grammar.md` blob SHA256 `7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786` into `COMMITTEE_ADOPTED_AUDIT_PENDING`. The next artefact is a scoped OP-0.2 auditor report over that identical hash; only that report may emit final `CLAIM_GRAMMAR_ADOPTED` (`docs/claim_grammar.md:415-442`).
- Environment & seal: The candidate remains `DOCUMENT_ONLY / NO_NEW_RESULT` and explicitly adds no theorem, measurement or estimator property (`docs/claim_grammar.md:3-19`). Current `git status --short` lists only five untracked documentary paths; no code, package, threshold, `data/`, `results/` or preregistration path changed. No scientific environment, RNG or seed band is involved. The last recorded live seal is `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, with no code, data, result, threshold, seed or scientific execution in the authorized revision (`docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md:15-30`).
- Provenance capture: Record branch `main`, source HEAD `726c8c1eda16334a1b30b9f4ad82927f0c834382`, predecessor hashes `08a34ea4bc699ba58717718c3ff621a4de740fb0ff4b66c1939360b4affa9c91` and `434b95d6a1fdd3fc9f44d5831447425412cbbc10807add06c682734d97d5a534`, current adopted-candidate hash `7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786` (`sha256sum docs/claim_grammar.md`), committee decision and UTC timestamp. Committee 025 records PI authorization for exactly the three corrective clauses, reconvening on the new hash and a subsequent scoped auditor, while withholding commit, push and scientific execution (`docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md:149-175,181-189`). `pip freeze`, `uname -a` and seeds are not operative for this documentary transition; seed band is `NONE`.
- Run mechanics: No scientific invocation or background process. The reconvened committee must record the exact `7b28c14c...` hash without editing the blob. The scoped auditor then recomputes that hash, checks all anchors and claim boundaries, and emits the final terminal externally; the grammar forbids a post-audit state edit that would change the audited blob (`docs/claim_grammar.md:415-442`). Any byte mismatch, missing anchor, incomplete type/gate or overclaim aborts fail-closed. Commit and push remain separate, explicitly unauthorized actions.
- Reproducibility risks / ambiguities:
  - The duality residual is closed: labeled representatives `Rep_K`, quotient `Omega_K`, map `q`, representative/class dual maps, relabel-equivariant support behavior and `Law_K(Dg)=d_#Law_K(g)` are now typed separately (`docs/claim_grammar.md:127-166`).
  - The generic-loss residual is closed: the direct theorem is restricted to exact 0-1 recovery, while generic loss requires disjoint frozen success regions or another proved binary reduction; the metric `Delta_T/2` reduction is stated explicitly (`docs/claim_grammar.md:284-304`).
  - The dimensional residual is closed literally: the 1+1D toy lacks the codimension-two spatial surfaces required for true null expansion and uses one-dimensional inter-geodesic distance only as a proxy (`docs/claim_grammar.md:83-97`).
  - Documentary safeguards remain complete: evidence promotion requires a versioned hash and independent gate (`docs/claim_grammar.md:39-55`), and result claims must declare embedding-only scoring, domain gate, abstentions, terminal precedence and `NO_RECONSTRUCTION_CLAIM` (`docs/claim_grammar.md:369-405`).
  - Residual durability risk is non-blocking for committee adoption: `git ls-files --error-unmatch docs/claim_grammar.md` exits `1`, so the blob remains untracked and can be lost until a later authorized commit. The exact hash nevertheless fixes its identity for `COMMITTEE_ADOPTED_AUDIT_PENDING`; final normative use should not precede the scoped audit and durable commit.

### Mathematician brief
- Computability: The normative objects remain decidable from a finite partial order: minimal elements, futures, longest-chain height, interval/chain counts and ordering fraction (`biblioteca/derived-md/Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md:40-42`). Domain failure, numerical abstention and estimator abstention remain correctly separated and ordered before scientific PASS/FAIL (`docs/claim_grammar.md:369-384`).
- Order observable: The current longest-chain/future-cardinality signal remains explicitly a finite-patch, singularity-truncation diagnostic (`docs/claim_grammar.md:83-91`; `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-195`). The added literal caveat is correct: 1+1D has no spatial two-surfaces carrying the true null expansion of a 3+1D symmetry sphere, and EGS substitutes one-dimensional inter-geodesic distance as an expansion proxy (`docs/claim_grammar.md:93-97`; EGS `derived-md:214-230`). The residual dimensional-proxy blocker is closed.
- Relevant invariants: Dualization is now correctly defined first on labeled representatives, `d_rep(P)=P^op`, and then on isomorphism classes by `d([P])=[P^op]`; this descent is well-defined because an order isomorphism also induces an isomorphism of the dual orders (`docs/claim_grammar.md:127-139`). Set-valued outputs remain representative-level and relabel-equivariant, while scalar invariants descend to the quotient (`docs/claim_grammar.md:137-150`). The observed-law condition `Law_K(Dg)=d_#Law_K(g)` correctly connects model reversal to the channel distribution (`docs/claim_grammar.md:141-152`).
- Analytic / continuum target: The generic-loss extension of the two-point argument is now mathematically sound. Exact 0-1 recovery uses the proved distinct-target theorem directly (`docs/claim_grammar.md:284-288`; `research_program/work_packages/wp4_two_point_theorem.md:81-124`). For general loss, the revised grammar freezes the two `delta`-success regions and permits the TV reduction only when they are disjoint or another binary reduction is proved (`docs/claim_grammar.md:290-304`). For metric loss, `delta<Delta_T/2` makes the target balls disjoint by the triangle inequality; the nearest-target classifier then yields the corresponding tail and expected-risk bounds (`research_program/synthesis/geometric_indeterminacy_decision.md:214-234`). The prior generic-loss blocker is closed.
- Caveats:
  - **Disposition: adopt this exact hash at committee level, pending the independent auditor.** `sha256sum docs/claim_grammar.md` returned `7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786`. The mathematically correct next state is `COMMITTEE_ADOPTED_AUDIT_PENDING`, not final `CLAIM_GRAMMAR_ADOPTED` (`docs/claim_grammar.md:407-442`); committee 025 authorizes reconvening and the subsequent auditor only after committee adoption (`docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md:181-189`).
  - The duality proposition now quantifies over `Rep_K`, not quotient classes, and includes the quotient map, class involution, law pushforward, coherent support bijections, relabel-equivariance, randomized semantics and deterministic self-dual abstention (`docs/claim_grammar.md:127-166`). For concrete instantiations, `iota_P` should be the canonical identity on the shared carrier or an explicitly natural relabel-compatible bijection; the universal representative-level equations and relabel-equivariance already make this auditable rather than an adoption blocker.
  - The TV lower-witness clause remains one-way and confidence-valid: common measurable space, bounded witness, simultaneous expectation intervals and positive `L_gap` are all required (`docs/claim_grammar.md:306-328`). It cannot be promoted into a geometric localizer without the separate target/output/loss contract.
  - No remaining causal-set or order-theoretic incompleteness requires `CLAIM_GRAMMAR_INCOMPLETE`; final adoption remains contingent only on the hash-specific anchor and claim-boundary audit required by the state machine (`docs/claim_grammar.md:415-442`).

### Mathematical logic brief
- Formal status: The candidate is a normative grammar, not a theorem or scientific result (`docs/claim_grammar.md:14-19`). Its duality equations remain correctly typed as `TARGET`; no existing estimator is promoted (`docs/claim_grammar.md:154-166`). Committee 025 sign-off authorizes these corrections, reconvening, and a subsequent scoped audit only after committee adoption (`docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md:181-189`).
- Quantifier / dependency order: The class/representative defect is closed. `Rep_K`, `Omega_K`, the quotient map `q`, representative duality `d_rep`, and quotient involution `d` are separated before the universal proposition quantifies over representatives (`docs/claim_grammar.md:127-160`). The model involution is now connected to observation through `Law_K(Dg)=d_#Law_K(g)`, while support coherence, relabel-equivariance, randomized coupling, and self-dual abstention are frozen before any duality claim (`docs/claim_grammar.md:141-166`).
- Equivalence claims: The deterministic equations are universal over admissible representatives and descend consistently through relabel invariance; self-duality therefore forces the scalar character to zero, not BH or WH (`docs/claim_grammar.md:149-166`). The exact 0-1 two-point consequence is correctly restricted to distinct targets (`docs/claim_grammar.md:284-288`). For generic loss, the grammar now requires frozen acceptable regions and either their disjointness or another proved binary-test reduction; it explicitly rejects distinct targets alone as sufficient and records the metric nearest-target special case (`docs/claim_grammar.md:290-304`; `research_program/synthesis/geometric_indeterminacy_decision.md:214-234`).
- Type / object discipline: A carrier-valued localizer lives on labeled representatives and is relabel-equivariant; an invariant scalar descends to isomorphism classes (`docs/claim_grammar.md:127-150`). The bounded witness remains a scalar `f:Omega->[0,1]` supplying only a TV lower bound and confidence endpoint; the text expressly denies that this makes `f` a geometric reconstructor and separately requires target/output/loss closure (`docs/claim_grammar.md:306-336`). Thus test witness, localizer, continuous target, discrete output, and loss remain distinct types.
- Caveats:
  - The state machine is logically complete and fail-closed: incompleteness, overclaim, or anchor failure is reachable from every state and dominates adoption; committee and auditor must use the identical blob hash (`docs/claim_grammar.md:407-442`).
  - `sha256sum docs/claim_grammar.md` returns the dossier hash `7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786`; this exact value must be recorded by the adopting committee and independently recomputed by `/auditor`.
  - Mathematical-logic disposition: `COMMITTEE_ADOPTED_AUDIT_PENDING`. No remaining type, quantifier, reduction, state-machine, or witness/localizer defect justifies `CLAIM_GRAMMAR_INCOMPLETE`; final `CLAIM_GRAMMAR_ADOPTED` remains reserved for the hash-specific audit (`docs/claim_grammar.md:415-442`).

### Physicist brief
- **Coordinates & patch:** The reviewed file matches SHA256 `7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786` (`sha256sum docs/claim_grammar.md`). Every future claim must now declare dimension, physical class, chart, patch, truncations, extension rule, channel and experimental sequence (`docs/claim_grammar.md:21-34,386-403`). This closes the finite-patch scope without promoting the existing 1+1D EF box into a universal geometry.
- **Physical meaning of the signal:** The grammar explicitly separates the global event horizon, the singular-Schwarzschild truncation cut, and a separately defined quasi-local expansion/trapping proxy (`docs/claim_grammar.md:57-91`). It also states literally that the 1+1D toy model lacks the spatial two-surfaces required for true 3+1D null expansion and that EGS uses one-dimensional inter-geodesic distance as a proxy (`docs/claim_grammar.md:93-97`; `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:214-230`). The regular-BH limitation of the truncation diagnostic is preserved (`docs/claim_grammar.md:89-91`; EGS:181-201).
- **Sprinkling domain:** Density and patch limits remain correctly separated: Poisson `rho_k` at fixed patch, conditional `n_k` for `fixed_n`, and patch growth with declared resolution and continuation (`docs/claim_grammar.md:99-112,190-231,233-262`). No finite-box density sequence is licensed as convergence to the global event horizon.
- **Claim boundary:** The representative/class duality is now well typed. `Rep_K`, `Omega_K`, the quotient map, representative dualization, induced class involution, model involution and pushforward law are distinct (`docs/claim_grammar.md:127-152`); set-valued outputs remain relabel-equivariant, scalar character descends to classes, and self-dual observations force abstention rather than BH/WH assignment (`docs/claim_grammar.md:154-172`). This gives the duality contract a defensible physical meaning as time reversal within a frozen time-oriented model family, not an automatic quotient of BH and WH.
- **Caveats:**
  - Generic-loss transport is now soundly bounded: direct two-point consequences are restricted to exact 0-1 recovery, while generic loss requires disjoint pre-frozen success regions or another proved binary reduction; metric loss uses `Delta_T` and the nearest-target reduction (`docs/claim_grammar.md:284-304`; `research_program/synthesis/geometric_indeterminacy_decision.md:214-234`).
  - A TV lower bound from a witness remains only evidence of distributional separation, not localisation or reconstruction (`docs/claim_grammar.md:306-336`).
  - Kinematic sprinkling remains explicitly separated from causal-set dynamics, manifold emergence and dynamical selection (`docs/claim_grammar.md:340-367`).
  - Committee 025 authorizes reconvening and, only after committee adoption, the scoped auditor; it authorizes no scientific execution (`docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md:181-188`).
  - **Physicist verdict:** `RECOMMEND_COMMITTEE_ADOPTION_AUDIT_PENDING`; no physics-based block remains.

## 5. Falsifier attack

### Falsifier attack
- Concrete failure modes: `DECISION=COMMITTEE_ADOPTED_AUDIT_PENDING`. No queda un fallo bloqueante en las tres cláusulas atacadas. (1) La gramática separa representantes `Rep_K`, cociente observable `Omega_K`, mapa `q` y dualidades `d_rep/d`, y formula la salida set-valued solo sobre representantes (`docs/claim_grammar.md:127-160`). (2) La involución de modelos queda ligada al canal mediante `Law_K(Dg)=d_#Law_K(g)` (`docs/claim_grammar.md:141-152`), cerrando el contraejemplo donde dualidad algebraica y leyes generativas no coincidían. (3) Para pérdida genérica exige regiones de éxito congeladas y disjuntas, o una reducción binaria demostrada; el caso métrico exige `delta<Delta_T/2` o clasificador al target más cercano (`docs/claim_grammar.md:284-304`; `research_program/synthesis/geometric_indeterminacy_decision.md:214-234`). El anterior contraejemplo con regiones solapadas queda prohibido literalmente.
- Ground-truth leakage: No encuentro una vía permitida. El contrato exige que embedding solo puntúe y aporte evidencia de que no define construcción, selección, abstención o frontera (`docs/claim_grammar.md:386-403`). La dualidad actúa sobre leyes observadas en `Omega_K`, no sobre coordenadas ocultas (`docs/claim_grammar.md:131-152`). Por tanto, el procedimiento EGS que identifica ladders ingoing/outgoing usando embedding no podría presentarse como order-only sin una sustitución intrínseca demostrada (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:480-482`).
- Freeze violations: No se detectan. Toda promoción exige artefacto versionado, hash, fecha, población/familia y gate independiente, y prohíbe preespecificación retrospectiva (`docs/claim_grammar.md:51-55`). La familia dual, canal, mapas, ley y acoplamiento deben congelarse antes de formular el claim (`docs/claim_grammar.md:141-152`), y las regiones de decisión y `delta` se congelan antes de datos (`docs/claim_grammar.md:290-304`).
- Verdict coercion: No se detecta. `FAILED_DATA_CONTRACT`, `OUT_OF_DOMAIN`, abstenciones numérica/del estimador y resultado científico tienen precedencia fail-closed explícita (`docs/claim_grammar.md:371-384`). Las clases autoduales fuerzan `CHARACTER_ABSTAIN_SELF_DUAL`, nunca BH/WH (`docs/claim_grammar.md:163-166`). Una cota TV sin regiones disjuntas tampoco puede coercionarse a imposibilidad bajo pérdida genérica (`docs/claim_grammar.md:298-304`).
- Premature / over-broad claims: La salvedad requerida aparece literalmente: el toy 1+1D no posee las superficies espaciales bidimensionales pertinentes, EGS no calcula expansión nula verdadera ni superficie marginal codimensión dos 3+1D, y usa distancia espacial unidimensional como proxy (`docs/claim_grammar.md:93-97`). Esto coincide con la fuente, que declara que en 1+1D no hay two-surfaces y que no pueden calcularse las expansiones (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:197-230`). Siguen además vigentes `NO_RECONSTRUCTION_CLAIM` y la prohibición de identificar el horizonte global desde patch finito (`docs/claim_grammar.md:68-81`, `:114-121`).
- Independent-falsification gate: Satisfecho en la capa de comité: las tres correcciones resistieron el ataque independiente y el autor no actúa como único verificador en esta reconvocatoria. No equivale todavía a adopción final: el blob mantiene correctamente `COMMITTEE_RECONVENE_PENDING / AUDIT_PENDING`, y su máquina exige auditoría posterior del mismo hash (`docs/claim_grammar.md:407-442`). El SHA verificado es exactamente `7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786`.
- Minimal falsification test: `bash -c 'test "$(sha256sum docs/claim_grammar.md | cut -d" " -f1)" = "7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786" && rg -q "Law_K\(Dg\) = d_# Law_K\(g\)" docs/claim_grammar.md && rg -q "regiones son disjuntas" docs/claim_grammar.md && rg -q "no calcula una expansión nula verdadera" docs/claim_grammar.md'` devolvió código `0`; cualquier deriva del hash o pérdida de una de las tres correcciones hace fallar el control.

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: PASS
- Freeze status: N/A for numerical thresholds: OP-0.2 is document-only and introduces no estimator, threshold or result. The exact candidate SHA256 is `7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786`; PASS authorizes only committee adoption into `COMMITTEE_ADOPTED_AUDIT_PENDING`, not final `CLAIM_GRAMMAR_ADOPTED`, which still requires `/auditor` on the identical blob (`docs/claim_grammar.md:407-442`).
- Seal integrity: The proposed committee action does not run or modify the sealed validation path. The live `nachocausal/thresholds.py` SHA256 remains `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching the operative prereg-002 seal (`docs/preregistration_002.md:7-12`).
- Seed discipline: No dev, validation or reserved seed is generated, read or burned. Decision 025 states that the correction implicates no threshold, seal, seed, implementation or empirical result (`docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md:149-160`), and its signed authorization permits reconvening and a later scoped audit only (`docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md:181-189`).
- Reporting rule: Record committee adoption as `COMMITTEE_ADOPTED_AUDIT_PENDING`; do not report final adoption unless the scoped auditor passes the same hash. Any audit failure must prevail under the grammar's fail-closed terminal order (`docs/claim_grammar.md:415-442`); confirmatory PASS, FAIL, INCONCLUSIVE and OUT_OF_DOMAIN remain report-alike with no retuning or rerun after inspection (`docs/preregistration_002.md:59-68`).
- Forbidden moves present? None. No post-hoc tuning, threshold loosening, ground-truth leakage, validation rerun, reconstruction claim, commit, push or scientific execution is proposed. The PI signed exactly the three corrective edits and reconvening, with audit allowed only after committee adoption (`docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md:162-189`).
- Reasons:
  - The class/representative defect is closed: `Rep_K`, `Omega_K`, quotient `q`, representative dualization and the induced involution on isomorphism classes are now typed separately (`docs/claim_grammar.md:127-140`).
  - The missing generative covariance is closed by the explicit pushforward contract `Law_K(Dg)=d_#Law_K(g)`, together with support involution, relabeling equivariance and randomized-estimator coupling (`docs/claim_grammar.md:141-166`).
  - The TV consequence is now restricted directly to exact 0-1 recovery, while generic loss requires pre-frozen disjoint success regions or another proved binary reduction; the metric special case states the required target separation and threshold (`docs/claim_grammar.md:284-304`).
  - The 1+1D caveat is now literal: no spatial two-surfaces supporting true 3+1D null expansion are available, and the EGS construction is identified as a one-dimensional inter-geodesic-distance proxy rather than a genuine codimension-two marginal surface (`docs/claim_grammar.md:83-97`).
  - Decision 025 declared these three corrections necessary and sufficient, and the signed PI decision authorizes reconvening on the corrected hash and the scoped audit after committee adoption (`docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md:149-173`, `docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md:181-189`).

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| Eichhorn–Gamito–Stokes, *Towards black-hole horizons and geodesic focusing in causal sets*, §III–IV, derived-md lines 181–201 | Causet mathematician / Physicist / grammar §3 — longest-chain and future-cardinality bimodality is a singularity- and finite-boundary-truncation diagnostic that is not expected to transfer directly to regular geodesically complete black holes | CONFIRMED |
| Eichhorn–Gamito–Stokes, §IV, Eqs. (11)–(12), derived-md lines 214–230 | Physicist / grammar lines 93–97 — the 1+1D setting lacks spatial two-surfaces, cannot compute the true null expansions, and instead uses one-dimensional spatial distance between neighboring geodesics as an expansion proxy | CONFIRMED |
| Eichhorn–Gamito–Stokes, §VI, derived-md lines 463–469 | Physicist — the truncation diagnostic is restricted to geodesically incomplete black holes, while the ladder construction is a discrete inter-geodesic-distance counterpart requiring numerous sprinklings for convergence | CONFIRMED |
| Eichhorn–Gamito–Stokes, §II, Eq. (4), derived-md lines 102–119 | Causet mathematician / grammar §§5,8 — sprinkling is a finite-region Poisson construction with \(N\sim\mathrm{Poisson}(rho V)\), \(ell=rho^{-1/d}\), inherited causal order and discarded embedding information | CONFIRMED |
| `research_program/work_packages/wp4_two_point_theorem.md` §3, lines 81–124 | Mathematical logician / grammar lines 284–288 — for exact 0–1 recovery with distinct targets, every order-only estimator has summed error at least \(1-TV\), with equality attainable | CONFIRMED |
| `research_program/synthesis/geometric_indeterminacy_decision.md` §6.2, lines 214–234 | Mathematical logician / grammar lines 290–304 — nearest-target reduction converts the exact binary bound into a metric tail bound at \(Delta_T/2\) and an expected-risk bound \(Delta_T(1-epsilon)/4\) | CONFIRMED |
| `research_program/work_packages/wp4_two_point_theorem.md` §5.2, lines 149–157 | Causet mathematician / grammar §5 — conditioning on common \(N=n\) closes the cardinality channel, whereas unequal Poisson count laws can distinguish unconditioned models | CONFIRMED |
| `research_program/models/first_witness_pair_candidates.md` Lemma 0, lines 23–31 | Causet mathematician / grammar §6 — conditioned on \(N=n\), points are i.i.d. from normalized volume and \(rho\) is absent from the conditional point law | CONFIRMED |
| `research_program/models/first_witness_pair_candidates.md` Theorem A, lines 62–105 | Causet mathematician / grammar §5 — the stated 1+1D dilation pair has exactly equal fixed-\(n\) unlabeled-poset laws while differing in absolute horizon scale | CONFIRMED |
| `research_program/models/first_witness_pair_candidates.md` Remark A3, lines 107–112 | Causet mathematician / grammar §5 — known-\(rho\) order-plus-cardinality reopens scale information through the Poisson count law | CONFIRMED |
| `research_program/work_packages/wp4_two_point_theorem.md` §5.4, lines 170–181 | Mathematical logician / grammar §6 — product-ensemble distinguishability differs from single-instance distinguishability, while the asymptotic in \(n\) remains a separate open problem | CONFIRMED |
| Chevalier, *Discrete Causal Action and Holes in Spacetime*, §2.3, derived-md lines 204–213 | Causet mathematician / grammar §8 — asymptotic KR dominance is non-manifoldlike and its suppression is a separate dynamics problem | CONFIRMED |

- Notes: The exact reviewed blob was verified at SHA256 `7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786`. Lines 93–97 now state exactly the limitation supported by EGS: the 1+1D observable is an inter-geodesic-distance proxy, not a true null expansion or codimension-two marginal surface. Section 7 now correctly restricts the direct exact theorem to 0–1 loss and uses the separate nearest-target reduction for metric loss; it also correctly requires disjoint acceptable regions or another proved binary reduction for generic loss. No remaining literature-dependent overclaim was located.

## 8. Synthesis

All four wave-1 roles recommend committee adoption pending audit. The falsifier finds no remaining
failure mode in the three corrected clauses and marks independent committee falsification
satisfied. The preregistration warden returns `PASS`; every literature-dependent claim is
confirmed. The exact blob therefore enters `COMMITTEE_ADOPTED_AUDIT_PENDING`.

This is committee adoption of a normative documentary grammar, not a scientific result and not
final OP-0.2 adoption. The durability warning remains: the blob is untracked until an explicitly
authorized commit. Its hash fixes the audit object in the meantime.

No dissent remains on type discipline, loss reduction, physical target, channel, duality,
teleology, dynamics, abstention or claim boundary.

## 9. Next-step spec

**Authorized reversible step:** run scoped `/auditor` on exactly
`7b28c14cca7189c185c1085a1e9abb83937cea72acff565fc5366b3a55312786` and verify:

1. byte-identical hash;
2. all `file:line` anchors and literature representations;
3. no objective promoted to result;
4. complete mandatory template, terminal precedence and state machine;
5. no code/data/result/seed/seal change;
6. report checker PASS.

On audit success emit `CLAIM_GRAMMAR_ADOPTED`; otherwise the highest-precedence failure terminal.
Commit, push and scientific execution remain unauthorized.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off

Authorization for the scoped next step is inherited from the signed conditional decision in
`docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md` §11; no additional authority is
claimed here.
