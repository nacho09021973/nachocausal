# OP-2.2 BD-action viability dossier (V1–V4)

STATUS: DOCUMENTARY_ONLY / NO_EXECUTION / NOT_A_PREREGISTRATION
SCOPE: DRAFT_FOR_COMMITTEE_AND_PI_REVIEW
DATE: 2026-07-17
GOVERNING_DECISIONS: `docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md`
(candidate returned for revision), `docs/comite/comite_decision_036_pr009-pr010-sequencing-
adjudication.md` (sequencing amendment; does NOT enable this candidate by itself)

## 0. Purpose and rules of this document

Four binary viability gates for the Benincasa–Dowker 2D action as a potential OP-2.2 development
witness, per the PI's instruction of 2026-07-17. This dossier runs no code, draws no seed, opens
no PR013, and freezes nothing — it is the documentary precondition check that decides whether a
Route-B preregistration is even worth drafting. Every hand computation below is flagged for
independent verification before anything is frozen (author ≠ sole verifier, per decision 035 §5).

Gate logic (PI, 2026-07-17):

- If **V2 fails** → close the candidate without executing anything.
- If **V1–V3 pass but V4 fails** → the candidate may only be proposed with ceiling terminal
  `REFERENCE_WITNESS_SEPARATION_ONLY`; the words "proxy de horizonte" and "localizador" are
  forbidden for it under any outcome (`docs/plan_operativo_15_julio_2026.md:356`,
  `docs/claim_grammar.md:336`).
- If **V4 passes** → and only then, a Route-B preregistration with the exact kill test.

## V1 — Is the BD formula and its convention correctly fixed?

**Provisional answer: PASS (documentary), with one numeric field pending authorized enumeration.**

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

**Provisional answer: PASS at the global level, by hand-exhibited counterexample pair.
Support-restricted confirmation (V2b) pending the authorized enumeration.**

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

**What this does NOT yet establish (V2b, pending).** The bar's relevant domain is the **support
of the frozen PR011 laws** `P_4(0.95)`, `P_4(1.05)` — not all 4-element posets. Whether a
distinguishing pair lies inside that support, and whether `S` restricted to that support collapses
to a function of `|relations|`, is exactly the read-only enumeration already specified as the
falsifier's minimal test in decision 035 §5/§9 (`build_diamond_family → poset_law_from_grid`;
compute `(|relations|, S)` per support poset). That run is execution: it requires separate PI
authorization and must be performed/verified by someone other than this dossier's author. If
enumeration shows support-restricted collapse → **close the candidate without further
computation** (PI gate rule).

## V3 — Computable within the pipeline and budget?

**Provisional answer: CONDITIONAL PASS.**

- **Computability:** `N` and every `N_m` are order-isomorphism invariants, polynomial-time on the
  relation matrix; the PR011 poset laws are already produced by the frozen dev path
  (`dev/pr011_tv_certification_enumeration.py`), read-only. At n=4 the family is **exactly
  enumerable**, so the exact witness gap `|E_P f − E_Q f|` and exact TV are computable without
  Monte Carlo. Trivial budget. No new seed band is needed for the enumeration itself (no RNG).
- **The statistical caveat that must be resolved before any kill-test threshold is named**
  (decision 035 falsifier, failure mode 2): the PR011 family's certified near-blind regime bounds
  TV ≤ ~0.0092, hence any `[0,1]` witness gap ≤ ~0.0092. If a Monte Carlo/Hoeffding certificate
  is insisted on (as WP5 certifier rehearsal), resolving a gap `g` requires
  `2·sqrt(ln(4/α)/(2m)) < g`; even in the best case `g = 0.0092` with `α = 0.05` this gives
  `m ≳ 1.0e5` per stream per cell `[derived this session — re-derive against the actual
  enumerated gap before freezing anything]`. The actual gap may be far smaller, potentially
  making the MC route infeasible. **The exact-enumeration route at n=4 avoids this entirely**;
  the MC route is optional WP5 rehearsal and must be justified as such, with its `(m, α)`
  feasibility shown against the enumerated gap (V3b, same authorized run as V1b/V2b).

## V4 — Does a mass-versus-shape control exist that can falsify the horizon interpretation?

**Provisional answer: FAIL-structural for the horizon-fidelity question, within the PR011 family
as parametrized. An algebraic control exists for the weaker question. Consequence: ceiling
`REFERENCE_WITNESS_SEPARATION_ONLY`.**

Two candidate controls were identified in decision 035:

1. **Algebraic control (constructible now).** At fixed n=4, `N` is constant, so the control
   reduces to conditioning on `|relations|`: compare the conditional laws of `S` given
   `|relations| = k` between τ=0.95 and τ=1.05. If the conditional (residual) TV contribution is
   zero, the witness separates only through relation count — mass/cardinality-only — and dies as
   an independent witness. This is definable before scoring (pure algebra on the frozen linear
   form) and demonstrably can fail. **But it falsifies only "is it `f_bench` in disguise" — it
   cannot certify or falsify horizon-relevance.**
2. **Geometric control (exterior-only vs horizon-straddling patches) — NOT constructible in this
   family.** Decision 035's falsifier (ground-truth-leakage channel i) already established that
   the PR011 family is parametrized only by `(R, V, τ)` — abstract copula/diamond-family laws
   with **no embedding, no `r=2M`, no patch placement**. There is no horizon object inside the
   family for a control to vary. Importing Schwarzschild coordinate/geometry data to build one
   would put embedding information into a dev promotion decision, which op13 §4 forbids
   (`FAILED_DEVELOPMENT_PROVENANCE` / leakage).

**Finding.** Within PR011-as-parametrized, no control can separate "detects horizon-relevant
structure" from "detects mass/global-curvature," because the family contains no horizon structure
to begin with. This is the PI's anticipated negative branch: *the current 1+1D family cannot
validate horizon fidelity* — itself a useful, documentable result. It does not kill the
candidate; it caps it:

- Maximum admissible framing: **separation witness / null-check baseline**, ceiling terminal
  `REFERENCE_WITNESS_SEPARATION_ONLY`.
- Forbidden framings: "proxy de horizonte," "localizador," any horizon-fidelity claim
  (`plan:356`, `claim_grammar.md:336`, decision 035 §8 point 6).
- A genuine V4-pass would require a **different, horizon-bearing family** (embedded Schwarzschild
  patches with controlled placement relative to `r=2M`) — a larger, separate step outside this
  dossier's scope, with its own WP5-gate justification.

## Summary and proposed disposition

| Gate | Provisional outcome | Pending |
| --- | --- | --- |
| V1 | PASS (formula + convention fixed on paper) | V1b: numeric `[S_min,S_max]` from authorized enumeration |
| V2 | PASS-global (diamond vs Y: `|rel|=5`, `S=-6` vs `+6`) | V2b: support-restricted check, independent verifier |
| V3 | CONDITIONAL PASS (exact route trivial) | V3b: MC `(m,α)` feasibility vs actual enumerated gap, if MC route kept |
| V4 | **FAIL-structural** for horizon fidelity in PR011; algebraic control available for the weaker question | — (a horizon-bearing family would be a separate, larger step) |

**Proposed disposition (for committee + PI, not self-executing):** per the PI's gate logic, the
candidate is eligible to be proposed for a Route-B preregistration **only** as a
`SEPARATION_ONLY`-capped separation witness / null-check baseline, and only after the single
authorized read-only enumeration run discharges V1b/V2b/V3b (one run answers all three). If V2b
shows support-restricted collapse onto `|relations|`, the candidate closes without execution of
anything further. Nothing in this dossier opens OP-2.2, drafts a preregistration, or authorizes
the enumeration run — each remains a separate, explicitly authorized step (decisions 035 §9,
036 §9).

**Hand-computation verification obligations before any freeze:** the P1/P2 interval counts and
`S` values (V2), the chain/antichain sanity values (V1), and the `m ≳ 1.0e5` Hoeffding estimate
(V3) were derived by this dossier's author in one session and must be independently re-derived
(committee role, `/auditor`, or the authorized enumeration itself) before being relied on.
