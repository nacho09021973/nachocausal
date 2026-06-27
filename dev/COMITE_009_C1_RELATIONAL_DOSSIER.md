# Dossier for Comité 009 — C1 relational closure before any probe

Status: **dossier draft, not a committee decision, no data, no freeze, no result**.

Use this file as the chair's dossier when invoking `/comite`. It frames one decision question and
collects the verified state and binding artefacts so the 7-role committee can deliberate from the
same record.

## Key Decision Question

Should the project revise C1 again before any implementation/probe, or may it proceed with a
strictly reversible **preflight implementation only** of `c1_selector(C)` and its Guard-v tests,
with no BH/MINK scoring, no dev-seed measurement, no threshold choice, and no promotion/freeze?

The committee should decide one of:

1. `REVISE_C1_SPEC_FIRST`: do not implement yet; close `R`, empty-interface behavior,
   `ASYMMETRY_SCORE`, `PERSISTENCE_THRESHOLD`, and `BULK_CONTROL` further in writing.
2. `ALLOW_PREFLIGHT_IMPLEMENTATION_ONLY`: implement `c1_selector(C)` and synthetic/relabel tests
   only; still forbid BH/MINK probes and threshold selection.
3. `DO_NOT_PROCEED_WITH_C1_DRAFT`: reject the `R=Max(C)` draft as structurally wall-dominated and
   require a different relational reference construction.

Recommended chair framing: `ALLOW_PREFLIGHT_IMPLEMENTATION_ONLY` only if the committee accepts that
the implementation is a guardrail exercise, not a data probe. Otherwise choose
`REVISE_C1_SPEC_FIRST`.

## Verified State For Chair

- Working tree, ignoring submodule internals: `git status --short --ignore-submodules=all` produced
  no output after commit `b9da25a`.
- Recent commits:
  - `b9da25a comite: add mathematical logic role`
  - `c287f61 pr003: add C1 selection guard and committee review`
  - `16de06d formal: relate chain ends to generated lower sets`
- Seal check: `make verify-seal` ->
  `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- No validation command, seed draw, scoring run, `results/` write, or `thresholds.py` edit is part
  of this dossier.

## Dossier Files

- `dev/PR003_C1_RELATIONAL_SPEC.md`
- `docs/comite/comite_decision_008_c1-relational-selection-guard.md`
- `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` §9.5
- `docs/pr003_leakage_gate.md`
- `nachocausal/selection_guard.py`
- `tests/test_selection_guard.py`
- `formal/HorizonFormal/HorizonFormal/Horizon.lean`
- `formal/HorizonFormal/HorizonFormal/ChainEnds.lean`
- `docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md`
- `docs/comite/comite_decision_008_c1-relational-selection-guard.md`

## Current C1 Draft Facts

- The C1 spec declares itself "dev specification, no data, no freeze, no result" and explicitly says
  it does not promote C1, authorise a probe, touch the sealed estimator, or claim reconstruction
  (`dev/PR003_C1_RELATIONAL_SPEC.md:3-8`).
- Input is only a finite causal poset via boolean past matrix `C`; no embedding, coordinates, `r`,
  `t`, Schwarzschild labels, or scoring module may enter (`dev/PR003_C1_RELATIONAL_SPEC.md:10-14`).
- C1 is framed through `H[C;R]`, with `A_R=down(R)` and `B_R=C\A_R`
  (`dev/PR003_C1_RELATIONAL_SPEC.md:16-31`).
- Current closed reference rule is `R(C)=Max(C)` (`dev/PR003_C1_RELATIONAL_SPEC.md:33-39`).
- The spec itself flags the wall risk: maximal elements are strongly coupled to the sampling wall
  (`dev/PR003_C1_RELATIONAL_SPEC.md:49-51`).
- If `H[C;R]` is empty, C1 returns `NO_INTERFACE`, not a physical success/failure
  (`dev/PR003_C1_RELATIONAL_SPEC.md:63-68`).
- Persistence is defined as maximal consecutive run of nonempty interface levels, but no threshold
  is fixed (`dev/PR003_C1_RELATIONAL_SPEC.md:70-97`).
- Asymmetry is not frozen: `ASYMMETRY_SCORE = OPEN`
  (`dev/PR003_C1_RELATIONAL_SPEC.md:99-114`).
- Explicit open items are `ASYMMETRY_SCORE`, `PERSISTENCE_THRESHOLD`, `BULK_CONTROL`,
  `C1_PROMOTION`, and `PHYSICAL_INTERPRETATION`
  (`dev/PR003_C1_RELATIONAL_SPEC.md:147-155`).

## Committee 008 Constraints

- Committee 008 asked whether the new C1 relational writing plus selection Guard-v was enough to
  authorise a dev probe (`docs/comite/comite_decision_008_c1-relational-selection-guard.md:9-11`).
- It found the new guard necessary but not enough: no concrete `c1_selector` implementation existed
  (`docs/comite/comite_decision_008_c1-relational-selection-guard.md:37-43`).
- It flagged a core mathematical blocker: with `R=Max(C)`, `A_R=down(R)` may collapse to all of
  `C`, making `B_R` and `H[C;R]` empty
  (`docs/comite/comite_decision_008_c1-relational-selection-guard.md:45-51`).
- It blocked any probe/promotion because load-bearing choices remain open:
  `ASYMMETRY_SCORE`, `PERSISTENCE_THRESHOLD`, `BULK_CONTROL`, and no concrete selector
  (`docs/comite/comite_decision_008_c1-relational-selection-guard.md:73-78`).
- It allowed reversible next steps: implement pure `c1_selector(C)`, specify empty-interface
  behavior, decide whether to retain/replace `R=Max(C)`, close open scores/controls, and extend
  tests (`docs/comite/comite_decision_008_c1-relational-selection-guard.md:98-104`).

## Guard-v Selection State

- `verify_selection_order_only` checks a selector under random relabelling and raises if selected
  element labels do not relabel-conjugate exactly (`nachocausal/selection_guard.py:52-84`).
- Selector output must be element labels such as `{"R": {...}, "interface": {(..., ...)}}`;
  scalar scores should be guarded separately as observables (`nachocausal/selection_guard.py:57-63`).
- The leakage gate now names this executable selection guard and its can-fail test
  (`docs/pr003_leakage_gate.md:45-53`).

## Formal Vocabulary Bridge

- `IdealEnd` is provisional ambient escape/end selection, not a physical escape end or asymptotic
  boundary (`dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md:229-234`).
- `ChainEnd` represents cofinal direction inside a selected ambient ideal, and coexists with
  `IdealEnd` rather than replacing it (`dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md:236-243`).
- `RelationalHorizon R` supplies the finite interface and Lean proves only structural guardrails,
  not classical horizon recovery (`dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md:245-253`).
- The C1 reading after the Lean bridge still says the selection rule for `R` and any C1
  antichain/flux comparator remains open and must be closed before a dev probe
  (`dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md:255-262`).

## Binding Guardrails For The Committee

- No dev probe, BH/MINK comparison, scoring run, threshold selection, or seed use is authorised by
  this dossier.
- The hidden embedding may score only after a blind construction; it may not define `R`,
  interface selection, antichain selection, argmin/argmax, persistence, or asymmetry.
- `NO_POST_HOC_TUNING`: any threshold or comparator must be fixed before data.
- `NO_GROUND_TRUTH_LEAKAGE`: selectors must pass `verify_selection_order_only`.
- `NO_RECONSTRUCTION_CLAIM`: C1 is at most a finite apparent/trapping precursor.
- `NO_THRESHOLD_LOOSENING`: no change to `K_LOC`, `theta_*`, `P_PERM_THRESHOLD`, or any sealed
  quantity.
- `RESPECT_SEAL_FREEZE`: seal remains `6e2c3888...`; recheck in the actual committee session.

## Specific Questions For Each Role

- **Reproducibility engineer:** Is a `c1_selector(C)` preflight implementation with synthetic and
  relabel tests reversible enough to allow now, or does it risk silently becoming a probe?
- **Causal-set mathematician:** Is `R=Max(C)` mathematically too degenerate for finite posets, and
  can the `NO_INTERFACE` behavior be accepted as a falsifiable draft?
- **Mathematical logician:** Are the object types and quantifier order coherent: choose `R` ->
  build `H[C;R]` -> derive persistence/asymmetry -> only then score? Are any iff/equality claims
  overused beyond Lean?
- **Physicist:** Does `R=Max(C)` collapse C1 into a sampling-wall detector even before data?
- **Falsifier:** What is the minimal synthetic/relabel test that would expose the worst failure
  without using BH/MINK data?
- **Pre-registration warden:** Does any proposed preflight step risk threshold tuning or a covert
  prereg/probe?
- **Literature verifier:** Are any new literature claims introduced? If not, mark as internal
  formal/spec work.
