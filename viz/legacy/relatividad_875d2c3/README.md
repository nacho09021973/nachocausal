# `viz/` — pedagogical figures for the limits manuscript

> **STATUS: SUPPORTING_FIGURES / DOES_NOT_TOUCH_THE_SEAL / NO_VALIDATION_SEEDS /
> NO_RECONSTRUCTION_CLAIM.**
>
> These figures illustrate theorems already proved in `docs/manuscript_limits_draft.md`.
> They produce no new results, consume none of the reserved seed band
> `[2,000,000–2,999,999]`, and do not touch `thresholds.py`.

## Why they exist

General relativity explains itself with the sagging rubber sheet. Causal sets are
always drawn one of two ways — abstract Hasse diagrams, or points in Minkowski with
light cones on top — and **neither shows what the order fails to see**, which is
precisely what this manuscript is about.

These five figures are aimed at a student, not a specialist. That choice **raises**
the accuracy bar rather than lowering it: an expert reads the caption and forgives an
imprecision; a student believes the picture literally.

## The figures

| # | File | What it shows | Anchor |
|---|---|---|---|
| 1 | `fig01_dictionary.py` | What is discarded in passing from spacetime to a causet | — |
| 2 | `fig02_invisible_scale.py` | Absolute scale is invisible to the order | Theorem 3.1 |
| 3 | `fig03_teleology.py` | What happens outside the patch is not in the patch | Theorem 3.2 |
| 4 | `fig04_box_wall.py` | Why the C1–C5 localisers died | acta 042 |
| 5 | `fig05_what_is_recoverable.py` | What the order **does** read: `r/r_s` | partner of Fig. 2 |

Figures 2 and 5 are a pair and must travel together: 2 says `r_s` is invisible, 5 says
`r/r_s` is not. Together they are the thesis of the manuscript in two images.

## Usage

```bash
python3 viz/make_figures.py     # writes all five to viz/output/ and prints their numbers
```

Every figure fixes its seed: two runs give byte-identical files. The numbers the
runner prints are the ones printed inside the panels; if they change, the manuscript
caption has stopped agreeing with the figure.

## Accuracy: why this is not decoration

Two properties of 1+1 Schwarzschild make the whole codebase exact and auditable at a
glance (`causet_core.py` documents them line by line):

1. **`det g = −1`**, so the volume form is `dt dr` and the sprinkling is **uniform on
   the `(t, r)` rectangle**. Any weighting in the code would be a bug.
2. With the tortoise coordinate `r* = r + r_s ln|r/r_s − 1|` the metric is conformally
   flat, so the causal order is **exactly** the product order in the null coordinates
   `(u, v) = (t − r*, t + r*)`. No geodesics are integrated, nothing is approximated.

Checks that run **before** drawing, and abort the figure if they fail:

- `fig02` verifies that `Φ_s` preserves the order **element by element** (0
  discrepancies over the **132 ordered pairs** of 12 elements — the 12 diagonal
  entries are forced `False` in both matrices and are not relations); otherwise it
  raises `AssertionError` instead of drawing something false.
- `fig03` verifies that both continuations leave the observed patch **identical**, and
  raises `RuntimeError` if it cannot find both.

`fig05` deliberately has **no** acceptance check. Its panel B illustrates an equality
that Theorem 3.1 proves; agreement within Monte Carlo error is "we did not detect a
difference", never "the curves are equivalent", and establishing equivalence would
need a margin fixed in advance — analysis this figure does not do and does not claim.
An earlier version printed "the gap must stay below the sd", a criterion nothing
enforced and whose scale was ~6× too lenient; it is gone (audit 035, E1/W4).

Uncertainties are labelled in the figure that shows them: `fig05` draws the **Monte
Carlo standard error of the mean** (`sd/√80`), not the single-realisation `sd`, and
`fig04` prints the sample size and the 95 % interval of both correlations — the band
one comes from `n = 22` and spans `[+0.05, +0.74]` (audit 035, W1).

## A trap Figure 2 avoids, and that must keep being avoided

Theorem 3.1 is `TV = 0` between **laws**, not between realisations. Two *independent*
sprinklings at different masses do **not** give the same poset. What happens is that
`Φ_s` is an order isomorphism, so the same point set, transported, is a legitimate
sprinkling of the other model with the same relations — and the theorem is what makes
that construction generic rather than cherry-picked.

If a future version of the figure suggests "two independent draws came out equal", it
is asserting something false and must be rejected.
