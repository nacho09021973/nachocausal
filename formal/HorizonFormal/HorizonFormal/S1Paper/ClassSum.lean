import HorizonFormal.S1Paper.Fiber
import Mathlib.Data.Real.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Symmetric
import Mathlib.LinearAlgebra.Span.Basic

/-!
# Class sums of the near-chain family: manuscript (3.12) and (C.11)

With the fiber lemma `fiber_eq` (Appendix C (C.5)) in hand, the class sum
`A_C = Σ_{σ∈Γ_C} P_σ` of the near-chain class `C_{a,b}` can be *computed*, and the
manuscript's (C.11) — `S_{a,b} = P_τ + P_τᵀ` equals `2A_{C_{a,b}}` when `b = a+1` and
`A_{C_{a,b}}` otherwise — becomes a theorem rather than an assumption.

This closes the poset half of `CLASS_SUM_TO_POSET_BRIDGE`: the matrices Appendix C
manipulates really are nonzero multiples of the class sums of genuine unlabeled
two-dimensional poset classes.
-/

namespace HorizonFormal.S1Paper

open Finset Matrix

variable {N : ℕ}

/-- Permutation matrix in the manuscript's convention (3.12): `P_σ = Σ_i e_i e_{σ(i)}ᵀ`. -/
def permM (σ : Equiv.Perm (Fin N)) : Matrix (Fin N) (Fin N) ℝ :=
  Matrix.of fun i j => if σ i = j then 1 else 0

/-- `P_σᵀ = P_{σ⁻¹}` — the matrix form of the fiber's closure under inversion (§3 (3.8)). -/
lemma permM_transpose (σ : Equiv.Perm (Fin N)) : (permM σ)ᵀ = permM σ⁻¹ := by
  ext i j
  show (if σ j = i then (1:ℝ) else 0) = (if σ⁻¹ i = j then 1 else 0)
  by_cases h : σ j = i
  · rw [if_pos h, if_pos (show σ⁻¹ i = j by rw [← h]; simp)]
  · rw [if_neg h, if_neg (fun hc => h (by rw [← hc]; simp))]

/-- The fiber `Γ_C := {σ : [P_σ] = C}` of the class of `P_τ` (manuscript §2, §3). -/
def fiber (τ : Equiv.Perm (Fin N)) : Finset (Equiv.Perm (Fin N)) :=
  univ.filter (fun σ => PosetIsomorphic σ τ)

/-- The class sum `A_C := Σ_{σ∈Γ_C} P_σ` (manuscript (3.12)). -/
noncomputable def classSum (τ : Equiv.Perm (Fin N)) : Matrix (Fin N) (Fin N) ℝ :=
  ∑ σ ∈ fiber τ, permM σ

/-- The symmetrized interval cycle `S_{a,b} := P_{τ_{a,b}} + P_{τ_{a,b}}ᵀ` (C.10). -/
noncomputable def Sab (a b : Fin N) (hab : a < b) : Matrix (Fin N) (Fin N) ℝ :=
  permM (tau a b hab) + (permM (tau a b hab))ᵀ

/-- The fiber of the near-chain class, as a `Finset` — (C.5) in computational form. -/
theorem fiber_almostChain (a b : Fin N) (hab : a < b) :
    fiber (tau a b hab) = {tau a b hab, (tau a b hab)⁻¹} := by
  ext σ
  simp only [fiber, mem_filter, mem_univ, true_and, Finset.mem_insert, Finset.mem_singleton]
  exact fiber_eq a b hab σ

/-- **(C.11), non-adjacent case**: `S_{a,b} = A_{C_{a,b}}` for `b > a+1`. -/
theorem Sab_eq_classSum (a b : Fin N) (hab : a < b) (hna : b.val ≠ a.val + 1) :
    Sab a b hab = classSum (tau a b hab) := by
  rw [classSum, fiber_almostChain, Finset.sum_pair (tau_ne_inv_of_not_adjacent a b hab hna),
    Sab, permM_transpose]

/-- **(C.11), adjacent case**: `S_{a,a+1} = 2 A_{C_{a,a+1}}` — the fiber is a single
transposition, without multiplicity. -/
theorem Sab_eq_two_classSum (a b : Fin N) (hab : a < b) (hadj : b.val = a.val + 1) :
    Sab a b hab = (2 : ℝ) • classSum (tau a b hab) := by
  have h := tau_self_inv_of_adjacent a b hab hadj
  have hf : fiber (tau a b hab) = {tau a b hab} := by
    rw [fiber_almostChain, ← h, Finset.insert_eq_self.mpr (Finset.mem_singleton_self _)]
  rw [classSum, hf, Finset.sum_singleton, Sab, permM_transpose, ← h, two_smul]

/-- **(C.11) in the form the span argument actually uses**: `S_{a,b}` is a *nonzero*
scalar multiple of the class sum `A_{C_{a,b}}` in both cases. -/
theorem Sab_nonzero_smul_classSum (a b : Fin N) (hab : a < b) :
    ∃ c : ℝ, c ≠ 0 ∧ Sab a b hab = c • classSum (tau a b hab) := by
  by_cases hadj : b.val = a.val + 1
  · exact ⟨2, two_ne_zero, Sab_eq_two_classSum a b hab hadj⟩
  · exact ⟨1, one_ne_zero, by rw [one_smul]; exact Sab_eq_classSum a b hab hadj⟩

/-- Hence the symmetrized interval cycle and the class sum span the same line: whatever
Appendix C proves about `span{S_{a,b}}` transfers verbatim to `span{A_{C_{a,b}}}`. -/
theorem span_Sab_eq_span_classSum (a b : Fin N) (hab : a < b) :
    Submodule.span ℝ {Sab a b hab} = Submodule.span ℝ {classSum (tau a b hab)} := by
  obtain ⟨c, hc, hEq⟩ := Sab_nonzero_smul_classSum a b hab
  rw [hEq, Submodule.span_singleton_smul_eq (IsUnit.mk0 c hc)]

end HorizonFormal.S1Paper
