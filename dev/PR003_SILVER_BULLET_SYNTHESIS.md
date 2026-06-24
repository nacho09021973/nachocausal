# PR-003 — "silver bullet" synthesis: cross-check of three external research opinions (dev, NOT a result)

Sandbox note. The user supplied three independently-generated research opinions
(`biblioteca/Investigacion_Opinion_{1,2,3}.md`) on extending the horizon reconstruction past
`BARE_RELOCALISATION`. **This is analysis only — nothing measured, nothing frozen, no claim.**
Its value is the honest cross-check between what the three docs recommend and what THIS project
has already established/refuted (which the docs only know partially). For adjudication, not a plan.

## What the three docs are

Three structured dictámenes (exec summary → state of art → taxonomy → comparison table → top-3
routes → minimal falsification experiments → possible negative result → recommendation). Almost
certainly three separate model runs. The signal is in their **convergence**.

## Where all three AGREE (strong convergent signal)

1. The greedy / iterative-reseed failure does NOT show the order lacks the information — it shows
   a *class* of method fails: rigid 1D trajectories optimised locally/greedily on short-range
   order. Matches our `BARE_RELOCALISATION` + S3 non-convergence exactly.
2. The horizon object is a **diffuse band / scalar field of thickness O(ℓ), not a curve.** This is
   literally the learning-branch the roadmap already anticipated
   (`hoja_de_ruta_24_jun_2026.md:67-70`: curve → "banda/antichain order-only").
3. **Honest coverage** (abstain/degenerate = miss) is the only valid metric — exactly what S3
   implemented (`dev/measure_iterative_reseed_v1.py`).
4. Reject GNN/ML as leakage-prone and epistemically empty — coherent with the leakage gate.

## Honest cross-check vs what we ALREADY know (the filter the docs cannot apply)

| Route the docs push | Our actual state |
|---|---|
| Collective expansion Θ sign-change (top in all 3) | **Already tried (Fase #1-B); FAILED robustness.** S1: signal depends on the unreliable `relphi` direction split; S2: degrades with taller box AND density (`dev/PR003_EXPANSION_ROBUSTNESS_NOTES.md`). Their per-element-field variant still needs an order-only direction discriminator — the unsolved problem. |
| Horizon molecules (Dou–Sorkin / Sorkin–Yazdi 2018) — doc 3 rates success 5/5 | Committee 002 **dimension-killed** the molecule/area angle for 1+1D vacuum (SMI∝area is 3D/4D; codim-2 "area" is a point in 2D; the action is topological Gauss–Bonnet). And Dou–Sorkin **needs the horizon location a priori** to count crossing links — not a blind finder. As a *link-density-anomaly* localizer (not entropy) it is not obviously dead, but the area/entropy narrative does not transfer. |
| Causal d'Alembertian / BD curvature (all 3) | R=0 in 1+1D vacuum ⇒ B→□, **null curvature signal** (falsifier, comite_002 §5.5). The *directed-Laplacian / Fiedler-bottleneck* variant is a different claim (causal-flow chokepoint, not curvature) and might survive R=0 — but docs themselves flag severe finite-patch boundary artefacts; low interpretability. |
| Multi-hypothesis over fronts | S3 is already a multi-front re-localisation; honest coverage degraded 51→48→44% with density. |

**Bottom line:** much of the "silver bullet" re-recommends paths we already have evidence against
in THIS geometry. It is not a magic fix. But it (a) validates our methodology, and (b) leaves two
genuinely-new grounded ideas + one strategic reframe.

## What genuinely survives (the extract)

1. **Thickened-antichain persistent homology (TDA, H0) — UNTRIED, strongest new idea.** Order-only,
   relabel-invariant, MINK-falsifiable. Targets the connected band as a **persistent component**,
   not a curve (the curve→band pivot the roadmap left open). **Robust to the falsifier's objection**
   that `L_past` level-sets are not maximal: persistence over a thickness filtration does not need
   maximality. Falsifiable prediction (docs 2-3, Exp 3): in BH a long-persistence H0 bar exists with
   no MINK counterpart, and its component forms an extended band. Lit: Major–Rideout–Surya 2007;
   Cunningham–Surya 2018 (citations UNVERIFIED here — needs the literature verifier).
2. **K-beam multi-hypothesis as a FALSIFICATION of the peel-off (not a hoped-for fix).** Decides the
   one thing Fase #3 needs: is the `BARE_RELOCALISATION` peel-off **algorithmic** (greedy myopia,
   curable) or **physical** (marginally-unstable null orbit = our bound)? If the K-beam also peels →
   it **hardens** the bound; if not → reopens extension. Cheap, pipeline-compatible, decisive both
   ways (docs 1-3; doc 2 Exp 1).
3. **Strategic reframe for Fase #3: turn `BARE_RELOCALISATION` into a PROVEN no-go.** All three docs
   independently propose an **information-theoretic lower bound** (Le Cam / Fano / Cramér–Rao): a
   two-point test between the causal-order distributions of a Schwarzschild patch and a Minkowski
   patch, giving `Error(r̂ − r_S) ≳ C·ℓ` (doc 1) or `≳ C/√ρ` (doc 3). This elevates Fase #3 from
   "accept the empirical wall" to "**prove the wall is information-theoretically forced**" — a much
   stronger publishable contribution, and the best fit for where the project now sits.

## Caveats / honesty

- Nothing here is measured, frozen, validated, or audited. The docs' literature citations are not
  verified (some — e.g. doc 2's "Boguñá–Krioukov 2026 local d'Alembertian" — need checking).
- Risk of being talked into re-labelling a negative: the band reframe does NOT obviously rescue S3 —
  we measured the band *thickness in ℓ-units growing* (d⊥/ℓ 0.52→0.88), so "it's a band not a curve"
  is not a free pass. Any band claim must still pass honest coverage + density convergence.
- TDA introduces a thickness/filtration parameter; any freeze of it must declare a principled anchor
  BEFORE seeing scored data (leakage gate contract 5 / anti-reverse-engineering), exactly as the
  guardian flagged for `l_k` in comite_002.

## Disposition

This is a frontier decision with genuine tension (docs optimistic on molecules/expansion that our
own committee already wounded) → adjudicate via `/comite`, not solo. Questions put to the committee:
(Q1) a dev TDA-persistence H0 probe before consolidating, or straight to Fase #3? (Q2) a K-beam
peel-off falsification to harden the bound, and formalising the Le Cam/Fano bound as the Fase #3
result?
