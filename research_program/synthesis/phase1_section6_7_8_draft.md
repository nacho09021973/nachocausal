# Fase 1 · Paso 1.5 — Draft §6 literature + §7 open/abandoned + §8 conclusions

> **STATUS: MANUSCRIPT_SECTION_DRAFT / NOT_FROZEN / NO_NEW_SCIENCE /
> DOES_NOT_TOUCH_SEAL / DOES_NOT_DISCHARGE_ITEM_5.**
>
> Cierre del manuscript de límites. Outline:
> `phase1_limits_paper_outline.md` §6–§8. Merge ensamblado:
> `docs/manuscript_limits_draft.md`.
>
> FECHA: 2026-07-28 · HEAD de referencia: `36b1d6c`
> Gobernanza: N2/N5 not contributions; R1 abandoned north; ítem 5 hedge.

---

## §6 Relation to the literature
<!-- manuscript body -->

We place the three pillars against published work without converting background
into claimed novelty.

### 6.1 Order, number, and scale

The slogan that continuum Lorentzian geometry arises from causal order together
with counting information—“Order + Number equals Geometry”—is standard in causal
set theory (`[BACKGROUND]`; e.g.\ Dowker and Zalel, arXiv:1703.07556). Recent
work makes related statements mathematically precise for *labeled* random
adjacency matrices and related reconstruction settings (Braun, arXiv:2507.01907,
separating chronological isomorphy / conformal content from volume-preservation /
isometry). Madsen (arXiv:2607.05840) states explicitly that order alone is
“famously insufficient,” connecting that insufficiency to Müller’s negative
finite-order results.

Theorem 3.1 does not invent this slogan. It supplies an **exact finite-\(n\)**
total-variation statement for Poisson sprinklings of Schwarzschild patches under
dilation (and a scoped \(3{+}1\) co-scaling statement): absolute mass is
non-identifiable in the order-only fixed-\(n\) channel. Continuum precursors
include the conformal character of causal determination of the metric
(Hawking–King–McCarthy, J.\ Math.\ Phys.\ 17, 174, 1976; Malament, J.\ Math.\
Phys.\ 18, 1399, 1977) and dilatations among causal automorphisms of Minkowski
space (Zeeman, via Bombelli’s 1987 thesis). Those continuum facts motivate the
orbit; they are not a substitute for the sprinkling-channel TV calculation.

### 6.2 Indistinguishability of orders without rates

Müller (arXiv:2503.01719) constructs pairs of non-isometric Lorentzian geometries
that admit finite causal sets with nearly identical order laws at fixed
cardinality—precise negative results for naive formulations of the
Hauptvermutung. That work is the closest published *qualitative* neighbor of our
indistinguishability theme. It does not develop Fisher information, Le Cam
two-point rates, or localization floors for a continuous geometric parameter of a
Schwarzschild family. Theorem 3.8 lives in a different genre: a rate lower bound
on a proved-regular parametric family in the order-only channel.

### 6.3 Constructive geometric estimators

Boguñá and Krioukov (Phys.\ Rev.\ D 110, 024008, 2024) estimate spacelike
distances from causal overlaps with errors that vanish in a continuum limit, with
discreteness scales of the form \(\rho^{-1/(d+1)}\) in their conventions. Their
direction is complementary to Theorem 3.8: they give **constructive upper rates**
for geometric functionals; we give **estimator-independent lower bounds** on a
localization problem for a named family. Neither result implies the other.

### 6.4 Horizons and quasi-local structure in causal sets

Eichhorn, Gamito, and Stokes (arXiv:2605.06813) develop causal-set diagnostics
related to black-hole horizons and geodesic focusing, including ladder-based
proxies for expansion. That literature motivates why quasi-local horizon
structure is interesting and why continuum intuition is subtle in low dimension.
It does not supply, in our order-only finite-patch bank, a stable codimension-two
screen with order-only transport—the obstruction recorded for channel C6—or a
counterexample to Theorems 3.1–3.2. Benincasa–Dowker-type interval abundances and
related curvature observables target manifoldlikeness and scalar curvature, not
the abandoned region-localizer north of this paper. Graph-observable surveys of
configuration space (e.g.\ Eichhorn et al., arXiv:2605.27514) classify classes of
causal sets; they are orthogonal to our measure-theoretic non-identifiability
statements.

### 6.5 Statistical methods

Quadratic-mean differentiability, Hellinger tensorization, data processing, and
two-point (Le Cam) lower bounds are textbook
(`[BACKGROUND]`; e.g.\ van der Vaart, *Asymptotic Statistics*; Tsybakov,
*Introduction to Nonparametric Estimation*). Theorem 3.8’s claim to attention is
the **instantiation**: a geometric family for which regularity is proved and for
which several “natural” alternative families are degenerate or non-regular
(Section 3.3.1). We do not claim a new method of nonparametric statistics.
Novelty wording for that instantiation remains subject to an independent
literature check (project Paso D, item 5); absolute priority language is
disallowed until that check is complete.

### 6.6 What we do not cite as competition

We do not treat failures of particular estimators in the literature—or our own
ledger—as proofs of non-identifiability. Conversely, we do not treat continuum
reconstruction theorems under order+number hypotheses as refutations of
fixed-\(n\) order-only blindness for absolute mass.

---

## §7 What is closed, open, and abandoned
<!-- manuscript body -->

### 7.1 Closed in this paper

| Question | Status | Where |
|---|---|---|
| Absolute \(r_s\) / \(M\) from order-only data at fixed \(N=n\) (stated families) | **Non-identifiable** (\(\mathrm{TV}=0\) on the orbit) | Thm 3.1 · `PROVED_NON_IDENTIFIABILITY` |
| Global event horizon from a single finite patch | **Not a functional** of patch data | Thm 3.2 · `PROVED_NON_IDENTIFIABILITY` |
| Localization rate for \(\tau\) on the regular EF diamond family | **Floor** \(\sim n^{-1/2}\) | Thm 3.8 · `PROVED_NON_IDENTIFIABILITY` (rate) |
| Sealed future-volume in-patch score under prereg-002 | **PASS** (caveated artifact status) | §4 · `VALIDATED` (caveated) |
| Named region-localizers C1–C6 in this bank | **Terminated** as listed | §5 · `EMPIRICAL_FAILURE_OF_CLASS_L` |

### 7.2 Abandoned as program north

```text
ABANDONED_AS_PROGRAM_NORTH:
  further order-only region-locators aimed at Schwarzschild 3+1 horizon structure
  (global EH, trapping, codim-2 screen, or proxy) in the post-PR008 candidate line.
```

This is a **governance** closure for the reconstruction ambition under the
order-only finite-patch package (Fase 0, R1). It is justified jointly by
Theorems 3.1–3.2, the non-transfer of the \(1{+}1\) scalar proxy as a \(3{+}1\)
horizon locator, and the ledger—not by Theorem 3.1 alone, and not by the ledger
alone.

### 7.3 Open (legitimate next science)

| Item | Status | Preferred path |
|---|---|---|
| Pointwise \(I(\tau)>0\) at every \(\tau\) (only no vanishing on subintervals is proved) | `OPEN` | Analyticity route noted in annex; not required for Thm 3.8 |
| Numerical \(\bar I\) / \(\bar\kappa\) for reference diamonds | `OPEN` / NUMERICAL where marked | Deterministic generators only |
| Regular parametric family + Fisher floor in \(3{+}1\) | `OPEN` | Template from Thm 3.8; new proof required |
| Order+number with known \(\rho\): separation of absolute mass | Open as **new program** | OP-1.2 §5: Poisson means differ when \(M\) differs; not developed here (Fase 3 B1) |
| Witness-pair or rate no-go for a *named* quasi-local proxy \(Q\neq T_{\mathrm{EH}}\) | `OPEN` | Fase 3 **B2** (adversarial pairs)—preferred scientific sequel |
| Independent literature check for instantiation priority (Thm 3.8) | Pending | Paso D item 5; hedge until done |
| Ordering-fraction / Chebyshev TV lower separation for fixed pairs | Conditional | Only if project conditions C3–C4 (comité 045) are closed; omitted from claims until then |

### 7.4 Explicitly not claimed open problems

We do not list “find the observable that reconstructs the \(3{+}1\) event horizon
from finite order-only data” as an open problem of this program. That question is
abandoned as north (§7.2), not deferred.

---

## §8 Conclusions
<!-- manuscript body -->

We asked what a finite unlabeled causal set can identify about Schwarzschild
geometry when the observation is order-only—often conditioned on cardinality—and
when continuum labels are used only to score, never to define, the estimator.

**Pillar P1.** Three non-identifiability statements are proved. Absolute horizon
radius (mass) is invisible at fixed \(n\) along dilation and co-scaling orbits
(Theorem 3.1). The global event horizon is not a functional of finite-patch data
(Theorem 3.2). On a regular one-parameter family of \(1{+}1\) causal diamonds with
finite Fisher information, no order-only procedure localizes the continuous
parameter below a two-point rate of order \(n^{-1/2}\) (Theorem 3.8). These results
are labeled `PROVED_NON_IDENTIFIABILITY`. They are not failures of particular
estimators, and they are not a slogan that causal sets cannot see black holes.

**Pillar P3.** Under a frozen pre-registration, a future-volume observable passes a
sealed blind validation contract for in-patch localization of a horizon-associated
boundary score in \(1{+}1\) Schwarzschild, with supervised re-verification after loss
of the primary raw artifact. The result is labeled `VALIDATED` with explicit
caveats. It shows that the order-only channel is not empty. It does not reconstruct
a global event horizon and does not transfer by itself to \(3{+}1\).

**Pillar P2.** Six named region-localization constructions in the same bank
terminate with typed terminals. The ledger is labeled
`EMPIRICAL_FAILURE_OF_CLASS_L`. It is a result of the benchmark discipline; it is
not a minimax theorem and does not replace Section 3.

**Program reading.** The finite unlabeled order, on a patch and at fixed
cardinality, is not the channel with which one reconstructs a \(3{+}1\)
Schwarzschild event horizon. It is the channel with which one can prove, by
equality of laws and by definition of global objects, the limits of what that
experiment can see—and with which one can still validate bounded in-patch
recoverability of a carefully contracted geometric score. Further scientific work,
if any, should open a **new** contract (order+number; non-horizon targets;
adversarial pairs for named quasi-local proxies), not another estimator under the
abandoned region-localizer north.

---

## Acknowledgments / data availability (stub)

```text
[TO BE FILLED]
Code and sealed thresholds: repository nachocausal; seal verify via make verify-seal.
No new validation ensembles were generated for this manuscript draft.
Primary prereg-002 raw artifact status: as documented in §4.3.
```

## References (minimal working list for draft)

```text
[1] L. Bombelli, Space-time as a Causal Set, Ph.D. thesis, Syracuse University (1987).
[2] M. Boguñá, D. Krioukov, Phys. Rev. D 110, 024008 (2024).
[3] M. Braun, arXiv:2507.01907.
[4] F. Dowker, S. Zalel, arXiv:1703.07556.
[5] A. Eichhorn, P. Gamito, N. Stokes, arXiv:2605.06813.
[6] S.W. Hawking, A.R. King, P.J. McCarthy, J. Math. Phys. 17, 174 (1976).
[7] N. Madsen, arXiv:2607.05840.
[8] D.B. Malament, J. Math. Phys. 18, 1399 (1977).
[9] O. Müller, arXiv:2503.01719.
[10] A.B. Tsybakov, Introduction to Nonparametric Estimation, Springer (2009).
[11] A.W. van der Vaart, Asymptotic Statistics, Cambridge (1998).
```

Full bibliography to be expanded from `research_program/bibliography/` and
`biblioteca/` before any external circulation. All arXiv IDs used above were
cross-checked in the adversarial filter / local library where noted in
`tarea_grok_2.md`; do not invent additional identifiers in later edits.

---

## Checklist paso 1.5

```text
[x] §6.1 Order+Number / scale background
[x] §6.2 Müller neighbor (qualitative)
[x] §6.3 Boguñá–Krioukov complementary rates
[x] §6.4 EGS / BD context; no abandoned-north reopening
[x] §6.5 Textbook methods; ítem 5 hedge on Thm 3.8
[x] §7 closed / abandoned / open tables
[x] §8 conclusions P1–P3 + program sentence
[x] Merge pointer → docs/manuscript_limits_draft.md
[ ] PI review before external circulation
[ ] Paso 1.6 polish / dedupe on full merge
[ ] Paso 1.7 number audit
```
