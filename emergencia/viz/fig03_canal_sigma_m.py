"""Fig. 3 — Por qué falló: el canal observable es `sigma(m)`, y `m` no basta.

Ésta es la explicación mecánica del techo que la figura 2 sólo dibuja.

Condicionado a la selección, dentro de un estrato `(n, side)` fijo, todo lo que el
observador ve del intervalo se reduce a **una variable discreta**: su cardinalidad
`m` (Lemas 1–3 de `P1a_count_volume_canal_sigma_m_d2.md`). `n` y `side` son
constantes del estrato y `S` es el espacio total, luego no aportan `sigma`-álgebra;
y `COUNT_VOLUME = sqrt((m-2)/(n-2))` es biyección creciente de `m`.

Consecuencia: el mejor predictor posible de la duración latente es la **media por
bin** `E[ell | m]`, y su correlación es `sqrt(SSB/SST)` — una identidad, no una
estimación. El panel A enseña por qué ese máximo es bajo: las nubes verticales sobre
cada `m` son mucho más altas que el desplazamiento de sus medias. El panel B lo dice
en distribución: una misma duración latente es compatible con casi cualquier `m`.
El panel C reparte la varianza: dos tercios largos quedan **dentro** del bin, es
decir, invisibles.

La figura recalcula el ANOVA desde el CSV sellado y aborta si no reproduce los
valores del ejecutable auditado.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

import datos
import estilo

N_PANEL = 64
LADO_PANEL = "PAST"
M_VIOLIN = [8, 11, 14, 17, 20, 23]


def dibujar():
    _, intervalos = datos.representaciones()
    a = datos.anova_sigma_m(intervalos, N_PANEL, LADO_PANEL)
    todos = {e: datos.anova_sigma_m(intervalos, *e) for e in datos.estratos()}

    estilo.use_style()
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15.6, 5.2))

    # ---------------------------------------------------------------- panel A
    rng = np.random.default_rng(20260807)   # sólo jitter visual del eje x discreto
    jitter = rng.uniform(-0.30, 0.30, size=a["N"])
    ax1.scatter(a["m"] + jitter, a["y"], s=3.2, color=estilo.GREY, alpha=0.10,
                lw=0, zorder=2)

    ms = np.array(sorted(a["medias"]))
    medias = np.array([a["medias"][int(m)] for m in ms])
    ax1.plot(ms, medias, color=estilo.GREEN, lw=2.6, marker="o", ms=4.5, zorder=5,
             label="$E[\\ell \\mid m]$ — el mejor predictor posible")
    cv = np.sqrt((ms - 2) / (N_PANEL - 2))
    ax1.plot(ms, cv, color=estilo.BLUE, lw=2.0, ls=(0, (4, 2)), zorder=4,
             label="COUNT_VOLUME $=\\sqrt{(m-2)/(n-2)}$")

    ax1.set_xlabel("$m$  (cardinalidad del intervalo) — todo lo observable")
    ax1.set_ylabel("$\\ell$  (duración latente, oculta)")
    ax1.set_title(f"A. Todo el canal, $n={N_PANEL}$, pasado", loc="left")
    ax1.legend(loc="upper left", fontsize=8.6)
    ax1.set_ylim(0, max(a["y"].max(), cv.max()) * 1.15)
    ax1.set_xticks([m for m in ms if m % 5 == 0])

    # ---------------------------------------------------------------- panel B
    grupos = [a["y"][a["m"] == m] for m in M_VIOLIN]
    partes = ax2.violinplot(grupos, positions=M_VIOLIN, widths=2.3,
                            showextrema=False, showmedians=True)
    for cuerpo in partes["bodies"]:
        cuerpo.set_facecolor(estilo.BLUE)
        cuerpo.set_alpha(0.42)
        cuerpo.set_edgecolor(estilo.BLUE)
    partes["cmedians"].set_color(estilo.BLUE)
    partes["cmedians"].set_linewidth(1.8)

    # Una duración latente concreta, y todos los `m` que la producen.
    corte = float(np.median(a["y"]))
    ax2.axhline(corte, color=estilo.RED, lw=1.6, ls=(0, (5, 3)), zorder=5)
    compatibles = sum(1 for g in grupos
                      if g.min() <= corte <= g.max())
    ax2.text(M_VIOLIN[-1] + 1.4, min(g.min() for g in grupos) + 0.01,
             f"la mediana global $\\ell = {corte:.3f}$ cae dentro\n"
             f"del soporte de {compatibles} de los {len(M_VIOLIN)} valores\n"
             "de $m$ dibujados",
             color=estilo.RED, fontsize=8.8, va="bottom", ha="right")

    ax2.set_xlabel("$m$")
    ax2.set_ylabel("$\\ell$")
    ax2.set_xticks(M_VIOLIN)
    ax2.set_title("B. Las distribuciones condicionales se solapan", loc="left")

    # ---------------------------------------------------------------- panel C
    xs = np.arange(len(todos))
    claves = datos.estratos()
    dentro = [todos[e]["t_emp"] for e in claves]
    fuera = [1 - v for v in dentro]

    # Barras contiguas: las dos bandas forman un bloque continuo sobre el que se
    # puede rotular sin leyenda. Los estratos se separan con el borde blanco.
    ax3.bar(xs, dentro, 1.0, color=estilo.RED, alpha=0.80,
            edgecolor="white", lw=1.4, zorder=3)
    ax3.bar(xs, fuera, 1.0, bottom=dentro, color=estilo.GREEN, alpha=0.85,
            edgecolor="white", lw=1.4, zorder=3)

    for k, e in enumerate(claves):
        ax3.text(k, 1.015, f"$\\rho_{{\\max}}$\n{todos[e]['rho_max']:.3f}",
                 ha="center", va="bottom", fontsize=8.6, color=estilo.COLOR_TECHO)

    ax3.set_xticks(xs)
    ax3.set_xticklabels([f"{n}\n{'pas.' if s == 'PAST' else 'fut.'}" for n, s in claves],
                        fontsize=9)
    ax3.set_ylabel("fracción de la varianza de $\\ell$")
    ax3.set_ylim(0, 1.30)
    ax3.set_xlim(-0.5, len(claves) - 0.5)
    ax3.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    # Sin leyenda: las dos bandas se rotulan sobre sí mismas.
    medio = (len(claves) - 1) / 2
    ax3.text(medio, np.mean(dentro) / 2, "varianza DENTRO del bin\ninvisible al observador",
             ha="center", va="center", color="white", fontsize=9.6, fontweight="bold",
             zorder=6)
    ax3.text(medio, np.mean(dentro) + np.mean(fuera) / 2,
             "ENTRE bins — todo lo utilizable", ha="center", va="center",
             color="white", fontsize=9.6, fontweight="bold", zorder=6)
    ax3.set_title("C. $\\rho_{\\max} = \\sqrt{SSB/SST}$, identidad exacta", loc="left")

    fig.suptitle("El canal observable es una sola variable discreta, y no lleva "
                 "la duración dentro",
                 x=0.005, ha="left", fontsize=13.5, y=1.005)
    estilo.nota_al_pie(fig, "p1a_representaciones_intervalos_d2.csv (SHA-256 verificado) · "
                            "ANOVA recalculado, contrastado contra "
                            "p1a_count_volume_canal_sigma_m_d2.py")
    fig.tight_layout(rect=(0, 0.02, 1, 0.985))

    return fig, {
        f"SSW/SST n={N_PANEL} {LADO_PANEL}": a["t_emp"],
        f"rho_max n={N_PANEL} {LADO_PANEL}": a["rho_max"],
        "SSW/SST rango sobre los seis estratos":
            (min(dentro), max(dentro)),
        "m observados en el estrato del panel A": a["K"],
        "violines que contienen la mediana global": compatibles,
    }


if __name__ == "__main__":
    f, numeros = dibujar()
    print(estilo.guardar(f, "fig03_canal_sigma_m"))
    for k, v in numeros.items():
        print(f"  {k:44s} {v}")
