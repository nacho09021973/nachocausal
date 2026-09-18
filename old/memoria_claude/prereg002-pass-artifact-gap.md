---
name: prereg002-pass-artifact-gap
description: "prereg-002 PASS's original raw artifact was unrecoverable; RESOLVED 2026-07-04 via SUPERVISED_REVERIFICATION MATCH — status now PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]"
metadata: 
  node_type: memory
  type: project
  originSessionId: ea90fda6-8c0d-4f6c-aece-76f5b54e383c
---

Auditor 005 (2026-07-03, `docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md`)
returned **AUDIT_FAIL**: the prereg-002 PASS (2026-06-22, commit fee12d5, seal 6e2c3888)
cites `results/validation.json` as raw output, but that file held the prereg-001 FAIL
(mtime 2026-06-21 12:14, BEFORE the prereg-002 seal 573cfcb of 2026-06-22 12:20). No file
on this machine contains any virgin-band seed (2076703…). Timing warn: 13m14s between seal
commit and PASS commit vs 32.5 min for the smaller prereg-001 run here.

**RESOLVED AS UNRECOVERABLE (2026-07-04, PI determination):** the second machine is not
available; `PRIMARY_PASS_ARTIFACT = UNAVAILABLE` is definitive. The label is
`[UNVERIFIED_PRIMARY_MISSING]` — permanent unless a comité authorises a
`SUPERVISED_REVERIFICATION` (same sealed instrument, same commit 573cfcb, same frozen
seeds, explicitly labelled, never presented as the first blind evaluation). PI's stated
vote: option A (authorise), not assumed. Comité 016 convened on exactly this question.
Anything building on the PASS (e.g. R-VAR V.2, [[pr003-fase3-lecam]]) carries the label.
Key sentence: relaunching can produce evidence, but cannot recreate the lost primary
evidence. R-VAR v2 spec (dev/PR003_R_VAR_SELECTOR_SPEC_V2.md) is written but NOT to be
executed before this procedural decision closes.

Related: comité 015 (`docs/comite/comite_decision_015_r-var-selector-adjudication.md`,
RECOMMEND_REVISE_AND_RECONVENE) conditions R-VAR spec v2 on this audit.

**CLOSED (2026-07-04): SUPERVISED_REVERIFICATION_MATCH.** Comité 016 recommended
`RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP` (option A); PI authorised in two steps —
(1) `docs/prereg002_reverification_declaration.md` committed first (predicate P, label
discipline, output routing, all fixed before launch, commit `f08bc04`), (2) launch itself
authorised explicitly afterward. Preflight required rebuilding `.venv` (the checked-in one
was broken — no `pyvenv.cfg`, no working pip); rebuilt from `requirements.txt`
(numpy==1.26.4, pytest==8.4.2), `make test` 28 passed. The rerun (`python -m
nachocausal.validate`, sealed, HEAD `f08bc04` — sealed subset byte-identical to `573cfcb`)
matched the `fee12d5` transcription on every field, no drift anywhere. Result:
`docs/prereg002_reverification_result.md`; checksums + provenance in git-ignored
`results/prereg002_reverification/`. **prereg-002's binding status everywhere it's cited is
now `PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]`** —
never bare "PASS", never "confirmed by re-running the blind evaluation". The MATCH verifies
the transcription is real (M); it does NOT restore the lost artifact or the historical
"first and only evaluation" claim (H) — that rests only on documentary/git evidence
(single introduction of `VALIDATION_DRAW_SEED` at `573cfcb`, no alternate value in history).
The virgin `VALIDATION_SEEDS` band is now permanently burned for any future protocol
comparison. R-VAR v2 (`dev/PR003_R_VAR_SELECTOR_SPEC_V2.md`) remains paused — this closure
resolves the artifact audit, not R-VAR's own open items (F1-F3, completion-class gap,
comité 015).

**Why:** the falsifier of comité 015 caught it; founding rule 1 requires artifact-level
backing for every published number.
**How to apply:** cite prereg-002 with the full bracketed status, and point to
`docs/prereg002_reverification_result.md` as the corroborating record, not just
`docs/preregistration_002_result.md` alone.
