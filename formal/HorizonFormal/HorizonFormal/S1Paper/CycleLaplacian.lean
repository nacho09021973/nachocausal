import HorizonFormal.S1Paper.ClassSum
import HorizonFormal.S1Paper.Restriction

/-!
# `Q_{a,b} = 2I_{E_N} - S_{a,b}|_{E_N}` is the cycle Laplacian — (C.12)–(C.14)

The direction here is the one the manuscript claims and the one that carries content:
`Q_{a,b}` is *defined* from the class-sum-connected `S_{a,b}` of `ClassSum.lean`, and the
Laplacian description is then **proved**. Defining `Q_{a,b}` as a sum of edge Laplacians
would make (C.13)–(C.14) vacuous.

The proof goes through one identity worth isolating, true for *every* permutation:

```
2·I - (P_σ + P_σᵀ) = ∑_i L_{i, σ(i)}
```

(`two_smul_one_sub_permSym`). For `σ = τ_{a,b}` the terms outside `[a,b]` vanish (`τ`
fixes those points), the terms `i ∈ [a,b)` give the path `L_{i,i+1}`, and the single term
`i = b` gives the closing edge `L_{b,a} = L_{a,b}`. That is exactly the consecutive
cycle's graph Laplacian.

Index convention: the manuscript is 1-indexed with `I_{a,b} = {a+1,…,b+1}`; `Fin N` here
is 0-indexed, so its `L_{a+1,b+1}` is our `edgeLaplacian N a b` and its
`∑_{k=a+1}^{b} L_{k,k+1}` is our `pathL a b`. Vertex sets match: `{a,…,b}`.
-/

namespace HorizonFormal.S1Paper

open scoped BigOperators
open Matrix Finset

variable {N : ℕ}

/-! ## Two elementary facts about `edgeLaplacian` -/

lemma edgeLaplacian_self (i : Fin N) : edgeLaplacian N i i = 0 := by
  ext x y
  simp [edgeLaplacian_apply, edgeVec_apply]

lemma edgeLaplacian_swap (i j : Fin N) : edgeLaplacian N i j = edgeLaplacian N j i := by
  ext x y
  simp only [edgeLaplacian_apply, edgeVec_apply]
  ring

private lemma ite_one_zero_comm (p q : Fin N) :
    (if p = q then (1:ℝ) else 0) = if q = p then (1:ℝ) else 0 := by
  by_cases h : p = q
  · simp [h]
  · simp [h, Ne.symm h]

/-! ## The permutation identity -/

/-- For **every** permutation, `2I - (P_σ + P_σᵀ) = ∑_i L_{i,σ(i)}`. The terms with
`σ i = i` vanish, so only the moved points contribute. -/
theorem two_smul_one_sub_permSym (σ : Equiv.Perm (Fin N)) :
    (2:ℝ) • (1 : Matrix (Fin N) (Fin N) ℝ) - (permM σ + (permM σ)ᵀ)
      = ∑ i, edgeLaplacian N i (σ i) := by
  ext a b
  rw [Matrix.sum_apply]
  have hterm : ∀ i : Fin N, edgeLaplacian N i (σ i) a b
      = (if a = i then (1:ℝ) else 0) * (if b = i then (1:ℝ) else 0)
        - (if a = i then (1:ℝ) else 0) * (if b = σ i then (1:ℝ) else 0)
        - (if a = σ i then (1:ℝ) else 0) * (if b = i then (1:ℝ) else 0)
        + (if a = σ i then (1:ℝ) else 0) * (if b = σ i then (1:ℝ) else 0) := by
    intro i
    simp only [edgeLaplacian_apply, edgeVec_apply]
    ring
  have h1 : ∑ i, (if a = i then (1:ℝ) else 0) * (if b = i then (1:ℝ) else 0)
      = if a = b then (1:ℝ) else 0 := by
    rw [Finset.sum_congr rfl (fun i _ => by rw [ite_mul, zero_mul, one_mul])]
    rw [Finset.sum_ite_eq Finset.univ a (fun i => if b = i then (1:ℝ) else 0)]
    rw [if_pos (Finset.mem_univ a), ite_one_zero_comm]
  have h2 : ∑ i, (if a = i then (1:ℝ) else 0) * (if b = σ i then (1:ℝ) else 0)
      = if b = σ a then (1:ℝ) else 0 := by
    rw [Finset.sum_congr rfl (fun i _ => by rw [ite_mul, zero_mul, one_mul])]
    rw [Finset.sum_ite_eq Finset.univ a (fun i => if b = σ i then (1:ℝ) else 0)]
    rw [if_pos (Finset.mem_univ a)]
  have h3 : ∑ i, (if a = σ i then (1:ℝ) else 0) * (if b = i then (1:ℝ) else 0)
      = if a = σ b then (1:ℝ) else 0 := by
    rw [Finset.sum_congr rfl (fun i _ => by rw [mul_comm, ite_mul, zero_mul, one_mul])]
    rw [Finset.sum_ite_eq Finset.univ b (fun i => if a = σ i then (1:ℝ) else 0)]
    rw [if_pos (Finset.mem_univ b)]
  have h4 : ∑ i, (if a = σ i then (1:ℝ) else 0) * (if b = σ i then (1:ℝ) else 0)
      = if a = b then (1:ℝ) else 0 := by
    rw [← h1]
    exact Equiv.sum_comp σ (fun j => (if a = j then (1:ℝ) else 0) * (if b = j then (1:ℝ) else 0))
  rw [Finset.sum_congr rfl (fun i _ => hterm i), Finset.sum_add_distrib,
    Finset.sum_sub_distrib, Finset.sum_sub_distrib, h1, h2, h3, h4]
  simp only [Matrix.sub_apply, Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply,
    smul_eq_mul, Matrix.transpose_apply, permM, Matrix.of_apply]
  rw [ite_one_zero_comm b (σ a), ite_one_zero_comm a (σ b)]
  ring

/-! ## The consecutive path and the cycle Laplacian -/

/-- `k+1`, clamped (the clamp is never reached where this is used: `k < b ≤ N-1`). -/
def nextF (k : Fin N) : Fin N := ⟨min (k.val + 1) (N - 1), by have := k.isLt; omega⟩

lemma nextF_val {k : Fin N} (h : k.val + 1 < N) : (nextF k).val = k.val + 1 := by
  simp only [nextF]
  omega

/-- The consecutive path `∑_{k∈[a,b)} L_{k,k+1}` — the manuscript's
`∑_{k=a+1}^{b} L_{k,k+1}` in 0-indexed form. -/
noncomputable def pathL (a b : Fin N) : Matrix (Fin N) (Fin N) ℝ :=
  ∑ i ∈ Finset.univ.filter (fun i : Fin N => a.val ≤ i.val ∧ i.val < b.val),
    edgeLaplacian N i (nextF i)

lemma pathL_mem_DCSymM (a b : Fin N) : pathL a b ∈ DCSymM N :=
  Submodule.sum_mem _ (fun i _ => edgeLaplacian_mem_DCSymM N i (nextF i))

/-- On `[a,b)` the interval cycle is exactly the successor map. -/
lemma tau_eq_nextF {a b i : Fin N} (hab : a < b) (h1 : a.val ≤ i.val) (h2 : i.val < b.val) :
    tau a b hab i = nextF i := by
  have hb := b.isLt
  apply Fin.ext
  rw [tau_apply_lt_val a b i hab h1 h2, nextF_val (by omega)]

/-- **The cycle decomposition**: summing `L_{i,τ(i)}` over all of `Fin N` leaves exactly
the path edges of `[a,b)` plus the closing edge `{a,b}`. -/
theorem sum_edgeLaplacian_tau (a b : Fin N) (hab : a < b) :
    ∑ i, edgeLaplacian N i (tau a b hab i) = edgeLaplacian N a b + pathL a b := by
  classical
  have hab' : a.val < b.val := hab
  rw [← Finset.sum_filter_add_sum_filter_not Finset.univ
    (fun i : Fin N => a.val ≤ i.val ∧ i.val < b.val) (fun i => edgeLaplacian N i (tau a b hab i))]
  have hIn : ∑ i ∈ Finset.univ.filter (fun i : Fin N => a.val ≤ i.val ∧ i.val < b.val),
      edgeLaplacian N i (tau a b hab i) = pathL a b := by
    refine Finset.sum_congr rfl (fun i hi => ?_)
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hi
    rw [tau_eq_nextF hab hi.1 hi.2]
  have hbmem : b ∈ Finset.univ.filter (fun i : Fin N => ¬ (a.val ≤ i.val ∧ i.val < b.val)) := by
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    omega
  have hOut : ∑ i ∈ Finset.univ.filter (fun i : Fin N => ¬ (a.val ≤ i.val ∧ i.val < b.val)),
      edgeLaplacian N i (tau a b hab i) = edgeLaplacian N a b := by
    rw [Finset.sum_eq_single_of_mem b hbmem ?_]
    · rw [tau_apply_b, edgeLaplacian_swap]
    · intro i hi hne
      simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hi
      have hival : i.val ≠ b.val := fun h => hne (Fin.ext h)
      rw [tau_apply_outside a b i hab (by omega), edgeLaplacian_self]
  rw [hIn, hOut, add_comm]

/-! ## (C.12): the definition of `Q_{a,b}` -/

/-- `S_{a,b}|_{E_N}`, extended by the harmless value `2I_{E_N}` off the index range so
that `Q` is a total function; `Q` is then `0` there and never contributes. -/
noncomputable def Smat (x y : Fin N) : Matrix (Fin N) (Fin N) ℝ :=
  if h : x < y then restr N (Sab x y h) else (2:ℝ) • cproj N

/-- **(C.12)**: `Q_{a,b} := 2I_{E_N} - S_{a,b}|_{E_N}`. -/
noncomputable def Qmat (x y : Fin N) : Matrix (Fin N) (Fin N) ℝ :=
  (2:ℝ) • cproj N - Smat x y

lemma Qmat_of_lt {x y : Fin N} (h : x < y) :
    Qmat x y = (2:ℝ) • cproj N - restr N (Sab x y h) := by
  rw [Qmat, Smat, dif_pos h]

lemma Qmat_eq_zero {x y : Fin N} (h : ¬ x < y) : Qmat x y = 0 := by
  rw [Qmat, Smat, dif_neg h, sub_self]

/-! ## (C.13)–(C.14): `Q_{a,b}` is the cycle Laplacian -/

/-- `2I - S_{a,b}` already lies in `Sym(E_N)`, so restricting to `E_N` changes nothing. -/
lemma two_one_sub_Sab_mem (a b : Fin N) (hab : a < b) :
    (2:ℝ) • (1 : Matrix (Fin N) (Fin N) ℝ) - Sab a b hab ∈ DCSymM N := by
  rw [Sab, two_smul_one_sub_permSym]
  exact Submodule.sum_mem _ (fun i _ => edgeLaplacian_mem_DCSymM N i _)

/-- Restriction to `E_N` is invisible here: `Q_{a,b} = 2I - S_{a,b}` as full matrices. -/
lemma Qmat_eq_two_one_sub_Sab (a b : Fin N) (hab : a < b) (hN : N ≠ 0) :
    Qmat a b = (2:ℝ) • (1 : Matrix (Fin N) (Fin N) ℝ) - Sab a b hab := by
  have hfix := restr_eq_self N (two_one_sub_Sab_mem a b hab)
  rw [restr_sub, restr_smul, restr_one N hN] at hfix
  rw [Qmat_of_lt hab, hfix]

/-- **(C.14)** (and, uniformly, (C.13)): `Q_{a,b}` is the graph Laplacian of the
consecutive cycle on `{a,…,b}` — the closing edge plus the path. -/
theorem Qmat_eq_cycleLaplacian (a b : Fin N) (hab : a < b) (hN : N ≠ 0) :
    Qmat a b = edgeLaplacian N a b + pathL a b := by
  rw [Qmat_eq_two_one_sub_Sab a b hab hN, Sab, two_smul_one_sub_permSym,
    sum_edgeLaplacian_tau a b hab]

/-- **(C.13)**: for an interval of length two the unique edge is counted twice. -/
theorem Qmat_adjacent (a b : Fin N) (hab : a < b) (hadj : b.val = a.val + 1) (hN : N ≠ 0) :
    Qmat a b = (2:ℝ) • edgeLaplacian N a b := by
  have hab' : a.val < b.val := hab
  have hb := b.isLt
  have hpath : pathL a b = edgeLaplacian N a b := by
    have hfil : Finset.univ.filter (fun i : Fin N => a.val ≤ i.val ∧ i.val < b.val) = {a} := by
      ext i
      simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton]
      constructor
      · intro h; exact Fin.ext (by omega)
      · intro h; subst h; omega
    have hnext : nextF a = b := Fin.ext (by rw [nextF_val (by omega)]; omega)
    rw [pathL, hfil, Finset.sum_singleton, hnext]
  rw [Qmat_eq_cycleLaplacian a b hab hN, hpath, two_smul]

/-- **(C.14)** exactly as stated in the manuscript (the non-adjacent case). -/
theorem Qmat_nonadjacent (a b : Fin N) (hab : a < b) (_hna : a.val + 1 < b.val) (hN : N ≠ 0) :
    Qmat a b = edgeLaplacian N a b + pathL a b :=
  Qmat_eq_cycleLaplacian a b hab hN

lemma Qmat_mem_DCSymM (x y : Fin N) (hN : N ≠ 0) : Qmat x y ∈ DCSymM N := by
  by_cases h : x < y
  · rw [Qmat_eq_cycleLaplacian x y h hN]
    exact Submodule.add_mem _ (edgeLaplacian_mem_DCSymM N x y) (pathL_mem_DCSymM x y)
  · rw [Qmat_eq_zero h]; exact Submodule.zero_mem _

end HorizonFormal.S1Paper
