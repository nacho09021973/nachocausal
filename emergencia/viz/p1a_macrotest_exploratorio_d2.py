"""Three diagnostic figures for the exact post-hoc thinning macrotest."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from emergencia import p1a_macrotest_exploratorio_d2 as macrotest  # noqa: E402

import estilo  # noqa: E402


PHASE = macrotest.PHASE
NP_PATH = ROOT / "emergencia/resultados" / macrotest.NP_FILENAME
NK_PATH = ROOT / "emergencia/resultados" / macrotest.NK_FILENAME
COLORS = {6: estilo.BLUE, 7: estilo.ORANGE, 8: estilo.GREEN, 9: estilo.PURPLE}
MARKERS = {6: "o", 7: "s", 8: "^", 9: "D"}


def _read(path: Path) -> list[dict[str, str]]:
    macrotest._verify_sidecar(path)
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _footer(fig, source: str) -> None:
    estilo.nota_al_pie(fig, f"PHASE={PHASE} · {source} (SHA-256 verificado)")


def figure_u(np_rows: list[dict[str, str]]):
    estilo.use_style()
    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    for n in macrotest.EXACT_N:
        rows = [row for row in np_rows if int(row["n"]) == n]
        ax.plot(
            [float(row["p"]) for row in rows],
            [float(row["U_orbital"]) for row in rows],
            color=COLORS[n], marker=MARKERS[n], ms=4.2, lw=1.8, label=f"n={n}",
        )
    ax.set_xlabel("retención $p$  (densidad relativa)")
    ax.set_ylabel("$U_n(p)$ — unicidad orbital absoluta")
    ax.set_xlim(-0.01, 1.01)
    ax.set_ylim(bottom=-0.001)
    ax.set_title("Macrotest exacto: unicidad orbital tras thinning", loc="left")
    ax.legend(title="población uniforme")
    _footer(fig, macrotest.NP_FILENAME)
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    return fig


def figure_availability(np_rows: list[dict[str, str]]):
    estilo.use_style()
    fig, (ax_e, ax_c) = plt.subplots(1, 2, figsize=(12.2, 4.9))
    for n in macrotest.EXACT_N:
        rows = [row for row in np_rows if int(row["n"]) == n]
        p = [float(row["p"]) for row in rows]
        e = [float(row["E_available"]) for row in rows]
        available_rows = [row for row in rows if row["U_orbital_given_available"] != "NA"]
        ax_e.plot(p, e, color=COLORS[n], marker=MARKERS[n], ms=3.8, lw=1.7, label=f"n={n}")
        ax_c.plot(
            [float(row["p"]) for row in available_rows],
            [float(row["U_orbital_given_available"]) for row in available_rows],
            color=COLORS[n], marker=MARKERS[n], ms=3.8, lw=1.7, label=f"n={n}",
        )
    ax_e.set_xlabel("retención $p$")
    ax_e.set_ylabel("$E_n(p)$")
    ax_e.set_title("A. Disponibilidad de candidato", loc="left")
    ax_e.set_xlim(-0.01, 1.01)
    ax_e.set_ylim(bottom=-0.001)
    ax_c.set_xlabel("retención $p$")
    ax_c.set_ylabel(r"$U_n^\star(p)=U_n(p)/E_n(p)$")
    ax_c.set_title("B. Unicidad orbital si hay candidato", loc="left")
    ax_c.set_xlim(0.09, 1.01)
    ax_c.set_ylim(0.84, 1.01)
    ax_c.legend(title="población uniforme")
    fig.suptitle("No confundir éxito absoluto con éxito condicionado", x=0.01, ha="left")
    _footer(fig, macrotest.NP_FILENAME)
    fig.tight_layout(rect=(0, 0.035, 1, 0.96))
    return fig


def figure_k(nk_rows: list[dict[str, str]]):
    estilo.use_style()
    fig, (ax_a, ax_c) = plt.subplots(1, 2, figsize=(12.2, 4.9))
    for n in macrotest.EXACT_N:
        rows = [
            row for row in nk_rows
            if int(row["n"]) == n and int(row["k_retained"]) >= macrotest.MIN_SUPPORT
        ]
        k = [int(row["k_retained"]) for row in rows]
        ax_a.plot(
            k, [float(row["u_orbital_given_k"]) for row in rows],
            color=COLORS[n], marker=MARKERS[n], mfc="white", ms=7.5, lw=1.2,
            label=f"$u_{{{n},k}}$",
        )
        ax_a.plot(
            k, [float(row["e_available_given_k"]) for row in rows],
            color=COLORS[n], marker=MARKERS[n], mfc=COLORS[n], ms=4.2, lw=1.2,
        )
        ax_c.plot(
            k, [float(row["u_orbital_given_available_and_k"]) for row in rows],
            color=COLORS[n], marker=MARKERS[n], mfc="white", ms=7.5, lw=1.2,
            label=f"n={n}",
        )
    ax_a.set_xlabel("número real de supervivientes $k$")
    ax_a.set_ylabel("probabilidad condicionada a $K=k$")
    ax_a.set_title("A. Orbital (hueco) y disponible (relleno)", loc="left")
    ax_a.set_xticks([6, 7, 8, 9])
    ax_a.legend(title="tamaño original")
    ax_c.set_xlabel("número real de supervivientes $k$")
    ax_c.set_ylabel(r"$P(r_{orb}=1\mid M\ne\varnothing,K=k)$")
    ax_c.set_title("B. Condicionada a disponibilidad", loc="left")
    ax_c.set_xticks([6, 7, 8, 9])
    ax_c.set_ylim(0.84, 1.01)
    ax_c.legend(title="tamaño original")
    fig.suptitle("Consistencia exacta: a igual $k$, todas las poblaciones coinciden", x=0.01, ha="left")
    _footer(fig, macrotest.NK_FILENAME + " · 34/34 celdas exactas")
    fig.tight_layout(rect=(0, 0.035, 1, 0.96))
    return fig


def _save_new(fig, name: str) -> Path:
    estilo.SALIDA.mkdir(exist_ok=True)
    path = estilo.SALIDA / f"{name}.png"
    if path.exists():
        raise FileExistsError(f"refusing to overwrite {path}")
    fig.savefig(path, metadata={"Phase": PHASE, "Source": "exact frozen coefficients"})
    plt.close(fig)
    return path


def main() -> int:
    np_rows = _read(NP_PATH)
    nk_rows = _read(NK_PATH)
    outputs = (
        _save_new(figure_u(np_rows), "fig07_macrotest_u_orbital"),
        _save_new(figure_availability(np_rows), "fig08_macrotest_disponibilidad_condicionada"),
        _save_new(figure_k(nk_rows), "fig09_macrotest_k_consistencia"),
    )
    for output in outputs:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
