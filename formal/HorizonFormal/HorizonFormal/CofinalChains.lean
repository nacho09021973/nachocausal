import Mathlib.Data.Set.Countable
import HorizonFormal.Ideals

/-!
# Cofinal chains in countable ideals

This file pins down the countable-cofinal-chain lemma before any causal-end
interpretation is attached to it.

The theorem is intentionally stated for a mathlib `Order.Ideal`: nonempty,
downward closed, and directed. Countability is required on the ideal as a set,
not on the whole ambient preorder.
-/

namespace HorizonFormal

open Order

variable {P : Type u} [Preorder P]

/-- A sequence is nondecreasing with respect to the ambient preorder. -/
def IsNondecreasingSeq (c : Nat → P) : Prop :=
  ∀ n : Nat, c n ≤ c (n + 1)

/-- A sequence lies in an ideal and is cofinal in that ideal. -/
def IsCofinalSeqInIdeal (I : Order.Ideal P) (c : Nat → P) : Prop :=
  (∀ n : Nat, c n ∈ I) ∧ ∀ x : P, x ∈ I → ∃ n : Nat, x ≤ c n

/-- A nondecreasing sequence that is cofinal in an ideal. -/
def IsCofinalChainInIdeal (I : Order.Ideal P) (c : Nat → P) : Prop :=
  IsNondecreasingSeq c ∧ IsCofinalSeqInIdeal I c

/--
A chain is terminal in an ideal if one of its entries already dominates the
whole ideal.

For a cofinal chain whose entries lie in `I`, this means the ideal has a maximum
element and hence is principal.
-/
def IsTerminalCofinalChainInIdeal (I : Order.Ideal P) (c : Nat → P) : Prop :=
  ∃ n : Nat, ∀ x : P, x ∈ I → x ≤ c n

/--
Enumeration of a countable ideal as ambient points.

The default point is drawn from `I.nonempty`, so every enumerated point remains
inside `I`.
-/
noncomputable def countableIdealEnumeration (I : Order.Ideal P)
    (hI : (I : Set P).Countable) : Nat → P :=
  Set.enumerateCountable hI (Classical.choose I.nonempty)

theorem countableIdealEnumeration_mem (I : Order.Ideal P)
    (hI : (I : Set P).Countable) (n : Nat) :
    countableIdealEnumeration I hI n ∈ I := by
  exact Set.enumerateCountable_mem hI (Classical.choose_spec I.nonempty) n

theorem countableIdealEnumeration_surjective_on (I : Order.Ideal P)
    (hI : (I : Set P).Countable) :
    ∀ x : P, x ∈ I → ∃ n : Nat, countableIdealEnumeration I hI n = x := by
  intro x hx
  have hrange :
      Set.range (countableIdealEnumeration I hI) = (I : Set P) := by
    simpa [countableIdealEnumeration] using
      Set.range_enumerateCountable_of_mem hI (Classical.choose_spec I.nonempty)
  exact (Set.mem_range.mp (by simpa [hrange] using hx))

/-- One recursive step: upper-bound the previous chain point and the next enumeration point. -/
noncomputable def cofinalChainNext (I : Order.Ideal P)
    (hI : (I : Set P).Countable) (n : Nat) (prev : I) : I :=
  ⟨Classical.choose
      (I.directed prev.1 prev.2
        (countableIdealEnumeration I hI (n + 1))
        (countableIdealEnumeration_mem I hI (n + 1))),
    (Classical.choose_spec
      (I.directed prev.1 prev.2
        (countableIdealEnumeration I hI (n + 1))
        (countableIdealEnumeration_mem I hI (n + 1)))).1⟩

theorem cofinalChainNext_prev_le (I : Order.Ideal P)
    (hI : (I : Set P).Countable) (n : Nat) (prev : I) :
    prev.1 ≤ (cofinalChainNext I hI n prev).1 :=
  (Classical.choose_spec
    (I.directed prev.1 prev.2
      (countableIdealEnumeration I hI (n + 1))
      (countableIdealEnumeration_mem I hI (n + 1)))).2.1

theorem countableIdealEnumeration_le_cofinalChainNext (I : Order.Ideal P)
    (hI : (I : Set P).Countable) (n : Nat) (prev : I) :
    countableIdealEnumeration I hI (n + 1) ≤ (cofinalChainNext I hI n prev).1 :=
  (Classical.choose_spec
    (I.directed prev.1 prev.2
      (countableIdealEnumeration I hI (n + 1))
      (countableIdealEnumeration_mem I hI (n + 1)))).2.2

/--
Construct a nondecreasing sequence in a countable ideal by recursively taking
directed upper bounds of the previous chosen point and the next enumerated ideal
element.
-/
noncomputable def cofinalChainSubtypeOfCountableIdeal (I : Order.Ideal P)
    (hI : (I : Set P).Countable) : Nat → I :=
  Nat.rec
    ⟨countableIdealEnumeration I hI 0, countableIdealEnumeration_mem I hI 0⟩
    (fun n prev => cofinalChainNext I hI n prev)

/-- The ambient version of `cofinalChainSubtypeOfCountableIdeal`. -/
noncomputable def cofinalChainOfCountableIdeal (I : Order.Ideal P)
    (hI : (I : Set P).Countable) : Nat → P :=
  fun n => (cofinalChainSubtypeOfCountableIdeal I hI n).1

theorem cofinalChainOfCountableIdeal_mem (I : Order.Ideal P)
    (hI : (I : Set P).Countable) (n : Nat) :
    cofinalChainOfCountableIdeal I hI n ∈ I :=
  (cofinalChainSubtypeOfCountableIdeal I hI n).2

theorem cofinalChainOfCountableIdeal_step (I : Order.Ideal P)
    (hI : (I : Set P).Countable) (n : Nat) :
    cofinalChainOfCountableIdeal I hI n ≤ cofinalChainOfCountableIdeal I hI (n + 1) := by
  change (cofinalChainSubtypeOfCountableIdeal I hI n).1 ≤
    (cofinalChainNext I hI n (cofinalChainSubtypeOfCountableIdeal I hI n)).1
  exact cofinalChainNext_prev_le I hI n (cofinalChainSubtypeOfCountableIdeal I hI n)

theorem countableIdealEnumeration_le_cofinalChain (I : Order.Ideal P)
    (hI : (I : Set P).Countable) :
    ∀ n : Nat, countableIdealEnumeration I hI n ≤ cofinalChainOfCountableIdeal I hI n := by
  intro n
  induction n with
  | zero =>
      simp [cofinalChainOfCountableIdeal, cofinalChainSubtypeOfCountableIdeal]
  | succ n _ih =>
      change countableIdealEnumeration I hI (n + 1) ≤
        (cofinalChainNext I hI n (cofinalChainSubtypeOfCountableIdeal I hI n)).1
      exact countableIdealEnumeration_le_cofinalChainNext I hI n
        (cofinalChainSubtypeOfCountableIdeal I hI n)

/--
Every countable mathlib ideal has a nondecreasing cofinal sequence.

No non-principality or local-finiteness hypothesis is needed for this existence
statement. Non-principality becomes relevant only if one additionally wants the
sequence to have no terminal maximum / no eventual principal bound.
-/
theorem exists_cofinalChain_of_countableIdeal (I : Order.Ideal P)
    (hI : (I : Set P).Countable) :
    ∃ c : Nat → P, IsCofinalChainInIdeal I c := by
  refine ⟨cofinalChainOfCountableIdeal I hI, ?_, ?_, ?_⟩
  · exact cofinalChainOfCountableIdeal_step I hI
  · exact cofinalChainOfCountableIdeal_mem I hI
  · intro x hx
    obtain ⟨n, hn⟩ := countableIdealEnumeration_surjective_on I hI x hx
    refine ⟨n, ?_⟩
    rw [← hn]
    exact countableIdealEnumeration_le_cofinalChain I hI n

/-- A terminal cofinal chain packages a maximum element of the ideal. -/
theorem hasMaximum_of_terminal_cofinalChain {I : Order.Ideal P} {c : Nat → P}
    (hc : IsCofinalChainInIdeal I c) (hterm : IsTerminalCofinalChainInIdeal I c) :
    ∃ m : P, HasMaximumInIdeal I m := by
  obtain ⟨n, hmax⟩ := hterm
  exact ⟨c n, ⟨hc.2.1 n, hmax⟩⟩

/--
No cofinal chain in a non-principal ideal can have a terminal element dominating
the whole ideal.
-/
theorem not_terminal_cofinalChain_of_nonprincipal {I : Order.Ideal P}
    (hI : IsNonprincipalIdeal I) {c : Nat → P}
    (hc : IsCofinalChainInIdeal I c) :
    ¬ IsTerminalCofinalChainInIdeal I c := by
  intro hterm
  exact not_hasMaximum_of_nonprincipal hI (hasMaximum_of_terminal_cofinalChain hc hterm)

/--
Every countable non-principal ideal has a nondecreasing cofinal sequence which
is not terminal in the ideal.
-/
theorem exists_nonterminal_cofinalChain_of_countable_nonprincipalIdeal
    (I : Order.Ideal P) (hcount : (I : Set P).Countable)
    (hnonprincipal : IsNonprincipalIdeal I) :
    ∃ c : Nat → P, IsCofinalChainInIdeal I c ∧
      ¬ IsTerminalCofinalChainInIdeal I c := by
  obtain ⟨c, hc⟩ := exists_cofinalChain_of_countableIdeal I hcount
  exact ⟨c, hc, not_terminal_cofinalChain_of_nonprincipal hnonprincipal hc⟩

end HorizonFormal
