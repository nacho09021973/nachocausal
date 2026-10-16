# Evaluación de las revisiones de §8–§9 (DeepSeek y Grok), 2026-10-16

Evaluador: Claude, autor de §8–§9; no es independiente. Informes: `informe_deepseek.md`
(deepseek-v4-pro, finish_reason=stop) y `informe_grok.md` (grok-4.7). Herramientas
`14929eb`. Ninguna de las dos entradas identificaba al autor.

Veredicto de los dos: **correcto con salvedades enumeradas**. Ningún fallo matemático.

| Afirmación | DeepSeek | Grok |
|---|---|---|
| D (Poisson) | correcta; pide escribir la continuidad de Ṡ | correcta; ídem |
| E (cota inferior de Fisher) | correcta | correcta; justifica 0 < p < 1 en K |
| F (cota superior) | correcta | correcta (n ≥ 2) |
| G (monotonía) | correcta; ningún contraejemplo; pide el detalle de la semicontinuidad | correcta; ningún contraejemplo; da el argumento de la semicontinuidad y el factor de c |
| H (tasa) | correcta como tasa; constante Poisson no literal | correcta como tasa; cota inferior solo para n ≥ n_0; constante Poisson no literal y estimador sin definir para N < 2 |

Salvedades incorporadas en `wp6_uniform_n_horizon_quotient.md`:
1. D: continuidad de Ṡ por la suma de segundas derivadas.
2. G: semicontinuidad inferior de c, con el argumento de Grok (Fatou puntual; el factor
   (1 − Δφ/T)_+ se anula cerca del horizonte).
3. H: cota inferior explícita 1/(8√(nJ̄)) para n ≥ n_0 = 1/(J̄|K|²).
4. H con Poisson: tasa Λ^{−1/2} con la constante 2√2 sup√(p(1−p))/m más
   |K| e^{−Λ}(1+Λ), y τ̂ fijo cuando N < 2. Comprobado: N^{−1/2} ≤ √2/√(N+1) para N ≥ 1,
   E[(N+1)^{−1}] = (1 − e^{−Λ})/Λ ≤ 1/Λ, y Jensen.

Frente a `expectativa_previa.md`: acertada en los tres puntos señalados (G esbozado,
D(2) sin escribir y el caso N < 2 en Poisson). La cota inferior sólo para n ≥ n_0 no la
anticipé.
