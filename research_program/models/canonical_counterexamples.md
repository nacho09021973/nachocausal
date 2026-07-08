# WP4 — Theoretical identifiability limits for finite causal sets

> **Working draft, REVISABLE, not frozen.** This is the README-defined WP4 ("WP4 — Contraejemplos
> y completaciones", `research_program/README.md` §7). It reuses the vocabulary of
> `research_program/taxonomy/identifiability_taxonomy.md`, the families of
> `research_program/models/wp3_model_families.md`, and the criteria interface of
> `research_program/work_packages/wp3b_identifiability_criteria.md` (WP3b), without duplicating
> WP3b's definitions.

## 1. Scope and status

WP4 is the theoretical identifiability-limit work package. Its question is prior to any estimator:

> Given only a finite order-only causal set `C_n`, what geometric targets are identifiable in
> principle, what targets are only statistically (ensemble-level) inferable, and what targets are
> intrinsically underdetermined — regardless of which order-only rule is used to try to recover
> them?

This is the causal-set analogue of asking what can in principle be measured before building a
measuring apparatus: it is a question about the information content of `C_n` itself, not about the
performance of any particular pipeline.

Explicitly:

- WP4 is theoretical infrastructure, at the same status level as WP3 and WP3b.
- WP4 asks what is identifiable **in principle** from finite causal order; it is not an empirical
  PR004-support document.
- WP4 does **not** evaluate PR004, or any PR004 run, output, or summary.
- WP4 does **not** use simulations. No numerical run backs any statement in this document.
- WP4 does **not** assume the sealed estimator (v2) is relevant to any criterion here, and does not
  reference its outputs (`prereg-002`, `prereg-003`) as evidence.
- WP4 **may conclude that some targets are not measurable from order-only data.** This document
  does not yet reach such a conclusion for any specific target — §5 defines candidate
  non-identifiability *templates*, not proven instances — but the identifiability principle in §3
  is stated precisely so that a future instantiation (§10) could establish such a conclusion, and
  §6 already states what that would mean for PR004 if it happened.

## 2. Central formal setup

- **Observed finite causal set `C_n`.** An unlabeled finite poset obtained by forgetting
  coordinates, labels, and embedding data (WP3 §2, order-only channel) unless a weaker forgetting
  is stated explicitly.
- **Model family `P_n(theta)`.** A parametrized family of laws over finite posets (WP3 §2):
  `P_n(theta) = Law(C_n | theta)` for `theta` in a parameter space `Theta`, where `theta` may
  encode a geometric completion (a latent spacetime patch, causal order, and sampling rule) or a
  non-geometric generative rule.
- **Geometric target `T(theta)`.** A functional of `theta` naming the specific quantity of
  interest — e.g. presence of a horizon-like structure, its location, a singularity-vs-boundary
  label, an effective dimension. A target must always be named explicitly; "geometry" alone is not
  a target (taxonomy §1.2).
- **Observation channel.** One of three, as fixed in WP3 §2 and WP3b §2, and never mixed within a
  single claim: **order-only**, **order + cardinality**, **order + external geometric input**.
- **Completion class `E_n(C_n)`.** The set of completions consistent with a specific observed
  order:

  `E_n(C_n) := { theta in Theta : C_n is a plausible realization under P_n(theta) }`

  ("plausible" is deliberately left as a single-instance placeholder — non-negligible probability,
  membership in a typical set, or an equivalent notion fixed by whoever instantiates a template;
  this document does not commit to one formalization). `E_n(C_n)` is the object that makes
  "multiple inequivalent completions may exist for the same finite observed order" precise: it is
  the set of all `theta` not excluded by having observed `C_n`.

## 3. Identifiability principle

Core criterion:

> A target `T` is identifiable from a given observation channel only if all observationally
> equivalent or near-equivalent completions agree on `T`.

Formally, using §2's objects: `T` is identifiable at instance `C_n` under a channel only if `T` is
constant over `E_n(C_n)` restricted to completions compatible with that channel — every
`theta in E_n(C_n)` gives the same value of `T(theta)`.

The corresponding non-identifiability witness:

> If there exist `theta` and `theta'` such that `P_n(theta)` and `P_n(theta')` are indistinguishable
> — or close under a stated distance — at finite `n`, but `T(theta) != T(theta')`, then no
> order-only estimator can reliably identify `T` at that `n`.

This is a statement about the pair of laws, not about any specific rule `T(C_obs)` (taxonomy §3.3):
if such a pair exists, **no** function of the observed order alone — regardless of how it is
constructed — can separate `theta` from `theta'`, because both are consistent with what was
observed. The statement must always carry a named `n` or asymptotic regime (WP3b §5): "close at
finite `n`" and "close asymptotically" are different claims and are not interchangeable.

This principle is a necessary condition, not a recipe: exhibiting a candidate pair informally (as
§5's templates do) motivates a non-identifiability question but does not establish it. Establishing
it requires the distance/regime to be made precise and argued (§7, §10).

## 4. Targets to classify

The following targets are distinguished. Each must be tied to a channel (§2) and a regime (WP3b
§5) before any identifiability statement about it is meaningful.

1. **Existence of a horizon-like structure.** A detection target: does `theta` contain a
   horizon-like structure `H_theta` at all (WP3 Family A) versus not (Family B)?
2. **Fine horizon localization.** Given existence, at what position or band, to scale `a_n`, is
   `H_theta` located? Materially stronger than (1): identifiability of (1) does not imply any rate
   for (2).
3. **Coarse horizon/non-horizon classification.** A coarser version of (1): a stable
   interior/exterior or near/far partition, without committing to a precise location. Kept
   separate from (2) because one may be identifiable while the other is not (§5.3).
4. **Singularity imprint.** Whether an observed order-level feature is attributable to (or
   requires) terminal/singularity-type future truncation, as distinct from a horizon-like
   structure per se (bibliography §2.6, Gap C).
5. **Boundary/truncation artifact.** Whether an observed feature is attributable to finite-box
   boundary or sampling-window effects unrelated to any horizon or singularity (WP3 Family B).
6. **Dimension or scale information.** Effective dimension or discreteness-scale quantities
   (e.g., of the Myrheim-Meyer type, bibliography §2.3). Included for contrast: this is the one
   target class in the bibliography matrix with real order-only support, but that support is
   ensemble-level (§5.4), not single-instance, and says nothing by itself about targets (1)-(5).
7. **PR004-style ladder/braiding/peel-off diagnostics — explicitly not a target.** A diagnostic's
   behavior (adherence, peel-off depth, braiding pattern, anchor loss) is a property of a
   *procedure* applied to `C_n` — a function of the data and a chosen algorithm — not a geometric
   functional `T(theta)` of the underlying completion. Such a diagnostic can be a **symptom**
   consistent with one or more of targets (1)-(6) failing or succeeding, but it is not itself a
   target, and no identifiability statement about targets (1)-(6) follows from the diagnostic's
   output alone. Treating a diagnostic pattern as if it were the target is exactly the confusion
   §5.5 describes.

## 5. Counterexample/completion templates

Each template below is a schematic description of a family of competing completions — not a
proven pair. Instantiating one requires the five ingredients of §10.

### 5.1 Horizon vs. non-horizon completion

An observed order `C_n` compatible with a completion `theta_H` containing a horizon-like structure
`H_theta` (Family A) may also be compatible with a completion `theta_B` with no horizon: a finite
box boundary, an acceleration-patch (Rindler-like) structure, or a different truncation rule
reproducing the same coarse order-level features (Family B, "confounding features").

Candidate sources of competition: a horizon-associated transition near `r_*` versus a box edge at
the same effective location; a horizon-like causal-depth pattern versus an accelerated-observer
structure with no trapping content; a horizon-associated future-cardinality drop versus a
sampling-window edge effect.

What would remain indeterminate: whether order-only data licenses "there is a horizon-like
structure" (target 1) as opposed to "there is *some* finite boundary of unspecified character"
(target 5) — the gap between targets 5 and 1/3 in §4.

### 5.2 Horizon vs. singularity-imprint completion

A feature attributed to a horizon-like structure may instead be induced by terminal structure — a
singularity-like region truncating futures — or by a generic causal-depth gradient from the
sampling geometry rather than near-horizon physics (bibliography §2.6, Gap C).

Candidate sources of competition: a completion `theta_H` where the signal is produced by proximity
to `H_theta`, versus a completion `theta_S` where the identical signal is produced by proximity to
a terminal/singularity-like boundary with no horizon in the causal sense.

Relevance to PR004-style diagnostics: a diagnostic measuring ladder adherence or peel-off with
depth cannot, by construction, distinguish "the ladder loses adherence approaching a horizon" from
"the ladder loses adherence approaching a terminal/singularity-like region producing the same
pattern without a horizon." This is a structural remark about what such a diagnostic can and
cannot settle by itself (§4, target 7); it is not an evaluation of any specific PR004 run, and no
PR004 data is used to make this point.

### 5.3 Shifted-horizon / fine-localization ambiguity

A coarse horizon-like class may be identifiable (target 3) — a rule may reliably tell "this patch
contains a horizon-like structure somewhere" against a matched Family B control — while the
precise location (target 2) is not identifiable at arbitrarily fine resolution from the same
order-only data.

Candidate sources of competition: completions `theta_0`, `theta_1` differing only by a
sub-discreteness or `O(ell)` shift of `H_theta`'s position, compensated elsewhere in the patch so
the induced finite-order laws remain close; completions where the coarse partition is stable but
the exact transition band varies across completions consistent with the same observed order.

This template keeps targets 2 and 3 explicitly separate: it is not evidence that either succeeds
or fails, only a description of how they could come apart.

### 5.4 Single-instance ambiguity despite ensemble separation

Two completions `theta`, `theta'` may induce ensemble laws `P_n(theta)`, `P_n(theta')` that are
well separated (e.g., total variation tending to 1 as `n -> infinity`), while a single realized
`C_n` does not carry enough information to discriminate `theta` from `theta'` reliably, because of
realization-specific variance: Poisson fluctuation of order `sqrt(V)` (bibliography §2.2),
finite-`n` boundary sensitivity, or seed-specific noise.

**Statement that must not be dropped: ensemble identifiability does not imply single-instance
recoverability.** A result showing `P_n(theta)` and `P_n(theta')` separated at the level of the
law says nothing, by itself, about whether the one `C_n` on the table can be correctly attributed
to `theta` or `theta'`. Conversely, a rule that appears to work on a handful of realized instances
is not thereby an ensemble statement.

### 5.5 Diagnostic instability without geometric obstruction

A diagnostic procedure applied to `C_n` may exhibit instability, peel-off, braiding-like collective
structure, or anchor loss for reasons that are properties of the diagnostic construction itself
(a greedy or beam-search selection rule, a scoring function, a finite search depth) rather than
evidence of a genuine geometric obstruction in the underlying completion.

This template is deliberately generic: it applies to any depth-indexed or rank-indexed diagnostic,
not to one implementation. A diagnostic-artifact explanation and a genuine-obstruction explanation
can produce superficially similar output, and telling them apart requires the machinery of
§§5.1–5.4, not the diagnostic's own output — this is the precise sense in which §4's target 7 is a
symptom, not a target.

The PR004 ladder-braiding diagnostic
(`dev/PR004_LADDER_BRAIDING_DIAGNOSTIC_PREREGISTRATION.md`) is one instance of the general
situation this template describes; its own preregistration already states (its §10) that it cannot
by itself prove a physical defect or order-only localization. This document does not read, use, or
draw on any PR004 output to make that observation.

### 5.6 Relation to WP3 families

| Template | Family A role | Family B role | Family C role |
|---|---|---|---|
| 5.1 horizon vs. non-horizon | supplies `theta_H` | supplies the competing non-horizon completion | an A/B pair close under a stated distance is the counterexample |
| 5.2 horizon vs. singularity imprint | supplies `theta_H` where the signal is horizon-driven | supplies a terminal/singularity-like completion (Family B subfamily) | a matched A/B pair with the same future-truncation signature |
| 5.3 fine-localization ambiguity | supplies the family of `H_theta` positions at sub-`ell` separations | not directly needed (both endpoints are Family A) | the near-identical-position pair with close induced laws |
| 5.4 single-instance ambiguity | either family may play `theta`; the class concerns the ensemble/single-instance gap, not A vs. B | | a Family C pair separated in law but unresolvable from one instance |
| 5.5 diagnostic instability | a diagnostic run on Family A data | a diagnostic run on Family B data producing a similar artifact is the key control | not primarily a Family C object; a statement about the diagnostic, cross-checked against A and B |

Descriptive only — no cell has been instantiated with a proved pair (§10).

## 6. Consequences for PR004

These are conditional governance rules, not a current verdict: this document does not yet
establish which antecedent holds for any target.

- **PR004 should continue only if WP4 leaves a theoretically identifiable target** (§4) compatible
  with what PR004's diagnostics actually probe. No target in §4 has been shown identifiable or
  non-identifiable by this document; §5's templates are candidates, not instances.
- **If WP4 shows order-only horizon identification (target 1) is impossible** — i.e., §5.1 or §5.2
  is instantiated per §10 into a genuine witness pair — **PR004 should be stopped or repurposed**,
  since the target its diagnostics are read as probing would be shown unreachable in that channel.
- **If only coarse classification (target 3) is identifiable**, while fine localization (target 2,
  §5.3) is shown not identifiable or remains an open witness candidate, **PR004 must not claim
  fine localization** from its ladder/peel-off output.
- **If only ensemble identifiability is plausible** (§5.4), while single-instance identifiability
  remains open or is refuted, **PR004 must not claim single-instance reconstruction** from any one
  seed's diagnostic run.
- **If a target requires order + cardinality or order + external geometric input** rather than
  order-only (§2), **PR004 must declare that it is not order-only** once it relies on that channel
  — e.g., if a diagnostic uses embedding-derived `r` to orient or select a ladder rather than only
  to score it after the fact, as its own protocol already flags.

None of these conditions has been triggered by this document. PR004 remains, under its own
preregistration, diagnostic-only exploration (§7 tier 6) — explicitly non-confirmatory — and this
document does not change that status either way.

## 7. Evidence hierarchy

Evidence for any identifiability or non-identifiability claim must be one of the following types,
graded from strongest to weakest. Weaker types can motivate a question but cannot establish a claim
that a stronger type would be needed to support.

1. **Theorem/proof.** A stated and proved result about the laws `P_n(theta)`.
2. **Lower bound.** A derived, checkable bound on achievable risk or rate for a stated target,
   channel, and regime.
3. **Indistinguishability construction.** An explicit pair or continuum (Family C, §5.6) with a
   computed or bounded statistical distance between `P_n(theta)` and `P_n(theta')`, instantiating
   the witness condition of §3 without necessarily yielding a general rate.
4. **Controlled simulation.** A simulation designed and preregistered specifically to probe a
   named criterion here, with stated families, channel, and regime, reported as its own artifact.
5. **Preregistered estimator test.** A frozen-protocol empirical result about a specific instrument
   (taxonomy §3.1), such as `prereg-002`/`prereg-003`-style tests — instrument-level evidence that
   does not by itself support a family-level or intrinsic claim (taxonomy §4.1).
6. **Diagnostic-only exploration.** Exploratory, non-preregistered runs, including PR004-style
   K-beam/braiding diagnostics.

**Diagnostic-only exploration (tier 6) cannot establish identifiability or non-identifiability.**
It can motivate a question or a future preregistration (tiers 3-4), but a claim in this document's
sense requires tier 1-3 evidence, or tier 4-5 evidence explicitly scoped to the instrument or
simulation in question.

## 8. Non-goals

This document does not assert, and no later document may cite it in support of:

- that a horizon is recoverable from order alone;
- that PR004 measures a real geometric obstruction;
- that `R^2` or fit quality of any kind is sufficient evidence for any claim here or built on it;
- that `d = 2` conclusions, existing or future, generalize automatically to higher dimension;
- any empirical conclusion. This document defines a principle (§3), targets (§4), and templates
  (§5); it contains no data, no simulation, and no estimator output.

## 9. Possible WP4 outcomes

A decision table of the outcomes this work package could eventually reach, once a template in §5
is instantiated per §10. None of these rows is asserted as current fact; the last row is the
current status of this document.

| Outcome | Established here? | Consequence for PR004 (§6) |
|---|---|---|
| Order-only horizon existence (target 1) impossible | No — template only (§5.1, §5.2) | Stop or repurpose PR004 |
| Fine localization (target 2) impossible, coarse classification (target 3) open/identifiable | No — template only (§5.3) | PR004 may report coarse signal only, must drop fine-localization claims |
| Single-instance (§4.2-type) impossible, ensemble open/identifiable | No — template only (§5.4) | PR004 may report ensemble-level patterns only, must not claim single-seed reconstruction |
| Identifiable only with an extra channel (cardinality or external geometry) | No — not addressed by a specific template yet | PR004 must declare it is not order-only if/when it relies on such input |
| **Unresolved; counterexample templates defined only** | **Yes — this is the current status** | PR004 may continue as diagnostic-only exploration (§7 tier 6), explicitly non-confirmatory, pending §10 |

## 10. Path from template to proof

Turning a template in §5 into an actual witness for §3's non-identifiability condition requires
later work to supply, explicitly:

1. A concrete pair (or continuum) `theta`, `theta'` instantiating one row of §5.6 — named parameter
   values within a stated family, not a schematic description.
2. A named target functional `T(theta)` from §4 such that `T(theta) != T(theta')`.
3. A distance or indistinguishability notion between `P_n(theta)` and `P_n(theta')` — total
   variation, Hellinger, KL, likelihood-ratio behavior, or contiguity — stated at a named finite
   `n` or asymptotic regime (WP3b §5).
4. A finite-`n` or asymptotic statement of how close (or far) `P_n(theta)` and `P_n(theta')` are
   under that distance.
5. Evidence at §7 tier 1-3 closing the gap. Tier 4-5 evidence can support a narrower, instrument- or
   simulation-scoped claim; tier 6 (diagnostic-only, PR004 included) does not close this gap by
   itself.

Until all five are supplied for a given template, it remains a template, and no claim of
non-identifiability follows from it.
