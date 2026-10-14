# Expectativa previa (escrita por Claude Opus 5.5 ANTES de enviar el encargo)

Fecha: 2026-10-14. Criterios de Claude, no verdades. Claude escribió `Monotonicity.lean` y este
encargo, y puede tener puntos ciegos sobre ambos (por eso la revisión es de otra familia).

Lo que un buen revisor debería encontrar o discutir:

E1. Pares sin relación causal. El paso 2 acota `τ(x,y) <= τ(P_bot, Q_top)` para todo `x ∈ P`,
    `y ∈ Q`. Los teoremas exigen `a ≤ b`; si `x` e `y` no están relacionados, `lengths` es vacío
    y `tau = sSup ∅ = 0` por convenio de Lean. La desigualdad sigue siendo cierta si
    `τ(P_bot, Q_top) >= 0`, pero el fichero no la enuncia: queda por descargar fuera de Lean.
E2. `BddAbove` y no vacío como hipótesis. No vacío se deduce de `a ≤ b` vía `segment_is_causal`
    (redundante); `BddAbove` es la cota de Cauchy–Schwarz, declarada fuera del encargo. Sin ella,
    `sSup` de un conjunto no acotado vale 0 en Lean y el teorema no diría nada útil. ¿Lo ve?
E3. La composición de las dos desigualdades necesita la monotonía en un extremo y luego en el
    otro, con no vacío y `BddAbove` en el punto intermedio (`τ(P_top,Q_bot) <= τ(x,Q_bot) <=
    τ(x,y)`). No hay un teorema que lo haga en un paso.
E4. Dominio: el certificado tiene `q` solo en `UV < 1` (tablas en `w ∈ [-1.351, 0.631]`); Lean
    toma `q : ℝ → ℝ` continua y no negativa en todo `ℝ`. Hace falta extender `q`, y como las
    curvas monótonas no salen del rectángulo de sus extremos, la extensión no cambia `τ` si el
    rectángulo está en el dominio. Salvedad de enunciado, no error.
E5. La clase de curvas es la de H1 (parametrización Lipschitz), no la de gráficas `U(V)` de B1.2;
    `Delta_max = τ` es el lema 3, fuera del alcance. El lema 2 en Lean no prueba nada sobre
    `Delta_max` sin el lema 3.
E6. `capped_mono` solo en `[0, ∞)` y los corolarios exigen `0 <= τ(a,b)`: con `q >= 0` y `a ≤ b`
    se tiene, pero no está enunciado como lema.
E7. La desigualdad del paso 2 `τ(x,y) >= τ(x,z) + τ(z,y)` (triangular inversa) no se formaliza;
    solo su consecuencia `>= τ(z,y)` vía un segmento. Suficiente para el uso; no es lo mismo.

Puntuación: cuántos de E1-E7 detecta, si sus objeciones son correctas al comprobarlas contra el
fichero, y objeciones válidas no previstas (a favor). Errores matemáticos, afirmaciones sobre
Mathlib que no se sostienen o literatura inventada, en contra.
