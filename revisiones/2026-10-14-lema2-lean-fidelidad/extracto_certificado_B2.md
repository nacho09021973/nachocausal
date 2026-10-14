# Extracto del certificado de la compuerta de B2

Pasajes literales, sin editar, de `B2_path2_gate_certificate.md` (líneas indicadas).

## Líneas 50-61 (§2, pasos 1 y 2)

## 2. Cadena

1. **Representación** (`dev/B2_NEW_REPRESENTATION_2026-10-11.md`). `Delta_max` (B1.2 §2) es,
   antes del tope `min(pi, ·)`, la separación temporal `τ` de la métrica 2D `q(UV)² dU dV`. La
   justificación, incluida la regularización `V_ε`, está en H1 (§6).
2. **Monotonía respecto a los extremos.** Para `τ` sin tope, si `z` está en el futuro causal de
   `x`, la concatenación da `τ(x,y) >= τ(x,z) + τ(z,y) >= τ(z,y)`. Con `x ∈ P` e `y ∈ Q`:
   `τ(P_top, Q_bot) <= τ(x,y)` si `P_top <= Q_bot`, y `τ(x,y) <= τ(P_bot, Q_top)`. El tope
   `min(pi, ·)` y `p` son no decrecientes, así que ambas desigualdades pasan a `Delta_max` y a
   `h`. **No** se usa ninguna desigualdad triangular inversa aditiva para la cantidad con tope,
   que en general sería falsa. Cada par de celdas se acota con **un** par de esquinas de la
   retícula.

## Líneas 106-107 y 110 (§3, cabecera de la tabla y fila de `p`)

| objeto | tratamiento |
|---|---|
| `p(b) = (1−cos min(b,pi))/2` | tabla certificada de 131 073 nodos en `[0, 3.2]`, `mpmath.iv` (`iv.cos`, `iv.pi`, **fuera** de la capa auditada de B1.5: H4); `p` no decreciente |

## Líneas 162-183 (§6, hipótesis H1)

- **H1. Representación.** B1.2 §2 da `Delta_max = min(pi, sup L[U])`, con el `sup` tomado sobre
  las curvas monótonas `U(V)` absolutamente continuas. Ese `sup` sin tope **es** la separación
  temporal `τ` de `q² dU dV`, porque el `sup` sobre gráficas `U(V)` coincide con el `sup` sobre
  todas las curvas causales futuras (`dU >= 0`, `dV >= 0`). El argumento es la **regularización
  `V_ε`** (ASTRA, ronda 1):
  - Sea una curva causal entre extremos con `ΔV > 0`, parametrizada por `U + V` y reescalada a
    `s ∈ [0, 1]`; sus coordenadas son Lipschitz.
  - Se cambia `V(s)` por `V_ε(s) = (1−ε) V(s) + ε (V_a + ΔV·s)` y se mantiene `U(s)`. La curva
    nueva tiene los mismos extremos, sigue siendo monótona y no sale del rectángulo. Además
    `V_ε' >= ε ΔV`, así que `U` es función absolutamente continua de `V_ε` y la curva es
    admisible en B1.2.
  - Cuando `ε → 0`, la longitud converge a la original: `q(U V_ε)` converge uniformemente en un
    compacto con `UV < 1`, y `sqrt(U' V_ε')` converge casi por doquier con una cota integrable.
  - Si `ΔV = 0`, la longitud es cero (convención degenerada de B1.2 §3).

  Este argumento cubre los **enlaces horizontales** de la cara `V=v0`. `face_h` acota cada
  punto `x` de esa cara mediante `s1` en el sentido futuro y mediante `s0` en el pasado. Ambos
  enlaces tienen `ΔV = 0` y ninguno se puede parametrizar por `V`. En las caras `U = const` los
  enlaces son verticales y admisibles con `U' = 0`. **No se usa ningún argumento de «medida
  nula»**: el que se propuso en la auditoría fallaba en toda la cara `V=v0` y está retirado.
  De H1 salen la cota de la recta (H1b), la monotonía de §2.2 y la calibración. La cota de
  Cauchy–Schwarz integral es un lema aparte (§2.4).
