# RECOVERY_STATUS

Written 2026-09-07. Purpose: resume this work after `/tmp` is gone.

```
GOLDEN_COMMIT=7ba3c04ccd50ea587c8d677d4709c7c27bfbe1ec
GOLDEN_MD_SHA256=99d28c92b9f064630d1a8ce4bed47024f18c24a154d0e24cfb889dee287d5326
GOLDEN_PDF_SHA256=f739e315507a87673c8736cd63da54e82afd9bd6d378f81d46880c767b3b0c42
ENGINE=LuaHBTeX 1.17.0 / TeX Live 2023/Debian / LaTeX2e 2023-11-01 pl1
PIPELINE_PROVENANCE=RECONSTRUCTED_BY_GOLDEN_REPLAY

REPLAY_ES_BUILT=YES
REPLAY_ES_MATERIALLY_EQUIVALENT=YES
REPLAY_ES_PIXEL_IDENTICAL=NO

PIXEL_IDENTICAL_PAGES=NONE_ESTABLISHED
LINE_CONTENT_IDENTICAL_PAGES=14/18 (1-9, 14-18)
PAGES_DIFFERING=10, 11, 12, 13

SIGNIFICANT_VISUAL_DIFFERENCES=NONE_OBSERVED
  page geometry identical (18 pp, 612.00x792.00 pt)
  70/70 equation tags, 20/20 bibliography entries
  identical font families (21 Type 1 faces), identical ink x-range 68.02..540.01
  residual differences are page-breaking only, on pages 10-13
  text tokens 11009 vs 11008, similarity 0.99896, 10 hunks (NOT token-identical)
  build log: overfull 0, undefined refs 0, undefined cites 0,
             missing glyphs 0, glyphs outside page 0, underfull hboxes 2

ROOT_CAUSE_LATEST=proofblock closing glue
  replay  9pt plus 3pt minus 5pt
  golden  9pt plus 3pt minus ~1pt (inferred by tracing/geometry, not confirmed)
  shrink model reproduces the page-11 divergence to ~0.004pt [UNVERIFIED,
  reported by the tracing session, no surviving artifact, not recomputed here]

NEXT_TEST=proofblock closing glue shrink 5pt -> 1pt, scratch only
NEXT_TEST_STATUS=NOT_EXECUTED

CURRENT_MANUSCRIPT_FIXES=
  section 2  explicit definition of M_u, M_v, psi_U, psi_V
  section 5  explicit definition of G_full^(N)
  both applied to manuscrito_v4_es.md and manuscrito_v4_en.md, verified in the diff

SCIENTIFIC_ERRORS_OPEN=0
EDITORIAL_ERRORS_OPEN=0
EXTERNAL_DEPENDENCIES_UNVERIFIED=0
```

## How to resume

1. Recreate `/tmp/nachocausal_v4_replay` (both `build.sh` and `verify.py` hard-code
   that path) and copy `pipeline/` back into it.
2. Restore the golden pair from Git and check the two sha256 above:
   `git show 7ba3c04:manuscrito/manuscrito_v4_es.md > golden_v4_es.md`
   `git show 7ba3c04:manuscrito/manuscrito_v4_es.pdf > golden_v4_es.pdf`
3. `bash pipeline/build.sh` to regenerate `replay_v4_es.pdf`.
4. `python3 pipeline/verify.py` and expect the scoreboard above, in particular
   `PAGES_LINE_CONTENT_IDENTICAL 14/18`. Any drop from 14/18 means the environment
   drifted; fix that before touching the glue.
5. Only then run the pending shrink test, in scratch, and compare pages 10-13.

## Scope of this checkpoint

Preservation only. No result was regenerated, no manuscript text was changed beyond
the two referee fixes already in the working tree, and no claim of pixel identity is
made anywhere in this directory.
