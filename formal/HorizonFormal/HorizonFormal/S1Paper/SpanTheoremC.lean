import HorizonFormal.S1Paper.CycleLaplacian
import HorizonFormal.S1Paper.Fiber
import Mathlib.LinearAlgebra.Basis.Defs
import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition

/-!
# Appendix C (C.15)–(C.21) and the finite matrix form of Theorem C

This closes the matrix half of Theorem C:

* `edgeLaplacian_eq_Qcomb` — the triangular inversion (C.15), *algebraically* from
  (C.13)–(C.14), with the explicit coefficient vector `wInv i j`;
* `span_QSet` — (C.16);
* `cproj_eq_Qcomb_cCoef` — (C.17) with `cCoef` **built** from (C.9) and (C.15), not
  obtained from an existential;
* `coeffSum_cCoef_eq_sN` — (C.18): the sum of *those* coefficients really is `s_N`;
* `identity_elimination` — (C.19), and `span_SSet` — (C.21);
* `span_classSum_restr_eq` — the target,
  `span {A_C|_{E_N} : C ∈ 𝒞_N} = Sym(E_N)`.

Coefficients are carried as functions `Fin N × Fin N → ℝ` supported on the pairs `x < y`
(`Qmat` is `0` off that set, so junk indices never contribute to a matrix; and the
support lemma `cCoef_eq_zero_of_not_lt` keeps them out of the coefficient *sum* too).
-/

namespace HorizonFormal.S1Paper

open scoped BigOperators
open Matrix Finset

variable {N : ℕ}

/-! ## Bookkeeping -/

/-- Bridge between the `{p // p.1 < p.2}` indexing used by `FiniteLinearAlgebra.lean` and
the plain product indexing used here. -/
lemma sum_pair_subtype_eq {M : Type*} [AddCommMonoid M] (f : Fin N → Fin N → M) :
    (∑ p : {p : Fin N × Fin N // p.1 < p.2}, f p.1.1 p.1.2)
      = ∑ p : Fin N × Fin N, if p.1 < p.2 then f p.1 p.2 else 0 := by
  classical
  rw [← Finset.sum_filter]
  exact (Finset.sum_subtype (Finset.univ.filter (fun q : Fin N × Fin N => q.1 < q.2))
    (fun x => by simp) (fun q : Fin N × Fin N => f q.1 q.2)).symm

lemma card_filter_val_Ico (i j : Fin N) (hij : i.val ≤ j.val) :
    (Finset.univ.filter (fun x : Fin N => i.val ≤ x.val ∧ x.val < j.val)).card
      = j.val - i.val := by
  classical
  have hkey := Finset.filter_card_add_filter_neg_card_eq_card
    (s := Finset.univ.filter (fun x : Fin N => x.val < j.val))
    (p := fun x : Fin N => x.val < i.val)
  have e1 : (Finset.univ.filter (fun x : Fin N => x.val < j.val)).filter
      (fun x : Fin N => x.val < i.val)
      = Finset.univ.filter (fun x : Fin N => x.val < i.val) := by
    ext x
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    omega
  have e2 : (Finset.univ.filter (fun x : Fin N => x.val < j.val)).filter
      (fun x : Fin N => ¬ x.val < i.val)
      = Finset.univ.filter (fun x : Fin N => i.val ≤ x.val ∧ x.val < j.val) := by
    ext x
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    omega
  rw [e1, e2, card_filter_val_lt, card_filter_val_lt] at hkey
  omega

/-- Collapsing the `y`-sum over the adjacency condition `y = x+1`: for each `x` in range
there is exactly one admissible `y`, namely `nextF x`. -/
lemma sum_adjacent_collapse {M : Type*} [AddCommMonoid M] (i j : Fin N)
    (F : Fin N → Fin N → M) :
    (∑ x : Fin N, ∑ y : Fin N,
        (if y.val = x.val + 1 ∧ i.val ≤ x.val ∧ x.val < j.val then F x y else 0))
      = ∑ x : Fin N, (if i.val ≤ x.val ∧ x.val < j.val then F x (nextF x) else 0) := by
  classical
  refine Finset.sum_congr rfl (fun x _ => ?_)
  by_cases hP : i.val ≤ x.val ∧ x.val < j.val
  · have hjN := j.isLt
    have hxN : x.val + 1 < N := by omega
    have hnext : (nextF x).val = x.val + 1 := nextF_val hxN
    rw [if_pos hP]
    have hcollapse := Finset.sum_eq_single (s := (Finset.univ : Finset (Fin N)))
      (f := fun y : Fin N =>
        if y.val = x.val + 1 ∧ i.val ≤ x.val ∧ x.val < j.val then F x y else 0)
      (nextF x)
      (fun y _ hy => if_neg (by
        have hyv : y.val ≠ x.val + 1 := fun hcon => hy (Fin.ext (by omega))
        tauto))
      (fun hmem => absurd (Finset.mem_univ (nextF x)) hmem)
    rw [hcollapse, if_pos ⟨hnext, hP.1, hP.2⟩]
  · rw [if_neg hP]
    exact Finset.sum_eq_zero (fun y _ => if_neg (by tauto))

/-! ## The coefficient calculus -/

/-- A finite combination of the `Q_{a,b}`. -/
noncomputable def Qcomb (c : Fin N × Fin N → ℝ) : Matrix (Fin N) (Fin N) ℝ :=
  ∑ p : Fin N × Fin N, c p • Qmat p.1 p.2

/-- The total coefficient mass, the quantity (C.18) is about. -/
noncomputable def coeffSum (c : Fin N × Fin N → ℝ) : ℝ := ∑ p : Fin N × Fin N, c p

lemma Qcomb_mem_span (c : Fin N × Fin N → ℝ) (S : Submodule ℝ (Matrix (Fin N) (Fin N) ℝ))
    (hS : ∀ x y : Fin N, Qmat x y ∈ S) : Qcomb c ∈ S :=
  Submodule.sum_mem _ (fun p _ => Submodule.smul_mem _ _ (hS p.1 p.2))

/-! ## (C.15): the triangular inversion -/

/-- The coefficient vector realizing (C.15): `L_{ij} = Q_{i,j} - ½ ∑_{k∈[i,j)} Q_{k,k+1}`.
For `j = i+1` the two terms collide and it degenerates to `L = ½ Q`, exactly the
manuscript's first inversion formula. -/
noncomputable def wInv (i j : Fin N) : Fin N × Fin N → ℝ := fun p =>
  (if p = (i, j) then (1:ℝ) else 0)
    - (if p.2.val = p.1.val + 1 ∧ i.val ≤ p.1.val ∧ p.1.val < j.val then (1/2 : ℝ) else 0)

lemma wInv_eq_zero_of_not_lt {i j : Fin N} (hij : i < j) {p : Fin N × Fin N}
    (h : ¬ p.1 < p.2) : wInv i j p = 0 := by
  rw [wInv, if_neg (by rintro rfl; exact h hij),
    if_neg (by rintro ⟨h1, -, -⟩; exact h (by rw [Fin.lt_def]; omega))]
  ring

/-- **(C.15)**: the edge Laplacians are recovered from the `Q`'s, algebraically. -/
theorem edgeLaplacian_eq_Qcomb (i j : Fin N) (hij : i < j) :
    Qcomb (wInv i j) = edgeLaplacian N i j := by
  classical
  have hN : N ≠ 0 := by have := i.isLt; omega
  have hsplit : Qcomb (wInv i j)
      = (∑ p : Fin N × Fin N, (if p = (i, j) then (1:ℝ) else 0) • Qmat p.1 p.2)
        - ∑ p : Fin N × Fin N,
            (if p.2.val = p.1.val + 1 ∧ i.val ≤ p.1.val ∧ p.1.val < j.val then (1/2 : ℝ) else 0)
              • Qmat p.1 p.2 := by
    rw [Qcomb, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl (fun p _ => by rw [wInv, sub_smul])
  have hfirst : (∑ p : Fin N × Fin N, (if p = (i, j) then (1:ℝ) else 0) • Qmat p.1 p.2)
      = Qmat i j := by
    rw [Finset.sum_congr rfl (fun p _ => by rw [ite_smul, one_smul, zero_smul])]
    rw [Finset.sum_ite_eq' Finset.univ (i, j) (fun p => Qmat p.1 p.2)]
    simp
  have hsecond : (∑ p : Fin N × Fin N,
      (if p.2.val = p.1.val + 1 ∧ i.val ≤ p.1.val ∧ p.1.val < j.val then (1/2 : ℝ) else 0)
        • Qmat p.1 p.2) = pathL i j := by
    rw [Fintype.sum_prod_type]
    have hcongr : ∀ x y : Fin N,
        (if y.val = x.val + 1 ∧ i.val ≤ x.val ∧ x.val < j.val then (1/2 : ℝ) else 0)
            • Qmat x y
          = if y.val = x.val + 1 ∧ i.val ≤ x.val ∧ x.val < j.val
              then ((1/2 : ℝ) • Qmat x y) else 0 := by
      intro x y; split_ifs <;> simp
    rw [Finset.sum_congr rfl (fun x _ => Finset.sum_congr rfl (fun y _ => hcongr x y))]
    rw [sum_adjacent_collapse i j (fun x y => (1/2 : ℝ) • Qmat x y), pathL,
      Finset.sum_filter]
    refine Finset.sum_congr rfl (fun x _ => ?_)
    by_cases hP : i.val ≤ x.val ∧ x.val < j.val
    · have hjN := j.isLt
      have hxN : x.val + 1 < N := by omega
      have hnext : (nextF x).val = x.val + 1 := nextF_val hxN
      have hlt : x < nextF x := by rw [Fin.lt_def, hnext]; omega
      rw [if_pos hP, if_pos hP, Qmat_adjacent x (nextF x) hlt hnext hN, smul_smul]
      norm_num
    · rw [if_neg hP, if_neg hP]
  rw [hsplit, hfirst, hsecond, Qmat_eq_cycleLaplacian i j hij hN, add_sub_cancel_right]


/-! ## (C.16): the `Q`'s span `Sym(E_N)` -/

/-- The family `{Q_{a,b} : a<b}`. -/
def QSet (N : ℕ) : Set (Matrix (Fin N) (Fin N) ℝ) :=
  {M | ∃ x y : Fin N, x < y ∧ M = Qmat x y}

/-- **(C.16)**: `span {Q_{a,b}} = Sym(E_N)`, via the triangular inversion — not via a
dimension count. -/
theorem span_QSet (hN : N ≠ 0) : Submodule.span ℝ (QSet N) = DCSymM N := by
  apply le_antisymm
  · rw [Submodule.span_le]
    rintro M ⟨x, y, -, rfl⟩
    exact Qmat_mem_DCSymM x y hN
  · rw [← span_LSet N, Submodule.span_le]
    rintro M ⟨i, j, hij, rfl⟩
    rw [← edgeLaplacian_eq_Qcomb i j hij]
    refine Qcomb_mem_span _ _ (fun x y => ?_)
    by_cases h : x < y
    · exact Submodule.subset_span ⟨x, y, h, rfl⟩
    · rw [Qmat_eq_zero h]; exact Submodule.zero_mem _

/-! ## (C.17): the explicit coefficients -/

/-- The coefficients of (C.17), **built** from (C.9) and (C.15): substitute each
`L_{ij}` of `I_{E_N} = N⁻¹∑_{i<j}L_{ij}` by its expression `wInv i j` in the `Q`'s. -/
noncomputable def cCoef (N : ℕ) : Fin N × Fin N → ℝ := fun p =>
  (N:ℝ)⁻¹ * ∑ q : Fin N × Fin N, (if q.1 < q.2 then wInv q.1 q.2 p else 0)

lemma cCoef_eq_zero_of_not_lt {p : Fin N × Fin N} (h : ¬ p.1 < p.2) : cCoef N p = 0 := by
  have hz : ∀ q : Fin N × Fin N, (if q.1 < q.2 then wInv q.1 q.2 p else 0) = 0 := by
    intro q
    by_cases hq : q.1 < q.2
    · rw [if_pos hq, wInv_eq_zero_of_not_lt hq h]
    · rw [if_neg hq]
  simp only [cCoef]
  rw [Finset.sum_congr rfl (fun q _ => hz q), Finset.sum_const_zero, mul_zero]

/-- **(C.17)**: `I_{E_N} = ∑_{a<b} c_{a,b} Q_{a,b}` with the coefficients above. -/
theorem cproj_eq_Qcomb_cCoef (hN : N ≠ 0) : Qcomb (cCoef N) = cproj N := by
  classical
  have hstep : ∀ q : Fin N × Fin N,
      (∑ p : Fin N × Fin N,
          ((N:ℝ)⁻¹ * (if q.1 < q.2 then wInv q.1 q.2 p else 0)) • Qmat p.1 p.2)
        = if q.1 < q.2 then ((N:ℝ)⁻¹) • edgeLaplacian N q.1 q.2 else 0 := by
    intro q
    by_cases hq : q.1 < q.2
    · rw [if_pos hq, ← edgeLaplacian_eq_Qcomb q.1 q.2 hq, Qcomb, Finset.smul_sum]
      exact Finset.sum_congr rfl (fun p _ => by rw [if_pos hq, smul_smul])
    · rw [if_neg hq]
      refine Finset.sum_eq_zero (fun p _ => ?_)
      rw [if_neg hq, mul_zero, zero_smul]
  have hterm : ∀ p : Fin N × Fin N, cCoef N p • Qmat p.1 p.2
      = ∑ q : Fin N × Fin N,
          ((N:ℝ)⁻¹ * (if q.1 < q.2 then wInv q.1 q.2 p else 0)) • Qmat p.1 p.2 := by
    intro p
    simp only [cCoef]
    rw [Finset.mul_sum, Finset.sum_smul]
  have hexpand : Qcomb (cCoef N)
      = ∑ q : Fin N × Fin N, (if q.1 < q.2 then ((N:ℝ)⁻¹) • edgeLaplacian N q.1 q.2 else 0) := by
    rw [Qcomb, Finset.sum_congr rfl (fun p _ => hterm p), Finset.sum_comm]
    exact Finset.sum_congr rfl (fun q _ => hstep q)
  rw [hexpand, ← sum_pair_subtype_eq (fun x y => ((N:ℝ)⁻¹) • edgeLaplacian N x y),
    ← cproj_eq_sum_edgeLaplacian N hN]

/-! ## (C.18): the coefficient sum really is `s_N` -/

lemma sum_range_cast (n : ℕ) : ∑ x ∈ Finset.range n, (x:ℝ) = (n:ℝ) * ((n:ℝ) - 1) / 2 := by
  induction n with
  | zero => simp
  | succ k ih => rw [Finset.sum_range_succ, ih]; push_cast; ring

lemma sum_range_gauss (n : ℕ) :
    ∑ y ∈ Finset.range n, ((y:ℝ) - ((y:ℝ)^2 + (y:ℝ))/4) = (n:ℝ) * sN n := by
  induction n with
  | zero => simp [sN]
  | succ k ih => rw [Finset.sum_range_succ, ih, sN, sN]; push_cast; ring

/-- The total coefficient mass contributed by one edge at distance `d = j - i` is
`1 - d/2` — the manuscript's "one long-interval term minus `d` adjacent terms of
coefficient `1/2`". -/
theorem coeffSum_wInv (i j : Fin N) (hij : i < j) :
    coeffSum (wInv i j) = 1 - (((j.val : ℝ)) - i.val)/2 := by
  classical
  have hijv : i.val ≤ j.val := le_of_lt hij
  rw [coeffSum]
  have hsplit : ∀ p : Fin N × Fin N, wInv i j p
      = (if p = (i, j) then (1:ℝ) else 0)
        - (if p.2.val = p.1.val + 1 ∧ i.val ≤ p.1.val ∧ p.1.val < j.val then (1/2:ℝ) else 0) :=
    fun p => rfl
  rw [Finset.sum_congr rfl (fun p _ => hsplit p), Finset.sum_sub_distrib]
  have hfirst : (∑ p : Fin N × Fin N, if p = (i, j) then (1:ℝ) else 0) = 1 := by
    rw [Finset.sum_ite_eq' Finset.univ (i, j) (fun _ => (1:ℝ))]
    simp
  have hsecond : (∑ p : Fin N × Fin N,
      if p.2.val = p.1.val + 1 ∧ i.val ≤ p.1.val ∧ p.1.val < j.val then (1/2:ℝ) else 0)
      = (((j.val : ℝ)) - i.val)/2 := by
    rw [Fintype.sum_prod_type, sum_adjacent_collapse i j (fun _ _ => (1/2:ℝ)),
      ← Finset.sum_filter, Finset.sum_const, card_filter_val_Ico i j hijv, nsmul_eq_mul]
    have : ((j.val - i.val : ℕ) : ℝ) = (j.val : ℝ) - i.val := by
      have : i.val ≤ j.val := hijv
      push_cast [Nat.cast_sub this]
      ring
    rw [this]
    ring
  rw [hfirst, hsecond]

/-- The distance sum of (C.18), in closed form. -/
theorem pair_distance_sum (N : ℕ) :
    (∑ q : Fin N × Fin N, if q.1 < q.2 then (1 - (((q.2.val:ℝ)) - q.1.val)/2) else 0)
      = (N:ℝ) * sN N := by
  classical
  have hcond : ∀ q : Fin N × Fin N,
      (if q.1 < q.2 then (1 - (((q.2.val:ℝ)) - q.1.val)/2) else 0)
        = (if q.1.val < q.2.val then (1 - (((q.2.val:ℝ)) - q.1.val)/2) else 0) := by
    intro q
    by_cases h : q.1.val < q.2.val
    · rw [if_pos h, if_pos (show q.1 < q.2 from h)]
    · rw [if_neg h, if_neg (show ¬ q.1 < q.2 from h)]
  rw [Finset.sum_congr rfl (fun q _ => hcond q), Fintype.sum_prod_type]
  have hinner : ∀ x : Fin N,
      (∑ y : Fin N, if x.val < y.val then (1 - (((y.val:ℝ)) - x.val)/2) else 0)
        = ∑ y ∈ Finset.range N, (if x.val < y then (1 - ((y:ℝ) - x.val)/2) else 0) :=
    fun x => Fin.sum_univ_eq_sum_range
      (fun k => if x.val < k then (1 - ((k:ℝ) - x.val)/2) else 0) N
  rw [Finset.sum_congr rfl (fun x _ => hinner x)]
  rw [Fin.sum_univ_eq_sum_range
    (fun k => ∑ y ∈ Finset.range N, (if k < y then (1 - ((y:ℝ) - k)/2) else 0)) N]
  rw [Finset.sum_comm]
  have hrow : ∀ y ∈ Finset.range N,
      (∑ x ∈ Finset.range N, (if x < y then (1 - ((y:ℝ) - x)/2) else 0))
        = (y:ℝ) - (((y:ℝ)^2 + (y:ℝ))/4) := by
    intro y hy
    rw [Finset.mem_range] at hy
    have hfil : (Finset.range N).filter (fun x => x < y) = Finset.range y := by
      ext x
      simp only [Finset.mem_filter, Finset.mem_range]
      omega
    rw [← Finset.sum_filter, hfil, Finset.sum_sub_distrib, Finset.sum_const,
      Finset.card_range, nsmul_eq_mul, mul_one]
    have hs : ∑ x ∈ Finset.range y, (((y:ℝ) - x)/2)
        = ((y:ℝ) * y - (y:ℝ)*((y:ℝ)-1)/2)/2 := by
      have hbody : ∀ x ∈ Finset.range y, ((y:ℝ) - (x:ℝ))/2 = (y:ℝ)/2 - (x:ℝ)/2 :=
        fun x _ => by ring
      have hdiv : ∑ x ∈ Finset.range y, ((x:ℝ)/2)
          = (∑ x ∈ Finset.range y, (x:ℝ))/2 := by
        rw [eq_div_iff (two_ne_zero), Finset.sum_mul]
        exact Finset.sum_congr rfl (fun x _ => by ring)
      rw [Finset.sum_congr rfl hbody, Finset.sum_sub_distrib, Finset.sum_const,
        Finset.card_range, nsmul_eq_mul, hdiv, sum_range_cast]
      ring
    rw [hs]; ring
  rw [Finset.sum_congr rfl hrow, sum_range_gauss]

/-- **(C.18)**: the sum of the coefficients constructed in (C.17) is exactly `s_N`. -/
theorem coeffSum_cCoef_eq_sN (hN : N ≠ 0) : coeffSum (cCoef N) = sN N := by
  classical
  have hNR : (N:ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hN
  simp only [coeffSum, cCoef]
  rw [show (∑ p : Fin N × Fin N,
      (N:ℝ)⁻¹ * ∑ q : Fin N × Fin N, (if q.1 < q.2 then wInv q.1 q.2 p else 0))
      = (N:ℝ)⁻¹ * ∑ p : Fin N × Fin N, ∑ q : Fin N × Fin N,
          (if q.1 < q.2 then wInv q.1 q.2 p else 0) by rw [Finset.mul_sum]]
  rw [Finset.sum_comm]
  have hq : ∀ q : Fin N × Fin N,
      (∑ p : Fin N × Fin N, if q.1 < q.2 then wInv q.1 q.2 p else 0)
        = if q.1 < q.2 then (1 - (((q.2.val:ℝ)) - q.1.val)/2) else 0 := by
    intro q
    by_cases h : q.1 < q.2
    · rw [if_pos h, Finset.sum_congr rfl (fun p _ => if_pos h), ← coeffSum,
        coeffSum_wInv q.1 q.2 h]
    · rw [if_neg h, Finset.sum_congr rfl (fun p _ => if_neg h), Finset.sum_const_zero]
  rw [Finset.sum_congr rfl (fun q _ => hq q), pair_distance_sum]
  field_simp

/-! ## (C.19)–(C.21): removing the identity term -/

/-- **(C.19)**: `(1-2s_N) I_{E_N} = -∑_{a<b} c_{a,b} S_{a,b}|_{E_N}`. -/
theorem identity_elimination (hN : N ≠ 0) :
    (1 - 2 * sN N) • cproj N
      = - ∑ p : Fin N × Fin N, cCoef N p • Smat p.1 p.2 := by
  classical
  have hq := cproj_eq_Qcomb_cCoef hN
  have hterm : ∀ p : Fin N × Fin N, cCoef N p • Qmat p.1 p.2
      = (cCoef N p * 2) • cproj N - cCoef N p • Smat p.1 p.2 := by
    intro p; rw [Qmat, smul_sub, smul_smul]
  have hmass : (∑ p : Fin N × Fin N, cCoef N p * 2) = 2 * coeffSum (cCoef N) := by
    rw [coeffSum, ← Finset.sum_mul]; ring
  rw [Qcomb, Finset.sum_congr rfl (fun p _ => hterm p), Finset.sum_sub_distrib,
    ← Finset.sum_smul, hmass, coeffSum_cCoef_eq_sN hN] at hq
  refine eq_neg_of_add_eq_zero_left ?_
  calc (1 - 2 * sN N) • cproj N + ∑ p : Fin N × Fin N, cCoef N p • Smat p.1 p.2
      = cproj N - ((2 * sN N) • cproj N - ∑ p : Fin N × Fin N, cCoef N p • Smat p.1 p.2) := by
        module
    _ = cproj N - cproj N := by rw [hq]
    _ = 0 := sub_self _

/-- The family `{S_{a,b}|_{E_N} : a<b}`. -/
def SSet (N : ℕ) : Set (Matrix (Fin N) (Fin N) ℝ) :=
  {M | ∃ (x y : Fin N) (h : x < y), M = restr N (Sab x y h)}

lemma Sab_isSymm (a b : Fin N) (hab : a < b) : (Sab a b hab).IsSymm := by
  show (Sab a b hab)ᵀ = Sab a b hab
  rw [Sab, Matrix.transpose_add, Matrix.transpose_transpose, add_comm]

lemma Smat_mem_span_SSet {x y : Fin N} (h : x < y) : Smat x y ∈ Submodule.span ℝ (SSet N) := by
  rw [Smat, dif_pos h]
  exact Submodule.subset_span ⟨x, y, h, rfl⟩

lemma cproj_mem_span_SSet (hN : N ≠ 0) : cproj N ∈ Submodule.span ℝ (SSet N) := by
  classical
  have hne : (1 - 2 * sN N) ≠ 0 := ne_of_gt (one_sub_two_sN_pos N)
  have hsum : (∑ p : Fin N × Fin N, cCoef N p • Smat p.1 p.2) ∈ Submodule.span ℝ (SSet N) := by
    refine Submodule.sum_mem _ (fun p _ => ?_)
    by_cases h : p.1 < p.2
    · exact Submodule.smul_mem _ _ (Smat_mem_span_SSet h)
    · rw [cCoef_eq_zero_of_not_lt h, zero_smul]
      exact Submodule.zero_mem _
  have hc : cproj N = (1 - 2 * sN N)⁻¹ • (-(∑ p : Fin N × Fin N, cCoef N p • Smat p.1 p.2)) := by
    rw [← identity_elimination hN, smul_smul, inv_mul_cancel₀ hne, one_smul]
  rw [hc]
  exact Submodule.smul_mem _ _ (Submodule.neg_mem _ hsum)

/-- **(C.21)**: `span {S_{a,b}|_{E_N}} = Sym(E_N)`, as an equality of submodules. -/
theorem span_SSet (hN : N ≠ 0) : Submodule.span ℝ (SSet N) = DCSymM N := by
  apply le_antisymm
  · rw [Submodule.span_le]
    rintro M ⟨x, y, h, rfl⟩
    exact restr_mem_DCSymM N hN (Sab_isSymm x y h)
  · rw [← span_QSet hN, Submodule.span_le]
    rintro M ⟨x, y, h, rfl⟩
    rw [Qmat]
    exact Submodule.sub_mem _
      (Submodule.smul_mem _ _ (cproj_mem_span_SSet hN)) (Smat_mem_span_SSet h)

/-! ## The finite matrix form of Theorem C -/

/-- `A_C` is symmetric — the matrix form of the fiber's closure under inversion (3.8). -/
theorem classSum_isSymm (σ : Equiv.Perm (Fin N)) : (classSum σ).IsSymm := by
  classical
  have hmem : ∀ ρ : Equiv.Perm (Fin N), ρ ∈ fiber σ ↔ PosetIsomorphic ρ σ := by
    intro ρ; simp [fiber]
  have hinj : ∀ x ∈ fiber σ, ∀ y ∈ fiber σ, x⁻¹ = y⁻¹ → x = y :=
    fun x _ y _ h => inv_injective h
  have himg : (fiber σ).image (fun ρ => ρ⁻¹) = fiber σ := by
    ext ρ
    simp only [Finset.mem_image]
    constructor
    · rintro ⟨τ, hτ, rfl⟩
      exact (hmem _).mpr (posetIsomorphic_inv_of_isomorphic ((hmem τ).mp hτ))
    · intro h
      exact ⟨ρ⁻¹, (hmem _).mpr (posetIsomorphic_inv_of_isomorphic ((hmem ρ).mp h)), by simp⟩
  show (classSum σ)ᵀ = classSum σ
  rw [classSum, Matrix.transpose_sum,
    Finset.sum_congr rfl (fun ρ _ => permM_transpose ρ), ← Finset.sum_image hinj, himg]

/-- `A_C` depends only on the class `C`, not on the representative: isomorphic
permutations have the same fiber. This is what makes indexing by permutations below the
same thing as indexing by classes. -/
theorem classSum_congr {σ σ' : Equiv.Perm (Fin N)} (h : PosetIsomorphic σ σ') :
    classSum σ = classSum σ' := by
  classical
  have hfib : fiber σ = fiber σ' := by
    ext ρ
    simp only [fiber, Finset.mem_filter, Finset.mem_univ, true_and]
    exact ⟨fun hρ => posetIsomorphic_trans hρ h,
      fun hρ => posetIsomorphic_trans hρ (posetIsomorphic_symm h)⟩
  rw [classSum, classSum, hfib]

/-- The class sums of *all* poset classes, restricted to `E_N`: `{A_C|_{E_N} : C ∈ 𝒞_N}`.
Indexing by permutations gives exactly the classes realized at cardinality `N`, since
`classSum σ` depends only on `[P_σ]`. -/
def ASet (N : ℕ) : Set (Matrix (Fin N) (Fin N) ℝ) :=
  Set.range (fun σ : Equiv.Perm (Fin N) => restr N (classSum σ))

/-- **Theorem C, finite matrix form**:
`span {A_C|_{E_N} : C ∈ 𝒞_N} = Sym(E_N)` for every `N ≥ 1`
(the manuscript states it for `N ≥ 2`; for `N = 1` both sides are trivially `0`). -/
theorem span_classSum_restr_eq (hN : N ≠ 0) :
    Submodule.span ℝ (ASet N) = DCSymM N := by
  apply le_antisymm
  · rw [Submodule.span_le]
    rintro M ⟨σ, rfl⟩
    exact restr_mem_DCSymM N hN (classSum_isSymm σ)
  · rw [← span_SSet hN, Submodule.span_le]
    rintro M ⟨x, y, h, rfl⟩
    obtain ⟨c, hc, hEq⟩ := Sab_nonzero_smul_classSum x y h
    rw [hEq, restr_smul]
    exact Submodule.smul_mem _ _ (Submodule.subset_span ⟨tau x y h, rfl⟩)


/-! ## Dimension of the certified span

The span statement above says *which* module the class sums generate. This section adds
its dimension, so that the certificate cannot be read as covering more (or less) than it
does. Nothing new is built: the basis is the edge-Laplacian family already proved
independent and spanning in `FiniteLinearAlgebra.lean`.

Note what is deliberately **not** proved here: the manuscript's boxed Theorem C also
asserts `dim V_N = rank G_{[P]}^{(N)}`, and no Lean theorem identifies the rank of the
Fisher/Gram matrix. That remains `NOT_FORMALIZED`; see `FORMALIZATION_STATUS.md`. -/

lemma card_filter_lt_fin (y : Fin N) :
    (Finset.univ.filter (fun x : Fin N => x < y)).card = y.val := by
  classical
  have hset : (Finset.univ.filter (fun x : Fin N => x < y))
      = Finset.univ.filter (fun x : Fin N => x.val < y.val) := by
    ext x
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Fin.lt_def]
  rw [hset, card_filter_val_lt]

lemma sum_range_id_eq_choose (n : ℕ) : ∑ k ∈ Finset.range n, k = n.choose 2 := by
  rw [Nat.choose_two_right]
  have h := Finset.sum_range_id_mul_two n
  omega

/-- The index set of the edge Laplacians has `C(N,2)` elements. -/
lemma card_pairs (N : ℕ) :
    Fintype.card {p : Fin N × Fin N // p.1 < p.2} = N.choose 2 := by
  classical
  rw [Fintype.card_subtype, Finset.card_filter, Fintype.sum_prod_type, Finset.sum_comm]
  have hrow : ∀ y : Fin N, (∑ x : Fin N, if x < y then 1 else 0) = y.val := by
    intro y
    rw [← Finset.card_filter]
    exact card_filter_lt_fin y
  rw [Finset.sum_congr rfl (fun y _ => hrow y),
    Fin.sum_univ_eq_sum_range (fun k => k) N, sum_range_id_eq_choose]

/-- The edge Laplacians form a basis of `Sym(E_N)` — independence and spanning are the
first pass's theorems, assembled here into a `Basis`. -/
noncomputable def edgeBasis (N : ℕ) :
    Module.Basis {p : Fin N × Fin N // p.1 < p.2} ℝ (DCSymM N) := by
  classical
  refine Module.Basis.mk (v := fun p => ⟨edgeLaplacian N p.1.1 p.1.2,
      edgeLaplacian_mem_DCSymM N p.1.1 p.1.2⟩) ?_ ?_
  · exact LinearIndependent.of_comp (DCSymM N).subtype (edgeLaplacian_linearIndependent N)
  · intro M _
    have hM := DCSymM_eq_sum_edgeLaplacian N M.2
    have hlift : M = ∑ p : {p : Fin N × Fin N // p.1 < p.2},
        (-(M.val p.1.1 p.1.2)) •
          (⟨edgeLaplacian N p.1.1 p.1.2, edgeLaplacian_mem_DCSymM N p.1.1 p.1.2⟩ :
            DCSymM N) := by
      apply Subtype.ext
      simpa using hM
    rw [hlift]
    exact Submodule.sum_mem _
      (fun p _ => Submodule.smul_mem _ _ (Submodule.subset_span ⟨p, rfl⟩))

/-- **`dim Sym(E_N) = C(N,2)`.** -/
theorem finrank_DCSymM (N : ℕ) : Module.finrank ℝ (DCSymM N) = N.choose 2 := by
  rw [Module.finrank_eq_card_basis (edgeBasis N), card_pairs N]

/-- The same in the arithmetic form the manuscript writes. -/
theorem finrank_DCSymM_eq_half (N : ℕ) :
    Module.finrank ℝ (DCSymM N) = N * (N - 1) / 2 := by
  rw [finrank_DCSymM, Nat.choose_two_right]

/-- **The dimension of the certified class-sum span:**
`dim span{A_C|_{E_N} : C ∈ 𝒞_N} = C(N,2)`.

Stated for the **real class sums** of `ClassSum.lean`, not for the edge Laplacians: it is
`span_classSum_restr_eq` that carries the poset content, and this theorem only computes
the dimension of that same module. -/
theorem finrank_span_classSum_restr (hN : N ≠ 0) :
    Module.finrank ℝ (Submodule.span ℝ (ASet N)) = N.choose 2 := by
  rw [span_classSum_restr_eq hN, finrank_DCSymM]

theorem finrank_span_classSum_restr_eq_half (hN : N ≠ 0) :
    Module.finrank ℝ (Submodule.span ℝ (ASet N)) = N * (N - 1) / 2 := by
  rw [finrank_span_classSum_restr hN, Nat.choose_two_right]

end HorizonFormal.S1Paper
