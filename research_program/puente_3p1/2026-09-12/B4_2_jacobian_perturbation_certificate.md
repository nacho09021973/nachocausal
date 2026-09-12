# B4.2 — Certificado de perturbación del Jacobiano congelado

> **STATUS: `FROZEN_SCALING / DETERMINISTIC_ERROR_AUDIT / NO_RESCALING`.**

Se conserva exactamente el punto, chart y reescalado de B4.1:

```text
R=diag(1,10000,10000,10000), C=I_3,
sigma_min(J_tilde_0)=1.1370e-3.
```

El objetivo es obtener cotas rigurosas entrada a entrada para
`J_tilde=J_tilde_0+E` y verificar

```text
||E||_F < 1.1370e-3.
```

La auditoría preliminar compara órdenes y pasos deterministas fijados antes del resultado. Estas
comparaciones sirven para detectar estabilidad, pero no son por sí mismas aritmética intervalar
rigurosa; por ello nunca pueden producir un terminal positivo si no se acompañan de una cota
formal.

## Terminales

```text
B4_STRONG_POSITIVE          ||E||_F < sigma_min(J_tilde_0) certificado;
B4_INCONCLUSIVE_BY_BOUNDS   no existe aún una envolvente formal suficiente.
```

No se reajusta el escalado, no se persiguen determinantes y no se cambia ningún dato físico.

## Resultado

La auditoría con órdenes `(10,14)` y pasos `10^-3, 5*10^-4` da una dispersión Frobenius
observada de

```text
||E||_F (observed spread) = 5.4022e-02
sigma_min(J_tilde_0)       = 1.1370e-03
formal_interval_enclosure  = FALSE
TERMINAL = B4_INCONCLUSIVE_BY_BOUNDS
```

La dispersión de convergencia no es un certificado de error, pero muestra que la implementación
actual está muy lejos de la tolerancia requerida. No se interpreta como rango menor que tres ni
como refutación de `B4_STRONG_POSITIVE`.

**Artefacto:** `verification_b4_2_perturbation_certificate.json`.
