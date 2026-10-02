import HorizonFormal.S1Paper.PermutationPoset
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Fin
import Mathlib.Data.Fintype.EquivFin

/-!
# The near-chain permutation family `τ_{a,b}` (Appendix C)

For `0 ≤ a < b ≤ N-1`, the manuscript's `τ_{a,b}` is the cycle on the consecutive
interval `I_{a,b} = {a,...,b}` (adapted to 0-indexed `Fin N`): it shifts each element
of `[a,b)` forward by one and sends `b` back to `a`, fixing everything outside `[a,b]`.

Throughout, all order/arithmetic reasoning is routed through `.val` (`Fin N → ℕ`) and
closed with `omega`; each `Fin`-level fact has a `_val` companion used for this purpose.
-/

namespace HorizonFormal.S1Paper

variable {N : ℕ}

/-- The underlying function of `τ_{a,b}`. -/
def tauFun (a b : Fin N) (k : Fin N) : Fin N :=
  if k = b then a
  else if h : a.val ≤ k.val ∧ k.val < b.val then ⟨k.val + 1, by omega⟩
  else k

lemma tauFun_apply_b (a b : Fin N) : tauFun a b b = a := by simp [tauFun]

lemma tauFun_apply_b_val (a b : Fin N) : (tauFun a b b).val = a.val := by
  rw [tauFun_apply_b]

lemma tauFun_apply_lt (a b k : Fin N) (h1 : a.val ≤ k.val) (h2 : k.val < b.val) :
    tauFun a b k = ⟨k.val + 1, by omega⟩ := by
  have hkb : k ≠ b := by intro h; subst h; omega
  simp [tauFun, hkb, h1, h2]

lemma tauFun_apply_lt_val (a b k : Fin N) (h1 : a.val ≤ k.val) (h2 : k.val < b.val) :
    (tauFun a b k).val = k.val + 1 := by
  rw [tauFun_apply_lt a b k h1 h2]

lemma tauFun_apply_outside (a b k : Fin N) (hab : a < b) (h : k.val < a.val ∨ b.val < k.val) :
    tauFun a b k = k := by
  have hab' : a.val < b.val := hab
  have hkb : k ≠ b := by intro hk; rw [hk] at h; omega
  have hnot : ¬ (a.val ≤ k.val ∧ k.val < b.val) := by omega
  unfold tauFun
  rw [if_neg hkb, dif_neg hnot]

lemma tauFun_apply_outside_val (a b k : Fin N) (hab : a < b)
    (h : k.val < a.val ∨ b.val < k.val) : (tauFun a b k).val = k.val := by
  rw [tauFun_apply_outside a b k hab h]

/-- `tauFun a b` is injective. -/
theorem tauFun_injective (a b : Fin N) (hab : a < b) : Function.Injective (tauFun a b) := by
  have hab' : a.val < b.val := hab
  intro x y hxy
  have hxyval : (tauFun a b x).val = (tauFun a b y).val := congrArg Fin.val hxy
  apply Fin.ext
  by_cases hxb : x = b <;> by_cases hyb : y = b
  · rw [hxb, hyb]
  · rw [hxb, tauFun_apply_b_val] at hxyval
    by_cases hy1 : a.val ≤ y.val ∧ y.val < b.val
    · rw [tauFun_apply_lt_val a b y hy1.1 hy1.2] at hxyval; omega
    · have hout : y.val < a.val ∨ b.val < y.val := by omega
      rw [tauFun_apply_outside_val a b y hab hout] at hxyval; omega
  · rw [hyb, tauFun_apply_b_val] at hxyval
    by_cases hx1 : a.val ≤ x.val ∧ x.val < b.val
    · rw [tauFun_apply_lt_val a b x hx1.1 hx1.2] at hxyval; omega
    · have hout : x.val < a.val ∨ b.val < x.val := by omega
      rw [tauFun_apply_outside_val a b x hab hout] at hxyval; omega
  · by_cases hx1 : a.val ≤ x.val ∧ x.val < b.val <;>
      by_cases hy1 : a.val ≤ y.val ∧ y.val < b.val
    · rw [tauFun_apply_lt_val a b x hx1.1 hx1.2, tauFun_apply_lt_val a b y hy1.1 hy1.2] at hxyval
      omega
    · have houty : y.val < a.val ∨ b.val < y.val := by omega
      rw [tauFun_apply_lt_val a b x hx1.1 hx1.2, tauFun_apply_outside_val a b y hab houty]
        at hxyval
      omega
    · have houtx : x.val < a.val ∨ b.val < x.val := by omega
      rw [tauFun_apply_outside_val a b x hab houtx, tauFun_apply_lt_val a b y hy1.1 hy1.2]
        at hxyval
      omega
    · have houtx : x.val < a.val ∨ b.val < x.val := by omega
      have houty : y.val < a.val ∨ b.val < y.val := by omega
      rw [tauFun_apply_outside_val a b x hab houtx, tauFun_apply_outside_val a b y hab houty]
        at hxyval
      omega

/-- `τ_{a,b}` as a genuine permutation of `Fin N` (Appendix C). -/
noncomputable def tau (a b : Fin N) (hab : a < b) : Equiv.Perm (Fin N) :=
  Equiv.ofBijective (tauFun a b)
    (Finite.injective_iff_bijective.mp (tauFun_injective a b hab))

lemma tau_eq_tauFun (a b : Fin N) (hab : a < b) (k : Fin N) :
    tau a b hab k = tauFun a b k := by
  simp only [tau, Equiv.coe_ofBijective]

lemma tau_apply_b (a b : Fin N) (hab : a < b) : tau a b hab b = a := by
  rw [tau_eq_tauFun]; exact tauFun_apply_b a b

lemma tau_apply_b_val (a b : Fin N) (hab : a < b) : (tau a b hab b).val = a.val := by
  rw [tau_apply_b]

lemma tau_apply_lt (a b k : Fin N) (hab : a < b) (h1 : a.val ≤ k.val) (h2 : k.val < b.val) :
    tau a b hab k = ⟨k.val + 1, by omega⟩ := by
  rw [tau_eq_tauFun]; exact tauFun_apply_lt a b k h1 h2

lemma tau_apply_lt_val (a b k : Fin N) (hab : a < b) (h1 : a.val ≤ k.val) (h2 : k.val < b.val) :
    (tau a b hab k).val = k.val + 1 := by
  rw [tau_apply_lt a b k hab h1 h2]

lemma tau_apply_outside (a b k : Fin N) (hab : a < b) (h : k.val < a.val ∨ b.val < k.val) :
    tau a b hab k = k := by
  rw [tau_eq_tauFun]; exact tauFun_apply_outside a b k hab h

lemma tau_apply_outside_val (a b k : Fin N) (hab : a < b)
    (h : k.val < a.val ∨ b.val < k.val) : (tau a b hab k).val = k.val := by
  rw [tau_apply_outside a b k hab h]

/-- The inverse of `τ_{a,b}` moves backward through `[a,b]`: `a ↦ b`, `k ↦ k-1` for
`k ∈ (a,b]`, identity outside. -/
lemma tau_inv_apply_a (a b : Fin N) (hab : a < b) : (tau a b hab)⁻¹ a = b := by
  rw [Equiv.Perm.inv_eq_iff_eq]
  exact (tau_apply_b a b hab).symm

lemma tau_inv_apply_a_val (a b : Fin N) (hab : a < b) : ((tau a b hab)⁻¹ a).val = b.val := by
  rw [tau_inv_apply_a]

lemma tau_inv_apply_gt (a b k : Fin N) (hab : a < b) (h1 : a.val < k.val) (h2 : k.val ≤ b.val) :
    (tau a b hab)⁻¹ k = ⟨k.val - 1, by omega⟩ := by
  rw [Equiv.Perm.inv_eq_iff_eq]
  apply Fin.ext
  have e1 : a.val ≤ k.val - 1 := by omega
  have e2 : k.val - 1 < b.val := by omega
  rw [tau_apply_lt_val a b ⟨k.val - 1, by omega⟩ hab e1 e2]
  show k.val = (k.val - 1) + 1
  omega

lemma tau_inv_apply_gt_val (a b k : Fin N) (hab : a < b) (h1 : a.val < k.val)
    (h2 : k.val ≤ b.val) : ((tau a b hab)⁻¹ k).val = k.val - 1 := by
  rw [tau_inv_apply_gt a b k hab h1 h2]

lemma tau_inv_apply_outside (a b k : Fin N) (hab : a < b) (h : k.val < a.val ∨ b.val < k.val) :
    (tau a b hab)⁻¹ k = k := by
  rw [Equiv.Perm.inv_eq_iff_eq]
  exact (tau_apply_outside a b k hab h).symm

lemma tau_inv_apply_outside_val (a b k : Fin N) (hab : a < b)
    (h : k.val < a.val ∨ b.val < k.val) : ((tau a b hab)⁻¹ k).val = k.val := by
  rw [tau_inv_apply_outside a b k hab h]

/-- Closed value formula for `τ_{a,b}`: a single `if`-cascade over `ℕ`-values, so that
every later ordering argument reduces to `split_ifs <;> omega`. -/
lemma tau_val (a b : Fin N) (hab : a < b) (k : Fin N) :
    (tau a b hab k).val =
      if k = b then a.val
      else if a.val ≤ k.val ∧ k.val < b.val then k.val + 1 else k.val := by
  have hab' : a.val < b.val := hab
  by_cases hkb : k = b
  · rw [if_pos hkb, hkb, tau_apply_b_val]
  · rw [if_neg hkb]
    by_cases hin : a.val ≤ k.val ∧ k.val < b.val
    · rw [if_pos hin, tau_apply_lt_val a b k hab hin.1 hin.2]
    · have hkb' : k.val ≠ b.val := fun h => hkb (Fin.ext h)
      have hout : k.val < a.val ∨ b.val < k.val := by omega
      rw [if_neg hin, tau_apply_outside_val a b k hab hout]

/-- **The adjacent case `b = a+1` is a self-inverse transposition**
(Appendix C: "when `b=a+1`, the cycle is a transposition and the two displayed
permutations coincide"). -/
theorem tau_self_inv_of_adjacent (a b : Fin N) (hab : a < b) (hadj : b.val = a.val + 1) :
    tau a b hab = (tau a b hab)⁻¹ := by
  have hab' : a.val < b.val := hab
  ext k
  by_cases hka : k = a
  · rw [hka, tau_apply_lt_val a b a hab (le_refl _) (by omega),
      tau_inv_apply_a_val a b hab]
    omega
  · by_cases hkb : k = b
    · rw [hkb, tau_apply_b_val, tau_inv_apply_gt_val a b b hab (by omega) (le_refl _)]
      omega
    · have hka' : k.val ≠ a.val := fun h => hka (Fin.ext h)
      have hout : k.val < a.val ∨ b.val < k.val := by omega
      rw [tau_apply_outside_val a b k hab hout, tau_inv_apply_outside_val a b k hab hout]

/-- **Non-adjacent case: `τ_{a,b} ≠ τ_{a,b}^{-1}`** when the interval has length `> 2`. -/
theorem tau_ne_inv_of_not_adjacent (a b : Fin N) (hab : a < b) (hna : b.val ≠ a.val + 1) :
    tau a b hab ≠ (tau a b hab)⁻¹ := by
  have hab' : a.val < b.val := hab
  intro hcontra
  have h1 : (tau a b hab a).val = a.val + 1 := tau_apply_lt_val a b a hab (le_refl _) (by omega)
  have h2 : ((tau a b hab)⁻¹ a).val = b.val := tau_inv_apply_a_val a b hab
  rw [hcontra] at h1
  omega

end HorizonFormal.S1Paper
