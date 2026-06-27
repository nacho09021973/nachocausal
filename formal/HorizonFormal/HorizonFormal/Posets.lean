import Mathlib.Order.Basic
import Mathlib.Data.Set.Finite.Basic

/-!
# Posets

Basic order-theoretic aliases for the NACHOCAUSAL formalisation track.

The first pass deliberately stays in mathlib's existing order hierarchy. Causal sets
are modelled as `PartialOrder`s; local finiteness is left as an explicit hypothesis
to be pinned against mathlib interval APIs before the first theorem depending on it.
-/

namespace HorizonFormal

/-- A finite causal set, at the algebraic level, is a finite partial order. -/
abbrev FiniteCauset (P : Type u) := PartialOrder P

/--
Placeholder predicate for the local-finiteness hypothesis used by the prose notes.

This is intentionally not yet wired to a mathlib class. The next formal step is to
replace it by the exact mathlib interval-finiteness API needed for bounded ideals.
-/
def LocallyFinitePoset (P : Type u) [PartialOrder P] : Prop :=
  ∀ a b : P, Set.Finite {x : P | a ≤ x ∧ x ≤ b}

end HorizonFormal
