import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-!
# Exact finite arithmetic checks (manuscript §6, §7, Appendices F, G)

Finite, exact rational identities used in the paper. Each is proved as a genuine
`N=2,3,4`-only fact, never presented as an all-`N` statement (per `ClaimMap.md`, these
are `TARGET_EXACT_CHECK` items).
-/

namespace HorizonFormal.S1Paper

/-! ## §7 / Appendix G: the exact `N=2` second derivatives, from moments -/

/-- **(a)** The second-moment values `⟨T_chain²⟩₀ = 16/5`, `⟨T_antichain²⟩₀ = 24/5`
(Appendix G (G.9)–(G.11)), derived algebraically from the stated moment identities
(taken here as hypotheses — this is `N2_ALGEBRA_FROM_MOMENTS_FORMALIZED`; the
polynomial-integral derivation of the moments themselves, `N2_INTEGRAL_FORMALIZED`, is
not attempted here). -/
theorem N2_moment_squares
    (A12 A21 M1_12 M2_12 : ℝ)
    (hA_prod : A12 * A21 = -1 / 15) (hA12_sq : A12 ^ 2 = 1 / 15) (hA21_sq : A21 ^ 2 = 1 / 15)
    (hM_prod : M1_12 * M2_12 = -4 / 15) (hM1_sq : M1_12 ^ 2 = 4 / 15) (hM2_sq : M2_12 ^ 2 = 4 / 15) :
    (2 * (2 * 1 * 1 - 2 * M1_12 ^ 2) + 2 * (2 * (0:ℝ) * 0 - 2 * A12 * A21)) = 16 / 5 ∧
    (2 * (1 * 1 - 2 * M1_12 * M2_12 + 1 * 1) + 2 * (-(A12 ^ 2 + A21 ^ 2))) = 24 / 5 := by
  constructor <;> nlinarith [hA_prod, hA12_sq, hA21_sq, hM_prod, hM1_sq, hM2_sq]

/-- **(b)** The exact `N=2` second derivatives `\mu_2''(\mathrm{antichain}) = 8/5`,
`\mu_2''(\mathrm{chain}) = -8/5` (Appendix G (G.12)), from the second moments (a) via
the finite-likelihood formula `p_\pi''(0) = (4/N!)(\langle T_\pi^2\rangle_0 -
N\|\psi\|^2)` with `N=2`, `\|\psi\|^2=2`. -/
theorem N2_second_derivatives (TchainSq TantiSq : ℝ)
    (hchain : TchainSq = 16 / 5) (hanti : TantiSq = 24 / 5) :
    (4 / (2:ℝ)) * (TantiSq - 2 * 2) = 8 / 5 ∧ (4 / (2:ℝ)) * (TchainSq - 2 * 2) = -(8 / 5) := by
  constructor <;> nlinarith [hchain, hanti]

/-- The exact check `\sum_C \mu_2''(C) = 8/5 - 8/5 = 0` (Appendix G, consistency with
(G.6)). -/
theorem N2_second_derivative_sum_zero : (8:ℝ) / 5 + (-(8 / 5)) = 0 := by norm_num

/-! ## §6, Appendix F: exact Fisher spectra -/

/-- `\operatorname{spec}_+(\widehat F_2) = \{2/9\}` (manuscript (6.6), Appendix F
(F.5)–(F.7)). -/
theorem N2_Fisher_spectrum : (1 / 81 : ℝ) / (1 / 18) = 2 / 9 := by norm_num

/-- `\operatorname{spec}_+(\widehat F_3) = \{3/8, 3/40, 3/200\}` (manuscript (6.8),
Appendix F (F.8)–(F.10)). -/
theorem N3_Fisher_spectrum :
    (1 / 32 : ℝ) / (1 / 12) = 3 / 8 ∧
    (1 / 1200 : ℝ) / (1 / 90) = 3 / 40 ∧
    (1 / 180000 : ℝ) / (1 / 2700) = 3 / 200 := by
  refine ⟨by norm_num, by norm_num, by norm_num⟩

/-- The three isolated (pure) `N=4` eigenvalues `12/25, 4/25, 4/525` (manuscript
(6.10), Appendix F (F.14)). -/
theorem N4_pure_eigenvalues :
    (4 / 75 : ℝ) / (1 / 9) = 12 / 25 ∧
    (8 / 3375 : ℝ) / (2 / 135) = 4 / 25 ∧
    (2 / 4134375 : ℝ) / (1 / 15750) = 4 / 525 := by
  refine ⟨by norm_num, by norm_num, by norm_num⟩

/-- **The `N=4` mixed-block characteristic determinant** (manuscript (6.11)–(6.12),
Appendix F (F.15)): expanding `det(G_{[P],\rm mix}^{(4)} - \lambda G_{\rm full,\rm
mix}^{(4)})` from the exact matrix entries in the manuscript gives, as a polynomial
identity in `\lambda`, exactly the cubic `144703125\lambda^3 - 9975000\lambda^2 +
142000\lambda - 128` up to the (verified nonzero) rational factor exhibited here — the
paper's own "up to a nonzero rational factor" qualifier, made exact. -/
theorem N4_cubic_determinant (l : ℝ) :
    ((1 / 55125 - l / 1050) * (11 / 455625 - l / 2025) * (11 / 5402250000 - l / 490000)
        - (1 / 55125 - l / 1050) * (1 / 49612500 : ℝ) ^ 2
        - (1 / 354375 : ℝ) ^ 2 * (11 / 5402250000 - l / 490000)
        + 2 * (1 / 354375) * (1 / 38587500) * (-1 / 49612500)
        - (1 / 38587500 : ℝ) ^ 2 * (11 / 455625 - l / 2025))
      = (-1 / 150760759570312500000 : ℝ) *
          (144703125 * l ^ 3 - 9975000 * l ^ 2 + 142000 * l - 128) := by
  ring

theorem N4_cubic_factor_ne_zero : (-1 / 150760759570312500000 : ℝ) ≠ 0 := by norm_num

-- The decreasing numerical order (6.13) combining the three pure eigenvalues with the
-- three cubic roots is *not* formalized: the manuscript gives the cubic's roots only
-- as numerical decimal truncations (F.16), with no closed form to check against
-- exactly. This gap is intentional and reported in `FORMALIZATION_STATUS.md`.

end HorizonFormal.S1Paper
