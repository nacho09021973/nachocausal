# Acta, ronda 2 — vinculación con B2.1 e IR ejecutado

**Casa:** ASTRA. Es la continuación de tu auditoría de B3. Allí diste
`AUDIT_PASS_CONDITIONAL_B21_BINDING_AND_EXECUTED_IR`: los puntos 1–5 se sostenían y quedaban dos
pendientes.

**Pendiente 6a (trazabilidad).** No veías el módulo `verify_b2_1_box_certificate.py`, del que
B3 importa `gate`, `b15` y `executed_ir`. Ahora va adjunto completo. El `executed_ir` que
contiene **no lo ha auditado nadie**: se escribió después de tu auditoría de B2.1, para atender
tu condición «IR ejecutado» de entonces. Esta ronda cubre también esa deuda de B2.1.

Evidencia que no puedes ver tú mismo y que se declara aquí:

```text
$ git log --oneline -- research_program/puente_3p1/2026-10-11/verify_b2_path2_gate_certificate.py
7909c0e B2 gate certificate: drho/dt(t0) >= +0.00705 with directed rounding, frozen pending audit
    (único commit: el verificador de la compuerta no ha cambiado desde el objeto auditado)

prueba negativa (ejecutada el 2026-10-12): se carga la compuerta desde la caché por defecto de
numba y se aplica executed_ir a gate.k_below
    -> RuntimeError: k_below was loaded from a numba cache (1 hits)
```

**Pendiente 6b (MENOR, serialización).** Ya está corregida en el verificador de B3 adjunto: los
extremos se escriben con `b15.iv_lo`/`b15.iv_hi`, que convierten hacia afuera. Además, el
producto final `W23` se calcula ahora en `mpmath.iv`; antes se hacía con escalares `mpf`.

## Lo que se te pide

1. ¿Vincula el módulo B2.1 la compuerta mostrada **sin alterarla**? Comprueba si hay alguna
   sustitución, parche o reasignación de funciones de `gate` además de `VN_FR`, que hace B3.
2. ¿Cumple `executed_ir`, junto con `fastmath_guard` / `guard_all_gate_kernels`, lo que
   exigiste: inspeccionar el código ejecutado, cubrir los cuerpos `prange` y no poder pasar en
   vacío? Busca cualquier manera de que pase sin haber inspeccionado el código real.
3. ¿Queda bien la corrección de 6b?

Para cada punto, da una clasificación y la condición de concesión. Termina con una línea
`Veredicto final B3: …` y otra `Control IR (también para B2.1): …`.
