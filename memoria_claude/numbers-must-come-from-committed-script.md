---
name: numbers-must-come-from-committed-script
description: Failure mode caught by /auditor 2026-07-25 — numbers computed in ad-hoc shell commands and pasted into a results note have no committed generator; emit them from the script instead
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8846831e-d475-4229-b6b1-cce722f8893c
  modified: 2026-07-25T07:25:08.422Z
---

Al redactar una nota de resultados en nachocausal, **todo** número debe salir del stdout del script
commiteado, no de un comando interactivo ad-hoc. En la sesión del 2026-07-25 calculé tres valores de
`V(tau)` con un `python -c` suelto y los cité en `wp4_comparable_pair_separation.md` §5; el script
commiteado no los emitía. `/auditor` lo marcó como **ERROR** (`auditor_report_024`, veredicto
`AUDIT_FAIL`) y tenía razón: la nota decía que todos sus números venían de un solo script, luego un
lector no podía reproducirlos.

**Why:** la regla fundacional del repo es que cada número lleva respaldo verificable o va marcado
`[UNVERIFIED]`. Que la *función* generadora esté commiteada no basta — hay que ejercitarla con esos
argumentos y que imprima. Es exactamente el modo de fallo que `/auditor` existe para cazar (AI que
"fabrica" resultados), y me pasó a mí, no a un agente hipotético.

**How to apply:** antes de escribir números en una nota, añadir un check numerado al script que los
imprima, y —mejor— un `assert` sobre la propiedad que sostienen (así el guardrail puede fallar en
vez de ser decoración). Después: barrido mecánico de comprobación, extraer todo literal numérico de
la nota y exigir que aparezca verbatim en una captura fresca del stdout
(`grep -oE '[0-9]+\.[0-9]{3,}' nota.md` → `grep -F` contra la captura). Correr `/auditor` **antes**
de tocar etiquetas `[PROVED]`/`[OPEN]`, nunca después. Relacionado:
[[program-paused-reentry-marker]].
