# Pre-registration 003 — PR-003 Fase #3 result: operational resolution floor (FROZEN)

> ## ✔ FROZEN PRE-REGISTRATION — 2026-06-25
>
> This is the frozen prereg-003. It registers the PR-003 Fase #3 result as an **operational
> (estimator-induced) resolution floor** of the sealed v2 estimator. It changes **no** code, seals
> **no** new constant, and touches **no** `RESERVED_002` seed: the freeze is doc-only. Sealed
> instrument unchanged — `nachocausal/thresholds.py` SHA256 =
> `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (`make verify-seal`,
> confirmed before and after this commit).
>
> **Provenance chain (all artefacts committed):**
> - Authorised by `docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md` §9 **C1**
>   (`RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`, ACCEPTED 2026-06-24).
> - Foundation audit `docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md`
>   = `AUDIT_PASS_WITH_WARNINGS` (warning W1: GPU-venv figures not re-executed under sealed numpy).
> - Freeze-readiness committee `docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md`
>   = `RECOMMEND_REVISE_AND_RECONVENE` (revisions B1–B8 + the W1 re-run required first).
> - **R-1 (W1 discharged):** `dev/measure_info_bound_o3.py` and `dev/measure_kbeam_peeloff.py`
>   re-run under the SEALED numpy 1.26.4 (CPU); they reproduce the §3 figures (logs
>   `dev/o3_sealed_numpy_rerun.log`, `dev/kbeam_sealed_numpy_rerun.log`).
> - **R-2:** this text was revised per comité-004 §8 B1–B8.
> - **C-1 re-audit** of the revised text `docs/auditor/auditor_report_002_pr003-c1-revised-draft.md`
>   = `AUDIT_PASS` (0 errors, 0 warnings).
> - **C-2 reconvene** (focused warden + falsifier): warden PASS, falsifier all seven objections
>   RESOLVED — no freeze-blocker.
> - **C-3:** explicit user authorisation, 2026-06-25 ("crear + commitear en main").
> - The dev/reversible draft this was frozen from is retained at
>   `docs/preregistration_003_draft.md`.

## 1. What this result IS (the precise registered claim)

The PR-003 Fase #3 result is an **operational (estimator-induced) resolution floor** for the
**sealed v2 estimator** viewed as a channel `T: C ↦ r̂` from the causal order `C` to the
radial boundary estimate `r̂`:

```
    Error( r̂ − r_S )  ≳  K · ℓ  =  K · ρ^(-1/2) ,      K = O(1)              (★)
```

in the frozen finite 1+1D patch (`BOX_AREA = T_EDGE·R_EDGE = 7.2`,
`thresholds.py:36-43`) at density `ρ = intensity / 7.2`, with discreteness scale
`ℓ = ρ^(-1/2)`. The constant is **not newly tuned**: it is the already-sealed `K_LOC = 2`
(`thresholds.py:98,106-108,111-113`), and the measurement (§3) shows the true operational
constant is `O(1) < 2`, i.e. `K_LOC = 2` is a **conservative ceiling**, reported — not re-sealed.

This is the consolidation pre-committed in `comite_decision_002` §9 and reaffirmed in
`comite_decision_003` §11: the reconstructible object is intrinsically the `O(ℓ)` seed
neighbourhood (`BARE_RELOCALISATION`); the extended-object cascade closed negative
(expansion S1/S2 NEGATIVE; iterative reseed S3 non-converging).

## 2. What this result is NOT (binding scope — read before §3)

- **NOT a Le Cam minimax lower bound over all functions of `C`.** (★) bounds the resolution of
  the *output* of the **sealed** estimator. A genuine minimax floor over every estimator
  `r̂ = f(C)` would require an **upper** bound on the full-data divergence
  `KL(P^C_0 ‖ P^C_1)` / `TV(P^C_0, P^C_1)`. The information evidence we have (R1 / O1) is a KL of
  the *output* `r̂ = T(C)`, and by the data-processing inequality
  `KL(P^{r̂}_0‖P^{r̂}_1) ≤ KL(P^C_0‖P^C_1)` it bounds the full-data KL **from below** — the wrong
  direction. **The minimax bound over `C` is left explicitly OPEN** (future work; §7). This frozen
  result is NOT a universal information limit.
  [grounding: `dev/PR003_INFO_BOUND_NOTES.md` §0, §7-O1, reclassified 2026-06-25.]
- **NOT an order-theoretic universal over estimators — it is the limit of OUR sealed tool.** (★) is
  a property of the *specific* sealed channel `T: C ↦ r̂` built from the future-VOLUME observable
  `O(i)=|future(i)|`. It is NOT a statement that no order-only estimator can localise finer than
  `O(ℓ)`; a different order-only statistic could in principle do better, and whether one does is
  left **OPEN** (§7). Note the future-volume observable is a *sibling* of EGS's primary longest-chain
  split, not the identical EGS statistic, and EGS flag the future-cardinality as boundary-sensitive
  ("varies between `n` and `√n` already for Minkowski", EGS md:193; comité-004 literature CONFIRMED).
  [grounding: comité-004 §8 B6, §4 mathematician + physicist.]
- **NOT a universal / asymptotic no-go.** The global event horizon needs an infinite sprinkling
  (EGS arXiv:2605.06813; comité-003 literature 1a CONFIRMED). (★) is a finite-`V`, finite-`ρ`
  statement.
- **NOT a regular-black-hole or non-Schwarzschild claim.** The truncation mechanism that makes
  `O(i)` carry the boundary is singular-Schwarzschild-specific (EGS derived-md:463-465;
  comité-003 literature 1f CONFIRMED).
- **NOT 3+1D, NOT Kerr, NOT metric reconstruction.** It stays inside the prereg-002 frozen
  language: "order-only localisation of the horizon-associated boundary within a finite patch"
  (`docs/preregistration_002_result.md`).
- **A lower bound is not falsified by one faster method.** A single estimator beating (★) would
  signal ground-truth leakage, to be audited against `docs/pr003_leakage_gate.md`, not taken as
  refutation (comité-003 §5 falsifier).

## 3. Evidence (all committed, dev, EXPLORE_POOL only — re-verified by /auditor + sealed re-run)

The operational floor (★) rests on three legs plus one hardening probe; all live in
`dev/PR003_INFO_BOUND_NOTES.md` (R1) and `dev/PR003_KBEAM_PEELOFF_NOTES.md` (R2). Every figure was
re-verified by `/auditor` (`auditor_report_002`, `AUDIT_PASS`) and reproduced under the sealed numpy
1.26.4 in R-1:

1. **In-repo anchor (§3 of the notes).** The frozen thresholds already encode (★):
   `theta_loc = K_LOC·ℓ/(2M)`, `theta_stab = K_LOC·ℓ`, `K_LOC = 2`, `POOLED_SD_FLOOR = 0.5`
   ("one O-discreteness unit") — `thresholds.py:78,98,106-108,111-113`.
2. **Numerical illustration O3 (§6 of the notes).** `dev/measure_info_bound_o3.py`, 24
   EXPLORE_POOL seeds × frozen INTENSITIES `(1500,3000,6000,12000)`, MINK same-cloud control. The
   per-element future-volume `O`-multiset is GPU≡CPU **bit-identical** (`maxdiff = 0`, integer
   observable); the downstream *float* figures (`r̂` scatter, `2s/ℓ`) are reproducible only
   *statistically*, not bit-level (GPU `np.log` ulp flips, `measure_info_bound_o3.py:47-49`) — so
   this result makes **no** bit-level reproducibility claim for the float figures. Result: `r̂`
   scatter `sd(r̂)/ℓ = 0.34 / 0.45 / 0.39 / 0.40` across the four intensities — i.e. `≈ 0.4·ℓ`,
   density-invariant within ≈30% over **×8 in density** (which is only **×2.83 in `ℓ`**:
   `ℓ = 0.069 → 0.024`); the whole `TVg(r̂)` curve collapses onto a single function of `s/ℓ`;
   resolvable separation `2s/ℓ = 0.60 / 0.47 / 0.62 / 0.71`. ⇒ measured constant `O(1) < 2`.
   **Sealed-environment confirmation (R-1, audit W1 discharged):** re-run on the SEALED
   numpy 1.26.4 (CPU, `--device cpu`) reproduces the scatter table `0.34/0.45/0.39/0.40` and the
   `2s/ℓ` row to the reported 2-decimal precision (seal `6e2c3888…` asserted pre+post; log
   `dev/o3_sealed_numpy_rerun.log`) — the constant is **not** an artefact of the GPU venv.
3. **Analytic Jacobian O2 (§7 of the notes).** `dO/dr = ρ·dA_fut/dr`, log-enhanced near `r_S`
   (tortoise term); `σ_O ∝ 1/ℓ` over `dO/dr ∝ 1/ℓ²` ⇒ `ρ` cancels ⇒ `δr = ℓ·√(A_fut)/(dA_fut/dr) ∝ ℓ`,
   dimensionless O(1) constant `≈0.4` pinned by leg 2. This leg is an explicit *scaling sketch*
   (Poisson `σ_O≈√O`, equal-variance approximations), not a theorem. O1 (the KL of the output) is the
   **operational** companion, explicitly NOT a minimax statement (see §2).
4. **Hardening — R2 K-beam peel-off (`dev/PR003_KBEAM_PEELOFF_NOTES.md`; 6 EXPLORE_POOL seeds,
   intensities 3600/7200/14400).** Under the *specific* order-only ranking tested (interval-cardinality
   regularity `−(|cp−c₀|+|cq−c₀|)`), widening the beam K = 1→64 enumerates ~50× more ladders but the
   order-only top-1 `d⊥/ℓ@k=8` stays ≈5-7ℓ and the min-beam plateaus ≈4-6ℓ; only the head (k≤3) adheres
   ≈2ℓ. The peel-off is **not** greedy myopia ⇒ evidence the wall is **physical within the box's reach**.
   **Caveats:** (a) under-reach — the fraction of seeds whose ladders reach `k=8` is ≤23 % even at K=64,
   `t_edge=6` ⇒ the label is "PHYSICAL within box reach", **not** unconditional; (b) the verdict is
   established only for the tested ranking criterion — a *different* order-only score might rank
   differently (`PR003_KBEAM_PEELOFF_NOTES.md:80`); (c) the single low-`d⊥` datum at intensity 14400/K=1
   rests on **one** ladder (anecdotal, notes:44-45) and is **not** load-bearing; the headline pools
   3600/7200. The only way to reopen extension is a taller-box prereg (C2, out of scope).
   **Sealed-environment confirmation (R-1):** the integer ladder enumeration is deterministic
   and the sealed numpy 1.26.4 (CPU) re-run reproduces the table essentially exactly (e.g. 7200: top-1
   `d⊥/ℓ@k=8` K=1→64 = 3.21→6.63, `n` = 8→147, reach = 23 %; log `dev/kbeam_sealed_numpy_rerun.log`).

## 4. The anchor and the no-new-constant rule (binding)

The frozen constant is `K = K_LOC = 2`, **already sealed** in `thresholds.py:98` since the
estimator-v2 / prereg-002 seal `6e2c3888…` (commit `573cfcb`), i.e. **before any PR-003 Fase #3
measurement existed** — so "conservative ceiling" is a pre-measurement fact, not a post-hoc label.
This freeze introduces **no new data-tuned constant**: leg 2 reports
that the measured constant is `O(1) < 2`, which is a *consistency* statement about the existing
seal, not a recalibration. Re-tuning `K` on the EXPLORE_POOL measurement would be
reverse-engineering and is forbidden (`pr003_leakage_gate.md` contract #5).

## 5. Relation to the prereg-002 PASS

prereg-002 (`docs/preregistration_002_result.md`, verdict PASS) already established, on 20
held-out RESERVED_002 seeds under the sealed instrument, that order alone localises the boundary
significantly and stably within the patch, with `median|dr|/2M = 0.064 ≤ θ_loc` and
`r_std = 0.008 ≤ θ_stab`. (★) is the *information-side reading* of that same sealed instrument:
the localisation cannot be sharpened below `O(ℓ)` by this estimator. No new blind run is required
for (★); it consolidates the already-validated instrument.

## 6. Falsifiability of (★)

**Positive falsification criterion for (★) (pre-committed — the route to FAIL).** (★) is the claim
that *the sealed channel* `T: C ↦ r̂` cannot resolve `r_S` finer than `≈ 0.4·ℓ` (with `K_LOC=2·ℓ`
the conservative reported ceiling). It is **falsified** if, on EXPLORE_POOL clouds at matched density,
the *sealed* estimator's blind error `median|r̂ − r_S|` is found to be materially below the registered
floor — concretely `< 0.2·ℓ` (half the measured `≈0.4·ℓ`) at any of the frozen intensities — which
would show the constant was not conservative and the floor mis-stated. **Scope note (declared, not
a hedge):** this criterion is evaluated on EXPLORE_POOL (no new RESERVED_002 blind run — (★)
consolidates the already-validated instrument, §5), so it trips only on a *systematic* error, not a
borderline one; its bite is correspondingly lower than a held-out test would give. Because (★) is
scoped to the sealed channel, a *different* order-only estimator localising finer does **not** falsify
(★) — it would instead resolve the OPEN minimax-over-`C` question of §7 — UNLESS it does so by reading
the hidden embedding, in which case it is a leakage finding to be audited against
`docs/pr003_leakage_gate.md`, not a refutation. This asymmetry is declared in advance, not invoked
post-hoc. [comité-004 §8 B1, §5 falsifier.]

Standing freeze-integrity checks (discharged at this freeze):
- **Anchor freeze-check:** `K = K_LOC = 2` is the sealed value; `make verify-seal` =
  `6e2c3888…` before and after; no `M nachocausal/`.
- **Direction-of-claim check (the O1 reclassification):** the text says "sealed
  estimator's resolution", never "no estimator of `C` can do better" — confirmed by `/auditor`
  (`auditor_report_002` §6, no residual minimax phrasing).
- **Number-provenance check:** every figure in §3 is literal output of a committed script
  (`measure_info_bound_o3.py`, `measure_kbeam_peeloff.py`); both re-run under the sealed numpy
  1.26.4 (R-1) reproduce the §3 figures (logs `dev/o3_sealed_numpy_rerun.log`,
  `dev/kbeam_sealed_numpy_rerun.log`).

## 7. Open items (explicitly NOT closed by this result)

- **OPEN — minimax floor over `C`.** Requires an upper bound on `KL(P^C_0‖P^C_1)` of the full
  causal set; the present evidence is the wrong side of the data-processing inequality (§2). This
  is the genuine future-work item, separate from (★).
- **O4 — literature.** Source Le Cam framing (Tsybakov 2009, *Introduction to Nonparametric
  Estimation*, Thm 2.2) and the Bretagnolle–Huber inequality and any causal-set information-theory
  precedent into `biblioteca/` before citing. **These sources are PHYSICALLY ABSENT from `biblioteca/`
  (comité-004 literature verdict: UNVERIFIED — ABSENT), so this frozen prereg-003 does NOT cite Thm 2.2
  or Bretagnolle–Huber as established support.** The result (★) does **not** depend
  on them: its evidence is the operational O2/O3 legs (§3); the Le Cam / Bretagnolle–Huber framing lives
  only in the O1 *diagnostic*, which §2 already downgrades. By itself O4 does **not** close the
  inequality-direction gap above.
- **C2 — taller-box prereg** (`t*/r_S∈[0,50]`) to address the R2 under-reach caveat: a NEW prereg
  (different `BOX_AREA`/ℓ table), out of scope here.

---

> **Provenance of this freeze.** Branch `main`; doc-only; no seed drawn; seal `6e2c3888…`
> intact (verified before+after the freeze commit). Grounding files:
> `dev/PR003_INFO_BOUND_NOTES.md` (R1, O1 reclassified 2026-06-25),
> `dev/PR003_KBEAM_PEELOFF_NOTES.md` (R2), `dev/o3_sealed_numpy_rerun.log` +
> `dev/kbeam_sealed_numpy_rerun.log` (R-1 sealed re-run),
> `docs/preregistration_002_result.md` (PASS),
> `docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md` §9 (C1),
> `docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md` (freeze-readiness),
> `docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md` +
> `docs/auditor/auditor_report_002_pr003-c1-revised-draft.md`,
> `docs/preregistration_003_draft.md` (the dev draft this was frozen from).
