# Pre-registration 001 — Addendum: frozen thresholds & sealed instrument

Status: **FROZEN** (block #4). This addendum fixes, *in writing and before any
validation seed is generated or analysed*, every threshold value, the boundary
definition, the geometry, the ensemble, and the validation seed set required by
`docs/preregistration.md:37-67`. It seals the committed package `nachocausal/`.
No value here is reverse-engineered from a dev outcome (`preregistration.md:49,55`);
each carries a principled anchor.

A 4-member independent review committee audited the freeze design (all four
verdicts: APPROVE-WITH-CHANGES); their CRITICAL/MAJOR findings are incorporated
and tagged `[cmte]` below. This realises the prereg's independent-falsification
gate (`preregistration.md:74-78`).

## Amendment A1 — significance statistic: Hartigan dip → control permutation

`preregistration.md:52` named "a standard bimodality test ... e.g. Hartigan dip
p<0.01." Dev work (`dev/PHASE0_NOTES.md:58-84`) established that the raw dip
p-value is **invalid on our tied integer O**: the box-matched flat control trips
dip p<0.01 at 12–50 % (a small-value-range ties artifact), far above any α. The
dip is therefore **rejected for cause** — not because another statistic gave a
nicer number — and replaced by a **control-calibrated** test. This is a
principled correction, recorded here as a named amendment so the freeze is
self-documenting.

Frozen significance test (criterion i): a **paired sign-flip permutation** on the
per-seed difference `d_s = sep_BH(s) − sep_MINK(s)`, where `sep` is the 2-means
separation of O and BH/MINK share one identical point cloud per seed (the
strongest box-match, `dev/prototype_o.py:404-409`), so `d_s` is exchangeable
under the no-horizon null. The null enumerates all `2^n` sign flips (exact for
n ≤ 20); PASS iff `p_perm ≤ 1e-4`. This is exact, tie-robust, and has no
divide-by-tiny failure mode (it supersedes the rejected "z ≥ 5/5σ" denominator,
`[cmte CRITICAL]`).

## Frozen protocol constants

| Item | Frozen value | Anchor |
|---|---|---|
| Geometry | tall box: `t_edge=6.0, r_edge=1.2, r_center=0.7`, EF metric, area=7.2 | `PHASE0_NOTES.md:41`; r∈[0.1,1.3] spans r_S |
| Hidden truth | `r_S = 2M = 0.5` (M=0.25), revealed only to score | `preregistration.md:33` |
| Cloud match | **same point cloud** per seed; BH & MINK differ only in causality | `prototype_o.py:404-409` |
| Boundary def | 1-D 2-means split threshold on integer O; classify `O < thr`. thr is a half-integer midpoint ⇒ exact ties impossible, no tie rule `[cmte M1]` | `sweep_o.py:71-88` |
| Blind statistic | `sep` = 2-means separation; pooled-SD floored at **0.5** (one O unit) `[cmte m2]` | `sweep_o.py:86` |
| Intensities (N levels) | `{1500, 3000, 6000, 12000}` | `PHASE0_NOTES.md:35` |
| Primary endpoint | N at intensity **12000** (single primary; other N + gap_ratio = context) `[cmte m1]` | — |
| Ensemble | **20 seeds**/level; level inconclusive if < 18 valid `[cmte m3]` | user decision |
| DEV_SEEDS | `20240617,13,101,7,42,99,2718,31415` | `sweep_o2.py:27` |
| Validation seeds | `11,23,57,88,137,271,314,577,911,1618,2024,4099,5040,6700,7777,8191,9001,12289,27644,65537` (disjoint, asserted in code) | `preregistration.md:66` |
| θ_sig (i) | paired sign-flip permutation, `p_perm ≤ 1e-4` | Amendment A1 |
| θ_fp (iv) | leave-one-out: MINK seed positive iff `sep` > 95th pctile of held-out MINK null; flagged fraction ≤ **0.05**. One control calibration **with** (i), not independent `[cmte C2]` | `preregistration.md:54` |
| θ_loc (ii) | median over seeds of bracket width `|dr|/(2M)` ≤ `2·ℓ_λ/(2M)`, **ℓ_λ from the frozen intensity & fixed area, never realized N** `[cmte C2]`; inconclusive if per-seed IQR > θ_loc `[cmte M3]`; coverage ≥ 0.5 | `preregistration.md:50` |
| θ_stab (iii) | std of blind boundary r-location across seeds ≤ `2·ℓ_λ` | `preregistration.md:53` |
| Guard-v (v) | `verify_order_only` RAISES on any causet whose O is not relabel-invariant; run on every causet | `prototype_o.py:325` |

Frozen numeric table (ℓ_λ = (λ/7.2)^(−½)):

| intensity λ | ℓ_λ | θ_loc = 2ℓ/(2M) | θ_stab = 2ℓ |
|---|---|---|---|
| 1500 | 0.0693 | 0.2771 | 0.1386 |
| 3000 | 0.0490 | 0.1960 | 0.0980 |
| 6000 | 0.0346 | 0.1386 | 0.0693 |
| 12000 | 0.0245 | 0.0980 | 0.0490 |

## Localisation metric — order-statistic bracket (criterion ii)

After the blind split (thr from O alone) the minimal elements split into a low-O
(interior-candidate) and high-O (exterior-candidate) class. Revealing r forms a
binning-free bracket `[r_lo, r_hi] = [max r over low-O, min r over high-O]`. A
clean split satisfies `r_lo ≤ r_S ≤ r_hi` (coverage) and the bracket **width**
`r_hi − r_lo` shrinks toward the discreteness floor ℓ as density grows;
misclassification (`r_lo > r_hi`) marks the seed impure. The frozen statistic is
the **median width / (2M)** over valid seeds (robust to per-seed scatter,
`[cmte M3]`), implemented in `nachocausal/scoring/scorer.py`.

## Convergence claim & criterion (reframed — `[cmte phys CRITICAL]`)

The committee (citing Eichhorn–Gamito–Stokes, in `biblioteca/`) showed that at
**fixed** t_edge the exterior "high" mode of O is limited by the box size, not by
the horizon. **The event horizon is global; this finite-box benchmark therefore
makes NO `r_h → 2M` asymptotic event-horizon claim.** The frozen claim is:

> the order-statistic bracket covers the hidden r_S and its width `|dr|/(2M)`
> contracts toward the discreteness floor ℓ as density ρ grows, while the
> box-matched flat control exhibits no such bimodal separation.

Frozen, decidable convergence rule (replaces the undecidable "monotone z within
noise", `[cmte M2]`): (a) median `|dr|/(2M)` at the primary N ≤ θ_loc; (b) the
4-N sequence is **non-increasing within one ℓ of slack** (`m_{k+1} ≤ m_k +
ℓ_k/(2M)`); (c) θ_sig permutation-significant at **every** N ≥ 3000 (value-at-N,
not a monotone-z slope). A pre-freeze dev check (exploration) that `dr/ℓ` is
invariant under t_edge 6.0 vs 8.0 guards against an edge artifact in the anchor.

## Frozen PASS/FAIL rule

PASS iff **ALL** at the primary N (intensity 12000): (i) `p_perm ≤ 1e-4` and
significant at every N≥3000; (ii) median `|dr|/(2M)` ≤ θ_loc, not IQR-inconclusive,
coverage ≥ 0.5, and convergence-slack (b) holds; (iii) boundary r-std ≤ θ_stab;
(iv) LOO false-positive fraction ≤ 0.05; (v) Guard-v raised on no causet. Any
unmet → FAIL; a primary level with < 18/20 valid seeds → INCONCLUSIVE. Unmet
*principled* thresholds are informative (possibly infeasible at that N), never a
licence to loosen (`preregistration.md:55-57`).

## Forbidden claims (unchanged)

Per `preregistration.md:69-72`: no event-horizon reconstruction, apparent-horizon,
Raychaudhuri, Kerr, manifoldlikeness, or thermodynamic claim. A 1+1D
recoverability benchmark of a known-truth horizon.

## Environment & seal provenance

- Sealed numeric environment: **numpy 1.26.4**, Python 3.12.3,
  Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-glibc2.39. `validate.py`/
  `dry_run.py` hard-fail on a different numpy (`thresholds.assert_environment`)
  `[cmte SWE CRITICAL-1]`.
- Accelerator admissibility: `past_matrix_fast == Minz` bit-for-bit, verified to
  N=10017 in commit **`1e61bec`** (`docs/reuse_check.md`); re-runnable via
  `make gate` (needs the Minz clone), evidence in
  `nachocausal/fixtures/gate_evidence.json`.
- Estimator non-drift: `make test` reproduces the 64 audited O multisets in
  `nachocausal/fixtures/o_samples.json` bit-for-bit `[cmte SWE MAJOR-1]`.
- **Seal: `nachocausal/thresholds.py` SHA256 =
  `ad02cb57e1445ca83a489bd4f3f9cae151517ca2aedbd1b29c44c60ac65f7faa`**
  (`make verify-seal`). The git commit that introduces this addendum + that
  thresholds.py is the freeze seal; step #5 (the blind validation run) begins
  only afterward.

## Independent pre-#5 audit (falsification gate, preregistration.md:74-78)

Before step #5, an independent adversarial auditor (separate session, blind to
any desired outcome, tasked to BREAK the instrument — find cheats, leakage,
hardcoding, or a verdict that cannot fail) audited the sealed package at commit
`34f3435` by **re-execution** (46 tool actions), not reading alone. Verdict:
**CLEAR-TO-PROCEED-TO-#5**; no CRITICAL/MAJOR/MINOR findings. Re-executed
evidence:

- **Order-only:** monkeypatching `estimate_O` to depend on a coordinate/label
  made `verify_order_only` RAISE; the scorer receives `thr` as an already-frozen
  float and never feeds back. No r_S/2M path into the observable.
- **Accelerator:** on a fresh seed (123456, not in any seed set/fixture)
  `past_matrix_fast == Minz` bit-for-bit (BH+MINK); the gate RAISES on a 1-bit
  poset corruption.
- **Thresholds:** θ_loc/θ_stab derive from intensity + fixed area, not realized
  N; the permutation p-value matches a brute-force 2ⁿ enumeration.
- **Falsifiable both ways:** forcing BH≡MINK → `p_perm=1.0` → FAIL; a genuine
  14-seed horizon signal → `p_perm=6.1e-5 ≤ 1e-4` → PASS-eligible.
- **Fixtures genuine:** 64/64 O-multisets regenerated from scratch, 0 mismatch;
  gate checksums reproduce.
- **No bypass:** no early read of validation data, no `if seed ==`, no r_S in any
  decision; validation seeds disjoint.
- **All seven guardrails fire** on the violating input built for each (Glue-3
  chi²=1197≫18.5, numpy pin, Minz gate, MIN_VALID_SEEDS→inconclusive, Guard-v).

Two NITs (non-blocking, confirmed not cheats): `validate.py` hardcodes the
`v_order_only` check True (sound — a Guard-v violation RAISES and aborts the run,
so it cannot be masked); `dry_run.py` temporarily lowers MIN_VALID_SEEDS for the
8-seed dev path only (restored in `finally`, never touches a threshold). Both
left as-is by decision. The independent-falsification gate is satisfied.
