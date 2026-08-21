import HorizonFormal.DeterministicRankBridge
import HorizonFormal.NoTiesFiniteSample

/-!
# Almost-sure strict rank coupling

This file only assembles the already certified finite-sample no-ties theorem
with the deterministic constructor of `StrictRankCoupling`.  It defines the
rank permutation pointwise, but makes no measurability or distributional claim
about that permutation.  In particular, uniformity remains outside this file.
-/

namespace HorizonFormal

open MeasureTheory ProbabilityTheory

/-- The pointwise permutation carrying a sample's `u`-ranks to its `v`-ranks.
This definition is meaningful even on samples with ties; strict coupling is
asserted only almost surely below. -/
noncomputable def sampleRankPermutation {n : ℕ} {Ω : Type*}
    (U V : Fin n → Ω → ℝ) (ω : Ω) : Equiv.Perm (Fin n) :=
  (Tuple.sort fun i ↦ U i ω).trans (Tuple.sort fun i ↦ V i ω).symm

/-- Two finite independent coordinate samples with atomless laws induce the
correct strict rank coupling almost surely.  No cross-coordinate independence,
measurability of `sampleRankPermutation`, or uniformity assertion is used. -/
theorem strictRankCoupling_ae
    {n : ℕ} {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {νU νV : Measure ℝ} [NoAtoms νU] [NoAtoms νV]
    {U V : Fin n → Ω → ℝ}
    (hU_indep : iIndepFun U μ)
    (hV_indep : iIndepFun V μ)
    (hU_law : ∀ i, HasLaw (U i) νU μ)
    (hV_law : ∀ i, HasLaw (V i) νV μ) :
    ∀ᵐ ω ∂μ, Nonempty
      (StrictRankCoupling (fun i ↦ U i ω) (fun i ↦ V i ω)
        (sampleRankPermutation U V ω)) := by
  filter_upwards
    [no_ties_finite_sample_ae hU_indep hU_law,
      no_ties_finite_sample_ae hV_indep hV_law] with ω hU hV
  exact ⟨strictRankCoupling_from_injective
    (fun i ↦ U i ω) (fun i ↦ V i ω) hU hV⟩

#print axioms HorizonFormal.sampleRankPermutation
#print axioms HorizonFormal.strictRankCoupling_ae

end HorizonFormal
