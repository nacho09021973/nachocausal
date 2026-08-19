import HorizonFormal.RectangularDiscrepancy

/-!
# Semantic fidelity audit of `RectangularDiscrepancy.lean`

`RectangularDiscrepancy.lean` proves `n Δₙ(π) ≤ 4 D*` for objects defined with
zero-based ranks (`Fin n`) and half-open intervals.  The scientific note
`emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md` §2 defines them
with **one-based** ranks and closed intervals:

* `F(a,b) = #{i ≤ a : Π(i) ≤ b}` for `0 ≤ a,b ≤ n`,
* `D(a,b) = F(a,b) - ab/n`, `D* = max_{0≤a,b≤n} |D(a,b)|`,
* `I = {a₁+1,…,a₂}`, `J = {b₁+1,…,b₂}`, `N(I,J) = #{i ∈ I : Π(i) ∈ J}`,
* `Δₙ = max_{I,J} |N(I,J)/n - |I||J|/n²|`.

This file re-states those objects *from scratch* in the note's own language,
indexed by natural numbers, and proves that they are equal to the ones the
theorem file uses.  Nothing here is assumed: the bridge is proved, so the
capstone `note_lemma_2_1` is Lemma 2.1 exactly as written in the note.
-/

namespace HorizonFormal
namespace Fidelity

open Finset

variable {n : ℕ}

/-! ## The note's objects, one-based -/

/-- The note's `Π(r)`, for one-based ranks `r ∈ {1,…,n}` (junk value outside). -/
def piOne (π : Equiv.Perm (Fin n)) (r : ℕ) : ℕ :=
  if h : 1 ≤ r ∧ r ≤ n then (π ⟨r - 1, by obtain ⟨h1, h2⟩ := h; omega⟩).val + 1 else 0

/-- The note's `F(a,b) = #{i ≤ a : Π(i) ≤ b}`, with `i` ranging over `{1,…,n}`. -/
def FOne (π : Equiv.Perm (Fin n)) (a b : ℕ) : ℕ :=
  ((Icc 1 n).filter fun r => r ≤ a ∧ piOne π r ≤ b).card

/-- The note's `D(a,b) = F(a,b) - ab/n`. -/
noncomputable def DOne (π : Equiv.Perm (Fin n)) (a b : ℕ) : ℝ :=
  (FOne π a b : ℝ) - (a : ℝ) * (b : ℝ) / (n : ℝ)

/-- The note's `N(I,J) = #{i ∈ I : Π(i) ∈ J}` for `I = {a₁+1,…,a₂}`,
`J = {b₁+1,…,b₂}`. -/
def NOne (π : Equiv.Perm (Fin n)) (a₁ a₂ b₁ b₂ : ℕ) : ℕ :=
  ((Icc (a₁ + 1) a₂).filter fun r => b₁ + 1 ≤ piOne π r ∧ piOne π r ≤ b₂).card

/-- The note's `|N(I,J)/n - |I||J|/n²|`, the quantity maximised in (1.1). -/
noncomputable def deltaOne (π : Equiv.Perm (Fin n)) (a₁ a₂ b₁ b₂ : ℕ) : ℝ :=
  |(NOne π a₁ a₂ b₁ b₂ : ℝ) / (n : ℝ) -
    ((a₂ - a₁ : ℕ) : ℝ) * ((b₂ - b₁ : ℕ) : ℝ) / (n : ℝ) ^ 2|

/-! ## The bridge -/

theorem succ_injective : Function.Injective fun i : Fin n => i.val + 1 := by
  intro i j h
  dsimp only at h
  exact Fin.ext (by omega)

@[simp] theorem piOne_succ (π : Equiv.Perm (Fin n)) (i : Fin n) :
    piOne π (i.val + 1) = (π i).val + 1 := by
  have h : 1 ≤ i.val + 1 ∧ i.val + 1 ≤ n := ⟨by omega, i.isLt⟩
  rw [piOne, dif_pos h]
  simp

/-- The note's `F(a,b)` counts exactly what `cornerCount` counts. -/
theorem FOne_eq_cornerCount (π : Equiv.Perm (Fin n)) (a b : RankEndpoint n) :
    FOne π a.val b.val = cornerCount π a b := by
  classical
  rw [FOne, cornerCount, ← Finset.card_image_of_injective
    (univ.filter fun i : Fin n => i.val < a.val ∧ (π i).val < b.val) succ_injective]
  congr 1
  ext r
  simp only [mem_filter, mem_Icc, mem_image, mem_univ, true_and]
  constructor
  · rintro ⟨⟨h1, h2⟩, h3, h4⟩
    refine ⟨⟨r - 1, by omega⟩, ⟨?_, ?_⟩, by simp; omega⟩
    · show r - 1 < a.val
      omega
    · have hr : ((⟨r - 1, by omega⟩ : Fin n)).val + 1 = r := by simp; omega
      have := piOne_succ π (⟨r - 1, by omega⟩ : Fin n)
      rw [hr] at this
      omega
  · rintro ⟨i, ⟨hi1, hi2⟩, rfl⟩
    refine ⟨⟨by omega, by omega⟩, by omega, ?_⟩
    rw [piOne_succ]
    omega

/-- The note's `N(I,J)` counts exactly what `rectangleCount` counts. -/
theorem NOne_eq_rectangleCount (π : Equiv.Perm (Fin n)) (I J : RankInterval n) :
    NOne π I.lower.val I.upper.val J.lower.val J.upper.val = rectangleCount π I J := by
  classical
  rw [NOne, rectangleCount, ← Finset.card_image_of_injective
    (univ.filter fun i : Fin n => I.lower.val ≤ i.val ∧ i.val < I.upper.val ∧
      J.lower.val ≤ (π i).val ∧ (π i).val < J.upper.val) succ_injective]
  congr 1
  ext r
  simp only [mem_filter, mem_Icc, mem_image, mem_univ, true_and]
  have hup : I.upper.val ≤ n := Nat.lt_succ_iff.mp I.upper.isLt
  constructor
  · rintro ⟨⟨h1, h2⟩, h3, h4⟩
    have hrn : r ≤ n := le_trans h2 (Nat.lt_succ_iff.mp I.upper.isLt)
    refine ⟨⟨r - 1, by omega⟩, ⟨?_, ?_, ?_, ?_⟩, by simp; omega⟩
    · show I.lower.val ≤ r - 1
      omega
    · show r - 1 < I.upper.val
      omega
    · have hr : ((⟨r - 1, by omega⟩ : Fin n)).val + 1 = r := by simp; omega
      have := piOne_succ π (⟨r - 1, by omega⟩ : Fin n)
      rw [hr] at this
      omega
    · have hr : ((⟨r - 1, by omega⟩ : Fin n)).val + 1 = r := by simp; omega
      have := piOne_succ π (⟨r - 1, by omega⟩ : Fin n)
      rw [hr] at this
      omega
  · rintro ⟨i, ⟨hi1, hi2, hi3, hi4⟩, rfl⟩
    refine ⟨⟨by omega, by omega⟩, ?_, ?_⟩ <;> rw [piOne_succ] <;> omega

/-! ## Sanity of the one-based transcription -/

/-- The note's `|I| = #{a₁+1,…,a₂} = a₂ - a₁`: the cardinality that (1.1)
normalises by is the cardinality of the note's own interval. -/
theorem card_noteInterval (a₁ a₂ : ℕ) : ((Icc (a₁ + 1) a₂).card : ℕ) = a₂ - a₁ := by
  rw [Nat.card_Icc]
  omega

/-- `F(0,b) = 0`: the lower endpoint `a = 0` of the note's grid is the empty count. -/
theorem FOne_zero_left (π : Equiv.Perm (Fin n)) (b : ℕ) : FOne π 0 b = 0 := by
  classical
  rw [FOne, card_eq_zero, filter_eq_empty_iff]
  intro r hr
  rw [mem_Icc] at hr
  omega

/-- `F(n,n) = n`: the upper endpoint `a = b = n` of the note's grid counts everything. -/
theorem FOne_full (π : Equiv.Perm (Fin n)) : FOne π n n = n := by
  classical
  rw [FOne]
  have : ((Icc 1 n).filter fun r => r ≤ n ∧ piOne π r ≤ n) = Icc 1 n := by
    apply filter_true_of_mem
    intro r hr
    rw [mem_Icc] at hr
    refine ⟨hr.2, ?_⟩
    have hr' : ((⟨r - 1, by omega⟩ : Fin n)).val + 1 = r := by simp; omega
    have := piOne_succ π (⟨r - 1, by omega⟩ : Fin n)
    rw [hr'] at this
    have := (π (⟨r - 1, by omega⟩ : Fin n)).isLt
    omega
  rw [this, Nat.card_Icc]
  omega

/-- An empty rank interval `I = {a+1,…,a}` contributes no points. -/
theorem NOne_empty (π : Equiv.Perm (Fin n)) (a b₁ b₂ : ℕ) : NOne π a a b₁ b₂ = 0 := by
  classical
  rw [NOne, card_eq_zero, filter_eq_empty_iff]
  intro r hr
  rw [mem_Icc] at hr
  omega

/-! ## The note's maxima, taken over the note's own index sets -/

/-- `{|D(a,b)| : 0 ≤ a ≤ n, 0 ≤ b ≤ n}`, the set that (2.1) maximises. -/
noncomputable def DStarOneValues (π : Equiv.Perm (Fin n)) : Finset ℝ :=
  ((range (n + 1)) ×ˢ (range (n + 1))).image fun p => |DOne π p.1 p.2|

theorem DOne_eq_cornerDiscrepancy (π : Equiv.Perm (Fin n)) (a b : RankEndpoint n) :
    DOne π a.val b.val = cornerDiscrepancy π a b := by
  rw [DOne, cornerDiscrepancy, FOne_eq_cornerCount π a b]

theorem DStarOneValues_eq (π : Equiv.Perm (Fin n)) :
    DStarOneValues π = cornerDiscrepancyValues π := by
  classical
  ext x
  constructor
  · intro hx
    obtain ⟨p, hp, rfl⟩ := mem_image.mp hx
    obtain ⟨a, b⟩ := p
    simp only [mem_product, mem_range] at hp
    refine mem_image.mpr ⟨(⟨a, by omega⟩, ⟨b, by omega⟩), mem_univ _, ?_⟩
    rw [← DOne_eq_cornerDiscrepancy]
  · intro hx
    obtain ⟨p, _, rfl⟩ := mem_image.mp hx
    obtain ⟨a, b⟩ := p
    refine mem_image.mpr ⟨(a.val, b.val), ?_, ?_⟩
    · simp only [mem_product, mem_range]
      exact ⟨a.isLt, b.isLt⟩
    · rw [DOne_eq_cornerDiscrepancy]

theorem DStarOneValues_nonempty (π : Equiv.Perm (Fin n)) :
    (DStarOneValues π).Nonempty := by
  classical
  refine ⟨|DOne π 0 0|, mem_image.mpr ⟨(0, 0), ?_, rfl⟩⟩
  simp only [mem_product, mem_range]
  omega

/-- The note's `D* = max_{0≤a,b≤n} |D(a,b)|`. -/
noncomputable def DStarOne (π : Equiv.Perm (Fin n)) : ℝ :=
  (DStarOneValues π).max' (DStarOneValues_nonempty π)

theorem DStarOne_eq (π : Equiv.Perm (Fin n)) :
    DStarOne π = cornerDiscrepancyStar π := by
  rw [DStarOne, cornerDiscrepancyStar]
  congr 1
  exact DStarOneValues_eq π

/-- The note's index set for (1.1): `0 ≤ a₁ ≤ a₂ ≤ n` and `0 ≤ b₁ ≤ b₂ ≤ n`. -/
def rectIndex (n : ℕ) : Finset (ℕ × ℕ × ℕ × ℕ) :=
  ((range (n + 1)) ×ˢ ((range (n + 1)) ×ˢ ((range (n + 1)) ×ˢ (range (n + 1))))).filter
    fun q => q.1 ≤ q.2.1 ∧ q.2.2.1 ≤ q.2.2.2

theorem mem_rectIndex {a₁ a₂ b₁ b₂ : ℕ} :
    (a₁, a₂, b₁, b₂) ∈ rectIndex n ↔
      ((a₁ ≤ a₂ ∧ a₂ ≤ n) ∧ (b₁ ≤ b₂ ∧ b₂ ≤ n)) := by
  simp only [rectIndex, mem_filter, mem_product, mem_range]
  omega

/-- `{|N(I,J)/n - |I||J|/n²| : I, J rank intervals}`, the set (1.1) maximises. -/
noncomputable def DeltaOneValues (π : Equiv.Perm (Fin n)) : Finset ℝ :=
  (rectIndex n).image fun q => deltaOne π q.1 q.2.1 q.2.2.1 q.2.2.2

theorem deltaOne_eq_normalized (π : Equiv.Perm (Fin n)) (I J : RankInterval n) :
    deltaOne π I.lower.val I.upper.val J.lower.val J.upper.val
      = normalizedRectangleDiscrepancy π I J := by
  rw [deltaOne, normalizedRectangleDiscrepancy, NOne_eq_rectangleCount]
  rfl

theorem DeltaOneValues_eq (π : Equiv.Perm (Fin n)) :
    DeltaOneValues π = rectangularDiscrepancyValues π := by
  classical
  ext x
  constructor
  · intro hx
    obtain ⟨q, hq, rfl⟩ := mem_image.mp hx
    obtain ⟨a₁, a₂, b₁, b₂⟩ := q
    obtain ⟨⟨h1, h2⟩, h3, h4⟩ := mem_rectIndex.mp hq
    refine mem_image.mpr ⟨(⟨(⟨a₁, by omega⟩, ⟨a₂, by omega⟩), h1⟩,
      ⟨(⟨b₁, by omega⟩, ⟨b₂, by omega⟩), h3⟩), mem_univ _, ?_⟩
    rw [← deltaOne_eq_normalized]
    rfl
  · intro hx
    obtain ⟨p, _, rfl⟩ := mem_image.mp hx
    obtain ⟨I, J⟩ := p
    refine mem_image.mpr ⟨(I.lower.val, I.upper.val, J.lower.val, J.upper.val), ?_, ?_⟩
    · exact mem_rectIndex.mpr ⟨⟨I.lower_le_upper, Nat.lt_succ_iff.mp I.upper.isLt⟩,
        J.lower_le_upper, Nat.lt_succ_iff.mp J.upper.isLt⟩
    · rw [deltaOne_eq_normalized]

theorem DeltaOneValues_nonempty (π : Equiv.Perm (Fin n)) :
    (DeltaOneValues π).Nonempty := by
  classical
  refine ⟨deltaOne π 0 0 0 0, mem_image.mpr ⟨(0, 0, 0, 0), ?_, rfl⟩⟩
  exact mem_rectIndex.mpr ⟨⟨le_rfl, Nat.zero_le n⟩, le_rfl, Nat.zero_le n⟩

/-- The note's `Δₙ` of (1.1). -/
noncomputable def DeltaOne (π : Equiv.Perm (Fin n)) : ℝ :=
  (DeltaOneValues π).max' (DeltaOneValues_nonempty π)

theorem DeltaOne_eq (π : Equiv.Perm (Fin n)) :
    DeltaOne π = rectangularDiscrepancy π := by
  rw [DeltaOne, rectangularDiscrepancy]
  congr 1
  exact DeltaOneValues_eq π

/-! ## Coverage: the maxima really see the whole domain of the note -/

/-- Every corner with `0 ≤ a,b ≤ n` — endpoints `0` and `n` included — is under `D*`. -/
theorem abs_DOne_le_DStarOne (π : Equiv.Perm (Fin n)) {a b : ℕ} (ha : a ≤ n) (hb : b ≤ n) :
    |DOne π a b| ≤ DStarOne π := by
  classical
  have hmem : |DOne π a b| ∈ DStarOneValues π := by
    simp only [DStarOneValues, mem_image, mem_product, mem_range, Prod.exists]
    exact ⟨a, b, ⟨by omega, by omega⟩, rfl⟩
  exact le_max' _ _ hmem

/-- The four extreme corners of the note's grid are inside the maximum. -/
theorem extreme_corners_le_DStarOne (π : Equiv.Perm (Fin n)) :
    |DOne π 0 0| ≤ DStarOne π ∧ |DOne π 0 n| ≤ DStarOne π ∧
      |DOne π n 0| ≤ DStarOne π ∧ |DOne π n n| ≤ DStarOne π :=
  ⟨abs_DOne_le_DStarOne π (Nat.zero_le n) (Nat.zero_le n),
   abs_DOne_le_DStarOne π (Nat.zero_le n) le_rfl,
   abs_DOne_le_DStarOne π le_rfl (Nat.zero_le n),
   abs_DOne_le_DStarOne π le_rfl le_rfl⟩

/-- Every rank rectangle the note allows is under `Δₙ`. -/
theorem deltaOne_le_DeltaOne (π : Equiv.Perm (Fin n)) {a₁ a₂ b₁ b₂ : ℕ}
    (h1 : a₁ ≤ a₂) (h2 : a₂ ≤ n) (h3 : b₁ ≤ b₂) (h4 : b₂ ≤ n) :
    deltaOne π a₁ a₂ b₁ b₂ ≤ DeltaOne π := by
  classical
  have hmem : deltaOne π a₁ a₂ b₁ b₂ ∈ DeltaOneValues π := by
    simp only [DeltaOneValues, mem_image]
    exact ⟨(a₁, a₂, b₁, b₂), mem_rectIndex.mpr ⟨⟨h1, h2⟩, h3, h4⟩, rfl⟩
  exact le_max' _ _ hmem

/-- In particular the full rectangle `I = J = {1,…,n}` is inside the maximum. -/
theorem full_rectangle_le_DeltaOne (π : Equiv.Perm (Fin n)) :
    deltaOne π 0 n 0 n ≤ DeltaOne π :=
  deltaOne_le_DeltaOne π (Nat.zero_le n) le_rfl (Nat.zero_le n) le_rfl

/-! ## Capstone -/

/--
**Lemma 2.1 of `P1a_count_volume_rectangular_discrepancy_l2_d2.md` §2**, stated
entirely in the note's one-based language: `n Δₙ ≤ 4 D*`, where `Δₙ` is the
maximum of `|N(I,J)/n - |I||J|/n²|` over `I = {a₁+1,…,a₂}`, `J = {b₁+1,…,b₂}`
with `0 ≤ a₁ ≤ a₂ ≤ n`, `0 ≤ b₁ ≤ b₂ ≤ n`, and `D*` is the maximum of
`|F(a,b) - ab/n|` over `0 ≤ a,b ≤ n` with `F(a,b) = #{i ≤ a : Π(i) ≤ b}`.
-/
theorem note_lemma_2_1 (hn : 1 ≤ n) (π : Equiv.Perm (Fin n)) :
    (n : ℝ) * DeltaOne π ≤ 4 * DStarOne π := by
  rw [DeltaOne_eq, DStarOne_eq]
  exact n_mul_rectangularDiscrepancy_le_four_mul_cornerDiscrepancyStar hn π

end Fidelity
end HorizonFormal

/-! ## Axiom audit -/

#print axioms HorizonFormal.n_mul_rectangularDiscrepancy_le_four_mul_cornerDiscrepancyStar
#print axioms HorizonFormal.Fidelity.note_lemma_2_1
#print axioms HorizonFormal.Fidelity.FOne_eq_cornerCount
#print axioms HorizonFormal.Fidelity.NOne_eq_rectangleCount
