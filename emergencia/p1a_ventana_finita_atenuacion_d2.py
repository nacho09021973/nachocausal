"""Atenuación de ventana finita: el objetivo poblacional de `fig04` y su sesgo en `n`.

Determinista. Calcula por **cuadratura**, sin sortear un solo punto, el objetivo
poblacional que la correlación muestral de `viz/fig04_box_wall.py` estima, y el factor
de atenuación finito que separa una de otro.

Resultado que implementa (`emergencia/P1a_ventana_finita_atenuacion.md`, Prop. 1):
condicionado a la posición de `x` y al total `N = n`, los otros `n-1` elementos son iid
uniformes por volumen en la ventana `W`, luego

    K = |J^+(x)|  |  x,N=n   ~   Binomial(n-1, P),      P = Vol(J^+(x) cap W)/Vol(W),

y de la descomposición de varianza se sigue, exactamente,

    Var(K)       = (n-1)^2 Var(P) + (n-1) E[P(1-P)]
    Corr(K,P)    = A(n)
    Corr(K,T)    = Corr(P,T) * A(n),        A(n) = (1 + E[P(1-P)]/((n-1)Var(P)))^(-1/2)

con `T = t(X)`. Ambas correlaciones comparten el **mismo** factor, `1 - A(n) = O(1/n)`.

Lo que NO calcula: nada sobre el elemento *seleccionado* por un argmax sobre el causet
completo. Allí la ley binomial deja de aplicar y el fenómeno es de extremos, distinto
de éste (ver el documento, §5).

    PYTHONDONTWRITEBYTECODE=1 python3 emergencia/p1a_ventana_finita_atenuacion_d2.py

No escribe en `resultados/`, no toca el sello y no consume la banda de semillas
reservada `[2 000 000 - 2 999 999]`.
"""

from __future__ import annotations

import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "viz"))

from causet_core import (causal_matrix, future_volume,  # noqa: E402
                         sprinkle_exterior, tortoise)

RS = 1.0
SEMILLA = 20260807          # fuera de la banda reservada [2_000_000, 2_999_999]

# Ventana de `viz/fig04_box_wall.py`, y dos variantes para exhibir que el objetivo es
# un funcional de la ventana y no una constante universal.
VENTANAS = {
    "fig04  t[0,6] r[1.1,4.0]": ((0.0, 6.0), (1.1, 4.0)),
    "alta   t[0,12] r[1.1,4.0]": ((0.0, 12.0), (1.1, 4.0)),
    "baja   t[0,3] r[1.1,4.0]": ((0.0, 3.0), (1.1, 4.0)),
    "ancha  t[0,6] r[1.1,8.0]": ((0.0, 6.0), (1.1, 8.0)),
}
ENES = (225, 900, 3600, 14400)


def momentos(t_rango, r_rango, nt=1601, nr=1201):
    """Momentos de `P` y `T` sobre la ventana, por cuadratura trapezoidal.

    `det g = -1`, luego la forma de volumen es `dt dr` y `X` es uniforme en el
    rectángulo: los momentos son integrales con peso constante.
    """
    (t0, t1), (r0, r1) = t_rango, r_rango
    tg = np.linspace(t0, t1, nt)
    rg = np.linspace(r0, r1, nr)
    rs_g = tortoise(rg, RS)

    P = np.empty((nt, nr))
    for j in range(nr):
        borde = tg[:, None] + np.abs(rs_g[None, :] - rs_g[j])
        alto = np.clip(t1 - np.clip(borde, t0, t1), 0.0, None)
        P[:, j] = np.trapz(alto, rg, axis=1) / ((t1 - t0) * (r1 - r0))

    wt = np.ones(nt); wt[0] = wt[-1] = 0.5
    wr = np.ones(nr); wr[0] = wr[-1] = 0.5
    W = np.outer(wt, wr); W /= W.sum()
    med = lambda f: float((W * f).sum())            # noqa: E731

    Tm = np.broadcast_to(tg[:, None], P.shape)
    EP, EP2 = med(P), med(P * P)
    ET, ET2 = med(Tm), med(Tm * Tm)
    var_P, var_T = EP2 - EP ** 2, ET2 - ET ** 2
    return dict(EP=EP, var_P=var_P, EP1P=EP - EP2, P_min=float(P.min()),
                corr_PT=(med(P * Tm) - EP * ET) / np.sqrt(var_P * var_T))


def atenuacion(m, n):
    return (1.0 + m["EP1P"] / ((n - 1) * m["var_P"])) ** -0.5


def p_de(t0, r0, t_rango, r_rango, nr=4001):
    (ta, tb), (ra, rb) = t_rango, r_rango
    rg = np.linspace(ra, rb, nr)
    borde = t0 + np.abs(tortoise(rg, RS) - tortoise(np.array([r0]), RS)[0])
    return float(np.trapz(np.clip(tb - np.clip(borde, ta, tb), 0.0, None), rg)
                 / ((tb - ta) * (rb - ra)))


# --------------------------------------------------------------------------- #
print("=" * 92)
print("BLOQUE A — objetivos poblacionales por CUADRATURA (ningún punto sorteado)")
print("=" * 92)
print(f"{'ventana':<26} {'E[P]':>9} {'Var(P)':>11} {'E[P(1-P)]':>11} {'Corr(p,t)':>11} {'min p':>9}")
M = {}
for nombre, (tr, rr) in VENTANAS.items():
    M[nombre] = m = momentos(tr, rr)
    print(f"{nombre:<26} {m['EP']:>9.6f} {m['var_P']:>11.4e} {m['EP1P']:>11.6f} "
          f"{m['corr_PT']:>+11.6f} {m['P_min']:>9.2e}")

principal = next(iter(VENTANAS))
print()
print(f"OBJETIVO DE fig04:  Corr(p(X), t(X)) = {M[principal]['corr_PT']:+.6f}")
print("El objetivo es un FUNCIONAL DE LA VENTANA: cambia con la razón de aspecto, luego")
print("no es una constante de los conjuntos causales sino del diseño del experimento.")

# Control de convergencia: dos mallas distintas deben coincidir.
grueso = momentos(*VENTANAS[principal], nt=801, nr=601)
d = abs(grueso["corr_PT"] - M[principal]["corr_PT"])
print(f"\nCONTROL malla 801x601 vs 1601x1201:  |Delta Corr(p,t)| = {d:.2e}",
      "OK" if d < 1e-4 else "FALLA")

# --------------------------------------------------------------------------- #
print()
print("=" * 92)
print("BLOQUE B — atenuación finita (identidad exacta, sin datos)")
print("=" * 92)
m = M[principal]
print(f"{'n':>7} {'A(n)':>11} {'1-A(n)':>11} {'Corr(K,T) = Corr(p,t)*A':>26}")
for n in ENES:
    A = atenuacion(m, n)
    print(f"{n:>7} {A:>11.6f} {1 - A:>11.2e} {m['corr_PT'] * A:>+26.6f}")
print("\n1-A(n) escala como 1/n aunque la fluctuación relativa condicional de K sea")
print("O(n^-1/2): la correlación es un cociente de momentos segundos y el ruido entra")
print("en varianza, no en desviación típica.")

# --------------------------------------------------------------------------- #
print()
print("=" * 92)
print("BLOQUE C — control de la premisa: E[K | x] = (n-1) p(x)")
print("=" * 92)
print("Falsable: si la cuadratura de p o la geometría discreparan, este bloque falla.")
rng = np.random.default_rng(SEMILLA)
tr, rr = VENTANAS[principal]
n_ctrl, reps = 400, 300
print(f"{'x = (t,r)':>16} {'p(x) cuadratura':>17} {'E[K]/(n-1) simulado':>21} {'|dif|':>10}")
peor = 0.0
for t0, r0 in ((1.0, 1.5), (3.0, 2.5), (5.0, 3.5)):
    p = p_de(t0, r0, tr, rr)
    conteos = []
    for _ in range(reps):
        t, r = sprinkle_exterior(RS, tr, rr, n_ctrl - 1, rng)
        t = np.append(t, t0); r = np.append(r, r0)
        conteos.append(future_volume(causal_matrix(t, r, RS))[-1])
    emp = float(np.mean(conteos)) / (n_ctrl - 1)
    peor = max(peor, abs(emp - p))
    print(f"{f'({t0:.1f}, {r0:.1f})':>16} {p:>17.6f} {emp:>21.6f} {abs(emp - p):>10.2e}")
tol = 3.0 * np.sqrt(0.25 / ((n_ctrl - 1) * reps))     # 3 SE binomiales, cota holgada
print(f"\nCONTROL peor |dif| = {peor:.2e}  frente a 3 SE = {tol:.2e}: ",
      "OK" if peor < tol else "FALLA")

# --------------------------------------------------------------------------- #
print()
print("=" * 92)
print("ESTADO DE CONTROL")
print("=" * 92)
print(f"""FINITE_WINDOW_TARGET_fig04 = {M[principal]['corr_PT']:+.6f}  (cuadratura)
TARGET_IS_WINDOW_FUNCTIONAL = YES ({len(VENTANAS)} ventanas evaluadas, valores distintos)
ATTENUATION_IS_EXACT_IDENTITY = YES (Prop. 1; no requiere iid entre elementos)
ATTENUATION_ORDER = O(1/n)
BINOMIAL_PREMISE_CONTROL = {'PASS' if peor < tol else 'FAIL'}
SAMPLING_TABLE_STATUS = CONTROL_ONLY_SINGLE_REALISATION_NOT_A_TEST
SELECTOR_REGIME = OUT_OF_SCOPE_ARGMAX_BREAKS_THE_BINOMIAL_LAW
NEW_STOCHASTIC_DATA_WRITTEN = NO
SEED_BAND_CONSUMED = NO (semilla {SEMILLA})
SEAL_TOUCHED = NO""")
