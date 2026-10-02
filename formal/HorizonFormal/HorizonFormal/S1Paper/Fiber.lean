import HorizonFormal.S1Paper.AlmostChain
import Mathlib.Order.Interval.Finset.Fin

/-!
# The fiber lemma `Γ_{C_{a,b}} = {τ_{a,b}, τ_{a,b}^{-1}}` (Appendix C (C.1)–(C.5))

This is the `CLASS_SUM_TO_POSET_BRIDGE` step: the manuscript's (C.5), proved here
in full rather than assumed.

The manuscript's argument is realizer-theoretic: a linear extension of `C_{a,b}`
inserts `z` after `k ∈ {a,…,b}` chain elements (`L_k`), and `L_s ∩ L_t = C_{a,b}`
exactly when `{s,t}={a,b}`, so the only ordered realizer pairs are `(L_a,L_b)` and
`(L_b,L_a)`, giving `τ_{a,b}` and its inverse.

Formalized in exactly that shape:

* `IsExtension` — `π` is (the rank function of) a linear extension of `P_τ`.
* `extension_val` — **the classification of linear extensions**: every extension of
  `P_{τ_{a,b}}` is `L_k` for `k = π b ∈ [a,b]`, with the closed value formula. This
  replaces the manuscript's one-line "every linear extension inserts `z` after
  exactly `k ∈ {a,…,b}` elements".
* `fiber_eq` — (C.5) itself.

The proof of `extension_val` is a counting argument: `(π x).val` is the number of
`j` with `π j < π x`, split into the `j ≠ b` part (where the extension is forced to
be strictly monotone, since only pairs `(i,b)` with `a ≤ i < b` are incomparable in
`P_τ`) and the single `j = b`.
-/

namespace HorizonFormal.S1Paper

open Finset

variable {N : ℕ}

/-! ## Counting helpers -/

lemma card_filter_val_lt (y : Fin N) :
    (univ.filter (fun i : Fin N => i.val < y.val)).card = y.val := by
  have h : (univ.filter (fun i : Fin N => i.val < y.val)) = Finset.Iio y := by
    ext i
    simp only [mem_filter, mem_univ, true_and, Finset.mem_Iio, Fin.lt_def]
  rw [h, Fin.card_Iio]

lemma card_filter_val_le (y : Fin N) :
    (univ.filter (fun i : Fin N => i.val ≤ y.val)).card = y.val + 1 := by
  have h : (univ.filter (fun i : Fin N => i.val ≤ y.val)) = Finset.Iic y := by
    ext i
    simp only [mem_filter, mem_univ, true_and, Finset.mem_Iic, Fin.le_def]
  rw [h, Fin.card_Iic]

/-- For a permutation of `Fin N`, the number of `j` with `π j < y` is `y`. -/
lemma card_lt_perm (π : Equiv.Perm (Fin N)) (y : Fin N) :
    (univ.filter (fun j : Fin N => (π j).val < y.val)).card = y.val := by
  have h : (univ.filter (fun j : Fin N => (π j).val < y.val))
      = (univ.filter (fun z : Fin N => z.val < y.val)).map π.symm.toEmbedding := by
    ext j
    simp only [mem_filter, mem_univ, true_and, Finset.mem_map, Equiv.coe_toEmbedding]
    constructor
    · intro h; exact ⟨π j, h, by simp⟩
    · rintro ⟨z, hz, rfl⟩; simpa using hz
  rw [h, Finset.card_map, card_filter_val_lt]

/-- Split a cardinality over the single index `b`. -/
lemma card_split_erase (b : Fin N) (P : Fin N → Prop) [DecidablePred P] :
    (univ.filter P).card = ((univ.erase b).filter P).card + (if P b then 1 else 0) := by
  have h : (univ : Finset (Fin N)) = insert b (univ.erase b) :=
    (Finset.insert_erase (Finset.mem_univ b)).symm
  conv_lhs => rw [h]
  rw [Finset.filter_insert]
  split_ifs with hp
  · rw [Finset.card_insert_of_notMem (by simp)]
  · rfl

/-! ## Comparability in `P_{τ_{a,b}}`

The incomparable pairs of `P_{τ_{a,b}}` are exactly `(i,b)` with `a ≤ i < b` — this
is the manuscript's (C.2) with `z = b` and the chain `Fin N \ {b}`. -/

lemma leSigma_tau_of_val (a b : Fin N) (hab : a < b) {i j : Fin N}
    (hij : i.val ≤ j.val) (hne : ¬ (j.val = b.val ∧ a.val ≤ i.val ∧ i.val < b.val)) :
    leSigma (tau a b hab) i j := by
  have hab' : a.val < b.val := hab
  refine ⟨Fin.le_def.mpr hij, ?_⟩
  rw [Fin.le_def, tau_val, tau_val]
  simp only [Fin.ext_iff]
  split_ifs <;> omega

/-- `a ∦ b` in `P_{τ_{a,b}}`: the incomparability that makes the class non-trivial. -/
lemma not_leSigma_tau_a_b (a b : Fin N) (hab : a < b) : ¬ leSigma (tau a b hab) a b := by
  have hab' : a.val < b.val := hab
  rintro ⟨-, h2⟩
  rw [Fin.le_def, tau_val, tau_val] at h2
  simp only [Fin.ext_iff] at h2
  split_ifs at h2 <;> omega

/-! ## Linear extensions of `P_τ` -/

/-- `b - 1`: the chain element immediately below `z = b`, used as the second probe
that pins down where an extension places `z`. -/
def predB (b : Fin N) : Fin N := ⟨b.val - 1, lt_of_le_of_lt (Nat.sub_le _ _) b.isLt⟩

@[simp] lemma predB_val (b : Fin N) : (predB b).val = b.val - 1 := rfl

/-- `π` is the rank function of a linear extension of `P_τ`. -/
def IsExtension (τ π : Equiv.Perm (Fin N)) : Prop := ∀ i j, leSigma τ i j → π i ≤ π j

section Extension

variable {a b : Fin N} {hab : a < b} {π : Equiv.Perm (Fin N)}

/-- Away from `b`, an extension is strictly monotone: all such pairs are comparable. -/
lemma ext_strict (hext : IsExtension (tau a b hab) π)
    {i j : Fin N} (hjb : j ≠ b) (hlt : i.val < j.val) :
    (π i).val < (π j).val := by
  have hcomp := hext i j (leSigma_tau_of_val a b hab (le_of_lt hlt)
    (by rintro ⟨h1, -, -⟩; exact hjb (Fin.ext h1)))
  have hij : i ≠ j := fun h => by rw [h] at hlt; omega
  exact Fin.lt_def.mp (lt_of_le_of_ne hcomp (π.injective.ne hij))

lemma ext_lt_b (hext : IsExtension (tau a b hab) π) {i : Fin N} (hi : i.val < a.val) :
    (π i).val < (π b).val := by
  have hab' : a.val < b.val := hab
  have hib : i ≠ b := fun h => by rw [h] at hi; omega
  have hcomp := hext i b (leSigma_tau_of_val a b hab (by omega) (by rintro ⟨-, h, -⟩; omega))
  exact Fin.lt_def.mp (lt_of_le_of_ne hcomp (π.injective.ne hib))

lemma ext_gt_b (hext : IsExtension (tau a b hab) π) {j : Fin N} (hj : b.val < j.val) :
    (π b).val < (π j).val := by
  have hjb : b ≠ j := fun h => by rw [h] at hj; omega
  have hcomp := hext b j (leSigma_tau_of_val a b hab (by omega)
    (by rintro ⟨h1, -, h3⟩; omega))
  exact Fin.lt_def.mp (lt_of_le_of_ne hcomp (π.injective.ne hjb))

/-- **Classification of the linear extensions of `P_{τ_{a,b}}`** (manuscript: "every
linear extension is obtained by inserting `z` after exactly `k ∈ {a,…,b}` elements of
the chain"). The extension is completely determined by `k = π b`, which is forced into
`[a,b]`, and then `π = L_k`. -/
theorem extension_val (hext : IsExtension (tau a b hab) π) :
    a.val ≤ (π b).val ∧ (π b).val ≤ b.val ∧
      ∀ i : Fin N, (π i).val =
        if i = b then (π b).val
        else if (π b).val ≤ i.val ∧ i.val < b.val then i.val + 1 else i.val := by
  have hab' : a.val < b.val := hab
  set k : ℕ := (π b).val with hk
  -- `W` = the elements other than `b` that `π` puts below `b`.
  set W : Finset (Fin N) := (univ.erase b).filter (fun j => (π j).val < k) with hW
  have hWcard : W.card = k := by
    have h := card_lt_perm π (π b)
    rw [card_split_erase b (fun j => (π j).val < (π b).val)] at h
    simpa [hW, hk] using h
  have hWmem : ∀ {j : Fin N}, j ∈ W ↔ (j ≠ b ∧ (π j).val < k) := by
    intro j; simp [hW, Finset.mem_filter, Finset.mem_erase]
  -- every member of `W` sits strictly below `b`
  have hWlt : ∀ {j : Fin N}, j ∈ W → j.val < b.val := by
    intro j hj
    obtain ⟨hjb, hjk⟩ := hWmem.mp hj
    have : j.val ≠ b.val := fun h => hjb (Fin.ext h)
    rcases Nat.lt_or_ge j.val b.val with h | h
    · exact h
    · have hgt := ext_gt_b hext (j := j) (by omega)
      omega
  have hkb : k ≤ b.val := by
    rw [← hWcard, ← card_filter_val_lt b]
    exact Finset.card_le_card (by intro x hx; simp only [mem_filter, mem_univ, true_and]
                                  exact hWlt hx)
  have hak : a.val ≤ k := by
    rw [← hWcard, ← card_filter_val_lt a]
    refine Finset.card_le_card ?_
    intro x hx
    simp only [mem_filter, mem_univ, true_and] at hx
    exact hWmem.mpr ⟨fun h => by rw [h] at hx; omega, ext_lt_b hext hx⟩
  -- the key equivalence: below `b` in `π`-order iff below `k` in the natural order
  have hK : ∀ j : Fin N, j ≠ b → ((π j).val < k ↔ j.val < k) := by
    intro j hjb
    constructor
    · intro hj
      have hjlt : j.val < b.val := hWlt (hWmem.mpr ⟨hjb, hj⟩)
      have hsub : (univ.filter (fun i : Fin N => i.val ≤ j.val)) ⊆ W := by
        intro i hi
        simp only [mem_filter, mem_univ, true_and] at hi
        have hib : i ≠ b := fun h => by rw [h] at hi; omega
        refine hWmem.mpr ⟨hib, ?_⟩
        rcases Nat.eq_or_lt_of_le hi with h | h
        · have : i = j := Fin.ext h
          rw [this]; exact hj
        · exact lt_trans (ext_strict hext hjb h) hj
      have := Finset.card_le_card hsub
      rw [card_filter_val_le, hWcard] at this
      omega
    · intro hj
      by_contra hcon
      have hsub : W ⊆ (univ.filter (fun i : Fin N => i.val < j.val)) := by
        intro i hi
        obtain ⟨hib, hik⟩ := hWmem.mp hi
        simp only [mem_filter, mem_univ, true_and]
        rcases Nat.lt_or_ge i.val j.val with h | h
        · exact h
        · rcases Nat.eq_or_lt_of_le h with h' | h'
          · exact absurd hik (by rw [show i = j from Fin.ext h'.symm]; exact hcon)
          · exact absurd (lt_trans (ext_strict hext hib h') hik) hcon
      have := Finset.card_le_card hsub
      rw [card_filter_val_lt, hWcard] at this
      omega
  refine ⟨hak, hkb, ?_⟩
  intro i
  by_cases hib : i = b
  · rw [if_pos hib, hib]
  · rw [if_neg hib]
    have hibval : i.val ≠ b.val := fun h => hib (Fin.ext h)
    -- count the elements `π`-below `i`
    have hcount := card_lt_perm π (π i)
    rw [card_split_erase b (fun j => (π j).val < (π i).val)] at hcount
    have hfil : ((univ.erase b).filter (fun j => (π j).val < (π i).val))
        = ((univ.erase b).filter (fun j : Fin N => j.val < i.val)) := by
      refine Finset.filter_congr ?_
      intro j hj
      simp only [Finset.mem_erase, mem_univ, and_true] at hj
      constructor
      · intro h
        rcases Nat.lt_or_ge j.val i.val with h' | h'
        · exact h'
        · rcases Nat.eq_or_lt_of_le h' with h'' | h''
          · exact absurd (show j = i from Fin.ext h''.symm) (by rintro rfl; omega)
          · exact absurd (ext_strict hext hj h'') (by omega)
      · intro h; exact ext_strict hext hib h
    rw [hfil] at hcount
    have hbase := card_split_erase b (fun j : Fin N => j.val < i.val)
    rw [card_filter_val_lt] at hbase
    -- resolve the two `if`s
    have hne : (π i).val ≠ k := fun h => hib (π.injective (Fin.ext h))
    have hiff : (k < (π i).val) ↔ ¬ (i.val < k) := by
      rw [← hK i hib]; omega
    by_cases hlt : i.val < k
    · have h1 : ¬ (k < (π i).val) := by rw [hiff]; omega
      rw [if_neg h1] at hcount
      rw [if_neg (show ¬ (b.val < i.val) by omega)] at hbase
      rw [if_neg (show ¬ (k ≤ i.val ∧ i.val < b.val) by omega)]
      omega
    · have h1 : k < (π i).val := by rw [hiff]; omega
      rw [if_pos h1] at hcount
      by_cases hib2 : i.val < b.val
      · rw [if_neg (show ¬ (b.val < i.val) by omega)] at hbase
        rw [if_pos (show k ≤ i.val ∧ i.val < b.val from ⟨by omega, hib2⟩)]
        omega
      · rw [if_pos (show b.val < i.val by omega)] at hbase
        rw [if_neg (show ¬ (k ≤ i.val ∧ i.val < b.val) by omega)]
        omega

/-- The extension that places `z` first among its admissible slots **is** `τ_{a,b}`
(the manuscript's `L_a`). -/
theorem extension_eq_tau (hext : IsExtension (tau a b hab) π) (hb : (π b).val = a.val) :
    π = tau a b hab := by
  obtain ⟨-, -, hform⟩ := extension_val hext
  ext i
  rw [hform i, tau_val, hb]

/-- The extension that places `z` last among its admissible slots is the identity
(the manuscript's `L_b`). -/
theorem extension_eq_one (hext : IsExtension (tau a b hab) π) (hb : (π b).val = b.val) :
    π = 1 := by
  obtain ⟨-, -, hform⟩ := extension_val hext
  ext i
  have hval : (π i).val = i.val := by
    rw [hform i, hb]
    by_cases h : i = b
    · rw [if_pos h, h]
    · rw [if_neg h, if_neg (show ¬ ((b : Fin N).val ≤ i.val ∧ i.val < b.val) by omega)]
  simpa using hval

/-! ## The two probes that pin down `π b`

`a ∦ b` and `b-1 ∦ b` are incomparable in `P_{τ_{a,b}}`, so in an ordered *realizer*
pair the two extensions must disagree on each of them. Each disagreement pins one
endpoint of `[a,b]`. -/

lemma ext_a_le_b_iff (hext : IsExtension (tau a b hab) π) :
    ((π a).val ≤ (π b).val) ↔ (π b).val ≠ a.val := by
  have hab' : a.val < b.val := hab
  obtain ⟨hak, hkb, hform⟩ := extension_val hext
  have ha := hform a
  rw [if_neg (show a ≠ b from fun h => by rw [h] at hab'; omega)] at ha
  constructor
  · intro h hcon
    rw [if_pos (show (π b).val ≤ a.val ∧ a.val < b.val from ⟨by omega, hab'⟩)] at ha
    omega
  · intro h
    rw [if_neg (show ¬ ((π b).val ≤ a.val ∧ a.val < b.val) by omega)] at ha
    omega

lemma ext_b_le_pred_iff (hext : IsExtension (tau a b hab) π) :
    ((π b).val ≤ (π (predB b)).val) ↔ (π b).val < b.val := by
  have hab' : a.val < b.val := hab
  obtain ⟨hak, hkb, hform⟩ := extension_val hext
  have hpb : predB b ≠ b := fun h => by have := congrArg Fin.val h; simp only [predB_val] at this
                                        omega
  have hh := hform (predB b)
  rw [if_neg hpb, predB_val] at hh
  constructor
  · intro h
    by_contra hcon
    rw [if_neg (show ¬ ((π b).val ≤ b.val - 1 ∧ b.val - 1 < b.val) by omega)] at hh
    omega
  · intro h
    rw [if_pos (show (π b).val ≤ b.val - 1 ∧ b.val - 1 < b.val from ⟨by omega, by omega⟩)] at hh
    omega

end Extension

/-! ## The fiber lemma -/

/-- **Manuscript (C.5): `Γ_{C_{a,b}} = {τ_{a,b}, τ_{a,b}^{-1}}`.**

A permutation whose two-dimensional poset is isomorphic to the near-chain class
`C_{a,b}` is either `τ_{a,b}` or its inverse — and both of them are. This is the
`CLASS_SUM_TO_POSET_BRIDGE` step, proved rather than assumed.

The proof follows the manuscript exactly: an isomorphism `e : P_σ ≅ P_τ` pushes the
natural order and the `σ`-order forward to two linear extensions `π₁, π₂` of `P_τ`
whose intersection is `P_τ` again, i.e. an *ordered realizer pair*; `extension_val`
classifies extensions as `L_k`, `k ∈ [a,b]`, and the two incomparabilities `a ∦ b`,
`b-1 ∦ b` force `{k₁,k₂} = {a,b}`; then `σ = π₂ ∘ π₁⁻¹ ∈ {τ, τ⁻¹}`. -/
theorem fiber_eq (a b : Fin N) (hab : a < b) (σ : Equiv.Perm (Fin N)) :
    PosetIsomorphic σ (tau a b hab) ↔ (σ = tau a b hab ∨ σ = (tau a b hab)⁻¹) := by
  have hab' : a.val < b.val := hab
  constructor
  · rintro ⟨e, he⟩
    have hkey : ∀ x y : Fin N,
        leSigma σ (e.symm x) (e.symm y) ↔ leSigma (tau a b hab) x y := by
      intro x y
      have h := he (e.symm x) (e.symm y)
      rw [Equiv.apply_symm_apply, Equiv.apply_symm_apply] at h
      exact h
    have hext₁ : IsExtension (tau a b hab) e.symm := fun x y hxy => ((hkey x y).mpr hxy).1
    have hext₂ : IsExtension (tau a b hab) (e.symm.trans σ) :=
      fun x y hxy => ((hkey x y).mpr hxy).2
    have hinter : ∀ x y : Fin N,
        e.symm x ≤ e.symm y → σ (e.symm x) ≤ σ (e.symm y) → leSigma (tau a b hab) x y :=
      fun x y h1 h2 => (hkey x y).mp ⟨h1, h2⟩
    obtain ⟨hak1, hkb1, -⟩ := extension_val hext₁
    obtain ⟨hak2, hkb2, -⟩ := extension_val hext₂
    have hA : (e.symm b).val = a.val ∨ (σ (e.symm b)).val = a.val := by
      by_contra hcon
      rw [not_or] at hcon
      exact not_leSigma_tau_a_b a b hab
        (hinter a b (Fin.le_def.mpr ((ext_a_le_b_iff hext₁).mpr hcon.1))
                    (Fin.le_def.mpr ((ext_a_le_b_iff hext₂).mpr hcon.2)))
    have hB : (e.symm b).val = b.val ∨ (σ (e.symm b)).val = b.val := by
      by_contra hcon
      rw [not_or] at hcon
      have h1 : (e.symm b).val < b.val := lt_of_le_of_ne hkb1 hcon.1
      have h2 : (σ (e.symm b)).val < b.val := lt_of_le_of_ne hkb2 hcon.2
      refine absurd (hinter b (predB b)
        (Fin.le_def.mpr ((ext_b_le_pred_iff hext₁).mpr h1))
        (Fin.le_def.mpr ((ext_b_le_pred_iff hext₂).mpr h2))) ?_
      rintro ⟨h, -⟩
      rw [Fin.le_def, predB_val] at h
      omega
    have hcase : ((e.symm b).val = a.val ∧ (σ (e.symm b)).val = b.val) ∨
                 ((e.symm b).val = b.val ∧ (σ (e.symm b)).val = a.val) := by
      rcases hA with h | h <;> rcases hB with h' | h' <;> omega
    rcases hcase with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · -- `(π₁,π₂) = (L_a,L_b) = (τ,1)`, so `σ·τ = 1`
      right
      have e1 : e.symm = tau a b hab := extension_eq_tau hext₁ h1
      have e2 : e.symm.trans σ = 1 := extension_eq_one hext₂ h2
      have hmul : σ * (tau a b hab) = 1 := by rw [Equiv.Perm.mul_def, ← e1]; exact e2
      exact mul_eq_one_iff_eq_inv.mp hmul
    · -- `(π₁,π₂) = (L_b,L_a) = (1,τ)`, so `σ = τ`
      left
      have e1 : e.symm = (1 : Equiv.Perm (Fin N)) := extension_eq_one hext₁ h1
      have e2 : e.symm.trans σ = tau a b hab := extension_eq_tau hext₂ h2
      have hmul : σ * (1 : Equiv.Perm (Fin N)) = tau a b hab := by
        rw [Equiv.Perm.mul_def, ← e1]; exact e2
      simpa using hmul
  · rintro (rfl | rfl)
    · exact posetIsomorphic_refl _
    · exact posetIsomorphic_symm (posetIsomorphic_inv _)

/-! ## Pairwise distinctness of the near-chain classes

The manuscript separates the `binom N 2` classes by the multiset of strict-past
cardinalities (C.6). Once (C.5) is available the same conclusion follows more directly:
the non-fixed set of `τ_{a,b}` is exactly the interval `[a,b]`, and that interval is
invariant under inversion, so an isomorphism forces the endpoints to agree. -/

/-- The non-fixed points of `τ_{a,b}` are exactly the interval `[a,b]`. -/
lemma tau_ne_self_iff (a b : Fin N) (hab : a < b) (k : Fin N) :
    tau a b hab k ≠ k ↔ (a.val ≤ k.val ∧ k.val ≤ b.val) := by
  have hab' : a.val < b.val := hab
  rw [ne_eq, Fin.ext_iff, tau_val]
  simp only [Fin.ext_iff]
  split_ifs <;> omega

lemma inv_apply_eq_self_iff (σ : Equiv.Perm (Fin N)) (k : Fin N) :
    σ⁻¹ k = k ↔ σ k = k := by
  rw [Equiv.Perm.inv_eq_iff_eq, eq_comm]

/-- **The conclusion of (C.6)**: distinct pairs `a < b` give non-isomorphic near-chain
classes, so the construction really supplies `binom N 2` distinct classes `C_{a,b}`. -/
theorem almostChain_pair_eq_of_isomorphic {a b a' b' : Fin N} (hab : a < b) (hab' : a' < b')
    (h : PosetIsomorphic (tau a b hab) (tau a' b' hab')) : a = a' ∧ b = b' := by
  have hv : a.val < b.val := hab
  have hv' : a'.val < b'.val := hab'
  have hfix : ∀ k : Fin N,
      (a.val ≤ k.val ∧ k.val ≤ b.val) ↔ (a'.val ≤ k.val ∧ k.val ≤ b'.val) := by
    intro k
    rcases (fiber_eq a' b' hab' _).mp h with he | he
    · rw [← tau_ne_self_iff a b hab k, he, tau_ne_self_iff]
    · rw [← tau_ne_self_iff a b hab k, he, ne_eq, inv_apply_eq_self_iff, ← ne_eq,
        tau_ne_self_iff]
  have h1 := (hfix a).mp (by omega)
  have h2 := (hfix a').mpr (by omega)
  have h3 := (hfix b).mp (by omega)
  have h4 := (hfix b').mpr (by omega)
  exact ⟨Fin.ext (by omega), Fin.ext (by omega)⟩

end HorizonFormal.S1Paper
