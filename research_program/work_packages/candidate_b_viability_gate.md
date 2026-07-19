# Candidate B viability gate — five-condition revision (ADOPTED, amended text)

STATUS: ADOPTED_AS_GATE_DEFINITION / SIGNED (PI: Nacho, 2026-07-19, "Autorizado a todas las
acciones que consideres" — see `docs/comite/comite_decision_037_...md` §11) / STILL NO
CANDIDATE-B OPENING
SCOPE: DOCUMENTARY_ONLY / NO_EXECUTION / NO_CANDIDATE_OPENING / NO_TERMINAL_EMITTED. Adoption of
this gate **as a precondition filter** is the only thing signed. Opening Candidate B, exercising
B1–B5 against a concrete `B`, any micro-pilot, and any reopening of Candidate A/PR009/PR010 or
the R-VAR shadows/`H_A` extension each remain separate committing steps requiring their own
dedicated committee decision plus PI authorization (decision 037 §9) — this sign-off does not
reach them.
DATE: 2026-07-19 (PI instruction: incorporate the two agreed reinforcements — operationalized
non-redundancy, and an identifiability-plausibility condition at reachable N)
RELATION_TO_DECISION_036: operationalizes, and does not amend, the "explicit, dedicated
feasibility showing" clause of `research_program/work_packages/next_observable_candidate_matrix.md`
§6 step 5 (amendment adopted per
`docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md`). Decision 036 and the
matrix text it adopted are untouched by this draft.
ADOPTION_PATH: per the decision-034/035/036 precedent, this gate binds only after its own
committee decision plus explicit PI sign-off. Until then it is a proposal.
PROVENANCE: reviewed by `docs/comite/comite_decision_037_candidate-b-viability-gate-review.md`
against repo HEAD `475cb93d501bafbf2506328a44df9733739fba24`; this text carries amendments A1–A6
from that decision's §9 next-step spec, applied 2026-07-19. Still UNSIGNED — decision 037's §9
requires a lightweight chair-level re-verification of this amended text (re-run the same
`grep`/anchor checks) before it is presented for PI sign-off; see ADOPTION_PATH above.

## 0. Purpose and non-authorization

This document drafts the revised viability gate that any **future** Candidate B (the matrix §4
intrinsic-cut BDG/SMI contrast, or a successor proposal occupying that slot) must pass before a
Candidate-B preregistration may even be drafted. It is the operational content of the
"feasibility showing" that matrix §6 step 5 already requires.

This draft authorizes nothing. In particular it does **not**:

- open Candidate B, define its observable, or draft its preregistration;
- reopen, retune, or reinterpret Candidate A (PR009/PR010) in any way;
- authorize a micro-pilot, an enumeration, a Monte Carlo run, a seed draw, or any execution;
- reactivate the pending, unauthorized shadows-`(S_z)`/boundary-`(H_A)` extension of R-VAR — that
  extension, not the closed `L(i)`/`future_card(i)` core (§2 B1), is what remains out of scope;
- emit any terminal, verdict, or scientific claim.

## 1. Preserved state (binding context, restated without modification)

- PR009 closed with terminal exactly `FAILED_DATA_CONTRACT`
  (`dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_CLOSURE_DECISION.md`). PR010 closed with
  terminal exactly `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`
  (`dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md`,
  `dev/PR010_REFERENCE_DEPTH_COVERAGE_DEVELOPMENT_PROTOCOL.md` §8). Both are contract/design
  closures, not scientific falsifications.
- Candidate A is untested and, under the current contract, untestable. It may not be cited later
  for or against its underlying hypothesis. No reopening or retuning of A is authorized by this
  draft or by passing this gate.
- A bench-specific negative (including any terminal from condition B5 below) must never be
  converted into a physical negative. This follows the precedence convention of
  `docs/plan_operativo_15_julio_2026.md:87-88,573-579`.
- No Candidate B is currently authorized. Passing this gate, once adopted, is a **precondition**
  for the separate committing step of opening Candidate B (its own committee decision plus PI
  authorization, per decision 036 §9); it is never itself an opening.

## 2. Gate semantics

The gate consists of **five cumulative conditions** (B1–B5). All five must reach `PASS` for the
gate to pass. Any `FAIL` closes the Candidate-B proposal under review without further
computation. Any `UNRESOLVED` blocks the gate — an `UNRESOLVED` condition is never coerced,
presumed, or averaged into a `PASS`. Conditions are evaluated documentarily first; no condition
may be settled by generating new scientific data under this gate.

Every certificate, witness, or estimate offered against B1–B5 must be independently re-derived
before being relied on (author ≠ sole verifier, per the decision-035 §5 precedent).

### B1 — Structural non-redundancy with respect to Candidate A and R-VAR

Candidate B must be **mathematically distinct** from Candidate A's observable family and from
the closed R-VAR statistics. Low empirical correlation is **not** sufficient and observed
correlations must never be converted into structural proofs.

**Prior-information map.** Define

```text
F_old(C) = (F_PR009(C), F_RVAR(C))
```

with each component pinned to a committed definition, no placeholder symbols:

- `F_PR009(C)` — the frozen PR009 preregistration statistic
  (`dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_PREREGISTRATION.md` §5), not the matrix §3
  entropy-based hypothesis template. **The matrix's template is superseded and must not be used
  here**: the preregistration's own §4 rejects endpoint entropy explicitly ("Those columns add
  no information beyond beam population. They are prohibited as the PR009 primary observable,"
  `:46-58`).

  Two-stage definition, both stages frozen:

  1. **Ensemble construction (deterministic given `C`).** Apply the frozen K-beam continuation
     predicate and deterministic start rule of §5.2–5.3
     (`M=3, K=64, MAX_DEPTH=12, MAX_STARTS=40`, `boundary_minimals_invariant` start sampling,
     `dev/measure_kbeam_peeloff.py`'s Definition-2 predicate) to `C`, producing a ladder ensemble
     indexed by depth `k = 0..MAX_DEPTH`. `F_PR009` is therefore not a functional of an isolated
     poset in the naive sense — it is a functional of `C` composed with this frozen deterministic
     ensemble map; any B1 exercise must state it is invoking this exact composition.
     **Correction (A4, decision 037 §9):** this construction is *not* free of randomness beyond
     `C`. PR009 prereg §16.7 (`:532-561`) fixes an exchangeable tie-break seeded by
     `TIE_RANK_MASTER_SEED = 9009009`, dependent on the sprinkling `seed`, not solely on the
     abstract poset — the prereg itself calls the resulting estimator "a reproducible
     **randomized** order-only estimator conditional on the frozen ranks." A witness-equality
     check under §2 Route 1 is therefore only well-posed if either (i) the candidate witness
     posets `C1`, `C2` are **tie-free** at every depth transition used (no two survivor rungs tied
     on `d_ij(k)`), so the tie-break is never invoked, or (ii) a single pre-frozen `seed` (and
     hence tie-rank assignment) is fixed for both `C1` and `C2` before the comparison is made, and
     that seed is stated as part of the witness. An exerciser must not choose a tie-rank
     assignment after seeing the candidate posets — doing so would manufacture equality rather
     than discover it.
  2. **Per-depth statistic profile (§5.4, §8.1).** For each transition `k -> k+1`, using the
     multiset `P_k` of pairwise enclosing-diamond separations `d_ij(k)` among survivor rungs at
     depth `k` (§5.3):

     ```text
     W_k = lower_median(P_k)                         (the width itself — required, not optional)
     theta_raw(k) = log(W_{k+1}) - log(W_k)           (only when both widths are evaluable)
     ```

     **`W_k` must be carried explicitly, not dropped in favor of `theta_raw(k)` alone**: since
     `theta_raw(k) = Delta log W_k`, two ensembles can share an identical `theta_raw` profile
     while differing in absolute width scale — collapsing to `theta_raw` alone would let a `B`
     built directly from raw width slip past this sub-gate as spuriously "novel." The output
     profile per depth is `(n_survivors(k), W_k, theta_raw(k), slice_status)`, with
     `slice_status` exactly one of the four frozen states `TRANSITION_EVALUABLE / WIDTH_ONLY /
     WIDTH_UNEVALUABLE / EMPTY` (`:466-476`) — this is the abstention grammar to use, not an
     analogy borrowed from PR010. **Output type:** a profile indexed by depth `k`, each entry a
     4-tuple with the stated abstention states; no run of PR009 ever reached scoring
     (`dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_CLOSURE_DECISION.md`), so this is the frozen
     *definition*, not a scored result — B1 exercises it by hand or by dev-only computation on
     toy posets, never by reading PR009/PR010 production data (`NO_GROUND_TRUTH_LEAKAGE`,
     `NON_CORROBORATION` discipline).

- `F_RVAR(C)` — the closed R-VAR prior-art functional, a **single joint** order-only multiset
  over `Min(C)` — **not** a pair of marginal multisets, which would let `B` recombine the
  per-element `L`–`future_card` correlation and appear spuriously novel by construction:

  ```text
  F_RVAR(C) = { (L(i), future_card(i)) : i in Min(C) }
  ```

  where `L(i)` is the longest-chain height from minimal element `i`, and

  ```text
  future_card(i) = |future(i)| = |J^+(i)|,   i in Min(C)
  ```

  is the **unrestricted** future cardinality — the sum is taken over the full poset `C`, not
  intersected with `Min(C)` (confirmed against the implementation:
  `dev/measure_pr003_rvar_egs_falsification_test.py:127`,
  `future_card_min = C[:, minimal].sum(axis=0)`, a column sum over all `N` rows, restricted only
  in *which* columns `i` are selected, not in which rows count toward the sum). Writing
  `future_card(i) = |J^+(i) ∩ Min(C)|` would be a different, smaller-domain statistic and must
  not be substituted.

  Pairing PRIMARY/SECONDARY adjudicated in
  `docs/comite/comite_decision_021_rvar-egs-truncation-object.md` §8; joint values computed
  per-element (though only reported as separate marginal summaries) by
  `dev/measure_pr003_rvar_egs_falsification_test.py:14-24,85-89` →
  `dev/rvar_egs_falsification_test_result.json`. **Output type:** a single multiset of ordered
  pairs over `Min(C)`, order-only, permutation-invariant, no auxiliary sort key.
  `R_VAR_STATUS = CLOSED_NEGATIVE_RESULT` (`docs/rvar_closure_negative_result.md`) records that
  this functional's MINK null is quasi-degenerate on this project's frozen box geometry — a
  statement about calibration on this bench, not about the functional's definition or its
  validity as a redundancy target. Citing `F_RVAR` here does not reopen, rerun, or recalibrate
  R-VAR.

**Correction (2026-07-19, PI review, two points):** (i) the longest-chain/cardinality-of-future
core of R-VAR (`L`, `future_card`) is committed prior art with an exact definition and a
measured record on this bench — it is not an absent or unlocated proposal, and citing it here
reactivates nothing. What has **not** been located anywhere in the repository is any
construction extending `F_RVAR` with shadows (`S_z`) or a boundary object (`H_A`); no committed
definition and no evaluation of that extension exists. That shadows/`H_A` extension, not the
`L`/`future_card` core, is the part of R-VAR that remains a pending, unauthorized proposal and
stays out of scope (§0). (ii) `F_PR009` must carry `W_k` explicitly and `F_RVAR` must be a joint
per-element multiset, not marginals — both corrected above; a version omitting either leaves a
redundancy loophole (a `B` built directly from absolute width, or from a per-element
recombination of `L` and `future_card`, could otherwise pass B1 spuriously).

**Scope statement (advisory, decision 037 §9 item 2, falsifier finding 4).** `F_old` as defined
above is explicitly scoped to Candidate A and R-VAR — the two prior-art objects decision 036 was
concerned with. It is **under-inclusive** against this project's sealed estimator-v2 family:
`future_card(i)` is literally the sealed `O_min(i)` restricted to `i in Min(C)`
(`docs/estimator_v2_freeze.md` §A; `nachocausal/gate.py:10` scores `improvement(O_min) < tau(n)`).
A `B` that repackages `O_min`/`improvement` over **non-minimal** elements would pass B1 by
construction while being structurally redundant with the sealed estimator. This is left as an
intentional scope limit for this version of the gate — decision 036's mandate was specifically
Candidate A and R-VAR — not a defect the gate silently hides. Whether `F_old` should later be
widened to cover the full `O_min`/`improvement` family is a separate policy choice belonging to
the committee and PI when a concrete `B` proposal makes it concrete, not resolved here.

`PASS` requires one of:

1. **Witness posets** `C1`, `C2` such that

   ```text
   F_old(C1) = F_old(C2)   but   B(C1) != B(C2)
   ```

   where `F_old(C1) = F_old(C2)` means: exact equality of the `F_PR009` per-depth profile
   `(n_survivors(k), W_k, theta_raw(k), slice_status)` over the same frozen depth range and
   ensemble-construction parameters, **and** exact equality of the `F_RVAR` joint multiset
   `{(L(i), future_card(i)) : i in Min(C)}` (compared as a multiset, since `Min(C)` carries no
   canonical labeling).

2. An **equivalent mathematical certificate** ruling out that `B` is a deterministic function of
   the **joint** `F_old = (F_PR009, F_RVAR)` on the relevant domain. (A4-adjacent correction, A1,
   decision 037 §9: the certificate must rule out dependence on the joint pair, not on either
   component alone — a `B` determined by `(F_PR009, F_RVAR)` together but by neither marginal
   separately would satisfy a "F_PR009 or F_RVAR" reading while being exactly the redundant case
   this condition exists to forbid.)

Where a comparable scalar ordering exists on a component of `F_old`, a counterexample to a
**merely monotone** equivalence must additionally be sought (two posets ordered one way by that
component and the opposite way by `B`); a distinctness witness alone does not discharge the
monotone case when an ordering comparison is well defined.

The accepted *form* of such a witness has precedent in the repo: the hand-exhibited
equal-`|relations|`, different-`S` poset pair of `dev/OP22_BD_VIABILITY_DOSSIER.md` V2 (diamond
vs Y-poset). That precedent is cited for form only; no BD content is imported into this gate.

Verdicts: `PASS` (witness or certificate exhibited and independently re-derived), `FAIL`
(a proof that `B` **is** such a function), otherwise `UNRESOLVED`. Because `F_PR009` and
`F_RVAR` are already anchored to committed definitions, the only condition-level `UNRESOLVED`
this sub-gate should ordinarily record is a specific, dated failure to exhibit a witness or
certificate at exercise time — not an anchor gap.

### B2 — Order-only computability

`B` must be defined solely from the causal order of an abstract finite poset and be invariant
under relabeling/permutation of elements. During **construction, selection, and orientation**,
`B` may not use:

- coordinates;
- the embedding;
- `r = 2M`;
- the known horizon;
- BH/MINK labels;
- auxiliary keys derived from ground truth.

The hidden geometry may only be used afterwards, for evaluation/scoring — never to build `B`
(founding rule, `CLAUDE.md`; matrix §4 order-only construction requirements). Any embedding
assistance in cut selection is a `FAIL` (matrix §4 kill clause).

Verdicts: `PASS` requires a written order-only construction specification meeting the list
above; `FAIL` on any embedding assistance; otherwise `UNRESOLVED`.

### B3 — Real bench coverage (read-only reuse of the PR010 artifact)

The PR010 development coverage artifact is reused **read-only**:
`data/reports/pr010_reference_depth_coverage_development.csv` with sidecar
`data/reports/pr010_reference_depth_coverage_development.sha256` (verified `OK` against the CSV
on 2026-07-19). No seed is recomputed, regenerated, extended, or supplemented; the PR010
development band and the reserved confirmatory bands remain exactly as frozen.

Two expressly distinguished cases:

1. If `B` consumes the **same** ladders, depths, or reference units as PR009/PR010 — i.e. units
   of the form `(seed, spacetime_kind, depth_k)` over the window `depth_k = {3,4,5}` — then the
   PR010 table is **binding as the support envelope**: `B` may not assume support the table does
   not show.
2. If `B` uses a **different combinatorial object**, the table bounds what the bench offers but
   does **not** automatically demonstrate coverage for `B`'s units. In that case `B` requires
   its own coverage showing, comparable in rigor to PR010's coverage study (as matrix §6 step 5
   already demands), before this condition can `PASS`.
3. **Budget comparability (A2, decision 037 §9).** Matrix §6 step 5's amended clause requires,
   verbatim, that B's reference-coverage / matched-cut population demands be met "under a budget
   comparable to the one that defeated Candidate A" (`next_observable_candidate_matrix.md:164-167`);
   absent that showing, B remains closed alongside A. This is a distinct check from cases 1–2
   above: cases 1–2 establish that support *exists*; this case establishes that reaching it costs
   no more than the budget PR009/PR010 already spent before hitting `FAILED_DATA_CONTRACT` /
   `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`. `B` must state the concrete unit cost (seeds,
   depths, starts, or the equivalent for its own combinatorial object) needed to reach the support
   level cases 1–2 require, and that cost must be shown comparable to — not merely bounded by —
   the PR009/PR010 budget. This case is a cumulative, independent requirement of B3: cases 1–2
   passing does not imply case 3 passes.

A coverage insufficiency under this condition, including a budget-comparability shortfall, is a
bench/design limitation, typed at the contract/design tier — it is **not** a scientific failure
of `B`.

Verdicts: `PASS`, `FAIL` (only for a demonstrated design-tier infeasibility, named as such),
otherwise `UNRESOLVED`.

### B4 — Boundary and censoring controls

Before Candidate B may open, it must be shown that the bench can distinguish `B`'s signal from:

- the temporal edge of the patch;
- the radial edge of the patch;
- the patch height;
- censoring by depth;
- abstention driven by lack of coverage;
- **(advisory, decision 037 §9 item 2, physicist)** the corner/boundary-artifact mode named by
  `docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md` (`:158,160,184`): the
  interval-DP argmax corner artifact (`|D*|≈N-few`, crossing interface `B∈{3..8}` independent of
  `N`) — a genuine horizon cut should grow like `sqrt(N)`, so B4 requires an explicit
  N-scaling/crossing-interface-growth control, not just the generic controls above;
- **(advisory, same source)** a generic-cut/cardinality-matched baseline per matrix §4
  (`next_observable_candidate_matrix.md:104,106-114`), so that `B`'s signal is compared against
  an arbitrary cut of the same size, not only against the boundary/censoring modes listed above;
- **(advisory, same source)** the aspect-ratio MINK-near-degeneracy mechanism
  (`docs/rvar_closure_negative_result.md:75-83`, `comite_decision_020...:184`): the frozen tall
  box's `T_EDGE/R_EDGE=5` drove two independently designed R-VAR objects into near-delta MINK
  nulls; B4 requires this be named and checked as a control, not merely risked silently — noting
  (physicist's Focus (c)) that the same near-complete MINK order could equally collapse
  `Delta_B`'s numerator rather than only shrink `F_B`'s denominator, so the sign of the effect on
  a cut statistic is not predictable from the R-VAR per-element result alone.

If the **existing** data and frozen artifacts do not permit these controls, the status of this
condition is `UNRESOLVED` — never `PASS` by presumption. Generating new data to settle it is
outside this gate and would require its own authorization.

**(advisory, decision 037 §9 item 2, falsifier — embedding-material quarantine.)** Any B4 control
built "from existing material" must be checked against the same order-only firewall as B2: if the
existing material includes embedding-derived diagnostic masks (e.g. interior/exterior `r`-based
labels marked "diagnostic only" in the R-VAR scripts), a control outcome computed from them may
not feed back into `B`'s construction, selection, or orientation, nor into redesigning a
successor `B` — that would be embedding-guidance one step removed, in violation of B2's own
firewall. Either B4's controls must be shown order-only, or the material used must be named and
quarantined from `B`'s design process explicitly.

**(advisory, decision 037 §9 item 2, falsifier — gate re-entry discipline.)** A `FAIL` closes the
proposal under review, but §0 permits "a successor proposal occupying that slot" with no attempt
limit stated. To avoid iterating designs against known B4/B5 failure reasons (tuning against the
bench), any successor Candidate-B proposal exercising this gate must cite every prior gate
attempt against the same matrix §4 slot and its recorded failure/unresolved conditions, in the
`NON_CORROBORATION` spirit already binding elsewhere in this project. This does not cap the
number of attempts; it requires each attempt's record to be visible to the next.

Verdicts: `PASS` (controls constructible and documented from existing material), `FAIL`
(a control is structurally impossible for `B` on this bench and `B`'s proposal offers no
replacement bench path), otherwise `UNRESOLVED`.

### B5 — Identifiability plausibility at reachable N

Before any Candidate-B PR is opened, `B`'s scientific contrast must be fixed, and the expected
signal

```text
Delta_B(N) = | E[B | Schwarzschild] - E[B | flat] |
```

must be estimated against a **conservative fluctuation envelope** `F_B(N)` that includes
sprinkling-to-sprinkling variation, seed variation, and finiteness effects. The minimal
condition is that, for some `N` actually reachable by the bench, the conservative signal band
protrudes above the noise envelope.

This condition presupposes `B`'s scientific contrast is already fixed (stated above); B1/B2 treat
`B` as not yet fully specified, so B5 may only be exercised once that fixing has happened —
exercising B5 first is a scope error, not a shortcut.

Rules:

- No sigma threshold is invented now, and none may ever be tuned against inspected data.
- Theory and already-existing results are used first. Only they may ground the estimate at this
  stage; no new scientific data may be generated under this gate.
- **(A6, decision 037 §9 — restructured into three disjoint antecedents, replacing the single
  governing conditional that previously scoped only the `UNRESOLVED`-leaning branch.)** Exactly
  one of the following three cases applies; they are mutually exclusive and jointly exhaustive of
  the epistemic states existing theory and results can leave this condition in:

  1. **If existing theory and already-existing results determine that a separation above noise
     exists** for some reachable `N`, the terminal is `FEASIBILITY_PLAUSIBLE` — sufficient prior
     evidence of separation above noise exists. Does **not** automatically open Candidate B and
     is **not** a scientific result.
  2. **If existing theory and already-existing results determine that the expected signal is
     covered by fluctuations across the entire reachable range**, the terminal is
     `NOISE_DOMINATED_AT_REACHABLE_N`. This terminal establishes **only** identification
     infeasibility within the finite range currently reachable by this bench; it establishes
     **neither** the physical absence of signal **nor** universal order-only blindness. A
     bench-specific negative, not a physical no-go, and self-contained — it needs no external
     precedent to be valid.
  3. **If existing theory and results determine neither of the above** — i.e. they do not fix the
     signal-to-fluctuation relation one way or the other — the terminal is
     `UNRESOLVED_NEEDS_MICROPILOT`. Existing information is insufficient. Does **not** authorize
     executing the micro-pilot.

  No fourth outcome and no free-form verdict outside these three tokens is permitted under any
  reading of this condition.

Verdicts: `PASS` only via `FEASIBILITY_PLAUSIBLE`; `NOISE_DOMINATED_AT_REACHABLE_N` closes the
proposal at the bench tier; `UNRESOLVED_NEEDS_MICROPILOT` blocks the gate.

## 3. Micro-pilot boundary

A micro-pilot, if ever pursued after an `UNRESOLVED_NEEDS_MICROPILOT` terminal, requires its own
separate authorization (committee decision plus PI sign-off) and must **first freeze**: the
definition of `B`, the scientific contrast, the sizes `N`, the seeds, the terminal read-out, and
— **(A3, decision 037 §9)** — the quantitative separation criterion used to decide whether
`Delta_B(N)` "protrudes above" `F_B(N)` and the fluctuation-envelope estimator itself. Neither of
these two is defined anywhere in this draft; fixing them only after micro-pilot data exists would
set the `FEASIBILITY_PLAUSIBLE`/`NOISE_DOMINATED_AT_REACHABLE_N` boundary on inspected data,
violating `NO_POST_HOC_TUNING` in the gate's own designed continuation. This draft does not
design, schedule, or budget any micro-pilot.

## 4. Proposed matrix pointer (NOT applied; for the future adopting decision only)

If and when a committee decision adopts this gate, that decision may append to matrix §6 step 5
the following sentence (verbatim proposal; this draft does not edit the matrix):

> The explicit, dedicated feasibility showing required by this step is operationalized as the
> five-condition cumulative gate of
> `research_program/work_packages/candidate_b_viability_gate.md` (B1 structural non-redundancy,
> B2 order-only computability, B3 real bench coverage, B4 boundary/censoring controls,
> B5 identifiability plausibility at reachable N), adopted per `docs/comite/comite_decision_0XX`.

## 5. What passing this gate would and would not mean

Passing B1–B5, once the gate is adopted, would mean only that drafting a Candidate-B
preregistration is *worth proposing* to the committee. It would not open Candidate B, would not
constitute evidence about horizons, would not alter the PR009/PR010 closures or Candidate A's
untested/untestable status, and would not reactivate the separatrix proposal. Failing or
blocking at any condition carries no physical meaning: it is a statement about this bench and
this design contract only.
