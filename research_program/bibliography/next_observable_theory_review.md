# Theoretical review for the post-PR008 observable

STATUS: WORKING_SYNTHESIS
DATE: 2026-07-11
SCOPE: LITERATURE_FIRST / NO_OBSERVABLE_AUTHORIZED

## 1. Question

After PR008 closed `H_hat` as `BASELINE_DOMINATED`, what order-only information channel
has a defensible physical connection to a black-hole boundary and is not merely another
encoding of algorithmic depth?

This review separates three questions:

1. What continuum quantity defines the physical target?
2. Which causal-set statistics respond to that quantity when the geometry is supplied?
3. Which of those statistics can be turned into an intrinsic finite-poset observable
   without embedding coordinates, horizon labels, radial distances, or a privileged cut?

The third question is the operative one. Success on the first two does not imply success
on the third.

## 2. Continuum target: expansion and trapping

The event horizon is global and teleological. Booth's review emphasizes that its existence
depends on the future structure of spacetime, while the quasi-local alternatives are built
around closed codimension-two surfaces and their null expansions. This makes an apparent,
trapping, or dynamical horizon a better design target for a local diagnostic than the event
horizon itself.

For future-directed outgoing and ingoing null normals, a marginally outer trapped surface
has vanishing outgoing expansion and negative ingoing expansion. A dynamical or trapping
horizon is foliated by such surfaces. Ashtekar and Krishnan use precisely the vanishing of
one future-directed null expansion as a defining condition.

The Raychaudhuri equation explains why this target is physical rather than merely
geometric labeling. The evolution of null-congruence expansion couples to shear and
Ricci focusing. A discrete proxy should therefore respond to the growth or contraction of
a family of null-like tracers, not only to the stopping depth of one optimized path.

Andersson, Mars and Simon add a crucial constraint: a marginally outer trapped surface
extends to a smooth horizon only under a stability condition. Consequently, a sign change
in one noisy slice is insufficient. A viable causal-set observable needs perturbation or
neighbourhood stability as part of its definition or validation.

### Design consequences

- The primary signal should be a signed change in a cross-sectional or branching quantity.
- A single-path depth is structurally too weak unless it is accompanied by transverse
  information.
- Stability under order-only perturbations is part of the target, not a post-hoc robustness
  campaign.
- Any cut, antichain, time orientation, or outward direction used by the estimator must be
  constructed from the poset or declared as external input.
- Foliation dependence is a scientific risk that must be measured explicitly.

## 3. Ladder molecules: closest intrinsic bridge

Bhattacharya, Mathur and Surya define ladder molecules as discrete analogues of null
geodesics in 2D causal sets. The construction is relational: linked pairs form rungs and
successive order constraints build a null-like ribbon. Eichhorn, Gamito and Stokes extend
the idea with fuzzy ladders and define a discrete expansion whose sign changes across a
1+1D toy black-hole horizon.

This is the strongest direct bridge between the continuum target and order structure:

- it represents a family or ribbon rather than only one longest chain;
- it admits a notion of transverse separation or opening;
- it has a published connection to expansion sign;
- it can, in principle, be expressed through links and intervals.

But the published proof of principle does not yet solve this repository's problem. The
existing implementation and examples use embedding information to orient, select, or
benchmark ladders. The exterior-sign behaviour is not uniformly successful, and long
ladders suffer combinatorial branching and peel-off. Therefore the literature licenses a
candidate family, not an intrinsic horizon locator.

### Required translation

Replace a geometrically selected ladder by an automorphism-invariant ensemble of locally
admissible ladder continuations. Measure how the effective endpoint population changes
with rung depth, after subtracting a matched flat/causally homogeneous baseline. The
transverse population, entropy, or effective number of endpoints carries information that
`H_hat` discarded when it collapsed a beam to first-empty depth.

## 4. Horizon molecules: strong benchmark, weak locator

Dou and Sorkin proposed counting links that cross a known horizon near a hypersurface.
Barton et al. produced a dimensionally viable molecule definition whose expectation
scales with horizon area for a supplied spacelike hypersurface and horizon. Homšak and
Veroni provide numerical Schwarzschild evidence in 3+1D: molecule counts follow the
area-law picture and concentrate near the horizon at the discreteness scale.

This is highly relevant evidence that local order relations near a horizon carry physical
information in 3+1D. It is not, however, an intrinsic detector. The definition partitions
elements using the horizon and a hypersurface that are already known in the continuum.
Using those labels during candidate selection would be ground-truth leakage.

Machet and Wang sharpen the warning. For null hypersurfaces, the molecule count can
receive non-local contributions away from the horizon-cut intersection and fail to remain
an area-local quantity. Thus even a physically motivated count can be contaminated by
the geometry of the chosen cut.

### Programmatic use

- Use horizon molecules as a geometry-aware validation target only.
- Never use horizon membership or straddling to define an order-only estimator.
- Ask whether a candidate order-only cut makes molecule-like counts peak near the hidden
  horizon, but keep that comparison outside terminal estimator logic.
- Treat null-cut dependence as a mandatory negative control.

## 5. Spacetime mutual information: promising boundary channel, partition problem

Machet and Wang define spacetime mutual information from the non-additivity of the
Benincasa-Dowker causal-set action across a partition. In a causal diamond truncated by a
Rindler horizon, the continuum result localizes to the codimension-two intersection and
scales with its area.

This suggests a richer channel than raw molecule counts: inclusive-interval abundances
and action non-additivity can detect a boundary contribution. It is attractive for 3+1D
because the BDG action is dimension-aware and built from order and number.

The unresolved issue is decisive. The calculation starts from regions separated by a
known causal horizon. It does not provide an intrinsic rule for choosing the partition.
The authors explicitly identify testing non-horizon null hypersurfaces as necessary to
determine whether the localization is horizon-specific or generic to the construction.

### Programmatic use

An order-only SMI scanner is a legitimate second-line candidate only if the candidate
partitions are generated without geometry and evaluated against matched non-horizon cuts.
Otherwise it is an area estimator conditional on the answer, not a horizon detector.

## 6. Information-channel audit

| Literature family | Order data used | Extra input in published result | Physical sensitivity | Intrinsic locator status |
|---|---|---|---|---|
| Single optimized chain / `H_hat` | comparability, depth, beam survival | start rule and fixed algorithm | singularity-truncated future/depth | closed as baseline-dominated |
| Rigid/fuzzy ladders | links, intervals, successive rungs | practical orientation/selection; embedding benchmark | null-like propagation and expansion sign | closest candidate, not yet intrinsic |
| Horizon molecules | crossing links/bi-atoms and cardinality | known horizon and hypersurface | area and near-horizon concentration | benchmark only |
| Spacetime mutual information | inclusive intervals, BDG action, partition | known horizon-induced partition | codimension-two boundary area | candidate only after intrinsic partition rule |
| Local interval/branching entropy | endpoint or continuation distribution | none in proposed form | transverse opening/focusing, unproven | new hypothesis requiring cheap falsification |

## 7. Non-negotiable leakage rules

The next observable must not consume:

- embedding coordinates or radial distance;
- horizon side, straddling, shell, or trapped labels;
- a cut selected because it is geometrically close to the horizon;
- an outward direction selected from continuum coordinates;
- a scale tuned after inspecting hidden-horizon performance;
- PR008 evaluation outcomes as training targets.

Geometry may enter only in a separate evaluation layer. The estimator layer must accept
a projected order-only record and must be executable on an abstract finite poset.

## 8. What the literature does and does not establish

### Established enough to guide design

- Null expansion and marginal trapping are physically appropriate quasi-local targets.
- Ladder-like structures can encode null propagation in 2D causal sets.
- A discrete ladder expansion can change sign across a 1+1D toy horizon.
- Horizon-molecule and SMI statistics contain area/boundary information when the relevant
  horizon or partition is supplied.
- Horizon-molecule numerics have reached Schwarzschild 3+1D and very large causal sets.

### Still open

- An automorphism-invariant ladder or beam-selection rule with no embedding assistance.
- A stable single-instance expansion estimator in finite causal sets.
- An intrinsic partition for SMI or molecule scans.
- Separation of horizon sensitivity from generic cut, boundary, density, and singularity
  effects.
- Transfer of a successful 1+1D order-only diagnostic to 3+1D.

## 9. Conclusion

The literature does not justify immediately implementing a complicated new estimator. It
does justify a narrow experimental sequence. The best first hypothesis is that transverse
branching of an order-only ladder ensemble contains expansion information that first-empty
depth erased. SMI-style action contrast is the strongest alternative channel, but its
partition problem makes it a second step. Horizon molecules should anchor validation, not
estimator construction.

## 10. Primary references

- Ashtekar & Krishnan, arXiv:gr-qc/0407042.
- Booth, arXiv:gr-qc/0508107.
- Andersson, Mars & Simon, arXiv:gr-qc/0506013.
- Kar & SenGupta, arXiv:gr-qc/0611123.
- Dou & Sorkin, arXiv:gr-qc/0302009.
- Barton et al., arXiv:1909.08620.
- Machet & Wang, arXiv:2012.06212.
- Bhattacharya, Mathur & Surya, arXiv:2301.06480.
- Dou, arXiv:2307.04150.
- Homšak & Veroni, arXiv:2404.11670.
- Eichhorn, Gamito & Stokes, arXiv:2605.06813.
