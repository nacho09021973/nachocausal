# Acta — auditoría del certificado por cajas de B2.1

**Fecha:** 2026-10-12. **Convoca:** el PI. **Casa:** ASTRA (sellada, una sola intervención).

Se te pide **auditar**, no proponer trabajo nuevo. El objeto está congelado y subido **antes**
de esta auditoría (`f1e030f`). Tu trabajo es intentar **romperlo**: busca una inclusión falsa,
un vértice mal elegido, una cota en la dirección equivocada o un caso que no esté cubierto. Un
acuerdo fácil no tiene valor. En este proyecto, de once errores, diez los encontró una familia
de modelos distinta de la que escribió el código.

No tienes herramientas. Solo cuentan esta acta y los adjuntos:

1. `B2_1_box_certificate.md` — la nota: qué afirma, la cadena (§3), la aritmética, las
   hipótesis, los controles y la lista de auditoría (§7).
2. `verify_b2_1_box_certificate.py` — el verificador de cajas, completo.
3. `verify_b2_path2_gate_certificate.py` — el verificador de la compuerta. B2.1 importa sus
   kernels **sin cambios**: `cell_weights`, `calibration_point_tables`, `cs_prefix`,
   `ub_table`, `b_hi_sum`, `g_range`, `rect_w`, `tiling` y las tablas.
4. `B2_path2_gate_certificate.md` — la nota de la compuerta, ya auditada y promocionada. Da
   H1–H5 y la monotonía del `sup` respecto a los extremos (§2.2).
5. `resumen_json.json` — la salida del verificador sin la lista de las 100 cajas.

## 1. Qué se afirma

Para todo `t ∈ [0.45, 0.55]`, en las dos lecturas de la curva (extremos binary64 y decimal),
`drho/dt(t) >= +0.0066481 > 0`. Para ello se parte el intervalo en 100 cajas y en cada una se
acota `S` por debajo, de forma uniforme para todo `lambda` de la caja, con un rectángulo
interior `K_in` y uno exterior `K_out`, y con las caras ensanchadas en franjas. Terminal:
`B2.1_POSITIVE_DERIVATIVE`.

## 2. Lo que no se reabre

La auditoría de la compuerta, con pase condicional y la condición verificada, cubre:
- la representación (H1, con `V_ε`);
- la monotonía del `sup` respecto a los extremos;
- la calibración y Cauchy–Schwarz integral dentro de `ub_table`;
- H3 como teorema;
- la capa escalar de B1.5;
- los kernels importados.

Aquí se audita el **ensamblado por cajas** y los **tres kernels nuevos** (`lb_rows_xy`,
`strip_weights`, `face_h_cells`).

## 3. Lo que se te pide

Responde los cinco puntos de §7 de la nota. Para cada hallazgo, indica una clasificación
(`SE_SOSTIENE`, `MENOR`, `REQUIERE_CORRECCIÓN` o `INVALIDA`) y la condición mínima de concesión.
Además:

6. **El control de fast-math nuevo** (`fresh_ir`): ¿puede pasar en vacío de alguna otra forma?
7. **Algo que la nota no pregunta.** ¿Hay alguna pieza de `run_box` que use un valor de una
   `lambda` concreta como si valiera para toda la caja?

**Veredictos posibles:** `AUDIT_PASS`, `AUDIT_PASS_CONDITIONAL_<COND>`,
`AUDIT_REQUIRES_MINOR_FIX`, `AUDIT_FAIL`.
