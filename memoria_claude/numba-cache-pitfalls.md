---
name: numba-cache-pitfalls
description: numba cache=True causó dos fallos el 2026-10-12: inspect_llvm vacío (control de fast-math que pasa en vacío) y globales congelados entre ejecuciones (tablas de otra T)
metadata:
  type: feedback
---

`@njit(cache=True)` tiene dos trampas que hoy costaron trabajo real:

1. **`inspect_llvm` devuelve un módulo vacío** cuando el kernel se carga de la caché, y un
   control de fast-math que lo lea **pasa en vacío**. Para inspeccionar código de verdad: caché
   privada vacía (`NUMBA_CACHE_DIR` temporal, fijado antes de importar numba), exigir
   `stats.cache_hits == 0` y clausura de símbolos (ver `guard_kernels` en
   `research_program/puente_3p1/2026-10-12/verify_b2_1_box_certificate.py`).
2. **Los globales quedan congelados como constantes** y la caché solo se invalida si cambia el
   fichero fuente. Si una tabla global depende de una variable de entorno (por ejemplo
   `NC2P1_T_EDGE`), cada subproceso reutiliza la de la primera compilación. Prueba mínima:
   `XVAL = 1, 5, 9` da `2.0` las tres veces.

**Why:** el segundo fallo invalidó dos barridos 2+1D (tablas `q(w)` de otra `T`), y ningún
control interno lo vio, porque todos compartían las mismas tablas. Lo destapó la comparación con
la versión GPU, que recibe las tablas como argumentos.

**How to apply:**
- Nada de `cache=True` en kernels que lean globales que dependan del entorno o de parámetros;
  pasar las tablas como argumentos.
- Validar siempre contra una implementación independiente (otra máquina, la GPU u otro
  algoritmo), no solo con controles de coherencia interna.

Relacionado: [[frente-2p1-ecuatorial]], [[puente-3p1-b2-gate]], [[gpu-exploration-backend]].
