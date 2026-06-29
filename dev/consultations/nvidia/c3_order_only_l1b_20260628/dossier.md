# NVIDIA consultation dossier

## Question

Committee 007 C3 requires that the eventual proof of BL localization (L1a/L1b) use no covert geometry: the tube/locality scale must be characterised order-theoretically, and continuum terms like geodesic/transversal may be used only for benchmarking, never to define Phi. Given the attached committee decision and dev note, provide a non-binding advisory memo that: (1) restates the L1b minimal falsification test in order-theoretic terms only; (2) identifies where the current sketch still relies on continuum/geometric language; (3) proposes one or two clean order-only reformulation patterns for the locality/tube notion; and (4) lists the sharpest failure modes or hidden assumptions that would keep C3 open. Do not recommend threshold changes, seal changes, or any operational retuning. Treat this as external advisory support only, not evidence.

## Metadata

```json
{
  "consultation_id": "c3_order_only_l1b_20260628",
  "context": [
    "/home/adnac/nachocausal/docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md",
    "/home/adnac/nachocausal/dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md"
  ],
  "created_utc": "2026-06-28T18:07:07.900385+00:00",
  "git": {
    "branch": "main",
    "head": "063e64e71e3ee6bc71922402b417fb31fd08bcba",
    "status_short": "m DeepMath\n M README.md\n?? completion_maximality_smoke.als\n?? dev/PR003_C1_REFERENCE_ALTERNATIVES.md\n?? dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md\n?? dev/consultations/\n?? docs/DEEPMATH_CONSULTING.md\n?? docs/NVIDIA_CONSULTING.md\n?? \"modelo contraejemplo.als\"\n?? poset_smoke.als\n?? scripts/consulting/"
  },
  "max_file_bytes": 200000,
  "nvidia": {
    "adapter_contract": "configured command reads dossier from stdin and writes answer to stdout",
    "external_repo": {
      "head": "5823e14295ed060af954677f25d162aa4ef9355e",
      "is_git_repo": true,
      "status_short": ""
    },
    "nvidia_cmd": "/home/adnac/ai/nvidia-consult/bin/nvidia-consult",
    "nvidia_cmd_configured": true,
    "nvidia_command_found": true,
    "nvidia_home": "/home/adnac/ai/nvidia-consult",
    "nvidia_home_exists": true
  },
  "question_sha256": "e9bcb24555b0df0ea83e587d4e736e6392d31dd049a1ea28cc5dcf7188e6d577",
  "repo_root": "/home/adnac/nachocausal",
  "run_requested": true
}
```

## Notes

- Target issue: committee-007 C3 no covert geometry in eventual proof.
- Keep within advisory-only scope; no threshold, seal, or prereg changes.

## Context

### /home/adnac/nachocausal/docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md

Bytes: 37558
SHA256: b04b7305e20fe9dd16f914884eaa13f5f0b6eea8232d39f01f8d3409bd2c697a

```text
# Comité Decision 007 — pr003-bl-localization-lemma-l1-regrade

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question
Re-grade Lemma L₁ of the support report `biblioteca/Horizontes En Conjuntos Causales.md`
(Entregable B/C). Does Trauthwein–Yukich 2026 (arXiv:2605.23292, BL-localization, Theorem 2.1 /
Def. 2.3) justify re-grading Lemma L₁ from "IMPOSSIBLE (C1 does not stabilize → no analytic null
law via Malliavin–Stein)" to "OPEN, with a concrete proof strategy"? Main dossier:
`dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md`. Adjudicate (a) whether BL-localization's
law-vs-realization distinction genuinely bypasses the no-stabilization objection; (b) whether the
mapping Φ(ℓ)=order-2-indexed Poisson functional with transversal tube ℓ^{2/3} is admissible as
[PLAUSIBLE-TRANSFER]; (c) that the quantum leg (Lemma L₆, rogue set) and the global verdict §6
remain intact; (d) that this does NOT touch the prereg-003 seal/freeze — dev theory, nothing
measured or frozen. Nothing is sealed, run, or implemented.

## 2. Verified state
Facts checked **this session**, each with its command / file:line.
- **Seal:** `make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`. Matches `docs/preregistration_002.md:8` and `docs/preregistration_003.md:9`. Sealed path INTACT.
- **Git:** branch `main`, HEAD `a4cfe4e`. Working tree clean except one untracked dev note `dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md` (`git status --porcelain` → `?? dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md`). `nachocausal/` unmodified.
- **No validation run is involved.** Reversible dev-phase THEORETICAL adjudication of a support-document lemma re-grading. No prereg, no seed draw, no `results/` write. `/auditor` precondition does not apply (this is not a PROCEED built on already-claimed results).
- **Primary source present:** `biblioteca/2605.23292v1.pdf` (Trauthwein–Yukich, "Second-order Poincaré inequalities and localization on the Poisson space", 22 May 2026), read this session by the chair (Thm 2.1 p.5; Def. 2.3 p.8).

## 3. Dossier
Files and references the chair supplied to the committee:
- `dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md` (main dossier; the re-grade rationale).
- `biblioteca/Horizontes En Conjuntos Causales.md` (git-ignored support report): Entregable B (`C1_IS_ONLY_AN_EMPIRICAL_DETECTOR`, line 102), Entregable C lemma table (L₁ line 111, L₂, L₆ line 116), §6 global verdict (`CREDIBLE_ONLY_AS_SEMICLASSICAL_PROGRAM`, line 166).
- `biblioteca/2605.23292v1.pdf` (Trauthwein–Yukich): Theorem 2.1 (p.5), Def. 2.3 BL-localization (p.8), eqs. 1.3 / 2.1–2.6, "weaker than stabilization" (intro p.3 + §2.2 p.6), space-time setup infinite time horizon (p.7), geometry-dependent radius (p.9).
- `docs/preregistration_003.md` (operational O(ℓ) resolution floor, FROZEN; seal `6e2c3888…`; z* / K_LOC scaling).
- `CLAUDE.md` (dev/validation separation; dev scripts committed but never tune sealed thresholds; embedding only scores), `docs/preregistration.md`, prior decisions `docs/comite/comite_decision_00{4,5,6}_*`.
- C1 definition context: `dev/X0_Qn_wellposedness_NOTES.md` §11; `docs/comite/comite_decision_006_*`. C1 = intrinsic height `s(x)`=longest chain to past boundary; foliation `Σ_ℓ`; flux `Φ(ℓ)`=# order relations crossing the level-ℓ cut; normalized via median/MAD; threshold `z*`.
- Binding guardrails: `RESPECT_SEAL_FREEZE` (`6e2c3888…`), `NO_GROUND_TRUTH_LEAKAGE`, `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`.

## 4. Expert briefs (wave 1 — blind, parallel)
### Reproducibility engineer brief
- **Proposed artefact(s):** The immediate deliverable is doc-only and touches no code path: a status edit to the git-ignored support report `biblioteca/Horizontes En Conjuntos Causales.md` (Entregable B / Lemma L₁), with the rationale already captured in the untracked note `dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md`. No new sealed artefact, no `nachocausal/` change. Any *future* substantiation must follow existing dev naming: (i) the analytic ψ(r)-bound sketch as the §4.1 sketch — extend the existing note, do not branch a parallel doc; (ii) any eventual numerical sanity-probe of the KPZ transversal-tube tail (the `ℓ^{2/3}`/`I_ψ(θ)<∞` claim) belongs as a committed `dev/measure_*.py`+`dev/PR003_*_NOTES.md` pairing (cf. `dev/measure_kbeam_peeloff.py`+`dev/PR003_KBEAM_PEELOFF_NOTES.md`), with raw ensembles written only to git-ignored `dev/dev_ensemble_raw/` per `CLAUDE.md`. Such a probe is a dev *sanity* check of a literature exponent — it must never read, define, or tune any sealed threshold.
- **Environment & seal:** Re-verify the seal is byte-identical before and after any edit: `make verify-seal` must print `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching `docs/preregistration_002.md:8` and `docs/preregistration_003.md:9` (chair confirmed INTACT this session). A doc/markdown re-grading cannot change that SHA — that invariance is itself the proof of non-touch. If a future numerical probe is run, it must use the sealed CPU env (numpy pinned `1.26.4`, `docs/estimator_v2_seal.md`) — NOT the `~/cs-horizon-reuse-check/venv_minz` (numpy<2) clone, which is only for `dev/prototype_o.py`. Package-diff-clean: `pip freeze` against the sealed lock.
- **Provenance capture:** For the doc-only re-grading: record commit (HEAD `a4cfe4e`, branch `main`), the unchanged seal SHA `6e2c3888…`, and `git status` showing `nachocausal/` clean. No seed band is drawn — load-bearing: zero `RESERVED_002`/virgin seeds touched. Any future `dev/measure_*` probe must self-record commit, `pip freeze`, `uname -a`, its own dev seed (fixed dev constant, never a validation seed), and run timestamps into its `dev/*.log`.
- **Run mechanics:** Immediate step is a single reversible edit to a git-ignored file plus a committed dev note — no invocation, no background process, trivially abortable. Guard: `make verify-seal` ≠ `6e2c3888…` ⇒ stop. Pre-flight (reversible): doc re-grading, ψ(r) sketch, optional dev sanity-probe — all dev-phase, discardable. Committing step: none in scope.
- **Reproducibility risks / ambiguities:**
  - KPZ transversal exponent `ℓ^{2/3}` and `I_ψ(θ)<∞` are self-flagged `[UNVERIFIED]` in the note (`dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md:118-119`). The re-grade rests on a *plausible-transfer* with no committed numerical/analytic backing yet — admissible only as "OPEN", never "confirmed".
  - Scope-creep risk: the note (§6) admits TY proves the *marginal* law (L₁) but the actual C1 statistic is `min_ℓ φ(ℓ)`, needing EVT atop, and `z*~√(2 log N_eff)` feeds the FROZEN prereg-003 floor. The re-grade must stay confined to L₁ and must NOT be read as re-opening or re-tuning the prereg-003 floor / `z*` — that would risk NO_THRESHOLD_LOOSENING.
  - `biblioteca/...md` is git-ignored ⇒ the re-graded artefact is not version-controlled; the auditable trail is the *committed* `dev/` note, not the support report.
  - L₆/§6 independence is asserted on TY being a *kinematic* Poisson CLT silent on the covtree stem σ-algebra (`...NOTES.md:97-99`) — plausible but should be confirmed by the mathematician/literature-verifier, not assumed.

### Mathematician brief
- **Computability.** On the order relation alone (partial order, transitive DAG): height `s(x)`=longest chain from minimal elements to `x` (`O(V+E)` after transitive reduction); level set/ideal foliation `Σ_ℓ`; crossing flux `Φ(ℓ)=#{x≺y : s(x)≤ℓ<s(y)}`. All relabel-invariant (`dev/X0_Qn_wellposedness_NOTES.md:645`). NOT decidable on a finite stem: `min_ℓ Φ` over an unbounded future (the L₆ rogue-set obstruction, §6:165 — independent of L₁). The project's *frozen* observable is distinct: estimator-v2 future-VOLUME with the data-independent `τ(n)` abstaining gate (`docs/estimator_v2_freeze.md:34-59`). C1's height/flux is *exploratory*, not the sealed estimator — this adjudication touches no frozen quantity.
- **Order observable.** `Φ(ℓ)` carries the horizon signal as an order-theoretic conductance/bottleneck (X0 §11.1, `:671`). **Correction:** this is *not* a Poisson order-2 U-statistic — a U-statistic kernel depends only on the pair `(x,y)`; here the crossing indicator depends on `s(·)`, a *global* functional of `P`. `Φ(ℓ)` is a Poisson **score functional** `H=Σ_z ξ(z,P̂)` with order-2 pair indexing but a globally-dependent kernel — exactly the object TY Setup p.7 is built for, and precisely *not* the U-statistic/finite-chaos machinery. The "U-statistic" phrasing in `dev/PR003…NOTES.md:59` is imprecise/[UNVERIFIED].
- **Relevant invariants.** Genuine order-2 Poisson U-statistics: ordering fraction `r=2R/[N(N-1)]`, kernel `1[x≺y]` → Myrheim–Meyer dimension (Surya LRR 2019 §4.2; Myrheim 1978; Bombelli–Lee–Meyer–Sorkin 1987); interval/k-chain abundances `C_k` (Surya §4). The longest chain/height `L_max` is the global extremal functional (KPZ/Tracy–Widom); future-volume `|J⁺(x)|` is estimator-v2 (`estimator_v2_freeze.md:34`). Ordering fraction stabilises classically; `s(x)` does not — the whole reason TY is invoked.
- **Analytic / continuum target.** L₁'s target = null law of finitely many normalised cuts `φ(ℓ)` under flat 1+1 Minkowski: joint Gaussian with Berry–Esseen rate `O(1/√Var Φ)` (TY eq.1.3 via Thm 2.1 p.5 — verified: hypotheses only `EF=0`, `EF²<∞`, `∫E[(D_{x,m}F)²]<∞`; bounds are fourth-moment integrals of `D,D²`; **no stabilization assumed**). Longest-chain continuum benchmark: `L_max/N^{1/2}→`const·(geodesic proper time) with Tracy–Widom fluctuations `O(N^{1/6})` — Hammersley/Ulam (Poissonised LIS) law = 1+1 Minkowski sprinkling (Baik–Deift–Johansson 1999; Johansson 2000; Surya §4.3).
- **Adjudication:**
  - **(a) Law-vs-realization bypass — SOUND, as a strategy not a proof.** TY p.8 (verified verbatim): "BL-localization establishes closeness in the `d_BL` metric between the **laws** … in contrast to 'stabilization', a notion comparing **specific realizations** … exactly (via stopping sets) or approximately in `L^q`." The prior IMPOSSIBLE (support §B:103, L₁:111) is a realization-level/`L^q` add-one-cost criterion. TY Thm 2.1 needs none of it. So the impossibility claim is **no longer supported** → re-grade to OPEN is warranted. But Def 2.3 still demands `d_BL` 4-tuple decay `ψ(r)` (eq 2.3) with `I_ψ(θ)<∞` (eq 2.5) — unproven for `Φ`, the genuine open step.
  - **Add-one cost `D_{x'}s(x)∈{0,1}` — CORRECT (for the height).** Proof: any chain in `P∪{x'}` ending at `x≠x'` contains ≤1 element ∉`P`; deleting it yields a chain in `P` of length ≥(new−1), so `s(x;P∪{x'}) ≤ s(x;P)+1`. ✓ Bounded *per-x* cost, unbounded *number* of affected `x` is exactly right. **Caveat:** this `{0,1}` bound is for `s`, **not** for `Φ`. `D_{x'}Φ(ℓ)` is unbounded (reclassifying an unbounded number of heights across the *absolute* level `ℓ` moves an unbounded number of crossings). The "coherent global re-indexing leaves the flux *profile* invariant" claim (`:68`) is the load-bearing unproven step [PLAUSIBLE-TRANSFER].
  - **(b) `ℓ^{2/3}` tube + integrable ψ — ADMIT as [PLAUSIBLE-TRANSFER], tube itself ESTABLISHED.** Transversal exponent 2/3 (longitudinal 1/3) is the KPZ/Tracy–Widom law of the Hammersley/Poissonised-Ulam process = 1+1 Minkowski sprinkling (BDJ 1999; Johansson 2000) — NOT a transfer. Transverse-wandering tail `~exp(−c r^{3/2}/ℓ)`, far stronger than TY's mild integrability AT FIXED SCALE. The real unproven difficulty: the locality scale **grows** with `ℓ` (`ℓ^{2/3}`), so `I_ψ(θ)<∞` must hold on the *unbounded* space-time domain — exactly why TY's localization-in-time (eq 2.4) and geometry-dependent `ξ^[r]` (p.9) are the purpose-built tools. Establishing `I_ψ(θ)<∞` for the flux score is the open analytic task (dossier §4.1, correctly [UNVERIFIED]).
  - **(c) Quantum leg L₆ + global §6 — INTACT.** TY is a kinematic CLT on Poisson sprinkling (Setup p.7); silent on the covtree stem σ-algebra / Dowker–Zalel measurability. Rogue-set obstruction (§F:46, §6:165, L₆:116) logically independent and untouched. Global `CREDIBLE_ONLY_AS_SEMICLASSICAL_PROGRAM` unchanged. NO_RECONSTRUCTION_CLAIM preserved.
  - **(d) Seal/freeze — UNTOUCHED.** Re-grades a git-ignored support doc + a `dev/` note, on an *exploratory* candidate (C1); no sealed estimator-v2 quantity, no `z*`/`τ(n)`, no validation data. RESPECT_SEAL_FREEZE, NO_THRESHOLD_LOOSENING, NO_POST_HOC_TUNING, NO_GROUND_TRUTH_LEAKAGE all preserved.
- **Verdict:** Re-grading **L₁ from IMPOSSIBLE → OPEN (with concrete proof strategy) is JUSTIFIED.** The "impossible" rested on a sufficient condition (stabilization) that TY 2026 shows unnecessary; BL-localization is strictly weaker, with hypotheses plausibly met by the 1+1D KPZ structure. Required corrections before this becomes a lemma: (i) relabel `Φ(ℓ)` a Poisson *score functional*, not a U-statistic; (ii) prove `I_ψ(θ)<∞` for the flux score via the DLPP transverse tail; (iii) close the absolute-level-vs-profile re-indexing step, since `D_{x'}Φ` (not `D_{x'}s`) is the unbounded operator the moment integrals see. L₁ ≠ L₂: TY delivers the marginal/joint CLT only; `z*~√(2 log N_eff)` still needs EVT of dependent Gaussian maxima atop it.
- **Caveats:** `Φ(ℓ)` "U-statistic" imprecise (globally-dependent kernel ⇒ score functional) [verified vs TY Setup p.7]; `{0,1}` add-one bound is for `s(x)` not `Φ(ℓ)`; `I_ψ(θ)<∞` on unbounded domain is [PLAUSIBLE-TRANSFER] not established (growing tube width); embedding of the causet score into TY's `X×ℝ×M` with the right metric is assumed not checked [UNVERIFIED]; L₆/§6 independent of this re-grade [support §6:165 verified].

### Physicist brief
- **Coordinates & patch:** The Schwarzschild side uses Eddington–Finkelstein/tortoise coords (`dev/gate_highN.py:30`; EGS Eq.6/7, `biblioteca/derived-md/Towards black-hole horizons...md:140,145`). But L₁ governs the **flat Minkowski null hypothesis**, natural coords null `u=t−r, v=t+r` (`dev/X0_Qn_wellposedness_NOTES.md:19`). The relevant domain for L₁ is a **finite 1+1D flat patch**, Poisson-sprinkled, with edge/lenticular truncation — not curved geometry. Finiteness forfeits asymptotic structure: no `J⁺`, hence no event-horizon/asymptotic claim is definable (EGS:175).
- **Physical meaning of the signal:** Order-only observable tracks `r=2M` because interior points have **singularity-truncated futures** → bimodal longest-chain/future-cardinality distribution sorting inside vs outside (EGS:191,193,463); the apparent-horizon `Θ_out(r)=(1/r)(1−2M/r)=0 ⇒ r=2M` content (EGS:223–225). This is the **signal** physics — L₁ is the flat **null**, which the verdict must NOT conflate with the re-grade.
- **Sprinkling domain:** Poisson sprinkling into a finite region (EGS:111). Crucial mismatch: TY's setup uses an **infinite time horizon** (TY Setup p.7), whereas the project's null is a **finite patch** whose future-cardinality law is strongly boundary-sensitive — even flat Minkowski in a causal diamond gives future cardinality varying between `n` and `√n` (EGS:193). Any analytic flat null law for `Φ(ℓ)` must absorb these finite-patch boundary/lenticular artefacts; TY's infinite-time functional does not model them directly. Conditioned (fixed-`N`) vs unconditioned sprinkling also matters (report:21).
- **Claim boundary:** Re-grading L₁ is a **statistical-foundations upgrade only** — flat null distribution of `Φ(ℓ)`; claims nothing about the Schwarzschild signal, reconstruction, asymptotics, 3+1D. The regular-BH caveat bounds even the signal: longest-chain bimodality **fails for regular (Hayward) black holes** (interior arbitrarily long proper time, EGS:195,463); diagnostic valid only for geodesically-incomplete Schwarzschild. The program is order-only **localisation in a finite singular-Schwarzschild 1+1D patch**, never reconstruction.
- **Caveats:** (1) A BL-localization flat null law does **not** change the claim boundary — purely statistical foundations (report:23–25; PR003:23,97). (2) No reconstruction over-claim risk *if scoped strictly to the flat null leg*; only hazard is rhetorical conflation of "null law now plausible" with "observable now works" — guard with NO_RECONSTRUCTION_CLAIM. (3) L₆ + §6 `CREDIBLE_ONLY_AS_SEMICLASSICAL_PROGRAM` are physically independent (TY kinematic; silent on QSG measure) — quantum barrier intact [VERIFIED]. (4) `ℓ^{2/3}` tube is a flat-space DLPP/KPZ statement; for the NULL the geometry *is* flat, so curvature/horizon is irrelevant to its applicability — transfer geometrically appropriate, correctly held at [PLAUSIBLE-TRANSFER] (`I_ψ(θ)<∞` un-derived). Finite-patch vs TY infinite-time gap is an additional un-closed item [UNVERIFIED]. Did not re-verify seal/HEAD; relies on the reproducibility role; adjudication treated as reversible/theoretical.

## 5. Falsifier attack
### Falsifier attack
- **Concrete failure modes:**
  1. **The load-bearing step is unproven and the re-grade status does not reflect it.** TY Def. 2.3 (p.8) requires the law of the local score `ξ(z,P)` be approximable in `d_BL` by a short-range truncation `ξ^[r]`, uniformly over added configs of size ≤5. The dev note's whole argument for Φ is the one line "un reordenamiento global coherente … deja el perfil de flujo … aprox. invariante" (`dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md:68`). The mathematician CONCEDED `D_{x'}Φ` is UNBOUNDED and this profile-invariance step is "load-bearing UNPROVEN" [PLAUSIBLE-TRANSFER]. A strategy resting on one unproven [PLAUSIBLE-TRANSFER] step is not yet concrete → correct classification is **PARTIALLY-OPEN / CONTINGENT on the profile-invariance lemma**, not OPEN. Calling it OPEN treats plausibility as proof.
  2. **Φ is a score functional, not a U-statistic; the score decomposition is asserted, not established.** The note calls Φ "una U-estadística de orden 2" (`:60`); the chosen anchoring (each pair at its upper point) is one decomposition, and whether it satisfies `I_ψ(θ)<∞` / `I_φ(θ')<∞` (eqs 2.5-2.6) for a tube width growing as `ℓ^{2/3}` is the acknowledged open task (`§4 point 1`).
  3. **`I_ψ(θ)<∞` on an unbounded growing domain is unestablished.** KPZ exponent 2/3 is `[UNVERIFIED]` in the note (`:119`). Even granting it, the tube cross-section grows with `ℓ`, so a polynomially-decaying `ψ(r)` integrating finitely against a growing volume element (∝ ℓ^{2/3}) is not automatic and is not argued — flagged "bosquejo pendiente".
  4. **TY's infinite-time Setup does not model finite-patch lenticular effects.** TY p.7 specifies `X×ℝ` unbounded in time; the project patch is finite (`thresholds.py:37-42`). Lenticular boundary effects produce spurious flux minima at box edges (EGS md:193) not captured by TY's infinite-time CLT. Applying TY's Berry–Esseen bound to a finite-patch boundary-contaminated observable is an unjustified domain transfer.
- **Ground-truth leakage:** The profile-invariance argument invokes the tube "alrededor de la geodésica" (`:69-71`). In a pure causal-set setting the geodesic is a *continuum* object; anchoring the tube around "the geodesic" risks importing embedding knowledge (which direction is the null geodesic) into the *analytic strategy* for the null law — the kind of covert metric reference `CLAUDE.md:18` forbids the observable from using. If the BL argument *needs* the geodesic tube to be well-defined, the strategy structurally leans on ground-truth geometry to establish the null distribution, not merely to score.
- **Freeze violations:** The note states "TY + EVT … justificaría el escalado `z* ~ √(2 log N_eff)` del floor, en lugar de un `z*=3` fijo" (`§6`). `z*~√(2 log N_eff)` is tied to the frozen prereg-003 floor (`thresholds.py:98` `K_LOC=2`). Framing TY+EVT as "backbone that would justify" this is a rhetorical handle on a frozen constant; the re-grade of L₁ could later be invoked to argue `z*` should be revisited. NO_THRESHOLD_LOOSENING applies to this rhetorical path, not only to code edits. L₁ and L₂ are distinct; connecting TY to the prereg-003 floor before L₂ is established is premature.
- **Verdict coercion:** The proposed binary IMPOSSIBLE → OPEN jump, given the conceded unproven load-bearing step + open `I_ψ` task, soft-coerces: it reads as progress (OPEN=tractable) while absorbing the unproven step. The honest intermediate is **PARTIALLY-OPEN (contingent)**; downgrading after ratifying OPEN is harder than calling it CONTINGENT now.
- **Premature / over-broad claims:** "posición geodésica" (`:68`) is a continuum concept with no order-internal definition → strategy applicable only in the manifold-like regime, not as a pure order-theoretic result. The prereg-003 connection pre-claims TY delivers the EVT scan result, which the note itself denies (`:91`). The regular-BH/Hayward failure (EGS:195) is inherited; calling the strategy "concrete" without naming the domain on which the CLT is expected to hold (flat Minkowski only?) is premature.
- **Independent-falsification gate:** NOT satisfied. `docs/preregistration.md` rule "the author of a claim is never its sole verifier" is strained: the dev note is authored by the same analyst/chair who convenes this committee; the support report is **git-ignored** (no committed auditable trail); the dev note is **untracked** at session time (`?? dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md`). No structural separation between author and verifier. *(Chair's note: the three Wave-1 experts and the literature verifier independently re-derived/confirmed the TY citations and the order-theoretic argument from the primary PDF — partial mitigation; see §8.)*
- **Minimal falsification test:** Write the `I_ψ(θ)` integral for the flux score Φ explicitly using the anchored-pair representation and the KPZ transversal exponent 2/3. Define `ψ(r) = sup_z sup_{|A|≤5} d_BL(Law(ξ(z,P)), Law(ξ^[r](z,P+A)))` for the growing tube of cross-section `∝ ℓ^{2/3}`, and evaluate whether `∫_0^∞ ψ(r) dr < ∞` **uniformly in ℓ**. If it diverges (tube volume grows faster than `ψ` decays), BL-localization fails for Φ and L₁ does NOT graduate from IMPOSSIBLE to OPEN. Until that sketch exists, the correct verdict is **CONTINGENT**, not OPEN.

## 6. Pre-registration verdict
### Pre-registration verdict
**Verdict: PASS — with one binding condition**

**Freeze status: ALL FROZEN before any validation seed was seen.** `K_LOC=2`, `theta_loc`, `theta_stab` → `thresholds.py:98,106-113` (sealed commit `573cfcb`, seal `6e2c3888…`, per `docs/preregistration_002.md:8`, `docs/preregistration_003.md:9`). `P_PERM_THRESHOLD=1e-4`, `POOLED_SD_FLOOR=0.5` → `thresholds.py:87,78`. The proposed step is doc-only (`biblioteca/Horizontes En Conjuntos Causales.md` git-ignored + untracked dev note); neither is part of the frozen instrument. The operational floor `★` (`docs/preregistration_003.md §1`, `K=K_LOC=2`) is unchanged; no constant introduced or re-calibrated.

**Seal integrity: INTACT.** `make verify-seal` → `6e2c3888…`, matching `docs/preregistration_002.md:8` and `docs/preregistration_003.md:9` verbatim. The step runs no sealed path and modifies no `nachocausal/` file.

**Seed discipline: CLEAN.** No seed drawn. `EXPLORE_POOL` (PR-003 Fase #3 measurements) not touched. `RESERVED_002` virgin band `[2_000_000, 2_999_999]` and the 20 `VALIDATION_SEEDS` (`thresholds.py:66-70`) untouched. Dev/validation separation intact.

**Reporting rule: COMPLIANT.** No measurement outcome; no PASS/FAIL/INCONCLUSIVE event. The note marks every unproven transfer `[PLAUSIBLE-TRANSFER]` and KPZ exponents `[UNVERIFIED]` and enumerates the two gaps (§4). Pre-committed transparent accounting.

**Forbidden moves present? NO — with one condition.** All five tokens checked: NO_POST_HOC_TUNING (no constant changed); NO_THRESHOLD_LOOSENING (`z*=3`, `K_LOC=2` unchanged); NO_GROUND_TRUTH_LEAKAGE (no data/score/embedding seen); NO_RECONSTRUCTION_CLAIM (statistical-foundations upgrade only); RESPECT_SEAL_FREEZE (confirmed). **Binding condition:** the dev-note §6 sentence ("TY + EVT … justificaría el escalado `z*~√(2 log N_eff)`") is admissible only as a conditional theoretical observation. **It does not and cannot authorize any modification of `K_LOC`, `theta_loc`, `theta_stab`, `P_PERM_THRESHOLD`, or `z*` where those are frozen/operative.** Any future step that would change a frozen threshold based on the TY-backed L₁ re-grade requires a NEW pre-registration with a new seal, independent audit, and explicit user authorization — identical to the process that produced `docs/preregistration_003.md`. The re-grade is accepted only with this condition treated as binding.

**Reasons (anchored):** Doc-only on git-ignored file + untracked dev note; no committed instrument file modified. L₁→L₂ firewall explicit (note §4 item 2: TY "alimenta el Lema L₂ pero no lo prueba"; mathematician concurs). The original block rested on stopping-set stabilization (realization-level); TY Def 2.3 (p.8) operates on the law — a change in framework, not sneaking around a proven impossibility (no published impossibility theorem overturned; a sufficient condition shown unnecessary). `D_{x'}Φ` unboundedness correctly flagged as load-bearing unproven, consistent with OPEN not CONFIRMED. `ℓ^{2/3}` tube `[UNVERIFIED]` pending the KPZ sketch — correct posture. §6 + L₆ INTACT (TY kinematic). No seed burned, no sealed path executed, no numerical claim. `docs/preregistration.md`: "Unmet principled thresholds are informative … never a licence to loosen" — a theoretical open-door on L₁ is not a licence to loosen any frozen threshold.

## 7. Literature verdict
### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| `2605.23292v1.pdf` Thm 2.1 p.5 — sharpened Malliavin–Stein for general Poisson functionals; hyp. EF=0, EF²<∞, ∫E[(D F)²]<∞; bounds=Σγ̂₀–γ̂₆ fourth-moment integrals of D,D⁽²⁾; NO stabilization | Mathematician | CONFIRMED |
| `2605.23292v1.pdf` Def 2.3 p.8 — BL-localization compares LAWS in d_BL vs stabilization comparing REALIZATIONS (stopping sets / L^q) | Mathematician, Repro | CONFIRMED |
| `2605.23292v1.pdf` "p.6" — "weaker … than the standard stopping set stabilization criterion … allows for interactions of scores at distant points" | Chair note | CONFIRMED, page error: verbatim block is on **p.3** (intro); p.6 carries "weaker than existing stabilization criteria" without the "interactions at distant points" clause. Substance accurate; page off by 3. |
| `2605.23292v1.pdf` Setup p.7 — H=Σ ξ((z,t_z,M_z),P̂), space-time sum over W×ℝ, unbounded time horizon | Mathematician, Physicist | CONFIRMED |
| `2605.23292v1.pdf` p.9 — ξ^[r] may depend on the geometry of balls B_r(·); time-localization eq 2.4 | Mathematician | CONFIRMED, minor: geometry-of-balls is p.9; eq 2.4 is **p.8** not p.9. |
| `2605.23292v1.pdf` eq 2.5 — integrability condition I_ψ(θ)<∞ | Mathematician | CONFIRMED |
| `Horizontes…md:102` — `C1_IS_ONLY_AN_EMPIRICAL_DETECTOR` (Entregable B) | All | CONFIRMED |
| `Horizontes…md` L₁ (~:111) — "Estabilización Débil del Corte", stabilization barrier (LPS 2016) | Mathematician, Repro | CONFIRMED with nuance: LPS 2016 (ref [15]) is the blocking stabilization framework (body :20,:94); the L₁ table row :111 cites ref [16] (Schulte–Yukich 2019) as the *tool*; TY itself is ref [13]. PR003's "anchored to LPS 2016" correctly names the barrier; the table attributes tools to [16]. |
| `Horizontes…md:116` — L₆ covtree stem σ-algebra rogue set | All | CONFIRMED |
| `Horizontes…md:166` — `CREDIBLE_ONLY_AS_SEMICLASSICAL_PROGRAM` (§6) | All | CONFIRMED |
| KPZ/Tracy–Widom transversal 2/3, longitudinal 1/3 (BDJ 1999, Johansson 2000) | Mathematician (self-flagged [UNVERIFIED]) | UNVERIFIED — BDJ 1999 present in biblioteca only as ref [5] of `derived-md/Dynamics_of_Causal_Sets_…md` (cited :292 for longest-chain fluctuations via LIS). No biblioteca source states the explicit 2/3 transversal / 1/3 longitudinal DLPP exponents; Johansson 2000 absent. Horizontes ref [11] (permuton limits) attached to the Tracy–Widom claim :15 is inconsistent. PR003 correctly self-flags [UNVERIFIED]. |
| `derived-md/Towards black-hole horizons…md:191,193,195,463` — bimodal future-cardinality; Hayward/regular-BH diagnostic failure | Physicist | CONFIRMED (all four lines) |

- **Notes:** (1) Citation-3 page error (p.6→p.3), substance supported. (2) eq 2.4 is p.8 not p.9. (3) L₁ reference ambiguity: ref [15] LPS=barrier, [13] TY=path-forward, [16] Schulte–Yukich=tool; PR003 correctly names the barrier. (4) KPZ exponents UNVERIFIED in biblioteca (Johansson 2000 absent; BDJ 1999 present only via a reference list) — the open analytic step's key exponent has no committed primary source in `biblioteca/`.

## 8. Synthesis
**Recommended direction:** Re-grade Lemma L₁ — but to a **precisely-worded contingent status**, not an unconditional "OPEN".

The four expert/control roles converge on the substance and split only on the *grade label*:
- **Agreement (4 roles):** The original `IMPOSSIBLE` verdict was anchored to *stabilization*, a **sufficient** condition for Malliavin–Stein. TY 2026 (Thm 2.1, no stabilization assumed; Def 2.3, laws-not-realizations — both CONFIRMED by the literature verifier from the primary PDF) shows that sufficient condition is **unnecessary**. No published impossibility theorem is overturned; a too-strong hypothesis is replaced by a strictly weaker one (BL-localization). Therefore `IMPOSSIBLE` is **no longer supported**. The mathematician (JUSTIFIED), physicist (statistical-foundations upgrade, no over-claim), and warden (PASS) concur. Unanimous on (c) L₆ + §6 INTACT and (d) seal/freeze UNTOUCHED.
- **Open disagreement (falsifier vs mathematician/physicist/warden), NOT hidden:** the falsifier argues the grade must be **PARTIALLY-OPEN / CONTINGENT**, not OPEN, because the strategy rests on one conceded unproven load-bearing step (`D_{x'}Φ` unbounded; "flux profile invariant under coherent re-indexing" is [PLAUSIBLE-TRANSFER]) plus an un-sketched integrability claim (`I_ψ(θ)<∞` on the growing `ℓ^{2/3}` domain) whose key KPZ exponent has **no committed primary source in biblioteca** (literature verifier: Johansson 2000 absent). The mathematician's own "required corrections before this becomes a lemma" (relabel score functional; prove `I_ψ`; close the level-vs-profile step) is, in substance, the falsifier's contingency list.

**Chair's resolution of the split:** the disagreement is about labelling, not facts — both sides agree exactly which steps are proven and which are not. The honest grade that satisfies both is:

> **Lemma L₁: re-graded IMPOSSIBLE → OPEN–CONTINGENT.** The impossibility (anchored to stabilization) is withdrawn; a concrete strategy (BL-localization, TY Def 2.3) is identified; the grade is *contingent* on two named sub-lemmas:
> - **L₁a (profile-invariance / bounded-effect control):** control the moment integrals of the *unbounded* operator `D_{x'}Φ` in TY Thm 2.1 — i.e. show the coherent global re-indexing of `s` leaves the flux law `d_BL`-close to its short-range truncation despite `D_{x'}Φ` being unbounded.
> - **L₁b (integrability):** establish `I_ψ(θ)<∞` for the anchored flux score on the unbounded domain with tube cross-section `∝ ℓ^{2/3}`, via the DLPP transverse tail.

This is not a PROCEED-to-a-committing-step; it is a reversible documentation re-grade. The warden returned **PASS** (no BLOCK), so a PROCEED verdict is admissible under the freeze invariant. The falsifier raised **no freeze violation and no unresolved leakage of the observable** — the "geodesic tube" concern is about the *proof technique's language*, not the definition of `Φ` (which is order-only: `s(x)`, `Σ_ℓ`, crossing count). It is recorded as a binding caveat (C3 below), not a block.

**Ranked alternatives:**
1. **(Recommended) Re-grade to OPEN–CONTINGENT** with sub-lemmas L₁a/L₁b named, the prereg-003 firewall binding (C1), and the dev note committed for an auditable trail (C2). Then sketch `I_ψ(θ)` (the falsifier's minimal test) as the next analytic step.
2. Re-grade to plain OPEN (mathematician's literal proposal). Rejected: under-states the conceded unproven load-bearing step; the falsifier's "treats plausibility as proof" critique stands.
3. Leave at IMPOSSIBLE / REVISE-AND-RECONVENE. Rejected: factually wrong — the impossibility's sole support (stabilization necessity) is refuted by TY, CONFIRMED from the primary source by two independent roles.

**Binding caveats carried into the verdict:**
- **C1 (prereg-003 firewall):** the re-grade of L₁ does NOT touch, re-open, or license revisiting the frozen `z*` / `K_LOC=2` operational floor. Any threshold change needs a new prereg + seal + audit (warden's binding condition). The dev-note §6 sentence is to be softened to make its conditional, non-authorizing status explicit.
- **C2 (independent-trail):** commit the dev note so the re-grade has a hash-anchored auditable trail (the support report is git-ignored). Partial mitigation of the falsifier's author=verifier gate already exists: the three Wave-1 experts + literature verifier independently re-derived/confirmed the load-bearing TY citations and the `D_{x'}s∈{0,1}` argument from the primary PDF this session.
- **C3 (no covert geometry in the eventual proof):** when L₁a/L₁b are written, the tube/locality scale must be characterised order-theoretically (the longest chain is order-only; "geodesic"/"transversal" are continuum descriptions used to *benchmark*, never to *define* `Φ`). Re-assert NO_GROUND_TRUTH_LEAKAGE at proof time.
- **C4 (finite-patch gap):** TY's infinite-time setup vs the project's finite patch (boundary/lenticular spurious minima) is an additional un-closed item to address before L₁ is a finished lemma.
- **C5 (labelling):** `Φ(ℓ)` is a Poisson *score functional* (globally-dependent kernel), not a U-statistic — correct the dev note. L₁ ≠ L₂ (TY gives the marginal/joint CLT; the `z*` scaling needs EVT atop).

## 9. Next-step spec
**Reversible (may be run now if the user asks):**
1. **Edit the dev note** `dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md`: (a) re-grade L₁ to **OPEN–CONTINGENT** with sub-lemmas L₁a/L₁b named (§6/§8 wording above); (b) correct "U-statistic" → "order-2-indexed Poisson *score functional*" (C5); (c) soften the §6 prereg-003 sentence to its non-authorizing conditional form (C1); (d) add C3/C4 as explicit open items. Guard: `make verify-seal` must print `6e2c3888…` before and after (a markdown edit cannot change it — invariance = proof of non-touch).
2. **Re-grade the support report** `biblioteca/Horizontes En Conjuntos Causales.md` Entregable B/C L₁ row to OPEN–CONTINGENT (git-ignored; the committed dev note is the auditable record).
3. **Commit the dev note** (C2) for a hash-anchored trail. *(A commit is a repo action — perform only on explicit user instruction, on `main`, atomically, never touching the sibling `formula` branch checkout.)*
4. **Sketch L₁b — the falsifier's minimal falsification test (the user's requested next analytic step):** write the `I_ψ(θ)` integral for the anchored flux score explicitly, `ψ(r)=sup_z sup_{|A|≤5} d_BL(Law(ξ(z,P)), Law(ξ^[r](z,P+A)))` with tube cross-section `∝ ℓ^{2/3}`, and evaluate whether `∫ ψ(r) dr < ∞` **uniformly in ℓ**. Divergence ⇒ BL-localization fails for Φ ⇒ L₁ reverts toward IMPOSSIBLE. Convergence sketch ⇒ L₁b plausibly closes. This sketch is dev/analytic, cites a primary KPZ source (the literature verifier found none in biblioteca — fetch BDJ 1999 / Johansson 2000 or mark the exponent [UNVERIFIED] until fetched).

**Committing steps (only on explicit user authorisation):** none in scope. No prereg, no seal change, no `validate.run()`, no seed draw. Any attempt to convert L₁b/L₁a into a change of `z*`/`K_LOC` is a NEW pre-registration (C1).

**Pre-committed binding rules:** C1 (prereg-003 firewall), C2 (commit the trail), C3 (no covert geometry in the proof), C4 (finite-patch gap is open), C5 (score-functional labelling; L₁≠L₂). Tokens enforced: `RESPECT_SEAL_FREEZE`, `NO_THRESHOLD_LOOSENING`, `NO_POST_HOC_TUNING`, `NO_GROUND_TRUTH_LEAKAGE`, `NO_RECONSTRUCTION_CLAIM`.

**Minimal falsification test (falsifier's, adopted):** the `∫ ψ(r) dr < ∞` uniform-in-ℓ check of step 4 — it is simultaneously the next analytic deliverable and the test that would expose the worst failure.

## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_CAVEATS

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_

```

### /home/adnac/nachocausal/dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md

Bytes: 27958
SHA256: 381e5d5bd42aa1b2df2c9bba8c2c75abce133ca3f63ec7351c18c204824bb201

```text
# PR-003 — BL-localización (Trauthwein–Yukich 2026) como ruta a la ley nula de C1 (dev, NOT a result)

Nota de sandbox. **Análisis teórico, nada medido, nada congelado, ningún claim.** Su valor es
re-evaluar un veredicto previo de la literatura de apoyo a la luz de un paper que el propio informe
citó pero aplicó bajo un marco más fuerte (y por tanto más restrictivo) del necesario.

## 0. Origen

El documento de apoyo `biblioteca/Horizontes En Conjuntos Causales.md` (git-ignored) audita el
candidato **C1** (altura intrínseca `s(x)`, foliación por ideales `Σ_ℓ`, flujo `Φ(ℓ)` normalizado
mediana/MAD, umbral `z*`) y emite dos veredictos:

- Entregable B (Dossier C1): `C1_IS_ONLY_AN_EMPIRICAL_DETECTOR`.
- §6 (global): `CREDIBLE_ONLY_AS_SEMICLASSICAL_PROGRAM`.

El Dossier B descansa en dos patas independientes:
1. **Pata semiclásica (Lema L₁):** "C1 carece de ley nula analítica porque `Φ` no estabiliza — el
   add-one cost de la altura no decae (un punto en el pasado profundo reordena toda la foliación),
   lo que bloquea Malliavin–Stein."
2. **Pata cuántica (Lema L₆):** "el min sobre cortes requiere el futuro asintótico → C1 es un
   *rogue set* no medible en la σ-álgebra de stems del covtree (Dowker–Zalel)."

Esta nota ataca **sólo la pata 1.** La pata 2 queda intacta (ver §5).

## 1. Qué prueba Trauthwein–Yukich (arXiv:2605.23292, "Second-order Poincaré inequalities and
   localization on the Poisson space", 22 May 2026; PDF en biblioteca)

- **Teorema 2.1 (p.5):** cota de 2º orden de Poincaré / Malliavin–Stein afilada para CUALQUIER
  funcional de Poisson `F` con `𝔼F=0` y momento finito de los operadores diferencia. Da
  `d_W(F,N), d_K(F,N) ≤ Σ_{i=0}^{6} γ̂_i`, con cada `γ̂_i` una integral de **cuartos momentos** de
  los operadores diferencia de 1er y 2º orden `D_xF`, `D²_{x,y}F` (def. p.4). **A este nivel NO se
  exige estabilización alguna** — sólo momentos cuartos finitos. Elimina los términos `γ₃,γ₄`
  (el `𝔼F⁴` problemático) de Last–Peccati–Schulte 2016 (p.6, punto 1).
- **Definición 2.3 (p.8) — BL-localización:** condición estructural sobre un funcional de tipo
  suma-de-scores `H = Σ_z ξ(z,P)` que hace colapsar los `γ̂_i` a `O(1/√Var H)`, dando la cota
  Berry–Esseen `d(H̃,N) = O(1/√Var H)` (eq. 1.3).

## 2. El punto clave: BL-localización es ESTRICTAMENTE más débil que estabilización

Cita textual (p.8):

> "BL-localization establishes closeness in the `d_BL` metric between the **laws** of the random
> variables ξ and their short-range versions ξ^[r], in contrast to 'stabilization', a notion
> comparing **specific realizations** of the scores — either exactly (via stopping sets) or
> approximately in L^q."

Y (p.6): "weaker and more flexible than the standard stopping set stabilization criterion … it
also **allows for interactions of scores at distant points**."

La objeción del informe (`D_{x'}s(x)` no decae) es una afirmación sobre **realizaciones
específicas** (estabilización L¹/stopping-set). BL-localización **no la usa**. Sólo pide que la
**distribución** del score local sea aproximable (en `d_BL`) por la de un score de rango corto,
uniformemente sobre cuádruplas y sobre configuraciones añadidas `𝒜` de tamaño ≤5 (eqs. 2.3–2.4).
**El informe descalificó C1 con el criterio antiguo; el criterio de 2026 no impone esa
descalificación.**

## 3. Mapeo sobre C1 — [PLAUSIBLE-TRANSFER], NO probado

- `Φ(ℓ) = Σ_{(x,y): x≺y, s(x)≤ℓ<s(y)} 1 = Σ_{z∈P} ξ(z,P)` es un **funcional de score de Poisson
  con indexado de orden 2** (no una U-estadística: el indicador de cruce depende de `s(·)`, un
  funcional GLOBAL de `P`, no de un núcleo que dependa sólo del par `(x,y)`). Anclando cada par en
  su punto superior `z=y`, `ξ(z,P) = #{x≺z : s(x)≤ℓ<s(z)}` — exactamente la forma `H=Σ_z ξ(z,P̂)`
  para la que TY Setup p.7 está construido, y precisamente NO la maquinaria U-estadística / caos de
  Wiener finito. [Corrección C5, comité 007.] El montaje espacio-temporal `X×ℝ` con **horizonte
  temporal infinito** (Setup p.7) = sprinkling con futuro no acotado.
- Dos detalles que invierten la intuición del informe:
  - El add-one cost de la **altura misma** es `D_{x'}s(x) ∈ {0,1}` (añadir un punto sube la cadena
    más larga en a lo sumo 1). Lo NO acotado es el **número** de `x` afectados — y eso es justo lo
    que mata la estabilización clásica pero **no** la BL-localización (que mira leyes, no
    realizaciones). Un reordenamiento global *coherente* de la etiqueta de altura re-indexa el corte
    pero deja el perfil de flujo, expresado en la propia foliación order-only por altura, aprox.
    invariante. La "posición geodésica" es sólo el benchmark semiclasico usado para razonar sobre
    el límite manifoldlike, no un dato que defina `Φ`.
  - En el benchmark continuo del orden producto 1+1D, la cadena más larga hasta `x` vive, con alta
    probabilidad, en un **tubo** de anchura transversal `~ℓ^{2/3}` alrededor de la geodésica
    correspondiente (exponente transversal 2/3 de la percolación de último paso dirigida / Ulam;
    *estándar, no re-derivado aquí*). Esto orienta la prueba de localización, pero la definición de
    `s(x)` y `Φ` sigue siendo puramente order-only.
- Dos rasgos de TY hechos a medida:
  1. **Decaimiento integrable, NO exponencial:** sólo se exige `I_ψ(θ)<∞` (eq. 2.5) y `I_φ(θ')<∞`
     (eq. 2.6), "a mild integrability condition" (p.3). Un `ψ(r)` polinómico/estirado (cola KPZ)
     podría bastar. Estabilización exigía decaimiento exponencial; aquí no.
  2. **Radio dependiente de la geometría:** TY permite que `ξ^[r]` "be dependent on the geometry of
     the balls `B_r(·)`" (p.9) y formaliza **localización en tiempo** (Def. 2.3, eq. 2.2/2.4) para
     scores de soporte temporal creciente — exactamente el tubo `ℓ^{2/3}`.

## 4. Gaps honestos (lo que aún hay que probar para convertir esto en lema)

1. **Establecer `ψ(r)` para el score de flujo** vía el exponente transversal de la DLPP y verificar
   `I_ψ(θ)<∞`. Es acotar una cola conocida, no inventar una propiedad nueva. → siguiente paso
   analítico (bosquejo pendiente).
2. **`Φ` vs el estadístico real de C1.** TY da la ley nula **marginal/conjunta de un nº finito de
   cortes** `φ(ℓ)` (Gaussiana, tasa Berry–Esseen). El estadístico de C1 es `min_ℓ φ(ℓ)` sobre una
   familia *creciente* de cortes correlacionados → **scan/extreme-value statistic**, no un CLT de
   Poisson directo. Por tanto:
   - TY ataca el **Lema L₁** (ley nula de los cortes) — el que estaba marcado "impossible".
   - TY **alimenta** el **Lema L₂** (`z* ~ √(2 log N_eff)`) pero no lo prueba: hace falta EVT de
     máximos de Gaussianas dependientes ENCIMA del CLT marginal de TY. Ese `√(2 log N_eff)` es el
     que el informe ya marcó `[THEOREM-CONFIRMED]` y que toca el floor operacional de prereg-003.

## 5. Qué NO toca

TY es una CLT **cinemática** sobre sprinkling de Poisson. No dice nada sobre la σ-álgebra de stems
del covtree. El veredicto cuántico (C1 = *rogue set*, Lema L₆, §6 del informe) **permanece
intacto.** TY no rescata la aspiración de "observable cuántico relacional".

## 6. Re-graduación (adjudicada — comité 007, RECOMMEND_PROCEED_WITH_CAVEATS)

- **Entregable B / Lema L₁:** de `IMPOSSIBLE` → **`OPEN–CONTINGENT`**. La imposibilidad (anclada a
  estabilización, una condición SUFICIENTE) se retira: TY Thm 2.1 no la asume y Def. 2.3 compara
  LEYES, no realizaciones. Se identifica una estrategia concreta, pero el grado es *contingente* de
  dos sub-lemas nombrados:
  - **L₁a (control del operador no acotado / invarianza de perfil):** acotar los momentos de
    `D_{x'}Φ` (UNbounded — el `{0,1}` es de `s`, no de `Φ`) en TY Thm 2.1; i.e. mostrar que el
    re-indexado global coherente de `s` deja la ley del flujo `d_BL`-cercana a su truncación de
    rango corto pese a `D_{x'}Φ` no acotado.
  - **L₁b (integrabilidad):** establecer `I_ψ(θ)<∞` para el score de flujo anclado en el dominio no
    acotado con sección de tubo `∝ ℓ^{2/3}`, vía la cola transversal DLPP. → bosquejada en §8.
- **Veredicto global §6:** SIN CAMBIO (`CREDIBLE_ONLY_AS_SEMICLASSICAL_PROGRAM`); la barrera
  cuántica L₆ es independiente y queda intacta.
- **Conexión prereg-003 [FIREWALL C1, vinculante]:** *condicional y NO autorizante.* SI L₁a+L₁b se
  cerraran, TY + EVT *sería* el backbone de un escalado `z* ~ √(2 log N_eff)`. Esta observación
  teórica **NO autoriza** modificar `z*`, `K_LOC=2`, `theta_loc`, `theta_stab` ni `P_PERM_THRESHOLD`
  donde están congelados/operativos. Cualquier cambio de un umbral congelado requiere una NUEVA
  pre-registración con nuevo sello, auditoría independiente y autorización explícita — idéntico al
  proceso que produjo `docs/preregistration_003.md`. L₁ ≠ L₂: TY da sólo el CLT marginal/conjunto;
  el escalado de `z*` necesita EVT de máximos de Gaussianas dependientes ENCIMA.
- **Gaps abiertos adicionales [comité 007]:** C3 (sin geometría encubierta en la prueba: el tubo y
  la escala de localidad deben caracterizarse orden-teóricamente; "geodésica"/"transversal" son
  descripciones del continuo usadas para *benchmark*, jamás para *definir* `Φ`); C4 (gap
  parche-finito vs montaje tiempo-infinito de TY: efectos lenticulares de borde no modelados).

## 8. Bosquejo de la cota ψ(r) desde el exponente transversal (L₁b) — dev analítico, NO probado

Siguiente paso analítico solicitado; coincide con la prueba de falsación mínima del comité 007
(`∫ ψ(r) dr < ∞` uniforme en ℓ). Esto es un BOSQUEJO: cierra L₁b a escala fija y aísla qué queda
abierto (L₁a). Todo paso del continuo es *benchmark*, no entra en la definición de `Φ` (C3).

### 8.1 La identidad estructural: orden causal 1+1D = orden producto 2D

En Minkowski 1+1D plano (la hipótesis nula), en coordenadas de cono de luz `u=t−x`, `v=t+x`:
`p ≺ q ⇔ u_p ≤ u_q ∧ v_p ≤ v_q`. **El orden causal ES el orden producto (coordenada a coordenada)
en el plano `(u,v)`.** Por tanto un causal set de Minkowski 1+1D = un **orden aleatorio 2D** de un
proceso de Poisson de intensidad ρ en el plano `(u,v)` (Surya LRR §4; el hecho 2D-order es estándar
en CST). Consecuencias inmediatas:

- `s(q)` = cadena máxima desde mínimos hasta `q` = **subsecuencia creciente más larga (LIS) /
  last-passage dirigido** hasta `q` — el problema de Ulam/Hammersley poissonizado.
- Entre dos puntos separados `(Δu, Δv)`, la cadena máxima tiene longitud
  `L ≈ 2√(ρ Δu Δv)` con fluctuaciones **Tracy–Widom** de orden `L^{1/3} ∝ (ρΔuΔv)^{1/6}` — la
  clase de universalidad KPZ. **Exponente longitudinal 1/3 + límite TW CONFIRMADOS**: Sasamoto–Spohn
  2010 (`biblioteca/1002.1879v2.pdf`) eq. (1.5) `h(0,t) ≅ −½(q−p)t + 2^{−1/3}((q−p)t)^{1/3} ξ_TW`
  con `ξ_TW` Tracy–Widom (eqs. 1.6–1.7, núcleo de Airy). La pertenencia de la cadena más larga del
  causal set 1+1D a esta clase es vía LIS poissonizada (BDJ 1999; Surya §4.3).
- Como `Δu Δv = τ²` (tiempo propio al cuadrado, salvo constante), `s ≈ 2√ρ · τ` → **la altura es
  proporcional al tiempo propio.** El nivel `ℓ` corresponde a `τ_ℓ = ℓ/(2√ρ)`.

### 8.2 La cola transversal (el insumo KPZ)

La cadena maximizante entre extremos separados tiempo propio `T` se concentra en un **tubo** en
torno a la recta geodésica del continuo. **La ESCALA transversal 2/3 está anclada** por dos vías:
Sasamoto–Spohn 2010 (`biblioteca/1002.1879v2.pdf`, Introducción p.2) — "the height fluctuations will
grow as `t^{1/3}`, while the **transverse correlation length increases as `t^{2/3}`**" — y, como
teorema directo para el modelo poissoniano de subsecuencias crecientes, Johansson 2000,
*Transversal fluctuations for increasing subsequences on the plane* (NO en biblioteca; fuente
primaria leída externamente). A nivel `ℓ`, `T ∝ ℓ`, luego la escala transversal del tubo es
`∝ ℓ^{2/3}`.

**La FORMA de la cola es donde hay que ser preciso [corrección de fuente primaria].** La cola
cúbica `P(W>r) ≤ C exp(−c (r/ℓ^{2/3})³) = C exp(−c r³/ℓ²)` que usé en una primera versión **NO está
literalmente probada por Johansson 2000**: su prueba usa colas longitudinales tipo Tracy–Widom y
obtiene, para excluir desviaciones `r=N^γ`, una estimación `~exp(−c N^{6γ−4})`, que reescrita en `r`
da `~exp(−c r⁶/N⁴)` (cola **sextica**, no cúbica). Esto no refuta la cola cúbica; muestra que esa
atribución concreta a Johansson **no está sustentada** → la forma cúbica queda **[UNVERIFIED]**.

**Lo que sí es robusto:** ambas colas (la cúbica `exp(−c r³/ℓ²)` y la sextica de Johansson
`exp(−c r⁶/ℓ⁴)`, ya que su escala `N^{2/3}` ↔ `ℓ^{2/3}`) **cruzan en `r ~ ℓ^{2/3}`** y dan el MISMO
`∫ r ψ dr ~ ℓ^{4/3}` (§8.4). La convergencia depende de la **escala 2/3** (anclada), NO de la forma
de la cola. La forma cúbica es ilustrativa; el insumo crítico es la escala.

### 8.3 ψ(r) para el score de flujo

Truncación de rango corto `ξ^[r](z,P)`: calcular `s(z)` y los socios de cruce `x≺z` usando sólo
puntos dentro de radio `r` de `z` (en la métrica del plano `(u,v)`). `ξ ≠ ξ^[r]` exige que la cadena
máxima que fija `s(z)` (o el cruce de un socio por el corte) use un punto fuera del tubo de radio
`r`. Por §8.2, a nivel `ℓ`:

  **ψ(r) ≲ C exp(−c r³ / ℓ²).**

Decaimiento estirado/cúbico-exponencial — más fuerte que la integrabilidad *suave* que TY exige
(eq. 2.5), pero con **escala fijada por ℓ** (no radio fijo). Esto es exactamente lo que la
estabilización clásica (radio fijo, decaimiento exponencial) no captaba y BL-localización sí admite.

### 8.4 La integral de localización a escala fija (cierra L₁b a ℓ fijo)

`ν` = Lebesgue 2D (`ρ du dv`); en coordenadas polares el elemento de volumen es **`r dr`**
(explícito, no `dr`). La integral relevante de TY eq. 2.5, **condicional** a una cota uniforme
`ψ_ℓ(r) ≤ C exp(−c r³/ℓ²)`:

  `∫₀^∞ r ψ_ℓ(r) dr ≤ C ∫₀^∞ r exp(−c r³/ℓ²) dr`.

Sustituyendo `r = ℓ^{2/3} s` (⇒ `r dr = ℓ^{4/3} s ds`), con `∫₀^∞ s e^{−c s³} ds = (1/3) c^{−2/3} Γ(2/3)`:

  `= (C/3) c^{−2/3} Γ(2/3) · ℓ^{4/3} < ∞.`

(Con la cola sextica de Johansson `exp(−c r⁶/ℓ⁴)`: `r = ℓ^{2/3} s`, `∫ s e^{−c s⁶} ds` constante ⇒
**mismo `ℓ^{4/3}`**. La forma de la cola sólo cambia la constante, no el exponente.)

**Conclusión L₁b — CONDICIONAL, no teorema:** *si* se prueba la cota uniforme de cola con escala
`ℓ^{2/3}` (cualquier forma que decaiga), *entonces* `I_ψ(θ) ~ ℓ^{4/3} < ∞` a cada escala `ℓ`. La
cuenta es correcta; **la localización existe donde la estabilización fallaba**. Pero L₁b NO está
cerrado como teorema: queda condicional a (a) la cota de cola con su escala 2/3, y (b) **el paso
"orden producto 1+1D ⇒ las hipótesis exactas del modelo LPP de Johansson aplican al observable
causal concreto"**, que debe FORMULARSE, no asumirse por analogía KPZ. [gap L₁b-(b), nuevo]

> **Corroboración independiente del 4/3:** el exponente `ℓ^{4/3}` que sale aquí coincide con el
> exponente KPZ conocido `t^{4/3}` de la varianza de la función de dos puntos estacionaria
> (Sasamoto–Spohn 2010 p.2, citando bounds de Balázs–Quastel–Seppäläinen [ref. 2]). No es
> coincidencia: ambos integran la escala transversal 2/3 sobre la estructura 2D. Esto da confianza
> en que la sustitución `r = ℓ^{2/3}s` y el resultado `ℓ^{4/3}` son la física KPZ correcta, no un
> artefacto del bosquejo.

### 8.5 Lo que NO cierra el bosquejo (queda en L₁a)

El que `I_ψ < ∞` a `ℓ` fija da BL-localización; la **tasa Berry–Esseen** de TY escala como
`~ I_ψ^a / √Var Φ(ℓ)`. Con `I_ψ ~ ℓ^{4/3}` creciendo con la escala, el CLT con tasa **no trivial**
exige `Var Φ(ℓ)` creciendo lo bastante rápido para dominar. Calcular `Var Φ(ℓ)` (cuántos cruces y
su covarianza a nivel `ℓ` en el orden 2D) es la tarea analítica genuina restante = **L₁a**, ligada
al operador no acotado `D_{x'}Φ`. El bosquejo NO la resuelve; la deja como el cuello real.

**Veredicto del bosquejo:** L₁b cierra **CONDICIONALMENTE** (integral convergente exhibida, dado
(a) la cota de cola con escala 2/3 y (b) la aplicabilidad del modelo LPP al observable causal); L₁a
sigue abierto (interacción I_ψ-vs-Var en dominio creciente). Coherente con `OPEN–CONTINGENT`, **no
hay base para volver a IMPOSSIBLE, ni para elevar a `OPEN` pleno**. La integral `∫ r ψ dr` da
**finito a ℓ fija pero creciente como ℓ^{4/3}** — exactamente la frontera que L₁a debe domar.

## 9. L₁a — Var Φ(ℓ) en el orden 2D y control de `D_{x'}Φ` (dev analítico, HEURÍSTICO, NO probado)

Escalas del parche (cuadrado de lado `U` en `(u,v)`, intensidad `ρ`): `N = ρU²` puntos; altura
máxima `L_max ≈ 2√(ρU²) = 2√N` (Ulam/LIS, §8.1); número de niveles `~2√N`; **antichain por nivel
`|Σ_ℓ| ~ √N`** (`= √ρ U`). Todo "geodésica/transversal" es benchmark del continuo, NO entra en la
definición de `Φ` (C3).

### 9.1 Resultado forzado: el flujo DEBE ser de *enlaces* (covering-links), no de relaciones

El conteo de **relaciones transitivas** que cruzan el corte, `Φ_rel(ℓ)=#{x≺y : s(x)≤ℓ<s(y)}`, es
**no local**: un único `y` profundo en el futuro es comparable con `~ρ·u_y v_y` puntos pasados, casi
todos bajo el corte ⇒ `D_{x'}Φ_rel` crece con el **área** del parche, sin cola integrable. **BL-loc
FALLA para `Φ_rel`.** El objeto correcto es el **flujo de enlaces** (relaciones de cobertura,
intervalo vacío) que cruzan el corte:

  `Φ(ℓ) := #{ x⋖y : s(x)≤ℓ<s(y) }`,

que coincide con la `β` de covering-links del comité 006 (`docs/comite/comite_decision_006_*`).
**Primera conclusión de L₁a: el programa de localización OBLIGA a usar el flujo de enlaces; la
variante transitiva está muerta para Malliavin–Stein.** (Esto refina C5 y la definición de C1.)

### 9.2 `Var Φ(ℓ)` — escala [HEURÍSTICO]

Los enlaces que cruzan están anclados en la membrana ≈ hiperbola `uv = ℓ²/4ρ` (tiempo propio
constante). El nº de enlaces por elemento en un orden 2D de Poisson `~ log N` (la integral de
intervalo-vacío `ρ∫∫e^{−ρab}da db` es log-divergente, cortada por la caja). Enlaces que cruzan
`~ |Σ_ℓ| × O(1)` por celda de corte ⇒ `E[Φ(ℓ)] ~ √N` (salvo factores log). Si las contribuciones a
lo largo de la membrana (sistema efectivamente 1D de longitud `~U`) son **localmente dependientes**
con correlación que decae en la escala KPZ, entonces

  **`Var Φ(ℓ) ~ E[Φ(ℓ)] ~ √N`** (polylog) — [HEURÍSTICO, fluctuación tipo-Poisson de suma de
  términos locales sobre una membrana 1D].

### 9.3 `D_{x'}Φ` — no acotado, pero ¿con momentos controlados?

Añadir `x'` cambia `Φ` por dos vías: (i) **enlaces incidentes a `x'`** (creados/destruidos: `x'`
puede caer en un intervalo antes vacío y romper un enlace) — número `K_{x'}` con media `~log N` y
cola integrable; (ii) **re-clasificación por el desplazamiento de altura** `Δs∈{0,1}` que `x'`
propaga en su tubo futuro. El **soporte** del tubo en el corte tiene anchura transversal `~ℓ^{2/3}`
(§8.2), que intersecta `~√ρ·ℓ^{2/3}` puntos de `Σ_ℓ`. **AQUÍ está el cuello:**

- **Lectura A (localidad-absoluta, pesimista):** si una *fracción constante* de esos `~ℓ^{2/3}`
  puntos cambia de altura ⇒ `D_{x'}Φ ~ ℓ^{2/3} ~ N^{1/3}` para CADA uno de los `~N` puntos
  interiores ⇒ `∫ E[|D_{x'}Φ|⁴] ν ~ N·N^{4/3} = N^{7/3}`. Con `Var~√N`, la tasa de TY **diverge**.
  → L₁ revertiría hacia IMPOSSIBLE.
- **Lectura B (localidad-condicional, optimista):** el nº de `z` cuya altura *realmente* cambia al
  añadir `x'` = los `z` cuya **cadena máxima pasa por `x'`**, que es `O(1)` genérico (la cadena
  óptima a casi todo `z` NO atraviesa un `x'` dado; unicidad a.s. de la geodésica de last-passage).
  El `ℓ^{2/3}` es el **soporte** (quién *podría* afectarse), no el desplazamiento *realizado*, que es
  **disperso**. ⇒ `E[|D_{x'}Φ|⁴]` uniformemente `O(polylog)`, cola integrable. Entonces `∫ E|DΦ|⁴ ν
  ~ N·polylog` y la tasa de TY → 0 (escala `~ N^{−1/4}` polylog, suma de `~√N` celdas casi-indep).
  → L₁ cierra (OPEN → hacia CONFIRMED).

### 9.4 L₁a reducido a UNA conjetura nítida con regla de decisión

> **Conjetura de localidad-condicional (L₁a):** el flujo de enlaces, expresado *relativo a su propia
> foliación por altura*, tiene radio de localización efectivo por-score = la escala LOCAL inter-nivel
> `O(1)` (en altura), NO el `ℓ^{2/3}` global que necesita la altura *absoluta* `s`. Equivale a la
> versión rigurosa de "el re-indexado coherente deja el perfil de flujo invariante" (§3, §6).

- Si **VERDADERA** ⇒ `I_ψ` acotado por la escala local (no `ℓ^{4/3}`), `Var~√N`, tasa `~N^{−1/4}→0`
  ⇒ **L₁ graduaría OPEN-CONTINGENT → (camino a) CONFIRMED.**
- Si **FALSA** (el rango de nivel-absoluto `ℓ^{2/3}` es irreducible) ⇒ tasa diverge ⇒ **L₁ revierte
  hacia IMPOSSIBLE.**

El cálculo de escala por sí solo NO decide entre A y B: depende de la **dispersión del
desplazamiento de altura realizado** (¿cuántos `z` reenrutan su cadena máxima por un `x'` dado?). Esa
es la cantidad decisiva y es **directamente medible**.

### 9.5 Prueba decisiva (dev, reversible — propuesta, NO ejecutada)

`dev/measure_*.py` (venv sellado numpy 1.26.4, DEV_SEEDS, jamás VALIDATION_SEEDS; no toca umbrales
sellados; seal `6e2c3888…` pre+post). Medir en sprinklings de Minkowski plano, para `N` creciente:
1. `Var Φ_link(ℓ)` vs `N` en el corte bulk → confirmar/refutar el exponente `√N` (§9.2).
2. La **distribución de `D_{x'}Φ_link`** (add-one cost empírico: re-sprinkle quitando/poniendo `x'`)
   → media, cola, y sobre todo el **nº de `z` con altura cambiada por `x'`** (Lectura A vs B, §9.3).
3. El **rango de correlación** del flujo de enlaces a lo largo de la membrana → ¿escala local `O(1)`
   o global `ℓ^{2/3}`? (decide la conjetura §9.4).
Decisión: A ⇒ documentar reversión de L₁; B ⇒ documentar camino a cierre. Resultado reportado igual
sea cual sea (regla de reporte simétrica).

### 9.6 Resultado del probe (EJECUTADO — dev, EMPÍRICO, tasa heurística)

`dev/measure_bl_localization_l1a.py`, log `dev/bl_localization_l1a.log`; venv sellado numpy 1.26.4;
8 DEV_SEEDS; Minkowski plano; corte bulk = mediana de altura; `N ∈ {207, 410, 814, 1620}`; seal
`6e2c3888…` verificado pre y post. **Corrección importante que los datos imponen al §9.3/§9.4:** el
operador decisivo NO es `#shifted` (re-indexado de alturas) sino **`D_{x'}Φ` (cambio de flujo)**.

| N | E[Φ] | Var[Φ] | Var/√N | #shifted | mean\|DΦ\| | max\|DΦ\| | frac(DΦ≠0) | #contrib/√N |
|---|---|---|---|---|---|---|---|---|
| 207 | 41.5 | 196.6 | 13.7 | 8.0 | 0.76 | 12 | 0.241 | 3.46 |
| 410 | 77.8 | 321.9 | 15.9 | 11.8 | 0.38 | 9 | 0.178 | 3.61 |
| 814 | 158.8 | 452.5 | 15.9 | 18.0 | 0.50 | 12 | 0.175 | 4.99 |
| 1620 | 323.6 | 560.0 | 13.9 | 35.2 | — | — | — | — |

Tres hallazgos:
1. **`Var Φ(ℓ) ~ √N`** — `Var/√N` PLANO (13.7→15.9→15.9→13.9) sobre 8× en N. Confirma §9.2. ✓
2. **El re-indexado de alturas NO es disperso** — `#shifted ~ N^{0.7}` (8→35), incluso más rápido
   que el N^{1/3} de la Lectura A. Las etiquetas de `s` se mueven masivamente al quitar `x'`.
3. **PERO el operador de flujo `D_{x'}Φ` está CONTROLADO** — `mean|DΦ|` y `max|DΦ|` acotados
   (~0.5, ~12) sin tendencia con N, y la **fracción de `x'` con `DΦ≠0` DECRECE** (0.24→0.175) ⇒
   `#contrib` crece **sub-linealmente** (~N^{0.65}, frac↓). Esto es literalmente "el re-indexado
   coherente deja el perfil de flujo invariante" (§3, §6) — **medido**.

**Veredicto del probe (Lectura B favorecida, NO prueba):** con `|DΦ|` acotado por contribuyente,
`#contrib` sub-lineal y `Var ~ √N`, la tasa de Berry–Esseen **heurística** de TY
`d_W ~ (∫E|DΦ|⁴ ν)^{1/2}/Var ~ (N^{0.65})^{1/2}/N^{1/2} = N^{−0.18} → 0`. Robusto mientras
`#contrib` sea sub-lineal (cualquier α<1 da tasa→0; los datos dan frac↓ ⇒ α<1 claramente). **Esto
descarta la Lectura A (tasa divergente) EN EL RÉGIMEN NUMÉRICO EXPLORADO (`N≤1620`)** — el experimento
falsa esa lectura *operativa* concreta, NO es una refutación de un enunciado asintótico aún no
formalizado.

**Caveats honestos (por qué sigue OPEN-CONTINGENT, no CONFIRMED):**
- La fórmula de tasa es una **reducción dimensional heurística** de los γ̂ de TY (Thm 2.1); NO se
  computaron los términos de 2º orden `D²Φ`. [HEURÍSTICO]
- Sólo 3–4 N (207–1620) y 40 remociones/seed: el **exponente α de #contrib** (≈0.65) y la **cola del
  4º momento** de `|DΦ|` (vía `max` proxy) están poco constreñidos; un `x'` raro tipo "vértice de
  corte" del DAG de cadenas máximas podría engrosar la cola a N grande. [dev, muestreo limitado]
- **C4 no aislado:** el corte = mediana en una caja fija; los efectos lenticulares de borde no se
  separaron de bulk. Pendiente: corte bulk explícito lejos de bordes temporales.
- Falta el cierre **analítico** de la sub-linealidad de #contrib (unicidad a.s. de geodésica de
  last-passage ⇒ dispersión del desplazamiento *realizado*).

**Estado L₁a:** evidencia empírica **a favor de la localidad-condicional (cierre de L₁)**, con la
tasa→0 plausible; pero el grado se mantiene **OPEN-CONTINGENT** hasta (i) γ̂ completos de TY con
`D²`, (ii) prueba analítica de #contrib sub-lineal, (iii) cola del 4º momento a N grande, (iv)
aislamiento C4. El probe **descartó la Lectura A en el régimen numérico explorado**, no **probó** la B.
**L₁a queda CONGELADO** hasta resolver el mapeo L₁b-(b) (ver `dev/PR003_L1B_LPP_MAPPING_NOTES.md`):
afinar tasas Berry–Esseen sería correcto sobre el objeto equivocado si el puente LPP/KPZ falla.

## 7. Backing

- arXiv:2605.23292 (PDF en `biblioteca/2605.23292v1.pdf`): Teorema 2.1 (p.5), Def. 2.3 (p.8),
  eqs. 1.3/2.1–2.6, discusión "weaker than stabilization" (intro p.3 + §2.2 p.6; corrección de
  página del verif. de literatura, comité 007), montaje espacio-temporal (p.7), radio geométrico
  (p.9; eq. 2.4 está en p.8).
- `biblioteca/Horizontes En Conjuntos Causales.md` Entregables B/C/§6 (documento de apoyo,
  git-ignored).
- Orden causal 1+1D = orden producto 2D / LIS: Surya LRR §4 (estándar CST).
- **Escalas KPZ — ANCLADAS:** longitudinal 1/3 + límite Tracy–Widom + varianza 4/3 de la función de
  dos puntos vía Sasamoto–Spohn 2010 (`biblioteca/1002.1879v2.pdf`, eqs. 1.5–1.7 e Introducción p.2);
  **transversal 2/3** como teorema del modelo poissoniano de subsecuencias crecientes vía
  **Johansson 2000, *Transversal fluctuations for increasing subsequences on the plane*** (NO en
  biblioteca; primaria leída externamente). Pertenencia de la cadena más larga a la clase: LIS
  poissonizada (BDJ 1999 *Shape Fluctuations…*; Surya §4.3).
- **[UNVERIFIED] — la FORMA de la cola transversal.** La cúbica `exp(−c r³/ℓ²)` NO está probada por
  Johansson 2000: su estimación se reescribe como `~exp(−c r⁶/N⁴)` (sextica). La atribución cúbica
  no está sustentada. **No es crítica**: ambas colas cruzan en `r~ℓ^{2/3}` y dan el mismo `ℓ^{4/3}`;
  la convergencia de §8.4 sólo usa la escala 2/3 (anclada), no la forma.
- **[gap L₁b-(b)]** El paso "orden producto 1+1D ⇒ hipótesis exactas del modelo LPP de Johansson
  aplican al observable causal" debe formularse, no asumirse por analogía KPZ.
- Adjudicación: `docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md`
  (RECOMMEND_PROCEED_WITH_CAVEATS; caveats C1–C5).

```
