# Comité Decision 019 — rvar-partF-execution-feasibility

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

PI, 2026-07-05, verbatim: "Convoca al comité para autorizar la ejecución de Parte F step 3
(cómputo de la tabla μ sobre nulos EXPLORE), bajo el addendum congelado en commit 0271fd9
(dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md)." This is a request to authorize an actual committing
step: sprinkling `EXPLORE_POOL` nulls and computing the frozen `μ_n` object comité 018 adjudicated.

## 2. Verified state

Facts checked **this session** (2026-07-05), each with its command / file:line. Per the skill's
own rule ("do not let `/comite` recommend PROCEED atop an `AUDIT_FAIL`"), `/auditor` was run first
to build the ground this session stands on.

- **`/auditor` ran first this session: `docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md`,
  `AUDIT_VERDICT=AUDIT_PASS`** (0 errors, 0 warnings). Confirmed: seal matches
  (`6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` = `docs/preregistration_002.md:8`);
  Gate 0 Tier 0 (`b142377`) and Tier 1 (`55e19b8`) result JSONs committed and match their reports
  exactly; the μ-freeze addendum commit `0271fd9` matched comité 018 §9.1's required tokens
  verbatim at the time of the audit; no Part F execution artefact existed anywhere in the tree;
  sealed test suite `28 passed` under `.venv/bin/python -m pytest -q tests/`.
- **Important scope limit on that PASS, surfaced by wave 1/2 this session and conceded by the
  chair: auditor 006 performed a token-match / provenance check, not a feasibility or
  executable-determinism check.** It correctly verified the frozen *text* matches what comité 018
  ordered; it did not and could not assess whether that text is computationally executable at
  production scale, or whether two independent implementers would consume identical seeds.
- **Mid-session, the working tree of `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` was hand-edited
  (uncommitted, `git status --short` shows `M`)**, adding: (i) an explicit "Part F
  M-consumption semantics" section stating Part F counts `MINK`-only draws and does **not**
  inherit Tier 1's `KINDS=("MINK","BH")` dual count; (ii) an explicit statement that the spawn
  scheme is closed locally to `SeedSequence(root).spawn(K)` only, no `Generator.spawn` alternate
  reading; (iii) the comité-018 dual-consumption-plan diff test elevated to a named hard
  precondition; (iv) an explicit disclaimer that **production feasibility at `N` up to
  production scale is NOT authorized, NOT claimed, and NOT inferable from AUDIT_006, Gate 0, or
  this addendum** — and a list of concrete blocking conditions. This edit closes the
  kind/spawn-form ambiguity two wave-1 roles and the falsifier independently found this session
  (see §4-§5) but does **not** address, and explicitly disclaims addressing, the computational
  feasibility question that is this brief's central finding. It is uncommitted; nothing in it
  changes the verdict below.
- Independently re-read by the chair and by the warden this session:
  `dev/measure_pr003_rvar_gate0.py:67-79` (`family_A`) enumerates **all `2^{|Max(C)|}` subsets**
  of the maximal antichain via `itertools.combinations`; `mincut_argmax_in_family` filters
  min-cut ties by iterating over that enumerated family. This is confirmed to be the *entire*
  Gate-0-verified code path — not merely the mathematician's inference, but directly read source.
- **Citation correction (caught by the falsifier this session, verified by the chair via
  `grep`):** the "production feasibility is untested... `[UNVERIFIED: actual runtime at
  N≈86k]`" finding is in **`docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md:222-224`**,
  not comité 017 as the chair's dossier for wave 1/2 this session mis-cited. Substance unaffected;
  provenance now correct for the record.
- git HEAD unchanged at `0271fd9` throughout this session's deliberation (no commit made). No
  seed touched, no code executed, beyond the chair's `make verify-seal`, `make test` (sealed
  venv), `git`/`grep` inspection, and the auditor's mechanical script — all read-only.

## 3. Dossier

- `docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md` (this session's
  foundation audit).
- `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` (committed text at `0271fd9`, plus the uncommitted
  working-tree edit described in §2).
- `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md`: Part D.1 (𝒜(C) membership predicate, disjunctive —
  "todo z∈D yace bajo algún elemento maximal que está en D"), Part D.2/D.2.1/D.2.2 (score,
  min-cut reduction, forced-in/out), Part D.3 (typed abstention ladder), Part D.4 (symmetric
  reporting), Part E ("polinomial... para cualquier poset finito" — the claim under dispute),
  Part F/F2 (μ_n definition).
- `dev/measure_pr003_rvar_gate0.py`, `dev/measure_pr003_rvar_gate0_tier1.py`,
  `dev/gate0_tier0_result.json`, `dev/gate0_tier1_result.json` — the only executed, verified
  R-VAR code and its results (N≤14/16 only).
- `docs/comite/comite_decision_017_r-var-v2-reconvene.md`,
  `docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md` — prior sessions;
  018's falsifier §5 finding 5 (production feasibility untested) is the specific open item this
  session was meant to close and instead confirms and sharpens.
- `nachocausal/thresholds.py` (`INTENSITIES`), `nachocausal/generator.py:47`
  (`n = rng.poisson(intensity)` — the corrected N-scaling), `dev/explore_seeds.py`.
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`
  (EGS arXiv:2605.06813, n~10³ sprinklings, regular-BH caveat); `biblioteca/Bombelli_1987_PhD.md`;
  `biblioteca/Benincasa_Dowker_Glaser_Actions_Quantum_Counting_arXiv2505.22217.md`;
  `biblioteca/Dynamics_of_Causal_Sets_arXiv_gr-qc0212064.md` (Kleitman-Rothschild bibliography
  entry).

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

Proposes a new script `dev/measure_pr003_rvar_partF_mu.py` (MINK-only per Part F2, not Tier 1's
dual-kind loop), requiring `assert_environment()` (never called in the Tier 0/1 precedent — a
real gap since μ is a number entering the pipeline, unlike Tier 0/1's algorithm-only check), full
provenance recording of the exact `(root, child_index)` trace. **Identifies two concrete
ambiguities auditor 006's token-check did not catch:** (1) a spawn-form divergence between spec
Part F2's own prose ("`numpy default_rng(seed).spawn`", i.e. `Generator.spawn`) and the addendum's
mandated `SeedSequence(root).spawn` — the addendum resolves it only if read as controlling over
F2's prose; (2) whether the μ null substrate is MINK-only (per Part F2's literal text, "sin
horizonte") or inherits Tier 1's dual `KINDS=("MINK","BH")` loop via "verbatim reuse" — neither
the addendum nor spec Part F mentions "kind" at all (confirmed by grep). **Recommends the
comité-018 dual-consumption-plan diff test become a hard precondition, not optional**, since these
two divergence points are exactly what it would catch.

### Mathematician brief

Order-theoretic content of R-VAR (𝒜(C), S=A/B, D.3 ladder) confirmed decidable and correctly
specified, consistent with prior sessions. **Central finding: the only Gate-0-verified
implementation (`family_A`) enumerates ALL `2^{|Max(C)|}` subsets of the maximal antichain**, and
the min-cut argmax is filtered *through* that enumerated family, not computed as a standalone
polynomial optimization. Invisible at Tier 0/Tier 1 (`N≤14`, `|Max|` tiny); at production
intensities, antichain size scales roughly as `√N` (Myrheim-Meyer/Surya-type result — flagged
`[UNVERIFIED in biblioteca]` by the literature verifier, see §7), giving `2^{|Max|}` in a range
from astronomically large to categorically infeasible. **Part E's "polynomial for any finite
poset" claim describes Picard's max-flow optimization step in isolation, not the enumerate-and-
filter code that actually passed Gate 0 — these are not the same verified object.** A genuinely
polynomial implementation would be new, unwritten, unverified code requiring its own fresh Gate 0
before any μ computation, per the project's own "each tier needs separate authorization"
discipline. The frozen `OUT_OF_DOMAIN_UNCALIBRATED` rule provides **zero** protection against this
— it catches empty-family-too-common, a failure mode anti-correlated with (not the same as)
computational blowup. **Recommends NOT authorizing execution under `0271fd9` as-is.**

### Mathematical logic brief

Confirms the macro structure of the addendum (roles, root→level allocation, level enumeration,
OOD/INCONCLUSIVE third states, M's definitional meaning) is complete and well-typed — the six
comité-018 §9.1 items are genuinely closed, matching auditor 006. **Independently found the same
kind-dimension gap as the reproducibility engineer, more sharply:** Tier 1's
`KINDS=("MINK","BH")` dimension has no counterpart anywhere in the addendum or spec Part F text
(confirmed via grep — zero hits for "kind" in either file, at the time of the audit). "Verbatim
reuse of Tier 1" is therefore a one-way semantic pointer, not a proved procedural identity — two
competent implementers given only the addendum + spec text are **not** guaranteed to consume the
same `(root, child_index[, kind])` sequence. Also flags: child-consumption order within a root
(ascending spawn index) is pinned only by an external pointer to the Tier 1 code, not
self-contained in the addendum's own prose; "children exhausted under skip/throw" (e.g. an
out-of-range-N child, which Tier 1 skips via `continue`) is undefined — does a skipped child count
toward the 400-budget or toward `rate_empty`'s denominator? Confirms via `git log --all` that the
comité-018 dual-consumption-plan diff test has not been run. **Recommends treating that diff test
as a hard precondition**, or a textual amendment pinning the three residual choices, after which
the diff test becomes a formality.

### Physicist brief

Coordinates, physical meaning of the R-VAR signal, and claim boundary all confirmed unchanged and
correctly scoped (NULL_ONLY, finite 1+1D patch, singular-Schwarzschild-only per EGS's own
regular-BH caveat). **Independently re-derived and corrected the N-vs-intensity scaling: production
N is `intensity` directly (`generator.py:47`, `n = rng.poisson(intensity)`), NOT the previously
assumed ×`BOX_AREA`-inflated figure** — confirmed empirically against `gate0_tier1_result.json`
(`TOY_INTENSITY=9.0` produced observed `N∈[2,14]`, consistent with Poisson(9), not Poisson(9)×7.2).
So production `N∈{1500,3000,6000,12000}` is only 1.5–12× EGS's own `n=10³`, not 10–86× larger as
the (corrected) prior dossier stated. **No physical obstruction to the null-only calibration
itself**; general sprinkling-theory direction (not magnitude) suggests `EMPTY_FAMILY` should become
rarer, not more common, as N grows past the toy regime's near-single-chain artifact — but the
exact magnitude is genuinely unmeasured and only running would produce it. This brief did **not**
engage with the mathematician's orthogonal computational-feasibility finding (different seat,
different concern) — see falsifier's synthesis of the two below.

## 5. Falsifier attack

- **Concrete failure modes:**
  1. **The feasibility blocker survives scrutiny and is understated, not overstated, by the
     mathematician.** There is no rescue reading. `family_A` (`gate0.py:70-71`) is the only
     verified path; every downstream verified step (min-cut filtering, Dinkelbach driver,
     EMPTY_FAMILY detection itself) consumes the enumerated family. **Worse: D.1's membership
     constraint (`D=↓(D∩Max(C))`) is disjunctive — not a closure implication, not expressible as
     Picard ∞-edges, and not covered by D.2.2's forced-in/out trick. It is not merely that a
     polynomial implementation is unwritten — it is unproven that a polynomial algorithm for
     `max_{D∈𝒜(C)} S` exists at all.** Part E over-claims as written; it must be re-scoped or
     retracted, not merely re-verified.
  2. **An independent blocker wave 1 missed entirely: cover computation itself is `O(N³)` pure
     Python** (`is_cover`/`assert_partial_order`, `gate0.py:51-53`, `tier1.py:88-101`). At
     `N=12000` that is ~`1.7×10¹²` predicate calls *per draw*, before `family_A` even starts —
     the verified code path is infeasible at production N even if `|Max|` were tiny.
  3. **Memory, not just time:** `family_A` materialises a dict entry per admissible down-set;
     at production widths this risks OOM — process death with no verdict token at all.
  4. **On the corrected N-scaling:** re-deriving `|Max|` from box geometry
     (`|Max| ≈ c·R_EDGE·√ρ`) gives the same order of magnitude as the mathematician's √N estimate;
     this does not rescue anything — even the friendliest constant makes `N=1500` "marginal to
     infeasible with the verified code," and `N=12000` "categorically infeasible under any
     constant." **The corrected, smaller N-range does not change the severity conclusion.**
  5. **A remedy/freeze self-conflict nobody flagged:** any fix requiring a frozen per-draw
     compute budget collides with Part E's own frozen text ("Ningún cap de presupuesto puede
     introducirse en sprinkling sin reabrir la herida de censura," spec:498-501) — adopting a
     compute-budget fix requires amending frozen spec text via committee first, not just adding a
     token to a new script.
  6. **Dossier integrity:** confirms (independently of the chair) that the "production feasibility
     untested" finding is comité **018**'s, not comité 017's as mis-cited in this session's
     dossier — corrected in §2 above. Also notes the N-scaling error the physicist corrected this
     session was **already on record correctly in comité 015**, and comité 018 silently
     reintroduced the wrong scaling for a full cycle without any seat catching it — a concrete
     instance of this committee's own anchor-checking being fallible on exactly this class of
     numeric fact.

- **Ground-truth leakage:** None via the embedding in the frozen design. Two indirect paths
  flagged: (i) the kind-dimension ambiguity means a faithful "verbatim reuse" implementer could
  sprinkle and score BH patches *during calibration*, producing step-6-adjacent material before
  steps 4-5 execute, contaminating the freeze; (ii) feasibility-driven level selection (silently
  computing only the levels that happen to terminate) would let an unfrozen, computational
  convenience select the calibration domain.

- **Freeze violations:** authorizing execution now creates the operationally likely sequence:
  job stalls/OOMs at production N → operator kills it → code gets "optimized" mid-flight → re-run
  on the same already-consumed roots — unverified-code substitution outside Gate 0, plus a re-run
  after seeing partial state, manufactured by authorizing an infeasible plan. **A scoped
  "1500-only" partial authorization is explicitly rejected**: it does not dodge the blocker (even
  N=1500 is marginal-to-infeasible), addendum §3 freezes exactly the 4 levels with interpolation
  forbidden so a 1-level table cannot serve the frozen object, and it would burn calibration roots
  under code that will inevitably be replaced. Also flags that the `0271fd9` commit went through
  without running the comité-018 falsifier's own named acceptance check (the dual-consumption-plan
  diff), on a weaker "optional" reading of that prior brief's closing language than its body text
  ("adopted as the acceptance check... before it is committed") supports.

- **Verdict coercion:** `OUT_OF_DOMAIN_UNCALIBRATED` is well-frozen for exactly one failure
  (draw-budget exhaustion) but is **unreachable, not merely mistargeted**, at production scale:
  certifying `𝒜(C)=∅` itself requires completing the `2^{|Max|}` enumeration, so the "cheap when
  empty" half of the anti-correlation argument breaks down — a wall-clock stall or OOM has no
  frozen token, creating a standing temptation to log a killed level as
  `OUT_OF_DOMAIN_UNCALIBRATED` (a statement about the null distribution) when it is really a
  statement about the code failing. This is a silent coercion risk the current freeze cannot
  prevent, because the needed third state (`COMPUTE_INFEASIBLE` or similar) does not exist and
  Part E currently forbids the compute-budget precondition that would define it.

- **Premature / over-broad claims:** Part E's "se computa en tiempo polinomial para todo poset
  finito" is an over-claim about the wrong object (the fixed-λ closure step, not the
  𝒜(C)-restricted problem) and must be re-scoped in any future revision. The addendum's claim
  boundary otherwise remains clean (NULL_ONLY, claim-inert `rate_empty`, `NON_CORROBORATION`,
  finite-patch 1+1D) — no metric/asymptotic/3+1D creep found.

- **Independent-falsification gate: NOT satisfied.** Auditor 006 ran a token-match, not a
  feasibility or executability check (conceded by the chair, §2). The comité-018 falsifier's own
  named acceptance check for this exact addendum has not been run. Gate 0 verified the algorithm
  only at N≤14/16, a regime that structurally cannot exercise the now-alleged failure. No seat has
  produced a single measured number about the production regime.

- **Minimal falsification test:** a single, claim-inert, zero-frozen-seed check: on a documented
  **dev seed outside `EXPLORE_POOL`** (precedent: `SEED=20240617` pattern from `dev/backend.py`/
  `dev/gate_highN.py`), sprinkle MINK once at each of the 4 `INTENSITIES` using the
  already-verified, already-polynomial `past_matrix_fast` (no new algorithm needed for this
  measurement), and report `|Max(C)|` and `|covers|` only — wall-capped, writing nothing but a dev
  log. If `|Max|` at `12000` is `≥~30` (expected with near-certainty given the box geometry), the
  infeasibility of the only verified implementation is settled by arithmetic alone, without ever
  running `family_A` to completion. **This is the cheapest possible resolution of the open
  question and should run before any further authorization request, reversible and zero-cost.**
  The comité-018 dual-consumption-plan diff test remains a separate, still-mandatory precondition
  for the kind/spawn-form ambiguity, but is second in priority: it checks a plan that, as of today,
  no implementation could execute regardless.

**Falsifier's bottom line: do not authorize Part F step 3 under `0271fd9`.** The freeze text is
statistically adequate (comité 018's adjudication stands) but computationally unexecutable by the
only verified code, and authorizing it risks not a bad μ table but a stalled run whose likely
mid-flight remediation would itself breach the freeze discipline.

## 6. Pre-registration verdict

- **Verdict: BLOCK**
- **Freeze status:** The statistical object, M=200, spawn scheme, levels, root allocation, and
  OUT_OF_DOMAIN rule are frozen in writing prior to any validation seed being touched
  (`dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` §0-§5). **What is not frozen is the algorithm/code that
  would actually execute step 3 at production N.** The addendum's §2 freezes only the spawn
  scheme, verbatim-reusing Tier 1's recipe — it says nothing about which `S(C)`/`𝒜(C)`
  implementation computes the score once patches are sprinkled at production intensity.
- **Seal integrity:** matches (`6e2c3888…` = `docs/preregistration_002.md:8`, per auditor 006).
  Unrelated to the question at hand — that seal certifies prereg-002's estimator-v2 blind-run
  seal, not any μ-computation code path. **The relevant algorithmic gate is Gate 0 (D.2.3), whose
  own acceptance rule is explicit: "CERO discrepancias... BLOQUEA incondicionalmente el freeze de
  la tabla μ."** Independently confirmed by direct reading of `dev/measure_pr003_rvar_gate0.py`:
  even the "min-cut" path filters through the exponentially-enumerated family — Gate 0 verified
  the enumeration-dependent object, not a hypothetical polynomial-only one. Part E's "polynomial
  for any finite poset" claim describes `maxflow_mincut_closure()` alone, not the full pipeline
  that was actually run.
- **Seed discipline:** sound as written — `MU_CALIBRATION_ROOTS`/`MU_FALSIFICATION_TEST_ROOTS`
  disjoint, root `1_000_000` excluded, `VALIDATION_SEEDS` untouched and out of scope. **Moot if
  the code consuming those seeds cannot terminate.**
- **Reporting rule:** as written, the addendum correctly requires symmetric reporting of
  `OUT_OF_DOMAIN_UNCALIBRATED`/`INCONCLUSIVE`, with no silent coercion to PASS/FAIL — but this
  presupposes step 3 runs to completion in finite time. The typed ladder has **no state for
  "execution did not terminate for compute-budget reasons"** — a fourth possible outcome the
  addendum does not cover, as the falsifier also independently found.
- **Forbidden moves present?** Not yet committed, but the authorization-as-requested would create
  the conditions for one: **bundling two committing steps into one** — "run step 3" would
  implicitly license "write new min-cut/filter code first, then run it," without that new code
  passing its own Gate 0. This directly violates the project's own precedent twice over: comité
  017 §9 ("Granting the full S1-S5 order as a single blanket authorization risks collapsing two
  separable committing events") and the addendum's own §6 ("Gate 0 Tier 0 → Tier 1 requirieron
  cada uno su propia autorización explícita en vez de heredar la del paso anterior"). Writing and
  using new, un-gated min-cut/filter code to make step 3 tractable is a materially different act
  than "running Part F step 3 under the addendum" and cannot be retroactively covered by this
  authorization request.
- **Reasons:** anchored to `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` §6; `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md`
  D.2.3 (`:439-441`); direct reading of `dev/measure_pr003_rvar_gate0.py:67-79` and
  `mincut_argmax_in_family`; `docs/comite/comite_decision_017_r-var-v2-reconvene.md:182,425`;
  the kind-dimension gap independently confirmed by two wave-1 roles and the addendum's own
  literal text (Part F2: "sprinkling Minkowski del mismo box, **sin horizonte**" — no "kind" token
  anywhere).
- **Recommendation:** BLOCK authorization of Part F step 3 execution under `0271fd9` as currently
  scoped. Before any re-authorization: (1) run the falsifier's cheap dev-seed feasibility probe
  (reversible, zero EXPLORE_POOL cost) to settle the arithmetic question empirically; (2) if
  infeasibility is confirmed, require either a new polynomial implementation (if one is found to
  exist) fresh-Gate-0-verified as its own separate checkpoint, or an explicit committee-level
  decision to redesign Part F's approach; (3) close the kind-dimension ambiguity in writing and
  run the comité-018 diff test as a hard precondition regardless, since it is now doing real work
  it wasn't originally asked to do; (4) only then bring a fresh, narrowly-scoped execution request
  back to the PI/comité.

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| EGS arXiv:2605.06813, derived-md:237 ("400 sprinklings of average size n = 10³") | Physicist | CONFIRMED |
| Surya LRR2019 §4 / Bombelli 1987 — maximal-antichain size ~√N in 2D orders | Mathematician | UNVERIFIED — no "Surya LRR2019" document exists in `biblioteca/`; Bombelli 1987 discusses maximal antichains conceptually but has no explicit N^{1/2}-scaling derivation; the closest adjacent material (Bollobás–Brightwell, "width of random graph orders") appears only as a bibliography entry inside another document, not as primary content |
| EGS, derived-md:249 (regular/Hayward-type BH — longest-chain/future-cardinality partition "likely does not allow a partition") | Physicist | CONFIRMED (paper's caveat is specific to the 3+1D case; physicist's paraphrase omits that qualifier — minor imprecision, not misrepresentation) |
| `nachocausal/generator.py:47` (`n = rng.poisson(intensity)`, no `BOX_AREA` multiplication) cross-checked against `gate0_tier1_result.json` | Physicist | CONFIRMED (code-reading/empirical claim, independently re-read) |

- **Notes:** the mathematician's specific √N antichain-scaling citation is not anchored in
  material physically present in `biblioteca/` — flagged `UNVERIFIED`, not wrong; it is a
  plausible, textbook-adjacent fact for 2D random posets, but this project's library does not
  contain a primary source for it. This does **not** weaken the feasibility finding: the
  categorical blocker (`family_A` enumerates `2^{|Max|}` subsets, confirmed by direct code
  reading by two independent seats) does not depend on the exact scaling constant, only on
  `|Max|` being non-trivially large at production N, which both the mathematician's and
  falsifier's independent order-of-magnitude estimates agree on. Separately confirmed: **no
  material in `biblioteca/` addresses the complexity of R-VAR-like admissible-completion
  enumeration or min-cut approaches to this specific horizon-partition problem** — the closest
  adjacent content is an unrelated BDG-action complexity result and a generic Kleitman–Rothschild
  remark about causal-set enumeration in general. The project is on its own for this specific
  algorithmic question; nothing in the library resolves whether an efficient algorithm is known
  to exist.

## 8. Synthesis

**This session inverts the expected outcome.** The PI's question was narrow — "authorize execution
under the already-frozen, already-audited addendum" — and the natural expectation, given
`AUDIT_PASS` and two prior committee sessions' worth of closed gaps, was a straightforward
`RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`. Instead, **every substantive role that engaged with
computability — the mathematician, the falsifier, and the warden (via independent direct code
reading) — converged on a categorical blocker the freeze process never checked for**: the only
Gate-0-verified R-VAR implementation enumerates all `2^{|Max(C)|}` subsets of the maximal
antichain, a cost that was invisible at Tier 0/Tier 1's toy scale (`N≤14`) and is expected to be
catastrophic at production intensities regardless of the exact scaling constant (unverified in
biblioteca, per §7, but immaterial to the conclusion). The falsifier sharpened this further: it is
not merely that a fast implementation is unwritten, but that **it is unproven a polynomial
algorithm for this constrained problem exists at all**, given the disjunctive form of the D.1
admissibility predicate.

**No disagreement is hidden.** The physicist found no physical obstruction and, independently,
corrected a scaling error that had persisted uncaught from comité 018 through this session's own
draft dossier (production N is smaller than previously assumed) — but this correction, verified
by the falsifier's independent re-derivation, does **not** rescue the feasibility conclusion; the
severity is essentially unchanged. The reproducibility engineer and logician, working
independently, found the same second-order problem (an unresolved `KINDS`/spawn-form ambiguity
inherited implicitly from "verbatim reuse of Tier 1") from two different angles, both recommending
the comité-018 diff test be promoted from optional to mandatory. Auditor 006's `AUDIT_PASS` is not
contradicted — it correctly verified what it was scoped to verify (text-token fidelity to comité
018's adjudication) — but it was never a feasibility check, and treating it as license to execute
would over-read its scope.

**This is not a "the freeze needs one more revision pass" situation like comité 018's was.** That
session found five well-specified, individually small drafting gaps, closeable in one revision
pass — which happened (`0271fd9`). This session's finding is different in kind: a genuine,
possibly open research question (does an efficient algorithm exist for `max_{D∈𝒜(C)} S`?) sitting
underneath a statistically-sound, textually-complete freeze. No revision to the addendum's prose
closes this; either a new, correctly verified algorithm needs to be found and separately
Gate-0'd, or Part F's approach needs to be reconsidered at the specification level, or (cheapest,
first) the actual severity needs to be measured rather than argued from asymptotics.

## 9. Next-step spec

**Reversible steps (zero seeds from `EXPLORE_POOL`, zero committing action — may be done now if
the PI asks):**

1. **Run the falsifier's feasibility probe.** On a documented dev seed *outside* `EXPLORE_POOL`
   (precedent: `SEED=20240617`, per `dev/gate_highN.py`/`dev/backend.py`), sprinkle MINK once at
   each of the 4 `thresholds.INTENSITIES` using the already-verified `past_matrix_fast`, and
   report only `|Max(C)|` and `|covers|` (no scoring, no `𝒜(C)` enumeration attempted). Wall-clock
   capped; writes nothing but a dev log. This settles by direct measurement whether `2^{|Max|}` is
   in fact catastrophic at each production level, replacing asymptotic argument with a number.
2. **Run the comité-018 dual-consumption-plan diff test** (two independent agents write the exact
   `(root, child_index[, kind])` consumption plan from the addendum text alone and a mocked
   oracle, then diff). Now explicitly a hard precondition per two independent wave-1 findings this
   session, not merely optional as the addendum's prior closing summary framed it.
3. If step 1 confirms infeasibility (expected), the PI/committee may choose among: (a) commission
   a new, genuinely polynomial `𝒜(C)`-restricted implementation (if the falsifier's disjunctive-
   predicate concern can be resolved) and require it pass its own fresh Gate 0 (zero-discrepancy
   against the existing brute-force reference at `N≤16`) before any μ-table computation touches
   it; (b) reconsider Part F's design at the specification level (a new committee question, not a
   drafting fix); (c) restrict production intensities to a level where step 1's measured `|Max|`
   is small enough to be tractable, IF such a level exists among the frozen four — noting the
   falsifier's objection that a *fewer-than-4-levels* table would not satisfy the addendum's own
   frozen "exactamente los 4 niveles" requirement without a further committee-level amendment.

**Committing step (NOT authorized by this brief; requires its own future, separately-authorized
session once step 1's measurement exists):**

4. Execution of Part F step 3 itself — sprinkling `MU_CALIBRATION_ROOTS`/`MU_FALSIFICATION_TEST_ROOTS`
   and computing `μ_n`. **Blocked pending the reversible steps above.**

**Falsifier's minimal falsification test:** the dev-seed `|Max|`/`|covers|` measurement in step 1,
adopted as the mandatory first move before any further Part F authorization request.

**Binding rules pre-committed:** `NO_RECONSTRUCTION_CLAIM` (unaffected, out of scope here);
`NO_POST_HOC_TUNING`/`NO_THRESHOLD_LOOSENING` (nothing here loosens M, α, or the levels; a future
compute-budget rule, if adopted, would itself need to amend Part E's current no-budget-cap text
via committee, not be smuggled in); `NO_GROUND_TRUTH_LEAKAGE` (the feasibility probe touches no
embedding-dependent quantity, only `|Max|`/`|covers|` on dev seeds); `RESPECT_SEAL_FREEZE`
(nothing here touches `nachocausal/` or the seal). `Q_DISPOSITION`, `OVERALL_VERDICT(014)`,
`CIRCULARITY_STANDARD=FUNCTIONAL_ONLY`, `ALLOY_003_AUTHORIZATION_STATUS=NOT_AUTHORIZED` all
unchanged. The mid-session uncommitted edit to the addendum (§2 above) is noted but neither
authorized for commit nor required to be reverted by this brief — it closes an orthogonal
ambiguity and does not bear on this verdict.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_DO_NOT_PROCEED

## 11. User sign-off

_(left blank for the user — decision, date, and any overriding notes)_
