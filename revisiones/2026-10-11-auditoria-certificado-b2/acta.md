# Acta — auditoría del certificado de la compuerta de B2

**Fecha:** 2026-10-11. **Convoca:** el PI.

Se os pide **auditar**, no decidir el siguiente paso ni proponer trabajo nuevo. El objeto está
congelado y subido **antes** de esta auditoría, a propósito. Vuestro trabajo es intentar
**romperlo**. Un acuerdo fácil no tiene valor: en este proyecto, de once errores, diez los
encontró una familia de modelos distinta de la que escribió el código, y ninguno se encontró
releyendo.

No tenéis herramientas. Solo cuentan esta acta y los adjuntos:

1. `B2_path2_gate_certificate.md` — la nota del certificado: cadena, aritmética, resultados,
   hipótesis (§6) y lista de auditoría (§7).
2. `verify_b2_path2_gate_certificate.py` — el verificador completo.
3. `B2_NEW_REPRESENTATION_2026-10-11.md` — de dónde sale la representación nueva.
4. `B1_2_angular_causal_reach.md` — la definición de `Delta_max` (§2) y las cotas LB/UB (§3).
5. `B2_PROMOTION_RULE_AMENDMENT_2026-10-11.md` — la regla de promoción, firmada por el PI.
6. `B2_2_SIGN_BUG_2026-10-11.md` — el error de signo que motivó la enmienda y fija las `v_n`.

---

## 1. Qué afirma el certificado

En el punto congelado `lambda* = lambda(0.5)` del camino `lambda(t) = (1-t)lambda0 + t lambda1`,
y a lo largo de `d = lambda1 − lambda0`:

```text
S_lo = +0.0013679   para  S = B' − 2 (Z'/Z) B
drho/dt(t0) >= +0.00705,   enclosure [0.00704746, +inf)
TERMINAL = B2_CORRECTED_POSITIVE   (regla: 0 no está en la envolvente de drho/dt)
```

con `rho = B/Z²`, `B = ∫∫_{K×K} w(x) w(y) h(x,y)`, `w = G(UV)`, `h = p(Delta_max)`,
`p(b) = (1 − cos min(b, pi))/2`, y `B' = 2 ∫_{∂K} w v_n H`, `H(x) = ∫_K w(y) h(x,y) dy`.

## 2. Las piezas nuevas, que nadie ha auditado

**(N1) Representación.** `Delta_max(x,y) = min(pi, sup_U ∫ q(U(V)V) sqrt(U'(V)) dV)` sobre
`U` monótonas (B1.2 §2) se lee como la separación temporal de la métrica 2D
`ds² = F(w) dU dV`, con `F = q²` y `w = UV`.

**(N2) Desigualdad triangular inversa.** Si `x ∈ P` e `y ∈ Q` (celdas de una retícula):
`P_top <= Q_bot ⇒ Delta(x,y) >= Delta(P_top, Q_bot)`, y
`P_bot <= Q_top ⇒ Delta(x,y) <= Delta(P_bot, Q_top)`.
Así cada par de celdas se acota con un solo par de esquinas.

**(N3) Calibración.** En `(w, nu) = (UV, ln V)`, con `a = nu' >= 0` y `b = w' − w nu' >= 0`, se
tiene `dtau = sqrt(F a b)`. Para `W_c = c nu + Phi_c(w)`:

```text
dW = Phi' b + (Phi' w + c) a >= 2 sqrt(Phi'(Phi' w + c) a b) >= dtau
   si  Phi' >= 0,  Phi' w + c >= 0,  4 Phi'(Phi' w + c) >= F.
Phi_c' = F / (2 (c + sqrt(c² + F w)))   (la raíz menor)
```

Es válida donde `c² + F w >= 0` y `c + sqrt(...) > 0`, y se exige en todo el rectángulo causal
del par. Resultado: `Delta <= c (nu_b − nu_a) + Phi_c(w_b) − Phi_c(w_a)` para cada `c` válido.
Se toma el mínimo sobre una rejilla de `c`, que no hace falta certificar porque cada `c` da una
cota válida por sí solo.

**(N4) Asignación de cotas en `S_lo`.**
- Cota inferior de `H` en las caras con `v_n > 0` (`U=-u_out`: `+1.0`; `U=u_in`: `+0.4`;
  `V=v0`: `+0.3`).
- Cota superior de `H` en `V=v1` (`v_n = −0.2`).
- `B_hi` con la cota superior.
- `S_lo = B'_lo − (2 Z'_hi/Z_lo) B_hi`.

**(N5) Aritmética.**
- Funciones trascendentes solo a través de tablas monótonas certificadas, construidas con la capa
  escalar ya auditada de B1.5.
- `np.nextafter` hacia afuera tras cada operación, también dentro de numba.
- Control del IR de LLVM contra `fast-math`, probado por mutación.

## 3. Lo que ya está auditado y no se reabre

- La capa escalar de B1.5: `s_encl`, `q_encl`, `G_encl` y la conversión `iv → float` hacia
  afuera. Su veredicto fue `AUDIT_PASS_FORMAL` en tres rondas.
- Las monotonías de `q` (creciente en `w`) y de `G` (unimodal, pico `1/e` en `w = 0`).

Si encontráis que el certificado usa esas piezas **fuera** de lo que se auditó, eso sí es
hallazgo.

## 4. Controles numéricos ya hechos (no sustituyen a la auditoría)

- Refinamiento: `S_lo = −0.00518, −0.00139, −0.00016, +0.00046, +0.00106, +0.00137` para
  `M = 16, 32, 48, 64, 96, 128`. Monótono, sin reversión.
- 0 de 3088 pares de la retícula contradicen una banda flotante independiente (geodésica por
  disparo y calibración).
- El prototipo flotante a la misma `M` da `+0.001499`; la capa certificada cuesta unos `1.2e-4`.
- El límite `M → ∞` del prototipo (`+0.002411`) coincide con un intervalo ideal medido por otra
  vía (`+0.002419`).

## 5. Lo que se os pide

Para cada una de **N1–N5** y de las hipótesis **H1–H5** de la nota (§6):

- **Hallazgo concreto, o constancia de que lo comprobasteis y se sostiene.** Un hallazgo cita la
  línea, la ecuación o la función.
- **Clasificación de cada hallazgo:** `INVALIDA_EL_CERTIFICADO`, `REQUIERE_CORRECCIÓN` (válido
  pero mal justificado o con un hueco reparable) o `MENOR`.

Al final, un veredicto único:

```text
AUDIT_PASS_FORMAL            el certificado se sostiene tal como está
AUDIT_PASS_CONDITIONAL_<X>   se sostiene bajo una hipótesis X nombrada
AUDIT_REQUIRES_MINOR_FIX     defectos reales que no cambian la conclusión
AUDIT_REQUIRES_MAJOR_FIX     un hueco que puede cambiar la conclusión
AUDIT_FAIL                   la conclusión no se sigue
```

Puntos donde más os pedimos que apretéis:

1. ¿Es (N1) correcto? En concreto: ¿el `sup` de B1.2 sobre curvas **monótonas parametrizadas
   por `V`** coincide con la separación temporal de `F dU dV`, que admite curvas causales
   generales, incluidas las de tramos nulos? Y la desigualdad triangular inversa, ¿vale para ese
   `sup` aunque las curvas concatenadas no sean parametrizables por `V`?
2. (N3): la raíz, la condición de validez sobre el rectángulo, la rama `c < 0` y el cruce de
   `w = 0`.
3. El tope `min(pi, ·)` dentro de (N2).
4. H3 (transporte de Reynolds con `h` solo acotada y continua) y H5 (convención del punto
   binary64).
5. Cualquier dirección de redondeo o índice de tabla que vaya hacia dentro.
