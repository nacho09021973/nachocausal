# Comité Decision 038 — truncated-futures-freeze-adjudication

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

¿Debe el comité autorizar la operación atómica de congelación del contrato
`docs/preregistration_square_box_truncated_futures_localization_draft.md` (SQUARE_BOX_2P4
Truncated-Futures Boundary-Localization) — cambio de estado a `FROZEN`, sellado con hash, commit a
git, y actualización controlada de `manifest.json`/`claim_ledger.md`/`terminal.txt` en
`evidence/square_box_truncated_futures_localization_20260719/` — antes de cualquier ejecución de
semillas confirmatorias (`TRUNC_FUT_EVAL_SEEDS = 4_600_000..4_600_031`)?

This question arrived at `/comite` after an iterative, multi-round PI review of the draft's
statistical design (rank formulas, sign test, `alpha`/`EFFECT_FLOOR`/`N_PAIR_MIN`/`MIN_N`
adjudication) already closed with the PI's own verdict `PREREGISTRATION_REVIEW_PASS /
READY_TO_FREEZE`. Per the PI's own framing in-session, that verdict is entry evidence for this
committee, not a substitute for it — `/comite` is the reserved venue for authorizing this
specific one-way act.

## 2. Verified state

Facts checked this session (chair, read-only); full trail in
`docs/auditor/auditor_report_021_truncated-futures-freeze-preflight.md` (`AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS`,
0 errors, 24 warnings, run ahead of this committee per the skill's "new prereg" trigger rule):

- Target file: `docs/preregistration_square_box_truncated_futures_localization_draft.md` (1142
  lines). Status line (top and bottom, both checked): `DRAFT_FOR_PI_REVIEW /
  READY_FOR_FINAL_PREREGISTRATION_REVIEW / NO_DATA_GENERATED`. Untracked in git
  (`git status --short`), no commit, no data generated.
- `make verify-seal` == `sha256sum nachocausal/thresholds.py` ==
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching the recorded
  prereg-002 seal (`docs/preregistration_003.md:9`). The draft references/modifies
  `nachocausal/thresholds.py` in 0 places.
- `bash .claude/skills/auditor/audit.sh` => 0 errors, 22 warnings, all pre-existing and unrelated
  (`data/reports/*.csv` from older PR004/PR005/PR011 tracks).
- Cited prior sealed result `BH_MINK_DISPERSION_DIFFERENCE_DETECTED` is real:
  `evidence/new_geometry_20260719/terminal.txt` and `RESULT_SEALED.txt` both confirm it, matching
  `docs/new_geometry_future_observables_addendum.md:12-18`.
- `evidence/square_box_truncated_futures_localization_20260719/` already exists (pre-dates this
  session, 2026-07-19) with `manifest.json`/`claim_ledger.md`/`terminal.txt` only —
  `terminal.txt`=`DRAFT_FOR_PI_REVIEW_NO_EVALUATION_RUN`, `manifest.json`
  `"evaluation_status":"NOT_RUN"`, no CSV/summary/seal file. Benign, but **stale**: does not
  mention `alpha_FWER`/`EFFECT_FLOOR`/`N_PAIR_MIN`/`MIN_N`/edge-control/synergy content added
  across this session (auditor finding 5).
- The whole 2026-07-19 SQUARE_BOX_2P4 cluster — including `docs/preregistration_square_box_boundary_localization.md`
  (already textually "## CONTRACT FROZEN") and `docs/new_geometry_future_observables_addendum.md`
  (`STATUS: SEALED_RESULT_ADDENDUM`) — is uncommitted to git (auditor finding 6). Two documents
  already asserting frozen/sealed status in prose have never been committed.
- `grep -n "RANDOM_CONTROL_SALT" docs/preregistration_square_box_truncated_futures_localization_draft.md`
  confirms the literal is unassigned (draft §11.3, §18) — verified independently by three Wave-1
  roles and both Wave-2 controls (below).
- No `Makefile` target exists to re-verify a document-text hash; `verify-seal` is hardcoded to
  `nachocausal/thresholds.py` (`Makefile:15-17`). No sibling contract used a document-hash seal —
  `docs/preregistration_square_box_boundary_localization.md` froze via a `STATUS: CONTRACT_FROZEN`
  header block, no hash (verified by reproducibility engineer and pre-registration warden,
  independently).

## 3. Dossier

Files and references supplied to the committee (full text in
`/tmp/claude-1000/-home-adnac-nachocausal/39dc3e8f-7ee5-496e-87e8-da5ce6f6bf4f/scratchpad/dossier_wave2.txt`,
a chair-authored working file, not part of the repo):

- `docs/preregistration_square_box_truncated_futures_localization_draft.md` — the object of the
  decision.
- `docs/preregistration_square_box_boundary_localization.md`, `docs/new_geometry_future_observables_addendum.md`,
  `docs/preregistration_new_geometry_future_observables.md` — sibling/motivating contracts.
- `docs/auditor/auditor_report_021_truncated-futures-freeze-preflight.md` — this session's
  preflight audit.
- `nachocausal/thresholds.py`, `nachocausal/generator.py`, `nachocausal/c1_selector.py:48-61` —
  sealed instrument and cited code conventions.
- `dev/run_new_geometry_future_observables.py:174-187,270-284` — cited `L(i)` convention and the
  sign-flip test this draft explicitly does not reuse.
- `evidence/square_box_truncated_futures_localization_20260719/`, `evidence/new_geometry_20260719/`
  — draft-stage scaffold and real sealed evidence.
- `CLAUDE.md`, `docs/preregistration.md` — founding rules and master frozen prereg-001.
- `biblioteca/`: Eichhorn–Gamito–Stokes arXiv:2605.06813, Bombelli 1987 PhD, `Anticadenas_Benincasa.md`
  (all citations independently confirmed, §7 below).

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

- Proposed artefact(s): The freeze operation itself touches four already-existing,
  currently-untracked paths — no new run artefacts are produced by *freezing*. (a)
  `docs/preregistration_square_box_truncated_futures_localization_draft.md` (1142 lines; status
  line flips `DRAFT_FOR_PI_REVIEW → FROZEN`). Note the filename still carries `_draft` — the
  sibling frozen contract `docs/preregistration_square_box_boundary_localization.md` kept its
  non-`_draft` name and froze via a `STATUS: CONTRACT_FROZEN` + `FROZEN_BY`/`FROZEN_DATE` header
  block (`docs/preregistration_square_box_boundary_localization.md:3-5,343-345`), so a
  rename-vs-keep decision is unresolved and should be made explicit at freeze. (b)
  `evidence/square_box_truncated_futures_localization_20260719/{manifest.json,claim_ledger.md,terminal.txt}`
  — updated from the stale `2026-07-19` scaffold (`manifest.json` currently
  `"status":"DRAFT_FOR_PI_REVIEW_NO_EVALUATION_RUN"`, `"evaluation_status":"NOT_RUN"`,
  `terminal.txt`=`DRAFT_FOR_PI_REVIEW_NO_EVALUATION_RUN`, verified this session). The seven
  run-output files the contract requires (`per_seed_localization.csv`, `evaluation_summary.json`,
  `evaluation_report.md`, `RESULT_SEALED.txt`, per draft §17:1035-1041) MUST NOT appear at freeze
  — their absence is the machine-checkable proof that `RESPECT_SEAL_FREEZE` / no-data-before-freeze
  holds.
- Environment & seal: Validation path is pure numpy pinned `numpy==1.26.4` (`Makefile:2-3`,
  `nachocausal/generator.py:3` "PURE NUMPY"). The frozen instrument `nachocausal/thresholds.py`
  re-verifies clean this session: SHA256 == `6e2c3888…fefd4`, matching `make verify-seal` and the
  recorded prereg-002 seal. This draft references/modifies `thresholds.py` in 0 places — freezing
  the document does not perturb the sealed instrument, and there is no new code/threshold seal
  constant to register. The external Minz clone (`CLAUDE.md:27-29`) is dev-only, not on the sealed
  path, not required to freeze.
- Provenance capture: (1) the git commit SHA that first tracks all four files — currently the
  ENTIRE `2026-07-19` cluster is untracked, so freeze is also the first commit of two documents
  whose prose already asserts FROZEN/SEALED. (2) If a document-hash seal is adopted, the SHA256 of
  the final draft text — but flag: **no precedent constant exists** for hashing a prereg
  *document's* own body; this is a new mechanism, not an inherited one `[UNVERIFIED — mechanism
  not defined in repo]`. (3) For the later run: `pip freeze`, `uname -a`, seed band
  `TRUNC_FUT_EVAL_SEEDS = 4_600_000..4_600_031`, `TRUNC_FUT_PRIMARY_INTENSITY = 9600.0`, and the
  pinned `RANDOM_CONTROL_SALT` literal — currently unassigned, a freeze-blocking gap.
- Run mechanics: This step is a reversible, non-committing metadata + first-commit operation,
  cleanly separable from the confirmatory run per the draft's own §13 development-gate language. A
  guard can abort cleanly because freeze runs no seeds and generates no data: the pre-flight
  assertion is "the §17 run-output files do not exist AND `git status` shows no
  `evidence/**/*.csv|*_summary.json|RESULT_SEALED.txt`." Recommend: freeze as its own atomic
  commit, do NOT chain the run into the same invocation — that would collapse the §13 gate.
- Reproducibility risks / ambiguities: `RANDOM_CONTROL_SALT` literal not yet pinned (freeze-
  blocking for the random-uniform arm's bit-reproducibility); document-hash seal has no repo
  precedent and no re-verification target (an unverifiable seal is decoration); stale evidence
  scaffold must be rewritten with the *current* PI-adjudicated parameters or provenance points at
  superseded content; `_draft` filename-vs-frozen-status is a provenance smell, reversible;
  observation-channel dependency (`numpy_sprinkle`/`past_matrix_fast`) is sound and on the sealed
  path.

### Mathematician brief

- Computability: Every quantity the selector consumes is a decidable function of the partial-order
  matrix `C` alone — `Min(C)`, `V(i)`, `L(i)` (memoised longest-future-chain recursion,
  `dev/run_new_geometry_future_observables.py:174-187,221,223`). Ranks, `T(i)`, the
  top-`k_floor`/`k_cap` selection, and the tie-expand-or-abstain rule (draft §7.1-§7.2) are all
  within-realization order operations — no `(t,r)`, `R_S`, or kind label enters selection
  (`NO_GROUND_TRUTH_LEAKAGE` holds at the order level). The `m=1` totality convention in §7.1 is
  provably unreachable under the `m≥8` gate — a well-definedness placeholder, not a live branch.
  `Min(C)` is provably an antichain (irreflexivity enforced,
  `nachocausal/generator.py:128`) — correct, and this is exactly why §9.1 must reach outside the
  order (to coordinates) for its edge diagnostic rather than to a relation *between* minimals.
- Order observable: `L(i)`/`V(i)` are precisely the Eichhorn–Gamito–Stokes §III bimodality
  diagnostic (quote reproduced, `biblioteca/derived-md/Towards black-hole horizons and geodesic
  focusing in causal sets.md:181-191`, Fig. 3 lower panel for `V`). The bivariate `T` is a
  defensible order-only combination of the two.
- Relevant invariants: future-volume/interval cardinality, longest-chain/height as proper-time
  proxy, ordering fraction, interval-abundance series `C_k` — cited as the surrounding order-
  invariant family, not smuggled into selection.
- Analytic / continuum target: the discrete `L` should approach the longest continuum proper time
  to the future of a minimal point, bounded inside `r=R_S`; the honest continuum target is a
  finite-patch truncation transition, not the true event horizon — "to define an event horizon in
  a causal set, an infinite sprinkling is required" (paper:173-175), directly underwriting the
  draft's own `NO_RECONSTRUCTION_CLAIM` scope.
- Caveats: transitivity of `C` is *assumed*, not enforced in code (`past_matrix_fast` computes the
  relation directly, no explicit transitive-closure step) — the §6.2 cover-recursion equivalence
  holds only if `C` is genuinely transitive, true for a faithful sprinkling but not
  matrix-guaranteed; worth an implementation-time assertion, not a freeze blocker. The
  `L_elements = L_links + 1` bridge is documentation-only and matches the repo convention, no
  ambiguity. `RANDOM_CONTROL_SALT` (§11.3) is the one genuinely open determinism parameter — per
  the draft's own §18 it must be pinned *at* freeze. The §9.1 open question (no non-circular
  order-only edge-proxy identified) is correctly scoped as research-open, not a theorem, and does
  not block freeze.

### Mathematical logic brief

- Formal status: the draft states one genuine elementary theorem (`Min(C)` is an antichain, §6),
  correctly argued in prose but not formalised anywhere in `formal/HorizonFormal/` (grep for
  `antichain`/`minimal`/`Min` returns zero hits — those Lean modules prove lemmas about a
  *different* object, `RelationalHorizon` as a `Set (P × P)` of crossing links, unrelated to this
  draft's machinery). §1.1/§10/§12 are correctly labelled definitions of a decision procedure plus
  a falsifiable hypothesis, never dressed as theorems. The reachability arithmetic (§12) was
  hand-verified: `P(Bin(13,½)≥12)≈1.71e-3≤0.005`, `ceil(log2 200)=8`, `MIN_N=max(13,8)=13` —
  consistent.
- Quantifier / dependency order: clean and freeze-appropriate — select from the order alone, then
  reveal coordinates for scoring; every threshold is pinned before data; `MIN_N` can only raise the
  bar as `n_pair` grows, no post-hoc slack. The one residual post-hoc degree of freedom is
  `RANDOM_CONTROL_SALT`, explicitly unassigned — "a dangling ∃ in an otherwise fully-quantified
  contract."
- Equivalence claims: three, all prose-level and correctly not over-claimed as proofs (the cover-
  recursion equivalence, the element/link bridge, the `log2(d/alpha)` identity). The load-bearing
  non-equivalence claim — why the repo's sign-flip test's magnitude-symmetry does not transfer to
  comparing two deterministic selectors on one realization — is a semantic argument used
  conservatively (motivates the weaker, safer sign test). Logically clean.
- Type / object discipline: sound — element-set selector vs real-valued scoring function are kept
  type-distinct, cleanly enforcing "ground truth only scores." The shared word "horizon"/"boundary"
  between this draft (a set of elements) and the Lean corpus (a set of link-pairs) is a
  categorically different object in each; neither artefact claims equivalence, so no in-document
  category mistake, but the nomenclature overlap should not be read as Lean underwriting this
  localizer.
- Caveats: no logical obstruction to the status-change/seal/commit operation, provided the freeze
  does not silently promote the antichain/enumeration prose to "formally verified" status, and the
  unassigned salt is acknowledged as an open binding before freeze.

### Physicist brief

- Coordinates & patch: 1+1D Schwarzschild sprinkling, Eddington–Finkelstein/tortoise causal
  relation (`nachocausal/generator.py:104,116-127`), matching EGS eq. (7). Square finite patch
  (`T_EDGE=R_EDGE=2.4`, aspect 1.0, `r∈[0.1,2.5]`, `R_S=0.5`). Coordinate-uniform sampling equals
  natural-volume Poisson because the induced metric has constant determinant (EGS §II). Finiteness
  forfeits a true event horizon, which "requires an infinite sprinkling to define" — the draft
  respects this (§1: "candidate boundary band only; no global event-horizon claim").
- Physical meaning of the signal: `T(i)` targeting jointly low `L(i)`/`V(i)` among minimals is
  *precisely* the EGS §III bimodality diagnostic, mechanistically grounded in singularity-truncated
  futures inside `r=R_S`.
- Sprinkling domain: coordinate-uniform Poisson, same cloud for BH/MINK, marginal uniformity gate;
  primary intensity 9600 gives `ell≈0.0245`, so `R_S=0.5` sits ~16ℓ from the inner wall `r=0.1` —
  the interior region is a thin sliver against that wall. Per-seed `|Min(C)|` fluctuation is
  handled by the §8 abstention gate and §10's `26/32` support floor.
- Claim boundary: a `..._DETECTED` verdict claims only that an order-only band lands closer to
  hidden `r=R_S` than the same-cloud MINK control allows by chance, under frozen thresholds — not
  metric reconstruction, not a global/asymptotic horizon, not 3+1D. EGS's own regular-black-hole
  caveat (Hayward: the longest-chain partition "would no longer work") is correctly reflected in
  the draft's §1.1 refusal to read a pass as horizon-detection per se.
- Caveats (support-level risks, not freeze-blockers, correctly deferred to §13's dev-gate):
  square-box geometry is the *opposite* regime from EGS's tall-box demonstration, where the
  bimodal separation "becomes even more pronounced when we increase the timelike extent of the
  box" — this design's power is genuinely uncertain until the dev-gate runs. `V(i)` is explicitly
  more boundary-sensitive than `L(i)` per EGS's own text (causal-diamond `n` vs `√n` even in flat
  space) — the draft's co-equal weighting imports this sensitivity, mitigated but not eliminated by
  the MINK control and §9.1's edge diagnostic. The `R_S`-near-inner-wall proximity is the precise
  confound EGS raise (finite-set inability to separate singularity-near from infinity-near
  futureless points); the §9.1 edge control and conjunctive abandonment criterion 2 are physically
  appropriate mitigations. Freezing touches no instrument and generates no data; `RANDOM_CONTROL_SALT`
  has no bearing on the causal physics.

## 5. Falsifier attack

- Concrete failure modes: `RANDOM_CONTROL_SALT` unassigned at the moment freeze is requested,
  contradicting the draft's own §18 freeze gate — either freezing now violates the document's own
  stated criterion, or the salt gets assigned as part of "the freeze operation" with no visible
  review of that specific literal. The document-hash seal has no re-verification mechanism
  (`Makefile`'s `verify-seal` is hardcoded to `thresholds.py`; no sibling contract used a hash) — a
  seal nobody can `make verify-seal-*` and re-check is decoration. Filename/status inconsistency
  (`_draft` suffix on a `FROZEN` document, no repo precedent for that combination) risks future
  misreading. Stale evidence scaffold risk: if the "controlled update" is even slightly incomplete,
  the committed manifest could freeze a description of the contract that doesn't match the frozen
  document's own current §12/§16.1. Square-box power risk is baked in at freeze time, not caught by
  it — a real risk `TRUNC_FUT_EVAL_SEEDS` gets burned on an underpowered design if §13's dev-gate is
  skipped or under-read.
- Ground-truth leakage: none found *within* a single run's selection channel — order-only
  throughout, coordinates/`R_S` post-selection only, §9.1's edge diagnostic explicitly licensed as
  scoring-only. **Program-level point worth recording explicitly, not silently:** this is the third
  localizer design in this geometry lineage (R-VAR closed-negative → largest-gap dev-diagnostic
  landed far from `R_S` → this truncated-futures design), and the choice of *this* observable is
  explicitly motivated by the prior contract's dev-diagnostic outcome, itself computed by revealing
  hidden `R_S` on `dev/` seeds. Each individual freeze's thresholds are independently anchored (no
  single-contract violation), but across the sequence the PI is iteratively re-designing the
  observable in response to ground-truth-scored feedback from prior attempts — legitimate as long
  as it stays on `dev/`, but exactly the mechanism `NO_GROUND_TRUTH_LEAKAGE` exists to bound, and it
  is getting less visible as contract-generations accumulate. Should be acknowledged explicitly in
  the freeze record.
- Freeze violations: the ordering relationship between "freeze" and the §13 dev-only support check
  is not pinned in the contract text itself — it should say explicitly "no dev-seed evaluation may
  occur before this freeze commits," not rely on session memory that nothing has run yet. Freezing
  with `RANDOM_CONTROL_SALT` unbound is itself a soft threshold-loosening path — an integer chosen
  at the freeze moment with no documented, run-independent derivation shown in the diff is one
  un-reviewed degree of freedom smuggled through the commit meant to close all such degrees of
  freedom. No virgin-seed burn: `TRUNC_FUT_EVAL_SEEDS` verified disjoint from every excluded range;
  freezing itself draws no seeds.
- Verdict coercion: none within the §16/§16.1 terminal-computation logic itself (rigorous,
  deterministic, mutually exclusive, contract-tier terminals correctly barred from being scientific
  negatives). Structural point for downstream reporting: §16's primary terminal and §16.1's synergy
  terminal can diverge (`T` "localizes" per §10 alone while adding nothing over `low-L` per §16.1)
  — any future summary/addendum of this contract's results must co-state both terminals in the same
  sentence, never cite `..._DETECTED` alone, or a technically-compliant future document could still
  create a false impression of a validated *combined* observable.
- Premature / over-broad claims: none in the frozen text — §1/§1.1 correctly exclude all
  over-claims and pre-commit to four alternative explanations a pass must distinguish. Worth
  recording plainly (not each time individually filed as "not a reopening"): three successive
  negative/inconclusive localizer attempts in this same geometry is itself information the freeze
  record should state.
- Independent-falsification gate: **not satisfied as currently scoped.** No procedural commitment
  anywhere in §13/§16/§17 requires an independent auditor pass on the eventual confirmatory
  `evaluation_summary.json`/`RESULT_SEALED.txt` before the terminal is treated as final — the same
  session that runs the evaluation could in principle also certify it. Does not block freezing the
  *design*, but should be added as a condition before any future confirmatory terminal is treated
  as settled.
- Minimal falsification test: `grep -n "RANDOM_CONTROL_SALT" docs/preregistration_square_box_truncated_futures_localization_draft.md`
  — if this still returns "not yet assigned"/"TBD" *after* the freeze commit, the freeze
  contradicts the draft's own §18 freeze gate and should be rejected on that basis alone. Binary,
  immediate, read-only, no seed execution required.

## 6. Pre-registration verdict

**Verdict: BLOCK**

- Freeze status: not yet complete by the document's own definition. §18 itself lists items that
  "must close before `FROZEN`, per PI instruction" that are **not** included in the operation
  described in the decision question: `RANDOM_CONTROL_SALT` (§11.3) "is not yet assigned a literal
  value" (draft:1129, echoed :570), and "final literal review... contract sealing, and controlled
  update of the `evidence/…/` scaffolding... none of these has happened yet" (draft:1130-1133).
  Authorizing the operation as worded would freeze a contract that still contains an unbound RNG
  parameter for one confirmatory arm. Per `docs/preregistration.md:66-67` ("Thresholds frozen in
  writing before any validation seed is generated/analysed"), a frozen contract must be fully
  literal before freeze, not partially literal with a promise to fill the gap later.
- Seal integrity: the existing sealed instrument (`thresholds.py`, `6e2c3888…fefd4`) is untouched
  and intact — `RESPECT_SEAL_FREEZE` holds for the existing chain. But the proposed *new* seal
  mechanism ("sellado con hash" of the draft document itself) has no precedent and no
  re-verification target in this repo — every prior seal in the chain is a git-commit SHA over a
  code/threshold file, re-checkable via `make verify-seal`. This draft defines no code file, so a
  document-text SHA256 with no `Makefile` recipe would be an unverifiable, decorative seal.
  Recommend the freezing **git commit SHA** itself serve as the seal, matching the established
  pattern, not an ad hoc hash of the markdown body.
- Seed discipline: sound and freeze-appropriate. `TRUNC_FUT_DEV_SEEDS`/`TRUNC_FUT_EVAL_SEEDS`
  explicitly checked disjoint, in writing, against every prior seed band in the project's history.
  No reserved virgin band burned — freezing draws no seeds at all.
- Reporting rule: sound as written. Two independent, deterministic, mutually-exclusive terminal
  procedures (§16, §16.1) are pre-committed, with contract/design terminals explicitly barred from
  being reported as scientific negatives — consistent with the project's "report alike" binding
  rule. "No threshold may be changed after evaluation" is stated verbatim.
- Forbidden moves present? None in the *design* itself — no post-hoc tuning, no ground-truth
  leakage, no reconstruction over-claim. But authorizing this specific atomic freeze operation *as
  worded* would itself be a procedural violation: it would flip the document to `FROZEN` while its
  own §18 explicitly says the operation is not yet closeable.
- Reasons: `draft.md:1129` (salt unassigned); `draft.md:1130-1133` (draft's own text says sealing/
  review hasn't happened); no precedent anywhere in the seal chain for a document-hash seal. The
  block is narrow and mechanically closeable: (1) pin `RANDOM_CONTROL_SALT` to a literal integer in
  the same commit, chosen independent of any run output (none exists yet, so this cannot leak
  ground truth or tune to a result); (2) adopt the freezing git-commit SHA as the seal, per
  established precedent, instead of an ad hoc document hash. Neither fix touches
  `nachocausal/thresholds.py` or any threshold value.

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| `Anticadenas_Benincasa.md:45` (isolated antichain: cardinality only, no internal metric/structure) | Mathematician | CONFIRMED |
| `Anticadenas_Benincasa.md:54` (cardinality = Lorentz-invariant discrete volume) | Mathematician | CONFIRMED |
| `Anticadenas_Benincasa.md:119` (interval-abundance / BD-action inputs) | Mathematician | CONFIRMED (document labels N₂/N₃, substantively the same as cited "C₂,C₃") |
| `Bombelli_1987_PhD.md:234` ('t Hooft: metric distance from causal structure + volume) | Mathematician | CONFIRMED — verbatim |
| Myrheim 1978 (no biblioteca path given) | Mathematician | **UNVERIFIED** — no such document exists anywhere in `biblioteca/`; joint citation with Bombelli, unanchored on its own |
| EGS `...md:181-188` (bimodal L-transition quote) | Mathematician, Physicist | CONFIRMED — near-verbatim |
| EGS `...md:150,186-188` (Fig. 1/Fig. 3 captions) | Mathematician | CONFIRMED |
| EGS `...md:173-175` (infinite sprinkling required for event horizon) | Mathematician, Physicist | CONFIRMED — verbatim |
| EGS `...md:145` (eq. 7, outgoing null geodesic) | Physicist | CONFIRMED |
| EGS `...md:135` (§II constant determinant ⇒ coordinate-uniform sprinkling) | Physicist | CONFIRMED for the substantive point; the specific "det g = -1" numeric value is a minor unverified embellishment — paper only states "constant determinant" |
| EGS `...md:171` (§III title, local diagnostics) | Physicist | CONFIRMED |
| EGS `...md:183` (footnote 3, Penrose-diagram alternative) | Physicist | CONFIRMED |
| EGS `...md:191` (bimodal distribution extractable without coordinates) | Physicist | CONFIRMED — verbatim |
| EGS `...md:193` (V(i) more boundary-sensitive; causal-diamond n vs √n) | Mathematician, Physicist | CONFIRMED — verbatim |
| EGS `...md:128` (1+1D toy rationale) | Physicist | CONFIRMED |
| EGS `...md:195` (regular/Hayward black holes: diagnostic fails) | Physicist | CONFIRMED |
| EGS `...md:188-191` ("jump becomes even more pronounced" with larger timelike extent) | Physicist | CONFIRMED — verbatim |
| "Surya §4 (LRR 2019)" (listed in chair's dossier framing, not actually invoked in either Wave-1 body text) | Chair (dossier), not attributed to any role's actual claim | **UNCONFIRMED / WITHDRAWN** — no such document exists in `biblioteca/`; this was the chair's own dossier-authoring imprecision, not a false claim by an expert. Corrected here: neither the mathematician nor the physicist actually cited Surya in their delivered briefs. |

- Notes: All in-brief `biblioteca/` citations from the mathematician and physicist roles check out
  against the actual source text, including verbatim quotes — strong anchoring throughout. Two
  soft issues, both minor and non-load-bearing: "Myrheim 1978" has no locatable artifact (mark
  `[UNVERIFIED]`, drop from any future citation of this brief without a real path); the physicist's
  "det g = -1" slightly overspecifies EGS §II (substantive point still holds). The chair's own
  dossier listed a Surya LRR reference that does not exist in `biblioteca/` — flagged and withdrawn
  here rather than silently dropped, per the anchoring mandate applying to the chair too.

## 8. Synthesis

**Recommended direction: do not authorize the freeze as worded. Close two narrow, mechanically
simple gaps in the same draft file first, then re-submit for freeze authorization.**

The design itself is in strong shape. Four independent Wave-1 experts and both Wave-2 controls
converge without contradiction: the observable (`L`/`V` on minimal elements) is exactly the
Eichhorn–Gamito–Stokes §III diagnostic (literature-verified verbatim), the order-only/scoring-only
separation is real and enforced (no leakage found by mathematician, logician, or falsifier), the
statistical machinery (sign test, `alpha_FWER`/`EFFECT_FLOOR`/`N_PAIR_MIN`/`MIN_N` reachability) is
internally consistent and independently hand-verified by the logician, the claim boundary is
correctly scoped against the paper's own stated limits (physicist), and seed discipline is sound
(warden). Two Wave-1 physical-power caveats (square box vs. EGS's tall-box regime; `V(i)`'s greater
boundary-sensitivity) are real but are exactly what the draft's own §13 dev-gate exists to surface
post-freeze without threshold tuning — they are not reasons to withhold freeze authorization, they
are reasons to actually run that dev-gate attentively once frozen.

**But per this skill's own rule, a pre-registration `BLOCK` forecloses a PROCEED verdict, and this
BLOCK is real, not a formality.** The pre-registration warden and the falsifier — working
independently, one from the frozen-contract lineage, one from an adversarial read of the same
text — converged on the identical finding: `docs/preregistration_square_box_truncated_futures_localization_draft.md`'s
own §18 explicitly states "must close before `FROZEN`" for (a) the `RANDOM_CONTROL_SALT` literal
and (b) "final literal review, contract sealing, and controlled update" — and the freeze operation
as posed to this committee did not include closing either. Three of four Wave-1 experts
(reproducibility engineer, causet mathematician, mathematical logician) independently flagged the
salt gap too, without being asked to check it specifically. This is not a single dissenting voice
to override; it is the strongest form of convergent evidence this committee produces.

**No open disagreement to surface.** All seven roles agree on the direction (the design is sound,
freeze is appropriate once two gaps close); none recommended abandoning or substantially redesigning
the contract. The physicist's power-risk caveats and the falsifier's program-level leakage-visibility
point are not disagreements with the other roles — they are additional context correctly deferred to
post-freeze reporting discipline (§9 below), not reasons to withhold this specific authorization.

**Ranked alternatives:**
1. **(Recommended) Close the two BLOCK items as further draft edits — still reversible, no commit
   yet — then bring the freeze back for explicit user authorization.** Cheapest, cleanest, matches
   the warden's own "narrow and mechanically closeable" framing.
2. Authorize the freeze now and treat `RANDOM_CONTROL_SALT`/the seal mechanism as follow-up
   corrections in a second commit. **Rejected** — this is precisely the "explore then lock" pattern
   `RESPECT_SEAL_FREEZE` exists to forbid; a frozen document with an acknowledged open gap is not
   frozen by this project's own definition (`docs/preregistration.md:66-67`).
3. Redesign the observable or geometry in response to the physicist's power-risk caveats before
   freezing. **Not recommended** — those caveats are support-level, not design-invalidating; the
   physicist and falsifier both explicitly route them to the post-freeze §13 dev-gate, which exists
   for exactly this purpose without requiring a pre-freeze redesign.

## 9. Next-step spec

**Stage A — reversible (further edits to the same untracked draft file; matches the pattern of this
entire session; may proceed now if the user asks, still no commit, no freeze, no seeds):**

1. Pin `RANDOM_CONTROL_SALT` to a literal integer in §11.3, with a stated derivation that is
   independent of any run output (none exists yet, so any principled fixed constant is safe from
   ground-truth leakage) — e.g. a documented, arbitrary-but-fixed integer in the same style as
   other named constants in this contract, chosen and shown in the diff for review, not silently
   inserted.
2. Replace the "document-hash seal" concept in §17/§18 with the established repo pattern: state
   that **the freezing git commit's SHA is the seal**, with no separate document-hash mechanism
   (matching every other seal in the chain, all of which are git-commit-SHA-over-a-tracked-file,
   none of which are ad hoc text hashes). This removes a step that would otherwise be unverifiable.
3. Add one sentence to the contract (§13 or §18) making explicit: "No dev-seed evaluation may occur
   before this freeze commits" — closing the falsifier's ordering-ambiguity point cheaply.
4. Add one sentence recording the programmatic context transparently: this is the third localizer
   design in the SQUARE_BOX_2P4/tall-box lineage (R-VAR closed-negative → largest-gap dev-diagnostic
   inconclusive → this design), and its observable choice was motivated by the prior contract's
   dev-diagnostic outcome — not a leakage violation on its own, but worth stating plainly per the
   falsifier's program-level point, rather than filed silently as "not a reopening" each time.
5. Add a reporting condition (§14 or a new subsection): any future summary/addendum of this
   contract's results must co-state both the §16 primary-localization terminal and the §16.1
   synergy terminal together — never cite one without the other.
6. Decide and state the filename/status-header convention (keep `_draft` suffix with a status
   header, matching the sibling contract's precedent, vs. rename) — **this is a genuine fork only
   the user can decide**; the reproducibility engineer and falsifier both flagged it but neither
   argued strongly for one option, since the sibling precedent (keep name, add header) exists but a
   rename is also defensible.

**Stage B — committing (only on explicit, separate user authorization, after Stage A closes and the
minimal falsification test below passes):**

7. Run the falsifier's minimal falsification test: `grep -n "RANDOM_CONTROL_SALT"
   docs/preregistration_square_box_truncated_futures_localization_draft.md` — must show a literal
   integer, not "TBD"/"not yet assigned."
8. Flip the status line (top and bottom) to the FROZEN state, using whatever exact token the PI
   prefers (the sibling contract used `STATUS: CONTRACT_FROZEN` + a `## CONTRACT FROZEN` closing
   block — recommend matching that precedent for consistency).
9. Update `evidence/square_box_truncated_futures_localization_20260719/{manifest.json,claim_ledger.md,terminal.txt}`
   to reflect the *current* design content (§12's `alpha_FWER=0.01`/`EFFECT_FLOOR=1.0`/
   `N_PAIR_MIN=26`/`MIN_N` formula, §9.1's edge control, §16.1's synergy terminals) — not the stale
   2026-07-19 scaffold. This is exactly the "controlled update" the PI already scoped.
10. Commit the affected files (the draft, the evidence scaffold — and, per auditor finding 6, this
    is also the first opportunity to commit the other already-"frozen"/"sealed"-labeled siblings in
    the same cluster if the user wants that cleaned up in the same pass, though that is a separate
    decision not adjudicated by this brief).
11. **Do not** run `TRUNC_FUT_DEV_SEEDS` or `TRUNC_FUT_EVAL_SEEDS` as part of this commit or
    immediately after it in the same session-turn — per the draft's own §13 gate and the falsifier's
    ordering point, freezing and evaluating must be visibly separate acts.
12. Before any future confirmatory terminal (from a later, separately-authorized run) is treated as
    settled, an `/auditor` pass over the produced `evaluation_summary.json`/`RESULT_SEALED.txt`
    should certify it — closing the falsifier's independent-falsification-gate finding. This is a
    condition for a *future* step, not something to execute now.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
