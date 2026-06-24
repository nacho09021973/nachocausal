# PR-003 Fase #1 — iterative order-only re-seeding (dev measurement, NOT a result)

Sandbox notes for `docs/hoja_de_ruta_24_jun_2026.md` Fase #1, авал `docs/comite/comite_decision_001_*`.
Produced by `dev/measure_iterative_reseed.py`. **Exploration only — nothing frozen, nothing
validated, not audited.** Scored with the hidden coordinate `r` (reveal ONLY to score; construction
is order-only). One concrete v0 instantiation of EGS's "piecewise discrete horizon" (arXiv:2605.06813
md:443, left to future work), made BLIND.

## Construction (order-only, blind)

- `O(i) = |future(i)|` = column sum of `C` (the SEALED v2 observable).
- `L_past(e)` = longest chain ending at `e` = an order-only discrete time. Its level sets
  `{e : L_past==d}` are **genuine antichains** (`a≺b ⇒ L_past(b)>L_past(a)`), i.e. the order-only
  "future antichains" to re-seed on.
- On each front `F_d` (size ≥ NMIN=8): re-run the sealed localiser — `two_means_split(O[F_d])` +
  the frozen `tau(n)` abstain gate. A non-abstaining front gives interior (`O<thr`) / exterior
  (`O≥thr`) **witness sets taken at the extremal O-value** (a function of the O-multiset → no
  label-dependent tie-break). The ordered union of those points over fronts = the piecewise locus.
- `r` revealed only to score: per front, midpoint `r = ½(r_in+r_ex)`, `d_perp = |mid−R_S|`.

## Result (2026-06-24, 6 seeds EXPLORE_POOL[:6], t_edge=6)

| intensity |   ell  | fronts/seed (med[min,max]) | abstain | d_perp/ell | covers R_S | connected | r-scatter std/IQR | Guard-v | FLAT CTRL (MINK) |
|----------:|-------:|---------------------------:|--------:|-----------:|-----------:|----------:|------------------:|:-------:|:-----------------|
|     3600  | 0.0447 | 96 [91,104]                |   30%   |   0.52     |    74%     |    90%    | 0.0974 / 0.0417   |  6/6    | PASS (BH 96 vs MINK 4; MINK d_perp 5.83ell) |
|     7200  | 0.0316 | 146 [141,152]              |   26%   |   0.63     |    65%     |    95%    | 0.0705 / 0.0309   |  6/6    | PASS (BH 146 vs MINK 4; MINK d_perp 7.98ell) |

`theta_stab` = 0.089 (3600) / 0.063 (7200).

## Reading (precise — what it does and does NOT show)

**Meets Fase #1's stated criteria (a)(b)(c), at a preliminary 2-density level:**
- **(a) Coverage ≫ the seed head.** ~96→146 localising fronts (vs the ~3-rung adherent head of
  `BARE_RELOCALISATION`) sampling the horizon line across the patch's t*; the count **grows with
  density**.
- **(b) Each piece O(ell).** Per-front `d_perp ≈ 0.5–0.6 ell` at both densities — physical
  `d_perp ≈ 0.023 → 0.020`, roughly constant/shrinking as `ell` halves. The single tracer drifted
  (tail 4–8 ell); this piecewise locus does **not**.
- **(c) Connected, not degrading.** Adjacent-front causal linkage 90%→95% (**improves**); robust
  r-scatter IQR 0.042→0.031 (**shrinks**, below `theta_stab`); localising fronts and connectivity
  both rise with density.
- **Guards pass:** relabel Guard-v invariant **6/6** at both densities (leakage contract 3);
  **MINK same-cloud flat control PASSES** — without a horizon the localiser builds only ~4 stray
  fronts at `d_perp` 6–8 ell, so the locus is **horizon-specific**.

**Caveats (honest):**
- `covers` (the bracket actually straddles R_S) is **74%→65%** — roughly a third of fronts localise
  a boundary offset from R_S; these outliers inflate the std (0.097→0.071, slightly **above**
  `theta_stab`) even though the robust IQR is well below it. The locus has a tight adherent **core**
  plus a noisy tail.
- **Two densities only.** The trend (fronts↑, connectivity↑, scatter↓) is encouraging but is **not**
  a convergence proof; the 14400 point is not yet run here.
- **"Connected" is a weak notion** — any causal link between adjacent-front witness sets, not a
  single through-chain along R_S.
- **Per-front localisation REUSES the sealed v2 localiser.** The advance over prereg-002 is the
  **connected extended ordered subset** (the geometric element-set output PR-003 wanted), not a new
  localisation principle. It is `prereg-002` localisation applied per order-only time-slice and
  threaded into a curve.
- **dev / v0 / scored with hidden r.** NOT frozen, NOT validated, NOT audited. Before any
  commitment: harden (3rd density for convergence; address the `covers`/outlier tail), then
  `/comite` + `/auditor`, per `docs/pr003_leakage_gate.md`.

**Open uncertainty (one line, no plan):** whether the adherent core survives hardening (3rd
density + a principled order-only handling of the non-covering / abstaining fronts) is the next
thing this v0 leaves open.
