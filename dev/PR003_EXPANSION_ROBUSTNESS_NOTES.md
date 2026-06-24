# PR-003 — expansion diagnostic robustness (S1 + S2, dev, NOT a result)

Sandbox notes for `docs/comite/comite_decision_002_*` (S1 minimal falsification test + S2
taller-box probe). Produced by `dev/measure_expansion_robustness.py`. **Exploration only —
nothing frozen, not validated, not audited.** Scored with hidden `r` (reveal ONLY to score).
EXPLORE_POOL[:2] seeds, `make verify-seal` = `6e2c3888…` before and after.

## S1 — minimal falsification test (does the sign-change survive WITHOUT the direction split?)

Fase #1-B builds the EGS Eq.14 expansion estimator only on the OUTGOING ladders, split by an
order-only proxy (`relphi_mean > median`) the dev notes flag as **ABSTAIN / unreliable**
(`PR003_EXPANSION_NOTES.md:53`). S1 re-runs at t_edge=6, intensity=3600 with the split vs with
**all ladders pooled**.

| variant | interior bins (r<R_S) | contrast BH | zero-crossing r* | d_perp/ell | flat ctrl |
|---|---|---|---|---|---|
| WITH split (Fase #1-B) | all NEGATIVE (−0.122,−0.026,−0.074,−0.017) | +0.138 | **0.508** | **0.84** | PASS |
| NO split (pooled) | mostly POSITIVE (+0.067,−0.041,+0.034,+0.026,+0.092,+0.128) | +0.110 | **0.283** | **2.78** | PASS |

**Verdict S1: the LOCALIZING signal does NOT survive removing the split.** The "contrast > 0"
is misleading — without the split the exterior is merely *more positive* than the interior (a
non-localizing gradient); the **interior negativity (true Θ_out<0) and the zero-crossing at R_S
both vanish**, the crossing drifting to r*=0.283 (d_perp 2.78 ℓ). So the clean apparent-horizon
signature at 3600 **depends on the `relphi` selection** — exactly the unreliable/possibly-leaky
channel the falsifier flagged (`comite_decision_002` §5). This partially vindicates the falsifier.

## S2 — taller-box probe at FIXED density (the physicist's lever)

`numpy_sprinkle` draws N=Poisson(intensity) in box [0,t_edge]×R_EDGE, so to hold density fixed
while raising timelike extent we scale intensity: (t_edge, N) = (6,3600),(12,7200),(24,14400),
giving ell≈0.0447 throughout. EGS (md:188-191,450) claim the contrast sharpens with timelike
extent; this tests it. split=True (the localizing config from S1).

| t_edge / N | samples BH | contrast BH | zero-crossing r* | d_perp/ell | flat ctrl |
|---|---|---|---|---|---|
| 6 / 3600  | 2751 | +0.138 | 0.508 | **0.84** | PASS |
| 12 / 7200 | 2834 | +0.052 | 0.404 | **2.49** | **FAIL** |
| 24 / 14400| 2392 | +0.087 | 1.202 | **10.54** | PASS |

**Verdict S2: a taller box at fixed density does NOT restore/strengthen the signal — it
DEGRADES.** d_perp/ell climbs 0.84 → 2.49 → 10.54; the zero-crossing drifts AWAY from R_S=0.5 as
the box grows (to r*=1.20 at t_edge=24, nowhere near the horizon). The physicist's hypothesis
(short box was the cause of interior undersampling) is **not supported** by this instrument.

- **Clean point (t_edge=12):** sample count is essentially unchanged (2834 vs 2751) yet the
  signal collapses and the flat control FAILS — so the t_edge=12 degradation is **not** an
  artefact of fewer samples; it is real degradation of the diagnostic with timelike extent.
- **Confound (t_edge=24):** `build_ladders(max_starts=500)` is FIXED regardless of box volume, so
  at 4× box the ladder coverage per unit t* drops (samples 2392). The t_edge=24 row is therefore
  partly confounded by under-sampling of ladders; a cleaner test would scale `max_starts` with
  box volume. The t_edge=12 row (uncounfounded) already refutes the hypothesis.

## Combined reading (honest)

The order-only **expansion / Θ_out diagnostic is fragile**: (S1) its localizing signature
depends on the unreliable `relphi` direction split, and (S2) it does not become density-robust
via the taller-box lever — it degrades both under higher density (the original 7200 result) AND
under longer timelike extent at fixed density. EGS themselves flag the method as needing
"numerous sprinklings to converge" (md:469). On this evidence the expansion variant is **not**
the path to a density-robust extended horizon object in this 1+1D patch with this proxy.

This does NOT touch the iterative-reseed v0 (the empirically-leading path, `comite_decision_002`
S3, not yet run). It only closes the expansion branch as a robust localizer.

**What it does NOT show:** not a frozen/validated/audited result; 2 seeds; the order-only `sep`
diamond proxy is a v0 (EGS warn of asymptotic silence at small separation, md:441); the t_edge=24
row is confounded by fixed `max_starts`. No threshold was touched; no "apparent horizon" claim is
made — only finite-patch 1+1D localisation of r_S, which here FAILS to be robust.

**Open uncertainty (one line, no plan):** whether ANY order-only direction discriminator (not the
broken `relphi`) could make the Θ_out sign-change both genuine and density-robust is left open;
on current evidence the expansion path is set aside in favour of iterative-reseed (S3).
