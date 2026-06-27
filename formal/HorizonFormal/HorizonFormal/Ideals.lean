import Mathlib.Order.Ideal
import Mathlib.Order.Preorder.Finite
import HorizonFormal.Posets

/-!
# Ideals

Lean targets for the order-theoretic core:

* principal ideals;
* bounded ideals;
* non-principal ideals;
* the first theorem target: a finite ideal with a maximum is principal.

Mathlib's `Order.Ideal P` already means nonempty + directed + lower set. This is
stronger than a bare down-set, so project prose should be translated carefully.
-/

namespace HorizonFormal

open Order

variable {P : Type u} [Preorder P]

/-- A project-level spelling for principal ideals. -/
abbrev PrincipalIdeal (p : P) : Order.Ideal P :=
  Order.Ideal.principal p

/-- An ideal is principal if it is equal to `↓p` for some `p`. -/
def IsPrincipalIdeal (I : Order.Ideal P) : Prop :=
  ∃ p : P, I = Order.Ideal.principal p

/-- An ideal is non-principal if it is not equal to any principal ideal. -/
def IsNonprincipalIdeal (I : Order.Ideal P) : Prop :=
  ¬ IsPrincipalIdeal I

/-- A bounded ideal has an upper bound in the ambient preorder. -/
def IsBoundedIdeal (I : Order.Ideal P) : Prop :=
  ∃ b : P, ∀ x : P, x ∈ I → x ≤ b

/--
`LEAN_TARGET L0`.

If `m ∈ I` is maximum in `I`, then `I = principal m`.

This should be the first real theorem because it needs no local-finiteness API.
-/
def HasMaximumInIdeal (I : Order.Ideal P) (m : P) : Prop :=
  m ∈ I ∧ ∀ x : P, x ∈ I → x ≤ m

/-- `FORMALISED L0`: an ideal with a maximum element is principal. -/
theorem ideal_eq_principal_of_hasMaximum {I : Order.Ideal P} {m : P}
    (hm : HasMaximumInIdeal I m) : I = Order.Ideal.principal m := by
  apply Order.Ideal.ext
  ext x
  constructor
  · intro hx
    exact Order.Ideal.mem_principal.mpr (hm.2 x hx)
  · intro hx
    exact I.lower (Order.Ideal.mem_principal.mp hx) hm.1

/-- `FORMALISED L1a`: a finite ideal is principal. -/
theorem isPrincipalIdeal_of_finite {I : Order.Ideal P} (hI : (I : Set P).Finite) :
    IsPrincipalIdeal I := by
  obtain ⟨a, ha⟩ := I.nonempty
  obtain ⟨m, _ham, hmmax⟩ := hI.exists_le_maximal ha
  have hgreat : IsGreatest (I : Set P) m :=
    (I.directed.maximal_iff_isGreatest).mp hmmax
  exact ⟨m, ideal_eq_principal_of_hasMaximum ⟨hgreat.1, fun x hx => hgreat.2 hx⟩⟩

/--
`FORMALISED L1`: a bounded ideal is principal whenever its bounding lower
interval is finite.
-/
theorem isPrincipalIdeal_of_bounded_of_finite_Iic {I : Order.Ideal P} {b : P}
    (hb : ∀ x : P, x ∈ I → x ≤ b) (hfin : (Set.Iic b).Finite) :
    IsPrincipalIdeal I := by
  apply isPrincipalIdeal_of_finite
  exact hfin.subset (by
    intro x hx
    exact hb x hx)

/-- A non-principal ideal has no maximum element. -/
theorem not_hasMaximum_of_nonprincipal {I : Order.Ideal P}
    (hI : IsNonprincipalIdeal I) : ¬ ∃ m : P, HasMaximumInIdeal I m := by
  rintro ⟨m, hm⟩
  exact hI ⟨m, ideal_eq_principal_of_hasMaximum hm⟩

/-- A non-principal ideal is infinite as a subset of the ambient preorder. -/
theorem not_finite_of_nonprincipal {I : Order.Ideal P}
    (hI : IsNonprincipalIdeal I) : ¬ (I : Set P).Finite := by
  intro hfin
  exact hI (isPrincipalIdeal_of_finite hfin)

end HorizonFormal
