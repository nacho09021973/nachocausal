import HorizonFormal.S1Paper.FiniteLinearAlgebra

/-!
# Restriction to `E_N`, the identity `I_{E_N}`, and the edge-Laplacian span

Appendix C works with operators *restricted to* `E_N = 𝟙^⊥`. In the `DCSymM` model of
`Sym(E_N)` used by `FiniteLinearAlgebra.lean`, that restriction is conjugation by the
orthogonal projection `cproj = I - N⁻¹J` onto `E_N`, and `I_{E_N}` is `cproj` itself.

This module supplies exactly what Appendix C's matrix half needs and nothing more:

* `cproj` (`= I_{E_N}`) and `restr M = cproj * M * cproj` (`= M|_{E_N}`);
* `restr` fixes `DCSymM` and lands in `DCSymM` on symmetric inputs;
* `span_LSet` : `span {L_{ij} : i<j} = DCSymM N`, i.e. (C.8);
* `cproj_eq_sum_edgeLaplacian` : `I_{E_N} = N⁻¹ ∑_{i<j} L_{ij}`, i.e. (C.9) in the
  form the identity-recovery step actually consumes.

No new notion of matrix, restriction or span is introduced: `DCSymM` and
`edgeLaplacian` are the ones already certified in `FiniteLinearAlgebra.lean`.
-/

namespace HorizonFormal.S1Paper

open scoped BigOperators
open Matrix Finset

variable (N : ℕ)

/-- The all-ones matrix `J`. -/
def onesM : Matrix (Fin N) (Fin N) ℝ := fun _ _ => 1

/-- `I_{E_N}`: the matrix of the orthogonal projection of `ℝ^N` onto `E_N = 𝟙^⊥`.
This is the manuscript's `I_{E_N}` in the `DCSymM` picture. -/
noncomputable def cproj : Matrix (Fin N) (Fin N) ℝ := 1 - (N:ℝ)⁻¹ • onesM N

lemma cproj_apply (i j : Fin N) :
    cproj N i j = (if i = j then (1:ℝ) else 0) - (N:ℝ)⁻¹ := by
  simp [cproj, onesM, Matrix.one_apply, Matrix.sub_apply, Matrix.smul_apply]

lemma cproj_symm : (cproj N).IsSymm := by
  ext i j
  simp only [Matrix.transpose_apply, cproj_apply]
  congr 1
  by_cases h : i = j
  · simp [h]
  · simp [h, Ne.symm h]

lemma cproj_rowsum (hN : N ≠ 0) (i : Fin N) : ∑ j, cproj N i j = 0 := by
  have hNR : (N:ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hN
  simp only [cproj_apply, Finset.sum_sub_distrib, Finset.sum_ite_eq, Finset.mem_univ, if_true,
    Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  rw [mul_inv_cancel₀ hNR, sub_self]

lemma cproj_mem_DCSymM (hN : N ≠ 0) : cproj N ∈ DCSymM N :=
  ⟨cproj_symm N, cproj_rowsum N hN⟩

/-- Column sums of a `DCSymM` matrix vanish too (symmetry). -/
lemma DCSymM_colsum {M : Matrix (Fin N) (Fin N) ℝ} (hM : M ∈ DCSymM N) (j : Fin N) :
    ∑ k, M k j = 0 := by
  obtain ⟨hs, hr⟩ := hM
  have hsymm : ∀ a b, M a b = M b a := fun a b => by
    have := congrFun (congrFun hs.symm a) b
    simpa [Matrix.transpose_apply] using this
  rw [Finset.sum_congr rfl (fun k _ => hsymm k j)]
  exact hr j

/-- `cproj` acts as the identity on `DCSymM` from the left. -/
lemma cproj_mul_of_mem {M : Matrix (Fin N) (Fin N) ℝ} (hM : M ∈ DCSymM N) :
    cproj N * M = M := by
  ext i j
  simp only [Matrix.mul_apply, cproj_apply, sub_mul]
  rw [Finset.sum_sub_distrib]
  have h1 : ∑ k, (if i = k then (1:ℝ) else 0) * M k j = M i j := by
    simp [ite_mul]
  have h2 : ∑ k, (N:ℝ)⁻¹ * M k j = 0 := by
    rw [← Finset.mul_sum, DCSymM_colsum N hM j, mul_zero]
  rw [h1, h2, sub_zero]

/-- `cproj` acts as the identity on `DCSymM` from the right. -/
lemma mul_cproj_of_mem {M : Matrix (Fin N) (Fin N) ℝ} (hM : M ∈ DCSymM N) :
    M * cproj N = M := by
  ext i j
  simp only [Matrix.mul_apply, cproj_apply, mul_sub]
  rw [Finset.sum_sub_distrib]
  have h1 : ∑ k, M i k * (if k = j then (1:ℝ) else 0) = M i j := by
    simp [mul_ite]
  have h2 : ∑ k, M i k * (N:ℝ)⁻¹ = 0 := by
    rw [← Finset.sum_mul, hM.2 i, zero_mul]
  rw [h1, h2, sub_zero]

/-- `M|_{E_N}`, the restriction of a matrix to `E_N`, as a matrix again. -/
noncomputable def restr (M : Matrix (Fin N) (Fin N) ℝ) : Matrix (Fin N) (Fin N) ℝ :=
  cproj N * M * cproj N

lemma restr_add (M M' : Matrix (Fin N) (Fin N) ℝ) :
    restr N (M + M') = restr N M + restr N M' := by
  simp [restr, Matrix.mul_add, Matrix.add_mul]

lemma restr_sub (M M' : Matrix (Fin N) (Fin N) ℝ) :
    restr N (M - M') = restr N M - restr N M' := by
  simp [restr, Matrix.mul_sub, Matrix.sub_mul]

lemma restr_smul (c : ℝ) (M : Matrix (Fin N) (Fin N) ℝ) :
    restr N (c • M) = c • restr N M := by
  simp [restr]

/-- On `Sym(E_N)` the restriction is the identity — nothing is lost. -/
lemma restr_eq_self {M : Matrix (Fin N) (Fin N) ℝ} (hM : M ∈ DCSymM N) : restr N M = M := by
  rw [restr, cproj_mul_of_mem N hM, mul_cproj_of_mem N hM]

lemma restr_one (hN : N ≠ 0) : restr N 1 = cproj N := by
  rw [restr, Matrix.mul_one, cproj_mul_of_mem N (cproj_mem_DCSymM N hN)]

/-- Rows of anything times `cproj` sum to zero. -/
lemma mul_cproj_rowsum (hN : N ≠ 0) (A : Matrix (Fin N) (Fin N) ℝ) (i : Fin N) :
    ∑ j, (A * cproj N) i j = 0 := by
  simp only [Matrix.mul_apply]
  rw [Finset.sum_comm]
  have : ∀ k, ∑ j, A i k * cproj N k j = 0 := by
    intro k; rw [← Finset.mul_sum, cproj_rowsum N hN k, mul_zero]
  simp [this]

/-- The restriction of a symmetric matrix lies in `Sym(E_N)`. -/
lemma restr_mem_DCSymM (hN : N ≠ 0) {M : Matrix (Fin N) (Fin N) ℝ} (hM : M.IsSymm) :
    restr N M ∈ DCSymM N := by
  refine ⟨?_, ?_⟩
  · show (restr N M)ᵀ = restr N M
    unfold restr
    rw [Matrix.transpose_mul, Matrix.transpose_mul,
      show (cproj N)ᵀ = cproj N from cproj_symm N, show Mᵀ = M from hM, Matrix.mul_assoc]
  · intro i
    exact mul_cproj_rowsum N hN (cproj N * M) i

/-! ## The edge-Laplacian span, (C.8) and (C.9) -/

/-- The generating family `{L_{ij} : i<j}` of (C.7), as a set of matrices. -/
def LSet : Set (Matrix (Fin N) (Fin N) ℝ) :=
  {M | ∃ i j : Fin N, i < j ∧ M = edgeLaplacian N i j}

/-- **(C.8)**: the edge Laplacians span `Sym(E_N)` exactly. The reverse inclusion reuses
the explicit reconstruction already certified in `FiniteLinearAlgebra.lean`. -/
theorem span_LSet : Submodule.span ℝ (LSet N) = DCSymM N := by
  apply le_antisymm
  · rw [Submodule.span_le]
    rintro M ⟨i, j, -, rfl⟩
    exact edgeLaplacian_mem_DCSymM N i j
  · intro M hM
    rw [DCSymM_eq_sum_edgeLaplacian N hM]
    refine Submodule.sum_mem _ (fun p _ => Submodule.smul_mem _ _ ?_)
    exact Submodule.subset_span ⟨p.1.1, p.1.2, p.2, rfl⟩

/-- **(C.9)** in the form the identity-recovery step consumes: `I_{E_N}` is the uniform
combination `N⁻¹ ∑_{i<j} L_{ij}` of the edge Laplacians. Obtained from the certified
reconstruction theorem by reading off `cproj`'s off-diagonal entries. -/
theorem cproj_eq_sum_edgeLaplacian (hN : N ≠ 0) :
    cproj N
      = ∑ p : {p : Fin N × Fin N // p.1 < p.2}, ((N:ℝ)⁻¹) • edgeLaplacian N p.1.1 p.1.2 := by
  have h := DCSymM_eq_sum_edgeLaplacian N (cproj_mem_DCSymM N hN)
  rw [h]
  refine Finset.sum_congr rfl (fun p _ => ?_)
  have hne : p.1.1 ≠ p.1.2 := ne_of_lt p.2
  have hcoef : -((0:ℝ) - (N:ℝ)⁻¹) = (N:ℝ)⁻¹ := by ring
  rw [cproj_apply, if_neg hne, hcoef]

end HorizonFormal.S1Paper
