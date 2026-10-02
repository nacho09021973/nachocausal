# Integración local del PR #9 — 2026-10-02

Estado: preparado para revisión; no publicado ni fusionado en GitHub.

## Entradas

- Base: `origin/main`, `a393934`.
- PR #9, `origin/relatividad`: `875d2c33310ff54b5510c7fcef474df572097cbb`.
- Rama de preparación: `integration/pr9-relatividad`.
- Worktree: `.worktrees/pr9-integration`.

Las cuatro ramas `split/pr9-relatividad-{docs,research,audit,artifacts}`
se compararon con main. No se aplicaron: la separación por rutas no resuelve
la precedencia entre versiones y sustituye el manuscrito y figuras actuales
por versiones anteriores. Se prepara una fusión de las dos historias originales.
Las ramas split se conservan.

## Resolución de conflictos

- README: conserva la presentación del manuscrito actual de main e incorpora
  el checkpoint de septiembre y el bloque teórico de relatividad.
- Backlog: conserva íntegra la entrada EF de main y añade la entrada de agosto
  sobre el tangente geométrico de relatividad.
- Manuscrito: la ruta canónica conserva exactamente main. La versión de
  relatividad se preserva, sin cambios, en
  `docs/archive/relatividad_875d2c3/manuscript_limits_draft.md`.
- Figuras: se mantienen los archivos actuales de main y su runner. La carpeta
  viz completa de relatividad se conserva en `viz/legacy/relatividad_875d2c3`.
  Es un snapshot histórico; las citas a viz en informes antiguos corresponden
  al commit de esos informes, no necesariamente a las figuras actuales.
- WP4: se conserva la actualización de relatividad, que incluye la derivación
  del prefactor y sus límites declarados, junto a su código permanente.
- `memoria_claude/`: conserva main; no se importan las memorias divergentes.

Los informes históricos y sus textos no se reescriben. La integración no
revalida sus afirmaciones ni constituye una revisión científica independiente.

## Controles B1

Los nueve archivos locales de `research_program/puente_3p1/2026-09-14/B1`
pertenecen al puente Schwarzschild, no al programa de saturación detenido.
Se copian byte por byte y se conservan sus originales en el checkout del usuario.

Su antecedente B1.5 faltaba en relatividad. Se incorporan sus cinco archivos
desde `6633ebd2da81188ecc492f59b44b75e0e2c59cd2`, sin incorporar el resto de
la rama `emergencia/p1a-canal-sigma-m`.

Se declara `mpmath==1.3.0` en requirements, usado por los verificadores
intervalares y disponible en el entorno con que se comprobaron.

Repeticiones de los generadores permanentes B1.6, B1.7 numérico y B1.7 formal:
los tres JSON coinciden exactamente con los conservados. Las salidas de esta
comprobación son temporales; los resultados canónicos y sus generadores están
incluidos en la integración. No se ejecutan simulaciones ni se amplía el par.

## Verificaciones

- `nachocausal/thresholds.py`: SHA-256
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`,
  coincide con `docs/preregistration_002.md`.
- Los preregistros y el código del instrumento no tienen cambios frente a main.
- Manuscrito canónico, runner y figuras actuales: preservados desde main.
- `git diff --check` señala espacios finales ya presentes en documentos de
  relatividad (incluidos informes históricos); no se limpian esos registros.
- Suite `python3 -m pytest -q tests/`: **496 passed, 1 warning**, 404.89 s.
  El warning corresponde a Axes3D no disponible en el entorno Matplotlib;
  ninguna prueba falla.
- Sin rutas sin resolver ni marcadores de conflicto. El chequeo de diff con
  espacios finales históricos excluidos (`core.whitespace=-blank-at-eol`) pasa.
- Snapshot de viz de relatividad: 14 archivos idénticos al commit fuente;
  viz actual: 17 archivos idénticos a main.
- Inventario de cambios del PR contrastado contra el árbol preparado: sólo
  README, backlog, hoja de ruta de emergencia, requirements y el índice de
  work packages combinan contenido; las otras diferencias intencionadas están
  descritas arriba.

## Publicación pendiente

Esta rama contiene ambos padres de la fusión. Una vez revisada, puede actualizar
relatividad mediante fast-forward, conservando el PR #9 y su historial.
No se ha hecho push, cerrado ningún PR ni modificado main.
