# B3 — certificado: `n=2` no recupera `phi` localmente en el punto congelado

> **STATUS: `FROZEN / PENDING_INDEPENDENT_AUDIT`.** Se congela y se sube **antes** de
> auditarlo. No se promociona hasta que lo revise otra familia de modelos. Guardarraíles de B3
> intactos: punto congelado, carta congelada, sin búsqueda de curvas, puntos ni parámetros.

**Fecha:** 2026-10-12 · **Verificador:** `verify_b3_certificate.py` →
`verification_b3_certificate.json` · **Especificación:**
`research_program/puente_3p1/2026-09-12/B3_transverse_n2_audit.md` · **Exploración previa:**
`dev/explore_b3_new_representation.py`.

Las cifras abreviadas están redondeadas hacia afuera: las cotas inferiores, hacia abajo; las
superiores, hacia arriba.

```text
M = 128
dphi/dx2            ∈ [0.4571239, 0.4572009]
dphi/dx3            ∈ [−0.0002180, −0.0001548]
drho/dx3            >= +0.0183232        (S_lo(e3) >= +0.0035566)
|drho/dx2|          <= 2.9271            (cota burda: H <= Z)
W23 = dphi_2 drho_3 − dphi_3 drho_2  >=  +0.0077379  > 0
carta: det(dv1, du_out, du_in / dx) = −10133099161583616/8106479329266893 ≠ 0  → rango 3
fastmath_guard: 19 kernels, IR ejecutado (caché vacía), sin flags, mutante detectado, ok
TERMINAL = B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY   (pendiente de auditoría)
```

Con `M = 64` el resultado es el mismo, con menos margen: `drho/dx3 >= +0.0121942` y
`W23 >= +0.0048460`.

---

## 1. Qué establece y qué no

En el punto congelado `lambda*`, el binary64 `path(0.5)` (convención H5 de la compuerta), y en
la carta cociente por el gauge `x = (v1/v0, u_in/u_out, u_in·v1)` con `v0` fijo, **`dphi` no es
paralelo a `drho`**: la componente `(x2, x3)` del producto `dphi ∧ drho` es estrictamente
positiva. Como la carta tiene rango 3 y `drho ≠ 0` (porque `drho/dx3 > 0`), existe una dirección
física `v` con `drho(v) = 0` y `dphi(v) ≠ 0`. Por tanto, **la ley `n=2`, una única escalar
`rho`, no puede reconstruir `phi` localmente en la familia física tridimensional.** Es el
terminal negativo de la especificación de B3, que justifica **proponer** el paso a `n=3`, no
autorizarlo.

**No** establece:
- nada fuera de `lambda*`;
- nada sobre `n=3`;
- ninguna afirmación global. Tampoco dice que `rho` no contenga información sobre `phi`: B2.1 muestra
  que `rho` sí distingue los puntos de la curva congelada. Lo que falla es recuperar `phi` en
  las direcciones transversales.

Respecto al 2026-10-11, B3 pasa de `INCONCLUSIVE_BY_BOUNDS` a este terminal. Es la misma
conclusión que el terminal histórico de 2026-09-12, pero ahora con soporte: el histórico se
retiró porque se apoyaba en un error de signo.

## 2. Cadena

**Por qué basta la componente `(x2, x3)`.** `dphi ≈ (−9e-5, 0.457, −2e-4)` es casi paralelo a
`e2`, de modo que `W23 ≈ 0.457 · drho_3`. Basta certificar `drho_3 > 0` con margen y acotar el
resto.

1. **`drho/dx3`.** La dirección `e3 = dlambda/dx3 = (0, 0, u_out/x3, 1/v1)` mueve solo las dos
   caras `U`, ambas con `v_n > 0`. Es exactamente el caso del certificado de la compuerta, que
   solo construye `S_lo`. Se llama al `run()` auditado de la compuerta **sin modificarlo**, con
   su tabla de velocidades `VN_FR` fijada a los racionales exactos de `e3`. Las caras `V` tienen
   velocidad exactamente 0: `frac_iv(0)` da `(−ε, +ε)` con `ε` subnormal, una contribución
   válida y despreciable. Resultado: `drho_3 >= S_lo(e3)/Z_hi²`.
2. **`dphi`.** `phi = Z_in/(Z_in + Z_out)`, con `Z_in` y `Z_out` las partes de `K` con `U > 0` y
   `U < 0`. Por tanto `dphi = (Z_out dZ_in − Z_in dZ_out)/(Z_in + Z_out)²`. Los `dZ` son
   integrales de `G` sobre las caras que se mueven; la cara `U = 0` no se mueve. `Z_in` y
   `Z_out` salen de `cell_weights` y las integrales de cara de `segment_weights`, ambos de la
   compuerta, y todo se combina en `mpmath.iv`.
3. **`|drho/dx2|`, cota burda.** `e2` solo mueve la cara `U = −u_out`, con `v = −u_out/x2`. Como
   `H <= Z`, se tiene `|S(e2)| <= 2|v| J (Z_hi + B_hi/Z_lo)`, y por tanto `|drho_2| <= 2.9271`.
   Basta porque va multiplicada por `|dphi_3| <= 0.000218`.
4. **`W23 >= dphi_2^lo · drho_3^lo − |dphi_3|^hi · |drho_2|^hi`**, con todos los factores
   positivos en su sentido.
5. **Carta.** El jacobiano es exacto en racionales desde los binary64 de `lambda*`, con las
   filas `(v1, u_out, u_in)`. Su determinante `≠ 0` da rango 3.

## 3. Hipótesis

Las de la compuerta, sin cambios:
- H1, con `V_ε`;
- H2;
- H3, que es teorema en cualquier rectángulo y para cualquier campo de velocidades de caras;
- H4;
- H5, la convención del punto;
- `B15_DEPENDENCIES`.

La definición de `phi` es la de B3 (`verify_b3_transverse_n2.py`, `phi_shape_derivative`).

## 4. Controles

- **`dphi`.** Las envolventes certificadas contienen los valores flotantes de B3
  (`−9.4276e-05`, `0.457162`, `−1.8642e-04`).
- **`Z` y `B_hi`.** Coinciden bit a bit con los de la compuerta, porque no dependen de la
  dirección.
- **Exploración en flotante** (`dev/explore_b3_new_representation.py`, `M = 64`): daba
  `drho/dx3 ∈ [0.0132, 0.0444]`. La cota certificada con `M = 64`, `0.0121942`, queda por debajo,
  como debe.
- **Control de fast-math.** Es el de B2.1: IR de las sobrecargas ejecutadas, caché privada
  vacía y `cache_hits == 0`, aplicado a los 19 kernels de la compuerta, que aquí sí se ejecutan
  todos.

## 5. Qué debe mirar la auditoría

1. Que llamar a `gate.run()` con `VN_FR` sustituido sea legítimo: que `run` solo use `VN_FR`
   para las velocidades y que el caso `v_n = 0` (rama superior con `vn_lo = −ε`) sea válido.
2. La fórmula de `dphi` y los signos de cada término de cara, en particular que la cara `U = 0`
   no se mueve.
3. La cota burda de `|S(e2)|`, en concreto que `I_f <= J_f · Z_hi` porque `H <= Z`.
4. La lógica B3: que una componente del producto distinta de cero, junto con rango 3 y
   `drho ≠ 0`, implique la existencia de `v` con `drho(v) = 0` y `dphi(v) ≠ 0`.
5. El jacobiano de la carta, y que la convención H5 (punto binary64) sea la de la especificación
   de B3.
