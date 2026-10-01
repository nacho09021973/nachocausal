import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Ring

/-!
# Abstract uniform-deletion kernel (Appendix G (G.13)–(G.18))

This module formalizes the *combinatorial shape* of the paper's uniform-deletion kernel
`K_{m,m-1}(C,D) = (1/m) #{v ∈ C : [C∖{v}] = D}` as an abstract finite Markov-type kernel:
nonnegative, rows summing to 1, and (structurally, by construction) independent of any
parameter `ε`.

This does **not** construct the kernel from actual poset deletion counts — that
construction (which needs the poset class types `𝒞_m` and the deletion map
`C ↦ [C ∖ {v}]`) is out of scope here; see `ClaimMap.md`. What *is* proved is the
composition/propagation logic (G.16)–(G.18) that the paper's Corollary H argument
actually consumes, as an interface any concrete realization of the kernel (poset-based
or otherwise) must satisfy.
-/

namespace HorizonFormal.S1Paper

open scoped BigOperators

/-- An abstract finite deletion-type kernel: nonnegative weights whose rows sum to 1
(Appendix G (G.13)–(G.14): non-negativity and "every element deletes to exactly one
class"). The structure carries no `ε`; that a composed kernel does not depend on any
perturbation parameter is therefore true by construction, not by a separate proof. -/
structure DeletionKernel (ι ι' : Type*) [Fintype ι] [Fintype ι'] where
  /-- The kernel weights `K i i'`. -/
  K : ι → ι' → ℝ
  nonneg : ∀ i i', 0 ≤ K i i'
  rowSum_eq_one : ∀ i, ∑ i', K i i' = 1

namespace DeletionKernel

variable {ι ι' ι'' : Type*} [Fintype ι] [Fintype ι'] [Fintype ι'']

/-- The pushforward of a vector `μ : ι → ℝ` (a finite unlabeled-poset law at some fixed
`ε`, or one of its derivatives) along a deletion kernel: `(m-1)`-level analogue of
`μ_{m-1,\varepsilon}^{[P]} = K_{m,m-1}\mu_{m,\varepsilon}^{[P]}` (App. G (G.15)). -/
def pushforward (κ : DeletionKernel ι ι') (μ : ι → ℝ) : ι' → ℝ :=
  fun i' => ∑ i, μ i * κ.K i i'

@[simp] lemma pushforward_apply (κ : DeletionKernel ι ι') (μ : ι → ℝ) (i' : ι') :
    κ.pushforward μ i' = ∑ i, μ i * κ.K i i' := rfl

lemma pushforward_linear (κ : DeletionKernel ι ι') (μ ν : ι → ℝ) (c d : ℝ) :
    κ.pushforward (fun i => c * μ i + d * ν i) = fun i' => c * κ.pushforward μ i' + d * κ.pushforward ν i' := by
  funext i'
  simp only [pushforward_apply]
  rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i _
  ring

@[simp] lemma pushforward_zero (κ : DeletionKernel ι ι') : κ.pushforward 0 = 0 := by
  funext i'; simp

/-- Composing two deletion kernels (App. G (G.16): `K_{N\to2}:=K_{3,2}\circ\cdots\circ K_{N,N-1}`
is exactly an iterate of this operation). -/
def comp (κ1 : DeletionKernel ι ι') (κ2 : DeletionKernel ι' ι'') : DeletionKernel ι ι'' where
  K i i'' := ∑ i', κ1.K i i' * κ2.K i' i''
  nonneg i i'' := Finset.sum_nonneg fun i' _ => mul_nonneg (κ1.nonneg i i') (κ2.nonneg i' i'')
  rowSum_eq_one i := by
    have : ∀ i', ∑ i'', κ1.K i i' * κ2.K i' i'' = κ1.K i i' := by
      intro i'
      rw [← Finset.mul_sum, κ2.rowSum_eq_one, mul_one]
    calc ∑ i'', ∑ i', κ1.K i i' * κ2.K i' i''
        = ∑ i', ∑ i'', κ1.K i i' * κ2.K i' i'' := Finset.sum_comm
      _ = ∑ i', κ1.K i i' := by simp [this]
      _ = 1 := κ1.rowSum_eq_one i

/-- **Projective consistency** (App. G (G.16)–(G.17)): pushing forward along the
composition is the same as pushing forward twice in sequence. This is the abstract
principle behind `\mu_2(\varepsilon) = K_{N\to2}\mu_N(\varepsilon)`. -/
theorem pushforward_comp (κ1 : DeletionKernel ι ι') (κ2 : DeletionKernel ι' ι'') (μ : ι → ℝ) :
    (κ1.comp κ2).pushforward μ = κ2.pushforward (κ1.pushforward μ) := by
  funext i''
  simp only [pushforward_apply, comp]
  calc ∑ i, μ i * ∑ i', κ1.K i i' * κ2.K i' i''
      = ∑ i, ∑ i', μ i * (κ1.K i i' * κ2.K i' i'') := by
        congr 1; funext i; rw [Finset.mul_sum]
    _ = ∑ i', ∑ i, μ i * (κ1.K i i' * κ2.K i' i'') := Finset.sum_comm
    _ = ∑ i', (∑ i, μ i * κ1.K i i') * κ2.K i' i'' := by
        congr 1; funext i'; rw [Finset.sum_mul]; congr 1; funext i; ring

end DeletionKernel

end HorizonFormal.S1Paper
