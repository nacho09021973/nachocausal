---
name: program-paused-reentry-marker
description: Programa en pausa limpia desde 2026-07-19 por decisión del PI; punto de reentrada único y explícito — leer antes de proponer cualquier paso nuevo
metadata: 
  node_type: memory
  type: project
  originSessionId: 6fe2e443-534b-438f-9fce-fe94a2ba9ac0
---

El PI pausó el programa voluntariamente el 2026-07-19 (no es cierre científico ni abandono;
contexto: fatiga, "creo que esto nos supera"). Todo quedó commiteado en `main` y pusheado en un
punto limpio. El marcador canónico es `docs/marcador_reentrada_2026-07-19.md`.

**Why:** tres objetos independientes (R-VAR, Candidate A/PR009/PR010, BD/OP-2.2) chocaron con la
misma pared del banco (caja alta, familia PR011 sin eje de colocación del horizonte), no con la
física. El PI decidió parar en limpio en vez de seguir moliendo candidatos contra el banco viejo.

**How to apply:** si el programa se retoma, el único siguiente paso pre-identificado es convocar
`/comite` para adjudicar UNA ejecución del falsifier enumerativo congelado de OP-2.2 (decisión
035 §5/§9, read-only, verificador ≠ autor) — descargaría V1b, resolvería V2-support y fijaría el
gap real para V3b. NO ejecutar ni convocar sin petición explícita del usuario. Estado al pausar:
gate de Candidate B `ADOPTED_AS_GATE_DEFINITION` (decisión 037 firmada, solo filtro
precondicional); dossier OP-2.2 rev. 3 con `AUDIT_PASS_WITH_WARNINGS` (auditor_report_020);
sello sin drift; `pr009-runner-scorer-v2.patch` borrado (superseded); el `.html` local se
conserva a propósito. Relacionado: [[estimator-v2-exploration]], [[pr003-fase3-lecam]].
