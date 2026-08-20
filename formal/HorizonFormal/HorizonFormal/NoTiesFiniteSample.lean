import HorizonFormal.AtomlessIndependent

/-!
# No ties in a finite atomless independent sample

This file performs only the finite aggregation from pairwise almost-sure
inequality to almost-sure injectivity of a sample.  It does not construct a
sorting permutation, ranks, or a `StrictRankCoupling`.
-/

namespace HorizonFormal

open MeasureTheory ProbabilityTheory

/-- A finite mutually independent family with a common atomless law is
injective almost surely. -/
theorem no_ties_finite_sample_ae
    {ι Ω α : Type*} [Finite ι]
    [MeasurableSpace Ω] [MeasurableSpace α] [MeasurableEq α]
    {μ : Measure Ω} {ν : Measure α} [NoAtoms ν]
    {X : ι → Ω → α}
    (hX_indep : iIndepFun X μ)
    (hX_law : ∀ i, HasLaw (X i) ν μ) :
    ∀ᵐ ω ∂μ, Function.Injective fun i ↦ X i ω := by
  letI : IsProbabilityMeasure μ := hX_indep.isProbabilityMeasure
  have hpair : ∀ᵐ ω ∂μ, ∀ i j, i ≠ j → X i ω ≠ X j ω := by
    apply Filter.eventually_all.2
    intro i
    apply Filter.eventually_all.2
    intro j
    by_cases hij : i = j
    · exact Filter.Eventually.of_forall fun _ hne ↦ (hne hij).elim
    · filter_upwards [atomless_independent_not_equal_ae
        (hX_indep.indepFun hij) (hX_law i) (hX_law j).aemeasurable] with ω hne
      exact fun _ ↦ hne
  filter_upwards [hpair] with ω hω
  intro i j hEq
  by_contra hij
  exact hω i j hij hEq

#print axioms HorizonFormal.no_ties_finite_sample_ae

end HorizonFormal
