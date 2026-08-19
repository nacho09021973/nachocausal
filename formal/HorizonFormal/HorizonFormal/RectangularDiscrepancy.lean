import Mathlib.Data.Finset.Max
import Mathlib.Data.Fintype.Perm
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# Deterministic rectangular discrepancy

The ranks in the scientific note are one-based.  Here a rank `r + 1` is represented
by `r : Fin n`.  Thus the note's interval `{a₁ + 1, ..., a₂}` is exactly the
half-open zero-based interval `[a₁, a₂)` used below.
-/

namespace HorizonFormal

/-- A rank endpoint is a natural number between `0` and `n`, inclusive. -/
abbrev RankEndpoint (n : ℕ) := Fin (n + 1)

/-- A rank interval is an ordered pair of endpoints, representing `[lower, upper)`. -/
abbrev RankInterval (n : ℕ) :=
  {p : RankEndpoint n × RankEndpoint n // p.1 ≤ p.2}

namespace RankInterval

/-- The inclusive lower endpoint of a rank interval. -/
def lower {n : ℕ} (I : RankInterval n) : RankEndpoint n := I.1.1

/-- The exclusive upper endpoint of a rank interval. -/
def upper {n : ℕ} (I : RankInterval n) : RankEndpoint n := I.1.2

/-- The number of ranks in `[lower, upper)`. -/
def length {n : ℕ} (I : RankInterval n) : ℕ := I.upper.val - I.lower.val

theorem lower_le_upper {n : ℕ} (I : RankInterval n) : I.lower ≤ I.upper := I.2

end RankInterval

/-- Number of permutation points in the lower-left corner `[0,a) × [0,b)`. -/
def cornerCount {n : ℕ} (π : Equiv.Perm (Fin n)) (a b : RankEndpoint n) : ℕ :=
  ((Finset.univ : Finset (Fin n)).filter fun i =>
    i.val < a.val ∧ (π i).val < b.val).card

/-- The corner discrepancy `F(a,b) - ab/n`, valued in `ℝ`. -/
noncomputable def cornerDiscrepancy {n : ℕ} (π : Equiv.Perm (Fin n))
    (a b : RankEndpoint n) : ℝ :=
  cornerCount π a b - (a.val : ℝ) * (b.val : ℝ) / (n : ℝ)

/-- Number of permutation points in the rectangle `I × J`. -/
def rectangleCount {n : ℕ} (π : Equiv.Perm (Fin n))
    (I J : RankInterval n) : ℕ :=
  ((Finset.univ : Finset (Fin n)).filter fun i =>
    I.lower.val ≤ i.val ∧ i.val < I.upper.val ∧
      J.lower.val ≤ (π i).val ∧ (π i).val < J.upper.val).card

/-- The scaled rectangular error `N(I,J) - |I||J|/n`. -/
noncomputable def rectangleError {n : ℕ} (π : Equiv.Perm (Fin n))
    (I J : RankInterval n) : ℝ :=
  rectangleCount π I J - (I.length : ℝ) * (J.length : ℝ) / (n : ℝ)

private theorem cast_cornerCount_eq_sum {n : ℕ} (π : Equiv.Perm (Fin n))
    (a b : RankEndpoint n) :
    (cornerCount π a b : ℝ) =
      ∑ i : Fin n, if i.val < a.val ∧ (π i).val < b.val then 1 else 0 := by
  classical
  simp [cornerCount]

private theorem cast_rectangleCount_eq_sum {n : ℕ} (π : Equiv.Perm (Fin n))
    (I J : RankInterval n) :
    (rectangleCount π I J : ℝ) =
      ∑ i : Fin n, if I.lower.val ≤ i.val ∧ i.val < I.upper.val ∧
        J.lower.val ≤ (π i).val ∧ (π i).val < J.upper.val then 1 else 0 := by
  classical
  simp [rectangleCount]

/-- Inclusion-exclusion for the count in a half-open rank rectangle. -/
theorem rectangleCount_eq_four_corners {n : ℕ} (π : Equiv.Perm (Fin n))
    (I J : RankInterval n) :
    (rectangleCount π I J : ℝ) =
      cornerCount π I.upper J.upper - cornerCount π I.lower J.upper -
        cornerCount π I.upper J.lower + cornerCount π I.lower J.lower := by
  classical
  rw [cast_rectangleCount_eq_sum, cast_cornerCount_eq_sum, cast_cornerCount_eq_sum,
    cast_cornerCount_eq_sum, cast_cornerCount_eq_sum]
  calc
    (∑ i : Fin n, if I.lower.val ≤ i.val ∧ i.val < I.upper.val ∧
        J.lower.val ≤ (π i).val ∧ (π i).val < J.upper.val then 1 else 0) =
        ∑ i : Fin n, (
          (if i.val < I.upper.val ∧ (π i).val < J.upper.val then (1 : ℝ) else 0) -
          (if i.val < I.lower.val ∧ (π i).val < J.upper.val then 1 else 0) -
          (if i.val < I.upper.val ∧ (π i).val < J.lower.val then 1 else 0) +
          (if i.val < I.lower.val ∧ (π i).val < J.lower.val then 1 else 0)) := by
      apply Finset.sum_congr rfl
      intro i _
      have hI := I.lower_le_upper
      have hJ := J.lower_le_upper
      change I.lower.val ≤ I.upper.val at hI
      change J.lower.val ≤ J.upper.val at hJ
      split_ifs <;> norm_num <;> omega
    _ = _ := by
      rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.sum_sub_distrib]

/--
The local four-corner identity from Lemma 2.1.  Its left side is
`N(I,J) - |I||J|/n`, with no extra normalization.
-/
theorem rectangleError_eq_four_corner_discrepancies {n : ℕ}
    (_hn : 1 ≤ n) (π : Equiv.Perm (Fin n)) (I J : RankInterval n) :
    rectangleError π I J =
      cornerDiscrepancy π I.upper J.upper - cornerDiscrepancy π I.lower J.upper -
        cornerDiscrepancy π I.upper J.lower + cornerDiscrepancy π I.lower J.lower := by
  have hI : (I.length : ℝ) = (I.upper.val : ℝ) - I.lower.val := by
    rw [RankInterval.length, Nat.cast_sub I.lower_le_upper]
  have hJ : (J.length : ℝ) = (J.upper.val : ℝ) - J.lower.val := by
    rw [RankInterval.length, Nat.cast_sub J.lower_le_upper]
  rw [rectangleError, rectangleCount_eq_four_corners, hI, hJ]
  simp only [cornerDiscrepancy]
  ring

/-- The finite set of absolute corner discrepancies. -/
noncomputable def cornerDiscrepancyValues {n : ℕ} (π : Equiv.Perm (Fin n)) : Finset ℝ :=
  (Finset.univ : Finset (RankEndpoint n × RankEndpoint n)).image fun p =>
    |cornerDiscrepancy π p.1 p.2|

private theorem cornerDiscrepancyValues_nonempty {n : ℕ} (π : Equiv.Perm (Fin n)) :
    (cornerDiscrepancyValues π).Nonempty := by
  classical
  refine ⟨|cornerDiscrepancy π 0 0|, ?_⟩
  simp [cornerDiscrepancyValues]

/-- The star discrepancy `D*`, the maximum absolute discrepancy over all corners. -/
noncomputable def cornerDiscrepancyStar {n : ℕ} (π : Equiv.Perm (Fin n)) : ℝ :=
  (cornerDiscrepancyValues π).max' (cornerDiscrepancyValues_nonempty π)

/-- Every absolute corner discrepancy is bounded by `D*`. -/
theorem abs_cornerDiscrepancy_le_star {n : ℕ} (π : Equiv.Perm (Fin n))
    (a b : RankEndpoint n) :
    |cornerDiscrepancy π a b| ≤ cornerDiscrepancyStar π := by
  classical
  unfold cornerDiscrepancyStar
  apply Finset.le_max'
  simp [cornerDiscrepancyValues]

/-- The normalized discrepancy of one rectangle, as in the definition of `Δₙ`. -/
noncomputable def normalizedRectangleDiscrepancy {n : ℕ} (π : Equiv.Perm (Fin n))
    (I J : RankInterval n) : ℝ :=
  |(rectangleCount π I J : ℝ) / (n : ℝ) -
    (I.length : ℝ) * (J.length : ℝ) / (n : ℝ) ^ 2|

/-- The empty half-open interval `[0,0)`. -/
def RankInterval.empty (n : ℕ) : RankInterval n := ⟨(0, 0), le_rfl⟩

/-- The finite set of normalized absolute discrepancies over all rank rectangles. -/
noncomputable def rectangularDiscrepancyValues {n : ℕ} (π : Equiv.Perm (Fin n)) :
    Finset ℝ :=
  (Finset.univ : Finset (RankInterval n × RankInterval n)).image fun p =>
    normalizedRectangleDiscrepancy π p.1 p.2

private theorem rectangularDiscrepancyValues_nonempty {n : ℕ}
    (π : Equiv.Perm (Fin n)) : (rectangularDiscrepancyValues π).Nonempty := by
  classical
  refine ⟨normalizedRectangleDiscrepancy π (RankInterval.empty n) (RankInterval.empty n), ?_⟩
  apply Finset.mem_image.mpr
  exact ⟨(RankInterval.empty n, RankInterval.empty n), Finset.mem_univ _, rfl⟩

/-- `Δₙ(π)`, the maximum normalized discrepancy over all pairs of rank intervals. -/
noncomputable def rectangularDiscrepancy {n : ℕ} (π : Equiv.Perm (Fin n)) : ℝ :=
  (rectangularDiscrepancyValues π).max' (rectangularDiscrepancyValues_nonempty π)

/-- The finite maximum defining `Δₙ(π)` is attained by a pair of intervals. -/
theorem rectangularDiscrepancy_eq_normalized_of_some_intervals {n : ℕ}
    (π : Equiv.Perm (Fin n)) :
    ∃ I J : RankInterval n,
      rectangularDiscrepancy π = normalizedRectangleDiscrepancy π I J := by
  classical
  have hm : rectangularDiscrepancy π ∈ rectangularDiscrepancyValues π := by
    unfold rectangularDiscrepancy
    exact Finset.max'_mem _ _
  obtain ⟨p, _, hp⟩ := Finset.mem_image.mp hm
  exact ⟨p.1, p.2, hp.symm⟩

/-- Multiplication by positive `n` removes exactly the outer normalization. -/
theorem n_mul_normalizedRectangleDiscrepancy {n : ℕ} (hn : 1 ≤ n)
    (π : Equiv.Perm (Fin n)) (I J : RankInterval n) :
    (n : ℝ) * normalizedRectangleDiscrepancy π I J = |rectangleError π I J| := by
  have hnposNat : 0 < n := by omega
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hnposNat
  have hnne : (n : ℝ) ≠ 0 := ne_of_gt hnpos
  have hinside :
      (rectangleCount π I J : ℝ) / (n : ℝ) -
          (I.length : ℝ) * (J.length : ℝ) / (n : ℝ) ^ 2 =
        rectangleError π I J / (n : ℝ) := by
    unfold rectangleError
    field_simp [hnne]
  rw [normalizedRectangleDiscrepancy, hinside, abs_div, abs_of_pos hnpos]
  field_simp [hnne]

/-- The scaled error of every rectangle is bounded by four corner discrepancies. -/
theorem abs_rectangleError_le_four_mul_cornerDiscrepancyStar {n : ℕ}
    (hn : 1 ≤ n) (π : Equiv.Perm (Fin n)) (I J : RankInterval n) :
    |rectangleError π I J| ≤ 4 * cornerDiscrepancyStar π := by
  let A := cornerDiscrepancy π I.upper J.upper
  let B := cornerDiscrepancy π I.lower J.upper
  let C := cornerDiscrepancy π I.upper J.lower
  let D := cornerDiscrepancy π I.lower J.lower
  have hA : |A| ≤ cornerDiscrepancyStar π := abs_cornerDiscrepancy_le_star π _ _
  have hB : |B| ≤ cornerDiscrepancyStar π := abs_cornerDiscrepancy_le_star π _ _
  have hC : |C| ≤ cornerDiscrepancyStar π := abs_cornerDiscrepancy_le_star π _ _
  have hD : |D| ≤ cornerDiscrepancyStar π := abs_cornerDiscrepancy_le_star π _ _
  have hAB : |A - B| ≤ |A| + |B| := by
    simpa [sub_eq_add_neg] using abs_add_le A (-B)
  have hABC : |A - B - C| ≤ |A| + |B| + |C| := by
    calc
      |A - B - C| ≤ |A - B| + |C| := by
        simpa [sub_eq_add_neg] using abs_add_le (A - B) (-C)
      _ ≤ |A| + |B| + |C| := add_le_add hAB le_rfl
  rw [rectangleError_eq_four_corner_discrepancies hn]
  change |A - B - C + D| ≤ 4 * cornerDiscrepancyStar π
  calc
    |A - B - C + D| ≤ |A - B - C| + |D| := abs_add_le _ _
    _ ≤ |A| + |B| + |C| + |D| := add_le_add hABC le_rfl
    _ ≤ cornerDiscrepancyStar π + cornerDiscrepancyStar π +
        cornerDiscrepancyStar π + cornerDiscrepancyStar π :=
      add_le_add (add_le_add (add_le_add hA hB) hC) hD
    _ = 4 * cornerDiscrepancyStar π := by ring

/--
Lemma 2.1: for every nonempty finite permutation, `n Δₙ(π) ≤ 4 D*`.
-/
theorem n_mul_rectangularDiscrepancy_le_four_mul_cornerDiscrepancyStar
    {n : ℕ} (hn : 1 ≤ n) (π : Equiv.Perm (Fin n)) :
    (n : ℝ) * rectangularDiscrepancy π ≤ 4 * cornerDiscrepancyStar π := by
  obtain ⟨I, J, hmax⟩ := rectangularDiscrepancy_eq_normalized_of_some_intervals π
  rw [hmax, n_mul_normalizedRectangleDiscrepancy hn]
  exact abs_rectangleError_le_four_mul_cornerDiscrepancyStar hn π I J

end HorizonFormal
