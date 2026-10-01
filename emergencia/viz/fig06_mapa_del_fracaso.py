"""Fig. 6 — El mapa: qué se intentó, en qué orden, y dónde murió cada cosa.

Las cinco figuras anteriores miden. Ésta ordena: es el recorrido completo de la línea
`emergencia` en una imagen, con el estado de cada tramo y el número que lo cerró.

Sirve para dos cosas concretas:

1. **Ver la forma del fracaso.** No fue un fallo aislado: son las once etapas que
   `HOJA_DE_RUTA.md` §2–§3 y §17–§19 registran — las siete fases `Fase 0`–`Fase 6`
   más las tres del ramal `COUNT_VOLUME` (`CV-4.1`, `CV-4.3`, `§18`)—, todas contra
   el mismo obstáculo. El recuento del título se calcula sobre la propia lista de
   etapas y aborta si deja de describir el diagrama. La columna de la derecha
   enseña que cada
   representación nueva mejoró la correlación —`0.27 → 0.47 → 0.57`— y que ninguna
   se acercó al gate. Una serie que mejora y no llega es más peligrosa que una que
   no mejora: invita a probar la siguiente.
2. **Ver dónde se fue el tiempo.** El corchete marca el tramo `B_n`, que existió
   entero porque se leyó una cota superior como si fuera el máximo alcanzable.

Los valores de correlación no están escritos a mano: se leen del CSV sellado al
dibujar. Los estados sí son textuales, y su fuente es `HOJA_DE_RUTA.md` §2–§3 y §17–§19.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

import datos
import estilo

CERRADO = "#B03030"
APARCADO = "#C98A00"
VIVO = "#1B7F5A"
NEUTRO = "#4A4A4A"


def _rango(metricas, repr_):
    sub = metricas[metricas["representation"] == repr_]["pearson_correlation"]
    return sub.min(), sub.max()


def dibujar():
    metricas, intervalos = datos.representaciones()
    comparacion = datos.leer("p1a_comparacion_selectores_d2.csv")

    h = _rango(metricas, "HEIGHT_ONLY")
    hw = _rango(metricas, "HEIGHT_WIDTH")
    cv = _rango(metricas, "COUNT_VOLUME")
    techos = [datos.anova_sigma_m(intervalos, *e)["rho_max"] for e in datos.estratos()]
    disp = comparacion[(comparacion["selector"] == "MIN_COVERAGE_LEX")
                       & (comparacion["n"] == 128)]["p_unique"].item()

    # Las representaciones deben ir de peor a mejor: si esto dejara de cumplirse,
    # la lectura «la serie mejoraba y aun así no llegaba» sería falsa.
    if not (h[1] < hw[1] < cv[1]):
        raise ValueError(f"el orden de las representaciones no es el descrito: "
                         f"{h}, {hw}, {cv}")

    etapas = [
        ("Fase 0", "No-go de escala absoluta bajo $N=n$",
         "demostrado — condicionar a $N=n$ borra la escala", CERRADO, ""),
        ("Fase 1", "Selección intrínseca de dos intervalos",
         "construida, con abstención por empate", VIVO, ""),
        ("Fase 2", "Puerta teórica y disponibilidad en $d=2$",
         f"disponible: $P=${disp:.3f} a $n=128$", VIVO, ""),
        ("Fase 3", "$F_{cov,3}$ como vía métrica",
         "cerrada — soporte menor degenerado", CERRADO, ""),
        ("Fase 4", "MIN_ONLY  vs  MIN_COVERAGE_LEX",
         "MIN_ONLY descartado; LEX pasa a selector de trabajo", VIVO, ""),
        ("Fase 5", "HEIGHT_ONLY  $=H/2\\sqrt{n}$",
         f"aparcada — $\\rho = {h[0]:.2f}$–{h[1]:.2f}", APARCADO,
         f"{h[1]:.2f}"),
        ("Fase 6", "HEIGHT_WIDTH  $=(H+W)/4\\sqrt{n}$",
         f"aparcada — $\\rho = {hw[0]:.2f}$–{hw[1]:.2f}", APARCADO,
         f"{hw[1]:.2f}"),
        ("Fase 6", "COUNT_VOLUME  $=\\sqrt{(m-2)/(n-2)}$",
         f"la mejor de las tres — $\\rho = {cv[0]:.2f}$–{cv[1]:.2f}", APARCADO,
         f"{cv[1]:.2f}"),
        ("CV-4.1", "Cota de resolución $B_n$ sobre $F_{relax}$",
         "correcta, pero floja ×2.3–2.6 y fuera del camino", NEUTRO, ""),
        ("CV-4.3", "Apretar $F_{relax}$ por arriba",
         f"vía descartada por teorema — factor máx. ×{datos.FACTOR_MAX_APRIETE}",
         CERRADO, ""),
        ("§18", "El canal es $\\sigma(m)$: identidad ANOVA exacta",
         f"gate EXCLUIDO en la muestra sellada — "
         f"$\\rho_{{\\max}} = {min(techos):.3f}$–{max(techos):.3f}", CERRADO,
         f"{max(techos):.2f}"),
    ]

    estilo.use_style()
    fig, ax = plt.subplots(figsize=(13.4, 9.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.4, len(etapas) + 0.4)
    ax.axis("off")
    ax.invert_yaxis()

    for k, (fase, intento, salida, color, marca) in enumerate(etapas):
        y = k
        ax.add_patch(FancyBboxPatch((1.25, y - 0.33), 6.05, 0.66,
                                    boxstyle="round,pad=0.02,rounding_size=0.08",
                                    facecolor=color, alpha=0.10,
                                    edgecolor=color, lw=1.4, zorder=2))
        ax.text(0.95, y, fase, ha="right", va="center", fontsize=9.4,
                color=NEUTRO, fontweight="bold")
        ax.text(1.45, y - 0.10, intento, ha="left", va="center", fontsize=10.4,
                color="#111")
        ax.text(1.45, y + 0.17, salida, ha="left", va="center", fontsize=8.8,
                color=color)
        if k + 1 < len(etapas):
            ax.add_patch(FancyArrowPatch((4.2, y + 0.34), (4.2, y + 0.66),
                                         arrowstyle="-|>", mutation_scale=11,
                                         color=NEUTRO, lw=1.1, zorder=1))

    # ------------------------------------------------- escala de correlación
    x0, x1 = 7.7, 9.7
    def a_x(rho):
        return x0 + (x1 - x0) * rho / 0.9

    ax.plot([x0, x1], [-0.30, -0.30], color=NEUTRO, lw=1.2)
    for rho in (0.0, 0.3, 0.6, 0.9):
        ax.plot([a_x(rho), a_x(rho)], [-0.30, -0.42], color=NEUTRO, lw=1.0)
        ax.text(a_x(rho), -0.55, f"{rho:.1f}", ha="center", va="bottom", fontsize=8.4,
                color=NEUTRO)
    ax.text((x0 + x1) / 2, -0.95, "correlación con la duración latente",
            ha="center", va="bottom", fontsize=9.4, color=NEUTRO)

    ax.plot([a_x(datos.GATE)] * 2, [-0.30, len(etapas) - 0.6],
            color=estilo.COLOR_GATE, lw=2.2, zorder=3)
    ax.text(a_x(datos.GATE) + 0.06, len(etapas) - 0.55, "gate 0.80", ha="left",
            va="bottom", fontsize=9.6, color=estilo.COLOR_GATE, fontweight="bold")

    for k, (_, _, _, color, marca) in enumerate(etapas):
        if not marca:
            continue
        valor = float(marca)
        ax.plot([x0, a_x(valor)], [k, k], color=color, lw=3.0,
                solid_capstyle="butt", zorder=3)
        ax.scatter([a_x(valor)], [k], s=70, color=color, zorder=4)
        ax.text(a_x(valor) + 0.07, k, f"{valor:.2f}", va="center", fontsize=8.8,
                color=color)

    # ------------------------------------------------- corchete del desvío
    # El corchete va en el carril de correlación, que en estas dos filas está
    # vacío: no hay ninguna correlación que dibujar en el tramo del desvío.
    ax.plot([7.42, 7.56, 7.56, 7.42], [7.62, 7.62, 9.38, 9.38],
            color=estilo.RED, lw=1.6)
    ax.text(7.66, 8.5,
            "el desvío: este tramo existió entero\n"
            "porque $\\rho^{ub}_{\\max}(B_n) = 0.83$–0.86\n"
            "se leyó como el máximo real,\n"
            "y $0.83 > 0.80$",
            ha="left", va="center", fontsize=8.8, color=estilo.RED)

    ax.text(1.25, len(etapas) - 0.35,
            "Cada representación nueva mejoró la anterior. Ninguna se acercó al gate,\n"
            "y la última resultó estar ya pegada al techo del canal.",
            ha="left", va="top", fontsize=9.6, color="#111")

    # El título lleva números, luego los números se cuentan sobre la propia lista
    # y no se escriben a mano (auditoría 032, hallazgo 4).
    fases = sorted({f for f, *_ in etapas if f.startswith("Fase")})
    ramal = [f for f, *_ in etapas if not f.startswith("Fase")]
    if (len(etapas), len(fases), len(ramal)) != (11, 7, 3):
        raise ValueError(f"el recuento del título no describe el diagrama: "
                         f"{len(etapas)} etapas, {len(fases)} fases, {len(ramal)} del ramal")

    fig.suptitle(f"Trayectoria del programa: {len(etapas)} etapas — "
                 f"{len(fases)} fases y el ramal COUNT_VOLUME",
                 x=0.02, ha="left", fontsize=14, y=0.985)
    estilo.nota_al_pie(fig, "correlaciones de p1a_representaciones_metricas_d2.csv · "
                            "techo recalculado del CSV de intervalos · "
                            "estados de HOJA_DE_RUTA.md §2–§3, §17–§19")
    fig.tight_layout(rect=(0, 0.02, 1, 0.97))

    return fig, {
        "HEIGHT_ONLY rho": h,
        "HEIGHT_WIDTH rho": hw,
        "COUNT_VOLUME rho": cv,
        "techo del canal": (min(techos), max(techos)),
        "disponibilidad LEX n=128": disp,
        "etapas dibujadas": len(etapas),
    }


if __name__ == "__main__":
    f, numeros = dibujar()
    print(estilo.guardar(f, "fig06_mapa_del_fracaso"))
    for k, v in numeros.items():
        print(f"  {k:30s} {v}")
