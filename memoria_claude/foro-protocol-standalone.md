---
name: foro-protocol-standalone
description: Protocolo de foro adversarial genérico extraído de /comite; vive en ~/foro (fuera de todo repo) y se carga como skill vía symlink desde ~/.claude/skills/foro
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9b6569d3-af20-421f-bc69-04fb87e40882
  modified: 2026-08-15T18:07:10.924Z
---

El protocolo de deliberación adversarial genérico (`/foro`) vive en **`/home/adnac/foro`**, un
directorio independiente fuera de nachocausal y de cualquier otro repo, creado 2026-08-15. Se
carga como skill mediante `~/.claude/skills/foro -> /home/adnac/foro` (symlink), así que está
disponible en todos los proyectos.

Es la generalización de `.claude/skills/comite/` de nachocausal, sin el dominio: los expertos de la
ola 1 se derivan de la pregunta, los 3 controles (falsificador, guardián de compromisos,
verificador de fuentes) son fijos, y lo específico de cada proyecto se declara en un `FORO.md` en
la raíz de ese proyecto (plantilla en `templates/FORO.template.md`).

**Por qué importa recordarlo:** es un repo git propio (`main`, commit inicial 7af7140) **sin
remoto**, así que no viaja a ninguna parte todavía y no aparece en el `git status` de ningún otro
proyecto. Para tenerlo en otra máquina hay que darle remoto y push, y rehacer el symlink.
`python ~/.claude/skills/foro/test_check_brief.py` debe dar `TEST_CHECK_BRIEF=PASS`.

Relacionado: [[memoria-claude-sync]] (misma clase de problema: estado valioso fuera del repo),
[[numbers-must-come-from-committed-script]] (la regla del oráculo fuera de la capa de lenguaje que
el protocolo enforcea).
