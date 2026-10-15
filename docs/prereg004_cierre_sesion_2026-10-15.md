# Prereg-004: nota de cierre de la sesión del 2026-10-15

Rama `prereg004/step3-port` (worktree `.worktrees/prereg004-step3`). Todo lo siguiente está en
origin. Esta nota no es un resultado ni un veredicto.

## Hecho hoy

| paso | commit | qué |
|---|---|---|
| auditoría 046 registrada | `efada85` | Codex, `AUDIT_PASS` sobre la remediación de 045 |
| comité 053 | `8cc3125` | paso 7 del 052: `RECOMMEND_REVISE_AND_RECONVENE`; solo texto y procedimiento |
| correcciones del 053 | `007947e` | precedencia del veredicto, NaN, (v) como precondición, aviso de potencia, `git add -f`, procedencia, procedimiento C1; 2 tests; `make test-004`, `dry-run-004`, `verify-seal-004` |
| revisión cruzada | `8c2c01f`, `f19c80f` | Gemini sobre `007947e`: «listo con cambios menores»; 11 objeciones confirmadas |
| G8 y texto | `76da124` | `--full-history` en `seed_manifest._check_freeze` (merge `-s ours` daba otro sorteo); test que falla sin el arreglo |
| sin ensayo de malla completa | `616c55d` | decisión del PI |
| auditoría del delta | `b18ba31`, `6f76d21`, `e6b5bfe`, `94422d7`, `0c16845` | Gemini sin ejecución de comandos: `782d031..616c55d` `AUDIT_PASS_WITH_WARNINGS` (W1 texto, W2 comentarios de `validate.py`, AST igual); `6f76d21..e6b5bfe` `AUDIT_PASS` |
| firma del PI | `94cd3b4` | comités 052 y 053 firmados sobre `0c16845`; reconvocatoria dispensada por el PI |
| tests previos a la congelación | `51bf237` | cinco tests fijados al estado candidato |
| **C1** | **`d6494e5aa32289594c1f30033ac041eecdb87ee6`** | `docs/preregistration_004.md` añadido; `STATUS = "FROZEN"` |
| nota de C1 firmada | `3e20d47` | SHA de C1 en el §11 del comité 053; el PI autoriza C2 y C3 |
| **C2** | **`8ff5b3b`** | `docs/validation_004_seeds.json`: 20 semillas, `draw_seed` `0xd6494e5a` |

Comprobado antes de C1: `make test` 560 aprobados; `make verify-seal` `6e2c3888…`;
`make verify-comite` 53 PASS; tabla §3 = `make verify-seal-004`; `make dry-run-004` exit 0.

## No hecho: C3

C3 no se lanzó. No existe `results/` ni se ha generado ninguna realización con semillas vírgenes.

Motivo: este equipo tiene WSL limitado a 4 CPUs (`C:\Users\ignac\.wslconfig`, `processors=4`;
`nproc` = 4). El §8 del prerregistro congelado mide la corrida con 20 hilos de numba y 20 CPUs
visibles, y solo afirma reproducibilidad para esa configuración. La guarda del código no lo
detecta: numba acepta 20 hilos sobre 4 núcleos. El PI decidió hacer C3 el 2026-10-16 en otro
equipo más potente. Tarea: `docs/prereg004_tarea_C3_2026-10-16.md`.
