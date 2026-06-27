import Mathlib.Order.Hom.Basic
import HorizonFormal.Ideals

/-!
# Ends

`IdealEnd` is deliberately provisional. The broad definition below records the
candidate "non-principal ideal" notion, but the project must decide whether causal
ends should instead be maximal non-principal ideals, indecomposable past/future
sets, or equivalence classes of cofinal chains.
-/

namespace HorizonFormal

variable {P : Type u} {Q : Type v} [Preorder P] [Preorder Q]

/-- Provisional ideal-end notion: a non-principal order ideal. -/
def IdealEnd (P : Type u) [Preorder P] : Type u :=
  {I : Order.Ideal P // IsNonprincipalIdeal I}

/-- Transport an order ideal across an order isomorphism. -/
def mapIdealOrderIso (e : P ≃o Q) (I : Order.Ideal P) : Order.Ideal Q where
  toLowerSet := {
    carrier := e '' (I : Set P)
    lower' := by
      intro a b hba ha
      rcases ha with ⟨x, hxI, rfl⟩
      refine ⟨e.symm b, I.lower ?_ hxI, by simp⟩
      exact (OrderIsoClass.map_le_map_iff e).mp (by simpa using hba)
  }
  nonempty' := by
    obtain ⟨x, hxI⟩ := I.nonempty
    exact ⟨e x, x, hxI, rfl⟩
  directed' := by
    rintro y ⟨x, hxI, rfl⟩ y' ⟨x', hx'I, rfl⟩
    obtain ⟨z, hzI, hxz, hx'z⟩ := I.directed x hxI x' hx'I
    exact ⟨e z, ⟨z, hzI, rfl⟩,
      (OrderIsoClass.map_le_map_iff e).mpr hxz,
      (OrderIsoClass.map_le_map_iff e).mpr hx'z⟩

@[simp]
theorem mem_mapIdealOrderIso {e : P ≃o Q} {I : Order.Ideal P} {y : Q} :
    y ∈ mapIdealOrderIso e I ↔ e.symm y ∈ I := by
  constructor
  · rintro ⟨x, hxI, rfl⟩
    simpa using hxI
  · intro hy
    exact ⟨e.symm y, hy, by simp⟩

@[simp]
theorem mapIdealOrderIso_principal (e : P ≃o Q) (p : P) :
    mapIdealOrderIso e (Order.Ideal.principal p) = Order.Ideal.principal (e p) := by
  apply Order.Ideal.ext
  ext y
  simp [Order.Ideal.mem_principal, e.symm_apply_le]

/-- Principality is preserved by order isomorphisms. -/
theorem isPrincipalIdeal_mapOrderIso {e : P ≃o Q} {I : Order.Ideal P}
    (hI : IsPrincipalIdeal I) : IsPrincipalIdeal (mapIdealOrderIso e I) := by
  obtain ⟨p, rfl⟩ := hI
  exact ⟨e p, mapIdealOrderIso_principal e p⟩

@[simp]
theorem mapIdealOrderIso_symm_mapIdealOrderIso (e : P ≃o Q) (I : Order.Ideal P) :
    mapIdealOrderIso e.symm (mapIdealOrderIso e I) = I := by
  apply Order.Ideal.ext
  ext x
  constructor
  · rintro ⟨y, ⟨p, hp, rfl⟩, hxy⟩
    have hpx : p = x := by simpa using hxy
    simpa [hpx] using hp
  · intro hx
    exact ⟨e x, ⟨x, hx, rfl⟩, by simp⟩

/-- Principality is reflected by order isomorphisms. -/
theorem isPrincipalIdeal_of_mapOrderIso {e : P ≃o Q} {I : Order.Ideal P}
    (hI : IsPrincipalIdeal (mapIdealOrderIso e I)) : IsPrincipalIdeal I := by
  have hpre := isPrincipalIdeal_mapOrderIso (e := e.symm) hI
  simpa using hpre

theorem isPrincipalIdeal_mapOrderIso_iff {e : P ≃o Q} {I : Order.Ideal P} :
    IsPrincipalIdeal (mapIdealOrderIso e I) ↔ IsPrincipalIdeal I :=
  ⟨isPrincipalIdeal_of_mapOrderIso, isPrincipalIdeal_mapOrderIso⟩

/-- Transport provisional ideal-ends across an order isomorphism. -/
def mapIdealEndOrderIso (e : P ≃o Q) : IdealEnd P → IdealEnd Q :=
  fun I =>
    ⟨mapIdealOrderIso e I.1, by
      intro hprincipal
      exact I.2 ((isPrincipalIdeal_mapOrderIso_iff (e := e) (I := I.1)).mp hprincipal)⟩

end HorizonFormal
