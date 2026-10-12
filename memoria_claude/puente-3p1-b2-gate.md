---
name: puente-3p1-b2-gate
description: "Puente 3+1D / B2 — compuerta en t0 PROMOCIONADA 2026-10-12 (CERTIFIED_POSITIVE_AT_T0, pase condicional del sanedrín con la condición verificada); B2.1 y B3 siguen INCONCLUSIVE_BY_BOUNDS; qué NO da el certificado"
metadata:
  node_type: memory
  type: project
  originSessionId: 9bbca683-ada3-4de3-a0b2-353599e0546a
  modified: 2026-10-12T07:10:00.533Z
---

**B2_GATE = CERTIFIED_POSITIVE_AT_T0**, promocionado por el PI el 2026-10-12. La nota es
`research_program/puente_3p1/2026-10-11/B2_path2_gate_certificate.md` (§8 auditoría, §9
promoción). `S_lo = +0.0013679`, `drho/dt(t0) >= +0.0070474`, con redondeo dirigido.
Verificador y JSON congelados en `7909c0e`; el sanedrín (`beaf6af`) dio
`AUDIT_PASS_CONDITIONAL_B15_DEPENDENCIES` y la condición se comprobó fuera de él. No hubo
segunda ronda (B1.5, en cambio, llegó a `AUDIT_PASS_FORMAL`).

**Lo que NO da** (no sobrevenderlo nunca):
- radio cuantificado de monotonía, así que nada para la malla de B2.1;
- el signo en el punto medio real: el objeto es `γ(s) = lambda*_binary64 + s·d` (H5).

La enmienda firmada sigue vigente: excluir cero en `t0` **no** emite un terminal de B2.1.
`B2.1 = B3 = INCONCLUSIVE_BY_BOUNDS`.

**Why:** el certificado es fácil de citar como si diera monotonía en la malla; el sanedrín
insistió en que no la da.

**B2.1 (2026-10-12, `f1e030f`): certificado por cajas, `drho/dt > 0` en todo [0.45,0.55]** (100 cajas, min S_lo +0.0012174), terminal B2.1_POSITIVE_DERIVATIVE, PROMOCIONADO 2026-10-12 (ASTRA, pase condicional con las condiciones atendidas, `998811d`; una sola casa). **Control de fast-math: con numba cache=True, inspect_llvm devuelve un módulo VACÍO → el control pasaba en vacío (también el de la compuerta); hay que inspeccionar IR recompilado sin caché (`fresh_ir`)**; los 19 kernels de la compuerta están limpios (`a9d3288`).

**B3 (2026-10-12, `1f7286d`): certificado B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY** (W23 >= +0.0077379; drho/dx3 vía gate.run() con VN_FR de e3), FROZEN/PENDING_AUDIT. Propone (no autoriza) n=3. Lean lema 2: encargo para Codex en `formal/TAREA_LEMA2_CODEX.md` (rama codex/lean-lema2), lo lanza el PI.

**How to apply:** no fiarse de ningún `fastmath_guard.ok` de una reejecución con la caché caliente. Transferencia del signo al punto medio real: PROMOCIONADA 2026-10-12 como B2_SIGN_TRANSFERRED_TO_REAL_MIDPOINT (`2026-10-12/B2_sign_transfer.md`; AUDIT_PASS de CIRO+ABNER a ciegas, auditoría ligera pedida por el PI; ABNER por la web porque la API agotó el timeout); pérdida <= 2.5436e-8 frente a S_lo 1.37e-3. Da de paso un radio de 1e-7 en γ, pero el módulo sqrt(δ) de h impide llegar a B2.1 (necesita 0.05). La consulta a
Pfeiffer no se ha enviado (decide el PI). Lean: lema 1 (calibración AM-GM) HECHO el 2026-10-12 en `formal/` (`7fa9c66`), sin sorry y
con solo los 3 axiomas estándar; el lema 2 (monotonía del `sup`) NO está autorizado. Orden y frentes: `docs/hoja_de_ruta_12_oct_2026.md`.

Relacionado: [[program-status-reentry-marker]], [[numbers-must-come-from-committed-script]].
