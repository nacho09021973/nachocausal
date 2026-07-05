---
name: comite-017-rvar-v2-adjudication
description: "R-VAR saga FULLY CLOSED 2026-07-05: comité 021's EGS graded object (longest-chain/future-cardinality over Min(C)) failed its own falsification test (MINK null quasi-degenerate, same tall-box-geometry mechanism as the earlier A(C) degeneracy); R_VAR_STATUS=CLOSED_NEGATIVE_RESULT (47be5c7), scoped to this geometry only; prereg-002/estimator-v2 track unaffected."
metadata: 
  node_type: memory
  type: project
  originSessionId: f1f91667-8861-4c95-a8b9-f7f967505a64
---

`docs/comite/comite_decision_017_r-var-v2-reconvene.md` (verdict
`RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`, not yet signed off / not yet committed to git as of
2026-07-04) re-adjudicated R-VAR v2 (`dev/PR003_R_VAR_SELECTOR_SPEC_V2.md`) now that
[[prereg002-pass-artifact-gap]] closed via SUPERVISED_REVERIFICATION_MATCH.

**Key finding: wave-1 experts (4 blind briefs) converged that v2's self-reported closures of
comité 015's 9 required items were genuine — the falsifier attack found 3 of them were closed in
letter, not substance**, after the chair caught and fixed a mid-session transmission error (wave-1
briefs were initially omitted from the falsifier's dossier). This is the concrete instance of the
"pattern-matching to what comité 015 wanted to hear" risk the chair flagged going in — worth
remembering as a reason to keep spawning a falsifier pass even when wave-1 looks unanimous.

**Substance gaps found (must be fixed in a v2.1 revision before any authorization executes):**
- V.1a's quantifier ("escape(Cᵢ) = cualquier referencia anclada propia") is trivially satisfiable
  or ill-posed depending on reading — same defect class that killed v1's V.1.
- The C.1 anti-circularity separation witness is Hasse-disconnected (outside R-VAR's own domain)
  and never fixes whether the compositional test concerns raw primitives or exposed outputs.
- F3:=1 is a vacuous no-op (redundant with an existing membership condition), and combined with
  the admitted singleton-argmax gap, the "4-type typed abstention ladder" collapses to ONE
  operative gate (`LOW_CONTRAST` vs. μ) in the common case — stated nowhere in v2 as a conjunction.
- CIRCULARITY_STANDARD: the mathematician's wave-1 argument for `FUNCTIONAL_ONLY` ("the strong ban
  would also condemn our own sealed O_min") is circular reasoning per the falsifier. Adjudicated
  decision: `FUNCTIONAL_ONLY` still adopted, but on independent grounds (functional determination,
  not mean-correlation, is what `NO_GROUND_TRUTH_LEAKAGE` actually prohibits) — conditional on
  three mandatory "teeth": test-object = exposed outputs (not raw primitives), a permanent
  `NON_CORROBORATION` clause (R-VAR/O_min BH-patch agreement may never be cited as corroborating
  the prereg-002 PASS), and a permanent limitation label on every R-VAR artefact.
- Highest-severity finding: a **silent-corruption failure mode** — if the unproven Dinkelbach/
  staircase edge-locality lemma (D.2.1) is false, the DP silently computes a wrong T/E/U, and
  because the same code computes both the μ-table and its own falsification test, the corruption
  is self-consistent (the test would pass while everything downstream is wrong). No abstention
  type in v2's typed ladder can see this. Remedy adopted as mandatory Gate 0 of the toy tier: a
  Tier-0 hand-checkable witness test + Tier-1 automated brute-force cross-check (N≲14, exact
  rational arithmetic, zero-disagreement acceptance rule) — must pass before any μ-table freeze.

**Scoped authorization adopted (narrow, falsifier-drafted S1-S5):** dev-only R-VAR v2.1
implementation + deterministic toy tier (incl. Gate 0) + EXPLORE-null-only μ calibration (exact M,
not a floor; spawn-disjoint sub-pools for calibration vs. falsification test) + the comité-015
falsification test. Explicitly NOT authorized: BH-patch scoring (separate future report-back
gate), Alloy 003, Lean-as-physical-substitute, citing R-VAR as corroboration of the prereg-002
PASS. `Q_DISPOSITION`/`OVERALL_VERDICT(014)`/`ALLOY_003_AUTHORIZATION_STATUS=NOT_AUTHORIZED`
unchanged.

**Momentum/halo risk was explicitly named and guarded against**: the chair's own framing paired
the good MATCH news with "R-VAR v2 sigue pausado" in one breath — flagged as a structural nudge.
Binding statement in the brief: this verdict would read identically if prereg-002 had never needed
reverification; CIRCULARITY_STANDARD etc. were adjudicated on independent merits, not on the mood
of a good audit day.

**Why:** demonstrates the project's `/comite` process catching its own convergence bias via the
falsifier role — worth citing as a positive example if asked "does the falsifier role actually
add value beyond rubber-stamping wave 1."
**How to apply:** before any R-VAR v2.1 work begins, check this decision's §9 next-step spec for
the exact revision checklist and the S1-S5 authorization scope; do not let "prereg-002 is closed"
be read as authorizing anything about R-VAR on its own.

**UPDATE 2026-07-04: v2.1 written and committed** (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_1.md`,
commit `6591f5f`), fixing all the substance gaps above. **PI then authorized S1-S5 narrowly,
explicitly capped to "Gate 0 Tier 0 only, stop after, no mu calibration without separate
follow-up authorization."** Gate 0 Tier 0 executed and PASSED (commit `b142377`,
`dev/measure_pr003_rvar_gate0.py` + `dev/PR003_RVAR_GATE0_TIER0_REPORT.md`): (i) the C.1 witness
pair (two Hasse-connected chains) showed matching d+(x), differing O(x), identical
EMPTY_FAMILY abstention; (ii) a 16-element permutation-poset cross-check of D.2.1/D.2.2 against
brute force, at every Dinkelbach step, zero disagreements. **Side finding, not yet applied to
the spec (out of scope for this session):** D.2.1's one-paragraph "staircase DP" sketch could
not be directly implemented as a scalar-threshold local DP; the correct algorithm is a
maximum-weight-closure/min-cut reduction (Picard 1976), which was implemented and verified
instead. Also found: the unconstrained optimum has a spurious tie with D=empty/D=C, confirming
the A(C) membership filters are load-bearing, not decorative. **UPDATE 2026-07-04 (same session): v2.2 written and committed** (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md`,
commit `6687357`), a surgical documentary-only patch — PI explicitly chose "v2.2 first, then
Tier 1" over jumping straight to Tier 1. Patches only D.2.1/D.2.2/D.2.3/Part E: the old "staircase
DP" sketch marked SUPERSEDED, replaced by the verified min-cut/maximum-weight-closure algorithm
(Picard 1976) — which turns out to work for ANY finite poset, not just dim<=2, a genuine
simplification. The spurious D=empty/D=C tie is elevated to a normative hard-constraint warning
(A(C) membership filters apply BEFORE optimization, not after). Gate 0 D.2.3 updated: Tier 0 =
PASS, Tier 1 still pending and still mandatory. v2.1 marked superseded pointing to v2.2.
**UPDATE 2026-07-04 (same session): Gate 0 Tier 1 authorized and executed — PASS** (commit
`55e19b8`, `dev/measure_pr003_rvar_gate0_tier1.py` + `dev/gate0_tier1_result.json` +
`dev/PR003_RVAR_GATE0_TIER1_REPORT.md`). PI authorization was conditioned on v2.2 being committed
first (it was, `6687357`). 382 posets auto-generated from EXPLORE_POOL seed 1000000 (spawn-derived
sub-seeds, N<=14, both MINK/BH kind per embedding); 100 with A(C) non-empty (the binding target)
tested against brute force at every Dinkelbach step, exact rational arithmetic — 0 mismatches.
83/100 showed the D.2.1 degenerate raw tie (D=empty/D=C at the unfiltered optimum — a structural
certainty for ANY poset, not data-dependent), correctly filtered in 100% of cases, confirming the
normative warning at scale rather than in one hand-built example. **Notable process point:** the
first run reported 58/100 "mismatches" (false GATE0_TIER1_FAIL) — root cause was a test-harness
bug, not an algorithm bug: it compared the min-cut tie set against a single `max()`-picked
brute-force representative instead of the FULL brute-force tie set, and ties (multiple down-sets
sharing the optimal ratio) turned out to be common at this scale even though Tier 0's one hand-built
poset happened not to have any. Verified by hand on one 12-way-tie case before fixing and
rerunning deterministically to 0/100 — worth remembering as a concrete instance of "the harness
can be the thing that's wrong, not the code under test," and as a reason automated Tier 1 catches
things a single hand-built Tier 0 example structurally cannot. Per PI instruction, stopped after
the Tier 1 verdict — does not authorize mu-freeze, Tier 2+, or any S2-S5 step; folding this result
into the spec text (a hypothetical v2.3, mirroring how Tier 0 was folded into v2.2) would need a
separate explicit authorization.

**UPDATE 2026-07-04/05: comité 018 resolved the EMPTY_FAMILY statistical-object hole** (PI: "no
llamemos S1 a la calibración μ"; `docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md`,
verdict `RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`). μ_n frozen as the conditional quantile of
`max S` given `𝒜(C)≠∅` (numerically option "A"), `EMPTY_FAMILY` rate reported separately per
intensity level as a claim-inert diagnostic (option "C" reporting). Mapping `EMPTY_FAMILY` to
`S:=0` (option "B") rejected on **type grounds** (S=0 is an achievable interior score value, not a
disjoint sentinel) — falsifier corrected the framing: B is not actually FP-unsafe (it preserves
`FP_RATE_NULL≤α` exactly by construction), so don't cite the FP-unsafe reason later. Falsifier
found the draft addendum itself under-specified as an executable procedure on 5 concrete grounds
(root→level allocation missing, abort-rule contradicted Tier1's actual code, false dilemma on
reusing root 1_000_000, "M" ambiguous on empty-vs-nonempty counting, OOD/step-5-floor deferred).
**Revised addendum committed at `0271fd9`** ("dev: freeze R-VAR mu calibration addendum"),
closing all 5 gaps — PI explicitly declined to commit `INSTRUCCIONES.md` alongside it (staged only
the addendum file). `/auditor` run afterward, `docs/auditor/auditor_report_006_...md`,
`AUDIT_PASS` (0 errors/warnings) — confirmed the commit matches comité 018's required tokens
verbatim, no silent deviation.

**UPDATE 2026-07-05: comité 019 convened to authorize Part F step 3 EXECUTION — verdict
`RECOMMEND_DO_NOT_PROCEED`** (`docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md`).
Major new finding, independently confirmed by 3 seats (mathematician, falsifier, warden via direct
code reading): **the only Gate-0-verified R-VAR implementation
(`dev/measure_pr003_rvar_gate0.py:family_A`) enumerates ALL `2^|Max(C)|` subsets of the maximal
antichain** — invisible at Tier 0/Tier 1's toy scale (N≤14) but expected to be catastrophically
infeasible at production `thresholds.INTENSITIES` (1500-12000). Part E's "polynomial for any
finite poset" claim describes the Picard min-cut step alone, not the enumerate-and-filter code
that actually passed Gate 0 — not the same verified object. Falsifier sharpened this further: the
D.1 admissibility predicate is disjunctive, so it may be **unproven that any polynomial algorithm
exists at all** for this problem, not just that a fast implementation is unwritten. Also found an
independent O(N³) cover-computation blocker, and that `OUT_OF_DOMAIN_UNCALIBRATED` (the frozen
halt rule) is *unreachable*, not just mistargeted, at production scale — certifying emptiness
itself requires completing the exponential enumeration. Physicist independently corrected a
scaling error inherited from comité 018 (production N is `intensity` directly per
`generator.py:47`, NOT ×BOX_AREA-inflated — so N=1500-12000, only 1.5-12x EGS's own n=10³, not
10-86x larger) — a good correction, but does NOT rescue the feasibility conclusion (severity
essentially unchanged; the falsifier independently confirmed the |Max| order-of-magnitude via box
geometry). Also: two wave-1 roles independently found a second, orthogonal ambiguity — the
addendum's "verbatim reuse of Tier 1" silently inherits Tier 1's `KINDS=("MINK","BH")` dual-sprinkle
dimension, which Part F's own MINK-only definition never resolves in text (zero "kind" mentions
anywhere) — **the PI hand-edited `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` mid-session (uncommitted)
to close this specific ambiguity** (explicit MINK-only rule, spawn-scheme closed locally, the
comité-018 dual-consumption-plan diff test promoted to a named hard precondition, and an explicit
disclaimer that production feasibility is NOT authorized/claimed by the addendum) — this edit is
good and consistent with the session's direction but does not touch the core feasibility blocker.

**Recommended next step (reversible, zero EXPLORE_POOL seeds, not yet executed as of session
end):** run a cheap dev-seed (outside EXPLORE_POOL, e.g. SEED=20240617 pattern) measurement of
`|Max(C)|`/`|covers|` at each of the 4 production intensities using the already-verified
`past_matrix_fast`, to replace asymptotic argument with an actual number, before any further Part
F authorization request. **Do NOT authorize Part F step 3 execution until that measurement exists
and, if infeasibility is confirmed, a new correctly-Gate-0'd algorithm exists or Part F's design
is reconsidered.**

**Why this matters for future sessions:** this is the second time in the R-VAR saga a
"looks-ready-to-execute, audit passed, tokens all present" moment turned out to hide a deeper,
unasked question when a full 7-role committee (not just an audit) was convened — first the
silent-corruption DP bug (comité 017→Gate 0), now algorithmic infeasibility (comité 018→019). Both
times the committee process caught something a narrower check (a token-match audit, a
self-reported closure list) did not. Treat "audit passed" as necessary, never sufficient, before
authorizing an execution step in this project — especially for anything computational that hasn't
been run at the actual target scale yet.
**How to apply:** before resuming, read `docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md`
in full (especially §9 next-step spec) rather than re-deriving from git log; do not treat
`dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md`'s commit (`0271fd9`) or auditor 006's PASS as authorization
to execute Part F — both are necessary, neither is sufficient, per this memory and per comité
019 itself.

**UPDATE 2026-07-05 (later same day): feasibility probe EXECUTED, verdict INFEASIBLE, evidence
committed.** The comité-019 §9 step-1 probe ran (dev seed 20240617, MINK-only, no μ, no
EXPLORE_POOL): |Max(C)| = 15/22/26/40 at intensities 1500/3000/6000/12000. At the primary
intensity 12000, 2^40 ≈ 1.1×10¹² subsets per draw — even an optimistic itertools floor is ~25h
per draw, before M=200 draws and before family_A's real per-subset cost. Per-level verdicts:
1500 FEASIBLE, 3000/6000 MARGINAL, 12000 INFEASIBLE → OVERALL INFEASIBLE (a fewer-than-4-levels
table would break the frozen "exactamente los 4 niveles" requirement, so one infeasible level
blocks the whole table). Evidence committed as `014d364` "Record R-VAR Part F feasibility
blocker": `dev/PR003_RVAR_PARTF_FEASIBILITY_PROBE_REPORT.md`,
`dev/measure_pr003_rvar_partF_feasibility_probe.py`, `dev/rvar_partF_feasibility_probe_result.json`.
Operative token: PARTF_CURRENT_ALGORITHM = INFEASIBLE. Next decision (PI, not yet made): (1)
redesign the algorithm to avoid 2^|Max(C)| enumeration, or (2) redesign 𝒜(C)/the selector so the
problem is computable without losing physical legitimacy. PI explicitly ruled out proposing level
restriction without an explicit comité (would break the 4-level freeze and look like convenience
tuning). Note the falsifier's open question: it is UNPROVEN a polynomial algorithm for
max_{D∈𝒜(C)} S exists at all (D.1's membership predicate is disjunctive, not Picard-closure
expressible).

**UPDATE 2026-07-05 (second follow-up, scratchpad exploration, NOT committed, NOT Gate-0'd):**
free-thinking session after the evidence commit found two things, both measured on dev seeds
(20240617/13/101, read-only, no EXPLORE_POOL):
1. **A polynomial exact algorithm for the SAME frozen object almost certainly exists.** Over
   down-sets, A(D) and B(D) are modular (Σ_v a_v, Σ_v b_v — already implicit in gate0's Picard
   reformulation); D=↓M reparametrizes 𝒜(C) by M⊆Max; and in these 1+1D sprinklings I_v =
   {m∈Max : v≤m} is a CONTIGUOUS INTERVAL of the sorted antichain (0 violations in 24/24
   poset-draws: MINK under u=t−r sort, BH under p=t+r ingoing sort). That makes the Dinkelbach
   inner problem a gap-DP O(K²) with lexicographic tie-break toward max B (handles the (0,0)
   boundary tie). Validated exactly vs gate0 brute force on the 16-element toy (modularity on
   all fam members, λ*, argmax all MATCH). Runs at production N in seconds even at BH K=426
   (brute force would be 2^426). Falsifier's "polynomial may not exist" concern resolved FOR 2D
   ORDERS via a per-draw interval certificate (checkable O(nK), typed abstention if it fails).
2. **A deeper blocker than compute: 𝒜(C) = ∅ for MINK at ALL production intensities,
   certified** (12/12 draws: zero unrelated (min,max) pairs — every minimal below every maximal,
   pure tall-box geometry T=6≫R=1.2, light crosses in Δt=1.2). BH is the opposite: 100% of
   minimals have partial intervals → family nonempty (horizon structure). So frozen Part F
   (μ over MINK nulls) would give rate_empty≈1 → OUT_OF_DOMAIN_UNCALIBRATED **even with infinite
   compute** — the frozen OOD rule fires correctly; the μ object is vacuous at production scale.
   Comité 019's physicist predicted the opposite (EMPTY_FAMILY rarer at large N) — measured wrong.
   Also suspicious (unverified values): BH argmax has |D*|≈N−few, B≈3–8 — S=A/B at production may
   be dominated by boundary cuts, not horizon cuts; physics question for comité.
   Probes were formalized into dev/ and committed at `6347459` (structure probe + interval-DP
   prototype + report); scratchpad copies superseded.

**UPDATE 2026-07-05 (third follow-up — comité 020, SIGNED): the whole thread is now adjudicated
and committed.** `docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md`
(BRIEF_CHECK=PASS, verdict RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP, warden PASS, PI signed §11
2026-07-05). Decisions:
1. Part F disposition = "never executed, BLOCKED_BY_MEASURED_DEGENERACY" (never say "produced
   OOD" — that token requires an actual run). Degeneracy at production = strongly-supported
   empirical prediction, NOT theorem (12 dev draws → M=200 pool is inductive; logician).
2. EMPTY-vs-nonempty dichotomy as object: REJECTED unanimously (post-hoc promotion on seen
   draws; box-aspect-ratio artifact detector; OOD→PASS coercion).
3. **Signed direction:** re-scope the immediate goal to order-only Schwarzschild-singularity-
   truncation localisation with a GRADED observable and non-degenerate MINK null (EGS
   future-cardinality/longest-chain bimodality direction) — needs a NEW /comite question to
   define the object, freeze ∀-before-∃ on unseen seeds, EGS regular-BH caveat inside the claim
   text. If that object fails its own Gate 0/calibration → R-VAR closes as documented negative
   result. Estimator-v2/prereg-002 track unaffected.
4. Interval-DP: mathematics survived hostile review (modularity + ∅-certificate independently
   re-derived; Bombelli 1987 CONFIRMED for order-dim-2), but DISQUALIFIED as implemented —
   cross-key probe ran (commit `5014a39`): **branch (a), BH certificate FAILS under the MINK key
   u=t−r** → abstain/OK boundary is key-dependent and the prototype picks the key from the
   hidden kind label = NO_GROUND_TRUTH_LEAKAGE as implemented. Blocked until an order-only key
   derivation (e.g. consecutive-ones/PQ-tree or 2D-realizer extraction from the order) is
   specified and frozen; also needs typed abstentions (NO_CONVERGENCE, cert-fail), exact
   arithmetic (no float64/1e-6), fresh Gate 0 Tier 0+Tier 1 with criteria committed pre-run,
   and independent non-author review (chair-authored-everything gate was NOT satisfied).
5. Record committed at `4a408a8`: comité 015–020 + auditor 003–006 + addendum's +48
   strictly-tightening lines (warden had found the ENTIRE adjudication chain untracked — "a
   working-tree freeze is not a freeze").
6. **Still pending (need explicit authorization):** §9 step 4 disposition-commit (PARTF_STATUS
   token note) and step 5 Part E re-scope amendment ("polinomial para todo poset finito" → 
   "polynomial for orders passing the per-draw interval certificate under a frozen order-only
   antichain ordering; typed abstention otherwise", no-budget-cap clause untouched, interval
   lemma flagged project-derived — no biblioteca source).
Biblioteca note: "Surya Foundation Model for Heliophysics.pdf" (NASA/IBM solar AI paper, name
collision) was moved OUT to /home/adnac/fuera-de-biblioteca/; the real Sumati Surya LRR 2019
(arXiv:1903.11544) is now at biblioteca/Surya_2019_Causal_Set_Approach_LRR_arXiv1903.11544.pdf
(title page verified). Other lit fixes from 020 §7: EGS regular-BH caveat is on PDF p.12 not
p.11; "C_k"/d+ Benincasa–Dowker terminology is a project bridge, not source notation.

**UPDATE 2026-07-05 (fourth follow-up): §9 step 4 disposition-commit EXECUTED.**
`docs/rvar_partF_disposition.md` committed at `896ec3e` — a standalone file (not folded into
comité 020 itself) carrying the PARTF_STATUS token verbatim, anchored to `6347459`/`014d364`/
`0271fd9`/`4a408a8`/`5014a39`, explicitly stating what it does NOT do (does not close R-VAR,
does not touch the Part E re-scope, does not rehabilitate the interval-DP, does not touch the
seal). `make verify-seal` re-checked before commit — matched `docs/preregistration_002.md:8`.
**Only step 5 (Part E re-scope amendment) and step 6 (new /comite question for the graded
EGS singularity-truncation object) remain pending** — PI explicitly chose to sequence them
separately rather than bundle, per PI's own stated order (disposition note first, alone,
"para que mañana... nadie reabra R-VAR como si fuera un fallo pendiente de depuración").

**UPDATE 2026-07-05 (sixth, FINAL follow-up): comité 021 convened for step 6, ran its own
falsification test, and R-VAR CLOSED as a documented negative result.**
`docs/comite/comite_decision_021_rvar-egs-truncation-object.md` (commit `a15c1a3`, verdict
`RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`) adjudicated the candidate object: PRIMARY =
longest-chain-from-minimal height `L(i)`, SECONDARY = future-cardinality restricted to
`Min(C)` (`⊆` sealed `O_min`), both order-only, no auxiliary sort key. **Falsifier seat
(corroborated independently by literature-verifier) overturned wave-1's working assumption**
that MINK non-degeneracy follows from physical necessity: EGS's "n vs √n already in
Minkowski" evidence is textually scoped to a **causal diamond**, not this project's frozen
**tall box** (`T_EDGE=6.0 ≫ R_EDGE=1.2`) — the same geometry mechanism that made `𝒜(C)=∅` for
MINK 12/12. Also found: `NON_CORROBORATION` (comité 017 §8) binds BOTH variants (imprint-based,
not functional-based, per the clause's actual wording), not just future-cardinality as wave-1
read it; and the sprinkling domain `r∈[0.1,1.3]` excludes `r=0`, so the measured truncation is
an excision-boundary proxy, not the physical singularity. Comité mandated a dev-seed-neutral
falsification test (zero new seed consumption) as the required gate before any spec draft.

**Test ran** (`dev/measure_pr003_rvar_egs_falsification_test.py` →
`dev/rvar_egs_falsification_test_result.json`, commit `3b46d2b`, report
`dev/PR003_RVAR_EGS_FALSIFICATION_TEST_REPORT.md`), reusing the same three dev seeds
(20240617/13/101) already consumed by the structure probe. **Result: MINK coefficient of
variation for both L(i) and future_card(i) was 0.006–0.024 at every intensity/seed, vs.
0.72–1.01 for BH (40–100× gap)** — every MINK minimal has nearly identical longest-chain
length and future cardinality, a near-delta-spike null, not graded spread. BH-side signal
itself is genuine and strongly separated (Cohen's d 5.9–9.2) and interior occupancy correctly
SCALES with `n_min` (no corner-artifact relapse) — but a strong BH signal can't be calibrated
against a near-degenerate MINK null. **Second independently-designed object hit the same
geometric wall as the first (binary) object.**

**PI decision (2026-07-05): CLOSE as documented negative result**, per the criterion
pre-committed in comité 020 §11.3. Recorded at `docs/rvar_closure_negative_result.md` (commit
`47be5c7`), token `R_VAR_STATUS = CLOSED_NEGATIVE_RESULT [NO_NONDEGENERATE_MINK_NULL_FOUND_ON_FROZEN_GEOMETRY;
...; GEOMETRY_SPECIFIC; PRIMARY_TRACK_UNAFFECTED]`. Explicitly scoped: this is a statement
about THIS frozen box geometry and these two tested objects, NOT a universal claim that no
order-only horizon diagnostic could ever work — a differently-shaped patch or a
geometry-normalized statistic is a **new** committee question with its own prereg, never a
reopening of this line (`NO_POST_HOC_TUNING` forbids redesigning on the same inspected dev
seeds). `make verify-seal` reconfirmed MATCH at every step; prereg-002/estimator-v2 PASS
track completely unaffected throughout.

**R-VAR SAGA IS NOW FULLY CLOSED.** Full chain for future reference: comité 015→020 (`𝒜(C)`
object, blocked by degeneracy, `896ec3e`) → Part E re-scope (`c92cb40`) → comité 021 (EGS
graded object, `a15c1a3`) → falsification test (`3b46d2b`) → closure (`47be5c7`). Nothing
further pending on this line unless a future session opens an entirely new committee question
for a differently-scoped object.

**UPDATE 2026-07-05 (fifth follow-up): §9 step 5 (Part E re-scope) EXECUTED.**
`dev/PR003_R_VAR_SELECTOR_SPEC_V2_3.md` committed at `c92cb40` (new versioned file, following
the project's established v1→v2→v2.1→v2.2 pattern rather than an in-place edit). Strikes the
false universal claim "se computa en tiempo polinomial para todo poset finito"
(v2.2:489-501) — the only Gate-0-verified impl (family_A) restricts to 𝒜(C) via `2^|Max(C)|`
enumeration, measured INFEASIBLE at production (`014d364`); the Picard min-cut alone solves the
unrestricted closure, not the 𝒜(C)-restricted selector. Substitutes: "polynomial for finite
orders that pass the per-draw interval certificate under a frozen order-only antichain
ordering; typed abstention otherwise." No-budget-cap clause left untouched (verbatim, per
comité 020 forbidden-moves (3)(ii)); interval lemma flagged project-derived (no biblioteca
source). Patch scope verified via diff against v2.2 to be Parte E + Parte H metadata only —
D.2.1/D.2.2/D.2.3 and closures (a)-(i) inherited unchanged, new closure (j) added for this
patch. `make verify-seal` re-checked before commit, matched. **R-VAR saga fully caught up to
comité 020's authorized steps: only step 6 (new /comite question defining the graded
Schwarzschild-singularity-truncation object) remains, and per the PI's signed direction it is
a fresh committee chapter, not a repair of R-VAR/Part F.**
