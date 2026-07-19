# Comité Decision 037 — candidate-b-viability-gate-review

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Adjudicar la adopción del borrador `research_program/work_packages/candidate_b_viability_gate.md`
(STATUS: `DRAFT_FOR_COMMITTEE_AND_PI_REVIEW` / `UNSIGNED` / `NOT_ADOPTED`), que operacionaliza la
"explicit, dedicated feasibility showing" de la matriz §6 paso 5 (decisión 036) como una puerta de
cinco condiciones acumulativas: B1 no-redundancia estructural respecto de Candidate A y R-VAR, B2
computabilidad order-only, B3 cobertura real del banco (reuso read-only del artefacto PR010), B4
controles de frontera/censoring, B5 plausibilidad de identificabilidad a N alcanzable.

El borrador declara explícitamente que NO abre Candidate B, no modifica la decisión 036 ni la
matriz, no reabre ni retunea Candidate A, no reactiva la extensión pendiente de R-VAR
(shadows `S_z` / frontera `H_A`), y no autoriza ningún micro-pilot.

Preguntas específicas fijadas por el PI para esta sesión:

1. ¿Son suficientes los mapas de información previa `F_old(C) = (F_PR009(C), F_RVAR(C))` de B1 tal
   como están definidos?
2. ¿Es fuerte y factible el testigo de no-redundancia de B1 (`F_old(C1) = F_old(C2)` pero
   `B(C1) != B(C2)`, más el caso de equivalencia meramente monótona)? ¿Es exigible en la práctica
   antes de que exista una definición concreta de B?
3. ¿Es válida la formulación de B5 (identificabilidad a N alcanzable, `Delta_B(N)` vs `F_B(N)`,
   tres terminales `FEASIBILITY_PLAUSIBLE` / `NOISE_DOMINATED_AT_REACHABLE_N` /
   `UNRESOLVED_NEEDS_MICROPILOT`)?
4. ¿Producen los tres terminales de B5 decisiones inequívocas sin autorizar un micro-pilot
   implícitamente? ¿La frontera del §3 (micro-pilot boundary) es suficiente?

Restricciones de sesión: NO abrir Candidate B, NO tocar Candidate A/PR009/PR010, NO reactivar
shadows/`H_A`, NO ejecutar semillas/runners/enumeración/Monte Carlo, NO modificar decisión 036 ni
la matriz. El comité delibera solo; cualquier cambio de texto al borrador se propone en esta acta,
no se aplica salvo autorización posterior explícita del usuario.

## 2. Verified state

Facts checked **this session** (2026-07-19) by the chair, each with its command/file:line:

- `make verify-seal` → `thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` — MATCH, reproduced
  independently by three separate wave agents (reproducibility engineer, warden, falsifier). No
  drift throughout the session.
- `git rev-parse HEAD` → `475cb93d501bafbf2506328a44df9733739fba24` (`docs: tighten OP-2.2 BD
  dossier gate semantics, rev. 2`). `git status --short`: the primary artefact
  `research_program/work_packages/candidate_b_viability_gate.md` is **untracked**;
  `research_program/work_packages/README.md` is **modified** (uncommitted, +6-line pointer,
  verified via `git diff` — pure cross-reference, opens nothing); three unrelated pre-existing
  untracked files (`docs/auditor/auditor_report_019_...md`,
  `nachocausal-program.local-before-pull.html`, `pr009-runner-scorer-v2.patch`) untouched.
- `sha256sum -c data/reports/pr010_reference_depth_coverage_development.sha256` (run from
  `data/reports/`) → `OK`, hash `58037a1b1ef9dcbf63901fb85e8ee7f2095270f432bff7f37176479d716bb58f`
  — independently reproduced by two separate wave agents this session. Confirmed **directory-
  sensitive**: the sidecar records a bare basename, so the same check FAILS when run from repo
  root (reproducibility engineer, falsifier both reproduced the failure).
- `dev/measure_pr003_rvar_egs_falsification_test.py` — the draft's B1 §`F_RVAR` cites this file
  at line 88 for `future_card_min = C[:, minimal].sum(axis=0)`. **Confirmed stale**: the actual
  line is **127** (`grep -n` reproduced independently by three separate wave agents). The
  *substance* of the citation is correct — a full-column sum over all `N` rows, restricted only in
  which columns (`i ∈ Min(C)`) are evaluated, i.e. `future_card(i) = |future(i)| = |J^+(i)|`
  unrestricted, matching the draft's claim and explicitly *not* `|J^+(i) ∩ Min(C)|` — but the
  `path:line` anchor itself must be corrected before adoption.
- `dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_PREREGISTRATION.md` §16.7 (`:532-561`) — the
  frozen exchangeable tie-break: `TIE_RANK_MASTER_SEED = 9009009; tie_rank =
  Generator(PCG64(SeedSequence([TIE_RANK_MASTER_SEED, seed]))).permutation(N)`. Confirmed verbatim
  this session. §16.7 explicitly calls the estimator "a reproducible **randomized** order-only
  estimator conditional on the frozen ranks" — this depends on the sprinkling `seed`, not solely
  on the abstract poset `C`.
- `research_program/work_packages/next_observable_candidate_matrix.md:164-167` (§6 step 5,
  amended per decision 036) — confirmed verbatim: opening B "additionally requires an explicit,
  dedicated feasibility showing — comparable in rigor to PR010's own coverage study — that B's
  reference-coverage / matched-cut population demands can be met **under a budget comparable to
  the one that defeated A**; absent that showing, B remains closed alongside A."
- `grep -in budget research_program/work_packages/candidate_b_viability_gate.md` → exactly **one**
  hit, at the micro-pilot disclaimer (line 295: "This draft does not design, schedule, or budget
  any micro-pilot"). The draft's B3 (coverage) and B5 (identifiability) conditions check support
  *existence* and signal-vs-noise respectively; **neither checks cost-of-meeting-demands against a
  budget comparable to the one that defeated Candidate A** — the matrix's own operative clause.
  Falsifier-verified, read-only, this session.
- `dev/comite/comite_decision_021_rvar-egs-truncation-object.md` §8 (`:475-486`) —
  `L(i)` PRIMARY, `future_card(i)` SECONDARY, both order-only, no auxiliary sort key. Confirmed.
- `docs/rvar_closure_negative_result.md:56-83` — `R_VAR_STATUS = CLOSED_NEGATIVE_RESULT`; MINK
  coefficient of variation 0.006–0.024 vs BH 0.72–1.01 (40–100× gap) on the frozen tall box
  (`T_EDGE=6.0, R_EDGE=1.2`). Confirmed verbatim. This is a calibration finding about *this*
  geometry, not a claim that the `L`/`future_card` functional is invalid.
- `docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md:158,160,184` — the prior
  interval-DP argmax corner-artifact (`|D*|≈N-few`, crossing interface `B∈{3..8}` independent of
  `N`, diagnosed as a corner artifact because a genuine horizon cut should grow like `sqrt(N)`) and
  the box-aspect-ratio (`T_EDGE/R_EDGE=5`) MINK near-completeness mechanism, which "saturates as
  `N→∞`." Confirmed verbatim.
- `research_program/work_packages/next_observable_candidate_matrix.md:82-121` (§4, Candidate B
  definition) — `I_order(X:Y)=S_order(X)+S_order(Y)-S_order(C)`; existing kill test already
  requires matched Rindler-horizon vs non-horizon null-cut comparison and cut-size/interval-
  count/boundary-cardinality baselines (`:104,106-114`); main risk explicitly named: "a
  codimension-two joint signal need not be horizon-specific" (`:120`). Confirmed.
- `dev/OP22_BD_VIABILITY_DOSSIER.md` V2 (`:92,101,228`) — diamond-vs-Y-poset witness form, cited
  by the draft's B1 for *form only* (equal-invariant, different-output poset pair). Confirmed; no
  BD content otherwise imported.
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:195`
  — the regular-black-hole/Hayward caveat ("would no longer work for regular black holes... could
  also be continued for arbitrarily long proper time inside the horizon"). Confirmed verbatim;
  **absent from the draft's own text**, though it belongs to a future Candidate-B claim boundary
  rather than to this gate itself.
- `nachocausal/gate.py:10` — the sealed gate scores `improvement(O_min) < tau(n)`. `future_card(i)`
  is explicitly "the sealed `O_min(i)` restricted" per the falsification-test docstring
  (`dev/measure_pr003_rvar_egs_falsification_test.py:21`). Falsifier flags this as a scoping
  question: `F_old` as currently defined does not cover a hypothetical `B` that repackages
  `O_min`/`improvement` over non-minimal elements — a possibly-intentional scoping choice (036's
  concern was Candidate A/R-VAR specifically) that the draft does not state explicitly.

## 3. Dossier

- `research_program/work_packages/candidate_b_viability_gate.md` (full document, 315 lines)
- `docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md` (full document)
- `research_program/work_packages/next_observable_candidate_matrix.md` (§3, §4, §6)
- `dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_PREREGISTRATION.md` (§4, §5.2–5.4, §8.1, §16.3,
  §16.7)
- `dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_CLOSURE_DECISION.md` (full document)
- `dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md` +
  `dev/PR010_REFERENCE_DEPTH_COVERAGE_DEVELOPMENT_PROTOCOL.md` (full documents)
- `docs/comite/comite_decision_021_rvar-egs-truncation-object.md` §8
- `docs/rvar_closure_negative_result.md` (full document)
- `dev/measure_pr003_rvar_egs_falsification_test.py`
- `docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md` (corner-artifact and
  aspect-ratio findings)
- `dev/OP22_BD_VIABILITY_DOSSIER.md` §V2 (witness form only)
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`
  (EGS mechanism, regular-BH caveat)
- `biblioteca/derived-md/Bombelli_1987_PhD.md` (number–volume correspondence)
- `docs/estimator_v2_freeze.md` §A (sealed `O_min` definition)
- `nachocausal/gate.py` (sealed gate)
- `formal/HorizonFormal/HorizonFormal/{Horizon,Ideals,Ends,ChainEnds}.lean`,
  `dev/LEAN_HYPOTHESIS_AUDIT.md` (unrelated formal object, cited by the logician for contrast only)
- `docs/plan_operativo_15_julio_2026.md:87-88,573-579` (bench-negative precedence convention)
- `CLAUDE.md`

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

- **Proposed artefact(s):** This decision is documentary; it produces/references, not runs.
  Primary: `research_program/work_packages/candidate_b_viability_gate.md` (untracked). Pointer:
  6-line addition to `research_program/work_packages/README.md` (modified, uncommitted, pure
  cross-reference). Future: the adopting decision `docs/comite/comite_decision_037_*.md` (this
  acta). The verbatim matrix-pointer sentence in the draft's §4 is a *proposal*, not an edit — the
  matrix stays byte-identical until a separate committing step. If the gate is later exercised
  against a real Candidate-B proposal, the first artefact would be a dev-only, read-only B1
  witness note (hand-computed toy-poset pair), never a production data touch.
- **Environment & seal:** Documentary adoption touches no sealed path. `make verify-seal` MATCH
  reproduced this session. The pinned-`numpy<2` dev env is irrelevant to adoption; becomes
  relevant only if B1/B5 are later exercised computationally via the numpy-array-based dev tools
  the draft names.
- **Provenance capture:** commit SHA at adoption (HEAD=`475cb93`); the draft carries `DATE:
  2026-07-19` prose but no commit/sha self-anchor — should be added at adoption. B3 support
  envelope sha256 independently verified this session:
  `58037a1b1ef9dcbf63901fb85e8ee7f2095270f432bff7f37176479d716bb58f`.
- **Run mechanics:** Adoption is a reversible documentary commit — until a committee decision plus
  PI sign-off exist, the draft "authorizes nothing" and can be abandoned by not committing it.
  Committing steps (opening Candidate B, any micro-pilot) are correctly firewalled: B5's
  `UNRESOLVED_NEEDS_MICROPILOT` explicitly does not authorize execution, and the §3 boundary
  requires a full freeze before any micro-pilot.
- **Reproducibility risks / ambiguities:**
  - **Stale `path:line` anchor** — the draft and DOSSIER cite
    `dev/measure_pr003_rvar_egs_falsification_test.py:88`; the actual line is **127** (grep-
    confirmed). Content claim correct; citation wrong; must be fixed before adoption so the anchor
    can fail-check later.
  - **Sidecar verification is directory-sensitive** — `sha256sum -c` fails from repo root, only
    passes from `data/reports/`; the draft's B3 should pin the hash inline and state the
    convention explicitly.
  - **Draft carries no self-provenance** — untracked, no committed sha256 of itself.
  - **No leakage / seal exposure introduced** by adoption itself.
  - `[UNVERIFIED]`: whether the future B1 dev computation is bit-reproducible depends on
    `measure_kbeam_peeloff.py`'s determinism under the frozen `boundary_minimals_invariant` start
    rule — not executed to check, out of scope this session.

### Mathematician brief

- **Computability:** Every atom of B1's `F_old` is decidable from the order relation alone. `L(i)`
  is the standard DAG longest-path recursion, total on any finite poset, order-only
  (`dev/measure_pr003_rvar_egs_falsification_test.py:67-87`). `future_card(i)=|future(i)|` is a
  column sum, order-only. `F_PR009`'s inputs (enclosing-diamond separation, `W_k`, `theta_raw`)
  are certified order-only in PR009 prereg §5.3-5.4 ("This scalar and all inputs to it are
  order-only"). The abstention/domain gate is the four-state grammar (`TRANSITION_EVALUABLE /
  WIDTH_ONLY / WIDTH_UNEVALUABLE / EMPTY`), correct partiality handling.
- **Order observable:** The horizon-carrying quantity is the joint per-minimal pair `(L(i),
  future_card(i))` — the causal-set image of the EGS focusing mechanism (longest-chain height ↔
  proper time, future cardinality ↔ volume, interior/exterior bimodality).
- **Relevant invariants:** longest chain/height (Myrheim 1978 `[UNVERIFIED — absent from
  biblioteca]`; Brightwell–Gregory `[UNVERIFIED — absent from biblioteca]`; Surya LRR 2019
  `[UNVERIFIED — absent from biblioteca]`); future-volume via the Bombelli–Meyer
  number–volume correspondence (CONFIRMED, `biblioteca/derived-md/Bombelli_1987_PhD.md:579`), the
  same functional sealed as estimator-v2 `O_min(i)=|future(i)|`.
- **Analytic / continuum target:** interior vs exterior branches of geodesic-focusing near
  `r=2M`, bounded correctly to finite-1+1D-patch localisation, never metric reconstruction.
- **Caveats:**
  - `future_card` codomain reading is mathematically correct — full-column sum, domain- not
    codomain-restricted (verified at the corrected line 127).
  - Citation-line drift confirmed (`:88`→`:127`), non-substantive.
  - **Joint-multiset requirement is necessary AND sufficient against the "recombine marginals"
    evasion** — separate marginals discard the per-element pairing/copula; any permutation-
    invariant `B` computed from the joint pairs is a function of this multiset, so the witness
    route cannot be gamed by recombination. Not claimed sufficient against *all* redundancy —
    that's what the certificate route and monotone clause are for.
  - Witness soundness has no gap for what B1 claims: `F_old(C1)=F_old(C2) ∧ B(C1)≠B(C2)` is a
    sound disproof that `B` is a deterministic function of `F_old`.
  - B1 is correctly not dischargeable before `B` exists — it is a well-posed filter on a proposed
    `B`, not a standalone theorem.
  - **`F_PR009` permutation-invariance is "in distribution," not pointwise** — prereg §16.7 fixes
    an exchangeable tie-break seeded by `TIE_RANK_MASTER_SEED`, dependent on the sprinkling
    `seed`. The draft's phrase "no randomness beyond what is fixed by `C` itself" is imprecise;
    the tie-seed must be part of the frozen ensemble-map parameters when an equality comparison
    is invoked.
  - B2 is precisely and completely stated — the invariance clause subsumes the prohibited-input
    list.

### Mathematical logic brief

- **Formal status:** The draft asserts no theorem of its own. Objects sort correctly into three
  kinds: imported definitions (`F_PR009`, `F_RVAR`, frozen and anchored), proof obligations
  against a future fixed `B` (B1-B5), and verdict/terminal tokens (PASS/FAIL/UNRESOLVED; B5's
  three terminals). No condition is formalised; the repo's only machine-checked artefacts
  concern a different object and remain physically `OPEN` — the gate's rigor is documentary, not
  formal.
- **Quantifier / dependency order:** Well-formed pre-registration schema; universally quantified
  over future `B`; no hidden existential asserting a viable `B` exists; B5's precondition "B's
  scientific contrast must be fixed" makes the ordering explicit. `NO_POST_HOC_TUNING` respected
  in principle.
- **Equivalence claims — ONE GENUINE GAP:** B1's Route 1 (witness: joint equality of both
  `F_PR009` profile AND `F_RVAR` multiset, `B(C1)≠B(C2)`) is **strictly stronger** than Route 2
  (certificate: "rule out `B` is a deterministic function of `F_PR009` **or** of `F_RVAR`" — i.e.
  each marginal separately). A `B` determined by the *joint* `(F_PR009,F_RVAR)` but by **neither**
  component alone would satisfy Route 2's literal wording while being fully determined by prior
  information — exactly the redundancy Route 1 forbids. **Recommend rewording Route 2 to
  reference the joint `F_old`.**
- **Type / object discipline:** Strong throughout — `F_RVAR` correctly typed as a permutation-
  invariant multiset (not marginals); `future_card(i)=|J^+(i)|` correctly restricted in domain,
  not codomain; `F_PR009` correctly typed as a functional of `C` composed with the frozen
  deterministic ensemble map. No category errors.
- **Caveats:**
  - **B5's governing conditional is mis-scoped** — the antecedent "If existing theory and results
    do NOT determine the signal-to-fluctuation relation" is written to govern all three
    terminals, but `FEASIBILITY_PLAUSIBLE` is by its own definition a determination-favorable
    case. Recommend restructuring into three disjoint antecedents.
  - With that fix, the three terminals do exhaustively partition epistemic states; the
    `FEASIBILITY_PLAUSIBLE`/`UNRESOLVED_NEEDS_MICROPILOT` boundary is vague but conservatively so
    (cannot launder toward PASS).
  - No laundering path from `UNRESOLVED_NEEDS_MICROPILOT` to authorization — explicit denial plus
    the §3 boundary is structurally sufficient (though see falsifier's freeze-violation finding
    below for a *second-pass* laundering risk this brief did not cover).
  - The gate's rigor is documentary, not formalised — acceptable, but the adopting decision
    should state this so B1-B5 are never over-cited as theorems.

### Physicist brief

- **Coordinates & patch:** frozen tall box `T_EDGE=6.0, R_EDGE=1.2, R_CENTER=0.7, R_S=0.5`,
  `r∈[0.1,1.3]`. Finiteness forfeits any asymptotic construction — only finite-patch localisation
  of `r=2M` is admissible. B2's prohibitions correctly enforce order-only construction.
- **Physical meaning:** Candidate B's action-non-additivity cut contrast is a **different object**
  from the R-VAR/EGS longest-chain bimodality cited as `F_RVAR` prior art — B's horizon-
  specificity is unproven (matrix's own risk: "a codimension-two joint signal need not be
  horizon-specific").
- **Claim boundary:** A gate PASS would license only *proposing* a Candidate-B preregistration.
  Flags a **missing regular-black-hole/Hayward caveat** (EGS: partition diagnostics fail for
  regular black holes since interior curves continue arbitrarily long) that belongs in B's
  eventual claim boundary but is absent from the draft.
- **Focus (a) — B4 is physically incomplete for a cut/partition observable.** Missing two
  load-bearing failure modes from this project's own history: (i) the corner/boundary-artifact
  mode (comité 020/021: interval-DP argmax `|D*|≈N-few`, crossing interface `B∈{3..8}`
  independent of `N` — a genuine cut should grow like `sqrt(N)`; matrix §4 already demands a
  cardinality-matched control and Rindler-vs-non-horizon-null-cut kill test that B4 doesn't name);
  (ii) the aspect-ratio MINK near-degeneracy mechanism (`T_EDGE/R_EDGE=5` drove two independently
  designed R-VAR objects into near-delta MINK nulls). Recommends B4 be amended (proposal only)
  with (i) an N-scaling/crossing-interface-growth control, (ii) a generic-cut/cardinality-matched
  baseline per matrix §4, (iii) an explicit aspect-ratio MINK-degeneracy control. As written, a
  future exerciser could record B4 PASS without ever testing the corner-artifact mode.
- **Focus (b) — B5 is well-posed only for a B whose contrast is already fixed; the draft partly
  conceals this.** `Delta_B(N)`/`F_B(N)` are undefined for a symbol; B5's own text admits "B's
  contrast must be fixed" but this sits *inside* B5 while B1/B2 treat `B` as unspecified — the
  gate ordering does not globally enforce "contrast fixed before B5." Resolvable by an explicit
  statement.
- **Focus (c) — reusing R-VAR's MINK-degeneracy as positive B5 evidence would be a trap; as a B4
  warning it is sound.** Crosses object classes (per-element statistics vs whole-poset action
  contrast); the same near-complete MINK order could equally collapse `Delta_B`'s numerator, not
  just shrink `F_B`'s denominator — the sign of the box effect on a cut statistic is unpredictable
  from the R-VAR per-element result. The draft currently does neither (safe omission, but B4
  would be stronger for naming it as a warning).

## 5. Falsifier attack

### Falsifier attack

- **Concrete failure modes:**
  1. **The gate does not operationalize the clause it claims to operationalize — a new, blocking
     finding wave-1 missed entirely.** Matrix §6 step 5's amended requirement is explicitly
     budgetary: B's coverage/matched-cut demands must be met "under a budget **comparable to the
     one that defeated A**; absent that showing, B remains closed" (matrix `:164-167`). The word
     "budget" appears in the draft exactly once, in the micro-pilot disclaimer (`:295`,
     `grep -in budget` → single hit). B3 checks support *existence*; B5 checks signal-vs-noise;
     **neither checks cost-of-meeting-demands**. If the draft's §4 pointer sentence ("the
     feasibility showing… **is operationalized as** the five-condition gate," `:302-306`) is
     adopted verbatim, a gate PASS would silently discharge a frozen requirement it does not
     contain — `NO_THRESHOLD_LOOSENING` at adoption time. **Blocking.**
  2. **Logician's Route-1/Route-2 gap: confirmed and blocking as worded** — Route 2's literal
     "or" admits a `B` that is a deterministic function of the *joint* `(F_PR009,F_RVAR)` but of
     neither marginal alone, i.e. exactly the redundant case Route 1 forbids. A one-line fix
     ("deterministic function of the joint `F_old`") is required pre-adoption.
  3. **B1's "no randomness beyond `C`" claim is false, and this is more severe than the
     mathematician's "imprecise wording" caveat — it enables witness laundering.** PR009 prereg
     §16.7's tie-break depends on the **sprinkling seed**, not the abstract poset; for hand-built
     witness posets (the accepted OP22 form the draft itself cites), no sprinkling seed exists,
     so `F_PR009(C1)=F_PR009(C2)` is undefined unless witnesses are tie-free — otherwise an
     exerciser could *choose* a tie-rank assignment to manufacture equality. Fix: delete the false
     sentence; require tie-free witnesses or a pre-frozen tie-rank convention.
  4. **`F_old` is under-inclusive against the repo's principal prior observable, `O_min`.**
     `future_card(i)` is literally the sealed `O_min(i)` restricted; a `B` repackaging
     `O_min`/`improvement` over **non-minimal** elements passes B1 by construction while being
     structurally redundant with the sealed estimator-v2 family. Possibly an intentional scoping
     choice (036's concern was Candidate A/R-VAR specifically) — flag for PI decision, not
     blocking, but the draft should say so explicitly.
  5. **B4 incompleteness (physicist): confirmed, severity "amend" not "block."** The matrix's own
     kill test (Rindler-vs-non-horizon-null-cut) remains independently binding regardless of B4,
     so the gate does not *remove* this control — but B4's "PASS (controls constructible and
     documented)" permits a documentary PASS that never names this bench's two historically
     realized failure modes (corner-artifact N-scaling, aspect-ratio degeneracy). Amend B4 with
     the physicist's three named controls before adoption.
  6. **B5's conditional mis-scoping (logician): confirmed, with a worse corollary.** On the
     *determined* branch (the complement of the mis-scoped antecedent), the draft specifies **no
     terminal vocabulary at all** — a grammar escape hatch permitting a free-form verdict outside
     the frozen tokens. The three-antecedent restructure must be a pre-adoption requirement, not
     a suggestion.
- **Ground-truth leakage:** No direct path into `B`'s construction (B2's list is sound; B3 reuse
  is read-only, sidecar verified). Two indirect channels wave-1 missed: (i) B4 controls sit
  outside B2's firewall — B4 controls "from existing material" may include embedding-derived
  diagnostic masks (interior/exterior `r`-based labels marked "diagnostic only" in the R-VAR
  script); a control outcome informing a successor-B redesign is embedding→observable guidance
  one step removed. (ii) unbounded gate re-entry — a FAIL "closes the proposal under review," but
  §0 admits "a successor proposal occupying that slot" with no attempt limit, no cross-attempt
  log, no `NON_CORROBORATION`-style discipline across successive B's; iterating designs against
  known B4/B5 failure reasons is tuning against the bench. Requires: order-only B4 controls (or
  an embedding-material quarantine statement) and a re-entry provision.
- **Freeze violations:** (i) the budget-clause substitution above is a loosening of a frozen
  matrix requirement, executed at adoption if the §4 pointer is adopted as literally worded. (ii)
  **A second-pass B5 laundering path the logician's "no laundering" verdict did not cover:** B5
  forbids inventing a sigma threshold now, but "protrudes above the noise envelope" has no numeric
  definition anywhere, and §3's micro-pilot freeze list names "the terminal read-out" but not the
  quantitative *separation criterion or fluctuation-envelope estimator*. If a micro-pilot runs and
  the protrusion criterion is fixed only after its data exists, the `FEASIBILITY_PLAUSIBLE`/
  `NOISE_DOMINATED` boundary would be set on inspected data — `NO_POST_HOC_TUNING` violated in the
  gate's own designed continuation. Amend §3's freeze list to explicitly include the separation
  criterion and envelope estimator. No sealed-path, virgin-seed, or re-run violation found in the
  documentary step itself.
- **Verdict coercion:** Asymmetries run conservative throughout (B5 PASS restricted to
  `FEASIBILITY_PLAUSIBLE`; B3 FAIL restricted to design-tier; UNRESOLVED never averaged into
  PASS). Two residual pressures, non-blocking: the token name `UNRESOLVED_NEEDS_MICROPILOT`
  embeds its remedy in the verdict, pre-framing the follow-on authorization decision; and a
  structural funnel — since only "theory and already-existing results" may ground B5 and no bench
  result exists for a cut-contrast object class, an honest B5 is near-deterministically
  `UNRESOLVED_NEEDS_MICROPILOT` — the PI should adopt knowing the gate is, in practice, a
  micro-pilot-request generator, not a discharger.
- **Premature / over-broad claims:** No metric-reconstruction, asymptotic-horizon, or 3+1D claim
  in the draft. The one over-claim is the proposed §4 pointer sentence itself ("**is
  operationalized as**"), false until the budget clause is carried (failure mode 1). The
  physicist's regular-black-hole caveat belongs to a future B's claim boundary, not this gate —
  correctly non-blocking. The stale `:88`→`:127` anchor is substantively harmless (content
  verified correct) but has one rider: B1's claim that its components are "already anchored to
  committed definitions" is strictly false while the draft carries a wrong line anchor and is
  itself uncommitted with no self-provenance hash — the adoption commit must fix both.
- **Independent-falsification gate:** Satisfied in design — the draft itself requires every
  certificate/witness/estimate be independently re-derived (author ≠ sole verifier, citing the
  decision-035 §5 precedent, confirmed verbatim). For this adoption itself, four wave-1 roles plus
  this falsifier pass constitute the independent check; the future adopting decision must name a
  non-author verifier for each condition when the gate is actually exercised.
- **Minimal falsification test:** Already executed this session, read-only:
  `grep -in budget research_program/work_packages/candidate_b_viability_gate.md` (one hit, the
  micro-pilot disclaimer) vs `sed -n '160,168p' research_program/work_packages/
  next_observable_candidate_matrix.md` (the budget-comparable clause). This single check exposes
  the worst failure (adoption-time substitution of a frozen requirement) with no execution of any
  sealed or committing path.

**Falsifier's own adjudication:** DO NOT ADOPT the current literal text. Conditions on six
pre-adoption amendments (A1–A6, see §9).

## 6. Pre-registration verdict

### Pre-registration verdict

- **Verdict: PASS** — for adopting the draft as a documentary gate *definition*, conditional on
  the wave-1/falsifier precision fixes (A1–A6, §9) being folded into the text before or at the
  actual adoption decision. Nothing in the draft as written commits a freeze/seed/reporting
  violation in *this* documentary step; the flagged gaps are exercise-time laxity risks for a
  *future* gate run and one adoption-time over-claim risk (the §4 pointer sentence), not
  violations already committed by writing this acta.
- **Freeze status:** The object being frozen is the gate's own text, not a threshold read against
  validation data. Matrix §6 step 5's underlying precondition is already frozen-in-writing
  (`next_observable_candidate_matrix.md:4-7`, decision 036); this draft operationalizes that
  clause and explicitly declines to touch it. No Candidate-B validation seed exists yet, so no
  threshold can be fit against inspected data; B5 explicitly bans inventing/tuning any sigma
  threshold against inspected data.
- **Seal integrity:** `make verify-seal` MATCH, reproduced three times independently this
  session. Adoption is a documentary git commit of an untracked `.md` file plus a 6-line README
  pointer; the sealed validation path is not invoked. `RESPECT_SEAL_FREEZE` holds.
- **Seed discipline:** No seed is drawn or referenced. The PR010 coverage artifact is reused
  strictly read-only, sha256 independently reproduced. `TIE_RANK_MASTER_SEED = 9009009` is a
  pre-existing frozen constant the draft cites by reference only, not a seed this adoption draws.
  No reserved/virgin band is touched or implied.
- **Reporting rule:** Enforced structurally throughout (gate-level UNRESOLVED-never-coerced
  clause; B1/B3/B4/B5 each maintain a genuine three-way PASS/FAIL/UNRESOLVED split with FAIL
  restricted to demonstrated, named conditions). The B5 conditional-scoping defect (logician,
  falsifier) is a wording imprecision, not a coercion of an abstain into PASS — the terminal
  separation itself remains intact.
- **Forbidden moves present?**
  - `NO_POST_HOC_TUNING`: absent in the documentary text as written; **at-risk in the designed
    continuation** per the falsifier's second-pass B5 laundering finding (§3's freeze list omits
    the separation criterion/envelope estimator) — must be closed (A3) before any micro-pilot,
    not before this adoption.
  - `NO_THRESHOLD_LOOSENING`: **at-risk at adoption** via the budget-clause omission (falsifier
    finding 1) — the proposed §4 pointer sentence, if adopted verbatim, would discharge a frozen
    matrix requirement the gate does not check. Must be closed (A2) before the pointer sentence is
    adopted.
  - `NO_GROUND_TRUTH_LEAKAGE`: absent in direct construction paths (B2's list is sound); one
    indirect, non-blocking channel flagged by the falsifier (B4 controls sourced from
    embedding-derived diagnostic material) — recommend closing at B4 amendment time.
  - Re-run after peeking: absent — B3 is read-only reuse; no micro-pilot, enumeration, Monte
    Carlo, or seed draw is authorized anywhere in the draft.
  - `NO_RECONSTRUCTION_CLAIM`: absent — §0 and §5 both explicitly disclaim any candidate opening,
    scientific claim, or reactivation of A or the shadows/`H_A` extension.
- **Reasons (residual items owed to the committee record, non-blocking for *writing this acta*,
  blocking for *adopting the literal current text*):**
  - Stale `path:line` anchor (`:88`→`:127`) — correct before final adoption text is signed.
  - B1 Route 2 must be reworded to the joint `F_old` (logician + falsifier, independently
    converged).
  - B1's "no randomness beyond `C`" sentence is false and must be deleted or qualified
    (falsifier, sharpening the mathematician's caveat).
  - B4 should name the corner-artifact and aspect-ratio controls (physicist, falsifier
    concurring on severity "amend").
  - B5's governing conditional must be restructured into three disjoint antecedents (logician,
    falsifier concurring, falsifier adding the determined-branch grammar-gap corollary).
  - The §4 matrix-pointer sentence must either carry the budget-comparability clause or be
    weakened to "partially operationalizes" (falsifier, new finding, most severe).
  - §3's micro-pilot freeze list should explicitly include the separation criterion and
    fluctuation-envelope estimator (falsifier, new finding).

## 7. Literature verdict

### Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| `dev/measure_pr003_rvar_egs_falsification_test.py:88` (`future_card_min`) | Repro engineer, Mathematician, Logician | UNCONFIRMED — actual line is **127** (grep-confirmed); substance correct, anchor stale |
| `dev/measure_pr003_rvar_egs_falsification_test.py:67-87` (`L(i)` recursion) | Mathematician | CONFIRMED |
| `dev/measure_pr003_rvar_egs_falsification_test.py:14-24,21-24` (docstring) | Mathematician | CONFIRMED — substantiates draft's domain-not-codomain phrasing |
| `dev/PR009_..._PREREGISTRATION.md` §5.2-5.4 (`:75-141`) | Mathematician, Logician | CONFIRMED, incl. verbatim "This scalar and all inputs to it are order-only" |
| `dev/PR009_..._PREREGISTRATION.md` §8.1 abstention grammar `:466-476` | Mathematician | UNCONFIRMED section label — lines correct, but grammar lives under §16.3, not §8.1 |
| `dev/PR009_..._PREREGISTRATION.md` §16.7 (`:532-561`) tie-break | Mathematician | CONFIRMED verbatim, incl. `TIE_RANK_MASTER_SEED = 9009009` |
| `formal/HorizonFormal/HorizonFormal/Horizon.lean` — `RelationalHorizon` | Logician | CONFIRMED |
| `formal/HorizonFormal/HorizonFormal/Ideals.lean` — `IdealEnd`/`ChainEnd` | Logician | PARTIALLY CONFIRMED — `IdealEnd`/`ChainEnd` actually defined in `Ends.lean`/`ChainEnds.lean` |
| `dev/LEAN_HYPOTHESIS_AUDIT.md:31,166,238-239` | Logician | CONFIRMED |
| `biblioteca/derived-md/Towards black-hole horizons...md:166-185` (EGS mechanism) | Mathematician, Physicist | CONFIRMED |
| same file `:175` (H_c infinite-curve requirement) | Physicist | CONFIRMED, Eq. (9) |
| same file `:195` (regular-BH/Hayward caveat) | Physicist | CONFIRMED verbatim |
| `docs/estimator_v2_freeze.md` §A (`:34-37`, `O_min`) | Mathematician | CONFIRMED |
| Myrheim 1978 | Mathematician | UNVERIFIED — absent from `biblioteca/` (consistent with comité 020's own prior finding) |
| Surya LRR 2019 §3-4/§4 | Mathematician | UNVERIFIED — absent from `biblioteca/` |
| Brightwell–Gregory `m≈1.77` | Mathematician | UNVERIFIED — absent from `biblioteca/` |
| Bombelli–Meyer `⟨n⟩=ρV` | Mathematician | CONFIRMED, `Bombelli_1987_PhD.md:579` |
| `docs/comite/comite_decision_021_...md` §8 (`:475-486`) | Logician, draft | CONFIRMED |
| `comite_decision_020...:119` (localisation framing) | Physicist | CONFIRMED |
| `comite_decision_020...:160,165,169` (corner-artifact) | Physicist | PARTIALLY CONFIRMED — `:169` is actually the aspect-ratio passage, not corner-artifact; correct anchors are `:158/:184` |
| `next_observable_candidate_matrix.md:104,106-114` (cardinality-matched control) | Physicist | CONFIRMED |
| `next_observable_candidate_matrix.md:119` ("noisy and dimension-dependent") | Physicist | CONFIRMED verbatim |
| `docs/rvar_closure_negative_result.md:75-83` + `comite_decision_020...:184` (aspect-ratio) | Physicist | CONFIRMED |
| `docs/rvar_closure_negative_result.md:56-83` (CV 0.006-0.024 vs 0.72-1.01) | Physicist | CONFIRMED verbatim |
| `comite_decision_020...:158` (saturates as N→∞) | Physicist | CONFIRMED verbatim |
| `nachocausal/thresholds.py:36-40` (box constants) | Physicist | CONFIRMED verbatim |
| `data/reports/pr010_..._development.sha256` = `58037a1b...` | Repro engineer, draft B3 | CONFIRMED |
| `thresholds.py` sha256 = `6e2c3888...bfefd4` | Repro engineer | CONFIRMED, matches `docs/preregistration_002.md:8` |
| HEAD=`475cb93` | Repro engineer | CONFIRMED |
| `candidate_b_viability_gate.md:81-112` (F_PR009 def) | Logician | CONFIRMED |
| `candidate_b_viability_gate.md:114-141` (F_RVAR def) | Logician | CONFIRMED |
| `candidate_b_viability_gate.md:162-172` / `:174-175` (Route 1 / Route 2) | Logician | CONFIRMED |
| `candidate_b_viability_gate.md:274-278` (B5 mis-scoping) | Logician | CONFIRMED |
| `candidate_b_viability_gate.md:284-285,292` (no-laundering, wave-1 reading) | Logician | CONFIRMED, though falsifier finds a second-pass gap this citation does not cover |
| `dev/OP22_BD_VIABILITY_DOSSIER.md` V2 (`:92,101,228`) | draft | CONFIRMED |
| `docs/plan_operativo_15_julio_2026.md:87-88,573-579` | draft | CONFIRMED verbatim |
| `docs/comite/comite_decision_035...md:450-451,735` ("author ≠ sole verifier") | draft, falsifier | CONFIRMED |
| `dev/PR009_..._CLOSURE_DECISION.md` = `FAILED_DATA_CONTRACT`; `dev/PR010_..._DECISION.md` = `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE` | draft | CONFIRMED |
| `next_observable_candidate_matrix.md:164-167` (budget-comparable clause) | Falsifier | CONFIRMED verbatim — the load-bearing citation for the session's most severe new finding |
| `nachocausal/gate.py:10` (`improvement(O_min) < tau(n)`) | Falsifier | CONFIRMED |

- **Notes:** The `:88`→`:127` stale anchor is definitively confirmed by direct grep and recurs
  across the DOSSIER and three wave-1 briefs without independent correction until the literature
  verifier settled it. The mathematician's §8.1 section-label (vs the correct §16.3) is a minor
  mislabel not affecting the grammar's content. The physicist's `:169` sub-citation is imprecise
  (it is the aspect-ratio passage, not the corner-artifact passage) but the correct anchors
  (`:158/:184`) are cited elsewhere in the same brief. Myrheim 1978, Surya LRR 2019, and
  Brightwell–Gregory remain absent from `biblioteca/` — consistent with comité 020's own prior
  literature-verdict table, not a new gap introduced this session; these three should not be
  relied upon as confirmed literature support in any adoption text. All numerical/hash/line-count
  claims that could be independently recomputed (seal sha256, B3 envelope sha256, HEAD commit,
  README diff, box constants, CV values, budget-clause text) were recomputed or directly grepped
  and matched — no fabricated provenance was found anywhere in the seven briefs.

## 8. Synthesis

**Convergence.** All seven roles converge that the draft's core architecture is sound: B1's joint
`F_RVAR` multiset genuinely closes the "recombine the marginals" evasion (mathematician,
independently confirmed by the falsifier); `F_PR009`'s two-stage definition (frozen ensemble
construction + per-depth profile) is order-only and correctly typed (mathematician, logician);
B2 is complete; B3's read-only reuse and explicit two-case distinction (same-unit vs
different-object) is sound; B5's overall three-terminal shape is the right honest structure for
an as-yet-undefined `B`'s identifiability question (physicist, logician). No role found any
direct ground-truth-leakage path in the draft's core construction rules, and the seal/seed
discipline is untouched by adopting this documentary text.

**No role recommends bare adoption of the literal current text.** The warden's own PASS is
explicitly conditional ("conditional on the wave-1 precision fixes... being folded in before or
at the actual adoption decision"); the falsifier's independent adjudication is stronger ("DO NOT
ADOPT the current literal text"). Both converge on the same underlying diagnosis: the draft's
*direction* is correct and its guardrail discipline is real, but six specific textual defects —
three already surfaced by wave-1 (B1 Route-2 marginal/joint gap, B4 missing named controls, B5
conditional mis-scoping) and three found only by the falsifier's independent re-verification (the
missing budget-comparability clause, the false "no randomness" sentence with its witness-
laundering consequence, and the second-pass B5 freeze-list gap) — must be closed before the text
is fit to adopt as the operative gate.

**The single most severe finding is the falsifier's, and it is new.** None of the four wave-1
experts checked the draft's B3/B5 pair against matrix §6 step 5's *literal* operative clause — the
budget-comparability requirement — despite all four having read that clause in the dossier. The
falsifier's one-command read-only test (`grep -in budget`) exposes that the draft's proposed §4
pointer sentence ("the feasibility showing… is operationalized as…") would, if adopted verbatim,
silently discharge a frozen requirement the five conditions do not check. This is exactly the
"guardrail that cannot fail is decoration" failure mode `CLAUDE.md` names as the founding hazard,
and it is squarely within the pre-registration warden's remit — the warden's own verdict already
flags it as an "at-risk" `NO_THRESHOLD_LOOSENING` item requiring closure before adoption, though
without the falsifier's escalation to "blocking."

**No disagreement survives on the object-level fixes.** Every wave-1 finding the falsifier
reviewed was independently reproduced or sharpened, never contradicted. The one place a genuine
severity disagreement exists is whether B4's incompleteness is "block" or "amend" — the physicist
implicitly treated it as amend-worthy but serious; the falsifier explicitly downgrades it to
"amend, not block," reasoning that the matrix's own kill test remains independently binding
regardless of B4's wording, so B4's gap is a documentation completeness issue, not a live leakage
or freeze hole. This committee adopts the falsifier's severity ranking as the more precise one
(it is the only role that explicitly weighed the *consequence* of each defect against the
gate's guardrail tokens, not merely the defect's existence).

**Recommended direction: prepare an amended text, do not adopt the current literal draft.** The
six required amendments (A1–A6, listed exactly in §9) are additive, narrowly scoped, mutually
non-conflicting, and each was independently specified by at least one role and reviewed
adversarially by the falsifier without further objection — they do not require a fresh full
seven-role deliberation to apply. The three physicist-recommended B4 controls and the falsifier's
two ground-truth-leakage/re-entry recommendations are advisory (non-blocking) and may be folded in
at the same edit pass at the PI's discretion.

**Ranked alternatives.** (1) **Recommended**: apply amendments A1–A6 to the draft text (a
reversible, non-committing documentary edit, explicitly authorized by the user before execution),
then treat the amended text — not this acta — as the object for final PI sign-off; the amended
text does not need a fresh wave-1/wave-2 cycle, but a lightweight chair-level re-verification
(re-run the same `grep`/anchor checks against the amended text) is owed before sign-off, per the
falsifier's own "independent-falsification gate" requirement. (2) Adopt the current literal text
as-is: **rejected** — falsified by the falsifier's budget-clause finding, and would let the §4
pointer sentence over-claim what the gate operationalizes. (3) Send the whole gate back for a full
re-convened seven-role review: **rejected as excessive** — no role's finding requires new
information gathering or a change of architecture; every fix is a textual amendment to an already
largely-correct draft. (4) Leave the draft unsigned indefinitely with no further action:
**rejected** — the fixes are cheap, well-specified, and leaving a known `NO_THRESHOLD_LOOSENING`
risk undocumented in the standing draft is itself a freeze-discipline hazard.

**Open disagreements (surfaced, not hidden).** None substantive on the required amendments
(A1–A6) — full convergence across wave-1, the falsifier, and the warden. One severity
classification (B4: "block" vs "amend") is resolved in favor of the falsifier's more precise
reasoning above, not by vote. One scoping question is left explicitly to the PI, not resolved by
the committee: whether `F_old`'s exclusion of the sealed `O_min`/`improvement` functional over
non-minimal elements (falsifier finding 4) is an intentional, acceptable scope limit (decision
036's concern was specifically Candidate A and R-VAR) or should be widened — this is a policy
choice about how broadly "non-redundancy" should reach, not a correctness defect, and the
committee does not adjudicate it here.

## 9. Next-step spec

**This session takes no action beyond writing this acta — no file other than this one is
modified.**

**Reversible steps (git-revertable, touches no seal, no validation seed, no PR009/PR010/Candidate-
A/shadows-`H_A` content; may be run only if and when the user separately requests this session):**

1. Amend `research_program/work_packages/candidate_b_viability_gate.md` with exactly the following
   six required changes (A1–A6), each independently converged on by at least two roles this
   session:
   - **A1 (B1 Route 2, blocking):** reword "an equivalent mathematical certificate ruling out that
     `B` is a deterministic function of `F_PR009` or of `F_RVAR` on the relevant domain" to
     "...ruling out that `B` is a deterministic function of the **joint** `F_old = (F_PR009,
     F_RVAR)` on the relevant domain" — closing the marginal/joint gap (logician, falsifier).
   - **A2 (§4 pointer sentence / B3, blocking):** either (a) add to B3 an explicit sixth check
     that `B`'s reference-coverage/matched-cut demands are met "under a budget comparable to the
     one that defeated Candidate A" (matrix `:164-167`, verbatim clause), or (b) reword the §4
     pointer sentence from "is operationalized as" to "partially operationalizes; the matrix's
     budget-comparability clause remains additionally and independently binding." Either closes
     the `NO_THRESHOLD_LOOSENING` risk (falsifier).
   - **A3 (§3 micro-pilot freeze list, freeze-violation risk):** add "the quantitative separation
     criterion for `Delta_B(N)` vs `F_B(N)` and the fluctuation-envelope estimator" to the list of
     items that must be frozen before any micro-pilot generates data (falsifier).
   - **A4 (B1 `F_PR009` construction text, blocking):** delete or qualify the sentence "with no
     randomness beyond what is already fixed by `C` itself" — it is false per PR009 prereg §16.7's
     seeded tie-break; require tie-free witness posets or a pre-frozen tie-rank convention for any
     B1 exercise using `F_PR009` (mathematician, sharpened to blocking by falsifier).
   - **A5 (citation hygiene, blocking for anchor integrity):** correct
     `dev/measure_pr003_rvar_egs_falsification_test.py:88` to `:127` everywhere it appears in the
     draft; add a self-provenance note (commit SHA at adoption) to the draft's header
     (reproducibility engineer, mathematician, falsifier).
   - **A6 (B5 conditional restructure, blocking):** restructure B5's terminal grammar into three
     explicitly disjoint antecedents — "if theory/results determine separation exists →
     `FEASIBILITY_PLAUSIBLE`; if they determine separation is absent/covered by noise →
     `NOISE_DOMINATED_AT_REACHABLE_N`; if they do not determine the relation either way →
     `UNRESOLVED_NEEDS_MICROPILOT`" — closing the determined-branch grammar gap (logician,
     falsifier).
2. Advisory, non-blocking, may be folded in at the same edit pass at PI discretion: the
   physicist's three named B4 controls (N-scaling/corner-artifact control, generic-cut/
   cardinality-matched baseline, aspect-ratio MINK-degeneracy control); the falsifier's B4-control
   embedding-material quarantine statement and gate re-entry discipline (successor B proposals
   must cite all prior gate attempts and their failure conditions); an explicit statement of
   `F_old`'s scope relative to the sealed `O_min`/`improvement` functional (falsifier finding 4,
   PI's scoping call).
3. After amendment, re-run the same read-only checks this session used
   (`grep -in budget`, the `:127` anchor, `sha256sum -c` from `data/reports/`, `make
   verify-seal`) against the amended text as a lightweight chair-level independent-falsification
   pass — not a full seven-role reconvene — before the amended text is presented for PI sign-off.

**Committing steps (each requires its own explicit PI authorization and, per decision-034/035/036
precedent, its own committee decision):**

- Formally adopting the amended gate text as binding (a signed follow-on to this acta or a
  dedicated new decision).
- Opening Candidate B, drafting its preregistration, or exercising B1–B5 against a concrete `B`
  proposal.
- Any micro-pilot — requires its own separate authorization and must first freeze `B`'s
  definition, contrast, `N` sizes, seeds, and terminal read-out (including, per A3, the
  separation criterion and fluctuation-envelope estimator).
- Any redesign or reopening of Candidate A, PR009, or PR010.
- Any reactivation of the shadows-`(S_z)`/boundary-`(H_A)` R-VAR extension.

**Binding rules pre-committed for any future action following this resolution:**

- The gate's five conditions (B1–B5), once amended per A1–A6, remain a **precondition filter**
  only — passing them never itself opens Candidate B, never constitutes a scientific claim, and
  never alters the PR009/PR010 closures or Candidate A's untested/untestable status.
- No amendment listed above may be treated as complete until independently re-verified by someone
  other than whoever applies the edit (author ≠ sole verifier, per decision-035 §5 and this
  draft's own §0/B1 discipline).
- The `NOISE_DOMINATED_AT_REACHABLE_N` and `UNRESOLVED_NEEDS_MICROPILOT` terminals remain
  bench-specific negatives, never physical no-gos, and `UNRESOLVED_NEEDS_MICROPILOT` never
  authorizes execution by itself.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off

**P.I / Nacho, 2026-07-19:** "Autorizado a todas las acciones que consideres."

Read as: authorization to (a) fold amendments A1–A6 into
`research_program/work_packages/candidate_b_viability_gate.md` per §9's next-step spec — done,
chair-level re-verification (`grep -in budget`, `:127` anchor, sidecar `sha256sum -c` from
`data/reports/`, `make verify-seal`) reproduced against the amended text with no drift; (b) fold
in, at the same edit pass, the advisory (non-blocking) items of §9 item 2 — the physicist's three
named B4 controls, the falsifier's B4 embedding-material quarantine statement and gate re-entry
discipline, and an explicit `F_old`/`O_min` scope statement (left as an intentional scope limit,
not widened — that widening decision is explicitly left open for a future concrete `B` proposal);
(c) formally adopt the amended text as the binding gate definition (STATUS updated to
`ADOPTED_AS_GATE_DEFINITION`).

This sign-off is read narrowly per this acta's own §9 "committing steps" list: it authorizes
adopting the gate **as a precondition filter** only. It does **not** authorize, and is not read
as authorizing, opening Candidate B, exercising B1–B5 against a concrete `B` proposal, any
micro-pilot, or any reopening of Candidate A/PR009/PR010 or the R-VAR shadows/`H_A` extension —
each of those remains, per this acta's own text, a separate committing step requiring its own
dedicated committee decision plus explicit PI authorization naming that specific action.
