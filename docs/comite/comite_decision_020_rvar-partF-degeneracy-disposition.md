# Comité Decision 020 — rvar-partF-degeneracy-disposition

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

PI delegated the convocation this session (2026-07-05, "tú mandas hoy"), question framed by the
chair: the structure probe committed at `6347459` (`dev/PR003_RVAR_STRUCTURE_PROBE_REPORT.md`)
certifies 𝒜(C)=∅ in 12/12 MINK draws at the 4 production intensities (zero unrelated (min,max)
pairs — tall-box geometry), while in BH 100% of minimals have partial intervals (family nonempty
via horizon-interior structure). The frozen Part F (μ over MINK nulls, addendum `0271fd9`) would
therefore yield `rate_empty≈1` → `OUT_OF_DOMAIN_UNCALIBRATED` even with unlimited compute: the
frozen calibration object is vacuous on its own null substrate at production scale. Additionally,
a polynomial candidate (interval gap-DP, `dev/explore_rvar_interval_dp.py`) exists for the same
frozen object, toy-validated against the committed Gate 0 reference, pending its own fresh Gate 0.
Adjudicate: **(1)** the correct disposition of R-VAR Part F given the measured degeneracy —
spec-level redesign of the calibration object/𝒜(C), recording R-VAR as non-viable at production,
or another route (e.g. is the EMPTY-MINK vs nonempty-BH dichotomy itself a legitimate object? —
that would be an object change); **(2)** the status of the interval-DP candidate and what fresh
Gate 0 it would owe if continued; **(3)** whether the Part E "polynomial for every finite poset"
over-claim re-scope that comité 019 already demanded proceeds.

Mid-session PI steer (verbatim intent, folded into §8): *"Quizá el proyecto todavía vive si se
rebaja el objetivo inmediato a singularidad/truncación order-only. Si ni eso sale, entonces sí:
sería momento de cerrar o convertirlo en resultado negativo."*

## 2. Verified state

Facts checked **this session** (2026-07-05), each with its command / file:line.

- `make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
  = `docs/preregistration_002.md:8`. MATCH. Nothing in this session touches `nachocausal/` or the seal.
- `git log -4`: HEAD = `6347459` (structure probe, 5 files), `014d364` (feasibility blocker,
  3 files), `0271fd9` (μ-freeze addendum), `55e19b8` (Gate 0 Tier 1 PASS).
- Sealed suite: `.venv/bin/python -m pytest -q tests/` → `28 passed in 293.64s`.
- Determinism re-check: chair re-ran `dev/measure_pr003_rvar_structure_probe.py`; output JSON
  byte-identical to `git show HEAD:dev/rvar_structure_probe_result.json` (diff clean). This
  verifies determinism, **not** correctness (falsifier, §5) — the chair authored the probe.
- Probe facts (commit `6347459`): MINK 12/12 draws (4 intensities × dev seeds 20240617/13/101):
  `unrelated_min_max_pairs = 0` → 𝒜(C)=∅ certified per draw (one-way certificate, §4 logician).
  BH 12/12: 100% of minimals partial-interval, K = 116–436. Interval property: 0 violations
  24/24 (MINK under `u=t−r`; BH under ingoing `p=t+r`; outgoing `q=t−r*` FAILS in BH, 5000+).
- Feasibility probe (commit `014d364`): |Max| = 15/22/26/40 at MINK production; 2^40 ≈ 1.1×10¹²;
  `OVERALL_VERDICT=INFEASIBLE` for the only Gate-0-verified implementation (`family_A`,
  `dev/measure_pr003_rvar_gate0.py:67-79`).
- Interval-DP prototype (commit `6347459`): toy validation vs the committed Gate 0 reference ALL
  PASS (modularity on all family members; λ* exact; unique argmax exact; H≠∅). Production demo
  CLAIM-INERT: MINK EMPTY_FAMILY all levels; BH OK, ≤9 Dinkelbach iterations, ≤9s/draw at K=426;
  BH argmax |D*|≈N−few, B∈{3..8}.
- **Chair dossier error, caught by the wave-1 reproducibility engineer and re-verified by the
  chair:** the addendum sections "Part F M-consumption semantics" (MINK-only), the
  dual-consumption-diff-test-as-HARD-precondition, the spawn-form closure and the
  production-feasibility disclaimer are **NOT in committed `0271fd9`** —
  `git show HEAD:dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md | grep -c "M-consumption|dual-consumption|MINK-only"`
  = 0; working tree = 6 hits; `git diff` = +48 uncommitted lines. The chair's original dossier
  stated the opposite; corrected here for the record.
- **Warden finding (this session, `git ls-files` / `git status --short`): the entire cited
  adjudication chain is untracked** — `docs/comite/comite_decision_015..019` and
  `docs/auditor/auditor_report_003..006` are all `??` (never committed). As of HEAD, the
  precedent record this brief cites (018 §9.1, 019 §9, AUDIT_006) has no git-anchored existence.
- Addendum (committed portion, `0271fd9`): M=200 exact, admissible-only, per level (:59-79); §4c
  OOD rule (:202-220) — block exhausted → `OUT_OF_DOMAIN_UNCALIBRATED`, HALT, reconvene; §4d
  `rate_empty` CLAIM-INERT (:222-240); :49-55 Tier 1 measured 190/191 MINK EMPTY at
  TOY_INTENSITY=9.0 and the addendum explicitly declines to use that rate as justification.
- Spec Part E over-claim: `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:489-501` ("se computa en tiempo
  polinomial para todo poset finito"); no-budget-cap clause :499-501. Tier-0-insufficient-alone
  rule: :429-431.
- Comité 019 (untracked, see warden): RECOMMEND_DO_NOT_PROCEED on Part F step 3; its claim that
  certifying 𝒜(C)=∅ requires the 2^|Max| enumeration is superseded by the probe's
  O(|Min|·|Max|) certificate (mathematician re-derived it independently this session).
- Seed discipline: all probes on dev seeds 20240617/13/101 (`dev/sweep_o.py:33` precedent);
  `EXPLORE_POOL` (1_000_000–1_000_039) and `VALIDATION_SEEDS` untouched.
- Geometry: `nachocausal/thresholds.py:36-40` — T_EDGE=6.0, R_EDGE=1.2, r_S=0.5;
  INTENSITIES :46.

## 3. Dossier

Files and references the chair supplied to the committee:

- `dev/PR003_RVAR_STRUCTURE_PROBE_REPORT.md`, `dev/measure_pr003_rvar_structure_probe.py`,
  `dev/rvar_structure_probe_result.json` (commit `6347459`)
- `dev/explore_rvar_interval_dp.py`, `dev/rvar_interval_dp_result.json` (commit `6347459`)
- `dev/PR003_RVAR_PARTF_FEASIBILITY_PROBE_REPORT.md`, `dev/rvar_partF_feasibility_probe_result.json`
  (commit `014d364`)
- `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` (committed `0271fd9` + uncommitted +48-line working-tree
  edit), `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md` (Parts D.1–D.4, E, F/F2)
- `dev/measure_pr003_rvar_gate0.py`, `dev/measure_pr003_rvar_gate0_tier1.py`,
  `dev/gate0_tier0_result.json`, `dev/gate0_tier1_result.json`
- `docs/comite/comite_decision_015..019` (untracked), `docs/auditor/auditor_report_003..006`
  (untracked)
- `nachocausal/thresholds.py`, `nachocausal/generator.py`
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`
  (EGS arXiv:2605.06813), `biblioteca/derived-md/Bombelli_1987_PhD.md`,
  `biblioteca/Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.pdf`

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

- **Proposed artefact(s):** No scoring/committing run is authorized by this decision. The only executable that may proceed *if* the committee continues the interval-DP candidate is its **own fresh Gate 0**, mirroring the existing naming: `dev/measure_pr003_rvar_interval_dp_gate0.py` → `dev/rvar_interval_dp_gate0_result.json` (Tier 0, exhaustive N≤16) and a Tier 1 100-poset variant, exactly paralleling `dev/measure_pr003_rvar_gate0.py`/`_tier1.py` → `dev/gate0_tier0_result.json`/`gate0_tier1_result.json`. Acceptance = **zero discrepancy vs the brute-force `family_A`+`brute_force_argmax`** reference (`dev/measure_pr003_rvar_gate0.py:67-88`) across all enumerated posets — same bar comité 019 §9(a) set. The current `dev/explore_rvar_interval_dp.py` Part-1 match is only against that reference **on one toy poset**; it is NOT a Gate 0. Separately, the dual-consumption-plan diff test the addendum names as a HARD precondition needs a concrete script/target before any Part F μ run — and see the provenance risk below.
- **Environment & seal:** Runs under the sealed dev env `.venv/bin/python` (the same interpreter that gives `28 passed` and the byte-identical structure-probe re-run). Validation path is pinned `numpy==1.26.4` (`Makefile:2-3`); the DP imports `family_A` etc. from `gate0`, so it must run against that same pin — a **package-diff-clean check** (`pip freeze` vs pinned numpy) is required so the DP's `Fraction`/boolean-matmul path is bit-reproducible. It does **not** need the external Minz clone (`make gate` / `~/cs-horizon-reuse-check/venv_minz`, `CLAUDE.md:27-29`); Minz is not on this path. Re-run `make verify-seal` before/after — must stay `6e2c38881234…bfefd4` = `docs/preregistration_002.md:8` (MATCH this session); nothing here touches `nachocausal/thresholds.py`, so the seal must not move.
- **Provenance capture:** every artefact JSON must record: commit SHA (currently `6347459`), `pip freeze` (numpy version explicit), `uname -a`, the dev seed band **20240617/13/101 only** (`dev/sweep_o.py:33` precedent — EXPLORE_POOL 1e6 and VALIDATION_SEEDS 2_000_000–2_999_999 stay untouched, `dev/explore_seeds.py`), UTC timestamps, and a determinism re-check (re-run → JSON byte-identical to committed, `diff` clean) exactly as the chair verified the structure probe this session.
- **Run mechanics:** the fresh Gate 0 is a **reversible pre-flight** — dev/, claim-inert, output is a PASS/FAIL of the *algorithm vs brute force*, no μ table, no scoring, no seal touch → safe foreground, single invocation, discardable. The **committing step remains Part F step 3 (the μ computation)** and stays gated (addendum §6 "cada tier necesita autorización separada"; comité 019 RECOMMEND_DO_NOT_PROCEED). Clean-abort guards already exist in the design: the interval certificate raises on violation → typed abstention (`explore_rvar_interval_dp.py` docstring pt 3), and the OOD rule HALTs without block extension or M reduction (addendum §4c). None of these may be coerced to PASS/FAIL.
- **Reproducibility risks / ambiguities:**
  - **PROVENANCE DISCREPANCY — the Part F guardrail is uncommitted.** The canonical "M-consumption = MINK-only", the dual-consumption-plan **HARD precondition**, the spawn-form closure, and the Part-F-specific blocking conditions exist **only in the working tree**, NOT in committed `0271fd9`: `git show HEAD:dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md | grep` for "M-consumption semantics"/"dual-consumption-plan"/"MINK-only"/"Blocking conditions" returns **nothing**, and `git diff` shows them all as `+` additions. The DOSSIER's note that "the committed addendum at 0271fd9 ALREADY contains these sections" is **contradicted by git** — the chair grepped the working file. These preconditions must be committed before they can bind any Part F execution; as-is they could be lost or silently edited (working tree also has `M INSTRUCCIONES.md`).
  - The interval property is **empirical** (0 violations in 24/24 draws, `dev/rvar_structure_probe_result.json`), not proven; the outgoing-sort q=t−r\* FAILS in BH (5000+ violations). The DP's correctness on production draws therefore rests on a *run-time raise*, not a static guarantee — a fresh Gate 0 at N≤16 cannot exercise the K∈{40,426} production regime where the certificate is load-bearing. [partially UNVERIFIED at production scale by construction]
  - **rate_empty degeneracy is orthogonal to feasibility.** Even a Gate-0-passing DP that computes μ hits `rate_empty≈1` on MINK → `OUT_OF_DOMAIN_UNCALIBRATED` (addendum §4c; 190/191 empty at Tier 1, addendum:49-55; 12/12 𝒜(C)=∅ certified, `dev/rvar_structure_probe_result.json`). The DP fixes *complexity*, not the empty-object problem — do not let "polynomial candidate passes Gate 0" be read as "Part F is viable." rate_empty stays CLAIM-INERT (addendum §4d).
  - The structure probe adds an emptiness **certificate** decidable in O(|Min|·|Max|) (DOSSIER; certificate reasoning in `dev/rvar_structure_probe_result.json`) — this means the old "OOD token unreachable at scale" finding (comité 019) no longer holds for *detecting* ∅; but detecting ∅ cheaply does not make the frozen calibration object non-vacuous. Any re-scope of the Part E "polinomial para todo poset finito" over-claim (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:489-501`) is a **spec-text edit under freeze discipline**, not an executable step — it needs the warden's sign-off, no run.

### Mathematician brief

- **Computability.** The whole R-VAR step is decidable on the order relation alone — no coordinates enter the selector, only the strict partial order `C` (via covers/`d+`, `Min`, `Max`). I re-derived the two load-bearing algebraic claims in `dev/explore_rvar_interval_dp.py` and both are CORRECT. (i) *Modularity*: for a down-set, along a cover `x⋖y` one has `z_x·z_y = z_y`, so `[x∈D][y∉D] = z_x − z_y`; expanding `A(D)=Σ_{cover}(z_x−z_y)(d⁺_x−d⁺_y)` and collecting per vertex gives exactly `a_v = d⁺_v·outdeg(v) − Σ_{v⋖y}d⁺_y − Σ_{x⋖v}d⁺_x + d⁺_v·indeg(v)` and `b_v = outdeg(v)−indeg(v)`, matching `explore_rvar_interval_dp.py:112-114` and the `c_z` linearization in `measure_pr003_rvar_gate0.py:159-163`. (ii) *Reparametrization*: the family is *defined* as `D=down(M), M⊆Max` (`measure_pr003_rvar_gate0.py:67-82`), so `v∈D ⇔ I_v∩M≠∅` — a strict subclass of down-sets (those generated by *global* maximals), and the DP optimises the SAME object, not all down-sets. The **𝒜(C)=∅ certificate is order-theoretically sound and cheap**: 𝒜 requires `(C−D)∩Min≠∅`; if every minimal lies below every maximal then every nonempty `M⊆Max` pulls all of `Min` into `down(M)`, so 𝒜=∅. This is decidable in `O(|Min|·|Max|)` (the `unrelated_min_max_pairs=0` test), correcting comité 019's assertion that emptiness needs the full `2^|Max|` enumeration. The domain/abstaining logic is the addendum's OOD rule (`PR003_RVAR_MU_FREEZE_ADDENDUM.md:202-220`) and the estimator-v2 `τ(n)` gate on `n=|Min|` (`nachocausal/thresholds.py:134-141`); both are order-only.
- **Order observable.** The step relies on the R-VAR selector `S(D)=A(D)/B(D)` maximised over 𝒜(C): `A` = signed `d⁺`-imbalance summed over the crossing cover-interface `H[C;D]`, `B=|H|`. It is a purely order-intrinsic functional of the relational horizon (the cover edges that cross a candidate down-set boundary), intended to peak where the discrete future-degree `d⁺` drops sharply — the order-only signature EGS attributes to the event horizon via crossing timelike-curve structure (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:22,94`). The project's primary sealed observable is distinct — future-VOLUME `O_min(i)=|future(i)|`, a column-sum of `C` (`docs/estimator_v2_freeze.md:34-37`) — and R-VAR is an auxiliary boundary selector layered on that same order.
- **Relevant invariants.** The DP's `d⁺` (cover-outdegree) is the same local quantity underlying Benincasa–Dowker interval-abundance / discrete d'Alembertian `C_k` (Benincasa–Dowker 2010, `biblioteca/`); the selector's `A` is a first-difference of it across the interface. The interval property is a statement about **order dimension ≤ 2** (a realizer of two linear extensions): 1+1D Minkowski causal order is provably 2-dimensional with the light-cone/null coordinates as an exact realizer (Myrheim 1978; Bombelli 1987 PhD, `biblioteca/derived-md/Bombelli_1987_PhD.md`; Surya LRR 2019 §4). Ordering fraction / Myrheim–Meyer dimension and longest-chain height are the standard 2D-order invariants that certify manifoldlikeness here.
- **Analytic / continuum target.** The step should approach the EGS 1+1D Schwarzschild toy horizon at `r/r_S=1` (`...geodesic focusing....md:166-185`), where ingoing/outgoing null geodesics in `(t*,r)` organise the causal order; the discrete crossing-interface is meant to localise that null boundary within the finite tall patch (`thresholds.py:37-42`, aspect ratio `T_EDGE/R_EDGE=5`). This is a **localisation** target only — `NO_RECONSTRUCTION_CLAIM`; no metric, no asymptotic event horizon, no 3+1D.
- **Caveats.**
  - The **interval property is a theorem only for genuinely order-dimension-2 orders sorted by a realizer coordinate.** MINK qualifies by construction; for BH it is empirically certified (0 violations, 24/24 draws under ingoing `p=t+r`) but **not proven** order-dim-2 from the generator, whose BH relation is a 3-region `np.where` (`nachocausal/generator.py:119-127`), not a manifest product order. `[Partially UNVERIFIED — theorem hypotheses for the BH order]`
  - The **ingoing/outgoing asymmetry is explained, not anomalous**: `p=t+r` is the horizon-*penetrating* (regular) advanced coordinate — condition `dt ≥ r_j−r_i` (`generator.py:118`) — whereas the outgoing sort uses `r*=r+2r_S log|r−r_S|/r_S` (`generator.py:104`) which **diverges at `r=r_S`**, so `q=t−r*` is not a global realizer coordinate across the horizon; its failure (5000+ violations at I=12000) is the expected signature of that divergence, and confirms the ingoing sort is load-bearing.
  - The per-draw `O(N·K)` certificate that **raises on interval-failure** (`explore_rvar_interval_dp.py:104-105`) is the correct falsifiable safeguard; a production version MUST convert the raise into a typed abstention, never a silent wrong answer.
  - **MINK-emptiness is an empirical regularity, not a theorem.** Nothing forbids an interior minimal (empty past at moderate `t`) unrelated to some maximal; but such minimals have probability `~exp(−ρ·vol)` and vanish as density grows, so emptiness becomes MORE certain with `N`. This **inverts comité 019's physicist prediction** (§4) — measured 100% at all 4 levels — and means the frozen Part-F calibration object (μ over MINK nulls) is genuinely vacuous on its own substrate at production scale, independent of compute. That is a real degeneracy of the *frozen object*, not a bug to be tuned away (`NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`).
  - **A fresh Gate 0 for the interval-DP must be falsifiable, not a re-run of the toy.** Minimum contents: (1) zero-discrepancy of `(λ*, argmax down-set, T/E/U partition)` vs the enumerate-and-filter `family_A` on *sprinkled* posets at the largest `K` still enumerable (`|Max|≲20`, dev seeds only), not just `PI`; (2) agreement at *every* Dinkelbach step including the `(A,B)=(0,0)` boundary-tie and the `EMPTY_FAMILY` branch; (3) an explicit test that the interval-certificate-fail path abstains rather than returns; (4) exercise **both** sort keys so the outgoing-sort failure is caught, not hidden; (5) the C.1 anti-circularity witness (`measure_pr003_rvar_gate0.py:103-127`) re-passed. Toy-only validation (`explore_rvar_interval_dp.py` Part 1) is necessary but **not sufficient**; its production Part 2 is correctly marked CLAIM-INERT.
  - The Part-E spec over-claim "*se computa en tiempo polinomial para todo poset finito*" (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:489-501`) remains **mathematically false as written and must be re-scoped**: `maxflow_mincut_closure` is polynomial over *all* down-sets, but the 𝒜(C)-restricted selector that passed Gate 0 was the `2^|Max|` enumerate-and-filter. The interval-DP would make the *restricted* object polynomial **only under the interval hypothesis** (order-dim-2 + valid realizer sort), i.e. for this project's sprinklings — NOT "todo poset finito." The corrected claim is: polynomial for finite orders that certify the interval property, with a typed abstention otherwise. `NO_GROUND_TRUTH_LEAKAGE` holds throughout — the sort key is an observable-side null/embedding coordinate feeding the *algorithm*, and must be shown not to leak the hidden BH/MINK label into the selector before any scoring use. `[UNVERIFIED — leakage check of the sort-key provenance not in DOSSIER]`

### Mathematical logic brief

- **Formal status:**
  - *Lean-proved theorems* exist only for the **horizon/ideal side** (`formal/HorizonFormal/HorizonFormal/*.lean`: Accessibility, Ideals, Horizon, ChainEnds, …), no `sorry`/`axiom` in the project files (the `sorry` grep hits are all mathlib test files). **None of the R-VAR selector claims are Lean-formalized**: no file mentions the family 𝒜(C), modularity, the interval property, the gap-DP, or Dinkelbach. So the entire explore-script chain is *outside* the formal artefact — it is script-level mathematics, not machine-checked.
  - Modularity identity A(D)=Σaᵥ, B(D)=Σbᵥ: an **algebraic lemma** (cover-edge telescoping), asserted in the docstring (`dev/explore_rvar_interval_dp.py:12-20`) and **verified by exhaustion on all members of one toy family** (`:229-231`). Proved-on-toy + analytic sketch; not independently proved for general C.
  - Interval property (Iᵥ contiguous in the null-sorted antichain): **not a theorem — an empirical regularity** ("0 violations in 24/24 dev draws"), and explicitly *sort-dependent* (outgoing q-sort FAILS in BH, 5000+ violations). It is a **runtime per-draw certificate** (`:97-105`), raise-on-failure. Its universal truth for 1+1D sprinklings is a **conjecture**.
  - Gap-DP correctness and the tie-break: **conditional theorem** — "IF the interval certificate passes THEN the DP returns the exact 𝒜(C)-argmax" — plus exact toy match against the committed Gate-0 reference (`:234-248`). Not proved for the general (non-interval) case.
  - Certificate "every min below every max ⟹ 𝒜(C)=∅": a **valid sufficient condition** (a small theorem, O(|Min|·|Max|)); correctly supersedes comité 019's belief that 2^|Max| enumeration was needed.
- **Quantifier / dependency order:**
  - Reparametrization holds because Max(C) is an antichain and, for M⊆Max, ↓M∩Max = M exactly (maximal x≤m ⟹ x=m). This bijection is ∀-quantified over M and is unconditional; the *degeneracy* filters (M≠∅; some minimal uncovered; B≥1) are what restrict to 𝒜(C).
  - The 𝒜(C)=∅ ⟹ OOD conclusion decomposes as: (i) **feasibility** (2^40 enumeration) — removed by infinite compute *or* by the DP; (ii) **degeneracy** (𝒜=∅) — invariant under compute. The dossier's "OOD even with infinite compute" correctly isolates (ii) from (i); that logical separation is **sound**. But its transfer from the 12 dev draws to the *frozen M=200 MINK calibration pool* is an **inductive/statistical step (∀-over-a-different-seed-pool), not a theorem** — see Caveats.
  - **Freeze hazard (Q1):** if the measured MINK-EMPTY vs BH-nonempty *dichotomy* is promoted to the observable, the 12 already-seen dev draws **cannot** serve as its justification without violating NO_POST_HOC_TUNING / rate_empty CLAIM-INERT (addendum §4d). Any such new object must be defined and frozen ∀-before-∃ over fresh validation seeds. This is a genuine change of object, not a threshold move.
- **Equivalence claims:**
  - 𝒜(C) = {↓M : M⊆Max} ∖ degenerates: **genuine EQUALITY** given D.1's definition `D = ↓(D∩Max)` (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:273`) and the antichain bijection above — *provided* "degenerates" faithfully encodes all three remaining D.1 predicates (∅≠D≠C, (C∖D)∩Min≠∅, H≠∅). The encoding is asserted and toy-verified, not proved in general.
  - "H≠∅ ⟺ B≥1": **identity for down-sets** (no complement→D cover edge can cross a down-set, so ΣbᵥD = |edges D→Cᶜ| = |H|). Sound.
  - "every min below every max ⟹ 𝒜=∅": **one-way (sufficient), NOT iff** — 𝒜 can be empty for other reasons (no member with H≠∅). The probe's `unrelated_min_max_pairs=0` is exactly the antecedent, so for the 12 draws the conclusion is **deductively certified**; it is not a characterization of emptiness in general.
  - Tie-break "any D with H=∅ has objective exactly 0 at every λ": rests on H=∅ ⟹ (A,B)=(0,0) (a down-set with no crossing cover has no crossing relation, hence a union of components, so both counts vanish); matches spec's G(D):=A·B*−B·A* with max_{𝒜}G=0 (`:380`). Plausible lemma, **toy-verified at the documented (0,0) boundary**, not generally proved.
- **Type / object discipline:**
  - The Lean core uses `Order.Ideal` = nonempty **+ directed** + lower-set; `Ideals.lean:16` itself flags this is "stronger than a bare down-set." 𝒜(C) members ↓M with |M|>1 are generally **non-directed** down-sets, so **the Lean Ideal API does not model R-VAR family members** — the formal artefact and the selector are different objects; do not cite Lean as backing for the DP chain.
  - Clean throughout otherwise: 𝒜(C) elements are down-sets (order ideals of the poset, not quotient classes); the "horizon" B=|H| is an order-theoretic cover count; "BH horizon structure" is a *physical interpretation* of the combinatorial fact 𝒜≠∅, kept separate from scoring (no NO_GROUND_TRUTH_LEAKAGE issue at the definitional level).
- **Caveats:**
  - The step from 𝒜=∅ on **12 dev draws** (seeds 20240617/13/101, `dev/rvar_structure_probe_result.json`) to rate_empty≈1 on the **frozen M=200 MINK calibration pool** is an **inductive generalization, not a theorem**. To make "OOD even with infinite compute" *deductive*, one would need a proved box-geometry lemma (R_EDGE=1.2 ≪ T_EDGE=6, `nachocausal/thresholds.py:36-40` [chair-pasted]) that *every* MINK causal-diamond draw at production intensity has every minimal below every maximal. Absent that, mark the production degeneracy conclusion as **strongly-supported empirical prediction, [UNVERIFIED as theorem]**.
  - Interval-DP (Q2): correctness is **conditional on the runtime interval certificate**; a fresh Gate 0 must exercise (i) DP=brute-force on *multiple fresh* toy posets with 𝒜≠∅ (the committed toy is a single point), (ii) the abstention path when the certificate FAILS (guard against silent wrong answers — the outgoing-sort BH case proves the property is not universal), and (iii) confirmation that a correct DP still returns EMPTY_FAMILY on MINK — i.e. **the DP fixes feasibility, not degeneracy; it does not rescue Part F.** Authorization is per-tier (addendum §6).
  - Part E over-claim (Q3): "polinomial para todo poset finito" (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:489-501`) is **true only for the unrestricted `maxflow_mincut_closure`** (Picard/min-cut) and **false-or-unproven for max over 𝒜(C) on all finite posets** — the DP establishes it *only* under the interval property, which demonstrably fails for general finite orders. Re-scope is warranted on **logical** grounds (a false universal), independent of the Part F disposition.
  - I read the explore script, spec D.1/D.2, and the Lean Ideal file directly; addendum line numbers (§4c :202-220, §4d :222-240, Tier-1 190/191 :49-55) are taken from the chair's DOSSIER, not opened by me this session.

### Physicist brief

- **Coordinates & patch.** The step must use the generator's **ingoing Eddington–Finkelstein** convention — tortoise `r* = r + 2r_S·log(|r−r_S|/r_S)`, ingoing rays `v = t+r = const`, horizon-crossing branches b1/b2/b3 (`nachocausal/generator.py:102-127`). This matches EGS's `(t*,r)` construction, in which `det g` is constant so a coordinate-uniform Poisson sprinkle is the natural-volume process (EGS PDF p.7, §II.A; `generator.py:10-12`). The patch is the frozen tall box `t∈[0,6]`, `r∈[0.1,1.3]`, `r_S=0.5` → horizon at fractional radial position `(0.5−0.1)/1.2 ≈ 0.33` from the inner edge (`nachocausal/thresholds.py:36-43`). **Forfeited by finiteness:** a true event horizon is the boundary of the past of `J⁺` and requires an *infinite* sprinkling; in a finite patch one cannot separate futureless points at `J⁺` from futureless points near the singularity (EGS PDF p.10, §III). So no asymptotic/event-horizon claim is available — only localisation of a horizon-*like* structure in the patch.
- **Physical meaning of the signal.** The BH-nonemptiness leg is genuine and is *exactly* EGS's singularity-truncation mechanism: minimal/interior elements inside `r_S` have futures cut off because every interior timelike curve reaches `r→0` in finite proper time, whereas exterior futures are limited only by the box (EGS PDF p.10-11, §III; probe report `dev/PR003_RVAR_STRUCTURE_PROBE_REPORT.md:72-75`). This is what makes maximal elements sit *inside* the box rather than only on the top slice, giving BH `K=116–436` vs MINK `K=13–44` (`dev/rvar_structure_probe_result.json`) and 100% partial-interval minimals. The observable therefore tracks the singularity-truncated interior, and the effect is bimodal in EGS's own diagnostic. **But** the R-VAR `𝒜(C)` object reads this only through a *binary* EMPTY/non-empty flag, not a graded score with a null distribution.
- **Sprinkling domain.** Poisson sprinkle, same cloud for BH/MINK differing only in causality (`generator.py:37-50`; `thresholds.py:51-54`), four intensities 1500/3000/6000/12000 (`thresholds.py:46`). **Why comité-019's prediction inverted:** that prediction implicitly used EGS's future-*cardinality* bimodality, which stays non-degenerate in Minkowski (varies between `n` and `√n`, EGS PDF p.11-12). The R-VAR emptiness is a *different* quantity and is forced by the **box aspect ratio**, not by `N`: light crosses the spatial width in `Δt = R_EDGE = 1.2 ≪ T_EDGE = 6`, so every bottom element's future cone covers the entire top slice → every minimal lies below every maximal → `𝒜(C)=∅` (certified `unrelated_min_max_pairs = 0`, 12/12; report :70-75). This is geometric and **saturates as `N→∞`** (larger `N` only sharpens the min→max completeness); the toy near-single-chain artifact and the production tall-box completeness are two different routes to the same empty family. The physicist prediction failed because it assumed emptiness was a small-`N` artifact that mixing would cure; in this box, mixing makes MINK *more* complete, not less. **Forfeited guarantee:** the μ substrate is MINK-only nulls (addendum §F2), which are deterministically empty at production scale → `rate_empty≈1` → the frozen OOD rule fires (OUT_OF_DOMAIN_UNCALIBRATED). The freeze worked; the object is vacuous on its own substrate.
- **Claim boundary.** Any verdict here claims at most **order-only localisation of a singularity-truncated interior in a finite 1+1D Schwarzschild patch** — NOT metric reconstruction (`NO_RECONSTRUCTION_CLAIM`), NOT an event-horizon claim (needs infinite sprinkling, EGS p.10), NOT 3+1D. Critically, EGS state their longest-chain/truncation partition **"would no longer work for regular black holes,"** where interior curves continue for arbitrary proper time (EGS PDF p.12, §III [page corrected per §7]; p.9-10 Hayward). So a signal built on future-truncation detects the **Schwarzschild singularity's truncation**, not a horizon generically — it must never be sold as a regular-horizon or horizon-generic diagnostic.
- **On the argmax shape (question c):** `|D*|≈N−few`, `B∈{3..8}` **independent of N** (N spans 1500→12000, K spans 116→436, yet B stays 3–8) is **not consistent with a horizon cut.** A genuine cut separating interior (`r<r_S`) from exterior minimals would split the minimal antichain near the horizon (~1/3 of the `n_min≈64–73` minimals interior at λ=12000), giving a crossing interface `B` that **grows with N** (order `n_min` ~ tens, ~`√N`), not `O(1)`. A constant `B≈3–8` excising `few` elements is a **corner/boundary artifact** — the DP is lopping off the handful of deepest singularity-truncated maximal elements at the inner-top corner, whose cover-interface is fixed regardless of N. So the current argmax does **not** localise `r=r_S`.
- **On the EF sort (question d):** ingoing `p=t+r` giving 0 interval-violations while outgoing `q=t−r*` fails inside the horizon (5000+ violations; `dev/rvar_structure_probe_result.json`) **is exactly the expected EF causal structure** and is a positive consistency check: ingoing rays `v=const` are regular across `r_S`, outgoing rays "tilt over"/flip inside the horizon (EGS PDF p.8 Fig.1 "tilting over at the horizon"; p.25 Fig.12 outgoing ladders reverse direction across `r_S`). The generator's `t_in = r_j−r_i` branch encodes `v=t+r` monotonicity; the interval property inheriting the ingoing sort is correct, not a coincidence.
- **Disposition (physics read):**
  - *Option (1b) record R-VAR non-viable at production* is the physically honest reading: the frozen calibration object is vacuous on its own MINK null by box geometry; no algorithm fixes that (report :98-101). `[supported]`
  - *Option (1a) spec-level redesign* is sound **only** if the new object has a non-degenerate MINK null — e.g. EGS's longest-chain / future-cardinality bimodality, which is graded in Minkowski (EGS p.11-12). That is a **new object → new pre-registration + fresh Gate 0**, not a tweak.
  - *Treating EMPTY(MINK)-vs-nonempty(BH) as the signal* is a **change of object** that I do **not** endorse as currently measured: it conflates a genuine BH singularity-truncation signal with a MINK **box artifact**, its argmax is a corner artifact (question c), and it collides with the EGS regular-BH caveat — so it cannot be claimed as a horizon detector without (i) demonstrated `r_S` localisation, (ii) robustness to box aspect ratio, and (iii) explicit re-scoping to "Schwarzschild-singularity-truncation," all under a fresh prereg. `NO_POST_HOC_TUNING`, `NO_GROUND_TRUTH_LEAKAGE` (the EMPTY/non-empty split must not be read off the embedding).
  - **Interval-DP candidate (question 2):** physically it changes nothing — it computes the *same* frozen degenerate object faster, so it inherits MINK-emptiness and does not rescue Part F. Status: legitimate algorithmic optimisation, **not** a physics fix; if continued, its fresh Gate 0 is a *correctness* gate (zero discrepancy vs enumerate-and-filter on sprinkled posets to K≈20, per report :48-52), never a substitute for the spec-level degeneracy decision.
  - **Part E re-scope (question 3): warranted.** Finding 1's polynomial argument rests on the **interval property**, a 1+1D geometric fact (`I_v` contiguous under a null sort — theorem for the MINK dominance order, *empirical* for BH, report :32-38), not a universal poset property. The over-claim "polynomial for every finite poset" must be re-scoped to "2D-order / sprinkled posets carrying the certified, per-draw-checkable interval property," matching the report's own hedge ("for the posets this project actually generates," report :22-23). `[supported]`
- **Caveats.**
  - MINK emptiness is a **box-aspect-ratio artifact** (`R_EDGE=1.2 ≪ T_EDGE=6`), certified `unrelated_min_max_pairs=0` 12/12 (`dev/rvar_structure_probe_result.json`; report :70-75) — not a small-N effect; it worsens with N.
  - BH-nonemptiness is real singularity-truncation (EGS PDF p.10-11) but is delivered to R-VAR only as a binary flag with a deterministically-empty null, so a μ-quantile calibration is ill-posed by construction (addendum §F2).
  - The interval property for BH is **empirical (0 violations, 24/24)**, not proven; a production use must keep the per-draw certificate as a guardrail that can fail (report :38). `[empirical]`
  - Any horizon-truncation signal is **Schwarzschild-singularity-specific** and fails EGS's regular-BH caveat (EGS PDF p.12 [corrected]); it must not be generalised. `[anchored EGS §III]`
  - `[UNVERIFIED]` The `|D*|≈N−few`, `B∈{3..8}` values are claim-inert dev-seed outputs (DOSSIER; report :88-90); my "corner-artifact" reading is a physical inference from their `N`-independence, not a validated measurement.

## 5. Falsifier attack

- Concrete failure modes:
  1. **"SAME frozen object" is false as implemented — the DP's answer depends on an extra input the frozen spec does not define.** `solve(C, max_sort_key)` (`dev/explore_rvar_interval_dp.py:87,94`) takes a sort key as input; the frozen selector (D.1, `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md`) is defined by `≤` alone. The interval certificate is *relative to a chosen ordering of Max*; the probe itself shows different keys give different verdicts on the same draw (q=t−r* FAILS in BH while p=t+r passes — dossier + `dev/measure_pr003_rvar_structure_probe.py:75-80`). No order-only key derivation (e.g. consecutive-ones/PQ-tree recognition, or a 2D-realizer extraction) is implemented or frozen. Until it is, "polynomial candidate for the SAME frozen object" over-claims: it is a polynomial candidate for a *key-augmented* object.
  2. **The toy "validation" is one poset with a trivial key.** Line 219: the toy sort key is the raw element index. The toy run therefore never exercises: a nontrivial realizer sort, the certificate-failure path (which currently `raise`s, `:105`, not typed abstention), the `EMPTY_FAMILY` branch against brute force, the `NO_CONVERGENCE` return (`:191` — a third, un-taxonomized status), or the (0,0)-tie at scale. Wave-1's own framing ("toy match is NOT a Gate 0") is right but understated: the toy match is close to vacuous for the parts that will be load-bearing.
  3. **Float soundness gap invisible to any N≤16/N≤20 Gate 0.** The "exact Fractions" pipeline casts `q*a − p*b` to float64 and cumsums it (`:185,117-121`); Dinkelbach terminates on `abs(val) < 1e-6` (`:188`). `a_v ~ d⁺²` grows like N², and q grows along Dinkelbach iterations; at production N sums approach the 2⁵³ float64 integer boundary with accumulated cumsum error. A wrong-but-plausible argmax raises no assertion. Fresh Gate 0 at enumerable K certifies correctness only where floats are exact; the regime where the DP is actually needed is exactly the regime the Gate 0 cannot reach (reproducibility engineer's risk (ii), sharpened: it is not just "cannot exercise K=426", it is "the numeric failure mode only exists there").
  4. **"BH family non-empty in 12/12" is not certified — it rests on claim-inert output.** The probe's ∅-certificate is one-way (its own header says partial intervals make 𝒜(C) "*potentially* nonempty", `measure_pr003_rvar_structure_probe.py:25-26`); non-emptiness additionally needs H≠∅ (`family_A`, `measure_pr003_rvar_gate0.py:68,77-79`). The only evidence H≠∅ holds in production BH is the DP production demo, which the script itself stamps CLAIM-INERT (`explore_rvar_interval_dp.py:5,288`). The decision question's premise "familia no vacía en BH" silently launders claim-inert output into a certified fact.
  5. **"OOD even with infinite compute" is a prediction, not a result.** It transfers 12 dev draws (+ the §4d-claim-inert Tier-1 rate 190/191, addendum `:49-55,222-240` which the addendum itself *declines to use*) to the untouched frozen M=200 pool. The logician flagged this; I add: adjudicating "register as non-viable" must be recorded as *Part F never executed (resource/degeneracy decision)*, never as *Part F produced OOD* — the frozen §4c outcome (block-exhausted→OOD+HALT) can only be produced by running.
  6. **The Part E over-claim has a second layer the mathematician's "corrected claim" does not fully fix.** Spec `:490-501` claims min-cut computes R-VAR polynomially "para todo poset finito", yet the feasibility blocker (014d364) concedes the only Gate-0-verified impl is 2^|Max| `family_A` — the spec asserts a general polynomial path that its own verification record contradicts (the min-cut solves the *unconstrained* closure subproblem; the constraints ∅≠D≠C, (C−D)∩Min≠∅, H≠∅ were handled only by enumeration). The proposed re-scope "polynomial for orders certifying the interval property" still needs the caveat of point 1: polynomial *given a valid Max-ordering, whose order-only construction is unimplemented*.
  7. **Dichotomy-as-object: kill it harder than wave 1 did.** Beyond the physicist's corner-artifact and the logician's ∀-before-∃ objections: MINK-emptiness is mechanically forced by the frozen box aspect ratio (light crosses R_EDGE=1.2 in Δt≪T_EDGE=6, `nachocausal/thresholds.py:37-38`), so the "observable" would be a detector of frozen box constants — geometry knowledge, not order structure — and it was noticed *because* 12/12 vs 12/12 separated on already-seen dev draws. Textbook post-hoc observable.

- Ground-truth leakage: **Direct and double.** (i) The DP production demo builds its sort key from the embedding: `t, r = emb[:,0], emb[:,1]` (`explore_rvar_interval_dp.py:260`); (ii) it *switches the key on the hidden label*: `key = (t−r) if kind=="MINK" else (t+r)` (`:262`). On hidden-embedding validation data the selector cannot know `kind`; picking the key by label is picking by ground truth. The structure probe likewise scans four embedding-derived candidate sorts and reports the per-draw `best_sort` (`measure_pr003_rvar_structure_probe.py:75-85,105`) — a min-over-coordinates certificate is itself embedding-guided. Since certificate-fail ⇒ abstention, the *abstain/OK boundary* is currently defined by embedding coordinates, not just scored by them. This is the single most disqualifying fact for the DP in its current form; the mathematician's [UNVERIFIED] flag is hereby VERIFIED at the cited lines.

- Freeze violations: (1) The addendum's MINK-only M-semantics, dual-consumption diff-test, spawn closure and feasibility disclaimer are **working-tree only** (`git diff` = +48 lines to `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md`; verified in this session). Any adjudication citing them as binding cites a phantom freeze; conversely, committing them now is post-outcome text (they were drafted knowing MINK is degenerate) — acceptable only because they are strictly tightening, and that tightening-only character must be stated in the commit. (2) A fresh DP Gate 0 designed *after* seeing the DP's production behavior risks acceptance criteria tailored to known outputs; the Gate 0 script and pass criteria must be committed before it runs, on dev-band seeds only (20240617/13/101), EXPLORE_POOL/VALIDATION_SEEDS untouched. (3) The physicist's argmax-shape argument (|D*|≈N−few, B∈{3..8}) reasons from CLAIM-INERT demo values; fine as red-team intuition, but it must not enter the decision record as evidence — §4d discipline applies symmetrically.

- Verdict coercion: three uncollapsed statuses exist in the DP (`OK`, `EMPTY_FAMILY`, `NO_CONVERGENCE`) plus a hard `raise` on certificate failure (`:105,191`). Only OK/EMPTY are surfaced in the demo table; NO_CONVERGENCE and certificate-fail have no typed abstention and would crash or vanish. Also: framing MINK-EMPTY as "the signal" (dichotomy option) is precisely an OOD→PASS coercion — a degenerate/uncalibratable branch re-read as a detection. Reject.

- Premature / over-broad claims: spec `:490-497` "se computa en tiempo polinomial para todo poset finito" — false as written, re-scope required; DP docstring "candidate resolution of comité 019's blocker" (`:9-10`) — resolves it only for interval-certified posets *with a supplied key*; any reading of the BH argmax as horizon localisation (it is |D*|≈N−few with constant B — not an r_S cut, per physicist); "interval property holds in the posets this project generates" (`:25-27`) — 24/24 empirical, MINK-side theorem only. All bounded-claim tokens hold only if these are cut. NO_RECONSTRUCTION_CLAIM.

- Independent-falsification gate: **NOT satisfied.** The chair authored the feasibility probe, the structure probe, and the DP prototype, wrote the dossier adjudicating them, and performed the "independent" re-run personally — a byte-identical re-run by the author verifies determinism, not correctness. Comité 019's contrary feasibility claim was declared "superseded" by the same author's artifact. Partial mitigation exists (wave-1 mathematician independently re-derived modularity and the ∅-certificate; wave-1 engineer caught the chair's uncommitted-guardrail error, proving the panel is not rubber-stamping). Requirement: the fresh Gate 0 script must be independently reviewed line-by-line against family_A semantics before execution, and the ∅-certificate re-implemented (not re-run) by a non-author, or explicitly labeled author-verified-only in the record.

- Minimal falsification test: **cross-key probe (read-only in spirit, one dev draw, no seal contact):** on the committed BH dev draw (seed 20240617, lowest intensity), call `solve(C, key)` with the *MINK* key t−r instead of t+r. Outcome (a) certificate fails → the selector's output/abstention provably depends on the hidden BH/MINK label through key choice → leakage confirmed, DP blocked until an order-only key derivation is specified and frozen. Outcome (b) certificate passes but argmax or λ* differs from the t+r run → the "same frozen object" claim is false (object is key-dependent). Outcome (c) certificate passes and results are identical → key-invariance evidence, and the leakage objection reduces to specifying any frozen order-only ordering. Every branch is informative; no seed-band or validation contact; this is the cheapest check that attacks the load-bearing weakness of the entire DP route.

## 6. Pre-registration verdict

- **Verdict: PASS** (as a *disposition* decision only — no execution of Part F step 3, no sealed-path run, no validation-band draw is being authorized by adjudicating (1)/(2)/(3) themselves). Any of the three sub-paths becoming an execution step requires a **separate**, later, freeze-then-execute event per the discipline below.

- **Freeze status:** Mixed — and this is the load-bearing finding.
  - The **estimator-v2 / prereg-002 freeze is intact and untouched**: `docs/preregistration_002.md:8` seal hash matches `make verify-seal` output (`6e2c3888…`), confirmed live. Nothing under adjudication here touches `nachocausal/thresholds.py` or the sealed estimator.
  - The **R-VAR μ-freeze addendum (`0271fd9`) is only partially frozen in the git sense.** `git diff HEAD -- dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` shows +48 uncommitted lines (MINK-only M-consumption semantics, dual-consumption diff-test-as-hard-precondition, spawn-form closure, production-feasibility disclaimer, new blocking conditions). These are exactly the guardrails the dossier leans on. **A markdown edit sitting in the working tree is not a freeze** — it is mutable until committed, contradicting the "written before execution, one-way" discipline this role exists to guard (`docs/preregistration_002.md:2-3`, "nothing here may be tuned on a result" — the analogous norm for the addendum is that its governing text must be commit-anchored before it can bind step 3).
  - **New finding beyond the chair's note:** `git ls-files` returns **zero** hits for `docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md`, `docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md`, and `docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md` — all three are untracked (`??` in `git status --short`), i.e. **never committed, not merely edited**. The entire cited adjudication chain ("comité 018 §9.1", "comité 019 §9 options", "AUDIT_006") that this decision's dossier treats as settled precedent is, as of HEAD, working-tree-only text with no git-anchored existence. Per the freeze discipline this role enforces, **no sub-decision here may be reported as "already adjudicated by 018/019" until those documents are themselves committed** — otherwise the record is unauditable and revisable without trace, which is precisely the failure mode RESPECT_SEAL_FREEZE exists to prevent.

- **Seal integrity:** Confirmed unaffected. `make verify-seal` → `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching `docs/preregistration_002.md:8` verbatim. None of (1a)/(1b)/(1-other)/(2)/(3) invoke, modify, or re-run the sealed estimator-v2 path.

- **Seed discipline:** The 12/12 structure-probe draws used dev seeds (`20240617`/`13`/`101`), disjoint from `EXPLORE_POOL` (`1_000_000..1_000_039`, addendum root-block table) and from `VALIDATION_SEEDS` (virgin `2_000_000..2_999_999`, `docs/preregistration_002.md:12-19`). No reserved virgin band is implicated or at risk in this decision. **But**: the same three dev seeds that produced the 12/12 EMPTY-MINK / 12/12 nonempty-BH pattern are the ones being proposed (sub-option 1-other) as grounds to promote EMPTY-vs-nonempty into the calibration object itself — that is using already-observed dev outcomes to select the observable *after seeing them on those exact seeds*. This is dev-band, not validation-band, so it does not burn a virgin seed reserve, but it is still a **freeze-order violation** if promoted directly (see below).

- **Reporting rule:** Textually preserved and must remain so under any redesign: addendum §4c (OOD is a third explicit state, never coerced to PASS/FAIL) and §4d (`rate_empty` is CLAIM-INERT, provenance-only, tied permanently to `NON_CORROBORATION`, comité 017 §8) are the correct instrument and are not weakened by any of the three sub-questions as posed. Any redesign of the object (1a) or promotion of the dichotomy (1-other) must re-declare these two clauses verbatim or explicitly re-derive equivalents — silent lapsing of either during a "spec-level redesign" would itself be a forbidden threshold-loosening move.

- **Forbidden moves present?**
  - **(1a) spec-level redesign of the object/𝒜(C):** Not itself forbidden, but freeze discipline requires: (i) any redesigned object be committed as a new spec/addendum text *before* any further dev-pool draw is consumed under it, mirroring the existing halt-no-adjust pattern (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:395-431`, D.2.3: "no se ajusta el algoritmo ni el test; se reconvoca al comité"); (ii) it is a **new committee question**, per comité-019's own §9 option (b) framing ("a new committee question, not a drafting fix") — that framing is sound and should be preserved regardless of that document's uncommitted status.
  - **(1b) recording Part F non-viable at production:** This is **freeze-compliant and is in fact the discipline working as designed** — it is the direct application of the OOD/halt-no-adjust rule (addendum §4c, D.2.3) rather than an exception to it. It must be reported as a **third explicit state** (non-viable-at-production), not silently folded into either a PASS or a FAIL of R-VAR generally, and must be committed as such (not left as a working-tree note).
  - **(1-other) promoting EMPTY-vs-nonempty as the object:** **BLOCK as proposed.** Promoting an observable to "the object" on the strength of the 12 dev draws already inspected is post-hoc object selection conditioned on outcomes already seen on those exact seeds — this is exactly what NO_POST_HOC_TUNING exists to prevent, independent of dev/validation banding. The wall required: freeze the dichotomy-as-observable in a committed spec/addendum *before* drawing any further confirmatory sample (fresh dev sub-block or, if this is to inform anything beyond dev exploration, a fresh reserved band), i.e. ∀-before-∃ over unobserved seeds, not the ones that motivated the promotion.
  - **(2) interval-DP fresh Gate 0:** Per-tier authorization discipline is explicit and must be followed in full, not partially: Tier 0 toy zero-discrepancy PASS is necessary but **the spec is explicit that it is insufficient** — "Tier 1 sigue siendo obligatorio y no queda satisfecho por el PASS de Tier 0" (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:429-431`). A fresh Tier 1 (≥100 sprinkled posets, N≲14, both MINK and BH, zero-discrepancy vs. brute-force exact-rational reference) must run and PASS before the interval-DP candidate may touch any μ-table computation. Additionally outstanding and unresolved: the mathematician's flag that the prototype's sort key uses embedding coordinates is a live, uncleared NO_GROUND_TRUTH_LEAKAGE risk — Gate 0 zero-discrepancy against a brute-force reference does **not** by itself certify absence of order-illegitimate (embedding-derived) information in the candidate; this must be resolved and documented *before* Tier 1 is treated as satisfying the leakage guardrail, not treated as closed by Tier 0 toy validation.
  - **(3) Part E re-scope:** Amending frozen spec text via committee is the correct and only legitimate instrument (precedent: comité 017 revised v2→v2.1, comité 018 froze the addendum) — this is not itself a forbidden move. What must be preserved in the amendment: (i) it must be a **committed, git-anchored text change** with the old universal claim struck and the new bounded claim ("orders certifying the interval property + typed abstention otherwise") substituted, not a silent in-place edit; (ii) the no-budget-cap clause (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:499-501`) may not be quietly loosened or tightened as a side effect of this amendment — any budget-cap policy change is a distinct committee decision, exactly as comité-019 §9 itself anticipates ("a future compute-budget rule... would itself need to amend Part E's current no-budget-cap text via committee, not be smuggled in").

- **Reasons (anchors):**
  - Seal match: `make verify-seal` output vs `docs/preregistration_002.md:8`.
  - Dev/validation seed disjointness: `docs/preregistration_002.md:9-19`; addendum root-block table (`dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md`, §4b area, EXPLORE_POOL 1_000_000–1_000_039).
  - Uncommitted addendum guardrails: `git diff HEAD -- dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` (+48 lines, 0 hits in `git show HEAD:...`).
  - Untracked committee/auditor record: `git ls-files docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md` → no output (untracked).
  - Halt-no-adjust / third-state OOD: `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:395-431` (D.2.3); addendum §4c/§4d.
  - Part E over-claim text: `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:489-501`.
  - Tier-0-insufficient-alone rule: `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:429-431`.
  - NON_CORROBORATION / CLAIM-INERT permanence: comité 017 §8, addendum §4d.

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| Bombelli 1987 PhD, §2.1/§2.4 (`biblioteca/derived-md/Bombelli_1987_PhD.md` ≈ PDF pp.61-63): "ldim(P)=2 ⟺ cdim(P)=2 (the causal order on 2-dimensional Minkowski space coincides with the coordinate partial order in R², since one can take these coordinates to be the null ones, u=x⁰+x¹ and v=x⁰-x¹)" | Mathematician | CONFIRMED |
| Myrheim 1978 (as cited inside Bombelli 1987, not itself a biblioteca document) | Mathematician | UNVERIFIED — no standalone Myrheim 1978 document in `biblioteca/`; only reachable as a reference inside Bombelli's thesis |
| "Surya LRR 2019 §4" | Mathematician | UNVERIFIED — confirmed absent from `biblioteca/` (matches comité 019's prior finding); should not be relied on |
| Benincasa–Dowker 2010 (`Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.pdf`) — link/cover-relation definition and interval-abundance action | Mathematician | UNCONFIRMED (partial) — substance (link = cover relation; abundances feed the action) is in the paper, but the operator is denoted **B**, never "C_k"; the d+ identification is a project-derived interpretive bridge, not literal source notation |
| EGS p.7 §II.A: constant det g in (t*,r); coordinate-uniform Poisson = natural volume | Physicist | CONFIRMED (verbatim, derived-md:164) |
| EGS p.10 §III: event horizon needs infinite sprinkling; futureless points at J⁺ vs near singularity indistinguishable in a finite patch | Physicist | CONFIRMED (derived-md:217-224) |
| EGS p.10-11 §III: interior timelike curves reach r=0 in finite proper time, truncating futures | Physicist | CONFIRMED (derived-md:226) |
| EGS p.11-12: future-cardinality varies between n and √n already in Minkowski | Physicist | CONFIRMED (derived-md:247) |
| EGS p.8 Fig.1: outgoing rays "tilt over" at the horizon | Physicist | CONFIRMED (derived-md:187) |
| EGS p.25 Fig.12: outgoing ladders reverse direction across r_S | Physicist | CONFIRMED as paraphrase (actual text: "change from growing towards larger r/rS ... to growing towards smaller r/rS", derived-md:562) |
| EGS "p.11 §III" regular-BH caveat ("would no longer work for regular black holes") | Physicist | UNCONFIRMED on page number — the sentence is on PDF p.12 (derived-md:249); content correct, page off by one (corrected inline in §4 above) |
| EGS p.9-10 Hayward regular-BH discussion | Physicist | CONFIRMED (derived-md:205-213) |
| Interval/2D-order lemma (up-set ∩ antichain = suffix∩prefix = interval) | Mathematician | UNVERIFIED / no biblioteca source — full "suffix" keyword sweep across all 56 PDFs: zero hits; project-derived, matches comité 019's finding that the library has nothing on this algorithmic question |
| `nachocausal/generator.py:88-127` ingoing-EF convention vs EGS eq.(6) t* | Physicist | CONFIRMED by construction match (comments never say "ingoing" explicitly — correct but implicit inference); the external Minz `spacetimes.py:759` reference is UNVERIFIED (repo not present) |
| "EGS 400 sprinklings of average size n=10³" (derived-md:237) | Chair/dossier | CONFIRMED |

- **Notes:** (1) "Surya LRR 2019 §4" does not exist anywhere in `biblioteca/` — drop or replace;
  the order-dimension-2 claim survives on Bombelli 1987 alone, which is CONFIRMED and is the
  load-bearing anchor. (2) The mathematician's "C_k"/"d+" terminology for the Benincasa–Dowker
  construction is a valid project-authored conceptual bridge, not literature notation (BD use
  **B**/N_k) — keep it labeled as a bridge. (3) EGS regular-BH caveat page corrected p.11→p.12.
  (4) The interval/2D-order suffix∩prefix lemma is wholly project-derived; it must continue to be
  flagged as such (not literature-anchored) wherever the DP is described.

## 8. Synthesis

**The committee answers all three sub-questions, and the answers converge with unusual
unanimity across all seven seats.** The PI's mid-session steer (re-scope the immediate goal to
order-only singularity/truncation; if even that fails, close or convert to a negative result) is
adopted as the recommended forward direction, with the guardrails below.

**(1) Disposition of Part F: record it as BLOCKED_BY_MEASURED_DEGENERACY, never executed.**
Every seat that engaged with the question — physicist ("the physically honest reading"),
warden ("freeze-compliant and in fact the discipline working as designed"), logician, falsifier —
supports recording that Part F as frozen cannot proceed: the compute blocker (`014d364`) is real
but secondary; the binding fact is that the frozen calibration object is empty on its own MINK
null substrate at production scale (certified on 12/12 dev draws; **strongly-supported empirical
prediction, not theorem, for the untouched M=200 pool** — logician's labeling is adopted). Two
falsifier-mandated precisions bind the record: (i) the disposition is *"Part F never executed —
blocked by measured degeneracy of the frozen object"*, NEVER *"Part F produced
OUT_OF_DOMAIN_UNCALIBRATED"* (the §4c token can only be produced by running); (ii) the BH-side
"family nonempty" statement rests partly on claim-inert DP output (the ∅-certificate is one-way)
and is recorded as such. The physicist's mechanism analysis stands: MINK emptiness is a box
aspect-ratio artifact that *worsens* with N (correcting comité 019's physicist), while BH
nonemptiness is genuine EGS singularity truncation — which is exactly why the PI's re-scope
direction is scientifically live.

**(1-other) The EMPTY-vs-nonempty dichotomy as an object: REJECTED, unanimously.** Physicist
(conflates a genuine truncation signal with a box artifact; corner-artifact argmax; regular-BH
caveat), logician (∀-before-∃ violated by the 12 already-seen draws), warden (BLOCK as proposed —
textbook post-hoc object selection), falsifier (a detector of frozen box constants; OOD→PASS
coercion). Any future truncation-based object must be **graded** (a score with a non-degenerate
MINK null — EGS's future-cardinality/longest-chain bimodality direction), frozen in a committed
spec before any confirmatory draw, and scoped explicitly to *Schwarzschild-singularity
truncation* so the EGS regular-BH caveat becomes part of the claim rather than a threat to it.
This is the PI's steer, formalized: **new committee question + own prereg + own Gate 0 chain; if
that object fails its own gates, R-VAR closes as a documented negative result.** Closing R-VAR
would not touch the project's primary result (prereg-002 PASS, estimator-v2 track, seal intact).

**(2) Interval-DP: legitimate dev exploration, currently DISQUALIFIED for any scoring use, gated
behind five named preconditions.** The mathematics survived hostile review — modularity and the
∅-certificate were independently re-derived (mathematician), the 2D-order anchor is CONFIRMED in
Bombelli 1987, and the certificate supersedes comité 019's "emptiness needs 2^|Max|" claim. But
the falsifier's attack lands three disqualifying hits as-implemented: the sort key is
embedding-derived AND switched on the hidden `kind` label (leakage VERIFIED at
`explore_rvar_interval_dp.py:260-262`); the object as implemented is *key-augmented*, not the
bare frozen selector; and the float64/1e-6 shortcut creates a numeric failure mode exactly where
no Gate 0 can reach. Preconditions before any further status: (a) an **order-only key
derivation** specified and frozen (or proven key-invariance); (b) the falsifier's **cross-key
probe** run first (cheapest, every branch informative); (c) typed abstentions for
`NO_CONVERGENCE` and certificate-fail (no raw `raise`, no silent third status); (d) exact
arithmetic or proven precision bounds (no float64 termination heuristic); (e) fresh Gate 0 —
criteria committed *before* running, Tier 0 multi-poset + Tier 1 ≥100 sprinkled posets both
kinds (Tier 0 alone insufficient per spec :429-431), zero discrepancy vs `family_A`, plus
independent non-author line review (the independence gate is currently NOT satisfied: the chair
authored every probe and the prototype; wave-1's independent re-derivations are the partial
mitigation). The physicist adds the sobering frame: even a perfect DP only computes the same
degenerate object faster — it is an enabler for a *redesigned* object, not a rescue of Part F.

**(3) Part E re-scope: YES — proceed, as a committed amendment.** Unanimous (mathematician:
false as written; logician: false universal; physicist: 1+1D geometric fact, not poset-generic;
falsifier: add the key-dependence caveat; warden: correct instrument, no-budget-cap clause
untouched as a side effect). The replacement claim: *computable in polynomial time for finite
orders that pass the per-draw interval certificate under a frozen, order-only antichain
ordering; typed abstention otherwise* — with the interval lemma flagged as project-derived (no
biblioteca source, per §7).

**(0) Before any of it: commit the record.** The warden's finding is the sleeper result of this
session: the entire adjudication chain (comité 015–019, auditor 003–006) is untracked, and the
addendum's load-bearing guardrail sections are +48 uncommitted lines. A working-tree freeze is
not a freeze. The falsifier's condition for committing the addendum edit now (post-outcome text)
is that it is strictly tightening, and the commit message must say so.

**Open disagreements, none hidden:** (i) falsifier vs physicist on using the claim-inert argmax
shape (|D*|≈N−few, B∈{3..8}) — resolved by recording it as red-team/physical intuition, not
evidence; (ii) the chair's dossier initially misstated the addendum sections as committed —
caught by the engineer, corrected in §2; (iii) comité 019's physicist prediction and its
"emptiness needs enumeration" claim are both superseded by measurement/certificate — recorded,
with the process lesson that this is the second consecutive session in which a committee-level
assertion fell to a cheap direct measurement; (iv) the independence-gate deficiency
(chair = author of all three artifacts) is acknowledged, partially mitigated by wave-1's
independent re-derivations and error-catching, and bound as precondition (e) above.

## 9. Next-step spec

**Reversible steps (may be run now if the user asks; dev seeds only, no EXPLORE_POOL, no
VALIDATION_SEEDS, no seal contact):**

1. **Falsifier's cross-key probe** (minimal falsification test, adopted as mandatory first move
   for the DP route): on the BH dev draw (seed 20240617, intensity 1500), run `solve(C, key)`
   with the MINK key `t−r`; compare against the `t+r` run. Branch (a) certificate fails →
   leakage confirmed, DP blocked pending an order-only key; (b) passes but differs → the
   "same object" claim is false as implemented; (c) passes identically → key-invariance
   evidence. Every branch informative; write-up goes to dev/, claim-inert.
2. Draft (not commit) the Part E amendment text and the Part F disposition note, for committee/PI
   review.

**Committing steps (each requires explicit user authorisation; sequenced):**

3. **Record-commit (priority zero):** commit `docs/comite/comite_decision_015..020`,
   `docs/auditor/auditor_report_003..006`, and the addendum's +48-line working-tree edit — the
   addendum commit message must state the edit is **strictly tightening, drafted post-outcome**
   (falsifier's condition). Until this lands, no sub-decision may cite 018/019 as settled
   precedent (warden).
4. **Disposition-commit:** record Part F status as
   `PARTF_STATUS = BLOCKED_BY_MEASURED_DEGENERACY [NEVER_EXECUTED; FROZEN_OBJECT_VACUOUS_ON_MINK_NULL_AT_PRODUCTION (strongly-supported empirical prediction, 12/12 dev draws certified); COMPUTE_BLOCKER_SECONDARY (014d364)]`
   — a third explicit state, not PASS, not FAIL, not OOD (addendum §4c semantics reserved for
   actual runs).
5. **Part E re-scope amendment** (sub-question 3): committed text change striking "para todo
   poset finito", substituting the bounded claim from §8, leaving the no-budget-cap clause
   untouched, flagging the interval lemma as project-derived.
6. **If the PI pursues the re-scoped goal** (order-only Schwarzschild-singularity-truncation
   localisation with a graded observable and non-degenerate MINK null): convene a NEW `/comite`
   question to define that object — the dichotomy shortcut is prohibited (§8); the freeze must be
   ∀-before-∃ on seeds not yet seen; the EGS regular-BH caveat enters the claim text itself. If
   that object later fails its own Gate 0 / calibration, R-VAR closes as a documented negative
   result (PI's stated criterion, adopted).
7. **Interval-DP continuation (only if step 6 needs it):** preconditions (a)–(e) of §8(2) in
   order, cross-key probe first, Gate 0 criteria committed before running, independent non-author
   review required.

**Binding rules pre-committed:** `NO_RECONSTRUCTION_CLAIM` (nothing here claims localisation
beyond the finite 1+1D patch; the truncation re-scope is *narrower*, not broader);
`NO_POST_HOC_TUNING` / `NO_THRESHOLD_LOOSENING` (the dichotomy promotion stays rejected; M, α,
levels untouched; any new object = new freeze, not an amendment of μ); `NO_GROUND_TRUTH_LEAKAGE`
(the DP is disqualified until the key is order-only; the abstain/OK boundary may not be defined
by embedding coordinates); `RESPECT_SEAL_FREEZE` (seal verified unchanged this session; nothing
touches `nachocausal/`); `NON_CORROBORATION` and `rate_empty` CLAIM-INERT (§4d) persist verbatim
into any redesigned object. **Falsifier's minimal falsification test:** the cross-key probe of
step 1, mandatory before any DP continuation decision.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off

**Signed: PI (adnacho), 2026-07-05**, via structured sign-off in-session. Decisions:

1. **Record-commit authorized** (§9 step 3): comité 015–020, auditor 003–006, and the addendum's
   +48-line strictly-tightening working-tree edit, committed with the falsifier's
   post-outcome/tightening-only declaration.
2. **Cross-key probe authorized and run** (§9 step 1): result recorded in
   `dev/rvar_crosskey_probe_result.json`.
3. **Direction signed:** the immediate goal is re-scoped to **order-only
   Schwarzschild-singularity-truncation localisation with a graded observable and a
   non-degenerate MINK null** (a new `/comite` question will define the object; freeze
   ∀-before-∃ on unseen seeds; the EGS regular-BH caveat enters the claim text). If that object
   fails its own Gate 0 / calibration, **R-VAR closes as a documented negative result.**
4. The rejection of the EMPTY-vs-nonempty dichotomy as an object is ratified.

Steps 4–5 of §9 (disposition-commit with the `PARTF_STATUS` token; Part E re-scope amendment)
remain pending as separate, explicitly-authorized committing steps.
