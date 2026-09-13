# B2 — kernel corregido y camino físico congelado

## Alcance

Este artefacto ejecuta únicamente `B2_CORRECTED_KERNEL_LOCAL_IDENTIFIABILITY` sobre la curva

```text
lambda(t)=(1-t)lambda0+t lambda1,    t0=1/2
lambda0=(0.5,1.0,1.0,0.5,0.1)
lambda1=(0.2,0.8,2.0,0.9,0.1)
```

No añade puntos, no busca `t0`, no ajusta parámetros y no reabre B1, B3 ni B4.

## Kernel y transporte

Se usa el kernel físico corregido

```text
q(uv)=2 exp(-s(uv)/2) / s(uv)^(3/2),
```

en las cotas angulares. La derivada de `rho=B/A^2` se obtiene por transporte de las cuatro
caras del rectángulo, no por diferencias finitas. Las cotas inferior y superior de cada término
angular son las de B1.4: familia fija de 19 caminos de dos tramos y cota Cauchy–Schwarz con
`q_max(V)` punto a punto.

## Garantía numérica y terminal

La estabilidad entre órdenes de Gauss 10, 14 y 18 se conserva como evidencia diagnóstica, pero no
se presenta como cota matemática del resto. El JSON contiene explícitamente el estado
`MISSING_FORMAL_REMAINDER_BOUND`; por ello el terminal fuerte sólo puede ser

```text
B2_CORRECTED_POSITIVE
```

cuando se añada una cota de resto con redondeo hacia afuera o una estimación analítica válida para
la cuadratura. Mientras tanto, aunque la banda numérica excluya cero, el terminal preregistrado es

```text
B2_CORRECTED_INCONCLUSIVE_BY_BOUNDS
```

`B2_CORRECTED_ZERO` no se emite por una banda que contenga cero: requiere probar exactamente
`rho_true'(t0)=0`.

**Artefactos:** `verify_b2_corrected_kernel.py` y `verification_b2_corrected_kernel.json`.
