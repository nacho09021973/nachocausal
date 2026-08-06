"""Figura 5 — Lo que el orden SÍ recupera: la posición relativa al horizonte.

Es la pareja obligada de la Figura 2, y juntas dicen el paper entero:

    Figura 2:  el orden NO ve  r_s          (la escala absoluta)
    Figura 5:  el orden SÍ ve  r / r_s      (la posición relativa)

El estadístico es lo más simple que existe: la **fracción de pares comparables**.
Se cuenta cuántas parejas de elementos están relacionadas y se divide por el total.
No hay umbrales, ni ajustes, ni coordenadas.

Panel A: la fracción cae de forma pronunciada al acercar el parche al horizonte —
los conos se estrechan, y el orden lo nota.
Panel B: la misma curva calculada con `r_s = 1` y con `r_s = 7`, con sprinklings
**independientes**, cae encima de sí misma.  Multiplicar la masa por 7 no mueve la
curva ni un pelo: el estadístico depende de `r/r_s` y de nada más.  Eso es el
Teorema 3.1 visto desde el otro lado.
"""

from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import numpy as np

from causet_core import causal_matrix, comparable_fraction, sprinkle_exterior
from style import AZUL, GRIS, NARANJA, usar_estilo

SEMILLA = 4242
N_PUNTOS = 60
REPETICIONES = 80
ANCHO = 1.0        # ancho del parche, en unidades de r_s
DURACION = 3.0     # duración del parche, en unidades de r_s
XS = np.array([1.05, 1.15, 1.3, 1.5, 1.8, 2.2, 2.8, 3.6, 5.0, 7.0, 9.0])


def barrido(rs, rng):
    """Fracción comparable media y desviación, con la forma del parche FIJA en r_s."""
    medias, desv = [], []
    for x in XS:
        vals = []
        for _ in range(REPETICIONES):
            t, r = sprinkle_exterior(
                rs, (0.0, DURACION * rs), (x * rs, (x + ANCHO) * rs), N_PUNTOS, rng)
            vals.append(comparable_fraction(causal_matrix(t, r, rs)))
        vals = np.asarray(vals)
        medias.append(vals.mean())
        desv.append(vals.std())
    return np.asarray(medias), np.asarray(desv)


def dibujar(salida):
    rng = np.random.default_rng(SEMILLA)
    m1, s1 = barrido(1.0, rng)
    m7, s7 = barrido(7.0, rng)          # sprinklings INDEPENDIENTES, no reescalados
    brecha = float(np.max(np.abs(m1 - m7)))

    usar_estilo()
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(12.0, 5.0))

    # --- A: la señal ---------------------------------------------------------
    axA.fill_between(XS, m1 - s1, m1 + s1, color=AZUL, alpha=0.18)
    axA.plot(XS, m1, "o-", color=AZUL, lw=2.0, ms=6)
    axA.axvline(1.0, color="#111111", lw=2.0)
    axA.text(1.0, axA.get_ylim()[0], "  horizonte", ha="left", va="bottom",
             fontsize=9, color="#111111", rotation=90)
    axA.set_xscale("log")
    axA.set_xticks([1, 2, 3, 5, 9])
    axA.set_xticklabels(["1", "2", "3", "5", "9"])
    axA.set_xlabel("posición del parche  $r/r_s$   (adimensional)")
    axA.set_ylabel("fracción de pares comparables")
    axA.set_title("A · el orden nota el horizonte", loc="left", pad=10)
    axA.annotate("cerca del horizonte los conos\nse estrechan: menos pares causales",
                 xy=(1.15, m1[1]), xytext=(2.1, m1[0] + 0.02), fontsize=9.5, color=GRIS,
                 ha="left", va="bottom",
                 arrowprops=dict(arrowstyle="->", color=GRIS, lw=1.2,
                                 connectionstyle="arc3,rad=0.15"))

    # --- B: invariancia de escala --------------------------------------------
    axB.errorbar(XS, m1, yerr=s1, fmt="o-", color=AZUL, lw=2.0, ms=6,
                 capsize=3, label="$r_s = 1$")
    axB.errorbar(XS, m7, yerr=s7, fmt="s--", color=NARANJA, lw=2.0, ms=6,
                 capsize=3, label="$r_s = 7$  (sprinklings independientes)")
    axB.set_xscale("log")
    axB.set_xticks([1, 2, 3, 5, 9])
    axB.set_xticklabels(["1", "2", "3", "5", "9"])
    axB.set_xlabel("posición del parche  $r/r_s$")
    axB.set_ylabel("fracción de pares comparables")
    axB.set_title("B · multiplicar la masa por 7 no mueve la curva", loc="left", pad=10)
    axB.legend(loc="lower right", fontsize=9.5)
    axB.text(0.03, 0.95, f"discrepancia máxima: {brecha:.3f}\n(desviación típica ≈ {s1.mean():.3f})",
             transform=axB.transAxes, ha="left", va="top", fontsize=9.5, color=GRIS)

    fig.suptitle("El orden lee la distancia al horizonte en unidades del horizonte — nunca en metros",
                 fontsize=13.5, y=0.99)
    fig.text(0.5, 0.005,
             "Pareja de la Figura 2: allí se veía que $r_s$ es invisible; aquí, que $r/r_s$ no lo es.",
             ha="center", fontsize=10.5)
    fig.tight_layout(rect=(0, 0.04, 1, 0.93))
    fig.savefig(salida)
    plt.close(fig)
    return salida, brecha, float(s1.mean())


if __name__ == "__main__":
    destino = pathlib.Path(__file__).parent / "salida" / "fig05_lo_recuperable.png"
    destino.parent.mkdir(exist_ok=True)
    ruta, brecha, sd = dibujar(destino)
    print(f"escrita {ruta}")
    print(f"  discrepancia máxima entre rs=1 y rs=7: {brecha:.4f}  (sd típica {sd:.4f})")
