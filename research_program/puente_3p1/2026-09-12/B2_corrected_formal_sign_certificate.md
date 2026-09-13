# B2 — certificado formal del signo

## Resultado

La ruta de certificación barata se auditó y se detiene por la `stop rule` preregistrada:

```text
TERMINAL = B2_CORRECTED_CERTIFICATION_ROUTE_TOO_COSTLY
```

La evaluación corregida sigue dando una banda numérica negativa, pero no se promueve a prueba.

## Qué se intentó certificar

Se congelaron la curva, `t0=1/2`, el kernel físico corregido y las cotas angulares de B1.4. El
certificado debía construir, mediante partición finita de cajas, enclosures para exactamente

```text
Z, Z', B, B'
```

y propagarlos en

```text
rho' = B'/Z^2 - 2 (B/Z^2) Z'/Z.
```

El terminal positivo habría requerido únicamente

```text
formal_upper_bound(drho_dt) < 0
```

En `t0`, el dominio analítico es `U in [-1.5,0.7]`, `V in [0.35,0.9]` y por tanto
`UV in [-1.35,0.63]`. En ese intervalo `q_true` es creciente en `UV`, `G` es creciente hasta
`UV=0` y decreciente después, y la probabilidad angular es creciente en el presupuesto. Una
partición candidata de `M=16` produciría `256` cajas para `Z`, `64` términos de frontera para
`Z'`, `65536` cajas para `B` y `16384` celdas de frontera para `B'`.

## Motivo de la parada

El entorno dispone de aritmética intervalar puntual (`mpmath.iv`), pero su backend no implementa
`LambertW` para evaluar de forma intervalar el `s` corregido. Tampoco hay una capa validada de suma
de cajas con redondeo hacia afuera que certifique las cuatro integrales. Construir ambas capas sería
infraestructura de cuadratura comparable a la ya aparcada en B4, por lo que se activa la stop rule
y no se abre ese proyecto auxiliar.

No se ejecutan B3 ni B4, no se modifica la estimación central y no se añaden puntos ni ajustes.

**Artefacto:** `verification_b2_formal_sign_certificate.json`.
