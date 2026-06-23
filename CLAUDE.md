# CLAUDE.md

Guidance for working in this repository.

## What this project is

nachocausal is a **recoverability benchmark** (not a reconstruction claim): recovering 1+1D
Schwarzschild event-horizon structure from causal-set order alone. See `README.md` and the
**frozen** pre-registration in `docs/preregistration.md`. The reuse/tooling decision is in
`docs/reuse_check.md`.

## Founding rules (honor these in any change)

- A guardrail that cannot fail is decoration. Every claim carries verifiable backing
  (file:line, command, commit, citation) or is marked `[UNVERIFIED]`.
- Exploration (`dev/`) and confirmation (validation) are strictly separated. Thresholds are
  anchored to principled bases and frozen before any validation data is seen.
- The hidden embedding (ground truth) only scores; it never defines or guides the observable.

## Layout

- `dev/` — exploration sandbox. The exploration **scripts** (`dev/explore_*.py`) are committed as
  scoped exceptions so they sync across machines via the GitHub clone (see the README's "What was
  explored" probes); generated raw ensembles (`dev_ensemble_raw/`) stay git-ignored. Committing the
  scripts does not touch the dev/validation separation — that separation is about code paths and
  seeds (dev never tunes the sealed thresholds), not about git tracking. The prototype
  `dev/prototype_o.py` runs against the external, non-vendored c-minz/Python-causets clone at
  `~/cs-horizon-reuse-check/`; run it with that repo's venv (numpy<2):
  `~/cs-horizon-reuse-check/venv_minz/bin/python dev/prototype_o.py`.
- `docs/` — frozen pre-registration and reuse-check decision (committed).
- `biblioteca/` — see below (git-ignored).

## Literature library

There is an **extensive local library of causal-set-theory articles and books** in
`biblioteca/` (~56 PDFs + notes): foundational and recent papers (Bombelli, Sorkin, Benincasa,
Dowker, Surya, Glaser, et al.), textbooks, and the directly relevant *"Towards black-hole
horizons and geodesic focusing in causal sets"*. PDF-derived markdown lives in
`biblioteca/derived-md/`. Consult it for background, definitions, and citations when reasoning
about causal sets. It is local reference material, git-ignored and not part of the committed
project.
