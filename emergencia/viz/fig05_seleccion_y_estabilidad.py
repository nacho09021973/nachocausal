"""Fig. 5 — Lo que la selección hace, y que no se ve en ninguna correlación.

Tres hechos medidos que no aparecen en la figura del gate y que explican por qué
«mejorar el selector» tampoco era una salida.

**A. El target es estable; los endpoints no.** Tras borrar al azar el 10 % o el 20 %
de los elementos, la cuádrupla exacta que el selector reelige cae a `0.55–0.60` y
`0.31–0.35`, mientras la duración estimada se mantiene dentro del 25 % en
`0.72–0.96` de los casos. Lo que el selector devuelve es robusto **aunque cambie de
sitio**: la magnitud no está anclada a los elementos que la producen (lección 6 de
`HOJA_DE_RUTA.md` §4).

**B. La selección es parte del target.** Dos scores balanceados distintos, sobre el
mismo poset y en las mismas repeticiones, coinciden en la cuádrupla elegida en menos
del 1 % de los casos a partir de `n=64`, y en el 0 % a `n>=96`. No hay «el» intervalo
canónico que distintos selectores aproximen: cada score define el suyo (lección 2).

**C. Los endpoints viven en la pared de la caja, y cada vez más.** Los extremos
seleccionados caen cerca del borde de la ventana entre `1.5` y `2.5` veces más a
menudo que si se repartieran uniformemente — y el enriquecimiento **crece con `n`**,
que es la dirección contraria a la que haría falta. El selector responde en buena
parte a dónde termina la caja, no a la geometría de dentro: el mismo obstáculo que
mató a los localizadores C1–C5 en el acta 042. Subir `n` no lo diluye.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

import datos
import estilo


def dibujar():
    thin = datos.leer("p1a_lex_target_thinning_d2.csv")
    pareada = datos.leer("p1a_comparacion_pareada_selectores_d2.csv")
    comparacion = datos.leer("p1a_comparacion_selectores_d2.csv")

    estilo.use_style()
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15.6, 5.0))

    # ---------------------------------------------------------------- panel A
    ns = sorted(thin["n"].unique())
    xs = np.arange(len(ns))
    ancho = 0.19
    for j, ret in enumerate(sorted(thin["retention"].unique(), reverse=True)):
        sub = thin[thin["retention"] == ret].set_index("n").loc[ns]
        ax1.bar(xs + (j - 1.5) * ancho * 1.06 - 0.0,
                sub["p_exact_reselected_given_both_unique"], ancho,
                color=estilo.RED, alpha=1.0 - 0.35 * j, zorder=3,
                label=f"misma cuádrupla exacta, retención {ret:.1f}")
        ax1.bar(xs + (j + 0.5) * ancho * 1.06 + 0.06,
                sub["p_target_within_25"], ancho,
                color=estilo.GREEN, alpha=1.0 - 0.35 * j, zorder=3,
                label=f"duración dentro del 25 %, retención {ret:.1f}")

    ax1.set_xticks(xs)
    ax1.set_xticklabels([f"$n={n}$" for n in ns])
    ax1.set_ylabel("probabilidad")
    ax1.set_ylim(0, 1.42)
    ax1.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax1.legend(loc="upper center", fontsize=7.2, ncol=2, columnspacing=0.9,
               handlelength=1.4)
    ax1.set_title("A. El target aguanta; los elementos no", loc="left")

    # ---------------------------------------------------------------- panel B
    pares = [("COVERAGE", "MIN_ONLY"), ("COVERAGE", "MIN_COVERAGE_LEX")]
    for (a, b), color, marca in zip(pares, [estilo.ORANGE, estilo.BLUE], ["o", "s"]):
        sub = pareada[(pareada["selector_a"] == a)
                      & (pareada["selector_b"] == b)].sort_values("n")
        ax2.plot(sub["n"], sub["p_same_quadruple_given_both_unique"], color=color,
                 lw=2.2, marker=marca, ms=7, zorder=3,
                 label=f"{a} vs {b}")
        for _, fila in sub.iterrows():
            if fila["p_same_quadruple_given_both_unique"] == 0:
                ax2.scatter([fila["n"]], [0], s=120, facecolor="white",
                            edgecolor=color, lw=1.8, zorder=4)

    ax2.set_xscale("log")
    ax2.set_xticks([32, 48, 64, 96, 128])
    ax2.set_xticklabels([32, 48, 64, 96, 128])
    ax2.minorticks_off()
    ax2.set_xlabel("$n$")
    ax2.set_ylabel("$P(\\mathrm{misma\\ cuádrupla} \\mid \\mathrm{ambos\\ únicos})$")
    ax2.set_ylim(-0.02, 0.30)
    ax2.legend(loc="upper right", fontsize=8.6)
    ax2.text(64, 0.135,
             "marca hueca sobre el eje:\ncoincidencia exacta CERO\nen 12 000 repeticiones",
             fontsize=8.6, color=estilo.GREY, ha="center")
    ax2.set_title("B. Cada score define su propio intervalo", loc="left")

    # ---------------------------------------------------------------- panel C
    referencia = comparacion["uniform_boundary_reference"].unique()
    if len(referencia) != 1:
        raise ValueError(f"la referencia uniforme no es única: {referencia}")
    referencia = float(referencia[0])

    for selector, sub in comparacion.groupby("selector"):
        sub = sub.sort_values("n")
        ax3.plot(sub["n"], sub["near_boundary_endpoint_fraction"],
                 color=estilo.COLOR_SELECTOR[selector], lw=2.2, marker="o", ms=6,
                 label=selector, zorder=3)

    ax3.axhline(referencia, color=estilo.GREY, lw=1.6, ls=(0, (5, 3)), zorder=2)
    ax3.text(128, referencia - 0.008,
             f"reparto uniforme: {referencia:.2f}", ha="right", va="top",
             fontsize=9, color=estilo.GREY)

    enriq = comparacion["boundary_enrichment"]
    ax3.set_xscale("log")
    ax3.set_xticks([32, 48, 64, 96, 128])
    ax3.set_xticklabels([32, 48, 64, 96, 128])
    ax3.minorticks_off()
    ax3.set_xlabel("$n$")
    ax3.set_ylabel("fracción de endpoints cerca del borde")
    ax3.set_ylim(0.14, 0.56)
    ax3.legend(loc="upper left", fontsize=8.6)
    ax3.text(33, 0.222,
             f"enriquecimiento ×{enriq.min():.2f} a ×{enriq.max():.2f},\ncreciente en $n$",
             fontsize=9.4, color=estilo.RED, fontweight="bold", va="bottom")
    ax3.set_title("C. El selector mira a la pared de la caja", loc="left")

    fig.suptitle("La selección no es un preliminar del experimento: es parte de lo "
                 "que se mide",
                 x=0.005, ha="left", fontsize=13.5, y=1.005)
    estilo.nota_al_pie(fig, "p1a_lex_target_thinning_d2.csv · "
                            "p1a_comparacion_pareada_selectores_d2.csv · "
                            "p1a_comparacion_selectores_d2.csv (SHA-256 verificados)")
    fig.tight_layout(rect=(0, 0.025, 1, 0.985))

    r80 = thin[thin["retention"] == 0.8]
    return fig, {
        "misma cuadrupla, retencion 0.8":
            (r80["p_exact_reselected_given_both_unique"].min(),
             r80["p_exact_reselected_given_both_unique"].max()),
        "duracion dentro del 25 %, retencion 0.8":
            (r80["p_target_within_25"].min(), r80["p_target_within_25"].max()),
        "coincidencia entre selectores, n=128":
            float(pareada[(pareada["n"] == 128)
                          & (pareada["selector_a"] == "COVERAGE")]
                  ["p_same_quadruple_given_both_unique"].max()),
        "enriquecimiento en el borde":
            (float(enriq.min()), float(enriq.max())),
        "p_floor de COVERAGE (suelo del score)":
            (float(comparacion[comparacion["selector"] == "COVERAGE"]["p_floor"].min()),
             float(comparacion[comparacion["selector"] == "COVERAGE"]["p_floor"].max())),
    }


if __name__ == "__main__":
    f, numeros = dibujar()
    print(estilo.guardar(f, "fig05_seleccion_y_estabilidad"))
    for k, v in numeros.items():
        print(f"  {k:42s} {v}")
