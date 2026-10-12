# Encargo para Codex — lema 2 de B2: monotonía de la separación temporal respecto a los extremos

**Autoriza:** el PI, 2026-10-12. **Proyecto:** `nachocausal/formal/`. Lean `v4.31.0`, Mathlib
`fabf563`, ya configurados: `lake exe cache get && lake build` funciona. **Rama:**
`codex/lean-lema2`. No hacer commit en `main`.

## Contexto (para entender, no para formalizar)

El certificado de la compuerta de B2 acota cada par de celdas `x ∈ P`, `y ∈ Q` con un solo par
de esquinas. Se apoya en esto: si `a' ≤ a` (componente a componente, es decir, `a'` está en el
pasado causal de `a`), entonces `τ(a', b) >= τ(a, b)`. La razón es que cualquier curva de `a` a
`b`, precedida del tramo de `a'` a `a`, es una curva de `a'` a `b` al menos igual de larga. Ver
`research_program/puente_3p1/2026-10-11/B2_path2_gate_certificate.md` §2.2. El lema 1 (AM-GM)
ya está en `NachoFormal/Calibration.lean`.

## Qué formalizar

Fichero nuevo `NachoFormal/Monotonicity.lean`, importado desde `NachoFormal.lean`. **No**
modificar `Calibration.lean`.

**Datos.** Una función `q : ℝ → ℝ` con `hq0 : ∀ w, 0 ≤ q w` y `hqc : Continuous q`. Los puntos
son `ℝ × ℝ`, con coordenadas `(U, V)`.

**Curva causal futura** de `a` a `b` con duración `T`: `T : ℝ`, `0 ≤ T`, `γ : ℝ → ℝ × ℝ` tales
que
- `γ 0 = a` y `γ T = b`;
- `MonotoneOn (fun s => (γ s).1) (Set.Icc 0 T)`, y lo mismo para `.2`;
- `LipschitzOnWith K γ (Set.Icc 0 T)` para algún `K`, o bien Lipschitz componente a componente:
  lo que resulte más cómodo, justificándolo en un comentario.

**Longitud:**

```text
L q γ T = ∫ s in (0)..T, q ((γ s).1 * (γ s).2) * Real.sqrt (deriv (fun s => (γ s).1) s * deriv (fun s => (γ s).2) s)
```

`deriv` vale 0 donde no hay derivada. Las curvas Lipschitz y monótonas son derivables en casi
todo punto, así que la definición es la correcta en c.t.p.

**Separación:** `tau q a b = sSup {ℓ | ∃ T γ, curva causal de a a b ∧ ℓ = L q γ T}`.

**Teoremas exigidos:**

1. `length_nonneg`: `0 ≤ L q γ T` para toda curva causal.
2. `concat_length`: si `γ₁` va de `a` a `m` en `T₁` y `γ₂` va de `m` a `b` en `T₂`, la curva
   concatenada `γ s = if s ≤ T₁ then γ₁ s else γ₂ (s - T₁)` va de `a` a `b` en `T₁ + T₂` y
   cumple `L q γ (T₁+T₂) = L q γ₁ T₁ + L q γ₂ T₂`. La idea es que las derivadas coinciden en los
   abiertos `(0,T₁)` y `(T₁,T₁+T₂)`, el punto `T₁` es nulo, y se usan
   `intervalIntegral.integral_add_adjacent_intervals` y la traslación
   `intervalIntegral.integral_comp_sub_right`.
3. `segment_is_causal`: si `a ≤ b` componente a componente, el segmento afín
   `s ↦ a + s • (b - a)` sobre `[0,1]` es una curva causal de `a` a `b`.
4. `tau_mono_left`: si `a' ≤ a` y `a ≤ b` componente a componente, el conjunto de longitudes de
   `a` a `b` es no vacío, y el de `a'` a `b` está acotado superiormente (hipótesis
   `BddAbove`), entonces `tau q a b ≤ tau q a' b`.
5. `tau_mono_right`: el simétrico, con `a ≤ b ≤ b'`, para `tau q a b ≤ tau q a b'`.
6. `capped_mono`: con `p b = (1 - Real.cos (min b Real.pi)) / 2`, `p` es monótona en `[0, ∞)`.
   Junto con 4 y 5, eso da `p (tau q a b) ≤ p (tau q a' b)` cuando `0 ≤ tau q a b`.

Las hipótesis de acotación (`BddAbove`) son explícitas a propósito: la cota superior viene de
Cauchy–Schwarz (`q_max · sqrt(ΔU ΔV)`) y **no** forma parte de este encargo.

## Fuera del alcance (no hacerlo)

- La equivalencia entre esta clase de curvas y la clase de gráficas `U(V)` absolutamente
  continuas de B1.2, es decir, el argumento de regularización `V_ε`. Será el lema 3.
- La cota de Cauchy–Schwarz y la calibración, que ya es el lema 1.
- Tocar cualquier cosa fuera de `formal/`.

## Criterio de aceptación

- `lake build` sin errores, **sin `sorry`** ni `admit` y sin `axiom` nuevos.
- `lake env lean Axioms.lean`, tras añadir `#print axioms` para los seis teoremas, muestra solo
  `propext`, `Classical.choice` y `Quot.sound`.
- Cada teorema lleva un docstring en español con su enunciado en lenguaje natural.
- Hay que actualizar `formal/README.md` con una fila para `Monotonicity.lean`.
- Si un enunciado resulta **falso** tal como está escrito, por ejemplo por un caso límite con
  `T = 0`, no se debilita en silencio. Se documenta en un comentario `-- AJUSTE:` qué se
  cambió y por qué, y se informa en el mensaje final.

## Cómo lanzarlo

```sh
cd ~/nachocausal && git checkout -b codex/lean-lema2
codex exec --model gpt-6-astra -c 'model_reasoning_effort="high"' --sandbox workspace-write \
  -C ~/nachocausal "Lee formal/TAREA_LEMA2_CODEX.md y cúmplelo. Trabaja solo en formal/. Termina con lake build limpio y el resultado de #print axioms."
```
