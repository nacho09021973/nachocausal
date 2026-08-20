import HorizonFormal.RectangularDiscrepancyFidelity

/-!
# Deterministic rank bridge

This file isolates the deterministic content of Lemma 3.1.  It assumes that a
finite sample in `[0,1]²` has no ties, that two permutations enumerate the
sample in nondecreasing coordinate order, and that `π` is the resulting rank
permutation.  No probability space, null event, measurability statement, or
distributional assertion occurs here.

The analytic input is deliberately abstract: `EmpiricalProcessDominatedBy`
says that a number `W` bounds the anchored empirical process at every point of
`[0,1]²`.  The theorem proves from these deterministic hypotheses that
`D* ≤ 3 n W`.
-/

namespace HorizonFormal

open Finset Set

/-- The number of sample points in the closed anchored rectangle
`[0,x] × [0,y]`. -/
noncomputable def empiricalCornerCount {n : ℕ} (u v : Fin n → ℝ) (x y : ℝ) : ℕ :=
  ((Finset.univ : Finset (Fin n)).filter fun i => u i ≤ x ∧ v i ≤ y).card

/-- `W` dominates the anchored empirical process of the labelled sample.

This predicate is the exact deterministic interface that the later
probabilistic definition of `W` must discharge. -/
def EmpiricalProcessDominatedBy {n : ℕ} (u v : Fin n → ℝ) (W : ℝ) : Prop :=
  ∀ x ∈ Set.Icc (0 : ℝ) 1, ∀ y ∈ Set.Icc (0 : ℝ) 1,
    |(empiricalCornerCount u v x y : ℝ) / (n : ℝ) - x * y| ≤ W

/-- Explicit deterministic rank data.

`uOrder` and `vOrder` send a zero-based rank to the original sample label.
The injectivity fields are precisely the no-ties hypotheses.  Monotonicity
says that the proposed orders are correct.  The last field fixes the
orientation of the rank permutation: `π r` is the `v`-rank of the point whose
`u`-rank is `r`. -/
structure StrictRankCoupling {n : ℕ} (u v : Fin n → ℝ)
    (π : Equiv.Perm (Fin n)) where
  uOrder : Equiv.Perm (Fin n)
  vOrder : Equiv.Perm (Fin n)
  u_noTies : Function.Injective u
  v_noTies : Function.Injective v
  uOrder_monotone : Monotone (u ∘ uOrder)
  vOrder_monotone : Monotone (v ∘ vOrder)
  rankPermutation_eq : π = uOrder.trans vOrder.symm

namespace StrictRankCoupling

variable {n : ℕ} {u v : Fin n → ℝ} {π : Equiv.Perm (Fin n)}
    (C : StrictRankCoupling u v π)

/-- Correct ordering plus no ties makes the ordered `u` coordinates strict. -/
theorem uOrder_strictMono : StrictMono (u ∘ C.uOrder) :=
  C.uOrder_monotone.strictMono_of_injective
    (C.u_noTies.comp C.uOrder.injective)

/-- Correct ordering plus no ties makes the ordered `v` coordinates strict. -/
theorem vOrder_strictMono : StrictMono (v ∘ C.vOrder) :=
  C.vOrder_monotone.strictMono_of_injective
    (C.v_noTies.comp C.vOrder.injective)

/-- A point's label is recovered either from its `u`-rank or from its
corresponding `v`-rank. -/
theorem vOrder_apply_rankPermutation (r : Fin n) : C.vOrder (π r) = C.uOrder r := by
  simp [C.rankPermutation_eq]

/-- At two order statistics, the empirical count is exactly the permutation
corner count. -/
theorem cornerCount_eq_empiricalCornerCount (a b : Fin n) :
    cornerCount π a.succ b.succ =
      empiricalCornerCount u v (u (C.uOrder a)) (v (C.vOrder b)) := by
  classical
  rw [cornerCount, empiricalCornerCount]
  apply Finset.card_equiv C.uOrder
  intro r
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  have hu : u (C.uOrder r) ≤ u (C.uOrder a) ↔ r ≤ a :=
    C.uOrder_strictMono.le_iff_le
  have hv : v (C.uOrder r) ≤ v (C.vOrder b) ↔ π r ≤ b := by
    rw [← C.vOrder_apply_rankPermutation r]
    exact C.vOrder_strictMono.le_iff_le
  simp only [Fin.val_succ]
  rw [hu, hv]
  omega

/-- The `u` marginal at its `(a+1)`-st order statistic contains exactly
`a+1` sample points. -/
theorem empiricalCornerCount_uOrder_one
    (hv_upper : ∀ i, v i ≤ 1) (a : Fin n) :
    empiricalCornerCount u v (u (C.uOrder a)) 1 = a.val + 1 := by
  classical
  rw [empiricalCornerCount]
  calc
    ((univ.filter fun i : Fin n => u i ≤ u (C.uOrder a) ∧ v i ≤ 1).card) =
        (Finset.Iic a).card := by
      symm
      apply Finset.card_equiv C.uOrder
      intro r
      simp only [Finset.mem_Iic, Finset.mem_filter, Finset.mem_univ, true_and]
      have hu : u (C.uOrder r) ≤ u (C.uOrder a) ↔ r ≤ a :=
        C.uOrder_strictMono.le_iff_le
      constructor
      · intro hra
        exact ⟨hu.mpr hra, hv_upper (C.uOrder r)⟩
      · intro h
        exact hu.mp h.1
    _ = a.val + 1 := by simp

/-- The `v` marginal at its `(b+1)`-st order statistic contains exactly
`b+1` sample points. -/
theorem empiricalCornerCount_one_vOrder
    (hu_upper : ∀ i, u i ≤ 1) (b : Fin n) :
    empiricalCornerCount u v 1 (v (C.vOrder b)) = b.val + 1 := by
  classical
  rw [empiricalCornerCount]
  calc
    ((univ.filter fun i : Fin n => u i ≤ 1 ∧ v i ≤ v (C.vOrder b)).card) =
        (Finset.Iic b).card := by
      symm
      apply Finset.card_equiv C.vOrder
      intro r
      simp only [Finset.mem_Iic, Finset.mem_filter, Finset.mem_univ, true_and]
      have hv : v (C.vOrder r) ≤ v (C.vOrder b) ↔ r ≤ b :=
        C.vOrder_strictMono.le_iff_le
      constructor
      · intro hrb
        exact ⟨hu_upper (C.vOrder r), hv.mpr hrb⟩
      · intro h
        exact hv.mp h.2
    _ = b.val + 1 := by simp

end StrictRankCoupling

/-- Any number dominating an absolute empirical-process error is nonnegative. -/
theorem EmpiricalProcessDominatedBy.nonneg {n : ℕ} {u v : Fin n → ℝ} {W : ℝ}
    (hW : EmpiricalProcessDominatedBy u v W) : 0 ≤ W := by
  have h := hW 0 ⟨le_rfl, zero_le_one⟩ 0 ⟨le_rfl, zero_le_one⟩
  exact (abs_nonneg _).trans h

/-- The elementary product estimate used in Lemma 3.1. -/
private theorem abs_mul_sub_mul_le_two_mul
    {x y A B W : ℝ}
    (hy0 : 0 ≤ y) (hy1 : y ≤ 1) (hA0 : 0 ≤ A) (hA1 : A ≤ 1)
    (hW0 : 0 ≤ W) (hx : |x - A| ≤ W) (hy : |y - B| ≤ W) :
    |x * y - A * B| ≤ 2 * W := by
  rw [show x * y - A * B = (x - A) * y + A * (y - B) by ring]
  calc
    |(x - A) * y + A * (y - B)| ≤ |(x - A) * y| + |A * (y - B)| :=
      abs_add_le _ _
    _ = |x - A| * y + A * |y - B| := by
      rw [abs_mul, abs_mul, abs_of_nonneg hy0, abs_of_nonneg hA0]
    _ ≤ W * 1 + 1 * W := by
      exact add_le_add (mul_le_mul hx hy1 hy0 hW0)
        (mul_le_mul hA1 hy (abs_nonneg _) zero_le_one)
    _ = 2 * W := by ring

/-- Every corner discrepancy is bounded by `3 n W` under the deterministic
rank hypotheses.  Endpoints equal to zero are included explicitly. -/
theorem abs_cornerDiscrepancy_le_three_mul_n_mul_W
    {n : ℕ} (hn : 1 ≤ n) (u v : Fin n → ℝ) (π : Equiv.Perm (Fin n))
    (C : StrictRankCoupling u v π)
    (hu_bounds : ∀ i, u i ∈ Set.Icc (0 : ℝ) 1)
    (hv_bounds : ∀ i, v i ∈ Set.Icc (0 : ℝ) 1)
    {W : ℝ} (hW : EmpiricalProcessDominatedBy u v W)
    (a b : RankEndpoint n) :
    |cornerDiscrepancy π a b| ≤ 3 * (n : ℝ) * W := by
  have hnposNat : 0 < n := by omega
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hnposNat
  have hnne : (n : ℝ) ≠ 0 := ne_of_gt hnpos
  have hW0 : 0 ≤ W := hW.nonneg
  refine Fin.cases ?_ (fun a => ?_) a
  · have hright : 0 ≤ 3 * (n : ℝ) * W :=
      mul_nonneg (mul_nonneg (by norm_num) hnpos.le) hW0
    simpa [cornerDiscrepancy, cornerCount] using hright
  refine Fin.cases ?_ (fun b => ?_) b
  · have hright : 0 ≤ 3 * (n : ℝ) * W :=
      mul_nonneg (mul_nonneg (by norm_num) hnpos.le) hW0
    simpa [cornerDiscrepancy, cornerCount] using hright
  let x : ℝ := u (C.uOrder a)
  let y : ℝ := v (C.vOrder b)
  let A : ℝ := ((a.val + 1 : ℕ) : ℝ) / (n : ℝ)
  let B : ℝ := ((b.val + 1 : ℕ) : ℝ) / (n : ℝ)
  have hx_bounds : x ∈ Set.Icc (0 : ℝ) 1 := hu_bounds (C.uOrder a)
  have hy_bounds : y ∈ Set.Icc (0 : ℝ) 1 := hv_bounds (C.vOrder b)
  have hA_num : (((a.val + 1 : ℕ) : ℝ)) ≤ (n : ℝ) := by
    exact_mod_cast (show a.val + 1 ≤ n by omega)
  have hA0 : 0 ≤ A := div_nonneg (by positivity) hnpos.le
  have hA1 : A ≤ 1 := (div_le_one hnpos).2 hA_num
  have hx : |x - A| ≤ W := by
    have h := hW x hx_bounds 1 ⟨zero_le_one, le_rfl⟩
    rw [C.empiricalCornerCount_uOrder_one (fun i => (hv_bounds i).2) a] at h
    simpa [x, A, abs_sub_comm] using h
  have hy : |y - B| ≤ W := by
    have h := hW 1 ⟨zero_le_one, le_rfl⟩ y hy_bounds
    rw [C.empiricalCornerCount_one_vOrder (fun i => (hu_bounds i).2) b] at h
    simpa [y, B, abs_sub_comm] using h
  have hproduct : |x * y - A * B| ≤ 2 * W :=
    abs_mul_sub_mul_le_two_mul hy_bounds.1 hy_bounds.2 hA0 hA1 hW0 hx hy
  have hjoint :
      |(cornerCount π a.succ b.succ : ℝ) / (n : ℝ) - x * y| ≤ W := by
    have h := hW x hx_bounds y hy_bounds
    rw [← C.cornerCount_eq_empiricalCornerCount a b] at h
    simpa [x, y] using h
  have hscaled :
      |(cornerCount π a.succ b.succ : ℝ) / (n : ℝ) - A * B| ≤ 3 * W := by
    calc
      |(cornerCount π a.succ b.succ : ℝ) / (n : ℝ) - A * B| =
          |((cornerCount π a.succ b.succ : ℝ) / (n : ℝ) - x * y) +
            (x * y - A * B)| := by ring_nf
      _ ≤ |(cornerCount π a.succ b.succ : ℝ) / (n : ℝ) - x * y| +
          |x * y - A * B| := abs_add_le _ _
      _ ≤ W + 2 * W := add_le_add hjoint hproduct
      _ = 3 * W := by ring
  have hdiscrepancy :
      cornerDiscrepancy π a.succ b.succ =
        (n : ℝ) * ((cornerCount π a.succ b.succ : ℝ) / (n : ℝ) - A * B) := by
    rw [cornerDiscrepancy]
    simp only [Fin.val_succ]
    dsimp only [A, B]
    field_simp [hnne]
  rw [hdiscrepancy, abs_mul, abs_of_pos hnpos]
  calc
    (n : ℝ) * |(cornerCount π a.succ b.succ : ℝ) / (n : ℝ) - A * B| ≤
        (n : ℝ) * (3 * W) := mul_le_mul_of_nonneg_left hscaled hnpos.le
    _ = 3 * (n : ℝ) * W := by ring

/-- Deterministic Lemma 3.1: the star discrepancy of the induced rank
permutation is at most `3 n W`. -/
theorem cornerDiscrepancyStar_le_three_mul_n_mul_W
    {n : ℕ} (hn : 1 ≤ n) (u v : Fin n → ℝ) (π : Equiv.Perm (Fin n))
    (C : StrictRankCoupling u v π)
    (hu_bounds : ∀ i, u i ∈ Set.Icc (0 : ℝ) 1)
    (hv_bounds : ∀ i, v i ∈ Set.Icc (0 : ℝ) 1)
    {W : ℝ} (hW : EmpiricalProcessDominatedBy u v W) :
    cornerDiscrepancyStar π ≤ 3 * (n : ℝ) * W := by
  unfold cornerDiscrepancyStar
  apply Finset.max'_le
  intro z hz
  rw [cornerDiscrepancyValues] at hz
  obtain ⟨p, _, rfl⟩ := Finset.mem_image.mp hz
  exact abs_cornerDiscrepancy_le_three_mul_n_mul_W hn u v π C hu_bounds hv_bounds hW p.1 p.2

/-- The same theorem stated with the scientific note's literal one-based
definition of `D*`. -/
theorem Fidelity.DStarOne_le_three_mul_n_mul_W
    {n : ℕ} (hn : 1 ≤ n) (u v : Fin n → ℝ) (π : Equiv.Perm (Fin n))
    (C : StrictRankCoupling u v π)
    (hu_bounds : ∀ i, u i ∈ Set.Icc (0 : ℝ) 1)
    (hv_bounds : ∀ i, v i ∈ Set.Icc (0 : ℝ) 1)
    {W : ℝ} (hW : EmpiricalProcessDominatedBy u v W) :
    Fidelity.DStarOne π ≤ 3 * (n : ℝ) * W := by
  rw [Fidelity.DStarOne_eq]
  exact cornerDiscrepancyStar_le_three_mul_n_mul_W hn u v π C hu_bounds hv_bounds hW

/-- Capstone for the deterministic kernel of Lemma 3.1.  The later rank bridge
must construct `C` and `hW` from random variables; that assertion is not part
of this theorem. -/
theorem Fidelity.note_lemma_3_1_deterministic
    {n : ℕ} (hn : 1 ≤ n) (u v : Fin n → ℝ) (π : Equiv.Perm (Fin n))
    (C : StrictRankCoupling u v π)
    (hu_bounds : ∀ i, u i ∈ Set.Icc (0 : ℝ) 1)
    (hv_bounds : ∀ i, v i ∈ Set.Icc (0 : ℝ) 1)
    {W : ℝ} (hW : EmpiricalProcessDominatedBy u v W) :
    Fidelity.DStarOne π ≤ 3 * (n : ℝ) * W :=
  Fidelity.DStarOne_le_three_mul_n_mul_W hn u v π C hu_bounds hv_bounds hW

/-- Deterministic endpoint consumed by the rest of NC-2F(B): combining Lemmas
2.1 and 3.1 gives the note's literal one-based `Δₙ ≤ 12 W`.  Constructing the
rank coupling from random variables remains outside this theorem. -/
theorem Fidelity.note_deltaOne_le_twelve_mul_W
    {n : ℕ} (hn : 1 ≤ n) (u v : Fin n → ℝ) (π : Equiv.Perm (Fin n))
    (C : StrictRankCoupling u v π)
    (hu_bounds : ∀ i, u i ∈ Set.Icc (0 : ℝ) 1)
    (hv_bounds : ∀ i, v i ∈ Set.Icc (0 : ℝ) 1)
    {W : ℝ} (hW : EmpiricalProcessDominatedBy u v W) :
    Fidelity.DeltaOne π ≤ 12 * W := by
  have hnposNat : 0 < n := by omega
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hnposNat
  have hDelta := Fidelity.note_lemma_2_1 hn π
  have hStar := Fidelity.note_lemma_3_1_deterministic
    hn u v π C hu_bounds hv_bounds hW
  have hscaled :
      (n : ℝ) * Fidelity.DeltaOne π ≤ (n : ℝ) * (12 * W) := by
    calc
      (n : ℝ) * Fidelity.DeltaOne π ≤ 4 * Fidelity.DStarOne π := hDelta
      _ ≤ 4 * (3 * (n : ℝ) * W) := mul_le_mul_of_nonneg_left hStar (by norm_num)
      _ = (n : ℝ) * (12 * W) := by ring
  exact (mul_le_mul_iff_right₀ hnpos).mp hscaled

#print axioms HorizonFormal.Fidelity.note_lemma_3_1_deterministic
#print axioms HorizonFormal.Fidelity.note_deltaOne_le_twelve_mul_W

end HorizonFormal
