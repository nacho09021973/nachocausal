# Comité Decision 018 — rvar-mu-empty-family-object-choice

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

PI, 2026-07-04, verbatim: "Solicito veredicto sobre el hueco abierto en
`dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` antes de autorizar Parte F." The narrow question: for the
μ calibration table over EXPLORE nulls (R-VAR v2.2 Part F), should the statistic be calibrated
(A) conditioned on `𝒜(C)≠∅` only; (B) over all sprinklings, treating `EMPTY_FAMILY` as
score/max = 0; or (C) reporting both magnitudes separately (`EMPTY_FAMILY` rate and the
conditional μ distribution), leaving the downstream decision rule explicitly pending. The PI
explicitly did **not** request authorization to execute Part F — only to fix the statistical
object the addendum must freeze.

## 2. Verified state

Facts checked **this session** (2026-07-04), each with its command / file:line.

- Seal: `make verify-seal` → `nachocausal/thresholds.py` sha256 =
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, MATCHES
  `docs/preregistration_002.md:8`. Re-confirmed independently by the warden this session.
- git HEAD = `55e19b8` ("dev: R-VAR v2.2 Gate 0 Tier 1 -- PASS (100 posets, 0 mismatches)").
  `git status --short`: clean except pre-existing untracked files (including three prior
  uncommitted comité briefs, 015-017, awaiting user sign-off — not this session's concern) plus
  the new draft `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` (untracked, uncommitted this session).
- **No seed touched, no code executed this session.** The chair's only actions were reading
  files, `make verify-seal`, `git status`/`git log`, and writing the draft addendum text.
- `dev/gate0_tier1_result.json` independently re-read and diffed against
  `dev/PR003_RVAR_GATE0_TIER1_REPORT.md`'s claimed numbers and against `git show
  55e19b8:dev/gate0_tier1_result.json`: `total_posets_generated=382`,
  `n_empty_family=282` (MINK 190/191, BH 92/191), `n_nonempty_family_tested=100`,
  `n_mismatches=0`, `n_degenerate_raw_ties=83`, `OVERALL_STATUS=GATE0_TIER1_PASS`. Numbers match
  exactly; committed at `55e19b8`. `TOY_INTENSITY=9.0` used for this run — explicitly labelled by
  the report itself as non-calibration/non-production, distinct from `thresholds.INTENSITIES`.
- `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md` re-read: Part D.1 (𝒜(C), order-decidable predicates),
  Part D.3 (typed abstention ladder, fixed order `DISCONNECTED_HASSE → EMPTY_FAMILY →
  LOW_CONTRAST (vs μ) → INCOHERENT_ARGMAX`, `:453-458`), Part D.4 item 1 (`FP_RATE_NULL`
  reporting mandatory by intensity level, `:472-473` — the warden corrects the dossier's citation
  of a non-existent "D.4.1" subsection; substance unaffected), Part F/F2 (`:507-552`, μ_n
  procedure, requires M exact + spawn scheme + levels + disjoint sub-pools fixed **before step 3
  begins**, not merely before step 4's freeze-commit).
- `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` (status `DRAFT_NOT_FREEZE`, written this session, not
  committed) fixes `M:=200` (the falsifier-of-017's named floor, `docs/comite/
  comite_decision_017_r-var-v2-reconvene.md:174,230-231`, taken as equality not inequality, argued
  from order-statistic granularity, not from any observed μ data), `SeedSequence(root).spawn(K)`
  (claimed verbatim reuse of Tier 1's executed recipe), the 4 intensity levels
  (`thresholds.INTENSITIES` verbatim), and a proposed disjoint EXPLORE_POOL sub-pool split
  (`MU_CALIBRATION_ROOTS`/`MU_FALSIFICATION_TEST_ROOTS`). It explicitly refuses to resolve
  A/B/C unilaterally and flags a further sub-question about reusing root `1_000_000`.
- `nachocausal/thresholds.py`: `INTENSITIES=(1500.0,3000.0,6000.0,12000.0)`, `THETA_FP=0.05`
  (Part F's reused, not derived, α basis), `DEV_SEEDS`/`VALIDATION_SEEDS` disjointness asserted at
  import time. `dev/explore_seeds.py`: `EXPLORE_POOL=1_000_000..1_000_039` (40 roots); reserved
  virgin band `[2_000_000,2_999_999]` permanently burned (comité 016), untouched.
- Standing comité 014 blockade unaffected; `CIRCULARITY_STANDARD=FUNCTIONAL_ONLY` (comité 017)
  and its 3 mandatory teeth unaffected; `ALLOY_003_AUTHORIZATION_STATUS=NOT_AUTHORIZED` unaffected.

## 3. Dossier

- `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` — the artefact under adjudication (§4, EMPTY_FAMILY
  convention hole).
- `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md` — controlling spec: D.1, D.2, D.3, D.4, Part F/F2.
- `docs/comite/comite_decision_017_r-var-v2-reconvene.md` — the mandate that produced v2.2 and
  required this addendum; its M-floor-not-frozen-value finding, its disjoint-sub-pool requirement,
  and its CIRCULARITY_STANDARD/NON_CORROBORATION adjudication.
- `dev/PR003_RVAR_GATE0_TIER1_REPORT.md`, `dev/gate0_tier1_result.json`,
  `dev/measure_pr003_rvar_gate0_tier1.py` — the executed, PASSED Gate 0 Tier 1 result and the
  actual script whose consumption/abort semantics the addendum claims to reuse.
- `nachocausal/thresholds.py`, `dev/explore_seeds.py` — sealed thresholds and seed hygiene.
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`
  (Eichhorn–Gamito–Stokes, arXiv:2605.06813) — future-cardinality/boundary-sensitivity discussion
  (Fig. 3, line 226-253).

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

**RECOMENDACIÓN: adoptar C como forma del freeze, rechazar B, y fijar que la magnitud μ dentro de
C es idéntica al objeto de A. La regla de decisión "posterior" NO está toda pendiente — D.3 ya la
fija a nivel de parche; solo queda diferible el tratamiento OUT_OF_DOMAIN por nivel.**

1. B requires inventing a sentinel `max(∅):=0` absent from the sealed spec — a new redaction-time
   degree of freedom, violates `NO_POST_HOC_TUNING`; if EMPTY_FAMILY rate dominates at some
   production intensity, μ_n collapses to 0 (degenerate) — the exact pathology addendum §4(b)
   flags.
2. D.3's ladder already evaluates `EMPTY_FAMILY` before `LOW_CONTRAST` — a patch with `𝒜(C)=∅`
   never reaches the μ-comparison; therefore μ must be calibrated on the SAME population that will
   be compared against it at scoring time, i.e. conditioned on `𝒜(C)≠∅` — A's object and C's
   conditional magnitude are numerically IDENTICAL, not rivals.
3. EMPTY_FAMILY rate reporting is already mandatory per D.4 item 1 (`FP_RATE_NULL` by intensity
   level), not optional courtesy; in-repo precedent (Gate0 Tier1 script/report) already treats
   EMPTY_FAMILY as its own reported category, never scored as 0.
4. NON_CORROBORATION: B would launder a structural ⊥ into a numeric value inside μ, risking
   manufactured apparent corroboration downstream — violates the permanent clause.
5. The ONLY legitimately-pending item is whether a pathological per-level EMPTY_FAMILY rate should
   mark that level OUT_OF_DOMAIN — a SEPARATE freeze, must not be folded into this addendum or
   decided by peeking at data.
6. The root-1000000-reuse sub-question in addendum §4 is a DIFFERENT, unresolved issue (seed-
   partition hygiene) that must not be bundled with the EMPTY_FAMILY object choice; addendum's
   proposed `[1:21]`/`[21:41]` re-partition is infeasible without resizing EXPLORE_POOL (only 40
   roots exist).

Recommended freeze label: `MU_TABLE_STATUS = FROZEN [NULL_ONLY; PRE_BH_PATCH;
COND_ON_A(C)≠∅; EMPTY_FAMILY_RATE_REPORTED_SEPARATELY; LEVELWISE_OOD=PENDING]`.

### Mathematician brief

- **Computability:** All `𝒜(C)` predicates order-decidable, no realizer/`dim≤2` needed (v2.2 Part
  E, verified via Gate 0 Tier1 100/100). D.3 ladder fixed order: `DISCONNECTED_HASSE →
  EMPTY_FAMILY → LOW_CONTRAST → INCOHERENT_ARGMAX`; first two are structural/domain gates, only
  `LOW_CONTRAST` consumes μ.
- **Order observable:** `max_{D∈𝒜(C)} S(D)`, `S=A(D)/B(D)`, `A(D)=Σ[d⁺(x)−d⁺(y)]` over cut
  `H[C;D]` — order-only proxy for future-volume jump at horizon (EGS bimodality).
- **Caveats/judgment:** **`𝒜(C)=∅` IS an order-theoretic invariant** (fully order-decidable,
  independent of embedding) — not an implementation artifact, `NO_GROUND_TRUTH_LEAKAGE` not at
  stake. **`S` has NO well-defined domain when `𝒜(C)=∅`** — max over empty set is undefined, not
  zero. **"Score=0 for EMPTY_FAMILY" (B) is order-theoretically WRONG**: `S=0` is an INTERIOR
  ACHIEVABLE value (`A(D)=0` for genuine balanced cuts) — folding empty families onto 0 collides
  them with real balanced-cut cases, corrupting the null distribution exactly at the decision-
  relevant center. Also contradicts the selector's own control flow: `EMPTY_FAMILY` abstains
  BEFORE reaching the μ-gate — calibrating on a mixture including patches the gate never sees is a
  type error. **REJECT B.** **Correct object = C, read as: conditional law of max S given
  `𝒜(C)≠∅`, PLUS separately-reported EMPTY_FAMILY Bernoulli rate per intensity** — conditioning is
  FORCED by D.3; empty-rate reporting is ALSO required (real boundary-sensitive invariant per EGS
  "n to √n", AND already feeds mandatory `FP_RATE_NULL` channel D.4). A alone under-specifies
  (discards a real invariant the FP-channel needs); C dominates A. On "decision rule pending" in
  C: scoring rule for a BH patch with `𝒜(C)=∅` is ALREADY fixed by D.3 (abstains, EMPTY_FAMILY) —
  C does NOT smuggle a post-hoc DOF there; what legitimately remains open is only whether a
  pathological per-level empty-rate should mark that level OUT_OF_DOMAIN — a separate, principled
  freeze, not a μ-tuning knob. `[UNVERIFIED]` production MINK empty-rate; if non-negligible,
  conditional estimator (A/C) stays well-defined whereas B degenerates.

### Mathematical logic brief

- **Formal status:** μ-procedure is prose-level, not Lean-formalized; only 2 unrelated theorems
  proved in `Horizon.lean`. `S(D):=A(D)/B(D)` is a definition; `μ_n` is a definitional procedure
  with numbers pending; "S total on 𝒜(C)" is proof-by-definition, not a theorem; D.2.1
  edge-locality remains an open unproven lemma; EMPTY_FAMILY convention is an OPEN DECISION.
- **Quantifier/dependency order:** addendum must freeze the object BEFORE step 3 touches data.
  Hazard: if C's "eventual decision rule" is a bare unbound existential ("some future rule TBD"),
  that rule could be instantiated AFTER seeing the EMPTY_FAMILY rate and μ distribution — a
  post-hoc DOF, violates `NO_POST_HOC_TUNING`. Quantifier subtlety: `𝒜(C)≠∅` is existential over
  D; `H[C;D]≠∅` is per-D — the accurate statement is a one-way entailment (`D∈𝒜(C) ⟹ H≠∅ ⟹ S
  defined`), not a family-level biconditional as comité 017 stated it.
- **Type discipline:** `S:{D∈𝒜(C)}→ℚ` is a PARTIAL function on patches, undefined exactly where
  `𝒜(C)=∅`. EMPTY_FAMILY is a typed structural abstention (`τ=EMPTY_FAMILY`), evaluated BEFORE the
  μ-gate. **B is a genuine category error**: assigns a numeric value where max is undefined; worse
  than an out-of-codomain sentinel because 0 IS attainable (`A(D)=0` for cancelling contrasts) —
  aliases structural-abstention onto an in-range score, destroying the D.3 type distinction.
  REJECT. **A is the correctly-typed μ-object.** **C is well-typed** and its μ table is
  NUMERICALLY IDENTICAL to A's; C's only addition is (i) reporting the empty rate (a load-bearing
  signal, 190/191 MINK at toy scale) and (ii) explicit deferral of the COMBINATION rule — honest
  and well-typed IFF BOUNDED: must (a) freeze `μ_n` = conditional quantile NOW, (b) freeze
  empty-rate as provenance NOW, (c) name WHICH later rule is pending and AT WHICH GATE it closes
  with its own pre-registration. Unbounded deferral re-introduces the open quantifier.
  Recommended: A's conditional quantile as the frozen `μ_n`, wrapped in C's reporting discipline,
  with the deferred combination rule explicitly named and gate-bound — never B.
- **Caveat:** the deferred "decision rule" is NOT needed for step 3 — per-patch EMPTY_FAMILY
  handling is ALREADY frozen at D.3 (fires before the μ-gate); the only residual open rule lives at
  the step-5 falsification/verdict layer (FP-rate denominator), already separated by the disjoint
  sub-pool rule.

### Physicist brief

- **Coordinates & patch:** null-calibration operates on the same frozen tall box (`T_EDGE≫R_EDGE`)
  as the paired BH box; finiteness forfeits asymptotic/global horizon claims — only `r=2M`
  localisation in a bounded patch survives.
- **Physical meaning:** `d⁺` is an order-only proxy for future-cardinality bimodality at the
  horizon (EGS Fig 3); on a NULL patch there is no singularity truncation and no horizon-induced
  bimodality — `μ_n` is the null distribution against which a BH patch's max-S must protrude.
- **Sprinkling domain:** production intensities (1500-12000) give N≈10.8k-86.4k, 10-86x larger
  than EGS's own N=10³ and vastly larger than Gate0's toy N≈65 (near-single-chain artifact).
  Production MINK empty-rate is UNMEASURED.
- **Claim boundary:** order-only `r=2M` localisation in a finite 1+1D Schwarzschild patch only;
  regular (Hayward-type) BH caveat carried (EGS:249, longest-chain partition likely fails for
  non-singular BHs).
- **Decision-question judgment:** **EMPTY_FAMILY rate is a physically/geometrically meaningful,
  boundary-sensitive quantity, NOT a nuisance to average away** — EGS:247 directly documents
  future-cardinality statistics (the same family `d⁺` derives from) are boundary-sensitive even in
  pure Minkowski ("varies between n and √n already for Minkowski"). A Minkowski patch yielding
  `𝒜(C)=∅` reports a genuine boundary/finite-size geometric fact, not noise. **Option B conflates
  a geometric/boundary effect with the score signal being calibrated** — injects
  structural-abstention mass into the continuous null score distribution, biasing μ_n downward,
  with a concrete degenerate-collapse failure mode already flagged in addendum §4. Option A avoids
  contamination but discards the boundary-sensitive signal. **Recommends C**: freeze two separate
  magnitudes — (i) EMPTY_FAMILY rate per intensity and (ii) conditional μ_n given `𝒜(C)≠∅` —
  decision rule left explicitly pending.

## 5. Falsifier attack

- **Concrete failure modes:**
  1. **The "consensus" object is not yet freezable — the consumption plan is unspecified.** The
     addendum fixes M=200 "por nivel" and "800 parches nulos en total... INDEPENDIENTES"
     (`dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md:38-40`) but never fixes *which roots feed which
     intensity level*, nor whether the 4 levels reuse the **same** child SeedSequences (same
     streams sprinkled at 4 intensities → cross-level correlated μ table, falsifying the
     "INDEPENDIENTES" claim) or consume disjoint child ranges. Nothing in §1-§4 selects one — an
     unbound execution-time DOF sitting inside the addendum itself.
  2. **The abort rule contradicts the "verbatim Tier 1" claim.** Addendum §2 says a root that
     exhausts 400 children without reaching M forces a **hard abort**. The Tier 1 script it claims
     to reuse verbatim does the opposite: on exhausting a root it silently proceeds to the next
     root (`dev/measure_pr003_rvar_gate0_tier1.py:180-186`). Two readings of the same freeze text =
     no freeze.
  3. **The consensus never engaged the strongest version of B.** All four briefs assert B "biases
     μ_n downward"/"manufactures corroboration." Doing the algebra: under B, `μ_n^B` is the
     0.95-quantile of the mixture, so the *unconditional* non-⊥ rate on nulls is exactly α (zeros
     pad the bottom, the quantile adjusts); under A it is `(1−p_empty)·α < α`. So **B holds
     `FP_RATE_NULL ≤ α` exactly, and A is the conservative choice, not the uniquely FP-safe one.**
     B still dies (S=0 is an attainable interior value — type collision — and `μ_n^B` degenerates
     when `p_empty ≥ 1−α`), but no brief derived this algebra; all four repeat the same
     dossier-supplied EGS quote and "type error" phrasing. Signature of dossier-anchored pattern
     matching, not four independent derivations — nobody caught failure modes 1 or 2 either.
  4. **F2 as sealed is ill-formed, and A is an amendment, not a reading.**
     `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:511-512` defines the quantile over "M parches NULOS"
     with statistic `max_{D∈𝒜(C_j)} S(C_j)` — undefined when `𝒜=∅`. Conditioning is
     architecturally forced by D.3, but textually this is a spec amendment, not a reading. Must be
     frozen as an explicit, quoted interpretation of a defective clause, not silently.
  5. **Production feasibility untested.** Gate 0 exercised N≤14; production λ=12000 gives
     N≈86k. No runtime budget or per-level completion order is frozen. `[UNVERIFIED: actual
     runtime at N≈86k]`.
  6. **Empty-rate estimator unfrozen.** Under stop-at-200-acceptances, `p̂ = n_empty/(n_empty+200)`
     is a biased estimator of the per-level empty rate; if it is to be "a geometry observable in
     its own right," its estimator and stopping-rule dependence must be frozen now.

- **Ground-truth leakage:** None via the embedding — `𝒜(C)=∅` is order-decidable and μ is
  null-only. **The real leak is data → convention:** the A/B/C choice is being adjudicated *after*
  seeing Tier 1's 190/191 MINK empty rate. The degenerate-collapse argument against B is only
  vivid because that number was seen. **The freeze rationale must rest solely on D.3's type
  ordering, striking all reliance on the toy rate** — otherwise this is a data-informed convention
  wearing a principled costume.

- **Freeze violations:**
  - The root-1_000_000 discussion (addendum:83-92) manufactures a **false dilemma**: it claims
    exclusion forces a `[1:21]/[21:41]` re-partition of the 40-root pool. Nothing requires 20/20
    symmetry — `MU_CALIBRATION_ROOTS := EXPLORE_POOL[1:20]` (19 roots) leaves the test half
    untouched. Presenting exclusion as infeasible pressures the committee toward reuse.
  - Deferring the OOD rule is **not costless** (see verdict coercion below).
  - Failure modes 1-2 mean that if execution were authorized on this text, the executor would
    resolve the enumeration/abort ambiguities *at run time* — post-freeze choices by construction.

- **Verdict coercion:**
  - The §5 label template reads `EMPTY_FAMILY_CONVENTION=<a|b>` — **option C does not even exist
    in the frozen vocabulary.** Fix the label or the reporting discipline silently coerces C into
    A.
  - **Vacuous step-5 PASS risk:** comité 017 already found the falsification test "has no frozen
    numeric decision rule." If the production empty rate is high, step 5's nulls are almost all
    EMPTY_FAMILY, `FP_RATE_NULL ≤ α` passes with near-zero power, and a test-that-cannot-fail gets
    reported as PASS. Freeze now: a minimum count of μ-gate-eligible (non-empty) nulls in step 5,
    below which the verdict is INCONCLUSIVE — never PASS.
  - A level that cannot be calibrated within budget must exit as
    `OUT_OF_DOMAIN_UNCALIBRATED` (unscoreable), never as a FAIL of the mechanism nor a
    PASS-by-omission.

- **Premature / over-broad claims:** One creep vector: elevating the EMPTY_FAMILY rate to "a
  geometry observable in its own right" (physicist) creates a new, un-preregistered observable; if
  any future text cites its boundary-sensitivity as evidence the pipeline "sees geometry," that
  violates the permanent NON_CORROBORATION clause (017). Freeze it as **provenance/diagnostic
  only**, claim-inert.

- **Independent-falsification gate:** Partially satisfied. The addendum author flagged the hole
  rather than self-adjudicating; Gate 0's brute-force cross-check covered the algorithm. But the
  four wave-1 briefs are not independent verifications of the *statistical object* — they share
  dossier anchors, identical phrasings, and identical blind spots (failure modes 1-3).

- **Minimal falsification test:** Deterministic, zero seeds, zero sprinkling: give the addendum
  text (§1-§4 only) to two independent agents with a mocked accept/reject oracle and have each
  independently write out the exact ordered consumption plan — (level, root, child_index)
  sequence, per-level stop condition, and abort trigger. **Diff the two plans.** Predicted
  divergence given failure modes 1-2 (per-root abort vs. next-root continuation; level/stream
  allocation). Any divergence proves the "consensus C" freeze is under-specified and must not be
  committed as written.

**Falsifier's bottom line:** B is dead (type collision at S=0, degenerate collapse), but not for
the FP reason the consensus gave. C-as-briefed ("bounded C" = A's conditional quantile + separate
empty-rate reporting) is the right object **only if** the addendum additionally freezes, before
any execution: (i) M counts non-empty draws, stated as an explicit amendment to F2's ambiguous
"M parches NULOS"; (ii) the exact root→level allocation, cross-level child-stream disjointness,
and a single abort semantics reconciled with `measure_pr003_rvar_gate0_tier1.py:180-186`; (iii) a
budget-bound OOD rule using only already-frozen numbers; (iv) the empty-rate estimator under the
stopping rule; (v) a step-5 minimum-eligible-nulls floor with INCONCLUSIVE below it. Without
(i)-(v), the 4-way consensus is freezing a label, not a procedure.

## 6. Pre-registration verdict

- **Verdict: PASS**
- **Freeze status:** No threshold is being fixed post-data here. `dev/
  PR003_R_VAR_SELECTOR_SPEC_V2_2.md:509-515` defines F2's procedure as a quantile of
  `max_{D∈𝒜(C_j)} S(C_j)` over M null patches — undefined when `𝒜(C_j)=∅`. `:446-458` (Part D.3)
  already fixes, in writing, that `EMPTY_FAMILY` is its own typed abstention firing before
  `LOW_CONTRAST` — not new information from validation data. `:467-479` (Part D.4) already
  mandates `FP_RATE_NULL` reporting by intensity level — separate reporting of a structural-
  abstention magnitude and a score-distribution magnitude is already the spec's existing
  discipline, not a new invention. Adjudicating "A conditioned on `𝒜(C)≠∅`, EMPTY_FAMILY rate
  reported separately" therefore does not consume any μ-table data. **Correction to dossier
  citation:** v2.2 has no subsection literally labelled "D.4.1" — the `FP_RATE_NULL` mandate is
  D.4's numbered item 1 (`:472-473`); non-load-bearing, but should not be cited as a verbatim
  subsection later.
- **M:=200 compliance:** comité 017's falsifier explicitly names "M≥200" as a floor, not a frozen
  value (`comite_decision_017:174,230-231`). The addendum's equality move is a structural,
  data-free argument (order-statistic granularity at α=0.05), not derived from any μ table — no
  null-scoring script has run between comité 017 and now (confirmed: HEAD=`55e19b8`, no μ-table
  artifact present, addendum states no seed touched).
- **Seal integrity:** re-confirmed this session, matches. Nothing in this question touches
  `nachocausal/` or the sealed entrypoint.
- **Seed discipline:** `EXPLORE_POOL`/`VALIDATION_SEEDS` disjoint by machine-checked assertion; no
  reserved virgin band touched or proposed to be touched. The root-1_000_000-reuse question is
  correctly flagged as a **separate**, not-yet-resolved seed-hygiene issue, out of scope for this
  verdict.
- **Reporting rule:** D.4's symmetric PASS/FAIL/INCONCLUSIVE rule is unaffected by A/B/C; C is in
  fact most aligned with it (reports both magnitudes side by side rather than letting one silently
  absorb the other).
- **Forbidden moves present? None identified**, subject to the falsifier's residual conditions
  (i)-(v) in §5 being closed in the next addendum revision — those are drafting completeness
  requirements, not freeze violations already committed.
- **Residual condition (binding on the eventual committed addendum, not a blocker on today's
  object-choice question):** per the logician and the falsifier, if C is adopted, the addendum
  must name, in writing, which later decision rule remains pending and at which gate it closes —
  an unbounded "decide later" deferral would itself become an open post-hoc quantifier.

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| EGS arXiv:2605.06813, "cardinality of the future of the minimal elements varies between n and √n... for Minkowski spacetime" — derived-md:247 | Mathematician, reproducibility engineer, physicist | CONFIRMED |
| EGS, bimodal longest-chain/future-cardinality distribution by r-coordinate — derived-md:226,237,239,245,247 | Physicist, mathematician | CONFIRMED |
| EGS, regular (Hayward-type) BH "likely does not allow a partition" — derived-md:249 | Physicist | CONFIRMED |
| EGS, finite-region event horizons of limited practical use, pivot to apparent horizon — derived-md:253 | Physicist | CONFIRMED (substance matches; "teleological" is the physicist's own paraphrase, not an EGS term — attribution should say so if quoted again) |

- **Notes:** All four citations resolve to real, on-topic text. **Important nuance on citation 1**
  (used by three of four wave-1 roles as the core anchor for "EMPTY_FAMILY carries real physical
  signal"): EGS's own rhetorical use of the n-to-√n sentence is a **caution about boundary
  sensitivity** (a threat to naive readings of the statistic), not a positive claim that the
  statistic is "physically real" in the sense the experts deployed it. This confirms the citation
  exists and says what is quoted, but its actual argumentative force is weaker/differently-angled
  than three briefs implied — it supports "this statistic is boundary-sensitive, treat it
  carefully" as much as "this statistic carries real physics." None of the four citations bear
  directly on the A/B/C question itself, which the literature verifier and the falsifier both
  independently flag is fundamentally an internal order-theoretic/type-discipline question, not a
  literature question — the type-error argument against B (mathematician, logician) stands
  independently of the EGS citation's exact rhetorical weight.

## 8. Synthesis

**The object-choice question is resolved, with high but not blind confidence.** All seven roles —
independently, though the falsifier shows wave 1's convergence leaned more on shared dossier
anchors than on four truly independent derivations — agree: **reject B**. `S=0` is an interior,
achievable score value (not a disjoint sentinel), so folding `EMPTY_FAMILY` into `score:=0` is a
genuine type/category error that collides structural abstention with real balanced-cut data,
exactly at the distribution's center. This holds regardless of the falsifier's correction that B
is not actually FP-unsafe in the naive sense wave 1 argued (B in fact holds `FP_RATE_NULL≤α`
exactly by construction) — B dies on type grounds, not FP-safety grounds, and the record should
say so precisely rather than repeat the less precise wave-1 framing.

**The frozen μ_n object is: the conditional quantile of `max S` given `𝒜(C)≠∅` (numerically
identical to option A), reported alongside the `EMPTY_FAMILY` rate as its own separate,
provenance-only diagnostic per intensity level (option C's reporting discipline).** This is
forced, not chosen: Part D.3's already-frozen abstention ladder evaluates `EMPTY_FAMILY` strictly
before the `LOW_CONTRAST`-vs-μ gate, so calibrating μ on any population other than
`𝒜(C)≠∅`-patches would calibrate against a population the gate never actually compares. The
`EMPTY_FAMILY` rate is additionally required reporting under D.4's existing `FP_RATE_NULL`
mandate and is a genuine, boundary-sensitive order invariant (tempered per §7's literature nuance,
but independently supported by the mathematician's and logician's pure type-discipline argument,
which does not depend on the EGS citation at all).

**This is NOT yet a committable freeze.** The falsifier's attack materially changes the picture:
the addendum draft, even amended to say "condition on `𝒜(C)≠∅`, report the empty rate," is
under-specified as an executable procedure. Five concrete gaps must close first (falsifier §5,
items 1-6, condensed to 5 binding items below), plus the false-dilemma correction on the
root-1_000_000 partition, plus scrubbing the addendum's justification prose of any reliance on the
already-observed toy 190/191 rate (the rationale must stand on D.3's type ordering alone — the
falsifier is right that leaning on an already-seen number, even a non-calibration toy number,
dresses a data-informed convention as a principled one). None of these gaps re-open the A-vs-B-vs-C
question itself; they are drafting-completeness conditions on the *next* revision of the same
addendum.

**No disagreement is hidden:** wave 1 unanimously preferred "C's framing," the falsifier agrees on
the destination but attacks the *rigor* of how wave 1 got there and the *completeness* of the
addendum text; the warden finds no freeze violation in adjudicating the object type today, but
attaches the same boundedness condition on C's deferred rule that the logician and falsifier both
independently raised. All three converge: the decision is soundly reached, the document
implementing it is not yet finished.

## 9. Next-step spec

**Reversible steps (text only; no seeds, no execution; may be done now if the PI asks):**

1. Revise `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` (still `DRAFT_NOT_FREEZE`) to record this
   session's adjudication and close the falsifier's gaps:
   - State plainly: `EMPTY_FAMILY_CONVENTION = COND_ON_A(C)_NEQ_EMPTY_WITH_SEPARATE_RATE_REPORT`
     (fix the `<a|b>` label bug — the frozen vocabulary must literally include this token, not
     silently coerce to bare "A").
   - Record that B is rejected on **type grounds** (S=0 is an achievable interior value, not a
     disjoint sentinel; EMPTY_FAMILY fires before the μ-gate in D.3's fixed order) — not on the
     FP-unsafety framing wave 1 used, which the falsifier's algebra shows is imprecise (B actually
     preserves `FP_RATE_NULL≤α` exactly; it is dead on type grounds regardless).
   - Strike any sentence justifying the object choice by appeal to the observed toy 190/191 rate;
     rest the justification solely on D.3's already-frozen type ordering.
   - State explicitly, as an amendment to F2's textually-defective "M parches NULOS" clause, that
     `M` counts patches with `𝒜(C)≠∅` only (non-empty draws) — an explicit, quoted interpretive
     amendment, not a silent reading.
   - Fix the root-partition false dilemma: correct to an asymmetric split (e.g.
     `MU_CALIBRATION_ROOTS := EXPLORE_POOL[1:20]`, 19 roots) that avoids reusing Gate-0-Tier-1's
     root `1_000_000` without requiring any resize of `EXPLORE_POOL`, OR explicitly accept the
     reuse with a stated rationale — either is fine, but the current "infeasible without
     resizing" framing must be removed as factually wrong.
   - Freeze an explicit root→level allocation and a single abort semantics for M-collection,
     reconciled with `measure_pr003_rvar_gate0_tier1.py`'s actual (continue-to-next-root, not
     abort) behavior — pick one, state it, and say why it may or may not diverge from Tier 1's
     precedent.
   - Freeze a budget-bound `OUT_OF_DOMAIN_UNCALIBRATED` rule: a level that exhausts its frozen
     root/child budget without reaching M valid draws halts and reconvenes rather than silently
     extending the budget or falling back to another pool. Falsifier's point: this costs zero new
     degrees of freedom (mechanical consequence of already-frozen numbers), so deferring it is
     strictly worse than freezing it now.
   - Freeze a step-5 minimum-eligible-nulls floor, below which the falsification-test verdict is
     `INCONCLUSIVE`, never `PASS` — guards against the vacuous-pass risk the falsifier names.
   - State the `EMPTY_FAMILY` rate is recorded as **provenance/diagnostic only, claim-inert** —
     never citable as evidence the pipeline "sees geometry" (binds to the permanent
     `NON_CORROBORATION` clause).
2. Optionally, run the falsifier's proposed zero-seed falsification test (two independent agents
   given only the revised addendum text + a mocked oracle, write out the exact consumption plan,
   diff them) as a cheap, reversible check that the revision actually closed the ambiguity — no
   seeds, no sprinkling, no committing action.

**Committing step (ONLY on explicit user authorisation, after step 1 is committed):**

3. Commit the revised addendum. This commit is itself the "freeze" comité 017 required before
   Part F step 3 may begin — it is a committing step in the project's existing sense (an
   uncommitted addendum carries no diff trail) but touches no seed and executes no code.
4. **Not authorized by this brief:** execution of Part F step 3 (μ-table computation) itself. That
   remains a separate, later authorization request, exactly as v2.2's own gating structure already
   requires (`NEXT_RECOMMENDED_ACTION`, v2.2 normative block) and as this committee's own §6/§9
   here reiterate.

**Falsifier's minimal falsification test:** the zero-seed dual-consumption-plan diff described in
§5, adopted as the acceptance check for the *revised* addendum before it is committed as the
Part-F-step-3 precondition.

**Binding rules pre-committed:** `NO_RECONSTRUCTION_CLAIM` (unaffected, out of scope here);
`NO_POST_HOC_TUNING`/`NO_THRESHOLD_LOOSENING` (object choice argued from already-frozen D.3
ordering, not from observed data; toy-rate reliance to be struck from the addendum prose);
`NO_GROUND_TRUTH_LEAKAGE` (`𝒜(C)≠∅` is order-decidable, no embedding access); `RESPECT_SEAL_FREEZE`
(nothing here touches `nachocausal/` or the seal). `Q_DISPOSITION`, `OVERALL_VERDICT(014)`,
`CIRCULARITY_STANDARD=FUNCTIONAL_ONLY`, `ALLOY_003_AUTHORIZATION_STATUS=NOT_AUTHORIZED` all
unchanged.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off

_(left blank for the user — decision, date, and any overriding notes)_
