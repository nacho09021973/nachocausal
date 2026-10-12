# Acta, ronda 3 — completitud del control de IR

**Casa:** ASTRA. Continúa tus rondas 1 y 2. En la ronda 2 diste
`AUDIT_PASS_CONDITIONAL_IR_COMPLETENESS` para B3 y `REQUIERE_CORRECCIÓN_DE_COBERTURA_COMPLETA`
para el control de IR, también para B2.1, con cuatro huecos:
1. B3 no exigía cuerpos `prange`;
2. `getattr(..., "_linking_libraries", ())` toleraba perder enlaces sin avisar;
3. el control comprobaba que había algún cuerpo, no que estuvieran todos;
4. la `define` se identificaba por el nombre Python, no por el símbolo exacto.

**Cambios** (adjuntos: el módulo B2.1 completo y el verificador de B3):
- `closure_check`: todo símbolo de código de numba **referenciado** en cualquier módulo del
  conjunto inspeccionado (llamado, declarado o tomado por dirección) tiene que estar **definido**
  en él. Se excluyen `_ZN08NumbaEnv*`, que son datos, y las cadenas `.const`. Además debe estar
  definido el nombre mangled exacto de cada sobrecarga ejecutada (`ov.fndesc.mangled_name`).
- `_linking_libraries` se lee directamente: si falta, lanza `AttributeError`.
- `guard_kernels` es un solo control, común a B2.1 (sus 19 kernels usados) y B3 (los 19 de la
  compuerta). Exige cuerpos `prange` reales (`_ZN…__numba_parfor_gufunc_0x…`) en cada kernel
  paralelo.

**Al implementar la clausura apareció un error mío, que se declara:** la primera versión solo
miraba los `declare`. Un cuerpo `prange` se llama directamente dentro del mismo módulo y nunca
se declara, así que esa versión no detectaba su eliminación. La prueba negativa (2) lo puso de
manifiesto, y se cambió a «todas las referencias».

Salidas de `dev/explore_ir_guard_negative_tests.py` (adjunto), ejecutado el 2026-10-12:

```text
positive: ok = True | parfor bodies {'calibration_point_tables': 1, 'ub_table': 2, 'b_hi_sum': 2, 'lb_rows_xy': 2}
(2) body removed : caught -- IR closure fails: referenced-not-defined ['_ZN13_3cdynamic_3e36__numba_parfor_gufunc_0x7ea
(3) required absent : caught -- IR closure fails: referenced-not-defined [], required-not-defined ['_ZN3fooB3v1E']
(1) cached kernel : caught -- k_below was loaded from a numba cache (1 hits)
```

Reejecución de B3 con el control nuevo: los mismos números, y
`fastmath_guard.ok = True`, con 19 kernels, cuerpos `prange` en los 4 paralelos y sin flags.

## Lo que se te pide

1. ¿Cierra la clausura los cuatro huecos? Busca un caso en que un cuerpo de código ejecutado
   quede **fuera** del conjunto inspeccionado y aun así el control pase.
2. ¿Son correctas las exclusiones (`NumbaEnv`, `.const`) y el criterio de «cuerpo real»?
3. ¿Prueban las tres pruebas negativas lo que dicen?

Termina con `Veredicto final B3: …` y `Control IR (también para B2.1): …`.
