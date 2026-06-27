# Comité Decision 009 — c1-relational-closure-preflight

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question
Should the project revise C1 again before any implementation/probe, or may it proceed with a
strictly reversible **preflight implementation only** of `c1_selector(C)` and its Guard-v tests,
with no BH/MINK scoring, no dev-seed measurement, no threshold choice, and no promotion/freeze?

## 2. Verified state
Facts checked this session:
- `git status --short --ignore-submodules=all` produced no output after pushing
  `8737582 comite: add C1 relational dossier`.
- `git log --oneline -5` included:
  `8737582 comite: add C1 relational dossier`,
  `b9da25a comite: add mathematical logic role`,
  `c287f61 pr003: add C1 selection guard and committee review`,
  `16de06d formal: relate chain ends to generated lower sets`,
  `03b31eb formal: add chain end existence wrappers`.
- `make verify-seal` ->
  `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- `.venv/bin/python -m pytest -q tests/test_selection_guard.py tests/test_leak.py` ->
  `7 passed in 0.19s`.
- `cd formal/HorizonFormal && . "$HOME/.elan/env" && lake build` ->
  `Build completed successfully (1448 jobs)`.
- No validation command, BH/MINK scoring, dev-seed measurement, threshold selection, `results/`
  write, or `thresholds.py` edit occurred.

## 3. Dossier
Files and references the chair supplied to the committee:
- `dev/COMITE_009_C1_RELATIONAL_DOSSIER.md`
- `dev/PR003_C1_RELATIONAL_SPEC.md`
- `docs/comite/comite_decision_008_c1-relational-selection-guard.md`
- `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §9.5
- `docs/pr003_leakage_gate.md`
- `nachocausal/selection_guard.py`
- `tests/test_selection_guard.py`
- `formal/HorizonFormal/HorizonFormal/Horizon.lean`
- `formal/HorizonFormal/HorizonFormal/ChainEnds.lean`
- `docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md`

## 4. Expert briefs (wave 1 — blind, parallel)
### Reproducibility engineer brief
- Proposed artefact(s): `nachocausal/c1_selector.py` for a pure preflight selector returning only `{"R": set[element], "interface": set[(element, element)]}`; `tests/test_c1_selector.py` for synthetic/relabel tests; optionally extend `tests/test_selection_guard.py` only for selector-guard coverage. No `results/`, no `validate.py`, no `thresholds.py`, no scoring path.
- Environment & seal: chair reports sealed `thresholds.py` SHA `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`; `pytest selection/leak -> 7 passed`; `lake build -> success`; dossier state is doc/spec only. Package state/pinned numpy are not restated in the dossier beyond existing project environment [UNVERIFIED].
- Provenance capture: current inspected HEAD is `8737582 comite: add C1 relational dossier`; prompt and repo agree on `8737582`. Any preflight run should record commit, command, Python/numpy versions or `pip freeze`, `uname -a`, fixed Guard-v seed(s), UTC timestamp, and explicit statement `NO_BH_MINK_SCORING`.
- Run mechanics: allow only single foreground invocations of unit tests against synthetic or constructed posets. `verify_selection_order_only(C, c1_selector, seed=s)` must abort on non-conjugate selection. The implementation is safe only as reversible preflight code plus tests; it must not call `validate`, scoring, BH/MINK labels, dev seeds, threshold logic, or write measurement artefacts.
- Reproducibility risks / ambiguities:
  - `R=Max(C)` may make `A_R=C`, `B_R=empty`, and `H[C;R]=empty`; preflight must assert deterministic `NO_INTERFACE` behavior before any data.
  - `ASYMMETRY_SCORE`, `PERSISTENCE_THRESHOLD`, and `BULK_CONTROL` remain open; implementing them now would convert preflight into an unregistered probe surface.
  - The current guard verifies relabel-conjugacy of element selections, not physical relevance or wall control.
  - Tests must avoid BH/MINK generated examples if “no probe” is interpreted strictly; synthetic hand-built posets are cleaner.
  - Verdict: `ALLOW_PREFLIGHT_IMPLEMENTATION_ONLY` is reproducibly safe if limited to selector construction and Guard-v tests, with no scoring, no seed measurement, no thresholds, and no persisted result artefacts.

### Mathematician brief
- Computability: On a finite causal poset, `R=Max(C)`, `A_R=down(R)`, `B_R=C\A_R`, covers, height levels, lower sets, ideals, and `H[C;R]` are decidable from the order relation alone. For finite partial orders, every element lies below at least one maximal element, hence `down(Max(C)) = C`; for finite preorders this should be treated on the antisymmetric quotient or gated explicitly. If antisymmetry/finiteness fails, the selector should abstain rather than infer a horizon.
- Order observable: The proposed step relies on the cover interface between `B_R` and `A_R`. With `R=Max(C)` on a finite poset, this observable degenerates: `A_R=C`, `B_R=empty`, so `H[C;R]=empty`. Therefore the current draft carries no intended C1 signal beyond detecting that the maximal-reference rule is trivial.
- Relevant invariants: Maximal elements, lower closure/down-set, cover relations, height, level slices, ideals, generated lower sets, and antichains are all order-only. The key invariant here is `down(Max(C))=C` for finite posets, which forces empty complement and empty interface.
- Analytic / continuum target: No continuum benchmark is needed for a reversible preflight that only verifies selector equivariance and confirms `NO_INTERFACE`. A continuum/BH-MINK target would be premature until `R` is replaced or refined so that `B_R` and `H[C;R]` can be nontrivial without using embedding information.
- Caveats:
  - `R=Max(C)` is not merely wall-risky; on finite posets it is structurally interface-killing.
  - `NO_INTERFACE` can be accepted as falsifiable preflight behavior only if the expected outcome is “this C1 reference draft fails/trivializes,” not as a neutral physical result.
  - A preflight implementation of `c1_selector(C)` is acceptable as a reversible guardrail exercise, but it should not be described as testing C1 signal.
  - Any fallback from `NO_INTERFACE` must be specified before data; otherwise it becomes a post-hoc degree of freedom.
  - [UNVERIFIED] The current code path may not yet enforce finite-partial-order versus finite-preorder assumptions at the selector boundary.

### Mathematical logic brief
- Formal status: `RelationalPast`, `RelationalBlackRegion`, `RelationalHorizon`, `IdealGeneratedByChain`, `ChainEndInIdeal`, and `ChainEnd` are definitions. Lean proves structural order facts for `RelationalHorizon` and chain-end quotients, including lower-set behavior, monotonicity/antitonicity, horizon crossing facts, order-isomorphism transport, countable nonprincipal existence wrappers, and `CofinalChainEquivalent_iff_generated_eq`. C1’s `R(C)=Max(C)`, persistence trace, and `NO_INTERFACE` behavior are specification-level definitions, not Lean theorems. `ASYMMETRY_SCORE`, `PERSISTENCE_THRESHOLD`, `BULK_CONTROL`, `C1_PROMOTION`, physical interpretation, and arbitrary embedding preservation remain open hypotheses.
- Quantifier / dependency order: The coherent order is: choose finite poset `C` -> choose `R(C)` by a fixed order-only rule -> construct `A_R`, `B_R`, and `H[C;R]` -> derive selected interface/levels -> define persistence/asymmetry -> freeze thresholds/controls -> only then score BH/MINK. Post-hoc freedom can enter at `R` selection, empty-interface fallback, antichain/interface summarisation, argmin/argmax tie-breaking, asymmetry side-slices, persistence threshold, and bulk/wall control. A reversible `c1_selector(C)` preflight is logically admissible only if it returns selected elements/pairs and is guarded by relabel-conjugacy, with no physics scoring or threshold choice.
- Equivalence claims: Proved: `ChainEventuallyLe c d ↔ IdealGeneratedByChain c ⊆ IdealGeneratedByChain d`; `CofinalChainEquivalent c d ↔ IdealGeneratedByChain c = IdealGeneratedByChain d`; cofinal chains in an ideal generate that ideal; order isomorphisms transport provisional ideal ends and chain ends. Proved only as structural one-way/projection facts: horizon membership implies black-side/past-side/cover/strict-order properties. Semantic only: `IdealEnd` as escape end, `ChainEnd` as physical cofinal direction, `RelationalHorizon` as horizon precursor, and C1 as apparent/trapping signal.
- Type / object discipline: `R` is a `Set P`, not an `Order.Ideal`; `RelationalPast R` is the lower closure of a reference set. `Order.Ideal` is stronger than a lower set because mathlib ideals include nonemptiness and directedness. `IdealEnd` is a sigma subtype of nonprincipal mathlib ideals, not a physical boundary. `ChainEndInIdeal` is a quotient class of nonterminal cofinal chains inside a fixed ideal; `ChainEnd` pairs an ambient provisional `IdealEnd` with such a quotient. `RelationalHorizon R` is a finite set of ordered pairs, not an event horizon. Treating `R=Max(C)` as an ideal/end or treating empty `H[C;R]` as physical failure would be a category mistake.
- Caveats:
  - `R=Max(C)` is order-only but may make `RelationalPast R = C`, hence `B_R = ∅` and `H[C;R] = ∅`; this is flagged in `dev/PR003_C1_RELATIONAL_SPEC.md` and committee 008.
  - `ASYMMETRY_SCORE` is explicitly open, so no C1 probe is logically closed yet.
  - `PERSISTENCE_THRESHOLD` is explicitly open; choosing it after any data would violate quantifier order.
  - `BULK_CONTROL` is explicitly open; wall-dominated maximal elements remain an unresolved confound.
  - Lean proves covariance under order isomorphisms, not arbitrary embeddings; embedding preservation remains `HYPOTHESES_OPEN`.
  - `RelationalHorizon` Lean theorems are order-theoretic guardrails only, not classical horizon recovery.
  - The selector Guard-v checks relabel-conjugacy of selected element objects; scalar scores and thresholds require separate guards if they become load-bearing.

### Physicist brief
- Coordinates & patch: finite 1+1D Schwarzschild-style patch only; finiteness forfeits access to future null infinity, true event-horizon asymptotics, and any global escape criterion. No asymptotic or reconstruction claim is licensed.
- Physical meaning of the signal: with `R=Max(C)` and `A_R=down(R)` including `R`, C1 likely collapses before physics: in any finite poset every element lies below some maximal element, so `A_R=C`, `B_R=empty`, and `H[C;R]=empty`. If later revised to near-maximal layers, the dominant risk is a sampling-wall detector, not an apparent/trapping precursor.
- Sprinkling domain: finite patch with top/future sampling wall risk; no BH/MINK data have been run for this C1 draft; no bulk control, asymmetry score, or persistence threshold is frozen.
- Claim boundary: permits at most a reversible preflight implementation to expose the degeneracy and Guard-v behavior. It does NOT permit BH/MINK scoring, dev-seed measurement, threshold choice, physical interpretation, promotion, freeze, or any horizon reconstruction claim.
- Caveats:
  - `R=Max(C)` appears structurally degenerate for finite posets under the written `down(R)` rule; this is stronger than merely “wall-coupled”.
  - Anchored: spec flags maximal elements as sampling-wall coupled and leaves `BULK_CONTROL`, `ASYMMETRY_SCORE`, and `PERSISTENCE_THRESHOLD` open.
  - Anchored: committee 008 blocked probes and identified empty-interface collapse as a core blocker.
  - [UNVERIFIED] Whether a nontrivial alternative reference, e.g. interior relational end/chain selection, can separate a trapping-like precursor from the sampling wall without coordinates.

## 5. Falsifier attack
- Concrete failure modes: `R=Max(C)` is already mathematically dead on finite posets: `down(Max(C))=C`, so `B_R=empty` and `H[C;R]=empty`. A preflight implementation risks giving engineering weight to a selector whose only valid output is `NO_INTERFACE`. It is under-powered because it cannot exercise persistence, asymmetry, antichain/interface selection, or C1 signal logic. It is wrong if presented as “testing C1”; it only tests that this C1 draft trivializes.
- Ground-truth leakage: If any fallback is added after `NO_INTERFACE`, leakage can enter through wall-aware choices: near-maximal layers, height cutoffs, sprinkling patch boundaries, causal depth from top wall, BH/MINK-specific expected behavior, or handcrafted synthetic examples shaped to resemble the desired bulk/wall distinction.
- Freeze violations: The main risk is using the preflight failure to justify a revised `R` rule, asymmetry score, persistence threshold, or bulk control after seeing behavior. Re-running with alternative selectors, changing tie-breaks, or adding `NO_INTERFACE` fallbacks would become post-hoc unless specified and reviewed before any implementation beyond the trivial selector.
- Verdict coercion: `NO_INTERFACE` must be treated as “current C1 reference rule is structurally degenerate,” not as an abstention that keeps C1 alive unchanged. Allowing implementation may coerce the project toward “preflight passed” because Guard-v passes, despite the signal being empty by theorem-level finite-poset reasoning.
- Premature / over-broad claims: No horizon reconstruction, apparent horizon, trapping precursor, escape-end, asymptotic event horizon, 3+1D, continuum, or BH/MINK discrimination claim is licensed. Even “C1 is order-only” is too broad if later selector revisions smuggle in wall geometry through height/layer choices.
- Independent-falsification gate: Not satisfied for C1 as a signal. Satisfied only for a narrow negative gate: demonstrate and record that `R=Max(C)` forces `NO_INTERFACE` on finite nonempty posets. That does not authorize BH/MINK probes or C1 promotion.
- Minimal falsification test: No BH/MINK data needed. Add or prove one synthetic finite-poset check: for several hand-built finite posets, compute `R=Max(C)`, assert `A_R == C`, `B_R == empty`, and `RelationalHorizon(R) == empty`. Expected result: universal `NO_INTERFACE`; if not, the implementation is wrong.

## 6. Pre-registration verdict
- Verdict: PASS
- Freeze status: Not frozen for validation/scoring; `ASYMMETRY_SCORE`, `PERSISTENCE_THRESHOLD`, and `BULK_CONTROL` remain open in `dev/COMITE_009_C1_RELATIONAL_DOSSIER.md` / C1 spec. This permits only preflight selector/Guard-v work, not validation or scoring.
- Seal integrity: Sealed path unchanged; `thresholds.py` SHA `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- Seed discipline: No BH/MINK scoring, no dev-seed measurement, no validation seed use, no reserved seed burned. Synthetic/order-only tests only.
- Reporting rule: Preflight may report only selector structure and Guard-v PASS/FAIL/NO_INTERFACE. `NO_INTERFACE` must mean “current `R=Max(C)` draft trivializes,” not physical failure or success. No post-hoc fallback.
- Forbidden moves present? None if limited to preflight. Post-hoc tuning, threshold loosening, leakage, re-run selection, BH/MINK scoring, validation, promotion/freeze, and physical over-claim remain forbidden.
- Reasons:
  - Wave 1 established `R=Max(C)` on finite partial orders forces `down(Max(C))=C`, hence `B_R=empty` and `H[C;R]=empty`.
  - Open scoring/threshold/control choices make any C1 probe unregistered.
  - A reversible `c1_selector(C)` plus relabel-conjugacy Guard-v tests is not a data probe if it avoids scoring, seeds, thresholds, and result artefacts.
  - Preflight is useful only to expose and lock the triviality/guard behavior before revising C1.

## 7. Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| No external literature claim introduced; dossier frames this as internal formal/spec work (`dev/COMITE_009_C1_RELATIONAL_DOSSIER.md`, “Specific Questions For Each Role”, Literature verifier) | Chair dossier | CONFIRMED |
| `dev/PR003_C1_RELATIONAL_SPEC.md` §§1-3: `A_R=down(R)`, `B_R=C\A_R`, `R(C)=Max(C)`, `NO_INTERFACE` on empty interface | Mathematician / physicist / logic | CONFIRMED |
| Standard finite-poset order fact: every element lies below some maximal element, hence `down(Max(C))=C` for finite nonempty posets | Mathematician / physicist / logic | CONFIRMED |
| `dev/PR003_C1_RELATIONAL_SPEC.md` §8: `ASYMMETRY_SCORE`, `PERSISTENCE_THRESHOLD`, `BULK_CONTROL`, `C1_PROMOTION`, `PHYSICAL_INTERPRETATION` remain open | Chair dossier / logic | CONFIRMED |
| `nachocausal/selection_guard.py`, `verify_selection_order_only`: relabel-conjugacy guard for selected element-label objects, not scalar observables | Reproducibility engineer / logic | CONFIRMED |
| `tests/test_selection_guard.py`: positive order-only selector test and negative label-dependent selector test exist | Reproducibility engineer | CONFIRMED |
| Runtime claim `pytest selection/leak -> 7 passed` | Reproducibility engineer | UNVERIFIED |
| `formal/HorizonFormal/HorizonFormal/Horizon.lean`: `RelationalPast`, `RelationalBlackRegion`, `RelationalHorizon`, lower/monotone/frontier lemmas | Logic / chair dossier | CONFIRMED |
| `formal/HorizonFormal/HorizonFormal/ChainEnds.lean`: `IdealGeneratedByChain`, generated-lower-set equivalence, chain-end quotient, order-isomorphism transport | Logic / chair dossier | CONFIRMED |
| Runtime claim `lake build -> success` | Reproducibility engineer / chair dossier | UNVERIFIED |
| `docs/comite/comite_decision_008_c1-relational-selection-guard.md` §§4-10: Guard-v necessary but insufficient; `R=Max(C)` may empty the interface; probes blocked | Chair dossier / Wave 1 roles | CONFIRMED |
| `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §9.5: `IdealEnd` ambient selection, `ChainEnd` cofinal direction, `RelationalHorizon` finite interface, no classical-horizon recovery | Logic / mathematician | CONFIRMED |
| Physical caveat: finite C1 interface is not an event horizon or reconstruction claim (`dev/PR003_C1_RELATIONAL_SPEC.md` §§1, 8; `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §9.5) | Physicist | CONFIRMED |

- Notes: No new external literature claims were introduced. I verified internal file anchors only. Runtime pass/build claims are marked `UNVERIFIED` because this Wave 2 role was read-only and did not run tests, validation, probes, or builds.

## 8. Synthesis
Recommended direction: **proceed only with a scoped negative preflight**, not with a C1 signal
implementation and not with any BH/MINK probe.

All four expert roles converged on the same structural point: in a finite nonempty poset,
`down(Max(C)) = C`, so the current written `R=Max(C)` draft makes `B_R = ∅` and
`H[C;R] = ∅`. The physicist and mathematician both say this is stronger than "wall-coupled":
the current reference rule is interface-killing. The logician adds that treating empty
`H[C;R]` as a physical failure/success would be a category mistake. The falsifier warns that a
passing Guard-v could create false confidence unless it is explicitly framed as proving the draft
trivializes.

Open disagreement is narrow: reproducibility and warden allow a preflight implementation, while
falsifier warns against engineering weight. The chair resolves this by narrowing the allowed
preflight to a **negative guardrail artefact**: implement only enough to prove/lock
`R=Max(C) -> NO_INTERFACE` on synthetic finite posets and relabel-conjugacy. Do not implement
asymmetry, persistence thresholds, bulk controls, BH/MINK comparisons, dev-seed measurements, or
fallback selectors.

Ranked alternatives:
- `ALLOW_PREFLIGHT_IMPLEMENTATION_ONLY`, scoped to negative synthetic tests proving this C1 draft
  trivializes: **recommended**.
- `REVISE_C1_SPEC_FIRST`: acceptable but less useful; the negative preflight can harden the
  reason for revision.
- `DO_NOT_PROCEED_WITH_C1_DRAFT`: too strong if it blocks documenting the failure mechanically;
  correct if anyone tries to treat the current draft as a signal candidate.

## 9. Next-step spec
Reversible steps allowed now, if the user authorises them:
- Add `nachocausal/c1_selector.py` implementing only the current selector contract:
  `{"R": set[element], "interface": set[(element, element)]}` for `R=Max(C)`.
- Add `tests/test_c1_selector.py` using hand-built finite posets only. The key assertion is:
  `R=Max(C)`, `A_R=C`, `B_R=empty`, `interface=empty`, and status/interpretation
  `NO_INTERFACE`.
- Add a Guard-v test:
  `verify_selection_order_only(C, c1_selector, seed=s)` on synthetic posets.
- Keep the test names and docstrings explicit that this is a **negative preflight** demonstrating
  the current C1 reference draft trivializes.

Forbidden until a new committee/audit step:
- Any BH/MINK scoring or generated data probe.
- Any dev-seed or validation-seed measurement.
- Any asymmetry score, persistence threshold, bulk/wall control, fallback selector, near-maximal
  layer selector, or alternate `R`.
- Any promotion/freeze/preregistration of C1.

Binding rules: `NO_POST_HOC_TUNING`, `NO_GROUND_TRUTH_LEAKAGE`, `NO_RECONSTRUCTION_CLAIM`,
`NO_THRESHOLD_LOOSENING`, `RESPECT_SEAL_FREEZE`.

Minimal falsification test to implement in preflight: for several hand-built finite posets,
compute the current `R=Max(C)` selector and assert universal `NO_INTERFACE`. If any finite poset
returns a nonempty interface under the written definitions, the implementation is wrong.

## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
