# Acta — auditoría del certificado de B3

**Fecha:** 2026-10-12. **Convoca:** el PI. **Casa:** ASTRA (sellada, una sola intervención).

Se te pide **auditar**, no proponer trabajo nuevo. El objeto está congelado y subido **antes**
de esta auditoría (`1f7286d`). Tu trabajo es intentar **romperlo**. Un acuerdo fácil no tiene
valor.

No tienes herramientas. Solo cuentan esta acta y los adjuntos:

1. `B3_certificate.md` — la nota, con la lista de auditoría en su §5.
2. `verify_b3_certificate.py` — el verificador.
3. `verification_b3_certificate.json` — su salida.
4. `B3_transverse_n2_audit.md` — la especificación de B3: la carta, los terminales y la
   definición de `phi`. Su cuerpo es histórico.
5. `verify_b3_transverse_n2.py` — el verificador histórico, que define `phi_shape_derivative`.
6. `verify_b2_path2_gate_certificate.py` — el verificador de la compuerta, cuyo `run()` se llama
   sin cambios.
7. `B2_path2_gate_certificate.md` — la nota de la compuerta, ya auditada y promocionada.

## 1. Qué se afirma

En el punto congelado y en la carta de B3, la componente `(x2, x3)` del producto
`dphi ∧ drho` es `>= +0.0077379 > 0`. Junto con el rango 3 de la carta y `drho ≠ 0`, eso da
`B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY`.

## 2. Lo que no se reabre

La cadena de la compuerta: H1–H5, la monotonía del `sup`, la calibración y Cauchy–Schwarz
integral, la capa escalar de B1.5 y sus kernels. Aquí se audita **el uso** de esa maquinaria
para B3 y las piezas nuevas: `dphi`, la cota burda de `|drho_2|` y la lógica del producto.

## 3. Lo que se te pide

Responde los cinco puntos de §5 de la nota. Para cada hallazgo, da una clasificación
(`SE_SOSTIENE`, `MENOR`, `REQUIERE_CORRECCIÓN` o `INVALIDA`) y la condición mínima de
concesión. Añade además:

6. **Algo que la nota no pregunta.** Busca cualquier pieza que pueda hacer que `W23 > 0` sea
   cierto en el código y falso en la matemática.

**Veredictos posibles:** `AUDIT_PASS`, `AUDIT_PASS_CONDITIONAL_<COND>`,
`AUDIT_REQUIRES_MINOR_FIX`, `AUDIT_FAIL`.
