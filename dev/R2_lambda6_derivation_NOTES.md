# R2 — derivación del exponente `κ ~ λ⁶` (notas de exploración, día 1)

```text
ESTADO: EXPONENTE DERIVADO Y VERIFICADO / PREFACTOR ABIERTO [UNVERIFIED]
ALCANCE: R2 de docs/program_reopening_note_2026-07-31.md
NATURALEZA: dev/ — exploración, no confirmación. No enmienda ningún work package.
```

Ítem R2: `wp4_fisher_localization_floor.md` §5a registra `κ ~ λ⁶` como **ajuste empírico**
(exponente 5.917 / 5.988) y declara que su derivación analítica —"a near-horizon/Rindler
expansion of `I(τ)` is a plausible route"— **no fue intentada**. Estas notas la intentan.

## 1. Resultado

`κ = V·I ~ λ⁶` deja de ser un ajuste: es `2 + 2·2`, con mecanismo identificado.

**`V ~ λ²`.** `det g_τ = −1` (§4), luego la medida de muestreo es Lebesgue `dv dr`; ambas
extensiones de la caja van como λ. Razón numérica entre λ=0.1 y λ=0.05: **4.0000**.

**`I ~ λ⁴`.** Con `r = τ(1+x)`, `ε = v/(2τ)`, `u = −Ũ/e`, la densidad conjunta en coordenadas
nulas es *exactamente*

```
log h = const(τ) + ε − x − ln(1+x),    x = W_Lambert(u·e^ε)
```

Como `x` depende solo del producto `u·e^ε`, se tiene `log h = const + ε + Φ(s+ε)` con `s = ln u`.
Desarrollando en ε, la parte **no separable** —la única que la cópula no borra— es

```
η = ε·Φ′(s) + O(ε²),   Φ′ = −x(2+x)/(1+x)² = −2x + 3x² + …
⇒ η_bilineal = −2uε = Ũ·v/(e·τ) = O(λ²)
```

Score `O(λ²)` ⇒ Fisher `O(λ⁴)`. **La cópula es ciega al espacio plano; lo primero que ve cerca
del horizonte es curvatura × área del parche, `~λ²`.**

## 2. Verificación numérica

Contra `research_program/work_packages/wp4_kappa_numeric_reference.py`, sin modificarlo.

| Cantidad | Predicción | Numérica | Script |
|---|---|---|---|
| `I = (dK/dτ)²/144` | estructura exacta | **coincide a 0.5 %** en λ=0.2, 0.1, 0.05 | `04` |
| `K(τ=1)` vs cópula real | `ΔŨ·Δv/(eτ)` | ratio 0.983 → 0.988 → 0.994 → **0.998** al bajar λ | `03` |
| `dK/dτ / λ²` | plano | 0.1341, 0.1346, 0.1348 | `04` |
| `K/λ²` | `2ab = 0.18` | 0.1789 | `01` |
| régimen de validez | falla en diamantes gordos | forma A: ratio 4e-4; formas finas: → 0.0312 | `02` |

`dK/dτ ∝ λ²` está medido sobre la cópula real en una década de λ. **El exponente no depende del
prefactor.**

## 3. El hueco: el prefactor

Empíricamente `I = (dK/dτ)²/144` con `dK/dτ → +0.1347 λ²`. Mi expresión analítica a orden
dominante da `dK_an/dτ → −0.7616 λ²`: **ratio −5.62, −5.63, −5.65** (deriva hacia ~5.657 = 4√2,
no establecido), **con cambio de signo**.

**Descartado como causa** (comprobado, no supuesto):

- *Convención de Fisher.* `hellinger_sq` no lleva el ½ y el script usa `I = 4H²/δ²`, lo que da
  exactamente `I = E[(∂_τ log c)²]`. Autoconsistente.
- *Centrado doble y expansión de Lambert.* `K(1)` ajustado contra la cópula real converge a la
  expresión analítica (0.998 a λ=0.05). Ambos correctos.
- *Paso δ demasiado grande.* El barrido escala `deltas=(0.04λ, 0.02λ, 0.01λ)`; para λ=0.05,
  `δ/2 = 0.001` frente a media anchura 0.015. Régimen sano.

**Causa localizada.** La expansión es correcta *puntualmente en τ=1* pero **no uniforme en τ**:

```
   tau        K_fit          K_an
0.9940   1.790432e-03   1.834072e-03
1.0000   1.798529e-03   1.787807e-03      <- se cruzan aquí
1.0060   1.806593e-03   1.743018e-03
```

`K_fit` **crece** con τ; `K_an` **decrece**. Coinciden en τ=1 y divergen en la derivada. Razón: a
esquinas fijas el diamante está a distancia `~λ` del horizonte, luego la escala natural de
variación en τ es `δτ ~ λ`, no `δτ ~ 1`. Expandir en `δτ ≪ 1` es el orden equivocado.

## 4. Ruta para cerrarlo

Asintótica emparejada: introducir `σ := (τ−1)/λ` y rehacer la expansión a **σ fijo**, obteniendo
`K(σ)` uniforme en la región donde el horizonte está dentro o cerca del borde de la caja. Su
derivada es la buena. No es un parche: es el orden correcto del problema.

## 5. Etiquetas

```text
EXPONENTE_LAMBDA6      = DERIVED_IN_THIS_PROJECT / NUMERICALLY_CROSS_CHECKED
PREFACTOR              = OPEN / [UNVERIFIED]
FACTOR_32_ES_CANONICO  = NO (descartado: no es convención de Fisher ni de centrado)
WORK_PACKAGE_TOCADO    = NINGUNO
SEMILLAS               = 0 · SIMULACIÓN = NINGUNA · SELLO = INTACTO
```

Nada de esto entra en `wp4_fisher_localization_floor.md` §5a/§6 hasta que el prefactor cierre o
se declare abierto en el texto del anexo, conforme a
`docs/program_reopening_note_2026-07-31.md` §4.4.
