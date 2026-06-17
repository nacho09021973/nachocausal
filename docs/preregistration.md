# Pre-registration 001 — 1+1D Schwarzschild event-horizon recoverability

Status: FROZEN. A recoverability benchmark, not a reconstruction claim. No result is reported
here.

## Precise, falsifiable question (frozen)

In a causal set from genuine Poisson sprinkling with the natural volume measure (no radial
densification) in a 1+1D toy Schwarzschild domain with hidden parameters (M, density rho, t-r
box geometry), where the estimator receives ONLY the anonymised poset (C, <=) and |C| — no
coordinates, no M, no r, no labels:

Does the order-only observable
  O(i) = length of the maximal timelike chain starting at minimal element i
produce a bimodal separation between truncated-future and extended-future elements, such that
there exists at least one order-only boundary definition between the classes (candidates:
antimode threshold of O, membrane of inter-class links, or cluster edge) that is stable under
seed/rho/extent and that, after freeze, localises the hidden r=2M within a pre-committed
tolerance, while being ABSENT in box-matched controls without a horizon (flat Minkowski, same
box geometry)?

Falsifiable: either the bimodality + boundary appears, matches r=2M within tolerance, is
stable, and is absent in controls — or it does not.

## Pre-committed rules (frozen)

1. Boundary is order-only, from the bimodality of O. The candidate space is explored ONLY on
   dev; the stable definition is selected and frozen.
2. Stability gate: if NO order-only boundary definition is stable on dev under seed/rho/extent
   -> FAIL. Post-hoc tuning, and choosing the definition that best matches ground truth, are
   forbidden.
3. Scoring: boundary identified blind (poset only). The embedding is revealed only after freeze,
   solely to measure boundary elements' distance to hidden r=2M. Ground truth only scores.
4. Controls: flat Minkowski with IDENTICAL box geometry, to isolate horizon-truncation from
   domain-edge truncation.

## Success criteria (form frozen; thresholds set on dev per the anchoring rule)

ALL of:
(i)   Bimodality of O significant at >= [theta_sig] on the dev ensemble.
(ii)  Boundary localises hidden r=2M within Delta_r/M <= [theta_loc].
(iii) Boundary location varies < [theta_stab] under seed/rho/extent.
(iv)  Box-matched controls produce NO significant bimodal separation (false positives <= [theta_fp]).
(v)   Verifiable assertion that no coordinates/labels entered O or the boundary procedure.
Failure/inconclusive: any unmet, or separation appears systematically in controls.

## Threshold anchoring (frozen rule)

Thresholds anchored to principled bases, NOT reverse-engineered from the dev outcome:
- theta_loc = k * ell / (2M), ell = rho^(-1/2) (2D discreteness scale), k a small pre-justified
  integer (cannot localise finer than the discreteness scale).
- theta_sig: a standard bimodality test at a level fixed in advance (e.g. Hartigan dip p<0.01).
- theta_stab: a pre-justified multiple of ell.
- theta_fp: conventional (<= 5%), fixed in advance.
Dev (a) selects the stable boundary definition and (b) confirms the principled thresholds are
meetable in principle — it does NOT set thresholds to the dev result. Unmet principled
thresholds are informative (possibly infeasible at that N), not a licence to loosen.

## Frozen protocol

- Domain: 1+1D Schwarzschild, Eddington-Finkelstein coords (det g = -1 in 2D, so
  coordinate-uniform sprinkling = natural-volume Poisson; ASSERTED in code, not assumed).
- Genuine Poisson; no densification. Estimator input: anonymised (C, <=) + |C| only.
- Estimator output: trapped region + candidate boundary, or "inconclusive".
- Controls: box-matched flat Minkowski; truncated no-horizon domains.
- Dev and validation seeds disjoint, documented, never reused. Thresholds frozen in writing
  before any validation seed is generated/analysed. N and ensemble MEASURED on dev, not assumed.

## Forbidden claims

No event-horizon reconstruction, apparent-horizon, Raychaudhuri, Kerr, manifoldlikeness, or
thermodynamic claim. A 1+1D recoverability benchmark of a known-truth horizon.

## Independent falsification gate

Before any escalation of the verdict's strength, an independent pass (separate session/tool,
blind to the proposed verdict, tasked to break it) must try to falsify it and fail. The author
of a claim is never its sole verifier.

## [UNVERIFIED] / open

- Literature N figures from planning ("~400 sprinklings at n~10^3", "n=10^4-2e6") are
  [UNVERIFIED] — not read from the source's quantitative section. Not evidence; N is measured on dev.
