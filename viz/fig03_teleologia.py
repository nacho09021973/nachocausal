"""Figura 3 — Lo que pasa fuera del parche no está en el parche (Teorema 3.2).

Un elemento `e` es maximal en el parche observado.  ¿Es maximal *de verdad*, o hay
algo por encima que simplemente no hemos visto?  **El parche no lo sabe y no puede
saberlo**, y ésa es la razón por la que el horizonte de eventos global —que es una
noción teleológica: depende de todo el futuro— no es un funcional de un parche finito.

La construcción es exacta y físicamente realizable, no un esquema: los dos elementos
añadidos son puntos legítimos del mismo sprinkling en una banda temporal posterior.
Uno cae en el futuro causal de `e`, el otro es espacialoide respecto de `e`.  El
subposet inducido sobre el parche es **idéntico** en ambos casos, y el script lo
verifica antes de dibujar.

Núcleo formal correspondiente: `dev/PR003_INFINITE_MAXIMALITY_NONCERTIFIABILITY.md`
(`VERDICT = PROVED`), del que esta figura es la sombra finita y dibujable.
"""

from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import numpy as np

from causet_core import causal_matrix, hasse_edges, layer_of, sprinkle_exterior
from style import (AZUL, GRIS, MORADO, ROJO, VERDE, layout_orden, usar_estilo)

SEMILLA = 2718
N = 9
RS = 1.0
T_RANGE = (0.0, 3.2)
R_RANGE = (1.2, 3.0)
BANDA_EXTRA = (3.2, 5.2)


def _maximales(rel):
    return np.nonzero(~rel.any(axis=1))[0]


def construir():
    """Devuelve el parche, el testigo `e`, y las dos continuaciones."""
    rng = np.random.default_rng(SEMILLA)
    t, r = sprinkle_exterior(RS, T_RANGE, R_RANGE, N, rng)
    rel = causal_matrix(t, r, RS)

    maxs = _maximales(rel)
    # testigo: el maximal con más pasado, para que se vea bien colocado
    e = int(maxs[np.argmax(rel[:, maxs].sum(axis=0))])

    # buscamos, en la banda posterior, un punto EN el futuro de e y otro espacialoide
    arriba = abajo = None
    for _ in range(4000):
        tq, rq = sprinkle_exterior(RS, BANDA_EXTRA, R_RANGE, 1, rng)
        t_ext = np.append(t, tq)
        r_ext = np.append(r, rq)
        rel_ext = causal_matrix(t_ext, r_ext, RS)
        if rel_ext[e, N] and arriba is None:
            arriba = (float(tq[0]), float(rq[0]), rel_ext)
        if (not rel_ext[e, N]) and abajo is None:
            abajo = (float(tq[0]), float(rq[0]), rel_ext)
        if arriba and abajo:
            break
    if not (arriba and abajo):
        raise RuntimeError("no se hallaron ambas continuaciones")

    # verificación dura: el parche inducido debe ser idéntico en ambas
    for nombre, (_, _, rel_ext) in (("A", arriba), ("B", abajo)):
        if not np.array_equal(rel_ext[:N, :N], rel):
            raise AssertionError(f"la continuación {nombre} alteró el parche observado")

    return t, r, rel, e, arriba, abajo


def _panel(ax, rel_ext, n_patch, e, titulo, nuevo_es_futuro, pos_base=None):
    layer = layer_of(rel_ext)
    edges = hasse_edges(rel_ext)
    pos = layout_orden(rel_ext, layer, edges)
    if pos_base is not None:
        for i in range(n_patch):
            pos[i] = pos_base[i]
    for i, j in edges:
        x0, y0 = pos[i]
        x1, y1 = pos[j]
        nuevo = (i >= n_patch) or (j >= n_patch)
        ax.plot([x0, x1], [y0, y1], color=MORADO if nuevo else GRIS,
                lw=1.8 if nuevo else 1.0, alpha=0.9 if nuevo else 0.5,
                zorder=2 if nuevo else 1)
    for i in range(rel_ext.shape[0]):
        if i >= n_patch:
            col, tam = MORADO, 210
        elif i == e:
            col, tam = ROJO, 190
        else:
            col, tam = AZUL, 130
        ax.scatter(*pos[i], s=tam, c=col, edgecolor="white", linewidth=1.4, zorder=3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for lado in ("left", "bottom"):
        ax.spines[lado].set_visible(False)
    ax.set_title(titulo, loc="left", pad=10)
    veredicto = "$e$ NO es maximal" if nuevo_es_futuro else "$e$ SÍ es maximal"
    ax.text(0.5, -0.02, veredicto, transform=ax.transAxes, ha="center", va="top",
            fontsize=12, color=ROJO if nuevo_es_futuro else VERDE, weight="bold")
    return pos


def dibujar(salida):
    t, r, rel, e, arriba, abajo = construir()

    usar_estilo()
    fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(13.0, 5.2))

    layer = layer_of(rel)
    edges = hasse_edges(rel)
    pos0 = layout_orden(rel, layer, edges)
    for i, j in edges:
        x0, y0 = pos0[i]
        x1, y1 = pos0[j]
        ax0.plot([x0, x1], [y0, y1], color=GRIS, lw=1.0, alpha=0.5, zorder=1)
    for i in range(len(t)):
        col = ROJO if i == e else AZUL
        ax0.scatter(*pos0[i], s=190 if i == e else 130, c=col,
                    edgecolor="white", linewidth=1.4, zorder=3)
    ax0.set_xticks([])
    ax0.set_yticks([])
    ax0.grid(False)
    for lado in ("left", "bottom"):
        ax0.spines[lado].set_visible(False)
    ax0.set_title("lo que observamos: el parche", loc="left", pad=10)
    ax0.text(0.5, -0.02, "$e$ es maximal AQUÍ DENTRO", transform=ax0.transAxes,
             ha="center", va="top", fontsize=12, color=GRIS, weight="bold")

    _panel(ax1, arriba[2], len(t), e, "continuación 1 (legítima)",
           nuevo_es_futuro=True, pos_base=pos0)
    _panel(ax2, abajo[2], len(t), e, "continuación 2 (igual de legítima)",
           nuevo_es_futuro=False, pos_base=pos0)

    todas = [ax0, ax1, ax2]
    lo_y = min(ax.get_ylim()[0] for ax in todas)
    hi_y = max(ax.get_ylim()[1] for ax in todas)
    lo_x = min(ax.get_xlim()[0] for ax in todas)
    hi_x = max(ax.get_xlim()[1] for ax in todas)
    for ax in todas:
        ax.set_ylim(lo_y, hi_y)
        ax.set_xlim(lo_x, hi_x)

    fig.suptitle("El mismo parche admite futuros que se contradicen",
                 fontsize=13.5, y=0.98)
    fig.text(0.5, 0.045,
             "El subposet azul es idéntico en los tres paneles — verificado elemento a elemento. "
             "Sólo cambia el punto morado, que está fuera de lo observado.",
             ha="center", fontsize=10, color=GRIS)
    fig.text(0.5, 0.005,
             "Teorema 3.2: el horizonte de eventos global no es medible respecto de los datos "
             "de un parche finito.",
             ha="center", fontsize=11)
    fig.tight_layout(rect=(0, 0.075, 1, 0.94))
    fig.savefig(salida)
    plt.close(fig)
    return salida


if __name__ == "__main__":
    destino = pathlib.Path(__file__).parent / "salida" / "fig03_teleologia.png"
    destino.parent.mkdir(exist_ok=True)
    print("escrita", dibujar(destino))
