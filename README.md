# nachocausal

Recovering black-hole horizon structure from causal-set **order and counting** (the theory's
*Order + Number* data) — framed as a *recoverability* benchmark, not a reconstruction claim.

> **Note on "order-only".** Throughout this README `order-only` means **blind to the
> embedding** — no coordinates, no ground truth reach the estimator. It does **not** mean
> "without counting": cardinalities are legitimate observables. See `CLAUDE.md`.

For any AI or agent connecting to this repo, read [INSTRUCCIONES.md](INSTRUCCIONES.md) first for
the available machinery and the correct workflow between committee, auditor, external consultors,
and Alloy.

**Manuscript under review:**
[Finite order-only observation of Schwarzschild patches](docs/manuscript_limits_draft.md)
separates exact fixed-\(n\) blindness to absolute scale, completion dependence of the global
event horizon, and a matching \(n^{-1/2}\) minimax localization rate on one declared
fixed-corner \(1{+}1\) family. Its claims are narrower than the historical program roadmap below.

**Current program roadmap:** [post-N1–N5 limits-paper route](tarea_grok_2.md).
The earlier [15 July operational plan](docs/plan_operativo_15_julio_2026.md) remains historical
input where not superseded by the current roadmap.

The project starts deliberately narrow and disciplined: reproduce, blind to coordinates and
under a success/failure criterion frozen in advance, the known-truth detection of a
Schwarzschild event horizon in a 1+1D causal set, using the order-only observable validated
in recent literature (arXiv:2605.06813): the longest timelike chain from minimal elements —
interior elements have futures truncated by the singularity.

## Strategic objectives

The program has three objectives, in explicit priority order — each later one only has value
insofar as it serves the one above it:

1. **Final target — Schwarzschild 3+1D order-only.** The long-term target is Schwarzschild 3+1D
   horizon localisation/reconstruction from order-only causal information. 3+1D is the
   destination of this program, not an optional extension. Embedding coordinates may be used for
   simulation, validation, and ground truth, but never as input to the order-only estimator.
2. **Structural foundation — 1+1D lower bounds and blindness maps.** The current 1+1D work
   (Paper I / PR-003, and the WP4/WP5 identifiability program under `research_program/`) is not
   the final goal; it is the technical foundation for 3+1D, valuable to the extent that it yields
   principles that survive the step up: information-theoretic lower bounds, order-only blindness
   regions, the asymmetry between "blindness proven" and "candidate visible" (never the reverse),
   and the separation between a universal *definition* and the first computable chart on one
   concrete family. 1+1D does **not** resolve 3+1D; the "candidate visible" side is **not**
   demonstrated; and no WP5-style map is a universal *computable* map. WP4/WP5 count as a
   structural-foundation proof of principle only insofar as their lower bound closes cleanly.
3. **Operational discipline — close verifiable units before expanding scope.** The project must
   not expand indefinitely into new work packages without closing technical units first. Each
   stage must produce a minimal verifiable unit: a narrow claim, an explicit information channel,
   reproducible proofs or numerics, written interpretation limits, and a bibliography/reuse-check
   pass before any public novelty claim. Before opening large new work packages, priority goes to
   closing: WP4 as a technical lower-bound/no-go result, WP5 as a definition/unilateral chart (if
   it proceeds), and any explicit bridge toward Schwarzschild 3+1D.

### Current observable status

PR008 is closed with terminal label `BASELINE_DOMINATED`; its fixed-`K` scalar `H_hat`
is retained only as an auxiliary diagnostic or future baseline. PR009 then attempted the
frozen reference stage for a new order-only effective-expansion observable, but terminated with
`FAILED_DATA_CONTRACT`: reference-MINK coverage at depth 7 was below the preregistered
minimum. Nothing was published, evaluation and scoring were not run, and no scientific
terminal or inference about horizon sensitivity exists.

PR010 is the active design phase. It will study coverage by depth using entirely new
development seeds, choose in advance between a larger reference block and a restricted
scorable-depth range, and only then define new confirmatory seeds, a new preregistration,
and a new audit. Unpublished PR009 values are forbidden inputs. See
`dev/PR009_LADDER_ENSEMBLE_EFFECTIVE_EXPANSION_CLOSURE_DECISION.md` and
`dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md`.

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
- **Status label (2026-07-04):** `PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED;
  BLINDNESS_DOCUMENTARY_ONLY]`. The original run's raw artifact was later found unrecoverable; a
  `SUPERVISED_REVERIFICATION` — a deterministic replay of the same sealed instrument, commit, and
  frozen seeds, user-authorised per comité 016 — matched the transcription exactly on every field
  (`docs/prereg002_reverification_result.md`). This verifies the transcription, not the lost
  artifact; it is never presented as the original blind evaluation.

**Bounded claim (do not overstate):** the causal order and its counts — no coordinates accessible
to the estimator — localise the horizon-associated boundary *significantly and stably* in a 1+1D
Schwarzschild model within a **finite patch**. It does **not** claim metric reconstruction, the
global event horizon (future null infinity), 3+1D, Kerr, or manifoldlikeness.

**Post-R-VAR new-geometry result (2026-07-19):** a separate frozen contract on the square patch
`SQUARE_BOX_2P4` (`T=2.4`, `R=2.4`, aspect ratio `1.0`) found a scientific
`BH_MINK_DISPERSION_DIFFERENCE_DETECTED` terminal for the order-only future-observable dispersion
summaries `cv_L` and `cv_V` over minimal elements
(`docs/new_geometry_future_observables_addendum.md`). Coverage was 24/24 in every cell; at the
primary endpoint, `median(D_L)=0.4987114017481817`, `median(D_V)=0.47639013575705436`, and both
paired sign-flip p-values were `1.1920928955078125e-07`. This is a **new scientific question**:
it does not localise a horizon, does not reconstruct geometry, and does not repair or supersede
the previous R-VAR closure, which remains `CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]`.

## Program-level question

The deeper program is narrower and more defensible than a generic "geometry from order" slogan:

- How much continuous geometry, and in particular horizon-type structure, can be recovered from
  causal order plus counting?
- Are there geometric observables whose localisation is not arbitrarily refinable from finite
  discrete order-and-count data?

The current repo does **not** claim a universal no-go theorem or a new physical uncertainty
principle. What it does claim today is more limited:

- **Paper I / prereg-002:** an order-only estimator can recover a horizon-associated boundary in a
  controlled finite 1+1D setting.
- **PR-003 / prereg-003:** the sealed v2 estimator exhibits an **operational resolution floor** in
  that setting.

The open scientific question is whether such a floor is merely estimator-specific, or whether it
signals a deeper **order/geometry indetermination** for fine geometric localisation. "Uncertainty"
is therefore used here only as a working analogy for a possible intrinsic operational limit, not
as an established physical principle.

Everything below this point is post-Paper-I development material. It is exploratory/dev-only
context and is not part of the sealed Paper I result.

## Next phase — PR-003: from *localising* the boundary toward a candidate horizon portion

With localisation PASSed, the next goal changes the **object the estimator returns**: from "the
boundary is between these two positions" to an **ordered subset / band of causal-set elements** —
candidate horizon structure rather than a reconstruction claim. The immediate defensible target (a
finite patch cannot reach the global event horizon, which needs all of future null infinity) is an
**order-only, blind candidate for a local portion of the 1+1D Schwarzschild horizon**, subject to a
separate freeze. This follows Eichhorn–Gamito–Stokes (arXiv:2605.06813, Sec. V) — longest-chain
interior/exterior split → boundary → an **outgoing fuzzy ladder** tracing the horizon → a band built
by iterating over successive antichains. **Key advance vs EGS:** they *seeded and selected* the
horizon ladder using the embedding (their §V.B); ours must be **fully order-only and blind**, seeded
from the v2 bracket boundary, with any reconstruction claim deferred until a separate dev cycle and
freeze.

### What was explored today (2026-06-22, dev only; coords used *only* to score)

Compute engine decision: **Numba now** (fast iteration) → port the validated *integer* kernel to
**C++** at seal time with a bit-for-bit cross-check (the ladder search is integer-only, so it is
deterministic either way). Probes (committed as scoped `dev/` exceptions): `explore_ladders.py`,
`explore_direction.py`, `explore_seed_bracket.py`.

- **Feasibility — yes, in dev-only exploration.** Order-only **fuzzy ladders** (EGS Def. 2) of length
  ≥8 are *abundant* even in our modest box (`t_edge=6`, N≈3600) — ladder scarcity is **not** a
  blocker (EGS's pessimism was about rigid ladders). Kernel verified correct independently at N=147.
- **#2 direction (outgoing vs ingoing), order-only — promising, dev-only.** The exteriority field
  `φ = L_fut` (EGS interior/exterior diagnostic) carries direction: a relative-exteriority feature
  predicts true `sign(Δr)` with AUC **0.72–0.95** in aggregate. *Preliminary:* tiny samples; the
  **near-horizon band is still untested**. This is exploratory context, not Paper I evidence.
- **#3 bracket-seeding — directionally right, low yield.** Seeding from the order-only v2 bracket
  boundary concentrates ladders near the horizon (67–100% near-horizon), indicating the bracket is a
  usable order-only dev seed — but only 1–3 long ladders are harvested per sprinkling, and `d_⊥ =
  |r−r_S|` median ≈ 3–4 ℓ (near, not yet the O(ℓ) target). This remains dev-only, not Paper I
  evidence.
- **Engineering note:** the *recursive* Numba njit ladder kernel **SIGSEGVs on real BH-generator
  posets** (`t_edge=6`), even at stack depth ≈21–30; this was **not** reproduced on synthetic
  light-cone posets up to `lmax=300`, so the failure is **workload-dependent**, not a universal
  recursion-depth limit. Mechanism `[UNVERIFIED]` — symptom reproduced, Numba internals not pinned.
  The ladder builder was switched to an **iterative** (explicit-stack) form (the C++-portable shape).
  This is dev-only implementation context, not Paper I evidence.
- **Measurement (2026-06-23, dev): `lmax` censoring lifted at `t_edge=6`.** The earlier
  `maxlen == lmax == 30` was a cap artifact, not a real length. Sweeping `lmax` ∈ {30,40,60,80,120}
  (intensity=3600, M=3, 3 seeds): true longest-ladder lengths are **46–96+** and **seed-dependent**.
  The science counts `ge6`/`ge8` are **identical across every `lmax`/budget cell** — the "length-≥8
  ladders abundant" claim was never censored; only `maxlen` (and slightly `mean`) were. Raising `lmax`
  shifts the binding cap onto `per_start_budget`: only seed1 reached budget-insensitive **saturation
  ≈46**; seed0 (≥96, still climbing) and seed2 (≥72) stayed budget-bound, their highest-budget cells
  hitting the wall-clock cap, so those lengths are **lower bounds** (true saturation not yet
  established). Measurement only — `/tmp`, nothing frozen, and not Paper I evidence.

### What was explored (2026-06-23, dev only; coords used *only* to score)

Process: the **leakage gate** — the order-only contract every new PR-003 observable must pass — is
written and anchored to the existing executable guards (`docs/pr003_leakage_gate.md`). Two
deliberation/integrity skills (`/comite`, `/auditor`) added under `.claude/skills/`. Probes:
`measure_near_horizon.py`, `sweep_near_horizon_density.py` (bracket-seeded longest ladders,
order-only build).

- **#2 direction — a strong *global* signal, still dev-only.** Of the `L_fut`-field features,
  **`relphi_mean`** (mean relative-exteriority along the ladder) predicts true `sign(Δr)` with AUC
  **0.94–0.97**, stable across a **4× density sweep** (intensity 3600→7200→14400). The other
  features are weak. The specifically near-horizon validation is still limited to **1/6/2** positive
  (outgoing) cases, so #2 is **retained provisionally**, not yet definitively freezable. This is
  exploratory context, not Paper I evidence.
- **#3 selection "longest" — REJECTED as the selector of a horizon portion.** A density sweep splits
  the bracket-seeded longest ladder into head vs tail. The **head** (first-3 rungs) keeps `d_⊥/ℓ`
  bounded around ~2.5 (2.34→2.86→2.59, non-monotone, large IQRs) — **compatible with** localisation
  at discreteness precision (`d_⊥`=O(ℓ)); this does **not** by itself demonstrate convergence or a
  seed-coherent curve. The **tail** has `d_⊥/ℓ` **growing** (4.37→6.17→7.56), so the longest-selected
  ladder **fails the required discreteness-scale adherence** — it does not stay at O(ℓ). (This is
  *not* a claim of physical divergence: ℓ roughly halves over the sweep, so physical `d_⊥` may still
  be decreasing, only slower than O(ℓ); the scaling is undetermined with three densities.)
  **Structural finding:** horizon information concentrates in the head near the seed; later growth
  optimises *length*, not *adherence*. `NO_POST_HOC_TUNING` honoured: dev only, nothing frozen, not
  Paper I evidence.

### Plan for tomorrow (one precise question first — do NOT pre-design alternatives)

1. ✅ **ANSWERED (2026-06-24, exploratory, 6 seeds; `dev/measure_truncated_head.py`,
   `dev/PR003_NEAR_HORIZON_NOTES.md`).** *Does a head truncated by an order-only rule give a
   **connected** sequence that stays O(ℓ)?* Verdict **`BARE_RELOCALISATION`**. (a) A connected,
   geometrically adherent head **exists but is only the seed's discreteness neighbourhood**:
   connectedness 100% at every density, but (measured with the hidden `d_⊥`) `k*` = O(1) rungs
   (3/2/3, no growth) and its physical extent `k*·ℓ` **halves with ℓ** (0.134→0.067) — the
   prereg-002 floor at the seed, not a lengthening segment. `k*` is **not** an order-only rule (it
   is read off `d_⊥`). (b) The head end is **not stably detectable from order**: cumulative
   `rel_phi` shows no density-robust breakpoint aligned with `k*` (ambiguous/unstable). (c) Still
   unproven: any *extended/growing* horizon segment, and any order-only stopping rule; the greedy
   contrast was underpowered (n=2/8/1).
2. **Firm up #2 at the horizon:** scale seeds so the near-horizon band has enough outgoing ladders to
   measure the `relphi_mean` direction AUC *at* the horizon (today 1/6/2 positives), not just at the
   ~5 ℓ scale — a precondition for a definitive #2 freeze.
3. **Only then freeze** the two order-only rules (#2 `relphi_mean`, the corrected #3) — both must
   pass the leakage gate — via `/comite`, then seal. Until then it is an embedding-seedable
   proof-of-principle, not a blind reconstruction.
4. **Then draft the revisable PR-003 plan** with success criteria in frozen form: `d_⊥ ≲ k·ℓ`,
   temporal persistence, discrete continuity, transverse convergence with density, held-out
   stability, a flat control (no persistent curve), shifted controls (vary M ⇒ the reconstruction
   shifts without retuning), and a geometric (element-set) output.

The roadmap: **boundary localisation ✅ → horizon-portion construction → convergence under patch
extension → 3+1D.**

### Current state of the PR-003 track (2026-07-03)

The ladder plan above is **frozen, not abandoned** — on 2026-06-26/27 the track pivoted to first
closing an *intrinsic relational definition* of the horizon interface
(`docs/hoja_de_ruta_27_jun_2026.md`; prereg-003, the sealed estimator's operational resolution
floor, is separately frozen in `docs/preregistration_003.md`). The honest boundary today:

- **Defined (given `R`):** for a finite causal poset and a reference subset `R`, the relational
  interface `H[C;R]` — infalling cover links from `down(R)` into its complement — is rigorously
  defined and formalised (`formal/HorizonFormal/HorizonFormal/Horizon.lean`). The pre-2026-07-02
  orientation was provably empty for every `R` (tombstone theorem `relationalHorizonOld_eq_empty`);
  the corrected orientation carries an explicit non-emptiness witness and the structural one-way
  lemma `relationalBlackRegion_no_escape` (no causal relation leaves the black-region candidate).
- **Open:** selecting `R(C)` from the causal order and its counts in a closed, robust, physically
  discriminating way. The only written draft rule, `R = Max(C)`, provably trivialises on finite
  posets (`NO_INTERFACE`; `nachocausal/c1_selector.py`, `dev/PR003_C1_RELATIONAL_SPEC.md` §8-9).
  The interface does not discover the horizon; it delimits what a (still missing) selector already
  declared unable to escape. No order-only horizon reconstruction is claimed.

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

### Optional Lean formalisation track

The order-theoretic formalisation lives under `formal/HorizonFormal/`. It is independent of the
sealed Python validation path and uses Lean 4 + mathlib via Lake. The reproducible dependency
pins are committed in `formal/HorizonFormal/lean-toolchain`, `formal/HorizonFormal/lakefile.toml`,
and `formal/HorizonFormal/lake-manifest.json`; `.lake/` build artifacts are intentionally ignored.

```bash
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | \
  sh -s -- -y --default-toolchain leanprover/lean4:v4.31.0
. "$HOME/.elan/env"

cd formal/HorizonFormal
lake update
lake build
```

The optional Minz admissibility cross-check (`make gate`) is **not** on the validation path and
**not** required to run the benchmark. It needs the external clone
[c-minz/Python-causets](https://github.com/c-minz/Python-causets) on `sys.path` via the env var
`NACHOCAUSAL_MINZ_PATH` (default `~/cs-horizon-reuse-check`). Its evidence is already recorded in
`nachocausal/fixtures/gate_evidence.json`.

## In-repo tooling — the `/comite`, `/auditor`, and `/alloy-verifier` skills

Two Claude Code skills live in `.claude/skills/` and travel with the repo, so any clone on any
machine has them with **no install step** — Claude Code auto-discovers project skills under
`.claude/skills/`. They encode this project's discipline as runnable guardrails: the committee is
**forward-looking** (deliberate before a one-way step), the auditor is **backward-looking** (verify
that what is already claimed is real), and Alloy is a **bounded formal verifier** that only enters
after a claim has been translated into a checkable finite model.

```bash
git clone https://github.com/nacho09021973/nachocausal
cd nachocausal
# open Claude Code here — both skills are picked up automatically
```

### `/comite <decision question>` — standing deliberation committee
A 7-role, two-wave **blind** expert panel (reproducibility engineer, causal-set mathematician,
mathematical logician, Schwarzschild physicist, falsifier, pre-registration warden, literature
verifier) chaired into a grounded, freeze-checked **decision brief** the user signs off on. The
committee *proposes*; the user *authorises* — it never launches the blind validation run, commits,
loosens a frozen threshold, or makes a reconstruction claim. Convene it for any one-way /
scientifically committing step (above all the blind validation run) or a frontier decision; also
via "convoca al comité".
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

### `/alloy-verifier <claim/model question>` — bounded model checker
This verifier enters **only** when a claim has already been translated into an explicit finite
relational model. It is not a committee, not an auditor, and not a theorem prover. Its job is to
run a bounded Alloy check against a stated model, target, and scope, then write a verification note
with a narrow verdict. If the model is not yet explicit, or if no verified Alloy executable exists,
it fails closed.
- Writes `docs/alloy/alloy_verification_NNN_<slug>.md`.
- Repo convention: committed/rerunnable models under `formal/alloy/`, exploratory models under
  `dev/alloy/`, verification notes under `docs/alloy/`.
- See `docs/ALLOY_VERIFICATION.md` for the entry condition and claim boundary.

## External advisory consultors

The repo can also prepare **advisory-only** external consultations through
wrappers that live outside the repository. These are reversible support tools,
not part of the sealed validation path and not evidence by themselves.

- DeepMath pattern: `docs/DEEPMATH_CONSULTING.md`
- NVIDIA pattern: `docs/NVIDIA_CONSULTING.md`

For `nachocausal`, archived consultation artefacts default to `dev/consultations/`
so they remain clearly outside the sealed/results path.

## Literature library

An extensive local library of causal-set-theory articles and books lives in `biblioteca/`
(papers by Bombelli, Sorkin, Benincasa, Dowker, Surya et al.; textbooks; and the directly
relevant "Towards black-hole horizons and geodesic focusing in causal sets"). It also holds
markdown notes and PDF-derived markdown under `biblioteca/derived-md/`. The folder is local
reference material only — it is git-ignored and not part of the committed project.
