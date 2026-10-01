# Auditor Report 035 — viz-figuras-generales-6-agosto

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

- **HEAD** `4959120295e82f571fb224df3d8d81898bc5cc11`, branch `emergencia/p1a-canal-sigma-m`.
- **Initial state**: `git status --short` empty (clean tree). Nothing of the user's was pending.
- **Temporal scope**: artefacts created or modified on **2026-08-06**. `git log --since
  2026-08-06 --until 2026-08-07` returns exactly four commits:

```text
f440fa7 2026-08-06 18:38  emergencia: registra en §21 que las figuras del manuscrito estan listas
0f6e8a6 2026-08-06 18:17  viz: translate the figure suite to English for the manuscript
e4eb5d5 2026-08-06 17:55  viz: cinco figuras pedagogicas para el manuscrito de limites
7fe36ca 2026-08-06 16:57  emergencia: registra en §20 el cierre del tramo covtree
```

**Resolution of "figuras generales".** Unambiguous from the history: the only figures created or
modified that day are the **five figures of `viz/`** — the limits-manuscript suite — introduced in
`e4eb5d5` and renamed/translated in `0f6e8a6`. `f440fa7` and `7fe36ca` touch only
`emergencia/HOJA_DE_RUTA.md` (no figure). The six `emergencia/viz/` figures are dated 2026-08-07
and are covered by reports 032–034; they are excluded here **except** for the shared code they
inherit, `viz/style.py`, which `emergencia/viz/estilo.py` imports and which therefore is in scope.
No ambiguity remained, so the audit proceeded without asking the user to delimit.

### Closed manifest

| # | Figure (artefact) | Generator | Inputs | Governing source |
|---|---|---|---|---|
| 1 | `viz/output/fig01_dictionary.png` | `viz/fig01_dictionary.py` (SEED 31415, N=13) | none (self-generated geometry) | conceptual; `CLAUDE.md` "order-only = blind to embedding" |
| 2 | `viz/output/fig02_invisible_scale.png` | `viz/fig02_invisible_scale.py` (SEED 20260806, N=12, s=2) | none | Theorem 3.1, `docs/manuscript_limits_draft.md:245` |
| 3 | `viz/output/fig03_teleology.png` | `viz/fig03_teleology.py` (SEED 2718, N=9) | none | Theorem 3.2, `docs/manuscript_limits_draft.md:125`; `dev/PR003_INFINITE_MAXIMALITY_NONCERTIFIABILITY.md:21` `VERDICT = PROVED` |
| 4 | `viz/output/fig04_box_wall.png` | `viz/fig04_box_wall.py` (SEED 11, N=900) | none | `docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md` |
| 5 | `viz/output/fig05_what_is_recoverable.png` | `viz/fig05_what_is_recoverable.py` (SEED 4242, 60 pts × 80 repeats × 11 positions × 2 masses) | none | partner of Theorem 3.1 |
| — | shared kernel | `viz/causet_core.py`, `viz/style.py`, runner `viz/make_figures.py` | — | `viz/README.md`; `emergencia/HOJA_DE_RUTA.md` §21 |

All five are **self-generating**: they read no CSV and no sealed artefact. Their "input" is the
1+1 Schwarzschild geometry implemented in `causet_core.py`, which is exact
(`det g = -1` ⟹ uniform sprinkling on the `(t,r)` rectangle; tortoise ⟹ causal order = product
order in `(u,v)`). Both properties were checked against the code and hold.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh` — exit code `0`:

```text
Auditor: 0 error(s), 23 warning(s)
```

All 23 are `committed data file with no generator reference` under `data/reports/` and
`evidence/`. None concerns `viz/`. They are classified `PREEXISTING_OUT_OF_SCOPE` (§8) and are
not re-litigated here; report 032 §2 holds the verbatim list.

## 3. Seal & freeze integrity

```text
git status --short                       -> (empty)
git rev-parse HEAD                       -> 4959120…
make verify-seal                         -> thresholds.py sha256: 6e2c3888…
cp -r viz/*.py viz/README.md <tmp>/vizrepro && python3 make_figures.py   (isolated; nothing versioned overwritten)
sha256sum <repo PNG> vs <tmp PNG>        -> 5/5 IDENTICAL
python3 make_figures.py (2nd run, tmp)   -> 5/5 OK (byte-identical)
```

Runner output in the isolated copy, verbatim:

```text
fig02  invisible scale          order discrepancies = 0   (must be 0)
fig03  teleology                patch verified identical in both continuations
fig04  box wall                 corr(|J+|,t) = -0.951   corr(|J+|,r) = +0.164   band corr = +0.465
fig05  what is recoverable      |rs=1 - rs=7| max = 0.0101   typical sd = 0.0248   (the gap must stay below the sd)
```

Auditor's independent recomputation, using only the modules' own `build()`/`sweep()` functions:

```text
FIG04  corr(|J+|,t)=-0.951468  ct^2=0.905291 -> panel prints 91 %
FIG04  corr(|J+|,r)=+0.163944  cr^2=0.026878   band corr=+0.464512   band n = 22 of 900
FIG04  band Fisher 95% CI = [+0.053, +0.741]   whole patch CI = [+0.100, +0.227]
FIG04  R2 linear(t)=0.9053   R2 quadratic(t)=0.9334   R2 joint(t,r)=0.9122
FIG02  N=12  matrix entries=144  off-diagonal ordered pairs=132  discrepancies=0
FIG05  sd of ONE realisation = 0.0248 (what the figure draws and prints)
FIG05  SE of the DIFFERENCE of means = 0.00391  (6.3x smaller); SE of one mean = 0.00277 (8.9x smaller)
FIG05  max gap = 0.0101 at r/rs = 1.15 -> z = 1.89;  0 of 11 points exceed |z| = 1.96
```

## 4. Reproducibility of published numbers

| Figure | Number drawn | Traced to | Auditor's status |
|---|---|---|---|
| 2 | `0 discrepancies` | `check_dilation_identity`, `causet_core.py:118-130` | **Reproduced** (0). Denominator mislabelled — see W2 |
| 2 | `12×12 relations` | `fig02_invisible_scale.py:124` | **Auditor reconstruction**: 144 entries, of which 12 are the forced-False diagonal; 132 are relations |
| 4 | `ρ = -0.951` | `fig04_box_wall.py:52` | **Reproduced** exactly (`-0.951468`) |
| 4 | `91 % of the variance` | `fig04_box_wall.py:76` (`100·ρ²`) | **Reproduced** (90.53 % → prints 91). Linear R² of a non-linear relation — see W6 |
| 4 | `ρ = +0.164` (whole patch) | `fig04_box_wall.py:52` | **Reproduced** (`+0.163944`), n=900, CI [+0.100,+0.227] |
| 4 | `ρ = +0.465` (band) | `fig04_box_wall.py:53,85` | **Reproduced** (`+0.464512`), but n=22 and CI [+0.053,+0.741] undisclosed — see W1 |
| 5 | `largest discrepancy 0.010` | `fig05_…py:94` | **Reproduced** (`0.0101`) |
| 5 | `typical sd ≈ 0.025` | `fig05_…py:94` (`s1.mean()`) | **Reproduced** (`0.0248`) — but it is not the uncertainty of the compared quantity: see E1 |
| 3 | "patch identical in both continuations" | `fig03_teleology.py:78-81` (raises otherwise) | **Verified**: the check runs and is enforced |
| 1 | — (no numbers drawn) | — | n/a |

No number drawn in any of the five figures lacks a committed generator, and every one of them was
reproduced by this audit.

## 5. dev/validation separation & ground-truth leakage

- **Byte-for-byte reproducible: yes, 5/5.** The suite was copied to
  `<scratchpad>/vizrepro` and run there; **no versioned file was overwritten**. The five PNGs
  produced there are `sha256`-identical to the committed ones, and a second run in the same
  isolated copy reproduces them again. No blockage to record.
- **Hashes**: the `viz/` suite carries no `.sha256` sidecars (unlike `emergencia/resultados/`);
  its integrity mechanism is regeneration, which was exercised here and passed.
- **Seeds**: `31415`, `20260806`, `2718`, `11`, `4242`. None lies in the reserved band
  `[2 000 000 – 2 999 999]` (`viz/README.md:8`; `docs/program_closure_note_2026-07-30.md:136`).
  All five are **analytic** seeds (they generate the sprinklings themselves); unlike
  `emergencia/viz/fig03`, none is a jitter-only seed. `viz/style.py` uses no randomness.
- **Hidden truth**: these figures illustrate theorems, they do not score an estimator. Coordinates
  `(t, r)` are used openly and by design — that is fig01's whole subject — and no figure uses a
  coordinate to define, select or tune an order-theoretic observable. `fig01`'s witness `p` is
  chosen from `rel` alone (`fig01_dictionary.py:36-39`); `fig03`'s witness `e` from `rel` alone
  (`fig03_teleology.py:53-56`). No violation.
- **Seal**: `make verify-seal` → `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`,
  matching `docs/preregistration_002.md:8` and `docs/preregistration_003.md:9`. Neither `e4eb5d5`
  nor `0f6e8a6` touches anything under `nachocausal/`. **Intact.**

## 6. Claim-boundary check

### E1 — `ERROR` — fig05 panel B: the drawn uncertainty is not the uncertainty of the compared quantity, and is unlabelled

- **Evidence**: `viz/fig05_what_is_recoverable.py:81,83` — `axB.errorbar(XS, m1, yerr=s1, …)`,
  `axB.errorbar(XS, m7, yerr=s7, …)`. `m1`, `m7` are **means over 80 repeats**
  (`fig05_…py:36-46`); `s1`, `s7` are the **standard deviations of a single realisation**
  (`vals.std()`, `:44`). The panel text `:94` states `largest discrepancy: 0.010 (typical sd ≈
  0.025)` and `viz/make_figures.py:49` prints `(the gap must stay below the sd)`.
- **Observed value**: bars of half-width `0.0248` drawn on points whose own standard error is
  `0.00277`, in a comparison whose relevant scale is the SE of the difference, `0.00391`.
- **Required condition**: error bars on a plotted mean must represent the uncertainty of that
  mean (or be labelled as spread); an agreement claim must be judged against the SE of the
  difference. The drawn bars are **8.9×** too large for the first and the stated yardstick is
  **6.3×** too lenient for the second. Neither the bars nor the band in panel A is labelled
  anywhere in the figure.
- **Impact**: panel B's entire claim — its title is *"multiplying the mass by seven does not move
  the curve"* — is visually carried by overlapping bars that overstate the strength of the
  agreement test by roughly an order of magnitude. **The scientific conclusion is not affected**:
  the auditor ran the correct test and it also passes (max `|z| = 1.89` at `r/r_s = 1.15`, `0` of
  `11` points beyond `1.96`), and Theorem 3.1 guarantees the two laws are identical anyway. It is
  classified `ERROR` and not `WARNING` because the defect is in drawn content that misrepresents
  the evidence, and the taxonomy forbids downgrading on the grounds that the present data happen
  to give the right answer.

### W1 — `WARNING` — fig04: the band correlation hides its sample size and its width

- **Evidence**: `viz/fig04_box_wall.py:35` `BAND = (2.9, 3.1)`, `:85` legend
  `band only ($\rho=+0.465$)`, drawn beside `whole patch ($\rho=+0.164$)`.
- **Observed**: band `n = 22` of `900`; Fisher 95 % CI `[+0.053, +0.741]`, against `[+0.100,
  +0.227]` for the whole patch.
- **Required**: two correlations presented side by side as commensurable should disclose their
  sample sizes, or their intervals.
- **Impact**: the CI excludes zero, so the figure's claim ("the physics, buried and recovered")
  is supported — but only just, and far more weakly than the bare `+0.465` suggests next to an
  `n = 900` number. `emergencia/HOJA_DE_RUTA.md` §21.2 and the `e4eb5d5` commit message elevate
  this value to a headline ("la física sólo reaparece al condicionar a una banda temporal
  estrecha") without the interval. Visual inspection of panel C reinforces the concern: the 22
  band points rise to `r ≈ 2` and then flatten or fall, so a single linear `ρ` is a generous
  summary of them.

### W2 — `WARNING` — fig02: the denominator "12×12 relations" is not an enumeration of relations

- **Evidence**: `viz/fig02_invisible_scale.py:122-125`, drawn text
  `identical element by element: 0 discrepancies across 12×12 relations`; replicated in
  `emergencia/HOJA_DE_RUTA.md` §21.2 ("0 discrepancias de orden en 12×12 relaciones").
- **Observed**: `144`. Of those, the `12` diagonal entries are set to `False` unconditionally by
  `causet_core.py:104` (`np.fill_diagonal(le, False)`) in **both** matrices, so they can never
  differ; the enumerable relations are the `132` ordered off-diagonal pairs.
- **Impact**: the strength of the check is inflated by 12 slots that are true by construction.
  The check itself is sound and its result (`0`) is correct.

### W3 — `WARNING` — fig01 panel B: the drawn caption is not borne out by the drawing

- **Evidence**: `viz/fig01_dictionary.py:100-102`, caption *"Vertical height in B is height in
  the order. Horizontal position only avoids crossings: it means nothing."* Layout by
  `viz/style.py` `order_layout` (barycentre heuristic, 6 sweeps).
- **Observed** (visual inspection of `viz/output/fig01_dictionary.png`): with most layers holding
  exactly two elements, the heuristic places them at the extreme `x = ±1`, collapsing the poset
  into two far-apart columns joined by long edges; roughly six edge crossings remain.
- **Impact**: no false statement of fact, but the panel that is supposed to show *"what the order
  sees"* is the least legible object in the suite, and its caption asserts a crossing-avoidance
  that the image visibly does not achieve. Pedagogical cost in the figure whose audience the
  README says raises the accuracy bar.

### W4 — `WARNING` — fig05: a stated acceptance criterion that no code enforces

- **Evidence**: `viz/make_figures.py:49` prints `(the gap must stay below the sd)`. No `raise`,
  `assert` or comparison exists anywhere in `viz/fig05_what_is_recoverable.py`.
- **Required**: `viz/README.md` records that `fig02` and `fig03` abort on a failed check; `fig05`
  advertises a criterion with no mechanism behind it.
- **Impact**: a guardrail that cannot fail is decoration. Compounded by E1, the advertised
  criterion is also the wrong one.

### W5 — `WARNING` — the trap the README says must never be reintroduced is undefended in the artefact

- **Evidence**: `viz/README.md:62-70` ("A trap Figure 2 avoids… If a future version of the figure
  suggests *two independent draws came out equal*, it is asserting something false"). The drawn
  `fig02` carries no such caution; the mitigation ("every node is at once a point of A (fill) and
  one of B (ring)") is indirect. Meanwhile `fig05` panel B advertises *"independent
  sprinklings"* in its own legend.
- **Context**: `emergencia/HOJA_DE_RUTA.md` §21.4 lists insertion of the five figures into
  `docs/manuscript_limits_draft.md` — with the laws-vs-realisations caption — as **pending**; a
  grep of the manuscript confirms no figure is referenced in it. On `origin/main`, commit
  `69bf65c` of the same day (2026-08-06 19:23) **withdrew the `NOT_FOR_ARXIV` token** from that
  manuscript.
- **Impact**: the five PNGs are standalone artefacts, adjacent to a manuscript now cleared for
  external circulation, and the caption that the project itself designated as the referee-facing
  safeguard does not exist yet. Nothing false is drawn; the safeguard is simply absent.

### W6 — `WARNING` — fig04: "explains X % of the variance" is a linear R², stated as a decomposition

- **Evidence**: `viz/fig04_box_wall.py:76` draws `the box explains {100·ρ²} % of the variance`;
  the docstring `:10-11` adds "radius explains ~3 %".
- **Observed**: `ρ²(t) = 0.9053`; a quadratic fit in `t` gives `0.9334`; the joint linear fit on
  `(t, r)` gives `0.9122`, so `r`'s incremental share is `≈ 0.7 %`, not `2.7 %`.
- **Impact**: the wording implies a variance decomposition that was not performed. The direction
  is conservative for the figure's thesis (the true dependence on `t` is stronger than 91 %), so
  no conclusion is overstated; the phrasing is.

### W7 — `WARNING` — fig03: the future/spacelike contrast is carried by one hard-to-see edge

- **Evidence**: `viz/fig03_teleology.py:95-110`; visual inspection of
  `viz/output/fig03_teleology.png`, panel 3.
- **Observed**: in continuation 2 the new element is drawn at the same visual height as `e` and
  linked by two long crossing edges to lower elements. The only cue distinguishing it from
  continuation 1 is the **absence** of a purple edge to `e`.
- **Impact**: a reader can misread the new element as sitting above `e`, i.e. as contradicting
  the panel's own verdict "e IS maximal". The underlying construction is correct and enforced:
  the auditor verified that a later-band point can never precede `e` (`t_q > 3.2 ≥ t_e` forces
  `u` or `v` to increase), so `beside` is genuinely spacelike, and `fig03_teleology.py:78-81`
  raises if either continuation perturbs the induced patch.

### Visual verification

Each PNG was opened and inspected.

| Figure | Labels / legends | Colour & scale | Visual vs logical order | Verdict |
|---|---|---|---|---|
| 1 | legend complete; no clipping | Okabe–Ito, consistent | panel B degenerate, ~6 crossings | **W3** |
| 2 | A/B ranges verified as exact `×2` of one another; no clipping | fill = A, ring = B, matches text | panel D Hasse legible | **W2** (caption denominator) |
| 3 | verdicts legible and colour-coded | purple = added element, consistent | panel 3 ambiguity | **W7** |
| 4 | "band" label tight over the shaded band but legible; colourbar fine | viridis for `\|J^+\|`, ordered | gradient vertical, as the text says | **W1**, **W6** |
| 5 | **error bars unlabelled in both panels**; log `x` axis correctly ticked | consistent | curves overlap as claimed | **E1** |

No clipped text, no colour that confuses categories, no axis that exaggerates a difference. The
one visual element that misleads is the unlabelled error bar of fig05 (E1), which does the
opposite — it makes an agreement look better founded than the drawn statistic supports.

## 7. Findings

| Class | Count | Items |
|---|---|---|
| `ERROR` | 1 | E1 (fig05 error bars / yardstick) |
| `WARNING` | 7 | W1 … W7 |
| `PREEXISTING_OUT_OF_SCOPE` | 23 | the mechanical warnings of §2, all under `data/reports/` and `evidence/`, none touching `viz/`; recorded in report 032 |

Procedural comparison with the `emergencia` chain, since that is what motivated this audit: the
defect class that produced report 032's error — **a quantity plotted or compared against a
yardstick that belongs to a different magnitude** — is present here too, as E1. The second class
— **counts and bounds stated more tightly than their enumeration or input precision supports** —
is present as W2 and W6. The third — **a stated criterion with no enforcement** — is present as
W4, and is worse here than in `emergencia/viz`, where every advertised check was demonstrated to
fire.

AUDIT_ERRORS=1
AUDIT_WARNINGS=7

## 8. Verdict

One of: `AUDIT_PASS` (no errors, no warnings), `AUDIT_PASS_WITH_WARNINGS` (no errors, ≥1 warning),
`AUDIT_FAIL` (≥1 error).
AUDIT_VERDICT=AUDIT_FAIL

**The five figures are not fit for circulation while E1 stands.** No number in the suite is
unreproducible, no theorem is misattributed, the seal is intact and every figure regenerates
byte-for-byte; the failure is one panel whose drawn uncertainty misrepresents the strength of its
own evidence, in the figure that the project designates as the partner carrying half its thesis.

### Recommended repairs — NOT APPLIED

1. **E1** — in `fig05_what_is_recoverable.py`, either plot `s1/√REPEATS` (the SE of the mean) and
   label the bars, or keep the sd and label it explicitly as single-realisation spread while
   adding the correct comparison; replace the printed yardstick in `make_figures.py:49` with the
   SE of the difference (`0.0039`), and make it an enforced check that aborts, as `fig02` and
   `fig03` do.
2. **W1** — print `n` and the Fisher interval next to the band correlation in
   `fig04_box_wall.py:85`, and qualify §21.2 of `HOJA_DE_RUTA.md` accordingly.
3. **W2** — say `132 ordered pairs` (or `12×12 matrix entries`) in `fig02_invisible_scale.py:124`
   and in §21.2.
4. **W3** — improve `order_layout` for narrow layers, or soften the caption to describe intent.
5. **W4** — see 1.
6. **W5** — insert the five figures into `docs/manuscript_limits_draft.md` with the
   laws-vs-realisations caption before any external circulation, as §21.4 already requires; or
   add the caution to `fig02` itself.
7. **W6** — say "linear R²" and drop or recompute the "radius explains ~3 %" claim.
8. **W7** — draw the spacelike element at a distinct horizontal offset, or annotate the absence of
   a relation to `e` explicitly.

Nothing in this report has been applied. The only file this audit wrote is the report itself.
