# B1.2 — Alcance causal angular 3+1D en la carta de Kruskal

> **STATUS: `DERIVED / DETERMINISTIC_CHECKS_ONLY / NO_RUNS / NO_SEEDS / NO_PAIR_SEARCH`.**
> **ADVANCES:** `L3`, únicamente mediante la relación causal angular necesaria para evaluar
> posteriormente `rho(lambda)`.

**Fecha:** 2026-09-12  
**Dependencia:** `research_program/synthesis/op11_spherical_dual_target.md` §2 y
`research_program/puente_3p1/2026-09-12/B1/B1_par_testigo_lambda.md` §6–§7.

## 1. Convenciones

En el sector `V>0` de la familia congelada, escribimos

```text
-U V = (s-1) exp(s),       s = r/(2M) > 0,
ds² = -C(UV) dU dV + r² dOmega²,
C(UV) = 32 M³/r · exp(-s).
```

La rama `s>0` es única porque `d[(s-1)e^s]/ds = s e^s > 0`. La orientación futura en el
sector `I union II` permite usar curvas con `U` y `V` no decrecientes. Para dos puntos
`x=(Ux,Vx,omega_x)` y `y=(Uy,Vy,omega_y)` de `K^+`, si `Ux>Uy` o `Vx>Vy`, no hay curva
futura causal `x -> y`.

Definimos la distancia angular esférica

```text
Delta = arccos(omega_x · omega_y) in [0, pi].
```

## 2. Reducción exacta a un problema variacional

Para una curva radial monótona `gamma: V -> U(V)` entre los extremos, el término radial es
`-C U'(V)dV²`, y una curva causal con movimiento angular `alpha(V)` satisface

```text
r² |alpha'(V)|² <= C(U(V)V) U'(V).
```

Por tanto, el máximo desplazamiento angular permitido por esa curva radial es

```text
L[U] = integral_{Vx}^{Vy} q(U(V)V) sqrt(U'(V)) dV,
q(s) = exp(-s/2)/sqrt(s).
```

La relación causal angular exacta es entonces

```text
x prec y  <=>  Ux <= Uy, Vx <= Vy,
              Delta <= Delta_max(x,y),

Delta_max(x,y) = min(pi, sup_U L[U]),
```

donde el supremo recorre `U` absolutamente continuas, no decrecientes, con
`U(Vx)=Ux`, `U(Vy)=Uy`, y cuyos valores permanecen en el rectángulo causal entre los extremos.
La última restricción no introduce un efecto de borde del patch: toda curva futura monótona entre
los extremos ya permanece en ese rectángulo del sector de Kruskal. La igualdad `Delta=...`
corresponde a una curva nula; para la probabilidad con medida continua, las fronteras de igualdad
son despreciables.

La derivación usa sólo la desigualdad causal local y la existencia de la geodésica mínima de
`S²` entre los dos ángulos. No usa sprinkling ni una selección de puntos.

## 3. Cotas rigurosas cerradas

Sea `dU=Uy-Ux >= 0`, `dV=Vy-Vx >= 0` y

```text
q_min <= q(UV) <= q_max
```

en el rectángulo causal. Entonces, por Cauchy–Schwarz,

```text
Delta_max <= min(pi, q_max sqrt(dU dV)).                 (UB)
```

Una trayectoria admisible explícita es la recta

```text
U_lin(V) = Ux + dU (V-Vx)/dV,
```

que proporciona la cota inferior determinista

```text
Delta_max >= min(pi, integral q(U_lin(V)V) sqrt(dU/dV) dV).  (LB)
```

Si `dU=0` o `dV=0`, ambas cotas son cero. El `q_max` de (UB) se obtiene sin búsqueda numérica:
como `q` decrece estrictamente con `s` y `s` crece con `-UV`, se evalúa `q` en el menor `s` del
rectángulo, equivalente al mayor producto `UV` entre sus cuatro esquinas. El patch congelado
impone `U V <= 1-epsilon_s`, por lo que `q_max` es finito.

Estas cotas son conservadoras pero válidas para cualquier par del patch. La expresión variacional
de §2 es el criterio exacto; la LB/UB permite una decisión certificada cuando `Delta` queda por
debajo de LB (causal) o por encima de UB (no causal), sin resolver una optimización.

## 4. Qué queda deliberadamente fuera

Este artefacto no calcula `rho(lambda)`, no escoge `lambda_0,lambda_1`, no barre `lambda`, no
inspecciona curvas de `rho`, y no afirma `L3` ni reconstrucción. B1.3 queda cerrado fuera de este
paso y requerirá congelar primero el par testigo.

## 5. Verificación determinista

`verify_angular_causal_reach.py` comprueba:

1. la identidad algebraica `C/r² = q(s)²`;
2. que la trayectoria recta respeta las cotas `LB <= UB` en casos fijos;
3. que el caso radial (`Delta=0`) y los casos degenerados dan `Delta_max=0`;
4. la monotonicidad usada para localizar `q_max` en las esquinas.

La verificación usa sólo aritmética determinista y cuadratura fija de SciPy; no hay semillas,
Monte Carlo, ajuste, búsqueda adaptativa ni datos generados.
