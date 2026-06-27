# Roadmap for Deep — Lean-first formal branch

Status: continuation roadmap for the formal Lean branch.

Date: 2026-06-27.

Scope: pure order theory. Do not formalise Schwarzschild, GKP, sprinklings,
fuzzy ladders, event horizons, or numerical estimators yet.

## 0. Working context

Repository:

```bash
cd /home/adnac/nachocausal
```

Lean project:

```bash
cd formal/HorizonFormal
. "$HOME/.elan/env"
lake build
```

Current expected build:

```text
Build completed successfully
```

Important: `DeepMath/` is a separate local helper workspace and should not be
added, edited, committed, or assumed part of this repo unless explicitly
requested later.

## 1. Current Lean module map

```text
formal/HorizonFormal/
├── HorizonFormal.lean
├── Main.lean
├── HorizonFormal/
│   ├── Posets.lean
│   ├── Ideals.lean
│   ├── CofinalChains.lean
│   ├── Ends.lean
│   ├── ChainEnds.lean
│   ├── Accessibility.lean
│   └── Horizon.lean
├── lakefile.toml
├── lake-manifest.json
└── lean-toolchain
```

The formal branch currently separates three layers:

1. Algebraic/order-theoretic facts already proved in Lean.
2. Provisional end definitions.
3. Relational horizon vocabulary with no physical claim.

## 2. Current proved core

### 2.1 Ideals

File:

```text
formal/HorizonFormal/HorizonFormal/Ideals.lean
```

Important definitions:

```lean
PrincipalIdeal
IsPrincipalIdeal
IsNonprincipalIdeal
IsBoundedIdeal
HasMaximumInIdeal
```

Proved:

```lean
ideal_eq_principal_of_hasMaximum
isPrincipalIdeal_of_finite
isPrincipalIdeal_of_bounded_of_finite_Iic
isPrincipalIdeal_of_bounded_of_finiteLowerIntervals
not_hasMaximum_of_nonprincipal
not_finite_of_nonprincipal
```

Interpretation:

- A maximum element in a mathlib ideal makes it principal.
- A finite mathlib ideal is principal.
- A bounded ideal is principal only when the relevant lower interval is finite.
- A non-principal ideal cannot have a maximum and cannot be finite.

Critical hypothesis:

```lean
FiniteLowerIntervals P := ∀ b : P, (Set.Iic b).Finite
```

Do not claim that ordinary interval local finiteness alone is enough for
bounded-ideal principalness. The proof consumes finite lower intervals.

### 2.2 Cofinal chains

File:

```text
formal/HorizonFormal/HorizonFormal/CofinalChains.lean
```

Important definitions:

```lean
IsNondecreasingSeq
IsCofinalSeqInIdeal
IsCofinalChainInIdeal
IsTerminalCofinalChainInIdeal
```

Cofinality is fixed as:

```lean
∀ x : P, x ∈ I → ∃ n : Nat, x ≤ c n
```

The chain type is:

```lean
c : Nat → P
```

Countability hypothesis is on the ideal subset:

```lean
(I : Set P).Countable
```

not necessarily on all of `P`.

Proved:

```lean
exists_cofinalChain_of_countableIdeal
hasMaximum_of_terminal_cofinalChain
not_terminal_cofinalChain_of_nonprincipal
exists_nonterminal_cofinalChain_of_countable_nonprincipalIdeal
```

Interpretation:

- Every countable mathlib ideal has a nondecreasing cofinal sequence.
- If the ideal is non-principal, no cofinal chain can have a terminal element
  dominating the whole ideal.
- Every countable non-principal ideal has a non-terminal cofinal chain.

Important correction:

Local finiteness and non-principality are not needed for existence of a cofinal
sequence. Non-principality is needed only for the non-terminal conclusion.

### 2.3 Provisional ideal ends

File:

```text
formal/HorizonFormal/HorizonFormal/Ends.lean
```

Current provisional definition:

```lean
IdealEnd P := {I : Order.Ideal P // IsNonprincipalIdeal I}
```

Proved:

```lean
mapIdealOrderIso
mapIdealOrderIso_principal
isPrincipalIdeal_mapOrderIso
isPrincipalIdeal_of_mapOrderIso
isPrincipalIdeal_mapOrderIso_iff
mapIdealEndOrderIso
```

Interpretation:

- Order isomorphisms preserve and reflect principality.
- Order isomorphisms transport provisional ideal ends.

Do not claim this for arbitrary embeddings. Embeddings into larger codomains can
create new lower elements and break ideal-image closure.

### 2.4 Chain ends, option 2

File:

```text
formal/HorizonFormal/HorizonFormal/ChainEnds.lean
```

Definitions:

```lean
ChainEventuallyLe c d := ∀ n, ∃ m, c n ≤ d m
CofinalChainEquivalent c d :=
  ChainEventuallyLe c d ∧ ChainEventuallyLe d c
```

Proved equivalence machinery:

```lean
chainEventuallyLe_refl
chainEventuallyLe_trans
cofinalChainEquivalent_refl
cofinalChainEquivalent_symm
cofinalChainEquivalent_trans
cofinalChainSetoid
nonterminalCofinalChainSetoid
```

End types:

```lean
NonterminalCofinalChainInIdeal I
ChainEndInIdeal I
ChainEnd P
```

Constructors:

```lean
chainEndInIdealOfNonterminalChain
chainEndInIdealOfCountableNonprincipal
chainEndOfCountableIdealEnd
nonempty_chainEndInIdeal_of_countable_nonprincipal
nonempty_chainEnd_of_countable_idealEnd
```

Interpretation:

- Option 2 is now represented: ends as equivalence classes of non-terminal
  cofinal chains.
- Provisional downstream decision: `ChainEnd P` coexists with `IdealEnd P`.
  `IdealEnd` selects the ambient non-principal ideal; `ChainEnd` represents the
  cofinal direction inside that ideal.
- This is not yet a physical escape end.

### 2.5 Accessibility

File:

```text
formal/HorizonFormal/HorizonFormal/Accessibility.lean
```

Proved:

```lean
accessesIdeal_iff_mem
relationalPastOfIdeal_eq
```

Important consequence:

If the reference object is already an `Order.Ideal`, then the relational past of
that ideal is just the ideal itself. For a nontrivial escape construction, start
from a reference subset or family `R : Set P` and then form its lower closure.

### 2.6 Relational horizon vocabulary

File:

```text
formal/HorizonFormal/HorizonFormal/Horizon.lean
```

Definitions:

```lean
RelationalReference
RelationalPast
RelationalBlackRegion
IsCover
RelationalHorizon
```

Proved:

```lean
mem_relationalPast_of_mem
relationalPast_lower
relationalPast_mono
relationalBlackRegion_antitone
relationalBlackRegion_upper
mem_relationalHorizon_pair
relationalHorizon_fst_mem_black
relationalHorizon_snd_mem_past
relationalHorizon_isCover
relationalHorizon_lt
relationalHorizon_ne
relationalHorizon_fst_not_mem_past
relationalHorizon_snd_not_mem_black
relationalPast_empty
relationalHorizon_empty
relationalPast_univ
relationalBlackRegion_univ
relationalHorizon_univ
```

Interpretation:

These are order-theoretic structural checks only. They establish that
`RelationalPast R` is a lower set, that enlarging `R` enlarges the past and
shrinks the black-region candidate, and that horizon pairs cross from
`RelationalBlackRegion R` to `RelationalPast R` along a strict cover. They do
not prove physical horizon recovery.

## 3. Current audit labels

Use these exact labels going forward:

```text
IDEAL_WITH_MAXIMUM_IS_PRINCIPAL = PROVED_IN_LEAN
FINITE_IDEAL_IS_PRINCIPAL = PROVED_IN_LEAN
BOUNDED_IDEAL_IS_PRINCIPAL = CONDITIONAL_ON_FINITE_LOWER_INTERVAL
NONPRINCIPAL_IDEAL_HAS_NO_MAXIMUM = PROVED_IN_LEAN
NONPRINCIPAL_IDEAL_IS_INFINITE = PROVED_IN_LEAN
COUNTABLE_IDEAL_HAS_COFINAL_CHAIN = PROVED_IN_LEAN
COUNTABLE_NONPRINCIPAL_IDEAL_HAS_NONTERMINAL_COFINAL_CHAIN = PROVED_IN_LEAN
ORDER_ISOMORPHISMS_PRESERVE_PROVISIONAL_IDEAL_ENDS = PROVED_IN_LEAN
EMBEDDINGS_PRESERVE_IDEAL_ENDS = HYPOTHESES_OPEN
CHAIN_END_EQUIVALENCE = PROVED_IN_LEAN
CHAIN_END_AS_QUOTIENT = DEFINITION_FORMALISED
CHAIN_END_COVARIANCE_UNDER_ORDER_ISOMORPHISMS = PROVED_IN_LEAN
CHAIN_GENERATED_LOWER_SET_EQUIVALENCE = PROVED_IN_LEAN
PREGEOMETRIC_RELATIONAL_HORIZON_FORMULATION = DEFINITION_FORMALISED
RELATIONAL_PAST_LOWER_SET = PROVED_IN_LEAN
RELATIONAL_REFERENCE_MONOTONICITY = PROVED_IN_LEAN
RELATIONAL_HORIZON_FRONTIER_SHAPE = PROVED_IN_LEAN
PHYSICAL_ESCAPE_END_INTERPRETATION = OPEN
```

Avoid these overbroad labels:

```text
IDl_FUNCTORIALITY_UNDER_MONOTONE_MAPS = PROVED
END_PRESERVATION_UNDER_ORDER_EMBEDDINGS = PROVED
BOUNDED_IDEAL_IS_PRINCIPAL_WITHOUT_FINITE_LOWER_INTERVAL = PROVED
CHAIN_END_EQUALS_PHYSICAL_CAUSAL_END = PROVED
```

## 4. Completed formal work package — chain-end transport

`ChainEnd` is now usable under order isomorphisms.

Goal:

```text
Order isomorphisms transport chain ends.
```

This was the right next step because:

- ideal ends already transport under order isomorphisms;
- chain representatives are maps `Nat → P`;
- the transport should be simple: map every chain point through the order
  isomorphism;
- it avoids arbitrary embeddings for now.

### 4.1 Chain transport

In `ChainEnds.lean`, now defined:

```lean
def mapChainOrderIso (e : P ≃o Q) (c : Nat → P) : Nat → Q :=
  fun n => e (c n)
```

Proved:

```lean
mapChainOrderIso_nondec
chainEventuallyLe_mapOrderIso
cofinalChainEquivalent_mapOrderIso
```

### 4.2 Transport cofinal chains inside transported ideals

Using existing:

```lean
mapIdealOrderIso e I
```

Proved:

```lean
mapChainOrderIso_cofinalSeqInIdeal
mapChainOrderIso_cofinalChainInIdeal
```

### 4.3 Preserve non-terminality

Proved:

```lean
mapChainOrderIso_not_terminal
```

### 4.4 Transport `NonterminalCofinalChainInIdeal`

Defined:

```lean
def mapNonterminalChainOrderIso
    (e : P ≃o Q) {I : Order.Ideal P} :
    NonterminalCofinalChainInIdeal I →
    NonterminalCofinalChainInIdeal (mapIdealOrderIso e I)
```

### 4.5 Descend to quotient

Proved compatibility:

```lean
mapNonterminalChainOrderIso_respects_equiv
```

Defined:

```lean
def mapChainEndInIdealOrderIso
    (e : P ≃o Q) (I : Order.Ideal P) :
    ChainEndInIdeal I →
    ChainEndInIdeal (mapIdealOrderIso e I)
```

### 4.6 Transport ambient `ChainEnd`

Using:

```lean
mapIdealEndOrderIso
```

Defined:

```lean
def mapChainEndOrderIso (e : P ≃o Q) :
    ChainEnd P → ChainEnd Q
```

This gives the clean algebraic statement:

```text
Chain-end classes are invariant under order isomorphism.
```

Audit label after this succeeds:

```text
CHAIN_END_COVARIANCE_UNDER_ORDER_ISOMORPHISMS = PROVED_IN_LEAN
```

Do not generalise to embeddings yet.

## 5. Second formal work package

Completed after isomorphism transport: compare `IdealEnd` and `ChainEnd` for
countable ideals at the API level.

Already formalised:

```lean
chainEndOfCountableIdealEnd
```

Added theorem-style existence wrappers:

```lean
theorem nonempty_chainEndInIdeal_of_countable_nonprincipal
    (I : Order.Ideal P) (hcount : (I : Set P).Countable)
    (hnonprincipal : IsNonprincipalIdeal I) :
    Nonempty (ChainEndInIdeal I)
```

and:

```lean
theorem nonempty_chainEnd_of_countable_idealEnd
    (I : IdealEnd P) (hcount : (I.1 : Set P).Countable) :
    Nonempty (ChainEnd P)
```

This is mostly packaging, but it makes downstream usage simpler.

## 6. Completed formal work package — generated lower sets

The ideal/lower-set content generated by a chain is now formalised.

Defined:

```lean
def IdealGeneratedByChain (c : Nat → P) : Set P :=
  {x : P | ∃ n, x ≤ c n}
```

Proved:

```lean
chain_mem_IdealGeneratedByChain
IdealGeneratedByChain_lower
IdealGeneratedByChain_subset_ideal
ideal_subset_IdealGeneratedByChain
IdealGeneratedByChain_eq_ideal
IdealGeneratedByChain_eq_ideal_of_cofinalChain
```

If `c` is cofinal in `I` and every `c n ∈ I`, then:

```lean
IdealGeneratedByChain c = (I : Set P)
```

This is useful because it shows the chain representation and ideal
representation carry the same lower-set content.

Also proved:

```lean
ChainEventuallyLe_iff_generated_subset
CofinalChainEquivalent_iff_generated_eq
```

So mutual cofinal domination is exactly equality of the generated lower sets.
This justifies the chain quotient relation as equality of represented lower-set
content. This remains algebraic; it is not yet a physical causal-end theorem.

## 7. Fourth formal work package

Only after the above: embeddings with repair hypotheses.

Do not attempt:

```text
arbitrary order embeddings preserve ends
```

Try one of these precise alternatives:

### Option A — lower-closed image

Hypothesis:

```lean
∀ {q p}, q ≤ e p → ∃ p', e p' = q
```

Meaning: every element below an embedded point is still in the image.

### Option B — work in image suborder

Transport from `P` to the subtype:

```lean
Set.range e
```

This should be closer to an isomorphism.

### Option C — lower closure of image

Define image ideal as lower closure of `e '' I`, then study when
non-principality is preserved or destroyed.

This is mathematically real work. Keep it separate from the isomorphism path.

## 8. Documentation work package

Update these files when each work package lands:

```text
dev/LEAN_HYPOTHESIS_AUDIT.md
dev/LEAN_FORMALIZATION_NOTES.md
formal/HorizonFormal/README.md
```

Any new theorem should get one of these labels:

```text
FORMALISED
LEAN_TARGET
HYPOTHESES_OPEN
DEFERRED_PHYSICS
DEFINITION_FORMALISED
```

Do not introduce `PROVED` in prose unless the Lean theorem name is cited.

## 9. Commit discipline

Before committing:

```bash
cd /home/adnac/nachocausal/formal/HorizonFormal
. "$HOME/.elan/env"
lake build

cd /home/adnac/nachocausal
git diff --check
git status --short
```

Stage explicitly. Do not use `git add .` while `DeepMath/` is present:

```bash
git add dev/LEAN_HYPOTHESIS_AUDIT.md \
        dev/LEAN_FORMALIZATION_NOTES.md \
        formal/HorizonFormal/HorizonFormal.lean \
        formal/HorizonFormal/HorizonFormal/ChainEnds.lean \
        formal/HorizonFormal/HorizonFormal/CofinalChains.lean \
        formal/HorizonFormal/HorizonFormal/Ends.lean \
        formal/HorizonFormal/README.md
```

Suggested commit message for the current option-2 work:

```bash
git commit -m "formal: define chain-end quotient"
git push origin main
```

## 10. Conceptual boundary

Everything above is algebraic. The current formal layer proves facts about:

- preorders;
- mathlib ideals;
- principal/non-principal ideals;
- cofinal sequences;
- equivalence classes of cofinal chains;
- transport under order isomorphism once implemented.

It does not yet prove:

- existence of physical future infinity in a finite causal set;
- event-horizon reconstruction;
- Schwarzschild correspondence;
- GKP boundary correspondence;
- manifoldlikeness;
- validity of any numerical horizon estimator.

The correct conceptual token for the current endpoint is:

```text
ALGEBRAIC_CHAIN_END_CORE_IN_PROGRESS
```

not:

```text
PHYSICAL_HORIZON_FORMALISED
```
