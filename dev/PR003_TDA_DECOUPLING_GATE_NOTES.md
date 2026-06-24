# PR-003 R0 — TDA decoupling gate (dev, NOT a result; zero new runs)

Authorised by `docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md` §9 step R0
(= the falsifier's minimal falsification test, §5). **No new simulation is run here** — this reads
only the *already-committed* S3 table to decide whether a thickened-antichain persistent-homology
(TDA H0) probe could add recoverability evidence, or would merely re-image the S3 negative on a
metric decoupled from the pre-committed success bar.

Provenance: HEAD `6b3649e`, branch `main`, `make verify-seal` = `6e2c3888…` (unchanged; this note
runs no sealed code). Source table: `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md:27-29`.

## The committed S3 numbers (verbatim)

| intensity | ℓ | d⊥/ℓ | honest coverage | connectivity |
|---|---|---|---|---|
| 3600  | 0.0447 | 0.52 | **51%** | 90% |
| 7200  | 0.0316 | 0.63 | **48%** | 95% |
| 14400 | 0.0224 | 0.88 | **44%** | 93% |

## The gate

A TDA H0 probe reports, in essence, **"a long-persistence connected band exists with no MINK
counterpart."** Its signal is *band connectivity / component persistence*. The pre-committed Fase #1
success bar (`docs/hoja_de_ruta_24_jun_2026.md:64,104`) is *honest coverage does not degrade with
density* (ideally improves), with the per-piece bracket staying O(ℓ).

**Decision rule (R0):** if the persistence/connectivity proxy is flat-or-rising while honest
coverage degrades across densities, the TDA signal is *decoupled* from the success criterion, and a
blind TDA probe is **disqualified as recoverability evidence** (it can report TRUE on a geometry the
pre-registration scores FAIL). In that case steps T1 (TDA probe) is NOT run.

## Verdict: DECOUPLED → blind TDA disqualified

- **Connectivity is high and does NOT track coverage.** As intensity rises 3600→7200→14400,
  connectivity is flat/stable (90→95→93%, no downward trend) while honest coverage falls
  *monotonically* (51→48→44%). The connectivity proxy and the success metric move in opposite or
  unrelated directions — they are decoupled.
- **The bracket actively worsens.** d⊥/ℓ grows monotonically 0.52→0.63→0.88; the per-piece locus is
  getting *wider in ℓ-units* as density rises — the opposite of convergence.
- A TDA H0 bar would therefore read "connected persistent band present" at all three densities
  (connectivity ≥90% throughout) **while** the pre-committed bar is FAILED at all three. The bar
  lifetime measures neither coverage nor d⊥/ℓ scaling, so it cannot rescue the negative; it can only
  relabel it.

**Conservatism note.** "Connectivity" here is the *weak* notion (any causal link between adjacent
fronts, not a through-chain — `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md:65`). A genuine H0-persistence
statistic over a thickness filtration would be *no stronger* at separating the band from the
coverage failure than this weak connectivity already is — if anything weaker-coupled to coverage.
So the decoupling conclusion is conservative: a real TDA bar would not do better than the proxy used
here, which already fails to track the success metric.

## Consequence (per comité-003 §9)

- **Skip the blind TDA probe.** T1 stays deferred behind its three prerequisites (a fallable TDA
  Guard-v; the missing homology literature — arXiv:0902.0434, Major–Rideout–Surya 2007,
  Cunningham–Surya 2018 — sourced into `biblioteca/`; a principled stability-plateau thickness anchor
  declared *before* any scored run). None is met today.
- Proceed instead to **R1** (Le Cam/Fano lower bound as the Fase #3 result) and optionally **R2**
  (guarded K-beam falsification).

This note is exploration; it freezes nothing and makes no claim beyond reading committed numbers.
