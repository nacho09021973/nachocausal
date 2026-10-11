# Sanedrín 2026-10-11 — auditoría del certificado de la compuerta de B2

**Estado del protocolo: `COMPLETED`.** Cinco casas, 3 rondas más residuo y veredicto, 0 turnos
fallidos (57 min):

- CLAUDE OPUS (`claude-opus-5-5`)
- ASTRA (`gpt-6-astra`)
- CIRO (`grok-4.6`)
- ABNER (`deepseek-v4-pro`)
- GEMINI (`gemini-3.8-flash`). Es la variante flash, más débil que la pro que supone el diseño.

**Objeto auditado:** `research_program/puente_3p1/2026-10-11/` en `7909c0e`.

## Veredicto unánime

```text
AUDIT_PASS_CONDITIONAL_B15_DEPENDENCIES   (leído como implicación, no como validez)
```

**La cadena analítica se sostiene:**

- **N1.** Con la regularización `V_ε` de ASTRA. El argumento de «medida nula» del asiento opus
  **fallaba** en toda la cara `V=v0`.
- **N2.** Por monotonía del `sup` en los extremos; el tope `min(pi,·)` la conserva.
- **N3.** La calibración es exacta, con la rama `c<0` correcta.
- **N4.** Los signos de `v_n` son correctos.
- **H3.** Pasa a ser teorema, con el módulo de continuidad de ASTRA.

**La condición son tres hechos que las casas no podían ver.** Debajo, cómo quedaron tras la
auditoría:

| hecho | comprobación posterior (2026-10-11) |
|---|---|
| `E_INV_HI >= 1/e` | `E_INV_HI = 0.36787944117144233 = iv_hi(iv.exp(-1))` (`B1/verify_b1_5_analytic_separation.py:171`); `>= 1/e` comprobado en `mpmath`. Cubierto por la 2.ª ronda de auditoría de B1.5 (§11) |
| `sum_dn <= Σ <= sum_up` | árbol por parejas con un `nextafter` hacia afuera en cada suma (`:114-140`); sustituyó a `math.fsum` en la 2.ª ronda de auditoría de B1.5 |
| dominio de `q_encl`/`G_encl` | nodos efectivos `wt[0] = -1.3510000000000002`, `wt[-1] = 0.6310000000000001`; `s_encl` certifica cada punto por dos desigualdades escalares, válidas para todo `w < 1` (B1.5 §5) |
| (v) reproducción | reejecutado a `M=128`: `S_lo`, `B_hi`, `B'_lo`, `Z`, `Z'`, la cota y el terminal **idénticos bit a bit** al JSON congelado; `fastmath_guard.ok = True` |

**Correcciones pendientes de la nota** (no tocan `S_lo`):

- **H4.** Reescribirla como hipótesis de entorno sobre todo `mpmath.iv` (`cos`, `log`, `pi`).
- **Cauchy–Schwarz integral.** Etiquetarla como lema nuevo; no es B1.2 UB.
- **H1.** Incluir el argumento `ε`.
- **`AU`/`AL`.** Justificar la resta.
- **§1.** Debe afirmar monotonía estricta en un intervalo **no cuantificado** de
  `γ(s) = lambda*_binary64 + s·d`, y no negarla.
- **«Sumas secuenciales».** Corregir: son un árbol por parejas.

**Lo que el certificado NO da**, según las cinco casas:

- la transferencia del signo al punto medio real de la curva;
- un radio cuantificado de monotonía, sin el cual no sirve para B2.1.

**Registro completo:** `sanedrin.log`; bitácora en `sanedrin.log.log`.
