# formal/ — Lean para nachocausal

Lean `v4.31.0`, Mathlib `fabf563` (`v4.31.0`). La configuración se copió de
`~/qca-causal-cones/formal`, que no se modifica; los dos proyectos no comparten código.

| fichero | contenido | estado |
|---|---|---|
| `NachoFormal/Calibration.lean` | B2, lema 1: la desigualdad AM-GM de la calibración (`calib_amgm`), la elección de `Phi'` (`calib_phi`) y las dos juntas (`calib_bound`) | sin `sorry`; solo `propext`, `Classical.choice`, `Quot.sound` |

Solo formaliza el álgebra puntual del §2.4 de
`research_program/puente_3p1/2026-10-11/B2_path2_gate_certificate.md`. No formaliza la
integración a lo largo de la curva, ni la validez de `c` en el rectángulo, ni el lema 2
(monotonía del `sup` respecto a los extremos), que no está autorizado.

Respecto a la hoja de ruta del 12 de octubre, `calib_phi` añade una hipótesis explícita,
`0 <= F`. Hace falta para que `Phi' >= 0` y se cumple porque `F = q²`.

```sh
lake exe cache get      # Mathlib precompilado
lake build              # debe terminar sin errores ni sorry
lake env lean Axioms.lean
```
