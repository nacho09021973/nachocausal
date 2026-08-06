"""Figura 1 — El diccionario: del continuum al orden.

Es la figura que le falta al campo.  La relatividad general tiene la malla elástica;
los conjuntos causales se dibujan o como puntos en Minkowski con conos, o como un
Hasse abstracto, y ninguno de los dos explica **qué se tira a la basura** al pasar de
uno al otro.  Aquí se ve: los dos paneles tienen los mismos elementos y las mismas
relaciones; el derecho ha perdido las coordenadas, y nada más.

`order-only` = trabajar sólo con el panel B, sin poder mirar nunca el A.
"""

from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import numpy as np

from causet_core import (causal_matrix, future_volume, hasse_edges, layer_of,
                         sprinkle_exterior, tortoise)
from style import (AZUL, GRIS, ROJO, VERDE, dibujar_conos, dibujar_hasse,
                   dibujar_horizonte, layout_orden, usar_estilo)

SEMILLA = 31415
N = 13
RS = 1.0
T_RANGE = (0.0, 5.0)
R_RANGE = (1.15, 3.2)


def construir():
    rng = np.random.default_rng(SEMILLA)
    t, r = sprinkle_exterior(RS, T_RANGE, R_RANGE, N, rng)
    rel = causal_matrix(t, r, RS)
    # testigo: el elemento con pasado y futuro más equilibrados, para que la
    # figura muestre las tres clases (pasado, futuro, incomparables) a la vez
    fut = rel.sum(axis=1)
    pas = rel.sum(axis=0)
    p = int(np.argmax(np.minimum(fut, pas)))
    return t, r, rel, p


def colores(rel, p, n):
    c = np.array([GRIS] * n, dtype=object)
    c[rel[p]] = VERDE           # futuro estricto de p
    c[rel[:, p]] = AZUL         # pasado estricto de p
    c[p] = ROJO
    return c


def dibujar(salida):
    t, r, rel, p = construir()
    n = len(t)
    c = colores(rel, p, n)

    usar_estilo()
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.6, 5.4))

    # --- A: el continuum ----------------------------------------------------
    axA.set_xlim(0.0, 3.5)
    axA.set_ylim(T_RANGE[0] - 0.35, T_RANGE[1] + 0.35)
    dibujar_horizonte(axA, RS, etiqueta=False)
    axA.text(RS, T_RANGE[0] - 0.30, "  horizonte $r=r_s$", ha="left", va="bottom",
             fontsize=9, color="#111111", rotation=90)
    # región de futuro causal de p, sombreada: t >= t_p + |r*(r) - r*(p)|
    rr = np.linspace(R_RANGE[0] - 0.04, 3.5, 400)
    frontera = t[p] + np.abs(tortoise(rr, RS) - tortoise(r[p], RS))
    axA.fill_between(rr, frontera, T_RANGE[1] + 0.35, color=VERDE, alpha=0.10, zorder=0)
    axA.plot(rr, frontera, color=VERDE, lw=1.4, alpha=0.85, zorder=2)
    for i in range(n):
        axA.scatter(r[i], t[i], s=95, c=c[i], edgecolor="white", linewidth=1.2, zorder=4)
    axA.scatter([], [], s=95, c=ROJO, label="el elemento $p$")
    axA.scatter([], [], s=95, c=VERDE, label="su futuro $J^+(p)$")
    axA.scatter([], [], s=95, c=AZUL, label="su pasado $J^-(p)$")
    axA.scatter([], [], s=95, c=GRIS, label="ni una cosa ni otra")
    axA.plot([], [], color=VERDE, lw=1.4, label="borde del cono de $p$")
    axA.legend(loc="upper left", fontsize=9.0, handletextpad=0.3)
    axA.set_xlabel("$r$")
    axA.set_ylabel("$t$")
    axA.set_title("A · lo que ve quien tiene coordenadas", loc="left", pad=10)

    # --- B: el orden --------------------------------------------------------
    layer = layer_of(rel)
    edges = hasse_edges(rel)
    pos = layout_orden(rel, layer, edges)
    for i, j in edges:
        x0, y0 = pos[i]
        x1, y1 = pos[j]
        axB.plot([x0, x1], [y0, y1], color=GRIS, lw=1.0, alpha=0.5, zorder=1)
    for i in range(n):
        axB.scatter(*pos[i], s=150, c=c[i], edgecolor="white", linewidth=1.4, zorder=3)
    axB.set_xticks([])
    axB.set_yticks([])
    axB.grid(False)
    for lado in ("left", "bottom"):
        axB.spines[lado].set_visible(False)
    axB.set_title("B · lo que ve el orden, y nada más", loc="left", pad=10)
    axB.text(0.5, -0.02,
             "mismos elementos, mismas relaciones, ninguna coordenada",
             transform=axB.transAxes, ha="center", va="top", fontsize=10, color=GRIS)

    fig.suptitle("Qué se pierde al pasar del espaciotiempo al conjunto causal",
                 fontsize=13.5, y=0.98)
    fig.text(0.5, 0.005,
             "La altura vertical en B es la altura en el orden. La posición horizontal "
             "sólo evita cruces: no significa nada.",
             ha="center", fontsize=9.5, color=GRIS)
    fig.tight_layout(rect=(0, 0.03, 1, 0.94))
    fig.savefig(salida)
    plt.close(fig)
    return salida


if __name__ == "__main__":
    destino = pathlib.Path(__file__).parent / "salida" / "fig01_diccionario.png"
    destino.parent.mkdir(exist_ok=True)
    print("escrita", dibujar(destino))
