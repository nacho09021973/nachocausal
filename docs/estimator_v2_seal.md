# Estimator-v2 — instrument SEAL (prerequisite #2)

Status: **SEAL record.** The git commit introducing this file together with the
estimator-v2 `nachocausal/` code is the **estimator-v2 instrument seal**. The
seal is the SHA256 of `nachocausal/thresholds.py`.

- **New seal:** `nachocausal/thresholds.py` SHA256 =
  **`2f4c4a996d53e0949ebc2c39d5f4bef048d8bdcd9365cf0e8bef70783d90ca42`**
  (`make verify-seal`). Was `ad02cb57…` for the prereg-001 instrument.
- Implements **exactly** the frozen input contract
  `docs/estimator_v2_freeze.md` (commit `7d25c34`); decision `bb21147`
  (SHA256 `44f54495…`).

## What is sealed — exactly 3 changes vs prereg-001 (per the freeze)

- **(A) VOLUME observable** — `estimator.estimate_O_volume` (`O(i)=|future(i)|`,
  column-sum of C over minimal elements). The height oracle `estimator.estimate_O`
  is **retained** as the audited poset-integrity anchor (`tests/test_regression.py`).
- **(C) τ(n) abstaining gate** — `nachocausal/gate.py` + frozen
  `nachocausal/fixtures/tau_table.json` (n = 2..128). Params:
  `GATE_ALPHA=0.01` (p99), `GATE_NULL_MC_SEED=20260621`, `GATE_NULL_MC_REPS=40000`,
  uniform null; abstain (`sep→0`, no boundary claimed) iff `improvement < τ(n)`.
  Regenerate: `scripts/gen_tau_table.py`.
- **(D) domain gate `T_EDGE_MIN=6`** — `t_edge < 6 ⇒ verdict OUT_OF_DOMAIN`, a
  distinct status that is **never a physical FAIL**.

**Guard-v (v)** now verifies the **production (volume) observable**
(`verify_order_only` default), so it guards the quantity actually used (freeze
cl. v). Everything else — criteria forms/thresholds, geometry (area=7.2,
intensities, primary 12000), 20-seed ensemble, anchoring, PASS/FAIL aggregation —
is **inherited verbatim** from `docs/preregistration_001_addendum.md`.

## Evaluation order (freeze cl. H), realized in `validate.run`

`domain → estimator(volume) → gate(τ) → criteria`: `run()` applies the domain
gate first; `_per_seed` runs the volume estimator then the τ gate; `run_level`/
`run` apply the criteria.

## Verification recorded at this seal

- **20/20 tests pass** (`pytest`): height-poset regression bit-exact (oracle
  integrity), poset checksum, leak + **Guard-v-can-fail on the volume observable**,
  seed invariants, `test_estimator_v2` (volume/improvement/gate/domain/path),
  `test_tau_table` (τ prefix bit-reproducible from the sealed MC params).
- **Dry-run on DEV_SEEDS** (verdict DISCARDED, `python -m nachocausal.dry_run`):
  the sealed path computes; localisation (ii) and false-positive (iv) **PASS** at
  the primary; (i) significance is False **only** because 8 dev seeds cap the
  permutation at p≈3.9e-3 (the same artefact as the prereg-001 dry-run, not a
  result). Guard-v raised on no causet.
- τ fixture sample: `τ(16)=0.9057, τ(40)=0.8505, τ(71)=0.8265, τ(128)=0.8069`.

## VALIDATION_SEEDS — NOT prereg-002 yet (deferred to #3)

This seal is the **instrument only**. `thresholds.VALIDATION_SEEDS` still holds
the **burned prereg-001 set**; it is inert here. **Do NOT invoke `validate.run()`
on the default seeds as a prereg-002 verdict.** Prerequisite #3 (freeze
prereg-002) draws fresh held-out seeds from the reserved virgin band
`[2_000_000, 2_999_999]` and re-freezes — that will change the `thresholds.py`
SHA again (the prereg-002 seal). [user decision 2026-06-22]

## Provenance & sequence

Decision `bb21147` (SHA256 `44f54495…`) → freeze `7d25c34` → **this seal**.
numpy pinned `1.26.4` (`assert_environment`). Sequence:
**freeze #1 ✅ → integrate & test #2 ✅ (this) → [#3 freeze prereg-002: draw
held-out seeds + re-seal] → single blind run.**
