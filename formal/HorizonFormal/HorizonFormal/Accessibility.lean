import HorizonFormal.Ends

/-!
# Accessibility

Order-only accessibility predicates. These are algebraic placeholders for the
relational-reference programme; no metric, coordinate, Schwarzschild, GKP, or
sprinkling structure is present here.
-/

namespace HorizonFormal

variable {P : Type u} [Preorder P]

/-- A point can access an ideal if it lies below some element of that ideal. -/
def AccessesIdeal (x : P) (I : Order.Ideal P) : Prop :=
  ∃ y : P, y ∈ I ∧ x ≤ y

/-- The relational past of an ideal/reference subset, as a predicate. -/
def RelationalPastOfIdeal (I : Order.Ideal P) : Set P :=
  {x : P | AccessesIdeal x I}

theorem accessesIdeal_of_mem {x : P} {I : Order.Ideal P} (hx : x ∈ I) :
    AccessesIdeal x I :=
  ⟨x, hx, le_rfl⟩

theorem mem_of_accessesIdeal {x : P} {I : Order.Ideal P}
    (hx : AccessesIdeal x I) : x ∈ I := by
  obtain ⟨y, hyI, hxy⟩ := hx
  exact I.lower hxy hyI

@[simp]
theorem accessesIdeal_iff_mem {x : P} {I : Order.Ideal P} :
    AccessesIdeal x I ↔ x ∈ I :=
  ⟨mem_of_accessesIdeal, accessesIdeal_of_mem⟩

@[simp]
theorem relationalPastOfIdeal_eq (I : Order.Ideal P) :
    RelationalPastOfIdeal I = (I : Set P) := by
  ext x
  simp [RelationalPastOfIdeal]

end HorizonFormal
