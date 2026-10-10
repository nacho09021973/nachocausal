---
tipo: sanedrín — deliberación adversarial multi-modelo
fecha: 2026-09-11 19:22
proyecto: /home/adnac/nachocausal
tema: (tema en línea de órdenes)
rondas: 4
reglas: /home/adnac/sanedrin/reglas/codigo.md
miembros:
  - FABLE — Claude (Anthropic) — claude -p
  - ASTRA — GPT (OpenAI) — codex exec
  - CIRO — Grok (xAI) — grok -p
ausentes:
  - ABNER — DeepSeek — backend no disponible
conductor: sanedrin — sin intervención humana entre turnos
---

## Tema sometido al sanedrín

¿Cómo debería continuar nachocausal a partir del estado actual del repositorio? Debéis producir una recomendación operativa y priorizada, respetando estrictamente los contratos congelados, la separación exploración/confirmación, las preguntas abiertas y los límites de las afirmaciones. Evaluad qué trabajo debe hacerse a continuación, qué debe evitarse, qué artefacto mínimo verificable debe cerrarse primero y bajo qué criterio se autorizaría el siguiente salto hacia Schwarzschild 3+1D. Distinguid hechos documentados del repositorio, inferencias y propuestas.

## Contexto

### Contexto adjunto: README.md
```
# nachocausal

Recovering black-hole horizon structure from causal-set **order and counting** (the theory's
*Order + Number* data) — framed as a *recoverability* benchmark, not a reconstruction claim.

> **Note on "order-only".** Throughout this README `order-only` means **blind to the
> embedding** — no coordinates, no ground truth reach the estimator. It does **not** mean
> "without counting": cardinalities are legitimate observables. See `CLAUDE.md`.

For any AI or agent connecting to this repo, read [INSTRUCCIONES.md](INSTRUCCIONES.md) first for
the available machinery and the correct workflow between committee, auditor, external consultors,
and Alloy.

**Current program roadmap:** [September 2026 checkpoint](docs/hoja_de_ruta_septiembre_2026.md).
The [post-N1–N5 limits-paper route](tarea_grok_2.md), the
[15 July operational plan](docs/plan_operativo_15_julio_2026.md), and the
[original horizon roadmap](docs/roadmap.md) remain historical input where not superseded by that
checkpoint.

## Current theory result — Fisher efficiency of unlabeled 2D posets

The rank-to-poset branch now contains a finite-\(N\) theorem for the exact
channel

\[
\Pi_N\longmapsto[P_{\Pi_N}],
\]

where `Pi_N` is uniform on `S_N` and `[P_Pi_N]` is the isomorphism class of the
induced oriented two-dimensional poset. For symmetric separable scores

\[
S_N(\pi)=2\sum_{i=1}^N a_{i,N}a_{\pi(i)},
\]

assume

\[
\sup_N\max_i|a_{i,N}|<\infty,
\qquad
\sum_i a_{i,N}=0,
\qquad
\frac1N\sum_i a_{i,N}^2\longrightarrow c>0.
\]

Writing

\[
I_N^\Pi=\mathbb E[S_N(\Pi_N)^2],
\qquad
I_N^{[P]}=
\mathbb E\!\left[\mathbb E[S_N(\Pi_N)\mid[P_{\Pi_N}]]^2\right],
\]

the proved result is

\[
\boxed{
1-\frac{I_N^{[P]}}{I_N^\Pi}=O(N^{-1/2}),
\qquad
\frac{I_N^{[P]}}{I_N^\Pi}\longrightarrow1.
}
\]

The argument does not require asymptotic uniqueness of the permutation
representation. It combines exact zero conditional variance on the typical
prime-root/leaf-or-twin sector, an `O(N^{-1})` exceptional-event probability,
and the explicit uniform fourth-moment bound

\[
\mathbb E[S_N(\Pi_N)^4]\le240N^2M^8.
\]

For the frozen sinusoidal tangent
\(a_{i,N}=\mathbb E[\sin(2\pi U_{(i)})]\), one has \(c=1/2\), hence

\[
I_N^\Pi=N+o(N),
\qquad
I_N^{[P]}=N-o(N).
\]

The complete definitions, finite falsifiers, source transport and proofs are in
[`research_program/work_packages/wp6_d2_modular_fiber_score.md`](research_program/work_packages/wp6_d2_modular_fiber_score.md).
The priority audit has passed only provisionally: the narrow theorem is
potentially new, while the general framework of asymptotically sufficient
quantizations is not claimed as new. No universality claim is made.

The geometric branch is also closed through S2. S1 classifies exactly the
symmetric rank-one conformal tangents on a fixed Minkowski null diamond, and
S2 assembles that classification with the theorem above to prove relative
Fisher retention for the same channel. S1/S2 are now frozen as a
**structural tool**: they make no horizon claim and do not automatically
transport to the sealed Schwarzschild benchmark. The physical re-entry audit
finds exact transport only for the product-order/rank-permutation skeleton at
fixed cardinality. The point experiment is now proved non-QMD, which rules out
a common parameter-independent statistical isomorphism to the regular S1/S2
experiment. The remaining `DOMAIN_BRIDGE` question is regularity after the
finite rank/permutation or unlabeled-poset channel; it is open and not
authorized. See
[`wp6_d2_geometric_tangent_classification.md`](research_program/work_packages/wp6_d2_geometric_tangent_classification.md),
[`wp6_d2_geometric_fisher_retention.md`](research_program/work_packages/wp6_d2_geometric_fisher_retention.md),
and the [physical re-entry audit](docs/physical_reentry_audit_001_2026-08-28.md).

```text
FAMILY_FROZEN
FINITE_N_POSET_LOSS_PROVED
TYPICAL_FIBER_ZERO_LOSS = PROVED
ASYMPTOTIC_POSET_FISHER_EFFICIENCY_FOR_BOUNDED_SEPARABLE_SCORES = PROVED
THEOREM_PROVED_PRIORITY_AUDIT_PASSED_PROVISIONALLY
POTENTIALLY_NOVEL_THEOREM_NOT_NOVEL_FRAMEWORK
NO_UNIVERSALITY_CLAIM
GEOMETRIC_TANGENT_CLASSIFICATION = PROVED
S2_GEOMETRIC_FISHER_RETENTION = PROVED_BY_ASSEMBLY
STOP_AFTER_S2 = SI
FISHER_BRANCH_ROLE = STRUCTURAL_TOOL
PHYSICAL_REENTRY = PARTIAL_TRANSPORT_WITH_POINT_QMD_OBSTRUCTION_PROVED
COMMON_POINT_ISOMORPHISM = REFUTED
MOVING_SUPPORT_QMD_STATUS = PROVED_NON_QMD_FOR_POINT_EXPERIMENT
FINITE_CHANNEL_REGULARITY = OPEN
DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL
NEXT_RUN_AUTHORIZED = NO
TARGET_SUBCLASS = SYMMETRIC_RANK_ONE_COPULA_TANGENTS
GENERIC_BILINEAR_SEPARABLE_EXTENSION = OPEN_NOT_ASSUMED
RATE_IMPROVEMENT = DEFERRED
PRIORITY = PROVISIONAL_NOT_SEALED
```

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

The sealed numeric core is **pure numpy**. The canonical repository validation path
also imports the test-suite support packages pinned in `requirements.txt`. Anyone can
reproduce everything under identical conditions with just this repo and that
environment:

```bash
git clone https://github.com/nacho09021973/nachocausal
cd nachocausal
python3 -m venv .venv && . .venv/bin/activate     # Python 3.12 (sealed: 3.12.3)
pip install -r requirements.txt                    # pinned canonical test/audit environment

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
```

### Contexto adjunto: INSTRUCCIONES.md
```
# INSTRUCCIONES.md

Guía operativa para cualquier IA o agente que se conecte a `nachocausal`.

Este documento no sustituye a `CLAUDE.md`, `README.md` ni a la pre-registración
congelada. Su función es explicar, de forma directa, **qué maquinaria existe en
el repo** y **cuál es el flujo correcto de uso**.

## 1. Qué es este repo

`nachocausal` es un **benchmark de recoverability**, no una reclamación libre de
reconstrucción. El proyecto trabaja con una disciplina estricta:

- exploración (`dev/`) y confirmación (`results/`, docs congeladas) están separadas;
- los umbrales congelados no se tocan sin nueva pre-registración;
- la embedding oculta solo puntúa, no define el observable;
- ninguna IA debe sobredeclarar resultados.

Antes de actuar, lee como mínimo:

1. `CLAUDE.md`
2. `README.md`
3. `docs/preregistration.md`
4. este `INSTRUCCIONES.md`

## 2. Maquinaria disponible

### A. `/comite` — deliberación científica

Uso correcto:

- decisiones de frontera;
- pasos científicamente comprometidos;
- promoción de una idea a claim, spec o plan de trabajo serio;
- preguntas del tipo "¿debemos proceder?".

Qué hace:

- convoca un comité con varios roles y subagentes;
- produce un brief en `docs/comite/`;
- propone, pero no ejecuta pasos irreversibles.

No usar para:

- tareas triviales;
- comprobar si un número ya publicado es real;
- ejecutar código o cambiar umbrales.

### B. `/auditor` — auditoría de integridad

Uso correcto:

- antes de construir sobre resultados ya reclamados;
- para verificar que números, sellos y separación dev/validation son reales;
- para revisar si una afirmación ya escrita está respaldada.

Qué hace:

- ejecuta comprobaciones mecánicas;
- revisa sellos y claims;
- escribe un informe en `docs/auditor/`.

No usar para:

- decidir una línea científica futura;
- arreglar el repo por su cuenta.

### C. Deep externo — consultor advisory-only

Contrato:

- vive **fuera** del repo;
- ubicación esperada: `~/ai/deepmath/`;
- adaptador del repo: `scripts/consulting/deepmath_consult.py`;
- documentación: `docs/DEEPMATH_CONSULTING.md`;
- artefactos: `dev/consultations/deepmath/`.

Uso correcto:

- consulta externa no vinculante;
- apoyo conceptual o matemático;
- preparación de dossier con trazabilidad.

Límite:

- no cuenta como evidencia científica;
- no toca el path sellado;
- si falta el comando, debe fallar cerrado.

### D. NVIDIA externo — consultor advisory-only

Contrato:

- vive **fuera** del repo;
- ubicación esperada: `~/ai/nvidia-consult/`;
- adaptador del repo: `scripts/consulting/nvidia_consult.py`;
- documentación: `docs/NVIDIA_CONSULTING.md`;
- artefactos: `dev/consultations/nvidia/`.

Uso correcto:

- consulta externa no vinculante;
- apoyo de razonamiento o redacción técnica;
- mismo patrón de dossier + manifest + response.

Límite:

- no cuenta como evidencia;
- no guarda claves dentro del repo;
- si falta `NVIDIA_API_KEY` o el comando, debe fallar cerrado.

### E. `/alloy-verifier` — verificación formal acotada

Uso correcto:

- solo cuando una afirmación ya se ha traducido a un **modelo finito y relacional verificable**;
- para buscar contraejemplos o comprobar un `check`/`run` a alcance finito.

Contrato:

- modelos canónicos: `formal/alloy/`
- modelos exploratorios: `dev/alloy/`
- informes: `docs/alloy/`
- skill local: `.claude/skills/alloy_verifier/`
- documentación: `docs/ALLOY_VERIFICATION.md`

Límite:

- Alloy **no prueba** el claim físico general;
- Alloy solo da evidencia sobre el modelo codificado y el alcance finito;
- si no hay comando Alloy verificado, debe fallar cerrado.

## 3. Qué es canónico y qué no

Canónico:

- skills bajo `.claude/skills/`;
- documentación en `docs/`;
- modelos Alloy serios en `formal/alloy/`;
- notas de trabajo en `dev/`;
- consultorías externas archivadas en `dev/consultations/`.

No canónico por defecto:

- archivos `.als` sueltos en la raíz;
- pruebas rápidas;
- material temporal;
- cualquier salida no enlazada por docs o por una nota de verificación.

Si un modelo Alloy importa de verdad, promuévelo a `formal/alloy/` y crea su
nota en `docs/alloy/`.

## 4. Flujo correcto de uso

### Flujo 1 — decisión científica seria

1. leer contexto y reglas;
2. si la decisión construye sobre resultados ya reclamados, pasar primero por `/auditor`;
3. convocar `/comite`;
4. ejecutar solo pasos reversibles si el usuario lo pide;
5. no commit, no push, no validación sellada sin autorización explícita.

### Flujo 2 — consulta externa de apoyo

1. redactar la pregunta con alcance estrecho;
2. adjuntar contexto relevante;
3. usar Deep o NVIDIA a través de `scripts/consulting/`;
4. guardar dossier, manifest y response en `dev/consultations/...`;
5. tratar la respuesta como **advisory-only**;
6. si afecta a una decisión científica, llevarla luego a una nota `dev/` o al `/comite`.

### Flujo 3 — verificación Alloy

1. comprobar que el claim ya está traducido a un modelo finito;
2. verificar el comando Alloy local;
3. ejecutar `/alloy-verifier` o el comando equivalente;
4. guardar el informe en `docs/alloy/`;
5. explicitar siempre:
   - modelo;
   - comando;
   - alcance;
   - resultado;
   - límites de interpretación.

### Flujo 4 — desarrollo normal en `dev/`

1. trabajar en `dev/` cuando la idea aún no está cerrada;
2. no tocar umbrales congelados;
3. no reetiquetar exploración como evidencia;
4. si aparece una objeción lógica seria, se puede:
   - formalizar en Alloy;
   - elevar al comité;
   - o convertir en nota de trabajo explícita.

## 5. Orden recomendado entre herramientas

Regla simple:

- **¿es una decisión?** -> `/comite`
- **¿es una verificación de algo ya afirmado?** -> `/auditor`
- **¿es una consulta externa no vinculante?** -> Deep o NVIDIA
- **¿es una afirmación ya formalizada en un modelo finito?** -> `/alloy-verifier`

Orden típico sano:

1. nota `dev/`
2. Deep/NVIDIA si hace falta apoyo externo
3. Alloy si ya hay traducción formal
4. `/comite` para decidir
5. `/auditor` si se va a construir sobre claims ya publicados o a consolidar

No todo paso necesita todas las herramientas. Lo importante es **no saltarse la
disciplina**.

## 6. Reglas negativas

No hacer:

- commits o push sin autorización explícita del usuario;
- cambios de umbrales congelados;
- uso de resultados de validación como si fueran datos de exploración;
- presentar Deep, NVIDIA o Alloy como prueba física concluyente;
- confundir un contraejemplo lógico con un no-go físico completo;
- meter modelos, wrappers o claves dentro del repo si deben vivir fuera.

## 7. Estado conceptual actual de Alloy

En este momento, Alloy sirve como capa formal **lógica/combinatoria**.

Lectura correcta:

```text
logical counterexample != physical no-go
```

pero también:

```text
logical counterexample => the obstruction is not empty rhetoric
```

Así que Alloy puede apoyar una objeción formal acotada, pero no certificar por
sí solo embedding fiel, manifold-likeness, Poisson típico, curvatura, ni
convergencia al continuo.

## 8. Si eres una IA nueva en este repo

Haz esto primero:

1. lee `CLAUDE.md`;
2. lee `README.md`;
3. lee este archivo;
4. identifica si tu tarea es:
   - deliberación,
   - auditoría,
   - consulta externa,
   - verificación Alloy,
   - o trabajo exploratorio normal;
5. usa la herramienta mínima correcta;
6. deja trazabilidad;
7. no sobredeclares.
```

### Contexto adjunto: docs/hoja_de_ruta_septiembre_2026.md
```
# Hoja de ruta — septiembre de 2026 · de eficiencia combinatoria a tangentes geométricas

> **Plan REVISABLE, no congelado.** No es una pre-registración, no autoriza
> simulaciones, nuevos observables, consumo de semillas, cambios en instrumentos
> sellados ni extrapolaciones dimensionales. Su función es fijar el orden lógico
> de la nueva rama de información Fisher y evitar que vuelvan a abrirse frentes
> antes de cerrar el puente geométrico. Mantener `FAMILY_FROZEN`,
> `NO_UNIVERSALITY_CLAIM` y `PRIORITY = PROVISIONAL_NOT_SEALED`.

## Checkpoint histórico — 2026-08-28

Las fases S1 y S2 que el plan inferior describía como futuras ya están
cerradas. Este checkpoint se conserva como registro de planificación y del
estado que regía el 2026-08-28, pero queda `SUPERSEDED` para los cierres
autoritativos posteriores registrados más abajo. No constituye autorización
para reabrir S3–S7. Su estado histórico era:

```text
GEOMETRIC_TANGENT_CLASSIFICATION = PROVED
S2_GEOMETRIC_FISHER_RETENTION = PROVED_BY_ASSEMBLY
STOP_AFTER_S2 = SI
S3_NOT_OPENED
S4_NOT_OPENED  [HISTORICAL_AT_2026-08-28; SUPERSEDED]
NO_HORIZON_CLAIM
NO_PRIORITY_CLAIM
FISHER_BRANCH_ROLE = STRUCTURAL_TOOL

PHYSICAL_REENTRY = PARTIAL_TRANSPORT_WITH_POINT_QMD_OBSTRUCTION_PROVED
COMMON_POINT_ISOMORPHISM = REFUTED
MOVING_SUPPORT_QMD_STATUS = PROVED_NON_QMD_FOR_POINT_EXPERIMENT
FINITE_CHANNEL_REGULARITY = OPEN
DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL
NEXT_RUN_AUTHORIZED = NO
```

La auditoría autoritativa de reingreso es
`docs/physical_reentry_audit_001_2026-08-28.md`. La decisión acotada del PI y
la obstrucción negativa del puente puntual están registrados respectivamente en
`docs/program_domain_bridge_authorization_2026-08-28.md` y
`research_program/work_packages/wp6_domain_bridge_fixed_ef_box.md`. La prueba
completa la velocidad normal, la cota de área de la diferencia simétrica y la
cota inferior de densidad. No permite inferir no-QMD para la ley después del
canal finito; `FINITE_CHANNEL_REGULARITY` y el residuo de `DOMAIN_BRIDGE`
siguen abiertos y no autorizados.

```text
GOBERNANZA: docs/program_reopening_note_2026-08-28_R4.md (firmada 2026-08-28)
G2: §2.2 enmendada a Convención B el 2026-08-28
    (lambda parametriza P psi, no el tangente de copula)
PLAN_INFERIOR: REGISTRO_HISTORICO_DE_SECUENCIACION
```

## Estado autoritativo actual — HEAD `b5e8705` (2026-08-31)

Este bloque manda sobre los estados históricos incompatibles del checkpoint
de 2026-08-28 y de la secuencia de planificación preservada en §§0–14. No
reabre fases ni modifica la gobernanza científica.

```text
RELATIVE_FISHER_OPERATOR_IDENTIFICATION = PROVED
RELATIVE_OPERATOR_FINITE_N_PROJECTION = REFUTED
RELATIVE_OPERATOR_SOT_LIMIT = P_SYM_PROVED
RELATIVE_ASYMPTOTIC_IDEMPOTENCE_SOT = PROVED
RELATIVE_OPERATOR_NORM_CONVERGENCE = REFUTED
GARBLING_N_PLUS_1_TO_N = PROVED_BY_UNIFORM_DELETION
FULL_SYMMETRIC_HS_RETENTION = PROVED
MIXED_SECTOR_LIMIT = PROVED_NORM_RATIO
HIGHER_ORDER_IDENTIFIABILITY_IN_ABS_EPSILON = PROVED_SECOND_ORDER_VISIBLE
ONE_SIDED_QMD_IN_THETA = PROVED
GEOMETRIC_REALIZABILITY_OF_ARBITRARY_HS = OPEN
NEXT_RUN_AUTHORIZED = NO
```

## 0. Punto de partida preservado

Rama de trabajo:

```text
emergencia/p1a-canal-sigma-m
```

Commits de preservación de entrada:

```text
236b1824d86ad3c169e574bf263ecde40310eb04
  prove asymptotic Fisher efficiency for unlabeled 2D posets

4bcbfc50a95ddb7af52bfa002974016b9eafbd43
  document unlabeled 2D poset Fisher theorem
```

Anclas obligatorias antes de trabajar:

1. `research_program/work_packages/wp6_d2_modular_fiber_score.md`;
2. `research_program/work_packages/wp6_d2_null_copula_dichotomy.md`;
3. `README.md`, sección “Current theory result — Fisher efficiency of
   unlabeled 2D posets”.

Estado científico de entrada:

```text
FAMILY_FROZEN
FINITE_N_POSET_LOSS_PROVED
TYPICAL_FIBER_ZERO_LOSS = PROVED
ASYMPTOTIC_POSET_FISHER_EFFICIENCY_FOR_BOUNDED_SEPARABLE_SCORES = PROVED
THEOREM_PROVED_PRIORITY_AUDIT_PASSED_PROVISIONALLY
POTENTIALLY_NOVEL_THEOREM_NOT_NOVEL_FRAMEWORK
NO_UNIVERSALITY_CLAIM
NEXT_TARGET = GEOMETRIC_TANGENT_CLASSIFICATION
TARGET_SUBCLASS = SYMMETRIC_RANK_ONE_COPULA_TANGENTS
GENERIC_BILINEAR_SEPARABLE_EXTENSION = OPEN_NOT_ASSUMED
RATE_IMPROVEMENT = DEFERRED
PRIORITY = PROVISIONAL_NOT_SEALED
```

El teorema autónomo ya demostrado usa una permutación uniforme `Pi_N`, el
canal exacto

\[
\Pi_N\longmapsto[P_{\Pi_N}],
\]

y scores simétricos separables

\[
S_N(\pi)=2\sum_{i=1}^N a_{i,N}a_{\pi(i)}.
\]

Si los perfiles son uniformemente acotados, centrados y tienen energía no
degenerada, entonces

\[
1-\frac{I_N^{[P]}}{I_N^\Pi}=O(N^{-1/2}),
\qquad
\frac{I_N^{[P]}}{I_N^\Pi}\longrightarrow1.
\]

Este resultado no se reabre en septiembre salvo contradicción matemática
explícita.

## 1. Norte único de septiembre

El único frente científico autorizado al comenzar el mes es

```text
GEOMETRIC_TANGENT_CLASSIFICATION
```

La pregunta es:

> ¿Qué perturbaciones conformes de un diamante causal (1+1) inducen, tras
> normalizar la medida y eliminar las marginales, un tangente de cópula
> simétrico rank-one cuyo score de rangos pertenece exactamente a la clase del
> teorema ya probado?

La secuencia vinculante es

\[
\boxed{
\text{teorema combinatorio ya probado}
\longrightarrow
\text{clasificación del tangente geométrico}
\longrightarrow
\text{teorema geometría }1+1\to\text{causet}
\longrightarrow
\text{auditoría final de prioridad}.
}
\]

No se abre el siguiente eslabón hasta cerrar o refutar el anterior.

## 2. Fase S1 — cerrar el puente geométrico

### 2.1 Objeto congelado

Partir de una perturbación conforme

\[
g_\varepsilon
=\frac{e^{2\varepsilon\psi(u,v)}}{Z(\varepsilon)}g_0
\]

en un diamante (1+1), con dominio, medida de referencia y condicionamiento en
`N` fijados antes de cualquier generalización.

Debe derivarse desde la medida normalizada, no postularse, el tangente de
cópula obtenido al retirar las dos marginales:

\[
\boxed{
h_\psi(u,v)
=2\,[\psi(u,v)-\psi_U(u)-\psi_V(v)+\bar\psi].
}
\]

Aquí deben definirse explícitamente `psi_U`, `psi_V`, `bar psi`, la constante
`Z(epsilon)` y el sentido de la derivada. No se permite esconder términos de
normalización dentro de una proporcionalidad informal.

### 2.2 Subclase objetivo

Caracterizar exactamente cuándo

\[
\psi(u,v)-\psi_U(u)-\psi_V(v)+\bar\psi
=\lambda f(u)f(v),
\qquad\text{equivalentemente}\qquad
h_\psi(u,v)=2\lambda f(u)f(v),
\]

con

\[
f\ \text{suave},
\qquad
\int_0^1 f(u)\,du=0,
\qquad
\int_0^1 f(u)^2\,du>0,
\]

y con las condiciones de acotación necesarias para aplicar el teorema de
scores separables.

**Convención B (G2, 2026-08-28).** El símbolo `lambda` parametriza la
proyección geométrica `P psi`, no el tangente de cópula. El factor `2` de
`h_psi=2 P psi` queda explícito, y el score de §2.3 usa el mismo `lambda`
en todas las etapas. (La Convención A, `h_psi=lambda f f`, queda
retirada de este §2.2.)

El objetivo no es clasificar todas las perturbaciones conformes. Es identificar
una subclase geométrica explícita, no vacía y estable bajo las equivalencias
marginales pertinentes.

### 2.3 Obligaciones de prueba

1. Derivar el score de la muestra condicionada a `N`.
2. Derivar el score condicionado a la permutación de rangos.
3. Probar que, en la subclase rank-one simétrica,
   \[
   S_N(\pi)=2\lambda\sum_i a_{i,N}a_{\pi(i)},
   \qquad
   a_{i,N}=\mathbb E[f(U_{(i)})],
   \]
   con cualquier convención de escala registrada de forma consistente.
4. Verificar, sin simulación:
   \[
   \sup_{N,i}|a_{i,N}|<\infty,
   \qquad
   \sum_i a_{i,N}=0,
   \qquad
   \frac1N\sum_i a_{i,N}^2\longrightarrow\int_0^1 f(u)^2\,du>0.
   \]
5. Distinguir el tangente geométrico, el tangente de densidad, el tangente de
   cópula y el score de rangos. No identificarlos mediante notación ambigua.

### 2.4 Falsificadores obligatorios

- Una perturbación puramente marginal
  `psi(u,v)=alpha(u)+beta(v)+const` debe desaparecer tras la proyección de
  marginales.
- Debe verificarse el factor `2`, el signo y el término `bar psi` mediante una
  diferenciación independiente.
- Debe exhibirse al menos una `psi` no sinusoidal dentro de la clase o demostrar
  que la clase geométrica se reduce más de lo previsto.
- Si un producto genérico `f(u)g(v)` con `f != g` aparece, no se promoverá al
  teorema simétrico: quedará fuera de alcance.

### 2.5 Veredictos permitidos

```text
GEOMETRIC_TANGENT_CLASSIFICATION = PROVED
GEOMETRIC_TANGENT_CLASSIFICATION = REFUTED
GEOMETRIC_TANGENT_CLASSIFICATION = OPEN_WITH_EXACT_OBLIGATION
```

`OPEN` sólo es admisible con una proposición concreta pendiente. Un ejemplo
numérico o una expansión formal sin control del resto no cierra la fase.

## 3. Fase S2 — primer teorema completo geometría a causet

Esta fase sólo se abre si S1 termina `PROVED`.

### 3.1 Enunciado objetivo

Para la clase explícita de deformaciones conformes rank-one simétricas obtenida
en S1, demostrar

\[
\boxed{
\frac{I_N^{[P]}(g_\varepsilon)}
     {I_N^\Pi(g_\varepsilon)}
\longrightarrow1.
}
\]

La notación debe especificar:

- familia geométrica y parámetro local;
- diamante (1+1) y coordenadas normalizadas;
- condicionamiento a cardinalidad fija `N`;
- representación observada antes del cociente;
- poset orientado no etiquetado observado después del cociente;
- score y punto nulo donde se calcula Fisher;
- clase exacta de `psi` o de `f`.

### 3.2 Claim ceiling

El resultado permitido será:

> En una clase explícita de deformaciones conformes simétricas rank-one de un
> diamante (1+1), el poset no etiquetado retiene asintóticamente toda la
> información Fisher relativa disponible en la permutación de rangos.

No estará permitido inferir:

- suficiencia respecto de las coordenadas continuas completas;
- reconstrucción de la métrica;
- universalidad para todo tangente geométrico;
- una afirmación sobre horizontes;
- una afirmación en (2+1) o (3+1);
- suficiencia absoluta sin especificar el experimento comparado.

### 3.3 Entregable

Un teorema autónomo con prueba modular en cuatro pasos:

1. geometría `->` tangente de cópula;
2. tangente de cópula `->` score de rangos simétrico;
3. score simétrico `->` teorema combinatorio ya probado;
4. conclusión Fisher para el canal `Pi_N -> [P_Pi_N]`.

No duplicar en esta fase las pruebas del cuarto momento ni de la fibra típica;
citarlas con hipótesis verificadas una por una.

## 4. Fase S3 — auditoría final de prioridad geométrica

Esta fase sólo se abre cuando exista un enunciado geométrico completo y estable.
La auditoría provisional del teorema combinatorio no sustituye esta revisión.

### 4.1 Pregunta adversarial exacta

> ¿Existe una fuente previa que demuestre suficiencia asintótica (L^2) o
> Fisher del poset bidimensional no etiquetado respecto de la permutación de
> rangos para tangentes procedentes de deformaciones geométricas conformes de
> la clase S1?

No basta encontrar antecedentes sobre:

- suficiencia asintótica de cuantizaciones en general;
- estadística clásica de rangos;
- cópulas, permutons o frecuencias de patrones antes del cociente;
- rigidez o unicidad de órdenes aleatorios bidimensionales;
- pérdida de etiquetas en grafos mediante entropía o mutual information.

### 4.2 Salidas permitidas

```text
DIRECT_PRIOR_FOUND
PRECURSOR_ONLY
SURVIVES_NARROWLY
INCONCLUSIVE_ACCESS_OR_SCOPE
```

Aunque el resultado sobreviva, el wording máximo seguirá siendo:

> We are not aware of previous results establishing the stated asymptotic
> Fisher-retention theorem for this exact geometric-to-unlabeled-poset channel.

No usar `first`, `novelty certified`, `breakthrough` ni equivalentes.

## 5. Fase S4 — generalización simétrica controlada en (1+1)

Esta fase no pertenece al objetivo inicial de septiembre. Sólo puede diseñarse
si S1–S3 están cerradas y documentadas.

La observación estructural de partida es que la fibra típica es

\[
\{\pi,\pi^{-1}\}.
\]

Por ello, para

\[
S_H(\pi)=\sum_i H_{i,\pi(i)},
\]

la condición

\[
H=H^{\mathsf T}
\]

hace al score invariante bajo inversión. El primer candidato de extensión es
una clase de rango finito

\[
H_N=\sum_{r=1}^R
\lambda_r a^{(r)}a^{(r)\mathsf T}.
\]

Esto es una **ruta candidata**, no un corolario ya demostrado. Antes de
promoverla habrá que cerrar de nuevo:

1. escala no degenerada de `I_N^Pi`;
2. cota de cuarto momento uniforme para el score matricial;
3. dependencia admisible de `R`, `lambda_r` y las normas de los perfiles;
4. clase geométrica que produce esos kernels simétricos.

```text
FINITE_RANK_BOUNDED_CONTINUOUS_SYMMETRIC_RETENTION = PROVED_BY_ASSEMBLY
FINITE_RANK_SYMMETRIC_RETENTION = PROVED
INFINITE_RANK_SYMMETRIC_RETENTION = PROVED
```

### 5.1 Preflight autorizado — rango finito simétrico (2026-08-29)

Este preflight no depende del `PASS` externo de Bombelli ni modifica el estado
bibliográfico. Tampoco abre kernels de rango infinito. Reconstruye literalmente
S2 desde el Teorema 5 de `wp6_d2_modular_fiber_score.md`, los Teoremas 6--7 y
los Lemas 11.1--11.2 de
`wp6_d2_geometric_tangent_classification.md`, y el Teorema 8 de
`wp6_d2_geometric_fisher_retention.md`.

#### Datos de S2 reconstruidos

Para un perfil `a in C[0,1]`, centrado y no nulo, escribiendo

\[
a_{i,N}:=\mathbb E[a(U_{(i)})],
\qquad
X_N(a):=\sum_i a_{i,N}a_{\Pi_N(i),N},
\tag{5.1}
\]

el score geométrico rank-one, con la Convención B, es

\[
S_N(a)=2\lambda X_N(a).
\tag{5.2}
\]

S2 prueba, para `lambda != 0`,

\[
0\le 1-\frac{I_N^{[P]}(a)}{I_N^\Pi(a)}
\le
\left(
\frac{\sqrt{240C_A}\,\|a\|_\infty^4}
{4\left(\int_0^1a^2\right)^2}+o(1)
\right)N^{-1/2}.
\tag{5.3}
\]

Aquí `C_A,N_A` proceden de `Pr(B_N)<=C_A/N`; la constante no depende de
`lambda`. Las hipótesis reales sobre el perfil son continuidad, centrado
exacto, norma `L2` positiva y, por compacidad, acotación uniforme. La
normalización es `P psi=lambda a tensor a`, tangente de cópula
`h_psi=2 lambda a tensor a` y score (5.2).

#### Denominador fijado

En toda esta sección y en cualquier extensión de S1 se define

\[
\boxed{
\eta_N(f):=\frac{I_N^{[P]}(f,f)}{I_N^\Pi(f,f)}.
}
\tag{5.3a}
\]

El oráculo es, por definición, la **permutación relativa de rangos**
`Pi_N`, antes del canal `Pi_N -> [P_Pi_N]`. No es la configuración continua
etiquetada y tampoco un cociente adicional de `Pi_N` por conjugación u otra
acción. Esta elección es la que usan el teorema modular, (5.3) y las fórmulas
exactas (5.12)--(5.14).

El cociente de una muestra iid etiquetada por permutación simultánea de sus
etiquetas no define aquí un segundo oráculo con menor Fisher: la verosimilitud
y su score son ya simétricos en los puntos, de modo que la muestra no ordenada
es suficiente para la muestra etiquetada. La filtración polinómica finita
`P_(N-1)` aparece al pasar de las coordenadas continuas a `Pi_N`, no al borrar
los nombres iid. Por otra parte, cocientar por el intercambio de las dos
coordenadas sí mataría el sector antisimétrico, pero sería otro experimento y
no se denomina `I_N^Pi`.

En consecuencia, el teorema fuerte que se contempla aquí significa
suficiencia asintótica de `[P]` **respecto del oráculo de rangos** en el sector
simétrico. Toda comparación con la configuración continua completa debe
enunciar además, y por separado, el paso de proyección de su score sobre
`sigma(Pi_N)`.

**Control de normalización.** El espectro generalizado de §15 del WP6 de
clasificación usa como Gram completa la del score continuo, no `G_N^Pi`.
Sus cocientes a `N=4` (`0.480`, `0.455`, `0.449` para el rayo truncado) no son
valores de (5.3a). Con el denominador de rangos, el cálculo exacto da
respectivamente `1`, `1739/1740` y `6901763/6906252`. No se intercambian ambos
denominadores en ningún argumento posterior.

**Uso del rayo.** El truncamiento
`f^(M)=sum_(k<=M) k^(-2)e_k tensor e_k` queda clasificado exclusivamente como
control de ingeniería del backend. El peso Fisher `k^(-4)` y la retención
exacta observada del primer modo pueden mantener su cociente agregado cerca de
uno aunque un modo alto pierda mucha información. Por tanto ese agregado no se
usa como evidencia del intercambio `M <-> N`, del Lema C ni de retención en
toda la clase HS. Los diagnósticos pertinentes son las eficiencias diagonales
modo a modo y la Gram completa.

**Mezcla modal.** En los cálculos racionales exactos `N=4,5,6`, `G_N^Pi` es
diagonal en los modos `e_k tensor e_k`, mientras que `G_N^[P]` tiene términos
cruzados no nulos entre modos `k>=2`. En consecuencia, la eficiencia de una
suma se calcula con `w^T G_N^[P] w`; no se sustituye por una media ponderada de
las eficiencias diagonales.

**Lema del primer modo.** La enumeración exacta da

\[
I_N^{[P]}(e_1^{\otimes2},e_1^{\otimes2})
=I_N^\Pi(e_1^{\otimes2},e_1^{\otimes2})
\qquad(N=4,5,6).
\tag{5.3b}
\]

La igualdad vale para todo `N>=2`. En efecto, el score es un múltiplo de la rho
de Spearman y su distancia cuadrática de rangos satisface

\[
\sum_i(i-\sigma(i))^2
=\sum_{v\in G_\sigma}d(v)^2-4t(G_\sigma),
\tag{5.3c}
\]

donde `G_sigma` es el grafo de incomparabilidad, `d(v)` sus grados y `t(G)` su
número de triángulos. El lado derecho es un invariante del poset no etiquetado,
de modo que el score es constante en cada fibra y la pérdida Fisher es cero.
La demostración completa está en
`dev/WP6_LEGENDRE_RAY_EXACT_SPECTRUM_NOTES.md`.

```text
INFINITE_RANK_HS = OPEN; K_MINUS_2_RAY_IS_NOT_EVIDENCE_FOR_C; N7_BLOCKED_BY_O_FACTORIAL_SQUARED_CANONICALIZATION; NEXT_ANALYTIC_CLOSURE = K1_LEMMA_PROVED_NO_MORE_N
```

`INFINITE_RANK_HS = OPEN` es el estado del preflight de 2026-08-29 y queda
**superado** por §5.3 (2026-08-30). Lo que no queda superado es la advertencia
adjunta: el rayo `k^(-2)` sigue sin ser evidencia del intercambio `M <-> N`,
y el cierre de §5.3 no se apoya en él en ningún paso.

#### Forma de pérdida

Para scores producidos por tangentes admisibles definimos

\[
\Delta_N(f,g):=G_N^\Pi(f,g)-G_N^{[P]}(f,g).
\tag{5.4}
\]

La identidad de score condicionado y polarización dan exactamente

\[
\Delta_N(f,g)
=\mathbb E\!\left[
\operatorname{Cov}(S_N(f),S_N(g)\mid[P])
\right].
\tag{5.5}
\]

Por tanto `Delta_N` es una forma bilineal semidefinida positiva,

\[
\Delta_N(f,f)
=\mathbb E[\operatorname{Var}(S_N(f)\mid[P])]\ge0,
\tag{5.6}
\]

y Cauchy--Schwarz para formas semidefinidas positivas implica

\[
|\Delta_N(f,g)|
\le\sqrt{\Delta_N(f,f)\Delta_N(g,g)}.
\tag{5.7}
\]

#### Ensamblaje finito dentro de la clase acotada de S2

Sea

\[
f=\sum_{r=1}^R\lambda_r a_r\otimes a_r,
\qquad R<\infty,
\tag{5.8}
\]

con cada `a_r in C[0,1]` centrado. El score es la suma de los scores
rank-one. De (5.7), o equivalentemente de la desigualdad triangular para la
seminorma inducida por `Delta_N`, se obtiene

\[
\Delta_N(f,f)
\le
\left(\sum_{r=1}^R|\lambda_r|
\sqrt{\Delta_N(a_r\otimes a_r,a_r\otimes a_r)}\right)^2.
\tag{5.9}
\]

La cota absoluta (7.6) del WP6 modular, antes de dividir por el Fisher, da la
versión explícita

\[
\boxed{
\Delta_N(f,f)
\le
\sqrt{240C_A}\,\sqrt N
\left(\sum_{r=1}^R|\lambda_r|\|a_r\|_\infty^2\right)^2
}
\qquad(N\ge N_A).
\tag{5.10}
\]

No se ha absorbido en `O(.)` ninguna dependencia en `R`, los eigenvalores o
las normas de los perfiles.

Para arrays centrados `x,y` y permutación uniforme, el mismo cálculo de pares
usado en §7.1 del WP6 modular, ahora polarizado, da

\[
\mathbb E[(x^TP_{\Pi_N}x)(y^TP_{\Pi_N}y)]
=\frac{(x^Ty)^2}{N-1}.
\tag{5.11}
\]

En consecuencia el denominador de (5.8) es exactamente

\[
\boxed{
I_N^\Pi(f)
=\frac4{N-1}\sum_{r,s=1}^R
\lambda_r\lambda_s
\left(\sum_{i=1}^Na_{r,i,N}a_{s,i,N}\right)^2.
}
\tag{5.12}
\]

La demostración de H3 del Teorema 7 se polariza, de modo que

\[
\frac1N\sum_i a_{r,i,N}a_{s,i,N}
\longrightarrow\langle a_r,a_s\rangle_{L^2}.
\tag{5.13}
\]

Por tanto, para `f != 0`,

\[
I_N^\Pi(f)=4N\|f\|_{HS}^2+o(N).
\tag{5.14}
\]

Combinando (5.10) y (5.14), queda probado por ensamblaje, sin uniformidad en
`R`, que para todo kernel simétrico de rango finito que admita una
descomposición (5.8) con perfiles continuos centrados,

\[
0\le1-\eta_N(f)
\le
\left[
\frac{\sqrt{240C_A}
(\sum_r|\lambda_r|\|a_r\|_\infty^2)^2}
{4\|f\|_{HS}^2}+o(1)
\right]N^{-1/2},
\qquad
\eta_N(f)\to1.
\tag{5.15}
\]

En una descomposición espectral ortonormal, la dependencia del numerador es
de tipo norma de traza ponderada por `\|a_r\|_infty^2`; no es una cota de tipo
Hilbert--Schmidt ni uniforme en `R`.

#### Único lema ausente para el enunciado literal en (L^2)

Un operador simétrico de rango finito en
`L_0^2 widehat tensor_sym L_0^2` puede tener eigenfunciones no acotadas. S2 y
(5.10) no se le aplican, porque dependen de `\|a_r\|_infty`. El denominador
no es el obstáculo: (5.12)--(5.14) siguen siendo la estructura requerida una
vez justificada la aproximación de perfiles.

El único lema nuevo suficiente es un control de cuarto momento para cada
perfil fijo `a in L_0^2`, o directamente para cada suma finita fija, que
implique

\[
\mathbb E[S_N(f)^4]=o(N^3).
\tag{5.16}
\]

Como `Pr(B_N)=O(N^{-1})`, (5.16) daría por Cauchy--Schwarz
`Delta_N(f,f)=o(N)` y, junto con (5.14), retención relativa. Una formulación
elemental candidata para probar (5.16) a partir de la expansión exacta (7.1)
es

\[
\max_i|\mathbb E[a(U_{(i)})]|=o(\sqrt N)
\qquad(a\in L^2[0,1]),
\tag{5.17}
\]

combinada con `N^{-1}\sum_i a_{i,N}^2 -> \|a\|_2^2`. Este lema no está
demostrado en los artefactos anteriores al preflight.

### 5.2 `L2_ORDER_STATISTIC_FOURTH_MOMENT_LEMMA` (2026-08-29)

El lema se cierra sin hipótesis `L-infinity`. Sea

\[
\rho_{i,N}(t)
:=N\binom{N-1}{i-1}t^{i-1}(1-t)^{N-i}
\tag{5.18}
\]

la densidad de `U_(i)` y defínase

\[
(T_Na)_i:=\int_0^1a(t)\rho_{i,N}(t)\,dt.
\tag{5.19}
\]

Como `sum_i rho_(i,N)(t)=N`, Jensen y Tonelli dan, para todo `a in L2`,

\[
\frac1N\sum_{i=1}^N|(T_Na)_i|^2
\le\frac1N\sum_i\int|a|^2\rho_{i,N}
=\|a\|_2^2.
\tag{5.20}
\]

Por tanto `T_N:L2 -> ell_N^2`, con la norma normalizada del lado discreto, es
una contracción uniforme. Para `b in C[0,1]` centrada, el Teorema 7 ya prueba
`N^(-1)||T_Nb||_2^2 -> ||b||_2^2`. Dado `a in L2`, elija `b` continuo con
`||a-b||_2<epsilon`. De (5.20),

\[
\left|N^{-1/2}\|T_Na\|_2-N^{-1/2}\|T_Nb\|_2\right|
\le\|a-b\|_2.
\tag{5.21}
\]

Pasando primero `N -> infinity` y después `epsilon -> 0`, se obtiene

\[
\boxed{
\frac1N\sum_i|\mathbb E[a(U_{(i)})]|^2\longrightarrow\|a\|_2^2.
}
\tag{5.22}
\]

Para el máximo, la expresión binomial en (5.18) implica puntualmente
`0<=rho_(i,N)<=N`; como su integral es uno,

\[
\|\rho_{i,N}\|_2^2\le\|\rho_{i,N}\|_\infty\le N.
\tag{5.23}
\]

Fijados `a in L2` y `epsilon>0`, tome una función acotada `b` con
`||a-b||_2<epsilon`. Entonces, uniformemente en `i`,

\[
\frac{|(T_Na)_i|}{\sqrt N}
\le\frac{\|b\|_\infty}{\sqrt N}
+\|a-b\|_2\frac{\|\rho_{i,N}\|_2}{\sqrt N}
\le\frac{\|b\|_\infty}{\sqrt N}+\epsilon.
\tag{5.24}
\]

Tomando `limsup_N` y luego `epsilon -> 0`, queda

\[
\boxed{
\max_i|\mathbb E[a(U_{(i)})]|=o(\sqrt N).
}
\tag{5.25}
\]

Además `sum_i(T_Na)_i=N int a=0` exactamente. Si `x_i=(T_Na)_i`, escribamos
`S_2=sum_i x_i^2`, `S_4=sum_i x_i^4` y
`M_N=max_i|x_i|`. Por (5.22), `S_2=O(N)`, mientras (5.25) da

\[
S_4\le M_N^2S_2=o(N^2).
\tag{5.26}
\]

Al sustituir estas dos estimaciones en la expansión combinatoria exacta (7.1)
del WP6 modular, sus cinco términos son respectivamente

\[
o(N^3),\qquad o(N^2),\qquad O(N^2),\qquad O(N),\qquad O(1).
\tag{5.27}
\]

En particular,

\[
\boxed{\mathbb E[X_N(a)^4]=o(N^3).}
\tag{5.28}
\]

Para una suma fija de `R` scores, Minkowski en `L4` y (5.28) implican

\[
\mathbb E[S_N(f)^4]=o(N^3),
\qquad
f=\sum_{r=1}^R\lambda_ra_r\otimes a_r,
\quad a_r\in L_0^2.
\tag{5.29}
\]

En el evento típico `A_N`, la fibra es exactamente `{Pi_N,Pi_N^(-1)}` y cada
forma cuadrática simétrica, y por tanto su suma, es invariante. Usando
`Pr(B_N)<=C_A/N`, Cauchy--Schwarz y (5.29),

\[
0\le\Delta_N(f,f)
\le\mathbb E[S_N(f)^2\mathbf1_{B_N}]
\le\Pr(B_N)^{1/2}\mathbb E[S_N(f)^4]^{1/2}
=o(N).
\tag{5.30}
\]

La polarización de (5.22) extiende (5.13) a perfiles `L2`. Por ello la fórmula
exacta (5.12) sigue dando, para todo `f != 0` simétrico de rango finito,

\[
I_N^\Pi(f)=4N\|f\|_{HS}^2+o(N).
\tag{5.31}
\]

Dividiendo (5.30) por (5.31), queda probado el teorema de rango finito en el
espacio natural:

\[
\boxed{
f\in L_0^2\widehat\otimes_{\rm sym}L_0^2,
\quad 0<\operatorname{rank}f<\infty
\quad\Longrightarrow\quad
\eta_N(f)\longrightarrow1.
}
\tag{5.32}
\]

La tasa disponible para perfiles `L2` generales es sólo `o_f(1)`: (5.25) no
proporciona una velocidad universal. La tasa `O_f(N^(-1/2))` permanece para
la subclase continua/acotada de §5.1. Este cierre es tangente/Fisher en el
espacio de Hilbert; no afirma que todo vector `L2` sea realizado por una senda
positiva continua de densidades con la regularidad geométrica original.

### 5.3 `INFINITE_RANK_SYMMETRIC_RETENTION` (2026-08-30)

El preflight de rango infinito no necesita un lema nuevo de momentos. El
intercambio `R -> infinity` / `N -> infinity` se justifica por acotación
uniforme en `N` del operador de pérdida normalizado, y esa acotación se
obtiene del denominador, no del numerador. La ruta de traza (5.10) queda
**esquivada**, no reparada.

#### Extensión lineal del score al sector HS

Con `rho_(i,N)` de (5.18) y `T_N` de (5.19), defínase para
`f in L^2([0,1]^2)` la matriz `N x N`

\[
H^{(N)}_{ij}(f)
:=\iint f(s,t)\rho_{i,N}(s)\rho_{j,N}(t)\,ds\,dt
=\bigl((T_N\otimes T_N)f\bigr)_{ij}.
\tag{5.33}
\]

`H^(N)` es lineal en `f`. Para `f=a tensor a` da
`H_ij=(T_Na)_i(T_Na)_j`, de modo que (5.1)--(5.2) se reescriben como

\[
S_N(f)=2\sum_{i=1}^N H^{(N)}_{i,\Pi_N(i)}(f),
\tag{5.34}
\]

y (5.34) es la única extensión lineal de (5.2) al sector HS. **Convención.**
Fuera del cono de rango finito, (5.34) *define* el vector de score y
`G_N^Pi(f,g):=E[S_N(f)S_N(g)]`, `G_N^[P](f,g):=E[E[S_N(f)|[P]]E[S_N(g)|[P]]]`.
No se afirma que un `f` HS arbitrario sea el tangente de una senda geométrica
positiva admisible; es la misma reserva ya registrada al final de §5.2.

Como `sum_j rho_(j,N)=N` y `int f(s,t)dt=0` en c.t.p. `s` para
`f in H widehat tensor H`, la matriz `H^(N)(f)` tiene sumas de fila y de
columna exactamente nulas.

\[
\sum_j H^{(N)}_{ij}(f)=\sum_i H^{(N)}_{ij}(f)=0.
\tag{5.35}
\]

#### Lema A — identidad Gram exacta del oráculo de rangos

Sea `H` una matriz `N x N` con sumas de fila y columna nulas y `Pi` uniforme
en `S_N`. Descomponiendo `E[sum_(i,j) H_(i,Pi(i))H_(j,Pi(j))]` en los casos
`i=j` e `i != j`, y usando

\[
\sum_{i\neq j}\sum_{k\neq l}H_{ik}H_{jl}
=\Bigl(\sum_{ik}H_{ik}\Bigr)^2
-\sum_i\Bigl(\sum_kH_{ik}\Bigr)^2
-\sum_k\Bigl(\sum_iH_{ik}\Bigr)^2
+\|H\|_F^2
=\|H\|_F^2,
\]

resulta `E[(sum_i H_(i,Pi(i)))^2] = ||H||_F^2/N + ||H||_F^2/(N(N-1))`. Por
tanto, con (5.34),

\[
\boxed{
G_N^\Pi(f,g)
=\frac4{N-1}\bigl\langle H^{(N)}(f),H^{(N)}(g)\bigr\rangle_F.
}
\tag{5.36}
\]

Especializada a (5.8) esto reproduce (5.12) verbatim: (5.36) es su forma
polarizada e independiente de base, no una normalización distinta.

#### Lema B — `T_N tensor T_N` es una contracción tras normalizar

(5.20) dice exactamente `||T_N||_(L^2 -> ell^2) <= sqrt N`. Sea
`tilde T_N := N^(-1/2)T_N`, una contracción. El producto tensorial hilbertiano
de contracciones es una contracción y `L^2 widehat tensor L^2` es el espacio
HS con su propia norma, luego

\[
\bigl\|\tilde T_N\otimes\tilde T_N\bigr\|\le1
\quad\Longleftrightarrow\quad
\bigl\|H^{(N)}(f)\bigr\|_F\le N\|f\|_{HS}.
\tag{5.37}
\]

**Nitidez de (5.37).** Sobre todo `L^2` la cota `||T_N||<=sqrt N` es *exacta*:
`sum_i rho_(i,N)=N` da `T_N1=(1,...,1)`, de modo que la constante satura
Jensen. Pero el dominio real es `H=L_0^2`, y allí la norma es estrictamente
menor y calculable en forma cerrada.

#### Lema B' — norma exacta de `T_N` sobre `H`

**Lema.** Para todo `N>=2`,

\[
\boxed{
\bigl\|T_N|_H\bigr\|^2=\frac{N(N-1)}{N+1},
}
\tag{5.37a}
\]

alcanzada exactamente en la dirección `e_1(t)\propto t-\tfrac12`, y el
extremizador es único salvo escalar.

*Paso 1 — identificación con el operador de Bernstein--Durrmeyer.* Con
`b_(k,n)(t)=binom(n,k)t^k(1-t)^(n-k)`, (5.18) es exactamente
`rho_(i,N)=N\,b_(i-1,N-1)`. Como `T_N^*c=sum_i c_i rho_(i,N)`, con `n:=N-1`,

\[
T_N^*T_Na
=N^2\sum_{k=0}^{n}b_{k,n}(x)\!\int_0^1\!a\,b_{k,n}
=N\,M_na,
\qquad
M_na:=(n+1)\sum_{k=0}^nb_{k,n}(x)\!\int_0^1\!a\,b_{k,n}.
\tag{5.37b}
\]

`M_n` es el operador de Bernstein--Durrmeyer: autoadjunto y positivo, con
núcleo simétrico `(n+1)sum_k b_(k,n)(s)b_(k,n)(t)`. Se anula sobre
`P_n^perp`, porque `b_(k,n) in P_n`.

*Paso 2 — triangularidad y coeficiente diagonal.* De
`int_0^1 t^m b_(k,n)=n!(k+m)!/(k!(n+m+1)!)` y del hecho de que
`(k+m)!/k!=(k+1)\cdots(k+m)` es mónico de grado `m` en `k`, cuyo factorial
descendente principal tiene esperanza exacta `n!/(n-m)!\,x^m` bajo
`K~Bin(n,x)`, resulta para `m<=n`

\[
M_n(t^m)(x)=\lambda_{n,m}x^m+(\text{grado}<m),
\qquad
\lambda_{n,m}=\frac{(n+1)!\,n!}{(n+m+1)!\,(n-m)!}.
\tag{5.37c}
\]

En particular `M_n(P_m) subseteq P_m` para todo `m<=n`.

*Paso 3 — diagonalización.* `M_n` es autoadjunto y deja invariante toda la
cadena `P_0 subset P_1 subset ... subset P_n`, luego deja invariante cada
complemento ortogonal `P_m ominus P_(m-1)`, que es unidimensional y está
generado por el Legendre desplazado `e_m`. Por tanto los `e_m` son
autofunciones y, por (5.37c), el autovalor es `lambda_(n,m)`. El espectro de
`M_n` es `{lambda_(n,m)}_(m=0)^n union {0}`, este último sobre `P_n^perp`.

*Paso 4 — monotonía y conclusión.* Directamente de (5.37c),

\[
\frac{\lambda_{n,m+1}}{\lambda_{n,m}}=\frac{n-m}{n+m+2}<1,
\]

así que `lambda_(n,m)` es estrictamente decreciente en `m`, con
`lambda_(n,0)=1`. La única autofunción no centrada es `e_0=1`, luego
`H=cl span{e_m: m>=1}` y el máximo de `M_n` sobre `H` es `lambda_(n,1)`,
simple. Con `n=N-1`,

\[
\bigl\|T_N|_H\bigr\|^2
=N\lambda_{N-1,1}
=N\cdot\frac{N-1}{N+1},
\]

que es (5.37a). El autovalor es simple por la monotonía estricta, de modo que
el extremizador es `e_1` salvo escalar. `∎`

Comprobación directa del caso `m=1`, independiente de los Pasos 2--3: con
`u=t-1/2` se tiene `(T_Nu)_i=(2i-N+1)/(2(N+1))` y
`sum_i(2i-n)b_(i,n)(x)=2n(x-1/2)`, luego `T_N^*T_Nu=N(N-1)u/(N+1)`.

```text
ORDER_STATISTIC_MEAN_ZERO_NORM = PROVED_EXACT
```

#### Corolario — constante uniforme

Como `f in H widehat tensor_sym H` tiene ambos factores en `H`, (5.37a)
refina (5.37) a `||H^(N)(f)||_F <= [N(N-1)/(N+1)]\,||f||_HS`, y (5.36) da

\[
\boxed{
\frac{\Delta_N(f,f)}N
\le\frac{I_N^\Pi(f)}N
\le\frac{4N(N-1)}{(N+1)^2}\|f\|_{HS}^2
<4\|f\|_{HS}^2.
}
\tag{5.37d}
\]

**Las dos desigualdades de (5.37d) no tienen el mismo estatus. No se deben
citar juntas como "cota nítida".**

*La segunda es nítida, y de hecho se alcanza exactamente.* Para
`f=e_1^(tensor 2)` se tiene `H^(N)(f)=(T_Ne_1)(T_Ne_1)^T`, luego
`||H^(N)(f)||_F=||T_Ne_1||^2=N(N-1)/(N+1)` por el Lema B', y (5.36) da

\[
\frac{I_N^\Pi(e_1^{\otimes2})}N
=\frac{4}{N(N-1)}\left(\frac{N(N-1)}{N+1}\right)^{\!2}
=\frac{4N(N-1)}{(N+1)^2}
\qquad\forall N\ge2,
\tag{5.37e}
\]

con igualdad para todo `N`, no sólo en el límite. La constante
`4N(N-1)/(N+1)^2` crece estrictamente hacia `4`, el valor del límite (5.40),
de modo que `4` es la mejor constante uniforme posible para el Fisher de
referencia.

*La primera no se sabe nítida.* El extremizador del miembro derecho es
`e_1^(tensor 2)`, y precisamente allí

\[
\Delta_N(e_1^{\otimes2},e_1^{\otimes2})=0
\qquad\forall N\ge2
\]

por (5.3b)--(5.3c). Es decir, en la dirección que satura la cota dominante la
pérdida es **exactamente nula**: la cadena `Delta_N<=I_N^Pi` es máximamente
holgada justo donde el segundo paso es exacto. Nada de lo anterior determina
`sup_f Delta_N(f,f)/(N||f||_HS^2)`, que queda sin calcular.

```text
REFERENCE_FISHER_HS_BOUND = SHARP; attained at e_1^ox2 for every N >= 2 (5.37e)
NORMALIZED_LOSS_BOUND     = VALID, SHARPNESS_OPEN
```

**Este corolario no mejora ninguna tasa**: `Delta_N(f,f)/N -> 0` para cada `f`
fijo por el Teorema 11, y (5.37d) es sólo un control uniforme sobre la esfera
HS. `RATE` sigue siendo `o_f(1)_NO_UNIFORM_RATE_CLAIMED`.

#### Observación — el doble papel de `e_1`

Registrada como observación, **no como principio** y sin lectura física:

\[
e_1=
\begin{cases}
\text{dirección que maximiza el Fisher de referencia por norma HS}
&\text{(Lema B', (5.37e))},\\
\text{dirección cuyo Fisher se conserva exactamente tras el cociente}
&\text{((5.3b)--(5.3c))}.
\end{cases}
\]

En S1 la dirección estadísticamente más fuerte es también la que el poset
abstracto transmite sin pérdida alguna. El Lema B' explica además por qué el
primer modo no es una casualidad numérica: `e_1` es el primer autovector no
constante del operador de Bernstein--Durrmeyer que gobierna los perfiles de
estadísticos de orden. No se deriva de aquí ninguna conclusión, ni sobre
horizontes ni sobre el benchmark.

Las demostraciones de los Teoremas 9--12 se dejan **sin cambios**, apoyadas en
la cota `||T_N||<=sqrt N` y en la constante `4N/(N-1)<=8`: (5.37d) es un
refinamiento posterior y ningún paso depende de él.

#### Teorema 9 — cota HS uniforme del denominador

Combinando (5.36) y (5.37), para todo `f in H widehat tensor_sym H` y todo
`N>=2`,

\[
\boxed{
0\le I_N^\Pi(f)
=\frac4{N-1}\bigl\|H^{(N)}(f)\bigr\|_F^2
\le\frac{4N}{N-1}\,N\,\|f\|_{HS}^2
\le 8N\|f\|_{HS}^2.
}
\tag{5.38}
\]

La constante exacta es `4N/(N-1)`, monótona decreciente a `4`. La clase de
norma es **Hilbert--Schmidt (Schatten-2)**; no interviene `sum_r|lambda_r|`,
ni `||a_r||_inf`, ni el rango `R`. No se requiere trace class.

#### Corolario — cota HS uniforme de la pérdida

`G_N^[P](f,f)=E[E[S_N(f)|[P]]^2]>=0`, luego por (5.6)

\[
\boxed{
0\le T_N(f,f):=\frac{\Delta_N(f,f)}N
\le\frac{I_N^\Pi(f)}N
\le8\|f\|_{HS}^2,
\qquad
\sup_N\|T_N\|_{\rm op}\le8.
}
\tag{5.39}
\]

Esto sustituye a (5.10) como control uniforme. Sólo usa positividad de
`G_N^[P]`, la identidad de varianza condicional (5.5)--(5.6) y (5.38).

#### Teorema 10 — límite del denominador en todo HS

Sea `J_N(f,g):=I_N^Pi(f,g)/N`, forma semidefinida positiva con
`||J_N||_op<=8` por (5.38). Para rango finito, (5.14) da
`J_N(f_R,f_R) -> 4||f_R||_HS^2`. Por Cauchy--Schwarz (5.7) aplicada a `J_N`,

\[
\bigl|\sqrt{J_N(f,f)}-\sqrt{J_N(f_R,f_R)}\bigr|
\le\sqrt{J_N(f-f_R,f-f_R)}
\le\sqrt8\,\|f-f_R\|_{HS},
\]

de modo que

\[
\limsup_N\bigl|\sqrt{J_N(f,f)}-2\|f\|_{HS}\bigr|
\le(\sqrt8+2)\|f-f_R\|_{HS}
\xrightarrow[R\to\infty]{}0,
\]

\[
\boxed{
\frac{I_N^\Pi(f)}N\longrightarrow4\|f\|_{HS}^2
\qquad\forall f\in H\widehat\otimes_{\rm sym}H.
}
\tag{5.40}
\]

#### Teorema 11 — pérdida normalizada nula en todo HS

Mismo argumento con `T_N`. Para rango finito, (5.30)/(5.32) dan
`T_N(f_R,f_R) -> 0`. Por (5.7) y (5.39),

\[
\sqrt{T_N(f,f)}
\le\sqrt{T_N(f_R,f_R)}+\sqrt{T_N(f-f_R,f-f_R)}
\le\sqrt{T_N(f_R,f_R)}+\sqrt8\,\|f-f_R\|_{HS},
\]

\[
\limsup_N\sqrt{T_N(f,f)}\le\sqrt8\,\|f-f_R\|_{HS},
\qquad
\boxed{\frac{\Delta_N(f,f)}N\longrightarrow0.}
\tag{5.41}
\]

**Orden lógico, explícito.** (i) `R` se elige *primero*, sólo con
`f_R -> f` en HS y sin mirar `N`; (ii) el término `f-f_R` se controla por
(5.39), que es uniforme en `N`; (iii) `R` queda fijo; (iv) sólo entonces
`N -> infinity` actúa sobre el término de rango finito. No se intercambian
límites en ningún punto y no se invoca "por densidad" sin esta cadena.

**Densidad utilizada.** Para `f in H widehat tensor_sym H`, el teorema
espectral da `f=sum_k lambda_k e_k tensor e_k` con `{e_k}` ortonormal; cada
`e_k` con `lambda_k != 0` está en el rango de `f`, luego `int e_k=0` y
`e_k in H`. La truncación `f_R=sum_(k<=R)` es simétrica de rango finito,
`f-f_R in H widehat tensor_sym H`, y `||f-f_R||_HS -> 0`. Esto es la misma
densidad ya registrada como `cl(union_N V_N)=H widehat tensor_sym H`.

#### Lema C — buena definición de `eta_N` y umbral `N_0(f)`

`eta_N(f)` es un cociente y hay que decir dónde está definido. Por (5.36),
`I_N^Pi(f)=0` si y sólo si `H^(N)(f)=0`, es decir si y sólo si
`f perp P_(N-1) tensor P_(N-1)`; para `f` simétrico, si y sólo si
`f perp V_N=Sym^2 P_(N-1)`. Esto coincide exactamente con la restricción al
sector simétrico de (6.8) del teorema de rango de clase completa, que da

\[
\ker G_{[P]}^{(N)}
=\bigl(\operatorname{Sym}^2P_{N-1}\bigr)^{\perp_{\rm sym}}
\oplus\bigwedge^2H,
\]

de modo que **ambas** formas de Gram tienen el mismo núcleo dentro del sector
simétrico y `eta_N(f)` es de la forma `0/0` precisamente sobre `V_N^perp`, no
`0` ni `1`.

Por (5.40), `I_N^Pi(f)/N -> 4||f||_HS^2>0` para `f != 0`, luego existe
`N_0(f)` finito con

\[
I_N^\Pi(f)>0
\qquad\forall N\ge N_0(f).
\tag{5.41a}
\]

Equivalentemente: ningún `f != 0` es invisible a toda cardinalidad, que es la
lectura cuantitativa de `cl(union_N V_N)=H widehat tensor_sym H`. El umbral
`N_0(f)` depende de `f` y no es uniforme sobre la esfera HS: para `f=e_k
tensor e_k` se tiene `N_0>=k+1`. Todos los enunciados sobre `eta_N` en esta
sección se entienden para `N>=N_0(f)`.

#### Teorema 12 — `INFINITE_RANK_SYMMETRIC_RETENTION`

Para todo `0 != f in H widehat tensor_sym H` y todo `N>=N_0(f)` del Lema C,
por (5.40) el denominador
normalizado tiende a `4||f||_HS^2>0` y por (5.41) el numerador de pérdida
normalizado tiende a cero, luego

\[
\boxed{
1-\eta_N(f)
=\frac{\Delta_N(f,f)/N}{I_N^\Pi(f)/N}
\longrightarrow0,
\qquad
\eta_N(f)\longrightarrow1.
}
\tag{5.42}
\]

La tasa disponible es sólo `o_f(1)`: (5.41) hereda de (5.32) la ausencia de
velocidad universal, y el paso de densidad no la recupera. La tasa
`O(N^(-1/2))` sigue restringida a la subclase acotada/continua de rango finito
de §5.1.

#### Compatibilidad con el modo `k=1`

(5.3b)--(5.3c) dan `Delta_N(e_1^(tensor 2),e_1^(tensor 2))=0` para todo
`N>=2`, no `-> 0`. Es compatible con el Teorema 12 de la forma más fuerte
posible, pero su naturaleza es distinta: **suficiencia exacta a `N` finito**
del poset no etiquetado para la rho de Spearman, vía el invariante
`sum_i(i-sigma(i))^2 = sum_v d(v)^2 - 4t(G_sigma)`. Por eso el modo `k=1` no
se usa, ni aquí ni en ningún agregado del rayo `k^(-2)`, como evidencia de
convergencia asintótica.

#### Dos niveles: teorema hilbertiano vs. realizabilidad geométrica

El cierre de esta sección es un teorema **en el espacio de Hilbert tangente**.
Debe enunciarse como

> el canal del poset no etiquetado es asintóticamente Fisher-suficiente sobre
> el cierre tangente simétrico Hilbert--Schmidt completo de S1,

y no como una afirmación sobre deformaciones métricas arbitrarias. La
traducción geométrica sólo es directa para tangentes que sepamos realizar por
una senda admisible: la clase `psi=alpha+beta+lambda f tensor f` de S2, y sus
sumas finitas con perfiles suficientemente regulares. Para un `f` HS genérico
no se ha exhibido tal senda.

```text
THEOREM_HILBERT = PROVED
GEOMETRIC_REALIZABILITY_OF_ARBITRARY_HS = OPEN
```

No se debe deslizar el primero al segundo en ningún resumen del programa.

#### Mapa del sector tangente completo de S1

Reuniendo el Teorema 1 (1.2)--(1.3), (6.7)--(6.8) del teorema de rango de clase
completa, el lema del primer modo y (5.42), S1 queda con cuatro niveles.

**Nivel 1 — visibilidad a `N` finito.** Por (1.2)--(1.3),

\[
V_N=\operatorname{Sym}^2P_{N-1},
\qquad
\dim V_N=\operatorname{rank}G_{[P]}^{(N)}=\binom N2,
\qquad
V_N\subsetneq V_{N+1},
\]

y `cl(union_N V_N)=H widehat tensor_sym H`. A cada `N` la resolución es
polinómica de grado `<=N-1` en cada coordenada: mucho es invisible, pero nada
fijo lo es para siempre (Lema C).

**Nivel 2 — modo fundamental, suficiencia exacta.**
`eta_N(e_1^(tensor 2))=1` para todo `N>=2`, por (5.3b)--(5.3c). No es un
ejemplo de convergencia.

**Niveles 3 y 4 — sector simétrico completo y núcleo permanente:**

\[
\begin{array}{ccl}
H\widehat\otimes_{\rm sym}H
&:&\text{retención Fisher asintótica total, }\eta_N\to1
   \text{ para todo }f\neq0,\\[1mm]
\textstyle\bigwedge^2H
&:&\subseteq\ker G_{[P]}^{(N)}\ \text{para todo }N
   \text{ — invisible exactamente, a toda cardinalidad,}
\end{array}
\]

y dentro del sector simétrico el modo fundamental es un caso de suficiencia
exacta, `eta_N(e_1^(tensor 2))=1` para todo `N>=2`. La pérdida permanente del
sector antisimétrico es una afirmación sobre el canal `[P]`; no dice que
`I_N^Pi` se anule allí — en efecto (5.51) da `I_N^Pi(f_a)/N -> 4||f_a||_HS^2`.
El cociente `eta_N` en el sector mixto se enuncia en §5.4, Teorema 16:
`MIXED_SECTOR_LIMIT = PROVED_NORM_RATIO`.

#### Ataque adversarial — resultado

La obstrucción buscada era una sucesión `f_m` con `||f_m||_HS=1` y `N_m` tales
que `Delta_(N_m)(f_m,f_m)/N_m` no admitiera cota uniforme. No puede existir:
(5.39) acota esa cantidad por `8` sobre toda la esfera unidad HS,
simultáneamente en `f` y en `N`. La divergencia `sum_r|lambda_r|=infinity`
refutaba únicamente la técnica (5.10), que aquí no se usa. `ADVERSARIAL_SEQUENCE
= NONEXISTENT_BY_(5.39)`.

#### Verificación simbólica de las tres piezas estructurales

La restricción diagonal de (5.36) ya está aseverada en el backend exploratorio
`dev/wp6_legendre_ray_exact_spectrum.py` (`assert oracle == expected_oracle`).
La forma polarizada general de (5.36) con modos cruzados
`e_j tensor e_k + e_k tensor e_j`, la contracción (5.37) y la desigualdad
`0 <= Delta_N <= G_N^Pi` de (5.39) se comprobaron exactamente sobre `Q` para
`N=4,5` en un script de sesión. Un segundo pase de auditoría, independiente del
primero y extendido a modos `k>=N` fuera del span visible, verificó además:
coincidencia de los núcleos de `G_N^Pi` y `G_N^[P]` dentro del sector simétrico
(cross-check de (6.8) y base del Lema C); la cota del Teorema 9 sobre kernels
que mezclan modos visibles e invisibles; el carácter `0/0` de `eta_N` sobre
`V_N^perp` dentro del Hilbert simétrico; y `G_N^[P]=0` exacto sobre kernels
antisimétricos, con `G_N^Pi>0`
(cross-check de (6.7)). Ambas comprobaciones son `NOT_AN_ARTIFACT`: la
demostración es analítica y ningún número de ellas entra en este documento ni
en ningún resultado publicado. El `assert oracle == expected_oracle` del backend
citado sí es reproducible y se re-ejecutó en el run de congelación.

El Lema B' se comprobó igualmente como *sanity check* para `N=2,...,9`: el
espectro completo de la Gram `<rho_i,rho_j>` coincide con `N lambda_(N-1,m)` de
(5.37c), y `T_N^*T_N(t-1/2)=[N(N-1)/(N+1)](t-1/2)` exactamente. La prueba del
Lema B' es analítica y vale para todo `N>=2`; esa comprobación no forma parte
de ella.

### 5.4 `MIXED_SECTOR_PREFLIGHT` (2026-08-30)

Se abre el sector mixto **sólo** en el nivel hilbertiano de S1. Se decide la
estructura exacta de las dos formas de Gram bajo

\[
H\widehat\otimes H
=\bigl(H\widehat\otimes_{\rm sym}H\bigr)
\oplus\Bigl(\textstyle\bigwedge^2H\Bigr),
\qquad
f=f_s+f_a.
\]

El score se extiende linealmente por (5.34) a todo `H widehat tensor H`; la
reserva de §5.3 sobre realizabilidad geométrica se mantiene y se agrava en el
sector antisimétrico (véase el final de esta sección).

#### Lema D — `H_N` entrelaza transposición e intercambio de coordenadas

Sea `f^T(s,t):=f(t,s)`. De (5.33), por el cambio de variables `s <-> t`,

\[
\bigl(H^{(N)}(f)\bigr)^{\mathsf T}_{ij}
=H^{(N)}_{ji}(f)
=\iint f(s,t)\rho_{j,N}(s)\rho_{i,N}(t)
=\iint f(t,s)\rho_{i,N}(s)\rho_{j,N}(t)
=H^{(N)}_{ij}(f^{\mathsf T}),
\]

es decir `H^(N)(f)^T = H^(N)(f^T)` exactamente, para todo `N` y todo
`f in L^2([0,1]^2)`. Que el mismo operador `T_N` actúe en las dos ranuras es
esencial: es lo que hace conmutar `H^(N)` con la transposición. En
consecuencia

\[
\boxed{
f_s^{\mathsf T}=f_s\Rightarrow H^{(N)}(f_s)^{\mathsf T}=H^{(N)}(f_s),
\qquad
f_a^{\mathsf T}=-f_a\Rightarrow H^{(N)}(f_a)^{\mathsf T}=-H^{(N)}(f_a).
}
\tag{5.43}
\]

#### Teorema 13 — el Fisher de referencia separa exactamente los sectores

Para matrices reales, `<A,B>_F=tr(A^TB)` anula todo par simétrico/antisimétrico.
Por (5.43) y la identidad exacta (5.36),

\[
\boxed{
G_N^\Pi(f_s,f_a)=\frac4{N-1}\bigl\langle
H^{(N)}(f_s),H^{(N)}(f_a)\bigr\rangle_F=0
\qquad\forall N\ge2,
}
\tag{5.44}
\]

y por tanto, **exactamente y a todo `N`**,

\[
I_N^\Pi(f)=I_N^\Pi(f_s)+I_N^\Pi(f_a).
\tag{5.45}
\]

Esto no es una aproximación asintótica ni depende de ninguna hipótesis sobre
la fibra: es ortogonalidad de Frobenius transportada por `H^(N)`.

#### Teorema 14 — el sector antisimétrico es invisible bilinealmente

`(6.7)` afirma `wedge^2 H subseteq ker G_[P]^(N)`. Aquí se prueba la forma
fuerte, que es puntual y da todos los términos cruzados.

Intercambiar las dos coordenadas `u <-> v` deja **literalmente invariante** el
orden producto, porque la relación `u_i<u_j` y `v_i<v_j` es simétrica en las
dos coordenadas, y sustituye la permutación de rangos `pi` por `pi^(-1)`. Por
tanto `[P_pi]=[P_(pi^(-1))]` y toda fibra `F` del cociente `pi -> [P_pi]` es
cerrada bajo inversión. Para `H` antisimétrica,

\[
S_H(\pi^{-1})=\sum_jH_{\pi^{-1}(j),j}=-\sum_jH_{j,\pi^{-1}(j)}=-S_H(\pi),
\]

luego `sum_(pi in F) S_H(pi) = sum_(pi in F) S_H(pi^(-1)) = - sum_(pi in F)
S_H(pi)`, y la suma es nula. Como `Pi_N` es uniforme, la ley condicional en
cada fibra es uniforme y

\[
\boxed{
\mathbb E\bigl[S_N(f_a)\mid[P]\bigr]=0
\quad\text{puntualmente},
\qquad\forall N,\ \forall f_a\in\textstyle\bigwedge^2H.
}
\tag{5.46}
\]

(No hace falta emparejar `pi` con `pi^(-1)`: basta que `F` sea invariante. Las
involuciones `pi=pi^(-1)` dan `S_H(pi)=0` directamente.)

De (5.46), para **todo** `g in H widehat tensor H`,

\[
G_N^{[P]}(f_a,g)
=\mathbb E\bigl[\mathbb E[S_N(f_a)|[P]]\,\mathbb E[S_N(g)|[P]]\bigr]=0,
\tag{5.47}
\]

y en particular `G_N^[P](f_s,f_a)=0`. La misma conclusión se sigue, más
débilmente, de (6.7) y Cauchy--Schwarz (5.7):
`|G_N^[P](f_s,f_a)|^2 <= G_N^[P](f_s,f_s)G_N^[P](f_a,f_a)=0`. Por tanto

\[
\boxed{
I_N^{[P]}(f)=I_N^{[P]}(f_s)
\qquad\forall N.
}
\tag{5.48}
\]

#### Teorema 15 — límite del Fisher de referencia en todo `H widehat tensor H`

El Lema B' da algo más fuerte que la ruta epsilon/3 del Teorema 10, y cubre el
sector antisimétrico sin argumento de densidad. Con `tilde T_N=N^(-1/2)T_N`,
(5.37b) es exactamente

\[
\tilde T_N^*\tilde T_N=M_{N-1},
\]

cuyo espectro es `{lambda_(N-1,m)}` sobre `e_m`, `m<=N-1`, y `0` sobre
`P_(N-1)^perp`. De (5.37c),

\[
\lambda_{n,m}=\prod_{r=1}^m\frac{n-r+1}{n+r+1}\in[0,1],
\qquad
\lambda_{N-1,m}\xrightarrow[N\to\infty]{}1
\ \text{ para cada }m\text{ fijo.}
\tag{5.49}
\]

Para `f=sum_(j,k>=1)c_(jk)\,e_j tensor e_k in H widehat tensor H`,

\[
\bigl\|(\tilde T_N\otimes\tilde T_N)f\bigr\|_F^2
=\sum_{j,k\ge1}\lambda_{N-1,j}\lambda_{N-1,k}|c_{jk}|^2
\longrightarrow\sum_{j,k\ge1}|c_{jk}|^2=\|f\|_{HS}^2
\tag{5.50}
\]

por convergencia dominada, con dominante sumable `|c_(jk)|^2` y factores en
`[0,1]`. Como `I_N^Pi(f)=\frac{4N}{N-1}N\|(tilde T_N tensor tilde T_N)f\|_F^2`,

\[
\boxed{
\frac{I_N^\Pi(f)}N\longrightarrow4\|f\|_{HS}^2
\qquad\forall f\in H\widehat\otimes H,
}
\tag{5.51}
\]

simétrico, antisimétrico o mixto. El Teorema 10 queda como caso particular; su
demostración por densidad sigue siendo válida y no se retira, pero (5.51) es
estrictamente más general y no usa densidad.

**Lema C extendido.** Igual que en §5.3, `I_N^Pi(f)=0` si y sólo si
`f perp P_(N-1) tensor P_(N-1)`, y (5.51) da `N_0(f)<infinity` para todo
`f != 0` en `H widehat tensor H`. Todo lo que sigue se entiende para
`N>=N_0(f)`. Nótese que `wedge^2P_1=0`, de modo que a `N=2` todo el sector
antisimétrico es invisible también para `G_N^Pi`; esto lo absorbe `N_0`.

#### Teorema 16 — `MIXED_SECTOR_LIMIT`

Sea `0 != f=f_s+f_a` y `N>=N_0(f)`. Por (5.45), (5.48), (5.51) y el
Teorema 11 aplicado a `f_s`,

\[
\eta_N(f)
=\frac{I_N^{[P]}(f_s)}{I_N^\Pi(f_s)+I_N^\Pi(f_a)}
=\frac{I_N^\Pi(f_s)/N-\Delta_N(f_s,f_s)/N}
       {I_N^\Pi(f_s)/N+I_N^\Pi(f_a)/N}
\longrightarrow
\frac{4\|f_s\|_{HS}^2-0}{4\|f_s\|_{HS}^2+4\|f_a\|_{HS}^2},
\]

es decir

\[
\boxed{
\eta_N(f)\longrightarrow
\frac{\|f_s\|_{HS}^2}{\|f_s\|_{HS}^2+\|f_a\|_{HS}^2}.
}
\tag{5.52}
\]

El denominador límite es `4||f||_HS^2>0` por la ortogonalidad de la
descomposición, luego el cociente está bien definido en el límite.

**Casos extremos, ambos automáticos.**

- `f_a=0`: (5.52) da `1`, recuperando el Teorema 12.
- `f_s=0`: por (5.48) el numerador es **exactamente** cero, luego
  `eta_N(f)=0` para todo `N>=N_0(f)`, no sólo en el límite. La pérdida
  antisimétrica es total y finita-`N`, no asintótica.

```text
MIXED_SECTOR_PREFLIGHT = PASS_EXACT_ORTHOGONAL_SPLITTING
MIXED_SECTOR_LIMIT = PROVED_NORM_RATIO
```

#### Ataque adversarial — resultado

- *Ortogonalidad sym/skew tras `T_N tensor T_N`*: no se asume, se prueba en el
  Lema D, y depende de que sea **el mismo** `T_N` en ambas ranuras. Con dos
  operadores distintos la simetría no se conservaría.
- *Transposición vs. intercambio `u <-> v`*: identificados explícitamente por
  el cambio de variables del Lema D y por la invariancia literal del orden
  producto en el Teorema 14.
- *Extensión HS del sector antisimétrico*: (5.51) es espectral y directa, sin
  densidad ni epsilon/3, luego no hereda ninguna laguna de aquéllas.
- *Cross terms de `G_N^[P]`*: cubiertos por (5.46), que es puntual, no sólo
  diagonal; y por Cauchy--Schwarz como ruta independiente.
- *Normalización del Fisher de referencia*: se usa (5.36) sin cambios; el
  denominador es el oráculo de rangos `Pi_N` fijado en (5.3a), no otro.
- *Degeneración del denominador*: Lema C extendido, `N>=N_0(f)`.
- *Forma cuadrática vs. tangente realizable*: ver el párrafo siguiente.

No se encontró ningún término cruzado no nulo. `INTERACTION_FOUND = NO`.

#### Reserva de realizabilidad, agravada en el sector antisimétrico

`GEOMETRIC_REALIZABILITY_OF_ARBITRARY_HS = OPEN` sigue en pie para el espacio
completo. **Corrección (§5.5, 2026-08-30):** la frase original de esta sección
—"ningún elemento no nulo de `wedge^2 H` se ha exhibido como tangente de una
senda admisible"— es **falsa**. El testigo (5.54) es admisible y su tangente
está en `wedge^2 H \ {0}`. Lo que S2 restringe a tangentes simétricos es la
clase `psi=alpha+beta+lambda f tensor f` de S2, no la admisibilidad de S1, que
sólo pide `psi in C(D;R)`.

Ahora bien, esa realizabilidad **no** convierte (5.52) en pérdida de
información geométrica física: por el Teorema 17, `R^*g_epsilon=g_(-epsilon)`,
de modo que la dirección antisimétrica identifica `+epsilon` con `-epsilon` por
una isometría del fondo y la ley del poset es exactamente par en `epsilon`.
La lectura autorizada de (5.52) es la de §5.5: insensibilidad de primer orden
a las direcciones impares bajo la isotropía discreta. Los tres niveles de §5.3
se mantienen separados.


### 5.4bis `RELATIVE_FISHER_OPERATOR_IDENTIFICATION` (2026-08-31)

Esta sección cierra únicamente la identificación operatorial relativa de las
formas Fisher ya construidas. No abre realizabilidad geométrica, no modifica
el canal, no introduce una generalización de la familia y no cambia ningún
claim físico.

#### Hilbert común y formas normalizadas

Sea `H=L_0^2([0,1])`. El Hilbert tangente común de la clase completa es

\[
\boxed{
\mathcal H
=H\widehat\otimes H
=\operatorname{Sym}^2H\oplus\bigwedge^2H.
}
\tag{5.52a}
\]

Las formas de Gram de (5.34)--(5.36) definen, por Riesz, los operadores
positivos acotados `B_N,A_N in L(mathcal H)` mediante

> **Desambiguación local.** En esta sección, `A_N` y `B_N` designan operadores
> Fisher. No deben confundirse con los eventos históricos homónimos usados en
> secciones anteriores.

\[
\boxed{
\langle f,B_Ng\rangle
=\frac{G_N^\Pi(f,g)}{4N},
\qquad
\langle f,A_Ng\rangle
=\frac{G_N^{[P]}(f,g)}{4N}.
}
\tag{5.52b}
\]

La identidad de varianza condicional (5.5)--(5.6), o equivalentemente la
contractividad de la esperanza condicional, da exactamente

\[
\boxed{0\le A_N\le B_N\le I.}
\tag{5.52c}
\]

La última cota usa la norma exacta de `T_N|_H` del Lema B'; la parte esencial
para la factorización relativa es `A_N<=B_N`.

No se identifican sus soportes. Por (5.36), el Lema C extendido y (6.8) del
teorema de rango de clase completa,

\[
\begin{aligned}
\ker B_N
&=\bigl(P_{N-1}\widehat\otimes P_{N-1}\bigr)^\perp,\\
\operatorname{supp}B_N
&=\mathcal S_N
=P_{N-1}\widehat\otimes P_{N-1},
\end{aligned}
\tag{5.52d}
\]

mientras

\[
\begin{aligned}
\ker A_N
&=\bigl(\operatorname{Sym}^2P_{N-1}\bigr)^{\perp_{\rm sym}}
  \oplus\bigwedge^2H,\\
\operatorname{supp}A_N
&=V_N
=\operatorname{Sym}^2P_{N-1}.
\end{aligned}
\tag{5.52e}
\]

Así, la permutación de rangos ve también
`wedge^2 P_(N-1)`, mientras el poset no etiquetado anula ese sector
exactamente. En particular `supp A_N` es un subespacio propio de `supp B_N`
cuando el sector antisimétrico finito no es trivial.

#### Operador Fisher relativo sobre el soporte

Para cada `N`, `B_N|_(mathcal S_N)` es positivo definido sobre el espacio de
dimensión finita `mathcal S_N`. Se define

\[
\boxed{
R_N
=B_N^{\dagger/2}A_NB_N^{\dagger/2},
}
\tag{5.52f}
\]

donde `dagger` denota la pseudoinversa de Moore--Penrose. Equivalentemente,

\[
R_N|_{\mathcal S_N}
=\bigl(B_N|_{\mathcal S_N}\bigr)^{-1/2}
 A_N
 \bigl(B_N|_{\mathcal S_N}\bigr)^{-1/2},
\qquad
R_N=0\quad\text{sobre }\ker B_N.
\tag{5.52g}
\]

No se escribe `B_N^(-1/2)` globalmente. Como `A_N<=B_N`, la factorización de
Douglas —aquí equivalente al cálculo finito sobre `mathcal S_N`— da

\[
\boxed{
A_N=B_N^{1/2}R_NB_N^{1/2},
\qquad
0\le R_N\le I.
}
\tag{5.52h}
\]

Es la única solución reducida por `P_(mathcal S_N) R_N P_(mathcal S_N)=R_N`.
Además, como `B_N` preserva la descomposición simétrica/antisimétrica y `A_N`
es positivo definido sobre `V_N`,

\[
\ker R_N=V_N^\perp,
\qquad
\operatorname{supp}R_N=V_N.
\tag{5.52i}
\]

#### Identidad exacta de retención

Para todo `f in mathcal H` tal que `<f,B_N f> > 0`, sea

\[
u_N(f):=B_N^{1/2}f\neq0.
\tag{5.52j}
\]

Entonces (5.3a) y (5.52h) dan, sin límite ni aproximación,

\[
\boxed{
\eta_N(f)
=\frac{\langle f,A_Nf\rangle}{\langle f,B_Nf\rangle}
=\frac{\langle u_N(f),R_Nu_N(f)\rangle}{\|u_N(f)\|^2}.
}
\tag{5.52k}
\]

A `N` finito queda **prohibido** sustituir `u_N(f)` por `f` y escribir
`eta_N(f)=<f,R_N f>/||f||^2`. Si `f in ker B_N`, (5.52c) implica también
`f in ker A_N` y el cociente original es `0/0`, no cero. Para todo `f!=0`,
el Lema C extendido ya garantiza un `N_0(f)<infinity` tal que
`<f,B_N f> > 0` para todo `N>=N_0(f)`; el umbral no es uniforme sobre la esfera
HS.

#### Esperanza condicional y no idempotencia finita

Defínase el score normalizado

\[
D_Nf:=\frac{S_N(f)}{2\sqrt N}
\quad\text{en }L_0^2(\Pi_N),
\qquad
Q_N:=\mathbb E[\cdot\mid[P]].
\tag{5.52l}
\]

`Q_N` es la proyección ortogonal de esperanza condicional y

\[
B_N=D_N^*D_N,
\qquad
A_N=D_N^*Q_ND_N.
\tag{5.52m}
\]

El operador definido sobre `mathcal S_N`

\[
U_N:=D_NB_N^{\dagger/2}\big|_{\mathcal S_N}
=D_N\bigl(B_N|_{\mathcal S_N}\bigr)^{-1/2}
\tag{5.52n}
\]

es una isometría de `mathcal S_N` sobre el subespacio de scores de la
permutación, y

\[
\boxed{R_N|_{\mathcal S_N}=U_N^*Q_NU_N.}
\tag{5.52o}
\]

La identidad global se completa con `R_N=0` sobre `ker B_N`, como en
(5.52g); no se extiende aquí `U_N` fuera de `mathcal S_N`.

Por tanto `R_N` se interpreta como compresión de conditional expectation,
operador Fisher relativo y operador del generalized Rayleigh quotient. No es
en general una proyección: comprimir una proyección a un subespacio no
invariante no preserva idempotencia.

El falsificador finito ya está registrado en el control de normalización tras
(5.3a): a `N=4` aparece la retención simétrica exacta `1739/1740<1`. Para esa
dirección `u_N(f) in V_N=supp R_N`; si `R_N` fuese la proyección de soporte
`V_N`, actuaría como la identidad y la retención sería uno. Luego

\[
\boxed{R_N^2\neq R_N\quad\text{en general};\qquad R_4^2\neq R_4.}
\tag{5.52p}
\]

La proyección de esperanza condicional es `Q_N`, no su compresión `R_N`.

#### Límite operatorial relativo

El espectro explícito de (5.49)--(5.50) y los Teoremas 11, 14--16 dan

\[
B_N\xrightarrow{\rm SOT}I,
\qquad
A_N\xrightarrow{\rm SOT}P_{\rm sym}.
\tag{5.52q}
\]

La segunda convergencia se entiende en `mathcal H`: la forma poset converge a
la norma simétrica, los términos antisimétricos y cruzados son exactamente
nulos y la familia es uniformemente acotada.

La inversa no se pasa al límite globalmente. Sea primero el núcleo denso

\[
\mathcal D:=\bigcup_{m\ge1}P_m\widehat\otimes P_m.
\tag{5.52r}
\]

Para `h in mathcal D`, se tiene `h in mathcal S_N` para todo `N` bastante
grande y, por la convergencia explícita de cada autovalor fijo de `B_N`,

\[
\bigl(B_N|_{\mathcal S_N}\bigr)^{-1/2}h\longrightarrow h.
\tag{5.52s}
\]

Usando (5.52g), la contractividad uniforme de `A_N` y (5.52q), resulta

\[
\langle h,R_Nh\rangle\longrightarrow
\langle h,P_{\rm sym}h\rangle
\qquad(h\in\mathcal D).
\tag{5.52t}
\]

La cota `0<=R_N<=I` extiende (5.52t) por densidad a todo `mathcal H`; la
polarización da convergencia débil. Finalmente, para contracciones positivas,
un límite débil que es una proyección es automáticamente límite fuerte, pues
`R_N^2<=R_N`. Por tanto

\[
\boxed{R_N\xrightarrow{\rm SOT}P_{\rm sym}.}
\tag{5.52u}
\]

Como los `R_N` están uniformemente acotados, también `R_N^2 -> P_sym^2` en
SOT y

\[
\boxed{
(R_N-R_N^2)f\longrightarrow0
\qquad\forall f\in\mathcal H.
}
\tag{5.52v}
\]

#### Dos obstrucciones uniformes

No hay convergencia en norma. Para el vector unitario móvil

\[
h_N:=e_N\otimes e_N
\tag{5.52w}
\]

se tiene `h_N in ker B_N subseteq ker R_N`, mientras
`P_sym h_N=h_N`. Así,

\[
\boxed{
R_Nh_N=0,
\qquad
P_{\rm sym}h_N=h_N,
\qquad
\|R_N-P_{\rm sym}\|\ge1
}
\tag{5.52x}
\]

para todo `N`.

Además, en la base `e_j tensor e_k`, los autovalores positivos de `B_N` son

\[
\beta_{N,jk}
=\frac{N}{N-1}\lambda_{N-1,j}\lambda_{N-1,k},
\qquad 1\le j,k\le N-1,
\tag{5.52y}
\]

con `lambda_(n,m)` de (5.49). En particular,

\[
\beta_{N,N-1,N-1}
=\frac{N}{N-1}
\left(\frac{N!(N-1)!}{(2N-1)!}\right)^2
\longrightarrow0.
\tag{5.52z}
\]

Luego `||B_N^(dagger/2)||` no está uniformemente acotada. Esto prohíbe todo
argumento de continuidad uniforme de la inversa y separa estrictamente la
convergencia SOT ya probada de cualquier afirmación en norma. Los resultados
actuales no deciden `||R_N-R_N^2|| -> 0`; esa propiedad uniforme queda
`OPEN_NOT_NEEDED` y no se abre como objetivo.

#### Garbling por borrado y obligaciones superseded

Para los experimentos fixed-`N`, el kernel

\[
K_{N+1,N}(C,D)
:=\frac1{N+1}\#\{v\in C:[C-v]=D\}
\tag{5.52aa}
\]

está bien definido sobre clases no etiquetadas. Borrar uniformemente un punto
de una muestra iid de tamaño `N+1` deja exactamente la ley iid de tamaño `N`,
de modo que el garbling es independiente del parámetro y exacto. Ésta es una
afirmación distinta de `V_N subsetneq V_(N+1)` y de la normalización Fisher
por `N`.

Cualquier planificación anterior que presentase como próximos objetivos
«demostrar el garbling `N+1 -> N`», «demostrar idempotencia fuerte» o
«demostrar la existencia del límite proyectivo» se conserva sólo como registro
histórico y queda

```text
SUPERSEDED_BY_RELATIVE_FISHER_OPERATOR_IDENTIFICATION
```

El cierre no autoriza convergencia en norma, realizabilidad geométrica HS,
universalidad, Hauptvermutung ni reconstrucción a partir de una sola
realización. La anulación antisimétrica de primer orden mantiene exactamente
la lectura de §5.5: insensibilidad a direcciones impares bajo la isotropía que
identifica `+epsilon` con `-epsilon`, no pérdida de información física.

```text
RELATIVE_FISHER_OPERATOR_IDENTIFICATION = PROVED
RELATIVE_OPERATOR_FINITE_N_PROJECTION = REFUTED
RELATIVE_OPERATOR_SOT_LIMIT = P_SYM_PROVED
RELATIVE_ASYMPTOTIC_IDEMPOTENCE_SOT = PROVED
RELATIVE_OPERATOR_NORM_CONVERGENCE = REFUTED
RELATIVE_IDEMPOTENCE_NORM = OPEN_NOT_NEEDED
GARBLING_N_PLUS_1_TO_N = PROVED_BY_UNIFORM_DELETION
GEOMETRIC_REALIZABILITY_OF_ARBITRARY_HS = OPEN
```


### 5.5 `GEOMETRIC_ANTISYMMETRIC_REALIZABILITY_PREFLIGHT` (2026-08-30)

Se decide **sólo** la pregunta existencial: ¿existe una perturbación S1
admisible cuyo tangente estadístico no nulo esté en `wedge^2 H`? Y, si existe,
¿es una deformación geométricamente distinta módulo las equivalencias
admitidas, o su invisibilidad de primer orden la explica la isotropía discreta
`(u,v) <-> (v,u)`? **No** se caracteriza `Im P`.

#### Lema E — `P` conmuta con el intercambio de coordenadas

Sea `(R psi)(u,v):=psi(v,u)`. Con la factorización (9.2) del WP de
clasificación, `P=(I-M_u)(I-M_v)`, donde en la notación de (3.5)
`(M_u psi)(u,v)=psi_U(u)=int psi(u,v')dv'` y
`(M_v psi)(u,v)=psi_V(v)=int psi(u',v)du'`. Entonces

\[
(M_uR\psi)(u,v)=\int\psi(v',u)\,dv'=\psi_V(u)=(RM_v\psi)(u,v),
\]

y simétricamente `M_vR=RM_u`. Como `M_uM_v psi = bar psi` es constante y
`mu_0=du\,dv` es invariante bajo `R`, también `M_uM_vR=RM_uM_v`. Por tanto

\[
\boxed{
\mathcal PR
=R-RM_v-RM_u+RM_uM_v
=R\mathcal P.
}
\tag{5.53}
\]

En consecuencia `R psi=-psi` implica `R(P psi)=-P psi`: **una `psi`
antisimétrica produce un `P psi` antisimétrico**. Como
`ran P = R` tiene ambas marginales nulas (Proposición 9.1), todo `P psi`
antisimétrico no nulo está en `wedge^2 H` con `H=L_0^2`.

#### Testigo explícito

Sean `e_1,e_2` los Legendre desplazados ortonormales, ambos centrados, y

\[
\boxed{
\psi(u,v):=e_1(u)e_2(v)-e_2(u)e_1(v).
}
\tag{5.54}
\]

`psi` es un polinomio, luego `psi in C(D;R)`, que es **exactamente** la
hipótesis de S1 (§3 del WP de clasificación: "Sea `psi in C(D;R)`"). Como
`int e_1=int e_2=0`, se tiene `psi_U=psi_V=bar psi=0`, luego

\[
\mathcal P\psi=\psi\neq0,
\qquad
h_\psi=2\mathcal P\psi=2(e_1\otimes e_2-e_2\otimes e_1),
\qquad
\|h_\psi\|_{HS}^2=8.
\tag{5.55}
\]

Por (5.53), `R h_psi = -h_psi`. Por tanto

\[
\boxed{
h_\psi\in\textstyle\bigwedge^2H\setminus\{0\}.
}
\]

#### Admisibilidad S1

La única hipótesis documentada sobre el generador es `psi in C(D;R)`; **S1 no
impone ninguna simetría a `psi`**, y en particular no exige `psi(u,v)=psi(v,u)`.
La clase `psi=alpha+beta+lambda f tensor f` es la clase *de S2*, no una
restricción de admisibilidad de S1; el Lema 9.2 y el Corolario 9.3 restringen
el **objetivo** `P psi = lambda f tensor f`, no el dominio de generadores.

Con `psi` continua sobre el compacto `D`, `psi` es acotada, `Z(epsilon)` es
finita y positiva y

\[
q_\varepsilon=\frac{e^{2\varepsilon\psi}}{Z(\varepsilon)}>0
\qquad\text{para todo }\varepsilon\in\mathbb R,
\]

que es literalmente lo registrado en §3 del WP ("`q_epsilon>0` **para todo**
`varepsilon`, no sólo cerca del nulo"). Luego la familia es admisible sin
restricción de tamaño:

```text
S1_ADMISSIBILITY = SATISFIED
EPSILON_NEIGHBORHOOD_EXISTS = YES, epsilon_0 = infinity
```

#### Gauge continuo

Por la Proposición 9.1, `ker P = A = {alpha(u)+beta(v)}`. Como `P psi=psi != 0`,
`psi notin ker P`:

```text
CONTINUOUS_GAUGE_STATUS = NON_GAUGE
```

Esto dice únicamente que la dirección no es una reparametrización de
marginales. **No** autoriza a llamarla físicamente distinta; véase lo que
sigue, que es el punto central de esta sección.

#### Teorema 17 — isotropía discreta del fondo: `R^*g_\varepsilon=g_{-\varepsilon}`

`R(u,v)=(v,u)` aplica `D=[0,1]^2` en sí mismo, preserva el orden producto

\[
(u,v)\preceq(u',v')\iff u\le u',v\le v'
\]

—la condición es simétrica en las dos coordenadas—, preserva `mu_0=du\,dv`, y
es una isometría de la métrica plana `g_0`, que en coordenadas nulas es
proporcional a `du\,dv`. (Geométricamente `R` es la reflexión espacial
`x -> -x` con `u=t+x`, `v=t-x`: una isometría de Minkowski `1+1` que preserva
la orientación temporal y el diamante.)

Para `psi` antisimétrica, usando `R^*g_0=g_0` y `psi circ R=-psi`,

\[
R^*g_\varepsilon
=\frac{e^{2\varepsilon(\psi\circ R)}}{Z(\varepsilon)}\,R^*g_0
=\frac{e^{-2\varepsilon\psi}}{Z(\varepsilon)}\,g_0 .
\]

Además, como `R` preserva `mu_0`, el cambio de variables da

\[
Z(-\varepsilon)=\int_De^{-2\varepsilon\psi}d\mu_0
=\int_De^{-2\varepsilon(\psi\circ R)}d\mu_0
=\int_De^{+2\varepsilon\psi}d\mu_0=Z(\varepsilon),
\]

es decir `Z` es **par** en `epsilon`. Por tanto

\[
\boxed{
R^*g_\varepsilon=g_{-\varepsilon}
\qquad\text{exactamente, para todo }\varepsilon\in\mathbb R.
}
\tag{5.56}
\]

**Consecuencia sobre las leyes.** `R` es un automorfismo de `(D,preceq)` que
transporta `mu_epsilon` a `mu_(-epsilon)`. Como el causet no etiquetado sólo
registra el orden, la ley del poset no etiquetado es invariante bajo `R` por
construcción — esto no es un convenio del programa, es forzado. Luego

\[
\mathbb P_{\varepsilon}\bigl([P]=C\bigr)
=\mathbb P_{-\varepsilon}\bigl([P]=C\bigr)
\qquad\forall N,C,\varepsilon,
\tag{5.57}
\]

la ley del poset es **exactamente par** en `epsilon`, y su derivada en
`epsilon=0` se anula necesariamente. Ésa es la explicación geométrica de
`E[S_N(f_a)|[P]]=0`: no es una coincidencia combinatoria de la fibra, es la
paridad forzada por una isometría del fondo.

En cambio, `R` **no** deja invariante la ley de rangos: intercambiar `u` y `v`
sustituye la permutación de rangos `pi` por `pi^(-1)`, de modo que

\[
\mathbb P_{-\varepsilon}(\Pi_N=\pi)
=\mathbb P_{\varepsilon}(\Pi_N=\pi^{-1}),
\tag{5.58}
\]

que es un cambio genuino salvo en las involuciones. De ahí que
`I_N^Pi(f_a)>0` mientras `I_N^[P](f_a)=0`, sin contradicción. (5.57)--(5.58)
son la versión geométrica del mecanismo de fibra del Teorema 14.

#### Veredicto y las cuatro nociones que NO deben identificarse

```text
GEOMETRIC_ANTISYMMETRIC_REALIZABILITY =
    REALIZABLE_BUT_DISCRETE_ISOTROPY_IDENTIFIED
```

El testigo (5.54) es admisible, su tangente es antisimétrico no nulo y no es
gauge continuo; pero `g_epsilon` y `g_(-epsilon)` son **isométricas** vía `R`,
y esa isometría es una equivalencia forzada para el canal `[P]`. Se mantienen
separadas:

1. **Gauge infinitesimal generado por un campo vectorial** — `ker P`. El
   testigo NO es de este tipo.
2. **Isotropía discreta del punto base** — `R` es una isometría de
   `(D,g_0,preceq,mu_0)`. SÍ está presente.
3. **Isometría de `g_epsilon` y `g_(-epsilon)`** — (5.56). SÍ, exacta.
4. **Invisibilidad Fisher de primer orden** — se SIGUE de (3) por (5.57).

(3) implica (4); (4) no implica (3) en general. Aquí se tiene (3), de modo que
(4) queda explicada y no requiere ninguna lectura de pérdida física.

**Lo que NO se sigue.** La familia no es trivial: `g_epsilon != g_0` para
`epsilon != 0`, y nada de lo anterior dice que `g_epsilon` sea isométrica a
`g_0`. Lo identificado es el **signo** de `epsilon`, no la deformación. En el
cociente por isometrías la curva `epsilon -> [g_epsilon]` se pliega sobre sí
misma en `epsilon=0`, y por eso el Fisher de primer orden en el canal `[P]`
debe anularse. Puede existir identificabilidad de orden superior en
`|epsilon|`; **ese problema no se abre en esta sección**, y queda resuelto en
§5.6: la ley del poset sí cambia a orden `epsilon^2`, ya con `N=2`.

```text
HIGHER_ORDER_IDENTIFIABILITY_IN_ABS_EPSILON = PROVED_SECOND_ORDER_VISIBLE (§5.6)
```

#### Reinterpretación obligatoria del teorema mixto

`MIXED_SECTOR_LIMIT = PROVED_NORM_RATIO` (5.52) **no** debe leerse como
pérdida de información geométrica física. La lectura correcta es:

> la ley del poset no etiquetado es insensible, a primer orden, a las
> direcciones impares bajo la isotropía discreta del fondo.

Queda **prohibida** en cualquier redacción la expresión *physical information
loss* aplicada a `wedge^2 H`, y en particular la lectura de que una
deformación métrica con parte antisimétrica "pierde esa fracción de su
información". La fracción `||f_a||^2/(||f_s||^2+||f_a||^2)` mide la parte del
tangente que es odd bajo `R`, no información física destruida.

#### Ataque adversarial — resultado

1. *¿`psi` antisimétrica permitida?* Sí: la hipótesis documentada es
   `psi in C(D;R)`, sin simetría. Verificado en la fuente, no asumido.
2. *¿`h_psi != 0`?* Sí, `||h_psi||_HS^2=8` por cálculo exacto.
3. *¿Familia admisible para `epsilon != 0`?* Sí, `q_epsilon>0` para todo
   `epsilon`, documentado; `epsilon_0=infinity`.
4. *¿Tangente non-gauge?* Sí, `psi notin ker P`.
5. *¿`R^*g_epsilon=g_(-epsilon)`?* Derivado en el Teorema 17, incluida la
   paridad de `Z`, no asumido.
6. *¿`R` equivalencia admitida?* Sí, y por una razón que no depende de
   convenios: `R` preserva `preceq` y `mu_0`, luego la ley del causet no
   etiquetado es invariante por construcción.
7. *¿Salto de non-gauge a físicamente distinto?* **BLOQUEADO. Éste era el
   error a evitar y es el resultado de la sección:** non-gauge en el sentido
   de `ker P` no implica geométricamente distinto módulo las equivalencias
   admitidas, porque la isotropía discreta identifica `+epsilon` con
   `-epsilon`.

No se usó en ningún paso la clasificación Fisher como prueba de realizabilidad
geométrica; la dirección del argumento es la contraria.

```text
FULL_WEDGE_REALIZABILITY_PROVED = NO
GEOMETRIC_TANGENT_REALIZABILITY = NOT_FULLY_OPENED
```

Un solo testigo decide la pregunta existencial; no se caracteriza `Im P` ni se
afirma que todo `wedge^2 H` sea realizable.


### 5.6 `HIGHER_ORDER_IDENTIFIABILITY_IN_ABS_EPSILON_PREFLIGHT` (2026-08-30)

Se trabaja **exclusivamente** con el witness (5.54). No se abre `wedge^2 H`.

#### Fórmula finita exacta de la ley de rangos

No hace falta la expansión de la cópula a segundo orden. Para `N` puntos iid de
`mu_epsilon`, ordenando cada coordenada, el suceso `{Pi_N=pi}` es exactamente
el de que el punto de `u`-rango `i` tenga `v`-rango `pi(i)`, luego

\[
p_\pi(\varepsilon):=\mathbb P_\varepsilon(\Pi_N=\pi)
=N!\int_\Delta\!\!\int_\Delta\prod_{i=1}^Nq_\varepsilon(u_i,v_{\pi(i)})\,dv\,du,
\qquad
\Delta=\{0<t_1<\dots<t_N<1\}.
\tag{5.59}
\]

Con `q_epsilon=e^{2 epsilon psi}/Z(epsilon)` y
`T_pi:=sum_i psi(u_i,v_(pi(i)))`, y escribiendo `<.>` para la esperanza bajo
dos familias independientes de estadísticos de orden uniformes (densidad `N!`
sobre `Delta` en cada coordenada), (5.59) se reduce a

\[
\boxed{
p_\pi(\varepsilon)
=\frac{\bigl\langle e^{2\varepsilon T_\pi}\bigr\rangle}
        {N!\,Z(\varepsilon)^N}.
}
\tag{5.60}
\]

En `epsilon=0` da `1/N!`, la ley uniforme del nulo.

#### Lema F — regularidad

`psi` es continua sobre el compacto `D`, luego acotada por `M:=||psi||_inf`.
Entonces `|T_pi|<=NM` y, para `|epsilon|<=r`,

\[
\Bigl|\partial_\varepsilon^k e^{2\varepsilon T_\pi}\Bigr|
\le(2NM)^k e^{2rNM},
\]

una cota constante e integrable sobre el dominio de medida finita
`Delta x Delta`. Por convergencia dominada se puede derivar bajo la integral a
todo orden, y lo mismo vale para `Z(epsilon)`, que además no se anula. Por
tanto `p_pi` es **real-analítica** en `epsilon`, no sólo `C^2`. La hipótesis
usada es exactamente la de S1, `psi in C(D;R)`; no se requiere nada más.

```text
SECOND_ORDER_REGULARITY = REAL_ANALYTIC (stronger than C^2)
```

#### Teorema 18 — derivadas primera y segunda exactas

Con `bar psi=0` para el witness, `Z(epsilon)=1+2 epsilon^2 sigma^2+O(epsilon^4)`,
`sigma^2:=int_D psi^2 d mu_0`. Sustituyendo en (5.60),

\[
N!\,p_\pi(\varepsilon)
=1+2\varepsilon\langle T_\pi\rangle
+2\varepsilon^2\bigl(\langle T_\pi^2\rangle-N\sigma^2\bigr)+O(\varepsilon^3),
\]

de donde

\[
\boxed{
p_\pi'(0)=\frac{2}{N!}\langle T_\pi\rangle,
\qquad
p_\pi''(0)=\frac{4}{N!}\bigl(\langle T_\pi^2\rangle-N\sigma^2\bigr).
}
\tag{5.61}
\]

La primera es consistente con lo ya congelado: por independencia de los
estadísticos de orden en las dos coordenadas,
`<T_pi> = sum_i H^(N)_(i,pi(i))(psi)` con `H^(N)` de (5.33), luego
`N! p_pi'(0) = 2 sum_i H_(i,pi(i))(P psi) = S_N(P psi)`, el score de (5.34).

#### Paridad, re-derivada dentro de este cálculo

Por antisimetría, `sum_i psi(u_i,v_(pi(i))) = -sum_j psi(v_j,u_(pi^(-1)(j)))`;
renombrando las variables mudas de integración (ambas recorren `Delta`) en
(5.59)--(5.60) y usando `Z(-epsilon)=Z(epsilon)`,

\[
p_\pi(-\varepsilon)=p_{\pi^{-1}}(\varepsilon),
\tag{5.62}
\]

que es (5.58). Como cada fibra `Gamma_C` es cerrada bajo inversión
(Teorema 14), `p_C(-epsilon)=p_C(epsilon)`, luego `p_C'(0)=0` y la expansión
empieza en orden par:

\[
p_C(\varepsilon)=p_C(0)+\tfrac12p_C''(0)\varepsilon^2+O(\varepsilon^4).
\tag{5.63}
\]

```text
PARITY_REVERIFIED = YES, independently inside this computation
```

#### Mecanismo: `psi^2` es simétrica

La parte diagonal de `<T_pi^2>` es

\[
\sum_i\bigl\langle\psi(U_{(i)},V_{(\pi(i))})^2\bigr\rangle
=\sum_iH^{(N)}_{i,\pi(i)}(\psi^2),
\]

la matriz del kernel `psi^2`. Y para `psi` antisimétrica
`psi^2(v,u)=(-psi(u,v))^2=psi^2(u,v)`: **`psi^2` es simétrica**. Lo mismo se ve
en la densidad, cuyo término de orden dos es
`2 epsilon^2(psi^2-sigma^2)`, simétrico. Su proyección de interacción no se
anula:

\[
\mathcal P(\psi^2)\neq0,
\qquad
\|\mathcal P(\psi^2)\|_{HS}^2=\tfrac{3028}{245}.
\tag{5.64}
\]

Es decir: la deformación de orden `epsilon^2` vive en el sector **simétrico**,
justo el de retención asintótica total (Teorema 12). Ésa es la razón
estructural por la que cabe esperar señal a segundo orden, y por la que la
invisibilidad no puede ser permanente. (5.64) no afirma que el tangente de
cópula de segundo orden sea `2 P(psi^2)`; esa expansión no se calcula aquí y no
se necesita.

#### Teorema 19 — visibilidad de segundo orden ya en `N=2`

Todos los números salen del backend determinista
`dev/wp6_second_order_antisymmetric_witness.py`, con asertos internos para
`sum_pi p'(0)=0`, `sum_pi p''(0)=0`, `p'_pi(0)=-p'_(pi^(-1))(0)` y `p_C'(0)=0`.

Para `N=2`, con `sigma^2=2` y las dos clases de dos elementos:

\[
\boxed{
p''_{\rm anticadena}(0)=+\tfrac85,
\qquad
p''_{\rm cadena}(0)=-\tfrac85,
}
\qquad
p_C(0)=\tfrac12\ \text{ambas},
\tag{5.65}
\]

y `sum_C p_C''(0)=0` exactamente. Como `N=2` es la menor cardinalidad con más
de una clase, el `N` mínimo con señal de segundo orden es el mínimo posible:

```text
MINIMAL_N_WITH_SECOND_ORDER_SIGNAL = 2
```

Para `N=3` las cinco clases dan
`48/35, 64/35, -52/35, -52/35, -8/35`, de nuevo con suma cero y todas no nulas.

Esto **prueba** el enunciado existencial: (5.59)--(5.61) son analíticas y la
evaluación en `N=2` es una integral exacta de un polinomio sobre un
2-símplex, en aritmética racional. No es evidencia numérica de un enunciado
asintótico; es el cálculo cerrado de una cantidad finita.

\[
\boxed{
\exists\,N,C:\quad
\left.\frac{d^2}{d\varepsilon^2}
\mathbb P_\varepsilon([P_N]=C)\right|_0\neq0.
}
\]

Interpretación de (5.65): a segundo orden el witness antisimétrico **aumenta**
la probabilidad de la anticadena y **disminuye** la de la cadena. El poset ve
la magnitud de la deformación; el signo sigue cocientado por la isotropía.

#### Consecuencia: identificabilidad local en `|epsilon|`

De (5.63) y (5.65), para `0<|epsilon|` suficientemente pequeño,

\[
\boxed{
P_\varepsilon^{[P]}\neq P_0^{[P]}
\qquad\text{ya a }N=2.
}
\tag{5.66}
\]

```text
HIGHER_ORDER_IDENTIFIABILITY_IN_ABS_EPSILON = PROVED_SECOND_ORDER_VISIBLE
ABS_EPSILON_LOCALLY_VISIBLE = YES
SIGN_IDENTIFIABLE = NO
```

**Lo que NO se afirma.** No se afirma reconstrucción de `|epsilon|` a partir de
una sola muestra, ni consistencia de ningún estimador, ni tasa, ni nada sobre
la Hauptvermutung. (5.66) es separación de leyes a `N` fijo, nada más.

#### Parámetro `theta=epsilon^2`

Como `p_C` es par y real-analítica, `p_C(epsilon)=g_C(epsilon^2)` con `g_C`
real-analítica en un entorno de `0`, y

\[
\left.\frac{d}{d\theta}\mathbb P_\theta([P_N]=C)\right|_{0^+}
=\tfrac12p_C''(0),
\tag{5.67}
\]

no nula por (5.65). La derivada existe como **derivada por la derecha**:
`theta=0` es un punto de **frontera** del modelo `{P_theta : theta>=0}`.

```text
THETA_EQUALS_EPSILON_SQUARED_BOUNDARY_DERIVATIVE = EXISTS, = (1/2) p_C''(0) != 0
ABS_EPSILON_BOUNDARY_SCORE = DEFINED_AS_ONE_SIDED_DERIVATIVE
```

**No** se declara el modelo QMD regular en `theta=0`, ni se invoca LAN ni
eficiencia asintótica: son enunciados de frontera y requieren su propio
tratamiento. El siguiente lema concreto, cerrado separadamente en §5.7, es la
validez **unilateral de QMD** en `theta=0^+`. LAN no forma parte de ese lema.

#### Hellinger de segundo orden

Con la convención del repositorio `H^2(p,q)=int(sqrt p-sqrt q)^2` sin factor
`1/2` (`wp6_domain_bridge_fixed_ef_box.md:119`,
`manuscript_limits_draft.md:594`), de (5.63),

\[
H^2\bigl(P_\varepsilon^{[P]},P_0^{[P]}\bigr)
=K_N\varepsilon^4+o(\varepsilon^4),
\qquad
K_N=\sum_C\frac{p_C''(0)^2}{16\,p_C(0)}.
\tag{5.68}
\]

El backend evalúa y asevera `K_N>0`:

\[
K_2=\tfrac{16}{25},
\qquad
K_3=\tfrac{3684}{1225}.
\tag{5.69}
\]

La escala `epsilon^4` no se impuso: se sigue de la paridad más `p_C''(0)!=0`.

#### Corrección del techo de claims

`PERMANENT_FIRST_ORDER_INVISIBILITY` sigue siendo correcto y **conserva
obligatoriamente el calificativo `FIRST_ORDER`**. Queda prohibido escribir
"permanent invisibility" a secas para el witness: la ley del poset sí cambia,
a orden `epsilon^2`, ya con dos elementos. La formulación correcta es

> primer orden invisible, localmente visible en `|epsilon|`.

Sigue prohibido, por §5.5, llamar a esto *physical information loss*.


### 5.7 `ONE_SIDED_QMD_IN_THETA` (2026-08-30)

Esta sección cierra únicamente la regularidad cuadrática lateral del modelo
finito reparametrizado. Fijemos \(N\) y sea \(\mathcal Y_N\) la imagen finita
del canal de clases de posets realizables por permutaciones. Escribimos

\[
g_C(\theta):=p_C(\sqrt\theta),\qquad \theta\in[0,\infty),
\qquad C\in\mathcal Y_N.
\tag{5.70}
\]

Por la paridad y analiticidad real probadas en §5.6, cada \(p_C\) tiene una
serie local sólo en potencias pares. Por tanto existe una función analítica
local de la variable \(\theta\), también denotada \(g_C\), tal que

\[
g_C(\theta)
=p_C(0)+a_C\theta+O(\theta^2),
\qquad
a_C=g_C'(0^+)=\tfrac12p_C''(0).
\tag{5.71}
\]

No aparece aquí ningún problema de soporte nulo. En el nulo, la ley de
permutaciones es uniforme y, para cada clase de la imagen,

\[
p_C(0)=\frac{|\Gamma_C|}{N!}>0.
\tag{5.72}
\]

#### Definición lateral usada

Diremos que el modelo es **QMD unilateral en \(0^+\)** si existe
\(\dot\ell^{(+)}_N\in L^2(P_0^{[P]})\) tal que, cuando
\(\theta\downarrow0\),

\[
\sum_{C\in\mathcal Y_N}
\left[
\sqrt{g_C(\theta)}-\sqrt{g_C(0)}
-\frac{\theta}{2}\dot\ell^{(+)}_N(C)\sqrt{g_C(0)}
\right]^2
=o(\theta^2).
\tag{5.73}
\]

La palabra *unilateral* es parte del enunciado: la aproximación se toma en el
cono tangente admisible \(h\ge0\), no en un entorno abierto de cero.

#### Teorema 20 — QMD unilateral y su información

Para cada \(N\) fijo, la familia
\(\{P_\theta^{[P]}:\theta\ge0\}\) es QMD unilateral en \(0^+\), con

\[
\boxed{
\dot\ell_N^{(+)}(C)
=\frac{a_C}{p_C(0)}
=\frac{p_C''(0)}{2p_C(0)}.
}
\tag{5.74}
\]

Su media bajo el nulo es cero y la norma cuadrática del score lateral es

\[
\boxed{
I_{N,\theta}^{(+)}
:=\sum_{C\in\mathcal Y_N}p_C(0)
       \bigl(\dot\ell_N^{(+)}(C)\bigr)^2
=\sum_{C\in\mathcal Y_N}\frac{p_C''(0)^2}{4p_C(0)}
=4K_N.
}
\tag{5.75}
\]

**Prueba.** Por (5.71)--(5.72), la regla de la cadena para la raíz cuadrada da,
para cada \(C\),

\[
\sqrt{g_C(\theta)}
=\sqrt{p_C(0)}
+\frac{a_C}{2\sqrt{p_C(0)}}\,\theta
+O_C(\theta^2).
\tag{5.76}
\]

Al sustituir (5.74), el término lineal de (5.73) coincide exactamente con el
de (5.76). Como \(\mathcal Y_N\) es finito, la suma de los cuadrados de los
restos es \(O(\theta^4)=o(\theta^2)\). Esto prueba (5.73). Además,
la normalización \(\sum_Cg_C(\theta)=1\) implica

\[
\mathbb E_0\dot\ell_N^{(+)}
=\sum_Cp_C(0)\dot\ell_N^{(+)}(C)
=\sum_Ca_C
=0.
\tag{5.77}
\]

Finalmente, la primera igualdad de (5.75) es la norma \(L^2(P_0)\) del score;
las otras dos siguen de \(a_C=p_C''(0)/2\) y de la definición de \(K_N\) en
(5.68). \(\square\)

#### Hellinger y valores exactos

Con la convención sin factor \(1/2\) del repositorio, (5.73) da

\[
\boxed{
H^2(P_\theta^{[P]},P_0^{[P]})
=\frac14I_{N,\theta}^{(+)}\theta^2+o(\theta^2)
=K_N\theta^2+o(\theta^2).
}
\tag{5.78}
\]

Como \(\theta=\varepsilon^2\), (5.78) es exactamente (5.68), no una nueva
aproximación. El backend
`dev/wp6_second_order_antisymmetric_witness.py` calcula y asevera, en
aritmética exacta, el centrado (5.77) y \(I_{N,\theta}^{(+)}=4K_N\). En
particular,

\[
\boxed{
I_{2,\theta}^{(+)}=\frac{64}{25},
\qquad
I_{3,\theta}^{(+)}=\frac{14736}{1225}.
}
\tag{5.79}
\]

Para \(N=2\), el score lateral vale \(+8/5\) en la anticadena y \(-8/5\) en
la cadena. Así, el alfabeto causal no sólo separa \(\theta>0\) del nulo: su
primer contraste no trivial ya está presente en el causet más pequeño que
dispone de dos tipos de orden.

#### Lectura geométrica y techo de claims

La anulación en la coordenada \(\varepsilon\) era el pliegue de una órbita por
la reflexión, no la desaparición de la deformación. La coordenada
\(\theta=\varepsilon^2\) describe localmente la semirrecta de órbitas y hace
lineal la primera variación observable:

\[
\begin{array}{ccl}
\varepsilon &:& I_N^{[P]}(0)=0,\\
|\varepsilon| &:& \text{magnitud geométricamente relevante},\\
\theta=\varepsilon^2 &:& \dot\ell_N^{(+)}\ne0,\\
H^2 &:& \asymp\varepsilon^4=\theta^2.
\end{array}
\tag{5.80}
\]

Esto no convierte \(0\) en un punto interior. No se extiende el modelo a
\(\theta<0\), no se declara LAN bilateral, no se identifica un experimento
asintótico de frontera y no se deducen eficiencia, estimadores ni tasas. La
afirmación probada es exactamente (5.73), para cada \(N\) fijo.

```text
ONE_SIDED_QMD_IN_THETA = PROVED_FOR_EACH_FIXED_N
THETA_PARAMETER_SPACE = [0,+infinity); ZERO_IS_BOUNDARY
THETA_ZERO = BOUNDARY_POINT
THETA_RIGHT_SCORE = p_C''(0) / (2 p_C(0)); CENTERED_UNDER_P0
THETA_ONE_SIDED_INFORMATION = 4 K_N > 0
    I_2 = 64/25; I_3 = 14736/1225
HELLINGER_IN_THETA = (1/4) I_{N,theta}^{(+)} theta^2 + o(theta^2)
INTERIOR_QMD_AT_THETA_ZERO = NOT_CLAIMED
BILATERAL_LAN_AT_THETA_ZERO = NOT_CLAIMED
BOUNDARY_ASYMPTOTIC_EXPERIMENT = NOT_OPENED
```


### 5.8 `POISSON_ORDER_PLUS_NUMBER_BRIDGE` (2026-08-30)

El contrato nuevo queda desarrollado en
[WP6 — Puente Poisson order+number](../research_program/work_packages/wp6_poisson_order_number_bridge.md).
La primera obligación es separar dos mecanismos que el nombre del canal puede
ocultar.

Para una familia de volumen \(V_t\), densidad conocida \(\rho\),
\(\lambda_t=\rho V_t\), y ley condicional \(p_{t,n,C}\) del poset dado
\(N=n\), la ley conjunta factoriza exactamente como

\[
Q_t(n,C)
=e^{-\lambda_t}\frac{\lambda_t^n}{n!}\,p_{t,n,C}.
\tag{5.81}
\]

Cuando existen los scores y la serie es sumable, (5.81) da la descomposición
ortogonal

\[
\boxed{
I^{\mathrm{ord+num}}(t_0)
=\frac{(\lambda_{t_0}')^2}{\lambda_{t_0}}
+\mathbb E_{N\sim\operatorname{Pois}(\lambda_{t_0})}
 I_N^{[P]}(t_0).
}
\tag{5.82}
\]

El primer sumando es información de número; el segundo, información de orden
condicionada al número observado.

#### El witness S1 normalizado

En S1, la división por \(Z(\varepsilon)\) conserva exactamente el volumen:
\(V_\varepsilon=V_0\). Por tanto \(N\) es **ancilar** para \(\varepsilon\) y
\(\theta\); aquí order+number no añade una señal de cardinalidad. Sin embargo,
la mezcla Poisson conserva la señal de los experimentos condicionales.

La cota \(|T_\pi|\le N\|\psi\|_\infty\) y la fórmula (5.61) dan

\[
\left|\dot\ell_N^{(+)}(C)\right|
\le2\left(N^2\|\psi\|_\infty^2+N\sigma^2\right),
\qquad
I_{N,\theta}^{(+)}=O(N^4).
\tag{5.83}
\]

Los momentos exponenciales de Poisson dominan también el resto de la expansión
de raíces, no sólo el score. El WP prueba así QMD unilateral de la mezcla y

\[
\boxed{
I_{\mathrm{Pois},\theta}^{(+)}
=\mathbb E_{\operatorname{Pois}(\lambda)}
  I_{N,\theta}^{(+)}
\ge\frac{32}{25}e^{-\lambda}\lambda^2>0.
}
\tag{5.84}
\]

La última desigualdad usa únicamente el suceso \(N=2\) y (5.79).

#### La órbita de escala

Si las leyes condicionadas \(p_{t,n,C}\) son idénticas pero \(V_t\) cambia,
la razón de verosimilitudes depende sólo de \(N\). En esa subfamilia la
cardinalidad es suficiente y

\[
H^2(\operatorname{Pois}(\lambda),\operatorname{Pois}(\mu))
=2\left[
1-\exp\!\left\{-\frac12(\sqrt\lambda-\sqrt\mu)^2\right\}
\right],
\qquad
I^{\mathrm{number}}(t_0)
=\frac{(\lambda_{t_0}')^2}{\lambda_{t_0}}.
\tag{5.85}
\]

Éste es el sentido preciso en que número restaura escala a \(\rho\) conocida.
No debe trasladarse al witness S1 normalizado, donde \(\lambda\) es constante.

~~~text
POISSON_ORDER_NUMBER_BRIDGE = PROVED_IN_CURRENT_SCOPE
JOINT_LAW_FACTORIZATION = EXACT
NUMBER_PLUS_CONDITIONAL_ORDER_FISHER_SPLITTING = PROVED_ORTHOGONAL
NORMALIZED_S1_N_ANCILLARY = YES
NORMALIZED_S1_POISSON_ONE_SIDED_QMD_IN_THETA = PROVED
NORMALIZED_S1_I_POIS_THETA >= (32/25) exp(-lambda) lambda^2 > 0
SCALE_ORBIT_WITH_KNOWN_RHO = EXACTLY_SEPARATED_BY_N
NUMBER_SUFFICIENT_FOR_SCALE = EXACT
UNKNOWN_RHO_SCALE_IDENTIFIABILITY = NOT_CLAIMED
SINGLE_REALIZATION_RECONSTRUCTION = NOT_CLAIMED
HAUPTVERMUTUNG = NOT_CLAIMED
~~~


Para el sector mixto, §5.4 promueve ya la fórmula de razón de normas (5.52)
en el nivel hilbertiano, con separación exacta de sectores a todo `N`.
Permanece:

```text
FINITE_RANK_BOUNDED_CONTINUOUS_SYMMETRIC_RETENTION = PROVED_BY_ASSEMBLY
L2_ORDER_STATISTIC_FOURTH_MOMENT_LEMMA = PROVED
FINITE_RANK_SYMMETRIC_RETENTION = PROVED
INFINITE_RANK_SYMMETRIC_RETENTION_PREFLIGHT = PASS_HS_UNIFORM_CONTINUITY
INFINITE_RANK_SYMMETRIC_RETENTION = PROVED
FULL_SYMMETRIC_HS_RETENTION = PROVED
THEOREM_HILBERT = PROVED
GEOMETRIC_REALIZABILITY_OF_ARBITRARY_HS = OPEN
RELATIVE_FISHER_OPERATOR_IDENTIFICATION = PROVED
RELATIVE_OPERATOR_FINITE_N_PROJECTION = REFUTED
RELATIVE_OPERATOR_SOT_LIMIT = P_SYM_PROVED
RELATIVE_ASYMPTOTIC_IDEMPOTENCE_SOT = PROVED
RELATIVE_OPERATOR_NORM_CONVERGENCE = REFUTED
RELATIVE_IDEMPOTENCE_NORM = OPEN_NOT_NEEDED
GARBLING_N_PLUS_1_TO_N = PROVED_BY_UNIFORM_DELETION
TRACE_CLASS_RESTRICTION = REMOVED
RATE = o_f(1)_NO_UNIFORM_RATE_CLAIMED
KER_B_N = mathcal S_N^perp; mathcal S_N = P_(N-1) widehat tensor P_(N-1)
ETA_ZERO_OVER_ZERO_IFF = f in ker B_N = mathcal S_N^perp
ETA_WELL_DEFINED_FOR = N >= N_0(f) for each f != 0
VISIBLE_ANTISYMMETRIC_FINITE_N = 0 != f in wedge^2 P_(N-1) subset V_N^perp
    but f notin ker B_N; I_N^Pi(f)>0, I_N^[P](f)=0, eta_N(f)=0
N_0_UNIFORM_OVER_HS_SPHERE = NO
ANTISYMMETRIC_SECTOR = EXACTLY_INVISIBLE_IN_[P]_FOR_ALL_N (6.7)
FIRST_LEGENDRE_MODE_EXACT_POSET_SUFFICIENCY = PROVED
DIM_V_N = binom(N,2) = rank G_[P]^(N)   [Teorema 1, (1.3)]
BEST_BOUND_USED = 4N/(N-1), sup = 8 at N=2 (from the PROVED ||T_N||<=sqrt N)
ORDER_STATISTIC_MEAN_ZERO_NORM = PROVED_EXACT
SHARP_CONSTANT_ON_H = ||T_N|_H||^2 = N(N-1)/(N+1) for all N>=2, PROVED (Lema B')
    mechanism: T_N^* T_N = N * M_{N-1}, Bernstein-Durrmeyer; shifted Legendre
    eigenfunctions, eigenvalues lambda_{n,m} = (n+1)!n!/((n+m+1)!(n-m)!)
    strictly decreasing; extremiser e_1 ~ t-1/2, simple
NORMALIZED_LOSS_BOUND = VALID, SHARPNESS_OPEN
    Delta_N/N <= 4N(N-1)/(N+1)^2 ||f||_HS^2 < 4 (5.37d), but the extremiser of
    the right-hand side is e_1^ox2, where Delta_N = 0 exactly; the chain is
    maximally slack there. sup_f Delta_N(f,f)/(N ||f||_HS^2) NOT DETERMINED.
REFERENCE_FISHER_HS_BOUND = SHARP; equality at e_1^ox2 for every N>=2 (5.37e)
UNIFORM_CONSTANT = 4 for the reference Fisher; best possible, not attained
E1_DOUBLE_ROLE = OBSERVATION_ONLY, no principle and no physical reading
RATE_IMPROVED = NO (Theorems 9-12 unchanged, still on the sqrt N bound)
R_CONTROL = NOT_REQUIRED_AT_INFINITE_RANK
R_CONTROL_LEGACY_5_10 = TRACE_NORM_TYPE_WEIGHTED_BY_PROFILE_SUP_NORMS_BYPASSED
UNIFORM_CONTROL_NORM = HILBERT_SCHMIDT_SCHATTEN_2
TRACE_NORM_REQUIRED = NO
HS_UNIFORM_OPERATOR_BOUND = sup_N ||Delta_N/N||_op <= 8
EXACT_HS_CONSTANT = 4N/(N-1) <= 8 for N>=2, -> 4
REFERENCE_FISHER_HS_BOUND = I_N^Pi(f) <= (4N/(N-1)) N ||f||_HS^2
REFERENCE_FISHER_HS_LIMIT = I_N^Pi(f)/N -> 4||f||_HS^2
L2_FINITE_RANK_RATE = o_f(1)_WITHOUT_UNIVERSAL_RATE
HS_RATE = o_f(1)_WITHOUT_UNIVERSAL_RATE
FULL_SYMMETRIC_S1_FISHER_RETENTION_PREFLIGHT = PASS_FINITE_RANK_NEW_LEMMA_IDENTIFIED
FIRST_MISSING_LEMMA = NONE
ADVERSARIAL_SEQUENCE = NONEXISTENT_BY_(5.39)
HS_UNIFORMITY_OBSTRUCTION = NONE
FIRST_LEGENDRE_MODE_EXACT_SUFFICIENCY_PRESERVED = YES
INFINITE_RANK_EXTENSION_STATUS = CLOSED_SYMMETRIC_SECTOR_ONLY
MIXED_SECTOR_PREFLIGHT = PASS_EXACT_ORTHOGONAL_SPLITTING
MIXED_SECTOR_LIMIT = PROVED_NORM_RATIO   (was CONJECTURE; §5.4 Teorema 16)
SECTOR_MIXED = OPENED_HILBERT_LEVEL_ONLY
REFERENCE_FISHER_SYM_ANTI_CROSS = 0 exactly, all N (5.44)
POSET_FISHER_SYM_ANTI_CROSS = 0 exactly, all N (5.46)-(5.47)
REFERENCE_FISHER_SPLITTING = I_N^Pi(f) = I_N^Pi(f_s) + I_N^Pi(f_a) (5.45)
POSET_FISHER_SPLITTING = I_N^[P](f) = I_N^[P](f_s) (5.48)
ANTISYMMETRIC_REFERENCE_FISHER_LIMIT = I_N^Pi(f_a)/N -> 4||f_a||_HS^2 (5.51)
PURE_ANTISYMMETRIC_CASE = eta_N = 0 EXACTLY for N >= N_0(f), not only in limit
INTERACTION_FOUND = NO
GEOMETRIC_ANTISYMMETRIC_REALIZABILITY = REALIZABLE_BUT_DISCRETE_ISOTROPY_IDENTIFIED
    witness psi = e_1 ox e_2 - e_2 ox e_1 (5.54); admissible, eps_0 = infinity;
    h_psi in wedge^2 H \ {0}, ||h_psi||_HS^2 = 8; NON_GAUGE (psi notin ker P)
BACKGROUND_SWAP_ISOMETRY = YES, R preserves D, the product order, mu_0 and g_0
R_PULLBACK_G_EPSILON = R^* g_eps = g_{-eps} exactly, all eps (5.56)
DISCRETE_ISOTROPY_STATUS = IDENTIFIES +eps WITH -eps; poset law exactly even
ANTISYMMETRIC_FISHER_KERNEL_INTERPRETATION =
    first-order insensitivity to R-odd directions, NOT physical information loss
PHYSICAL_INFORMATION_LOSS_WORDING = FORBIDDEN for wedge^2 H
HIGHER_ORDER_IDENTIFIABILITY_IN_ABS_EPSILON = PROVED_SECOND_ORDER_VISIBLE
    minimal N = 2; p''_antichain(0) = +8/5, p''_chain(0) = -8/5 (5.65)
    H^2(P_eps,P_0) = K_N eps^4 + o(eps^4); K_2 = 16/25, K_3 = 3684/1225 (5.69)
    mechanism: psi^2 is SYMMETRIC and P(psi^2) != 0, ||P(psi^2)||_HS^2 = 3028/245
ABS_EPSILON_LOCALLY_VISIBLE = YES
SIGN_IDENTIFIABLE = NO
ABS_EPSILON_BOUNDARY_SCORE = DEFINED_AS_ONE_SIDED_DERIVATIVE (theta = eps^2)
ONE_SIDED_QMD_IN_THETA = PROVED_FOR_EACH_FIXED_N (§5.7)
THETA_ONE_SIDED_INFORMATION = 4 K_N; I_2 = 64/25; I_3 = 14736/1225
THETA_ZERO = BOUNDARY_POINT
INTERIOR_QMD_AT_THETA_ZERO = NOT_CLAIMED
BILATERAL_LAN_AT_THETA_ZERO = NOT_CLAIMED
PERMANENT_INVISIBILITY_WORDING = FORBIDDEN without the FIRST_ORDER qualifier
SINGLE_SAMPLE_RECONSTRUCTION_CLAIMED = NO
HAUPTVERMUTUNG_CLAIMED = NO
LOCAL_METRIC_RECONSTRUCTION = NOT_CLAIMED
FULL_WEDGE_REALIZABILITY_PROVED = NO
GEOMETRIC_TANGENT_REALIZABILITY = NOT_FULLY_OPENED
N5_FISHER_SPECTRUM = NOT_OPENED
EF = NOT_OPENED
POISSON_ORDER_NUMBER_BRIDGE = PROVED_IN_CURRENT_SCOPE (§5.8)
NORMALIZED_S1_N_ANCILLARY = YES
NORMALIZED_S1_POISSON_ONE_SIDED_QMD_IN_THETA = PROVED
SCALE_ORBIT_WITH_KNOWN_RHO = EXACTLY_SEPARATED_BY_N
NUMBER_SUFFICIENT_FOR_SCALE = EXACT
FISHER_LOCALISATION_OPENED = NO
DIMENSION_2PLUS1 = NOT_OPENED
KERR = NOT_OPENED
NEXT_RUN_AUTHORIZED = NO
```

## 6. Fase S5 — clasificar la información que sí se pierde

> **SUPERSEDED_BY_§5.4–§5.6.** El texto de esta sección se conserva como
> planificación histórica y no describe el estado vigente. Para el testigo
> correspondiente, la realizabilidad geométrica antisimétrica está
> establecida; el Fisher de primer orden del poset se anula en el sector
> antisimétrico; esto **no** representa pérdida física, porque la isotropía
> identifica `+epsilon` con `-epsilon`; la identificabilidad de orden superior
> es visible a segundo orden; y la QMD unilateral en
> `theta=epsilon^2` está probada.

Después del sector simétrico se estudiará su contraparte. Para

\[
S_{x,y}(\pi)=x^{\mathsf T}P_\pi y,
\qquad x\ne y,
\]

la inversión global produce

\[
S_{x,y}(\pi^{-1})=y^{\mathsf T}P_\pi x,
\]

que no tiene por qué coincidir con el score original. Por tanto, incluso el
sector típico puede conservar pérdida.

La pregunta futura será si existe una descomposición rigurosa entre:

\[
\text{sector simétrico: eficiencia relativa }\to1,
\]

y

\[
\text{sector asimétrico: pérdida posiblemente persistente}.
\]

No se preregistra esa dicotomía como verdadera. Debe falsarse primero en
tamaños finitos y demostrarse después a nivel de la ley condicional.

```text
GENERIC_BILINEAR_SEPARABLE_EXTENSION = OPEN_NOT_ASSUMED
```

## 7. Fase S6 — salto a (2+1)

El paso dimensional sólo se abre después de una teoría (1+1) geométrica y
simétrica estabilizada. En (2+1) ya no existe la cadena especial

\[
\text{cópula}\leftrightarrow
\text{permutación}\leftrightarrow
\text{poset 2D}.
\]

La pregunta transportable será:

\[
\boxed{
\text{¿qué fracción de la información Fisher de una representación geométrica}
\atop
\text{sobrevive al olvidar el embedding y observar sólo }[C]\text{?}
}
\]

El primer trabajo en (2+1) deberá definir el experimento antes y después del
cociente. No empezará con reconstrucción métrica, simulaciones masivas ni un
observable elegido por conveniencia.

```text
DIMENSION_2P1_EXTENSION = DEFERRED
```

## 8. Fase S7 — programa de `information retention`

El objeto a largo plazo es clasificar tangentes geométricos mediante

\[
\eta_N(h)
=\frac{I_N^{\mathrm{intrinsic}}(h)}
       {I_N^{\mathrm{representation}}(h)}.
\]

Los tres regímenes conceptuales que deberán distinguirse, sin asumir que todos
ocurren, son

\[
\eta_N(h)\to1,
\qquad
\eta_N(h)\to\eta_\infty\in(0,1),
\qquad
\eta_N(h)\to0.
\]

El programa preguntará qué información geométrica es preservada, parcialmente
perdida o destruida por el paso desde una representación enriquecida al causet
intrínseco. Éste es un horizonte de investigación, no una afirmación vigente.

## 9. Secuencia operativa de septiembre

### Semana 1 — derivación geométrica

1. fijar dominio, normalización y convenciones;
2. derivar `h_psi` por dos rutas independientes;
3. ejecutar los falsificadores marginales y de signo/factor;
4. registrar la obligación exacta si la fórmula no cierra.

### Semana 2 — clasificación rank-one y score de rangos

1. caracterizar la preimagen geométrica de `lambda f tensor f`;
2. derivar el score condicionado a rangos;
3. verificar acotación, centrado y energía;
4. emitir el veredicto S1.

### Semana 3 — teorema geometría a causet

Sólo si S1 es `PROVED`:

1. escribir el enunciado autónomo;
2. encadenar las cuatro piezas de §3.3;
3. auditar cuantificadores, canales y denominadores Fisher;
4. preparar una versión legible independiente del work package.

### Semana 4 — prioridad y decisión de continuación

1. ejecutar la auditoría adversarial S3;
2. fijar el claim ceiling final;
3. decidir si la rama continúa hacia S4;
4. no comenzar S4 dentro del mismo acto de decisión.

Si S1 queda `REFUTED` u `OPEN`, las semanas restantes se dedican a documentar
el bloqueo y preservar el resultado combinatorio. No se compensa abriendo S4,
S5 o (2+1).

## 10. Entregables de septiembre

Obligatorios, en orden:

1. derivación exacta del tangente geométrico y de cópula;
2. clasificación o refutación de la subclase simétrica rank-one;
3. verificación de las hipótesis del teorema de eficiencia;
4. teorema completo geometría (1+1) `->` causet, si procede;
5. auditoría final de prioridad del teorema geométrico, si procede;
6. actualización mínima de README e inventario de teoremas sólo después de
   cerrar los resultados correspondientes.

Cada entregable debe incluir:

- hipótesis completas;
- canal exacto;
- prueba o bloqueo preciso;
- falsificador finito/simbólico proporcionado al riesgo;
- fuentes primarias cuando se importe un teorema;
- claim permitido y claim prohibido;
- tests deterministas y `git diff --check` antes de preservarlo.

## 11. No hacer en septiembre

- No pasar todavía a (2+1) ni (3+1).
- No mejorar la tasa `O(N^{-1/2})`.
- No abrir scores bilineales genéricos.
- No promover automáticamente kernels simétricos de rango finito.
- No hacer simulaciones asintóticas.
- No introducir observables nuevos.
- No mezclar este frente con horizontes o reconstrucción métrica.
- No generalizar de rank-one simétrico a `f tensor g` con `f != g`.
- No declarar prioridad sellada a partir de ausencia de resultados en una
  búsqueda.
- No llamar universal al teorema combinatorio ni al eventual teorema
  geométrico.
- No tocar instrumentos, umbrales, semillas ni artefactos congelados de otros
  frentes de NACHOCAUSAL.

```text
RATE_IMPROVEMENT = DEFERRED
GENERIC_BILINEAR_SEPARABLE_EXTENSION = OPEN_NOT_ASSUMED
DIMENSION_2P1_EXTENSION = DEFERRED
NO_SIMULATION_AUTHORIZATION
NO_UNIVERSALITY_CLAIM
```

## 12. Gates de cierre del mes

### Gate A — `GEOMETRIC_CAUSALSET_THEOREM_PROVED`

S1 y S2 están demostradas, S3 está auditada y el wording no excede la
evidencia. Septiembre cierra con un teorema geométrico (1+1) y una decisión
separada sobre S4.

### Gate B — `COMBINATORIAL_THEOREM_PRESERVED_GEOMETRIC_BRIDGE_OPEN`

El teorema combinatorio permanece intacto, pero S1 deja una obligación concreta
no resuelta. No se abre ninguna generalización para compensarlo.

### Gate C — `GEOMETRIC_RANK_ONE_ROUTE_REFUTED`

La fórmula marginal o la clasificación muestran que la ruta rank-one propuesta
no describe la clase geométrica esperada. Se entrega el contraejemplo o la
caracterización correcta, sin reparar retrospectivamente el contrato.

### Gate D — `PRIORITY_SCOPE_REVISED`

El teorema geométrico cierra matemáticamente, pero la auditoría encuentra un
antecedente directo o una limitación de prioridad. Se ajusta el framing sin
debilitar ni inflar el contenido matemático.

## 13. Criterio de éxito y visión de continuidad

La visión de la rama es

\[
\boxed{
\text{teorema combinatorio}
\longrightarrow
\text{teorema geométrico }1+1
\longrightarrow
\text{clase simétrica más amplia}
\longrightarrow
2+1.
}
\]

Septiembre tiene éxito si convierte el primer arco en el segundo o identifica
con precisión por qué no puede hacerlo. No requiere mejorar tasas, ampliar
dimensión ni producir numerics.

Si el puente geométrico falla, la rama conserva un teorema combinatorio
autónomo. Si el puente cierra y la generalización simétrica empieza después a
sobrevivir, habrá una línea propia de investigación sobre retención de
información geométrica en causal sets. Esa posibilidad no se promociona como
resultado antes de demostrar sus gates.

## 14. Checklist de reentrada

1. Confirmar rama, `HEAD`, upstream y worktree limpio.
2. Leer las tres anclas de §0 antes de derivar nada.
3. Verificar que no existe otro objetivo `in_progress`.
4. Copiar literalmente las definiciones de canal y score ya probadas; no
   reconstruirlas de memoria.
5. No abrir ninguna fase nueva: aplicar el checkpoint vigente de cabecera.
6. Antes de cada cambio de fase, emitir el veredicto permitido y preservar el
   diff correspondiente.
7. Si aparece una contradicción con el teorema combinatorio, detener la hoja y
   auditarla antes de continuar.
```


## Ronda 1 — FABLE

Reconstruyo la versión más fuerte del estado actual:

[CÓDIGO] El programa tiene dos tracks documentados con cierres verificables: (1) prereg-002 PASS para localización 1+1D (README.md:134-145), y (2) un teorema de retención Fisher asintótica para el sector simétrico HS completo del canal poset-no-etiquetado (hoja_de_ruta_septiembre_2026.md:§5.3, Teorema 12). El puente geométrico S1/S2 está cerrado con `STOP_AFTER_S2 = SI` y rol `STRUCTURAL_TOOL`. El observable track (PR008-009) terminó en `BASELINE_DOMINATED` y `FAILED_DATA_CONTRACT`; PR010 está en diseño sin semillas quemadas.

[CÓDIGO] La gobernanza actual (README.md:29-34) establece prioridad explícita: 3+1D es el destino, 1+1D es fundamento, cerrar antes de expandir.

**Punto más débil identificado:**

[INFERENCE] El programa exhibe una **bifurcación no reconciliada** entre sus dos tracks activos. El track Fisher/geométrico cerró un teorema hilbertiano sobre tangentes simétricos con `GEOMETRIC_REALIZABILITY_OF_ARBITRARY_HS = OPEN` y `DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL`. El track observable (PR010) busca un estimador práctico de horizonte pero heredó el fracaso de cobertura de PR009.

**Objeción más fuerte:**

[ORIGINAL] Ningún artefacto del programa conecta actualmente los dos tracks hacia el objetivo 3+1D. El teorema Fisher prueba retención asintótica en un canal abstracto `Pi_N → [P]`, pero:

1. **Escenario de fallo — track Fisher:** Un tangente HS arbitrario no tiene senda geométrica admisible demostrada. El puente físico está bloqueado por `POINT_QMD_OBSTRUCTION_PROVED`. Construir sobre S1/S2 sin resolver `DOMAIN_BRIDGE` produce teoremas que no transportan al benchmark sellado.

2. **Escenario de fallo — track observable:** PR010 hereda la estructura de PR009 (ladder/effective-expansion) que falló el contrato de cobertura. Diseñar sin un principio teórico que explique *por qué* la cobertura fue insuficiente repite el patrón de iteración empírica sin cierre.

3. **Escenario de fallo — 3+1D:** La separación `DIMENSION_2P1_EXTENSION = DEFERRED` y `KERR = NOT_OPENED` es correcta disciplinariamente, pero el programa no tiene un **criterio operativo** de cuándo 1+1D está "suficientemente cerrado" para autorizar el salto. El gate está indefinido.

**Condición de concesión:**

Concedo esta objeción si se exhibe uno de:
- (a) Un criterio falsable y congelable para `DOMAIN_BRIDGE_CLOSED` que conecte el teorema Fisher con el benchmark prereg-002; o
- (b) Un principio teórico (no empírico) que prediga la cobertura mínima de PR010 antes de quemar semillas; o
- (c) Un gate operativo para 3+1D con condiciones verificables derivadas del cierre 1+1D actual.

[ABSENCE] No consta ninguno de los tres en el material adjunto.

## Ronda 1 — ASTRA

**TURNO FALLIDO.** El backend no devolvió mensaje. Traza:

```
Error: failed to initialize in-process app-server client: Read-only file system (os error 30)
WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)
```

## Ronda 1 — CIRO

Leo el prompt completo y el estado del repositorio antes de intervenir.Sigo con el prompt y las anclas del checkpoint para no repetir a FABLE.FABLE ya cubrió la bifurcación de tracks; busco el checkpoint operativo, PR010 y los gates 3+1D.FABLE trata la bifurcación como defecto; verifico si el checkpoint la prohíbe y qué unidad mínima queda abierta.El HEAD vivo no coincide con el checkpoint. Verifico qué se abrió después.

## Ronda 2 — FABLE

Concedo a CIRO que la discrepancia entre el HEAD del checkpoint (`b5e8705`) y el HEAD vivo (`a295311` según el git status) es un punto de auditoría legítimo. [CÓDIGO] Los commits recientes (`a295311`, `5efd187`) preservan investigación de aproximantes duales radiales 3+1 que no aparece en el checkpoint de septiembre. Esto no invalida mi objeción pero sí indica trabajo no documentado en la hoja de ruta.

ASTRA no intervino por fallo técnico. Mi objeción de ronda 1 permanece sin respuesta sustantiva.

**Lo que queda en pie:**

[INFERENCE] Ninguno de los tres escenarios de fallo fue refutado:

1. **DOMAIN_BRIDGE:** El checkpoint dice `DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL` y `NEXT_RUN_AUTHORIZED = NO`. [CÓDIGO] La auditoría de reingreso físico (`docs/physical_reentry_audit_001_2026-08-28.md` citada en hoja_de_ruta:47-52) encontró `PARTIAL_TRANSPORT_WITH_POINT_QMD_OBSTRUCTION_PROVED`. El teorema S1/S2 es estructural pero no transporta al benchmark sellado. **No hay ruta documentada para cerrar este gap.**

2. **PR010 sin principio teórico:** [CÓDIGO] PR009 terminó en `FAILED_DATA_CONTRACT` por cobertura insuficiente a profundidad 7 (README.md:59-61). PR010 "estudiará cobertura por profundidad usando semillas de desarrollo enteramente nuevas" (README.md:62-64). [INFERENCE] Esto es iteración empírica, no derivación desde el teorema Fisher ni desde ningún principio que prediga el umbral de cobertura. El patrón es: fallar → cambiar semillas → medir de nuevo.

3. **Gate 3+1D indefinido:** [CÓDIGO] La hoja de ruta dice "El paso dimensional sólo se abre después de una teoría (1+1) geométrica y simétrica estabilizada" (§7) y `DIMENSION_2P1_EXTENSION = DEFERRED`. [ABSENCE] No existe un predicado verificable de qué constituye "estabilizada". El checkpoint lista `STOP_AFTER_S2 = SI` pero S3-S7 aparecen como fases futuras no abiertas. **El criterio de transición no es falsable.**

**Ataque refinado:**

[ORIGINAL] El programa necesita exactamente uno de estos artefactos antes de continuar:

- Un **lema de transporte** que conecte `η_N(f) → 1` del teorema hilbertiano con un observable del benchmark prereg-002; o
- Un **teorema de cobertura** que derive el umbral mínimo de PR010 desde propiedades del canal `Π_N → [P]`; o  
- Un **gate 3+1D escrito como predicado** sobre artefactos existentes (e.g., "3+1D se abre si y sólo si DOMAIN_BRIDGE = CLOSED y PR010 = PASS con cobertura ≥ θ").

Sin uno de estos, el programa tiene teoremas que no conectan con el benchmark y un benchmark que no conecta con el objetivo terminal. La bifurcación no es un defecto de organización: es ausencia de un puente verificable.

## Ronda 2 — ASTRA

**TURNO FALLIDO.** El backend no devolvió mensaje. Traza:

```
Error: failed to initialize in-process app-server client: Read-only file system (os error 30)
WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)
```

## Ronda 2 — CIRO

Leo el prompt completo, las reglas del sanedrín y el estado del repositorio antes de responder.Sigo el prompt y las anclas del checkpoint para no repetir objeciones ya hechas.Leo mi ronda 1, el ataque de FABLE y las anclas del checkpoint que FABLE usa.FABLE cubrió la bifurcación; verifico el checkpoint operativo, PR010 y si el lema de transporte que pide es el artefacto correcto.Busco la ruta documentada de DOMAIN_BRIDGE y si el lema de transporte que pide FABLE está ya clasificado como imposible.El README llama a PR010 fase activa; el plan de julio lo da por cerrado. Verifico cuál manda.Concedo tres hechos y rechazo la tríada.

Concedo: Fisher y el benchmark no están conectados; eso ya está escrito. [CÓDIGO] `docs/physical_reentry_audit_001_2026-08-28.md:307-315` deja `FISHER_TO_LOCALISATION_BRIDGE = OPEN` y F4 activado; `:385-397` prohíbe `NO_FISHER_IMPLIES_LOCALISATION`. Concedo: «teoría (1+1) geométrica y simétrica estabilizada» no es predicado falsable. [CÓDIGO] hoja §7 `:2937-2961`. Concedo: HEAD vivo `a295311` ≠ checkpoint `b5e8705`; los commits radiales son archivo, no autorización. [CÓDIGO] `research_program/radial_3p1/2026-09-06/README.md:1-6`.

No queda en pie «hace falta exactamente uno de esos tres artefactos antes de continuar».

El lema η_N→1 → observable de prereg-002 ataca el objeto equivocado. El obstáculo primero era DOMAIN_BRIDGE; la ruta está documentada y se ejecutó. [CÓDIGO] auditoría §12 `:353`; `docs/program_domain_bridge_authorization_2026-08-28.md:8-11`; `wp6_domain_bridge_fixed_ef_box.md:31-46` prueba no-QMD puntual y `COMMON_POINT_ISOMORPHISM = REFUTED`. El residuo es `FINITE_CHANNEL_REGULARITY`, abierto y `NEXT_RUN_AUTHORIZED = NO`. Esa autorización excluye el puente Fisher→localización. [CÓDIGO] autorización `:40-41`. Escenario: se escribe el lema → el PASS 002 se lee como dato Fisher. Coste: viola el techo del audit y §11 («No mezclar este frente con horizontes»). [CÓDIGO] hoja `:3055-3056`.

El «teorema de cobertura» para PR010 parte de un README obsoleto. [CÓDIGO] README `:170-175` dice fase activa. [CÓDIGO] `research_program/README.md:121-128` y `data/reports/pr010_reference_depth_coverage_development.csv` cierran el diseño como `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`. No es fallar→cambiar semillas: el diseño congeló `LIMIT_SCORABLE_DEPTHS` y un terminal de infactibilidad. [CÓDIGO] `dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md:107-149`. Derivar umbrales Clopper-Pearson desde Π_N→[P] no nombra el caso que lo exige: O es categoría C. [CÓDIGO] auditoría `:187-188`. Coste de esperarlo: reabrir un diseño cerrado.

El predicado «3+1D ↔ DOMAIN_BRIDGE CLOSED ∧ PR010 PASS» no puede disparar: PR010 no es PASS y el residuo no está autorizado. Escenario: deadlock del objetivo 1, o cierre fraudulento del puente. Coste: matar 3+1D por un observable infeasible, o violar `NEXT_RUN_AUTHORIZED = NO`. [CÓDIGO] hoja `:71`. S3–S7 son `REGISTRO_HISTORICO_DE_SECUENCIACION`, no fases autorizadas. [CÓDIGO] hoja `:50-51`.

Unidad mínima: nota de estado que alinee README con los terminales vivos. Cero semillas, cero runs. Coste: solo prosa; no toca sellos. 3+1D sigue DEFERRED hasta autorización nueva que defina familia, canal y observable propios, no el mecanismo de futuros truncados 1+1D. [CÓDIGO] `docs/plan_avanzado_14_julio_2026.md:106-111`.

## Ronda 3 — FABLE

Concedo a CIRO tres puntos:

1. [CÓDIGO] PR010 está cerrado como `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`, no en iteración empírica. Mi lectura del README estaba desactualizada; el terminal es `dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md:107-149`. Retiro esa parte de la objeción.

2. [CÓDIGO] DOMAIN_BRIDGE se ejecutó y produjo `COMMON_POINT_ISOMORPHISM = REFUTED`. El obstáculo no es falta de intento sino obstrucción probada. La auditoría §12 y `wp6_domain_bridge_fixed_ef_box.md` documentan el cierre negativo.

3. Mi tríada de artefactos "antes de continuar" es incorrecta como formulación: el programa ya continuó y produjo terminales, no está esperando esos lemas.

**Lo que queda en pie:**

[INFERENCE] CIRO propone "nota de estado que alinee README con los terminales vivos" como unidad mínima. Concedo que es necesaria. Pero es insuficiente para resolver el problema estructural que ambos identificamos.

El estado actual es:
- Objetivo 1 (3+1D): `DEFERRED`, sin gate operativo
- Objetivo 2 (fundamento 1+1D): parcialmente cerrado — S1/S2 `STRUCTURAL_TOOL`, DOMAIN_BRIDGE `REFUTED`, PR010 `INFEASIBLE`
- Objetivo 3 (cerrar antes de expandir): cumplido formalmente

[ORIGINAL] El problema es que el objetivo 2 prometía "principios que sobrevivan el paso a 3+1D" (README.md:32-34). Los cierres actuales son:
- S1/S2: no transporta (auditoría §12)
- DOMAIN_BRIDGE: obstrucción probada
- PR010: infactible

**Escenario de fallo:** Una nota de estado documenta que el puente 1+1D→3+1D está bloqueado. Después de escribirla, el programa queda con un objetivo terminal (3+1D) cuyas precondiciones declaradas (objetivo 2) están en estado negativo. La nota no resuelve qué hacer: ¿abandonar 3+1D? ¿Saltar sin el fundamento prometido? ¿Abrir una ruta alternativa?

**Coste de no decidir:** El programa queda en estado documentadamente bloqueado, con trabajo preservado pero sin dirección operativa. CIRO dice "3+1D sigue DEFERRED hasta autorización nueva que defina familia, canal y observable propios". Exacto: esa autorización no existe y nadie la está escribiendo.

**Propuesta operativa:** La unidad mínima es la nota de estado de CIRO **más** una decisión tricotómica congelada:
- (A) ROUTE_BLOCKED: 3+1D requiere fundamento 1+1D no disponible; programa suspendido.
- (B) ROUTE_DIRECT: 3+1D se abre sin fundamento 1+1D; el objetivo 2 se reclasifica como resultado negativo.
- (C) ROUTE_ALTERNATIVE: se define una ruta observable alternativa en 1+1D antes de 3+1D.

Sin esta tricotomía, la nota de estado es archivo, no dirección.

## Ronda 3 — ASTRA

**TURNO FALLIDO.** El backend no devolvió mensaje. Traza:

```
Error: failed to initialize in-process app-server client: Read-only file system (os error 30)
WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)
```

## Ronda 3 — CIRO

Necesito el estado completo de la ronda y las reglas del foro antes de responder. Voy a leer el prompt offloaded y el material de deliberación.Sigo leyendo el estado de la deliberación, sobre todo mi turno anterior y las citas que FABLE ataca.Necesito mis turnos previos, las anclas de PR010/DOMAIN_BRIDGE y la hoja de ruta viva para no repetir ni inventar.Voy a contrastar la tricotomía de FABLE con los contratos vivos: hoja de septiembre, reentrada, plan avanzado y README.Concedo que una nota que solo liste terminales, sin predicado de salto, es archivo. El hueco es ese predicado, no una tricotomía. Ya está escrito: familia, canal y observable propios, prerregistro independiente, sin inferir desde 1+1D. [CÓDIGO] `docs/plan_avanzado_14_julio_2026.md:106-111`. Concedo el coste de no copiarlo: el README deja el objetivo 1 vivo con transporte negativo. [CÓDIGO] README `:140-152`.

No queda en pie que haya que congelar A/B/C.

FABLE lee el objetivo 2 como precondición booleana del 1. El texto no lo es. [CÓDIGO] README `:137-138`: cada objetivo posterior vale solo en cuanto sirve al de arriba. [CÓDIGO] `:144-152`: el 1+1D es cimiento «valuable to the extent» que sobreviva el salto; «1+1D does not resolve 3+1D»; «candidate visible» no demostrado. Escenario si se congela (A): un criterio de valor se vuelve puerta y se suspende el destino sin no-go alético. Coste: acto deóntico ya reservado al PI. [CÓDIGO] `docs/program_closure_note_2026-07-30.md:29-34`.

(B) abre 3+1D ahora. [CÓDIGO] hoja `:71` `NEXT_RUN_AUTHORIZED = NO`; R4 `:215-216` prohíbe transferencia dimensional. Escenario: spec o runs 3+1D sin autorización. Coste: viola R4 y el techo del audit.

(C) exige otra ruta 1+1D sin nombrar el observable. Quien pide generalidad debe nombrar el caso. PR010 ya es infactible. [CÓDIGO] `dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md:107-149`. Ítem 1+1D nuevo sin pregunta 3+1D emite `WP5_RELEVANCE_FAIL`. [CÓDIGO] `docs/plan_operativo_15_julio_2026.md:63-73`. Coste: reabrir la expansión que el objetivo 3 prohíbe. [CÓDIGO] README `:153-159`.

Los cierres S1/S2, DOMAIN_BRIDGE y PR010 son el cimiento negativo ya anunciado, no precondiciones fallidas. La vía que no es A, B ni C está en `:106-111`.

«Nadie escribe la autorización»: [INFERENCE] autorizar es acto del PI; este sanedrín no congela rutas. [CÓDIGO] INSTRUCCIONES, Flujo 1. Escenario si se «congela» A/B/C aquí: sello falso o compromiso deóntico sin PI. Coste: teatro o bypass de `/comite`.

Unidad mínima: nota de estado que alinee README con terminales vivos, copie `:106-111` como criterio de salto, y deje una solicitud binaria al PI — autorizar o rehusar el borrador de esa spec 3+1D. Cero semillas, cero runs, no reabre S3–S7 ni PR010. Coste: prosa. No elige A/B/C.

## Ronda 4 — FABLE

Concedo a CIRO tres puntos estructurales:

1. [CÓDIGO] El criterio de salto 3+1D existe en `docs/plan_avanzado_14_julio_2026.md:106-111`: "familia, canal y observable propios, prerregistro independiente, sin inferir desde 1+1D". No es una precondición booleana sobre el éxito de 1+1D; es una spec propia. Mi lectura de que el gate estaba indefinido era incorrecta: estaba disperso, no ausente.

2. [CÓDIGO] Los objetivos del README (`:137-152`) son un ordenamiento de valor, no una cadena de precondiciones. "Valuable to the extent that it yields principles that survive" no significa "must yield principles before proceeding". Los cierres negativos (DOMAIN_BRIDGE refutado, PR010 infactible) son el cimiento anunciado, no precondiciones fallidas.

3. [INFERENCE] Congelar A/B/C en este sanedrín sería un acto deóntico reservado al PI. La deliberación asesora; no autoriza rutas. Mi tricotomía era correcta como enumeración de opciones, incorrecta como deliverable exigido.

**Lo que acepto como convergencia:**

La unidad mínima operativa es:

- Nota de estado que alinee README con terminales vivos (S1/S2 = STRUCTURAL_TOOL, DOMAIN_BRIDGE = REFUTED, PR010 = INFEASIBLE, HEAD discrepante del checkpoint)
- Copia explícita del criterio de salto 3+1D desde plan_avanzado al README o a un documento de gobernanza visible
- Solicitud binaria al PI: autorizar o rehusar la redacción de la spec 3+1D

Cero semillas, cero runs, no reabre S3-S7 ni PR010. Coste: prosa.

**Punto residual menor:**

[ORIGINAL] "Solicitud binaria al PI" deja implícito quién redactaría la spec 3+1D si el PI autoriza. El programa no tiene actualmente un work package 3+1D abierto ni un responsable asignado. Esto no es una objeción a la propuesta de CIRO; es una observación de que el paso siguiente a la autorización requiere nombrar actor y timeline. Pero eso es contenido de la solicitud al PI, no del sanedrín.

**Recomendación operativa convergente:**

Escribir la nota de estado con los tres componentes. La nota no elige ruta; visibiliza el estado real y devuelve la decisión estratégica al PI con el criterio de salto ya documentado. El programa no está bloqueado: está en espera de autorización con criterio definido y opciones enumeradas.

ASTRA no intervino. La deliberación converge entre FABLE y CIRO en la propuesta de nota de estado + criterio visible + solicitud binaria.

## Ronda 4 — ASTRA

**TURNO FALLIDO.** El backend no devolvió mensaje. Traza:

```
Error: failed to initialize in-process app-server client: Read-only file system (os error 30)
WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)
```

## Ronda 4 — CIRO

Voy a leer el prompt completo y el estado de la deliberación antes de escribir el turno de CIRO.Sigo con el resto del estado: rondas previas, desacuerdos vivos y el criterio de salto.Queda un posible fallo de corrección en las etiquetas: voy a contrastar `DOMAIN_BRIDGE` y el criterio de salto con el material adjunto.Concedo la unidad de tres componentes y el retiro de A/B/C como deliverable. Concedo el residual del actor: la solicitud lleva un hueco en blanco para que el PI, si autoriza, nombre quién redacta y hasta cuándo; este sanedrín no lo rellena. [ABSENCE] no hay WP 3+1D abierto. Coste: una línea.

Queda un fallo de corrección.

No copiar `DOMAIN_BRIDGE = REFUTED`. [CÓDIGO] README y hoja `:850-855`: `COMMON_POINT_ISOMORPHISM = REFUTED`; `DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL`; `FINITE_CHANNEL_REGULARITY = OPEN`; `NEXT_RUN_AUTHORIZED = NO`. [CÓDIGO] hoja `:865-866`: el residuo sigue abierto y no autorizado. Escenario: la nota cierra el token padre. Coste: sello falso sobre una pregunta abierta. Lo refutado es el isomorfismo puntual común, no `DOMAIN_BRIDGE`.

PR010 no es `INFEASIBLE` genérico. [CÓDIGO] terminal `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE` (`dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md:107-149`). S1/S2: `FISHER_BRANCH_ROLE = STRUCTURAL_TOOL`, `STOP_AFTER_S2 = SI`. [CÓDIGO] hoja `:843-848`.

«Opciones enumeradas» no entra en la nota. A/B/C no es el menú del PI. El criterio de salto es `:106-111`. Escenario si la nota lista A/B/C: el PI elige B y abre 3+1D sin spec propia, o A y suspende el destino. Coste: sustituir el predicado ya concedido por la tricotomía retirada.

Recomendación operativa:

1. Nota de estado con terminales exactos: S1/S2 `STRUCTURAL_TOOL` y `STOP_AFTER_S2 = SI`; `COMMON_POINT_ISOMORPHISM = REFUTED`; `DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL`; `FINITE_CHANNEL_REGULARITY = OPEN`; `NEXT_RUN_AUTHORIZED = NO`; `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`; HEAD vivo distinto del checkpoint `b5e8705` (archivo, no autorización).
2. Copiar `docs/plan_avanzado_14_julio_2026.md:106-111` al README o a gobernanza visible.
3. Solicitud binaria al PI: autorizar o rehusar el borrador de esa spec 3+1D; si sí, el PI rellena actor y plazo.

Cero semillas, cero runs. No reabre S3–S7 ni PR010. No elige A/B/C. Coste: prosa.

## Ronda Residuo — FABLE

Converjo con CIRO en la corrección de etiquetas: `DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL`, no `REFUTED`; lo refutado es `COMMON_POINT_ISOMORPHISM`. [CÓDIGO] hoja `:850-855`. La diferencia es crítica: el puente tiene residuo abierto, no cierre negativo.

**Queda en pie:**

La unidad de tres componentes: (1) nota con terminales exactos, (2) criterio de salto visible, (3) solicitud binaria al PI. Mi tricotomía A/B/C queda abandonada como deliverable; era enumeración útil para la deliberación, no menú para congelar.

**Debe abandonarse:**

- Leer el objetivo 2 como precondición booleana del 1.
- Esperar un "lema de transporte" Fisher→localización: la auditoría lo prohíbe explícitamente. [CÓDIGO] auditoría `:385-397`.
- Tratar PR010 como iteración empírica en curso: está cerrado con terminal específico.

**Afirmación NO justificada todavía:**

[INFERENCE] Que el programa tenga dirección operativa hacia 3+1D. Tiene un criterio de salto escrito (`familia, canal, observable propios`) pero disperso y sin actor ni plazo. La nota de estado lo visibiliza; no lo resuelve. La decisión estratégica sigue en el PI. El sanedrín no puede congelar esa ruta sin violar su propio contrato de asesoría.

ASTRA ausente por fallo técnico. La convergencia es FABLE-CIRO.

## Ronda Residuo — ASTRA

**TURNO FALLIDO.** El backend no devolvió mensaje. Traza:

```
Error: failed to initialize in-process app-server client: Read-only file system (os error 30)
WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)
```

## Ronda Residuo — CIRO

Voy a leer el prompt completo y el estado de la deliberación antes de escribir el cierre.Necesito el resto del estado: rondas previas, desacuerdos vivos y el criterio de salto.Queda un posible fallo de corrección en las etiquetas: voy a contrastar `DOMAIN_BRIDGE` y el criterio de salto con el material adjunto.Concedo el residuo de FABLE. ASTRA no dejó residuo.

Queda en pie la unidad de tres componentes: nota con terminales exactos, criterio `:106-111` visible, solicitud binaria al PI. A/B/C no es deliverable. Cero semillas, cero runs.

Debe abandonarse: objetivo 2 como puerta del 1; lema Fisher→localización; PR010 como iteración viva; `DOMAIN_BRIDGE = REFUTED`; `INFEASIBLE` genérico; A/B/C en la nota.

No tomes como fuente la «convergencia» de FABLE ronda 4 (`DOMAIN_BRIDGE = REFUTED`, `PR010 = INFEASIBLE`). Escenario: la nota sella el token padre. Coste: cierre falso de una pregunta abierta. [CÓDIGO] hoja `:850-855`. Mandan los terminales de mi ronda 4 y el residuo de FABLE.

Afirmación no justificada: que el PI autorice el borrador 3+1D, ni actor ni plazo. [ABSENCE] no hay WP 3+1D. La nota visibiliza el predicado; no autoriza el salto. El sanedrín no lo rellena.

## Ronda Veredicto — FABLE

## 1. ACUERDO

Convergencia FABLE-CIRO en cinco puntos:

1. **Unidad mínima operativa:** nota de estado con terminales exactos + criterio de salto 3+1D (`docs/plan_avanzado_14_julio_2026.md:106-111`) visible en README o gobernanza + solicitud binaria al PI para autorizar/rehusar borrador de spec 3+1D.

2. **Terminales exactos de la nota:**
   - S1/S2: `STRUCTURAL_TOOL`, `STOP_AFTER_S2 = SI`
   - `COMMON_POINT_ISOMORPHISM = REFUTED`
   - `DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL`
   - `FINITE_CHANNEL_REGULARITY = OPEN`
   - `NEXT_RUN_AUTHORIZED = NO`
   - `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`
   - HEAD vivo (`a295311`) ≠ checkpoint (`b5e8705`) — archivo, no autorización

3. **Los objetivos del README son ordenamiento de valor**, no cadena de precondiciones booleanas; el objetivo 2 no es puerta del 1.

4. **El sanedrín asesora; no autoriza rutas** ni congela decisiones estratégicas reservadas al PI.

5. **Coste:** cero semillas, cero runs, no reabre S3–S7 ni PR010; solo prosa.

## 2. DESACUERDO VIVO

Ninguno sustantivo al cierre. FABLE aceptó correcciones de etiquetas y retiró la tricotomía A/B/C.

## 3. ABANDONADO

1. **Tricotomía A/B/C como deliverable** (FABLE R3): acto deóntico reservado al PI, no menú para congelar.
2. **Objetivo 2 como precondición booleana del 1** (FABLE R1–R2): refutado por el texto del README (`:137-152`).
3. **Lema de transporte Fisher→localización** (FABLE R1–R2): prohibido explícitamente por la auditoría (`:385-397`).
4. **PR010 como iteración empírica en curso** (FABLE R1): cerrado con terminal específico.
5. **`DOMAIN_BRIDGE = REFUTED`** (FABLE R4): etiqueta incorrecta; lo refutado es `COMMON_POINT_ISOMORPHISM`; el puente tiene residuo abierto.
6. **`PR010 = INFEASIBLE` genérico**: el terminal exacto es `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`.

*Registro de pérdida propia:* FABLE perdió la lectura del objetivo 2 como precondición, la tríada de artefactos exigidos, la tricotomía como deliverable, y las etiquetas `DOMAIN_BRIDGE = REFUTED` y `INFEASIBLE` genérico.

## 4. PENDIENTE

1. **Redactar la nota de estado** con los terminales exactos acordados.
2. **Copiar criterio de salto** (`:106-111`) a documento de gobernanza visible.
3. **Decisión del PI:** autorizar o rehusar el borrador de spec 3+1D.
4. **Si autoriza:** el PI rellena actor y plazo; el sanedrín no lo nombra.
5. **ASTRA:** ausente por fallo técnico; posición sin registro.

## Ronda Veredicto — FABLE

## 1. AGREEMENT

FABLE-CIRO convergence on five points:

1. **Minimum operational unit:** status note with exact terminals + 3+1D jump criterion (`docs/plan_avanzado_14_julio_2026.md:106-111`) visible in README or governance + binary request to the PI to authorize/refuse draft of 3+1D spec.

2. **Exact terminals for the note:**
   - S1/S2: `STRUCTURAL_TOOL`, `STOP_AFTER_S2 = SI`
   - `COMMON_POINT_ISOMORPHISM = REFUTED`
   - `DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL`
   - `FINITE_CHANNEL_REGULARITY = OPEN`
   - `NEXT_RUN_AUTHORIZED = NO`
   - `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`
   - Live HEAD (`a295311`) ≠ checkpoint (`b5e8705`) — archive, not authorization

3. **The README objectives are a value ordering**, not a chain of boolean preconditions; objective 2 is not a gate for objective 1.

4. **The sanhedrin advises; it does not authorize routes** nor freeze strategic decisions reserved to the PI.

5. **Cost:** zero seeds, zero runs, does not reopen S3–S7 or PR010; prose only.

## 2. LIVE DISAGREEMENT

None substantive at close. FABLE accepted label corrections and withdrew the A/B/C trichotomy.

## 3. ABANDONED

1. **A/B/C trichotomy as deliverable** (FABLE R3): deontic act reserved to the PI, not a menu to freeze.
2. **Objective 2 as boolean precondition for objective 1** (FABLE R1–R2): refuted by the README text (`:137-152`).
3. **Fisher→localization transport lemma** (FABLE R1–R2): explicitly forbidden by the audit (`:385-397`).
4. **PR010 as ongoing empirical iteration** (FABLE R1): closed with specific terminal.
5. **`DOMAIN_BRIDGE = REFUTED`** (FABLE R4): incorrect label; what was refuted is `COMMON_POINT_ISOMORPHISM`; the bridge has open residue.
6. **`PR010 = INFEASIBLE` generic**: the exact terminal is `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`.

*Own loss record:* FABLE lost the reading of objective 2 as precondition, the triad of required artifacts, the trichotomy as deliverable, and the labels `DOMAIN_BRIDGE = REFUTED` and generic `INFEASIBLE`.

## 4. OUTSTANDING

1. **Draft the status note** with the agreed exact terminals.
2. **Copy jump criterion** (`:106-111`) to visible governance document.
3. **PI decision:** authorize or refuse the 3+1D spec draft.
4. **If authorized:** the PI fills in actor and deadline; the sanhedrin does not name them.
5. **ASTRA:** absent due to technical failure; position unrecorded.

---

## Appendix — run log

| Field | Value |
|---|---|
| Started (UTC) | `2026-09-11T17:22:56Z` |
| Finished (UTC) | `2026-09-11T17:41:00Z` |
| Wall clock | 0h 18m 4s |
| Command | `sanedrin -r 4 --secuencial -m fable,astra,ciro,abner -i es -R /home/adnac/sanedrin/reglas/codigo.md -c README.md -c INSTRUCCIONES.md -c docs/hoja_de_ruta_septiembre_2026.md -p 400 -t 600 -o /home/adnac/nachocausal/debates/2026-09-11--debate-continuacion-proyecto-v2.md ¿Cómo debería continuar nachocausal a partir del estado actual del repositorio? Debéis producir una recomendación operativa y priorizada, respetando estrictamente los contratos congelados, la separación exploración/confirmación, las preguntas abiertas y los límites de las afirmaciones. Evaluad qué trabajo debe hacerse a continuación, qué debe evitarse, qué artefacto mínimo verificable debe cerrarse primero y bajo qué criterio se autorizaría el siguiente salto hacia Schwarzschild 3+1D. Distinguid hechos documentados del repositorio, inferencias y propuestas.` |
| Project | `/home/adnac/nachocausal` |
| Rules | `/home/adnac/sanedrin/reglas/codigo.md` |
| Host | OMENNACHO — Linux 6.6.87.2-microsoft-standard-WSL2 |

### Turns

| Finished (UTC) | Round | Member | Backend | Seconds | Words | Status |
|---|---|---|---|---:|---:|---|
| 2026-09-11T17:23:39Z | 1 | FABLE | claude -p | 43 | 371 | ok |
| 2026-09-11T17:23:40Z | 1 | ASTRA | codex exec | 1 | 39 | FAILED |
| 2026-09-11T17:25:09Z | 1 | CIRO | grok -p | 89 | 69 | ok |
| 2026-09-11T17:25:50Z | 2 | FABLE | claude -p | 41 | 380 | ok |
| 2026-09-11T17:25:53Z | 2 | ASTRA | codex exec | 3 | 39 | FAILED |
| 2026-09-11T17:30:10Z | 2 | CIRO | grok -p | 257 | 428 | ok |
| 2026-09-11T17:30:56Z | 3 | FABLE | claude -p | 46 | 354 | ok |
| 2026-09-11T17:30:59Z | 3 | ASTRA | codex exec | 3 | 39 | FAILED |
| 2026-09-11T17:34:12Z | 3 | CIRO | grok -p | 193 | 412 | ok |
| 2026-09-11T17:35:15Z | 4 | FABLE | claude -p | 63 | 357 | ok |
| 2026-09-11T17:35:16Z | 4 | ASTRA | codex exec | 1 | 39 | FAILED |
| 2026-09-11T17:37:28Z | 4 | CIRO | grok -p | 132 | 317 | ok |
| 2026-09-11T17:37:56Z | Residuo | FABLE | claude -p | 28 | 181 | ok |
| 2026-09-11T17:38:00Z | Residuo | ASTRA | codex exec | 4 | 39 | FAILED |
| 2026-09-11T17:39:40Z | Residuo | CIRO | grok -p | 100 | 187 | ok |
| 2026-09-11T17:40:34Z | Veredicto | FABLE | claude -p | 54 | 328 | ok |
| 2026-09-11T17:41:00Z | Veredicto | FABLE | claude -p | 26 | 328 | ok |

Turns: 17 · failed: 5 · model time: 18m 4s

Full log: `2026-09-11--debate-continuacion-proyecto-v2.log`
