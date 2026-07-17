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

## WP4 identifiability synthesis

Cross-package roadmap (not a duplicate proof): `../synthesis/geometric_indeterminacy_decision.md`.
Authoritative two-point theorem: `wp4_two_point_theorem.md`.
