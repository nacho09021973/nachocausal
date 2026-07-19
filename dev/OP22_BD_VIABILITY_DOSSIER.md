# OP-2.2 BD-action viability dossier (V1–V4)

STATUS: DOCUMENTARY_ONLY / NO_EXECUTION / NOT_A_PREREGISTRATION
SCOPE: DRAFT_FOR_COMMITTEE_AND_PI_REVIEW
DATE: 2026-07-17 (rev. 2, same day: gate semantics tightened per PI instruction — V2
UNRESOLVED branch without execution, V3 exact frozen-formula budget, V4 split into
`ALGEBRAIC_NONREDUNDANCY` vs `HORIZON_FIDELITY`, no OP-2.2 terminal emitted); 2026-07-19 (rev. 3:
corrections from `docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md` —
E1 fixed (V3 budget table re-anchored to the n=4 certified ceiling `ε=0.004611899229`, dropping
the mis-anchored rounded n=8 value; nominal-TV realistic scale added), W1 fixed (V3 headline now
states no compute cap exists), W2 fixed (V4b premise corrected to the frozen generator's actual
hard-frozen horizon locus/placement; FAIL-structural conclusion unchanged and strengthened). No
gate verdict, disposition, or OP-2.2 terminal changed by rev. 3; V1/V2/V4a stand as in rev. 2.
GOVERNING_DECISIONS: `docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md`
(candidate returned for revision), `docs/comite/comite_decision_036_pr009-pr010-sequencing-
adjudication.md` (sequencing amendment; does NOT enable this candidate by itself)

## 0. Purpose and rules of this document

Four binary viability gates for the Benincasa–Dowker 2D action as a potential OP-2.2 development
witness, per the PI's instruction of 2026-07-17. This dossier runs no code, draws no seed, opens
no PR013, and freezes nothing — it is the documentary precondition check that decides whether a
Route-B preregistration is even worth drafting. Every hand computation below is flagged for
independent verification before anything is frozen (author ≠ sole verifier, per decision 035 §5).

Gate logic (PI, 2026-07-17, second instruction — supersedes the first pass where stricter):

- **V1** is `PASS` only with the exact formula and the exact normalization convention; nothing
  less counts.
- **V2** is `PASS` only on an **analytic proof of non-equivalence**. If no analytic proof is
  available at the required level, the verdict is `UNRESOLVED` — the enumerative test is **not
  executed** to settle it. If V2 resolves to fail → close the candidate without executing
  anything.
- **V3** must state the **exact** `(m, α)` budget from the frozen radius formula, including
  multiplicity; the PI's 1/√m scaling estimate is a sanity check, never a result.
- **V4** must separate `ALGEBRAIC_NONREDUNDANCY` from `HORIZON_FIDELITY` explicitly. If the
  horizon-fidelity contrast is not constructible in PR011 → the candidate may at most be
  recommended with ceiling terminal `REFERENCE_WITNESS_SEPARATION_ONLY`; the words "proxy de
  horizonte" and "localizador" are forbidden for it under any outcome
  (`docs/plan_operativo_15_julio_2026.md:356`, `docs/claim_grammar.md:336`).
- If **V4 passes** → and only then, a Route-B preregistration with the exact kill test.
- **This dossier emits no OP-2.2 terminal of any kind.** Enumeration, Monte Carlo and scoring
  remain unexecuted and unauthorized by this document.

## V1 — Is the BD formula and its convention correctly fixed?

**Provisional answer: PASS (documentary), claimed strictly for the exact formula and the exact
normalization convention — nothing else.** The numeric endpoints `[S_min, S_max]` are a separate
field (V1b) that this PASS does not cover; it awaits the (not yet authorized) enumeration.

The formula that would be frozen — and the only formula entitled to the name Benincasa–Dowker in
D=2 (decision 035 §4 mathematician, §7 literature verdict, both anchored to the primary sources) —
is the four-term action:

```text
S(C) = N - 2*N1 + 4*N2 - 2*N3
```

- `N = N0 = |C|` (cardinality).
- `N_i` = number of **inclusive order intervals** `[x,y] = {z : x ⪯ z ⪯ y}` of cardinality
  `i+1`, one interval per related pair `x ≺ y`. (BD2010 Eq.13,
  `biblioteca/derived-md/Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md:117,
  123`; Bhatnagar Eq.3.11, `biblioteca/derived-md/Bhatnagar_2021...md:519,523`.)
- The coefficients `(1, -2, +4, -2)` are fixed by the 2D continuum limit and are not tunable.
  Any dimensionful prefactor (`ħ`, powers of the discreteness length) is dropped: it is an affine
  reparametrization absorbed by the [0,1] map below, and this must be stated in any frozen text.
- The decision-035 correction stands: a 3-term `N0,N1,N2` object is NOT this action and forfeits
  the bibliographic-provenance claim.

**[0,1] convention (no clipping).** At the frozen family's fixed `n`, the poset space is finite,
so `S` has an exact theoretical range `[S_min, S_max]` computable by enumeration before any
scoring. Freeze `x ↦ (S - S_min)/(S_max - S_min)`. Clipping is excluded: the range provably
bounds every attainable value, and empirical clipping would collapse the alternating-sum extremes
and distort the TV bound (decision 035 §4 mathematician, point 5).

**Pending (V1b):** the numeric `[S_min, S_max]` at n=4 requires the read-only enumeration —
execution, hence outside this dossier; it is the same authorized run as V2b/V3b below.

**Hand sanity checks (to be independently verified):**
- 4-chain `a≺b≺c≺d`: relations 6; `N1=3` (`[a,b],[b,c],[c,d]`), `N2=2` (`[a,c],[b,d]`),
  `N3=1` (`[a,d]`); `S = 4-6+8-2 = 4`. Matches decision 035 §4.
- 4-antichain: relations 0; `S = 4`.

## V2 — Can non-equivalence with `f_bench` be demonstrated?

**Provisional answer: PASS at the global level, by analytic (hand-exhibited) counterexample
pair. At the support-restricted level: `UNRESOLVED` — no analytic proof is in hand, and per the
PI's gate rule the enumerative test is NOT executed to settle it.**

`f_bench(poset) = |relations|/6` is permanently barred from seeding OP-2.2
(`dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md:130-131`). Decision 035 (logician, point 5)
requires *proving*, not asserting, that the BD scalar is not an affine/monotone reparametrization
of `|relations|` on the relevant domain. The cleanest form (PI, 2026-07-17): exhibit two posets
with the same `|relations|` but different `S`.

**Counterexample pair (n=4, hand-derived this session — requires independent re-derivation):**

*P1 — diamond.* Elements `{a,b,c,d}`; covers `a≺b, a≺c, b≺d, c≺d`; transitive closure adds
`a≺d`. Relations: `(a,b),(a,c),(a,d),(b,d),(c,d)` → `|relations| = 5`.
Intervals: `[a,b]={a,b}`, `[a,c]={a,c}`, `[b,d]={b,d}`, `[c,d]={c,d}` (cardinality 2 each, since
`b∥c`); `[a,d]={a,b,c,d}` (cardinality 4). So `N1=4, N2=0, N3=1`.

```text
S(P1) = 4 - 2*4 + 4*0 - 2*1 = -6
```

*P2 — Y-poset (two minimal elements).* Elements `{a,b,c,d}`; covers `a≺b, d≺b, b≺c`; transitive
closure adds `a≺c, d≺c`. Relations: `(a,b),(d,b),(b,c),(a,c),(d,c)` → `|relations| = 5`.
Intervals: `[a,b]={a,b}`, `[d,b]={d,b}`, `[b,c]={b,c}` (cardinality 2); `[a,c]={a,b,c}`,
`[d,c]={d,b,c}` (cardinality 3, `d∉[a,c]` since `a⊀d`, `a∉[d,c]` since `d⊀a`). So
`N1=3, N2=2, N3=0`.

```text
S(P2) = 4 - 2*3 + 4*2 - 2*0 = +6
```

Same `n=4`, same `|relations|=5`, different `S` (−6 vs +6). Therefore **`S` is not a function of
`|relations|` on the space of 4-element posets** — a fortiori not an affine or monotone
reparametrization of `f_bench`. Consistency check: `Σ_{m≥1} N_m = |relations|` holds for both
(P1: 4+0+1=5; P2: 3+2+0=5), confirming the identity of decision 035 §4 (mathematician, point 2).

**What this does NOT establish (V2b — typed `UNRESOLVED`, not "pending").** The bar's relevant
domain is the **support of the frozen PR011 laws** `P_4(0.95)`, `P_4(1.05)` — not all 4-element
posets. Whether a distinguishing pair lies inside that support, and whether `S` restricted to
that support collapses to a function of `|relations|`, has no analytic proof in this dossier. Per
the PI's gate semantics (2026-07-17, second instruction), the absence of an analytic proof makes
the support-restricted verdict `UNRESOLVED`; the read-only enumeration that would settle it
empirically (decision 035 §5/§9: `build_diamond_family → poset_law_from_grid`; compute
`(|relations|, S)` per support poset) is **deliberately not executed** — it is execution,
requires separate PI authorization, and must be performed/verified by someone other than this
dossier's author. If a later authorized run shows support-restricted collapse → **close the
candidate without further computation** (PI gate rule). An analytic proof route (e.g., showing
the counterexample pair P1/P2 both receive positive probability under the frozen copula grid, by
inspection of the frozen construction rather than by running it) is left open for the committee;
none is claimed here.

## V3 — Computable within the pipeline and budget?

**Provisional answer: CONDITIONAL PASS — calculable from the frozen formula, but not declarable
viable against any committed resource/compute cap, because no such cap exists anywhere in the
repo for OP-2.2 (the α-ledger budgets error probability, not compute; corrected per
`docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md` finding W1).**

- **Computability:** `N` and every `N_m` are order-isomorphism invariants, polynomial-time on the
  relation matrix; the PR011 poset laws are already produced by the frozen dev path
  (`dev/pr011_tv_certification_enumeration.py`), read-only. At n=4 the family is **exactly
  enumerable**, so the exact witness gap `|E_P f − E_Q f|` and exact TV are computable without
  Monte Carlo. Trivial budget. No new seed band is needed for the enumeration itself (no RNG).
- **`(m, α)` budget from the frozen formula** (decision 035 falsifier, failure mode 2; table
  re-anchored per auditor_report_019 finding E1). The frozen certificate (op13:59-76;
  `certifier/bench.py:97-98,120`) is
  `TV_lower = max(0, |mu_p − mu_q| − r_p − r_q − eps_p − eps_q)` with
  `r = sqrt(ln(4/α_j)/(2m))`. With `eps = 0` and `m_p = m_q = m`, `BOUND_POSITIVE` is attainable
  at the expected means only if `2·sqrt(ln(4/α_j)/(2m)) < g`, i.e.

  ```text
  m > 2·ln(4/α_j) / g²        (per stream, per cell)
  ```

  This candidate family is pinned at **n=4** throughout this dossier (V1, V2, V4, CELL-PR011).
  Its own committed certified ceiling is `ε ≤ 0.004611899229`
  (`data/reports/pr011_tv_certification_n4.csv`, `docs/plan_avanzado_14_julio_2026.md:51`) — this
  is the correct best-case bound on any `[0,1]` witness gap `g` for **this** family. The n=8
  ladder value `ε ≤ 0.009223798457` (loosely cited as "~0.0092" in decision 035,
  `comite_decision_035…md:385`) is a valid but *looser* family-wide bound only — ε grows with n by
  construction — and must not be substituted for the n=4-pinned family's own tighter ceiling.

  Evaluated at the n=4 ceiling `g = 0.004611899229` (best case for **this** family; the true
  enumerated gap can only be smaller, inflating `m` by the factor `(0.004611899229/g_true)²`):

  | α_j | m_min per stream |
  | --- | --- |
  | 0.05 | 412,046 |
  | 0.04 (CELL-PR011 allocation) | 433,029 |
  | 0.01 | 563,383 |

  **This is a best-case bound, not a realistic estimate.** The committed *nominal* TV at the
  exact CELL-PR011 parameters (n=4, `grid_m=12`) is `primary_tv_nominal =
  0.0014402226592060835` (same CSV, annotation field — nominal, not certified). If the true gap
  sits near that scale, `m_min ≈ 4.23e6 / 4.44e6 / 5.78e6` per stream — over an order of
  magnitude above the best-case table above, and the more realistic planning number for the MC
  route.

  **Multiplicity is included via the frozen α-ledger** (`sum α_j ≤ alpha_total`, OP-2.1 prereg
  §4.2, G4): with `K` cells splitting `alpha_total` equally, `α_j = alpha_total/K` and
  `m_min = 2·ln(4K/alpha_total)/g²` per stream per cell — logarithmic in `K`, so multiplicity
  adds ~10–40% here, not orders of magnitude. Total draws per cell are `2·m` (two streams).
  Caveat: this `m_min` is the *attainability* threshold (empirical means at their expectations),
  not a power guarantee; a preregistered run would need margin above it.
- **The PI's 1/√m scaling estimate is superseded and must not be cited as the budget.** Scaling
  CELL-PR011's rehearsal radius (`m = 200, α_j = 0.04` → `r = 0.1073 ≈ 0.11`) by the loose
  family-wide bound, `m ~ 200·(0.11/0.009223798457)² ≈ 2.8e4`, sets **one** radius equal to that
  bound; the frozen certificate needs `r_p + r_q < g` (each radius `< g/2`), which costs a
  further factor ≈ 4 on top of whichever gap is used — a formula-vs-heuristic discrepancy that
  holds independently of which bound (n=4 or n=8) is chosen. This is precisely why the frozen
  formula, not the scaling heuristic, is the budget (PI, 2026-07-17). The actual gap may be far
  smaller than either bound above, potentially making the MC route outright infeasible. **The
  exact-enumeration route at n=4 avoids all of this**; the MC route is optional WP5 rehearsal and
  must be justified as such, with its `(m, α_j)` feasibility re-evaluated against the actual
  enumerated gap (V3b, same authorized run as V1b).

## V4 — Does a mass-versus-shape control exist that can falsify the horizon interpretation?

**Provisional answer: the gate splits into two typed sub-gates that must never be conflated
(PI, 2026-07-17): `ALGEBRAIC_NONREDUNDANCY` — constructible, and `HORIZON_FIDELITY` —
FAIL-structural (not constructible) within the PR011 family as parametrized. Consequence:
ceiling `REFERENCE_WITNESS_SEPARATION_ONLY`, regardless of TV quality.**

**The physical distinction that governs this gate (PI, 2026-07-17, verbatim requirement):**
regressing (or conditioning) `S_BD` against `N` and `|relations|` can demonstrate that the BD
action contains something beyond size and ordering fraction — **but it does not demonstrate
horizon sensitivity.** That residual is a control of *algebraic redundancy*, not a
*mass-versus-shape* control. The two sub-gates are therefore:

1. **V4a — `ALGEBRAIC_NONREDUNDANCY` (constructible now).** At fixed n=4, `N` is constant, so
   the regression on `(N, |relations|)` degenerates to conditioning on `|relations|`: compare
   the conditional laws of `S` given `|relations| = k` between τ=0.95 and τ=1.05. If the
   conditional (residual) TV contribution is zero, the witness separates only through relation
   count — mass/cardinality-only — and dies as an independent witness. This is definable before
   scoring (pure algebra on the frozen linear form) and demonstrably can fail. **Its passing
   certifies only that `S` is not `f_bench` in disguise. It is silent — structurally, not merely
   in practice — on horizon relevance, and no wording in any later document may launder a V4a
   pass into a horizon claim.**
2. **V4b — `HORIZON_FIDELITY` (exterior-only vs horizon-straddling patches) — NOT constructible
   in this family.** **(Premise corrected per auditor_report_019 finding W2 — conclusion
   unchanged, and strengthened.)** The premise inherited verbatim from decision 035's falsifier
   (ground-truth-leakage channel i) — "no embedding, no `r=2M`, no patch placement recorded" — is
   imprecise at the generator level. The frozen builder is in fact EF-Schwarzschild-derived:
   `W(t,r) = e^{r/t}(r/t − 1)` vanishes at `r = t`, i.e. **`τ` plays the role of `2M`, and the
   horizon locus `r = τ` is present in the construction**
   (`research_program/work_packages/wp4_kappa_numeric_reference.py:56-57`); the patch corners
   are recorded as frozen constants `(r_p,v_p) = (2,0)`, `(r_q,v_q) = (0.5,1)`
   (`dev/pr011_tv_certification_enumeration.py:41-44`); and placement is not merely unrecorded
   but **hard-frozen to straddling** by
   `assert Up < 0 < Uq, "reference shape must straddle the horizon (Up<0<Uq)"`
   (`wp4_kappa_numeric_reference.py:74-75`). What is true, and load-bearing, is that none of this
   is exposed as a **family axis**: the poset laws the frozen builder outputs are abstract
   unlabeled posets, the only variable parameter across the family is `τ`, and an exterior-only
   (non-straddling) member is not expressible without modifying frozen code — the assert rejects
   it — or designing a new family. The exterior-versus-straddling contrast is therefore still
   **not constructible within PR011-as-frozen**, and the finding is if anything sharper than the
   original wording: the family does not merely omit a horizon object, it hard-forbids
   non-straddling members outright, and since the two candidate laws (τ=0.95, τ=1.05) differ
   exactly by moving the horizon locus inside a fixed patch, τ-separation is inseparable from
   mass/global-curvature response without placement variation. Importing Schwarzschild
   coordinate/geometry data to *vary placement* — the one axis the frozen family does not expose
   — would put embedding information into a dev promotion decision, which op13 §4 forbids
   (`FAILED_DEVELOPMENT_PROVENANCE` / leakage).

**Finding.** Because PR011 fixes the horizon locus (`r=τ`) and the patch placement as frozen
constants — rather than exposing either as a variable family axis, and in fact hard-forbidding
non-straddling members via its own assertion — the horizon-fidelity gate **cannot be passed
within this family — even if the resulting TV were excellent.** V4a and V4b answer different
questions; a strong V4a residual plus a strong TV certificate still sums to zero evidence of
horizon sensitivity. This is the PI's anticipated negative branch: *the current 1+1D family
cannot validate horizon fidelity* — itself a useful, documentable result. It does not kill the
candidate; it caps it:

- Maximum admissible framing: **separation witness / null-check baseline**, ceiling terminal
  `REFERENCE_WITNESS_SEPARATION_ONLY` — the cap holds even under an excellent TV result.
- Forbidden framings: "proxy de horizonte," "localizador," any horizon-fidelity claim
  (`plan:356`, `claim_grammar.md:336`, decision 035 §8 point 6).
- A genuine V4-pass would require a **different, horizon-bearing family** (embedded Schwarzschild
  patches with controlled placement relative to `r=2M`) — a larger, separate step outside this
  dossier's scope, with its own WP5-gate justification.

## Summary and proposed disposition

| Gate | Provisional outcome | Pending |
| --- | --- | --- |
| V1 | PASS, strictly for exact formula + exact normalization convention | V1b: numeric `[S_min,S_max]` from a (not yet authorized) enumeration |
| V2 | PASS-global by analytic counterexample (diamond vs Y: `|rel|=5`, `S=-6` vs `+6`); **support-restricted: `UNRESOLVED`** (no analytic proof; enumerative test deliberately not run) | analytic proof route, or a separately authorized enumeration with independent verifier |
| V3 | CONDITIONAL PASS — calculable, not declarable viable against any cap (none exists); `m > 2·ln(4/α_j)/g²` → 412,046–563,383 per stream at the n=4 certified ceiling `g=0.004611899229`; ≈4.23e6–5.78e6 at the nominal-TV scale | V3b: re-evaluate against actual enumerated gap, if MC route kept |
| V4 | Split verdict — V4a `ALGEBRAIC_NONREDUNDANCY`: constructible; V4b `HORIZON_FIDELITY`: **FAIL-structural** in PR011 (horizon locus and patch placement hard-frozen, not exposed as a family axis; non-straddling members forbidden by construction) | — (a horizon-bearing family would be a separate, larger step) |

**Proposed disposition (for committee + PI, not self-executing):** because V4b is not
constructible in PR011, the maximum recommendation this dossier can support is
`REFERENCE_WITNESS_SEPARATION_ONLY` — a `SEPARATION_ONLY`-capped separation witness / null-check
baseline, even in the best statistical case. Whether BD merits that small separation experiment,
or PR011 should instead be abandoned as a bench for horizon validation (while remaining valid
for exercising statistical machinery), turns on V2's support-restricted question — which stays
`UNRESOLVED` here by design. **No OP-2.2 terminal of any kind is emitted by this dossier.**
Nothing in it opens OP-2.2, drafts a preregistration, or authorizes enumeration, Monte Carlo or
scoring — each remains a separate, explicitly authorized step (decisions 035 §9, 036 §9); if a
later authorized run shows support-restricted collapse onto `|relations|`, the candidate closes
without further computation.

**Hand-computation verification obligations before any freeze:** the P1/P2 interval counts and
`S` values (V2), the chain/antichain sanity values (V1), and the budget arithmetic
(`radius(200, 0.04) = 0.1073`; `m_min = 412,046 / 433,029 / 563,383` at
`α_j = 0.05 / 0.04 / 0.01`, `g = 0.004611899229`, the n=4 certified ceiling) (V3) were derived by
this dossier's author and must be independently re-derived (committee role, `/auditor`, or the
authorized enumeration itself) before being relied on. The V3/V4b corrections in this revision
were independently re-derived against `data/reports/pr011_tv_certification_n4.csv` and
`research_program/work_packages/wp4_kappa_numeric_reference.py` by the agent applying
`docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md`'s findings — this still
counts as author-adjacent, not committee-independent, verification, and a further independent
check remains owed before this text is frozen.
