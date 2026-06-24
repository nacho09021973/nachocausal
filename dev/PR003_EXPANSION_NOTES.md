# PR-003 Fase #1-B — apparent horizon by discrete-expansion sign change (dev, NOT a result)

Sandbox notes for `docs/hoja_de_ruta_24_jun_2026.md` Fase #1 (variant B, the CANONICAL diagnostic).
Produced by `dev/measure_expansion_horizon.py`. **Exploration only — nothing frozen, not validated,
not audited.** Scored with hidden `r` (reveal ONLY to score). Pivot to B авал by the committee /
the literature note `biblioteca/Anticadenas_Benincasa.md` + EGS arXiv:2605.06813.

## What it does (order-only, blind)

EGS define the apparent horizon as Theta_out(r)=0 (md:201,225); Theta_out=(1/r)(1−2M/r): **+ for
r>2M, − for r<2M, 0 at R_S**. Discrete counterpart (Eq. 14, md:276-287): pairs of fuzzy ladders,
logarithmic change of the SPATIAL DISTANCE between them along the rung index → mean(E) changes sign
across the horizon. EGS used the embedding for those distances; here it is **order-only**:
`sep(u,v) = sqrt(|smallest enclosing causal diamond|)` (highest common past e, lowest common future
f, `|[e,f]|`). `r` revealed only to score WHERE mean(E) crosses zero.

## Result (2026-06-24, 6 seeds EXPLORE_POOL[:6], t_edge=6)

| intensity | ell | r* (pooled) | r* per-seed med [min,max] | d_perp(r*)/ell | contrast BH (hi vs lo) | contrast MINK | flat ctrl |
|----------:|----:|:-----------:|:--------------------------|:--------------:|:-----------------------|:--------------|:---------:|
|     3600  | 0.0447 | **0.491** | 0.503 [0.445, 0.566]   | **0.72**       | +0.134 (+0.074 vs −0.059) | +0.019 (no crossing) | PASS |
|     7200  | 0.0316 |   nan      | 0.551 [0.483, 0.560]   | 1.60           | +0.071 (+0.082 vs **+0.011**) | +0.026 (r*=0.194 noise) | PASS |

Interior bins (mean(E) below R_S): **3600** r=0.31..0.49 = −0.168 / −0.012 / −0.029 / −0.001
(negative, converging). **7200** r=0.37..0.55 = +0.027 / +0.015 / +0.050 / +0.033 (positive — the
interior negativity is GONE).

## Reading (precise — mixed; do NOT overclaim)

- **POSITIVE, headline (3600):** the canonical EGS apparent-horizon signature is **reproduced
  order-only and blind** — mean(E) is negative inside R_S (geodesic convergence, Theta_out<0) and
  positive outside, with the zero-crossing **at r*≈0.49–0.50 (d_perp 0.72 ell)**. The MINK
  same-cloud flat control shows **no interior convergence and no sign change** (positive throughout),
  so the signal is **horizon-specific**, not a coordinate/boundary artifact of the diamond proxy.
  This is the strongest, most physically defensible PR-003 signal so far.
- **NEGATIVE / blocking (7200):** the signal **does NOT converge — it degrades with density.** At
  7200 the interior-negative region disappears from the pooled profile (interior bins go positive),
  the pooled zero-crossing is undefined, and d_perp grows 0.72 → 1.60 ell. The per-seed crossing
  median (0.551) still brackets R_S, so per-seed localisation is not lost, but the **interior
  convergence structure and the precision both weaken**, the opposite of the Fase #1 success
  criterion "no degrada (idealmente mejora) con densidad".
- **Probable cause (UNDETERMINED with 2 densities):** the interior (r<R_S) is **undersampled** —
  few long ladders survive inside (singularity-truncated futures), so the negative-expansion bins
  thin out and wash away as ell shrinks. Whether this is fixable (more interior ladders, a better
  order-only sep proxy, larger seed count) or intrinsic is open.

## What it does NOT show

- NOT convergence — robustness with density is **not** established (it worsens at 7200).
- NOT a frozen/validated/audited result; ONE v0 instantiation; scored with hidden r.
- The order-only `sep` proxy (enclosing-diamond cardinality) is a v0 choice, not EGS's coordinate
  distance; the zero-crossing is a coarse interpolation of binned means; the direction split
  (`relphi`, provisional #2) is unreliable (the ingoing cross-check did not behave).
- MINK is not perfectly flat (mild +offset from boundary/proxy), so the discriminant is "BH
  sign-flip vs MINK monotone-positive", not "BH-positive vs MINK-zero".

## Verdict (exploratory)

**PARTIAL.** Blind reproduction of the EGS Theta_out sign-change at R_S is achieved at 3600 (a real
positive), but Fase #1-B **fails the convergence requirement** at 7200. The apparent-horizon
diagnostic is the right physics and works at one density; making it **density-robust** (chiefly the
interior undersampling) is the open obstacle.

**Open uncertainty (one line, no plan):** whether the interior-expansion signal can be made
density-robust (sampling vs proxy vs intrinsic) is what this v0 leaves unresolved.
