import Mathlib

/-!
# B2 — lema 1: la desigualdad de calibración (AM-GM)

Paso puntual de la cota superior por calibración del certificado de la compuerta de B2
(`research_program/puente_3p1/2026-10-11/B2_path2_gate_certificate.md` §2.4).

Con `W_c = c ln V + Phi_c(UV)` y `w = UV`, a lo largo de una curva causal futura con `V > 0`:

  `dW_c = Phi' · (V dU) + (Phi' w + c) · (dV / V)`,   `dtau = sqrt(F dU dV)`.

Con `a = dV/V >= 0` y `b = V dU >= 0` se tiene `a b = dU dV`. Así que `dW_c >= dtau` es
exactamente `calib_amgm`. `calib_phi` comprueba que la elección
`Phi' = F / (2 (c + sqrt(c² + F w)))` cumple sus tres hipótesis, con igualdad en la tercera.

Alcance: solo el álgebra puntual. **No** formaliza la integración a lo largo de la curva, ni
la validez de `c` en el rectángulo causal, ni la monotonía del `sup` (lema 2, no autorizado).
-/

namespace NachoFormal

/-- **Lema 1.** Si `p >= 0`, `p w + c >= 0`, `4 p (p w + c) >= F`, `a >= 0` y `b >= 0`, entonces
`p b + (p w + c) a >= sqrt(F a b)`. -/
theorem calib_amgm {F w c a b p : ℝ}
    (hp : 0 ≤ p) (hq : 0 ≤ p * w + c) (hF : F ≤ 4 * p * (p * w + c))
    (ha : 0 ≤ a) (hb : 0 ≤ b) :
    Real.sqrt (F * a * b) ≤ p * b + (p * w + c) * a := by
  have hA : 0 ≤ p * b := mul_nonneg hp hb
  have hB : 0 ≤ (p * w + c) * a := mul_nonneg hq ha
  have hab : 0 ≤ a * b := mul_nonneg ha hb
  have key : F * a * b ≤ (p * b + (p * w + c) * a) ^ 2 := by
    have h1 : F * (a * b) ≤ 4 * p * (p * w + c) * (a * b) :=
      mul_le_mul_of_nonneg_right hF hab
    nlinarith [sq_nonneg (p * b - (p * w + c) * a)]
  calc Real.sqrt (F * a * b)
      ≤ Real.sqrt ((p * b + (p * w + c) * a) ^ 2) := Real.sqrt_le_sqrt key
    _ = p * b + (p * w + c) * a := Real.sqrt_sq (add_nonneg hA hB)

/-- La elección de `Phi'` del certificado: con `F >= 0`, `c² + F w >= 0` y
`c + sqrt(c² + F w) > 0`, `p = F / (2 (c + sqrt(c² + F w)))` cumple las tres hipótesis de
`calib_amgm`, con igualdad en la tercera. Además `p w + c = (sqrt(c² + F w) + c) / 2`. -/
theorem calib_phi {F w c : ℝ} (hF : 0 ≤ F) (hdisc : 0 ≤ c ^ 2 + F * w)
    (hden : 0 < c + Real.sqrt (c ^ 2 + F * w)) :
    0 ≤ F / (2 * (c + Real.sqrt (c ^ 2 + F * w))) ∧
    F / (2 * (c + Real.sqrt (c ^ 2 + F * w))) * w + c
        = (Real.sqrt (c ^ 2 + F * w) + c) / 2 ∧
    0 ≤ F / (2 * (c + Real.sqrt (c ^ 2 + F * w))) * w + c ∧
    4 * (F / (2 * (c + Real.sqrt (c ^ 2 + F * w))))
        * (F / (2 * (c + Real.sqrt (c ^ 2 + F * w))) * w + c) = F := by
  set s := Real.sqrt (c ^ 2 + F * w) with hs_def
  have hs2 : s ^ 2 = c ^ 2 + F * w := Real.sq_sqrt hdisc
  have hden' : (2 * (c + s)) ≠ 0 := by positivity
  have hmid : F / (2 * (c + s)) * w + c = (s + c) / 2 := by
    field_simp
    nlinarith [hs2]
  refine ⟨by positivity, hmid, ?_, ?_⟩
  · rw [hmid]; linarith
  · rw [hmid]
    field_simp
    ring

/-- Los dos lemas juntos: la calibración del certificado domina el tiempo propio puntual. -/
theorem calib_bound {F w c a b : ℝ} (hF : 0 ≤ F) (hdisc : 0 ≤ c ^ 2 + F * w)
    (hden : 0 < c + Real.sqrt (c ^ 2 + F * w)) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    Real.sqrt (F * a * b) ≤
      F / (2 * (c + Real.sqrt (c ^ 2 + F * w))) * b
        + (F / (2 * (c + Real.sqrt (c ^ 2 + F * w))) * w + c) * a := by
  obtain ⟨hp, -, hq, heq⟩ := calib_phi hF hdisc hden
  exact calib_amgm hp hq heq.ge ha hb

end NachoFormal
