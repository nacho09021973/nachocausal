# Memory index

- [ESTADO DEL PROGRAMA — marcador de reentrada](program-status-reentry-marker.md) — cerrado 2026-07-30 (deóntico, tag `program-closed-2026-07-30`) y REABIERTO ACOTADO 2026-07-31 sólo para R1 (paper de límites) y R2 (derivar λ⁶); caja de 6 semanas, R2 tope 2; C6 ya es teorema, no BLOCKED; 2026-08-16: R2 cerrado como abierto y tricotomía EF-4.3 REFUTADA en n=24; 2026-08-21: positividad de `V_n^h` CERRADA (es de NC-0 §10.3, no de NC-2B) y frente vivo reducido a tres deudas de escala; LEER PRIMERO
- [GPU exploration backend](gpu-exploration-backend.md) — optional CuPy GPU path in dev/ only; sealed validation stays CPU numpy 1.26.4, two-venv setup, WSL libcuda gotcha
- [Next step: blind validation](next-step-blind-validation.md) — step #5 EXECUTED 2026-06-21 → verdict FAIL (coverage 0.30, fp 0.10); seeds burned; next is estimator-v2 dev work
- [Estimator-v2 exploration](estimator-v2-exploration.md) — post-FAIL dev work: volume observable fixes coverage (ii), false-positive (iv) axis still open; dev scripts + seed hygiene (EXPLORE_POOL / reserved 002 band)
- [PR-003 Fase #3 / Le Cam](pr003-fase3-lecam.md) — result FROZEN as prereg-003 (2026-06-25, doc-only O(ℓ) floor); open per §7: minimax-over-C, O4 lit sourcing, C2 taller-box (parked)
- [Prereg-002 PASS artifact gap](prereg002-pass-artifact-gap.md) — CLOSED 2026-07-04: SUPERVISED_REVERIFICATION MATCH; status now PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]
- [R-VAR saga: comité 017→021, CLOSED](comite-017-rvar-v2-adjudication.md) — R_VAR_STATUS=CLOSED_NEGATIVE_RESULT (47be5c7): 2nd graded object also hit tall-box MINK-null degeneracy; prereg-002 track unaffected
- [Todo número sale del script commiteado](numbers-must-come-from-committed-script.md) — fallo real cazado por /auditor 2026-07-25 (AUDIT_FAIL): números de comandos ad-hoc en una nota; emitirlos desde el script + assert + barrido verbatim
- [Protocolo /foro standalone](foro-protocol-standalone.md) — foro adversarial genérico extraído de /comite; vive en ~/foro (fuera de todo repo, sin git) y se carga por symlink desde ~/.claude/skills/foro
- [Memoria sync entre máquinas](memoria-claude-sync.md) — snapshot commiteado en memoria_claude/; re-copiar+commitear al final de toda sesión que cambie la memoria; restaurar al empezar en máquina nueva
