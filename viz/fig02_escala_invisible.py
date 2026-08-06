"""Figura 2 — Teorema 3.1: la escala absoluta es invisible al orden.

Idea pedagógica en una frase: **en Schwarzschild 1+1, cambiar la masa es exactamente
cambiar las unidades**, y el orden no sabe leer las unidades.

Los cuatro paneles cuentan el argumento entero:

  A  parche con horizonte `r_s = 1`, con sus propios ejes;
  B  su imagen por `Phi_s(t,r) = (st, sr)` con `r_s = 2`, con sus propios ejes
     — misma forma, otras etiquetas;
  C  los dos parches sobre **ejes comunes**: son objetos distintos, y un observador
     con coordenadas los distingue de un vistazo;
  D  el diagrama de Hasse: **uno solo**, porque ambos inducen literalmente el mismo
     poset etiquetado.

Honestidad del dibujo (importa, y va en el pie de figura del paper)
-------------------------------------------------------------------
La identidad del panel D es **por construcción**: `Phi_s` es un isomorfismo de orden,
de modo que el mismo conjunto de puntos, transportado, es un sprinkling legítimo del
otro modelo con las mismas relaciones.  Lo que hace el Teorema 3.1 es convertir esa
construcción en **genérica**: como `Phi_s` lleva la ley del sprinkling a la ley del
sprinkling, las leyes de los posets no etiquetados coinciden y `TV = 0`.

Lo que esta figura NO dice: que dos sprinklings *independientes* a masas distintas
salgan iguales.  No salen.  Salen con la **misma distribución**, que es justamente lo
que impide a cualquier estimador distinguirlos.
"""

from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import numpy as np

from causet_core import (causal_matrix, check_dilation_identity, dilate,
                         hasse_edges, layer_of, sprinkle_exterior)
from style import AZUL, NARANJA, dibujar_conos, dibujar_hasse, dibujar_horizonte, usar_estilo

SEMILLA = 20260806
N = 12
RS_A = 1.0
S = 2.0
T_RANGE = (0.0, 5.0)
R_RANGE = (1.15, 3.0)


def construir():
    rng = np.random.default_rng(SEMILLA)
    t_a, r_a = sprinkle_exterior(RS_A, T_RANGE, R_RANGE, N, rng)
    t_b, r_b, rs_b = dilate(t_a, r_a, RS_A, S)

    rel_a = causal_matrix(t_a, r_a, RS_A)
    rel_b = causal_matrix(t_b, r_b, rs_b)
    identicas, discrepancias = check_dilation_identity(t_a, r_a, RS_A, S)
    if not identicas:
        raise AssertionError(
            f"Phi_s no preservó el orden ({discrepancias} discrepancias): "
            "la figura afirmaría algo falso, así que no se dibuja."
        )
    return (t_a, r_a, rel_a), (t_b, r_b, rs_b, rel_b), discrepancias


def dibujar(salida):
    (t_a, r_a, rel_a), (t_b, r_b, rs_b, rel_b), discrepancias = construir()

    usar_estilo()
    fig, axes = plt.subplots(2, 2, figsize=(11.0, 8.6))
    axA, axB, axC, axD = axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1]

    # --- A: modelo original -------------------------------------------------
    axA.set_xlim(0.0, 3.4)
    axA.set_ylim(T_RANGE[0] - 0.3, T_RANGE[1] + 0.3)
    dibujar_horizonte(axA, RS_A)
    dibujar_conos(axA, t_a[:5], r_a[:5], RS_A, escala=0.22)
    axA.scatter(r_a, t_a, s=46, c=AZUL, edgecolor="white", linewidth=1.0, zorder=4)
    axA.set_xlabel("$r$")
    axA.set_ylabel("$t$")
    axA.set_title(f"A · masa pequeña:  $r_s = {RS_A:g}$", loc="left", pad=22)

    # --- B: modelo dilatado -------------------------------------------------
    axB.set_xlim(0.0, 3.4 * S)
    axB.set_ylim(T_RANGE[0] * S - 0.6, T_RANGE[1] * S + 0.6)
    dibujar_horizonte(axB, rs_b)
    dibujar_conos(axB, t_b[:5], r_b[:5], rs_b, escala=0.22 * S)
    axB.scatter(r_b, t_b, s=46, c=NARANJA, edgecolor="white", linewidth=1.0, zorder=4)
    axB.set_xlabel("$r$")
    axB.set_ylabel("$t$")
    axB.set_title(f"B · masa doble:  $r_s = {rs_b:g}$   (imagen por $\\Phi_s$, $s={S:g}$)",
                  loc="left", pad=22)
    axB.text(0.5, 1.0, "misma figura que A: sólo cambian las etiquetas de los ejes",
             transform=axB.transAxes, ha="center", va="baseline", fontsize=9, color="#5A5A5A")

    # --- C: ejes comunes ----------------------------------------------------
    axC.set_xlim(0.0, 3.4 * S)
    axC.set_ylim(T_RANGE[0] * S - 0.6, T_RANGE[1] * S + 0.6)
    axC.axvline(RS_A, color="#111111", lw=2.0, zorder=3)
    axC.axvline(rs_b, color="#111111", lw=2.0, zorder=3)
    axC.text(RS_A, T_RANGE[0] * S - 0.4, " $r_s=1$", ha="left", va="bottom",
             fontsize=9, color="#111111", rotation=90)
    axC.text(rs_b, T_RANGE[0] * S - 0.4, " $r_s=2$", ha="left", va="bottom",
             fontsize=9, color="#111111", rotation=90)
    axC.scatter(r_a, t_a, s=46, c=AZUL, edgecolor="white", linewidth=1.0,
                zorder=4, label=f"$r_s={RS_A:g}$")
    axC.scatter(r_b, t_b, s=46, c=NARANJA, edgecolor="white", linewidth=1.0,
                zorder=4, label=f"$r_s={rs_b:g}$")
    axC.legend(loc="upper left", fontsize=10)
    axC.set_xlabel("$r$")
    axC.set_ylabel("$t$")
    axC.set_title("C · sobre ejes comunes son distintos", loc="left", pad=22)
    axC.text(0.5, 1.0, "esto lo distingue quien tiene coordenadas",
             transform=axC.transAxes, ha="center", va="bottom", fontsize=9, color="#5A5A5A")

    # --- D: el poset, uno solo ---------------------------------------------
    layer = layer_of(rel_a)
    dibujar_hasse(axD, rel_a, hasse_edges(rel_a), layer, color_nodo=AZUL,
                  borde=NARANJA, grosor_borde=2.6, tam=170)
    axD.set_title("D · el orden que ambos inducen", loc="left", pad=22)
    axD.text(0.5, 1.0,
             "cada nodo es a la vez un punto de A (relleno) y uno de B (anillo)",
             transform=axD.transAxes, ha="center", va="bottom", fontsize=9, color="#5A5A5A")
    axD.text(0.5, -0.04,
             f"idéntico elemento a elemento: {discrepancias} discrepancias "
             f"en {N}×{N} relaciones",
             transform=axD.transAxes, ha="center", va="top", fontsize=9.5, color="#5A5A5A")

    fig.suptitle(
        "En Schwarzschild 1+1, cambiar la masa es cambiar las unidades — y el orden no lee unidades",
        fontsize=13.5, y=0.985)
    fig.text(0.5, 0.005,
             "Teorema 3.1:  $\\mathrm{TV}\\left(P_n(r_s;P),\\,P_n(s\\,r_s;\\Phi_s(P))\\right) = 0$ "
             "para todo $n$ y todo $s>0$.",
             ha="center", fontsize=11)
    fig.tight_layout(rect=(0, 0.022, 1, 0.965))
    fig.savefig(salida)
    plt.close(fig)
    return salida, discrepancias


if __name__ == "__main__":
    destino = pathlib.Path(__file__).parent / "salida" / "fig02_escala_invisible.png"
    destino.parent.mkdir(exist_ok=True)
    ruta, d = dibujar(destino)
    print(f"escrita {ruta}  (discrepancias de orden: {d})")
