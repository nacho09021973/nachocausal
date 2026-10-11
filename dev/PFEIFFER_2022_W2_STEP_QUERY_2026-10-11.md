# Query on steps (3.15)–(3.22) of Pfeiffer (2022)

**Date:** 2026-10-11
**Status:** `DRAFT_FOR_PI_REVIEW` — not sent
**Scope:** one step in one section. Independent of any work of ours.

---

## What this is

While auditing an unrelated operator we had to follow the cone-region (`W2`) estimate
in your thesis closely. We believe the chain (3.15)–(3.22) does not establish what
(3.27)–(3.32) then use it for, and we would rather ask than assume we have misread you.

The question is narrow: **does a differential operator in `rho` with alternating
coefficients preserve the sup-norm bounds substituted in (3.18)–(3.22)?** We think it
does not, and that identity (3.17) does not license the exchange.

## The step

As we read it:

1. **(3.15)** moves `O_d` outside the integral under absolute values.
2. **(3.17)** is `d|f|/dx = sgn(f) df/dx`. This is an identity for a *single*
   derivative of an absolute value. It does not state that `F <= G` implies
   `|O_d F| <= |O_d G|`.
3. **(3.18)–(3.22)** replace `sqrt(-g)` and `phi` by their supremum norms, and `O_d`
   is applied *after* that replacement.
4. **(3.27)–(3.32)** then use the roots of `O_d`: the factor
   `A_{lambda,l}(n) = prod 2(j - l)` annihilates the result.

Our concern is at (3). `A_{lambda,l}(n)` annihilates the *comparison function*, not the
original integrand. `O_d` has alternating coefficients, so it is not monotone: from
`|F| <= G` it does not follow that `|O_d F| <= |O_d G|`, nor that `O_d G = 0` forces
`O_d F = 0`. The annihilation is a property of the object substituted in, not of the
object being estimated.

If that is right, the conclusion that the cone region contributes at `O(rho^{-2/d})`
does not follow **from this argument**. We are not claiming the estimate is false.

## Why boundedness alone cannot suffice

A functional example, not a geometric one. Take a positive bounded amplitude containing
a term `U^3 log U`, with phase `V = U^2 f_0`:

```
int U^3 log U  e^{-rho f_0 U^2} dU  =  -log(rho) / (4 f_0^2 rho^2)  +  c / rho^2  +  (exp. small)
```

The fourth root carries that logarithm to order `rho^{-1/2}`. This is **not** a smooth
Ricci-flat counterexample and we do not present it as one — no such geometry is
exhibited. It shows only that hypotheses of mere boundedness cannot close the gap: an
amplitude satisfying them produces a term the estimate would have to exclude. Ruling it
out needs regularity the current argument does not assume.

## What we are *not* questioning

- **Belenchia–Benincasa–Dowker (arXiv:1510.04656) is unaffected.** Their eq. (25) bounds
  the *integrand* first by a positive-coefficient kernel, and only then rewrites the
  already-bounded quantity using the sign-reversed identity. That is a different
  operation and it is sound. Their flat case is §II.B, the curved one §III.B.
- **Identity (3.28) on a monomial stands.** That `A_{lambda,l}(n)` annihilates the
  integral of a monomial is correct, and we verified it.
- The rest of the thesis, which we did not audit.
- This is independent of the operator we were studying; it would read the same if we had
  never looked at ours.

## How this was checked

Three independent reviewers (different model families: `grok-4.6`, `deepseek-v4-pro`,
`gpt-6-astra`) were given your original text, not our summary, under blind conditions.
All three reached the same reading of (3.15)–(3.22) and located the defect at the same
step, each citing the equations independently.

We record this because we do not think agreement is evidence by itself — in the same
round, on a different question, two of the three were wrong and the dissenting one was
right. What we offer is the argument, not the count. If (3.17) does license the exchange
for a reason not written out in the text, that would settle it and we would like to know.

---

## Notes for the PI (strip before sending)

- Reference to confirm before sending: exact title, institution and year of the thesis,
  and whether a published version supersedes it.
- `biblioteca/` is git-ignored; the PDF and its sha256 are local only.
- Tone was chosen deliberately: a query, not an erratum. The reviewers verified the
  text as written; an author may hold an argument never committed to paper.
- Nothing here depends on `S4W`, and sending it does not reopen the closed appendix.
