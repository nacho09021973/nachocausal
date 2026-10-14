# Comité Decision 052 — prereg004-2p1-design

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question
Design of prereg-004 for the signed 2+1D equatorial front: (a) box height T and its margin, (b) intensities and primary endpoint, (c) the anchor of the localisation threshold theta_loc in 2+1D, (d) the coverage floor, (e) the LOO false-positive criterion (and how significance (i), stability (iii) carry over) — to be frozen on principled bases BEFORE any 2+1 validation data is seen.

## 2. Verified state
Facts checked **this session**, each with its command / file:line (seal SHA, env, git, results
presence). Anything unchecked is marked `[UNVERIFIED]`.
- `make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`. This matches `docs/preregistration_002.md:7-9`, so the sealed 1+1 package is untouched.
- `git status --porcelain` → 0 lines, so the tree is clean; HEAD is `eeaf4c7`. `ls docs/preregistration_00*` lists 001 (plus its addendum and result), 002 (plus its result) and 003 (plus its draft). There is **no `docs/preregistration_004.md`**.
- 2+1 seed bands (`dev/gen2p1_efbox.py`: `EXPLORE_BAND = (7_000_000, 7_000_999)`, `VIRGIN_BAND = (8_000_000, 8_999_999)`):
  - the virgin band has never been used;
  - the exploration seeds used are listed in the dossier;
  - phase-A seeds 1, 2, 3, 4, 7, 99 and 12345 are burned (`dev/2P1_PHASE_A_RESULT_2026-10-12.md`).
- `nachocausal/thresholds.py:46`: `INTENSITIES = (1500, 3000, 6000, 12000)`. `:98`: `K_LOC = 2`. `:103`: `ell = (intensity/BOX_AREA)**-0.5`. `:141`: `GATE_TAU_N_MAX = 128`.
- Results presence: `results/` holds only artefacts from earlier fronts. No 2+1 validation output exists.
- Dev 2+1 results are summarised in the dossier:
  - t_min = 8, 10 and 10 at ρ = 32, 63 and 126;
  - BH localises 180/180 and the flat control abstains 180/180;
  - the files are `dev/2P1_TMIN_SWEEP_RESULT_2026-10-12.md`, `dev/2P1_TMIN_RHO126_RESULT_2026-10-13.md`, and the v2 JSONLs.
- `/auditor` was **not run** for this session. The reason given in the dossier is that no published 2+1 claim underlies this design question. The falsifier and the warden both require `/auditor` on the 2+1 package before any virgin seed is drawn (§5, §6).
- Chair self-correction: the dossier said that the dev τ(n) for n > 128 used "the same procedure" as the sealed table. That is **false**. Dev uses 4000 reps and a per-n rng; the sealed table uses 40000 reps and one shared stream (logic brief, warden, falsifier).


## 3. Dossier
Files and references the chair supplied to the committee:
- The chair's dossier text was given to every member. It is reproduced in substance in §2, and the full text is the chair's working file.
- docs/acta_frente_2p1_ecuatorial_2026-10-12.md
- docs/preregistration.md, docs/preregistration_001_addendum.md, docs/preregistration_002.md, docs/preregistration_002_result.md
- docs/estimator_v2_freeze.md, docs/estimator_v2_decision_spec.md
- nachocausal/thresholds.py, nachocausal/estimator.py, nachocausal/gate.py, nachocausal/validate.py, scripts/gen_tau_table.py
- dev/gen2p1_efbox.py, dev/gen2p1_gpu.py, dev/validate_gen2p1_gpu.py, dev/explore_2p1_estimator.py, dev/sweep_2p1_T.py, dev/analyze_2p1_tmin.py
- dev/2P1_PHASE_A_RESULT_2026-10-12.md, dev/2P1_PHASE_B_INTERIM_2026-10-12.md, dev/2P1_TMIN_SWEEP_RESULT_2026-10-12.md, dev/2P1_TMIN_RHO126_RESULT_2026-10-13.md, dev/2P1_NUMBA_CACHE_STALE_TABLES_2026-10-12.md, and the v2 JSONLs
- research_program/puente_3p1/2026-10-12/E1_equatorial_restriction_lemma.md
- biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md (EGS); biblioteca/derived-md/The causal set approach to quantum gravity.md (Surya LRR 2019)
- CLAUDE.md


## 4. Expert briefs (wave 1 — blind, parallel)
### Reproducibility engineer brief
- **Proposed artefact(s):**
  - `docs/preregistration_004.md`: the frozen prereg. It names T plus its margin, the ρ grid and primary endpoint, θ_loc, the coverage floor, the (i)/(iii)/(iv) criteria, the 20-seed draw, and the seal SHA. It follows the structure of `docs/preregistration_002.md:1-70` (seal line, blind draw, frozen analysis, binding rules, provenance chain). Before it, a `docs/preregistration_004_decision.md`/committee brief in `docs/comite/` records the anchor rationale, and that brief has to pass `make verify-comite`.
  - **A new sealed sub-package, not `dev/`.** For example `nachocausal2p1/` (or `nachocausal/eq2p1/`) containing `generator.py` (promoted from `dev/gen2p1_efbox.py`), `estimator.py` (thin wrapper that imports `nachocausal.estimator.improvement/two_means_split` unchanged), `thresholds.py` (its own seal file), `validate.py`, `dry_run.py` and `fixtures/tau_table_2p1.json`. Do **not** edit `nachocausal/thresholds.py`: its SHA `6e2c3888…` is the prereg-002 seal (`docs/preregistration_002.md:7-9`), and editing it would break the sealed 1+1 package.
  - **New Makefile targets:**
    - `verify-seal-004`: SHA256 of the new thresholds file **and** of the tau fixture.
    - `dry-run-004`: exploration-band seeds only, verdict discarded.
    - `test-004`: kept outside `make test`, the same pattern as `op21-bench` (`Makefile` OP-2.1 block).
  - **Outputs:**
    - `results/validation_004.json`
    - `results/validation_004_provenance_launch.txt`, same shape as `results/validation_provenance_launch.txt`
    - `results/validation_004_run.log`
    - `results/preflight_004_{test,dryrun}.log`
    - Then `docs/preregistration_004_result.md`.

- **Environment & seal:**
  - The blind run uses the sealed CPU `.venv` (`numpy==1.26.4`, `requirements.txt:7`; `thresholds.assert_environment` checks `PINNED_NUMPY`, `nachocausal/thresholds.py:18-32`). The acta's `gpu_dev_only` rule applies (`docs/acta_frente_2p1_ecuatorial_2026-10-12.md:100`), so CuPy/`.venv-gpu` must not be importable on the run path: CuPy needs numpy≥2 (`requirements-gpu.txt`), and `NC2P1_DEVICE` must be forced off or removed.
  - **New dependency surface.** The 1+1 sealed package is pure numpy, with no numba under `nachocausal/` (grep returned nothing). The 2+1 generator needs `numba` (`dev/gen2p1_efbox.py:24`, `@njit(parallel=True)` at :137, :249, :282) and `scipy.special.lambertw/roots_legendre` (:25). `requirements.txt` only gives ranges for these (`scipy>=1.11,<2`, `numba>=0.59,<1`). Prereg-004 must **hard-pin** exact numba, llvmlite and scipy versions and extend `assert_environment` for the 2+1 package to check them.
  - **Pre-flight checks, all reversible:**
    - `make verify-seal` must still print `6e2c38881234…bfefd4`, proving the 1+1 package is untouched.
    - `make verify-seal-004` must print the new SHA recorded in the prereg.
    - `git status --porcelain` must be 0 lines.
    - `git diff <seal-commit> -- nachocausal/ nachocausal2p1/ docs/preregistration_004.md` must be 0 lines. This is the same "package_docs_diff: 0 lines" check as `results/validation_provenance_launch.txt:4`.

- **Provenance capture:** the launch file records:
  - `captured_utc`, `start_utc` and `end_utc`
  - the full HEAD commit SHA and branch
  - both thresholds SHAs (1+1 and 2+1) and the tau-fixture SHA
  - `package_docs_diff` line count
  - `uname -a`, `python -V`, and the full `pip freeze` of the sealed venv. The prereg-001 freeze listed only 6 packages; it must now include numba, llvmlite and scipy.
  - `NUMBA_NUM_THREADS`, OMP/MKL thread env, and `numba.config.CACHE`/`NUMBA_CACHE_DIR` (expected: cache disabled)
  - the frozen `T_EDGE` value **as read by the generator module at runtime** (echoed, not assumed)
  - the 20 seeds, plus the draw recipe: `numpy(1.26.4).default_rng(VALIDATION_DRAW_SEED_004).choice(arange(8_000_000, 9_000_000), 20, replace=False)`. That band is reserved and never used (`dev/gen2p1_efbox.py:34`). The draw seed is fixed in the prereg before drawing, mirroring `docs/preregistration_002.md:20-24`.
  - a runnable guard asserting the seeds are disjoint from `EXPLORE_BAND` and the burned Phase-A seeds
  - per-seed records: N, n_minimal, generator stats (transitivity violations, fine-shot audit, radial check vs `past_matrix_fast`) and seconds
  - `tests` pass count

- **Run mechanics:**
  - **Reversible pre-flight, done first:**
    1. `make test`, `make test-004`, both verify-seal targets.
    2. `make dry-run-004` on exploration-band seeds (verdict discarded, like `nachocausal/dry_run.py:3`).
    3. One CPU-timing realisation at the frozen (T, primary ρ). The ~4× CPU-vs-GPU estimate is from the dossier, not measured at the frozen T `[UNVERIFIED for T=16/20]`.
    4. CPU/GPU order parity rerun at the frozen T. Parity is shown only at T=6, 12, 16 (`dev/validate_gen2p1_gpu.py`, per the dossier). If T=20 is chosen, it needs its own parity check before freezing, because the dev anchors were measured on GPU.
  - **The committing step:** a single explicit foreground-or-background invocation `python -m nachocausal2p1.validate` with `guard=True`, run only after the user explicitly authorises it.
  - **Writing results:** write `results/validation_004.json` atomically (temp file plus rename), then immediately hash it and commit it. This is a lesson from prereg-002's `PRIMARY_ARTIFACT_LOST` status (dossier) and the 2026-06-21 relaunch with an empty log (`results/validation_provenance_launch.txt:17-19`).
  - **Clean abort:** `assert_environment` failure, seal mismatch, or a non-empty diff aborts **before** the first seed. A mid-run generator assertion (`"fine shooting missed"`, `dev/gen2p1_efbox.py:330`), a transitivity violation, or a radial-check mismatch must be pre-registered as **seed-invalid**, counting toward the `<18/20 → INCONCLUSIVE` rule (`docs/preregistration_002.md:55-56`). It must never trigger a rerun on replacement seeds. If the process crashes, it is relaunched on the *same* seeds with identical env and commit, and the relaunch is logged with a timestamp (the prereg-001 precedent).
  - Background runs need a log to a committed path, plus a heartbeat line per seed.

- **Reproducibility risks / ambiguities:**
  - **T comes from an environment variable at import time.** `T_EDGE = float(os.environ.get("NC2P1_T_EDGE", "6.0"))` is at `dev/gen2p1_efbox.py:29`, and the z-tables are built from it at import (:43-53). This is exactly the failure class behind the numba-cache stale-table incident (`dev/2P1_NUMBA_CACHE_STALE_TABLES_2026-10-12.md`). In the sealed package T must be a frozen literal constant, the env knob must be removed, and `cache=False` must be kept (:114-282). Otherwise a missing env var silently gives T=6, which is outside the plateau.
  - **The τ(n) gate for n>128 is not "the same procedure" as the sealed table.**
    - Dev: `default_rng([GATE_NULL_MC_SEED, n])` with **4000** reps per n (`dev/explore_2p1_estimator.py:36-38`).
    - Sealed: a **single** shared rng, n ascending, `GATE_NULL_MC_REPS` = 40000 reps (`scripts/gen_tau_table.py:7-10,38-44`; `docs/estimator_v2_seal.md`).
    - Measured n_minimal reaches 99–184 at ρ=126 (`dev/2p1_sweep_T_rho126_v2_2026-10-12.jsonl`), so the gate verdict depends on this extension. Prereg-004 must freeze an explicit procedure (preferably: continue the sealed single stream contiguously to n_max at 40000 reps), regenerate it as a committed fixture with its SHA, and verify that n≤128 reproduces `tau_table.json` bit-for-bit. The dev τ values must not be reused as-is.
  - **The n_max of the τ fixture must cover the frozen grid.** Higher ρ means more minimal elements. A run that hits n > fixture max must raise `OUT_OF_DOMAIN`/abort (as `nachocausal/gate.py:49` does), never extrapolate. Expected n_max at untested ρ>126 is `[UNVERIFIED]`.
  - **Possible ground-truth leakage in the record format.** Dev records put the estimator output and the scoring (`r_lo`, `covers_2M`) in one dict (`dev/explore_2p1_estimator.py:40-64`). The sealed validate must run an order-only Guard-v analogue: the estimator receives only `order`, and scoring is a separate function that receives `r` afterwards (`NO_GROUND_TRUTH_LEAKAGE`). The guard-can-fail test has to be ported to the 2+1 package.
  - **RNG stream coupling.** The fine-shot audit draws from the *same* `rng` after sprinkling (`dev/gen2p1_efbox.py:337-350`). This is harmless to the sprinkle, but the call order and audit size (20000) must be frozen so per-seed logs reproduce bit-for-bit.
  - **Thread-level determinism of `parallel=True` numba kernels.** The kernels write per-pair results, with no reductions visible in the stage-1/shoot signatures. Bit-reproducibility across thread counts is still `[UNVERIFIED]`. The pre-flight should run one dev seed with `NUMBA_NUM_THREADS=1` and with the default count, and confirm identical orders.
  - **Cost.** Wall-clock for 20 seeds × the ρ grid × (BH + Minkowski) on CPU at T=16–20 is `[UNVERIFIED]`. The dossier gives GPU ~40 s to 8 min per realisation at ρ=126 and CPU ~4× slower, so a ρ>126 primary could take many hours on CPU. Prereg-004 should state the expected runtime and the crash/relaunch rule up front, so the duration cannot become a reason to change the grid after launch.
  - **Two seals live side by side.** The 1+1 `make verify-seal` must keep printing `6e2c3888…` (dossier). Any shared import (`nachocausal.estimator`, `nachocausal.gate`) is part of the 2+1 instrument, so the 2+1 seal record should also list the SHAs of those imported 1+1 modules, not only the new thresholds file.

### Mathematician brief
- **Computability:**
  - **What can be computed from the order alone.** Given the boolean past matrix C, everything the estimator needs is computable in finite time from the order relation alone, with no use of coordinates. Minimal elements are the all-False rows. O(i) = |future(i)| is the column sum C[:,i]. The 1-D 2-means split and `improvement` follow from those (`nachocausal/estimator.py:113-131`, `:134-157`). The cost is O(N²) memory and time. At N≈16000 the matrix is about 2.6e8 booleans, so it is tractable on CPU for the blind run.
  - **The order is partial, not total.** The flat control and the black-hole cloud are both genuine partial orders. Transitivity holds with 0 violations (DOSSIER, generator controls). `verify_order_only` (`estimator.py:164`), the permutation-invariance check, carries over unchanged and should be a stated precondition in prereg-004.
  - **New in 2+1: the order is only numerically decidable.** In 1+1 the causal relation has a closed form (`nachocausal/generator.py` `past_matrix_fast`). In 2+1 it comes from geodesic shooting with tolerances (`dev/gen2p1_efbox.py:164` `REL_MARGIN`/`TOL`, `shoot_pairs_fast` `:250`). Pairs close to null separation can therefore be misclassified. The existing controls (same-angle pairs equal the closed form, the CPU and GPU generators agree exactly, mutation is detected) bound this empirically but not analytically. Prereg-004 should freeze `REL_MARGIN`/`TOL` and the audit count as part of the sealed bench.
  - **The τ(n) gate is still data-independent, but its table must be extended.** τ(n) is the p99 of `improvement` under an abstract Uniform[0,1] null (`thresholds.py:125-140`, α=0.01, seed 20260621, 40000 reps). In 2+1, n (the number of minimal elements) exceeds the sealed `GATE_TAU_N_MAX=128`. The extension must be produced by the same script (`scripts/gen_tau_table.py`) with the same seed and reps. It should be emitted as a new hashed fixture covering the expected n range at the largest frozen intensity, and that hash frozen in prereg-004. Values computed in dev alone are not enough.
  - **Domain gate.** `T_EDGE_MIN=6` was pinned by 1+1 exploration (`thresholds.py:116-121`). In 2+1 the analogous gate must be re-pinned to the 2+1 t_min, because T=6 is a mis-localising regime there (`dev/2P1_PHASE_B_INTERIM_2026-10-12.md`). The 1+1 value cannot be inherited.
- **Order observable:**
  - **Definition.** O(i) = |J⁺(i) ∩ C| for minimal elements i, i.e. the number of elements that have i in their past. This is the future-cardinality variant that Eichhorn–Gamito–Stokes propose next to the longest-chain variant (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`, around l.181-193, Fig. 3 lower panel: "Again, the distribution is bimodal").
  - **Why it carries the horizon signal.** For a minimal element inside the horizon, every future-directed causal curve reaches the inner boundary r=0.1 in finite t*. Its future volume within the box is therefore bounded uniformly in T. For a minimal element outside, the future reaches r=1.3 and grows roughly linearly in T. The gap is bimodal and widens with T (same source, l.188-191).
  - **Same mechanism in 2+1.** On the equatorial slice the radial null structure is identical to 1+1: radial rays have dφ=0, and by lemma E1 the 2+1 order is the 3+1 order restricted to the equator (`research_program/puente_3p1/2026-10-12/E1_equatorial_restriction_lemma.md`). Angular motion only slows radial escape. So the 1+1 mechanism carries over with no new physics.
  - **Closed form of the finite-T bias.** In ingoing EF coordinates, outgoing radial null rays obey dr/dt* = (1−2M/r)/(1+2M/r). Near the horizon this gives δ(t*) ≈ δ₀·e^{t*/(4M)}, with δ = r−2M. Here 4M = 1 (`dev/gen2p1_efbox.py:31-32`), so the e-folding time is one t* unit. An element at 2M+δ₀ only acquires an outside-like future volume if δ₀ ≳ c·e^{−(T−t₀)}. The effective boundary therefore sits at r_eff(T) − 2M ∝ e^{−T/(4M)}. This matches qualitatively the outside-horizon bracket at T=6 and the coverage from T≈10 onward. The constants c and t₀ have not been fitted. [UNVERIFIED as a quantitative fit; derivation only]
- **Relevant invariants:**
  - **Future volume** of minimal elements: primary, see above.
  - **Longest chain from minimal elements** (EGS l.181-188). This is the audited cross-check oracle `estimate_O` (`estimator.py:26-55`). Brightwell–Gregory: E[l] / (ρV)^{1/d} → m_d (Surya LRR 2019, §4.3, eq. 21; `biblioteca/derived-md/The causal set approach to quantum gravity.md` l.1221-1240). In 2+1, use d=3 scaling.
  - **Ordering fraction** r = 2R/(n(n−1)) (Surya §4.2, eq. 14, l.1000-1012; Myrheim 1978). It depends only on d in flat space. It is not needed for the decision, but is a cheap order-only sanity check that the flat control is 3-dimensional (Myrheim–Meyer d≈3) and not mis-generated.
  - **Number of minimal elements n, and the scaling that matters for (c).**
    - An element at height t above t*=0 is minimal iff its past cone within the box is empty, with probability ≈ exp(−κρt^d). The minimal elements therefore form a layer of thickness ∝ ρ^{−1/d}.
    - Count: n ∝ ρ^{(d−1)/d}·(base area). That is n ∝ ρ^{1/2}·L in 1+1 and n ∝ ρ^{2/3}·π(1.3²−0.1²) in 2+1. [UNVERIFIED constant; scaling derivation only]
    - The scored bracket [max r of low-O, min r of high-O] is a 1-D order statistic of the minimal elements projected onto r, pooled over all φ. Its spacing near r=2M is g(ρ) ≈ 1/(λ_r), where λ_r ∝ ρ^{2/3}·2π·2M is the linear r-density of minimal elements.
    - In 1+1, g ∝ ρ^{−1/2} = ell. This is exactly why the sealed anchor K_LOC·ell/2M (`thresholds.py:101-108`) is principled there.
    - In 2+1, g ∝ ρ^{−2/3}/(2π·2M), not ρ^{−1/3}. Taking the proportionality constant ≈ 1 (an assumption, not derived), this gives g/2M ≈ 0.025 at ρ=126 and ≈ 0.063 at ρ=32. The dossier reports measured widths of ~0.01-0.03·2M and ~0.05-0.13·2M respectively. That agreement is suggestive, not established. [UNVERIFIED: constant not derived; this is a dev observation and must not be used to tune]
- **Analytic / continuum target:**
  - **Primary target.** As T→∞ and ρ→∞, the bimodal split separates minimal elements exactly at r=2M (EGS l.181-191; their finite-n statement is about "large enough timelike extent", not asymptotics).
  - **Finite-T, finite-ρ target.** The bracket midpoint should approach 2M with:
    - bias ∝ e^{−T/(4M)} (the effective-horizon offset above);
    - half-width ∝ ρ^{−2/3} (the projected minimal-element spacing).
  - **Consequences for prereg-004:**
    - **(a) T.** t_min(ρ) should grow only logarithmically. Requiring bias ≲ half-width gives e^{−T/(4M)} ≲ ρ^{−2/3}, i.e. t_min(ρ) ≈ t_min(ρ_ref) + 4M·(2/3)·ln(ρ/ρ_ref).
      - Going from ρ=32 to 126 predicts an increase of about 0.9 t* units. That is consistent with the measured 8→10 on a grid of step 2 (`dev/2P1_TMIN_RHO126_RESULT_2026-10-13.md`).
      - Extrapolating to ρ=4×126 adds about 0.9 more.
      - So T=16 leaves a margin of about 5 e-folds over t_min(126)=10, and T=20 about 9. That is a principled, data-free margin argument for T∈{16,20} that does not depend on further sweeps. [UNVERIFIED beyond the tested ρ≤126]
    - **(c) θ_loc.** Anchor θ_loc to the frozen-intensity analogue of the 1+1 rule, "cannot localise finer than the order-statistic spacing": θ_loc = K_LOC·g(ρ)/2M, with g computed from the frozen intensity and the bench geometry only (as `thresholds.py:97-99` requires for ell). Do not use the dimensional transfer ell=ρ^{−1/3}, which gives θ≈1.0 at ρ=63 (DOSSIER).
  - **Flat control target.** The 2+1 Minkowski order on the same cloud has no trapped region. Its O profile has no bimodality beyond boundary effects, so the gate should abstain at rate ≥ 1−α per seed (`thresholds.py:125-135`).
- **Caveats:**
  - **θ_loc and θ_stab are vacuous if transferred dimensionally.** K_LOC·ρ^{−1/3}/2M ≈ 1.0 at ρ=63 (DOSSIER), and θ_stab = K_LOC·ell (`thresholds.py:111-113`) is likewise ≈ 0.4 in r at ρ=126. A threshold that cannot fail is decoration (first founding rule). Both must be re-anchored on the ρ^{−2/3} projected-spacing basis above, or on an analytically computed E[n_min] for the bench (a model-level integral over the box geometry, not over any validation realisation). Whichever anchor is chosen, its constant must be fixed from analysis and not read off the dev widths (`NO_POST_HOC_TUNING`). [UNVERIFIED that the constant can be derived analytically in closed form; it may need a pre-registered data-free MC on the continuum geometry]
  - **The (iv) LOO false-positive test cannot fail in 2+1 as written.** `nachocausal/validate.py:64` flags a MINK seed iff `s[i] > np.percentile(null, 95)`. The flat control abstained in 180/180 dev runs, and abstention sets sep→0 (`thresholds.py:128-129`). So all MINK seps are 0, the percentile is 0, and the strict `>` flags nothing whatever happens. The real false-positive content sits in the gate's abstention rate. Prereg-004 should state (iv) as a binomial criterion: flat-control false-localisation count ≤ k out of n seeds, with k fixed from α=0.01 and n. With 0 observed failures, the 95% upper bound is about 3/n, so a 0.05 claim needs n ≳ 60 flat seeds. [UNVERIFIED that the chair prefers this restatement; the degeneracy itself is verified from code]
  - **(i) permutation significance carries over, but needs enough seeds.** It is an exact sign-flip test for n≤20 (`thresholds.py:85-87`; `validate.py:50`, p = mean(means ≥ obs), which includes the identity). The smallest attainable p is 2^{−n}. P_PERM_THRESHOLD = 1e-4 therefore needs n ≥ 14 paired seeds per primary cell. prereg-002 used 20 (`docs/preregistration_002.md:16`). At the 2+1 GPU-dev/CPU-blind cost of ~8 min × 4 (CPU) per realisation at T=24, this sets a hard floor on seeds × intensities. (b) should be chosen so that the primary cell has ≥20 seeds on the CPU path.
  - **(d) the coverage floor ≥0.5 can fail but has little power.** The measured 0.9-1.0 at T≥10 (DOSSIER) cannot be used to raise it post hoc. Any stricter floor must come from a stated principle, e.g. the expected coverage of the order-statistic bracket under the e^{−T/(4M)} bias bound, decided before virgin data. The 1+1 precedent shows coverage falling with density (0.97→0.78, `docs/estimator_v2_freeze.md` cl. E). In 2+1 the half-width shrinks as ρ^{−2/3} while the bias is fixed by T, so coverage may fall faster with ρ at fixed T. This favours a primary endpoint at the highest frozen ρ only if T has the log-margin above. [UNVERIFIED for ρ>126]
  - **Reach of the bench and claim.** The order comes from a dimensionally reduced metric that is not an Einstein solution. Lemma E1 makes its causal order equal the 3+1 equatorial order, and the observable depends only on the order. So the claim is order-theoretically about 3+1-equatorial causal relations, but it covers finite-patch localisation only (`no_3p1_claim_from_2p1`, `NO_RECONSTRUCTION_CLAIM`).
  - **EGS boundary-sensitivity caveat.** Future cardinality "may be affected more strongly by the choice of boundary" (EGS l.193). The inner cut r=0.1 and the outer r=1.3 enter O directly. Prereg-004 must freeze the r-range exactly as sealed in 1+1 and not vary it.
  - **The ghost of the numba cache incident.** The fix (cache disabled; the GPU rerun was identical, `dev/2P1_NUMBA_CACHE_STALE_TABLES_2026-10-12.md`) must be part of the frozen CPU blind path, with a test that the T-dependent tables are rebuilt per call. Otherwise the order itself, and hence every order-only quantity, is wrong silently.
  - **Seed hygiene.** The virgin band 8_000_000..8_999_999 has never been used (DOSSIER). Draw the held-out seeds once and blind, as in prereg-002 (`docs/preregistration_002.md:14-30`), only after the θ table, the τ(n) extension hash and T are sealed (`RESPECT_SEAL_FREEZE`).

### Mathematical logic brief
- **Formal status:**
  - **Proved in Lean (`formal/HorizonFormal/`):** only order-theoretic material: ideals, accessibility, chain ends, and `relationalHorizon` as cover pairs (`HorizonFormal/Horizon.lean:80-246`). Nothing in Lean mentions 2+1, the equator, `theta_loc`, coverage, `tau(n)` or LOO. A grep over `formal/` for "equator" or "2p1" returns nothing.
  - **No prereg-004 quantity is a theorem.** T, the ρ grid, `theta_loc`, the coverage floor and (i)-(iv) are all definitions or frozen conventions.
  - **E1 (equatorial restriction) is a written proof that passed audit, not a Lean theorem.**
    - Its equivalence between the existence of curves in 3+1 and in 2+1 is the core claim.
    - Its translation into the computable `Delta_max` criterion is **conditional**: it holds only on rectangular `K` with the degenerate rule. Its key step, that the sup is attained by a maximiser, is self-marked `[INFERENCE, no formalizado aquí]` (`E1_equatorial_restriction_lemma.md` §3, around lines 85-100).
  - **The t_min values are dev empirical point estimates, not theorems.** t_min(32)=8, t_min(63)=10, t_min(126)=10, each from 10 seeds per cell. A coverage of 0.9 means 9 of 10, so the binomial uncertainty is wide.
  - **Open conjecture:** that t_min(ρ) ≤ 10 (or ≤ T_chosen) for ρ > 126. The data are non-decreasing (8, 10, 10), not decreasing (`dev/2P1_TMIN_RHO126_RESULT_2026-10-13.md:27,41`).

- **Quantifier / dependency order (required freeze order):**
  1. **Fix the ρ grid and the primary ρ\*.** Cost is a legitimate reason to choose them, outcomes are not.
  2. **Set T ≥ max over that finite grid of t_min(ρ), plateau clause included.** The domain gate must be either one constant `T_EDGE_MIN_2p1` or a frozen table indexed by ρ. The statement must be "for all ρ in the frozen grid", **never** "for all ρ".
     - The dossier itself shows bias staying roughly fixed in T while the bracket narrows with ρ. So "covers 2M" is (finite-T bias) ≤ (half-width), and that cannot hold uniformly as ρ grows.
     - If ρ\* > 126, the inequality t_min(ρ\*) ≤ T rests on an untested conjecture. A dev check at ρ\* is required before freezing, or ρ\* must be ≤ 126.
     - The plateau clause "stable on [T, 2T]" (`estimator_v2_decision_spec.md` Decision 2, clause 3) has been verified only on [10, 20] at ρ=126 (plus T=24). T=16 would need [16, 32] and T=20 would need [20, 40]. Neither is measured.
     - So T=16 or 20 is a *margin above* t_min, not a t_min that passes Decision 2. It should be labelled that way, with a separately stated margin rationale. A surface-gravity bias decay is a candidate rationale, but it is physics, not logic `[UNVERIFIED]`.
  3. **Set the expected N per ρ: N = ρ·5.278·T.** All thresholds are functions of the frozen (ρ, T, geometry) only, never of realised N or realised n_min (precedent: `thresholds.py:98-100`).
  4. **Choose the `theta_loc` and `theta_stab` anchor.**
     - **Main post-hoc entry point.** The dossier rejects ρ^{-1/3} *because* it is "near-vacuous against measured widths". That reverses the order the anchor rule requires: the anchor is meant to come before the outcome (`docs/preregistration.md:49`: "NOT reverse-engineered from the dev outcome").
     - Choosing a different anchor after seeing widths of 0.01-0.03·2M is legitimate only if the new anchor is derived *independently* of those numbers and the brief records explicitly that the choice was made knowing dev widths.
     - **Logically clean options:**
       - (α) Keep 2ρ^{-1/3}/2M and state openly that criterion (ii) is weak in 2+1. This is the same stance as the coverage floor (`estimator_v2_freeze.md` clause E).
       - (β) Derive a scale from a structural argument fixed in writing before any table of candidate values is compared with the dev widths.
     - **Non-dimensional caveat:** ρ^{-1/3} is a scale in spacetime 3-volume, while the bracket is an r-gap between minimal elements, a codimension-1 antichain. Matching the exponent to the object is a modelling choice, not a theorem `[UNVERIFIED]`.
  5. **Re-derive the τ(n) table for n > 128.** It must be regenerated by the **sealed** procedure and frozen as a literal fixture. The dev path is *not* the same procedure:
     - dev: `default_rng([GATE_NULL_MC_SEED, n])` with 4000 reps (`dev/explore_2p1_estimator.py:36-39`);
     - sealed: one shared rng, n ascending and contiguous, 40000 reps (`scripts/gen_tau_table.py:7-10,38-46`; `thresholds.py:139`).

     The dossier's "same procedure" is therefore false on two counts: the rng scheme and the number of reps.
  6. **Draw the virgin seeds from 8_000_000..8_999_999 once, after steps 1-5.**
  - **Ground truth enters T selection, and this should be stated.** The bias and coverage that choose T are scored with r=2M. That matches the 1+1 Decision 2 precedent and stays in dev only. It is allowed because the hidden embedding never enters the observable or the boundary, but "T is chosen GT-free" would be a false sentence.

- **Equivalence claims:**
  - **E1:** this is an iff on the *existence* of causal curves. It holds for any D×S² (§1).
  - **Order formula used by the generator:** the iff `x ≺ y ⟺ dist_φ ≤ min(π, sup L)` is proved only for rectangular K, non-degenerate case, and that proof contains the inference step above. The degenerate case dU=0 or dV=0 is a separate stated rule.
    - The EF box (t* × r) is **not** a (U,V) rectangle. The generator relies on the ambient order: "every causal rectangle of two points of the box lies in {V>0, UV<1}" (`dev/gen2p1_efbox.py:9-10`).
    - So the sprinkled poset is the ambient order restricted to the box, not the box's intrinsic causal order. prereg-004 should state this explicitly as the definition of the order.
  - **CPU ≡ GPU:** this is an empirical equality on the tested T values (6, 12, 16) only (`dev/validate_gen2p1_gpu.py`), not a proof. The blind run is CPU-only (`gpu_dev_only`), so no equivalence claim is needed there.
  - **(iv) LOO false positives:** under gate ties, the criterion reduces to a count. From `nachocausal/validate.py:53-66`: a seed is flagged iff it is strictly greater than `np.percentile(other MINK, 95)`.
    - If all MINK seeds abstain (sep = 0, as in 180/180 in dev), the fraction is exactly 0.
    - If m MINK seeds escape the gate with distinct positive seps, then at n=20 the condition "≤ 0.05" holds iff m ≤ 1 (m = 2 generically gives 2/20). This is derived by reading the code, not executed `[UNVERIFIED by run]`.
    - For n < 20, a single escape gives 1/n > 0.05, so the test fails. The verdict of (iv) therefore depends on the **ensemble size**, which must be frozen first.
    - Recommendation: state (iv) as the equivalent explicit count ("≤ 1 of n MINK non-abstains") so it is transparent. It is a gate check and not independent evidence (cmte C2, `thresholds.py:91`).
  - **(i) sign-flip permutation:** one-sided and exact for n ≤ 20 (`validate.py:30-50`).
    - With MINK sep = 0 and every BH sep > 0, p = 2^{-n} whatever the magnitudes. That reduces (i) to "every BH seed localises".
    - p ≤ 1e-4 can only be reached if n ≥ 14 valid seeds (2^{-13} ≈ 1.2e-4). An ensemble under 14, which the 2+1 cost may tempt, makes (i) **impossible to pass by definition**. Keep ENSEMBLE=20 and MIN_VALID_SEEDS=18 (`thresholds.py:49`).
  - **(iii) `theta_stab` = 2ℓ:** this inherits the anchor problem. With ℓ = ρ^{-1/3}, 2ℓ ≈ 0.50 in r at ρ=63, which equals 2M itself. So (iii) is as near-vacuous as (ii) and must be decided together with (ii), not separately.

- **Type / object discipline:**
  - **The scored estimand is a set-valued statistic, not a horizon.** It is a 2-means partition of the minimal-element antichain by the order-only cardinality O. It is mapped to an r-interval only at scoring (`dev/explore_2p1_estimator.py:54-66`).
  - **Four different objects are in play:**
    - the Lean `relationalHorizon`: cover pairs between an ideal's past and its black region (`Horizon.lean:127-160`);
    - the estimator's bracket: an interval in r;
    - the scoring target r=2M: a coordinate locus, the equatorial trace of the event horizon;
    - the T-dependent "effective horizon" seen at T=6 (`dev/2P1_PHASE_B_INTERIM_2026-10-12.md`).
  - The correct prereg-004 sentence is "the bracket covers r=2M in the finite 2+1 equatorial patch". It is **not** "the estimator detects the event horizon", and not an identification of the Lean relational horizon with r=2M. No Lean theorem connects these objects.
  - **ρ vs intensity:** 1+1 indexes thresholds by intensity (expected N) over a fixed BOX_AREA (`thresholds.py:41-47,101-103`). In 2+1 the volume is proportional to T, so the same ρ gives different N at different T. Thresholds must be keyed by **ρ** together with the frozen T. Mixing the "intensity" and "ρ" vocabularies risks an ℓ computed from the wrong denominator.
  - **The bench is not a 2+1 Einstein solution** (acta §6, `no_einstein_2p1_claim`). "Horizon" here means the equatorial restriction of the 3+1 Schwarzschild horizon via E1, not a 2+1 gravitational object.

- **Caveats:**
  - Dev `tau(n)` for n > 128 is not the sealed procedure (4000 vs 40000 reps; per-n vs shared rng). Every dev gate decision with n > 128 used a different τ than a correct regeneration would give. Abstain margins are probably small, but this is `[UNVERIFIED]` until the frozen table is regenerated and the dev improvement values are compared against it (`dev/explore_2p1_estimator.py:33-39`, `scripts/gen_tau_table.py:38-46`).
  - The coverage floor of 0.5 is a deliberately weak floor, not nominal coverage (`estimator_v2_freeze.md:76-81`).
    - Raising it toward the measured 0.9-1.0 would anchor a threshold to dev outcomes, the forbidden pattern (`preregistration.md:49`).
    - Keeping 0.5 is the only choice that keeps the reasoning clean, unless an a-priori rationale written *before* the 0.9-1.0 numbers is on record. None is in the dossier.
  - Expect a coverage decline with ρ, as in 1+1 (0.97 → 0.78; freeze clause E). With fixed T and shrinking width, the finite-T bias eventually exceeds the half-width. This is a structural reason the T margin must cover the primary ρ\*, not merely ρ ≤ 126 (`dev/2P1_TMIN_RHO126_RESULT_2026-10-13.md:34-35`).
  - (i) and (iv) are both near-tautological given the gate and must not be read as two independent confirmations (cmte C2, `thresholds.py:89-92`). The criteria with real content in 2+1 are (ii) and (iii), and their anchor is exactly the open item (c).
  - The convergence slack (b) `m_{k+1} ≤ m_k + ℓ_k/(2M)` (freeze clause F) needs an ordered sequence of ≥ 2 intensities, and its ℓ inherits the item (c) anchor. It must be re-stated over the frozen ρ grid at fixed T `[UNVERIFIED that prose in the dossier addresses this]`.
  - The bounded claim in the prereg-004 text must read "finite 2+1 equatorial patch localisation", with no 3+1, reconstruction or Einstein-2+1 claim (acta §6, §7). Lemma E1 transfers the *order* only, not any estimator property, to 3+1.

### Physicist brief
- **Coordinates and patch.** prereg-004 must freeze the same coordinates the dev bench uses: ingoing EF on the equatorial slice, `-(1-2M/r)dv^2 + 2 dv dr + r^2 dphi^2`, with `v = t* + r`, `sqrt(-g) = r`, `2M = 0.5`, `t* in [0,T]`, `r in [0.1,1.3]`, `phi in S^1` (`dev/gen2p1_efbox.py:6-7,31`). The order should be computed in Kruskal-type (U,V) using the E1 §3 rule: the `Delta_max` criterion when dU, dV > 0, and same-angle only when dU = 0 or dV = 0 (`research_program/puente_3p1/2026-10-12/E1_equatorial_restriction_lemma.md:85-104`).
  - **The box is not a (U,V) rectangle.** The EF box is not a (U,V) rectangle, so the poset is the ambient order restricted to the sprinkled points. Causal curves may leave the box.
  - **Why the E1 rule still applies.** The rule needs C, r > 0 on each pair's causal rectangle `[U_x,U_y]x[V_x,V_y]`. My own inference: inside the horizon (U, V > 0), UV is largest at the corner y, so r is smallest at y. Then r >= min(r_x, r_y) >= 0.1 > 0 and the rule applies. This is `[INFERENCE, not written in E1]`; prereg-004 should state it explicitly.
  - **Which horizon.** The ground-truth target is `r = 2M`, which is `U = 0` in the patch (`docs/acta_frente_2p1_ecuatorial_2026-10-12.md:41-44`).
  - **What finiteness costs.** The claim covers a finite patch only. It is not the event horizon, which needs J+ / an infinite future. Eichhorn–Gamito–Stokes note that even an infinite sprinkling cannot easily tell futureless points at J+ from those near the singularity (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:175`). They also note that in finite regions "event horizons are useless" (`:199`).
  - **Recommendation for (a).** Freeze `T = 20`. That is twice `t_min = 10` at rho = 63 and 126, and inside the plateau for all three densities (`dev/2P1_TMIN_RHO126_RESULT_2026-10-13.md:12-24`). T = 16 leaves only 1.6x margin at densities where t_min has not been measured.

- **Physical meaning of the signal.**
  - **Interior points.** All future-directed causal curves from an interior point have dr < 0. Its future is confined to `r < r_x` and is cut off by the inner edge `r = 0.1`. That edge stands in for the singularity, so the singularity-truncated future is here really an edge-truncated one.
  - **Exterior points.** An exterior point's future reaches outward and up to t* = T, so its count grows with T.
  - **Why the observable splits in two.** These two behaviours give `O = |future|` of the minimal elements its two clusters. The gap at r = 2M widens with T.
  - **Why a finite T biases the split outward.** Points just outside 2M hug the horizon for a long t* before escaping. With finite T their futures are cut off by the box top, so the split shifts outward. This is the "effective horizon" seen at T = 6: bracket at r ~ 0.51-0.57, 0/5 cover (`dev/2P1_PHASE_B_INTERIM_2026-10-12.md`).
  - **The bias does not shrink with density.** It is a continuum effect, while the bracket narrows as rho rises. So at fixed T, coverage must eventually fail as rho grows; the 1+1 decline 0.97 -> 0.78 is a precedent (`docs/estimator_v2_freeze.md` clause E).
  - **Unknown decay rate.** How fast the bias decays with T is not established. Surface gravity gives e-folding ~ 4M = 1 in t*, but the measured T=6 -> T=8 reduction looks slower `[UNVERIFIED]`. prereg-004 must not rely on an assumed decay law.
  - **It is still a dimension-dependent effect.** The sealed 1+1 bench covered at `T_EDGE = 6` (`nachocausal/thresholds.py:37`), but 2+1 does not.

- **Sprinkling domain.**
  - **Region and measure.** Poisson sprinkling, uniform in (t*, phi), density ∝ r (`dev/gen2p1_efbox.py:105-110`). Volume = `pi(1.3^2 - 0.1^2) T = 5.278 T`.
  - **The flat control is valid on the same cloud.** The same cloud is also a correct Poisson sprinkling of the flat polar annulus, whose measure is also r dt dr dphi. So the MINK control (`dt >= |x-y|`, `dev/gen2p1_efbox.py:14,356`) is a valid null on the same cloud. The flat plane is convex, so no ambient-order issue arises there.
  - **Freeze rho from constants, not from the realised N.** rho must be fixed from the frozen intensity and the fixed 3-volume, as in the 1+1 precedent (`nachocausal/thresholds.py:96-98`).
  - **Recommendation for (b).** Intensities rho in {32, 63, 126}, with the primary endpoint at rho = 126, the highest density where t_min has been measured. Any rho > 126 should be a secondary cell only: the finite-T bias is not yet measured there.
  - **Guarantees that are forfeited.** There is no t_min plateau evidence above rho = 126. Coverage at 10 seeds per cell is uncertain by ±0.1-0.15 (RHO126 result, "Límites"). The blind run is CPU-only and roughly 4x slower than the GPU dev runs; the cost at T = 20 should be checked before freezing `[UNVERIFIED wall-time]`.

- **Claim boundary.**
  - **What the verdict claims.** At most: an embedding-blind, order-only estimator localises `U = 0` (r = 2M) to within theta_loc in a finite 2+1 equatorial patch of Schwarzschild.
  - **Not reconstruction or 3+1.** It is not metric reconstruction and not an asymptotic event horizon. It is also not a 3+1 result; E1 only transfers the order on the equator (`acta:30-32`).
  - **Not a 2+1 gravity result.** The bench "is not an Einstein solution in 2+1" (`acta:31`).
  - **Regular-black-hole caveat.** Eichhorn–Gamito–Stokes argue that interior/exterior partitions based on futureless or finite-length curves "would no longer work for regular black holes" such as Hayward (`.../Towards black-hole horizons...md:195`). They propose apparent-horizon diagnostics instead (`:199`, `:467`). Our observable depends on futures being cut off at the inner edge or singularity, so the verdict says nothing about regular black holes.

- **Caveats.**
  - **(c) Proposed principled anchor for theta_loc** `[INFERENCE, dev-informed]`.
    - *Basis.* The bracket is a gap between radial order statistics of the minimal elements. These lie in a layer about one ell thick above t* = 0.
    - *Spacing.* Their radial line density at r is `rho·ell·A_perp(r)`, so the spacing is `delta_r = 1/(rho^{(d-1)/d}·A_perp)`.
    - *1+1 check.* In 1+1 (A_perp = 1) this reduces exactly to the sealed `ell = rho^{-1/2}` (`nachocausal/thresholds.py:101-108`).
    - *2+1 form.* In 2+1, A_perp = 2πr evaluated at 2M. This uses ground truth on the scoring side only, as 1+1 already does by dividing by TWO_M. The anchor becomes `theta_loc = K_LOC·delta_r/2M = 2/(2π·2M·rho^{2/3}·2M)`.
    - *Values.* About 0.126 / 0.080 / 0.051 at rho = 32 / 63 / 126. Against measured widths of ~0.01-0.03·2M at rho = 126 this is not vacuous. Against ~0.05-0.13·2M at rho = 32 it is borderline, so low-density cells could fail localisation.
    - *Disclosure.* The O(1) layer-thickness prefactor is absorbed in K_LOC = 2, as in 1+1. The derivation was made after seeing dev widths, and prereg-004 must say so. K_LOC must not be retuned.
  - **(d) Coverage floor.** I recommend keeping 0.5 as the inherited deliberately weak floor (`docs/estimator_v2_decision_spec.md:86-150`). Raising it to match the dev 0.9-1.0 would anchor the floor on observed data, which is close to tuning. The finite-T bias argument above shows coverage is expected to fall at higher rho.
  - **(e) False-positive, significance and stability.** I am not adding a physics objection. The same-cloud MINK null is geometrically valid, and the flat control abstained 180/180 in dev. Criteria (i), (iii) and (iv) have not been measured in 2+1, so carrying over the thresholds `FP_PERCENTILE = 95`, `THETA_FP = 0.05` (`thresholds.py:90-93`) is a design choice, not something checked here `[UNVERIFIED in 2+1]`. theta_stab should use the same delta_r(d) anchor as theta_loc, mirroring `thresholds.py:111-113`.
  - **Gate threshold above n = 128.** The tau(n) table for n > 128 is computed in dev (sealed `GATE_TAU_N_MAX = 128`). It must be frozen and sealed as a literal table in prereg-004 before any virgin seed (8_000_000-8_999_999) is drawn.


## 5. Falsifier attack
- **Concrete failure modes:**
  1. **(i) and (iv) carry almost no evidence in 2+1. Both reduce to "the gate behaved".**
     - (iv) cannot fail when every flat seed abstains. `loo_fp_fraction` flags a seed only when `s[i] > np.percentile(null, 95)` (`nachocausal/validate.py:53-66`). Abstention sets sep_MINK to 0 (`validate.py:97-99`). With all seps at 0 the percentile is 0, nothing is flagged, and the fraction is 0.
     - The dev flat control abstained 180/180, so as written (iv) is the count "≤1 of n_valid MINK seeds escapes the gate". Two escapes make it FAIL.
     - (i) collapses the same way. With MINK at 0 and every BH sep > 0, p = 2^-n_valid, which passes at n ≥ 14 (`validate.py:28-50`). So (i) only says "no BH seed abstained".
     - Neither may be presented as independent confirmation (`thresholds.py:89-92`, cmte C2). The verdict's real content therefore rests on (ii), (iii) and coverage, whose anchors are the open questions.
  2. **The θ_loc anchor was derived after the outcome it is meant to judge.**
     - The dossier rejects ρ^{-1/3} *because* it is "near-vacuous against measured widths". `dev/2P1_TMIN_RHO126_RESULT_2026-10-13.md` §Pendiente uses the same wording.
     - Both the mathematician and the physicist then derive ρ^{-2/3}·(2π·2M)^{-1}. The mathematician notes it "agrees" with the dev widths (0.025 vs 0.01-0.03 at ρ=126). The physicist states the derivation was made after seeing the widths.
     - This is the pattern `docs/preregistration.md:49` forbids ("NOT reverse-engineered from the dev outcome").
     - The exponent may well be right: the minimal-element layer argument reduces to the sealed ρ^{-1/2} in 1+1. Even so, the constant and the evaluation point are free choices:
       - the prefactor ≈ 1 is "assumed, not derived";
       - A_perp is taken at r=2M rather than, for example, the mean perimeter 2π·0.7. That choice changes θ by ×1.4.
     - Each such choice moves θ relative to widths already seen.
  3. **The (ii) convergence slack and "significance at every N≥3000" have no 2+1 definition.**
     - `validate.py:183-198` uses `ell_over_2M` from the 2D `ell` keyed on the 1+1 intensity/`BOX_AREA = T_EDGE*R_EDGE` (`thresholds.py:42,101-103`). None of the four briefs freezes the 2+1 replacement. The logic brief flags it only as `[UNVERIFIED]`.
     - If the slack inherits ρ^{-1/3}, then ℓ/2M ≈ 0.63 at ρ=32. That slack cannot fail.
     - The "≥3000" significance clause has no 2+1 counterpart on a ρ grid. Leaving it undefined lets it be filled in after the run.
  4. **The T margin rests on two contradictory decay claims.**
     - The mathematician argues e^{-T/4M}: "5 e-folds of margin at T=16". The physicist says the measured T=6→8 decay is slower and that prereg-004 "must not rely on an assumed decay law".
     - Rough check: the T=6 bracket offset (~+0.01 to +0.07 in r, `dev/2P1_PHASE_B_INTERIM_2026-10-12.md`) against T=8, ρ=126 bias +0.0116 gives a factor of about 1-6. The prediction is e^2 ≈ 7.4.
     - The Decision-2 plateau clause [T, 2T] is unmeasured for T=16 ([16,32]) and T=20 ([20,40]) (logic brief).
     - So the T margin is an untested extrapolation and should be labelled as one.
  5. **Coverage is already imperfect, and the 0.5 floor has little power.**
     - In the ρ=126 sweep, 11/60 records have `low_O_all_inside: false`; in the ρ=32/63 sweep, 30/120 do (grep over `dev/2p1_sweep_T_rho126_v2_2026-10-12.jsonl` and `dev/2p1_sweep_T_v2_2026-10-12.jsonl`). In those records the bracket sits at an exterior point, i.e. outward bias. The counts span all T, including the T=6/8 regimes.
     - On those seeds, (ii) width still scores whenever width ≥ 0. "Clean" in the sealed scorer means only width ≥ 0 (`nachocausal/scoring/scorer.py:42-45`). A narrow, mislocated bracket therefore passes θ_loc and fails only coverage.
     - With floor 0.5 and n=20, up to 9 mislocated seeds still PASS. Prereg-004 should report the coverage count verbatim and not let a "PASS" headline hide it.
  6. **The sealed τ procedure differs from the dev one, and dev gate verdicts used the dev τ.**
     - Dev: 4000 reps with a per-n rng (`dev/explore_2p1_estimator.py:33-39`). Sealed: a single stream with 40000 reps (`scripts/gen_tau_table.py:38-46`).
     - Dev n_minimal reaches 184 at ρ=126, above `GATE_TAU_N_MAX=128`.
     - The smallest dev gate margins are 0.037 for MINK (τ − improvement) and 0.036 for BH (improvement − τ), same grep. These are probably larger than the Monte Carlo noise of a p99 quantile at 4000 reps, but this is `[UNVERIFIED]` until the table is regenerated.
     - A larger ρ* would push n past any fixture and trigger the OUT_OF_DOMAIN/abort path.
  7. **Cost pressure could edit the grid.** A CPU run at T=20, ρ=126 (N≈13300) is roughly 4× the GPU minutes, times 20 seeds, times 3 ρ. That is `[UNVERIFIED]`, likely many hours. If the runtime is not frozen in the prereg, the temptation is to drop ρ cells or seeds after launch. Below 14 valid seeds, (i) becomes impossible to pass by construction.
  8. **T read from an environment variable.** `T_EDGE = float(os.environ.get("NC2P1_T_EDGE","6.0"))` (`dev/gen2p1_efbox.py:29`), and the z-tables are built from T at import (:43-53). If the variable is missing, the run silently uses T=6, a regime where localisation is known to go wrong.

- **Ground-truth leakage:**
  - **Observable:** no path found. In the dev code, `estimate()` receives only `order`, and `score()` is the only place r appears (`dev/explore_2p1_estimator.py:42-66`). The sealed 1+1 runner freezes `thr` from O before revealing r (`validate.py:100`).
  - **Thresholds:** three paths where ground truth reaches the choice of thresholds.
    - (a) The physicist's θ_loc evaluates A_perp = 2π·r *at r = 2M*. The hidden horizon radius therefore sets the threshold's scale, not merely its unit as TWO_M does in 1+1. This is scoring-side, so it is not technically a breach, but it must be declared. A ground-truth-free form (perimeter averaged over [0.1,1.3]) should be considered *and chosen before* comparing either against dev widths.
    - (b) T is selected using bias and coverage scored against r=2M. The 1+1 Decision-2 precedent permits this, but "T chosen GT-free" would be false (logic brief).
    - (c) The plan to "measure the five prereg-002 criteria in the candidate configuration" on dev (`2P1_TMIN_RHO126_RESULT` §Pendiente 2) turns ground-truth-scored dev pass/fail into feedback on θ, unless θ, K_LOC and the evaluation point are frozen first.
  - **Port:** the sealed port must keep the order-only Guard-v and the split dict (repro brief). Dev records mix the estimate and the score in one dict.

- **Freeze violations:**
  - **Smuggled in now:** none of the briefs proposes touching virgin seeds 8_000_000+ or the 1+1 seal (`make verify-seal` = `6e2c3888…`, dossier).
  - **Live risks:**
    - (1) Choosing among ρ^{-1/3}, ρ^{-2/3}·(2π·2M)^{-1} and ρ^{-2/3}·(2π·0.7)^{-1}, or any prefactor, with dev widths in view is post-hoc anchor selection (`NO_POST_HOC_TUNING`). The brief must record a commitment (anchor, K_LOC=2 unchanged, evaluation point) *before* dev criteria are evaluated, and must state that this happened with the dev widths already known.
    - (2) Raising the coverage floor from 0.5 toward the measured 0.9-1.0 would be tuning. Lowering it is forbidden (`NO_THRESHOLD_LOOSENING`).
    - (3) If T is chosen in dev at a ρ* > 126 and then re-swept because coverage looked weak, that is a fresh-seed rerun. Unused exploration seeds may be used, but every sweep must be declared before it runs, as 88a25f6 was.
    - (4) The OUT_OF_DOMAIN/config-error relaunch rule must be frozen. A relaunch is allowed on the *same* seeds only if no scoring output was produced. Otherwise a mis-set T could buy a second look.

- **Verdict coercion:**
  - **INCONCLUSIVE inherits a hiding route.** A BH abstention makes the seed invalid (`validate.py:104-107`), and fewer than 18 valid seeds gives INCONCLUSIVE (`validate.py:131-133,172-176`). A detector that fails to detect on ≥3 of 20 seeds therefore reports INCONCLUSIVE, not FAIL.
  - **Generator seed-invalidation adds a second route.** The repro brief would also count generator assertion failures as seed-invalid. Both routes collapse into the same INCONCLUSIVE.
  - **What prereg-004 must freeze:** report the BH-abstain count and the generator-invalid count separately and verbatim, and decide in advance whether BH abstention ≥ k is a FAIL of (i)/(ii).
  - **The domain gate is decorative.** With T frozen at 16/20 and `T_EDGE_MIN_2p1` re-pinned to about 10, it can never fire in the blind run. That is fine, but it must not be cited as an extra safeguard.
  - **OUT_OF_DOMAIN must stay a separate status.** If T is the 6.0 env default and T_EDGE_MIN is *not* re-pinned (the inherited 6.0, `thresholds.py:121`), the run proceeds in-domain in a regime known to localise wrongly. So: re-pin, hard-code T, and keep OUT_OF_DOMAIN distinct (`validate.py:162-170`).

- **Premature / over-broad claims:**
  - "Detects the event horizon": the target is r=2M in a finite box. Bias at T=6 shows the estimator tracks a T-dependent *effective* boundary (Phase-B interim).
  - "3+1 result": E1 transfers the order on the equator only, and its computable form is conditional (`E1_equatorial_restriction_lemma.md` §3, self-marked `[INFERENCE]`).
  - "2+1 gravity": the bench is not an Einstein solution (acta §6).
  - "Scaling ρ^{-2/3} confirmed": the constant is assumed, and the fit is a dev observation.
  - "t_min ≤ 10 for all ρ": untested above ρ=126, and the data are non-decreasing (8, 10, 10).
  - Allowed wording: "finite 2+1 equatorial patch localisation within frozen θ on the frozen ρ grid".

- **Independent-falsification gate:** not satisfied.
  - The same operator and chair ran the sweeps, wrote the dossier's framing ("near-vacuous against measured widths"), and will author prereg-004.
  - Two wave-1 experts converged on an anchor with those widths in view. Their agreement is not independent.
  - /auditor has not run on any 2+1 artefact. The only independent check is ASTRA on E1, and it was conditional.
  - Minimum before freezing:
    - an independent derivation of the θ_loc constant and its evaluation point, written blind to the dev width table;
    - /auditor on the 2+1 package (τ fixture SHA, hard-coded T, guard port) before the virgin seeds are drawn.

- **Minimal falsification test:** a pre-freeze "guardrails can fail" test, `test_004_criteria_can_fail`, run against the ported 2+1 `validate` on **already-used exploration seeds only**, with its verdict discarded. It feeds three known-bad inputs and asserts each yields **FAIL** (not PASS, INCONCLUSIVE or OUT_OF_DOMAIN):
  - (a) the ρ=126, T=8 exploration cell (known coverage 0.20, `dev/2P1_TMIN_RHO126_RESULT_2026-10-13.md`), with the domain gate bypassed in the test only. Expected: `ii_localisation_primary` is false.
  - (b) a synthetic MINK sep vector with 2 of 20 non-zero. Expected: `iv_false_positive_primary` is false.
  - (c) the T=20, ρ=126 dev bracket widths scaled ×(θ_loc/median+ε). Expected: `loc_pass` is false.

  Alongside it, regenerate τ(n) for n ∈ [129, n_max(ρ*)] by the sealed single-stream procedure at 40000 reps. Assert that n ≤ 128 is bit-equal to `tau_table.json`, and recompute the dev gate margins: no BH or MINK verdict may flip.

  If (a), (b) or (c) does not FAIL, the criterion is decoration and prereg-004 must not be frozen.


## 6. Pre-registration verdict
- Verdict: BLOCK (on launching any 2+1 validation run now). Drafting and freezing prereg-004 is allowed once the conditions below are met. The step is not yet frozen, so no run may start.
- Freeze status: NOT frozen. HEAD eeaf4c7 has no `docs/preregistration_004.md` (DOSSIER). Every item (a)-(e) is still open design. The only frozen material is the sealed 1+1 package (`docs/preregistration_002.md:7-9`) and the inherited forms in `docs/preregistration_002.md` ("Frozen analysis"). Those carry 1+1 numbers: T_EDGE_MIN=6, tau(n) with n<=128, the K_LOC*rho^{-1/2} anchor. None of them is a 2+1 threshold. A prereg-004 file must be committed before the seed draw. It must name T and its margin, the rho grid and primary endpoint, theta_loc and theta_stab with derivations, the coverage floor, the (i)/(iii)/(iv) criteria, the tau fixture SHA, the ENSEMBLE and MIN_VALID_SEEDS values, and the draw seed. This mirrors the structure of `docs/preregistration_002.md:1-70`.
- Seal integrity: The 1+1 seal must stay untouched. `make verify-seal` must print `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (the same value as `docs/preregistration_002.md:7-9`, confirmed by the chair this session). I agree with the reproducibility engineer's brief that the 2+1 instrument needs its own sealed sub-package and its own thresholds file with its own SHA. `nachocausal/thresholds.py` must not be edited. The 2+1 seal record must also list the SHAs of the imported 1+1 modules (estimator, gate). The tau(n) table for n>128 must be regenerated by the SEALED procedure: one shared rng, n ascending, 40000 reps, and a check that n<=128 reproduces `tau_table.json` bit-for-bit. The dev procedure (per-n rng, 4000 reps, `dev/explore_2p1_estimator.py:36-39`) is not the same procedure, as the mathematical logic brief shows. Dev tau values must not be reused. The T literal must replace the `NC2P1_T_EDGE` env knob (`dev/gen2p1_efbox.py:29`) before sealing, and numba cache must stay off. The blind run is CPU-only (acta `gpu_dev_only`), and CPU/GPU parity at the frozen T must be shown first. Parity is shown only at T=6, 12 and 16 (DOSSIER). That is an extra reason to prefer T=16 over T=20 unless T=20 is parity-checked.
- Seed discipline: Use the virgin band 8_000_000..8_999_999 (`dev/gen2p1_efbox.py:VIRGIN_BAND`), never used (DOSSIER). Draw 20 seeds once and blind. Fix the draw seed in the prereg BEFORE drawing, with the recipe numpy(1.26.4).default_rng(seed).choice(arange(8e6, 9e6), 20, replace=False) as in `docs/preregistration_002.md:14-30`. Add a runnable disjointness guard against EXPLORE_BAND (7_000_000..7_000_999, with used sub-ranges listed in the DOSSIER) and the burned Phase-A seeds 1,2,3,4,7,99,12345. The prereg-001 and prereg-002 seeds are already burned. No virgin seed may be touched during dry-run. Dry-run uses exploration-band seeds with the verdict discarded (the `nachocausal/dry_run.py` pattern). The draw happens only after the theta table, the tau fixture hash and T are sealed.
- Reporting rule: Confirmed only if the prereg text repeats the `docs/preregistration_002.md` binding clause. PASS, FAIL, INCONCLUSIVE and OUT_OF_DOMAIN are reported alike. There is no re-run on fresh seeds after a result. There is no loosening of a frozen threshold. Seed-invalid events (generator assertion, transitivity violation, radial-check mismatch) count toward the <18/20 INCONCLUSIVE rule and never trigger replacement seeds. A crash is relaunched on the SAME seeds, env and commit, and logged. results/validation_004.json is written atomically and committed at once (lesson of the PRIMARY_ARTIFACT_LOST status). Wall-clock cost and the crash rule are stated up front so duration cannot justify changing the grid later.
- Forbidden moves present? Not yet executed, but three are live risks that the prereg must neutralise explicitly.
  - Post-hoc anchor (`NO_POST_HOC_TUNING`). The dimensional-transfer anchor was rejected because it is "near-vacuous against measured widths" (DOSSIER). That reverses the order required by `docs/preregistration.md:49` ("NOT reverse-engineered from the dev outcome") and by `docs/preregistration.md:55-57` ("unmet principled thresholds are informative... not a licence to loosen"). The physicist's delta_r anchor (0.126/0.080/0.051 at rho=32/63/126) was derived after seeing dev widths, and the physicist says so. If it is adopted, it is a re-anchoring made with knowledge of dev outcomes. It is admissible only if all of the following hold. The structural derivation is written in the prereg first. K_LOC=2 is inherited and not retuned. The disclosure sentence "chosen knowing dev widths" is included. The alternative of keeping 2*rho^{-1/3}/2M, with an honest "criterion (ii) is weak in 2+1" note, is recorded as the conservative option. The bracket-width-matching constant must not be read off dev. A rho=32 cell that fails localisation under the new anchor is reported as a FAIL, not repaired.
  - Coverage floor (`NO_THRESHOLD_LOOSENING`). Keep 0.5 as inherited (`docs/preregistration_002.md`, "Localisation (ii)"). Raising it toward the dev 0.9-1.0 would anchor a threshold to dev outcomes. Lowering it is forbidden. Both the physicist and the logic brief agree.
  - Ground truth. T is chosen by dev scoring against r=2M. This must be stated honestly (GT only scores, never defines the observable). Do not write "T is chosen GT-free". The sealed validate must separate estimator output from scoring (`dev/explore_2p1_estimator.py:40-64` mixes them) with a Guard-v analogue that can fail (`NO_GROUND_TRUTH_LEAKAGE`).
  - Reconstruction over-claim (`NO_RECONSTRUCTION_CLAIM`). The text must read "finite 2+1 equatorial patch localisation". It must not claim 3+1, an event horizon, metric reconstruction, an Einstein-2+1 result or regular black holes.
- Reasons:
  - Founding rule 1 (anchoring, `docs/preregistration.md:46-56`). Every theta must be a function of frozen (rho, T, geometry) only, never of realised N or n_min (`nachocausal/thresholds.py:96-100`). Key them by rho together with the frozen T, not by the 1+1 "intensity" over BOX_AREA. Otherwise the 1+1 vocabulary silently uses the wrong denominator.
  - Domain and T. T_EDGE_MIN=6 is a mis-localising regime in 2+1 (`dev/2P1_PHASE_B_INTERIM_2026-10-12.md`). The 2+1 domain gate must be a new frozen constant at or above the t_min of the frozen grid, and it must not be inherited. T must be labelled a "margin above t_min", not a Decision-2 pass. The plateau clause [T,2T] is verified only on [10,20] at rho=126 (logic brief). Claims hold for the frozen grid only. The best-supported choice is a primary rho* <= 126 (measured t_min = 8/10/10). A primary rho* > 126 requires a dev check at rho* BEFORE freezing; otherwise it is only a secondary cell. T=16 versus T=20 is a cost-and-parity decision. Margin arguments for either rest on an e-folding derivation that is `[UNVERIFIED]` as a fit (mathematician brief), so no decay-law claim should enter the prereg.
  - Intensities and cost. Keep ENSEMBLE=20 and MIN_VALID_SEEDS=18 (`thresholds.py:49`). With sign-flip permutation, p=2^{-n} needs n>=14 for p<=1e-4, so fewer seeds make (i) impossible to pass. The rho grid and primary endpoint are chosen on cost grounds and fixed before the draw, never on outcome. Convergence slack (freeze clause F) must be restated over the frozen rho grid at fixed T, and the grid needs at least 2 values.
  - (iv) is degenerate. With all MINK seps = 0, `nachocausal/validate.py:64` flags nothing (strict `>` against percentile 0), so it cannot fail as written. Restate it in the prereg as an explicit count (for example, flat-control non-abstentions <= 1 of 20, matching the 0.05 form), and say openly that (i) and (iv) are gate-derived and not independent confirmations (cmte C2, `thresholds.py:89-92`). Do not drop (iv). Strengthening it with a binomial bound needs more flat seeds, so state the limit honestly and do not tune it. The real discriminating content is (ii) and (iii), and both depend on the unsettled anchor (c). theta_stab must use the same anchor as theta_loc and be decided together with it.
  - E1 and order definition. The order is the ambient order restricted to the sprinkled box points, not the box's intrinsic order. Lemma E1 passed audit conditionally. Its maximiser step is self-marked `[INFERENCE]`, and the extension to the EF box (r>=0.1 on each causal rectangle) is the physicist's own inference. Both must be stated as assumptions. REL_MARGIN/TOL and the audit count are frozen as part of the sealed bench. A thread-determinism check (NUMBA_NUM_THREADS=1 versus the default) is a pre-flight item `[UNVERIFIED]` today.
  - Audit trail. `/auditor` was not run, and the dossier justifies this: no published 2+1 claim underlies the step. Even so, prereg-004 must cite the 1+1 estimator PASS status with its caveats (PRIMARY_ARTIFACT_LOST; BLINDNESS_DOCUMENTARY_ONLY). The committee brief must pass `make verify-comite` before the seal commit.
  - Condition to lift BLOCK. All three of the following are in place, in this order: (1) the prereg-004 document, the sealed 2+1 thresholds file and the tau fixture are committed with the SHAs recorded, git status clean, `make verify-seal` unchanged; (2) the preflight is green (tests, dry-run on exploration seeds, CPU timing, CPU/GPU parity at the frozen T); (3) the user explicitly authorises the single `validate` run.


## 7. Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| EGS (arXiv:2605.06813), derived-md l.175: futureless points at J+ cannot be told from those near the singularity, even with an infinite sprinkling | Physicist | CONFIRMED (l.175; the arXiv ID appears in biblioteca/fuzzy_ladders_comprehensive_literature_review.md:40 and :520, not in the paper's own md) |
| EGS l.181-193, minimal elements, longest chain, and the bimodal split by future cardinality (Fig. 3 lower panel, "Again, the distribution is bimodal") | Mathematician | CONFIRMED (the bimodal sentence is at l.193; the longest-chain text and Fig. 3 are at ~l.181-191) |
| EGS l.193: future cardinality "may be affected more strongly by the choice of boundary" | Mathematician | CONFIRMED (l.193; the paper's example is a causal diamond, where the future cardinality varies between n and √n already in Minkowski) |
| EGS l.188-191: gap "widens with T", and interior futures are bounded uniformly in T while exterior futures grow roughly linearly in T | Mathematician | UNCONFIRMED. The paper says the longest-chain jump grows more pronounced with larger timelike extent (l.191). For the future-cardinality variant it states only bimodality, with no widening claim and no linear growth. The mechanism is the expert's inference, not a quotation. |
| EGS l.195: the interior/exterior partition "would no longer work for regular black holes" (Hayward type) | Physicist | CONFIRMED (l.195; the paper says "likely", and the Hayward case is 3+1) |
| EGS l.199: "event horizons are useless" in finite regions; apparent-horizon diagnostics are proposed instead | Physicist | CONFIRMED (l.199; the paper's wording is "In practical calculations with finite regions of black-hole spacetimes, e.g., in numerical relativity, event horizons are useless") |
| EGS l.467: proposed alternative diagnostics | Physicist | CONFIRMED (l.467 is the conclusion paragraph on ladders and geodesic expansion, used there to locate the apparent horizon) |
| Surya LRR 2019 ("The causal set approach to quantum gravity"), eq. 14, ordering fraction r = 2R/(n(n−1)), Myrheim 1978, l.1000-1012 | Mathematician | CONFIRMED on content and lines (eq. 14 at l.1007-1009; "r depends only on the dimension" is stated). The section label is wrong: the equation is in §4.1 "Spacetime dimension estimators" (l.986), not §4.2. §4.2 is "Topological invariants" (l.1157). |
| Surya LRR 2019 §4.3, eq. 21, Brightwell–Gregory: l/(ρV)^{1/d} → m_d, l.1221-1240 | Mathematician | CONFIRMED (§4.3 at l.1221; eq. 21 at l.1233; Brightwell and Gregory 1991 at l.1228). The expert's "E[l]/(ρV)^{1/d}" is consistent with the text's "expectation value ... limits to". |
| Myrheim–Meyer d≈3 as a sanity check for the flat control | Mathematician | CONFIRMED as a general result (Surya §4.1, l.986-1012). The application to the 2+1 flat control is the expert's proposal, not a literature claim. |
| Brightwell–Gregory scaling "in 2+1 use d=3" | Mathematician | CONFIRMED as the d-dependent constant m_d (eq. 21). Its use for the minimal-element layer scaling n ∝ ρ^{2/3} is the expert's own derivation, which the expert itself marked [UNVERIFIED]. |
| Dimensional-scaling derivations (bias ∝ e^{−T/4M}, g ∝ ρ^{−2/3}, ρ^{(d−1)/d} layer) | Mathematician, Physicist | UNVERIFIED. No biblioteca source was cited for them. Both experts mark them as derivations, and no biblioteca source for them was found in this check. |
| Brightwell–Gregory 1991, Myrheim 1978 and Meyer 1988 as primary papers | Mathematician | UNVERIFIED as primary sources. They were checked only through Surya's review. |
| Other repo-internal citations (Logician, Reproducibility): the 0.97→0.78 coverage decline | Logician, Physicist, Mathematician | CONFIRMED at docs/estimator_v2_freeze.md:80 ("coverage 0.97→0.78 over ρ=208→3333, Finding 4"), but it is cited as "clause E". The "deliberately weak floor" text is at docs/estimator_v2_freeze.md:76-81, which is the Decision 1 section. The "clause E" attribution is a repo-internal label that I did not check against the file's lettering (the visible lettering is "G. Remaining criteria"). |

- Notes:
  - Overall, every biblioteca citation resolves to a real document and to approximately the cited lines. Only the section label for Surya eq. 14 (§4.1, not §4.2) was wrong.
  - The one claim that goes beyond its source is the Mathematician's use of EGS l.188-191 for "gap widens with T" and for "future volume bounded uniformly in T / roughly linear in T". The paper makes the widening statement only for the longest-chain observable, and for cardinality it states only bimodality. The ρ- and T-scaling mechanism is therefore an unanchored derivation. The brief should not present it as EGS-backed.
  - No biblioteca source supports the 2+1 bias decay law or the ρ^{−2/3} spacing law that the anchors for (a) and (c) depend on. The committee should treat those as unanchored.
  - EGS treat only 1+1 Schwarzschild sprinklings. Nothing in biblioteca supports a 2+1 or 3+1 extension of the cardinality observable, and EGS flag its boundary sensitivity (l.193). This favours the Mathematician's caution to freeze the r-range (0.1 to 1.3).
  - The arXiv ID 2605.06813 is not in the paper's own derived md. The ID is attested in biblioteca/fuzzy_ladders_comprehensive_literature_review.md:40 and :520.


## 8. Synthesis
Recommended direction, ranked alternatives, and **open disagreements (never hidden)**. If a
pre-registration BLOCK or an unresolved falsification exists, the verdict cannot be a PROCEED
verdict.
**Recommended direction: do not freeze prereg-004 yet.** The two controls make a PROCEED verdict impossible:
- the warden **BLOCKs** any 2+1 validation run until prereg-004 and its instrument are sealed;
- the falsifier's **independent-falsification gate is not satisfied**.

What the committee *does* converge on is a concrete design skeleton, plus a short list of pre-freeze obligations. Once those are met, the design can be reconvened and frozen.

**Converged design elements** (all seven roles, or no dissent recorded):
1. **Instrument.**
   - A new sealed 2+1 sub-package with its own thresholds and seal. `nachocausal/thresholds.py` is never edited, and `make verify-seal` stays `6e2c3888…`. The 2+1 seal record also lists the SHAs of the imported 1+1 modules.
   - T is a hard-coded literal: no `NC2P1_T_EDGE` env knob, numba cache off.
   - REL_MARGIN, TOL and the audit size are frozen.
   - The blind run is CPU-only, with exact pins for numba, llvmlite and scipy.
   - The estimator and the scorer are split, with a Guard-v analogue that can fail.
2. **τ(n) for n > 128.**
   - Regenerate it with the **sealed** procedure (single stream, n ascending, 40000 reps) up to n_max at the top frozen ρ. Assert bit-equality with `tau_table.json` for n ≤ 128, and freeze it as a hashed fixture.
   - Recompute the dev gate margins against it; no verdict may flip. Dev τ values are never reused.
3. **Seeds.** ENSEMBLE = 20 and MIN_VALID_SEEDS = 18, inherited. With fewer than 14 valid seeds, (i) is impossible by construction. Draw once, blind, from the virgin band 8_000_000..8_999_999, after everything else is sealed, with a runnable disjointness guard.
4. **ρ grid.** {32, 63, 126}, primary ρ* = 126. ρ* ≤ 126 is the highest density with measured t_min. Any ρ > 126 is at most a secondary cell, and only after its own declared dev t_min check.
5. **T** is a **margin above t_min** (max over the grid = 10), labelled as such and **not** as a Decision-2 pass. The plateau [T, 2T] is unmeasured for T = 16 and T = 20, and no decay law enters the prereg.
6. **The coverage floor stays at 0.5** (no raising toward the dev 0.9-1.0, no lowering). The coverage count, the BH-abstain count and the generator-invalid count are reported verbatim and separately.
7. **(i) and (iv) are gate-derived.**
   - (iv) is restated as an explicit count: flat-control non-abstentions ≤ 1 of 20.
   - Neither criterion is presented as independent confirmation.
   - The discriminating content is (ii), (iii) and coverage.
8. **Undefined 1+1 clauses get explicit 2+1 definitions before freezing.** These are the convergence slack (F) and "significance at every N ≥ 3000". They are restated over the frozen ρ grid at fixed T.
9. **The domain gate `T_EDGE_MIN_2p1`** is re-pinned at ≥ 10. The inherited 6 is a mis-localising regime. The gate is acknowledged as non-firing at a frozen T ≥ 16, so it is not counted as a safeguard. OUT_OF_DOMAIN stays a distinct status.
10. **Claim wording:** "finite 2+1 equatorial patch localisation within frozen θ on the frozen ρ grid". There is no claim about the event horizon, 3+1, reconstruction, Einstein 2+1 or regular black holes. Two things are stated as assumptions: the ambient order restricted to the box, and the two inference steps of E1 and its extension to the EF box.

**Ranked alternatives for the open item (c), the θ_loc / θ_stab anchor:**
- **(c1, recommended) A structural ρ^{-2/3} spacing anchor, independently re-derived.**
  - The exponent comes from the minimal-element layer argument, which reduces exactly to the sealed ρ^{-1/2} in 1+1 (mathematician, physicist).
  - The constant and the **evaluation point** must be fixed by a derivation written **blind to the dev width table**, by a party other than the chair: for example an ASTRA turn given the geometry and the 1+1 rule only. The ground-truth-free evaluation point (mean perimeter over [0.1, 1.3]) is preferred over A_perp at r = 2M (falsifier).
  - K_LOC = 2 is unchanged, and the prereg carries the disclosure "chosen with dev widths already known".
  - θ_stab uses the same anchor.
- **(c2, conservative) Keep the dimensional transfer 2ρ^{-1/3}/2M,** and state openly that (ii) and (iii) are weak in 2+1. This is the same stance as the 0.5 coverage floor (logic brief α, warden).
- **Rejected:** any anchor whose constant is read off the dev widths, or a choice among candidate anchors made by comparing them with dev widths (`NO_POST_HOC_TUNING`).

**Open disagreements (not resolved here):**
- **T = 16 vs T = 20.**
  - The physicist recommends 20 (twice t_min).
  - The warden leans to 16: CPU/GPU parity is shown only at T ≤ 16, and the cost is lower.
  - The mathematician's log-margin argument supports either, but the literature verifier finds that argument unanchored. The physicist and the falsifier also doubt its decay rate.
  - Either value needs CPU/GPU parity and CPU timing at that T before freezing.
- **Whether ≥ k BH abstentions should be a FAIL rather than INCONCLUSIVE.** The falsifier raises this hiding route; no role proposes a k. The user must decide it before freezing.
- **The anchor (c1 vs c2), and whether c1 needs a blind re-derivation.** The falsifier and the warden require it; the mathematician and the physicist offered their derivation as sufficient.
- **The mathematician's EGS citation for "the gap widens with T"** is UNCONFIRMED for the cardinality observable (literature verdict). Their ρ^{-2/3} and e^{-T/4M} laws are unanchored derivations. They may motivate the design but must not be cited as literature-backed.


## 9. Next-step spec
The sequenced plan, separating **reversible** steps (may be run now if the user asks) from
**committing** steps (only on explicit user authorisation), with the binding rules pre-committed
and the falsifier's minimal falsification test included:
**Reversible (may run now if the user asks; nothing touches the virgin band or the 1+1 seal):**
1. **τ fixture.** Regenerate τ(n) up to n_max at ρ = 126 and T = T_candidate, using the sealed single-stream procedure with 40000 reps, as a dev artefact. Assert that n ≤ 128 is bit-equal to `tau_table.json`. Recompute every dev gate margin; flips are reported, not fixed.
2. **Blind θ derivation.** Commission an independent derivation of the (c1) constant and its evaluation point. The deriver sees the geometry, the 1+1 rule and the minimal-element layer argument, but **not** the dev width table. Record it before any comparison.
3. **2+1 sub-package.** Port it with:
   - hard-coded T, cache off and frozen tolerances;
   - the split between estimator and scorer, plus a Guard-v analogue;
   - a 2+1 definition of the convergence slack and of the significance clause;
   - (iv) as a count;
   - separate abstain and invalid counters;
   - atomic result writing.
4. **`test_004_criteria_can_fail`** (the falsifier's minimal falsification test), run on already-used exploration seeds only, with the verdict discarded. Three cases must each give FAIL:
   - (a) ρ = 126, T = 8 (coverage 0.20), with the domain gate bypassed in the test → (ii) false;
   - (b) a synthetic flat control with 2 of 20 escapes → (iv) false;
   - (c) widths scaled just above θ_loc → loc_pass false.

   If any case does not FAIL, that criterion is decoration and prereg-004 is not frozen.
5. **Pre-flight at the candidate T and ρ\*:**
   - CPU/GPU order parity;
   - CPU wall-clock per realisation, so the full-run runtime can be stated in the prereg;
   - a thread-determinism check (`NUMBA_NUM_THREADS=1` vs the default).
6. **`/auditor` on the 2+1 package:** τ fixture SHA, hard-coded T, guard port and seed guard.
7. **Reconvene `/comite`** on the concrete prereg-004 draft, with T, the anchor and the BH-abstention rule decided by the user.

**Committing (only on explicit user authorisation, after steps 1-7 are green):**
- **C1.** Commit `docs/preregistration_004.md` together with the sealed 2+1 thresholds and the τ fixture (SHAs recorded), with `make verify-seal` unchanged and the tree clean.
- **C2.** Draw the 20 virgin seeds once and blind, with the draw seed fixed in the prereg beforehand.
- **C3.** The single blind CPU run.
  - Its result is reported alike whatever it is.
  - There is no rerun on fresh seeds.
  - A crash is relaunched on the same seeds, env and commit, only if no scoring output was produced, and the relaunch is logged.


## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_

**Decisions the PI took on the open forks (2026-10-13, in chat, transcribed by the chair):**
- **T = 16.** It is labelled a margin above t_min = 10. CPU/GPU parity at T = 16 was already shown.
- **θ_loc / θ_stab anchor: (c1).** The structural ρ^{-2/3} spacing anchor, with its constant and evaluation point **re-derived blind** to the dev width table by a party other than the chair. K_LOC = 2 stays unchanged, and the prereg discloses that the choice was made knowing the dev widths.
- **BH abstention rule:** **≥ 3 BH abstentions out of 20 = FAIL** of criterion (i), not INCONCLUSIVE. INCONCLUSIVE stays reserved for generator-invalid seeds.

**Decisions the PI took on the prereg-004 draft open items O1-O8 (2026-10-14, one by one in a Claude Code session, transcribed by Claude):**
- **O1.** `VALIDATION_DRAW_SEED_004 = 20261014`.
- **O2.** Step 5 accepted as partial (parity on 1 of 10 seeds; the dev pairwise parity at T = 16 and port = dev bit-equality stand in for the rest; no thread probe).
- **O3.** The blind run uses 20 numba threads, enforced in code.
- **O4.** A per-seed progress log with blind fields only is added before C1.
- **O5.** The four step-3 interpretations confirmed, including `p_perm` with an abstained BH as `sep = 0`, knowing that 1+1 excludes such seeds.
- **O6.** The four step-4 deviations accepted.
- **O7.** The §8 recommendations as transcribed in `nachocausal2p1/thresholds.py` (`[C052-n]`) signed, and the two `[PI-S3]` clauses signed.
- **O8.** Blind review by `revision-ciega gemini` authorised; not yet run.

Detail and pointers: `docs/preregistration_004_draft.md` §10.

The verdict (`RECOMMEND_REVISE_AND_RECONVENE`) and the authorisation of the committing steps (C1-C3) have not yet been signed.
