"""Fig. 2 — El gate `0.80` y lo lejos que se quedó todo.

Ésta es la figura del fracaso, y conviene mirarla antes que ninguna explicación.

El contrato congelado que gobierna este experimento
(`P1a_contrato_representaciones_alternativas_d2.md` §:145-146, :156) exigía, para
poder preregistrar un cociente entre lados, una correlación de al menos `0.80` entre
el estimador observable y la duración latente. Se probaron tres representaciones en
seis estratos. La mejor llega a `0.57`.

La segunda línea, en `0.50`, es el umbral de **aparcamiento fuerte**. No es
decorativa — separa `HEIGHT_WIDTH` (aparcada) de `COUNT_VOLUME` (no aparcada), que es
el terminal que el registro sellado consigna. La figura recomputa esa separación con
el predicado **literal** del contrato —los dos disyuntos y los cuantificadores, en
`datos.aparcada_fuerte`— y aborta si el CSV dejara de reproducirla. La línea dibujada
es sólo el primer disyunto, que es el que vive en este eje; el segundo (mediana del
error relativo con `IC95_inf > 0.50`) no se puede trazar aquí y por eso se evalúa en
el código y no en el dibujo.

*(El `0.30` del mismo contrato acota la mediana del error relativo para la
**cualificación**, otro eje; dibujarlo aquí fue el error 1 de la auditoría 032. Usar
`max(sup) < 0.50` como atajo del predicado fue el aviso 2 de la auditoría 033.)*

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

    sup_max = {}
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
        sup_max[repr_] = max(a + b for a, b in zip(alturas, altos))

    # La línea de `0.50` decide un terminal sellado, así que se comprueba que lo
    # decide bien: `HEIGHT_WIDTH_STRONGLY_PARKED = TRUE` y
    # `COUNT_VOLUME_STRONGLY_PARKED = FALSE` en
    # `P1a_resultados_representaciones_alternativas_d2.md` §5–§6. El predicado es
    # el del contrato, con sus dos disyuntos y sus cuantificadores (`datos.
    # aparcada_fuerte`), no el atajo `max(sup) < 0.50`. Si el CSV dejara de
    # reproducir esos dos terminales, la figura no se dibuja.
    aparcada = {r: datos.aparcada_fuerte(metricas, r) for r in ORDEN}
    if not (aparcada["HEIGHT_WIDTH"] and not aparcada["COUNT_VOLUME"]):
        raise ValueError(
            "los terminales de aparcamiento no reproducen el registro sellado: "
            f"aparcada = {aparcada}, sup(IC95) = {sup_max}"
        )

    ax.axhline(datos.GATE, color=estilo.COLOR_GATE, lw=2.4, zorder=6)
    ax.axhline(datos.APARCADO_FUERTE, color=estilo.COLOR_GATE, lw=1.4, ls=(0, (5, 3)),
               zorder=6)

    ax.text(len(estratos) - 0.45, datos.GATE + 0.018,
            "gate preregistrado  $\\rho \\geq 0.80$", ha="right", va="bottom",
            color=estilo.COLOR_GATE, fontsize=10.5, fontweight="bold")
    ax.text(len(estratos) - 0.45, datos.APARCADO_FUERTE - 0.018,
            "aparcado fuerte  $\\mathrm{IC}95_{sup}(\\rho) < 0.50$", ha="right",
            va="top", color=estilo.COLOR_GATE, fontsize=9)
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

    # La distinción que la línea de 0.50 hace, atribuida a la regla que la decide.
    # El `sup IC95` se reporta como cantidad, no como razón: de `sup < 0.50` sí se
    # sigue el aparcamiento, pero de `sup > 0.50` NO se sigue lo contrario bajo
    # `:152-157` (auditoría 034, hallazgo 1). Quien decide es `aparcada_fuerte`.
    ax.text(-0.44, 0.055,
            "Por la regla de aparcamiento del contrato (§:152-157 — para todo $n$, algún lado):\n"
            f"HEIGHT_WIDTH APARCADA ($\\sup \\mathrm{{IC}}95 = {sup_max['HEIGHT_WIDTH']:.3f}$)   ·   "
            f"COUNT_VOLUME NO aparcada (${sup_max['COUNT_VOLUME']:.3f}$), y aun así lejos del gate.",
            ha="left", va="bottom", fontsize=8.8, color="#333", zorder=8,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="white", alpha=0.92,
                      edgecolor="none"))

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
        "HEIGHT_WIDTH aparcada (regla :152-157)": aparcada["HEIGHT_WIDTH"],
        "COUNT_VOLUME aparcada (regla :152-157)": aparcada["COUNT_VOLUME"],
        "sup IC95 HEIGHT_WIDTH (cantidad, no criterio)": float(sup_max["HEIGHT_WIDTH"]),
        "sup IC95 COUNT_VOLUME (cantidad, no criterio)": float(sup_max["COUNT_VOLUME"]),
    }


if __name__ == "__main__":
    f, numeros = dibujar()
    print(estilo.guardar(f, "fig02_el_gate"))
    for k, v in numeros.items():
        print(f"  {k:42s} {v}")
