# Fase 1 · Paso 1.3 — Draft abstract + §1 + §2

> **STATUS: MANUSCRIPT_SECTION_DRAFT / NOT_FROZEN / NO_NEW_SCIENCE /
> DOES_NOT_TOUCH_SEAL / DOES_NOT_DISCHARGE_ITEM_5.**
>
> Completa el front matter del paper de límites junto a
> `phase1_section3_nonidentifiability_draft.md` (§3). Outline autoritativo:
> `phase1_limits_paper_outline.md`.
>
> FECHA: 2026-07-28 · HEAD de referencia: `239dc59`
> Gobernanza: Fase 0 R1–R3; `NO_RECONSTRUCTION_CLAIM`.

**Convenciones** (igual que el draft §3): `[PROVED]`, `[BACKGROUND]`, `[REMARK]`,
`PROVED_NON_IDENTIFIABILITY`, `EMPIRICAL_FAILURE_OF_CLASS_L`, `VALIDATED`.

---

## Title block (working)

**Title.**  
Finite order-only observation of Schwarzschild patches: exact scale blindness,
localization floors, and a typed ledger of failed region-locators

**Running subtitle / footnote.**  
A recoverability-limits paper — not a path to 3+1 event-horizon reconstruction
from finite unlabeled order.

---

## Abstract
<!-- manuscript body -->

We study what can and cannot be recovered from the isomorphism class of a finite
causal set obtained by Poisson sprinkling into a Schwarzschild region, when only
the unlabeled causal order is observed—typically conditioned on cardinality
\(N=n\). We prove three non-identifiability statements. First, absolute mass
(horizon radius in absolute units) is exactly non-identifiable at fixed \(n\)
under patch-shape-preserving dilations in \(1{+}1\) dimensions and under
co-scaling in a scoped \(3{+}1\) class: the total variation between the induced
poset laws vanishes on the entire mass orbit. Second, the global event horizon of
a spacetime is not a functional of any observation determined by a single finite
patch. Third, in a regular one-parameter family of \(1{+}1\) causal diamonds with
fixed Eddington–Finkelstein corners and finite Fisher information, no order-only
procedure can localize the continuous geometric parameter below a two-point rate
of order \(n^{-1/2}\). These limits are measure-theoretic or definitional; they do
not depend on the success or failure of particular estimators. Separately, we
record a sealed in-patch recoverability result for a future-volume observable
under a frozen pre-registration, and a typed ledger of six exhausted
region-localization channels in the same \(1{+}1\) bank, labeled as empirical
failure of a named construction class rather than as a universal no-go. The paper
is a recoverability benchmark and a map of channel limits. It is not a claim that
black-hole horizons have been reconstructed from causal sets, and it is not a
pathway to \(3{+}1\) event-horizon reconstruction from finite order-only data
alone.

**Keywords.** causal sets; order-only observation; Schwarzschild; identifiability;
total variation; Fisher information; recoverability benchmark; event horizon
(teleology)

---

## §1 Introduction and claim grammar
<!-- manuscript body -->

### 1.1 Recoverability, not reconstruction

Causal set theory proposes that continuum Lorentzian geometry is recovered, in a
suitable limit, from a locally finite partial order together with counting
information—the slogan “Order + Number equals Geometry”
(`[BACKGROUND]`; e.g.\ Dowker–Zalel, arXiv:1703.07556). The present work does
**not** attempt continuum reconstruction of a black-hole spacetime. It asks a
narrower, finite-sample question:

> Given only the isomorphism class of a finite causal set sprinkled into a
> Schwarzschild *patch*, which geometric targets are identifiable, at what rate,
> and which targets are information-theoretically or definitionally out of reach?

We call affirmative answers under a frozen protocol *recoverability* results, and
negative answers that apply to **all** measurable functions of the observation
*non-identifiability* results. We reserve the word *reconstruction* for structural
recovery of continuum geometry; that word does not appear as a claim in this paper
(`NO_RECONSTRUCTION_CLAIM`; program claim grammar
`docs/claim_grammar.md`).

### 1.2 The observation channel

A *completion* is a Lorentzian region of finite volume equipped with a Poisson
point process of intensity \(\rho\) with respect to the volume measure. The
induced causal set is the set of points ordered by the manifold’s causal
relation. Two observation models must be kept distinct
(`[PROVED]` setup lemmas: `first_witness_pair_candidates.md` §1):

| Channel | Observation | Role in this paper |
|---|---|---|
| **Order-only, fixed \(n\)** | Isomorphism class of the poset conditioned on \(N=n\) | Primary channel for Theorems 3.1 and 3.8 |
| **Order+number** | Joint law of order and cardinality (e.g.\ \(N\sim\mathrm{Poisson}(\rho V)\) with \(\rho\) known) | Contrast only: scale can re-enter through \(N\) (Remark after Thm 3.1) |

Conditioning on \(N=n\) removes the total-volume leak through cardinality: the \(n\)
points are i.i.d.\ from the normalized volume measure. Absolute scale is then
precisely what a constant conformal (or co-scaling) orbit can hide; that is the
content of Theorem 3.1, not an artifact of a bad estimator.

### 1.3 Hidden embeddings score only

Wherever a numerical benchmark is reported, continuum embeddings and horizon
labels are used **only to score** an estimator’s output. They do not enter the
definition of the observable, the selection rule, or the frozen thresholds
(`[BACKGROUND]` program rule: `CLAUDE.md`, pre-registration discipline). An
estimator that requires the embedding is outside the order-only channel.

### 1.4 Three objects that must not be conflated

The claim grammar of the project forces a permanent trichotomy
(`docs/claim_grammar.md` §3):

1. **Global event horizon** — a set defined by the causal structure of the full
   spacetime (e.g.\ boundary of the past of future null infinity). It depends on
   the continuation outside any finite patch (Theorem 3.2).
2. **Singularity-truncation cut** — in a frozen *singular* Schwarzschild family,
   an in-patch locus associated with the artificial edge of the computational
   domain near \(r=0\). It is not a quasi-local trapping surface and must not be
   renamed as one.
3. **Quasi-local proxy** — expansion, trapping, or codimension-two screen
   analogues defined by a separate continuum contract. In \(1{+}1\) dimensions
   there is no spatial 2-sphere carrying a standard null expansion; continuum
   “ladder” constructions in the literature use one-dimensional stand-ins and do
   not automatically supply an order-only codimension-two object in \(3{+}1\)
   (`[BACKGROUND]`; Eichhorn–Gamito–Stokes and claim grammar notes).

Every positive or negative statement in this paper names which of (1)–(3) is at
stake. Silent substitution among them is a terminal failure of wording
(`TELEOLOGY_CLAIM_FAIL` in the project grammar).

### 1.5 Abandoned program north: \(3{+}1\) order-only horizon locators

A natural ambition is to *localize a horizon region* in \(3{+}1\) Schwarzschild from
order-only data by inventing a better combinatorial observable. That ambition is
**not** the north of this paper. Under a frozen program decision
(`phase0_program_north_decision.md`, R1), the following is labeled
`ABANDONED_AS_PROGRAM_NORTH`:

> localizing or reconstructing Schwarzschild \(3{+}1\) horizon structure (global
> event horizon, trapped region, codimension-two screen, or proxy thereof) by
> opening further order-only region-locators in the post-PR008 candidate line
> (ladders, intrinsic cuts, molecule densities, depth retuning, and relatives).

The reasons are structural rather than motivational fatigue: absolute mass is
non-identifiable at fixed \(n\) already in scoped \(3{+}1\) (Theorem 3.1); the
global event horizon is not a finite-patch functional (Theorem 3.2); the scalar
proxy used in \(1{+}1\) does not transfer as a horizon locator
(`survival_matrix_1p1_to_3p1.md`); and a named class of in-bank region-locators
terminated with typed empirical failures (Section 5 of the full manuscript plan;
label `EMPIRICAL_FAILURE_OF_CLASS_L`, not a substitute for Theorems 3.1–3.8).

What remains legitimate is exactly the content of this paper: **limits of the
finite order-only channel**, a sealed bounded recoverability result, and an
honest ledger. Reopening a reconstruction pathway would require a *new* program
with its own channel and target contracts (e.g.\ order+number with known
\(\rho\), or non-horizon targets)—not another estimator under the abandoned north.

### 1.6 Contributions (and non-contributions)

We claim three pillars only:

| Pillar | Content | Program label |
|---|---|---|
| **P1** | Theorems 3.1, 3.2, 3.8 (scale blindness; global EH teleology; rate floor on a regular \(1{+}1\) family) | `PROVED_NON_IDENTIFIABILITY` |
| **P2** | Typed ledger of six exhausted region-localization channels in the project bank | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **P3** | Sealed pre-registered in-patch recoverability PASS for a future-volume observable, with documented verification caveats | `VALIDATED` (caveated) |

**Explicitly not claimed as independent contributions:**

- the Order+Number slogan or continuum conformal determination of the metric
  (`[BACKGROUND]`; Theorem 3.1 is a finite-\(n\) formalization);
- textbook two-point / Hellinger / data-processing machinery
  (`[BACKGROUND]`; Theorem 3.8 is an *instantiation* on a proved-regular family);
- a “blindness map” as mathematical novelty (data-processing asymmetry is
  textbook; we use only a few sentences of notational discipline in later
  sections);
- that causal sets “cannot see black holes” in any unrestricted sense.

**Independent literature check.** Novelty wording for the geometric instantiation
in Theorem 3.8 remains subject to an external literature pass (project Paso D,
item 5). Until that pass is complete, the manuscript must not assert priority as
an absolute (“first in the literature”); hedges of the form “to our knowledge, in
the order-only causal-set channel” are the maximum allowed.

### 1.7 Closing sentence of the introduction

We do not claim to reconstruct a Schwarzschild event horizon from a finite causal
set. We map what the finite order-only channel can and cannot identify under
frozen contracts—and we document both a bounded positive recoverability result
and a typed ledger of failed region-locators without promoting the ledger to a
universal no-go.

---

## §2 Setup: geometry, sprinkling, and targets
<!-- manuscript body -->

### 2.1 Geometry in \(1{+}1\) dimensions

The primary arena is **1+1 Schwarzschild**. In ingoing Eddington–Finkelstein (EF)
coordinates \((v,r)\),

\[
g_\tau
=
-(1-\tau/r)\,dv^2 + 2\,dv\,dr,
\qquad
\tau>0,
\]

with horizon at \(r=\tau\) and volume element \(dv\,dr\) (\(\det g=-1\)). Global null
coordinates \((\tilde U,v)\) exist in which the causal order is the product order
and the horizon sits at \(\tilde U=0\)
(`[PROVED]` formulas: `wp4_fisher_localization_floor.md` §4).

**Diamond family (regular family for Theorem 3.8).** Fix corners
\(p=(v_p,r_p)\) (exterior) and \(q=(v_q,r_q)\) (interior) with
\(0<r_q<\tau_0\le\tau_1<r_p\) and \(v_p<v_q\). For each
\(\tau\in[\tau_0,\tau_1]\) the patch is the causal diamond

\[
D_\tau
:=
J^+_\tau(p)\cap J^-_\tau(q).
\]

In null coordinates \(D_\tau\) is a coordinate box straddling the horizon, with
minimal radius \(r_q>0\) (singularity avoided). This is the family on which
quadratic-mean differentiability and the localization floor are proved (Section 3.3).

**Dilation orbit (family for Theorem 3.1 in \(1{+}1\)).** For \(s>0\), the map
\(\Phi_s(t,r)=(st,sr)\) pulls \(g_{s r_s}\) back to \(s^2 g_{r_s}\). Patches are
transported covariantly: \(P\mapsto\Phi_s(P)\). No null-box assumption is required
for the exact \(\mathrm{TV}=0\) statement (Section 3.1).

### 2.2 Geometry in \(3{+}1\) dimensions (scoped use only)

We do **not** develop a \(3{+}1\) reconstruction theory. The only \(3{+}1\) result
used as a theorem is the **co-scaling orbit for absolute mass** at fixed \(n\),
inside a fixed temporal sector \(\sigma\) and fixed patch shape \(\lambda\)
(`[PROVED]` scoped class: `op12_tv_zero_3p1.md`). Dimensionless targets such as
\(r/(2M)-1\) are constant on that orbit; absolute \(M\) is not identifiable from
the order-only fixed-\(n\) law. Transfer of \(1{+}1\) *localization proxies* to
\(3{+}1\) horizon region-finding is outside the scope of the theorems and is
marked abandoned as program north (§1.5).

### 2.3 Sprinkling and laws

Let \((P,g)\) be a finite-volume patch. A Poisson point process of intensity
\(\rho>0\) with respect to \(\mathrm{vol}_g\) induces a random finite causal set.
Write:

| Symbol | Meaning |
|---|---|
| \(P_{g,\rho}\) | Law of the unlabeled poset including random cardinality |
| \(P_{g,n}\) or \(Q^n\) | Law conditioned on \(N=n\) (order-only fixed-\(n\) channel) |
| \(P^{\mathrm{order+number}}_{g,\rho}\) | Joint law of order and \(N\) when \(\rho\) is part of the model |

**Lemma 2.1 (cardinality conditioning).** `[PROVED]`  
Conditioned on \(N=n\), the \(n\) points are i.i.d.\ with law
\(\mathrm{vol}_g/\mathrm{vol}_g(P)\).  
(Anchor: FWP Lemma 0. This is the sole statement of the lemma in the paper;
later sections cite “Lemma 2.1” rather than re-proving it.)

**Lemma 2.2 (copula reduction on null boxes).** `[PROVED]`  
If the patch is a coordinate box in global null coordinates with metric
\(g=-\Omega\,dU\,dV\), \(\Omega>0\) continuous, then the unlabeled poset law at
fixed \(n\) depends on \(g\) only through the copula of the normalized volume
measure.  
(Anchor: FWP Lemma 1. Used for the diamond family in Theorem 3.8; cited as
Lemma 2.2 thereafter.)

Total variation \(\mathrm{TV}\) and Hellinger distance \(H\) between laws on the
space of finite unlabeled posets are the standard ones; we use \(\mathrm{TV}\le H\)
and Hellinger tensorization for product samples
(`[BACKGROUND]` / project note `wp4_two_point_theorem.md`).

### 2.4 Targets

A *target* is a map \(T\) from completions to a metric space \((\Theta,d_\Theta)\).
An *order-only estimator* is any (possibly randomized) measurable map from
isomorphism classes of finite posets into \(\Theta\). Risk is
\(\mathbb{E}\,d_\Theta(\widehat T, T)\); minimax risk is the infimum over
estimators of the supremum risk over a frozen family
(`[BACKGROUND]` framing: `geometric_indeterminacy_decision.md`).

Targets used in this paper:

| Target | Symbol | Status in this paper |
|---|---|---|
| Absolute horizon radius / mass | \(r_s\), \(M\) | Non-identifiable at fixed \(n\) (Thm 3.1) |
| Continuous diamond parameter | \(\tau\in[\tau_0,\tau_1]\) | Rate floor (Thm 3.8); **not** named “horizon detection” as physics |
| Global event horizon | \(T_{\mathrm{EH}}\) | Not a finite-patch functional (Thm 3.2) |
| In-patch future-volume score | as in prereg-002 | Bounded recoverability (Pillar P3; later section) |
| Region-locators C1–C6 | named combinatorial constructions | Empirical class failure (Pillar P2; later section) |

Every scientific sentence that reports a guarantee is expected to name, at least
implicitly by reference to a frozen card: dimension and family; chart and patch;
channel; target and loss; direction of guarantee (\(\mathrm{TV}=0\), rate lower
bound, PASS under pre-registration, …); and what is *not* claimed
(claim grammar items 1–12, `docs/claim_grammar.md` §1).

### 2.5 Two labels that must not be mixed

| Label | Meaning | Used for |
|---|---|---|
| `PROVED_NON_IDENTIFIABILITY` | No measurable estimator of the channel can drive risk to zero (equal laws, or two-point / Fisher lower bound; or target not a functional of the data) | Theorems 3.1, 3.2, 3.8 |
| `EMPIRICAL_FAILURE_OF_CLASS_L` | Every rule in a **named** list or class \(L\) fails under a fixed protocol | Ledger C1–C6 |

**Rule R3 (binding).** The ledger is never cited as a proof of
`PROVED_NON_IDENTIFIABILITY`. Conversely, Theorems 3.1–3.8 are never presented as
“we tried estimators and they failed.”

### 2.6 Notational discipline for upper bounds

Data processing implies that coarsening the observation cannot increase
distinguishability. An upper bound on total variation (or Hellinger) between
laws therefore **proves blindness** when it is small, but a large upper bound does
**not** prove that a coarse observation is informative. Regions outside a proved
blind zone are at most *candidate visible*. This is textbook data processing, not
an independent theorem; we enforce it only as wording discipline in the later map
of open questions.

---

## Cross-walk to §3 numeration

| This draft | §3 draft | Outline ID |
|---|---|---|
| Thm 3.1 (promised) | Theorem 3.1 | T1 |
| Thm 3.2 (promised) | Theorem 3.2 | T2 |
| Thm 3.8 (promised) | Theorem 3.8 | T3 |
| Lemma 2.1–2.2 | Lemma 0 / FWP Lemma 1 | setup |
| Pillar P2–P3 | (later sections 4–5) | outline §4–§5 |

**Stitching note for the full manuscript:** concatenate  
`phase1_section1_2_abstract_draft.md` (title, abstract, §1, §2)  
+ `phase1_section3_nonidentifiability_draft.md` (§3 body)  
then draft §4–§8 (pasos 1.4–1.5). Minor duplicate definitions (channel, Lemma 0)
should be deduplicated on merge: keep full statements in §2, short pointers in §3.

---

## Claim-grammar mini-check (§1–§2 claims only)

| Sentence type in §1–§2 | Grammar OK? |
|---|---|
| Recoverability vs reconstruction framing | Yes — no result claim |
| Channel definitions | Yes — definitions |
| Abandoned north | Program decision, not a new theorem |
| Contribution list P1–P3 | Forward reference to labeled results |
| Lemmas 2.1–2.2 | `[PROVED]` with anchors |
| Target table | Taxonomy, not PASS claims |
| R3 / DPI discipline | Methodological, not novelty |

No `VALIDATED` or numerical PASS appears in §1–§2 (those wait for §4).

---

## Checklist paso 1.3

```text
[x] Abstract filled (must/must-not from outline)
[x] §1.1 recoverability vs reconstruction
[x] §1.2 channels fixed_n vs order+number
[x] §1.3 embedding scores only
[x] §1.4 trichotomy EH / truncation / quasi-local
[x] §1.5 abandoned north R1
[x] §1.6 contributions P1–P3 only; N2/N5 non-contributions; ítem 5 hedge
[x] §1.7 closing sentence
[x] §2.1 1+1 geometry + diamond + dilation
[x] §2.2 3+1 scoped only
[x] §2.3 sprinkling laws + Lemmas 2.1–2.2
[x] §2.4 targets table
[x] §2.5 EMPIRICAL_FAILURE vs PROVED_NON_IDENTIFIABILITY
[x] §2.6 DPI wording discipline (ex-N5, not a contribution)
[x] Cross-walk to §3
[ ] PI review of abstract + §1 wording
[ ] Paso 1.4 — §4 positive + §5 ledger
```

## Next (1.4)

Draft Pillar P3 (prereg-002 positive, caveats) and Pillar P2 (ledger C1–C6 table with
`EMPIRICAL_FAILURE_OF_CLASS_L` on every row), reusing
`docs/paper_outline_c1c6_plus_prereg002.md` as material source only.
