import HorizonFormal.S1Paper.Parity
import HorizonFormal.S1Paper.JetPropagation

/-!
# Corollary H, packaged (manuscript (7.16), Appendix G (G.19))

This module states exactly the hypotheses needed to conclude the paper's
`r_N(\gamma_\psi) = 2` statement (first jet vanishes, second jet does not), making
transparent what the argument actually consumes: parity of the curve, differentiability
enough to speak of a second derivative at `0`, a deletion kernel propagating that second
derivative, and non-vanishing of the pushed-forward value. Nothing about "`r_N = 2`" is
assumed directly.
-/

namespace HorizonFormal.S1Paper

variable {ι ι' : Type*} [Fintype ι] [Fintype ι']

/-- The paper's `r_N(\gamma_\psi) = 2` statement, made abstract: the first derivative at
`0` vanishes and the second does not. -/
def FirstZeroSecondNonzero (v' v₂ : ι → ℝ) : Prop := v' = 0 ∧ v₂ ≠ 0

/-- **Corollary H, packaged.** Given
* `v` even (so `even_hasDerivAt_zero` forces the first derivative `v'` at `0` to vanish);
* `v` differentiable at every `ε` with derivative curve `v₁`, and `v₁` itself
  differentiable at `0` with derivative `v₂` (i.e. `v₂` is the second derivative of `v`
  at `0` — exactly the real-analyticity the paper invokes in Appendix G (G.3));
* a deletion kernel `κ` whose pushforward carries `v₂` to some `w₂`;
* `w₂ ≠ 0` (the paper's explicit `N=2` computation, (7.10)/(G.12), transported through
  `κ` in place of the specific `K_{N\to2}`);

this concludes `FirstZeroSecondNonzero v' v₂`: the first jet of `v` vanishes and its
second jet does not — the paper's `r_N(\gamma_\psi) = 2`. -/
theorem corollaryH
    {v v₁ : ℝ → ι → ℝ} {v' v₂ : ι → ℝ}
    (heven : ∀ ε, v ε = v (-ε))
    (hv' : ∀ i, HasDerivAt (fun ε => v ε i) (v' i) 0)
    (hv₁ : ∀ ε, HasDerivAtPi v (v₁ ε) ε)
    (hv₂ : HasDerivAtPi v₁ v₂ 0)
    (κ : DeletionKernel ι ι') {w₂ : ι' → ℝ}
    (hpush : κ.pushforward v₂ = w₂)
    (hw₂ : w₂ ≠ 0) :
    FirstZeroSecondNonzero v' v₂ := by
  refine ⟨even_hasDerivAt_zero heven hv', ?_⟩
  apply κ.pushforward_ne_zero_of_ne_zero
  rw [hpush]; exact hw₂

end HorizonFormal.S1Paper
