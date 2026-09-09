import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith

/-!
# Horizon threshold: algebraic gluing and deterministic mesh control

These lemmas formalise only the stated algebraic implications. They do not
formalise the generator, a Poisson limit, the Jacobian, or horizon detection.
The two old outgoing coordinates are oriented towards the future separately.
-/

namespace HorizonFormal.HorizonThreshold

noncomputable def exteriorCoordinate (scale u : ℝ) : ℝ :=
  -Real.exp (-u / scale)

noncomputable def interiorCoordinate (scale w : ℝ) : ℝ :=
  Real.exp (w / scale)

theorem exteriorCoordinate_le_iff {scale u u' : ℝ} (hs : 0 < scale) :
    exteriorCoordinate scale u ≤ exteriorCoordinate scale u' ↔ u ≤ u' := by
  simp only [exteriorCoordinate, neg_le_neg_iff, Real.exp_le_exp]
  rw [div_le_div_iff_of_pos_right hs]
  exact neg_le_neg_iff

theorem interiorCoordinate_le_iff {scale w w' : ℝ} (hs : 0 < scale) :
    interiorCoordinate scale w ≤ interiorCoordinate scale w' ↔ w ≤ w' := by
  simp only [interiorCoordinate, Real.exp_le_exp]
  exact div_le_div_iff_of_pos_right hs

theorem exteriorCoordinate_lt_interiorCoordinate (scale u w : ℝ) :
    exteriorCoordinate scale u < interiorCoordinate scale w := by
  have hu := Real.exp_pos (-u / scale)
  have hw := Real.exp_pos (w / scale)
  dsimp [exteriorCoordinate, interiorCoordinate]
  linarith

theorem inward_product_order_iff (scale ve vi u w : ℝ) :
    (ve ≤ vi ∧ exteriorCoordinate scale u ≤ interiorCoordinate scale w) ↔
      ve ≤ vi := by
  exact and_iff_left (le_of_lt (exteriorCoordinate_lt_interiorCoordinate scale u w))

theorem no_outward_product_order (scale ve vi u w : ℝ) :
    ¬ (vi ≤ ve ∧ interiorCoordinate scale w ≤ exteriorCoordinate scale u) := by
  intro h
  exact (not_le_of_gt (exteriorCoordinate_lt_interiorCoordinate scale u w)) h.2

/-- A crossing pair and an admissible threshold carry exactly the same score
    witnesses. The nonempty witnesses are retained on both sides. -/
theorem crossing_score_iff_threshold
    {E I : Type*} (ve : E → ℝ) (vi : I → ℝ)
    (he : E → ℕ) (hi : I → ℕ) (k : ℕ) :
    (∃ e i, ve e ≤ vi i ∧ k ≤ he e + hi i) ↔
      ∃ s : ℝ, ∃ e i, ve e ≤ s ∧ s ≤ vi i ∧ k ≤ he e + hi i := by
  constructor
  · rintro ⟨e, i, hvi, hk⟩
    exact ⟨ve e, e, i, le_rfl, hvi, hk⟩
  · rintro ⟨s, e, i, he', hi', hk⟩
    exact ⟨e, i, le_trans he' hi', hk⟩

/-- Local mesh bound. A finite mesh and a union bound yield the probabilistic
    upgrade in the accompanying note; neither is asserted by this lemma. -/
theorem monotone_mesh_error
    {f g : ℝ → ℝ} (hf : Monotone f) (hg : Monotone g)
    {a s b eta omega : ℝ} (has : a ≤ s) (hsb : s ≤ b)
    (ha : |f a - g a| ≤ eta) (hb : |f b - g b| ≤ eta)
    (hgap : g b - g a ≤ omega) :
    |f s - g s| ≤ eta + omega := by
  rcases abs_le.mp ha with ⟨ha₁, ha₂⟩
  rcases abs_le.mp hb with ⟨hb₁, hb₂⟩
  have hfa := hf has
  have hfb := hf hsb
  have hga := hg has
  have hgb := hg hsb
  apply abs_le.mpr
  constructor <;> linarith

#print axioms exteriorCoordinate_le_iff
#print axioms interiorCoordinate_le_iff
#print axioms exteriorCoordinate_lt_interiorCoordinate
#print axioms inward_product_order_iff
#print axioms no_outward_product_order
#print axioms crossing_score_iff_threshold
#print axioms monotone_mesh_error

end HorizonFormal.HorizonThreshold
