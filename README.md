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

Status: **pre-registration 002 PASSED — order-only horizon *localisation* in a finite 1+1D patch
is demonstrated under a fully frozen protocol.** The arc:

- **prereg-001 (v1 estimator, longest-chain/height observable): `FAIL`** (`docs/preregistration_001_result.md`).
  Strong horizon signal (sign-flip p≈1e-6 at all N) but the v1 estimator missed the pre-registered
  localisation-coverage (0.30 < 0.50) and false-positive (0.10 > 0.05) bars. Those validation seeds
  are now burned.
- **estimator-v2 sealed** (`docs/estimator_v2_freeze.md` → `docs/estimator_v2_seal.md`, seal
  `2f4c4a99…`). Exactly three changes vs v1, each anchored by principle and frozen *before* re-running:
  (A) future **volume** observable, (C) a data-independent **τ(n) abstaining gate**, (D) a minimum
  time-extent **domain gate** `T_EDGE_MIN=6` (`t_edge<6` ⇒ OUT_OF_DOMAIN, never a physical FAIL).
- **prereg-002 sealed** (`docs/preregistration_002.md`, seal `6e2c3888…`): 20 held-out seeds drawn
  **once, blind** from the reserved virgin band `[2_000_000, 2_999_999]`.
- **Frozen result (block #4, 2026-06-22): `PASS`** (`docs/preregistration_002_result.md`). All six
  checks hold at the primary endpoint (intensity 12000): sign-flip `p=9.5e-7`, coverage 0.95, median
  `|dr|/2M = 0.064 ≤ θ_loc`, boundary r-std 0.008, false-positive 0.00, Guard-v clean. 20/20 valid
  seeds at all four N levels.

**Bounded claim (do not overstate):** the causal order alone — no coordinates accessible to the
estimator — localises the horizon-associated boundary *significantly and stably* in a 1+1D
Schwarzschild model within a **finite patch**. It does **not** claim metric reconstruction, the
global event horizon (future null infinity), 3+1D, Kerr, or manifoldlikeness.

## Next phase — PR-003: from *localising* the boundary to *constructing* a horizon portion

With localisation PASSed, the next goal changes the **object the estimator returns**: from "the
boundary is between these two positions" to an **ordered subset / band of causal-set elements** — a
discrete causal curve that *is* a reconstructed portion of the horizon. The immediate defensible
target (a finite patch cannot reach the global event horizon, which needs all of future null
infinity) is an **order-only, blind reconstruction of a local portion of the 1+1D Schwarzschild
horizon**. This follows Eichhorn–Gamito–Stokes (arXiv:2605.06813, Sec. V) — longest-chain
interior/exterior split → boundary → an **outgoing fuzzy ladder** tracing the horizon → a band built
by iterating over successive antichains. **Key advance vs EGS:** they *seeded and selected* the
horizon ladder using the embedding (their §V.B); ours must be **fully order-only and blind**, seeded
from the v2 bracket boundary.

### What was explored today (2026-06-22, dev only; coords used *only* to score)

Compute engine decision: **Numba now** (fast iteration) → port the validated *integer* kernel to
**C++** at seal time with a bit-for-bit cross-check (the ladder search is integer-only, so it is
deterministic either way). Probes (committed as scoped `dev/` exceptions): `explore_ladders.py`,
`explore_direction.py`, `explore_seed_bracket.py`.

- **Feasibility — yes.** Order-only **fuzzy ladders** (EGS Def. 2) of length ≥8 are *abundant* even
  in our modest box (`t_edge=6`, N≈3600) — ladder scarcity is **not** a blocker (EGS's pessimism was
  about rigid ladders). Kernel verified correct independently at N=147.
- **#2 direction (outgoing vs ingoing), order-only — promising.** The exteriority field
  `φ = L_fut` (EGS interior/exterior diagnostic) carries direction: a relative-exteriority feature
  predicts true `sign(Δr)` with AUC **0.72–0.95** in aggregate. *Preliminary:* tiny samples; the
  **near-horizon band is still untested**.
- **#3 bracket-seeding — directionally right, low yield.** Seeding from the order-only v2 bracket
  boundary concentrates ladders near the horizon (67–100% near-horizon), confirming the bracket is a
  valid order-only seed — but only 1–3 long ladders are harvested per sprinkling, and `d_⊥ = |r−r_S|`
  median ≈ 3–4 ℓ (near, not yet the O(ℓ) target).
- **Engineering note:** the *recursive* Numba njit ladder kernel **SIGSEGVs on real BH-generator
  posets** (`t_edge=6`), even at stack depth ≈21–30; this was **not** reproduced on synthetic
  light-cone posets up to `lmax=300`, so the failure is **workload-dependent**, not a universal
  recursion-depth limit. Mechanism `[UNVERIFIED]` — symptom reproduced, Numba internals not pinned.
  The ladder builder was switched to an **iterative** (explicit-stack) form (the C++-portable shape).
- **Measurement (2026-06-23, dev): `lmax` censoring lifted at `t_edge=6`.** The earlier
  `maxlen == lmax == 30` was a cap artifact, not a real length. Sweeping `lmax` ∈ {30,40,60,80,120}
  (intensity=3600, M=3, 3 seeds): true longest-ladder lengths are **46–96+** and **seed-dependent**.
  The science counts `ge6`/`ge8` are **identical across every `lmax`/budget cell** — the "length-≥8
  ladders abundant" claim was never censored; only `maxlen` (and slightly `mean`) were. Raising `lmax`
  shifts the binding cap onto `per_start_budget`: only seed1 reached budget-insensitive **saturation
  ≈46**; seed0 (≥96, still climbing) and seed2 (≥72) stayed budget-bound, their highest-budget cells
  hitting the wall-clock cap, so those lengths are **lower bounds** (true saturation not yet
  established). Measurement only — `/tmp`, nothing frozen.

### Plan for tomorrow

1. **Write the iterative longest-ladder kernel** (explicit stack — robust, and the form we port to
   C++). The greedy-first builder is the current bottleneck; the longest-ladder search will harvest
   *more and longer* near-horizon ladders.
2. **Re-test #2/#3 in the near-horizon band** with sufficient sample: measure the direction AUC where
   it matters, and push `d_⊥` toward O(ℓ) by selecting the longest outgoing bracket-seeded ladder.
3. **Settle the two gating order-only rules:** the direction rule (#2) and a **fixed** ladder
   **selection** rule (#3) — both must be frozen before any reconstruction freeze, or it is only an
   embedding-seeded proof-of-principle, not a blind reconstruction.
4. **Then draft the revisable PR-003 plan** with success criteria in frozen form: `d_⊥ ≲ k·ℓ`,
   temporal persistence, discrete continuity, transverse convergence with density, held-out
   stability, a flat control (no persistent curve), shifted controls (vary M ⇒ the reconstruction
   shifts without retuning), and a geometric (element-set) output.

The roadmap: **boundary localisation ✅ → horizon-portion construction → convergence under patch
extension → 3+1D.**

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

## In-repo tooling — the `/comite` and `/auditor` skills

Two Claude Code skills live in `.claude/skills/` and travel with the repo, so any clone on any
machine has them with **no install step** — Claude Code auto-discovers project skills under
`.claude/skills/`. They encode this project's discipline as runnable guardrails: the committee is
**forward-looking** (deliberate before a one-way step), the auditor is **backward-looking** (verify
that what is already claimed is real).

```bash
git clone https://github.com/nacho09021973/nachocausal
cd nachocausal
# open Claude Code here — both skills are picked up automatically
```

### `/comite <decision question>` — standing deliberation committee
A 6-role, two-wave **blind** expert panel (reproducibility engineer, causal-set mathematician,
Schwarzschild physicist, falsifier, pre-registration warden, literature verifier) chaired into a
grounded, freeze-checked **decision brief** the user signs off on. The committee *proposes*; the
user *authorises* — it never launches the blind validation run, commits, loosens a frozen
threshold, or makes a reconstruction claim. Convene it for any one-way / scientifically committing
step (above all the blind validation run) or a frontier decision; also via "convoca al comité".
- Writes `docs/comite/comite_decision_NNN_<slug>.md`.
- Brief gate: `python .claude/skills/comite/check_comite_brief.py <brief.md>` — fails on a missing
  section, a surviving `{{…}}` placeholder, an invalid verdict, or a pre-registration `BLOCK`
  paired with a PROCEED verdict. `make verify-comite` runs it over every brief in `docs/comite/`.

### `/auditor [scope]` — backward-looking integrity audit
The standing guardrail against AI-faked results: every published number must be the literal output
of a committed deterministic script, the live seal must match a frozen record, the dev/validation
separation and the *hidden-embedding-only-scores* rule must hold, and no text may over-claim beyond
finite-patch 1+1D localisation. It *reports*; it never fixes. Produces an audit report with an
`AUDIT_VERDICT` the user reads; also via "audita el repo".
- Writes `docs/auditor/auditor_report_NNN_<slug>.md`.
- Mechanical core, runnable standalone (no Claude Code needed): `make audit` (or
  `bash .claude/skills/auditor/audit.sh`) — flags CI that swallows failures, app code with no
  tests, **seal drift** (live `thresholds.py` SHA recorded in no `docs/` freeze file),
  **gitignored-but-tracked** paths (committed despite being declared uncommitted), and committed
  data files with no generator. Exit `0` clean / `1` errors / `2` bad invocation.
- Report gate: `python .claude/skills/auditor/check_audit_report.py <report.md>` — fails if the
  verdict contradicts its own error/warning counts. `make verify-audit` runs it over every report
  in `docs/auditor/`.

## Literature library

An extensive local library of causal-set-theory articles and books lives in `biblioteca/`
(papers by Bombelli, Sorkin, Benincasa, Dowker, Surya et al.; textbooks; and the directly
relevant "Towards black-hole horizons and geodesic focusing in causal sets"). It also holds
markdown notes and PDF-derived markdown under `biblioteca/derived-md/`. The folder is local
reference material only — it is git-ignored and not part of the committed project.
