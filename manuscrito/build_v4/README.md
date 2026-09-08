# V4 reproducible PDF build

PIPELINE_PROVENANCE=RECONSTRUCTED_BY_GOLDEN_REPLAY

This is not the original V3/V4 build pipeline. The original pipeline was not
recovered. This stable pipeline was reconstructed by golden replay and is kept
only because its Spanish replay matched the measurable golden anchors closely
enough for the MATERIALMENTE EQUIVALENTE criterion.

## Golden anchors

| Anchor | Value |
| --- | --- |
| Golden commit | `7ba3c04ccd50ea587c8d677d4709c7c27bfbe1ec` |
| Golden Spanish Markdown sha256 | `99d28c92b9f064630d1a8ce4bed47024f18c24a154d0e24cfb889dee287d5326` |
| Golden Spanish PDF sha256 | `f739e315507a87673c8736cd63da54e82afd9bd6d378f81d46880c767b3b0c42` |
| Engine | LuaHBTeX 1.17.0 / TeX Live 2023/Debian |

Golden files are not copied into this directory. Retrieve them, when needed,
with:

```bash
git show 7ba3c04ccd50ea587c8d677d4709c7c27bfbe1ec:manuscrito/manuscrito_v4_es.md
git show 7ba3c04ccd50ea587c8d677d4709c7c27bfbe1ec:manuscrito/manuscrito_v4_es.pdf
```

## Build

Run from the repository root:

```bash
manuscrito/build_v4/build.sh manuscrito/manuscrito_v4_es.md
manuscrito/build_v4/build.sh manuscrito/manuscrito_v4_en.md
```

The resulting PDFs are written next to their source Markdown files:

```text
manuscrito/manuscrito_v4_es.pdf
manuscrito/manuscrito_v4_en.pdf
```

Intermediate TeX and LaTeX logs are written under `manuscrito/build_v4/out/`.
They are build products and are not part of the committed pipeline.

## Verification

After building both languages, run:

```bash
manuscrito/build_v4/verify.py
```

The final acceptance checks are: letter page size (`612x792 pt`), 70 equation
tags, 20 bibliography entries, no overfull boxes, no undefined references or
citations, no missing glyphs, no glyphs outside the page, and presence in the
extracted PDFs of the two frozen textual corrections and the required manuscript
anchors.

Underfull boxes from the final LaTeX logs are benign for this build.

## TeX packages

The build requires LuaHBTeX from TeX Live 2023/Debian and the LaTeX packages
used by the reconstructed preamble:

- `amsmath`
- `amssymb`
- `amsthm`
- `booktabs`
- `etoolbox`
- `fontenc`
- `geometry`
- `hyperref`
- `inputenc`
- `lmodern`
- `mathrsfs`
- `newunicodechar`
- `textcomp`
- `url`

No `texlive-lang-spanish` dependency is required for the replay behavior; the
pipeline disables pattern hyphenation explicitly to preserve the reconstructed
golden layout.
