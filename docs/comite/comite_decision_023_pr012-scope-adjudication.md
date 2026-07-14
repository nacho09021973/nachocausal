# Comité Decision 023 — pr012-scope-adjudication

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

PR012 is the unit that follows PR011's now-closed viability ladder (`n∈{4..8}`, all
`PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` via `HELLINGER_FALLBACK`, closed 2026-07-14, commit
`d8ce482`). PR011 §11 names PR012 (or "named certification scaling") as the next unit, opening
"if PR011 terminal is `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` — extend `n`, `ρ` ladder with prereg."
But PR011 §3.1 explicitly marks `ρ` as "not used" (the channel is `N=n` conditioned, not
Poisson-`ρ` conditioned) — the literal §11 pointer is internally ambiguous about what "extend the
`ρ` ladder" could even mean under PR011's own frozen channel definition.

The committee was asked to scope PR012 concretely, without authorizing execution:

1. What is PR012's decision question? (Candidates: (a) a TV curve `TV(τ0,τ1)` vs `Δτ=τ1-τ0` at
   fixed `n`, same `G_◊`/channel as PR011; (b) extending the tractable-`n` ladder beyond `{4..8}`;
   (c) switching the channel from `N=n`-conditioned to Poisson-`ρ`-conditioned sprinkling; (d) a
   combination.)
2. Does PR012 reuse PR011's frozen `G_◊` geometry and `HELLINGER_FALLBACK` method, or does it need
   a new geometry class / channel / certification method?
3. What numeric anchor would need to be frozen before any PR012 execution?
4. What gates (mirroring PR011 §10's G0a/G0b/G1/G2a/G2b/G3) should gate PR012?

## 2. Verified state

Facts checked this session, each with its command / file:line:

- `make verify-seal` → `nachocausal/thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (unchanged; PR011/PR012 track
  has never touched this file — `git show d8ce482 --stat` has no `nachocausal/` entries).
- `git log --oneline -3` on `main`: `d8ce482` (ladder closure) → `b823f19` → `9a5e3df`. Working
  tree clean except one untracked, unrelated patch file. Pushed to `origin/main`.
- **Backward-looking audit run this session, before this committee convened** (per skill
  discipline — a committing-step-adjacent `/comite` must stand on a fresh audit when it proposes
  building on already-claimed results): `docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md`,
  `AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS` (0 errors, 2 warnings). Independently reproduced
  `certify(n)` for `n=6,7,8` bit-for-bit on a fresh process; verified the CSV↔sha256↔test-constant
  hash chain for all three; confirmed the generator script has an **empty diff** in the closure
  commit (no code changed alongside the new artifacts); confirmed every ε value quoted in the
  three updated docs matches its source CSV verbatim. The two warnings, both carried forward from
  `auditor_report_009`: (i) the primary enumeration route has never closed tier-1 at any `n` —
  every rung rests on `HELLINGER_FALLBACK`; (ii) `audit.sh`'s heuristic flags the new artifact
  files as "no generator reference" despite prose documentation.
- **New finding, surfaced by this committee's Wave 2 (falsifier), not previously caught by
  `auditor_report_008/009/010`:** the terminal-selection logic in `dev/pr011_tv_certification_enumeration.py`
  (`certify()`, both the primary and fallback branches) is `TERMINAL_DISTINGUISHABLE if epsilon <
  1.0 else TERMINAL_INDISTINGUISHABLE if epsilon <= 0.0 else TERMINAL_INCOMPLETE`. Since
  `epsilon` is never negative (`certified_tv_upper` floors at 0.0 and rounds up), `epsilon <= 0.0`
  can only be reached when `epsilon == 0.0`, and `epsilon == 0.0` also satisfies `epsilon < 1.0` —
  which is checked **first**. The `TERMINAL_INDISTINGUISHABLE` branch (`PAIR_INDISTINGUISHABLE_TV_ZERO`,
  spec §8's "valid negative result") is **dead code**: it can never fire. This did not corrupt any
  of the five already-certified results (all five ε values are strictly positive, `0.0046`–`0.0092`,
  so the branch was never reached in practice), but it means the generator, as currently written,
  **cannot report the negative terminal PR011's own spec names as a valid outcome**. `[UNVERIFIED
  beyond static reading of the pasted code — not independently re-executed with `ε=0` this session;
  recommended as the falsifier's minimal test in §5]`.

## 3. Dossier

- `research_program/synthesis/pr011_mass_distinguishability_viability.md` — PR011 spec,
  `FROZEN_VIABILITY_SPEC`, §§1–13 (decision question, geometry `G_◊`, channel, methods, gates,
  current status).
- `dev/pr011_tv_certification_enumeration.py` — the committed generator PR012 would reuse or
  extend.
- `research_program/models/first_witness_pair_candidates.md` §2 — Theorem A (scale-dilation pair,
  `TV=0` exactly, PROVED).
- `research_program/work_packages/wp4_fisher_localization_floor.md` — Fisher/QMD regularity floor
  for the fixed-EF-corner diamond family; degenerate Kruskal-box and non-regular reshaped-EF-box
  counter-cases.
- `research_program/work_packages/wp4_two_point_theorem.md` — Theorem 1 (identifiability iff),
  Theorem 2 (Le Cam two-point bound).
- `formal/HorizonFormal/` — Lean corpus (order-theoretic only; zero probabilistic content, no
  `sorry`).
- `docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md` — fresh audit grounding this
  session.
- `docs/plan_avanzado_14_julio_2026.md:31` — flagged physical-mechanism attribution
  (singularity-imprint bimodality), corrected by the physicist brief as belonging to prereg-002,
  not PR011/PR012.
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`
  (Eichhorn–Gamito–Stokes, arXiv:2605.06813) — regular-black-hole caveat, literature-verified.
- `biblioteca/derived-md/The causal set approach to quantum gravity.md` (Surya, LRR 2019) —
  Myrheim–Meyer dimension estimator, chain-abundance diagnostics, literature-verified.
- `CLAUDE.md` — founding rules (anchoring, dev/validation separation, ground-truth non-leakage).

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

- Proposed artefact(s): PR012 must stay entirely in Track B and mirror PR011's committed layout
  exactly: spec at `research_program/synthesis/pr012_*.md` (status `FROZEN_*_SPEC` before any
  run); generator at `dev/pr012_*.py`; a reversible pre-flight at `dev/pr012_freeze_sanity_check.py`
  mirroring `dev/pr011_freeze_sanity_check.py`; certification outputs as `data/reports/pr012_*.csv`
  + `.sha256` sidecar pairs. Zero touch to `nachocausal/` or `nachocausal/thresholds.py`.
- Environment & seal: pure-arithmetic Track-B path, not the sealed validation env. Seal to
  re-verify unchanged before/after: `6e2c3888…`. Pin numpy 1.26.4 to protect against float drift.
- Provenance capture: PR011 embeds no machine provenance inside artifacts (grep empty).
  Provenance rests on the spec's provenance-header text + sha256 sidecar + one-commit-per-`n`
  discipline. PR012 must record commit, seal SHA, numpy version, uname/pip freeze, UTC timestamp,
  and an explicit determinism note (no RNG/no seed).
- Run mechanics: single deterministic invocation, no background job, no seed band currently. The
  refuse-overwrite guard (`publish_certification` raises on an existing artifact) is what makes
  publishing the committing step safe.
- Reproducibility risks / ambiguities:
  - The three candidates have sharply different repro contracts: (b) extend-`n` is cheapest/safest;
    (c) switch to Poisson-`ρ` **introduces an RNG**, breaking the current deterministic no-seed
    guarantee and forcing a new seed-band/ensemble/provenance discipline; (a) TV-curve-vs-`Δτ`
    keeps determinism but multiplies rows/files.
  - The refuse-overwrite one-file-per-`n` pattern does not map onto a `Δτ` curve (many points) —
    artifact shape must be re-specified before freeze if (a) is chosen.
  - The only reading that actually "uses `ρ`" is (c) — the exact reading that breaks determinism.
    `§11`'s "`ρ` ladder" is ambiguous without a new channel spec.
  - Extending `n` (b) rests on a bound (`ε=n·TV_copula`) that degrades with `n` — a real ceiling
    on how far (b) can go before self-defeating (`ε≥1`).
  - Any `Δτ`-curve run must re-verify the Theorem A exclusion as `Δτ→0` — new code, must be
    frozen/spec'd, not added post-hoc.
  - `[UNVERIFIED]` bit-stability of `HELLINGER_M=100` grid arithmetic across numpy versions.

### Mathematician brief

- Computability: (b) `N=n`-conditioned is finite/decidable (`TV` a finite sum over `Ω_n`), but
  primary exact enumeration already fails to close by `n=8` (`raw_mass_sum≈0.001`). (c)
  `ρ`-conditioned is a countable-support, only-truncation-computable object. `|Ω_n|` grows
  super-exponentially `[UNVERIFIED — from memory]`, the hard ceiling on (b).
- Order observable: the full unlabeled-poset law `P_n(τ)` is the sufficient statistic; carries the
  horizon signal via `τ` deforming null cones in `g_τ`. `ε=⌈n·√H²·√(1-H²/4)⌉` is an `n`-fold
  data-processing bound, generically loose, growing linearly in `n`. PR012 (Track B) must not
  conflate this with Track A's sealed estimator-v2 observable.
- Relevant invariants: ordering fraction / Myrheim–Meyer dimension, longest-chain/height, interval
  abundances — all strictly coarser than `P_n(τ)`; usable only as sanity diagnostics.
- Analytic / continuum target: for the QMD-regular `G_◊`, `H²(c_τ,c_{τ+Δτ})=(Δτ²/4)I(τ)+o(Δτ²)` —
  a candidate-(a) curve is meaningful as a check that measured TV follows this smooth `O(Δτ)` LAN
  law rather than a non-regular `√|δ|` law.
- Caveats:
  - (c) is not merely a harder computation of the same quantity — it **changes the observable**:
    `N` becomes readable from the poset, reopening the cardinality leak §4.2 deliberately closed
    and the absolute-scale information Theorem A excises. (c) needs a new spec/channel semantics.
  - (a) `Δτ→0` is **not** the Theorem-A degenerate regime (the fixed-corner class is proved to
    have no `TV=0` witnesses) — ordinary vanishing, not degeneracy. The real `Δτ→0` danger is
    **numerical**: catastrophic cancellation in the Hellinger grid difference. Any (a) curve must
    freeze a minimum `Δτ_floor` derived from an error model, before execution.
  - A curve parametrized by reshaping (rather than pure `τ`-variation within fixed-corner `G_◊`)
    can wander into the non-regular family (`H²≍|δ|`, floor `1/n`). Must constrain strictly to
    `G_◊`, re-verify the `Φ_s`-non-relatedness sanity check at every `Δτ`, not just the one frozen
    pair.

### Mathematical logic brief

- Formal status: the Lean corpus is entirely order-theoretic (horizon/ideal/chain-end), zero
  probabilistic content, no `sorry`. **None** of PR011/PR012's probabilistic objects (`P_n(τ)`,
  TV, Hellinger, Le Cam, Fisher) are formalized in Lean — backing is prose proofs + committed
  Python enumerator only. Proved (prose): Theorem 1 (genuine iff), Theorem 2 (Le Cam, standard),
  Theorem A (`TV=0` on scale orbit, PROVED at every `n`). Conditional: Corolario 3 depends on an
  unproved adversarial pair. The five certified `ε` values are certified **upper bounds** of form
  `ε=⌈n·copula_TV_upper⌉` — **not** direct evaluations of the §1 object `TV(P_n(τ0),P_n(τ1))`.
- Quantifier / dependency order: §11's literal pointer is **not a well-formed extension of PR011
  as frozen** — a definitional defect, not a wording nit. §4 fixes `P_n(τ)` for a fixed `n`; §3.1
  records `ρ` "not used" because the channel conditions on `N=n` — under that binding definition,
  `∀ρ` has no free variable to bind. "Extend the `ρ` ladder" is only well-typed if §4's channel is
  **first** replaced with an unconditioned Poisson-`ρ` channel (candidate c) — a change to a
  load-bearing definition producing a *different* object from `P_n`, not "a ladder of the same
  `P_n`." This row is a likely **drafting relic** (dates to freeze `6662a3b`, pre-`n=5..8`,
  unrevised) and should be corrected/split — via an audited errata, never a silent rewrite of
  frozen text — before PR012 is scoped further.
- Equivalence claims: Theorem 1's iff is safe to lean on. Theorem A is stated as an equivalence
  ("the `TV=0` class is exactly the scale orbit") — if PR012 ever leans on the converse (`TV>0 ⟹`
  not scale-related), the committee must confirm both directions are proved, not assume the
  contrapositive of the one proved direction. The `ε<1` certification is **one-way** and must
  never be read as `TV=ε` or as the risk floor.
- Type / object discipline: "TV curve vs `Δτ`" is well-typed in the abstract (a function
  `I_Δτ→[0,1]` at fixed `n`/channel). The category error is at the **method** level: `certify()`
  returns `ε(n,Δτ)=⌈n·copula_TV_upper(Δτ)⌉`, a bound-of-a-bound, not `TV(P_n(τ0),P_n(τ1))`.
  Because `ε` is linear in `n` by construction, it will **exceed 1** as `Δτ` grows, so a curve
  built from the fallback goes **vacuous** over most of any nontrivial `Δτ` interval while still
  nominally type-checking as a `[0,1]`-or-more object. PR012 must name which object each curve
  point represents and which method certifies it.
- Caveats: no seal/track violation implicated; Lean corpus has no TV/Le Cam/Fisher content;
  `ε=⌈n·copula_TV_upper⌉` is an `n`-fold bound, not `TV(P_n)` — a naive PR012 "TV curve" from
  `HELLINGER_FALLBACK` would be a bound-of-a-bound curve, vacuous once `n·copula_TV_upper≥1`.

### Physicist brief

- Coordinates & patch: PR012 must inherit PR011's frozen EF chart exactly, with corners fixed in
  **absolute** coordinates — this is what breaks Theorem A's scale orbit. Must not reshape the
  diamond toward a thin near-horizon sliver (re-enters non-regular regime, `κ~λ⁶` degradation).
- Physical meaning — **correction to the decision-question framing**: PR011/PR012's
  distinguishability mechanism is **not** prereg-002's singularity-truncated-futures bimechanism —
  the diamond's `r_q>0` avoids the singularity automatically inside `D_τ`. The signal is instead
  the proven Fisher-regular `τ`-dependence of the diamond's internal causal order — a different
  physical effect requiring its own claim-boundary text, not reuse of prereg-002's caveat.
- Behaviour as `Δτ→0`: **graceful, no qualitative floor**, in the `N=n` channel — `G_◊`'s proved
  QMD regularity gives `H²=(Δτ²/4)I(τ)+o(Δτ²)`, `TV≤(Δτ/2)√(nĪ)`, shrinking smoothly to 0. The
  only floor (`δτ~ℓ/√κ`) is an operational statement that **presupposes a physical density `ρ`**,
  which the `N=n` channel does not have.
- Sprinkling domain: frozen channel conditions on `N=n`; `ρ` explicitly not used. Switching to (c)
  **requires its own new claim-boundary statement**: `ρ` becomes dimensionful (floor `δτ~ℓ/√κ`
  becomes relevant); `n=ρ·V(τ)` becomes random **and `τ`-dependent** (`V(τ)` differs between the
  two masses), **reopening** the cardinality leak §4.2 deliberately closed — part of the "signal"
  would then ride on a pure area difference, no longer strictly order-only.
- Claim boundary: PR012 claims only certified statistical distinguishability of scalar `τ=2M`
  within one named 1+1D EF diamond family `G_◊`, at fixed cardinality (or density, if c). Does
  **not** rest on singularity-truncated futures — needs its own boundary text, not copied from
  prereg-002.
- Caveats: **recommends candidate (a)** — TV vs `Δτ` at fixed `n`, same `G_◊`, same `N=n` channel
  — as the physically clean question, staying inside proven regularity. Candidate (c) needs its
  own freeze + claim boundary; must not be folded silently into the §11 "extend the `ρ` ladder"
  pointer, which is internally inconsistent with §3.1 and should not be papered over.

## 5. Falsifier attack

- Concrete failure modes:
  1. **Candidate (a) as recommended is, with the current method, a study that cannot fail.** The
     only certification method past the never-converging primary route is `HELLINGER_FALLBACK`,
     whose output is an analytic consequence of already-proved QMD regularity (`H²=(Δτ²/4)I(τ)+o(Δτ²)`).
     The entire shape of the proposed "TV curve" (linear in `Δτ`, linear in `n`) is foregone by
     theorems already on file — every point is a PASS by construction, and the mathematician's
     stated purpose (checking the curve follows the regular LAN law rather than a non-regular
     `√|δ|` law) is unachievable by this method, since there is no certified *lower* bound
     anywhere and the copula-level input is poset-level-blind by construction. A poset-level
     non-regularity would be invisible.
  2. **The terminal PR012 would inherit may be semantically inverted.** PR011 §7 itself states:
     "If `ε` is small, masses are hard to distinguish (large minimax floor)." The certified
     `ε=0.0092` at `n=8` gives, via Le Cam, minimax error-sum `≥1-ε≈0.99` — i.e. the frozen pair
     is provably *almost impossible* to distinguish at every certified `n`. `ε<1` is logically
     **consistent with `TV=0`** and therefore certifies no distinguishability at all by itself;
     what would rule that out is the **converse** of Theorem A, which exists as an unlabeled prose
     bullet, not a numbered proved theorem with the same proof apparatus as the forward direction.
  3. **The mathematician's proposed "declare the expected FAIL boundary" is unreachable inside any
     tractable extension** — by the proved linearity, vacuity (`ε≥1`) requires `n≳868` at
     `Δτ=0.1` (derived by linearity from the certified values; approximate). A "frozen FAIL
     boundary" here is decorative; leaving the range open "until vacuity appears" would be
     tuning-by-exploration.
  4. **`Δτ→0` numerics**: the `M=100`/`M=72` cross-check compares two quadratures of the same
     integrand — a correlated check, not an absolute error bound. `H²` at `Δτ=0.001` is
     `~1.3e-10` by the `Δτ²` law; the stability check can pass on cancellation noise. No absolute
     quadrature-error bound was found in the generator by inspection. Any `Δτ_floor` chosen
     *after* observing which points raise `RuntimeError` would be post-hoc tuning.
  5. **Candidate (c)**: an order+cardinality channel makes the "order-only" token false for that
     unit; §11's "`ρ` ladder" phrase cannot authorize it because §11 is ill-typed against frozen
     §3.1/§4 — an ill-typed pointer authorizes nothing.
- Ground-truth leakage: Track B has no hidden embedding contact (confirmed, `CLAUDE.md`
  guardrail intact). Analogues to watch: (i) using the already-observed nominal enumeration TVs
  or the five certified `ε` values to choose PR012's `Δτ` grid or `n` range would be
  design-from-data — the grid must derive from theory (the proved `I(τ)`) only; (ii) marketing the
  curve as "recoverability evidence" would be wrong — both `τ` values are closed-form inputs to
  every certified number, nothing is recovered; (iii) importing `plan_avanzado_14_julio_2026.md:31`'s
  singularity-imprint framing into PR012 text would be a cross-track narrative leak from Track A.
- Freeze violations: (i) "correct §11 before scoping" must be an **audited errata appendix**, never
  a silent rewrite of a `FROZEN_VIABILITY_SPEC` document; (ii) candidate (c)'s RNG opens a
  seed-band door — any re-draw after an unfavorable curve point would be a virgin-seed-burn
  analogue; (iii) a many-point curve must freeze its *full* point set up front — "add three more
  `Δτ` points" after seeing the curve would be threshold-shopping in disguise.
- Verdict coercion: **confirmed live defect** in the reusable generator (independently surfaced
  this wave, not previously caught by `auditor_report_008/009/010`): the terminal-selection chain
  `TERMINAL_DISTINGUISHABLE if epsilon<1.0 else TERMINAL_INDISTINGUISHABLE if epsilon<=0.0 else
  TERMINAL_INCOMPLETE` has an unreachable `INDISTINGUISHABLE` branch, since `epsilon<1.0` is
  checked first and `epsilon==0.0` satisfies it. The spec's own "valid negative result"
  `PAIR_INDISTINGUISHABLE_TV_ZERO` can never be emitted by this generator as written — a
  structural PASS-only verdict map on any pair genuinely at `TV=0`. This did not corrupt PR011's
  five already-certified results (all five `ε>0`), but any PR012 reuse of `certify()` unmodified
  inherits this asymmetry. Separately: a curve run must pre-declare what a `RuntimeError`-raising
  `Δτ` point records (an explicit ABSTAIN/OUT_OF_DOMAIN row), else failed points would be silently
  omitted.
- Premature / over-broad claims: any PR012 text reading the ladder or a curve as "masses are
  distinguishable" over-claims by converting an upper bound into a lower bound (failure mode 2)
  and by inheriting a terminal name the spec's own §7 arguably contradicts. Claim boundary must
  read: *certified upper bounds on TV for one scalar-`τ` pair in one fixed-corner 1+1D EF diamond
  family at fixed `n`; small `ε` means a large minimax floor at these `n`* — `NO_RECONSTRUCTION_CLAIM`.
- Independent-falsification gate: **not satisfied**. Every rung rests on `HELLINGER_FALLBACK`; the
  `n`-fold product bound is prose-proved by the same authorship pipeline that coded and ran it,
  machine-checked nowhere (Lean corpus has zero probabilistic content); the auditor's own
  mechanical check cannot trace artifacts to the generator by anything but a naming heuristic. The
  claim's author is currently its own effective verifier for the probabilistic layer. PR012's
  gates must include an independent re-derivation (or a finite Alloy/Lean-checkable instance) of
  the product bound and of Theorem A's converse before any curve is published.
- Minimal falsification test: run, in `dev/`, no seal contact:
  `python3 -c "from dev.pr011_tv_certification_enumeration import certify; r = certify(4, 0.95, 0.95 + 1e-9); print(r.terminal, r.epsilon_certified_upper)"`.
  Either outcome is informative: (i) a `RuntimeError` from Hellinger grid instability, proving no
  `Δτ` curve can run without a frozen, error-model-derived `Δτ_floor`; or (ii)
  `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` with `ε≈0` for a pair that is physically and numerically
  indistinguishable — exposing the inverted terminal semantics, the unreachable
  `INDISTINGUISHABLE` branch, and the cancellation regime simultaneously. Candidate (a) must not
  reuse `certify()` unmodified until this probe is run and its result understood.

## 6. Pre-registration verdict

- Verdict: **PASS**
- Freeze status: no thresholds are frozen by this scoping session — correctly so; PR012 has no
  spec document yet, so "frozen before data is seen" is a requirement on a *future* PR012 freeze
  commit, not on this deliberation. What this session checks is whether the scoping recommendation
  is freeze-compatible in principle. It is, for candidate (a): mirrors PR011's own already-frozen
  numeric-anchor pattern (fixed corners, fixed pair rule, frozen `n`-ladder, frozen error budget)
  which is proven workable by PR011's own precedent. Candidate (c) is **not yet freeze-compatible**
  as scoped — no numeric anchor, no seed discipline, reopens exclusions PR011 bound shut.
- Seal integrity: confirmed unchanged, `6e2c3888…`; `git show d8ce482 --stat` touches no
  `nachocausal/` path. The older `ad02cb57…` SHA in `docs/preregistration_001_addendum.md` is a
  historical record of the pre-estimator-v2 freeze, not live drift — not load-bearing here since
  PR012, like PR011, must stay off the Track-A path entirely.
- Seed discipline: PR011's track runs with zero RNG; candidates (a) and (b) preserve this, so no
  new seed-band question arises for them. Candidate (c) is the one place a seed question is
  created from scratch — an RNG entering this track for the first time — and would require its
  own new dev/validation-seed-disjointness discipline, frozen *before* any candidate-(c) freeze,
  never retrofitted. No Track-A virgin seed band may ever be reused here regardless of candidate.
- Reporting rule: PR011's own §8 terminal table already sets the correct precedent (one primary
  terminal, negative/non-terminal outcomes reported on the same footing as the positive one) —
  whatever PR012 candidate is chosen must inherit this all-outcomes-reported symmetry, and per §5
  above must first **fix or explicitly work around** the confirmed unreachable-`INDISTINGUISHABLE`-branch
  defect before that symmetry can actually hold in practice.
- Forbidden moves present? None in the scoping session itself. Three latent risks must be closed
  before any PR012 freeze or they become forbidden moves on first draft: (1) §11's pointer is
  inconsistent with §3.1 and dated to a pre-`n=5..8` freeze — must be corrected via an audited
  errata, not a silent rewrite; (2) the vacuous-`ε` risk (a `HELLINGER_FALLBACK` curve is
  `ε=n·TV_copula`, not `TV(P_n)`, and goes vacuous past `ε≥1` while still type-checking) must be
  named per-point in any PR012 spec, else a vacuous point could be reported with the same
  evidentiary weight as a genuine bound — a disguised threshold-loosening; (3) the `Δτ→0`
  numerical floor must be frozen from an error model *in the spec itself*, before any curve point
  is computed, else there is room to quietly discard/re-derive near-zero points after seeing them
  misbehave.
- Reasons: this session only scopes and authorizes nothing, consistent with `CLAUDE.md`'s
  dev/validation separation and PR011's own precedent that spec freeze is not authorization to
  execute (§10). Seal unchanged and Track B structurally walled off from `nachocausal/` (verified
  this session, `git show d8ce482 --stat`). Auditor precedent for this exact lineage:
  `auditor_report_010`, `AUDIT_PASS_WITH_WARNINGS`, both warnings unrelated to freeze integrity.
  Candidate (a) reuses PR011's already-frozen anchor exactly, the pattern that makes
  "freeze-before-data" achievable in practice; candidate (c) fails freeze-compatibility as scoped
  and needs its own ground-up spec, never inheriting PR011's freeze by reference.

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| Eichhorn–Gamito–Stokes arXiv:2605.06813, regular-black-hole caveat attaches to chain/partition diagnostics (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:195,199`) | Physicist | CONFIRMED |
| Myrheim–Meyer dimension estimator / ordering fraction `r=2R/n(n−1)`, Surya LRR 2019 §4.1 (`biblioteca/derived-md/The causal set approach to quantum gravity.md:986-1010`) | Causet mathematician | CONFIRMED |
| Longest-chain / height diagnostic — Myrheim 1978; Brightwell–Gregory 1991 (same LRR doc, lines 132, 1226-1299, bibliography 3432) | Causet mathematician | CONFIRMED |
| "Bombelli–Meyer 1987" (cited as source for the ordering-fraction/Myrheim–Meyer estimator) | Causet mathematician | **UNCONFIRMED** |
| Interval abundances `C_k` attributed to "Benincasa–Dowker" | Causet mathematician | **UNCONFIRMED** |

Notes:
- Eichhorn–Gamito–Stokes: the source states verbatim (line 195) that the chain/cardinality
  "partition" diagnostic "would no longer work for regular black holes, because…timelike curves
  can also be continued for arbitrarily long proper time inside the horizon." This scopes the
  caveat to the §III chain/cardinality diagnostics specifically, not the §IV geodesic-focusing
  machinery — consistent with the physicist's claim that it bites prereg-002's mechanism, less
  directly a diamond-order PR012 mechanism.
- **"Bombelli–Meyer 1987" does not exist as cited.** The actual 1987 causal-set founding paper is
  **Bombelli, Lee, Meyer, Sorkin (1987)**, "Space-time as a causal set" (four authors, "BLMS
  1987"). A genuine two-author Bombelli–Meyer paper exists but is dated **1989** ("The origin of
  Lorentzian geometry," a different topic — Lorentzian-geometry statistics, not the
  ordering-fraction estimator). If any future PR012 draft cites this material it must say "BLMS
  1987" for the founding paper or "Bombelli & Meyer 1989" for the correct 1989 paper — not
  conflate the two.
- **`C_k` is not Benincasa–Dowker's notation.** Benincasa–Dowker's order-interval abundance (used
  in the BDG action) is denoted `N_i`/`N_m` in the primary sources
  (`biblioteca/derived-md/Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md:123`,
  `biblioteca/derived-md/Bhatnagar_2021_Causal_Set_Theory_and_Benincasa_Dowker_Conjecture.md:519,575`).
  `C_k` does appear in `biblioteca/`, but as Meyer's/Roy-et-al.'s **chain-abundance** diagnostic
  (Surya LRR, lines 1100-1105, 1249, 1633) — part of the Myrheim–Meyer dimension-estimator family,
  a related but different quantity. Any PR012 draft citing "interval abundances" must pick the
  correct symbol/attribution and not pair `C_k` with "Benincasa–Dowker."
- Per the verifier's scope note: Theorem A, the Fisher/QMD floor, the two-point/Le Cam theorem,
  and the Lean corpus are in-repo project material, not external literature, and were correctly
  excluded from this literature-verification pass.

## 8. Synthesis

**Recommended direction:** scope PR012 as candidate (a) — a certified-`TV`-vs-`Δτ` question at
fixed `n`, reusing PR011's frozen `G_◊` geometry and `N=n` channel — but **do not draft or freeze
that spec yet**. Three of four Wave-1 experts (mathematician, logician, physicist) converge on (a)
as the physically and order-theoretically cleanest continuation, and the pre-registration warden
confirms it is the only candidate that is freeze-compatible today using PR011's own precedent.
Candidate (c) (a genuine Poisson-`ρ` channel) is unanimously assessed as a materially different,
heavier undertaking — new observable, breaks the track's current determinism, reopens the
cardinality leak and the absolute-scale exclusion PR011 deliberately closed — and should be
tracked as a **separate, later, ground-up spec**, never folded into PR012-as-PR011-extension.
Candidate (b) (bare `n`-ladder extension) is available but self-limiting: the `ε=n·TV_copula`
bound degrades linearly and the primary enumeration route has never once closed tier-1, so pushing
`n` further mostly produces looser certificates on the same underlying question PR011 already
answered, not new information.

**The falsifier's attack blocks an immediate PROCEED**, and per this skill's own discipline an
unresolved falsification cannot coexist with a PROCEED verdict. Two findings are load-bearing and
must be resolved — not merely caveated in a future spec — before PR012 can be scoped further:

1. **A confirmed, previously-uncaught logic defect** in the reusable generator: the
   `TERMINAL_INDISTINGUISHABLE` branch in `certify()` is dead code (§5, verdict-coercion finding).
   It never corrupted PR011's five certified results (all `ε>0`), but it means the "valid negative
   result" terminal PR011's own spec names in §8 cannot currently be emitted, and any PR012 reuse
   of `certify()` unmodified inherits a structurally PASS-only verdict map. This is a backward-
   looking finding about already-frozen, already-audited code that three prior audit passes
   (`auditor_report_008/009/010`) did not catch — it should be logged and fixed (or the branch
   logic explicitly justified as unreachable-by-design, if that is somehow intended) through the
   normal audit/fix channel before PR012 relies on the same code path.
2. **An open question about whether PR011's own terminal name over-claims.** The falsifier
   (finding 2) and the mathematical logician (equivalence-claims caveat) both flag, independently,
   that a certified upper bound `ε<1` is logically consistent with `TV=0`, and that
   `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` is not itself evidence of distinguishability without the
   unproved converse of Theorem A. This is a genuine open disagreement the committee cannot
   resolve by fiat — it bears on how PR011's *already-published* five certifications should be
   read, not just on PR012's scope, and deserves its own `/auditor` pass or a targeted follow-up
   `/comite` focused on PR011's terminal semantics before that language is reused in a new spec.

**Open disagreements, surfaced not hidden:**
- The mathematician's proposal to freeze a "declare the expected FAIL boundary" for candidate (b)
  is contradicted by the falsifier's derivation that this boundary (`n≳868`) is unreachable at
  tractable `n` — the mathematician's own brief did not compute this; the falsifier's arithmetic
  should be checked independently before it is treated as settled.
- Whether Theorem A's stated equivalence ("`TV=0` class exactly = scale orbit") has both
  directions actually proved, or only the forward direction with the converse asserted in prose,
  is unresolved between the logician (flags as a caveat) and the falsifier (treats the gap as
  load-bearing and blocking). This should be checked directly against
  `research_program/models/first_witness_pair_candidates.md` before PR012 leans on it.
- The reproducibility engineer and physicist frame candidate (c) as merely "heavier"; the causet
  mathematician and physicist go further and call it a **different observable**, not a scaled-up
  version of PR011's. This is not a contradiction so much as a matter of emphasis, but any future
  PR012-adjacent text should use the stronger framing (different observable) to avoid implying (c)
  is a routine extension.

## 9. Next-step spec

**Reversible steps (may be run now if the user asks, no freeze/authorization required):**

1. Run the falsifier's minimal test in `dev/` (no seal contact, no repo write beyond terminal
   output): `python3 -c "from dev.pr011_tv_certification_enumeration import certify; r =
   certify(4, 0.95, 0.95 + 1e-9); print(r.terminal, r.epsilon_certified_upper)"`. This is read-only
   diagnostic execution of already-committed code with a new input, not a committing step.
2. Draft (not freeze) a short errata note documenting the §11 "extend `n`, `ρ` ladder" ambiguity
   and the dead-`TERMINAL_INDISTINGUISHABLE`-branch finding, for the user's review — a plain
   markdown note, not an edit to the frozen `pr011_mass_distinguishability_viability.md` itself.
3. Consider a targeted `/auditor` pass specifically on PR011's terminal semantics (open
   disagreement 2 above) — backward-looking, no repo modification, produces a report the user
   reads.

**Committing steps (only on explicit user authorisation — none of these should be taken by the
committee or automatically):**

- Editing `dev/pr011_tv_certification_enumeration.py` to fix the dead branch (or any other code
  change) — this is a change to previously-audited, already-relied-upon code and needs the user's
  sign-off even though it is a "bug fix," per this project's discipline that the committee never
  edits code.
- Amending `pr011_mass_distinguishability_viability.md` (a `FROZEN_VIABILITY_SPEC` document) via
  an audited errata appendix, once findings 1–2 above are resolved.
- Drafting and freezing a `research_program/synthesis/pr012_*.md` spec for candidate (a), gated on:
  a frozen `Δτ` grid + `Δτ_floor` derived from an explicit error model (not from observing which
  points misbehave); explicit per-point labeling of which mathematical object is certified
  (`TV(P_n)` via primary enumeration vs the `ε` bound-of-a-bound via `HELLINGER_FALLBACK`); a
  gates table mirroring PR011 §10 (G0a spec freeze, G0b — n/a here, no PR010-style prerequisite
  identified, G1 `/comite` on the numeric anchor — i.e. a **follow-up** `/comite` once findings
  1–2 are closed, G2a/G2b `/auditor` on freeze text and pre-execution `ε`, G3 literature check if
  triggered); and an explicit resolution (not a caveat) of open disagreement 2 above, since it
  bears on how any new PR012 terminal should be worded.
- Any PR012 certification execution — out of scope until the spec above is frozen and gated.

**Falsifier's minimal falsification test** (repeated for visibility): see reversible step 1. Its
result should be read before any further PR012 scoping work, since it directly tests the
verdict-coercion and Δτ→0-numerics findings simultaneously.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
