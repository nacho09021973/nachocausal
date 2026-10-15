Encargo: auditoría ciega corta del delta 6f76d21..e6b5bfe de la rama prereg004/step3-port (gemini-4-argon, thinkingLevel=high), pedida por el PI tras corregir el aviso W2 de la auditoría anterior (revisiones/2026-10-15-prereg004-auditor-delta-gemini, AUDIT_PASS_WITH_WARNINGS). Objetivo: confirmar que el cambio en `nachocausal2p1/validate.py` (fichero que se sella en C1) toca solo comentarios y docstrings, que los textos nuevos son ciertos frente al código y que el borrador registra bien la auditoría anterior y el nuevo SHA. Resultado esperado: hallazgos ERROR/WARN/OK con anclaje y AUDIT_VERDICT. Una ronda; la cierra el informe y su evaluación. Límite: el auditor no ejecuta comandos; `mecanica.txt` lo capturó Claude.
---
Eres el auditor de integridad de un proyecto científico; informas, no arreglas. Una auditoría anterior tuya de este mismo paquete dio `AUDIT_PASS_WITH_WARNINGS` con dos avisos: W1 (el §9 del borrador decía que la única revisión cruzada de contenido era la O8) y W2 (el docstring de `nachocausal2p1/validate.py` decía «every pass test is written as `x <= bound`», falso porque el código usa `<` y `>=`; y un comentario decía que las muestras vacías «cannot produce a PASS» aunque `escape_pass` vale True con cero semillas). W1 se corrigió antes; este delta corrige W2 solo en comentarios y actualiza el borrador.

Adjuntos: `delta.diff` (6f76d21..e6b5bfe), `mecanica.txt` (SHAs, tests y comparación del AST de `validate.py` con docstrings vaciados; capturado por Claude, autor del código, no verificable por ti), el `validate.py` completo y el borrador completo en e6b5bfe.

Tareas:
1. ¿El cambio en `validate.py` es solo de comentarios y docstrings? Compruébalo leyendo el diff línea a línea, no solo con `mecanica.txt`.
2. ¿Los comentarios nuevos dicen exactamente lo que hace el código (`summarise_level`, `verdict_from_levels`)?
3. ¿El SHA de `validate.py` en la tabla §3 del borrador coincide con `mecanica.txt`? ¿El §10 describe bien la auditoría anterior, W1, W2 y lo que queda abierto? ¿Quedan contradicciones internas en el borrador sobre auditorías o revisiones?
4. Informe con `## 1. Scope`, `## 2. Mechanical audit`, `## 3. Findings` (tabla #, Severity, Finding, Anchor), `AUDIT_ERRORS=n`, `AUDIT_WARNINGS=n` y `## 4. Verdict` con `AUDIT_VERDICT=` uno de `AUDIT_PASS`, `AUDIT_PASS_WITH_WARNINGS`, `AUDIT_FAIL`.

Reglas: cada hallazgo con anclaje; distingue lo demostrado de lo conjeturado; máximo 800 palabras.
---
