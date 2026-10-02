import HorizonFormal.S1Paper.DeletionKernel
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Mul

/-!
# Jet propagation through the deletion kernel (Appendix G (G.18))

The abstract logical content of the paper's jet-propagation step: if a curve
`v : ℝ → (ι → ℝ)` (playing the role of `\mu_N(\varepsilon)`, a vector on the finite
class set `\mathcal C_N`) has a derivative at `0`, then its pushforward `κ.pushforward ∘ v`
along a `DeletionKernel` also has a derivative at `0`, equal to the pushforward of the
original derivative. Iterating gives the second-derivative statement (G.18), and the
contrapositive is exactly the "non-vanishing at level 2 forces non-vanishing at level N"
implication the paper's Corollary H uses.
-/

namespace HorizonFormal.S1Paper

open scoped BigOperators

variable {ι ι' : Type*} [Fintype ι] [Fintype ι']

/-- Componentwise `HasDerivAt` for a curve into `ι → ℝ`. -/
def HasDerivAtPi (v : ℝ → ι → ℝ) (v' : ι → ℝ) (x : ℝ) : Prop :=
  ∀ i, HasDerivAt (fun ε => v ε i) (v' i) x

/-- **Derivative commutes with pushforward** (the linear-algebra content underlying
App. G (G.18)): if `v` has componentwise derivative `v'` at `x`, then the pushforward
curve `ε ↦ κ.pushforward (v ε)` has derivative `κ.pushforward v'` at `x`. -/
theorem DeletionKernel.hasDerivAtPi_pushforward (κ : DeletionKernel ι ι')
    {v : ℝ → ι → ℝ} {v' : ι → ℝ} {x : ℝ} (hv : HasDerivAtPi v v' x) :
    HasDerivAtPi (fun ε => κ.pushforward (v ε)) (κ.pushforward v') x := by
  intro i'
  simp only [DeletionKernel.pushforward_apply]
  have : ∀ i, HasDerivAt (fun ε => v ε i * κ.K i i') (v' i * κ.K i i') x :=
    fun i => (hv i).mul_const (κ.K i i')
  simpa using HasDerivAt.fun_sum (u := Finset.univ) (fun i _ => this i)

/-- **Second-derivative propagation** (App. G (G.18)): given that `v` has derivative `v₁`
everywhere near `x` with `HasDerivAtPi v₁ v₂ x` (i.e. `v₂` is the second derivative at
`x`), the pushforward curve has second derivative `κ.pushforward v₂` at `x`. -/
theorem DeletionKernel.second_deriv_pushforward (κ : DeletionKernel ι ι')
    {v v₁ : ℝ → ι → ℝ} {v₂ : ι → ℝ} {x : ℝ}
    (hv₁ : ∀ ε, HasDerivAtPi v (v₁ ε) ε) (hv₂ : HasDerivAtPi v₁ v₂ x) :
    HasDerivAtPi (fun ε => κ.pushforward (v₁ ε)) (κ.pushforward v₂) x :=
  κ.hasDerivAtPi_pushforward hv₂

/-- **Jet propagation, contrapositive form** (App. G (G.18)–(G.19), the exact logical
step the paper's Corollary H needs): if the pushforward of the second derivative at `x`
is nonzero (in some coordinate), the original second derivative was already nonzero. -/
theorem DeletionKernel.pushforward_ne_zero_of_ne_zero (κ : DeletionKernel ι ι')
    {v₂ : ι → ℝ} (h : κ.pushforward v₂ ≠ 0) : v₂ ≠ 0 := by
  intro hv₂
  apply h
  rw [hv₂, DeletionKernel.pushforward_zero]

end HorizonFormal.S1Paper
