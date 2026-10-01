# S4W — uniform W1 remainder control near the null direction

**Date:** 2026-09-15  
**Branch:** `s4w-5layer-candidate`  
**Scope:** analytic proof for fixed compact `W1`; no global `phi=1` claim; no variance claim; no horizon claim.  
**Status:** `INTERNAL_PROOF_CANDIDATE / INDEPENDENT_AUDIT_REQUIRED`

## 1. Statement

For the five-layer operator

\[
B_*\phi(x)=\frac{8\sqrt6}{3}\rho^{1/2}
\left[-\frac12\phi(x)+\sum_{L_1}\phi-14\sum_{L_2}\phi+41\sum_{L_3}\phi-44\sum_{L_4}\phi+16\sum_{L_5}\phi\right],
\]

with

\[
\widehat{\mathcal O}_*=
\frac23(H+\tfrac12)(H+1)(H+\tfrac32)(H+2),
\qquad H=\rho\partial_\rho,
\]

consider Schwarzschild 4D Ricci-flat and a fixed compact regulator `phi` that equals `1` in a neighbourhood of `x`.

Let `W1` be the local RNC region used by Belenchia–Benincasa–Dowker. Then the remainder after subtracting the explicit quadratic-Weyl contribution is uniform as the interval orientation approaches the null direction, and the resulting mean contribution satisfies

\[
\boxed{
\mathbb E[B_*\phi(x)]_{W1}
=
-\frac{73\sqrt6}{1575\pi}
C_{abcd}C^{abcd}(x)\rho^{-1/2}
+O(\rho^{-3/4}\log\rho)
}
\]

under the smoothness assumptions stated below.

Since

\[
\rho^{-3/4}\log\rho=o(\rho^{-1/2}),
\]

the local Weyl/Kretschmann term is asymptotically isolated inside fixed compact `W1`.

This proof does **not** establish the unregulated global `phi=1` case, realization-level convergence, variance control, or a horizon detector.

## 2. Why the remainder must be controlled in RNC variables, not in boosted `U`

The preceding W1 derivation used Wang's small-Alexandrov-diamond expansion to identify the degree-eight curvature-squared coefficient. The apparent obstruction is that the ACD orientation

\[
U_y^a=y^a/\tau
\]

can acquire arbitrarily large rapidity as `u/v -> 0`, so a remainder written only as `O(l^9)` for each fixed `U` is not automatically uniform in `U`.

The correct control comes from the Belenchia–Benincasa–Dowker RNC expansion, where the remainder is a smooth function of the coordinate vector `y` on a compact set. Thus the null-direction limit is controlled directly in `y`, without requiring a boost-uniform estimate on Wang's `O(l^9)`.

## 3. BBD volume expansion in vacuum

In the local RNC region, BBD write the interval volume in the form

\[
V(y)=V_0(y)
-\frac{\pi}{4320}\tau^6R(x)
+\frac{\pi}{720}\tau^4y^\mu y^\nu R_{\mu\nu}(x)
+\tau^4y^\mu y^\nu y^\rho S_{\mu\nu\rho}(y),
\]

with `S_{mu nu rho}(y)` sufficiently smooth on fixed compact `W1`.

For Schwarzschild vacuum,

\[
R_{\mu\nu}=0,
\qquad R=0,
\]

so

\[
\boxed{
V(y)-V_0(y)
=
\tau^4y^\mu y^\nu y^\rho S_{\mu\nu\rho}(y).
}
\]

Because `W1` is compact and `S` is smooth, Taylor expansion at `y=0` is uniform.

## 4. Uniform Taylor decomposition

Write

\[
S_{\mu\nu\rho}(y)
=
A_{\mu\nu\rho}
+B_{\mu\nu\rho\alpha}y^\alpha
+y^\alpha y^\beta
C_{\mu\nu\rho\alpha\beta}(y),
\]

where `C(y)` is uniformly bounded on compact `W1`.

Hence

\[
V(y)-V_0(y)
=
\tau^4Q_3(y)+\tau^4Q_4(y)+R_V(y),
\]

with `Q_3,Q_4` homogeneous polynomials of degree 3 and 4 and

\[
\boxed{
|R_V(y)|\le C_V\tau^4|y|^5
}
\]

for a direction-independent constant `C_V`.

This is the required uniformity statement: the bound is in regular RNC coordinates and contains no negative power of `tau` or boost factor.

## 5. The degree-seven term vanishes identically

Fix any timelike vector `z` and set

\[
y=\lambda z,\qquad \lambda\to0.
\]

Then the RNC expansion gives

\[
V(\lambda z)
=
V_0(\lambda z)
+\lambda^7\tau(z)^4Q_3(z)
+\lambda^8\tau(z)^4Q_4(z)
+O(\lambda^9).
\]

Wang's vacuum ACD expansion starts, after the flat term, at curvature-squared order `l^8`; there is no `l^7` term. Therefore for every timelike `z`,

\[
\tau(z)^4Q_3(z)=0.
\]

Since `tau(z) != 0` on the timelike cone,

\[
Q_3(z)=0
\]

on an open set. As `Q_3` is polynomial,

\[
\boxed{Q_3\equiv0.}
\]

Thus there is no degree-seven correction that could dominate the desired `rho^-1/2` Weyl term.

## 6. Identification of the degree-eight term

The degree-eight homogeneous polynomial is fixed by Wang's curvature-squared coefficient. In four-dimensional vacuum, after covariantizing the observer dependence,

\[
V_8(y)=
\frac{\pi}{29030400}
\left[
82K\tau^8
+1376\tau^4T_{abcd}y^ay^by^cy^d
\right],
\]

where

\[
K=C_{abcd}C^{abcd}
\]

and `T_abcd` is the Bel–Robinson tensor.

Therefore on fixed compact `W1`,

\[
\boxed{
V(y)=V_0(y)+V_8(y)+R_V(y),
\qquad |R_V(y)|\le C_V\tau^4|y|^5.
}
\]

Wang is used here only to identify the homogeneous coefficient. The uniform remainder control comes from the BBD RNC smoothness statement.

## 7. Explicit behaviour near the null direction

Use

\[
0\le u\le v\le a,
\qquad
\tau^2=2uv.
\]

On fixed compact `W1`, the Euclidean RNC norm obeys

\[
|y|\le C v.
\]

Hence

\[
|R_V|
\le C_V\tau^4|y|^5
\le C' u^2v^7.
\]

Thus

\[
\boxed{
|R_V(u,v,\Omega)|\le C'u^2v^7
}
\]

uniformly as

\[
u/v\to0.
\]

There is no factor of the form

\[
\gamma^4,\qquad \tau^{-4},\qquad (u/v)^{-p}.
\]

The large-boost behaviour of the electric/magnetic Weyl split is an artifact of using `U=y/tau`; in the covariant polynomial in `y`, the potentially divergent boost factors are compensated by powers of `tau`.

## 8. Uniform metric-determinant remainder

The RNC determinant expansion in Ricci-flat spacetime has

\[
\sqrt{-g(y)}
=
1+G_4(y)+R_g(y),
\]

with

\[
G_4(y)
=-\frac1{180}
C^\gamma{}_{\mu}{}^\alpha{}_{\nu}
C_{\gamma\rho\alpha\sigma}
y^\mu y^\nu y^\rho y^\sigma.
\]

For a smooth metric on compact `W1`, Taylor's theorem gives

\[
\boxed{|R_g(y)|\le C_g|y|^5.}
\]

Again, the bound is uniform in direction.

## 9. Expansion of the local integrand

Write

\[
\sqrt{-g}\,e^{-\rho V}
=
e^{-\rho V_0}
\left[
1+G_4-\rho V_8+\mathcal E
\right].
\]

The explicit terms `G4` and `-rho V8` are exactly those that generated the previously frozen coefficient

\[
-\frac{73\sqrt6}{1575\pi}K\rho^{-1/2}.
\]

The potentially leading remainder pieces are

\[
R_g=O(|y|^5),
\]

and

\[
-\rho R_V
=O(\rho\tau^4|y|^5).
\]

All higher nonlinear combinations carry additional powers of `|y|`.

## 10. Asymptotic size of the remainder

The BBD `W1` analysis reduces smooth compactly-supported remainders to Laplace-type integrals of the form

\[
\widehat{\mathcal O}
\int
(v-u)^2
|y|^s
(\sigma u^2v^2)^q
\Psi(y)
e^{-\sigma u^2v^2}
\,du\,dv\,d\Omega,
\]

with `Psi` and the required derivatives uniformly bounded and

\[
\sigma=\frac{\pi\rho}{6}.
\]

For the first omitted Taylor order here,

\[
s=5.
\]

The basic scaling of such a term before the extra five-layer root is

\[
\rho^{3/2}\rho^{-(s+4)/4}.
\]

For `s=5`,

\[
\rho^{3/2}\rho^{-9/4}=\rho^{-3/4}.
\]

Possible diagonal terms can introduce at most a logarithm, hence

\[
\boxed{
R_{W1}=O(\rho^{-3/4}\log\rho).
}
\]

The additional factor `(H+2)` in `O_*` also annihilates any pure `rho^-2` contribution that could arise at the boundary of the corresponding density integral.

Therefore

\[
\boxed{
R_{W1}=o(\rho^{-1/2}).
}
\]

## 11. Nonlinear exponential terms

On sufficiently small fixed `W1`,

\[
\frac{V_8}{V_0}=O(|y|^4),
\qquad
\frac{R_V}{V_0}=O(|y|^5).
\]

Choose the RNC radius so that

\[
\left|\frac{V-V_0}{V_0}\right|<\frac12
\]

uniformly. Then

\[
e^{-\rho(V-V_0)}
=
1-\rho V_8-\rho R_V
+O((\rho V_8)^2)
+O(\rho^2|V_8R_V|)
+\cdots
\]

with a uniform dominating exponential.

Every nonlinear term contains at least eight additional powers of `y` beyond the flat contribution and is therefore asymptotically smaller than the `rho^-1/2` term. In particular, the first quadratic pieces are at worst `O(rho^-3/2)` after the full `rho^(3/2)` prefactor.

## 12. Final compact-W1 asymptotic

Combining the explicit degree-four determinant correction, the explicit degree-eight interval-volume correction, and the uniform remainder estimate gives

\[
\boxed{
\mathbb E[B_*\phi(x)]_{W1}
=
-\frac{73\sqrt6}{1575\pi}
C_{abcd}C^{abcd}(x)\rho^{-1/2}
+O(\rho^{-3/4}\log\rho)
}
\]

for Schwarzschild 4D Ricci-flat and fixed compact regulator `phi=1` near `x`.

Since the separately proved compact-`W2` contribution satisfies

\[
\langle B_*\rangle_{W2}=O(\rho^{-1}),
\]

we obtain the internally derived compact-regulated mean asymptotic

\[
\boxed{
\mathbb E[B_*\phi(x)]
=
-\frac{73\sqrt6}{1575\pi}
C_{abcd}C^{abcd}(x)\rho^{-1/2}
+O(\rho^{-3/4}\log\rho)
}
\]

up to the exponentially suppressed/far compact sector treated as in the existing BBD decomposition.

## 13. Allowed status and scope boundary

```text
S4W_W1_NULL_DIRECTION_UNIFORMITY
= INTERNALLY_PROVED_FOR_FIXED_COMPACT_W1

S4W_W1_REMAINDER
= O(rho^-3/4 log rho)

S4W_COMPACT_REGULATED_MEAN_ASYMPTOTIC
= INTERNALLY_DERIVED

S4W_LEADING_COEFFICIENT
= -73 sqrt(6)/(1575 pi)

INDEPENDENT_AUDIT
= STILL_REQUIRED
```

Not established by this note:

- unregulated global `phi=1` on the entire causal past;
- uniform removal of the longitudinal cutoff;
- realization-by-realization convergence;
- finite or controlled variance;
- practical estimator performance;
- horizon localization or Page–Shoom reconstruction;
- novelty/priority.

The central point is that **the null-direction uniformity is obtained from the smooth BBD RNC remainder in `y`, not from a boost-uniform interpretation of Wang's `O(l^9)` term.**
