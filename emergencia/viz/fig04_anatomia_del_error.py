"""Fig. 4 — Anatomía del error: por qué la línea siguió viva meses de más.

La figura 3 explica por qué el resultado es negativo. Ésta explica por qué se tardó
tanto en verlo, que para el que trabaja aquí es la información más cara.

**A.** `COUNT_VOLUME` no era un estimador mediocre al que le faltase un empujón:
está pegado al óptimo de su propio canal. Sustituirlo por cualquier otra función de
lo observable habría ganado, como mucho, la longitud de esas barras. Toda la
literatura interna sobre «mejorar la representación» estaba atacando un margen de
tres milésimas.

**B.** El error de navegación. Durante meses el techo operativo no era `rho_max`
sino `rho_max_ub_Bn = 0.83–0.86`, una cota superior derivada vía `B_n` y **leída como
si fuera el máximo real**. Ese número está *por encima* del gate `0.80`: mientras se
creyó, el gate parecía alcanzable y la pregunta parecía ser «cuánto falta». El techo
real siempre estuvo en `0.53–0.57`. Retractación registrada en
`P1a_count_volume_canal_sigma_m_d2.md` §6.

**C.** La consecuencia operativa. Con `0.83–0.86` como techo, faltaba un factor
`1.17` (exclusión parcial) o `1.36` (total), y la vía natural era apretar el conjunto
factible `F_relax`. El Teorema CV-4.3 acabó demostrando que **ninguna** restricción
de ese tipo puede aportar más de `1.000017`. La holgura existía —`B_n` era floja por
un factor `2.3–2.6`— pero estaba entera en el paso `min` sobre `F_relax`, es decir,
justo donde no se estaba buscando.

Lección de clase, no de detalle: *una cota superior no es el valor que acota*, y usar
la cota como si lo fuera convierte un no-go en un problema abierto.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

import datos
import estilo

# B_n por estrato, salida literal del ejecutable auditado
# `emergencia/p1a_count_volume_techo_apriete_d2.py` (determinista, sólo lectura).
B_N = {
    (64, "FUTURE"): 0.001102, (64, "PAST"): 0.001100,
    (96, "FUTURE"): 0.000771, (96, "PAST"): 0.000771,
    (128, "FUTURE"): 0.000598, (128, "PAST"): 0.000597,
}
FACTOR_PARCIAL = 1.17   # exclusión parcial del gate por la vía B_n
FACTOR_TOTAL = 1.36     # exclusión en los seis estratos


def dibujar():
    _, intervalos = datos.representaciones()
    claves = datos.estratos()
    a = {e: datos.anova_sigma_m(intervalos, *e) for e in claves}

    huecos = {e: a[e]["rho_max"] - a[e]["rho_obs"] for e in claves}
    holguras = {e: (a[e]["ssw"] / a[e]["N"]) / B_N[e] for e in claves}
    if min(huecos.values()) < 0:
        raise ValueError("rho_obs supera rho_max: la identidad del canal estaría rota")

    estilo.use_style()
    fig = plt.figure(figsize=(15.6, 5.4))
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1, 3, 3)

    # ---------------------------------------------------------------- panel A
    ys = np.arange(len(claves))
    for k, e in enumerate(claves):
        ax1.plot([a[e]["rho_obs"], a[e]["rho_max"]], [k, k], color=estilo.GREY,
                 lw=2.4, zorder=2, solid_capstyle="butt")
    ax1.scatter([a[e]["rho_obs"] for e in claves], ys, s=95, color=estilo.BLUE,
                zorder=4, label="COUNT_VOLUME, lo que se usó")
    ax1.scatter([a[e]["rho_max"] for e in claves], ys, s=95,
                color=estilo.COLOR_TECHO, marker="D", zorder=4,
                label="$\\rho_{\\max}$, el óptimo del canal")
    for k, e in enumerate(claves):
        ax1.text(a[e]["rho_max"] + 0.0012, k, f"  +{huecos[e]:.4f}",
                 va="center", fontsize=8.6, color=estilo.GREY)

    ax1.set_yticks(ys)
    ax1.set_yticklabels([f"$n={n}$ {'pas.' if s == 'PAST' else 'fut.'}"
                         for n, s in claves])
    ax1.set_xlabel("correlación con la duración latente")
    ax1.set_xlim(0.520, 0.578)
    ax1.set_ylim(-0.5, len(claves) + 0.35)
    ax1.legend(loc="upper left", fontsize=8.6)
    ax1.set_title("A. No sobraba estimador: sobraba esperanza", loc="left")

    # ---------------------------------------------------------------- panel B
    lo_r = min(a[e]["rho_max"] for e in claves)
    hi_r = max(a[e]["rho_max"] for e in claves)
    lo_b, hi_b = datos.RHO_MAX_UB_BN

    # Ventana ajustada: con el eje completo [0,1] el techo creído y el gate se
    # solapan visualmente, que es justo lo que hay que poder distinguir.
    ax2.set_xlim(0.46, 0.96)
    ax2.set_ylim(0, 1)
    ax2.set_yticks([])
    ax2.grid(False)
    for lado in ("left", "right", "top"):
        ax2.spines[lado].set_visible(False)

    ax2.axvspan(lo_r, hi_r, ymin=0.10, ymax=0.34, color=estilo.COLOR_TECHO, alpha=0.9,
                lw=0)
    ax2.text((lo_r + hi_r) / 2, 0.37,
             f"techo REAL del canal\n$\\rho_{{\\max}} = {lo_r:.3f}$–{hi_r:.3f}",
             ha="center", va="bottom", fontsize=9.8, color=estilo.COLOR_TECHO,
             fontweight="bold")

    ax2.axvspan(lo_b, hi_b, ymin=0.62, ymax=0.86, color=estilo.GREY, alpha=0.55, lw=0)
    ax2.text(hi_b + 0.006, 0.74,
             f"techo CREÍDO\n$\\rho^{{ub}}_{{\\max}}(B_n) = {lo_b}$–{hi_b}\n"
             "cota superior leída\ncomo si fuera el máximo",
             ha="left", va="center", fontsize=9, color="#333")

    ax2.axvline(datos.GATE, color=estilo.COLOR_GATE, lw=2.6, zorder=5)
    ax2.text(datos.GATE - 0.008, 0.13, "gate  0.80", ha="right", va="bottom",
             rotation=90, color=estilo.COLOR_GATE, fontsize=10.5, fontweight="bold")

    ax2.annotate("", xy=(lo_b, 0.47), xytext=(hi_r, 0.47),
                 arrowprops=dict(arrowstyle="<|-|>", color="#333", lw=1.3,
                                 shrinkA=0, shrinkB=0))
    ax2.text((hi_r + lo_b) / 2, 0.50,
             "mientras se creyó el techo de arriba,\nel gate caía DENTRO de lo alcanzable\n"
             "y la pregunta era «cuánto falta»",
             ha="center", va="bottom", fontsize=8.8, color="#333")

    ax2.set_xlabel("correlación con la duración latente")
    ax2.set_title("B. Se navegó con el techo equivocado", loc="left")

    # ---------------------------------------------------------------- panel C
    etiquetas = ["holgura real de $B_n$,\ntoda ella en el paso\n$\\min$ sobre $F_{relax}$",
                 "hacía falta para excluir\nel gate en los seis estratos",
                 "hacía falta para excluir\nel gate parcialmente",
                 "podía dar cualquier apriete\nde $F_{relax}$ por arriba\n(Teorema CV-4.3)"]
    valores = [float(np.mean(list(holguras.values()))), FACTOR_TOTAL, FACTOR_PARCIAL,
               datos.FACTOR_MAX_APRIETE]
    colores = [estilo.GREEN, estilo.GREY, estilo.GREY, estilo.RED]

    # Escala logarítmica y referencia en 1: el punto es que la barra roja no se
    # separa de la línea, y eso no es un defecto del dibujo.
    for k, (v, c) in enumerate(zip(valores, colores)):
        ax3.plot([1.0, v], [k, k], color=c, lw=3.4, solid_capstyle="butt", zorder=3)
        ax3.scatter([v], [k], s=110, color=c, zorder=4)
        texto = f"×{v:.6f}" if v < 1.01 else f"×{v:.2f}"
        ax3.text(v * 1.06, k, texto, va="center", fontsize=9.4, color="#333")

    ax3.axvline(1.0, color="#333", lw=1.2, zorder=2)
    ax3.set_xscale("log")
    ax3.set_xlim(0.995, 4.6)
    ax3.set_ylim(-0.7, len(valores) - 0.3)
    ax3.set_xticks([1.0, 1.2, 1.5, 2.0, 3.0, 4.0])
    ax3.set_xticklabels(["1", "1.2", "1.5", "2", "3", "4"])
    ax3.minorticks_off()
    ax3.set_yticks(np.arange(len(valores)))
    ax3.set_yticklabels(etiquetas, fontsize=8.4)
    ax3.set_xlabel("factor de mejora sobre $B_n$  (escala logarítmica)")
    ax3.annotate("indistinguible de 1", xy=(1.0, len(valores) - 1),
                 xytext=(1.35, len(valores) - 1.45), fontsize=8.8, color=estilo.RED,
                 arrowprops=dict(arrowstyle="->", color=estilo.RED, lw=1.1))

    ax3.set_title("C. La holgura existía, y no estaba donde se buscó", loc="left")

    fig.suptitle("El coste no fue el resultado negativo: fue leer una cota superior "
                 "como si fuera el máximo",
                 x=0.005, ha="left", fontsize=13.5, y=1.005)
    estilo.nota_al_pie(
        fig,
        "huecos y holguras recalculados desde p1a_representaciones_intervalos_d2.csv · "
        "$B_n$ de p1a_count_volume_techo_apriete_d2.py · el panel A dibuja el hueco "
        "exacto del Bloque A; su versión corregida $\\sqrt{1-T_{corr}}-\\rho_{obs}$ "
        "vale $|\\Delta| < 0.0008$ (ver README)")
    fig.tight_layout(rect=(0, 0.03, 1, 0.985))

    return fig, {
        "hueco rho_max - rho_obs, maximo": max(huecos.values()),
        "hueco rho_max - rho_obs, minimo": min(huecos.values()),
        "holgura de B_n, rango": (min(holguras.values()), max(holguras.values())),
        "factor maximo de cualquier apriete": datos.FACTOR_MAX_APRIETE,
        "factor necesario (parcial / total)": (FACTOR_PARCIAL, FACTOR_TOTAL),
        "techo creido vs techo real": (datos.RHO_MAX_UB_BN, (lo_r, hi_r)),
    }


if __name__ == "__main__":
    f, numeros = dibujar()
    print(estilo.guardar(f, "fig04_anatomia_del_error"))
    for k, v in numeros.items():
        print(f"  {k:42s} {v}")
