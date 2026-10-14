# Pre-registration 004 — DRAFT (2+1D equatorial patch localisation)

> ## ⚠ DRAFT — NOT FROZEN, NOT YET A PRE-REGISTRATION
>
> This file is the reversible draft of what `docs/preregistration_004.md` *would* register. It
> freezes nothing, seals nothing, draws no seed and touches **no** seed of the virgin band
> `8_000_000..8_999_999`. It is the input to step 7 of
> `docs/comite/comite_decision_052_prereg004-2p1-design.md` §9 ("reconvene `/comite` on the
> concrete prereg-004 draft"). Freezing is a separate committing step (C1, §9 below) that needs
> steps 1-7 green and explicit PI authorisation; only then is the non-draft
> `docs/preregistration_004.md` created and `nachocausal2p1/thresholds.py` set to `FROZEN`.
>
> Sealed 1+1 instrument unchanged: `nachocausal/thresholds.py` SHA256 =
> `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (`make verify-seal`).
> Draft written 2026-10-13 on branch `prereg004/step3-port`, base commit `2fe277f`.
>
> Every value below is a pointer to a committed artefact. Items still open are listed in §10 and
> must be settled (or explicitly accepted as open) by the committee and the PI before C1.

## 1. Claim to be registered (and its boundary)

**Claim form.** On the frozen 2+1 equatorial Schwarzschild bench (§2), an embedding-blind
estimator that sees only the causal order and its cardinalities (§4) places a bracket on the
minimal-element antichain that, at the primary density, has median width ≤ θ_loc·2M, covers
r = 2M in at least half of the bracket-valid seeds, is stable across seeds within θ_stab, and is
significant against the same-cloud flat control — all on 20 seeds drawn once and blind (§6).

Allowed wording of any result: **"finite 2+1 equatorial patch localisation within frozen θ on
the frozen ρ grid"** (comité 052 §8 item 10, §5 "Premature / over-broad claims").

**Not claimed** (comité 052 §6 "Forbidden moves", acta `docs/acta_frente_2p1_ecuatorial_2026-10-12.md:107`
`no_3p1_claim_from_2p1, no_einstein_2p1_claim, gpu_dev_only`):
- no event-horizon claim: the target is the coordinate locus r = 2M in a finite box, and the
  estimator is known to track a T-dependent effective boundary at small T
  (`dev/2P1_PHASE_B_INTERIM_2026-10-12.md`);
- no 3+1 result: lemma E1 transfers the *order* on the equator only, not any estimator property;
- no 2+1 gravity result: the bench metric is not an Einstein solution in 2+1;
- no metric reconstruction; no statement about regular black holes (EGS l.195, comité 052 §7);
- no "for all ρ": every statement is for the frozen grid {32, 63, 126} only.

**Assumptions stated, not proved** (comité 052 §6 "E1 and order definition"):
- A1. The poset is the **ambient** causal order of the equatorial Schwarzschild patch restricted
  to the sprinkled points, not the intrinsic order of the EF box.
- A2. Lemma E1's computable `Delta_max` criterion relies on a maximiser step self-marked
  `[INFERENCE]` (`research_program/puente_3p1/2026-10-12/E1_equatorial_restriction_lemma.md` §3).
- A3. Its application to the EF box (r ≥ 0.1 on every causal rectangle of two box points) is the
  committee physicist's own inference, not written in E1.
- A4. The order is decided numerically by geodesic shooting with frozen tolerances (§3); it is
  checked empirically per seed (audit, transitivity, radial closed form), not analytically.

## 2. Bench (geometry, sprinkling, control)

| Item | Value | Source |
|---|---|---|
| Metric | ingoing EF, equatorial: `-(1-2M/r)dv² + 2dv dr + r²dφ²`, `v = t* + r` | comité 052 physicist brief; `nachocausal2p1/generator.py` |
| 2M | 0.5 (scoring unit only) | `nachocausal2p1/thresholds.py` `TWO_M` |
| Box | `t* ∈ [0, T]`, `r ∈ [0.1, 1.3]`, `φ ∈ S¹` (r-range = sealed 1+1, never varied) | `thresholds.py` `R_LO, R_HI` |
| T | **16.0**, hard-coded literal, no environment knob | `thresholds.py` `T_EDGE`; PI decision, comité 052 §11 |
| Volume | `π(1.3² − 0.1²)·T = 5.278·T` (√−g = r) | `thresholds.py` `VOL_PER_T, BOX_VOLUME` |
| Sprinkling | Poisson, mean `n_mean(ρ) = round(ρ·BOX_VOLUME)` | `thresholds.py` `n_mean` |
| Flat control | Minkowski order (`dt ≥ |x−y|`) on the **same** cloud | comité 052 physicist brief |

**T = 16 is a margin above t_min, not a Decision-2 pass.** Measured dev t_min = 8 / 10 / 10 at
ρ = 32 / 63 / 126 (`dev/2P1_TMIN_SWEEP_RESULT_2026-10-12.md`,
`dev/2P1_TMIN_RHO126_RESULT_2026-10-13.md`). The plateau clause [T, 2T] is unmeasured at T = 16
([16, 32]). No decay law for the finite-T bias enters this pre-registration (comité 052 §8 item 5;
literature verdict §7: the e^{−T/4M} argument is unanchored). T was chosen using dev bias and
coverage scored against r = 2M: **T is not chosen ground-truth-free** (comité 052 logic brief).

## 3. Instrument

Sub-package `nachocausal2p1/` (step 3, `dev/PREREG004_STEP_3_2026-10-13.md`); `nachocausal/` is
not edited.

- **Generator** `nachocausal2p1/generator.py`: numerical core copied literally from
  `dev/gen2p1_efbox.py`; T literal; numba cache off. Frozen numerics (`thresholds.py`):
  `TOL = 1e-6`, `REL_MARGIN = 1e-3`, `COARSE = (128, 512)`, `FINE = (2048, 8192)`,
  `COARSE_MARGIN = 0.05`, `N_HYP = 48`, `AUDIT_PAIRS = 20000`.
- **Per-seed validity** (any failure ⇒ seed **INVALID**, never replaced): generator assertion;
  any endpoint failure or disagreement in the 20 000-pair re-shoot audit (stage-1/2 and coarse
  shot vs fine); a transitivity violation; a radial-check mismatch vs the closed form
  `nachocausal.generator.past_matrix_fast`.
- **Estimator** `nachocausal2p1/estimator.py`: thin wrapper over the sealed 1+1 primitives
  (`estimate_O_volume`, `two_means_split`, `improvement`, `verify_order_only`), unchanged.
- **Gate** `nachocausal2p1/gate.py`: τ(n) from `nachocausal2p1/fixtures/tau_table_2p1.json`
  (§5); `n > 256` **aborts the run** (never extrapolates).
- **Scoring** `nachocausal2p1/scoring/`: the only place r is read, after the threshold is fixed
  from O.
- **Runner** `nachocausal2p1/validate.py`: Guard-v → estimate → gate → bracket; atomic write;
  the label `validation_004` is one-shot and refused unless `STATUS == "FROZEN"`, the seeds are
  the drawn ones, `guard=True`, and `results/validation_004.json` does not exist.
- **Environment** (`thresholds.assert_environment`, hard-fail): Python 3.12.3, numpy 1.26.4,
  numba 0.66.0, llvmlite 0.48.0, scipy 1.17.1; CPU only (CuPy not loaded, `NC2P1_DEVICE` unset
  or `cpu`).

**SHAs at drafting time** (to be re-taken and recorded at C1; `make verify-2p1`, `sha256sum`):

| File | SHA256 |
|---|---|
| `nachocausal2p1/thresholds.py` (candidate) | `e7a69934dff0219f4d3560e1f892eeb9ecf8accb5fa72996e1e0cf73f7e326eb` |
| `nachocausal2p1/fixtures/tau_table_2p1.json` | `4bc4aec839257af7fed210030c0afa9041c265cacf43802bb735fb99df367a28` |
| `nachocausal/thresholds.py` (1+1 seal) | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` |
| `nachocausal/estimator.py` (imported) | `aa4411c3d095230e0f6dde78e4a8de11240c0cb42ad14353453848d70cdf1680` |
| `nachocausal/generator.py` (imported, radial check) | `d6f09fdc21b76f6cf329c33580342a068135f7ece7ed11c304552f0848216f9f` |
| `nachocausal/__init__.py` (imported) | `f1ec7306ced3e1f948b3a147b4e8c69f201c2bb803a1cb2525b5602239a2c7b7` |

The thresholds SHA will change at C1 (`STATUS`, `VALIDATION_DRAW_SEED`, `VALIDATION_SEEDS`).

## 4. Observable and estimator

- **Observable:** for each minimal element i of the order, `O(i) = |future(i)|` (future
  cardinality). Counting is legitimate (`Order + Number`); the estimator sees only the order.
- **Split:** sealed 1-D 2-means on O; `improvement` is the split's variance reduction.
- **Gate:** abstain (`sep → 0`, no boundary claimed) iff `improvement < τ(n)`, n = number of
  minimal elements.
- **Bracket (scoring only):** `[max r over low-O minimals, min r over high-O minimals]`;
  `covers` iff `r_lo ≤ 2M ≤ r_hi`; `clean` iff width ≥ 0; point estimate = midpoint.
- **Guard-v:** `verify_order_only` on every causet; it raises on failure (aborting the run).

## 5. Gate table τ(n) (step 1)

Generated by `dev/gen_tau_table_2p1.py` with the **sealed** procedure unchanged
(`scripts/gen_tau_table.build_tau`: one stream `default_rng(20260621)`, n ascending and
contiguous from 2, 40 000 reps, α = 0.01 → p99, uniform null) up to `n_max = 256`. Bit-equal to
`nachocausal/fixtures/tau_table.json` for n ≤ 128 (asserted). Largest dev `n_minimal` = 184
(ρ = 126). Re-gating all 360 dev decisions with it flips none; minimum margin 0.0358
(`dev/regate_2p1_sweeps.py`; `dev/PREREG004_STEPS_1_2_2026-10-13.md`). Dev τ values are not
reused.

## 6. Seeds — to be drawn once, blind, at C2 (not drawn)

- **Ensemble:** `ENSEMBLE = 20` per ρ level (the same 20 seeds at every ρ);
  `MIN_VALID_SEEDS = 18` generator-valid seeds per level.
- **Recipe** (mirrors `docs/preregistration_002.md:20-24`):
  `numpy(1.26.4).default_rng(VALIDATION_DRAW_SEED_004).choice(arange(8_000_000, 9_000_000), size=20, replace=False) -> sorted`.
- **`VALIDATION_DRAW_SEED_004 = 20261014`** (`nachocausal2p1/thresholds.py`, name
  `VALIDATION_DRAW_SEED`), fixed by the PI on 2026-10-14 before any draw (O1, §10). Like
  prereg-002's `20260622`, it is the date of the decision.
- **Runnable guard** (`thresholds.check_validation_seeds`, at import): exactly 20 distinct seeds,
  all in `VIRGIN_BAND`, none in `EXPLORE_BAND = 7_000_000..7_000_999`, none among the burned
  Phase-A seeds `1, 2, 3, 4, 7, 99, 12345`. `validate.check_seed` refuses any virgin seed before
  `STATUS == "FROZEN"`.
- Burned and never reusable: the whole exploration band, the Phase-A seeds, and the prereg-001
  and prereg-002 seeds. Dry runs use only `DRY_RUN_SEEDS = 7_000_100..7_000_109`.

## 7. Frozen analysis

Grid `RHO_GRID = (32, 63, 126)`, **primary endpoint ρ\* = 126** (comité 052 §8 item 4). Every
threshold is a function of (ρ, T, box geometry) only, never of realised N or n_min.

**θ anchor (c1), derived blind** (`revisiones/2026-10-13-anclaje-theta-ciego/astra.md`, commit
`bab6fef`): radial order-statistic spacing of the minimal-element layer, evaluated at the mean box
perimeter `P* = π(R_LO + R_HI) = 1.4π` (box ends only, no ground truth); K_LOC = 2 inherited
unchanged.

```text
ell_rad(ρ)    = ρ^(-2/3) / (1.4π)
theta_loc(ρ)  = K_LOC·ell_rad/(2M)
theta_stab(ρ) = K_LOC·ell_rad
slack(ρ)      = ell_rad/(2M)            (convergence clause F)

ρ       theta_loc   theta_stab
32      0.09023     0.04511
63      0.05744     0.02872
126     0.03619     0.01809
```

**Disclosure (required by comité 052 §6):** the anchor was commissioned when the chair already
knew the dev bracket widths; the deriver (ASTRA) did not see them. The conservative alternative
(c2), the dimensional transfer `2ρ^{-1/3}/2M` with an explicit "(ii) and (iii) are weak in 2+1"
note, was recorded and not chosen (PI decision, comité 052 §11). These θ have **not** been
compared with dev widths and will not be before the freeze. A low-ρ cell failing under this anchor
is reported as a FAIL, not repaired.

**Criteria** (`nachocausal2p1/validate.py` `summarise_level`, `verdict_from_levels`). The run is
**PASS iff all six hold**; otherwise FAIL, except for the two statuses below.

| Check | Definition |
|---|---|
| (i) significance | at every ρ ≥ 63: sign-flip `p_perm ≤ 1e-4` on `d = sep_BH − sep_MINK` over generator-valid seeds (exact for n ≤ 20; a BH abstention enters with sep = 0), **and** BH abstentions < 3 at that level |
| (ii) localisation | at ρ\*: median clean width/2M ≤ θ_loc(ρ\*), **and** IQR of widths/2M ≤ θ_loc (else inconclusive ⇒ not passed), **and** coverage ≥ 0.5 over bracket-valid seeds |
| (ii) convergence F | for consecutive grid levels: `m(ρ_{k+1}) ≤ m(ρ_k) + slack(ρ_k)`, m = median width/2M; any unscored level fails it |
| (iii) stability | at ρ\*: std of clean bracket midpoints ≤ θ_stab(ρ\*) |
| (iv) flat escapes | at ρ\*: flat-control non-abstentions ≤ 1 of the generator-valid seeds |
| (v) order-only | Guard-v ran on every causet (`guard=True`) |

- **INCONCLUSIVE** iff the primary level has < 18 generator-valid seeds. It is reserved for
  generator-invalid seeds; ≥ 3 BH abstentions is a **FAIL** of (i), never INCONCLUSIVE (PI
  decision, comité 052 §11).
- **OUT_OF_DOMAIN** iff `T < T_EDGE_MIN = 10`. At the frozen T = 16 this gate cannot fire and is
  **not** counted as a safeguard (comité 052 §5 "Verdict coercion").
- **(i) and (iv) are gate-derived.** With the flat control abstaining, (i) reduces to "no BH
  seed abstained" and (iv) to "≤ 1 flat seed escaped the gate". Neither is independent
  confirmation; the discriminating content is (ii), (iii) and coverage (comité 052 §8 item 7).
- **Reported verbatim and separately, whatever the verdict:** per level, generator-invalid count
  and reasons, BH-abstain count, flat-escape count, bracket-valid and clean counts, coverage count
  (not only the fraction), median and IQR width/2M, midpoint std, p_perm.
- **Known weakness, stated in advance** (comité 052 §5 item 5; ASTRA risks): a narrow, reproducible
  but mislocated bracket can pass (ii)-width and (iii); only coverage catches it, and with floor
  0.5 up to 9 of 20 non-covering seeds still PASS. The coverage floor 0.5 is a deliberately weak
  floor, not nominal coverage, and is neither raised nor lowered.

**Can-fail evidence (step 4):** `tests/test_004_criteria_can_fail.py` (9 tests) shows (ii) via
coverage, (ii) via width, (iv) and (v) can each produce FAIL; `dev/mutation_check_004.py` catches
5/5 mutations (`dev/PREREG004_STEP_4_2026-10-13.md`).

## 8. Pre-flight (step 5) and expected runtime

`dev/PREREG004_STEP_5_2026-10-13.md`, script `dev/preflight_2p1.py` (commit `5902843`):

- **CPU/GPU parity, seed `7_000_100`, ρ = 126, T = 16** (20 numba threads): all 15 compared
  fields match the GPU dev record (`dev/preflight_2p1_2026-10-13.jsonl`, sha256 `6838b4ac…`,
  commit `2fe277f`). Valid seed; audit 0/0/0/0; radial 0; transitivity 0. **Seeds
  `7_000_101..7_000_109` not run:** the PI accepted the partial parity on 2026-10-14 (O2, §10).
- **Thread determinism** (`NUMBA_NUM_THREADS=1` vs default): **not run** (O2). In its place the
  blind run is fixed to 20 numba threads, the only measured configuration, and
  `thresholds.assert_blind_threads()` aborts the validation run otherwise (O3, §10).
- **Measured CPU time, ρ = 126:** 591.9 s per seed (588.7 s generation with checks, 3.2 s
  estimation), 20 numba threads, i7-13700 under WSL2 (10 cores / 20 threads visible).
- **Expected runtime of the blind run** `[UNVERIFIED — extrapolated, not measured]`: ρ = 32 and 63
  are scaled from the measured ρ = 126 CPU time in proportion to the GPU dev means at T = 16
  (15.5 s, 51.1 s, 194.6 s at ρ = 32/63/126, `gen_seconds` in the v2 sweep JSONLs): ≈ 47 s + 155 s + 592 s ≈ 13 min per seed, **≈ 4.4 h for
  20 seeds × 3 levels at 20 threads**. At 4 threads it is unmeasured; attempt 1 did not finish one
  ρ = 126 seed in 22.5 min, so ≥ 7.5 h for the primary level alone.
- **This duration is stated so that it can never justify changing the grid or the seeds after
  launch.**

## 9. Binding rules and sequence

- **One-way:** the single blind `python -m nachocausal2p1.validate` on the drawn seeds, with
  `guard=True`, is the only evaluation. It has not been run. It is launched once, as an explicit
  step, only after explicit PI authorisation.
- **Report alike:** PASS, FAIL, INCONCLUSIVE or OUT_OF_DOMAIN is recorded and reported regardless
  of which it is. No post-hoc tuning, no re-running on fresh seeds after a result, no loosening of
  a frozen threshold. An unmet principled threshold is informative, never a licence to retune
  (`docs/preregistration.md:55-57`).
- **Invalid seeds** (§3) count toward the < 18/20 INCONCLUSIVE rule and never trigger
  replacement seeds.
- **Crash rule:** a crash is relaunched on the **same** seeds, environment and commit, **only if
  no scoring output was produced**, and the relaunch is logged with timestamps. The progress log
  below records each launch (a `start` line with its time) and carries no scoring field.
- **Writing:** `results/validation_004.json` is written atomically and committed immediately with
  its SHA (lesson of prereg-002 `PRIMARY_ARTIFACT_LOST`, `docs/preregistration_002_result.md`).
- **Progress log** (O4, §10): `results/validation_004.progress.jsonl`, one fsynced line per seed
  and level with only `seed, rho, invalid, abstained_BH, abstained_MINK, seconds`
  (`validate.PROGRESS_FIELDS`), appended as the run goes. It is committed together with the
  result, or alone after a crash.
- **Provenance launch file** `results/validation_004_provenance_launch.txt` records: start/end
  UTC; HEAD SHA and branch; both thresholds SHAs, the τ fixture SHA and the imported 1+1 module
  SHAs (§3); `git diff <seal> -- nachocausal/ nachocausal2p1/ docs/preregistration_004.md` line
  count (must be 0); `git status --porcelain` (must be empty); `uname -a`, `python -V`, full
  `pip freeze`; `NUMBA_NUM_THREADS`, OMP/MKL thread env, numba cache setting; `T_EDGE` as read by
  the generator at runtime; the 20 seeds and draw recipe; test pass count.
- **Sequence:** comité 052 §9 steps 1-6 (done, §5-§8 above; step 5 partial) → **step 7: `/comite`
  on this draft** → C1 freeze (`docs/preregistration_004.md` + `STATUS = "FROZEN"` + fixture,
  SHAs recorded, `make verify-seal` unchanged, tree clean, `make verify-comite` passing) → C2 blind
  draw → C3 single blind CPU run.

**Audit trail:** `/auditor` on the candidate package: report 043 `AUDIT_FAIL` → fixes `c16fb12`
→ report 044 `AUDIT_PASS` (`docs/auditor/auditor_report_044_prereg004-2p1-remediation-reaudit.md`).
The auditor is the same model family that wrote the code and is **not** an independent review
(global rule 5). The 1+1 precedent is PASS with caveats `PRIMARY_ARTIFACT_LOST;
TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY` (`docs/preregistration_002_result.md:1`).

## 10. Open items O1-O8: resolution (2026-10-14)

The PI settled the eight items on 2026-10-14, in a Claude Code session, one by one; Claude
transcribed the decisions. The same decisions are recorded in comité 052 §11.

| item | decision | where |
|---|---|---|
| O1 draw seed | `VALIDATION_DRAW_SEED_004 = 20261014` | `thresholds.py`, §6 |
| O2 step 5 partial | **accepted as partial**: parity on 1 of 10 seeds plus the dev pairwise parity at T = 16 and port = dev bit-equality; the 9 remaining seeds and the thread probe are not run | §8 |
| O3 thread count | **20**, enforced in code: `thresholds.assert_blind_threads()` (environment `NUMBA_NUM_THREADS=20` and `numba.get_num_threads() == 20`), called by `validate.run` under the validation label before any generation | `thresholds.py`, `validate.py`; tests `test_blind_threads_can_fail`, `test_validation_run_checks_threads_before_generation` |
| O4 progress log | **added before C1**: `results/<label>.progress.jsonl`, blind fields only | `validate.py`; tests `test_progress_line_is_blind`, `test_progress_log_written_per_seed_before_the_verdict` |
| O5.1 | confirmed: ≥ 3 BH abstentions FAIL (i) at every required ρ (63 and 126) | `validate.py` `summarise_level`, `verdict_from_levels` |
| O5.2 | confirmed: `p_perm` over generator-valid seeds, an abstained BH enters with `sep = 0`. **Deviation from 1+1**, where such a seed is excluded from `p_perm` and from the valid count (`nachocausal/validate.py:117`); the 2+1 rule is the more conservative one | `estimator.py:42-43`, `validate.py` |
| O5.3 | confirmed: coverage over bracket-valid seeds, count reported (as 1+1, `nachocausal/validate.py:142`) | `validate.py` |
| O5.4 | confirmed: 20 000-pair fine-shot audit; any failure or disagreement invalidates the seed | `validate.py` `generate` |
| O6.1-O6.4 | accepted: 10-seed dev cells with the test-only `MIN_VALID_SEEDS` bypass; (i) also failing in (a) and (c), with the synthetic (ii)-only case; no domain-gate bypass needed (pure functions); (iv) named `iv_flat_escapes_primary`, measured at the primary | `tests/test_004_criteria_can_fail.py` |
| O7 | signed: ρ grid {32, 63, 126} with primary 126; 20 seeds / 18 valid; coverage floor 0.5; (iv) ≤ 1 escape; `T_EDGE_MIN = 10`; exact pins; CPU-only path; and the two `[PI-S3]` clauses (slack F, significance at every ρ ≥ 63) | `thresholds.py` |
| O8 independent review | **authorised**: `revision-ciega gemini` on this draft and the 2+1 package, after the O3/O4 delta is committed. **Pending** | `revisiones/` (to be prepared) |

**Consequences still open before C1:**

- O3 and O4 change `nachocausal2p1/validate.py` and `thresholds.py` after auditor report 044. The
  delta needs a `/auditor` re-audit in a separate session (PI audit protocol: freeze and push
  first, then the auditor reads only the delta).
- O8: the blind review has to run and be evaluated.
- Step 7: reconvene `/comite` on this draft, and the PI signs the comité 052 verdict.
