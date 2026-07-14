# Comité Decision 022 — pr011-viability-freeze-readiness

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Should the **PR011 mass-distinguishability viability specification** — with numeric anchor filled
(shape A moderate, certification pair `τ=0.95` vs `1.05`, channel `N=n`, primary method exact
enumeration) — be **frozen as a research-program document**, and what **scoped next step** (if any)
is authorized: spec-only freeze, reversible dev pre-flight (enumeration scaffold), or TV
certification execution?

## 2. Verified state

Facts checked **this session**, each with its command / file:line.

- **Seal intact.** `make verify-seal` → `thresholds.py sha256 =
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`; matches
  `docs/preregistration_003.md:9` and `docs/preregistration_002.md:8`.
- **Git.** HEAD `11ef1d64d72a337bfdc8723e917a3477c171a825` (`git rev-parse HEAD`). Working tree
  **not clean**: modified `dev/run_pr010_reference_depth_coverage_development.py`,
  `tests/test_pr010_reference_depth_coverage_development.py`, `research_program/README.md`,
  `research_program/work_packages/README.md`, `research_program/work_packages/wp4_two_point_theorem.md`;
  untracked `research_program/synthesis/` (incl. PR011 spec), `dev/pr011_freeze_sanity_check.py`,
  `tests/test_pr011_freeze_sanity.py`, PR010 coverage CSV/sha256, `pr009-separation-optimization.patch`.
  `nachocausal/` **unmodified** (`git status --short` — no `M nachocausal/`).
- **PR011 geometry sanity.** `python3 dev/pr011_freeze_sanity_check.py` → `PR011_FREEZE_SANITY=PASS`;
  `python3 -m pytest tests/test_pr011_freeze_sanity.py -q` → 1 passed.
- **Kappa anchor reproducible.** `python3 research_program/work_packages/wp4_kappa_numeric_reference.py`
  (head) → shape A moderate `V=1.471720`, `kappa=7.969751e-04` at `tau=1`, corners `r_p=2,r_q=0.5,
  v_p=0,v_q=1` — matches `research_program/synthesis/pr011_mass_distinguishability_viability.md` §3.1.
- **PR010 status.** PR010 remains an open coverage-design front (`research_program/README.md:93-76`);
  no PR010 terminal committed in `docs/`. G0 in PR011 spec §10 is **OPEN**.
- **Mechanical audit (chair).** `bash .claude/skills/auditor/audit.sh` → 0 errors, 12 warnings
  (pre-existing committed CSVs without generator refs in tree); seal OK. Not a full `/auditor` report
  for PR011 — no PR011 numbers are claimed yet.
- **No TV certification executed.** No `dev/pr011_tv_certification_*.py` exists; no `data/reports/pr011_*`.
- **No sealed path invoked.** No `make test` / `validate.run()` this session.

## 3. Dossier

Files and references supplied to the committee:

- `research_program/synthesis/pr011_mass_distinguishability_viability.md` — freeze candidate (§3–§6
  numeric anchor filled)
- `research_program/synthesis/geometric_indeterminacy_decision.md` — program synthesis
- `research_program/work_packages/wp4_two_point_theorem.md` — proved two-point bound
- `research_program/work_packages/wp4_fisher_localization_floor.md` §4–5a — diamond family + kappa
- `research_program/work_packages/wp4_kappa_numeric_reference.py` — numeric anchor source
- `research_program/models/first_witness_pair_candidates.md` §2 — Theorem A (`TV=0` scale orbit)
- `dev/pr011_freeze_sanity_check.py`, `tests/test_pr011_freeze_sanity.py`
- `docs/preregistration_003.md` §2, §7 (OPEN minimax-over-`C`; NOT conflated with (★))
- `docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md` — composite
  adversary caveat
- Binding guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
  `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

- **Proposed artefact(s):** (i) frozen spec at
  `research_program/synthesis/pr011_mass_distinguishability_viability.md` with status
  `FROZEN_VIABILITY_SPEC`; (ii) optional reversible dev script
  `dev/pr011_tv_certification_enumeration.py` + test; (iii) certification report
  `data/reports/pr011_tv_certification_*.csv` **only after** execution authorization. No
  `docs/preregistration_*` file — PR011 is explicitly not a sealed prereg
  (`pr011_mass_distinguishability_viability.md:5-8`).
- **Environment & seal:** Pre-flight only. `make verify-seal` must match `6e2c3888…` before/after
  any write. Enumeration uses **no** sealed `nachocausal/validate.py` path; may read
  `nachocausal/generator.py` geometry patterns only if a future script copies the diamond law —
  today no such script exists. No GPU, no seeds, no RNG for viability certification.
- **Provenance capture:** Freeze record must cite HEAD, seal SHA, commit of spec freeze, and
  explicit "no PR009/PR010 scientific inputs" (`pr011 spec §12`). Any report must name method tier,
  `n`, `ε`, and error budget (`§6.1`).
- **Run mechanics:** `pr011_freeze_sanity_check.py` is deterministic foreground, exit 0 — PASS.
  Enumeration at `n=4` is the first feasibility probe; spec orders `4→8` with 1h CPU ceiling
  (`§6.1`). Working tree is dirty — **commit order matters**: spec freeze should not be presented
  as executed while PR010 dev files sit uncommitted alongside unless provenance headers disambiguate.
- **Reproducibility risks:**
  - Counting unlabeled posets `|Ω_n|` is not the hard part; **computing** `P_n(τ)(c)` for each class
    requires a certified sprinkling-to-poset map — not yet implemented.
  - Kappa numbers are quadrature references, not poset-law certification — must not be cited as `ε`.

### Mathematician brief

- **Computability:** On `Ω_n` (finite), TV is well-defined. Channel `N=n` conditioned closes
  cardinality leak (`wp4_two_point_theorem.md` Obs. 5.2). Diamond family satisfies `r_q < τ < r_p`
  and horizon straddle for all frozen `τ` values (`dev/pr011_freeze_sanity_check.py` PASS).
- **Order law:** For `N=n`, law is pushforward of `n` i.i.d. uniform draws on `D_τ` through causal
  order + unlabeling. Poset is a function of copula ranks (Lemma 1, `first_witness_pair_candidates.md`)
  on the null box — diamond is a null box (`wp4_fisher` §4). Compared pair `(τ_0,τ_1)=(0.95,1.05)`
  is **not** on the scale orbit of Theorem A (fixed corners, varying `τ` only).
- **Distinguishability expectation:** `TV(P_n(0.95), P_n(1.05))` should be **strictly positive** for
  some `n` in the regular family (Fisher `Ī > 0` on `[τ_0^fam,τ_1^fam]`). **Upper bound `ε` is not
  proved** until enumeration/coupling runs. Viability terminal `PAIR_DISTINGUISHABLE` requires
  `ε < 1`, not `ε ≈ 0`.
- **Caveats:** Exact enumeration requires summing over **all** unlabeled posets with correct masses —
  implementation non-trivial. Fallback Hellinger on copulas bounds laws on **latent ranks**, not
  posets without Lemma 1 + data processing. Composite adversary N/A for fixed simple pair.

### Mathematical logic brief

- **Claim structure:** PR011 separates (a) **spec freeze** (definitions, exclusions, terminals),
  (b) **certification execution** (numeric `TV`), (c) **interpretation** (two-point corollaries).
  The spec preserves this layering (`§2.1–2.2`, `§7`, `§8`). No quantifier shift from "estimator
  fails" to "no estimator can" without certified `ε`.
- **Freeze vs execution:** Spec §10 gates both "frozen" and "executed" on PR010 close — logically
  conflates **document freeze** with **empirical gate**. Recommend splitting: `FROZEN_VIABILITY_SPEC`
  (allowed now) vs `EXECUTION_AUTHORIZED` (requires G0).
- **Terminal discipline:** Terminals in `§8` are mutually exclusive and do not coerce
  `CERTIFICATION_INCOMPLETE` into indeterminacy — consistent with `wp3b` tier rules.
- **Minimax phrasing:** Spec correctly does not amend `prereg-003` (★); fills OPEN §7 programmatically.
  No universal "no estimator" claim without exhibited `ε`.

### Physicist brief

- **Coordinates & patch:** EF diamond with corners `(0,2)` exterior / `(1,0.5)` interior; family
  `τ ∈ [0.8,1.2]`; certification at `τ=0.95,1.05`. Horizon straddle verified (`Ũ_p < 0 < Ũ_q`).
  Patch avoids `r=0` singularity face (`wp4_fisher` §4: `r_q > 0`).
- **Target:** `T(τ)=τ=2M` is the **horizon-radius parameter within the frozen chart**, not absolute
  physical meters (Theorem A blocks absolute `r_s` from order alone). Consistent with bounded claim.
- **Not event horizon:** Finite patch, teleological caveat (`pr011` inherits synthesis §11). PR011
  asks **parameter distinguishability** in `G_◊`, not global horizon reconstruction.
- **Shape A moderate:** Not the thinnest near-horizon diamond (which shrinks `κ` sharply per
  `wp4_fisher` §5a item iii) — reasonable first viability shape; **not** tuned from PR009/PR010 data
  (anchor predates this session's PR010 CSVs).
- **Caveats:** EF 1+1D Schwarzschild singular, not Hayward-regular — conclusions are
  singularity-adjacent family only (`prereg-003` §2). Mass pair separation `Δτ=0.1` is O(1) in
  family span — appropriate for viability, not fine-tuning.

## 5. Falsifier attack

**Concrete failure modes**

1. **G0 contradiction.** Spec requires PR010 close before freeze **or** execution (`§7-8`, `§10`).
   Freezing today while PR010 is open violates the spec's own gate unless G0 is split (logic brief).
2. **Enumeration infeasibility mislabeled as science.** `|Ω_8| ≈ 1.7×10^4` but computing each
   mass needs integrating over sprinkle configurations — likely **far** harder than the 1h ceiling;
   risk of `INFEASIBLE_AT_TRACTABLE_N` without proving indistinguishability.
3. **κ anchor smuggled as TV.** `kappa ≈ 8×10^{-4}` suggests large Fisher scale but **does not**
   substitute for poset-law `TV` — citing kappa as viability evidence would be verdict coercion.
4. **Dirty working tree.** PR010 dev modifications + untracked PR011 files in one tree — risk of
   presenting PR011 as "clean freeze" while PR010 science is co-mingled in commits.
5. **Minimax overclaim migration.** If terminal `PAIR_DISTINGUISHABLE` is read as "masses
   estimable in nature" rather than "within `G_◊` at certified `n`" — violates `NO_RECONSTRUCTION_CLAIM`.

**Ground-truth leakage:** None in spec — order-only channel; embedding absent from estimator class.
Kappa script uses geometry only — OK for anchor, not for order law.

**Freeze violations:** Freezing in `research_program/` does not touch `thresholds.py` — OK. Risk:
committing `data/reports/pr011_*` without generator test — auditor WARN pattern.

**Minimal falsification test**

> At `n=4`, `τ_0=0.95`, `τ_1=1.05`, with frozen corners, **compute or prove** whether
> `P_4(τ_0)` and `P_4(τ_1)` assign **identical** mass to every unlabeled 4-element poset. If yes
> (`TV=0`), the pair is indistinguishable at `n=4` and viability must not be claimed at that `n`.
> One-page calculation or script; no seeds.

## 6. Pre-registration verdict

- **Verdict: PASS** (for **research-program spec freeze only**; not a `docs/preregistration_*` freeze)
- **Freeze status:** PR011 numeric anchor is pre-committed in writing (`pr011 spec §3.1–3.2`, `§5`,
  `§6.1`) without using PR009/PR010 scientific outputs (`§12`). No validation seeds required for
  spec freeze. **Execution** of TV certification is a separate authorization with its own error
  budget — not a prereg-001/002/003 threshold step.
- **Seal integrity:** Step does not modify sealed instrument; `6e2c3888…` intact; `nachocausal/` 0 M.
- **Seed discipline:** No seeds burned. Enumeration route is deterministic; no `RESERVED_002` /
  `EXPLORE_POOL` requirement for spec freeze.
- **Reporting rule:** Terminals `§8` forbid coercing incomplete certification into indeterminacy
  or recoverability. PASS/FAIL/INCONCLUSIVE pattern applies to viability terminals, not prereg-002.
- **Forbidden moves present?** None in the spec text. **Risk:** executing before PR010 close if user
  treats freeze as full G0 discharge — spec ambiguity (see §8).
- **Reasons:** PR011 is explicitly not sealed prereg (`§5-8`); does not loosen frozen thresholds;
  does not claim reconstruction; separates viability from estimator channels. Warden **BLOCK** would
  apply only if this were smuggled as `docs/preregistration_004.md` without a separate deliberation.

## 7. Literature verdict

| Claim | Status | Anchor |
|---|---|---|
| Two-point / Le Cam bound | Standard; repo PROVED | `wp4_two_point_theorem.md` §3 |
| Diamond EF regularity | PROVED in repo | `wp4_fisher_localization_floor.md` §4 Lemma R, Prop. 4 |
| Theorem A scale blindness | PROVED in repo | `first_witness_pair_candidates.md` §2 |
| Tsybakov 2009 in biblioteca | [UNVERIFIED this session] | `prereg-003` §7 O4; comité 005 |
| Bombelli statistical Lorentzian geometry | Cited in synthesis §19 | biblioteca not line-checked this session |

**Notes:** PR011 execution does not require new literature if it stays on proved repo theorems.
External memo still needs Tsybakov sourced per O4.

## 8. Synthesis

**Recommended direction:** **Freeze the PR011 viability spec now** as `FROZEN_VIABILITY_SPEC` in
`research_program/synthesis/` after user sign-off, with a **binding amendment** to §10 gates:

- **G0a (spec freeze):** allowed once this comité brief is signed — no PR010 dependency.
- **G0b (TV certification execution):** remains blocked until PR010 closes under its own rules.

**Ranked alternatives**

1. **(Recommended)** Spec freeze now + reversible dev scaffold (`pr011_tv_certification_enumeration.py`
   structure + `n=4` feasibility probe only) — **no** terminal emitted until execution authorized.
2. Wait for PR010 close, then freeze spec and execute certification in one step — cleaner G0, slower.
3. Do not freeze — keep `FREEZE_CANDIDATE` until PR010 terminal exists — most conservative, delays
   identifiability track.

**Open disagreements (not hidden)**

| Issue | Positions |
|---|---|
| G0 timing | Spec author: PR010 before freeze **or** execute (`§10`). Logic + falsifier: split freeze vs execution. Repro: dirty tree needs commit discipline. |
| Primary method | Spec: exact enumeration. Falsifier: likely infeasible at `n≥6` within 1h — may need copula Hellinger fallback earlier than ladder suggests. |
| κ reference | Physicist: good shape choice. Falsifier: must not substitute for `TV`. |
| Doc location | Warden PASS for `research_program/`; would BLOCK `docs/preregistration_004` without new question. |

No pre-registration BLOCK. Falsification test is concrete but not yet run — does not block spec
freeze; **does** block emitting any viability terminal.

## 9. Next-step spec

### Reversible (may run if user asks — not authorized by this brief alone)

1. **Amend PR011 §10** to split G0a/G0b as in §8 (chair/user edit).
2. **User sign-off** on this comité brief → set spec status `FROZEN_VIABILITY_SPEC`.
3. **Commit** `research_program/synthesis/*`, `dev/pr011_freeze_sanity_check.py`,
   `tests/test_pr011_freeze_sanity.py` — separately from PR010 dev changes.
4. **Scaffold** `dev/pr011_tv_certification_enumeration.py` (law computation stub + `n=4` probe);
   add test that fails until masses sum to 1.
5. Run **falsifier minimal test** (§5): check `TV=0` vs `TV>0` at `n=4` — deterministic only.

### Committing (only on explicit user authorisation)

1. **TV certification run** producing `data/reports/pr011_*` and a viability terminal — requires
   **G0b** (PR010 closed) + user execution authorization + `/auditor` on reported `ε`.
2. Any `docs/preregistration_004.md` for mass-estimation scaling — separate `/comite`.
3. No changes to `nachocausal/thresholds.py`, sealed validation, or PR010 protocol.

**Binding rules pre-committed:** order-only + `N=n`; pair `(0.95,1.05)` fixed; no PR009/PR010 inputs;
no reconstruction; κ is not `ε`; terminal only with certified upper TV bound or proved `TV=0`.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_CAVEATS

## 11. User sign-off

**Decision:** Authorize spec freeze + G0a/G0b amendment (option `freeze_spec`).

**Date:** 2026-07-14

**Notes:** TV certification execution remains blocked until PR010 closes (G0b). Freeze-text audit:
`docs/auditor/auditor_report_007_pr011-viability-freeze-text.md` (`AUDIT_PASS_WITH_WARNINGS`).
Commit PR011 bundle separately from PR010 dev artefacts.