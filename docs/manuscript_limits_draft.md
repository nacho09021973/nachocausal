# Manuscript draft — Recoverability limits for finite order-only Schwarzschild patches

> **STATUS: INTERNAL_MANUSCRIPT_DRAFT / PI_REVIEW_OK / POLISH_1_6B_DONE /
> NUMBER_AUDIT_1_7_PASS_WITH_CAVEATS / NOT_FROZEN / NOT_FOR_ARXIV /
> DOES_NOT_TOUCH_SEAL / ITEM_5_DISCHARGED_BY_PHASE_2_2026-07-28.**
>
> Assembled from Phase 1 section drafts (pasos 1.2–1.5). Re-merged after 1.6b
> dedupe (Lemma 2.1–2.2 sole definitions in §2; §3 cites by number).
> Number audit: `research_program/synthesis/phase1_number_audit_17.md`.
> Authoritative outline: `research_program/synthesis/phase1_limits_paper_outline.md`.
> Program north: `research_program/synthesis/phase0_program_north_decision.md`.
>
> **PI review:** structure and content accepted 2026-07-28.
>
> **Sources:**
> - `phase1_section1_2_abstract_draft.md` — title, abstract, §1–§2
> - `phase1_section3_nonidentifiability_draft.md` — §3
> - `phase1_section4_5_positive_ledger_draft.md` — §4–§5
> - `phase1_section6_7_8_draft.md` — §6–§8
>
> Before any external circulation: seal verify; optional auditor re-check of Class C
> numbers. Paso D item 5 was discharged with both tiers on 2026-07-28; this is not a
> novelty certificate and absolute priority language remains forbidden.

---


<!-- begin phase1_section1_2_abstract_draft.md -->

## Title block (working)

**Title.**  
Finite order-only observation of Schwarzschild patches: exact scale blindness,
localization floors, and a typed ledger of failed region-locators

**Running subtitle / footnote.**  
A recoverability-limits paper — not a path to 3+1 event-horizon reconstruction
from finite unlabeled order.

---

## Abstract

We study what can and cannot be recovered from the isomorphism class of a finite
causal set obtained by Poisson sprinkling into a Schwarzschild region, when only
the unlabeled causal order is observed—typically conditioned on cardinality
\(N=n\). We prove three non-identifiability statements. First, absolute mass
(horizon radius in absolute units) is exactly non-identifiable at fixed \(n\)
under patch-shape-preserving dilations in \(1{+}1\) dimensions and under
co-scaling in a scoped \(3{+}1\) class: the total variation between the induced
poset laws vanishes on the entire mass orbit. Second, the global event horizon of
a spacetime is not a functional of any observation determined by a single finite
causally convex patch. Third, in a regular one-parameter family of \(1{+}1\)
causal diamonds with
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
   the continuation outside any finite causally convex patch (Theorem 3.2).
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
global event horizon is not a functional of data from a finite causally convex
patch (Theorem 3.2); the scalar
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

**Independent literature check.** The external pass required by project Paso D,
item 5 was completed with responses from both tiers on 2026-07-28
(`phase2_novelty_and_item5.md` §3.4–§3.6). Neither reader found a prior containing
the family-specific instantiation, but Müller’s Theorem 3 is a quantitative
precursor and all steps after family regularity are standard. This is not a
novelty certificate: absolute priority language (“first in the literature”)
remains forbidden, and the manuscript retains bounded comparative wording.

### 1.7 Closing sentence of the introduction

We do not claim to reconstruct a Schwarzschild event horizon from a finite causal
set. We map what the finite order-only channel can and cannot identify under
frozen contracts—and we document both a bounded positive recoverability result
and a typed ledger of failed region-locators without promoting the ledger to a
universal no-go.

---

## §2 Setup: geometry, sprinkling, and targets

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
| Global event horizon | \(T_{\mathrm{EH}}\) | Not a functional of a finite causally convex patch (Thm 3.2) |
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

<!-- end phase1_section1_2_abstract_draft.md -->


<!-- begin phase1_section3_nonidentifiability_draft.md -->

## §3 Proved non-identifiability

This section records three statements of **non-identifiability** for geometric targets
under finite order-only observation. Each statement is of the form: either two
geometries with distinct target values induce **identical** laws on the observed
unlabeled poset, or their laws are so close that **no** measurable function of the
poset can separate them at a stated rate. In the program vocabulary of
`identifiability_taxonomy.md` §4.4 these are
`PROVED_NON_IDENTIFIABILITY` results. They do **not** depend on the success or
failure of any particular estimator constructed in this repository.

**Setup pointer (no re-definition).** Completions, the order-only fixed-\(n\) channel,
Lemma 2.1 (i.i.d.\ sampling after conditioning on \(N=n\); FWP Lemma 0), and
Lemma 2.2 (copula reduction on null boxes; FWP Lemma 1) are as in §2. Proof sketches
below cite those lemmas by number rather than restating them.

### 3.1 Exact scale blindness at fixed cardinality

#### Theorem 3.1 (exact witness orbit for absolute scale)
`[PROVED]` · Label: `PROVED_NON_IDENTIFIABILITY`

**1+1 dimensions.** Let \(g_{r_s}\) be the 1+1 Schwarzschild metric with horizon
radius \(r_s>0\), let \(P\) be any finite-volume patch, and let
\(\Phi_s(t,r)=(st,sr)\) for \(s>0\). Write \(P_n(r_s;P)\) for the law of the
unlabeled \(n\)-element poset obtained by conditioning the sprinkling of
\((P,g_{r_s})\) on \(N=n\). Then, for every \(n\ge 0\) and every \(s>0\),

\[
\mathrm{TV}\bigl(P_n(r_s;P),\, P_n(s r_s;\Phi_s(P))\bigr)
\;=\; 0.
\]

In particular, for every (possibly randomized) order-only estimator \(\widehat r_s\)
and every \(s\neq 1\),

\[
\mathbb{P}_{r_s}\bigl(\widehat r_s = r_s\bigr)
+
\mathbb{P}_{s r_s}\bigl(\widehat r_s = s r_s\bigr)
\;\le\; 1,
\]

so no order-only procedure can recover absolute horizon radius on both ends of the
orbit with total error probability less than one. Since \(s\) is arbitrary, the entire
dilation orbit \(\{r_s>0\}\) shares a single poset law at each fixed \(n\): **within this
orbit, the observed finite order carries no information about \(r_s\) in absolute
units**.

*Proof sketch (full proof: `first_witness_pair_candidates.md` §2, Theorem A).*  
By direct computation, \(\Phi_s^* g_{s r_s}=s^2 g_{r_s}\). A constant conformal factor
preserves causal order. Volume forms in 1+1 dimensions scale by \(s^2\), which cancels
under normalization of the sampling measure. By Lemma 2.1, the \(n\) i.i.d.\ sample on
the dilated geometry is the \(\Phi_s\)-image in law of the sample on the original
geometry, with identical induced relations. Unlabeled poset laws therefore coincide,
and total variation vanishes. The estimation consequence is the two-point bound at
\(\mathrm{TV}=0\) (`wp4_two_point_theorem.md`, Teorema 2). ∎

**3+1 dimensions (scoped).** `[PROVED]` in the scoped class of
`op12_tv_zero_3p1.md`, not as a general Hauptvermutung. Fix a temporal sector
\(\sigma\in\{+,-\}\) and a patch shape \(\lambda\). For masses \(M,M'\) in a
prescribed interval and \(a=M'/M\), the identification in dimensionless Kruskal
coordinates \(\phi_a(U,V,\omega)=(U,V,\omega)\) satisfies
\(g_{M',\lambda}=a^2 g_{M,\lambda}\) and, after volume normalization,

\[
\frac{\mu_{M',\lambda}}{\mu_{M',\lambda}(K)}
=
\phi_{a\#}
\Bigl(
\frac{\mu_{M,\lambda}}{\mu_{M,\lambda}(K)}
\Bigr).
\]

A positive conformal rescaling preserves causality. The general coupling lemma
(`op12_tv_zero_3p1.md` §2) then yields, for every \(n\),

\[
P^{\mathrm{fixed}\,n}_{M,\sigma,\lambda}
=
P^{\mathrm{fixed}\,n}_{M',\sigma,\lambda}.
\]

Thus absolute mass (and absolute \(r_h=2M\)) is non-identifiable in the fixed-\(n\)
order-only channel inside each fixed sector and shape. Dimensionless targets such as
\(r/(2M)-1\) are constant along the orbit and are not constrained by this equality.

#### What Theorem 3.1 does not say

1. **Relative location.** Targets expressed in units of the discreteness scale
   \(\ell=\rho^{-1/d}\), of the patch size, or of \(\sqrt{n}\), are invariant under
   the dilation orbit and are **untouched** (Remark A2, FWP §2).
2. **Order+number with known density.** If \(N\sim\mathrm{Poisson}(\rho V)\) is
   observed and \(\rho>0\) is known, the pair with \(s\neq 1\) is typically
   distinguishable through cardinality alone at precision \(\sim 1/\sqrt{n}\)
   (Remark A3, FWP §2; OP-1.2 §5 in 3+1). Scale is a *Number* observable in that
   channel.
3. **Novelty as physics.** `[BACKGROUND]` The statement formalizes the causal-set
   slogan that order alone does not fix scale (“Order + Number”; e.g.\ Dowker–Zalel,
   arXiv:1703.07556; Madsen, arXiv:2607.05840; Braun, arXiv:2507.01907,
   §§3.3–3.4). Continuum precursors include the conformal character of causal
   isomorphisms (Hawking–King–McCarthy 1976; Malament 1977). Those are precursors of
   the difficult causal-isomorphism-to-conformal direction, not machinery used in the
   three-line proof above. More directly, Bombelli’s 1987 thesis states recovery only
   up to a global scale factor and records Zeeman’s Poincaré-plus-dilatations result
   for causal isomorphisms of Minkowski space. The
   contribution here is the **exact finite-\(n\) TV statement** for the sprinkling
   channel, not a new continuum theorem.

### 3.2 The global event horizon is not a functional of data from a finite causally convex patch

#### Theorem 3.2 (teleological non-identifiability)
`[PROVED]` as a definitional theorem · Label: `PROVED_NON_IDENTIFIABILITY`

Let \(T_{\mathrm{EH}}(M,g)\) denote the event horizon of a time-oriented Lorentzian
manifold \((M,g)\) (the boundary of the causal past of future null infinity, in the
standard asymptotically flat setting, or the appropriate analogue in the completion
under study). Let \(P\subset M\) be a finite-volume **causally convex** region common
to the admissible completions, and let \(\mathcal{D}(P)\) be any
\(\sigma\)-algebra of observables determined by the restriction of the geometry and
of a sprinkling to \(P\) alone (in particular: the unlabeled causal set of the
sprinkling in \(P\)).

**Claim.** \(T_{\mathrm{EH}}\) is not \(\mathcal{D}(P)\)-measurable in general: there
exist pairs of completions that induce identical data on \(P\) and distinct global
event horizons.

*Reason.* By definition, the event horizon depends on the causal structure of the
*entire* future development, not on a single compact region. Choose two completions
whose metrics agree on a neighborhood of \(P\), in both of which \(P\) remains
causally convex, but whose continuation outside \(P\) changes the past of future null
infinity. Causal convexity prevents a relation between two points of \(P\) from being
created by a causal curve that leaves and re-enters \(P\); therefore both the
normalized sprinkling measure and the induced order law on \(P\) agree, while
\(T_{\mathrm{EH}}\) need not. Hence no function of finite-patch order-only data can
equal \(T_{\mathrm{EH}}\) on all admissible completions.
(`[BACKGROUND]` claim grammar: `docs/claim_grammar.md` §3; program synthesis on
teleology.)

#### What Theorem 3.2 does not say

1. It does **not** prohibit *quasi-local* proxies (trapped surfaces, expansion of
   null congruences, singularity-truncation cuts inside a frozen singular family).
   Those targets require their own contracts (`claim_grammar.md` §3).
2. It does **not** assert that black-hole physics is invisible to causal sets. It
   asserts only that the **global event horizon**, as a set defined by the full
   spacetime, is the wrong target for a finite-patch experiment.
3. Empirical failure of particular quasi-local constructions (ledger C1–C6) is
   **not** invoked and is **not** a substitute for this argument.

### 3.3 Localization floor in a regular one-parameter family (1+1)

The dilation orbit of Theorem 3.1 kills absolute scale. Relative geometric
parameters can still vary inside a fixed coordinate chart. Two natural attempts to
encode “horizon location in the box” fail regularity or information content; a third
family is regular and yields a genuine rate lower bound. We record the diagnosis and
the floor. Full proofs:
`wp4_fisher_localization_floor.md` (annex).

#### 3.3.1 Two sterile or non-regular designs `[REMARK]`

**Proposition 3.3 (Kruskal box degeneracy).** `[PROVED]`  
On a *fixed* Kruskal coordinate box, the normalized volume measure of 1+1
Schwarzschild is independent of mass: with \(x=r/(2M)\), the relation
\(UV=(1-x)e^{x}\) is mass-independent and the conformal factor contributes only a
global \(16M^2\), which cancels upon normalization. Hence the copula, the poset law
at every \(n\), and the Fisher information in the mass parameter are **identically
trivial** (\(I\equiv 0\)).  
*Reading.* Fixing a Kruskal box pins the horizon at \(U=0\) for every mass; the
construction is Theorem 3.1 in disguise (annex Prop.\ 1).

**Proposition 3.4 (fixed EF coordinate box: non-regularity).** `[PROVED]` (sketch in annex)  
On a fixed Eddington–Finkelstein coordinate rectangle, the volume measure is Lebesgue
for every mass, but the support of the law in global null coordinates moves with the
parameter at nonzero speed. Hellinger distance is first order in the shift: quadratic
mean differentiability fails and a finite Fisher information is not defined. A weaker
total-variation bound still yields an order-\(1/n\) two-point floor at the point
level; whether the poset channel attains it is open (annex Props.\ 2–3).

#### 3.3.2 The diamond family with fixed EF corners

**Construction.** Fix \(0<r_q<\tau_0\le\tau_1<r_p\) and \(v_p<v_q\). For each
\(\tau\in[\tau_0,\tau_1]\) let
\[
D_\tau
:=
J^+_\tau(p)\cap J^-_\tau(q),
\qquad
p=(v_p,r_p),\; q=(v_q,r_q)
\]
in the ingoing EF chart of 1+1 Schwarzschild of horizon radius \(\tau\). In global
null coordinates adapted to \(g_\tau\), \(D_\tau\) is a coordinate box straddling the
horizon \(\tilde U=0\), with singularity avoided (\(r\ge r_q>0\)).

**Lemma 3.5 (regularity).** `[PROVED]`  
The copula density \(c_\tau\) of the normalized sampling measure on \(D_\tau\) is
jointly continuous, \(C^1\) in \(\tau\), and bounded above and below by positive
constants on the compact parameter interval, with uniformly bounded score.  
(Annex Lemma R.)

**Proposition 3.6 (QMD and finite Fisher).** `[PROVED]`  
The Fisher information \(I(\tau)=\int (\partial_\tau\log c_\tau)^2\,c_\tau\) is finite
and continuous on \([\tau_0,\tau_1]\); set \(\bar I:=\sup I(\tau)<\infty\). The family
is differentiable in quadratic mean, and

\[
H^2(c_\tau,c_{\tau+\delta})
\;\le\;
\frac{\delta^2}{4}\,\bar I.
\]

(Annex Prop.\ 4; Hellinger convention \(H^2=\int(\sqrt{p}-\sqrt{q})^2\in[0,2]\).)

**Proposition 3.7 (no exact re-identification).** `[PROVED]`  
\(c_\tau\neq c_{\tau'}\) whenever \(\tau\neq\tau'\) in \([\tau_0,\tau_1]\). In
particular the exact \(\mathrm{TV}=0\) branch for *relative* location never occurs on
this family.  
(Annex Prop.\ 5; Ricci pinning and \(r\)-preservation contradiction, with symbolic
checks in `wp4_fisher_localization_floor_symbolic_checks.py`.)

#### Theorem 3.8 (order-only two-point localization floor)
`[PROVED]` · Label: `PROVED_NON_IDENTIFIABILITY` (rate)

Let \(Q^n_\tau\) be the law of the unlabeled \(n\)-point poset from \(D_\tau\)
conditioned on \(N=n\). For every \(n\), every \(\tau,\tau+\delta\in[\tau_0,\tau_1]\),
and every (possibly randomized) order-only estimator \(\widehat\tau=f(C_n)\):

1. **Total variation bound.**
   \[
   \mathrm{TV}\bigl(Q^n_\tau,\,Q^n_{\tau+\delta}\bigr)
   \;\le\;
   \frac{|\delta|}{2}\,\sqrt{n\,\bar I}.
   \]
2. **Estimation-to-testing.**
   \[
   \mathbb{P}_\tau\bigl(|\widehat\tau-\tau|\ge|\delta|/2\bigr)
   +
   \mathbb{P}_{\tau+\delta}\bigl(|\widehat\tau-(\tau+\delta)|\ge|\delta|/2\bigr)
   \;\ge\;
   1-\frac{|\delta|}{2}\sqrt{n\,\bar I}.
   \]
3. **Floor.** No order-only procedure localizes \(\tau\) to precision \(|\delta|/2\)
   with confidence \(1-\varepsilon\) at both endpoints whenever
   \[
   |\delta|
   \;<\;
   \frac{2(1-2\varepsilon)}{\sqrt{n\,\bar I}}.
   \]
   Thus the minimax localization radius is of order \(1/\sqrt{n\bar I}\) at fixed \(n\).

*Proof sketch (annex §5).*  
Prop.\ 3.6 bounds Hellinger at the copula level. Hellinger tensorizes over \(n\)
i.i.d.\ samples (Lemma 2.1). In copula coordinates every family member is the unit
square with the same product order, while all \(\tau\)-dependence lies in the
sampling density. The map from the sample to the unlabeled poset is therefore
parameter-independent (Lemma 2.2); data processing and \(\mathrm{TV}\le H\) yield
(1). The nearest-endpoint test reduction yields (2)–(3)
(`wp4_two_point_theorem.md`). ∎

#### What Theorem 3.8 does and does not claim

| Claims | Does **not** claim |
|---|---|
| A lower bound on risk for **all** order-only estimators (randomized included) | That the bound is **tight** for posets (it is inherited by data processing from the point process and may be loose) |
| Rate exponent \(n^{-1/2}\) on this named regular family | That \(\bar I\) is evaluated in closed form for reference corners (finiteness is proved; numerical \(\kappa\) is marked NUMERICAL elsewhere) |
| Technique: QMD + Hellinger + two-point | Novelty of Le Cam / Hellinger machinery `[BACKGROUND]` (textbook) |
| | Any result in 3+1 dimensions |
| | That \(\tau\) is “horizon information” as a distinct physical invariant |

**Physics caveat (mandatory).** In 1+1 Schwarzschild the scalar curvature is
\(R_\tau=-2\tau/r^3\). The parameter \(\tau\) is simultaneously the horizon radius and
the only curvature amplitude of the family. There is no threshold structure that
activates because the diamond crosses \(r=\tau\). Discriminating \(\tau\) is
discrimination of a continuous geometric parameter of the patch—not a proof that an
event horizon has been localized as a codimension-one object. Naming the theorem a
“horizon detector bound” is **forbidden** in the manuscript.

#### Intrinsic units `[REMARK]` (former N4, deflated)

Under simultaneous dilation of corners and parameter, the combination
\(\kappa(\tau):=V(\tau)\,I(\tau)\) is exactly dilation-invariant (annex §5a): it depends
on the dimensionless shape of the diamond, not on absolute size. With
\(n=\rho V\) and \(\ell=\rho^{-1/2}\),

\[
\frac{\delta_n}{\ell}
\;\sim\;
\frac{1}{\sqrt{\bar\kappa}},
\qquad
\bar\kappa
:=
V\cdot\bar I.
\]

`[BACKGROUND]` Dimensionally, Fisher information for a length parameter scales as
\(\mathrm{length}^{-2}\) and area as \(\mathrm{length}^{2}\), so \(V\cdot I\) is
dimensionless. The annex proves the invariance on this family; we do **not** present
\(\kappa\) as an independent novelty theorem.

### 3.4 Summary of §3

| Result | Target | Channel | Guarantee | Label |
|---|---|---|---|---|
| Thm 3.1 | Absolute \(r_s\) or \(M\) | order-only, \(N=n\) | \(\mathrm{TV}=0\) on dilation orbit (1+1 and scoped 3+1) | `PROVED_NON_IDENTIFIABILITY` |
| Thm 3.2 | Global event horizon | data from a finite causally convex patch | not a functional of those data | `PROVED_NON_IDENTIFIABILITY` |
| Thm 3.8 | Parameter \(\tau\) of the EF diamond family | order-only, \(N=n\) | floor \(\sim 1/\sqrt{n\bar I}\) | `PROVED_NON_IDENTIFIABILITY` (rate) |
| Prop 3.3–3.4 | design of families | — | Kruskal sterile; fixed EF box non-regular | `[REMARK]` |

None of these results is an `EMPIRICAL_FAILURE_OF_CLASS_L` statement. Failures of
named region-locators appear in §5 of the outline (ledger), not here.


---

<!-- end phase1_section3_nonidentifiability_draft.md -->


<!-- begin phase1_section4_5_positive_ledger_draft.md -->

## §4 A sealed in-patch recoverability positive

Section 3 maps **limits**: targets that no order-only map can identify, or can identify
only above a rate floor. Those theorems would be empty of scientific interest if the
order-only channel were *vacuously* uninformative about every geometric score. This
section records that it is not. Under a frozen pre-registration, a single order-only
observable—future volume—passes a sealed blind validation contract in a finite
\(1{+}1\) Schwarzschild patch. The result is **recoverability of an in-patch geometric
signal**, not reconstruction of a global event horizon
(`NO_RECONSTRUCTION_CLAIM`).

### 4.1 Frozen contract (preregistration 002)

**Label.** Pre-registration: `docs/preregistration_002.md` (status FROZEN).  
**Instrument.** Estimator-v2 under the sealed package
(`docs/estimator_v2_freeze.md`, `docs/estimator_v2_seal.md`).  
**Seal.** `nachocausal/thresholds.py` SHA256
`6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
(`make verify-seal`). Thresholds and seeds were frozen **before** the blind
validation run.

**Observable (order-only).** For each sprinkled element \(i\),
\[
O(i) \;=\; \bigl|\mathrm{future}(i)\bigr|
\]
(cardinality of the causal future inside the patch). The point estimate of the
horizon-associated boundary uses a bracket midpoint under a frozen analysis plan
inherited from the prereg-001 addendum and modified only by the three sealed
estimator-v2 changes: VOLUME observable; \(\tau(n)\) abstention gate; domain gate
\(T_{\mathrm{EDGE\_MIN}}=6\).

**Channel.** Order-only selection and scoring: no continuum coordinates are available
to the estimator. The hidden embedding is used **only** to score localization error
after the estimate is produced (§1.3).

**Held-out seeds.** Twenty validation seeds drawn once, blind, from the virgin band
\([2\,000\,000,\,2\,999\,999]\) by a deterministic `numpy` draw
(`VALIDATION_DRAW_SEED=20260622`), disjoint from all exploration seeds
(prereg-002 text; guard in `thresholds.py`).

**Primary endpoint.** Intensity \(\lambda=12000\) (mean \(N\) of order \(1.2\times 10^4\)),
\(t_{\mathrm{edge}}=6\) (in-domain). **PASS** if and only if all six frozen checks hold
at that endpoint (significance, localization, convergence slack, stability, false
positive, order-only guard); otherwise FAIL / INCONCLUSIVE / OUT_OF_DOMAIN as
specified—**report alike**, no post-hoc retuning.

### 4.2 Blind outcome

**Verdict.** `[VALIDATED]` with documented artifact caveats (next subsection):

```text
PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]
```

At the primary endpoint, all six frozen checks evaluated true
(`docs/preregistration_002_result.md`). Headline primary numbers (transcribed from
the original validation table; same values MATCH under supervised re-verification):

| Check | Primary (\(\lambda=12000\)) |
|---|---|
| Sign-flip \(p_{\mathrm{perm}}\) | \(9.54\times 10^{-7}\le 10^{-4}\) |
| Median \(\lvert dr\rvert/(2M)\) vs \(\theta_{\mathrm{loc}}\) | \(0.064\le 0.098\) |
| Coverage | \(0.95\ge 0.5\) |
| Boundary \(r\)-std vs \(\theta_{\mathrm{stab}}\) | \(0.008\le 0.049\) |
| LOO false-positive fraction | \(0.00\le 0.05\) |
| Order-only guard | no raise |

The \(\tau(n)\) abstention gate behaves as designed: Schwarzschild abstention \(0.00\)
at every intensity level; Minkowski control abstention \(0.90\)–\(1.00\) (suppresses
structureless false structure). A transparent non-primary caveat is recorded: at
\(\lambda=6000\), false-positive fraction \(0.10\) misses \(\theta_{\mathrm{fp}}\); the
frozen rule evaluates false positives **only** at the primary endpoint, where the
check passes.

**Run provenance (historical).** Blind `validate.run()` on the sealed package at
commit `573cfcb`, seal as above, numpy 1.26.4; chain
decision → freeze → estimator seal → prereg-002 seal → single blind run
(prereg-002 result §Provenance).

### 4.3 Artifact integrity and supervised re-verification

Honesty about the raw artifact is part of the positive, not a footnote to hide.

1. The **primary raw** `results/validation.json` of the original 2026-06-22 blind run
   was later found unrecoverable (`auditor_report_005`, `AUDIT_FAIL`; second machine
   unavailable per PI determination).
2. A **supervised re-verification** was authorized
   (`comite_decision_016`, `prereg002_reverification_declaration.md`): deterministic
   replay on the same sealed instrument, commit lineage, and frozen seeds—not a
   second blind discovery, not a retuning loop.
3. Outcome: **MATCH** on every frozen field
   (`prereg002_reverification_result.md`).

Therefore the scientific claim remains the frozen PASS under the pre-registered
contract, with the epistemic status explicitly weakened to
`PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY`. We do
not claim recovery of the original raw bytes.

### 4.4 What the PASS means

**Means (bounded, frozen claim).** In a finite \(1{+}1\) Schwarzschild patch at the
sealed domain edge, the causal order alone—under this observable and this
protocol—carries enough information to localize a horizon-*associated* boundary
score **significantly and stably** relative to frozen thresholds, with bracket width
contracting toward the discreteness floor as density grows, while a box-matched
flat control does not produce the same separation
(prereg-002 result, “What this PASS does and does NOT mean”).

**Units.** Localization is scored in units of \(2M\) and compared to thresholds built
from the discreteness scale \(\ell\). This is compatible with Theorem 3.1: absolute
\(r_s\) is non-identifiable at fixed \(n\); the PASS does not claim absolute scale.

**Role relative to Section 3.** The channel is not empty. Non-identifiability of
absolute mass, of the global event horizon, and the rate floor for a continuous
family parameter coexist with recoverability of a **different**, carefully
contracted in-patch score.

### 4.5 What the PASS does not mean

| Forbidden reading | Why |
|---|---|
| Global event horizon reconstructed | Theorem 3.2; claim grammar §3 |
| Full metric reconstruction | Outside contract |
| \(3{+}1\) Schwarzschild / Kerr | Outside bank and dimension |
| Region-locators C1–C6 work | They do not; see §5 |
| Every order-only map succeeds at something | Only this sealed instrument under this protocol |
| Primary raw artifact still on disk | §4.3 |

### 4.6 Methodological note (optional short paragraph)

Dev/validation separation, pre-frozen thresholds, and one-way blind evaluation are
part of the positive’s credibility. A guardrail that cannot fail is decoration: every
number above is either the literal output of a sealed run / MATCH re-verification or
is marked as transcription. No threshold was loosened after seeing validation
outcomes (`NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`).

---

## §5 Typed negative ledger: six exhausted region-localization channels

### 5.1 Why a ledger is a result

Section 3 answers questions of the form: *no estimator in the whole measurable class
can identify \(T\).* This section answers a different question:

> Within a **named** class \(L\) of order-only constructions aimed at localizing a
> *region* of horizon-like structure in this finite \(1{+}1\) bank, what happened to
> each construction under project adjudication?

Documenting typed failures with terminals, anchors, and lessons is a scientific
deliverable of a recoverability benchmark (“documented failure \(>\) almost-PASS”;
committee decision 042). The program label for the entire section is:

```text
EMPIRICAL_FAILURE_OF_CLASS_L
L = {C3-early, C1, C2, C3-third, C4, C5, C6}
      (region-localization constructions in this bank)
```

**Rule R3 (binding, restated).** Nothing in §5 is a proof of
`PROVED_NON_IDENTIFIABILITY`. In particular, §5 does **not** prove that every
conceivable order-only map fails to localize every conceivable quasi-local proxy.
It proves only that the listed constructions, under the listed adjudications,
terminated as stated.

### 5.2 Master table

Anchors: `docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md` §3–§4
(C1–C5); C6 via decisions 043–044 and the consolidation outline
`docs/paper_outline_c1c6_plus_prereg002.md` §4–§5. Label on every row:
`EMPIRICAL_FAILURE_OF_CLASS_L`.

| ID | Construction (one line) | Terminal | Lesson (one line) | Program label |
|---|---|---|---|---|
| **C3-early** | Future-width / funnel collapse as horizon proxy | `REJECTED_HAYWARD` | Funnel tracks singularity truncation, not trapping (fails regular Hayward control) | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **C1** | Bottleneck / ideal / flow through `Max` | `BLOCKED_UNCLOSED` + `MAX_TRIVIAL` | Finite `Max` trivializes; definition never closed as frozen localizer | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **C2** | Common-future overlap / \(\kappa\) on a wavefront | `BLOCKED_E_INDEP` + `TRUNCATION` | Without null structure + ceiling control, confounds with box truncation | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **C3-third** | Truncated-future selectors \((L,V)\) on minimals | `INCONCLUSIVE_EDGE_MARGINAL` | Edge-dominated marginal channel; insufficient pair synergy | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **C4** | Common-future convergence conditioned on neighbors | `REJECTED_NO_E_M` | No order-only, relabel-invariant neighbor graph \(E_M\) (decision 039) | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **C5** | Global common-future matrix → spectral block / partition | `EXHAUSTED` (F3) | Wall \(\neq\) `Max`; twin/bridge ambiguity; no lateral dual (040–041) | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **C6** | Antichain waist \(W(p,q)\) of an Alexandrov interval | `BLOCKED_NO_STABLE_CODIM2` | Antichain exists as order object; stable codim-2 screen and transport do not | `EMPIRICAL_FAILURE_OF_CLASS_L` |

**Line status.** C1–C5: `EXHAUSTED_FOR_LOCALIZATION` as a localizer line for
horizon/edge structure in this bank (decision 042). C6: closed at the conservative
terminal after committee red-team (043→044), not promoted to a frozen localizer.

### 5.3 Channel notes (short)

**C3-early.** Width collapse looked like a trapping diagnostic until a regular
(non-singular) black-hole control removed the funnel: the signal was singularity
geometry, not apparent horizon. Terminal: reject for horizon localization.

**C1.** Ideal-theoretic bottleneck formalisms never closed in the finite unlabeled
setting; maximality notions that work in the continuum idealize badly when `Max` is
trivial or unclosed. Never promoted to a frozen localizer.

**C2.** Common-future overlap statistics confound physical near-horizon structure with
the computational ceiling of the patch. Independence and truncation controls blocked
promotion.

**C3-third.** Clean developmental channel on truncated futures of minimals; remains
inconclusive and edge-dominated—a marginal channel rather than a region partitioner.

**C4.** Any “neighbor-conditioned” construction requires an edge set \(E_M\) on
minimals. No order-only, permutation-invariant, non-circular, tie-closed definition of
\(E_M\) was available; continuum references (Rideout–Wallden, Boguñá–Krioukov) do not
supply that \(E_M\) in the C4 domain (decision 039). Concept blocked before
pre-registration.

**C5.** Global matrix methods can be mathematically live as linear algebra on the
poset; as a *localization channel* they exhaust on wall/bridge/twin ambiguity and the
absence of a lateral dual peel that would turn a spectral block into a horizon
region (decisions 040–041).

**C6 (detail).** For \(p\prec^* q\), the waist
\[
W(p,q)
\;=\;
\{\,x : p\prec^* x \land x\prec^* q\,\}
\]
is an antichain in the order (order-only theorem; full proof in project appendix
material). Existence of an antichain is not existence of a **stable codimension-two
screen** with order-only transport and sign. Committee 043 initially overstated
abundance/stability; red-team 044 lowered the terminal to the conservative
`BLOCKED_NO_STABLE_CODIM2`. The self-correction is part of the method: the ledger
records the lower claim, not the withdrawn higher one.

### 5.4 Cross-cutting structural reading

Across C1–C6, the recurring obstructions in this bank are:

1. **Ceiling / wall / truncation** of the finite patch mistaken for physical boundary;
2. **No lateral pairing** or neighbor structure that is purely order-only;
3. **Scale \(\leftrightarrow\) depth** confounds when absolute scale is invisible
   (Theorem 3.1) but patch depth is visible;
4. **No stable order-only codimension-two object** with transport (C6), in a dimension
   where continuum codim-2 screens are already subtle.

These are lessons about *this construction class in this bank*, not a theorem that
the order contains no geometric information (contradicted by §4) and not a theorem
that every quasi-local continuum proxy is non-identifiable (that would require
witness pairs or Fisher analysis for each named \(T\), i.e.\ Section 3 methodology).

### 5.5 What §5 does not authorize

| Forbidden | Correct substitute |
|---|---|
| “Therefore horizon localization is impossible order-only” | Theorems 3.1–3.2 for absolute scale and global EH; open/abandoned for other \(T\) under R1 |
| “C1–C6 prove minimax lower bounds” | Only Thm 3.8-style arguments prove minimax floors |
| Reopening A–C matrix candidates as the program north | `ABANDONED_AS_PROGRAM_NORTH` (Fase 0 R1) |
| Renaming singularity funnel as trapping | claim grammar trichotomy §1.4 |

### 5.6 Relation to the abandoned north and to Section 3

The ledger **motivates** the program decision not to spend further cycles on the same
region-localizer line (§1.5). The **proofs** that absolute mass and the global event
horizon are out of reach are Section 3, not Section 5. A future no-go for a named
quasi-local proxy \(Q\) would require a new witness pair or rate bound for that \(Q\)
(Fase 3 option B2), not another row of the same ledger style without measure-theoretic
content.

---

<!-- end phase1_section4_5_positive_ledger_draft.md -->


<!-- begin phase1_section6_7_8_draft.md -->

## §6 Relation to the literature

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
non-identifiable in the order-only fixed-\(n\) channel. Hawking–King–McCarthy
(J.\ Math.\ Phys.\ 17, 174, 1976) and Malament (J.\ Math.\ Phys.\ 18, 1399,
1977) are continuum precursors for the difficult causal-isomorphism-to-conformal
direction; that machinery is not used in Theorem 3.1’s easy direction. More
directly, Bombelli’s 1987 thesis states recovery only up to a global scale factor
and records Zeeman’s Poincaré-plus-dilatations result for Minkowski causal
isomorphisms. Those facts motivate the orbit; they are not a substitute for the
sprinkling-channel TV calculation.

### 6.2 Indistinguishability of orders without rates

Müller (arXiv:2503.01719) constructs pairs of non-isometric Lorentzian geometries
that admit finite causal sets with nearly identical order laws at fixed
cardinality—precise negative results for naive formulations of the
Hauptvermutung. His Theorem 3 is also the closest published **quantitative**
precursor: for normalized flat cylinders, the probability of observing a total
order has an explicit \(K\)-dependent lower bound while temporal diameter varies.
The mechanism is degeneration toward one order type, not a QMD family, and the
paper does not formulate Fisher information, a Le Cam risk bound, or a local
minimax floor for a Schwarzschild parameter. Theorem 3.8 is the family-specific
regular-parametric instantiation; it is not the first quantitative
indistinguishability statement for a continuous geometric family.

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
The independent check required by project Paso D, item 5 was completed with
responses from both tiers on 2026-07-28. Neither reader found a prior containing
this family-specific instantiation, but both treated the machinery after QMD as
standard and identified residual literature in random geometric graphs and
latent-space models. Absolute priority language remains disallowed.

### 6.6 What we do not cite as competition

We do not treat failures of particular estimators in the literature—or our own
ledger—as proofs of non-identifiability. Conversely, we do not treat continuum
reconstruction theorems under order+number hypotheses as refutations of
fixed-\(n\) order-only blindness for absolute mass.

---

## §7 What is closed, open, and abandoned

### 7.1 Closed in this paper

| Question | Status | Where |
|---|---|---|
| Absolute \(r_s\) / \(M\) from order-only data at fixed \(N=n\) (stated families) | **Non-identifiable** (\(\mathrm{TV}=0\) on the orbit) | Thm 3.1 · `PROVED_NON_IDENTIFIABILITY` |
| Global event horizon from a single finite causally convex patch | **Not a functional** of patch data | Thm 3.2 · `PROVED_NON_IDENTIFIABILITY` |
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
| Deeper prior-art sweep in random geometric graphs / latent-space minimax inference | `OPEN` bibliographic residual | Both external tiers identified this as the most plausible remaining neighborhood; no concrete sink anchored |
| Ordering-fraction / Chebyshev TV lower separation for fixed pairs | Conditional | Only if project conditions C3–C4 (comité 045) are closed; omitted from claims until then |

### 7.4 Explicitly not claimed open problems

We do not list “find the observable that reconstructs the \(3{+}1\) event horizon
from finite order-only data” as an open problem of this program. That question is
abandoned as north (§7.2), not deferred.

---

## §8 Conclusions

We asked what a finite unlabeled causal set can identify about Schwarzschild
geometry when the observation is order-only—often conditioned on cardinality—and
when continuum labels are used only to score, never to define, the estimator.

**Pillar P1.** Three non-identifiability statements are proved. Absolute horizon
radius (mass) is invisible at fixed \(n\) along dilation and co-scaling orbits
(Theorem 3.1). The global event horizon is not a functional of data from a finite
causally convex patch
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

<!-- end phase1_section6_7_8_draft.md -->

---

## Appendix E — Number audit (internal)

See `research_program/synthesis/phase1_number_audit_17.md` for the full Class A–E
sweep. Summary: `AUDIT_PASS_WITH_DECLARED_CAVEATS`. Validation table numbers are
transcriptions from `docs/preregistration_002_result.md` with supervised MATCH
re-verification; primary raw artifact remains lost as documented in §4.3. No new
ensembles were run for this draft. Seal hash unchanged.
