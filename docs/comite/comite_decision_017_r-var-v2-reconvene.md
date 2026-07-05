# Comité Decision 017 — r-var-v2-reconvene

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

PI, 2026-07-04, verbatim: "Convoca al comité para re-evaluar R-VAR v2 con prereg-002 cerrado."
Context supplied: comité 015 issued `RECOMMEND_REVISE_AND_RECONVENE` on R-VAR v1, conditioning
execution of v2 on the closure of the prereg-002 artifact audit (comité 016). That closure has
now occurred: `SUPERVISED_REVERIFICATION_MATCH` on every field, status now
`PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]`. R-VAR v2
(`dev/PR003_R_VAR_SELECTOR_SPEC_V2.md`) remains paused, written but not committed, not executed.

Chair's framing of the actual task: `dev/PR003_R_VAR_SELECTOR_SPEC_V2.md` is a document written by
a **prior session's chair**, responding point-by-point to comité 015's 9 required closures (a)-(i)
and self-reporting all nine as delivered (Part H, `CLOSURES_DELIVERED`). This committee's job is
NOT to re-read v2's self-report and rubber-stamp it, but to **independently verify** whether each
claimed closure is genuine, and to adjudicate the three items v2 itself flags as still requiring a
committee decision: (1) `CIRCULARITY_STANDARD` (`FUNCTIONAL_ONLY` vs
`FUNCTIONAL_PLUS_MEAN_MONOTONE_BAN`); (2) a scoped authorization partially superseding comité 014's
still-standing `NEXT_FORBIDDEN_ACTIONS`; (3) acceptance of V.1a as a candidate scenario for a
future Alloy 003 run (not authorizing Alloy 003 here).

## 2. Verified state

Facts checked **this session** (2026-07-04), each with its command / file:line.

- Seal: `make verify-seal` → `nachocausal/thresholds.py` sha256 =
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, MATCHES
  `docs/preregistration_002.md:8`. Re-confirmed independently by the warden this session.
- git HEAD = `82b4ede` ("prereg-002: SUPERVISED_REVERIFICATION executed — MATCH"), parents
  `f08bc04` (declaration) and `abf90f0`. `git status --short`: only `M INSTRUCCIONES.md`
  (pre-existing, unrelated user edit, untouched) plus pre-existing untracked files, including
  BOTH `dev/PR003_R_VAR_SELECTOR_SPEC.md` (v1) and `dev/PR003_R_VAR_SELECTOR_SPEC_V2.md` — the
  warden independently confirmed both remain uncommitted this session.
- `formal/HorizonFormal/HorizonFormal/Horizon.lean`: `git diff --stat HEAD -- ...` is EMPTY —
  working tree matches HEAD exactly, both `relationalBlackRegion_no_escape` (:110) and the
  tombstone `relationalHorizonOld_eq_empty` (:120) present. The repo-state hazard comité 015
  flagged (an uncommitted revert to the provably-empty orientation) is NOT present this session.
- **prereg-002 is CLOSED via `SUPERVISED_REVERIFICATION_MATCH`**
  (`docs/prereg002_reverification_result.md`, committed at `82b4ede`; declaration at
  `docs/prereg002_reverification_declaration.md`, committed at `f08bc04`; authorised by comité 016,
  `COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`). Every one of ~60 fields
  (verdict token, six boolean checks, full per-level table at all 4 intensities) matched the
  `fee12d5` transcription exactly, no drift anywhere. Status everywhere cited:
  `PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]`. This MATCH
  verifies transcription fidelity (M); it does **not** establish that the original 2026-06-22 run
  was not off-git seed-shopped (H) — documentary support only. `VALIDATION_SEEDS` is declared
  **permanently burned** for any future protocol comparison or selector design/calibration — this
  binds R-VAR v2 directly, re-derived independently by the warden this session from
  `nachocausal/thresholds.py:44-75` and `dev/explore_seeds.py:23-42` (both bands disjoint by
  machine-checked assertion at import time, not merely documented in prose).
- **`dev/PR003_R_VAR_SELECTOR_SPEC_V2.md` carries a stale citation**: its preamble (:17-22) and
  normative block (:400-401, `PASS_DEPENDENCY_LABEL = [UNVERIFIED-raw-artifact]`) still cite
  auditor 005's `AUDIT_FAIL` as current. This predates and is superseded by the MATCH above. All
  four wave-1 experts and the warden independently flagged this; it is a correction, not a
  forbidden move, but must be fixed before v2 is treated as current or committed.
- Standing comité 014 blockade, re-confirmed verbatim
  (`docs/comite/comite_decision_014_q-reference-rule-disposition.md:917-929,1063-1076`):
  `OVERALL_VERDICT = Q_REFERENCE_PATH_REMAINS_BLOCKED`. Bars (non-exhaustive): "cualquier
  simulación, sprinkling, enumeración o búsqueda de contraejemplos"; "cualquier análisis
  estadístico"; "implementar código para Q, la tripartición, A6.4, o cualquier pullback lateral";
  Alloy 003 en cualquier modalidad; Lean como sustituto de definición física ausente; "commit o
  push sin autorización explícita del PI". **Still in force.**
- comité 015 verdict `RECOMMEND_REVISE_AND_RECONVENE` required 9 written closures (a)-(i) before
  reconvening. v2's Part H self-reports all nine closed. Independent verification this session
  (§4-§5 below) finds **six genuinely closed** (a-partially, b, d-partially, f, h, i) and **three
  closed in letter but not in substance** (a's V.1a quantifier, c's compositional witness, d's
  F3-as-no-op) — see falsifier attack, §5, for the concrete gaps. No validation results were
  produced this session; no seeds touched; only read-only commands and `make verify-seal` executed
  by the chair.

## 3. Dossier

- `dev/PR003_R_VAR_SELECTOR_SPEC_V2.md` (the artefact under adjudication, read in full by all
  roles) and `dev/PR003_R_VAR_SELECTOR_SPEC.md` (v1, superseded, historical)
- `docs/comite/comite_decision_015_r-var-selector-adjudication.md` (the mandate v2 responds to)
- `docs/comite/comite_decision_016_prereg002-supervised-reverification.md`,
  `docs/prereg002_reverification_result.md`, `docs/prereg002_reverification_declaration.md`
- `docs/comite/comite_decision_014_q-reference-rule-disposition.md` (:900-930, :1060-1080)
- `docs/comite/comite_decision_012_c1-admissible-completion-class.md` (:325-362)
- `docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md`
- `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md`
- `dev/PR003_Q_A6_4_ROBUST_ABSTENTION_SPEC.md` (§II.1 :175-320)
- `dev/explore_seeds.py:23`; `nachocausal/thresholds.py` (`VALIDATION_SEEDS` :66-75, `THETA_FP`)
- `docs/preregistration.md`, `docs/preregistration_002.md` + result
- `formal/HorizonFormal/HorizonFormal/Horizon.lean`
- `biblioteca/derived-md/`: Eichhorn–Gamito–Stokes arXiv:2605.06813; Dou–Sorkin arXiv:0811.4235;
  Surya LRR 2019 §4; Benincasa–Dowker arXiv:1001.2725; Bombelli 1987

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

- **Proposed artefact(s):** dev-only, no-commit, pre-flight-guarded pipeline: `dev/measure_pr003_rvar.py` (toy tier, deterministic enumeration verifying D.2.1/D.2.2 + witness C.1); run-log artefacts only under `dev/*.log`; a μ-table freeze addendum committed BEFORE any BH-patch scoring — that commit is itself a committing step needing the standing "commit/push sin autorización del PI" bar lifted. All BLOCKED absent scoped authorization.
- **Environment & seal:** sealed CPU env, numpy HARD-PINNED 1.26.4; re-verify via `make verify-seal`; `assert_environment()` must pass at run start; NOT the minz clone.
- **Provenance capture:** git HEAD, status cleanliness, pip freeze, uname, exact seed band (EXPLORE_POOL only), M (null-patch count, M≥200, exact value frozen in addendum), UTC timestamps, seal SHA before/after.
- **Run mechanics:** single foreground invocation, mandatory reversible pre-flight guard, hard-abort on: assert_environment fail, seal mismatch, seeds outside EXPLORE_POOL or intersecting VALIDATION_SEEDS, or selection_guard failure. Toy tier deterministic/reversible. The μ-table freeze commit IS the committing boundary.
- **Reproducibility risks / ambiguities:**
  - RNG spawn spec under-specified (M and exact `Generator.spawn()` form not fixed) — bit-exactness not guaranteed across idioms.
  - Stale AUDIT_FAIL citation in v2 (`:17-22,:400-401`) — superseded by the reverification MATCH; must be updated in any revision.
  - Authorization gap is the binding blocker, not seed-discipline: the entire toy+null run is a standing comité 014 `NEXT_FORBIDDEN_ACTION`; v2 correctly concedes it needs a scoped supersession, not a self-grant.
  - μ α-basis reuse (=`THETA_FP`) is defensible, not a new number.
  - Virgin-band burn is now permanent and binds every tier — the pre-flight disjointness guard must be a hard fail, not advisory.

### Mathematician brief

- **Computability:** every R-VAR primitive is decidable on the order alone, poly-time. Two gates must not be conflated: sealed estimator-v2 τ(n) gate belongs to the validator; R-VAR's own typed `⊥(τ)` ladder is fully order-decidable.
- **Order observable:** `d⁺(z):=#{w:z⋖w}` aggregated into `S(D)=A(D)/B(D)` — a radius-1 proxy for future-volume `|↑x|`, the only order-visible imprint of a 1+1D horizon.
- **Relevant invariants:** cover-degree/links, future-volume (Bombelli 1987; Surya LRR 2019 §4), longest-chain/height, interval abundances C_k (Benincasa–Dowker, not used by R-VAR).
- **Analytic / continuum target:** corrected mean law `E[d⁺] ∼ ln(ρ·future-Area) + const`. Null-calibration target `FP_RATE_NULL ≤ α=0.05 ≡ θ_fp`.
- **Caveats:** Dinkelbach/staircase DP rests on an unproven edge-locality lemma (`PLAUSIBLE, no probado`); `INCOHERENT_ARGMAX` cannot fire under singleton argmax, whole abstention burden on μ (v2 admits this); `sig_sp` rejection is order-theoretically forced (on minimals it reconstructs banned O(i) exactly).

**Verification of the specific closures**

- **Closure (a) GENUINE.** 𝒦_comb/𝒦_adm/𝒦_Schw inherit clauses verbatim from comité 012 D1/D2, each order-decidable — a genuinely closed, well-typed quantifier domain. V.1a/V.1b split fixes both comité-015 findings; selector degraded off V.1 as premise, severing the laundering hazard. [**See falsifier attack §5 below — this verdict is challenged on the V.1a quantifier specifically.**]
- **Closure (e) SPECIFICATION-CLOSED, PROOF-OPEN.** D.2.2's forced-in/forced-out logic is correct as a reduction (checked mathematically: `S(D)≤λ* ⟺ G(D)≤0`), but inherits the same unproven edge-locality DP lemma as D.2.1. Literal comité-015 gap ("not specified") closed; correctness still open — honest, do not upgrade to "proven."
- **F3 := H_MIN = 1 principled? YES.** Adds zero free parameters — coincides exactly with "S is well-defined" (H≠∅). Any H_MIN≥2 would be a genuine statistical choice needing calibration.
- **CIRCULARITY_STANDARD — my own verdict: recommend `FUNCTIONAL_ONLY`.** Corrected `E[d⁺]∼ln(ρ·future-Area)+const` sign is robust regardless of Jacobian/constant corrections, so `FUNCTIONAL_PLUS_MEAN_MONOTONE_BAN` WOULD kill d⁺ — mathematically correct. But the strong standard is mathematically incoherent as a circularity criterion: mean-monotonicity is not functional determination, and applied uniformly it would retroactively condemn the project's own already-sealed `O_min` future-volume observable. Consistency forces `FUNCTIONAL_ONLY`; the real firewall is role-separation + null-only μ calibration, not a mean-monotonicity ban. [**See falsifier attack §5 — flags this specific argument as circular reasoning.**]

Flag: v2's `PASS_DEPENDENCY_LABEL=[UNVERIFIED-raw-artifact]` is STALE, superseded by the reverification MATCH; must be updated in any revision.

### Mathematical logic brief

- **Formal status:** only `relationalBlackRegion_no_escape` (Horizon.lean:110) and tombstone `relationalHorizonOld_eq_empty` (:120) are proved Lean theorems; v2 is write-only. Definitions correctly typed: 𝒦_comb/𝒦_adm/𝒦_Schw, 𝒜(C), S=A/B, F1/F3, the abstention ladder, the μ *procedure* (numeric table deferred). Conjectures honestly labelled and — load-bearing — NOT in the selector's dependency chain: V.1a/V.1b, C-COL, D.2.1/D.2.2. v2 explicitly severs V.1 from the selector — the structural fix comité 015 demanded.
- **Quantifier/dependency order:** binding freeze order explicit and correct: scoped authorization → toy tier → μ-table over EXPLORE nulls → freeze commit → falsification test on nulls → only then BH patches. Both comité-015-named post-hoc DOFs (F1 mean-vs-median, sig_lk/sig_sp fork) collapsed BEFORE any data, on pre-data structural grounds.
- **Equivalence claims:** only genuine proved iff is Lemma 1's `↓↓R=↓R` collapse + 𝒜₀↔M bijection. F1's ratio-comparison equivalence is a correct integer identity. Forced-in/out characterisations are correct definitions, contingent on the unproven optimizer.
- **Type/object discipline:** clean at load-bearing joints. 𝒦_adm is a genuinely closed, well-typed set of finite posets. Part C rigorously separates functional determination (C.1) from mean-monotone correlation (C.2).
- **Caveats:** C.1's separation witness exhibits agreement only on P1/P2, asserts invariance under P3-P6 — full compositional check registered as toy-tier obligation, not yet exhibited [**falsifier finds this gap larger than stated, §5**]. F3:=1 logically redundant with the H≠∅ membership predicate — a null threshold, not a working guardrail (honest, not a defect). Stale `PASS_DEPENDENCY_LABEL` flagged again.

**Verification of the two comité-015 closures and the Part C fork:**

- **Closure (a) — genuinely fixed, not relabelled.** 𝒦_adm(O) is a decidable order-theoretic predicate on finite posets. V.1a's conclusion is correctly SCOPED to the last band; V.1b quarantines the over-reaching all-element no-go as OPEN + forbidden-to-cite. **Verdict: real fix.** [**Falsifier disagrees on the quantifier inside V.1a specifically — see §5.**]
- **Closure (d) — hazard closed; singleton-argmax gap honestly relocated, not eliminated.** H[C;D]≠∅ as membership condition makes S total on 𝒜(C) by construction. With H_MIN:=1 frozen, INCOHERENT_ARGMAX **cannot** fire on a singleton argmax — v2 admits this verbatim, an honest admission reproducing the falsifier's exact point without disguising it. Not a well-posedness defect; the statistical abstention burden is UNVERIFIED until the frozen null falsification test actually runs.
- **Overall logical verdict — v2's selector is WELL-POSED as a mathematical object.** Every quantifier bound, every abstention case typed, score total on stated domain. Unproven apparatus (V.1a/V.1b, C-COL, D.2.1/D.2.2) is honestly labelled and — decisively — the selector's definition depends on none of it, so openness does not render the object ill-posed. Well-posed as a *parametric* object; not fully-instantiated until F2's μ-procedure executes on authorised EXPLORE nulls. This holds independently of the two open committee forks.

### Physicist brief

- **Coordinates & patch:** ingoing Eddington–Finkelstein coordinates, finite box. Finiteness forfeits any asymptotic/event-horizon claim — order-only localisation of r=2M in a finite patch, not a horizon in the asymptotic sense.
- **Physical meaning of the signal:** interior future light-cones tilt so no future-directed causal curve keeps non-decreasing r inside the horizon (Dou–Sorkin md:498, confirmed verbatim by literature verifier) — interior futures truncated, exterior futures bounded only by the box, yielding the bimodal longest-chain/future-volume split (EGS md:226,239,245,247, confirmed). d⁺ is a coverage-degree proxy for this same imprint.
- **Sprinkling domain:** Poisson in EF box; future-cardinality is boundary/box-shape sensitive (EGS md:247) — nulls must absorb this. Domain draws exclusively from EXPLORE_POOL, hard pre-flight guard against VALIDATION_SEEDS.
- **Claim boundary:** order-only localisation of r=2M in a finite 1+1D Schwarzschild-EF patch, nothing more. Intrinsically Schwarzschild-specific — mechanism relies on singularity-truncated interior futures, which fail for regular (Hayward-type) BHs (EGS md:249,253 — "likely to fail", confirmed).
- **Caveats:** boundary-sensitivity of future-cardinality (anchored); apparent-horizon (Θ_out sign change) NOT directly computable in 1+1D (EGS md:290, confirmed: "we do not have spatial two-surfaces available"); EGS's own ladder/apparent-horizon construction is in practice seeded from the longest-chain partition (md:600, confirmed); backward-collimation rate κ has no primary-source anchor in biblioteca/ — `[UNVERIFIED]` as a rate claim; EGS md:288 anchors ONLY the Θ_out sign change (confirmed), no Lyapunov rate.

**Session-specific questions:**

- **Does prereg-002's MATCH change the physical dependency chain? No.** The future-truncation imprint is a property of Schwarzschild causal structure, independent of any one run's provenance. The MATCH concerns transcription integrity, not physics; d⁺'s soundness as a signal is unchanged. Only action item: correct v2's stale citations in any revision.
- **CIRCULARITY_STANDARD physical judgment:** v2's claim that the strong ban kills *all* functional selectors is physically correct for the future-volume family (d⁺, longest-chain, future cardinality), but **overstated as a universal over all order-only statistics** — there IS a physically distinct candidate, the apparent-horizon/Θ_out-sign-change channel, realised via null-ladder collimation, not a priori a mean-monotone function of future volume. BUT: (i) not directly computable in 1+1D; (ii) in EGS's actual pipeline the ladders are in practice seeded from/bootstrapped off the longest-chain partition, so the "independent" channel is not genuinely independent in practice. **Adjudication input: the committee may adopt the strong standard, but its "kills all functional selectors" consequence is proven only for the future-volume family and is `[UNVERIFIED]` as a universal.**
- **C-COL and V.1a:** degradation of C-COL to conjecture status with citation obligation + hard prohibition on using κ/1/κ to set thresholds is honest and physically sufficient containment, PROVIDED the prohibition is a hard guard, not advisory. V.1a as Alloy-003 candidate scenario is physically acceptable.
- **Regular-BH portability:** v2 does not over-reach, but this silence should be made an explicit standing claim-boundary requirement rather than left implied.

## 5. Falsifier attack

*[The falsifier's copy of the dossier initially omitted the wave-1 briefs due to a chair transmission error, caught and corrected mid-session by sending the full brief content. The falsifier produced two passes: an incomplete-context pass (which still surfaced most of the load-bearing findings below) and, after correction, a second pass with full context that sharpened several points and added items 7-10 below plus the composite-ladder and M-value findings. Both are merged here; nothing from either pass is dropped.]*

- **Concrete failure modes:**
  1. **Closure (a) is letter-compliant but V.1a as written is trivially true or ill-posed — unfit as an Alloy 003 candidate.** V.1a says `∃ C₁, C₂ ∈ 𝒦_adm(O): m ∈ down(escape(C₁)) ∧ m ∉ down(escape(C₂))` "donde escape(Cᵢ) es **cualquier** referencia anclada propia de Cᵢ" (`v2:67-71`). On the existential reading, the completions do no work: take C₁=C₂=O, M₁={m}, M₂=Max(O)∖{m} — the statement holds with zero completion content whenever |Max(O)|≥2 and m∉↓M₂. On the universal reading it is a different, much stronger claim. This is the same "quantifier body under-specified" defect that killed v1's V.1 (comité 015 logician), reintroduced one level down (the reference quantifier instead of the completion class). Fix in writing before any Alloy-003 candidacy acceptance: bind `escape(Cᵢ)` to a fixed rule (e.g. R-VAR's own `E(Cᵢ)` when non-⊥).
  2. **Closure (c)'s separation witness proves less than II.1 demands, twice.** (i) II.1 requires non-determination by the whole primitive set, but the witness pair P₁/P₂ (`v2:133-138`) only shows radius-1-at-x insufficiency — globally the two posets have different full primitive profiles, so the "P3/P4 no restauran la determinación" dismissal is one unproven sentence. (ii) P₂'s Hasse diagram is disconnected — the sole witness sits outside R-VAR's own effective domain (`DISCONNECTED_HASSE`). C.1 never fixes what the functional-determination test *object* is (available primitives vs. exposed outputs S/T/E/U/τ) — on the primitives reading the claim is trivially false; on the outputs reading the witness doesn't address it. Closure (c) is marked `[ENTREGADO]` at a confidence the evidence does not support.
  3. **Closure (d)'s F3:=1 is the vacuous value.** `H≠∅` is already a membership condition of 𝒜; `H_MIN:=1` adds nothing. v2's substitute (extreme-value μ over max S) is statistically legitimate, but labelling F3 "CERRADO...con base principiada" when it was closed by setting it to no-op overstates.
  4. **Closure (g)'s "α=0.05 ≡ θ_fp, no un número nuevo" is convention-borrowing dressed as inheritance.** `THETA_FP` governs a different statistic in a different role; reusing the numeral is fine as a pre-data freeze, but the "base principiada" framing overstates and must not be cited later as if the value were derived.
  5. **The Part F binding order bundles the BH-patch step (6) into the same authorization.** A scoped grant covering v2's full order authorizes horizon-patch EXPLORE scoring in the same breath as the toy tier. A report-back gate after step 5 (nulls-only falsification) is required before any BH patch is scored.
  6. **Stale authority citation** (`v2:17-22,400-401`) must be corrected — and the document committed — before any authorization is pinned to it, so the spec is not a moving target.
  7. **F3's "principled? YES" (mathematician) and "logically redundant, a null threshold" (logician) are not reconciled by either brief, and the unreconciled version is more comfortable than the truth.** F3=1 changes nothing structurally — it excludes nothing that `H≠∅` didn't already exclude — so the small-`|H|`-noise risk comité 015 named (failure modes 3-4, comité 015 §5) is **never excluded by construction**, only diluted after the fact by μ's extreme-value calibration. Calling this "principled? YES" without stating plainly that it defers the entire small-interface risk to μ is the self-congratulatory-closure pattern the chair asked about.
  8. **v2 Part H labels closure (e) `[CERRADO]` while D.2.1's edge-locality lemma remains unproven and, if false, would produce a *silently wrong* algorithm, not merely a slow one.** The word "CERRADO" in the normative block overstates what "SPECIFICATION-CLOSED, PROOF-OPEN" (mathematician) actually means. No wave-1 brief recommends withholding the `CLOSURES_DELIVERED` verdict on (e) pending the lemma check — all four accept v2's own framing.
  9. **The typed abstention ladder's four τ-types collapse to one operative gate in the single most common real case.** F3 excludes nothing (item 7) and `INCOHERENT_ARGMAX` cannot fire on a singleton argmax (all four wave-1 briefs note this fact individually, none states the conjunction): for a unique optimum, the *entire* four-type ladder reduces to a single live check, `LOW_CONTRAST` vs. μ. A ladder with four named types that in practice is one gate with three decorative labels is not the "typed abstention ladder" comité 015 asked for in the load-bearing sense.
  10. **The physicist's Θ_out/apparent-horizon rescue of "not a universal ban" is conceded, in the same brief, to be practically non-independent** (EGS's own ladders bootstrap off the longest-chain partition). A channel that saves a claim only "in principle, for a channel nobody has implemented and that this project cannot implement in 1+1D" is a rescue in name only; no wave-1 brief flags that this caveat neutralises its own rescue. Separately: computing Θ_out in a finite EF patch would very likely require direct access to `r` / the trapping condition — i.e. exactly the hidden-geometry access the order-only mandate forbids feeding into an observable definition. The channel is thus **doubly disqualified**: not independently seeded in practice, and its own computation would likely itself constitute `NO_GROUND_TRUTH_LEAKAGE` unless a purely order-only reformulation is found and independently verified (none attempted).

- **Ground-truth leakage:**
  - **The sharpest remaining leak is meta-level: choosing CIRCULARITY_STANDARD by outcome.** "FUNCTIONAL_ONLY because the strong ban would also condemn the already-sealed O_min" is circular — it takes O_min's admissibility as a fixed point and rejects any standard that threatens it. If the strong standard were correct, the honest output would be program-level `OUT_OF_DOMAIN` ("no admissible order-only reference selector exists in this patch") — a guardrail must be able to fail the *program*. Uncritically adopting FUNCTIONAL_ONLY is the bigger risk here: "functional determination" is ill-posed as stated (trivially violated on the primitives reading, near-unfailable on the outputs reading) — bare FUNCTIONAL_ONLY is a guardrail that cannot fail. The fork as posed is also a **false dilemma** (two options, one pre-labelled fatal). If FUNCTIONAL_ONLY is adopted, it must be adopted on independent grounds and with teeth: (i) the test object defined as the *exposed outputs* (S, T/E/U, τ), in writing; (ii) a binding `NON_CORROBORATION` clause — since d⁺ and O_min read the same future-truncation imprint, any future BH-patch agreement between R-VAR and the sealed estimator is partially guaranteed by construction and may never be cited as independent corroboration of the prereg-002 PASS; (iii) a permanent limitation label on every R-VAR artefact.
  - μ's null-only calibration is genuinely leak-resistant as specified. Residual hole: `numpy default_rng(seed).spawn` sub-seed derivation produces streams the pre-flight guard cannot verify from seed integers alone — spawn keys must be logged and the guard must check the spawn derivation. **A second, subtler residual hole: `M` itself ("≥200, exact value fijado en el addendum") is a floor, not a frozen value** — if `M` is chosen after a preliminary look at how stable μ looks with a candidate `M`, that is post-hoc tuning of the calibration's statistical power even though no embedding or ground truth touches it directly. The exact rule for choosing `M` (not just a floor) must be frozen before any null is scored.
  - The apparent-horizon/Θ_out channel (physicist's brief) is doubly disqualified as a leakage-safe alternative, per item 10 above — flag this sharply, not just as "impractical."
  - P-BH uses the hidden embedding to *score* a frozen prediction — compliant, provided failure is recorded as falsifying R-VAR (v2 says so) and never triggers silent redesign.
  - v2's C-COL prohibition ("PROHIBIDO: usar κ, 1/κ o cualquier cantidad de la geometría oculta para fijar F1-F3, μ, o ventanas de reporte," `:353-354`) is correctly hard-worded but is currently a **document-local** rule — it needs elevation to a standing, cross-document binding rule (comité-015-pattern) before any freeze, or a future revision could silently drop it without violating any *committed* prohibition.

- **Freeze violations:**
  - None committed yet (v2 is write-only). Prospective: μ_n table intensity levels are unenumerated in v2 — must be enumerated and interpolation forbidden. `M` must be fixed by an explicit rule (not a floor) *before* any null is scored, not after inspecting the first table's stability. The 015 falsification test has no frozen numeric decision rule ("FP_RATE_NULL ≤ α por construcción" is not itself a test with a tolerance) — freeze the rule and require test nulls spawn-disjoint from calibration nulls. `VALIDATION_SEEDS` burn binds v2's F2 directly, guard-enforced.
  - **Validation circularity in the binding order itself:** Part F's step 4 ("commit de freeze de la tabla μ") precedes step 5 ("test de falsación mínima... solo nulos") — but if both draw from the same EXPLORE null pool without an explicit disjointness rule, the falsification test's "null patches should abstain ≈ always" prediction is partly checked against the very data that defined the abstention threshold. Not leakage in the strict ground-truth sense (no BH label, no embedding), but a real freeze-hygiene gap: **freeze μ on one null sub-pool, test `FP_RATE_NULL` on a spawn-disjoint sub-pool**, both from `EXPLORE_POOL`.
  - Granting the full S1-S5 order as a single blanket authorization risks collapsing two separable committing events — "run the toy tier + nulls" vs. "commit a frozen threshold (the μ table)" — that comité 014's own precedent (`Q_A6_AGGREGATION_SPECIFICATION_ONLY`, write-only) treats as distinct. S4 (the freeze-commit) should be flagged as its own checkpoint requiring the addendum (exact `M`, spawn scheme, enumerated levels) to already be committed, not merely "part of" the same grant.

- **Verdict coercion:**
  - `INCOHERENT_ARGMAX` still cannot fire on a singleton argmax — combined with F3's redundancy (item 7), this is the composite finding of item 9 above: the ladder collapses to one operative gate in the common case.
  - "Guaranteed-by-construction" P-null is a cannot-fail check as framed — reframe as a genuine test or it is decoration.
  - Label direction after the MATCH: neither silently keeping the AUDIT_FAIL framing nor silently upgrading to bare "PASS" is acceptable — the revision must do neither.
  - **The worst hole in the proposal: a silent-corruption failure mode the typed abstention ladder cannot see.** If the D.2.1 edge-locality lemma is false in the sprinkled regime, the DP silently optimizes over a *subfamily* of 𝒜 — Dinkelbach still terminates, T/E/U still emit, no ladder type fires. Worse, the corruption is self-consistent: the same buggy code computes both the μ_n null table (step 3) and the falsification test (step 5), so `FP_RATE ≈ α` by construction and the test *passes* while the frozen μ table and every downstream T/E/U belong to an undocumented different selector than the pinned spec. v2's proposed toy verification "en posets escritos a mano" is insufficient — author-chosen small posets can miss exactly the long-link geometry that breaks locality.

- **Premature / over-broad claims:** clean where checked (`PHYSICAL_IDENTIFIABILITY_STATUS=NOT_ESTABLISHED` preserved; C-COL demoted with citation obligation and barred from thresholds; EGS anchors only the Θ_out sign change). Residual over-reach candidates: V.1a's ambiguous quantifier branded "conjetura formalizable"; any future wording letting T/E/U be read as "interior/exterior" rather than a wall-anchored escape partition; **the foreseeable over-claim is not metric reconstruction but "R-VAR independently confirms the PASS"** (the `NON_CORROBORATION` clause above exists precisely to forbid this). The MATCH itself establishes M, explicitly not H — any R-VAR motivation leaning on the PASS inherits `BLINDNESS_DOCUMENTARY_ONLY`. **One further, previously unflagged over-claim: v2 Part C.2 states "es el único imprint order-visible" (`:159-160`) as established fact, not conjecture — but the physicist's own Θ_out/apparent-horizon discussion names a second, physically distinct (if impractical) channel, directly contradicting "único." Must be softened to "the only imprint currently identified/practical in this pipeline."**

- **Independent-falsification gate: NOT satisfied,** and materially unchanged from comité 015's own finding ("the proposed implementer would also be the author of the predictions being tested," comité 015:208). v2 was authored by a prior session's chair to 015's own checklist; the C.1 separation witness is a single-author, unmechanized derivation; the proposed toy-tier implementer would again be the author lineage verifying its own PLAUSIBLE lemmas. This session's four wave-1 briefs are themselves not independent verification either — they are analytic review of the same document, converging without an independent reconstruction: **no brief hand-built the C.1 separation witness to check it, and no brief re-tested V.1a's re-scoping against an explicit adversarial poset** (it was accepted because it correctly answers comité 015's objection *as stated*, which is exactly the "pattern-matching to what comité 015 wanted to hear" risk the chair asked about). Three closures ((a) V.1a's quantifier, (c) witness scope, (d) vacuous F3) are closed in letter, not substance. Minimum remedy: the toy tier's acceptance gate must be machine-checkable, not author-judged; V.1a and the C.1 test-object definition fixed in writing before any authorization pins v2.

- **Minimal falsification test (two-tier, cheapest-first):**
  - **Tier 0 (committee-executable by hand, before authorizing even the toy tier):** a committee member — not v2's author — hand-constructs two small posets in `𝒦_adm` (convex, product-order, dim≤2) with isomorphic radius-1 Hasse neighbourhoods at a distinguished minimal `x` but different `|↑x|` (v2's own C.1 witness shape, `:132-138`), verifies by hand that `d⁺(x)` is indeed equal in both, then hand-builds one larger (~15-20 element) poset and checks that the D.2.1 Dinkelbach/staircase DP's crossing-set computation produces the same T/E/U partition that direct brute-force enumeration of `𝒜(C)` produces. Cheaper than the μ-table computation itself; should be the FIRST toy-tier deliverable, not optional.
  - **Tier 1 (automated, inside the toy tier, before any μ-table computation):** on ≥100 sprinkled posets at N small enough for exhaustive enumeration of 𝒜(C) (N ≲ 14, sub-seeded from EXPLORE_POOL with logged spawn keys, both MINK and BH boxes), compare the Dinkelbach-DP pipeline's exact (λ*, T, E, U, τ) against brute-force enumeration with exact rational arithmetic. **Frozen acceptance rule: zero disagreements; any single mismatch falsifies the D.2.1/D.2.2 machinery and BLOCKS the μ freeze unconditionally.**
  - Both tiers target the one failure mode the typed abstention ladder structurally cannot see; Tier 0 is cheap enough that there is no excuse to skip straight to Tier 1.

- **On the narrowest scoped-supersession wording (chair's question 4):** authorize, by pinned commit hash of the *revised* v2 only: (S1) dev-only implementation of the R-VAR v2 selector exactly as pinned, no imports from the sealed path, no implementation of any A6.4 marker/gate/Q/tripartición/lateral pullback; (S2) the deterministic toy tier including the brute-force cross-check above; (S3) null-only Minkowski EXPLORE sprinkling for the μ_n table (levels and M enumerated and frozen first); (S4) commit of the μ table + frozen numeric decision rule; (S5) the 015 falsification test on calibration-disjoint null spawns. **Explicitly NOT authorized:** BH-patch scoring (requires report-back), Alloy 003, Lean, any citation of R-VAR output as evidence about Q or as corroboration of the prereg-002 PASS, any seed outside logged EXPLORE_POOL spawn provenance. Admitting d⁺ within R-VAR changes nothing about `Q_DISPOSITION=Q_DIAGNOSTIC_CANDIDATE_ONLY` or `OVERALL_VERDICT(014)=Q_REFERENCE_PATH_REMAINS_BLOCKED`.

- **On momentum/halo risk (chair's question 5):** the risk is real and structurally present. Even the chair's own dossier paragraph opens by stating prereg-002's closure and only then notes "R-VAR v2 sigue pausado" — structurally pairing a hard-won MATCH with an invitation to also move R-VAR forward now. v2's own `NEXT_RECOMMENDED_ACTION` primed "reconvene once the artifact question resolves," and the reverification result had to state explicitly that it "does not itself authorise resuming R-VAR." The reproducibility engineer's and physicist's own briefs both correctly note the MATCH is physically and procedurally irrelevant to R-VAR's merits — the right instinct, but the framing juxtaposition itself should be named, not just individually deflected. **Binding statement for the record: the closure of prereg-002 is not evidence for or against any of R-VAR v2's three open items; CIRCULARITY_STANDARD, the scoped comité-014 supersession, and V.1a's Alloy-003 candidacy are adjudicated as if prereg-002 had not just closed — this verdict would read identically either way.**

## 6. Pre-registration verdict

- **Verdict: PASS — CONDITIONAL** (process-compliant subject to five binding conditions; this is a
  scoping/authorization decision, not a validation run).

- **Freeze status:** the sealed prereg surface is untouched. At the dev level, v2 Part F freezes
  F1 (exact-rational comparison), F3 (`H_MIN:=1`), the sig fork (`SIG_LK_ONLY_SIG_SP_REJECTED`),
  and F2's *procedure* + α=0.05 (reused `THETA_FP`) in writing before any EXPLORE code runs —
  satisfying comité 015's own remedy. **Gap:** F2's numeric table `M` and RNG spawn scheme are
  deferred to "el addendum de freeze" without pinning *when* relative to step (3) (table
  computation) in the binding order. Must be committed **before step (3) begins**, not merely
  before step (4)'s freeze-commit — mirroring `VALIDATION_DRAW_SEED` being fixed before the
  prereg-002 draw.
- **Seal integrity:** re-confirmed this session, `6e2c3888…` matches. Nothing in v2 or the
  proposed authorization touches `nachocausal/` or the sealed entrypoint.
- **Seed discipline:** re-derived independently from source (not trusting citations):
  `DEV_SEEDS`/`VALIDATION_SEEDS`/`EXPLORE_POOL` are disjoint by machine-checked assertion at
  import time (`thresholds.py:71-75`, `explore_seeds.py:36-42`). No leak path found.
- **Reporting rule:** v2 D.4 binds symmetric FP-channel reporting and frozen predictions before
  running, mirroring the prereg-002 publish-either-way rule. Compliant, contingent on this
  actually binding the eventual falsification-test run.
- **Forbidden moves present?** None found in v2 itself; it correctly declines to self-grant its
  own authorization. One stale artefact (auditor-005 `AUDIT_FAIL` citation) — a correction, not a
  forbidden move, but must be fixed before v2 is committed.
- **Binding conditions for a clean PASS (not yet satisfied):**
  1. Commit `dev/PR003_R_VAR_SELECTOR_SPEC_V2.md` with the stale `AUDIT_FAIL` citation corrected
     to the reverification status, and mark v1 superseded in the same commit.
  2. Pin `M` and the exact RNG spawn scheme in a written addendum, committed *before* Part F
     step (3) begins.
  3. Scope the comité-014 supersession narrowly and explicitly: toy-tier implementation +
     EXPLORE-null calibration + the minimal falsification test on nulls only. All other comité 014
     bars (Alloy 003, Lean-as-physical-substitute, BH-patch scoring, any other statistical
     analysis) remain standing.
  4. Resolve `CIRCULARITY_STANDARD` as part of *this* authorization, before any toy-tier code
     exists — it is a definitional gate on whether d⁺/S is an admissible object at all.
  5. V.1a acceptance is a labelled conjecture registration for a *possible future* committee only —
     never pre-authorizing Alloy 003; `ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED` stands.
  - On the scoped-supersession legitimacy question: **not itself a freeze violation.** Comité 014
    used the identical mechanism on itself (`Q_A6_AGGREGATION_SPECIFICATION_ONLY`, an explicit,
    narrow, written exception inside a blanket blockade), and comité 015's own warden already
    endorsed this exact mechanism as the correct path for R-VAR (`comite_decision_015:222,235-iv`).
    One asymmetry: comité 014's carve-out was specification-only; v2's is broader (actual code +
    statistical calibration) — a legitimate escalation of the same mechanism, but the committee
    must make the scope explicit and narrow, not wave through Part F's entire pipeline as one grant.
  - On v2 being untracked: **matters, and is remedied as precondition 1 above.** The project's own
    practice commits frozen/authorized dev specs (e.g. `d0230b5` after comité 014's
    `Q_A6_AGGREGATION_SPECIFICATION_ONLY`). An uncommitted "closure" document carries no diff
    trail and could be silently edited after this committee's review without detection.

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| Dou–Sorkin arXiv:0811.4235, derived-md:498 — "as we cross the horizon at r=2 the links only extend to the left, since there are no future-directed causal curves which have non-decreasing r in the interior" | Physicist | CONFIRMED (verbatim; source has minor OCR typos, paraphrase faithful) |
| Same doc, :166, :176, :205 (light-cone tilt / no outgoing solution inside r<2M) | Physicist | CONFIRMED |
| EGS arXiv:2605.06813, derived-md:226,239,245,247 (bimodal longest-chain/future-volume split) | Physicist | CONFIRMED |
| Same doc, :249,253 (regular/Hayward-type BH partition "likely to fail") | Physicist | CONFIRMED |
| Same doc, :600 (ladder/apparent-horizon construction seeded from longest-chain partition) | Physicist | CONFIRMED |
| Same doc, :288 (Θ_out sign change at r=2M ONLY, no Lyapunov rate) | Physicist / Mathematician | CONFIRMED — no κ-rate language anywhere near this passage |
| Same doc, :290 ("we do not have spatial two-surfaces... cannot compute the expansions") | Physicist | CONFIRMED verbatim |
| comité 015:113 — corrected `∫∫ρe^{−ρuv}dudv` null-Jacobian re-derivation | Mathematician | CONFIRMED, exact line found |
| comité 012:325-362 D1/D2 normative tokens (convexity MANDATORY_FOR_C1, etc.) | Mathematician (v2 Part A.1) | CONFIRMED verbatim, v2 reproduces token-for-token |
| comité 010 — Alloy 001/002 "exactly 4 Element" scope, non-admissible completion finding | Mathematician (v2 V.1b) | CONFIRMED, faithful paraphrase |
| A6.4 §II.1:186-195 — sig_sp exact-determination on minimals | Mathematician / v2 Part B | CONFIRMED (paraphrase of Spanish original, math claim accurately represented) |
| A6.4:302,319 — sig_lk/d⁺ `ADMISSIBLE_COMPONENT` status | v2 Part B | CONFIRMED |

- **Notes:** all checked citations resolve to real, on-topic text at or within one/two lines of
  the claimed location. No fabricated or misattributed citation found among the priority list. One
  minor, non-load-bearing imprecision flagged: a comité-010 internal cross-reference to EGS
  derived-md:223-225 (unrelated to this session's claims) actually describes a different horizon
  definition than the one it's pointed at; does not affect any of the twelve verified citations
  above.

## 8. Synthesis

**Unanimity on the core facts.** All seven roles agree: prereg-002's MATCH is scientifically
orthogonal to R-VAR v2's merits (physicist: "the future-truncation imprint is a property of
Schwarzschild causal structure, independent of any run's provenance"); v2 is well-posed as a
*parametric* mathematical object (logician); six of the nine comité-015 closures — (b), (f), (h),
(i) fully, (e) and (g) honestly-labelled-incomplete rather than falsely claimed complete — hold up
under independent re-derivation; the standing comité 014 blockade is unaffected and requires a new,
explicit, narrowly-scoped authorization, not a self-grant; all checked literature citations are
genuine (literature verifier).

**The falsifier's attack materially changes the picture wave 1 converged on, and the committee
adopts it.** Three of wave 1's "genuine closure" verdicts do not survive scrutiny at the substance
level, though they are not fabrications:
1. **Closure (a) is split.** The 𝒦_adm completion-class definition itself (comité 015's core
   complaint — "V.1 has no truth value") is genuinely fixed: 𝒦_adm is now a closed, well-typed,
   order-decidable domain inherited verbatim from comité 012 D1/D2 (mathematician, logician,
   literature verifier all independently confirm this). But V.1a's own internal quantifier
   ("escape(Cᵢ) = cualquier referencia anclada propia") is newly ill-posed in exactly the way
   comité 015 killed v1 for — the falsifier's two-poset construction shows it is either trivially
   true or a different, unstated, much stronger claim. **This must be fixed in writing (bind
   `escape(Cᵢ)` to a specific rule) before V.1a is registered as an Alloy-003 candidate.**
2. **Closure (c) is not yet delivered at the standard II.1 demands**, though v2 honestly labels it
   `[ENTREGADO — la adjudicación es del comité]` rather than falsely claiming full delivery. The
   witness pair is Hasse-disconnected (outside R-VAR's own domain) and never fixes whether the
   compositional test concerns the raw primitives or the exposed outputs. **Must be redone with a
   Hasse-connected pair and an explicit test-object definition before it can ground any
   CIRCULARITY_STANDARD adjudication.**
3. **Closure (d)'s hazard (undefined score) is genuinely fixed**; F3's *contribution* is honestly
   near-zero (redundant with the H≠∅ membership condition) rather than a substantive threshold —
   this is not a defect, but the "principled closure" framing overstates what F3 itself
   accomplishes. **Composite finding, adopted:** combined with the singleton-argmax gap (also in
   closure (d)), F3's redundancy means the typed abstention ladder's four τ-types collapse to ONE
   operative gate (`LOW_CONTRAST` vs. μ) in the single most common real case (a unique optimum) —
   not four independent safeguards. This must be stated plainly in any revision, not obscured by
   the ladder's four-type appearance.

**Four smaller fixes, adopted without further debate (falsifier §5, items 7-10 and the freeze-hygiene point):** (i) closure (e)'s normative-block label must read "SPECIFICATION-CLOSED, PROOF-OPEN," never bare `[CERRADO]`, until the Tier-0/Tier-1 falsification tests below pass; (ii) `M`'s exact value (not merely its floor ≥200) and the RNG spawn scheme must be fixed by an explicit written rule before any null is scored; (iii) v2 Part C.2's "es el único imprint order-visible" must be softened to "the only imprint currently identified/practical in this pipeline," since the physicist's own Θ_out discussion names a second (if doubly-disqualified, per falsifier item 10) channel; (iv) the μ-table freeze (step 4) and the falsification test (step 5) must draw from spawn-disjoint EXPLORE null sub-pools, not the same pool, closing the mild validation-circularity the falsifier flagged; (v) the C-COL κ-prohibition (v2:353-354) is correctly worded but currently document-local — it is elevated here to a standing rule binding on any future revision of v2 or successor document, not just this one.

**CIRCULARITY_STANDARD: neither wave-1 position is adopted as argued; the committee adjudicates
independently.** The mathematician's argument for `FUNCTIONAL_ONLY` ("the strong standard would
also condemn our own O_min") is accepted by the falsifier as **circular reasoning** — it treats
O_min's admissibility as a fixed point rather than something to independently justify. The
physicist's caution (the strong ban's universal "kills everything" claim is `[UNVERIFIED]`, and a
physically distinct apparent-horizon channel exists in principle, even if impractical here) is
closer to the falsifier's own reading. The falsifier additionally shows the fork as posed is a
**false dilemma**: bare `FUNCTIONAL_ONLY` risks being an unfalsifiable guardrail (functional
determination is ill-posed without fixing the test object), while the strong ban risks program
death without proof that it is actually required. **Adjudicated decision:
`CIRCULARITY_STANDARD = FUNCTIONAL_ONLY`, adopted not on the "it would condemn O_min" argument but
on independent grounds** — functional determination (a decidable, per-instance property) is the
correct formalization of what `NO_GROUND_TRUTH_LEAKAGE` actually prohibits (the hidden embedding
*defining* the observable), while mean-monotone correlation with a *different*, already-accepted
order-only statistic is not that failure mode — **conditional on three mandatory teeth, all
absent from v2 as written:** (i) the compositional test object is defined in writing as the
*exposed outputs* (S, T, E, U, τ), not the raw primitive set; (ii) a permanent, binding
`NON_CORROBORATION` clause: no future agreement between R-VAR and the sealed `O_min` estimator on
a BH patch may ever be cited as independent corroboration of the prereg-002 PASS; (iii) a permanent
limitation label on every R-VAR artefact stating the mean-monotone correlation with future-volume
explicitly. Absent these three conditions, `FUNCTIONAL_ONLY` is decoration, per the falsifier.

**The falsifier's single highest-severity finding — a silent-corruption failure mode — is adopted
as a mandatory precondition, not a caveat.** If the unproven Dinkelbach/staircase edge-locality
lemma (D.2.1) is false in the sprinkled regime, the DP silently optimizes over a wrong subfamily,
and because the *same* code computes both the μ-table (step 3) and the falsification test
(step 5), the corruption is self-consistent: the test would pass while every downstream T/E/U
belongs to an undocumented different selector. No abstention type in v2's typed ladder can detect
this. **The falsifier's brute-force cross-check (exhaustive enumeration vs. the DP, exact rational
arithmetic, N≲14, ≥100 posets both MINK and BH boxes, zero-disagreement acceptance rule) is
adopted as Gate 0 of the toy tier, executed and passing before any μ-table computation begins.**

**Scoped authorization: adopt the falsifier's narrow S1-S5 wording, matching the warden's
conditions.** Authorizes dev-only R-VAR v2 implementation, the deterministic toy tier (including
mandatory Gate 0), null-only EXPLORE calibration of μ, and the comité-015 falsification test on
calibration-disjoint nulls. Does **not** authorize BH-patch scoring (a separate report-back gate
after step 5), Alloy 003, Lean-as-physical-substitute, or citing R-VAR as corroboration of the
prereg-002 PASS. This changes nothing about `Q_DISPOSITION=Q_DIAGNOSTIC_CANDIDATE_ONLY` or
`OVERALL_VERDICT(014)=Q_REFERENCE_PATH_REMAINS_BLOCKED`.

**V.1a as Alloy-003 candidate: accepted, narrowly, and only after its quantifier is fixed.** Not
itself authorizing Alloy 003 (`ALLOY_003_AUTHORIZATION_STATUS = NOT_AUTHORIZED` stands).

**Momentum/halo risk (raised by the chair, addressed explicitly by the falsifier): real, and
mitigated by structure, not assertion.** Even this session's own dossier paragraph paired the
MATCH with "R-VAR v2 sigue pausado" in the same breath — a structural nudge the falsifier named
explicitly. The reverification MATCH and R-VAR v2's merits are adjudicated on separate, independent
records in this brief (§2 vs. §4-§5); the CIRCULARITY_STANDARD decision above was **not** made by
appeal to "we just had good news" but on the falsifier's independent functional-determination
argument. Binding for the record: **this decision would read identically if prereg-002 had never
needed reverification** — the closure of one is not evidence for or against the other.

**Why not a clean `RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP` on v2 as-is, and why not
`RECOMMEND_REVISE_AND_RECONVENE` either:** the defects found (V.1a's quantifier, the C.1 witness,
F3's labelling, the missing silent-corruption gate) are real but narrow, well-specified, and
individually small — none require another full committee session to re-litigate a mandate that
this session has otherwise substantially validated. They are exactly the shape of "conditions
precedent" this project's own precedent handles (comité 016's four preconditions before its own
PASS). The next-step spec below bundles these as a small, enumerated **v2.1 revision** plus the
narrowly-scoped authorization, mirroring that precedent.

## 9. Next-step spec

**Reversible steps (may be done now if the user asks; no code executed, no seeds consumed):**

1. **Revise `dev/PR003_R_VAR_SELECTOR_SPEC_V2.md` → v2.1**, addressing, in writing only:
   - Correct the stale `PASS_DEPENDENCY_LABEL` / preamble (`:17-22,:400-401`) to cite the
     reverification MATCH (`docs/prereg002_reverification_result.md`) and the current status
     `PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]`.
   - Fix V.1a's quantifier: bind `escape(Cᵢ)` to a specific, non-"cualquier" rule (e.g. R-VAR's own
     `E(Cᵢ)` when non-⊥), closing the falsifier's trivial-satisfiability / ambiguity attack.
   - Redo the C.1 separation witness with a Hasse-connected pair, and state explicitly whether the
     compositional non-determination claim concerns the raw primitive set or the exposed outputs
     (S, T, E, U, τ) — adopt the latter per §8's CIRCULARITY_STANDARD teeth.
   - Record `CIRCULARITY_STANDARD = FUNCTIONAL_ONLY`, test-object = exposed outputs, plus the
     `NON_CORROBORATION` clause and the permanent limitation label, verbatim from §8.
   - Add the falsifier's two-tier falsification test as **Gate 0** of the toy tier: Tier 0
     (committee-member-executed, by hand, on a 5-10 element witness pair plus one 15-20 element
     poset, before authorizing even the toy tier) and Tier 1 (automated brute-force cross-check,
     N≲14, ≥100 posets, exact rational arithmetic, zero-disagreement acceptance rule).
   - Relabel F3's closure honestly as "redundant with the H≠∅ membership condition, not an
     independent threshold," and state explicitly that the ladder collapses to one operative gate
     (`LOW_CONTRAST` vs. μ) on a unique-optimum argmax — not four independent safeguards.
   - Relabel closure (e) as "SPECIFICATION-CLOSED, PROOF-OPEN" in the normative block (Part H),
     removing the bare `[CERRADO]` token until Gate 0 passes.
   - Soften Part C.2's "es el único imprint order-visible" to "the only imprint currently
     identified/practical in this pipeline."
   - Enumerate the exact μ_n intensity levels and forbid interpolation; state that `M`'s **exact
     value** (not merely a floor) and the RNG spawn-key scheme are pinned by an explicit written
     rule **before** the μ-table computation step (not merely before its freeze-commit); require
     the freeze table (step 3-4) and the falsification test (step 5) to draw from spawn-disjoint
     EXPLORE null sub-pools, never the same pool.
   - Elevate the C-COL κ-prohibition (`:353-354`) from document-local wording to a standing rule
     that binds any future revision of v2 or successor document, cited by name.
2. Commit v2.1, with v1 and the original v2 marked superseded in the same commit (per this
   project's practice, e.g. `d0230b5`).

**Committing step (ONLY on explicit user authorisation, after step 1-2 are committed):**

3. **Grant the scoped authorization** (S1-S5, falsifier §5 / warden §6), pinned to v2.1's exact
   commit hash:
   - S1: dev-only implementation of the pinned R-VAR v2.1 selector; no import from the sealed
     path; no implementation of any A6.4 marker/gate/Q/tripartición/lateral pullback.
   - S2: the deterministic toy tier, including mandatory Gate 0 (Tier 0 hand-check, then Tier 1
     automated brute-force cross-check) — **BLOCKS all subsequent steps unconditionally on any
     disagreement, at either tier.**
   - S3: null-only Minkowski EXPLORE sprinkling for the μ_n table, `EXPLORE_POOL`-only with a hard
     pre-flight guard (abort on any seed outside the pool or intersecting `VALIDATION_SEEDS`),
     exact levels and exact `M` (not a floor) pinned first, on its own null sub-pool.
   - S4: commit the μ table + a frozen numeric decision rule (not "by construction"). This is its
     own checkpoint — the addendum (exact `M`, spawn scheme, levels) must already be committed
     before this step, not bundled into it after the fact.
   - S5: the comité-015 minimal falsification test on a **spawn-disjoint** null sub-pool from S3's
     calibration pool.
   - **Explicitly NOT authorized:** BH-patch scoring (separate future report-back gate); Alloy 003;
     Lean as a physical-definition substitute; citing R-VAR output as evidence about Q or as
     corroboration of the prereg-002 PASS; any seed outside logged `EXPLORE_POOL` spawn
     provenance.
   - On MISMATCH at Gate 0 or on failing the falsification test (S5): halt, do not adjust the DP
     or the test, reconvene the committee with the failure as a finding.

**Falsifier's minimal falsification test:** the Gate-0 brute-force cross-check above — the first
mandatory step of S2, before any other toy-tier or null work proceeds.

**Binding rules pre-committed:** `NO_RECONSTRUCTION_CLAIM` (claim boundary unchanged — order-only
localisation in a finite 1+1D patch); `NO_POST_HOC_TUNING` / `NO_THRESHOLD_LOOSENING` (F1/F2-basis/
F3/sig-fork frozen in writing before any EXPLORE code runs; `M`/spawn-scheme pinned before table
computation); `NO_GROUND_TRUTH_LEAKAGE` (EXPLORE_POOL-only hard guard; `VALIDATION_SEEDS`
permanently burned; `NON_CORROBORATION` clause; μ calibrated on nulls only); `RESPECT_SEAL_FREEZE`
(no sealed-path import, no threshold touch). `Q_DISPOSITION`, `OVERALL_VERDICT(014)`,
`PHYSICAL_IDENTIFIABILITY_STATUS=NOT_ESTABLISHED`, `ALLOY_003_AUTHORIZATION_STATUS=NOT_AUTHORIZED`
all unchanged.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off

_(left blank for the user — decision, date, and any overriding notes)_
