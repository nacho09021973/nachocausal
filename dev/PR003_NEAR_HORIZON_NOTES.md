# PR-003 point 3 — near-horizon dev measurement (exploration only, NOT a result)

Sandbox notes for `docs/hoja_de_ruta_23_jun_2026.md` point 3. No verdict, no frozen
threshold. Produced by `dev/measure_near_horizon.py` (bracket-seeded LONGEST fuzzy
ladders; order-only build, coords reveal only to score direction / d_perp / near mask).
Regime: intensity=3600, t_edge=6, ell=0.0447, R_S=0.5.

## What was measured (2026-06-23)

Pooled over EXPLORE_POOL[:12] = 300 bracket-seeded longest ladders (length >= 6).
Direction truth = sign(delta r) along the ladder; near band in ell units of mean_r.

| band      | ladders | out / in | d_perp/ell (median) | AUC relphi_mean |
|:----------|--------:|---------:|--------------------:|----------------:|
| all       |     300 |  56 / 244 |                  —  |           0.942 |
| < 5 ell   |     229 |  18 / 211 |               3.04  |           0.954 |
| < 3 ell   |     127 |   2 / 125 |               2.27  |   0.908 (n_out=2) |
| < 2 ell   |      72 |   1 / 71  |               1.46  |   0.803 (n_out=1) |

(3-seed pre-check agreed: AUC(all) relphi_mean 0.937; <3ell all-inward.)

## Findings (anchored to the run above)

1. **Direction feature winner: `relphi_mean`** (mean relative-exteriority of L_fut along
   the ladder). AUC(all) = 0.942, AUC(<5ell) = 0.954, stable from 3 -> 12 seeds. The other
   two features (`phi_slope`, `relphi_slope`) are weak/unstable. Candidate for the frozen
   direction discriminant (#2) — but see limit 2.

2. **Near-horizon longest ladders are overwhelmingly INGOING — robust, not small-sample.**
   Within 3 ell of the horizon only 2/127 ladders are outgoing (1/72 within 2 ell). The
   "outgoing fuzzy ladder tracing the horizon" (EGS Sec V) is rare under longest-from-bracket
   selection. The direction AUC at <3 ell rests on 1-2 positives -> NOT yet a measurement of
   direction *at* the horizon, only at the ~5 ell scale.

3. **Longest selection does NOT reach d_perp ~ O(ell).** Band-conditional d_perp medians
   (1.46 / 2.27 / 3.04 ell) just track the band cut; the longest ladder sits ~3 ell off and
   drifts (cf. measure_pr003: longest tail d_perp ~ 4.5 ell vs greedy tail ~ 0.5 ell). The
   roadmap target "push d_perp toward O(ell)" conflicts with "select the longest ladder".

## Open question this forces (for roadmap point 2, the freeze)

Is the d_perp ~ 3 ell offset a **density (discreteness-floor) artifact** that shrinks toward
O(1) as intensity grows, or a **fixed property of longest-from-bracket selection**?
- If it shrinks with density -> the convergence success criterion holds; freeze as-is.
- If it plateaus -> the selection rule #3 must change (longest is wrong; need an outgoing /
  near-staying selection), before anything is frozen.
Decisive next measurement: a **density sweep** of near-horizon d_perp/ell.

## Density sweep result (2026-06-23) — `dev/sweep_near_horizon_density.py`

6 seeds, t_edge=6 fixed, intensity 3600 -> 7200 -> 14400 (ell 0.0447 -> 0.0316 -> 0.0224,
a ~2x density doubling each step; ell ∝ intensity^-1/2). d_perp/ell split head (first-3
rungs, near the bracket seed) vs tail (rungs 3..).

| intensity |   ell  | ladders | first3 d_perp/ell | tail d_perp/ell | AUC dir (all) |
|----------:|-------:|--------:|------------------:|----------------:|--------------:|
|     3600  | 0.0447 |     148 | 2.34 [1.30,3.52]  |            4.37  |        0.943  |
|     7200  | 0.0316 |     211 | 2.86 [1.26,4.16]  |            6.17  |        0.966  |
|    14400  | 0.0224 |     231 | 2.59 [1.36,4.00]  |            7.56  |        0.960  |

### Verdict (head converges, tail diverges — NOT the script's first glib label)

- **HEAD (first-3 rungs): non-monotonic / FLAT at ~2.5 ell** (2.34 -> 2.86 -> 2.59, big
  overlapping IQRs). Bounded in ell units across a 4x density change => the near-seed end of
  the ladder tracks the horizon at the discreteness floor: physical d_perp = ~2.5 ell -> 0 as
  ell -> 0. This is just the prereg-002 bracket localisation re-appearing at the seed; it
  CONVERGES. Good.
- **TAIL (body of the ladder): MONOTONE-INCREASING (4.37 -> 6.17 -> 7.56).** The longest
  ladder's body drifts further from the horizon in ell units, and *worse* at higher density.
  "Longest" diverges.
- **DIRECTION (relphi_mean): robust across 4x density, AUC(all) 0.94-0.97.** Candidate #2 rule
  holds up. (Near-band AUC still rests on few outward examples: near out counts 1/6/2.)

### Implication for roadmap point 2 (the freeze)

The longest-from-bracket selection (#3) is **confirmed wrong as-is**: it converges at the head
but diverges in the tail, so the *object it returns* is a long ladder whose body leaves the
horizon. The horizon-tracking signal lives in the FIRST FEW rungs near the seed, not in the
length. Selection rule #3 must therefore pick a SHORT, near-staying ladder (or truncate the
longest to its converging head) — NOT the longest. The convergence success criterion can hold,
but for the head, not the whole ladder. Direction rule #2 (relphi_mean) is on track to freeze.
