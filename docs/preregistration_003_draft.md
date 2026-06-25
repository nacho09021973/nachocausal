# Pre-registration 003 — DRAFT (PR-003 Fase #3 result: operational resolution floor)

> ## ⚠ DRAFT — NOT FROZEN, NOT YET A PRE-REGISTRATION
>
> This file is a **dev / reversible draft** of what `docs/preregistration_003.md` *would*
> register. It freezes nothing, seals nothing, and touches **no** `RESERVED_002` seed. It is
> NOT the prereg-003 seal. Freezing is a separate, committing step (§8 below) that requires
> `/comite` + `/auditor` + explicit user authorisation, and only at that point is the
> non-draft `docs/preregistration_003.md` created. Until then every number here is a pointer to
> a committed dev artefact, to be re-verified literally by `/auditor` before any freeze.
>
> Authorised by `docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md` §9 **C1**
> (`COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`, ACCEPTED 2026-06-24).
> Sealed instrument unchanged: `nachocausal/thresholds.py` SHA256 =
> `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (`make verify-seal`).

## 1. What this result IS (the precise claim to be registered)

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
  direction. **The minimax bound over `C` is left explicitly OPEN** (future work; §7). Do not
  phrase the frozen result as a universal information limit.
  [grounding: `dev/PR003_INFO_BOUND_NOTES.md` §0, §7-O1, reclassified 2026-06-25.]
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

## 3. Evidence (all committed, dev, EXPLORE_POOL only — to be re-verified by /auditor)

The operational floor (★) rests on three legs plus one hardening probe; all live in
`dev/PR003_INFO_BOUND_NOTES.md` (R1) and `dev/PR003_KBEAM_PEELOFF_NOTES.md` (R2):

1. **In-repo anchor (§3 of the notes).** The frozen thresholds already encode (★):
   `theta_loc = K_LOC·ℓ/(2M)`, `theta_stab = K_LOC·ℓ`, `K_LOC = 2`, `POOLED_SD_FLOOR = 0.5`
   ("one O-discreteness unit") — `thresholds.py:78,98,106-108,111-113`.
2. **Numerical illustration O3 (§6 of the notes).** `dev/measure_info_bound_o3.py`, 24
   EXPLORE_POOL seeds × frozen INTENSITIES `(1500,3000,6000,12000)`, MINK same-cloud control,
   GPU build bit-identical to sealed CPU for this observable (`maxdiff = 0`): `r̂` scatter
   `≈ 0.40·ℓ`, **density-invariant** over ×8 density; the whole `TVg(r̂)` curve collapses onto a
   single function of `s/ℓ`; resolvable separation `2s/ℓ ≈ 0.6`. ⇒ measured constant `O(1) < 2`.
3. **Analytic Jacobian O2 (§7 of the notes).** `dO/dr = ρ·dA_fut/dr`, log-enhanced near `r_S`
   (tortoise term); `σ_O ∝ 1/ℓ` over `dO/dr ∝ 1/ℓ²` ⇒ `ρ` cancels ⇒ `δr = ℓ·√(A_fut)/(dA_fut/dr) ∝ ℓ`,
   dimensionless O(1) constant `≈0.4` pinned by leg 2. O1 (the KL of the output) is the
   **operational** companion, explicitly NOT a minimax statement (see §2).
4. **Hardening — R2 K-beam peel-off (`dev/PR003_KBEAM_PEELOFF_NOTES.md`).** Widening the beam
   K = 1→64 enumerates ~50× more ladders but the order-only top-1 `d⊥/ℓ@k=8` stays ≈5-7ℓ and the
   min-beam plateaus ≈4-6ℓ; only the head (k≤3) adheres ≈2ℓ. The peel-off is **not** greedy
   myopia ⇒ evidence the wall is **physical within the box's reach**. **Caveat:** under-reach
   (reach≥8 ≤23 % at `t_edge=6`) ⇒ label is "PHYSICAL within box reach", not unconditional; the
   only way to reopen extension is a taller-box prereg (C2, out of scope).

## 4. The anchor and the no-new-constant rule (binding)

The frozen constant is `K = K_LOC = 2`, **already sealed** in `thresholds.py` since prereg-002.
This draft (and the eventual freeze) introduces **no new data-tuned constant**: leg 2 reports
that the measured constant is `O(1) < 2`, which is a *consistency* statement about the existing
seal, not a recalibration. Re-tuning `K` on the EXPLORE_POOL measurement would be
reverse-engineering and is forbidden (`pr003_leakage_gate.md` contract #5).

## 5. Relation to the prereg-002 PASS

prereg-002 (`docs/preregistration_002_result.md`, verdict PASS) already established, on 20
held-out RESERVED_002 seeds under the sealed instrument, that order alone localises the boundary
significantly and stably within the patch, with `median|dr|/2M = 0.064 ≤ θ_loc` and
`r_std = 0.008 ≤ θ_stab`. (★) is the *information-side reading* of that same sealed instrument:
the localisation cannot be sharpened below `O(ℓ)` by this estimator. No new blind run is required
for (★); it consolidates the already-validated instrument. (If, on freeze, the committee wants an
independent confirmatory blind quantity, that would be specified here — currently none is needed.)

## 6. Falsifiability / how a freeze would be checked

- **Anchor freeze-check:** `K = K_LOC = 2` is the sealed value; `make verify-seal` =
  `6e2c3888…` before and after; no `M nachocausal/`.
- **Direction-of-claim check (the O1 reclassification):** the frozen text must say "sealed
  estimator's resolution", never "no estimator of `C` can do better". `/auditor` to confirm the
  document does not reintroduce the minimax phrasing.
- **Number-provenance check:** every figure in §3 must be literal output of a committed script
  (`measure_info_bound_o3.py`, `measure_kbeam_peeloff.py`) with its git-ignored log regenerable
  on demand — `/auditor`'s standing job.

## 7. Open items (explicitly NOT closed by this result)

- **OPEN — minimax floor over `C`.** Requires an upper bound on `KL(P^C_0‖P^C_1)` of the full
  causal set; the present evidence is the wrong side of the data-processing inequality (§2). This
  is the genuine future-work item, separate from (★).
- **O4 — literature.** Source Le Cam framing (Tsybakov 2009, *Introduction to Nonparametric
  Estimation*, Thm 2.2) and any causal-set information-theory precedent into `biblioteca/` before
  citing. By itself O4 does **not** close the inequality-direction gap above.
- **C2 — taller-box prereg** (`t*/r_S∈[0,50]`) to address the R2 under-reach caveat: a NEW prereg
  (different `BOX_AREA`/ℓ table), out of scope here.

## 8. Procedure to turn this DRAFT into the frozen prereg-003 (committing — needs separate OK)

1. Review/iterate this draft (reversible, dev).
2. `/comite` over the draft (one-way step) → freeze-check + falsification of the claim form/scope.
3. `/auditor` → verify every published number is literal committed-script output and the document
   does not over-claim beyond the operational, finite-patch 1+1D resolution floor.
4. Only then create `docs/preregistration_003.md` (non-draft) and commit it as the prereg-003
   freeze — atomic on `main` (verify `git branch --show-current = main`; shared-checkout `formula`
   hazard), `make verify-seal` = `6e2c3888…` before+after, `git status` shows no
   `M nachocausal/` and no `M docs/preregistration_*`.

---

> **Provenance of this draft.** Branch `main`; dev/reversible; no seed drawn; seal `6e2c3888…`
> intact. Grounding files: `dev/PR003_INFO_BOUND_NOTES.md` (R1, O1 reclassified 2026-06-25),
> `dev/PR003_KBEAM_PEELOFF_NOTES.md` (R2), `docs/preregistration_002_result.md` (PASS),
> `docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md` §9 (C1).
