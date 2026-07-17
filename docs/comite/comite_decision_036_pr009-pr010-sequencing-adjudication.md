# Comité Decision 036 — pr009-pr010-sequencing-adjudication

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Resolver, y solo esto, la pregunta de secuenciación PR009/PR010 identificada como disagreement D3
en la decisión 035 (`docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md`).

`research_program/work_packages/next_observable_candidate_matrix.md` §6 ("Recommended sequence")
establece: "Open Candidate B only if [Candidate A] is killed or survives with a clearly non-depth
channel." Candidate A (ladder-ensemble effective expansion) se instanció como PR009, que cerró con
terminal `FAILED_DATA_CONTRACT`. Su sucesor de diseño, PR010, cerró con terminal
`PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`. Ninguno de los dos alcanzó "killed" ni "survived" en
el sentido literal de la matriz.

Tres preguntas:

1. ¿El terminal `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE` (precedido por
   `PR009_...FAILED_DATA_CONTRACT`) cuenta como cierre operativo suficiente de Candidate A para
   permitir abrir Candidate B, sin que ese cierre se narre como un resultado científico negativo?
   ¿O bien la matriz debe modificarse prospectivamente para admitir explícitamente un tercer
   estado de cierre — "killed, survived, or formally closed as design-infeasible" — antes de que
   Candidate B (o cualquier otro candidato de esa familia, incluida la acción BD) pueda abrirse?
2. Si se requiere enmendar la matriz, ¿quién tiene autoridad para hacerlo y qué forma debe tomar
   la enmienda?
3. ¿Esta resolución habilita automáticamente que el candidato BD-action (o cualquier futuro
   candidato de esa familia) proceda a la revisión documental de la decisión 035 §9, o esa
   habilitación requiere su propia decisión de comité posterior?

Salidas posibles: (a) el cierre PR009/PR010 es suficiente tal cual, la matriz se declara
satisfecha/superada y el canal queda abierto para Candidate B; (b) la matriz requiere enmienda
formal, esta sesión adopta el texto exacto; (c) la secuenciación permanece bloqueada, no se
resuelve esta sesión.

Restricciones de sesión: NO tocar la fórmula BD-action, NO ejecutar la enumeración de la decisión
035, NO abrir PR013, NO tocar OP-2.1/PR012/OP-2.3, NO modificar ningún archivo salvo esta acta.

## 2. Verified state

Facts checked **this session** (2026-07-17) by the chair:

- `make verify-seal` → `thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` — matches the frozen seal,
  undisturbed throughout the session.
- `git rev-parse HEAD` → `a5572640b229737890c69723ee84fe7f6024b300`; `git status --porcelain` →
  clean worktree.
- Recent commits: `a557264` comite: OP-2.2 BD-action witness candidate adjudication (decision
  035); `67cf15a` op21: record OP-2.1 terminal (R6); earlier `cd3ef51` op21 opening (decision
  034).
- `research_program/work_packages/next_observable_candidate_matrix.md:1-5` — header
  `STATUS: DESIGN_TRIAGE_ONLY / DATE: 2026-07-11 / AUTHORIZATION:
  CHEAP_KILL_TESTS_ONLY_AFTER_PREREGISTRATION`. Not `FROZEN`, not sealed — the repo's own
  vocabulary convention (compare `dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md:4`
  `DESIGN_STATUS: FROZEN_FOR_AUDIT`) places this document in the revisable-planning tier, not the
  frozen/preregistration tier.
- `research_program/work_packages/next_observable_candidate_matrix.md:148-155` — §6 "Recommended
  sequence," step 5: "Open Candidate B only if A is killed or survives with a clearly non-depth
  channel."
- `dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_CLOSURE_DECISION.md` (full text) — `STATUS:
  CLOSED`, `TERMINAL_LABEL: FAILED_DATA_CONTRACT`, `SCOPE: CONTRACT_CLOSURE /
  NO_SCIENTIFIC_TERMINAL / NO_RERUN`. "PR009 is neither a dead observable nor a surviving
  observable... none of the preregistered scientific terminal labels applies" (`:18-21`). "This
  closure does not establish: absence or presence of horizon sensitivity; failure or survival of
  the effective-expansion observable; a null or negative physical result..." (`:52-57`). "PR009 is
  closed without amendment," forbidden-repairs list (`:64-74`).
- `dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md` (full text) — `DESIGN_STATUS: FROZEN_FOR_AUDIT`,
  `RELATION_TO_PR009: SUCCESSOR_WITHOUT_DATA_REUSE`. Terminal `PR010_DESIGN_INFEASIBLE_
  REFERENCE_COVERAGE` "forbids a confirmatory preregistration for **this PR010 design**...
  Development may not be extended, repeated, or supplemented to reverse it" (`:145-152`). "Makes
  no claim about... horizon sensitivity... The PR009 terminal remains exactly
  `FAILED_DATA_CONTRACT`" (`:206-210`). Reserved, unconsumed confirmatory seed bands
  `REFERENCE_SEEDS=1102000..1102023` / `EVALUATION_SEEDS=1103000..1103011` (`:154-167`).
- `dev/score_pr009_effective_expansion.py:42-47` — the scorer defines **four** scientific labels,
  not two: `INCONCLUSIVE_COVERAGE`, `KILLED_GENERIC_OR_BASELINE_SIGNAL`,
  `KILLED_NO_SIGNED_EXPANSION`, `SURVIVED_CHEAP_KILL_TEST`. None ever fired — chair-verified this
  session via `grep -rlE "SURVIVED_CHEAP_KILL_TEST|KILLED_NO_SIGNED_EXPANSION|
  KILLED_GENERIC_OR_BASELINE_SIGNAL|INCONCLUSIVE_COVERAGE"` (falsifier, independently re-run):
  hits only the preregistration, the scorer source, and its test — no scientific verdict on
  Candidate A exists anywhere in the repository.
- No PR011-of-Candidate-A (a further redesign attempt) exists — chair `find` this session:
  Candidate A's design chain is stalled after PR010, not proven dead.
- `research_program/work_packages/README.md:13-18` — still calls the matrix the "Active design
  front," text unmodified since 2026-07-11, predates both closures.
- `docs/plan_operativo_15_julio_2026.md` — chair grep this session: zero mentions of "PR009",
  "PR010", or "candidate_matrix" anywhere. `:87-88` and `:573-579` state the general precedence
  principle: contract/leakage/resource/abstain terminals "tienen precedencia sobre cualquier
  terminal científico."
- `research_program/work_packages/op13_positive_evidence_protocol.md:194-202` — a structurally
  analogous, though op13-scoped, precedence chain placing contract/manifest-failure terminals
  strictly above scientific-outcome terminals.
- `docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md` §8 disagreement D3 —
  the source of this session's question; also records (§8, §7:221-224,592) that the BD-action
  candidate under discussion there is "not even literally Candidate B" — a raw single-poset
  scalar, structurally distinct from Candidate B's cut/partition contrast `I_order(X:Y)`.

## 3. Dossier

- `research_program/work_packages/next_observable_candidate_matrix.md` (full document)
- `research_program/work_packages/README.md`
- `dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_CLOSURE_DECISION.md` (full document)
- `dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md` (full document)
- `dev/score_pr009_effective_expansion.py:42-47`
- `docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md` (full document)
- `research_program/work_packages/op13_positive_evidence_protocol.md:190-208`
- `docs/plan_operativo_15_julio_2026.md:8-12,52-62,87-88,573-579`
- `CLAUDE.md`

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

**1.** Closure docs are frozen/immutable (PR009 `STATUS: CLOSED`, "closed without amendment";
PR010 `DESIGN_STATUS: FROZEN_FOR_AUDIT`). A committee decision can layer a sequencing
interpretation on top without editing either file — the freeze-respecting move. Neither closure is
a scientific/negative result — both explicitly forbid that narration — so the matrix's own §7
stop-rule "a negative result closes the candidate" does **not** apply.

**2.** The design-infeasible terminal is a real, auditable, reproducible artifact (csv + sha256 +
deterministic Clopper-Pearson rule) but is **conditional** — scoped to one frozen design
(`depth_k={3,4,5}`), forbids only *this* PR010 design from reversing, does not foreclose a
differently-designed successor. No such successor exists; Candidate A is stalled, not proven dead.
**The matrix's literal §6 precondition is satisfied by neither closure.** Reserved seed bands are
unconsumed but their reuse by a future redesign is ambiguous — flag `[UNVERIFIED]`, don't assume
reuse is permitted.

**3.** The matrix is `DESIGN_TRIAGE_ONLY`, not sealed/frozen — amending it doesn't implicate
`NO_THRESHOLD_LOOSENING`/`RESPECT_SEAL_FREEZE`. But it has zero version discipline; any amendment
should go through a committee decision as the audit anchor, with a dated revision note, and the
stale README re-synced. Two parallel governance surfaces (matrix vs. `plan_operativo_15_
julio_2026.md`) exist with no link between them — this is why D3 is unresolved.

**Auto-enablement (Q3): no.** The repo's consistent pattern is explicit, separate authorization
gates. Treating a matrix-sequencing resolution as an implicit open for the next candidate would be
scope creep.

**Recommendation: (b)-leaning** — amend with a third closure state via committee decision + dated
pointer + synced README + explicit statement of the matrix's relation to the newer plan; (a)
defensible only if the acta simultaneously records neither closure is scientific/negative AND
marks the matrix formally superseded with a pointer — otherwise it leaves the same
untraceable-authority gap D3 names.

### Mathematician brief

**Correction to the dossier:** the scorer defines **four** scientific labels, not three —
`INCONCLUSIVE_COVERAGE`, `KILLED_GENERIC_OR_BASELINE_SIGNAL`, `KILLED_NO_SIGNED_EXPANSION`,
`SURVIVED_CHEAP_KILL_TEST` (`dev/score_pr009_effective_expansion.py:42-47`) — the system already
contemplates a scientific non-killed/non-survived outcome (`INCONCLUSIVE_COVERAGE`), distinct from
the contract-gate (`FAILED_DATA_CONTRACT`) that actually fired. PR009 stopped at tier (i)
data-contract, never reached tier (ii) scorer.

**1.** Three different logical types: *killed/survives* are **a-posteriori values in the range of
the confirmatory scoring function** `f: EvaluationData → {KILLED_*, SURVIVED_*,
INCONCLUSIVE_COVERAGE}` — they exist only if `f` was applied to real evaluation data.
`FAILED_DATA_CONTRACT` is **not a value of `f` at all** — a domain guard that fired before `f`
ran; `f` is partial, this is a domain-error, not a range element. `PR010_DESIGN_INFEASIBLE_
REFERENCE_COVERAGE` is **one level higher still**: an a-priori constructive-impossibility
statement about whether a valid input to `f` can even be built, touching zero channel content
(schema has no sign/contrast/effect-size fields, and PR010 "must not... compute or inspect horizon
zones, radii, contrasts, signs, effect sizes, or terminal statistics"). Different quantifier
structure entirely — not comparable elements of one ordered outcome set.

**2.** Is the precondition satisfied literally? **No**, for two independent reasons: (i) category
mismatch — `{killed,survived}` doesn't contain either closure terminal; (ii) the "clearly
non-depth channel" qualifier is a **scientific-content condition** presupposing the kill test
produced channel-discriminating information — a design that emitted zero channel data cannot
satisfy this even in principle, architecturally. **Output (a) is not supportable on the text as
written** — endorsing it would be an abstain→PASS coercion.

**3.** A genuine but *weaker* argument exists: §1's meta-predicate "admits a cheap test that can
kill it" may itself be refuted one level above the kill test (constructibility/admissibility gate)
— but this is a **different proposition** from "killed" (about the observable's behavior on
data). Relabeling apparatus-infeasibility as the scientific `KILLED_*` terminal is a **type error**
smuggling a claim about nature out of a claim about measurement design. The honest sentence:
"Candidate A's cheap-test channel is terminally and irreversibly closed at the constructibility
level, while producing no scientific verdict on the observable."

**Bottom line: (b)** — a formal amendment adding an explicitly *typed* third disjunct
(administrative/closure state) carrying an anti-leakage clause that it conveys **no** channel
information and licenses **no** inference about the observable; not threshold-loosening since no
frozen numeric threshold moves — it completes an under-specified state space.

**(3): No auto-enablement** — two independent gates remain (the §6 sequencing slot; the identity
question that the BD-action object is "not even literally Candidate B"). `[UNVERIFIED]`: notes
that IF the matrix is declared superseded, §6 ceases to bind and the whole precondition question
is moot — cleaner than amending a doc simultaneously treated as dead.

### Mathematical logic brief

**1.** The matrix is explicitly **lower-tier** (`STATUS: DESIGN_TRIAGE_ONLY`, not `FROZEN`/sealed)
by the repo's own vocabulary convention — belongs to the class of revisable planning documents,
**not** frozen preregistrations governed by `RESPECT_SEAL_FREEZE`. Narrowly retiring/amending its
§6 gate is not threshold-loosening of a frozen object.

**2.** "No decision records supersession" ⇒ "still binding" is a **non-sequitur** (argument from
silence). Absence of an explicit supersession record is evidence of *incomplete paperwork*, not
*continued force*. The matrix carries no perpetuity/no-repair clause analogous to genuinely frozen
artifacts elsewhere. The correct logical state is **undetermined pending an explicit decision** —
not resolvable by default reasoning in either direction.

**3.** A never-satisfiable gate is itself "decoration" **in reverse**. `CLAUDE.md`'s canonical
failure mode is a rule too weak to ever gate; the dual failure is a rule that can **never** be
satisfied and thus never issues a real pass. Both PR009 and PR010 forbid reopening, and no third
attempt exists — reading §6 as still-binding-until-killed-or-survived makes it a **permanent veto
with no principled discharge condition**, a real freeze-discipline hazard symmetric to (but
opposite from) "laundering away an inconvenient rule."

**4. Load-bearing formal point.** §6 step 5 is a two-way disjunction over **scientific**
outcomes (`killed ∨ survives`). The repo's own convention elsewhere (op13's terminal-precedence
chain; `plan_operativo_15_julio_2026.md:87-88,573-579`) places contract/manifest-failure
terminals in a precedence **tier strictly above** scientific-outcome terminals — **not a third
value on the same axis**, but a distinct pre-empting tier with its own defined downstream
handling. PR009/PR010 landed exactly in that higher tier. §6, naming only the two scientific-axis
values, is **silent on the case that actually occurred** — incompleteness, not an implicit
prohibition. Applying the rule to a case outside its domain and reading the omission as forbidding
is a quantifier-scope error.

**Proposed amendment text** (as a starting draft, refined below by the falsifier and physicist):
"Open Candidate B only if A is killed, survives with a clearly non-depth channel, **or A's
implementation track is formally closed at a contract/design-feasibility tier that pre-empts the
scientific outcome (per the plan operativo terminal-precedence convention), with no scientific
killed/survived claim implied**."

**Bearing on the questions:** Q1 — the closures are *operationally* sufficient in the sense of
pre-empting the scientific axis (opening a successor need not be narrated as negative science),
but §6 *as literally written* is inapplicable/incomplete, not satisfied — outcome (a) overstates
by claiming "satisfied/surpassed." Q2 — amendment is within committee-recommendation + PI-decision
competence; no seal touched; scope to §6 only. Q3 — **no**: decision 035 §9 routes BD-family work
through its own separate committing gate regardless, and the BD candidate is "not even literally
Candidate B" — coupling the two would repeat decision-034's D2 fallacy ("the instruction alone
authorizes nothing"). **Recommends (b)**; notes (c) is "logically available but entrenches a veto
with no discharge condition, should be chosen only deliberately, not by default silence."

### Physicist brief

**What §6 is for, physically:** an **engineering-risk allocator**, not a physics-content rule. A
and B share the same physical-link score (3), but A ranks #1 (15/18) for being better-engineered
(order-only feasibility 2, leakage 2, cheap falsifiability 3) vs. B's worse engineering
(feasibility 1, leakage 1 — lowest in the table, falsifiability 2). The rule exists to prevent
spending limited attention/compute on the noisier, more dimension-dependent, higher-leakage
channel while the cleaner channel is untested.

**Is design-infeasible = killed/survived, physically? No.** Killed/survived are statements about
**horizon physics** (the proxy is an artifact vs. matches the preregistered control / shows the
preregistered sign ordering). PR009/PR010 reached **neither** — both closures explicitly forbid
any horizon-sensitivity inference. Root cause confirmed: an insufficient rate of
Minkowski/reference null-ladder continuations reaching evaluable depth under the frozen
sprinkling/beam budget — an **apparatus/coverage problem**, not a claim about the sign or
magnitude of any expansion effect. The horizon-physics question A was built to answer remains
**fully open**.

**Does this change the risk calculus? It argues *against* reading §6 as satisfied, not for it.**
The one affirmative pathway is "survives with a clearly **non-depth** channel" — what actually
happened is the opposite extreme: A did not survive, and its failure was **maximally
depth-entangled**. The engineering hazard §6 guards (burning budget on an unpopulatable channel) is
**not retired** by switching to B — if anything elevated: B's cut-contrast needs its **own**
matched-cut population (Rindler/non-horizon simulations) at the same sprinkling intensity that
just defeated A, and B carries the lower feasibility score and the worst leakage risk in the
table, plus its own untouched risks ("the intrinsic-partition problem may be as hard as horizon
localization itself," "BDG action estimators are noisy and dimension-dependent"). **Opening B here
gives it zero physical uplift** — A is untested-and-currently-unrunnable, not "the next-best
signal is now available."

**Reading on the three outputs (physics grounds):**
- **(a) reject** — forces the twin closures into a binary they physically are not; either narrates
  A as negative science (forbidden) or pretends the gate's physical purpose (non-depth survival)
  is met when the opposite occurred.
- **(b) physically honest *only with conditions*.** Must (i) record A's horizon-sensitivity
  question as **unresolved, not negative**; (ii) forbid A's infeasibility from counting as **any**
  evidence about B; and (iii) **gate opening B on an explicit feasibility showing that B's own
  reference-coverage/interval-abundance demands are met under the same budget that just defeated
  A** — otherwise the amendment defeats the rule's physical rationale rather than serving it. Must
  not become a lever to retune A's depth budget either (matrix's own stop rule).
- **(c) physically defensible** if the committee is unwilling to state the feasibility condition
  now.

**Question 3 — no, and this may make the sequencing question moot for the BD candidate anyway.**
Decision 035 already found the BD scalar is a raw single-poset functional, **not** Candidate B's
`I_order(X:Y)` cut-contrast — the cut-contrast is engineered specifically to *cancel* the
extensive/cardinality-dominant bulk term and isolate a differenced boundary contribution, which is
the entire reason it could be horizon-specific. A raw scalar performs no such cancellation and
carries the cardinality-dominance/mass-detector risk profile already flagged in decision 035. **The
sequencing question and the BD-scalar question are physically decoupled.**

## 5. Falsifier attack

### Falsifier attack

- **Concrete failure modes:**
  1. **Output (a)'s own wording is falsifiable on the text.** Neither PR009's nor PR010's terminal
     is in `{killed, survived}`. Declaring the matrix "satisfecha/superada" is a false statement
     of record, not an interpretation.
  2. **Option (b) is structurally post-hoc rule-editing.** The gate is being amended only after,
     and only because, its literal application blocks the desired next step — exactly what
     `CLAUDE.md:14`'s "guardrail that cannot fail" warns against in both directions. Survivable
     only if the amendment is explicitly typed administrative, scoped to §6 step 5 alone, and
     carries the mathematician's no-inference clause.
  3. **The "declare the whole matrix superseded" escape route is a trap.** It discards §7's stop
     rules ("no post-hoc change of seed, cut, orientation..."; "a negative result closes the
     candidate; it does not authorize retuning the same channel") along with the one inconvenient
     gate — laundering away multiple live protections to escape one.
  4. **The logician's draft amendment, adopted verbatim, is under-specified.** (i) it cites "the
     op13 terminal-precedence convention," but op13's chain is explicitly scoped to op13's own
     terminals — the genuinely general principle lives at `docs/plan_operativo_15_
     julio_2026.md:87-88`, not op13; (ii) it omits the physicist's B-side coverage-feasibility
     precondition, which would open the candidate with the worst feasibility/leakage row in the
     table against the very coverage wall that just defeated the better-engineered candidate;
     (iii) it has no anti-retune-A clause.
  5. **Over-reach on what the closures prove.** PR010 forbids only "a confirmatory
     preregistration for **this PR010 design**." Candidate A is stalled, not dead; any amendment
     saying "A's track is closed" (rather than "A's implementation track under the frozen
     PR009/PR010 designs is closed") overstates the artifact.
  6. **Seed-band smuggling.** The reserved bands `1102000..1102023`/`1103000..1103011` "may not
     be expanded, shortened, replaced, or supplemented." Any acta language implying they become
     available to Candidate B or a redesigned A is an unauthorized seed reassignment.

- **Ground-truth leakage:** The step itself touches no data and no embedding. Falsifier-verified
  directly: `grep -rlE "SURVIVED_CHEAP_KILL_TEST|KILLED_NO_SIGNED_EXPANSION|
  KILLED_GENERIC_OR_BASELINE_SIGNAL|INCONCLUSIVE_COVERAGE"` over the repo hits only the
  preregistration, the scorer source, and its test — **no scientific label ever fired anywhere**,
  so there is no channel content to leak. Two residual paths: (i) *narrative laundering* — any
  acta sentence implying a sign/magnitude fact about `theta_eff` is forbidden by PR009's own
  `NO_SCIENTIFIC_TERMINAL` scope; (ii) *design-side leakage* — PR010's development coverage
  statistics are now known from consumed dev seeds; if they shape Candidate B's cut/reference
  construction undeclared, consumed-development information enters a new design silently. Any
  future B prereg must declare dependence on PR009/PR010 dev artifacts.

- **Freeze violations:** (a) is de-facto gate loosening — an unmet gate declared passed. (b) does
  not literally trip `NO_THRESHOLD_LOOSENING` (matrix is `DESIGN_TRIAGE_ONLY`, no frozen numeric
  values move) but is a post-outcome rule change and must be firewalled from ever licensing a
  retune of A's depth/budget or a PR009 re-run. Seed-band hazard as above. The "declare the whole
  matrix superseded" route violates freeze discipline in spirit by voiding §7 wholesale.

- **Verdict coercion:** (a) is the coercion — the scorer's own label set already contains a
  non-killed/non-survived scientific state (`INCONCLUSIVE_COVERAGE`) and even *that* never fired;
  the true state is "scientific axis pre-empted at a higher-precedence tier"
  (`plan_operativo_15_julio_2026.md:87-88`). The acta must not narrate A as "effectively killed"
  *nor* as "still promising"; if (b) is adopted, the record must say "gate amended," never "gate
  passed."

- **Premature / over-broad claims:** This is pure governance — no statement about horizon
  localization, metric, asymptotics, or 3+1D is licensed. Two specific traps: (i) leaning on
  Candidate B's "3+1D path: 3" score as physics — the matrix says scores "are design judgements
  from the literature review, not experimental results"; (ii) letting the D3 resolution double as
  BD-action review authorization — the acta must state Q3 = **no**, explicitly.

- **Independent-falsification gate:** Partially satisfied. Four independent wave-1 roles
  converged on (b), and the mathematician independently falsified the chair's own dossier (which
  said three scorer labels; the file has four) — proof the dossier framing is not authoritative
  and the acta must cite files, not the dossier. But the amendment *text* has a single author
  (the logician); adopting it verbatim would make its author its sole verifier. Gate closes only
  if the adopted text demonstrably merges the mathematician's typed/no-inference clause and the
  physicist's B-side feasibility precondition — done in §9 below — and the resulting acta is
  flagged for a subsequent `/auditor` pass if and when the matrix is actually edited.

- **Minimal falsification test:** Already executed this session (read-only):
  `grep -rlE "SURVIVED_CHEAP_KILL_TEST|KILLED_NO_SIGNED_EXPANSION|
  KILLED_GENERIC_OR_BASELINE_SIGNAL|INCONCLUSIVE_COVERAGE" /home/ignac/nachocausal` → hits only
  `dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_PREREGISTRATION.md`,
  `dev/score_pr009_effective_expansion.py`, `tests/test_pr009_effective_expansion_scorer.py`.
  This proves no scientific verdict on Candidate A exists anywhere in the repository; therefore
  any acta or amendment sentence asserting or implying "killed," "survived," or "matriz
  satisfecha" is falsified by the repo itself. **Post-adoption invariant**: if/when the matrix is
  edited, re-run this grep plus `grep -nE "satisfecha|superada|killed|survived" <new text>` and
  require every hit to occur inside an explicit negation or quotation.

## 6. Pre-registration verdict

### Pre-registration verdict

- Verdict: **PASS** — but only for a resolution shaped as amendment-path (b), i.e. typed third
  disjunct + the physicist's Candidate-B feasibility precondition + the mathematician's
  anti-inference clause. Any resolution that reads PR009/PR010's closures as literally satisfying
  §6 without amendment (output (a) as literally worded) is **BLOCKED** as scoped; that specific
  move must not be adopted this session.
- Freeze status: The matrix's precondition text is frozen-in-place but the matrix itself carries
  `STATUS: DESIGN_TRIAGE_ONLY`, not `FROZEN`/sealed — per the repo's own vocabulary tier, it is
  amendable by committee decision without implicating `RESPECT_SEAL_FREEZE`. PR009's closure text
  is explicit that "PR009 is neither a dead observable nor a surviving observable" and "no
  scientific terminal result was produced." PR010's `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`
  "forbids a confirmatory preregistration for this PR010 design" only — design-scoped, not a claim
  about the observable. Neither closure literally instantiates "killed" or "survived." So: no
  threshold for *this* step is being loosened or newly frozen — this session only proposes to
  record an interpretive/typing decision about an unmet precondition.
- Seal integrity: Not implicated. `make verify-seal` matches; this session runs no code, touches
  no `nachocausal/thresholds.py`. Undisturbed by a documentary acta.
- Seed discipline: No seed of any kind is drawn, consumed, or referenced by this resolution.
  PR009's original bands are exhausted by contract failure (no reuse permitted). PR010's
  `REFERENCE_SEEDS`/`EVALUATION_SEEDS` remain reserved-but-unconsumed; this session must not
  authorize or imply their use, and does not.
- Reporting rule: Any resolution this session adopts must itself state, in the acta, that neither
  PR009 nor PR010 is a PASS/FAIL/scientific result and must not be narrated as one. Any drafted
  amendment text must carry an anti-leakage clause conveying zero channel information, matching
  the repo-wide rule that PASS/FAIL/INCONCLUSIVE are reported alike and never coerced.
- Forbidden moves present?
  - **Post-hoc tuning / threshold loosening**: absent, provided the amendment adds a new typed
    disjunct rather than relaxing the existing killed/survived disjunction's content, and the
    physicist's B-feasibility gate is included as a *net-stricter* addition, not a loosening.
    Omitting that gate would let a design-infeasible closure open the weaker-engineered,
    higher-leakage-risk candidate with zero uplift in physical justification — that omission is
    the freeze-unsafe choice.
  - **Ground-truth leakage**: absent — no PR009 internal values are read or reused; this
    resolution deals only in already-public terminal labels.
  - **Re-run after peeking**: absent — no re-run is proposed or authorized; both closures forbid
    it explicitly.
  - **Reconstruction / negative-result over-claim**: the live hazard. Reading the twin closures as
    "matrix satisfied, Candidate A effectively killed, channel open" (output (a) verbatim) is a
    type error — conflating a domain-guard/contract failure and an a-priori design-infeasibility
    terminal with an a-posteriori scientific killed/survived outcome — and would coerce an abstain
    into an implicit PASS for §6's purposes. That move is **BLOCKED**.
  - **§9 auto-enablement**: BLOCKED by design — decision 035 §9 already requires its own explicit
    PI authorization plus its own committee decision for any subsequent OP-2.2/BD-family step, and
    this session's own restrictions forbid touching BD-action, OP-2.1/PR012/OP-2.3, and PR013.
    Resolving D3's sequencing question therefore does **not**, and must not, automatically clear
    §9's BD-action documentary review — unanimous across all four wave-1 briefs on Q3 = No.
- Reasons:
  - `next_observable_candidate_matrix.md:3` (`DESIGN_TRIAGE_ONLY`) plus `:154` (§6 precondition)
    show the precondition is real but sits in a non-sealed, triage-tier document — amendable via
    committee decision, not via silent narrative reinterpretation.
  - `dev/PR009_..._CLOSURE_DECISION.md:15-21,33-40` — explicit, self-declared non-scientific
    terminal; forecloses reading PR009 as "killed."
  - `dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md:145-152` — infeasibility terminal is
    design-scoped ("for this PR010 design"), not observable-scoped; forecloses reading PR010 as
    "killed" or "survived" for Candidate A as such.
  - `dev/score_pr009_effective_expansion.py:42-47` — four-label scientific taxonomy that never
    fired; confirms neither closure produced a scientific-range value.
  - `docs/comite/comite_decision_035_...md` §8 D3 — already on record as unresolved and gated
    behind either an explicit supersession statement or an acknowledgment that §6 remains
    binding; §9 next-steps explicitly require separate authorization for anything past the acta.
  - The physicist's engineering-risk-allocator reading of the comparative-scores table is the
    load-bearing reason a Candidate-B feasibility precondition, not its absence, is the
    freeze-consistent supplement to any amendment — additive rigor, not threshold loosening.
  - No file other than the acta may be touched this session; the amendment text can be *proposed*
    in the acta for a future, separately authorized edit to the matrix, not silently applied now.

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| `dev/score_pr009_effective_expansion.py:42-47` — four scientific labels incl. `INCONCLUSIVE_COVERAGE` | Mathematician | CONFIRMED |
| `research_program/work_packages/op13_positive_evidence_protocol.md:194-202` — precedence chain, contract/manifest-failure terminals above scientific-outcome terminals | Logician | CONFIRMED |
| `docs/plan_operativo_15_julio_2026.md:87-88` — precedence principle, exact quote | Logician | CONFIRMED |
| `docs/plan_operativo_15_julio_2026.md:573-579` — "Terminales con precedencia" list | Logician | CONFIRMED |
| `next_observable_candidate_matrix.md:1-5` header — `STATUS: DESIGN_TRIAGE_ONLY`, no freeze/seal token | Logician, Reproducibility engineer | CONFIRMED |
| `dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md:1-6` header — `DESIGN_STATUS: FROZEN_FOR_AUDIT` | Logician, Reproducibility engineer | CONFIRMED |
| `dev/PR009_..._CLOSURE_DECISION.md:3-6` — `STATUS: CLOSED`, `TERMINAL_LABEL: FAILED_DATA_CONTRACT` | Reproducibility engineer | CONFIRMED |
| `PR009…:13-16` — "no inference about horizon sensitivity is permitted" | Physicist | CONFIRMED |
| `PR009…:18-21` — "neither a dead observable nor a surviving observable" | Mathematician | CONFIRMED |
| `PR009…:52-57` — list of what closure does not establish | Reproducibility engineer, Mathematician | CONFIRMED |
| `PR009…:64-74` — "closed without amendment" + forbidden-repairs list | Reproducibility engineer | CONFIRMED |
| `PR009…:78-80` — "a distinct statistical-design boundary" | Physicist | CONFIRMED |
| `PR010…:71-80,91-93` — coverage schema, no sign/contrast/effect-size fields | Mathematician | CONFIRMED |
| `PR010…:104-108` — "resolved permanently," `LIMIT_SCORABLE_DEPTHS` | Mathematician | CONFIRMED |
| `PR010…:116-152` — Clopper-Pearson infeasibility rule and terminal | Physicist, Reproducibility engineer, Mathematician | CONFIRMED |
| `PR010…:154-167` — reserved unconsumed seed bands | Reproducibility engineer | CONFIRMED |
| `PR010…:206-210` — no horizon-sensitivity claim | Reproducibility engineer, Mathematician | CONFIRMED |
| `next_observable_candidate_matrix.md:7-11` — §1 selection rule | Mathematician, Physicist | CONFIRMED |
| `next_observable_candidate_matrix.md:14` — "design judgements... not experimental results" | Logician | CONFIRMED |
| `next_observable_candidate_matrix.md:20-22` — score table values A=[3,2,2,3], B=[3,1,1,2] | Physicist | CONFIRMED |
| `next_observable_candidate_matrix.md:90-118` — Candidate B construction, kill test, risks | Physicist | CONFIRMED |
| `next_observable_candidate_matrix.md:148,154` — §6 heading + step 5 text | Logician, Mathematician, Physicist | CONFIRMED |
| `next_observable_candidate_matrix.md:164` — "a negative result closes the candidate..." | Physicist | CONFIRMED |
| `docs/plan_operativo_15_julio_2026.md:8-12` — "No es preregistro, no congela umbrales..." | Logician | CONFIRMED |
| `docs/comite/comite_decision_035...md:82,175,188,522-523,679-683` — D3 framing | Logician | CONFIRMED |
| `docs/comite/comite_decision_035...md:675-683,221-224,592` — BD scalar not literally Candidate B | Physicist | CONFIRMED |
| `research_program/work_packages/README.md:15-18` — "authorizes no production experiment" | Reproducibility engineer | CONFIRMED (see note — path correction) |
| `git log` commits `f7e3c3a`, `ff98ae1`, `631da6c` | Reproducibility engineer | CONFIRMED |

- Notes: The literature verifier's first pass flagged `README.md:15-18` as UNCONFIRMED because it
  checked the top-level `/README.md`, which does not contain "authorizes no production
  experiment." The chair's own wave-2 dossier compression dropped the directory prefix when
  restating the reproducibility engineer's citation. The correct path is
  `research_program/work_packages/README.md:16` ("It authorizes no production experiment; the
  first permitted next artifact is a preregistration for the cheap kill test..."), verified
  directly by the chair this session (`grep -n "production experiment"
  research_program/work_packages/README.md` → line 16 match). The underlying claim is CONFIRMED
  at the correct path; this is a citation-path bookkeeping error, not a substantive one, and no
  wave-1 argument depends on the wrong path.

## 8. Synthesis

**Convergence.** All four wave-1 experts, the falsifier, and the pre-registration warden converge
on outcome **(b)**: the matrix's §6 precondition, read literally, is not satisfied by PR009/PR010's
twin closures — those closures are a different *kind* of object (contract/design-infeasibility,
pre-empting the scientific axis) from "killed" or "survived" (a-posteriori scientific verdicts that
never fired) — and a narrow, explicitly-typed amendment is the freeze-honest way to let a future
successor candidate open without either (i) falsely narrating Candidate A as scientifically
resolved, or (ii) leaving a permanent, undischargeable veto in place. No role endorsed outcome (a)
as literally worded; outcome (c) was held open by the logician and physicist only as a deliberate,
non-default choice, not a default one.

**The load-bearing formal point** (logician, independently confirmed by the falsifier's citation
correction and the literature verifier): the repo has a standing convention — stated generally at
`docs/plan_operativo_15_julio_2026.md:87-88,573-579` and instantiated narrowly in op13's own
terminal chain — that contract/data-availability/resource-abort terminals sit in a precedence tier
**above** scientific-outcome terminals, not as a third value on the scientific axis but as a
distinct, pre-empting tier with its own defined handling. PR009 (`FAILED_DATA_CONTRACT`) and PR010
(`PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`) both landed in that higher tier. The matrix's §6, by
naming only `{killed, survived}`, is **silent on the case that actually occurred** — an
incompleteness in the original 2026-07-11 triage document, not a deliberate prohibition to be
read as "still binding until literally satisfied."

**The physical rationale (physicist) supplies the missing half of a safe amendment.** §6 exists as
an *engineering-risk allocator* — it ranked Candidate A above Candidate B specifically because A
was better-engineered (higher feasibility, lower leakage risk) while both shared the same
physical-link score. PR009/PR010's infeasibility does not change that physical calculus in
Candidate B's favor: B was never shown to escape the same reference-coverage/matched-cut population
wall that just defeated A, and it carries the table's worst feasibility and leakage scores. An
amendment that merely inserts a third disjunct without also requiring a fresh feasibility showing
for whatever candidate benefits from it would open the door for the *wrong* reason — not because
the risk calculus favors B, but because A's gate mechanically broke. The committee therefore adopts
the physicist's conditional as **part of**, not separate from, the amendment.

**No disagreement survives synthesis on the object-level questions.** The falsifier's refinements
(correct the op13-vs-plan_operativo citation; add the anti-retune-A clause; scope "A's track" to
"A's implementation track under the frozen PR009/PR010 designs," not "Candidate A" simpliciter) are
incorporated into the final text below without contradicting any wave-1 role. The warden's
PASS-only-for-(b)-shaped-resolution verdict and the falsifier's BLOCKED reading of bare (a) agree.

**Recommended direction: outcome (b).** Adopt, as this session's product, the exact amendment text
below — proposed for a **future, separately-requested** edit to
`next_observable_candidate_matrix.md` §6 (this session modifies no file but this acta, per its own
restrictions). The amendment:

> 5. Open Candidate B only if A is killed, survives with a clearly non-depth channel, **or A's
> implementation track — across all attempted designs to date (PR009, PR010) — is formally closed
> at a contract/design-feasibility precedence tier that pre-empts the scientific killed/survived
> axis** (per the precedence convention of `docs/plan_operativo_15_julio_2026.md:87-88,573-579`:
> `FAILED_DATA_CONTRACT`/`LEAKAGE_DETECTED`/`RESOURCE_ABORT`/`ABSTAIN` precede any scientific
> terminal). **This third branch carries no scientific killed/survived claim, conveys no
> information about the observable's channel content, and does not authorize retuning or
> reopening A's closed designs** (per this section's own stop rule). **Opening B under this third
> branch additionally requires an explicit, dedicated feasibility showing — comparable in rigor to
> PR010's own coverage study — that B's reference-coverage / matched-cut population demands can be
> met under a budget comparable to the one that defeated A; absent that showing, B remains closed
> alongside A.**

**Ranked alternatives.** (1) Adopt the amendment above, proposed for a future authorized edit —
recommended, converges all seven roles. (2) Declare the matrix formally superseded by
`docs/plan_operativo_15_julio_2026.md` in its entirety — rejected: no role found this recorded
anywhere, it would silently discard §7's other live stop-rules along with §6, and the newer plan
has its own independent, non-equivalent OP-2.2 structure that was never shown to subsume the
matrix's candidate-ranking logic. (3) Leave it blocked (outcome c) — logically available, and
explicitly not rejected by the logician or physicist, but the committee's converged reading is that
indefinite silence is itself a discharge-condition-free veto, which is a founding-rule hazard in
its own right; the committee recommends resolving it now rather than deferring again. (4) Declare
outcome (a) as literally worded — rejected: blocked by the pre-registration warden, falsified by
the falsifier's grep, and unsupported by any wave-1 role.

**Open disagreements (surfaced, not hidden).**
- None substantive survive to this synthesis — the four wave-1 briefs, falsifier, and warden
  converged on the same outcome and the same structural reasoning (typed third tier, not a third
  scientific value), differing only in which clauses to include, all of which are additive and
  non-conflicting and have been merged into the single amendment text above.
- One citation-path bookkeeping error (§7 note) is corrected; it was the chair's error in dossier
  compression, not a substantive disagreement between roles.

## 9. Next-step spec

**This session takes no action beyond writing this acta — no file other than this one is
modified.**

**Reversible steps (git-revertable, touches no seal, no validation seed, no PR012/PR013/
OP-2.1/OP-2.3/BD-action formula; may be run only if and when the user separately requests that
session):**

1. Edit `research_program/work_packages/next_observable_candidate_matrix.md` §6 step 5 to the
   exact amendment text in §8 above, with a dated revision note pointing to this decision
   (`comite_decision_036`).
2. Re-sync `research_program/work_packages/README.md:13-18` ("Active design front" description) so
   it no longer implies PR009's cheap kill test is still the "first permitted next artifact" —
   note instead that PR009/PR010 are closed (design-infeasible) and a future redesign or
   Candidate-B feasibility study is the next open item.
3. Explicitly record, in whichever document the matrix amendment lives, that this resolution does
   **not** by itself authorize opening Candidate B, drafting a Candidate-B feasibility study, or
   touching the BD-action candidate from decision 035 — each remains its own future committing
   step.

**Committing steps (each requires its own explicit PI authorization and, per decision-034/035
precedent, likely its own committee decision):**

- Actually opening Candidate B (or any successor design of Candidate A) for development.
- Any subsequent BD-action / OP-2.2 documentary review (decision 035 §9) — this resolution does
  **not** enable it; unanimous across all four wave-1 experts on Q3.
- Any redesign of Candidate A (a hypothetical "PR011-of-Candidate-A") that would touch PR009's or
  PR010's frozen artifacts, reserved seed bands, or budget parameters.

**Binding rules pre-committed for any future action following this resolution:**

- The amendment's third branch must never be cited as scientific evidence for or against
  Candidate A's underlying hypothesis (effective-expansion horizon sensitivity).
- PR009 and PR010 remain closed without amendment; no repair, re-run, or seed reuse is authorized
  by this decision.
- Opening Candidate B requires the dedicated feasibility showing named in the amendment text,
  frozen and reported before any Candidate-B kill-test data is seen.
- The BD-action candidate from decision 035 remains gated by decision 035 §9 independently of this
  resolution; even a fully resolved sequencing question does not make it "Candidate B" (it is a
  raw single-poset scalar, not the cut/partition contrast the matrix's Candidate B specifies).

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off

_(left blank for the user — decision, date, and any overriding notes)_
