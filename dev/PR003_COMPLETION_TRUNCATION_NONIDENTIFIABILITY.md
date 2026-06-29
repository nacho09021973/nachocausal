# PR-003 C1 completion/truncation non-identifiability

Status: **dev conceptual note, no code, no data, no freeze, no result**.

This note records the next single mathematical question before developing any
new C1 reference selector.

## Repo anchors

- `dev/PR003_C1_REFERENCE_ALTERNATIVES.md` lists R1/R2/R3 replacement ideas
  after the negative `R=Max(C)` preflight.
- `dev/MEMO_random_orders_identifiability.md` frames a related law-level
  identifiability problem for unlabelled finite suborders.
- `dev/X0_Qn_wellposedness_NOTES.md` records that C1/C2 require mandatory
  truncation controls before any physical interpretation.
- `docs/preregistration.md` already separates horizon-truncation from
  domain-edge truncation through matched flat controls.
- `docs/comite/comite_decision_006_pr003-c1-c2-c3-refine-before-promotion.md`
  keeps the truncation confound active for C1/C2.

Those files do not yet isolate the sharper obstruction below.

## Correction to the selector-existence question

The weak question

```text
Does there exist a deterministic, relabel-invariant, order-only, nontrivial
selector R(C)?
```

is not enough for C1. The abstract answer is probably yes: finite posets have
many canonical order-only profiles, including past/future cardinalities,
interval profiles, automorphism orbits, and iterative refinements. A canonical
selector can satisfy Guard-v while still having no physical membrane meaning.

The C1-relevant selector question must include the correspondence obligations:

```text
R(C) must be order-only, deterministic, equivariant, nondegenerate,
stable under sprinkling/truncation, and convergent toward the intended
geometric reference object in the manifoldlike regime.
```

Without the last two clauses, a closed selector only proves mathematical
definability, not recoverability of the intended causal structure.

## Automorphism caveat

Automorphism arguments are useful but insufficient. If `g in Aut(C)`,
equivariance gives `R(C) = g R(C)`. This rules out selecting a single named
representative inside a nontrivial orbit, but it does not rule out selecting:

- the whole orbit;
- a union of orbits;
- an invariant antichain or invariant global subset.

Also, finite Poisson sprinklings are generically asymmetric. A no-go based only
on exceptional symmetric posets would not settle the physical regime.

## Central proposition

The stronger obstruction is completion/truncation dependence.

```text
COMPLETION_AND_TRUNCATION_NONIDENTIFIABILITY

There exist a finite poset C and two physically admissible completions

    i1 : C -> C1
    i2 : C -> C2

such that C is the same order-only observed subposet in both completions, but
the physically correct C1 reference induced from C1 and pulled back along i1 is
incompatible with the physically correct C1 reference induced from C2 and pulled
back along i2.

Therefore no selector R(C) depending only on the finite order of C can be
universally correct for both completions.
```

Here "incompatible" must be made precise before any proof attempt. Minimal
options:

- different selected reference subset inside the shared copy of `C`;
- different selected interface/antichain for `H[C;R]`;
- different C1 argmin/argmax decision on the same shared elements;
- one completion inducing a defined finite C1 reference while the other induces
  `NO_INTERFACE`.

## Required definitions before proof

The proposition is not ready until these terms are closed:

- **Observed subposet:** induced finite suborder, stem, interval, or another
  explicitly allowed observation class.
- **Physically admissible completion:** the class of manifoldlike extensions or
  truncations allowed in PR-003, including whether they are Schwarzschild,
  Hayward, flat controls, box-truncated patches, or a restricted comparison
  class.
- **Induced reference:** the rule that says what the "correct" C1 reference is
  in a completed spacetime before restriction back to `C`.
- **Pullback to C:** how references or decisions in the completion are compared
  on the shared finite subposet.
- **Incompatibility:** the exact observable contradiction that no intrinsic
  finite selector can satisfy simultaneously.

## Consequence for R1/R2/R3

Until the proposition is adjudicated, R1/R2/R3 are not implementation targets.
They are secondary attempts to construct an intrinsic selector. If the
completion/truncation proposition holds in the physically admissible class, then
those candidates are attempts to reconstruct information absent from the finite
order itself.

If the proposition fails, or only holds for inadmissible completions, the project
can return to R-selector closure with stronger obligations: stability under
sprinkling/truncation and convergence to the intended geometric object, not only
Guard-v.

## Committee question

The next committee question should be exactly:

```text
Can the same finite order-only subposet admit two physically permitted
completions that induce incompatible C1 decisions on the shared subposet?
```

Recommended verdict vocabulary:

```text
COMPLETION_NONIDENTIFIABILITY_PLAUSIBLE_FORMALISE
COMPLETION_NONIDENTIFIABILITY_NOT_ESTABLISHED_RETURN_TO_R_SELECTOR
NEEDS_PRECISE_COMPLETION_CLASS
```

No dev probe, no selector implementation, no threshold change, and no C1
promotion follows from this note.

## Alloy status — logical layer only

Two bounded Alloy models now support the claim that the non-identifiability
hypothesis is mathematically non-vacuous at the **finite relational** level:

- `docs/alloy/alloy_verification_001_completion-maximality-counterexample.md`
  checks a minimal claim of **completion-invariance of observed maximality** and
  finds a bounded counterexample.
- `docs/alloy/alloy_verification_002_completion-nonidentifiability-interface.md`
  checks a stronger minimal claim: the same observed finite order forces the
  same **interface decision** across completions. It also finds a bounded
  counterexample.

The second case is the more relevant one for PR-003 because it no longer turns
only on a global auxiliary property like maximality. It already formalizes a
completion-sensitive **decision on the shared observed copy**.

Provisional summary:

```text
LOGICAL_NONIDENTIFIABILITY_LAYER_SUPPORTED
PHYSICAL_LAYER_OPEN
```

## What Alloy 001 establishes

Alloy 001 shows:

```text
observed maximality does not factor through the observed subposet alone
```

In other words, even if two completions induce the same observed order on `C`,
whether an observed element is maximal may still depend on hidden completion
structure.

This is useful as a first obstruction, but it is not yet close enough to the
project's actual C1 target because maximality is only an auxiliary order
property.

## What Alloy 002 establishes

Alloy 002 shows:

```text
an abstract interface decision need not factor through the observed subposet alone
```

This is a better fit to the present PR-003 proposition. The model encodes:

- one shared observed finite order;
- two distinct completions extending that order;
- an order-only interface predicate on observed elements;
- a bounded witness where the predicate disagrees across completions.

So the statement

```text
"same observed order => same interface decision"
```

is already false in a small explicit finite model.

## What the Alloy results do NOT establish

Neither bounded model proves the full physical no-go the project actually
cares about. In particular, they do **not** establish that the target physical
object `T` of C1 fails to be recoverable under a physically admissible class
`\mathfrak A` with a common local germ.

They do **not** encode, certify, or approximate in any strong sense:

- faithful embedding into Schwarzschild;
- typical Poisson sprinkling;
- curvature control;
- a common local metric germ;
- continuum convergence;
- the full PR-003 notion of physically admissible completion.

Therefore the implication chain must stay explicit:

```text
combinatorial counterexample
  does NOT imply
physical no-go
```

But the converse methodological point is now stronger than before:

```text
combinatorial counterexample
  DOES imply
the non-identifiability hypothesis is not empty rhetoric
```

## Consequence for the next formal step

The immediate use of Alloy is now diagnostic, not dispositive.

Recommended interpretation:

1. Alloy 001 + 002 justify treating completion/truncation non-identifiability
   as a live formal obstruction, not merely a verbal worry.
2. They do not yet justify a committee-level physical no-go verdict.
3. Any third Alloy model should be framed honestly as a check of an
   **explicit combinatorial approximation** to admissibility, not as Alloy
   certifying "physically admissible completion" directly.

Until that approximation class is written down, the correct status is:

```text
logical obstruction: supported
physical obstruction: open
```
