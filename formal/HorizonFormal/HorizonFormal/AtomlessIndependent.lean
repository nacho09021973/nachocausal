import Mathlib.MeasureTheory.Measure.Prod
import Mathlib.MeasureTheory.Measure.Typeclasses.NoAtoms
import Mathlib.Probability.HasLaw
import Mathlib.Probability.Independence.Basic

/-!
# Independent atomless variables do not collide

This file contains only the first probabilistic brick needed by the random-rank
bridge.  It does not construct ranks, prove uniformity, or address measurability
of sorting operations.
-/

namespace HorizonFormal

open MeasureTheory ProbabilityTheory Set

/-- If `X` and `Y` are independent and the law of `X` has no atoms, then
`X ≠ Y` almost surely.  No assumption on the law of `Y` is needed. -/
theorem atomless_independent_not_equal_ae
    {Ω α : Type*} [MeasurableSpace Ω] [MeasurableSpace α] [MeasurableEq α]
    {μ : Measure Ω} [IsFiniteMeasure μ]
    {ν : Measure α} [NoAtoms ν]
    {X Y : Ω → α}
    (hXY : IndepFun X Y μ)
    (hX : HasLaw X ν μ)
    (hY : AEMeasurable Y μ) :
    ∀ᵐ ω ∂μ, X ω ≠ Y ω := by
  have hdiag : (μ.map Y).prod ν (diagonal α) = 0 := by
    apply Measure.measure_prod_null_of_ae_null measurableSet_diagonal
    refine ae_of_all _ fun y => ?_
    simp [diagonal]
  have hcollision : μ {ω | Y ω = X ω} = 0 := by
    change μ ((fun ω => (Y ω, X ω)) ⁻¹' diagonal α) = 0
    rw [← Measure.map_apply_of_aemeasurable
      (hY.prodMk hX.aemeasurable) measurableSet_diagonal]
    rw [hXY.symm.map_prod_eq_prod_map_map hY hX.aemeasurable, hX.map_eq]
    exact hdiag
  have hae : ∀ᵐ ω ∂μ, ω ∉ {ω | Y ω = X ω} :=
    measure_eq_zero_iff_ae_notMem.mp hcollision
  filter_upwards [hae] with ω hω
  simpa [ne_comm] using hω

#print axioms HorizonFormal.atomless_independent_not_equal_ae

end HorizonFormal
