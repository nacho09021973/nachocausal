# AGENTS.md

Guidance for AI agents working in this repository.

## Project Context

`nachocausal` is a scientific recoverability benchmark, not a reconstruction
claim. It tests whether 1+1D Schwarzschild event-horizon structure can be
recovered from causal-set order alone, under pre-registered PASS/FAIL criteria.

Read these before changing behavior or interpreting results:

- `CLAUDE.md` for project-specific working rules and local reference material.
- `README.md` for current status, reproducibility commands, and pending work.
- `docs/preregistration.md` and the numbered preregistration/result docs for
  frozen confirmatory protocol.
- `docs/estimator_v2_exploration.md` and related estimator-v2 docs for
  post-FAIL exploration context.

## Non-Negotiable Scientific Rules

- Treat the committed validation path as sealed unless the user explicitly asks
  to work on a new preregistered seal.
- Do not tune thresholds, estimators, seeds, or criteria using held-out
  validation results.
- Keep exploration and confirmation separate. `dev/` is exploration; committed
  package code under `nachocausal/` is the validation instrument.
- Ground truth embedding may score results but must not guide order-only
  observables or boundary construction.
- Any scientific or benchmark claim must include verifiable support
  (file/line, command output, commit, or citation) or be marked `[UNVERIFIED]`.
- Burned validation seeds must not be reused or reinterpreted as fresh evidence.

## Repository Layout

- `nachocausal/` - committed package and validation path.
- `nachocausal/fixtures/` - committed reproducibility fixtures, including
  `tau_table.json`, `o_samples.json`, and `gate_evidence.json`.
- `tests/` - regression, leak, seed, tau-table, checksum, and estimator tests.
- `docs/` - preregistrations, result records, seal records, and exploration
  writeups.
- `dev/` - exploration sandbox. A small set of exploration scripts is tracked as
  a scoped exception, but generated raw data and incidental files should stay
  untracked.
- `scripts/` - utility scripts such as tau-table generation.
- `biblioteca/` - local git-ignored causal-set literature library. It can be
  used for background and citations but is not part of the committed project.

## Environment

- Use Python 3.12 where possible; sealed environment used Python 3.12.3.
- Install with `pip install -r requirements.txt` in a virtual environment.
- `numpy==1.26.4` is hard-pinned for bit-exact reproducibility. Do not relax or
  upgrade it casually.
- The validation path is pure numpy plus pytest.
- `make gate` is optional and requires the external `c-minz/Python-causets`
  clone on `sys.path` via `NACHOCAUSAL_MINZ_PATH` (default
  `~/cs-horizon-reuse-check`). It is not required for the benchmark validation
  path.

## Common Commands

```bash
make test
make dry-run
make verify-seal
make gate
```

Use `make test` before finishing changes that touch package code, fixtures, or
tests. Use `make dry-run` only when the sealed PASS/FAIL path itself is relevant.
Use `make verify-seal` when touching or auditing frozen threshold code.

## Development Guidance

- Prefer narrow, auditable changes over broad refactors.
- Preserve deterministic behavior, seeded randomness, and bit-exact fixture
  expectations.
- Do not modify committed result docs, frozen thresholds, or seal records unless
  explicitly requested.
- If changing estimator-v2 or exploratory logic, keep confirmatory language out
  of the change unless it has been run only under a frozen protocol.
- Respect `.gitignore`: do not add raw generated ensembles, `results/`,
  `biblioteca/`, virtualenvs, caches, or `__pycache__`.
- Keep documentation precise about whether evidence is exploratory,
  preregistered, sealed, or held-out.

## Before Finalizing

- Check `git status --short` and make sure changes are intentional.
- Run the smallest relevant verification command. For most code changes this is
  `make test`.
- Report any command you could not run and why.
