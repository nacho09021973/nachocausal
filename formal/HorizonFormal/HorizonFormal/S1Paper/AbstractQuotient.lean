import Mathlib.Analysis.InnerProductSpace.Projection.Basic
import Mathlib.Analysis.InnerProductSpace.Orthogonal

/-!
# Corollary D, abstract interface (manuscript §5, Appendix D)

This module formalizes the *abstract* content of Corollary D: given a finite-dimensional
real inner product space `𝒳` and a finite family of "representatives" `R : 𝒞 → 𝒳` with
positive weights `w : 𝒞 → ℝ`, the induced "score" map
`D f C := ⟪f, R C⟫ / w C` has kernel exactly `(span (range R))ᗮ`, factors through the
orthogonal projection onto `V := span (range R)`, and is injective on `V`.

This is the paper's `D\mathscr S_N = B_N P_N^{\rm vis}` and
`\ker D\mathscr S_N = V_N^{\perp_{\rm sym}} \oplus \bigwedge^2 H` (§5 (5.5)–(5.6),
Appendix D (D.4)–(D.9)) with the S1-specific `\mathcal X = H\widehat\otimes H`,
`\mathcal C_N`, `R_C^{(N)}`, `\mu_{N,0}(C)` left as an uninstantiated interface: this
module proves the *general* Hilbert-space fact, not the S1 instance. Instantiating it
against the real `H\widehat\otimes H` (infinite-dimensional) is out of scope; see
`ClaimMap.md`.
-/

namespace HorizonFormal.S1Paper

variable {𝒳 : Type*} [NormedAddCommGroup 𝒳] [InnerProductSpace ℝ 𝒳] [FiniteDimensional ℝ 𝒳]
variable {𝒞 : Type*} [Fintype 𝒞]

/-- The abstract data behind the paper's score differential: a finite family of
representatives `R : 𝒞 → 𝒳` with positive reference weights `w` (the manuscript's
`\mu_{N,0}(C) > 0`, §3 (3.7)). -/
structure ScoreData (𝒳 : Type*) [NormedAddCommGroup 𝒳] [InnerProductSpace ℝ 𝒳]
    (𝒞 : Type*) [Fintype 𝒞] where
  R : 𝒞 → 𝒳
  w : 𝒞 → ℝ
  w_pos : ∀ C, 0 < w C

namespace ScoreData

variable (s : ScoreData 𝒳 𝒞)

/-- The score differential `(D\mathscr S_N f)(C) = \langle f, R_C\rangle / w(C)`
(manuscript (3.7)). -/
noncomputable def D : 𝒳 →ₗ[ℝ] (𝒞 → ℝ) where
  toFun f C := (inner ℝ f (s.R C)) / s.w C
  map_add' f g := by
    funext C
    simp only [Pi.add_apply, inner_add_left, add_div]
  map_smul' c f := by
    funext C
    simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply, inner_smul_left,
      RCLike.conj_to_real, mul_div_assoc]

@[simp] lemma D_apply (f : 𝒳) (C : 𝒞) : s.D f C = (inner ℝ f (s.R C)) / s.w C := rfl

/-- The visible subspace `V_N := \operatorname{span}\{R_C\}` (manuscript (3.10)). -/
def V : Submodule ℝ 𝒳 := Submodule.span ℝ (Set.range s.R)

/-- **Kernel of the score differential is the orthogonal complement of `V`**
(manuscript (3.10), Appendix D (D.4)). -/
theorem ker_D_eq_orthogonal : LinearMap.ker s.D = (s.V)ᗮ := by
  ext f
  simp only [LinearMap.mem_ker, Submodule.mem_orthogonal]
  constructor
  · intro hf u hu
    have hfC : ∀ C, (inner ℝ f (s.R C) : ℝ) = 0 := by
      intro C
      have := congrFun hf C
      simp only [D_apply, Pi.zero_apply, div_eq_zero_iff] at this
      rcases this with h | h
      · exact h
      · exact absurd h (ne_of_gt (s.w_pos C))
    have hu' : u ∈ s.V := hu
    unfold V at hu'
    refine Submodule.span_induction
      (p := fun x (_ : x ∈ Submodule.span ℝ (Set.range s.R)) => (inner ℝ x f : ℝ) = 0)
      (fun x hx => ?_) (by simp) (fun x y _ _ hx hy => ?_) (fun a x _ hx => ?_) hu'
    · obtain ⟨C, rfl⟩ := hx
      rw [real_inner_comm]; exact hfC C
    · simp [inner_add_left, hx, hy]
    · simp [inner_smul_left, hx]
  · intro hf
    funext C
    have hRC : s.R C ∈ s.V := Submodule.subset_span ⟨C, rfl⟩
    have := hf (s.R C) hRC
    simp only [D_apply, Pi.zero_apply]
    rw [real_inner_comm] at this
    simp [this]

/-- **Factorization through the orthogonal projection onto `V`**
(manuscript (5.5), Appendix D (D.7)): `D f` only depends on the component of `f` in
`V`. -/
theorem D_eq_D_starProjection (f : 𝒳) : s.D f = s.D (s.V.starProjection f) := by
  have hmem : f - s.V.starProjection f ∈ (s.V)ᗮ := by
    have hval : (s.V)ᗮ.starProjection f = f - s.V.starProjection f := by
      simp [Submodule.starProjection_orthogonal' s.V]
    rw [← hval]
    exact (s.V)ᗮ.starProjection_apply_mem f
  have hker : f - s.V.starProjection f ∈ LinearMap.ker s.D := by
    rw [ker_D_eq_orthogonal]; exact hmem
  have heq : s.D (f - s.V.starProjection f) = 0 := hker
  rw [map_sub] at heq
  exact sub_eq_zero.mp heq

/-- **Injectivity on `V`** (manuscript's `B_N` injective, Appendix D §5): if `f, g ∈ V`
have the same score, they are equal. -/
theorem injOn_D_V : Set.InjOn s.D (s.V : Set 𝒳) := by
  intro f hf g hg hfg
  have : f - g ∈ LinearMap.ker s.D := by
    show s.D (f - g) = 0
    rw [map_sub, hfg, sub_self]
  rw [ker_D_eq_orthogonal] at this
  have hfgV : f - g ∈ s.V := Submodule.sub_mem s.V hf hg
  have hboth : f - g ∈ s.V ⊓ (s.V)ᗮ := ⟨hfgV, this⟩
  rw [s.V.inf_orthogonal_eq_bot] at hboth
  exact sub_eq_zero.mp hboth

end ScoreData

end HorizonFormal.S1Paper
