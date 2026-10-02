import Mathlib.Analysis.Normed.Operator.Basic

/-!
# SOT convergence is not operator-norm convergence (manuscript (6.20), (6.26))

The one abstract, cheaply-formalizable piece of Theorem F's asymptotic boundary
(Phase VII): a per-index unit-vector witness on which a bounded operator has norm-1
output forces the *operator norm* to be at least 1 — this is exactly the mechanism
behind the paper's `\|\widehat F_N - \Pi_{\rm sym}\| \ge 1` (6.26), which is *not*
contradicted by, and does not contradict, strong/pointwise (SOT) convergence
`\widehat F_N \to \Pi_{\rm sym}` (6.20). The S1-specific witness
`h_N = p_N \otimes p_N / \|p_N\|_{L^2}^2` and the operator `\widehat F_N - \Pi_{\rm sym}`
themselves are not constructed here (they need the polynomial Hilbert space, out of
scope; see `ClaimMap.md`) — only the abstract inequality mechanism is certified.
-/

namespace HorizonFormal.S1Paper

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- **A unit-norm witness forces operator norm `≥ 1`** (manuscript (6.26)): if `T` is a
bounded linear operator and some unit vector `h` has `‖T h‖ = 1`, then `‖T‖ ≥ 1`. In the
paper's use, `T = \widehat F_N - \Pi_{\rm sym}` and `h = h_N`, with
`\widehat F_N h_N = 0` and `\Pi_{\rm sym} h_N = h_N`, so `T h_N = -h_N` and
`\|T h_N\| = \|h_N\| = 1`. -/
theorem one_le_opNorm_of_witness (T : E →L[ℝ] E) {h : E} (hh : ‖h‖ = 1) (hTh : ‖T h‖ = 1) :
    1 ≤ ‖T‖ :=
  calc (1:ℝ) = ‖T h‖ := hTh.symm
    _ ≤ ‖T‖ * ‖h‖ := T.le_opNorm h
    _ = ‖T‖ := by rw [hh, mul_one]

end HorizonFormal.S1Paper
