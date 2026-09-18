---
name: memoria-claude-sync
description: Claude memory is synced across machines via committed memoria_claude/ snapshot — re-copy + commit at end of any session that changes memory
metadata: 
  node_type: memory
  type: project
  originSessionId: a589c5ae-bf47-4b70-ac29-121d4b74fa88
---

The PI works from two machines. Claude's file-based memory does NOT travel with the repo, so
since 2026-07-05 a snapshot is committed at `memoria_claude/` (see its README.md for restore
instructions).

**Why:** without this, the second machine's sessions start blind to the R-VAR closure,
prereg state, seed hygiene, and process lessons.

**How to apply:**
- At session END, if any memory file changed this session:
  `cp ~/.claude/projects/-home-adnac-nachocausal/memory/*.md memoria_claude/` (do NOT
  overwrite memoria_claude/README.md with a memory file), then commit + push.
- At session START on a machine where `MEMORY.md` looks older than
  `memoria_claude/MEMORY.md` in git: restore per `memoria_claude/README.md`.
- Source of truth on conflict: the most recent commit on `main`.
