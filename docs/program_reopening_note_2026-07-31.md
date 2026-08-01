# Nota de reapertura acotada de `nachocausal`

```text
ESTADO: REOPENED_BOUNDED / WRITE_UP_ONLY_PLUS_ONE_DERIVATION
FECHA: 2026-07-31
NO_SUSTITUYE: docs/program_closure_note_2026-07-30.md (permanece íntegra en el registro)
SELLO: intacto — no se toca
SEMILLAS: banda virgen [2,000,000–2,999,999] permanece sin quemar
```

## 1. Base

El cierre del 2026-07-30 es explícitamente **deóntico, no alético**: retira la autorización
para seguir ampliando el programa bajo su objetivo fuerte, y declara que **no** afirma que no
exista camino legítimo alguno. Su cláusula 1 acota la prohibición a lo que se abra *"dentro del
objetivo de reconstrucción de horizonte 1+1D/3+1D que este programa perseguía"*, y su cláusula 3
establece que los manuscritos se conservan *"como registro de lo probado, lo refutado y lo que
quedó abierto"*.

Esta nota no revoca el cierre. Restaura autorización para **dos tareas nominadas**, y para nada
más.

## 2. Qué se reabre — lista cerrada de dos ítems

**R1 — Llevar el registro de límites a entregable.** El manuscrito
`docs/manuscript_limits_draft.md` (1.280 líneas, teoremas numerados) con el Teorema 3.8 (suelo de
localización order-only, N1) y el 3.9, con las siete correcciones de la revisión externa
(`R-A1`–`R-B2`) ya aplicadas. Es redacción, no investigación.

**R2 — Derivar analíticamente el exponente `λ⁶`.** `wp4_fisher_localization_floor.md` §5a
registra una ley de potencias **empírica** `κ ~ λ⁶` (exponente estable 5.9–6.0) bajo
estrechamiento de diamantes hacia el horizonte, y declara textualmente que su derivación
analítica —"a near-horizon/Rindler expansion of `I(τ)` is a plausible route"— **no fue
intentada**. Se autoriza intentarla.

**Tensión declarada, no disimulada.** R2 es un cálculo nuevo dentro de un programa cerrado. Se
autoriza porque es un **límite sobre** la localización cerca del horizonte, no un intento de
reconstruirlo — dirección opuesta a la del objetivo clausurado — y porque su diana numérica ya
existe. Si el PI considera que aun así viola la cláusula 1, R2 decae y R1 sigue en pie por sí
solo.

## 3. Qué sigue cerrado

Sin cambios, y con las cláusulas del cierre en vigor:

- reconstrucción de horizonte 1+1D o 3+1D, en cualquier reformulación;
- PR004, localizadores C1–C6, anclas de presente, ladder-braiding, diagnósticos de rescate;
- `Q_trap` v2 — sigue `UNADJUDICATED_AT_CLOSURE`, no se reconvoca;
- nuevos observables, nuevos work packages fuera de R2, simulaciones, validaciones;
- extracción de semillas: **ninguna**. La banda virgen no se toca;
- **lenguaje de novedad absoluta: prohibido** (cláusula 2 del cierre; `NOVELTY_CERTIFIED = NO`,
  `PRIOR_FOR_N1 = NOT_FOUND_BY_EITHER_READER` no es un certificado);
- sello, terminales, pruebas e historial: no se alteran. La reapertura es **append-only**;
  `nachonumero` pinea `nachocausal@bcd4633` vía `verify_herencia.py` y ese commit no se toca.

## 4. Entregable y test de terminado

> Una nota de límites, sometible, sobre lo que el canal order-only **no** puede localizar en una
> familia regular de diamantes de Schwarzschild 1+1D, con el suelo `δ ~ ℓ/√κ` y su constante
> calculada.

Terminado cuando, y solo cuando:

1. el manuscrito compila a un PDF autocontenido, sin referencias internas al repo que un lector
   externo no pueda seguir;
2. toda afirmación de prioridad está acotada según §3, sin excepción;
3. las cifras publicadas (`V ≈ 1.4717`, `I ≈ 5.415e-4`, `κ ≈ 7.97e-4`, `δ_τ/ℓ ≈ 35.4`) son salida
   literal de `wp4_kappa_numeric_reference.py` re-ejecutado, con su error de cuadratura declarado
   como tal y **no** presentado como exacto;
4. R2 está resuelto **o** explícitamente marcado como abierto en el texto.

El punto 4 es deliberado: **R2 no puede bloquear R1.** Si la expansión Rindler no sale, el
manuscrito sale igual, con el `λ⁶` como observación numérica y problema abierto declarado.

## 5. Caja de tiempo

**Seis semanas desde esta nota.** Al llegar, se somete lo que haya o se vuelve a archivar. No hay
prórroga. R2 tiene además su propio tope: **dos semanas**; si no ha salido, se marca abierto y se
pasa a R1 sin discusión.

## 6. Reglas heredadas de la sesión del 2026-07-31

1. Perímetro fijo: R1 y R2. Nada entra sin una nueva nota firmada.
2. Todo hallazgo fuera de perímetro va fechado a `docs/backlog_hallazgos.md`, nunca al trabajo en
   curso.
3. La novedad no es criterio de éxito. El entregable es el registro, no la medalla.
4. Ningún resultado se reabre para "mejorarlo". Se publica lo probado, con sus límites escritos.

## 7. Firma

```text
REOPENED_BY_PI: Ignacio
DATE: 2026-07-31
AUTHORISED_SCOPE: R1, R2
NOT_AUTHORISED: todo lo listado en §3
DECISION_R2: AUTORIZADO
BRANCH: reopen/r1-r2-limits-writeup, desde bcd4633
```
