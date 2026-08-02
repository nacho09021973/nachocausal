# Manuscript draft — Recoverability limits for finite order-only Schwarzschild patches

> **STATUS: MANUSCRIPT_DRAFT / PI_REVIEW_OK / POLISH_1_6B_DONE /
> NUMBER_AUDIT_1_7_PASS_WITH_CAVEATS / NOT_FROZEN /
> CLEARED_FOR_ARXIV_BY_PI_2026-08-06 / SEAL_VERIFIED_AT_CLEARANCE /
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
> **arXiv clearance (PI, 2026-08-06).** The `NOT_FOR_ARXIV` token is withdrawn. The
> seal-verify precondition below was discharged at clearance:
> `nachocausal/thresholds.py sha256 = 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`,
> matching `docs/preregistration_002.md`.
>
> **What this clearance does and does not override.** The closure note
> (`docs/program_closure_note_2026-07-30.md`) carries two separate constraints, and only
> one of them is affected. Clause 3 — manuscripts kept "as a record … not as an
> announcement" — is **superseded** by this decision. `NO_PUBLIC_NOVELTY_CLAIM` is **not**
> superseded and remains fully in force: this is a limits paper, it asserts no priority,
> and posting it is not a novelty claim. The two are compatible precisely because the
> content already complies.
>
> Standing constraints, unchanged: seal verify before any external circulation; optional
> auditor re-check of Class C numbers. Paso D item 5 was discharged with both tiers on
> 2026-07-28; this is not a novelty certificate and absolute priority language remains
> forbidden.
>
> **Not yet done before posting:** the five figures in `viz/` are ready and English but
> are **not inserted** in this text. The Figure 2 caption must carry the
> laws-versus-realisations distinction (`viz/README.md`), which is where a referee looks.

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

We ask which continuum-geometric properties are identifiable from the isomorphism
class of a finite causal set sprinkled into a Schwarzschild patch when only the
unlabeled order is observed, typically conditional on \(N=n\). Three obstructions
are proved. Absolute mass is exactly invisible at fixed \(n\) under
patch-shape-preserving dilations in \(1{+}1\) dimensions and co-scaling in a
scoped \(3{+}1\) class. The global event horizon is not a functional of data from
one finite causally convex patch. In a regular one-parameter family of \(1{+}1\)
causal diamonds with finite Fisher information, no order-only procedure localizes
the parameter below a two-point rate of order \(n^{-1/2}\). Conversely, for
sufficiently small null lapse \(dv\), the comparable-pair count separates every
fixed distinct parameter pair and is consistent whenever
\(\sqrt n\,|\delta_n|\to\infty\). Thus \(n^{-1/2}\) is the boundary exponent in
the \(o/\omega\) sense; critical-scale constants remain open. These statements
are measure-theoretic or definitional, not conclusions from failed estimators.
We also report a sealed in-patch future-volume recoverability result and a typed
ledger of six exhausted region-localization channels, explicitly not a universal
no-go. This is a map of finite order-only channel limits, not a reconstruction of
a black-hole event horizon or a route to \(3{+}1\) reconstruction from such data
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
| **Order-only, fixed \(n\)** | Isomorphism class of the poset conditioned on \(N=n\) | Primary channel for Theorems 3.1, 3.8, and 3.9 |
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
label `EMPIRICAL_FAILURE_OF_CLASS_L`, not a substitute for Theorems 3.1–3.9).

What remains legitimate is exactly the content of this paper: **limits of the
finite order-only channel**, a sealed bounded recoverability result, and an
honest ledger. Reopening a reconstruction pathway would require a *new* program
with its own channel and target contracts (e.g.\ order+number with known
\(\rho\), or non-horizon targets)—not another estimator under the abandoned north.

### 1.6 Contributions (and non-contributions)

We claim three pillars only:

| Pillar | Content | Program label |
|---|---|---|
| **P1** | Theorems 3.1, 3.2, 3.8–3.9 (scale blindness; global EH teleology; rate floor and matching fixed-\(n\) separation exponent on a regular \(1{+}1\) family) | `PROVED_NON_IDENTIFIABILITY`; `PROVED_FIXED_N_SEPARATION` |
| **P2** | Typed ledger of six exhausted region-localization channels in the project bank | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **P3** | Sealed pre-registered in-patch recoverability PASS for a future-volume observable, with documented verification caveats | `VALIDATED` (caveated) |

**Explicitly not claimed as independent contributions:**

- the Order+Number slogan or continuum conformal determination of the metric
  (`[BACKGROUND]`; Theorem 3.1 is a finite-\(n\) formalization);
- textbook two-point / Hellinger / data-processing / Hoeffding / Chebyshev machinery
  (`[BACKGROUND]`; Theorems 3.8–3.9 instantiate it on a proved-regular family);
- a “blindness map” as mathematical novelty (data-processing asymmetry is
  textbook; we use only a few sentences of notational discipline in later
  sections);
- that causal sets “cannot see black holes” in any unrestricted sense.

**Independent literature check.** The external pass required by project Paso D,
item 5 was completed with responses from both tiers on 2026-07-28
(`phase2_novelty_and_item5.md` §3.4–§3.6). Neither reader found a prior containing
the family-specific localization-floor instantiation now stated as Theorem 3.8,
but Müller’s Theorem 3 is a quantitative precursor and all steps after family
regularity are standard. The newly promoted Theorem 3.9 has not yet received a
theorem-specific priority audit. This is not a novelty certificate: absolute
priority language (“first in the literature”) remains forbidden, and the
manuscript retains bounded comparative wording.

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

**Diamond family (regular family for Theorems 3.8–3.9).** Fix corners
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
space of finite unlabeled posets are the standard ones, with the convention fixed
once and for all as

\[
H^2(P,Q)
:=
\int\bigl(\sqrt{dP}-\sqrt{dQ}\bigr)^2
\;=\;
2\Bigl(1-\!\int\!\sqrt{dP\,dQ}\Bigr)
\;\in[0,2].
\]

We use \(\mathrm{TV}\le H\), the data-processing inequality for both distances
under a common measurable map, and the **exact tensorization identity** for
product samples: since the affinity \(\int\sqrt{dP\,dQ}=1-\tfrac12H^2(P,Q)\)
factorizes over independent coordinates,

\[
1-\tfrac12\,H^2\bigl(P^{\otimes n},Q^{\otimes n}\bigr)
\;=\;
\Bigl(1-\tfrac12\,H^2(P,Q)\Bigr)^{\!n}.
\]

With \(t:=\tfrac12H^2(P,Q)\in[0,1]\), Bernoulli's inequality \((1-t)^n\ge 1-nt\)
turns this into the form used in Theorem 3.8,

\[
H^2\bigl(P^{\otimes n},Q^{\otimes n}\bigr)\;\le\;n\,H^2(P,Q).
\]

(`[BACKGROUND]`. Traceability, not a dependency: `wp4_two_point_theorem.md`.)

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
| Continuous diamond parameter | \(\tau\in[\tau_0,\tau_1]\) | Rate floor and matching \(o/\omega\) separation boundary (Thms 3.8–3.9); **not** named “horizon detection” as physics |
| Global event horizon | \(T_{\mathrm{EH}}\) | Not a functional of a finite causally convex patch (Thm 3.2) |
| In-patch future-volume score | as in prereg-002 | Bounded recoverability (Pillar P3; later section) |
| Region-locators C1–C6 | named combinatorial constructions | Empirical class failure (Pillar P2; later section) |

Every scientific sentence that reports a guarantee is expected to name, at least
implicitly by reference to a frozen card: dimension and family; chart and patch;
channel; target and loss; direction of guarantee (\(\mathrm{TV}=0\), rate lower
bound, PASS under pre-registration, …); and what is *not* claimed
(claim grammar items 1–12, `docs/claim_grammar.md` §1).

### 2.5 Labels that must not be mixed

- `PROVED_NON_IDENTIFIABILITY`
  - *Meaning:* No measurable estimator of the channel can drive risk to zero
    (equal laws, or two-point / Fisher lower bound; or target not a functional
    of the data)
  - *Used for:* Theorems 3.1, 3.2, 3.8
- `PROVED_FIXED_N_SEPARATION`
  - *Meaning:* A named order-only statistic yields tests with vanishing total
    error under the theorem's stated family, lapse, and parameter-separation
    quantifiers
  - *Used for:* Theorem 3.9
- `EMPIRICAL_FAILURE_OF_CLASS_L`
  - *Meaning:* Every rule in a **named** list or class \(L\) fails under a
    fixed protocol
  - *Used for:* Ledger C1–C6

**Rule R3 (binding).** The ledger is never cited as a proof of
`PROVED_NON_IDENTIFIABILITY`. Conversely, Theorems 3.1–3.9 are never presented as
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

## §3 Exact obstructions and fixed-\(n\) statistical limits

This section records three **non-identifiability** statements for geometric targets
under finite order-only observation and one companion **positive separation**
theorem. The negative statements show either that distinct target values induce
identical laws on the observed unlabeled poset, or that no measurable function of
the poset can separate nearby parameters below a stated rate. The companion theorem
exhibits a named order-only statistic that separates fixed distinct parameters above
that rate. In the program vocabulary these are, respectively,
`PROVED_NON_IDENTIFIABILITY` and `PROVED_FIXED_N_SEPARATION`. Neither label is
inferred from the success or failure of the empirical locator classes in §5.

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
\(\mathrm{TV}=0\) (`wp4_two_point_theorem.md`, Teorema 2). \(\blacksquare\)

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
   §§3.3–3.4). **Dimensional scope of those two citations.** Braun assumes
   \(d\ge 3\) throughout (arXiv:2507.01907, p.\ 2: “we assume all spacetimes have
   the same dimension \(d\in\mathbb{N}\) no less than 3”), and Madsen’s error
   optimisation holds the covariance term subdominant only “for \(d>2\)”
   (arXiv:2607.05840, Thm.\ 4.18). Both are therefore background for the scoped
   \(3{+}1\) statement, and **neither licenses the \(1{+}1\) results**; the
   restriction is inherited from Malament’s \(d>2\) hypothesis, not a gap in
   technique (`docs/bibliography_claims.md` §§1.1, 1.3, 2.5bis).
   Continuum precursors include the conformal character of causal
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
the floor. Section 3.3.2 and Theorem 3.8 are self-contained below; the two sterile
designs of §3.3.1 and Proposition 3.7 are stated here and proved in
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
in the ingoing EF chart of 1+1 Schwarzschild of horizon radius \(\tau\). Fix once
and for all an open interval \(J\) with \([\tau_0,\tau_1]\subset J\) and
\(\overline J\subset(r_q,r_p)\); nothing below uses more than \(r_q<\tau<r_p\), so
every statement of this subsection holds verbatim for \(\tau\in J\), with all
constants uniform on compact subsets of \(J\). (The enlargement is free and is what
lets Proposition 3.6 quote a criterion stated on an open parameter set.)

**Null coordinates and the product order.** Put

\[
\omega_\tau(r):=e^{r/\tau}\bigl(r/\tau-1\bigr),
\qquad
\omega_\tau'(r)=\frac{r\,e^{r/\tau}}{\tau^{2}}>0,
\]

a smooth strictly increasing bijection \((0,\infty)\to(-1,\infty)\) with
\(\omega_\tau(\tau)=0\), and define on \(r>0\)

\[
\tilde U:=-e^{-v/(2\tau)}\,\omega_\tau(r).
\]

Outgoing null curves of \(g_\tau\) satisfy \(dr=\tfrac12(1-\tau/r)\,dv\). Along an
arbitrary curve,
\(d\tilde U=e^{-v/(2\tau)}\bigl[\omega_\tau(r)\,dv/(2\tau)-\omega_\tau'(r)\,dr\bigr]\),
while

\[
\omega_\tau'(r)\cdot\frac{1-\tau/r}{2}
=
\frac{r\,e^{r/\tau}}{\tau^{2}}\cdot\frac{r-\tau}{2r}
=
\frac{e^{r/\tau}(r/\tau-1)}{2\tau}
=
\frac{\omega_\tau(r)}{2\tau},
\]

so substituting \(dr=\tfrac12(1-\tau/r)\,dv\) gives \(d\tilde U=0\) **exactly**:
\(\tilde U\) is constant on outgoing null rays, with no approximation and no
near-horizon restriction. Along future-directed ingoing null curves (\(dv=0\),
\(dr<0\)) one has \(d\tilde U=-e^{-v/(2\tau)}\omega_\tau'(r)\,dr>0\). Hence
\((\tilde U,v)\) is a global double-null chart on \(r>0\), smooth across the horizon
\(r=\tau\) (which is the ray \(\tilde U=0\)), both coordinates are non-decreasing
along future-directed causal curves and strictly increasing along the two null
directions, and the causal order is **exactly** the product order:

\[
x\preceq y
\quad\Longleftrightarrow\quad
\tilde U_x\le\tilde U_y
\ \ \text{and}\ \
v_x\le v_y .
\]

**The diamond is the corresponding null box.** For \(\tau\in J\) we have
\(r_q<\tau<r_p\), hence \(\omega_\tau(r_q)<0<\omega_\tau(r_p)\) and therefore
\(\tilde U_p(\tau)<0<\tilde U_q(\tau)\), where \(\tilde U_p(\tau):=\tilde U(p)\) and
\(\tilde U_q(\tau):=\tilde U(q)\); with \(v_p<v_q\) this gives \(q\in J^+_\tau(p)\)
for every \(\tau\in J\). By the product order,

\[
D_\tau=[\tilde U_p(\tau),\,\tilde U_q(\tau)]\times[v_p,v_q],
\]

a nonempty coordinate box straddling the horizon \(\tilde U=0\). Write

\[
r_\tau(\tilde U,v):=\omega_\tau^{-1}\bigl(-e^{v/(2\tau)}\tilde U\bigr)
\]

for the areal radius in the chart; \(r_\tau\) is strictly decreasing in
\(\tilde U\). Its minimum over the closed box is attained at the corner \(q\) and
equals \(r_q\); its maximum is attained at \((\tilde U_p(\tau),v_q)\) and equals
\(r_+(\tau)=\omega_\tau^{-1}\bigl(e^{(v_q-v_p)/(2\tau)}\omega_\tau(r_p)\bigr)\),
continuous in \(\tau\). Consequently, for every compact \(K'\subset J\), with
\(R:=\max_{\tau\in K'}r_+(\tau)<\infty\),

\[
r_\tau(\tilde U,v)\in[r_q,R]\subset(0,\infty)
\qquad\text{for all }(\tilde U,v)\in D_\tau,\ \tau\in K' :
\]

the radial parameter is confined to a **compact interval that does not depend on
\(\tau\)** and is bounded away from \(0\) and \(\infty\). The singularity is avoided
automatically, and \(\omega_\tau'(r)=r\,e^{r/\tau}/\tau^2\) is bounded above and
below by positive constants on that range, uniformly in \(\tau\in K'\).

**Sampling density, normalization and marginals.** Since \(\det g_\tau=-1\), the
volume measure is \(dv\,dr\) and, by Lemma 2.1, the fixed-\(n\) sample is i.i.d.\
uniform on \(D_\tau\) in the \((v,r)\) chart. Differentiating
\(\omega_\tau(r)=-e^{v/(2\tau)}\tilde U\) at fixed \(v\) gives
\(\partial r/\partial\tilde U=-e^{v/(2\tau)}/\omega_\tau'(r)\), so
\(dv\,dr=\bigl(e^{v/(2\tau)}/\omega_\tau'(r_\tau(\tilde U,v))\bigr)\,d\tilde U\,dv\)
and the normalized sampling density on the null box is

\[
\pi_\tau(\tilde U,v)
=
\frac{e^{v/(2\tau)}}{V(\tau)\,\omega_\tau'\bigl(r_\tau(\tilde U,v)\bigr)}
=
\frac{\tau^{2}\,e^{v/(2\tau)}}{V(\tau)\;r\,e^{r/\tau}}\bigg|_{\,r=r_\tau(\tilde U,v)},
\]

normalized by the \(g_\tau\)-area of the diamond,

\[
V(\tau)
:=
\operatorname{vol}_{g_\tau}(D_\tau)
=
\int_{v_p}^{v_q}\!\!\int_{\tilde U_p(\tau)}^{\tilde U_q(\tau)}
\frac{e^{v/(2\tau)}}{\omega_\tau'\bigl(r_\tau(\tilde U,v)\bigr)}\,d\tilde U\,dv
\;\in(0,\infty),
\]

which is the same \(V(\tau)\) used in Theorem 3.9. The two marginals of
\(\pi_\tau\) on the box are

\[
\pi_1(\tilde U;\tau):=\int_{v_p}^{v_q}\pi_\tau(\tilde U,v)\,dv,
\qquad
\pi_2(v;\tau):=\int_{\tilde U_p(\tau)}^{\tilde U_q(\tau)}\pi_\tau(\tilde U,v)\,d\tilde U .
\]

**Distribution functions and quantiles.** Define

\[
F_\tau(\tilde U):=\int_{\tilde U_p(\tau)}^{\tilde U}\pi_1(s;\tau)\,ds,
\qquad
G_\tau(v):=\int_{v_p}^{v}\pi_2(s;\tau)\,ds,
\]

the marginal distribution functions of \(\pi_\tau\) on the box, and let
\(F_\tau^{-1},G_\tau^{-1}:[0,1]\to\) (the respective edges of the box) be the
marginal quantile maps. Their regularity is item (iv) of the next lemma.

**Lemma 3.5 (regularity).** `[PROVED]`  
Let \(K'\subset J\) be compact. Uniformly in \(\tau\in K'\):

(i) \(r_\tau(\tilde U,v)\) is jointly smooth in \((\tilde U,v,\tau)\) on the closed
box, and \(|\partial r/\partial\tilde U|\) is bounded above and below by positive
constants;

(ii) \(\pi_\tau\) is jointly smooth in \((\tilde U,v,\tau)\) and bounded above and
below by positive constants;

(iii) the marginals \(\pi_1(\cdot\,;\tau)\) and \(\pi_2(\cdot\,;\tau)\) are smooth
in all arguments and bounded above and below by positive constants;

(iv) \(F_\tau\) and \(G_\tau\) are \(C^1\) strictly increasing bijections onto
\([0,1]\) with derivatives bounded away from \(0\), and the quantile maps
\((x,\tau)\mapsto F_\tau^{-1}(x)\) and \((y,\tau)\mapsto G_\tau^{-1}(y)\) are
\(C^1\);

(v) consequently the copula density

\[
c_\tau(x,y)
=
\frac{\pi_\tau\bigl(F_\tau^{-1}(x),\,G_\tau^{-1}(y)\bigr)}
     {\pi_1\bigl(F_\tau^{-1}(x);\tau\bigr)\,\pi_2\bigl(G_\tau^{-1}(y);\tau\bigr)},
\qquad (x,y)\in[0,1]^2,
\]

is jointly continuous, \(C^1\) in \(\tau\) with \(\partial_\tau c_\tau\) jointly
continuous, bounded above and below by positive constants, and
\(|\partial_\tau c_\tau|\) is bounded; in particular the score
\(\partial_\tau\log c_\tau\) is bounded uniformly on \([0,1]^2\times K'\).

*Proof.* Write \(\sigma_\tau(\tilde U,v):=e^{v/(2\tau)}/\omega_\tau'\bigl(r_\tau(\tilde
U,v)\bigr)\) for the unnormalized density, so \(\pi_\tau=\sigma_\tau/V(\tau)\).

*Preliminary: a fixed open domain.* The defining relation
\(\omega_\tau(r)=-e^{v/(2\tau)}\tilde U\) has a (unique) solution \(r>0\) exactly
when \(-e^{v/(2\tau)}\tilde U>-1\), because \(\omega_\tau\) is an increasing
bijection \((0,\infty)\to(-1,\infty)\). Hence \(r_\tau\) and \(\sigma_\tau\) are
defined and smooth on the **open** set

\[
\mathcal O:=\bigl\{(\tilde U,v,\tau)\in\mathbb R^3:\ \tau>0,\ e^{v/(2\tau)}\tilde U<1\bigr\},
\]

which contains the compact set
\(\mathcal K:=\{(\tilde U,v,\tau):\tau\in K',\,(\tilde U,v)\in D_\tau\}\) (on the box
the corresponding radius satisfies \(r\ge r_q>0\), so the inequality is strict).
Every differentiation below is performed on \(\mathcal O\); in particular
\(\tau\mapsto\sigma_\tau(\tilde U,v)\) may be differentiated **at fixed
\((\tilde U,v)\)**, including at points that leave the moving box \(D_\tau\). Since
\(\mathcal K\subset\mathcal O\) is compact, it has a compact neighbourhood
\(\mathcal K^+\subset\mathcal O\), and each two-sided bound below is the statement
that a continuous non-vanishing function is pinched on \(\mathcal K^+\).

(i) On \(\mathcal O\) the relation \(\omega_\tau(r)+e^{v/(2\tau)}\tilde U=0\) has
\(r\)-derivative \(\omega_\tau'(r)\), pinched between positive constants on the
uniform compact radial range \([r_q,R]\) established above; the implicit function
theorem with smooth data gives joint smoothness of \(r_\tau\) and
\(\partial r/\partial\tilde U=-e^{v/(2\tau)}/\omega_\tau'(r)\), whose modulus is
pinched because \(v\) runs over the compact \([v_p,v_q]\).

(ii) By (i), \(\sigma_\tau\) is smooth on \(\mathcal O\) and pinched between positive
constants on \(\mathcal K^+\). The normalizer has **fixed** limits in \(v\) and
**moving** limits in \(\tilde U\); the Leibniz rule for variable limits (smooth
integrand on \(\mathcal O\), edges \(\tilde U_p(\tau),\tilde U_q(\tau)\) explicit
smooth functions of \(\tau\)) gives that \(V\) is smooth with

\[
V'(\tau)=\int_{v_p}^{v_q}\Bigl[
\tilde U_q'(\tau)\,\sigma_\tau\bigl(\tilde U_q(\tau),v\bigr)
-\tilde U_p'(\tau)\,\sigma_\tau\bigl(\tilde U_p(\tau),v\bigr)
+\int_{\tilde U_p(\tau)}^{\tilde U_q(\tau)}\partial_\tau\sigma_\tau\,d\tilde U
\Bigr]dv .
\]

Moreover \(0<V(\tau)<\infty\) with both bounds uniform on \(K'\), since
\(\sigma_\tau\) is pinched and the box has edge lengths \(v_q-v_p>0\) (fixed) and
\(\tilde U_q(\tau)-\tilde U_p(\tau)\), continuous and strictly positive on the
compact \(K'\), hence pinched. Therefore \(\pi_\tau=\sigma_\tau/V(\tau)\) is smooth
on \(\mathcal O\) and pinched on \(\mathcal K^+\).

(iii) The two marginals are of different types and must be treated separately.
\(\pi_1(\tilde U;\tau)=\int_{v_p}^{v_q}\pi_\tau\,dv\) has **fixed** limits: ordinary
differentiation under the integral sign (smooth integrand, compact fixed interval)
gives joint smoothness in \((\tilde U,\tau)\), with no boundary terms.
\(\pi_2(v;\tau)=\int_{\tilde U_p(\tau)}^{\tilde U_q(\tau)}\pi_\tau\,d\tilde U\) has
**moving** limits: the same Leibniz rule as in (ii) gives joint smoothness in
\((v,\tau)\), with the two boundary terms
\(\tilde U_q'(\tau)\pi_\tau(\tilde U_q(\tau),v)-\tilde U_p'(\tau)\pi_\tau(\tilde
U_p(\tau),v)\). In both cases the two-sided bounds are the pinching of \(\pi_\tau\)
multiplied by the corresponding interval length, itself pinched by (ii).

(iv) \(G_\tau(v)=\int_{v_p}^{v}\pi_2\,ds\) has a fixed lower limit; \(F_\tau(\tilde
U)=\int_{\tilde U_p(\tau)}^{\tilde U}\pi_1\,ds\) has a **moving** lower limit and
therefore acquires the boundary term \(-\tilde U_p'(\tau)\,\pi_1(\tilde
U_p(\tau);\tau)\) on differentiating in \(\tau\); both are jointly \(C^1\), and
\(F_\tau(\tilde U_q(\tau))=G_\tau(v_q)=1\) by normalization, so each is a strictly
increasing bijection onto \([0,1]\) with \(F_\tau'=\pi_1>0\) and \(G_\tau'=\pi_2>0\)
bounded away from \(0\) by (iii). The implicit function theorem applied to
\(F_\tau(\tilde U)-x=0\) and \(G_\tau(v)-y=0\) then gives joint \(C^1\) dependence of
the inverses on \((x,\tau)\) and \((y,\tau)\), one-sided in \(x,y\) at the endpoints
\(0,1\) (where the inverses return the box edges).

(v) Compose (ii)–(iv): the quotient has smooth numerator and denominator bounded
away from \(0\); each factor is \(C^1\) in \(\tau\) with jointly continuous
\(\tau\)-derivative, so \(\partial_\tau c_\tau\) is jointly continuous on the
compact \([0,1]^2\times K'\) and hence bounded there; all bounds are uniform because
every ingredient is pinched on compact domains. Boundedness of the score follows
from \(|\partial_\tau\log c_\tau|\le|\partial_\tau c_\tau|/c_{\min}\).
\(\blacksquare\)  
(Traceability, not a dependency: annex Lemma R.)

**Proposition 3.6 (QMD and finite Fisher).** `[PROVED]`  
The Fisher information
\(I(\tau)=\int_{[0,1]^2}(\partial_\tau\log c_\tau)^2\,c_\tau\) is finite and
continuous on \([\tau_0,\tau_1]\); set \(\bar I:=\sup I(\tau)<\infty\). The family
is differentiable in quadratic mean, and, writing \(J_\delta\) for the closed
interval with endpoints \(\tau\) and \(\tau+\delta\),

\[
H^2(c_\tau,c_{\tau+\delta})
\;\le\;
|\delta|\int_{J_\delta}\frac{I(s)}{4}\,ds
\;\le\;
\frac{\delta^2}{4}\,\bar I.
\]

*Proof.* **Finiteness and continuity of \(I\).** By Lemma 3.5(v) the integrand
\((\partial_\tau\log c_\tau)^2c_\tau\) is bounded uniformly on
\([0,1]^2\times[\tau_0,\tau_1]\) and, for each \((x,y)\), continuous in \(\tau\).
The unit square carries finite Lebesgue measure, so dominated convergence gives
both finiteness of \(I(\tau)\) and continuity of \(I\) on \([\tau_0,\tau_1]\);
compactness then gives \(\bar I=\sup I=\max I<\infty\) — the supremum is attained,
and in particular finite.

**Integrated bound.** Since \(c_\tau\ge c_{\min}>0\) and \(c_\tau\) is \(C^1\) in
\(\tau\) (Lemma 3.5(v)), \(\sqrt{c_\tau}\) is \(C^1\) in \(\tau\) with
\(\partial_\tau\sqrt{c_\tau}=\partial_\tau c_\tau/(2\sqrt{c_\tau})\) bounded, and

\[
\int_{[0,1]^2}\bigl(\partial_s\sqrt{c_s}\bigr)^2
=
\frac14\int_{[0,1]^2}\frac{(\partial_s c_s)^2}{c_s}
=
\frac{I(s)}{4}.
\]

Taking \(\delta>0\) (the case \(\delta<0\) is identical with the endpoints
exchanged), the fundamental theorem of calculus and Cauchy–Schwarz along the
parameter path give, pointwise in \((x,y)\),

\[
\bigl(\sqrt{c_{\tau+\delta}}-\sqrt{c_\tau}\bigr)^2
=
\Bigl(\int_\tau^{\tau+\delta}\partial_s\sqrt{c_s}\,ds\Bigr)^{\!2}
\le
\delta\int_\tau^{\tau+\delta}\bigl(\partial_s\sqrt{c_s}\bigr)^2 ds ;
\]

integrating over \([0,1]^2\) and applying Fubini (the integrand is bounded on a
finite-measure product) yields the displayed bound. No expansion in \(\delta\) is
used, so the bound holds for **every** admissible \(\delta\), not only
asymptotically; \(\bar I<\infty\) is exactly what makes it uniform over the
parameter interval.

**QMD.** In copula coordinates the family lives on a **fixed** domain: every
\(c_\tau\) is a probability density on the same unit square with respect to
Lebesgue measure, the \(\tau\)-dependent box edges having been absorbed by the
quantile transforms of Lemma 3.5(iv). In this compact, smooth, fixed-domain
setting the definition of quadratic-mean differentiability can be verified
directly. By Lemma 3.5(v), \(c_\tau\ge c_{\min}>0\) and \(\partial_\tau c_\tau\) is
jointly continuous, so

\[
(z,\tau)\longmapsto\partial_\tau\sqrt{c_\tau(z)}
=\frac{\partial_\tau c_\tau(z)}{2\sqrt{c_\tau(z)}}
=\tfrac12\bigl(\partial_\tau\log c_\tau(z)\bigr)\sqrt{c_\tau(z)}
\]

is continuous on the compact \([0,1]^2\times K'\), hence bounded and **uniformly**
continuous there. Fix \(\tau\in[\tau_0,\tau_1]\), which is interior to \(J\), and put

\[
G_\delta(z)
:=\sqrt{c_{\tau+\delta}(z)}-\sqrt{c_\tau(z)}-\delta\,\partial_\tau\sqrt{c_\tau(z)}
=\int_0^\delta\Bigl[\partial_s\sqrt{c_s(z)}\big|_{s=\tau+u}-\partial_\tau\sqrt{c_\tau(z)}\Bigr]du .
\]

Uniform continuity gives \(\sup_z|G_\delta(z)|\le|\delta|\,\varepsilon(\delta)\) with
\(\varepsilon(\delta)\to0\) as \(\delta\to0\), so \(\int_{[0,1]^2}G_\delta^2=o(\delta^2)\):
the family is differentiable in quadratic mean at \(\tau\), with \(L^2\)-derivative
\(\partial_\tau\sqrt{c_\tau}\) and score \(\partial_\tau\log c_\tau\). Expanding
\(H^2(c_\tau,c_{\tau+\delta})=\int(\delta\,\partial_\tau\sqrt{c_\tau}+G_\delta)^2\)
and bounding the cross term by Cauchy–Schwarz yields the local form
\(H^2(c_\tau,c_{\tau+\delta})=(\delta^2/4)I(\tau)+o(\delta^2)\), since
\(\int(\partial_\tau\sqrt{c_\tau})^2=I(\tau)/4\). \(\blacksquare\)

*Relation to the standard criterion, and what depends on it.* The three properties
used above — an open parameter set with a \(\tau\)-independent dominating measure;
\(\tau\mapsto\sqrt{c_\tau(z)}\) continuously differentiable for every \(z\); and a
finite, continuous Fisher information — are exactly the hypotheses of the textbook
sufficient condition for QMD (van der Vaart [11, Lemma 7.6]), and the open interval
\(J\) of the construction is what supplies the first. We record the correspondence
for orientation only: **nothing here relies on that citation**, whose edition is not
held in the local library (`[UNVERIFIED]` as to numbering; the locally held
\(L^2\)-differentiability treatment gives the same statement under the same
hypotheses), because the two displays above verify the definition directly. Nor
does **Theorem 3.8 depend on QMD at all**: the floor uses only the non-asymptotic
integrated bound, which is proved by Cauchy–Schwarz without any expansion.
(Hellinger convention \(H^2=\int(\sqrt p-\sqrt q)^2\in[0,2]\) as in §2.3.
Traceability, not a dependency: annex Prop.\ 4.)

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

*Proof.*  
**(1).** By Lemma 2.1 the \(n\) points are i.i.d.\ from the normalized volume
measure on \(D_\tau\). By §3.3.2, \(D_\tau\) is a coordinate box in the global
double-null chart \((\tilde U,v)\), in which the causal order is exactly the product
order, so Lemma 2.2 applies: the fixed-\(n\) unlabeled poset law depends on
\(g_\tau\) only through the copula \(c_\tau\). Concretely, the coordinatewise
quantile transform \((\tilde U,v)\mapsto(F_\tau(\tilde U),G_\tau(v))\) is increasing
in each coordinate, hence order-preserving, and carries the sample to \(n\)
i.i.d.\ points of \([0,1]^2\) with density \(c_\tau\); the induced map \(\Phi\)
from \(n\) unit-square points to the unlabeled poset is *the same* measurable map
for every \(\tau\), all of the \(\tau\)-dependence having been moved into
\(c_\tau\). Proposition 3.6 gives
\(H^2(c_\tau,c_{\tau+\delta})\le\delta^2\bar I/4\); the tensorization corollary of
§2.3 gives
\(H^2\bigl(c_\tau^{\otimes n},c_{\tau+\delta}^{\otimes n}\bigr)\le n\delta^2\bar
I/4\); and data processing under \(\Phi\) together with \(\mathrm{TV}\le H\) gives

\[
\mathrm{TV}\bigl(Q^n_\tau,Q^n_{\tau+\delta}\bigr)
\;\le\;
H\bigl(c_\tau^{\otimes n},c_{\tau+\delta}^{\otimes n}\bigr)
\;\le\;
\frac{|\delta|}{2}\sqrt{n\bar I}.
\]

**(2).** Put \(A:=\{|\widehat\tau-\tau|<|\delta|/2\}\). On \(A\) the triangle
inequality gives \(|\widehat\tau-(\tau+\delta)|\ge|\delta|-|\widehat\tau-\tau|>
|\delta|/2\), so \(A\subseteq\{|\widehat\tau-(\tau+\delta)|\ge|\delta|/2\}\), while
\(A^c=\{|\widehat\tau-\tau|\ge|\delta|/2\}\). Hence

\[
\mathbb{P}_\tau\bigl(|\widehat\tau-\tau|\ge|\delta|/2\bigr)
+
\mathbb{P}_{\tau+\delta}\bigl(|\widehat\tau-(\tau+\delta)|\ge|\delta|/2\bigr)
\;\ge\;
1-\bigl[\mathbb{P}_\tau(A)-\mathbb{P}_{\tau+\delta}(A)\bigr]
\;\ge\;
1-\mathrm{TV}\bigl(Q^n_\tau,Q^n_{\tau+\delta}\bigr),
\]

by the definition of \(\mathrm{TV}\) as a supremum over events; now insert (1).
For randomized \(\widehat\tau=f(C_n,U)\) with \(U\) independent of the data, the
same computation runs on the product space, whose total variation is again
\(\mathrm{TV}(Q^n_\tau,Q^n_{\tau+\delta})\) because the extra factor is common to
both models.

**(3).** If some order-only procedure had both error probabilities at most
\(\varepsilon\), then by (2) \(2\varepsilon\ge1-(|\delta|/2)\sqrt{n\bar I}\), i.e.
\(|\delta|\ge2(1-2\varepsilon)/\sqrt{n\bar I}\). The contrapositive is (3), with the
inequality strict as stated. \(\blacksquare\)

(The two-point testing inequality and the data-processing / \(\mathrm{TV}\le H\)
steps are `[BACKGROUND]`, §2.3 and [10]. Traceability, not a dependency: annex §5
and `wp4_two_point_theorem.md`.)

#### Theorem 3.9 (fixed-\(n\) separation by comparable-pair count)
`[PROVED]` · Label: `PROVED_FIXED_N_SEPARATION`

Retain the diamond family above and put \(dv:=v_q-v_p>0\) and
\(K:=[\tau_0,\tau_1]\). Let \(p(\tau)\) be the probability that two independent
points drawn from normalized volume on \(D_\tau\) are causally comparable, and let
\(S_n\) be the number of comparable unordered pairs in the observed unlabeled
poset. Define

\[
\kappa(r_p,r_q)
:=
\frac{(r_p^2-r_q^2)-2r_pr_q\log(r_p/r_q)}
     {12r_pr_q(r_p-r_q)^2}
>0.
\]

There exists
\(dv_0=dv_0(r_p,r_q,\tau_0,\tau_1)>0\) such that, for every fixed
\(0<dv<dv_0\):

1. **Uniform mean separation on \(K\).** The map \(\tau\mapsto p(\tau)\) is
   strictly increasing and, for all \(\tau,\tau'\in K\),
   \[
   |p(\tau')-p(\tau)|
   \;\ge\;
   \frac{\kappa(r_p,r_q)\,dv}{2}\,|\tau'-\tau|.
   \]
2. **Fixed-pair total-variation separation.** For every \(n\ge2\) and every
   fixed pair \(\tau\ne\tau'\) in \(K\),
   \[
   \mathrm{TV}(Q^n_\tau,Q^n_{\tau'})
   \;\ge\;
   1-
   \frac{4(2n-3)}
        {n(n-1)|p(\tau')-p(\tau)|^2}
   \;\longrightarrow\;1.
   \]
   Thus the midpoint test based only on \(S_n\) is consistent for each fixed
   pair.
3. **Separated and moving alternatives.** The testing cardinality \(n_0\) is
   pair-dependent when distinct parameters may approach one another. It is uniform
   on sets satisfying \(|\tau'-\tau|\ge\eta>0\). More generally, for any sequences
   \(\tau_n,\tau_n'\in K\) with
   \(\sqrt n\,|\tau_n'-\tau_n|\to\infty\), the same \(S_n\)-test has total error
   tending to zero.

*Proof.* Write \(a:=r_p\), \(b:=r_q\), \(d:=dv\). Put
\(\omega_\tau(r):=e^{r/\tau}(r/\tau-1)\), a strictly increasing bijection
\((0,\infty)\to(-1,\infty)\) with \(\omega_\tau(\tau)=0\) and
\(\omega_\tau'(r)=r\,e^{r/\tau}/\tau^2>0\). Then
\(\tilde U:=-e^{-v/(2\tau)}\omega_\tau(r)\) is the exactly null coordinate of
§2.1, \((\tilde U,v)\) is a global double-null chart on \(r>0\), and the causal
order is the product order with **both coordinates increasing to the future**:
for \(x,y\in D_\tau\),
\[
x\prec y
\quad\Longleftrightarrow\quad
\tilde U_x\le\tilde U_y
\ \ \text{and}\ \
v_x\le v_y .
\]
At fixed \(v\), \(\tilde U\) is strictly decreasing in \(r\), and the horizon
\(r=\tau\) is the ray \(\tilde U=0\). Let \(\rho_\tau(r_0,D)\) be the areal radius
at \(v=v_0+D\) of the outgoing null ray through \((v_0,r_0)\), i.e. the solution
of \(\omega_\tau(\rho)=e^{D/(2\tau)}\omega_\tau(r_0)\); differentiating,
\[
\frac{\partial\rho}{\partial D}=\frac{\rho-\tau}{2\rho},
\qquad
\rho_\tau(r_0,0)=r_0 .
\]
(The subscript distinguishes \(\rho_\tau\) from the sprinkling intensity \(\rho\)
of §2.3.)

**Reduction to a two-fold integral.** By §2.1, \(\det g_\tau=-1\), so
\(\mathrm{vol}_{g_\tau}=dv\,dr\) and the normalized sampling law on \(D_\tau\) is
absolutely continuous with respect to \(dv\,dr\) (indeed uniform). Consequently
the coincidence sets \(\{\tilde U_x=\tilde U_y\}\) and \(\{v_x=v_y\}\), and the
null boundaries of \(D_\tau\), all carry product measure zero, so two independent
points are a.s. untied and the trichotomy \(x\prec y\), \(y\prec x\), spacelike is
a.s. clean. Both sides of
\[
\int_{v_0}^{v_0+D}\rho_\tau(r_0,v-v_0)\,dv=\rho_\tau(r_0,D)^2-r_0^2+\tau D
\]
vanish at \(D=0\) and have the same \(D\)-derivative by the ray flow, so they
agree. At fixed \(v\in[v_x,v_q]\), \(\tilde U\) is decreasing in \(r\), so the
slice of \(J^+(x)\cap J^-(q)\) is \(\{r:R_q(v)\le r\le R_x(v)\}\) between the
outgoing rays through \(q\) and through \(x\), non-empty precisely because
\(\tilde U_x\le\tilde U_q\); integrating and cancelling the two \(\tau D\) terms
gives, for \(x=(v_x,r_x)\in D_\tau\) and \(D:=v_q-v_x\),
\[
\operatorname{vol}\bigl(J^+(x)\cap D_\tau\bigr)
=\rho_\tau(r_x,D)^2+\rho_\tau(r_q,-D)^2-r_x^2-r_q^2 ,
\]
and in particular
\(V(\tau)=\rho_\tau(r_p,dv)^2+\rho_\tau(r_q,-dv)^2-r_p^2-r_q^2\). Points are
exchangeable and a.s. untied, and comparability in a product order means exactly
\(x\prec y\) or \(y\prec x\), so \(p=2\,\mathbb P(X\prec Y)\); Fubini then gives,
with \(\alpha(D):=\rho_\tau(r_p,dv-D)\) and \(\beta(D):=\rho_\tau(r_q,-D)\),
\[
p(\tau)=\frac{2}{V(\tau)^2}\int_0^{dv}\!\!\int_{\beta(D)}^{\alpha(D)}
\bigl[\rho_\tau(r,D)^2+\beta(D)^2-r^2-r_q^2\bigr]\,dr\,dD .
\]

**Step 1 (one uniform analytic neighbourhood).** The flow is defined implicitly by
\(F(\tau,r,D,y):=\omega_\tau(y)-e^{D/(2\tau)}\omega_\tau(r)=0\), with
\(\partial_yF=\omega_\tau'(y)>0\) and \(y=r\) at \(D=0\). The real-analytic
implicit-function theorem makes \(\rho_\tau\) jointly real-analytic in
\((\tau,r,D)\) near every \((\tau,r,0)\) with \(\tau,r>0\). A finite subcover of
the product of a compact \(\tau\)-interval slightly larger than \(K\) (still
inside \((b,a)\)) with a compact positive \(r\)-interval containing \([b,a]\)
yields one \(\eta>0\) on which \(\rho_\tau\) is jointly analytic for \(|D|<\eta\);
the local branches agree because \(\omega_\tau\) is strictly increasing.

**Step 2 (fixed square and analytic division).** For \(s,u\in[0,1]\) put
\(A:=\rho_\tau(a,(1-s)d)\), \(B:=\rho_\tau(b,-sd)\), \(x:=B+u(A-B)\) and
\(H:=\rho_\tau(x,sd)^2+B^2-x^2-b^2\). Since \(A-B=a-b>0\) at \(d=0\), one uniform
shrink of \(\eta\) keeps \(A>B\). The substitutions \(D=sd\) and \(r=B+u(A-B)\)
turn the numerator of the display above into
\(N(\tau,d)=d\int_0^1\!\!\int_0^1(A-B)H\,du\,ds\). At \(d=0\) one has \(H=0\), so
analytic division \(H=d\widehat H\), with
\(\widehat H=\int_0^1\partial_dH(\tau,s,u,\lambda d)\,d\lambda\), gives
\(N=d^2\widehat N\) with \(\widehat N\) jointly analytic — compactness of the unit
square supplies one common analytic neighbourhood, so the local power series may
be integrated term by term. Likewise \(V(\tau,d)=d\widehat V\) with
\(\widehat V(\tau,0)=a-b>0\) uniformly in \(\tau\), since \(V(\tau,0)=0\) and
\(\partial_dV(\tau,0)=a-b\) by the ray flow. After one further uniform shrink of
\(\eta\), \(\widehat V\) has no zero near \(K\times\{0\}\), so
\(P(\tau,d):=2\widehat N(\tau,d)/\widehat V(\tau,d)^2\)
is a jointly real-analytic extension through \(d=0\) of \(p(\tau)\) for \(d>0\).

**Step 3 (first two coefficients).** Expanding the flow from its ODE,
\(\rho_\tau(r,D)=r+D\,(r-\tau)/(2r)+D^2\tau(r-\tau)/(8r^3)+O(D^3)\), substituting
and integrating the retained coefficients (antiderivatives \(r(r-2\tau)/2\) and
\(r/4-\tau\log r/4\)) gives \(\widehat N(\tau,0)=(a-b)^2/4\),
\(\widehat V(\tau,0)=a-b\), hence \(P(\tau,0)=1/2\) and
\(\partial_dP(\tau,0)=\kappa(r_p,r_q)\,\tau\). Writing
\[
p(\tau)
=
\frac12+\kappa(r_p,r_q)\tau\,dv+R(\tau,dv)
\]
defines \(R\).

**Step 4 (uniform remainder).** Choose \(0<\varepsilon<\eta\) with
\(K\times[-\varepsilon,\varepsilon]\) inside the analytic domain of \(P\) and set
\(C_1:=\tfrac12\max_{K\times[-\varepsilon,\varepsilon]}
|\partial_\tau\partial_d^2P|\), finite by compactness and depending only on
\((r_p,r_q,\tau_0,\tau_1)\). Taylor's formula with integral remainder gives, for
\(0\le dv\le\varepsilon\),
\[
\partial_\tau R(\tau,dv)
=
dv^2\int_0^1(1-z)\,\partial_\tau\partial_d^2P(\tau,z\,dv)\,dz ,
\qquad
|\partial_\tau R(\tau,dv)|\le C_1dv^2
\]
uniformly for \(\tau\in K\).

**Positivity of \(\kappa\) and choice of \(dv_0\).** With \(x:=r_p/r_q>1\) the
numerator of \(\kappa\) is \(2r_pr_q\varphi(x)\), where
\(\varphi(x):=(x-1/x)/2-\log x\); since \(\varphi(1)=0\) and
\(\varphi'(x)=(x-1)^2/(2x^2)>0\) for \(x\ne1\), \(\varphi>0\) on \((1,\infty)\)
and \(\kappa>0\). Step 4 then gives
\(\partial_\tau p(\tau)\ge\kappa\,dv-C_1dv^2\) on \(K\). Take
\[
dv_0:=
\begin{cases}
\varepsilon, & C_1=0,\\
\min\{\varepsilon,\ \kappa/(2C_1)\}, & C_1>0;
\end{cases}
\]
then \(\partial_\tau p\ge\kappa\,dv/2>0\) throughout \(K\) for every
\(0<dv<dv_0\), which is (1). The bound on \(R\) alone would give separation only
for each pre-fixed pair; the \(\partial_\tau R\) bound is what makes one \(dv_0\)
serve the whole interval. (Traceability, not a dependency: the same argument is
§4 of `wp4_comparable_pair_separation.md`.)

For the symmetric Bernoulli kernel
\(f(x,y)=\mathbf 1\{x,y\text{ comparable}\}\), the exact fixed-\(n\)
Hoeffding identity is
\[
\operatorname{Var}_\tau(S_n)
=
\binom n2\{2(n-2)\zeta_{1,\tau}+\zeta_{2,\tau}\}.
\]
Here
\(\zeta_{1,\tau}:=\operatorname{Var}_\tau(
\mathbb E_\tau[f(X,Y)\mid X])\) and
\(\zeta_{2,\tau}:=\operatorname{Var}_\tau(f(X,Y))\). Since both variables inside
these variances take values in \([0,1]\),
\(\zeta_{1,\tau},\zeta_{2,\tau}\le1/4\), and hence
\[
\operatorname{Var}_\tau(S_n)
\le
\binom n2\frac{2n-3}{4}.
\]
The two means differ by
\(\Delta_m=\binom n2|p(\tau')-p(\tau)|\). Chebyshev's inequality at their midpoint
bounds the sum of the two testing errors by
\[
\frac{4\{\operatorname{Var}_\tau(S_n)+
          \operatorname{Var}_{\tau'}(S_n)\}}{\Delta_m^2}
\le
\frac{4(2n-3)}
     {n(n-1)|p(\tau')-p(\tau)|^2}.
\]
For any test, total variation is at least one minus its total error; data
processing is legitimate because \(S_n\) is a function of the unlabeled poset.
This proves (2), and combining it with (1) gives (3). \(\blacksquare\)

#### Corollary 3.10 (sharp boundary exponent in the \(o/\omega\) sense)
`[PROVED]`

For fixed admissible \(0<dv<dv_0\), Theorems 3.8–3.9 locate the statistical
boundary at exponent \(n^{-1/2}\):

- if \(|\delta_n|=o(n^{-1/2})\), then
  \(\mathrm{TV}(Q^n_{\tau_n},Q^n_{\tau_n+\delta_n})\to0\) whenever both endpoints
  remain in \(K\);
- if \(|\delta_n|=\omega(n^{-1/2})\), the comparable-pair test separates the two
  laws with total error tending to zero.

This does not identify the critical-scale constant when
\(|\delta_n|\asymp n^{-1/2}\), and it does not claim that \(S_n\) is
constant-optimal.

#### What Theorems 3.8–3.9 do and do not claim

| Claims | Does **not** claim |
|---|---|
| A lower bound on risk for **all** order-only estimators (randomized included) | That the bound is **tight** for posets (it is inherited by data processing from the point process and may be loose) |
| A consistent test based on one order-only statistic for every fixed pair, at sufficiently small \(dv\) | A numerically certified value of \(dv_0\), or monotonicity at arbitrary \(dv\) |
| Boundary exponent \(n^{-1/2}\) in the \(o/\omega\) sense on this named family | Constant optimality, or a conclusion at \(\lvert\delta_n\rvert=c/\sqrt n\) |
| One \(dv_0\) uniform over \(\tau\in K\) | One \(n_0\) uniform over all \(\tau\ne\tau'\); this requires \(\lvert\tau-\tau'\rvert\ge\eta>0\) |
| Techniques: QMD, Hellinger, Hoeffding moments, Chebyshev, and two-point testing | Novelty of that statistical machinery `[BACKGROUND]` (textbook) |
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
\(\kappa_{\mathrm{dim}}(\tau):=V(\tau)\,I(\tau)\) is exactly dilation-invariant
(annex §5a): it depends
on the dimensionless shape of the diamond, not on absolute size. With
\(n=\rho V\) and \(\ell=\rho^{-1/2}\),

\[
\frac{\delta_n}{\ell}
\;\sim\;
\frac{1}{\sqrt{\bar\kappa_{\mathrm{dim}}}},
\qquad
\bar\kappa_{\mathrm{dim}}
:=
V\cdot\bar I.
\]

`[BACKGROUND]` Dimensionally, Fisher information for a length parameter scales as
\(\mathrm{length}^{-2}\) and area as \(\mathrm{length}^{2}\), so \(V\cdot I\) is
dimensionless. The annex proves the invariance on this family; we do **not** present
\(\kappa_{\mathrm{dim}}\) as an independent novelty theorem.

### 3.4 Summary of §3

- **Thm 3.1**
  - *Target:* Absolute \(r_s\) or \(M\)
  - *Channel:* order-only, \(N=n\)
  - *Guarantee:* \(\mathrm{TV}=0\) on dilation orbit (1+1 and scoped 3+1)
  - *Label:* `PROVED_NON_IDENTIFIABILITY`
- **Thm 3.2**
  - *Target:* Global event horizon
  - *Channel:* data from a finite causally convex patch
  - *Guarantee:* not a functional of those data
  - *Label:* `PROVED_NON_IDENTIFIABILITY`
- **Thm 3.8**
  - *Target:* Parameter \(\tau\) of the EF diamond family
  - *Channel:* order-only, \(N=n\)
  - *Guarantee:* floor \(\sim 1/\sqrt{n\bar I}\)
  - *Label:* `PROVED_NON_IDENTIFIABILITY` (rate)
- **Thm 3.9 / Cor 3.10**
  - *Target:* Same parameter and family, \(0<dv<dv_0\)
  - *Channel:* order-only, \(N=n\)
  - *Guarantee:* fixed-pair \(\mathrm{TV}\to1\); matching \(n^{-1/2}\) boundary
    exponent
  - *Label:* `PROVED_FIXED_N_SEPARATION`
- **Prop 3.3–3.4**
  - *Target:* design of families
  - *Channel:* —
  - *Guarantee:* Kruskal sterile; fixed EF box non-regular
  - *Label:* `[REMARK]`

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

- **C3-early**
  - *Construction:* Future-width / funnel collapse as horizon proxy
  - *Terminal:* `REJECTED_HAYWARD`
  - *Lesson:* Funnel tracks singularity truncation, not trapping (fails regular
    Hayward control)
  - *Program label:* `EMPIRICAL_FAILURE_OF_CLASS_L`
- **C1**
  - *Construction:* Bottleneck / ideal / flow through `Max`
  - *Terminal:* `BLOCKED_UNCLOSED` + `MAX_TRIVIAL`
  - *Lesson:* Finite `Max` trivializes; definition never closed as frozen
    localizer
  - *Program label:* `EMPIRICAL_FAILURE_OF_CLASS_L`
- **C2**
  - *Construction:* Common-future overlap / \(\kappa\) on a wavefront
  - *Terminal:* `BLOCKED_E_INDEP` + `TRUNCATION`
  - *Lesson:* Without null structure + ceiling control, confounds with box
    truncation
  - *Program label:* `EMPIRICAL_FAILURE_OF_CLASS_L`
- **C3-third**
  - *Construction:* Truncated-future selectors \((L,V)\) on minimals
  - *Terminal:* `INCONCLUSIVE_EDGE_MARGINAL`
  - *Lesson:* Edge-dominated marginal channel; insufficient pair synergy
  - *Program label:* `EMPIRICAL_FAILURE_OF_CLASS_L`
- **C4**
  - *Construction:* Common-future convergence conditioned on neighbors
  - *Terminal:* `REJECTED_NO_E_M`
  - *Lesson:* No order-only, relabel-invariant neighbor graph \(E_M\)
    (decision 039)
  - *Program label:* `EMPIRICAL_FAILURE_OF_CLASS_L`
- **C5**
  - *Construction:* Global common-future matrix → spectral block / partition
  - *Terminal:* `EXHAUSTED` (F3)
  - *Lesson:* Wall \(\neq\) `Max`; twin/bridge ambiguity; no lateral dual
    (040–041)
  - *Program label:* `EMPIRICAL_FAILURE_OF_CLASS_L`
- **C6**
  - *Construction:* Antichain waist \(W(p,q)\) of an Alexandrov interval
  - *Terminal:* `BLOCKED_NO_STABLE_CODIM2`
  - *Lesson:* Antichain exists as order object; stable codim-2 screen and
    transport do not
  - *Program label:* `EMPIRICAL_FAILURE_OF_CLASS_L`

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

Three qualifications keep those results from being read as more than background
here. First, **dimension**: Braun assumes \(d\ge 3\) (p.\ 2) and Madsen’s rate is
optimised for \(d>2\) (Thm.\ 4.18), so neither covers the \(1{+}1\) setting of
Theorem 3.1. Second, **what Braun’s hypothesis consumes**: his Theorem 1.4
requires the laws of the adjacency matrices to agree *for every* \(k\in\mathbb{N}\),
and the proof passes to the projective limit \(\nu_\infty\); it is a statement about
the full order data at all cardinalities, not about any scalar summary or any single
\(k\). Third, **what kind of statement it is**: Theorem 1.4 is an
identifiability-in-law result — an injectivity statement with no estimator, no rate,
and no finite-\(n\) risk bound. It therefore neither competes with nor is weakened by
finite-\(n\) risk statements such as Theorem 3.1; the two occupy different layers.
Braun’s sampling model does, however, coincide with the channel used here: he models
\(\{X_1,\dots,X_k\}\) as “the random support of a PPP conditioned on \(k\) elements”
(p.\ 4), i.e.\ fixed-cardinality conditioning.

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
direction is complementary to Theorems 3.8–3.9: they give **constructive upper
rates** for spacelike-distance functionals; Theorem 3.8 gives an
**estimator-independent lower bound** for a named parametric family, while
Theorem 3.9 supplies an elementary order-only test attaining the same boundary
exponent for that family. Theorem 3.9 is not a spacelike-distance estimator, and
neither line implies the other.

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

Quadratic-mean differentiability, Hellinger tensorization, data processing,
Hoeffding variance identities, Chebyshev testing, and two-point (Le Cam) lower
bounds are textbook
(`[BACKGROUND]`; e.g.\ van der Vaart, *Asymptotic Statistics*; Tsybakov,
*Introduction to Nonparametric Estimation*). Theorems 3.8–3.9 claim the
**instantiation**: a geometric family for which regularity, a uniform small-lapse
expansion of a concrete order statistic, and both sides of the \(n^{-1/2}\)
boundary exponent are proved. Several “natural” alternative families are
degenerate or non-regular (Section 3.3.1). We do not claim a new method of
nonparametric statistics or an optimal critical-scale constant.
The independent check required by project Paso D, item 5 was completed with
responses from both tiers on 2026-07-28. Neither reader found a prior containing
the family-specific localization-floor instantiation now stated as Theorem 3.8,
but both treated the machinery after QMD as standard and identified residual
literature in random geometric graphs and latent-space models. Theorem 3.9 has
not yet received a theorem-specific priority audit and is advanced here without a
novelty claim. Absolute priority language remains disallowed.

### 6.6 What we do not cite as competition

We do not treat failures of particular estimators in the literature—or our own
ledger—as proofs of non-identifiability. Conversely, we do not treat continuum
reconstruction theorems under order+number hypotheses as refutations of
fixed-\(n\) order-only blindness for absolute mass.

---

## §7 What is closed, open, and abandoned

### 7.1 Closed in this paper

- Absolute \(r_s\) / \(M\) from order-only data at fixed \(N=n\) (stated families)
  - *Status:* **Non-identifiable** (\(\mathrm{TV}=0\) on the orbit)
  - *Where:* Thm 3.1 · `PROVED_NON_IDENTIFIABILITY`
- Global event horizon from a single finite causally convex patch
  - *Status:* **Not a functional** of patch data
  - *Where:* Thm 3.2 · `PROVED_NON_IDENTIFIABILITY`
- Localization rate for \(\tau\) on the regular EF diamond family
  - *Status:* **Floor** \(\sim n^{-1/2}\)
  - *Where:* Thm 3.8 · `PROVED_NON_IDENTIFIABILITY` (rate)
- Fixed-\(n\) separation of \(\tau\ne\tau'\) by comparable-pair count, for
  \(0<dv<dv_0\)
  - *Status:* **Consistent for each fixed pair**; matching \(o/\omega\) boundary
    exponent
  - *Where:* Thm 3.9 / Cor 3.10 · `PROVED_FIXED_N_SEPARATION`
- Sealed future-volume in-patch score under prereg-002
  - *Status:* **PASS** (caveated artifact status)
  - *Where:* §4 · `VALIDATED` (caveated)
- Named region-localizers C1–C6 in this bank
  - *Status:* **Terminated** as listed
  - *Where:* §5 · `EMPIRICAL_FAILURE_OF_CLASS_L`

### 7.2 Abandoned as program north

```text
ABANDONED_AS_PROGRAM_NORTH:
  further order-only region-locators aimed at Schwarzschild
  3+1 horizon structure (global EH, trapping, codim-2 screen,
  or proxy) in the post-PR008 candidate line.
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
| Numerical \(\bar I\) / \(\bar\kappa_{\mathrm{dim}}\) for reference diamonds | `OPEN` / NUMERICAL where marked | Deterministic generators only |
| Regular parametric family + Fisher floor in \(3{+}1\) | `OPEN` | Template from Thm 3.8; new proof required |
| Order+number with known \(\rho\): separation of absolute mass | Open as **new program** | OP-1.2 §5: Poisson means differ when \(M\) differs; not developed here (Fase 3 B1) |
| Witness-pair or rate no-go for a *named* quasi-local proxy \(Q\neq T_{\mathrm{EH}}\) | `OPEN` | Fase 3 **B2** (adversarial pairs)—preferred scientific sequel |
| Theorem-specific priority audit for Thm 3.9, including random geometric graphs / latent-space minimax inference | `OPEN` bibliographic residual | Existing external tiers audited the Thm 3.8 instantiation; no novelty claim is made for Thm 3.9 |
| Critical-scale constant, constant efficiency of \(S_n\), and a numerically certified \(dv_0\) | `OPEN` | Theorem 3.9 closes the exponent and fixed-pair consistency only; deterministic quantitative analysis required |

### 7.4 Explicitly not claimed open problems

We do not list “find the observable that reconstructs the \(3{+}1\) event horizon
from finite order-only data” as an open problem of this program. That question is
abandoned as north (§7.2), not deferred.

---

## §8 Conclusions

We asked what a finite unlabeled causal set can identify about Schwarzschild
geometry when the observation is order-only—often conditioned on cardinality—and
when continuum labels are used only to score, never to define, the estimator.

**Pillar P1.** Three non-identifiability statements and one companion separation
theorem are proved. Absolute horizon
radius (mass) is invisible at fixed \(n\) along dilation and co-scaling orbits
(Theorem 3.1). The global event horizon is not a functional of data from a finite
causally convex patch
(Theorem 3.2). On a regular one-parameter family of \(1{+}1\) causal diamonds with
finite Fisher information, no order-only procedure localizes the continuous
parameter below a two-point rate of order \(n^{-1/2}\) (Theorem 3.8). For the same
family at sufficiently small \(dv\), the comparable-pair count separates every
fixed distinct parameter pair, and succeeds for moving alternatives at
\(\omega(n^{-1/2})\) (Theorem 3.9). Thus the boundary exponent is matched in the
\(o/\omega\) sense, without a constant-optimality claim. The results are labeled
`PROVED_NON_IDENTIFIABILITY` and `PROVED_FIXED_N_SEPARATION`. They are not failures
of particular estimators, and they are not a slogan that causal sets cannot see
black holes.

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
recoverability of a carefully contracted geometric score and separate a continuous
shape parameter at the matching boundary exponent. Further scientific work,
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
