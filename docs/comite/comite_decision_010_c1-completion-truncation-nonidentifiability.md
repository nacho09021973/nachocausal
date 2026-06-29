# Comité Decision 010 — C1 completion/truncation non-identifiability adjudication

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

¿Puede el mismo subposet finito observado admitir dos completions físicamente permitidas que
induzcan decisiones C1 incompatibles sobre el subposet compartido?

## 2. Verified state

Facts checked **this session**, each with its command / file:line.

- **Seal SHA** (command: `python -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('nachocausal/thresholds.py').read_bytes()).hexdigest())"`):
  `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
- **Git HEAD**: `16e04e4 dev: PR-003 C1 relational spec, Alloy verification, tooling infrastructure
  (exploration, NOT results)`; working tree clean (`git status --short --ignore-submodules=all`
  produced no output).
- **No results/ validation files touched**: this is a purely conceptual/logical adjudication; no
  `validate.run()` has been launched; no dev seeds drawn.
- **Prior comité decisions**: 001–009 in `docs/comite/`; this is decision 010.
- **Alloy models present**: `formal/alloy/completion_maximality_invariance_counterexample.als` and
  `formal/alloy/completion_nonidentifiability_interface_counterexample.als` (both committed at
  HEAD).
- **Alloy reports present**: `docs/alloy/alloy_verification_001_completion-maximality-counterexample.md`
  and `docs/alloy/alloy_verification_002_completion-nonidentifiability-interface.md` (committed).
  Both record `ALLOY_VERDICT=ALLOY_COUNTEREXAMPLE_FOUND` at scope `exactly 4 Element`.
- **C1 selector implemented**: `nachocausal/c1_selector.py`; comité 009 preflight confirmed
  `NO_INTERFACE` for all finite posets with `R=Max(C)` (`dev/PR003_C1_RELATIONAL_SPEC.md:168-180`).
- **Proposition status**: `dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md` records 5 terms
  explicitly UNCLOSED before any proof attempt (L91-106): observed subposet class, physically
  admissible completion class, induced reference rule, pullback rule, incompatibility.

## 3. Dossier

Files and references supplied to the committee:

- `dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md` — central proposition + committee question
- `dev/PR003_C1_REFERENCE_ALTERNATIVES.md` — R1/R2/R3 selector alternatives; status OPEN pending adjudication
- `dev/PR003_C1_RELATIONAL_SPEC.md` — C1 spec; §9 preflight result NO_INTERFACE; ASYMMETRY_SCORE / PERSISTENCE_THRESHOLD / BULK_CONTROL / C1_PROMOTION all OPEN
- `docs/alloy/alloy_verification_001_completion-maximality-counterexample.md` — Alloy 001: ALLOY_COUNTEREXAMPLE_FOUND (observed maximality not completion-invariant, scope 4)
- `docs/alloy/alloy_verification_002_completion-nonidentifiability-interface.md` — Alloy 002: ALLOY_COUNTEREXAMPLE_FOUND (same observation does not force same interface decision, scope 4)
- `formal/alloy/completion_maximality_invariance_counterexample.als` — Alloy 001 model
- `formal/alloy/completion_nonidentifiability_interface_counterexample.als` — Alloy 002 model
- `docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md` — truncation confound active; C1/C2 REFINE_CANDIDATES_BEFORE_PROMOTION
- `docs/comite/comite_decision_009_c1-relational-closure-preflight.md` — comité 009 ALLOW_PREFLIGHT_IMPLEMENTATION_ONLY; NO_INTERFACE confirmed
- `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` — full conceptual note; §7 two-face problem (order conjugate Q, III_PENDING_TWO_FACE_LEMMA, tripartition canonical object)
- `dev/LEAN_HYPOTHESIS_AUDIT.md` — Lean hypothesis audit labels
- `formal/HorizonFormal/HorizonFormal/Horizon.lean`, `ChainEnds.lean`, `Ends.lean` — Lean artefacts
- `docs/preregistration.md`, `docs/preregistration_001_addendum.md`, `docs/preregistration_002.md` — sealed prereg and PASS result
- `docs/estimator_v2_seal.md` — sealed estimator (untouched)
- `biblioteca/derived-md/` (EGS arXiv:2605.06813, Surya LRR 2019, Reid 2004, Benincasa-Dowker 2010, Bombelli-Henson-Sorkin)

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief
- Proposed artefact(s): This is a conceptual/logical adjudication, not a probe — so the executable shape is an **Alloy bounded-model artefact + report**, NOT a sealed `nachocausal/` run. The relevant model already exists at `formal/alloy/completion_nonidentifiability_interface_counterexample.als` (`check SameObservationForcesSameInterfaceDecision for exactly 4 Element`), with its report at `docs/alloy/alloy_verification_002_completion-nonidentifiability-interface.md`. Any refinement must land as a new `formal/alloy/*.als` + a new `docs/alloy/alloy_verification_003_*.md` produced by `/alloy-verifier` (skill at `.claude/skills/alloy_verifier/`, gated by `check_alloy_report.py`) — never edited into the committed 001/002 pair. Note the existing report records paths under `/home/adnac/...`; a re-run on this host (`/home/ignac/nachocausal`) will differ in path strings only.
- Environment & seal: No sealed env is invoked by this question. The sealed validation env (`numpy==1.26.4`, per `Makefile` header) and the external Minz clone (`~/cs-horizon-reuse-check/venv_minz`, `CLAUDE.md:27-29`) are NOT in scope. The committing tool is Alloy CLI (`/home/adnac/.local/bin/alloy exec`, per doc 002 §3) — host-dependent, so the binary path must be re-verified locally before any re-run. Mandatory pre-flight regardless of step: `make verify-seal` must still print `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` to confirm `nachocausal/thresholds.py` is untouched; `RESPECT_SEAL_FREEZE` holds because no threshold is read or written.
- Provenance capture: Any new artefact must record: commit (`16e04e4`, tree clean), the exact Alloy invocation + exit code + stdout trace (the doc-002 §4 format is the standard), the Alloy binary version/path as resolved on this host, the scope (`exactly 4 Element`), and a timestamp. Because Alloy bounded checking at fixed scope is deterministic, no seed band applies — and critically **no DEV/virgin seeds are consumed**, so no seed-burn risk.
- Run mechanics: Single foreground invocation (`alloy exec`, exit-0 in doc 002); fully reversible — it writes only a new `.als`/report and reads no sealed state, so it is pre-flight, not a committing step. A guard aborts cleanly by: (a) `make verify-seal` SHA mismatch → halt; (b) Alloy binary not found at the verified path → halt rather than silently skip; (c) report failing `.claude/skills/alloy_verifier/check_alloy_report.py` → reject. No background run needed.
- Reproducibility risks / ambiguities:
  - The Alloy counterexample is **diagnostic, not dispositive**: a scope-4 combinatorial counterexample does NOT establish a physical no-go [`dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md` §"What Alloy results do NOT establish"; DOSSIER fact 8]. Reproducing the trace answers the *encoded* question, not the scientific one.
  - The proposition is **not yet closed**: 5 terms (observed subposet class, admissible completion class, induced reference rule, pullback rule, incompatibility notion) remain undefined [`dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md` §"Required definitions before proof", lines 91-116]. The current `.als` encodes an abstract interface decision, not the "physically admissible completion" of PR-003 (same file, line 218, 247) — so the model is faithful to a *toy* notion only. [UNVERIFIED] whether any committed `.als` constrains completions to manifoldlike/admissible ones.
  - Bounded scope (`exactly 4`) means absence of a larger-scope check is not anchored; a refinement run should record the maximal scope attempted to bound the `[UNVERIFIED]` gap.
  - Host path drift: committed report 002 references `/home/adnac/...`; this session is `/home/ignac/...`. A re-run cannot be bit-identical in recorded paths — only the assertion verdict (counterexample-found) is the reproducible invariant.

### Mathematician brief
- Computability: On the finite causal order alone (a strict partial order, antisymmetric + transitive), the predicates the step relies on are decidable in polynomial time from the order matrix: maximality `Max(C)`, down-/up-sets `down(R)` [dev/PR003_C1_RELATIONAL_SPEC.md:20,38], antichains, order-interval cardinalities `|[x,y]|`, future-volume `|J⁺(x)∩C|`, interval-abundances `C_k`, and the ordering fraction. The conjugate order `Q` is computable as the transitive orientation of the incomparability graph **provided `dim_DM(C)≤2`** (asserted by generator audit, not measured — Prop 7.3) [dev/...NOTES.md §7.3, §7.4.1]; general order-dimension ≥3 testing is NP-hard, but that branch is excluded by the product-order hypothesis. The relevant gate is a *domain gate* that returns `NO_INTERFACE`/abstains when the observed region degenerates (`H[C;R]=∅`) — this is decidable on the order [spec:67,174]. The exact closed form of a `τ(n)` abstention threshold as a function of `n` is **not specified in the DOSSIER** [UNVERIFIED]; only `BULK_CONTROL` is named as OPEN [spec:151, KEY FACT 9]. `Q` is itself a *partial* (not linear) order: it linearises only `P`-incomparable (spacelike) pairs [NOTES §7.2].
- Order observable: The step's interface predicate is a *maximality/boundary* observable: `isInterface[c,e] ⇔ e∈Obs ∧ e is maximal in c` (no element above it) [formal/alloy/...als:27-30], equivalently `R=Max(C)`, `A_R=down(R)`, `B_R=A_R∖down(↓...)` [spec:38,55]. This is the object Alloy 002 attacks. The horizon-carrying alternative the §7 work isolates is the **conjugate-order lateral split**: with realiser `P=L_U∩L_V`, define `x<_Q y :⇔ U_x<U_y ∧ V_x>V_y` and the canonical **tripartition** `{L_A, core_A, R_A}` [NOTES §7.4.1]. The maximality observable carries the *truncation* signal (capped futures), not robustly the horizon; the conjugate split carries the *spacelike/lateral* signal orthogonal to the future the statistic later measures (avoiding §7.5 circularity).
- Relevant invariants: Ordering fraction / Myrheim–Meyer dimension (Reid 2004, `biblioteca/derived-md/Reid_2004_Manifold_Dimension_of_Causal_Sets_arXiv_gr-qc0207103.md`; Surya LRR 2019 §4); order-interval abundances `C_k` with a continuum limit (Benincasa–Dowker, `biblioteca/derived-md/Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md`); longest-chain/height (timelike geodesic proxy); future-volume `|J⁺(x)|` (monotone but truncation-sensitive); order dimension / conjugate order (Dushnik–Miller 1941; Gallai 1967 modular decomposition) [NOTES §7.2-7.4.1]. Relabel-invariance of any such selector is forced by `Aut(C)`-equivariance, and Poisson is the measure that reconciles discreteness with covariance (`biblioteca/derived-md/Discreteness without symmetry breaking a theorem.md`).
- Analytic / continuum target: The bounded claim is recovery of 1+1D Schwarzschild event-horizon structure from order. The continuum benchmark is the Kruskal–Szekeres null-product order `x≺y ⇔ U_x<U_y ∧ V_x<V_y`, regular across the horizon (`ds²=−Ω²dU dV`) [NOTES §7.3, Prop 7.3], with the horizon as the `Θ_out=0` outgoing-null locus per EGS (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:223-225`). A convergent order-only selector must approach this object in the manifoldlike regime [dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md:39-46], not merely satisfy Guard-v.
- Caveats:
  - The Alloy 002 witness is a *genuine* obstruction only to **boundary/maximality-type** selectors, and only at the **unrestricted** order-extension level: the model lets each completion add one ungrounded element to flip an observed element's maximality [als:32-48; report §5], with **no** convexity, dimension-2, sprinkling, or manifoldlike constraint [doc:204-218]. It correctly shows `same observed order ⇏ same interface decision` is non-vacuous, but `combinatorial counterexample ⇏ physical no-go` [doc:222-226].
  - Order-theoretically, the completions used are **not physically admissible for PR-003**: an admissible completion must be (a.s.) a convex/down-set restriction of a Poisson sprinkling of a manifoldlike region, i.e. a **dimension-2 product order** [Prop 7.3]; arbitrary one-element extensions of a 2-element observation are neither convex nor product-order-realisable. The decision question is therefore answered YES at the logical layer, **NOT_ESTABLISHED** at the admissible layer → `NEEDS_PRECISE_COMPLETION_CLASS` [doc:133-136].
  - Stability under sprinkling/truncation favours **convex/interval-local** invariants (`C_k`, ordering fraction restricted to a bulk-controlled region) over global extremal predicates: maximality and future-volume are non-monotone/cap-sensitive under truncation, which is exactly the `R=Max(C)⇒NO_INTERFACE` trivialisation [KEY FACT 1] and the Comité 006 truncation confound [KEY FACT 5]. This is an order-theoretic reason `BULK_CONTROL` must be closed before any selector.
  - The two-face work **does** bear on the question: the conjugate order `Q` is a function of the order's *realiser* (a property of the generator), so it is robust where maximality is not — it is the candidate that the Alloy 002 obstruction does **not** reach. But it is not free: exhaustive bipartition is **refuted** for `|A|≥2` by the worked intercalation counterexample (only the tripartition survives) [NOTES §7.4.1], and `Q`'s uniqueness-up-to-swap requires modular-primeness (Gallai), which is `PLAUSIBLE a.s.` under Poisson but [UNVERIFIED] vs primary citation [NOTES §7.2, §7.4.1]. Hence `III_PENDING_TWO_FACE_LEMMA`, not a closure token.
  - Automorphism equivariance forbids naming a single representative but permits whole orbits / invariant antichains [doc:49-59], and generic finite Poisson sprinklings are asymmetric [doc:58-59, KEY FACT 12]; a no-go resting on exceptional symmetric posets would not settle the physical regime. RESPECT_SEAL_FREEZE upheld (thresholds.py SHA unchanged; no threshold loosening recommended).

### Mathematical logic brief
- Formal status: The central object `COMPLETION_AND_TRUNCATION_NONIDENTIFIABILITY` is an **open existential conjecture**, explicitly marked "dev conceptual note, no code, no data, no freeze, no result" with five terms still UNCLOSED before any proof attempt [dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md L3, §"Required definitions before proof"]. It is not a theorem, not conditional — it is a not-yet-well-formed proposition (its predicate `incompatible` is undefined, L82). The Alloy 002 result is a **proved refutation of a narrow surrogate assertion**, not of the physical proposition. What is mechanically established is: `SameObservationForcesSameInterfaceDecision` is **false** at scope `exactly 4 Element` [completion_nonidentifiability_interface_counterexample.als L54-58; alloy_verification_002 §5, §7 `ALLOY_COUNTEREXAMPLE_FOUND`]. This is a bounded counterexample (∃ at fixed scope), logically valid as a non-vacuity witness; it does **not** discharge any universally quantified physical claim. The Lean artefacts are **definitions plus order-theoretic guardrail theorems**, none of which is the proposition. `RelationalReference`, `RelationalPast`, `RelationalBlackRegion`, `RelationalHorizon` are `def`/`abbrev` [Horizon.lean L17-42]; the proved theorems are monotonicity/lower-set/cover facts. The audit labels these `PROVED_AS_ORDER_TRIVIALITY` and `DEFINITION_FORMALISED` [LEAN_HYPOTHESIS_AUDIT.md].
- Quantifier / dependency order: The proposition has shape `∃ C, ∃ (i1,i2 admissible), [obs(C,i1)=obs(C,i2)] ∧ [pullback(induced(C1)) incompatible-with pullback(induced(C2))]`. The binding order that must be committed *before* the proof is strict: (a) **observed-subposet class** first; (b) **admissible-completion class 𝔄** next — the load-bearing degree of freedom; (c) **induced-reference rule** on completions; (d) **pullback** restricting to shared `C`; (e) **incompatibility** defined last. The post-hoc danger lives entirely in (b) and (e): because 𝔄 and the incompatibility predicate are chosen by the author, an adversary could tune them after seeing candidate witnesses to manufacture either outcome. The doc correctly forbids advancing until these are closed and frozen, and lists `NEEDS_PRECISE_COMPLETION_CLASS` as a verdict precisely for this gap [doc L135].
- Equivalence claims: No `iff` in this proposition is proved. The Alloy result is a **one-way refutation**: it proves `¬(same observation ⇒ same interface decision)` in a model; it says nothing about the converse and nothing about the physical implication. The doc states the honest gap explicitly: `combinatorial counterexample DOES NOT imply physical no-go` [doc L222-226]. The only genuine equivalences in the codebase are Lean order-theoretic ones unrelated to the proposition: `CofinalChainEquivalent_iff_generated_eq` and `accessesIdeal_iff_mem`, both `PROVED_AS_ORDER_THEORETIC_EQUIVALENCE` with physical reading open [LEAN_HYPOTHESIS_AUDIT.md rows 30, 34].
- Type / object discipline: The proposition mixes three type-strata: (i) **finite order objects** (`C`, completions, the Alloy `Completion.lt` strict order); (ii) **algebraic end objects** — `IdealEnd P` is a *subtype of mathlib `Order.Ideal`*, and `ChainEnd` is a *sigma over a quotient*; (iii) **physical objects** (Schwarzschild horizon, sprinkling, metric germ) — which the Alloy model deliberately does NOT encode [alloy_verification_002 §6]. Hazard active: all Lean transport theorems (`mapIdealEndOrderIso`, `mapChainEndOrderIso`) are proved for `P ≃o Q` (isomorphisms) ONLY; completion maps `i : C → C1` are **embeddings**, not isomorphisms — NO current Lean transport theorem applies to them. The induced-reference pullback in the proposition is exactly the unproved embedding case.
- Caveats:
  - The Alloy `isInterface` predicate is a bare order-only maximality-style condition (`no ((e→Element) & c.lt)`) [als L27-30]; it is an explicit combinatorial *surrogate* for the C1 interface decision, not the C1 decision itself. Supports only `LOGICAL_NONIDENTIFIABILITY_LAYER_SUPPORTED / PHYSICAL_LAYER_OPEN` [doc L160-163].
  - No current Lean theorem bears on the completion proposition. The Lean bridge is labelled `[CONCEPTUAL_FORMULATION]`, "a vocabulary bridge, not a promotion of C1 and not a physics result" [NOTES §9.5].
  - Automorphism caveat is logically correct [doc §"Automorphism caveat" L48-56]; NOT a no-go in the physical regime (generic Poisson: `Aut(C)` trivial) [doc L58-59].
  - `COMPLETION_NONIDENTIFIABILITY_PLAUSIBLE_FORMALISE` is the correct order of operations: 𝔄 and incompatibility predicate MUST BE committed (frozen) BEFORE witness search to prevent post-hoc tuning via definitional gerrymandering [doc §"Required definitions" L122-136].

### Physicist brief
- Coordinates & patch: The step must sprinkle in ingoing Eddington–Finkelstein `(t*, r)`, `t* = t + 2M ln|(r−2M)/2M|` (EGS eq 6; `biblioteca/derived-md/Towards black-hole horizons…md:140`). The 1+1D induced metric `ds² = −f(r)dt² + f(r)⁻¹dr²` with `f=1−2M/r` (EGS eq 5/8) has `det g = −1`, so coordinate-uniform Poisson = natural-volume Poisson with constant density (EGS:135). The patch is a finite `t*–r` box (hidden `M, ρ`, extent). Forfeited by finiteness: there is no `𝒥⁺`, hence **no event-horizon claim is admissible** — a finite poset can carry only an apparent/trapping precursor (EGS §III:173-175; teleological THEOREM-CONFIRMED, `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md §1`). Kruskal regularity across `r=2M` makes the radial order a 2D product order (Prop 7.3), so the EF chart singularity at `r=2M` is a chart artefact, not an order break.
- Physical meaning of the signal: The order-only observable (estimator-v2 future VOLUME `|future(i)|`) tracks `r=2M` because **interior minimal elements have singularity-truncated futures** — every interior timelike curve reaches `r=0` in finite proper time, bounding its longest chain and future cardinality; exterior futures are limited only by box size (EGS §III:181-193). This yields the **bimodal** distribution of future-size over minimal elements whose `∂` between modes localises the horizon (EGS Fig 3). Physically this is the boundary of `Past(γ₀)` for an infinite-length curve `γ₀` (EGS eq 9).
- Sprinkling domain: Declared region = a single `t*–r` box of the 1+1D Schwarzschild submanifold; Poisson process with natural volume measure, constant intensity; primary endpoint intensity 12000, `t_edge=6` domain gate (`docs/preregistration_002.md:41-57`). Matched controls: box-identical flat Minkowski (no horizon) and truncated no-horizon patches. Forfeited guarantees: the box top is a sampling wall that mimics future-truncation isotropically near the top level — the horizon-truncation vs domain-edge-truncation confound.
- Claim boundary: The PASS verdict claims **localisation/recoverability** of the hidden `r=2M` — the order *remembers* the horizon. It does NOT claim the order *defines* the horizon. Explicit regular-black-hole caveat: the future-truncation partition **fails for Hayward-type regular black holes** (EGS:195).
- Caveats:
  - The Alloy 002 witness is a 4-element pair of completions with unconstrained `lt`; no faithful Schwarzschild embedding, Poisson measure, curvature, common local germ, or continuum convergence [alloy_verification_002 §6]. Non-manifoldlike: a single point's causal relations in a sprinkling are fixed by its embedding and cannot flip a bulk bimodal partition.
  - The physically admissible completion class = 2D-product-order manifoldlike extensions of the `f(r)` family, with the No-Spurious-Horizon correspondence: `r=2M` concentration in the Schwarzschild limit, vanishing horizon probability in the Minkowski limit [NOTES §9.3; EGS eq 12].
  - The matched-flat control **helps** identifiability of the signal: converts "is there a horizon?" into a class-discriminating test. Does **not** convert recoverability into definition, nor eliminate the finite-patch top-wall confound.
  - A genuinely admissible non-identifiability instance does exist, but it is NOT the Alloy witness: a **Schwarzschild patch and a Hayward (regular-BH) patch** can share the same near-horizon observed suborder while the singularity-truncation that defines the trapped region lives in the deep-interior `r→0` OUTSIDE the observed patch (EGS:164-169,195). These are real recoverability-limiting completion confounds, not intrinsic logical incompatibility on the shared bulk.
  - [UNVERIFIED] that typical 2D Poisson product-orders are modular-prime a.s. (uniqueness of conjugate-order lateral split) — not anchored to a primary citation in `biblioteca/`.

## 5. Falsifier attack

### Falsifier attack
- Concrete failure modes:
  1. **The question is unanswerable as stated because C1 has no closed decision function.** Three of the four load-bearing components of C1 are explicitly `OPEN` at `dev/PR003_C1_RELATIONAL_SPEC.md:114,97,152`: `ASYMMETRY_SCORE = OPEN`, `PERSISTENCE_THRESHOLD = OPEN`, `BULK_CONTROL = OPEN`. There is no closed C1 decision procedure against which incompatibility can be measured.
  2. **The only closed C1 selector, R=Max(C), trivialises universally and cannot produce any decision at all.** `down(Max(C))=C` for every finite nonempty poset → `B_R=∅` → `H[C;R]=∅` → `NO_INTERFACE` (`dev/PR003_C1_RELATIONAL_SPEC.md §9; nachocausal/c1_selector.py`). The unique closed selector cannot produce a decision, incompatible or otherwise.
  3. **Five formal terms are undefined, making the proposition not-yet-a-proposition.** `dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md:91-106`. The committee is being asked to adjudicate a sentence with five undefined subject terms. Any verdict is a verdict about a propositional blank.
  4. **The Alloy 002 counterexample encodes bare maximality as `isInterface`, not any closed C1 decision.** `formal/alloy/completion_nonidentifiability_interface_counterexample.als:27-30`: `isInterface[c,e]` is just `no ((e -> Element) & c.lt)`. This is not the project's C1 interface `H[C;R]` (which requires cover edges from `B_R` into `A_R`, a persistence trace, and a closed asymmetry score). `docs/alloy/alloy_verification_002_completion-nonidentifiability-interface.md §6` acknowledges this explicitly.
  5. **Alloy scope is exactly 4 elements only; absence of larger-scope countercheck is unanchored.** The check `for exactly 4 Element` was not extended to scopes 5, 6, or higher. A counterexample at the smallest nontrivial scope does not bound the rate at which physically admissible witnesses appear or fail to appear.
  6. **The Alloy 002 witness is not a manifoldlike Poisson sprinkling and cannot be.** The witness is a one-element extension of a two-element observation. Mathematician brief confirms: "one-element extensions of 2-element observation are neither convex nor product-order-realisable." The 2D-product-order constraint (Prop 7.3) rules out the witness.
- Ground-truth leakage:
  1. **"Induced reference rule" is undefined and can silently encode the horizon location.** Defining what reference is "physically correct" in a completed Schwarzschild spacetime requires identifying where `r=2M` is — using the hidden embedding to *define* the observable, not just score it. This violates CLAUDE.md founding rule: "The hidden embedding (ground truth) only scores; it never defines or guides the observable."
  2. **The physically admissible completion class `𝔄` could be constrained to completions that contain a horizon.** If `𝔄` includes "completions of the Schwarzschild spacetime" based on horizon presence, ground truth has entered the domain of the proposition.
  3. **The Schwarzschild-vs-Hayward near-horizon example (physicist brief) is a real but leaky case.** Constructing this witness requires knowing the horizon location in both spacetimes — using ground-truth geometry to *define* which patches are compared.
- Freeze violations:
  1. **The Alloy 002 witness was found before the five defining terms were frozen.** The Mathematical Logic brief states: "𝔄 and incompatibility MUST BE frozen BEFORE witness search to prevent post-hoc tuning." The witness came first; the definitions are still open. Any committee verdict that endorses the witness under subsequently-frozen definitions retroactively ratifies a search that preceded its own specification — the exact post-hoc tuning structure the founding rules prohibit.
  2. **Any Alloy 003 model adding physical admissibility constraints after seeing the Alloy 002 witness is model-level post-hoc tuning.** A refinement that tightens admissibility *after* observing that Alloy 002 witnesses are non-admissible is tuning the model class to fit the known result. The correct order: freeze admissibility constraints first, then search.
  3. **A PLAUSIBLE verdict could be used to unblock R1/R2/R3 implementation — constituting an unregistered probe trigger.** R1/R2/R3 are not registered candidate selectors with frozen Guard-v obligations; unblocking them via a conceptual verdict would constitute an unregistered probe surface.
- Verdict coercion:
  1. **PLAUSIBLE_FORMALISE is not logically bounded above.** There is no guardrail preventing a future dossier from citing a `PLAUSIBLE` verdict as if it established the physical obstruction. The verdict can silently escalate to ESTABLISHED in downstream notes.
  2. **`NEEDS_PRECISE_COMPLETION_CLASS` has no downstream binding force.** Neither preregistration document specifies what happens if a formal sub-question returns INCONCLUSIVE. INCONCLUSIVE on the formal question has no defined effect on the project state.
  3. **Both PLAUSIBLE and NOT_ESTABLISHED allow selector development to continue — asymmetry in reportability.** If the definitions are undefined in both cases, neither verdict is falsifiable against the proposition.
  4. **Silent abstention collapse: `LOGICAL_NONIDENTIFIABILITY_LAYER_SUPPORTED` asymmetrically endorses the logical layer.** The current summary `LOGICAL_NONIDENTIFIABILITY_LAYER_SUPPORTED / PHYSICAL_LAYER_OPEN` is not neutral INCONCLUSIVE — it collapses PHYSICAL_LAYER_OPEN into a more prestigious reading.
- Premature / over-broad claims:
  1. **"Physically permitted" in the decision question is not yet defined.** The Alloy witness is not physically admissible by the project's own physicist brief. Calling this a question about "physically permitted" completions is over-broad.
  2. **A committee verdict is being sought on a proposition that has not been translated into a checked formal object.** The Alloy models check surrogates; the committee verdict goes beyond their formal backing.
  3. **The decision question conflates sub-claim (L) (logical layer, established at scope 4) and sub-claim (P) (physical layer, explicitly OPEN).** Answering (L) positively and using it to support (P) is a scope violation.
- Independent-falsification gate:
  - **Gate is NOT satisfied for the physical layer.** The proposition, the Alloy models, and the committee dossier were all authored and run by the same project team. No independent external logician or physicist has attempted to construct or refute the physical admissibility of the Alloy witnesses.
  - **Gate is partially satisfied for the logical layer only:** the falsifier role constitutes an adversarial within-committee pass. This does not satisfy the gate for the physical layer.
  - **The Alloy results are not independently reproducible in this session.** Committed reports reference `/home/adnac/.local/bin/alloy exec`; this session runs on `/home/ignac`. Re-run requires re-verified Alloy binary path (read-only mandate in this session).
- Minimal falsification test: Take the exact `lt`-relations from the Alloy 002 witness (`docs/alloy/alloy_verification_002_completion-nonidentifiability-interface.md §4`) and verify, by explicit product-order embedding check, whether either completion is realizable as a 2D product order on a finite subset of Minkowski or Schwarzschild (i.e., whether there exist two total orders whose product contains the `lt` relation as a sub-order, respecting the convexity constraint). If neither completion passes this check — which Prop 7.3 and the manifoldlike constraint predict — then the Alloy witness establishes nothing about the physical proposition and the correct summary is `PHYSICAL_LAYER_EMPTY_EVIDENCE`, not `PHYSICAL_LAYER_OPEN`. **This is executable, does not require a BH/MINK run, does not burn any seed, and directly exposes the worst failure.**

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: PASS
- Freeze status: All thresholds for this committee step are already frozen in writing before any validation seed has been seen or analysed. The prereg-002 seal records every frozen numeric value (`docs/preregistration_002.md:7-9`). The proposed step touches none of those values. The five open terms in `dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md:93-106` are pre-proof definitional gaps in a downstream conceptual track; none maps to any frozen threshold in `docs/preregistration_001_addendum.md:49-53` or `docs/preregistration_002.md:42-56`. Seal SHA confirmed: `thresholds.py` SHA256 = `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (`docs/preregistration_002.md:7-9`; DOSSIER verified state matches exactly).
- Seal integrity: The proposed step does not execute the sealed validation path. `docs/preregistration_002.md:59-63` states the single blind `validate.run()` on these seeds has not been run yet. This conceptual adjudication is upstream of that run and leaves the sealed path entirely unchanged. The Alloy 002 model is a bounded logical verification with no sealed-path execution. Seal SHA to confirm: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- Seed discipline: No seed is drawn, evaluated, or consumed by this adjudication. The validation band is `[2_000_000, 2_999_999]` (`docs/preregistration_002.md:15-28`). The dev band and burned prereg-001 set are both untouched. Virgin validation band is intact.
- Reporting rule: The binding reporting rule at `docs/preregistration_002.md:59-68` applies to the single blind `validate.run()` outcome only. The proposed verdict vocabulary (PLAUSIBLE_FORMALISE / NOT_ESTABLISHED_RETURN_TO_R_SELECTOR / NEEDS_PRECISE_COMPLETION_CLASS) carries no numeric threshold and does not constitute a result reportable under the validation reporting rule.
- Forbidden moves present? No. No post-hoc tuning, no threshold loosening, no ground-truth leakage into validation seeds, no re-run after peeking, no reconstruction over-claim, no C1 promotion (`dev/PR003_C1_RELATIONAL_SPEC.md:153` keeps `C1_PROMOTION` explicitly OPEN and blocked).
- Reasons:
  - The preregistration covers the bimodality-based boundary pipeline for the single blind validation run. C1/C2 are downstream extensions explicitly kept OPEN; this adjudication operates on that downstream open track, not on the sealed instrument.
  - `R=Max(C)` trivialising to NO_INTERFACE is a confirmed structural negative authorised as a scoped negative preflight by comité 009. The COMPLETION_AND_TRUNCATION_NONIDENTIFIABILITY question is the logically necessary next step before any R-selector replacement.
  - Alloy 002 is a bounded logical counterexample, not a sealed-path execution. The doc explicitly records: "combinatorial counterexample does NOT imply physical no-go" (`dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md:207-217`).
  - The Alloy results do not create independent reporting obligations under the preregistration.

## 7. Literature verdict

### Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| Reid 2004 — `Reid_2004_Manifold_Dimension_of_Causal_Sets_arXiv_gr-qc0207103.md` — Myrheim-Meyer dimension estimator | Mathematician | CONFIRMED |
| Benincasa-Dowker 2010 — `Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md` — layer structure L_i / interval abundances C_k | Mathematician | CONFIRMED |
| Surya LRR 2019 §4 — `The causal set approach to quantum gravity.md` — ordering fraction eq. (14) | Mathematician | CONFIRMED |
| Dushnik-Miller 1941 — order dimension | Mathematician | UNVERIFIED |
| Gallai 1967 — modular decomposition | Mathematician | UNVERIFIED |
| Bombelli-Henson-Sorkin — `Discreteness without symmetry breaking a theorem.md` — no equivariant map from sprinklings to spacetime directions | Mathematician | CONFIRMED |
| EGS arXiv:2605.06813 §IV eq. (12) — `Towards black-hole horizons and geodesic focusing in causal sets.md` — Θ_out(r)=0 at r=2M defines apparent horizon | Mathematician / Physicist | CONFIRMED |
| EGS eq. (5)/(6)/(8)/(9)/(12), §III lines 173-175, §III lines 181-193, Fig. 3 | Physicist | CONFIRMED |
| EGS lines 164-169, 195 (Hayward regular BH caveat, chain-length partition fails) | Physicist | CONFIRMED |
| `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md §1` — [THEOREM-CONFIRMED] finite poset carries only apparent/trapping precursor | Physicist | CONFIRMED |
| Lean: `relationalPast_lower`, `relationalPast_mono`, `relationalBlackRegion_antitone`, `relationalHorizon_lt` — `Horizon.lean`; `CofinalChainEquivalent_iff_generated_eq`, `mapChainEndOrderIso` — `ChainEnds.lean`; `mapIdealEndOrderIso` — `Ends.lean` | Mathematical logician | CONFIRMED |
| `dev/LEAN_HYPOTHESIS_AUDIT.md` lines 35-36 — labels PROVED_AS_ORDER_TRIVIALITY and DEFINITION_FORMALISED | Mathematical logician | UNCONFIRMED |

- Notes:
  - **Dushnik-Miller 1941** and **Gallai 1967**: no corresponding file exists anywhere under `biblioteca/` or `biblioteca/derived-md/`. These are standard combinatorics references invoked by the Mathematician without any local source that can be checked.
  - **LEAN_HYPOTHESIS_AUDIT.md lines 35-36**: both data rows at lines 35 and 36 carry the label `PROVED_AS_ORDER_TRIVIALITY` (for `relationalHorizon_empty` and `relationalHorizon_univ`). The label `DEFINITION_FORMALISED` appears at line 31 (for `ChainEndInIdeal` / `ChainEnd`), not at lines 35-36. The logician's citation bundles `DEFINITION_FORMALISED` into rows 35-36; the file does not support that pairing. This is a minor precision error; the broader claim (that definitions are formalised and that some theorems are order trivialities) is well-supported.

## 8. Synthesis

**Core finding**: The proposition COMPLETION_AND_TRUNCATION_NONIDENTIFIABILITY is not yet well-formed. It contains five undefined terms (including the predicate `incompatible` itself), making it impossible to adjudicate as either PLAUSIBLE or NOT_ESTABLISHED in any binding scientific sense. Any verdict short of NEEDS_PRECISE_COMPLETION_CLASS is epistemically premature.

**Consensus across all roles:**
- The Alloy 002 result establishes `LOGICAL_NONIDENTIFIABILITY_LAYER_SUPPORTED` — the hypothesis is non-vacuous as a combinatorial statement. This is a real and useful finding.
- The physical layer is `OPEN`, not established. Alloy witnesses are not manifoldlike Poisson sprinklings and cannot be (not product-order-realisable). `combinatorial counterexample ⇏ physical no-go`.
- The five undefined terms must be committed *before* any further witness search to avoid post-hoc tuning.

**Key disagreement — physicist vs. logician on physical salience:**
- **Physicist** finds the proposition NOT_ESTABLISHED for the manifoldlike bulk signal; the bimodal partition is determined by near-horizon bulk order already in `C`, and typical single-element extensions cannot flip it. Recommends treating the genuine physical non-identifiability (Schwarzschild vs. Hayward boundary case) as a *recoverability bound*, not a definitional obstruction. Leans toward NOT_ESTABLISHED_RETURN_TO_R_SELECTOR with NEEDS_PRECISE_COMPLETION_CLASS.
- **Mathematical logician** agrees on the formal gap but insists the correct order of operations is PLAUSIBLE_FORMALISE: close the definitions first, then search for witnesses; this is logically prior to answering NOT_ESTABLISHED (which requires a closed proposition to refute).
- **Mathematician** reads the Alloy result as ordering-fraction/maximality-type obstruction only; the conjugate-Q track (not yet reaching Alloy) is the physically robust alternative; aligns with NEEDS_PRECISE_COMPLETION_CLASS.

**Critical unresolved concern raised by falsifier:**
- The Alloy 002 witness was found *before* the five defining terms were frozen. Any verdict endorsing the witness as supporting the physical proposition retroactively ratifies a search that preceded its own specification — the exact structure of post-hoc tuning the founding rules prohibit. This is not a freeze violation in the pre-registration sense (no numeric thresholds touched, warden PASS), but it is a methodological ordering violation at the logical layer.
- The **minimal falsification test** (product-order embedding check on the Alloy 002 witness) is the single most important next step: if the witness is not 2D-product-order realisable, the correct summary is `PHYSICAL_LAYER_EMPTY_EVIDENCE`, substantially weaker than `PHYSICAL_LAYER_OPEN`.

**Ground-truth leakage risk (real, not hypothetical):**
- The "induced reference rule" remains undefined. When defined, it must not identify `r=2M` using the hidden embedding — it must be an order-only construction. This constraint is binding and must be made explicit in the closure of term (c).

**Verdict rationale**: RECOMMEND_REVISE_AND_RECONVENE. The committee cannot issue a PROCEED verdict because the proposition itself is not yet a proposition. The correct path is:
1. Execute the falsifier's minimal falsification test (reversible, no seeds, immediately executable).
2. Freeze the five defining terms in writing, in the correct binding order, before any further witness search.
3. Return to committee with a closed proposition and the product-order test result.

Ranking of alternatives:
1. **(Recommended)** NEEDS_PRECISE_COMPLETION_CLASS → RECOMMEND_REVISE_AND_RECONVENE: close the five terms, run the product-order check, reconvene.
2. NOT_ESTABLISHED_RETURN_TO_R_SELECTOR (physicist position): acceptable *only* if the product-order check confirms the Alloy witnesses are non-admissible; premature until that check is done.
3. PLAUSIBLE_FORMALISE without freezing 𝔄 first: inadmissible — risks post-hoc tuning of the admissibility class.

## 9. Next-step spec

**Reversible steps** (may be run now if the user asks; no authorisation required):

1. **Falsifier minimal falsification test** (highest priority): For the Alloy 002 witness lt-relations (`docs/alloy/alloy_verification_002_completion-nonidentifiability-interface.md §4`), perform an explicit product-order embedding check: do there exist two total orders on {Element$0, Element$1, Element$2, Element$3} whose intersection (= 2D product order) contains the completion A lt-relation and the completion B lt-relation respectively, respecting convexity? This is a finite combinatorial check, executable as a short Python script in `dev/`, producing a note in `dev/alloy/`. If either completion is NOT product-order realisable, update the Alloy summary from `PHYSICAL_LAYER_OPEN` to `PHYSICAL_LAYER_EMPTY_EVIDENCE`. If either IS realisable, the physical layer remains genuinely open and requires further analysis.
   - Location: `dev/alloy/product_order_check_alloy002_witness.py` + `dev/alloy/product_order_check_alloy002_witness_note.md`
   - Guard: does not read thresholds.py, does not draw seeds, does not touch validated data.

2. **Write the five definitions in closed form** (draft): Produce a `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` that commits in writing: (a) observed subposet class, (b) physically admissible completion class 𝔄, (c) induced reference rule (must be order-only, cannot use r=2M from embedding), (d) pullback rule, (e) incompatibility predicate. Draft must include the ground-truth leakage constraint on term (c) as a binding restriction.
   - This draft goes to the next committee session for review BEFORE any witness search.

3. **Document the Lean embedding gap**: Add a note to `dev/LEAN_HYPOTHESIS_AUDIT.md` recording that Lean transport theorems are proved for isomorphisms only; the completion-embedding case remains `HYPOTHESES_OPEN`. This is a clarification, not new science.

**Committing steps** (only on explicit user authorisation; do NOT proceed without sign-off):

4. **Alloy 003 model**: Only after the five definitions are frozen in writing and the product-order check result is known, commission a new Alloy model `formal/alloy/completion_nonidentifiability_physical_admissibility.als` that encodes the closed admissibility class. Run via `/alloy-verifier`. The model must not encode r=2M directly; admissibility must be expressed through order-only structural constraints compatible with Prop 7.3.

5. **Committee 011 reconvene**: Once the product-order check, the five definitions draft, and (if run) Alloy 003 results are available, reconvene the committee with a closed proposition. That session may issue one of: COMPLETION_NONIDENTIFIABILITY_PLAUSIBLE_FORMALISE, COMPLETION_NONIDENTIFIABILITY_NOT_ESTABLISHED_RETURN_TO_R_SELECTOR, or a new refined verdict.

**Binding rules pre-committed:**
- `𝔄` and the incompatibility predicate MUST be committed in writing (step 2) BEFORE any witness search (steps 4+). Violation = post-hoc tuning.
- The induced reference rule (term c) MUST be order-only: it must not receive `r=2M` or any embedding coordinate. `NO_GROUND_TRUTH_LEAKAGE`.
- The product-order check result (step 1) must be recorded and cited in the next committee dossier regardless of outcome. PASS, FAIL, and INCONCLUSIVE reported alike.
- R1/R2/R3 remain NOT implementation targets until a closed verdict is reached in committee 011.
- Seal SHA `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` must still verify before any committing step.

**Independent falsification gate status:** NOT satisfied for the physical layer. Committee 011 dossier must include an independent falsification attempt (separate session, blind to the proposed verdict) before any PLAUSIBLE verdict can stand.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

Conceptual label (dossier vocabulary): `NEEDS_PRECISE_COMPLETION_CLASS`

Mapping:
- The five definitions must be closed and frozen before any verdict on the proposition itself.
- The falsifier minimal falsification test (product-order check) must be executed first.
- R1/R2/R3 development remains blocked.
- No C1 promotion, no dev probe, no threshold change follows from this session.

## 11. User sign-off

_(left blank for the user — decision, date, and any overriding notes)_
