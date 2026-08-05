# Bibliography claims dossier

Not a decorative bibliography. Every row exists to answer one question: **what does the
causal-set literature actually license us to claim about recovering Schwarzschild horizon
structure from order alone**, and where does that license run out. Per the founding rule
(`CLAUDE.md`): every claim below carries verifiable backing (file:line into
`biblioteca/derived-md/`, an arXiv id actually fetched this session, or a citation actually
read) or is marked `[UNVERIFIED]`. Nothing here is reconstructed from training-data memory of
"what the theorem probably says."

`biblioteca/` is git-ignored local reference material (see `CLAUDE.md`); this dossier is the
committed, auditable index of what has actually been read out of it (plus a few papers fetched
live via alphaXiv that are not yet locally archived — flagged per entry).

## Schema

Each entry:
- **Enunciado exacto** — the claim, close to the source's own wording/notation.
- **Fuente primaria** — authors, venue, year, arXiv id/DOI.
- **Hipótesis** — the conditions under which the claim holds.
- **Dimensión y clase de espacios** — dimension and class of spacetimes/posets it applies to.
- **Qué respalda** — what part of C1 / the recoverability claim it supports.
- **Qué NO demuestra** — the explicit limits of the claim.
- **Estado** — `SUPPORTED` / `PARTIAL` / `UNSUPPORTED` / `CONTRADICTED` / `UNSUPPORTED_GAP`
  (no literature found — a genuine hole, not a claim).

Line numbers into `biblioteca/derived-md/*.md` are marker-pdf/OCR conversion line numbers
(non-authoritative reading aid per the file headers), not original PDF pagination; `PDF_PAGE`
markers in each file give the underlying page for cross-reference.

---

## §1. What causal order reconstructs: the Hawking–King–McCarthy–Malament theorem

### 1.1 HKMM theorem (continuum): order + volume element ⟹ Lorentzian geometry, for d>2

**Enunciado exacto**: "Theorem 1 Hawking–King–McCarthy–Malament (HKMM): If a chronological
bijection f_b exists between two d-dimensional spacetimes which are both future and past
distinguishing, then these spacetimes are conformally isometric when d > 2." Slogan: "Causal
Structure + Volume Element = Lorentzian Geometry."

**Fuente primaria**: S.W. Hawking, A.R. King, P.J. McCarthy, "A new topology for curved
space-time which incorporates the causal, differential, and conformal structures," J. Math.
Phys. 17, 174–181 (1976), doi:10.1063/1.522874; D.B. Malament, "The class of continuous
timelike curves determines the topology of spacetime," J. Math. Phys. 18, 1399–1404 (1977),
doi:10.1063/1.523436. Both predate arXiv and are **not in `biblioteca/`**. Read this session via
the secondary restatement in S. Surya, "The causal set approach to quantum gravity," Living Rev.
Relativ. 22 (2019) 5, arXiv:1903.11544 —
`biblioteca/derived-md/The causal set approach to quantum gravity.md:340-352`. Independently
also cited (without restating hypotheses) in
`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:81`
and refs [16]-[17] at line 677-678 of the same file.

**Hipótesis**: (i) a *chronological* bijection f_b (a *causal* bijection suffices per Levichev
1987, cited at the same location — causal bijection ⇒ chronological bijection); (ii) both
spacetimes are **future and past distinguishing**: I±(p)=I±(q) ⇒ p=q; (iii) **d > 2**. The
original 1976 Hawking–King–McCarthy result assumed the stronger hypothesis of *strong
causality*; Malament (1977) is cited as generalizing it to the weaker distinguishing condition.

**Dimensión y clase de espacios donde aplica**: Lorentzian manifolds, **d > 2 only** — the
conformal-isometry conclusion is explicitly not claimed for d=2.

**Qué respalda**: The theoretical justification that the causal-order poset is, in principle,
the right object to carry geometric information (up to a local conformal factor) — the backbone
premise of the whole causal-set recoverability program C1 sits on top of.

**Qué NO demuestra**: (1) Does not recover the volume element/conformal factor from order alone
— see §1.2. (2) **States a d>2 hypothesis; the project works in 1+1D (d=2), which is outside the
theorem's own stated scope.** This is a load-bearing gap, not a technicality: nothing read this
session extends HKMM to d=2, and 2D Lorentzian geometry is famously conformally trivial/locally
flat for different structural reasons, so the theorem's absence in d=2 cannot be assumed to be
merely a proof-technique gap. (3) Requires smooth continuum bijections on both sides; says
nothing directly about discrete causal *sets* — the discrete analogue is a conjecture (Entry 2.5,
the Hauptvermutung), not a corollary.

**Estado**: `SUPPORTED` (as a statement of the reviewed continuum theorem) but `PARTIAL` as
backing for this project specifically, because of the d=2 exclusion. `[UNVERIFIED against
primary 1976/1977 sources — relied solely on Surya 2019's restatement this session]`.

### 1.2 What order alone does *not* determine: the missing conformal factor

**Enunciado exacto**: "Discreteness supplies the missing conformal factor, or the missing
(1/10)th of the metric, in d=4." CST slogan: "Order + Number ∼ Lorentzian Geometry."

**Fuente primaria**: Surya (2019), arXiv:1903.11544 —
`biblioteca/derived-md/The causal set approach to quantum gravity.md:462-481`; phrase "(9/10)th
of the metric" attributed to Finkelstein (1969) at line 351.

**Hipótesis**: HKMM hypotheses (§1.1) plus the causal-set-specific postulate that order-interval
cardinality ~ spacetime volume, itself only an ensemble-average statement (see §2.4).

**Dimensión y clase de espacios**: d>2 continuum for the rigorous half; any d for the CST
cardinality proposal.

**Qué respalda**: The precise reason order **alone** (no auxiliary volume/cardinality input) can
recover at most the conformal class of the metric, never a volume-dependent quantity. Any C1
observable that claims to recover something volume-dependent (e.g. a horizon *area*, as opposed
to a conformally-invariant causal boundary) needs an explicit cardinality/density input, not
order alone.

**Qué NO demuestra**: The n∼ρV correspondence holds "on the average" over a sprinkling ensemble
(line 563), not for a single finite realization (Poisson fluctuation δn=√n, line 596) — matters
directly for a benchmark that scores a *single* causal set instance, not an ensemble average.

**Estado**: `SUPPORTED` for the general claim; `PARTIAL` for single-instance applicability
(ensemble-average caveat).

### 1.3 Braun (2025): the probabilistic discrete analogue of §1.1 — and it carries the same d≥3 exclusion

**Enunciado exacto**: "Theorem 1.4 (Probabilistic spacetime reconstruction, unweighted case).
Let (M,g) and (M′,g′) be two causally continuous and future chronocomplete spacetimes of finite
volume λ>0. Then the two spacetimes (M,g) and (M′,g′) are smoothly isometric if and only if for
every k ∈ N, the distributions of the random adjacency matrices C_k(X_1,…,X_k) and
C′_k(X′_1,…,X′_k) under P coincide." The author's own framing: "In a probabilistic way, our
result makes a key paradigm of causal set theory rigorous: spacetime can be recovered by only
knowing 'order' and 'number' of its points. It confirms a weak version of Bombelli's conjecture."

**Fuente primaria**: M. Braun, "Spacetime reconstruction by order and number," arXiv:2507.01907v1
[gr-qc], 2 Jul 2025. Locally archived at
`biblioteca/emergencia/2507.01907v1_Braun_Spacetime_Reconstruction_Order_Number.pdf`. Read this
session via alphaXiv (pages 1–5, 7, 9, 11, 13, 15); no `derived-md` conversion exists yet, so
citations below are to PDF pages, not conversion lines.

**Hipótesis**: (i) both spacetimes causally continuous (= distinguishing + reflecting, Hawking–
Sachs) and future chronocomplete — global hyperbolicity implies both (Lemma 2.10); (ii) finite
volume λ>0, the *same* for both; (iii) **d ≥ 3**, stated verbatim on p.2: "we assume all
spacetimes have the same dimension d ∈ N no less than 3"; (iv) the laws coincide **for every
k ∈ N** simultaneously — the proof passes to ν_∞ by Kolmogorov extension (§3.3) and then to
generic sequences, so no single k suffices.

**Dimensión y clase de espacios**: **d ≥ 3 only.** The mechanism is inherited from §1.1: Braun's
proof routes through Theorem 2.13 (Malament) to get conformal isometry from chronological
isomorphy (§3.3), then upgrades to isometry by volume-preservation (§3.4). Malament's theorem is
exactly the d>2 input, so Braun's dimensional restriction is not an artefact of technique but the
same structural fact recorded in §1.1.

**Qué respalda**: The strongest existing evidence that the *information* is present in the
order+number channel. Two points bear directly on this project. First, the sampling model is
**ours**: p.4, "Given k ∈ N, we think of {X_1,…,X_k} as the random support of a PPP conditioned
on k elements" — that is fixed-cardinality conditioning, the channel used throughout `emergencia/`
and the pre-registration. Second, it settles identifiability-in-law affirmatively, which means
this project must **not** be framed as testing whether order+number determines geometry.

**Qué NO demuestra**: (1) **d ≥ 3; the 1+1D work in `emergencia/` is outside the theorem's stated
scope**, exactly as in §1.1 and for the same reason. Nothing read this session extends Braun to
d=2, and in d=2 the conformal group is infinite-dimensional, so the "9 of 10 degrees of freedom
from order" accounting Braun cites on p.3 does not transfer. (2) It is a statement about the
**full** adjacency matrix at **all** k. It licenses nothing about a scalar summary, a single k, or
a selected sub-configuration; in particular it does not bound, and is not in tension with, the
conditional-variance measurements of the σ(M) channel. (3) It is an injectivity/rigidity result:
**no estimator, no rate, no finite-n guarantee, no risk bound.** "If the laws coincide then the
spacetimes are isometric" says nothing about how much of the geometry a finite sample recovers.
(4) arXiv v1 preprint, not peer-reviewed as of this reading. `[UNVERIFIED as to internal
correctness — read for statement and hypotheses, not audited line by line]`.

**Estado**: `SUPPORTED` as a statement of the reviewed theorem; `PARTIAL` as backing for this
project, for two independent reasons — the d=2 exclusion and the full-data hypothesis.

---

## §2. Manifold-likeness, sprinkling, and what is/isn't proven to be recoverable

Source throughout: S. Surya, "The causal set approach to quantum gravity," Living Rev. Relativ.
22 (2019) 5, arXiv:1903.11544 — `biblioteca/derived-md/The causal set approach to quantum
gravity.md` (3724 lines, read via targeted sections this session: 80-500, 690-950, 986-1250,
3420-3612).

### 2.3 Causal set axioms (poset definition)

**Enunciado exacto**: "A set C with an order relation ≺ is a causal set if it is 1. Acyclic:
x≺y and y≺x ⇒ x=y, ∀x,y∈C 2. Transitive: x≺y and y≺z ⇒ x≺z, ∀x,y,z∈C 3. Locally finite:
∀x,y∈C, |I[x,y]|<∞, where I[x,y] ≡ Fut(x)∩Past(y)."

**Fuente primaria**: Bombelli, Lee, Meyer, Sorkin (BLMS), "Space-time as a causal set," Phys.
Rev. Lett. 59:521 (1987), doi:10.1103/PhysRevLett.59.521. Read via Surya (2019),
`.../The causal set approach to quantum gravity.md:438-461`.

**Hipótesis**: None beyond the three axioms — this is definitional.

**Dimensión y clase de espacios**: Any locally finite poset, independent of embedding dimension.

**Qué respalda**: The literal source of C1's "strict partial order" requirement — acyclicity +
transitivity = strict partial order; local finiteness is the standard discreteness axiom that
should ground any admissibility condition on hidden completion elements.

**Qué NO demuestra**: Nothing about convexity, dimension, or manifold embeddability — a poset
satisfying only these three axioms need not be manifold-like (see §2.5, Kleitman-Rothschild
dominance).

**Estado**: `SUPPORTED`.

### 2.4 Faithful embedding / manifold-likeness (Poisson sprinkling, causal convexity)

**Enunciado exacto**: A causal set C approximates (M,g) at density ρ_c=V_c⁻¹ if there is a
faithful embedding Φ:C→M with Φ(C) Poisson-distributed at density ρ_c w.r.t. the spacetime
volume measure: P_v(n) = (ρ_c v)ⁿ/n! · exp(−ρ_c v).

**Fuente primaria**: Surya (2019) — `.../The causal set approach to quantum gravity.md:518-577`.
Random-sprinkling idea attributed to Myrheim (1978, unpublished CERN-TH-2538 preprint, line
409); random-lattice symmetry-restoration argument to Christ et al. (1982, line 543-544).

**Hipótesis**: (a) injective order-preserving embedding; (b) Poisson-uniform w.r.t. the
spacetime's own volume measure; (c) finite embedded regions are noted as "naturally" — not
proven necessarily — **causally convex** (unions of Alexandrov intervals, line 532-533): the
review *motivates and adopts* causal convexity as a convenient assumption for finite regions; it
does **not** prove it a necessary consequence of faithful embedding. It motivates C1's convexity
clause as an additional hypothesis; it does not mandate it. `[re-graded 2026-07-02 audit;
previously described as "the direct textual source for C1's convexity clause"]`

**Dimensión y clase de espacios**: General Lorentzian (M,g), any d; worked example in d=2 de
Sitter/Minkowski (line 588).

**Qué respalda**: The order-embedding-preserving-observed-subposet clause is directly supported
(this is literally Eq. 6 in the review). The convexity/no-inadmissible-hidden-elements clause is
only *motivated* — adopted as a convenient assumption, plus the discussion of spurious "voids"
from non-convex or badly-distributed completions (lines 596-608) — not derived as necessary.

**Qué NO demuestra**: A deterministic (non-random) lattice embedding is explicitly shown **not**
to work — "not regular in all frames" (line 536-538, boosted-lattice counterexample Fig. 5) —
warning against any C1-completion procedure relying on a single deterministic embedding instead
of treating faithfulness as a statistical/ensemble property.

**Estado**: `PARTIAL` — `SUPPORTED` for the faithful-embedding/order-preservation content;
the causal-convexity clause is motivated-as-hypothesis, not proven necessary
`[re-graded 2026-07-02 audit, previously `SUPPORTED`]`.

### 2.5 The Hauptvermutung: unproven in general, proven only piecemeal (O-Hauptvermutung)

**Enunciado exacto**: "The Hauptvermutung of CST: C can be faithfully embedded at density ρ_c
into two distinct spacetimes, (M,g) and (M′,g′), iff they are approximately isometric." Proven
fragment: "O-Hauptvermutung: If C faithfully embeds into (M,g) and (M′,g′) then (M,g) and
(M′,g′) have the same manifold invariant G associated with O." Status, verbatim: "there is no
full proof of the conjecture" (line 114); "there is as yet no complete proof" even of the
rigorous approximate-isometry notion (line 926).

**Fuente primaria**: Surya (2019) —
`.../The causal set approach to quantum gravity.md:706-718,918-943`. Rigorous
approximate-isometry attempts: Bombelli (2000), Noldus (2002, 2004), Bombelli & Noldus (2004),
Bombelli et al. (2012), Lorentzian Gromov–Hausdorff distance. An unpublished in-progress proof
attempt is cited ("Sorkin and Zwane, work in progress," line 928) — unverifiable, not counted as
support.

**Hipótesis**: A rigorous "approximate isometry" notion at fixed density, not yet fully defined
(Riemannian Gromov-Hausdorff doesn't directly generalize to indefinite signature). O-Hauptvermutung
is per-invariant (dimension, homology, distance functions, curvature, discrete Einstein-Hilbert
action — line 931-933), proven case by case, not as one theorem.

**Dimensión y clase de espacios**: General; the space Ω of *all* causal sets is combinatorially
dominated (~2^(n²/4)) by Kleitman–Rothschild (KR) posets, which are **not** manifold-like (lines
726-741, citing Kleitman & Rothschild 1975) — "most [causal sets] do not" admit a continuum
approximation at all (line 109).

**Qué respalda**: The single most important caveat for the whole program: geometric/topological
reconstruction from causal order+number is a **conjecture**, evidenced only piecemeal, with no
general proof. Directly supports treating recoverability as an empirical benchmark claim (this
repo's own framing, per `README.md`) rather than a theorem-backed guarantee.

**Qué NO demuestra**: Does not establish that any *given*, small, finite, possibly non-generic
causal set (exactly the regime this project's benchmark probes) is manifold-like or admits a
unique/near-unique admissible completion — by sheer combinatorial dominance most posets are
KR-like, not manifold-like.

**Estado**: `PARTIAL` (conjectural in general; only case-by-case sub-results proven).

### 2.5bis Müller (2025) and Madsen (2026): the finite-order Hauptvermutung is FALSE; order+volume+chains gives only ε-approximate isometry

**Enunciado exacto** (negative half, Müller via Madsen's restatement): "Müller showed this
version is false: he constructs examples of finite causal sets admitting causal-order-preserving
embeddings into geometrically distinct manifolds. The underlying issue is that without volume
information, finite causal data is too sparse to pin down the manifold; an adversary can rearrange
the embedded points in different spacetimes while preserving the order." (positive half, Madsen
Cor. 5.6): a causal set presented as a Poisson sprinkling at common density ρ of two globally
hyperbolic d-dimensional spacetimes admits, with probability ≥ 1−2(ρV_max)^(−K′_d), a smooth
diffeomorphism Φ : M°_1 → M°_2 with Φ*g_2 = g_1 + E and
‖E‖ = O(ρ^(−2/(5d)) λ^(−2/5) log^(3/2)(ρV_max)).

**Fuente primaria**: N. Madsen, "On the Uniqueness of Embeddings of Causal Sets,"
arXiv:2607.05840v1 [gr-qc], 7 Jul 2026 —
`biblioteca/emergencia/2607.05840v1_Madsen_Uniqueness_Embeddings_Causal_Sets.pdf`; read this
session via alphaXiv (pages 1–5, 10, 22–24, 29–31, 38–39). O. Müller, "On the Hauptvermutung of
causal set theory," arXiv:2503.01719 — present in `biblioteca/2503.01719v2.pdf` but **not read
this session**; the negative result above is cited here *through Madsen's §6.2 restatement*, not
from the primary source.

**Hipótesis** (Madsen): a "well-conditioned embedding" — (F1) exact order preservation; (F2)
scale-dependent uniform density, |f(C)∩D| − ρVol(D)| ≤ δ_D·ρVol(D) with
δ_D = K_d √(log(ρV_M)/(ρ Vol(D))); (F3) longest-chain/proper-time correspondence, via
Bollobás–Brightwell (1992) at rate 1/(2d). Plus global hyperbolicity, scale separation
ρλ^d ≥ c_*^(−2d)(log ρV_M)², and a conclusion restricted to the **deep interior** M°.

**Dimensión y clase de espacios**: stated for general d, but the error optimization in Thm 4.18
holds the covariance term subdominant **"for d > 2"**; the quoted rate is therefore not
established in d=2. Together with §1.1 and §1.3, this is the third independent result whose
stated scope excludes the dimension this project works in.

**Qué respalda**: (1) Müller's negative half is the strongest external support for this repo's
own framing that finite causal order *remembers* without *defining* — it is now a theorem that
order alone, finitely, is insufficient, not a suspicion. (2) Madsen's proof architecture is an
external template for the kind of argument `emergencia/` §13 attempts: a purely deterministic
geometric part plus **one** probabilistic concentration input, the author stating explicitly that
the argument "isolates the geometric content of the conjecture from its probabilistic content."
His (F2) tolerance has the same √(log/count) shape, and the same Chernoff-plus-union-bound
provenance, as the discrepancy lemma used there.

**Qué NO demuestra**: (1) **Not exact uniqueness** — ε-approximate isometry only, with ε→0 only
in the high-density limit ρ→∞. (2) Not a fixed-n finite-sample statement in this project's sense:
the guarantee is asymptotic in density, and Remark 5.4 states no almost-sure statement is
available for infinite-volume M at all (second Borel–Cantelli). (3) The deep-interior restriction
does **not** vanish: Remark 5.5(b) concedes that for a fixed manifold with boundary the excluded
layer of width c_*λ "does not shrink as ρ→∞" — so nothing is claimed near a boundary, which is
where horizon-adjacent questions live. (4) (F3) is **assumed, not derived**: footnote 1, p.4,
"its logical relationship to (F1)–(F2) is open … Whether (F2) implies (F3) is left to future
work." (5) arXiv v1, single author, 39 pages of heavy machinery (Karcher means, Lorentzian
Procrustes, degree argument), not peer-reviewed.

**Estado**: `PARTIAL`, and `[UNVERIFIED as to internal correctness — statement and hypotheses read,
argument not audited]`. Reading note, flagged rather than asserted: Corollary 3.7 (p.10) invokes
Lemma 4.1 from a later section, a forward dependency that a referee would be expected to query;
this is a structural observation about presentation, not a claim that the result is wrong.

### 2.5ter Bombelli tiene DOS formulaciones, y solo una es la que WP6 ataca

**Leído en primaria esta sesión** (2026-08-05): `biblioteca/Bombelli_1987_PhD.pdf`,
*Space-time as a causal set*, Syracuse University, diciembre 1987, 171 pp., con capa de
texto extraíble.

**Formulación A — tesis 1987, versión de EMBEBIDO.** §2.3 («Our main conjecture») y §2.9:

> «Our main conjecture (Hauptvermutung) is that the topology and differentiable structure
> are unique, and the metric is determined up to "small variations", i.e., if there exist
> two such faithful embeddings, the two manifolds are approximately isometric.»

y su forma precisa en §2.9:

> «Our "main conjecture" was that any pair of faithful embeddings, `f : P -> (M,g_ab)` and
> `f' : P -> (M',g'_ab)`, are related by a `P`-preserving diffeomorphism `phi : M -> M'`
> which is an approximate isometry of `g_ab` to `g'_ab`.»

Es un enunciado sobre **un causal set individual** y sus embebidos, con isometría
**aproximada**. La tesis aporta un argumento parcial (unicidad de la dimensión vía
`n`-pixies, cubrimiento por conjuntos de Alexandrov pequeños) y lo llama explícitamente
«a start in proving such a statement».

**Formulación B — la que cita Brightwell–Luczak, versión ESTADÍSTICA.** Atribuida a
L. Bombelli, *Statistical Lorentzian geometry and the closeness of Lorentzian manifolds*,
J. Math. Phys. **41** (2000) 6944–6958: si `U` y `V` son regiones de variedades
lorentzianas de volumen finito **sin difeomorfismo que preserve la medida** entre ellas,
entonces existe un poset finito `Q` con `t(Q;U) != t(Q;V)`, donde `t(Q;U)` es la
probabilidad de que una muestra iid uniforme de `|Q|` elementos de `U` induzca un poset
isomorfo a `Q`.

**La diferencia es material y hay que respetarla en cualquier texto.** A habla de embebidos
de un causal set concreto y de isometría **aproximada**; B habla de **leyes** —densidades
de patrones— y de difeomorfismo que preserva la medida, **exacto**. `research_program/
work_packages/wp6_d2_null_copula_dichotomy.md` ataca **B**, no A.

**Formulación B, ahora LEÍDA EN PRIMARIA** (2026-08-05). Preprint descargado a
`biblioteca/gr-qc0002053_Bombelli_Statistical_Lorentzian_Geometry_Closeness.pdf`
(arXiv:gr-qc/0002053v2, 11 jun 2000 = J. Math. Phys. **41** (2000) 6944–6958). La
conjetura está en §III, como la tercera de tres «reasonable conjectures» sobre `d_n(G,G')`:

> «(iii) For any two arbitrary (distinguishing, finite-volume) different geometries `G` and
> `G'` there is a finite `n` such that `d_n(G,G') > 0`, with `d_n(G,G') -> 1` as
> `n -> infinity`.»

donde «Lorentzian geometry» está definido en la introducción como **una clase de
equivalencia por difeomorfismo**, y el muestreo es «points randomly scattered in a
Lorentzian manifold, **with uniform density according to the volume element**» (abstract).
**La restatement de Brightwell–Luczak es fiel**: «diferentes» significa no relacionadas por
difeomorfismo que preserve la medida, y `t(Q;U)` es su `P_n(C|G)`.

**Y §VII plantea explícitamente el programa de WP6.** Bombelli escribe que las `P_n(C|G)`
son interesantes en sí mismas «as a **complete set of invariants** (together with the
volume) of finite volume, distinguishing Lorentzian geometries», y propone como dirección
abierta:

> «It would be worth while to study the type of information about the manifold that those
> different invariants contain; for example, how they encode dimensionality, **how they are
> affected by conformal transformations as opposed to changes in the conformal structure**,
> or how one can tell "localized" changes from "global" changes... Possible starting points
> ... e.g., comparing a two-dimensional and a three-dimensional manifold, or **modifying one
> by a conformal transformation**; and studying analytically **the effect of small
> variations `g -> g + delta g`**.»

Las tres cursivas son, respectivamente: el Teorema C de WP6 (qué transformaciones conformes
son exactamente invisibles), su instanciación en `d=2`, y el análisis de primer orden de R2
(`O(lambda^2)`). **Que el autor lo proponga como dirección abierta en 2000 no prueba que
siga abierta en 2026**; eso lo decide la auditoría de novedad. Pero fija el enunciado y la
paternidad de la pregunta.

**Estado de fuentes.** A: `SUPPORTED`, tesis 1987 leída en primaria. B: `SUPPORTED`,
preprint 2000 leído en primaria esta sesión. El hueco de fuente primaria de WP6 **queda
cerrado**.

### 2.5quater Aghili–Bombelli–Pilgrim (2018): 2D, pero el caso uniforme

`biblioteca/emergencia/1805.07312v1_Aghili_Bombelli_Pilgrim_Path_Length_2D_Causal_Sets.pdf`,
leído en abstract e introducción esta sesión. Distribución de longitudes de cadenas
maximales en causal sets 2-dimensionales, con relación de recursión para `n_k`, usada como
medida de embebibilidad y de dimensionalidad.

**Riesgo de novedad para WP6: bajo.** El objeto es «causal sets obtained from **uniformly
distributed points in Minkowski space**» — el caso plano/uniforme, igual que el modelo
`P_d(n)` de Winkler. No hay densidad no uniforme, ni cópula, ni identificabilidad de la
métrica. Refuerza el patrón ya observado: la literatura de causal sets 2D trabaja en el
caso plano, y la densidad **no uniforme** —de la que habla la conjetura B— no es su objeto.

### 2.5quinquies Artefacto propio del PI: revival del código Bombelli–Meyer 1987

**Artefacto**: J. I. Martín Gandul, *Bombelli & Meyer 1987 Causal Set Simulated Annealing
Revival*, 2026. DOI `10.5281/zenodo.20307735`;
`https://nacho09021973.github.io/bombelli/`; repositorio `nacho09021973/bombelli`; MIT.
Puerto fiel a Python 3.12 del programa Pascal de recocido simulado de la tesis de Bombelli
(1987), con David Meyer, que embebe causal sets pequeños en Minkowski. **Leído esta sesión
vía la página y el README, no ejecutado aquí.**

**Qué establece.** Preservando función de energía y conjunto de movimientos originales, sobre
el caso canónico de 12 elementos: el calendario original (`T_0 = 100`, `alpha = 0.9`) da
energía final media `22.735` sobre 100 semillas y **ningún embebido logrado**; un calendario
retocado (`T_0 = 180`, `alpha = 0.8`) da media `0.000` y **95/100** ejecuciones de energía
cero. Mismo algoritmo, misma energía, mismos movimientos. Cobertura `d ∈ {2,3,4}`,
`n = 6, 12`, hasta `n = 256` para estudios de dimensión; semillas deterministas.

**Dónde encaja, y dónde NO.** Encaja en la **formulación A** de §2.5ter —embebidos fieles de
un causal set individual, la Hauptvermutung de la tesis del 87—. **No toca la formulación
B** (leyes `P_n(C|G)`, JMP 2000), que es la que ataca
`research_program/work_packages/wp6_d2_null_copula_dichotomy.md`. No aporta nada a (E') ni
al parámetro `b`, y no debe citarse como si lo hiciera. En `d=2` además el problema de
embebido es trivial —todo poset de dimensión 2 embebe—, luego las celdas informativas de
ese trabajo son `d = 3, 4`.

**Para qué sí sirve aquí.** Da respaldo **empírico, reproducible y con DOI** a una tesis que
este repositorio sostiene por otras vías: que la ruta de **embebido** es frágil —dependiente
del optimizador hasta el punto de dar 0/100 frente a 95/100 con el mismo algoritmo—,
mientras que la ruta de **leyes** no requiere encontrar embebido alguno. Es un argumento
independiente a favor de trabajar con `P_n(C|G)` y no con embebidos.

**Lo que un auditor atacaría, y hay que anticiparlo.** La afirmación «con los parámetros
originales no se logra ningún embebido» es fuerte respecto de un programa histórico
publicado, y descansa por completo en la **fidelidad del puerto**. No es una afirmación de
que los resultados de 1987 fueran erróneos, sino sobre *ese calendario, en ese banco de
pruebas, tal como está portado*. Cualquier cita debe conservar esa distinción.

**VERIFICACIÓN INDEPENDIENTE, 2026-08-05.** Ejecutado en un segundo entorno desde clon
limpio (`github.com/nacho09021973/bombelli`, HEAD `d351c7b`, Python 3.12.3, numpy 1.26.4),
fuera de este repositorio y sin tocar nada suyo:

```text
python3 experiments.py schedule --data-dir <scratch>     (1m47s)
diff -u data/schedule_comparison.csv <scratch>/schedule_comparison.csv   -> vacio, exit 0
sha256 de ambos: 2bbe8632c2b583a58e655076e30d584e5e673e43c86e0457d6d7ff738ebadd72
python3 -m pytest -q                                     -> 24 passed
PYTHON=python3 make verify-data                          -> EXIT=0, salida VACIA
```

El objetivo `verify-data` del propio proyecto regenera **los cuatro** CSV en un directorio
temporal y hace `diff` contra los comprometidos; salida vacía y código 0 significa que
`dimension_atlas.csv`, `schedule_comparison.csv`, `warmup_comparison.csv` y
`correlate_summary.csv` se reproducen **todos** sin deriva.

**Las dos filas se reproducen byte a byte**, incluido el hash del CSV completo:
`bombelli_defaults` (`T_0=100`, `alpha=0.9`) → media `22.735`, `0/100`; `tuned`
(`T_0=180`, `alpha=0.8`) → media `0.000`, `95/100`.

**Alcance exacto de lo verificado**, leído del código (`experiments.py:145-230`), porque es
más estrecho de lo que sugiere la frase de portada:

- La dimensión es **`SCHEDULE_DIM = 3`**, no 2. Es un enunciado sobre embebido en Minkowski
  **tridimensional**.
- Semillas `1959..2058` (`SCHEDULE_BASE_SEED = 1959`, 100 consecutivas), fijas en el código.
- «Energía cero» es `< 1e-6` (`SCHEDULE_ZERO_EPS`); el docstring declara que energía 0
  significa embebido fiel.
- Entre las dos filas **solo** cambian `initial_temp` y `cooling_factor`: misma energía,
  mismos movimientos, mismo annealer.
- La media `0.000` de la fila `tuned` es **visualización redondeada a tres decimales**, no
  exactitud: 5 de 100 ejecuciones no alcanzaron el umbral.

**Lo que la verificación NO establece.** Que el puerto sea fiel al Pascal de 1987 — eso
exigiría el original, que no está aquí. Lo verificado es **reproducibilidad interna**: el
código publicado, ejecutado limpio en otra máquina, produce exactamente las cifras
publicadas. La distinción del párrafo anterior sobre 1987 sigue vigente en su totalidad.

**Estado**: `SUPPORTED_AS_ARTEFACT` (existe, DOI, público);
`REPRODUCED_INDEPENDENTLY_BYTE_EXACT` para los cuatro CSV (`make verify-data`, EXIT=0) y su
suite de 24 tests;
`[UNVERIFIED]` la fidelidad al Pascal original de 1987.

### 2.6 Myrheim–Meyer dimension estimator: what it estimates, and what it is *not*

**Enunciado exacto**: Ordering fraction r = 2R/[n(n−1)] (Eq. 14), R = number of related pairs.
"It was shown by Myrheim (1978) that r depends only on the dimension **when C faithfully embeds
into M^d**" (line 1010-1011). Meyer's estimator: ⟨R⟩/n² = f₀(d) = Γ(d+1)Γ(d/2)/[4Γ(3d/2)]
(Eq. 18), generalized to a k-chain-abundance family C_k (Eq. 19).

**Fuente primaria**: J. Myrheim, "Statistical geometry," CERN-TH-2538 (1978, unpublished); D.
Meyer, "The dimension of causal sets," PhD thesis, MIT (1988). Read via Surya (2019) —
`.../The causal set approach to quantum gravity.md:986-1156`.

**Hipótesis**: (1) Valid strictly for faithful embedding in **flat Minkowski M^d** (line 1011);
extended by Roy, Sinha & Surya (2013) to small causal diamonds in a Riemann normal neighborhood
of a curved spacetime under RT²≪1 (line 1118-1121), a curvature-corrected version (Eq. 20) —
still a small-region/flat-limit calculation at base. (2) **Statistical, ensemble-averaged**: "the
right dimension cannot be obtained from a single realization... but rather by averaging over the
ensemble" (line 1054-1056), fluctuations shrinking only as density grows (line 1066-1069). (3) An
integer result only shows statistical indistinguishability from a typical member of the reference
ensemble by *this one invariant* — Surya states explicitly it "does not of course imply that
C∼A_d or even that C is manifold-like" (line 1076-1077) — an instance of the weaker
O-Hauptvermutung (§2.5), not manifold-likeness itself.

**Dimensión y clase de espacios**: Minkowski M^d (base estimator, any d); RNN of curved
spacetimes under RT²≪1 (extension). A distinct family (mid-point scaling, Bombelli 1987/Reid
2003; Glaser & Surya 2013; Aghili et al. 2019 — line 1153-1156) exists but was not detailed
further this session.

**Qué respalda**: A concrete, order-only, ensemble-statistical procedure recovering an integer
spacetime dimension from causal order alone — evidence that *some* dimension-like quantity is
order-recoverable under stated conditions.

**Qué NO demuestra — critical gap for C1**: This is a *statistical/geometric embedding
dimension*, **not the same object as the combinatorial Dushnik–Miller order-dimension** used in
`comite_decision_012`'s `dim_DM ≤ 2` clause (minimum number of linear extensions realizing the
order). Grepped this file for "Dushnik," "order dimension," "realizer," "linear extension":
**zero occurrences**. This review gives no basis for treating Myrheim-Meyer dimension as a proxy
for, or equivalent to, order-dimension-2 — that equivalence, if used anywhere in the project, is
currently uncited. See §5.

**Estado**: `PARTIAL` — order-based dimension recovery supported under stated conditions;
explicitly silent on (does not support) any connection to combinatorial order-dimension.

### 2.7 Topology reconstruction: full manifold topology is impossible; spatial homology recoverable only under scale separation

**Enunciado exacto**: "It is clear that the full manifold topology cannot be reproduced in a
causal set since it requires arbitrarily small open sets" (line 1159-1160). Naive order-interval
topology "is roughly discrete or trivial" at the discreteness scale (line 1171-1173). Proven
fragment: "there exists a range of values of v such that N_v(A) is homological to Σ (up to the
discreteness scale) as long as there is a sufficient separation between the discreteness scale
ℓ_c ≡ V_c^{1/d} and K the scale of extrinsic curvature of Σ" (lines 1176, 1188-1192).

**Fuente primaria**: S. Major, D. Rideout, S. Surya, "On recovering continuum topology from a
causal set," J. Math. Phys. 48:032501 (2007), arXiv:gr-qc/0604124; "Stable homology as an
indicator of manifoldlikeness in causal set theory," Class. Quantum Grav. 26:175008 (2009),
arXiv:0902.0434. Read via Surya (2019) —
`.../The causal set approach to quantum gravity.md:1157-1220`.

**Hipótesis**: (1) inextendible antichain A ⊂ C as discrete analogue of a Cauchy hypersurface Σ;
(2) Σ **compact**; (3) nerve simplicial complex N_v(A) built from a collar-thickening parameter
v; (4) **scale separation** ℓ_c ≪ K required — without it the result is not shown. A parallel
attempt at full spacetime-region (not just spatial) homology is shown to generically **fail**:
Alexandrov intervals that intersect in the continuum can fail to intersect in the causal set
("straddling" intervals, lines 1196-1204), producing spurious cycles.

**Dimensión y clase de espacios**: (M,g) with a compact Cauchy hypersurface Σ; sprinklings
C∈C(M,ρ_c); no explicit dimension restriction.

**Qué respalda**: A genuine, citable, peer-reviewed proof that *some* topology (spatial-slice
homology) is order-recoverable, under stated conditions — directly relevant to whether the
project's completion program can recover horizon *topology*, not just local order.

**Qué NO demuestra**: Not full manifold topology (impossible in principle, line 1159-1160). The
spacetime-region (not spatial-slice) homology construction — closer to what horizon/trapping
structure needs — is explicitly "preliminary... there is much that remains to be understood"
(line 1211); a related chain-complex approach is "only... partially investigated" (line 1218).
The continuum theorem behind the naive order-interval topology (Penrose 1972, line 1170) does
**not** survive discretization without the extra antichain/collar machinery.

**Estado**: `PARTIAL` — `SUPPORTED` for spatial-slice homology under stated conditions;
`UNSUPPORTED`/open for full spacetime-region topology recovery, which is what a
future-inaccessibility/trapping-boundary style definition (per the strategic-refocus track) would
actually need.

---

## §3. Horizon definitions in causal-set theory

Four distinct lineages exist. None was designed to solve exactly this project's problem, but
each is a candidate physically-motivated alternative or cross-check for the order-only observable.

### 3.1 Lineage A — causal links crossing the horizon

**3.1.1 Link definition (building block).** "The interval delimited by x and y is empty... a
link is a pair x≺y such that no other causet element lies causally between them." Fuente: R.D.
Sorkin, "Light, Links and Causal Sets," DICE08 proceedings, J. Phys. Conf. Ser. 174:012018
(2009) — `biblioteca/derived-md/Sorkin_2008_Light_Links_and_Causal_Sets_Dice08.md:150-165`.
Hipótesis: causal set well-approximated by (a patch of) Minkowski M⁴; used there for a scalar
Green function, not for a horizon. Qué respalda: the exact order-theoretic definition all
link-counting horizon-entropy proposals build on. Qué NO demuestra: this source itself states no
horizon-entropy result and explicitly defers to Dou–Sorkin, "Black Hole Entropy as Causal Links"
(gr-qc/0302009, footnote at line 83) — **since acquired and read in full:
`biblioteca/0302009v1.pdf`, see §3.1.1bis and §5.5 item 7** `[estado de adquisición normalizado
2026-07-02]`. Estado: `SUPPORTED` (definition only).

**3.1.1bis Original claim and subsequent dimensional limitation (now locally archived and read
in full): expected link count proportional to horizon area, as argued analytically in the 2003
paper.** "We will identify a
certain kind of 'causal link'... and we will show that the black hole entropy can be equated to
the number of such links crossing the horizon H in proximity to the hypersurface Σ." General
4D formula: ⟨n⟩ = γ · [A(H∩Σ)/l_c²] · (1 + O(l_c/√A(H∩Σ))), where l_c = ρ_c^{-1/4} is the
fundamental causal-set length and γ is an O(1) constant; "almost all of these links will turn
out to be localized very near to H," so conditions deep inside the black hole are irrelevant to
the count. Fuente primaria: D. Dou, R.D. Sorkin, "Black Hole Entropy as Causal Links," Found.
Phys. 33, 279 (2003), arXiv:gr-qc/0302009 — now archived at `biblioteca/0302009v1.pdf` (no
derived-md yet; read directly via `pdftotext` this session, page numbers below are original
paper pagination). Hipótesis: causal set faithfully embedded (unit density, Poisson-sprinkled,
scale separation l_c≪ curvature scale) into a Lorentzian M; H a horizon, Σ a spacelike/null
hypersurface it crosses. Dimensión: general d (4D formula quoted; paper states cases studied
"include not only equilibrium black holes but ones far from equilibrium," abstract). Qué
respalda: this is the actual primary source for the link-counting horizon-entropy proposal —
Sorkin (2008, §3.1.1 above) only *cites* it; this is where the formula and its derivation live.
Directly relevant as a candidate order+cardinality (not order-alone) observable proportional to
horizon area, complementary to this project's own order-only recovery target. Qué NO demuestra:
the formula is asymptotic/leading-order ("for macroscopic black holes we can safely neglect the
second term," p. 13) — subleading l_c/√A corrections are not controlled; γ is not derived from
first principles, only constrained to be O(1); does not by itself locate H from the causet (H,
Σ are continuum inputs, same caveat as Lineage B/D). **And the general-d/4D claim did not survive
later scrutiny**: the original one-link DS molecule is IR-divergent (unbounded count) in d≥3
(§3.1.3, Barton et al. 2019 §1); Dou's own later review (arXiv:2307.04150, §5.5 item 10)
describes the original proposal as successful in 1+1D but failing beyond two dimensions [per its
arXiv abstract — full read still pending, §5.5 item 10]. Estado:
`PARTIAL` — `SUPPORTED` as the 2003 paper's own historical claim and for the 1+1D-truncation
cases it computed; `CONTRADICTED` as a currently-valid general result in d≥3 (IR divergence of
the original DS molecule, §3.1.3). The 4D formula is retained above as what the original paper
argued, not as an established result. `[re-graded 2026-07-02 audit; previous Estado `SUPPORTED`
was inconsistent with §3.1.3]` Cita: pp. 1-3 (intro, link/faithful-embedding definitions), p. 13
(general 4D formula, quoted above).

**3.1.2 Horizon-crossing link count scales linearly with horizon area (numerical replication and
extension to 1+1D Schwarzschild).** Replicates and numerically extends 3.1.1bis's analytic
result: "It is natural to imagine that the total number of links that cross the event horizon
is an obvious source of black hole entropy"; "A linear relation is observed between the entropy
and the horizon area" (flat 2D/3D/4D at large H; 1+1D Schwarzschild numerically).
Fuente: A. Dhital, "Black Hole Entropy in the Causal Set Approach," MS thesis, University of
Mississippi (2023) —
`biblioteca/derived-md/Dhital_2023_Black_Hole_Entropy_in_Causal_Set_Approach.md:59-66,510-512,877-905,2400-2412,2578-2591`.
Hipótesis: Poisson sprinkling; count link-matrix entries with minimal element outside/maximal
inside the horizon, referenced to a spacelike hypersurface. Dimensión: flat 2D (exact), flat
3D/4D (large H only — **linearity explicitly fails for H≪1**), and 1+1D Schwarzschild
(numerical). Qué respalda: a link-counting statistic **conditioned on an externally supplied
horizon partition** — its own construction classifies link endpoints as outside/inside the
horizon, i.e. it presupposes the ground-truth partition this project tries to recover. Useful as
an area-law/counting benchmark; **not an intrinsic order-only horizon locator**. The link
relation is order-theoretic only once the partition is given. `[re-graded 2026-07-02 audit;
previous wording "order-only observable for locating the horizon" was an overclaim]` Qué NO
demuestra: no closed-form curved-geometry result, only simulation; unpublished MS thesis (not
peer-reviewed); fails outside the tested regimes; does not locate the horizon from order alone
(see Qué respalda). Estado: `PARTIAL`.

**3.1.3 The original 1-link Dou–Sorkin molecule diverges in d≥3 (negative result).** "It was
realised by Dou [4] that the proposed molecules would not work in higher dimensions: in 3 or
more dimensions the number of DS horizon molecules is unbounded... even at non-zero discreteness
scale." Fuente: Barton, Counsell, Dowker, Gould, Jubb, Taylor, "Horizon Molecules in Causal Set
Theory," Phys. Rev. D 100, 126008 (2019), arXiv:1909.08620 §1 (fetched live via alphaXiv;
**since acquired: `biblioteca/1909.08620v1.pdf`, §5.5 item 8** `[normalizado 2026-07-02]`). Dimensión: d≥3 (fails there); original DS proposal only
tested in 1+1D truncations and a spherically-symmetric collapsing shell. Qué respalda: nothing
directly — a negative result flagging the naive link-count proposal's non-robustness outside
1+1D, which is why Lineage B (horizon molecules) exists. Qué NO demuestra: does not invalidate
the 1+1D case (the project's own regime). Estado: `CONTRADICTED` (for d≥3).

### 3.2 Lineage B — horizon molecules

**3.2.1 Horizon n-molecule definition + area-law expectation (proven under stated assumptions).**
"A horizon n-molecule is a subcauset {p⁻,p₊,₁,...,p₊,ₙ} such that p⁻≺p₊,ₖ ∀k; p⁻∈C⁻₋;
p₊,ₖ∈C⁻₊ ∀k; {p₊,₁,...,p₊,ₙ} are the only elements in both C⁻ and the future of p⁻." Claim:
lim_{ρ→∞} ρ^{(2-d)/d}⟨Hₙ⟩ = a_n^(d) ∫_J dV_J — expected molecule count converges to horizon
area up to a dimension-dependent O(1) constant. Fuente: Barton et al. (2019), arXiv:1909.08620
§2, §4, §6.1 (alphaXiv, fetched live; **since acquired: `biblioteca/1909.08620v1.pdf`, §5.5
item 8** `[normalizado 2026-07-02]`). Hipótesis: (M,g) globally
hyperbolic d-dim; H=∂I⁻(γ₀) a causal horizon (see 3.4.1); Σ Cauchy surface meeting H
transversally in codim-2 spacelike J; l≪τ≪L_G; requires an "exponentially suppressed" tail
assumption — **proven only for finite-volume-to-past-of-Σ cases, left as an explicit open
problem more generally (§4.2)**. Dimensión: general d, explicit constants for d=2,3,4;
statement is about the *expectation* over sprinklings, not a single causet. Qué respalda: a
rigorous (under stated hypotheses), dimension-general, geometry-covariant order observable whose
continuum-limit expectation is horizon area — a strong candidate benchmark/alternative to this
project's own order-only observable. Qué NO demuestra: (i) convergence for a **single** finite
causet is explicitly left "as an open problem" (§6.1) — the same single-instance gap as §1.2 and
§2.6; (ii) the exponential-suppression assumption is not proven in general, only conjectured;
(iii) H, Σ, J are continuum *inputs* to the construction, not causal-set-intrinsic outputs — the
construction does not itself identify the horizon from the causet. Estado: `PARTIAL`.

**3.2.2 Explicit disclaimer: molecules are not shown to be the entropy microstates.** "We will
not know whether our molecules are the 'right' ones... until we know the statistical mechanics
of black hole thermodynamics within the full theory of quantum causal sets." Fuente: same, §7 —
alphaXiv, fetched live. Qué respalda: honesty check — this lineage delivers a geometrically
well-defined area-scaling counting statistic, not (yet) a derivation of black-hole entropy from
microstates; does not derive the Bekenstein-Hawking 1/4 normalization. Estado: `UNSUPPORTED` (as
an entropy-microstate claim).

### 3.3 Lineage C — mutual information / entanglement entropy

**3.3.1 Naive causal-set entanglement entropy gives a volume law, not area/log law.**
S=Σ_λ λln|λ| from Wv=iλΔv; "the entanglement entropy grows linearly with the number of elements
in the smaller diamond, thus obeying a spacetime-volume law! ... not an area law, [and] not even
a spatial volume law." Fuente: R.D. Sorkin, Y.K. Yazdi, "Entanglement Entropy in Causal Set
Theory" —
`biblioteca/derived-md/Entanglement_Entropy_in_Causal_Set_Theory_Yazdi.md:21,81-96,121-131`.
Hipótesis: free massless scalar on a causal set approximating a 1+1D Minkowski causal diamond
nested in a larger one; Sorkin-Johnston vacuum. Dimensión: 1+1D flat only (this result). Qué
respalda: a cautionary negative data point against treating naive causal-set entanglement
entropy as horizon-locating. Qué NO demuestra: not a horizon computation at all — an ordinary
nested-diamond bipartition; recovers neither the expected scaling nor a horizon location without
the truncation of 3.3.2. Estado: `CONTRADICTED` (relative to continuum area/log-law expectation,
untruncated).

**3.3.2 Eigenmode truncation recovers continuum log-law scaling (1+1D flat only).** Truncating
the smallest eigenvalues of iΔ at λ̃_min∼√N/4π recovers S=a·ln(x)+b with a=0.346±0.028 (continuum
expects 1/3). Fuente: same paper, §3 —
`.../Entanglement_Entropy_in_Causal_Set_Theory_Yazdi.md:128-176,259-263`. Hipótesis: same 1+1D
flat causal-diamond setup, plus an explicit truncation rule motivated by the causet's fundamental
length as a low-pass filter. Dimensión: **1+1D flat only** — paper states explicitly
"it is not yet known how the truncation procedure... will generalize to higher dimensions." Qué
respalda: shows a Lorentz-invariant-compatible UV cutoff can be introduced in causal sets to
recover continuum-consistent entropy scaling — potentially transferable machinery, not a horizon
result. Qué NO demuestra: does not identify a black-hole horizon; does not generalize beyond
1+1D flat diamonds (explicitly open, two untested competing conjectures for higher-d);
Bekenstein-Hawking area-law normalization for a genuine event horizon is not addressed. Estado:
`PARTIAL`.

**3.3.3 Connection to black-hole horizon entropy: explicitly future work, not delivered.** "The
way now seems open to begin to address questions which hinge on understanding the entropy of
entanglement associated with black hole horizons... Work is also underway [ref marked 'in
preparation,' not read]." Fuente: same, §5 —
`.../Entanglement_Entropy_in_Causal_Set_Theory_Yazdi.md:254-263`. Estado: `UNSUPPORTED` (a
stated future direction, not a result).

### 3.4 Lineage D — causal horizon as boundary of the past of a future-inextendible curve

**3.4.1 Primary definition (Barton et al. 2019).** "H is a causal horizon, i.e. it is the
boundary of the past of a future inextendible timelike curve, γ₀, of infinite proper future
length: H := ∂I⁻(γ₀)." Fuente: Barton, Counsell, Dowker, Gould, Jubb, Taylor, Phys. Rev. D 100,
126008 (2019), arXiv:1909.08620 §2 — fetched live via alphaXiv; **since acquired:
`biblioteca/1909.08620v1.pdf`, §5.5 item 8** `[normalizado 2026-07-02]`. Hipótesis: (M,g) globally hyperbolic, Cauchy surface Σ; γ₀ future-inextendible
timelike of infinite proper future length; H meets Σ transversally in codim-2 spacelike J.
Dimensión: general d; horizon-type-agnostic (black-hole, Rindler, cosmological — citing Gibbons–
Hawking, Jacobson–Parentani for the latter two). Qué respalda: the precise, primary-source
definition underlying Lineage B's construction, and the exact distinction (infinite vs. finite
proper length) that separates horizon-crossing from singularity-terminating curves — directly
the distinction needed in 1+1D Schwarzschild. Qué NO demuestra: purely a continuum definition;
operationalizing it on a *finite* causal set is done separately (3.4.2). Estado: `SUPPORTED`
(definition; primary source read directly this session, not via secondary citation).

**3.4.2 Finite-causal-set operationalization via longest-chain diagnostic (this project's target
regime, 1+1D Schwarzschild).** "In [Barton et al.], this point was addressed by defining a causal
horizon H_c = ∂Past(γ₀)... We expand upon this idea for a causal set of finite size... For
minimal elements inside the horizon, the length of the longest chain is limited... the longest
chains starting at minimal elements outside the horizon are in practice only limited by the
overall size of the causal set... we observe a sharp transition [bimodal distribution] exactly
at the location of the horizon." Fuente: A. Eichhorn, P. Gamito, N. Stokes, "Towards black-hole
horizons and geodesic focusing in causal sets" (2026) —
`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:175-195`
(full treatment in §4 below). Hipótesis: sprinkling into 1+1D Schwarzschild toy model; requires
**geodesic incompleteness** (timelike curves inside the horizon must terminate at r=0 in finite
proper time) — explicitly does **not** work for geodesically-complete regular black holes (e.g.
Hayward). Dimensión: 1+1D Schwarzschild, finite sprinklings — the project's exact regime. Qué
respalda: an order-only, finite-causal-set-computable diagnostic for the same boundary this
project targets — a close, physically-motivated relative/cross-check for the project's own
observable (this is exactly PR-001's `dev/prototype_o.py:166-197` observable, independently
re-derived). Qué NO demuestra: fails for geodesically-complete black holes; is a local diagnostic
*approximating* H_c, not proven to converge to it as ρ→∞. Estado: `PARTIAL`.

---

## §4. Direct contrast paper: "Towards black-hole horizons and geodesic focusing in causal sets"

A. Eichhorn, P. Gamito, N. Stokes, Heidelberg (2026), local PDF at
`biblioteca/Towards black-hole horizons and geodesic focusing in causal sets.pdf`, derived-md at
`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md` (738
lines, read in full this session). Already summarized at a high level in `docs/roadmap.md`
(Phase 1/2/3 background); this section pins down the precise claims, thresholds, and numbers so
they can be compared line-by-line against this project's own results rather than paraphrased.

### 4.1 Diagnostic 1 — event horizon via longest timelike chain / minimal-element future cardinality

Covered in §3.4.2 above (bimodal longest-chain distribution). Complementary observable: future
cardinality of minimal elements is also bimodal (line 192-193), but "may be affected more
strongly by the choice of boundary" — for a causal diamond in Minkowski, future cardinality of
minimal elements already varies between n and √n with no horizon present, i.e. this
complementary observable is **more boundary-sensitive** and a weaker diagnostic than the
longest-chain one. **Estado**: `PARTIAL` (see 3.4.2); the cardinality variant specifically flagged
`CONTRADICTED`-adjacent as a false-positive risk in bounded regions — file:line 192-195.

### 4.2 Diagnostic 2 — apparent horizon via causal ladders + discrete geodesic expansion

**Enunciado exacto**: Causal ladder L_k (Definition 1, lines 245-260): a sequence of rungs
(p_i,q_i), each a link (p_i≺*q_i), satisfying five interval-cardinality conditions that pin the
ladder to a narrow opening angle around a null geodesic. Discrete expansion
E_I^{ab,n} = (1/N_J)Σ_J [D_IJ^{(a+n)(b+n)} − D_IJ^{ab}] / D_IJ^{ab} (Eq. 14, line 285), using the
causal-set predistance function of Eichhorn–Surya–Versteegen (2019, arXiv:1809.06192, ref [40]).
Results (rigid ladders, weighted average over sprinklings): mean(E)_Minkowski = 0.185±0.007 (Eq.
23, line 357 — a **nonzero systematic bias from discreteness**, continuum expectation is exactly
0); after Minkowski-baseline subtraction, mean(E)_{r<r_S} = −0.039±0.011,
mean(E)_{r>r_S} = 0.027±0.011 (Eq. 25, lines 380-381) — **sign changes across r=2M as expected**.

**Fuente primaria**: same paper, §IV (lines 197-386). Ladder concept originates in A.
Bhattacharya, A. Mathur, S. Surya, Gen. Rel. Grav. 55, 32 (2023), arXiv:2301.06480 (ref [15]) —
**since acquired, text layer legible (`biblioteca/2301.06480v1.pdf`, §5.5 item 9); only its
abstract has been spot-read, full text still not analyzed** `[normalizado 2026-07-02]`; the
definition and results attributed to it here are as restated/extended in the 2026 paper, which
is what was actually read.

**Hipótesis**: 1+1D setting only (ladders "defined for (1+1) dimensional settings" — line 128,
an explicit scope restriction of the underlying method, not just this paper's choice); requires
a **mandatory Minkowski-baseline subtraction** because discreteness itself biases mean(E) away
from zero (a purely discretization artifact, not a curvature signal) — the paper is explicit
that the baseline-subtracted value, not the raw one, is "the physically meaningful quantity"
(line 378). Requires many sprinklings for convergence (large fluctuations per-sprinkling, line
365-370) — costly.

**Dimensión y clase de espacios**: 1+1D Schwarzschild toy model (line 130-136, induced metric on
constant-angle submanifold) — exactly this project's own regime. Method explicitly stated as
generalizable in principle to any f(r) of the form ds²=−f(r)dt²+f(r)⁻¹dr² (line 159-164),
including regular black holes (Hayward, tested at line 156-169) where the event-horizon diagnostic
(§4.1) fails but this one is expected to survive (line 199).

**Qué respalda**: The single strongest external validation this project has for its own
methodology: an independent group, working in the same 1+1D Schwarzschild toy model, found it
**necessary** to run box-matched Minkowski controls and subtract a discreteness-induced baseline
before any horizon-crossing signal is physically meaningful — this is exactly the protocol
already in `docs/preregistration.md` Phase 0 step 4 ("run BH + box-matched Minkowski controls"),
now independently corroborated rather than merely internally motivated.

**Qué NO demuestra**: Costly — "requires numerous sprinklings... to converge" (line 469); the
magnitude of mean(E) itself is not shown to be a clean function of r (only its *sign* is
targeted: "our target is merely the sign of mean(E) in the two regions," line 386) — this is a
**weaker claim than localizing r=2M precisely**, only a two-region (interior/exterior)
classification, not a continuous localization. Also requires embedding information in practice
to separate ingoing/outgoing ladder pairs (line 482, "we have identified pairs of ladders that
are both out-(or in-)going by using embedding information, rather than using a
causal-set-intrinsic way" — explicitly flagged by the authors themselves as a limitation to be
fixed in future work via ladder *crossings*).

**Estado**: `PARTIAL` — sign-change result is real and reproduced with quoted uncertainties, but
(a) targets sign only, not localization precision comparable to this project's own O(ℓ)-resolution
goal, and (b) the practical implementation leaks embedding information for ladder orientation, a
methodological point this project's `NO_GROUND_TRUTH_LEAKAGE` guardrail should watch closely if
ladders are ever adopted here.

### 4.3 Diagnostic 3 — discrete horizon via fuzzy ladders

**Enunciado exacto**: Fuzzy ladder L_k^(M) (Definition 2, lines 405-421): drops rigid conditions
4-5 of Definition 1 down to interval-cardinality *windows* M−1≤|[p_{i−M},p_i]|≤2M−1 (and
symmetrically for q), trading rigidity for length. Rigid ladders are essentially never longer
than 5-6 rungs (line 392: "only find a single ladder with six rungs in a sprinkling with 2·10⁶
points"); fuzzy ladders (M=3) routinely reach 8 rungs (Fig. 13, line 436). Using fuzzy ladders
that originate near r=r_S and trace an outgoing null geodesic, the paper constructs "a portion of
a discrete horizon" (lines 441-445) — explicitly a **proof-of-principle**, not a general
construction (line 445: "our results constitute a proof-of-principle that a discrete
approximation of a black-hole horizon can be identified").

Discrete-expansion results with fuzzy ladders (M=3, 8-rung, N≥10, baseline-subtracted): interior
mean(E)_{Schw,r<r_S} = −0.33±0.01 (Eq. A2, line 645, "cleaner identification" than rigid ladders);
**exterior mean(E)_{Schw,r>r_S} = −0.16±0.01 (Eq. A3, line 650) — wrong sign**, the paper states
explicitly: "this is not the expected behavior, since the expansion in the Schwarzschild exterior
should be positive... rather than zero or negative" (line 655).

**Fuente primaria**: same paper, §V and App. C (lines 388-475, 580-656).

**Hipótesis**: Requires selecting the fuzzy-ladder origin "very close to r=r_S" **using embedding
information** (line 441-442: "we use the embedding information to identify the origin of an
appropriate ladder by simply selecting a ladder that starts very close to r=r_S" — an explicit,
acknowledged use of ground-truth information to construct the horizon candidate, not to score
it). Requires splitting "glued" ingoing/outgoing segments using embedding information as well
(line 594). Requires resolving a fuzzy-ladder self-intersection pathology (App. C.1, lines
584-592) via a heuristic (discard ladders sharing >half their points with a chosen representative,
line 586).

**Dimensión y clase de espacios**: 1+1D Schwarzschild toy model only, proof-of-principle scale
(O(10) sprinklings generated to find usable examples, line 443).

**Qué respalda**: Direct precedent for the project's own fork-A1 "construction" framing
(`docs/roadmap.md` Phase 3) — an independent group has already produced a portion of a discrete
1+1D Schwarzschild horizon from ladders, giving a concrete external target/comparison for any
future nachocausal construction attempt.

**Qué NO demuestra — the central caveat for this project**: **The construction, as published,
uses embedding (ground-truth) information as an ingredient in selecting and orienting the ladder
that becomes the horizon candidate, not only to score a horizon candidate obtained order-only.**
This is precisely the boundary this project's founding rule draws sharply
("the hidden embedding only scores; it never defines or guides the observable" — `CLAUDE.md`).
Any adoption of fuzzy ladders here would need an order-intrinsic replacement for both the
origin-selection step and the in/outgoing-splitting step (the paper itself proposes ladder
*crossings*, line 482-483, as an untested candidate for the latter) before it could be called an
order-only observable in this project's sense. Additionally: the exterior sign-flip failure
(4.3, Eq. A3) shows fuzzy ladders are **not uniformly more reliable** than rigid ones — rigidity
vs. length is a real trade-off, not a strict improvement, contrary to what "fuzzy ladders trace
longer geodesics" alone might suggest. The horizon is also explicitly an "unstable point in the
dynamics" (line 443-444) — ladders "peel off" after a few rungs by construction, so any
extraction of a long horizon segment requires an unproven iterative procedure the authors
explicitly "leave to future work" (line 443).

**Estado**: `PARTIAL` — genuine proof-of-principle result, but (a) methodologically incompatible
with this project's no-leakage rule as published, (b) not uniformly better than the rigid-ladder
diagnostic (exterior sign failure), (c) the horizon-instability/peeling problem is acknowledged as
unsolved by the source itself.

---

## §5. Poset order-dimension-2 combinatorics — bibliographic gap for C1, now partially closed

`comite_decision_012_c1-admissible-completion-class.md` (D1 table, row "Dimensión de orden ≤ 2")
invokes an equivalence — `dim_DM ≤ 2 ⟺ realizable as product order of 2 linear orders
(Dushnik–Miller)` — as settled by citation. As of the first pass of this dossier, no paper in
`biblioteca/` stated, proved, or even paraphrased this. **Update (2026-07-02): the user has since
acquired the primary source and its two classic secondary sources.** `biblioteca/` now contains
`dushnik_miller-partially_ordered_sets.pdf` (= `ordenes dimension 010.pdf`, byte-identical,
md5 `dc17be5441...`), `ordenes dimension 003.pdf` (identified this session, see 5.2), and
`ordenes dimension 009.pdf` (identified this session, see 5.2), plus a cluster of supplementary
order-theory background files (§5.4). `biblioteca/derived-md/Bombelli_1987_PhD.md:436-482`
remains the only *previously* local source touching this topic, and still explicitly declines to
state the theorem ("the usual definition, although equivalent to this one, looks quite different,
and it will not be necessary to give it here," line 443) — it is now superseded by the primary
source itself.

### 5.1 Dushnik–Miller (1941): now read in full — existence direction, reversibility theorem, and "conjugate" orders CONFIRMED

**Enunciado exacto** (read directly from the OCR'd JSTOR scan, `pdftotext` extraction, this
session — no derived-md yet, citations below are original paper pagination pp. 600-605):

- Dimension (§2.2, p. 601): "By the dimension of a partial order P defined on a set S is meant
  the smallest cardinal number m such that P is realized by m linear orders on S" — where P is
  *realized* by a collection of linear orders {L_α} iff P = ∩L_α (§2.1).
- **Conjugate orders** (§3.1, p. 602) — directly answers the "órdenes conjugados" item from the
  original literature-priorities request: "Let P and Q be two partial orders on the same set of
  elements S, and suppose that every pair of distinct elements of S is ordered in just one of
  these partial orders; in such a case we shall say that P and Q are conjugate partial orders. A
  partial order will be called *reversible* if and only if it has a conjugate."
- **Theorem 3.61** (p. 602-604), the dimension-2 equivalence itself, proved (not just stated):
  "The following four properties of a partial order P are equivalent: (1) P is reversible. (2)
  There exists a linear extension of P which is non-separating. (3) The dimension of P is ≤ 2.
  (4) There exists a representation of P by means of a family of intervals on some linearly
  ordered set." Proved via an explicit four-way cyclic implication (1)⟹(2)⟹(3)⟹(4)⟹(1), each
  step read and checked this session.
- Existence of arbitrary finite/transfinite dimension (Theorem 4.1, 4.22, p. 604-605): for every
  cardinal n there exists a partial order of dimension exactly n, with an explicit finite
  construction for n<∞ using a lemma of Erdős–Szekeres (1935) on monotone subsequences.

**Fuente primaria**: B. Dushnik, E.W. Miller, "Partially Ordered Sets," Amer. J. Math. 63(3)
(1941), 600–610. **Now locally archived**: `biblioteca/dushnik_miller-partially_ordered_sets.pdf`
(text-layer OCR present via the original JSTOR scan — fully machine-readable, confirmed this
session via `pdftotext`).

**Hipótesis**: General partial orders (finite or transfinite cardinality S); Theorem 3.61's
interval-representation clause (4) requires only *some* linearly ordered set as host, no metric
structure.

**Dimensión y clase de espacios**: Any poset; dimension-2 case (`dim_DM P ≤ 2`) = intersection
of **at most two** linear orders = existence of a conjugate = interval representation (the
`dim P = 1` chain case is included, trivially representable by repeating one order). No
restriction to causal-set-specific structure — this is pure order theory, imported into C1 by
analogy.

**Qué respalda**: This is now the actual, checkable primary source for the `dim_DM ≤ 2`
equivalence the committee decision invokes — not a name-drop but a read, verified four-way
theorem. It also directly furnishes the "conjugate order" vocabulary requested at the start of
this dossier effort, and the interval-representation characterization (clause 4) is a second,
independent way to certify `dim_DM ≤ 2` for an admissible completion, beyond checking for a
literal pair of linear extensions.

**Qué NO demuestra**: **Says nothing about uniqueness of the realizer/conjugate up to swapping
the two orders**, nor about automorphisms or modular decomposition — the proof of Theorem 3.61
only establishes *existence* of a conjugate/realizer pair when dimension ≤ 2, not that the pair
is essentially unique. This gap (§5.2 in the previous pass of this dossier) is **not closed** by
reading the primary source directly — the 1941 paper simply does not address the question.

**Estado**: `SUPPORTED` — primary source, now local, read in full this session (not a secondary
restatement). Supersedes the earlier `[UNVERIFIED]` entries built only on arXiv secondary
citations.

### 5.2 Kelly–Trotter (1982) and Trotter (1995): identified and now in `biblioteca/`, but not yet OCR-readable in this environment

Two more of the requested sources are confirmed present, via direct visual inspection of their
cover/first pages (both are scanner-only PDFs, no text layer — this environment has no
`tesseract`/`marker_single` available, so full-text extraction was not possible this session;
identification below is from an ILLiad library-request cover sheet and a running-head/TOC page
respectively, both read as images):

- **`ordenes dimension 003.pdf`** = D. Kelly, W.T. Trotter, "Dimension theory for ordered sets,"
  in I. Rival (ed.), *Ordered Sets* (Proceedings, NATO Advanced Study Institute, Banff, Aug 1981),
  NATO ASI Series C83, Reidel, 1982, pp. 171–211 (42 pages, matching the cited page range).
  Confirmed via an interlibrary-loan (ILLiad, Georgia Tech) cover sheet naming exactly this
  article, author, journal title, and page range. This is the exact chapter
  `biblioteca/derived-md/Bombelli_1987_PhD.md` cites and declines to restate.
- **`ordenes dimension 009.pdf`** = W.T. Trotter, "Partially Ordered Sets," Chapter 8 in
  *Handbook of Combinatorics* (R. Graham, M. Grötschel, L. Lovász, eds.), Elsevier, 1995, pp.
  433–480 (47 pages, matching). Confirmed via the chapter's own title page (visible: chapter
  number, title, author, department, and the handbook's copyright line). Table of contents
  visible on the same page: §1 Notation and terminology, §2 Dilworth's theorem and the
  Greene–Kleitman theorem, §3 Kierstead's chain partitioning theorem, §4 Sperner's lemma and the
  cross-cut conjecture, §5 Linear extensions and correlation, §6 Balancing pairs and the 1/3-2/3
  conjecture, §7 Dimension and posets of bounded degree, §8 Interval orders and semiorders, §9
  Degrees of freedom, §10 Dimension and planarity, §11 Regressions and monotone chains — **no
  section is titled specifically "realizers" or "irreducibility,"** so it is not yet clear
  (without OCR) whether this chapter contains the uniqueness-up-to-swap result either; §9
  "Degrees of freedom" is the most likely candidate by title alone but was not read.
- **`preview-9780080933849_A23543816.pdf`** = a bookseller front-matter/TOC preview of the same
  *Handbook of Combinatorics* Vol. 1 (confirmed: lists "8. Partially Ordered Sets" in its TOC,
  then begins Chapter 1 content) — does not itself contain Trotter's chapter text; superseded in
  value by `ordenes dimension 009.pdf`, which has the actual chapter.

**Estado**: both `PARTIAL` — confirmed correct, present, and correctly identified, but not yet
read at file:line level. `[UNVERIFIED content — identification only, from cover/TOC pages;
full-text OCR not available in this session's toolset]`. Flag for a future session with OCR
tooling (or `marker_single`, already used for this project's other derived-md conversions per
`CLAUDE.md`).

### 5.2bis Trotter (1976), "Combinatorial Problems in Dimension Theory for Partially Ordered
Sets": acquired and read in full (auditor pass, 2026-07-03) — does not resolve §5.3

**Identificación exacta**: W.T. Trotter, Jr., "Combinatorial Problems in Dimension Theory for
Partially Ordered Sets," *Colloques Internationaux du C.N.R.S. N°260 — Problèmes Combinatoires et
Théorie des Graphes* (Orsay, 1976), pp. 403–406. Locally archived at
`biblioteca/parcial_Set_Trotter.pdf` (4 pages, ClearScan OCR text layer — confirmed machine-readable
via `pdftotext`, unlike the `biblioteca/derived-md/`-less scans in §5.2). This is a **different,
shorter paper** from both the Kelly–Trotter (1982) chapter and the Trotter (1995) handbook chapter
already catalogued in §5.2 — a conference proceedings note, not a survey/handbook chapter.

**Contenido**: a short survey of results in poset dimension theory as of 1976 — Hiraguchi's
`Dim(X) ≤ |X|/2` bound and simplified proofs thereof, irreducible/doubly-irreducible posets,
existence of m-dimensional irreducible posets of arbitrary length (Trotter's own prior result),
splits `S(X)` and the inequality `Dim(X) ≤ Dim(S(X)) ≤ 1+Dim(X)`, amalgamations of rooted posets,
and `Dim(X × Y)` bounds for cartesian products. Ends with five open problems as of 1976.

**Qué respalda**: general poset-dimension background (irreducibility, splits, products);
tangential to but not overlapping the `dim_DM ≤ 2` equivalence itself (§5.1 already covers that,
via the primary Dushnik–Miller source).

**Qué NO demuestra**: **read in full this session — grepped for "uniqu", "realizer", "conjugate",
"automorph": zero occurrences.** It does not state, prove, or bear on realizer/conjugate
uniqueness-up-to-swap for dimension-2 posets. **§5.3's `UNSUPPORTED_GAP` verdict is unchanged by
this source.**

**Estado**: `SUPPORTED` (background only) — read in full, correctly identified, does not touch
the open question.

**Provenance note**: this file was present in `biblioteca/` (mtime 2026-07-02, the same session as
this dossier's other `[re-graded 2026-07-02 audit]` edits) but was never entered into this
dossier — found and closed out by `/auditor` (`docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md`,
finding #2) on 2026-07-03, not by the original dossier pass. §5.5's earlier claim that only item 2
was "genuinely missing" is corrected below.

### 5.3 Uniqueness / automorphisms / modular decomposition: `RESOLVED_NEGATIVELY` (2026-08-05)

> **Resolución, 2026-08-05.** Este ítem deja de ser una cita pendiente: la afirmación es
> **falsa**, con testigo explícito y verificable. Enumeración exhaustiva determinista de
> `S_n` clasificando el poset inducido `P_sigma` (`i < j` y `sigma(i) < sigma(j)`) por
> isomorfismo — `dev/r3_bridge_e_fibers.py`, sin aleatoriedad ni semillas — da fibras
> iguales a la órbita por inversión para `n <= 3` y **falla en `n = 4`**: la clase del
> poset «una 2-cadena más dos puntos aislados» tiene fibra de tamaño **tres**,
> `{3421, 4231, 4312}`, donde `4231` es auto-inversa y `4312 = 3421^{-1}`. Comprobación:
> `P_3421` tiene la única relación `1<2`, `P_4231` la única relación `2<3`, `P_4312` la
> única relación `3<4`; los tres son isomorfos. Luego un poset de dimensión 2 **puede
> tener realizadores esencialmente distintos**, y no solo el intercambio de los dos
> órdenes. Coherente con la descomposición modular de Gallai: el grafo de
> incomparabilidad del testigo es `K_4` menos una arista, descomponible y con varias
> orientaciones transitivas `[UNVERIFIED: Gallai 1967 no leído en primaria]`.
>
> **ESTO NO ES UNA CONTRIBUCIÓN.** El testigo es casi con certeza folclore. La estructura
> de las orientaciones transitivas de un grafo de comparabilidad está caracterizada por la
> **descomposición modular de Gallai (1967)**, y `K_4` menos una arista es el caso
> descomponible de manual; la terminología está en el propio survey local
> (`biblioteca/ordenes dimension 004.pdf`, l. 127-134, equivalencia de Baker et al. 1970, y
> problemas abiertos sobre *recognizing permutation graphs and transitively orientable
> graphs*). El valor de la enumeración fue **interno**: impedir que este repositorio
> siguiera persiguiendo un lema falso y reformular el puente E. No debe aparecer como
> resultado en ningún texto sometible. `[UNVERIFIED: Gallai 1967 y Golumbic no leídos en
> primaria; el enunciado de que esto es clásico es él mismo una conjetura bibliográfica.]`
>
> **Consecuencia operativa.** La instrucción de abajo («do not adopt "realizer uniqueness
> up to swap" as literature-backed») se **refuerza**: no es que falte respaldo, es que el
> enunciado es falso y no debe usarse en ninguna forma. Kelly–Trotter 1982 y Trotter 1995
> dejan de ser rutas a perseguir para esta pregunta; el OCR de §5.2 pierde esta
> motivación. Uso en curso: `research_program/work_packages/wp6_d2_null_copula_dichotomy.md`
> §5.2bis, donde el testigo obliga a reformular el puente E como injectividad en un único
> punto (E') en lugar de unicidad del realizador.

**Registro histórico previo a la resolución.** No source read to date — including the primary 1941 paper (§5.1) and the 1976 Trotter note
(§5.2bis), both now fully read — states or proves, for general dimension-2 posets, that the
realizer/conjugate is unique up to swapping the two linear orders.** The two most likely
remaining candidates to contain this (Kelly–Trotter 1982, Trotter 1995) are now physically present
in `biblioteca/` but not text-extractable without OCR tooling not available this session (§5.2).
Prior arXiv-based search for automorphism groups / modular decomposition of 2-dimensional posets
specifically (performed in the previous pass of this dossier) still returned nothing on-target.

**Do not adopt "realizer uniqueness up to swap" as literature-backed** anywhere in C1/`comite`
material until either (a) `ordenes dimension 003.pdf` or `009.pdf` is OCR'd and actually read, or
(b) another primary source is found and read. This remains exactly the class of claim
`CLAUDE.md`'s founding rule prohibits stating without verifiable backing — the *closest* it can
currently be stated is "the existence direction is proven (Dushnik–Miller 1941, §5.1); the
uniqueness direction is an open citation, physically present in the library but not yet legible
to any tool available this session."

### 5.4 Supplementary order-theory background now in `biblioteca/` (not explicitly requested, not deeply read this session)

Identified via `pdfinfo`/`pdftotext` metadata only — noted for completeness, not analyzed for
dossier-grade claims this session:

- `ordenes dimension 001.pdf` — J. Cohen, review of Davey & Priestley, *Introduction to Lattices
  and Order*. General order-theory background (lattices, joins/meets).
- `ordenes dimension 002.pdf` — excerpt from Davey & Priestley, *Introduction to Lattices and
  Order* itself (standard textbook).
- `ordenes dimension 004.pdf` — V.V. Ubale, A.N. Bhavale, "A Survey of Dimension of Posets"
  (recent survey; abstract explicitly mentions fractional dimension, geometric representations,
  and open problems — a useful map of the field, not yet mined for citable claims).
- `ordenes dimension 005.pdf` — V. Novák, "On the well dimension of ordered sets," Czechoslovak
  Math. J. 19(1) (1969), 1–16.
- `ordenes dimension 006.pdf` — P.C. Fishburn, *Utility Theory for Decision Making* — the
  standard reference for interval orders and semiorders (Fishburn is a foundational figure in
  that specific sub-area of dimension theory).
- `ordenes dimension 007.pdf` — I. Rabinovitch, "The Dimension of Semiorders," J. Combin. Theory
  Ser. A 25 (1978), 50–61.
- `ordenes dimension 008.pdf` — unattributed lecture notes/slides, "Combinatorics and algebra of
  partially ordered sets" (covers Hasse diagrams, and advanced/tangential material — Tamari
  posets, weight symbols, Calabi–Yau posets — likely too specialized to be load-bearing for C1).
- `fractional-graph-theory-a-rational-approach-to-the-theory-of-...pdf` — E.R. Scheinerman, D.H.
  Ullman, *Fractional Graph Theory: A Rational Approach to the Theory of Graphs* — relevant to
  the "fractional dimension" topic flagged in `ordenes dimension 004.pdf`'s abstract, not yet
  cross-checked.

None of these are marked `SUPPORTED` in this dossier — they are inventoried, not yet mined.

### 5.5 Acquisition status (updated 2026-07-02)

| # | Source | Status |
|---|---|---|
| 1 | Dushnik & Miller (1941) | **Acquired, read in full this session** — §5.1 |
| 2 | Trotter, *Dimension Theory* (1992 book) | Not acquired; substitutes present (Trotter 1995 handbook chapter, item 3 below) may cover the same ground — unread |
| 3 | Kelly & Trotter (1982) chapter | **Acquired**, not yet OCR-readable — §5.2 |
| 4 | arXiv:1710.09467 (Barrera-Cruz et al.) | **Acquired** (`1710.09467v2.pdf`), already read via alphaXiv in the prior pass |
| 5 | arXiv:1802.09326 (Majumder et al.) | **Acquired** (`1802.09326v3.pdf`), already read via alphaXiv |
| 6 | arXiv:0809.1828 (Brightwell & Massow) | **Acquired** (`0809.1828v1.pdf`), already read via alphaXiv |
| 7 | gr-qc/0302009 (Dou & Sorkin 2003) | **Acquired, read in full this session** — §3.1.1bis |
| 8 | arXiv:1909.08620 (Barton et al., horizon molecules) | **Acquired** (`1909.08620v1.pdf`), already read via alphaXiv |
| 9 | arXiv:2301.06480 (Bhattacharya, Mathur, Surya, ladders) | **Acquired**, text layer confirmed readable (`2301.06480v1.pdf`); abstract spot-read this session — see note below |
| 10 | arXiv:2307.04150 (Dou 2023, arXiv manuscript / invited handbook chapter) | **Acquired**, text layer confirmed readable (`2307.04150v1.pdf`); chronological review of horizon-molecule proposals, submitted to arXiv 2023-07-09 as an invited chapter for the *Handbook of Quantum Gravity* — no published-edition reference documented, so dated 2023 until one is; full read still pending |
| 11 | Trotter (1976), CNRS Colloque N°260 note | **Acquired, read in full** (`parcial_Set_Trotter.pdf`) — §5.2bis; found present-but-uncatalogued by `/auditor` audit 003, 2026-07-03; does not resolve §5.3 |

**Late addendum (item 9)**: the abstract of arXiv:2301.06480 — "Null Geodesics from Ladder
Molecules," A. Bhattacharya, A. Mathur, S. Surya — states a result not captured in §4.2's
secondhand summary: **"similar to the uniqueness of null geodesics between horismotically
related events in M², in such causal sets there is a unique ladder molecule between any two
linked pairs which are related by the generalised horismotic relation."** This is a genuine
uniqueness theorem (of ladders, not of order-dimension-2 realizers — a different "uniqueness"
question from §5.3) that the 2026 paper's own restatement in §4.2 did not surface; worth a full
read in a future session since it may bear on how reliable the rigid-ladder diagnostic is in
principle, as opposed to only empirically. Not yet marked `SUPPORTED`/entered in §3-4 — abstract
only, full text not analyzed this session.

**Still genuinely missing after this pass**: only item 2 (Trotter's 1992 book) has no local
substitute confirmed to cover the same ground — and even that is provisional, since item 3 is
physically acquired but not yet actually legible (OCR blocker), and items 9-10 are acquired and
legible but not yet fully read for dossier-grade claims. `[Correction, 2026-07-03: this claim was
itself incomplete — item 11 (Trotter 1976, `parcial_Set_Trotter.pdf`) was already present in
`biblioteca/` at the time this sentence was written but had not been entered into this dossier;
found by `/auditor` audit 003. It is a real but partial substitute — general poset-dimension
background, not a hit on the §5.3 uniqueness question. The residual gap is unchanged: only a
genuine reading of Kelly–Trotter (1982) or Trotter (1995) (item 3, OCR-blocked) can close §5.3.]`
