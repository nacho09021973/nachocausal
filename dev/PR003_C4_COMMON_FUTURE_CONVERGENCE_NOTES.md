# PR003 C4 Common-Future Convergence Notes

STATUS: CANDIDATE_4_CONCEPT_ONLY / NO_SEEDS
DATE: 2026-07-20

This is a conceptual note for a fourth candidate localizer:

```text
persistent conditioned common-future convergence localizer
```

It is not a pre-registration, not an implementation, not a frozen contract, and not an
experimental authorization. No seeds, synthetic generators, real generators, tests, evidence
artifacts, or terminal runs are authorized by this note.

## 1. Repository anchors and scope

The route follows the repository's existing development-note convention for reversible conceptual
localizer work: `docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md:45-48`
explicitly points C1/C2 probes to a `dev/*_NOTES.md` companion and names
`dev/X0_Qn_wellposedness_NOTES.md` as the pattern. This file therefore stays in `dev/` and does not
touch `docs/preregistration_*`, evidence ledgers, manifests, terminals, `thresholds.py`, code, or
tests.

Read-only anchors used here:

- C2 trail: `dev/X0_Qn_wellposedness_NOTES.md:673-697` defines C2 as future-overlap collapse of a
  wavefront antichain, using `S(A)=cap_i J+(a_i)` and a not-yet-closed normalizer.
- C2 adjudication: `docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md:66-84`
  and `:180-194` record that the raw common-future functional is computable, but the old
  `E_indep` normalizer was the wrong object and truncation stability is mandatory.
- Third localizer contract: `docs/preregistration_square_box_truncated_futures_localization_draft.md:132-140`
  fixes that selection sees only the finite partial order and coordinates/`R_S` are scoring-only;
  `:157-180` defines `Min(C)`, strict `J+(i)`, and the past-matrix convention; `:181-220`
  defines future length `L(i)` and future volume `V(i)`; `:345-378` records `d_edge` as a
  post-selection diagnostic and explicitly leaves detailed future structure and pairwise overlap
  `J+(i) cap J+(j)` unexplored.
- Third localizer dev result: `evidence/square_box_truncated_futures_localization_20260719/dev_support_summary.json:19-31`
  records command, HEAD, no evaluation-seed consumption, valid primary BH support, and the primary
  descriptive medians; `:110-114` records `n_pair=16`, `INSUFFICIENT_VALID_PAIRS`, and terminal
  `INCONCLUSIVE_TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION`. The companion report repeats the
  non-confirmatory boundary at `dev_support_report.md:1-16`.
- Implementation anchors: `dev/run_truncated_futures_localization.py:161-183` implements
  `minimal_elements`, future-chain length in link units, and future volume under the same
  past-matrix convention; `nachocausal/generator.py:88-129` builds the past matrix; and
  `nachocausal/c1_selector.py:48-61` defines the cover relation.
- Height convention: `dev/X0_Qn_wellposedness_NOTES.md:759-764` defines past height `h(x)` as the
  number of elements in the longest chain ending at `x`, with occupied heights `1..H`.

There is no durable repository artifact for the read-only audit of the third dev run. Therefore
this note uses only facts visible in the run artifacts above and does not treat any unstored audit
statement as a load-bearing repository source.

## 2. Context from the third localizer

This is the fourth design in the localizer line. The third design, the truncated-futures
localizer, was implemented and executed cleanly as a development support run, but did not provide
support sufficient to advance to confirmatory evaluation:

```text
DEV_SUPPORT_RUN_COMPLETED
PRIMARY_LOCALIZATION_INCONCLUSIVE
SYNERGY_NOT_EVALUABLE_IN_DEV
NO_CONFIRMATORY_CLAIM
EVAL_NOT_AUTHORIZED
```

The run used exactly the development support band recorded in the summary artifact, not evaluation
seeds. It produced:

```text
valid_BH_trunc = 16
median_BH_loc_med = 15.62132964154105
median_BH_loc_q75 = 15.87624294734664
false_positive_MINK_fraction = 0.0
n_pair = 16
synergy_layer_terminal_descriptive = INSUFFICIENT_VALID_PAIRS
terminal = INCONCLUSIVE_TRUNCATED_FUTURES_BOUNDARY_LOCALIZATION
```

These are descriptive development facts only. They are not confirmatory evidence and are not a
negative result for common-future observables generally.

A read-only check of the primary-intensity CSV showed that, in the 16 BH realizations at the
primary intensity, `T`, `low-L`, and `low-V` produced identical readouts. The same check gave
descriptive

```text
median edge_rank_med for the trunc arm = 0.018779756656674307
```

rounded as `edge_rank_med = 0.0188`. This suggests edge domination in the development sample and
is one reason to ask whether the third localizer's three arms exploited essentially the same
marginal information. It is not a confirmatory inference.

The previous contract explicitly left the following structures unevaluated:

```text
J+(i) cap J+(j), detailed non-scalarized structure of J+(i), total degree,
shadow/interval structure, and future-branching statistics at fixed rank
```

This fourth candidate focuses only on pairwise common futures. It must not be presented as a
continuation or retune of `T`, `low-L`, or `low-V`.

## 3. Physical question

Falsifiable conceptual question:

> Can anomalous and persistent convergence of the common futures of neighboring minimal pairs
> carry localization information not determined by marginal future depths and future volumes, and
> can that information survive edge, top-truncation, density, and same-cloud Minkowski controls?

Current status separation:

- Conceptual exploration: this note only.
- Future support test: not authorized; would require a separate synthetic falsifier suite first.
- Confirmation: not designed and not authorized.

Motivation, stated cautiously:

> Two initially neighboring points whose causal futures converge unusually strongly and
> persistently could be a discrete signature of focusing. The proposal investigates whether this
> joint structure can localize the target region in a curved patch without reducing to future
> volume, causal depth, or edge proximity.

This wording is motivation, not interpretation. A common-future signal may measure a box edge, a
singularity funnel, a density variation, global geometry, or top truncation. A successful score
would not by itself demonstrate a horizon.

Candidate references supplied by the PI, checked only to the level supported by their primary
arXiv records:

- Eichhorn-Gamito-Stokes, arXiv:2605.06813, "Towards black-hole horizons and geodesic focusing in
  causal sets": the arXiv abstract states that the paper studies discrete horizon diagnostics,
  apparent horizons based on local geodesic properties, and a discrete expansion counterpart
  changing sign across the black-hole horizon. This supports focusing as a motivation only; it
  does not validate this common-future score.
- Boguna-Krioukov, arXiv:2401.17376, "Measuring spatial distances in causal sets via causal
  overlaps": the arXiv abstract states that causal overlaps are used to estimate spacelike
  distances in causal sets. This supports the broad plausibility that overlaps can encode
  spacelike relational information, but it is not the same formula as `|J+(i) cap J+(j)|` and does
  not validate this localizer.

Neither reference is load-bearing for the definition below.

## 4. Poset primitives

Let `C=(E,<)` be a finite strict partial order. The repository's matrix convention is:

```text
C[a,b] = true iff b precedes a
```

as documented in `docs/preregistration_square_box_truncated_futures_localization_draft.md:178-180`
and implemented in `nachocausal/generator.py:88-129`.

Minimals:

```text
M = Min(C) = {i in E : no j precedes i}
```

`Min(C)` is an antichain in a strict partial order; the third contract records this at
`docs/preregistration_square_box_truncated_futures_localization_draft.md:165-169`.

Strict future:

```text
J+(i) = {j in E : i precedes j}
```

`J+(i)` excludes `i` itself. In the matrix convention, this is column `i`: `{j : C[j,i]}`.

Covers/links, when needed for comparison to prior conventions:

```text
i <* j iff i < j and there is no k with i < k < j
```

This is the repository's cover relation in `nachocausal/c1_selector.py:48-61`.

Relabeling requirement:

Every score, valid edge set, selected band, and terminal must commute with arbitrary permutations
of element labels. A selection rule may use only order-derived sets and multisets; it may not use
raw labels as tie-breakers.

Coordinates:

Coordinates, `r`, `R_S`, `t`, and box-wall distances may be used only after selection for scoring
or diagnostics, matching the third contract's observation channel. If coordinates are used to
construct the neighbor graph, the candidate ceases to be order-only.

## 5. Past height

Use the existing repository convention from `dev/X0_Qn_wellposedness_NOTES.md:759-764`:

```text
h(x) = number of elements in the longest chain ending at x
```

Consequences:

- `h(x)` counts elements, not links.
- Every minimal has `h(i)=1`.
- For nonempty `C`, `H=max_{x in C} h(x)` and `H>=1`.
- For empty `C`, set `H=0` only as a totality convention and abstain immediately:
  `EMPTY_CAUSAL_SET_ABSTAIN`.

This differs from the third localizer's future length `L(i)`, which is counted in future-link
units with base `0` for a future-maximal element (`docs/preregistration_square_box_truncated_futures_localization_draft.md:181-220`;
`dev/run_truncated_futures_localization.py:167-183`). This candidate does not change either
convention.

## 6. Intrinsic prefixes and future subsets

The only proposed freezeable prefix fractions at this conceptual stage are:

```text
q in {1/2, 3/4}
```

Define:

```text
C_q = {x in C : h(x) <= floor(q H)}
F_i^q = J+(i) cap C_q,  for i in M
```

Because `J+(i)` is strict and minimals cannot be in the future of another minimal, every
`F_i^q` should be a subset of `C_q \ M`. This makes removing `M` from the universe coherent. A
future implementation must still check this rather than assume it.

Degeneracies and abstentions:

- If `C` is empty: `EMPTY_CAUSAL_SET_ABSTAIN`.
- If `H=0`: `HEIGHT_ZERO_ABSTAIN`.
- If `floor(H/2) < 1`, then `C_{1/2}` is empty under the existing height convention:
  `PREFIX_EMPTY_ABSTAIN`.
- If `floor(H/2) = floor(3H/4)`, the two prefixes are identical and do not provide two temporal
  scales: `PREFIX_SCALES_NOT_DISTINCT_ABSTAIN`.
- If either prefix has `|C_q \ M|=0`: `PREFIX_UNIVERSE_EMPTY_ABSTAIN`.
- If every `F_i^q` is empty at a required prefix: `FUTURES_EMPTY_ABSTAIN`.
- If a future subset contains an element outside the declared universe `C_q \ M`:
  `PREFIX_UNIVERSE_INCOMPATIBLE_ABSTAIN`.

These are abstentions, not scientific failures.

## 7. Conditioned overlap score

For a candidate pair `{i,j}` and prefix `q`, define:

```text
a_q = |F_i^q|
b_q = |F_j^q|
c_q = |F_i^q cap F_j^q|
n_q = |C_q \ M|
```

Proposed combinatorial normalization:

```text
mu_q = a_q b_q / n_q

sigma_q^2 =
  a_q b_q (n_q - a_q) (n_q - b_q)
  ---------------------------------
          n_q^2 (n_q - 1)

Z_ij(q) = (c_q - mu_q) / sigma_q
```

This is the hypergeometric fixed-marginal mean and variance for the overlap of two subsets of
sizes `a_q` and `b_q` drawn from a universe of size `n_q`. In this note `Z_ij(q)` is not a p-value,
is not interpreted as asymptotically normal, and is only a dimensionless combinatorial
standardization of observed overlap relative to fixed marginal sizes.

Algebraic validity conditions:

- `n_q > 1`.
- `0 <= a_q <= n_q` and `0 <= b_q <= n_q`.
- `0 <= c_q <= min(a_q,b_q)`.
- `F_i^q` and `F_j^q` are subsets of the same universe `C_q \ M`.
- `sigma_q^2 > 0`, equivalently no structural zero-variance case such as `a_q=0`, `b_q=0`,
  `a_q=n_q`, or `b_q=n_q`.
- `mu_q`, `sigma_q^2`, `sigma_q`, and `Z_ij(q)` are finite.

Mandatory abstentions:

```text
N_PREFIX_LEQ_ONE_ABSTAIN              if n_q <= 1
MARGINAL_SIZE_OUT_OF_UNIVERSE_ABSTAIN if a_q > n_q or b_q > n_q
OVERLAP_OUT_OF_RANGE_ABSTAIN          if c_q > min(a_q,b_q)
ZERO_VARIANCE_ABSTAIN                 if sigma_q^2 = 0
NONFINITE_SCORE_ABSTAIN               if any required quantity is non-finite
PREFIX_EMPTY_ABSTAIN                  if C_q is empty
FUTURE_EMPTY_ABSTAIN                  if required future subsets are empty
UNIVERSE_SUBSET_MISMATCH_ABSTAIN      if subsets and universe are incompatible
```

The formula must not be repaired by adding epsilons, continuity corrections, pseudocounts,
alternative denominators, or fitted weights after observing data.

## 8. Persistence score

For each valid candidate pair:

```text
S_ij = min( Z_ij(1/2), Z_ij(3/4) )
```

The minimum is binding. It is chosen to require that the common-future convergence:

- appears before the top of the causet;
- persists at both intrinsic prefixes;
- does not depend exclusively on final layers near the roof.

Do not replace `min` with a mean, maximum, sum, learned weight, or post-hoc threshold in this
concept.

If either prefix score is invalid, the pair is invalid. If no pair remains valid after all
abstention checks: `NO_VALID_PAIR_SCORE_ABSTAIN`.

## 9. Critical unresolved object: neighbor graph on minimals

The localizer requires:

```text
E_M subset {{i,j} : i,j in M, i != j}
```

This is the main conceptual precondition. A one-dimensional spatial section does not by itself
define an order-only adjacency relation among minimals. The induced order on `M` is empty because
`M` is an antichain; therefore adjacency cannot be read from relations between minimals alone.

Read-only repository search found no closed construction of a neighbor graph among minimals that
satisfies all of:

- input is only the finite order;
- invariant under relabeling;
- expected degree is fixed in a way appropriate to a 1D section;
- tie handling is closed;
- connectivity or controlled abstention is specified;
- degeneracies have typed terminals;
- computational cost is bounded;
- no coordinates, spatial order, or geometric labels enter selection.

Some repository material discusses "neighborhoods" or spacelike neighbors in other contexts
(`dev/PR003_Q_REFERENCE_RULE_DEVELOPMENT.md`, `dev/PR003_Q_A6_4_ROBUST_ABSTENTION_SPEC.md`,
R-VAR notes), but those do not provide an admissible `E_M` for minimals in this candidate. The
third localizer explicitly states that no such proxy has been identified or validated in
`docs/preregistration_square_box_truncated_futures_localization_draft.md:355-368`.

Therefore this note declares:

```text
NEIGHBOR_GRAPH_UNRESOLVED
```

This blocks preregistration, implementation, and any seed run. If a future version constructs
`E_M` from coordinates, the candidate must instead declare:

```text
NEIGHBOR_GRAPH_NOT_ORDER_ONLY
```

and must not be advertised as an order-only localizer.

## 10. Conditional selection rule

This section is conditional on a future admissible `E_M`; it is not currently executable.

Given valid `S_ij` values on valid edges:

```text
{i*,j*} = argmax_{{i,j} in E_M} S_ij
```

The candidate band would be:

```text
H_hat_common_future(C) = {i*,j*}
```

Closed tie and invalidity rules required before implementation:

- Non-finite `S_ij`: invalid edge; if all invalid, `NO_VALID_EDGE_SCORE_ABSTAIN`.
- No admissible edges: `NO_NEIGHBOR_EDGES_ABSTAIN`.
- Exact tie in maximal `S_ij`: abstain unless a future order-only, relabel-invariant tie key is
  proven. Raw element labels are forbidden.
- Several winning edges sharing an endpoint: same rule; no arbitrary endpoint preference.
- Several disjoint winning edges: same rule; no coordinate or label tie-break.
- If the future `E_M` construction itself returns degree above its declared one-dimensional limit
  because of ties or degeneracy: `NEIGHBOR_DEGREE_DEGENERATE_ABSTAIN`.

Under the current note, the selection rule is blocked by `NEIGHBOR_GRAPH_UNRESOLVED`.

## 11. Non-redundancy against marginal `L` and `V`

The joint overlap is not determined in general by the marginal future sizes. A finite construction
suffices.

Consider a universe `U={x,y,z,w}` and two pairs of minimals with strict futures:

```text
Pair A:
F_i = {x,y}
F_j = {x,y}

Pair B:
F_p = {x,y}
F_q = {z,w}
```

For both pairs:

```text
|F_first| = 2
|F_second| = 2
```

If future depth is also held fixed by making `x,y,z,w` maximal, then every minimal in the example
has future-chain length `L=1` in link units and future volume `V=2`. However:

```text
|F_i cap F_j| = 2
|F_p cap F_q| = 0
```

At a prefix where `U` is the universe, `n=4`, `a=b=2`, `mu=1`,
`sigma^2 = 2*2*(4-2)*(4-2)/(4^2*3) = 1/3`. Therefore the two standardized overlaps have
opposite signs:

```text
Z_A = (2 - 1) / sqrt(1/3)
Z_B = (0 - 1) / sqrt(1/3)
```

This proves that common-future overlap is not algebraically determined by the marginal pair
`(L(i),V(i))`, `(L(j),V(j))` in general. It does not prove the proposed localizer works on the
SQUARE_BOX_2P4 causets.

Future synthetic precondition before any real-generator seed:

- construct two pairs or two finite posets with the same relevant marginal `L` and `V` values;
- make their common futures differ;
- make their `S_ij` values differ;
- make the candidate's selected edge or terminal differ;
- verify exact relabel invariance.

No such synthetic suite is implemented here.

## 12. Synthetic falsifiers required before any generator seed

Before any real `BH` or `MINK` generator seed, a future design must define and pass a synthetic
falsifier battery with these conceptual contracts:

1. Marginal separation: same `L` and `V`, different common futures, different `S_ij`, different
   selection or terminal.
2. Relabeling: exact invariance of scores, valid edges, selection, and terminal under arbitrary
   label permutations.
3. Symmetric top truncation: if all futures are symmetrically truncated by the roof, the localizer
   must not create a false preferred region.
4. Symmetric neck: a geometric convergence not associated with the target region must trigger
   rejection, a control failure, or abstention, not a physical detection.
5. Density inhomogeneity: the score must not automatically select denser regions merely because
   they contain more elements.
6. Maximal peeling: recompute after removing one or more maximal layers by a fixed rule. If the
   winning edge changes materially or persistence disappears, terminal:

   ```text
   TRUNCATION_DOMINATED
   ```

7. Algebraic degeneracies: explicitly cover `sigma=0`, empty futures, coincident prefixes,
   insufficient height, exact ties, no admissible edges, and invalid universes.

Passing these would be necessary for support testing, not evidence of a physical claim.

## 13. Future controls required, not implemented

Mandatory controls before any support run:

- `MINK same-cloud`: asks whether the same point cloud with flat causality reproduces the signal.
  If yes, kill the candidate as a box/global-geometry artifact.
- `marginal-only`: preserves or uses only `a_q` and `b_q`, never `c_q`. It asks whether the score
  is doing anything beyond marginal future sizes. If it matches the candidate, kill for marginal
  redundancy.
- Random edge selection over the same admissible `E_M`: asks whether the selected band is better
  than choosing among the same graph without overlap information. If not, kill for no selection
  content.
- `d_edge` postselection diagnostic only: asks whether selected endpoints sit at future-truncating
  walls. If edge proximity explains the readout, kill or mark boundary-confounded; never use
  `d_edge` for selection.
- Maximal-layer peeling: asks whether the signal is roof-driven. If unstable, terminal
  `TRUNCATION_DOMINATED`.
- Density control: asks whether local density alone creates the score. If yes, kill as a density
  artifact.
- Historical comparison with the third localizer: only a reference readout. It is not an
  adjustable baseline and cannot authorize retuning.

## 14. Development and inference discipline

Two future development modes must remain separate.

Strictly descriptive development:

- may use fewer than 26 valid realizations;
- performs no between-seed inference;
- computes no significance terminal;
- checks computation, degeneracies, falsifier behavior, and artifact discipline only;
- does not authorize confirmation.

Development with between-seed inference:

- must guarantee in advance `n_valid >= 26`;
- must assign more than 26 seeds if abstentions are plausible;
- must not reuse seeds from the third localizer;
- must not choose alpha, multiplicity, effect floor, or inferential terminals at this conceptual
  stage.

No seed ranges are proposed here.

## 15. Conceptual death criteria

The candidate must not advance to preregistration if any of the following holds:

1. `NEIGHBOR_GRAPH_UNRESOLVED`.
2. `NEIGHBOR_GRAPH_NOT_ORDER_ONLY` while the intended claim remains order-only.
3. The score is determined by `L`, `V`, or other already-exploited marginal summaries.
4. No synthetic pair separates marginal summaries from common-future overlaps.
5. The score or selection is not relabel-invariant.
6. Selection materially depends on the roof.
7. MINK same-cloud reproduces the same signal.
8. Density inhomogeneity reproduces the signal.
9. Algebraic indefiniteness is structural rather than exceptional.
10. Computational cost exceeds the real pipeline budget.
11. Required controls need unavailable information.
12. The physical motivation requires stronger bibliographic support than the primary sources
    actually provide.

Killing this candidate would not refute focusing observables in general and would not refute all
localizers based on common futures.

## 16. Final state

The formulas and abstention structure are conceptually specified, and a finite non-redundancy
example shows that common-future overlap is not generally determined by marginal future volume and
future length. However, the required neighbor graph on minimals is not resolved in the repository
as an order-only, relabel-invariant construction.

Final typed state:

```text
CANDIDATE_4_CONCEPT_BLOCKED_NEIGHBOR_GRAPH / NO_SEEDS
```

No code, tests, contracts, manifests, ledgers, terminals, evidence artifacts, thresholds, seeds, or
data were authorized by this note.
