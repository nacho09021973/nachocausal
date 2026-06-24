# Comité Decision 003 — pr003-silver-bullet-synthesis

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question
PR-003 "silver bullet" synthesis. Adjudicate the honest cross-check in
`dev/PR003_SILVER_BULLET_SYNTHESIS.md` between three external research opinions
(`biblioteca/Investigacion_Opinion_{1,2,3}.md`) and what this project has already
established/refuted. Two forks:
- **Q1:** Run a dev TDA-persistence (H0, thickened-antichain persistent homology) probe before
  consolidating, or go straight to Fase #3 (accept the `BARE_RELOCALISATION` empirical bound)?
- **Q2:** Run a K-beam multi-hypothesis "peel-off" falsification to decide whether the peel-off is
  algorithmic (greedy myopia, curable) or physical (marginally-unstable null orbit = the bound),
  thereby hardening the bound; AND formalise an information-theoretic lower bound
  (Le Cam / Fano / Cramér–Rao) as the Fase #3 result?

*(Re-run after the original committee session was cut off mid-Wave-2; all inputs — the synthesis
note and the three opinion docs — survived intact, the Wave-1/Wave-2 briefs did not, so the panel
was re-convened from scratch.)*

## 2. Verified state
Facts checked **this session**, each with its command / file:line. Anything unchecked is marked
`[UNVERIFIED]`.

- **Live seal:** `make verify-seal` → `thresholds.py sha256 = `
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`. **Matches** the prereg-002
  frozen record at `docs/preregistration_002.md:8` and `docs/preregistration_002_result.md:10`.
  (Note: `docs/estimator_v2_seal.md:7-8` records the *earlier* estimator-v2 seal `2f4c4a99…`;
  prereg-002 re-sealed `thresholds.py` to `6e2c3888…` at commit `573cfcb`. Provenance chain
  `docs/preregistration_002_result.md:68-69`: decision `bb21147` → freeze `7d25c34` →
  estimator-v2 seal `2f4c4a99` (`22b7660`) → prereg-002 seal `6e2c3888` (`573cfcb`) → blind run #4
  PASS.)
- **prereg-002 = PASS** (`docs/preregistration_002_result.md:1,7`): all six frozen checks hold at
  the primary endpoint (intensity 12000).
- **Git:** HEAD `6b3649e`, branch `main`, working tree clean except the untracked dev note
  `dev/PR003_SILVER_BULLET_SYNTHESIS.md` (`git status`).
- **S3 / `BARE_RELOCALISATION` committed result** (`dev/PR003_ITERATIVE_RESEED_V1_NOTES.md:27-29,
  37,40,46`): honest coverage **51→48→44%** (degrades monotonically across intensities
  3600/7200/14400); per-piece bracket d⊥/ℓ **0.52→0.63→0.88** (grows in ℓ-units; physical d⊥
  plateaus ~0.020); connectivity **90→95→93%** (high & stable); Guard-v 6/6 and MINK control PASS
  at every density. **This is the decoupling the falsifier flags: connectivity/persistence is
  stable while the pre-committed bar (honest coverage) degrades** — verified directly this session.
- **Fase #3 pre-commitment fired:** S3 non-convergence was the pre-committed trigger to enter
  Fase #3 (`docs/comite/comite_decision_002…` §9; `docs/hoja_de_ruta_24_jun_2026.md:104,114,
  134-142`).
- **Reserved virgin band:** `RESERVED_002 = [2_000_000, 2_999_999]` untouched
  (`docs/estimator_v2_seal.md:52-59`).
- **Falsifier model substitution:** the skill assigns the falsifier to Fable 5; Fable 5 returned
  "currently unavailable" this session, so the falsifier was re-dispatched on `opus`. All other
  roles ran on their assigned models.

## 3. Dossier
Files and references the chair supplied to the committee:
- `dev/PR003_SILVER_BULLET_SYNTHESIS.md` (the decision artefact — the chair's honest cross-check)
- `biblioteca/Investigacion_Opinion_{1,2,3}.md` (the three external opinions)
- `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md`, `dev/measure_iterative_reseed_v1.py` (S3 result)
- `dev/PR003_EXPANSION_ROBUSTNESS_NOTES.md` (Fase #1-B S1+S2 negative)
- `docs/preregistration.md`, `docs/preregistration_002.md`, `docs/preregistration_002_result.md`,
  `docs/estimator_v2_seal.md`
- `docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md`,
  `docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md`
- `docs/hoja_de_ruta_24_jun_2026.md` (roadmap; curve→band pivot :67-70), `docs/pr003_leakage_gate.md`
  (5-contract order-only gate; #5 anti-reverse-engineering)
- `nachocausal/estimator.py` (order-only observable + `verify_order_only` Guard-v)
- `biblioteca/` references: Eichhorn–Gamito–Stokes arXiv:2605.06813 (`biblioteca/derived-md/`),
  `biblioteca/Anticadenas_Benincasa.md`, Benincasa–Dowker 2010

## 4. Expert briefs (wave 1 — blind, parallel)
### Reproducibility engineer brief
- **Proposed artefact(s):** Follow the established dev convention exactly — committed pure-numpy probe scripts that *import* sealed modules but never mutate them, each paired with a notes file, emitting a git-ignored `dev/*.log` with a provenance header.
  - Q1 (TDA-persistence H0 probe): `dev/measure_tda_persistence.py` + `dev/PR003_TDA_PERSISTENCE_NOTES.md`, log `dev/tda_persistence.log`. Sibling naming to `dev/measure_iterative_reseed_v1.py` (dev/measure_iterative_reseed_v1.py:1) and its notes `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md`.
  - Q2 (K-beam peel-off falsification): `dev/measure_kbeam_peeloff.py` + `dev/PR003_KBEAM_PEELOFF_NOTES.md`, log `dev/kbeam_peeloff.log`.
  - The Le Cam/Fano lower bound is a *derivation*, not a measurement run — it belongs in a notes/doc artefact (e.g. `dev/PR003_INFO_BOUND_NOTES.md`), not a sealed-path invocation. Any numerical KL/affinity estimate it cites must come from its own dev script with the same provenance header, never from the validation seed band.
  - Scripts live in `dev/` (committed as scoped exceptions per .gitignore and CLAUDE.md:22-29); raw output stays under the git-ignored `dev/*.log` / `dev_ensemble_raw/` (.gitignore).
- **Environment & seal:** Pure numpy, hard-pinned `numpy==1.26.4` (requirements.txt:7), enforced by `thresholds.assert_environment`; no external Minz clone needed (the `~/cs-horizon-reuse-check/venv_minz` note in CLAUDE.md:28-29 applies only to `dev/prototype_o.py`/`make gate`). Re-verify the live seal with `make verify-seal` → must read `thresholds.py sha256 = 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (matches docs/preregistration_002.md:8, docs/preregistration_002_result.md:10) **before and after** the run, exactly as the v1 log records it (dev/iterative_reseed_v1.log:3, and the script's own assertion at dev/measure_iterative_reseed_v1.py:30). Package-diff-clean: `git status` clean except the untracked dev note (DOSSIER verified state); the new dev scripts are the only adds, on `main` only — never on branch `formula` (DOSSIER HAZARD).
- **Provenance capture (header each log must record, mirroring dev/iterative_reseed_v1.log:1-6):** git HEAD short SHA (currently 6b3649e); `thresholds.py` sha256 (= 6e2c3888…) printed at start AND end; `numpy.__version__`; `platform.uname()`; the explicit seed list with proof it draws from `EXPLORE_POOL`/`[1_000_000, …]` and that **RESERVED_002 `[2_000_000, 2_999_999]` is untouched** (docs/estimator_v2_seal.md:52-59); ISO-8601 UTC timestamps (`datetime.now(timezone.utc)`); plus run params (`R_S`, `NMIN`, `t_edge`, intensities, and for TDA the *filtration/thickness parameter*). The script already imports `hashlib, platform, subprocess, time, datetime` for exactly this (dev/measure_iterative_reseed_v1.py:43-49).
- **Run mechanics:** These are *reversible exploration* probes — no committing step, nothing sealed is touched, no validation seed burned, so they need no `/comite` gate to *execute* (only to *freeze* a rule, per docs/pr003_leakage_gate.md:76). Single foreground invocation with a `--smoke` fast path (2 seeds × smallest intensity) before the full sweep, matching the v1 interface (dev/measure_iterative_reseed_v1.py:37-38). The 14400 density took 662s for the v1 sweep (dev/iterative_reseed_v1.log); if the TDA persistence computation is heavier, run in background and poll — never `&`. A guard aborts cleanly by asserting the seal SHA at startup and refusing to run if it ≠ 6e2c3888…, and by asserting every seed ∈ EXPLORE_POOL (raises before any compute). Reversible pre-flight = the entire run (read-only on sealed code); the only *committing* action is `git add` of the script+notes, which must be atomic on `main`.
- **Reproducibility risks / ambiguities:**
  - **Anti-reverse-engineering (the live one):** TDA introduces a thickness/filtration parameter `ℓ_k`; leakage-gate contract 5 (docs/pr003_leakage_gate.md:60-65) and comite_decision_002 (DOSSIER) both require it be anchored to a principled basis BEFORE any scored data is seen. A dev probe may *sweep* it for exploration, but the log must label the sweep as exploration and must NOT pick the best-scoring value — that would be `NO_POST_HOC_TUNING` / `NO_GROUND_TRUTH_LEAKAGE`. [anchored]
  - **Guard-v on the constructed set:** any band/component the TDA probe builds must pass relabel-invariance (leakage-gate contract 3, docs/pr003_leakage_gate.md:45-49); the v1 already reports "relabel Guard-v invariant 6/6" (dev/iterative_reseed_v1.log) — the TDA log must carry the analogous line or it is not order-only. [anchored]
  - **TDA library dependency:** persistent-homology typically needs an external package (e.g. ripser/gudhi) NOT in requirements.txt (only numpy + pytest). Either implement H0 persistence in pure numpy (union-find over the thickness filtration — feasible and keeps the pin clean) or pin any new dep explicitly; importing an unpinned package breaks bit-reproducibility and the package-diff-clean check. Recommend pure-numpy union-find. [anchored: requirements.txt has no TDA dep]
  - **Honest-metric carry-over:** the band reframe does not auto-rescue S3 — d⊥/ℓ grew 0.52→0.88 with density (dev/iterative_reseed_v1.log; dev/PR003_SILVER_BULLET_SYNTHESIS.md:65-67). The TDA log must report honest coverage + a density-convergence row (e.g. add 14400) so a DEGRADING result is recorded as NEGATIVE, not silently dropped — same discipline as dev/measure_iterative_reseed_v1.py:32-35. [anchored]
  - **Le Cam/Fano numerics:** if the bound is evaluated numerically (KL/affinity between BH and MINK order distributions), that estimate must use EXPLORE_POOL seeds and a MINK same-cloud control, never the reserved band; otherwise it leaks. The literature anchors (Major–Rideout–Surya 2007; Cunningham–Surya 2018) are flagged [UNVERIFIED] in the synthesis (dev/PR003_SILVER_BULLET_SYNTHESIS.md:48,64) and are the literature verifier's call, not mine. [anchored / [UNVERIFIED] citations]
  - **Shared checkout:** another agent flips this checkout to branch `formula` (DOSSIER HAZARD). Any `git add` of these dev artefacts must verify `git branch --show-current` = `main` first; a mid-run branch flip would also invalidate the HEAD recorded in the log header. [anchored: DOSSIER]

### Mathematician brief
- **Computability:** All three survivors are decidable on the strict partial order `≺` alone (poset axioms: transitivity, irreflexivity, local finiteness — `biblioteca/Anticadenas_Benincasa.md:18-22`). The repo already exposes the needed primitives order-only and *relabel-provably*: `estimate_O_volume` = column-sum `|future(i)|` and `estimate_O` = single-source longest future chain via topo-DP (`nachocausal/estimator.py:46-55,113-131`), both guarded by `verify_order_only` which conjugates `C` by a random permutation and RAISES if the multiset or per-element value moves (`estimator.py:164-196`). The abstaining/domain gates are `τ(n)` (frozen `fixtures/tau_table.json`, abstains where the 2-means improvement is below the gate — `estimator.py:134-153`, `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md:46-54`) and `T_EDGE_MIN=6 ⇒ OUT_OF_DOMAIN`. A partial order is the correct setting: antichains are genuinely the order-only spatial slices (`Anticadenas §3.1`, line 40-41), and any new per-front field must inherit both gates — a value defined on a sub-cardinality neighbourhood is *undefined, not zero*, and must abstain (comité-002 `Mathematician brief`, line 94).
- **Order observable:**
  - (a) **Thickened-antichain H0:** the filtration object is the future-thickened antichain `A^{+t} = A ∪ {y : 0 < |I(A,y)| ≤ t}` — purely interval-cardinality, hence order-only (`Anticadenas §3.2`, line 46; Investigacion_Opinion_2.md:91; Opinion_3.md:161). The H0 (connected-components) bar over the thickness parameter `t` carries the horizon signal because near the null boundary the thickened slice stays *connected across scales* whereas in flat regions connectivity collapses quickly (Opinion_3.md:164) — i.e. a long-persistence H0 bar with no Minkowski counterpart (Opinion_3.md:181,294). This is the order-theoretically cleanest survivor and it **dodges the falsifier's maximality objection** (comité-002 §5 attack 7, line 236-238: `L_past` level-sets are not guaranteed inextendible): persistent H0 over `t` does not require an inextendible/Cauchy antichain — it reads the *stability range* of the homology, which is the established manifoldlikeness indicator (`Anticadenas:48`, ref 26 = arXiv:0902.0434 "Stable Homology as an Indicator of Manifoldlikeness").
  - (b) **K-beam peel-off:** keep the K highest-scoring partial chains in topo-DP over the DAG, score = links-per-interval / transverse-interval abundance — order-only, `O(K·N·E)` (Opinion_3.md:199,227; Opinion_2.md:140-141). As a *falsification* it is well-posed: it is the same longest-future-chain DP (`estimator.py:46-55`) widened from arg-max-1 to top-K; if the beam still peels as K grows the bound is physical, if it converges the peel-off was greedy myopia (Opinion_2.md:184-190, Synthesis lines 49-53).
  - (c) **Le Cam/Fano bound:** the right order-statistic is the *distribution of bounded-radius Alexandrov-interval subgraph counts* (the `N_k`/`C_k` interval-abundance vector restricted to a discrete radius), compared between the Schwarzschild-sprinkled and Minkowski-sprinkled `C` (Opinion_2.md:58-62; Opinion_3.md:325). The two-point test is well-posed as a minimax/Le-Cam two-hypothesis problem over these two Poisson-induced order-distributions; `D_KL(P_Schw ‖ P_Mink) → 0` over local subgraphs ⇒ a strictly-positive minimax error floor (Opinion_2.md:60-62).
- **Relevant invariants:** ordering fraction / Myrheim–Meyer dimension (`Anticadenas §2.2`, comité-002 line 110); height `L_past`; future-volume `O(i)=|future(i)|` (sealed v2, `estimator.py:113-131`); inclusive-interval cardinality `|I(x,y)|` and small-interval abundances `C_k ≡ N_k` (BD2010 Eq.13, comité-002 lit-verdict line 347 — CONFIRMED); stable/persistent H0 over thickness (`Anticadenas:48`, arXiv:0902.0434).
- **Analytic / continuum target:**
  - (a) thickened-antichain H0 → the *stability plateau* of homology that signals manifoldlikeness (arXiv:0902.0434, `Anticadenas:48`); the BH-specific long bar should localise the apparent-horizon band where `Θ_out(r)=(1/r)(1−2M/r)=0` at `r=2M` (EGS Eq.12, comité-002 lit-verdict line 338 — CONFIRMED). Honesty note: the continuum target is *localisation of the band*, not metric/event-horizon reconstruction.
  - (b) K-beam → the fuzzy-ladder null-geodesic bundle of EGS (Eq.14 discrete expansion, comité-002 line 339 — CONFIRMED).
  - (c) info bound → a Cramér–Rao/Le Cam floor `Error(r̂−r_S) ≳ C·(r_S²/V)^{1/4}·ℓ` (Opinion_1.md:182) or `≳ C/√ρ` form (Opinion_3.md, Synthesis line 57); the continuum analogue is a Le-Cam-type non-parametric minimax lower bound (Opinion_3.md:325).
- **Caveats:**
  - **(a) The thickness `t` is a free filtration parameter and is the leakage hot-spot.** Anchoring it to "best localises r_S in EXPLORE_POOL" = guided by hidden `r`, which leakage-gate contract 5 forbids (`docs/pr003_leakage_gate.md:60-65`; comité-002 §6 freeze-item, line 271-273). The disciplined route is *not to pick one `t`* but to read the persistence interval (born/death in `t`-units), which is exactly what persistent homology is designed to avoid choosing — anchor on the *stability-plateau* criterion of arXiv:0902.0434 declared before scored data, not on a tuned scalar.
  - **(a) Relabel-invariance is automatic but must be made fallable.** The thickened-antichain set is a function of `C` only, so a Guard-v analogue (conjugate `C`, recompute the persistence diagram) must RAISE on mismatch — leakage-gate contract 3 (`pr003_leakage_gate.md:45-52`); the existing pattern is `estimator.py:164-196`. [UNVERIFIED — no such guard is written yet for a TDA module.]
  - **(a) Codimension/overkill caveat:** in 1+1D the horizon is codim-1 (a line/band), so H0 is the right degree but H1 is likely empty; Opinion_2.md:45 flags persistent homology may be computational overkill vs the direct future-volume observable. The band is *not* a free pass — measured transverse thickness grows in ℓ-units `d⊥/ℓ 0.52→0.88` (`dev/PR003_ITERATIVE_RESEED_V1_NOTES.md:29,40-42`), so a "persistent band" claim must still pass honest coverage + density convergence.
  - **(b) The K-beam is decisive *both ways* and contains no leakage** provided the path score is a derived function of `C` (links/interval abundance) and never of `r`; `r` only scores `d⊥` afterward (leakage-gate contracts 1,5). It does not introduce a frozen threshold, so it is a clean dev probe.
  - **(c) The info bound is the order-theoretically soundest "result" of the three** because it requires no new frozen parameter and no scored construction — it is an analysis over the two Poisson-order distributions, turning the empirical wall into a proven floor (Synthesis line 54-59). Two open points: the bound must be stated for the *actual* finite patch volume V and density ρ used (not asymptotic), and the chosen order-statistic (local interval-count subgraphs, Opinion_2.md:62) must be shown to be the one the v2 observable actually uses, else the bound constrains a different estimator than ours. [UNVERIFIED — derivation not done in-repo; literature citations Major–Rideout–Surya 2007 / Cunningham–Surya 2018 left to the literature verifier; the in-repo anchor for stable persistence is arXiv:0902.0434 at `Anticadenas:48,182`.]
  - **General honesty bound holds for all three:** each yields an order-only object *localised in a finite 1+1D patch* — NO metric reconstruction, NO event/Killing horizon (needs infinite sprinkling, EGS, comité-002 line 341), NO 3+1D (`NO_RECONSTRUCTION_CLAIM`).

### Physicist brief
- **Coordinates & patch:** Every surviving step MUST stay in the project's frozen frame: ingoing Eddington–Finkelstein `(t*, r)` with `f(r)=1−r_S/r`, `t* = t + 2M ln|((r−2M)/2M)|` (EGS Eqs. 5–7, derived-md:130–145; prereg `det g=−1 in 2D ⇒ coordinate-uniform sprinkling = natural-volume Poisson`, docs/preregistration.md:61–62). The patch is finite (S3 used `t_edge=6`, `r/r_S∈[0,2]`-type box; iterative-reseed notes:69). Finiteness forfeits the event horizon outright: EGS state the event horizon is `∂Past(J⁺)` and *requires an infinite sprinkling*; futureless points near J⁺ are not even distinguishable from futureless points near `r=0` without the longest-chain trick (derived-md:173–179). So no step may claim an asymptotic/event horizon — only order-only localisation of hidden `r=2M` inside a finite box.
- **Physical meaning of the signal:** The order-only observable tracks `r=2M` because **interior outgoing futures are singularity-truncated**: every interior timelike curve must reach `r=0` in finite proper time, so longest-chain-from-minimal-elements is *short* inside and box-limited *long* outside, producing a **bimodal** split whose boundary sits at `r=2M` (EGS derived-md:181–195, 463; comite_002:156). The sharpness/bimodality strengthens with greater *timelike* box extent (EGS derived-md:188–191, 450; comite_002:342). Critically this bimodality is a signature of a *singular* black hole — it is implicitly a Schwarzschild-singular claim and would fail for a regular (Hayward) black hole where interior curves can be arbitrarily long (EGS derived-md:195, 463–465).
- **Sprinkling domain:** Declared region = 1+1D induced Schwarzschild metric in `(t*,r)`, genuine Poisson at intensity `ρ=ℓ⁻²` (`ℓ=ρ^{−1/2}`), no radial densification (prereg:61–63). S3 ran intensities 3600/7200/14400, `ℓ`=0.0447/0.0316/0.0224, 6 EXPLORE seeds, box-matched MINK control passing at each density (iterative_reseed notes:25–29). Forfeited guarantee: a 1+1D *sprinkling into the induced metric* is not a slice of a 3+1D sprinkling — it is a measure-zero submanifold treated as its own 2D spacetime (EGS derived-md:135); nothing here transfers to 3+1D, and the ladder method's own known open problem is non-convergence / density-fragility (EGS verbatim derived-md:469; comite_002:343,377).
- **Claim boundary:** The verdict claims **order-only localisation of a hidden `r_S` within a bracket in a finite 1+1D singular-Schwarzschild patch**, MINK-falsified and relabel-invariant. It does NOT claim: metric reconstruction, an apparent horizon (`Θ_out` framing is explicitly avoided, notes:70), an event/asymptotic horizon (needs infinite sprinkling), curvature recovery (R=0 in 1+1D vacuum ⇒ no Ricci signal, comite_002:117,338), or any 3+1D result. Regular-black-hole caveat: the longest-chain/bimodality diagnostic is *inapplicable* to geodesically-complete regular black holes (EGS derived-md:463–465) — any band/TDA/bound result inherits this and must be stated as singular-Schwarzschild-specific.
- On the three survivors:
  - **(a) Persistent connected band (TDA H0):** Physically meaningful as an *image of the truncation boundary*, NOT of a continuum-thin horizon. EGS are explicit that the discrete horizon is irreducibly "fuzzy" — an idealized infinitesimally thin boundary becomes a fuzzy O(ℓ) structure (derived-md:70). A persistent H0 component is the honest discrete object for that. BUT the finiteness risk is real and measured: S3 found the band thickness *grows in ℓ-units* (`d⊥/ℓ` 0.52→0.63→0.88) even as physical `d⊥` plateaus ~0.020 (iterative_reseed notes:25–29,40–42). So "it is a band not a curve" is not a free pass — a persistence bar that does not tighten relative to `ℓ` as `ρ→∞` would be a finiteness/truncation artefact, not a convergent horizon image. A TDA H0 probe is physically legitimate *only if* its persistence is judged against MINK and against `ℓ`-scaling, and any thickness/filtration parameter is anchored before scoring (leakage gate contract 5; comite_002 guardian note on `l_k`).
  - **(b) K-beam peel-off — PHYSICAL, and EGS strongly supports this reading.** EGS state it twice and unambiguously: ladders originate close to `r=r_S` but "peel off after a few rungs… because the horizon location is an unstable point in the dynamics, i.e. in the continuum any infinitesimal initial distance `δ=(r−r_S)` of an outgoing null geodesic from the horizon grows as a function of affine parameter" (derived-md:443), and in the conclusions "the horizon is a marginally unstable surface — the angle of an outgoing geodesic has to be fine-tuned exactly… The probability for a corresponding ladder to exist in the causal set is zero due to spacetime discreteness" (derived-md:474). This is the 1+1D analogue of the photon-sphere/horizon-skimming instability (in Schwarzschild the `r=2M` outgoing-null orbit is marginally unstable; `Θ_out` vanishes there, EGS Eq.12, comite_002:338). EGS's *geodesic-focusing* result reinforces, not undercuts, this: the discrete expansion changes sign across `r_S` (interior `mean(E)<0`, exterior `>0`, derived-md:380), exactly the instability that drives any near-`r_S` outgoing tracer inward. So the K-beam falsification is well-posed: if a non-greedy multi-hypothesis beam *also* peels off, the peel-off is **physical** (the marginally-unstable orbit = the resolution wall, EGS derived-md:443,474 supplies the mechanism) and the bound hardens; if the beam stays on-horizon longer, it was algorithmic. Both outcomes are physically interpretable — this is the decisive, honest experiment. Caveat: EGS's own fix for *reach* (not for the instability) is greater timelike box extent (`t*/r_S∈[0,50]`, ~8× S3's `t_edge=6`, derived-md:450, comite_002:171,194); a K-beam at the short box may under-reach for box reasons distinct from the instability, so the K-beam must hold the box fixed against the single-tracer baseline to isolate the physical peel-off.
  - **(c) Information-theoretic floor `Error(r̂−r_S) ≳ C·ℓ` (or `≳ C/√ρ`):** Physically honest and, in my view, the most defensible Fase #3 statement. It is the correct formalisation of EGS's own qualitative claim that "spacetime discreteness causes there to be no approximation of the horizon without such [peel-off] effects" (derived-md:443) and that the horizon is irreducibly fuzzy at scale `ℓ` (derived-md:70). `C·ℓ` and `C/√ρ` are the same statement (`ℓ=ρ^{−1/2}` in 2D, prereg:62), which is internally consistent. It is the honest reading of the measured data: physical `d⊥` plateaus at O(ℓ)≈0.020 while `d⊥/ℓ` grows — i.e. the wall scales with `ℓ`, exactly a discreteness floor (iterative_reseed notes:40–42). A Le Cam/Fano two-point test between Schwarzschild and box-matched Minkowski causal-order distributions is the right instrument and matches the existing MINK-control discipline (prereg:65). It must be stated as patch- and singular-specific (not asymptotic, not 3+1D, not regular-BH).
- **Caveats:**
  - The band/TDA, longest-chain split, and the lower bound are ALL singular-Schwarzschild-specific; none survives for a regular (Hayward) black hole (EGS derived-md:463–465). [anchored]
  - `t_edge=6` is ~8× shorter than EGS's contrast-sharpening box `t*/r_S∈[0,50]`; degraded coverage may partly be a box/domain artefact, and a taller box is a coordinate/domain lever neutral to the seal but **requires a new prereg** (different BOX_AREA/ℓ-table) — out of scope for a dev step (iterative_reseed notes:69; comite_002:171,194). [anchored]
  - No intrinsic order-only ingoing/outgoing discriminator exists; EGS used embedding and cite ladder *crossings* as the intrinsic route (derived-md:482). Any K-beam claiming "outgoing peel-off" must not smuggle the embedding direction — the `relphi` split already failed robustness in Fase #1-B (comite_002:211–217). [anchored]
  - The order-only distance proxy `sep` is a v0 stand-in for EGS's predistance, which suffers "asymptotic silence" at small separation (EGS derived-md:441,557); a TDA thickness filtration or K-beam distance built on `sep` inherits this near-horizon bias. [anchored]
  - The expansion-Θ route already FAILED convergence by 7200 (comite_002:217–218); a band/bound built on the same density-fragile substrate must show `ℓ`-scaling, not just one-density success. [anchored]
  - Whether ANY order-only construction can make an *extended* locus density-robust in this patch is genuinely open; on current evidence (expansion S1/S2 negative, reseed S3 non-converging) the honest move is to consolidate on the measured bound, not to relabel the negative as a band success. [anchored: iterative_reseed notes:65,84–87]

## 5. Falsifier attack
**Concrete failure modes**

- **The TDA H0 probe is structurally incapable of producing a NEW positive; it can only re-image the same negative.** The persistent-H0 band is, per the physicist brief, "the image of the truncation boundary, fuzzy O(ℓ)" — the *same object* S3 already measured. S3's failure was never "we couldn't see a connected band": connectivity was already 90→95→93% (`dev/PR003_ITERATIVE_RESEED_V1_NOTES.md:29`, conn column). The failure was that the band's thickness *in ℓ-units grows* (d⊥/ℓ 0.52→0.63→0.88, `:27-29`) and honest coverage *degrades* (51→48→44%, `:27-29`). A persistence diagram measures bar lifetime, not coverage and not d⊥/ℓ scaling — so a "long-persistence H0 bar with no MINK counterpart" can be reported TRUE while every metric the pre-committed bar actually requires ("coverage no se degrada con densidad", `hoja_de_ruta_24_jun_2026.md:64,104`) stays FAILED. This is the worst failure mode: a metric swap that relabels the S3 negative as a TDA positive.
- **The K-beam "peel-off" falsification is a heads-I-win/tails-you-win device.** Synthesis `:50-53` states it is "decisive both ways": if K-beam peels → "hardens the bound"; if it doesn't → "reopens extension." But the physicist (taller-box caveat) and the S3 notes (`:68-69`) already establish the box is ~8× too short (t_edge=6 vs EGS's t*/r_S∈[0,50]) and that interior ladders *starve* (`:56-60`). So a peel-off at K-beam depth is **confounded with box under-reach** and cannot be cleanly attributed to "marginally-unstable null orbit = physical bound." The "decisive both ways" framing is precisely the failure: a confounded experiment is decisive in *neither* direction, yet is sold as decisive in both.
- **Under-powered K-beam baseline.** The physicist requires "hold box fixed vs single-tracer baseline" to isolate physical peel-off; but if the box is the wrong size for *both* arms, the comparison only shows "K beams peel like 1 beam in a short box," which is uninformative about the asymptotic horizon — and the EGS "asymptotic silence near horizon" (literature verifier CONFIRMED) means the separation proxy is *least* sensitive exactly where the claim lives.
- **The Le Cam/Fano bound is the wrong shape of object for a falsification programme** (expanded under over-claims).

**Ground-truth leakage**

- **TDA thickness t/ℓ_k is an irreducible leakage vector, and the "stability-plateau anchor" does not close it.** Contract 5 (`docs/pr003_leakage_gate.md:60-65`) forbids the score feeding back. But "read the persistence interval, anchor the plateau BEFORE scored data" (mathematician, warden Obligation 1) is leak-free *only if* the plateau is read on MINK/EXPLORE_POOL geometry whose r is never revealed. The danger: the plateau is itself a function of ℓ_k, and ℓ_k is the discreteness scale tied to density — the very axis (`d⊥/ℓ`) along which the BH signal and the embedding scale co-vary. A "principled plateau" computed on the BH explore pool can encode r_S indirectly because the band's persistence lifetime *is* the truncation-boundary geometry. Comité-002 already "flagged l_k anchor" (DOSSIER); this is the same flag un-resolved, now one level more abstract and harder to audit.
- **No TDA Guard-v exists.** Contract 3 (`:45-52`) requires a relabel-invariance guard that RAISES on the construction. Mathematician and reproducibility engineer both mark it "[UNVERIFIED] / not yet written." Until that guard exists and is shown to be able-to-fail, there is no executable proof the persistence diagram depends on ≺ alone and not on a label-ordering artefact of the union-find. A persistence computation with a tie-breaking rule on element indices is a classic silent label-dependence.
- **K-beam direction smuggling.** The peel-off ladder needs an outgoing/ingoing orientation. The DOSSIER is explicit: "no order-only ingoing/outgoing discriminator (relphi split failed Fase #1-B)" and "K-beam must not smuggle embedding direction." A K beams over *what hypothesis space*? If the K hypotheses are seeded or pruned by anything correlated with the embedding direction (even the failed relphi proxy used as a tie-break), contract 4 (`:54-58`) is violated. The synthesis does not specify the order-only seed for the K beams — that gap is a leakage hole, not a detail.

**Freeze violations**

- **The decision smuggles a post-hoc re-opening of an already-closed phase.** This is the sharpest freeze problem. The roadmap pre-committed (`comite_decision_002` §9; `hoja_de_ruta_24_jun_2026.md:104,114,134-142`): "if S3 does not hold, PR-003 enters Fase #3." S3 did not hold. Fase #3 is declared **ACTIVA** (`:136`). Proposing two NEW probes (TDA, K-beam) *after* seeing the S3 negative, with the stated hope of "reopening extension" (synthesis `:52`), is **re-running on fresh ideas after seeing a result** to escape a pre-committed verdict — the structural twin of re-running on fresh seeds. The pre-registration discipline (`preregistration_002.md:64-68`, "no re-running after seeing a result … an unmet principled threshold is informative, never a licence to retune") applies in spirit: the cascade #1/#2 was the committed search; mining a third route post-negative is scope-creep that the warden's "reversible dev probe" framing launders.
- **Thickness sweep → pick-best is one keystroke from a violation.** Reproducibility engineer warns "dev may sweep but must NOT pick best-scoring value"; warden Obligation 1 makes the same point. The risk is that this prohibition is unenforceable without the (non-existent) TDA Guard-v and a written, timestamped plateau declaration *committed before* any scored run. Nothing in the proposal commits that artefact first.
- **Virgin-seed exposure.** Both probes are scoped to EXPLORE_POOL + MINK, and RESERVED_002 is verified untouched (provenance headers). Good — *but* the Le Cam "numerical illustration" (warden) and the K-beam "taller-box" temptation (physicist: "taller box needs NEW prereg") are two routes by which someone could later justify drawing from RESERVED_002 or re-sealing the band. The proposal must not become the on-ramp to a taller-box run on virgin seeds.

**Verdict coercion**

- **Asymmetric reporting baked into the K-beam framing.** "Hardens the bound" (PASS-flavoured) vs "reopens extension" (also PASS-flavoured) — there is *no branch labelled FAIL or INCONCLUSIVE*. A confounded peel-off (box under-reach) should map to INCONCLUSIVE, but the synthesis (`:50-53`) has no slot for it. That is a silent INCONCLUSIVE → {harden | reopen} collapse: both outcomes are framed as wins.
- **The TDA "band exists" reporting risks collapsing the S3 NEGATIVE into a PASS.** S3's honest label is "INCONCLUSIVE-as-extended-object / NEGATIVE on convergence" (`:78`, roadmap `:114-115`). If a TDA bar is then reported as "a persistent band the order recovers," the project's net story silently shifts from NEGATIVE to positive without any metric meeting the pre-committed bar. The synthesis itself warns of this (`:65-67`: "it's a band not a curve is not a free pass") — but the Q1 option "run TDA before consolidating" is exactly the action that creates the temptation.

**Premature / over-broad claims**

- **The Le Cam/Fano lower bound is unfalsifiable-by-construction and risks an untestable "proven no-go" over-claim.** A minimax lower bound says "no estimator can do better than C·ℓ." It cannot be *empirically falsified* by any finite measurement — a method that appears to beat it is dismissed as leakage, and a method that respects it confirms nothing new. Elevating Fase #3 from "measured empirical wall" to "**information-theoretically forced** wall" (synthesis `:54-59`) is a strict over-claim *unless* the derivation's assumptions (which observable, which finite V and ρ, Schwarzschild-vs-Minkowski two-point reduction) exactly match the sealed v2 observable — the mathematician explicitly flags "info bound must use actual finite V,ρ and match v2 observable." A D_KL→0 argument over an *idealised* interval-subgraph-count distribution proves a no-go for a *different* estimator than the one sealed, then claims it for ours. That is the metric-reconstruction-style over-reach in lower-bound clothing.
- **Scope drift toward asymptotic / 3+1D.** The whole motivation ("is the peel-off the marginally-unstable null orbit") is an *asymptotic horizon* concept (EGS event horizon needs infinite sprinkling — literature verifier CONFIRMED). Any claim that K-beam peel-off = "the physical horizon bound" silently imports asymptotic-horizon language into a finite patch that, per the physicist, "forfeits the event horizon." The only defensible claim remains finite-patch 1+1D localisation of hidden r_S — and even the "fuzzy O(ℓ)" bound is **UNCONFIRMED as a quantified bound** (literature verifier: only qualitative at derived-md:70). So "C·ℓ" cannot be anchored to EGS as a published quantitative result.

**Independent-falsification gate**

- **Not satisfied for the live proposals.** The three proposed artefacts (`dev/measure_tda_persistence.py`, `dev/measure_kbeam_peeloff.py`, `dev/PR003_INFO_BOUND_NOTES.md`) **do not exist** — confirmed: `ls` returns "No such file or directory" for all three; tree is clean except the single untracked `dev/PR003_SILVER_BULLET_SYNTHESIS.md` (`git status --porcelain`). So every "decidable on ≺ alone / relabel-proven / decisive both ways" claim in the briefs is asserted about code that has not been written or run — verifier and author are not yet separable because there is nothing to verify. The mathematician's claim that the K-beam DP and TDA filtration are order-only is, today, **author-asserted with no independent execution** ([UNVERIFIED] by construction).
- **Literature gate fails for the load-bearing citations.** The TDA route rests on arXiv:0902.0434 ("Stable Homology as Indicator of Manifoldlikeness"), Major–Rideout–Surya 2007, Cunningham–Surya 2018 — literature verifier confirms **none are in biblioteca/**; 0902.0434 is "cited by URL only." So the single "strongest new idea" (synthesis `:42`) has *no verified support* in-repo: the claimed dodge of the maximality objection ("persistence does not need maximality") is sourced to a paper no one in the committee has read in-repo.

**Minimal falsification test**

One read-only check exposes the worst failure mode (TDA relabelling the S3 negative). **On the already-committed S3 output, compute whether a persistent-H0 lifetime statistic and the honest-coverage statistic are monotonically *anti-correlated* across the three densities** — i.e. take the existing table (`dev/PR003_ITERATIVE_RESEED_V1_NOTES.md:27-29`: conn 90/95/93%, d⊥/ℓ 0.52/0.63/0.88, honest cov 51/48/44%) and show that band-connectedness/persistence is flat-or-rising while the pre-committed metric (coverage, d⊥/ℓ) degrades. If persistence rises or holds while coverage falls (which the existing numbers already indicate: connectivity is *stable* while coverage *degrades*), then a "long-persistence H0 bar" is demonstrably *decoupled* from the success criterion — proving the TDA band can report PASS on a geometry the pre-registration scores FAIL. That single anti-correlation, computable from committed numbers with no new run, falsifies the premise that TDA adds recoverability evidence rather than re-labelling.

**Bottom-line falsifier position:** Q1 — do **NOT** run TDA before consolidating: it re-images an already-measured negative on a metric (persistence) that is decoupled from the pre-committed bar, and its leakage guard (TDA Guard-v) and literature support do not yet exist. Q2 — the K-beam is confounded by the documented box under-reach and lacks an order-only direction seed (relphi already failed); the Le Cam/Fano bound is acceptable *only* as a finite-V, finite-ρ, v2-observable-matched derivation explicitly labelled "lower bound for *this* sealed estimator," never as an empirically-forced universal no-go. Consolidating on the *measured* `BARE_RELOCALISATION` O(ℓ) bound (Fase #3 as already pre-committed) is the only move that does not smuggle a post-hoc reopening of a closed cascade.

## 6. Pre-registration verdict
**Verdict: PASS**

**Freeze status: All thresholds for the proposed dev steps are already frozen (prereg-002); no new threshold freeze is required yet — but one WILL be required before any scored/committing step involving TDA filtration or K-beam parameters.**

The only frozen threshold package relevant to the next step is the prereg-002 seal:
- `nachocausal/thresholds.py` SHA256 = `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, anchored at `docs/preregistration_002.md:8` and confirmed live by `make verify-seal` (reported in `comite_decision_002` §2 and `PR003_ITERATIVE_RESEED_V1_NOTES.md:8`).
- The Fase #3 entry is pre-committed and documented: `hoja_de_ruta_24_jun_2026.md:134-143` ("S3 no aguanta ⇒ PR-003 entra en Fase #3"; the pre-commitment appeared in `comite_decision_002` §9-S3). Nothing new is being frozen by the proposed Q1/Q2 dev probes.
- The thresholds that would eventually govern any Fase #3 result (TDA filtration parameter `t` or `l_k`, K-beam depth K, Le Cam numerics) are **not yet frozen**, which is correct: they MUST NOT be frozen until after dev exploration is done and a principled anchor is declared, before any scored data is seen (`preregistration_001_addendum.md:49,55`; `pr003_leakage_gate.md:60-65`).

**Seal integrity: INTACT — the proposed steps do not touch the sealed path.** The TDA probe (`dev/measure_tda_persistence.py`), the K-beam script (`dev/measure_kbeam_peeloff.py`), and the Le Cam/Fano derivation (`dev/PR003_INFO_BOUND_NOTES.md`) are described as pure dev artefacts under `dev/`, reusing the sealed v2 localiser without modification. They do not touch `nachocausal/thresholds.py`, `nachocausal/gate.py`, `nachocausal/estimator.py`, or `nachocausal/validate.py`, and do not call `validate.run()`. The seal SHA `6e2c3888…` must be confirmed with `make verify-seal` before and after each run, as pre-committed in `comite_decision_002` §9 and `PR003_ITERATIVE_RESEED_V1_NOTES.md:8`. `git status --short` must show no `M nachocausal/` and no `M docs/preregistration_*` after any dev run (`comite_decision_001` §9-R3).

**Seed discipline: CLEAN — no reserved virgin band burned.** All proposed dev probes must use `EXPLORE_POOL = [1_000_000, 1_000_039]` (`dev/explore_seeds.py:23`). The Le Cam/Fano derivation is analytic and uses `EXPLORE_POOL` + MINK point clouds only (reproducibility engineer brief in the dossier). The virgin band `RESERVED_002 = [2_000_000, 2_999_999]` (`docs/estimator_v2_seal.md:52-59`; `preregistration_002.md:15-17`) remains untouched. The `_assert_hygiene()` guard in `dev/explore_seeds.py:36-45` is the executable sentinel. The prereg-002 validation seeds (`2076703, …, 2983811`, `preregistration_002.md:25-27`) were consumed once and are closed; no re-evaluation of them is proposed.

**Reporting rule: BINDING and respected.** The pre-committed reporting rule (`preregistration_002.md:63-68`: "PASS, FAIL, INCONCLUSIVE, or OUT_OF_DOMAIN is recorded and reported regardless of which it is; no post-hoc tuning, no re-running on fresh seeds after seeing a result, no loosening a frozen threshold") applies to the sealed validation run, which is closed (PASS, `preregistration_002_result.md:1,7`). For the proposed dev probes, the roadmap pre-commits to honest reporting of negative/null outcomes identically: `hoja_de_ruta_24_jun_2026.md:64,80` ("no degradar con densidad") was the bar, it was not met, and the result was labelled FAIL of convergence without softening (`PR003_ITERATIVE_RESEED_V1_NOTES.md:35-39`). The same discipline applies to TDA and K-beam: a null or negative result (H0 persistence bar absent, K-beam also peels off) must be reported as such and not re-labelled. No post-hoc anything.

**Forbidden moves present? NO — with two binding forward obligations explicitly called out.**

- `NO_POST_HOC_TUNING`: not violated. No threshold exists for TDA or K-beam; the proposed sequence is measure → (then freeze before any scored/committing step) → score. The Le Cam/Fano derivation is analytic, not tuned to dev outcomes. The TDA filtration parameter `t` is proposed to be read from the persistence interval's stability plateau — a principled, non-tuned criterion — but this anchor has not yet been written down in a freeze document. That freeze must happen before any scored data (`preregistration.md:49,55`).
- `NO_THRESHOLD_LOOSENING`: not violated. `thresholds.py` is read-only for all proposed steps.
- `NO_GROUND_TRUTH_LEAKAGE`: not violated on the face of the proposal. TDA filtration is over the order-only set `A^{+t}` (defined purely from `C`); K-beam is a DP over the order relation; Le Cam uses MINK vs BH causal-order distributions. Embedding `r` enters only to score (dossier, reproducibility engineer brief). The leakage gate contract 5 (`pr003_leakage_gate.md:60-65`) is the governing rule: filtration parameter `t` must be anchored before scored data; `comite_decision_002` §5 "ground-truth leakage 1" and the dossier ("filtration params anchored before scored data") both flag this as the maximum structural risk. **It is not yet violated because no scored data has been seen. It WILL be violated if `t` is chosen by sweeping over EXPLORE_POOL scores and then frozen.**
- `NO_RECONSTRUCTION_CLAIM`: not violated. The synthesis document (`PR003_SILVER_BULLET_SYNTHESIS.md:56-59`) frames Fase #3 as "a proven no-go / info-theoretic lower bound", not a reconstruction claim. The Le Cam/Fano bound `Error(r̂ − r_S) ≳ C·ℓ` is a lower bound on any estimator, which is the opposite of a reconstruction claim. TDA H0 is a recoverability probe, not metric reconstruction. The frozen claim (`preregistration_002_result.md:55-65`) is "order-only localisation within a finite patch" — the proposed Fase #3 result stays within that language.
- `RESPECT_SEAL_FREEZE`: not violated by the proposed steps (see seal integrity above).

**Two forward obligations the warden places on record now, binding before any scored/committing step:**
1. **TDA filtration parameter `t` must be frozen with a principled anchor BEFORE any scored data** (leakage gate contract 5, `pr003_leakage_gate.md:60-65`; `comite_decision_002` §5 leakage 1; dossier "anti-reverse-engineering"). The disciplined route is to read the stability plateau from the persistence diagram's interval structure — a principled, data-driven but non-score-guided criterion — and declare it in writing before revealing `r` on any EXPLORE_POOL seed. Sweeping `t` over scored EXPLORE_POOL data and picking the best-localising value is a `NO_GROUND_TRUTH_LEAKAGE` / `NO_POST_HOC_TUNING` violation (`pr003_leakage_gate.md:69-72`). A Guard-v for TDA relabel-invariance is also not yet written (`comite_decision_002` §4 mathematician brief "relabel Guard-v for TDA not yet written [UNVERIFIED]") and must be built and verified before any freeze.
2. **K-beam depth K and any box-hold comparison must be similarly frozen** before any scored/committing use. K-beam is described as decisive both ways (algorithmic vs physical peel-off), which is its scientific value; to preserve that decisiveness the comparison protocol (hold box fixed vs baseline, as the physicist notes) must be declared before peeking at results.

**Reasons (each anchored):**
- The proposed steps are within the dev lane, explicitly reversible, using only `EXPLORE_POOL`, and do not touch `thresholds.py` or the sealed validation path. This is the same lane cleared by `comite_decision_001` §6 (PASS) and `comite_decision_002` §6 (PASS). `hoja_de_ruta_24_jun_2026.md:29-47` pre-commits the governing discipline for all Fase #3 dev steps.
- S3's failure of convergence (`PR003_ITERATIVE_RESEED_V1_NOTES.md:35-39`; `hoja_de_ruta_24_jun_2026.md:97-115`) was the pre-committed trigger for entering Fase #3 (`comite_decision_002` §9). That trigger has fired. Proceeding to Q1/Q2 dev probes as Fase #3 exploration is consistent with the pre-committed cascade, not a deviation from it.
- TDA H0 persistence is order-only, relabel-invariant by construction if implemented over the abstract poset, and MINK-falsifiable — satisfying leakage gate contracts 1-4 on paper. Contract 5 (anti-reverse-engineering of `t`) is the open obligation.
- K-beam is decisive both ways and pipeline-compatible; no new frozen param if K is declared before scoring (`PR003_SILVER_BULLET_SYNTHESIS.md:49-53`).
- Le Cam/Fano is an analytic derivation over the causal-order distributions of the two sprinklings — no new scored param, no new freeze required at this stage; the bound is derived, not fitted (`PR003_SILVER_BULLET_SYNTHESIS.md:55-59`).
- The Fase #3 write-up is not pre-registered yet and is not required to be at this dev stage. It will require a new freeze document before any committing step, per `preregistration.md:66-67` and `comite_decision_002` §6 committing bullet 1.
- No Fase #3 freeze has been attempted; therefore no threshold has been loosened, no validation seed burned, no post-hoc re-run performed, and no reconstruction claim made. All five guardrail tokens remain unviolated.

## 7. Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| EGS arXiv:2605.06813 — event horizon = ∂Past(J⁺) requires infinite sprinkling (derived-md:173-179) | Physicist (1a) | CONFIRMED |
| EGS arXiv:2605.06813 — interior curves singularity-truncated ⇒ bimodal chain-length split at r=2M (derived-md:181-195) | Physicist (1b) | CONFIRMED |
| EGS arXiv:2605.06813 — discrete horizon irreducibly fuzzy O(ℓ) (derived-md:70) | Physicist (1c) | UNCONFIRMED |
| EGS arXiv:2605.06813 — ladders "peel off after a few rungs because the horizon location is an unstable point in the dynamics" (derived-md:443) | Physicist (1d) | CONFIRMED |
| EGS arXiv:2605.06813 — "horizon is a marginally unstable surface… probability for a ladder zero due to discreteness" (derived-md:474) | Physicist (1e) | CONFIRMED |
| EGS arXiv:2605.06813 — bimodality/longest-chain diagnostic fails for regular/Hayward BH (derived-md:463-465) | Physicist (1f) | CONFIRMED |
| EGS arXiv:2605.06813 — Eddington–Finkelstein coords Eqs.5-7 (derived-md:130-145) | Physicist (1g) | CONFIRMED |
| EGS arXiv:2605.06813 — expansion sign-change across r_S, Θ_out Eq.12 / discrete expansion Eq.14 | Physicist (1h) | CONFIRMED |
| EGS arXiv:2605.06813 — box t*/r_S∈[0,50] to ensure longest-chain diagnostic works (derived-md:450) | Physicist (1i) | CONFIRMED |
| EGS arXiv:2605.06813 — predistance "asymptotic silence" at small separation (derived-md:441,557) | Physicist (1j) | CONFIRMED |
| arXiv:0902.0434 "Stable Homology as an Indicator of Manifoldlikeness" — stable-homology-as-manifoldlikeness claim | Mathematician | UNVERIFIED |
| Anticadenas_Benincasa.md cites arXiv:0902.0434 (ref 26, line 182) | Mathematician | CONFIRMED |
| Anticadenas_Benincasa.md — poset axioms (lines 18-22): transitivity, irreflexivity, local finiteness | Mathematician | CONFIRMED |
| Anticadenas_Benincasa.md — antichains = order-only spatial slices §3.1 (lines 40-41) | Mathematician | CONFIRMED |
| Anticadenas_Benincasa.md — future-thickened antichain §3.2 (line 46) | Mathematician | CONFIRMED |
| BD2010 arXiv:1001.2725 — small-interval abundances N_k, Eq.13: S^(2)[C] = N − 2N₁ + 4N₂ − 2N₃ | Mathematician | CONFIRMED |
| Major–Rideout–Surya 2007 — causal-set homology/TDA (dev/PR003_SILVER_BULLET_SYNTHESIS.md:48) | Reproducibility engineer (via synthesis) | UNVERIFIED |
| Cunningham–Surya 2018 — causal-set homology/TDA (dev/PR003_SILVER_BULLET_SYNTHESIS.md:48) | Reproducibility engineer (via synthesis) | UNVERIFIED |

**Notes:**
- **1c — EGS derived-md line 70, "discrete horizon irreducibly fuzzy O(ℓ)":** Line 70 contains the introductory "Motivation" section, discussing the general claim that the horizon is "fuzzy" in a discrete setting. The text says the horizon "corresponds to a 'fuzzy' discrete structure" but does not state a precise O(ℓ) bound as a quantified claim. The physicist's phrasing "irreducibly fuzzy O(ℓ)" goes slightly beyond what line 70 actually asserts (qualitative, not a quantified error bound). Status: UNCONFIRMED as a quantified O(ℓ) bound — the qualitative fuzziness claim is present, but no O(ℓ) scaling is stated at that location.
- **arXiv:0902.0434 (Stable Homology):** Referenced by URL only in Anticadenas_Benincasa.md line 182 (ref 26) and cited inline at line 48 for the claim that a stable homology plateau is a manifoldlikeness indicator. The paper is **not present as a PDF or derived-md in biblioteca/**; it can only be confirmed as *cited*, not opened. Status: UNVERIFIED (cannot locate the paper itself in biblioteca/).
- **Major–Rideout–Surya 2007 / Cunningham–Surya 2018:** Neither paper is present in biblioteca/ in any form (PDF or derived-md). The synthesis document itself explicitly flags these as "citations UNVERIFIED." Status: UNVERIFIED.

## 8. Synthesis
**Recommended direction: PROCEED to Fase #3 along the spine the project is already pre-committed
to — consolidate on the measured `BARE_RELOCALISATION` O(ℓ) bound — and develop the
Le Cam/Fano lower bound as the Fase #3 *result*, scoped strictly to this estimator. Do NOT run a
blind TDA probe as a rescue, and run the K-beam only as a tightly-controlled, leakage-guarded
falsification. This is `RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`.**

The warden returns PASS (no pre-registration BLOCK) and there is no *unresolved* falsification that
forbids all action — the falsifier's objections are decisive against specific *framings*, not
against the consolidation spine, and the recommended scoping resolves each one. Therefore a PROCEED
verdict is admissible.

Where the roles converge:
- **All six agree the honest spine is consolidation on the measured bound** (physicist "consolidate,
  don't relabel the negative"; mathematician "info bound is the soundest result"; warden "Fase #3
  trigger has fired"; falsifier "the only move that doesn't smuggle a post-hoc reopening";
  reproducibility engineer treats Le Cam as a derivation, not a run; the synthesis note itself,
  `:54-59`).
- **The Le Cam/Fano lower bound is the strongest Fase #3 candidate** — no new frozen parameter, no
  scored construction, and it turns the empirical wall into a derived floor.
- **The K-beam peel-off question is physically real**: EGS derived-md:443,474 (CONFIRMED) supply the
  marginally-unstable-orbit mechanism, so "is the peel-off physical or algorithmic" is a genuine,
  decidable question — *if* the experiment is not confounded.

Open disagreements (surfaced, not hidden):
- **TDA H0 — mathematician/physicist (cautiously pro) vs falsifier (against), with the warden and
  literature verifier supplying the deciding constraints.** The mathematician calls TDA the
  "order-theoretically cleanest survivor" that "dodges the maximality objection"; the physicist
  calls a persistent band "physically meaningful … only if judged vs MINK and vs ℓ-scaling." The
  falsifier shows the *committed* S3 numbers already decouple the TDA signal from the success bar:
  connectivity 90→95→93% (stable) while honest coverage 51→48→44% degrades and d⊥/ℓ 0.52→0.88 grows
  (verified this session, §2). The literature verifier removes the math's main support: the three
  homology/TDA citations (arXiv:0902.0434, Major–Rideout–Surya 2007, Cunningham–Surya 2018) are
  **UNVERIFIED / not in biblioteca/**. **The chair sides with the falsifier on TDA**: running it
  blind now would re-image a known negative on a decoupled metric, with no Guard-v, no anchored
  thickness, and no in-repo literature. TDA is not killed — it is *gated* behind three
  prerequisites (below).
- **K-beam "decisive both ways" (synthesis/mathematician) vs "confounded ⇒ decisive in neither"
  (falsifier, echoed by the physicist's box caveat).** Both are right about different things: the
  question is real but the short box (t_edge=6 vs EGS t*/r_S∈[0,50]) confounds a peel-off with
  under-reach, and there is no order-only direction discriminator (relphi failed Fase #1-B). The
  resolution is to run the K-beam **only** with the box held fixed against the single-tracer
  baseline, an explicitly order-only hypothesis seed (no relphi/embedding), and an explicit
  **INCONCLUSIVE** branch for box-confounded peel-off — closing the verdict-coercion hole.
- **Le Cam scope — "proven no-go" (synthesis `:54-59`) vs "unfalsifiable over-claim" (falsifier).**
  Resolved by labelling: the bound is admissible as "a lower bound *for this sealed estimator* at
  the actual finite V, ρ," never as an empirically-forced universal/asymptotic no-go. The EGS
  "fuzzy O(ℓ)" anchor is UNCONFIRMED as a *quantified* bound (literature verdict 1c), so `C·ℓ`
  must be derived in-repo, not attributed to EGS.

Ranked alternatives:
1. **(Recommended) Consolidate to Fase #3 + Le Cam/Fano derivation (scoped) + guarded K-beam
   falsification.** Honest, pre-committed, leakage-safe.
2. **TDA H0 probe — only after its three prerequisites are met** (decoupling gate cleared, TDA
   Guard-v written and shown to fire, missing literature sourced into biblioteca/ and a principled
   thickness anchor declared in writing). Otherwise deferred.
3. **Straight to Fase #3 with no further dev probes at all** (pure consolidation on the measured
   bound). The most conservative; loses the chance to *harden* the bound via the K-beam.

## 9. Next-step spec
**Reversible steps (exploration; may be run now if the user asks — no `/comite` gate to execute,
seal untouched, EXPLORE_POOL only):**

- **R0 — Decoupling gate (zero new run; do this first).** From the *already-committed* table
  `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md:27-29`, document the anti-correlation the falsifier
  identified: connectivity/persistence-proxy (90→95→93%) vs honest coverage (51→48→44%) and d⊥/ℓ
  (0.52→0.88). **Decision rule:** if persistence is flat-or-rising while coverage degrades, TDA is
  *disqualified as recoverability evidence* and steps R1/T* below are NOT run. (On current numbers
  this gate already reads "decoupled" — so the default is to skip the blind TDA probe.)
- **R1 — Le Cam/Fano derivation as the Fase #3 result.** Write `dev/PR003_INFO_BOUND_NOTES.md`:
  derive `Error(r̂−r_S) ≳ C·ℓ` (≡ `C/√ρ`) as a two-point Le Cam bound between the Schwarzschild and
  box-matched Minkowski causal-order distributions, **stated for the actual finite V and ρ of the
  patch and matched to the sealed v2 observable** (mathematician/physicist). Any numerical
  illustration uses EXPLORE_POOL + MINK only. Label explicitly: "lower bound for THIS sealed
  estimator," NOT a universal/asymptotic no-go; `C·ℓ` derived in-repo, not attributed to EGS
  (literature 1c UNCONFIRMED).
- **R2 — K-beam peel-off falsification, guarded.** Write `dev/measure_kbeam_peeloff.py` +
  `dev/PR003_KBEAM_PEELOFF_NOTES.md` + git-ignored log, pure-numpy (no new deps), seal-asserted
  before+after, EXPLORE_POOL only. **Binding pre-committed protocol (declare before peeking):**
  (a) hold the box fixed and compare K-beam against the single-tracer baseline at the *same* box;
  (b) the K hypotheses must be seeded by an order-only quantity (links/interval abundance) and MUST
  NOT use relphi or any embedding-derived direction (falsifier leakage / physicist relphi caveat);
  (c) a three-way report — peel-off persists as K grows ⇒ evidence the bound is **physical**;
  converges ⇒ **algorithmic**; box-confounded/under-reach ⇒ **INCONCLUSIVE** (no silent
  collapse to a "win").

**Gated step (reversible, but only after prerequisites — defer unless the user wants it):**

- **T1 — TDA H0 probe**, only if R0 does *not* show decoupling AND all three prerequisites are met:
  (i) a TDA relabel-invariance **Guard-v** exists, mirrors `estimator.py:164-196`, and is shown to
  fire on a violating input; (ii) the missing homology literature (arXiv:0902.0434,
  Major–Rideout–Surya 2007, Cunningham–Surya 2018) is sourced into `biblioteca/` and confirms the
  "persistence dodges maximality" claim; (iii) a principled stability-plateau thickness criterion is
  declared in writing *before* any scored EXPLORE_POOL run (warden Obligation 1). Implement H0 in
  pure-numpy union-find; report honest coverage + a density-convergence row so a degrading result is
  recorded NEGATIVE.

**Committing steps (NOT now — only on explicit user authorisation, each via a fresh freeze +
`/comite` + `/auditor`):**

- **C1 — Freeze the Fase #3 result** (the Le Cam bound's precise form + any K-beam/TDA parameter)
  in a new pre-registration document with a principled anchor, before any RESERVED_002 seed is
  touched (warden; `preregistration.md:66-67`).
- **C2 — Any taller-box run** (`t*/r_S∈[0,50]`) requires a **new prereg** (different BOX_AREA/ℓ
  table) — out of scope for a dev step (physicist; iterative_reseed notes:69).
- **Commit hygiene for all artefacts:** atomic on `main`; verify `git branch --show-current = main`
  first (shared-checkout `formula` hazard); `make verify-seal` = `6e2c3888…` before+after;
  `git status` shows no `M nachocausal/` and no `M docs/preregistration_*`.

**Falsifier's minimal falsification test (folded in as R0):** on the committed S3 numbers, show
whether the persistence/connectivity statistic is anti-correlated with honest coverage across
densities; if persistence holds/rises while coverage falls, TDA is decoupled from the success
criterion and must not be run as a rescue.

## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off
**Decision: ACCEPTED** — `RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`. Proceed to Fase #3 on the
pre-committed spine (consolidate on the measured `BARE_RELOCALISATION` O(ℓ) bound) and develop the
Le Cam/Fano lower bound as the Fase #3 result. Blind TDA H0 **deferred** behind its three
prerequisites; K-beam to be run **only** under the guarded protocol (R2).

**Executed this session (reversible, dev-only):** R0 — decoupling gate
(`dev/PR003_TDA_DECOUPLING_GATE_NOTES.md`, verdict DECOUPLED → blind TDA disqualified) and R1 — the
Le Cam/Fano derivation sketch (`dev/PR003_INFO_BOUND_NOTES.md`, anchored to the frozen `K_LOC·ℓ`
floor; open items O1–O4). R2 (guarded K-beam) and any committing freeze (C1/C2) remain pending and
unauthorised.

**Signed:** Ignacio — 2026-06-24.
