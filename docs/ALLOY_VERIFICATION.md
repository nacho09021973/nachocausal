# Alloy verification track

`nachocausal` can use **Alloy as a bounded model checker** for claims that have already been
translated into an explicit finite relational model.

This track is intentionally narrow:

- it does **not** replace `/comite`;
- it does **not** replace `/auditor`;
- it does **not** turn a bounded pass into a theorem;
- it does **not** enter before the claim is formalized into a checkable model.

## Entry condition

Use Alloy only when all of the following are true:

1. the target claim has been translated into a finite relational model;
2. the model has explicit signatures, relations, facts, and a `run`/`check` target;
3. the finite scope to check is explicit;
4. an Alloy executable contract is verified locally.

If any of those is missing, the verifier must fail closed.

## Repo convention

- committed/rerunnable models: `formal/alloy/`
- exploratory models: `dev/alloy/`
- verification notes: `docs/alloy/`

## Local command contract

The verifier must use a **verified local command**, not a guessed CLI. A convenient pattern is:

```bash
export ALLOY_CMD="$HOME/.local/bin/alloy"
```

If that command is absent or unverified, the verifier must fail closed with
`ALLOY_VERDICT=ALLOY_TOOL_UNAVAILABLE`.

## Guardrail

Alloy is **supporting evidence about a model**, not a scientific proof about the project claim.
A passed bounded check may justify:

- "no counterexample was found in the encoded model at scope S"

It may not justify:

- "the claim is proved"
- "the physical statement holds in general"
- "the translation is faithful unless independently reviewed"

## Skill entrypoint

Use:

```text
/alloy-verifier <claim/model question>
```

The verifier writes a single note under `docs/alloy/`.
