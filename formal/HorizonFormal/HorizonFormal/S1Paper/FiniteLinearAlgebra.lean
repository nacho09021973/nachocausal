import Mathlib.Data.Real.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Symmetric
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.Pi

/-!
# Finite linear algebra core of Theorem C

This module formalizes the parts of the S1 paper's Theorem C (manuscript §4, Appendix B,
Appendix C) that are pure finite-dimensional linear algebra over `Fin N`, independent of
any poset / permutation structure:

* `EN N`, the subspace `𝟙^⊥ ⊆ (Fin N → ℝ)` (paper (3.11), Appendix B (B.1)), with its
  dimension `N - 1`.
* `DCSymM N`, the "doubly centered symmetric matrices" — the Lean model of `Sym(E_N)`
  (self-adjoint endomorphisms of `E_N`, extended by zero on `span {𝟙}`, per Appendix B
  (B.5)–(B.6)).
* `edgeLaplacian i j`, the edge Laplacian `(e_i - e_j)(e_i - e_j)ᵀ` (Appendix C (C.7)),
  proved linearly independent and spanning of `DCSymM N` via an *explicit reconstruction
  formula*, which is a direct route to Appendix C (C.8) that does not need the
  interval-cycle triangularization machinery.
* The identity-recovery inequality `1 - 2 s_N = ((N-3)^2+2)/6 > 0` for every `N ≥ 2`
  (Appendix C (C.18)–(C.20)), proved as a genuine `∀ N` statement — not a finite check.

What this module does **not** establish: that `edgeLaplacian`/the doubly-centered
symmetric matrix space is what the paper calls `A_C|_{E_N}` for an actual poset class
`C`. That bridge (interval cycles ↔ near-chain posets ↔ permutation fibers) is tracked
separately; see `ClaimMap.md` and `FORMALIZATION_STATUS.md`.
-/

namespace HorizonFormal.S1Paper

open scoped BigOperators
open Matrix

variable (N : ℕ)

/-! ## The sum functional and `E_N = 𝟙^⊥` -/

/-- The coordinate-sum functional on `Fin N → ℝ`. -/
def sumFn : (Fin N → ℝ) →ₗ[ℝ] ℝ where
  toFun v := ∑ i, v i
  map_add' x y := by simp [Finset.sum_add_distrib]
  map_smul' c x := by simp [Finset.mul_sum]

@[simp] lemma sumFn_apply (v : Fin N → ℝ) : sumFn N v = ∑ i, v i := rfl

/-- `E_N := 𝟙^⊥`, realized as the kernel of the coordinate-sum functional
(manuscript (3.11), Appendix B (B.1)). -/
def EN : Submodule ℝ (Fin N → ℝ) := LinearMap.ker (sumFn N)

lemma mem_EN {v : Fin N → ℝ} : v ∈ EN N ↔ ∑ i, v i = 0 := Iff.rfl

lemma sumFn_surjective (hN : 0 < N) : Function.Surjective (sumFn N) := by
  intro c
  refine ⟨Pi.single ⟨0, hN⟩ c, ?_⟩
  simp [sumFn_apply, Finset.sum_pi_single]

/-- `dim E_N = N - 1` for `N ≥ 1` (manuscript (3.11)/(B.1); the paper always has `N ≥ 2`). -/
theorem finrank_EN (hN : 0 < N) : Module.finrank ℝ (EN N) + 1 = N := by
  have hsurj : LinearMap.range (sumFn N) = ⊤ :=
    LinearMap.range_eq_top.mpr (sumFn_surjective N hN)
  have hrank := LinearMap.finrank_range_add_finrank_ker (sumFn N)
  rw [hsurj] at hrank
  have h1 : Module.finrank ℝ (⊤ : Submodule ℝ ℝ) = 1 := by simp
  have h2 : Module.finrank ℝ (Fin N → ℝ) = N := by
    simp [Module.finrank_pi]
  rw [h1] at hrank
  have : EN N = LinearMap.ker (sumFn N) := rfl
  rw [← this] at hrank
  omega

/-! ## Doubly-centered symmetric matrices, the Lean model of `Sym(E_N)` -/

/-- The Lean model of `Sym(E_N)`: symmetric matrices with vanishing row sums.
Since symmetry forces vanishing column sums too, this is exactly (the matrix picture of)
the self-adjoint endomorphisms of `E_N` extended by zero on `span {𝟙}`
(Appendix B (B.5)–(B.6)). -/
def DCSymM : Submodule ℝ (Matrix (Fin N) (Fin N) ℝ) where
  carrier := {M | M.IsSymm ∧ ∀ i, ∑ j, M i j = 0}
  zero_mem' := by
    constructor
    · simp [Matrix.IsSymm]
    · intro i; simp
  add_mem' := by
    rintro M M' ⟨hMs, hMr⟩ ⟨hM's, hM'r⟩
    refine ⟨?_, ?_⟩
    · simpa [Matrix.IsSymm, Matrix.transpose_add] using congrArg₂ (· + ·) hMs hM's
    · intro i; simp [Finset.sum_add_distrib, hMr i, hM'r i]
  smul_mem' := by
    rintro c M ⟨hMs, hMr⟩
    refine ⟨?_, ?_⟩
    · simpa [Matrix.IsSymm, Matrix.transpose_smul] using congrArg (c • ·) hMs
    · intro i
      simp only [Matrix.smul_apply, smul_eq_mul]
      rw [← Finset.mul_sum, hMr i, mul_zero]

lemma mem_DCSymM {M : Matrix (Fin N) (Fin N) ℝ} :
    M ∈ DCSymM N ↔ M.IsSymm ∧ ∀ i, ∑ j, M i j = 0 := Iff.rfl

/-! ## Edge Laplacians -/

/-- The `i`-th standard basis vector of `Fin N → ℝ`. -/
def stdVec (i : Fin N) : Fin N → ℝ := Pi.single i 1

/-- `e_i - e_j`. -/
def edgeVec (i j : Fin N) : Fin N → ℝ := stdVec N i - stdVec N j

@[simp] lemma edgeVec_apply (i j a : Fin N) :
    edgeVec N i j a = (if a = i then (1:ℝ) else 0) - (if a = j then (1:ℝ) else 0) := by
  simp [edgeVec, stdVec, Pi.single_apply]

lemma sum_edgeVec (i j : Fin N) : ∑ a, edgeVec N i j a = 0 := by
  simp [edgeVec, stdVec]

/-- The edge Laplacian `L_{ij} = (e_i - e_j)(e_i - e_j)ᵀ` (Appendix C (C.7)). -/
def edgeLaplacian (i j : Fin N) : Matrix (Fin N) (Fin N) ℝ :=
  fun a b => edgeVec N i j a * edgeVec N i j b

lemma edgeLaplacian_apply (i j a b : Fin N) :
    edgeLaplacian N i j a b = edgeVec N i j a * edgeVec N i j b := rfl

lemma edgeLaplacian_symm (i j : Fin N) : (edgeLaplacian N i j).IsSymm := by
  ext a b
  simp [edgeLaplacian_apply, Matrix.transpose_apply, mul_comm]

lemma edgeLaplacian_rowsum (i j a : Fin N) : ∑ b, edgeLaplacian N i j a b = 0 := by
  simp only [edgeLaplacian_apply, ← Finset.mul_sum]
  rw [sum_edgeVec]; ring

lemma edgeLaplacian_mem_DCSymM (i j : Fin N) : edgeLaplacian N i j ∈ DCSymM N :=
  ⟨edgeLaplacian_symm N i j, edgeLaplacian_rowsum N i j⟩

/-- Off-diagonal entries: `edgeLaplacian i j` is nonzero at `(a,b)`, `a ≠ b`, only when
`{a,b} = {i,j}`, in which case it equals `-1`. -/
lemma edgeLaplacian_offdiag (i j : Fin N) (hij : i ≠ j) (a b : Fin N) (hab : a ≠ b) :
    edgeLaplacian N i j a b = if (a = i ∧ b = j) ∨ (a = j ∧ b = i) then (-1:ℝ) else 0 := by
  simp only [edgeLaplacian_apply, edgeVec_apply]
  by_cases hai : a = i <;> by_cases haj : a = j <;> by_cases hbi : b = i <;> by_cases hbj : b = j <;>
    simp_all <;> ring

/-- Diagonal entries: `edgeLaplacian i j a a = 1` iff `a ∈ {i, j}`, for `i ≠ j`. -/
lemma edgeLaplacian_diag (i j : Fin N) (hij : i ≠ j) (a : Fin N) :
    edgeLaplacian N i j a a = if a = i ∨ a = j then (1:ℝ) else 0 := by
  simp only [edgeLaplacian_apply, edgeVec_apply]
  by_cases hai : a = i <;> by_cases haj : a = j <;> simp_all <;> ring

/-! ### Linear independence -/

/-- The family `{L_ij : i < j}` is linearly independent: reading off the `(i,j)` entry of a
vanishing combination isolates the coefficient of `L_ij` (Appendix C, the "its `(i,j)`
entry is `-w_{ij}`" argument). -/
theorem edgeLaplacian_linearIndependent :
    LinearIndependent ℝ
      (fun p : {p : Fin N × Fin N // p.1 < p.2} => edgeLaplacian N p.1.1 p.1.2) := by
  rw [linearIndependent_iff']
  intro s w hw p hp
  have hentry := congrFun (congrFun hw p.1.1) p.1.2
  simp only [Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul, Matrix.zero_apply] at hentry
  have hkey : ∀ q ∈ s, w q * edgeLaplacian N q.1.1 q.1.2 p.1.1 p.1.2
      = if q = p then -(w p) else 0 := by
    intro q _
    rcases eq_or_ne q p with rfl | hne
    · have hp1 : q.1.1 < q.1.2 := q.2
      rw [edgeLaplacian_offdiag N q.1.1 q.1.2 (ne_of_lt hp1) q.1.1 q.1.2 (ne_of_lt hp1)]
      simp
    · have hq1 : q.1.1 < q.1.2 := q.2
      have hp1 : p.1.1 < p.1.2 := p.2
      have hab : p.1.1 ≠ p.1.2 := ne_of_lt hp1
      rw [edgeLaplacian_offdiag N q.1.1 q.1.2 (ne_of_lt hq1) p.1.1 p.1.2 hab]
      have : ¬ ((p.1.1 = q.1.1 ∧ p.1.2 = q.1.2) ∨ (p.1.1 = q.1.2 ∧ p.1.2 = q.1.1)) := by
        rintro (⟨h1, h2⟩ | ⟨h1, h2⟩)
        · exact hne (Subtype.ext (Prod.ext h1.symm h2.symm))
        · omega
      simp [this, hne]
  rw [Finset.sum_congr rfl hkey, Finset.sum_ite_eq' s p (fun _ => -(w p)), if_pos hp] at hentry
  have : -(w p) = 0 := hentry
  linarith

/-! ### Spanning, via explicit reconstruction -/

/-- Converts a sum over the subtype `{p : Fin N × Fin N // p.1 < p.2}` into an ordinary
double `Finset.sum` guarded by an `if i < j`. Purely bookkeeping. -/
private lemma sum_subtype_lt_eq_sum_sum {V : Type*} [AddCommMonoid V] (f : Fin N → Fin N → V) :
    (∑ p : {p : Fin N × Fin N // p.1 < p.2}, f p.1.1 p.1.2)
      = ∑ i, ∑ j, if i < j then f i j else 0 := by
  classical
  have h1 : (∑ p : {p : Fin N × Fin N // p.1 < p.2}, f p.1.1 p.1.2)
      = ∑ q ∈ Finset.univ.filter (fun q : Fin N × Fin N => q.1 < q.2), f q.1 q.2 :=
    (Finset.sum_subtype (Finset.univ.filter (fun q : Fin N × Fin N => q.1 < q.2))
      (by simp) (fun q => f q.1 q.2)).symm
  have h2 : (∑ q ∈ Finset.univ.filter (fun q : Fin N × Fin N => q.1 < q.2), f q.1 q.2)
      = ∑ q : Fin N × Fin N, if q.1 < q.2 then f q.1 q.2 else 0 :=
    Finset.sum_filter (fun q : Fin N × Fin N => q.1 < q.2) (fun q => f q.1 q.2)
  have h3 : (∑ q : Fin N × Fin N, if q.1 < q.2 then f q.1 q.2 else 0)
      = ∑ i, ∑ j, if i < j then f i j else 0 :=
    Finset.sum_product' (f := fun i j => if i < j then f i j else 0) Finset.univ Finset.univ
  rw [h1, h2, h3]

/-- Every doubly-centered symmetric matrix is *exactly* reconstructed from its off-diagonal
entries via the edge Laplacians: `M = ∑_{i<j} (-M_{ij}) • L_{ij}`. This directly proves
`{L_ij}` spans `Sym(E_N)` and is the Lean route to Appendix C (C.8) (the paper's argument
via a dimension count is bypassed by this explicit identity). -/
theorem DCSymM_eq_sum_edgeLaplacian {M : Matrix (Fin N) (Fin N) ℝ} (hM : M ∈ DCSymM N) :
    M = ∑ p : {p : Fin N × Fin N // p.1 < p.2}, (-(M p.1.1 p.1.2)) • edgeLaplacian N p.1.1 p.1.2 := by
  classical
  obtain ⟨hsymm, hrow⟩ := hM
  have hMsymm : ∀ i j, M i j = M j i := by
    intro i j; have := congrFun (congrFun hsymm.symm i) j; simpa [Matrix.transpose_apply] using this
  ext a b
  simp only [Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul]
  rw [sum_subtype_lt_eq_sum_sum N
    (fun i j => (-(M i j)) * edgeLaplacian N i j a b)]
  rcases eq_or_ne a b with rfl | hab
  · -- Diagonal case: rewrite each term via `edgeLaplacian_diag`, then split the "a = i ∨ a = j"
    -- disjunction (valid: for `i < j` they cannot both hold) and collapse each half separately.
    have step : (∑ i, ∑ j, if i < j then (-(M i j)) * edgeLaplacian N i j a a else 0)
        = (∑ i, ∑ j, if i < j ∧ a = i then (-(M i j)) else 0)
            + (∑ i, ∑ j, if i < j ∧ a = j then (-(M i j)) else 0) := by
      rw [← Finset.sum_add_distrib]
      congr 1; funext i
      rw [← Finset.sum_add_distrib]
      congr 1; funext j
      by_cases hij : i < j
      · rw [edgeLaplacian_diag N i j (ne_of_lt hij) a]
        by_cases hai : a = i
        · by_cases haj : a = j
          · exact absurd (hai.symm.trans haj) (ne_of_lt hij)
          · simp [hij, hai, haj, hij.ne, hij.ne']
        · by_cases haj : a = j
          · simp [hij, hai, haj, hij.ne, hij.ne']
          · simp [hij, hai, haj, hij.ne, hij.ne']
      · simp [hij]
    rw [step]
    have hterm1 : (∑ i, ∑ j, if i < j ∧ a = i then (-(M i j)) else 0)
        = ∑ j, if a < j then (-(M a j)) else 0 := by
      have : ∀ i, (∑ j, if i < j ∧ a = i then (-(M i j)) else 0)
          = if a = i then (∑ j, if i < j then (-(M i j)) else 0) else 0 := by
        intro i; by_cases hai : a = i <;> simp [hai]
      rw [Finset.sum_congr rfl (fun i _ => this i)]
      simp
    have hterm2 : (∑ i, ∑ j, if i < j ∧ a = j then (-(M i j)) else 0)
        = ∑ i, if i < a then (-(M i a)) else 0 := by
      rw [Finset.sum_comm]
      have : ∀ j, (∑ i, if i < j ∧ a = j then (-(M i j)) else 0)
          = if a = j then (∑ i, if i < j then (-(M i j)) else 0) else 0 := by
        intro j; by_cases haj : a = j <;> simp [haj]
      rw [Finset.sum_congr rfl (fun j _ => this j)]
      simp
    rw [hterm1, hterm2]
    -- Rewrite `∑_{i<a} -(M i a)` via symmetry as `∑_{i<a} -(M a i)`, then combine both
    -- sums into a single `∑_k, if k ≠ a then -(M a k) else 0` and split off the `k = a`
    -- term of the (zero) row sum.
    have hswap : (∑ i, if i < a then (-(M i a)) else 0) = ∑ i, if i < a then (-(M a i)) else 0 :=
      Finset.sum_congr rfl (fun i _ => by rw [hMsymm i a])
    rw [hswap, ← Finset.sum_add_distrib]
    have hcollapse : ∀ k, (if a < k then (-(M a k)) else 0) + (if k < a then (-(M a k)) else 0)
        = if k ≠ a then (-(M a k)) else 0 := by
      intro k
      rcases lt_trichotomy a k with h | h | h
      · have h1 : k ≠ a := (ne_of_lt h).symm
        have h2 : ¬ k < a := not_lt_of_gt h
        simp [h, h1, h2]
      · simp [h]
      · have h1 : k ≠ a := ne_of_lt h
        have h2 : ¬ a < k := not_lt_of_gt h
        simp [h, h1, h2]
    rw [Finset.sum_congr rfl (fun k _ => hcollapse k)]
    have hsplit : (∑ k, M a k) = M a a + ∑ k, if k ≠ a then M a k else 0 := by
      have e : (∑ k, M a k)
          = ∑ k, ((if k = a then M a k else 0) + (if k ≠ a then M a k else 0)) := by
        apply Finset.sum_congr rfl
        intro k _
        by_cases h : k = a <;> simp [h]
      rw [e, Finset.sum_add_distrib]
      congr 1
      simp
    have hne : (∑ k, if k ≠ a then (-(M a k)) else 0) = -(∑ k, if k ≠ a then M a k else 0) := by
      rw [← Finset.sum_neg_distrib]
      apply Finset.sum_congr rfl
      intro k _
      by_cases h : k ≠ a <;> simp [h]
    have hval : (∑ k, if k ≠ a then M a k else 0) = -(M a a) := by
      have h0 := hsplit
      rw [hrow a] at h0
      linarith
    rw [hne, hval]
    ring
  · -- Off-diagonal case: the double sum collapses to a single surviving pair.
    have step : (∑ i, ∑ j, if i < j then (-(M i j)) * edgeLaplacian N i j a b else 0)
        = (∑ i, ∑ j, if i < j ∧ a = i ∧ b = j then M i j else 0)
            + (∑ i, ∑ j, if i < j ∧ a = j ∧ b = i then M i j else 0) := by
      rw [← Finset.sum_add_distrib]
      congr 1; funext i
      rw [← Finset.sum_add_distrib]
      congr 1; funext j
      by_cases hij : i < j
      · rw [edgeLaplacian_offdiag N i j (ne_of_lt hij) a b hab]
        by_cases hai : a = i
        · by_cases hbj : b = j
          · by_cases haj : a = j
            · exact absurd (hai.symm.trans haj) (ne_of_lt hij)
            · simp [hij, hai, hbj, haj, hij.ne, hij.ne']
          · by_cases hbi : b = i
            · exact absurd (hai.trans hbi.symm) hab
            · simp [hij, hai, hbj, hbi, hij.ne, hij.ne']
        · by_cases haj : a = j
          · by_cases hbi : b = i
            · simp [hij, hai, haj, hbi, hij.ne, hij.ne']
            · simp [hij, hai, haj, hbi, hij.ne, hij.ne']
          · simp [hij, hai, haj, hij.ne, hij.ne']
      · simp [hij]
    rw [step]
    have hterm1 : (∑ i, ∑ j, if i < j ∧ a = i ∧ b = j then M i j else 0)
        = if a < b then M a b else 0 := by
      have hstep1 : ∀ i, (∑ j, if i < j ∧ a = i ∧ b = j then M i j else 0)
          = if a = i then (∑ j, if i < j ∧ b = j then M i j else 0) else 0 := by
        intro i; by_cases hai : a = i <;> simp [hai]
      rw [Finset.sum_congr rfl (fun i _ => hstep1 i)]
      simp only [Finset.sum_ite_eq, Finset.mem_univ, if_true]
      have hstep2 : (∑ j, if a < j ∧ b = j then M a j else 0) = if a < b then M a b else 0 := by
        have : ∀ j, (if a < j ∧ b = j then M a j else 0) = (if b = j then (if a < j then M a j else 0) else 0) := by
          intro j; by_cases hbj : b = j <;> simp [hbj]
        rw [Finset.sum_congr rfl (fun j _ => this j)]
        simp
      exact hstep2
    have hterm2 : (∑ i, ∑ j, if i < j ∧ a = j ∧ b = i then M i j else 0)
        = if b < a then M a b else 0 := by
      rw [Finset.sum_comm]
      have hstep1 : ∀ j, (∑ i, if i < j ∧ a = j ∧ b = i then M i j else 0)
          = if a = j then (∑ i, if i < j ∧ b = i then M i j else 0) else 0 := by
        intro j; by_cases haj : a = j <;> simp [haj]
      rw [Finset.sum_congr rfl (fun j _ => hstep1 j)]
      simp only [Finset.sum_ite_eq, Finset.mem_univ, if_true]
      have hstep2 : (∑ i, if i < a ∧ b = i then M i a else 0) = if b < a then M a b else 0 := by
        have : ∀ i, (if i < a ∧ b = i then M i a else 0) = (if b = i then (if i < a then M i a else 0) else 0) := by
          intro i; by_cases hbi : b = i <;> simp [hbi]
        rw [Finset.sum_congr rfl (fun i _ => this i)]
        simp only [Finset.sum_ite_eq, Finset.mem_univ, if_true]
        rw [hMsymm b a]
      exact hstep2
    rw [hterm1, hterm2]
    rcases lt_or_gt_of_ne hab with h | h
    · simp [h, not_lt_of_gt h]
    · simp [h, not_lt_of_gt h]

/-! ## Identity recovery (Appendix C (C.17)–(C.20))

The paper's route to `span{S_{a,b}} = Sym(E_N)` (as opposed to the direct
reconstruction route via edge Laplacians above) goes through the near-chain/interval-
cycle family `Q_{a,b}`, and needs the coefficient sum `s_N` in `I_{E_N} = ∑ c_{a,b}
Q_{a,b}` to satisfy `1 - 2 s_N ≠ 0`. This section certifies exactly that non-vanishing,
as its own `∀ N` statement (not a finite check), independently of which spanning route
is used for the main theorem above. -/

/-- The coefficient sum `s_N = (N-1)(5-N)/12` from Appendix C (C.18). -/
noncomputable def sN (N : ℕ) : ℝ := ((N : ℝ) - 1) * (5 - (N : ℝ)) / 12

/-- The algebraic identity `1 - 2 s_N = ((N-3)^2+2)/6` (Appendix C (C.20), first
equality). -/
theorem one_sub_two_sN_eq (N : ℕ) : 1 - 2 * sN N = (((N : ℝ) - 3) ^ 2 + 2) / 6 := by
  unfold sN; ring

/-- **Identity recovery, non-vanishing for every `N`** (Appendix C (C.18)–(C.20)):
`1 - 2 s_N` never vanishes — indeed it is strictly positive for every natural number
`N`, not merely checked at finitely many values. This is exactly the fact the paper
needs to solve for `I_{E_N}` in terms of the `S_{a,b}` after substituting
`Q_{a,b} = 2 I_{E_N} - S_{a,b}`. -/
theorem one_sub_two_sN_pos (N : ℕ) : 0 < 1 - 2 * sN N := by
  rw [one_sub_two_sN_eq]
  positivity
