# Lean hypothesis audit — order-theoretic core

Status: dev audit, not a physics result. This file records the exact hypotheses
needed before a prose lemma may remain labelled `PROVED` in the Lean-first branch.

Date: 2026-06-27.

## Audit rule

A statement is allowed to keep a strong proof label only after its formal type
makes every mathematical hypothesis explicit. If the Lean statement needs extra
structure that the prose version did not mention, the prose label must be
weakened to `CONDITIONAL` or `HYPOTHESES_OPEN` until the missing assumptions are
added to the design notes.

## Current theorem inventory

| Claim | Current Lean status | Exact hypotheses | Audit verdict |
|---|---:|---|---|
| An ideal with a maximum is principal. | `FORMALISED` as `ideal_eq_principal_of_hasMaximum`. | `[Preorder P]`; `I : Order.Ideal P`; `m ∈ I`; every `x ∈ I` satisfies `x ≤ m`. | `PROVED_AS_STATED_IN_LEAN`. |
| Every finite ideal is principal. | `FORMALISED` as `isPrincipalIdeal_of_finite`. | `[Preorder P]`; `I : Order.Ideal P`; `(I : Set P).Finite`. | `PROVED_WITH_FINITE_IDEAL_HYPOTHESIS`. |
| Every bounded ideal is principal. | `FORMALISED` only as `isPrincipalIdeal_of_bounded_of_finite_Iic`. | `[Preorder P]`; upper bound `b`; every `x ∈ I` satisfies `x ≤ b`; and `(Set.Iic b).Finite`. | `CONDITIONAL`; boundedness alone is insufficient. |
| A non-principal ideal has no maximum. | `FORMALISED` as `not_hasMaximum_of_nonprincipal`. | `[Preorder P]`; `I : Order.Ideal P`; non-principal means `¬ ∃ p, I = principal p`. | `PROVED_FOR_MATHLIB_IDEALS`. |
| A non-principal ideal is infinite. | `FORMALISED` as `not_finite_of_nonprincipal`. | Same as above. | `PROVED_FOR_MATHLIB_IDEALS`. |
| Order isomorphisms preserve/refect principal ideals. | `FORMALISED` as `isPrincipalIdeal_mapOrderIso_iff`. | `[Preorder P] [Preorder Q]`; `e : P ≃o Q`; ideal transported by `mapIdealOrderIso`. | `PROVED_FOR_ORDER_ISOMORPHISMS`. |
| Order isomorphisms preserve provisional ideal ends. | `FORMALISED` as `mapIdealEndOrderIso`. | Same as above; `IdealEnd` currently means non-principal mathlib ideal. | `PROVED_FOR_PROVISIONAL_IDEALEND`. |
| Every countable ideal has a nondecreasing cofinal sequence. | `FORMALISED` as `exists_cofinalChain_of_countableIdeal`. | `[Preorder P]`; `I : Order.Ideal P`; `(I : Set P).Countable`; sequence `c : Nat → P`; cofinal means `∀ x ∈ I, ∃ n, x ≤ c n`. | `PROVED_FOR_COUNTABLE_MATHLIB_IDEALS`. |
| Every countable non-principal ideal has a non-terminal cofinal sequence. | `FORMALISED` as `exists_nonterminal_cofinalChain_of_countable_nonprincipalIdeal`. | Same countability hypothesis plus `IsNonprincipalIdeal I`; terminal means `∃ n, ∀ x ∈ I, x ≤ c n`. | `PROVED_FOR_COUNTABLE_NONPRINCIPAL_MATHLIB_IDEALS`. |
| `x ⇝ I` iff `x ∈ I`. | `FORMALISED` as `accessesIdeal_iff_mem`. | `[Preorder P]`; `I : Order.Ideal P`; accessibility defined by `∃ y ∈ I, x ≤ y`. | `PROVED`; also shows the ideal formulation is already downward closed. |
| Relational horizon for `R = ∅` is empty. | `FORMALISED` as `relationalHorizon_empty`. | `[Preorder P]`; `R : Set P`; relation uses preorder cover placeholder. | `PROVED_AS_ORDER_TRIVIALITY`. |
| Relational horizon for `R = univ` is empty. | `FORMALISED` as `relationalHorizon_univ`. | Same as above. | `PROVED_AS_ORDER_TRIVIALITY`. |

## Hypotheses exposed by Lean

### 1. `Order.Ideal` is stronger than a down-set

In mathlib, `Order.Ideal P` is not an arbitrary lower set. It includes:

- nonemptiness;
- downward closure;
- upward directedness.

Therefore any project statement using "ideal" must be checked for this stronger
meaning. If a note only needs `↓R = {x | ∃ y ∈ R, x ≤ y}`, the correct object is a
reference subset plus its lower closure, not automatically `Order.Ideal`.

### 2. Bounded does not mean finite

The informal statement:

```text
in a locally finite poset, every bounded ideal is principal
```

is not yet a Lean theorem in that exact wording. The checked theorem is:

```text
if I ⊆ Set.Iic b and Set.Iic b is finite, then I is principal
```

This is the right finite-interval form. To recover the prose version we still
need to connect the project phrase "locally finite" to the exact interval API:

```lean
∀ b : P, (Set.Iic b).Finite
```

or another hypothesis strong enough to imply finiteness of the relevant lower
interval. Standard interval local finiteness between two endpoints is not, by
itself, enough unless the lower bound side is also controlled.

### 3. Countable cofinal chains are now precisely stated

The claim:

```text
every non-principal ideal in a countable locally finite poset admits a cofinal
nondecreasing sequence/chain
```

has been narrowed and formalised as:

```lean
exists_cofinalChain_of_countableIdeal
  (I : Order.Ideal P) (hI : (I : Set P).Countable) :
  ∃ c : Nat → P, IsCofinalChainInIdeal I c
```

where:

- the chain type is `c : Nat → P`;
- membership is part of `IsCofinalSeqInIdeal`: `∀ n, c n ∈ I`;
- nondecreasing means `∀ n, c n ≤ c (n + 1)`;
- cofinal means `∀ x : P, x ∈ I → ∃ n : Nat, x ≤ c n`;
- countability is on the ideal subset `(I : Set P)`, not necessarily on all of `P`;
- no local-finiteness hypothesis is required for existence of the cofinal sequence;
- no non-principality hypothesis is required for existence either.

The next formal strengthening is now also checked:

```text
countable non-principal ideal admits a nondecreasing cofinal sequence with no
terminal element dominating the whole ideal.
```

This is formalised as:

```lean
exists_nonterminal_cofinalChain_of_countable_nonprincipalIdeal
```

The remaining open part is the physical/causal-end reading of "unbounded":
non-terminal inside an ideal is not yet the same as future infinity, escape, or
asymptotic causal end selection.

Audit verdict: `PROVED_FOR_COUNTABLE_NONPRINCIPAL_MATHLIB_IDEALS`; stronger
escape/end interpretations remain `HYPOTHESES_OPEN`.

### 4. Embeddings are not isomorphisms

The formalised preservation result is for order isomorphisms `P ≃o Q`. A plain
order embedding into a larger codomain can acquire new lower elements below the
image, so image ideals need not be ideals without extra closure/lifting
hypotheses.

Allowed current statement:

```text
order isomorphisms preserve and reflect principality and provisional IdealEnd.
```

Not yet allowed:

```text
arbitrary order embeddings preserve ideal ends.
```

Possible repair hypotheses for embeddings:

- the image is lower closed in the codomain;
- work with the induced suborder on the image;
- require an isomorphism onto the relevant down-closed subposet;
- define a separate lower-closure operation and prove what it does to
  principality/non-principality.

### 5. `IdealEnd` is provisional

Current Lean definition:

```lean
IdealEnd P := {I : Order.Ideal P // IsNonprincipalIdeal I}
```

This is mathematically clean but physically broad. It does not yet encode:

- maximality;
- indecomposable past/future set status beyond mathlib directedness;
- equivalence classes of cofinal chains;
- terminality or causal-end selection constraints.

Audit verdict: all theorems using `IdealEnd` are `PROVED_FOR_PROVISIONAL_IDEALEND`,
not yet proof of the final causal-end interpretation.

### 6. Accessibility to an ideal is tautological

For a mathlib ideal `I`, the relation:

```lean
AccessesIdeal x I := ∃ y ∈ I, x ≤ y
```

is equivalent to `x ∈ I`, because ideals are downward closed. Therefore a
nontrivial relational escape construction should start from a reference subset
`R : Set P`, family of maximal elements, growth-flow output, or ladder family,
and then form its lower closure. Starting directly with an `Order.Ideal` erases
the distinction between "reference" and "past of reference".

## Label corrections to carry into the design notes

- `LEVEL_1_ISOMORPHISM_COVARIANCE = PROVED` remains acceptable when it means
  order isomorphisms, not arbitrary embeddings.
- `LEVEL_2_ORDER_THEORETIC_IDL_FUNCTORIALITY = PROVED` is too broad. Replace by:
  `IDEAL_TRANSPORT_UNDER_ORDER_ISOMORPHISMS = PROVED`.
- `END_PRESERVATION_UNDER_ORDER_EMBEDDINGS = PROVED` is too strong. Replace by:
  `END_PRESERVATION_UNDER_ORDER_ISOMORPHISMS = PROVED_FOR_PROVISIONAL_IDEALEND`
  and keep embeddings as `HYPOTHESES_OPEN`.
- `CHAIN_REPRESENTATION_UNDER_COUNTABLE_LOCAL_FINITE_HYPOTHESES = PROVED` should
  be narrowed to `COUNTABLE_IDEAL_HAS_NONDECREASING_COFINAL_SEQUENCE =
  PROVED_FOR_MATHLIB_IDEALS`. Local finiteness and non-principality are not
  needed for this theorem; they belong to stronger end/unboundedness claims.
- `COUNTABLE_NONPRINCIPAL_IDEAL_HAS_NONTERMINAL_COFINAL_CHAIN =
  PROVED_FOR_MATHLIB_IDEALS` is now a valid algebraic token.
- `FINITE_CAUSAL_END_APPROXIMATION = OPEN` remains correct.
- `ESCAPE_END_SELECTION = OPEN` remains correct.
- `PREGEOMETRIC_RELATIONAL_HORIZON_FORMULATION = PROVED` should be read as
  `DEFINITION_FORMALISED`; the physical interpretation remains open.

## Next Lean targets after this audit

1. Replace the placeholder `LocallyFinitePoset` with the exact hypothesis needed
   for lower-interval finiteness, or introduce a second explicit predicate:
   `FiniteLowerIntervals`.
2. Decide whether the final `IdealEnd` definition should be non-principal
   ideals, maximal non-principal ideals, or equivalence classes of non-terminal
   cofinal chains.
3. Add a small embeddings file only after choosing one of the repair hypotheses
   above.
4. Keep `IdealEnd` provisional until the project chooses between non-principal
   ideals, maximal non-principal ideals, or cofinal-chain equivalence classes.
