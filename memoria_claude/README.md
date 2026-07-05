# memoria_claude/ — memoria persistente de Claude Code (copia para sincronizar entre máquinas)

Esto es una **copia commiteada** de la memoria file-based de Claude Code para este proyecto.
La memoria "viva" que Claude lee en cada sesión NO es esta carpeta, sino:

```
~/.claude/projects/-home-adnac-nachocausal/memory/
```

(el sufijo del directorio es la ruta del repo con `/` → `-`; si el repo no está en
`/home/adnac/nachocausal`, ajusta el nombre).

## Restaurar en una máquina nueva

```bash
mkdir -p ~/.claude/projects/-home-adnac-nachocausal/memory
cp -r memoria_claude/*.md ~/.claude/projects/-home-adnac-nachocausal/memory/
```

(No copies este README a la carpeta de memoria; solo los ficheros de memoria y `MEMORY.md`.)

## Disciplina de sincronización

- Al **terminar** una sesión que haya cambiado la memoria: recopiar la memoria viva aquí y
  commitear (`cp ~/.claude/projects/-home-adnac-nachocausal/memory/*.md memoria_claude/`).
- Al **empezar** en otra máquina: restaurar como arriba ANTES de lanzar Claude Code.
- Fuente de verdad en caso de conflicto: la copia con el commit más reciente en `main`.
- Esto es contexto interno del asistente (estado del proyecto, lecciones de proceso, gotchas
  de entorno). No forma parte de los resultados científicos: nada aquí es un registro
  congelado, un umbral ni un veredicto — para eso están `docs/` y los comités.

Última sincronización: 2026-07-05 (post-cierre R-VAR, tras `plan_genial.md`).
