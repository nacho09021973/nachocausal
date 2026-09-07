# V4 PDF build recovery checkpoint

**PIPELINE_PROVENANCE: `RECONSTRUCTED_BY_GOLDEN_REPLAY`**

> This is **not** the original V3/V4 build pipeline. The original was ephemeral and
> could not be recovered. What is preserved here was reconstructed by replaying the
> golden Markdown until the output matched the golden PDF on every measurable
> feature listed below. Any resemblance to the original pipeline is inferred from
> output agreement, never from the original sources.

## Golden anchors (in Git, not duplicated here)

| Anchor | Value |
| --- | --- |
| Golden commit | `7ba3c04ccd50ea587c8d677d4709c7c27bfbe1ec` |
| Golden Spanish Markdown | `manuscrito/manuscrito_v4_es.md` @ `7ba3c04` |
| — sha256 | `99d28c92b9f064630d1a8ce4bed47024f18c24a154d0e24cfb889dee287d5326` |
| Golden Spanish PDF | `manuscrito/manuscrito_v4_es.pdf` @ `7ba3c04` |
| — sha256 | `f739e315507a87673c8736cd63da54e82afd9bd6d378f81d46880c767b3b0c42` |
| Engine | LuaHBTeX 1.17.0, TeX Live 2023/Debian, LaTeX2e 2023-11-01 patch level 1 |

The golden files are **deliberately not copied** into this directory. Retrieve them
with `git show 7ba3c04:manuscrito/manuscrito_v4_es.md` and
`git show 7ba3c04:manuscrito/manuscrito_v4_es.pdf`, then check the two sha256 above.
All three anchors were re-verified against the repository when this checkpoint was
written.

## What is preserved here

Eight artifacts, copied byte-for-byte from the replay tree, no edits:

| File | sha256 |
| --- | --- |
| `pipeline/md2tex.py` | `68ba5a190b59761ba3b6ff86e89a8e52058c4a76f34fe0510f51f8bb97df4618` |
| `pipeline/build.sh` | `80d8c0fef68ce3725f1df84df1a87fad5502493e9f5a7f94327811c71a8bcb88` |
| `pipeline/pdfgeom.py` | `d7b4f5fe713481ace52373812b45c241407eb95f2ceb2d7c261bdc0a1b1e4fc8` |
| `pipeline/compare.py` | `03e7843c21d77b34890212228bf43c02fa412300fc2379648b97aebd64fdb6a1` |
| `pipeline/imgdiff.py` | `2a93bf1efdd28fa6cd130aafd5f76e0453a431e3c3ff7a77e251a42b9dede0df` |
| `pipeline/verify.py` | `4cca53d636d04565203fad9ce9cce4277868547aaaf1bb4c3b9d9b3588c06db9` |
| `pipeline/pdfsig.py` | `05c03837d31e5599d4fa34f7a67603bb44a364e67c7156567400e7494acf31d9` |
| `pipeline/sigdiff.py` | `fa2cfce998d366db68046ecf7076a816826daf28e348db8b1064ab9feff44991` |

Excluded on purpose: `img/`, `build/`, `build_open/`, `build_diag/`, `probe/`,
`fixtures/`, logs, `.aux`/`.log`/`.out`, renders, replay/golden/scratch PDFs and TeX,
`md2tex_open.py` (refuted open-margin experiment), and `__pycache__`.

**Known limitation.** `build.sh` and `verify.py` hard-code the absolute path
`/tmp/nachocausal_v4_replay`. They were preserved unmodified so that provenance stays
exact; a future run must either recreate that directory or adjust the path. This is a
deliberate trade of convenience for byte-fidelity.

## Replay status: materially equivalent, not pixel-identical

Re-verified by `pipeline/verify.py` against the existing replay and golden PDFs when
this checkpoint was written (read-only comparison, nothing rebuilt):

| Check | Result |
| --- | --- |
| Page count | 18 vs 18 |
| Page size | 612.00 x 792.00 pt both |
| Equation tags | 70 in source, 0 missing from golden, 0 missing from replay |
| Bibliography | 20 entries, all present in both |
| Font families | match; 21 faces, all Type 1 Latin Modern + rsfs10/MSBM10/EUFM10 |
| Ink x-range | golden 68.02..540.01, replay 68.02..540.01 |
| Hyphen breaks | golden 1, replay 1 (the explicit hyphen in "real-analitica") |
| Text tokens | **11009 vs 11008**, similarity 0.99896, 10 hunks |
| Lines identical | **14/18** pages: 1-9, 14-18 |

From the replay build log (`lastrun.log`): overfull 0, undefined references 0,
undefined citations 0, missing characters 0, glyphs outside the page 0,
**underfull hboxes 2** (badness 1264 and 1337, both benign spacing warnings).

Two corrections to any looser summary of this state:

1. The text is **not** token-identical: 11009 vs 11008 tokens across 10 diff hunks.
   "Materially equivalent" is the accurate claim; "same textual content" is not.
2. `PAGES_LINE_CONTENT_IDENTICAL 14/18` means *line content* agrees, which is weaker
   than pixel identity. **No page has been established as pixel-identical.** The four
   pages that differ in line content are 10, 11, 12 and 13.

## Latest diagnosis (in progress, not concluded)

The first genuine mismatch was localised at the **closing glue of the proofblock**
environment.

| | Natural | Stretch | Shrink |
| --- | --- | --- | --- |
| Replay (current) | 9pt | 3pt | 5pt |
| Golden (inferred by tracing/geometry) | 9pt | 3pt | ~1pt |

The shrink model was reported to reproduce the observed page-11 divergence to within
approximately 0.004pt. `[UNVERIFIED]` — that figure comes from the tracing session's
console output; no artifact recording it survived into this checkpoint, and it was
not recomputed here.

**The shrink = 1pt fix has NOT been executed and is NOT validated.** It is the next
test, to be run scratch-only, never written into the manuscript source before it
passes.
