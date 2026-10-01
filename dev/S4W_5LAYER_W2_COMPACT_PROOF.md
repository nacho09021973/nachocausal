# S4W — proof of compact-W2 suppression for the five-layer operator

**Date:** 2026-09-15  
**Branch:** `s4w-5layer-candidate`  
**Scope:** analytic lemma only; no simulation; no global `phi=1` claim; no Kretschmann coefficient claim.

## 1. Statement

Let the curved-spacetime `W2` contribution before application of the density differential operator be written as

\[
J(\rho)=\int_D dz\int_0^{U_*(z)}
A(U,z)e^{-\rho\mathcal V(U,z)}\,dU,
\]

where `z` denotes the longitudinal/angular variables and `D` is compact.
Assume:

1. `U_*(z)>0` is continuous on `D`, so `inf_D U_*>0`;
2. for `0<=U<=U_*(z)`,
   \[
   \mathcal V(U,z)=U^2 g(U,z),
   \]
   with `g` positive and sufficiently smooth, and there exists `c>0` such that
   \[
   g(U,z)\ge c
   \]
   uniformly;
3. the change of variable
   \[
   s=\sqrt{\mathcal V(U,z)}=U\sqrt{g(U,z)}
   \]
   is uniformly invertible on a fixed neighbourhood of `U=0` for all `z\in D`;
4. after this change of variable, the transformed amplitude
   \[
   \widetilde A(s,z)=A(U(s,z),z)\,\partial_s U(s,z)
   \]
   is `C^4` in `s` with derivatives through order 4 uniformly bounded on the compact domain.

Let

\[
H=\rho\partial_\rho,
\qquad
\widehat{\mathcal O}_*
=\frac23(H+\tfrac12)(H+1)(H+\tfrac32)(H+2),
\]

and define

\[
I_{2,*}(\rho)=\widehat{\mathcal O}_*J(\rho).
\]

Then

\[
\boxed{I_{2,*}(\rho)=O(\rho^{-5/2})}
\qquad (\rho\to\infty).
\]

Consequently, since the integral term in the mean five-layer d'Alembertian carries the prefactor `rho^(3/2)`, the full compact-`W2` contribution obeys

\[
\boxed{\langle B_*\rangle_{W2}=O(\rho^{-1})}
=o(\rho^{-1/2}).
\]

Thus a local candidate term of order `C^2 rho^(-1/2)` cannot be contaminated by a **fixed compact** `W2` region under the assumptions above.

## 2. Reduction to a Gaussian Laplace integral

Because

\[
\mathcal V(U,z)=U^2g(U,z),\qquad g(0,z)\ge c>0,
\]

we have

\[
\left.\partial_U s\right|_{U=0}=\sqrt{g(0,z)}\ge\sqrt c>0.
\]

By the parameter-dependent inverse-function theorem and compactness of `D`, there is a common neighbourhood of `U=0` on which `U\mapsto s` is invertible uniformly in `z`.

The part of the integral outside that neighbourhood has `\mathcal V\ge v_0>0` uniformly and therefore contributes

\[
O(\rho^N e^{-\rho v_0})
\]

after application of any fixed polynomial in `H`; this is smaller than every inverse power of `rho`.

Hence it is sufficient to analyse

\[
J_{\rm loc}(\rho)
=\int_D dz\int_0^{s_*(z)}
\widetilde A(s,z)e^{-\rho s^2}\,ds,
\]

where `s_*(z)` is bounded below by some `s_0>0` after fixing the common local neighbourhood.

## 3. Action of the five-layer density operator

For `x=\rho s^2`,

\[
\widehat{\mathcal O}_*e^{-\rho s^2}
=P_*(x)e^{-x},
\]

with

\[
P_*(x)=1-14x+\frac{41}{2}x^2-\frac{22}{3}x^3+\frac23x^4.
\]

Equivalently, `O_*` annihilates the four pure powers

\[
\rho^{-1/2},\qquad
\rho^{-1},\qquad
\rho^{-3/2},\qquad
\rho^{-2}.
\]

Indeed, for any `\alpha`,

\[
(H+\alpha)\rho^{-\beta}=(\alpha-\beta)\rho^{-\beta},
\]

so the roots `-1/2,-1,-3/2,-2` of `O_*` give the four cancellations exactly.

Since the domain is compact, differentiation under the integral is justified, and we may write

\[
I_{2,*}
=\int_D dz\int_0^{s_*(z)}
\widetilde A(s,z)P_*(\rho s^2)e^{-\rho s^2}\,ds
+O(\rho^{-N})
\]

for arbitrary fixed `N` from the exponentially suppressed nonlocal remainder just isolated.

## 4. Four exact moment cancellations

Taylor-expand uniformly at `s=0`:

\[
\widetilde A(s,z)
=a_0(z)+a_1(z)s+a_2(z)s^2+a_3(z)s^3+R_4(s,z),
\]

with

\[
|R_4(s,z)|\le C s^4
\]

for a constant `C` independent of `z`.

For `m=0,1,2,3`, first extend the upper limit to infinity. The tail satisfies

\[
\int_{s_0}^{\infty}s^m|P_*(\rho s^2)|e^{-\rho s^2}ds
=O(\operatorname{poly}(\rho)e^{-\rho s_0^2}),
\]

uniformly in `z`.

On `[0,\infty)`,

\[
\int_0^\infty s^m e^{-\rho s^2}ds
=\frac12\Gamma\!\left(\frac{m+1}{2}\right)
\rho^{-(m+1)/2}.
\]

Applying `O_*` gives zero for `m=0,1,2,3`, because the exponents are respectively

\[
\frac12,\quad1,\quad\frac32,\quad2.
\]

Therefore every Taylor term through cubic order contributes only an exponentially small upper-limit error.

In particular, no `rho^-2 log rho` term is generated in this endpoint problem: after the `s=sqrt(V)` reduction the standard Gaussian Laplace expansion has ordinary half-integer powers, and the first four are annihilated exactly.

## 5. Remainder bound

Using `|R_4(s,z)|<=Cs^4`,

\[
\begin{aligned}
\left|
\int_0^{s_*(z)}R_4(s,z)
P_*(\rho s^2)e^{-\rho s^2}ds
\right|
&\le
C\int_0^\infty s^4|P_*(\rho s^2)|e^{-\rho s^2}ds.
\end{aligned}
\]

Set `q=sqrt(rho) s`. Then

\[
\int_0^\infty s^4|P_*(\rho s^2)|e^{-\rho s^2}ds
=
\rho^{-5/2}
\int_0^\infty q^4|P_*(q^2)|e^{-q^2}dq.
\]

The remaining `q` integral is a finite numerical constant. Hence, uniformly in `z`,

\[
\left|\cdots\right|\le C'\rho^{-5/2}.
\]

Since `D` has finite measure,

\[
\boxed{I_{2,*}=O(\rho^{-5/2})}.
\]

Multiplication by the `rho^(3/2)` prefactor of the mean GCD integral yields

\[
\boxed{\langle B_*\rangle_{W2}=O(\rho^{-1})}.
\]

## 6. Scope boundary

This proof is deliberately narrower than a global `phi=1` statement.

It proves suppression for a **fixed compact W2 domain** satisfying the stated uniform positivity and smoothness assumptions. It does **not** prove that the implicit `O(rho^-1)` constant remains bounded when the compact support is removed or when the longitudinal cutoff is sent to infinity.

That distinction matters because, in Schwarzschild, the electric/magnetic Weyl decomposition with respect to the interval orientation `U_y` can grow strongly with rapidity. The separate symbolic check reported in the audit discussion finds `E^2+H^2 ~ gamma^4` at large boosts, while the hyperboloid measure grows as `~e^(2 eta)`. This identifies a genuine non-uniformity risk in the limit of unbounded longitudinal support, but does not contradict the compact-domain theorem above.

Therefore the allowed status is

```text
S4W_W2_FIXED_COMPACT_REGION = PROVED_O_RHO_MINUS_1
S4W_W2_CONTAMINATION_AT_C2_ORDER = ABSENT_UNDER_STATED_ASSUMPTIONS
S4W_GLOBAL_PHI_EQUALS_1 = NOT_PROVED
S4W_UNIFORM_LONGITUDINAL_CUTOFF_REMOVAL = OPEN
```

No claim about the local `C^2` coefficient, a normalized Kretschmann estimator, variance, horizon localization, or novelty follows from this lemma alone.
