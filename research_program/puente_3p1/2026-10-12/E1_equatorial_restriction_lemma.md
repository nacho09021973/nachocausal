# E1 — Lema ecuatorial: el orden causal de Schwarzschild 3+1D restringido al ecuador es el de la métrica 2+1D inducida

> **STATUS: `PROOF_WRITTEN / PENDING_AUDIT`.** Unidad teórica. **No** abre ningún frente 2+1D:
> eso necesita un acta aprobada por el PI. Es el primer paso que el PI autorizó el 2026-10-12
> («¿Empiezo por el lema ecuatorial?» — «sí»).

**Fecha:** 2026-10-12 · **Depende de:** B1.2
(`research_program/puente_3p1/2026-09-12/B1/B1_2_angular_causal_reach.md` §1–§2) y la
representación de la compuerta, H1 (`research_program/puente_3p1/2026-10-11/B2_path2_gate_certificate.md` §6).

## 1. Enunciado

Sea `(M⁴, g)` el sector de Kruskal de Schwarzschild que usa el puente:

```text
g = −C(UV) dU dV + r(UV)² dΩ²,     −UV = (s−1) e^s,   s = r/(2M),   C = 32 M³ e^{−s} / r,
```

con orientación temporal futura `dU >= 0`, `dV >= 0` (B1.2 §1). Sea `E = {θ = π/2}` el ecuador y
`(E, g_E)` la variedad 2+1D con la métrica inducida:

```text
g_E = −C(UV) dU dV + r(UV)² dφ².
```

**Lema E1.** Para `x, y ∈ E`, y para cualquier dominio de la forma `D × S²` con `D` un
conjunto del plano `(U, V)` (en particular el parche `K × S²`):

```text
existe una curva causal futura de x a y en D × S²   ⟺   existe una curva causal futura de x a y en D × S¹_E,
```

donde `S¹_E` es el ecuador de `S²` y las curvas se toman en la misma clase de regularidad:
absolutamente continuas, o localmente Lipschitz. Es decir, `J⁺_{3+1} ∩ (E × E) = J⁺_{2+1}`.

## 2. Demostración

**(⇐)** Una curva causal de `(E, g_E)` es una curva de `M⁴` contenida en `E`. Como `g_E` es la
restricción de `g`, su vector tangente tiene la misma norma en ambas métricas. Por tanto es
causal futura en `M⁴`.

**(⇒) Proyección por longitud recorrida.** Sea `γ(λ) = (U(λ), V(λ), ω(λ))`, con `λ ∈ [0, 1]`,
causal futura de `x` a `y` en `D × S²`. La causalidad, en casi todo punto, es

```text
r(UV)² |ω'|²_{S²}  <=  C(UV) U' V',       U' >= 0,  V' >= 0.                    (1)
```

Sea `ℓ(λ) = ∫_0^λ |ω'(μ)| dμ` la longitud recorrida sobre `S²`. Es no decreciente,
absolutamente continua (o Lipschitz, si `γ` lo es) y cumple `ℓ' = |ω'|` en casi todo punto. Sea
`Δ ∈ [0, π]` la distancia de círculo máximo entre `ω(0) = ω_x` y `ω(1) = ω_y`. Como `ω_x` y
`ω_y` están en el ecuador, que es un círculo máximo, `Δ` es también su distancia angular dentro
del ecuador. Además, ninguna curva en `S²` es más corta que el círculo máximo, así que
`ℓ(1) >= Δ`.

Sea `σ ∈ {+1, −1}` el sentido del arco ecuatorial corto de `φ_x` a `φ_y`. Se define

```text
α(λ) = φ_x + σ · min(ℓ(λ), Δ),          γ_E(λ) = (U(λ), V(λ), θ = π/2, φ = α(λ)).
```

Entonces:
- **Extremos.** `α(0) = φ_x` y `α(1) = φ_x + σΔ = φ_y` (mod 2π), porque `ℓ(1) >= Δ`. Las
  coordenadas `U` y `V` no cambian, así que `γ_E` va de `x` a `y` y su proyección al plano
  `(U, V)` es la de `γ`. Por tanto se queda en `D × S¹_E`.
- **Regularidad.** `min(ℓ, Δ)` es absolutamente continua (o Lipschitz) si `ℓ` lo es, y además
  `|α'| <= ℓ' = |ω'|` en casi todo punto.
- **Causalidad.** `r` solo depende de `UV`, que no cambia. Por (1),
  `r² |α'|² <= r² |ω'|² <= C U' V'`, y `U'`, `V'` no cambian de signo. Por tanto `γ_E` es causal
  futura en `(E, g_E)`. ∎

**Observaciones.**
- La demostración no usa nada de Schwarzschild salvo la estructura de producto deformado
  `M² ×_r S²` y que el ecuador sea un círculo máximo. Vale igual para cualquier métrica
  `−C dU dV + r² dΩ²` con `C, r > 0` dependientes solo de `(U, V)`.
- Tampoco usa ninguna forma especial de la curva: sirve para la separación temporal general de
  la compuerta (H1, curvas causales futuras cualesquiera), no solo para la clase de gráficas
  `U(V)` de B1.2.

## 3. Consecuencia: qué se hereda y qué cambia en un banco 2+1D ecuatorial

**Se hereda exactamente.** La relación causal entre dos puntos `(U_x, V_x, φ_x)` y
`(U_y, V_y, φ_y)` es

```text
x ≺ y   ⟺   distancia angular ecuatorial(φ_x, φ_y)  <=  Delta_max(U_x, V_x; U_y, V_y),
```

con **el mismo** `Delta_max = min(π, sup L[U])` de B1.2. Por E1, el `sup` de las longitudes
angulares alcanzables es el mismo en `S²` y en `S¹`. Toda la maquinaria certificada de
`Delta_max` se aplica sin cambios:
- la representación como separación temporal de `q² dU dV`;
- la monotonía respecto a los extremos;
- la cota de la recta;
- Cauchy–Schwarz integral;
- la calibración.

**Cambia:**

| objeto | 3+1D (puente) | 2+1D ecuatorial |
|---|---|---|
| elemento de volumen | `∝ r² C dU dV dΩ`, peso `G(w) = s e^{−s}` | `∝ r C dU dV dφ`, peso `G_2(w) = e^{−s}` |
| ley angular de un par al azar | `p(b) = (1 − cos min(b, π))/2` | `p_2(b) = min(b, π)/π` |
| fracción interior `φ` | `Z_in/Z` con `G` | `Z_in/Z` con `G_2` |

La ley `p_2` es lineal, y por tanto Lipschitz con constante `1/π`. Para dos ángulos
independientes y uniformes en `S¹`, la distancia es uniforme en `[0, π]`. En cuanto al peso:
`r · C = 32 M³ e^{−s}`, frente a `r² · C ∝ s e^{−s}` en 3+1D, con las constantes absorbidas en la
normalización.

**No se hereda ningún resultado de B2, B3 ni B4:** `ρ`, `φ` y sus derivadas cambian con `G_2` y
`p_2`. Lo que se hereda es la maquinaria para certificarlos.

## 4. Lo que E1 no dice

- E1 no hace de `(E, g_E)` una solución de las ecuaciones de Einstein en 2+1D: no lo es. Es un
  banco de **geometría causal** cuyo orden coincide con el de Schwarzschild 3+1D en el ecuador.
- Un conjunto causal sembrado en `(E, g_E)` **no** es un subconjunto de un sembrado de 3+1D: el
  ecuador tiene medida cero en `M⁴`. Lo que comparten es la relación de orden entre puntos
  dados, no la ley del sembrado.
- E1 no abre ningún frente: un banco 2+1D necesita un acta con el estimador, la verdad de
  referencia y umbrales congelados, aprobada por el PI.

## 5. Qué debe mirar la auditoría

1. El caso `Δ = π`, con puntos antipodales en el ecuador: los dos sentidos sirven y `σ` se
   elige cualquiera.
2. Que `min(ℓ, Δ)` conserve la clase de regularidad elegida, y que `ℓ` esté bien definida para
   curvas solo absolutamente continuas en `S²`.
3. Que la orientación temporal y el dominio `D × S²` (o el parche) se conserven al no tocar
   `(U, V)`.
4. Que la ley `p_2` y el peso `G_2` de §3 sean correctos.
