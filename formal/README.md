# formal/ — Lean para nachocausal

Lean `v4.31.0`, Mathlib `fabf563` (`v4.31.0`). La configuración se copió de
`~/qca-causal-cones/formal`, que no se modifica; los dos proyectos no comparten código.

| fichero | contenido | estado |
|---|---|---|
| `NachoFormal/Calibration.lean` | B2, lema 1: la desigualdad AM-GM de la calibración (`calib_amgm`), la elección de `Phi'` (`calib_phi`) y las dos juntas (`calib_bound`) | sin `sorry`; solo `propext`, `Classical.choice`, `Quot.sound` |
| `NachoFormal/Monotonicity.lean` | B2, lema 2: curvas causales (componentes monótonas y Lipschitz), longitud `∫ q(UV)√(U'V')`, `length_nonneg`, `concat_length`, `segment_is_causal`, `tau_mono_left`, `tau_mono_right`, `capped_mono` y dos corolarios `capped_tau_mono_*` | sin `sorry`; solo `propext`, `Classical.choice`, `Quot.sound` |

Solo formaliza el álgebra puntual del §2.4 de
`research_program/puente_3p1/2026-10-11/B2_path2_gate_certificate.md`. No formaliza la
integración a lo largo de la curva ni la validez de `c` en el rectángulo. El lema 2 (monotonía
del `sup` respecto a los extremos) está en `Monotonicity.lean`, según `TAREA_LEMA2_CODEX.md`;
las cotas `BddAbove` son hipótesis explícitas (vienen de Cauchy–Schwarz, fuera del encargo) y
la equivalencia con las gráficas `U(V)` de B1.2 queda para el lema 3.

Respecto a la hoja de ruta del 12 de octubre, `calib_phi` añade una hipótesis explícita,
`0 <= F`. Hace falta para que `Phi' >= 0` y se cumple porque `F = q²`.

```sh
lake exe cache get      # Mathlib precompilado
lake build              # debe terminar sin errores ni sorry
lake env lean Axioms.lean
```
