# Comité Decision 016 — prereg002-supervised-reverification

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

PI, 2026-07-04, verbatim: "Solicito veredicto procedimental sobre prereg-002. Hecho nuevo: el
artefacto primario del PASS prereg-002 no es recuperable. La segunda máquina no está disponible y
la búsqueda exhaustiva en la máquina actual fue negativa. El repositorio ya marca el respaldo del
PASS como [UNVERIFIED_PRIMARY_MISSING] / [UNVERIFIED]. Pregunta única: ¿Autoriza el comité una
re-verificación supervisada de prereg-002 usando el mismo instrumento sellado, mismo commit,
mismos seeds congelados y misma banda virgen, etiquetada explícitamente como
SUPERVISED_REVERIFICATION, y sin presentarla como la primera evaluación ciega original? Opciones
aceptables: A) Autorizar la re-verificación supervisada bajo etiqueta explícita. B) Prohibir la
re-verificación y mantener prereg-002 como PASS reportado pero no auditable. C) Autorizar solo
una auditoría documental sin relanzar el instrumento. No solicito cambios de código, nuevos
modelos, nuevas seeds ni relajación del sello." PI's stated vote: A, explicitly not assumed.

## 2. Verified state

Facts checked **this session** (2026-07-04), each with its command / file:line.

- Seal: `make verify-seal` → `nachocausal/thresholds.py` sha256 =
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, MATCHES
  `docs/preregistration_002.md:8`. Independently re-confirmed by the warden at BOTH commits:
  `git cat-file -p 573cfcb:nachocausal/thresholds.py | sha256sum` = same hash.
- Sealed path byte-identical between seal commit and HEAD:
  `git diff --stat 573cfcb..HEAD -- nachocausal/` = only two additive files
  (`c1_selector.py` +80, `selection_guard.py` +84, 0 deletions), neither imported by
  `validate.py:21`. Verified independently by reproducibility engineer, warden, and literature
  verifier.
- git HEAD = `abf90f0`. `Horizon.lean` restored to HEAD 2026-07-03 (comité 015 precondition,
  user-authorised). Untracked: comité 015 brief, auditor 005 report, R-VAR specs v1/v2.
- Auditor 005 (`docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md`):
  `AUDIT_VERDICT=AUDIT_FAIL` (1 ERROR, 2 WARN). ERROR: the artifact cited at
  `docs/preregistration_002_result.md:11` contained the prereg-001 FAIL (seeds 11…65537,
  instrument `ad02cb57…`), mtime 2026-06-21 12:14 predating the prereg-002 seal commit
  `573cfcb` (2026-06-22 12:20:06). WARN: 13m14s window between seal commit and PASS record
  commit `fee12d5` (12:33:20) vs 32.5 min for the smaller prereg-001 run on this machine.
  WARN: no launch provenance snapshot for the PASS (the FAIL has one).
- Precision correction (falsifier, hygiene): the accurate statement is that no **run/log/output
  artifact** on this machine contains any virgin-band seed — the seeds themselves are of course
  present in `nachocausal/thresholds.py:66-70` and `docs/preregistration_002.md` (spec/text
  artifacts). Auditor 005 stated it correctly; over-compressed summaries must not drop the
  qualifier.
- NEW FACT (PI attestation, 2026-07-04): the second machine is NOT available; recovery is not a
  live option. `PRIMARY_PASS_ARTIFACT = UNAVAILABLE`, definitive. Label in force:
  `[UNVERIFIED_PRIMARY_MISSING]` (`results/README.md`). `results/prereg002/` exists and is
  empty (verified by literature verifier). `results/prereg001/` holds the archived FAIL
  artifacts (mtimes preserved).
- Falsifier's in-git seed-shopping test, executed this session (read-only):
  `git log --all -S "VALIDATION_DRAW_SEED" -- nachocausal/thresholds.py` and
  `git log --all --oneline -S "2076703"` → single introduction at `573cfcb`; no alternate
  draw-seed value exists anywhere in git history, on any branch. In-git seed shopping is
  falsified. Off-git shopping on the unavailable machine remains untestable in principle.
- Binding texts (verbatim, line-verified): `docs/preregistration_002_result.md:12` "First and
  only evaluation of the held-out band."; `docs/preregistration_002.md:61-63` "the single blind
  `validate.run()` on these seeds is the only evaluation … It is launched once.";
  `docs/preregistration_002.md:64-67` "the outcome ... is recorded and reported regardless of
  which it is. No post-hoc tuning, no re-running on fresh seeds after seeing a result, no
  loosening a frozen threshold."; `docs/preregistration.md:77-78` "The author of a claim is
  never its sole verifier."
- Context: comité 015 = `RECOMMEND_REVISE_AND_RECONVENE` (R-VAR); R-VAR spec v2 written
  (`dev/PR003_R_VAR_SELECTOR_SPEC_V2.md`), execution explicitly paused pending THIS decision.

## 3. Dossier

- `docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md` (foundation audit —
  this committee stands on its AUDIT_FAIL, per the /auditor–/comite contract)
- `docs/preregistration_002.md`, `docs/preregistration_002_result.md`,
  `docs/preregistration_001_result.md`, `docs/preregistration.md`,
  `docs/preregistration_001_addendum.md`
- `docs/estimator_v2_seal.md`, `docs/estimator_v2_freeze.md`, `docs/estimator_v2_decision_spec.md`
- `nachocausal/validate.py`, `estimator.py`, `gate.py`, `generator.py`, `thresholds.py`,
  `fixtures/tau_table.json`; `Makefile`
- `results/README.md`, `results/prereg001/*` (archived FAIL artifacts)
- `docs/comite/comite_decision_014` (scoped-authorization precedent), `comite_decision_015`
- `README.md`, `docs/hoja_de_ruta_23/24/25_jun_2026.md` (downstream dependency chain)
- PI framing (verbatim): "Relanzar sí puede producir evidencia, pero no puede recrear la
  evidencia primaria perdida."

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

**Proposed artefact(s) (option A only).** The sealed entrypoint is hard-wired to write `results/{label}.json` with `label="validation"` (`validate.py:217-222`, `:230`), and `results/` is git-ignored by design (auditor 005 §4; `results/README.md:1`). To make a `SUPERVISED_REVERIFICATION` artefact that can *never* be confused with the lost primary, capture into a dedicated, self-labelling directory `results/prereg002_reverification/` (the sibling of the now-`UNAVAILABLE` `results/prereg002/`, `results/README.md:11-20`):
- `validation_SUPERVISED_REVERIFICATION_2026-07-04.json` — the raw `validate.run()` verdict dict (the object `_write` emits, `validate.py:217`), copied out of the frozen entrypoint's `results/validation.json` immediately after the run.
- `reverification_run.log` — full stdout/stderr of the single invocation (mirrors `results/prereg001/validation_run.log`).
- `reverification_provenance.txt` — the launch/finish snapshot (schema below), modelled on `results/prereg001/validation_provenance_launch.txt` — the very file whose *absence* for the PASS is auditor 005 WARN 3 (`docs/auditor/...005...:135`).
- `SHA256SUMS` — checksums of all three plus the sealed `thresholds.py`.

Every filename and the directory name carry the string `reverification`/`SUPERVISED_REVERIFICATION`; the JSON should also carry `label="reverification_supervised_2026-07-04"` (a call-time argument, not a code edit) so the artefact self-identifies even if moved. This directly answers auditor 005's remediation (a)/(b) (`...005...:154-158`).

**Environment & seal.**
- Seal SHA must be re-verified *before* and *after* the run: `make verify-seal` → must print `6e2c3888…12bfefd4`, matching `docs/preregistration_002.md:8` and the chair's this-session check. `assert_environment()` additionally hard-fails if numpy ≠ `1.26.4` (`thresholds.py:18-32`, `PINNED_NUMPY`; called at `validate.py:157`). Pins to reproduce the sealed venv: numpy==1.26.4, Python 3.12.3, pytest 8.4.2 (`results/prereg001/validation_provenance_launch.txt:6-16`).
- Checkout question — **the sealed path is byte-identical between seal-era `573cfcb` and HEAD `abf90f0`.** `git diff 573cfcb..HEAD -- nachocausal/` (run this session) shows **only two additions**: `nachocausal/c1_selector.py` and `nachocausal/selection_guard.py`. Neither is on the sealed path: `validate.py:21` imports only `estimator, gate, generator, thresholds` and `from .scoring import blind_bracket`. `thresholds.py` is unchanged (not in the diff), consistent with the intact seal SHA. So a run at HEAD is numerically identical to one at `573cfcb`. Recommendation: still run from a detached checkout of `573cfcb` (the commit the PASS record names, `docs/preregistration_002_result.md:11`) so the provenance line reads exactly the sealed commit and the two unrelated untracked-era files are absent — cleaner audit trail, zero behavioural difference.

**Provenance capture (the snapshot this run MUST record — the gap that sank the primary).** Reproduce every field the FAIL run captured and the PASS never did (`...005...:74-77`, WARN 3): `captured_utc`, `start_utc`, `finish_utc`, `elapsed`; `commit` (full sha + `git status --porcelain` = clean on the sealed path); `thresholds_sha256` (from `make verify-seal`, before and after); `uname -a`; `python --version`; full `pip freeze`; `make test` result (the FAIL run recorded "10 passed"); and — beyond the FAIL snapshot — a **per-seed line log** (seed, N, sep_BH, sep_MINK, abstained flags, bracket) for all 20 seeds × 4 intensities, plus `SHA256SUMS` of the outputs. Record `NACHOCAUSAL_MINZ_PATH`/`OMP_NUM_THREADS` state too. This is the whole point of the exercise: the reverification artefact must be *self-corroborating* so it can never itself become `[UNVERIFIED_PRIMARY_MISSING]`.

**Run mechanics.**
- Single invocation of the unmodified sealed path: `python -m nachocausal.validate` (the exact entrypoint the PASS record cites, `docs/preregistration_002_result.md:11`; `validate.py:225-233` runs `run()` with defaults — `seeds=None`→`VALIDATION_SEEDS`, `guard=True`, `label="validation"`, `write=True`). No `seeds=`, no `guard=False`, no threshold mutation. Do **not** route through `dev/run_validation_instrumented.py`; even though its provenance note claims a pass-through wrapper (`results/prereg001/validation_provenance_launch.txt:18`), a supervised reverification should exercise the module verbatim and capture provenance out-of-band, so no wrapper can be questioned.
- Expected runtime on THIS machine: prereg-001 (80 `_per_seed` calls, each building BH+MINK) took 32.5 min (`results/validation_run.log`; auditor 005 WARN 2). Prereg-002 has the same 20 seeds × 4 intensities = 80 `_per_seed` calls; the τ-gate reads a *precomputed* fixture (`gate.py:23-29`, no live Monte-Carlo) so it adds negligible cost. Extrapolated: **~30-35 min, order-of-hour worst case**, i.e. many multiples of the 13m14s seal→record window that auditor 005 flags as implausible on this host (WARN 2). Budget for background execution.
- Abort conditions (pre-committed): seal SHA ≠ frozen value → abort before run; numpy ≠ 1.26.4 → `assert_environment` aborts (`thresholds.py:27`); `assert_coordinate_uniform` (Glue-3) raises (`validate.py:85`, `generator.py:53-84`); `verify_order_only` raises (`validate.py:92`, `estimator.py:164-183`) — any raise is a *finding*, reported, not retried.
- **Pre-committed mismatch rule (mandatory, decide before running):** a faithful replay must reproduce the transcribed table (`docs/preregistration_002_result.md`) bit-for-bit. If the verdict or any scored number **differs**, that outcome is reported *as-is* and **falsifies the transcription** — it is NOT grounds to re-run on fresh seeds (forbidden, `docs/preregistration_002.md:64-67`), loosen a threshold, or bury the run. If it **matches**, it *corroborates* the transcription but does not — and must not be presented to — restore the lost primary blind evaluation (PI framing: "no puede recrear la evidencia primaria perdida"; `docs/preregistration_002_result.md:12` "first and only evaluation" is spent). Either way the artefact is labelled `SUPERVISED_REVERIFICATION`, never "blind first eval". This is fully consistent with the frozen text: the prohibition names *fresh* seeds; this run uses the *same* frozen `VALIDATION_SEEDS`, same instrument, same commit.

**Reproducibility risks / ambiguities.**
- Cross-machine bit-for-bit is *well-supported but not contractually guaranteed*: the entire sealed path is pure numpy with no BLAS/linalg call — RNG is `np.random.default_rng(seed)` PCG64 (`generator.py:46`, `estimator.py:176`), point cloud from `rng.poisson`/`rng.random` (`generator.py:47-49`), poset from elementwise comparisons (`generator.py:88+`), observable from integer column sums (`estimator.py:113-119`), split/gate from `np.sort` on floats (`estimator.py:92,138`). NumPy's PCG64 stream and IEEE-754 elementwise ops are documented reproducible across platforms *for the same numpy version*; there is no matmul/reduction whose thread order could vary. So under the pinned numpy 1.26.4 a match is expected — but the guarantee is empirical, so a mismatch would be diagnostic (env drift), not automatically a transcription failure. [Partly UNVERIFIED: I did not execute to confirm cross-arch bit-identity.]
- Nondeterminism sources in `validate.run`: none found on inspection. All RNG is explicitly seeded; the τ-table is a frozen JSON fixture, not live MC (`gate.py:5-6,23-29`); `signflip_perm_p` uses exact enumeration for n≤20 (our n=20, `validate.py:41-45`, `thresholds.py:85`), so no sampling RNG is hit at the validation ensemble size. `two_means_split` ties are broken deterministically by `np.sort` order (`estimator.py:80-92`). [UNVERIFIED that no tie-sensitivity exists in the specific virgin-band clouds — deterministic regardless, but worth noting a knife-edge split value would still be reproducible.]
- Sealed-code delta vs HEAD: confirmed additive-only (two unused new modules), so no behavioural divergence — but this is *why* running from `573cfcb` detached is the tidiest choice (removes the two untracked-era files from the provenance picture entirely).
- Scope note (not my adjudication, flagged for the warden/falsifier): the `results/` directory is git-ignored (`.gitignore:21`), so even a successful reverification artefact is not itself committed — the durable record must be a committed provenance note/transcription (as with the PASS), which reproduces the *exact* fragility auditor 005 identified unless the provenance file + checksums are committed alongside. Recommend committing `reverification_provenance.txt` + `SHA256SUMS` to `docs/` or a tracked location, not leaving them only under git-ignored `results/`.

### Mathematician brief

- **Computability.** `validate.run()` at `573cfcb` is a deterministic pure function of (code, `VALIDATION_SEEDS`, numpy build). Randomness sources, all seeded or absent:
  1. Sprinkle — `generator.numpy_sprinkle`: `rng = np.random.default_rng(seed); rng.poisson(intensity); rng.random((n,2))` (generator.py:46-49), seeded by the frozen per-seed validation seed. PCG64 is platform-independent given the numpy version.
  2. Guard-v — `verify_order_only`: `rng = np.random.default_rng(seed)` with the same run seed (estimator.py:176-178, called at validate.py:92). Affects only raise/no-raise, never a recorded number.
  3. Sign-flip permutation — for the recorded case `n_valid = 20 ≤ PERM_EXACT_MAX_N = 20` (thresholds.py:85), the code takes the **exact enumeration** of all `2^20` flips (validate.py:41-45); the random branch `default_rng(0)` (validate.py:47) is never reached. So `p_perm` is not merely seeded, it is deterministic *and exact*.
  4. LOO false-positive (`loo_fp_fraction`, validate.py:53-66), `two_means_split`, `improvement`, `estimate_O_volume`, `np.percentile/var/median`: no rng.
  5. τ(n) gate — precomputed fixture `fixtures/tau_table.json` (MC seed 20260621, gate.py:26-40), loaded not regenerated; data-independent.
  Bit-for-bit here means: same frozen inputs ⟹ identical `results/validation.json` bytes. What could break it: the observable is an **integer** column-sum `past_matrix.sum(axis=0)` (estimator.py:128) with boolean comparisons — no BLAS/matmul in the path — so the verdict is robust; the only ULP-sensitive ops are `np.log`/`sqrt` inside the BH relation (generator.py:104) and `var`/`percentile`/`std` feeding the *continuous* columns. Guarded by `eps=1e-12` (generator.py:100) and integer O, cross-platform divergence would at most perturb `med|dr|/2M` and `r_std` in the last digit; `p_perm`, `θ_loc`, `θ_stab`, `fp`, `coverage` are exact rationals and platform-invariant. The `python -m nachocausal.validate` entrypoint runs `run()` with **no arguments** (validate.py:225-233, defaults at 155-159): zero free parameters at replay.

- **Order observable (documentary consistency of the transcribed PASS).** The transcribed numbers are internally consistent with the frozen machinery, and several are forced values:
  - `p_perm = 9.54e-07`. With 20 valid seeds and exact enumeration, the minimum attainable p is one configuration in `2^20`: `1/1048576 = 9.5367431640625e-07 → 9.54e-07`. This is exactly `2^-20`. It occurs iff all 20 paired differences `d = sep_BH − sep_MINK > 0` and the all-plus flip is the unique max (validate.py:50, `means >= obs − 1e-12`). The value is the permutation floor — the strongest signal the test can emit and fully consistent with `PERM_EXACT_MAX_N = 20`.
  - `θ_loc(12000) = 0.098`: `θ_loc = K_LOC·ℓ/2M = 2·(12000/7.2)^{-1/2}/0.5 = 0.097980` (thresholds.py:101-108; BOX_AREA=7.2 at :41, TWO_M=0.5 at :42). Matches. All four levels match: `θ_loc = {0.277, 0.196, 0.139, 0.098}` for `{1500,3000,6000,12000}` — reproduced by hand from the frozen formula.
  - `θ_stab = θ_loc/2` exactly (since `θ_stab = K_LOC·ℓ = TWO_M·θ_loc = 0.5·θ_loc`, thresholds.py:111-113): `{0.139, 0.098, 0.069, 0.049}` = half of the θ_loc row. Table matches at every level.

- **Relevant invariants (available cross-checks; an impossible value would refute the transcription documentarily — Option C's power).**
  - Discrete-denominator columns, all `k/20` (n_valid=20): `fp ∈ {0.00, 0.05, 0.10}` = `{0,1,2}/20` (validate.py:146, `flags/n`); `coverage ∈ {0.85, 0.95}` = `{17,19}/20` (validate.py:142); abstain fractions `{0.90, 0.95, 1.00}` = `{18,19,20}/20` (validate.py:124-125). Every transcribed value is a legal multiple of `1/20`. A value like `fp = 0.07` or `coverage = 0.93` would be *impossible* and would refute the transcription with no run.
  - Convergence slack (validate.py:192, `b ≤ a + a.ell_over_2M`, with `ell_over_2M = θ_loc/2`): `0.137 ≤ 0.172+0.139`, `0.072 ≤ 0.137+0.098`, `0.064 ≤ 0.072+0.069` — all hold; `slack_ok = True` is consistent. Loc check `0.064 ≤ 0.098`, stab `0.008 ≤ 0.049` — consistent.
  - `N̄` Poisson plausibility: `{1518, 3026, 6037, 12052}` vs intensities `{1500,3000,6000,12000}`, each ≈ +2.1σ high (σ = √(λ/20)). The **common sign and magnitude** across all four levels is expected, not anomalous: the four levels reuse the *same 20 seeds* (validate.py:172, one `VALIDATION_SEEDS` list), and `default_rng(seed).poisson(λ)` draws are positively correlated across λ at fixed seed, so the sample-mean offsets move together — a fingerprint of the shared-seed design that a naive fabricator inventing independent N̄'s would not reproduce. [This correlation reasoning is analytic/[UNVERIFIED-by-run]; the first-order plausibility (each N̄ within ~2σ of λ) is verifiable by hand and holds.]
  - Net: every transcribed number is expressible as a value the frozen machinery can actually produce; I found no impossible entry. Full consistency raises confidence but is a *necessary-not-sufficient* condition.

- **Analytic / epistemic reach of each option.**
  - **A (SUPERVISED_REVERIFICATION):** because the map (code@573cfcb, frozen seeds, numpy 1.26.4) → verdict is a deterministic pure function whose output is already published, a replay is *computing a known value, not sampling a new one*. Outcome is binary and falsifiable: bit-for-bit match ⟹ the transcription is the faithful output (integrity restored, `[UNVERIFIED_PRIMARY_MISSING]` → reproduced); any mismatch ⟹ the transcription is **falsified** and must be reported alike. Evidential value: the strongest available guarantee of *reality* of the PASS numbers. Limit: it cannot recreate historical *primacy/blindness* — but see the caveats: blindness is protected by the pre-outcome seal, not by execution scarcity, so A does not damage it.
  - **B (freeze as-is):** the PASS remains backed solely by a human-typed transcription (fee12d5) whose cited raw pointer is *contradicted* on disk and which has no provenance snapshot (auditor 005 ERROR#1 + WARN#2/#3). The strongest published result then carries the weakest evidence chain — the exact configuration the founding rule ("verifiable backing or [UNVERIFIED]") is designed to prevent. It fabricates nothing but *declines available corroboration*.
  - **C (documentary audit only):** maximal reach = confirm internal consistency (the checks above) and detect any impossible value. It can *refute* a bad transcription but cannot *confirm* the numbers are the actual output on the actual seeds; it cannot separate a faithful transcription from a machinery-respecting fabrication. Necessary-condition verification, not sufficiency.

- **Caveats (anchored / marked).**
  - Under A the statistical meaning of the PASS is **unchanged**, because zero researcher degrees of freedom remain: thresholds sealed (SHA `6e2c3888…` matches, chair-verified), seeds fixed and public (thresholds.py:66-70), outcome already known and published. A deterministic replay consumes no fresh randomness (n=20 → exact enumeration, validate.py:41-45; sprinkle reseeded identically) and offers no point of selection. Selection/optional-stopping/garden-of-forking-paths hazard added by A = 0.
  - The binding prohibition names **"fresh seeds"** ("no re-running on fresh seeds after seeing a result", preregistration_002.md:65-67); the proposal uses the *same* frozen seeds/instrument/commit — the distinct hazard the prohibition targets (drawing new randomness and selecting a favorable draw) is *unreachable* by same-seed replay. This is the precise line between **re-run-to-verify** (deterministic replay, adds no dof — permitted by the statistics) and **re-run-to-retry** (fresh seeds, forbidden). RESPECT_SEAL_FREEZE and NO_POST_HOC_TUNING are not engaged by A; NO_THRESHOLD_LOOSENING holds (no threshold touched); NO_GROUND_TRUTH_LEAKAGE holds (no virgin-band seed enters dev, auditor 005 §5).
  - The one property A cannot restore is the historical *"first and only evaluation"* phrasing (preregistration_002_result.md:12) — hence the PI's explicit `SUPERVISED_REVERIFICATION` label and refusal to present it as the original blind run is *statistically necessary and sufficient*: it preserves NO_GROUND_TRUTH_LEAKAGE / honest framing while extracting the full deterministic-integrity gain. Mislabeling it as the primary blind run would be the only way A could over-claim.
  - "A weaker real result beats a strong fabricated one" (CLAUDE.md): A gives the strongest guarantee that the PASS is *real* (bit-for-bit determinism ⟹ match or falsify); C gives partial (consistency only); B gives none while retaining the strongest-looking claim — the precise pattern the rule warns against. On the statistics, A best serves the founding rule, provided it carries its explicit label and any mismatch is reported alike. NO_RECONSTRUCTION_CLAIM is untouched by all three (the bounded finite-patch 1+1D localisation claim, preregistration_002_result.md:52-64, is not enlarged by verifying its backing).

### Mathematical logic brief

- **Formal status.** The binding prohibition (`docs/preregistration_002.md:66-67`) is an *enumerated* set of forbidden operations: `{post-hoc tuning, re-running on FRESH seeds after seeing a result, loosening a frozen threshold}`. A `SUPERVISED_REVERIFICATION` uses the *same* frozen seeds, same seal, same threshold — so it is not a member of that set. **Option A does not violate the LETTER of the "fresh seeds" clause.** The `PURPOSE` of the clause, stated precisely, is to eliminate *selection/optimisation degrees of freedom* — the forking-paths pathology whereby a null outcome is re-drawn (new seeds) or the acceptance region is moved (threshold loosening) until PASS, and only the favourable draw is reported. A deterministic replay with thresholds frozen, seeds fixed, and the outcome already public has **zero residual degrees of freedom**: the input is fixed, `f` is fixed, `output = f(sealed@573cfcb, frozen_seeds)` is a pure function of committed inputs, and there is nothing left to select or suppress. So Option A violates neither letter nor purpose of that clause. The correct formal name for what a replay produces is **not** "evaluation" (a decision under uncertainty with residual DoF) and **not** "measurement" (of a fresh physical quantity), but **verification of transcription fidelity** — a decidable equality test of the proposition `transcription(fee12d5) = f(sealed, frozen_seeds)`, i.e. recomputation of a known deterministic function to confirm a claimed value. (Generator committed + deterministic: auditor 005 §4, lines 90-92.)

- **Quantifier / dependency order.** For the exercise to carry evidential value, the following must be *universally fixed BEFORE* the existential "launch" (∀-predicates, then ∃-run); any predicate chosen after seeing replay output re-injects exactly the forking-paths DoF the seal was meant to kill:
  - **(i) publish-either-way:** `∀ outcome ∈ {MATCH, MISMATCH}` → recorded and reported, mirroring `docs/preregistration_002.md:64` "regardless of which it is." Asymmetric reporting (hide a MISMATCH) is the single most destructive omission.
  - **(ii) comparison predicate `P`:** fix its *domain and equality relation* ex ante — which fields? The verdict line (`PASS`), the six boolean checks (`_result.md:17-24`), and/or the full per-level table (`_result.md:29-34`, including `p_perm`, `med|dr|/2M`, `r_std`). State whether equality is bit-for-bit or field-typed.
  - **(iii) partial-match rule:** pre-commit the tolerance for platform float drift. Either require bit-identity (which then obligates a pinned environment — numpy 1.26.4, `_result.md:11` — as part of `P`), or pre-specify a numeric tolerance on floats with *exact* equality on the verdict booleans. Choosing the tolerance after seeing the drift = a post-hoc DoF that silently manufactures "match."
  - **(iv) author-verifier separation:** the supervisor/verifier must be disjoint from the transcription's author — `docs/preregistration.md:78` "The author of a claim is never its sole verifier." "SUPERVISED" must denote this disjointness, not mere observation.

- **Equivalence claims.** `"REVERIFICATION reproduces the transcription" ⟺ "the original run happened as described"` is **FALSE**. Let `M` = the mathematical proposition `transcription = f(sealed, frozen_seeds)` and `H` = the historical proposition `a blind run occurred on 2026-06-22 as described`. Then `H ⟹ M` but `M ⇏ H`: a MATCH is **necessary but not sufficient** for `H`. A MATCH *establishes* that the transcribed numbers are the true output of the committed deterministic function; it *cannot* establish **when, where, or whether** an original execution occurred, nor its blindness, nor close the provenance/timing gaps (auditor 005 findings 2-3). The epistemic subtlety, however, is decisive: **the bounded scientific claim of prereg-002 is a property of `M`, not of `H`.** The claim is "order alone localises the boundary on the virgin band" — a fact about `f` on frozen inputs — and the anti-tuning guarantee is carried by the **seal** (thresholds sha frozen at `573cfcb` *before* the seeds could be scored, `make verify-seal` MATCHES `_002.md:8`) plus determinism, **not** by the historical blindness of a run. So `M` bears the scientific weight; `H` is epistemically redundant *given seal + determinism*. What a MATCH genuinely cannot restore is the **audit trail** (findings 2-3) and the truth of the *historical* sentence `_result.md:12` "First and only evaluation" — a bookkeeping/provenance fact, not the bounded claim's content. Distinguish sharply: historical fact (unrecoverable, and not the scientific claim) vs mathematical fact (replay-recoverable, and *is* the scientific claim).

- **Type / object discipline.** The labels are of **distinct types** and must never be coerced across type:
  - `[UNVERIFIED_PRIMARY_MISSING]` (`results/README.md:16`) — a *provenance/artifact* type: "no primary raw artifact corroborates the transcription."
  - `SUPERVISED_REVERIFICATION_MATCH` — an *equality-verification* type: "transcription = f(inputs) under `P`."
  - `SUPERVISED_REVERIFICATION_MISMATCH` — falsification of the transcription.
  - `blind PASS` — a *historical-evaluation* type: "first blind evaluation yielded PASS."

  Final status of prereg-002 by branch:
  - **A-MATCH:** `PASS`, backing = {transcription `fee12d5` + REVERIFICATION_MATCH}. The **primary artifact is still lost** — a replay produces a *new* artifact, not the missing one (PI: "no puede recrear la evidencia primaria perdida"). Correct status: **`PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED]`**, *never* unqualified "blind PASS."
  - **A-MISMATCH:** the high-value branch — the transcription is *falsified*; the reported PASS is retracted. Must be published (this is precisely why pre-commitment (i) is mandatory).
  - **B:** `PASS [UNVERIFIED_PRIMARY_MISSING]`, permanently; honest under CLAUDE.md's founding rule only because the `[UNVERIFIED]` tag is carried forever.
  - **C-consistent:** verifies seal + draw-determinism + commit chain, but leaves `M` (the central equality) **unchecked** — `M` is not decidable without executing `f`. Status stays `[UNVERIFIED_PRIMARY_MISSING]` with strengthened circumstantial support; C's information is a strict subset of A's.
  - **C-inconsistent:** a documentary contradiction impeaches the transcription with no run.

  **Label-laundering guard (formal):** epistemic strength here is **two-axis** — a *mathematical-correctness* axis and a *provenance* axis — and they are independent. A REVERIFICATION_MATCH raises the first axis to maximal while the second stays at "primary artifact missing." No single scalar `PASS` may absorb both axes. Enforce operationally: the string "First and only evaluation" (`_result.md:12`) may not co-occur with a post-reverification status without annotation, and the "RE-" prefix must never be shed. The vocabulary `SUPERVISED_REVERIFICATION` **proves exactly what the prose needs iff** the term *evaluation* is held fixed to "outcome-determining draw with residual DoF" and *verification* to "recomputation of a committed function"; the sole failure mode is later **equivocation** on "evaluation," which would type-error a verification into a second evaluation and thereby violate `_002.md:61` "the only evaluation."

- **Caveats.**
  - The type distinction that saves Option A (evaluation ≠ verification) is *linguistic discipline*, not a physical safeguard; it holds only as long as documents refuse to call run #5 an "evaluation." [anchor: `docs/preregistration_002.md:61`, `_result.md:12`]
  - A MATCH does not resolve auditor 005 findings 2 (13m14s timing gap) and 3 (provenance asymmetry); those are historical facts about `H`, orthogonal to `M`. [anchor: `docs/auditor/auditor_report_005…:134-135`]
  - Bit-for-bit reproducibility is claimed "in principle" but not demonstrated; without a pinned environment inside predicate `P`, a benign float-drift MISMATCH is possible and would be mis-typed as a falsification absent rule (iii). [anchor: auditor 005:91 "in principle"; `_result.md:11` numpy pin]
  - The seal, not any run, is what guarantees no-threshold-tuning; this is verified live. [anchor: `make verify-seal` = `docs/preregistration_002.md:8`, auditor 005:38-42]
  - Author-verifier separation (`preregistration.md:78`) is a precondition of the word "SUPERVISED" having content; if the supervisor is not disjoint from the author, Option A degrades to Option B with extra steps. [anchor: `docs/preregistration.md:78`]
  - I express no vote on A/B/C; this brief is confined to definitional precision of the options and labels, per role. [UNVERIFIED — scope statement, not a factual claim]

### Physicist brief

- **Coordinates & patch:** The prereg-002 PASS is a strictly bounded, order-only claim: the causal order alone (no coordinates visible to the estimator) localises the horizon-associated `r=2M` cut, *significantly and stably*, in a **finite 1+1D Eddington–Finkelstein Schwarzschild patch** at `t_edge=6`, with the bracket contracting toward the discreteness floor as density grows and the box-matched flat control showing no such separation (`docs/preregistration_002_result.md:52-64`; README status `README.md:24-45`). It is a **recoverability** result, explicitly NOT metric reconstruction, NOT the global event horizon at future null infinity, NOT 3+1D/Kerr/manifoldlikeness (`_result.md:60-64`, guarded by NO_RECONSTRUCTION_CLAIM). Its evidentiary status matters because this single PASS is the *only* blind, sealed, field-facing empirical result in the project — everything downstream (PR-003, R-VAR V.2) is scaffolding erected on it, so the difference between "PASS, auditable" and "PASS, non-auditable transcription" propagates to every claim built above it.

- **Physical meaning of the signal:** The *underlying physics is not in doubt*; only the *provenance of one artifact* is. The mechanism — interior future light-cones tilt monotonically toward decreasing `r`, truncating interior futures against the singularity while exterior futures run to `t*=6`, producing a future-volume/longest-chain **bimodality** that sharpens with timelike extent — is independently grounded in Dou–Sorkin and EGS and re-derived in committee (`docs/comite/comite_decision_015_...md:153`, and the confirmed continuum root `Θ_out>0` outside / `<0` inside / `=0` at `r=2M`, `md:157`; longest-chain bounded-inside/extensive-outside confirmed exact at `md:248`). Dev-side corroboration at EXPLORE scale exists: the estimator-v2 decision spec shows localisation and coverage passing at `t_edge=6` across a density sweep `I=1500…24000` and a patch sweep (`docs/estimator_v2_decision_spec.md:33-35, 63`). **Its limits are decisive, however:** that evidence used `EXPLORE_POOL` seeds only (`estimator_v2_decision_spec.md:8`), was *not blind*, was the basis on which the instrument was tuned, and therefore cannot substitute for the held-out virgin-band verdict — it establishes that the physics is real and reproducible, not that the frozen blind test was passed. So what is at risk is narrow but real: the *specific frozen, blind, one-shot confirmation* on virgin seeds `2076703…2983811`, whose raw artifact is now definitively lost (`results/README.md` prereg002 entry, `[UNVERIFIED_PRIMARY_MISSING]`).

- **Sprinkling domain (dependency chain):** Committed documents that assert or lean on the PASS as foundation —
  - `README.md:24` top-line project status: "pre-registration 002 PASSED — order-only horizon localisation … is demonstrated"; `README.md:37, 49` ("With localisation PASSed, the next goal…").
  - Roadmaps, all under "Punto de partida (verificado)": `docs/hoja_de_ruta_23_jun_2026.md:14`, `docs/hoja_de_ruta_24_jun_2026.md:12`, `docs/hoja_de_ruta_25_jun_2026.md:12` — each states prereg-002 `PASS` as the *verified* starting point.
  - PR-003 program: the leakage-gate architecture and every candidate observable are defined as successors to the PASS (`README.md:49, 95`; `docs/pr003_leakage_gate.md`; `docs/preregistration_003_draft.md`).
  - R-VAR V.2 statistical-necessity framing explicitly cites the PASS truncation signal / bimodality as the thing its selector must not be circular with (`comite_decision_015_...md:113, 133, 181` — "the same future-truncation asymmetry the prereg-002 PASS measured"; V.2 "leans on" the PASS, `md:181`).
  - Note a precise correction to the DOSSIER framing: estimator-v2's *frozen thresholds* are **upstream** of the PASS (frozen before the blind seeds were drawn, `preregistration_002.md:35-41`), so they do not *depend* on it; the genuine downstream dependents are the roadmaps, PR-003, and R-VAR V.2.
  Under **option B** (PASS reportado, no auditable), every one of these lines currently reading "verificado / demonstrated" would have to be re-qualified to "PASS reported, primary artifact lost, non-auditable" — the word *verificado* in the three roadmaps and *demonstrated* in `README.md:24` become over-claims the moment the primary evidence is conceded gone. Under **A-match** (supervised reverification reproduces PASS bit-for-bit, as the deterministic generator predicts, `auditor_005:90-96`) the chain is restored to auditable footing, with the honesty cost that the confirming evidence is labelled a reverification, not the original blind run. Under **A-mismatch** the entire chain falsifies at the root and PR-003 / R-VAR V.2 must halt and be re-examined — which is exactly the outcome a genuine guardrail must be able to produce.

- **Claim boundary (suggested field-facing wording, NO_RECONSTRUCTION_CLAIM throughout):**
  - **Under B:** *"prereg-002 verdict: PASS (order-only localisation of the r=2M cut in a finite 1+1D EF patch, t_edge=6). Backing: committed transcription only (`docs/preregistration_002_result.md`, `fee12d5`); the primary raw artifact is definitively lost and no primary evidence corroborates the transcription (`[UNVERIFIED_PRIMARY_MISSING]`, auditor 005). Not independently auditable. Does not claim metric reconstruction, the global event horizon, or any 3+1D result."* The roadmaps' "verificado" must be softened to "reportado, no auditable."
  - **Under A-match:** *"prereg-002 verdict: PASS, reproduced by supervised reverification (SUPERVISED_REVERIFICATION, same sealed instrument `6e2c3888…`, commit `573cfcb`, same frozen seeds, same virgin band; not the original blind run — the primary artifact was lost). Order-only localisation of the r=2M cut in a finite 1+1D EF patch. Does not claim metric reconstruction, the global event horizon (future null infinity), 3+1D, Kerr, or manifoldlikeness."* The label must never present the reverification as the first blind evaluation.

- **Caveats:**
  - The physics signal is independently attested and not contingent on this artifact (EGS/Dou–Sorkin, `comite_decision_015_...md:153,157,248`); losing the artifact does not put the *phenomenon* in doubt, only the *frozen blind confirmation*. [anchored]
  - **Regular-black-hole non-generality:** the future-truncation mechanism is Schwarzschild-specific — for Hayward-type regular BHs the longest-chain/future-volume partition "is likely to fail" (`comite_decision_015_...md:157, 168`, EGS md:249). The PASS certifies a Schwarzschild-EF patch only; this caveat is independent of the artifact question but must survive into any reworded status line. [anchored]
  - **Scientific cost of option B (the load-bearing point):** nachocausal's founding premise is that guardrails must be *able to fail* (auditor is "the standing guardrail against AI-faked results"; the reporting rule commits to recording PASS/FAIL/INCONCLUSIVE alike, `preregistration_002.md:64-67`). A central empirical result that is *reported but permanently non-auditable* is precisely the failure mode the whole apparatus exists to exclude: it asks the field to trust a number no primary artifact backs, on a project whose credibility rests on every number being the literal output of a committed script. B freezes that contradiction into the record permanently; the deterministic generator makes reverification cheap and, if it matches, harmless to the freeze (same seeds, not FRESH). [anchored: `results/README.md`; `auditor_005:151-161`]
  - **Freeze tension to flag, not resolve (physicist is not the warden):** the binding rule bans "re-running on FRESH seeds after seeing a result" (`preregistration_002.md:65-66`); option A uses the SAME frozen seeds, so it is not the banned move — but it does touch the "first and only evaluation of the held-out band" clause (`_result.md:12`), which is why the honest SUPERVISED_REVERIFICATION label is load-bearing and why this is a committee, not a unilateral, call (auditor 005 recommends exactly this adjudication, `auditor_005:161`). NO_THRESHOLD_LOOSENING and RESPECT_SEAL_FREEZE hold under A only if nothing but the label changes. [anchored]
  - `[UNVERIFIED]` procedural: there is no committed `comite_decision_016` yet (`ls docs/comite/` stops at 015), though `results/README.md` forward-references "comité 016" — this deliberation is that record; treat the reference as pending, not existing.

## 5. Falsifier attack

- **Concrete failure modes:**
  1. **The letter of the freeze forbids A, and wave-1 quoted around it.** The binding one-way rule is not only the fresh-seeds sentence (`docs/preregistration_002.md:64-67`); it is `docs/preregistration_002.md:61-63`: "the single blind `validate.run()` **on these seeds** is the **only evaluation** … It is **launched once**." A second launch on these seeds is literally a second evaluation and a second launch. The logician's brief cites only the enumerated prohibitions at :64-67 and renames the act "verification, not evaluation" — a relabelling manoeuvre of exactly the kind the founding rules exist to distrust. The committee may still authorise A on the purpose test (zero residual selection DoF), but only by *explicitly acknowledging it is construing against the plain letter*; authorising A while claiming "the letter is silent" sets the precedent that any freeze can be escaped by an enumerated-prohibitions-only reading. NO_THRESHOLD_LOOSENING applies to rules, not just numbers.
  2. **The RE plan is internally contradictory and, as written, destroys evidence.** "Single invocation `python -m nachocausal.validate`, unmodified, no wrapper" hard-writes `results/validation.json` (`nachocausal/validate.py:225-233`, `_write` at :217-222, label fixed to `"validation"`). That path currently holds the prereg-001 FAIL raw artifact — per auditor 005 §4 the **only surviving raw artifact that corroborates any published verdict** ("the on-disk artifacts fully corroborate the published FAIL", `docs/auditor/auditor_report_005…md:99-101`). An unmodified launch overwrites it: destroying the last corroborated artifact on the very machine already flagged for artifact loss. You cannot have both "unmodified invocation" and "artefacts to `results/prereg002_reverification/`" without a wrapper, a `run(label=…)` deviation, or post-run file moves — each a deviation from "same instrument, same invocation" that must be chosen and recorded BEFORE launch, plus SHA256+archival of the prereg-001 files first. If this is improvised mid-run, the reverification is procedurally contaminated at birth. [Chair note: the prereg-001 artifacts were archived to `results/prereg001/` on 2026-07-03 (results/README.md), so the overwrite target is now an empty path — but the pre-launch SHA256 of the archived files and the pre-declared output-routing rule remain mandatory.]
  3. **The comparison target no longer exists at full precision.** The raw `validation.json` of the PASS is lost; the only comparand is the *rounded* transcription (`docs/preregistration_002_result.md:29-34`: "0.064", "9.54e-07", k/20 grids). So "bit-identity" (RE) is unachievable by construction against the record; the predicate can only be "rerun output, printed at the record's own precision, equals the record." Fields with ~2 significant digits give a weak per-field test; the power against fabrication comes only from the joint ~60-field match plus determinism. State this honestly: A-match is "matches the rounded transcription," not "bit-identical to the original run."
  4. **The predicate's outcome space is incomplete.** Wave-1 pre-committed MATCH/MISMATCH but not the cells: MISMATCH-with-rerun-PASS, MISMATCH-with-rerun-FAIL, INCONCLUSIVE, crash, abort. The killer cell is **mismatch-but-PASS**: the temptation to report "minor transcription typos, PASS confirmed" converts the reverification into a *second first-run* — the exact retry the freeze forbids. Pre-commit now: ANY mismatch on any pre-listed field retracts fee12d5's record as transcription; the rerun's own verdict then gets whatever label the committee fixes *today*, not after seeing which cell obtains.
  5. **Wall-time will be spun.** RE predicts ~30-35 min here, but prereg-002 scores ~160 calls vs prereg-001's 80 (auditor 005 WARN 2), so ~60+ min is plausible. Whatever the rerun's duration, it will be read as evidence for or against the 13m14s anomaly in whichever direction flatters. Pre-commit the interpretation rule (e.g., "rerun duration is recorded but adjudicates nothing about the original host") before the number exists.
  6. **B has an honest case wave-1 undersold; and the tempting escape from B is itself forbidden.** B is the only option that takes `:61-63` at face value. Its real cost is the physicist's softening of README/hojas — bearable. The seductive alternative "just run a fresh blind prereg-002b on a new virgin band (≥3,000,000)" is **barred**: it is precisely "re-running on fresh seeds after seeing a result" (`preregistration_002.md:64-67`). Record this closure now, or it will be proposed in six months as the "clean" fix.
  7. **C is audit theater.** The mathematician's consistency checks (θ formulas, k/20 legality, p-floor 2^-20) cannot distinguish a faithful transcription from a *competent fabrication* — an AI assistant is exactly the class of agent that produces internally consistent k/20 tables with correct p-floors. C adds ≈0 bits over auditor 005 + wave-1; choosing C is choosing B while appearing to act.
  8. Dossier hygiene: "no virgin-band seed in any file on this machine" is false as stated — the 20 seeds are in `nachocausal/thresholds.py:66-70` and `docs/preregistration_002.md:25-27`; auditor 005 said no seed *outside thresholds/docs/spec artifacts* (report :69-73). The chair's summary must not propagate the over-compressed version. [Chair: corrected in §2.]

- **Ground-truth leakage:** The rerun itself opens no new estimator-side path — the embedding scores exactly as sealed (`validate.py:22` imports `scoring.blind_bracket`; unchanged 573cfcb..HEAD, only `c1_selector.py`/`selection_guard.py` added, neither imported by `validate.py:21-22`). The NEW vector is downstream: RE recommends committing provenance **plus a per-seed log** to a TRACKED location. Per-seed ground-truth distances (|dr|, covers, sep) for the held-out band, sitting tracked in the repo, become tuning-visible to all future dev — including R-VAR v2, which is paused *waiting on this very decision* and whose authors will read these artifacts. That is the hidden embedding beginning to *guide* future observable design at per-seed granularity on the confirmatory band. Pre-commit: track checksums + level-aggregate fields only (the FAIL-run schema), quarantine per-seed ground-truth scores, and declare the 2M-band permanently burned for any future protocol comparison. NO_GROUND_TRUTH_LEAKAGE is currently satisfied; the RE's tracking recommendation, taken naively, breaks it.

- **Freeze violations:** (a) The second launch vs `:61-63` letter (mode 1) — must be owned, not construed away. (b) The comparison predicate and float-tolerance are researcher DoF being **fixed after the target values are public**; any tolerance beyond "record's own printed precision, round-half-even; booleans/checks/k-of-20 fields exact" is a knob that can absorb a real mismatch (laundering) — including the pre-built escape hatch "must be the other machine's float drift" (cross-machine bit-identity is [UNVERIFIED] per RE). Pre-commit: this machine's rerun is *definitive* for the M-claim; machine-drift excuses inadmissible. (c) The mismatch-but-PASS cell is a smuggled retry unless closed now (mode 4). (d) Output-path improvisation mid-run (mode 2) is an unfrozen protocol change made after launch.

- **Verdict coercion:** The reporting costs are grossly asymmetric: MATCH → a headline ("PASS reverified") the PI wants; MISMATCH → retraction of the flagship result *plus* an implicit fabrication finding against commit fee12d5, authored by the same person who must report it, supervised by the same AI lineage that wrote the transcription. Publish-either-way is empty without a **pre-launch committed launch declaration** (commit "reverification launched at T, predicate P, publish regardless" BEFORE pressing enter); determinism removes retry gains but not abort-and-stay-silent. Label-laundering paths, none mechanically guarded: the RE- prefix has no grep gate in `audit.sh`/`check_*` scripts; `docs/preregistration_002_result.md:12` "First and only evaluation of the held-out band" becomes literally false at launch and must be annotated in the same commit as the launch declaration, not after; `README.md` "demonstrated" lines will be restored on A-match without the bracket unless a mechanical string-pattern check is added to the auditor.

- **Premature / over-broad claims:** The central over-claim risk is **A-match read as restoring blindness**. It cannot. Replay verifies M (transcription = output of the sealed f on frozen inputs). The live doubt from auditor 005 is H: *when* the run happened relative to the seal and whether inputs (notably `VALIDATION_DRAW_SEED=20260622`) were outcome-shopped off-git on the unavailable machine. Replay is constitutionally blind to H: a draw-seed-shopped PASS replays as a perfect MATCH. The logician's "H is bookkeeping" proves too much — by that logic the one-way launch rule (`:61-63`) and the independent-falsification gate (`preregistration.md:74-78`) were never needed for any deterministic pipeline; but those rules protect *input provenance* (seed draw, freeze ordering), which determinism does not. The plausibility argument against shopping (p_perm at the exact 2^-20 floor at all four levels is very hard for a lucky null draw; ~14h window between abe6c56 2026-06-21 22:38 and seal allows few full-pipeline trials) is probabilistic comfort, not verification — report it as such. Honest A-match label therefore needs BOTH tags: `TRANSCRIPTION_REVERIFIED` (M, verified) and `BLINDNESS_DOCUMENTARY_ONLY` (H, resting solely on the git timeline). Claim boundary otherwise intact (finite-patch 1+1D wording at `preregistration_002_result.md:52-64` is correct; keep it verbatim).

- **Independent-falsification gate:** Not strictly achievable. `preregistration.md:78`: "The author of a claim is never its sole verifier." Here the operator, the machine, the AI assistant, and the transcription's author coincide; every possible verifier already knows the target numbers, so "blind to the proposed verdict" (`preregistration.md:76-77`) is unattainable in principle. "SUPERVISED" must not be allowed to connote a second person who does not exist. The strongest available substitute: (i) mechanical predicate committed before launch, (ii) raw artifacts + SHA256SUMS + full provenance snapshot committed immediately after, making *future third-party* falsification possible — which is precisely what B forecloses forever. Who supervises the supervisor: nobody today; the design goal must be that nobody *needs* to, because every byte needed to re-supervise is committed.

- **Minimal falsification test:** Executed this session (read-only): `git log --all -S "VALIDATION_DRAW_SEED" -- nachocausal/thresholds.py` and `git log --all --oneline -S "2076703"` → **single introduction at 573cfcb** ("Seal prereg-002 … draw blind held-out seeds + freeze"); no alternate draw-seed value exists anywhere in git history, on any branch; the reserved-band hygiene predates it (abe6c56, 2026-06-21 22:38). This falsifies *in-git* seed shopping — and, by its own limits, demonstrates the residue: **off-git shopping on the unavailable machine is untestable by any replay or documentary act**, which is exactly why an A-match may never be labelled as restoring blindness. One further pre-launch check is mandatory if A passes: `sha256sum` of the archived prereg-001 files (`results/prereg001/*`) committed BEFORE launch, so the FAIL evidence survives the rerun no matter what the invocation does.

## 6. Pre-registration verdict

- Verdict: PASS (attaches to **A only**, and only as conditioned below; **B** and **C** are not what is being authorised, though C remains the fallback if any precondition below fails; **B** is BLOCKed as a permanent posture — it is not required by the rules, only by omission).

- Freeze status: A does not touch any frozen threshold, form, or instrument. It re-invokes the identical sealed contract: geometry/ensemble/thresholds inherited verbatim from `docs/preregistration_001_addendum.md`, estimator-v2 changes sealed at `docs/estimator_v2_freeze.md`/`docs/estimator_v2_seal.md`, and the prereg-002 seal at `docs/preregistration_002.md:8-11`. Nothing frozen is being decided post-hoc — the θ values, τ(n) table, and PASS predicate are all pre-existing and untouched. What IS unfrozen and must be written and committed **before launch**, as a condition of this PASS, is the reverification-specific machinery that prereg-002 never anticipated needing a second time: (1) publish-either-way commitment for THIS run, (2) an exact comparison predicate P defining MATCH (field-by-field equality against `docs/preregistration_002_result.md`'s transcribed table, `results/README.md`'s cited values), (3) a partial-match/float-drift rule (what tolerance, if any, on the `9.54e-07`-type floats, fixed *before* the replay is run, not after), (4) author-verifier separation per the independent-falsification gate (`docs/preregistration.md:74-78`: "the author of a claim is never its sole verifier") — i.e., whoever launches/reads `results/prereg002_reverification/` cannot be the same party who authored the original transcription unverified. These four are conditions precedent, not optional.

- Seal integrity: Confirmed directly — `sha256sum nachocausal/thresholds.py` at HEAD (`abf90f0`) and `git cat-file -p 573cfcb:nachocausal/thresholds.py | sha256sum` both equal `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching `docs/preregistration_002.md:8-11`. `git diff --stat 573cfcb..HEAD -- nachocausal/` shows only two **new, additive** files (`c1_selector.py`, `nachocausal/selection_guard.py`, commits `063e64e`/`c287f61`) with zero lines changed in any file the sealed path touches (`thresholds.py`, `validate.py`, `scorer.py`, `tau_table.json` etc. all untouched). So checking out `573cfcb` (or running at current HEAD, since the sealed subset is byte-identical) executes the literal sealed instrument. This matches wave-1 repro engineer's claim; independently re-verified here, not merely trusted.

- Seed discipline: Same frozen `VALIDATION_SEEDS` from the virgin band, same `VALIDATION_DRAW_SEED=20260622` draw — no new seeds, no fresh band, no relaxation. The binding rule at `docs/preregistration_002.md` ("no post-hoc tuning, no re-running on fresh seeds after seeing a result, no loosening a frozen threshold") names **fresh seeds** specifically — a deterministic replay on the *same* 20 seeds through the *same* pure function (`validate.run`, confirmed deterministic by wave-1 mathematician) has no researcher degree of freedom to exploit: a pure function of fixed input has exactly one possible output, so there is no "try again until it looks better" available via same-seed replay, which is precisely the abuse the fresh-seed ban forecloses. It therefore falls outside the letter of what that clause prohibits — but it is inside the *spirit* of "first and only evaluation" (`docs/preregistration_002_result.md:12`), which is why it cannot be presented as a second instance of that phrase. Formally, what changed is not the evaluation (there remains exactly one *evaluation event*, now unrecoverable) but who has *audited* it: the committee, not an individual, is now the party making this determination, which is itself consistent with the falsification-gate's requirement that the author never be sole verifier (`preregistration.md:78`) — the reverification IS that independent check, deferred rather than skipped.

- Reporting rule: MATCH and MISMATCH must be reported alike, exactly as PASS/FAIL/INCONCLUSIVE/OUT_OF_DOMAIN were required to be reported alike originally (`docs/preregistration_002.md`, binding rules section). The reverification record must live in a **tracked** path, not `results/` (git-ignored per `results/README.md` header, ".gitignore:21" — that is structurally why the original raw artifact could vanish without trace). Wave-1 repro engineer's recommendation to commit provenance + checksums to a tracked location (e.g. `results/prereg002_reverification/` promoted out of gitignore, or equivalently a new `docs/` transcription with checksums) is adopted as binding: without a tracked, git-visible artifact this time, the entire exercise reproduces the original failure mode and gains nothing auditable. Label discipline per wave-1 logician: any MATCH outcome is reported as `PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED]` — never bare "PASS," never "confirmed by re-running the blind evaluation." The RE- prefix is permanent and non-optional in all future references.

- Forbidden moves present? None of the enumerated forbidden moves is triggered by A-as-conditioned: no post-hoc tuning (thresholds untouched, confirmed above), no threshold loosening (same θ values), no ground-truth leakage (boundary is still derived order-only, blind, before r is revealed — same procedure as original), no reconstruction over-claim (scope of the claim is unchanged; if anything the label narrows it further to transcription-fidelity). On "re-run after peeking": adjudicated above — a same-seed deterministic replay is not the mechanism the rule bans (which is *drawing new seeds* to escape an unwanted outcome); it is closer in kind to re-running a hash check than to re-running an experiment. It is licit **only** conditional on the four pre-commitments being written and committed first, and only under the RE- label — an unconditioned, unlabelled relaunch presented as "the validation" would cross into exactly the forbidden territory (silently manufacturing a second "first and only" evaluation), which is why B is the correct default *absent* those preconditions and why C alone (documentary audit, no relaunch) is the ceiling if the four pre-commitments cannot in fact be written down cleanly (e.g., if predicate P proves undefinable given float non-determinism concerns already flagged by the mathematician as non-issue, `p_perm` floor is exact rational `2^-20`, so P is well-posed).

- Reasons:
  - Seal SHA independently re-confirmed at both `573cfcb` and HEAD `abf90f0`; sealed files unchanged (`git diff --stat 573cfcb..HEAD -- nachocausal/`) — A runs the literal sealed instrument, satisfying `docs/preregistration_002.md:8-11`.
  - Fresh-seeds ban (`docs/preregistration_002.md`, binding rules) targets drawing *new* seeds post-outcome; same-seed deterministic replay of a pure function (`nachocausal/validate.run`) cannot be gamed and is a different act in kind — permits A without violating that clause's purpose.
  - Independent-falsification / author-never-sole-verifier gate (`docs/preregistration.md:74-78`) is *satisfied*, not violated, by committee-authorised, separation-enforced reverification — this is the mechanism the founding document anticipated for exactly this kind of doubt.
  - `results/README.md`'s own text already flags "whether to authorise one is a `/comite` matter" — the document that recorded the loss explicitly deferred this decision to this body, which supports procedural readiness to rule now, not a bar to ruling.
  - The reporting-alike rule (`docs/preregistration_002.md`, "outcome ... recorded and reported regardless") extends without modification to MATCH/MISMATCH — its enforceability depends entirely on the artifact this time landing in a tracked path (unlike the original, lost in a gitignored one) — hence tracked-path commitment is a hard precondition of the PASS, not a nicety.
  - Label discipline (wave-1 logician) — `PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED]`, RE- prefix permanent — is adopted as binding text for any MATCH outcome; a MISMATCH outcome must be defined and pre-committed (predicate P + drift rule) with equal reporting force before launch, per the same alike-reporting rule.
  - Conclusion: PASS for **A**, conditional on the four pre-commitments (publish-either-way; exact predicate P; float-drift/partial-match rule; author-verifier separation) being drafted and **committed to a tracked path before the replay is launched**, and on the reverification artifact + checksums themselves landing in a tracked (non-gitignored) path. **B** is not adopted (nothing in the freeze compels leaving the PASS permanently non-auditable when a compliant, zero-degrees-of-freedom verification path exists). **C** is the fallback verdict only if any of the four preconditions cannot in fact be met in writing before launch — in that case, downgrade automatically to C-only (documentary audit, no relaunch) rather than proceeding under a defective A.

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| `git diff 573cfcb..HEAD --stat -- nachocausal/` → only c1_selector.py (+80) and selection_guard.py (+84) added, 164 insertions, 0 deletions, no sealed-path file touched | Repro engineer | CONFIRMED |
| validate.py:21 `from . import estimator, gate, generator, thresholds` + `from .scoring import blind_bracket`; `python -m nachocausal.validate` → `run()` defaults `seeds=None→VALIDATION_SEEDS`, `label="validation"`, `write=True` | Repro engineer | CONFIRMED (minor: run() defaults live at validate.py:155-170; the `__main__` call is at ~224-232 — substance exact, line anchor approximate) |
| thresholds.py:85 `PERM_EXACT_MAX_N = 20`; exact-enumeration branch in validate.py; `9.5367431640625e-07 == 2**-20 == 1/1048576` | Mathematician | CONFIRMED |
| theta_loc = K_LOC·ell/TWO_M, ell = (intensity/BOX_AREA)^-0.5, K_LOC=2, BOX_AREA=7.2, TWO_M=0.5; `2*sqrt(7.2/12000)/0.5 = 0.09797958971132713 ≈ 0.098`; theta_stab = theta_loc·TWO_M ≈ 0.049 | Mathematician | CONFIRMED |
| gate.py loads `nachocausal/fixtures/tau_table.json` (no live MC in validation path); fixture exists | Mathematician | CONFIRMED |
| docs/preregistration_002_result.md:29-34 transcribed columns are legal k/20 multiples: fp∈{0.00,0.05,0.10}, coverage∈{0.85,0.95}, abstain∈{0.90,0.95,1.00} | Mathematician | CONFIRMED |
| docs/preregistration.md:78 "The author of a claim is never its sole verifier." | Logician | CONFIRMED (sentence spans lines 77-78) |
| README.md:24-25 "pre-registration 002 PASSED — order-only horizon *localisation* in a finite 1+1D patch is demonstrated under a fully frozen protocol."; hoja_de_ruta_23:14, 24:12, 25:12 each open with "prereg-002 `PASS`" as verified starting point | Physicist | CONFIRMED |
| docs/estimator_v2_decision_spec.md:33-35 density/patch sweep rows; :63 "Against the frozen `coverage ≥ 0.5`, the density sweep passes everywhere (min 0.78)"; :8 "all evidence cited used **EXPLORE_POOL** only" | Physicist | CONFIRMED with a nuance (see Notes) |
| results/prereg001/validation.json exists (seeds 11…65537, verdict FAIL); results/README.md states "PRIMARY_PASS_ARTIFACT = UNAVAILABLE (definitive…)" + "[UNVERIFIED_PRIMARY_MISSING]"; results/prereg002/ exists and is empty | Chair/auditor | CONFIRMED |
| preregistration_002_result.md:12 "First and only evaluation of the held-out band." (verbatim); preregistration_002.md ~:63-67 reporting rule naming FRESH seeds (verbatim, region confirmed) | Various | CONFIRMED |
| thresholds.py VALIDATION_SEEDS: 20-seed tuple, first 2076703, last 2983811; three asserts (length, DEV disjointness, band membership) immediately follow | Repro engineer/Mathematician | CONFIRMED |

- Notes:
  1. validate.py line anchors in the repro brief are off by ~60 lines for run()'s defaults (actual :155-170); substance exact.
  2. estimator_v2_decision_spec claim 9 merges two table rows (density sweep row does not itself state t_edge=6; the patch-sweep row does). Both underlying facts individually CONFIRMED; the composite phrasing slightly overstates citation precision.
  3. results/prereg002/ verified as existing but empty — consistent with the chair's framing.
  4. Several line anchors (thresholds.py:85, :101-113; preregistration_002.md:64-67) land within a few lines of the actual text; content matches in all cases.

## 8. Synthesis

**Unanimity on the core facts.** All seven roles agree: the sealed path is byte-identical between
`573cfcb` and HEAD (triple-verified); `validate.run()` is a deterministic pure function with all
randomness seeded and the permutation test exact at n=20; every transcribed PASS number is
documentarily consistent with the frozen machinery (θ formulas reproduced by hand, all discrete
columns legal k/20 multiples, p_perm exactly the 2^-20 floor) and no impossible value exists; the
in-git seed-shopping hypothesis is falsified (single introduction of `VALIDATION_DRAW_SEED` at
the seal commit, no alternate value anywhere in history).

**The recommendation: OPTION A, under binding written preconditions.** Four roles argue A
affirmatively (mathematician: zero residual degrees of freedom, strongest available guarantee of
reality; logician: violates neither letter nor purpose of the fresh-seeds clause, and the
scientific claim is the mathematical proposition M which replay can verify; physicist: option B
freezes a "reported but permanently non-auditable" flagship result into the record — the exact
failure mode the project exists to exclude; warden: PASS attached to A with four conditions
precedent). The falsifier does not produce an unresolved falsification of A; his attacks convert
into binding conditions (below), and his own executed test (in-git seed-shopping falsified)
strengthens the documentary case. C is rejected as primary ("audit theater": adds ≈0 bits over
auditor 005 + the wave-1 documentary checks, cannot distinguish faithful transcription from
competent fabrication) but retained as automatic fallback if any precondition fails. B is
rejected as a permanent posture but its honest core is preserved: the fresh-band "prereg-002b"
escape is **explicitly barred forever** (it IS the forbidden fresh-seeds re-run).

**Open disagreements (surfaced, none hidden):**
1. **Letter vs purpose of `preregistration_002.md:61-63`.** The falsifier holds that "launched
   once … the only evaluation" plainly forbids a second launch and that the committee must OWN
   construing against the letter rather than claim the letter is silent; the logician and warden
   hold the act is a verification, not an evaluation, so the letter is not engaged. The
   committee adopts the falsifier's framing as the honest one: **this decision explicitly
   construes the purpose over the letter of :61-63, acknowledges that, and records it** — it
   does not pretend the letter is silent. This is a one-time, committee-level construction,
   not a precedent for enumerated-prohibitions-only readings of freezes.
2. **What A-match restores.** Logician: the scientific claim is M; H (historical blindness) is
   epistemically redundant given seal + determinism. Falsifier: that proves too much — the
   one-way rule protects *input provenance* (off-git draw-shopping on the lost machine), which
   replay cannot test; a shopped PASS replays as a perfect MATCH. Resolution adopted: the
   A-match label carries BOTH tags — `TRANSCRIPTION_REVERIFIED` (M, verified) and
   `BLINDNESS_DOCUMENTARY_ONLY` (H, resting solely on the git timeline plus the 2^-20-floor
   implausibility argument, reported as probabilistic comfort, not verification).
3. **Author-verifier separation.** Warden requires it as precondition (4); falsifier shows it is
   not strictly achievable (operator, machine, AI lineage, and transcription author coincide;
   every verifier knows the target). Resolution adopted: the substitute is mechanical — the
   comparison predicate is committed before launch and executed by script, not judgment; all
   raw artifacts + checksums + provenance are committed so that *future third-party*
   falsification is possible (which B forecloses forever). The word SUPERVISED denotes this
   mechanical-predicate-plus-committed-evidence regime, not a second person.
4. **Per-seed logs.** Repro engineer wants a per-seed log for self-corroboration; falsifier
   flags tracked per-seed ground-truth scores as a leakage vector into future dev (including
   R-VAR). Resolution adopted: per-seed log IS captured but stays in git-ignored `results/`
   with its SHA256 committed; the tracked record carries checksums + level-aggregate fields
   only (the FAIL-run schema). The 2M band is declared permanently burned for any future
   protocol comparison.

**Why not RECOMMEND_PROCEED_WITH_CAVEATS or REVISE:** the warden's §6 verdict is PASS (for A as
conditioned), no falsification is unresolved (every falsifier attack is closed by a
pre-commitment adopted in §9), and the step is precisely scoped: one deterministic replay under
a pre-committed, committed-before-launch declaration. The launch itself remains a committing
step requiring explicit user (PI) authorisation.

## 9. Next-step spec

**Reversible steps (may be done now if the user asks; no launch, no seeds consumed):**

1. **Draft the launch declaration** `docs/prereg002_reverification_declaration.md` (tracked),
   containing ALL of the following, and **commit it before any launch**:
   - Purpose sentence: verification of transcription fidelity of `fee12d5`; explicitly NOT the
     first blind evaluation; explicit acknowledgment that the committee construes the purpose
     over the letter of `preregistration_002.md:61-63` (one-time, recorded).
   - **Publish-either-way:** MATCH and MISMATCH (and crash/abort) reported alike, in a tracked
     result note, regardless of outcome.
   - **Comparison predicate P (mechanical, exhaustive, closed outcome space):** the rerun's
     output, printed at the record's own precision (round-half-even), field-by-field against
     `docs/preregistration_002_result.md`: the verdict token, the six boolean checks, and every
     cell of the per-level table. Booleans, verdict, and all k/20-grid fields (fp, coverage,
     abstain, n_valid): exact equality. Float fields (p_perm, med|dr|/2M, θ columns, r_std,
     N̄): equality at the record's printed precision. ANY field mismatch ⟹
     `SUPERVISED_REVERIFICATION_MISMATCH` ⟹ the fee12d5 record is retracted as transcription;
     the rerun's own verdict is then reported under the pre-fixed label
     `REVERIFICATION_RUN_RESULT` (whatever it is) and prereg-002's status becomes
     `RETRACTED_TRANSCRIPTION [REVERIFICATION_RUN_RESULT=<PASS|FAIL>]` — the
     "mismatch-but-PASS" cell can NEVER be reported as "PASS confirmed". No machine-drift
     excuse is admissible: this machine's rerun is definitive for the M-claim.
   - **Wall-time rule:** rerun duration is recorded but adjudicates nothing about the original
     host or the 13m14s anomaly (auditor 005 WARN 2 remains open regardless of outcome).
   - **Label discipline:** outcome labels are exactly `SUPERVISED_REVERIFICATION_MATCH` /
     `_MISMATCH`; on MATCH, prereg-002's status becomes
     `PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]`;
     the RE- prefix is never shed; `docs/preregistration_002_result.md` gets an annotation (in
     the same commit as the declaration) noting that "first and only evaluation" refers to the
     historical 2026-06-22 event whose primary artifact is lost, and pointing here.
   - **Leakage quarantine:** per-seed logs stay in git-ignored `results/prereg002_reverification/`;
     only checksums + level aggregates are committed; the 2M virgin band is declared permanently
     burned for any future protocol comparison; fresh-band "prereg-002b" is recorded as
     forbidden forever (it is the fresh-seeds re-run).
   - **Output routing (pre-declared, no mid-run improvisation):** pre-launch, commit
     `sha256sum results/prereg001/*` (preserving the FAIL evidence); the sealed entrypoint
     writes `results/validation.json` as designed; immediately post-run, the file is COPIED
     (not moved) to `results/prereg002_reverification/validation_SUPERVISED_REVERIFICATION_<date>.json`
     and `results/validation.json` is then removed so no stale pointer survives; run log and
     provenance snapshot (full FAIL-run schema: commit, seal SHA before/after, uname, python,
     pip freeze, UTC start/finish, make test result) captured alongside; SHA256SUMS of
     everything committed to the tracked declaration's companion note.
   - Environment: detached checkout of `573cfcb` (or HEAD — byte-identical sealed subset;
     declaration states which), sealed venv numpy==1.26.4, `make verify-seal` before and after.
2. Optional pre-launch: run `make test` in the sealed venv and record output in the declaration.

**Committing step (ONLY on explicit user authorisation, after step 1 is committed):**

3. **Launch the SUPERVISED_REVERIFICATION**: single foreground/background invocation of the
   unmodified sealed entrypoint per the declaration; ~30-70 min expected. Then execute the
   mechanical predicate script, write the tracked result note (MATCH or MISMATCH, alike), commit
   artifacts' checksums, update `results/README.md` and the status lines (README/hojas de ruta)
   per the outcome-specific wording already fixed in §4-physicist and §9.1. On MISMATCH: halt
   PR-003/R-VAR downstream work and reconvene.

**Falsifier's minimal falsification test:** already executed this session (in-git seed-shopping
search: falsified). The pre-launch mandatory residue — committing `sha256sum results/prereg001/*`
before launch — is folded into step 1 output routing.

**Binding rules pre-committed:** `NO_RECONSTRUCTION_CLAIM` (labels narrow the claim, never widen
it); `NO_POST_HOC_TUNING` / `NO_THRESHOLD_LOOSENING` (no threshold, form, or instrument touched;
predicate P frozen before launch); `NO_GROUND_TRUTH_LEAKAGE` (per-seed quarantine; 2M band
burned); `RESPECT_SEAL_FREEZE` (seal verified before/after; sealed path unmodified); MATCH,
MISMATCH, crash reported alike; `PHYSICAL_IDENTIFIABILITY_STATUS` and all comité 014/015 tokens
unchanged. R-VAR v2 remains paused until this closes.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off

_(left blank for the user — decision, date, and any overriding notes)_
