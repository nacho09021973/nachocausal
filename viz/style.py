"""Estilo común de las figuras pedagógicas.

Paleta segura para daltonismo (Okabe–Ito) y tipografía grande: estas figuras están
pensadas para proyectarse en un aula, no para mirarse al 400 % en un PDF.
"""

from __future__ import annotations

import matplotlib as mpl
import numpy as np

# Okabe–Ito
AZUL = "#0072B2"
NARANJA = "#E69F00"
VERDE = "#009E73"
ROJO = "#D55E00"
MORADO = "#CC79A7"
CIELO = "#56B4E9"
AMARILLO = "#F0E442"
GRIS = "#5A5A5A"

HORIZONTE = "#111111"
PUNTO = "#0072B2"


def usar_estilo():
    mpl.rcParams.update({
        "figure.dpi": 130,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.18,
        "grid.linewidth": 0.6,
        "legend.frameon": False,
        "lines.dash_capstyle": "round",
    })


def dibujar_horizonte(ax, rs, etiqueta=True):
    """Línea vertical del horizonte `r = rs`, con la región interior sombreada."""
    ax.axvline(rs, color=HORIZONTE, lw=2.0, zorder=3)
    lo, hi = ax.get_ylim()
    ax.fill_betweenx([lo, hi], 0, rs, color=HORIZONTE, alpha=0.07, zorder=0)
    ax.set_ylim(lo, hi)
    if etiqueta:
        ax.text(rs, hi, "  horizonte  $r=r_s$", ha="left", va="top",
                fontsize=9, color=HORIZONTE, rotation=90)


def dibujar_conos(ax, t, r, rs, escala=0.35, color=GRIS, alpha=0.55):
    """Conos de luz en `(t, r)`: las nulas tienen `dt/dr = ±(1 - rs/r)^{-1}`.

    Se estrechan al acercarse al horizonte — que es *el* dibujo que hay que ver.
    """
    for ti, ri in zip(np.atleast_1d(t), np.atleast_1d(r)):
        pend = 1.0 / (1.0 - rs / ri)
        dr = escala
        dt = pend * dr
        # cono futuro
        ax.plot([ri, ri + dr], [ti, ti + dt], color=color, lw=1.1, alpha=alpha, zorder=2)
        ax.plot([ri, ri - dr], [ti, ti + dt], color=color, lw=1.1, alpha=alpha, zorder=2)


def layout_orden(rel, layer, edges=None, pasadas=6):
    """Posiciones del Hasse derivadas **sólo del orden**, nunca de coordenadas.

    `y` = altura en el orden (contenido real).  `x` = orden dentro de la capa,
    fijado primero por una regla canónica y refinado después por baricentro para
    reducir cruces.  El eje `x` **no transporta información**: es legibilidad, y
    reordenar dentro de una capa no cambia el poset.
    """
    npred = rel.sum(axis=0)
    nsucc = rel.sum(axis=1)
    capas = {int(L): sorted(np.nonzero(layer == L)[0].tolist(),
                            key=lambda i: (int(npred[i]), -int(nsucc[i]), int(i)))
             for L in np.unique(layer)}

    if edges:
        vecinos_arriba = {i: [] for i in range(rel.shape[0])}
        vecinos_abajo = {i: [] for i in range(rel.shape[0])}
        for i, j in edges:
            vecinos_arriba[i].append(j)
            vecinos_abajo[j].append(i)

        def ranking(capa):
            return {nodo: k for k, nodo in enumerate(capa)}

        niveles = sorted(capas)
        for paso in range(pasadas):
            secuencia = niveles[1:] if paso % 2 == 0 else niveles[-2::-1]
            for L in secuencia:
                referencia = ranking(capas[L - 1]) if paso % 2 == 0 else ranking(capas[L + 1])
                lado = vecinos_abajo if paso % 2 == 0 else vecinos_arriba

                def baricentro(nodo):
                    vs = [referencia[v] for v in lado[nodo] if v in referencia]
                    return sum(vs) / len(vs) if vs else -1.0

                capas[L] = sorted(capas[L], key=lambda nodo: (baricentro(nodo), int(nodo)))

    pos = {}
    for L, idx in capas.items():
        k = len(idx)
        for j, i in enumerate(idx):
            x = 0.0 if k == 1 else (j - (k - 1) / 2.0) / max(k - 1, 1) * 2.0
            pos[i] = (x, float(L))
    return pos


def dibujar_hasse(ax, rel, edges, layer, pos=None, color_nodo=PUNTO,
                  valores=None, cmap="viridis", tam=110, borde="white", grosor_borde=1.2):
    """Diagrama de Hasse.  `valores` colorea los nodos por un escalar de orden."""
    if pos is None:
        pos = layout_orden(rel, layer, edges)
    for i, j in edges:
        x0, y0 = pos[i]
        x1, y1 = pos[j]
        ax.plot([x0, x1], [y0, y1], color=GRIS, lw=0.9, alpha=0.55, zorder=1)
    xs = [pos[i][0] for i in range(rel.shape[0])]
    ys = [pos[i][1] for i in range(rel.shape[0])]
    if valores is None:
        ax.scatter(xs, ys, s=tam, c=color_nodo, edgecolor=borde,
                   linewidth=grosor_borde, zorder=3)
        sc = None
    else:
        sc = ax.scatter(xs, ys, s=tam, c=valores, cmap=cmap, edgecolor=borde,
                        linewidth=grosor_borde, zorder=3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for lado in ("left", "bottom"):
        ax.spines[lado].set_visible(False)
    return sc
