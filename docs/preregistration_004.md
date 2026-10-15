# Pre-registration 004 — 2+1D equatorial patch localisation (FROZEN)

> **Frozen at C1**: the unique commit that introduces this file on branch `prereg004/step3-port`
> (`seed_manifest._check_freeze`). C1 seals this document and the instrument `nachocausal2p1/`
> (SHAs in §3), including the draw recipe (§6). Any change to them after C1 is a new
> pre-registration.
>
> - Authorisation: comités 052 and 053 signed by the PI on 2026-10-15 on candidate `0c16845`
>   (commit `94cd3b4`); C1 authorised by the PI on 2026-10-15, in chat.
> - Source: this text is `docs/preregistration_004_draft.md` at `0c16845`, with only the edits
>   needed to freeze it: this header; §3 SHAs of the frozen files; in §9, the sentences that called
>   this file a draft; in §10, the W2 wording requested by the PI at signature and the status. The
>   draft is kept unchanged as history.
> - No seed has been drawn at C1. C2 (blind draw) and C3 (single blind CPU run) each need a separate
>   explicit PI authorisation (§9).
> - Sealed 1+1 instrument unchanged: `nachocausal/thresholds.py` SHA256 =
>   `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (`make verify-seal`).
> - Every value below is a pointer to a committed artefact.

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
  those of the committed C2 manifest, `guard=True`, and `results/validation_004.json` does not exist.
- **Environment** (`thresholds.assert_environment`, hard-fail): Python 3.12.3, numpy 1.26.4,
  numba 0.66.0, llvmlite 0.48.0, scipy 1.17.1; CPU only (CuPy not loaded, `NC2P1_DEVICE` unset
  or `cpu`).

**Sealed SHAs at C1** (`make verify-seal-004`, 2026-10-15):

| File | SHA256 |
|---|---|
| `nachocausal2p1/thresholds.py` (`STATUS = "FROZEN"`) | `72c06b4d2dd909621f313f74a0c7256a18e7bbf2dce7e8147266a59302b12f38` |
| `nachocausal2p1/fixtures/tau_table_2p1.json` | `4bc4aec839257af7fed210030c0afa9041c265cacf43802bb735fb99df367a28` |
| `nachocausal2p1/__init__.py` | `178c182d94ce8e70c6edf6eab0ca15cb328d9f91e6771fc06733a5a3fcb3616f` |
| `nachocausal2p1/dry_run.py` | `eb98e3339b9f208a6e4af8e40c6a4b139806accc7cc9762bea52039701211995` |
| `nachocausal2p1/estimator.py` | `3a5010c403dd5083fcc2c4256c6e235ca092546d1e86dc83e3a980ecb4424ec4` |
| `nachocausal2p1/gate.py` | `b688535636be2ac3a585fd34b5a2ed97481886452fac1be92de619f49124629c` |
| `nachocausal2p1/generator.py` | `5324a924f7ef923984841199249e9a571626004efbdf85ca6dcd006c97e88b55` |
| `nachocausal2p1/seed_manifest.py` | `299b4cc2ae02ee557e88d2210fc0ae658a6e24eb904ac73d09df555ac7d87255` |
| `nachocausal2p1/validate.py` | `1dc539b6cd6d0b8711b80ca1a4da3abc79308807f7e1416a47ba5e136177749f` |
| `nachocausal2p1/scoring/__init__.py` | `641c78ef485d75a2f175adda2de8623cd6b1b5ecd91255dfafacf81897cf0039` |
| `nachocausal2p1/scoring/scorer.py` | `b9097beb20a3c7e3457f756a5d2cb469172ff9022fbf4bef83febd754265d144` |
| `nachocausal/thresholds.py` (1+1 seal) | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` |
| `nachocausal/estimator.py` (imported) | `aa4411c3d095230e0f6dde78e4a8de11240c0cb42ad14353453848d70cdf1680` |
| `nachocausal/generator.py` (imported, radial check) | `d6f09fdc21b76f6cf329c33580342a068135f7ece7ed11c304552f0848216f9f` |
| `nachocausal/__init__.py` (imported) | `f1ec7306ced3e1f948b3a147b4e8c69f201c2bb803a1cb2525b5602239a2c7b7` |

At C1 only `nachocausal2p1/thresholds.py` (`STATUS = "FROZEN"` and its docstring) and the
docstring of `nachocausal2p1/__init__.py` changed with respect to the signed candidate `0c16845`;
their SHAs above are the frozen ones. Nothing changes at C2: the draw is recorded separately in
`docs/validation_004_seeds.json`. C1 also seals `nachocausal2p1/seed_manifest.py`, the permanent
producer and reader of that manifest.

## 4. Observable and estimator

- **Observable:** for each minimal element i of the order, `O(i) = |future(i)|` (future
  cardinality). Counting is legitimate (`Order + Number`); the estimator sees only the order.
- **Split:** sealed 1-D 2-means on O; `improvement` is the split's variance reduction.
- **Gate:** abstain (`sep → 0`, no boundary claimed) iff `improvement < τ(n)`, n = number of
  minimal elements.
- **Bracket (scoring only):** `[max r over low-O minimals, min r over high-O minimals]`;
  `covers` iff `r_lo ≤ 2M ≤ r_hi`; `clean` iff width ≥ 0; point estimate = midpoint.
  A seed is **bracket-valid** iff it is generator-valid, the BH did not abstain, and both
  classes of the split are non-empty (`scoring.scorer.blind_bracket`, `validate.per_seed`).
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
- **`VALIDATION_DRAW_SEED_004 = draw_seed_from_commit(SHA of the C1 freeze commit)`**: the first
  8 hex digits of the full SHA of the C1 commit, as an integer (`nachocausal2p1/thresholds.py`,
  `draw_seed_from_commit`). The frozen text fixes the rule, not a number. This gives a
  reproducible derivation from the identified C1 commit; it does not guarantee unpredictability
  to its author, who can compute the hash of a candidate commit before publishing it.
  C2 records the full C1 SHA, the draw seed and the sorted 20 seeds in the separate manifest
  `docs/validation_004_seeds.json`, never by editing the instrument sealed at C1.
  (PI, 2026-10-14: O1 first fixed `20261014`, then
  revised after the O8 review, D5.)
- **Runnable guard** (`seed_manifest.load_manifest`, via `thresholds.validation_seeds`):
  the manifest must equal its committed HEAD version, name the unique commit introducing
  `docs/preregistration_004.md`, and match the unchanged C1 instrument and exact draw recipe.
  `thresholds.check_validation_seeds` requires exactly 20 distinct seeds,
  all in `VIRGIN_BAND`, none in `EXPLORE_BAND = 7_000_000..7_000_999`, none among the burned
  Phase-A seeds `1, 2, 3, 4, 7, 99, 12345`. `validate.check_seed` refuses any virgin seed before
  `STATUS == "FROZEN"` and a verified, committed C2 manifest. Nothing is drawn at import.
- Burned and never reusable **as validation seeds**: the whole exploration band, the Phase-A
  seeds, and the prereg-001 and prereg-002 seeds. `check_seed` still admits the exploration band
  after the freeze, for dry runs and tests; the validation run admits only the 20 seeds of the C2
  manifest (`validate.run`). Dry runs use only `DRY_RUN_SEEDS = 7_000_100..7_000_109`.

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
**PASS iff (i)-(iv) hold**, with (v) as a precondition (below); otherwise FAIL, except for the
statuses listed under "Verdict precedence".

| Check | Definition |
|---|---|
| (i) significance | at every ρ ≥ 63: sign-flip `p_perm ≤ 1e-4` on `d = sep_BH − sep_MINK` over generator-valid seeds (exact for n ≤ 20; a BH abstention enters with sep = 0), **and** BH abstentions < 3 at that level |
| (ii) localisation | at ρ\*: median clean width/2M ≤ θ_loc(ρ\*), **and** IQR of clean widths/2M ≤ θ_loc (a larger or NaN IQR fails (ii); the code field `loc_inconclusive` means this FAIL, not the run verdict INCONCLUSIVE), **and** coverage ≥ 0.5 over bracket-valid seeds |
| (ii) convergence F | for consecutive grid levels: `m(ρ_{k+1}) ≤ m(ρ_k) + slack(ρ_k)`, m = median clean width/2M; a NaN median (no clean bracket at a level) fails it |
| (iii) stability | at ρ\*: population std (ddof = 0) of clean bracket midpoints ≤ θ_stab(ρ\*) |
| (iv) flat escapes | at ρ\*: flat-control non-abstentions ≤ 1 of the generator-valid seeds |
| (v) order-only | precondition, not a criterion that can be false in the validation run: the validation label refuses `guard=False` and a Guard-v failure raises (`ABORTED_GUARD_V`, §9). It is not counted as a passed criterion |

- **Verdict precedence** (as coded, `validate.py` `run` and `verdict_from_levels`):
  `OUT_OF_DOMAIN` > `ABORTED_GUARD_V` / `ABORTED_TAU_RANGE` (§9) > `INCONCLUSIVE` > `PASS`/`FAIL`.
  - **OUT_OF_DOMAIN** iff `T < T_EDGE_MIN = 10`. At the frozen T = 16 this gate cannot fire and
    is **not** counted as a safeguard (comité 052 §5 "Verdict coercion").
  - **INCONCLUSIVE** iff **any** level of the grid has < 18 generator-valid seeds (PI decision of
    2026-10-14 after the O8 review, D2; before, only the primary level counted and a short
    secondary level gave FAIL). It is evaluated **before** (i)-(iv), and the verdict then carries
    no per-clause `checks`; so it takes precedence over any FAIL, including a FAIL of (i) at
    ρ = 126 when ρ = 32 is short (`tests/test_004_criteria_can_fail.py`
    `test_inconclusive_takes_precedence_over_a_fail_of_i`).
  - **BH abstentions never cause INCONCLUSIVE**: when every level has ≥ 18 generator-valid seeds,
    ≥ 3 BH abstentions at a required level is a **FAIL** of (i) (PI decision, comité 052 §11).
  - **Under INCONCLUSIVE**, the result document also reports, from the recorded level
    aggregates, the value each clause (i)-(iv) would have taken, labelled **non-verdict**, so that
    a failure masked by INCONCLUSIVE is visible. These values never turn INCONCLUSIVE into a PASS
    or a FAIL (comité 053 §8 item 1). The code does not produce them (`verdict_from_levels`
    returns before building `checks`); the result document computes them by hand from
    `levels[ρ]`, applying the inequalities of the table to the recorded aggregates. A clause
    whose input is a count over **zero** generator-valid seeds (for example `n_escape_MINK = 0`,
    `n_abstain_BH = 0`) is reported as **not evaluable**, not as passed.
- **NaN never passes** (O8 review, D1): every pass comparison is false on NaN (`≤` for (ii),
  F, (iii), (iv); `≥` for the coverage floor; `<` for the abstention count, which is an integer).
  A level with no clean bracket has NaN median, IQR and midpoint std. With exactly **one** clean
  bracket the median is defined, the IQR is NaN and the midpoint std is **0.0**, not NaN. **At
  ρ\*** (iii) then passes on its own, but (ii) fails through the IQR, so the run cannot PASS
  (`test_one_clean_bracket_passes_iii_but_fails_ii`). At ρ = 32 or 63 only the median enters
  (through F); the IQR and the midpoint std of those levels are reported but are not criteria, so
  a secondary level with one clean bracket can be part of a PASS.
- **(i) and (iv) are gate-derived.** With the flat control abstaining, `d ≥ 0` on every seed and
  the exact sign-flip test gives `p = 2^-m`, with m the number of seeds where the BH passes the
  gate, whatever the size of `sep_BH`. So (i) reduces to "fewer than 3 BH seeds abstained" at
  each required level, and (iv) to "≤ 1 flat seed escaped the gate". The reduction of (i) needs
  **no** flat escape at that level: (iv) allows one at ρ\* and does not limit escapes at ρ = 63,
  and an escape can make `d < 0` on a seed, so (i) can then also fail through `p_perm`. Neither is independent
  confirmation; the discriminating content is (ii), (iii) and coverage (comité 052 §8 item 7;
  O8 review, D10 and D12).
- **Declared dependence between levels** (O8 review, D7; inherited from 1+1,
  `nachocausal/generator.py:46`). The three ρ levels use the same 20 seeds, and each seed seeds
  `numpy.random.default_rng(seed)` with no ρ. The levels therefore share their random stream:
  the first `n(32)` values of `t` at ρ = 63 are the `t` of ρ = 32, and the next ones are the
  uniforms behind `r` at ρ = 32 (checked on seed 7_000_100). Each level is a correct Poisson
  sprinkle, but the levels are **not independent**, and the convergence clause F compares
  correlated medians. This is declared, not changed (PI decision, 2026-10-14), so that the dev
  parity records stay valid.
- **Declared selection on clean brackets** (O8 review, D8; as 1+1, `nachocausal/validate.py:136`).
  The median and IQR of widths and the midpoint std use only clean brackets (`width ≥ 0`);
  inverted brackets (`r_lo > r_hi`) are left out of them, and only coverage, over all
  bracket-valid seeds, sees them. `n_clean` is reported per level.
- **Reported verbatim and separately, whatever the verdict:** per level, generator-invalid count
  and reasons, BH-abstain count, flat-escape count, bracket-valid and clean counts, coverage count
  (not only the fraction), median and IQR width/2M, midpoint std, p_perm. These descriptive
  aggregates are also reported when a level has fewer than 18 generator-valid seeds;
  its status and the run verdict remain INCONCLUSIVE. Empty samples have zero counts and
  NaN statistics (IQR is also NaN with one clean bracket), never a statistical PASS.
- **Known weakness, stated in advance** (comité 052 §5 item 5; ASTRA risks): a narrow, reproducible
  but mislocated bracket can pass (ii)-width and (iii); only coverage catches it, and with floor
  0.5 up to 10 of 20 non-covering seeds still PASS. The coverage floor 0.5 is a deliberately weak
  floor, not nominal coverage, and is neither raised nor lowered.
- **Low power of (ii)-width and IQR, stated in advance** (comité 053 §8 item 7). This follows
  from theory only: the ASTRA neighbour model (`revisiones/2026-10-13-anclaje-theta-ciego/astra.md`
  l.33-46) and the frozen formula. No dev JSONL and no dev width was consulted to write it.
  For a classifier that splits the minimal elements exactly at r = 2M, the bracket is the gap
  between the nearest minimal elements on either side in radial projection. With radial
  intensity `λ_r(2M) = c₃ρ^{2/3}·2π(2M)√2`, `c₃ = Γ(4/3)(3/π)^{1/3} ≈ 0.879`, each side is
  Exp(δ) with `δ = 1/λ_r(2M) ≈ 0.256 ρ^{-2/3}`, and the width is Gamma(2, δ). The bound
  `θ_loc·2M = 2ρ^{-2/3}/(1.4π) ≈ 0.455 ρ^{-2/3} ≈ 1.78 δ`. Then P(one width ≤ bound) =
  `1 − e^{-1.78}·2.78 ≈ 0.53`; the median width is `1.678 δ ≈ 0.94` of the bound; the IQR is
  `1.73 δ ≈ 0.97` of the bound. So even an ideal order-only localiser passes the width and IQR
  clauses at ρ\* only about half the time `[UNVERIFIED — closed-form arithmetic in a flat-local
  approximation, ρ^{-1/3} ≈ 0.2 not ≪ 2M; no simulation]`. This is a property of the test, fixed
  before any validation data. **A FAIL is reported as FAIL**, with no qualifier added after the
  result. **No result of this run may be used to re-derive, rescale or loosen θ_loc, θ_stab or
  K_LOC**, here or in any successor pre-registration.

**Can-fail evidence (step 4):** `tests/test_004_criteria_can_fail.py` (20 tests) shows (ii) via
coverage, (ii) via width, (iv) and (v) can each produce FAIL; since the O8 review (D9) it also
shows, each failing alone, (i) by 3 BH abstentions at ρ = 63, the convergence clause F, (iii),
the IQR clause of (ii), a NaN median failing F, a NaN IQR never passing, and a short secondary
level giving INCONCLUSIVE; since comité 053 it also fixes the verdict precedence (a short level
gives INCONCLUSIVE with no `checks` even with 3 BH abstentions at ρ\*) and the one-clean-bracket
case. (v) is shown false only outside the validation label, where it is a precondition (§7).
`dev/mutation_check_004.py` catches
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
- **Writing:** `results/validation_004.json` is written atomically. `results/` is git-ignored
  (`.gitignore:21`), which keeps the tree clean during the run (the seed guard re-checks
  `git status --porcelain`), so a plain `git add` records nothing. Immediately after the run
  ends, crashes or aborts, the four run files are **force-added** by name in one commit:
  `git add -f results/validation_004.json results/validation_004.progress.jsonl
  results/validation_004_provenance_launch.txt results/validation_004_run.log` (only the files
  that exist), with their `sha256sum` lines written into `docs/preregistration_004_result.md`
  in the same commit, and the commit is pushed (lesson of prereg-002 `PRIMARY_ARTIFACT_LOST`,
  `docs/preregistration_002_result.md`; comité 053 §8 item 4).
- **Run log:** the run's stdout and stderr go to `results/validation_004_run.log`, so the
  verdict line, or the traceback of an abort, is kept.
- **Progress log** (O4, §10): `results/validation_004.progress.jsonl`, one fsynced line per seed
  and level with only `seed, rho, seconds` (`validate.PROGRESS_FIELDS`), appended as the run
  goes. It says nothing about the outcome: abstentions and invalid seeds would reveal a FAIL of
  (i) or (iv) hours before the end (O8 review, D6). It is force-added with the result, or alone
  after a crash (Writing, above). Its `start` line uses local time with offset; the provenance
  file records UTC.
- **Deterministic aborts are not crashes** (O8 review, D11). A Guard-v failure or a seed with
  `n_minimal > 256` (outside the τ table) raises and stops the run without a result. Rerunning
  the same seeds, environment and commit would stop in the same place, so such an abort is not
  relaunched: it is reported as `ABORTED_GUARD_V` or `ABORTED_TAU_RANGE`, with the progress log
  and the traceback, and it is not a PASS. These two names are labels of the result document;
  the code raises an exception and writes no verdict.
- **Entry point:** `python -m nachocausal2p1.validate` runs `validate.run()` with its defaults
  (seeds from the committed C2 manifest, `guard=True`, `write=True`) and prints the verdict and the result path. The
  validation label refuses `write=False` (O8 review, D3 and D4).
- **Provenance launch file** `results/validation_004_provenance_launch.txt`. No code writes it;
  it is produced by these commands, run in order from the repo root on the C2 commit, with
  `PY=/home/ignac/nachocausal/.venv/bin/python` and `C1=<full C1 SHA>` (comité 053 §8 item 6):

  ```bash
  export NUMBA_NUM_THREADS=20      # before the block, so that `env` below records it
  F=results/validation_004_provenance_launch.txt; mkdir -p results
  { echo "start_utc $(date -u +%FT%TZ)"
    echo "head $(git rev-parse HEAD) branch $(git rev-parse --abbrev-ref HEAD) c1 $C1"
    make verify-seal-004
    sha256sum docs/preregistration_004.md docs/validation_004_seeds.json
    echo "sealed_diff_lines $(git diff $C1 -- nachocausal/ nachocausal2p1/ docs/preregistration_004.md | wc -l)"   # must be 0
    echo "status_porcelain_lines $(git status --porcelain | wc -l)"                                          # must be 0
    uname -a; lscpu | grep -E 'Model name|^CPU\(s\)|Thread'; $PY -V
    $PY -m pip freeze > /tmp/pf.txt; cat /tmp/pf.txt
    echo "pip_freeze_vs_lock_diff_lines $(diff <(sort /tmp/pf.txt) <(grep -vE '^(#|$)' requirements-lock.txt | sort) | wc -l)"
    env | grep -E '^(NUMBA_|OMP_|MKL_|OPENBLAS_|NC2P1_)' | sort
    $PY -c "from nachocausal2p1 import thresholds as t; print('T_EDGE', t.T_EDGE, 'STATUS', t.STATUS); print('seeds', t.validation_seeds())"
    make test-004 PY=$PY 2>&1 | tail -1
  } > $F 2>&1
  ```

  The commands need `bash` (process substitution). The run itself is launched in the same shell as
  `nohup $PY -m nachocausal2p1.validate > results/validation_004_run.log 2>&1`,
  with the host kept awake; on exit, `echo "end_utc $(date -u +%FT%TZ)" >> $F`. Bit-reproducibility
  is claimed only for 20 numba threads on the measured host (§8); a run elsewhere is unverified.
- **Pre-flight commands** (no virgin seed): `make test-004`, `make dry-run-004` (mechanics only:
  off-grid ρ = 2, burned seeds `7_000_100..7_000_102`, no widths; exit 0 on 2026-10-15),
  `make verify-seal`, `make verify-seal-004`, `make verify-comite`, and the global `make test`.
  A full-grid dry run on `DRY_RUN_SEEDS` after C1 (anticipated by comité 052) is **not** part of
  the plan: the port was already run at ρ = 126, T = 16 on seed `7_000_100` (§8), and a full grid
  would cost about 2 h for a result that is discarded (PI agreed, 2026-10-15).
- **Sequence:** comité 052 §9 steps 1-6 (done, §5-§8 above; step 5 partial) → step 7: comité 053
  (`RECOMMEND_REVISE_AND_RECONVENE`; wording and procedure only) → this revision → cross-family
  review of §7/§9 against `validate.py` and `/auditor` on the delta → C1 freeze → C2 blind draw →
  C3 single blind CPU run.
- **C1/C2/C3 binding (auditor 045 E1):** C1 is the unique commit introducing the non-draft
  `docs/preregistration_004.md`; it seals that document and the instrument, including the draw
  recipe. After explicit C2 authorisation, on the pinned environment and a clean tree,
  `python -m nachocausal2p1.seed_manifest <full-C1-SHA>` creates only
  `docs/validation_004_seeds.json` (`freeze_commit`, `draw_seed`, `seeds`), refusing to overwrite
  an existing manifest. Commit and publish that manifest without changing the C1 instrument.
  C3 uses the published C2 commit as HEAD and the manifest's C1 commit as the reference for the
  zero-diff check above. The C2 manifest is an administrative addition outside the sealed paths;
  it cannot change any analysis parameter.
- **C1 procedure** (comité 053 §8 item 5; `seed_manifest._check_freeze` finds C1 with
  `git log --full-history --diff-filter=A`):
  - C1 **adds** `docs/preregistration_004.md` as a new file and keeps the draft
    `docs/preregistration_004_draft.md`; never `git mv` the draft, since a rename is not an
    addition and C2 would then refuse.
  - C1 also sets `STATUS = "FROZEN"` in `nachocausal2p1/thresholds.py`. Before committing:
    `make verify-seal` unchanged, `make verify-comite` passing, tree clean.
  - C1 is **pushed**, and its full SHA is written into a signed, pushed note (the sign-off of
    the comité that clears C1) **before** C2 is run.
  - C1, C2 and C3 are committed on `prereg004/step3-port` and are never amended, rebased or
    squashed. The branch is merged only by fast-forward or by a merge commit, which keep the C1
    SHA. A re-made C1 would give a new draw seed; that is forbidden.

**Audit trail:** `/auditor` on the candidate package: report 043 `AUDIT_FAIL` → fixes `c16fb12`
→ report 044 `AUDIT_PASS` → O3/O4/O8 changes (`5afb33d`, `4190a10`) → report 045 `AUDIT_FAIL`
(E1, E2, W1, W2) → remediation `782d031` → report 046 `AUDIT_PASS`
(`docs/auditor/auditor_report_046_prereg004-auditor045-remediation-reaudit.md`). Reports 043 and
044 do not name their producer; this document treats them as the author's model family, so not an
independent review (global rule 5). Reports 045 and 046 were produced by **Codex**, a different
model family; 046 states that it does not certify that it ran in a separate session. Neither
caught that the §7 text then contradicted the verdict precedence in the code (comité 053 §8
item 1). Comité 053 (`docs/comite/comite_decision_053_prereg004-draft-readiness-c1.md`) is
Claude. Cross-family *content* reviews: Gemini O8 on `5afb33d` and Gemini on `007947e` (§10); the delta `782d031..616c55d` was audited by Gemini without command execution (`revisiones/2026-10-15-prereg004-auditor-delta-gemini/`, `AUDIT_PASS_WITH_WARNINGS`). The 1+1 precedent is PASS with caveats `PRIMARY_ARTIFACT_LOST;
TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY` (`docs/preregistration_002_result.md:1`).

## 10. Open items O1-O8: resolution (2026-10-14)

The PI settled the eight items on 2026-10-14, in a Claude Code session, one by one; Claude
transcribed the decisions. The same decisions are recorded in comité 052 §11.

| item | decision | where |
|---|---|---|
| O1 draw seed | first `20261014`; **revised** after the O8 review (D5): derived at C2 from the SHA of the C1 commit, `draw_seed_from_commit` | `thresholds.py`, §6 |
| O2 step 5 partial | **accepted as partial**: parity on 1 of 10 seeds plus the dev pairwise parity at T = 16 and port = dev bit-equality; the 9 remaining seeds and the thread probe are not run | §8 |
| O3 thread count | **20**, enforced in code: `thresholds.assert_blind_threads()` (environment `NUMBA_NUM_THREADS=20` and `numba.get_num_threads() == 20`), called by `validate.run` under the validation label before any generation | `thresholds.py`, `validate.py`; tests `test_blind_threads_can_fail`, `test_validation_run_checks_threads_before_generation` |
| O4 progress log | **added before C1**: `results/<label>.progress.jsonl`; **reduced** after the O8 review (D6) to `seed, rho, seconds` | `validate.py`; tests `test_progress_line_is_blind`, `test_progress_log_written_per_seed_before_the_verdict` |
| O5.1 | confirmed: ≥ 3 BH abstentions FAIL (i) at every required ρ (63 and 126) | `validate.py` `summarise_level`, `verdict_from_levels` |
| O5.2 | confirmed: `p_perm` over generator-valid seeds, an abstained BH enters with `sep = 0`. **Deviation from 1+1**, where such a seed is excluded from `p_perm` and from the valid count (`nachocausal/validate.py:117`); the 2+1 rule is the more conservative one | `estimator.py:42-43`, `validate.py` |
| O5.3 | confirmed: coverage over bracket-valid seeds, count reported (as 1+1, `nachocausal/validate.py:142`) | `validate.py` |
| O5.4 | confirmed: 20 000-pair fine-shot audit; any failure or disagreement invalidates the seed | `validate.py` `generate` |
| O6.1-O6.4 | accepted: 10-seed dev cells with the test-only `MIN_VALID_SEEDS` bypass; (i) also failing in (a) and (c), with the synthetic (ii)-only case; no domain-gate bypass needed (pure functions); (iv) named `iv_flat_escapes_primary`, measured at the primary | `tests/test_004_criteria_can_fail.py` |
| O7 | signed: ρ grid {32, 63, 126} with primary 126; 20 seeds / 18 valid; coverage floor 0.5; (iv) ≤ 1 escape; `T_EDGE_MIN = 10`; exact pins; CPU-only path; and the two `[PI-S3]` clauses (slack F, significance at every ρ ≥ 63) | `thresholds.py` |
| O8 independent review | **done**: `revision-ciega gemini` (gemini-4-argon, high) on 5afb33d. Verdict NOT READY; 12 defects confirmed against the code (D1-D12), 5 claims partial or unsupported. Fixed or declared on 2026-10-14 (below) | `revisiones/2026-10-14-prereg004-gemini/evaluacion.md` |

**What the O8 review changed (2026-10-14).** Code fixes with no decision needed: D1 (NaN never
passes), D3 (`write=False` refused under the validation label), D4 (`__main__`), D9 (isolated
can-fail tests), D10 (§7 wording), D11 (deterministic aborts written down). PI decisions: D2
(any short level ⇒ INCONCLUSIVE), D5 (draw seed from the C1 commit), D6 (progress log reduced),
D7 and D8 (declared in §7, not changed). D12 is stated in §7.

**Consequences of the O8 changes (closed).** The re-audit of the O3/O4/O8 delta was done:
report 045 `AUDIT_FAIL`, remediation `782d031`, report 046 `AUDIT_PASS` (§9 audit trail).
Step 7 was comité 053 (2026-10-15).

**Auditor 045 remediation (2026-10-14; not a new audit verdict).** The PI authorised the
proposed corrections after report 045 (`AUDIT_FAIL`, 2 errors and 2 warnings): E1 is addressed
by the separate C2 manifest and explicit C1/C2/C3 references above; E2 by retaining descriptive
aggregates for INCONCLUSIVE levels; W1 by limiting the SHA claim to reproducibility; W2 by
correcting the coverage example to 10/20. The historical report 045 remains unchanged.
The changed candidate was re-audited in report 046 (`AUDIT_PASS`).

**Comité 053 revision (2026-10-15; wording, procedure and tests only).** The PI chose to apply
the eight changes of comité 053 §8 and to add a cross-family review. Changed: verdict precedence
and non-verdict clause values under INCONCLUSIVE (§7); the NaN and one-clean-bracket statements,
the IQR wording, (iii) ddof, (v) as a precondition (§7); the power disclosure for (ii) (§7); the
SHA table (§3); force-adding the run files, the run log and the provenance commands (§9); the C1
procedure (§9); the audit trail (§9); two tests in `tests/test_004_criteria_can_fail.py`; the
`make test-004`, `dry-run-004` and `verify-seal-004` targets. Nothing under `nachocausal/` or
`nachocausal2p1/` changed in this step (the later G8 fix below changes `seed_manifest.py`); no θ,
T, ρ, K, seed or criterion changed.

**Cross-family review of this revision (2026-10-15).** `revision-ciega gemini` (gemini-4-argon,
high) on `007947e`: «listo con cambios menores enumerados»; eleven objections, all confirmed or
partly confirmed against the code (`revisiones/2026-10-15-prereg004-c053-gemini/evaluacion.md`).
One was a code loophole (G8): `seed_manifest._check_freeze` ran `git log --diff-filter=A` without
`--full-history`, so a second C1 merged in with `-s ours` hid the first and gave another draw.
Fixed in `nachocausal2p1/seed_manifest.py` (`--full-history`), with the test
`test_second_c1_merged_with_ours_strategy_is_refused` (fails without the fix, passes with it).
The other ten are text: the one-clean-bracket statement holds only at ρ\*; non-verdict values
under INCONCLUSIVE are computed by hand and counts over zero seeds are "not evaluable"; the
reduction of (i) needs no flat escape; "bracket-valid" defined (§4); the exploration band is
burned only as validation seeds (§6); `ABORTED_*` are document labels; the provenance block is
bash, exports `NUMBA_NUM_THREADS=20` first and ignores blank lockfile lines (§9).

**Gemini audit of the delta `782d031..616c55d` (2026-10-15).** `AUDIT_PASS_WITH_WARNINGS`, 0 errors,
2 warnings, without command execution (`revisiones/2026-10-15-prereg004-auditor-delta-gemini/`).
W1 (§9 said O8 was the only cross-family content review) is fixed in the text. W2 (the
`validate.py` docstring still said "every pass test is written as `x <= bound`", and a comment said
empty samples "cannot produce a PASS" although `escape_pass` reads True on zero seeds) is fixed in
the comments and docstring only, by PI decision: no executable code changed; the AST is equal
after excluding docstrings; the file's SHA changed (§3).

**Gemini audit of the comments-only delta `6f76d21..e6b5bfe` (2026-10-15).** `AUDIT_PASS`,
0 errors, 0 warnings, without command execution (`revisiones/2026-10-15-prereg004-auditor-w2-gemini/`).

**Signature and C1 (2026-10-15).** The PI signed comités 052 and 053 on candidate `0c16845`
(commit `94cd3b4`), explicitly waiving the reconvening recommended by comité 053 as a PI procedural
decision, and accepting as unverified the power figures of §7 and thread determinism (§8). The PI
then authorised C1. Five pre-freeze tests were pinned to the candidate state in `51bf237`, so they
test the same behaviour after C1.

**Open after C1:** record the full C1 SHA in a signed, pushed note before C2 (§9); C2 and C3, each
on separate explicit PI authorisation.
