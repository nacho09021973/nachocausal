# Comité Decision 008 — c1-relational-selection-guard

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question
Is the new C1 relational writing plus selection Guard-v sufficient to authorise a dev probe, or must
C1 be revised again before any data are run?

## 2. Verified state
- Branch: `main`; changes are local and uncommitted at the time of this brief.
- Lean check: `cd formal/HorizonFormal && . "$HOME/.elan/env" && lake build` ->
  `Build completed successfully (1448 jobs)`.
- Leak/selection tests: `.venv/bin/python -m pytest -q tests/test_selection_guard.py tests/test_leak.py`
  -> `5 passed in 0.19s`.
- New C1 spec: `dev/PR003_C1_RELATIONAL_SPEC.md` declares status "dev specification, no data, no
  freeze, no result" and explicitly leaves `ASYMMETRY_SCORE`, `PERSISTENCE_THRESHOLD`,
  `BULK_CONTROL`, `C1_PROMOTION`, and `PHYSICAL_INTERPRETATION` open.
- New executable guard: `nachocausal/selection_guard.py` verifies relabel-conjugacy of element
  selections. `tests/test_selection_guard.py` contains one passing order-only selector and one
  label-dependent selector that must raise.
- No validation command, seed draw, scoring run, `results/` write, or `thresholds.py` edit occurred.

## 3. Dossier
- `dev/PR003_C1_RELATIONAL_SPEC.md`
- `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §9.5
- `docs/pr003_leakage_gate.md`
- `nachocausal/selection_guard.py`
- `tests/test_selection_guard.py`
- `formal/HorizonFormal/HorizonFormal/{Horizon.lean,ChainEnds.lean}`
- Prior committee constraint: `docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md`
  (`REFINE_CANDIDATES_BEFORE_PROMOTION`)

## 4. Expert briefs (wave 1 — blind, parallel)
### Reproducibility engineer brief
The new selection Guard-v is a real executable guard: it has a positive test and a negative
can-fail test. It is scoped correctly to element-label selections and deliberately excludes scalar
scores. The C1 spec is doc-only and records open fields before data. Reproducibility blocker: no
actual `c1_selector` implementation exists yet, so the guard verifies the guard machinery, not C1
itself.

### Mathematician brief
The formal layering is coherent: `RelationalHorizon R` is the finite interface, `IdealEnd` selects
an ambient non-principal ideal only provisionally, and `ChainEnd` records cofinal direction inside
that ideal. The spec's choice `R=Max(C)` is order-defined and finite-poset available. Mathematical
blocker: with `R=Max(C)`, `A_R=down(R)` may collapse to all of `C` in many finite posets, making
`B_R` and `H[C;R]` empty. That is acceptable as a falsifiable draft, but not probe-ready until
the expected degeneracy and fallback rule are specified.

### Physicist brief
The spec keeps the correct physical boundary: finite apparent/trapping precursor only, never event
horizon or reconstruction. The maximal-element reference is likely dominated by the sampling wall,
so a positive C1 signal would be suspect unless the open bulk-control and asymmetry tests are
closed first. No Schwarzschild or metric claim is licensed by this wording.

## 5. Falsifier attack
- `R=Max(C)` is too wall-coupled. In a finite patch, every element may lie below some maximal
  element, causing `A_R=C`, `B_R=empty`, and `H[C;R]=empty`; a later fallback could become a
  post-hoc degree of freedom if not fixed now.
- `ASYMMETRY_SCORE` is explicitly open. Since asymmetry is the key discriminator against wall and
  persistent-density controls, C1 is not yet closed.
- `PERSISTENCE_THRESHOLD` is open. Running a probe before freezing this invites threshold tuning.
- The selection Guard-v is necessary but not sufficient: it can prove relabel-conjugacy, not
  physical relevance or wall-control.
- Minimal falsification test before any probe: implement `c1_selector(C)` and run
  `verify_selection_order_only(C, c1_selector)` on synthetic relabelled posets, including a case
  where `R=Max(C)` produces an empty interface. The expected behavior for empty interface must be
  fixed before results are inspected.

## 6. Pre-registration verdict
- Verdict: BLOCK for any probe or promotion.
- Reason: C1 still contains open load-bearing choices (`ASYMMETRY_SCORE`, `PERSISTENCE_THRESHOLD`,
  `BULK_CONTROL`) and no concrete C1 selector implementation exists.
- Freeze integrity: PASS. No frozen threshold, validation seed, scoring path, or sealed estimator
  was touched.

## 7. Literature verdict
No new external literature claim is introduced. The step is internal formal/specification work.
Existing literature and committee caveats from decisions 006/007 remain binding and are not
re-adjudicated here.

## 8. Synthesis
Recommended direction: revise C1 once more before any dev probe. The new spec and selection Guard-v
are progress, but not enough to proceed to data. The committee accepts the layering
`IdealEnd`/`ChainEnd`/`RelationalHorizon` as the right vocabulary bridge and accepts the new
selection guard as a necessary executable gate. It rejects probe execution until the open C1
degrees of freedom are closed in writing.

Ranked alternatives:
- Revise C1 before probe: recommended.
- Run a probe now using `R=Max(C)` and open asymmetry/persistence choices: rejected as post-hoc
  tuning risk.
- Promote C1 as project axis: rejected; violates committee-006 sequencing.

## 9. Next-step spec
Reversible steps allowed now:
- Implement a pure `c1_selector(C)` that returns only `{"R": set[element], "interface": set[(x,y)]}`.
- Specify the empty-interface behavior and whether `R=Max(C)` is retained, refined, or replaced by
  a dynamic relational reference.
- Close `ASYMMETRY_SCORE`, `PERSISTENCE_THRESHOLD`, and `BULK_CONTROL` in writing before any data.
- Extend tests so `verify_selection_order_only` guards the concrete `c1_selector`.

Committing steps requiring explicit user authorisation:
- Any dev probe on BH/MINK data.
- Any freeze/preregistration/promotion of C1.
- Any threshold selection after seeing probe output.

Binding rules: `NO_POST_HOC_TUNING`, `NO_GROUND_TRUTH_LEAKAGE`, `NO_RECONSTRUCTION_CLAIM`,
`NO_THRESHOLD_LOOSENING`, `RESPECT_SEAL_FREEZE`.

## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
