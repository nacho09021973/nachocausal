# Comité Decision 015 — r-var-selector-adjudication

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Adjudicación del candidato R-VAR (`dev/PR003_R_VAR_SELECTOR_SPEC.md`): (1) tesis V.1 de no-go
lógico y necesidad estadística; (2) resolución de la tensión anti-circularidad (`sig_lk` como
proxy logarítmico declarado del volumen futuro `O(i)`); (3) autorización de implementación dev +
pruebas en posets de juguete y sprinkling EXPLORE (hoy prohibidas por comité 014
`NEXT_FORBIDDEN_ACTIONS`); (4) elecciones de freeze F1-F3 (estadístico exacto de `S`, margen de
abstención `μ`, mínimo de `|H|`). Incluye el flag de estado del repositorio: el working tree de
`formal/HorizonFormal/HorizonFormal/Horizon.lean` revierte la corrección de orientación del
commit 110e4af.

## 2. Verified state

Facts checked **this session** (2026-07-03), each with its command / file:line. Anything
unchecked is marked `[UNVERIFIED]`.

- Seal: `make verify-seal` → `nachocausal/thresholds.py` sha256 =
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, MATCHES the frozen record
  `docs/preregistration_002.md:8`. Seal intact.
- git HEAD = `abf90f0` ("docs: document additional Trotter poset-dimension source (auditor
  003)"), branch `main` (`git log --oneline -3`).
- Working tree (`git status --short`): `M INSTRUCCIONES.md`;
  `M formal/HorizonFormal/HorizonFormal/Horizon.lean` (`git diff --stat`: 13 insertions,
  128 deletions). The Horizon.lean modification REVERTS the orientation correction of commit
  110e4af: it deletes the corrected `RelationalHorizon` (HEAD:64-68), the proved theorem
  `relationalBlackRegion_no_escape` (HEAD:110), the tombstone `relationalHorizonOld_eq_empty`
  (HEAD:120), and the `VPoset` non-emptiness witness, restoring the pre-correction `B_R→A_R`
  orientation that HEAD's own tombstone theorem proves empty for every `R` in every preorder.
  The chair did NOT make this edit; its origin is unexplained. Confirmed independently by the
  literature verifier (`git show HEAD:...Horizon.lean` vs on-disk).
- Artefact under adjudication: `dev/PR003_R_VAR_SELECTOR_SPEC.md` (343 lines, untracked, written
  2026-07-03, no commit).
- No validation results produced this session; no seeds touched; only read-only commands and
  `make verify-seal` executed. This adjudication is pre-implementation and does not build on new
  published numbers (auditor not required by the skill rule; however see the falsifier's
  `results/validation.json` staleness finding in §5, referred to `/auditor`).
- Binding constraints re-verified: comité 014 `NEXT_FORBIDDEN_ACTIONS`
  (`docs/comite/comite_decision_014_q-reference-rule-disposition.md:917-921`, `1063-1076`);
  comité 010 verdict `RECOMMEND_REVISE_AND_RECONVENE` + `ALLOY_COUNTEREXAMPLE_FOUND` at scope
  `exactly 4 Element` (`docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md:238`, `:31`).
- Citation correction found by the literature verifier: `EXPLORE_POOL` is defined at
  `dev/explore_seeds.py:23`, NOT at `thresholds.py:57-62` (that range is VALIDATION_SEEDS
  provenance commentary). The reproducibility brief's seed-band requirement stands; the line
  anchor is corrected here.

## 3. Dossier

Files and references the chair supplied to the committee:

- `dev/PR003_R_VAR_SELECTOR_SPEC.md` — the artefact under adjudication (read in full by all roles)
- `formal/HorizonFormal/HorizonFormal/Horizon.lean` (HEAD vs working tree; corrected version via
  `git show HEAD:...`)
- `dev/PR003_C1_REFERENCE_ALTERNATIVES.md`, `dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md`,
  `dev/PR003_Q_A6_4_ROBUST_ABSTENTION_SPEC.md`, `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md`,
  `dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md`
- `docs/comite/comite_decision_010/012/013/014*.md`
- `docs/preregistration.md`, `docs/preregistration_002.md` (+ result),
  `docs/estimator_v2_seal.md`, `docs/estimator_v2_freeze.md`, `docs/estimator_v2_decision_spec.md`
- `nachocausal/c1_selector.py`, `nachocausal/selection_guard.py`, `nachocausal/thresholds.py`
  (sealed), `nachocausal/generator.py`, `dev/explore_seeds.py`, `dev/measure_kbeam_peeloff.py`,
  `dev/measure_pr003.py`
- `biblioteca/`: Eichhorn–Gamito–Stokes arXiv:2605.06813 (derived-md); Dou–Sorkin
  arXiv:0811.4235 (derived-md) and arXiv:gr-qc/0302009 (Horizon.lean header); Surya LRR 2019 §4;
  Benincasa–Dowker arXiv:1001.2725; Bombelli 1987; Reid 2004 (derived-md)

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

- **Proposed artefact(s):** All strictly under `dev/` (exploration sandbox, CLAUDE.md:22). (a) a dev exploration script following the committed `dev/explore_*.py` naming convention — `dev/explore_r_var.py` — implementing 𝒜(C) (spec VI.1), score S (VI.3), the consensus tri-partition/typed-abstention selector (VI.4); (b) a pure-poset toy driver reusing the existing dev measurement pattern of `dev/measure_pr003.py` (per-sprinkling aggregation, `--smoke` 3-seed self-check, `python3 dev/measure_pr003.py --smoke`). Any generated ensembles land in the git-ignored `dev/dev_ensemble_raw/` (CLAUDE.md:24). A companion `dev/PR003_R_VAR_*_NOTES.md`. **No** file under `nachocausal/` (sealed package), no edit to `thresholds.py`, no new `docs/comite` or `docs/preregistration*` artefact — those are committing/frozen surfaces.

- **Environment & seal:** Toy-poset and sprinkling-EXPLORE work runs on the pinned sealed env `numpy==1.26.4` (`nachocausal/thresholds.py:18`, `assert_environment()` at :21-30) — the same pin `dry_run.py` prints. Sprinkling generation, if authorized, uses the external non-vendored c-minz clone at `~/cs-horizon-reuse-check/venv_minz/bin/python` (numpy<2) exactly as `dev/prototype_o.py` (CLAUDE.md:27-29). Re-verify the seal is untouched before and after: `make verify-seal` must print `nachocausal/thresholds.py sha256 = 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` and MATCH `docs/preregistration_002.md:8` (VERIFIED intact this session, DOSSIER). Package-diff-clean: R-VAR is a dev consumer of the poset only — it must not import from the sealed decision path (`nachocausal/validate.py`, `estimator.py`, `gate.py`).

- **Provenance capture:** The run must record: `git HEAD` (currently `abf90f0`, DOSSIER); working-tree cleanliness (see risks — currently dirty: `M INSTRUCCIONES.md`, `M formal/.../Horizon.lean`); `pip freeze`/`numpy.__version__` assertion output; `uname -a`; the seed band actually consumed (must be `EXPLORE_POOL = 1_000_000..1_000_039`, `docs/preregistration_002.md` + `thresholds.py:57-62`); UTC timestamps; and the live seal SHA at start/end. Emit these to the run log header (as `dev/*.log` artefacts already do, e.g. `dev/o3_sealed_numpy_rerun.log`), never into a sealed or docs path.

- **Run mechanics:** Single foreground invocation with a mandatory reversible **pre-flight guard** that aborts (non-zero, before any data is generated) if any of: `assert_environment()` fails; `verify-seal` SHA ≠ frozen; requested seeds ⊄ EXPLORE_POOL or intersect `VALIDATION_SEEDS` (the virgin band `[2_000_000, 2_999_999]`, `thresholds.py:59-74` asserts disjointness); or `selection_guard.verify_selection_order_only` (`nachocausal/selection_guard.py:52-79`) fails on the R-VAR selector (relabel-conjugacy / Guard-v, mandated by the DOSSIER binding constraints). Toy-poset enumeration is fully deterministic, reversible, and touches no seeds. Larger sprinkled N should run in background only after the toy tier passes. **None of this is a committing step**: no threshold value is written, no verdict is produced, no virgin seed is drawn — mirroring `dry_run.py`'s "verdict DISCARDED" discipline (`nachocausal/dry_run.py:1-8`).

- **Reproducibility risks / ambiguities:**
  - **Blocking authorization gap:** the entire run (toy enumeration counts as "enumeración/búsqueda de contraejemplos"; sprinkling as "simulación/sprinkling") is currently a `NEXT_FORBIDDEN_ACTION` under comité 014 (DOSSIER; `docs/comite/comite_decision_014*.md:917-921,1063-1076`). Adjudication (3) is exactly the request to scope a new authorization superseding this; absent it, the pre-flight guard should refuse to run. [anchored]
  - **Dirty working tree / provenance mismatch:** the spec anchors on the *corrected* orientation `Horizon.lean:64-68/110` (spec §0, lines 22, 33-35), but the working tree has reverted commit `110e4af` to the provably-empty `B_R→A_R` orientation (DOSSIER; `git diff --stat` 13(+)/128(−)). Any dev run citing that file reads bytes that disagree with `git show HEAD:...`. Restore (`git restore formal/HorizonFormal/HorizonFormal/Horizon.lean`) and confirm a clean tree before anchoring — and note the R-VAR spec itself is untracked with no commit. [anchored, DOSSIER]
  - **Anti-circularity leak surface (provenance):** the score uses `d⁺ = sig_lk`, declared a noisy log-proxy of the banned `O(i)` future volume (spec V, VI.3). Provenance guard must assert the selector code path never imports the volume estimator nor the hidden embedding (the embedding "only scores" — CLAUDE.md founding rule; `dev/prototype_o.py:14` "never feeds estimator"). This is verifiable but must be an explicit test, not an assumption. `[PLAUSIBLE risk — the E[d⁺]≈ln(ρV)+γ derivation is itself marked PLAUSIBLE/unanchored in spec V]`
  - **Poly-time claim is unproven:** `|𝒜(C)|` is exponential; the `dim≤2` realizer-DP is a `[PLAUSIBLE, no desarrollado]` sketch (spec VI.6). At sprinkled N up to 12000 (`thresholds.INTENSITIES`) full enumeration is infeasible, so any budget/lmax cap re-introduces the censoring/label-dependence wound already documented in `dev/measure_pr003.py` (#1/#2 header) — a determinism and reproducibility hazard that must be measured, not assumed. [anchored]
  - **Freeze must precede validation:** F1 (statistic/normalisation), F2 (margin μ), F3 (min |H|) are open (spec VII). The dev run must not read `VALIDATION_SEEDS` nor calibrate μ against them; μ's "null patches" basis must be frozen from EXPLORE data only, before any sealed run — else `NO_POST_HOC_TUNING`/`RESPECT_SEAL_FREEZE` are at risk. [anchored, prereg-002 seal]

### Mathematician brief

- **Computability:** Everything R-VAR needs is decidable in poly time on the strict partial order alone (antisymmetric+transitive, no coordinates): `Min`, `Max`, the cover/link relation `⋖` (`IsCover`, HEAD Horizon.lean:57–61), down-sets `↓X`, the interface `H[C;D]` (Horizon.lean:64–68), out-cover-degree `d⁺`, and cardinalities — cf. comité 010:72 (same predicate class decidable in P). The candidate family `𝒜(C)` is a *total* function of `C` (evaluable for every finite poset), with a *typed domain gate* replacing the earlier `τ(n)` gate: EMPTY_FAMILY / INCOHERENT_ARGMAX (both order-decidable) and LOW_CONTRAST-vs-`μ`. Note: the `τ(n)` closed form remains unspecified elsewhere (comité 010:72 `[UNVERIFIED]`); R-VAR does not depend on it, it abstains via `μ`. `Q`/realizer machinery is only invoked as a *search structure*; the output is realizer-independent because `𝒜` and `S` are defined by `≤` alone (VI.6) — this is a genuine improvement over Q (no `REALIZER_DISAGREEMENT` channel).

- **Order observable:** `S(C,D) = mean_{(x,y)∈H[C;D]} [ d⁺(x) − d⁺(y) ]`, where `d⁺(z)=#{w : z⋖w}` is the future *link/cover* degree (EGS: a link is the nearest-neighbour relation `≺*`, derived-md "Towards black-hole horizons…":122). Horizon signal: the trapped side has singularity-truncated futures ⟹ depressed future valence; contrast peaks where truncation onsets. This is a **link-degree proxy** for EGS's discrete geodesic *expansion*, which "changes sign across the black-hole horizon" (EGS abstract; §IV, derived-md:281 expansion = log-change of null-congruence cross-section). It is *not* the sealed estimator-v2 future-volume `O(i)` and *not* EGS's ladder expansion — it is a new, distinct order-only functional.

- **Relevant invariants:** future cover-degree `d⁺` (out-degree in the Hasse/link matrix); future-volume `|J⁺(x)∩C|` (the frozen estimator-v2 observable, comité 001:77, estimator.py:113); longest-chain/height (Bombelli 1987 PhD; Reid 2004, `derived-md/Reid_2004_…`); ordering fraction → Myrheim–Meyer dimension (Surya LRR 2019 §4); interval abundances `C_k` (Benincasa–Dowker 2010, `derived-md/Benincasa_Dowker_2010_…1001.2725`). All are `Aut(C)`-equivariant permutation invariants (comité 001:77 leakage-gate contract 3).

- **Analytic / continuum target:** Part IV's collimation target — admissible cut boundaries converge backward onto `r=2M` at `e^{-κΔt}` (κ = surface gravity as Lyapunov/expansion exponent). The principled continuum benchmark is the **past attractor of the outgoing null congruence = event horizon**, i.e. the sign-change locus of the geodesic expansion (EGS §IV; focusing/expansion, derived-md:281), with the Le Cam `O(ℓ)` band as the accepted resolution floor (comités 010/012). Correct target; convergence *rate* is `[estándar, no anclado]` in the spec and I could not anchor `κ`-as-Lyapunov to a primary biblioteca cite this session → treat Part IV as motivation, `[UNVERIFIED]`.

**Per-claim verdicts (as required):**

- **Lemma 1 (collapse to `𝒟(C)`): CORRECT.** `A_R=↓R` is a lower set and `↓↓R=↓R` by transitivity — exactly `relationalPast_lower` + `le_trans` (HEAD Horizon.lean:88–91); `H` reads `R` only through `A_R,B_R`, and `R↦↓R` surjects onto `𝒟(C)`. One condition to record: the D-ANCHOR restriction `D=↓(D∩Max(C))` is a **proper subclass** of `𝒟(C)` (down-sets generated by non-global-maximals are excluded); this is a legitimate physical choice, not a theorem, and should be labelled definitional (the spec does so).

- **Lemma 2 (one-way automatic): CORRECT.** It is literally `relationalBlackRegion_no_escape` (HEAD Horizon.lean:110-area theorem: `B_R` upper set ⟹ no `x≤y` from black region into past). Automatic for every `D` ⟹ correctly barred as an admissibility condition by founding rule 1.

- **Lemma 3 (interface non-empty + crossing-edge orientation): CORRECT-WITH-CONDITIONS.** The orientation half is a clean proof (a cover `y⋖x`, `x∈D` down-set ⟹ `y∈D`, so no `B→D` cover). Non-emptiness genuinely requires the stated hypothesis **weak connectivity of the Hasse diagram**; a low-density sprinkling can be Hasse-disconnected, so this is a real precondition, not decoration — keep it as a stated hypothesis/theorem, never as a silent guarantee.

- **T1/T2 (degeneracy of ⊆-extremal cuts): CORRECT-AS-MOTIVATION / [UNVERIFIED] as theorems.** The order-theoretic kernel is sound: `𝒜(C)` has ⊆-minimal single-generator cuts `↓{m}` and ⊆-maximal cuts, and the ⊆-order alone does not isolate the horizon cut — consistent with the completion/truncation nonidentifiability (comité 010, Alloy 001/002 at `exactly 4 Element`). But the specific "singularity-basin vs late-exterior" identifications are continuum-geometric, unproven, and conditional on the sealed generator; the spec flags this. Do not treat as established.

- **`E[d⁺] ≈ ln(future volume)+γ` (2D Poisson): CORRECT-WITH-CONDITIONS (functional form).** Independent check: expected future-link count `= ∫∫ ρ e^{−ρV(u,v)} dV`; in null coordinates `V∝uv`, the `v`-integral gives `∫dv/v`, which diverges **logarithmically** with future extent, so `E[d⁺] ∼ ln(ρ·Area)+const`, the constant an exponential-integral `γ`. The form is right; the integral *as written* (`∫∫ρe^{−ρuv}dudv`) drops the ½ null Jacobian and the finite bounds, and the coefficient is scheme-dependent — so it substantiates a **monotone log relation in expectation**, which is the load-bearing point. Consequence for adjudication (2): this means `sig_lk`/`d⁺` is a *consistent monotone proxy of the banned `O(i)`* in the mean. The A6.4-II.1 "no functional determination" defense is technically true per-realization (links don't fix volume exactly) but **weak** — it does not remove the distributional overlap with the prereg-002 PASS truncation signal. The real firewall is role-separation + hidden-embedding-only-scores, not statistical independence; the committee should not accept "no functional determination" alone as resolving the circularity.

- **Poly-time via dim≤2 staircases: CORRECT-WITH-CONDITIONS (and better-founded than claimed, but the sketch is incomplete).** The `dim_DM(C)≤2` premise is essentially *guaranteed*, not merely audited: any 1+1D metric is conformally flat and causal structure is conformally invariant in 2D, so a sprinkling's order is the 2D product order of the two null coordinates (two linear extensions = a realizer) — comité 010:72,78, comité 011:137; realizer computable in P (dim-2 recognition/transitive orientation of the incomparability graph), NP-hardness only at dim≥3. Anchored down-sets = monotone staircases: correct. **Two gaps the sketch glosses, both coinciding with open freeze choices:** (i) `S` is a **mean** over `H` (normalized by `|H|`) — maximizing a ratio is not a plain additive DP; it needs parametric/Dinkelbach DP (still poly), and this is exactly freeze F1 (mean-vs-sum/normalization); (ii) the output uses the **full argmax set** `𝒜*` and its consensus intersections `T,E` — there can be exponentially many optimal staircases, so computing `⋂` in poly time requires a forced-in/forced-out DP marking, which the spec does not provide. Rate the end-to-end poly-time claim **PLAUSIBLE**, contingent on F1 and on a consensus-intersection algorithm being specified before any implementation authorization.

- **Caveats (anchored):**
  - Working-tree `Horizon.lean` reverts commit 110e4af to the `B_R→A_R` orientation, which `relationalHorizonOld_eq_empty` (HEAD:120-area) proves **empty for every `R` in every preorder** — the entire spec (H at Horizon.lean:64–68) is only well-posed against the *committed* orientation. Any dev authorization must be conditioned on restoring HEAD first; building on the on-disk file would build on a provably empty interface. Anchored: DOSSIER git state + HEAD tombstone theorem.
  - The score `d⁺`-contrast is a *new* observable distinct from both the validated estimator-v2 `O(i)` and EGS's ladder expansion; its horizon-tracking is a `[predicción física, NO evaluada]` (spec VI.3). No numeric support exists this session (comité 014 NEXT_FORBIDDEN_ACTIONS in force).
  - Part IV `κ`-Lyapunov rate `[UNVERIFIED]` against a primary biblioteca cite (spec self-flags `[estándar, no anclado]`); EGS anchors only the *sign-change of expansion across the horizon* (§IV), not the backward `e^{−κΔt}` collimation rate.
  - Thesis V.1 (completion-reversibility ⟹ no order-only logical invariant) is order-theoretically *coherent* and matches comité 010's `RECOMMEND_REVISE_AND_RECONVENE` + Alloy `ALLOY_COUNTEREXAMPLE_FOUND` at `exactly 4 Element`, but comité 010:77–78 already ruled that combinatorial completions there are **not admissible** (non-convex, non-product-order) ⟹ `combinatorial counterexample ⇏ physical no-go`. So V.1 must be registered against the **admissible (convex, dim-2 product-order) completion class**, not the unrestricted one, or it inherits the same `NEEDS_PRECISE_COMPLETION_CLASS` gap — a conjecture to formalize, not an established no-go `[UNVERIFIED]`.

### Mathematical logic brief

**Formal status (per-claim classification, adjudication (a)):**
- **Lemma 1 (collapse to ↓R / down-set lattice)** — PROVABLE, elementary (`↓↓R=↓R` by transitivity); *not yet mechanised*. The attached bijection "`𝒜₀(C)` ≃ proper non-empty `M⊆Max(C)` mod `↓M=↓M'`" is a genuine, true equivalence (in a finite poset `↓M=C ⟺ M=Max(C)`, `↓M=∅ ⟺ M=∅`), also unmechanised. Status label in spec ("formalizable en Lean en una línea") is accurate.
- **D-ANCHOR / N3** — DEFINITIONS (physical commitments), not theorems. Correctly typed as such (spec VI.2 table).
- **Lemma 2 (one-way automatic)** — the *only* claim backed by an ACTUALLY-PROVED Lean theorem: `relationalBlackRegion_no_escape` (HEAD Horizon.lean, proved: `fun hxy => hx (relationalPast_lower hxy hy)`). Sound; the decoration inference ("automatic ⟹ cannot be an admissibility condition") is valid.
- **Lemma 3 (interface non-empty)** — CONDITIONAL theorem (hypothesis: weakly-connected Hasse diagram), provable, unmechanised; sketch is correct.
- **T1/T2 (ceiling/floor degeneracy)** — CONTINUUM/geometric INTERPRETATION, conditional on the sealed generator's intended patch; not order-theoretic theorems, not numerically checked. Correctly flagged conditional.
- **Collimation (Part IV)** — PHYSICAL CONJECTURE/interpretation, self-marked `[estándar, no anclado a cita primaria]`; not a poset statement at all.
- **Thesis V.1 (logical no-go)** — CONJECTURE (correctly registered as such), *not well-posed as written* (see below).
- **V.2 (statistical necessity)** — CONSEQUENCE/interpretation downstream of V.1; conjectural.
- **Equivariance VI.5** — PROVABLE, high confidence, near-trivial (every object built from `≤`, argmax-as-set and ⋂ are symmetric); unmechanised, "por construcción" is honest.
- **Computability VI.6** — PLAUSIBLE sketch, conditional on `dim_DM(C)≤2` (Prop 7.3, itself conditional); explicitly "esbozo, no desarrollado".

**Quantifier / dependency order (adjudication (b)):** The intended freeze order is correct in principle — F1–F3 must be fixed *before* validation data. But thesis V.1's quantifier body is under-specified: it reads "para cualquier maximal `m ∈ Max(C)` existen **completaciones admisibles** donde `m` escapa y … donde `m` está condenado" — i.e. `∀m∈Max(C). ∃c₁,c₂ ∈ 𝒦. (m escapes in c₁) ∧ (m doomed in c₂)`, where the domain `𝒦` = "clase de completación puramente combinatoria" and the predicate "admisible" are **nowhere defined in writing** in this spec (the Sources table cites comité 010/012 and Alloy 001/002 but no formal completion-class definition). Until `𝒦` and "admisible completion" are written down, V.1 has no truth value, and the downstream implication "reversible ⟹ ningún invariante lógico order-only puede condenar a ningún elemento" is an inference over an undefined quantifier domain. The Alloy 001/002 counterexamples exist only "at exactly 4 Element" (comité 010:31) — a bounded existence witness, **not** the universal `∀C` claim V.1 makes.

**Equivalence claims:** Only Lemma 1's `↓`-equivalence and the `𝒜₀`↔`M` bijection are genuine (provable, unmechanised) iff-statements. `relationalHorizonOld_eq_empty` and `relationalBlackRegion_no_escape` are the sole *proved* (Lean) statements in the entire dependency graph. Everything the physics rides on — T1/T2's "⊆-maximal cut ↔ singularity basin", collimation's "cut boundaries = horizon up to `O(e^{-κΔt})`", V.1's reversibility — is one-way/semantic/asymptotic, not a proved equivalence.

**Type / object discipline:** Clean where it matters. Candidates are order *ideals* (down-sets `𝒟(C)`), i.e. equivalence classes of raw references `2^C` under `↓`-closure — the quotient is handled correctly, no set/ideal confusion. Score `S` and `d⁺` are order-only (cover counts). The one discipline hazard is the mapping `(T,E,U) ⊆ C` → "singularity basin / exterior / horizon band": that is an order-subset-to-continuum-region correspondence realisable only through the hidden embedding, and the spec correctly confines it to a *falsifiable prediction* (VI.4) rather than a definition — no `NO_GROUND_TRUTH_LEAKAGE` violation. **Anti-circularity, the load-bearing point:** what the founding rule and A6.4 II.1 actually prohibit is *functional* determination of `O(i)` (II.1 requires checking the **whole** selector: `dev/PR003_Q_A6_4_ROBUST_ABSTENTION_SPEC.md:186-190`). R-VAR's functional uses *only* `d⁺` = future cover-degree = second component of `sig_lk` (`...:302`, ADMISSIBLE `...:319`), which does **not** functionally fix future volume `O(x)` (distinct cover-degree-preserving posets have distinct volumes). So at the functional level R-VAR is non-circular; the declared tension `E[d⁺]≈ln O(i)+γ` is *statistical correlation*, a different (weaker) relation than II.1 bans. That distinction is logically sound — but the spec only *asserts* the compositional (whole-selector) check; it does not exhibit the class-by-class argument that no composed functional recovers `O(x)` on any element class (the II.1 residual channel is proved only for the *components*). That gap is the real content of adjudication (2).

**Caveats:**
- Working-tree reversion is destructive to the whole spec, not cosmetic (adjudication (c)). The on-disk `RelationalHorizon` (working tree Horizon.lean:38-42) is the `B_R→A_R` orientation; by `relationalPast_lower` (still present) it is **provably empty for every `R`**, so `H[C;D]=∅ ⟹` Lemma 3 false, `S(C,D)` = mean over ∅ **undefined**, and R-VAR degenerates. The spec is written against HEAD and says so (spec:30-35).
- The reversion also **deletes the guardrail, not just the correct definition**: `grep` of the 138-line working tree finds no `no_escape`, no `relationalHorizonOld`, no tombstone, and **no `VPoset` non-emptiness witness** (all present and proved at HEAD). HEAD's design comment states the witness is "what lets the formalisation fail"; removing it means the reverted (vacuous) file *compiles clean* with no failing check. This is a "guardrail-that-cannot-fail" regression (a deleted falsifier) and independently warrants restoration before any Lean work — regardless of the R-VAR decision. [Anchored: HEAD `git show`; working-tree grep, both this session.]
- Hidden post-hoc DOF in F1–F3 (adjudication (d)): **F1** leaves mean-vs-median and normalisation *open* — a statistic family from which one could be selected after seeing separation; the choice `d⁺` vs the offered alternative `sig_sp` (spec V, "funcional alternativo … perfil de incomparabilidad") is a **second, un-frozen fork** and must be collapsed to one before freeze. **F2** `μ` "calibrado sobre parches nulos sin horizonte" is a data-derived threshold on EXPLORE null patches — precisely the `NO_POST_HOC_TUNING`/`NO_THRESHOLD_LOOSENING` surface; it must be pinned to a principled basis and frozen, not fit to a target abstention rate, and it inherits estimator-v2's still-open false-positive axis (iv). **F3** minimum `|H|` is a free integer that could silently drop argmax members. All three are the genuine degrees of freedom; the spec's own "CLOSED_UP_TO_FREEZE" label is honest, but none may be fixed under comité-014 `NEXT_FORBIDDEN_ACTIONS` until a scoped authorization is granted.
- Adjudication (3): implementation/toy-poset/EXPLORE-sprinkling are today forbidden (comité 014:917-921, 1063-1076). Nothing in this pre-implementation logic assessment requires lifting that; V.1's ill-posedness (undefined completion class) should be resolved *in writing* first, since testing an undefined proposition in Alloy/Lean is not yet meaningful.

### Physicist brief

- **Coordinates & patch:** The step MUST use the sealed generator's ingoing Eddington–Finkelstein `(t*, r)` coordinates — the BH branch computes `func = r + 2·r_S·log(|r−r_S|/r_S)` and the EF causal recipe of `past_matrix_fast` (`nachocausal/generator.py:88-129`), which is exactly Dou–Sorkin's EF relation (`biblioteca/derived-md/A Causal Set Black Hole_ arXiv0811.4235.md:134,176-186`) and EGS eqs. for `(t*,r)` with constant `det g` (`Towards…md:164-176`). The finite patch is `t* ∈ [0, 6]`, `r ∈ [0.1, 1.3]` with `r_S = 2M = 0.5`, `M = 0.25` (`nachocausal/thresholds.py:37-42`, `numpy_sprinkle` box `edges=[T_EDGE,R_EDGE]`, `center=[3.0,0.7]`, generator.py:44-50). So interior `= [0.1, 0.5)`, exterior `= (0.5, 1.3] = 2.6·r_S`. **Forfeited by finiteness:** the exterior reaches only 2.6 `r_S` — there is no asymptotic region and no `J⁺` in the box, and an event horizon is by definition the past-boundary of `J⁺`, which requires an *infinite* sprinkling (EGS `md:217`). Therefore any verdict is a localisation of `r=2M` in a finite patch, never an event-horizon claim. Note also the patch floor is `r=0.1 ≠ 0`: the actual singularity `r=0` is **not** in the domain; "singularity basin" means the near-floor truncated wedge, not `r=0` itself.

- **Physical meaning of the signal:** Inside the horizon all future light cones tilt monotonically toward decreasing `r` (Dou–Sorkin `md:498`: "as we cross the horizon at r=2 … the links only extend to the left"; `md:452`: "no information escapes … no causal relations from circled to uncircled"), so interior elements' futures are truncated (squeezed against the `r≈0.1` floor and the top edge) while exterior futures run up to `t*=6`. This is the EGS event-horizon diagnostic: longest-chain-from-minimal is bounded inside, extensive outside, giving a **bimodal** distribution sharpening with timelike extent (`md:226-245`) — the same future-truncation asymmetry the prereg-002 PASS measured. The continuum root of the sign is `Θ_out(r)` (outgoing null expansion) `>0` for `r>2M`, `<0` for `r<2M`, `=0` at `r=2M` (`md:288`). The spec's `d⁺` contrast is a *local* read of this same imprint.

- **Sprinkling domain:** Declared region = the cuboid above; **Poisson** sprinkle `n = rng.poisson(intensity)`, points i.i.d. uniform in the box (`generator.py:37-50`); coordinate-uniform equals natural-volume Poisson because 2D EF has `det g = −1` (`generator.py:10-12`, `Towards…md:164`). `N` is Poisson-mean `= intensity` (Minz cross-check default `intensity=420` → N≈420, `generator.py:151`); `BOX_AREA = 7.2`. A Glue-3 χ² uniformity gate (`assert_coordinate_uniform`, `generator.py:53-82`, crit 18.467) can fail on a broken sprinkle. **Forfeited guarantee:** it tests *marginal* per-axis uniformity, not joint 2D (generator.py:26-29) — adequate for a cuboid Poisson process but not a joint-manifoldlikeness certificate.

- **Claim boundary:** A PASS/FAIL/INCONCLUSIVE verdict claims only order-only *localisation* of the `r=2M` cut inside this finite 1+1D EF patch. It does NOT claim: metric reconstruction (`NO_RECONSTRUCTION_CLAIM`), an asymptotic event horizon (no `J⁺`; EGS `md:217`), or any 3+1D result. **Regular-black-hole caveat (from the paper):** the entire future-truncation mechanism is *Schwarzschild-specific* — for regular (e.g. Hayward) black holes timelike curves continue for arbitrarily long proper time inside the horizon, so the longest-chain / future-volume partition "is likely to fail" (EGS `md:249`, `205-213`). The signal is a singularity artefact, not a generic horizon detector.

- **Geometric-claim verdicts (against the actual generator):**
  - **T1 (⊆-maximal cuts → singularity basin):** *plausible-unanchored (mechanism supported).* Consistent with the patch: interior top-wall maximals exist (uniform sprinkle over `t*∈[0,6]`, `r∈[0.1,0.5)`), and enlarging `D` toward them shrinks `B_D` to the near-floor truncated wedge. Backed in *mechanism* by EGS `md:226-245` and the tilting in Dou–Sorkin `md:498`, but the specific ⊆-order/basin statement is not numerically verified (spec.md:118-127 flags "no verificados numéricamente"). Anchors: thresholds.py:37-42; generator.py:44-50.
  - **T2 (⊆-minimal cuts → single-maximal past cone, untrapped late exterior in B):** *plausible-unanchored.* `↓{single exterior maximal}` satisfies N3 (`B_D ∩ Min(C) ≠ ∅` — interior minimals near `r=0.1` remain in `B`), and its `B` does include late untrapped exterior. Consistent with the patch; not numerically verified (spec.md:129-135).
  - **Part IV collimation (all admissible boundaries converge backward to `r=2M` at rate `κ`, surface gravity as Lyapunov exponent):** *plausible-unanchored / contested.* This is standard GR near-horizon peeling (`κ = 1/(4M) = 1`, so `1/κ = 1` under a `t*=6` wall — numerically self-consistent with the "last ~1/κ band" claim), but it is **not** anchored in the cited literature as stated: EGS treats `Θ_out` and ladder focusing (`md:251-296`) without the κ-Lyapunov framing, and Dou–Sorkin gives the EF relations (`md:134-186`) but no backward-collimation theorem. The spec itself marks it `[estándar, no anclado]` (spec.md:144). Stronger caution: the project's own exploration treats the peel-off as an **open falsification** — `dev/measure_kbeam_peeloff.py:1-` asks whether peel-off is "PHYSICAL" or "algorithmic (greedy myopia)"; so collimation is not established even in `dev/`. Verdict: plausible physics, unverified, actively contested.
  - **VI.3 (`S` = future cover-degree contrast peaks at horizon, vanishes for wall and basin cuts):** *plausible-unanchored, with a caveat.* The *sign/direction* is well-anchored (Dou–Sorkin `md:452,498`; EGS `Θ_out` sign change `md:288`): the trapped side has direction-restricted, truncated futures. But the project's and EGS's *established* horizon tracer is **longest-chain / future-volume** (`md:226-245`), whereas `S` uses local out-degree `d⁺` (cover valence). Cover degree ≠ chain length; a local valence is a plausibly weaker, noisier tracer, and that it specifically *peaks at r=2M* (rather than varying monotonically) is unverified. The wall-cut→0 and basin-cut→0 vanishing rests on near-uniform truncation at the top edge / near the floor — plausible but untested.

- **Caveats:**
  - Physical (not merely logical) near-degeneracy for adjudication (2): the spec's own sketch `E[d⁺] ≈ ln(future volume)+γ` (spec.md:194-196) means `S` is physically *the same future-truncation imprint* the sealed estimator uses, read locally — the committee must weigh this as a **physics** overlap with `O(i)`, not only an A6.4 compositional-rule question. [anchored: spec.md:185-198; mechanism EGS md:226-245]
  - The patch never contains `r=0`; all "singularity"/basin language refers to the truncated `r≈0.1` floor. Any wording implying the singularity itself is sampled would over-claim. [thresholds.py:37-42]
  - Regular-BH non-generality (EGS md:249) means a PASS here certifies a Schwarzschild-EF patch only; the observable is not portable to Hayward-type spacetimes. [EGS md:205-213,249]
  - Repo-state flag (physics reading): the working-tree reversion of `Horizon.lean` restores the `B_R→A_R` orientation, which is physically *backwards* — Dou–Sorkin (`md:452`) establishes causal relations run *into* the trapped interior with *no escape*, i.e. the corrected infalling `A_R→B_R` orientation (HEAD). The provably-empty reverted orientation contradicts the sprinkling's causal structure and must be restored before any formal or dev work. [DOSSIER; Dou–Sorkin md:452; spec.md:30-35]
  - No numbers were produced this session; comité 014 `NEXT_FORBIDDEN_ACTIONS` bars sprinkling/EXPLORE, so every T1/T2/IV/VI.3 verdict above is analytic-only and remains `[UNVERIFIED]` until an authorized EXPLORE run. `RESPECT_SEAL_FREEZE`, `NO_GROUND_TRUTH_LEAKAGE` intact.

## 5. Falsifier attack

- **Concrete failure modes:**
  1. **V.1 proves too little for the conclusion it licenses.** The quantifier body (spec dev/PR003_R_VAR_SELECTOR_SPEC.md:169-176) reverses only maximals (`∀m∈Max(C)`), yet the drawn conclusion is "ningún invariante lógico order-only puede condenar a **ningún** elemento". Near-wall maximals are exactly the already-conceded Le Cam band; reversibility there says nothing about deep-past elements, which is where a logical R would live. Moreover 𝒦 ("clase de completación puramente combinatoria") is nowhere defined (logic brief), and the only witnesses are Alloy 001/002 at `exactly 4 Element` under completions the project's own comité-010 record classifies as non-admissible (non-convex, non-product-order — comité 010 mathematician brief, `NEEDS_PRECISE_COMPLETION_CLASS`, docs/comite/comite_decision_010:72-90 region). Adjudication (1) as posed invites laundering a bounded toy counterexample into a physical no-go that then *justifies* the statistical selector. If accepted at all, V.1 must be accepted only as unproven framing carrying NEEDS_PRECISE_COMPLETION_CLASS, never citable as established.
  2. **S is not even well-defined on all of 𝒜(C).** Membership in 𝒜(C) (spec:209) does not require `H[C;D]≠∅`; Lemma 3 delivers that only under Hasse weak connectivity (spec:88-92), which low-density sprinklings can violate (mathematician brief). `media` over an empty H is NaN/crash; F3 (min |H|) — the only fix — is optional ("si se adopta", spec:309). A selector whose score is partial on its own declared domain is broken as specified.
  3. **The selector plausibly reproduces the very T2 degeneracy it was built to escape, via noise.** S is a mean of per-pair d⁺ contrasts with high Poisson fluctuation (A6.4 Firma 5 KNOWN_DEGENERACIES, dev/PR003_Q_A6_4_ROBUST_ABSTENTION_SPEC.md:315-317). Var(S) ~ σ²/|H|: small-interface cuts (T2's `D=↓{m}`, spec:129-131) have the noisiest scores, and argmax over an exponentially large family maximizes noise. The claim that S *peaks at the horizon* is explicitly `[predicción física, NO evaluada]` (spec:238-240); the wall→0 and basin→0 contrast claims of VI.3 are untested (physicist brief). Without |H|-aware normalization frozen in F1, argmax-of-mean is a small-sample-artifact detector.
  4. **μ faces a max-of-many selection effect the spec never addresses.** `max S` over exponentially many correlated candidates is far above any per-cut null quantile. Unless F2 calibrates the *distribution of the maximum* (extreme-value-correct, order-only MC, analogous to the τ(n) table discipline in docs/preregistration_002.md:46-48), LOW_CONTRAST will systematically under-fire and null patches will emit detections.
  5. **Escape is wall-relative, and the bridge to the horizon is a contested conjecture.** D-ANCHOR defines escape as "reaches t*=6" (spec:55-67). The event horizon is teleological and needs infinite sprinkling (EGS derived-md:217; physicist brief). The bridge from wall-cuts to r=2M is Part IV collimation — self-flagged unanchored (spec:144-146), κ-rate [UNVERIFIED] (mathematician), and CONTESTED by the project's own still-open peel-off falsification (dev/measure_kbeam_peeloff.py:1-7: "PHYSICAL … or algorithmic greedy myopia?"). Even a clean PASS of the falsifiable prediction is a wall-anchored escape partition, horizon only modulo an open conjecture.
  6. **Authorization (3) before the algorithm exists guarantees spec/code divergence.** Exact argmax is infeasible (|𝒜(C)| exponential); maximizing a *mean* needs Dinkelbach/parametric DP; the consensus intersection over a possibly exponential argmax set has no specified algorithm (mathematician brief). Any budget/beam/lmax cap reintroduces the label-dependence/censoring wound the project already documented against itself (dev/measure_pr003.py:1-27, wounds #1/#2). Floating-point comparison of means makes the argmax *set* platform-dependent, silently voiding the determinism and equivariance claims of VI.5 (spec:270-276) — F1 must mandate exact integer/rational comparison (cross-multiplied sums) or those claims are false in practice.
  7. **Repo integrity is actively compromised, twice.** (a) The working-tree Horizon.lean reversion (git diff, verified this session) does not merely restore the empty orientation: it **deletes** `relationalBlackRegion_no_escape`, the tombstone `relationalHorizonOld_eq_empty`, and the VPoset witness — i.e., the only mechanized backing of Lemma 2 and the only failing check in the formal layer. A reverted file that compiles clean with no falsifier is a deleted guardrail (founding rule CLAUDE.md:14). The edit is unexplained (chair did not make it): restoration **and** an origin account are preconditions to any authorization. (b) On-disk `results/validation.json` + `results/validation_run.log` contain the prereg-001-era **FAIL** (seeds 11…65537, thresholds sha `ad02cb57…`), while docs/preregistration_002_result.md:12 cites `results/validation.json` as the PASS's raw output. The PASS that V.2 leans on (spec:179-181) is currently backed in this working copy only by the committed transcription — flag to /auditor; do not build further weight on it uninspected.

- **Ground-truth leakage:**
  - **F2 μ calibration is the sharpest leak surface.** If μ is chosen to *separate* generator-labelled BH vs MINK EXPLORE ensembles, the hidden embedding's labels shape the abstention boundary — that is the embedding defining the observable's decision surface, not scoring it. Only admissible basis: an order-only null-model quantile of **max S** (MC on uniform sprinklings, α fixed in advance), mirroring the τ(n) discipline.
  - **The un-collapsed sig_lk/sig_sp fork (spec:196-198) is a deferred leak.** If the fork survives into dev and is settled by which statistic better matches embedding-scored partitions on EXPLORE, the embedding has *guided the definition of the observable*. The committee must collapse the fork now, in writing, on principled grounds.
  - **The sig_sp escape hatch is already a flagged circularity channel.** On minimals, `|spacelike(x)|` determines `O(x)` *exactly* (A6.4:186-195, Firma 8 :249-269, mitigated only by M1's extremal exclusion) — and R-VAR's one real guard N3 (spec:101-111) privileges precisely `Min(C)`. Offering sig_sp as the fallback if sig_lk is judged circular offers a channel that is *worse*, on the exact element class the spec's own hard condition foregrounds.
  - **The sig_lk admissibility anchor is stale.** Firma 5's `CIRCULAR_WITH_PASS = NO … los links no fijan el volumen` (A6.4:302-320) predates this spec's own `E[d⁺]≈ln(ρV)+γ` derivation (spec:193-195). The spec simultaneously cites the audit and derives the fact that undermines it in the mean. Physicist brief: S is *the same* future-truncation imprint the sealed estimator measures, read locally. "No functional determination" alone must be rejected as the resolution (mathematician concurs); if adjudication (2) admits sig_lk, it must do so on the role-separation + hidden-embedding-only-scores firewall explicitly, with a new written class-by-class composicional check (the II.1 obligation the spec asserts but never exhibits — logic brief), not on the stale Firma-5 verdict.
  - κ=1/(4M) and the "banda ~1/κ" come from the hidden geometry; using them to set F3, μ, or U-band reporting windows injects geometry into thresholds.

- **Freeze violations:**
  - Granting (3) while F1 (mean vs median, normalization, arithmetic), the sig_lk/sig_sp fork, F2 basis, and F3 remain open is the canonical explore-then-baptize-as-principled pattern: run EXPLORE, see which statistic "works", then freeze it. **F1-F3 + the fork must be frozen in a committed written artefact before the first scored EXPLORE run**, or NO_POST_HOC_TUNING is decoration.
  - Comité 014's ban is textually unqualified ("**cualquier** simulación, sprinkling, enumeración … **cualquier** análisis estadístico", comite_decision_014:917-921). It may not be read down as Q-scoped; only an explicit superseding committee decision with exact scope (EXPLORE_POOL ⊆ {1_000_000..1_000_039} only, mandatory pre-flight guard per the reproducibility brief, no sealed-path imports) can authorize.
  - F3 as a post-run free integer can silently prune argmax members and flip (T,E,U) — a verdict-changing threshold; freeze it or drop it, never leave it "si se adopta".
  - No virgin-seed exposure is inherent to the ask, but only if the guard *hard-fails* on any seed ∉ EXPLORE_POOL; make that binding, not advisory.

- **Verdict coercion:**
  - **INCOHERENT_ARGMAX structurally cannot fire on a singleton argmax**: for a unique proper D, `T=C∖D≠∅` and `E=D≠∅` always (spec:248-258). So a lone noise-driven maximizer *always* emits a confident tri-partition; the entire abstention burden collapses onto μ — a single point of failure with a known selection-effect weakness (failure mode 4).
  - On null patches, a non-⊥ output is observationally identical to a detection; the spec has no FALSE_POSITIVE reporting channel. Report-alike requires publishing null-patch non-abstention rates with the same prominence as horizon-patch detections.
  - Missing domain types: DISCONNECTED_HASSE / UNDEFINED_SCORE (H=∅). As specified these collapse into a crash or a silent mislabel as EMPTY_FAMILY — an OUT_OF_DOMAIN condition coerced into another verdict type.
  - `U(C)=∅` (zero abstention) reads as maximal success but is also the exact signature of a singleton noise argmax; no disambiguation is specified.

- **Premature / over-broad claims:**
  - The PI framing "el único R distinguible intrínsecamente" is reconstruction-flavoured; the spec's redefinition (consensus object + abstention band, spec:182-184) is acceptable **only** with NO_RECONSTRUCTION_CLAIM and `PHYSICAL_IDENTIFIABILITY_STATUS = NOT_ESTABLISHED` (spec:305) repeated in every downstream artefact.
  - Part IV's boxed "las fronteras de TODOS los cuts admisibles coinciden con el horizonte" is written in factual register while unanchored, κ-rate unverified, and contradicted-as-open by dev's own peel-off instrument; demote to conjecture with a citation obligation before any freeze.
  - Even total success = order-only, wall-anchored escape partition in a finite 1+1D EF patch of *eternal Schwarzschild* (singularity-truncation mechanism; regular-BH "likely to fail", EGS derived-md:205-213, 249). Not an event horizon (teleological), not asymptotic, not 3+1D, not metric.
  - "Formalizable en Lean en una línea" (spec:53) and the theorem-branding of Lemmas 2-3 are untested assertions; Lemma 3's connectivity hypothesis is load-bearing precisely in the sprinkled regime.

- **Independent-falsification gate:** NOT satisfied. Lemma 1/3, T1/T2, colimación, the ln V+γ sketch, and V.1 are all single-session, single-author derivations, none mechanized; wave-1 already caught a real defect in the author's own ln V+γ derivation (dropped ½ null Jacobian — mathematician brief), demonstrating why the gate matters. The proposed implementer of the toy/EXPLORE tests would also be the author of the predictions being tested. Minimum remedy: (i) mechanize Lemmas 1-3 in Lean (after restoring HEAD); (ii) write 𝒦 down and register V.1's precise statement before any Alloy run; (iii) commit the frozen predictions (VI.4's null-abstention and U-band claims) *before* any run so failure cannot be reframed as exploration.

- **Minimal falsification test:** ONE check, conditional on (a) HEAD Horizon.lean restored, (b) an explicit superseding authorization of comité 014's ban, and (c) F1-F3 + the sig_lk/sig_sp fork frozen in a committed document: run the frozen R-VAR selector on the **MINK (no-horizon) members of the paired EXPLORE ensembles only** (same-cloud design, dev/measure_pr003.py header; seeds ⊆ EXPLORE_POOL, pre-flight guard hard-failing otherwise) and report the fraction of null patches emitting a non-⊥ tri-partition. The spec's own VI.4 prediction (spec:266) demands ≈0 by LOW_CONTRAST; any material non-abstention rate falsifies the selector at its weakest joint — the μ/max-of-many/singleton-argmax coercion chain — before a single horizon-patch claim exists, and consumes no virgin seed. If the committee declines to lift the 014 ban, then no test is runnable and the only honest disposition of (3) is DENY-pending-freeze, since an unfalsifiable-but-authorized implementation is exactly the "guardrail that cannot fail" the founding rules prohibit.

Tokens: NO_RECONSTRUCTION_CLAIM, NO_POST_HOC_TUNING, NO_THRESHOLD_LOOSENING, NO_GROUND_TRUTH_LEAKAGE, RESPECT_SEAL_FREEZE.

## 6. Pre-registration verdict

- **Verdict: BLOCK**

- **Freeze status:** No F1-F3 freeze exists in writing anywhere in the repo, and none is being proposed now — the spec itself lists them as "elecciones de freeze pendientes" and the decision question defers them ("a resolución de freeze F1-F3" as items to be chosen, not already chosen) (`dev/PR003_R_VAR_SELECTOR_SPEC.md:239-243, 308-309, 322-323`). The step under adjudication is the *authorization to eventually implement and freeze*, which is exactly backwards relative to `docs/preregistration.md:66` ("Thresholds frozen in writing" before dev/validation seeds are touched) and `docs/preregistration_002.md:3` ("Every value here is frozen BEFORE any validation seed is generated/analysed"). Authorizing dev implementation *before* F1 (exact statistic), F2 (abstention margin μ), F3 (min |H|) are frozen creates the precise sequence the freeze discipline exists to prevent: build code → see toy-poset/EXPLORE numbers → *then* pick the statistic and margin that "look right." The spec's own F2 language — "margen μ... calibrado sobre parches nulos" — describes a threshold that will be *data-derived*, which is admissible only if calibrated on EXPLORE-band data and frozen *before* any validation seed, in writing, with a pre-registered addendum. No such addendum exists or is proposed with a concrete committed procedure; it is deferred to "later."

- **Seal integrity:** `make verify-seal` run this session → `thresholds.py` SHA256 = `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, MATCHES `docs/preregistration_002.md:8`. Seal intact and unrelated to this proposal — R-VAR is a candidate *reference selector*, not a modification of the sealed `estimator-v2` path (`docs/estimator_v2_seal.md`, commit `22b7660`), and the spec does not propose running or touching the sealed path (`dev/PR003_R_VAR_SELECTOR_SPEC.md:3-4` "sin datos, sin freeze, sin commit"). On this narrow point the proposal is compliant. However: seal integrity is necessary but not sufficient — see Reasons below on the working-tree flag, which is a repo-hygiene breach adjacent to (not identical to) seal integrity.

- **Seed discipline:** dev seeds are `EXPLORE_POOL = 1_000_000..1_000_039` (`docs/preregistration_002.md:16`; defined at `dev/explore_seeds.py:23` per the literature verifier's correction), disjoint from the reserved virgin validation band `[2_000_000, 2_999_999]` (`docs/preregistration_002.md:17-18`, `nachocausal/thresholds.py:74-75`). The proposal's item (3) — "autorización de implementación dev + prueba en posets de juguete y sprinkling EXPLORE" — if granted, would use only the EXPLORE_POOL band, not the virgin band; that part is seed-discipline-compatible *in principle*. But item (3) is not merely a seed-band question — it is a **direct request to countermand a standing, explicitly-worded committee prohibition**: comité 014 `NEXT_FORBIDDEN_ACTIONS` bars "cualquier simulación, sprinkling, enumeración o búsqueda de contraejemplos," "cualquier análisis estadístico," and "implementación de código para Q/A6.4/pullback lateral" (`docs/comite/comite_decision_014_q-reference-rule-disposition.md:917-921`). R-VAR is presented as "la vía R directa de C1... no reabre la vía Q" (`dev/PR003_R_VAR_SELECTOR_SPEC.md:8-11`), but VI.3's score is explicitly built on `sig_lk`, "componente ADMISSIBLE en la auditoría A6.4 II.2" (`dev/PR003_R_VAR_SELECTOR_SPEC.md:190`) — i.e., R-VAR's *only* non-decorative discriminating axis is imported machinery from the very A6.4 apparatus comité 014 froze under `NEXT_FORBIDDEN_ACTIONS = implementación de código para ... A6.4`. Labeling this "R directa, not Q" does not exempt it from a prohibition written against the shared underlying statistic. A **new, scoped** authorization is procedurally available (comité 014 itself used this mechanism to authorize `Q_A6_AGGREGATION_SPECIFICATION_ONLY`, write-only, `docs/comite/comite_decision_014_q-reference-rule-disposition.md:900-912`), but that authorization must be *given*, in writing, by this committee, before any code, toy poset, or EXPLORE run — it is not self-granted by writing a spec that requests it. No seed has been burned this session (chair confirms "no seeds touched"), so there is no seed-discipline *violation* yet — but there is no valid authorization for the seed-touching step being requested either.

- **Reporting rule:** Not yet applicable at this pre-implementation stage — no PASS/FAIL/INCONCLUSIVE result is being reported. The binding text is unambiguous and must bind any future EXPLORE run under this candidate exactly as it binds prereg-002: "the outcome ... is recorded and reported regardless of which it is. No post-hoc tuning, no re-running on fresh seeds after seeing a result, no loosening a frozen threshold" (`docs/preregistration_002.md:64-67`). This warden requires that any scoped authorization the full committee might grant explicitly re-state this rule as a condition, and that F1-F3 be frozen and committed *before* the first EXPLORE toy-poset number is generated — not "F1-F3 pendientes de freeze pre-validación" left loose across a whole EXPLORE-implementation phase (`dev/PR003_R_VAR_SELECTOR_SPEC.md:239-243` currently only promises freeze "before any validation data," which is the addendum's minimum bar for *validation*, not for the dev/EXPLORE phase where the actual statistic-shopping risk lives).

- **Forbidden moves present?** Two, both procedural rather than data-level (no data has been touched):
  1. **Implicit threshold-shopping setup.** F1 (mean vs. median, normalization by |H|) and F2 (μ) are left open with only a promise to freeze "before validation" — this is the exact structure that produces post-hoc tuning if EXPLORE implementation is authorized without first nailing F1-F3 down in writing, because "informed by EXPLORE, frozen before validation" is a legitimate procedure but the spec has not committed to the mechanism (which specific EXPLORE-derived quantity may inform F2, what freeze-then-commit gate applies) — this gap is flagged by the reproducibility engineer's brief too ("F1-F3 must be frozen from EXPLORE data only") and is not yet closed in the artefact under review.
  2. **Circumvention-by-relabelling risk on the O(i) exclusion.** §7.5 explicitly prohibits using the estimator's future-volume statistic to select the reference, precisely to avoid circularity with the sealed PASS observable (`docs/comite/comite_decision_014_q-reference-rule-disposition.md:407-408`, cross-referenced `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md §7.5`). The spec's own honesty is commendable — it states outright that `E[d⁺] ≈ ln(future volume) + γ`, i.e., `sig_lk` is "un proxy logarítmico ruidoso de la cantidad prohibida, no la cantidad" (`dev/PR003_R_VAR_SELECTOR_SPEC.md:193-198`) and flags this itself as `REQUIERE ADJUDICACIÓN DE COMITÉ` (`Part VII:298-300`). A monotone-in-expectation log transform of a banned quantity is not automatically outside the ban's spirit merely because it is not the identity function; this warden treats the tension as **unresolved, not resolved-in-favor-of-use** by the "role separation" argument (selector defines / sealed estimator validates / hidden embedding scores) offered in V.2, because role separation protects against *ground-truth leakage*, not against *selector-observable statistical entanglement*, which is a distinct failure mode the O(i) exclusion was written to close. This is squarely a matter for the full committee's mathematician/logician/physicist seats, and this warden's procedural verdict is that R-VAR must not be implemented, coded, or run against EXPLORE data until that adjudication happens — which is exactly what the artefact itself requests, correctly, as `BLOCKING_ADJUDICATIONS_FOR_COMITE (2)`.

  No ground-truth leakage, no threshold loosening, no re-run-after-peeking, and no reconstruction over-claim are present in the artefact itself — it repeatedly and correctly self-limits (`NO_RECONSTRUCTION_CLAIM`-consistent framing throughout, e.g. `PHYSICAL_IDENTIFIABILITY_STATUS = NOT_ESTABLISHED (sin cambio; nada aquí lo establece)`, `dev/PR003_R_VAR_SELECTOR_SPEC.md:305`).

- **Reasons:**
  - **BLOCK is driven by process, not physics.** This warden's remit is the freeze/seal/seed/reporting discipline, and on that narrow remit alone: (a) no F1-F3 freeze exists (`dev/PR003_R_VAR_SELECTOR_SPEC.md:239-243, 308-309`), (b) the requested authorization would lift a standing, named committee prohibition (`docs/comite/comite_decision_014_q-reference-rule-disposition.md:917-921`) on the exact mechanism (A6.4-derived statistics, "análisis estadístico," "implementación de código") the candidate's only real discriminant depends on, and (c) doing so before the anti-circularity tension on §7.5/O(i) is adjudicated risks baking a proxy-of-the-banned-quantity into code that then generates numbers used to *set* F1/F2 — a sequencing hazard the addendum's freeze-before-data rule exists to prevent (`docs/preregistration.md:66`, `docs/preregistration_002.md:3`).
  - **The repo-state flag is an independent BLOCK-reinforcing fact, not this warden's primary basis, but material to trust in any authorization granted today.** Chair confirms: working tree of `formal/HorizonFormal/HorizonFormal/Horizon.lean` reverts the orientation correction of commit `110e4af` (13 insertions, 128 deletions), restoring the `B_R→A_R` orientation that HEAD's own tombstone theorem (`relationalHorizonOld_eq_empty`) proves empty for every R. The spec itself flags this, unprompted and correctly, as `REPO_STATE_FLAG` (`dev/PR003_R_VAR_SELECTOR_SPEC.md:341-343`) and states all of Part I-VI's Lean citations use "la orientación corregida commiteada," not the dirty working-tree version (`:30-35`). This warden treats an uncommitted deletion of a proof-guardrail with no explanation as a state that must be restored (`git checkout -- formal/HorizonFormal/HorizonFormal/Horizon.lean`) or explicitly justified in writing *before* any new authorization is granted that touches formal artefacts, per the logician brief's characterization of it as "a deleted falsifier." Authorizing new Lean/Alloy work (even conceptually adjacent) while this sits unexplained in the working tree is a hygiene violation this warden will not wave through silently, even though item (3)'s explicit scope (dev+toy-posets+EXPLORE) does not itself touch Lean.
  - **What would flip this to PASS:** (i) restore or explicitly justify-and-commit the `Horizon.lean` working-tree state; (ii) full committee adjudicates and resolves (not merely notes) the §7.5/O(i) proxy tension for `sig_lk`, in writing, as its own decision record; (iii) F1 (exact statistic + normalization + min-|H| policy) and F2 (μ, with its "null patches" calibration procedure spelled out as a committed algorithm, not just a phrase) are frozen in a written, committed addendum *before* any EXPLORE_POOL code is run — mirroring the `preregistration_002.md` seal pattern (freeze commit precedes seed use); (iv) the scoped authorization for dev-only + toy-poset + EXPLORE work is granted explicitly, narrowly, and in writing by this committee (analogous to comité 014's `Q_A6_AGGREGATION_SPECIFICATION_ONLY` grant), rather than inferred from the candidate document's own self-authorization request. Until then: **BLOCK** on (2), (3) as scoped in the decision question, and on any premature (4).

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| Dou–Sorkin, "A Causal Set Black Hole" — `biblioteca/A Causal Set Black Hole_ arXiv0811.4235.pdf` / `derived-md/...md:134,176-186` EF causal relation | Physicist | CONFIRMED |
| Dou–Sorkin, same doc, `derived-md/...md:452` "no causal relations from circled to uncircled elements" | Physicist | CONFIRMED (exact string match) |
| Dou–Sorkin, same doc, `derived-md/...md:498` "the links only extend to the left" | Physicist | CONFIRMED (exact string match) |
| Dou–Sorkin arXiv:gr-qc/0302009, cited in `formal/.../Horizon.lean` header comment (orientation source) | Physicist/Mathematician | CONFIRMED — HEAD header explicitly cites it (lines 22-25) |
| Eichhorn–Gamito–Stokes `derived-md/...md:122` link = nearest-neighbour relation | Physicist/Mathematician | CONFIRMED |
| Same doc `md:164` (t*,r) constant-determinant metric | Physicist/Mathematician | PARTIALLY CONFIRMED — prose confirms "constant determinant... constant sprinkling density"; the specific "det g = −1" sits in an `[EQUATION_EXTRACTION_UNCERTAIN]` OCR block; treat the numeric form as UNVERIFIED pending direct PDF-page read |
| Same doc `md:217` event horizon requires infinite sprinkling / no J⁺ in finite box | Physicist/Mathematician | CONFIRMED (line 217 exact) |
| Same doc `md:226-245` longest-chain-from-minimal bounded inside / extensive outside / bimodal | Physicist/Mathematician | CONFIRMED (line 245 exact) |
| Same doc `md:249` + `205-213` regular (Hayward) BH caveat "likely to fail" | Physicist/Mathematician | CONFIRMED (line 249) |
| Same doc `md:281` expansion = log-change of cross-section | Physicist/Mathematician | CONFIRMED (line 281 exact) |
| Same doc `md:288` Θ_out sign change at r=2M; abstract "changes sign across horizon" | Physicist/Mathematician | CONFIRMED (line 288 and abstract line 22) |
| Surya, LRR 2019, §4 — ordering fraction / Myrheim–Meyer dimension estimator | Mathematician | CONFIRMED — §4.1 "Spacetime dimension estimators" |
| Benincasa–Dowker 2010 (arXiv:1001.2725) — interval abundances C_k | Mathematician | CONFIRMED |
| Bombelli 1987 PhD — longest-chain/height as order invariant | Mathematician | CONFIRMED (raw PDF line 1429: "the height [as] the length of the longest path") |
| Reid 2004 (`derived-md/Reid_2004...md`) — longest chain ~ proper time | Mathematician | CONFIRMED |
| `nachocausal/generator.py:88-129` past_matrix_fast (EF causal recipe) | Repo anchor | CONFIRMED |
| `nachocausal/generator.py:44-50` box center [3.0,0.7], edges | Repo anchor | CONFIRMED |
| `nachocausal/thresholds.py:37-42` patch t*∈[0,6], r∈[0.1,1.3], r_S=0.5 | Repo anchor | CONFIRMED |
| `thresholds.py:57-62` EXPLORE_POOL 1_000_000..1_000_039 | Repo anchor | **UNCONFIRMED / MISCITED** — `EXPLORE_POOL` is defined at `dev/explore_seeds.py:23`; `thresholds.py:57-62` is VALIDATION_SEEDS provenance commentary. Corrected in §2 |
| `thresholds.py:59-74` VALIDATION_SEEDS virgin band disjointness assert | Repo anchor | CONFIRMED (spans lines 59-75) |
| `nachocausal/selection_guard.py:52-79` verify_selection_order_only | Repo anchor | CONFIRMED |
| `dev/PR003_Q_A6_4_ROBUST_ABSTENTION_SPEC.md:186-190` compositional closure rule II.1 | Repo anchor | CONFIRMED (rule text at 186-195) |
| Same file ~:302, ~:319 sig_lk definition / ADMISSIBLE_COMPONENT | Repo anchor | CONFIRMED |
| `docs/comite/comite_decision_010...md:31` ALLOY_COUNTEREXAMPLE_FOUND at exactly 4 Element | Repo anchor | CONFIRMED (exact line 31) |
| Same file `:72,77-78` poly-time decidability; completions not admissible / NEEDS_PRECISE_COMPLETION_CLASS | Repo anchor | CONFIRMED |
| `docs/comite/comite_decision_014...md:917-921` NEXT_FORBIDDEN_ACTIONS | Repo anchor | CONFIRMED |
| `dev/measure_kbeam_peeloff.py` header — peel-off PHYSICAL vs algorithmic open question | Repo anchor | CONFIRMED (header lines 1-9) |
| `git show HEAD:.../Horizon.lean` :64-68 corrected RelationalHorizon, :110 no_escape, :120 tombstone | Repo anchor | CONFIRMED; commit 110e4af exists and is an ancestor of HEAD |
| κ=1/(4M) with M=0.25 ⇒ κ=1 | Physicist (arithmetic) | CONFIRMED (`thresholds.py`: M = R_S/2.0 = 0.25; 1/(4·0.25)=1) |

- Notes:
  1. **Miscitation found**: "thresholds.py:57-62 (EXPLORE_POOL)" is wrong — `EXPLORE_POOL` is defined in `dev/explore_seeds.py:23`. Corrected in §2 of this brief.
  2. The EGS "det g = −1" numeric claim cannot be verified from `derived-md` alone (OCR-flagged equations); the surrounding prose is consistent. Treat the numeric form as UNVERIFIED pending a direct PDF-page read.
  3. The working-tree Horizon.lean reversion was independently confirmed (`git show HEAD` vs on-disk) and exactly matches the spec's own `REPO_STATE_FLAG`.
  4. The two Dou–Sorkin arXiv identifiers (0811.4235 in biblioteca derived-md; gr-qc/0302009 in the Horizon.lean header) refer to two different, compatible Dou–Sorkin outputs; no contradiction.

## 8. Synthesis

**Where the committee agrees (no dissent found):**

1. **The order-theoretic core of R-VAR is sound.** Lemma 1 (collapse to anchored down-sets) is
   correct and provable; Lemma 2 is literally the already-proved Lean theorem
   `relationalBlackRegion_no_escape`; Lemma 3 is correct *conditional on Hasse weak connectivity*
   (a real precondition, not decoration); the decoration inventory (VI.2) is valid; equivariance
   VI.5 is provable by construction; realizer-independence is a genuine structural improvement
   over the blocked Q path (mathematician, logician concur).
2. **Thesis V.1 is not adjudicable as posed.** The completion class 𝒦 is nowhere defined in
   writing; Alloy 001/002 are bounded 4-element witnesses under completions comité 010 already
   ruled non-admissible; and the falsifier adds that V.1's quantifier (over `Max(C)`) proves too
   little for its conclusion (over *all* elements). All of mathematician, logician, and falsifier
   converge: V.1 must be re-registered against the **admissible (convex, dim-2 product-order)
   completion class**, in writing, or it inherits `NEEDS_PRECISE_COMPLETION_CLASS`. It may be
   used as *framing*, never cited as established.
3. **The anti-circularity tension (2) is NOT resolved by the spec's own defense.** Four roles
   independently reject "no functional determination" as sufficient: the mathematician confirms
   `E[d⁺]` is a consistent monotone proxy of the banned `O(i)` in the mean (and found a defect —
   dropped ½ null Jacobian — in the spec's own derivation); the physicist elevates it to a
   *physics* overlap (same future-truncation imprint, read locally); the logician identifies the
   missing artefact (the II.1 whole-selector class-by-class compositional check is asserted, not
   exhibited); the falsifier shows the A6.4 Firma-5 admissibility verdict is stale (it predates
   the spec's own ln V+γ derivation) and that the offered `sig_sp` fallback is *worse* (exact
   determination of `O(x)` on minimals — the very class N3 privileges). If sig_lk is ever
   admitted, it must be on the explicit role-separation firewall plus a new written compositional
   check — and the sig_lk/sig_sp fork must be collapsed NOW, on principled grounds, not settled
   later by what "works" on EXPLORE.
4. **The Horizon.lean working-tree reversion is a blocking integrity fact.** It deletes not just
   the corrected definition but the proved guardrails (no_escape, tombstone, VPoset witness) —
   "a deleted falsifier" (logician). It is unexplained (the chair did not make it). Restoration
   *and an origin account* are preconditions to anything else. (Falsifier additionally flags a
   second integrity item: on-disk `results/validation.json` appears to hold the prereg-001-era
   FAIL while `docs/preregistration_002_result.md:12` cites it as the PASS's raw output — refer
   to `/auditor` before any further weight is placed on the PASS transcription.)
5. **Authorization (3) cannot be granted today.** The comité-014 ban is textually unqualified
   and R-VAR's only discriminating statistic is imported from the A6.4 apparatus the ban names;
   a new authorization is procedurally available but must be explicit, scoped, and granted by a
   committee decision *after* the blockers above are cleared — not self-granted by the spec.
   The pre-registration verdict is **BLOCK**, so this brief cannot carry a PROCEED verdict.

**Genuine defects in the spec found by the committee (must be fixed in a revision):**

- `S` undefined when `H[C;D]=∅` (𝒜(C) membership does not require non-empty interface;
  connectivity can fail) → add typed abstentions `DISCONNECTED_HASSE` / `UNDEFINED_SCORE`, make
  the |H| floor (F3) mandatory, not "si se adopta".
- `INCOHERENT_ARGMAX` can structurally never fire on a singleton argmax → the entire abstention
  burden falls on μ; μ must be calibrated on the **distribution of the maximum** (extreme-value
  correct, order-only null MC, τ-table discipline), never on embedding-labelled separation.
- Argmax-of-mean is a small-|H| noise-artifact detector unless F1 freezes an |H|-aware
  normalisation; F1 must also mandate exact integer/rational comparison (floating-point argmax
  sets are platform-dependent, silently voiding determinism/equivariance).
- The consensus-intersection over a possibly exponential argmax set has no specified algorithm;
  the Dinkelbach/parametric DP for the mean objective is unspecified — algorithm spec must
  precede implementation authorization or spec/code divergence is guaranteed (falsifier,
  mathematician).
- Part IV collimation must be demoted from factual register to conjecture with a citation
  obligation; it is unanchored, and the project's own `dev/measure_kbeam_peeloff.py` treats
  peel-off as an open falsification.
- Null patches need a FALSE_POSITIVE reporting channel with the same prominence as detections;
  `U(C)=∅` needs disambiguation from the singleton-noise-argmax signature.
- Miscitation: EXPLORE_POOL lives at `dev/explore_seeds.py:23`, not `thresholds.py:57-62`.

**Ranked alternatives:**

1. **(Recommended) Revise and reconvene.** Fix the working tree (+ origin account), run
   `/auditor` on the `results/validation.json` discrepancy, produce R-VAR spec v2 closing the
   defects above (𝒦 written down; V.1 re-registered; fork collapsed; typed abstentions added;
   F1-F3 given concrete frozen proposals incl. the max-distribution μ procedure and exact
   arithmetic; consensus-intersection algorithm specified; Part IV demoted), then reconvene for
   the scoped authorization decision.
2. Abandon the sig_lk score axis now and redesign the functional (e.g. around longest-chain
   contrast, the *established* tracer per EGS md:226-245) — costlier, and the physicist notes
   any future-truncation statistic will share the physics overlap to some degree; the committee
   does not prefer this without first attempting the firewall + compositional check route.
3. Proceed to implementation now — rejected unanimously (prereg BLOCK; comité-014 ban;
   unfrozen forks; unexplained working-tree state).

**Open disagreements (surfaced, none hidden):** No role recommended proceeding today, so there
is no verdict-level dissent. Two genuine tensions of emphasis remain for the next committee:
(i) the logician holds R-VAR is *formally* non-circular (statistical correlation is a weaker
relation than the II.1 functional-determination ban) while the physicist and falsifier weigh the
*physical* identity of the imprint as near-disqualifying — the next decision must adjudicate
which standard governs; (ii) the falsifier would condition any future authorization on
mechanising Lemmas 1-3 in Lean first, while the logician holds mechanisation is premature until
V.1's completion class is written — sequencing to be decided at reconvening.

## 9. Next-step spec

**Reversible steps (may be run now if the user asks; none touches a seed or a frozen surface):**

1. **Restore the formal layer**: `git checkout -- formal/HorizonFormal/HorizonFormal/Horizon.lean`
   (or `git restore`), verify `git diff` clean on that path, and record in writing where the
   reversion came from. Precondition to everything else.
2. **Run `/auditor`** scoped to the falsifier's finding: does `results/validation.json` /
   `results/validation_run.log` on disk match what `docs/preregistration_002_result.md:12` cites
   as the PASS raw output? Fold `AUDIT_VERDICT` into the next brief.
3. **Write R-VAR spec v2** (`dev/`, write-only, within comité-014's still-standing constraints —
   no code, no simulation, no enumeration): (a) define 𝒦 (the admissible completion class:
   convex, dim-2 product-order per comité 010/012) and re-register V.1 against it as a
   conjecture; (b) collapse the sig_lk/sig_sp fork in writing (committee note: sig_sp is the
   *worse* channel on minimals); (c) exhibit the II.1 whole-selector compositional check for the
   chosen signature; (d) add typed abstentions DISCONNECTED_HASSE / UNDEFINED_SCORE and make the
   |H| floor mandatory; (e) specify the exact-arithmetic argmax rule, the Dinkelbach/parametric
   DP, and the forced-in/forced-out consensus-intersection algorithm; (f) demote Part IV to
   conjecture with citation obligation; (g) write the F2 μ procedure as an order-only
   extreme-value null-MC on max S with α fixed in advance; (h) add the FALSE_POSITIVE reporting
   channel and the U(C)=∅ disambiguation; (i) fix the EXPLORE_POOL citation.
4. **Reconvene `/comite`** on spec v2 for the scoped authorization decision (the analogue of
   comité 014's `Q_A6_AGGREGATION_SPECIFICATION_ONLY` grant, but for: dev implementation +
   deterministic toy-poset tier + EXPLORE-band sprinkling, with the reproducibility engineer's
   mandatory pre-flight guard — env pin, seal check before/after, seed band ⊆ EXPLORE_POOL
   hard-fail, Guard-v on the selector, no sealed-path imports).

**Committing steps (only on explicit user authorisation, and only after the reversible steps
above and a reconvened PASS):**

5. **Freeze F1-F3 + the collapsed fork in a committed written artefact** (prereg-addendum
   pattern: freeze commit precedes any scored run), including the frozen predictions of VI.4
   (null-patch abstention ≈ 0; U-band concentration) so failure cannot be reframed as
   exploration.
6. **Run the falsifier's minimal falsification test FIRST**: the frozen selector on the MINK
   (no-horizon) members of the paired EXPLORE ensembles only (seeds ⊆ EXPLORE_POOL, pre-flight
   guard hard-failing otherwise); report the fraction of null patches emitting a non-⊥
   tri-partition, PASS/FAIL/INCONCLUSIVE alike. Any material non-abstention rate falsifies the
   selector before any horizon-patch claim exists and consumes no virgin seed.
7. Only after 6 reports: horizon-patch EXPLORE runs, under the same guard and reporting rule.

**Binding rules pre-committed for any future authorization:** `NO_RECONSTRUCTION_CLAIM` (the
deliverable is a consensus object + abstention band in a finite 1+1D EF patch, never "el único R"
in a reconstruction register); `NO_POST_HOC_TUNING` / `NO_THRESHOLD_LOOSENING` (F1-F3 frozen
before the first scored run; no re-selection of statistic after seeing separation);
`NO_GROUND_TRUTH_LEAKAGE` (μ never calibrated on embedding-labelled separation; hidden embedding
only scores); `RESPECT_SEAL_FREEZE` (no sealed-path imports; seal verified before/after every
run); PASS/FAIL/INCONCLUSIVE and null-patch false-positive rates reported alike;
`PHYSICAL_IDENTIFIABILITY_STATUS = NOT_ESTABLISHED` repeated in every downstream artefact.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off

_(left blank for the user — decision, date, and any overriding notes)_
