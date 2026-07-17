# Comité Decision 035 — op22-bd-action-witness-adjudication

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Adjudicar el diseño de OP-2.2 (testigo de desarrollo en la familia PR011,
`docs/plan_operativo_15_julio_2026.md:349-368`), sin ejecutar cálculos ni escribir preregistro.
Seis preguntas:

1. ¿La prohibición de decisión 034 — "`f_bench`... can never seed OP-2.2, and appears in no
   promotion, feature, orientation, frontier or abstention decision"
   (`dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md:130-131`) — es absoluta, o puede sustituirse
   prospectivamente mediante una nueva procedencia Route-B? No basta reinterpretación narrativa:
   cualquier habilitación debe quedar explícitamente adoptada por una nueva decisión de comité.
2. ¿Puede admitirse la acción Benincasa–Dowker 2D como candidato único independiente para OP-2.2,
   declarando: (a) motivación bibliográfica anterior al scoring; (b) que usa `N0,N1,N2` con
   coeficientes teóricos fijos; (c) que `Σ_m N_m = |relations|` y que esta dominancia conocida se
   divulga como riesgo de selección adaptativa; (d) que la acción escalar no hereda
   automáticamente la dominancia de la firma completa?
3. ¿Cuál sería la convención exacta de intervalos y la fórmula BD que quedaría congelada? La
   transformación a `[0,1]` debe usar un rango teórico fijado previamente; evitar clipping salvo
   justificación expresa.
4. ¿Cuál es el kill-test falsable del escalar, con umbral fijado antes del scoring?
5. ¿Cómo se define un control masa-versus-forma operativo, definible antes de mirar resultados?
6. Puerta WP5: ¿qué propiedad transferible a 3+1D estudia la acción BD? No autorizar "proxy de
   horizonte" ni "localizador" por mera separación de masas.

Salidas posibles: (a) admitir el candidato para redactar un preregistro Route-B; (b) devolverlo
para revisión por falta de control geométrico; (c) rechazarlo y mantener cerrado el canal.

Restricciones de sesión: no ejecutar el escalar, no abrir PR013, no tocar OP-2.1/PR012/OP-2.3, no
modificar ningún archivo salvo esta acta.

## 2. Verified state

Facts checked **this session** (2026-07-17) by the chair, each with its command / file:line:

- `make verify-seal` → `thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` — matches the frozen seal
  (`docs/preregistration_002.md:6-8`).
- `git rev-parse HEAD` → `67cf15a1b4015de4513b9b600782213ddcdbbe84`; `git status --porcelain` →
  clean worktree throughout the session.
- `docs/comite/comite_decision_034_op21-certifier-opening.md` §9 (`:362-366`) lists "any
  subsequent opening of OP-2.2 (witness development)" as a **committing step requiring its own
  explicit PI authorization**; §11 (`:404-406`) confirms "OP-2.2 is not opened." 034 is the latest
  prior committee decision (`ls docs/comite/` → highest is `034`); no `docs/comite/comite_decision_0
  3[5-9]` existed before this session.
- `dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md:103-134` — the frozen OP-2.1 dev prereg,
  §4.2, `CELL-PR011`: witness `f_bench(poset) = |relations| / 6` (relation count over `C(4,2)=6`
  pairs, n=4 posets, drawn read-only from `dev/pr011_tv_certification_enumeration.py`), marked
  **`BENCH_ONLY_NON_PROMOTABLE`**: "`f_bench` is not a witness candidate, can never seed OP-2.2,
  and appears in no promotion, feature, orientation, frontier or abstention decision
  (op13:98-104)." This clause is the literal source of "decision 034's prohibition" named in
  question 1 — it lives in the frozen dev prereg governed by decision 034, not verbatim in
  decision 034's own prose.
- `research_program/work_packages/op13_positive_evidence_protocol.md` §4 (`:83-108`) — Route
  A/B provenance rules, full text read by the chair. §5 multiplicity (`:110-120`). §9 terminal
  precedence chain (`:190-208`); `OP_1_3_AUTHOR_TERMINAL = POSITIVE_EVIDENCE_PROTOCOL_PROVED`,
  `IMPLEMENTATION_READINESS = PENDING_GENERATOR_AND_WITNESS_SPEC` (`:229-230`).
- `nachocausal/thresholds.py:57` `DEV_SEEDS`; `:59-74` reserved virgin validation band
  `[2_000_000, 2_999_999]`; `docs/preregistration_002.md:18` `EXPLORE_POOL =
  1_000_000..1_000_039`; OP-2.1 minted its own disjoint `SYNTH_MC_BAND = [3_000_000,3_999_999]`
  (`OP21...PREREGISTRATION.md:82-94`). **No OP-2.2 dev seed band exists anywhere in the repo**
  (chair grep, this session).
- `research_program/work_packages/next_observable_candidate_matrix.md` (2026-07-11) — still
  named the "Active design front" by `research_program/work_packages/README.md:13-18`
  (unmodified since). Candidate B, "intrinsic-cut BDG/SMI contrast" (`:79-118`), is a **cut/
  partition non-additivity contrast** `I_order(X:Y)=S(X)+S(Y)-S(C)`, not a raw single-poset
  scalar. §6 sequencing rule (`:148-155`): "Open Candidate B only if [Candidate A] is killed or
  survives with a clearly non-depth channel."
- Candidate A (ladder-ensemble effective expansion, PR009/PR010) status: `dev/PR009_LADDER_
  ENSEMBLE_EFFECTIVE_EXPANSION_CLOSURE_DECISION.md` — `TERMINAL_LABEL: FAILED_DATA_CONTRACT`,
  "neither a dead observable nor a surviving observable." Successor `dev/PR010_REFERENCE_DEPTH_
  COVERAGE_DECISION.md` + commit `631da6c` — terminal `PR010_DESIGN_INFEASIBLE_REFERENCE_
  COVERAGE`. **Neither reached killed or survived**; the matrix's own §6 opening precondition
  for Candidate B is, on its literal terms, unsatisfied, and no committee decision records the
  matrix as superseded by `docs/plan_operativo_15_julio_2026.md`.
- `docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md`
  (falsifier `:225-236`, synthesis `:340-361`) — prior committee session on the same 1+1D vacuum
  Schwarzschild patch closed the BD curvature-field angle as a "definitive null" premised on
  "en vacío 1+1D... R_μν=0" and the BD boundary/molecule-area angle as a "non-sequitur
  dimensional" (codim-2 = point in 2D, action topological/Gauss-Bonnet). **This session's
  literature verifier (§7 below) found the R=0 premise UNCONFIRMED and literature-contradicted**
  — see §8 correction.
- `docs/comite/comite_decision_023_pr012-scope-adjudication.md:341-364` — correct BD primary-
  source notation is `N_i`/`N_m`, not `C_k`; confirms the decision question's own `N0,N1,N2`
  notation is the right symbol family (though, per §4 below, an incomplete term list).
- `docs/plan_operativo_15_julio_2026.md` §1.1 WP5 gate (`:52-62`); OP-2.2 spec (`:349-368`); stop
  rules (`:657-674`); "Qué NO autoriza este plan" (`:678-689`).

## 3. Dossier

Files and references the chair supplied to the committee:

- `docs/plan_operativo_15_julio_2026.md` (full document; esp. `:52-62`, `:349-368`, `:678-689`)
- `docs/comite/comite_decision_034_op21-certifier-opening.md` (full document)
- `dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md` (full document, esp. `:103-134`)
- `research_program/work_packages/op13_positive_evidence_protocol.md` (full document)
- `research_program/work_packages/next_observable_candidate_matrix.md` (full document)
- `dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_CLOSURE_DECISION.md`,
  `dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md`
- `docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md`,
  `docs/comite/comite_decision_023_pr012-scope-adjudication.md`
- `docs/claim_grammar.md:81,87,96,119,336`
- `nachocausal/thresholds.py:57,59-74`
- `biblioteca/derived-md/Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md`,
  `biblioteca/derived-md/Bhatnagar_2021_Causal_Set_Theory_and_Benincasa_Dowker_Conjecture.md`,
  `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`
- `dev/pr011_tv_certification_enumeration.py`, `tests/test_pr011_tv_certification_enumeration.py`
- `research_program/synthesis/op11_spherical_dual_target.md:133-140`

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

Scope: mechanical readiness only — whether a Route-B dev-then-freeze protocol for a BD-action
witness *can be built and enforced* today, independent of the scientific merits. I take the
frozen OP-2.1 dev prereg and the PR009/PR010 closures as the governing templates.

**1. The template already exists and is binding.** `dev/OP21_REFERENCE_CERTIFIER_
PREREGISTRATION.md` is a complete, reusable Route-B skeleton the BD candidate must match, not
merely echo: status `FROZEN_ON_COMMIT / NO_SCIENTIFIC_CLAIM` (`:3`); explicit governing theory
contract (`:7-9`); dedicated seed band declared and proven disjoint (`:82-94`); frozen derivation
rule for every RNG draw (`:95-99`); a `manifest()` with the exact op13:135-139 fields — commit
SHA, numpy version, `uname`, RNG rule, per-cell params, per-stream sha256, kernel source hash,
timestamps (`:76-78`); bit-exact double-run reproducibility gate C3 (`:163-165`); a frozen
terminal precedence chain (`:196-211`); one-shot rule (`:217-225`); and an integrity snapshot
re-verifying the seal after every commit (`:227-235`). PR009/PR010 supply the terminal-label
template: closure decisions carry a single `TERMINAL_LABEL` and quarantine internal values from
reuse. OP-2.2 already has its four terminals reserved (`plan:360-365`). So there is no format
gap — a candidate that does not fill this skeleton is, mechanically, `FAILED_DEVELOPMENT_
PROVENANCE` (op13 §4).

**2. Blocking mechanical precondition: no frozen OP-2.2 dev seed band exists.**
`nachocausal/thresholds.py:57` fixes `DEV_SEEDS`; `:59-74` reserves the virgin validation band
`[2_000_000,2_999_999]`; `docs/preregistration_002.md:18` fixes `EXPLORE_POOL =
1_000_000..1_000_039`; OP-2.1 had to *mint* its own `SYNTH_MC_BAND = [3_000_000,3_999_999]` and
prove it unreserved. OP-2.2 explores PR011 posets τ=0.95 vs τ=1.05 with dev sprinkling — it needs
its own declared band, disjoint from `DEV_SEEDS`, `EXPLORE_POOL`, the validation band, and the
OP-2.1 `SYNTH_MC_BAND`, plus a frozen per-draw derivation rule and a seed-band guard demonstrably
able to fail. None of that exists yet. Admitting the candidate before this band is defined and
its disjointness verified would be premature: freeze cannot bind seeds that have not been chosen.

**3. Question-5 control is a mechanical gate, not just a scientific one.** op13 §4 requires that
*before promoting f* the dev prereg register: dev seeds, search space, available information,
**selection rule**, dependencies, promotion criterion, and hash of all transformations — omitting
any one triggers `FAILED_DEVELOPMENT_PROVENANCE`. A mass-versus-form control that "cannot be
defined before looking at results" leaves the *selection-rule* and *promotion-criterion* fields
undefined at freeze time. That is a manifest-completeness failure by construction, independent of
the physics.

**4. Collinearity-with-f_bench must be firewalled in the manifest.** Question 2(c) concedes
`Σ_m N_m = |relations|`; `f_bench = |relations|/6` is `BENCH_ONLY_NON_PROMOTABLE` and "can never
seed OP-2.2." The prohibition attaches to that specific quantity and any channel that reduces to
it — not to the PR011 cell family as such. So a genuinely independent BD scalar is not barred *a
priori*, but the provenance manifest must (i) record the dependency on `|relations|` explicitly,
(ii) document a selection rule that excludes any promotion decision reducible to relation count,
and (iii) show the scalar was not chosen by inspecting `f_bench`'s quarantined values. Absent
that documented firewall, the candidate is indistinguishable at manifest level from a re-badged
`f_bench`, and question 1's requirement — an explicit new committee decision, not narrative
reinterpretation — is not met.

**5. The [0,1]/BD-formula convention (Q3) is a hashed transformation, so it must be frozen
pre-scoring.** Clipping is a transformation that can collapse values and move the TV; if used it
must be declared with express justification and its hash frozen before any draw.

**6. Sequencing precondition unresolved (flag, not my adjudication).** The matrix's own §6 rule
opens Candidate B only if Candidate A "is killed or survives with a clearly non-depth channel."
Candidate A closed twice on data-contract/coverage-design infeasibility — neither killed nor
survived. Whether the newer `plan_operativo_15_julio_2026.md` supersedes that gate is a
governance question for the wardens.

**Reproducibility-engineer bottom line.** Even granting a sound scientific case, admission for
immediate Route-B drafting is premature: three mechanical preconditions are absent — (i) a
frozen, disjointness-verified OP-2.2 dev seed band; (ii) a pre-scoring selection rule / mass-vs-
form control that lets the provenance manifest be completed (Q5); (iii) a documented f_bench/
`|relations|` collinearity firewall plus an explicit committee enabling decision (Q1).
Recommendation weighs toward **(b) return for revision**: the deliverable to unblock is a
manifest stub that names all seven op13 §4 fields, the new seed band, the frozen BD formula/
interval convention with justified (or excluded) clipping, and the kill-test threshold (Q4) — all
fixable on paper, none requiring execution. No token is at risk in returning it; coercing it into
(a) without these would violate `NO_POST_HOC_TUNING` and the freeze-before-data rule.
`[UNVERIFIED]` whether the newer operational plan formally supersedes `next_observable_candidate_
matrix.md` §6 — not stated in any file in the dossier.

### Mathematician brief

**1. The genuine BD D=2 action is a FOUR-term sum, not three. Verified.** Primary source, both
docs: `1/ℏ · S^(2)[C] = N − 2N₁ + 4N₂ − 2N₃` (BD2010 Eq.13, `biblioteca/derived-md/Benincasa_
Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md:117`; Bhatnagar Eq.3.11,
`...Bhatnagar_2021...md:523`), where `N = N₀` = cardinality and `Nᵢ` = number of inclusive order
intervals of cardinality `(i+1)` (`:123` / `:519`). This uses **N₀,N₁,N₂,N₃** — four abundances.
The coefficients `(1,−2,+4,−2)` are fixed by the 2D continuum limit `Bφ → (□ − ½R)φ` (Eq.12,
`:108`); they are not free.

→ **Direct hit on decision-question 2(b).** A candidate declared to use only `N0,N1,N2` (three
terms) with "fixed theoretical coefficients" is **NOT the BD 2D action**; it is a truncation that
drops `−2N₃`. Dropping N₃ destroys the very continuum-limit derivation that supplies the
coefficients, so the truncated object has *no* theoretical-coefficient provenance. Either the
spec must restore N₃ (become the true 4-term BD action) or it must stop calling itself
Benincasa–Dowker. This is the single most important correction before any freeze.

**2. `Σₘ Nₘ = |relations|` — correct as an identity, but only for m≥1, and it is a *derived*
result, not a quoted one.** Each inclusive order interval `I(x,y)={z : x≤z≤y}` has a unique
minimum `x` and maximum `y`, so intervals of cardinality ≥2 are in bijection with related pairs
`x≺y`. Hence `Σ_{m≥1} Nₘ = |relations|` (number of order relations). Checked on the 4-chain:
`N₁,N₂,N₃ = 3,2,1`, sum `= 6 = C(4,2)`, and `S = 4−6+8−2 = 4`. Note: if `N₀=N` is included the sum
is `N + |relations|`, not `|relations|`. This identity is **not stated verbatim** in BD2010 or
Bhatnagar; it is elementary and correct but must be logged as *derived*, not cited.

**3. Consequence for "distinguishing power" (order-theoretic, not empirical).** The scalar action
is a fixed linear form in `(N₀,N₁,N₂,N₃)`, and `N₁+N₂+N₃ = |relations|`. So the action is
algebraically tied to cardinality and total relation count — the same quantities as the banned
bench witness `f_bench = |relations|/6`. The action does not *automatically* inherit the full-
signature dominance (2(d) is fair as stated), because the alternating coefficients can partially
cancel the monotone relation-count growth. But it is a **single-poset functional with no
partition/cut**, so it can never isolate a differenced/boundary contribution the way `I_order(X:
Y)=S_order(X)+S_order(Y)-S_order(C)` (Candidate B) can. These are **different mathematical
objects**: the raw scalar carries the *cardinality-dominance* risk profile, whereas Candidate B
carries the *dimension-dependent/noisy-estimator* profile. The raw scalar's dominant risk is pure
mass discrimination, not horizon shape.

**4. In 1+1D vacuum this was believed to be an expected NULL for curvature** (superseded — see
§8 correction below, literature verifier). The continuum limit is `⟨S_ρ⟩ → ½∫√-g R + Vol_{d-2}
(J)` (Bhatnagar Eq.4.1, `:562-565`). In `d=2`, codim-2 is **0-dimensional**, so `Vol_0(J)` is a
*point count*, not an area — this confirms decision_002's non-sequitur-dimensional finding on the
boundary/molecule angle independent of the R=0 question. This bears directly on WP5-gate question
6 — the only transferable object is the codim-2 joint/boundary term of the BD action, and in
1+1D it degenerates to a point count, so **neither "proxy de horizonte" nor "localizador" is
licensed**.

**5. Principled [0,1] convention (question 3).** PR011 fixes n=4 posets (`C(4,2)=6`). The finite
space of posets on 4 elements is fully enumerable, so `S = N−2N₁+4N₂−2N₃` has an **exact, closed
theoretical range** `[S_min, S_max]` computed by enumeration (not simulation). Freeze `x ↦ (S −
S_min)/(S_max − S_min)`. Because that range provably bounds every attainable value at fixed n,
**no clipping is ever needed**; empirical clipping would collapse the alternating-sum extremes
and distort the TV lower bound. The range must be derived from the poset enumeration *before*
scoring, and n must be held fixed for the normalization to be well-defined.

**6. Mass-vs-shape control (question 5), math form.** Because `N₁+N₂+N₃ = |relations|` and
`N₀=N`, the action's leading behaviour co-moves with cardinality and relation density. A
principled, pre-scoring control is: condition on (or regress out) `N` and `|relations|`, and
require the *residual* action to still separate τ=0.95 vs 1.05. If the residual TV vanishes, the
scalar is a mass discriminator, full stop. This control is definable **before** looking at
results (it is pure algebra on the frozen linear form), so failure to define it would be a design
defect, not an intrinsic impossibility.

**7. Kill-test form (question 4), math principle.** With `N` and `|relations|` regressed out, the
residual BD-action TV lower bound between τ=0.95 and τ=1.05 must exceed a threshold frozen before
scoring; else KILL as "mass-only."

**8. Computability / order-invariance.** `N` and every `Nₘ` are order-isomorphism invariants, so
`S` is well-defined on isomorphism classes and embedding-independent — no ground-truth leakage
from the functional itself. Counting intervals of bounded cardinality is polynomial-time.

**Bottom line for the six questions:** the object as literally specified (`N0,N1,N2`) is a
mis-labelled 3-term truncation of a 4-term theoretical formula; the relation-count identity is
correct but derived and only for m≥1; a clean fixed-range [0,1] convention and a mass-vs-shape
control are both definable pre-freeze. Mathematically this supports **outcome (b) — return for
revision** (restore N₃, log the derived identity, freeze the enumerated range and the mass-
residual control) rather than admit as-is.

### Mathematical logic brief

**1. Formal status of the "f_bench can never seed OP-2.2" clause — both, but of two different
logical types.** It is doubly sourced: (a) a **frozen-artifact commitment**: a universally-
quantified prohibition inside a comité-034-governed dev prereg that no later decision has
reopened; (b) a **standing op13 provenance obligation**: any future witness must independently
satisfy Route-B selection hygiene (`op13:98-104`). (a) is a fixed prohibition on one named
object; (b) is a live rule any future witness must independently satisfy. The bar in (a) is not
"discharged" by anything — it is a permanent exclusion, closer in kind to `RESPECT_SEAL_FREEZE`/
`NO_THRESHOLD_LOOSENING` than to a dischargeable obligation.

**2. "Substitution via new Route-B provenance" vs "mere reinterpretation" — a change of object,
not a change of narrative.** `f_bench = |relations|/6` is a *specific* witness; the clause
quantifies over that object, not the class of all PR011-family witnesses. *Reinterpretation* =
re-labelling `f_bench`/the barrier without a new adaptive-dev→freeze→single-confirmatory chain —
forbidden, and per decision 034's own **D2 pattern** ("the instruction alone authorizes
nothing"), a prior narrative cannot self-authorize. *Prospective substitution* = a **different**
witness `f ≠ f_bench` carrying its own op13 §4 Route-B provenance — this does **not** require
reopening the frozen dev prereg; the new Route-B prereg stands *alongside* it. Either way, per the
D2 template, any enablement must be an explicit new committee decision, not an inference.

**3. Quantifier order and dependency structure required (op13 §4 Route B).** `∃f selected in dev
(over dev seeds/replicas) . freeze(hash(f)) . ∀ confirmatory replica r . coverage(f,r) holds` —
freeze must strictly precede the *single* confirmatory evaluation; the ∀ over replicas sits
*inside* a fixed `f`, never per-replica best-witness selection. The bar on `f_bench` is a side
constraint `f ∉ {f_bench}` — plus, critically, `f` must not depend on `f_bench`'s selection
history nor reuse the PR011 quarantine replicas for both selecting and certifying.

**4. "Σ_m N_m = |relations|" disclosed as a risk is NOT sufficient to discharge `ADAPTIVE_
SELECTION_UNCONTROLLED`.** `op13:106-108` is explicit: same-replica select-and-certify triggers
`ADAPTIVE_SELECTION_UNCONTROLLED` "salvo que exista una cota uniforme demostrada sobre toda la
clase de testigos" — an existence-of-proof over the whole witness class. Disclosure of a hazard
is an epistemic act; it instantiates no bound. Moreover, `Σ_m N_m = |relations|` is a **sharp
structural warning**: it states the BD scalar is, on this family, a deterministic function of the
relation count — i.e. potentially an affine/monotone reparametrization of the barred `f_bench`.
Under op13 §5 multiplicity, transformations are part of the cell tuple; an affine relabel of a
barred witness is **not a new object** and does not escape the bar. This must be excluded before
any freeze.

**5. Type/object discipline — Q2(d) must be PROVED as a precondition, not asserted.**
Structurally identical to decision 034's **D1** (a type signature proves module-level blindness
only, never the end-to-end fact — the chair adopted the stricter reading there). Whether the BD
scalar is a function of `|relations|` on the frozen family is a **decidable finite fact** (n=4,
`C(4,2)=6`, the family is enumerable via `dev/pr011_tv_certification_enumeration.py`). Asserting
non-inheritance without the check repeats the D1 fallacy. The precondition to discharge: *the BD
scalar is not an affine/monotone reparametrization of `|relations|` on the frozen family* —
proved by enumeration before freeze, not asserted.

**Bearing on the verdict.** Q1: the bar is *absolute for `f_bench`* and needs no override to
remain in force; a different witness can proceed only under a fresh Route-B prereg **and** an
explicit new committee decision. Q2: as stated, (c) does not discharge `ADAPTIVE_SELECTION_
UNCONTROLLED` and (d) is under-stated; both the replica-separation discipline and the enumerated
non-inheritance proof are *preconditions*, not disclosures. On the strict-reading template the
committee has itself adopted (D1/D2), a candidate presented with (c)/(d) as mere assertions is
**not ready for freeze** — this points away from outcome (a) and toward **(b) return-for-
revision** until the finite non-collapse proof and the dev/confirmatory replica separation are
exhibited.

### Physicist brief

**1. The scalar's continuum target is the wrong geometric object** (mechanism corrected in §8
below — literature verifier — but the conclusion survives). The 2D BD/Sorkin action's continuum
limit estimates the **Ricci scalar** R. The horizon target is **not** R. It is the marginally-
outer-trapped locus `Θ_out(r=2M)=0` (EGS Eq.12; mirrored as `h_M(x)=r/(2M)−1=0`). R and Θ_out are
geometrically distinct: R is a smooth radial function whereas Θ_out is defined precisely by its
sign flip at r=2M. A curvature estimator does not, by construction, see the horizon-defining
feature.

**2. The operationally-transferable 1+1D horizon diagnostic is a different construction
entirely.** EGS state that in 1+1D there is no transverse 2-surface, so `Θ` cannot even be
computed directly; the diagnostic that actually survives to 1+1D is the **longest-chain/future-
cardinality bimodality** with a sharp transition at r=2M, plus the finite-patch caveat that a true
event horizon needs an infinite sprinkling. The BD action is neither of these.

**3. Mass-vs-shape control (Q5) — definable before scoring, and it is the kill test.** The
`G_diamond` family carries a dilatation trap (`TV=0` iff same scale orbit), so the τ=0.95/1.05
separation must live in genuine *shape* (non-dilatation) content, not mass per se. A physically-
motivated control: mass-at-fixed-shape (hold the patch's null aspect ratio and placement relative
to r=2M fixed, vary M) vs shape-at-fixed-mass (hold M, vary the null extents / whether the patch
straddles r=2M). Pre-committed kill threshold: **if a patch lying entirely in the exterior
separates the two masses as well as a horizon-straddling patch, the signal is generic curvature/
cardinality, not horizon-specific → kill.** This matches the candidate-matrix's own kill
criterion. Because this control is definable now, the candidate is *not* un-freezable for lack of
a control — but the same control is what I expect it to fail.

**4. Q2(c)/(d), physics view.** `Σ_m N_m = |relations|` is raw cardinality; the alternating BD
coefficients are designed so the leading cardinality terms cancel and leave R. So (d) — "the
scalar does not automatically inherit the full-signature dominance" — is technically true but
physically hollow: escaping cardinality dominance lands you on the Ricci scalar, which in this
geometry still carries no r=2M-specific feature.

**5. Honest WP5-Q6 answer.** There is **no genuine horizon-specific, transferable-to-3+1D
property** in this scalar for this patch. Its only defensible transferable role is as a **generic
negative-control / null-check baseline** — a dimension-appropriate cardinality/interval-abundance
summary that any true horizon candidate must *beat* on matched horizon vs non-horizon cuts. Under
the OP-2.2 spec's own rule it must **not** be called "proxy de horizonte" or "localizador."

**Physicist recommendation.** Outcome **(b) return for revision** — or admit to Route-B
preregistration *only if* bound to: (i) the pre-committed exterior-only vs straddling mass-vs-
shape control with its kill threshold frozen before scoring; (ii) an explicit ceiling terminal of
`REFERENCE_WITNESS_SEPARATION_ONLY` (no horizon-proxy/localizer language); and (iii) framing as a
null-check/baseline, not a horizon observable. Absent (i)–(iii), physics reading supports **(c)
reject**: the scalar targets R, not Θ_out, and has no horizon-specific content in this 1+1D vacuum
patch.

## 5. Falsifier attack

### Falsifier attack

- **Concrete failure modes:**
  1. **The object as specified is not the BD action.** The decision question freezes "N0,N1,N2
     con coeficientes teóricos fijos" (3 terms); the repo's own verified formula is the 4-term
     `S^(2)[C]/ℏ = N − 2N₁ + 4N₂ − 2N₃`. A 3-abundance truncation destroys the continuum-limit
     coefficient provenance that is the entire "motivación bibliográfica" of Q2(a).
  2. **Structurally under-powered by the family's own certification.** OP-2.2 lives in the PR011
     τ=0.95/1.05 family, whose certified regime is "casi ciego": minimax floor `0.4954–0.4977`,
     `H² = 1.329e-06` (`docs/plan_operativo_15_julio_2026.md:32-36`). That floor implies TV ≤
     ~0.0092 [arithmetic: TV ≤ 1−2·0.4954], so **any** bounded witness — BD or not — has mean-gap
     ≤ ~0.0092. A kill-test threshold above ~0.009 kills every witness a priori; below it, the
     Hoeffding radius at OP-2.1-scale budgets (m=200 → r ≈ 0.11) swamps the signal by ~12×.
     Unless the prereg proves feasible (m, α) resolving a ≤0.009 gap, OP-2.2 with the BD scalar
     is decoration that can only reach `REFERENCE_WITNESS_INCONCLUSIVE`/`FAIL`.
  3. **Sequencing precondition unmet.** "Open Candidate B only if A is killed or survives with a
     clearly non-depth channel." Candidate A terminated `FAILED_DATA_CONTRACT` and `PR010_
     DESIGN_INFEASIBLE_REFERENCE_COVERAGE` — neither killed nor survived. And the raw single-
     poset BD scalar is **not even Candidate B**, which is an intrinsic-cut contrast with matched-
     cut controls; admitting it silently substitutes a new, matrix-unvetted candidate while
     claiming the matrix's legitimacy.
  4. **Physics prior update (see literature verdict): the "R=0" premise both wave-1 mathematician
     and physicist relied on for the "definitive null" framing is UNCONFIRMED and literature-
     contradicted** — EGS state the toy (1+1)D Schwarzschild metric they sprinkle into has
     "nonvanishing curvature," and a direct computation gives `R=2r_S/r³≠0`. This does not save
     the candidate (R still has no feature *at* r=2M, so it remains non-horizon-specific), but it
     means the reasoning chain used by two of four wave-1 experts to reach that conclusion was
     built on a false premise and must be corrected, not merely footnoted.
  5. **Q2(d) is an unproven assertion.** "No hereda automáticamente la dominancia" is exactly the
     decision-034 D1 fallacy pattern: whether `S_BD` is an affine/monotone function of
     `|relations|` on the frozen family support is a finite decidable fact, and `Σ_{m≥1}N_m =
     |relations|` makes collapse plausible. Asserting instead of enumerating is disqualifying.

- **Ground-truth leakage:** The PR011 family has no hidden embedding (synthetic laws), so classic
  embedding leakage is absent — but three substitute paths exist: (i) the physicist's "exterior-
  only vs horizon-straddling patch" control **cannot be defined inside the PR011 family** (it is
  parametrized only by R, V, τ — no r=2M, no patch placement); implementing it would import
  Schwarzschild coordinate/geometry data into a dev promotion/orientation decision, which op13
  explicitly bars; (ii) the [0,1] normalization range, if computed from dev scoring distributions
  instead of prior enumeration, encodes dev-replica information into the frozen transform; (iii)
  OP-2.2's "fidelidad geométrica" leg consults geometry by construction — if it co-decides which
  witness is "the one," that is selection by geometric ground truth, not diagnosis.

- **Freeze violations:** (i) No OP-2.2 seed band exists; any draw before a new disjoint band is
  minted and frozen reuses or burns a reserved band. (ii) Q4's kill threshold "fijado antes del
  scoring" is only meaningful if committed before **any** BD value is computed on PR011 laws —
  but `CELL-PR011` already computed enumeration-exact TV on the exact τ-pair, so the near-blind
  scale is already known; a threshold that happens to sit just under 0.0092 must be justified
  from the pre-existing certified bound explicitly, not chosen freely. (iii) Using the same dev
  replicas to tune the witness AND run its kill test triggers `ADAPTIVE_SELECTION_UNCONTROLLED`
  absent a uniform class bound; disclosure of the `Σ N_m` identity instantiates no bound and
  discharges nothing.

- **Verdict coercion:** (i) Questions Q3–Q6 ask the committee to state "la convención exacta ...
  que quedaría congelada" — answering them concretely pre-drafts the prereg the session is barred
  from writing; a (b) verdict that ships a complete frozen formula is (a) in disguise. This brief
  avoids that by stating candidate conventions as *requirements to be frozen in a future Route-B
  prereg*, not as already-frozen values. (ii) `REFERENCE_WITNESS_SEPARATION_ONLY` is a coercion
  magnet: mass separation reported as "positive progress" collapses the plan's own bar "no
  llamarlo proxy de horizonte si solo discrimina masas" and claim_grammar's forbidden
  identification "existe un test" = "existe un localizador." (iii) The predictable high-
  probability outcome in the near-blind regime is INCONCLUSIVE; any future prereg lacking an
  explicit, publishable-as-is INCONCLUSIVE path invites silent retry.

- **Premature / over-broad claims:** WP5-Q6 has no honest positive answer beyond negative-
  control/baseline: the only 3+1D-transferable BD object (codim-2 joint/SMI-area) degenerates to
  a point count in 2D; the curvature channel targets R, not Θ_out. Any WP5 pass phrased as "BD
  action studies a transferable horizon-relevant property" is an overclaim. `NO_RECONSTRUCTION_
  CLAIM` also bars letting τ-separation on n=4 abstract posets be narrated as anything about a
  horizon.

- **Independent-falsification gate:** Partially satisfied at committee level (wave-1 briefs are
  separated; decision-034 R6 precedent requires a separate-session `/auditor` before any
  terminal). NOT yet satisfied for the two load-bearing mathematical claims: the `Σ N_m` identity
  and the non-collinearity of `S_BD` with `|relations|` are currently asserted only inside briefs
  by their proposers, with no independent enumeration on record. Whoever authors a future Route-B
  prereg must not be the sole runner/verifier of that enumeration.

- **Minimal falsification test:** One read-only script over the already-frozen dev code (a
  reversible pre-flight step, **not executed in this session**, and requiring the user's separate
  authorization to run in a future session): enumerate the support of `P_4(0.95)` and `P_4(1.05)`
  via `dev/pr011_tv_certification_enumeration.py` (`build_diamond_family` → `poset_law_from_
  grid`), compute for each unlabeled poset the pair `(|relations|, S_BD)` with the **full 4-term**
  formula, and check (a) whether `S_BD` is a function of `|relations|` on that support — if yes,
  the candidate is an affine relabel of the barred `f_bench` and outcome (c) is forced; and (b)
  whether the `|relations|`-conditional residual of `S_BD` shifts at all between the two laws —
  if the residual TV contribution is 0, the mass-vs-shape kill test is already decided and the
  witness is dead before freeze. This single enumeration adjudicates Q2(c), Q2(d), Q4 and Q5
  simultaneously, costs seconds, consumes no seeds, and must be run/verified by someone other
  than the candidate's proposer **before** any Route-B prereg is drafted.

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: **BLOCK**
- Freeze status: No OP-2.2-specific thresholds/BD-formula/interval-convention/kill-test/mass-vs-
  shape control are frozen in writing anywhere in the repo — `docs/plan_operativo_15_julio_
  2026.md:349-368` states only qualitative bullets with no numeric thresholds, no BD coefficient
  set, no [0,1] range, no kill-test statistic. `op13_positive_evidence_protocol.md:229-230`
  records `IMPLEMENTATION_READINESS=PENDING_GENERATOR_AND_WITNESS_SPEC` — the governing protocol
  itself declares no concrete witness spec exists yet. Nothing for this step is frozen pre-
  validation because the step is pre-preregistration by design (session scope: adjudicate design
  only).
- Seal integrity: Not implicated — `make verify-seal` confirms `thresholds.py sha256: 6e2c3888…`
  matches the frozen record, and this session proposes no execution, no threshold edit, no seal-
  path run. Seal integrity is intact and undisturbed by the design question itself.
- Seed discipline: No OP-2.2 dev seed band exists yet (`nachocausal/thresholds.py:57,59-74`;
  `docs/preregistration_002.md:18`; `dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md:82-94` — none
  names an OP-2.2 band). A mechanical precondition for Route-B drafting is currently absent. No
  virgin/validation band is proposed to be touched in this session, so no burn has occurred, but
  the band that would need minting for Route-B drafting to be well-formed does not exist.
- Reporting rule: Not yet engaged — no scoring run is proposed this session. The binding op13
  terminal-precedence chain and the four OP-2.2 terminals already named (`REFERENCE_WITNESS_
  READY_FOR_FREEZE`, `_SEPARATION_ONLY`, `_INCONCLUSIVE`, `_FAIL`) are pre-committed as symmetric
  terminal vocabulary; nothing in the design proposal attempts to suppress or reweight any of
  them. Compliant in principle but untested by this session's scope.
- Forbidden moves present? None executed (no run occurred), but the design as scoped, if drafted
  into a preregistration today, would risk **threshold-freeze-by-narrative**: three of the six
  sub-questions (Q3, Q4, Q5) are exactly the frozen-before-scoring artifacts op13 §4 Route B
  requires, and none is fixed to a number/procedure in any committed document.
- Reasons:
  - **Governance/procedure (in narrow remit):** decision 034 §9 names "any subsequent opening of
    OP-2.2 (witness development)" as a **committing step requiring its own explicit PI
    authorization**, separate from this design-adjudication session, and confirms "OP-2.2 is not
    opened." This session's own restriction list is consistent with that gate — it is scoped as
    design-adjudication, not opening. A PASS-to-Route-B-drafting verdict here does not itself
    constitute the opening-authorization decision-034 requires; that remains a distinct future
    committing act.
  - **Governance/procedure:** the `f_bench` bar bars the *named object*, not the witness class per
    se — so a genuinely new, independently-provenanced Route-B candidate is not per se barred by
    mere existence of the bar. But per decision-034's own D2 pattern, any prospective
    substitution or enablement must be an **explicit new committee decision** — this brief
    records adjudication of design admissibility, not that enabling decision; the two must not be
    conflated in the acta.
  - **Freeze-status finding (bears on freeze-compatibility though scientific in nature):** Q2, Q3,
    Q4, Q5 ask for concrete frozen artifacts that op13 §4's Route B explicitly requires to be
    registered *before* promotion. None of these seven fields has a value fixed in any committed
    doc for OP-2.2 today. This is a warden-relevant gate, not a physics opinion: the manifest is
    incomplete by construction.
  - **Freeze-status finding:** `Σ_m N_m = |relations|` collinearity with the barred `f_bench` is
    disclosed as a risk (Q2c) but op13:106-108 requires a **demonstrated uniform bound over the
    whole witness class** to discharge `ADAPTIVE_SELECTION_UNCONTROLLED`, not mere disclosure —
    this does not yet exist in any document.
  - **Sequencing precondition, procedural but load-bearing for freeze validity:** the candidate
    matrix's §6 rule gates Candidate B on Candidate A reaching killed/survived; PR009/PR010
    reached neither. If OP-2.2 is understood as instantiating Candidate B, this precondition is
    unresolved in writing; if OP-2.2 is governed instead by `plan_operativo_15_julio_2026.md` as
    a superseding track, that supersession itself is not recorded as an explicit committee
    decision anywhere anchorable. This documentation gap must be closed (either "superseded, see
    decision-NNN" or "matrix still binds, Candidate A precondition unmet") before any
    preregistration text can claim freeze-consistency.
  - **Conclusion:** the design as scoped cannot proceed straight to Route-B preregistration
    drafting without first fixing, in a committed document, the seven op13 §4 manifest fields —
    none of which requires executing the scalar or opening PR013 to write down. This is a
    **named-prior-fix BLOCK, not a channel closure**: the acta records which fields are missing,
    not a rejection of the channel outright.

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| BD2010 Eq.13 `S^(2)=N−2N₁+4N₂−2N₃`, `derived-md/Benincasa_Dowker_2010...md:117` | Mathematician | CONFIRMED |
| BD2010 def. of N, Nᵢ (order intervals of cardinality i+1), `...:123` | Mathematician | CONFIRMED |
| BD2010 Eq.12 continuum limit `lim Bₖφ = (□−½R)φ`, `...:108` | Mathematician | CONFIRMED |
| Bhatnagar Eq.3.11 `N−2N₁+4N₂−2N₃`, `derived-md/Bhatnagar_2021...md:523` | Mathematician | CONFIRMED |
| Bhatnagar def. of N, Nᵢ, `...:519` | Mathematician | CONFIRMED |
| Bhatnagar Eq.4.1 `⟨Sρ⟩→½∫√−g R + Vol_{d−2}(J)`, `...:562–565` | Mathematician | CONFIRMED |
| EGS Eq.12 `Θ_out(r)=(1/r)(1−2M/r)`, `Θ_out(2M)=0`, `derived-md/Towards black-hole horizons...md:223-225` | Physicist | CONFIRMED |
| `op11_spherical_dual_target.md:136-137` `h_M(x)=r/(2M)−1=0` | Physicist | CONFIRMED |
| EGS "no transverse two-surfaces available in 1+1D," `...md:227` | Physicist | CONFIRMED |
| EGS longest-chain/future-cardinality bimodality, sharp transition at horizon, `...md:181-193` | Physicist | CONFIRMED |
| EGS finite-patch caveat, infinite sprinkling required, `...md:173-179` | Physicist | CONFIRMED |
| Physicist's formula `(□−R/2)φ → −R` "estimates the Ricci scalar" | Physicist | UNCONFIRMED |
| "2D vacuum Schwarzschild exterior has R_μν=0 and R=0" (licenses the "definitive null" framing) | Mathematician + Physicist | UNCONFIRMED |
| `comite_decision_002...md:225-236,356-361` "R=0 ⇒ Bₖφ→□φ, no curvature signal" / "definitive null" | Mathematician + Physicist | UNCONFIRMED (repo-internal, and its physics premise is contradicted by the primary source) |
| Correct BD notation is `N_i`/`N_m`, not `C_k` (`comite_decision_023...md:341-364`) | Chair/dossier | CONFIRMED |

- Notes: BD2010 itself (`...:108-112`) specifies the estimator with test field `φ=−2`, not a
  generic φ, and states `Bₖ(−2)` "is close to the scalar curvature of the approximating
  spacetime" — i.e. `(□−½R)(−2) = R` (since `□(const)=0`), not `−R`. The physicist brief's
  schematic `(□−R/2)φ → −R` inverts this sign and is not literally supported by BD2010 Eq.12 or
  by Bhatnagar's equivalent limit. A paraphrase error, not fatal, but should not be cited as
  BD2010's literal result.
  **More importantly: the "2D vacuum Schwarzschild has R=0" premise, which both the
  mathematician's and physicist's "definitive null" arguments depend on (via `comite_decision_
  002:228,356-361`), is directly contradicted by the primary source both briefs otherwise rely
  on.** EGS state explicitly, of the exact (t,r)-Schwarzschild toy metric used in this repository
  (`ds²=−(1−r_S/r)dt²+(1−r_S/r)⁻¹dr²`, their Eq.5, `derived-md/Towards black-hole horizons...
  md:130-135`): "we test it for the first time in a spacetime with **nonvanishing curvature**,
  namely the (1+1) dimensional toy model of Schwarzschild spacetime" (`...md:266`). A direct
  computation confirms this: for `ds²=−f(r)dt²+f(r)⁻¹dr²`, the 2D Ricci scalar is `R=−f''(r)`;
  with `f=1−r_S/r`, `R=2r_S/r³ ≠ 0` everywhere outside `r=0`. The repo-internal claim conflates
  "the Einstein tensor vanishes identically in 2D" (a trivial topological identity true for *any*
  2D metric) with "R=0" — these are not the same statement, and the biblioteca EGS source itself
  says the opposite of R=0 for this metric. Both wave-1 briefs' "definitive null / no curvature
  signal" argument therefore rests on an UNCONFIRMED, literature-contradicted premise — flagged to
  the chair as a load-bearing physics error, not merely an unverified citation. See §8 for how
  this changes (and does not change) the synthesis.

## 8. Synthesis

**Correction to the wave-1 record (must be read before the recommendation below).** The literature
verifier found that the "R=0 in 1+1D vacuum Schwarzschild ⇒ no curvature signal / definitive
null" premise — inherited from `comite_decision_002` and repeated by both the wave-1 mathematician
and physicist — is **false for the actual toy metric this repository's diagnostics are built
around**. EGS state their (t,r)-Schwarzschild toy model has "nonvanishing curvature," and the
literature verifier's direct computation gives `R(r) = 2r_S/r³ ≠ 0`. The premise conflated "the 2D
Einstein tensor vanishes identically" (a content-free topological fact true of every 2D metric)
with "the 2D Ricci scalar vanishes" (false here). **This is corrected, not merely footnoted, for
any future session that reuses this reasoning — `comite_decision_002`'s "definitive null" holding
for the BD curvature-field angle should be treated as unsound on its stated grounds.**

This correction does **not** rescue the candidate, because the physicist's independent, still-
valid point survives on its own: `R(r)=2r_S/r³` is a smooth, monotonically-decreasing function of
`r` with **no zero, sign change, or extremum at `r=2M`** — unlike `Θ_out`, which is *defined* by
its sign flip there. A nonzero-but-smooth curvature signal that varies with `r_S` (hence with `M`)
at any fixed `r` is, if anything, a *stronger* argument that the BD scalar is a **mass detector**
(since `R` scales monotonically with `r_S=2M`) rather than a horizon locator — it simply is not
the "no signal at all" argument comité 002 made. The chair adopts the corrected reasoning: the BD
curvature channel has real but non-horizon-specific content, entangled with mass in exactly the
way Q2(c)'s `Σ N_m = |relations|` warning already flagged from the combinatorial side. Two
independent lines (order-theoretic cardinality-dominance and continuum curvature-scales-with-mass)
converge on the same conclusion via different, now both-verified, mechanisms.

**Convergence across all seven roles.** All four wave-1 experts and the falsifier converge on
**(b) devolver para revisión** (the physicist and falsifier hold a conditional path to (c) reject
open if the named fixes are not met); the pre-registration warden's verdict is **BLOCK** with a
named-prior-fix framing, not a channel closure; the literature verifier confirms every load-
bearing citation except the R=0 premise, which is corrected above without changing the bottom
line. No role recommends unconditional admission (outcome a). The committee's answer to the six
questions:

1. **The `f_bench` bar is absolute for that specific object and needs no override to remain in
   force.** It does not, however, extend to every possible PR011-family witness. A genuinely
   different witness `f ≠ f_bench` may proceed under a fresh Route-B provenance chain, but two
   things are non-negotiable, per the logician and falsifier: (i) it must be proved by
   enumeration — not asserted — that the candidate is not an affine/monotone reparametrization of
   `f_bench`/`|relations|` on the frozen n=4 family (op13 §5's "affine relabel is not a new
   object" rule), and (ii) any enablement of a substitute witness must be recorded as an
   **explicit new committee decision**, never inferred from this brief or from narrative
   reinterpretation of decision 034.
2. **The BD 2D action as literally specified (`N0,N1,N2`) cannot be admitted as written** — it is
   a mislabelled 3-term truncation of the true 4-term formula (`N0,N1,N2,N3`, coefficients
   `1,−2,4,−2`), and the truncation forfeits the very continuum-limit provenance that (a) claims.
   (c) is true as a disclosure but does not discharge `ADAPTIVE_SELECTION_UNCONTROLLED` (op13
   requires a *demonstrated uniform bound*, not disclosure). (d) is asserted, not proved, and
   repeats the decision-034 "D1 fallacy" pattern (a structural property claimed without checking
   the decidable finite fact). None of (a)-(d) is ready for freeze as worded.
3. **No convention is frozen or freezable today.** The mathematician's proposal — enumerate the
   exact theoretical range `[S_min,S_max]` over all n=4 posets and normalize `x↦(S−S_min)/
   (S_max−S_min)`, no clipping — is the only principled construction on record and should be
   adopted verbatim *if and when* a Route-B prereg is drafted, but it has not been enumerated or
   committed to a document yet.
4. **No kill-test threshold is frozen.** The falsifier's finding is decisive context: the PR011
   family's own certified near-blind regime bounds any witness's mean-gap to ≲0.0092, while
   OP-2.1-scale Hoeffding radii (~0.11 at m=200) are ~12× larger — so *any* kill-test threshold
   chosen without first checking feasible `(m,α)` risks either killing every witness a priori or
   being vacuous. This must be resolved before a threshold is named, independent of which witness
   is chosen.
5. **A mass-vs-shape control is definable pre-scoring** — two independent, complementary
   operationalizations are already on record: the mathematician's algebraic residual-after-
   regressing-out-`(N,|relations|)`, and the physicist's geometric exterior-only-vs-straddling
   patch control (itself flagged by the falsifier as **not constructible inside the PR011 family
   as currently parametrized**, since that family carries no `r=2M`/patch-placement structure — a
   family-design gap, not an impossibility). Both should be required, not either/or, in any future
   Route-B prereg; failing to define at least the algebraic one before scoring would itself be a
   design defect.
6. **No genuine horizon-specific, 3+1D-transferable property survives in this candidate.** The
   only defensible transferable role — corrected per §8 above — is as a generic cardinality/
   curvature negative-control baseline that any true horizon candidate must outperform on matched
   horizon vs non-horizon cuts. The terms "proxy de horizonte" and "localizador" are not licensed
   by anything found this session and must not appear in any future document describing this
   candidate; the maximum admissible terminal ceiling is `REFERENCE_WITNESS_SEPARATION_ONLY`,
   explicitly framed as a null-check/baseline artifact.

**Recommended direction.** Return the candidate for revision (plan output **b**), not admit as
Route-B-ready (a) and not close the channel permanently (c) — a future BD-family candidate is not
structurally excluded, but the one presented in this session is not the object it claims to be and
several of its required preconditions (seed band, uniform bound, enumerated non-collinearity
proof, kill-test feasibility check, family-design gap for the geometric control) do not yet exist
in writing.

**Ranked alternatives.** (1) Return for revision with the named fixes below — recommended,
converges all seven roles. (2) Reject and close the channel permanently — rejected: no role
argued the channel is structurally dead, only that this specific candidate as worded is not
ready; the physicist's own conditional-admit path and the falsifier's cheap decisive test both
presuppose the channel stays open pending that test. (3) Admit as-is for Route-B drafting —
rejected: contradicted by the warden's BLOCK and by every wave-1 role.

**Open disagreements (surfaced, not hidden).**
- **D1 — severity of the R=0 correction.** The literature verifier treats it as a load-bearing
  physics error requiring correction of the wave-1 reasoning chain, not just a citation fix. The
  falsifier agrees it must be corrected but notes it does not change the bottom line. The chair
  adopts both: corrected in §8, verdict unchanged.
- **D2 — is the exterior-vs-straddling geometric mass-vs-shape control (physicist) actually
  constructible inside PR011?** The falsifier says no as currently parametrized (PR011 carries no
  `r=2M`/patch-placement structure); the physicist proposed it without flagging that gap. The
  chair records this as an open family-design question for any future Route-B prereg, not
  resolved here.
- **D3 — governing-document status of `next_observable_candidate_matrix.md`.** Three roles
  (reproducibility engineer, logician, falsifier) flag that its §6 sequencing rule (Candidate B
  opens only after Candidate A is killed/survived) is, on its literal terms, unsatisfied by
  PR009/PR010's twin inconclusive closures, and that no committee decision records the matrix as
  superseded by the newer operational plan. This is not resolved in this session — it requires
  either an explicit statement that the matrix is superseded, or treating the sequencing
  precondition as still binding and therefore itself part of what must be fixed before any BD-
  family candidate (which is not even literally "Candidate B" as scoped — it is a raw scalar, not
  Candidate B's cut/partition contrast) can proceed.

## 9. Next-step spec

**This session takes no action beyond writing this acta.** The following is a sequenced menu for
the user to authorize in a future session — none of it is executed here.

**Reversible steps (each is read-only or dev-only, git-revertable, touches no seal, no validation
seed, no PR012/PR013/OP-2.1/OP-2.3; may be run only if and when the user separately authorizes
that session):**

1. **The falsifier's minimal falsification test.** Enumerate `P_4(0.95)` and `P_4(1.05)` via the
   already-frozen `dev/pr011_tv_certification_enumeration.py`; compute `(|relations|, S_BD)` with
   the full 4-term formula for every unlabeled poset in the support; check whether `S_BD` is a
   function of `|relations|` on that support (settles Q2(c)/(d) and Q1's non-collinearity
   precondition), and whether the `|relations|`-conditional residual TV is nonzero between the two
   laws (settles the algebraic mass-vs-shape kill test, Q4/Q5). Costs seconds, consumes no seeds,
   touches no sealed path. Must be run and reported by someone other than the candidate's
   proposer.
2. **Feasibility check of the kill-test threshold** against the PR011 family's certified near-
   blind bound (`TV ≤ ~0.0092`) and OP-2.1-scale Hoeffding radii, before any threshold is named.
3. **A written erratum note** (wherever the project records such things — not this file) that
   `comite_decision_002`'s "definitive null" finding for the BD curvature-field angle rests on an
   incorrect R=0 premise, per §7/§8 above, so future sessions do not re-inherit the error.
4. **A written resolution of D3** — either an explicit committee/PI statement that
   `next_observable_candidate_matrix.md` is superseded by `docs/plan_operativo_15_julio_2026.md`,
   or an acknowledgment that its §6 sequencing precondition remains binding and unmet.

**Committing steps (each requires its own explicit PI authorization and, per decision 034 §9's
precedent, its own committee decision — none is authorized by this brief):**

- Drafting a Route-B dev preregistration for any BD-family (or other) OP-2.2 witness.
- Minting and freezing a new OP-2.2 dev seed band.
- Any subsequent opening of OP-2.2 witness development as such (decision 034 already reserves
  this; this session does not open it either).
- Any PR013 proposal.

**Binding rules pre-committed for any future OP-2.2 work (violating any one voids the outcome):**

- The witness must be the true BD 2D action (`N0,N1,N2,N3`, coefficients `1,−2,4,−2`) or must
  drop the Benincasa–Dowker name.
- Non-collinearity with `f_bench = |relations|/6` must be proved by enumeration on the frozen
  n=4 family before freeze, not asserted.
- The `[0,1]` transform must use the enumerated theoretical range; no clipping without express,
  frozen justification.
- The kill-test threshold must be checked against the PR011 family's certified near-blind bound
  before it is named.
- At least the algebraic (regress-out-`N`/`|relations|`) mass-vs-shape control is mandatory; the
  geometric exterior-vs-straddling control requires first closing the PR011 family-design gap the
  falsifier identified (D2).
- Terminal ceiling is `REFERENCE_WITNESS_SEPARATION_ONLY` at most; "proxy de horizonte" and
  "localizador" are forbidden language for this candidate under any outcome.
- Author ≠ sole verifier: an `/auditor` pass (or equivalent independent check) is required before
  any OP-2.2 terminal is recorded, mirroring the OP-2.1 R6 precedent.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off

_(left blank for the user — decision, date, and any overriding notes)_
