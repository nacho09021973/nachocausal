# Work Packages

Subárbol para paquetes de trabajo activos del programa.

Cada paquete debería fijar:

- pregunta exacta;
- alcance;
- evidencia requerida;
- artefactos esperados;
- criterio de cierre o de abandono.

## Active design front

`next_observable_candidate_matrix.md` translates the post-PR008 literature review into a
ranked, falsifiable observable-design sequence. It authorizes no production experiment.

Candidate A's cheap kill test (the originally "first permitted next artifact") ran as PR009,
which closed `FAILED_DATA_CONTRACT`; its coverage-redesign successor PR010 closed
`PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`. Neither is a scientific result about Candidate A's
observable (see `dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_CLOSURE_DECISION.md`,
`dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md`). The matrix's §6 sequencing rule was amended
2026-07-17 per `docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md` to admit
this closure as a non-scientific precondition for opening Candidate B, conditional on a dedicated
feasibility showing for Candidate B itself — see that decision for the full text and caveats. No
candidate is currently open; the next permitted artifact is either a redesigned Candidate-A
attempt or the Candidate-B feasibility showing the amendment requires.

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
