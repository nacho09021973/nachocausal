import Mathlib.Data.Fin.Tuple.Sort
import Mathlib.MeasureTheory.Constructions.BorelSpace.Order

/-!
# Measurability of finite tuple sorting

This file proves only that Mathlib's actual sorting permutation is measurable
when the finite permutation type carries the discrete measurable structure.
The proof includes the lexicographic tie-breaking built into `Tuple.sort`; it
does not assume that the tuple is injective and contains no probability theory.
-/

namespace HorizonFormal

variable {n : ℕ}

local instance permMeasurableSpace :
    MeasurableSpace (Equiv.Perm (Fin n)) := ⊤

/-- Mathlib's sorting permutation is measurable as a function of a finite real
tuple, with the discrete measurable structure on the permutation type. -/
theorem measurable_tupleSort :
    Measurable (fun x : Fin n → ℝ => Tuple.sort x) := by
  apply measurable_to_countable'
  intro σ
  have hmono :
      MeasurableSet {x : Fin n → ℝ | Monotone (x ∘ σ)} := by
    rw [show {x : Fin n → ℝ | Monotone (x ∘ σ)} =
        ⋂ i, ⋂ j, {x | i ≤ j → x (σ i) ≤ x (σ j)} by
      ext x
      simp only [Set.mem_setOf_eq, Set.mem_iInter]
      exact ⟨fun h i j hij => h hij, fun h i j hij => h i j hij⟩]
    exact MeasurableSet.iInter fun i => MeasurableSet.iInter fun j => by
      by_cases hij : i ≤ j
      · simpa [hij] using measurableSet_le
          (measurable_pi_apply (σ i)) (measurable_pi_apply (σ j))
      · simp [hij]
  have htie : MeasurableSet
      {x : Fin n → ℝ |
        ∀ i j, i < j → x (σ i) = x (σ j) → σ i < σ j} := by
    rw [show {x : Fin n → ℝ |
          ∀ i j, i < j → x (σ i) = x (σ j) → σ i < σ j} =
        ⋂ i, ⋂ j,
          {x | i < j → x (σ i) = x (σ j) → σ i < σ j} by
      ext x
      simp only [Set.mem_setOf_eq, Set.mem_iInter]]
    exact MeasurableSet.iInter fun i => MeasurableSet.iInter fun j => by
      by_cases hij : i < j
      · by_cases hσ : σ i < σ j
        · simp [hσ]
        · have heq : MeasurableSet
              {x : Fin n → ℝ | x (σ i) = x (σ j)} :=
            measurableSet_eq_fun
              (measurable_pi_apply (σ i))
              (measurable_pi_apply (σ j))
          rw [show {x : Fin n → ℝ |
                i < j → x (σ i) = x (σ j) → σ i < σ j} =
              {x | x (σ i) = x (σ j)}ᶜ by
            ext x
            simp [hij, hσ]]
          exact heq.compl
      · simp [hij]
  rw [show (fun x : Fin n → ℝ => Tuple.sort x) ⁻¹' {σ} =
      {x | Monotone (x ∘ σ) ∧
        ∀ i j, i < j → x (σ i) = x (σ j) → σ i < σ j} by
    ext x
    simp only [Set.mem_preimage, Set.mem_singleton_iff, Set.mem_setOf_eq]
    rw [eq_comm, Tuple.eq_sort_iff]]
  exact hmono.inter htie

#print axioms HorizonFormal.measurable_tupleSort

end HorizonFormal
