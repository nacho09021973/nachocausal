# Auditor Report 030 — wp4-ibar-direct-score-derivation-revised-precommit

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/ignac/nachocausal`, branch `main`, `HEAD=ba6f747779ae4d12114bc15f19dcdac27a56636d`
(clean at HEAD; working-tree changes are the two untracked files below).

**Target:** `research_program/work_packages/wp4_ibar_direct_score_derivation.md` (`??` in
`git status`, UNCOMMITTED) — the **revised** version, after a fix pass addressing all six `WARN`
findings of `docs/auditor/auditor_report_029_wp4-ibar-direct-score-derivation-precommit.md`.

**Report 029 is itself uncommitted (`??`)** and referred to a now-superseded draft of the target
document. Per the PI's instruction, it is **not treated as a registered audit** and is not
referenced as authoritative history — this report re-derives and re-checks everything from
scratch against the current file, treating this as a fresh precommit audit. (Report 029 remains on
disk as a record of the prior iteration's findings; whether to keep, discard, or fold it into this
one is the PI's call, not this audit's.)

**Trigger:** re-audit after a revision pass, with an explicit bar set by the PI: **0 errors and,
reasonably, 0 warnings** — the six prior warnings were judged local, textual, and cheap to close,
not externally-imposed or inevitable, so `AUDIT_PASS_WITH_WARNINGS` was explicitly rejected as a
basis for commit.

**Hard scope restrictions honored** (identical to report 029): documentary/mathematical audit
only; no execution against the sealed pipeline; no pointwise scientific evaluation of `I(tau)` or
`Ibar`; no quadrature; the closed Hellinger contract
(`wp4_ibar_interval_executable_contract.md`, terminal `NUMERICAL_NONCONVERGENCE`, commit
`ba6f747`) was not touched, re-run, or reopened. Independent re-derivation used `sympy` (exact
symbolic algebra) and `numpy` (numerical verification of inequality chains over dense grids) as
auxiliary tools only, never to compute a scientific value of `I(tau)` or `Ibar`.

## 2. Mechanical audit

Verbatim output of `bash .claude/skills/auditor/audit.sh` (exit code 0):

```
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: [same long list of
docs/auditor, docs/comite, docs/hoja_de_ruta_*, docs/prereg* files as in report 029 — unchanged]
WARN: committed data file with no generator reference: data/reports/kbeam_braiding_diagnostic_per_survivor.csv
WARN: committed data file with no generator reference: data/reports/pr004_braiding_v2_per_lineage.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K16.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K2.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K32.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K4.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K64.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K8.csv
WARN: committed data file with no generator reference: data/reports/pr005_population_depth_barrier_slices.csv
WARN: committed data file with no generator reference: data/reports/pr005_population_depth_barrier_slices_heldout.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n4.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n4.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n5.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n5.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n6.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n6.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n7.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n7.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n8.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n8.sha256
WARN: committed data file with no generator reference: data/reports/present_anchor_clean_v3_kill_test.csv
WARN: committed data file with no generator reference: data/reports/present_anchor_sanity_pilot.csv
WARN: committed data file with no generator reference: evidence/new_geometry_20260719/mink_control_metrics.csv
----------------------------------------
Auditor: 0 error(s), 23 warning(s)
```

All 23 warnings are pre-existing, repo-wide, unrelated to the audited document (no code, no data
file, no seal-adjacent artifact was touched by this revision). Not attributable to this change;
not counted in this document's own verdict (§7).

## 3. Seal & freeze integrity

Not applicable — no code, no numerics, no threshold touched. `nachocausal/thresholds.py` untouched;
live seal `6e2c3888…` unaffected. `IBAR_DIAMOND_INTERVAL` and `CONSTANT_LEVEL_DEFEATER` are still
repeated verbatim, unchanged, at the top of the document (`wp4_ibar_direct_score_derivation.md:18-19`).
OK.

## 4. Reproducibility of published numbers

No numeric scientific result is published (no `I(tau)`, `Ibar`, `kappa`, or score value). Every
quantitative statement is a closed-form identity or an elementary inequality, independently
re-verified below. OK, not applicable in the usual sense.

## 5. dev/validation separation & ground-truth leakage

No sprinkling, no seed, no sealed-estimator path, no hidden embedding. The object (`c_tau`) is
unchanged from the closed contract; only the estimator is being re-derived. No leakage path. OK.

## 6. Claim-boundary check

Scope confined to 1+1D EF-diamond Fisher-information machinery for the Anexo C constant-efficiency
defeater. §12 (unchanged by this revision) explicitly withholds
`IMPLEMENTATION_AUTHORIZATION`/`EXECUTION_AUTHORIZATION` and scopes relevance away from 3+1D. OK.

## 7. Findings — verification of the six fixes, plus full re-confirmation of everything else

### 7.1 Fix 1 — two-step monotonicity in Lemma 2.4 (§2, lines 100–131)

Independently re-derived, not merely re-read: **Step 1** (`partial_U r|_{tau,v} =
-exp(v/2tau)/W'(tau,r) < 0` for all `r>0`, since both factors are positive) establishes that, at
any fixed `v`, `r` is strictly decreasing in `U` — this holds identically at *every* `v`, which is
the fact the composition argument below needs. **Step 2** turns on the sign identity
`Utilde>0 <=> W(tau,r)<0 <=> r<tau`, which holds *for every `v`* because the factor
`exp(-v/(2tau))` multiplying `W` in `Utilde` is strictly positive and therefore never flips the
sign comparison — I re-verified this factorization directly from the definition
`Utilde=-exp(-v/2tau)*W(tau,r)`. Consequently the sign of `partial_v r = (r-tau)/(2r)` is constant
along each *entire* vertical edge `U=Up(tau)` or `U=Uq(tau)` (not just at one point on it), which
is exactly what licenses "the minimum along this edge is at one specific endpoint" rather than
requiring a case-by-case check at every `v`.

The composition step — global min = (min-over-`U`, valid at any `v`, by Step 1) composed with
(min-over-`v` on that specific edge, by Step 2) — is a standard and valid iterated-extremum
argument (minimizing over one variable first, uniformly in the other, then minimizing the
resulting one-variable function): since Step 1's conclusion holds *for every* `v`, minimizing over
`U` first and then over `v` on the resulting edge is licensed and gives the true 2D global minimum;
the same holds for the maximum on the other edge. I verified this composition is not merely
asserted but structurally sound — no combination of interior points or the other two edges
(`v=v_p`, `v=v_q` at non-extremal `U`) can beat these two corners, because Step 1 already pins the
`U`-extremum (for *every* `v`, so in particular whichever `v` would be picked next) to one of the
two edges. **[PROVED]** — this closes the gap named in report 029 finding #3; the argument is now
complete and independently reproducible without reconstruction by the reader.

### 7.2 Fix 2 — generous `r_max<3.2` bound replacing the fragile `r_max<3.1` bound (§2, lines 133–152)

Independently re-verified every link of the chain numerically (`numpy`, 20001-point grid over
`tau in [1.0,1.2]`) and algebraically:

- `(3.2-tau)/(3-tau) > 1` for all `tau<3`: confirmed trivially true over the full grid (numerator
  exceeds denominator by exactly `0.2>0` since both share the same `-tau`), needing no numerical
  coincidence.
- `exp(0.2/tau) >= exp(0.2/1.2) = exp(1/6)`: confirmed — `0.2/tau` is manifestly decreasing in
  `tau`, minimized at the right endpoint `tau=1.2`; numerically `min = 1.181360...`, exactly
  `exp(1/6)`.
- `exp(1/6) > exp(1/100)`: this reduces to the purely rational comparison `1/6 > 1/100`, true by
  inspection — **no decimal/floating-point computation is load-bearing here**, unlike the old
  chain's tightest link.
- `exp(dv/(2tau)) <= exp(0.01)` for `tau>=1`: confirmed, `dv/(2tau)=0.01/tau<=0.01`.

Chaining these: `min(lhs) = 1.312623` (at `tau=1.0`) versus `max(rhs) = 1.010050` (at `tau=1.0`) —
**margin `0.302573`**, roughly 2200× the old chain's margin of `~1.37e-4` (previously
`1.010101` vs `1.010050`). Every intermediate inequality now holds with a wide, structural margin
rather than a tight decimal coincidence. **[PROVED]**, and now robust: the chain would survive
small perturbations of `r_p`, `dv`, or the `tau`-interval that the old `3.1` chain would not have.

Checked for consistency: `grep -n "3\.1\|3\.2"` across the full document shows every live use of
the bound is now `3.2` (§2 lines 138/146/151, §9 lines 400/402/463); the only remaining `3.1`
occurrences (lines 134, 148) are explicit, correctly-worded historical comparisons ("se usa `3.2`,
no el óptimo `3.1`"; "no ~0.005% como con la cota anterior de `3.1`") — not stray leftovers.
**OK, no inconsistency found.**

### 7.3 Fix 3 — compactness proof for `f1, f2` bounded away from zero (§9(b), lines 412–432)

Independently re-checked the four-step argument against the standard theorem it invokes
(a continuous, strictly positive function on a compact set attains a strictly positive minimum):

1. Continuity of `f1(tau,w)` — integral of a continuous integrand (established via §9(a)'s own
   compactness argument for `htilde`) over an interval of *fixed* length `v_q-v_p` — standard,
   correct.
2. Strict positivity of `htilde` everywhere on `K` — re-verified directly from its formula
   (`exp(v/2tau)/W'(tau,r)*DeltaU(tau)`, a product/quotient of a positive exponential, `W'>0` for
   `r>0`, and `DeltaU>0` by Lemma 2.2 — no subtraction anywhere that could produce a sign change or
   a zero) — correct, and correctly used to argue `f1>0` cannot arise from cancellation (there is
   none to cancel).
3. Compactness of the closed domain `(tau,w) in [1.0,1.2]x[0,1]`, explicitly **including the
   endpoints `w=0,1`** — correctly identified as the same as the unit-square boundary `x=0,1` after
   the rank identification of §4, and explicitly *not* excluded.
4. The compactness conclusion itself (continuous + strictly positive + compact ⟹ positive minimum)
   is the correct, standard extreme-value-theorem argument, correctly applied.

This is precisely the missing step report 029 flagged (bounded `r` alone does not suffice; the
compactness-over-the-closed-domain step is what actually closes the gap), and it is now present,
complete, and correct. **[PROVED]** — no hand-waving remains; the conclusion (already independently
confirmed correct in report 029) now has a justification in the document itself that matches it.

### 7.4 Fix 4 — explicit `a1, a2` boundedness corollary (§9(b′), lines 434–445)

Re-verified the corollary's logic: `a1(w)=-partial_tau F1(w)/f1(w)`. The numerator
`partial_tau F1(w) = integral_0^w f1(w')(E[D|w']-E[D])dw'` is an integral, over an interval of
length `<=1`, of an integrand that is a bounded quantity (`f1` bounded above by §9(b)'s `M_1`;
`E[D|w'], E[D]` are averages of `D`, itself bounded — `D` is a continuous elementary function
(§4's formula) of quantities all shown bounded in §9(a)/(b): `1/tau`, `v/(2r^2)`,
`(1/r+1/tau)*exp(v/2tau)/W'`, `beta_tau(w)` [a continuous function of `tau` on the compact
interval `[1.0,1.2]`, hence bounded by the ordinary continuous-function-on-compact-set fact — a
weaker claim than §9(a)'s strict-positivity argument, and correctly not over-elaborated], and
`DeltaU'/DeltaU` [bounded since `DeltaU` is bounded away from zero by the same compactness
argument as §9(b), applied to Lemma 2.2's straddle]) — hence `partial_tau F1(w)` is uniformly
bounded by some `C_1<infty`. Dividing by `f1(w)>=m_1>0` (§9(b)) gives `|a1(w)|<=C_1/m_1<infty`
**uniformly over the closed interval `w in [0,1]`, including the endpoints** — because the bound
on `f1` from (b) already holds at the endpoints, not just the interior. Symmetric argument for
`a2(v)`. **[PROVED]** — this is exactly the corollary report 029 asked to see spelled out (finding
#11), and the logic given is sound and complete, correctly including the boundary case.

### 7.5 Fix 5 — clarification that `Q1, Q2` are used only definitionally (§6, lines 284–291)

Re-verified against the actual computable formulas of §6–§7 (unchanged by this revision): `a1(w)`
is computed from `partial_tau F1(w)` and `f1(w)`, both forward quantities (§5); the final
`I(tau) = integral integral_Omega f(w,v)*sigma(w,v)^2 dw dv` (§7) integrates over `(w,v) in Omega`
directly, never over `(x,y)` and never requiring an evaluation of `Q1(x)` or `Q2(y)` for any
concrete `x,y`. Confirmed: no `F1^{-1}`/`F2^{-1}` evaluation appears anywhere in the computational
path. The new sentence accurately describes this. **[PROVED]**, resolves report 029 finding #14.

### 7.6 Fix 6 — the §6→§8 bridging paragraph (§8, lines 343–368)

This is the most delicate of the six and was re-derived from first principles, independently of
the document's own wording, exactly as report 029 attempted and found did not trivially close via
term-by-term substitution.

**(a) The chain-rule identity itself.** `d/dtau[g(tau,w(tau,x),v(tau,y))] = partial_tau g|_{w,v} +
(dw/dtau)*partial_w g + (dv/dtau)*partial_v g` is the ordinary multivariable total-derivative
decomposition of a composition of one outer variable (`tau`) through two inner variables
(`w(tau,x)`, `v(tau,y)`) that each also depend on `tau`. This is elementary calculus with no room
for a missing or misattributed term: exactly one term for the direct dependence and exactly one
term per intermediate variable's own rate of change, matching `dw/dtau|_x = a1(w)`,
`dv/dtau|_y = a2(v)` by §6's own definitions of `a1, a2` as those very derivatives. **[PROVED]**,
no error.

**(b) The logical inference.** `s_tau(x,y)`, defined as `partial_tau log c_tau(x,y)` at literally
fixed `(x,y)`, is — by the identification `log c_tau(x,y) = g(tau, w(tau,x), v(tau,y))` (a
tautology of the copula-density formula under the rank correspondence) — *identical to*, not merely
approximated by, the total derivative of (a). This is the crux: `sigma(w,v)` is not a candidate
expression being checked against an independently-defined "true score"; it is a direct computation,
via the chain rule, of the one and only quantity `s_tau(x,y)` means. Given that identity, the
general copula fact (`E[s_tau|x]=0` for all `x`, following purely from marginal uniformity of any
copula's density, a fact that holds regardless of which formula is used to write down `s_tau`)
transfers to `sigma` immediately upon the measure-preserving substitution `x=F1(w)`. **[PROVED]** —
the inference is valid; I found no step that assumes what it needs to prove.

**(c) Honesty of the argument, not a restatement of the same gap.** I attempted, independently and
before reading the document's own account, the term-by-term route (averaging the explicit
`D-E[D|w]-E[D|v]+E[D]+a1*(...)+ a2*(...)` formula over `v` at fixed `w`) and found — as the
document's own paragraph explicitly states — a residual (`E[D]-E[E[D|v]|w]` against
`E[a2(v)*partial_v g|w]`) whose mutual cancellation is not manifest by inspection of the summands.
The document's added paragraph does not paper over this; it names the residual explicitly and
states plainly that the direct route does not close, then supplies the actual, different, valid
route (the chain-rule identity of (a)–(b)) as the reason the direct route is unnecessary. This is
a materially different, and complete, argument — not the same gap in fancier language.
**[PROVED]** — this fully resolves report 029 finding #9. The identity `E[s|w]=E[s|v]=0` is now
proved in the document, with an honest account of why the tempting alternative route does not
work.

### 7.7 Re-confirmation: everything previously verified in report 029 remains correct and untouched

- The ten closed-form point identities of §2–§3 (`Wp`, `partial_tau W`, `partial_v r`,
  `partial_tau r`, `partial_v log h`, `partial_tau log h`, `partial_U log h`, mixed derivative,
  corner identity) are unchanged text; re-spot-checked against the document as currently written —
  identical to the version independently re-derived and confirmed in report 029. **[PROVED]**.
- `beta_tau(w)` bookkeeping in §4 and its propagation into §6 (`D(w,v)`, `E[D|w]`, `E[D|v]`,
  `E[D]`, `a1`, `a2`) — unchanged text (lines 232–277, 293–312 identical to the pre-revision
  version). **[PROVED]**, no regression.
- `A'(tau)/A(tau)` cancellation producing the doubly-centered score formula (§6) — unchanged text
  (lines 298–312). **[PROVED]**, no regression.
- Absence of double-counting between `D(w,v)` and the `a1*partial_w g + a2*partial_v g` transport
  terms — unchanged; re-confirmed as the same exact chain-rule decomposition verified in report
  029 and again in §7.6(a) above.
- Jacobian-exact inversion-free integral of §7 (`c_tau(x,y)dx dy = f(w,v)dw dv` exactly, via
  `dx=f1 dw`, `dy=f2 dv`) — unchanged text (lines 320–332). **[PROVED]**, no regression.
- `dv`-scaling (§10): confirmed **unchanged** by this revision (byte-for-byte identical to the
  pre-revision version, lines 472–514) — still explicitly labeled "Esbozo estructural (no probado
  aquí; obligaciones listadas)" with `[UNVERIFIED]` obligations (a), (b) stated, not upgraded to a
  proof. **[PROVED]** as a documentary-hygiene claim: the revision did not smuggle in a promotion
  of this open item, exactly as instructed.
- `kappa_sep`/`kappa_loc` naming (§10) — unchanged, consistent. **[PROVED]**.
- The closed Hellinger contract, its terminal, and the two frozen states — untouched anywhere in
  the document (confirmed by re-reading §1 and §12, lines 9–31 and 530–546, unchanged). OK.

### 7.8 Search for new issues introduced by the revision itself

Checked specifically whether the new text in §9(a) (a new illustrative parenthetical bounding
`exp(v/(2tau))` numerically, `[exp(v_p/2*1.2), exp(v_q/2*1.0)]`, not present in the pre-revision
draft) is itself correct: substituting `v_p=0, tau=1.2` gives `exp(0)=1`; substituting
`v_q=0.02, tau=1.0` gives `exp(0.01)`; these are indeed the correct minimum and maximum of
`exp(v/(2tau))` over `v in [0,0.02]`, `tau in [1.0,1.2]` (the exponent `v/(2tau)` is maximized at
largest `v`/smallest `tau` and minimized at smallest `v`, any `tau`) — **numerically correct**, and
in any case not load-bearing for the boundedness conclusion, which rests on the general
compactness argument stated in the same sentence, not on this illustrative bracket. Not a defect.

No other new content was found to introduce a gap: the edits were confined to §2 (Lemma 2.4), §6
(one clarifying sentence), §8 (one bridging paragraph before (I1)), and §9 (Lemma 9.1(b),(b′)) —
matching exactly the six items the PI specified, with no incidental changes elsewhere.

### 7.9 Findings table

| # | Severity | Finding | Anchor |
| --- | --- | --- | --- |
| 1 | OK | Two-step monotonicity argument for Lemma 2.4's corner-extremum identification is now complete, explicit, and independently re-verified as structurally sound (closes report 029 #3) | `wp4_ibar_direct_score_derivation.md` §2 (lines 100–131) |
| 2 | OK | `r_max<3.2` replaces the fragile `r_max<3.1` bound; every link re-verified with wide, non-coincidental margin (`0.30` vs. old `~1.4e-4`); all downstream references consistently updated (closes report 029 #4) | `wp4_ibar_direct_score_derivation.md` §2 (lines 133–152), §9 (lines 400, 402, 463) |
| 3 | OK | `f1, f2` bounded away from zero now has a complete, correct four-step compactness proof (continuity, strict positivity/no-cancellation, closed-domain compactness including endpoints, extreme-value theorem) — closes the exact gap the PI named (closes report 029 #10) | `wp4_ibar_direct_score_derivation.md` §9(b) (lines 412–432) |
| 4 | OK | Explicit, sound corollary derives uniform boundedness of `a1(w)`, `a2(v)` including at domain endpoints, with no boundary singularity (closes report 029 #11) | `wp4_ibar_direct_score_derivation.md` §9(b′) (lines 434–445) |
| 5 | OK | Clarifying sentence on `Q1, Q2` being definitional only, verified accurate against the actual (unchanged) computable formulas — no inversion hidden anywhere (closes report 029 #14) | `wp4_ibar_direct_score_derivation.md` §6 (lines 284–291) |
| 6 | OK | §6→§8 bridging paragraph independently re-derived and confirmed to give a complete, honest proof of `E[s\|w]=E[s\|v]=0` — explicitly names the residual that defeats the naive term-by-term route and supplies the correct alternative route instead of glossing over it (closes report 029 #9) | `wp4_ibar_direct_score_derivation.md` §8 (lines 343–368) |
| 7 | OK | All previously-verified material (10 point identities, `beta_tau` bookkeeping, `A'/A` cancellation, absence of double-counting, inversion-free Jacobian, `dv`-scaling correctly left `[UNVERIFIED]`, `kappa_sep`/`kappa_loc` naming) re-confirmed unchanged and correct; no regression from the edits | `wp4_ibar_direct_score_derivation.md` §2–§7, §10 |
| 8 | OK | New illustrative bound on `exp(v/2tau)` added incidentally in §9(a) checked and confirmed numerically correct; not load-bearing, no defect | `wp4_ibar_direct_score_derivation.md` §9(a) (lines 406–410) |
| 9 | OK | No new issues found anywhere else in the document; edits are confined to exactly the six requested locations | `wp4_ibar_direct_score_derivation.md` (whole file) |

AUDIT_ERRORS=0
AUDIT_WARNINGS=0

## 8. Verdict

**The PI's bar is met: 0 errors and 0 warnings of the auditor's own.** All six warnings from the
prior iteration were independently re-derived from scratch (not merely re-read against the
document's own claim of having fixed them) and each is now genuinely, substantively closed: the
two-step monotonicity argument for Lemma 2.4 is complete; the `r_max<3.2` bound has real,
structural margin instead of a fragile decimal coincidence; the `f1,f2`-bounded-away-from-zero
claim now has the actual compactness proof the PI named as missing; the `a1,a2` boundedness
corollary is explicit and sound, including at domain endpoints; the `Q1,Q2` notation is clarified
without changing any formula; and the `E[s|w]=E[s|v]=0` identity now has a complete, honest
proof that explicitly names why the tempting direct route fails and supplies the correct one. No
new issues were introduced by the edits, which were confined exactly to the six requested
locations. Everything previously verified as correct (the ten closed-form identities, the
`beta_tau`, `A'/A`, no-double-counting, and inversion-free-integral results) remains unchanged and
correct, and the `dv`-scaling obligation of §10 remains honestly `[UNVERIFIED]`, not promoted.

This document is now, in this auditor's assessment, a self-contained and genuinely demonstrative
derivation for its stated scope (a replacement estimator for `I(tau)`'s constant-efficiency
defeater), with no outstanding documentary debt.

AUDIT_ERRORS=0
AUDIT_WARNINGS=0
AUDIT_VERDICT=AUDIT_PASS
