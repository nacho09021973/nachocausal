import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Tactic.Linarith

/-!
# Parity ⟹ vanishing first derivative (Theorem G / manuscript (7.4)–(7.6))

The abstract calculus lemma behind the paper's parity mechanism: an *even* curve into a
finite-dimensional vector space has vanishing derivative at `0`. This isolates exactly
the mechanism the paper attributes to the coordinate-swap isometry `\iota`
(`\mu_{N,\varepsilon}^{[P]} = \mu_{N,-\varepsilon}^{[P]}` ⟹ the first derivative vanishes).
-/

namespace HorizonFormal.S1Paper

variable {ι : Type*} [Fintype ι]

/-- **Evenness kills the first derivative.** If `v : ℝ → (ι → ℝ)` satisfies
`v ε = v (-ε)` for every `ε` and has derivative `v'` at `0`, then `v' = 0`. This is the
content of manuscript (7.4)–(7.6): a law folded onto itself by an isometric involution
has zero first-order tangent at the fixed point. -/
theorem even_hasDerivAt_zero {v : ℝ → ι → ℝ} {v' : ι → ℝ}
    (heven : ∀ ε, v ε = v (-ε)) (hv : ∀ i, HasDerivAt (fun ε => v ε i) (v' i) 0) :
    v' = 0 := by
  funext i
  simp only [Pi.zero_apply]
  have hv0 : HasDerivAt (fun ε => v ε i) (v' i) (-(0:ℝ)) := by rw [neg_zero]; exact hv i
  have hneg : HasDerivAt (fun ε : ℝ => -ε) (-1 : ℝ) 0 := (hasDerivAt_id (0:ℝ)).neg
  have hcomp := hv0.comp 0 hneg
  have hcomp' : HasDerivAt (fun ε => v (-ε) i) (v' i * (-1)) 0 := hcomp
  have heq : (fun ε => v (-ε) i) = (fun ε => v ε i) := by
    funext ε; rw [← heven ε]
  rw [heq] at hcomp'
  have hun := (hv i).unique hcomp'
  linarith [hun]

end HorizonFormal.S1Paper
