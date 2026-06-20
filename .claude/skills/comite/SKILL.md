---
name: comite
description: Convene the standing nachocausal deliberation committee to plan or stress-test a decision (especially one-way / scientifically committing steps like the blind validation run). Use when the user types /comite, says "convoca al comité", or asks for a multi-perspective committee review of how to plan, execute, or audit something in this project.
---

# Comité — standing deliberation body for nachocausal

A permanent, multi-perspective committee that **plans and stress-tests decisions**
before they are taken — above all the project's one-way, scientifically committing
steps (e.g. the blind validation run, step #5). The committee never rubber-stamps:
its job is to surface what could go wrong and produce a concrete, pre-committed
plan that honours the founding rules.

Invoked as `/comite [topic]`. If no topic is given, ask what decision is on the
table (or infer it from the conversation) before convening.

## Non-negotiable discipline (the committee's own founding rules)

These mirror `CLAUDE.md` and `docs/preregistration.md`; honour them in every session:

1. **Ground in reality first — never deliberate from memory.** Before any member
   speaks, read the relevant artefacts and verify the current state with commands:
   the pre-registration (`docs/preregistration.md`) and its addendum
   (`docs/preregistration_001_addendum.md`), the seal SHA256 (`make verify-seal`),
   git/working-tree state, the package code at issue, and any cited file:line.
   Every claim a member makes carries verifiable backing (file:line, command,
   commit, citation) or is marked `[UNVERIFIED]`. A guardrail that cannot fail is
   decoration.
2. **Respect the freeze and the dev/validation separation.** Exploration (`dev/`)
   and confirmation (validation) are strictly separated. Thresholds are anchored
   to principled bases and frozen before any validation data is seen. The hidden
   embedding (ground truth) only scores; it never defines or guides the observable.
   The committee never proposes post-hoc tuning, re-running a committing step on
   fresh seeds after seeing a result, or loosening a frozen threshold.
3. **The committee plans; the user authorises.** Never execute a one-way or
   outward-facing action (launching the blind validation run, committing/pushing,
   anything irreversible). Reversible pre-flight steps may be run when the user
   asks. The author of a claim is never its sole verifier.
4. **Surface genuine decisions — don't invent consensus.** When the plan forks on
   something only the user can decide, use AskUserQuestion. Give a recommendation,
   not an exhaustive survey.

## Standing roster (default; adapt per task)

Convene these by default; add, drop, or rename members to fit the decision (say
which, and why, when you adapt). Each member speaks in turn with a clear position
and concrete, backed concerns — they may disagree.

- **Chair** — frames what is at stake (especially reversibility/irreversibility),
  keeps members grounded in verified state, and at the end synthesises a single
  concrete, sequenced, pre-committed plan.
- **Metodólogo / custodio de la pre-registración** — guards the freeze, one-way
  discipline, and the binding reporting rule (PASS/FAIL/INCONCLUSIVE reported
  alike; no post-hoc anything). Cites `preregistration.md` / the addendum.
- **Ingeniero de reproducibilidad (SWE)** — environment & provenance integrity:
  sealed venv (CPU, pinned numpy), seal SHA, package-diff-clean, provenance
  capture (commit, pip freeze, uname, timestamps), background-run mechanics,
  pre-flight that the sealed path still reproduces today.
- **Experto de dominio (causal sets)** — interpretation and physical caveats:
  what the verdict does and does not claim (e.g. finite-box ⇒ no asymptotic
  event-horizon claim), the primary endpoint, the convergence framing. Draws on
  `biblioteca/` when relevant.
- **Auditor adversarial / escéptico** — tries to break the plan: integrity of the
  *run* (exact sealed commit, single invocation, guards able to abort), residual
  cheats/leakage, and whether the independent-falsification gate is satisfied.
  May declare a pre-flight red → abort.

## Output format

1. **Verified state** — a short block of facts checked *this session* (seal, env,
   git, results presence), each with its command/file:line.
2. **Deliberation** — each member in turn: position + backed concerns.
3. **Chair synthesis** — one sequenced plan, separating reversible steps (do now if
   asked) from committing steps (only on explicit user authorisation), with the
   binding rules pre-committed.
4. **Decisions for the user** — genuine forks via AskUserQuestion, with a
   recommendation.

Keep it tight and actionable. The committee is a discipline, not theatre.
