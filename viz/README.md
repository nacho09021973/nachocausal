# `viz/` — pedagogical figures for the limits manuscript

> **STATUS: SUPPORTING_FIGURES / DOES_NOT_TOUCH_THE_SEAL / NO_VALIDATION_SEEDS /
> NO_RECONSTRUCTION_CLAIM.**
>
> These figures illustrate theorems and diagnostics already documented in
> `docs/manuscript_limits_draft.md`. They produce no new results, consume none of
> the reserved seed band
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
| 5 | `fig05_what_is_recoverable.py` | A scale-free statistic varies across a specified `r/r_s` patch family | partner of Fig. 2 |

Figures 2 and 5 are a pair and must travel together: Figure 2 visualizes the exact
co-scaling witness for absolute-scale blindness; Figure 5 shows that the comparable-
pair fraction varies with dimensionless patch placement in one specified family.
Figure 5 is illustrative: it does **not** establish identification of `r/r_s`,
injectivity beyond the plotted sweep, or horizon localization.

In the manuscript the images appear in argumentative order, so asset `fig05` is
publication Figure 3, asset `fig03` is publication Figure 4, and asset `fig04` is
publication Figure 5.

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
  discrepancies); otherwise it raises `AssertionError` instead of drawing something
  false.
- `fig03` verifies that both continuations leave the observed patch **identical**.

## A trap Figure 2 avoids, and that must keep being avoided

Theorem 3.1 is `TV = 0` between **laws**, not between realisations. Two *independent*
sprinklings at different masses do **not** give the same poset. What happens is that
`Φ_s` is an order isomorphism, so the same point set, transported, is a legitimate
sprinkling of the other model with the same relations — and the theorem is what makes
that construction generic rather than cherry-picked.

If a future version of the figure suggests "two independent draws came out equal", it
is asserting something false and must be rejected.

Figure 3 uses independent ensembles only to display agreement of Monte Carlo curves.
Its caption must report `N=60`, 80 repeats, and the fixed seed, and must say that the
observed variation does not prove recovery or localization. Figure 4's maximal-element
construction is a toy analogy for completion dependence, not the event horizon itself;
Figure 5's time-banded residual is a diagnostic, not recovered horizon physics.

Asset `fig04` separates its fixed-seed within-causet Pearson coefficient from two
deterministic quadrature targets: the window functional `Corr(p(X),t(X))` and the
finite-`n` tagged-element correlation. The exact attenuation formula applies to the
tagged marginal law, not identically to the dependent Pearson coefficient computed
inside one causet. No iid confidence interval is authorized for that internal
coefficient.
