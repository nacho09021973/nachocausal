# Comité Decision 053 — prereg004-draft-readiness-c1

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question
Step 7 of comité 052 §9: is `docs/preregistration_004_draft.md`, together with the candidate instrument `nachocausal2p1/`, ready for the PI to sign the comité 052 verdict and decide C1 (commit the non-draft `docs/preregistration_004.md` + `STATUS = "FROZEN"` + sealed fixture)? If not, what exactly must change before C1? The committee does not authorise C1-C3; the PI decides.

## 2. Verified state
Facts checked **this session** (2026-10-15, worktree `.worktrees/prereg004-step3`, branch `prereg004/step3-port`), each with its command / file:line. Anything unchecked is marked `[UNVERIFIED]`.
- `git log --oneline -4` → `efada85` (record audit 046), `782d031` (resolve audit 045 findings), `3cc152a` (record audit 045), `4190a10` (O8 fixes). `git status --short` is empty. `efada85` is pushed: `git ls-remote origin refs/heads/prereg004/step3-port` → `efada85cc2c6…`.
- `make verify-seal verify-2p1 PY=/home/ignac/nachocausal/.venv/bin/python` gave:
  - 1+1 seal `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, intact;
  - `nachocausal2p1/thresholds.py` `2bf954fb…`;
  - τ fixture `4bc4aec8…`.
- `sha256sum nachocausal2p1/seed_manifest.py` → `e4047104…`.
- `nachocausal2p1/thresholds.py:31` is `STATUS = "CANDIDATE_NOT_FROZEN"`.
- Not present: `docs/preregistration_004.md`, `docs/validation_004_seeds.json` and `results/`. No virgin seed has been drawn and no 2+1 validation output exists.
- `pytest -q tests/test_004_seed_manifest.py tests/test_2p1_package.py tests/test_004_criteria_can_fail.py` → **61 passed** in 13.05 s. The global suite was not rerun.
- `git check-ignore -v results/validation_004.json` → `.gitignore:21:results/`. The draft's "committed immediately" (§9) is therefore not executable with a plain `git add`.
- `grep -n 'test-004\|dry-run-004\|verify-seal-004' Makefile` → no output.
- `nachocausal2p1/validate.py:226-233` (read by the chair): `verdict_from_levels` returns INCONCLUSIVE, with no `checks`, before evaluating (i) whenever any ρ level is not `scored`.
- `validate.py:191-192`: `np.std` of one midpoint is `0.0`, so `stab_pass` can be True with n_clean = 1.
- `validate.py:248`: coverage uses `>=`.
- `seed_manifest.py:40-42`: C1 is identified as the unique commit returned by `git log --diff-filter=A -- docs/preregistration_004.md`.
- Producers of the audits:
  - 045 and 046 were produced by **Codex** (header line 3 of each report).
  - 043 and 044 do not name their producer `[UNVERIFIED]`. Draft §9 says they are the same family as the author.
  - The falsifier's statement that 045 is Claude is **contradicted** by 045's own header.
- Cross-family content review: only Gemini O8, on `5afb33d`, before the D1-D12 fixes (`revisiones/2026-10-14-prereg004-gemini/evaluacion.md`).
- Stale text in the draft (chair, confirmed by every wave-1 role):
  - §3 shows thresholds `e7a69934…`, but the file is now `2bf954fb…`;
  - §9 "Audit trail" stops at 043/044;
  - §10 still says the re-audit is pending.
- Prior input to this question: `/auditor` 046 `AUDIT_VERDICT=AUDIT_PASS` (0 errors, 0 warnings) on the delta `3cc152a..782d031`. It states that it does not certify session separation.
- `HERRAMIENTAS_COMMIT` `c12c10e` (`git -C ~/herramientas rev-parse --short HEAD`). This is informational: this committee is the repo's own `.claude/skills/comite/`.

## 3. Dossier
Files and references the chair supplied to the committee (dossier text kept at the chair's scratchpad; reproduced in substance in §2):
- docs/preregistration_004_draft.md (object under review)
- docs/comite/comite_decision_052_prereg004-2p1-design.md
- docs/prereg004_auditor045_remediation.md
- docs/auditor/auditor_report_043_prereg004-2p1-candidate-package.md, …_044_prereg004-2p1-remediation-reaudit.md, …_045_prereg004-post-044-delta.md, …_046_prereg004-auditor045-remediation-reaudit.md
- revisiones/2026-10-14-prereg004-gemini/evaluacion.md; revisiones/2026-10-13-anclaje-theta-ciego/astra.md
- nachocausal2p1/ (thresholds.py, validate.py, seed_manifest.py, generator.py, estimator.py, gate.py, scoring/, dry_run.py)
- tests/test_004_criteria_can_fail.py, tests/test_004_seed_manifest.py, tests/test_2p1_package.py
- dev/PREREG004_STEPS_1_2_2026-10-13.md, dev/PREREG004_STEP_3_2026-10-13.md, dev/PREREG004_STEP_4_2026-10-13.md, dev/PREREG004_STEP_5_2026-10-13.md
- docs/preregistration_002.md, docs/preregistration_002_result.md; docs/acta_frente_2p1_ecuatorial_2026-10-12.md
- research_program/puente_3p1/2026-10-12/E1_equatorial_restriction_lemma.md
- biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md (EGS); biblioteca/derived-md/The causal set approach to quantum gravity.md (Surya LRR 2019)

- Members and models: reproducibility engineer, mathematician, logician, physicist (opus, wave 1, blind); falsifier (fable), pre-registration warden (sonnet), literature verifier (sonnet) (wave 2). The logician prompt added a focus line (text-vs-code of §7, C1/C2/C3 logic); the other wave-1 prompts were identical.

## 4. Expert briefs (wave 1 — blind, parallel)
### Reproducibility engineer brief
**Bottom line (SWE):** The draft is not ready for C1 as written. No change to the scientific design is needed. There are four defects in the C1 text and mechanics: R1 to R4 below. All are editorial or tooling fixes that can be made before C1 without touching any θ, the ρ grid, T or the seeds. The two load-bearing ones are R1 (no defined way to commit the result) and R3 (stale SHAs in the text to be sealed). Until they are fixed, the PI would be signing a frozen text that contradicts the repo and an unspecified commit procedure.

- **Proposed artefact(s):**
  - **C1** (one commit, the unique commit that adds the file, as required by `nachocausal2p1/seed_manifest.py:40-42`):
    - `docs/preregistration_004.md` (the non-draft, de-staled text).
    - `nachocausal2p1/thresholds.py` with `STATUS = "FROZEN"` (currently `:31` `CANDIDATE_NOT_FROZEN`).
    - The existing `nachocausal2p1/fixtures/tau_table_2p1.json` (4bc4aec8…, also enforced at runtime in `nachocausal2p1/gate.py:29-31`).
  - **C2:** only `docs/validation_004_seeds.json`, written by `python -m nachocausal2p1.seed_manifest <full-C1-SHA>` (`seed_manifest.py:85-101`; it refuses to overwrite, refuses a dirty tree, and refuses anything before FROZEN).
  - **C3 outputs:**
    - `results/validation_004.json`
    - `results/validation_004.progress.jsonl`
    - `results/validation_004_provenance_launch.txt`
    - `results/validation_004_run.log` (stdout and stderr, so an `ABORTED_*` traceback is kept; draft §9 l.284-288)
    - then `docs/preregistration_004_result.md`
  - **Missing before C1 (asked for by comité 052, `docs/comite/comite_decision_052_prereg004-2p1-design.md:85-86,90-93`):** the Makefile has none of the `test-004`, `dry-run-004` or `verify-seal-004` targets. Only `verify-2p1` exists (`Makefile:21-23`). Either add them before C1, or have the frozen text name the exact substitute commands. Today the "make test-004" step is not executable as specified.

- **Environment & seal:**
  - **Environment:** the sealed CPU `.venv` (`/home/ignac/nachocausal/.venv`, Python 3.12.3).
    - `thresholds.assert_environment()` hard-pins numpy 1.26.4, numba 0.66.0, llvmlite 0.48.0 and scipy 1.17.1 (`nachocausal2p1/thresholds.py:35-62`), matching `requirements-lock.txt:10,14,15,26`.
    - It also forbids CuPy and requires `NC2P1_DEVICE` to be unset or `cpu`.
    - Minz/`venv_minz` (CLAUDE.md:50) is not needed on the 2+1 path, because the gate is the τ fixture.
  - **Before C1 and before/after C3:**
    - `make verify-seal PY=<.venv>` must print `6e2c3888…12bfefd4`.
    - `make verify-2p1` must show the thresholds SHA (2bf954fb… now; this changes at C1 and must then be recorded) and τ fixture 4bc4aec8….
    - `git diff --exit-code <C1> -- nachocausal/ nachocausal2p1/ docs/preregistration_004.md` must be empty. This is enforced in code: `seed_manifest.py:43`, reached through `validate.run → thresholds.validation_seeds → load_manifest`.
  - **Package-diff-clean gap:** `assert_environment` checks only 5 packages. Nothing compares the full `pip freeze` with `requirements-lock.txt`. Recommend that C3 pre-flight `diff` them and record the result in the provenance file. Advisory only; not a blocker.

- **Provenance capture:**
  - `results/validation_004_provenance_launch.txt` with:
    - start/end UTC
    - HEAD SHA and branch; the C1 SHA; the C2 manifest sha256
    - both thresholds SHAs, the τ fixture SHA and the three imported 1+1 SHAs (draft §3)
    - a zero-diff line count; empty `git status --porcelain`
    - `uname -a`, `python -V`, full `pip freeze`
    - `NUMBA_NUM_THREADS=20` and OMP/MKL env; numba cache off
    - `T_EDGE` at runtime
    - the 20 seeds, `draw_seed` and the recipe
    - the test pass count
  - **Gap:** no code produces this file. Gemini already flagged it (`revisiones/2026-10-14-prereg004-gemini/informe_gemini.md:86`), and `grep provenance_launch` finds it only in docs. So it is a manual step and must be scripted or written out command-by-command in the frozen text.
  - **Add `lscpu` / CPU model:** the 20-thread pin is tied to the one measured host, an i7-13700 under WSL2 (draft §8 l.253-254).

- **Run mechanics:**
  - **Reversible pre-flight (no virgin seed):**
    - the full `make test` plus the three 004 test files (61 passed per dossier; global suite not rerun this session);
    - `python -m nachocausal2p1.dry_run` (off-grid ρ = 2, burned seeds, no widths; `nachocausal2p1/dry_run.py:16-29`);
    - the seal checks above.
    - Comité 052:86 also anticipated a full-grid dry run after C1 on `DRY_RUN_SEEDS`. The draft does not say whether it is part of the plan. State it, or drop it explicitly.
  - **Committing steps:** C2, then C3. C3 is a single background invocation with an explicit environment and a log, for example `setsid nohup env NUMBA_NUM_THREADS=20 <.venv>/bin/python -m nachocausal2p1.validate > results/validation_004_run.log 2>&1`. It runs about 4.4 h, which is `[UNVERIFIED]` extrapolation (draft §8 l.255-258).
  - **Clean abort before seed 1:** the code already aborts on wrong env/pins, threads ≠ 20, FROZEN missing, a manifest mismatch or dirty tree, a sealed-path diff, or an existing result (`validate.py:262-283`, `seed_manifest.py:74-82`).
  - **Mid-run:** invalid seeds count toward INCONCLUSIVE. Guard-v and τ-range aborts are deterministic and not relaunched. Only a no-output crash is relaunched on the same seeds (draft §9 l.272-288).
  - **Keep the machine awake:** WSL2 host sleep is an unlogged crash vector. Pin power settings for the run `[UNVERIFIED]`.

- **Reproducibility risks / ambiguities:**
  - **R1 (blocker, repeats the prereg-002 failure).** Draft §9 l.277-278 says `results/validation_004.json` is "committed immediately". But `results/` is git-ignored (`.gitignore:19-21`: "not committed. The committed verdict record lives in docs/"), and auditor 046:71 confirms that `check-ignore` matches. A plain `git add` silently does nothing. That is exactly the `PRIMARY_ARTIFACT_LOST` path (`docs/preregistration_002_result.md:1,22`). The frozen text must fix the mechanism: `git add -f` of the result, the progress log, the provenance file and the run log, plus sha256 recorded in `docs/`, or a copy into `docs/` with hashes.
  - **R2.** The progress "heartbeat" lives in ignored `results/`. Comité 052:93 asked for a log to a committed path. This is covered only if R1's force-add also covers it after a crash, as draft l.282-283 implies.
  - **R3 (blocker, text to be sealed).**
    - Draft §3 l.100 shows thresholds `e7a69934…`, but the file is now `2bf954fb…` (dossier).
    - §9 l.312-316 omits audits 045/046, and still says the auditor is the same model family. 046 was Codex, with the self-stated caveat about session separation.
    - §10 l.343-348 and l.355 still say the re-audit is pending.
    - The SHA table also omits the 2+1 code files (`seed_manifest.py` e4047104…, `validate.py`, `generator.py`, `estimator.py`, `gate.py`, `scoring/`). Git-diff covers them, but recording them in the frozen doc removes any dependence on git history.
  - **R4.** The C2 binding uses `git log --diff-filter=A` on the current branch (`seed_manifest.py:40`). A squash or rebase merge of `prereg004/step3-port` after C1 changes or duplicates the C1 SHA, and that permanently breaks `load_manifest`. The frozen text must say where C1 to C3 are committed: on this branch, with no rewrite, and merged only by fast-forward or merge commit. `[UNVERIFIED]` whether this has been decided.
  - **R5 (declared, accepted).** The SHA-derived draw seed can be ground by whoever authors C1 (`thresholds.py:118-121`; draft §6 l.140-142; auditor 045 W1). This is not re-litigated. Recommend pushing C1 before running C2, so the published C1 is the reference.
  - **R6.** Thread determinism has never been probed. Parity was measured on 1 of 10 seeds only (O2/O3, accepted by the PI). Bit-reproducibility is therefore claimed only for 20 threads on the measured host. A rerun on other hardware is unverified by construction, and the result doc must say so.
  - **R7 (minor).** `validate.py:295-296` writes the progress `start` time with local `%z`. Make sure the provenance file records UTC so relaunch timestamps can be compared.
### Mathematician brief
- **Computability.** Once the order matrix exists, everything the estimator does is decided exactly from the order plus counts, and runs in polynomial time:
  - Minimal elements are the rows with an empty past (`nachocausal/estimator.py:113-131`).
  - O(i) = |future(i)| is a column sum, O(N²).
  - The 1-D 2-means split and `improvement` are exact, O(n log n), and invariant under shift and scale (`nachocausal/estimator.py:80-155`).
  - The τ(n) gate is a table lookup for n in [2, 256]. When n > 256 it raises an error and the run aborts; it never extrapolates (`nachocausal2p1/gate.py:87-99`).

  The matrix itself is the part that is not exact. It is built by numerical geodesic shooting (`nachocausal2p1/generator.py:299-346`). It is still a strict partial order by construction: a relation requires U_x<U_y and V_x<V_y, which makes it irreflexive and antisymmetric. Transitivity is then checked in full on the output matrix (`generator.py:366-369`). The float32 A@A is exact because N ≈ 5.278·16·126 ≈ 10.6k < 2²⁴.

  Only these parts of the matrix are certified by sampling: the 20 000-pair re-shoot audit and the same-angle radial closed form (`generator.py:356-363`). The rest is not certified. Draft A4 (l.48-49) states this correctly.

  Margin on the gate range: the largest dev n_minimal is 184, against a cap of 256 (`dev/PREREG004_STEPS_1_2_2026-10-13.md:12`). My order-of-magnitude estimate is E[n_min] ≈ c₃ρ^{2/3}·(proper area of t*=0) ≈ 0.88·25.1·6.4 ≈ 140 at ρ=126. The Poisson standard deviation is about 12, so an abort for exceeding 256 is far in the tail [UNVERIFIED — my arithmetic, not a committed script]. OUT_OF_DOMAIN cannot fire at T=16; the draft says so correctly (l.204-205).

- **Order observable.** The observable is the estimator-v2 future volume: O(i) = |{j : i ≺ j}| for each minimal element i (`docs/estimator_v2_freeze.md`; `nachocausal/estimator.py:113-131`). The minimal elements are split by 1-D 2-means.
  - Why it carries the horizon signal: the future of an interior minimal element (r<2M) is confined to r<r_i and ends at the r=0.1 wall in finite t*. Its O is therefore bounded independently of T. An exterior element's future grows with T. EGS describe exactly this bimodality for longest chains (EGS derived-md l.181-191, l.463) and for future cardinality (l.193).
  - EGS also warn (l.193) that future cardinality "may be affected more strongly by the choice of boundary". That is the origin of the T-dependent effective boundary disclosed at draft l.34-35.
  - The order is the ambient order restricted to the sprinkled points: the Kruskal 1+1 order plus the angular reach `dist_phi ≤ min(π, sup L)` (`generator.py:12-14`; E1 lemma, `research_program/puente_3p1/2026-10-12/E1_equatorial_restriction_lemma.md` §3, with the [INFERENCE] step disclosed as A2).
  - The flat control is a genuine flat Poisson sprinkle. The cloud's density ∝ r on (r, φ) is uniform in Cartesian x, y, and `mink_order` uses the Euclidean distance (`generator.py:100-105, 349-353`). So it is a fair same-cloud null.

- **Relevant invariants.**
  - Minimal-antichain size n: its scaling ρ^{(D−1)/D} = ρ^{2/3} is derived by ASTRA (`revisiones/2026-10-13-anclaje-theta-ciego/astra.md` l.7-12). It is also the gate's n.
  - Future cardinality: counts are legitimate, "Order + Number" (Surya LRR, `biblioteca/derived-md/The causal set approach to quantum gravity.md` l.409-410, Myrheim 1978).
  - Longest chain / height: this is the EGS diagnostic (EGS l.181) and the discrete geodesic distance (Surya LRR l.1226). It is not the estimator here.
  - The ordering fraction and Myrheim–Meyer dimension (Surya LRR l.1000-1010) are not used and are not needed.
  - Guard-v (relabelling invariance, `nachocausal/estimator.py:164`) is a necessary, not sufficient, certificate that the observable depends only on the order. That is enough here because the code reads only the matrix (`nachocausal2p1/estimator.py:29-45`).

- **Analytic / continuum target.**
  - The target is the coordinate locus r = 2M = 0.5 on the t*=0 slice of a finite equatorial EF box. It is reached as the bracket between the radially adjacent minimal elements on either side, not as an event horizon (draft §1).
  - The bracket's discreteness scale comes from the radial intensity of minimal elements at the slice. The induced metric there is h = (1+2M/r)dr² + r²dφ² (ASTRA l.3-5). ASTRA gives λ_r(r) ≈ c₃ρ^{2/3}·2πr√(1+2M/r), with c₃ = Γ(4/3)(3/π)^{1/3} ≈ 0.88 (ASTRA l.33-41).
  - The frozen scale is ℓ_rad = ρ^{-2/3}/(1.4π) (`nachocausal2p1/thresholds.py:195-213`). I re-checked the table: at ρ=126, ρ^{2/3} ≈ 25.13, so ℓ_rad ≈ 0.009047, θ_loc ≈ 0.03619 and θ_stab ≈ 0.01809. This matches draft l.173-176.
  - In 1+1 the same construction gives ρ^{-1/2}, which matches the sealed `ell` (`nachocausal/thresholds.py:101-113`). The dimensional transfer is consistent.

- **Caveats.**
  - **Tight passability of (ii) width/IQR, even for a perfect classifier — must be disclosed before C1.** My own analysis, using only the frozen formula and ASTRA's idealised model and no dev data [UNVERIFIED — my arithmetic, not a committed script]:
    1. With perfect classification at a sharp boundary, width ~ Gamma(2, δ) with δ = 1/λ_r(2M) ≈ 0.256ρ^{-2/3} ≈ 1.13·ℓ_rad.
    2. The ideal median width is then 1.678δ ≈ 1.90ℓ_rad, against the bound 2ℓ_rad. The ideal IQR is 1.73δ ≈ 1.96ℓ_rad, against the same bound.
    3. For a median of 20 seeds, P(pass) ≈ Φ(0.26) ≈ 0.6. The IQR clause is near a coin flip. The O(1) corrections (flat-cone approximation at ρ^{-1/3} ≈ 0.2 against curvature scale M = 0.25) are larger than these margins.
    4. ASTRA flagged the same thing (l.42, l.52: "K=2 does not define a coverage level"; 0.594).

    This does not breach a founding rule. It concerns power, not whether the criteria can fail, and θ was not compared with dev widths. So I do **not** re-litigate the (c1) anchor. But §7 should say in advance that a FAIL of (ii)-width/IQR is compatible even with ideal order-only localisation. That way the result cannot later be argued to justify loosening or re-deriving θ (`NO_THRESHOLD_LOOSENING`). This is a wording addition to the "Known weakness" bullet (l.230-233), not a parameter change.
  - **Uniform null for τ(n) — inherited, declare only.** τ(n) is calibrated against a Uniform[0,1] null (`scripts/gen_tau_table.py:4, 60`). `improvement` is shift/scale-invariant but not shape-invariant, and the flat-control O law is not uniform. The gate is a heuristic threshold, not a calibrated test against the actual flat null. This is why (iv) is measured empirically and why (i)/(iv) are gate-derived (draft l.206-211). Inherited from the sealed 1+1; no change needed.
  - **Unrecorded near-null relations — minor, declare.** Pairs with |d − dmax| < TOL are counted (`generator.py:325-327`, `near_boundary_pairs_tol`) but neither invalidate the seed nor are reported among the per-level aggregates. One wrong relation can flip an element's minimality and therefore n and O. In the continuum this is a measure-zero event [UNVERIFIED that it is negligible at TOL = 1e-6]. I recommend reporting `near_boundary_pairs_tol` per seed in the result for transparency. It is not a criterion change.
  - **Future cardinality vs longest chain.** The observable departs from the EGS longest-chain diagnostic, and EGS expect it to be more boundary-sensitive (EGS l.193). This is consistent with the disclosed T-dependent effective boundary. The "no event-horizon claim" (draft l.33-35) is therefore mathematically required, not just prudent.
  - **Stale documentary text (agrees with the chair) — must be fixed before C1.**
    - §3: the candidate `thresholds.py` SHA is e7a69934…, but the current value is 2bf954fb… (draft l.100).
    - §9: the audit trail stops at 043/044 (l.312-316).
    - §10: the text still says the re-audit is pending (l.343-347, l.355), but report 046 was AUDIT_PASS.

    None of these affects the order-theoretic content. They are documentary defects, but a frozen pre-registration must not misstate its own audit state.
  - **Mathematical verdict.** The observable, order construction, gate and scoring are order-theoretically sound, computable, and correctly separated from the hidden embedding (`nachocausal2p1/scoring/scorer.py` is the only place r is read). Ready for C1 subject to (a) fixing the stale §3/§9/§10 text and (b) adding the a-priori tight-passability disclosure to §7. Neither (a) nor (b) changes any threshold, seed or code path. The PI decides C1.
### Mathematical logic brief
- **Formal status:**
  - No Lean or other formal artefact covers prereg-004. `grep -rl "2p1|prereg.*004|equatorial" formal/` returns nothing. Every statement in the draft is therefore a *definition* (the criteria, implemented in `nachocausal2p1/validate.py:160-256` and `thresholds.py:177-213`), a *declared assumption* (A1-A4, draft §1:41-49; E1's maximiser step is self-marked `[INFERENCE]`), or a *physical interpretation*. None of it is a proved theorem.
  - The can-fail property is shown by examples, not proved. Each clause has a synthetic counterexample in `tests/test_004_criteria_can_fail.py:108-276`, and the chair reports 61 tests passing.
  - θ(ρ) is a definition anchored in a blind derivation (ASTRA). It is not a derived bound. I checked ρ=126 by hand: 126^(-2/3)/(1.4π) ≈ 0.009049, giving θ_loc ≈ 0.0362 and θ_stab ≈ 0.0181. Both match draft §7:173-176 and `thresholds.py:195-207`.
- **Quantifier / dependency order:**
  - **Most of §7 matches the code.** (i) is checked ∀ρ∈{63,126} as (p_perm ≤ 1e-4 ∧ n_abstain_BH < 3) (`validate.py:177-178,234-235`). (ii) and (iii) are checked only at ρ*=126. F is checked for each consecutive pair, with the slack taken from the lower level ρ_k (`validate.py:238-244`), as the draft says. (iv) is checked at ρ* over generator-valid seeds. Coverage is counted over bracket-valid seeds. Seeds where the BH abstained are not bracket-valid (`validate.py:147-149`), so they leave the coverage denominator.
  - **Verdict precedence (code):** OUT_OF_DOMAIN (`validate.py:285`) > deterministic abort (an exception) > INCONCLUSIVE (`:229-233`) > PASS/FAIL. The draft never states this order.
  - **Defect Q1: text contradicts code.** Draft §7:200-201 says "≥ 3 BH abstentions is a **FAIL** of (i), never INCONCLUSIVE".
    - In the code, if *any* level has fewer than 18 generator-valid seeds, the verdict is INCONCLUSIVE before (i) is evaluated, even when ρ=126 has 3 or more abstentions.
    - The INCONCLUSIVE branch also returns no `checks` dict (`:231-233`), so the failed (i) is not recorded as a check. Only the level aggregates show it.
    - What is true is narrower: "abstentions never *cause* INCONCLUSIVE". The sentence should say exactly that, and should state that INCONCLUSIVE takes precedence over every FAIL.
    - This is not a re-litigation of the D2 or §11 decisions. It only makes the text match the code.
  - **C1→C2 dependency.**
    - The draw seed is a function of the C1 SHA (`thresholds.py:123-128`). `seed_manifest._check_freeze` defines "C1" as *the unique commit in HEAD's ancestry that adds `docs/preregistration_004.md`* (`seed_manifest.py:40-42`). It does not check against a SHA that was announced in advance.
    - So an amend, rebase or squash of C1 *before C2* silently produces a new valid C1 and a new draw. That is an extra post-hoc degree of freedom, beyond the "author can pre-compute the hash" caveat the draft already discloses (§6:140-142).
    - The draft requires C2 to be published (§9:307) but never requires C1 to be pushed and its full SHA recorded before C2 is run.
  - **What C3 enforces.**
    - `load_manifest` (`seed_manifest.py:74-82`) enforces three things: the manifest equals its HEAD version, the tree is clean, and the sealed paths have zero diff against C1 (`:43`).
    - It does not enforce that HEAD *is* the C2 commit, or that anything has been pushed. That part is procedural. It is harmless because the sealed paths are diff-checked.
    - The sealed paths are `nachocausal/`, `nachocausal2p1/` and the frozen doc. They exclude `tests/`, the `Makefile` and `scripts/`, so the "test pass count" in the provenance file is not bound to C1.
- **Equivalence claims:**
  - **"Every pass test is written as `x ≤ bound`"** (§7:202) is literally false.
    - Coverage is written `coverage_frac >= COVERAGE_FLOOR` (`validate.py:248`) and (i) uses `n_abstain_BH < 3` (`:178`).
    - The *semantic* claim, that NaN never passes, still holds for these clauses, because every IEEE comparison with NaN is False.
  - **"NaN (empty or one-element sample) never passes"** (§7:202) is false for (iii).
    - `np.std` of a single clean midpoint is `0.0`, not NaN (`validate.py:191`), so `stab_pass=True` with n_clean=1.
    - The run verdict is unaffected, because IQR is then NaN and (ii) fails (`_iqr`, `:76-77`). But the per-check boolean for (iii) misreports.
    - The draft also leaves the std convention unstated: it is population std (ddof=0).
  - **"(i) reduces to < 3 BH abstentions"** (§7:206-211) is one-way and conditional.
    - It holds only if no flat-control seed escapes (then d ≥ 0 and p = 2^-m).
    - It needs m ≥ 14, since 2^-13 > 1e-4 (`thresholds.py:102`), and n_valid ≥ 18 with < 3 abstentions gives m ≥ 16.
    - A flat-control escape can make d < 0, so it is not an equivalence in general. The draft does word it conditionally, which is correct.
  - **(v)** cannot evaluate to False under the validation label. `run` refuses `guard=False` (`validate.py:276-277`), and a failing Guard-v raises an exception instead of returning a result. So (v) is a precondition enforced by abort, not a criterion that can fail. The can-fail test (`test_v_guard_off_fails_v_only`) uses a non-validation path. The draft should state this, as it already does for OUT_OF_DOMAIN (§7:204-205).
  - **Manifest ↔ C1 SHA** is a genuine functional equivalence. `check_manifest` recomputes `_draw(sha)` and requires equality (`seed_manifest.py:61-70`).
- **Type / object discipline:**
  - Units are consistent: (ii) uses widths/2M and θ_loc is dimensionless; (iii) uses raw midpoint std in r and θ_stab = K·ell_rad in r.
  - **Terminology clash.** The level field `loc_inconclusive` (`validate.py:187`) and the draft's phrase "else inconclusive ⇒ not passed" (§7:192) produce a **FAIL** of (ii), not the verdict INCONCLUSIVE. The test name `test_nan_iqr_is_inconclusive_not_pass` (`tests/test_004_criteria_can_fail.py:250`) repeats the clash. The draft text should say "fails (ii)" so the IQR clause is not read as a third route to INCONCLUSIVE.
  - Coverage is a fraction over a seed set (bracket-valid seeds) that differs from the set behind the median, IQR and std (clean brackets). The draft declares this (D8, §7:220-223). It is consistent.
- **Caveats:**
  - **Fail-closed trap at C1.** If C1 creates the frozen doc by `git mv` of the draft, or adds it while deleting a similar draft, git's default rename detection (diff.renames is unset here; git 2.43) reports the change as R, not A. Then `--diff-filter=A` returns nothing and C2 refuses.
    - This is not a soundness hole, but it would block C2. The C1 instruction should say "add as a new file; keep the draft". `[UNVERIFIED — not executed; inferred from git defaults and seed_manifest.py:40]`
  - **Writing/committing contradiction.** `results/` is in `.gitignore:21` (I confirmed with `git check-ignore`). That is what keeps the tree clean during C3, which matters because `check_seed`→`load_manifest` re-runs `git status --porcelain` on every seed (`validate.py:95`, `seed_manifest.py:80`). But §9:277-283 says the result and progress log are "committed immediately". That needs `git add -f`, and the draft should say so.
  - **Stale draft text** (chair-observed, and I confirmed it):
    - §3:100 lists thresholds SHA e7a69934…, but the current file is 2bf954fb….
    - §9:312-316 cites only audits 043/044.
    - §10:345-347 and §10:355 still say the re-audit is pending, but report 046 is done.
    - §9:314 "same model family … not independent" was true of 044 but not of the Codex-run 046.
  - **Not ready for C1 as written.** I see no logical defect that stops a criterion from failing or lets a NaN or INCONCLUSIVE case become a PASS. But the text should change before C1:
    1. Fix Q1 and state the verdict precedence explicitly.
    2. Correct the `x ≤ bound` / one-element-NaN claims, or change (iii) to return NaN when n_clean < 2. A code change needs a re-audit, so wording is the cheaper fix.
    3. Rename the IQR "inconclusive" wording.
    4. Declare that (v) is enforced by abort.
    5. Require that C1 be pushed and its full SHA recorded before C2, with no amend, rebase or squash afterwards.
    6. Fix the stale SHA, audit and §10 text and the `git add -f` wording.
### Physicist brief
- **Coordinates and patch.** The step must use ingoing Eddington–Finkelstein coordinates on the equatorial plane: `-(1-2M/r)dv² + 2dv dr + r²dφ²` with `v = t* + r` (draft §2 l.55). The generator maps these to Kruskal coordinates as `V = e^{(t*+r)/4M}`, `UV = (1-r/2M)e^{r/2M}` (`nachocausal2p1/generator.py` `to_kruskal`). This is horizon-penetrating, and the slices `t* = const` are spacelike everywhere, so the initial slice where the minimal elements sit is a legitimate past boundary on both sides of r = 2M.
  - The patch is finite: `t* ∈ [0,16]`, `r ∈ [0.1,1.3]`, `φ ∈ S¹`, with 2M = 0.5 (`nachocausal2p1/thresholds.py:85-91`).
  - Finiteness gives up the following:
    - Any event-horizon claim. EGS defines the event horizon through J⁺ and needs an infinite causal set (EGS derived-md l.173-181).
    - Any statement beyond T = 16, so no "for all T" and no decay law (draft §2 l.63-68).
    - Any statement at r < 0.1. The inner wall stands in for the singularity: inside the horizon it is spacelike and acts as a future boundary.
  - The order is the ambient Schwarzschild order restricted to the sprinkled points, not the box's intrinsic order (draft A1). E1's `Delta_max` criterion depends on a step its author marked `[INFERENCE]` (`research_program/puente_3p1/2026-10-12/E1_equatorial_restriction_lemma.md:98,172`). The draft correctly lists A1-A4 as assumptions, not proofs.

- **Physical meaning of the signal.** Every future-directed causal curve from a minimal element inside r = 2M reaches the inner wall at r = 0.1 in finite t*. So its future, counted inside the box, saturates. An exterior minimal element's future grows roughly in proportion to T. This is the mechanism EGS gives for proper time and longest chains, and EGS note that future cardinality is also bimodal (EGS l.188-193).
  - Rough check `[INFERENCE, my own order-of-magnitude estimate]`: near-horizon tails on both sides grow only like `4M·ln(2M/|r−2M|)`. At T = 16 = 16·(4M), the 2-means threshold sits far from both tails. So I expect misclassification near r = 2M to be smaller than the Poisson spacing.
  - Two limits:
    - EGS warn that the cardinality diagnostic "may be affected more strongly by the choice of boundary" than chain length (EGS l.193). The signal depends on the box (inner wall, T); it is not intrinsic to the spacetime.
    - The thing being located is the coordinate locus r = 2M on the initial slice, read only through scoring. It is not a horizon surface.

- **Sprinkling domain.**
  - Poisson sprinkling with density proportional to `√−g = r` on the declared box. The mean is `round(ρ·5.278·T)` (`generator.py` `sprinkle`; `thresholds.py:90-108`).
  - ρ grid {32, 63, 126}, primary ρ* = 126 (`thresholds.py:100-101`).
  - Flat control: the Minkowski order on the same cloud, treating (r, φ) as Cartesian polar coordinates (`generator.py:349-353`).
  - Guarantees given up:
    - The three levels share one random stream, so they are not independent sprinkles of each other. This is declared in §7 (D7).
    - The order is decided by numerical geodesic shooting, checked per seed rather than proved analytically (A4).
    - The minimal-element layer is a 2D surface density. Its radial intensity at r is approximately `λ_r(r) = c₃ρ^{2/3}·2πr·√(1+2M/r)`, with `c₃ = Γ(4/3)(3/π)^{1/3} ≈ 0.88` (ASTRA, `revisiones/2026-10-13-anclaje-theta-ciego/astra.md:35-40`).

- **Claim boundary.**
  - Claimed: finite 2+1 equatorial-patch localisation within the frozen θ on the frozen ρ grid, with T = 16 and r ∈ [0.1, 1.3] (draft §1 l.28).
  - Not claimed:
    - metric reconstruction;
    - an event horizon or apparent horizon;
    - a 3+1 result (E1 transfers only the order on the equator, not any property of the estimator);
    - 2+1 gravity (the bench metric is not an Einstein solution in 2+1);
    - "for all ρ" or "for all T".
  - Regular-black-hole caveat: EGS l.195 say the partition "would no longer work for regular black holes" (for example Hayward), because the interior allows arbitrarily long proper time. The draft carries this correctly (§1 l.38). A PASS says nothing about whether the method works for singular-versus-regular geometries in general.
  - Coverage floor of 0.5: a narrow but mislocated bracket can pass (draft §7 l.230-233). The verdict therefore certifies "frequently covers and is narrow", not "accurate".

- **Caveats.**
  - **(Physics; affects interpretation; must be added to §7 before C1.)** Even a perfect classifier sits at the Poisson resolution limit under the (c1) anchor.
    - Ideal model `[INFERENCE, flat-local approximation; ρ^{-1/3} ≈ 0.2 is not ≪ 2M = 0.5]`: the bracket width of a perfect classifier is Gamma(2, δ), with `δ = 1/λ_r(2M) ≈ 1/(3.91 ρ^{2/3})`.
    - The bound is `θ_loc·2M = 2/(1.4π ρ^{2/3}) ≈ 1.78 δ`.
    - So for an ideal estimator:
      - P(single width ≤ bound) = `1 − e^{-1.78}(2.78) ≈ 0.53`;
      - the population median width is ≈ 0.94 × the bound;
      - the population IQR is ≈ 1.73 δ, about 0.97 × the bound.
    - The (ii) width and IQR clauses at ρ* could therefore fail with roughly coin-flip probability even if the order localised r = 2M perfectly.
    - Comparison with 1+1, using the same convention (ASTRA l.30): there the bound/δ ratio is about 2.5, so per-seed pass probability is about 0.71. The 2+1 anchor is relatively stricter, because P* is evaluated at r = 0.7 and the constant c₃ is absorbed into K_LOC (ASTRA l.33, l.52).
    - This uses no dev widths and no ground truth beyond theory. It neither breaks a founding rule nor makes a criterion unable to fail, so I do **not** reopen the PI's (c1)/K_LOC decision.
    - But ASTRA's own risk statement ("riesgo de exigir demasiado", astra.md:52) and the `λ_r` vs `ell_rad` gap (l.38-42) are missing from draft §7. Before C1, §7's "Known weakness" should add, in advance: a FAIL driven only by (ii)-width or IQR at ρ* is not evidence that the order fails to localise r = 2M, because the bound sits at about one Poisson spacing. θ stays unchanged. This is wording only.
  - The finite-T effective boundary is real at small T (`dev/2P1_PHASE_B_INTERIM_2026-10-12.md`, cited at draft l.34-35). T = 16 is a margin, not a measured plateau (draft l.63-68), and T was chosen using r = 2M scoring, so it is not ground-truth-free. These are declared correctly.
  - The order depends on `[INFERENCE]` steps in E1 (E1 lemma l.98, l.172) and on A3, the physicist's application of E1 to the box with r ≥ 0.1. Neither is formalised (Lean has nothing on 2+1: comité 052 l.153). This is acceptable as a stated assumption, not as a result.
  - The flat control treats (t*, r, φ) as Minkowski polar coordinates on the same cloud (`generator.py:349-353`). As the draft already says (§7 l.206-211), it is a gate-derived comparison, not an independent physical null.
  - Draft text is out of date and should be fixed before C1, though it does not affect the physics:
    - the §3 thresholds SHA is `e7a69934…` but the file is now `2bf954fb…`;
    - the §9 audit trail stops at 044;
    - §10 l.343-355 still says a re-audit is pending, but it has been done (046 AUDIT_PASS).
    - Source: chair's dossier `[UNVERIFIED by me beyond the draft text, which shows the old values at l.100, l.312-316, l.345-355]`.
  - **Readiness from the physics side:** coordinates, domain, observable and claim boundary are sound and correctly bounded. The only change I need before C1 is the §7 resolution-limit disclosure above, together with the text corrections. I see no physics reason to change T, ρ, θ or the order definition.

## 5. Falsifier attack
- **Concrete failure modes:**
  1. **The text to be frozen contradicts the code it seals.** The worst defect is Q1.
     - Draft §7 l.199-201 says "≥ 3 BH abstentions is a **FAIL** of (i), never INCONCLUSIVE".
     - In the code, `verdict_from_levels` returns INCONCLUSIVE first whenever any level is short (`nachocausal2p1/validate.py:229-233`). It also returns no `checks` dict in that case. So a decisive (i)-FAIL at ρ=126 is reported as INCONCLUSIVE whenever ρ=32 has ≤ 17 valid seeds. ρ=32 is not even a level that (i) requires (`validate.py:234`).
     - Draft l.202 says "every pass test is written as `x ≤ bound`, so a NaN (empty or one-element sample) never passes". That is false twice over. Coverage uses `>=` (`validate.py:248`). With one clean bracket, `np.std` gives 0.0, not NaN, so `stab_pass=True` (`validate.py:191-192`).
     - These are exactly the D1/D2 sentences that the O8 fixes introduced. Audits 045 and 046 both passed them. So the audit chain did not check text against code, and its PASS status says less than it appears to.
  2. **The frozen text misstates its own state.** All three wave-1 briefs and the chair confirm this:
     - §3 l.100 gives the thresholds SHA as e7a69934…, but the file is now 2bf954fb….
     - §9 l.312-316 stops at audit 044 and says the auditor is the "same model family". That is wrong for 046, which was run by Codex.
     - §10 l.343-355 still says the re-audit is pending.
     - A pre-registration that misreports its audit state cannot be signed as is.
  3. **C1 commits a result-writing mechanism that silently does nothing.** Draft §9 l.277-278 says the result is "committed immediately", but `results/` is git-ignored (`.gitignore:19-21`). A plain `git add` adds nothing, which is a repeat of `PRIMARY_ARTIFACT_LOST` (`docs/preregistration_002_result.md:1`). The provenance launch file has no producer in the code; it is a manual step.
  4. **The design gives the localisation clause little power.** Two briefs worked this out independently from theory alone (Mathematician, Physicist; both `[UNVERIFIED — their arithmetic]`). Even a perfect classifier passes (ii)-width/IQR at ρ* with probability of only about 0.5-0.6.
     - This does not stop the criterion from failing. It means a FAIL carries little information.
     - Disclosing this in advance is correct. But see "Verdict coercion" below on how the disclosure must be worded.
  5. **The sequence names Makefile targets that do not exist.** `make test-004`, `dry-run-004` and `verify-seal-004` were asked for by comité 052:85-93, but the `Makefile` targets list (`grep '^[a-z0-9-]*:' Makefile`) has none of them. `verify-comite` does exist.
  6. **Thread nondeterminism: lower risk than the briefs imply.** The `prange` loops in `generator.py:130-134,242-248,275-279` write one element per iteration, with no reductions across iterations. On inspection, 20-thread nondeterminism is unlikely. `[UNVERIFIED — never probed, O2]`.

- **Ground-truth leakage:**
  1. **None found in the blind path.**
     - The estimator is called on the order matrix only (`validate.py:143-144`).
     - r is first passed to `blind_bracket`, which runs after `thr` has been fixed (`validate.py:145-151`).
     - The progress log carries only `seed, rho, seconds` (`validate.py:48`).
  2. **Residual leak through the dev data.**
     - The dev widths at ρ=126, T=20 are committed (`dev/2p1_sweep_T_rho126_v2_2026-10-12.jsonl`, used by `tests/test_004_criteria_can_fail.py:34,138-145`). The frozen θ is in `thresholds.py`. The "do not compare θ with dev widths" rule (draft §7) therefore depends on people choosing not to look; nothing enforces it.
     - The step-4 mutation check has already shown a partial comparison: "(ii) también es falso en T = 8" (`dev/PREREG004_STEP_4_2026-10-13.md:61-65`, declared).
     - Requirement: the new §7 power disclosure must be derived from theory only (ASTRA plus the Gamma(2, δ) model). Its text must say so, and must say that no dev JSONL was consulted to write it.
  3. **Declared, not a blocker:** T=16 was chosen with r=2M scoring on exploration seeds (Physicist brief; `thresholds.py:86-87`). T shapes the observable O, so ground truth guided one parameter of the observable during dev. It is disclosed, and it was done on dev seeds, so I do not reopen the PI decision. The result document must repeat it.

- **Freeze violations:**
  1. **C1 can be re-made silently.**
     - `_check_freeze` defines C1 as "the unique commit in HEAD's ancestry adding the frozen doc" (`nachocausal2p1/seed_manifest.py:40-42`), not as a SHA announced in advance.
     - Before C2, an amend or rebase, or a new branch off efada85 with a fresh C1, produces a new valid C1 and a new 32-bit draw (`thresholds.py:123-128`).
     - After C3, the same route allows an undetectable "new C1 → new seeds → rerun". The one-shot guard is only the existence of a git-ignored file (`validate.py:281-282`).
     - Combined with the declared grinding freedom (W1/D5), and with the fact that generator code can be called directly on virgin seeds outside `check_seed`, the separation is enforced only by procedure.
     - I do not reopen D5. Before C2, though, C1 must be pushed and its full SHA recorded in a signed, pushed document (this comité's sign-off). C1 to C3 must stay on `prereg004/step3-port` with no rewrite, and be merged only fast-forward or by merge commit. C1 must add the frozen document as a new file, not by `git mv` of the draft (R detection breaks `--diff-filter=A`, logic brief).
  2. **No loosening or post-hoc tuning is smuggled in by the proposed edits,** provided they stay wording-only. Any code change (for example making (iii) NaN when n_clean < 2) reopens the audit chain and needs a new re-audit before C1.

- **Verdict coercion:**
  1. **INCONCLUSIVE silently takes priority over FAIL** (`validate.py:229-233`). FAIL can collapse into INCONCLUSIVE, and the per-clause outcomes are not recorded.
     - Before C1, the text must state the precedence: OUT_OF_DOMAIN > ABORTED_* > INCONCLUSIVE > PASS/FAIL.
     - It must also commit in advance that, under INCONCLUSIVE, the result document will report the clause values computable from the recorded aggregates, labelled non-verdict, so a masked (i) or (ii) failure is visible.
  2. **(v) can never be False under the validation label** (`validate.py:276-277`; Guard-v raises an exception instead). It is a precondition enforced by aborting, so it must not be listed as a sixth criterion that can fail.
  3. **The proposed "a FAIL of (ii) is not evidence of non-localisation" wording is itself asymmetric.** It excuses FAIL in advance and leaves PASS fully informative.
     - Required wording: FAIL is reported as FAIL, plainly. The low power is stated as a property of the test. The result can never be used to re-derive or loosen θ/K_LOC in any successor pre-registration.
     - The draft also says "else inconclusive ⇒ not passed" for the IQR clause (l.192). That clause produces a FAIL of (ii), not INCONCLUSIVE, so the word "inconclusive" there must be replaced.

- **Premature / over-broad claims:**
  - The claim boundary in §1 is correct: finite 2+1 equatorial patch, no event horizon, no 3+1 claim, no 2+1 gravity claim. No over-claim found.
  - Residual risk is in the reading: a PASS certifies "narrow and covers at least 50% of the time", not accuracy (coverage floor 0.5, l.230-233). (i) and (iv) follow from the gate and are not independent confirmation (l.206-211).
  - The result document must not count six "passed" criteria when (v) cannot fail and (i)/(iv) are gate-derived.

- **Independent-falsification gate:** Partially satisfied, which is not enough for an unconditional "ready".
  - Claude wrote the code. Audits 043, 044 and 045 are Claude.
  - The only review by a different model family on content is Gemini O8, on 5afb33d, before the fixes.
  - The O8 fixes (4190a10) were audited only by Claude (045). Codex 046 covered only the 782d031 delta, and states that it may not be session-separated.
  - This committee is Claude too. For the post-O8 semantics (the D1/D2 text versus the code), the author is effectively its own sole verifier, and failure mode 1 shows the result.
  - Recommendation: after the wording fixes, run one cross-family pass (any non-Claude model) over the final `docs/preregistration_004.md` §7/§9 text against `validate.py`. This should happen before C1, or else the gap must be declared in §9.

- **Minimal falsification test:** Run a pure-function check that touches no virgin seed and no width.
  - Call `validate.verdict_from_levels` on synthetic levels: ρ=32 with 17 generator-valid seeds (`status="inconclusive"`), ρ=126 with `n_abstain_BH=3`, and every other field passing.
  - Assert that the verdict is `INCONCLUSIVE` and that `"checks"` is absent.
  - This turns draft §7 l.199-201 ("≥ 3 abstentions is a FAIL of (i), never INCONCLUSIVE") into a failing executable fact.
  - Before C1, the text must be corrected to state the precedence, and this case must be added to `tests/test_004_criteria_can_fail.py` as a documented expectation. Until then the PI would be signing a pre-registration whose verdict rule is false as written.
  - **Verdict: NOT READY for C1.** All required changes are wording or procedure. No θ, ρ, T, seed or code path needs to change.

## 6. Pre-registration verdict
- Verdict: BLOCK
- Freeze status: Numeric thresholds (T=16, ρ grid {32,63,126}, ρ*=126, θ_loc/θ_stab via the ASTRA-derived (c1) anchor, τ fixture 4bc4aec8…) are written in advance in `docs/preregistration_004_draft.md` §7 (l.173-176 table) and `nachocausal2p1/thresholds.py`. Nothing is frozen yet. `thresholds.py:31` has `STATUS = "CANDIDATE_NOT_FROZEN"`. `docs/preregistration_004.md` and `docs/validation_004_seeds.json` do not exist (dossier). No validation seed has been seen. The text to be sealed is not yet fit to freeze, for the reasons below. They are editorial and wording fixes only, and no θ, T, ρ or seed changes.
- Seal integrity: The 1+1 seal `6e2c3888…12bfefd4` is intact (dossier `make verify-seal`). The 2+1 package imports the sealed 1+1 files unchanged. `seed_manifest.py:43` runs `git diff --exit-code <C1> -- SEALED_PATHS` on `nachocausal/`, `nachocausal2p1/` and the frozen doc. This is code-enforced, so RESPECT_SEAL_FREEZE is not at risk. Current candidate SHAs are thresholds `2bf954fb…` and τ fixture `4bc4aec8…`. The draft §3 table (l.100) still shows `e7a69934…`, which is false.
- Seed discipline: Virgin band 8_000_000..8_999_999 is untouched until C2 (dossier). The draw seed is the first 8 hex digits of the C1 SHA (D5). `seed_manifest.py:40-42` defines C1 as the unique commit that adds the frozen doc. Nothing requires C1 to be pushed and its full SHA announced before C2 is run. An amend, rebase or squash of C1 before C2 would silently produce a new valid C1 and a new draw. A squash or rebase merge after C1 would permanently break `load_manifest`. This is an unclosed post-hoc degree of freedom (Logician brief; SWE R4/R5). The author's ability to grind the hash is already declared (draft l.140-142) and is not re-litigated.
- Reporting rule: Partly satisfied. The draft treats PASS, FAIL and INCONCLUSIVE alike, and burned-seed and abort rules are stated at l.272-288. But the text misstates the verdict logic (defect 2 below), and the mechanism for committing the result is broken (defect 1 below). The 1+1 precedent `docs/preregistration_002_result.md` records this same failure as `PRIMARY_ARTIFACT_LOST`.
- Forbidden moves present? None found at present: no tuning, no loosening, no leakage, no re-run after peeking, and no reconstruction over-claim. Two latent risks are listed in the reasons. The first is an undeclared ideal-case FAIL probability for (ii), which invites a later θ re-derivation. The second is the open C1 SHA procedure.
- Reasons (the first six must change before C1; I checked 1-3 and 5 against the repo, and took 4 and 6 from the wave-1 briefs):
  1. **Result-commit mechanism is broken (blocker).** Draft l.277 says `results/validation_004.json` is "committed immediately". `.gitignore:19-21` ignores `results/` ("not committed. The committed verdict record lives in docs/"). A plain `git add` does nothing. The frozen text must specify `git add -f` of the result, progress log, provenance file and run log, or a copy into `docs/` with sha256 values. This is the PRIMARY_ARTIFACT_LOST path from prereg-002.
  2. **Text contradicts code on verdict precedence (blocker).** Draft l.200-201 says ≥3 BH abstentions is "a FAIL of (i), never INCONCLUSIVE". In `validate.py` (Logician: l.229-233), INCONCLUSIVE (any level with <18 valid seeds) takes precedence over every FAIL, and the INCONCLUSIVE branch returns no `checks`. The text should say that abstentions never cause INCONCLUSIVE, and it should state the full precedence: OUT_OF_DOMAIN > abort > INCONCLUSIVE > PASS/FAIL. This only aligns the text with the code. It is not a re-litigation of D2 or §11.
  3. **Stale SHAs and audit state in the text to be sealed (blocker).** l.100 shows thresholds `e7a69934…` against the real `2bf954fb…`. l.312-316 stops at audits 043/044. l.346 and l.355 still say the re-audit is pending, but audit 046 was AUDIT_PASS (Codex). l.314's "same model family, not independent" claim does not describe 046. The SHA table also omits the 2+1 code files (`seed_manifest.py` `e4047104…`, `validate.py`, `generator.py`, `estimator.py`, `gate.py`, `scoring/`). A frozen pre-registration must not misstate its own audit state.
  4. **Resolution-limit disclosure missing from §7 (required by two independent briefs).** The "Known weakness" bullet (l.230-233) covers only the coverage floor. It must add, in advance, that a FAIL driven only by (ii)-width or IQR at ρ* is compatible with ideal order-only localisation, because the bound sits near one Poisson spacing. The Physicist and Mathematician estimate roughly a coin-flip pass probability, about 0.53-0.6, for an ideal classifier. These figures are `[UNVERIFIED]` and use no dev data. ASTRA's own risk statement is at astra.md:52. This is wording only and θ is unchanged. It is what stops a later re-derivation of θ, which would breach NO_THRESHOLD_LOOSENING.
  5. **C1→C2 procedure is not binding.** The frozen text must require the following. C1 is added as a NEW file with the draft kept; a `git mv` would register as a rename, `--diff-filter=A` would return nothing, and C2 would refuse. C1 to C3 are committed on `prereg004/step3-port` with no amend, rebase or squash, and merged only by fast-forward or merge commit. C1 is pushed and its full SHA recorded before C2 runs.
  6. **Smaller statements in l.202 and §7 that are literally false.**
     - "Every pass test is written as `x ≤ bound`" is false: `validate.py:248` uses `>=` and `:178` uses `<`. The NaN-never-passes semantics still hold.
     - "A one-element sample is NaN" is false for (iii): the std of one midpoint is 0.0, and ddof=0 is unstated.
     - (v) is enforced by abort and cannot evaluate False under the validation label; the draft should say so.
     - The IQR `loc_inconclusive` wording means "fails (ii)", not the INCONCLUSIVE verdict.
     - The `near_boundary_pairs_tol` count should be reported per seed.
  7. **Runnable-command gap.** The Makefile has no `test-004`, `dry-run-004` or `verify-seal-004` targets. I grepped and found none, and only `verify-2p1` exists. Comité 052 asked for them. The frozen text must name the exact substitute commands, and must say whether the full-grid dry run on `DRY_RUN_SEEDS` is part of the plan. No code writes `validation_004_provenance_launch.txt`, so the frozen text must give its content and the command-by-command procedure (UTC timestamps, lscpu, and a pip freeze diff against `requirements-lock.txt`).
  8. **Review coverage, for the PI to weigh (not a freeze-rule breach).** The fixes after the O8 Gemini review (4190a10) and the changes after audit 045 have been checked only by /auditor 045/046 for the technical delta. No second model family has reviewed the text after the edits in items 1-7. Those edits are wording-only, so the PI could accept a light check instead. Audit 046 itself says session independence is not certified.
  9. **What does not need to change.** T, the ρ grid, θ, K, the seeds, and the code (the fixes are wording only; Logician's optional (iii) NaN change is declined). No wave-1 brief found a criterion that cannot fail. Bit-reproducibility holds only for 20 threads on the measured host, and the result doc must say so (SWE R6). The 61 tests pass (dossier); the global suite was not rerun.
  - **Conditions to lift the BLOCK, for the PI:** make fixes 1-7 in the draft, which then becomes the non-draft text. Re-run `make verify-seal verify-2p1` and refresh the SHA table. Then the PI may decide C1. The committee does not authorise C1-C3.

## 7. Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| EGS (arXiv:2605.06813) derived-md l.173-181: event horizon = boundary of past of J+, needs an infinite sprinkling | physicist | CONFIRMED (l.173) |
| EGS l.181-191 and l.463: bimodal longest-chain split of minimal elements, inside vs outside the horizon | mathematician | CONFIRMED (the chain text starts at l.181 and "bimodal" is at l.191 and l.463; l.463 is the summary of the first diagnostic) |
| EGS l.193: future cardinality is also bimodal, but "may be affected more strongly by the choice of boundary" | mathematician, physicist | CONFIRMED. The l.188-193 range is fine. The paper's own example (a causal diamond) makes the cardinality vary between n and √n even in Minkowski, which supports the T-dependent effective boundary disclosure. |
| EGS l.195: the partition "would no longer work for regular black holes" (Hayward) | physicist | CONFIRMED. The paper says "likely does not allow a partition", in 3+1; it is hedged. |
| Surya LRR ("The causal set approach to quantum gravity", derived-md) l.409-410, Myrheim 1978: counts are legitimate, "Order + Number" | mathematician | CONFIRMED in substance, with a mislocated line. l.409-410 are the passage substituting continuum volume with cardinality, citing Myrheim 1978. The "Order + Number ∼ Lorentzian Geometry" formula (5) is at l.471. |
| Surya LRR l.1000-1010: ordering fraction and Myrheim–Meyer dimension | mathematician | CONFIRMED |
| Surya LRR l.1226: discrete geodesic distance = longest chain (Myrheim 1978) | mathematician | CONFIRMED |
| ASTRA `astra.md` l.3-5: induced metric h = (1+2M/r)dr² + r²dφ² on t*=0 | mathematician | CONFIRMED |
| ASTRA l.7-12: minimal-element surface density ∝ ρ^{(D-1)/D}, so ρ^{2/3} in 2+1D | mathematician | CONFIRMED |
| ASTRA l.33-41 (physicist writes l.35-40): c₃ = Γ(4/3)(3/π)^{1/3}; λ_r(r) = c₃ρ^{2/3}·2πr√(1+2M/r) | mathematician, physicist | CONFIRMED. The c₃ ≈ 0.88 value, ρ=126 → ℓ_rad ≈ 0.00905, and θ_loc/θ_stab ≈ 0.0362/0.0181 all check out. |
| ASTRA l.42: the O(1) factors between ℓ_rad and 1/λ_r are absorbed into K_LOC=2 | mathematician, physicist | CONFIRMED. The ASTRA formula "no es 1/λ_r(r)" is on that line. |
| ASTRA l.52: "riesgo de exigir demasiado", K=2 sets no coverage level, 1−3e⁻² ≈ 0.594 | mathematician, physicist | CONFIRMED. 1−3e⁻² = 0.594 is correct. |
| ASTRA l.30 (same 1+1 convention) → "bound/δ ≈ 2.5, per-seed pass ≈ 0.71" | physicist | UNCONFIRMED as cited. l.29-31 gives only the reduction ℓ_rad = ρ^{-2/3}/P_* and the 1+1 reduction to ρ^{-1/2}. The ratio 2.5 and the 0.71 are not in ASTRA. They are the physicist's own derivation, and the dossier marks this only as `[INFERENCE]`. |
| ASTRA l.46: width mean 2δ, midpoint std δ/√2 for an exponential-neighbour model | (not cited by an expert; used to check them) | CONFIRMED, and consistent with the Gamma(2,δ) model both experts use |
| E1 lemma `research_program/puente_3p1/2026-10-12/E1_equatorial_restriction_lemma.md` §3: x≺y ⟺ dist_φ ≤ min(π, sup L) on rectangular patches | mathematician | CONFIRMED (§3 l.81 onward) |
| E1 l.98 and l.172: the maximiser-existence step is marked `[INFERENCE, no formalizado aquí]` | physicist | CONFIRMED (both lines) |
| Comité 052 `docs/comite/comite_decision_052_prereg004-2p1-design.md` l.153: Lean has nothing on 2+1 | physicist, logician | CONFIRMED in substance (the Mathematical-logic brief says nothing in Lean mentions 2+1 or the equator). I only skimmed the line number. |

- **Notes**
  - **ASTRA derivation:** it exists at the stated worktree path. The line numbers cited by the mathematician and physicist are accurate except for the physicist's "l.30" for the 1+1 bound/δ ≈ 2.5 comparison. That figure, and the 0.71, have no anchor in ASTRA and should be treated as `[INFERENCE]`.
  - **Idealised-model arithmetic:** I checked the experts' numbers using only the ASTRA formulas.
    - δ ≈ 0.256ρ^{-2/3} ≈ 1.13 ℓ_rad.
    - Bound/δ ≈ 1.78.
    - Gamma(2) median = 1.678δ ≈ 0.94 × the bound.
    - IQR ≈ 1.73δ ≈ 0.97 × the bound.
    - P(single width ≤ bound) ≈ 0.53.
    - All of these are numerically correct. I did not check the mathematician's Φ(0.26) ≈ 0.6 median-of-20 figure.
    - The two experts do not agree on the conclusion. The mathematician says "coin flip" for the IQR and about 0.6 for the median. The physicist says about 0.53 per seed. Both agree that the (ii) clause is close to the edge and that this needs disclosing in advance.
  - **E1 lemma location:** it is not in the main checkout `/home/ignac/nachocausal/research_program/`. It exists only in the worktree, `/home/ignac/nachocausal/.worktrees/prereg004-step3/research_program/puente_3p1/2026-10-12/E1_equatorial_restriction_lemma.md`. The E1 text also cites "ASTRA, §6". That is E1's own audit, not the blind-anchor ASTRA `astra.md`. A reader could confuse the two.
  - **EGS limits:** EGS defines the diagnostics for 1+1 patches (Fig. 3) and for the 3+1 discussion. It does not treat 2+1 equatorial patches. The experts apply it by analogy, which the draft already discloses as A1-A4.
  - **Not checked:** I did not verify the repo-internal line anchors (`validate.py`, `seed_manifest.py`, `.gitignore`, the draft's line numbers). Those are not literature citations and are outside this role.
  - **Overall:** no citation is fabricated, and none supports a claim contrary to what the expert asserted. The two defects are one mislocated line (Surya "Order + Number" is at l.471, not l.409-410) and one unanchored figure (ASTRA l.30).

## 8. Synthesis
Recommended direction, ranked alternatives, and **open disagreements (never hidden)**. If a
pre-registration BLOCK or an unresolved falsification exists, the verdict cannot be a PROCEED
verdict.

**Recommended direction: do not freeze yet. First revise the text, then decide C1.**
- The warden **BLOCKs**, and the falsifier rates the draft NOT READY. Either one rules out a PROCEED verdict.
- All seven roles agree on two points:
  - the design (T, ρ grid, θ/K_LOC, seeds, criteria code) needs no change;
  - no criterion is unable to fail; no ground-truth leakage was found in the blind path; no over-claim was found.
- What blocks is the **text to be sealed**, plus the **C1→C3 procedure**.
- The chair's §2 checks confirm every blocker that can be checked mechanically.

**Required changes before C1 (converged; numbered for the sign-off):**
1. **Verdict precedence (Q1).** Replace §7 "≥ 3 BH abstentions is a FAIL of (i), never INCONCLUSIVE" with:
   - "BH abstentions never *cause* INCONCLUSIVE";
   - the precedence actually coded: OUT_OF_DOMAIN > ABORTED_GUARD_V / ABORTED_TAU_RANGE > INCONCLUSIVE > PASS/FAIL (`validate.py:226-233`).

   Commit in advance that, under INCONCLUSIVE, the result document reports the clause values computable from the recorded aggregates, labelled *non-verdict* (falsifier).
2. **Literally false sentences in §7:**
   - "every pass test is written as `x ≤ bound`": coverage uses `>=` and (i) uses `<`. The NaN semantics still hold.
   - "one-element sample ⇒ NaN": with one clean midpoint the std is 0.0, so (iii) can pass. State ddof = 0, and that (ii)-IQR fails in that case.
   - "else inconclusive ⇒ not passed" for the IQR clause: it should read "fails (ii)".
   - (v): state that it is a precondition enforced by abort, not a criterion that can be False under the validation label. Do not count it as a sixth "passed" criterion.
3. **Stale state.**
   - Refresh the §3 SHA table to the current values (`2bf954fb…`; `seed_manifest.py` `e4047104…`). Add the SHAs of the 2+1 code files.
   - Extend the §9 audit trail to cover 045 (AUDIT_FAIL, Codex) → 782d031 → 046 (AUDIT_PASS, Codex, session separation not certified). Correct the "same model family" sentence.
   - Close the "re-audit pending" lines in §10.
4. **Committing the result.** `results/` is git-ignored. §9 must fix the mechanism: `git add -f` of the result, the progress log, the provenance file and a run log (stdout and stderr), with their sha256 recorded in `docs/`. Otherwise the `PRIMARY_ARTIFACT_LOST` failure of prereg-002 repeats.
5. **C1→C2→C3 procedure, made binding in the text:**
   - C1 adds `docs/preregistration_004.md` as a **new file**, keeping the draft; never `git mv` (rename detection would defeat `--diff-filter=A`).
   - C1 is pushed, and its full SHA is recorded in a signed, pushed note **before** C2.
   - C1 to C3 stay on `prereg004/step3-port` with no amend, rebase or squash, and are merged only by fast-forward or by a merge commit.
6. **Runnable commands.**
   - Either add the `make` targets asked for by comité 052, or name the exact substitute commands.
   - Say whether a full-grid dry run on `DRY_RUN_SEEDS` happens after C1.
   - Write the provenance-launch procedure out command by command: UTC timestamps, `lscpu`, `pip freeze` diffed against `requirements-lock.txt`.
7. **Power disclosure for (ii), worded symmetrically.** Add to "Known weakness" a statement derived **from theory only** (ASTRA plus the Gamma(2, δ) neighbour model; no dev JSONL consulted). It says that even an ideal classifier passes (ii)-width/IQR at ρ\* only about half the time (bound ≈ 1.78 δ). These figures are `[UNVERIFIED]`, from the experts' arithmetic as checked by the literature verifier.
   - The wording must be the falsifier's, not the physicist's: a FAIL is reported as FAIL, and the low power is a property of the test. No result may be used to re-derive or loosen θ/K_LOC in any successor pre-registration.
   - The physicist's "1+1 ratio ≈ 2.5 / 0.71" is not anchored in ASTRA (literature verdict) and must not be cited as ASTRA's.
8. **Executable proof of item 1 (falsifier's minimal test).** Add to `tests/test_004_criteria_can_fail.py` the case "ρ = 32 short + ρ = 126 with 3 abstentions ⇒ INCONCLUSIVE, no `checks`" as a documented expectation. This is a test file, outside `SEALED_PATHS`. It changes no criterion.

**Optional (advisory, not blocking):**
- report `near_boundary_pairs_tol` per seed (mathematician);
- record the CPU model and state that bit-reproducibility holds only for 20 threads on this host (SWE R6);
- record UTC in the progress `start` line (SWE R7);
- keep the host awake during the run.

**Ranked alternatives:**
- **(A, recommended)** Make the wording and procedure changes 1-8, with no code change in `nachocausal2p1/`. Then do a short cross-family check of the final §7/§9 text against `validate.py` (`revision-ciega`, PI permission required). Then the PI decides C1.
- **(B)** Same as A, but without the cross-family check. The gap is declared in §9: the post-O8 semantics have been checked against code only by Codex audits 045/046 and this Claude committee.
- **(C, rejected by the warden)** Code changes such as making (iii) NaN when n_clean < 2. They reopen the audit chain (re-audit needed) and add nothing the wording does not already give.

**Open disagreements (not resolved here):**
- **Cross-family review before C1.**
  - The falsifier asks for one non-Claude pass on the final text.
  - The warden leaves it to the PI ("light check" acceptable, since the edits are wording-only).
  - Factual correction by the chair: the falsifier says 045 was Claude, but 045 and 046 were both **Codex** (§2). Their technical delta checks are therefore already cross-family.
  - What remains true is narrower. Neither Codex audit caught the Q1 text-versus-code contradiction. The last *content* review by a non-Claude model predates the D1/D2 sentences.
- **Wording of the power disclosure.**
  - The physicist proposes "a FAIL driven only by (ii) is not evidence that the order fails to localise".
  - The falsifier rejects that as an asymmetric pre-excuse of FAIL.
  - The chair recommends the falsifier's wording (item 7).
- **Power figures.**
  - The mathematician gives ≈ 0.6 for a median of 20 seeds, plus a coin-flip IQR.
  - The physicist gives ≈ 0.53 per seed.
  - These are different quantities; they do not contradict each other. Neither is a committed script, so both stay `[UNVERIFIED]` in the text.
- **Thread nondeterminism.**
  - The SWE treats it as an unprobed risk (R6).
  - The falsifier judges it unlikely on inspection (no cross-iteration reductions).
  - Both agree that it is unverified and must be declared.


## 9. Next-step spec
The sequenced plan, separating **reversible** steps (may be run now if the user asks) from
**committing** steps (only on explicit user authorisation), with the binding rules pre-committed
and the falsifier's minimal falsification test included:

**Reversible (may run now if the user asks; nothing touches the virgin band, the 1+1 seal or `nachocausal2p1/`):**
1. Edit `docs/preregistration_004_draft.md` with changes 1-7 of §8. Wording only; no θ, T, ρ, K, seed or code change.
2. Add the falsifier's minimal test (§8 item 8) to `tests/test_004_criteria_can_fail.py`:
   - synthetic levels with ρ = 32 short and ρ = 126 at `n_abstain_BH = 3`;
   - expect `INCONCLUSIVE` with no `checks`.

   Run the three 004 test files and the global suite, and report the counts.
3. Add the `make` targets, or substitute commands, for test, dry-run and seal (§8 item 6). The Makefile is outside `SEALED_PATHS`.
4. Re-run `make verify-seal verify-2p1` and refresh the SHA table.
5. Optional, with explicit PI permission because it sends text to a third party: `revision-ciega` with a non-Claude model on the final §7/§9 against `validate.py`. One round, closed by its evaluation. Alternative B: declare the gap in §9.
6. Commit and push the revised draft (PI authorisation for the commit), then run `/auditor` on that delta in a separate session.

**Committing (only on explicit user authorisation, after steps 1-6 are green):**
- **C1.**
  - Add `docs/preregistration_004.md` as a new file (the draft is kept), set `STATUS = "FROZEN"`, and include the fixture, all in one commit on `prereg004/step3-port`.
  - Before that commit: `make verify-seal` is unchanged, the tree is clean, and `make verify-comite` passes.
  - Push C1. Record its full SHA in a signed, pushed note. No amend, rebase or squash afterwards.
- **C2.**
  - `python -m nachocausal2p1.seed_manifest <full-C1-SHA>` on the pinned environment and a clean tree.
  - Commit and push only `docs/validation_004_seeds.json`.
- **C3.**
  - A single blind CPU run, `NUMBA_NUM_THREADS=20`, under `nohup`, with a run log. HEAD is the C2 commit.
  - Afterwards, `git add -f` the result, progress log, provenance file and run log, with their sha256 values in `docs/`.
  - The result is reported alike whatever it is. No rerun on fresh seeds. A no-output crash is relaunched on the same seeds; deterministic aborts are not relaunched.


## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_

**PI sign-off (2026-10-15, in chat, transcribed by Claude).** Signed with two wording adjustments
of the PI. Revised candidate identified: `0c16845` on `prereg004/step3-port`.
- **Verdict.** `RECOMMEND_REVISE_AND_RECONVENE` accepted.
- **Changes.** The eight changes of §8 were applied in `007947e`.
- **Open disagreements, resolved by the PI:**
  - (a) A cross-family review was run: Gemini on `007947e`
    (`revisiones/2026-10-15-prereg004-c053-gemini/`). Its code finding G8 (`--full-history`) was
    fixed in `76da124`, together with ten text fixes.
  - (b) The power disclosure uses the falsifier's wording.
  - (c) The power figures stay `[UNVERIFIED]` (closed-form arithmetic); the PI expressly accepts
    this limitation.
  - (d) Thread determinism is declared, not probed; the PI expressly accepts this limitation.
- **Full-grid dry run.** The post-C1 full-grid dry run on `DRY_RUN_SEEDS` is dropped (`616c55d`).
- **Audit.** The delta audit was assigned by the PI to Gemini instead of a Claude `/auditor`,
  without command execution:
  - `782d031..616c55d`: `AUDIT_PASS_WITH_WARNINGS`. W1 was fixed in the text. W2 was fixed in
    `validate.py` comments and docstring only; no executable code changed; the AST is equal after
    excluding docstrings.
  - `6f76d21..e6b5bfe`: `AUDIT_PASS`.
- **Reconvening.** Having considered the Gemini review and both delta audits, including their
  stated limitations and lack of command execution, the PI explicitly waives the reconvening
  recommended by comité 053. No further comité is required before the separate C1 decision. This
  is a PI procedural decision, not a new committee verdict or independent verification of command
  execution.
- **C1-C3.** This sign-off does not authorise C1, C2 or C3. C1 needs its own explicit PI decision
  and must follow the §9 C1 procedure of the draft.
