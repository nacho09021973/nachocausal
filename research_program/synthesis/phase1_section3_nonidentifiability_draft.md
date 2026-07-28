# Fase 1 · Paso 1.2 — Draft §3: Proved non-identifiability

> **STATUS: MANUSCRIPT_SECTION_DRAFT / NOT_FROZEN / NO_NEW_SCIENCE /
> ANCHORS_TO_EXISTING_PROOFS / DOES_NOT_TOUCH_SEAL / DOES_NOT_DISCHARGE_ITEM_5.**
>
> Redacción de la sección matemática principal del paper de límites
> (`phase1_limits_paper_outline.md` §3). **No inventa teoremas:** resume y unifica
> pruebas ya ancladas en el repo. Toda afirmación `PROVED` lleva ancla `file` y
> etiqueta de programa.
>
> FECHA: 2026-07-28 · HEAD de referencia: `dce6171`
> Gobernanza: Fase 0 R3; N2=lema; N1=instanciación acotada; N3/N4 remarks; N5 fuera.

**Convenciones de este draft**

| Marca | Significado |
|---|---|
| `[PROVED]` | Teorema con prueba en el repo; aquí se reexpone |
| `[BACKGROUND]` | Hecho de literatura / libro; no se reclama como contribución |
| `[REMARK]` | Diseño o corolario; no contribución numerada |
| `EMPIRICAL_FAILURE_OF_CLASS_L` | **No se usa en §3** (reservado al ledger) |

---

## §3 Proved non-identifiability
<!-- manuscript body starts -->

This section records three statements of **non-identifiability** for geometric targets
under finite order-only observation. Each statement is of the form: either two
geometries with distinct target values induce **identical** laws on the observed
unlabeled poset, or their laws are so close that **no** measurable function of the
poset can separate them at a stated rate. In the program vocabulary of
`identifiability_taxonomy.md` §4.4 these are
`PROVED_NON_IDENTIFIABILITY` results. They do **not** depend on the success or
failure of any particular estimator constructed in this repository.

Throughout, a *completion* is a Lorentzian patch equipped with a Poisson sprinkling
of intensity \(\rho\) with respect to the volume measure. Conditioning on cardinality
\(N=n\) makes the \(n\) points i.i.d.\ from the normalized volume measure
(`[PROVED]` Lemma 0, `first_witness_pair_candidates.md` §1). The *order-only,
fixed-\(n\) channel* observes only the isomorphism class of the induced causal set.

### 3.1 Exact scale blindness at fixed cardinality
<!-- (T1) · former N2 → lemma -->

#### Theorem 3.1 (exact witness orbit for absolute scale)
`[PROVED]` · Label: `PROVED_NON_IDENTIFIABILITY`

**1+1 dimensions.** Let \(g_{r_s}\) be the 1+1 Schwarzschild metric with horizon
radius \(r_s>0\), let \(P\) be any finite-volume patch, and let
\(\Phi_s(t,r)=(st,sr)\) for \(s>0\). Write \(P_n(r_s;P)\) for the law of the
unlabeled \(n\)-element poset obtained by conditioning the sprinkling of
\((P,g_{r_s})\) on \(N=n\). Then, for every \(n\ge 0\) and every \(s>0\),

\[
\mathrm{TV}\bigl(P_n(r_s;P),\, P_n(s r_s;\Phi_s(P))\bigr)
\;=\; 0.
\]

In particular, for every (possibly randomized) order-only estimator \(\widehat r_s\)
and every \(s\neq 1\),

\[
\mathbb{P}_{r_s}\bigl(\widehat r_s = r_s\bigr)
+
\mathbb{P}_{s r_s}\bigl(\widehat r_s = s r_s\bigr)
\;\le\; 1,
\]

so no order-only procedure can recover absolute horizon radius on both ends of the
orbit with total error probability less than one. Since \(s\) is arbitrary, the entire
orbit \(\{r_s>0\}\) shares a single poset law at each fixed \(n\): **the observed finite
order carries no information about \(r_s\) in absolute units**.

*Proof sketch (full proof: `first_witness_pair_candidates.md` §2, Theorem A).*  
By direct computation, \(\Phi_s^* g_{s r_s}=s^2 g_{r_s}\). A constant conformal factor
preserves causal order. Volume forms in 1+1 dimensions scale by \(s^2\), which cancels
under normalization of the sampling measure. Conditioning on \(N=n\) (Lemma 0), the
\(n\) i.i.d.\ sample on the dilated geometry is the \(\Phi_s\)-image in law of the
sample on the original geometry, with identical induced relations. Unlabeled poset
laws therefore coincide, and total variation vanishes. The estimation consequence is
the two-point bound at \(\mathrm{TV}=0\) (`wp4_two_point_theorem.md`, Teorema 2). ∎

**3+1 dimensions (scoped).** `[PROVED]` in the scoped class of
`op12_tv_zero_3p1.md`, not as a general Hauptvermutung. Fix a temporal sector
\(\sigma\in\{+,-\}\) and a patch shape \(\lambda\). For masses \(M,M'\) in a
prescribed interval and \(a=M'/M\), the identification in dimensionless Kruskal
coordinates \(\phi_a(U,V,\omega)=(U,V,\omega)\) satisfies
\(g_{M',\lambda}=a^2 g_{M,\lambda}\) and, after volume normalization,

\[
\frac{\mu_{M',\lambda}}{\mu_{M',\lambda}(K)}
=
\phi_{a\#}
\Bigl(
\frac{\mu_{M,\lambda}}{\mu_{M,\lambda}(K)}
\Bigr).
\]

A positive conformal rescaling preserves causality. The general coupling lemma
(`op12_tv_zero_3p1.md` §2) then yields, for every \(n\),

\[
P^{\mathrm{fixed}\,n}_{M,\sigma,\lambda}
=
P^{\mathrm{fixed}\,n}_{M',\sigma,\lambda}.
\]

Thus absolute mass (and absolute \(r_h=2M\)) is non-identifiable in the fixed-\(n\)
order-only channel inside each fixed sector and shape. Dimensionless targets such as
\(r/(2M)-1\) are constant along the orbit and are not constrained by this equality.

#### What Theorem 3.1 does not say

1. **Relative location.** Targets expressed in units of the discreteness scale
   \(\ell=\rho^{-1/d}\), of the patch size, or of \(\sqrt{n}\), are invariant under
   the dilation orbit and are **untouched** (Remark A2, FWP §2).
2. **Order+number with known density.** If \(N\sim\mathrm{Poisson}(\rho V)\) is
   observed and \(\rho>0\) is known, the pair with \(s\neq 1\) is typically
   distinguishable through cardinality alone at precision \(\sim 1/\sqrt{n}\)
   (Remark A3, FWP §2; OP-1.2 §5 in 3+1). Scale is a *Number* observable in that
   channel.
3. **Novelty as physics.** `[BACKGROUND]` The statement formalizes the causal-set
   slogan that order alone does not fix scale (“Order + Number”; e.g.\ Dowker–Zalel,
   arXiv:1703.07556; Madsen, arXiv:2607.05840; Braun, arXiv:2507.01907,
   §§3.3–3.4). Continuum precursors include the conformal character of causal
   isomorphisms (Hawking–King–McCarthy 1976; Malament 1977) and dilatations among
   causal automorphisms of Minkowski space (Zeeman, via Bombelli 1987). The
   contribution here is the **exact finite-\(n\) TV statement** for the sprinkling
   channel, not a new continuum theorem.

### 3.2 The global event horizon is not a finite-patch functional
<!-- (T2) -->

#### Theorem 3.2 (teleological non-identifiability)
`[PROVED]` as a definitional theorem · Label: `PROVED_NON_IDENTIFIABILITY`

Let \(T_{\mathrm{EH}}(M,g)\) denote the event horizon of a time-oriented Lorentzian
manifold \((M,g)\) (the boundary of the causal past of future null infinity, in the
standard asymptotically flat setting, or the appropriate analogue in the completion
under study). Let \(P\subset M\) be a region of finite volume, and let
\(\mathcal{D}(P)\) be any \(\sigma\)-algebra of observables determined by the
restriction of the geometry and of a sprinkling to \(P\) alone (in particular: the
unlabeled causal set of the sprinkling in \(P\)).

**Claim.** \(T_{\mathrm{EH}}\) is not \(\mathcal{D}(P)\)-measurable in general: there
exist pairs of completions that induce identical data on \(P\) and distinct global
event horizons.

*Reason.* By definition, the event horizon depends on the causal structure of the
*entire* future development, not on a single compact region. One may modify the
metric (or the conformal factor, or the topology of the continuation) outside \(P\)
so that the past of future null infinity changes while the geometry on \(P\) is held
fixed; the induced sprinkling law on \(P\) is then unchanged, while
\(T_{\mathrm{EH}}\) need not be. Hence no function of finite-patch order-only data
can equal \(T_{\mathrm{EH}}\) on all admissible completions.
(`[BACKGROUND]` claim grammar: `docs/claim_grammar.md` §3; program synthesis on
teleology.)

#### What Theorem 3.2 does not say

1. It does **not** prohibit *quasi-local* proxies (trapped surfaces, expansion of
   null congruences, singularity-truncation cuts inside a frozen singular family).
   Those targets require their own contracts (`claim_grammar.md` §3).
2. It does **not** assert that black-hole physics is invisible to causal sets. It
   asserts only that the **global event horizon**, as a set defined by the full
   spacetime, is the wrong target for a finite-patch experiment.
3. Empirical failure of particular quasi-local constructions (ledger C1–C6) is
   **not** invoked and is **not** a substitute for this argument.

### 3.3 Localization floor in a regular one-parameter family (1+1)
<!-- (T3) · former N1 → bounded instantiation -->

The dilation orbit of Theorem 3.1 kills absolute scale. Relative geometric
parameters can still vary inside a fixed coordinate chart. Two natural attempts to
encode “horizon location in the box” fail regularity or information content; a third
family is regular and yields a genuine rate lower bound. We record the diagnosis and
the floor. Full proofs:
`wp4_fisher_localization_floor.md` (annex).

#### 3.3.1 Two sterile or non-regular designs `[REMARK]`

**Proposition 3.3 (Kruskal box degeneracy).** `[PROVED]`  
On a *fixed* Kruskal coordinate box, the normalized volume measure of 1+1
Schwarzschild is independent of mass: with \(x=r/(2M)\), the relation
\(UV=(1-x)e^{x}\) is mass-independent and the conformal factor contributes only a
global \(16M^2\), which cancels upon normalization. Hence the copula, the poset law
at every \(n\), and the Fisher information in the mass parameter are **identically
trivial** (\(I\equiv 0\)).  
*Reading.* Fixing a Kruskal box pins the horizon at \(U=0\) for every mass; the
construction is Theorem 3.1 in disguise (annex Prop.\ 1).

**Proposition 3.4 (fixed EF coordinate box: non-regularity).** `[PROVED]` (sketch in annex)  
On a fixed Eddington–Finkelstein coordinate rectangle, the volume measure is Lebesgue
for every mass, but the support of the law in global null coordinates moves with the
parameter at nonzero speed. Hellinger distance is first order in the shift: quadratic
mean differentiability fails and a finite Fisher information is not defined. A weaker
total-variation bound still yields an order-\(1/n\) two-point floor at the point
level; whether the poset channel attains it is open (annex Props.\ 2–3).

#### 3.3.2 The diamond family with fixed EF corners

**Construction.** Fix \(0<r_q<\tau_0\le\tau_1<r_p\) and \(v_p<v_q\). For each
\(\tau\in[\tau_0,\tau_1]\) let
\[
D_\tau
:=
J^+_\tau(p)\cap J^-_\tau(q),
\qquad
p=(v_p,r_p),\; q=(v_q,r_q)
\]
in the ingoing EF chart of 1+1 Schwarzschild of horizon radius \(\tau\). In global
null coordinates adapted to \(g_\tau\), \(D_\tau\) is a coordinate box straddling the
horizon \(\tilde U=0\), with singularity avoided (\(r\ge r_q>0\)).

**Lemma 3.5 (regularity).** `[PROVED]`  
The copula density \(c_\tau\) of the normalized sampling measure on \(D_\tau\) is
jointly continuous, \(C^1\) in \(\tau\), and bounded above and below by positive
constants on the compact parameter interval, with uniformly bounded score.  
(Annex Lemma R.)

**Proposition 3.6 (QMD and finite Fisher).** `[PROVED]`  
The Fisher information \(I(\tau)=\int (\partial_\tau\log c_\tau)^2\,c_\tau\) is finite
and continuous on \([\tau_0,\tau_1]\); set \(\bar I:=\sup I(\tau)<\infty\). The family
is differentiable in quadratic mean, and

\[
H^2(c_\tau,c_{\tau+\delta})
\;\le\;
\frac{\delta^2}{4}\,\bar I.
\]

(Annex Prop.\ 4; Hellinger convention \(H^2=\int(\sqrt{p}-\sqrt{q})^2\in[0,2]\).)

**Proposition 3.7 (no exact re-identification).** `[PROVED]`  
\(c_\tau\neq c_{\tau'}\) whenever \(\tau\neq\tau'\) in \([\tau_0,\tau_1]\). In
particular the exact \(\mathrm{TV}=0\) branch for *relative* location never occurs on
this family.  
(Annex Prop.\ 5; Ricci pinning and \(r\)-preservation contradiction, with symbolic
checks in `wp4_fisher_localization_floor_symbolic_checks.py`.)

#### Theorem 3.8 (order-only two-point localization floor)
`[PROVED]` · Label: `PROVED_NON_IDENTIFIABILITY` (rate)

Let \(Q^n_\tau\) be the law of the unlabeled \(n\)-point poset from \(D_\tau\)
conditioned on \(N=n\). For every \(n\), every \(\tau,\tau+\delta\in[\tau_0,\tau_1]\),
and every (possibly randomized) order-only estimator \(\widehat\tau=f(C_n)\):

1. **Total variation bound.**
   \[
   \mathrm{TV}\bigl(Q^n_\tau,\,Q^n_{\tau+\delta}\bigr)
   \;\le\;
   \frac{|\delta|}{2}\,\sqrt{n\,\bar I}.
   \]
2. **Estimation-to-testing.**
   \[
   \mathbb{P}_\tau\bigl(|\widehat\tau-\tau|\ge|\delta|/2\bigr)
   +
   \mathbb{P}_{\tau+\delta}\bigl(|\widehat\tau-(\tau+\delta)|\ge|\delta|/2\bigr)
   \;\ge\;
   1-\frac{|\delta|}{2}\sqrt{n\,\bar I}.
   \]
3. **Floor.** No order-only procedure localizes \(\tau\) to precision \(|\delta|/2\)
   with confidence \(1-\varepsilon\) at both endpoints whenever
   \[
   |\delta|
   \;<\;
   \frac{2(1-2\varepsilon)}{\sqrt{n\,\bar I}}.
   \]
   Thus the minimax localization radius is of order \(1/\sqrt{n\bar I}\) at fixed \(n\).

*Proof sketch (annex §5).*  
Prop.\ 3.6 bounds Hellinger at the copula level. Hellinger tensorizes over \(n\)
i.i.d.\ samples. The diamond is a null box, so the unlabeled poset is a function of
the copula sample (FWP Lemma 1); data processing and \(\mathrm{TV}\le H\) yield (1).
The nearest-endpoint test reduction yields (2)–(3)
(`wp4_two_point_theorem.md`). ∎

#### What Theorem 3.8 does and does not claim

| Claims | Does **not** claim |
|---|---|
| A lower bound on risk for **all** order-only estimators (randomized included) | That the bound is **tight** for posets (it is inherited by data processing from the point process and may be loose) |
| Rate exponent \(n^{-1/2}\) on this named regular family | That \(\bar I\) is evaluated in closed form for reference corners (finiteness is proved; numerical \(\kappa\) is marked NUMERICAL elsewhere) |
| Technique: QMD + Hellinger + two-point | Novelty of Le Cam / Hellinger machinery `[BACKGROUND]` (textbook) |
| | Any result in 3+1 dimensions |
| | That \(\tau\) is “horizon information” as a distinct physical invariant |

**Physics caveat (mandatory).** In 1+1 Schwarzschild the scalar curvature is
\(R_\tau=-2\tau/r^3\). The parameter \(\tau\) is simultaneously the horizon radius and
the only curvature amplitude of the family. There is no threshold structure that
activates because the diamond crosses \(r=\tau\). Discriminating \(\tau\) is
discrimination of a continuous geometric parameter of the patch—not a proof that an
event horizon has been localized as a codimension-one object. Naming the theorem a
“horizon detector bound” is **forbidden** in the manuscript.

#### Intrinsic units `[REMARK]` (former N4, deflated)

Under simultaneous dilation of corners and parameter, the combination
\(\kappa(\tau):=V(\tau)\,I(\tau)\) is exactly dilation-invariant (annex §5a): it depends
on the dimensionless shape of the diamond, not on absolute size. With
\(n=\rho V\) and \(\ell=\rho^{-1/2}\),

\[
\frac{\delta_n}{\ell}
\;\sim\;
\frac{1}{\sqrt{\bar\kappa}},
\qquad
\bar\kappa
:=
V\cdot\bar I.
\]

`[BACKGROUND]` Dimensionally, Fisher information for a length parameter scales as
\(\mathrm{length}^{-2}\) and area as \(\mathrm{length}^{2}\), so \(V\cdot I\) is
dimensionless. The annex proves the invariance on this family; we do **not** present
\(\kappa\) as an independent novelty theorem.

### 3.4 Summary of §3

| Result | Target | Channel | Guarantee | Label |
|---|---|---|---|---|
| Thm 3.1 | Absolute \(r_s\) or \(M\) | order-only, \(N=n\) | \(\mathrm{TV}=0\) on dilation orbit (1+1 and scoped 3+1) | `PROVED_NON_IDENTIFIABILITY` |
| Thm 3.2 | Global event horizon | any finite-patch data | not a functional of the patch | `PROVED_NON_IDENTIFIABILITY` |
| Thm 3.8 | Parameter \(\tau\) of the EF diamond family | order-only, \(N=n\) | floor \(\sim 1/\sqrt{n\bar I}\) | `PROVED_NON_IDENTIFIABILITY` (rate) |
| Prop 3.3–3.4 | design of families | — | Kruskal sterile; fixed EF box non-regular | `[REMARK]` |

None of these results is an `EMPIRICAL_FAILURE_OF_CLASS_L` statement. Failures of
named region-locators appear in §5 of the outline (ledger), not here.

<!-- manuscript body ends -->

---

## Repo anchors (auditor table)

| Statement | Primary anchor | Supporting |
|---|---|---|
| Lemma 0 (i.i.d.\ at fixed \(n\)) | `first_witness_pair_candidates.md` §1 | — |
| Thm 3.1 1+1 | FWP §2 Theorem A | Lemma 2 dilation |
| Thm 3.1 3+1 | `op12_tv_zero_3p1.md` §2–§3 | — |
| Thm 3.2 | `docs/claim_grammar.md` §3 | geometric_indeterminacy teleology |
| Prop 3.3 Kruskal | `wp4_fisher_localization_floor.md` Prop 1 | — |
| Prop 3.4 fixed EF box | annex Props 2–3 | — |
| Lemma 3.5–Prop 3.7, Thm 3.8 | annex §4–§5 | symbolic checks script |
| \(\kappa\) dilation | annex §5a | — |
| Two-point / TV–H | `wp4_two_point_theorem.md` | — |

## Open gaps intentionally left open in this draft

1. Pointwise \(I(\tau)>0\) at every single \(\tau\) (annex: only no vanishing on a subinterval is proved). **Not needed** for Thm 3.8.
2. Numerical value of \(\bar I\) / \(\bar\kappa\) for reference corners — NUMERICAL elsewhere; do not promote to `PROVED` here.
3. Ordering-fraction Chebyshev separation (outline antiguo §6.1) — **omitted** until comité 045 conditions C3–C4 close.
4. Independent literature check for “first order-only geometric floor” wording (ítem 5) — if used, hedge or complete Paso D.

## Checklist paso 1.2

```text
[x] (T1) enunciado + prueba sketch + qué no dice + background lema
[x] (T2) enunciado teleológico + qué no dice
[x] (T3) familia regular + floor + física del parámetro τ
[x] N3/N4 como remarks dentro de §3
[x] N5 ausente como contribución
[x] Ningún claim de ledger como no-go
[x] Anclas file por teorema
[ ] Revisión PI / red-team de wording
[ ] Integrar en manuscript completo (paso 1.3+)
```

## Siguiente paso (1.3)

Redactar §1 (claim grammar + abandoned north) y §2 (setup), reutilizando el abstract
skeleton de `phase1_limits_paper_outline.md` §2, y alinear numeración de teoremas
con el manuscript unificado.
