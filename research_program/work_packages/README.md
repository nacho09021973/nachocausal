# Work Packages

Subárbol para paquetes de trabajo activos del programa.

Cada paquete debería fijar:

- pregunta exacta;
- alcance;
- evidencia requerida;
- artefactos esperados;
- criterio de cierre o de abandono.

## Historical observable-design front (closed as program north)

The paragraphs in this section preserve the pre-Phase-0 sequencing record. They
do **not** authorize a current next artifact: Phase 0 R1 and committee decision
042 close further C1–C6-style order-only region-localizers as the program north.

`next_observable_candidate_matrix.md` translates the post-PR008 literature review into a
ranked, falsifiable observable-design sequence. It now remains a historical
triage artifact and authorizes no production experiment.

Candidate A's cheap kill test (the originally "first permitted next artifact") ran as PR009,
which closed `FAILED_DATA_CONTRACT`; its coverage-redesign successor PR010 closed
`PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`. Neither is a scientific result about Candidate A's
observable (see `dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_CLOSURE_DECISION.md`,
`dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md`). The matrix's §6 sequencing rule was amended
2026-07-17 per `docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md` to admit
this closure as a non-scientific precondition for opening Candidate B, conditional on a dedicated
feasibility showing for Candidate B itself — see that decision for the full text and caveats.
That was the permitted-next-artifact state before Phase 0 R1; it is superseded
for forward planning. No Candidate A/B/C localizer is currently open.

The feasibility showing is operationalized as a five-condition cumulative gate (structural
non-redundancy vs Candidate A/R-VAR, order-only computability, real bench coverage,
boundary/censoring controls, identifiability plausibility at reachable N) at
`candidate_b_viability_gate.md`. `docs/comite/comite_decision_037_candidate-b-viability-gate-review.md`
reviewed the first draft (`RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`, conditional on six textual
amendments A1–A6); those amendments plus the advisory B4/scope items were folded in, chair-level
re-verification reproduced clean, and the PI signed off 2026-07-19 (decision 037 §11). The gate
is now `ADOPTED_AS_GATE_DEFINITION` **as a precondition filter only** — it opens no candidate and
modifies neither decision 036 nor the matrix; opening Candidate B, exercising B1–B5 against a
concrete `B`, or any micro-pilot each remain separate committing steps requiring their own
dedicated committee decision plus PI authorization.

## WP4 identifiability synthesis

Cross-package roadmap (not a duplicate proof): `../synthesis/geometric_indeterminacy_decision.md`.
Authoritative two-point theorem: `wp4_two_point_theorem.md`.

## WP7 — F2 frente a F3 en orden producto

`wp7_f2_f3_product_order_contract.md` fija la pregunta determinista de si la
discrepancia rectangular mesoscópica de F2 controla la altura/LIS de F3 en `d=2`, o si
una cadena plantada de tamaño `Theta(sqrt(n))` produce un contraejemplo. El primer ataque
es deductivo y tiene cinco obligaciones P1--P5; no autoriza simulación, semillas, dimensión
mayor ni afirmaciones de novedad.

## Phase 3 B2 pre-opening front

The next program-level branch is prepared, but not scientifically opened, in
`phase3_b2_witness_pair_preopening_contract.md`. Its first question for
2026-07-29 is whether an intrinsic binary quasi-local target
`Q_FMOTS` admits a nontrivial Müller-style conformal witness-pair route under the
fixed-cardinality order-only channel.

This front authorizes no estimator, code, simulation, seeds, thresholds, or
reopening of the C1–C6 region-localizer line. Target adoption and witness
construction remain separate committing decisions.
