# Comité Decision {{NNN}} — {{SLUG}}

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question
{{DECISION_QUESTION}}

## 2. Verified state
Facts checked **this session**, each with its command / file:line (seal SHA, env, git, results
presence). Anything unchecked is marked `[UNVERIFIED]`.
{{VERIFIED_STATE}}

## 3. Dossier
Files and references the chair supplied to the committee:
{{DOSSIER_LIST}}

## 4. Expert briefs (wave 1 — blind, parallel)
### Reproducibility engineer brief
{{REPRODUCIBILITY_BRIEF}}
### Mathematician brief
{{MATHEMATICIAN_BRIEF}}
### Mathematical logic brief
{{MATHEMATICAL_LOGIC_BRIEF}}
### Physicist brief
{{PHYSICIST_BRIEF}}

## 5. Falsifier attack
{{FALSIFIER_ATTACK}}

## 6. Pre-registration verdict
{{PREREGISTRATION_VERDICT}}

## 7. Literature verdict
{{LITERATURE_VERDICT}}

## 8. Synthesis
Recommended direction, ranked alternatives, and **open disagreements (never hidden)**. If a
pre-registration BLOCK or an unresolved falsification exists, the verdict cannot be a PROCEED
verdict.
{{SYNTHESIS}}

## 9. Next-step spec
The sequenced plan, separating **reversible** steps (may be run now if the user asks) from
**committing** steps (only on explicit user authorisation), with the binding rules pre-committed
and the falsifier's minimal falsification test included:
{{NEXT_STEP_SPEC}}

## 10. Verdict
COMMITTEE_DECISION_VERDICT={{VERDICT}}

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
