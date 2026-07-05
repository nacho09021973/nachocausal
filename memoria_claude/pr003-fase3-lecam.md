---
name: pr003-fase3-lecam
description: PR-003 Fase
metadata: 
  node_type: memory
  type: project
  originSessionId: 7e004ff0-2fa1-4158-94c4-a9157e033783
---

PR-003 entered **Fase #3** after S3 iterative-reseed failed convergence (commit `6b3649e`).
Committee decision 003 (ACCEPTED 2026-06-24, `docs/comite/comite_decision_003_*.md`):
consolidate on the measured `BARE_RELOCALISATION` O(ℓ) floor and develop the **Le Cam/Fano
lower bound** as the Fase #3 *result*, scoped to THIS sealed estimator at finite V,ρ. Blind TDA
deferred (R0 gate found it DECOUPLED). K-beam only under the guarded R2 protocol.

**Done this session (2026-06-24, reversible dev, nothing frozen):** O3 numerical illustration of
the Le Cam bound — `dev/measure_info_bound_o3.py` (GPU via `dev/backend.py`, RTX 5060), 24
EXPLORE_POOL seeds × 4 frozen intensities. Result: order-only localisation floor scales as
`ℓ=ρ^(-1/2)` — `r̂` scatter `≈0.4·ℓ` density-invariant, TVg(r̂) curves collapse vs `s/ℓ`; the
constant is O(1) **< K_LOC=2 ⇒ K_LOC=2 is a conservative (safe) floor**. GPU=CPU bit-identical for
the future-volume observable (maxdiff=0 at N≈12000). Written up in `dev/PR003_INFO_BOUND_NOTES.md`
§6. Seal `6e2c3888…` intact before+after.

**R2 done (2026-06-25, reversible dev, GPU):** guarded K-beam peel-off falsification —
`dev/measure_kbeam_peeloff.py` (GPU BH build + transitive-reduction C·C matmul; K-beam on numba),
6 EXPLORE_POOL seeds × {3600,7200,14400}, t_edge=6. Verdict: **peel-off NOT cured by K** — as K
grows 1→64 the order-only top-1 ladder's d⊥/ℓ at depth 8 stays ~5-7ℓ (no improvement), min-beam
plateaus ~4-6ℓ, only the head (k≤3) stays adherent ~2ℓ → evidence the wall is **PHYSICAL** (not
greedy myopia) → hardens the Le Cam bound. CAVEAT: under-reach at t_edge=6 (reach≥8 ≤23%) → label is
"PHYSICAL within box reach"; a taller box (t*/r_S∈[0,50]) is a NEW prereg (C2), the only way left to
reopen extension. Write-up `dev/PR003_KBEAM_PEELOFF_NOTES.md`. Seal `6e2c3888…` intact before+after.
NOTE: installing numba in .venv-gpu was required (added to requirements-gpu.txt); numba 0.65 +
numpy 2.4.6 + cupy 14.1 coexist.

**O1+O2 closed as sketches (2026-06-25, `dev/PR003_INFO_BOUND_NOTES.md` §7):** O2 = Jacobian
`dO/dr=ρ·dA_fut/dr` (log-enhanced near r_S via the tortoise `func`); with σ_O∝1/ℓ and dO/dr∝1/ℓ² the
ρ cancels → `δr=ℓ·√(A_fut)/(dA_fut/dr)` ∝ ℓ (O2★), constant ≈0.4 pinned by O3's σ(r̂). O1 = estimator-
output KL ≈3.1·(2s/ℓ)² reaches O(1) at 2s≈0.57ℓ (matches O3 TVg=0.5 at ~0.6ℓ); Bretagnolle–Huber →
O(ℓ) floor. Sketches, NOT theorems; freeze nothing.

**CORRECTION 2026-07-05 (this paragraph was stale):** the C1 freeze DID happen —
`docs/preregistration_003.md` is FROZEN 2026-06-25 (doc-only result, seal `6e2c3888…` intact,
full chain: comité 003/004, auditor 001/002 PASS, W1 discharged via sealed-numpy reruns, PI
authorised). Remaining open items live in prereg-003 §7: minimax-over-C (OPEN), O4 literature
sourcing (Tsybakov/Bretagnolle–Huber ABSENT from biblioteca), C2 taller-box prereg (parked).
Original stale text follows for history: ~~**Still pending (Fase #3):** **C1 freeze** of the Fase #3 result (Le Cam bound + R2 hardening) = needs
new prereg + `/comite` + `/auditor`, NOT yet authorised.~~ O4 (source Tsybakov 2009 / causal-set info-
theory precedent into biblioteca/). Optional: taller-box prereg to settle R2's under-reach caveat.
Net: the Le Cam result now has anchor(§3)+numerical(§6/O3)+analytic(§7/O1-O2) legs — ready for a C1
freeze proposal when the user authorises a committing step.

UNCOMMITTED as of 2026-06-25: O3+R2 probes, notes, requirements-gpu.txt numba line, and prior-session
GPU infra (dev/backend.py etc.) are all working-tree only — left for user to review/commit (dev/
__init__.py is marked "NOT committed", so commit-intent of the GPU batch is ambiguous).

GPU path: see [[gpu-exploration-backend]]. Prior FAIL + estimator-v2 history: [[estimator-v2-exploration]].
