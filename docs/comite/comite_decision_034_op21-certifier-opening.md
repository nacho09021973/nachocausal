# Comité Decision 034 — op21-certifier-opening

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Apertura de OP-2.1 — certificador positivo de referencia
(`docs/plan_operativo_15_julio_2026.md:313-336`). El PI ha instruido "Inicia OP-2.1 según el plan
operativo"; la decisión 033 §9.6 exige "a separate committee decision and PI authorization" antes
de abrirlo — esta sesión de comité es esa decisión. ¿Debe abrirse OP-2.1 ahora, y con qué alcance
exacto: (a) ubicación del módulo en el repo y su interfaz (dos streams de `f(C) ∈ [0,1]` → cota
inferior unilateral auditable de TV según OP-1.3 §3); (b) verificaciones mínimas del plan (leyes
sintéticas con TV conocida; cobertura; reproducibilidad; multiplicidad; optional stopping si
aplica; abstención por precisión/recursos; prueba de que el estimador de intervalo no consume
información geométrica); (c) qué seeds/datos puede tocar; (d) uso de PR011 exclusivamente como
banco de integración; (e) prohibiciones explícitas (sin confirmación física nueva, sin tocar
seal/`thresholds.py`/seeds de validación, sin abrir PR012/PR013, sin código 3+1D)?

## 2. Verified state

Facts checked **this session** (2026-07-15) by the chair, each with its command / file:line:

- `make verify-seal` → `thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` — matches the prereg-002
  frozen seal (`docs/preregistration_002.md:6-8`).
- `git rev-parse HEAD origin/main` → both `016be8b4054caf24f989f71ddf93befe9e3f62eb`
  ("docs: close phase 1 theory gate"); `git status --porcelain` → clean worktree.
- `sha256sum` over the eleven pre-decision paths of decision 033 §2 recomputed at HEAD:
  ALL ELEVEN MATCH (decisions 027–032, auditor reports 015–016, OP-1.1/OP-1.2/OP-1.3).
- PI sign-off on decision 033 present
  (`docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md:177-188`); it accepted
  `PHASE_1_THEORY_READY` and expressly did **not** authorize OP-2.1.
- Decision 033 §9.6 (`comite_decision_033…md:156-158`): "OP-2.1 requires a separate committee
  decision and PI authorization after the durable handoff." The durable handoff is complete
  (commit `016be8b` pushed); the PI has now instructed opening OP-2.1.
- `PHASE_0_AUDIT_READY = SURVIVAL_MATRIX_COMPLETE + CLAIM_GRAMMAR_ADOPTED`
  (`docs/plan_operativo_15_julio_2026.md:169-175`), closed at commit `496985d`; auditor reports
  013/014 exist. Phase-2 dependencies (`plan:310`) — `PHASE_0_AUDIT_READY` + OP-1.3 probado —
  both satisfied at HEAD.
- OP-1.3 contract (`research_program/work_packages/op13_positive_evidence_protocol.md`):
  `OP_1_3_AUTHOR_TERMINAL=POSITIVE_EVIDENCE_PROTOCOL_PROVED`,
  `IMPLEMENTATION_READINESS=PENDING_GENERATOR_AND_WITNESS_SPEC` (`:227-230`); Hoeffding
  fixed-sample certificate (`:36-81`); routes A/B (`:83-108`); multiplicity (`:110-120`);
  generator-error trichotomy (`:122-139`); `SEQUENTIAL_STOPPING=FORBIDDEN` (`:141-151`);
  deterministic terminal-precedence chain (`:190-208`).
- Seed policy: 20 held-out validation seeds drawn once, blind, from the reserved virgin band
  `[2_000_000, 2_999_999]` (`docs/preregistration_002.md:14-30`); dev
  `EXPLORE_POOL = 1_000_000..1_000_039` (`:18`); `nachocausal/thresholds.py:57,66-75` encode
  `DEV_SEEDS` and programmatic band disjointness. No seed consumed by the Phase-1 closure
  (auditor report 016).
- Absence checks (warden, this session): `find dev -iname "*OP21*"` and
  `find . -iname "*reference_certifier*"` both return empty — the opening is genuine, not a
  retroactive rubber-stamp of already-run exploration.
- Guard-binding check (falsifier, this session): `tests/test_leak.py:15-31` binds only
  `estimator`/`generator` imports; `nachocausal/selection_guard.py:1-7` verifies past-matrix
  selectors — **no existing test constrains a new certifier module**.
- PR011 ladder CLOSED; PR012 `DRAFT_SCOPE` audited (commit `584a9f0`, auditor report 012
  `PASS_WITH_WARNINGS`), NOT frozen, NOT executed; OP-2.4 governs its re-adjudication
  (`plan:379-394`).

## 3. Dossier

Files and references the chair supplied to the committee:

- `docs/plan_operativo_15_julio_2026.md:308-336` (OP-2.1 spec + terminals), `:379-406` (OP-2.4 y
  gate de Fase 2), `:646-663` (reglas de parada), `:667-678` (qué NO autoriza el plan)
- `research_program/work_packages/op13_positive_evidence_protocol.md` (contrato teórico completo)
- `research_program/synthesis/op11_spherical_dual_target.md`,
  `research_program/synthesis/op12_tv_zero_3p1.md`
- `docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md` §9
- `docs/claim_grammar.md`; `docs/preregistration_002.md`; `docs/estimator_v2_seal.md`
- `nachocausal/` package; `tests/`; `dev/`; `Makefile`
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`;
  Hoeffding 1963 y Howard et al. arXiv:1810.08240 `[UNVERIFIED_LOCAL_SNAPSHOT]` per
  `op13:232-237`

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

**Proposed artefact(s)** — keep the reference certifier physically inert and provably outside the sealed instrument:
- Code: a new **non-sealed** pure-numpy subpackage, e.g. `nachocausal/certifier/reference_certifier.py` + `__init__.py`. Rationale for the location: the prereg-002 seal is the SHA256 of `nachocausal/thresholds.py` *only* (`docs/estimator_v2_seal.md:5-9`, `docs/preregistration_002.md:7-9`), so adding a sibling module leaves the seal byte-identical — but the module must **not** be wired into `validate.run()` (`nachocausal/validate.py`), so the sealed evaluation-order path (`docs/estimator_v2_seal.md:33-38`) is untouched.
- Interface (matches OP-1.3 §3 exactly): a pure function `certify_tv_lower(stream_P, stream_Q, m_P, m_Q, alpha_j, eps_P, eps_Q) -> {TV_lower_j, r_Pj, r_Qj, abstain?, provenance}` implementing `TV_lower_j = max(0, |μ̂_P−μ̂_Q| − r_P − r_Q − ε_P − ε_Q)`, `r = sqrt(log(4/alpha_j)/(2m))` (`op13:59-76`). The signature accepts **only** two float streams in `[0,1]` plus scalars — no poset, no `past_matrix`, no embedding/coords — which *is* the constructive proof that "el estimador de intervalo no consume información geométrica" (plan:324); enforce with a runnable guard that raises if any stream leaves `[0,1]`.
- Tests: `tests/test_op21_reference_certifier.py` — synthetic laws with closed-form TV (coverage ≥ 1−α_total over a declared dev-seed MC), bit-exact reproducibility, weighted-Bonferroni budget `Σ_j alpha_j ≤ alpha_total` cell = full tuple (`op13:110-120`), an assertion that any sequential-stopping path **raises** (`SEQUENTIAL_STOPPING=FORBIDDEN`, `op13:141-151`), and precision/resource abstention (`REFERENCE_PRECISION_ABSTAIN`, plan:333).
- A dev pre-registration `dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md` declaring synthetic laws, coverage target, MC seeds and cell budget **before** the coverage MC is run (dev/validation separation, `CLAUDE.md:16-17`).

**Environment & seal**
- Pinned env: `numpy==1.26.4` (`thresholds.PINNED_NUMPY`, `nachocausal/thresholds.py:18`); the certifier and its coverage MC must call `thresholds.assert_environment()` (`thresholds.py:21-32`) so bit-reproducibility holds. Do **not** use the external Minz venv `~/cs-horizon-reuse-check/venv_minz` (numpy<2, `CLAUDE.md:28-29`) — that is for `dev/prototype_o.py` only; the certifier is pure-numpy, no Minz.
- Re-verify `make verify-seal` == `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (chair-verified this session) **before and after** landing the module; it must be unchanged (adding files ≠ editing `thresholds.py`). Package-diff-clean: `git status` shows only the new certifier/test/prereg files against HEAD `016be8b`.

**Provenance capture** (the op13 manifest fields, `op13:135-139`): record commit SHA, `pip freeze` (at minimum numpy version), `uname -a`, RNG family + draw rule, the **dev** seed band used, per-cell `m_Pj,m_Qj,alpha_j,ε_Pj,ε_Qj`, witness/code hashes, and start/end timestamps. Seeds: dev/synthetic seeds only (`EXPLORE_POOL = 1_000_000..1_000_039`, `preregistration_002.md:18`); the reserved **virgin** band `[2_000_000,2_999_999]` and the 20 held-out seeds (`preregistration_002.md:14-27`) are untouched — no seed consumed.

**Run mechanics**
- Single foreground invocation: `python -m pytest -q tests/test_op21_reference_certifier.py` (add an optional `certifier-test` Makefile target — reversible, does not alter `verify-seal`/`dry-run`/`gate`). This is an all-**reversible pre-flight**: OP-2.1 has **no committing step** (it is WP5 technology, not a physical confirmation; plan:326,336). `validate.run()` is never called → `RESPECT_SEAL_FREEZE` holds by construction.
- Clean abort: the numpy-pin guard, the `[0,1]`-domain guard, and the sequential-stopping guard each raise before any output; PR011 must be consumed **read-only** as an integration bench (import its already-computed TV as fixtures, never re-execute it as a new confirmation, plan:326).

**Reproducibility risks / ambiguities**
- Module location is a genuine committee decision: even though the seal (sha of `thresholds.py`) is unchanged, placing code inside `nachocausal/` risks it being mistaken for the sealed instrument — a distinct non-sealed subpackage + a docstring stating "not part of the prereg-002 evaluation path" mitigates this. [anchored: `docs/estimator_v2_seal.md:33-38`]
- Coverage verification is itself Monte Carlo, so it needs its own frozen seed provenance; accidental use of `generator.numpy_sprinkle` with a validation-band seed would breach the freeze — guard by asserting seeds ∈ dev band. [anchored: `preregistration_002.md:16-18`, `nachocausal/validate.py:84`]
- The sequential-stopping "optional stopping si aplica" check can only assert the fixed-sample default and forbid the sequential branch; the Howard et al. confidence sequence needed to lift it is `arXiv:1810.08240` `[UNVERIFIED_LOCAL_SNAPSHOT]` (`op13:147,236`) — do not instantiate it under OP-2.1.
- ε-bound (generator error) provenance: the certifier consumes `ε_Pj,ε_Qj` as inputs; who certifies them (EXACT_GENERATOR vs BOUNDED_GENERATOR_ERROR) is out of OP-2.1's scope (`op13:122-139`) and must be supplied/hashed by the caller, else `GENERATOR_ERROR_NOT_BOUNDED` — flag so the reference module cannot silently assume `ε=0`. [anchored: `op13:122-139`]

### Mathematician brief

- **Computability:** The observed object is a finite partial order (poset) `C=(S,≺)`, not a total order; every quantity OP-2.1 consumes is a poset invariant computable in poly-time on `≺` with no embedding. The two inputs are streams of `f(C)∈[0,1]` — the certifier's declared input *type* is a real in `[0,1]`, so "el estimador de intervalo no consume información geométrica" is discharged structurally at the interface, not merely by audit: coordinates, `r`, `M`, `h_M`, expansions are type-unreachable from `[0,1]` (op11:244-245). The Hoeffding fixed-sample certificate is computable for arbitrary `n` — it carries **no** `n≤8` exhaustive-enumeration ceiling that the exact TV sum has (op13:80-81), which is precisely the WP5 payload "cuando enumerar posets sea imposible" (plan:336). The abstaining machinery is already realized and total: τ(n) gate `nachocausal/gate.py` + frozen `fixtures/tau_table.json` (n=2..128), abstain (`sep→0`) iff `improvement < τ(n)`; domain gate `T_EDGE_MIN=6 ⇒ OUT_OF_DOMAIN`, a status that is **never a physical FAIL** (docs/estimator_v2_seal.md:20-26).

- **Order observable:** OP-2.1 itself does **not** select a witness; it certifies, for *given* pre-registered `f`, the bounded-witness inequality `TV(P,Q) ≥ |E_P f − E_Q f|`, proved by the layer-cake representation `E_P f − E_Q f = ∫₀¹ [P(f>t)−Q(f>t)] dt` with each integrand bounded by `TV` over a unit interval (op13:17-34; claim_grammar:308-315). The horizon signal, when a real `f` is later plugged in, must ride on an order-only functional — the sealed estimator-v2 future-volume `O(i)=|future(i)|`, the column-sum of the causal matrix over minimal elements (estimator_v2_seal.md:16). Correctness of OP-2.1 is confined to the *estimator* of this gap, independent of whether any particular `f` localizes a boundary.

- **Relevant invariants:** future-volume `|future(i)|` (production observable, estimator_v2_seal.md:16); the height/longest-chain oracle `estimate_O`, retained bit-exact as the poset-integrity anchor (estimator_v2_seal.md:16-17, `tests/test_regression.py`); and the Benincasa–Dowker interval-abundance family `C_k` and the ordering fraction as the standard order invariants of a Lorentzian causal set (Surya, LRR 2019 §4; Benincasa–Dowker `biblioteca/`). All are functions of `≺` alone.

- **Analytic / continuum target:** OP-2.1's own target is a statistical *separation* floor `TV_lower>0`, which is **not** recoverability (op13 §8:163-174). The genuine continuum benchmark for the eventual horizon claim is the marginal-sphere locus `h_M(x)=r(x)/(2M)−1=0`, `H(g)` (op11:133-138), reached in the family via the null expansion `θ_k=(2/r) k(r)` whose sign is normalization-independent (op11:125-129), and the focusing/trapping picture of Eichhorn–Gamito–Stokes arXiv:2605.06813 (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-230`). The TV=0 orbit (mass-dilation) of op12 §2-3 is the null direction the certifier must be able to *not* over-separate.

- **Caveats:**
  - A passing certificate proves only the conditional schema; `TV_lower>0` from a mere cardinality statistic distinguishes masses in `order+number` while localizing **no** boundary — that is `TARGET_WITNESS_MISMATCH`, not recovery (op13:173-174). OP-2.1 must not be presented as physical confirmation.
  - Finite-sample bounds need not be monotone in `n`; any `n_star(Δ_alt;η)=min{n∈N_grid: TV_lower≥η}` crossing requires a **pre-frozen** persistence rule, else `NO_CROSSING_IN_GRID` with no extrapolation (op13:153-161).
  - The plan's "optional stopping si aplica" must default to fixed-sample: `SEQUENTIAL_STOPPING=FORBIDDEN` until a Howard-et-al confidence sequence (arXiv:1810.08240 `[UNVERIFIED_LOCAL_SNAPSHOT]`) is instantiated and proved (op13:141-151).
  - Generator error must resolve to `EXACT_GENERATOR` or `BOUNDED_GENERATOR_ERROR(ε)` with a certified/causal-margin bound; declaring float errors "small" is not a bound → `GENERATOR_ERROR_NOT_BOUNDED` abstention (op13:122-133).
  - PR011 (incl. `tests/test_pr011_tv_certification_enumeration.py`) may serve **only** as an integration bench, never as new physical confirmation (plan:326); this respects `NO_GROUND_TRUTH_LEAKAGE` since the certifier reads only `[0,1]` streams, never the hidden embedding.
  - Scope stays order-only 1+1D localisation in a finite patch: no 3+1D code, no touching the sealed `thresholds.py` (`6e2c3888…`) or validation seeds — consistent with `RESPECT_SEAL_FREEZE`, `NO_RECONSTRUCTION_CLAIM`.

### Mathematical logic brief

- **Formal status.**
  - The object OP-2.1 must implement is the *fixed-sample Hoeffding certificate* of op13 §3 (`op13_positive_evidence_protocol.md:36-81`). Its mathematical content — `TV_lower_j = max(0, |μ̂_P−μ̂_Q| − r_P − r_Q − ε_P − ε_Q)` is a valid ≥1−α_total lower bound on `TV(P_j,Q_j)` — is a **proved conditional theorem (paper proof / schema only)**, carrying author terminal `POSITIVE_EVIDENCE_PROTOCOL_PROVED` with `IMPLEMENTATION_READINESS = PENDING_GENERATOR_AND_WITNESS_SPEC` (`op13:227-230`). It is explicitly *not* a scientific PASS and cannot be inherited retrospectively (`op13:205-208, 223-225`). The witness-shift lemma ("TV error ε moves any `[0,1]` witness expectation by ≤ε") is likewise proved (`op13:32-34`).
  - The Lean artefacts under `formal/HorizonFormal/` (Horizon.lean, Ideals.lean, ChainEnds.lean, …) formalise the *order-theoretic horizon* layer only; they are disjoint from the statistical certifier. **OP-2.1 has no machine-checked (Lean) backing** — its correctness rests entirely on the op13 markdown proof. Recommend scoping OP-2.1's "prueba de que el estimador de intervalo no consume información geométrica" (`plan:324`) as a **still-open proof obligation to be discharged inside OP-2.1**, i.e. a `CONDITIONAL` deliverable, not an assumed fact.
- **Quantifier / dependency order.**
  - Coverage is **conditional on a frozen witness**: "condicionalmente al testigo congelado, la cobertura sigue válida" (`op13:96`). Correct order is ∀(f, cells `J`, α_j, m_Pj/m_Qj, ε bounds) chosen *before* confirmatory replicas are seen (Route A, `op13:87-91`) or before the single confirmatory evaluation (Route B, `op13:92-96`). Reversing this — selecting/tuning `f` on the same replicas — is the exact place post-hoc DOF enters and triggers `ADAPTIVE_SELECTION_UNCONTROLLED` (`op13:106-108`).
  - Coverage is a **simultaneous (union-bound) statement over all cells**, `Σ_j α_j ≤ α_total` (`op13:44,64-65`); a cell is the *full tuple* (`op13:113-120`), so appending "best mass/best n/best patch" after the fact silently enlarges `J` and voids the guarantee. OP-2.1, being a *generic module that only receives two `f(C)∈[0,1]` streams* (`plan:315`), must sit strictly **below** cell/witness selection and must not itself choose cells.
  - `n_star` requires a pre-specified grid `N_grid`; no extrapolation (`NO_CROSSING_IN_GRID`) and **monotonicity is not assumed** — any persistence-in-n requirement is a separate rule frozen before data (`op13:153-161`).
  - "Optional stopping si aplica" (`plan:322`) must default to fixed-sample: `SEQUENTIAL_STOPPING = FORBIDDEN` until a Howard-et-al time-uniform confidence sequence is *instantiated and proved* (`op13:141-151`). The all-times quantifier does not yet exist, so OP-2.1 may build the interface but must hard-abstain on any sequential path.
- **Equivalence claims.**
  - The certifier proves a strictly **one-way (unilateral) inequality** `TV_lower_j ≤ TV(P_j,Q_j)` (`plan:315-316`, `op13:68-76`) — not equality, not an upper bound. `POSITIVE_EVIDENCE_PROTOCOL_PROVED ⇒ scientific PASS` is **false** (`op13:207-208`); `TV_lower>0 ⇒ horizon recovery` is **false** (`op13:163-174`, `TARGET_WITNESS_MISMATCH`). No genuine iff should be asserted between a passing certificate and any localisation claim (`NO_RECONSTRUCTION_CLAIM`).
  - For contrast, the order layer does contain a real biconditional, `AccessesIdeal x I ↔ x ∈ I` (`accessesIdeal_iff_mem`, `LEAN_HYPOTHESIS_AUDIT.md:34`); OP-2.1 has nothing of that strength and should not borrow "proved" language from it.
- **Type / object discipline.**
  - OP-2.1's domain type is **two streams of `[0,1]`-valued reals** (empirical means of a frozen witness), a universe disjoint from the Lean poset objects (ideals, quotient chain-end classes, cover relation). The "no consume información geométrica" clause (`plan:324`) is precisely a **type-level firewall**: the interval estimator's input type must be *(the two float streams)*, never *(the causal set C, embedding coordinates, `h_M`, per-element labels)* — which `op13:98-102` allows only in a separate diagnostic, never in promotion/frontier/abstention decisions. Because `f` is frozen upstream (Route A/B), the estimator is geometry-blind **by construction if and only if** it reads only the stream values; this invariant must be *proved/enforced* (candidate anchor: existing `tests/test_leak.py`, `nachocausal/selection_guard.py`), not assumed.
  - Keep the cell as an intact product type (`op13:113-120`); collapsing the tuple is a category error that hides multiplicity. PR011 is an **integration-bench fixture type**, never a physical-confirmation type (`plan:326`) — using it to source a certificate would be a use/mention (bench-vs-confirmation) category mistake.
- **Caveats.**
  - The decision-033 §9.6 gate is a **conjunction**: "a separate committee decision *and* PI authorization after the durable handoff." The durable handoff is complete (HEAD `016be8b`, DOSSIER VERIFIED STATE); the PI instruction "Inicia OP-2.1" opens the question, but the *specific scope* is fixed by this committee and the authorization is the sign-off on this brief — the instruction alone is not scope-authorization (`comite_decision_033` §9.6, DOSSIER).
  - Opening OP-2.1 is logically admissible: it produces schema-level technology and consumes **no** confirmatory information provided it (i) touches only synthetic laws with known TV and dev seeds, never the reserved virgin band `[2_000_000,2_999_999]` (`preregistration_002.md:14-30`), (ii) does not touch `thresholds.py`/seal `6e2c3888` (`plan:667-678`), (iii) opens no PR012/PR013 and writes no 3+1D code (`plan:667-678`), (iv) emits no new physical confirmation (`plan:326`). These prohibitions are consistent with `RESPECT_SEAL_FREEZE`, `NO_GROUND_TRUTH_LEAKAGE`, `NO_THRESHOLD_LOOSENING`.
  - `[UNVERIFIED]`: I did not machine-check that `tests/test_leak.py` / `selection_guard.py` actually enforce the geometry-blind input type for a *new* certifier module; the DOSSIER lists them but does not show their assertions bind OP-2.1's interface. The "no-geometry" proof obligation should be treated as open until so demonstrated.
  - Stop-rule alignment: if the reference certifier fails coverage the mandated response is "reparar método; no cambiar target" (`plan:646-663`) — i.e. `REFERENCE_COVERAGE_FAIL` must never be coerced into PASS (`NO_POST_HOC_TUNING`); report PASS/FAIL/`REFERENCE_PRECISION_ABSTAIN` alike.

### Physicist brief

- **Coordinates & patch:** OP-2.1 must use **no coordinates at all** — this is the load-bearing point. The module is a generic TV lower-bound certifier over two abstract streams `f(C)∈[0,1]`, and the plan's own minimal-verification list demands "prueba de que el estimador de intervalo no consume información geométrica" (plan:324). Physically this is correct and required: coordinates, `r`, `M`, expansions and continuous labels are prohibited outside the separated embedding-only scoring layer (op11:244-245). The underlying geometry OP-2.1 will eventually serve is the finite patch of OP-1.1 (`V∈[v0,v1]`, `U∈[-u_out,u_in]`, interior held off the singularity `UV=1` via `u_in·v1 ≤ 1-ε_s`; op11:41-61). Finiteness is not incidental: an event horizon is `∂Past(J⁺)` and "to define an event horizon in a causal set, an infinite sprinkling is required" (2605.06813, md:173). So the finite patch **forfeits any asymptotic event-horizon claim by construction**; only interior/exterior *localisation* survives.

- **Physical meaning of the signal:** The order-only observable that tracks `r=2M` is the length of the longest chain (or future-cardinality) from minimal elements, which is **bimodal**: interior minimal elements have truncated futures "because each timelike curve inside the horizon must reach r=0 within a finite amount of proper time," while exterior chains are limited only by patch size, giving "a sharp transition ... exactly at the location of the horizon" (2605.06813, md:181-193). This matches the quasi-local characterisation `Θ_out(r=2M)=0` (md:223-225), which for Schwarzschild coincides with the event/Killing horizon and with OP-1.1's `h_M(x)=r/(2M)-1=0` boundary between untrapped and trapped spheres (op11:135-140). **OP-2.1 itself computes none of this** — it only certifies a one-sided TV lower bound between two supplied `f(C)` streams; the physics enters solely through whatever downstream witness (OP-2.2) later feeds it.

- **Sprinkling domain:** No new Poisson sprinkling is drawn or authorised by OP-2.1. Verification runs on **synthetic laws with known TV** (plan:320) and PR011 strictly as an **integration bench, never as new physical confirmation** (plan:326); PR011 is enumeration-based (tests/test_pr011_tv_certification_enumeration.py), so it exercises the certifier combinatorially, not via a physical sprinkling. The eventual physical channel remains the declared finite patch with Poisson intensity `ρ` known (op11:180-188) and effective scale `ell_eff=(μ_g(K_g)/n)^{1/4}` (op12:96-98); OP-2.1 touches **no validation seed** — the reserved virgin band [2_000_000, 2_999_999] (prereg-002:14-30) stays untouched, consistent with the seed policy.

- **Claim boundary:** A `POSITIVE_CERTIFIER_REFERENCE_PASS` (plan:330) certifies **the estimator's coverage/reproducibility**, not any horizon and not any new physics — it is WP5 technology "que necesitará 3+1D cuando enumerar posets sea imposible" (plan:336). It makes **no** physical confirmation: `NO_RECONSTRUCTION_CLAIM` holds — this is order-only *localisation* in a finite 1+1D patch, never metric reconstruction, never asymptotic-horizon, never 3+1D. The regular-black-hole caveat is essential and must be recorded in scope: for Hayward-type regular black holes the very bimodal diagnostic **fails**, because interior timelike curves can be continued for arbitrarily long proper time, so the partition does not exist (2605.06813, md:195). Any eventual localisation claim built on this certifier is therefore **Schwarzschild(-singular)-specific**, not a generic black-hole result.

- **Caveats:**
  - The `f(C)∈[0,1]` streams OP-2.1 ingests must remain provably geometry-blind; if any coordinate/`r`/`M`/embedding label leaks into stream construction the correct terminal is `POSITIVE_CERTIFIER_INVALID` (plan:334) — physically this is the same firewall as op11:324 (`FAILED_DATA_CONTRACT` on embedding-built estimates). `NO_GROUND_TRUTH_LEAKAGE`.
  - Finite-patch TV distinctness is real physics: within a fixed sector and patch, the mass orbit is a genuine TV=0 class in `fixed_n` (op12:73-79), so the certifier must never be read as identifying absolute `M` or `r_h=2M`; only relative/dimensionless localisation is meaningful (op12:93-103).
  - No physical PASS is available from OP-2.1 regardless of outcome; a coverage failure is a **method repair, not a target change** ("Certificador falla cobertura → reparar método; no cambiar target", plan:646-663) — I endorse that stop rule from the physics side.
  - `[UNVERIFIED]` The exact Kruskal normalisation coefficient (`32M³/r` vs `16M³/r`) is a declared convention only and unverified in the local snapshot (op11:32-37, 343-345); no result here depends on it, and OP-2.1 depends on it not at all.

## 5. Falsifier attack

### Falsifier attack

- Concrete failure modes:
  1. **A stateless pure function cannot enforce `SEQUENTIAL_STOPPING=FORBIDDEN`.** The reproducibility brief promises "sequential-stopping path RAISES" inside `certify_tv_lower(...)`, but a pure per-call function over two streams has no cross-call memory: a caller can invoke it repeatedly with growing `m` and stop when `TV_lower>0`, silently voiding the Hoeffding coverage (op13 fixed-sample premise, `research_program/work_packages/op13_positive_evidence_protocol.md:141-151`). The promised guard is a guardrail that cannot fail — decoration by the founding rule (`CLAUDE.md:14`). Enforcement must be relocated to a manifest/bench layer (op13:135-139) or the scope is claiming a property the artefact cannot have.
  2. **Same defect for multiplicity.** `Σ_j α_j ≤ α_total` (op13:44, :110-120) is a property of the *set* of calls, not of one call. A test asserting "weighted Bonferroni holds" against a single function proves nothing; without a budget-ledger object in scope, the multiplicity verification of plan:321 is untestable as specified.
  3. **Coverage MC is under-powered against the worst bug class.** Hoeffding is heavily conservative, so empirical coverage will sit near 1 even under moderately anti-conservative implementation errors (e.g., `log(2/α)` for `log(4/α)` in op13:60-61, or silently dropped ε). A bench that cannot fail a broken certifier certifies nothing. The dev prereg must include a mutation-detection power requirement, not just "coverage ≥ 1−α_total".
  4. **No precedence chain for the OP-2.1 terminals.** op13 fixes a total deterministic precedence for its terminals (op13:190-208); plan:328-334 lists five OP-2.1 terminals with **no** ordering. Simultaneous coverage-fail + reproducibility-fail (or fail + abstain) leaves publication to discretion — exactly the hole the op13 chain was built to close. Scope must freeze a precedence chain before any bench run.
  5. **The terminal-issuing run is not separated from the build loop.** Nothing in plan:313-336 or the briefs distinguishes exploratory debugging iterations from the single run that emits `POSITIVE_CERTIFIER_REFERENCE_PASS`. Without a frozen bench spec + one-shot rule (dev prereg written *before* the coverage MC, as the repro brief gestures at but does not make binding), PASS is rerun-until-pass and unfalsifiable.
  6. **Seed-band confusion in the reproducibility brief.** It anchors "guard asserts seeds ∈ dev band" to `docs/preregistration_002.md:16-18`, but that band is `EXPLORE_POOL = 1_000_000..1_000_039` — 40 *sprinkling* seeds — while `nachocausal/thresholds.py:57` defines a different 8-seed `DEV_SEEDS` tuple. A coverage MC needs thousands of RNG streams; "∈ dev band" is either vacuous or unsatisfiable. A new synthetic-MC seed band must be declared in the dev prereg, disjoint from the virgin band `[2_000_000, 2_999_999]` (`preregistration_002.md:16-18`).
  7. **Existing guards do not bind the new module.** Confirmed: `tests/test_leak.py:15-31` binds only `estimator`/`generator` imports; `nachocausal/selection_guard.py:1-7` verifies past-matrix *selectors*, not stream functions. The logician's `[UNVERIFIED]` is now VERIFIED-NEGATIVE: no existing test constrains a new certifier; all its guards must be new and must be demonstrably able to fail.
  8. **`make test` contamination.** `Makefile:9-10` runs `pytest tests/` wholesale — the same target that is the sealed-path regression gate. Dropping a stochastic, long-running coverage MC into `tests/` changes the semantics and runtime of the canonical suite; certifier benches need a separate target or marker.

- Ground-truth leakage: No direct embedding path (synthetic streams carry no geometry). Two indirect channels: (i) **PR011 fixture streams require choosing an `f` to map posets → [0,1]** — a witness choice OP-2.1 is expressly barred from making (mathematician brief; op13:83-108). Any PR011-derived `f` used in the bench is a de facto witness selection outside Route-B provenance and can contaminate OP-2.2 (`FAILED_DEVELOPMENT_PROVENANCE`, op13:98-104). It must be declared bench-only and non-promotable, or PR011 integration should be dropped. (ii) Choosing the "synthetic laws with known TV" *after* inspecting PR011 statistics tunes the bench toward passing; laws must be closed-form-TV and declared before any run.

- Freeze violations: (i) Coverage-fail → fix → rerun on the same bench without a re-frozen prereg is tuning-on-result; plan:654 ("reparar método; no cambiar target") permits repair but does not license silent re-runs of the *terminal* run. (ii) Coverage-MC seeds not pre-frozen (failure mode 6). (iii) Any edit to pre-existing `nachocausal/*.py` (including `nachocausal/__init__.py` to expose the subpackage) mutates the package the sealed `validate.run()` imports; the scope must require sha256 of every pre-existing `nachocausal/` file unchanged, not only `make verify-seal` on `thresholds.py`. (iv) Governance order: decision 033 §9.6 and the PI sign-off itself ("do not start OP-2.1… requires a separate committee decision and PI authorization", `comite_decision_033…md:169-170, 185-188`) make authorization a conjunction over a *fixed scope*. The PI instruction predates this committee's scope; a pre-emptive general "inicia OP-2.1" is not sign-off on conditions the PI has not seen. Require explicit post-decision PI signature on the exact scope, contra the logician's "authorization = sign-off on this brief".

- Verdict coercion: (i) `TV_lower = max(0,·) = 0` is a *valid vacuous certificate*, not an abstention; conflating the two coerces in both directions (a 0-bound reported as ABSTAIN hides a working-but-weak method; an ε-unbounded input reported as 0-bound instead of mandatory abstention violates op13:122-133). The interface must return distinct states. (ii) With no terminal precedence (failure mode 4), FAIL/ABSTAIN collision resolution is discretionary. (iii) `REFERENCE_COVERAGE_FAIL` must be publishable as-is; any workflow where only PASS gets committed is asymmetric reporting.

- Premature / over-broad claims: (i) The two briefs *contradict* each other on plan:324: mathematician says no-geometry is "discharged structurally at interface"; logician says it is a still-open proof obligation. The logician is right — the type signature proves only that the *module* reads no geometry; it cannot prove streams weren't geometry-built upstream. A PASS must never be cited as end-to-end no-leakage. (ii) `POSITIVE_CERTIFIER_REFERENCE_PASS` certifies coverage/reproducibility of a statistical bound — zero physics; op13:207-208 already blocks promotion to scientific PASS and the scope must restate it. (iii) WP5 phrasing "tecnología que necesitará 3+1D" (plan:336) invites citing OP-2.1 as 3+1D readiness; it is not (`GO_3P1_DEVELOPMENT` untouched, plan:674).

- Independent-falsification gate: NOT satisfied as briefed. The reproducibility engineer proposes to author the module, its tests, and the dev prereg — author and sole verifier coincide. Require: mutation/adversarial bench cases specified in the dev prereg by a non-implementer role, and an `/auditor` pass over the terminal-issuing run before any OP-2.1 terminal is recorded.

- Minimal falsification test: **Mutation check of the coverage bench.** In a throwaway branch of the (future) test suite, monkeypatch the radius to the anti-conservative `r_j = sqrt(log(2/α_j)/(2m_j))` (or silently zero the ε terms) and run the exact planned coverage MC: `pytest tests/test_op21_reference_certifier.py -k coverage` must emit `REFERENCE_COVERAGE_FAIL` against the mutant. If the bench passes the broken certifier, the bench is decoration (`CLAUDE.md:14`) and no OP-2.1 terminal may issue from it. This one check simultaneously exposes failure modes 3 and 5 (an un-failable bench and an unfalsifiable PASS).

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: **PASS** (conditional — opening is admissible only under the scope conditions below, none of which are yet in place and must be satisfied before any seed is drawn)
- Freeze status: The instrument being opened is a *schema*, not a threshold-bearing instrument. `research_program/work_packages/op13_positive_evidence_protocol.md:227-230` states `OP_1_3_AUTHOR_TERMINAL = POSITIVE_EVIDENCE_PROTOCOL_PROVED` but `IMPLEMENTATION_READINESS = PENDING_GENERATOR_AND_WITNESS_SPEC` — i.e. no concrete `n`, `alpha_j`, `eps_P/eps_Q`, witness, or seeds are frozen yet for OP-2.1 itself. `docs/plan_operativo_15_julio_2026.md:313-336` fixes only interface + terminals + minimal checks, not numeric thresholds. Per the reproducibility-engineer brief, a *new* `dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md` must be written and frozen (git commit) **before** any coverage-MC or reproducibility run is executed — this is a **hard precondition of PASS**, not yet satisfied (confirmed absent: `find dev -iname "*OP21*"` returns nothing). No thresholds.py edit is authorized or needed (`docs/plan_operativo_15_julio_2026.md:672`: "Tocar `thresholds.py`, prereg-002/003 o el sello `6e2c3888`" is listed under "Qué NO autoriza este plan").
- Seal integrity: `make verify-seal` output pasted by chair: `thresholds.py` sha256 `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` matches the frozen value recorded at `docs/preregistration_002.md:6-8`. OP-2.1's module (`nachocausal/certifier/reference_certifier.py`, per repro-engineer brief) must be a new, non-sealed subpackage that never imports or calls `validate.run()`; it does not touch, extend, or re-run the sealed path. This must remain unchanged before/after OP-2.1 work — confirm the seal is re-verified after any OP-2.1 commit.
- Seed discipline: Dev pool `EXPLORE_POOL = 1_000_000..1_000_039` (`docs/preregistration_002.md:18`, mirrored `nachocausal/thresholds.py:57` `DEV_SEEDS`) is disjoint from the reserved validation virgin band `[2_000_000, 2_999_999]` (`docs/preregistration_002.md:14-30`; `nachocausal/thresholds.py:66-75` asserts disjointness and band membership programmatically). OP-2.1's coverage-MC and reproducibility checks must draw exclusively from dev seeds / synthetic-law generators with independently declared, provenance-tracked RNG draws (op13:135-139 manifest requirement) — never from `VALIDATION_SEEDS`. No PR011 validation-run confirmatory seed may be consumed; PR011 is integration bench only (`docs/plan_operativo_15_julio_2026.md:326`: "PR011 puede usarse como banco de integración, nunca como nueva confirmación física").
- Reporting rule: The five plan terminals (`docs/plan_operativo_15_julio_2026.md:328-332`) plus the op13 terminal-precedence chain (op13:190-208, with `INCOMPLETE_CONFIRMATORY_MANIFEST > ... > POSITIVE_EVIDENCE_PROTOCOL_PROVED`) must all be reported identically regardless of outcome — a coverage failure, precision-abstain, or invalidity finding is reported with the same visibility and file-path discipline as a PASS. Per the stop-rules table (`docs/plan_operativo_15_julio_2026.md:646-663`: "Certificador falla cobertura" → "reparar método; no cambiar target"), a coverage failure triggers method repair, never target substitution or re-tuning on the same dev sample without declaring the new attempt as an additional cell (op13:110-120 multiplicity rule).
- Forbidden moves present? None yet in the proposal as scoped by the plan text and expert briefs — but three latent risks must be closed by explicit committee-fixed scope (not left to implementer discretion):
  1. **Post-hoc tuning risk**: op13:141-151 `SEQUENTIAL_STOPPING = FORBIDDEN` must be enforced structurally (test asserts a raise on any sequential/peeking code path per repro-engineer brief), since Hoeffding fixed-sample is the only authorized stopping rule until a valid always-valid confidence sequence is separately proved.
  2. **Ground-truth leakage risk**: the certifier module must accept *only* `[0,1]` float streams + scalars, structurally incapable of ingesting geometry, per the "no-geometry" proof obligation flagged as still-open by the mathematical-logic brief (op13 §3 is schema-only; the constructive no-geometry proof is plan:324's minimum-verification item, not yet discharged). This proof is a **precondition of PASS**, not a nice-to-have.
  3. **Reconstruction over-claim risk**: any PASS terminal must carry the op13 §8 caveat verbatim (`TV_lower>0` is separation, not recoverability; TARGET_WITNESS_MISMATCH is the correct terminal for cardinality-only separation, op13:173-174) and must not be reported as a Schwarzschild-specific or physics confirmation (physicist brief: PASS certifies coverage/reproducibility, not physics).
- Reasons:
  - `docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md:156-158` (item 6 of the atomic-handoff instructions): "OP-2.1 requires a separate committee decision and PI authorization after the durable handoff" — this session is that gate, and PI sign-off at `:177-188` ("do not start OP-2.1... ") was explicitly *not* an OP-2.1 authorization at the time; today's PI instruction ("Inicia OP-2.1 según el plan operativo") is the missing authorization, so the procedural gate is now satisfiable, conditional on scope below.
  - `docs/plan_operativo_15_julio_2026.md:313-336` fixes location/interface/terminals/PR011-role exactly as the decision question states; nothing in the plan text authorizes touching `thresholds.py`, drawing validation seeds, or running PR012/PR013 (`:672-678`, "Qué NO autoriza este plan").
  - `research_program/work_packages/op13_positive_evidence_protocol.md:229-230` — `IMPLEMENTATION_READINESS=PENDING_GENERATOR_AND_WITNESS_SPEC` is the operative freeze-status fact: OP-2.1 opening authorizes writing/freezing that missing spec (a new dev-level pre-registration) as its *first* deliverable, before any seed is drawn or coverage MC executed — this is the freeze discipline extended one level down, exactly analogous to how prereg-002 preceded the estimator-v2 validation run.
  - `nachocausal/thresholds.py:57,66-75` gives the only currently-frozen seed bands; OP-2.1 must cite these programmatic guards directly rather than re-deriving seed bounds informally.
  - Absence check: `find dev -iname "*OP21*"` and `find . -iname "*reference_certifier*"` both return empty — confirming this is a genuine opening (not a retroactive rubber-stamp of already-run exploration), which satisfies the "no re-run after peeking" concern structurally, provided the dev pre-registration is written and committed *before* any code in `nachocausal/certifier/` executes a Monte Carlo draw.

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| docs/estimator_v2_seal.md:5-9 (seal = SHA256 of thresholds.py) | Repro engineer | CONFIRMED |
| docs/preregistration_002.md:7-9 (prereg-002 seal SHA256) | Repro engineer | CONFIRMED |
| docs/estimator_v2_seal.md:33-38 (sealed evaluation order `domain→estimator(volume)→gate(τ)→criteria`) | Repro engineer | CONFIRMED |
| nachocausal/thresholds.py:18 (`PINNED_NUMPY = "1.26.4"`) + :21-32 (`assert_environment`) | Repro engineer | CONFIRMED |
| docs/preregistration_002.md:18 (`EXPLORE_POOL = 1_000_000..1_000_039`) | Repro engineer | CONFIRMED |
| docs/preregistration_002.md:14-30 (virgin band `[2_000_000,2_999_999]` drawn once, blind) | Repro engineer | CONFIRMED |
| CLAUDE.md:28-29 (Minz venv note, `venv_minz`) | Repro engineer | CONFIRMED |
| research_program/work_packages/op13_positive_evidence_protocol.md:17-34 (layer-cake proof, `TV ≥ \|E_P f − E_Q f\|`) | Mathematician | CONFIRMED |
| docs/claim_grammar.md:273-338, esp. :306-315,317-328 (lower-bound claim + limits, `L_gap`, prohibited forms) | Mathematician | CONFIRMED |
| op13:80-81 ("no tiene el techo n≤8 de la suma exhaustiva") | Mathematician | CONFIRMED |
| docs/estimator_v2_seal.md:16-17 (VOLUME observable + retained height/longest-chain oracle) | Mathematician | CONFIRMED (estimator.py:26-37 shows `estimate_O` is literally a single-source longest-path/"longest timelike chain" DP, so "longest-chain oracle" is an accurate gloss of what the doc calls "height oracle") |
| docs/estimator_v2_seal.md:20-26 (τ(n) gate + `OUT_OF_DOMAIN` never physical FAIL) | Mathematician | CONFIRMED |
| research_program/synthesis/op11_spherical_dual_target.md:133-140 (marginal locus `h_M(x)=0`) | Mathematician | CONFIRMED |
| op11:244-245 (coordinates/r/M/expansions prohibited in construction/selection) | Mathematician | CONFIRMED |
| research_program/synthesis/op12_tv_zero_3p1.md:73-79 (TV=0 mass-orbit, `fixed_n` class = full mass interval) | Mathematician | CONFIRMED |
| op13:173-174 (`TARGET_WITNESS_MISMATCH`, cardinality-statistic case) | Mathematician | CONFIRMED |
| biblioteca/derived-md/The causal set approach to quantum gravity.md (Surya LRR 2019, §4 order invariants) | Mathematician | CONFIRMED (file exists, "Sect. 4" order-invariant/Hauptvermutung discussion at lines 124, 930-1985) |
| op13:227-230 (`POSITIVE_EVIDENCE_PROTOCOL_PROVED` + `IMPLEMENTATION_READINESS=PENDING_GENERATOR_AND_WITNESS_SPEC`) | Logician | CONFIRMED |
| op13:205-208 (author terminal does not convert a future run into scientific PASS) | Logician | CONFIRMED |
| op13:92-96 (Route B conditional coverage) | Logician | CONFIRMED |
| op13:106-108 (`ADAPTIVE_SELECTION_UNCONTROLLED`, same-replica rule) | Logician | CONFIRMED |
| op13:113-120 (cell = full tuple `(f,n,geometria P,geometria Q,patch,canal,alternativa,target auxiliar)`) | Logician | CONFIRMED |
| op13:141-151 (`SEQUENTIAL_STOPPING=FORBIDDEN` + Howard et al. arXiv:1810.08240) | Logician | CONFIRMED |
| op13:153-161 (`n_star` grid + `NO_CROSSING_IN_GRID` + non-monotonicity caveat) | Logician | CONFIRMED |
| formal/LEAN_HYPOTHESIS_AUDIT.md:34 (`accessesIdeal_iff_mem` biconditional) | Logician | CONFIRMED, path correction: the file is at **dev/LEAN_HYPOTHESIS_AUDIT.md:34**, not `formal/`; content matches exactly (row 34: "`x ⇝ I` iff `x ∈ I`" … `PROVED`) |
| biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:171-175 ("infinite sprinkling required" to define event horizon) | Physicist | CONFIRMED (line 173 verbatim) |
| same file :181-193 (bimodal truncated-futures diagnostic, sharp transition at horizon) | Physicist | CONFIRMED |
| same file :223-225 (`Θ_out(r=2M)=0`, quasi-local apparent horizon) | Physicist | CONFIRMED |
| same file :195 (Hayward regular-BH failure of the partition) | Physicist | CONFIRMED |
| op11:41-61 ("finite 1+1D patch definition") | Physicist | **UNCONFIRMED as characterized** — lines 41-61 define `K^+_{M,lambda}` with `omega ∈ S^2` (full, untruncated angular sphere) inside a document explicitly titled "OP-1.1 — Target esférico y clausura dual en Schwarzschild **3+1D**" (op11:1). This is a 3+1D spherically-symmetric patch, not a "1+1D" patch; the file's only "1+1D" mention (line 351) refers to a *different* paper's toy limit, not this patch definition. |
| op11:180-188 (dual channels `fixed_n` vs `order+number`, Poisson intensity `PPP(rho·mu_g)`) | Physicist | CONFIRMED |
| op12:96-98 (`ell_eff(n;g)=(mu_g(K_g)/n)^{1/4}`) | Physicist | CONFIRMED |
| op11:32-37,343-345 (Kruskal `32M³/r` convention flagged `[UNVERIFIED_EXACT_KRUSKAL_NORMALIZATION_LOCAL_SNAPSHOT]`) | Physicist | CONFIRMED |
| docs/plan_operativo_15_julio_2026.md:313-336 (OP-2.1 spec, terminals) | Plan anchor | CONFIRMED |
| :326 (PR011 bench-only, "nunca como nueva confirmación física") | Plan anchor | CONFIRMED |
| :667-678 (forbidden list, "Qué NO autoriza este plan") | Plan anchor | CONFIRMED |
| :646-663 (stop-rules table, "Reglas de parada") | Plan anchor | CONFIRMED |
| :310 (Phase-2 deps: `PHASE_0_AUDIT_READY` + OP-1.3 probado) | Plan anchor | CONFIRMED |

- Notes: One citation does not support the claim it was used for: the physicist's "finite 1+1D patch definition → op11:41-61" points to a patch definition (`K^+_{M,lambda}`) that the source document itself frames as the **3+1D** spherically-symmetric target (full `S^2`, no angular truncation) — not a 1+1D patch. If the physicist's OP-2.1 argument leans on a genuinely 1+1D finite-patch definition, that anchor should instead point to the actual 1+1D geometry frozen in `nachocausal/thresholds.py` (the "tall box" geometry comment) or `docs/preregistration_001_addendum.md`, not `op11:41-61`. All other dossier citations were opened and confirmed to exist at (or very near) the cited lines and to say what the expert claimed, including one path fix (logician's Lean audit citation lives at `dev/LEAN_HYPOTHESIS_AUDIT.md:34`, not `formal/LEAN_HYPOTHESIS_AUDIT.md:34` — the dossier's own "(locate the actual file)" caveat anticipated this).

## 8. Synthesis

All seven roles support opening OP-2.1; no role recommends against. The pre-registration verdict
is a conditional PASS and the falsifier found no blocker to the opening itself — but the falsifier
demonstrated that the wave-1 scope, as briefed, contains guardrails that cannot fail. The
committee therefore recommends PROCEED with a scope that adopts every falsifier repair as binding.

**Recommended direction.** Open OP-2.1 with this committee-fixed scope:

1. **Two-layer architecture, not a lone pure function.** Layer 1: `certifier/reference_certifier.py`
   (top-level package directory, see disagreement D3), a pure fixed-sample Hoeffding kernel per
   op13 §3 whose input type is exactly two `[0,1]` float streams plus scalars. Layer 2: a
   **manifest/ledger bench** owning what a stateless call cannot: the frozen cell list `J`, the
   α-budget ledger (`Σ_j α_j ≤ α_total`), the one-shot terminal-run rule, and the structural
   rejection of any sequential path (falsifier modes 1–2; op13:135-139).
2. **Dev pre-registration first.** `dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md` is the first
   deliverable, committed **before** any Monte Carlo draw, declaring: synthetic laws with
   closed-form TV, coverage target, a **new dedicated synthetic-MC seed band disjoint from both**
   `EXPLORE_POOL`/`DEV_SEEDS` **and the virgin band** (falsifier mode 6), the cell budget, the
   OP-2.1 terminal-precedence chain (falsifier mode 4), the distinct return states
   (`ZERO_BOUND` ≠ `ABSTAIN`; ε-unbounded ⇒ mandatory abstain, op13:122-133), and the
   **mutation-detection power requirement** (falsifier mode 3).
3. **Build loop vs terminal run.** Debug iterations are unrestricted dev work; the single run that
   emits an OP-2.1 terminal happens once, after the dev prereg freeze, and is followed by an
   `/auditor` pass before the terminal is recorded (falsifier: independent-falsification gate).
4. **Package integrity beyond the seal.** Before/after checks record sha256 of **every
   pre-existing `nachocausal/*.py` file** (not only `thresholds.py`) so the sealed import surface
   is provably untouched (falsifier freeze-violation iii). A separate Makefile target (or pytest
   marker) isolates the certifier bench from the canonical `make test` (falsifier mode 8).
5. **PR011 integration bench is optional and quarantined.** If used, any `f` mapping PR011 posets
   to `[0,1]` is declared bench-only and non-promotable in the dev prereg (cannot seed OP-2.2
   candidates), or PR011 integration is dropped entirely (falsifier leakage channel i).
6. **Claim boundary.** `POSITIVE_CERTIFIER_REFERENCE_PASS` = coverage/reproducibility of a
   statistical bound. Zero physics, zero recovery, zero 3+1D readiness. Any report restates
   op13 §8 and op13:207-208 verbatim.

**Open disagreements (surfaced, not hidden).**

- **D1 — no-geometry proof.** Mathematician: discharged structurally by the `[0,1]` input type.
  Logician + falsifier: still-open obligation; the type signature proves module-level blindness
  only, never end-to-end stream provenance. **Chair adopts the stricter reading**: the scope
  treats plan:324 as an obligation discharged *inside* OP-2.1 (interface guard + a leak test that
  demonstrably can fail), and a PASS is never citable as end-to-end no-leakage.
- **D2 — what counts as PI authorization.** Logician: the PI's instruction plus sign-off on this
  brief suffices. Falsifier: the instruction predates the scope, so explicit post-decision PI
  signature on the exact scope is required. **Chair adopts the falsifier's reading**: §11 sign-off
  on this brief is the authorization, and the instruction alone authorizes nothing.
- **D3 — module location.** Repro engineer proposed `nachocausal/certifier/` (subpackage of the
  sealed package, seal formally unchanged) while flagging the confusion risk himself; the
  falsifier hardened it (any edit to `nachocausal/__init__.py` mutates the sealed import
  surface). **Chair recommends a top-level `certifier/` package outside `nachocausal/`** so that
  no pre-existing `nachocausal/` file needs any edit; alternative (inside, with hash freeze of
  all pre-existing files) is workable but strictly riskier. This fork is presented to the PI.
- **D4 — citation repairs (literature verifier).** The physicist's "finite 1+1D patch → op11:41-61"
  anchor is UNCONFIRMED as characterized (op11 defines the 3+1D spherical patch); the correct 1+1D
  anchor is the frozen geometry in `nachocausal/thresholds.py` / `docs/preregistration_001_addendum.md`.
  The logician's Lean citation lives at `dev/LEAN_HYPOTHESIS_AUDIT.md:34`, not `formal/`. Neither
  error is load-bearing for the OP-2.1 decision; both are recorded here as the binding correction.

**Ranked alternatives.** (1) Open with the scope above — recommended. (2) Open with the repro
engineer's original single-function scope — rejected: falsifier modes 1–2 make two plan-mandated
verifications (multiplicidad, optional stopping) untestable. (3) Defer OP-2.1 — rejected: both
Phase-2 dependencies are verified satisfied and no role found a blocker.

## 9. Next-step spec

**Reversible steps (run only after PI sign-off on this brief; each is git-revertable and touches
no seal, no validation seed, no PR012/PR013):**

1. **R1 — Dev pre-registration (first deliverable, before any code executes an MC draw).** Write
   and commit `dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md` declaring, at minimum:
   - the synthetic law pairs with closed-form TV (e.g. Bernoulli(p)/Bernoulli(q) and at least one
     continuous-on-[0,1] pair), each with its exact TV value derivation;
   - coverage target `1 − α_total` and the per-cell weighted-Bonferroni budget (op13:110-120);
   - a **new synthetic-MC seed band**, explicitly disjoint from `EXPLORE_POOL`
     (`1_000_000..1_000_039`), `DEV_SEEDS` (`thresholds.py:57`) and the virgin band
     `[2_000_000, 2_999_999]`, with the RNG derivation rule;
   - the OP-2.1 terminal precedence chain, frozen before any bench run (proposal, mirroring
     op13:190-208): `POSITIVE_CERTIFIER_INVALID > REFERENCE_REPRODUCIBILITY_FAIL >
     REFERENCE_COVERAGE_FAIL > REFERENCE_PRECISION_ABSTAIN > POSITIVE_CERTIFIER_REFERENCE_PASS`;
   - distinct return states: `ZERO_BOUND` (valid vacuous certificate) ≠ `ABSTAIN`
     (precision/resources) ≠ `ABSTAIN_GENERATOR_ERROR` (ε not bounded ⇒ mandatory, op13:122-133);
   - the **mutation-detection power requirement**: the coverage bench MUST emit
     `REFERENCE_COVERAGE_FAIL` against the two canonical mutants (anti-conservative radius
     `log(2/α)` for `log(4/α)`; silently dropped ε terms);
   - the one-shot rule: exactly one terminal-issuing bench run after this prereg freezes; repairs
     reopen the prereg with a new version, never a silent re-run;
   - PR011 usage decision: bench-only, non-promotable fixture `f` — or explicitly dropped.
2. **R2 — Module skeleton.** Create top-level `certifier/` (location per D3, subject to PI
   choice) with the pure Hoeffding kernel (op13 §3 formulas) + the manifest/ledger bench layer
   (cells `J`, α-ledger, fixed-sample-only API with **no** incremental/sequential entry point).
   Docstring: "not part of the prereg-002 evaluation path". No edit to any pre-existing
   `nachocausal/*.py` file, including `__init__.py`.
3. **R3 — Bench + guards (all must be demonstrably able to fail).** `tests/` module under a
   dedicated pytest marker + separate Makefile target (never inside canonical `make test`):
   `[0,1]`-domain guard, numpy-pin via `thresholds.assert_environment()`, seed-band guard,
   bit-exact double-run reproducibility, budget-ledger overdraft rejection, sequential-path
   structural rejection, coverage MC per prereg, and the mutation checks of R1.
4. **R4 — Pre/post integrity snapshot.** Record sha256 of every pre-existing `nachocausal/*.py`
   before work and re-verify after every commit, alongside `make verify-seal` (must remain
   `6e2c3888…`); `git status` must show only new files plus the declared new paths.
5. **R5 — Terminal-issuing run (one-shot, after R1–R4).** Execute the frozen bench once; write the
   op13-style manifest (op13:135-139: commit, pip freeze, uname, RNG rule, seed band, per-cell
   parameters, hashes, timestamps); emit exactly one terminal by the frozen precedence chain;
   report it whatever it is (PASS, FAIL and ABSTAIN alike).
6. **R6 — Independent audit.** Run `/auditor` over the terminal-issuing run before the terminal is
   recorded as the OP-2.1 outcome (independent-falsification gate; author ≠ sole verifier).

**Committing steps (each requires its own explicit PI authorization at the time):**

- Any commit/push of OP-2.1 artefacts to `origin/main`.
- Recording the OP-2.1 terminal in the plan/roadmap as the Phase-2 gate input.
- Any subsequent opening of OP-2.2 (witness development) — expressly NOT authorized by this brief.

**Binding rules pre-committed (violating any one voids the OP-2.1 outcome):**

- No edit to `thresholds.py`, prereg-002/003, or the seal `6e2c3888…` (plan:672); no validation or
  confirmatory seed drawn (plan:673); no PR012 action (plan:670, OP-2.4 governs); no PR013
  (plan:671); no 3+1D code (plan:674).
- `SEQUENTIAL_STOPPING=FORBIDDEN` (op13:141-151): the API exposes no incremental path; the Howard
  et al. confidence sequence is not instantiated under OP-2.1.
- The certifier never selects witnesses or cells (op13:83-120); ε-bounds are caller-supplied and
  never silently zero (op13:122-139).
- `POSITIVE_CERTIFIER_REFERENCE_PASS` is a statistics-infrastructure terminal: it licenses no
  physical claim, no recovery claim, no 3+1D-readiness claim (op13:163-174, :207-208; plan:336,674).
- PASS, FAIL, ABSTAIN reported alike; `REFERENCE_COVERAGE_FAIL` is publishable as-is
  (plan:646-663).

**Falsifier's minimal falsification test (binding, part of R3/R5):** monkeypatch the radius to the
anti-conservative `r_j = sqrt(log(2/α_j)/(2m_j))` (and, separately, zero the ε terms) and run the
exact planned coverage MC — `pytest -k coverage` under the certifier marker MUST emit
`REFERENCE_COVERAGE_FAIL` against each mutant. If the bench passes a broken certifier, the bench
is decoration and no OP-2.1 terminal may issue from it.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off

Signed: Nacho / PI

Date: 2026-07-15

Decision: authorize opening OP-2.1 with the committee-fixed scope of section 9 (dev
pre-registration first, two-layer kernel+ledger architecture, new dedicated synthetic-MC seed
band, frozen terminal-precedence chain, binding mutation-detection test, one-shot terminal run
followed by `/auditor`). Fork resolutions: module lives in a top-level `certifier/` package
outside `nachocausal/` (D3, chair recommendation); PR011 integration is retained but quarantined
— any PR011-derived `f` is bench-only and non-promotable, declared as such in the dev
pre-registration. Commit/push of OP-2.1 artefacts and the recording of any OP-2.1 terminal remain
separate committing steps requiring their own explicit authorization; OP-2.2 is not opened.
