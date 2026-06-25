# Comité Decision 004 — pr003-c1-freeze-readiness

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question
Should the **PR-003 Fase #3 C1 freeze** proceed — turn `docs/preregistration_003_draft.md` into a
frozen `docs/preregistration_003.md` — for the **OPERATIONAL, estimator-induced O(ℓ) resolution
floor** of the **sealed estimator channel C↦r̂** (explicitly **NOT** a Le Cam minimax bound, **NOT**
an information floor over the full causal set C)? Is the draft freeze-ready WITHOUT over-claiming, or
what corrections/preconditions are required first?

## 2. Verified state
Facts checked **this session**, each with its command / file:line.
- **Seal intact.** `make verify-seal` → `nachocausal/thresholds.py sha256 =
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`; independently reproduced via
  `python3 hashlib`. Matches the prereg-002 frozen record (`docs/preregistration_002_result.md:10`,
  `docs/preregistration_002.md:8`). `git status --short` shows no `M nachocausal/`.
- **git.** HEAD `bffa8a9`, branch `main`, working tree clean.
- **Files.** `docs/preregistration_003_draft.md` exists (committed `bffa8a9`, new file +142 lines);
  the frozen `docs/preregistration_003.md` does **NOT** exist (`ls` → No such file).
- **prereg-002 = PASS** (`docs/preregistration_002_result.md:1,7`), SAME sealed instrument `6e2c3888`.
- **Anchors resolve.** `K_LOC=2` (`thresholds.py:98`), `POOLED_SD_FLOOR=0.5` (`:78`),
  `theta_loc/theta_stab` (`:106-113`), `BOX_AREA=7.2`/`T_EDGE=6`/`R_S=0.5` (`:36-43`).
- **Separation enforced at runtime.** Both evidence scripts refuse any non-`EXPLORE_POOL` seed and any
  `RESERVED_002` seed (`dev/measure_info_bound_o3.py:114-116`, `dev/measure_kbeam_peeloff.py:94-96`).
- **AUDIT (this session).** `/auditor` ran the backward-looking integrity audit and wrote
  `docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md`:
  **`AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS`** — 0 errors, 1 warning **W1**: the O3
  (`measure_info_bound_o3.py`) and R2 (`measure_kbeam_peeloff.py`) figures are GPU-produced
  (numpy 2.4.6, dev venv, notes HEAD `5081f4e`); traced to committed scripts + recorded notes but
  **NOT independently re-executed** this CPU session; the freeze should re-run both generators in a
  GPU/sealed session to confirm the recorded figures before creating the frozen file. Mechanical
  audit (`bash audit.sh`) clean: 0/0. Not an `AUDIT_FAIL`, so a PROCEED is not barred on integrity
  grounds — but see §5/§8.
- **Process note.** The Wave-2 falsifier ran on `sonnet` (model substitution): Fable 5 was
  unavailable this session ("Claude Fable 5 is currently unavailable").

## 3. Dossier
Files and references supplied to the committee:
- `docs/preregistration_003_draft.md` (the draft under review); `docs/preregistration_002.md` +
  `_result.md` (PASS, same instrument); `docs/preregistration.md`,
  `docs/preregistration_001_addendum.md`; `docs/estimator_v2_seal.md`, `_freeze.md`.
- `nachocausal/thresholds.py`, `nachocausal/estimator.py`, `nachocausal/generator.py`,
  `nachocausal/scorer.py`, `Makefile` (`verify-seal`/`dry-run`/`test`).
- `dev/PR003_INFO_BOUND_NOTES.md` (R1, O1 reclassified 2026-06-25), `dev/measure_info_bound_o3.py`
  (O3); `dev/PR003_KBEAM_PEELOFF_NOTES.md` (R2), `dev/measure_kbeam_peeloff.py`.
- `docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md` (§9 C1 authorisation),
  `docs/pr003_leakage_gate.md`, `docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md`.
- `biblioteca/derived-md/` — Eichhorn–Gamito–Stokes arXiv:2605.06813; Bombelli 1987; Sorkin 2008.

## 4. Expert briefs (wave 1 — blind, parallel)
### Reproducibility engineer brief
- **Proposed artefact(s):** Exactly one new file, `docs/preregistration_003.md` (non-draft sibling of the existing `docs/preregistration_003_draft.md`, mirroring the `preregistration_002.md` / `_result.md` naming). DOC-ONLY commit on `main`. No new `dev/` script, no `nachocausal/` change, no `results/` artefact, no seed drawn. The frozen doc should carry the same provenance footer the draft already has (`docs/preregistration_003_draft.md:139-142`) plus the freeze commit's HEAD. The draft's own §8 procedure (`:126-135`) is the correct executable shape; it requires `git branch --show-current = main` and the shared-checkout `formula` hazard check before the atomic commit.
- **Environment & seal:** The freeze is doc-only, so it does NOT need the GPU dev venv (numpy 2.4.6, `dev/PR003_KBEAM_PEELOFF_NOTES.md:9`) — it only needs the sealed env (numpy==1.26.4) for the `make verify-seal` gate. Re-verify `make verify-seal` → `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` BEFORE and AFTER the commit, and confirm `git status --short` shows no `M nachocausal/` and no `M docs/preregistration_*`. The seal is a file-SHA, not a numpy version, so the GPU/CPU venv split does not affect seal verification. Package-diff-clean: confirm `git diff --stat` touches only the one `.md`.
- **Provenance capture (the doc must record):** commit HEAD at freeze (draft footer currently anchors `bffa8a9`); branch `main`; seal SHA `6e2c3888…` verified pre+post; the source dev artefacts and their recorded HEADs — O3 `dev/measure_info_bound_o3.py` and R2 `dev/measure_kbeam_peeloff.py`, with the notes recorded at HEAD `5081f4e`, numpy 2.4.6, GPU venv (`auditor_report_001:108`). Both generator scripts ALREADY self-record on every run: UTC ISO timestamp + `platform.node()` host + git branch/HEAD + `np.__version__` + seal-pre/seal-post (`measure_info_bound_o3.py:300-303,322-323`; `measure_kbeam_peeloff.py:307-309,326-327`), and seed band `EXPLORE_POOL`-only with `RESERVED_002` refused at runtime. Logs are git-ignored but regenerable.
- **Run mechanics:** Two-phase. (1) Reversible pre-flight (no commit): `make verify-seal`, `make test`, `git status --short`, branch check, and — to discharge audit W1 — re-run BOTH generators and diff their printed figures against the recorded notes. Each script aborts cleanly on its own: `assert_seal("pre")`/`assert_seal("post")` raise `SystemExit` on seal mismatch; `assert_seeds` raises on any non-`EXPLORE_POOL`/`RESERVED_002` seed. Foreground, single-invocation. (2) The committing step is the single atomic add+commit of `docs/preregistration_003.md` on `main`, gated by post-commit `make verify-seal`. Phase (1) is fully reversible; only phase (2) is one-way, and even it is doc-only and git-revertible.
- **Reproducibility risks / ambiguities:**
  - **W1 (open precondition).** O3/R2 figures GPU-produced (numpy 2.4.6) and NOT independently re-executed this CPU session (`auditor_report_001:108`, W1). Precondition: re-run both generators and confirm the recorded floats before creating the frozen file; pin the re-execution HEAD/host/numpy in the provenance footer.
  - **Float vs integer reproducibility split.** The load-bearing GPU≡CPU `maxdiff=0` claim is specifically for the integer `O`-multiset / future-volume histogram (`PR003_INFO_BOUND_NOTES.md:190-193`), order-derived and insensitive to GPU `np.log` ulp flips. The O3 docstring warns the GPU build is NOT bit-identical to sealed CPU in general (`measure_info_bound_o3.py:47-49`). So expect bit-exact reproduction of the integer observable but only statistical (not bit-level) reproduction of the float figures. **The freeze text must not assert bit-level reproducibility of the float figures.**
  - **Provenance footer staleness.** Draft footer anchors HEAD `bffa8a9` while the notes were recorded at HEAD `5081f4e`. The frozen doc must update its own HEAD and keep the distinct generator-HEAD `5081f4e` so the two are not conflated.
  - **No new blind run is part of this freeze** (draft `:100-102`) — correct; consolidates the already-validated instrument, burns no `RESERVED_002` seed. The executable shape must NOT invoke `make dry-run`/any sealed PASS-FAIL path on fresh seeds.
  - **Shared-checkout hazard** named by the draft (`:134`) but its mechanics are `[UNVERIFIED]` this session; the pre-flight should resolve it (confirm no concurrent worktree on `main` mutating `docs/`) before the atomic commit.

### Mathematician brief
- **Computability.** Everything the step relies on is decidable from the order relation alone. The estimator's input is the boolean past-matrix `C`; the observable `O(i)=|future(i)|=C[:,i].sum()` over minimal elements is computed without any coordinate (`estimator.py:113-131`); the 2-means split / threshold / separation are functions of the sorted multiset `{O(i)}` only (`estimator.py:92-107`). Strict partial order; future-volume and minimality predicates are order- and permutation-invariant, so `T:C↦r̂` is genuinely order-only. The τ(n) abstaining gate (`estimator.py:134-139`) and the T_EDGE_MIN domain gate are functions of `C` and the frozen box, not of the hidden embedding. No metric data enters scoring.
- **Order observable.** Future-volume of minimal elements `O(i)=|{j:i≺j}|`. Carries the horizon signal because the singularity truncates the causal future of interior elements: in EF coordinates the outgoing ray uses the tortoise term `func(r)=r+2r_S·log(|r−r_S|/r_S)` (`generator.py:104`; `t_out=func_i−func_j`, `t_in=rj−ri`, `generator.py:117-127`), folding the interior future inward toward `r=0`, so `|future|` drops sharply across `r_S` — a bimodal `{O(i)}`. EGS confirm this mechanism and the bimodality ("Towards black-hole horizons…" md:191-193).
- **Relevant invariants.** Future-volume / future-cardinality of minimal antichain elements — the v2 observable (EGS md:193). NOTE EGS's *primary* split diagnostic is the **longest chain** from minimal elements (md:181,188-191), not future-volume; EGS warn the future-cardinality "varies between n and √n already for Minkowski" (md:193). The classical invariants — ordering fraction `f(n)=N_rel/(N choose 2)` (Myrheim 1978; `Bombelli_1987_PhD.md:904,978,2110`), longest-chain/height as timelike-distance proxy (`Sorkin_2008…Dice08.md:86`; `causetgloss.md:130`) — are the standard toolkit but are NOT the channel being floored here.
- **Analytic / continuum target.** The 1+1D Schwarzschild event horizon at `r_S=2M=0.5`, recovered as the bimodal split of the order-only future-cardinality in the finite EF patch (`generator.py:104`; EGS md:179-191). The sharp transition becomes a clean partition only in the infinite-timelike-extent limit (EGS md:188-191) — correctly flagged as needing an infinite sprinkling, hence NOT an asymptotic-horizon claim.
- **Caveats.**
  - **Data-processing direction — CORRECT as stated, load-bearing finding.** The DPI reads `KL(P^{r̂}_0‖P^{r̂}_1) ≤ KL(P^C_0‖P^C_1)` because `r̂=T(C)` is a function of `C` and KL is monotone non-increasing under any statistic (the Tsybakov 2009 Thm-2.2 setting the draft cites at §7-O4). The Le Cam two-point lower bound requires an **upper** bound on the **full-data** divergence; the output KL is on the small side of the DPI, so it can only bound `KL(P^C)` from **below** — wrong direction for a minimax floor over all `f(C)`. The draft (§2 bullet 1, lines 40-48) and notes (§0:42-49, §7-O1:269-302) state this exactly right, including the correct subtlety that a *larger* full-data KL makes the hypotheses *more* distinguishable, weakening any universal-impossibility reading (notes:296). No residual minimax-over-`C` reading; the direction argument is sound.
  - **O2 Jacobian leg — order-theoretically sound, dimensionally consistent.** `δr≈σ_O/(dO/dr)=ℓ·√(A_fut)/(dA_fut/dr)` (notes:256); the ρ-cancellation is correct, `√(A_fut)/(dA_fut/dr)` is an O(1) dimensionless length ratio in 1+1D ⇒ `δr∝ℓ`. The log-enhancement near `r_S` is the genuine tortoise-ray derivative (`generator.py:104`). Caveat: explicitly a *sketch* with `σ_O≈√O` Poisson and equal-variance approximations (notes:278-279) — adequate for the *scaling*, not over-claimed as a theorem.
  - **O3 numerical leg — sound and density-invariant.** Runs the actual sealed pipeline (`two_means_split`→`blind_bracket`, lines 142-157), EXPLORE_POOL-guarded with RESERVED_002 refusal, SAME_CLOUD two-point construction (only the BH matrix `r_S` changes), seal asserted before/after. `sd(r̂)/ℓ≈0.34–0.45` across the density range and the `TVg(r̂)` collapse to a function of `s/ℓ` are the right demonstration that ℓ is the resolution scale. Measured O(1)<2 confirms `K_LOC=2` conservative, reported not re-sealed.
  - **Observable-choice caveat to surface in the freeze.** The floor is registered for the *future-volume* channel, which EGS flag as boundary-sensitive (md:193) and which is *not* their primary (longest-chain) split. Recommend one explicit sentence that the O(ℓ) floor is observable-specific, not an order-theoretic universal over estimators. Minor, not freeze-blocking.
  - **K_LOC=2 vs measured ≈0.4 (no-new-constant).** The frozen thresholds already encode (★); the §6 measurement is a *consistency* check (margin ~5×), not a recalibration; correctly forbidden to re-tune K on EXPLORE_POOL (draft §4; leakage gate #5).
  - **Assessment:** From the order-theory side the draft is **freeze-ready**: (★) is correctly an order-only, estimator-channel statement; the DPI-direction argument is correct; O2/O3 sound at the labelled sketch/illustration level. Single recommended (non-blocking) precondition: the explicit "observable-specific, not universal-over-estimators" sentence.

### Physicist brief
- **Coordinates & patch:** The sealed instrument lives in the EGS 1+1D Schwarzschild patch `ds²=−f(r)dt²+f(r)⁻¹dr²` (EGS md:161), sprinkled in Schwarzschild `(t,r)` / tortoise `(t*,r)` coordinates — both constant determinant ⇒ constant sprinkling density (md:130-135). The frozen box is finite: `T_EDGE=6, R_EDGE=1.2`, `r∈[0.1,1.3]` straddling `r_S=2M=0.5`, `BOX_AREA=7.2` (`thresholds.py:37-43`). Finiteness is the crux: an **event** horizon requires an infinite sprinkling (EGS md:173,175). The draft correctly forfeits this — §2:49-51 ties the finite-V, finite-ρ statement to md:2605.06813. **Honest.**
- **Physical meaning of the signal:** Observable `O_min(i)=|future(i)|`, future-VOLUME of minimal elements (`estimator_v2_freeze.md:35`) — the volume-sibling of EGS's *first* diagnostic, the longest-chain split (EGS md:186, Fig.3 lower panel). It tracks `r=2M` because interior minimal elements have their future truncated by the curvature singularity (chains/volumes terminate in short proper time) whereas exterior elements run to the box boundary; this yields the bimodal distribution (EGS md:463, md:191). The draft's Jacobian reading (`dO/dr=ρ·dA_fut/dr`, log-enhanced via the tortoise term) is the correct continuum companion. **Faithful to EGS.**
- **Sprinkling domain:** Frozen finite patch; Poisson sprinkling at frozen intensities `(1500,3000,6000,12000)`, `ℓ=ρ^(−1/2)`, `ρ=intensity/7.2` (`thresholds.py:46,101-103`) — standard Bombelli–Sorkin process (EGS md:115). Domain gate `T_EDGE_MIN=6` (`thresholds.py:129`) marks sub-extent configs OUT-OF-DOMAIN, never FAIL — appropriate since the bimodal split needs "large enough timelike extent" (EGS md:191). Forfeited: any guarantee about depths beyond box reach, and anything outside `r∈[0.1,1.3]`.
- **Claim boundary:** The verdict claims **order-only localisation of the horizon-associated boundary to an O(ℓ) floor in a finite 1+1D patch**, and the draft §2 forfeits, correctly and with anchors, all four over-claims: (a) NOT a minimax/info floor over `C` (only the sealed channel; DPI wrong-direction, lines 40-48); (b) NOT asymptotic/global event horizon (EGS md:173); (c) **NOT regular-BH** — truncation is singular-Schwarzschild-specific, exactly EGS md:465 + md:195 (lines 52-54 cite md:463-465 accurately); (d) NOT 3+1D/Kerr/reconstruction (lines 55-57). **Correctly forfeited on all axes.**
- **"PHYSICAL within box reach" honesty:** Honestly bounded. The peel-off probed in R2 is EGS's *marginally-unstable null orbit*: the horizon is marginally unstable, so any δ=(r−r_S) grows and the probability of an adherent ladder is zero under discreteness (EGS md:443, md:474). R2 shows widening K=1→64 enumerates ~50× more ladders yet order-only top-1 `d⊥/ℓ@k=8` stays ≈5-7ℓ (notes:54-55) and head k≤3 stays ≈2ℓ (notes:60) — the wall is geometric, not greedy myopia. The under-reach caveat is faithfully carried (reach≥8 ≤23% at K=64, `t_edge=6`, notes:41,72-73), so "physical" is asserted only within reachable depth, and both draft (line 84) and notes (76-77) refuse the "clean unconditional PHYSICAL." Taller-box route (`t*/r_S∈[0,50]`) is EGS future-work, correctly fenced as C2/out-of-scope. **Honestly bounded.**
- **Caveats:**
  - The volume observable is a *sibling* of EGS's longest-chain diagnostic, not the literal EGS quantity (project uses future-VOLUME; EGS Fig.3 uses future-HEIGHT/longest-chain). Same singular-truncation bimodality; the draft should not imply the figure is the identical EGS statistic. Minor; non-blocking.
  - The R2 peel-off (apparent-horizon / fuzzy-ladder diagnostic, EGS 3rd) and the localisation floor (longest-chain / 1st diagnostic) are *distinct* EGS mechanisms; R2 "hardens" the floor by ANALOGY, not identity. The draft (§3:79-84) presents R2 as a hardening probe — correct.
  - R2/O3 scored under GPU/numpy 2.4.6, not sealed CPU/numpy 1.26.4; integer link-matmul bit-identical (notes:34) but the AUDIT flagged the GPU figures not re-executed this session. For a *freeze*, the number-provenance re-run is a genuine precondition (draft §6:111-113).
  - The 14400-density single-tracer tail rests on ONE ladder (notes:42,44-45) — anecdotal; the draft does not lean on it and it must NOT be promoted into the frozen text.
  - **Physicist verdict:** physics-ready **conditional on** the standing number-provenance re-run (R2/O3) and on keeping the future-VOLUME-vs-longest-chain distinction and the "PHYSICAL within box reach" caveat verbatim. Tokens upheld.

## 5. Falsifier attack
*(Wave-2 falsifier; ran on `sonnet` — Fable unavailable this session.)*

**Concrete failure modes**
1. **K_LOC=2 anchor has no pre-committed derivation in the public record.** `thresholds.py:98` annotates `K_LOC=2` only as "user decision; cannot localise finer than ~ell"; `docs/preregistration.md:51` calls the multiplier "a small pre-justified integer" without recording the justification. "Conservative ceiling" is honest only if K=2 was chosen for a reason independent of any dev observation; the record does not show why K=2 vs 1 or 3 before any sprinkle. Risk of an implicit NO_POST_HOC_TUNING issue (K chosen large enough not to be falsified).
2. **O2 (Jacobian sketch) rests on three unverified approximations that are load-bearing for the constant** (`PR003_INFO_BOUND_NOTES.md:278`): Gaussianity, equal variance across r_S±s, Δμ=2s. The future-volume Jacobian is asymmetric (one-sided tortoise divergence), so the Gaussian KL can mis-estimate distinguishability; SAME_CLOUD correlation among minimal elements means n_eff<n_min, making σ_O larger than computed. Neither correction is estimated.
3. **R2 uses only 6 seeds; the 14400 datum rests on ONE ladder ("anecdotal", notes:44-45).** At 14400/K=1 the count reaching k=8 is zero (NaN top-1), so the "≈5-7ℓ" pooling is driven by 3600/7200 (reach 19%/23%). The frozen draft must not present this as robustly established across all densities.
4. **numpy version mismatch reaches the observable path, not just floats.** `thresholds.py:18` pins `1.26.4` and `assert_environment()` hard-fails on mismatch — but `measure_info_bound_o3.py`/`measure_kbeam_peeloff.py` do NOT call it; they only print the version. O3 ran under 2.4.6. The GPU-check verifies `maxdiff=0` for the integer O-multiset only, NOT the `two_means_split`/`blind_bracket` float midpoint (argmin/argmax tie-breaking, `np.log` path). The figures 0.40ℓ / 0.6 / d⊥/ℓ may have been produced by a different numerical path than the sealed instrument. W1 covers re-execution but not this version-path gap.
5. **"density-invariant over ×8 density" is ×8 in density but only ×2.83 in ℓ.** ℓ=(0.069,0.049,0.035,0.024); scatter 0.34/0.45/0.39/0.40 = ~30% variation. The collapse is empirically supportive but not a strong universality demonstration; state the ranges literally.
6. **The R2 beam scoring criterion (interval-cardinality regularity) is not pre-committed as the unique/optimal order-only selector** (notes:80 "a different order-only score *might* rank differently"). "PHYSICAL" in frozen text should carry a qualifier naming the specific ranking criterion tested.

**Ground-truth leakage** — No actual violation. `blind_bracket` (`scorer.py:26-58`) reads `embedding[:,1]` to form bracket edges/midpoint; in O3 it is called with the SAME_CLOUD `emb` generated at nominal `r_S=0.5` while only the causal matrix shifts to r_S±s. This is the intended design and conceptually correct (coordinates are real and fixed; only causal relations change; the embedding only SCORES). Subtle modelling caveat: scatter may be understated when the true boundary genuinely differs from 0.5, because points near r_S±s are sampled by a sprinkle designed at r_S=0.5. Not flagged in draft/notes; not leakage.

**Freeze violations**
1. O3/R2 figures measured under numpy 2.4.6, not the pinned 1.26.4; neither script calls `assert_environment()`. Freezing on numbers measured outside the pinned environment is a RESPECT_SEAL_FREEZE concern in spirit (even though the seal is a file-SHA). W1 flags re-execution but not the version-path issue.
2. O3 was run *after* the S1/S2/S3 cascade failure and *after* the committee set the floor as the Fase #3 target — confirmatory test structured as an "illustration", with no pre-declared expected range for the constant. The measured 0.40 then closes O2 and certifies K=2 conservative.
3. The *claim* that K_LOC=2 is a "conservative ceiling" was only reachable after O3 returned ~0.40; freezing this retrospective interpretation promotes a post-hoc characterisation of a sealed constant into a registered finding.

**Verdict coercion**
1. Draft §5 "No new blind run is required for (★)" rules out INCONCLUSIVE by construction. prereg-002 PASS shows the estimator *succeeds at localisation*; it does NOT establish the estimator *cannot do better than K_LOC·ℓ* — logically independent claims. (★) as framed (a lower bound on the sealed estimator's error) is auto-satisfied by any positive error, with no mechanism to return FAIL.
2. "A lower bound is not falsified by one faster method" (§2 last bullet) + "a method beating it ⇒ ground-truth leakage" (§2:59-60) jointly make (★) unfalsifiable by empirical evidence absent any pre-committed positive falsification criterion. Asymmetric treatment of evidence.

**Premature / over-broad claims** — All explicit reconstruction/3+1D/minimax claims are correctly negated in the draft itself. Risk lives in prose derived from the NOTES: `PR003_INFO_BOUND_NOTES.md §3` says K_LOC·ℓ is "the right floor", whereas O3 shows the constant is ~0.4–0.6 (K=2 over-states by ×3–5). The draft consistently uses "conservative ceiling"; ensure no "right floor" phrasing migrates into the frozen text.

**Independent-falsification gate — NOT SATISFIED.** O3/R2 were designed, executed, and interpreted by the same project, no independent replication; the auditor performed no independent run (traced to scripts/notes only); float figures reproduce only statistically. Author == sole verifier. The closest independent check — running O3 under the sealed numpy 1.26.4 — has not been done.

**Minimal falsification test.** Run `measure_info_bound_o3.py` under numpy **1.26.4** (the pinned sealed version, not the GPU 2.4.6 venv) on the same 24 EXPLORE_POOL seeds; confirm `sd(r̂)/ℓ` reproduces 0.34/0.45/0.39/0.40 within ±0.05ℓ and the TVg=0.5 crossing stays in [0.47,0.71] per intensity. If the sealed-numpy run returns a constant substantially above 0.5ℓ (e.g. scatter ≥0.8ℓ at any density), the "conservative ceiling" framing collapses. Single concrete, read-only, RESERVED_002-free check.

## 6. Pre-registration verdict
- **Verdict: CONDITIONAL PASS — freeze may proceed, with one mandatory precondition and two binding forward obligations** (NOT a BLOCK).
- **Freeze status: thresholds frozen before any validation seed was seen — PASS on the core discipline.** The governing constant `K_LOC=2` is sealed in `nachocausal/thresholds.py:98` since the prereg-002 seal `573cfcb` (SHA `6e2c3888…`, `docs/preregistration_002.md:8`); `theta_loc/theta_stab` (`:106-113`) and `BOX_AREA` (`:36-43`) are pre-sealed. No new constant is introduced — the draft states `K_LOC=2` is "already sealed" and that reporting `O(1)<2` is a consistency statement, not a recalibration (`docs/preregistration_003_draft.md:29-31,88-92`). The draft was written (commit `bffa8a9`) after the EXPLORE_POOL dev runs (R1 `d5d91ca`, R2 `b250326`), but this is NOT a freeze violation: the freeze-before-seeing rule governs the relationship between threshold-writing and VALIDATION SEED generation; all thresholds were frozen before the RESERVED_002 seeds were drawn/evaluated. The freeze-before-seeing discipline applies to the validation band; it is honoured in full.
- **Seal integrity: INTACT.** Doc-only freeze; `thresholds.py` untouched. Live seal confirmed (`auditor_report_001:35-43`) and matches the prereg-002 record (`docs/preregistration_002.md:8`). No new constant sealed; no-new-constant rule respected (`docs/pr003_leakage_gate.md` #5).
- **Seed discipline: CLEAN.** Evidence uses only EXPLORE_POOL seeds; virgin RESERVED_002 `[2_000_000,2_999_999]` untouched (runtime guards `measure_info_bound_o3.py:114-116`, `measure_kbeam_peeloff.py:94-96`; `auditor_report_001:73-81`). The 20 prereg-002 validation seeds were consumed once and closed.
- **Reporting rule: BINDING AND RESPECTED.** prereg-002 reported PASS with the non-primary fp caveat recorded (`docs/preregistration_002_result.md:46-51`). The draft records the constant as `O(1)<2` (conservative confirmation), names the under-reach caveat ("PHYSICAL within box reach", `:83-84`), and lists the 14400 tail as anecdotal. No post-hoc.
- **Forbidden moves present? NO** — none of the five tokens tripped: NO_POST_HOC_TUNING (K held at 2; re-tuning forbidden `:88-92`), NO_THRESHOLD_LOOSENING (`thresholds.py` unmodified), NO_GROUND_TRUTH_LEAKAGE (`r` confined to scoring; leakage gate 1–5 satisfied, `auditor_report_001:70-81`), NO_RECONSTRUCTION_CLAIM (minimax/3+1D/Kerr/reconstruction only under NOT/OPEN, `:40-60,117-119`), RESPECT_SEAL_FREEZE (byte-identical instrument).
- **Reasons (preconditions the warden makes binding):**
  - **MANDATORY PRECONDITION — close audit W1.** O3/R2 figures were produced in a GPU venv (numpy 2.4.6) and not independently re-executed in the sealed CPU env (numpy 1.26.4). Before the non-draft file is created, both generators must be re-run to confirm the recorded figures, and the freeze text must NOT assert bit-level float reproduction. **Do not execute the freeze commit until W1 is cleared.**
  - **Binding forward obligation 1 — freeze-text wording check by `/auditor`** to confirm the frozen text never reintroduces "no estimator of C can do better" or universal minimax language (draft binds this at `:109-110`).
  - **Binding forward obligation 2 — `formula` branch hazard.** The commit must be atomic on `main`; `git branch --show-current` must read `main` at commit time (`:134-135`); the shared-checkout `formula` hazard is unresolved (`[UNVERIFIED]`). Verify branch before committing.

## 7. Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| EGS (arXiv:2605.06813) md:161 — induced 1+1D metric ds²=−f(r)dt²+f(r)⁻¹dr² | Repro eng / physicist | CONFIRMED |
| EGS md:130-135 — Schwarzschild/tortoise coords give constant determinant ⇒ constant sprinkling density | Repro eng / physicist | CONFIRMED |
| EGS md:173 (and md:175) — defining an EVENT horizon requires INFINITE sprinkling | physicist | CONFIRMED |
| EGS md:186 Fig.3 lower = future-cardinality; md:188-191 bimodal split needs large timelike extent; PRIMARY diagnostic = LONGEST CHAIN from minimal elements | physicist | CONFIRMED |
| EGS md:191-193 — future-cardinality boundary-sensitive ("varies between n and √n for Minkowski") | falsifier | CONFIRMED |
| EGS md:463, md:465 — interior/exterior split via longest chain; truncation inapplicable to geodesically complete / regular (Hayward) BHs (md:195,465) | physicist / falsifier | CONFIRMED |
| EGS md:443, md:474 — horizon marginally unstable; peel-off / adherent-ladder probability zero under discreteness | physicist | CONFIRMED |
| Myrheim 1978 / Bombelli 1987 (`Bombelli_1987_PhD.md:904,978,2110`) — ordering fraction f(n)=N_rel/(N choose 2) | mathematician | CONFIRMED |
| Sorkin 2008 (`Sorkin_2008…Dice08.md:86`) — longest chain as timelike-distance proxy | mathematician | CONFIRMED |
| `causetgloss.md:130` — level/height as timelike-distance proxy | mathematician | CONFIRMED (with note) |
| Tsybakov 2009 *Intro to Nonparametric Estimation* Thm 2.2 (Le Cam / data-processing) + Bretagnolle–Huber inequality | warden / repro eng / notes | **UNVERIFIED — PHYSICALLY ABSENT** |

- **Tsybakov 2009 / Bretagnolle–Huber — PHYSICALLY ABSENT from `biblioteca/`.** No PDF, derived-md, or converted file exists. The draft (§7 O4) itself flags this: "source … before citing." This open item is NOT closed: the book must be added to `biblioteca/` before the frozen `docs/preregistration_003.md` may cite Thm 2.2 or Bretagnolle–Huber. **Freeze-blocking IF the frozen doc names that theorem as support.** The (★) claim does not depend on it (it lives in the O1 diagnostic, now downgraded), so keeping these strictly under §7 OPEN/future-work, with no reliance, is the alternative.
- Citation 7 phrasing: EGS says "marginally unstable surface" (md:474), not "null orbit" — substance matches; no material discrepancy. Citation 9: the explicit timelike-distance-proxy statement is at Sorkin md:86; `causetgloss.md:130` defines level/height consistently but does not itself make the proxy claim.

## 8. Synthesis
**Recommended direction: REVISE the draft and discharge one reversible empirical precondition, then
RECONVENE (lightweight) before the one-way freeze. Do NOT create `docs/preregistration_003.md` yet.**

**Where all six roles agree (the core is sound):** the draft's central scope is correct and already
well-hedged. (★) is an *operational, estimator-channel* statement; the data-processing-inequality
direction argument is correct and load-bearing (mathematician); the claim boundary is correctly
forfeited on the asymptotic / regular-BH / 3+1D / Kerr / reconstruction axes (physicist, auditor,
warden); the seal is intact, separation is enforced at runtime, and no reserved seed is burned
(warden, auditor). The backward-looking audit returned **AUDIT_PASS_WITH_WARNINGS** (not FAIL), so a
PROCEED is not barred on integrity grounds, and the warden adjudicates the central legitimacy
question — registering an info-side reading of an already-passed sealed instrument — as **not** a
freeze violation, because thresholds were frozen before any validation seed was drawn and the dev
evidence used EXPLORE_POOL only.

**Why the verdict is REVISE_AND_RECONVENE, not PROCEED.** Two classes of unresolved items, and the
template's freeze invariant bars a PROCEED while either stands:

- **(A) An unresolved empirical falsification path.** O3 and R2 were measured under numpy 2.4.6 (GPU
  dev venv), not the sealed pinned 1.26.4; the dev scripts do **not** call
  `thresholds.assert_environment()`; and the GPU≡CPU `maxdiff=0` check covers only the **integer**
  O-multiset, **not** the **float** `r̂` outputs on which the load-bearing figures (0.40ℓ scatter,
  2s/ℓ≈0.6, d⊥/ℓ) rest (auditor W1; reproducibility engineer float/integer split; falsifier
  failure-mode 4 + freeze-violation 1). The falsifier's minimal test — re-run under sealed numpy
  1.26.4 and confirm the table — is **unrun**. Until it passes, the freeze would risk registering an
  environment-dependent number as a density-invariant fact.

- **(B) Draft revisions required before the text is frozen:**
  1. **Add a pre-committed POSITIVE falsification criterion for (★)** (falsifier verdict-coercion).
     As written, (★) is a lower bound auto-satisfied by any positive error, with "a faster method =
     leakage" as a shield ⇒ no route to FAIL. The frozen prereg must state a concrete, pre-committed
     route to FAIL (e.g.: an order-only estimator that PASSES the leakage gate and localises at c·ℓ
     with c materially below the measured ~0.4 at matched density falsifies (★)).
  2. **Contain Tsybakov 2009 / Bretagnolle–Huber.** Physically absent from `biblioteca/` (lit
     verifier). The frozen doc must NOT cite them as support; keep strictly under §7 OPEN until
     sourced, OR add the source first. (★) does not depend on them.
  3. **Honest scaling wording:** "density-invariant over ×8 density" = ×8 in density but only ×2.83
     in ℓ, with ~30% spread (0.34–0.45) in the measured constant — state the ranges literally
     (falsifier #5).
  4. **R2 robustness wording:** 6 seeds; reach≥8 ≤23%; the 14400 datum rests on ONE ladder
     (anecdotal, notes:44-45) and must NOT be promoted; "top-1 ≈5-7ℓ" is pooled mostly from
     3600/7200 (falsifier #3; physicist caveat d).
  5. **"PHYSICAL within box reach" must name the specific tested order-only ranking criterion**
     (interval-cardinality regularity); a different order-only score might rank differently
     (falsifier #6; notes:80).
  6. **Floor is OBSERVABLE-SPECIFIC** (future-volume channel), not an order-theoretic universal over
     estimators; keep the future-VOLUME-vs-EGS-longest-chain "sibling not identical" distinction
     (mathematician; physicist caveat a).
  7. **K_LOC=2 "conservative ceiling" phrasing:** present it as the pre-sealed integer confirmed
     consistent by O3, never as info-theoretically derived; do not let "the right floor" phrasing
     from the notes migrate into the frozen text (falsifier #1 + premature-claim note).
  8. **No bit-level float-reproducibility claim** in the freeze text (only the integer observable is
     bit-stable — reproducibility engineer).

**Open disagreements (surfaced, not hidden):**
- The **warden** returns CONDITIONAL PASS (freeze may proceed once W1 + the two obligations are met);
  the **falsifier** is more conservative (independent-falsification gate NOT satisfied; (★) lacks a
  route to FAIL). The chair sides with the more conservative reading for two reasons: the template's
  freeze invariant bars a PROCEED while an unresolved empirical falsification path (the sealed-numpy
  re-run) exists; and adding a positive falsification criterion is a genuine *draft change*, not a
  runtime gate — so a reconvene over the revised text is the disciplined path.
- The three experts call the draft "freeze-ready conditional on the re-run + minor wording"; the
  chair agrees the *core* is freeze-ready but classes items B1 (positive falsifiability) and B2
  (absent citation) as more than cosmetic, which tips the overall verdict to REVISE.

No pre-registration BLOCK exists (warden = CONDITIONAL PASS), and no fatal falsification stands — so
this is REVISE_AND_RECONVENE, not DO_NOT_PROCEED. The path to freeze is short and well-specified.

## 9. Next-step spec
**Reversible steps (may be run now if the user asks — dev-only, no commit, no seed drawn):**
- **R-1 (the decisive empirical precondition / falsifier minimal test).** Re-run
  `dev/measure_info_bound_o3.py` and `dev/measure_kbeam_peeloff.py` under the **sealed numpy 1.26.4**
  environment (NOT the GPU 2.4.6 venv) on the same EXPLORE_POOL seeds. Confirm `sd(r̂)/ℓ` reproduces
  0.34/0.45/0.39/0.40 within ±0.05ℓ and the TVg=0.5 crossing stays in [0.47,0.71] per intensity;
  confirm the R2 `d⊥/ℓ@k=8` and reach table. EXPLORE_POOL only; RESERVED_002 refused at runtime;
  writes only git-ignored logs. **STOP-and-re-deliberate** if the constant returns ≥0.8ℓ at any
  density (the "conservative ceiling" framing would collapse). *(Discharges audit W1 + the
  version-path concern + the independence gap.)*
- **R-2.** Revise `docs/preregistration_003_draft.md` per Synthesis B1–B8 (reversible dev edits).
- **R-3.** If the frozen text is to cite Le Cam framing, add Tsybakov 2009 to `biblioteca/` first;
  otherwise keep it under §7 OPEN with no reliance.

**Committing steps (only on explicit user authorisation, AFTER R-1 and R-2 pass):**
- **C-1.** Re-run `/auditor` on the REVISED draft text — require `AUDIT_PASS` or
  `AUDIT_PASS_WITH_WARNINGS` with W1 closed; confirm no minimax/universal phrasing and no reliance on
  absent citations.
- **C-2.** Lightweight reconvene (chair confirmation that R-1 passed and B1–B8 are in the text; a
  focused warden + falsifier re-read suffices — a full six-role panel is not required).
- **C-3.** Create `docs/preregistration_003.md` atomically on `main`: verify
  `git branch --show-current == main` (resolve the `formula` hazard first), `make verify-seal` ==
  `6e2c3888…` BEFORE and AFTER, `git status` shows no `M nachocausal/` and no `M
  docs/preregistration_002*`. Then commit. **This is the one-way step; it needs explicit user OK.**

**Binding pre-committed rules** (carry into the freeze): no new data-tuned constant (K stays
`K_LOC=2`); the floor is registered for the sealed future-volume channel only; minimax-over-C stays
OPEN; PASS/FAIL/INCONCLUSIVE reported alike; no `RESERVED_002` seed touched; the doc-only commit
seals nothing in code.

**Falsifier's minimal falsification test (included):** R-1 above — re-run
`measure_info_bound_o3.py` under sealed numpy 1.26.4; FAIL if scatter ≥0.8ℓ at any density.

## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
