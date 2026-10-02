"""Single authorized figure for the post-hoc large-n orbital baseline."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from emergencia import p1a_large_n_orbital_baseline_d2 as baseline  # noqa: E402

import estilo  # noqa: E402


PHASE = baseline.PHASE
CSV_PATH = baseline.RESULTS_DIR / baseline.CSV_FILENAME
OUTPUT_NAME = "fig10_large_n_orbital_baseline"


def _rows() -> list[dict[str, str]]:
    baseline._verify_sidecar(CSV_PATH)
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows or any(row["PHASE"] != PHASE for row in rows):
        raise RuntimeError("large-n figure received missing or wrong phase metadata")
    return rows


def draw():
    rows = sorted(_rows(), key=lambda row: int(row["n"]))
    exact = [row for row in rows if row["method"] == "EXACT"]
    mc = [row for row in rows if row["method"] == "MONTE_CARLO"]
    series = (
        ("$U_n$ — unicidad orbital absoluta", "U_hat", "U_ci95_low", "U_ci95_high", estilo.BLUE),
        ("$E_n$ — disponibilidad", "E_hat", "E_ci95_low", "E_ci95_high", estilo.ORANGE),
        ("$U_n^\\star$ — unicidad si disponible", "U_star_hat", "U_star_ci95_low", "U_star_ci95_high", estilo.PURPLE),
    )

    estilo.use_style()
    fig, ax = plt.subplots(figsize=(10.2, 5.8))
    for label, value, low, high, color in series:
        x = [int(row["n"]) for row in rows]
        y = [float(row[value]) for row in rows]
        ax.plot(x, y, color=color, lw=1.9, label=label, zorder=2)
        ax.scatter(
            [int(row["n"]) for row in exact],
            [float(row[value]) for row in exact],
            marker="o", s=55, facecolors="white", edgecolors=color, linewidths=1.7,
            zorder=4,
        )
        mc_x = [int(row["n"]) for row in mc]
        mc_y = [float(row[value]) for row in mc]
        yerr = [
            [float(row[value]) - float(row[low]) for row in mc],
            [float(row[high]) - float(row[value]) for row in mc],
        ]
        ax.errorbar(
            mc_x, mc_y, yerr=yerr, fmt="o", color=color, mfc=color, mec="white",
            mew=0.8, ms=6.5, capsize=3, lw=1.2, zorder=5,
        )

    ax.set_xlabel("tamaño del poset $n$")
    ax.set_ylabel("probabilidad")
    ax.set_xticks([6, 7, 8, 9, 10, 12, 16, 24, 32])
    ax.set_ylim(-0.025, 1.035)
    ax.set_title("Baseline orbital post-hoc: exacta hasta 9, Monte Carlo hasta 32", loc="left")
    ax.legend(loc="best")
    ax.text(
        0.99, 0.02,
        "hueco: exacto · relleno + Wilson 95%: Monte Carlo (100 000 por n)",
        transform=ax.transAxes, ha="right", va="bottom", fontsize=8.2, color=estilo.GREY,
    )
    estilo.nota_al_pie(
        fig,
        f"PHASE={PHASE} · {baseline.CSV_FILENAME} (SHA-256 verificado) · sin ajuste asintótico",
    )
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    return fig


def main() -> int:
    output = estilo.SALIDA / f"{OUTPUT_NAME}.png"
    if output.exists():
        raise FileExistsError(f"refusing to overwrite {output}")
    fig = draw()
    fig.savefig(output, metadata={"Phase": PHASE, "Claim": "finite-n descriptive only"})
    plt.close(fig)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
