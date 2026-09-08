import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.Order.Compact
import Mathlib.Data.Set.Function
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# E2: segment accessibility in a compact future box

This is the first deterministic lemma for the E2 formalisation.  The
Schwarzschild-specific work is isolated in the hypotheses `hz_seg` and
`hT_seg`: later modules can discharge them from the concrete null-coordinate
formulae for `z` and `T`.  No action functional, grid approximation, or
probabilistic input is used here.
-/

namespace HorizonFormal

open Set

abbrev Point := ℝ × ℝ

/-- The six scalar inequalities defining a compact future box. -/
def FutureBox (z T : Point → ℝ) (a b t₀ t₁ vₓ wₓ : ℝ) : Set Point :=
  {p | a ≤ z p ∧ z p ≤ b ∧ t₀ ≤ T p ∧ T p ≤ t₁ ∧ vₓ ≤ p.1 ∧ wₓ ≤ p.2}

theorem segment_mem_futureBox
    {z T : Point → ℝ} {a b t₀ t₁ vₓ wₓ : ℝ}
    {p q : Point}
    (hp : p ∈ FutureBox z T a b t₀ t₁ vₓ wₓ)
    (hq : q ∈ FutureBox z T a b t₀ t₁ vₓ wₓ)
    (hz_seg : ∀ θ ∈ Icc (0 : ℝ) 1,
      z ((1 - θ) • p + θ • q) ∈ Icc a b)
    (hT_seg : ∀ θ ∈ Icc (0 : ℝ) 1,
      T p ≤ T ((1 - θ) • p + θ • q) ∧
        T ((1 - θ) • p + θ • q) ≤ T q) :
    ∀ θ ∈ Icc (0 : ℝ) 1,
      (1 - θ) • p + θ • q ∈ FutureBox z T a b t₀ t₁ vₓ wₓ := by
  intro θ hθ
  rcases hp with ⟨hpa, hpb, hpt₀, hpt₁, hpv, hpw⟩
  rcases hq with ⟨hqa, hqb, hqt₀, hqt₁, hqv, hqw⟩
  rcases hz_seg θ hθ with ⟨hz_lower, hz_upper⟩
  rcases hT_seg θ hθ with ⟨hT_lower, hT_upper⟩
  have hθ0 : 0 ≤ θ := hθ.1
  have hθ1 : θ ≤ 1 := hθ.2
  have hT_lower' : t₀ ≤ T ((1 - θ) • p + θ • q) :=
    le_trans hpt₀ hT_lower
  have hT_upper' : T ((1 - θ) • p + θ • q) ≤ t₁ :=
    le_trans hT_upper hqt₁
  have hpv' : vₓ ≤ ((1 - θ) • p + θ • q).1 := by
    change vₓ ≤ (1 - θ) * p.1 + θ * q.1
    calc
      vₓ = (1 - θ) * vₓ + θ * vₓ := by ring
      _ ≤ (1 - θ) * p.1 + θ * q.1 := by
        exact add_le_add
          (mul_le_mul_of_nonneg_left hpv (sub_nonneg.mpr hθ1))
          (mul_le_mul_of_nonneg_left hqv hθ0)
  have hpw' : wₓ ≤ ((1 - θ) • p + θ • q).2 := by
    change wₓ ≤ (1 - θ) * p.2 + θ * q.2
    calc
      wₓ = (1 - θ) * wₓ + θ * wₓ := by ring
      _ ≤ (1 - θ) * p.2 + θ * q.2 := by
        exact add_le_add
          (mul_le_mul_of_nonneg_left hpw (sub_nonneg.mpr hθ1))
          (mul_le_mul_of_nonneg_left hqw hθ0)
  exact ⟨hz_lower, hz_upper, hT_lower', hT_upper', hpv', hpw'⟩

private theorem affine_mem_Icc {x y a b θ : ℝ}
    (hx : x ∈ Icc a b) (hy : y ∈ Icc a b)
    (hθ : θ ∈ Icc (0 : ℝ) 1) :
    (1 - θ) * x + θ * y ∈ Icc a b := by
  constructor
  · calc
      a = (1 - θ) * a + θ * a := by ring
      _ ≤ (1 - θ) * x + θ * y := by
        exact add_le_add
          (mul_le_mul_of_nonneg_left hx.1 (sub_nonneg.mpr hθ.2))
          (mul_le_mul_of_nonneg_left hy.1 hθ.1)
  · calc
      (1 - θ) * x + θ * y ≤ (1 - θ) * b + θ * b := by
        exact add_le_add
          (mul_le_mul_of_nonneg_left hx.2 (sub_nonneg.mpr hθ.2))
          (mul_le_mul_of_nonneg_left hy.2 hθ.1)
      _ = b := by ring

noncomputable def psiInterior (rS r : ℝ) : ℝ :=
  2 * r + 2 * rS * Real.log ((rS - r) / rS)

theorem psiInterior_strictAnti_point {rS x y : ℝ}
    (hrS : 0 < rS) (hx : 0 < x) (hxy : x < y) (hy : y < rS) :
    psiInterior rS y < psiInterior rS x := by
  have hden : 0 < rS - x := sub_pos.mpr (lt_trans hxy hy)
  have hnumy : 0 < rS - y := sub_pos.mpr hy
  have htpos : 0 < (rS - y) / (rS - x) := div_pos hnumy hden
  have htlt : (rS - y) / (rS - x) < 1 := by
    rw [div_lt_iff₀ hden]
    linarith
  have hlog_bound : Real.log ((rS - y) / (rS - x)) ≤
      (rS - y) / (rS - x) - 1 :=
    Real.log_le_sub_one_of_pos htpos
  have hlogratio :
      Real.log ((rS - y) / rS) - Real.log ((rS - x) / rS) =
        Real.log ((rS - y) / (rS - x)) := by
    calc
      Real.log ((rS - y) / rS) - Real.log ((rS - x) / rS) =
          Real.log (rS - y) - Real.log (rS - x) := by
            have h1 := Real.log_div (ne_of_gt hnumy) (ne_of_gt hrS)
            have h2 := Real.log_div (ne_of_gt hden) (ne_of_gt hrS)
            rw [h1, h2]
            ring
      _ = Real.log ((rS - y) / (rS - x)) := by
        symm
        exact Real.log_div (ne_of_gt hnumy) (ne_of_gt hden)
  have hmain :
      2 * (y - x) + 2 * rS *
          (Real.log ((rS - y) / rS) - Real.log ((rS - x) / rS)) ≤
        -2 * x * (y - x) / (rS - x) := by
    rw [hlogratio]
    have halg :
        2 * (y - x) + 2 * rS *
            ((rS - y) / (rS - x) - 1) =
          -2 * x * (y - x) / (rS - x) := by
      field_simp [ne_of_gt hden]
      ring
    have hscaled := mul_le_mul_of_nonneg_left hlog_bound (by positivity : 0 ≤ 2 * rS)
    linarith [halg, hscaled]
  have hneg : -2 * x * (y - x) / (rS - x) < 0 := by
    exact div_neg_of_neg_of_pos
      (by nlinarith [hx, sub_pos.mpr hxy]) hden
  dsimp [psiInterior]
  linarith

theorem psiInterior_strictAntiOn {rS α β : ℝ}
    (hrS : 0 < rS) (hα : 0 < α) (hβ : β < rS) :
    StrictAntiOn (psiInterior rS) (Icc α β) := by
  intro x hx y hy hxy
  exact psiInterior_strictAnti_point hrS
    (lt_of_lt_of_le hα hx.1) hxy (lt_of_le_of_lt hy.2 hβ)

noncomputable def psiExterior (rS r : ℝ) : ℝ :=
  2 * r + 2 * rS * Real.log ((r - rS) / rS)

theorem psiExterior_slope_point {rS x y : ℝ}
    (hrS : 0 < rS) (hrSx : rS < x) (hxy : x ≤ y) :
    2 * (y - x) ≤ psiExterior rS y - psiExterior rS x := by
  have hargx : 0 < (x - rS) / rS :=
    div_pos (sub_pos.mpr hrSx) hrS
  have hargy : 0 < (y - rS) / rS :=
    div_pos (sub_pos.mpr (lt_of_lt_of_le hrSx hxy)) hrS
  have harg : (x - rS) / rS ≤ (y - rS) / rS := by
    exact div_le_div_of_nonneg_right (sub_le_sub_right hxy rS) hrS.le
  have hlog : Real.log ((x - rS) / rS) ≤
      Real.log ((y - rS) / rS) :=
    Real.strictMonoOn_log.monotoneOn hargx hargy harg
  dsimp [psiExterior]
  nlinarith [mul_nonneg hrS.le (sub_nonneg.mpr hlog)]

theorem psiExterior_strictMonoOn {rS α β : ℝ}
    (hrS : 0 < rS) (hα : rS < α) (hαβ : α ≤ β) :
    StrictMonoOn (psiExterior rS) (Icc α β) := by
  intro x hx y hy hxy
  have hrSx : rS < x := lt_of_lt_of_le hα hx.1
  have hbound := psiExterior_slope_point hrS hrSx hxy.le
  have hstrict : 0 < 2 * (y - x) := by positivity
  dsimp [psiExterior] at hbound ⊢
  linarith

private theorem continuousOn_psiExterior {rS α β : ℝ}
    (hrS : 0 < rS) (hα : rS < α) :
    ContinuousOn (psiExterior rS) (Icc α β) := by
  have harg : ContinuousOn (fun r : ℝ => (r - rS) / rS) (Icc α β) :=
    (continuousOn_id.sub continuousOn_const).div_const rS
  have hlog : ContinuousOn (fun r : ℝ => Real.log ((r - rS) / rS)) (Icc α β) :=
    harg.log (by
      intro r hr
      exact ne_of_gt (div_pos (sub_pos.mpr (lt_of_lt_of_le hα hr.1)) hrS))
  change ContinuousOn
    (fun r : ℝ => 2 * r + 2 * rS * Real.log ((r - rS) / rS)) (Icc α β)
  exact (continuousOn_const.mul continuousOn_id).add
    (continuousOn_const.mul hlog)

private theorem continuousOn_psiInterior {rS α β : ℝ}
    (hrS : 0 < rS) (hβ : β < rS) :
    ContinuousOn (psiInterior rS) (Icc α β) := by
  have harg : ContinuousOn (fun r : ℝ => (rS - r) / rS) (Icc α β) :=
    (continuousOn_const.sub continuousOn_id).div_const rS
  have hlog : ContinuousOn (fun r : ℝ => Real.log ((rS - r) / rS)) (Icc α β) :=
    harg.log (by
      intro r hr
      exact ne_of_gt (div_pos (sub_pos.mpr (lt_of_le_of_lt hr.2 hβ)) hrS))
  change ContinuousOn
    (fun r : ℝ => 2 * r + 2 * rS * Real.log ((rS - r) / rS)) (Icc α β)
  exact (continuousOn_const.mul continuousOn_id).add
    (continuousOn_const.mul hlog)

theorem psiExterior_image_Icc {rS α β : ℝ}
    (hrS : 0 < rS) (hα : rS < α) (hαβ : α ≤ β) :
    psiExterior rS '' Icc α β = Icc (psiExterior rS α) (psiExterior rS β) := by
  apply ContinuousOn.image_Icc_of_monotoneOn hαβ
    (continuousOn_psiExterior hrS hα)
  exact (psiExterior_strictMonoOn hrS hα hαβ).monotoneOn

theorem psiInterior_image_Icc {rS α β : ℝ}
    (hrS : 0 < rS) (hα : 0 < α) (hαβ : α ≤ β) (hβ : β < rS) :
    psiInterior rS '' Icc α β = Icc (psiInterior rS β) (psiInterior rS α) := by
  apply ContinuousOn.image_Icc_of_antitoneOn hαβ
    (continuousOn_psiInterior hrS hβ)
  exact (psiInterior_strictAntiOn hrS hα hβ).antitoneOn

theorem inverse_slope_ge_two_on_image
    {ψ h : ℝ → ℝ} {I : Set ℝ}
    (hleft : Set.LeftInvOn h ψ I)
    (hslope : ∀ ⦃x : ℝ⦄, x ∈ I → ∀ ⦃y : ℝ⦄, y ∈ I → x ≤ y →
      2 * (y - x) ≤ ψ y - ψ x)
    {u v : ℝ} (hu : u ∈ ψ '' I) (hv : v ∈ ψ '' I) (huv : u ≤ v) :
    0 ≤ h v - h u ∧ h v - h u ≤ (v - u) / 2 := by
  rcases hu with ⟨x, hx, rfl⟩
  rcases hv with ⟨y, hy, rfl⟩
  have hxu : h (ψ x) = x := hleft hx
  have hyv : h (ψ y) = y := hleft hy
  have hxy : x ≤ y := by
    by_contra hnot
    have hyx : y ≤ x := le_of_not_ge hnot
    have hs := hslope hy hx hyx
    linarith
  constructor
  · rw [hyv, hxu]
    exact sub_nonneg.mpr hxy
  · rw [hyv, hxu]
    have hs := hslope hx hy hxy
    linarith

noncomputable def psiExteriorInv (rS α β : ℝ) : ℝ → ℝ :=
  Function.invFunOn (psiExterior rS) (Icc α β)

noncomputable def psiInteriorInv (rS α β : ℝ) : ℝ → ℝ :=
  Function.invFunOn (psiInterior rS) (Icc α β)

theorem psiExteriorInv_mem {rS α β z : ℝ}
    (hrS : 0 < rS) (hα : rS < α) (hαβ : α ≤ β)
    (hz : z ∈ Icc (psiExterior rS α) (psiExterior rS β)) :
    psiExteriorInv rS α β z ∈ Icc α β := by
  rw [← psiExterior_image_Icc hrS hα hαβ] at hz
  exact Function.invFunOn_mem (by exact hz)

theorem psiExteriorInv_rightInverse {rS α β z : ℝ}
    (hrS : 0 < rS) (hα : rS < α) (hαβ : α ≤ β)
    (hz : z ∈ Icc (psiExterior rS α) (psiExterior rS β)) :
    psiExterior rS (psiExteriorInv rS α β z) = z := by
  rw [← psiExterior_image_Icc hrS hα hαβ] at hz
  exact Function.invFunOn_eq (by exact hz)

theorem psiExteriorInv_leftInverse {rS α β r : ℝ}
    (hrS : 0 < rS) (hα : rS < α) (hαβ : α ≤ β)
    (hr : r ∈ Icc α β) :
    psiExteriorInv rS α β (psiExterior rS r) = r := by
  change Function.invFunOn (psiExterior rS) (Icc α β) (psiExterior rS r) = r
  exact (psiExterior_strictMonoOn hrS hα hαβ).injOn.leftInvOn_invFunOn hr

theorem psiExteriorInv_order {rS α β u v : ℝ}
    (hrS : 0 < rS) (hα : rS < α) (hαβ : α ≤ β)
    (hu : u ∈ Icc (psiExterior rS α) (psiExterior rS β))
    (hv : v ∈ Icc (psiExterior rS α) (psiExterior rS β)) (huv : u ≤ v) :
    0 ≤ psiExteriorInv rS α β v - psiExteriorInv rS α β u ∧
      psiExteriorInv rS α β v - psiExteriorInv rS α β u ≤ (v - u) / 2 := by
  rw [← psiExterior_image_Icc hrS hα hαβ] at hu hv
  apply inverse_slope_ge_two_on_image
    ((psiExterior_strictMonoOn hrS hα hαβ).injOn.leftInvOn_invFunOn)
  · intro x hx y hy hxy
    exact psiExterior_slope_point hrS (lt_of_lt_of_le hα hx.1) hxy
  · exact hu
  · exact hv
  · exact huv

theorem psiExteriorInv_monotoneOn {rS α β : ℝ}
    (hrS : 0 < rS) (hα : rS < α) (hαβ : α ≤ β) :
    MonotoneOn (psiExteriorInv rS α β)
      (Icc (psiExterior rS α) (psiExterior rS β)) := by
  intro u hu v hv huv
  exact sub_nonneg.mp (psiExteriorInv_order hrS hα hαβ hu hv huv).1

theorem psiInteriorInv_mem {rS α β z : ℝ}
    (hrS : 0 < rS) (hα : 0 < α) (hαβ : α ≤ β) (hβ : β < rS)
    (hz : z ∈ Icc (psiInterior rS β) (psiInterior rS α)) :
    psiInteriorInv rS α β z ∈ Icc α β := by
  rw [← psiInterior_image_Icc hrS hα hαβ hβ] at hz
  exact Function.invFunOn_mem
    (show ∃ a ∈ Icc α β, psiInterior rS a = z from hz)

theorem psiInteriorInv_rightInverse {rS α β z : ℝ}
    (hrS : 0 < rS) (hα : 0 < α) (hαβ : α ≤ β) (hβ : β < rS)
    (hz : z ∈ Icc (psiInterior rS β) (psiInterior rS α)) :
    psiInterior rS (psiInteriorInv rS α β z) = z := by
  rw [← psiInterior_image_Icc hrS hα hαβ hβ] at hz
  exact Function.invFunOn_eq
    (show ∃ a ∈ Icc α β, psiInterior rS a = z from hz)

theorem psiInteriorInv_leftInverse {rS α β r : ℝ}
    (hrS : 0 < rS) (hα : 0 < α) (hαβ : α ≤ β) (hβ : β < rS)
    (hr : r ∈ Icc α β) :
    psiInteriorInv rS α β (psiInterior rS r) = r := by
  change Function.invFunOn (psiInterior rS) (Icc α β) (psiInterior rS r) = r
  exact (psiInterior_strictAntiOn hrS hα hβ).injOn.leftInvOn_invFunOn hr

theorem psiInteriorInv_antitoneOn {rS α β : ℝ}
    (hrS : 0 < rS) (hα : 0 < α) (hαβ : α ≤ β) (hβ : β < rS) :
    AntitoneOn (psiInteriorInv rS α β)
      (Icc (psiInterior rS β) (psiInterior rS α)) := by
  intro u hu v hv huv
  rw [← psiInterior_image_Icc hrS hα hαβ hβ] at hu hv
  rcases hu with ⟨x, hx, rfl⟩
  rcases hv with ⟨y, hy, rfl⟩
  rw [psiInteriorInv_leftInverse hrS hα hαβ hβ hx,
    psiInteriorInv_leftInverse hrS hα hαβ hβ hy]
  by_contra hnot
  have hxy : x < y := lt_of_not_ge hnot
  have hstrict := (psiInterior_strictAntiOn hrS hα hβ) hx hy hxy
  linarith

/-- Exterior null coordinates: `z = v - w`, `T = v - h (v - w)`.

The assumptions on `h` are the exact scalar properties needed from the
exterior inverse radial map.  In particular, `h_oneLip` is used only when the
radial null coordinate increases along a comparable segment.
-/
theorem segment_mem_exteriorFutureBoxOn
    {h : ℝ → ℝ} {a b t₀ t₁ vₓ wₓ : ℝ}
    {p q : Point}
    (h_mono : MonotoneOn h (Icc a b))
    (h_oneLip : ∀ ⦃x y : ℝ⦄, x ∈ Icc a b → y ∈ Icc a b → x ≤ y →
      h y - h x ≤ y - x)
    (hp : p ∈ FutureBox (fun r => r.1 - r.2)
      (fun r => r.1 - h (r.1 - r.2)) a b t₀ t₁ vₓ wₓ)
    (hq : q ∈ FutureBox (fun r => r.1 - r.2)
      (fun r => r.1 - h (r.1 - r.2)) a b t₀ t₁ vₓ wₓ)
    (hpq : p.1 ≤ q.1 ∧ p.2 ≤ q.2) :
    ∀ θ ∈ Icc (0 : ℝ) 1,
      (1 - θ) • p + θ • q ∈ FutureBox (fun r => r.1 - r.2)
        (fun r => r.1 - h (r.1 - r.2)) a b t₀ t₁ vₓ wₓ := by
  intro θ hθ
  have hz_seg : ∀ θ ∈ Icc (0 : ℝ) 1,
      (fun r : Point => r.1 - r.2) ((1 - θ) • p + θ • q) ∈ Icc a b := by
    intro θ hθ
    have hlin : ((1 - θ) • p + θ • q) =
        ((1 - θ) * p.1 + θ * q.1, (1 - θ) * p.2 + θ * q.2) := by rfl
    rw [hlin]
    have hpz : p.1 - p.2 ∈ Icc a b := by
      exact ⟨by simpa using hp.1, by simpa using hp.2.1⟩
    have hqz : q.1 - q.2 ∈ Icc a b := by
      exact ⟨by simpa using hq.1, by simpa using hq.2.1⟩
    have hm := affine_mem_Icc hpz hqz hθ
    change ((1 - θ) * p.1 + θ * q.1) -
      ((1 - θ) * p.2 + θ * q.2) ∈ Icc a b
    convert hm using 1 <;> ring
  have hT_seg : ∀ θ ∈ Icc (0 : ℝ) 1,
      p.1 - h (p.1 - p.2) ≤
          ((1 - θ) • p + θ • q).1 -
            h (((1 - θ) • p + θ • q).1 - ((1 - θ) • p + θ • q).2) ∧
        ((1 - θ) • p + θ • q).1 -
            h (((1 - θ) • p + θ • q).1 - ((1 - θ) • p + θ • q).2) ≤
          q.1 - h (q.1 - q.2) := by
    intro θ hθ
    have hθ0 : 0 ≤ θ := hθ.1
    have hθ1 : θ ≤ 1 := hθ.2
    have hV : (1 - θ) * p.1 + θ * q.1 - p.1 ≥ 0 := by
      rw [show (1 - θ) * p.1 + θ * q.1 - p.1 = θ * (q.1 - p.1) by ring]
      exact mul_nonneg hθ0 (sub_nonneg.mpr hpq.1)
    have hW : (1 - θ) * p.2 + θ * q.2 - p.2 ≥ 0 := by
      rw [show (1 - θ) * p.2 + θ * q.2 - p.2 = θ * (q.2 - p.2) by ring]
      exact mul_nonneg hθ0 (sub_nonneg.mpr hpq.2)
    have hVq : q.1 - ((1 - θ) * p.1 + θ * q.1) ≥ 0 := by
      rw [show q.1 - ((1 - θ) * p.1 + θ * q.1) =
          (1 - θ) * (q.1 - p.1) by ring]
      exact mul_nonneg (sub_nonneg.mpr hθ1) (sub_nonneg.mpr hpq.1)
    have hWq : q.2 - ((1 - θ) * p.2 + θ * q.2) ≥ 0 := by
      rw [show q.2 - ((1 - θ) * p.2 + θ * q.2) =
          (1 - θ) * (q.2 - p.2) by ring]
      exact mul_nonneg (sub_nonneg.mpr hθ1) (sub_nonneg.mpr hpq.2)
    have hD : (1 - θ) * (p.1 - p.2) + θ * (q.1 - q.2) -
        (p.1 - p.2) = θ * ((q.1 - p.1) - (q.2 - p.2)) := by ring
    have hzp : p.1 - p.2 ∈ Icc a b :=
      ⟨by simpa using hp.1, by simpa using hp.2.1⟩
    have hzq : q.1 - q.2 ∈ Icc a b :=
      ⟨by simpa using hq.1, by simpa using hq.2.1⟩
    have hzθ : (1 - θ) * (p.1 - p.2) + θ * (q.1 - q.2) ∈ Icc a b :=
      affine_mem_Icc hzp hzq hθ
    have hT_lower : p.1 - h (p.1 - p.2) ≤
        (1 - θ) * p.1 + θ * q.1 -
          h ((1 - θ) * (p.1 - p.2) + θ * (q.1 - q.2)) := by
      by_cases hd : (1 - θ) * (p.1 - p.2) + θ * (q.1 - q.2) ≤ p.1 - p.2
      · have hh := h_mono hzθ hzp hd
        linarith [hV]
      · have hd' : p.1 - p.2 ≤
          (1 - θ) * (p.1 - p.2) + θ * (q.1 - q.2) := le_of_not_ge hd
        have hh := h_oneLip hzp hzθ hd'
        linarith [hV, hW, hD]
    have hT_upper :
        (1 - θ) * p.1 + θ * q.1 -
          h ((1 - θ) * (p.1 - p.2) + θ * (q.1 - q.2)) ≤
        q.1 - h (q.1 - q.2) := by
      by_cases hd : (1 - θ) * (p.1 - p.2) + θ * (q.1 - q.2) ≤ q.1 - q.2
      · have hh := h_oneLip hzθ hzq hd
        linarith [hVq, hWq]
      · have hd' : q.1 - q.2 ≤
          (1 - θ) * (p.1 - p.2) + θ * (q.1 - q.2) := le_of_not_ge hd
        have hh := h_mono hzq hzθ hd'
        linarith [hVq]
    have hlin : ((1 - θ) • p + θ • q) =
        ((1 - θ) * p.1 + θ * q.1, (1 - θ) * p.2 + θ * q.2) := by rfl
    rw [hlin]
    convert And.intro hT_lower hT_upper using 1 <;> ring
  exact segment_mem_futureBox hp hq hz_seg hT_seg θ hθ

/-- Interior null coordinates: `z = v + w`, `T = v - h (v + w)`.

Here `h_antitone` is the exact interior monotonicity property of the inverse
radial map; no Lipschitz estimate is needed for the temporal coordinate.
-/
theorem segment_mem_interiorFutureBoxOn
    {h : ℝ → ℝ} {a b t₀ t₁ vₓ wₓ : ℝ}
    {p q : Point}
    (h_antitone : AntitoneOn h (Icc a b))
    (hp : p ∈ FutureBox (fun r => r.1 + r.2)
      (fun r => r.1 - h (r.1 + r.2)) a b t₀ t₁ vₓ wₓ)
    (hq : q ∈ FutureBox (fun r => r.1 + r.2)
      (fun r => r.1 - h (r.1 + r.2)) a b t₀ t₁ vₓ wₓ)
    (hpq : p.1 ≤ q.1 ∧ p.2 ≤ q.2) :
    ∀ θ ∈ Icc (0 : ℝ) 1,
      (1 - θ) • p + θ • q ∈ FutureBox (fun r => r.1 + r.2)
        (fun r => r.1 - h (r.1 + r.2)) a b t₀ t₁ vₓ wₓ := by
  intro θ hθ
  have hz_seg : ∀ θ ∈ Icc (0 : ℝ) 1,
      (fun r : Point => r.1 + r.2) ((1 - θ) • p + θ • q) ∈ Icc a b := by
    intro θ hθ
    have hlin : ((1 - θ) • p + θ • q) =
        ((1 - θ) * p.1 + θ * q.1, (1 - θ) * p.2 + θ * q.2) := by rfl
    rw [hlin]
    have hpz : p.1 + p.2 ∈ Icc a b := by
      exact ⟨by simpa using hp.1, by simpa using hp.2.1⟩
    have hqz : q.1 + q.2 ∈ Icc a b := by
      exact ⟨by simpa using hq.1, by simpa using hq.2.1⟩
    have hm := affine_mem_Icc hpz hqz hθ
    change ((1 - θ) * p.1 + θ * q.1) +
      ((1 - θ) * p.2 + θ * q.2) ∈ Icc a b
    convert hm using 1 <;> ring
  have hT_seg : ∀ θ ∈ Icc (0 : ℝ) 1,
      p.1 - h (p.1 + p.2) ≤
          ((1 - θ) • p + θ • q).1 -
            h (((1 - θ) • p + θ • q).1 + ((1 - θ) • p + θ • q).2) ∧
        ((1 - θ) • p + θ • q).1 -
            h (((1 - θ) • p + θ • q).1 + ((1 - θ) • p + θ • q).2) ≤
          q.1 - h (q.1 + q.2) := by
    intro θ hθ
    have hθ0 : 0 ≤ θ := hθ.1
    have hV : 0 ≤ θ * (q.1 - p.1) := mul_nonneg hθ0 (sub_nonneg.mpr hpq.1)
    have hS : p.1 + p.2 ≤ (1 - θ) * (p.1 + p.2) + θ * (q.1 + q.2) := by
      calc
        p.1 + p.2 = (1 - θ) * (p.1 + p.2) + θ * (p.1 + p.2) := by ring
        _ ≤ (1 - θ) * (p.1 + p.2) + θ * (q.1 + q.2) := by
          exact add_le_add (le_refl _)
            (mul_le_mul_of_nonneg_left (add_le_add hpq.1 hpq.2) hθ0)
    have hSq : (1 - θ) * (p.1 + p.2) + θ * (q.1 + q.2) ≤ q.1 + q.2 := by
      have hθ1 : θ ≤ 1 := hθ.2
      calc
        (1 - θ) * (p.1 + p.2) + θ * (q.1 + q.2) ≤
            (1 - θ) * (q.1 + q.2) + θ * (q.1 + q.2) := by
          exact add_le_add
            (mul_le_mul_of_nonneg_left (add_le_add hpq.1 hpq.2)
              (sub_nonneg.mpr hθ.2)) (le_refl _)
        _ = q.1 + q.2 := by ring
    have hlin : ((1 - θ) • p + θ • q) =
        ((1 - θ) * p.1 + θ * q.1, (1 - θ) * p.2 + θ * q.2) := by rfl
    rw [hlin]
    have hT :
        p.1 - h (p.1 + p.2) ≤
          (1 - θ) * p.1 + θ * q.1 -
            h ((1 - θ) * (p.1 + p.2) + θ * (q.1 + q.2)) ∧
          (1 - θ) * p.1 + θ * q.1 -
            h ((1 - θ) * (p.1 + p.2) + θ * (q.1 + q.2)) ≤
          q.1 - h (q.1 + q.2) := by
      constructor
      · have hh := h_antitone
          ⟨by simpa using hp.1, by simpa using hp.2.1⟩
          (affine_mem_Icc
            ⟨by simpa using hp.1, by simpa using hp.2.1⟩
            ⟨by simpa using hq.1, by simpa using hq.2.1⟩ hθ) hS
        have hV' : 0 ≤ (1 - θ) * p.1 + θ * q.1 - p.1 := by
          rw [show (1 - θ) * p.1 + θ * q.1 - p.1 = θ * (q.1 - p.1) by ring]
          exact hV
        linarith [hV']
      · have hVq : (1 - θ) * p.1 + θ * q.1 ≤ q.1 := by
          calc
            (1 - θ) * p.1 + θ * q.1 ≤ (1 - θ) * q.1 + θ * q.1 := by
              exact add_le_add
                (mul_le_mul_of_nonneg_left hpq.1 (sub_nonneg.mpr hθ.2))
                (le_refl _)
            _ = q.1 := by ring
        have hh := h_antitone
          (affine_mem_Icc
            ⟨by simpa using hp.1, by simpa using hp.2.1⟩
            ⟨by simpa using hq.1, by simpa using hq.2.1⟩ hθ)
          ⟨by simpa using hq.1, by simpa using hq.2.1⟩ hSq
        linarith [hVq]
    simp only [Prod.fst, Prod.snd]
    convert hT using 1 <;> ring
  exact segment_mem_futureBox hp hq hz_seg hT_seg θ hθ

theorem segment_mem_exteriorFutureBox
    {h : ℝ → ℝ} {a b t₀ t₁ vₓ wₓ : ℝ} {p q : Point}
    (h_mono : Monotone h)
    (h_oneLip : ∀ x y : ℝ, h x - h y ≤ x - y)
    (hp : p ∈ FutureBox (fun r => r.1 - r.2)
      (fun r => r.1 - h (r.1 - r.2)) a b t₀ t₁ vₓ wₓ)
    (hq : q ∈ FutureBox (fun r => r.1 - r.2)
      (fun r => r.1 - h (r.1 - r.2)) a b t₀ t₁ vₓ wₓ)
    (hpq : p.1 ≤ q.1 ∧ p.2 ≤ q.2) :
    ∀ θ ∈ Icc (0 : ℝ) 1,
      (1 - θ) • p + θ • q ∈ FutureBox (fun r => r.1 - r.2)
        (fun r => r.1 - h (r.1 - r.2)) a b t₀ t₁ vₓ wₓ := by
  apply segment_mem_exteriorFutureBoxOn
  · intro x hx y hy hxy
    exact h_mono hxy
  · intro x y hx hy hxy
    exact h_oneLip y x
  · exact hp
  · exact hq
  · exact hpq

theorem segment_mem_interiorFutureBox
    {h : ℝ → ℝ} {a b t₀ t₁ vₓ wₓ : ℝ} {p q : Point}
    (h_antitone : Antitone h)
    (hp : p ∈ FutureBox (fun r => r.1 + r.2)
      (fun r => r.1 - h (r.1 + r.2)) a b t₀ t₁ vₓ wₓ)
    (hq : q ∈ FutureBox (fun r => r.1 + r.2)
      (fun r => r.1 - h (r.1 + r.2)) a b t₀ t₁ vₓ wₓ)
    (hpq : p.1 ≤ q.1 ∧ p.2 ≤ q.2) :
    ∀ θ ∈ Icc (0 : ℝ) 1,
      (1 - θ) • p + θ • q ∈ FutureBox (fun r => r.1 + r.2)
        (fun r => r.1 - h (r.1 + r.2)) a b t₀ t₁ vₓ wₓ := by
  apply segment_mem_interiorFutureBoxOn
  · intro x hx y hy hxy
    exact h_antitone hxy
  · exact hp
  · exact hq
  · exact hpq

/-- Schwarzschild exterior accessibility on the compact radial image.

The inverse is only used on `Icc (psiExterior rS α) (psiExterior rS β)`,
where its radial membership, inverse identities, and order estimates have
already been proved above.
-/
theorem schwarzschild_exterior_segment_accessible
    {rS α β t₀ t₁ vₓ wₓ : ℝ} {p q : Point}
    (hrS : 0 < rS) (hα : rS < α) (hαβ : α ≤ β)
    (hp : p ∈ FutureBox (fun r => r.1 - r.2)
      (fun r => r.1 - psiExteriorInv rS α β (r.1 - r.2))
      (psiExterior rS α) (psiExterior rS β) t₀ t₁ vₓ wₓ)
    (hq : q ∈ FutureBox (fun r => r.1 - r.2)
      (fun r => r.1 - psiExteriorInv rS α β (r.1 - r.2))
      (psiExterior rS α) (psiExterior rS β) t₀ t₁ vₓ wₓ)
    (hpq : p.1 ≤ q.1 ∧ p.2 ≤ q.2) :
    ∀ θ ∈ Icc (0 : ℝ) 1,
      (1 - θ) • p + θ • q ∈ FutureBox (fun r => r.1 - r.2)
        (fun r => r.1 - psiExteriorInv rS α β (r.1 - r.2))
        (psiExterior rS α) (psiExterior rS β) t₀ t₁ vₓ wₓ := by
  apply segment_mem_exteriorFutureBoxOn
  · exact psiExteriorInv_monotoneOn hrS hα hαβ
  · intro x y hx hy hxy
    have hord := psiExteriorInv_order hrS hα hαβ hx hy hxy
    linarith [hord.2]
  · exact hp
  · exact hq
  · exact hpq

/-- Schwarzschild interior accessibility on the compact radial image. -/
theorem schwarzschild_interior_segment_accessible
    {rS α β t₀ t₁ vₓ wₓ : ℝ} {p q : Point}
    (hrS : 0 < rS) (hα : 0 < α) (hαβ : α ≤ β) (hβ : β < rS)
    (hp : p ∈ FutureBox (fun r => r.1 + r.2)
      (fun r => r.1 - psiInteriorInv rS α β (r.1 + r.2))
      (psiInterior rS β) (psiInterior rS α) t₀ t₁ vₓ wₓ)
    (hq : q ∈ FutureBox (fun r => r.1 + r.2)
      (fun r => r.1 - psiInteriorInv rS α β (r.1 + r.2))
      (psiInterior rS β) (psiInterior rS α) t₀ t₁ vₓ wₓ)
    (hpq : p.1 ≤ q.1 ∧ p.2 ≤ q.2) :
    ∀ θ ∈ Icc (0 : ℝ) 1,
      (1 - θ) • p + θ • q ∈ FutureBox (fun r => r.1 + r.2)
        (fun r => r.1 - psiInteriorInv rS α β (r.1 + r.2))
        (psiInterior rS β) (psiInterior rS α) t₀ t₁ vₓ wₓ := by
  apply segment_mem_interiorFutureBoxOn
  · exact psiInteriorInv_antitoneOn hrS hα hαβ hβ
  · exact hp
  · exact hq
  · exact hpq

#print axioms segment_mem_exteriorFutureBoxOn
#print axioms segment_mem_interiorFutureBoxOn
#print axioms inverse_slope_ge_two_on_image
#print axioms psiInterior_strictAnti_point
#print axioms psiInterior_strictAntiOn
#print axioms psiExterior_slope_point
#print axioms psiExterior_strictMonoOn
#print axioms psiExterior_image_Icc
#print axioms psiInterior_image_Icc
#print axioms psiExteriorInv_mem
#print axioms psiExteriorInv_rightInverse
#print axioms psiExteriorInv_leftInverse
#print axioms psiExteriorInv_order
#print axioms psiExteriorInv_monotoneOn
#print axioms psiInteriorInv_mem
#print axioms psiInteriorInv_rightInverse
#print axioms psiInteriorInv_leftInverse
#print axioms psiInteriorInv_antitoneOn
#print axioms inverse_slope_ge_two_on_image
#print axioms schwarzschild_exterior_segment_accessible
#print axioms schwarzschild_interior_segment_accessible

end HorizonFormal
