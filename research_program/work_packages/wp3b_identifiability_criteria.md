# WP3b — Identifiability criteria interface (WP3 model families -> WP4 counterexamples)

> **Working draft, REVISABLE, not frozen.** This document defines mathematical/specification
> infrastructure. It does not prove recoverability, does not evaluate the sealed estimator, does
> not use or reference any numerical run, and does not make an empirical claim. It builds directly
> on `research_program/models/wp3_model_families.md` (Families A/B/C) and reuses the vocabulary of
> `research_program/taxonomy/identifiability_taxonomy.md`.
>
> **Naming note.** This document is **WP3b**, not WP4. The README-defined WP4 remains "WP4 —
> Contraejemplos y completaciones" (`research_program/README.md` §7), with intended output
> `research_program/models/canonical_counterexamples.md`. WP3b is an interface work package: it
> sits between WP3 (the model families) and WP4 (the counterexamples/completions built on those
> families), fixing the criteria vocabulary WP4 should use rather than replacing WP4.

## 1. Scope and status

WP3b specifies **criteria** — precise conditions under which a statement of the form "`G(theta)` is
identifiable / not identifiable from `P_n(theta)` under channel `X`" would be well-posed and
checkable. It is infrastructure, not a result.

Explicitly:

- WP3b is mathematical/specification infrastructure, at the same status level as WP3.
- WP3b does **not** prove recoverability for any observable, family, or regime.
- WP3b does **not** evaluate, score, or reference the sealed estimator (v2) or any of its outputs,
  including `prereg-002` and `prereg-003`.
- WP3b does **not** use numerical runs, simulations, or diagnostic exploration outputs (including,
  but not limited to, the PR004 K-beam/braiding diagnostic) as grounds for any criterion defined
  here. Those remain instrument-level or diagnostic-level evidence under the taxonomy (§3.1, §3.3
  distinction) and cannot substitute for the criteria below.
- WP3b does not by itself decide whether any target in §3 is met by any model family. It only
  states what would have to be shown, against which law, and under which channel and loss.

This document is written so that WP4 (counterexamples/completions, README §7) and later work
packages (WP5 or beyond) can point to a specific criterion here, a specific family from WP3, and a
specific evidence type from §7 before making a claim.

## 2. Observation channels

Following WP3 §2, identifiability must always be stated **relative to one of three channels**.
The channel changes what "identifiable" can possibly mean, so criteria are never channel-free.

### 2.1 Order-only

The observation is the unlabeled finite poset `C_n` up to isomorphism, with `n` itself treated as
not carrying separate information (or explicitly marginalized). This is the strongest channel
restriction and the one relevant to the programme's central question (README §0).

Criterion form: a statement about `G(theta)` under this channel must be phrased purely in terms of
the laws `P_n(theta)` induced on isomorphism classes of finite posets, with no appeal to `n` as a
free covariate beyond what the order itself fixes.

### 2.2 Order + cardinality

The observation is the finite order together with `n` (or a regime in which `n` is informative,
e.g. as a proxy for volume). This channel is strictly weaker than order-only as a hardness claim
and strictly stronger as an information channel: anything shown non-identifiable under order +
cardinality is automatically non-identifiable order-only, but not conversely.

Criterion form: a statement here must make explicit whether `n` is fixed, random with a stated
law, or asymptotic, and whether `G(theta)` is being inferred jointly from order and `n` or from `n`
alone (in which case it is not really an order-identifiability statement at all and should be
labeled as such).

### 2.3 Order + external geometric input

The observation includes the order plus additional structure not derivable from the order alone:
a supplied horizon partition, a supplied antichain/surface, embedding coordinates, or similar
(WP3 §2, channel 3). Results here are benchmarks, not intrinsic order-only identifiability
results.

Criterion form: any criterion invoked under this channel must name the specific external input
used, and any claim built on it must carry an explicit label that it is not an order-only result
(taxonomy §7.2–7.4 claim-type discipline).

### 2.4 Cross-channel discipline

A criterion, bound, or claim must name exactly one of the three channels above. Statements that
silently mix channels (e.g., proving something order+cardinality and reporting it as order-only)
are not admissible under this WP's vocabulary.

## 3. Targets

Identifiability criteria are relative to a **target** — the specific thing being asked about a
latent observable `G(theta)`. WP3b distinguishes at least the following five targets. They are not
nested in a single ladder of difficulty; each requires its own criterion.

### 3.1 Coarse horizon classification

Target: decide, from the observation channel, a coarse label such as interior/exterior or
near/far relative to a horizon-like structure `H_theta`, with error controlled under a named loss.
This is a **detection/classification** task in the taxonomy sense (taxonomy §2.4), not a
localization task.

### 3.2 Fine horizon localization

Target: estimate a position, band, or neighborhood associated with `H_theta` to a stated scale
`a_n` (in units of the discreteness scale `ell` where applicable), with the scale itself part of
the claim. This is a **localization** task (taxonomy §2.2) and is a materially stronger target than
3.1: passing 3.1 does not imply any particular rate for 3.2.

### 3.3 Singularity imprint detection

Target: decide whether an observed order-level feature is attributable to (or requires) a
terminal/singularity-type future truncation, as opposed to a horizon-like structure per se
(bibliography §2.6, Gap C). This target exists precisely to keep "horizon signal" and
"singularity imprint" from being silently identified with each other (README §5, risk 3).

### 3.4 Boundary/truncation artifact detection

Target: decide whether an observed order-level feature is attributable to finite-box boundary
effects, sampling-window truncation, or density gradients unrelated to any horizon or singularity
(WP3 Family B, "confounding features"). This is the control-side counterpart of 3.3.

### 3.5 Lower-bound or non-identifiability statements

Target: exhibit that, under a named channel and a named class of rules or laws, two or more values
of `G(theta)` cannot be told apart with precision better than a stated scale, or at all, in a
stated asymptotic or finite-`n` regime. This target is qualitatively different from 3.1–3.4: it is
a statement about the law `P_n(theta)` (or a family of laws), not about any particular estimator
(taxonomy §3.3, §4.3).

Any later claim must name which of 3.1–3.5 it addresses. A result about 3.1 does not transfer to
3.2, and a positive result under any of 3.1–3.4 says nothing about 3.5 unless argued separately.

## 4. Single-instance vs ensemble identifiability

### 4.1 Ensemble identifiability

A target is **ensemble-identifiable** under a channel if the criterion is stated at the level of
the law `P_n(theta)` itself: separation, contiguity, or convergence statements that hold for the
distribution over realizations, for a sequence indexed by `n`, or as an expectation over the
sampling mechanism (bibliography §4.2, Gap B).

### 4.2 Single-instance identifiability

A target is **single-instance identifiable** under a channel if the criterion controls the
behavior of a rule (or of an optimal decision) on one observed finite causal set with a stated
finite-sample guarantee (e.g., a bound holding with specified probability, or an exact statement
for the realization at hand), not merely in expectation or in the `n -> infinity` limit.

### 4.3 The non-implication that must be stated every time

**Ensemble identifiability does not imply reliable recovery from one finite causal set.** A law
`P_n(theta)` can be asymptotically separated from `P_n(theta')` (ensemble sense) while any given
finite realization carries variance — Poisson fluctuation of order `sqrt(V)` (bibliography §2.2),
finite-`n` boundary sensitivity, or realization-specific noise — large enough that a single
instance does not permit the inference at the claimed precision. Conversely, single-instance
behavior observed on specific seeds is not by itself an ensemble statement and must not be
reported as one.

Every future document invoking WP3b must state which of 4.1 or 4.2 it is claiming, and if it moves
from one to the other, must argue the transfer explicitly rather than assume it.

## 5. Finite-n vs asymptotic identifiability

Three distinct regimes must be kept apart, matching taxonomy §6 (statistical identifiability
regimes) but indexed here to sample size / density rather than to a fixed asymptotic dichotomy
alone:

### 5.1 Finite-sample distinguishability

A statement at a fixed, named `n` (or fixed density/intensity): a bound or exact value for a
distance (TV, Hellinger, KL) or for the risk of the best possible rule under a stated channel and
loss, at that specific `n`. This is the regime relevant to any claim about one experiment run at
one intensity.

### 5.2 Asymptotic consistency

A statement about the limit `n -> infinity` (or density `-> infinity` at fixed patch, or patch size
`-> infinity` at fixed density, which must be distinguished from each other): existence of a
consistent test or estimator, or convergence of a localization scale `a_n -> 0`, in the taxonomy's
"separación total" sense (taxonomy §6.1).

### 5.3 Impossibility / lower-bound regimes

A statement that a target cannot be achieved better than a stated scale, either at every finite
`n` in a stated range, or in the limit, via contiguity (taxonomy §6.2–6.3) or an explicit two-point
/ Le Cam / Fano argument over a Family C construction (WP3 §5). A lower bound must specify whether
it is a finite-`n` bound or an asymptotic one; the two are not interchangeable, and a finite-`n`
impossibility result is generally the more informative and harder one to obtain.

A single document should not silently slide between 5.1, 5.2, and 5.3. In particular, an
asymptotic consistency result (5.2) says nothing by itself about finite-sample behavior (5.1), and
neither says anything about impossibility (5.3) unless a matching lower bound is separately
established.

## 6. Positive, null, and adversarial criteria

Each of the targets in §3 requires evidence stated against the relevant WP3 family, not against an
estimator. The three families play distinct evidentiary roles and a full identifiability claim
should reference more than one of them where applicable.

### 6.1 Family A (positive geometric horizon family) — recoverability-side criterion

A positive claim (e.g., that target 3.1 or 3.2 is achievable under a stated channel) must be
stated as a property of the laws `P_n^A(theta)`: existence of a decision rule, test, or estimator
whose risk under a named loss is controlled, uniformly over the relevant subset of `Theta_A`, at
the stated finite-`n` or asymptotic regime (§5). A positive result confined to Family A alone does
not license a claim about targets 3.3–3.5, and does not by itself rule out that the same order-
level signal is also produced by Family B (see 6.2).

### 6.2 Family B (null/control non-horizon family) — separation/confound criterion

A claim that an observable actually tracks a horizon-like structure (as opposed to a boundary,
truncation, or non-geometric confound) requires showing separation between `P_n^A(theta)` and the
relevant `P_n^B(phi)` control class, not just a positive signal computed on Family A in isolation
(WP3 §4, bibliography §2.6 Gap C). This is the criterion that operationalizes targets 3.3 and 3.4:
a claim of "horizon detection" that has not been checked against the matched Family B control is
not a horizon-detection claim under this WP's vocabulary — it is at most a Family-A-internal
signal.

A negative or partial result here must specify whether indistinguishability holds against all of
Family B or only a named subfamily (WP3 §4, "Role in identifiability").

### 6.3 Family C (adversarial / near-non-identifiable family) — lower-bound criterion

A non-identifiability or lower-bound claim (target 3.5) must be stated against a Family C
construction: a two-point pair `theta_0, theta_1` (or a continuum `theta_t`) with
`G(theta_0) != G(theta_1)` but with `P_n^C(theta_0)` and `P_n^C(theta_1)` close under a named
statistical distance, at a named finite `n` or asymptotic regime (WP3 §5). The criterion is not
satisfied by exhibiting that one estimator fails on a Family C instance; it requires a bound on the
statistical distance between the two laws themselves (taxonomy §4.3, §7.4).

### 6.4 Cross-family requirement

A claim that a target in §3 is resolved for a given channel and regime should, where the target
type makes it meaningful, address all three families: a positive rule (6.1) that is also separated
from the relevant null control (6.2), stress-tested against the closest available adversarial
construction (6.3). A criterion satisfied against Family A alone, without 6.2 or 6.3 as
applicable, should be labeled as partial.

## 7. Acceptable evidence types

Evidence for any claim invoking a WP3b criterion must be one of the following types, graded here
from strongest to weakest. Weaker types can motivate a question but cannot alone close a claim
that a stronger type would be needed to support.

1. **Theorem/proof.** A stated and proved mathematical result about the laws `P_n(theta)`
   (existence of a test, a bound, a rate, a contiguity relation, an impossibility result).
2. **Bound.** A derived, checkable inequality (finite-sample or asymptotic) on a risk, a
   statistical distance, or a rate, even without a full theorem-style writeup, provided the
   assumptions and regime are stated.
3. **Controlled simulation.** A simulation designed and preregistered specifically to probe a
   named criterion in this document, with stated families, channel, loss, and regime, run and
   reported as its own artifact with explicit scope — not reused diagnostic output.
4. **Preregistered estimator test.** A frozen-protocol empirical result about a specific
   instrument (in the sense of taxonomy §3.1), such as `prereg-002`/`prereg-003`-style tests. This
   is instrument-level evidence and, per taxonomy §4.1, does not by itself support a family-level
   or intrinsic-level claim under §3.5 or §6.3.
5. **Diagnostic-only exploration.** Exploratory, non-preregistered runs (including, explicitly,
   PR004-style K-beam/braiding diagnostics). These may motivate a question or a future
   preregistration but are not evidence for or against any criterion in this document, and must
   not be cited as if they were.

A claim invoking this document must state which evidence type it relies on. A criterion in §3 or
§6 that currently has no evidence of type 1–3 attached should be reported as open, not as
resolved by type 4 or 5 evidence.

## 8. Non-goals

This document does not assert, and no later document may cite it in support of:

- that the horizon is reconstructible from order alone;
- that any existing estimator (sealed or otherwise) is optimal;
- that `R^2` or fit quality of any kind is sufficient evidence for an identifiability or
  non-identifiability claim;
- that `d = 2` results, existing or future, generalize to higher dimension.

These mirror WP3 §7 and taxonomy §8 and are restated here because WP3b's criteria are exactly the
kind of document that a later claim might otherwise misuse as license for one of the above.

## 9. Open questions

WP3b leaves the following open for later work packages, including WP4 (counterexamples/completions):

1. Which specific loss functions and metrics (TV vs Hellinger vs KL vs a task-specific loss)
   should be fixed as the default for each target in §3, and does the choice change which
   criterion in §6 is tractable first?
2. Is there a concrete, specified Family C construction (WP3 §5) for which a finite-`n` bound
   (§5.1) is currently within reach, as opposed to only an asymptotic contiguity argument (§5.2)?
3. Which subfamily of Family B is the relevant control for the current repo's near-horizon
   signal — box-boundary confounds, singularity-truncation confounds, or both jointly (§6.2,
   bibliography Gap C/D)?
4. Can any ensemble-identifiability result (§4.1) be strengthened to a single-instance guarantee
   (§4.2) for a stated target, or is there a structural reason (e.g., `sqrt(V)` fluctuation) that
   blocks this in general?
5. Does the coarse/fine distinction (targets 3.1 vs 3.2) correspond to a genuine gap in achievable
   rate, or could a single criterion cover both under a suitably chosen loss?
6. What is the minimal external-geometric-input channel (§2.3) needed to make target 3.3
   (singularity imprint detection) tractable, and can that requirement be reduced toward
   order + cardinality (§2.2)?
7. How should this criteria document be revised once WP3's Family A/B/C definitions are
   specialized (rather than left as design patterns), so that criteria here remain applicable
   without silent redefinition?
