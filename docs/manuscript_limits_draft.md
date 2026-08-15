# Finite order-only observation of Schwarzschild patches: exact scale blindness and a matching minimax localization rate

**José Ignacio Martín-Gandul**

Independent researcher, Alcalá de Guadaíra, Seville, Spain
`adnacho@gmail.com`

---

## Abstract

We study which continuum-geometric properties are identifiable from the
isomorphism class of a finite causal set sprinkled into a Schwarzschild patch,
typically conditional on \(N=n\). The organizing distinction is between absolute
scale, dimensionless patch shape, and completion-dependent targets. Absolute mass
is exactly invisible under patch-shape-preserving co-scaling, in \(1{+}1\)
dimensions and in a scoped \(3{+}1\) class, while the global event horizon is not a
functional of one finite causally convex patch. By contrast, on a regular
one-parameter family of fixed-corner \(1{+}1\) diamonds, the comparable-pair
fraction yields an explicit estimator whose uniform risk is \(O(n^{-1/2})\) for
fixed sufficiently small null lapse. A Fisher-information two-point bound gives
the matching \(\Omega(n^{-1/2})\) lower rate, so the minimax rate is
\(n^{-1/2}\). The constants are not sharp; a deterministic lapse sweep supports,
but does not prove, the conjectured quadratic small-lapse Fisher scaling.
For the future-cardinality observable used in a preregistered in-patch experiment, we
also derive an exact tagged-element binomial law and its finite-\(n\) correlation
attenuation. The empirical result is reported with its artifact caveat, and a
short record of unsuccessful region-locators is retained as experimental context,
not as evidence for a universal no-go. The results show that fixed-\(n\) order can retain
dimensionless shape information while supplying neither an external ruler nor a
global completion.

**Keywords.** causal sets; order-only observation; Schwarzschild; identifiability;
total variation; Fisher information; recoverability benchmark; event horizon
(teleology)

---

## §1 Introduction and observation model

### 1.1 Recoverability, not reconstruction

Causal set theory proposes that continuum Lorentzian geometry is recovered, in a
suitable limit, from a locally finite partial order together with counting
information—the slogan “Order + Number equals Geometry” (reviewed by Surya
[12]). The present work does
**not** attempt continuum reconstruction of a black-hole spacetime. It asks a
narrower, finite-sample question:

> Given only the isomorphism class of a finite causal set sprinkled into a
> Schwarzschild *patch*, which geometric targets are identifiable, at what rate,
> and which targets are information-theoretically or definitionally out of reach?

We call affirmative answers under a fixed protocol *recoverability* results, and
negative answers that apply to all measurable functions of the observation
*non-identifiability* results. We reserve *reconstruction* for structural recovery
of continuum geometry, which is not claimed here.

### 1.2 The observation channel

A *completion* is a Lorentzian region of finite volume equipped with a Poisson
point process of intensity \(\varrho\) with respect to the volume measure. The
induced causal set is the set of points ordered by the manifold’s causal
relation. Two observation models must be kept distinct
as formalized in Lemma 2.1:

| Channel | Observation | Role in this paper |
|---|---|---|
| **Order-only, fixed \(n\)** | Isomorphism class of the poset conditioned on \(N=n\) | Primary channel for Theorems 3.1, 3.8, and 3.9 |
| **Order+number** | Joint law of order and cardinality (e.g.\ \(N\sim\mathrm{Poisson}(\varrho\,\mathrm{Vol}(W))\) with \(\varrho\) known) | Contrast only: scale can re-enter through \(N\) (Remark after Thm 3.1) |

Conditioning on \(N=n\) removes the total-volume leak through cardinality: the \(n\)
points are i.i.d.\ from the normalized volume measure. Absolute scale is then
precisely what a constant conformal (or co-scaling) orbit can hide; that is the
content of Theorem 3.1, not an artifact of a bad estimator.

Figure 1 summarizes this loss of embedding information in the observation map.

![**Continuum-to-order observation map.** Left: embedding information
available to a continuum observer; right: the same finite causal relations after
coordinates are discarded. Vertical placement on the right encodes order height and
horizontal placement is diagrammatic only. The panel illustrates the observation
channel, not continuum reconstruction.](../viz/output/fig01_dictionary.png){width=100%}

\clearpage

### 1.3 Hidden embeddings score only

Wherever a numerical benchmark is reported, continuum embeddings and horizon
labels are used **only to score** an estimator’s output. They do not enter the
definition of the observable, the selection rule, or the frozen thresholds. An
estimator that requires the embedding is outside the order-only channel.

### 1.4 Three objects that must not be conflated

Three targets must be kept distinct:

1. **Global event horizon** — a set defined by the causal structure of the full
   spacetime (e.g.\ boundary of the past of future null infinity). It depends on
   the continuation outside any finite causally convex patch (Theorem 3.2).
2. **Singularity-truncation cut** — in a frozen *singular* Schwarzschild family,
   an in-patch locus associated with the artificial edge of the computational
   domain near \(r=0\). It is not a quasi-local trapping surface and must not be
   renamed as one.
3. **Quasi-local proxy** — expansion, trapping, or codimension-two screen
   analogues defined by a separate continuum contract. In \(1{+}1\) dimensions
   there is no spatial 2-sphere carrying a standard null expansion; continuum
   “ladder” constructions in the literature use one-dimensional stand-ins and do
   not automatically supply an order-only codimension-two object in \(3{+}1\)
   (see §6.4).

Every positive or negative statement in this paper names which of (1)–(3) is at
stake; none is silently substituted for another.

### 1.5 Scale versus shape

The scale-blindness and localization results concern different statistical
families. Theorem 3.1 compares \((r_s,W)\) with \((sr_s,\Phi_s(W))\): parameter and
patch are co-scaled, so every dimensionless feature of the experiment is held
fixed. Theorems 3.8–3.9 instead keep the Eddington--Finkelstein corners fixed while
\(\tau\) varies. Ratios such as \(r_p/\tau\), \(r_q/\tau\), and
\((v_q-v_p)/\tau\) then change, and so can the order law. There is no
contradiction: a fixed-\(n\) order supplies no external unit of length, but it can
retain information about dimensionless patch shape. The paper does not claim that
arbitrary dimensionless geometry is recoverable.

### 1.6 Contributions (and non-contributions)

The paper has three components:

| Component | Content | Where |
|---|---|---|
| **Theory** | Exact co-scaling blindness; global-event-horizon nonlocality; and matching minimax upper and lower rates on a regular fixed-corner \(1{+}1\) family | Theorems 3.1, 3.2, 3.8–3.9 and Corollary 3.10 |
| **Future cardinality** | An exact tagged-element law and a preregistered in-patch evaluation of the same observable | Section 4 |
| **Empirical context** | A compact record of seven unsuccessful region-localization constructions | Section 5 |

**Explicitly not claimed as independent contributions:**

- the Order+Number slogan or continuum conformal determination of the metric
  (Theorem 3.1 is a finite-\(n\) formalization);
- textbook two-point, Hellinger, data-processing, Hoeffding, and Chebyshev
  machinery (Theorems 3.8–3.9 instantiate it on a regular family);
- data-processing asymmetry as mathematical novelty (it is textbook);
- that causal sets “cannot see black holes” in any unrestricted sense.

We do not claim to reconstruct a Schwarzschild event horizon from a finite causal
set. We identify what this observation channel can and cannot determine, and at
what statistical rate, under explicit geometric families.

**Organizing thesis.** In the experiments studied here, fixed-\(n\) order retains
aspects of dimensionless patch shape, but supplies neither an absolute scale nor
completion-dependent global information. Theorem 3.1 removes the ruler, Theorem
3.2 removes the completion, Theorems 3.8–3.9 quantify estimation within shape, and
§4 gives a recoverable shape functional.

---

## §2 Setup: geometry, sprinkling, and targets

### 2.1 Geometry in \(1{+}1\) dimensions

The primary arena is **1+1 Schwarzschild**. In ingoing Eddington–Finkelstein (EF)
coordinates \((v,r)\),

\[
g_\tau
=
-(1-\tau/r)\,dv^2 + 2\,dv\,dr,
\qquad
\tau>0,
\]

with horizon at \(r=\tau\) and volume element \(dv\,dr\) (\(\det g=-1\)). Global null
coordinates \((\tilde U,v)\) exist in which the causal order is the product order
and the horizon sits at \(\tilde U=0\); the explicit transformation is derived in
§3.3.2.

**Diamond family (regular family for Theorems 3.8–3.9).** Fix corners
\(z_{\mathrm{out}}=(v_p,r_p)\) (exterior) and
\(z_{\mathrm{in}}=(v_q,r_q)\) (interior) with
\(0<r_q<\tau_0\le\tau_1<r_p\) and \(v_p<v_q\). For each
\(\tau\in[\tau_0,\tau_1]\) the patch is the causal diamond

\[
D_\tau
:=
J^+_\tau(z_{\mathrm{out}})\cap J^-_\tau(z_{\mathrm{in}}).
\]

In null coordinates \(D_\tau\) is a coordinate box straddling the horizon, with
minimal radius \(r_q>0\) (singularity avoided). This is the family on which
quadratic-mean differentiability and the localization floor are proved (Section 3.3).

**Dilation orbit (family for Theorem 3.1 in \(1{+}1\)).** For \(s>0\), the map
\(\Phi_s(t,r)=(st,sr)\) pulls \(g_{s r_s}\) back to \(s^2 g_{r_s}\). Patches are
transported covariantly: \(W\mapsto\Phi_s(W)\). No null-box assumption is required
for the exact \(\mathrm{TV}=0\) statement (Section 3.1).

### 2.2 Geometry in \(3{+}1\) dimensions (scoped use only)

We do **not** develop a \(3{+}1\) reconstruction theory. Fix a compact mass interval
\(I_M=[M_{\min},M_{\max}]\subset(0,\infty)\) and a dimensionless patch-shape vector

\[
\lambda=(v_0,v_1,u_{\mathrm{out}},u_{\mathrm{in}},\varepsilon_s),
\quad
0<v_0<v_1,
\quad
u_{\mathrm{out}},u_{\mathrm{in}}>0,
\quad
u_{\mathrm{in}}v_1\le 1-\varepsilon_s,
\quad
0<\varepsilon_s<1.
\]

In dimensionless Kruskal coordinates \((U,V,\omega)\), \(\omega\in S^2\), put
\(\xi=r/(2M)\), so that

\[
-UV=(\xi-1)e^\xi,
\qquad
\mathcal D_{\max}=\{(U,V,\omega):UV<1\}.
\]

Thus the maximal Schwarzschild domain is represented by the same dimensionless
manifold for every \(M\). For each temporal sector \(\sigma\in\{+,-\}\), its metric
and chosen time orientation may be written

\[
g_M^\sigma=M^2\widehat g^\sigma,
\qquad \mathfrak t^\sigma,
\]

where \(\widehat g^\sigma\) is independent of \(M\). This factorization, rather than
any convention-dependent numerical coefficient in the Kruskal line element, is all
that the proof below uses. Define

\[
\begin{aligned}
K^+_\lambda
&=
\{(U,V,\omega):V\in[v_0,v_1],\;
U\in[-u_{\mathrm{out}},u_{\mathrm{in}}],\;\omega\in S^2\},\\
d(U,V,\omega)&=(-V,-U,\omega),
\qquad
K^-_\lambda=d(K^+_\lambda).
\end{aligned}
\]

The inequalities in \(\lambda\) keep these compact patches away from the
singularity \(UV=1\); hence their positive metric volumes are finite and nonzero.
For fixed \(\sigma\) and \(\lambda\), the scoped class is

\[
\mathcal G^\sigma_{3+1}(\lambda,I_M)
=
\left\{
\bigl(K^\sigma_{M,\lambda},g_M^\sigma,\mathfrak t^\sigma,
\mu_M^\sigma,\prec_M^\sigma\bigr):M\in I_M
\right\}.
\]

Here \(K^\sigma_{M,\lambda}\) is the copy of \(K^\sigma_\lambda\) in the
mass-\(M\) maximal extension, \(\mu_M^\sigma=|d\mathrm{Vol}_{g_M^\sigma}|\), and
\(\prec_M^\sigma\) is maximal-Schwarzschild causality restricted to pairs of
patch points. Theorem 3.1 also holds if this is replaced by intrinsic patch
causality: its explicit conformal map carries the patch onto the patch and hence
carries causal curves that remain inside one patch to curves that remain inside
the other.

The only \(3{+}1\) result used as a theorem is the co-scaling orbit for absolute
mass at fixed \(n\) inside this fixed sector and shape. Dimensionless targets such
as \(r/(2M)-1\) are constant on that orbit; transfer of \(1{+}1\) localization
proxies to \(3{+}1\) region-finding remains outside scope. The complete argument
needed here is given in §3.1.

### 2.3 Sprinkling and laws

Let \((W,g)\) be a finite-volume patch. A Poisson point process of intensity
\(\varrho>0\) with respect to \(\mathrm{vol}_g\) induces a random finite causal set.
This volume-based sprinkling is the standard Lorentz-invariant discretization; in
Minkowski space, Bombelli, Henson, and Sorkin (2006) show that no measurable
equivariant rule extracts a preferred direction from it. Their theorem motivates
the sampling choice but is not used in our finite-patch proofs [4].
Write:

| Symbol | Meaning |
|---|---|
| \(P_{g,\varrho}\) | Law of the unlabeled poset including random cardinality |
| \(P_{g,n}\) or \(Q^n\) | Law conditioned on \(N=n\) (order-only fixed-\(n\) channel) |
| \(P^{\mathrm{order+number}}_{g,\varrho}\) | Joint law of order and \(N\) when \(\varrho\) is part of the model |

**Lemma 2.1 (cardinality conditioning).**
Conditioned on \(N=n\), the \(n\) points are i.i.d.\ with law
\(\mathrm{vol}_g/\mathrm{vol}_g(W)\).

*Proof.* For disjoint measurable cells \(A_1,\ldots,A_m\) partitioning \(W\),
independent Poisson counts conditioned on their sum \(n\) have the multinomial
law with cell probabilities
\(\mathrm{vol}_g(A_j)/\mathrm{vol}_g(W)\). Refining the partition gives the joint
law of \(n\) independent points from normalized volume. \(\blacksquare\)

**Lemma 2.2 (copula reduction on null boxes).**
If the patch is a coordinate box in global null coordinates with metric
\(g=-\Omega\,dU\,dV\), \(\Omega>0\) continuous, then the unlabeled poset law at
fixed \(n\) depends on \(g\) only through the copula of the normalized volume
measure.

*Proof.* Continuity and strict positivity of \(\Omega\) on the compact box make
both marginal densities continuous and strictly positive. Hence their distribution
functions \(\mathsf F\) and \(\mathsf G\) are strictly increasing. The
probability-integral transform
\((U,V)\mapsto(\mathsf F(U),\mathsf G(V))\) sends each sampled point to the unit square with the
associated copula law. Both coordinates are strictly increasing, so the transformation
preserves the product causal order. Applying it independently to all \(n\) points
and then forgetting labels proves the claim. \(\blacksquare\)

For a member of the scoped \(3{+}1\) class, let

\[
\nu_{M,\sigma,\lambda}
:=
\frac{\mu_M^\sigma|_{K^\sigma_{M,\lambda}}}
{\mu_M^\sigma(K^\sigma_{M,\lambda})}.
\]

Draw \(X_1,\ldots,X_n\) independently from this probability measure and put
\(i\prec_X j\) exactly when \(X_i\prec_M^\sigma X_j\), using the ambient relation
just defined. Write \(P^{\mathrm{fixed}\,n}_{M,\sigma,\lambda}\) for the law after
forgetting the labels. For \(n=0\) this is the point mass at the empty poset.

**Lemma 2.3 (measure--order coupling).**

Let \((K,\prec,\nu)\) and \((K',\prec',\nu')\) be causal probability spaces. Suppose
there are conull representatives and a bimeasurable bijection
\(\psi:K\to K'\), with inverse measurable modulo null sets, such that

\[
\psi_\#\nu=\nu',
\qquad
x\prec y\ \Longleftrightarrow\ \psi(x)\prec'\psi(y)
\quad\text{for }(\nu\otimes\nu)\text{-almost every }(x,y).
\]

Then the labeled and unlabeled fixed-\(n\) poset laws agree for every \(n\ge0\).

*Proof.* Couple \(X_i\sim\nu\) with \(Y_i=\psi(X_i)\). The transported points are
i.i.d. with law \(\nu'\). For a finite sample, the union over the finitely many
distinct ordered pairs \((i,j)\), \(i\ne j\), of the exceptional events in the
displayed equivalence is null. Hence all labeled relations agree almost surely.
Applying the measurable map
that forgets labels preserves equality in law. The case \(n=0\) is immediate.
\(\blacksquare\)

Total variation \(\mathrm{TV}\) and Hellinger distance \(H\) between laws on the
space of finite unlabeled posets are the standard ones, with the convention fixed
once and for all as

\[
H^2(P,Q)
:=
\int\bigl(\sqrt{dP}-\sqrt{dQ}\bigr)^2
\;=\;
2\Bigl(1-\!\int\!\sqrt{dP\,dQ}\Bigr)
\;\in[0,2].
\]

We use \(\mathrm{TV}\le H\), the data-processing inequality for both distances
under a common measurable map, and the **exact tensorization identity** for
product samples: since the affinity \(\int\sqrt{dP\,dQ}=1-\tfrac12H^2(P,Q)\)
factorizes over independent coordinates,

\[
1-\tfrac12\,H^2\bigl(P^{\otimes n},Q^{\otimes n}\bigr)
\;=\;
\Bigl(1-\tfrac12\,H^2(P,Q)\Bigr)^{\!n}.
\]

With \(t:=\tfrac12H^2(P,Q)\in[0,1]\), Bernoulli's inequality \((1-t)^n\ge 1-nt\)
turns this into the form used in Theorem 3.8,

\[
H^2\bigl(P^{\otimes n},Q^{\otimes n}\bigr)\;\le\;n\,H^2(P,Q).
\]

These distance identities are standard and are included to fix conventions.

### 2.4 Targets

A *target* is a map \(\mathcal T\) from completions to a metric space
\((\Theta,d_\Theta)\).
An *order-only estimator* is any (possibly randomized) measurable map from
isomorphism classes of finite posets into \(\Theta\). Risk is
\(\mathbb{E}\,d_\Theta(\widehat{\mathcal T},\mathcal T)\); minimax risk is the infimum over
estimators of the supremum risk over the declared family.

Targets used in this paper:

| Target | Symbol | Status in this paper |
|---|---|---|
| Absolute horizon radius / mass | \(r_s\), \(M\) | Non-identifiable at fixed \(n\) (Thm 3.1) |
| Continuous diamond parameter | \(\tau\in[\tau_0,\tau_1]\) | Minimax rate \(n^{-1/2}\) at fixed small lapse (Thms 3.8–3.9 and Cor. 3.10); not a distinct horizon invariant |
| Global event-horizon incidence | \(\chi_{\mathrm{EH}}(W;\mathcal M,g)\) | Not a functional of a finite causally convex patch (Thm 3.2) |
| In-patch future-cardinality score | Section 4 | Exact tagged law and bounded empirical recoverability |
| Region-locators C1–C6 | named combinatorial constructions | Empirical failures summarized in §5 |

Every guarantee below specifies its geometric family, observation channel,
target, loss, and direction. In particular, empirical failure of a named
estimator is never used as a proof of non-identifiability.

### 2.5 Notation

The following symbols keep their displayed meanings across sections; auxiliary
letters introduced inside one proof are local to that proof.

| Symbol | Meaning |
|---|---|
| \(W\) | Generic observed finite patch |
| \(D_\tau\) | Fixed-corner causal diamond at parameter \(\tau\) |
| \(z_{\mathrm{out}},z_{\mathrm{in}}\) | Exterior and interior EF corners; their coordinates retain subscripts \(p,q\) |
| \(\Theta=[\tau_0,\tau_1]\), \(\Theta_{\mathrm{ext}}\) | Compact parameter set and a containing open interval |
| \(\Delta v=v_q-v_p\) | Null lapse of the fixed-corner diamond |
| \(P_{g,\varrho},P_{g,n},Q_\tau^n\) | Poset laws; \(P\) is reserved for probability-law notation |
| \(p(\tau),S_n,\widehat p_n\) | Comparable-pair probability, count, and ordering fraction |
| \(c_\tau,I(\tau),\bar I\) | Copula density, Fisher information, and its supremum on \(\Theta\) |
| \(\mathcal R_\tau,\mathcal V(\tau),\mathcal E(\tau,\Delta v)\) | Outgoing-ray flow, diamond volume, and small-lapse remainder |
| \(J^\pm(x)\) | Causal future/past of \(x\) |
| \(L,U,Y,F,\alpha_n\) | Pretagged label, continuum future fraction, time score, future count, and attenuation in §4.1 |
| \(\varrho,\ell=\varrho^{-1/d}\) | Sprinkling intensity and discreteness length |
| \(H,\mathrm{TV}\) | Hellinger and total-variation distances |

## §3 Exact obstructions and fixed-\(n\) statistical limits

This section separates equality of laws along a co-scaling orbit, dependence of a
global target on data outside the patch, and statistical estimation inside a
fixed-corner family. The last problem receives both a lower bound valid for every
order-only estimator and a constructive upper bound based on comparable pairs.
None of these conclusions is inferred from the empirical locator failures in §5.

Completions, the fixed-\(n\) channel, cardinality conditioning, copula reduction,
and measure--order coupling are defined and proved in §2.

### 3.1 Exact scale blindness at fixed cardinality

#### Theorem 3.1 (exact witness orbit for absolute scale)

**1+1 dimensions.** Let \(g_{r_s}\) be the 1+1 Schwarzschild metric with horizon
radius \(r_s>0\), let \(W\) be any finite-volume patch, and let
\(\Phi_s(t,r)=(st,sr)\) for \(s>0\). Write \(\mathbb P_n(r_s;W)\) for the law of the
unlabeled \(n\)-element poset obtained by conditioning the sprinkling of
\((W,g_{r_s})\) on \(N=n\). Then, for every \(n\ge 0\) and every \(s>0\),

\[
\mathrm{TV}\bigl(\mathbb P_n(r_s;W),\,\mathbb P_n(s r_s;\Phi_s(W))\bigr)
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
dilation orbit \(\{r_s>0\}\) shares a single poset law at each fixed \(n\): **within this
orbit, the observed finite order carries no information about \(r_s\) in absolute
units**.

*Proof.*
By direct computation, \(\Phi_s^* g_{s r_s}=s^2 g_{r_s}\). A constant conformal factor
preserves causal order. Volume forms in 1+1 dimensions scale by \(s^2\), which cancels
under normalization of the sampling measure. By Lemma 2.1, the \(n\) i.i.d.\ sample on
the dilated geometry is the \(\Phi_s\)-image in law of the sample on the original
geometry, with identical induced relations. Unlabeled poset laws therefore coincide,
and total variation vanishes. The estimation consequence follows by applying the
same two-point decision rule to two identical distributions. \(\blacksquare\)

**3+1 dimensions (scoped).** In
\(\mathcal G^\sigma_{3+1}(\lambda,I_M)\), not as a general Hauptvermutung. Fix
\(\sigma\in\{+,-\}\), \(\lambda\), and masses \(M,M'\in I_M\). Then, for every
\(n\ge0\),

\[
P^{\mathrm{fixed}\,n}_{M,\sigma,\lambda}
=
P^{\mathrm{fixed}\,n}_{M',\sigma,\lambda}.
\]

Consequently the corresponding total variation distance is zero. Thus absolute mass
(and absolute \(r_h=2M\)) is non-identifiable in the fixed-\(n\) order-only channel
inside each fixed sector and shape. Dimensionless targets such as \(r/(2M)-1\) are
constant along the orbit and are not constrained by this equality.

*Proof of the scoped \(3{+}1\) statement.* Put \(s=M'/M>0\). Between the two copies
of the maximal dimensionless Kruskal domain define

\[
\Phi_s:\mathcal D_{\max,M}^{\sigma}\longrightarrow
\mathcal D_{\max,M'}^{\sigma},
\qquad
\Phi_s(U,V,\omega)=(U,V,\omega).
\]

It is a diffeomorphism with inverse \(\Phi_{1/s}\), preserves the fixed temporal
sector and its time orientation, and maps
\(K^\sigma_{M,\lambda}\) onto \(K^\sigma_{M',\lambda}\). Since
\(g_M^\sigma=M^2\widehat g^\sigma\),

\[
\Phi_s^*g_{M'}^\sigma
=
s^2g_M^\sigma.
\]

In particular, for every tangent vector \(Z\),

\[
g_{M'}^\sigma(d\Phi_s Z,d\Phi_s Z)
=
s^2g_M^\sigma(Z,Z).
\]

The positive factor preserves timelike, null, and causal character. Together with
the preserved time orientation, \(\Phi_s\) sends every future-directed causal curve
to one of the same type; applying \(\Phi_{1/s}\) gives the converse. Therefore, for
all patch points,

\[
x\prec_M^\sigma y
\quad\Longleftrightarrow\quad
\Phi_s(x)\prec_{M'}^\sigma\Phi_s(y).
\]

For ambient causality, a witnessing curve may leave the patch and \(\Phi_s\)
transports the whole curve. For intrinsic patch causality, a witnessing curve
remains in \(K^\sigma_{M,\lambda}\), and its image remains in
\(K^\sigma_{M',\lambda}\); applying the inverse gives the converse. Thus the same
statement holds for either convention. The difficult converse direction of the
conformal-causality theorems is not used because the conformal map is explicit.

In four dimensions the positive volume measure scales as

\[
\Phi_s^*\mu_{M'}^\sigma=s^4\mu_M^\sigma,
\qquad
\mu_{M'}^\sigma(K^\sigma_{M',\lambda})
=s^4\mu_M^\sigma(K^\sigma_{M,\lambda}).
\]

Hence the constant cancels after conditioning on cardinality:

\[
(\Phi_s)_\#\nu_{M,\sigma,\lambda}
=
\nu_{M',\sigma,\lambda}.
\]

The restriction of \(\Phi_s\) to the patches is a bimeasurable bijection satisfying
the hypotheses of Lemma 2.3 (indeed, the order equivalence holds everywhere, not
merely almost everywhere). The fixed-\(n\) unlabeled poset laws are therefore equal
for every \(n\ge1\); for \(n=0\) both are the point mass at the empty poset.
\(\blacksquare\)

#### What Theorem 3.1 does not say

1. **The patch is co-scaled.** The theorem compares \((r_s,W)\) with
   \((sr_s,\Phi_s(W))\); it does not assert equality of laws when one externally
   specified absolute patch is held fixed as the mass varies. An external length
   reference breaks this particular witness orbit and can make identification
   possible, but does not by itself prove identifiability. The fixed-corner family
   of Theorems 3.8–3.9 is an explicit case in which the order law does vary.
2. **Relative location.** Targets expressed in units of the discreteness scale
   \(\ell=\varrho^{-1/d}\), of the patch size, or of \(\sqrt{n}\), are invariant under
   the dilation orbit and are untouched.
3. **Order+number with known density.** If \(N\sim\mathrm{Poisson}(\varrho V)\) is
   observed and \(\varrho>0\) is known, the pair with \(s\neq 1\) is typically
   distinguishable through cardinality alone at precision \(\sim 1/\sqrt{n}\).
   Scale is a *Number* observable in that
   channel.
4. **Continuum background.** Conformal determination from causal structure and the
   causal-set “Order + Number” principle are standard. Hawking--King--McCarthy,
   Malament, Bombelli, Braun, and Madsen provide relevant continuum or reconstruction
   context [1,3,6--8]. The contribution here is the exact finite-\(n\) total-variation statement
   for the declared Schwarzschild sprinkling orbit, not a new continuum theorem.

Figures 2 and 3 should be read together: the first is the exact coupling witness;
the second is a deliberately bounded illustration of scale-free variation that the
theorem does not rule out.

![**Coupling witness for Theorem 3.1 in 1+1 dimensions.** Panels A and B
use one point sample and its image under \(\Phi_s\); panel D therefore shows the
same relations element by element. This visualizes the coupling used to prove
equality of poset laws. It does **not** assert that two independently generated
sprinklings are elementwise identical.](../viz/output/fig02_invisible_scale.png){width=100%}

![**A scale-free companion to Figure 2.** The comparable-pair fraction
is evaluated for \(N=60\) on co-scaled exterior rectangles, with 80 repetitions per
point and fixed seed 4242. The empirical variation with dimensionless patch placement
does not establish recovery, injective identification, or horizon localization.
The overlap of the independent \(r_s=1\) and \(r_s=7\) ensembles is consistent with
the exact co-scaling law of Theorem 3.1.](../viz/output/fig03_what_is_recoverable.png){width=100%}

\clearpage

### 3.2 The global event horizon is not a functional of data from a finite causally convex patch

#### Theorem 3.2 (teleological two-point obstruction)

For an asymptotically flat completion \((\mathcal M,g)\) and an observed patch
\(W\), define
the binary target
\[
\chi_{\mathrm{EH}}(W;\mathcal M,g)
:=
\mathbf 1\{W\cap\mathcal H^+(\mathcal M,g)\ne\varnothing\},
\]
where \(\mathcal H^+(\mathcal M,g)\) is the future event horizon. There exist two admissible
completions, indexed by \(j=0,1\), and a finite-volume patch \(W\) that is causally
convex in **both** completions, such that their restricted metrics, volume measures,
and causal relations agree on \(W\), while
\(\chi_{\mathrm{EH}}(W;\mathcal M_0,g_0)=0\) and
\(\chi_{\mathrm{EH}}(W;\mathcal M_1,g_1)=1\). Consequently, for every possibly randomized
estimator \(\widehat\chi\) based only on the finite-patch data,
\[
\mathbb P_0(\widehat\chi=1)+\mathbb P_1(\widehat\chi=0)\ge1.
\]
In particular, the full global event-horizon set cannot be recovered from those
data.

*Proof by an explicit completion pair.* Use ingoing spherical null coordinates and
compare Minkowski spacetime with a standard collapse completion of Vaidya type,

\[
ds^2=-\left(1-\frac{2m(v)}r\right)dv^2+2\,dv\,dr+r^2d\Omega^2,
\]

where \(m(v)=0\) for \(v\le v_0\), increases afterwards, and settles to a positive
mass. The two metrics agree exactly on the flat region \(v<v_0\). The Minkowski
completion has no event horizon. In the collapse completion the event horizon is an
outgoing null hypersurface whose generators extend backwards into that same flat
region before the infalling matter arrives; this standard teleological behaviour is
reviewed, including collapse examples found by tracing the horizon backwards, in
[20, §2.1]. Choose a sufficiently small diamond \(W\) around a point of this precursor
segment. Strong causality supplies, in each completion, an arbitrarily small
causally convex neighbourhood of that point. Inside their common flat overlap,
where the metrics and local cones coincide, choose one still smaller Minkowski
causal diamond \(W\) whose closure lies in both neighbourhoods and in \(v<v_0\).
Any causal curve between points of \(W\) is confined to the corresponding larger
causally convex neighbourhood; there the common diamond is causally convex.
Thus the same \(W\) is causally convex in both full completions.

The restricted metric, volume measure, and causal relation on \(W\) are therefore
identical, so every sprinkling observable determined by \(W\) has the same law in
the two models. Yet \(\chi_{\mathrm{EH}}=0\) in Minkowski and
\(\chi_{\mathrm{EH}}=1\) in the collapse completion. If
\(a:=\mathbb P_0(\widehat\chi=1)=\mathbb P_1(\widehat\chi=1)\), equality of the data
laws gives
\(\mathbb P_0(\widehat\chi=1)+\mathbb P_1(\widehat\chi=0)=a+(1-a)=1\).
This proves the displayed bound and the claimed obstruction. \(\blacksquare\)

#### What Theorem 3.2 does not say

1. It does **not** prohibit *quasi-local* proxies (trapped surfaces, expansion of
   null congruences, singularity-truncation cuts inside a frozen singular family).
   Those targets require separate definitions and analyses.
2. It does **not** assert that black-hole physics is invisible to causal sets. It
   asserts only that the **global event horizon**, as a set defined by the full
   spacetime, is the wrong target for a finite-patch experiment.
3. Empirical failure of particular quasi-local constructions (C1–C6) is
   **not** invoked and is **not** a substitute for this argument.

Figure 4 gives a finite order-theoretic analogy for this dependence on a completion;
its maximal-element property is not a surrogate definition of the event horizon.

![**Toy order-theoretic analogy for teleology.** The blue induced
subposet is identical in all panels, while continuations outside it change a global
maximality property. Maximality of the orange element is not the event horizon; the
diagram only illustrates why common finite-patch data cannot determine a
completion-dependent target.](../viz/output/fig04_teleology.png){width=100%}

\clearpage

### 3.3 Localization floor in a regular one-parameter family (1+1)

The dilation orbit of Theorem 3.1 kills absolute scale only when parameter and patch
are co-scaled. Here the Eddington--Finkelstein corners are held fixed, so varying
\(\tau\) changes dimensionless patch shape. Two natural designs fail regularity or
information content; a third family is regular and admits matching lower and upper
rates.

#### 3.3.1 Why fixed corners are needed

**Proposition 3.3 (Kruskal box degeneracy).**
On a *fixed* Kruskal coordinate box, the normalized volume measure of 1+1
Schwarzschild is independent of mass: with \(x=r/(2M)\), the relation
\(UV=(1-x)e^{x}\) is mass-independent and the conformal factor contributes only a
global \(16M^2\), which cancels upon normalization. Hence the copula, the poset law
at every \(n\), and the Fisher information in the mass parameter are **identically
trivial** (\(I\equiv 0\)).

*Proof.* In dimensionless Kruskal coordinates both the coordinate domain and causal
order are independent of \(M\), while the volume density is multiplied everywhere
by the same factor \(16M^2\). Conditioning on \(N=n\) cancels that factor. The
normalized point law and hence every induced poset law are therefore constant in
\(M\). \(\blacksquare\)

**Observation 3.4 (a fixed EF rectangle does not supply the regular experiment
below).** On a fixed Eddington--Finkelstein rectangle the volume density \(dv\,dr\)
is parameter-independent, but the causal-order map varies with \(\tau\). After
passing to parameter-dependent global null coordinates to make the order map common,
the image of the rectangle has moving support. Thus this design does not meet the
fixed-domain smooth-density hypotheses used for the Fisher argument below. This
follows directly from the EF metric and the \(\tau\)-dependent null transformation
displayed in §3.3.2; it is a design diagnostic, not a claim that no other analysis
of the rectangle is possible.

#### 3.3.2 The diamond family with fixed EF corners

**Construction.** Fix \(0<r_q<\tau_0\le\tau_1<r_p\) and \(v_p<v_q\). For each
\(\tau\in[\tau_0,\tau_1]\) let
\[
D_\tau
:=
J^+_\tau(z_{\mathrm{out}})\cap J^-_\tau(z_{\mathrm{in}}),
\qquad
z_{\mathrm{out}}=(v_p,r_p),\quad z_{\mathrm{in}}=(v_q,r_q)
\]
in the ingoing EF chart of 1+1 Schwarzschild of horizon radius \(\tau\). Fix once
and for all an open interval \(\Theta_{\mathrm{ext}}\) with
\([\tau_0,\tau_1]\subset\Theta_{\mathrm{ext}}\) and
\(\overline{\Theta_{\mathrm{ext}}}\subset(r_q,r_p)\); nothing below uses more than
\(r_q<\tau<r_p\), so every statement of this subsection holds verbatim for
\(\tau\in\Theta_{\mathrm{ext}}\), with all constants uniform on compact subsets of
\(\Theta_{\mathrm{ext}}\). (The enlargement is free and is what
lets Proposition 3.6 quote a criterion stated on an open parameter set.)

**Null coordinates and the product order.** Put

\[
\omega_\tau(r):=e^{r/\tau}\bigl(r/\tau-1\bigr),
\qquad
\omega_\tau'(r)=\frac{r\,e^{r/\tau}}{\tau^{2}}>0,
\]

a smooth strictly increasing bijection \((0,\infty)\to(-1,\infty)\) with
\(\omega_\tau(\tau)=0\), and define on \(r>0\)

\[
\tilde U:=-e^{-v/(2\tau)}\,\omega_\tau(r).
\]

Outgoing null curves of \(g_\tau\) satisfy \(dr=\tfrac12(1-\tau/r)\,dv\). Along an
arbitrary curve,
\(d\tilde U=e^{-v/(2\tau)}\bigl[\omega_\tau(r)\,dv/(2\tau)-\omega_\tau'(r)\,dr\bigr]\),
while

\[
\omega_\tau'(r)\cdot\frac{1-\tau/r}{2}
=
\frac{r\,e^{r/\tau}}{\tau^{2}}\cdot\frac{r-\tau}{2r}
=
\frac{e^{r/\tau}(r/\tau-1)}{2\tau}
=
\frac{\omega_\tau(r)}{2\tau},
\]

so substituting \(dr=\tfrac12(1-\tau/r)\,dv\) gives \(d\tilde U=0\) **exactly**:
\(\tilde U\) is constant on outgoing null rays, with no approximation and no
near-horizon restriction. Along future-directed ingoing null curves (\(dv=0\),
\(dr<0\)) one has \(d\tilde U=-e^{-v/(2\tau)}\omega_\tau'(r)\,dr>0\). Hence
\((\tilde U,v)\) is a global double-null chart on \(r>0\), smooth across the horizon
\(r=\tau\) (which is the ray \(\tilde U=0\)), both coordinates are non-decreasing
along future-directed causal curves and strictly increasing along the two null
directions, and the causal order is **exactly** the product order:

\[
x\preceq y
\quad\Longleftrightarrow\quad
\tilde U_x\le\tilde U_y
\ \ \text{and}\ \
v_x\le v_y .
\]

**The diamond is the corresponding null box.** For
\(\tau\in\Theta_{\mathrm{ext}}\) we have
\(r_q<\tau<r_p\), hence \(\omega_\tau(r_q)<0<\omega_\tau(r_p)\) and therefore
\(\tilde U_p(\tau)<0<\tilde U_q(\tau)\), where
\(\tilde U_p(\tau):=\tilde U(z_{\mathrm{out}})\) and
\(\tilde U_q(\tau):=\tilde U(z_{\mathrm{in}})\); with \(v_p<v_q\) this gives
\(z_{\mathrm{in}}\in J^+_\tau(z_{\mathrm{out}})\) for every
\(\tau\in\Theta_{\mathrm{ext}}\). By the product order,

\[
D_\tau=[\tilde U_p(\tau),\,\tilde U_q(\tau)]\times[v_p,v_q],
\]

a nonempty coordinate box straddling the horizon \(\tilde U=0\). Write

\[
r_\tau(\tilde U,v):=\omega_\tau^{-1}\bigl(-e^{v/(2\tau)}\tilde U\bigr)
\]

for the areal radius in the chart; \(r_\tau\) is strictly decreasing in
\(\tilde U\). Its minimum over the closed box is attained at the corner
\(z_{\mathrm{in}}\) and
equals \(r_q\); its maximum is attained at \((\tilde U_p(\tau),v_q)\) and equals
\(r_+(\tau)=\omega_\tau^{-1}\bigl(e^{(v_q-v_p)/(2\tau)}\omega_\tau(r_p)\bigr)\),
continuous in \(\tau\). Consequently, for every compact
\(\Theta'\subset\Theta_{\mathrm{ext}}\), with
\(r_{\max}:=\max_{\tau\in\Theta'}r_+(\tau)<\infty\),

\[
r_\tau(\tilde U,v)\in[r_q,r_{\max}]\subset(0,\infty)
\qquad\text{for all }(\tilde U,v)\in D_\tau,\ \tau\in\Theta' :
\]

the radial parameter is confined to a **compact interval that does not depend on
\(\tau\)** and is bounded away from \(0\) and \(\infty\). The singularity is avoided
automatically, and \(\omega_\tau'(r)=r\,e^{r/\tau}/\tau^2\) is bounded above and
below by positive constants on that range, uniformly in \(\tau\in\Theta'\).

**Sampling density, normalization and marginals.** Since \(\det g_\tau=-1\), the
volume measure is \(dv\,dr\) and, by Lemma 2.1, the fixed-\(n\) sample is i.i.d.\
uniform on \(D_\tau\) in the \((v,r)\) chart. Differentiating
\(\omega_\tau(r)=-e^{v/(2\tau)}\tilde U\) at fixed \(v\) gives
\(\partial r/\partial\tilde U=-e^{v/(2\tau)}/\omega_\tau'(r)\), so
\(dv\,dr=\bigl(e^{v/(2\tau)}/\omega_\tau'(r_\tau(\tilde U,v))\bigr)\,d\tilde U\,dv\)
and the normalized sampling density on the null box is

\[
\pi_\tau(\tilde U,v)
=
\frac{e^{v/(2\tau)}}{\mathcal V(\tau)\,\omega_\tau'\bigl(r_\tau(\tilde U,v)\bigr)}
=
\frac{\tau^{2}\,e^{v/(2\tau)}}{\mathcal V(\tau)\;r\,e^{r/\tau}}\bigg|_{\,r=r_\tau(\tilde U,v)},
\]

normalized by the \(g_\tau\)-area of the diamond,

\[
\mathcal V(\tau)
:=
\operatorname{vol}_{g_\tau}(D_\tau)
=
\int_{v_p}^{v_q}\!\!\int_{\tilde U_p(\tau)}^{\tilde U_q(\tau)}
\frac{e^{v/(2\tau)}}{\omega_\tau'\bigl(r_\tau(\tilde U,v)\bigr)}\,d\tilde U\,dv
\;\in(0,\infty),
\]

which is the same \(\mathcal V(\tau)\) used in Theorem 3.9. The two marginals of
\(\pi_\tau\) on the box are

\[
\pi_1(\tilde U;\tau):=\int_{v_p}^{v_q}\pi_\tau(\tilde U,v)\,dv,
\qquad
\pi_2(v;\tau):=\int_{\tilde U_p(\tau)}^{\tilde U_q(\tau)}\pi_\tau(\tilde U,v)\,d\tilde U .
\]

**Distribution functions and quantiles.** Define

\[
\mathsf F_\tau(\tilde U):=\int_{\tilde U_p(\tau)}^{\tilde U}\pi_1(s;\tau)\,ds,
\qquad
\mathsf G_\tau(v):=\int_{v_p}^{v}\pi_2(s;\tau)\,ds,
\]

the marginal distribution functions of \(\pi_\tau\) on the box, and let
\(\mathsf F_\tau^{-1},\mathsf G_\tau^{-1}:[0,1]\to\) (the respective edges of the box) be the
marginal quantile maps. Their regularity is item (iv) of the next lemma.

**Lemma 3.5 (regularity).**
Let \(\Theta'\subset\Theta_{\mathrm{ext}}\) be compact. Uniformly in
\(\tau\in\Theta'\):

(i) \(r_\tau(\tilde U,v)\) is jointly smooth in \((\tilde U,v,\tau)\) on the closed
box, and \(|\partial r/\partial\tilde U|\) is bounded above and below by positive
constants;

(ii) \(\pi_\tau\) is jointly smooth in \((\tilde U,v,\tau)\) and bounded above and
below by positive constants;

(iii) the marginals \(\pi_1(\cdot\,;\tau)\) and \(\pi_2(\cdot\,;\tau)\) are smooth
in all arguments and bounded above and below by positive constants;

(iv) \(\mathsf F_\tau\) and \(\mathsf G_\tau\) are \(C^1\) strictly increasing bijections onto
\([0,1]\) with derivatives bounded away from \(0\), and the quantile maps
\((x,\tau)\mapsto \mathsf F_\tau^{-1}(x)\) and
\((y,\tau)\mapsto \mathsf G_\tau^{-1}(y)\) are
\(C^1\);

(v) consequently the copula density

\[
c_\tau(x,y)
=
\frac{\pi_\tau\bigl(\mathsf F_\tau^{-1}(x),\,\mathsf G_\tau^{-1}(y)\bigr)}
     {\pi_1\bigl(\mathsf F_\tau^{-1}(x);\tau\bigr)\,
      \pi_2\bigl(\mathsf G_\tau^{-1}(y);\tau\bigr)},
\qquad (x,y)\in[0,1]^2,
\]

is jointly continuous, \(C^1\) in \(\tau\) with \(\partial_\tau c_\tau\) jointly
continuous, bounded above and below by positive constants, and
\(|\partial_\tau c_\tau|\) is bounded; in particular the score
\(\partial_\tau\log c_\tau\) is bounded uniformly on
\([0,1]^2\times\Theta'\).

*Proof.* Write \(\sigma_\tau(\tilde U,v):=e^{v/(2\tau)}/\omega_\tau'\bigl(r_\tau(\tilde
U,v)\bigr)\) for the unnormalized density, so
\(\pi_\tau=\sigma_\tau/\mathcal V(\tau)\).

*Preliminary: a fixed open domain.* The defining relation
\(\omega_\tau(r)=-e^{v/(2\tau)}\tilde U\) has a (unique) solution \(r>0\) exactly
when \(-e^{v/(2\tau)}\tilde U>-1\), because \(\omega_\tau\) is an increasing
bijection \((0,\infty)\to(-1,\infty)\). Hence \(r_\tau\) and \(\sigma_\tau\) are
defined and smooth on the **open** set

\[
\mathcal O:=\bigl\{(\tilde U,v,\tau)\in\mathbb R^3:\ \tau>0,\ e^{v/(2\tau)}\tilde U<1\bigr\},
\]

which contains the compact set
\(\mathcal C_{\Theta'}:=\{(\tilde U,v,\tau):\tau\in\Theta',\,
(\tilde U,v)\in D_\tau\}\) (on the box
the corresponding radius satisfies \(r\ge r_q>0\), so the inequality is strict).
Every differentiation below is performed on \(\mathcal O\); in particular
\(\tau\mapsto\sigma_\tau(\tilde U,v)\) may be differentiated **at fixed
\((\tilde U,v)\)**, including at points that leave the moving box \(D_\tau\). Since
\(\mathcal C_{\Theta'}\subset\mathcal O\) is compact, it has a compact neighbourhood
\(\mathcal C_{\Theta'}^+\subset\mathcal O\), and each two-sided bound below is the
statement that a continuous non-vanishing function is pinched on
\(\mathcal C_{\Theta'}^+\).

(i) On \(\mathcal O\) the relation \(\omega_\tau(r)+e^{v/(2\tau)}\tilde U=0\) has
\(r\)-derivative \(\omega_\tau'(r)\), pinched between positive constants on the
uniform compact radial range \([r_q,r_{\max}]\) established above; the implicit function
theorem with smooth data gives joint smoothness of \(r_\tau\) and
\(\partial r/\partial\tilde U=-e^{v/(2\tau)}/\omega_\tau'(r)\), whose modulus is
pinched because \(v\) runs over the compact \([v_p,v_q]\).

(ii) By (i), \(\sigma_\tau\) is smooth on \(\mathcal O\) and pinched between positive
constants on \(\mathcal C_{\Theta'}^+\). The normalizer has **fixed** limits in \(v\) and
**moving** limits in \(\tilde U\); the Leibniz rule for variable limits (smooth
integrand on \(\mathcal O\), edges \(\tilde U_p(\tau),\tilde U_q(\tau)\) explicit
smooth functions of \(\tau\)) gives that \(\mathcal V\) is smooth with

\[
\mathcal V'(\tau)=\int_{v_p}^{v_q}\Bigl[
\tilde U_q'(\tau)\,\sigma_\tau\bigl(\tilde U_q(\tau),v\bigr)
-\tilde U_p'(\tau)\,\sigma_\tau\bigl(\tilde U_p(\tau),v\bigr)
+\int_{\tilde U_p(\tau)}^{\tilde U_q(\tau)}\partial_\tau\sigma_\tau\,d\tilde U
\Bigr]dv .
\]

Moreover \(0<\mathcal V(\tau)<\infty\) with both bounds uniform on \(\Theta'\), since
\(\sigma_\tau\) is pinched and the box has edge lengths \(v_q-v_p>0\) (fixed) and
\(\tilde U_q(\tau)-\tilde U_p(\tau)\), continuous and strictly positive on the
compact \(\Theta'\), hence pinched. Therefore
\(\pi_\tau=\sigma_\tau/\mathcal V(\tau)\) is smooth on \(\mathcal O\) and pinched
on \(\mathcal C_{\Theta'}^+\).

(iii) The two marginals are of different types and must be treated separately.
\(\pi_1(\tilde U;\tau)=\int_{v_p}^{v_q}\pi_\tau\,dv\) has **fixed** limits: ordinary
differentiation under the integral sign (smooth integrand, compact fixed interval)
gives joint smoothness in \((\tilde U,\tau)\), with no boundary terms.
\(\pi_2(v;\tau)=\int_{\tilde U_p(\tau)}^{\tilde U_q(\tau)}\pi_\tau\,d\tilde U\) has
**moving** limits: the same Leibniz rule as in (ii) gives joint smoothness in
\((v,\tau)\), with the two boundary terms
\(\tilde U_q'(\tau)\pi_\tau(\tilde U_q(\tau),v)-\tilde U_p'(\tau)\pi_\tau(\tilde
U_p(\tau),v)\). In both cases the two-sided bounds are the pinching of \(\pi_\tau\)
multiplied by the corresponding interval length, itself pinched by (ii).

(iv) \(\mathsf G_\tau(v)=\int_{v_p}^{v}\pi_2\,ds\) has a fixed lower limit;
\(\mathsf F_\tau(\tilde U)=\int_{\tilde U_p(\tau)}^{\tilde U}\pi_1\,ds\) has a
**moving** lower limit and
therefore acquires the boundary term \(-\tilde U_p'(\tau)\,\pi_1(\tilde
U_p(\tau);\tau)\) on differentiating in \(\tau\); both are jointly \(C^1\), and
\(\mathsf F_\tau(\tilde U_q(\tau))=\mathsf G_\tau(v_q)=1\) by normalization, so
each is a strictly increasing bijection onto \([0,1]\) with
\(\mathsf F_\tau'=\pi_1>0\) and \(\mathsf G_\tau'=\pi_2>0\)
bounded away from \(0\) by (iii). The implicit function theorem applied to
\(\mathsf F_\tau(\tilde U)-x=0\) and \(\mathsf G_\tau(v)-y=0\) then gives joint
\(C^1\) dependence of
the inverses on \((x,\tau)\) and \((y,\tau)\), one-sided in \(x,y\) at the endpoints
\(0,1\) (where the inverses return the box edges).

(v) Compose (ii)–(iv): the quotient has smooth numerator and denominator bounded
away from \(0\); each factor is \(C^1\) in \(\tau\) with jointly continuous
\(\tau\)-derivative, so \(\partial_\tau c_\tau\) is jointly continuous on the
compact \([0,1]^2\times\Theta'\) and hence bounded there; all bounds are uniform because
every ingredient is pinched on compact domains. Boundedness of the score follows
from \(|\partial_\tau\log c_\tau|\le|\partial_\tau c_\tau|/c_{\min}\).
\(\blacksquare\)

**Proposition 3.6 (QMD and finite Fisher).**
The Fisher information
\(I(\tau)=\int_{[0,1]^2}(\partial_\tau\log c_\tau)^2\,c_\tau\) is finite and
continuous on \([\tau_0,\tau_1]\); set \(\bar I:=\sup I(\tau)<\infty\). The family
is differentiable in quadratic mean, and, writing \(\Theta_\delta\) for the closed
interval with endpoints \(\tau\) and \(\tau+\delta\),

\[
H^2(c_\tau,c_{\tau+\delta})
\;\le\;
|\delta|\int_{\Theta_\delta}\frac{I(s)}{4}\,ds
\;\le\;
\frac{\delta^2}{4}\,\bar I.
\]

*Proof.* **Finiteness and continuity of \(I\).** By Lemma 3.5(v) the integrand
\((\partial_\tau\log c_\tau)^2c_\tau\) is bounded uniformly on
\([0,1]^2\times[\tau_0,\tau_1]\) and, for each \((x,y)\), continuous in \(\tau\).
The unit square carries finite Lebesgue measure, so dominated convergence gives
both finiteness of \(I(\tau)\) and continuity of \(I\) on \([\tau_0,\tau_1]\);
compactness then gives \(\bar I=\sup I=\max I<\infty\) — the supremum is attained,
and in particular finite.

**Integrated bound.** Since \(c_\tau\ge c_{\min}>0\) and \(c_\tau\) is \(C^1\) in
\(\tau\) (Lemma 3.5(v)), \(\sqrt{c_\tau}\) is \(C^1\) in \(\tau\) with
\(\partial_\tau\sqrt{c_\tau}=\partial_\tau c_\tau/(2\sqrt{c_\tau})\) bounded, and

\[
\int_{[0,1]^2}\bigl(\partial_s\sqrt{c_s}\bigr)^2
=
\frac14\int_{[0,1]^2}\frac{(\partial_s c_s)^2}{c_s}
=
\frac{I(s)}{4}.
\]

Taking \(\delta>0\) (the case \(\delta<0\) is identical with the endpoints
exchanged), the fundamental theorem of calculus and Cauchy–Schwarz along the
parameter path give, pointwise in \((x,y)\),

\[
\bigl(\sqrt{c_{\tau+\delta}}-\sqrt{c_\tau}\bigr)^2
=
\Bigl(\int_\tau^{\tau+\delta}\partial_s\sqrt{c_s}\,ds\Bigr)^{\!2}
\le
\delta\int_\tau^{\tau+\delta}\bigl(\partial_s\sqrt{c_s}\bigr)^2 ds ;
\]

integrating over \([0,1]^2\) and applying Fubini (the integrand is bounded on a
finite-measure product) yields the displayed bound. No expansion in \(\delta\) is
used, so the bound holds for **every** admissible \(\delta\), not only
asymptotically; \(\bar I<\infty\) is exactly what makes it uniform over the
parameter interval.

**QMD.** Choose a compact
\(\Theta'\subset\Theta_{\mathrm{ext}}\) whose interior contains \(\Theta\). In
copula coordinates the family lives on a **fixed** domain: every
\(c_\tau\) is a probability density on the same unit square with respect to
Lebesgue measure, the \(\tau\)-dependent box edges having been absorbed by the
quantile transforms of Lemma 3.5(iv). In this compact, smooth, fixed-domain
setting the definition of quadratic-mean differentiability can be verified
directly. By Lemma 3.5(v), \(c_\tau\ge c_{\min}>0\) and \(\partial_\tau c_\tau\) is
jointly continuous, so

\[
(z,\tau)\longmapsto\partial_\tau\sqrt{c_\tau(z)}
=\frac{\partial_\tau c_\tau(z)}{2\sqrt{c_\tau(z)}}
=\tfrac12\bigl(\partial_\tau\log c_\tau(z)\bigr)\sqrt{c_\tau(z)}
\]

is continuous on the compact \([0,1]^2\times\Theta'\), hence bounded and
**uniformly** continuous there. Fix \(\tau\in[\tau_0,\tau_1]\), which is interior
to \(\Theta_{\mathrm{ext}}\), and put

\[
G_\delta(z)
:=\sqrt{c_{\tau+\delta}(z)}-\sqrt{c_\tau(z)}-\delta\,\partial_\tau\sqrt{c_\tau(z)}
=\int_0^\delta\Bigl[\partial_s\sqrt{c_s(z)}\big|_{s=\tau+u}-\partial_\tau\sqrt{c_\tau(z)}\Bigr]du .
\]

Uniform continuity gives \(\sup_z|G_\delta(z)|\le|\delta|\,\varepsilon(\delta)\) with
\(\varepsilon(\delta)\to0\) as \(\delta\to0\), so \(\int_{[0,1]^2}G_\delta^2=o(\delta^2)\):
the family is differentiable in quadratic mean at \(\tau\), with \(L^2\)-derivative
\(\partial_\tau\sqrt{c_\tau}\) and score \(\partial_\tau\log c_\tau\). Expanding
\(H^2(c_\tau,c_{\tau+\delta})=\int(\delta\,\partial_\tau\sqrt{c_\tau}+G_\delta)^2\)
and bounding the cross term by Cauchy–Schwarz yields the local form
\(H^2(c_\tau,c_{\tau+\delta})=(\delta^2/4)I(\tau)+o(\delta^2)\), since
\(\int(\partial_\tau\sqrt{c_\tau})^2=I(\tau)/4\). \(\blacksquare\)

The hypotheses above also match the standard sufficient criterion for QMD. The
direct proof is included because the lower bound in Theorem 3.8 needs only the
non-asymptotic integrated inequality, not the local expansion.

**Remark 3.7 (no exact re-identification in the matched-rate regime).** For
\(0<\Delta v<\Delta v_0\), Theorem 3.9 proves that \(p(\tau)\) is strictly
increasing. Since comparable-pair probability is a functional of \(c_\tau\), this
immediately implies \(c_\tau\ne c_{\tau'}\) and already separates the two-point
poset laws whenever \(\tau\ne\tau'\). No broader no-re-identification claim is
needed for the minimax theorem.

#### Theorem 3.8 (order-only two-point localization floor)

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
   Thus the minimax localization radius is bounded below at order
   \(1/\sqrt{n\bar I}\). The matching upper rate is proved in Theorem 3.9 and
   Corollary 3.10 for fixed sufficiently small \(\Delta v\).

*Proof.*  
**(1).** By Lemma 2.1 the \(n\) points are i.i.d.\ from the normalized volume
measure on \(D_\tau\). By §3.3.2, \(D_\tau\) is a coordinate box in the global
double-null chart \((\tilde U,v)\), in which the causal order is exactly the product
order, so Lemma 2.2 applies: the fixed-\(n\) unlabeled poset law depends on
\(g_\tau\) only through the copula \(c_\tau\). Concretely, the coordinatewise
quantile transform
\((\tilde U,v)\mapsto(\mathsf F_\tau(\tilde U),\mathsf G_\tau(v))\) is increasing
in each coordinate, hence order-preserving, and carries the sample to \(n\)
i.i.d.\ points of \([0,1]^2\) with density \(c_\tau\); the induced map \(\Phi\)
from \(n\) unit-square points to the unlabeled poset is *the same* measurable map
for every \(\tau\), all of the \(\tau\)-dependence having been moved into
\(c_\tau\). Proposition 3.6 gives
\(H^2(c_\tau,c_{\tau+\delta})\le\delta^2\bar I/4\); the tensorization corollary of
§2.3 gives
\(H^2\bigl(c_\tau^{\otimes n},c_{\tau+\delta}^{\otimes n}\bigr)\le n\delta^2\bar
I/4\); and data processing under \(\Phi\) together with \(\mathrm{TV}\le H\) gives

\[
\mathrm{TV}\bigl(Q^n_\tau,Q^n_{\tau+\delta}\bigr)
\;\le\;
H\bigl(c_\tau^{\otimes n},c_{\tau+\delta}^{\otimes n}\bigr)
\;\le\;
\frac{|\delta|}{2}\sqrt{n\bar I}.
\]

**(2).** Put \(E:=\{|\widehat\tau-\tau|<|\delta|/2\}\). On \(E\) the triangle
inequality gives \(|\widehat\tau-(\tau+\delta)|\ge|\delta|-|\widehat\tau-\tau|>
|\delta|/2\), so \(E\subseteq\{|\widehat\tau-(\tau+\delta)|\ge|\delta|/2\}\), while
\(E^c=\{|\widehat\tau-\tau|\ge|\delta|/2\}\). Hence

\[
\mathbb{P}_\tau\bigl(|\widehat\tau-\tau|\ge|\delta|/2\bigr)
+
\mathbb{P}_{\tau+\delta}\bigl(|\widehat\tau-(\tau+\delta)|\ge|\delta|/2\bigr)
\;\ge\;
1-\bigl[\mathbb{P}_\tau(E)-\mathbb{P}_{\tau+\delta}(E)\bigr]
\;\ge\;
1-\mathrm{TV}\bigl(Q^n_\tau,Q^n_{\tau+\delta}\bigr),
\]

by the definition of \(\mathrm{TV}\) as a supremum over events; now insert (1).
For randomized \(\widehat\tau=f(C_n,U)\) with \(U\) independent of the data, the
same computation runs on the product space, whose total variation is again
\(\mathrm{TV}(Q^n_\tau,Q^n_{\tau+\delta})\) because the extra factor is common to
both models.

**(3).** If some order-only procedure had both error probabilities at most
\(\varepsilon\), then by (2) \(2\varepsilon\ge1-(|\delta|/2)\sqrt{n\bar I}\), i.e.
\(|\delta|\ge2(1-2\varepsilon)/\sqrt{n\bar I}\). The contrapositive is (3), with the
inequality strict as stated. \(\blacksquare\)

(The two-point testing inequality and the data-processing / \(\mathrm{TV}\le H\)
steps are standard; see §2.3 and [10].)

#### Theorem 3.9 (estimation by the comparable-pair fraction)

Retain the diamond family above and put \(\Delta v:=v_q-v_p>0\) and
\(\Theta:=[\tau_0,\tau_1]\). Let \(p(\tau)\) be the probability that two independent
points drawn from normalized volume on \(D_\tau\) are causally comparable, and let
\(S_n\) be the number of comparable unordered pairs in the observed unlabeled
poset. Thus \(\widehat p_n:=S_n/\binom n2\) is the classical ordering fraction.
Define

\[
\kappa(r_p,r_q)
:=
\frac{(r_p^2-r_q^2)-2r_pr_q\log(r_p/r_q)}
     {12r_pr_q(r_p-r_q)^2}
>0.
\]

There exists
\(\Delta v_0=\Delta v_0(r_p,r_q,\tau_0,\tau_1)>0\) such that, for every fixed
\(0<\Delta v<\Delta v_0\):

1. **Uniform mean separation on \(\Theta\).** The map \(\tau\mapsto p(\tau)\) is
   strictly increasing and, for all \(\tau,\tau'\in\Theta\),
   \[
   |p(\tau')-p(\tau)|
   \;\ge\;
   \frac{\kappa(r_p,r_q)\,\Delta v}{2}\,|\tau'-\tau|.
   \]
2. **Fixed-pair total-variation separation.** For every \(n\ge2\) and every
   fixed pair \(\tau\ne\tau'\) in \(\Theta\),
   \[
   \mathrm{TV}(Q^n_\tau,Q^n_{\tau'})
   \;\ge\;
   1-
   \frac{4(2n-3)}
        {n(n-1)|p(\tau')-p(\tau)|^2}
   \;\longrightarrow\;1.
   \]
   Thus the midpoint test based only on \(S_n\) is consistent for each fixed
   pair.
3. **Separated and moving alternatives.** The testing cardinality \(n_0\) is
   pair-dependent when distinct parameters may approach one another. It is uniform
   on sets satisfying \(|\tau'-\tau|\ge\eta>0\). More generally, for any sequences
   \(\tau_n,\tau_n'\in\Theta\) with
   \(\sqrt n\,|\tau_n'-\tau_n|\to\infty\), the same \(S_n\)-test has total error
   tending to zero. The displayed Chebyshev bound and item (1) make the dependence
   explicit: its threshold cardinality is of order
   \[
   n_0\asymp
   \frac{1}{\kappa(r_p,r_q)^2(\Delta v)^2|\tau'-\tau|^2},
   \]
   so it diverges as either the lapse or the pair separation tends to zero.
4. **Uniform plug-in estimation.** Let \(\Pi_{p(\Theta)}\) be projection onto the
   interval \(p(\Theta)\) and define
   \[
   \widehat\tau_n
   :=p^{-1}\!\left(\Pi_{p(\Theta)}(\widehat p_n)\right).
   \]
   Then
   \[
   \sup_{\tau\in\Theta}\mathbb E_\tau|\widehat\tau_n-\tau|
   \le
   \frac{2}{\kappa(r_p,r_q)\Delta v}
   \sqrt{\frac{2n-3}{2n(n-1)}}
   \le \frac{2}{\kappa(r_p,r_q)\Delta v\sqrt n},
   \]
   and
   \[
   \sup_{\tau\in\Theta}\mathbb E_\tau(\widehat\tau_n-\tau)^2
   \le
   \frac{4}{\kappa(r_p,r_q)^2(\Delta v)^2}
   \frac{2n-3}{2n(n-1)}.
   \]

*Proof.* Write \(r_{\mathrm{out}}:=r_p\), \(r_{\mathrm{in}}:=r_q\), and
\(h:=\Delta v\). Put
\(\omega_\tau(r):=e^{r/\tau}(r/\tau-1)\), a strictly increasing bijection
\((0,\infty)\to(-1,\infty)\) with \(\omega_\tau(\tau)=0\) and
\(\omega_\tau'(r)=r\,e^{r/\tau}/\tau^2>0\). Then
\(\tilde U:=-e^{-v/(2\tau)}\omega_\tau(r)\) is the exactly null coordinate of
§2.1, \((\tilde U,v)\) is a global double-null chart on \(r>0\), and the causal
order is the product order with **both coordinates increasing to the future**:
for \(x,y\in D_\tau\),
\[
x\prec y
\quad\Longleftrightarrow\quad
\tilde U_x\le\tilde U_y
\ \ \text{and}\ \
v_x\le v_y .
\]
At fixed \(v\), \(\tilde U\) is strictly decreasing in \(r\), and the horizon
\(r=\tau\) is the ray \(\tilde U=0\). Let \(\mathcal R_\tau(r_0,D)\) be the areal radius
at \(v=v_0+D\) of the outgoing null ray through \((v_0,r_0)\), i.e. the solution
of \(\omega_\tau(\mathcal R)=e^{D/(2\tau)}\omega_\tau(r_0)\); differentiating,
\[
\frac{\partial\mathcal R}{\partial D}=\frac{\mathcal R-\tau}{2\mathcal R},
\qquad
\mathcal R_\tau(r_0,0)=r_0 .
\]

**Reduction to a two-fold integral.** By §2.1, \(\det g_\tau=-1\), so
\(\mathrm{vol}_{g_\tau}=dv\,dr\) and the normalized sampling law on \(D_\tau\) is
absolutely continuous with respect to \(dv\,dr\) (indeed uniform). Consequently
the coincidence sets \(\{\tilde U_x=\tilde U_y\}\) and \(\{v_x=v_y\}\), and the
null boundaries of \(D_\tau\), all carry product measure zero, so two independent
points are a.s. untied and the trichotomy \(x\prec y\), \(y\prec x\), spacelike is
a.s. clean. Both sides of
\[
\int_{v_0}^{v_0+D}\mathcal R_\tau(r_0,v-v_0)\,dv
=\mathcal R_\tau(r_0,D)^2-r_0^2+\tau D
\]
vanish at \(D=0\) and have the same \(D\)-derivative by the ray flow, so they
agree. At fixed \(v\in[v_x,v_q]\), \(\tilde U\) is decreasing in \(r\), so the
slice of \(J^+(x)\cap J^-(z_{\mathrm{in}})\) is
\[
\left\{r:
\mathcal R_\tau(r_q,v-v_q)\le r\le
\mathcal R_\tau(r_x,v-v_x)
\right\},
\]
between the outgoing rays through \(z_{\mathrm{in}}\) and through \(x\), non-empty
precisely because
\(\tilde U_x\le\tilde U_q\); integrating and cancelling the two \(\tau D\) terms
gives, for \(x=(v_x,r_x)\in D_\tau\) and \(D:=v_q-v_x\),
\[
\operatorname{vol}\bigl(J^+(x)\cap D_\tau\bigr)
=\mathcal R_\tau(r_x,D)^2+\mathcal R_\tau(r_q,-D)^2-r_x^2-r_q^2 ,
\]
and in particular
\(\mathcal V(\tau)=\mathcal R_\tau(r_p,\Delta v)^2+
\mathcal R_\tau(r_q,-\Delta v)^2-r_p^2-r_q^2\). Points are
exchangeable and a.s. untied, and comparability in a product order means exactly
\(x\prec y\) or \(y\prec x\), so \(p=2\,\mathbb P(X\prec Y)\); Fubini then gives,
with \(\alpha(D):=\mathcal R_\tau(r_p,\Delta v-D)\) and
\(\beta(D):=\mathcal R_\tau(r_q,-D)\),
\[
p(\tau)=\frac{2}{\mathcal V(\tau)^2}\int_0^{\Delta v}\!\!\int_{\beta(D)}^{\alpha(D)}
\bigl[\mathcal R_\tau(r,D)^2+\beta(D)^2-r^2-r_q^2\bigr]\,dr\,dD .
\]

**Step 1 (one uniform analytic neighbourhood).** The flow is defined implicitly by
\(\mathfrak F(\tau,r,D,y):=\omega_\tau(y)-e^{D/(2\tau)}\omega_\tau(r)=0\), with
\(\partial_y\mathfrak F=\omega_\tau'(y)>0\) and \(y=r\) at \(D=0\). The real-analytic
implicit-function theorem makes \(\mathcal R_\tau\) jointly real-analytic in
\((\tau,r,D)\) near every \((\tau,r,0)\) with \(\tau,r>0\). A finite subcover of
the product of a compact \(\tau\)-interval slightly larger than \(\Theta\) (still
inside \((r_{\mathrm{in}},r_{\mathrm{out}})\)) with a compact positive
\(r\)-interval containing \([r_{\mathrm{in}},r_{\mathrm{out}}]\)
yields one \(\eta>0\) on which \(\mathcal R_\tau\) is jointly analytic for \(|D|<\eta\);
the local branches agree because \(\omega_\tau\) is strictly increasing.

**Step 2 (fixed square and analytic division).** For \(s,u\in[0,1]\) put
\[
r_+(s):=\mathcal R_\tau(r_{\mathrm{out}},(1-s)h),\qquad
r_-(s):=\mathcal R_\tau(r_{\mathrm{in}},-sh),\qquad
\xi:=r_-+u(r_+-r_-),
\]
and
\[
\mathcal H:=\mathcal R_\tau(\xi,sh)^2+r_-^2-\xi^2-r_{\mathrm{in}}^2.
\]
Since \(r_+-r_-=r_{\mathrm{out}}-r_{\mathrm{in}}>0\) at \(h=0\), one
uniform shrink of \(\eta\) keeps \(r_+>r_-\). The substitutions \(D=sh\) and
\(r=r_-+u(r_+-r_-)\)
turn the numerator of the display above into
\(\mathcal N(\tau,h)=h\int_0^1\!\!\int_0^1(r_+-r_-)\mathcal H\,du\,ds\).
At \(h=0\) one has \(\mathcal H=0\), so analytic division
\(\mathcal H=h\widehat{\mathcal H}\), with
\(\widehat{\mathcal H}=\int_0^1\partial_h\mathcal H(\tau,s,u,\lambda h)\,d\lambda\),
gives \(\mathcal N=h^2\widehat{\mathcal N}\) with
\(\widehat{\mathcal N}\) jointly analytic — compactness of the unit
square supplies one common analytic neighbourhood, so the local power series may
be integrated term by term. Likewise
\(\mathcal V(\tau,h)=h\widehat{\mathcal V}(\tau,h)\), with
\(\widehat{\mathcal V}(\tau,0)=r_{\mathrm{out}}-r_{\mathrm{in}}>0\) uniformly
in \(\tau\), since \(\mathcal V(\tau,0)=0\) and
\(\partial_h\mathcal V(\tau,0)=r_{\mathrm{out}}-r_{\mathrm{in}}\) by the ray flow.
After one further uniform shrink of \(\eta\), \(\widehat{\mathcal V}\) has no zero
near \(\Theta\times\{0\}\), so
\(\mathfrak p(\tau,h):=
2\widehat{\mathcal N}(\tau,h)/\widehat{\mathcal V}(\tau,h)^2\)
is a jointly real-analytic extension through \(h=0\) of \(p(\tau)\) for \(h>0\).

**Step 3 (first two coefficients).** Expanding the flow from its ODE,
\(\mathcal R_\tau(r,D)=r+D\,(r-\tau)/(2r)+D^2\tau(r-\tau)/(8r^3)+O(D^3)\), substituting
and integrating the retained coefficients (antiderivatives \(r(r-2\tau)/2\) and
\(r/4-\tau\log r/4\)) gives
\(\widehat{\mathcal N}(\tau,0)=(r_{\mathrm{out}}-r_{\mathrm{in}})^2/4\),
\(\widehat{\mathcal V}(\tau,0)=r_{\mathrm{out}}-r_{\mathrm{in}}\), hence
\(\mathfrak p(\tau,0)=1/2\) and
\(\partial_h\mathfrak p(\tau,0)=\kappa(r_p,r_q)\,\tau\). Writing
\[
p(\tau)
=
\frac12+\kappa(r_p,r_q)\tau\,\Delta v+\mathcal E(\tau,\Delta v)
\]
defines the remainder \(\mathcal E\).

**Step 4 (uniform remainder).** Choose \(0<\varepsilon<\eta\) with
\(\Theta\times[-\varepsilon,\varepsilon]\) inside the analytic domain of
\(\mathfrak p\) and set
\(C_1:=\tfrac12\max_{\Theta\times[-\varepsilon,\varepsilon]}
|\partial_\tau\partial_h^2\mathfrak p|\), finite by compactness and depending only on
\((r_p,r_q,\tau_0,\tau_1)\). Taylor's formula with integral remainder gives, for
\(0\le\Delta v\le\varepsilon\),
\[
\partial_\tau \mathcal E(\tau,\Delta v)
=
(\Delta v)^2\int_0^1(1-z)\,
\partial_\tau\partial_h^2\mathfrak p(\tau,z\Delta v)\,dz ,
\qquad
|\partial_\tau \mathcal E(\tau,\Delta v)|\le C_1(\Delta v)^2
\]
uniformly for \(\tau\in\Theta\).

**Positivity of \(\kappa\) and choice of \(\Delta v_0\).** With \(x:=r_p/r_q>1\) the
numerator of \(\kappa\) is \(2r_pr_q\varphi(x)\), where
\(\varphi(x):=(x-1/x)/2-\log x\); since \(\varphi(1)=0\) and
\(\varphi'(x)=(x-1)^2/(2x^2)>0\) for \(x\ne1\), \(\varphi>0\) on \((1,\infty)\)
and \(\kappa>0\). Step 4 then gives
\(\partial_\tau p(\tau)\ge\kappa\Delta v-C_1(\Delta v)^2\) on \(\Theta\). Take
\[
\Delta v_0:=
\begin{cases}
\varepsilon, & C_1=0,\\
\min\{\varepsilon,\ \kappa/(2C_1)\}, & C_1>0;
\end{cases}
\]
then \(\partial_\tau p\ge\kappa\Delta v/2>0\) throughout \(\Theta\) for every
\(0<\Delta v<\Delta v_0\), which is (1). The bound on \(\mathcal E\) alone would give
separation only for each pre-fixed pair; the derivative bound is what makes one
\(\Delta v_0\) serve the whole interval.

For the symmetric Bernoulli kernel
\(f(x,y)=\mathbf 1\{x,y\text{ comparable}\}\), the exact fixed-\(n\)
Hoeffding identity is
\[
\operatorname{Var}_\tau(S_n)
=
\binom n2\{2(n-2)\zeta_{1,\tau}+\zeta_{2,\tau}\}.
\]
Here
\(\zeta_{1,\tau}:=\operatorname{Var}_\tau(
\mathbb E_\tau[f(X,Y)\mid X])\) and
\(\zeta_{2,\tau}:=\operatorname{Var}_\tau(f(X,Y))\). Since both variables inside
these variances take values in \([0,1]\),
\(\zeta_{1,\tau},\zeta_{2,\tau}\le1/4\), and hence
\[
\operatorname{Var}_\tau(S_n)
\le
\binom n2\frac{2n-3}{4}.
\]
The two means differ by
\(\Delta_m=\binom n2|p(\tau')-p(\tau)|\). Chebyshev's inequality at their midpoint
bounds the sum of the two testing errors by
\[
\frac{4\{\operatorname{Var}_\tau(S_n)+
          \operatorname{Var}_{\tau'}(S_n)\}}{\Delta_m^2}
\le
\frac{4(2n-3)}
     {n(n-1)|p(\tau')-p(\tau)|^2}.
\]
For any test, total variation is at least one minus its total error; data
processing is legitimate because \(S_n\) is a function of the unlabeled poset.
This proves (2), and combining it with (1) gives (3). In particular, the testing
bound becomes informative once
\(n(\Delta v)^2|\tau'-\tau|^2\) is large; its required cardinality therefore grows
as \(((\Delta v)|\tau'-\tau|)^{-2}\) up to fixed geometric constants.

For (4), the same variance bound gives
\[
\operatorname{Var}_\tau(\widehat p_n)
\le
\frac{2n-3}{4\binom n2}
=
\frac{2n-3}{2n(n-1)}.
\]
Moreover \(\widehat p_n\) is unbiased for \(p(\tau)\). Item (1) says that the
inverse of \(p\) on \(p(\Theta)\) is Lipschitz with constant
\(2/(\kappa\Delta v)\), while interval projection cannot increase distance from
\(p(\tau)\). Hence
\[
|\widehat\tau_n-\tau|
\le
\frac{2}{\kappa\Delta v}|\widehat p_n-p(\tau)|.
\]
Taking second moments proves the squared-risk bound, and Cauchy--Schwarz proves
the absolute-risk bound. \(\blacksquare\)

#### Corollary 3.10 (Fisher positivity and the minimax rate)

Fix \(0<\Delta v<\Delta v_0\). Then, for every \(\tau\in\Theta\),

\[
I(\tau)
\ge 2p'(\tau)^2
\ge \frac{\kappa(r_p,r_q)^2(\Delta v)^2}{2}>0.
\]

Let
\[
\mathcal R_{n,1}
:=
\inf_{\widetilde\tau}
\sup_{\tau\in\Theta}
\mathbb E_\tau|\widetilde\tau-\tau|
\]
be minimax absolute-error risk over all possibly randomized functions of the
unlabeled poset. For all sufficiently large \(n\),

\[
\frac{1}{8\sqrt{n\bar I}}
\le
\mathcal R_{n,1}
\le
\frac{2}{\kappa(r_p,r_q)\Delta v\sqrt n}.
\]

Thus the minimax rate is \(n^{-1/2}\) for every fixed admissible lapse. Equivalently,
the two laws merge when \(|\delta_n|=o(n^{-1/2})\), whereas the ordering-fraction
procedure separates them when \(|\delta_n|=\omega(n^{-1/2})\). No claim is made
about the optimal constant at \(|\delta_n|\asymp n^{-1/2}\).

*Proof.* Let \(Z_1,Z_2\) be independent with density \(c_\tau\), let
\(f(Z_1,Z_2)\) indicate comparability, and write
\(s_\tau=\partial_\tau\log c_\tau\). Differentiation under the integral is
justified by Lemma 3.5, and the score has mean zero. Hence
\[
p'(\tau)
=
\operatorname{Cov}_\tau\!\left(
f(Z_1,Z_2),s_\tau(Z_1)+s_\tau(Z_2)
\right).
\]
The pair score has variance \(2I(\tau)\), while
\(\operatorname{Var}(f)=p(1-p)\le1/4\). Cauchy--Schwarz therefore gives
\(p'(\tau)^2\le I(\tau)/2\); Theorem 3.9(1) gives the displayed lower bound.

The minimax upper bound is Theorem 3.9(4). For the lower bound, choose an interior
\(\tau_*\in\Theta\) and
\(\delta_n=1/\sqrt{n\bar I}\); for large \(n\), both endpoints lie in
\(\Theta\). Theorem 3.8 gives total variation at most \(1/2\), so the sum of the
two error probabilities at radius \(\delta_n/2\) is at least \(1/2\). Multiplying
by \(\delta_n/2\) and taking the larger endpoint risk yields
\(\mathcal R_{n,1}\ge\delta_n/8\). The \(o/\omega\) statements follow from
Theorems 3.8 and 3.9. \(\blacksquare\)

Figure 5 evaluates the concrete family
\((r_p,r_q,v_p,v_q)=(3,0.5,0,0.02)\), \(\Theta=[1,1.2]\), without sprinkling.
Gauss--Legendre quadrature gives
\(p(1)=0.500591097337\) and \(p(1.2)=0.500705392490\). At \(\tau=1\), the
relative remainder of \(1/2+\kappa\tau\Delta v\), measured against
\(p(\tau)-1/2\), falls from \(1.50\%\) at \(\Delta v=0.02\) to \(0.38\%\) at
\(\Delta v=0.005\); the maxima over the 41-node \(\tau\)-mesh are \(2.06\%\) and
\(0.52\%\). This is the expected first-order decrease for an \(O((\Delta v)^2)\)
absolute remainder.

A separate direct-score quadrature on the same 41 parameter nodes and 1921 spatial
nodes per axis gives
\[
4.5407456\times10^{-6}\le I(\tau)\le4.6629799\times10^{-6}.
\]
The profile is numerically monotone decreasing, so the mesh maximum occurs at the
endpoint \(\tau=1\), on each of the 481-, 961-, and 1921-node grids. At
\(\tau=1,1.1,1.2\), refinement from 961 to 1921 nodes changes the values by
\(0.71\%\), \(0.55\%\), and \(0.44\%\), respectively. On the finest mesh,
\(\min_\tau I(\tau)/(2p'(\tau)^2)=7.028\), displaying the slack in the Fisher
inequality of Corollary 3.10.

The deterministic small-lapse sweep at \(\tau_0=1\) is

| \(\Delta v\) | \(I(\tau_0)\) at 961 nodes/axis | \(I(\tau_0)/(\Delta v)^2\) |
|---:|---:|---:|
| \(0.080\) | \(5.6491702\times10^{-5}\) | \(0.008827\) |
| \(0.040\) | \(1.7025283\times10^{-5}\) | \(0.010641\) |
| \(0.020\) | \(4.6960692\times10^{-6}\) | \(0.011740\) |
| \(0.010\) | \(1.2348400\times10^{-6}\) | \(0.012348\) |
| \(0.005\) | \(3.1671853\times10^{-7}\) | \(0.012669\) |

A first-order Richardson extrapolation from the two smallest lapses gives
\(I(\tau_0)/(\Delta v)^2\to0.01299\). This is evidence—not a proof—of quadratic
small-lapse scaling. If the corresponding uniform limit were \(0.0130\), the two
Corollary 3.10 coefficients would scale as approximately
\(1.10/(\Delta v\sqrt n)\) and \(66.7/(\Delta v\sqrt n)\), a constant gap of about
61.

For the plotted \(\Delta v=0.02\), the uncapped plug-in expression is
\(3333/\sqrt n\), and it does not fall below the parameter diameter \(0.2\) until
\(n=2.78\times10^8\). The diagnostic Le Cam expression obtained by inserting the
finite mesh maximum is \(57.9/\sqrt n\) and crosses \(0.2\) at
\(n=8.38\times10^4\). Thus the matched-rate theorem is genuinely asymptotic for
this weak-signal example; the finite-\(n\) constants are not practically sharp.

![**Fixed-corner shape information, Fisher scale, and the asymptotic minimax
rate.** Panel A compares deterministic \(p(\tau)\) with its small-lapse leading
term. Panel B compares the 1921-node direct-score profile with the proved quantity
\(2p'(\tau)^2\). Panel C shows the approach of
\(I(\tau_0)/(\Delta v)^2\) toward the Richardson diagnostic \(0.01299\). Panel D
shows the two uncapped \(n^{-1/2}\) expressions and shades the region above the
parameter diameter; the vertical lines mark their crossings. The orange expression
does not certify \(0.02<\Delta v_0\), and the blue expression is **not** a certified
minimax lower bound because a mesh maximum is not a supremum enclosure. All four
panels are deterministic and use no sprinkling or validation
seed.](../viz/output/fig05_minimax_rate.png){width=100%}

#### What Theorems 3.8–3.9 do and do not claim

| Claims | Does **not** claim |
|---|---|
| Matching \(n^{-1/2}\) minimax upper and lower rates for fixed admissible \(\Delta v\) | Equality or optimality of the two constants |
| An explicit ordering-fraction estimator and consistent fixed-pair tests | A numerically certified value of \(\Delta v_0\), or monotonicity at arbitrary lapse |
| Pointwise \(I(\tau)\ge\kappa^2(\Delta v)^2/2\), plus numerical evidence for quadratic small-lapse scaling | A proof of the uniform upper scaling \(\bar I=O((\Delta v)^2)\) as \(\Delta v\downarrow0\) |
| A convergent direct-score mesh diagnostic for the declared family | A certified enclosure of \(\bar I\); Figure 5 does not replace one |
| One \(\Delta v_0\) uniform over \(\tau\in\Theta\) | One testing cardinality uniform over all distinct pairs; the bound requires \(n(\Delta v)^2|\tau-\tau'|^2\to\infty\) |
| QMD, Hellinger, Hoeffding moments, Chebyshev, and two-point testing | Novelty of this standard statistical machinery |
| | Any result in 3+1 dimensions |
| | That \(\tau\) is “horizon information” as a distinct physical invariant |

**Physical interpretation.** In 1+1 Schwarzschild the scalar curvature is
\(R_\tau=-2\tau/r^3\). The parameter \(\tau\) is simultaneously the horizon radius and
the only curvature amplitude of the family. There is no threshold structure that
activates because the diamond crosses \(r=\tau\). Discriminating \(\tau\) is
discrimination of a continuous geometric parameter of the patch, not a proof that an
event horizon has been localized as a codimension-one object.

### 3.4 Summary of §3

| Result | Target and family | Guarantee |
|---|---|---|
| Thm 3.1 | Absolute \(r_s\) or \(M\) on a co-scaling orbit | Exact equality of fixed-\(n\) poset laws |
| Thm 3.2 | Global event horizon over alternative completions | Not a functional of one finite patch |
| Thm 3.8 | \(\tau\) in the fixed-corner diamond family | Estimator-independent lower risk bound |
| Thm 3.9 / Cor 3.10 | Same family, \(0<\Delta v<\Delta v_0\) | Explicit ordering-fraction estimator and minimax rate \(n^{-1/2}\) |

The first result removes an absolute ruler; the last two show that order can still
carry information about dimensionless shape when the external patch is held fixed.

## §4 Future cardinality: exact tagged law and preregistered experiment

Section 3 maps **limits**: targets that no order-only map can identify, or can identify
only above a rate floor. Those theorems would be empty of scientific interest if the
order-only channel were *vacuously* uninformative about every geometric score. This
section records that it is not. In a preregistered held-out evaluation, a single
order-only observable—future cardinality—met every primary endpoint in a finite
\(1{+}1\) Schwarzschild patch. This is evidence for an in-patch geometric signal,
not reconstruction of a global event horizon. We first give the exact population
law of the observable and then describe the more complicated selected procedure
used in the evaluation.

### 4.1 Tagged-element law for future cardinality

**Proposition 4.1 (future-cardinality attenuation).** Let \((W,\prec,\nu)\) be a
non-atomic causal probability patch and let \(X_1,\ldots,X_n\) be i.i.d. from
\(\nu\), with \(n\ge2\). Fix a label \(L\) independently of the sample and define

\[
\upsilon(x):=\nu\{y\in W:x\prec y\},
\qquad
U=\upsilon(X_L),
\qquad
F=\sum_{i\ne L}\mathbf 1\{X_L\prec X_i\}.
\]

For any declared \(Y=t(X_L)\in L^2(\nu)\), and for \(\nu\)-almost every \(x\),

\[
F\mid(X_L=x)\sim\operatorname{Binomial}(n-1,\upsilon(x)).
\]

Consequently,

\[
\begin{aligned}
\operatorname{Var}(F)
&=(n-1)^2\operatorname{Var}(U)
 +(n-1)\mathbb E[U(1-U)],\\
\operatorname{Cov}(F,U)&=(n-1)\operatorname{Var}(U),\\
\operatorname{Cov}(F,Y)&=(n-1)\operatorname{Cov}(U,Y).
\end{aligned}
\]

If \(\operatorname{Var}(U),\operatorname{Var}(Y)>0\), put

\[
\alpha_n
:=
\left(
1+\frac{\mathbb E[U(1-U)]}
{(n-1)\operatorname{Var}(U)}
\right)^{-1/2}.
\]

Then

\[
\operatorname{Corr}(F,U)=\alpha_n,
\qquad
\operatorname{Corr}(F,Y)=\operatorname{Corr}(U,Y)\alpha_n.
\]

Writing \(\gamma=\mathbb E[U(1-U)]/\operatorname{Var}(U)\),

\[
\alpha_n=1-\frac{\gamma}{2(n-1)}+O(n^{-2}),
\]

so both correlation gaps are \(O(n^{-1})\).

*Proof.* Conditional on \(X_L=x\), the remaining \(n-1\) points are independent
and each lies in \(J^+(x)\cap W\) with probability \(\upsilon(x)\). This gives the
binomial law. Total variance gives the displayed variance, while
\(\mathbb E[F\mid X_L]=(n-1)U\) gives the two covariance identities. Substitution
into the definition of correlation and Taylor expansion of
\((1+\gamma/(n-1))^{-1/2}\) finish the proof. \(\blacksquare\)

The proposition concerns a label fixed before seeing the causet. The preregistered
procedure below computes the same combinatorial quantity \(F_i=|J^+(i)|\), but
then restricts to minimal elements and partitions their values using the full
causet. Conditioning on minimality already changes the law of the other points,
and the subsequent selector adds further dependence. Proposition 4.1 therefore
justifies the choice of observable before selection: future cardinality is a
binomial thinning of continuum future-volume fraction and its correlation
attenuation is \(O(n^{-1})\). It is not an unbiasedness theorem for the final bracket;
§4.2 separately evaluates the selected rule built from that observable.

**Population illustration.** Figure 6 uses a deliberately separate, fully exterior
window to expose finite-box confounding:

\[
W=[0,6]\times[1.1,4],
\qquad r_s=1,
\qquad \nu=dt\,dr/\operatorname{Vol}(W),
\]

the tortoise coordinate \(r_*(r)=r+\log(r-1)\) gives

\[
\upsilon(t,r)
=
\frac{1}{\operatorname{Vol}(W)}
\int_{1.1}^{4}
\bigl[6-t-|r_*(r')-r_*(r)|\bigr]_+\,dr'.
\]

Deterministic quadrature, without sprinkling, gives

| Quantity | Value |
|---|---:|
| Window-and-chart target \(\rho_\infty=\operatorname{Corr}(U,Y)\) | \(-0.951388\) |
| Tagged attenuation \(\alpha_{900}=\operatorname{Corr}(F,U)\) | \(0.998400\) |
| Tagged finite-\(n\) correlation \(\rho_{900}=\operatorname{Corr}(F,Y)\) | \(-0.949866\) |
| One-causet coefficient in Figure 6, \(\widehat\rho_{\mathrm{cloud}}\) | \(-0.951\) (rounded) |

The target depends on the window, normalized measure, and declared time coordinate;
it is not an intrinsic Schwarzschild scalar. This is **not** the crossing-window
experiment of §4.2: it has \(r_s=1\), remains at \(r>1\), and uses Schwarzschild
time, whose chart is singular at the horizon. The cloud pairs \((F_i,Y_i)\) in one
causet are dependent, so ordinary i.i.d. correlation intervals do not apply. For
fixed \(u>0\), the conditional coefficient of variation is

\[
\operatorname{CV}(F\mid U=u)
=
\sqrt{\frac{1-u}{(n-1)u}},
\]

which is pointwise \(O(n^{-1/2})\), not uniform as \(u\downarrow0\).

![**Future cardinality in a finite Schwarzschild window.** In the fixed-seed
\(N=900\) causet, the dependent internal coefficients are
\(\widehat\rho_{\mathrm{cloud}}(F,t)=-0.951\),
\(\widehat\rho_{\mathrm{cloud}}(F,r)=0.164\), and \(0.465\) in the narrow time
band. Panel B separately reports the deterministic window target
\(\rho_\infty=-0.951388\) and the tagged-element value
\(\rho_{900}=-0.949866\). None of these correlations establishes horizon
recovery.](../viz/output/fig06_box_wall.png){width=100%}

### 4.2 Evaluation contract

The pre-registration, estimator specification, thresholds, seeds, and executable
instrument are archived with the repository. The sealed threshold file has the
following SHA256 (concatenate the two displayed lines):
\[
\begin{gathered}
\texttt{6e2c38881234cef48e859096b46f261c}\\
\texttt{fa83ea8a2f6c955cc1dbc42537bfefd4}.
\end{gathered}
\]
All choices below were fixed before evaluation on the held-out seeds.

**Geometry and ensemble.** The Schwarzschild radius is \(r_s=2M=0.5\). In this
subsection the repository coordinate named \(t\) is the ingoing
Eddington--Finkelstein time coordinate used by the sealed generator; it is not
the exterior Schwarzschild time used only in the separate Figure 6 illustration.
The sprinkling window is
\[
(t,r)\in[0,6]\times[0.1,1.3],
\qquad \operatorname{Vol}(W)=7.2.
\]
The expected cardinalities are \(1500,3000,6000,12000\), with twenty paired
Schwarzschild/Minkowski point clouds per level. The primary endpoint is 12000.
The held-out seeds were drawn once from a reserved band disjoint from exploration.

**Order-only output.** For each causet \(C\), let \(\mathcal M(C)\) be its minimal
elements. For \(i\in\mathcal M(C)\), compute
\[
O_i=|J_C^+(i)|.
\]
The best one-dimensional two-means split of the integer values \(\{O_i\}\) fixes a
half-integer threshold and partitions \(\mathcal M(C)\) into low- and high-future
classes. This partition, together with its separation score, is the output of the
order-only stage. A data-independent gate, calibrated under a matched
\(\mathrm{Uniform}[0,1]\) null, abstains when the split explains too little
variance.

**Scored estimand.** Only after the partition has been fixed are the hidden radial
coordinates revealed. They convert the two classes into the order-statistic bracket
\[
B(C)=[r_{\mathrm{lo}},r_{\mathrm{hi}}]
=
\left[
\max_{O_i<\mathrm{thr}}r_i,
\min_{O_i>\mathrm{thr}}r_i
\right].
\]
The scored target is the declared transition radius \(r_s=0.5\): coverage means
\(r_s\in B(C)\), localization error is represented by the bracket width, and the
reported point location is its midpoint. Thus coordinates score an order-only
partition; they do not choose the observable, threshold, or selected classes.

**Principled threshold scale.** The primary endpoint has
\[
\varrho=\frac{\bar n}{\operatorname{Vol}(W)}
=\frac{12000}{7.2}=1666.67,
\qquad
\ell=\varrho^{-1/2}=0.0244949.
\]
The frozen localization constant was \(K_{\mathrm{loc}}=2\). Hence the two
reported tolerances were fixed *a priori* at two discreteness lengths,
\[
\theta_{\mathrm{loc}}
=\frac{K_{\mathrm{loc}}\ell}{2M}
=0.09798\approx0.098,
\qquad
\theta_{\mathrm{stab}}
=K_{\mathrm{loc}}\ell
=0.04899\approx0.049.
\]
They are therefore resolution-anchored criteria, not numbers tuned to the held-out
outcome.

At the primary endpoint the frozen contract required simultaneously:
paired sign-flip \(p\le10^{-4}\); median bracket width
\(|dr|/(2M)\le0.098\); coverage at least \(0.5\); radial midpoint standard
deviation at most \(0.049\); leave-one-out false-positive fraction at most
\(0.05\); convergence slack across the four levels; and an order-isomorphism
guard. Fewer than 18 valid seeds would be inconclusive. The frozen experiment used
upper time boundary \(t=6\); any shorter window was outside its declared domain.

### 4.3 Outcome

**Verdict.** The frozen primary endpoint passed every declared check. The original
raw result file was subsequently lost; all transcribed fields were reproduced by a
supervised deterministic replay, so the result is retained with that caveat rather
than described as a preserved blind artifact.

At the primary endpoint, all six frozen checks evaluated true in the archived result
record. Headline primary numbers (transcribed from
the original validation table; same values MATCH under supervised re-verification):

| Check | Primary (target mean \(\bar n=12000\)) |
|---|---|
| Sign-flip \(p_{\mathrm{perm}}\) | \(9.54\times 10^{-7}\le 10^{-4}\) |
| Median \(\lvert dr\rvert/(2M)\) vs \(\theta_{\mathrm{loc}}\) | \(0.064\le 0.098\) |
| Coverage | \(0.95\ge 0.5\) |
| Boundary \(r\)-std vs \(\theta_{\mathrm{stab}}\) | \(0.008\le 0.049\) |
| LOO false-positive fraction | \(0.00\le 0.05\) |
| Order-only guard | no raise |

The abstention threshold \(g_n\) (called `tau(n)` in the archived code) behaves as
designed: Schwarzschild abstention \(0.00\)
at every intensity level; Minkowski control abstention \(0.90\)–\(1.00\) (suppresses
structureless false structure). A transparent non-primary caveat is recorded: at
target mean \(\bar n=6000\), false-positive fraction \(0.10\) misses
\(\theta_{\mathrm{fp}}\); the
frozen rule evaluates false positives **only** at the primary endpoint, where the
check passes.

The historical blind run used the frozen package at commit `573cfcb`, NumPy 1.26.4,
and the threshold hash given above.

### 4.4 Artifact status and supervised re-verification

1. The primary `results/validation.json` from the original 2026-06-22 blind run was
   later found unrecoverable.
2. A supervised deterministic replay used the same archived estimator, commit, and
   frozen seeds. It was a verification exercise, not a second blind discovery or a
   retuning loop.
3. Every frozen field matched the recorded table.

The evidential status is therefore weaker than it would be with the original bytes:
the historical blindness is documentary, while numerical reproducibility is supported
by the matching replay. No threshold was changed after observing the outcome.

### 4.5 Interpretation

In a finite \(1{+}1\) Schwarzschild patch at the
preregistered domain edge, the causal order alone—under this observable and this
protocol—carries enough information to localize a horizon-*associated* boundary
score while meeting the declared significance and stability criteria, with bracket width
contracting toward the discreteness floor as density grows, while a box-matched
flat control does not produce the same separation.

The rule was evaluated directly against the frozen success criteria; it does not
assume that the selected bracket is unbiased or that Proposition 4.1 survives
conditioning on minimality. Localization is scored in units of \(2M\), with the
target radius and embedding known to the evaluator. This is compatible with
Theorem 3.1 because the experiment tests an order-only partition against a declared
dimensionless score; it does not infer an unknown absolute scale from fixed-\(n\)
order.

**Role relative to Section 3.** The channel is not empty. Non-identifiability of
absolute mass, of the global event horizon, and the rate floor for a continuous
family parameter coexist with recoverability of a **different**, carefully
defined in-patch score.

### 4.6 Scope limits

| Misreading | Why it does not follow |
|---|---|
| Global event horizon reconstructed | Theorem 3.2 |
| Full metric reconstruction | Outside the stated experiment |
| \(3{+}1\) Schwarzschild / Kerr | Not studied here |
| Region-locators C1–C6 work | They do not; see §5 |
| Every order-only map succeeds at something | Only the preregistered procedure is evaluated |
| Primary raw artifact preserved | §4.4 |

---

## §5 Investigated region-locators: empirical limits

The results in §3 concern all measurable estimators in explicitly stated
experiments. This section has a narrower purpose: it records what happened to seven
constructions actually investigated in the finite \(1{+}1\) benchmark. Failure here
is evidence about these constructions, not a minimax theorem and not a universal
no-go for quasi-local observables.

| Channel | Construction | Outcome | Main lesson | Archived record |
|---|---|---|---|---|
| C3-early | Future-width or funnel collapse | Rejected | The funnel followed singularity truncation rather than a regular trapping structure | X0-Qn §11.3 |
| C1 | Bottleneck or ideal flow through maximal elements | Not closed | Finite maximal elements trivialized the proposed definition | COM-008/010 |
| C2 | Common-future overlap on a wavefront | Blocked | The statistic was confounded by the computational ceiling | COM-006 |
| C3-third | Truncated-future selectors on minimal elements | Inconclusive | The signal remained edge-dominated and marginal | TF-20260719 |
| C4 | Common-future convergence conditioned on neighbors | Blocked | No permutation-invariant, non-circular neighbor graph was available | COM-039 |
| C5 | Spectral partition of the common-future matrix | Exhausted | Wall, bridge, and twin ambiguities prevented a stable region interpretation | COM-042 |
| C6 | Antichain waist of an Alexandrov interval | Blocked | An antichain exists order-theoretically, but no stable codimension-two screen with transport and sign was obtained | COM-043/044 |

The final column gives stable, repository-searchable archive identifiers: `COM-nnn`
denotes the corresponding committee decision, `TF-20260719` the frozen
truncated-futures evidence bundle, and `X0-Qn` the dated well-posedness notebook.

The recurring problems were finite-window truncation mistaken for physical
structure, absence of a lateral neighbor relation, scale--depth confounding, and
lack of a stable codimension-two object. These observations motivated stopping this
particular estimator line. They do not imply that causal order contains no geometric
information—Section 4 gives a counterexample—or that every named quasi-local target
is non-identifiable. Such a claim would require its own completion pair, equality of
laws, or statistical lower bound.

## §6 Relation to the literature

We place the mathematical and empirical results against published work without
claiming novelty for standard causal-set or statistical machinery.

### 6.1 Order, number, and scale

The slogan that continuum Lorentzian geometry arises from causal order together
with counting information—“Order + Number equals Geometry”—is standard in causal
set theory [1,12]. Recent
work makes related statements mathematically precise for *labeled* random
adjacency matrices and related reconstruction settings (Braun [3],
separating chronological isomorphy / conformal content from volume-preservation /
isometry). Madsen [7] states explicitly that order alone is
“famously insufficient,” connecting that insufficiency to Müller’s [9] negative
finite-order results.

Three qualifications keep those results from being read as more than background
here. First, **dimension**: Braun assumes \(d\ge 3\). Madsen states Theorem 4.18
for general \(d\), although its proof explicitly calls the covariance term
subdominant only for \(d>2\); the \(d=2\) bookkeeping therefore requires separate
qualification. Second, **what Braun’s hypothesis consumes**: his Theorem 1.4
requires the laws of the adjacency matrices to agree *for every* \(k\in\mathbb{N}\),
and the proof passes to the projective limit \(\nu_\infty\); it is a statement about
the full order data at all cardinalities, not about any scalar summary or any single
\(k\). Third, **what kind of statement it is**: Theorem 1.4 is an
identifiability-in-law result — an injectivity statement with no estimator, no rate,
and no finite-\(n\) risk bound. It therefore neither competes with nor is weakened by
finite-\(n\) risk statements such as Theorem 3.1; the two occupy different layers.
Braun’s sampling model does, however, coincide with the channel used here: he models
\(\{X_1,\dots,X_k\}\) as “the random support of a PPP conditioned on \(k\) elements”
(p.\ 4), i.e.\ fixed-cardinality conditioning.

The comparison is most transparent as a ladder of information regimes. Conditioning on
\(N=n\) removes the global volume--density calibration and leaves the exact dilation-null
direction of Theorem 3.1. Holding the EF corners fixed supplies an external geometric ruler:
alternatives at separation \(n^{-1/2}\) remain locally difficult in the sense of Theorem 3.8,
whereas fixed alternatives separate and the ordering fraction estimates \(\tau\) at the matching
rate by Theorem 3.9. Madsen occupies a richer regime in which two embeddings share a density
calibration and satisfy F1--F3; there, high-density well-conditioned presentations are forced
toward approximate isometry on their deep interiors. The common-density calibration prevents
the global-dilation degeneracy present in the fixed-cardinality experiment. It is not the only
substantive hypothesis: F2’s continuum-diamond volume control and F3’s longest-chain/proper-time
correspondence are additional geometric inputs, and Madsen proves conditional uniqueness of
admissible embeddings rather than an order-only estimator or a finite-\(n\) risk bound.

Theorem 3.1 does not invent this slogan. It supplies an **exact finite-\(n\)**
total-variation statement for Poisson sprinklings of Schwarzschild patches under
dilation (and a scoped \(3{+}1\) co-scaling statement): absolute mass is
non-identifiable in the order-only fixed-\(n\) channel. Hawking–King–McCarthy
(J.\ Math.\ Phys.\ 17, 174, 1976) and Malament (J.\ Math.\ Phys.\ 18, 1399,
1977) are continuum precursors for the difficult causal-isomorphism-to-conformal
direction; that machinery is not used in Theorem 3.1’s easy direction. More
directly, Bombelli’s 1987 thesis states recovery only up to a global scale factor
and records Zeeman’s Poincaré-plus-dilatations result for Minkowski causal
isomorphisms. Those facts motivate the orbit; they are not a substitute for the
sprinkling-channel TV calculation.

### 6.2 Indistinguishability of orders without rates

Müller [9] constructs pairs of non-isometric Lorentzian geometries
that admit finite causal sets with nearly identical order laws at fixed
cardinality—precise negative results for naive formulations of the
Hauptvermutung. His Theorem 3 is also the closest published **quantitative**
precursor: for normalized flat cylinders, the probability of observing a total
order has an explicit \(K\)-dependent lower bound while temporal diameter varies.
The mechanism is degeneration toward one order type, not a QMD family, and the
paper does not formulate Fisher information, a Le Cam risk bound, or a local
minimax floor for a Schwarzschild parameter. Theorem 3.8 is the family-specific
regular-parametric instantiation; it is not the first quantitative
indistinguishability statement for a continuous geometric family.

### 6.3 Constructive geometric estimators

Boguñá and Krioukov [2] estimate spacelike
distances from causal overlaps with errors that vanish in a continuum limit, with
discreteness scales of the form \(\varrho^{-1/(d+1)}\) in their conventions. Their
direction is complementary to Theorems 3.8–3.9: they give **constructive upper
rates** for spacelike-distance functionals; Theorem 3.8 gives an
**estimator-independent lower bound** for a named parametric family, while
Theorem 3.9 supplies an elementary order-only estimator attaining the same rate
for that family. Its statistic \(S_n/\binom n2\) is the classical *ordering
fraction* underlying the Myrheim--Meyer dimension estimator (Myrheim 1978; Meyer
1988 [14,15]; reviewed by Surya [12] and tested in curved settings by Reid [13]). Here the
dimension is fixed and the same statistic estimates a continuous parameter of a
curved family. Theorem 3.9 is not a spacelike-distance or dimension estimator.

### 6.4 Horizons and quasi-local structure in causal sets

The causal-set black-hole literature includes the counting of causal links crossing
a horizon [16], later horizon-molecule definitions with continuum area limits [17],
and explicit algorithms for the causal relation in four-dimensional Schwarzschild
spacetime [18]. These constructions
are essential context, but they assume a declared continuum horizon or address a
different observation problem; they do not make the global event horizon a
functional of one finite patch.

Eichhorn, Gamito, and Stokes [5] develop causal-set diagnostics
related to black-hole horizons and geodesic focusing, including ladder-based
proxies for expansion. That literature motivates why quasi-local horizon
structure is interesting and why continuum intuition is subtle in low dimension.
It does not supply, in our order-only finite-patch bank, a stable codimension-two
screen with order-only transport—the obstruction recorded for channel C6—or a
counterexample to Theorems 3.1–3.2. Benincasa–Dowker-type interval abundances [19] and
related curvature observables target manifoldlikeness and scalar curvature, not
the region-locators tested here.

### 6.5 Statistical methods

Quadratic-mean differentiability, Hellinger tensorization, data processing,
Hoeffding variance identities, Chebyshev testing, and two-point (Le Cam) lower
bounds are textbook [10,11]. Theorems 3.8–3.9 claim the
**instantiation**: a geometric family for which regularity, a uniform small-lapse
expansion of a concrete order statistic, and both sides of the \(n^{-1/2}\)
minimax rate are proved. We do not claim a new method of nonparametric statistics,
an optimal critical-scale constant, or priority over every related latent-order
model.

### 6.6 What we do not cite as competition

We do not treat failures of particular estimators in the literature—or our own
experiments—as proofs of non-identifiability. Conversely, we do not treat continuum
reconstruction theorems under order+number hypotheses as refutations of
fixed-\(n\) order-only blindness for absolute mass.

---

## §7 Scope and open questions

### 7.1 Established here

| Question | Result |
|---|---|
| Absolute scale on a patch-shape-preserving orbit | Exactly absent from the fixed-\(n\) order law |
| Global event horizon from one causally convex patch | Not a functional of the observation |
| Fixed-corner parameter \(\tau\) at small fixed \(\Delta v\) | Minimax absolute-error rate \(n^{-1/2}\) |
| Future cardinality of a pretagged element | Exact binomial mixture and finite-\(n\) attenuation |
| Preregistered minimal-element procedure | Met all primary criteria; original raw artifact lost |
| Investigated region-locators | Unsuccessful as listed; no universal no-go |

### 7.2 Open questions

1. Prove the numerically supported uniform small-lapse law
   \(\bar I\sim C(\Delta v)^2\), or find a counterexample away from
   \(\tau_0\). The endpoint sweep gives
   \(I(\tau_0)/(\Delta v)^2\to0.01299\) by first-order Richardson extrapolation,
   but it is neither uniform in \(\tau\) nor a certified asymptotic enclosure.
2. Compute certified numerical values of \(\bar I\), \(\Delta v_0\), and the
   critical-scale efficiency of the ordering-fraction estimator.
3. Derive the law induced by conditioning on minimality and by the data-dependent
   split in §4; Proposition 4.1 covers neither selection step.
4. Construct a regular \(3{+}1\) parametric family with comparable lower and upper
   order-only rates.
5. Study absolute scale in the order+number channel with known sprinkling density.
6. For a specifically defined quasi-local proxy, seek either a witness pair or a
   constructive estimator under a new observation contract.

Direct reconstruction of the global event horizon from one finite order-only patch
is not an open estimator problem under the present observation model; Theorem 3.2
shows that the target itself must first be changed.

## §8 Conclusions

A finite unlabeled order at fixed cardinality has no external ruler, but it need
not be devoid of geometric information. We made that distinction explicit for
Schwarzschild patches. Co-scaling the mass and patch leaves the order law exactly
unchanged, and a global event horizon cannot be determined from one causally
convex patch because alternative future completions can agree on all patch data.

When the Eddington--Finkelstein corners are held fixed instead, varying \(\tau\)
changes dimensionless patch shape. On the regular diamond family, a Fisher
two-point argument bounds every order-only estimator from below, while inversion
of the ordering fraction gives an explicit uniform upper bound. For every fixed
\(0<\Delta v<\Delta v_0\), the minimax absolute-error rate is therefore
\(n^{-1/2}\). The plotted family also makes the limitation concrete: the available
upper constant is nontrivial relative to the parameter diameter only at very large
\(n\). Deterministic quadrature supports matching \(1/\Delta v\) scaling of the
two constants, but a uniform proof and sharp constants remain open.

Future cardinality provides a complementary positive result. For a pretagged
element it is exactly a binomial thinning of continuum future volume, with an
explicit \(O(n^{-1})\) correlation attenuation. The preregistered minimal-element
procedure uses the same observable but adds selection dependence; its primary
empirical outcome is therefore reported separately, together with the loss of the
original raw artifact and the matching replay of its transcribed fields. The unsuccessful
region-locators in §5 provide design lessons, not impossibility theorems.

The resulting picture is narrower and more useful than either “order reconstructs
the black hole” or “order sees nothing”: fixed-\(n\) order can encode
dimensionless shape, while absolute scale and completion-dependent targets require
additional information or a different question.

## Acknowledgments

The author used AI assistants — Anthropic's Claude and OpenAI's ChatGPT — for code
writing, literature search, and manuscript preparation. All code, mathematical
statements, proofs, and numerical results were verified by the author, who takes
full responsibility for the content.

## Funding

No external funding was received for this work.

## Competing interests

The author declares no competing interests.

## Data and code availability

Code, deterministic figure generators, the pre-registration, sealed thresholds,
and the supervised re-verification record are available in the `nachocausal`
repository. The figure runner emits the complete numerical sweep quoted in the text;
those values reproduce in the pinned environment. Cross-machine PNG byte identity
is not claimed because font and FreeType rasterization can alter pixels without
altering the underlying numbers. The seal can be checked with `make verify-seal`.
No new validation ensemble was generated for this manuscript revision. The missing
primary artifact and the scope of its deterministic replay are described in §4.4.

## References

[1] L. Bombelli, *Space-time as a Causal Set*, Ph.D. thesis, Syracuse University
(1987).

[2] M. Boguñá and D. Krioukov, “Measuring spatial distances in causal sets via
causal overlaps,” *Phys. Rev. D* **110**, 024008 (2024),
doi:10.1103/PhysRevD.110.024008, arXiv:2401.17376.

[3] M. Braun, “Spacetime reconstruction by order and number,” arXiv:2507.01907
(2025).

[4] L. Bombelli, J. Henson, and R. D. Sorkin, “Discreteness without symmetry
breaking: a theorem,” arXiv:gr-qc/0605006 (2006).

[5] A. Eichhorn, P. Gamito, and N. Stokes, “Towards black-hole horizons and
geodesic focusing in causal sets,” arXiv:2605.06813 (2026).

[6] S. W. Hawking, A. R. King, and P. J. McCarthy, “A new topology for curved
space-time which incorporates the causal, differential, and conformal structures,”
*J. Math. Phys.* **17**, 174 (1976).

[7] N. Madsen, “On the uniqueness of embeddings of causal sets,”
arXiv:2607.05840 (2026).

[8] D. B. Malament, “The class of continuous timelike curves determines the
topology of spacetime,” *J. Math. Phys.* **18**, 1399 (1977).

[9] O. Müller, “On the Hauptvermutung of causal set theory,” arXiv:2503.01719
(2025).

[10] A. B. Tsybakov, *Introduction to Nonparametric Estimation*, Springer (2009).

[11] A. W. van der Vaart, *Asymptotic Statistics*, Cambridge University Press
(1998).

[12] S. Surya, “The causal set approach to quantum gravity,”
*Living Rev. Relativ.* **22**, 5 (2019), arXiv:1903.11544.

[13] D. D. Reid, “Manifold dimension of a causal set: tests in conformally flat
spacetimes,” arXiv:gr-qc/0207103.

[14] J. Myrheim, *Statistical Geometry*, CERN preprint TH-2538 (1978).

[15] D. A. Meyer, *The Dimension of Causal Sets*, Ph.D. thesis,
Massachusetts Institute of Technology (1988).

[16] D. Dou and R. D. Sorkin, “Black hole entropy as causal links,”
arXiv:gr-qc/0302009 (2003).

[17] C. Barton, A. Counsell, F. Dowker, D. S. W. Gould, I. Jubb, and G. Taylor,
“Horizon molecules in causal set theory,” arXiv:1909.08620 (2019).

[18] S. He and D. Rideout, “A causal set black hole,” arXiv:0811.4235 (2008).

[19] D. M. T. Benincasa and F. Dowker, “The scalar curvature of a causal set,”
*Phys. Rev. Lett.* **104**, 181301 (2010), arXiv:1001.2725.

[20] I. Booth, “Black hole boundaries,” arXiv:gr-qc/0508107 (2005).
