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

### Verdict (precise — what the 3-point sweep does and does NOT establish)

- **HEAD (first-3 rungs): d_perp/ell stays bounded around ~2.5** (2.34 -> 2.86 -> 2.59), but with
  large overlapping IQRs and **non-monotone**. This is **COMPATIBLE WITH** horizon localisation at
  discreteness precision (d_perp = O(ell)). It does **NOT** by itself demonstrate convergence, nor
  that the first-3 rungs form a seed-coherent horizon curve. (It is consistent with the prereg-002
  bracket localisation re-appearing at the seed.)
- **TAIL (body of the ladder): d_perp/ell GROWS (4.37 -> 6.17 -> 7.56).** So the longest-selected
  ladder **fails the required discreteness-scale adherence** — it does not stay at O(ell) of the
  horizon. This does **NOT** establish *physical* divergence: ell roughly halves over the sweep, so
  physical d_perp could still be decreasing (e.g. 7.56 * ell0/2 = 3.78 ell0 < 4.37 ell0), only
  slower than O(ell). Whether it scales as ell^a (0<a<1), logarithmically, or saturates is
  **undetermined** with three densities.
- **DIRECTION (relphi_mean): strong GLOBAL signal, AUC(all) 0.94-0.97** across the 4x sweep. The
  specifically near-horizon validation is still limited to **1/6/2 positive (outgoing) cases**.

### Frozen verdict (recorded; not yet designing the corrected #3)

- **#2 `relphi_mean`: retained PROVISIONALLY** — insufficient near-horizon support (1/6/2) for a
  definitive freeze.
- **#3 `longest`: REJECTED** as the selector of a complete horizon portion (fails discreteness-
  scale adherence along the tail).
- **Structural finding:** horizon information concentrates in the HEAD near the seed; the later
  growth optimises *length*, not *adherence*.
- **Single next question (do not pre-design alternatives):** does a head truncated by a rule
  defined *only* on causal observables produce a **connected** sequence whose distance to the
  horizon stays O(ell)?

## Single-next-question measurement (2026-06-24) — `dev/measure_truncated_head.py`

Exploration only, NOTHING frozen. 6 seeds (EXPLORE_POOL[:6]), t_edge=6 fixed, intensity
3600 -> 7200 -> 14400 (ell 0.0447 -> 0.0316 -> 0.0224, ~2x density per step). Per bracket-
seeded LONGEST ladder we record the per-rung `d_perp/ell` (hidden coord, SCORE ONLY) and the
cumulative-mean `rel_phi` (order-only #2 feature). `k*` = longest prefix whose **median**
`d_perp/ell` stays <= 3 (a *reference* band, NOT a frozen threshold). Run completed exit 0,
all densities present, **connectedness = 100%** at every density (every prefix is a verified
chain in C), no NaN/Inf, nothing dropped except sub-min_len ladders by design. The script
aggregates pooled-per-density; it did **not** emit per-seed breakdowns, so per-seed dispersion
is not available from this run (not reconstructed here).

| intensity | ell | ladders | conn | k* (rungs) | k*·ell (phys) | k* in ell-floors |
|----------:|----:|--------:|-----:|-----------:|--------------:|-----------------:|
|     3600  | 0.0447 |    148 | 100% |        3   |        0.134  |             3.0  |
|     7200  | 0.0316 |    211 | 100% |        2   |        0.063  |             2.0  |
|    14400  | 0.0224 |    231 | 100% |        3   |        0.067  |             3.0  |

`d_perp/ell` profile by prefix length k (median, pooled): rises monotonically at all three
densities — k=0 (seed rung) ~1.7-1.8 ell (the prereg-002 floor, stable in ell units), crossing
~3 ell by k=2-3, into the body 5-8 ell. The deep tail (k=15) **grows with density**
5.2 -> 6.5 -> 8.2, reconfirming the longest-tail divergence in ell units.

### Exploratory verdict (6 seeds): **BARE_RELOCALISATION**

- **Geometric result (measured with hidden `d_perp`).** A connected, geometrically adherent head
  **exists** but it is only the seed's discreteness neighbourhood: `k*` = O(1) rungs (3 / 2 / 3,
  no growth on refinement) and its **physical** extent `k*·ell` **halves with ell**
  (0.134 -> 0.067, x0.50, while ell shrank x0.50; k* in ell-floors stays ~2-3). This is the
  prereg-002 bracket localisation re-appearing at the seed, **not** a lengthening reconstructed
  horizon segment.
- **Rejected readings:** `FIXED_PHYSICAL_SEGMENT` (k*·ell did not stay constant — it tracked ell
  down; k* did not grow); `FAIL_GEOMETRIC_ADHERENCE` (connectedness is 100% and the head *does*
  stay O(ell) for ~2-3 rungs — it is the body that leaves, the already-known longest behaviour);
  `NO_STABLE_SCALING` (the k* sequence wobbles 3->2->3, but the physical trend halving-with-ell and
  the stable ell-floor count ~2-3 are consistent; the 7200 dip to k*=2 is the one wobble, flagged).
- **`k*` is NOT an order-only rule.** It is read off `d_perp` (the hidden diagnostic geometry), so
  it is a geometric diagnostic only.

### Order-only detectability of the head end (`rel_phi`): **AMBIGUOUS / UNSTABLE**

- No cumulative-`rel_phi` breakpoint aligns with the geometric head end `k*` (2-3): the
  `relphi_cum` extremum sits around k~=5 at all densities, **past** k*.
- Scale/sign are not density-robust: 3600 hovers near 0 with mild oscillation
  (+0.5 ... -10.9 ... +12.6); 7200 plunges to ~ -65; 14400 to ~ -102. Magnitude grows with density
  but there is no stable breakpoint coincident with where geometric adherence is lost.
- => a signal exists at higher density but it is **not** a stable, aligned marker of the head end.
  (Not "clear aligned breakpoint"; not "no visible signal".)

### Greedy contrast: **UNDERPOWERED / inconclusive**

Greedy (stop-at-first-stuck) ladders reaching min_len=6 from the invariant bracket are **rare**:
n = 2 / 8 / 1 across 3600 / 7200 / 14400. Greedy length median 9.5 / 8 / 6 (shrinking), tail
`d_perp/ell` 6.40 / 5.72 / 0.88 — these vary wildly on n=1-8 ladders, so they are anecdotal, not a
measurement. The single n=1 tail of 0.88 at 14400 supports nothing. (Not comparable to the earlier
`measure_pr003` greedy-tail ~0.5 ell, which used a different seed set and 40-seed per-sprinkling
aggregation.) Greedy here neither confirms nor denies an adherent extended head.

**What this does NOT show:** no reconstructed horizon *segment* (extended, growing); no order-only
stopping rule (k* uses hidden geometry); and it does not settle whether some other, still-unmeasured
order-only truncation could extend adherence past the seed floor.

### Post-committee addenda (2026-06-24, R1/R2 — `comite_decision_001`)

- **Two distinct channels, do not conflate them:**
  - *Geometric channel* (scored with hidden `d_perp`): `BARE_RELOCALISATION` — the adherent head
    exists but is the seed's discreteness neighbourhood (k\*=O(1), k\*·ell halves with ell). Solid.
  - *Order-only detectability channel* (`rel_phi`, greedy): **ABSTAIN** — `rel_phi` gives no
    density-robust breakpoint aligned with the head end (extremum at k~5, past k\*=2-3; scale/sign
    not robust) and the greedy contrast is statistically empty (n=2/8/1). There is therefore **no
    order-only evidence that the head end is detectable from order alone.** This abstain is reported
    in its own right, not folded into the geometric verdict.
- **Tail growth is NOT a search-budget artifact** (falsifier's minimal test, run by the committee
  chair on `EXPLORE_POOL[0]`): complete-search fraction = 89% / 93% / 87% at 3600 / 7200 / 14400,
  and the tail (k>=10) `d_perp/ell` on COMPLETE-only ladders (6.21 / 8.95 / 10.07) matches the
  all-ladder values (6.00 / 9.11 / 8.23). So the ell-unit tail growth is real. **But** whether it is
  *physical* (vs ell-unit) divergence remains **undetermined** with three densities (ell roughly
  halves over the sweep, so physical `d_perp` could still be shrinking sub-O(ell)). `measure_truncated_head.py`
  now also reports the per-density complete-fraction and per-seed k\* dispersion (R1).
  **6-seed re-run confirms it:** complete-fraction = 86% / 90% / 79% at 3600 / 7200 / 14400
  (≈ the 1-seed 89/93/87%); per-seed k\* median[min,max] = 3[0,5] / 2[0,4] / 3[1,4] (wide spread).
- **Next:** roadmap `docs/hoja_de_ruta_24_jun_2026.md` — cascade #1 (iterative order-only
  re-seeding) -> #2 (order-only stopping observable) -> #3 (accept the bound), each leakage-gated,
  with the minimal falsification test (complete-only agreement / relabel Guard-v / MINK flat control)
  carried forward.

## Physical-tail scaling extension — 5-density exploratory sweep

**Commit y estado del árbol usados:** `c2e64b56ed9666455a2b134c9e87d0b58569ca8a` — árbol limpio
(ningún archivo modificado antes de este run; esta sección es la única modificación post-run).

**Comando exacto:**
```bash
cd /home/ignac/nachocausal
PYTHONUNBUFFERED=1 python3 -u - <<'PY' > /tmp/sweep_5density_raw.txt 2>&1
import sys, time
sys.path.insert(0, ".")
sys.path.insert(0, "dev")
from explore_seeds import EXPLORE_POOL
from sweep_near_horizon_density import run
print(f"START: {time.strftime('%Y-%m-%dT%H:%M:%S')}", flush=True)
summary = run(list(EXPLORE_POOL[:6]), [21600.0, 28800.0], t_edge=6.0)
print(f"END: {time.strftime('%Y-%m-%dT%H:%M:%S')}", flush=True)
print(f"summary={summary}", flush=True)
PY
```

**Ejecución:** START 2026-07-01T09:25:14 → END 2026-07-01T12:51:38 (3 h 26 min total).
- intensity=21600: 4 583 s (76.4 min) para 6 semillas.
- intensity=28800: 7 801 s (130.0 min) para 6 semillas.

**Salida literal nueva (intensidades 21600 y 28800):**
```
intensity= 21600  ell=0.0183  ladders= 251 [4583s]
   d_perp/ell  first3=2.84 [1.40,4.17]   tail=8.89   overall=7.77
   direction relphi_mean  AUC(all)=0.951  AUC(<3ell)=0.756  near out/in=3/26

intensity= 28800  ell=0.0158  ladders= 250 [7801s]
   d_perp/ell  first3=3.00 [1.53,4.98]   tail=10.16   overall=8.39
   direction relphi_mean  AUC(all)=0.959  AUC(<3ell)=0.486  near out/in=5/37
```

### Tabla completa de cinco densidades

Puntos 1-3 tomados de "Density sweep result (2026-06-23)"; puntos 4-5 del run actual.

| intensity |  ell   | ladders | first3 d⊥/ell [IQR]  | tail d⊥/ell | tail d⊥ físico | AUC(all) |
|----------:|-------:|--------:|----------------------:|------------:|---------------:|---------:|
|      3600 | 0.0447 |     148 | 2.34 [1.30, 3.52]    |        4.37 |         0.1953 |    0.943 |
|      7200 | 0.0316 |     211 | 2.86 [1.26, 4.16]    |        6.17 |         0.1950 |    0.966 |
|     14400 | 0.0224 |     231 | 2.59 [1.36, 4.00]    |        7.56 |         0.1693 |    0.960 |
|     21600 | 0.01826|     251 | 2.84 [1.40, 4.17]    |        8.89 |         0.1623 |    0.951 |
|     28800 | 0.01581|     250 | 3.00 [1.53, 4.98]    |       10.16 |         0.1606 |    0.959 |

**`tail d⊥ físico` = (tail d⊥/ell) × ell** — nunca confundir con `tail d⊥/ell` ni con `bl`:
- 3600:  4.37  × 0.0447  = 0.1953
- 7200:  6.17  × 0.0316  = 0.1950
- 14400: 7.56  × 0.0224  = 0.1693
- 21600: 8.890 × 0.01826 = 0.1623
- 28800: 10.158× 0.01581 = 0.1606

Cambios consecutivos en d⊥ físico:

| tramo           | Δ abs   | Δ rel  |
|:----------------|--------:|-------:|
| 3600 → 7200     | −0.0004 |  −0.2% |
| 7200 → 14400    | −0.0256 | −13.1% |
| 14400 → 21600   | −0.0070 |  −4.2% |
| 21600 → 28800   | −0.0017 |  −1.0% |

### Advertencias de comparabilidad

1. **Parámetros idénticos:** EXPLORE_POOL[:6], t_edge=6, min_len=6, lmax=120, M=3,
   budget=30000, selector `longest_censored`. Comparables con los 3 runs existentes. ✓
2. **Fracción de búsquedas completas no reportada** por `sweep_near_horizon_density.py`.
   El falsificador verificó a 3600/7200/14400 que las colas de búsquedas completas coinciden
   con las del total (ver addenda del comité, 2026-06-24); esa verificación no está disponible
   aquí sin modificar el script.
3. **Escalado temporal empírico:** entre 21600 y 28800 el tiempo escala como N^1.85
   (mucho mejor que el N^3.7 observado entre 14400 y 21600, probablemente efecto de caché).
   El presupuesto de búsqueda no se redujo.
4. **Script `MONOTONE-INCREASING` para first3:** el VERDICT READ-OFF del script cubre sólo
   los dos puntos nuevos (2.84 → 3.00). Sobre los 5 puntos totales, `first3 d⊥/ell` es
   **NON-MONOTONE** (2.34 → 2.86 → 2.59 → 2.84 → 3.00); la etiqueta del script no aplica
   al sweep completo.

### Respuestas a las tres preguntas

**P1. ¿`tail d⊥/ell` continúa creciendo, se estabiliza o cambia de tendencia?**

Crece monotonamente (4.37 → 6.17 → 7.56 → 8.89 → 10.16), pero los incrementos consecutivos
disminuyen: +1.80, +1.39, +1.33, +1.27. Esto extiende a cinco densidades el fallo exploratorio
de adherencia O(ell) para el selector `longest_censored` bajo el presupuesto fijo utilizado.
La completitud de la búsqueda en las dos densidades nuevas no fue registrada (ver advertencia 2
y veredicto `SEARCH_COMPLETENESS_AT_21600_28800`). La tasa de crecimiento adimensional se
desacelera pero no revierte.

**P2. ¿`tail d⊥ físico` disminuye, permanece constante o aumenta?**

Decrece: 0.1953 → 0.1950 → 0.1693 → 0.1623 → 0.1606. La tasa de descenso se desacelera
rápidamente: de −13.1% (7200→14400) a −4.2% (14400→21600) a −1.0% (21600→28800). El
último par cambia solo 0.0017 mientras ell cae un 13.4%; bajo el modelo potencia con α=0.22,
se esperaría un cambio de 3.1% — se observa sólo 1.0%.

**P3. ¿Los cinco puntos discriminan entre d⊥ → c>0 y d⊥ ∝ ell^α?**

No de forma concluyente. El patrón no es uniforme: plano en 3600-7200 (~0.195), salto brusco
a 14400 (−13%), luego casi plano en 21600-28800 (~0.161). Este comportamiento sigmoidal es
inconsistente con un modelo potencia puro en todo el rango; a su vez, la tendencia global es
decreciente, lo que no descarta que la asíntota sea c=0 (decaimiento lento). Los residuos del
modelo potencia (máx 0.009) son menores que los del modelo plateau c=0.1615 para los puntos
1-2 (residuos ~0.034), pero el último par favorece el plateau.

### Ajuste log-log descriptivo

```
EXPLORATORY_EFFECTIVE_EXPONENT_ONLY
  ln(d⊥) = 0.219 × ln(ell) − 0.927
  → d⊥ ≈ 0.396 × ell^0.219
  EXPLORATORY_EFFECTIVE_EXPONENT = 0.22
```

ADVERTENCIA OBLIGATORIA: el modelo potencia se impone, no se identifica. Los exponentes
efectivos por pares consecutivos son:

| tramo           | α_par  |
|:----------------|-------:|
| 3600 → 7200     |  0.004 |
| 7200 → 14400    |  0.411 |
| 14400 → 21600   |  0.207 |
| 21600 → 28800   |  0.073 |

Rango 0.004–0.411: demasiado inestable para interpretar α≈0.22 como ley física. El exponente
global es un promedio descriptivo del rango completo, no un parámetro físico identificado.

### Veredictos

```
LONGEST_TAIL_O_ELL_ADHERENCE
  = FAILED_IN_EXPLORATORY_3_DENSITY_SWEEP           [sin cambio; confirmado por 5 puntos]

LONGEST_TAIL_PHYSICAL_CONVERGENCE =
  EVIDENCE_FAVOURS_SLOW_DECAY_BUT_NOT_IDENTIFIED

LONGEST_TAIL_SCALING_EXPONENT = UNRESOLVED

EXPLORATORY_EFFECTIVE_EXPONENT = 0.22
  (EXPLORATORY_EFFECTIVE_EXPONENT_ONLY — modelo potencia impuesto, no identificado)

SEARCH_COMPLETENESS_AT_21600_28800 = UNVERIFIED
```

### Qué sigue sin estar identificado

- Si la asíntota d⊥(ell→0) es cero (decaimiento lento) o un plateau positivo c≈0.16.
- El mecanismo del salto no-uniforme entre 7200 y 14400 (el mayor descenso de la serie).
- La fracción de búsquedas completas a 21600/28800 y su efecto sobre los valores de cola.
- No se ha diseñado todavía un nuevo selector de horizonte, una banda de adherencia,
  ni la extensión a Schwarzschild 3+1D.
