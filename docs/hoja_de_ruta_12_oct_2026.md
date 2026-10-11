# Hoja de ruta — 12 oct 2026 · B2 tras la auditoría del certificado de la compuerta

> **Plan REVISABLE, no congelado.** No es pre-registración, no fija umbrales y no autoriza nada
> por sí mismo; cada paso marcado *requiere decisión del PI* espera a esa decisión. Siguen
> vigentes los guardarraíles de B2 (`no_new_path`, `no_new_t0`, `no_new_points`, `no_search`,
> `no_adjustment`) y el de la enmienda: excluir cero en `t0` **no** emite un terminal de B2.1.
> Sigue la convención de una hoja de ruta por fecha; no sustituye a las anteriores.

## 0. Dónde quedó la sesión del 2026-10-11

| pieza | estado | dónde |
|---|---|---|
| Error de signo en B2.2 (caras inferiores sin normal exterior) | corregido; B2.2 y B3 → `INCONCLUSIVE_BY_BOUNDS` | `933aa85`, `dev/B2_2_SIGN_BUG_2026-10-11.md` |
| Regla de promoción de B2 → «excluir cero» | **firmada** por el PI | `b39978e`, `dev/B2_PROMOTION_RULE_AMENDMENT_2026-10-11.md` |
| Representación antigua `[recta, CS]` | agotada en `t0`; opción (B) `M=16` muerta | `41918aa`, `dev/B2_GATE_RESULT_2026-10-11.md` |
| Representación nueva: tiempo propio 2D + calibración de Hamilton–Jacobi | intervalo ideal de `S` excluye cero | `339540b`, `9563807`, `dev/B2_NEW_REPRESENTATION_2026-10-11.md` |
| Camino 2: prototipo flotante | `S_lo > 0` desde `M=64` | `b040ec1`, `dev/B2_PATH2_PROTOTYPE_2026-10-11.md` |
| **Certificado con redondeo dirigido** | `S_lo = +0.0013679`, `drho/dt(t0) >= +0.00705`, terminal `B2_CORRECTED_POSITIVE` | `7909c0e`, `research_program/puente_3p1/2026-10-11/` |
| **Auditoría del sanedrín** (5 casas, 0 fallos) | `AUDIT_PASS_CONDITIONAL_B15_DEPENDENCIES`, unánime; condición comprobada después y reejecución idéntica bit a bit | `beaf6af`, `revisiones/2026-10-11-auditoria-certificado-b2/RESUMEN.md` |

El certificado **no** está promocionado todavía. Lo bloquean solo los pasos 1 y 2 de abajo.

## 1. Correcciones de la nota del certificado (sin tocar `S_lo`)

Fichero: `research_program/puente_3p1/2026-10-11/B2_path2_gate_certificate.md`. Todas salen del
veredicto del sanedrín (`sanedrin.log`, «Ronda Veredicto»):

1. **H4.** Reescribirla como hipótesis de entorno: IEEE-754 binary64 más **todas** las
   evaluaciones de `mpmath.iv` (`exp`, `cos`, `log`, `pi`), y compilación sin `fast-math`.
2. **Cauchy–Schwarz integral.** Etiquetarla como lema nuevo de esta auditoría (CIRO, ronda 2):
   `L[U] <= sqrt(dU ∫ q(U(V)V)² dV) <= sqrt(dU ∫ q(U_b V)² dV)`. No es «B1.2 UB / H1a».
3. **H1.** Incluir el argumento de regularización `V_ε` de ASTRA (ronda 1). Es lo que cubre los
   enlaces horizontales de la cara `V=v0`. Retirar cualquier rastro del argumento de medida nula.
4. **Resta `AU`/`AL`.** Explicar por qué `PU_hi[ka] − PU_lo[kb]` acota la integral: el prefijo
   común se cancela (ABNER, ronda 1).
5. **§1.** Sustituir la negación actual por: monotonía estricta de `rho` en **algún intervalo no
   cuantificado** de `γ(s) = lambda*_binary64 + s·d`. Decir explícitamente que **no** da el
   signo en el punto medio real ni un radio usable en B2.1.
6. **§3.** Cambiar «sumas secuenciales dirigidas» por «árbol por parejas dirigido de B1.5».
7. **H3.** Pasa de «contrastado» a teorema: Leibniz sobre rectángulos de caras afines, con el
   módulo de continuidad de ASTRA.
8. **Declarar `λ5 = 0.1`** como componente congelada que no se mueve.
9. **Añadir una sección «Auditoría»** con el veredicto, la tabla de la condición comprobada y la
   reejecución bit a bit (copiar de `RESUMEN.md`).

Hecho cuando el diff solo toca texto, el verificador reproduce el JSON congelado y el commit
cita `beaf6af`.

## 2. Promoción — *requiere decisión del PI*

Con el paso 1 hecho, el PI decide si el estado pasa de `CERTIFICATE_FROZEN / PENDING_INDEPENDENT_AUDIT`
a algo como:

```text
B2_GATE = CERTIFIED_POSITIVE_AT_T0 (AUDIT_PASS_CONDITIONAL_B15_DEPENDENCIES, condición verificada)
B2.1    = INCONCLUSIVE_BY_BOUNDS   (sin cambio)
B3      = INCONCLUSIVE_BY_BOUNDS   (sin cambio)
```

Antes de firmar conviene confirmar dos cosas:

- que el veredicto condicional, con la condición verificada fuera del sanedrín, basta según la
  costumbre del repo; B1.5 llegó a `AUDIT_PASS_FORMAL` en tres rondas;
- si se quiere una segunda pasada corta del sanedrín sobre la nota corregida. No se pidió.

Al promocionar hay que actualizar la memoria de proyecto y, si procede, el estado del puente 3+1D.

## 3. Lean: lema de calibración — *requiere decisión del PI*

El PI pidió esperar al sanedrín antes de usar Lean, y el sanedrín ya ha terminado.

**Lema 1 (barato, recomendado).** Para reales `F, w, c, a, b`:

```text
Phi' >= 0,  Phi'·w + c >= 0,  4·Phi'·(Phi'·w + c) >= F,  a >= 0,  b >= 0
  ⟹  Phi'·b + (Phi'·w + c)·a >= sqrt(F·a·b)
```

Además, `Phi' = F/(2(c + sqrt(c² + F·w)))` cumple las tres hipótesis cuando `c² + F·w >= 0` y
`c + sqrt(c² + F·w) > 0`, con igualdad en la tercera.

- **Infraestructura:** copiar la configuración de `~/qca-causal-cones/formal`, que tiene Lean
  v4.31.0 y Mathlib `fabf563` (`lean-toolchain`, `lakefile.toml`). El proyecto sería
  `nachocausal/formal/`, **sin tocar** `qca-causal-cones`; su `CLAUDE.md` prohíbe meter causal
  sets allí.
- **Criterio de hecho:** `lake build` sin `sorry`, y `#print axioms` limitado a los tres axiomas
  estándar.

**Lema 2, la monotonía del `sup` respecto a los extremos.** Es caro: hay que formalizar curvas
absolutamente continuas y la regularización `V_ε`. El sanedrín ya lo cerró en papel. No se hace
salvo decisión expresa.

## 4. Abierto, sin orden ni autorización

- **B2.1, monotonía en la malla `{0.45, …, 0.55}`.** Requiere un **radio cuantificado**, por
  ejemplo una cota inferior de `rho'` en un intervalo, que es otro certificado. El certificado
  actual no lo da.
- **Transferir el signo** del punto binary64 al punto medio real. Probablemente basta un
  argumento de continuidad con módulo explícito; está sin hacer.
- **B3, `n=2` frente a `phi`.** Sigue inconcluso tras corregir el signo. La representación nueva
  podría estrechar `drho/dx`; está sin evaluar.
- **Consulta a Pfeiffer.** Borrador corregido en `dev/PFEIFFER_2022_W2_STEP_QUERY_2026-10-11.md`,
  sin enviar; la sugerencia era mandarla a Pfeiffer con Bjerrum-Bohr y Eichhorn en copia. Envío
  externo: decide el PI.
- **`qca-causal-cones`.** La pregunta de si un sustrato tipo QCA, con cono `C_micro` anisótropo,
  cambiaría `h` y la identificabilidad es legítima, pero sería un programa nuevo con acta propia.
  No se mezcla.

## 5. Orden propuesto para mañana

1. Correcciones de la nota (§1). Hacerlo y hacer commit.
2. Decisión del PI sobre la promoción (§2).
3. Si el PI lo autoriza, Lean del lema 1 (§3).
4. Repasar §4 y elegir, si procede, el siguiente frente.
