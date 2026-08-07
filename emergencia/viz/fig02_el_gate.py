"""Fig. 2 — El gate `0.80` y lo lejos que se quedó todo.

Ésta es la figura del fracaso, y conviene mirarla antes que ninguna explicación.

El contrato congelado (`P1a_contrato_gate_altura_duracion_lex_d2.md`) exigía, para
poder preregistrar un cociente entre lados, una correlación de al menos `0.80` entre
el estimador observable y la duración latente. Se probaron tres representaciones en
seis estratos. La mejor llega a `0.57`.

Lo que hace la figura no es sólo enseñar que se falló, sino **cuánto** margen había:
la banda morada es el techo `rho_max` del canal `sigma(m)` — el máximo alcanzable por
*cualquier* función de lo observado, no sólo por las tres fórmulas probadas. Ese techo
también está por debajo del gate. Es decir: el gate no se falló por elegir mal la
fórmula. Se falló porque la información no está.

`rho_max` se recalcula aquí desde el CSV sellado y la figura aborta si no reproduce
el valor del ejecutable auditado (`datos.anova_sigma_m`).
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

import datos
import estilo

ORDEN = ["HEIGHT_ONLY", "COUNT_VOLUME", "HEIGHT_WIDTH"]
ETIQUETA = {
    "HEIGHT_ONLY": "HEIGHT_ONLY\n$H/2\\sqrt{n}$",
    "COUNT_VOLUME": "COUNT_VOLUME\n$\\sqrt{(m-2)/(n-2)}$",
    "HEIGHT_WIDTH": "HEIGHT_WIDTH\n$(H+W)/4\\sqrt{n}$",
}


def dibujar():
    metricas, intervalos = datos.representaciones()
    estratos = datos.estratos()

    techo = {e: datos.anova_sigma_m(intervalos, *e)["rho_max"] for e in estratos}

    estilo.use_style()
    fig, ax = plt.subplots(figsize=(11.6, 5.4))

    ancho = 0.26
    xs = np.arange(len(estratos))

    # Banda del techo del canal, dibujada primero para que quede detrás.
    lo, hi = min(techo.values()), max(techo.values())
    ax.axhspan(lo, hi, color=estilo.COLOR_TECHO, alpha=0.13, lw=0, zorder=0)
    for k, e in enumerate(estratos):
        ax.hlines(techo[e], k - 0.44, k + 0.44, color=estilo.COLOR_TECHO,
                  lw=2.2, zorder=5)

    for j, repr_ in enumerate(ORDEN):
        desplaz = (j - 1) * ancho
        alturas, bajos, altos = [], [], []
        for n, side in estratos:
            fila = metricas[(metricas["representation"] == repr_)
                            & (metricas["n"] == n) & (metricas["side"] == side)].iloc[0]
            alturas.append(fila["pearson_correlation"])
            bajos.append(fila["pearson_correlation"] - fila["pearson_bootstrap95_low"])
            altos.append(fila["pearson_bootstrap95_high"] - fila["pearson_correlation"])
        ax.bar(xs + desplaz, alturas, ancho * 0.92,
               yerr=[bajos, altos], capsize=2.5, error_kw=dict(lw=1.0, ecolor="#333"),
               color=estilo.COLOR_REPR[repr_], label=ETIQUETA[repr_], zorder=3)

    ax.axhline(datos.GATE, color=estilo.COLOR_GATE, lw=2.4, zorder=6)
    ax.axhline(datos.UMBRAL_FUERTE, color=estilo.COLOR_GATE, lw=1.4, ls=(0, (5, 3)),
               zorder=6)

    ax.text(len(estratos) - 0.45, datos.GATE + 0.018,
            "gate preregistrado  $\\rho \\geq 0.80$", ha="right", va="bottom",
            color=estilo.COLOR_GATE, fontsize=10.5, fontweight="bold")
    ax.text(len(estratos) - 0.45, datos.UMBRAL_FUERTE + 0.014,
            "umbral fuerte secundario  0.30", ha="right", va="bottom",
            color=estilo.COLOR_GATE, fontsize=9)
    ax.text(-0.44, hi + 0.016,
            f"techo del canal $\\sigma(m)$:  $\\rho_{{\\max}} = {lo:.3f}$–{hi:.3f}\n"
            "ninguna función de lo observable pasa de aquí",
            ha="left", va="bottom", color=estilo.COLOR_TECHO, fontsize=9.4)

    ax.set_xticks(xs)
    ax.set_xticklabels([f"$n={n}$\n{'pasado' if s == 'PAST' else 'futuro'}"
                        for n, s in estratos])
    ax.set_ylabel("correlación de Pearson con la duración latente")
    ax.set_ylim(0, 1.06)
    ax.set_xlim(-0.55, len(estratos) - 0.45)
    ax.legend(loc="upper left", fontsize=9.2, ncol=3, columnspacing=1.4)
    ax.set_title("Tres representaciones, seis estratos, un gate que nunca estuvo cerca",
                 loc="left", fontsize=13.5)

    mejor = metricas["pearson_correlation"].max()
    ax.annotate(f"máximo de toda la línea: {mejor:.3f}",
                xy=(1 + 0, mejor), xytext=(1.6, 0.66), fontsize=9.6,
                color=estilo.BLUE,
                arrowprops=dict(arrowstyle="->", color=estilo.BLUE, lw=1.2))

    estilo.nota_al_pie(fig, "p1a_representaciones_metricas_d2.csv (IC bootstrap 95 %) · "
                            "techo recalculado desde p1a_representaciones_intervalos_d2.csv")
    fig.tight_layout(rect=(0, 0.025, 1, 1))

    return fig, {
        "rho maximo observado (COUNT_VOLUME)": float(mejor),
        "techo del canal, minimo": float(lo),
        "techo del canal, maximo": float(hi),
        "gate": datos.GATE,
        "distancia gate - mejor rho": float(datos.GATE - mejor),
        "distancia gate - techo maximo": float(datos.GATE - hi),
    }


if __name__ == "__main__":
    f, numeros = dibujar()
    print(estilo.guardar(f, "fig02_el_gate"))
    for k, v in numeros.items():
        print(f"  {k:42s} {v}")
