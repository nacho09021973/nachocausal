"""Figura 4 — Por qué murieron los localizadores: la pared de la caja se come la señal.

Ésta es la figura honesta del expediente de fracasos (`docs/comite/comite_decision_042`,
línea C1–C5).  El observable más natural del orden es el **volumen de futuro**
`|J^+(i)|`.  Parece que debería crecer al acercarse al horizonte.  Y crece un poco.
Pero el efecto dominante no es físico: es que el parche de simulación **termina**, y
un elemento cerca del techo tiene poco futuro por la simple razón de que el techo
está ahí.

El número que lo resume: la altura en la caja explica ~91 % de la varianza de
`|J^+|`; el radio explica ~3 %.  La física está, pero enterrada bajo un artefacto
del aparato.  Condicionando a una banda temporal estrecha reaparece — que es
exactamente el tipo de reparación que el ledger C1–C5 registra como necesaria y que
ninguna de aquellas líneas llegó a cerrar.

Lección para el estudiante: en conjuntos causales finitos, **la frontera de la caja
es un observable**, y compite con la física que se quiere medir.
"""

from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import numpy as np

from causet_core import causal_matrix, future_volume, sprinkle_exterior
from style import AZUL, GRIS, NARANJA, ROJO, usar_estilo

SEMILLA = 11
N = 900
RS = 1.0
T_RANGE = (0.0, 6.0)
R_RANGE = (1.1, 4.0)
BANDA = (2.9, 3.1)


def _corr(a, b):
    return float(np.corrcoef(np.asarray(a, float), np.asarray(b, float))[0, 1])


def construir():
    rng = np.random.default_rng(SEMILLA)
    t, r = sprinkle_exterior(RS, T_RANGE, R_RANGE, N, rng)
    fv = future_volume(causal_matrix(t, r, RS))
    banda = (t > BANDA[0]) & (t < BANDA[1])
    return t, r, fv, banda


def dibujar(salida):
    t, r, fv, banda = construir()
    c_t, c_r = _corr(fv, t), _corr(fv, r)
    c_r_banda = _corr(fv[banda], r[banda])

    usar_estilo()
    fig, (axA, axB, axC) = plt.subplots(1, 3, figsize=(14.0, 4.9))

    # --- A: el campo ---------------------------------------------------------
    sc = axA.scatter(r, t, c=fv, s=16, cmap="viridis", linewidth=0)
    axA.axhspan(BANDA[0], BANDA[1], color=ROJO, alpha=0.18, zorder=0)
    axA.text(R_RANGE[1], np.mean(BANDA), " banda ", ha="right", va="center",
             fontsize=9, color=ROJO)
    axA.set_xlabel("$r$")
    axA.set_ylabel("$t$")
    axA.set_title("A · volumen de futuro $|J^+|$", loc="left", pad=10)
    fig.colorbar(sc, ax=axA, shrink=0.85, label="$|J^+(i)|$")
    axA.text(0.5, 1.0, "el degradado es VERTICAL, no radial",
             transform=axA.transAxes, ha="center", va="baseline",
             fontsize=9.5, color=GRIS)

    # --- B: contra la altura -------------------------------------------------
    axB.scatter(t, fv, s=12, c=AZUL, alpha=0.5, linewidth=0)
    axB.set_xlabel("$t$  (altura en la caja)")
    axB.set_ylabel("$|J^+(i)|$")
    axB.set_title(f"B · artefacto:  $\\rho = {c_t:+.3f}$", loc="left", pad=10)
    axB.text(0.5, 1.0, f"la caja explica el {100 * c_t ** 2:.0f} % de la varianza",
             transform=axB.transAxes, ha="center", va="baseline",
             fontsize=9.5, color=ROJO)

    # --- C: contra el radio --------------------------------------------------
    axC.scatter(r, fv, s=12, c=GRIS, alpha=0.35, linewidth=0, label=f"todo el parche ($\\rho={c_r:+.3f}$)")
    axC.scatter(r[banda], fv[banda], s=42, c=NARANJA, edgecolor="white",
                linewidth=0.6, zorder=3,
                label=f"sólo la banda ($\\rho={c_r_banda:+.3f}$)")
    axC.set_xlabel("$r$  (posición radial)")
    axC.set_ylabel("$|J^+(i)|$")
    axC.set_title("C · la física, enterrada y recuperada", loc="left", pad=10)
    axC.legend(loc="upper left", fontsize=9)

    fig.suptitle("El observable más natural del orden mide, sobre todo, el borde del parche",
                 fontsize=13.5, y=0.99)
    fig.text(0.5, 0.005,
             "Éste es el modo de fallo que mató a los localizadores C1–C5: "
             "la pared de la caja compite con la señal que se busca.",
             ha="center", fontsize=10.5)
    fig.tight_layout(rect=(0, 0.04, 1, 0.93))
    fig.savefig(salida)
    plt.close(fig)
    return salida, c_t, c_r, c_r_banda


if __name__ == "__main__":
    destino = pathlib.Path(__file__).parent / "salida" / "fig04_pared_de_la_caja.png"
    destino.parent.mkdir(exist_ok=True)
    ruta, a, b, c = dibujar(destino)
    print(f"escrita {ruta}")
    print(f"  corr(|J+|, t) = {a:+.3f}   corr(|J+|, r) = {b:+.3f}   "
          f"corr en banda = {c:+.3f}")
