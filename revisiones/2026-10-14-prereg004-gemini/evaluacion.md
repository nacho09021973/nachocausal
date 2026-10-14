# Evaluación de la revisión O8 del prereg-004 (gemini-4-argon, thinkingLevel=high)

Fecha: 2026-10-14. Evaluador: Claude Opus 5.5, que escribió buena parte del paquete y del borrador
(no es evaluación independiente). Herramienta: revision-ciega @ ~/herramientas c12c10e. Documentos
en 5afb33d (borrador, thresholds.py, validate.py, tests 2p1) y 2d71bc0/c16fb12 (resto). Una ronda.

**Veredicto del revisor:** NO LISTO. Tras comprobarlo contra el código, la mayoría de los defectos
son reales. Se marca cada uno: **comprobado** (leído o ejecutado aquí), **parcial** o **no se
sostiene**.

## Defectos reales

| # | defecto | estado | comprobación |
|---|---|---|---|
| D1 | `ii_convergence_slack` pasa en vacío si una mediana es NaN (`b > a + s` es False con NaN); `loc_inconclusive = iqr > θ` es False con IQR NaN | **comprobado** | `validate.py` `verdict_from_levels` y `summarise_level`: comparaciones `>` con valores que pueden ser `nan` (`widths` vacío ⇒ `median = nan`). Error de código |
| D2 | un nivel no primario con < 18 semillas válidas da `FAIL`, no `INCONCLUSIVE` | **comprobado** | `verdict_from_levels`: `levels[ρ].get("significant", False)` y `slack_ok = False` si `status != "scored"`; solo la primaria devuelve `INCONCLUSIVE`. El §9 dice que las inválidas cuentan para INCONCLUSIVE |
| D3 | `validate.run(label=validation_004, write=False)` pasa todos los candados y no deja rastro | **comprobado** | `run()`: los candados no miran `write` |
| D4 | `python -m nachocausal2p1.validate` (§9) no hace nada: no hay `__main__` | **comprobado** | `grep __main__`: solo en `dry_run.py` |
| D5 | la semilla del sorteo (O1) fijada antes de C1 permite calcular las 20 semillas vírgenes antes de congelar | **comprobado** (lógica) | receta en `thresholds.py`; `check_seed` impide ejecutarlas con este código, pero no calcularlas. Se arregla derivando la semilla de un artefacto posterior a C1 (p. ej. el SHA del commit de C1) |
| D6 | el registro de progreso (O4) revela el FAIL de (i) o (iv) durante la corrida (`abstained_BH`, `abstained_MINK`) | **comprobado** | `PROGRESS_FIELDS`; era G1 de la expectativa |
| D7 | los niveles de ρ comparten flujo aleatorio: los primeros `n(32)` valores de `t` en ρ=63 son los de ρ=32, y los siguientes son los uniformes de `r` de ρ=32 | **comprobado ejecutando** `generator.sprinkle` con la semilla 7_000_100 (inspección, sin artefacto): `t63[:n32] == t32` y `t63[n32:]/T == u_r32[:2650]`, ambos True | `validate.generate` usa `default_rng(seed)` sin ρ. Igual en 1+1 (`nachocausal/generator.py:46`). Cada nivel es un sembrado de Poisson correcto; lo que no hay es independencia entre niveles, y no está declarado |
| D8 | mediana, IQR y `boundary_r_std` solo sobre horquillas «limpias» (`width >= 0`): se descartan las invertidas | **comprobado** | `summarise_level`; igual que 1+1 (`nachocausal/validate.py:136`). Selección heredada y no declarada |
| D9 | faltan tests de fallo aislado para (i) por abstenciones, holgura F, (iii) e IQR | **comprobado** | ningún test los provoca (`grep` en los dos ficheros de tests) |
| D10 | §7 dice que (i) se reduce a «ninguna abstención BH», pero la regla tolera 2 | **comprobado** | `docs/preregistration_004_draft.md:192` frente a `BH_ABSTAIN_FAIL = 3` |
| D11 | `n_minimal > 256` o un fallo de Guard-v abortan sin escribir veredicto (estado indistinguible de una caída) | **comprobado**, por diseño | documentado en `validate.py` y en el auditor 043; falta un desenlace escrito |
| D12 | (i) se reduce a contar aperturas de la compuerta: p = 2^-m sin depender de la magnitud | **comprobado** (G3) | `signflip_perm_p` exacto para n ≤ 20; el §7 ya lo dice a medias |

## Parciales o que no se sostienen

- **Hilos de BLAS sin fijar** (`A @ A` en float32): no afecta al resultado. Las sumas son enteras
  ≤ N ≈ 10⁴ < 2²⁴, exactas en float32 con cualquier orden; solo se compara con 0.5.
- **«`dry_run` no existe»**: existe como módulo `nachocausal2p1/dry_run.py` (no se le envió).
- **SHA de `thresholds.py` desfasado en §3**: el borrador ya dice que se retoma en C1.
- **Semillas de prereg-001/002 sin comprobar**: la guarda exige `VIRGIN_BAND = 8_000_000..8_999_999`,
  que no las contiene.
- **Bin(18, 0.35) ≥ 9 = 16,3 %**: es 13,9 % (`scipy.stats.binom`). El argumento (suelo 0,5 con
  poca potencia) se mantiene.
- **Puntuación en RAM antes del final contra la regla de caídas**: lectura estricta de «scoring
  output»; en memoria no es salida. Discutible; D6 es el problema real.
- **`v_order_only` nunca puede ser False en el fichero**: cierto, por diseño (Guard-v aborta);
  es D11.

## Contra la expectativa previa

G1 sí (D6). G2 parcial (habla de SIMD/BLAS, no del determinismo de una corrida a otra). G3 sí
(D12). G4 sí y más fuerte (D7: acoplamiento entre coordenadas, no solo semillas comunes). G5 sí
(D8). G6 no. G7 no tal cual, pero encuentra D3, más grave.

No previstos y válidos: D1, D2, D3, D4, D5, D9, D10, D11.

## Lectura

Las decisiones O1-O7 siguen tomadas, pero la revisión reabre O1 (D5) y O4 (D6). Hay errores de
código que ningún test cubría (D1, D3) y un desajuste entre texto y código en el desenlace
INCONCLUSIVE (D2). D7 y D8 vienen del 1+1 sellado: hay que declararlos o cambiarlos, y decidirlo
corresponde al PI. **El prereg-004 no puede congelarse así.**
