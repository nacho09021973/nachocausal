# B4.1 — Certificación de rango del Jacobiano `n=3`

> **STATUS: `FROZEN_POINT / FIXED_CHART / ALL_MINORS_AUDITED / NO_SEARCH`.**

Se audita el Jacobiano `J=Dm(lambda*)` completo, sin descartar filas. El chart físico y los cuatro
momentos son exactamente los de B4. Los cuatro menores `3x3` se calculan y se compara además la
formulación espectral `lambda_min(J^T J)`.

Para acondicionamiento se declara antes del resultado el reescalado fijo

```text
R=diag(1,10000,10000,10000), C=I_3,
J_tilde=R J C.
```

Como `R` y `C` son invertibles, esto no altera el rango.

## Terminales

```text
B4_STRONG_POSITIVE          algún menor certificado excluye cero, o
                             sigma_min(J_tilde) tiene cota inferior positiva;
B4_INCONCLUSIVE_BY_BOUNDS   ninguna envolvente disponible decide;
B4_NEGATIVE_EXACT_RANK      sólo con dependencia exacta/rango menor demostrado.
```

Un determinante numéricamente pequeño no es evidencia de rango menor.

## Primera auditoría

La evaluación disponible de B4 produce valores centrales y todos los menores, pero todavía no
una aritmética intervalar rigurosa de los momentos ni de sus derivadas. Por ello el resultado se
mantiene en `B4_INCONCLUSIVE_BY_BOUNDS`, aunque los números centrales y la singularidad mínima se
reportan para guiar una futura certificación. No se cambia el punto, el chart ni la familia.

Los valores centrales obtenidos son

```text
det(omit row 0) = -1.0473e-15
det(omit row 1) =  2.4217e-13
det(omit row 2) = -5.3893e-13
det(omit row 3) = -8.2623e-13
sigma_min(J_tilde) = 1.1370e-03
TERMINAL = B4_INCONCLUSIVE_BY_BOUNDS
```

La positividad de `sigma_min` aquí es sólo central/numerical; no se eleva a certificado sin
envolvente rigurosa.

**Artefacto:** `verification_b4_1_rank_certification.json`.
