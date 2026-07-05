# R-VAR Part F — Disposition Record

> Disposition-commit per `docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md`
> §9 step 4 ("Disposition-commit," committing step, requires explicit user authorisation —
> **authorized 2026-07-05**, PI adnacho, per comité 020 §11 sign-off note: "Steps 4–5 of §9
> ... remain pending as separate, explicitly-authorized committing steps").

## Status token

```
PARTF_STATUS = BLOCKED_BY_MEASURED_DEGENERACY [
  NEVER_EXECUTED;
  FROZEN_OBJECT_VACUOUS_ON_MINK_NULL_AT_PRODUCTION
    (strongly-supported empirical prediction, 12/12 dev draws certified);
  COMPUTE_BLOCKER_SECONDARY (014d364)
]
```

This is a **third explicit state** — not `PASS`, not `FAIL`, not
`OUT_OF_DOMAIN_UNCALIBRATED`. The `OOD` token is reserved for an actual Part F run that
exhausts its block under the frozen addendum's §4c rule (`dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md`);
Part F step 3 (the μ computation) has never been executed and this record must not be read as
implying otherwise (comité 020 §8, falsifier precision (i)).

## What this means

Part F (μ-calibration over MINK nulls, frozen `0271fd9`) cannot proceed as specified: the
frozen calibration object 𝒜(C) is certified empty (`unrelated_min_max_pairs = 0`, 12/12 dev
draws across all 4 production intensities) on its own MINK null substrate, by box-geometry
necessity (`R_EDGE=1.2 ≪ T_EDGE=6`, `nachocausal/thresholds.py:36-40`) — a degeneracy that
*worsens*, not improves, with N. This is independent of the separate compute-feasibility
blocker already on record (`014d364`, `2^40` enumeration `INFEASIBLE` for the only
Gate-0-verified implementation); the degeneracy binds even under unlimited compute.

Corresponding facts, in the black-hole leg: 100% of minimals have partial intervals (family
potentially nonempty via horizon-interior singularity-truncation structure), but full H≠∅
non-emptiness rests on claim-inert demo output, not a certified fact (comité 020 §5 falsifier
attack 4) — this record does not assert BH-side non-emptiness as certified.

## What this does not do

- Does **not** close R-VAR. The PI's signed direction (comité 020 §11.3) re-scopes the
  immediate goal to an order-only Schwarzschild-singularity-truncation localisation with a
  graded observable and non-degenerate MINK null, to be defined by a **new** `/comite`
  question — not a repair of Part F.
- Does **not** touch the Part E "polynomial for every finite poset" over-claim
  (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:489-501`); that re-scope is comité 020 §9 step 5,
  a separate committing step, deliberately not bundled into this one.
- Does **not** rehabilitate the interval-DP candidate for scoring use: the cross-key probe
  (`5014a39`, `dev/rvar_crosskey_probe_result.json`) confirmed branch (a) — the DP's
  certificate/argmax depend on the hidden BH/MINK label through the sort key, i.e.
  ground-truth leakage — so the DP stays disqualified pending an order-only key derivation
  (comité 020 §8(2), §9 step 7 preconditions a–e).
- Does **not** touch the sealed estimator-v2 path. `make verify-seal` must continue to match
  `docs/preregistration_002.md:8`; nothing under R-VAR reads or writes `nachocausal/thresholds.py`.

## Anchors

| Fact | Source |
| --- | --- |
| 𝒜(C)=∅ certified, 12/12 MINK draws, all 4 intensities | `6347459`, `dev/rvar_structure_probe_result.json` |
| Compute blocker: 2^40 enumeration INFEASIBLE (family_A, only Gate-0-verified impl) | `014d364`, `dev/rvar_partF_feasibility_probe_result.json` |
| Frozen Part F object / OOD third-state rule (§4c) / rate_empty CLAIM-INERT (§4d) | `0271fd9`, `dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md` |
| Adjudication record (comité 015–020, auditor 003–006), addendum tightening edit | `4a408a8` |
| Cross-key probe: branch (a), key-dependence / leakage confirmed, DP blocked | `5014a39`, `dev/rvar_crosskey_probe_result.json` |
| Disposition adjudication and PARTF_STATUS token text | `docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md` §9 step 4, §11 |
| Seal unaffected | `make verify-seal` → matches `docs/preregistration_002.md:8` |

## Next steps (not authorized by this record)

Per comité 020 §9: step 5 (Part E re-scope amendment) and step 6 (new `/comite` question for
the graded singularity-truncation object) remain separate, explicitly-authorized committing
steps, sequenced after this one.
