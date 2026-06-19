# Roadmap — recovering the 1+1D Schwarzschild horizon from causal-set order

Status: ROADMAP (revisable planning, not a frozen result and not a pre-registration).
It sets no thresholds and reports no verdict. Each numbered phase becomes its own FROZEN
pre-registration before any of its validation data is generated.

Ultimate goal: recover Schwarzschild **horizon structure** from causal order alone, as a
*recoverability benchmark* — never a reconstruction claim (`docs/preregistration.md:69-72`).

## Strategy decided (2026-06-18)

- **Framing A1** — escalate as independent falsifiable recoverability benchmarks, not a
  construction claim.
- **Next step B1** — close pre-registration 001 to a frozen *result* before adding any new
  observable.
- **Compute C1** — stay on the dense N×N poset (ceiling N≈2–3·10⁴, `docs/reuse_check.md:30-37`);
  escalate to a sparse/graph redesign only when a phase provably needs it.
- **Dimension D1** — solve 1+1D fully first; 3+1D is a distant phase.

Every phase honours the founding rules unchanged: a guardrail that can fail; dev/validation
strictly separated with disjoint documented seeds; thresholds anchored to principled bases and
frozen in writing before any validation seed is analysed; ground truth only scores; and the
**independent falsification gate** before escalating any verdict's strength
(`docs/preregistration.md:25-78`).

## The three routes to the horizon (the goal, decomposed)

Grounded in Eichhorn, Gamito & Stokes, *Towards black-hole horizons and geodesic focusing in
causal sets* (arXiv:2605.06813, published 2026-05-07; PDF in `biblioteca/`). [arXiv id
cross-checked via alphaXiv on 2026-06-18.]

1. **Event horizon via longest timelike chain** (paper Sec. III). Interior minimal elements have
   futures truncated by the singularity → **bimodal** longest-chain distribution → interior/
   exterior partition with boundary at r=2M. This is exactly PR-001's observable
   (`dev/prototype_o.py:166-197`). Caveat from the paper: this diagnostic is singularity-specific
   and is expected to **fail for regular black holes** (Hayward) in 3+1D.
2. **Apparent horizon via causal ladders + discrete geodesic expansion** (paper Sec. IV). Ladders
   (the paper's ref [15] = *Null Geodesics from Ladder Molecules*, arXiv:2301.06480, 2023) trace
   null geodesics; the discrete
   expansion **E changes sign across r=2M** (Θ_out=0 at the horizon). Local, physically defined,
   survives regular black holes. Costly: needs many sprinklings for mean(E) to converge and a
   mandatory **Minkowski-baseline subtraction**.
3. **Discrete horizon via fuzzy ladders** (paper Sec. V). Relaxed-rigidity ladders trace the
   outgoing null geodesic that "peels off" near r_S, **constructing a portion of the horizon**.
   Newest ground (fuzzy ladders ≈ May 2026; primary literature minimal per
   `biblioteca/fuzzy_ladders_comprehensive_literature_review.md`) — highest payoff, highest
   tuning risk.

## Phased plan

### Phase 0 — close PR-001 to a frozen result  ← ACTIVE
The pre-registration, prototype, accelerator and guards exist; what is missing is a measured
signal and a frozen verdict (`README.md:20-22`).

1. **Measure signal on dev.** Per-sprinkling N and ensemble size for a clear bimodality of O
   are still `[UNVERIFIED]` (`docs/reuse_check.md:39-40`). Sweep N up to the dense ceiling
   (~2·10⁴) and seeds/ρ/extent on dev seeds only; record where bimodality is unambiguous.
2. **Select & freeze the order-only boundary definition** from the candidates (antimode
   threshold of O, inter-class link membrane, or cluster edge) — chosen for stability, never for
   best match to ground truth (`docs/preregistration.md:27-31`).
3. **Freeze thresholds** by the anchoring rule (θ_loc=k·ℓ/(2M) with ℓ=ρ^−½, θ_sig as a fixed-
   level dip test, θ_stab a multiple of ℓ, θ_fp≤5%) — in writing, before any validation seed
   (`docs/preregistration.md:47-57`).
4. **Generate validation** on a disjoint documented seed set; run BH + box-matched Minkowski
   controls; score blind, reveal embedding only to measure distance to hidden r=2M.
5. **Independent falsification gate** (separate session/tool, blind, tasked to break it).

Exit: the project's first frozen verdict (success / failure / inconclusive), committed.

### Phase 1 — null-geodesic infrastructure
Links + transitive reduction and rigid-ladder detection as an order-only observable, with its own
fail-able Guard-v analogue. Reuses `biblioteca/Geodesicas_nulas.md` and the fuzzy-ladders review.

### Phase 2 — apparent horizon (PR-002)
Discrete expansion E with Minkowski subtraction; falsifiable criterion = **sign change of E
localises r=2M**. Likely the first phase to hit the dense compute ceiling → reassess fork C.

### Phase 3 — discrete horizon (PR-003)
Fuzzy ladders → construct and blind-score a portion of the horizon. The phase closest to
"construction"; keep the benchmark framing (fork A1) and watch the forbidden-claims line.

## Open / to verify

- N and ensemble size for a clear bimodality signal — measured on dev in Phase 0
  (`docs/reuse_check.md:39-40`).
- Dense N×N ceiling ≈ 2–3·10⁴ here; routes 2/3 may force a sparse/graph redesign of generation
  **and** estimator (`docs/reuse_check.md:34-37`).
- Adjacent literature for a possible later entropy phase (out of current scope): *On the horizon
  entropy of a causal set* (arXiv:2012.06212), Boltzmannian horizon-molecule state counting
  (arXiv:2404.11670). The 2D causal structure used here is He–Rideout (arXiv:0811.4235).
