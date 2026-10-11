# Query on the light-cone-region estimate in Pfeiffer (2022), §3.3

**Date:** 2026-10-11
**Status:** `DRAFT_FOR_PI_REVIEW` — not sent
**Scope:** one step in one section of one thesis. Independent of any work of ours.

**Reference, verified against the source and the public record:**

> Christopher-Dustin Pfeiffer, *Higher curvature terms for Causal Sets. Extended proof and
> generalization for the Causal Set d'Alembertian*. Master thesis, Niels Bohr Institute,
> University of Copenhagen, submitted 20 May 2022. Supervisor: Emil Bjerrum-Bohr.
> Co-supervisor: Astrid Eichhorn.
> Public copy: `https://nbi.ku.dk/english/theses/masters-theses/christopher-dustin-pfeiffer/`
> Local sha256 (first 16): `39beffd1f8696be6`. No published version supersedes it.

---

## 0. What is and is not affected

**The published paper is not affected.** de Brito, Eichhorn & Pfeiffer, *Higher-order curvature
operators in causal set quantum gravity*, EPJ Plus **138**, 592 (2023) (arXiv:2301.13525), does
not reproduce this argument. It states that `I_d[phi](x)` is computed *"by following [55]"* —
Belenchia, Benincasa & Dowker, arXiv:1510.04656 — and cites `[55, 54, 56, 57]` only for a
detailed explanation of the steps, where `[57]` is the thesis. **BBD's estimate is sound** (see
§3 below), so the published result rests on a valid argument. Nothing here propagates to it.

What follows concerns §3.3 of the thesis, *The light cone region*, equations (3.15)–(3.22) and
their use in (3.27)–(3.32).

## 1. The question

We had to follow the `W2` estimate closely while auditing an unrelated operator. We believe the
chain (3.15)–(3.22) does not establish what (3.27)–(3.32) then use it for, and we would rather
ask than assume we have misread.

The question is narrow: **does `O_d`, a differential operator in `rho` with alternating
coefficients, preserve the supremum-norm bounds substituted in (3.18)–(3.22)?**

## 2. The step, as we read it

1. **(3.15)** moves `O_d` outside the integral under absolute values.
2. **(3.17)** records
   `| d/dx |f(x)| | = | sgn(f(x)) d/dx f(x) | = | d/dx f(x) |`.
   **This identity is correct** — all three expressions carry absolute values, and `sgn(f) = ±1`
   where `f != 0`. We are not disputing it. Our point is only that it concerns one derivative of
   an absolute value, and does not state that `|F| <= G` implies `|O_d F| <= |O_d G|`.
3. **(3.18)–(3.22)** pull `||sqrt(-g)||_inf` and `||phi||_inf` out in front, and `O_d` is applied
   to what remains **after** that replacement.
4. **(3.27)–(3.32)** then use the roots of `O_d`: the factor `A_{lambda,l}(n) = prod 2(j-l)`
   annihilates the result.

Our concern is at step 3. `A_{lambda,l}(n)` annihilates the *comparison function*, not the
original integrand. `O_d` has alternating coefficients, so it is not monotone: from `|F| <= G` it
does not follow that `|O_d F| <= |O_d G|`, nor that `O_d G = 0` forces `O_d F = 0`. The
annihilation looks like a property of the object substituted in, not of the object being
estimated.

If that is right, the conclusion that the cone region contributes at `O(rho^{-2/d})` does not
follow **from this argument**. We are not claiming the estimate is false.

## 3. Why boundedness alone seems insufficient

A functional example, not a geometric one. Take a positive bounded amplitude containing a term
`U^3 log U`, with phase `V = U^2 f_0`:

```
int U^3 log U e^{-rho f_0 U^2} dU = -log(rho)/(4 f_0^2 rho^2) + c/rho^2 + (exp. small)
```

The fourth root carries that logarithm to order `rho^{-1/2}`. This is **not** a smooth Ricci-flat
counterexample and we do not offer it as one — no such geometry is exhibited. It shows only that
hypotheses of mere boundedness cannot close the gap: an amplitude satisfying them produces a term
the estimate would have to exclude. Ruling it out appears to need regularity the argument does not
assume.

**BBD (arXiv:1510.04656) is unaffected by this.** Their eq. (25) bounds the *integrand* first by a
positive-coefficient kernel, and only then rewrites the already-bounded quantity using the
sign-reversed identity — a different operation, and a sound one. Their flat case is §II.B, the
curved one §III.B.

## 4. What we are not questioning

- BBD, as above.
- **Identity (3.28) on a monomial stands.** That `A_{lambda,l}(n)` annihilates the integral of a
  monomial is correct, and we verified it.
- Identity (3.17) itself, which is correct as printed.
- The rest of the thesis, which we did not audit.
- This is independent of the operator we were studying; it would read the same had we never
  looked at ours.

## 5. How this was checked

Three independent reviewers from different model families (`grok-4.6`, `deepseek-v4-pro`,
`gpt-6-astra`) were given the original text, not our summary, under blind conditions. All three
reached the same reading of (3.15)–(3.22) and located the step at the same place, each citing the
equations independently.

We record this because we do not think agreement is evidence by itself — in the same round, on a
different question, two of the three were wrong and the dissenting one was right. What we offer is
the argument, not the count. If (3.17) does license the exchange for a reason not written out, that
would settle it, and we would like to know.

---

## Notes for the PI (strip before sending)

- **Reference: resolved.** Title, author, institution, date and both supervisors confirmed against
  the NBI page and the thesis title page; the local PDF matches. No published version supersedes it.
- **Scope: resolved, and favourable.** The EPJ Plus paper leans on BBD, not on this chain, so the
  note does not impugn a published result. §0 says so explicitly — that is what makes this a
  low-stakes technical query rather than an erratum against the literature.
- **I corrected my own draft.** The earlier version stated (3.17) without its outer absolute
  values, which made a correct identity look false. Caught by rendering page 23 of the thesis
  rather than trusting `pdftotext`, which drops the outer bars.
- **Recipient is the open question.** Pfeiffer's current position is not determinable from public
  sources; the thesis is from 2022 and he may have left the field. The people with a live stake are
  the supervisors: Emil Bjerrum-Bohr (NBI Copenhagen) and Astrid Eichhorn (SDU Odense), who was
  both co-supervisor and co-author of the paper. Writing to all three is the natural route.
- `biblioteca/` is git-ignored; the PDFs and their sha256 are local only.
