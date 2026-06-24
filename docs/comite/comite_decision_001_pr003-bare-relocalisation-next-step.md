# Comité Decision 001 — pr003-bare-relocalisation-next-step

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Tras cerrar la "única pregunta siguiente" de PR-003 con veredicto exploratorio
**`BARE_RELOCALISATION`** (6 semillas; `dev/measure_truncated_head.py`,
`dev/PR003_NEAR_HORIZON_NOTES.md`, `docs/hoja_de_ruta_23_jun_2026.md` punto 1), ¿de qué modo
deberíamos seguir? La cabeza conexa adherente a O(ℓ) existe pero es solo el vecindario de
discreteness de la semilla (k\* = O(1) rungs 3/2/3; k\*·ℓ se halva con ℓ, 0.134→0.067); `rel_phi`
no marca el fin de la cabeza de forma estable; el contraste greedy quedó sin potencia (n=2/8/1).
`k*` NO es regla order-only (se lee de `d_⊥`). Decisión de frontera, no *committing* aún; no
congelar nada.

## 2. Verified state

Facts checked **this session**, each with its command / file:line.

- **Seal intact.** `make verify-seal` → `thresholds.py sha256 =
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, which **matches** the frozen
  reference in `docs/preregistration_002.md`. `RESPECT_SEAL_FREEZE` holds.
- **Git.** Branch `main` @ `fcbf0bb`. Working tree (uncommitted): `M README.md`,
  `M dev/PR003_NEAR_HORIZON_NOTES.md`, `M docs/hoja_de_ruta_23_jun_2026.md`; untracked
  `dev/measure_truncated_head.py` and `cpp/`. No commit made.
- **Frozen results present.** `docs/preregistration_001_result.md` = **FAIL**;
  `docs/preregistration_002_result.md` = **PASS** (order-only localisation of the
  horizon-associated boundary in a finite 1+1D patch, blind, sealed).
- **Status of the verdict under discussion.** `BARE_RELOCALISATION` is **dev exploration** — not
  sealed, not (until this session) independently checked. The dev sweep used intensities
  3600/7200/14400 (DEV regime), distinct from the sealed prereg-002 grid (1500/3000/6000/12000).
- **Chair ran the falsifier's minimal test this session** (reversible, read-only, `EXPLORE_POOL[0]`
  only): complete-fraction per density = **89% / 93% / 87%**; tail (k≥10) `d_⊥/ℓ` on COMPLETE-only
  ladders = **6.21 / 8.95 / 10.07** vs ALL = 6.00 / 9.11 / 8.23. → the tail growth is **not** a
  search-budget artifact; it persists under complete-only aggregation. The falsifier's central
  failure mode is **refuted by data**.

## 3. Dossier

Files and references supplied to the committee:

- Exploration just closed: `dev/measure_truncated_head.py`, `dev/PR003_NEAR_HORIZON_NOTES.md`
  (§"Single-next-question measurement (2026-06-24)"), `dev/truncated_head.log`.
- Roadmap & gate: `docs/hoja_de_ruta_23_jun_2026.md` (point 1), `docs/pr003_leakage_gate.md`
  (5 contracts).
- Prior PR-003 dev machinery: `dev/measure_pr003.py` (`boundary_minimals_invariant`,
  `longest_censored`, `reconstruct`), `dev/explore_direction.py` (`greedy_ladder`,
  `order_only_heights`, `rel_field`), `dev/explore_ladders.py`, `dev/measure_near_horizon.py`,
  `dev/sweep_near_horizon_density.py`, `dev/explore_seeds.py` (`EXPLORE_POOL`, reserved bands).
- Sealed instrument: `docs/preregistration.md`, `docs/preregistration_002.md` + result,
  `docs/estimator_v2_seal.md` / `_freeze.md`, `nachocausal/{thresholds,estimator,generator,
  validate}.py`, `Makefile` (`verify-seal`/`dry-run`/`test`/`audit`).
- Literature: Eichhorn–Gamito–Stokes arXiv:2605.06813 (`biblioteca/` + `derived-md/`),
  Surya LRR 2019, Bombelli 1987, Myrheim 1978.

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief
- **Proposed artefact(s):** A new dev measurement script, e.g. `dev/measure_orderonly_truncation.py`, living beside the existing PR-003 dev scripts (`dev/measure_truncated_head.py:1`, `dev/measure_pr003.py`, `dev/explore_direction.py`). It must reuse the same imports already vetted in `dev/measure_truncated_head.py:47-52` (`generator`, `thresholds`, `explore_seeds.EXPLORE_POOL`, `explore_ladders`, `explore_direction.{greedy_ladder,order_only_heights,rel_field}`, `measure_pr003.{boundary_minimals_invariant,longest_censored}`). Spec, not code: the script must (1) define the candidate stopping rule purely on order observables (the `rel_phi`/`Lfut`/`Lpast` family from `explore_direction.order_only_heights`/`rel_field`), with `d_perp` consumed ONLY for the score read-off exactly as at `dev/measure_truncated_head.py:87`, never inside the cut; (2) report whether an order-only breakpoint coincides with the observed k*=O(1). Findings append to `dev/PR003_NEAR_HORIZON_NOTES.md` and the closed point in `docs/hoja_de_ruta_23_jun_2026.md`. NOTHING in `docs/preregistration_*` or `nachocausal/thresholds.py` is touched — this is dev, not a prereg.
- **Environment & seal:** Validation/dev-measure path is pure numpy pinned `numpy==1.26.4` (`requirements.txt:7`); the project's own `nachocausal` package is sufficient — these `dev/measure_*` scripts do NOT need the external Minz clone (the Minz/`~/cs-horizon-reuse-check/venv_minz`, numpy<2 note in `CLAUDE.md:26-29` applies only to `dev/prototype_o.py`, not here). Before and after the run, re-verify the seal with `make verify-seal` and confirm it still prints `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching the frozen reference at `docs/preregistration_002.md:8` and `docs/estimator_v2_seal.md:7`. Package-diff-clean check: `git status --short` must show no `M nachocausal/` and no `M docs/preregistration_*` after the run — only the dev artefact + notes.
- **Provenance capture:** The run must record: commit (`fcbf0bb`, branch main, with the pre-existing dirty set `M README.md`, `M dev/PR003_NEAR_HORIZON_NOTES.md`, `M docs/hoja_de_ruta_23_jun_2026.md`, untracked `cpp/` + the new script); `pip freeze` (assert `numpy==1.26.4`); `uname -a`; the exact seed band used — must stay inside `EXPLORE_POOL` (`dev/explore_seeds.py:23`, `1_000_000..1_000_039`) and MUST NOT touch `RESERVED_002_LO..HI` `[2_000_000, 2_999_999]` (`dev/explore_seeds.py:25-32`) nor any burned `VALIDATION_SEEDS`; intensities (the existing `{3600,7200,14400}` sweep, `dev/measure_truncated_head.py:201`); start/end timestamps. The script already prints per-density wall-clock (`dev/measure_truncated_head.py:140`) — keep that.
- **Run mechanics:** Single foreground invocation, `python3 dev/measure_orderonly_truncation.py` (smoke first: `--smoke` = 2 seeds × {3600,7200}, mirroring `dev/measure_truncated_head.py:198-199`). The full 6×3 sweep is short (prior run printed per-density seconds), so no background job is warranted. A guard aborts cleanly by: running `dev/explore_seeds.py`'s hygiene asserts (`dev/explore_seeds.py:37-42`) as a pre-flight — if any chosen seed falls in the reserved/burned bands it raises before sprinkling. Reversible pre-flight = the measurement run + `make verify-seal` + `make test` (bit-exact regression + leak + seed-invariant, `Makefile` `test` target); these touch nothing frozen. The committing step (NOT taken here) would be any edit to `nachocausal/thresholds.py`, a new `docs/preregistration_003.md`, or a sealed run on reserved seeds — none of which this step performs.
- **Reproducibility risks / ambiguities:**
  - The proposed order-only cut is exactly the missing piece flagged in the DOSSIER: k* is currently read off `d_perp` (hidden geometry, `dev/measure_truncated_head.py:87,130-136`), so it is a diagnostic, not a rule. Any artefact must pass all 5 leakage contracts in `docs/pr003_leakage_gate.md` (pure-order input, no scoring import, relabel invariance, order-only blind seeding, no score feedback) — verifiable, but the script SPEC alone cannot guarantee them; a relabel-invariance check (à la `boundary_minimals_invariant` / `measure_pr003.py:191`) must be wired in. [anchored]
  - `rel_phi` is reported AMBIGUOUS/UNSTABLE (no density-robust breakpoint; extremum at k~5 past k*=O(1)) per the DOSSIER verdict — so an order-only truncation rule may simply not exist at the needed scale; the measurement risks confirming a null. This is a scientific risk, not a provenance one, but it bounds what the run can claim. [anchored: DOSSIER, dev/PR003_NEAR_HORIZON_NOTES.md]
  - Greedy contrast is UNDERPOWERED (n=2/8/1 ladders ≥ min_len=6, `dev/measure_truncated_head.py:67` `min_len=6`); widening seeds within `EXPLORE_POOL` (40 available, only 6 used) is the cheap, reversible way to add power WITHOUT burning reserved seeds. [anchored]
  - [UNVERIFIED] I have not opened `nachocausal/dry_run.py` to confirm `make dry-run` discards its verdict on DEV seeds; the Makefile comment asserts it ("verdict discarded") but the brief does not require running it for this dev step.
  - [UNVERIFIED] untracked `cpp/` appeared in the working tree; I did not inspect it. If any proposed run depends on a compiled `cpp/` artefact rather than the pure-numpy package, that breaks the "runs on the project's own nachocausal package" guarantee and must be ruled out before the run.

### Mathematician brief
- **Computability.** Everything the closed exploration touches is decidable on the order relation `C` alone. `boundary_minimals_invariant` (dev/measure_pr003.py:163) is a function of the future-volume multiset `{|fut(i)| : i minimal}` — pure column sums of `C` (nachocausal/estimator.py:128), permutation-invariant (verified by Guard-v, estimator.py:164). The fuzzy ladder (EGS Def 2, derived-md "Towards black-hole horizons…":245, conditions 4-5 = interval-cardinality gate `M-1 ≤ |[a,b]| ≤ 2M-1`) and `longest_censored`/`greedy_ladder` (dev/measure_pr003.py:60, dev/explore_direction.py:37) run on the link (covering) matrix `L = C ∧ ¬C²` and interval cardinalities, all order-only. The poset is a strict **partial** order, not total; the longest-chain DP (`order_only_heights`, dev/explore_direction.py:74) is the single-source longest path on the transitively-closed DAG, well-defined because acyclicity is asserted (estimator.py:73). The abstaining `τ(n)` gate (thresholds.py:131-141) is data-independent (frozen MC quantile of `improvement(O_min)` under a Uniform null at matched `n` = #minimals), so the "no boundary claimed" branch is itself order-only and decidable. **Caveat:** `longest_censored` returns a *lower bound* unless `complete=True` (measure_pr003.py:140); the budget/lmax-bounded path is **not** relabel-invariant (measure_pr003.py:11-12) — only a completed search is.
- **Order observable carrying the horizon signal.** Two order-only fields, both EGS's diagnostics rendered coordinate-free: (i) the future longest-chain height `L_fut(e)` and its companion `L_past(e)` (dev/explore_direction.py:74), which is EGS's interior/exterior separator — "the length of the longest timelike curves … organized by the r-coordinate … separates the minimal antichain into horizon-interior (short) and horizon-exterior (long)" (EGS Fig. 3 + Fig. 14 caption, derived-md:186,450); (ii) the future **volume** `O(i)=|fut(i)|=Σ_j C[j,i]` on minimals, with a 1-D 2-means split (`two_means_split`, estimator.py:80) giving the bracket. The relevant continuum closed form is the cylinder/diamond volume: in the near-horizon optical patch the past-volume `O` is monotone in `r`, so its level-set crossing localises `r_S`; the height field is the Brightwell–Gregory longest-chain proper-time proxy `T ∝ ℓ · (longest chain)` (Surya LRR 2019 §4, derived-md "The causal set approach…":132,430). The #2 feature `relphi_mean = mean rel_field(L_fut, L_past)` (explore_direction.py:86) is "exteriority relative to time-depth," and empirically separates direction (AUC ~0.94) but has no near-horizon support (1-2 positives) — provisional only.
- **Relevant invariants.** Ordering fraction `r = 2|≺|/(n(n−1))` → Myrheim–Meyer dimension (Surya §4, derived-md:1010,1052); longest-chain/height (Brightwell–Gregory; proper-time proxy, Surya §4 derived-md:430,1038); future-volume `|fut(i)|` (the frozen estimator-v2 observable, estimator.py:113; docs/estimator_v2_freeze.md); interval cardinality `C_k`/`|[a,b]|` (the abundance/Benincasa–Dowker family, derived-md "Towards…":245, conditions 4-5). All are permutation-invariant functions of `C` — the leakage gate's contract 3 (docs/pr003_leakage_gate.md:45-49).
- **Analytic / continuum target.** The 1+1D Schwarzschild **outgoing radial null geodesic at r = r_S** — the bifurcate Killing/event horizon, which in 1+1D coincides with the apparent horizon `Θ_out(r_S)=0` (EGS derived-md:225). The step should approach a connected order-only chain whose hidden `d_⊥ = |r − r_S|` stays `O(ℓ)` over an extent that *grows* with `t*` (affine parameter) as `ρ→∞`. **The continuum forbids this for any single tracer:** the horizon is marginally *unstable*, `δ=(r−r_S)` grows with affine parameter, the outgoing-null angle must be infinitely fine-tuned, so probability of a ladder staying on `r_S` is zero and tracers "peel off after a few rungs" (EGS derived-md:443,474). EGS's own remedy is **not** one longer ladder but an **iterated piecewise** construction — "identify another antichain to the future of the first … a piecewise discrete horizon as the union of the ladders" (EGS derived-md:443, explicitly left to future work).
- **Caveats.**
  - The decision question's two horns are not symmetric: a single order-only quantity that *lengthens the adherent head past the seed floor is ruled out at the continuum level* — peel-off is `O(1)` rungs by the marginal instability of `r_S` (EGS derived-md:443). The measured `k* = O(1)` rungs with `k*·ℓ` halving as `ℓ` halves (PR003 notes:101-119) is exactly this floor, consistent with prereg-002 bracket re-localisation, not a defect to be tuned away. [anchored]
  - Therefore "intrinsically `O(ℓ)`" is the correct reading for a *single* tracer; the order-theoretically open and *not-yet-measured* route is **iteration**: re-seed a fresh order-only bracket on an antichain to the future of the head and concatenate (EGS derived-md:443). This is computable (same `O`/ladder machinery, re-applied) and stays inside the leakage gate **iff** the re-seed uses only `C`-derived antichains and `r` never feeds back (gate contract 5, docs/pr003_leakage_gate.md:60-65). [anchored — proposal, NOT yet built]
  - `k*` as used is **not** an order-only stopping rule — it is read off hidden `d_⊥` (PR003 notes:125; measure_truncated_head.py:130). Any frozen truncation must come from an order observable; `rel_phi` does **not** currently provide an aligned, density-robust breakpoint (extremum at k≈5, past `k*`≈2-3; PR003 notes:128-136). So an order-only *cut* is unproven independent of whether a longer segment exists. [anchored]
  - The greedy contrast is `n=2/8/1` — statistically empty (PR003 notes:138-145); it cannot adjudicate "short because adherent vs short because stuck." [anchored]
  - Whether `d_⊥/ℓ` tail growth (5.2→6.5→8.2) is true *physical* divergence is **undetermined** with three densities: `ℓ` roughly halves over the sweep, so physical `d_⊥` may still shrink (sub-`O(ℓ)`); scaling exponent unmeasured (PR003 notes:70-73). Do not over-read the tail as proof the body leaves the horizon in physical units. [anchored]
  - `[UNVERIFIED]` I did not re-execute any script; all numbers are read from dev/PR003_NEAR_HORIZON_NOTES.md and the chair's pasted state, not regenerated. Anything built next is DEV exploration — nothing here is sealed, frozen, or audited (RESPECT_SEAL_FREEZE; the iteration idea must pass `/comite` + the leakage gate before any committing measurement).

### Physicist brief
- **Coordinates & patch:** The step must use the **advanced Eddington–Finkelstein** coordinates `(t*, r)` already frozen into the generator: `func = r + 2*r_S*log(|r - r_S|/r_S)` with the EF BH causality of `past_matrix_fast` (nachocausal/generator.py:104, 115–127), `r_S = 2M = 0.5`, `M = 0.25` (nachocausal/thresholds.py:40,43). This is exactly EGS's choice — they sprinkle the `(t*, r)` induced 1+1D metric and note `det g` is constant so coordinate-uniform Poisson = natural-volume Poisson (EGS md:130–135; generator.py:10–12). The patch is the **frozen finite box** `T_EDGE=6, R_EDGE=1.2, R_CENTER=0.7` → `r ∈ [0.1, 1.3]` spanning `r_S=0.5`, area 7.2 (thresholds.py:37–41). What finiteness forfeits: there is no `J^+` and no future-inextendible curve of infinite length, so the **asymptotic/global event horizon is not available** — EGS define `H_c` via an infinite-length curve and explicitly retreat to "a causal set of finite size, because this is all that is available in practice" using *longest-chain truncation* of singularity-bounded interior futures (EGS md:175–181). Any claim is therefore an **apparent-horizon-flavoured local patch of `r=2M`**, never the global horizon.
- **Physical meaning of the signal:** The order-only observable tracks `r=2M` through **singularity-truncated futures**: timelike curves from minimal elements *inside* the horizon must reach `r=0` in finite proper time, so their **longest future chain is bounded (short)**; exterior minimal elements have **long futures**. This interior-short / exterior-long bimodality is EGS's interior/exterior diagnostic (EGS md:181), and the project's order-only proxy is the longest-future-chain field `φ = L_fut(e)` and its relative form `rel_phi` (dev/explore_direction.py:4–6,75; "interior short, exterior long"). The fuzzy ladder is the discrete analogue of a near-horizon null congruence; "tracking the horizon" means a connected chain staying at `r≈r_S`, and `r=2M` is precisely where EGS's outgoing null expansion `Θ_out` vanishes (marginally outer trapped surface; EGS md:225). Critically, `r=r_S` is a **marginally unstable** null orbit: any `δ=(r−r_S)` of an outgoing geodesic grows with affine parameter, so ladders "peel off" after a few rungs — discreteness guarantees no exact fine-tuning onto the horizon (EGS md:443,474). This is the continuum reason the measured longest-ladder tail `d_perp/ell` grows (4.37→6.17→7.56; dev/PR003_NEAR_HORIZON_NOTES.md:58): the body is *expected* to drift off, not adhere.
- **Sprinkling domain:** Declared region is the single tall box above; **Poisson** intensity drawn per seed (`rng.poisson(intensity)`, generator.py:48), same point cloud for BH and MINK differing only in causality (generator.py:42–43; SAME_CLOUD, thresholds.py:54). Frozen intensities `(1500,3000,6000,12000)`, primary 12000 (thresholds.py:46–47); the dev sweep used 3600/7200/14400 (DEV regime only, dev/PR003_NEAR_HORIZON_NOTES.md:6,51,91), with `ell = (intensity/area)^{-1/2}` ∝ intensity^{-1/2} so density doubles each step. Coordinate-uniformity is guarded (Glue-3 chi-square, generator.py:53–82) — this can fail. **Forfeited guarantees:** the dev sweep is NOT sealed and NOT on the frozen intensity grid; `ell` must be computed from the *frozen* intensity, never realized N, or the thresholds stop being literal constants (thresholds.py:96–97). [UNVERIFIED] no per-seed dispersion was emitted, so the 7200 `k*=2` wobble cannot be attributed to seed variance vs. a real density effect (dev/PR003_NEAR_HORIZON_NOTES.md:98–99,124).
- **Claim boundary:** Answering the decision question directly — **the O(ell) adherent head does NOT refute PR-003's aim; it bounds the achievable physical scale.** A reconstructible "piece of horizon" in this finite 1+1D patch has a near-horizon coherence length set by *two* scales: the discreteness floor `ell` below (you cannot localise finer than ~ell, K_LOC=2, thresholds.py:98) and the **instability length** of the marginally-unstable null orbit above (peel-off after a few rungs, EGS md:443,474). The measured head `k*·ell ≈ 0.134→0.067` (≈13–27% of `R_S=0.5`) that **halves as ell halves** (dev/PR003_NEAR_HORIZON_NOTES.md:104–105,116–119) is the physical signature of `ell`-floor localisation — i.e. **prereg-002 bracket localisation re-appearing at the seed**, NOT a lengthening reconstructed segment. So the verdict `BARE_RELOCALISATION` claims **order-only localisation of `r≈2M` to discreteness precision in a finite 1+1D patch** and claims NOT: a fixed-physical-length horizon segment, a *growing/extended* reconstructed horizon, metric reconstruction, the asymptotic/global horizon, or 3+1D (NO_RECONSTRUCTION_CLAIM honoured). EGS's own route to a longer horizon is **iterative re-seeding of successive antichains** — "left to future work" (EGS md:443) — meaning a single connected ladder is *not expected* to extend; PR-003's growing-segment target is the open question, and the bare result neither achieves nor forecloses it. **Regular-black-hole caveat (from the paper):** the longest-chain (singularity-truncated-future) diagnostic that gives this whole order-only signal works *only because* Schwarzschild is geodesically incomplete; for a regular (Hayward-type) black hole interior timelike curves can be arbitrarily long, so the interior/exterior partition by future-length "likely does not" hold (EGS md:164,195). The result is intrinsically tied to the singular toy model.
- **Caveats:**
  - `k*` is **NOT order-only**: it is read off the hidden `d_perp = |r − r_S|/ell`, a SCORE-ONLY diagnostic. It is a *geometric* statement, not an estimator output — anchored dev/PR003_NEAR_HORIZON_NOTES.md:125–126. Any frozen truncation rule must be defined on the causal order alone; embedding may only score (NO_GROUND_TRUTH_LEAKAGE; docs/hoja_de_ruta_23_jun_2026.md:78–87).
  - The order-only end-of-head marker `rel_phi` is **AMBIGUOUS/UNSTABLE**: extremum at k≈5 sits *past* the geometric `k*`=2–3 and its scale/sign are not density-robust (≈0 → −65 → −102) — so there is no order-only stopping rule yet (dev/PR003_NEAR_HORIZON_NOTES.md:128–136). PR-003 cannot freeze a truncation rule on this as-is.
  - The advance over EGS is **blindness**: EGS seeded/selected the horizon ladder using the embedding coordinate slope to pick outgoing (EGS md:390,441; "we use the embedding information... selecting a ladder that starts very close to r=r_S and that is outgoing"). Ours must seed from the order-only v2 bracket and select order-only, or it collapses to EGS's assisted proof-of-principle (docs/hoja_de_ruta_23_jun_2026.md:18–20,78–81).
  - The dev sweep is exploration, not sealed/audited; the frozen seal (`6e2c3888…`) and the prereg-002 PASS are the only committing claims (DOSSIER VERIFIED STATE; thresholds.py top). No threshold here may be loosened or back-fit to the sweep outcome (NO_POST_HOC_TUNING, RESPECT_SEAL_FREEZE).
  - **Recommendation:** proceed per roadmap as **acotación**, not refutation — pursue EGS's iterative re-seeding (md:443) as the physical mechanism for an *extended* horizon, with a density-sweep convergence test of `d_perp/ell` and an order-only stopping rule, all gated by the leakage checklist and `/comite` before any seal (docs/hoja_de_ruta_23_jun_2026.md:48,68–73,107–113).

## 5. Falsifier attack

> Note (chair): the falsifier's **minimal test was run this session** and its central failure mode
> (tail growth = search-budget artifact) was **refuted** — complete-fraction 89/93/87%,
> complete-only tail ≈ all tail (see §2). The remaining points stand as binding caveats.

### Falsifier attack
- **Concrete failure modes:**
  - **(A) over-claims "EXPECTED continuum behaviour".** The O(ell) head / drifting tail is presented (Wave-1 (A); PHYSICIST brief) as the *predicted* marginally-unstable peel-off (EGS md:443,474). But the dev run does **not** measure peel-off; it measures the tail of `longest_censored`, which is a **search-budget artifact, not a geodesic**. `longest_censored` returns `best_len` and a `complete` flag (`dev/measure_pr003.py:140-141`), and the docstring is explicit: "otherwise it is a **LOWER BOUND**" (`measure_pr003.py:16,53-54`). In the head script, `collect()` captures `comp` (`measure_truncated_head.py:82`) but **never filters or reports on it** — every profile/k* number pools complete and budget/lmax-truncated ladders together (`measure_truncated_head.py:89,101-110`). At intensity 14400 the run took 1758 s (`truncated_head.log:20`) with `budget=30000, lmax=120` (`measure_pr003.py:198`); there is no evidence the longest searches completed, so the "tail grows 5.2→6.5→8.2" trend (`truncated_head.log:22`) may be tracking **where the DFS budget ran out at higher density**, not a physical drift. The "EXPECTED continuum" reading is [UNVERIFIED] against this confound. *[Chair: TESTED — refuted; complete-fraction 87-93%, complete-only tail ≈ all tail.]*
  - **k* is admittedly a hidden-geometry diagnostic, yet it carries the verdict.** The notes concede "`k*` is **NOT** an order-only rule … read off `d_perp`" (`PR003_NEAR_HORIZON_NOTES.md:125-126`; `measure_truncated_head.py:87` `# TRUTH — score only`). So BARE_RELOCALISATION is a verdict about a *truth-defined* quantity. That is acceptable as scoring, but the proposal's framing "the O(ell) head is the expected behaviour, NOT a refutation" silently upgrades a hidden-coordinate diagnostic into a continuum-physics claim. The only order-only observable offered (`rel_phi`) is "AMBIGUOUS/UNSTABLE", with the extremum at k≈5 **past** k*=2-3 (`PR003_NEAR_HORIZON_NOTES.md:130-135`). There is therefore **no order-only evidence** that any "head" boundary even exists.
  - **(C) "widen seeds for power" is underpowered for the one thing it targets.** The greedy contrast (the *only* in-codebase order-only truncation) reached min_len on n=2/8/1 ladders (`truncated_head.log:10,18,26`); the n=1 tail of 0.88 at 14400 "supports nothing" (`PR003_NEAR_HORIZON_NOTES.md:143-145`). Widening seeds inside EXPLORE_POOL increases longest-ladder count but does nothing to guarantee greedy power, and the 7200 k*=2 wobble is "unattributable" because **no per-seed dispersion was emitted** (`PR003_NEAR_HORIZON_NOTES.md:97-99`; PHYSICIST brief). More seeds without per-seed variance reporting buys precision theater, not power.
  - **(B) iterative re-seeding is the highest-risk route and the briefs admit the mechanism that makes it pass is unverified.** MATHEMATICIAN: re-seed is inside the gate "**iff r never feeds back**". That is exactly leakage-gate contract #5 (`docs/pr003_leakage_gate.md:60-65`) and it is the EGS trap (md §V.B; gate "Por qué existe", lines 11-16). No artifact yet demonstrates the concatenation is order-only and feedback-free; it is "left to future work (EGS md:443)" (PHYSICIST). Proposing it as "the open route" while the feedback-free property is unproven is a forward-leaning over-claim.
- **Ground-truth leakage:** The dev run **scores** with `d_perp = |emb[p,1]-R_S|/ell` (`measure_truncated_head.py:87`) — coordinate, correctly score-only. The danger is in route (B): EGS's re-seeding selects/seeds with the embedding slope (PHYSICIST: "EGS seeded/selected with embedding slope md:390,441"). If the "antichain to the future of the head" is chosen using anything derived from where the *previous* head landed in `r`, the embedding has entered **selection**, violating gate contracts #1 and #5 (`pr003_leakage_gate.md:35-41,60-65`). Also latent: `k*` itself is read off `d_perp` (`measure_truncated_head.py:130-136`); if any future "order-only truncation rule" is calibrated to reproduce that `k*`, that is `r` guiding the observable through the back door (gate FAIL list, `pr003_leakage_gate.md:69-72`). The REFERENCE band `ADH=3.0` (`measure_truncated_head.py:56`) is currently a label only — but the moment a truncation rule is tuned to land at 3 ell, it becomes a truth-derived threshold.
- **Freeze violations:** Nothing frozen was touched (seal `6e2c3888…fefd4` matches, verified above). But three smuggling risks:
  - **Intensity-grid divergence from the sealed prereg.** prereg-002's primary endpoint is **intensity 12000** with grid inherited from the addendum (`preregistration_002.md:53,56`). The dev sweep used **3600/7200/14400** (`measure_truncated_head.py:201`), which **excludes 12000**. Reading a "halving-with-ell" trend (`truncated_head.log:34`) off a dev-only grid and then importing it into a narrative about the prereg-002 floor risks comparing across non-matching grids. Keep BARE_RELOCALISATION strictly dev and do not let this grid back-propagate into any sealed comparison.
  - **Re-run-on-fresh-seeds-after-seeing-a-result.** (C) widening seeds *after* seeing k*=3/2/3 is textbook post-hoc seed expansion. It must stay in EXPLORE_POOL[ already-burnt indices ] disciplined; the reproducibility brief flags that RESERVED_002 [2_000_000,2_999_999] must NOT be touched (`dev/explore_seeds.py:28`). Any reach beyond EXPLORE_POOL = `NO_GROUND_TRUTH_LEAKAGE` burn of validation seeds.
  - **No-feedback ordering not verified.** Gate #5 requires measure→freeze→score (`pr003_leakage_gate.md:60-65`). The reproducibility brief admits "did not verify `make` dry-run discards dev verdict." Until that is shown, a dev verdict could silently leak into a frozen artifact.
- **Verdict coercion:** The exploratory verdict logic is **asymmetric in favor of the benign reading**. The read-off in `run()` has three branches (`measure_truncated_head.py:183-192`): GROWS, tracks-ell-down, or ~constant. The data hit "tracks ell down → SEED RE-LOCALISATION." But the `complete`-flag confound (above) means a fourth possibility — "tail is a budget artifact, undetermined" — has **no branch** and cannot be emitted. The MATHEMATICIAN concedes the tail "may still be sub-O(ell) physically (undetermined, 3 densities)" and the notes say scaling is "**undetermined** with three densities" (`PR003_NEAR_HORIZON_NOTES.md:73). Yet the headline verdict BARE_RELOCALISATION reads as a clean negative-but-expected outcome rather than INCONCLUSIVE. The honest status of the order-only channel (`rel_phi` AMBIGUOUS, greedy UNDERPOWERED) is an **abstain**, and folding it under a tidy BARE_RELOCALISATION label is a silent abstain→FAIL-flavored collapse. prereg-002's own machinery has explicit INCONCLUSIVE (<18/20) and OUT_OF_DOMAIN states (`preregistration_002.md:57`); the dev verdict has no comparable abstain channel.
- **Premature / over-broad claims:** Route (B) "piecewise discrete **horizon**" (Wave-1 (B)) edges toward a reconstruction claim — `NO_RECONSTRUCTION_CLAIM`. The notes are careful ("no reconstructed horizon *segment*", `PR003_NEAR_HORIZON_NOTES.md:147-149`), but the Wave-1 framing of an "iterative re-seeding into a piecewise discrete horizon" is exactly the language the benchmark forbids. The PHYSICIST correctly bounds it: finiteness "forfeits asymptotic/global horizon," and the result is order-only localisation in a finite 1+1D patch. Any claim beyond "finite-patch 1+1D order-only **localisation** at the discreteness floor" overreaches. The REGULAR-BH caveat (works only because Schwarzschild is geodesically incomplete, EGS md:164,195) further restricts generality — this is **not** evidence about regular black holes, and must not be stated as such.
- **Independent-falsification gate:** **Not satisfied** at brief time. The exploration script, its verdict, and the notes are one authored artifact; there is no independent re-derivation of the tail-growth or k* numbers, and crucially the `complete`-flag confound was never checked by anyone — the author who wrote `comp` into the tuple (`measure_truncated_head.py:89`) is also the one who never filtered on it. Per the gate, `/comite` (falsifier + warden) and `/auditor` are the required independent checks before any freeze (`pr003_leakage_gate.md:74-79`); none has run on this dev result. Author == sole verifier here. *[Chair: partially remedied — the falsifier's completeness confound was independently tested this session and refuted; a full `/auditor` remains required before any freeze.]*
- **Minimal falsification test:** ONE read-only check exposes the worst failure (tail "growth" being a search-budget artifact rather than continuum peel-off). Re-aggregate the **existing** run's per-rung profile **conditioned on `complete==1`** and report the complete-fraction per density (uses `comp = r[3]` already stored at `measure_truncated_head.py:89`). If a large fraction of the 14400 longest ladders are `complete==0` (budget/lmax-hit), the tail 8.2 is a **lower-bound / search-budget readout**, not a physical drift, and Wave-1 (A)'s "EXPECTED continuum peel-off" claim collapses — the tail trend would then be **undetermined**, downgrading BARE_RELOCALISATION to INCONCLUSIVE on its central quantitative claim. This is the single highest-leverage check and it requires no new seeds, no writes, and nothing frozen. **→ RUN BY CHAIR THIS SESSION: complete-fraction = 89%/93%/87%; complete-only tail (k≥10) = 6.21/8.95/10.07 ≈ all-ladder 6.00/9.11/8.23. The artifact hypothesis is REFUTED; the tail growth in ℓ-units is real. (Whether it is *physical* divergence remains undetermined — an independent caveat, not the artifact.)**

## 6. Pre-registration verdict

**Verdict: PASS**

- **Freeze status:** No thresholds are frozen for this step, and none are required — it is an
  explicitly DEV/exploratory measurement with no committing run and no sealed data. The future
  freeze of PR-003 rules #2/#3 is explicitly deferred (`docs/hoja_de_ruta_23_jun_2026.md:45`
  "Punto 2 — congelar: pendiente"; lines 71-73 "Solo entonces congelar… vía /comite, y sellar").
- **Seal integrity:** The step does not execute the sealed validation path, does not touch
  `nachocausal/thresholds.py` or `docs/preregistration_*.md`. Seal SHA
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (confirmed against
  `docs/preregistration_002.md:8`) remains unmolested.
- **Seed discipline:** Seeds restricted to `EXPLORE_POOL = 1_000_000..1_000_039`
  (`dev/explore_seeds.py:23`), disjoint from `DEV_SEEDS`, `VALIDATION_SEEDS`, and the virgin
  `RESERVED_002` band `[2_000_000, 2_999_999]` (machine-checked `_assert_hygiene()`,
  `explore_seeds.py:36-45`). Prereg-002 virgin seeds untouched.
- **Reporting rule:** Dev-exploratory findings only; the binding PASS/FAIL/INCONCLUSIVE "report
  alike" rule (`preregistration_002.md:63-68`) is not yet triggered (no frozen prereg run here).
  The roadmap records `BARE_RELOCALISATION` without softening (`hoja_de_ruta_23_jun_2026.md:50-66`).
- **Forbidden moves present? No.** `NO_POST_HOC_TUNING` (no threshold exists to tune; rules #2/#3
  not frozen — measure-then-freeze order honoured, `hoja_de_ruta:89-96`); `NO_THRESHOLD_LOOSENING`
  (`thresholds.py` read-only); `NO_GROUND_TRUTH_LEAKAGE` (embedding enters only post-build for
  `d_perp`, `measure_truncated_head.py:87,94`; gate contracts 4-5); `NO_RECONSTRUCTION_CLAIM`
  (recoverability benchmark, `hoja_de_ruta:14`); `RESPECT_SEAL_FREEZE` (seal intact, single blind
  run not launched).
- **Reasons:** Step is within the dev lane (`hoja_de_ruta:115-119`); leakage gate
  (`docs/pr003_leakage_gate.md`) is the governing checklist and its 5 contracts are compatible
  with the proposed step (step does not yet *claim* to pass the gate — that verification is the
  obligation before freezing #2/#3); EXPLORE_POOL hygiene is an executable failure
  (`explore_seeds.py:36-45`); the only committing steps (freeze #2/#3, PR-003 plan) require a new
  `/comite` and are not taken here (`hoja_de_ruta:71-73`; `pr003_leakage_gate.md:76-78`).

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| EGS md:443 — outgoing geodesics "peel off" after few rungs; horizon cannot be exactly fine-tuned | Mathematician + Physicist | CONFIRMED |
| EGS md:474 — r=r_S is a MARGINALLY UNSTABLE null orbit; exact fine-tuning required to stay forever | Mathematician + Physicist | CONFIRMED |
| EGS md:443 — ITERATED/PIECEWISE construction (another antichain to the future; union of ladders = piecewise discrete horizon), left to future work | Mathematician + Physicist | CONFIRMED |
| EGS md:181 — interior minimals SHORT futures (singularity-truncated), exterior LONG; longest-chain truncation as interior/exterior diagnostic | Physicist + Mathematician | CONFIRMED |
| EGS md:225 — r=2M where Θ_out vanishes; apparent horizon coincides with horizon in 1+1D | Physicist | CONFIRMED |
| EGS md:130–135 — sprinkling the (t*,r) induced 1+1D metric; det g constant ⇒ coord-uniform = volume Poisson | Physicist | CONFIRMED |
| EGS md:164,195 — regular (Hayward-type) BH caveat: interior/exterior partition by future-length likely does NOT hold | Physicist | CONFIRMED |
| EGS md:390,441 — EGS SEEDED/SELECTED the horizon ladder USING the embedding (coordinate slope, outgoing near r=r_S) | Physicist | CONFIRMED |
| EGS Fig 3 / Fig 14 caption (md:186,450) — longest timelike-curve length organised by r separates antichain interior(short)/exterior(long) | Mathematician | CONFIRMED |
| Surya LRR §4 (md~1006–1010,1052) — ordering fraction r → Myrheim–Meyer dimension | Mathematician | CONFIRMED |
| Surya LRR §4.3 (md~1222–1228) — longest chain/height as Brightwell–Gregory proper-time proxy T ∝ ℓ·(longest chain) | Mathematician | CONFIRMED |
| Myrheim 1978 (CERN TH-2538) — ordering-fraction / dimension estimator | Mathematician | UNVERIFIED — not a standalone file in biblioteca/; content corroborated in Bombelli_1987_PhD.md and Surya LRR |
| Bombelli 1987 PhD — causal-set proposal (order + volume → spacetime); ordering fraction | Mathematician | CONFIRMED |

- **Notes:** Myrheim 1978 primary source is absent from `biblioteca/` but its attributed content
  (ordering fraction → dimension; longest-chain suggestion) is consistently reported in the two
  secondary sources present. All EGS claims are textually well-supported ("peel off" md:429,443;
  "marginally unstable" md:474; iterative/piecewise future-work md:443; embedding-seeded selection
  md:441). Surya `T ∝ ℓ·(longest chain)` with `1.77 ≤ m_d ≤ 2.62` confirmed (eq. ~21).

## 8. Synthesis

**The finding is not a failure of PR-003; it is a measured bound, and the literature predicts it.**
Wave 1 converges (and the falsifier's one quantitative attack was tested and refuted) on:

1. **The geometric core of `BARE_RELOCALISATION` is solid.** The connected adherent head exists but
   is the seed's discreteness neighbourhood (k\*=O(1); k\*·ℓ halves with ℓ). A *single* order-only
   tracer **cannot** be made to stay O(ℓ) over a growing extent — `r_S` is a marginally unstable
   null orbit, so peel-off after O(1) rungs is the continuum expectation (EGS md:443,474,
   CONFIRMED), not a defect to tune away. The tail growth in ℓ-units is real (not a search-budget
   artifact — chair-tested, §2/§5).

2. **The order-only detectability channel is an ABSTAIN, and must be labelled as such.** `rel_phi`
   gives no density-robust breakpoint aligned with the head end; greedy is statistically empty
   (n=2/8/1). So there is currently **no order-only evidence that the head boundary is detectable
   from order alone** — independent of the geometric result. The falsifier is right that this
   abstain should not be folded silently into the tidy geometric verdict (action item R2).

3. **The open, computable route is EGS's iterative re-seeding** (md:443, CONFIRMED): concatenate
   successive order-only-seeded brackets along future antichains into a *piecewise* locus. This is
   the only route that could yield an *extended* near-horizon object, and it is exactly what EGS
   left to future work.

**Recommended direction (ranked):**

- **#1 (recommended) — Dev exploration of iterative order-only re-seeding**, with leakage discipline
  pre-committed: order-only seed (future antichain chosen from `C`-derived quantities only), `d_⊥`
  score-only, a **wired relabel-invariance Guard-v on the constructed element set**, and an explicit
  **no-`r`-feedback assertion** between pieces. Question it answers: does a *piecewise* order-only
  locus stay O(ℓ) per piece and converge under density — i.e. is the *bounded* per-piece scale a
  building block, even though a single tracer cannot extend?
- **#2 — Dev search for an order-only stopping observable.** Before any #3 freeze, test whether
  **any** order-only observable (not only `rel_phi`) marks the geometric head end k\* density-robustly.
  Higher risk of a clean null; but it is the precondition for ever freezing a truncation rule.
- **#3 — Accept the bound and pivot.** Treat `BARE_RELOCALISATION` as the achievable-scale result,
  stop chasing an extended single ladder, and redirect to roadmap point 2 (firm up #2 direction AUC
  *at* the horizon, today 1/6/2) and/or draft the PR-003 plan as a **bounded-scale** localisation
  claim.

**Open disagreements (not hidden):**
- *Physicist vs falsifier on route (B).* The physicist recommends pursuing iterative re-seeding as
  the physical mechanism for an extended horizon; the falsifier warns the word "horizon" in
  "piecewise discrete horizon" edges toward `NO_RECONSTRUCTION_CLAIM` and that its feedback-free
  property is unproven. **Resolution:** pursue it as **dev exploration of a bounded-scale building
  block**, never described as a reconstructed horizon, with contract-#5 (no `r` feedback) wired and
  checked before any claim. Both are satisfied by #1-with-caveats.
- *Whether to extend at all (#1/#2) vs accept the bound (#3).* The mathematician frames extension as
  continuum-forbidden for a single tracer (favouring iteration #1 or acceptance #3 over a
  longer-single-ladder hunt); no role advocates chasing a longer single ladder. This is a genuine
  user-level fork (keep pushing construction vs consolidate the bound).

No pre-registration BLOCK (§6 PASS) and no unresolved falsification (the one quantitative attack was
refuted; the rest are caveats now folded into the spec) ⇒ a PROCEED-with-caveats verdict is
admissible.

## 9. Next-step spec

**Reversible steps (may be run now if the user asks — nothing frozen, EXPLORE_POOL only):**
- **R1 [DONE this session].** Falsifier completeness check — complete-fraction 89/93/87%,
  complete-only tail ≈ all tail ⇒ tail growth is not a budget artifact. *Optional:* extend to all 6
  seeds and add per-density complete-fraction + per-seed dispersion to `dev/measure_truncated_head.py`
  output, for the record.
- **R2 (doc-only).** Add to `dev/PR003_NEAR_HORIZON_NOTES.md` an explicit **ABSTAIN** label for the
  order-only detectability channel (rel_phi ambiguous + greedy underpowered), kept distinct from the
  geometric `BARE_RELOCALISATION`; and record that the tail growth is confirmed not-a-budget-artifact
  but its *physical* (vs ℓ-unit) divergence remains undetermined at three densities.
- **R3 (the chosen measurement, dev).** Implement direction #1 (or #2) as a new
  `dev/measure_*.py`, smoke-first, with: order-only seed from `C` only; `d_⊥` consumed strictly
  score-only; a relabel-invariance Guard-v on the constructed element set (analogue of
  `boundary_minimals_invariant` / `verify_order_only`); a no-`r`-feedback assertion across pieces; a
  **flat-space (MINK, same cloud) control** that must NOT produce a persistent adherent locus.
  Findings append to the dev notes + roadmap. Re-verify `make verify-seal` and run `make test`
  before/after; `git status --short` must show no `M nachocausal/` and no `M docs/preregistration_*`.

**Committing steps (ONLY on explicit user authorisation — each its own `/comite` + `/auditor`):**
- **C1.** Freeze rule #2 (`relphi_mean`) and a corrected #3 (truncation / iteration rule) — only
  after both pass the leakage gate's 5 contracts and a full `/auditor`.
- **C2.** Draft and seal the revisable PR-003 plan (roadmap point 4), with disjoint dev/validation
  seeds and a reserved virgin band.
- **Never (in any step here):** touch `nachocausal/thresholds.py`, run the sealed validation path,
  burn `RESERVED_002` seeds, back-fit the dev intensity grid into a sealed comparison, or state a
  reconstruction / "piecewise horizon" claim.

**Minimal falsification test carried forward** (generalises the falsifier's): any future
iterative/truncation construction must satisfy, before it may be called a result —
(a) complete-only vs all aggregation agree (no budget artifact); (b) the relabel-invariance Guard-v
holds on the constructed set; (c) the MINK same-cloud control yields no persistent adherent locus.

## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_CAVEATS

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
