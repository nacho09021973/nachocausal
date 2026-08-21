import HorizonFormal.NoTiesFiniteSample
import HorizonFormal.TupleSortMeasurable
import Mathlib.MeasureTheory.Group.Measure
import Mathlib.Probability.IdentDistrib
import Mathlib.Probability.UniformOn

/-!
# Uniformity of the sorting permutation of an iid atomless tuple

This file treats one finite iid family only.  It proves that Mathlib's actual
sorting permutation, including its definition on tuples with ties, has the
uniform law.  Atomlessness is used only to make the exact relabelling identity
valid almost surely; the random variable itself is not modified on the null
set of ties.
-/

namespace HorizonFormal

open Function MeasureTheory ProbabilityTheory
open scoped ENNReal

variable {n : ℕ}

local instance iidPermMeasurableSpace :
    MeasurableSpace (Equiv.Perm (Fin n)) := ⊤

/-- Relabelling an injective tuple by `σ` relabels its sorting permutation by
left multiplication with `σ⁻¹`.  Here `Equiv.trans` applies its left argument
first, so the displayed orientation sends an old sample label to its new
label. -/
theorem tupleSort_comp_perm_of_injective
    (u : Fin n → ℝ) (σ : Equiv.Perm (Fin n))
    (hu : Function.Injective u) :
    Tuple.sort (u ∘ σ) = (Tuple.sort u).trans σ.symm := by
  apply Equiv.ext
  intro r
  apply σ.injective
  apply hu
  have h := congr_fun
    (Tuple.comp_perm_comp_sort_eq_comp_sort (f := u) (σ := σ)) r
  simpa [Function.comp_apply] using h

/-- A left-invariant probability measure on a finite measurable group is the
uniform measure. -/
theorem finite_leftInvariant_probability_eq_uniform
    {G : Type*} [Group G] [Fintype G] [MeasurableSpace G]
    [MeasurableSingletonClass G] [MeasurableMul G]
    (m : Measure G) [IsProbabilityMeasure m] [m.IsMulLeftInvariant] :
    m = uniformOn (Set.univ : Set G) := by
  apply Measure.ext_of_singleton
  intro x
  rw [uniformOn_univ]
  simp only [Measure.count_singleton]
  have hsame : ∀ y : G, m {y} = m {1} := by
    intro y
    have h := measure_preimage_mul m y {y}
    simpa using h.symm
  have hsum :=
    sum_measure_singleton (μ := m) (s := (Finset.univ : Finset G))
  simp_rw [hsame] at hsum
  have hmass : m {1} * (Fintype.card G : ℝ≥0∞) = 1 := by
    simpa [mul_comm] using hsum
  rw [hsame x]
  simpa [ENNReal.div_eq_inv_mul] using
    ENNReal.eq_inv_of_mul_eq_one_left hmass

/-- The sorting permutation of a finite iid real tuple with atomless common
law is uniform on `Equiv.Perm (Fin n)`. -/
theorem iid_tupleSort_uniform
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {ν : Measure ℝ} [NoAtoms ν]
    (U : Ω → Fin n → ℝ)
    (hU_indep : iIndepFun (fun i ω => U ω i) μ)
    (hU_law : ∀ i, HasLaw (fun ω => U ω i) ν μ) :
    HasLaw
      (fun ω => Tuple.sort (U ω))
      (uniformOn (Set.univ : Set (Equiv.Perm (Fin n))))
      μ := by
  letI : IsProbabilityMeasure μ := hU_indep.isProbabilityMeasure
  have hU_vector :
      HasLaw U (Measure.pi (fun _ : Fin n => ν)) μ :=
    hU_indep.hasLaw_pi hU_law
  have hNoTies : ∀ᵐ ω ∂μ, Function.Injective (U ω) :=
    no_ties_finite_sample_ae hU_indep hU_law
  let S : Ω → Equiv.Perm (Fin n) := fun ω => Tuple.sort (U ω)
  let m : Measure (Equiv.Perm (Fin n)) := μ.map S
  have hS_aemeasurable : AEMeasurable S μ := by
    exact measurable_tupleSort.comp_aemeasurable hU_vector.aemeasurable
  have hS_law : HasLaw S m μ :=
    ⟨hS_aemeasurable, rfl⟩
  letI : IsProbabilityMeasure m :=
    hS_law.isProbabilityMeasure_iff.mp inferInstance
  letI : m.IsMulLeftInvariant := by
    refine ⟨?_⟩
    intro g
    let σ : Equiv.Perm (Fin n) := g.symm
    have h_relabel_indep :
        iIndepFun (fun i ω => U ω (σ i)) μ :=
      hU_indep.precomp σ.injective
    have h_relabel_law :
        ∀ i, HasLaw (fun ω => U ω (σ i)) ν μ :=
      fun i => hU_law (σ i)
    have h_relabel_vector :
        HasLaw (fun ω i => U ω (σ i))
          (Measure.pi (fun _ : Fin n => ν)) μ :=
      h_relabel_indep.hasLaw_pi h_relabel_law
    have h_vector_ident :
        IdentDistrib U (fun ω i => U ω (σ i)) μ μ :=
      hU_vector.identDistrib h_relabel_vector
    have h_sort_ident :
        IdentDistrib S
          (fun ω => Tuple.sort (fun i => U ω (σ i))) μ μ := by
      simpa [S, Function.comp_def] using
        h_vector_ident.comp measurable_tupleSort
    have h_sort_relabel_ae :
        (fun ω => Tuple.sort (fun i => U ω (σ i))) =ᵐ[μ]
          (fun ω => g * S ω) := by
      filter_upwards [hNoTies] with ω hω
      change Tuple.sort (U ω ∘ σ) = g * Tuple.sort (U ω)
      rw [tupleSort_comp_perm_of_injective (U ω) σ hω]
      change (Tuple.sort (U ω)).trans g = g * Tuple.sort (U ω)
      rfl
    have h_relabel_to_left :
        IdentDistrib
          (fun ω => Tuple.sort (fun i => U ω (σ i)))
          (fun ω => g * S ω) μ μ :=
      IdentDistrib.of_ae_eq h_sort_ident.aemeasurable_snd h_sort_relabel_ae
    have h_left_ident :
        IdentDistrib S (fun ω => g * S ω) μ μ :=
      h_sort_ident.trans h_relabel_to_left
    have h_left_law : HasLaw (fun ω => g * S ω) m μ :=
      h_left_ident.hasLaw hS_law
    have hg_measurable :
        Measurable (fun τ : Equiv.Perm (Fin n) => g * τ) :=
      measurable_of_finite _
    calc
      Measure.map (fun τ : Equiv.Perm (Fin n) => g * τ) m =
          Measure.map (fun τ : Equiv.Perm (Fin n) => g * τ)
            (Measure.map S μ) := rfl
      _ = Measure.map ((fun τ : Equiv.Perm (Fin n) => g * τ) ∘ S) μ :=
        AEMeasurable.map_map_of_aemeasurable
          hg_measurable.aemeasurable hS_aemeasurable
      _ = m := by
        simpa [Function.comp_def] using h_left_law.map_eq
  exact ⟨hS_aemeasurable, finite_leftInvariant_probability_eq_uniform m⟩

#print axioms HorizonFormal.tupleSort_comp_perm_of_injective
#print axioms HorizonFormal.finite_leftInvariant_probability_eq_uniform
#print axioms HorizonFormal.iid_tupleSort_uniform

end HorizonFormal
