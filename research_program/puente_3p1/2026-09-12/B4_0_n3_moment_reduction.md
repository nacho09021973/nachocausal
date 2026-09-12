# B4.0 — Reducción exacta de la ley `n=3` a cuatro momentos

> **STATUS: `ANALYTIC_REDUCTION_VERIFIED / B4_PARKED / N3_RANK_UNRESOLVED`.**

Sea `nu=mu/mu(K)` y, para un punto radial-angular `x`,

```text
f(x)=nu(J^+(x) cap K),
p(x)=nu(J^-(x) cap K).
```

Por intercambio de dos iid y ausencia de empates de medida positiva,
`E[f]=E[p]=rho/2`.

## Identidades exactas

Con `A` antichain, `E` una relación, `V` un mínimo con dos máximos, `Lambda` dos mínimos con un
máximo y `C` cadena de tres,

```text
P_C      = 6 E[p f]
P_V      = 3 E[f^2] - P_C
P_Lambda = 3 E[p^2] - P_C
P_E      = 3 rho - 6 E[f^2] - 6 E[p^2] + 6 E[p f]
P_A      = 1 - 3 rho + 3 E[f^2] + 3 E[p^2]
```

La razón de `P_C` es la elección del orden pasado–medio–futuro (`3!`). Para `V` y `Lambda`,
`3 E[f²]` y `3 E[p²]` cuentan además las cadenas, que se restan una vez. La ecuación para
`P_E` usa el número esperado de pares comparables:

```text
P_E + 2 P_V + 2 P_Lambda + 3 P_C = 3 rho.
```

## Consecuencia diferencial

Definiendo

```text
m=(rho, E[f^2], E[p^2], E[p f]),
q=(P_E,P_V,P_Lambda,P_C),
```

se tiene `q=T m`, con

```text
T = [[3,-6,-6, 6], [0,3,0,-6], [0,0,3,-6], [0,0,0,6]],
det(T)=162.
```

Por tanto `rowspan Dq = rowspan Dm` exactamente. El test de rango de B4 puede trabajar con `Dm`:

```text
rank Dm = 3                         => rango físico completo a n=3;
dphi in rowspan(Dm)                 => phi localmente identificable a n=3;
exists v: Dm v=0, dphi(v)!=0       => n=3 insuficiente para phi.
```

## Gobernanza

```text
B4.0_N3_MOMENT_REDUCTION = VERIFIED
B4_SPECIFICATION = AUTHORIZED
B4_EXECUTION = PARKED
```

La reducción evita una integral inicial sobre `K^3`, pero B4 queda aparcado hasta disponer de una
cuadratura certificada con resto formal para las integrales concretas de B4.3. El terminal débil
sigue siendo sólo de primer orden.

La primera ejecución preliminar queda documentada en `verification_b4_execution.json` y es
`B4_INCONCLUSIVE_BY_BOUNDS`: el menor numérico no está acompañado aún por una envolvente
certificada.
