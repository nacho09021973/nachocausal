# nachocausal

Recovering black-hole horizon structure from causal-set order alone — framed as a
*recoverability* benchmark, not a reconstruction claim.

The project starts deliberately narrow and disciplined: reproduce, blind to coordinates and
under a success/failure criterion frozen in advance, the known-truth detection of a
Schwarzschild event horizon in a 1+1D causal set, using the order-only observable validated
in recent literature (arXiv:2605.06813): the longest timelike chain from minimal elements —
interior elements have futures truncated by the singularity.

Founding rules (see docs/preregistration.md):
- A guardrail that cannot fail is decoration. Every claim carries verifiable backing
  (file:line, command, commit, citation) or is marked [UNVERIFIED].
- Exploration (dev) and confirmation (validation) are strictly separated. Thresholds are
  anchored to principled bases and frozen before any validation data is seen.
- The hidden embedding (ground truth) only scores; it never defines or guides the observable
  or the boundary.

Status: pre-registration frozen. Dev prototype built and smoke-tested (exploration only; lives
in dev/, deliberately not committed). No frozen result yet. No event/apparent horizon, Kerr, or
manifoldlikeness claim.

## Literature library

An extensive local library of causal-set-theory articles and books lives in `biblioteca/`
(papers by Bombelli, Sorkin, Benincasa, Dowker, Surya et al.; textbooks; and the directly
relevant "Towards black-hole horizons and geodesic focusing in causal sets"). It also holds
markdown notes and PDF-derived markdown under `biblioteca/derived-md/`. The folder is local
reference material only — it is git-ignored and not part of the committed project.
