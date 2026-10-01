# Auditor Report 036 — viz-cierre-e1-y-avisos-035

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/ignac/nachocausal`, branch `emergencia/p1a-canal-sigma-m`, commit `534df4f`
(`viz: cierra E1 y los siete avisos de la auditoria 035`), parent `4959120`. Working tree clean.

**Focused re-audit**, scope fixed by the user: verify the closure of `E1` and of `W1`–`W7` of
report 035, and the absence of regression in what 035 passed (byte-for-byte reproducibility,
formal citations, seeds, seal, and that `viz/style.py` and `emergencia/` were not touched). The 23
pre-existing mechanical warnings remain **out of scope**; report 032 is their record.

Same declared deviation as reports 033–035: §7 counts only findings inside this scope.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh` — exit code `0`:

```text
Auditor: 0 error(s), 23 warning(s)
```

Unchanged across reports 032–036. No warning names `viz/`, `tests/` or `emergencia/`.

## 3. Seal & freeze integrity

```text
$ make verify-seal
thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4
```

Matches `docs/preregistration_002.md:8` and `docs/preregistration_003.md:9`. `534df4f` touches
nothing under `nachocausal/`. **Intact.**

## 4. Reproducibility of published numbers

**4.1 Reproducibility — unchanged and verified.** The suite was copied to `<scratchpad>/ra` and
run there; **no versioned file was overwritten**. All five PNGs produced in isolation are
`sha256`-identical to the committed ones, and a second in-place run reproduces them byte for byte.

**4.2 `E1` — CLOSED, and the substitution is the right one.** Verified numerically rather than by
reading:

```text
SE of the mean drawn = 0.00277  =  sd/sqrt(80) = 0.00277   (identical, elementwise)
largest gap 0.0101 = 1.89 SE of the difference
quoted factors: sd/SE_mean = 8.94 ("~9" in the README), sd/SE_diff = 6.33 ("~6")
```

`fig05_what_is_recoverable.py:77` computes `se1, se7 = s1/sqrt(REPEATS), …`; `:107-110` plots
those, not `s1`/`s7`. Both panels label the quantity (`:97-99`, `:119-121`). The acceptance
criterion is gone: `grep "must stay below"` over `viz/` returns nothing outside the docstring that
records its removal.

**Critically, the remediation did not take the shortcut the user warned against.** The figure does
not now assert that a contrast "passes". Panel B's own text (`:119-121`) reports the gap in SE of
the difference as a *diagnostic*; the footer (`:128-131`) states that the curves agree within
Monte Carlo error "which is not the same as establishing equivalence"; the docstring (`:24-28`)
says an equivalence claim would need a margin fixed in advance and that this figure does not do
that analysis. The runner (`make_figures.py:50-51`) repeats it. The branch chosen — illustrating
an analytically proved equality — is the correct one, and the audit confirmed the premise
independently: `sweep` fixes the patch shape in units of `r_s`, so under a common RNG stream the
`r_s = 7` experiment is the exact dilation of the `r_s = 1` one (identical order, identical
statistic, checked at `r/r_s = 1.05, 2.2, 9.0`). The equality is a theorem, not a measurement.

**4.3 `W1` — CLOSED, and the interval is not flattering.** `fig04_box_wall.py:49-58` implements
Fisher's `z` with `se = 1/sqrt(n-3)`; recomputed by hand, the figure's band interval
`[+0.0533, +0.7410]` matches exactly. Because Fisher's interval assumes bivariate normality and
`|J^+|` vs `r` is visibly non-normal, the auditor ran a 4000-resample bootstrap as a control:
`[+0.069, +0.721]`, i.e. **narrower** than the printed interval. The published interval is the
conservative one; no over-precision. Panel C now prints `n = 900` and `n = 22` alongside both
correlations, and the panel title reads "buried and **barely** recovered".

**4.4 `W2` — CLOSED.** `fig02_invisible_scale.py:65` computes `N*(N-1) = 132`; the drawn text
(`:127-130`) reads `0 discrepancies across the 132 ordered pairs of 12 elements`. The underlying
check still compares all 144 matrix entries, which implies the 132 — no inconsistency, and the
inflated denominator is gone.

**4.5 `W6` — CLOSED.** `fig04_box_wall.py:98` now draws `linear $R^2 = \rho^2 = 0.91$`; the
docstring `:10-15` states the quadratic fit reaches `0.93` and that adding `r` moves the joint
`R^2` from `0.905` to `0.912`. Both figures match the auditor's own recomputation in report 035
(`0.9053`, `0.9334`, `0.9122`). The unperformed variance decomposition is explicitly disclaimed.

**4.6 `W3`, `W5`, `W7` — CLOSED (text and drawing).** `fig01_dictionary.py:100-104` no longer
claims crossings are avoided; `fig02_invisible_scale.py:141-145` draws the laws-vs-realisations
caution inside the figure ("B is A transported by `Φ_s`, not a second draw…"), which is what
`viz/README.md:62-70` had required of any circulating version;
`fig03_teleology.py:88-93,112-117` offsets the added element and names the relation to `e` in
words in each panel. All three verified by opening the regenerated PNGs.

**4.7 `W4` — CLOSED**, jointly with E1 (§4.2).

## 5. dev/validation separation & ground-truth leakage

`git diff --stat 4959120 534df4f -- viz/style.py viz/causet_core.py emergencia/viz/
emergencia/resultados/` is **empty**: the shared style module, the geometry kernel, the
`emergencia` figure suite and every sealed artefact are untouched, exactly as the commit message
claims. The decision not to change `order_layout` (shared with `emergencia/viz/estilo.py`) is
recorded in the commit and is the reason `W3` was closed on the caption rather than the layout —
a defensible trade-off, since altering it would have forced a regeneration and re-audit of the
already-closed `emergencia` suite.

Seeds unchanged (`31415`, `20260806`, `2718`, `11`, `4242`); none in the reserved band
`[2 000 000 – 2 999 999]`. No new randomness introduced: `_fisher_ci` is arithmetic on already
computed quantities, and the bootstrap used for the §4.3 control was run by the auditor outside
the repo, not added to it. Ground truth still only scores; coordinates are used openly and by
design, and no figure lets one define or tune an order-theoretic observable.

## 6. Claim-boundary check

No over-claim introduced, and one removed. `fig05`'s panel B title now names Theorem 3.1 as the
source of the equality instead of implying the simulation established it, and every surface that
mentions the agreement pairs it with the statement that it is not equivalence
(`fig05_…py:26-28,129`; `make_figures.py:53`). `emergencia/HOJA_DE_RUTA.md` §21.2 carries a
qualification blockquote and §21.4 a status paragraph; `git diff` over that file shows **zero**
deleted lines, so the historical record was annotated, not rewritten — as instructed.

Nothing in the commit declares the figures fit for circulation; the commit message states the
opposite pending this re-audit.

**Finding 1 — WARNING (residual, deliberate).** `fig01` panel B remains the least legible object
in the suite: with most layers holding two elements, `order_layout` places them at `x = ±1` and
the poset renders as two distant columns joined by long crossing edges
(`viz/output/fig01_dictionary.png`). Report 035's `W3` offered two remediations — fix the layout
or soften the caption — and the caption was chosen, correctly and for a stated reason (the layout
lives in shared code). The text defect is therefore closed. The legibility defect is not, and it
sits in the panel whose whole purpose is to show *"what the order sees"*. Recorded so it does not
disappear from the ledger; it is a deferred improvement, not an oversight.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | WARN | `fig01` panel B legibility unresolved (two-column collapse, long crossings); `W3` closed on the caption because the layout lives in shared `viz/style.py` | `viz/output/fig01_dictionary.png`; `viz/style.py` `order_layout`; report 035 `W3` |
| 2 | OK | `E1` closed: bars are `sd/√80` exactly; gap reported as `1.89 SE` of the difference as a diagnostic; acceptance criterion removed; equivalence explicitly disclaimed in four places | §4.2; `fig05_…py:77,107-110,119-121,128-131`; `make_figures.py:50-53` |
| 3 | OK | The premise of the chosen remediation independently verified: the two sweeps sample the same law by exact dilation, so the equality is analytic | §4.2 |
| 4 | OK | `W1` closed: `n` and both 95 % intervals printed; Fisher interval `[+0.053,+0.741]` verified by hand and **wider** than a 4000-resample bootstrap `[+0.069,+0.721]` | §4.3; `fig04_box_wall.py:49-58,103-109` |
| 5 | OK | `W2` closed: `132 ordered pairs`, computed not asserted | §4.4; `fig02_…py:65,127-130` |
| 6 | OK | `W6` closed: "linear `R²`" drawn; quadratic `0.93` and joint `0.912` stated; decomposition disclaimed | §4.5; `fig04_box_wall.py:10-15,98` |
| 7 | OK | `W3`/`W5`/`W7` closed in text and drawing; the laws-vs-realisations caution now travels inside `fig02` | §4.6 |
| 8 | OK | `W4` closed: no unenforced criterion remains anywhere in `viz/` | §4.2 |
| 9 | OK | No regression: 5/5 byte-identical in isolation and in place; seal intact; `viz/style.py`, `viz/causet_core.py`, `emergencia/` diff empty; seeds unchanged | §4.1, §3, §5 |
| 10 | OK | Historical record annotated, not rewritten: zero deleted lines in `HOJA_DE_RUTA.md` | §6 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=1

## 8. Verdict

One of: `AUDIT_PASS` (no errors, no warnings), `AUDIT_PASS_WITH_WARNINGS` (no errors, ≥1 warning),
`AUDIT_FAIL` (≥1 error).
AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS

**`E1` is closed, and closed the right way.** The repair did not swap `sd` for `SE` and declare a
test passed — the failure mode the user flagged in advance. It re-founded the panel on what is
actually true: the equality is a theorem, the simulation illustrates it, and agreement within
Monte Carlo error is stated as a diagnostic that cannot establish equivalence. All seven warnings
are closed; the one that survives is a legibility item deliberately deferred because its fix lives
in code shared with an already-closed suite.

**No finding blocks circulation.** Nothing drawn is false or misleading, every number reproduces,
the seal is intact and the historical record was preserved. The remaining obstacle to
dissemination is not in this report: it is `HOJA_DE_RUTA.md` §21.4's own pending item — the five
figures are still not inserted into `docs/manuscript_limits_draft.md`, the manuscript that
`origin/main` `69bf65c` cleared for arXiv. That is a publication step, not an integrity defect.

Recommended, **not applied**:

1. When `emergencia/viz` next needs regeneration anyway, improve `order_layout` for narrow layers
   and regenerate both suites together, closing the `fig01` residual at no extra audit cost.
2. Insert the five figures into the manuscript with their captions, per §21.4, before external
   circulation.
