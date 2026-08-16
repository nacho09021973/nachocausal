# Nota de ampliación acotada — test de falsación del foro-001 en `n=24`

```text
ESTADO: SCOPE_EXTENSION_BOUNDED / SINGLE_FALSIFICATION_TEST
FECHA: 2026-08-16
NO_SUSTITUYE: docs/program_closure_note_2026-07-30.md
NO_SUSTITUYE: docs/program_reopening_note_2026-07-31.md
SELLO: intacto — no se toca
SEMILLAS: banda virgen [2.000.000–2.999.999] permanece sin quemar
```

## 1. Qué corrige esta nota

La firma del PI en `docs/foro/foro_decision_001_ef4-falsacion-adversarial.md:635` (2026-08-15)
autorizó exclusivamente el ítem C-2 y dejó fuera, entre otras cosas, la *ampliación de `n`* y el
*test `n=24`*. `docs/backlog_hallazgos.md:22` lo repite al trasladar la línea EF-0..EF-8 al backlog.

Esta nota levanta esa prohibición **para un único test nominado y para nada más**. No reabre la
línea EF-0..EF-8, que permanece en `docs/backlog_hallazgos.md` como hallazgo fuera de perímetro.

## 2. Desambiguación de nombres (obligatoria)

Dos objetos distintos han venido compartiendo etiqueta. En este repositorio, a partir de esta nota:

- **`R1`** — tarea de redacción del manuscrito de límites (`docs/manuscript_limits_draft.md`),
  definida en `docs/program_reopening_note_2026-07-31.md` §2. Sigue siendo el entregable principal.
- **`FORO001-F1`** — el *test mínimo de falsación* especificado en
  `docs/foro/foro_decision_001_ef4-falsacion-adversarial.md:581-587` (allí llamado `R-1`). Es lo
  que esta nota autoriza.

## 3. Perímetro autorizado — lista cerrada

1. Escribir un script determinista nuevo bajo `dev/` que ejecute la enumeración exhaustiva de la
   tricotomía de EF-4.3 en `n=24, rho=2`, replicando literalmente los predicados de
   `tests/test_p1a_entropia_fibras_ef4.py:63-154` (`fixed_inner`, `small_product`, `loss_case`).
2. Ejecutarlo y registrar su salida verbatim en un fichero de resultado bajo `dev/`.
3. Commitear ambos.

## 4. Qué sigue prohibido

- Modificar `tests/test_p1a_entropia_fibras_ef4.py` o cualquier test sellado. El script vive en
  `dev/` y no altera el test existente en `n=12`.
- Ampliar `n` más allá de `24`, o `rho` más allá de `2`, sin otra nota firmada.
- Extraer semillas: **ninguna**. El test es determinista y sin semillas.
- Promover ningún token de EF-4 (C-1 del foro sigue `NOT_AUTORISED`; la regla precomprometida
  sigue vigente: el autor de una reparación no firma su propia promoción).
- Sacar el PR #4 de draft (C-5 del foro sigue en pie).
- Reabrir la línea EF-0..EF-8 en cualquier otra dirección.

## 5. Predicado de decisión, precomprometido antes de ejecutar

Sobre las `C(24,4)^2 = 112.911.876` tuplas:

- Si **alguna** tupla falla los tres disyuntos (`fixed_inner`, `small_product`, `loss_case`)
  → la tricotomía queda **refutada en `n` finito**; `C1` pasa de `INCONCLUSIVE` a `REFUTED` y hay
  que delimitar por escrito qué parte de EF-4 sobrevive.
- Si **ninguna** falla → la tricotomía **no** queda refutada en `n=24`. Esto **no** demuestra `C1`
  ni promueve ningún token: elimina un contraejemplo concreto en un tamaño concreto, nada más.
  `C1` permanece `INCONCLUSIVE` salvo nota posterior.
- Se registra además cuántas tuplas tienen `small_product = False`, es decir cuántas veces los
  disyuntos `fixed_inner` / `loss_case` se ejercitan de verdad. Si ese número es `0`, el test es
  **vacuo también en `n=24`** y no ha certificado nada, cualquiera que sea el veredicto anterior.

## 6. Relación con la caja de tiempo

No hay prórroga de la caja de seis semanas de `docs/program_reopening_note_2026-07-31.md` §5, que
vence el **2026-09-11**. Este test no bloquea `R1` ni justifica retrasarlo.

## 7. Firma

```text
AUTHORISED_BY_PI: Ignacio
DATE: 2026-08-16
AUTHORISED_SCOPE: FORO001-F1 (enumeración de tricotomía en n=24, rho=2), script dev/ + resultado + commit
ALSO_AUTHORISED: push de a7b6623; commit del cierre de C-3 en wp4_fisher_localization_floor.md
NOT_AUTHORISED: todo lo listado en §4; C-1 y C-5 del foro-001 siguen sin autorizar
OVERRIDING_NOTES: sustituye a `NOT_AUTORISED: ampliación de n; test n=24; commit; push` de
  foro_decision_001:635 sólo en lo enumerado en §3 y en ALSO_AUTHORISED
```
