# B1 — Par testigo mínimo en `λ`: forma cerrada de `φ`, gauge de boost y ruta a L3

> **STATUS: `THEORY_ONLY / NO_RUNS / NO_SEEDS / NO_SEAL_TOUCHED / L3_OPEN`.**
> Unidad `PUENTE-3P1/B1` bajo el bloque VÍA B (`docs/puente_schwarzschild_3p1_2026-09-12.md`).
> No autoriza simulación ni preregistro. `PHASE_0_R1` intacto.

**Fecha:** 2026-09-12 · **Verificador:** `verify_phi_and_boost.py` →
`verification_phi_and_boost.json` (`CONCLUSION = PHI_CLOSED_FORM_VERIFIED_BOOST_IS_GAUGE`)

---

## 1. Qué hace B1

Decidir si el lema de biyección bimedible de `op12_tv_zero_3p1.md` §2 fuerza `TV = 0` entre dos
formas de patch con distinta fracción interior, o si deja abierta la separación.

Resultado de esta unidad, por adelantado:

```text
B1_PHI_CLOSED_FORM        = DERIVED_AND_VERIFIED
B1_BOOST_GAUGE            = IDENTIFIED_AND_VERIFIED     (hallazgo de diseño, §3)
B1_LEMMA_FORCES_TV_ZERO   = NOT_ESTABLISHED             (§4)
B1_SEPARATION_CRITERION   = REDUCED_TO_ONE_SCALAR       (§5)
B1_BLOCKING_SUBPROBLEM    = ANGULAR_REACH_DELTA_MAX     (§6)
L3                        = OPEN
```

---

## 2. `φ(λ)` en forma cerrada

En el patch, `V ∈ [v0,v1]` con `v0 > 0`, luego `UV > 0 ⟺ U > 0`: **el interior (`r < 2M`) es
exactamente `U > 0`, y el corte del horizonte es `U = 0`**. El patch atraviesa el horizonte por
construcción.

Con `w = UV` y `s = r/(2M)` definido por `(1-s)e^s = w` (rama única, C1 de B0), el elemento de
volumen de B0 da `dVol = 32 M⁴ · G(w) · sinθ · dU dV dθ dφ` con `G(w) = s e^{-s}`. Como
`dw = -s e^s ds`,

```text
G(w) dw = -s² ds      ⟹      W(w) = -s(w)³/3   es primitiva de G.
```

Esto es el volumen euclídeo radial `r² dr` disfrazado, y colapsa la integral 2D a una 1D.
Integrando primero en `U` a `V` fija (`dU = dw/V`), y usando `s(0) = 1` en el horizonte:

```text
F_in(λ)  = (1/3) ∫_{v0}^{v1} [ 1 - s( u_in·V)³ ] dV/V
F_out(λ) = (1/3) ∫_{v0}^{v1} [ s(-u_out·V)³ - 1 ] dV/V

φ(λ) = F_in / (F_in + F_out)
```

El prefactor `32 M⁴` y el `4π` angular se cancelan en el cociente — esto es A1 y A2 del filtro,
explícitos. Verificado contra cuadratura 2D directa en tres `λ` (error `< 1e-8`, D2).

---

## 3. Hallazgo de diseño — el boost de Killing es gauge sobre `λ`

`λ` tiene 5 componentes, pero **no son 5 grados de libertad físicos**. El boost de Killing de
Schwarzschild

```text
B_a : (U, V, ω) ↦ (a·U, V/a, ω),   a > 0
```

es una isometría exacta del ambiente (`g_UV dU dV` es invariante), preserva la causalidad y
preserva `μ`. Actúa sobre el patch como

```text
B_a : (v0, v1, u_out, u_in) ↦ (v0/a, v1/a, a·u_out, a·u_in)
```

y **deja `φ` invariante** (verificado, D3, error `< 1e-9`). Por tanto `B_a` satisface las hipótesis
del lema de OP-1.2 §2 y da `TV = 0` — pero de forma **trivial y esperada**, porque es literalmente
la misma geometría reetiquetada.

Consecuencia operativa, y es la razón por la que B1 debía hacerse antes que cualquier cálculo:

> Un par testigo `λ_0 ≠ λ_1` que difiera **sólo por un boost** daría `TV = 0` y parecería matar el
> blanco. Sería un falso negativo. El par debe diferir en los **invariantes de boost**.

Los invariantes son tres (4 parámetros − 1 gauge; `ε_s` es restricción, no geometría):

```text
I₁ = v1/v0        I₂ = u_in/u_out        I₃ = u_in·v1
```

Verificado que los tres son exactamente boost-invariantes (D3, error `< 1e-12`).

```text
EFFECTIVE_LAMBDA_DIMENSION = 3
```

---

## 4. ¿Fuerza el lema `TV = 0`? — No establecido

El lema de OP-1.2 §2 exige una biyección bimedible `φ: K_{λ_0} → K_{λ_1}`, con inversa medible
módulo nulos, que empuje `μ` a `μ'` y preserve el orden inducido para c.t.p. par ordenado.

Estado honesto:

- Las **únicas** biyecciones de ese tipo conocidas hoy entre estos patches son las isometrías del
  ambiente compatibles con simetría esférica y sector fijo: el boost `B_a` (las rotaciones de `S²`
  actúan trivialmente, porque el patch contiene `S²` entero — `op11` §2).
- Todas ellas preservan `φ`. Luego para un par que difiera en `I₁,I₂,I₃` **con `φ` distinto**,
  ninguna biyección conocida aplica.
- Esto **no** es una prueba de inexistencia. `no conocida ≠ no existe`. Terminal correcto:
  `B1_LEMMA_FORCES_TV_ZERO = NOT_ESTABLISHED`, no `LEMMA_DOES_NOT_APPLY`.

Por eso B1 no se cierra por este lado, sino por el de §5, que sí es decidible.

---

## 5. Ruta de separación: la fracción de ordenación a `n = 2`

En lugar de argumentar sobre la no existencia de biyecciones, se ataca `TV > 0` directamente en el
`n` más pequeño posible.

A `n = 2` hay exactamente **dos** clases de isomorfismo de poset: la 2-cadena y la 2-anticadena.
Luego la ley del poset no etiquetado a `n=2` es un único número, la **fracción de ordenación**

```text
ρ(λ) = P( X₁ ≺ X₂  ó  X₂ ≺ X₁ ),     X₁,X₂ iid ~ μ/μ(K)
```

y por tanto, exactamente,

```text
TV( P_{λ₀,2}, P_{λ₁,2} ) = |ρ(λ₀) - ρ(λ₁)|.
```

Esto da un criterio **suficiente, exacto y sin simulación** para L3:

> **Criterio B1.** Si existe un par `λ₀, λ₁` con `φ(λ₀) ≠ φ(λ₁)` y `ρ(λ₀) ≠ ρ(λ₁)`, entonces
> `TV(P_{λ₀,2}, P_{λ₁,2}) > 0`: la ley del poset no etiquetado separa dos formas de patch con
> distinta fracción interior, ya a `n = 2`. L3 queda establecido **para ese par**.

Nótese lo que el criterio **no** da: la implicación general `φ(λ) ≠ φ(λ') ⟹ TV > 0` del contrato
L3. Un par testigo establece no-degeneración, igual que PR011 §1 hizo en 1+1D; no establece
identificabilidad de `φ`. La dirección de garantía aquí es `TV ≥ ·` (positiva), que es la difícil
— declararlo por adelantado es requisito de `claim_grammar.md` §1.7.

Además `ρ` es invariante de orden+medida, luego es automáticamente invariante bajo cualquier
biyección que satisfaga el lema de §4: si `ρ` difiere, el lema **no puede** aplicarse. Las dos
rutas son consistentes y la de §5 es estrictamente más informativa.

---

## 6. Lo que bloquea cerrar B1 hoy — el alcance angular `Δ_max`

Calcular `ρ(λ)` exige la relación causal del ambiente, y **aquí es donde 3+1D deja de parecerse a
1+1D**.

En 1+1D la causalidad en coordenadas nulas es el orden producto: `x ≺ y ⟺ U_x ≤ U_y ∧ V_x ≤ V_y`.
En 3+1D esférico eso es **sólo la condición radial** (`Δ = 0`, misma `ω`). Para separación angular
`Δ = dist_{S²}(ω_x, ω_y) > 0` hace falta además que el par tenga «margen» para recorrer `Δ`:

```text
x ≺ y   ⟺   U_x ≤ U_y ,  V_x ≤ V_y ,  y  Δ ≤ Δ_max(U_x,V_x,U_y,V_y)
```

donde `Δ_max` es el supremo del desplazamiento angular sobre curvas causales de `x` a `y` en
Schwarzschild maximal. Como el orden es el **inducido del ambiente** (`op11` §2: la curva no está
obligada a quedarse en `K`), `Δ_max` se calcula sin efectos de borde del patch — lo cual simplifica,
no complica.

`Δ_max` no es elemental: involucra el potencial angular de las curvas causales de Schwarzschild y
la estructura de la esfera de fotones. Y como `μ` sobre `S²` es continua, **casi todo par tiene
`Δ > 0`**: la ruta radial no es un atajo válido, es un conjunto de medida nula.

```text
B1_BLOCKING_SUBPROBLEM = ANGULAR_REACH_DELTA_MAX
```

Éste es el primer cálculo genuinamente 3+1D que el programa encuentra: todo lo anterior, incluido
`φ(λ)`, redujo a integrales radiales unidimensionales. `Δ_max` no reduce.

---

## 7. B1.2 — resultado cerrado y siguiente paso

`B1.2` queda completado dentro de su alcance estrecho en
`B1_2_angular_causal_reach.md`: se obtuvo una caracterización variacional exacta de
`Δ_max(U_x,V_x,U_y,V_y)` y cotas deterministas explícitas, verificadas en
`verify_angular_causal_reach.py` (`CONCLUSION = ANGULAR_REACH_VARIATIONAL_FORMULA_AND_BOUNDS_VERIFIED`).
La pieza habilita la evaluación posterior de `ρ(λ)` por cuadratura determinista; no la ejecuta.

El paso siguiente, aún no autorizado por este documento, es **B1.3**: congelar el par
`(lambda_0,lambda_1)` antes de inspeccionar `ρ`, y sólo entonces calcular la fracción de
ordenación. No se hace selección ni barrido aquí.

Declaración de eslabón, según la regla de admisión del bloque:

> `B1.2` avanza **L3**: es la única pieza que falta para evaluar `ρ(λ)` y decidir si la ley del
> poset no etiquetado separa dos formas de patch con distinta `φ`.

## 8. Fuentes

- Carta, patch, target y canal: `research_program/synthesis/op11_spherical_dual_target.md` §2, §4, §5
- Lema de biyección bimedible y órbita: `research_program/synthesis/op12_tv_zero_3p1.md` §2, §3, §7
- Patrón de par testigo / viabilidad: `research_program/synthesis/pr011_mass_distinguishability_viability.md` §1
- Análogo 1+1D: `research_program/work_packages/wp4_two_point_theorem.md`
- Requisitos de claim y dirección de garantía: `docs/claim_grammar.md` §1
- Gauge de dilatación (B0): `research_program/puente_3p1/2026-09-12/verify_dilation_gauge.py`
