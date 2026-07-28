# Post-PR008 observable candidate matrix

STATUS: DESIGN_TRIAGE_ONLY
DATE: 2026-07-11
AUTHORIZATION: CHEAP_KILL_TESTS_ONLY_AFTER_PREREGISTRATION
REVISION: §6 step 5 amended 2026-07-17 per `docs/comite/comite_decision_036_
pr009-pr010-sequencing-adjudication.md` — see that decision for the full rationale and the
binding caveats on this amendment (it authorizes no candidate opening by itself).
REVISION: §8 added 2026-07-28 per `docs/comite/comite_decision_046_weyl-level-sheet-page-shoom-adjudication.md`
(commit `a0a0f9d`) — records an adjacent, non-matrix candidate adjudicated BLOCKED, and the
cross-cutting structural obstruction it identified. It closes no candidate in §2 and authorizes
nothing.

## 1. Selection rule

A candidate advances only if it introduces information absent from `H_hat`, has a direct
physical interpretation, can be computed on an abstract finite poset, and admits a cheap
test that can kill it before optimization.

Scores use `0` (poor), `1` (weak), `2` (moderate), or `3` (strong). They are design
judgements from the literature review, not experimental results.

## 2. Comparative matrix

| Candidate | New information beyond depth | Physical link | Order-only feasibility | 3+1D path | Leakage risk (3=low) | Cheap falsifiability | Total / 18 | Rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A. Ladder-ensemble effective expansion | 3 | 3 | 2 | 2 | 2 | 3 | 15 | 1 |
| B. Intrinsic-cut BDG/SMI contrast | 3 | 3 | 1 | 3 | 1 | 2 | 13 | 2 |
| C. Intrinsic-cut molecule density | 2 | 2 | 1 | 3 | 1 | 3 | 12 | 3 |
| D. Retuned single-path or first-empty depth | 0 | 1 | 3 | 1 | 2 | 3 | 10 | reject |

The ranking does not authorize combining candidates. Each must first face its own frozen
kill test.

## 3. Candidate A: ladder-ensemble effective expansion

### Hypothesis

For an order-only ensemble of admissible ladder continuations, the change in effective
transverse endpoint population across rung depth acts as a discrete expansion proxy.

For depth `k`, let `p_k(e)` be the normalized multiplicity of distinct admissible endpoints
or endpoint pairs. Candidate summaries include:

```text
N_eff(k) = exp(-sum_e p_k(e) log p_k(e))
theta_eff(k) = log N_eff(k+1) - log N_eff(k)
```

This is a hypothesis template, not a frozen definition. It uses distributional information
that `H_hat` discarded. Raw survivor count alone is not sufficient because beam width and
duplicate multiplicity can be algorithmic artifacts.

### Order-only construction requirements

- Seeds are selected by a frozen local order predicate.
- Rungs and continuations use links, intervals, and cardinalities only.
- No radial or embedding-based outward direction is supplied.
- If orientation is necessary, both order-theoretic orientations are evaluated under a
  frozen symmetric rule.
- The flat/control subtraction is derived from independent simulations or analytic nulls,
  never from evaluation horizon labels.

### Cheapest kill test

Use a tiny preregistered grid with three independent controls:

1. homogeneous 1+1D Minkowski patches: baseline-subtracted median `theta_eff` must be
   compatible with zero;
2. hidden-label Schwarzschild 1+1D patches: an order-only score fixed before unblinding
   must show the expected sign ordering across coarse interior/exterior evaluation groups;
3. depth-matched permutation: the score must outperform a baseline conditioned on the
   same depth and survivor budget.

Kill the candidate if it is determined by first-empty depth, total survivors, boundary
distance, or beam cap; if its sign changes under equivalent endpoint encodings; or if the
Minkowski control has a comparable transition.

### Main risks

- Combinatorial explosion and cap dependence.
- Hidden orientation through seed or rung selection.
- Endpoint entropy measuring optimizer diversity rather than geometric expansion.
- 1+1D transverse structure may not generalize to 3+1D screen area.

## 4. Candidate B: intrinsic-cut BDG/SMI contrast

### Hypothesis

Non-additivity of a dimension-appropriate causal-set action across an intrinsically selected
order cut contains a boundary signal that distinguishes horizon-like partitions from generic
partitions.

For a candidate partition `C = X union Y`, the literature motivates a contrast of the form:

```text
I_order(X:Y) = S_order(X) + S_order(Y) - S_order(C)
```

where `S_order` is assembled from cardinality and inclusive-interval abundances. Exact
coefficients and cut construction must be frozen in a separate preregistration.

### Order-only construction requirements

- Candidate cuts arise from antichains, rank-free layers, or other intrinsic poset rules.
- The horizon is never used to choose or orient a cut.
- The dimension choice is estimated independently or fixed by the simulation contract.
- Cut complexity and region cardinalities are matched across controls.

### Cheapest kill test

Compare the score on matched Rindler-horizon and non-horizon null-cut simulations without
telling the estimator which is which. This directly implements the negative control that
Machet and Wang identify as necessary. Also compare against cut-size, interval-count, and
boundary-cardinality baselines.

Kill the candidate if generic cuts produce the same localization, if the score is a monotone
function of region size, or if selecting the cut requires embedding assistance.

### Main risks

- The intrinsic-partition problem may be as hard as horizon localization itself.
- BDG action estimators are noisy and dimension-dependent.
- A codimension-two joint signal need not be horizon-specific.
- Computational cost may be high in 3+1D.

## 5. Candidate C: intrinsic-cut molecule density

### Hypothesis

Molecule-like link configurations around an intrinsically generated cut have a distinctive
density or asymmetry near a trapped boundary.

### Order-only construction requirements

- The cut is generated without horizon labels.
- Molecule predicates use order relations and cardinality only.
- Straddling and geometric distance appear only in blinded evaluation.

### Cheapest kill test

Scan matched intrinsic cuts in Schwarzschild, Rindler, and flat finite boxes. Require the
candidate to outperform cut area/cardinality and ordinary link-density baselines while
remaining stable across spacelike-like and null-like order-cut families.

Kill the candidate if its peak follows the box boundary, cut cardinality, or a generic null
joint rather than the hidden horizon.

### Main risks

- Published molecule definitions condition on a known horizon.
- Null cuts can introduce non-local contamination.
- The statistic may estimate area conditional on a cut but provide no localization.

## 6. Recommended sequence

1. Draft a preregistration for Candidate A only.
2. Implement an abstract-poset input boundary before any Schwarzschild evaluation.
3. Freeze matched depth, survivor-budget, and Minkowski baselines.
4. Run the cheap kill test once.
5. Open Candidate B only if A is killed, survives with a clearly non-depth channel, or A's
   implementation track — across all attempted designs to date (PR009, PR010) — is formally
   closed at a contract/design-feasibility precedence tier that pre-empts the scientific
   killed/survived axis (per the precedence convention of
   `docs/plan_operativo_15_julio_2026.md:87-88,573-579`: `FAILED_DATA_CONTRACT`/
   `LEAKAGE_DETECTED`/`RESOURCE_ABORT`/`ABSTAIN` precede any scientific terminal). This third
   branch carries no scientific killed/survived claim, conveys no information about the
   observable's channel content, and does not authorize retuning or reopening A's closed
   designs (per §7 below). Opening B under this third branch additionally requires an explicit,
   dedicated feasibility showing — comparable in rigor to PR010's own coverage study — that B's
   reference-coverage / matched-cut population demands can be met under a budget comparable to
   the one that defeated A; absent that showing, B remains closed alongside A. (Amendment
   adopted per `docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md`; PR009
   closed `FAILED_DATA_CONTRACT`, PR010 closed `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE` —
   neither is a scientific result about Candidate A's observable.)
6. Keep Candidate C as a validation bridge to 3+1D, not as the default locator.

## 7. Stop rules

- No hyperparameter sweep before a candidate passes its cheap kill test.
- No use of `R^2` as a primary metric without a physically signed target.
- No post-hoc change of seed, cut, orientation, beam cap, depth, entropy, or baseline rule.
- No promotion from 1+1D to 3+1D without a written translation of the cross-sectional
  quantity.
- A negative result closes the candidate; it does not authorize retuning the same channel.

## 8. Adjacent line adjudicated and closed — Page–Shoom Weyl level-sheet (2026-07-28)

Recorded so a future session does not re-propose this construction under another name. **This
section closes no candidate of §2 and authorizes nothing.**

### 8.1 What was adjudicated

A four-step pipeline proposed as a causal-set discretization of the Page–Shoom horizon detector:
(1) build an intrinsic `order+number` Weyl-sensitive profile `K̂(x)`; (2) form approximately radial
level bands from it; (3) read their causal character via intra-band comparability; (4) approximate
the sign/zero of `||dK||² = (1-2M/r)(K'(r))²`, which vanishes at `r=2M`.

**Terminal:** `BLOCKED_NO_INTRINSIC_WEYL_SENSITIVE_LEVEL_SET_GENERATOR`
(`COMMITTEE_DECISION_VERDICT=RECOMMEND_DO_NOT_PROCEED`).

**Decisive reason (Gate A):** the only `ESTABLISHED` order-only curvature channel (Benincasa–Dowker)
recovers the **Ricci scalar `R`**, not Weyl or Kretschmann (BD 2010 eq. 12); `R≡0` in 3+1D
Schwarzschild vacuum, so that channel does not distinguish radii there; and the extension to
Weyl²-order is **explicitly declared unfinished future work** in the primary literature
(`arXiv:2007.13192` §4). Status `NOT_AVAILABLE`, **not** `IMPOSSIBLE`.

**Gate B was NOT refuted:** it is recorded `UNRESOLVED_FINITE_BAND_IDENTIFIABILITY`. The continuum
discriminant survives probabilistically (an exact interior `r=const` leaf is spacelike ⇒ `p_comp=0`
identically; the exterior leaf is timelike ⇒ `p_comp>0`). What is open is finite-resolution: with
finite band thickness `δ` comparable pairs appear inside too, while the exterior fraction tends
continuously to zero as `r→2M`. Deciding it requires deriving `p_band(r; δ, patch, ρ)`.

**Binding scope (do not collapse this in any future citation):** decision 046 does **not** show that
the Page–Shoom detector is indiscretizable. It shows that this repository, and the established
causal-set literature to date, lack the ingredient (an intrinsic Weyl-sensitive level-set generator)
needed to discretize it intrinsically.

### 8.2 The cross-cutting finding that bears on §2

The load-bearing result is not the terminal but the obstruction it exposed: **Page–Shoom does not
fail for curvature reasons, it fails for foliation reasons.** Its causally-native step is (3) —
comparability is exactly what the order reads for free. What does not exist is the **canonical
intrinsic foliation/partition** that steps (1)–(2) must supply. That is the *same* object that C4
(neighbour graph, `comite_decision_039`), C5 (lateral peel, `comite_decision_042`) and C6 (waist
screen + transport, `comite_decision_043`/`044`) each failed to construct by different routes.

**Consequence for candidates B and C, stated with care.** Both are specified as *intrinsic-cut*
observables — "candidate cuts arise from antichains, rank-free layers, or other intrinsic poset
rules" (§4), "the cut is generated without horizon labels" (§5). They therefore **depend on the same
unbuilt object**, and each must now discharge the intrinsic-cut construction explicitly as part of
its own kill test rather than assuming it. This **raises the bar** on B and C; it does **not** close
them, and no adjudication of B or C is performed here.

**What decision 046 explicitly does NOT imply for B and C:** the `R≡0` argument is a **3+1D vacuum**
fact and does **not** transfer to this project's 1+1D sector, where the induced metric is not
Ricci-flat (`R = -2τ/r³ ≠ 0`, machine-checked at
`research_program/work_packages/wp4_fisher_localization_floor_symbolic_checks.py:71`). Any future
argument that "046 kills the BDG line" is therefore invalid as stated and must be re-derived in the
correct dimension. Symmetrically, the absence of a 3+1D sprinkler in this repo is a practical
blocker, and the vacuity of Weyl in `d≤3` is a dimensional one — neither is a physical reason to
close a construction.

### 8.3 Sole reopening trigger

An order-only observable sensitive to Weyl² (or a higher curvature invariant) with a **proven,
non-degenerate continuum limit**, appearing in peer-reviewed causal-set literature. This is an
external condition, not a work item. Absent it, this construction is not to be revisited under a new
name.
