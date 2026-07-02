# Comité Decision 011 — patch-ensemble-architecture

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.
>
> **Procedural note:** `comite_decision_010` §9 step 5 anticipated the next committee session
> would close the C1 completion-class question; that question is still open (see §8 below). This
> session (011) was convened on a separate question (architecture) by the PI. The C1
> reconvene is now assigned to session **012** once its prerequisites are met.

## 1. Decision question

¿Es arquitectónicamente sólido reemplazar el selector `longest_censored` por un ensamblaje de
parches locales (cabezas cortas sembradas desde la frontera) como estrategia para reconstruir el
horizonte, primero en 1+1, luego en 2+1, y finalmente en Schwarzschild 3+1?

## 2. Verified state

Facts checked **this session** (2026-07-01):

| Fact | Evidence |
|:-----|:---------|
| `git log --oneline -1` | `eeffc65 dev: PR-003 5-density physical-tail scaling sweep` |
| `git status --short` | (clean) |
| Seal SHA | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` — `make verify-seal` PASS (reproducibility engineer, this session) |
| 5-density sweep verdicts | `LONGEST_TAIL_O_ELL_ADHERENCE = FAILED`; `LONGEST_TAIL_PHYSICAL_CONVERGENCE = EVIDENCE_FAVOURS_SLOW_DECAY_BUT_NOT_IDENTIFIED`; `SEARCH_COMPLETENESS_AT_21600_28800 = UNVERIFIED` — committed in `dev/PR003_NEAR_HORIZON_NOTES.md`, commit `eeffc65` |
| BARE_RELOCALISATION | k*=3/2/3 (no growth); k*·ell halves with ell; committed 2026-06-24 |
| V1 iterative-reseed verdict S3 | HONEST coverage 51%→48%→44% (monotone FALL), OPTIMISTIC 74%→65%→54%; committed `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md`, pre-committed bar FAIL — `docs/hoja_de_ruta_24_jun_2026.md:64,80` |
| `docs/preregistration_002.md` | boundary estimator PASS; validation band `[2_000_000, 2_999_999]` untouched |
| `comite_decision_010` §9 binding rules | five C1 definitions not yet committed; R1/R2/R3 blocked; product-order check not yet run — all still open |

## 3. Dossier

Files and references supplied to the committee:

- `dev/PR003_NEAR_HORIZON_NOTES.md` — 5-density sweep (eeffc65) + BARE_RELOCALISATION
- `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md` — S3 honest coverage table, V1 verdict
- `dev/PR003_ITERATIVE_RESEED_NOTES.md` — exploratory reseed (scored with hidden r, not audited)
- `dev/sweep_near_horizon_density.py` — longest_censored kernel, budget=30000, lmax=120, M=3
- `dev/measure_truncated_head.py` — k* = _kstar(d⊥/ell profile), reference band ADH=3.0
- `nachocausal/selection_guard.py` — `verify_selection_order_only` (single-selector guard)
- `tests/test_leak.py` — current leakage guard coverage
- `docs/pr003_leakage_gate.md` — order-only discipline (contracts 1–5)
- `docs/preregistration_002.md` — boundary estimator seal + prereg-002 PASS
- `docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md` — binding prerequisites
- `docs/hoja_de_ruta_24_jun_2026.md:64,80` — pre-committed convergence bar (coverage must not degrade)
- `formal/HorizonFormal/` — Lean corpus (order-theoretic, no patch/assembly objects)
- `biblioteca/fuzzy_ladders_comprehensive_literature_review.md` — literature synthesis
- EGS arXiv:2605.06813 — primary fuzzy-ladder reference

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

- **Proposed artefact(s):** New `dev/measure_patch_assembly.py` + companion log `dev/patch_assembly.log`
  (naming follows `dev/measure_*.py` family). Must live only in `dev/` — never touch sealed
  validation path. Any new selector should pass through `nachocausal/selection_guard.py:52`
  `verify_selection_order_only` and mirror `nachocausal/c1_selector.py:c1_selector` (line 56) as
  the relabel-invariant precedent.

- **Environment & seal:** `numpy==1.26.4` hard-pinned (`requirements.txt`);
  `thresholds.assert_environment()` hard-fails otherwise. Seal SHA
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` — PASS this session.
  Package-diff-clean check required before any run.

- **Provenance capture:** `git rev-parse HEAD`, `git status --porcelain`, numpy version,
  `uname -a`, seed band (EXPLORE_POOL only, assert not in `[2_000_000, 2_999_999]`), all sweep
  knobs echoed, START/END UTC timestamps, "EXPLORATION ONLY — NOT A RESULT" label.

- **Run mechanics:** Single foreground invocation (small seed subset first), escalate to background
  for full pool. Guard abort points: (1) `thresholds.assert_environment()`; (2)
  `verify_selection_order_only` RAISES if selector is label-dependent — must run BEFORE scoring;
  (3) seed-band assertion.

- **Reproducibility risks:**
  - Order-only adherence proxy does NOT exist (`k*` reads `d⊥` from embedding: `measure_truncated_head.py:113-119`). **This is a central unresolved spec item — [UNVERIFIED] that any order-only surrogate exists in dev/.**
  - Guard-v for multi-seed patch UNION not demonstrated: `verify_selection_order_only` tests single-selector; union-level label dependency has no existing test. `tests/test_leak.py` covers only `estimate_O_volume`.
  - Coverage/"tangential convergence" metric is meaningful only after `r` is revealed for scoring; must never feed back into selection (leakage-gate contract 5).
  - 2+1/3+1 extension needs new sprinkling domain, S¹/S² kernel, and comparables — none exist in `dev/`; premature for any executable step.
  - `make verify-seal` must be re-run before and after any dev run.

### Mathematician brief

- **Computability:** Everything needed is decidable on `C` alone. Future-volume `O(i)=|future(i)|`
  is O(N²), label-invariant (`estimator_v2_seal.md §A`). The τ(n) abstaining gate and T_EDGE_MIN
  domain gate are decidable on order-derived quantities, never on coordinates. **Critical:** fuzzy-
  ladder DFS `longest_censored` is only label-invariant when `complete=True` — under budget/lmax
  censor, `best_len` is a lower bound (`measure_pr003.py:56-57,140-141`). **Short O(1)-rung heads
  are complete-search-decidable and therefore invariant; this is a genuine order-theoretic
  advantage of the proposed architecture.** However, `k*` is read off `d⊥` (hidden coordinate,
  `emb[p,1]`, `sweep_near_horizon_density.py:61`) — NOT order-only, does not survive the leakage
  gate as a selector.

- **Order observable:** Horizon signal: (a) future-volume bracket (prereg-002 PASS); (b)
  `relphi_mean` = mean relative-exteriority of L_fut along the chain (`explore_direction.rel_field`),
  AUC(all) 0.94–0.97. The fuzzy ladder is order-only by interval-cardinality rigidity (EGS Def. 2,
  `measure_pr003.py:104-113`). **Head concentrates horizon information; tail optimises length, not
  adherence** — motivates the architecture change.

- **Relevant invariants:** longest-chain height `Lpast/Lfut` (Myrheim 1978); ordering fraction
  (Myrheim–Meyer dimension, Surya LRR 2019 §4); future-volume `O(i)` (sealed); interval
  cardinality `|I(x,y)|` / `C_k` (EGS §II, Bhattacharya–Mathur–Surya 2023). `d⊥` is NOT among
  them.

- **Analytic target:** d⊥→0 (transverse) AND physical coverage grows (tangential). No published
  order-only adherence result exists to match against; EGS §V uses embedding to identify horizon.

- **Caveats:**
  - **Condition B (tangential coverage) is currently AGAINST the proposal:** S3 honest coverage
    51%→48%→44% (monotone FAIL, `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md`). Coverage scaling [UNVERIFIED].
  - No order-only stopping observable exists; `relphi_cum` extremum at k≈5 misaligns with k*=2–3.
  - Dimensional escalation 1+1→2+1→3+1 is not order-theoretically guaranteed: ladder abundance
    in d>2 unknown, interval-cardinality rigidity is dimension-sensitive.
  - Near-horizon AUC(<3ell): 0.756→0.486 across last two densities; outgoing counts 3/29, 5/42
    — too few to certify `relphi_mean` AT the horizon.

### Mathematical logic brief

- **Formal status:** The entire Lean corpus (`formal/HorizonFormal/`) covers pure order theory.
  **None** of the proposed objects appears in it: "parches locales", "ensamblaje", "compatibilidad
  causal", "cobertura transversal", "S¹/S²" have no formal definition in any committed file.
  Grep finds "parche" only as informal prose; S¹/S² hits are unrelated Python identifiers. This
  is structurally the same defect adjudicated in committee 010 (RECOMMEND_REVISE_AND_RECONVENE,
  five undefined C1 terms; `comite_decision_010:179,238-240`). **The proposal cannot be adjudicated
  in its current form: four of its terms are undefined, so it is a propositional blank.**

- **Quantifier/dependency order:** Seeding layer IS order-only: frontier = level sets of L_past
  (genuine antichains); per-front localiser reuses sealed O. **Post-hoc degrees of freedom
  concentrate in exactly the undefined terms**: seed/frontier rule and NMIN, causal compatibility
  predicate, coverage notion, topology target — all must be frozen BEFORE any convergence claim
  is scored, or `NO_POST_HOC_TUNING` / `NO_GROUND_TRUTH_LEAKAGE` is violated. Both convergence
  conditions (A d⊥→0, B coverage grows) are read off hidden `r`. The binding order: freeze
  definitions → measure. Stage dependency 1+1→2+1→3+1 is NOT monotone: realiser/conjugate-order
  machinery is conditional on dim_DM(C)≤2 (Prop 7.3); at d≥3 order dimension NP-hard
  (`comite_decision_010:72`).

- **Equivalence claims:** No iff or equality relating "patch assembly" to "horizon" is proved.
  "Ensamblaje ≈ sección del horizonte con topología S¹/S²" is a semantic aspiration.

- **Type/object discipline:** A "patch" is a finite ordered element-set; "cobertura transversal"
  and "sección con topología S¹/S²" attribute continuum topological type to a finite discrete set
  — a **category mistake** unless mediated by an explicit limiting object (nerve, persistence
  complex, Poisson-density limit) that does not exist. Transport discipline: every Lean covariance
  theorem (`mapIdealEndOrderIso`, `mapChainEndOrderIso`) is proved for order isomorphisms only;
  patches glued across seeds are related by embeddings — no transport theorem exists
  (`LEAN_HYPOTHESIS_AUDIT.md:124-149,337`). "Causal compatibility between neighbouring pieces" IS
  precisely this unproved embedding-gluing case. "Reconstruir el horizonte" is an undefined
  predicate that collides with the NO_RECONSTRUCTION_CLAIM guardrail.

- **Caveats:**
  - The exploratory reseed (`PR003_ITERATIVE_RESEED_NOTES.md`: per-front d⊥≈0.5ℓ, coverage
    growing) is scored with hidden `r` — hidden-coordinate diagnostic, not an order-only theorem.
  - S3 coverage already FAILED the pre-committed bar (`PR003_ITERATIVE_RESEED_V1_NOTES.md`).
  - "Connected" in the reseed result is weak: any causal link between adjacent-front witness sets,
    not a single through-chain along R_S.
  - 2+1/3+1: no sprinkling domain, no observable, roadmap defers all such physics.
  - τ(n) IS a working order-only stopping rule (`PR003_ITERATIVE_RESEED_V1_NOTES.md`: abstained
    would-cover rate below localised cover-rate at every density). But it is not strong enough to
    make coverage converge.

### Physicist brief

- **Coordinates & patch:** Sealed 2D **Eddington–Finkelstein** coordinates `(t*, r)`,
  `generator.py:115-127`. EF is mandatory (regular across r=2M). Finite tall box
  `t∈[0,6]`, `r∈[0.1,1.3]`, `R_S=0.5`, `M=0.25` (`thresholds.py:37-43`). **Forfeited by
  finiteness:** the true event horizon is teleological (needs 𝒥⁺); the admissible object is a
  local apparent/trapping-precursor. Any verdict is about order-only localisation in a finite
  1+1D patch.

- **Physical meaning of signal:** `O(i)=|future(i)|` — interior futures truncated by the
  singularity → bimodality → bracket localises r=2M. The signal tracks **singularity-truncation
  of futures**, not marginal-null-expansion (Θ_out=0 trapping criterion).

- **Sprinkling domain:** Poisson(intensity) coordinate-uniform, χ² gate verified (`generator.py:
  53-82`). SEARCH_COMPLETENESS at 21600/28800 = UNVERIFIED. Top box edge = sampling wall
  (mimics future-truncation); must be discriminated from horizon by persistence + asymmetry
  (`PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md §2`).

- **Claim boundary:** At most: **order-only localisation of the horizon-associated boundary in a
  finite 1+1D EF patch at discreteness precision O(ℓ)** (exactly prereg-002 PASS object). Does
  NOT claim: extended horizon segment, metric reconstruction, asymptotic/global event horizon,
  2+1D, 3+1D, Kerr, or discrimination of trapping vs. focusing vs. singularity.

- **Caveats:**
  - **In 1+1D the horizon has NO surface to "cover."** The horizon is a single null generator
    (line in (t*,r)); spatial section is S⁰ (two points). The "surface coverage" motivation is
    physically vacuous in 1+1D — the assembly reduces to tiling prereg-002 localisations along
    t on one generator. Coverage argument acquires content only at 2+1 (S¹) and 3+1 (S²).
  - **Head is architecturally the right object; tail is not.** A short head ≈ one local null-
    generator segment (EGS discrete analogue). Discarding `longest_censored` is physically
    justified; the ensemble-of-heads re-scopes to what empirically adheres.
  - **Head-stopping rule is NOT order-only.** k* reads hidden d⊥. relphi_cum extremum at k≈5
    misaligns with k*=2–3. This is the central unresolved gap.
  - **Direction signal fails at the horizon.** AUC(<3ell) = 0.756 (21600) → 0.486 (28800);
    outgoing counts 3/29 and 5/42. At finest density the direction discriminant is chance-level
    precisely where needed.
  - **Two blocking physics prerequisites before any "reconstruction" language:**
    (1) an order-only head-truncation observable; (2) the regular-BH (Hayward) counterfactual
    to establish genuine trapping vs. singularity signal.
  - **3+1 cost/coverage claim [UNVERIFIED]; 2+1→3+1 speculative.**

## 5. Falsifier attack

### Falsifier brief

**Attack 1: The head-termination rule is defined over the hidden coordinate — it cannot be implemented order-only**
- Failure scenario: `k*` in `measure_truncated_head.py:113-119` computes the cutpoint from the `d_perp/ell` profile (hidden coordinate `r` from embedding). The order-only candidate `relphi_cum` fires at k≈5, 2–3 rungs past k*=2–3, with magnitude not density-robust. The ABSTAIN verdict on the order-only detectability channel is committed at `PR003_NEAR_HORIZON_NOTES.md:128-135,158`. Any implementation must either leak `r` (Gate contract 1 violation) or use a mis-aligned breakpoint, producing heads already in the drifting-tail regime.
- Counter-test: Find an order-only observable whose breakpoint aligns with k*=2–3 at ALL five densities. No such observable exists in the codebase.
- Currently distinguishable: **YES** (ABSTAIN verdict committed and anchored).

**Attack 2: Coverage degrades monotonically with density — the assembly already FAILED the pre-committed criterion (LETHAL)**
- Failure scenario: S3 honest coverage 51%→48%→44% across 3600/7200/14400; OPTIMISTIC 74%→65%→54%. Pre-committed bar: "coverage no se degrada (idealmente mejora) con densidad" (`hoja_de_ruta_24_jun_2026.md:64,80`). Verdict: **FAIL**, committed `PR003_ITERATIVE_RESEED_V1_NOTES.md`. Per-piece d⊥/ℓ widens 0.52→0.63→0.88. Root cause: interior outgoing futures starve at higher density — this is a property of the **localiser itself**, not the selector. Switching from `longest_censored` to short-head patches does NOT change the localiser; the failure carries over.
- Counter-test: A 4th density (e.g., 28800) showing HONEST coverage reversing upward, or a modification to the localiser changing the interior-starving mechanism.
- Currently distinguishable: **YES — the verdict is already committed, no additional computation needed.** Read `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md`.

**Attack 3: The direction discriminant AUC(<3ell) collapses to near-chance at highest densities — heads near the horizon are un-orientable**
- Failure scenario: AUC(<3ell) = 0.756 (21600) → 0.486 (28800); outgoing near-horizon counts 3/29 and 5/42 (`PR003_NEAR_HORIZON_NOTES.md:201-208`). At intensity=28800, a selector retaining only outgoing heads within 3ℓ would select 5/47 candidates using a classifier at AUC=0.486. The patch assembly has no usable direction filter precisely in the finest-discreteness regime.
- Counter-test: A direction observable achieving AUC(<3ell) > 0.7 stably across all five densities, or a non-direction orientation criterion.
- Currently distinguishable: **YES** (committed sweep data, eeffc65).

**Attack 4: Guard-v for the multi-patch union is not implemented — the relabel-invariance guarantee does not cover the assembled object**
- Failure scenario: `verify_selection_order_only` (`selection_guard.py:52-84`) tests a single selector on a single matrix. The patch assembly is a UNION of witness sets across L_past time-fronts from multiple seeds. Per-seed Guard-v passes 6/6 (`PR003_ITERATIVE_RESEED_V1_NOTES.md`), but the union-building function has no corresponding test. A tie-breaking bug correlated with spatial position through labelling order would pass per-seed guard but fail union guard. `tests/test_leak.py` covers only `estimate_O_volume`.
- Counter-test: Wrap the full union-building function as a single selector; call `verify_selection_order_only` on it at multiple seeds and densities.
- Currently distinguishable: **PARTIAL** (per-seed passes real; union gap identified but not yet falsified — no failing test constructed).

**Attack 5: The 2+1→3+1 escalation route is architecturally undefined and cannot be evaluated**
- Failure scenario: `generator.past_matrix_fast` accepts only `"BH"` (1+1D). No 2+1/3+1 code, data, or pre-registration exists at HEAD eeffc65. Five load-bearing terms of the proposal have no operational definitions. In 2+1D the `O(i)` observable has different scaling (2+1D Alexandrov interval volume ~r³, not r²), which could break `two_means_split`. The escalation is purely verbal.
- Counter-test: A 2+1D BTZ causal set with AUC > 0.9 for boundary localisation.
- Currently distinguishable: **NO** (no 2+1/3+1 code or data).

**Minimal falsification priority:** Attack 2 is cheapest and most discriminating — it is already decided. Reading `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md` suffices. The failure is lethal to the proposal as stated because the root cause is in the localiser's density behaviour, not the selector.

## 6. Pre-registration verdict

### Preregistration warden brief

**Freeze status — frozen (binding):**
- `prereg-002` (boundary estimator PASS) + sealed v2 instrument + thresholds.py seal SHA
- `prereg-003` (2026-06-25 doc-only): O(ℓ) operational resolution floor — no new constant, no new instrument
- `comite_decision_010` binding rules: five C1 definitions not committed; R1/R2/R3 blocked; product-order check not run

**NOT frozen (therefore not yet measurable as a result):** Any new observable ("short head", "O(1) rungs", "causal compatibility", "coverage ensemble", "patch union"); the head-termination rule as order-only; Guard-v for multi-seed union; relphi_mean direction in this architecture; 2+1 and 3+1 routes; coverage scaling.

**What must be frozen BEFORE any new measurement — ordered checklist:**
1. Run and record the product-order check (`comite_decision_010 §9 step 1`, reversible, mandatory)
2. Close and commit the five C1 definitions (`dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md`) in binding order: observed subposet, admissible completion class `𝔄`, induced reference rule (order-only), pullback rule, incompatibility predicate
3. Convene committee **012** with the closed C1 proposition and product-order check result
4. Define new observables in writing BEFORE any data contact: "short head", head-length rule (order-only), "causal compatibility" (order-only, no embedding), "coverage" (honest denominator), all passing leakage-gate contracts 1–5 in writing
5. Demonstrate Guard-v for the patch union (runnable guard, multi-seed, multi-density)
6. Resolve the head-termination observable gap: formal statement that an order-only stopping rule exists, committed before implementation
7. Prereg-003 addendum for the new architecture (separate committee session)
8. Then and only then: implement, pass Guard-v, run dev probes on EXPLORE_POOL

Items 4–8 are NOT permitted until items 1–3 are discharged.

**What IS permitted NOW:**
- Reading any committed file (read-only)
- Drafting `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` as conceptual draft (not for data contact)
- Running the product-order check script (`dev/alloy/product_order_check_alloy002_witness.py`, prescribed by comite_010 §9 step 1)
- Adding the Lean embedding-gap clarification to `dev/LEAN_HYPOTHESIS_AUDIT.md` (comite_010 §9 step 3)
- Committee deliberation (this session)
- Investigating WHY coverage falls (root-cause analysis, reversible)

**Scope verdict: BLOCK** on five conditions:
- **BLOCK-1 (comite_010 binding rule):** The ensemble of short heads is a de facto new R-selector candidate; R1/R2/R3 development blocked until comite_010's C1 verdict is closed. Only a committee session with a closed C1 proposition can lift this block.
- **BLOCK-2 (leakage gate, contracts 1 and 3):** Exploratory evidence (iterative reseed notes) was scored with hidden `r`; relphi_mean direction not Guard-v verified for the patch-union context. Building architecture on unverified leakage-gate compliance is a FAIL condition.
- **BLOCK-3 (observable undefined — cannot measure what is not defined):** Five load-bearing terms are undefined. Any measurement over undefined observables is post-hoc tuning by construction.
- **BLOCK-4 (scope violation — 2+1 and 3+1):** Outside every existing prereg scope. No registered protocol, no frozen geometry, no leakage-gate framework for d>1+1. Hard scope violation.
- **BLOCK-5 (missing order-only head-termination observable):** Not a caveat — a falsification of the central architectural assumption. No order-only stopping rule for head termination exists or has been proposed in closed form.

**Open PI decisions (only the PI can decide):**
- **PI-1 (direction of attack):** Pursue the `Q`-track (conjugate-order lateral split, the path not attacked by Alloy 002) vs. persist on the maximality/boundary-bracket family (which the ensemble is). Not compatible in the same timeline without explicit prioritisation.
- **PI-2 (2+1/3+1 investment):** New prereg, new geometry, new committee per dimension. Is this in scope for the current phase, or must 1+1 be fully closed first?
- **PI-3 (committee 012 timing):** Five-definition draft must be reviewed by committee 012 before any implementation. PI must authorise the committee 012 session.

## 7. Literature verdict

### Literature verifier brief

**EGS (arXiv:2605.06813) — what it does and does NOT do:**
- Seeds from the **bottom region** (t*/r_S ∈ [0,0.2], §IV.A), **not** from a relational boundary bracket
- Uses **longest-ladder selector** (§IV.A); uses **embedding information** to disambiguate ingoing/outgoing (Appendix C.1) and to select the horizon-approximating ladder (§V.B: "we use the embedding information to identify the origin of an appropriate ladder by simply selecting a ladder that starts very close to r=r_S and that constitutes an outgoing null geodesics")
- Iterative re-seeding is **future work conjecture** (§V.B: "We leave such an iterative procedure to future work")
- Operates in **1+1D only**; explicitly notes fuzzy ladders "defined for (1+1) dimensional settings" (§II.A)
- Does NOT validate order-only direction discriminant, boundary-seeded patch assembly, or density convergence of ladder adherence

**Gap vs. proposed architecture:** The boundary-bracketing strategy and short-head ensemble have no EGS validation. EGS is not prior art for the proposed architecture.

**Patch/ensemble precedent:** None in the biblioteca. Bhattacharya et al. (2023) define ladder molecules for 2D Minkowski only; no patch assembly or ensemble stitching. `fuzzy_ladders_comprehensive_literature_review.md §11,§13 item 9` classifies order-only horizon reconstruction as OPEN. The proposed architecture must be registered as a **novel contribution** if pursued.

**Direction signal precedent:** None. `relphi_mean` is entirely project-internal. EGS §VI.2 acknowledges the need for an order-intrinsic direction discriminant but flags it as "a practical hurdle" due to rarity of ladder crossings. Any claim that relphi_mean implements an EGS-suggested technique would be an over-reading.

**Dimensional scaling precedent:** Explicit literature warnings:
- Bhattacharya et al. (2023): higher d>2 ladders "do not result from a straightforward generalization" (`fuzzy_ladders_comprehensive_literature_review.md §3`)
- EGS §VI: "A main challenge to solve is to find an appropriate generalization of ladders... A tubular 'binding of ladders'... may be a statistically rare subset of a causal set"
- EGS §II.A: "defined for (1+1) dimensional settings"
- Review §13 item 3: ladder abundance in d>2 = **OPEN**; §8 warns of combinatorial explosion
- S¹/S² section topology for 2+1/3+1 horizon reconstruction: **no literatura anchor**

**Novel claims requiring registration:**
1. Short-head patch assembly from relational boundary bracket → horizon reconstruction strategy
2. relphi_mean / relative-exteriority as direction discriminant with AUC>0.94 in 1+1D Schwarzschild
3. Order-only truncation rule for horizon adherence (head stays d⊥=O(ℓ))
4. BARE_RELOCALISATION as a named structural finding with specific density-scaling
5. S¹/S² section topology for 2+1/3+1 ladder generalization [UNVERIFIED against any source]

**Mis-citations / over-readings (anchored):**
1. "EGS §V: subtracted means −0.33 / −0.16" — these numbers are from **EGS Appendix C.2**, not §V. §IV.B.3 (Eq. 25) gives rigid-ladder results (interior −0.039, exterior +0.027).
2. "EGS §II: ladder molecules as null-geodesic analogue" — EGS §II is the causal set theory introduction; ladders are introduced in **EGS §IV.A** (Definition 1).
3. "NP-hardness of order-dimension testing cited at comite_decision_010 §72" — the citation traces to `COMITE_009_C1_RELATIONAL_DOSSIER.md line 72`, not comite_decision_010; and has no direct biblioteca source (Yannakakis 1982 is standard but not in biblioteca as a primary source). Status: [UNVERIFIED against a biblioteca document].
4. "Myrheim 1978: longest-chain/height as geodesic estimator" — no Myrheim 1978 primary source in biblioteca; attribution credible but [UNVERIFIED against a readable biblioteca document].

## 8. Synthesis

### Architectural direction: the re-scoping is correct; the proposal is not yet adjudicable

**Point of consensus across all seven roles:** Replacing `longest_censored` (length-maximising) with
short boundary-seeded heads (adherence-preserving, complete-search-decidable) is the *right
re-scoping* of what survives the 5-density sweep evidence. The head concentrates the horizon signal;
the tail optimises length, not adherence; and short heads have a genuine order-theoretic advantage
(completeness, label-invariance). Discarding `longest_censored` as a full-horizon-portion selector
is justified.

### Lethal blocker: coverage already FAILED the pre-committed convergence criterion

The falsifier's Attack 2 is not a future risk — it is a past FAIL. S3 honest coverage
51%→48%→44% across three densities under the pre-committed bar "coverage no se degrada con
densidad" (`docs/hoja_de_ruta_24_jun_2026.md:64,80`) is a committed FAIL
(`dev/PR003_ITERATIVE_RESEED_V1_NOTES.md`). **This failure lives in the localiser's density
behaviour** (interior outgoing futures starve at higher density — same EGS-identified open
problem), **not in the selector**. Switching from `longest_censored` to short-head patches does
not change the localiser; the failure carries over unless the localiser is modified. The
architecture proposal cannot be declared sound until the root cause of coverage degradation is
understood and a path to fixing it is demonstrated.

### Five structural gaps (from unanimously convergent expert testimony)

1. **No order-only stopping rule** for head termination (Mathematician + Physicist + Reproducibility +
   Logician): k* reads hidden d⊥; relphi_cum misaligns at k≈5; ABSTAIN committed
   (`PR003_NEAR_HORIZON_NOTES.md:128-135,158`). This is the central unresolved architectural
   assumption.

2. **Five load-bearing terms undefined** (Logician + Reproducibility + Warden): "parches locales",
   "ensamblaje", "compatibilidad causal", "cobertura transversal", "S¹/S²" — same situation as
   committee 010 for C1. Cannot measure what is not defined.

3. **Direction signal chance-level at the horizon** (Physicist + Mathematician + Falsifier):
   AUC(<3ell) = 0.486 at 28800, outgoing counts 3–5/30–47. The orientation filter fails where
   needed.

4. **Guard-v for multi-seed union not demonstrated** (Reproducibility + Falsifier): single-selector
   guard passes are not sufficient; union-level label dependency has no existing test.

5. **2+1/3+1 route has no substrate** (Physicist + Reproducibility + Logician + Literature): no code,
   no prereg, no data, literature explicitly warns of difficulty, S¹/S² section topology unanchored.

### What genuinely survives and should be carried forward

- τ(n) IS a working order-only stopping rule for the FRONT (not the head): abstained would-cover rate
  below localised cover-rate at every density (`PR003_ITERATIVE_RESEED_V1_NOTES.md`). Not strong
  enough to make coverage converge, but an anchored positive result.
- Per-piece d⊥/ℓ ≈ 0.5–0.9 across densities — each individual head stays at O(ℓ), physical d⊥
  plateaus ~0.020.
- Guard-v 6/6 at every density (per-seed).
- MINK flat control PASS at every density (locus is BH-specific).
- AUC(all) 0.94–0.97 stable (direction signal is real, just not near-horizon).
- Prereg-002 PASS: the seed generator is sound.

### Dissent on record (not hidden)

- **Physicist vs. scope claim:** The physicist is the only voice explicitly noting that in 1+1D there
  is no spatial surface to cover (S⁰ horizon section), making the "coverage" motivation physically
  vacuous in 1+1D. The 2+1/3+1 route is where coverage acquires content. All other roles treat
  coverage as a meaningful metric in 1+1D (as the tangential convergence condition B). This
  dissent does not change the verdict but contextualises it: even if coverage were to converge in
  the 1+1D reseed, it would measure tiling of a null generator, not a 2D surface.

- **Preregistration warden (BLOCK-1) vs. committee framing:** The warden notes that the ensemble
  constitutes a new R-selector candidate, blocked by committee 010 until the C1 question is closed
  in a separate session (which committee 010 expected to be committee 011). Since this session IS
  committee 011, the blocking condition must be interpreted forward: the C1 five-definition work
  is a prerequisite before the architecture can be revisited (now as committee 012). This committee
  cannot both close the C1 question and adjudicate the architecture in the same session; the two
  questions are sequenced.

### Ranked alternatives

1. **(Recommended)** `RECOMMEND_REVISE_AND_RECONVENE`: close the five definitions + product-order
   check, understand the coverage-degradation root cause, define order-only head-termination
   observable, then reconvene as committee 012 for the C1 question and committee 013 for the
   architecture question once prerequisites are met.
2. `RECOMMEND_DO_NOT_PROCEED` on the 2+1/3+1 route (applicable immediately, unconditionally):
   no substrate exists; should not be a goal in the current project phase without new prereg
   and committee authorisation.
3. `RECOMMEND_PROCEED_WITH_CAVEATS` (inadmissible): a scope BLOCK and an unresolved lethal
   falsification (Attack 2) are active. Per the committee charter, these preclude any PROCEED
   verdict.

## 9. Next-step spec

### Reversible steps (permitted now, may be run if the user asks; no PI authorisation required)

**R1 (HIGHEST PRIORITY — prescribed by comite_010 §9 step 1):**
Run the product-order check: `dev/alloy/product_order_check_alloy002_witness.py`. Output:
`dev/alloy/product_order_check_alloy002_witness_note.md`. Guard: does not read thresholds.py,
does not draw seeds, does not touch validated data. Result must be committed and cited in the
committee 012 dossier regardless of outcome (PASS, FAIL, INCONCLUSIVE).

**R2 (prescribed by comite_010 §9 step 3):**
Add Lean embedding-gap clarification to `dev/LEAN_HYPOTHESIS_AUDIT.md`: transport theorems
proved for isomorphisms only; the embedding-gluing case for patch union has no transport theorem.
Clarification, not new science.

**R3 (root-cause investigation of coverage degradation — NEW):**
Read `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md` §"Why coverage falls" carefully. Investigate
whether the interior-starving mechanism is: (a) a finite-budget artefact fixable with budget
increase, (b) a fundamental property of the sealed localiser in this regime, or (c) a property
that a different seeding rule could avoid. Produce a `dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md`
note summarising the root-cause diagnosis. NO new measurements required; this is a
read-and-analyse step on committed data.

**R4 (draft five definitions — prescribed by comite_010 §9 step 2):**
Draft `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` for committee review: (a) observed subposet
class, (b) admissible completion class 𝔄, (c) induced reference rule (order-only, no r=2M), (d)
pullback rule, (e) incompatibility predicate. Draft must include ground-truth leakage constraint
on term (c). This draft is for committee 012 review BEFORE any witness search; it may be
committed only on PI authorisation after committee 012 endorses it.

### Committing steps (only on explicit PI authorisation; do NOT proceed without sign-off)

**C1 (committee 012 reconvene for C1 question):**
Once R1 + R4 are done: convene committee 012 with the closed C1 proposition and product-order
check result. Committee 012 must issue one of: COMPLETION_NONIDENTIFIABILITY_PLAUSIBLE_FORMALISE,
COMPLETION_NONIDENTIFIABILITY_NOT_ESTABLISHED_RETURN_TO_R_SELECTOR, or a refined verdict.
Only after committee 012 closes the C1 question can R-selector development (including short-head
ensemble) be unblocked.

**C2 (architecture revisit — committee 013):**
Only after C1 closes AND the following are demonstrated:
- (a) Order-only head-termination observable defined in closed form and committed
- (b) Coverage degradation root cause understood; a path to convergence demonstrated (or the
  architecture redesigned to avoid the starving localiser)
- (c) Guard-v demonstrated for multi-seed patch union at three densities
- (d) All five architecture terms ("parches locales", "ensamblaje", "compatibilidad causal",
  "cobertura transversal", head-length rule) defined in writing, order-only, passing
  leakage-gate contracts 1–5
- (e) Prereg-003 addendum drafted and endorsed by a committee session

**C3 (2+1/3+1 route — NOT before a new prereg):**
The 2+1 and 3+1 routes are out of scope for any current phase. If the PI decides to invest in
2+1, a new preregistration (covering sprinkling domain, observable, leakage-gate compliance for
d=2+1, convergence criterion) and a dedicated committee session are required before any
measurement. The recommendation is to close 1+1 first.

### Binding rules pre-committed

- The product-order check (R1) MUST be run and recorded before committee 012 convenes. PASS, FAIL,
  and INCONCLUSIVE are all reported.
- The five-definition draft (R4) MUST be committed in writing BEFORE any witness search or
  architecture probe. Writing after seeing data = post-hoc tuning.
- The head-termination observable MUST be order-only: it must not receive `d⊥` or any embedding
  coordinate. NO_GROUND_TRUTH_LEAKAGE.
- The coverage bar remains the pre-committed criterion: "coverage no se degrada con densidad"
  (`docs/hoja_de_ruta_24_jun_2026.md:64,80`). No threshold loosening.
- EXPLORE_POOL seeds only for any dev probe; RESERVED_002 band `[2_000_000, 2_999_999]` must NOT
  be burned.
- Seal SHA `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` must be verified
  before any dev probe.
- NO architecture measurement proceeds until all five structural gaps in §8 are closed.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

Conceptual label: `ARCHITECTURE_DIRECTION_CORRECT_BUT_NOT_ADJUDICABLE`

Mapping:
- The re-scoping (short heads over long tail) is the correct architectural direction and is
  unanimously supported by all seven roles.
- The proposal as stated cannot be adjudicated: five load-bearing terms are undefined, coverage
  has already failed the pre-committed convergence bar, the central stopping rule is not
  order-only, and 2+1/3+1 is out of scope.
- The path to reconvening is sequenced: R1 + R4 → committee 012 (C1 closure) → C2 prerequisites
  → committee 013 (architecture). Two committee sessions are required before the architecture
  can receive a PROCEED verdict.
- 2+1 and 3+1 routes: RECOMMEND_DO_NOT_PROCEED unconditionally in the current phase.

## 11. User sign-off

_(left blank for the user — decision, date, and any overriding notes)_
