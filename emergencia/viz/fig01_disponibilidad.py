"""Fig. 1 — Disponibilidad: la única parte de la línea que salió bien.

Qué muestra: el selector intrínseco de dos intervalos pasa de no existir casi nunca
(`n=6`: una permutación de cada 720) a estar disponible en el 70 % de los posets
(`n=128`, `MIN_COVERAGE_LEX`). Es un éxito de ingeniería, medido con enumeración
exacta donde se puede y Monte Carlo donde no.

Por qué está la primera: porque es la trampa. **Disponibilidad no es
identificabilidad** (lección 1 de `HOJA_DE_RUTA.md` §4). Esta curva subiendo es
exactamente lo que hizo creer durante meses que la línea avanzaba, y no mide nada
de lo que la línea quería medir. Las figuras 2–4 miden eso otro.

El panel A vale además como control de código: enumeración exacta y Monte Carlo son
dos implementaciones independientes del mismo estado, y coinciden en `n=6..9`.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

import datos
import estilo

TIES = ["TIE_BRIDGE_ONLY", "TIE_PAST_ENDPOINT", "TIE_FUTURE_ENDPOINT", "TIE_MIXED"]


def _colapsar(df):
    """P(VACÍO), P(ÚNICO), P(EMPATE) por `n`, sumando las cuatro clases de empate."""
    p = df.pivot_table(index="n", columns="state", values="probability", aggfunc="sum")
    return p["EMPTY"], p["UNIQUE"], p[TIES].sum(axis=1)


def dibujar():
    exacta, mc = datos.disponibilidad()
    comparacion = datos.leer("p1a_comparacion_selectores_d2.csv")

    e_vacio, e_unico, e_empate = _colapsar(exacta)
    m_vacio, m_unico, m_empate = _colapsar(mc)

    # Control: las dos vías independientes deben coincidir donde ambas existen.
    comunes = sorted(set(e_unico.index) & set(m_unico.index))
    brecha = max(abs(e_unico[n] - m_unico[n]) for n in comunes)
    if brecha > 0.01:
        raise ValueError(f"exacta y Monte Carlo discrepan en P(ÚNICO): {brecha:.4f}")

    estilo.use_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 4.9))

    # ---------------------------------------------------------------- panel A
    series = [
        ("vacío — el selector no se puede aplicar", m_vacio, e_vacio, estilo.GREY, "o"),
        ("único — hay selección", m_unico, e_unico, estilo.GREEN, "s"),
        ("empate — hay que abstenerse", m_empate, e_empate, estilo.ORANGE, "^"),
    ]
    for etiqueta, mcs, ex, color, marca in series:
        ax1.plot(mcs.index, mcs.values, color=color, lw=2.0, label=etiqueta, zorder=3)
        ax1.plot(ex.index, ex.values, ls="none", marker=marca, ms=7,
                 mfc="white", mec=color, mew=1.6, zorder=4)

    ax1.set_xscale("log")
    ax1.set_xticks([6, 8, 12, 16, 24, 32, 48, 64])
    ax1.set_xticklabels([6, 8, 12, 16, 24, 32, 48, 64])
    ax1.set_xlabel("$n$  (elementos del causet)")
    ax1.set_ylabel("probabilidad del estado")
    ax1.set_ylim(-0.03, 1.05)
    ax1.set_title("A. Estados del selector de cobertura", loc="left")

    # Las dos vías se distinguen en la propia leyenda, para no plantar un bloque
    # de texto encima de las curvas.
    proxy_mc = plt.Line2D([], [], color=estilo.GREY, lw=2.0)
    proxy_ex = plt.Line2D([], [], ls="none", marker="o", ms=7, mfc="white",
                          mec=estilo.GREY, mew=1.6)
    manejas, etiquetas = ax1.get_legend_handles_labels()
    ax1.legend(manejas + [proxy_mc, proxy_ex],
               etiquetas + ["línea: Monte Carlo",
                            f"marca hueca: exacta (dif. $\\leq$ {brecha:.4f})"],
               loc="center right", fontsize=8.8)
    ax1.annotate(f"$n=6$: 1 de 720\n$P={e_unico[6]:.4f}$",
                 xy=(6, e_unico[6]), xytext=(7.4, 0.20), fontsize=8.6,
                 color=estilo.GREEN,
                 arrowprops=dict(arrowstyle="->", color=estilo.GREEN, lw=1.1))

    # ---------------------------------------------------------------- panel B
    for selector, sub in comparacion.groupby("selector"):
        sub = sub.sort_values("n")
        color = estilo.COLOR_SELECTOR[selector]
        ax2.plot(sub["n"], sub["p_unique"], color=color, lw=2.0, marker="o", ms=5,
                 label=selector, zorder=3)
        ax2.fill_between(sub["n"], sub["p_unique_ci95_low"], sub["p_unique_ci95_high"],
                         color=color, alpha=0.18, lw=0, zorder=2)

    ax2.set_xscale("log")
    ax2.set_xticks([32, 48, 64, 96, 128])
    ax2.set_xticklabels([32, 48, 64, 96, 128])
    ax2.minorticks_off()
    ax2.set_xlabel("$n$")
    ax2.set_ylabel("$P(\\mathrm{selección\\ única})$")
    ax2.set_ylim(0.10, 0.80)
    ax2.set_title("B. Tres selectores balanceados, misma muestra", loc="left")
    ax2.legend(loc="upper left", fontsize=9.2)

    mejor = comparacion[(comparacion["selector"] == "MIN_COVERAGE_LEX")
                        & (comparacion["n"] == 128)]["p_unique"].item()
    ax2.annotate(f"selector de trabajo\n{mejor:.3f} a $n=128$",
                 xy=(128, mejor), xytext=(64, 0.42), fontsize=8.8,
                 color=estilo.GREEN,
                 arrowprops=dict(arrowstyle="->", color=estilo.GREEN, lw=1.1))

    fig.suptitle("Disponibilidad: resuelta — y no era el problema",
                 x=0.005, ha="left", fontsize=13.5, y=1.005)
    estilo.nota_al_pie(fig, "p1a_enumeracion_exacta_d2.csv · p1a_monte_carlo_d2.csv · "
                            "p1a_comparacion_selectores_d2.csv (SHA-256 verificados)")
    fig.tight_layout(rect=(0, 0.02, 1, 0.985))

    return fig, {
        "P(unico) exacta n=6": float(e_unico[6]),
        "P(unico) MC n=64": float(m_unico[64]),
        "max |exacta - MC| en P(unico)": float(brecha),
        "MIN_COVERAGE_LEX P(unico) n=128": float(mejor),
        "P(empate) MC n=64": float(m_empate[64]),
    }


if __name__ == "__main__":
    f, numeros = dibujar()
    print(estilo.guardar(f, "fig01_disponibilidad"))
    for k, v in numeros.items():
        print(f"  {k:42s} {v}")
