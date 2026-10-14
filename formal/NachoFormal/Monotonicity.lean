import Mathlib

/-!
# B2 — lema 2: monotonía de la separación temporal respecto a los extremos

Encargo: `formal/TAREA_LEMA2_CODEX.md` (autorizado por el PI el 2026-10-12). Contexto en
`research_program/puente_3p1/2026-10-11/B2_path2_gate_certificate.md` §2.2: si `a' ≤ a`
componente a componente, toda curva causal de `a` a `b`, precedida del segmento de `a'` a `a`,
es una curva causal de `a'` a `b` al menos igual de larga; luego `τ(a', b) ≥ τ(a, b)`.

Puntos en `ℝ × ℝ` con coordenadas `(U, V)` y el orden producto. La longitud de una curva es
`∫₀ᵀ q(U V) √(U' V')`, con `deriv` (que vale 0 donde no hay derivada).

**Elección de la hipótesis de regularidad.** El encargo admite Lipschitz para `γ` o Lipschitz
componente a componente. Se usa la segunda, con una constante común `K` para las dos
componentes: es la forma en que se usa (cota de `|U'|` y `|V'|` para la integrabilidad), y la
concatenación y el segmento la conservan sin pasar por la norma de `ℝ × ℝ`. Para `ℝ × ℝ` con la
norma del máximo ambas formulaciones son equivalentes con la misma constante.

Fuera del alcance: la equivalencia con la clase de gráficas `U(V)` de B1.2 (lema 3), la cota de
Cauchy–Schwarz y la calibración (lema 1, `Calibration.lean`).
-/

namespace NachoFormal

open MeasureTheory Set Filter Topology

/-- Integrando de la longitud: `q(U V) √(U' V')`. -/
noncomputable def lenIntegrand (q : ℝ → ℝ) (γ : ℝ → ℝ × ℝ) (s : ℝ) : ℝ :=
  q ((γ s).1 * (γ s).2) *
    Real.sqrt (deriv (fun s => (γ s).1) s * deriv (fun s => (γ s).2) s)

/-- Longitud de `γ` en `[0, T]`: `L q γ T = ∫₀ᵀ q(U V) √(U' V') ds`. -/
noncomputable def L (q : ℝ → ℝ) (γ : ℝ → ℝ × ℝ) (T : ℝ) : ℝ :=
  ∫ s in (0 : ℝ)..T, lenIntegrand q γ s

/-- Curva causal futura de `a` a `b` con duración `T`: `T ≥ 0`, extremos `a` y `b`, ambas
componentes monótonas y Lipschitz (con una constante común) en `[0, T]`. -/
structure IsCausalCurve (a b : ℝ × ℝ) (T : ℝ) (γ : ℝ → ℝ × ℝ) : Prop where
  nonneg : 0 ≤ T
  start : γ 0 = a
  finish : γ T = b
  mono₁ : MonotoneOn (fun s => (γ s).1) (Icc 0 T)
  mono₂ : MonotoneOn (fun s => (γ s).2) (Icc 0 T)
  lip : ∃ K : NNReal, LipschitzOnWith K (fun s => (γ s).1) (Icc 0 T) ∧
    LipschitzOnWith K (fun s => (γ s).2) (Icc 0 T)

/-- Conjunto de longitudes de las curvas causales de `a` a `b`. -/
def lengths (q : ℝ → ℝ) (a b : ℝ × ℝ) : Set ℝ :=
  {ℓ | ∃ T γ, IsCausalCurve a b T γ ∧ ℓ = L q γ T}

/-- Separación temporal: `τ(a, b) = sup` de las longitudes de curvas causales de `a` a `b`. -/
noncomputable def tau (q : ℝ → ℝ) (a b : ℝ × ℝ) : ℝ :=
  sSup (lengths q a b)

/-- Concatenación: `γ₁` en `[0, T₁]` y después `γ₂` desplazada. -/
noncomputable def concat (γ₁ γ₂ : ℝ → ℝ × ℝ) (T₁ : ℝ) : ℝ → ℝ × ℝ :=
  fun s => if s ≤ T₁ then γ₁ s else γ₂ (s - T₁)

variable {q : ℝ → ℝ}

/-- **Teorema 1.** Si `q ≥ 0`, la longitud de toda curva causal es no negativa. -/
theorem length_nonneg (hq0 : ∀ w, 0 ≤ q w) {a b : ℝ × ℝ} {T : ℝ} {γ : ℝ → ℝ × ℝ}
    (h : IsCausalCurve a b T γ) : 0 ≤ L q γ T :=
  intervalIntegral.integral_nonneg h.nonneg fun _ _ => mul_nonneg (hq0 _) (Real.sqrt_nonneg _)

/-- Con `q` continua, el integrando de una curva causal es integrable en `[0, T]`: la parte
`q(U V)` es continua en el compacto y `|U'|, |V'| ≤ K` en el interior. -/
theorem integrable_of_causal (hqc : Continuous q) {a b : ℝ × ℝ} {T : ℝ} {γ : ℝ → ℝ × ℝ}
    (h : IsCausalCurve a b T γ) : IntervalIntegrable (lenIntegrand q γ) volume 0 T := by
  obtain ⟨K, hK1, hK2⟩ := h.lip
  rw [intervalIntegrable_iff_integrableOn_Ioc_of_le h.nonneg,
    integrableOn_Ioc_iff_integrableOn_Ioo]
  have hqpart : ContinuousOn (fun s => q ((γ s).1 * (γ s).2)) (Icc 0 T) :=
    hqc.comp_continuousOn (hK1.continuousOn.mul hK2.continuousOn)
  obtain ⟨C, hC⟩ := isCompact_Icc.exists_bound_of_continuousOn hqpart
  refine IntegrableOn.of_bound measure_Ioo_lt_top ?_ (C * K) ?_
  · have m1 : AEStronglyMeasurable (fun s => q ((γ s).1 * (γ s).2))
        (volume.restrict (Ioo 0 T)) :=
      (hqpart.mono Ioo_subset_Icc_self).aestronglyMeasurable measurableSet_Ioo
    have m2 : AEStronglyMeasurable
        (fun s => Real.sqrt (deriv (fun s => (γ s).1) s * deriv (fun s => (γ s).2) s))
        (volume.restrict (Ioo 0 T)) :=
      ((measurable_deriv _).mul (measurable_deriv _)).sqrt.aestronglyMeasurable
    exact m1.mul m2
  · refine ae_restrict_of_forall_mem measurableSet_Ioo fun s hs => ?_
    have hn : Icc 0 T ∈ 𝓝 s := Icc_mem_nhds hs.1 hs.2
    have d1 := norm_deriv_le_of_lipschitzOn hn hK1
    have d2 := norm_deriv_le_of_lipschitzOn hn hK2
    rw [Real.norm_eq_abs] at d1 d2
    have hCs := hC s (Ioo_subset_Icc_self hs)
    have hsq : Real.sqrt (deriv (fun s => (γ s).1) s * deriv (fun s => (γ s).2) s) ≤ K := by
      calc Real.sqrt (deriv (fun s => (γ s).1) s * deriv (fun s => (γ s).2) s)
          ≤ Real.sqrt ((K : ℝ) * K) := by
            apply Real.sqrt_le_sqrt
            calc deriv (fun s => (γ s).1) s * deriv (fun s => (γ s).2) s
                ≤ |deriv (fun s => (γ s).1) s * deriv (fun s => (γ s).2) s| := le_abs_self _
              _ = |deriv (fun s => (γ s).1) s| * |deriv (fun s => (γ s).2) s| := abs_mul _ _
              _ ≤ K * K := mul_le_mul d1 d2 (abs_nonneg _) K.coe_nonneg
        _ = K := Real.sqrt_mul_self K.coe_nonneg
    rw [lenIntegrand, norm_mul, Real.norm_eq_abs (Real.sqrt _),
      abs_of_nonneg (Real.sqrt_nonneg _)]
    exact mul_le_mul hCs hsq (Real.sqrt_nonneg _) ((norm_nonneg _).trans hCs)

/-- **Teorema 3.** Si `a ≤ b` componente a componente, el segmento afín `s ↦ a + s • (b - a)`
sobre `[0, 1]` es una curva causal de `a` a `b`. -/
theorem segment_is_causal {a b : ℝ × ℝ} (hab : a ≤ b) :
    IsCausalCurve a b 1 (fun s => a + s • (b - a)) where
  nonneg := zero_le_one
  start := by simp
  finish := by simp
  mono₁ := by
    intro x _ y _ hxy
    have : 0 ≤ b.1 - a.1 := sub_nonneg.mpr (Prod.le_def.mp hab).1
    simp only [Prod.fst_add, Prod.smul_fst, smul_eq_mul, Prod.fst_sub]
    nlinarith
  mono₂ := by
    intro x _ y _ hxy
    have : 0 ≤ b.2 - a.2 := sub_nonneg.mpr (Prod.le_def.mp hab).2
    simp only [Prod.snd_add, Prod.smul_snd, smul_eq_mul, Prod.snd_sub]
    nlinarith
  lip := by
    refine ⟨Real.toNNReal (|b.1 - a.1| + |b.2 - a.2|), ?_, ?_⟩
    · refine LipschitzOnWith.of_dist_le' fun x _ y _ => ?_
      simp only [Real.dist_eq, Prod.fst_add, Prod.smul_fst, smul_eq_mul, Prod.fst_sub]
      rw [show a.1 + x * (b.1 - a.1) - (a.1 + y * (b.1 - a.1)) = (b.1 - a.1) * (x - y) by ring,
        abs_mul]
      exact mul_le_mul_of_nonneg_right (le_add_of_nonneg_right (abs_nonneg _)) (abs_nonneg _)
    · refine LipschitzOnWith.of_dist_le' fun x _ y _ => ?_
      simp only [Real.dist_eq, Prod.snd_add, Prod.smul_snd, smul_eq_mul, Prod.snd_sub]
      rw [show a.2 + x * (b.2 - a.2) - (a.2 + y * (b.2 - a.2)) = (b.2 - a.2) * (x - y) by ring,
        abs_mul]
      exact mul_le_mul_of_nonneg_right (le_add_of_nonneg_left (abs_nonneg _)) (abs_nonneg _)

/-- Componentes de la concatenación. -/
private lemma concat_comp (γ₁ γ₂ : ℝ → ℝ × ℝ) (T₁ : ℝ) (f : ℝ × ℝ → ℝ) :
    (fun s => f (concat γ₁ γ₂ T₁ s)) =
      fun s => if s ≤ T₁ then f (γ₁ s) else f (γ₂ (s - T₁)) := by
  funext s; unfold concat; split_ifs <;> rfl

/-- Pegar dos funciones monótonas que coinciden en la junta da una función monótona. -/
private lemma glue_monotoneOn {f₁ f₂ : ℝ → ℝ} {T₁ T₂ : ℝ} (hT₂ : 0 ≤ T₂)
    (h₁ : MonotoneOn f₁ (Icc 0 T₁)) (h₂ : MonotoneOn f₂ (Icc 0 T₂)) (hm : f₁ T₁ = f₂ 0)
    (hT₁ : 0 ≤ T₁) :
    MonotoneOn (fun s => if s ≤ T₁ then f₁ s else f₂ (s - T₁)) (Icc 0 (T₁ + T₂)) := by
  intro x hx y hy hxy
  simp only
  split_ifs with h1 h2 h2
  · exact h₁ ⟨hx.1, h1⟩ ⟨hy.1, h2⟩ hxy
  · calc f₁ x ≤ f₁ T₁ := h₁ ⟨hx.1, h1⟩ ⟨hT₁, le_rfl⟩ h1
      _ = f₂ 0 := hm
      _ ≤ f₂ (y - T₁) := h₂ ⟨le_rfl, hT₂⟩ ⟨by linarith, by linarith [hy.2]⟩ (by linarith)
  · exact absurd (hxy.trans h2) h1
  · exact h₂ ⟨by linarith, by linarith [hx.2]⟩ ⟨by linarith, by linarith [hy.2]⟩ (by linarith)

/-- Caso mixto de la cota de Lipschitz al pegar: `x ≤ T₁ < y`. -/
private lemma glue_dist_mixed {f₁ f₂ : ℝ → ℝ} {T₁ T₂ : ℝ} {K : NNReal}
    (h₁ : LipschitzOnWith K f₁ (Icc 0 T₁)) (h₂ : LipschitzOnWith K f₂ (Icc 0 T₂))
    (hm : f₁ T₁ = f₂ 0) (hT₁ : 0 ≤ T₁) (hT₂ : 0 ≤ T₂) {x y : ℝ} (hx0 : 0 ≤ x) (hxT : x ≤ T₁)
    (hyT : T₁ < y) (hy : y ≤ T₁ + T₂) :
    dist (f₁ x) (f₂ (y - T₁)) ≤ K * dist x y := by
  have e1 := h₁.dist_le_mul x ⟨hx0, hxT⟩ T₁ ⟨hT₁, le_rfl⟩
  have e2 := h₂.dist_le_mul 0 ⟨le_rfl, hT₂⟩ (y - T₁) ⟨by linarith, by linarith⟩
  rw [Real.dist_eq, Real.dist_eq, abs_of_nonpos (by linarith : x - T₁ ≤ 0)] at e1
  rw [Real.dist_eq, Real.dist_eq, abs_of_nonpos (by linarith : (0 : ℝ) - (y - T₁) ≤ 0)] at e2
  rw [Real.dist_eq, Real.dist_eq x y, abs_of_nonpos (by linarith : x - y ≤ 0)]
  calc |f₁ x - f₂ (y - T₁)| ≤ |f₁ x - f₁ T₁| + |f₂ 0 - f₂ (y - T₁)| := by
        rw [← hm]; exact abs_sub_le _ _ _
    _ ≤ K * -(x - T₁) + K * -(0 - (y - T₁)) := add_le_add e1 e2
    _ = K * -(x - y) := by ring

/-- Pegar dos funciones `K`-Lipschitz que coinciden en la junta da una función `K`-Lipschitz. -/
private lemma glue_lipschitzOn {f₁ f₂ : ℝ → ℝ} {T₁ T₂ : ℝ} {K : NNReal}
    (h₁ : LipschitzOnWith K f₁ (Icc 0 T₁)) (h₂ : LipschitzOnWith K f₂ (Icc 0 T₂))
    (hm : f₁ T₁ = f₂ 0) (hT₁ : 0 ≤ T₁) (hT₂ : 0 ≤ T₂) :
    LipschitzOnWith K (fun s => if s ≤ T₁ then f₁ s else f₂ (s - T₁)) (Icc 0 (T₁ + T₂)) := by
  refine LipschitzOnWith.of_dist_le_mul fun x hx y hy => ?_
  split_ifs with h1 h2 h2
  · exact h₁.dist_le_mul x ⟨hx.1, h1⟩ y ⟨hy.1, h2⟩
  · exact glue_dist_mixed h₁ h₂ hm hT₁ hT₂ hx.1 h1 (lt_of_not_ge h2) hy.2
  · rw [dist_comm, dist_comm x]
    exact glue_dist_mixed h₁ h₂ hm hT₁ hT₂ hy.1 h2 (lt_of_not_ge h1) hx.2
  · have := h₂.dist_le_mul (x - T₁) ⟨by linarith [lt_of_not_ge h1], by linarith [hx.2]⟩
      (y - T₁) ⟨by linarith [lt_of_not_ge h2], by linarith [hy.2]⟩
    rwa [Real.dist_eq (x - T₁), show x - T₁ - (y - T₁) = x - y by ring, ← Real.dist_eq] at this

/-- La concatenación de dos curvas causales que se encuentran en `m` es causal. -/
theorem concat_is_causal {a m b : ℝ × ℝ} {T₁ T₂ : ℝ} {γ₁ γ₂ : ℝ → ℝ × ℝ}
    (h₁ : IsCausalCurve a m T₁ γ₁) (h₂ : IsCausalCurve m b T₂ γ₂) :
    IsCausalCurve a b (T₁ + T₂) (concat γ₁ γ₂ T₁) := by
  have hm : γ₁ T₁ = γ₂ 0 := h₁.finish.trans h₂.start.symm
  obtain ⟨K₁, h₁₁, h₁₂⟩ := h₁.lip
  obtain ⟨K₂, h₂₁, h₂₂⟩ := h₂.lip
  refine ⟨add_nonneg h₁.nonneg h₂.nonneg, ?_, ?_, ?_, ?_, ?_⟩
  · simp [concat, h₁.nonneg, h₁.start]
  · unfold concat
    split_ifs with h
    · have : T₂ = 0 := le_antisymm (by linarith) h₂.nonneg
      subst this
      rw [add_zero, hm, h₂.finish.symm]
    · simp [h₂.finish]
  · rw [concat_comp γ₁ γ₂ T₁ Prod.fst]
    exact glue_monotoneOn h₂.nonneg h₁.mono₁ h₂.mono₁ (congrArg Prod.fst hm) h₁.nonneg
  · rw [concat_comp γ₁ γ₂ T₁ Prod.snd]
    exact glue_monotoneOn h₂.nonneg h₁.mono₂ h₂.mono₂ (congrArg Prod.snd hm) h₁.nonneg
  · refine ⟨max K₁ K₂, ?_, ?_⟩
    · rw [concat_comp γ₁ γ₂ T₁ Prod.fst]
      exact glue_lipschitzOn (h₁₁.weaken (le_max_left _ _)) (h₂₁.weaken (le_max_right _ _))
        (congrArg Prod.fst hm) h₁.nonneg h₂.nonneg
    · rw [concat_comp γ₁ γ₂ T₁ Prod.snd]
      exact glue_lipschitzOn (h₁₂.weaken (le_max_left _ _)) (h₂₂.weaken (le_max_right _ _))
        (congrArg Prod.snd hm) h₁.nonneg h₂.nonneg

/-- Antes de la junta, el integrando de la concatenación es el de `γ₁`. -/
private lemma lenIntegrand_concat_left (γ₁ γ₂ : ℝ → ℝ × ℝ) {T₁ x : ℝ} (hx : x < T₁) :
    lenIntegrand q (concat γ₁ γ₂ T₁) x = lenIntegrand q γ₁ x := by
  have hev : concat γ₁ γ₂ T₁ =ᶠ[𝓝 x] γ₁ := by
    filter_upwards [Iio_mem_nhds hx] with s hs
    simp [concat, (mem_Iio.mp hs).le]
  have d1 : deriv (fun s => (concat γ₁ γ₂ T₁ s).1) x = deriv (fun s => (γ₁ s).1) x :=
    (hev.fun_comp Prod.fst).deriv_eq
  have d2 : deriv (fun s => (concat γ₁ γ₂ T₁ s).2) x = deriv (fun s => (γ₁ s).2) x :=
    (hev.fun_comp Prod.snd).deriv_eq
  simp only [lenIntegrand, d1, d2, hev.eq_of_nhds]

/-- Después de la junta, el integrando de la concatenación es el de `γ₂` desplazado. -/
private lemma lenIntegrand_concat_right (γ₁ γ₂ : ℝ → ℝ × ℝ) {T₁ x : ℝ} (hx : T₁ < x) :
    lenIntegrand q (concat γ₁ γ₂ T₁) x = lenIntegrand q γ₂ (x - T₁) := by
  have hev : concat γ₁ γ₂ T₁ =ᶠ[𝓝 x] fun s => γ₂ (s - T₁) := by
    filter_upwards [Ioi_mem_nhds hx] with s hs
    simp [concat, not_le.mpr (mem_Ioi.mp hs)]
  have d1 : deriv (fun s => (concat γ₁ γ₂ T₁ s).1) x = deriv (fun s => (γ₂ s).1) (x - T₁) := by
    exact (hev.fun_comp Prod.fst).deriv_eq.trans (deriv_comp_sub_const (f := fun s => (γ₂ s).1) T₁ x)
  have d2 : deriv (fun s => (concat γ₁ γ₂ T₁ s).2) x = deriv (fun s => (γ₂ s).2) (x - T₁) := by
    exact (hev.fun_comp Prod.snd).deriv_eq.trans (deriv_comp_sub_const (f := fun s => (γ₂ s).2) T₁ x)
  simp only [lenIntegrand, d1, d2, hev.eq_of_nhds]

/-- **Teorema 2.** Si `γ₁` va de `a` a `m` en `T₁` y `γ₂` de `m` a `b` en `T₂`, la curva
concatenada `γ s = if s ≤ T₁ then γ₁ s else γ₂ (s - T₁)` va de `a` a `b` en `T₁ + T₂` y su
longitud es la suma: `L q γ (T₁ + T₂) = L q γ₁ T₁ + L q γ₂ T₂`. -/
theorem concat_length (hqc : Continuous q) {a m b : ℝ × ℝ} {T₁ T₂ : ℝ}
    {γ₁ γ₂ : ℝ → ℝ × ℝ} (h₁ : IsCausalCurve a m T₁ γ₁) (h₂ : IsCausalCurve m b T₂ γ₂) :
    IsCausalCurve a b (T₁ + T₂) (concat γ₁ γ₂ T₁) ∧
      L q (concat γ₁ γ₂ T₁) (T₁ + T₂) = L q γ₁ T₁ + L q γ₂ T₂ := by
  have hc := concat_is_causal h₁ h₂
  refine ⟨hc, ?_⟩
  have hT₁ := h₁.nonneg
  have hT₂ := h₂.nonneg
  have hint := integrable_of_causal (q := q) hqc hc
  have i1 : IntervalIntegrable (lenIntegrand q (concat γ₁ γ₂ T₁)) volume 0 T₁ :=
    hint.mono_set (by
      rw [uIcc_of_le hT₁, uIcc_of_le (add_nonneg hT₁ hT₂)]
      exact Icc_subset_Icc le_rfl (le_add_of_nonneg_right hT₂))
  have i2 : IntervalIntegrable (lenIntegrand q (concat γ₁ γ₂ T₁)) volume T₁ (T₁ + T₂) :=
    hint.mono_set (by
      rw [uIcc_of_le (le_add_of_nonneg_right hT₂), uIcc_of_le (add_nonneg hT₁ hT₂)]
      exact Icc_subset_Icc hT₁ le_rfl)
  unfold L
  rw [← intervalIntegral.integral_add_adjacent_intervals i1 i2]
  congr 1
  · refine intervalIntegral.integral_congr_ae ?_
    have hne : ∀ᵐ x ∂(volume : Measure ℝ), x ∉ ({T₁} : Set ℝ) :=
      measure_eq_zero_iff_ae_notMem.mp (Real.volume_singleton)
    filter_upwards [hne] with x hx hxI
    rw [uIoc_of_le hT₁] at hxI
    exact lenIntegrand_concat_left γ₁ γ₂ (lt_of_le_of_ne hxI.2 hx)
  · calc ∫ x in T₁..T₁ + T₂, lenIntegrand q (concat γ₁ γ₂ T₁) x
        = ∫ x in T₁..T₁ + T₂, lenIntegrand q γ₂ (x - T₁) := by
          refine intervalIntegral.integral_congr_ae (ae_of_all _ fun x hxI => ?_)
          rw [uIoc_of_le (le_add_of_nonneg_right hT₂)] at hxI
          exact lenIntegrand_concat_right γ₁ γ₂ hxI.1
      _ = ∫ x in (0 : ℝ)..T₂, lenIntegrand q γ₂ x := by
          rw [intervalIntegral.integral_comp_sub_right]; simp

/-- **Teorema 4.** Si `a' ≤ a` y `a ≤ b` componente a componente, el conjunto de longitudes de
`a` a `b` es no vacío y el de `a'` a `b` está acotado superiormente, entonces
`τ(a, b) ≤ τ(a', b)`: alejar el extremo inicial hacia el pasado no acorta la separación. -/
theorem tau_mono_left (hq0 : ∀ w, 0 ≤ q w) (hqc : Continuous q) {a' a b : ℝ × ℝ}
    (ha : a' ≤ a) (_hab : a ≤ b) (hne : (lengths q a b).Nonempty)
    (hbdd : BddAbove (lengths q a' b)) : tau q a b ≤ tau q a' b := by
  apply csSup_le hne
  rintro ℓ ⟨T, γ, hγ, rfl⟩
  obtain ⟨hc, hL⟩ := concat_length (q := q) hqc (segment_is_causal ha) hγ
  refine le_trans ?_ (le_csSup hbdd ⟨1 + T, _, hc, rfl⟩)
  rw [hL]
  linarith [length_nonneg (q := q) hq0 (segment_is_causal ha)]

/-- **Teorema 5.** Si `a ≤ b ≤ b'` componente a componente, el conjunto de longitudes de `a` a
`b` es no vacío y el de `a` a `b'` está acotado superiormente, entonces `τ(a, b) ≤ τ(a, b')`:
alejar el extremo final hacia el futuro no acorta la separación. -/
theorem tau_mono_right (hq0 : ∀ w, 0 ≤ q w) (hqc : Continuous q) {a b b' : ℝ × ℝ}
    (_hab : a ≤ b) (hb : b ≤ b') (hne : (lengths q a b).Nonempty)
    (hbdd : BddAbove (lengths q a b')) : tau q a b ≤ tau q a b' := by
  apply csSup_le hne
  rintro ℓ ⟨T, γ, hγ, rfl⟩
  obtain ⟨hc, hL⟩ := concat_length (q := q) hqc hγ (segment_is_causal hb)
  refine le_trans ?_ (le_csSup hbdd ⟨T + 1, _, hc, rfl⟩)
  rw [hL]
  linarith [length_nonneg (q := q) hq0 (segment_is_causal hb)]

/-- Probabilidad acotada del certificado: `p(b) = (1 - cos(min(b, π))) / 2`. -/
noncomputable def pCap (b : ℝ) : ℝ := (1 - Real.cos (min b Real.pi)) / 2

/-- **Teorema 6.** `p(b) = (1 - cos(min(b, π))) / 2` es monótona en `[0, ∞)`. -/
theorem capped_mono : MonotoneOn pCap (Ici 0) := by
  intro x hx y hy hxy
  have hx' : min x Real.pi ∈ Icc 0 Real.pi :=
    ⟨le_min (mem_Ici.mp hx) Real.pi_pos.le, min_le_right _ _⟩
  have hy' : min y Real.pi ∈ Icc 0 Real.pi :=
    ⟨le_min (mem_Ici.mp hy) Real.pi_pos.le, min_le_right _ _⟩
  have := Real.antitoneOn_cos hx' hy' (min_le_min hxy le_rfl)
  unfold pCap
  linarith

/-- Corolario de 4 y 6: con las hipótesis de `tau_mono_left` y `0 ≤ τ(a, b)`,
`p(τ(a, b)) ≤ p(τ(a', b))`. -/
theorem capped_tau_mono_left (hq0 : ∀ w, 0 ≤ q w) (hqc : Continuous q) {a' a b : ℝ × ℝ}
    (ha : a' ≤ a) (hab : a ≤ b) (hne : (lengths q a b).Nonempty)
    (hbdd : BddAbove (lengths q a' b)) (h0 : 0 ≤ tau q a b) :
    pCap (tau q a b) ≤ pCap (tau q a' b) := by
  have hle := tau_mono_left hq0 hqc ha hab hne hbdd
  exact capped_mono (mem_Ici.mpr h0) (mem_Ici.mpr (h0.trans hle)) hle

/-- Corolario de 5 y 6: con las hipótesis de `tau_mono_right` y `0 ≤ τ(a, b)`,
`p(τ(a, b)) ≤ p(τ(a, b'))`. -/
theorem capped_tau_mono_right (hq0 : ∀ w, 0 ≤ q w) (hqc : Continuous q) {a b b' : ℝ × ℝ}
    (hab : a ≤ b) (hb : b ≤ b') (hne : (lengths q a b).Nonempty)
    (hbdd : BddAbove (lengths q a b')) (h0 : 0 ≤ tau q a b) :
    pCap (tau q a b) ≤ pCap (tau q a b') := by
  have hle := tau_mono_right hq0 hqc hab hb hne hbdd
  exact capped_mono (mem_Ici.mpr h0) (mem_Ici.mpr (h0.trans hle)) hle

end NachoFormal
