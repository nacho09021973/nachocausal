# C5 F1–F7 synthetic suite report

STATUS: SYNTHETIC_FINITE_POSET_SUITE / CANDIDATE_5_NOT_YET_OPENED
NO_PROJECT_GENERATOR / NO_EVALUATION_SEEDS / NO_FREEZE / NO_RECONSTRUCTION_CLAIM

Runner: `dev/c5_f1_f7_synthetic_suite.py`

## Summary

Overall: **SUITE_FAIL**

| Falsifier | Result |
|---|---|
| F1 | PASS |
| F1b | PASS |
| F2 | PASS |
| F3 | FAIL |
| F4 | PASS |
| F5 | PASS |
| F6 | PASS |
| F7 | PASS |

## Units

### F1 / bridge_vs_phiV — `PASS`

- primary: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`
- control: `ABSTAIN` part=`None`
- note: Φ★_L EMIT while Φ_V abstains (equal V)

### F1 / two_V_classes — `INCONCLUSIVE`

- primary: `ABSTAIN_ROOF_UNSTABLE` part=`None`
- control: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`
- note: primary=ABSTAIN_ROOF_UNSTABLE control=EMIT

### F1b / bridge — `INFO`

- primary: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`
- note: V=[5, 5, 5, 5]

### F1b / cross — `INFO`

- primary: `EMIT` part=`[['m1', 'm3'], ['m2', 'm4']]`
- note: V=[5, 5, 5, 5]

### F1b / pair_separator — `PASS`

- primary: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`
- control: `EMIT` part=`[['m1', 'm3'], ['m2', 'm4']]`
- note: same V=[5, 5, 5, 5]; parts [['m1', 'm2'], ['m3', 'm4']] vs [['m1', 'm3'], ['m2', 'm4']]

### F2 / roof_only_equal_mid — `PASS`

- primary: `ABSTAIN_SPECTRAL_MULTIPLICITY` part=`None`
- note: roof-only → ABSTAIN_SPECTRAL_MULTIPLICITY (no stable detection)

### F2 / roof_only_asymmetric — `PASS`

- primary: `ABSTAIN_SPECTRAL_MULTIPLICITY` part=`None`
- note: roof-only → ABSTAIN_SPECTRAL_MULTIPLICITY (no stable detection)

### F3 / wall_vs_bridge — `FAIL`

- primary: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`
- control: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`
- note: side-wall surrogate PATTERN_EQ bridge emission (twin-pair ambiguity)

### F3 / wall_vs_cross — `PASS`

- primary: `EMIT` part=`[['m1', 'm3'], ['m2', 'm4']]`
- control: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`
- note: wall=EMIT/[['m1', 'm2'], ['m3', 'm4']] ≠ cross

### F4 / same_cloud_mink — `INFO`

- primary: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`

### F4 / same_cloud_warped — `INFO`

- primary: `ABSTAIN_SPECTRAL_MULTIPLICITY` part=`None`

### F4 / same_cloud_compare — `PASS`

- primary: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`
- control: `ABSTAIN_SPECTRAL_MULTIPLICITY` part=`None`
- note: MINK=EMIT/[['m1', 'm2'], ['m3', 'm4']] vs warped=ABSTAIN_SPECTRAL_MULTIPLICITY/None

### F5 / density_lobe — `PASS`

- primary: `ABSTAIN_SPECTRAL_MULTIPLICITY` part=`None`
- control: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`
- note: no EMIT on density unit (ABSTAIN_SPECTRAL_MULTIPLICITY)

### F6 / height_base — `INFO`

- primary: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`

### F6 / height_extended — `INFO`

- primary: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`

### F6 / height_compare — `PASS`

- primary: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`
- control: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`
- note: partition stable under roof-tower extension (not pure roof tracking)

### F7 / relabel_bridge — `PASS`

- primary: `EMIT` part=`[['m1', 'm2'], ['m3', 'm4']]`
- note: all tested relabelings conjugate

## Interpretation

**F3 FAIL is structural, not a runner bug.** The side-wall surrogate (two twin corridors with local roofs) produces the same peel-stable bipartition as the bridge mid pattern `{{m1,m2},{m3,m4}}`. So Φ★_L, on these finite units, does not separate wall-type reconvergence from the non-marginal mid pattern used as a positive control. This matches Decision 040 / lateral dual doctrine: side control cannot be internal to the map; wall combinatorics can mimic the signal.

Secondary unit `wall_vs_cross` may still PASS (diagonal mid pattern differs). Aggregate F3 remains FAIL while the critical twin ambiguity stands.

## Scope limits

- Finite synthetic posets only; not Poisson sprinklings of Schwarzschild.
- F4 uses a hand cloud with Minkowski vs warped cones — not the sealed same-cloud generator.
- F3 side wall is an order-only twin-corridor surrogate, not continuum box walls.
- F8 (emission rate floor) is out of scope for this suite.
- Spectral step uses Jacobi floats with multiplicity/zero tolerances; bridge/cross
  eigenvectors are known exact from F1b dossier and match here.

## Terminal

```text
C5_F1_F7_SUITE = SUITE_FAIL
F1 = PASS
F1b = PASS
F2 = PASS
F3 = FAIL
F4 = PASS
F5 = PASS
F6 = PASS
F7 = PASS
CANDIDATE_5_NOT_YET_OPENED
NO_EVALUATION_SEEDS
F3_STRUCTURAL_WALL_BRIDGE_AMBIGUITY = YES
```
