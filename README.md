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

Status: pre-registration frozen; **instrument sealed** (block #4). The order-only estimator,
generator, frozen thresholds, and blind PASS/FAIL runner live in the committed package
`nachocausal/`, with every threshold value fixed in writing in
`docs/preregistration_001_addendum.md` *before* any validation data. An independent adversarial
audit cleared the seal. **Frozen result (step #5, 2026-06-21): `FAIL`** — the single committed
blind run emits FAIL; the causal order carries strong horizon signal (sign-flip p≈1e-6 at all
N) but the v1 estimator misses the pre-registered localisation-coverage (0.30 < 0.50) and
false-positive (0.10 > 0.05) bars. Recorded verbatim in `docs/preregistration_001_result.md`;
the validation seeds are now burned (no re-run/re-tune). No event/apparent horizon, Kerr, or
manifoldlikeness claim.

## Running / reproducing on a fresh machine

The validation path is **pure numpy**. Anyone can reproduce everything under identical
conditions with just this repo and the pinned environment:

```bash
git clone https://github.com/nacho09021973/nachocausal
cd nachocausal
python3 -m venv .venv && . .venv/bin/activate     # Python 3.12 (sealed: 3.12.3)
pip install -r requirements.txt                    # numpy==1.26.4 (hard-pinned), pytest

make test       # bit-exact regression vs the 64 audited O multisets + leak/seed guards
make dry-run    # run the full frozen PASS/FAIL path on dev seeds (verdict discarded)
make verify-seal  # print the thresholds.py SHA256 (compare to the addendum)
```

numpy is hard-pinned because the frozen poset/estimator are guaranteed bit-for-bit reproducible
only under the version the instrument was sealed against; the package hard-fails on any other
numpy.

The optional Minz admissibility cross-check (`make gate`) is **not** on the validation path and
**not** required to run the benchmark. It needs the external clone
[c-minz/Python-causets](https://github.com/c-minz/Python-causets) on `sys.path` via the env var
`NACHOCAUSAL_MINZ_PATH` (default `~/cs-horizon-reuse-check`). Its evidence is already recorded in
`nachocausal/fixtures/gate_evidence.json`.

## Literature library

An extensive local library of causal-set-theory articles and books lives in `biblioteca/`
(papers by Bombelli, Sorkin, Benincasa, Dowker, Surya et al.; textbooks; and the directly
relevant "Towards black-hole horizons and geodesic focusing in causal sets"). It also holds
markdown notes and PDF-derived markdown under `biblioteca/derived-md/`. The folder is local
reference material only — it is git-ignored and not part of the committed project.
